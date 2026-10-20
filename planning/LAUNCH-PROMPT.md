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

## Next session: print design and the event handout (prepared 10/20/2026, reviewed the same day)

Model: Opus 5.5 at high effort. The main loop is the art director; workers
are pre-assigned below. Paste:

```
/pickup continue. Branch dev/print-design-2026-10. This session is graphic
design and page layout, with a little frontend: read the "Next session"
section of planning/LAUNCH-PROMPT.md, then private/handout/BRIEF.md (local
only). Ask me the brief's section 2 questions in one message with your
defaults, then start designing while I answer.
```

### The job

The event is Friday 10/23 and Saturday 10/24/2026 in Toppenish; ATNI's
30-minute slot shows the live page and the Dynamic Drought Module (D21).
The two PDFs in docs/downloads/ (33 and 14 pages, tagged, bookmarked) are
sound inside but have no photography and a quiet visual voice. Make, in
this order:

1. A one-page, full-color event handout (content, print specs, images, and
   open questions: private/handout/BRIEF.md).
2. Photographic covers and openers for both PDFs (photos and per-photo
   notes: BRIEF.md section 5).
3. S22 (s22-classroom): link the PDFs, and the handout once approved; its
   notes still carry the download placeholder. Use cc-slide-change.

You are the designer. Work inside the ATNI Climate system (League Spartan,
Lexend Deca, Cascadia Code; ATNI Red #E13D33 on near-black #010B13; water
blues #5E97C9 and #9CC7F0) and make strong choices: scale, crop, duotone or
gradient-mapped photos, scrims, rhythm, the basin map as a recurring mark.
Anything outside the system (a gold sampled from the gorge photo, say) goes
to Patrick as a rendered option beside a version without it.

### Timing, choosing, done

- Patrick chooses from pictures: send `compare.png` from the
  design-directions workflow (directions labeled A, B, C) with your pick
  and grafts; he answers with a letter and notes. Aim to show handout
  directions within the first two hours.
- Patrick approves names, wording, and the final proof by the evening of
  10/21; printing is 10/22.
- Handout done: source tracked in the repo with only approved names; a
  printer's file in the form his BRIEF answer asks for; the PDF in
  docs/downloads/ (after approval); a printed proof scanned by two phones
  at arm's length; MEDIA-CREDITS rows for every published photo; VOICE-PASS
  rows for DRAFT strings; VERIFY rows for claims in the abstract;
  tools/check.py clean on new prose.
- Covers done: `python tools/print_pdf.py` passes its asserts with no new
  sparse pages; print-visual-qa shows no blockers on the changed pages.
- S22 done: build --check or build plus diff, static mode, probe for s22.
  Branch work goes live only when Patrick merges to main (question 6 in
  the brief).

### Code map (tools/print_pdf.py, 401 lines)

- `DOCS` (line 23): one entry per printed document (`kind`, `out`, `short`,
  `cover_title`). `OUT` (line 18) is fixed to docs/downloads/, which is the
  published copy: drafts render from a copy with OUT under private/craft/,
  or add an `--out` flag first (small, worth it before parallel cover work).
- `blocks()` (62) and `inline()` (38): the Markdown subset these documents use.
- `assemble()` (128): cover, contents, openers (`.opener`, units and parts),
  lesson sections (`section.lsn`, `.draft` for Lesson 4.3, `.tight` refit),
  the Editor's Note exclusion, contents markers (`.mk`, `@@Tnn@@`).
- `basin_svg()` (108) draws source/columbia_svg.json (W, H, land, lakes,
  tribs, mainstem, snake, salmon; the file also holds states, ctx, routeA,
  routeB, pts, labels, rivers, fa, fb).
- `css()` (227): the whole print design. `@page` margin boxes carry footer
  and page number (Chrome 155); `@page :first` is the full-bleed cover.
- `build()` (348): pass 1 finds heading pages and refits spilling lessons,
  pass 2 fills contents numbers, then PyMuPDF writes bookmarks and metadata.
  Asserts: every heading found, no em dash, stable page count. Prints
  "sparse pages" for thin non-opener pages.
- Render: Chrome headless with a temporary `--user-data-dir` (without one,
  Chrome attaches to Patrick's open browser and prints nothing).
- Review: `python tools/contact_sheet.py <pdf> <out.png> --pages 1-8`, or
  `<pdf> <dir> --each --pages 3,26 --dpi 110` for single pages.
- Limits: Chrome prints RGB only (no CMYK or PDF/X); content in a page
  margin is clipped; text extraction shows the footer middle dot as U+FFFD
  (it renders fine); one glyph on lessons page 34 falls back to Segoe UI.

Page (source/template.html; `python source/build.py`): `IMAGES` registry
line 852 (15 photos, every `credit:''`); `go()` line 889; S22 `.links`
line 815. Probe baseline for 10/20/2026 is in the HANDOFF.md entry of that
date.

### QR code (no new package)

DesignCraft's CLI makes a vector QR now (tested 10/20/2026: 33 x 33
modules, one vector path). In the Bash tool:

```
mkdir -p private/craft/qr
"C:/Program Files/DesignCraft/designcraft-cli.exe" run --cmd 'file.new={}' --cmd 'object.qrCode={"content":"https://atniclimate.github.io/climate-curriculum/","rect":[0,0,144,144]}' --export private/craft/qr/qr-page.pdf
"C:/Program Files/VectorCraft/vectorcraft-cli.exe" convert private/craft/qr/qr-page.pdf private/craft/qr/qr-page.svg
```

The SVG is a full Letter page with the code in the top-left 144 pt; set its
width, height, and viewBox to 144 (`0 0 144 144`) and save as private/craft/qr/qr.svg (the
design-directions workflow looks there). It carries a 2-module margin, so
place it on a light tile that brings the quiet zone to 4 modules. No
decoder is installed: scan the screen render with a phone before the
printed proof. segno stays the fallback if Patrick prefers it (needs his
yes and a checking-cves pass).

### VectorCraft and DesignCraft

Native Windows apps (github.com/storytold; Rust; MIT or Apache-2.0; pre-1.0,
fast releases), installed 10/17/2026 under C:\Program Files\.

- VectorCraft 0.12.0: MCP registered at local scope, confirmed Connected on
  10/20/2026 (`claude mcp get vectorcraft` in PowerShell 7). Reads the repo,
  writes only to private/craft/. Tools appear as `mcp__vectorcraft__*`
  (draw_path, draw_shape, add_text, pathfinder, command_run, export,
  render_preview, ...). Exports SVG and PDF including PDF/X-1a, X-3, X-4,
  CMYK, spot colors, bleed and marks: the route to a print-shop file that
  Chrome cannot make. CLI: `vectorcraft-cli.exe convert IN OUT`, `info`,
  `commands`.
- DesignCraft 0.8.0: CLI usable for one-shot jobs (`run`, `script`,
  `describe COMMAND`); MCP deliberately not registered, because 0.8.0 has
  no folder confinement. To enable it, Patrick installs the 0.10.0 MSI
  (check SHA256SUMS.txt), then in PowerShell 7:
  `claude mcp add -s local designcraft -- "C:\Program Files\DesignCraft\designcraft-cli.exe" mcp --automation-read-root "I:\climate-curriculum" --automation-write-root "I:\climate-curriculum\private\craft"`
  and restarts Claude Code. Its PDF/X-4 is self-validated, not certified;
  no SVG export.
- The Chrome pipeline stays the source of record unless a rendered
  comparison says otherwise.

### Subagent roster (.claude/agents/, committed)

| Work | Agent | Model, effort | Skills, tools |
|---|---|---|---|
| Direction, decisions with Patrick, integration | main session | Opus 5.5, high | frontend-design, design-critique as needed |
| Layout, covers, openers, photo treatment | print-designer | claude-opus-5-5, high | frontend-design, design-critique; all tools incl. VectorCraft MCP |
| Vector elements, basin mark, QR tile | vector-artist | claude-opus-5-5, high | canvas-design; VectorCraft MCP |
| Critique of renders (type, image, content lenses) | visual-critic | claude-opus-5-5, high; writes renders only | design-critique, accessibility-review |
| Mechanical preflight (fonts, ppi, EXIF, links) | print-preflight | sonnet, medium; read-only | PyMuPDF, Pillow |
| Copy, citations, acknowledgement wording | copy-steward | claude-opus-5-5, high | pf-voice, ux-copy |
| S22 links, page polish, gates | slide-engineer | sonnet, high | cc-slide-change, cc-release-check, playwright-cli |
| Citation and claim proof | claim-verifier (user level) | sonnet | read-only |
| Pedagogy or cultural framing | curriculum-specialist (user level) | inherits | curriculum-design-check |
| Package check, only if one is installed | security-vulnerability-checker (user level) | opus | checking-cves |
| Push, merge, Pages check, only when asked | gh-specialist (user level) | inherits | gh-align |

Plugin skills named in `skills:` (for example design:design-critique) are
not documented to preload; agents can still call them with the Skill tool.

### Saved workflows (.claude/workflows/; parse-checked, not yet run)

- `design-directions`: args `{piece, brief, outDir, directions?}`. One
  print-designer per direction (default photo-forward, typographic,
  map-mark; pass your own angles) drafts in its own folder under outDir,
  two visual-critics score each, then a recommendation with grafts and a
  content check, plus `compare.png` for Patrick. About 11 agents. Make the
  QR first so drafts use the real tile.
- `print-visual-qa`: args `{pdf, pages?, group?, outDir?}`. Renders pages,
  runs type, image, and content critics per six pages plus a preflight, and
  returns one ranked fix list. A full 33-page pass is about 21 agents; pass
  `pages` for what changed.
- Workers write only under private/craft/ (git-ignored); the main session
  moves approved work into tracked files.

### Authority

- Commit on dev/print-design-2026-10 as work lands. Push or merge to main
  only when Patrick asks in the session (main is the live site).
- Names, affiliations, credit lines, and acknowledgement wording come from
  Patrick; BRIEF.md drafts are not approval. Nothing from the brief enters
  a tracked file until he approves it.
- Photos go public only as the stripped copies in private/print-assets/,
  with MEDIA-CREDITS rows and Patrick's credit line.
- No invented cultural content: no Tribal-language greeting, no named
  departments or places for a Nation unless Patrick supplies them.
