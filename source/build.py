"""Rebuild docs/index.html from source/template.html and source/columbia_svg.json."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>[hidden]{display:none!important}</style></head><body>')
t = (root / 'source/template.html').read_text()
m = (root / 'source/columbia_svg.json').read_text()
(root / 'docs/index.html').write_text(head + t.replace('__MAP__', m) + '</body></html>')
print('built docs/index.html')
