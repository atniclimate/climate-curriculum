"""Rebuild docs/index.html from source/template.html and source/columbia_svg.json.

python source/build.py          write docs/index.html
python source/build.py --check  build in memory only; exit 1 if docs/index.html is stale
"""
import sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>[hidden]{display:none!important}</style></head><body>')
# Explicit UTF-8 and LF: Windows defaults to cp1252 and CRLF, which breaks the build.
t = (root / 'source/template.html').read_text(encoding='utf-8')
m = (root / 'source/columbia_svg.json').read_text(encoding='utf-8')
out = head + t.replace('__MAP__', m) + '</body></html>'
dest = root / 'docs/index.html'
if '--check' in sys.argv:
    # CRLF-normalized so a core.autocrlf checkout does not read as stale.
    same = dest.read_bytes().replace(b'\r\n', b'\n') == out.encode('utf-8')
    print('docs/index.html is up to date' if same else 'docs/index.html differs from a fresh build')
    sys.exit(0 if same else 1)
dest.write_text(out, encoding='utf-8', newline='\n')
print('built docs/index.html')
