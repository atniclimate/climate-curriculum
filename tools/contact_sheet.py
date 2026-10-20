"""Render PDF pages to PNG for visual review: one contact sheet, or single pages.

  python tools/contact_sheet.py <pdf> <out.png> [--pages 1-8] [--cols 4] [--dpi 40]
  python tools/contact_sheet.py <pdf> <outdir> --each [--pages 3,7,26] [--dpi 110]

Used by people and by the print-visual-qa workflow (.claude/workflows/).
"""
import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF


def pages(spec, count):
    if not spec:
        return list(range(count))
    out = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        lo, hi = int(a), int(b or a)
        if not 1 <= lo <= hi:  # "0" would wrap to the last page; "5-3" would select nothing
            sys.exit(f"bad page range {part!r}")
        out += range(lo - 1, min(count, hi))
    if not out:
        sys.exit(f"no pages in {spec!r}; the PDF has {count}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("out")
    ap.add_argument("--pages"); ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--dpi", type=int, default=40); ap.add_argument("--each", action="store_true")
    a = ap.parse_args()
    d = fitz.open(a.pdf)
    sel = pages(a.pages, d.page_count)
    if a.each:
        Path(a.out).mkdir(parents=True, exist_ok=True)
        for p in sel:
            f = Path(a.out) / f"p{p + 1:02d}.png"
            d[p].get_pixmap(dpi=a.dpi).save(f)
            print(f)
        return
    W, H, gap = d[0].rect.width, d[0].rect.height, 20
    rows = (len(sel) + a.cols - 1) // a.cols
    sheet = fitz.open()
    pg = sheet.new_page(width=a.cols * W + (a.cols + 1) * gap, height=rows * H + (rows + 1) * gap)
    pg.draw_rect(pg.rect, fill=(0.6, 0.6, 0.6))
    for n, p in enumerate(sel):
        r, c = divmod(n, a.cols)
        x, y = gap + c * (W + gap), gap + r * (H + gap)
        pg.show_pdf_page(fitz.Rect(x, y, x + W, y + H), d, p)
    pg.get_pixmap(dpi=a.dpi).save(a.out)
    print(a.out)


if __name__ == "__main__":
    main()
