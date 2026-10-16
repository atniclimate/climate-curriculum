# Launch prompt: TCU template build-out (CCIC 200 and TCR 201 for every AIHEC TCU)

How to start the session: open Claude Code in I:\climate-curriculum and send
"Read planning/tcu/LAUNCH-TCU-TEMPLATES.md and go." Everything below is the
prompt. Written 10/15/2026 from Patrick's request in the module planning
session (branch dev/revisions-2026-10, tip 2f415f3).

```text
You are working in I:\climate-curriculum (local clone of
github.com/atniclimate/climate-curriculum). I am Patrick. This session builds
the TCU template versions of the Tribal College pathway: CCIC 200 (Climate
Change in Indian Country) and TCR 201 (Tribal Climate Resilience), one
template set per AIHEC Tribal College and University and per NWIC extended
campus site, 40 sites in all (Appendix A). Each site gets a deep-dive place
module, a scout-built resource packet, launchable .html presentations, .pptx
templates, and an uploadable minisite. This is a large build with room for
creativity on the first run; I chose all 40 deep dives in this run.

=== READ THIS FIRST (read only, in this order, all binding) ===
  1. CLAUDE.md (house style, design system, engineering rules, guardrails)
  2. planning/HANDOFF.md (top entry), planning/DECISIONS.md (PENDING means
     unruled; D22, D23, D26, D27 bear on this work), planning/modules/PACKET-D27.md
     (proposed D28 to D34: their defaults are not rulings)
  3. curriculum/CCIC-200_Climate_Change_in_Indian_Country_Syllabus.md and
     curriculum/TCR-201_Tribal_Climate_Resilience_Syllabus.md (the source of
     the shared core), curriculum/Understanding-a-Climate-of-Change_Guiding-Document.md
     (the Four Questions spine)
  4. planning/modules/SEEDS.md and two briefs as worked examples of the
     neutral-form and consent conventions:
     planning/modules/briefs/m-columbia-missing-is-not-zero.md and
     planning/modules/briefs/m-columbia-now-and-ahead.md
  5. H:\NEXUS\AGENTS.md (the archive's own rules; read-only archive)
  6. source/build.py and the top of source/template.html (presenter keys and
     the single-file offline pattern to reuse); do not edit either

=== PRECONDITIONS ===
- Create branch dev/tcu-templates-2026-10 from dev/revisions-2026-10 at
  2f415f3 (or its newer tip; if newer, read the new commits first). Never
  push, never merge. Work only on that branch.
- `python source/build.py --check` passes before you start and at the end.
  This session never changes source/, docs/, or curriculum/; the check
  proves the workshop is untouched.
- The Yakama Tribal Teachers Workshop is 10/23 and 10/24/2026; nothing here
  touches the workshop page, and nothing merges to main.

=== AUTHORITY AND CONTRACT STATE ===
My direct request on 10/15/2026 authorizes, and only authorizes:
- Creating tcu/ at the repo root for the SHARED, PUBLIC parts: tcu/README.md,
  tcu/DESIGN.md, tcu/registry.yaml (the 40 sites, public facts only),
  tcu/core/ccic-200/ and tcu/core/tcr-201/ (template syllabi with slots),
  tcu/engine/ (build and check scripts), tcu/templates/ (minisite skeleton,
  presentation template, .pptx template). Commit these.
- Creating private/tcu/ (private/ is already git-ignored) for EVERYTHING
  site-specific: scout packets, the NEXUS index, data case packs, deep
  dives, built minisites, built .pptx files, review notes, and the run
  ledger. Never commit anything under private/.
- Drafting curriculum content in tcu/ derived from curriculum/. curriculum/
  itself stays unedited (D26e is PENDING).
- Running Workflow scripts for the scout and deep-dive fan-out (Execution
  order, steps 5, 7, 8), each workflow under 50 agents.
Every deep dive and packet is DRAFT FOR TCU REVIEW. It stays in private/
until the TCU (and, where it applies, the chartering Nation) has reviewed
it; promotion to the public tree is mine to decide later.
You may not: rule on any D-item; edit CLAUDE.md, curriculum/, source/,
docs/, or planning/DECISIONS.md; contact any TCU, Nation, or person; push.
Stop conditions even under this authorization: a needed file sits outside
the paths above; a source would require logging in or paying; a request
would send private text to a public service; anything that would speak for
a Nation, a TCU, or a person.

Content rules (binding on every agent):
- An institution's own public name is used as its name, in its own folder.
  No page speaks for the TCU or for its chartering Nation, and no learner
  speaks or acts as a Nation, council, Elder, or knowledge holder (the D22
  rule; analytic roles and quoting a Nation's own public words are fine).
- Public ecology and public agency data (ecoregions, watersheds, species
  lists, climate records, projections, hazards) are written in full. Any
  cultural relationship to a species, place, food, or season, any place name
  in a language, and any story or teaching is left as
  `[NEEDS TRIBAL CONFIRMATION: <Nation>]`. Where local expertise belongs,
  write `[LOCAL EXPERT: TCU faculty or knowledge holder]`; each TCU builds its
  own ground-truthed lessons from local experts and knowledge holders, and
  the template's job is to make room for that, not to fill it.
- Every data view is labeled LIVE, SNAPSHOT, or TEACHING MODEL. Live data
  never runs in class; each site carries a dated, checksummed case pack.
  Absence of data is unknown, never zero.
- Never extract, quote, or summarize: anything under NEXUS Emails,
  Financial, JobApplications, or HR; student files, rosters, exams with
  responses, or registration data; contact lists, including
  H:\raw-data\bia-tribal-leaders-directory; Patrick's own personal and
  education records; planning/discovery-2026-10-12/file-locations.private.jsonl
  or sealed manifests. Third-party work in NEXUS: digest and short excerpts
  only, with its author credited, kept in private/.
- Web search queries are built only from public seeds (the institution's
  public name and town, public program names). Never put NEXUS-derived text,
  people's names from private files, or internal project names into a web
  query or fetch.
- Module author on every authored page: "Patrick A. Freeland (module
  author), with ATNI Climate". ATNI Climate is never called owner. Previously
  cited authors (Freeland and Jones; Steve Robinson; agency issuers; third
  parties) stay as cited. Licensing is set later (proposed D32); no license
  text is added.
- Tools: TCR 201 may draw on the TCR Policy Scanner (I:\tcr-policy-scanner)
  and Policy Sentinel (I:\policy-sentinel) for tool facts and methods only,
  read from their own README and docs, read only. Do not copy any
  per-Nation Scanner output, rank, or packet into anything. 201 teaches hand
  first, then tools; tools support and never replace Tribal decision-making.
- CCIC 200 is not a technical or data-science course. It is an early primer:
  weather and climate, local impacts, ways of knowing, and sovereignty
  through InterTribal and international policy, so students reach TCR 201
  ready to act. Keep the shared fundamentals the same at every site.

=== CORRECTIONS TO THE PLAN YOU WILL MEET ===
- curriculum-specialist is scoped to lesson design and review, not web
  research. Scouts run as Workflow agents with the scout charter in step 5;
  curriculum-specialist writes and reviews deep-dive lessons only.
- Patrick's TCU list (Appendix A) may not match AIHEC's current member list
  (for example, it may be missing Salish Kootenai College and Blackfeet
  Community College in Montana; not verified). Scouts check AIHEC's public
  member page and report differences in private/tcu/LEDGER.md. Do not add
  or drop a site; Patrick decides.
- Appendix B gives two addresses for the Nisqually site, none for
  Muckleshoot, and "including the Kamiah Center" for Nez Perce. Record them
  as given, marked verify; the scouts confirm from NWIC's public pages.
- Many campuses sit outside any AIANNH area (for example Haskell in
  Lawrence, IAIA in Santa Fe, SIPI in Albuquerque, United Tribes in
  Bismarck, California Tribal College in Woodland). Climate unit rule:
  use the AIANNH area in H:\raw-data\climate-projections\cache that contains
  the campus; if none contains it, use the campus county (LOCA2 under
  H:\raw-data\loca2 if that county exists there, otherwise record "no
  projection in raw-data" as unknown). Record the unit and why in the case
  pack. FEMA NRI in raw-data covers only some states; a missing state is
  unknown. Some raw-data file names contain an em dash (for example the
  Navajo Nation agency slugs); match on them as they are, but never print
  that character on a page or in a committed file.
- The D27 module architecture is PENDING. tcu/ is this build's own layout;
  if D27b later moves module source, tcu/ moves with it. Do not presume D27.

=== EXECUTION ORDER ===
Each step ends in a commit (public tcu/ files) or a written file under
private/tcu/ before the next step starts. Append one line per step to
private/tcu/LEDGER.md.

1. Orient and registry (main session). Write tcu/registry.yaml: for all 40
   sites, slug, public name exactly as Appendix A or B gives it (keep its
   diacritics), town, state, kind (TCU or NWIC site), address if given,
   campus coordinates if a public source gives them (else unknown), climate
   unit per the rule above, and status "draft". Commit: "TCU templates:
   site registry".

2. Template system design (main session). Write tcu/DESIGN.md: the shared
   core versus local slots; the slot list (institution, place, ecoregion,
   watershed, relatives of that place as species, climate profile, hazards,
   shared case and local case, local expert and knowledge holder slots,
   InterTribal and international policy primer); the four-part assessment
   grammar from Patrick's syllabi (Presence / Application / Inquiry /
   Reflection, and Activity / Reflection / Check for Understanding /
   Completion; confirm both against the NEXUS syllabi before using them);
   the Frog's Eye, Bird's Eye, Moon's Eye scales; file layout; what is
   public and what stays private; how a TCU edits and rebuilds its own
   minisite. Be inventive here: this is the design the 40 sites repeat.
   Commit: "TCU templates: design".

3. Shared core (main session, curriculum-specialist in design mode for the
   lesson text). tcu/core/ccic-200/ and tcu/core/tcr-201/: template
   syllabi and week-by-week plans in Markdown with {{slots}}, derived from
   curriculum/ without editing it. The Columbia River case becomes the
   shared case slot beside a local case slot. 200 carries the sovereignty
   primer; 201 carries adaptation, mitigation, resilience, and policy
   action with hand-first tool labs. Commit: "TCU templates: shared core".

4. Engine and templates (main session). tcu/engine/: a build script that
   turns core plus one site's private files into (a) one single-file
   offline .html presentation per course, reusing the workshop's presenter
   keys (arrows or Space move, N notes, T clock, H highlight); (b) a
   minisite (index, 200, 201, lesson pages, resource packet, place profile,
   case pack credits) with relative links only, no network calls, fonts
   copied from docs/fonts, working from file:// and any static host; (c) a
   zip per site ready to upload; (d) one .pptx per course from
   tcu/templates/pptx/ via python-pptx (note in the template that the ATNI
   fonts fall back if not installed). A check script fails on an em dash,
   any external URL loaded by a page, missing alt text, an unlabeled data
   view, or a case-pack file without its meta.json. Build the neutral
   template example into private/tcu/_example/ and pass the check. Use the
   ATNI design system only; no TCU logos or new palettes (open question).
   Commit: "TCU templates: engine and templates".

5. Scouts and the NEXUS index (fan-out, read only on sources; writes only
   under private/tcu/).
   a. One NEXUS indexer (a single agent): private/tcu/_nexus-index.md, a
      locator-first index of NEXUS material by TCU, AIHEC, IPCCWG, Sensing
      the Earth, and Patrick's syllabi, honoring H:\NEXUS\AGENTS.md and the
      exclusions above. Locators and short digests, no bulk text.
   b. One web scout per site (Workflow, regional waves of at most 12):
      writes private/tcu/<slug>/packet/scout.md covering the TCU's history
      of climate and environmental programs, degree programs, partnering
      agencies and organizations, related research and publications,
      regional climate science centers and Extension ties, and the public
      climate or hazard plans of the place (link and cite only; a Nation's
      plan is noted, not summarized). Each item: source URL, issuer, date
      as the source states it, "opened MM/DD/YYYY", and a one-line note.
      Unopened leads are listed as leads, never as facts.
   c. Haskell Indian Nations University gets four extra scouts (Appendix C),
      run in the first wave.
   Scout charter (paste into each scout agent): its site slug, its one
   output path, the content rules above, the web-query rule, and "public
   sources only; quote short; cite everything; unknown is an answer".

6. Data profiles (main session, scripted). For each site, read H:\raw-data
   read only (climate-projections cache, loca2, fema-nri, census-tiger,
   usgs-gnis, slr-derived and alaska-context where they apply) and write
   private/tcu/<slug>/data/: SNAPSHOT case-pack files, each with a meta.json
   (source, issuer, unit, scenarios, baseline and future windows as the
   file states them, captured_at, SHA-256, license as stated or "not
   stated"). Public ecoregion, watershed, and species sources fetched for
   the profile go in the same pack with their terms recorded.

7. Pilot sites (Workflow or sequential; then a review gate). Full deep
   dives and built minisites for three pilots: Haskell Indian Nations
   University (with the Appendix C timeline), Northwest Indian College's
   Bellingham campus, and the NWIC Nez Perce site (an interior contrast).
   One curriculum-specialist (design mode) per pilot writes
   private/tcu/<slug>/deep-dive/ (place profile: geography, region,
   ecoregion, environment, plant and animal relatives as public species
   lists, climate profile from step 6, hazards; and the 200 and 201 local
   lesson slots with sockets to the shared weeks). Then a fresh-context
   curriculum-specialist in review mode reads the three pilots once and
   writes private/tcu/_review/pilots.md. Fix the core, engine, or templates
   from that review before fanning out; commit those fixes.

8. Fan-out (Workflow, regional waves; each workflow under 50 agents). For
   the other 37 sites, pipeline per site: deep-dive writer
   (curriculum-specialist, design mode) after that site's scout packet and
   data profile exist. The main session builds each site with the engine
   and runs the check. After each wave, one fresh-context review of one
   sampled site per region, written to private/tcu/_review/wave-<n>.md;
   note defects for the next wave, do not re-run a writer to polish.

9. Close (main session). Build all 40, run the check on all, re-run
   `python source/build.py --check`. Write tcu/README.md (how a TCU uses,
   edits, rebuilds, and uploads its minisite; what is shared and what is
   theirs) and private/tcu/STATUS.md (per site: built, checked, gaps,
   [NEEDS TRIBAL CONFIRMATION] count, open leads). HANDOFF.md entry; PLAN.md
   gains a "TCU templates" section with every site [hold] for TCU review.
   Commit the public files. STOP and report.

=== DATE DISCIPLINE ===
Today's date is never a default. Dates come from the record: an issuer's
own date, a file's stated creation or version date, a commit timestamp
(`git show -s --format=%cI <sha>`), or the moment the run itself opened a
page or captured a file (written "opened MM/DD/YYYY" or captured_at). A
source with no date is written "undated". Historical dates in the Haskell
timeline come only from sources that state them. Never write "verify at
time of teaching" as if it were verified.

=== RUNNING LONG ===
private/tcu/LEDGER.md and the commit log are the ledger. If context is
compacted, recover from them plus tcu/registry.yaml and STATUS.md, not by
re-reading curriculum/ or NEXUS. Build and check output go to the
scratchpad; quote only the failing line. Trust each agent's report after
the wave review; verify a claim only when a check contradicts it.

=== DELEGATION AND EXCLUSIONS ===
Allowed: Workflow scripts for steps 5, 7, and 8 (scouts, NEXUS indexer,
deep-dive writers, reviewers); curriculum-specialist for lesson design and
review. Out of scope by name: the project stewards (tcr-policy-scanner,
dynamic-drought-module, geobase, rstep, and the others; read their repos
only for a tool fact, never edit), feature-dev agents, code-review agents,
Codex, Plan. No subagent spawns another.

=== COMMUNICATION ===
Report by site name and step, never by hash alone. At the STOP: what was
built by folder; a table of the 40 sites (built, checked, gaps, open
confirmations); what waits on me; the next step; and the git commands to
review the branch and push it, explaining each and its expected output.
House style everywhere: no em dash, Oxford comma, MM/DD/YYYY, capitalized
Indigenous, Tribal, Nations, Elder, Knowledge, First Foods; relatives, not
resources; no "stakeholders"; Patrick's own first-person voice stays
`[PERSONAL VOICE: Patrick writes this]`.

=== DELIVERABLE ===
Public and committed on dev/tcu-templates-2026-10: tcu/README.md,
tcu/DESIGN.md, tcu/registry.yaml, tcu/core/, tcu/engine/, tcu/templates/,
HANDOFF and PLAN updates. Private, never committed: private/tcu/ with the
NEXUS index, 40 scout packets plus Haskell's four, 40 data case packs, 40
deep dives, 40 built minisites with zips and .pptx files, reviews, LEDGER,
and STATUS. No push.
```

## Appendix A. AIHEC Tribal Colleges and Universities (as Patrick gave them, 10/15/2026)

Alaska: Iḷisaġvik College, Utqiaġvik (Barrow), AK.
Arizona: Diné College, Tsaile, AZ; Tohono Oʼodham Community College, Sells, AZ.
Kansas: Haskell Indian Nations University, Lawrence, KS.
Michigan: Bay Mills Community College, Brimley, MI; Keweenaw Bay Ojibwa
Community College, Baraga, MI; Saginaw Chippewa Tribal College, Mount
Pleasant, MI.
Minnesota: Fond du Lac Tribal and Community College, Cloquet, MN; Leech Lake
Tribal College, Cass Lake, MN; White Earth Tribal and Community College,
Mahnomen, MN.
Montana: Aaniiih Nakoda College (formerly Fort Belknap College), Blaine
County / Harlem, MT; Chief Dull Knife College, Lame Deer, MT; Fort Peck
Community College, Poplar, MT; Little Big Horn College, Crow Agency, MT;
Stone Child College, Box Elder, MT.
Nebraska: Little Priest Tribal College, Winnebago, NE; Nebraska Indian
Community College, Macy, NE.
New Mexico: Institute of American Indian Arts (IAIA), Santa Fe, NM; Navajo
Technical University (formerly Navajo Technical College), Crownpoint, NM;
Southwestern Indian Polytechnic Institute (SIPI), Albuquerque, NM.
North Dakota: Cankdeska Cikana Community College, Fort Totten, ND; Nueta
Hidatsa Sahnish College (formerly Three Tribes College), New Town, ND;
Sitting Bull College, Fort Yates, ND; Turtle Mountain Community College,
Belcourt, ND; United Tribes Technical College, Bismarck, ND.
Oklahoma: College of the Muscogee Nation, Okmulgee, OK.
South Dakota: Oglala Lakota College, Kyle, SD; Sinte Gleska University,
Mission, SD; Sisseton Wahpeton College, Sisseton, SD; Ihanktonwan Community
College, Marty, SD; Lower Brule Community College, Lower Brule, SD.
Washington: Northwest Indian College, Bellingham, WA.
Wisconsin: College of Menominee Nation, Keshena and Green Bay, WI; Lac
Courte Oreilles Ojibwa Community College, Hayward, WI.
Other / system partners and initiatives: California Tribal College,
Woodland, CA (hosted via Woodland Community College).

That is 35 institutions.

## Appendix B. NWIC extended campus sites (as Patrick gave them, 10/15/2026)

- Tulalip Site: 7707 36th Ave NW, Tulalip, WA 98271
- Nisqually Site: Nisqually Indian Tribe-Education Building, 12503 Yelm
  Highway S.E. / 4820 She-Nah-Num Dr. SE, Olympia, WA 98513 (two addresses
  given; verify)
- Port Gamble S'Klallam Site: 31912 Little Boston Rd NE, Kingston, WA 98346
- Muckleshoot Site: located on the Muckleshoot Reservation (no address given;
  verify)
- Nez Perce Site: located in Idaho, including the Kamiah Center at 401 Idaho
  Street, Kamiah, ID 83536

Five sites; with Appendix A, 40 in all.

## Appendix C. Haskell Indian Nations University: the wide net

Haskell has a rich InterTribal tradition and a long record of climate work
(Patrick's request names Dr. Dan Wildcat, the Indigenous Peoples Climate
Change Working Group, and other initiatives over the years). Everything
below is a lead for the scouts to verify from sources they open, not a
fact this prompt asserts.

Four extra scouts, each writing one file under private/tcu/haskell/packet/:
- H1 wetlands-and-wpo.md: the wetlands south of campus and the Wakarusa
  River; the Wetlands Preservation Organization (its own public words and
  history); the federal and state push for the bypass highway (the South
  Lawrence Trafficway) through the wetlands, the resistance, the legal and
  review record, and the outcome; how Haskell continued to use the wetlands
  afterward to teach students about important species.
- H2 land-and-water-over-time.md: how the wetlands and the Wakarusa
  changed from Haskell's founding to now, from public-domain or openly
  licensed sources only (historic USGS topographic maps, aerial imagery,
  land survey plats, agency reports), each with its date and license; the
  species of the wetlands from public lists, with any cultural relationship
  left as a confirmation mark.
- H3 climate-initiatives.md: Dr. Dan Wildcat's public work, the Indigenous
  Peoples Climate Change Working Group, Haskell environmental and climate
  programs, summer research programs, partnerships with agencies and
  universities, and related research, all from public sources; NEXUS
  material appears only by locator in the NEXUS index, never in a query.
- H4 institutional-history.md: Haskell's founding and history as it bears
  on the land and the wetlands, from Haskell's own publications and public
  archives. Boarding-school history is handled with care: plain, sourced,
  no speculation, and a support-resource line on any page that carries it.

Interactive timeline (Haskell minisite, one page, built by the engine):
Haskell's founding, then how the wetlands and the Wakarusa changed over
time, the WPO resistance and the bypass highway, and Haskell's teaching
use of the wetlands since. Each event: date as its source states it,
source, image credit and license; a map strip comparing dated public maps
where licenses allow; keyboard path, screen-reader text, a reduced-motion
form, and a plain list view at 390px. Everything is DRAFT FOR TCU REVIEW,
quotes WPO and Haskell in their own public words, and never speaks for
either.
