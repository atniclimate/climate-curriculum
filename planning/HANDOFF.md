# Session Handoff

The last thing each Claude Code session does is update this file, so the next
session (or Patrick) can pick up without rereading everything. Newest entry on
top. Keep each entry short.

## Template

### MM/DD/YYYY, branch: <branch name>
- Done: what changed, by slide (S-number and title), with commit hashes
- Waiting on Patrick: decisions (D-number and plain name), voice-pass items, reviews
- Next up: the next unchecked item in PLAN.md
- Watch out: anything fragile, half-finished, or surprising

---

### 10/20/2026 (afternoon), branch: dev/print-design-2026-10 (from main 0d037c3)
- Next action: start the print-design session with the paste block in
  planning/LAUNCH-PROMPT.md, "Next session: print design and the event
  handout" (Opus 5.5, high). That section holds the job, deadline,
  definition of done, code map, QR route, roster, and workflows.
- Released: Patrick merged dev/workshop-polish-2026-10 into main (0d037c3);
  GitHub Pages built it at 17:36 UTC 10/20/2026 (success); the live page and
  both PDFs answered 200. dev/workshop-polish-2026-10 pushed (4ab5e83);
  dev/revisions-2026-10 fast-forwarded on origin to 66dbaa1.
- Prepared (commit 0956718, then a same-day review pass, uncommitted at
  review time): six agents in .claude/agents/, two workflows in
  .claude/workflows/ (parse-checked, not yet run), tools/contact_sheet.py
  (page ranges now validated), the LAUNCH-PROMPT next-session section, and
  a relaxed Resume block. The review fixed parallel designers overwriting
  the published PDFs, a CLAUDE.md section the vector agent cited that does
  not exist, and a QR plan that waited on a package install (DesignCraft's
  CLI makes the code; tested).
- Local only (git-ignored private/): handout/BRIEF.md (content, draft copy,
  citations, acknowledgement candidates, image notes, eight questions);
  print-assets/ (six photos, EXIF and GPS removed by prep_images.py; the
  OneDrive originals carry GPS and are never published); craft/ (worker and
  VectorCraft write root).
- Checks: no page or PDF source changed after the merge; build and PDF
  evidence from the morning entry still holds.
- Fixed at close: prep_images.py now converts the iPhone photos' Display P3
  profiles to sRGB (re-run; copies verified EXIF-free).

### 10/20/2026, branch: dev/workshop-polish-2026-10 (from dev/revisions-2026-10; no TCU commits)
- Done: D21, D22 printing note, D25 rulings recorded (e4f178d). Page polish
  (21dc2e0): probe now clean apart from by-design .sort/.webwrap columns, S4
  control panel scroll with notes open at 1366, phone progress segments 27px
  wide (above 24px). D25 slide fixes S4 notes, S5, S9, S10 (Kettle Falls,
  AUG table, Salmon River), S16 (Nez Perce, Tutuilla, Pushpum), S20 (0f1b67b).
  Copy-edit plus D25 corrections in both curriculum documents (f7dfef8).
  tools/print_pdf.py (a1b73fd) and docs/downloads PDFs: lessons 33 pages,
  guiding document 14 pages, tagged, bookmarked (484b8c4).
- Evidence: the source re-check report and copy-edit logs were session
  scratch (not kept); VERIFY.md rows carry the sources. build --check passes;
  tools/check.py 0 errors.
- Waiting on Patrick: merge to main if the polish and PDFs should be live for
  10/23 (merging also brings the dev/revisions-2026-10 commits); S22 links to
  the PDFs; voice pass VP1 to VP8; Colville review of the Kettle Falls line;
  Yakama Nation confirmation of the Pushpum wording; NESC 215 title wording;
  copy-edit flags (guiding doc Four Questions note contradiction, Language
  Guide missing Knowledge and Beings, OCAP framing, "Patrick A. Freeland").
- Watch out: an untracked zip appeared in curriculum/ ("Climate Change & The
  Tribes Curriculum  062326.zip"), not committed. vectorcraft/designcraft
  were not reachable from this session (no MCP tools, not on PATH).
  Lesson 4.3 case summary still says "proposes" inside "from the draft".
  The TCU branch (dev/tcu-templates-2026-10) is separate and untouched.

### 10/15/2026, branch: dev/revisions-2026-10
- Done (planning only; no slide, source, docs, or curriculum change; build
  check passed before starting, and no commit touched source/):
  - planning/modules/SEEDS.md: 68 seeds (4 Parts, 14 lessons, 10 CCIC weeks,
    8 CCIC assignments, 4 TCR modules, 5 TCR signature assessments, 23
    slides) mapped to 12 module clusters (6784076); corrections from the
    briefs (7daf5dd), including removal of a phrase that came from the
    private synthesis.
  - planning/modules/briefs/: 12 concept briefs by curriculum-specialist
    agents in three waves of four (9c8d64f, 835c6a1, 0e45f0b). Checkpoint
    fixes made by the main session: brief G named a Nation and a
    culturally significant place outside the confirmation marks; brief H
    quoted the private synthesis; brief I described Nation-named project
    cards and the held case outside the marks. All fixed in place.
  - Module author line on every brief, per Patrick's direction today:
    Patrick A. Freeland, with ATNI Climate (not owner); prior cited authors
    kept; licensing later (d350932, 0e45f0b).
  - planning/modules/PACKET-D27.md: D27 in four parts (form, location
    conflict, pilot, module skill), premise corrections to D22, proposed
    D28 to D34, and the curriculum findings that wait on D26e.
  - PLAN.md: Phase 8, all [hold] until D27; pilot first, STOP after its
    rehearsal.
- Waiting on Patrick, in order:
  1. D21 and the safety packet (unchanged from 10/14/2026).
  2. After the workshop: D27 (module architecture; D27b location conflict
     between D27's text, CLAUDE.md, and the private synthesis), then D28
     (does D22 reach every seed: TCR 201 Weeks 6 and 9, CCIC 200 Week 4,
     L4.1, L1.3, L3.1, L2.1), D29 (scenario generations), D30 (module
     storage), D31 (case-pack terms), D32 (license timing), D33 (station
     rule and courtesy notice), D34 (visible labels on s04, s10, s20).
  3. D22 premise: the proposed listener rename swaps the two jobs (packet).
- Next up: Patrick rules D27. On or after 10/25/2026, Phase 8a: author the
  pilot (Missing Is Not Zero) by hand, paper set first; STOP for rehearsal.
- Also next (separate session, Patrick's request): the TCU template
  build-out for 35 AIHEC TCUs and 5 NWIC extended sites. Launch prompt:
  planning/tcu/LAUNCH-TCU-TEMPLATES.md (new branch dev/tcu-templates-2026-10;
  shared core public in tcu/, every site-specific draft private in
  private/tcu/ until the TCU reviews it).
- Watch out:
  - Nothing is verified by the briefs unless they say "opened"; every
    proposed VERIFY row is OPEN and not yet in VERIFY.md.
  - The source Google Doc was edited 10/12/2026: after the repo's
    curriculum drafts (09/24 and 10/06/2026), not after the revision notes
    (10/14/2026) as the previous entry says. Drive was not fetched.
  - The repo has no LICENSE file.
  - Briefs propose public stations and gauges chosen by geography only;
    whether any sits on Tribal or trust land is not checked (D33).

### 10/14/2026, branch: dev/revisions-2026-10
- Done:
  - Repo set up as a clone of atniclimate/climate-curriculum; branch created.
  - Build fixed for Windows (UTF-8, LF) and given a --check mode; output is
    byte-identical to the live page. Commits 2484022, a2589b1.
  - Every slide has a stable id, s01-title to s23-close; DOM order matches the
    notes' S1 to S23 (dc2c2bb). No visible change to any slide this session.
  - .gitignore (library/, private/) and .gitattributes (LF) (6d4f71b).
  - tools/: check.py (static gate, baseline 0 errors / 17 warnings),
    probe.js + probe-summary.py (viewport probe, run once: h1Count 0, small
    tap targets, unequal cards on S6, S13, S16, S18, S20), extract.py.
  - Skills: cc-release-check and cc-slide-change (project, .claude/);
    curriculum-design-check and the curriculum-specialist agent (user level,
    ~/.claude/). Trimmed from seven project skills after the critic and Codex
    round 2 called the first set overbuilt.
  - A 36-agent team gathered sources and reviewed the environment; two Codex
    reviews (thought-partner mode). Public results in planning/research/
    (environment review; references with proposed VERIFY rows V15 onward and
    known corrections). Everything private is in library/ (git-ignored):
    152 extracts from H:\NEXUS and Drive, CATALOG.md, README.md (intake
    rules), _synthesis/ (curriculum lineage, place-based modules, all team
    reports, both Codex reviews, probe baseline).
  - Planning: D2 restated and D12 status noted; D16 to D27 added; PLAN gets a
    workshop readiness track on hold; VOICE-PASS edit path fixed.
- Waiting on Patrick, in order:
  1. D21 ATNI's role at the Yakama Tribal Teachers Workshop, Fri 10/23 and Sat
     10/24/2026 (run by the Indigenous Climate Project with Washington Wild and
     PEI; the agenda does not mention this site). This decides everything else
     this week.
  2. Safety packet: D22 Goldendale lesson role play (cultural, one at a time),
     D23 S23 reflections, D24 core route, D25 known factual corrections
     (includes the S11 Patrick Luke quote: re-cite to CRITFC and courtesy to
     the Yakama hosts and family).
  3. S1/S2 packet: D8, D9, D1, D2, D3 together.
  4. D26 process packet (packets and PROVISIONAL, STOP vs CHECKPOINT, "ships"
     = merged to main, commit .claude/, curriculum drafting, D12).
  5. After the workshop: D27 module architecture; D4 to D7, D10, D11, D13 to
     D20 as their phases come up.
- Next up: answer D21. If ATNI shows anything, run the workshop readiness
  track (cc-release-check route and sheet). If not, Phase 1 after 10/24.
- Watch out:
  - GitHub Pages serves main:/docs (checked). A merge to main is a release.
  - Your global ~/.claude/settings.json holds a third-party API key in plain
    text (env block). Consider moving or rotating it.
  - A reference agent put your work email in the User-Agent header of a
    script that queried the Wikimedia Commons API for image licenses
    (Wikimedia asks for a contact there). It should have used a generic
    contact; no other outbound use was found.
  - Raw private text from agents was deleted from the session scratchpad
    after the privacy audit (it had swept in non-teaching records).
  - library/ is not tiered or deduplicated yet; treat all of it as not
    quotable. Several NEXUS folders and Drive leads were not covered
    (library/README.md, Known gaps).
  - The source curriculum doc on Drive was edited 10/12, after the revision
    notes; the repo may be behind it.
