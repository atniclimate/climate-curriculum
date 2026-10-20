# m-columbia-reading-to-record: One Reading, a Whole Record (working title)

Cluster C. Status: concept brief, planning only (no build before D27).
Module author: Patrick A. Freeland, with ATNI Climate. Licensing to be set later.
Seeds: P1, L-open, L1.2, C-W2, C-W3, C-A1, C-A2, T-M1, s05. Written from SEEDS.md as of commit 6784076.

Location per D27's text (default, PENDING): source in
modules/m-columbia-reading-to-record/module.md, built flat to
docs/m-columbia-reading-to-record.html. Learner-facing wording here is a
placeholder for Patrick's voice pass (VOICE-PASS), not final copy.

## 1. Seeds served and the socket slides

What each seed already asks for, by locator (no seed text is changed):

- P1 (Guiding Document, Part One Key Takeaway, lines 119 to 127): the same gauges that predict tomorrow show patterns over many years. The module makes that a thing learners do.
- L-open (Grades 6-12, lines 91 to 118): step 4 says climate normals use 30 years; the 9-12 differentiation asks learners to label a memory "weather" or "possible pattern" and name the date plus the nearest station's record. The module is where that check happens.
- L1.2 (lines 161 to 197): journal entries become a record; 9-12 compares entries with the nearest official station and discusses 30-year normals. The module gives that comparison an offline form.
- C-W2 (CCIC 200, line 484): "one day of temperature at a local station, then 30 years of the same date." The module is that dataset, frozen and steppable.
- C-W3 (CCIC 200, lines 507 to 529): metadata (who, where, when, how) and comparing class data with the nearest station. The module shows what a missing day and a missing date do to a reading.
- C-A1 (CCIC 200, lines 202 to 214): weekly comparison of one journal entry with an official record; the Week 9 summary asks "What did the official record miss, and what did you miss?"
- C-A2 (CCIC 200, lines 216 to 228): matching official records for visit days; "Missing or messy measurements are fine if explained."
- T-M1 (TCR 201, Week 2, lines 331 to 371): "compared to what?"; a baseline changes the numbers, not the shape. The module offers a station-scale version of Lab 2A as an optional control.
- s05 (source/template.html lines 512 to 571, s05-gauges): "One reading is weather; thirty years of the same readings is climate." Notes call the animations "illustrations, not live readings."

Socket slide: s05-gauges only. The module is reached from s05's speaker
notes or from the s22 index (after D24), never embedded in the deck.

Not in scope: the s05 redesign. The revision notes (S5, lines 148 to 157)
describe a Reading, Record, Pattern, Knowledge, Decision chain for the slide;
that is Phase 4 page work. This module covers Reading, Record, and Pattern on
a classroom page and stops there. It shows no drought declaration and no
decision.

Cross-references by locator only (private, dated 10/14/2026, not policy):
library/_synthesis/place-based-modules.md, section 2.1 row PM-01 and the
PM-01 card; library/_synthesis/curriculum-development.md, section 4.3.

## 2. Learning outcome, activity, observable evidence, transfer

| Band | Outcome | Activity | Observable evidence | Transfer |
|---|---|---|---|---|
| 6-12 (6-8; 9-12) | Tell one reading from a record, using one station's same-date readings across many years | Pick a date; step one reading at a time into a strip of years; place one personal memory or journal reading beside it (9-12 adds "inside the usual range, outside it, or can't tell") | Said, written, or pointed: "One reading tells us ___; the record tells us ___." 9-12: one memory labeled with a reason, or "can't tell" with the missing piece named (date, place, or station gap) | L1.2 journal (ten entries) compared against the same strip; the Opening half-circle memories; L-close |
| CCIC 200 | Compare a personal observation with an official record, carrying metadata, and treat a missing day as missing | Week 2 Application: the 30-year same-date step-through (line 484). Week 3 Inquiry: a metadata check, entering a reading with and without a date | A weekly Weather Journal comparison line: station id, date, issuer, capture date, the student's reading, where it falls, and how many years in the strip are missing | Field Observation Project comparison (C-A2); Week 9 journal summary; Week 6 trend work (cluster F) |
| TCR 201 | State a station-scale number with its baseline, date, and source, and show that a baseline moves the numbers but not the shape | Optional control in Week 2 Lab 2A: switch the strip's reference between two runs of years in the pack and between those and the issuer's normal | One sentence fit for a council packet: value, station, baseline period, issuer, capture date, missing-day count | Climate Signal Brief (T-SA1), Frog's Eye step |
| Workshop | Feel the shift from one reading to a record in a few minutes | 3 to 5 minute excerpt: the facilitator steps from one year to all years; the room answers "one reading, or part of a pattern?" | Hands, voices, or a pointed-at card on the check question; teachers take the printable card set | A teacher runs the full hand twin in class |

Three scales: Frog's Eye is the learner's own memory or journal reading;
Bird's Eye is one station across many years; Moon's Eye is not on this page
(it points to s08 and, for TCR 201, the global records in Module 1).

Assessment grammar follows the courses' own: CCIC 200 Presence, Inquiry,
Application, Reflection; feedback, never a score, on the page.

## 3. The interaction, sketched in words

One screen, top to bottom (a vertical stack at 390px):

1. A label bar, always visible: "SNAPSHOT: NOAA NCEI GHCN-Daily, station
   [agency station name and id], years [first] to [last], captured
   [MM/DD/YYYY], dataset version [as the issuer states it]."
2. A date chooser (month and day). The learner picks the date of a memory,
   a journal entry, or a field visit. Default is a date the teacher sets in
   the case pack; the page never defaults to today.
3. Reading: one card shows that date in one year, for example a daily high
   in °F with °C beside it. Text under it: this is one reading.
4. Record: an "Add the next year" button and an "Add all years" button.
   Each press drops that year's reading into a strip (years along one axis,
   value along the other). A counter reads "[n] of [N] years shown; [m]
   missing." A missing year is drawn on a separate "No reading recorded" rail
   below the axis as a hollow mark with the words, not at zero, and no line
   is ever drawn across it.
5. Pattern: once all years are in, two toggles appear. "Usual range" shades
   the middle half of the recorded years (computed from readings present;
   missing years excluded and counted). "Issuer's normal" draws NOAA NCEI's
   1991 to 2020 daily normal for that station and date, labeled with issuer,
   period, and version, and with a note that the issuer smooths daily
   normals and estimates some missing months; the strip itself fills nothing.
6. My reading: an optional box takes a date and a value (no name, no story,
   no place). A distinct star mark joins the strip. The page answers in
   words: inside the usual range, outside it, or "can't tell", with why
   (no date entered; that year is missing; the date is outside the pack).
   The memory itself stays on the learner's paper.
7. Element switch: high temperature, low temperature, precipitation. On
   precipitation, a measured 0.00 in is a solid mark labeled "measured: dry";
   a trace is labeled "trace"; a missing day stays on the missing rail.
   Three different things, shown three different ways.
8. TCR 201 control (collapsed by default): choose the reference years (for
   example the earliest 15 years in the pack versus the latest 15) and watch
   every mark's height relabel as a difference while the shape stays.

What changes when the learner acts: marks accumulate; the counter and the
missing count update and are announced; the range and normal appear only
after the record is built, so the pattern is earned, not shown first.

## 4. Hand twin

"Thirty cards" (built from the same case pack, so paper and page agree):

- Print one card per year for the chosen date: the year and the reading.
  Years with no reading print as a card that says "No reading recorded" and
  carries no number. The sheet header carries the same SNAPSHOT label.
- Movement (10 minutes): tape a line on the floor marked in degrees.
  Students holding cards stand at their value; missing-card holders stand in
  a marked box off the line, not at zero. The room sees the spread and the
  gaps. A student may set a sticky note for their own memory on the line and
  keeps the note.
- Seated version (10 minutes): cards laid on a desk strip, or the teacher
  reads values aloud while students tally on a printed number line.
- Workshop excerpt (4 minutes): ten cards, one including a missing year;
  one question, "one reading, or part of a pattern?"
- TCR 201 paper control (10 minutes): average the earliest cards, write
  each card's difference from that average, repeat with the latest cards;
  the order of the cards does not change, every number does.
- No power, no internet: the printed cards are the whole lesson.

Ways to perceive: see the marks or cards, hear values read aloud, stand in
the line. Ways to respond: stand, point, say, or write the sentence frame.

## 5. Data

| Dataset | Issuer | Public URL | License | Posture | What the case pack freezes |
|---|---|---|---|---|---|
| Global Historical Climatology Network daily (GHCN-Daily), one station | NOAA NCEI | https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily (opened: "daily updates", rebuilt "each weekend", each update gets "a unique version number") | Not stated on the product page or the readme (both opened); status unknown until checked | SNAPSHOT | The station's daily file for TMAX, TMIN, and PRCP, from 1991 through the last full year at capture; the ghcnd-version.txt string; the station's metadata line; capture date; SHA-256 checksum; the conversion from tenths of °C and tenths of mm |
| GHCN-Daily readme | NOAA NCEI | https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt (opened: "Version 3.35", undated; "missing = -9999") | Not stated (opened) | SNAPSHOT (reference only) | Version line, missing code, units, and flag definitions quoted in the teacher notes; checksum |
| U.S. Climate Normals, daily station normals | NOAA NCEI | https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals (opened: current normals 1991 to 2020, "first released in May 2021 (v1.0.0)"; 23 sites reissued in 2023 as v1.0.1) | Not stated on page (opened) | SNAPSHOT | The station's daily normals for all 366 days, with the version as issued; checksum. If the station has no daily normals, the toggle is absent and says so |
| Today's gauges and journal comparison (DDM; CoCoRaHS; NWS) | ATNI Climate; CoCoRaHS; NWS | DDM link already on s05 (not opened this session) | DDM not checked; CoCoRaHS data policy not opened | LIVE (link out only, optional) | Nothing. Labeled LIVE; the page works without it |
| The learner's own reading | The learner | none | not applicable | none | Nothing. Session memory only, see section 7 |

Missing values: a day with no reading (GHCN's -9999, or a day absent from the
file) is shown as "No reading recorded" on its own rail, counted, announced,
and excluded from the range; it is never drawn at zero, never joined across,
and never interpolated. A value carrying a NOAA quality flag is shown as
"flagged by NOAA", counted, and left out of the range (default; question 7).

## 6. Place

Neutral form: one public federal station in the Columbia Basin, named only
by its agency station name and id, with no Nation named, no reservation
layer, and no place name in a language. Station metadata (latitude,
longitude, elevation) comes from the issuer's station list. The station is
chosen so it is not on Tribal trust land and its agency name does not carry
a Nation's name (question 1).

What a Nation overlay would add, only with that Nation's recorded
confirmation: a Tribal environmental or air quality program's own station
record beside the federal one `[NEEDS TRIBAL CONFIRMATION: host Nation]`;
any weather or season words in that Nation's language
`[NEEDS TRIBAL CONFIRMATION: host Nation]`; any sign, relative, or First
Food tied to a date or a season `[NEEDS TRIBAL CONFIRMATION: host Nation]`.
None of these is drafted here.

Consent level: C0 for the neutral form (public agency data, no Nation
content, no Nation named). An overlay with a Nation's station data is C2
(Nation-governed data used place-specifically); language, seasonal
teachings, or First Foods would be C3. Learners speak only as themselves; no
role is assigned (D22 applies, and nothing here touches it). CCIC 200 lets a
student use weather words from their own language if they choose
(line 210); the page has no field that asks for them and stores none.

Personal memories (L-open) stay with the student: the page asks only for a
date and a value, never what happened or where.

## 7. Access

- Keyboard: Tab order is label bar, date chooser, Add next, Add all, element
  switch, toggles, my reading, Clear. Inside the strip, arrow keys move
  year to year (roving tabindex); Home and End jump to first and last.
- Screen reader: each mark is announced as "[year], [date]: high [n] °F" or
  "[year], [date]: no reading recorded"; the counter is aria-live polite. A
  "Show as table" button gives the same data as a plain table with a
  "missing" cell, not a blank.
- Missing never depends on color: hollow mark, its own rail, and the words.
- Reduced motion: marks appear in place with no drop; nothing loops.
- Load (estimate, not measured): page code 30 to 50 KB plus a case pack of
  about 150 to 400 KB inlined for offline use; one SVG of at most about 40
  marks; no animation loop. Should hold at 4x CPU throttle; confirm in probe.
- 390px: the strip turns vertical (one row per year, value as a bar), with
  44px targets and the missing rail as a labeled row.
- Storage: session memory by default. An opt-in "Save on this device" and a
  "Clear my reading" button mirror D23's default, which is PENDING; this
  module follows whatever D23 rules. No analytics, no network calls.

## 8. Minutes

- Workshop excerpt: 3 to 5 minutes (page or the ten-card twin), per D24's
  default (PENDING).
- Grades 6-12: 20 to 25 minutes as a second-day follow-on to L1.2, or in
  place of L1.2's pair missions (20 to 30 min) when there is no internet;
  5 minutes inside the Opening's 9-12 differentiation.
- CCIC 200: 15 minutes in Week 2 Application (45 to 85 min block); 15 minutes
  in Week 3 Inquiry (95 to 110 min); about 5 minutes per weekly journal
  comparison.
- TCR 201: 10 to 15 minutes as an optional station-scale control inside Lab
  2A (35 to 60 min).
- Hand twin: 10 minutes full; 4 minutes excerpt.

## 9. Facts to verify

Proposed rows in VERIFY.md format. Status stays OPEN; the main session
re-opens each source before CHECKED.

| # | Slide | Claim as written | Status | Source and date checked | Notes |
|---|---|---|---|---|---|
| C-1 | module | NCEI current U.S. Climate Normals are 1991 to 2020, first released May 2021 (v1.0.0); 23 sites reissued 2023 (v1.0.1) | OPEN | https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals (opened 10/15/2026) | Record the chosen station's normals version |
| C-2 | module | NCEI daily normals are smoothed and constrained to monthly normals; missing months were estimated from nearby stations | OPEN | Same page (opened 10/15/2026) | Basis for the toggle's caveat; the page did not describe missing-data handling for daily normals |
| C-3 | module | GHCN-Daily missing code -9999; TMAX and TMIN in tenths of °C; PRCP in tenths of mm | OPEN | https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt, "Version 3.35" (opened 10/15/2026) | Build trap: -9999 must never reach a chart |
| C-4 | module | GHCN-Daily is updated daily and each update has a version number | OPEN | GHCN-Daily product page (opened 10/15/2026) | Freeze the version string in the pack |
| C-5 | module | How GHCN-Daily records trace precipitation | OPEN | readme.txt flag table (not opened for this point) | Needed for the "trace" label |
| C-6 | module | License or use terms for GHCN-Daily and the normals | OPEN | Not stated on the pages opened; NOAA or NCEI data policy page not opened | Needed before a public case pack ships |
| C-7 | L-open line 106; C-W2 line 461 | Climate normals use 30 years | OPEN | WMO climatological standard normals guidance (not opened); NCEI normals page (opened, uses 30-year periods) | Name WMO or NCEI as the issuer when stated |
| C-8 | module | Chosen station id, name, coordinates, elevation, record start | OPEN | ghcnd-stations.txt and the station's NCEI record (not opened) | Depends on question 1 |
| C-9 | C-A1 line 209; C-W3 line 529 | Students can find the nearest NWS station through the DDM | OPEN | DDM station registry, local source I:\dynamic-drought-module\src\config\station-registry.ts (read 10/15/2026; live site not opened) | The registry lists USGS, SNOTEL, SCAN, RAWS, NOAA tides, AgriMet, and CoCoRaHS; no NWS Cooperative or airport station type was found (not verified live) |
| C-10 | module | CoCoRaHS data use terms, if journal comparisons use it | OPEN | CoCoRaHS data policy (not opened) | references section 4 says site content and data have separate terms |

## 10. Open questions for Patrick

1. Which station? Default: one long-record federal station in the
   mid-Columbia with a near-complete 1991 to 2020 run, off Tribal trust land,
   whose agency name carries no Nation's name; Patrick picks.
2. Which reading first? Default: daily high temperature; precipitation second,
   because zero versus trace versus missing teaches best there.
3. How many years? Default: 1991 through the last full year at capture, so
   the normals period and recent years sit on one strip.
4. Show the issuer's normal line? Default: yes, only after the record is
   built, labeled with issuer, period, version, and the smoothing caveat.
5. Exact date or a few days either side? Default: exact date only.
6. Units? Default: °F first with °C beside; inches with mm beside.
7. NOAA-flagged values? Default: shown as "flagged by NOAA", counted, left
   out of the range.
8. Does the ten-card twin serve D21's default kit ("reading versus record"
   demonstration)? Default: no assumption; D21 is PENDING, and there is no
   merge to main from 10/21 to 10/24/2026.
9. Working title for the voice pass? Default: "One Reading, a Whole Record".

## 11. Build size

M: one screen, no new engine, but it needs a dated, checksummed station case
pack (and a license check) before anything ships.
