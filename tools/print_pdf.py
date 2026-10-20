"""Print-ready PDFs of the curriculum documents (Letter, ATNI Climate type and color).

Run:  python tools/print_pdf.py          (writes docs/downloads/*.pdf)
Needs Google Chrome (headless print) and PyMuPDF (page numbers, bookmarks).
The Markdown files in curriculum/ stay the source; the PDFs are build output.
"""
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "downloads"
CHROME = [Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
          Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")]
PRINTED = "10/20/2026"

DOCS = [
    dict(src="curriculum/CRCCT_Grades6-12_Hands-On_Lessons.md", out="Grades-6-12-Hands-On-Lessons.pdf",
         kind="lessons", short="Grades 6 to 12 Hands-On Lessons",
         cover_title="Grades 6 to 12<br>Hands-On Lessons"),
    dict(src="curriculum/Understanding-a-Climate-of-Change_Guiding-Document.md",
         out="Understanding-a-Climate-of-Change-Guiding-Document.pdf",
         kind="guiding", short="Guiding Document and Language Revision",
         cover_title="Guiding Document<br>and Language Revision"),
]
QUESTIONS = ["How does a cloud work?", "How do you know what you know?",
             "What can we do?", "How do we work together?"]
WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4}

# ---------- Markdown (only what these documents use) ----------

def inline(s):
    toks = []
    def keep(h):
        toks.append(h)
        return f"\x00{len(toks) - 1}\x00"
    s = html.escape(s, quote=False)
    def code(m):
        t = m.group(1)
        if t.startswith("[PLACEHOLDER"):
            return keep(f'<span class="ph">{t[1:-1]}</span>')
        if t.lower().startswith("[verify"):
            return keep(f'<span class="vf">{t[1:-1]}</span>')
        return keep(f"<code>{t}</code>")
    s = re.sub(r"`([^`]+)`", code, s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", lambda m: keep(f'<a href="{m.group(2)}">{m.group(1)}</a>'), s)
    def url(m):
        u = m.group(0).rstrip(".,;:")
        return keep(f'<a class="url" href="{u}">{u}</a>') + m.group(0)[len(u):]
    s = re.sub(r"https?://[^\s<)\]]+", url, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: toks[int(m.group(1))], s)


def blocks(lines):
    """Markdown lines -> list of blocks: {'t': 'h'|'hr'|'html', ...}."""
    out, para, i = [], [], 0
    def flush():
        if para:
            out.append({"t": "html", "html": f"<p>{inline(' '.join(para))}</p>", "text": " ".join(para)})
            para.clear()
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            flush(); i += 1; continue
        if ln.strip() == "---":
            flush(); out.append({"t": "hr"}); i += 1; continue
        m = re.match(r"(#{1,6}) (.*)", ln)
        if m:
            flush(); out.append({"t": "h", "lvl": len(m.group(1)), "text": m.group(2).strip()}); i += 1; continue
        if ln.startswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            head, body = rows[0], [r for r in rows[2:]]
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            tb = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append({"t": "html", "html": f"<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>"}); continue
        if ln.startswith(">"):
            flush(); q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(re.sub(r"^> ?", "", lines[i].rstrip())); i += 1
            inner = "".join(b["html"] for b in blocks(q) if b["t"] == "html")
            out.append({"t": "html", "html": f"<blockquote>{inner}</blockquote>"}); continue
        m = re.match(r"(- |(\d+)\. )", ln)
        if m:
            flush(); ordered = bool(m.group(2)); items = []
            pat = r"\d+\. " if ordered else r"- "
            while i < len(lines) and re.match(pat, lines[i]):
                items.append(re.sub(pat, "", lines[i].rstrip(), count=1)); i += 1
            tag = "ol" if ordered else "ul"
            start = f' start="{m.group(2)}"' if ordered and m.group(2) != "1" else ""
            lis = "".join(f"<li>{inline(t)}</li>" for t in items)
            out.append({"t": "html", "html": f"<{tag}{start}>{lis}</{tag}>"}); continue
        para.append(ln.strip()); i += 1
    flush()
    return out

# ---------- Graphics ----------

def basin_svg(cls):
    m = json.loads((ROOT / "source" / "columbia_svg.json").read_text(encoding="utf-8"))
    tribs = "".join(f'<path d="{d}"/>' for d in m["tribs"])
    return (f'<svg class="{cls}" viewBox="0 0 {m["W"]:.0f} {m["H"]:.0f}" aria-hidden="true">'
            f'<path class="land" d="{m["land"]}"/><path class="lake" d="{m["lakes"]}"/>'
            f'<g class="trib">{tribs}</g><path class="main" d="{m["mainstem"]}"/>'
            f'<path class="main" d="{m["snake"]}"/><path class="main sal" d="{m["salmon"]}"/></svg>')


def four_questions():
    tiles = "".join(f'<div><span class="n">{n}</span><span class="q">{q}</span></div>'
                    for n, q in enumerate(QUESTIONS, 1))
    return f'<div class="fourq"><span class="label">Four questions, one river</span><div class="tiles">{tiles}</div></div>'

# ---------- Assembly ----------

def esc(s):
    return inline(s)


def assemble(doc, marks, tight=frozenset()):
    lines = (ROOT / doc["src"]).read_text(encoding="utf-8").splitlines()
    bl = blocks(lines)
    cut = next(i for i, b in enumerate(bl) if b["t"] == "hr")
    front, body = bl[:cut], bl[cut + 1:]
    title = next(b["text"] for b in front if b["t"] == "h" and b["lvl"] == 1)
    fpar = [b for b in front if b["t"] == "html"]
    # front matter: drop the "Draft for editing" line (the cover carries the printing date)
    fpar = [b for b in fpar if not b.get("text", "").startswith("Draft for editing")]

    toc, parts, n, i = [], [], 0, 0
    open_sec = False
    prev_h2 = False
    def anchor(text, level):
        nonlocal n
        n += 1
        toc.append((level, text, n))
        return f'<span class="mk">@@T{n:02d}@@</span>' if marks else ""
    while i < len(body):
        b = body[i]
        if b["t"] == "hr":
            i += 1; continue
        if b["t"] == "html":
            parts.append(b["html"]); prev_h2 = False; i += 1; continue
        lvl, text = b["lvl"], b["text"]
        if open_sec and lvl <= 3:
            parts.append("</section>"); open_sec = False
        # internal editor's table: not for facilitators
        if text.startswith("Editor's Note"):
            i += 1
            while i < len(body) and not (body[i]["t"] == "h" and body[i]["lvl"] <= lvl):
                i += 1
            continue
        if doc["kind"] == "lessons" and lvl == 2:
            m = re.match(r"Unit (\d): (.*)", text)
            if m:
                parts.append(f'<section class="opener"><span class="numeral">{m.group(1)}</span>'
                             f'<span class="label red">Unit {m.group(1)}</span><h2>{anchor(text, 1)}{esc(m.group(2))}</h2>')
                i += 1
                while i < len(body) and body[i]["t"] != "h":
                    if body[i]["t"] == "html":
                        parts.append(body[i]["html"])
                    i += 1
                parts.append("</section>"); prev_h2 = True; continue
            brk = " class=\"brk\"" if text in ("Opening Lesson", "Closing Lesson", "Columbia River Background for Teachers",
                                                "Standards Alignment") else ""
            parts.append(f'<h2{brk}>{anchor(text, 1)}{esc(text)}</h2>'); prev_h2 = bool(brk); i += 1; continue
        if doc["kind"] == "lessons" and lvl == 3:
            m = re.match(r"(Lesson \d\.\d|Opening|Closing): (.*)", text)
            if m:
                brk = "" if prev_h2 else " brk"
                draft = m.group(1) == "Lesson 4.3"
                cls = "lsn" + (" draft" if draft else "") + (" tight" if len(toc) + 1 in tight else "")
                parts.append(f'<section class="{cls}">'); open_sec = True
                chip = '<span class="chip">Draft</span>' if draft else ""
                parts.append(f'<h3 class="lesson{brk}">{anchor(text, 2)}<span class="label red">{m.group(1)}{chip}</span>'
                             f'<span class="t">{esc(m.group(2))}</span></h3>')
                if draft:
                    parts.append('<div class="banner"><b>Draft, under review. Not ready to teach.</b> This lesson asks '
                                 'students to role-play Tribal governments at a consultation table. ATNI Climate is '
                                 'revising it so that no student speaks as a Nation, council, Elder, or knowledge holder. '
                                 'It is printed here for facilitator review only.</div>')
                prev_h2 = False; i += 1; continue
        if doc["kind"] == "guiding" and lvl == 2:
            i += 1; continue  # subtitle, on the cover
        if doc["kind"] == "guiding" and lvl == 3:
            m = re.match(r"Part (One|Two|Three|Four): (.*)", text)
            if m:
                k = WORDS[m.group(1)]
                parts.append(f'<section class="opener short"><span class="numeral">{k}</span>'
                             f'<span class="label red">Part {m.group(1)}</span><h2>{anchor(text, 1)}{esc(m.group(2))}</h2></section>')
                i += 1; prev_h2 = True; continue
            parts.append(f'<h2 class="sec">{anchor(text, 1)}{esc(text)}</h2>'); i += 1; prev_h2 = False; continue
        tag = {2: "h2", 3: "h3", 4: "h4"}.get(lvl, "h5")
        parts.append(f"<{tag}>{esc(text)}</{tag}>"); prev_h2 = False; i += 1
    if open_sec:
        parts.append("</section>")

    sub = next((b["text"] for b in front if b["t"] == "h" and b["lvl"] == 2), "")
    cover = (f'<section class="cover">{basin_svg("map")}<div class="fade top"></div><div class="fade bot"></div>'
             f'<img class="lockup" src="{(ROOT / "docs/img/atni-climate-lockup-on-dark.png").as_uri()}" alt="ATNI Climate">'
             f'<div class="cbody"><span class="label red">Columbia River Climate Change Teachers Program</span>'
             f'<p class="series">{esc(title.split(":")[0])}</p><h1>{doc["cover_title"]}</h1>'
             f'<p class="by">Patrick Freeland and Cayla Jones · ATNI Climate, Affiliated Tribes of Northwest Indians</p>'
             f'<p class="ed">Workshop printing, {PRINTED} · Draft for review</p></div></section>')
    rows = "".join(f'<li class="l{lv}"><span class="tt">{esc(t)}</span><span class="pg" data-k="{k}">000</span></li>'
                   for lv, t, k in toc)
    colo = "".join(b["html"] for b in fpar)
    contents = (f'<section class="contents">{four_questions()}<span class="label">Contents</span>'
                f'<ol class="toc">{rows}</ol><div class="colophon">{colo}'
                + (f"<p>{esc(sub)}.</p>" if sub else "") +
                f'<p>Printed {PRINTED} from the Markdown source in the public repository '
                f'https://github.com/atniclimate/climate-curriculum. Live workshop: '
                f'https://atniclimate.github.io/climate-curriculum/</p></div></section>')
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}: {doc["short"]}</title>'
            f'<style>{css(doc)}</style></head><body>{cover}{contents}<main>{"".join(parts)}</main></body></html>')
    return page, toc


def css(doc):
    f = (ROOT / "docs" / "fonts").as_uri()
    foot = f"Understanding a Climate of Change · {doc['short']}"
    return f"""
@font-face{{font-family:"League Spartan";src:url({f}/league-spartan.woff2) format("woff2");font-weight:100 900}}
@font-face{{font-family:"Lexend Deca";src:url({f}/lexend-deca.woff2) format("woff2");font-weight:100 900}}
@font-face{{font-family:"Cascadia Code";src:url({f}/cascadia-code.woff2) format("woff2");font-weight:200 700}}
@page{{size:letter;margin:.72in .75in .8in;
  @bottom-left{{content:"{foot}";font:400 7pt "Lexend Deca";color:#6B7380;letter-spacing:.02em}}
  @bottom-right{{content:counter(page);font:700 8pt "League Spartan";color:#C0302A}}}}
@page :first{{margin:0;@bottom-left{{content:none}}@bottom-right{{content:none}}}}
:root{{--ink:#15191E;--muted:#5B6370;--red:#E13D33;--red-t:#B8291F;--hair:#D6DAE0;--wash:#F4F5F7;--base:#010B13;--water:#5E97C9;--magenta:#9732B4}}
*{{box-sizing:border-box}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{margin:0;font:400 8.8pt/1.45 "Lexend Deca","Segoe UI",sans-serif;color:var(--ink);font-kerning:normal;hyphens:manual}}
p{{margin:0 0 .55em;orphans:3;widows:3;text-wrap:pretty}}
a{{color:var(--ink);text-decoration:none;border-bottom:.5pt solid #A9B0BA}}
a.url{{overflow-wrap:anywhere;font-size:.94em}}
strong{{font-weight:600;color:#000}}
code{{font:400 .9em "Cascadia Code",Consolas,monospace}}
.label{{display:block;font:600 7.4pt "League Spartan",sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}}
.label.red{{color:var(--red-t)}}
h1,h2,h3,h4,h5{{font-family:"League Spartan","Century Gothic",sans-serif;color:#000;margin:0;break-after:avoid;text-wrap:balance;position:relative}}
h2{{font-size:20pt;font-weight:700;letter-spacing:-.015em;line-height:1.1;margin:1.1em 0 .5em;padding-top:.35em;border-top:2.5pt solid var(--red)}}
h2.brk,.brk{{break-before:page}}
h2.sec{{font-size:15pt;border-top:1pt solid var(--ink);padding-top:.4em}}
h3{{font-size:12.5pt;font-weight:700;margin:1.2em 0 .35em;line-height:1.2}}
h3.lesson{{margin:0 0 .7em;padding:0 0 .55em;border-bottom:1pt solid var(--hair)}}
h3.lesson .t{{display:block;font-size:19pt;line-height:1.12;letter-spacing:-.015em;margin-top:.15em}}
h3.lesson .label{{font-size:8.5pt}}
h4{{font:600 7.6pt "League Spartan";letter-spacing:.16em;text-transform:uppercase;color:var(--red-t);margin:1.2em 0 .35em}}
h5{{font-size:10pt;margin:1em 0 .3em}}
.mk{{position:absolute;left:0;top:0;font-size:5px;color:#fff;line-height:1;white-space:nowrap}}
ul,ol{{margin:0 0 .7em;padding-left:1.25em}}
li{{margin:0 0 .22em;padding-left:.1em}}
ul{{list-style:none;padding-left:1em}}
ul>li{{position:relative}}
ul>li::before{{content:"";position:absolute;left:-.95em;top:.6em;width:.32em;height:.32em;background:var(--red)}}
ol>li::marker{{font:700 9pt "League Spartan";color:var(--red-t)}}
table{{width:100%;border-collapse:collapse;margin:.4em 0 1em;font-size:8pt;line-height:1.38;break-inside:auto}}
thead{{display:table-header-group}}
th{{background:var(--base);color:#fff;text-align:left;font:600 7pt "League Spartan";letter-spacing:.1em;text-transform:uppercase;padding:5pt 6pt;vertical-align:bottom}}
td{{padding:4.5pt 6pt;border-bottom:.5pt solid var(--hair);vertical-align:top}}
tr{{break-inside:avoid}}
tbody tr:nth-child(even) td{{background:var(--wash)}}
blockquote{{margin:.3em 0 .9em;padding:.2em 0 .2em 1em;border-left:2pt solid #B9C0C9;color:#3A414B;font-size:.95em}}
blockquote p:last-child{{margin-bottom:0}}
.ph{{background:#F3E8F7;color:#5E1F72;border:.5pt solid #C99BD9;padding:0 .3em;font-size:.92em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.vf{{background:#FFF4D6;color:#6B4E00;padding:0 .3em;font-size:.92em}}
/* cover */
.cover{{width:8.5in;height:11in;background:var(--base);color:#fff;position:relative;overflow:hidden;break-after:page}}
.cover .map{{position:absolute;right:-1.1in;top:1.35in;width:9.2in;height:auto}}
.map .land{{fill:#0E1720;stroke:#24303C;stroke-width:.8}}
.map .lake{{fill:#16314A}}
.map .trib path{{fill:none;stroke:#2F5677;stroke-width:1.1}}
.map .main{{fill:none;stroke:#9CC7F0;stroke-width:3;stroke-linejoin:round}}
.map .sal{{stroke:#E13D33;stroke-width:3.2}}
.cover .fade{{position:absolute;left:0;right:0}}
.cover .fade.top{{top:1.3in;height:1.1in;background:linear-gradient(to bottom,var(--base),rgba(1,11,19,0))}}
.cover .fade.bot{{bottom:0;height:5.2in;background:linear-gradient(to top,var(--base) 52%,rgba(1,11,19,0))}}
.cover .lockup{{position:absolute;left:.78in;top:.7in;height:.62in;width:auto}}
.cover .cbody{{position:absolute;left:.78in;right:.78in;bottom:.85in;padding-top:.28in;border-top:3pt solid var(--red)}}
.cover .label{{color:#F26B5E;font-size:8.5pt}}
.cover .series{{font:700 13pt "League Spartan";letter-spacing:.06em;text-transform:uppercase;margin:.6em 0 .25em;color:#E8ECF0}}
.cover h1{{font:700 40pt/1.0 "League Spartan";letter-spacing:-.01em;text-transform:uppercase;color:#fff;margin:0 0 .45em}}
.cover .by{{font-size:9.5pt;color:#E8ECF0;margin:0 0 .2em}}
.cover .ed{{font:400 8.5pt "Cascadia Code",monospace;color:#8A94A6;margin:0}}
/* contents */
.contents{{break-after:page}}
.fourq{{margin:0 0 .2in}}
.fourq .tiles{{display:grid;grid-template-columns:repeat(4,1fr);gap:5pt;margin-top:6pt}}
.fourq .tiles div{{background:var(--base);color:#fff;padding:9pt 9pt 11pt;display:grid;gap:4pt;align-content:start;border-top:3pt solid var(--red)}}
.fourq .n{{font:800 22pt/1 "League Spartan";color:#fff}}
.fourq .q{{font:600 9pt/1.2 "League Spartan";color:#E8ECF0}}
.toc{{list-style:none;padding:0;margin:6pt 0 .25in;border-top:1pt solid var(--ink)}}
.toc li{{display:flex;align-items:baseline;gap:8pt;margin:0;padding:1.6pt 0;border-bottom:.5pt solid var(--hair)}}
.toc li::before{{display:none}}
.toc .tt{{flex:1}}
.toc .l1 .tt{{font:700 10pt "League Spartan"}}
.toc .l2{{padding-left:1.1em;font-size:8.6pt;color:#2A3038}}
.toc .pg{{font:700 9pt "League Spartan";color:var(--red-t);min-width:2.2em;text-align:right;font-variant-numeric:tabular-nums}}
.colophon{{font-size:7.8pt;color:var(--muted);border-top:.5pt solid var(--hair);padding-top:8pt}}
.colophon p{{margin:0 0 .45em;max-width:none}}
/* openers */
.opener{{break-before:page;break-after:page;position:relative;padding-top:2.2in;min-height:8.6in}}
.opener.short{{break-after:auto;min-height:0;padding-top:1.05in;margin-bottom:.15in}}
.opener.short .numeral{{font-size:84pt}}
.opener.short h2{{font-size:24pt}}
.opener .numeral{{position:absolute;top:0;left:-.06in;font:800 150pt/1 "League Spartan";color:var(--red);letter-spacing:-.04em}}
.opener h2{{border:0;padding:0;margin:.15em 0 .6em;font-size:30pt;line-height:1.05}}
.opener .label{{font-size:9pt}}
.opener p{{font-size:10.5pt;line-height:1.55;max-width:5.6in}}
.opener + h3.lesson, .opener + section > h3.lesson{{break-before:page}}
/* draft lesson */
.draft{{border-left:3pt solid var(--red);padding-left:11pt}}
.tight{{font-size:8.3pt;line-height:1.42}}
.chip{{display:inline-block;margin-left:8pt;padding:1pt 6pt;background:var(--red);color:#fff;letter-spacing:.14em}}
.banner{{background:#FCEBEA;border:1pt solid var(--red);padding:8pt 10pt;margin:0 0 1em;font-size:9pt}}
.banner b{{color:var(--red-t)}}
"""

# ---------- Build ----------

def chrome():
    for c in CHROME:
        if c.exists():
            return c
    sys.exit("Chrome or Edge not found")


def render(page_html, pdf, tmp):
    src = tmp / "page.html"
    src.write_text(page_html, encoding="utf-8")
    prof = tmp / "profile"
    r = subprocess.run([str(chrome()), "--headless=new", f"--user-data-dir={prof}", "--no-first-run",
                        "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                        f"--print-to-pdf={pdf}", src.as_uri()], capture_output=True, text=True, timeout=180)
    if not pdf.exists():
        sys.exit(f"Chrome did not write {pdf}: {r.stderr[-800:]}")


def build(doc):
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        tight, found, toc, pages1 = set(), {}, [], 0
        for _ in range(3):  # pass 1, plus up to two refits of lessons that spill a few lines onto a new page
            page, toc = assemble(doc, marks=True, tight=frozenset(tight))
            p1 = tmp / "pass1.pdf"
            render(page, p1, tmp)
            found = {}
            with fitz.open(p1) as d:
                txt = [str(d[p].get_text(sort=True)) for p in range(d.page_count)]
                pages1 = d.page_count
            for pno, t in enumerate(txt):
                for m in re.findall(r"@@T(\d\d)@@", t):
                    found.setdefault(int(m), pno + 1)
            missing = [k for _, _, k in toc if k not in found]
            assert not missing, f"headings not found in pass 1: {missing}"
            spill = {p + 1 for p in range(2, len(txt)) if len(txt[p].split()) < 120 and "@@T" not in txt[p]}
            def owner(s):  # the lesson that started last before spill page s
                ks = [k for lv, _, k in toc if lv == 2 and found[k] < s]
                return ks[-1] if ks else None
            refit = {owner(s) for s in spill} - {None} - tight
            if not refit:
                break
            tight |= refit
        page, _ = assemble(doc, marks=False, tight=frozenset(tight))
        page = re.sub(r'<span class="pg" data-k="(\d+)">000</span>',
                      lambda m: f'<span class="pg">{found[int(m.group(1))]}</span>', page)
        assert chr(0x2014) not in page, "em dash in printed text"
        p2 = tmp / "pass2.pdf"
        render(page, p2, tmp)
        with fitz.open(p2) as d:
            assert d.page_count == pages1, "pass 2 page count changed; contents numbers may be off"
            # a page with only a line or two of text is usually a lesson spilling over; report it for a layout fix
            txt = [str(d[p].get_text(sort=True)) for p in range(d.page_count)]
            sparse = [p + 1 for p in range(2, d.page_count) if len(txt[p].split()) < 120
                      and not re.match(r"\s*\d\s+(U N I T|P A R T)", txt[p])]  # openers are short on purpose
            if sparse:
                print(f"  sparse pages to look at: {sparse}")
            d.set_toc([[lv, re.sub(r"\s+", " ", txt), found[k]] for lv, txt, k in toc])
            d.set_metadata({"title": f"Understanding a Climate of Change: {doc['short']}",
                            "author": "Patrick Freeland and Cayla Jones, ATNI Climate",
                            "subject": "Columbia River Climate Change Teachers Program",
                            "creator": "tools/print_pdf.py"})
            OUT.mkdir(parents=True, exist_ok=True)
            d.save(OUT / doc["out"], garbage=3, deflate=True)
            print(f"{doc['out']}: {d.page_count} pages, {len(toc)} contents entries")


if __name__ == "__main__":
    want = sys.argv[1:]
    for doc in DOCS:
        if not want or doc["kind"] in want:
            build(doc)
