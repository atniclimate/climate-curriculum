import json, sys
from collections import defaultdict
raw = open(sys.argv[1], encoding='utf-8').read().strip()
rep = json.loads(json.loads(raw)) if raw.startswith('"') else json.loads(raw)
print('h1Count', rep['h1Count'])
CHROME = ('Clock', 'Highlight', 'Notes', 'Previous slide', 'Next slide', 'Go to ')
chrome = defaultdict(set)
for r in rep['runs']:
    taps = r.get('tapTargets', [])
    for t in taps:
        if t.startswith(CHROME):
            chrome[r['vp']].add(t)
    r['tapTargets'] = [t for t in taps if not t.startswith(CHROME)]
for vp, s in chrome.items():
    print(f'CHROME {vp}: ' + '; '.join(sorted(s)))
for r in rep['runs']:
    rest = {k: v for k, v in r.items() if k not in ('vp', 'notes', 'id') and v}
    if rest:
        print(f"{r['vp']} notes={'open' if r['notes'] else 'closed'} {r['id']}: {json.dumps(rest)}")
for p in rep['perf']:
    print('PERF', json.dumps(p))
