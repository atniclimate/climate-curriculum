# Decision Packet: D27 and the decisions the module briefs surfaced

Claude proposes; Patrick rules. Nothing here is a ruling, and nothing here is
written into planning/DECISIONS.md. When Patrick rules, the ruling goes into
DECISIONS.md (D27 changes from PENDING; D28 onward are added there only if
Patrick accepts them as decisions).

Inputs: planning/modules/SEEDS.md and the twelve briefs in
planning/modules/briefs/ (commits 6784076 to 0e45f0b). Brief-level
questions (station picks, titles, minutes) stay in each brief's section 10;
only questions that reach past one module are raised here.

Form, as in DECISIONS.md: plain name; what it changes; options with
implications; default; ruling.

Recorded direction (not a decision; given by Patrick on 10/15/2026): module
author is Patrick A. Freeland, with ATNI Climate also listed but not as owner.
Previously cited authors stay as cited. Licensing is set later (see D32). All
twelve briefs carry the author line.

---

## D27. Place-based module architecture

What it changes: whether the module family exists as a build target, where its
source and pages live, which module is authored first, and whether a module
skill is built. Nothing is authored before 10/25/2026 (after the Yakama Tribal
Teachers Workshop, 10/23 and 10/24/2026), and no merge to main 10/21 to
10/24/2026.

It can be ruled whole or in four parts.

### D27a. Adopt the module form
One authored source per module with a single manifest (cc-module/v1): hooks
(socket slide ids), minutes for excerpt and lesson, place and naming review,
outcome / activity / evidence / transfer per grade band, hand twin, data
posture (LIVE, SNAPSHOT, TEACHING MODEL), permission requirement and status,
case items (source, dates, checksum, license), plus one field the briefs
added: author ("Patrick A. Freeland (module author), with ATNI Climate").
Options:
- A. Adopt as written in D27, with the author field. Every brief already
  follows its sections, so each brief becomes the first draft of its
  manifest.
- B. Adopt later, after the pilot is rehearsed by hand.
Default: A.

### D27b. Where module source and pages live (a conflict to rule, not a default to assume)
Three places name a location, and they disagree:
- D27's text: source in modules/m-<river-or-basin>-<topic>/module.md (repo
  root), pages built flat to docs/<id>.html.
- CLAUDE.md, build rule: "source/template.html (and any source/ modules) is
  the editable source."
- The private S2 synthesis (library/_synthesis/place-based-modules.md,
  section 3.1, 10/14/2026): source/modules/<id>/, pages at
  docs/modules/<id>.html.
Options:
- A. D27's text. modules/<id>/ at the root; flat docs/<id>.html.
  Implications: source/build.py (23 lines today, reads only source/) reads a
  second folder; CLAUDE.md's build rule and "Where things are" each gain a
  line; flat pages sit beside index.html, so fonts/ and img/ paths are the
  same as the workshop's and a downloaded docs/ folder still works offline
  one level deep.
- B. source/modules/<id>/module.md; flat docs/<id>.html. Implications:
  matches CLAUDE.md's existing words; the build stays inside source/; the
  flat output keeps A's offline simplicity. Only D27's text changes.
- C. The S2 layout: source/modules/<id>/ and docs/modules/<id>.html.
  Implications: pages one folder down need ../fonts/ and ../img/ paths; a
  separate site folder for modules; two documents (D27 and CLAUDE.md) change.
In every option, a module awaiting a Nation's permission stays in the
git-ignored private/modules/ (private/ is already ignored).
Default: A, as D27's text says. Note: B costs one word in D27 and matches
CLAUDE.md; Claude did not pick it silently.

### D27c. The pilot
Options:
- A. "Missing Is Not Zero" (cluster A, m-columbia-missing-is-not-zero),
  paper-first and authored by hand: invented two-week rain gauge, kinds of
  blank, a neutral siting grid with no real place and no role play. Size S,
  consent C0, no case pack. It carries the rule every other data module
  depends on (a blank is unknown, never zero).
- B. A data module first (cluster C, B, or D): tests the case pack and a
  license record, but needs a capture and opened use terms before anything
  ships (see D31).
Default: A. STOP after its rehearsal.

### D27d. A module skill
Options:
- A. Hand-author the pilot, rehearse it, then decide whether a skill is worth
  building (D27's text). Implication: the second module is also by hand
  unless Patrick rules otherwise after the rehearsal.
- B. Build the skill first from the briefs' shared template. Implication: a
  skill shaped before any module has met a classroom; both Codex reviews
  advised waiting for teacher evidence before the larger builds.
- C. No skill; cc-slide-change and cc-release-check cover modules.
Default: A.

Ruling: PENDING

---

## Premise corrections to pending decisions (read before ruling them)

- D22, listener rename. D22 proposes renaming "Elder listener" and "child
  listener" to "clarity listener" and "relationship listener". Read in
  order, that swaps their jobs: in L2.3 (Grades 6-12 Lessons, step 4) the
  Elder listener checks respect, patience, and honesty (relationship), and
  the child listener raises a hand at any unclear word (clarity). If the
  intent is to keep the jobs, the pairing is Elder listener to relationship
  listener and child listener to clarity listener. (Found by brief H.)
- D22 names only L4.3. Several other seeds put learners in a Nation's,
  council's, or Elder's place; see D28.
- D25, known factual corrections. Briefs E, G, and K add items that D25's
  list does not yet name (see "Findings that wait on D26e" below); D25
  covers live slides, so only the slide items belong there.

---

## D28. Does D22's rule reach every seed, not only L4.3?

What it changes: whether the rule "no learner speaks or acts as a Nation,
council, Elder, or knowledge holder" applies across the pathway, and which
existing lessons and weeks get revised. The briefs found these seeds (each
flagged, none ruled):
1. TCR 201 Week 9: a negotiation simulation where a learner team plays a
   fictional composite Nation, and a mock resolution sprint (briefs A, L).
2. TCR 201 Week 6: a tabletop with learners as a fictional Treaty Tribe's
   council chair and department directors, then a mock council briefing
   (brief K).
3. CCIC 200 Week 4: role-play of a knowledge holder declining a question
   (brief H).
4. L4.1: learners wear "Tribal Nation government" and "Elder or knowledge
   holder" cards, and the government card tugs (brief L).
5. L1.3: "what would a family fishing at a usual and accustomed place want
   this graph to look like?" (brief D).
6. L3.1 Part B: lost fish "voice that hazard", with no exclusion for the
   Treaty fishing station (brief E).
7. L2.1 card 11: an invented grandmother's observation, a stand-in Elder
   voice (brief G); and revision notes S9 listing "an Elder's story" as a
   sortable example (brief G).
Options:
- A. The rule applies pathway-wide. Each item is revised one at a time
  (cultural, per D26a) in a D26e branch draft for Patrick's review; until
  then, modules use the neutral forms the briefs propose (anchored cards,
  role-free analysts, partners declining as themselves).
- B. Modules follow the rule; the curriculum keeps its current lessons until
  a separate review.
- C. Case by case, item by item.
Default: A, decided one item at a time, starting with 1 and 2 (TCR 201,
where whole class periods are built on the role).
Ruling: PENDING

## D29. Scenario generations across the pathway

What it changes: which projection sources modules use and how CCIC 200's
assigned tool is taught beside them. CCIC 200 assigns the Climate Toolbox,
whose future data page (opened 10/15/2026 by brief F) states CMIP5 RCP4.5
and RCP8.5; TCR 201 and the s10 slide use CMIP6 SSP2-4.5 and SSP3-7.0.
Options:
- A. Modules speak CMIP6 SSP2-4.5 and SSP3-7.0; CCIC 200 keeps the Toolbox
  for homelands work with a teacher card ("two generations, two columns";
  an RCP result never sits under an SSP heading).
- B. Move CCIC 200 to a CMIP6 source (a curriculum edit under D26e).
- C. Modules use CMIP5 to match the Toolbox.
Default: A.
Ruling: PENDING

## D30. Student input in modules

What it changes: what any module page keeps after the learner leaves.
Options:
- A. Session memory only in every module, cleared on reload, no export;
  modules adopt D23's ruling for s23 only if it is stricter. The consent
  rehearsal (cluster H) never saves under any ruling.
- B. Follow D23's default (session memory plus an opt-in "Save on this
  device" and a clear button) in every module except H.
Default: A. Modules hold reasons, predictions, and practice lines, not
reflections worth keeping across days.
Ruling: PENDING

## D31. Case packs: use terms opened before anything ships

What it changes: when a data module may merge to main. The briefs found that
several issuers state no terms on the pages opened: NOAA NCEI normals and
GHCN-Daily, Columbia River DART (with a USACE disclaimer of warranties),
NRCS SNOTEL (license page not opened), NCEI Climate at a Glance. USGS states
public domain (opened). The Climate Toolbox shows CC BY 4.0; the Dynamic
Drought Module carries a share-alike community license.
Options:
- A. No case pack ships until each issuer's terms are opened and recorded in
  planning/MEDIA-CREDITS.md; "U.S. government work, presumed public domain"
  stays OPEN until a page says so; Patrick or ATNI staff write to DART before
  any derived DART chart merges (brief E).
- B. Ship on the public-domain presumption for federal agencies and fix later.
Default: A.
Ruling: PENDING

## D32. Repo license, and when it must be set

What it changes: the license on module-made content (invented data, cards,
drawings, practice lines). The repo has no LICENSE file (checked 10/15/2026),
so today nothing in it carries a stated license. Patrick's direction on
10/15/2026: authorship now (Patrick A. Freeland, with ATNI Climate, not as
owner); licensing once it is better established.
Options:
- A. Choose a license before the first module merges to main; until then
  modules are drafted and rehearsed with the author line only.
- B. Choose a license now.
- C. Publish modules without a stated license and choose later.
Default: A. Share-alike or attribution terms of any third-party item a module
uses are honored per item regardless (D31).
Ruling: PENDING

## D33. How neutral-form stations are chosen, and the courtesy notice

What it changes: the C1 rule for data modules (clusters B, C, D, E). The
briefs chose stations and gauges by geography and hydrology only, and could
not verify whether any sits on Tribal or trust land.
Options:
- A. Choose by geography and record only; check land status at capture and
  swap any station on Tribal or trust land; a courtesy notice goes to the
  Nation's office only when a module is used in or near that Nation's
  community, and only Patrick or his designee sends it.
- B. Keep a station on Tribal or trust land with that Nation's confirmation
  (C2).
Default: A.
Ruling: PENDING

## D34. Visible data labels on live slides

What it changes: three live slides show modeled views without a visible
label, which is the rule the modules teach. s04 (the cloud tool) says
"teaching model" only in its notes; s10 places "Today" in the same control
and color ramp as the two futures, with no visible TEACHING MODEL label on
the futures; s20's ripples (including "Decided without consultation") are
unlabeled teaching models.
Options:
- A. Add a visible label on each, after 10/24/2026, through cc-slide-change
  (Phase 1g for s04; Phase 5 for s10; Phase 6 for s20), with ledger rows.
- B. Leave the slides; modules carry the labels.
Default: A, after 10/24/2026. No page work before then.
Ruling: PENDING

---

## Findings that wait on D26e (curriculum drafting, PENDING)

Not decisions; the list a D26e branch draft would start from, each cited in
its brief. curriculum/ was not edited this session.
- L3.3 step 2 explains the drought tool's empty Tribal layers by data tiers;
  the tool's own files call them deployer placeholders "about provenance
  and currency, not secrecy" (brief A, V-A3).
- L1.3, L-open, CCIC 200 Week 7: "2015 had near-normal precipitation" is not
  supported by the press release opened; the paper itself was not opened
  (brief D, F1).
- L3.1: Round 2 "This is what 2015 looked like" ties invented odds to a real
  year; Part A counts days over 20 °C, which is not EPA's 7-day criterion;
  "Bonneville water temperatures" names no station or sensor (brief E).
- L-open and CCIC 200 Week 2: "normals use 30 years" names no issuer or
  period (brief C).
- CCIC 200 C-A1 and Week 3: the drought tool may not list NWS stations
  (local registry read; live site not opened) (brief C).
- CCIC 200 C-A5 example locations include places that need a Nation's
  confirmation (brief F).
- CCIC 200 Framing Worksheet sorts only adaptation or mitigation; Part 3
  teaches three jobs (brief I).
- TCR 201: line 455 SSP selectability unconfirmed; line 444 baseline
  confirmed; line 458 answered (CMIP5 only on the Toolbox page); the Week 4
  worked example's notice or consultation status is an open placeholder
  (brief F). SA4 has two due weeks (brief L). Line 598 repeats an
  unsourced tree carbon figure that the references review corrected only in
  CCIC 200 (brief I).
- L3.2: cooling center key differs from s16 (A versus A and R); wood stove
  key has no reason or source (brief I).
- TCR 201 Template G "Last contact" column is a correspondence record
  (brief L).
- CCIC 200 Week 8 and Assignment 6: absent students are sent to "the online
  NOAA data" (breaks the offline rule); "continuous measurement" since 1958
  is contradicted by the file's own note on the 2022 to 2023 Maunakea
  months; the NOAA file fills missing months, which neither course mentions.
  TCR 201 Lab 1 says the yearly high is in May and the low in September;
  the file shows other months in some years, so "usually" (brief J).

## Cross-module questions from the briefs (defaults in the briefs)

- CCIC 200 Week 7 minutes shared by clusters D and K: default split, D 15
  minutes in Inquiry, K the Application block (briefs D question 3, K
  question 3).
- One card file as the single source for cluster I and s16's neutral cards
  (brief I question 2).
- Module chain wording as the reference for s20's physical links in the
  Phase 6 rebuild (brief K question 2).
- Grade bands listed without a seed: CCIC 200 for D, E, I, and L; TCR 201 for
  H; Grades 6-12 for J (no 6-12 lesson teaches the carbon cycle). SEEDS.md
  now names the proposed seeds for D, E, and H; I, J, and L wait on Patrick
  (brief I section 1, brief J question 1, brief L question 8).
