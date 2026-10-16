"""Capture each site's case pack (step 6 of the TCU build). Run on the build machine only.

python tcu/engine/data_profile.py <slug> [...] | --all

Reads, read only: tcu/registry.yaml; H:/raw-data (climate-projections cache,
fema-nri, census-tiger tracts, alaska-context). Fetches public services for the
campus point: EPA Level III and IV ecoregions, USGS Watershed Boundary
Dataset, and GBIF occurrence facets (species counts). Writes
private/tcu/<slug>/data/<name>.csv|.json with <name>.meta.json, a data README,
and seeds private/tcu/<slug>/site.yaml (fact slots) if it does not exist.
Every view is a SNAPSHOT; a missing source is written as unknown, never zero.
"""
import csv
import datetime
import hashlib
import io
import json
import math
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RAW = Path('H:/raw-data')
SITES = ROOT / 'private' / 'tcu'
UA = {'User-Agent': 'tcu-template-build (education research script)'}
VARS = [  # cache variable, file name, title, unit
    ('Average Temperature [degF]', 'proj-avg-temp', 'Average temperature', 'degrees F'),
    ('Annual Precipitation [in]', 'proj-annual-precip', 'Annual precipitation', 'inches'),
    ('Number of Frost Free Days', 'proj-frost-free', 'Frost-free days per year', 'days'),
    ('Normal Length of Growing Season [days]', 'proj-growing-season', 'Length of the growing season', 'days'),
    ('Annual Frozen Precipitation [in]', 'proj-frozen-precip', 'Frozen precipitation (snow and ice) per year', 'inches of water'),
    ('Maximum 3-Day Precipitation [in]', 'proj-max-3day-precip', 'Largest 3-day precipitation total each year', 'inches'),
    ('Number of Days >= 100 \u00b0F', 'proj-days-100f', 'Days at or above 100 degrees F', 'days'),
]
NRI_HAZ = {'AVLN': 'Avalanche', 'CFLD': 'Coastal flooding', 'CWAV': 'Cold wave', 'DRGT': 'Drought', 'ERQK': 'Earthquake',
           'HAIL': 'Hail', 'HWAV': 'Heat wave', 'HRCN': 'Hurricane', 'ISTM': 'Ice storm', 'LNDS': 'Landslide',
           'LTNG': 'Lightning', 'RFLD': 'Riverine flooding', 'SWND': 'Strong wind', 'TRND': 'Tornado', 'TSUN': 'Tsunami',
           'VLCN': 'Volcanic activity', 'WFIR': 'Wildfire', 'WNTW': 'Winter weather'}
GBIF_GROUPS = [('plants', 'kingdomKey', 6), ('birds', 'classKey', 212), ('mammals', 'classKey', 359),
               ('ray-finned fishes', 'classKey', 204), ('amphibians', 'classKey', 131), ('reptiles', 'classKey', 358),
               ('insects', 'classKey', 216)]
NOW = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
_species_cache_p = SITES / '_sources' / 'gbif-species-cache.json'
_species = json.loads(_species_cache_p.read_text(encoding='utf-8')) if _species_cache_p.exists() else {}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def get_json(url, tries=3):
    for k in range(tries):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
        except Exception as e:  # network: retry, then report unknown
            err = e
            time.sleep(2 * (k + 1))
    raise RuntimeError(f'{url[:90]}: {err}')


def write_pack(d, name, data, ext, meta):
    d.mkdir(parents=True, exist_ok=True)
    (d / f'{name}.{ext}').write_bytes(data)
    meta = {'label': 'SNAPSHOT', **meta, 'captured_at': NOW, 'sha256': sha(data)}
    (d / f'{name}.meta.json').write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding='utf-8')
    return name


def csv_bytes(rows):
    b = io.StringIO()
    w = csv.DictWriter(b, fieldnames=list(rows[0]), lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    return b.getvalue().encode('utf-8')


# ---------- projections (raw-data cache) ----------
def projections(site, d, notes):
    cu = site['climate_unit']
    slug = cu.get('cache_slug')
    if not slug:
        notes.append(f"Projections: no projection in raw-data for this site's climate unit ({cu['area']}); {cu['why']}")
        return []
    import pyarrow.parquet as pq
    src = RAW / 'climate-projections' / 'cache' / f'{slug}.smoothed.parquet'
    meta_src = json.loads((RAW / 'climate-projections' / 'cache' / f'{slug}.meta.json').read_text(encoding='utf-8'))
    t = pq.read_table(src).to_pylist()
    src_sha = sha(src.read_bytes())
    made, card = [], []
    for var, name, title, unit in VARS:
        # the degree sign in one cache name is not reliably encoded, so match on the text before it
        rows = [r for r in t if r['variable'] == var or (var.startswith('Number of Days >= 100') and r['variable'].startswith('Number of Days >= 100'))]
        if not rows:
            notes.append(f'Projections: variable "{var}" not in the cache file for {slug} (unknown).')
            continue
        by = {}
        for r in rows:
            k = 'ssp245' if r['scenario'] == 'ssp245' else 'ssp370'
            by.setdefault(r['year'], {})[k] = r
        out = []
        for y in sorted(by):
            o = {'year': y}
            for k in ('ssp245', 'ssp370'):
                r = by[y].get(k)
                o[k] = '' if r is None else round(r['value'], 3)
                o[k + '_p25'] = '' if r is None else round(r['p25'], 3)
                o[k + '_p75'] = '' if r is None else round(r['p75'], 3)
            out.append(o)
        b0, b1 = meta_src['baseline_window']
        mean = lambda k, a, z: (lambda v: round(sum(v) / len(v), 2) if v else '')([o[k] for o in out if a <= o['year'] <= z and o[k] != ''])
        for k, lab in (('ssp245', 'SSP2-4.5'), ('ssp370', 'SSP3-7.0')):
            base = mean(k, b0, b1)
            w = meta_src['future_windows']
            mid, late = mean(k, *w['2050']), mean(k, *w['2080'])
            card.append({'variable': title, 'unit': unit, 'scenario': lab, f'baseline_{b0}_{b1}': base,
                         f'mean_{w["2050"][0]}_{w["2050"][1]}': mid, f'mean_{w["2080"][0]}_{w["2080"][1]}': late,
                         'change_mid': round(mid - base, 2) if '' not in (mid, base) else '',
                         'change_late': round(late - base, 2) if '' not in (late, base) else ''})
        made.append(write_pack(d, name, csv_bytes(out), 'csv', {
            'title': f'{title}, {cu["area"]} (projection, not a prediction)',
            'source': meta_src.get('source', 'not stated'), 'issuer': 'University of Montana Native Climate (as the raw-data cache states the source)',
            'unit': unit, 'scenarios': ['SSP2-4.5 (Middle of the Road)', 'SSP3-7.0 (High Emissions)'],
            'models': meta_src.get('models'), 'n_models': meta_src.get('n_models'),
            'baseline_window': meta_src['baseline_window'], 'future_windows': meta_src['future_windows'],
            'license': 'not stated in raw-data', 'derived_from': f'H:/raw-data/climate-projections/cache/{slug}.smoothed.parquet (sha256 {src_sha[:16]})',
            'note': ('Projection, not a prediction. Values are the cache file\'s smoothed multi-model middle, with the 25th to 75th '
                     'percentile band across models; the smoothing method is not stated in raw-data. A public data view of the '
                     f'{cu["area"]}, not any Nation\'s voice; C2 until reviewed.'),
            'view': {'type': 'series', 'x': 'year', 'unit': unit, 'baseline': meta_src['baseline_window'], 'series': [
                {'name': 'SSP2-4.5 (Middle of the Road)', 'y': 'ssp245', 'lo': 'ssp245_p25', 'hi': 'ssp245_p75'},
                {'name': 'SSP3-7.0 (High Emissions)', 'y': 'ssp370', 'lo': 'ssp370_p25', 'hi': 'ssp370_p75'}]}}))
    if card:
        made.append(write_pack(d, 'projection-card', csv_bytes(card), 'csv', {
            'title': f'Projection card, {cu["area"]}: window means from the smoothed series',
            'source': meta_src.get('source', 'not stated'), 'issuer': 'Derived by the TCU build from the raw-data cache',
            'unit': 'per row', 'scenarios': ['SSP2-4.5', 'SSP3-7.0'], 'baseline_window': meta_src['baseline_window'],
            'future_windows': meta_src['future_windows'], 'license': 'not stated in raw-data',
            'derived_from': f'proj-*.csv in this pack', 'note': 'Means of the smoothed yearly values inside each window. Projection, not a prediction.'}))
    return made


# ---------- FEMA NRI (raw-data covers AK, AZ, OK, VA only) ----------
def nri(site, pt, d, notes):
    fips = {'AK': '02', 'AZ': '04', 'OK': '40', 'VA': '51'}.get(site['state'])
    if not fips or not pt:
        notes.append(f"Hazards: FEMA National Risk Index tracts in raw-data cover AK, AZ, OK, and VA only; {site['state']} is unknown here.")
        return []
    import pyogrio.raw
    import shapely
    from shapely.geometry import Point
    meta, _, geom, fields = pyogrio.raw.read(f'zip://{RAW}/census-tiger/TIGER2024-TRACT/tl_2024_{fips}_tract.zip', columns=['GEOID'])
    gs = shapely.from_wkb(geom)
    P = Point(pt[1], pt[0])
    hit = [fields[0][i] for i in range(len(gs)) if gs[i].contains(P)]
    if not hit:
        notes.append('Hazards: no census tract contains the point (unknown).')
        return []
    tract = hit[0]
    src = RAW / 'fema-nri' / 'v1.20-hosted-2026-10-12' / f"NRI_Table_CensusTracts_{site['state']}.csv"
    row = next((r for r in csv.DictReader(src.open(encoding='utf-8-sig')) if r.get('TRACTFIPS') == tract), None)
    if row is None:
        notes.append(f'Hazards: tract {tract} not found in the NRI table (unknown).')
        return []
    rows = [{'measure': 'Overall risk', 'rating': row.get('RISK_RATNG', '')},
            {'measure': 'Expected annual loss', 'rating': row.get('EAL_RATNG', '')},
            {'measure': 'Social vulnerability', 'rating': row.get('SOVI_RATNG', '')},
            {'measure': 'Community resilience', 'rating': row.get('RESL_RATNG', '')}]
    rows += [{'measure': name, 'rating': row.get(f'{k}_RISKR', '')} for k, name in NRI_HAZ.items()]
    srcj = json.loads((src.parent / 'source.json').read_text(encoding='utf-8'))
    return [write_pack(d, 'nri-tract', csv_bytes(rows), 'csv', {
        'title': f'FEMA National Risk Index ratings, census tract {tract}',
        'source': f"{srcj.get('release', 'National Risk Index')} ({srcj.get('layer', '')})", 'issuer': 'FEMA',
        'unit': 'rating words as published', 'license': 'not stated in raw-data',
        'derived_from': f'{src.as_posix()} (sha256 {sha(src.read_bytes())[:16]})',
        'note': 'Ratings compare this tract with others in the nation. A blank rating is unknown, never zero. The tract holding the point is not the whole community.'})]


# ---------- public services ----------
def arcgis_point(base, layer, pt):
    q = urllib.parse.urlencode({'geometry': f'{pt[1]},{pt[0]}', 'geometryType': 'esriGeometryPoint', 'inSR': 4326,
                                'spatialRel': 'esriSpatialRelIntersects', 'outFields': '*', 'returnGeometry': 'false', 'f': 'json'})
    url = f'{base}/{layer}/query?{q}'
    return url, get_json(url)


def ecoregion(pt, d, notes):
    base = 'https://geodata.epa.gov/arcgis/rest/services/ORD/USEPA_Ecoregions_Level_III_and_IV/MapServer'
    out = {}
    for lvl, layer in (('l3', 11), ('l4', 7)):
        url, j = arcgis_point(base, layer, pt)
        f = (j.get('features') or [{}])[0].get('attributes', {})
        out[lvl] = {k: v for k, v in f.items() if k.upper() in ('US_L3NAME', 'US_L3CODE', 'US_L4NAME', 'US_L4CODE', 'NA_L2NAME', 'NA_L1NAME', 'L3_KEY', 'L4_KEY')}
        out[lvl + '_url'] = url
    if not out['l3']:
        notes.append('Ecoregion: the EPA conterminous United States service returned none for this point (unknown; Alaska uses a separate ecoregion map).')
    write_pack(d, 'ecoregion', json.dumps(out, indent=1).encode(), 'json', {
        'title': 'EPA ecoregions at the campus point', 'source': base, 'issuer': 'U.S. EPA Office of Research and Development',
        'unit': 'names and codes', 'license': 'not stated on the service (U.S. government work; terms not opened)'})
    return out


def watershed(pt, d, notes):
    base = 'https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer'
    out = {}
    for lvl, layer in (('huc8', 4), ('huc10', 5), ('huc12', 6)):
        url, j = arcgis_point(base, layer, pt)
        f = (j.get('features') or [{}])[0].get('attributes', {})
        out[lvl] = {'name': f.get('name'), 'code': f.get(lvl)}
        out[lvl + '_url'] = url
    if not out['huc8'].get('name'):
        notes.append('Watershed: the USGS WBD service returned none for this point (unknown).')
    write_pack(d, 'watershed', json.dumps(out, indent=1).encode(), 'json', {
        'title': 'USGS Watershed Boundary Dataset units at the campus point', 'source': base, 'issuer': 'U.S. Geological Survey',
        'unit': 'names and hydrologic unit codes', 'license': 'not stated on the service (USGS data are generally public domain; terms page not opened)'})
    return out


def species(pt, d, notes):
    lat, lon = pt
    dlat, dlon = 10 / 110.57, 10 / (111.32 * math.cos(math.radians(lat)))
    ring = [(lon + dlon * math.cos(a * math.pi / 8), lat + dlat * math.sin(a * math.pi / 8)) for a in range(16)]
    ring.append(ring[0])
    wkt = 'POLYGON((' + ','.join(f'{x:.5f} {y:.5f}' for x, y in reversed(ring)) + '))'
    rows = []
    for group, key, val in GBIF_GROUPS:
        q = urllib.parse.urlencode({'geometry': wkt, key: val, 'facet': 'speciesKey', 'facetLimit': 12, 'limit': 0,
                                    'occurrenceStatus': 'PRESENT'})
        j = get_json('https://api.gbif.org/v1/occurrence/search?' + q)
        counts = (j.get('facets') or [{}])[0].get('counts', [])
        if not counts:
            rows.append({'group': group, 'scientific_name': '', 'common_name': '', 'records': ''})
        for c in counts:
            k = c['name']
            if k not in _species:
                s = get_json(f'https://api.gbif.org/v1/species/{k}')
                _species[k] = {'sci': s.get('canonicalName') or s.get('scientificName', ''), 'common': s.get('vernacularName', '')}
            rows.append({'group': group, 'scientific_name': _species[k]['sci'], 'common_name': _species[k]['common'], 'records': c['count']})
    return write_pack(d, 'species-gbif', csv_bytes(rows), 'csv', {
        'title': 'Most-recorded species within about 10 km of the campus point, by group (GBIF)',
        'source': 'GBIF occurrence search API, facet by species, geometry = 16-sided polygon of about 10 km radius', 'issuer': 'GBIF.org (records from many publishing institutions)',
        'unit': 'occurrence records', 'license': 'records carry CC0 1.0, CC BY 4.0, or CC BY-NC 4.0 per publishing dataset; GBIF asks users to cite a download DOI, which a facet query does not create',
        'note': ('Record counts show where people looked and reported, not how many live here. A species missing from this list is '
                 'unknown here, never absent. A list of species is not a list of relationships: any cultural relationship stays with the Nation.')})


def seed_site(sd, site, eco, ws, notes):
    p = sd / 'site.yaml'
    if p.exists():
        return
    l3 = (eco or {}).get('l3', {})
    l4 = (eco or {}).get('l4', {})
    fmt = lambda h: f"{h['name']} ({h['code']})" if h and h.get('name') else 'unknown'
    cu = site['climate_unit']
    y = {
        'schema': 'tcu-site/v1', 'slug': site['slug'], 'draft': True,
        'institution': {'name': site['name'] if site['kind'] == 'TCU' else f"{site['institution']}, {site['name']}",
                        'short_name': 'unknown', 'kind': site['kind'], 'town': site['town'], 'state': site['state'],
                        'web': 'unknown', 'charter_statement': '[NEEDS TRIBAL CONFIRMATION: the Nation(s) whose homelands the campus is on]'},
        'place': {'county': site['county'], 'coordinates': site.get('coordinates', 'unknown'),
                  'ecoregion_l3': f"{l3.get('US_L3NAME')} (Level III {l3.get('US_L3CODE')})" if l3.get('US_L3NAME') else 'unknown',
                  'ecoregion_l4': f"{l4.get('US_L4NAME')} (Level IV {l4.get('US_L4CODE')})" if l4.get('US_L4NAME') else 'unknown',
                  'watershed_huc8': fmt((ws or {}).get('huc8')), 'watershed_huc10': fmt((ws or {}).get('huc10')),
                  'watershed_huc12': fmt((ws or {}).get('huc12')),
                  'climate_unit': f"{cu['area']} ({cu['basis']}; {cu['projection']})",
                  'homelands': '[NEEDS TRIBAL CONFIRMATION: the Nation(s) whose homelands the campus is on]'},
        'region': {'name': 'unknown', 'casc': 'unknown', 'state_climatologist': 'unknown', 'intertribal': 'unknown'},
        'case': {'shared': 'Columbia River Basin', 'local': 'unknown'},
        'sources': ['tcu/registry.yaml (public facts, 10/15/2026)', 'data/ecoregion.meta.json', 'data/watershed.meta.json'],
    }
    p.write_text('# Seeded by tcu/engine/data_profile.py; the deep-dive writer completes region, case, and institution slots.\n'
                 + yaml.safe_dump(y, allow_unicode=True, sort_keys=False, width=110), encoding='utf-8')


def profile(site):
    sd = SITES / site['slug']
    d = sd / 'data'
    d.mkdir(parents=True, exist_ok=True)
    notes, made = [], []
    pt = None
    c = site.get('coordinates')
    if isinstance(c, dict):
        pt = (c['lat'], c['lon'])
    elif isinstance(site.get('town_point'), dict):
        pt = (site['town_point']['lat'], site['town_point']['lon'])
        notes.append('Point: the campus location is unknown; the town point (Census Gazetteer) stands in for ecoregion, watershed, species, and tract.')
    else:
        notes.append('Point: no campus or town point; ecoregion, watershed, species, and tract are unknown.')
    made += projections(site, d, notes)
    eco = ws = None
    if pt:
        made += nri(site, pt, d, notes)
        for fn in (ecoregion, watershed):
            try:
                r = fn(pt, d, notes)
                eco = r if fn is ecoregion else eco
                ws = r if fn is watershed else ws
                made.append(fn.__name__)
            except Exception as e:
                notes.append(f'{fn.__name__}: service error, unknown ({e})')
        try:
            made.append(species(pt, d, notes))
        except Exception as e:
            notes.append(f'species: service error, unknown ({e})')
    if site['state'] == 'AK':
        ak = RAW / 'alaska-context' / '2026-10-12'
        f = ak / 'usdm_02185.json'
        if f.exists():
            made.append(write_pack(d, 'usdm-north-slope', f.read_bytes(), 'json', {
                'title': 'U.S. Drought Monitor, North Slope Borough (as captured in raw-data)', 'source': f.as_posix(),
                'issuer': 'U.S. Drought Monitor (National Drought Mitigation Center, USDA, NOAA)', 'unit': 'as in file',
                'license': 'not stated in raw-data'}))
        else:
            notes.append('Alaska context: no North Slope Borough drought file in raw-data (unknown).')
    seed_site(sd, site, eco, ws, notes)
    (d / 'README.md').write_text(f"# Case pack: {site['slug']}\n\nCaptured {NOW[5:7]}/{NOW[8:10]}/{NOW[:4]} by tcu/engine/data_profile.py. Every file has a "
                                 f".meta.json. SNAPSHOT only; nothing here runs live.\n\n## Files\n\n" + ''.join(f'- {m}\n' for m in made)
                                 + '\n## Unknowns and notes\n\n' + (''.join(f'- {n}\n' for n in notes) or '- none\n'), encoding='utf-8')
    return site['slug'], len(made), notes


def main(argv):
    reg = yaml.safe_load((ROOT / 'tcu' / 'registry.yaml').read_text(encoding='utf-8'))['sites']
    want = [s for s in reg if '--all' in argv or s['slug'] in argv]
    with ThreadPoolExecutor(6) as ex:
        for slug, n, notes in ex.map(profile, want):
            print(f'{slug}: {n} pack files; ' + ' | '.join(x[:90] for x in notes))
    _species_cache_p.parent.mkdir(parents=True, exist_ok=True)
    _species_cache_p.write_text(json.dumps(_species, ensure_ascii=False), encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1:])
