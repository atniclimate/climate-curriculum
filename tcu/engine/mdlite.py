"""A small Markdown subset to HTML, with the TCU marker boxes.

Covers what tcu/core and the deep dives use: headings, paragraphs, lists (two
levels), pipe tables, blockquotes, rules, fenced code, ::: divs, and inline
bold, italic, code, and links. Markers ([LOCAL EXPERT: ...] and the rest,
DESIGN.md section 3) become labeled boxes.
shortcut: not CommonMark; if pages need more, vendor a real parser (ask Patrick first).
"""
import html
import re

MARKERS = {
    'LOCAL EXPERT': ('mk-local', 'Local expert'),
    'NEEDS TRIBAL CONFIRMATION': ('mk-confirm', 'Needs Tribal confirmation'),
    'TCU REVIEW': ('mk-local', 'TCU review'),
    'PLACEHOLDER': ('mk-place', 'Placeholder'),
    'INSTRUCTOR SELECTS': ('mk-place', 'Instructor selects'),
    'PERSONAL VOICE': ('mk-voice', 'Personal voice'),
    'UNKNOWN': ('mk-unknown', 'unknown'),
}
MARK_RE = re.compile(r'`?\[(LOCAL EXPERT|NEEDS TRIBAL CONFIRMATION|TCU REVIEW|PLACEHOLDER|INSTRUCTOR SELECTS|PERSONAL VOICE|UNKNOWN)(?::\s*([^\]]*))?\]`?(?!\()')
VERIFY_RE = re.compile(r'`?\[verify(?:[ :]([^\]]*))?\]`?(?!\()')


def marker_html(kind, text):
    cls, label = MARKERS[kind]
    body = f'<span class="mk-t">{text}</span>' if text else ''
    return f'<span class="mk {cls}"><b>{label}</b>{body}</span>'


def inline(s):
    s = html.escape(s, quote=False)
    s = MARK_RE.sub(lambda m: marker_html(m.group(1), (m.group(2) or '').strip()), s)
    s = VERIFY_RE.sub(lambda m: '<span class="mk mk-verify"><b>verify</b>' + (f'<span class="mk-t">{m.group(1).strip()}</span>' if m.group(1) else '') + '</span>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r'(?<!["=>])(https?://[^\s<)]+[^\s<).,;:])', r'<a href="\1">\1</a>', s)
    return s


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def _table(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    head, body = cells[0], [r for r in cells[2:]]
    out = ['<div class="tw"><table><thead><tr>' + ''.join(f'<th scope="col">{inline(c)}</th>' for c in head) + '</tr></thead><tbody>']
    for r in body:
        out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
    out.append('</tbody></table></div>')
    return ''.join(out)


def _list(lines):
    """lines: list items with indentation; two levels."""
    out, stack = [], []
    for ln in lines:
        ind = len(ln) - len(ln.lstrip(' '))
        level = 0 if ind < 2 else 1
        txt = ln.strip()
        ordered = bool(re.match(r'\d+[.)]\s', txt))
        txt = re.sub(r'^(?:[-*+]|\d+[.)])\s+', '', txt)
        tag = 'ol' if ordered else 'ul'
        while len(stack) > level + 1:
            out.append(f'</li></{stack.pop()}>')
        if len(stack) == level + 1:
            out.append('</li>')
        else:
            out.append(f'<{tag}>')
            stack.append(tag)
        out.append(f'<li>{inline(txt)}')
    while stack:
        out.append(f'</li></{stack.pop()}>')
    return ''.join(out)


def to_html(md, id_prefix=''):
    lines = md.replace('\r\n', '\n').split('\n')
    out, i, n = [], 0, len(lines)
    is_item = lambda l: re.match(r'^\s*(?:[-*+]|\d+[.)])\s+', l)
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s.startswith('```'):
            j = i + 1
            while j < n and not lines[j].strip().startswith('```'):
                j += 1
            out.append('<pre><code>' + html.escape('\n'.join(lines[i + 1:j])) + '</code></pre>')
            i = j + 1
            continue
        if s.startswith(':::'):
            cls = s[3:].strip()
            j, depth = i + 1, 1
            while j < n:
                t = lines[j].strip()
                if t.startswith(':::'):
                    depth += 1 if t[3:].strip() else -1
                    if depth == 0:
                        break
                j += 1
            out.append(f'<div class="{html.escape(cls)}">' + to_html('\n'.join(lines[i + 1:j]), id_prefix) + '</div>')
            i = j + 1
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            lvl = len(m.group(1))
            txt = m.group(2).strip()
            out.append(f'<h{lvl} id="{id_prefix}{slugify(re.sub(r"[`*]", "", txt))}">{inline(txt)}</h{lvl}>')
            i += 1
            continue
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', s):
            out.append('<hr>')
            i += 1
            continue
        if s.startswith('|') and i + 1 < n and re.match(r'^\|?\s*:?-{2,}', lines[i + 1].strip()):
            j = i
            while j < n and lines[j].strip().startswith('|'):
                j += 1
            out.append(_table(lines[i:j]))
            i = j
            continue
        if s.startswith('>'):
            j = i
            while j < n and lines[j].strip().startswith('>'):
                j += 1
            out.append('<blockquote>' + to_html('\n'.join(l.strip()[1:].lstrip() for l in lines[i:j]), id_prefix) + '</blockquote>')
            i = j
            continue
        if is_item(ln):
            j, items = i, []
            while j < n and (is_item(lines[j]) or (lines[j].startswith('  ') and lines[j].strip() and items)):
                if is_item(lines[j]):
                    items.append(lines[j].rstrip())
                else:
                    items[-1] += ' ' + lines[j].strip()
                j += 1
            out.append(_list(items))
            i = j
            continue
        if s.startswith('@@RAW') and s.endswith('@@'):
            out.append(s)
            i += 1
            continue
        j, para = i, []
        while j < n and lines[j].strip() and not re.match(r'^(#{1,6}\s|```|:::|>|\|)', lines[j].strip()) and not is_item(lines[j]):
            para.append(lines[j].strip())
            j += 1
        out.append('<p>' + inline(' '.join(para)) + '</p>')
        i = j
    return '\n'.join(out)


def plain(md):
    """Markdown to plain text for decks and .pptx (markers kept as bracket text)."""
    s = re.sub(r'`([^`]*)`', r'\1', md)
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\1', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'\1', s)
    s = re.sub(r'^#{1,6}\s+', '', s, flags=re.M)
    s = re.sub(r'^:::.*$', '', s, flags=re.M)
    return s.strip()


if __name__ == '__main__':
    # self-check
    t = to_html('# A\n\nSome **b** and *i* [x](y.html) `[PLACEHOLDER: z]`\n\n- one\n  - two\n- three\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n::: socket\ninside [LOCAL EXPERT: TCU faculty or knowledge holder]\n:::\n')
    assert '<h1 id="a">' in t and '<strong>b</strong>' in t and '<em>i</em>' in t and 'mk-place' in t
    assert t.count('<ul>') == 2 and '<table>' in t and 'class="socket"' in t and 'mk-local' in t
    print('mdlite ok')
