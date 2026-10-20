"""Static gate for the climate-curriculum repo. Read-only: never writes a file.

Run after `python source/build.py`:
    python tools/check.py            # whole default set
    python tools/check.py PATH ...   # house style on named files only
    python tools/check.py --selftest

ERROR (exit 1): em dash, external src/stylesheet/url() in docs/index.html, network calls,
missing local asset, slide-id problems.
WARN (exit 0): house-style words a human should look at (lowercase Tribal terms,
"stakeholder", CLAUDE.md filler words). Judgment calls stay with pf-voice and Patrick.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')  # Windows console defaults to cp1252

EM_DASH = chr(0x2014)  # spelled as a code point so this file never contains one
# Lookarounds skip JS keys ('elders', treaty:) and URL slugs (/nonprofits-tribes-and-).
LOWER_TERMS = re.compile(r'''(?<![\w/'"-])(indigenous|tribal|tribes|elders?|treaty|treaties|first foods)(?![\w'":/-])''')
# A quoted "stakeholders" is the rule being stated, not a use.
STAKEHOLDER = re.compile(r'''(?<!["'])stakeholder''', re.I)
FILLER = re.compile(r'\b(delve\w*|tapestry|unlock\w*|empower\w*)\b', re.I)
EXT_SRC = re.compile(r'''(?:\bsrc\s*=\s*["']?|<link[^>]*\bhref\s*=\s*["']?|url\(\s*["']?|@import\s+["'])https?://''', re.I)
NETWORK = re.compile(r'\b(fetch\s*\(|XMLHttpRequest|sendBeacon|new\s+WebSocket|EventSource\s*\()')
LOCAL_ASSET = re.compile(r'''["'(]((?:img|fonts)/[\w./-]+\.(?:jpe?g|png|webp|svg|gif|woff2?|mp4|webm))''', re.I)
SECTION = re.compile(r'<section\b[^>]*class="[^"]*\bslide\b[^"]*"[^>]*>')
SLIDE_ID = re.compile(r'data-slide-id="([^"]*)"')
ID_FORM = re.compile(r'^s(\d\d)-[a-z0-9]+(?:-[a-z0-9]+)*$')


def scan_style(name, text):
    """Return (errors, warnings) lists of 'name:line: message' strings."""
    errs, warns = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if EM_DASH in line:
            errs.append(f'{name}:{n}: em dash (U+2014)')
        for rx, msg in ((LOWER_TERMS, 'lowercase term (capitalize if it names a People, role or Treaty)'),
                        (STAKEHOLDER, '"stakeholder" (Nations and relatives are not stakeholders)'),
                        (FILLER, 'filler word from CLAUDE.md list')):
            for m in rx.finditer(line):
                warns.append(f'{name}:{n}: {msg}: "{m.group(0)}"')
    return errs, warns


def scan_slides(text):
    """Every slide section has a unique, well-formed id. Ids are frozen, so the number need not match position."""
    errs, ids = [], []
    for pos, m in enumerate(SECTION.finditer(text), 1):
        sid = SLIDE_ID.search(m.group(0))
        if not sid:
            errs.append(f'slide {pos}: no data-slide-id')
            continue
        sid = sid.group(1)
        f = ID_FORM.match(sid)
        if not f:
            errs.append(f'slide {pos}: malformed id "{sid}"')
        if sid in ids:
            errs.append(f'slide {pos}: duplicate id "{sid}"')
        ids.append(sid)
    return errs, ids


def scan_built(docs, text):
    errs = []
    for n, line in enumerate(text.splitlines(), 1):
        if EXT_SRC.search(line):
            errs.append(f'docs/index.html:{n}: external resource (page must run offline)')
        m = NETWORK.search(line)
        if m:
            errs.append(f'docs/index.html:{n}: network call "{m.group(0)}" (no network for student data)')
    for rel in sorted(set(LOCAL_ASSET.findall(text))):
        if not (docs / rel).is_file():
            errs.append(f'docs/index.html: missing asset docs/{rel}')
    return errs


def selftest():
    e, w = scan_style('t', 'a ' + EM_DASH + ' b\nthe tribal council\nTribal Nations\nour stakeholders\nlet us delve\n'
                           "elders:['Elders'] /nonprofits-tribes-and- never \"stakeholders\"")
    assert len(e) == 1 and len(w) == 3, (e, w)
    e, ids = scan_slides('<section class="slide hall" data-slide-id="s01-title"><section class="slide" data-slide-id="s03-x"><section class="slide">')
    assert ids == ['s01-title', 's03-x'] and len(e) == 1, e
    assert EXT_SRC.search('<img src="https://x/y.png">') and EXT_SRC.search("url('http://x')")
    assert not EXT_SRC.search('<a href="https://atniclimate.org">')
    print('selftest ok')


def main(argv):
    if argv[:1] == ['--selftest']:
        selftest()
        return 0
    root = Path(__file__).resolve().parents[1]
    if argv[:1] == ['--root']:
        root, argv = Path(argv[1]), argv[2:]
    errs, warns = [], []
    if argv:
        files = [Path(a) for a in argv]
    else:
        # shortcut: reads the single template; switch to the source/order.txt parts in the D10 split commit
        files = [root / 'source/template.html', root / 'README.md',
                 *sorted((root / 'curriculum').glob('*.md')),
                 # revision notes are a locked scope source that quotes the banned words; not ours to fix
                 *sorted(p for p in (root / 'planning').glob('*.md') if not p.name.startswith('revision-notes'))]
        tpl = (root / 'source/template.html').read_text(encoding='utf-8')
        e, ids = scan_slides(tpl)
        errs += e
        print(f'slides: {len(ids)} ({ids[0] if ids else "-"} .. {ids[-1] if ids else "-"})')
        built = root / 'docs/index.html'
        errs += scan_built(built.parent, built.read_text(encoding='utf-8'))
        if EM_DASH in built.read_text(encoding='utf-8'):
            errs.append('docs/index.html: em dash present in build output')
        print(f'placeholders in template: {tpl.count("[PLACEHOLDER")}, [verify] markers: {tpl.count("[verify]")}')
    for f in files:
        e, w = scan_style(f.relative_to(root) if f.is_relative_to(root) else f, f.read_text(encoding='utf-8'))
        errs += e
        warns += w
    for w in warns:
        print('WARN ', w)
    for e in errs:
        print('ERROR', e)
    print(f'{len(errs)} error(s), {len(warns)} warning(s)')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
