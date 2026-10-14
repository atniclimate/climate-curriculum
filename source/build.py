"""Rebuild docs/index.html from source/template.html and source/columbia_svg.json."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>[hidden]{display:none!important}</style></head><body>')
# Explicit UTF-8 and LF: Windows defaults to cp1252 and CRLF, which breaks the build.
t = (root / 'source/template.html').read_text(encoding='utf-8')
m = (root / 'source/columbia_svg.json').read_text(encoding='utf-8')
(root / 'docs/index.html').write_text(head + t.replace('__MAP__', m) + '</body></html>',
                                      encoding='utf-8', newline='\n')
print('built docs/index.html')
