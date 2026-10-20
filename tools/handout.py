"""One-page event handout for the Yakama workshop (Letter, ATNI Climate type and color).

Run:  python tools/handout.py                    (office and bleed PDFs to private/craft/handout/)
      python tools/handout.py office --out docs/downloads   (the published copy, after approval)
      python tools/handout.py photo              (remake source/handout/gorge-band.jpg; reads private/)
Two outputs from one page: office (US Letter, 0.25 in white safe frame, nothing printed in it)
and bleed (8.75 x 11.25 in: art runs 0.125 in past the trim on every side, type stays 0.375 in
inside it; TrimBox and BleedBox are set). Needs Google Chrome (headless print) and PyMuPDF.
Renders from tracked files only: docs/fonts/, docs/img/, source/handout/, source/columbia_svg.json.
"""
import base64
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "private" / "craft" / "handout"
SRC = ROOT / "source" / "handout"
CHROME = [Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
          Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")]
PRINTED = "10/20/2026"
KINDS = {"office": "Understanding-a-Climate-of-Change-Handout.pdf",
         "bleed": "Understanding-a-Climate-of-Change-Handout-bleed.pdf"}

# Band photo: placed 8.75 in wide in both outputs (the office frame shows its middle 8.0 in).
BAND_W, BAND_H, BAND_TOP = 8.75, 1.68, 7.93   # inches; BAND_TOP from the trim

# lon/lat to columbia_svg.json map units. Affine fit to the 17 dam points in its `pts`
# (rms 1.7 units, max 3.8, on a 1000-unit-wide map; the JSON does not store its projection).
PROJ = ((88.7462, 1.6944, 10984.6263), (0.7891, -126.3834, 6338.1197))
TOPPENISH = (-120.308, 46.377)
LOWER_GRANITE = (-117.4286, 46.6603)  # self-check point, pts["lowergranite"] = (640.2, 347.7)


def project(lon, lat):
    (a, b, c), (d, e, f) = PROJ
    return a * lon + b * lat + c, d * lon + e * lat + f

# ---------- Content (Patrick's rulings of 10/20/2026) ----------

ROOT_URL = "atniclimate.github.io/climate-curriculum/"
QUESTIONS = ["How does a cloud work?", "How do you know what you know?",
             "What can we do?", "How do we work together?"]
PAPERS = [  # (citation, path or URL line, annotation)
    (f'Freeland, P. A. (2026). <i>Understanding a climate of change</i> [Interactive workshop]. '
     f'ATNI Climate, Affiliated Tribes of Northwest Indians.', "", ""),
    (f'Freeland, P. A., &amp; Jones, C. (2026). <i>Understanding a climate of change: Guiding document and '
     f'language revision</i> (Workshop printing, 10/20/2026; draft for review). ATNI Climate.',
     "downloads/Understanding-a-Climate-of-Change-Guiding-Document.pdf", ""),
    (f'Freeland, P. A. (2026). <i>Understanding a climate of change: Grades 6 to 12 hands-on lessons</i> '
     f'(Workshop printing, 10/20/2026; draft for review). ATNI Climate.',
     "downloads/Grades-6-12-Hands-On-Lessons.pdf", ""),
    ('ATNI Climate. (2026). <i>Dynamic Drought Module</i> [Interactive map].',
     "https://atniclimate.github.io/dynamic-drought-module/", "Shown in the same slot; a separate site."),
    ('Robinson, S. (n.d.). <i>Climate change and the Tribes: Columbia River edition</i> [Unpublished draft '
     'curriculum]. The Indigenous Climate Project, with the Affiliated Tribes of Northwest Indians, the Columbia '
     'River Inter-Tribal Fish Commission, Pacific Education Institute, and Washington Wild.',
     "", "The original source for the lessons; in copy-edit and layout."),
]
ORGS = ['Yakama Nation <span class="m">(host)</span>', "Indigenous Climate Project", "Washington Wild",
        "Pacific Education Institute (PEI)", "Affiliated Tribes of Northwest Indians (ATNI), ATNI Climate"]
TEAM = [("Tom Uniack", "Washington Wild"), ("Megan Rivard", "Pacific Education Institute"),
        ("Cayla Jones", "Yakama Nation Fisheries"), ("Kyle Shields", "Yakama Nation"),
        ("Phil Rigdon", "Yakama Nation"), ("Elese Washines", "Yakama Nation"),
        ("Dawn Vyvyan", ""), ("Christine Jong", "ATNI"), ("Reuben Martinez", "ATNI"),
        ("Amber Schulz-Oliver", "ATNI"), ("Steve Robinson", "")]

# ---------- Graphics ----------

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(Path(p).read_bytes()).decode()


def qr_svg():
    s = (SRC / "qr.svg").read_text(encoding="utf-8")
    s = s[s.index("<svg"):].replace('fill="#343334"', 'fill="#010B13"')
    return s.replace('width="144" height="144"', 'width="100%" height="100%" role="img" '
                     'aria-label="QR code to https://atniclimate.github.io/climate-curriculum/"', 1)


def basin_mark():
    m = json.loads((ROOT / "source" / "columbia_svg.json").read_text(encoding="utf-8"))
    x, y = project(*TOPPENISH)
    tribs = "".join(f'<path d="{d}"/>' for d in m["tribs"])
    return (f'<svg class="basin" viewBox="0 0 {m["W"]:.0f} {m["H"]:.0f}" role="img" '
            f'aria-label="Columbia River basin map; the red dot marks Toppenish">'
            f'<path class="land" d="{m["land"]}"/><path class="lake" d="{m["lakes"]}"/>'
            f'<g class="trib">{tribs}</g><path class="main" d="{m["mainstem"]}"/><path class="main" d="{m["snake"]}"/>'
            f'<circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="30"/></svg>')


def make_photo():
    """Crop and grade the band from the stripped copy (EXIF and GPS already removed). Not run at render."""
    from PIL import Image, ImageEnhance
    src = Image.open(ROOT / "private/print-assets/gorge-dusk-4251.jpg").convert("RGB")
    w = 3600                               # drops the white blob in the far right corner
    h = round(w * BAND_H / BAND_W)
    bottom = 2010                          # keeps the river glint and the rock outcrop; cuts the pole's foot
    im = src.crop((0, bottom - h, w, bottom))
    im = im.point([round(255 * (i / 255) ** 0.92) for i in range(256)] * 3)  # midtone lift: office printers print dark
    im = ImageEnhance.Contrast(im).enhance(1.06)
    SRC.mkdir(parents=True, exist_ok=True)
    im.save(SRC / "gorge-band.jpg", quality=90, optimize=True)  # no exif= argument: nothing carried over
    with Image.open(SRC / "gorge-band.jpg") as chk:
        assert not chk.getexif() and "exif" not in chk.info, "EXIF in the band photo"
    print(f"gorge-band.jpg {im.width}x{im.height} px, {im.width / BAND_W:.0f} ppi at {BAND_W} in")

# ---------- Page ----------

def page(kind):
    bleed = kind == "bleed"
    B = .125 if bleed else 0        # trim offset on the sheet
    E = -.125 if bleed else .25     # where art stops, measured from the trim (negative = into the bleed)
    pw, ph = 8.5 + 2 * B, 11 + 2 * B
    f = {n: b64(ROOT / f"docs/fonts/{n}.woff2", "font/woff2") for n in ("league-spartan", "lexend-deca", "cascadia-code")}
    qs = "".join(f'<li><span class="n">{i}</span>{q}</li>' for i, q in enumerate(QUESTIONS, 1))
    papers = "".join(
        f'<li><span class="n">{i}</span><div><p>{c}</p>'
        + (f'<p class="u">{u}</p>' if u else "") + (f'<p class="an">{a}</p>' if a else "") + "</div></li>"
        for i, (c, u, a) in enumerate(PAPERS, 1))
    orgs = "".join(f"<li>{o}</li>" for o in ORGS)
    team = "".join(f"<li><b>{n}</b>{(', <span class=\"m\">' + a + '</span>') if a else ''}</li>" for n, a in TEAM)
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Understanding a Climate of Change: Teachers Climate Change Workshop at Yakama Nation</title>
<style>
@font-face{{font-family:"League Spartan";src:url({f['league-spartan']}) format("woff2");font-weight:100 900}}
@font-face{{font-family:"Lexend Deca";src:url({f['lexend-deca']}) format("woff2");font-weight:100 900}}
@font-face{{font-family:"Cascadia Code";src:url({f['cascadia-code']}) format("woff2");font-weight:200 700}}
@page{{size:{pw}in {ph}in;margin:0}}
:root{{--red:#E13D33;--red-t:#B8291F;--base:#010B13;--ink:#15191E;--muted:#5B6370;--hair:#D6DAE0;--sky:#9CC7F0;--water:#5E97C9;
  --e:{E}in;--d:50pt;--l:13pt;--b:9.6pt;--s:7.5pt}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{width:{pw}in;height:{ph}in;overflow:hidden;position:relative;background:#fff;color:var(--ink);
  font:400 var(--b)/1.42 "Lexend Deca",sans-serif;font-kerning:normal}}
.sheet{{position:absolute;left:{B}in;top:{B}in;width:8.5in;height:11in}}
ul,ol{{list-style:none}}
.lbl{{display:flex;align-items:baseline;gap:.08in;font:600 var(--s)/1 "League Spartan";letter-spacing:.16em;text-transform:uppercase;
  color:var(--base);padding-bottom:.06in;margin-bottom:.07in;border-bottom:.6pt solid var(--hair)}}
.lbl .no{{font:700 var(--s)/1 "Cascadia Code";letter-spacing:0;color:var(--red-t)}}
.cf{{font:400 var(--s)/1 "Cascadia Code";color:var(--red-t);border-bottom:.6pt dotted var(--red-t);text-transform:none;letter-spacing:0}}

/* art boxes run to var(--e); their padding brings type back to the same place on the trim */
.tab{{position:absolute;left:var(--e);right:var(--e);top:var(--e);height:calc(.8in - var(--e));background:var(--red-t);color:#fff;
  display:flex;justify-content:space-between;align-items:center;padding:calc(.28in - var(--e)) calc(.5in - var(--e)) 0;
  font:600 var(--s)/1.4 "League Spartan",sans-serif;letter-spacing:.15em;text-transform:uppercase}}
.tab .ev{{text-align:right}}

.main{{position:absolute;left:.5in;right:.5in;top:.92in}}
.head{{display:grid;grid-template-columns:1fr 1.32in;column-gap:.3in;align-items:start}}
h1{{font:800 var(--d)/.86 "League Spartan",sans-serif;letter-spacing:-.035em;color:var(--base)}}
h1 span{{display:block}}
h1 .r{{color:var(--red)}}
.by{{margin-top:.13in;color:var(--muted)}}
.by b{{font-weight:500;color:var(--base)}}
.qr .tile{{width:1.32in;height:1.32in;padding:.08in;background:#fff;border:.75pt solid var(--hair)}}
.qr .tile svg{{display:block}}
.qr .lab{{display:block;font:600 var(--s)/1.2 "League Spartan";letter-spacing:.15em;text-transform:uppercase;color:var(--red-t);margin:.09in 0 .03in}}
.qr .url{{font:400 var(--s)/1.3 "Cascadia Code",monospace;color:var(--ink)}}
.rule{{margin-top:.12in;border-top:2.5pt solid var(--base);position:relative}}
.rule::after{{content:"";position:absolute;left:0;top:-2.5pt;width:1.32in;border-top:2.5pt solid var(--red)}}

.body{{margin-top:.14in;display:grid;grid-template-columns:3.95in 1fr;column-gap:.32in}}
.abs{{line-height:1.38;text-wrap:pretty}}
.abs b{{font-weight:600;color:var(--base)}}
.qs{{display:grid;grid-template-columns:1.6in 1fr;gap:.05in .15in;margin:.07in 0 .08in;padding:.06in 0;
  border-top:.6pt solid var(--hair);border-bottom:.6pt solid var(--hair)}}
.qs li{{display:grid;grid-template-columns:.16in 1fr;font:600 var(--b)/1.2 "League Spartan";color:var(--base)}}
.qs .n{{color:var(--muted)}}
.use{{margin-top:.1in}}
.use li{{display:grid;grid-template-columns:.82in 1fr;column-gap:.1in;align-items:baseline;padding:.06in 0;border-bottom:.6pt solid var(--hair)}}
.use li:last-child{{border-bottom:0}}
.use .k{{display:flex;gap:2.5pt}}
kbd{{display:inline-block;min-width:13pt;height:13pt;padding:0 2.5pt;border:.8pt solid var(--base);border-bottom-width:1.8pt;border-radius:2pt;
  font:600 var(--s)/11pt "Cascadia Code";text-align:center;color:var(--base)}}
.use .tag{{font:700 var(--s)/13pt "Cascadia Code";color:var(--red-t)}}
.use p{{line-height:1.36}}
.use p b{{font:700 var(--b) "League Spartan";color:var(--base)}}
.use code{{font:400 .9em "Cascadia Code",monospace;color:var(--base)}}

.root{{font:400 var(--s)/1.3 "Lexend Deca";color:var(--muted);margin-bottom:.03in}}
.root span{{font-family:"Cascadia Code";color:var(--ink)}}
.papers li{{display:grid;grid-template-columns:.17in 1fr;padding:.03in 0;border-bottom:.6pt solid var(--hair)}}
.papers li:last-child{{border-bottom:0}}
.papers .n{{font:800 var(--b)/1 "League Spartan";color:var(--red-t);padding-top:.5pt}}
.papers p{{font-size:var(--s);line-height:1.31;padding-left:.12in;text-indent:-.12in}}
.papers p+p{{text-indent:0;margin-top:1pt}}
.papers i{{color:var(--base)}}
.papers .u{{font-family:"Cascadia Code";color:var(--muted);overflow-wrap:anywhere}}
.papers .an{{color:var(--muted)}}

.band{{position:absolute;left:var(--e);right:var(--e);top:{BAND_TOP}in;height:{BAND_H}in;
  background:url({b64(SRC / 'gorge-band.jpg', 'image/jpeg')}) center/{BAND_W}in auto no-repeat}}
.band::after{{content:"";position:absolute;inset:0 0 -1px;background:linear-gradient(180deg,rgba(1,11,19,0) 64%,rgba(1,11,19,.5) 88%,var(--base) 100%)}}
.band .lead{{position:absolute;left:calc(4.6in - var(--e));right:calc(.5in - var(--e));top:.1in;z-index:1}}
.band .lead .lbl{{border-color:rgba(1,11,19,.35);margin-bottom:.07in}}
.band .lead .lbl .no{{color:var(--base)}}
.band .lead p{{font:600 var(--l)/1.18 "League Spartan";letter-spacing:-.005em;color:var(--base);text-align:right}}  /* ragged left follows the falling horizon */
.head{{position:relative}}
.where{{position:absolute;left:4.3in;top:.9in;width:1.7in}}  /* the open corner right of "a Climate" */
.basin{{display:block;width:.9in;height:auto}}
.basin .land{{fill:none;stroke:#9AA3AE;stroke-width:5}}  /* the coast: the Pacific edge places the river */
.basin .lake{{fill:var(--water)}}
.basin .trib path{{fill:none;stroke:var(--sky);stroke-width:6;stroke-linejoin:round}}
.basin .main{{fill:none;stroke:var(--water);stroke-width:18;stroke-linejoin:round;stroke-linecap:round}}
.basin .dot{{fill:var(--red);stroke:#fff;stroke-width:10}}
.where p{{margin-top:.04in;font:400 var(--s)/1.3 "Lexend Deca";color:var(--muted)}}
.where p::before{{content:"";display:inline-block;width:5pt;height:5pt;border-radius:50%;background:var(--red);margin-right:3pt}}

/* the footer starts .2 in up inside the band, where the scrim is already half to fully near-black */
.foot{{position:absolute;left:var(--e);right:var(--e);top:{BAND_TOP + BAND_H - .2:.2f}in;bottom:var(--e);color:#fff;z-index:1;
  background:linear-gradient(180deg,transparent .2in,var(--base) .2in);
  padding:0 calc(.5in - var(--e)) calc(.32in - var(--e));display:grid;grid-template-columns:2.25in 1fr;column-gap:.3in;
  grid-template-rows:auto 1fr}}
.foot h2{{font:600 var(--s)/1 "League Spartan";letter-spacing:.16em;text-transform:uppercase;color:var(--sky);margin-bottom:.06in}}
.foot li{{font:500 var(--s)/1.36 "Lexend Deca"}}
.foot .m{{color:#C9D2DC}}
.foot .team ul{{columns:2;column-gap:.16in}}
.foot .team li{{break-inside:avoid}}
.foot .team b{{font-weight:600}}
.foot .meta{{grid-column:1/-1;align-self:end;margin-top:.04in;padding-right:1.1in;font:500 var(--s)/1.3 "Lexend Deca";color:#C9D2DC}}  /* clear the logo */
.foot .logo{{position:absolute;right:calc(.5in - var(--e));bottom:calc(.39in - var(--e));width:.9in;height:auto;display:block}}
</style></head>
<body><div class="sheet">

<header class="tab">
  <span>Columbia River Climate Change<br>Teachers Program · ATNI Climate</span>
  <span class="ev">Teachers Climate Change Workshop at Yakama Nation<br>Toppenish · 10/23/2026 and 10/24/2026</span>
</header>

<div class="main">
<section class="head">
  <div>
    <h1><span>Understanding</span><span>a Climate</span><span class="r">of Change</span></h1>
    <p class="by"><b>Patrick A. Freeland</b> · ATNI Climate</p>
  </div>
  <div class="qr">
    <div class="tile">{qr_svg()}</div>
    <span class="lab">Scan for the live page</span>
    <span class="url">atniclimate.github.io/<br>climate-curriculum/</span>
  </div>
  <div class="where">{basin_mark()}<p>Toppenish, in the Columbia River basin</p></div>
</section>
<div class="rule"></div>

<section class="body">
  <div>
    <h2 class="lbl"><span class="no">01</span>The workshop</h2>
    <p class="abs"><b>Understanding a Climate of Change</b> is a free, interactive workshop that runs in a web browser,
    built for school Chromebooks, and works offline once downloaded. Four questions guide it:</p>
    <ol class="qs">{qs}</ol>
    <p class="abs">Teachers and students follow air from the Pacific over the Cascades, see what river and weather gauges record,
    travel the salmon's journey home past the dams, sort climate actions by job, and watch a stress, and care,
    ripple through a web of relatives.</p>
    <div class="use">
      <h2 class="lbl"><span class="no">02</span>How to use it</h2>
      <ul>
        <li><span class="k"><kbd>&larr;</kbd><kbd>&rarr;</kbd><kbd>N</kbd><kbd>T</kbd></span>
          <p><b>Present it.</b> Arrow keys move slides; N opens facilitator notes; T starts the clock.</p></li>
        <li><span class="tag">6 to 12</span>
          <p><b>Teach from it.</b> Every part has matching hands-on lessons for Grades 6 to 12.</p></li>
        <li><span class="tag">offline</span>
          <p><b>Take it offline.</b> Download the project from GitHub and open <code>docs/index.html</code>.</p></li>
      </ul>
    </div>
  </div>
  <div>
    <h2 class="lbl"><span class="no">03</span>Papers to take home</h2>
    <p class="root">1 to 3 at <span>{ROOT_URL}</span></p>
    <ol class="papers">{papers}</ol>
  </div>
</section>
</div>

<section class="band" aria-label="Columbia Gorge at dusk">
  <div class="lead">
    <h2 class="lbl"><span class="no">04</span>Acknowledgements</h2>
    <p>With gratitude to the Yakama Nation, whose homelands, waters, and people host this gathering.</p>
  </div>
</section>

<footer class="foot">
  <div><h2>Organizations</h2><ul>{orgs}</ul></div>
  <div class="team"><h2>Planning team</h2><ul>{team}</ul></div>
  <p class="meta">Suggested citation: Freeland, P. A. (2026). <i>Understanding a climate of change</i> [Event handout].<br>ATNI Climate. {ROOT_URL} · Photo: Patrick A. Freeland · Draft for review, printed {PRINTED}</p>
  <img class="logo" src="{b64(ROOT / 'docs/img/atni-climate-lockup-on-dark.png', 'image/png')}" alt="ATNI Climate">
</footer>

</div>
<script>/* the columns must clear the band; build() fails on this marker */
document.fonts.ready.then(()=>{{const b=document.querySelector('.body').getBoundingClientRect().bottom,
t=document.querySelector('.band').getBoundingClientRect().top;
if(b>t-4)document.body.insertAdjacentHTML('beforeend','<p style="position:absolute;top:0;left:0;z-index:9">LAYOUT OVERFLOW</p>')}})</script>
</body></html>
"""
    html = html.replace("Yakama Nation", "Yakama&nbsp;Nation")  # never splits across lines
    assert chr(0x2014) not in html, "em dash in printed text"
    return html

# ---------- Build ----------

def chrome():
    for c in CHROME:
        if c.exists():
            return c
    sys.exit("Chrome or Edge not found")


def build(kind):
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        src, pdf = tmp / "handout.html", tmp / "handout.pdf"
        src.write_text(page(kind), encoding="utf-8")
        r = subprocess.run([str(chrome()), "--headless=new", f"--user-data-dir={tmp / 'profile'}", "--no-first-run",
                            "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                            f"--print-to-pdf={pdf}", src.as_uri()], capture_output=True, text=True, timeout=180)
        if not pdf.exists():
            sys.exit(f"Chrome did not write {pdf}: {r.stderr[-800:]}")
        with fitz.open(pdf) as d:
            assert d.page_count == 1, f"{kind}: {d.page_count} pages; the handout must fit one"
            assert "LAYOUT OVERFLOW" not in d[0].get_text(), f"{kind}: the columns run into the photo band"
            if kind == "bleed":  # trim inset 9 pt (0.125 in) from the 8.75 x 11.25 in media
                p = d[0]
                p.set_bleedbox(p.mediabox)
                p.set_trimbox(fitz.Rect(9, 9, p.mediabox.width - 9, p.mediabox.height - 9))
            d.set_metadata({"title": "Understanding a Climate of Change: Teachers Climate Change Workshop at Yakama Nation",
                            "author": "Patrick A. Freeland, with ATNI Climate",
                            "subject": "Columbia River Climate Change Teachers Program",
                            "creator": "tools/handout.py"})
            OUT.mkdir(parents=True, exist_ok=True)
            d.save(OUT / KINDS[kind], garbage=3, deflate=True)
        print(f"{OUT / KINDS[kind]}: 1 page, {kind}")


if __name__ == "__main__":
    want = sys.argv[1:]
    if "--out" in want:  # docs/downloads is written only when named here
        i = want.index("--out")
        OUT = Path(want[i + 1]).resolve()
        del want[i:i + 2]
    tx, ty = project(*LOWER_GRANITE)
    assert abs(tx - 640.2) < 5 and abs(ty - 347.7) < 5, "basin projection drifted"
    if want == ["photo"]:
        make_photo()
        sys.exit()
    for kind in KINDS:
        if not want or kind in want:
            build(kind)
