# Launch Prompt

Paste the block below into the first Claude Code session in I:\climate-curriculum.
For later sessions, use the short "Resume" block at the bottom.

## First session

```
You are working in I:\climate-curriculum, a local clone of
github.com/atniclimate/climate-curriculum: the Columbia River Climate Change
Teachers curriculum and its interactive workshop "Understanding a Climate of
Change" (ATNI Climate; authors Patrick Freeland and Cayla Jones). I am Patrick.

The working rules, scope, and plan live in files, not in this prompt. Read
them first, in this order, and treat them as binding:
  1. CLAUDE.md                                (rules; precedence order)
  2. planning/revision-notes-2026-10-14.md    (scope source of truth)
  3. planning/PLAN.md                         (work order and STOP points)
  4. planning/DECISIONS.md                    (open decisions; you never rule)
  5. planning/VERIFY.md, MEDIA-CREDITS.md, VOICE-PASS.md, HANDOFF.md
Then read README.md, curriculum/, source/, and docs/index.html.

Two lines in this prompt are LOCKED (my words; keep them exactly):

  S1 title slide, these line breaks on wide screens:
    Four Directions, one River. When you can communicate in a
    respectful way, where both an Elder and a Child can understand;
    this is the surest sign that you are able to share knowledge.

  S2 title:
    To seek understanding is less about being told

How each one fits with the revision notes (casing, punctuation, whether the
old Elder/Child blockquote stays, what happens to "Four Questions, One
River") is open in DECISIONS D8, D9, D1, and D2.

=== PHASE 0: ORIENT (read only until step 5) ===
1. Create branch dev/revisions-2026-10 and tell me the git command you used,
   what it does, and what output to expect.
2. Run the build (python source/build.py; try python, py, python3) and
   compare its output to the committed docs/index.html. Report whether it
   matches. If not, STOP and show me what differs.
3. Slide inventory: a table of S-number, current title, and where each
   slide lives in source/template.html. Flag any place where the live site
   order differs from the S1 to S23 numbering in the revision notes.
4. Read I:\community-connector (READ ONLY; never edit that repo). Report its
   graph engine's size, dependencies, and license, for D15.
5. First commit: add the planning/ folder and CLAUDE.md as they are, plus a
   stable data-slide-id on every slide (e.g. s04-cloud-tool). Rebuild.
   No visible change to the page.
6. Decision walkthrough. Take me through only the decisions Phase 1 and 2
   need, ONE AT A TIME, in this order: D8, D9, D1, D2, D3, D12, D10. For
   each: the plain name and ID, a short narrative of what it changes on
   the page, concrete implications of each option, and the default ruling
   I can accept or change. Wait for my answer before the next one. Record
   my rulings in DECISIONS.md. Leave D4 to D7, D11, and D13 to D15 for
   when their phase comes up.

=== PHASE 1 AND ONWARD ===
Follow planning/PLAN.md from Phase 1, honoring every STOP. Additional
expectations:

Layout and blocking (Phase 1), all slides:
- The S1 lines hold my breaks at 1920x1080 and 1366x768 and read as an even
  stanza; on narrow screens (390px) they reflow with text-wrap: balance, no
  stranded single words.
- Headings use text-wrap: balance; body text uses text-wrap: pretty; body
  lines about 45 to 75 characters; consistent vertical rhythm and safe
  margins; no clipping at 1366x768 or on a projector; a scrim wherever text
  sits on a photo and fails contrast.
- Sibling cards render equal heights (grid, align-items: stretch) and their
  copy is balanced to the word targets in the notes.
- Report a before/after list by S-number and plain title.

Draft language: place DRAFT strings from the notes where the plan says to,
list every one in VOICE-PASS.md, and never present a DRAFT as final.

Facts and media: every factual claim gets a VERIFY.md row before it ships;
every photo, video, dataset, and library gets a MEDIA-CREDITS.md row with
its license confirmed on the item's own page.

K-12 interactivity: the slides themselves are the K-12 interactive (cloud
tool, gauges, reciprocal inquiry card, nested zoom, species cards,
constellation). Every interactive piece needs: keyboard and touch use,
screen-reader labels, prefers-reduced-motion, smooth performance on a
school Chromebook (test at 4x CPU throttle), and a low-tech classroom
version described in the slide notes. Separate student pages wait on D13.

Concept briefs (Phase 7): for S9, S12, S15, S16, and S17, write a one-page
brief each in planning/briefs/, with a sketch of the interaction, the
learning goal, and open questions for me. Do not build them.

At every STOP: show what changed (S-number and plain title), what is
waiting on me (decision ID with its plain name), and the next step.

At the end of the session: update PLAN.md checkboxes, add a HANDOFF.md
entry, commit, and give me the git commands to review the branch and push
it, explaining what each does and what output to expect. Do not push.
```

## Resume (later sessions)

```
Resume work on I:\climate-curriculum. Read CLAUDE.md, the top entry of
planning/HANDOFF.md, and planning/PLAN.md. Check DECISIONS.md for rulings I
have made since the last session. Tell me in a few lines where things stand
and what is next, then continue from the next unchecked item in PLAN.md.
A STOP is a decision only I can make (D26b); between STOPs, use your
judgment and keep going. Bring me newly needed decisions with a default
ruling, batched when they are linked. Commit as you go on the branch; push
or merge only when I ask in the session. End by updating PLAN.md and
HANDOFF.md.
```

## Next session: print design and the event handout (prepared 10/20/2026)

Model: Opus 5.5 at high effort (the main loop does the design thinking;
workers are pre-assigned below). Paste:

```
/pickup continue. Branch dev/print-design-2026-10. This session is graphic
design and page layout, with a little frontend: read the top HANDOFF.md entry
and the "Next session" section of planning/LAUNCH-PROMPT.md, then
private/handout/BRIEF.md (local only). Ask me the brief's section 2 questions
in one message with your defaults, then start designing while I answer.
```

### Where things stand

- Live: main at 0d037c3 serves the polished workshop page and two print PDFs
  (docs/downloads/). The event is Friday 10/23/2026 and Saturday 10/24 in
  Toppenish; ATNI's 30-minute slot shows the page and the Dynamic Drought
  Module (D21). Anything that must be printed needs Patrick's approval by
  the evening of 10/21 to leave print time.
- The interior design of the PDFs works (33 and 14 pages, tagged, bookmarked,
  no spill pages). What they lack is imagery and a stronger visual voice;
  that, and a one-page handout, are this session's work.

### Outcomes (you choose the path)

1. A one-page, full-color event handout: abstract of the online page, cited
   papers, QR code to the live page, acknowledgements with the Yakama Nation
   first. Content, draft copy, names to confirm, image notes, and the open
   questions are in private/handout/BRIEF.md. The background is IMG_4251
   (Columbia Gorge at dusk), already stripped of GPS EXIF in
   private/print-assets/gorge-dusk-4251.jpg.
2. Photographic covers and openers for both print guides, using the prepared
   images in private/print-assets/ (suggested pairings in BRIEF.md section 5).
   A photo goes public only as a stripped copy, with a MEDIA-CREDITS row and
   Patrick's confirmed credit line.
3. Small frontend: link the two PDFs (and the handout once approved) from S22
   (s22-classroom), whose notes still carry the download placeholder; any
   further interface polish the design pass suggests. Use cc-slide-change
   for slide edits.
4. DesignCraft and VectorCraft available to the session if they can be
   (see "Tools" below); they are for element revisions (SVG map, marks,
   icons, layout checks), not a requirement for shipping.

Design latitude: you are the designer. Work inside the ATNI Climate system
(League Spartan, Lexend Deca, Cascadia Code; ATNI Red #E13D33 on near-black
#010B13; water blues #5E97C9 and #9CC7F0) and make strong choices within it:
scale, crop, duotone or gradient-mapped photos, scrims, rhythm, the basin map
as a recurring mark. CLAUDE.md asks before new fonts or palettes, so present
anything beyond the system (for example a gold sampled from IMG_4251) as
rendered side-by-side options, not as an abstract question. Prefer showing
Patrick two or three rendered directions over describing one.

### Code map (tools/print_pdf.py, 401 lines)

- `DOCS` (line 23): one entry per printed document (`kind`, `out`, `short`,
  `cover_title`). A handout can be a third `kind`, or its own small source.
- `blocks()` (62) and `inline()` (38): the Markdown subset these documents use
  (headings, pipe tables, flat lists, blockquotes, code-span placeholders).
- `assemble()` (128): cover, contents, openers (`.opener`, units and parts),
  lesson sections (`section.lsn`, `.draft` for Lesson 4.3, `.tight` refit),
  the Editor's Note exclusion, and contents markers (`.mk`, `@@Tnn@@`).
- `basin_svg()` (108) draws source/columbia_svg.json (keys W, H, land, lakes,
  tribs, mainstem, snake, salmon, pts, labels): the cover map and any mark.
- `css()` (227): the whole print design. `@page` margin boxes carry the
  footer and page number (Chrome 155 supports them); `@page :first` is the
  full-bleed cover.
- `build()` (348): pass 1 finds heading pages, refits lessons that spill
  (adds `.tight`), pass 2 fills contents numbers, then PyMuPDF writes
  bookmarks and metadata. Asserts: every heading found, no em dash, page
  count stable between passes. Prints "sparse pages" when a page holds
  little text and is not an opener.
- Render: Chrome headless with its own `--user-data-dir` (without it Chrome
  attaches to Patrick's open browser and prints nothing).
- Review: `python tools/contact_sheet.py <pdf> <out.png> --pages 1-8` or
  `--each --pages 3,26 --dpi 110` for single pages to read closely.
- Known limits: Chrome prints RGB only (no CMYK or PDF/X); content in a page
  margin is clipped (the Lesson 4.3 rule had to move inside the box);
  text extraction maps the footer middle dot to U+FFFD (it renders fine);
  one glyph on the lessons page 34 falls back to Segoe UI.

### Page code map (source/template.html; build with python source/build.py)

- `IMAGES` registry (line 852): every photo the page uses; all `credit:''`.
- `go()` (889): slide navigation; preloads the next slide's photo.
- S22 `.links` (line 815): where download links would go.
- Gates: `python source/build.py --check`, `python tools/check.py`, the probe
  (cc-release-check probe mode; baseline 10/20/2026 is in HANDOFF.md).

### Known checks for this work

- Print: `python tools/print_pdf.py` (and its asserts), contact sheets read
  by eye or by the print-visual-qa workflow, house style via tools/check.py
  on any new prose, a printed proof with two phones scanning the QR code from
  arm's length.
- Page: build --check or build plus diff, probe for touched slides only.

### Tools: VectorCraft and DesignCraft (researched 10/20/2026)

Both are native Windows apps from github.com/storytold (Rust, MIT or
Apache-2.0, pre-1.0, releases every few days), installed by MSI on 10/17/2026
under C:\Program Files\. Each CLI carries its own stdio MCP server
(`<tool>-cli.exe mcp`); no network, no keys.

- VectorCraft 0.12.0 (latest 0.13.1): registered 10/20/2026 at local scope
  (not in the repo): `vectorcraft-cli.exe mcp --automation-read-root
  I:\climate-curriculum --automation-write-root
  I:\climate-curriculum\private\craft`. Handshake verified (32 tools:
  draw_path, draw_shape, add_text, set_paint, pathfinder, transform,
  command_run, command_batch, open_file, export, render_preview, ...). The
  tools appear as `mcp__vectorcraft__*` in a new session. Confined: it reads
  the repo and writes only to private/craft (git-ignored; the folder must
  exist). Exports SVG and PDF, including PDF/X-1a, X-3, X-4, CMYK, spot
  colors, bleed and marks, so it can produce a print-shop file that Chrome
  cannot. `render_preview` returns a PNG of the artboard.
  CLI without MCP: `"C:\Program Files\VectorCraft\vectorcraft-cli.exe"
  convert in.svg out.pdf`, `info FILE`, `commands`.
- DesignCraft 0.8.0 (latest 0.10.0): NOT registered on purpose. 0.8.0 has no
  folder-confinement flags, so its MCP server could read and write anything
  the account can. Patrick: install the 0.10.0 MSI from
  https://github.com/storytold/designcraft/releases (check SHA256SUMS.txt),
  then in PowerShell 7:
  `claude mcp add -s local designcraft -- "C:\Program Files\DesignCraft\designcraft-cli.exe" mcp --automation-read-root "I:\climate-curriculum" --automation-write-root "I:\climate-curriculum\private\craft"`
  and restart Claude Code. Tools: new_document (presets, margins, bleed),
  place_image, set_story_text, render_page, export_png, execute
  (file.exportPdf with PDF/X-4 and PDF/A-2b, IDML, EPUB). No SVG export
  (use VectorCraft). Its PDF/X-4 is self-validated, not certified.
- Use them where they beat hand-written SVG/CSS: the basin mark as a clean
  vector, a print-shop PDF/X version of the handout with bleed, CMYK
  conversion. The Chrome pipeline stays the source of record unless a
  rendered comparison says otherwise.

### Subagent roster (definitions in .claude/agents/, committed)

| Work | Agent | Model, effort | Skills, MCP |
|---|---|---|---|
| Design direction, decisions with Patrick, integration | main session | Opus 5.5, high | frontend-design, design-critique as needed |
| Layout of the handout, covers, openers | print-designer | claude-opus-5-5, high | frontend-design, design-critique; inherits mcp__vectorcraft__* (and designcraft once registered) |
| Vector elements (basin mark, QR tile, rules, icons) | vector-artist | claude-opus-5-5, high | canvas-design; VectorCraft MCP |
| Critique of renders (type, image, content lenses) | visual-critic | claude-opus-5-5, high; read-only | design-critique, accessibility-review |
| Mechanical preflight (fonts, ppi, EXIF, links) | print-preflight | sonnet, medium; read-only | PyMuPDF, Pillow |
| Copy, citations, acknowledgements wording | copy-steward | sonnet, high | pf-voice, ux-copy |
| S22 download links, page polish, gates | slide-engineer | sonnet, high | cc-slide-change, cc-release-check, playwright-cli |
| Citation and claim proof | claim-verifier (user level) | sonnet | read-only |
| Pedagogy or cultural framing questions | curriculum-specialist (user level) | inherits | curriculum-design-check |
| QR library check before install | security-vulnerability-checker (user level) | inherits | checking-cves |
| Push, merge, Pages check (only when asked) | gh-specialist (user level) | inherits | gh-align |

### Saved workflows (.claude/workflows/)

- `design-directions`: args `{piece, brief, outDir, directions?}`. Three
  print-designers draft photo-forward, typographic, and map-mark directions
  in parallel in private/craft/directions/, two visual-critics score each,
  and a final pass recommends one with grafts. About 10 agents. Use it at
  the start of the handout and again for the cover and opener system.
- `print-visual-qa`: args `{pdf, pages?, group?, outDir?}`. Renders pages,
  runs type, image, and content critics per group of six pages plus a
  preflight, and returns one ranked fix list. About 3 agents per six pages
  plus 3. Use it before showing Patrick a PDF and before printing.
- Workers write only under private/craft/ (git-ignored); the main session
  moves approved work into tracked files.

### Authority for the session

- Commit on dev/print-design-2026-10 as the work lands. Push the branch or
  merge to main only when Patrick asks in the session (main publishes the
  live site through GitHub Pages).
- Names, affiliations, credit lines, and acknowledgement wording come from
  Patrick; BRIEF.md drafts are not approval. No brief content goes into a
  tracked file until he approves it.
- Photos go public only as the stripped copies, with MEDIA-CREDITS rows.
- Installing segno (or any package) waits for Patrick's yes; the brief has
  the recommendation.
