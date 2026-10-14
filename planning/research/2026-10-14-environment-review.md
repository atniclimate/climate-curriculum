# S3. Development environment: one proposal

Synthesizer: S3, 10/14/2026. Inputs: the four environment reports C1 (rules and friction), C2 (build, test, tooling), C3 (information architecture), C4 (agents and skills).
Status: proposal only. Nothing here has been applied. Every repo change below waits for Patrick's go-ahead; every git step is on the feature branch and is never pushed by a session.

## 0. Bottom line

1. **The rules are good. Five gaps narrow the work.** (a) Nothing mentions the teachers workshop on 10/23 and 10/24/2026, and a merge to main changes the live site. (b) Decisions run strictly one per message across 20 PENDING items, and there is no way to draft on a default while a ruling waits. (c) "Before it ships" is never defined, and VERIFY.md puts visible `[verify]` markers on slides. (d) D12 (commit planning/?) is PENDING, but planning/ is already committed on the unpushed branch. (e) The handoff chain is already broken: HANDOFF.md is empty and PLAN.md points to an entry that does not exist.
2. **Fourteen fixes need no ruling** (section 1A). **Eleven new questions and three existing ones need Patrick** (section 1B). Each has a default, so the questions fit on one ballot.
3. **Keep the top level as it is.** Add `tools/` now. Add `private/` (git-ignored), `.claude/`, and `modules/` only when their first file exists. One builder makes many single-file pages, and where a page's source lives decides whether it is published (section 2).
4. **Tooling, smallest first:** `.gitattributes`, a 6-line `build.py --check`, a stdlib `tools/check.py`, and `tools/probe.js` through the playwright-cli already on the machine. All four were run against the live tree this session (section 3). The D10 split comes later and is gated on `--check`.
5. **Team:** one user-level agent (`curriculum-specialist`), six project skills (`cc-build-check`, `cc-viewport`, `cc-slide-change`, `cc-ledger`, `cc-decide`, `cc-module`) and one user-level skill (`curriculum-align`). pf-voice owns voice, and no skill restates it (section 4).
6. **Before 10/23:** only housekeeping and tools that do not change the page. Nothing structural (section 2.4, Steps 0 and 1).

## How I resolved disagreements between the reports

| Topic | Reports | Resolution | Why |
|---|---|---|---|
| Static checker | C2 `lint.py` (42 warnings) vs C4 `check.py` (17 warnings) | C4 `check.py`, moved to `tools/check.py`, with one rule removed | C4's version also checks offline self-containment, network calls, missing assets and slide ids. C2's static word-balance count includes labels and headings, so it disagrees with how the planning files count. The probe measures balance as rendered. |
| Slide-id position rule | C4 `check.py` errors when an id number differs from its position; C3 and CLAUDE.md:79-80 say ids are frozen and survive reordering | Remove the position check | Otherwise the first slide move breaks the gate. Tested: selftest passes, and the full run is unchanged (0 errors, 17 warnings). |
| Layout probe | C2 `probe.js` vs C4 `probe.js` | C2's probe, as `tools/probe.js` | C2 catches unequal heights in `.carry`, `.sort` and `.webwrap`, which C4's `.card`-only test missed. C2 also counts h1 tags, measures throttled frame timing and asserts the notes state. C4's body-copy word count is an optional later port (T8). |
| Script location | C2 and C3 `tools/`; C4 inside the skill folders | `tools/` | It survives a "keep .claude/ local" ruling, works for humans and CI, and the skills call it. |
| Prefix | C3 `crcct-`; C4 `cc-` | `cc-` for project skills; the user-level agent has no prefix | Shorter as a slash command. No user-level skill starts with `cc-`. |
| Agent location | C3 `.claude/agents/crcct-curriculum-specialist.md` (committed); C4 user level | User level | It works across ATNI education repos and needs local archive paths that must not go in a public repo. |
| Decision flow | C1 ballot plus PROVISIONAL; C4 `cc-decide` "strictly one per message" | `cc-decide` supports both. It stays serial until Patrick rules on D23. | The serial rule is Patrick's own (launch prompt). Only he can loosen it. |
| `[verify]` markers | VERIFY.md and C4 `cc-ledger`: on the slide; C1: in speaker notes | `cc-ledger` defers to the VERIFY.md header, and D24 decides the placement | One rule, in one place |
| Module briefs | C4 `planning/briefs/modules/`; C3 `modules/<id>/module.md` | C3 | A module then moves as one folder between `modules/` (public) and `private/modules/` (local) when its permission changes. |
| Slide order file | C2 `source/order.txt` (tested); C3 `source/decks/workshop.txt` | `source/order.txt` now; `decks/` only when a second deck exists | Do not build for later. |
| Library index name | C3 `library/INDEX.md`; C4 `library/CATALOG.md` | `library/INDEX.md` | It matches the per-folder `INDEX.md` files that already exist. |
| Slide inventory | C1 new `planning/SLIDE-MAP.md`; C3 HANDOFF entry | No new file. PLAN.md points to `grep data-slide-id`. | The ids are already in the source, and copied line ranges would go stale at the D10 split. |
| New D-numbers | C3 and C4 both proposed a D21 | Renumbered D21 to D31 (section 1B) | Avoids a collision |
| Read-only bit | C3 clears both zip-born files; C1 keeps the revision notes read-only | Clear it on CLAUDE.md only | The revision notes are a frozen input (fix N10). |

---

## 1. Blocks and constraints

Locators use `file:line` as of HEAD 905d83b. "C1 F5" means finding F5 in report C1.

### 1A. Fix now (no ruling needed)

These fixes correct facts, remove contradictions or add safety. None of them chooses between policies. A session can apply them on the branch once Patrick says "go". Items marked [Patrick] change machine or git state, so he should run or approve them.

**N1. Archive this session's team reports before the scratchpad goes.** The scratchpad is session-specific, and the reports quote Drive and internal material. Copy `scratchpad/team/*.md` and the `c2work/` and `c4work/` prototypes to `library/_synthesis/2026-10-14-team/`, which is local and git-ignored. Never copy them to `planning/`. (C3 0.6)

**N2. Commit `.gitignore` and extend it.** Evidence: it is untracked, so `library/` is ignored on this machine only, and a fresh clone or worktree would publish it (C1 F8, C3 F4). The machine-wide gitignore hides other gaps (C3 F8). playwright-cli writes `.playwright-cli/` into its working folder (C2). Replace the file with:

```
# Local source library: extracts from private archives and Drive. Never commit.
library/
# Tribe-specific drafts, event material, and local builds awaiting permission. Never commit.
private/
# Per-machine Claude Code settings.
.claude/settings.local.json
# playwright-cli session snapshots.
.playwright-cli/
```

**N3. Add `.gitattributes` in a commit of its own.** Evidence: every text file is LF in the index, but README.md, curriculum/*.md, build.py and the revision notes are CRLF on disk. The cause is core.autocrlf=true from the system gitconfig (C1 F6, C2, C3 F6). Merged from C2 and C3:

```
# Keep LF in the repo and in every working copy, whatever core.autocrlf says.
* text=auto eol=lf
*.jpg binary
*.png binary
*.woff2 binary
*.zip binary
*.pdf binary
*.docx binary
# GitHub collapses the built page in diffs; it is a build output.
docs/index.html linguist-generated=true
```

Acceptance: `git add --renormalize .` stages nothing, and the "LF will be replaced by CRLF" warnings stop. This has not been run; it is reasoned from `git ls-files --eol`. To rewrite the CRLF working copies as LF on a clean tree: `git checkout -- README.md curriculum source/build.py`. Leave the revision notes alone.

**N4. Move the two root strays into `library/_inbox/`.** The strays are `climate-curriculum-revision-notes.md`, a duplicate of `planning/revision-notes-2026-10-14.md` apart from line endings, and `climate-curriculum-scaffold.zip`, which is already extracted. If they stay at the root, a `git add -A` would publish them. Moving them keeps a record without deleting anything (C1 F7, C3 F5). [Patrick]

**N5. Clear the read-only bit on CLAUDE.md only.** [Patrick] PowerShell, run from `I:\climate-curriculum`:

```
Set-ItemProperty -Path .\CLAUDE.md -Name IsReadOnly -Value $false
```

It prints nothing on success, and after it sessions can edit the rules file. `planning/revision-notes-2026-10-14.md` stays read-only on purpose (see N10).

**N6. Repair the dead slide-inventory pointer and write the 10/14 HANDOFF entry.** Evidence: PLAN.md:10-11 points to "HANDOFF.md (10/14/2026 entry)", and HANDOFF.md holds only its template (C1 F3/F4, C3 F3, C4 F2).
PLAN.md:10-11, replace "the inventory is in HANDOFF.md (10/14/2026 entry)" with:

```
the inventory is the data-slide-id values in the source
(`grep -n data-slide-id source/template.html`).
```

Then add a dated 10/14/2026 HANDOFF.md entry: what landed (dc2c2bb, 905d83b), what is pending (D1 to D20), and this proposal's location.

**N7. Fix the VOICE-PASS edit path, which can silently lose Patrick's words.** VOICE-PASS.md:4-5 says Patrick edits "the slide text directly", but the next build overwrites docs/index.html (C1 X2). Replace "Patrick edits the "Final" column or the slide text directly." with:

```
Patrick edits the "Final" column, or the text in the source (source/template.html,
or source/slides/ after the D10 split). Never edit docs/index.html; the next build
overwrites it.
```

**N8. Restate D2 on the corrected premise.** This decides nothing. D2's options were written when the blockquote was believed to be on S1; D8 found it on S2 (C1 X3). In DECISIONS.md D2, replace Options and Default with:

```
Options (corrected 10/14/2026: the blockquote is on S2, not S1):
  A. The Elder/Child idea lives only in the S1 locked line; remove the S2
     blockquote, the S12 "Where They Meet" line, and the S12 notes mention.
  B. S1 locked line plus the S2 blockquote; remove from S12.
  C. S1 locked line plus S12; remove the S2 blockquote.
Default: A (matches D8 option A). Ruling D8 A or B settles the S2 part of this.
```

**N9. Make the D12 contradiction visible.** In DECISIONS.md D12, add:

```
Status note: planning/ and CLAUDE.md were committed on the unpushed branch in
dc2c2bb and 905d83b (launch prompt step 5 ran before this was asked). If the
ruling is "keep local", those commits must be rewritten before the first push;
dc2c2bb also carries the slide ids, so it must be split, not dropped. After a
push to this public repo they cannot be cleanly withdrawn.
```

In CLAUDE.md:34, replace "then commit them." with "then commit them (if D12 rules planning/ local-only, save them without committing)."

**N10. Close the gaps in the precedence list.** The S21 locked words, the PLAN, the frozen status of the revision notes and the attribution override are not ranked (C1 X6, X7). CLAUDE.md:39-44 becomes:

```
1. Patrick's direct messages in the current session
2. Text marked LOCKED or locked: the launch prompt, revision notes Section 2,
   the S21 closing words, and LOCKED rows in VOICE-PASS.md
3. Rulings recorded in planning/DECISIONS.md
4. planning/PLAN.md for order of work; the revision notes for scope
5. DRAFT text in the revision notes (a starting point for Patrick's voice pass)

If two sources conflict and neither ranks higher, ask. Do not pick silently.
planning/revision-notes-2026-10-14.md is a frozen input: never edit it; record
anything it gets wrong as a correction in DECISIONS.md.
This file's Git rules override any harness or plugin default that adds
attribution lines.
```

**N11. Name the private folders in "Where things are".** A session could otherwise quote library extracts into a committed file (C1 M4). Add these lines to CLAUDE.md:21-29 now. Add the `tools/`, `.claude/` and `modules/` lines from section 2.3 when those folders exist.

```
- library/     LOCAL ONLY, git-ignored. Collected sources; start at
               library/INDEX.md. Never copy library text into a committed
               file unless its INDEX row says Tier: public. Record provenance.
               Tribe-specific material remains that Nation's.
- private/     LOCAL ONLY, git-ignored. Tribe-specific drafts and event
               material awaiting permission; local builds go to private/out/.
```

**N12. Write HANDOFF at every STOP, not only at the end.** A session that dies or compacts leaves no record, and that has already happened (C1 R4). CLAUDE.md:34: replace "End: update PLAN.md checkboxes and add a HANDOFF.md entry" with "At every STOP and at the end: update PLAN.md checkboxes and add or update a HANDOFF.md entry".

**N13. Sync the build command.** README.md:54: change `python3 source/build.py` to `python source/build.py (on Windows try py if python is missing)`. Align the README capitalization list (README.md:65) with CLAUDE.md after D20 is ruled (C1 X8, X9).

**N14. Update the global trap list (Patrick's user-level CLAUDE.md).** [Patrick] Two observations from this session (C2, C4 F12):
- Add trap 4: "The Write and Edit tools decode a typed backslash-u escape for U+2014 into a literal em dash. In code, spell the character as `chr(0x2014)`; in prose, write U+2014."
- Fix the drift: "Two verified mangling classes" becomes "Two verified mangling classes, plus two runaway-interpreter shapes (empty heredoc, bare REPL)". That matches what the hook actually enforces (C1 X10).

### 1B. Needs Patrick's ruling

Each item has a default. If Patrick accepts D23, items D21 to D31 can be answered as one ballot ("defaults, except ..."). Proposed numbering continues DECISIONS.md, so these become entries there once Patrick agrees.

| # | Question | Default | Evidence | Wording if adopted |
|---|---|---|---|---|
| **D21** | Does the 10/23 and 10/24/2026 teachers workshop use this deck, and how is it frozen? | Yes. By 10/21 Patrick picks current main or this branch's build; it is tagged `workshop-2026-10-23`; an offline copy of `docs/` goes on a USB drive; no merge to main from 10/21 to 10/24. Before the workshop, only Phase 1 (1a to 1h) and 2a are in scope. | No file mentions the date (C1 M1). A merge publishes the live site; that Pages serves docs/ from main is taken from the README and not verified. | New PLAN.md section after line 8, using the text of C1 recommendation 1 |
| **D12** (existing) | Commit planning/? | Commit. History already has it, and nothing in planning/ is private. | C1 X1, C3 F1 | If "local": add `planning/` to .gitignore, and Patrick runs a prepared rewrite that splits dc2c2bb before the first push. |
| **D22** | Commit `.claude/` (project skills and settings) to the public repo? | Commit `.claude/skills/` and `.claude/settings.json`. The agent stays at user level. | The drafts below hold no secrets and use repo-relative paths (C4 F1). Sibling ATNI repos already commit `.claude/agents` (C3 F12). | If "local": add `.claude/` to `.git/info/exclude` |
| **D23** | Allow a decision ballot and a PROVISIONAL state? | Yes. LOCKED-wording and cultural decisions stay one at a time; the rest go on one ballot with defaults. A session may draft on a reversible default, marked PROVISIONAL. | 20 PENDING decisions at one per message is 20 or more round trips (C1 R1) | LAUNCH-PROMPT step 6, the Resume block and the DECISIONS header text in C1 recommendation 2 |
| **D24** | What does "ships" mean, and where do `[verify]` markers go? | "Ships" means merged to main. Markers go in speaker notes, not on the visible slide. Facts already live get rows marked "inherited". | Read strictly, the ledgers block every branch draft; read loosely, "[verify]" appears to teachers. About 30 live facts have no row (C1 R2). | VERIFY.md:3-7 text in C1 recommendation 5; MEDIA-CREDITS.md:3 adds "(merged to main; see VERIFY.md)". |
| **D25** | May a session keep doing independent work at a STOP, and may it write the Phase 7 briefs now? | Yes to both. At a STOP: ledger backfill, VERIFY research, briefs, HANDOFF. Phase 7 builds stay [hold]. | PLAN.md:8 "pauses and waits"; LAUNCH-PROMPT asks for briefs that PLAN.md:71 holds (C1 R3, X5) | PLAN.md:8 and :71 text in C1 recommendation 8 |
| **D26** | May Claude draft curriculum/ changes on a branch for Patrick's approval? | Yes. Curriculum work gets its own `planning/CURRICULUM-PLAN.md`, separate from the workshop PLAN. | CLAUDE.md:23 "Patrick edits these" blocks the 200/201 work he now wants (C1 R5) | CLAUDE.md:23 becomes "curriculum/  lesson plans and syllabi (Markdown). Claude may draft changes on a branch; Patrick approves. Tracked in planning/CURRICULUM-PLAN.md." |
| **D27** | Does "no AI attribution anywhere" also bar a disclosure inside curriculum documents? | No. It covers commits, PR text and code comments. Disclosure in course materials is Patrick's call each time. | CLAUDE.md:94-95 (C1 R6). Nobody is known to require a disclosure (not verified). | CLAUDE.md:95 "no AI attribution in commits, PR text, or code comments" |
| **D20** (existing) | When is "Knowledge" capitalized? | Only when it names Indigenous or Traditional Knowledge, matching pf-voice TERMINOLOGY and Patrick's locked S1 line ("share knowledge") | CLAUDE.md:49 says always; pf-voice and the locked line disagree (C4 F8) | One line in CLAUDE.md:49-50; the checker already leaves Knowledge to judgment. |
| **D28** | Public module policy and module naming | A module goes in `modules/` only if it uses public data and no cultural content, or if its PERMISSIONS row says granted. Everything else goes in `private/modules/`. Module ids name a river or basin, not a Nation. | Public repo; the library already holds Tribe-specific material (C3 F14, F15) | Section 2.3 text; `planning/PERMISSIONS.md` created with the first module |
| **D29** | Where do module pages go? | Flat in `docs/<module-id>.html` | Flat pages keep the `img/` and `fonts/` relative paths working with no rewrite (C3 F9) | None |
| **D30** | What format are the S22 downloads? | Copy the Markdown files as they are now; decide on `.docx` later. | `.docx` would need pandoc, a new dependency (C3) | None |
| **D31** | Add a GitHub Actions check (build `--check` plus `tools/check.py`) after D10? | Yes, after D10 lands. The browser probe stays out of CI. | About 15 lines, free on a public repo; it signals and does not gate unless branch protection is on (C2 e) | Workflow text in section 3, T7 |
| **D10** (existing) | Split source/template.html? | Yes, after the Phase 1 review and alone in its commit, gated on `--check` | Tested byte-identical on a scratch copy (C2 a) | Section 3, T6 |

Also for Patrick, on his own settings rather than this repo: add a trusted-repo line for this repo to the user-level autoMode environment. It currently names only two other repos and says "assume private", while this repo is public (C1 F10). Suggested text: `Trusted repo: I:\climate-curriculum (PUBLIC GitHub repo; library/ and private/ are git-ignored; never push without Patrick)`.

### 1C. Keep as is

- The build rule: source in, docs/index.html out, never hand-edited, UTF-8 and LF (CLAUDE.md:12-19).
- "If two sources conflict and neither ranks higher, ask." (CLAUDE.md:44)
- "Never fill a ruling on Patrick's behalf." (DECISIONS.md:5-6). D23 adds PROVISIONAL beside it, not instead of it.
- LOCKED handling; DRAFT is never presented as final.
- The content guardrails (CLAUDE.md:82-89). D24 clarifies only when they apply.
- Stable `data-slide-id` values (CLAUDE.md:79-80). The checker is changed to match them.
- Feature branch, no push, Patrick pushes; git and PowerShell commands are explained to him.
- Chromebook target, WCAG 2.2 AA, the three viewports, 44px taps.
- House style and the em dash ban.
- The global verification policy and the heredoc hook. Nothing this repo needs is blocked by them: edits go through Edit, and the build runs by path.
- No CDNs and no unapproved libraries. That is why the probe runs through the playwright-cli already on the machine and adds nothing to the repo.

---

## 2. Repo organization and migration order

### 2.1 Proposed tree

Key: [C] committed, [L] local only (git-ignored), [B] build output (committed, never hand-edited), [later] created only when its first file exists.

```
climate-curriculum/
  README.md  CLAUDE.md  .gitignore  .gitattributes        [C]
  .claude/                     [C or L per D22] [later]
    skills/cc-*/SKILL.md
    settings.json              allowlist (section 3, T5)
    settings.local.json        [L]
  tools/                       [C] check.py, probe.js, probe-summary.py
  curriculum/                  [C] keep the four filenames (outside links point to them)
  modules/                     [C] [later, D28] public-safe modules only
    README.md                  module contract and index
    m-<place>-<topic>/
      module.md                teacher guide and frontmatter (2.3)
      case/                    frozen case pack: small data, credited stills, provenance.md
      slides/                  [after D10] built with the shared engine
  source/                      [C]
    build.py                   adds --check now; reads order.txt after D10
    template.html              until D10
    columbia_svg.json
    order.txt  shell/ css/ slides/ js/     [after D10]
  docs/                        [C] GitHub Pages root: outputs and static assets only
    index.html                 [B] the workshop
    m-<module-id>.html         [B] [later, D29] flat beside index.html
    downloads/                 [later, D30]
    img/  fonts/  .nojekyll
  planning/                    [C per D12]
    PLAN  DECISIONS  VERIFY  MEDIA-CREDITS  VOICE-PASS  HANDOFF  LAUNCH-PROMPT
    revision-notes-2026-10-14.md          frozen input (read-only on disk)
    CURRICULUM-PLAN.md         [later, D26]
    PERMISSIONS.md             [later, with the first Tribe-named item]
    briefs/<slide-id>.md       [later, Phase 7]
    research/<topic>.md        [later] public sources only
  library/                     [L] exists; INDEX.md, gdrive/, nexus/, _synthesis/, _inbox/
  private/                     [L] [later]
    events/YYYY-MM-DD-<slug>/  run sheets and local notes for an event
    modules/m-<place>-<topic>/ modules awaiting or under a Nation's permission
    out/                       local builds of private module pages
```

Two traps to design around (C3):
- The machine-wide gitignore ignores `build/` and `dist/`, so no folder may use those names.
- The workshop is one HTML page plus `img/` and `fonts/` beside it, not literally one file. Every page in `docs/` must keep those relative paths working.

### 2.2 Committed versus local

The real publishing line is "committed or not", because the whole repo is public, not just `docs/`.

| Material | Where | Committed |
|---|---|---|
| Workshop source, build, tools | `source/`, `tools/` | yes |
| Built pages and assets | `docs/` | yes (build output) |
| Lessons and syllabi | `curriculum/` | yes; Tribe-specific passages need a PERMISSIONS row |
| Planning record, briefs, public-source research | `planning/` | per D12 (already in branch history) |
| Public-safe modules | `modules/` | yes (D28) |
| Tribe-specific modules, event material, local builds | `private/` | never |
| Collected sources and team reports | `library/` | never |
| Project skills and settings | `.claude/` | per D22; `settings.local.json` never |
| Probe output and screenshots | session scratchpad | never |

### 2.3 Naming rules and drop-in text

- Folders and files: lowercase kebab-case, ASCII. The four `curriculum/*.md` names stay as they are.
- Dates in filenames are `YYYY-MM-DD` (they sort); dates in prose are MM/DD/YYYY. The split is intentional.
- Slide ids `sNN-<slug>` are frozen once assigned. A new slide takes the next unused number, and a retired number is never reused. Order lives in `source/order.txt` after D10. Hash URLs stay positional (`#s4`), so notes and docs cite ids, not hashes.
- Modules are `m-<place>-<topic>` (for example `m-nooksack-atmospheric-river`, `m-columbia-gorge-drought`), with the place named by river or basin (D28). Slide ids inside a module are `mNN-<slug>`.
- Project skills are `.claude/skills/cc-<name>/`.
- Library items are `library/<origin>/<group>/<slug>[-YYYY].md`. Index columns: Title | Locator | Kind | Relevance | Extracted | Reason | Tier. Tier is one of public, atni-internal, tribe-specific or personal. Committed files cite only Tier public. The `tsdf` skill can help assign tiers.

`module.md` frontmatter (from C3). Fill it with values; never invent Tribe content:

```
id: m-<place>-<topic>
title:
four_question: Q1          # Q1 cloud, Q2 knowing, Q3 doing, Q4 together
workshop_hooks: []         # slide ids, e.g. s04-cloud-tool
course_hooks: []           # e.g. CRCCT 1.2, CCIC-200 Week 2, TCR-201 Week 4
grades: []                 # 6-8, 9-12, 200, 201
minutes: 20
tools: []                  # ATNI Climate tool repo names
tools_checked: YYYY-MM-DD  # when tool claims were checked against the tool itself
offline: case-pack         # case-pack | live-only
permission: none-needed    # none-needed | requested | granted | withheld (see planning/PERMISSIONS.md)
status: idea               # idea | brief | draft | taught
```

`tools_checked` exists because the tool reviews found syllabus text that overstates what some tools do today.

CLAUDE.md "Where things are": add these lines when the folders exist (N11 already covers library/ and private/):

```
- tools/       check.py (static gate), probe.js (layout probe); see .claude/skills
- .claude/     project skills cc-* (build check, viewport, slide change, ledgers,
               decisions, modules)
- modules/     public-safe place-based modules, one folder per m-<place>-<topic>
```

The README "Data sovereignty" section gets one added sentence: "Tribe-specific modules and materials stay out of this public repository until the Tribe has given permission."

### 2.4 Migration order

**Step 0. Now, before 10/23. Housekeeping only; the page does not change.** N1 to N14, plus T1 (section 3). Create `private/events/2026-10-23-teachers-workshop/` locally, so that workshop-day material never lands in the repo by accident.

**Step 1. Also safe before 10/23: tools that read the page and never change it.** T2 (`build.py --check`), T3 (`tools/check.py`) and T4 (`tools/probe.js`). Install `cc-build-check` and `cc-viewport` first. If the workshop needs last fixes, these two are the gates.

**Step 2. Rulings before the first push.** D21 (freeze) first, because it is time-bound. Then D12, D22 and the ballot (D23). If D12 is "local", the history rewrite is prepared by a session and run by Patrick.

**Step 3. After 10/24.** The remaining skills, the user-level agent and `curriculum-align` (T5). Then `planning/CURRICULUM-PLAN.md` (D26). `planning/PERMISSIONS.md` is seeded with the Tribe-named public content already in `curriculum/` (for example the TCR-201 Week 4 worked example), status "to confirm". The library tools register goes in `library/_synthesis/` so `cc-module` has a stable input.

**Step 4. D10 split (PLAN 2b, after the Phase 1 review, before 3a).** T6, alone in its commit. The engine (navigation, notes, clock, highlight, presenter keys, chrome) stays in its own `js/` and `css/` parts, separate from per-slide interactives, so module decks can reuse it.

**Step 5. First module.** The `modules/` (or `private/modules/`) folder is created with the first `module.md`. The build learns more than one page: `modules/<id>/` builds to `docs/<id>.html`, and `private/modules/<id>/` builds to `private/out/<id>.html`. Each page inlines its own case-pack data.

**Step 6. S22 downloads (D30). Step 7. Student pages (D13). Step 8. CI (D31).** When the revision-notes scope is complete, move it and the finished briefs to `planning/archive/`.

---

## 3. Tooling, smallest first

Each tool is read-only against the repo except the build. Probe output and screenshots go to the scratchpad, never to `docs/`.

**T1. `.gitignore` and `.gitattributes`** (N2, N3). No code.
Acceptance: `git check-ignore -v library private .playwright-cli` names the repo `.gitignore` for each path; `git add --renormalize .` stages nothing; a rebuild gives no CRLF warning.

**T2. `build.py --check` (6 lines, on the current single-template build).** It becomes the gate for "a markup-only change leaves the page identical" and, later, for the split. Replace the last three lines of source/build.py and add `import sys` at the top:

```python
out = head + t.replace('__MAP__', m) + '</body></html>'
dest = root / 'docs/index.html'
if '--check' in sys.argv:  # build in memory only; exit 1 if the committed page is stale
    same = dest.read_bytes() == out.encode('utf-8')
    print('docs/index.html is up to date' if same else 'docs/index.html differs from a fresh build')
    sys.exit(0 if same else 1)
dest.write_text(out, encoding='utf-8', newline='\n')
print('built docs/index.html')
```

Tested this session in memory against the live tree, with nothing written: it prints "up to date" and exits 0. With one byte appended to the output it prints "differs" and exits 1.
Acceptance: the same two results on the real file. Revert the one-byte change afterwards.

**T3. `tools/check.py` (static gate, stdlib only; full text in Appendix A).** It reports ERROR (exit 1) for an em dash, an external src, stylesheet or `url()` in the built page, a network call, a missing `img/` or `fonts/` asset, or a missing, malformed or duplicate slide id. It reports WARN (exit 0) for lowercase Tribal terms, "stakeholder" and filler words. Knowledge, Nations, Peoples and Beings are left to judgment until D20 is ruled. This is C4's script with two edits: the slide-id position check is removed, and the root is `parents[1]` because the file lives in `tools/`.
Acceptance: `python tools/check.py --selftest` prints `selftest ok`. `python tools/check.py` gives `0 error(s), 17 warning(s)` on the 10/14/2026 tree. Both were run this session on the edited text.

**T4. `tools/probe.js` and `tools/probe-summary.py` (layout probe; full text in Appendices B and C).** It runs through the playwright-cli 0.1.22 already installed, with nothing added to the repo. It covers 3 viewports, notes closed and open, and 23 slides. It reports slide and inner scroll, horizontal scroll, `<br>` line counts, tap targets under 44px (and under 24px), unequal sibling heights, text under 12px, unnamed buttons, images without alt, the h1 count, and frame timing under 4x CPU throttle. The run takes about 66 seconds. Run it from the scratchpad:

```
playwright-cli -s=probe open
playwright-cli -s=probe --raw run-code --filename I:/climate-curriculum/tools/probe.js > probe-out.txt
playwright-cli -s=probe close
python I:/climate-curriculum/tools/probe-summary.py probe-out.txt
```

Known limit: the URL is hard-coded to this machine's `file:///I:/climate-curriculum/docs/index.html`. C2 loaded `file://` this way through `page.goto` inside run-code. C4 found that `playwright-cli open file://...` is refused. If `file:` stops working, serve the folder with `python -I -m http.server 8765 --bind 127.0.0.1 --directory docs` and change the URL constant to `http://127.0.0.1:8765/index.html`.
Acceptance: `h1Count 0`. At 1366x768 with notes open: S2 +47px, S4 `.ctl` +94px, S10 `.stop` +159px (it scrolls by design), S16 +80px, S20 +101px, S23 +23px. There is no horizontal scroll at any width. This is the 10/14/2026 baseline from C2, and C4 independently reproduced it.

**T5. Skills, agent and project settings** (section 4). Install them to the paths in 4.1. If D22 is "commit", add `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(python source/build.py:*)",
      "Bash(python tools/check.py:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git show:*)"
    ]
  }
}
```

Acceptance: each skill appears in the session's skill list. `/cc-build-check` reproduces the T3 counts. A dry run of the agent ("review CCIC-200 Week 1 against its NESC 215 lineage; return the review in your message") returns a list of what it read, writes no file, and leaves `git status` unchanged.

**T6. D10 split (Step 4).** Use C2's one-time `split.py` and its 25-line `build.py`, which reads `source/order.txt`. Both are kept in the archived C2 report (N1). Update `tools/check.py` in the same commit so it joins the order.txt parts instead of reading template.html; that limit is marked in the script with a `shortcut:` comment. Update the CLAUDE.md build rule in the same commit too. Do not reflow long lines or drop dead CSS in this commit.
Acceptance: `python source/build.py --check` exits 0 after the split. Appending one space to any slide file makes it exit 1. Tested on a scratch copy: 61 parts, largest 144 lines, exit 0, then exit 1.

**T7. CI check (D31, after T6):**

```yaml
name: check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.13' }
      - run: python source/build.py --check
      - run: python tools/check.py
```

Acceptance: green on a clean push; red when docs/index.html is stale.

**T8 (optional).** Port C4's body-copy word-balance count (6 lines, `p` text only) into `tools/probe.js`, so the PLAN "word balance before each STOP" gate is measured rather than counted by hand.
Acceptance: it reports S13 Key Lesson and Key Takeaway as 32/24, which matches the deep review's hand count.

---

## 4. Skills and the curriculum-specialist agent

### 4.1 Install map

| Item | Path | Level | Reuses |
|---|---|---|---|
| curriculum-specialist (agent) | `~/.claude/agents/curriculum-specialist.md` | user | pf-voice, curriculum-align, cc-ledger |
| curriculum-align | `~/.claude/skills/curriculum-align/SKILL.md` | user | none (no existing alignment skill) |
| cc-build-check | `.claude/skills/cc-build-check/SKILL.md` | project | `tools/check.py`, pf-voice |
| cc-viewport | `.claude/skills/cc-viewport/SKILL.md` | project | `tools/probe.js`, playwright-cli |
| cc-slide-change | `.claude/skills/cc-slide-change/SKILL.md` | project | cc-decide, cc-build-check, cc-viewport, cc-ledger |
| cc-ledger | `.claude/skills/cc-ledger/SKILL.md` | project | the ledger files' own headers |
| cc-decide | `.claude/skills/cc-decide/SKILL.md` | project | DECISIONS.md |
| cc-module | `.claude/skills/cc-module/SKILL.md` | project | curriculum-specialist, curriculum-align, tsdf |

Not duplicated: pf-voice (voice), codex-adversary (outside review), session-handoff, pickup and trueup (session rituals), claim-verifier (fact lookups; cc-ledger may hand a claim to it, but whether its output fits the VERIFY row is not verified), tsdf (data tiers).

### 4.2 Agent: `~/.claude/agents/curriculum-specialist.md`

At install, replace `<ARCHIVE_PATH>` with the local teaching-archive path. It is left out of this public file on purpose. The `effort` field follows the frontmatter of the sibling ATNI agents; whether the harness honors it is not verified.

```markdown
---
name: curriculum-specialist
description: Curriculum development specialist for the ATNI Climate education pathway, centered on the Columbia River Climate Change Teachers curriculum at I:\climate-curriculum (the "Understanding a Climate of Change" workshop, Grades 6-12 hands-on lessons, CCIC 200, TCR 201) and its lineage from NESC 215 at Northwest Indian College. Designs and reviews lessons, place-based modules, syllabi, assessments, and alignment matrices, and drafts in-class modules built on ATNI Climate tools. Use for pedagogy, sequencing, alignment, and content review; not for slide engineering, builds, or git work.
tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Skill, Write, Edit
model: opus
effort: high
---

You are the curriculum development specialist for ATNI Climate's education
pathway. This file carries no project state on purpose; a snapshot here goes
stale. Orient from the files every time, in this order:

1. `I:\climate-curriculum\CLAUDE.md`: house style, content guardrails, and the
   precedence order. It outranks anything below.
2. `planning/HANDOFF.md` (top entry), `planning/PLAN.md`, and, when it exists,
   `planning/CURRICULUM-PLAN.md`: where the work is. `planning/DECISIONS.md`:
   what Patrick has ruled; PENDING means unruled; PROVISIONAL means drafted on
   a default and still unruled. `planning/revision-notes-2026-10-14.md`: scope
   source of truth, frozen.
3. The curriculum, `curriculum/*.md`:
   - the Guiding Document: the spine. The Four Questions (How does a cloud
     work? How do you know what you know? What can we do? How do we work
     together?) and the table mapping each Part to the workshop slides,
     Grades 6-12, CCIC 200, and TCR 201.
   - the Grades 6-12 lessons (Standards Alignment section).
   - the CCIC 200 syllabus: adapted from NESC 215; the list near the top of
     what it keeps from NESC 215 is your lineage statement.
   - the TCR 201 syllabus: the action course.
4. The source library, `library/` (git-ignored, local only): start at
   `library/INDEX.md`, else every `INDEX*.md` under `library/`. Each row has a
   Tier; only Tier public may be quoted or paraphrased into a committed file.
   Cite library items by locator, never from memory. Originals in
   `<ARCHIVE_PATH>` and in Google Drive are read-only to you; never edit,
   share, or comment on them.

Lineage: NESC 215 (Climate Change in Indian Country, Northwest Indian
College, taught by Patrick) is the root of the 200-level course; CCIC 200
keeps its shape and TCR 201 takes the student's plan to decision-makers. The
workshop and the Grades 6-12 lessons sit upstream of both. Verify any detail
of NESC 215 against the library copy before relying on it. Keep the pathway
coherent: a change at one level names its effect on the others.

Alignment frameworks in use: NGSS performance expectations (Grades 6-12),
Washington Since Time Immemorial (RCW 28A.320.170), Common Core ELA Speaking
and Listening, and the college's catalog outcomes (postsecondary). Oregon and
Idaho classrooms may need their own state frameworks: check, do not assume.
Use the `curriculum-align` skill for any matrix; never invent a standard code.

Standing guardrails:

- Never write the em dash (U+2014). Follow CLAUDE.md house style; for any
  public-facing prose load the `pf-voice` skill and follow it. Patrick writes
  his own first-person voice: leave `[PERSONAL VOICE -- Patrick writes this
  section]` rather than simulate it.
- Tribal Nations are sovereigns and rights holders, never stakeholders.
  Plants, animals, and waters are relatives.
- Cultural content, Tribe-specific stories, place names beyond public
  sources, and anything a Nation has not confirmed: mark it
  `[NEEDS TRIBAL CONFIRMATION: <Nation>]` and leave it unwritten. Traditional
  Ecological Knowledge, sacred sites, and places that could be harmed are a
  stop: never sought, never inferred, never drafted.
- Do not fill bracketed placeholders only ATNI staff or a Tribe can supply.
- Knowledge holders and Elders are compensated and credited as they choose;
  a module that invites them says so.
- No student data anywhere: no names, grades, rosters, or submissions in any
  file you write. Student work stays with the student: no module may require
  accounts, uploads, analytics, or network calls for student data.
- Every fact, threshold, date, or statistic you introduce gets a proposed
  VERIFY row (`cc-ledger` skill) with a source you opened. Unverified stays
  OPEN.
- Every DRAFT you write is labeled DRAFT and gets a proposed VOICE-PASS row.
- Materials by other teachers or organizations are cited with their rights
  noted; quote only short excerpts.

How you work:

- Read before you propose. Quote the file and line you build on. Planning
  documents have been wrong about the source before; check the source itself.
- Design for the room: school Chromebooks, mixed grade levels, a 30-minute
  workshop segment or a 50-minute class period, a low-tech version of every
  interactive, and the three scales (Frog's Eye, Bird's Eye, Moon's Eye).
- Write only to the paths your task names. With no path named, return the
  draft in your final message. Never edit `docs/`, `source/`, `CLAUDE.md`,
  the revision notes, or a DECISIONS ruling. Never commit or change git state.
- When a choice belongs to Patrick, say so and give a default; do not decide.

Final message: what you read (paths and lines) versus only inventoried, the
draft or review, open questions for Patrick with defaults, proposed ledger
rows, and anything marked for Tribal confirmation. Say "not verified"
wherever you inferred.
```

### 4.3 `~/.claude/skills/curriculum-align/SKILL.md`

```markdown
---
name: curriculum-align
description: Map a lesson, module, unit, or syllabus to the frameworks it must answer to - NGSS performance expectations, state Tribal sovereignty curricula (Washington Since Time Immemorial; Oregon and Idaho equivalents where taught), Common Core ELA, institutional course outcomes (for example a college catalog's outcomes for a predecessor course) - and to the curriculum's own spine, producing an alignment matrix with every code checked on the issuer's own page. Use when writing or revising learning outcomes, building a standards table, or checking a course against its predecessor.
argument-hint: "[path to the lesson or syllabus] [frameworks, or 'default']"
user-invocable: true
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Edit, Write
---

1. Read the target and list its learning goals and activities by heading
   and line.
2. Pick frameworks: the ones named, else by level and place. Grades 6-12:
   NGSS PEs plus the state Tribal sovereignty curriculum, and Common Core ELA
   where discussion or writing is assessed. Postsecondary: the institution's
   catalog outcomes and the predecessor course's outcomes. Always: the
   curriculum's own spine (for the climate curriculum, the Four Questions
   and Parts).
3. For each code, open the issuer's page (NGSS, the state education agency,
   the institution's catalog) and quote the expectation. A code you cannot
   open is marked `[verify]`, never guessed. Never invent a code or a
   standard's wording.
4. Matrix: `| Goal or activity (file:line) | Framework | Code | Expectation (quoted) | Strength (addresses / touches) | Source URL and date |`.
   Mark gaps both ways: goals with no standard, and required standards no
   activity reaches.
5. Write where the caller says (else return it). Dates MM/DD/YYYY; no em
   dash; recommend, never rewrite outcomes the author owns.
```

### 4.4 `.claude/skills/cc-build-check/SKILL.md`

```markdown
---
name: cc-build-check
description: Rebuild the workshop page and run the static gate - em dash, offline self-containment, network calls, missing images or fonts, slide-id integrity, and house-style warnings across source, curriculum, and planning. Use after every source change, before every commit, and when asked to "build", "check the build", or "run the gate".
argument-hint: "[optional: markdown or html paths for a house-style-only check]"
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
---

1. Markup-neutral change (refactor, ids, comments): run
   `python source/build.py --check` instead of building. Exit 0 proves the
   built page is unchanged; exit 1 means it is not, so find out why first.
2. Content change: `python source/build.py` (fall back to `py`). Then
   `git diff --stat -- docs/index.html` and
   `git diff --word-diff -- docs/index.html`; everything in the diff must be
   intended.
3. Gate: `python tools/check.py` (with paths after it, house style on those
   files only).
   - ERROR lines fail the gate (exit 1); fix them before anything else.
   - WARN lines are for a human. A cited title keeps its published casing;
     a generic plural "treaties" may be right. Decide each one; never
     mass-replace.
   - Knowledge, Nations, Peoples, and Beings are not checked; read them
     yourself in any text you wrote (see D20).
4. Prose you wrote also gets a pf-voice pass (load the pf-voice skill); the
   script checks mechanics, not voice.
5. Report: the build or check line, the diff summary, error and warning
   counts, and each warning you accepted with its reason.

Never hand-edit docs/index.html. Never edit tools/check.py mid-task to make
a gate pass; report the problem instead.
```

### 4.5 `.claude/skills/cc-viewport/SKILL.md`

```markdown
---
name: cc-viewport
description: Render the built workshop at 1920x1080, 1366x768, and 390x844 with speaker notes closed and open, and measure clipped or scrolling content, hall lines that break away from their intended br, tap targets under 44px, unequal sibling heights, text under 12px, missing names and alt text, the h1 count, and frame timing under 4x CPU throttle. Use after any layout or copy change, before every STOP, and when asked to "check viewports" or "check layout".
argument-hint: "[optional: slide ids to focus the report on]"
user-invocable: true
allowed-tools: Read, Bash
---

Run cc-build-check first; this probes docs/index.html as built. Run from
the session scratchpad, never the repo root, and write all output there.

1. `playwright-cli -s=probe open`
2. `playwright-cli -s=probe --raw run-code --filename I:/climate-curriculum/tools/probe.js > probe-out.txt`
   (about a minute). If the file: URL is refused, serve docs/ with
   `python -I -m http.server 8765 --bind 127.0.0.1 --directory I:/climate-curriculum/docs`
   as a background task and point the probe's URL at
   http://127.0.0.1:8765/index.html for this run only.
3. `playwright-cli -s=probe close` (and stop the server if you started one).
4. `python I:/climate-curriculum/tools/probe-summary.py probe-out.txt`
5. Read the findings:
   - `slideScroll`, `innerScroll`: content taller than its box. At 1920 and
     1366 this is a defect unless it scrolls by design (S10 stop card). At
     390 slide-level scroll is the phone layout; look only at innerScroll.
   - `hScroll`: horizontal page scroll; always a defect.
   - `lineBreaks`: a line with br renders a different line count than
     intended (the S1 stanza rule).
   - `tapTargets`: under 44x44 breaks the CLAUDE.md rule; `FAIL-2.5.8`
     (under 24) means check WCAG 2.2 SC 2.5.8, whose spacing exception the
     probe does not apply.
   - `unequal`: siblings in one row differ by more than 2px.
   - `under12px`, `unnamedButtons`, `imgNoAlt`, `h1Count`, and `PERF`
     (relative frame timing; headless is not a Chromebook).
6. Word balance (PLAN gate) is not measured yet: for slides you changed,
   count the p text of sibling cards yourself.
7. Report by S-number and plain title, viewport, notes state; compare with
   the last run and say what changed. Screenshots, if needed, go to the
   scratchpad.

Baseline 10/14/2026 (before Phase 1): h1Count 0; 1366x768 notes open:
S2 +47, S4 .ctl +94, S10 .stop +159, S16 +80, S20 +101, S23 +23 px; no
horizontal scroll at any width.
```

### 4.6 `.claude/skills/cc-slide-change/SKILL.md`

```markdown
---
name: cc-slide-change
description: The procedure for any change to a workshop slide - locate it by data-slide-id, confirm the decision gate and any LOCKED text, check the premise against the source, edit source only, rebuild and gate, probe viewports, record ledger rows, keep speaker notes and the low-tech version in step, and commit one slide per commit without AI attribution. Use whenever a task edits slide copy, layout, notes, or an interactive.
argument-hint: "[slide id or S-number] [what changes]"
user-invocable: true
allowed-tools: Read, Grep, Glob, Edit, Bash, Skill
---

Target: `$ARGUMENTS`. If empty, ask which slide and stop.

1. Locate: grep `data-slide-id="sNN-` in the source (source/template.html,
   or source/slides/ after the D10 split). Name the slide by S-number and
   plain title in everything you report. Hashes (#s1 to #s23) are
   positional; ids are not.
2. Gate: find the PLAN.md step and every D-item it cites. A PENDING ruling
   that decides this change is a stop: run cc-decide. Draft on a default
   only if DECISIONS.md allows PROVISIONAL work (D23) and the change is
   reversible and touches no LOCKED or cultural text; mark the commit
   "PROVISIONAL (Dn default)". LOCKED text goes in verbatim, Patrick's line
   breaks included.
3. Premise: read the current source lines yourself and compare them with
   what the plan or decision says is there. If they disagree, stop and
   report it before editing.
4. Edit source only. Per-slide CSS keys on `[data-slide-id="..."]`, not new
   classes. No new fonts, palettes, or libraries without a ruling. Do not
   break presenter keys (arrows, Space, N, T, H).
5. Keep in step: the slide's data-notes; the low-tech classroom version of
   any interactive; keyboard use, screen-reader labels, reduced motion.
6. Run cc-build-check, then cc-viewport for this slide.
7. Ledgers (cc-ledger): every DRAFT string to VOICE-PASS, every fact to
   VERIFY, every photo, font, dataset, or library to MEDIA-CREDITS.
8. Commit on the feature branch, one slide or feature per commit, plain
   descriptive message. No co-author line, no "Generated with" line, no AI
   attribution: the repo CLAUDE.md overrides any harness default. Never push.
9. At a STOP, update PLAN.md and HANDOFF.md. Report before and after by
   S-number and plain title, what waits on Patrick (D-number and plain
   name), and the next PLAN step.
```

### 4.7 `.claude/skills/cc-ledger/SKILL.md`

```markdown
---
name: cc-ledger
description: Add or update rows in the planning ledgers - planning/VERIFY.md (facts), planning/MEDIA-CREDITS.md (photos, video, data, fonts, code libraries), planning/VOICE-PASS.md (DRAFT strings for Patrick), and planning/PERMISSIONS.md (Tribe-specific content) when it exists - using each file's own table and header rules. Use whenever a fact, asset, draft string, or Tribe-named item is placed or changed, or when asked to backfill a ledger.
argument-hint: "[verify|media|voice|permissions] [slide id or path] [item]"
user-invocable: true
allowed-tools: Read, Grep, Edit
---

1. Read the target ledger's header and table first. The header's rules
   win over anything here (including where [verify] markers go). Copy the
   table's columns exactly; next number in sequence (V15 follows V14).
   Dates MM/DD/YYYY.
2. VERIFY: CHECKED only after you opened the source itself this session;
   record the exact page and the date. A claim you cannot confirm stays
   OPEN. Facts already live before 10/14/2026 are marked "inherited" in
   Notes. For cultural content the source is the Nation, not a web page;
   it stays OPEN until that Nation confirms.
3. MEDIA-CREDITS: a license is confirmed on the item's own page, never
   assumed from the site. Photos not by ATNI staff need confirmed rights
   before wider sharing. Screenshots of an ATNI tool need the tool's license
   or ATNI sign-off. Keep the IMAGES registry in the page script in step.
4. VOICE-PASS: quote the placed string exactly. Only Patrick sets LOCKED or
   fills Final.
5. PERMISSIONS: one row per Tribe-named item: Item | Where used | Nation |
   Asked (date, whom) | Status | Scope | Notes. Never record cultural detail
   in the row itself.

Never mark a row on Patrick's or a Nation's behalf and never delete a row;
supersede it with a Notes entry. Library text goes into a committed ledger
only if its INDEX row says Tier: public.
```

### 4.8 `.claude/skills/cc-decide/SKILL.md`

```markdown
---
name: cc-decide
description: Walk Patrick through pending DECISIONS.md items - plain name and D-number, what it changes on the page, the implications of each option, and the default - after checking each decision's premise against the current source; then record his ruling verbatim. One at a time by default; as a ballot only where Patrick has allowed it. Use when a plan step is gated on a PENDING decision, when Patrick asks to go through decisions, or when a new question needs a D-number.
argument-hint: "[D-number, 'next', or 'ballot']"
user-invocable: true
allowed-tools: Read, Grep, Edit
---

1. Mode. Read the DECISIONS.md header. Unless it records that Patrick
   allows ballots (D23), present exactly one decision per message and wait.
   If ballots are allowed: decisions that change LOCKED wording or cultural
   content still go one at a time; the rest may go in one message, each
   with its default, so he can answer "defaults, except ...".
2. Premise check: read the source lines each decision is about (cite
   file:line) and confirm the decision describes them correctly. If not,
   say so first and propose corrected wording.
3. Present each: D-number and plain name; what changes on the page
   (S-number and plain title); each option with its concrete consequences,
   including which other D-items it settles or reopens; the default.
4. Record: change "Ruling: PENDING" to his choice in his words, with the
   date (MM/DD/YYYY). "Sounds good" to a default is a ruling for the
   default; say so when you record it. Update any "See Dn" cross-reference
   the ruling settles. Never fill a ruling he did not give, and never
   decide by silence. A PROVISIONAL draft stays PROVISIONAL until he rules.
5. A new question gets the next D-number with question, options, default,
   and "Ruling: PENDING".
```

### 4.9 `.claude/skills/cc-module/SKILL.md`

```markdown
---
name: cc-module
description: Design a modular, place-grounded in-class segment that uses an ATNI Climate tool (drought, hazards, land use, adaptation profiles, policy and funding, geospatial) to ground one of the Four Questions in the place where the class is taught - for the workshop, Grades 6-12, CCIC 200, or TCR 201 - and write it as a module brief for Patrick. Use when asked for a place-based module, an in-class presentation built from an ATNI tool, or a local version of a lesson.
argument-hint: "[place] [Four Question or Part] [audience] [optional tool]"
user-invocable: true
allowed-tools: Read, Grep, Glob, Write, Agent, Skill
---

Inputs: a place (a river, basin, or landscape), a Four Question or Part, an
audience level, and optionally a tool. If any is missing, ask, then stop.

1. Ground: read `library/INDEX.md` (or every `library/**/INDEX*.md`) and
   the tools register in `library/_synthesis/` for what each ATNI tool
   shows today, whether it is public, its license, and its offline story.
   Read the Guiding Document's Part-to-level table so the module lands at
   the right level.
2. Choose the tool by what the place needs, not by what is newest. Public
   data only; no Tribe-specific data without that Nation's consent.
3. Place the module (D28): public data and no cultural content go to
   `modules/m-<place>-<topic>/`; anything naming a Nation's own material
   goes to `private/modules/m-<place>-<topic>/`. Name the place by river or
   basin. Create `module.md` with the frontmatter in modules/README.md
   (status: brief).
4. Delegate the draft to the `curriculum-specialist` agent with the inputs,
   the tool facts you found (with locators), and the module.md path.
5. The brief has: Question and level; learning goal; a 10 to 20 minute flow
   at three scales (Frog's Eye: a local observation; Bird's Eye: the tool's
   view of the watershed; Moon's Eye: the regional or global pattern); the
   tool step with an offline case pack (small data and credited stills in
   case/, with provenance.md; no live network in class); a low-tech
   version; a reflection prompt; alignment (run curriculum-align); VERIFY
   rows; MEDIA-CREDITS rows; PERMISSIONS rows and
   `[NEEDS TRIBAL CONFIRMATION: <Nation>]` markers; open questions for
   Patrick with defaults.
6. Run cc-build-check on the brief (house style); load pf-voice for any
   student-facing copy. Do not build slides from a brief until Patrick
   approves it.
```

---

## 5. What not to build

1. **A voice or copy-writing skill.** pf-voice owns the voice, and CLAUDE.md carries the curriculum extras. A third copy would drift.
2. **A repo steward agent.** This repo's CLAUDE.md already does that job.
3. **A library-lookup skill.** `library/INDEX.md` plus Grep is enough until the library outgrows an index.
4. **A test framework in the repo** (package.json, a Playwright test project, axe-core). The repo stays vanilla with no dependencies. Contrast checking with axe-core would need Patrick's approval under the vendoring rule.
5. **The browser probe in CI.** It needs a browser download, the timing is flaky, and the layout verdicts need a human.
6. **Hooks that block writes** (for example an em dash PreToolUse hook). The gate runs at build and commit time.
7. **A DDM-style specialist roster.** Revisit at Phase 3 (cloud tool rebuild), where a read-only design critic and a science verifier would earn their place.
8. **A Codex skill.** codex-adversary exists at user level; a curriculum review is a prompt for it.
9. **Drive or archive sync automation into `library/`.** The harvest needs a sensitivity judgment per file.
10. **Any structural change before 10/24/2026**, or a split tool before D10 is ruled. Once the split happens, no reflow, renames or dead-code removal inside the split commit.
11. **New per-session ritual skills.** pickup, trueup and session-handoff already exist.
12. **`source/decks/`, `docs/modules/` subfolders, or `planning/SLIDE-MAP.md`** until a second deck, D29 or a real need asks for them.

---

## 6. Open questions for Patrick (each with a proposed default)

1. Does the teachers workshop on 10/23 and 10/24/2026 use this deck, and from which build? Default: yes; pick main or this branch by 10/21, tag it, keep an offline USB copy, and do not merge from 10/21 to 10/24 (D21).
2. D12: commit planning/? Default: commit; it is already in branch history.
3. Commit `.claude/skills/` to the public repo? Default: yes; the agent stays at user level (D22).
4. Allow a ballot for non-LOCKED decisions and a PROVISIONAL state? Default: yes (D23).
5. "Ships" means merged to main, and `[verify]` markers go in speaker notes? Default: yes (D24).
6. May a session keep working at a STOP, and draft the Phase 7 briefs now? Default: yes; builds stay on hold (D25).
7. May Claude draft curriculum/ changes on a branch for your approval? Default: yes, tracked in planning/CURRICULUM-PLAN.md (D26).
8. Should the AI-attribution ban cover only git and code? Default: yes; disclosure in course materials is your call each time (D27).
9. D20: capitalize "Knowledge" only when it names Indigenous or Traditional Knowledge? Default: yes.
10. Public modules only with public data and no cultural content, or with a granted permission, and named by river or basin? Default: yes (D28).
11. Module pages flat in docs/? Default: yes (D29). S22 downloads as Markdown copies for now? Default: yes (D30). CI check after D10? Default: yes (D31).

---

## What I read, ran, and did not check

- **Read in full:** C1.md, C2.md, C3.md, C4.md; I:/climate-curriculum/CLAUDE.md; source/build.py.
- **Read in part:** planning/VERIFY.md and VOICE-PASS.md (headers), PLAN.md lines 1-25, the DECISIONS.md heading list.
- **Compared:** C2's probe text against its tested file (they differ only in comments and an equivalent `noAlt` expression; Appendix B is the tested file). The user-level skill and agent folders, listed by name, to rule out duplicates.
- **Ran, read-only and in memory, with no file written:** the edited `check.py` (`selftest ok`; 0 errors and 17 warnings on the live tree); the `build.py --check` patch (exit 0 on the live tree, exit 1 with one byte changed). `git status` was unchanged afterwards.
- **Not checked by me:** the deep review, the library contents, the G, T, N and D reports, GitHub Pages settings, `.gitattributes` renormalize behavior, the T6 split (C2 tested it on a scratch copy), and whether the harness honors the agent `effort` field.

---

## Appendix A. tools/check.py

C4 script with the edits named in section 3, T3. Selftest and full run verified on this exact text.

```python
"""Static gate for the climate-curriculum repo. Read-only: never writes a file.

Run after `python source/build.py`:
    python tools/check.py            # whole default set
    python tools/check.py PATH ...   # house style on named files only
    python tools/check.py --selftest

ERROR (exit 1): em dash, external src/stylesheet/url() in docs/index.html, network calls,
missing local asset, slide-id problems.
WARN (exit 0): house-style words a human should look at (lowercase Tribal terms,
"stakeholder", CLAUDE.md filler words). Judgment calls stay with pf-voice and Patrick.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')  # Windows console defaults to cp1252

EM_DASH = chr(0x2014)  # spelled as a code point so this file never contains one
# Lookarounds skip JS keys ('elders', treaty:) and URL slugs (/nonprofits-tribes-and-).
LOWER_TERMS = re.compile(r'''(?<![\w/'"-])(indigenous|tribal|tribes|elders?|treaty|treaties|first foods)(?![\w'":/-])''')
# A quoted "stakeholders" is the rule being stated, not a use.
STAKEHOLDER = re.compile(r'''(?<!["'])stakeholder''', re.I)
FILLER = re.compile(r'\b(delve\w*|tapestry|unlock\w*|empower\w*)\b', re.I)
EXT_SRC = re.compile(r'''(?:\bsrc\s*=\s*["']?|<link[^>]*\bhref\s*=\s*["']?|url\(\s*["']?|@import\s+["'])https?://''', re.I)
NETWORK = re.compile(r'\b(fetch\s*\(|XMLHttpRequest|sendBeacon|new\s+WebSocket|EventSource\s*\()')
LOCAL_ASSET = re.compile(r'''["'(]((?:img|fonts)/[\w./-]+\.(?:jpe?g|png|webp|svg|gif|woff2?|mp4|webm))''', re.I)
SECTION = re.compile(r'<section\b[^>]*class="[^"]*\bslide\b[^"]*"[^>]*>')
SLIDE_ID = re.compile(r'data-slide-id="([^"]*)"')
ID_FORM = re.compile(r'^s(\d\d)-[a-z0-9]+(?:-[a-z0-9]+)*$')


def scan_style(name, text):
    """Return (errors, warnings) lists of 'name:line: message' strings."""
    errs, warns = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if EM_DASH in line:
            errs.append(f'{name}:{n}: em dash (U+2014)')
        for rx, msg in ((LOWER_TERMS, 'lowercase term (capitalize if it names a People, role or Treaty)'),
                        (STAKEHOLDER, '"stakeholder" (Nations and relatives are not stakeholders)'),
                        (FILLER, 'filler word from CLAUDE.md list')):
            for m in rx.finditer(line):
                warns.append(f'{name}:{n}: {msg}: "{m.group(0)}"')
    return errs, warns


def scan_slides(text):
    """Every slide section has a unique, well-formed id. Ids are frozen, so the number need not match position."""
    errs, ids = [], []
    for pos, m in enumerate(SECTION.finditer(text), 1):
        sid = SLIDE_ID.search(m.group(0))
        if not sid:
            errs.append(f'slide {pos}: no data-slide-id')
            continue
        sid = sid.group(1)
        f = ID_FORM.match(sid)
        if not f:
            errs.append(f'slide {pos}: malformed id "{sid}"')
        if sid in ids:
            errs.append(f'slide {pos}: duplicate id "{sid}"')
        ids.append(sid)
    return errs, ids


def scan_built(docs, text):
    errs = []
    for n, line in enumerate(text.splitlines(), 1):
        if EXT_SRC.search(line):
            errs.append(f'docs/index.html:{n}: external resource (page must run offline)')
        m = NETWORK.search(line)
        if m:
            errs.append(f'docs/index.html:{n}: network call "{m.group(0)}" (no network for student data)')
    for rel in sorted(set(LOCAL_ASSET.findall(text))):
        if not (docs / rel).is_file():
            errs.append(f'docs/index.html: missing asset docs/{rel}')
    return errs


def selftest():
    e, w = scan_style('t', 'a ' + EM_DASH + ' b\nthe tribal council\nTribal Nations\nour stakeholders\nlet us delve\n'
                           "elders:['Elders'] /nonprofits-tribes-and- never \"stakeholders\"")
    assert len(e) == 1 and len(w) == 3, (e, w)
    e, ids = scan_slides('<section class="slide hall" data-slide-id="s01-title"><section class="slide" data-slide-id="s03-x"><section class="slide">')
    assert ids == ['s01-title', 's03-x'] and len(e) == 1, e
    assert EXT_SRC.search('<img src="https://x/y.png">') and EXT_SRC.search("url('http://x')")
    assert not EXT_SRC.search('<a href="https://atniclimate.org">')
    print('selftest ok')


def main(argv):
    if argv[:1] == ['--selftest']:
        selftest()
        return 0
    root = Path(__file__).resolve().parents[1]
    if argv[:1] == ['--root']:
        root, argv = Path(argv[1]), argv[2:]
    errs, warns = [], []
    if argv:
        files = [Path(a) for a in argv]
    else:
        # shortcut: reads the single template; switch to the source/order.txt parts in the D10 split commit
        files = [root / 'source/template.html', root / 'README.md',
                 *sorted((root / 'curriculum').glob('*.md')),
                 # revision notes are a locked scope source that quotes the banned words; not ours to fix
                 *sorted(p for p in (root / 'planning').glob('*.md') if not p.name.startswith('revision-notes'))]
        tpl = (root / 'source/template.html').read_text(encoding='utf-8')
        e, ids = scan_slides(tpl)
        errs += e
        print(f'slides: {len(ids)} ({ids[0] if ids else "-"} .. {ids[-1] if ids else "-"})')
        built = root / 'docs/index.html'
        errs += scan_built(built.parent, built.read_text(encoding='utf-8'))
        if EM_DASH in built.read_text(encoding='utf-8'):
            errs.append('docs/index.html: em dash present in build output')
        print(f'placeholders in template: {tpl.count("[PLACEHOLDER")}, [verify] markers: {tpl.count("[verify]")}')
    for f in files:
        e, w = scan_style(f.relative_to(root) if f.is_relative_to(root) else f, f.read_text(encoding='utf-8'))
        errs += e
        warns += w
    for w in warns:
        print('WARN ', w)
    for e in errs:
        print('ERROR', e)
    print(f'{len(errs)} error(s), {len(warns)} warning(s)')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
```

## Appendix B. tools/probe.js

C2 tested file, verbatim.

```js
// Viewport and accessibility probe for docs/index.html. Read-only: loads the built page over file://.
// Run:  playwright-cli open  then  playwright-cli run-code --filename probe.js  then  playwright-cli close
// Returns JSON: per viewport x notes state x slide, only the slides with findings, plus 4x-throttled frame stats.
async page => {
  const URL = 'file:///I:/climate-curriculum/docs/index.html';
  const VIEWPORTS = [[1920, 1080], [1366, 768], [390, 844]];
  const GRIDS = '.agenda,.g2,.g3,.g4,.key,.carry,.conv,.eyes,.claims,.steps3,.kin,.kinmore,.flowrow,.inst,.focus,.sort,.webwrap';
  const probe = GRIDS => {  // runs inside the page on the visible slide
    const s = document.querySelector('.slide:not([hidden])');
    const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden'; };
    const out = { id: s.dataset.slideId };
    // (a) overflow: slide scrolls, .fit children clip, page scrolls sideways
    if (s.scrollHeight > s.clientHeight + 1) out.slideScroll = s.scrollHeight - s.clientHeight;
    const clip = [...s.querySelectorAll('.inner.fit *')].filter(e => vis(e) && e.scrollHeight > e.clientHeight + 1 && getComputedStyle(e).overflowY !== 'visible')
      .map(e => `${e.tagName.toLowerCase()}.${[...e.classList].join('.')}+${e.scrollHeight - e.clientHeight}px`);
    if (clip.length) out.innerScroll = clip;
    if (document.documentElement.scrollWidth > innerWidth) out.hScroll = document.documentElement.scrollWidth - innerWidth;
    // (b) line breaks: rendered lines vs intended (<br> count + 1) in hall copy and headings
    const lines = el => { const r = document.createRange(); r.selectNodeContents(el);
      return new Set([...r.getClientRects()].filter(q => q.width > 1).map(q => Math.round(q.top))).size; };
    const brk = [...s.querySelectorAll('.hallcopy p,.hallcopy .display,.hallcopy .quote,h1,h2')].filter(vis).map(e => {
      const want = e.querySelectorAll('br').length + 1, got = lines(e);
      return e.querySelector('br') && got !== want ? `${e.className || e.tagName}: ${got} lines, want ${want}` : null; }).filter(Boolean);
    if (brk.length) out.lineBreaks = brk;
    // (c) tap targets under 44x44 (CLAUDE.md); under 24 also fails WCAG 2.2 SC 2.5.8
    const taps = [...document.querySelectorAll('button,a[href],input,select,textarea,[role=button],[tabindex="0"]')]
      .filter(e => vis(e) && (s.contains(e) || !e.closest('.slide'))).map(e => [e, e.getBoundingClientRect()])
      .filter(([, r]) => r.width < 44 || r.height < 44)
      .map(([e, r]) => `${(e.getAttribute('aria-label') || e.textContent || e.id || e.className).trim().slice(0, 24)} ${Math.round(r.width)}x${Math.round(r.height)}${Math.min(r.width, r.height) < 24 ? ' FAIL-2.5.8' : ''}`);
    if (taps.length) out.tapTargets = [...new Set(taps)];
    // (d) equal heights: siblings that share a row should match
    const uneq = [...s.querySelectorAll(GRIDS)].filter(vis).flatMap(g => {
      const rows = {}; [...g.children].filter(vis).forEach(c => { const r = c.getBoundingClientRect(); (rows[Math.round(r.top)] ||= []).push(Math.round(r.height)); });
      return Object.values(rows).filter(h => h.length > 1 && Math.max(...h) - Math.min(...h) > 2).map(h => `.${[...g.classList].join('.')}: ${h.join('/')}`); });
    if (uneq.length) out.unequal = uneq;
    // extras: text under 12px, unnamed buttons, images without alt
    const tiny = [...s.querySelectorAll('*')].filter(e => vis(e) && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && parseFloat(getComputedStyle(e).fontSize) < 12)
      .map(e => `${e.tagName.toLowerCase()}.${[...e.classList].join('.')} ${getComputedStyle(e).fontSize}`);
    if (tiny.length) out.under12px = [...new Set(tiny)];
    const unnamed = [...s.querySelectorAll('button')].filter(b => vis(b) && !(b.getAttribute('aria-label') || b.textContent.trim())).length;
    if (unnamed) out.unnamedButtons = unnamed;
    const noAlt = [...s.querySelectorAll('img:not([alt])')].length;
    if (noAlt) out.imgNoAlt = noAlt;
    return out;
  };
  const report = { h1Count: null, runs: [], perf: [] };
  for (const [w, h] of VIEWPORTS) {
    await page.setViewportSize({ width: w, height: h });
    for (const notes of [false, true]) {
      await page.goto(URL + '#s1');
      await page.reload();  // a hash-only goto keeps the old document, and with it the notes state
      await page.evaluate(() => document.fonts.ready);
      report.h1Count ??= await page.evaluate(() => document.querySelectorAll('h1').length);
      if (notes) await page.keyboard.press('n');
      const open = await page.evaluate(() => !document.getElementById('notes').hidden);
      if (open !== notes) throw new Error(`notes pane should be ${notes ? 'open' : 'closed'}`);
      for (let i = 1; i <= 23; i++) {
        await page.evaluate(i => { location.hash = '#s' + i; }, i);
        await page.waitForTimeout(350);  // slide fade
        const r = await page.evaluate(probe, GRIDS);
        if (Object.keys(r).length > 1) report.runs.push({ vp: `${w}x${h}`, notes, ...r });
      }
    }
  }
  // 4x CPU throttle (school Chromebook stand-in): frame stats while each heavy interactive runs
  await page.setViewportSize({ width: 1366, height: 768 });
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
  const frames = () => new Promise(res => { const t = []; let last = performance.now(); const end = last + 2000;
    const f = now => { t.push(now - last); last = now; now < end ? requestAnimationFrame(f) : res({ fps: Math.round(t.length / 2), worstMs: Math.round(Math.max(...t)), over50ms: t.filter(x => x > 50).length }); };
    requestAnimationFrame(f); });
  for (const [slide, act] of [[4, '#cmPlay'], [10, '#rB'], [20, '.scen button']]) {
    await page.goto(URL + '#s' + slide); await page.waitForTimeout(500);
    const idle = await page.evaluate(frames);
    await page.locator(act).first().click();
    const active = await page.evaluate(frames);
    report.perf.push({ slide, act, idle, active });
  }
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 1 });
  return JSON.stringify(report);
}
```

## Appendix C. tools/probe-summary.py

C2 summarize.py, verbatim.

```python
import json, sys
from collections import defaultdict
raw = open(sys.argv[1], encoding='utf-8').read().strip()
rep = json.loads(json.loads(raw)) if raw.startswith('"') else json.loads(raw)
print('h1Count', rep['h1Count'])
CHROME = ('Clock', 'Highlight', 'Notes', 'Previous slide', 'Next slide', 'Go to ')
chrome = defaultdict(set)
for r in rep['runs']:
    taps = r.get('tapTargets', [])
    for t in taps:
        if t.startswith(CHROME):
            chrome[r['vp']].add(t)
    r['tapTargets'] = [t for t in taps if not t.startswith(CHROME)]
for vp, s in chrome.items():
    print(f'CHROME {vp}: ' + '; '.join(sorted(s)))
for r in rep['runs']:
    rest = {k: v for k, v in r.items() if k not in ('vp', 'notes', 'id') and v}
    if rest:
        print(f"{r['vp']} notes={'open' if r['notes'] else 'closed'} {r['id']}: {json.dumps(rest)}")
for p in rep['perf']:
    print('PERF', json.dumps(p))
```
