"""Build one TCU site: minisite, two single-file decks, two .pptx, and zips.

python tcu/engine/build.py <slug> [<slug> ...]     build sites under the sites folder
python tcu/engine/build.py --all                   build every site folder that has a site.yaml
python tcu/engine/build.py --sites <dir> <slug>    use another sites folder (a source kit uses ./sites)

Reads: tcu/core (shared), tcu/templates, and <sites>/<slug>/ (site.yaml,
deep-dive/, packet/, data/). Writes only <sites>/<slug>/build/.
"""
import base64
import csv
import datetime
import html
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

import yaml

ENGINE = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE))
import mdlite  # noqa: E402

TCU = ENGINE.parent
CORE = TCU / 'core'
TEMPLATES = TCU / 'templates'
FONTS = next((p for p in (TEMPLATES / 'fonts', TCU.parent / 'docs' / 'fonts') if p.is_dir()), None)
DEFAULT_SITES = next((p for p in (TCU.parent / 'private' / 'tcu', TCU / 'sites') if p.is_dir()), TCU / 'sites')
COURSES = {'ccic-200': 'CCIC 200: Climate Change in Indian Country', 'tcr-201': 'TCR 201: Tribal Climate Resilience'}
EYES = {'frog': "Frog's Eye", 'bird': "Bird's Eye", 'moon': "Moon's Eye"}
AUTHOR = ('Patrick A. Freeland (module author), with ATNI Climate. Built on <em>Understanding a Climate of Change</em>, '
          'by Patrick Freeland and Cayla Jones; Steve Robinson\'s <em>Climate Change and the Tribes: Columbia River '
          'Edition</em> (draft); and NESC 215, Climate Change in Indian Country, Northwest Indian College.')
WEEK_ORDER = ['Key lesson', 'Key takeaway', 'Learning objectives', 'Before class', 'Session shape', 'Hands-on activity',
              'Local lesson', 'Check for Understanding', 'Assignment', 'Reflection', 'Guest or Elder slot',
              'Instructor notes', 'Sovereignty thread']
LABELS = ('LIVE', 'SNAPSHOT', 'TEACHING MODEL')


# ---------- loading ----------
def front(text):
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end > 0:
            return yaml.safe_load(text[4:end]) or {}, text[end + 5:]
    return {}, text


def sections(md, level=2):
    """Split Markdown into (heading, body) by level-N headings; body before the first is ''."""
    out, cur, buf = [], '', []
    pat = re.compile(r'^' + '#' * level + r'\s+(.*)$')
    for ln in md.split('\n'):
        m = pat.match(ln)
        if m:
            out.append((cur, '\n'.join(buf).strip()))
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(ln)
    out.append((cur, '\n'.join(buf).strip()))
    return out


def read(p):
    return p.read_text(encoding='utf-8') if p.exists() else ''


def load_weeks(course):
    weeks = []
    for p in sorted((CORE / course).glob('week-*.md')):
        meta, body = front(read(p))
        meta.setdefault('week', int(re.sub(r'\D', '', p.stem) or 0))
        meta.setdefault('title', p.stem)
        weeks.append({'meta': meta, 'secs': dict((h, b) for h, b in sections(body) if h), 'file': p.name})
    return weeks


def load_sockets(site_dir, course):
    md = read(site_dir / 'deep-dive' / f'{course}-local.md')
    out = {}
    for h, b in sections(md):
        m = re.match(r'socket:\s*(week-\d+/[\w-]+)', h)
        if m and b.strip():
            out[m.group(1)] = b
    return out


# ---------- slots ----------
def slot_value(site, path):
    cur = site
    for k in path.split('.'):
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return None
    if isinstance(cur, dict):
        cur = cur.get('value', cur.get('name'))
    if isinstance(cur, list):
        cur = '; '.join(str(x.get('name', x)) if isinstance(x, dict) else str(x) for x in cur)
    return None if cur in (None, '', 'unknown') else str(cur)


class Ctx:
    def __init__(self, slug, site_dir, site):
        self.slug, self.dir, self.site = slug, site_dir, site
        self.raw = []
        self.unknown = set()
        self.open_sockets = []
        self.views = {}

    def token(self, h):
        self.raw.append(h)
        return f'\n\n@@RAW{len(self.raw) - 1}@@\n\n'

    def fill(self, md, course=None, sockets=None, socket_meta=None):
        def sock(m):
            key = m.group(1)
            course_, wk_id = key.split('/', 1)
            meta = (socket_meta or {}).get(wk_id.split('/', 1)[1], {})
            purpose = meta.get('purpose', wk_id)
            eye = EYES.get(meta.get('eye', ''), '')
            tag = ' · '.join(x for x in (eye, f"consent {meta['consent']}" if meta.get('consent') else '') if x)
            body = (sockets or {}).get(wk_id)
            if body:
                return f"\n::: socket\n<<LABEL Local lesson: {purpose}{' (' + tag + ')' if tag else ''}>>\n\n{body}\n:::\n"
            self.open_sockets.append(key)
            return (f"\n::: socket open\n<<LABEL Local lesson slot: {purpose}{' (' + tag + ')' if tag else ''}>>\n\n"
                    "This part of the week belongs to the people who teach here. "
                    "[LOCAL EXPERT: TCU faculty or knowledge holder]\n:::\n")
        md = re.sub(r'\{\{socket:([\w-]+/week-\d+/[\w-]+)\}\}', sock, md)
        md = re.sub(r'\{\{view:([\w.-]+)\}\}', lambda m: self.token(self.view(m.group(1))), md)

        def slot(m):
            v = slot_value(self.site, m.group(1))
            if v is None:
                self.unknown.add(m.group(1))
                return f'[UNKNOWN: {m.group(1)}]'
            return v
        return re.sub(r'\{\{([a-z_]+(?:\.[a-z0-9_]+)+)\}\}', slot, md)

    def html(self, md, **kw):
        h = mdlite.to_html(self.fill(md, **kw))
        h = re.sub(r'&lt;&lt;LABEL (.*?)&gt;&gt;', r'<span class="label">\1</span>', h)
        h = re.sub(r'<p><span class="label">(.*?)</span></p>', r'<span class="label">\1</span>', h)
        return re.sub(r'<p>@@RAW(\d+)@@</p>|@@RAW(\d+)@@', lambda m: self.raw[int(m.group(1) or m.group(2))], h)

    # ---------- data views ----------
    def view(self, name):
        data = self.dir / 'data'
        f = next((p for p in sorted(data.glob(name + '.*')) if not p.name.endswith('.meta.json')), None)
        meta_p = data / f'{name}.meta.json'
        if f is None or not meta_p.exists():
            return ('<figure class="view" data-label="SNAPSHOT"><span class="vlab">SNAPSHOT</span>'
                    f'<p><span class="mk mk-unknown"><b>unknown</b><span class="mk-t">case pack file {html.escape(name)} not found</span></span></p></figure>')
        meta = json.loads(meta_p.read_text(encoding='utf-8'))
        self.views[name] = meta
        label = meta.get('label', 'SNAPSHOT')
        label = label if label in LABELS else 'SNAPSHOT'
        title = html.escape(meta.get('title', name))
        cap = (f"{html.escape(meta.get('source', 'source not stated'))}; issuer: {html.escape(meta.get('issuer', 'not stated'))}; "
               f"captured {html.escape(fmt_date(meta.get('captured_at', '')))}; SHA-256 {html.escape(meta.get('sha256', '')[:12])}; "
               f"license: {html.escape(meta.get('license', 'not stated'))}.")
        if meta.get('note'):
            cap += ' ' + html.escape(meta['note'])
        body = ''
        if f.suffix == '.csv':
            rows = list(csv.DictReader(f.open(encoding='utf-8')))
            v = meta.get('view', {})
            if v.get('type') == 'series' and rows:
                body = series_svg(rows, v, title)
            body += table_html(rows, open_=not body)
        elif f.suffix.lower() in ('.jpg', '.jpeg', '.png'):
            body = f'<img src="data/{f.name}" alt="{html.escape(meta.get("alt", ""))}">'
        return (f'<figure class="view" data-label="{label}"><span class="vlab">{label}</span>'
                f'<h3>{title}</h3>{body}<figcaption>{cap}</figcaption></figure>')


def fmt_date(s):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', str(s))
    return f'{m.group(2)}/{m.group(3)}/{m.group(1)}' if m else (str(s) or 'not stated')


def table_html(rows, open_=False):
    if not rows:
        return '<p>No rows.</p>'
    cols = list(rows[0].keys())
    cell = lambda v: html.escape(v) if v not in ('', None) else '<span class="mk mk-unknown"><b>unknown</b></span>'
    t = ('<div class="tw"><table><thead><tr>' + ''.join(f'<th scope="col">{html.escape(c)}</th>' for c in cols) + '</tr></thead><tbody>'
         + ''.join('<tr>' + ''.join(f'<td>{cell(r[c])}</td>' for c in cols) + '</tr>' for r in rows) + '</tbody></table></div>')
    return f'<details class="tbl"{" open" if open_ else ""}><summary>Data table ({len(rows)} rows)</summary>{t}</details>'


def series_svg(rows, v, title):
    x = v.get('x', 'year')
    series = v.get('series', [])
    W, H, L, R, T, B = 760, 300, 56, 16, 16, 40
    xs = [float(r[x]) for r in rows]
    vals = []
    for s in series:
        for k in (s['y'], s.get('lo'), s.get('hi')):
            if k:
                vals += [float(r[k]) for r in rows if r.get(k) not in ('', None)]
    if not xs or not vals:
        return ''
    x0, x1, y0, y1 = min(xs), max(xs), min(vals), max(vals)
    pad = (y1 - y0) * .08 or 1
    y0, y1 = y0 - pad, y1 + pad
    X = lambda a: L + (a - x0) / ((x1 - x0) or 1) * (W - L - R)
    Y = lambda a: T + (1 - (a - y0) / ((y1 - y0) or 1)) * (H - T - B)
    g = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{title}. Chart; the same numbers are in the data table below.">']
    for i in range(5):
        yv = y0 + (y1 - y0) * i / 4
        g.append(f'<line x1="{L}" x2="{W - R}" y1="{Y(yv):.1f}" y2="{Y(yv):.1f}" stroke="rgba(232,236,240,.12)"/>'
                 f'<text x="{L - 6}" y="{Y(yv) + 4:.1f}" text-anchor="end" font-size="11" fill="#9AA4B5">{yv:.1f}</text>')
    step = 10 if x1 - x0 <= 80 else 20
    for xv in range(int(x0 // step * step + step), int(x1) + 1, step):
        g.append(f'<text x="{X(xv):.1f}" y="{H - 18}" text-anchor="middle" font-size="11" fill="#9AA4B5">{xv}</text>')
    if v.get('baseline'):
        b0, b1 = v['baseline']
        g.append(f'<rect x="{X(b0):.1f}" y="{T}" width="{X(b1) - X(b0):.1f}" height="{H - T - B}" fill="rgba(156,199,240,.08)"/>'
                 f'<text x="{X(b0) + 3:.1f}" y="{T + 12}" font-size="11" fill="#9CC7F0">baseline {b0} to {b1}</text>')
    colors = ['#9CC7F0', '#F26B5E', '#D7A6E8', '#E8ECF0']
    dashes = ['', '7 5', '2 4', '10 3 2 3']
    for i, s in enumerate(series):
        c, d = colors[i % 4], dashes[i % 4]
        if s.get('lo') and s.get('hi'):
            pts = [r for r in rows if r.get(s['lo']) not in ('', None) and r.get(s['hi']) not in ('', None)]
            if pts:
                poly = ' '.join(f'{X(float(r[x])):.1f},{Y(float(r[s["hi"]])):.1f}' for r in pts) + ' ' + \
                       ' '.join(f'{X(float(r[x])):.1f},{Y(float(r[s["lo"]])):.1f}' for r in reversed(pts))
                g.append(f'<polygon points="{poly}" fill="{c}" fill-opacity=".14"/>')
        pts = [r for r in rows if r.get(s['y']) not in ('', None)]
        path = ' '.join(('M' if j == 0 else 'L') + f'{X(float(r[x])):.1f} {Y(float(r[s["y"]])):.1f}' for j, r in enumerate(pts))
        g.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2.2"' + (f' stroke-dasharray="{d}"' if d else '') + '/>')
        ly = T + 14 + i * 16
        g.append(f'<line x1="{W - R - 230}" x2="{W - R - 200}" y1="{ly}" y2="{ly}" stroke="{c}" stroke-width="2.2"'
                 + (f' stroke-dasharray="{d}"' if d else '') + f'/><text x="{W - R - 194}" y="{ly + 4}" font-size="11.5" fill="#E8ECF0">{html.escape(s.get("name", s["y"]))}</text>')
    if v.get('unit'):
        g.append(f'<text x="8" y="{T + 4}" font-size="11" fill="#9AA4B5">{html.escape(v["unit"])}</text>')
    g.append('</svg>')
    return ''.join(g)


# ---------- pages ----------
NAV = [('index.html', 'Home'), ('place.html', 'Place'), ('ccic-200.html', 'CCIC 200'), ('tcr-201.html', 'TCR 201'),
       ('primer.html', 'Primer'), ('respect.html', 'Respect'), ('resources.html', 'Resources'), ('credits.html', 'Credits')]


def page(ctx, fname, title, body, built):
    site = ctx.site
    tpl = read(TEMPLATES / 'minisite' / 'page.html')
    nav = list(NAV)
    if (ctx.dir / 'deep-dive' / 'timeline.yaml').exists():
        nav.insert(2, ('timeline.html', 'Timeline'))
    cur = fname if fname in dict(nav) else ('ccic-200.html' if fname.startswith('ccic') else 'tcr-201.html' if fname.startswith('tcr') else '')
    navh = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == cur else '') + f'>{t}</a>' for h, t in nav)
    draft = '<div class="draft" role="note">Draft for TCU review</div>' if site.get('draft', True) else ''
    name = html.escape(slot_value(site, 'institution.name') or ctx.slug)
    out = (tpl.replace('__TITLE__', html.escape(title)).replace('__SITE__', name).replace('__NAV__', navh)
           .replace('__DRAFT__', draft).replace('__AUTHOR__', AUTHOR).replace('__BUILT__', built).replace('__BODY__', body))
    (ctx.out / fname).write_text(out, encoding='utf-8', newline='\n')


def chips(items):
    return '<div class="chips">' + ''.join(f'<span class="chip">{html.escape(i)}</span>' for i in items if i) + '</div>'


def week_page(ctx, course, wk, sockets, prev_next, built):
    m, secs = wk['meta'], wk['secs']
    smeta = {s['id']: s for s in (m.get('sockets') or []) if isinstance(s, dict) and 'id' in s}
    eyes = [EYES.get(e, e) for e in (m.get('eyes') or [])]
    body = [f'<p class="label">{html.escape(COURSES[course])} · Week {m["week"]}</p>',
            f'<h1>{html.escape(str(m["title"]))}</h1>', chips([str(m.get('thread', ''))] + eyes)]
    order = WEEK_ORDER + [h for h in secs if h not in WEEK_ORDER]
    for h in order:
        if h in secs and secs[h].strip():
            body.append(f'<h2 id="{mdlite.slugify(h)}">{html.escape(h)}</h2>')
            body.append(ctx.html(secs[h], course=course, sockets=sockets, socket_meta=smeta))
    p, n = prev_next
    body.append('<p>' + (f'<a href="{p[0]}">Back: {html.escape(p[1])}</a>' if p else '') + (' · ' if p and n else '')
                + (f'<a href="{n[0]}">Next: {html.escape(n[1])}</a>' if n else '') + '</p>')
    page(ctx, f'{course}-week-{int(m["week"]):02d}.html', f'{COURSES[course].split(":")[0]} Week {m["week"]}: {m["title"]}', '\n'.join(body), built)


def course_page(ctx, course, weeks, built):
    md = read(CORE / course / 'syllabus.md')
    _, md = front(md)
    cards = ''.join(f'<li><span class="label">Week {w["meta"]["week"]}</span><a href="{course}-week-{int(w["meta"]["week"]):02d}.html">'
                    f'{html.escape(str(w["meta"]["title"]))}</a></li>' for w in weeks)
    body = (f'<p class="label">Course</p><h1>{html.escape(COURSES[course])}</h1>'
            f'<p><a href="{course}-deck.html">Open the presentation (one file, works offline)</a> · '
            f'<a href="{course}.pptx">PowerPoint version</a></p><h2>Weeks</h2><ul class="cards">{cards}</ul>'
            + ctx.html(re.sub(r'^# .*\n', '', md, count=1)))
    page(ctx, f'{course}.html', COURSES[course], body, built)


def doc_page(ctx, fname, title, md_path, kicker, built, extra=''):
    md = read(md_path)
    _, md = front(md)
    if not md.strip():
        md = f'# {title}\n\n[UNKNOWN: {md_path.name} not written yet]'
    page(ctx, fname, title, f'<p class="label">{html.escape(kicker)}</p>' + extra + ctx.html(md), built)


def resources_page(ctx, built):
    pk = ctx.dir / 'packet'
    files = sorted(pk.glob('*.md'), key=lambda p: (p.name != 'scout.md', p.name)) if pk.is_dir() else []
    parts = ['<p class="label">Resource packet</p><h1>Resources</h1>',
             '<p>Built by public-web scouts. Every item names its source, its date as the source states it, and the day it was '
             'opened. Leads were found but not opened: they are leads, not facts.</p>']
    for f in files:
        md = re.sub(r'^# ', '## ', read(f), flags=re.M)
        parts.append(f'<section aria-label="{html.escape(f.stem)}">' + ctx.html(md) + '</section>')
    if not files:
        parts.append(ctx.html('[UNKNOWN: resource packet not built yet]'))
    page(ctx, 'resources.html', 'Resources', '\n'.join(parts), built)


def credits_page(ctx, built):
    rows = []
    data = ctx.dir / 'data'
    for mp in sorted(data.glob('*.meta.json')) if data.is_dir() else []:
        m = json.loads(mp.read_text(encoding='utf-8'))
        name = mp.name[:-len('.meta.json')]
        rows.append(f"| {name} | {m.get('label', 'SNAPSHOT')} | {m.get('source', 'not stated')} | {m.get('issuer', 'not stated')} | "
                    f"{fmt_date(m.get('captured_at', ''))} | {m.get('license', 'not stated')} | {m.get('sha256', '')[:16]} |")
    md = ('# Credits\n\n## Authors\n\nPatrick A. Freeland (module author), with ATNI Climate. Built on *Understanding a Climate of '
          'Change*, by Patrick Freeland and Cayla Jones; Steve Robinson\'s *Climate Change and the Tribes: Columbia River Edition* '
          '(draft); and NESC 215, Climate Change in Indian Country, Northwest Indian College. Previously cited authors and agency '
          'issuers stay as cited on each page. Licensing is set later.\n\n'
          '## Case pack\n\nEvery data view on this site comes from one of these files. LIVE sources are linked, never embedded. '
          'A blank is unknown, never zero.\n\n| File | Label | Source | Issuer | Captured | License as stated | SHA-256 (first 16) |\n'
          '|---|---|---|---|---|---|---|\n' + ('\n'.join(rows) if rows else '| none | | | | | | |') +
          '\n\n## Fonts\n\nLeague Spartan, Lexend Deca, and Cascadia Code: the ATNI Climate design system fonts, copied from the '
          'workshop page (docs/fonts). Their license rows are pending in planning/MEDIA-CREDITS.md. [verify]\n')
    page(ctx, 'credits.html', 'Credits', ctx.html(md), built)


def timeline_page(ctx, built):
    t = yaml.safe_load(read(ctx.dir / 'deep-dive' / 'timeline.yaml')) or {}
    ev = t.get('events', [])
    items = []
    for e in ev:
        src = ' '.join(f'<a href="{html.escape(s["url"])}">{html.escape(s.get("title", s["url"]))}</a> ({html.escape(s.get("issuer", ""))})'
                       for s in e.get('sources', []) if s.get('url'))
        items.append(f'<li><span class="when">{html.escape(str(e.get("date", "undated")))}</span>'
                     f'{ctx.html(e.get("event", ""))}<p class="byline">Source: {src or "not stated"}</p></li>')
    strip = ''
    maps = t.get('maps', [])
    if maps:
        strip = '<h2>Map strip</h2><div class="strip">' + ''.join(ctx.view(m) for m in maps) + '</div>'
    support = f'<div class="support" role="note">{ctx.html(t["support_line"])}</div>' if t.get('support_line') else ''
    body = (f'<p class="label">Timeline</p><h1>{html.escape(t.get("title", "Timeline"))}</h1>{support}'
            + ctx.html(t.get('intro', '')) + f'<ol class="tl">{"".join(items)}</ol>{strip}')
    page(ctx, 'timeline.html', t.get('title', 'Timeline'), body, built)


def count_marks(texts):
    c = {'confirm': {}, 'local': 0, 'placeholder': 0, 'voice': 0, 'verify': 0}
    for t in texts:
        for m in mdlite.MARK_RE.finditer(t):
            k, v = m.group(1), (m.group(2) or '').strip()
            if k == 'NEEDS TRIBAL CONFIRMATION':
                c['confirm'][v] = c['confirm'].get(v, 0) + 1
            elif k == 'LOCAL EXPERT':
                c['local'] += 1
            elif k in ('PLACEHOLDER', 'INSTRUCTOR SELECTS'):
                c['placeholder'] += 1
            elif k == 'PERSONAL VOICE':
                c['voice'] += 1
        c['verify'] += len(mdlite.VERIFY_RE.findall(t))
    return c


def leads_count(ctx):
    n = 0
    for f in (ctx.dir / 'packet').glob('*.md') if (ctx.dir / 'packet').is_dir() else []:
        for h, b in sections(read(f)):
            if 'lead' in h.lower():
                n += len(re.findall(r'^\s*[-*]\s', b, flags=re.M))
    return n


# ---------- decks ----------
def deck_slides(ctx, course, weeks, sockets):
    S = []
    name = slot_value(ctx.site, 'institution.name') or ctx.slug

    def add(part, kicker, title, md='', notes='', big=False, hall=False, raw=''):
        S.append({'part': part, 'kicker': kicker, 'title': ctx.fill(title), 'md': md, 'notes': notes, 'big': big, 'hall': hall, 'raw': raw})
    add('Open', 'Template draft for TCU review', COURSES[course], f'{name}\n\nPatrick A. Freeland (module author), with ATNI Climate.',
        'Presenter keys: arrows or Space move; N speaker notes; T clock; H highlight pass. Fonts: League Spartan, Lexend Deca, '
        'Cascadia Code are inlined in this file.', hall=True)
    add('Open', 'How each week runs', 'Presence, Application, Inquiry, Reflection',
        '- **Presence:** showing up for each other.\n- **Application:** hands-on work.\n- **Inquiry:** questions that lead to more questions.\n'
        '- **Reflection:** what shifted, said plain enough for an Elder and a child.\n\nEach week also keeps a module record: lecture or '
        'presentation, a Check for Understanding, the module assignment, and a reflection.')
    add('Open', 'Course map', 'Ten weeks', '| Week | Title | Eyes |\n|---|---|---|\n' + '\n'.join(
        f'| {w["meta"]["week"]} | {w["meta"]["title"]} | {", ".join(EYES.get(e, e) for e in (w["meta"].get("eyes") or []))} |' for w in weeks))
    for w in weeks:
        m, s = w['meta'], w['secs']
        part = f'Week {m["week"]}'
        smeta = {x['id']: x for x in (m.get('sockets') or []) if isinstance(x, dict) and 'id' in x}
        notes = '\n\n'.join(f'**{h}.** {s[h]}' for h in ('Learning objectives', 'Before class', 'Guest or Elder slot', 'Instructor notes') if s.get(h))
        add(part, f'Week {m["week"]} · {m.get("thread", "")}', str(m['title']), ' · '.join(EYES.get(e, e) for e in (m.get('eyes') or [])), notes, hall=True)
        for h, big in (('Key lesson', True), ('Key takeaway', True), ('Session shape', False), ('Hands-on activity', False),
                       ('Local lesson', False), ('Check for Understanding', False), ('Reflection', False)):
            if s.get(h, '').strip():
                add(part, f'Week {m["week"]}', h, s[h], notes if h == 'Session shape' else '', big=big)
                S[-1]['sockets'] = (sockets, smeta)
    place = read(ctx.dir / 'deep-dive' / 'place-profile.md')
    if place.strip():
        for h, b in sections(front(place)[1])[1:]:
            add('Place', 'This place', h, b)
    add('Close', 'Say it plain', 'What will you carry forward?',
        'One sentence, in words both an Elder and a child could understand.', hall=True)
    return S


def render_deck(ctx, course, slides, title):
    fonts = ''
    if FONTS:
        for fam, f, w in (('League Spartan', 'league-spartan.woff2', '100 900'), ('Lexend Deca', 'lexend-deca.woff2', '100 900'),
                          ('Cascadia Code', 'cascadia-code.woff2', '200 700')):
            p = FONTS / f
            if p.exists():
                fonts += (f'@font-face{{font-family:"{fam}";src:url(data:font/woff2;base64,{base64.b64encode(p.read_bytes()).decode()}) '
                          f'format("woff2");font-weight:{w};font-display:swap}}\n')
    out = []
    for i, s in enumerate(slides):
        sk, sm = s.get('sockets', (None, None))
        body = ctx.html(s['md'], course=course, sockets=sk, socket_meta=sm) if s['md'] else ''
        notes = ctx.html(s['notes'], course=course) if s['notes'] else '<p>No notes for this slide.</p>'
        cls = 'slide hall' if s['hall'] else 'slide'
        head = f'<h1>{mdlite.inline(s["title"])}</h1>' if s['hall'] else f'<h2>{mdlite.inline(s["title"])}</h2>'
        draft = '<span class="draft">Draft for TCU review</span>' if i == 0 and ctx.site.get('draft', True) else ''
        out.append(f'<section class="{cls}" data-part="{html.escape(s["part"])}" aria-label="Slide {i + 1}: {html.escape(s["title"])}"'
                   + (' hidden' if i else '') + f'><div class="in">{draft}<span class="k">{html.escape(s["kicker"])}</span>{head}'
                   f'<div class="{"big" if s["big"] else ""}">{body}</div></div><aside class="notes-src">{notes}</aside></section>')
    tpl = read(TEMPLATES / 'presentation' / 'deck.html')
    return tpl.replace('__FONTS__', fonts).replace('__TITLE__', html.escape(title)).replace('__SLIDES__', '\n'.join(out))


# ---------- main ----------
def build(slug, sites_dir):
    site_dir = sites_dir / slug
    site = yaml.safe_load(read(site_dir / 'site.yaml')) or {}
    ctx = Ctx(slug, site_dir, site)
    out = site_dir / 'build' / 'site'
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    ctx.out = out
    built = datetime.date.today().strftime('%m/%d/%Y')
    shutil.copy(TEMPLATES / 'minisite' / 'site.css', out / 'site.css')
    if FONTS:
        shutil.copytree(FONTS, out / 'fonts')
    data = site_dir / 'data'
    for img in (data.glob('*') if data.is_dir() else []):
        if img.suffix.lower() in ('.jpg', '.jpeg', '.png'):
            (out / 'data').mkdir(exist_ok=True)
            shutil.copy(img, out / 'data' / img.name)
    texts = []
    deck_files = {}
    for course in COURSES:
        weeks = load_weeks(course)
        sockets = load_sockets(site_dir, course)
        texts.append(read(CORE / course / 'syllabus.md'))
        course_page(ctx, course, weeks, built)
        for i, w in enumerate(weeks):
            texts.append('\n'.join(w['secs'].values()))
            nav = lambda j: (f'{course}-week-{int(weeks[j]["meta"]["week"]):02d}.html', f'Week {weeks[j]["meta"]["week"]}') if 0 <= j < len(weeks) else None
            week_page(ctx, course, w, sockets, (nav(i - 1), nav(i + 1)), built)
        texts += list(sockets.values())
        slides = deck_slides(ctx, course, weeks, sockets)
        (out / f'{course}-deck.html').write_text(render_deck(ctx, course, slides, f'{COURSES[course]} · {slot_value(site, "institution.name") or slug}'),
                                                 encoding='utf-8', newline='\n')
        deck_files[course] = slides
    place = site_dir / 'deep-dive' / 'place-profile.md'
    texts.append(read(place))
    doc_page(ctx, 'place.html', 'Place profile', place, 'Place profile', built)
    doc_page(ctx, 'primer.html', 'Sovereignty primer', CORE / 'shared' / 'primer.md', 'CCIC 200 primer', built)
    doc_page(ctx, 'respect.html', 'Respect and data care', CORE / 'shared' / 'respect.md', 'Shared rules', built)
    resources_page(ctx, built)
    credits_page(ctx, built)
    if (site_dir / 'deep-dive' / 'timeline.yaml').exists():
        timeline_page(ctx, built)
        texts.append(read(site_dir / 'deep-dive' / 'timeline.yaml'))
    texts.append(read(site_dir / 'site.yaml'))
    marks = count_marks(texts)
    leads = leads_count(ctx)
    status = {'slug': slug, 'built': built, 'confirm': marks['confirm'], 'confirm_total': sum(marks['confirm'].values()),
              'local_expert': marks['local'], 'placeholder': marks['placeholder'], 'personal_voice': marks['voice'],
              'verify': marks['verify'], 'unknown_slots': sorted(ctx.unknown), 'open_sockets': sorted(set(ctx.open_sockets)),
              'leads': leads, 'views': sorted(ctx.views)}
    name = slot_value(site, 'institution.name') or slug
    panel = ''.join(f'<div><b>{v}</b>{k}</div>' for k, v in (
        ('Tribal confirmation marks', status['confirm_total']), ('Local expert slots', status['local_expert']),
        ('Open local lesson slots', len(status['open_sockets'])), ('Unknown facts', len(status['unknown_slots'])),
        ('Leads not yet opened', leads), ('Verify tags', status['verify'])))
    who = ''.join(f'<li>{html.escape(k or "unnamed")}: {v}</li>' for k, v in sorted(marks['confirm'].items()))
    home = (f'<p class="label">Climate pathway</p><h1>{html.escape(name)}</h1>'
            + ctx.html(f'{{{{institution.town}}}}, {{{{institution.state}}}}. A template set for two courses: CCIC 200, Climate Change in '
                       'Indian Country, a primer on weather and climate, local impacts, ways of knowing, and sovereignty; and TCR 201, '
                       'Tribal Climate Resilience, where the learning turns to action.')
            + '<h2>Review panel</h2><p>What is still open on this site. Each mark is a place for this TCU, its local experts, or a '
              'Nation to speak; nothing here was filled for them.</p>'
            + f'<div class="panel">{panel}</div>'
            + (f'<details class="tbl"><summary>Confirmation marks by Nation</summary><ul>{who}</ul></details>' if who else '')
            + '<h2>Start here</h2><ul class="cards">'
            + ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in (
                ('place.html', 'Place profile: this land and water, by Frog\'s Eye, Bird\'s Eye, and Moon\'s Eye'),
                ('ccic-200.html', 'CCIC 200: Climate Change in Indian Country'), ('tcr-201.html', 'TCR 201: Tribal Climate Resilience'),
                ('ccic-200-deck.html', 'CCIC 200 presentation (one file, offline)'), ('tcr-201-deck.html', 'TCR 201 presentation (one file, offline)'),
                ('primer.html', 'Sovereignty primer'), ('respect.html', 'Respect and data care'), ('resources.html', 'Resource packet'),
                ('credits.html', 'Credits and case pack')))
            + ('<li><a href="timeline.html">Timeline</a></li>' if (site_dir / 'deep-dive' / 'timeline.yaml').exists() else '') + '</ul>')
    page(ctx, 'index.html', 'Home', home, built)
    # .pptx (optional dependency)
    try:
        import pptx_deck
        for course, slides in deck_files.items():
            pptx_deck.write(slides, out / f'{course}.pptx', COURSES[course], name)
        status['pptx'] = True
    except ImportError as e:
        status['pptx'] = f'skipped: {e}'
    # zips
    b = site_dir / 'build'
    with zipfile.ZipFile(b / f'{slug}-minisite.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file():
                z.write(p, f'{slug}/{p.relative_to(out).as_posix()}')
    with zipfile.ZipFile(b / f'{slug}-source-kit.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for base, arc in ((CORE, 'tcu/core'), (ENGINE, 'tcu/engine'), (TEMPLATES, 'tcu/templates')):
            for p in sorted(base.rglob('*')):
                if p.is_file() and '__pycache__' not in p.parts:
                    z.write(p, f'{arc}/{p.relative_to(base).as_posix()}')
        if FONTS and FONTS != TEMPLATES / 'fonts':
            for p in FONTS.glob('*.woff2'):
                z.write(p, f'tcu/templates/fonts/{p.name}')
        for extra in ('README.md', 'DESIGN.md'):
            if (TCU / extra).exists():
                z.write(TCU / extra, f'tcu/{extra}')
        for p in sorted(site_dir.rglob('*')):
            if p.is_file() and 'build' not in p.relative_to(site_dir).parts:
                z.write(p, f'tcu/sites/{slug}/{p.relative_to(site_dir).as_posix()}')
    (b / 'status.json').write_text(json.dumps(status, indent=1, ensure_ascii=False), encoding='utf-8')
    return status


def main(argv):
    sites_dir = DEFAULT_SITES
    if '--sites' in argv:
        i = argv.index('--sites')
        sites_dir = Path(argv[i + 1]).resolve()
        argv = argv[:i] + argv[i + 2:]
    slugs = [a for a in argv if not a.startswith('--')]
    if '--all' in argv:
        slugs = sorted(p.parent.name for p in sites_dir.glob('*/site.yaml'))
    if not slugs:
        print(__doc__)
        return 2
    for s in slugs:
        st = build(s, sites_dir)
        print(f"built {s}: confirm {st['confirm_total']}, local {st['local_expert']}, open sockets {len(st['open_sockets'])}, "
              f"unknown {len(st['unknown_slots'])}, leads {st['leads']}, pptx {st['pptx']}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
