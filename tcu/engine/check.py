"""Check one or more built TCU sites. Exit 1 on any failure.

python tcu/engine/check.py <slug> [...] | --all [--sites <dir>]

Fails on: an em dash anywhere in the built site or the site's source files;
any external URL a page loads (src, stylesheet, CSS url() or @import, fetch,
XMLHttpRequest, WebSocket, sendBeacon); an <img> without alt or an <svg> or
role="img" element without an accessible name; a data view without a LIVE,
SNAPSHOT, or TEACHING MODEL label; a case-pack file without its meta.json; a
leftover {{slot}} in built output. Links (<a href>) to public sources are allowed.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ENGINE = Path(__file__).resolve().parent
TCU = ENGINE.parent
DEFAULT_SITES = next((p for p in (TCU.parent / 'private' / 'tcu', TCU / 'sites') if p.is_dir()), TCU / 'sites')
EXTERNAL = re.compile(r'^(?:[a-z][a-z0-9+.-]*:)?//', re.I)
LABELS = {'LIVE', 'SNAPSHOT', 'TEACHING MODEL'}
EMDASH = chr(0x2014)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.errs = []
        self.views = []  # [label, text seen]

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ('src', 'srcset', 'poster', 'data'):
            v = (a.get(k) or '').strip()
            if v and (EXTERNAL.match(v) or v.startswith('http')):
                self.errs.append(f'loads external URL: <{tag} {k}="{v[:80]}">')
        if tag == 'link' and (EXTERNAL.match(a.get('href') or '') or (a.get('href') or '').startswith('http')):
            self.errs.append(f'loads external URL: <link href="{(a.get("href") or "")[:80]}">')
        if tag in ('iframe', 'embed', 'object'):
            self.errs.append(f'<{tag}> not allowed')
        if tag == 'img' and 'alt' not in a:
            self.errs.append(f'img without alt: {a.get("src", "")[:60]}')
        if (tag == 'svg' or a.get('role') == 'img') and not (a.get('aria-label') or a.get('aria-labelledby') or a.get('aria-hidden') == 'true'):
            self.errs.append(f'<{tag}> image without an accessible name')
        if tag == 'figure' and 'view' in (a.get('class') or '').split():
            self.views.append([a.get('data-label'), ''])

    def handle_data(self, data):
        if self.views:
            self.views[-1][1] += data


def check_html(text, name):
    errs = []
    p = Page()
    p.feed(text)
    errs += p.errs
    for lab, seen in p.views:
        if lab not in LABELS or lab not in seen:
            errs.append(f'data view without a visible LIVE, SNAPSHOT, or TEACHING MODEL label (data-label={lab!r})')
    for m in re.finditer(r'url\(\s*["\']?((?:https?:)?//[^)"\']+)', text):
        errs.append(f'CSS loads external URL: {m.group(1)[:80]}')
    for m in re.finditer(r'@import\s+(?:url\()?["\']?(https?:|//)', text):
        errs.append('CSS @import of an external URL')
    for pat in (r'\bfetch\s*\(', r'XMLHttpRequest', r'new\s+WebSocket', r'sendBeacon', r'EventSource'):
        if re.search(pat, text):
            errs.append(f'network call in script: {pat}')
    if re.search(r'\{\{[^}]*\}\}', text):
        errs.append('unresolved {{slot}} in output: ' + re.search(r'\{\{[^}]*\}\}', text).group(0)[:60])
    return [f'{name}: {e}' for e in errs]


def check_site(site_dir):
    errs = []
    built = site_dir / 'build' / 'site'
    if not (built / 'index.html').exists():
        return [f'{site_dir.name}: not built (no build/site/index.html)']
    for f in sorted(built.rglob('*')):
        if f.suffix in ('.html', '.css', '.js', '.json', '.md', '.txt', '.yaml', '.svg'):
            t = f.read_text(encoding='utf-8')
            if EMDASH in t:
                errs.append(f'{f.relative_to(site_dir)}: em dash (U+2014)')
            if f.suffix == '.html':
                errs += check_html(t, str(f.relative_to(site_dir)))
            if f.suffix == '.css':
                for m in re.finditer(r'url\(\s*["\']?((?:https?:)?//[^)"\']+)', t):
                    errs.append(f'{f.relative_to(site_dir)}: CSS loads external URL {m.group(1)[:80]}')
    for f in sorted(site_dir.rglob('*')):
        rel = f.relative_to(site_dir)
        if f.is_file() and rel.parts[0] != 'build' and f.suffix in ('.md', '.yaml', '.yml', '.json', '.csv', '.txt'):
            if EMDASH in f.read_text(encoding='utf-8', errors='replace'):
                errs.append(f'{rel}: em dash (U+2014) in source')
    data = site_dir / 'data'
    for f in sorted(data.rglob('*')) if data.is_dir() else []:
        if f.is_file() and not f.name.endswith('.meta.json') and f.name not in ('README.md', 'SHA256SUMS'):
            stem_meta = f.with_name(f.stem + '.meta.json')
            full_meta = f.with_name(f.name + '.meta.json')
            if not (stem_meta.exists() or full_meta.exists()):
                errs.append(f'{f.relative_to(site_dir)}: case-pack file without its meta.json')
    return errs


def main(argv):
    sites_dir = DEFAULT_SITES
    if '--sites' in argv:
        i = argv.index('--sites')
        sites_dir = Path(argv[i + 1]).resolve()
        argv = argv[:i] + argv[i + 2:]
    slugs = sorted(p.parent.name for p in sites_dir.glob('*/site.yaml')) if '--all' in argv else [a for a in argv if not a.startswith('--')]
    if not slugs:
        print(__doc__)
        return 2
    bad = 0
    for s in slugs:
        errs = check_site(sites_dir / s)
        print(f'{s}: ' + ('pass' if not errs else f'FAIL ({len(errs)})'))
        for e in errs[:40]:
            print('  ' + e)
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
