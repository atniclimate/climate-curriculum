# CLAUDE.md

Working rules for Claude Code sessions in this repo. Read this first, every session.

## What this is

Columbia River Climate Change Teachers curriculum, ATNI Climate Program.
Authors: Patrick Freeland and Cayla Jones. Case material: Steve Robinson,
"Climate Change and the Tribes: Columbia River Edition" (draft).
Live workshop: https://atniclimate.github.io/climate-curriculum/ (served from docs/).

## Build rule (most important)

- source/template.html (and any source/ modules) is the editable source.
- docs/index.html is a BUILD OUTPUT. Never hand-edit it.
- Rebuild after every source change: `python source/build.py`
  (on Windows try `python`, then `py`, then `python3`).
- The built page must stay a single self-contained file that runs offline
  when someone downloads docs/ and opens index.html.

## Where things are

- curriculum/  lesson plans and syllabi (Markdown, Patrick edits these)
- docs/        published workshop; docs/img/ photos, docs/fonts/ subset fonts
- source/      template, Columbia map JSON, build script
- planning/    PLAN (work order), DECISIONS (Patrick rules), VERIFY (fact
               checks), MEDIA-CREDITS (licenses), VOICE-PASS (draft strings
               for Patrick), HANDOFF (session log), revision-notes-2026-10-14
               (scope source of truth), LAUNCH-PROMPT (how sessions start),
               research/ (public-source research reports)
- tools/       check.py (static gate), probe.js + probe-summary.py (layout
               probe via playwright-cli), extract.py (document text for
               library intake); build.py --check proves no change
- .claude/     project skills: cc-release-check (build, static, probe,
               offline, route, run sheet, voice diff), cc-slide-change
- library/     LOCAL ONLY, git-ignored. Collected sources from Patrick's
               archive and Drive; start at library/README.md. Never copy
               library text into a committed file without Patrick's say.
               Tribe-specific material remains that Nation's.
- private/     LOCAL ONLY, git-ignored. Tribe-specific drafts and event
               material awaiting permission.

## Every session

- Start: read this file, planning/HANDOFF.md (top entry), and planning/PLAN.md.
- End: update PLAN.md checkboxes and add a HANDOFF.md entry, then commit them.
- Photo paths and credits: the IMAGES registry near the top of the page script.

## Precedence when instructions conflict

1. Patrick's direct messages in the current session
2. Text marked LOCKED (launch prompt, revision notes Section 2)
3. Rulings recorded in planning/DECISIONS.md
4. DRAFT text in the revision notes (a starting point for Patrick's voice pass)

If two sources conflict and neither ranks higher, ask. Do not pick silently.

## Voice and house style

- Never write the em dash (U+2014). Use semicolons, commas, colons, periods.
- Capitalize: Indigenous, Tribal, Tribes, Nations, Peoples, Knowledge, Elder,
  Beings, Treaty, First Foods. Keep "Trust" capitalized in the Part Four line.
- Oxford comma. Dates MM/DD/YYYY.
- Never call Tribal Nations or Tribal people "stakeholders."
- Plants, animals, and waters are relatives, not resources.
- "Journey" is intentional for salmon. Otherwise avoid AI filler diction
  (delve, tapestry, unlock, empower, and similar).
- Plain words first, readable for upper elementary through adult; technical
  terms introduced as actions or images.
- Sibling cards on one slide carry roughly equal word counts.
- Scale language: Frog's Eye, Bird's Eye, Moon's Eye.

## Design

ATNI Climate design system: League Spartan, Lexend Deca, Cascadia Code;
ATNI Red on black; Patrick's Hall-mode photo backgrounds; no top-left bracket.
No new fonts or palettes without asking.

## Engineering rules

- Vanilla HTML, CSS, JS. No CDNs. Any third-party library is vendored into
  the repo, license checked and recorded in planning/MEDIA-CREDITS.md, and
  only after Patrick approves (see DECISIONS).
- Target hardware: school Chromebooks. Test animations with DevTools CPU
  throttling at 4x; keep an SVG or static fallback for anything heavy.
- Accessibility: WCAG 2.2 AA, full keyboard use, visible focus, screen-reader
  labels, prefers-reduced-motion respected, tap targets at least 44px.
- Check layouts at 1920x1080, 1366x768, and 390px wide.
- Student input stays in the browser (localStorage in try/catch); the page
  works without it. No analytics, no network calls for student data.
- Every slide carries a stable data-slide-id (e.g. s04-cloud-tool) so
  references survive reordering.

## Content guardrails

- Do not fill bracketed placeholders only ATNI staff or a Tribe can supply.
- Cultural content and Tribe-specific material require that Nation's
  confirmation; mark it, do not invent it.
- Any factual claim, threshold, date, or statistic goes in planning/VERIFY.md
  with its source before it ships.
- Any photo, video, or library goes in planning/MEDIA-CREDITS.md with license.

## Git

- Work on a feature branch. Do not push; Patrick reviews and pushes.
- Plain descriptive commit messages. No Claude co-author lines, no
  "Generated with" lines, no AI attribution anywhere.
- One feature or slide per commit where practical.
- When giving Patrick git or PowerShell commands, explain what each does and
  what output to expect.

## Presenter keys (do not break)

Arrow keys or Space: move slides. N: speaker notes. T: clock. H: highlight pass.
