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
