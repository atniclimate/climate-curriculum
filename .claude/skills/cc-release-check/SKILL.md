---
name: cc-release-check
description: One release-assurance workflow for the workshop, in modes - build (build and prove no unintended change), static (house style, offline assets, network calls, slide ids), probe (viewports, accessibility, frame timing), offline (network-off folder test), route (what a chosen slide route shows that is not release-ready), sheet (timed facilitator run sheet with 15/30/60-minute variants), and voice-diff (changed learner-facing strings for Patrick). Use after source changes, before commits, before any event or merge to main, and when asked to build, check, probe, "is this ready to show", "make a run sheet", or "what text changed".
argument-hint: "[build|static|probe|offline|route|sheet|voice-diff|all] [slide ids or paths] [minutes]"
---

Modes run alone or together; produce one report. Read-only except `build`.
Run from the repo root unless a step says otherwise. Merging to main publishes
the live site (GitHub Pages serves main:/docs); never merge yourself.

build
- Markup-neutral change: `python source/build.py --check` (exit 0 = page
  unchanged). Content change: `python source/build.py` (or `py`), then
  `git diff --stat -- docs/index.html`; everything in the diff is intended.
  Never hand-edit docs/index.html.

static
- `python tools/check.py [paths]`. ERROR fails (exit 1). WARN is for a human:
  decide each, never mass-replace. Knowledge, Nations, Peoples, Beings are
  not checked (D20). Baseline 10/14/2026: 0 errors, 17 warnings. Prose you
  wrote also gets a pf-voice pass. In code, spell the em dash `chr(0x2014)`;
  the Write and Edit tools turn a typed escape into the literal character.

probe (run from the session scratchpad; `<repo>` is the clone's absolute path)
- `playwright-cli -s=probe open`, then
  `playwright-cli -s=probe --raw run-code --filename <repo>/tools/probe.js > probe-out.txt`,
  then `playwright-cli -s=probe close`, then
  `python <repo>/tools/probe-summary.py probe-out.txt`. If file: is refused,
  serve docs/ on 127.0.0.1 with `python -I -m http.server` and point the
  probe URL there for that run.
- Read: slideScroll/innerScroll (clipping; S10 stop card scrolls by design;
  at 390 only innerScroll counts), hScroll (always a defect), lineBreaks (the
  S1 stanza rule), tapTargets (under 44 breaks the house rule; FAIL-2.5.8 is
  under the WCAG 2.2 AA 24px floor), unequal (sibling heights), under12px,
  unnamedButtons, imgNoAlt, h1Count, PERF (relative; headless is not a
  Chromebook). Word balance is counted by hand.
- Baseline 10/14/2026: h1Count 0; part-progress segments 4px tall at 390;
  S4 sliders 20px tall; S16 picks 40x38; S20 nodes about 30px; unequal .carry
  on S6, S13, S18, .sort on S16, .webwrap on S20; no horizontal scroll. Full
  output is local: library/_synthesis/2026-10-14-team/probe-baseline-2026-10-14.json.

offline
- Copy docs/ elsewhere, disable the network, open index.html, step every
  slide: fonts, images, map load. docs/ (index.html plus img/ and fonts/) is
  the offline package, not index.html alone. Note every outbound link a slide
  depends on and its printed fallback.

route (for a real event or slot; route slides only)
- Route = the slides Patrick names. With none named, propose a core route of
  10 to 12 slides, marking the rest OPTIONAL DEMO, TEACHER HANDOFF, APPENDIX;
  Patrick confirms. The 23 slides list 30.5 minutes before interaction, so a
  30-minute slot needs cuts. A 20 to 45 minute module never fits whole; a
  route may hold a 3 to 5 minute excerpt.
- List, per route slide: visible facts without a CHECKED VERIFY row (and the
  known corrections in planning/research/2026-10-14-references.md section 0);
  media without a MEDIA-CREDITS row (all 15 photos uncredited 10/14/2026);
  DRAFT strings and bracketed placeholders; probe and offline findings;
  learner input stored on a shared device (S23 uses localStorage); any role
  that has a learner speak as a Nation, council, Elder, or knowledge holder;
  Tribe-specific content without permission. For each: fix, replace, hide
  from the route, or accept with Patrick's say.

sheet
- Per slide: minute marks (data-min plus 2 to 4 minutes per "Ask the room",
  1 to 2 per transition), purpose, the one thing that must land, the likely
  misconception, the hand twin, and a cut line. Variants for 15, 30, and 60
  minutes; a printed fallback list; a projector-only plan. Name three
  observable teacher outcomes and the closing check that shows them (a
  handoff card: what I will teach next; the place and public data I start
  with; whom I contact before localizing; my no-internet version; one open
  question).

voice-diff
- Changed learner-facing strings only, by S-number and plain title, old and
  new with word counts. Propose; only Patrick marks LOCKED (VOICE-PASS.md).

Report by S-number and plain title; compare with the baseline; say what is
blocked on Patrick (D-number and plain name).
