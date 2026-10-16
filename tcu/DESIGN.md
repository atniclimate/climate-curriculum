# TCU Templates: Design

How one shared pathway (CCIC 200, Climate Change in Indian Country, and TCR
201, Tribal Climate Resilience) becomes a template set for each Tribal College
and University (TCU) and each Northwest Indian College (NWIC) extended campus
site, 40 sites in all (tcu/registry.yaml).

Module author: Patrick A. Freeland (module author), with ATNI Climate.
Built on *Understanding a Climate of Change*, by Patrick Freeland and Cayla
Jones; Steve Robinson's *Climate Change and the Tribes: Columbia River Edition*
(draft); and NESC 215, Climate Change in Indian Country, Northwest Indian
College. Licensing is set later; no license text is added here.

Status: DRAFT. Written 10/15/2026 on branch dev/tcu-templates-2026-10. The
place-based module architecture (D27) is PENDING; tcu/ is this build's own
layout and moves with D27 if D27b moves module source.

---

## 1. The idea in one paragraph

Every site teaches the same two courses with the same spine, the same key
lessons, and the same respect rules. What changes from site to site is the
ground under the students' feet: the campus, its water, its ecoregion and
watershed, its plant and animal relatives, its climate record and projections,
its hazards, its local case, and above all the local experts and knowledge
holders who teach there. The template's job is to make room for that local
teaching, not to fill it. So every page is built from two layers: a **shared
core** that is the same everywhere, and **local slots** that each TCU fills, or
leaves visibly open, with its own people. Nothing is silently filled, and
nothing local is invented.

## 2. Shared core and local slots

| Layer | What it holds | Who writes it | Where it lives |
|---|---|---|---|
| Shared core | Course arcs, key lessons and takeaways, session shapes, hands-on activities, assignments, rubrics, the shared case (Columbia River Basin), the sovereignty primer, respect and data care rules | Derived from curriculum/ (never edited there) | tcu/core/ (public) |
| Fact slots | Public facts about the institution and place: name, town, county, coordinates, ecoregion, watershed, climate unit, public species lists, public hazard data, public plans (link and cite only) | Registry, scouts, and data profiles; checked by the TCU | private/tcu/<slug>/ until TCU review |
| Local lesson sockets | The place-based part of each week: a field site, a local record, the local case, local relatives | Deep-dive draft, then the TCU's own faculty | private/tcu/<slug>/deep-dive/ |
| Local expert slots | Teaching that belongs to local experts and knowledge holders | Only the TCU, through its own protocols | Marked `[LOCAL EXPERT: TCU faculty or knowledge holder]`, never filled by the template |
| Confirmation marks | Any cultural relationship to a species, place, food, or season; any place name in a language; any story or teaching | Only that Nation | Marked `[NEEDS TRIBAL CONFIRMATION: <Nation>]`, never filled by the template |

The shared fundamentals are the same at every site. A site may add local
lessons through its sockets; it does not rewrite the shared weeks. If a TCU
wants a different shared week, that is a change to the core, proposed to
Patrick, so all sites can benefit.

## 3. Markers

Every marker is visible on the page and in the deck, styled so a reader can
tell at a glance what kind of gap it is. The check script counts them.

| Marker | Meaning | Shown as |
|---|---|---|
| `{{slot.path}}` | A fact slot. The engine fills it from the site's `site.yaml`. | The value. If missing: a hatched grey box reading "unknown: slot.path" (never blank, never zero) |
| `{{socket:<course>/<week>/<id>}}` | A local lesson socket (section 5) | The site's local lesson, or an open "Local lesson slot" box with the socket's purpose |
| `[LOCAL EXPERT: TCU faculty or knowledge holder]` | Room for local teaching | Water-blue outlined box with the words "Local expert" |
| `[NEEDS TRIBAL CONFIRMATION: <Nation>]` | Only that Nation can supply or approve this | Magenta outlined box with the Nation's name as the institution or source publicly gives it, or "the Nation(s) whose homelands the campus is on" when no public source names them |
| `[TCU REVIEW: <institution>]` | The TCU itself must review or choose this (a field site on institution land, a protocol path). A TCU is not a Nation: never put an institution in a confirmation mark | Water-blue outlined box with the words "TCU review" |
| `[PLACEHOLDER: ...]` | The institution or instructor supplies it (course number, honoraria, policies) | Grey outlined box |
| `[INSTRUCTOR SELECTS]` | A reading slot: the kind of source is described; the instructor chooses | Grey outlined box |
| `[PERSONAL VOICE: Patrick writes this]` | Patrick's own first-person voice | Red outlined box |
| `[verify]` | A detail to confirm before teaching | Small red tag; listed in tcu/core/verify.md |

Rules for markers:
- A marker is never replaced by guessed content. A TCU replaces it only with
  its own words, and a confirmation mark only with the Nation's recorded
  confirmation.
- An unknown fact is "unknown", with how one would find out. Absence of data
  is unknown, never zero.
- Markers stay in English; a TCU may add its own language with that Nation's
  permission.

## 4. Two assessment grammars, one week

Both grammars come from Patrick's own course syllabi and were confirmed
against the originals on 10/15/2026 (locators in the private NEXUS index).

1. **Session shape (NESC 215, Northwest Indian College):** "Presence,
   Application (Assignments), Inquiry, & Reflection." Every class session
   moves through these four modules. Presence is showing up for each other;
   Application is hands-on work; Inquiry is questions that lead to more
   questions; Reflection is writing or speaking about what shifted.
2. **Module record (College of the Muscogee Nation course syllabi, 2022 and
   2023):** each module "consists of four parts": attending the in-class
   lecture or presentation, an in-class Check for Understanding, a module
   assignment, and a reflection, 25 points each, 100 points per module.

The launch prompt names the second grammar "Activity / Reflection / Check for
Understanding / Completion". The syllabi's own words are used here. The
closest reading of the shorthand: Activity is the module assignment, and
Completion is credit for attending the lecture or presentation. Patrick
confirms or corrects this reading.

How they fit together on every week page:

| Session shape (time) | Module record (evidence) | What the week page carries |
|---|---|---|
| Presence | Attending the lecture or presentation | Opening, guest or Elder slot, going outside |
| Inquiry | Check for Understanding | Key lesson; three short Check for Understanding items, answered in class, said, drawn, or written |
| Application | Module assignment | The hands-on activity and the assignment step due this week |
| Reflection | Reflection | The week's reflection prompt (NESC 215 prompts kept) and one "say it plain" line: the week's idea in words both an Elder and a child could understand |

Grading stays with each course's syllabus weights (tcu/core/*/syllabus.md). A
TCU that grades by module may use the 25-25-25-25 record instead; the week
pages carry everything either way needs. Checks for Understanding are
feedback first: a wrong answer is a teaching moment, not a penalty.

## 5. Sockets: where the shared week meets the place

Each shared week names its sockets in its front matter: an id, a purpose, the
eye it works at, and its consent level. A site's deep dive fills a socket with
a section headed `## socket: <week>/<id>`. The engine places the section where
the week calls `{{socket:...}}`. An unfilled socket stays visible as an open
invitation to local experts.

Starter sockets (the core may refine them; the week files are the authority):

| Course | Week | Socket | Purpose |
|---|---|---|---|
| CCIC 200 | 1 | land-and-water | Where this course meets: the campus, its nearest water, and the acknowledgment that only the Nation writes or approves |
| CCIC 200 | 2 | local-weather | What the weather journal will see here; the nearest public station, read by hand |
| CCIC 200 | 3 | field-site | Candidate public field sites for the Field Observation Project; never a culturally sensitive place |
| CCIC 200 | 4 | right-path-in | How a student finds the right path to a knowledge holder at this TCU (protocol, honoraria); local expert slot |
| CCIC 200 | 5 | relatives | Plant and animal relatives of this place from public species lists; any cultural relationship stays a confirmation mark |
| CCIC 200 | 6 | climate-profile | The site's case pack: projections for the climate unit, labeled, with "projection, not a prediction" |
| CCIC 200 | 7 | hazards | The hazards of this place from public data and public plans (link and cite only) |
| CCIC 200 | 8 | carbon-here | Where carbon moves on this land: public land cover, forests, soils, energy; local mitigation examples from public sources |
| CCIC 200 | 9 | local-case | The local case: a public, place-based climate story analyzed for exposure, sensitivity, and adaptive capacity |
| CCIC 200 | 10 | carry-forward | Who the final products are shared with locally; local expert slot |
| TCR 201 | 1 | plan-inventory | Public plans of the place: a Nation's plan is noted and linked, not summarized; county and state plans named |
| TCR 201 | 2 | heat-here | Optional: how added heat reaches this place's land and water, from the case pack |
| TCR 201 | 3 | regional-signal | The regional climate science partners (climate adaptation science center, Extension, state climatologist) as public sources |
| TCR 201 | 4 | projection-card | The site's projection card (Template I form) from the case pack |
| TCR 201 | 5 | observed-record | The observed record: public stations and monitors, captured as SNAPSHOT |
| TCR 201 | 6 | exposure | Infrastructure and hazard exposure from public data |
| TCR 201 | 7 | funding-landscape | Public programs active in the region, each a lead until verified this term |
| TCR 201 | 8 | land-and-jurisdiction | Land tenure and governance from public records; ceded lands and usual and accustomed areas only as the Nation describes them |
| TCR 201 | 9 | coordination-web | The jurisdictions, InterTribal organizations, and partners an action here would touch |
| TCR 201 | 10 | capstone-audience | Who hears the capstone; local expert slot |

## 6. The three eyes

Every lesson page and every place profile is organized by scale, using the
series' language:

- **Frog's Eye:** up close, at the water. The campus, a creek or shoreline, a
  rain gauge, a field site, what a person can see, hear, and measure on foot.
- **Bird's Eye:** above the land. The watershed and ecoregion, the county and
  the climate unit, the hazards, the plans, and the partners.
- **Moon's Eye:** the whole planet. Global records, satellites, and the large
  patterns that reach this place (for example, Arctic warming, El Niño and La
  Niña, the jet stream, the monsoon, Great Lakes ice).

Each week names the eye or eyes it works at, so a student always knows the
scale of the evidence in front of them. Every eye has a blank it cannot see
past, and the pages say so.

## 7. The slot list

The fact slots each site carries in `private/tcu/<slug>/site.yaml` (template:
tcu/templates/site/site.yaml). Every slot holds a value with its source, or
the word unknown.

1. **Institution:** public name as the institution gives it, town, state,
   kind (TCU or NWIC site), public web address (opened date), course numbers
   (`[PLACEHOLDER]`), and any chartering statement only as the institution
   publicly states it, cited. No page speaks for the TCU or its chartering
   Nation.
2. **Place:** county, coordinates (or unknown), and whose homelands the campus
   is on, as `[NEEDS TRIBAL CONFIRMATION: <Nation>]` unless the institution's
   own public words state it (cited).
3. **Ecoregion:** EPA Level III and Level IV ecoregion at the campus point.
4. **Watershed:** USGS Watershed Boundary Dataset units (HUC8, HUC10, HUC12)
   at the campus point.
5. **Relatives of the place:** public species lists by group (plants, birds,
   mammals, fish, amphibians and reptiles, insects), each list with its source
   and terms. A species list is not a list of relationships: any cultural
   relationship stays a confirmation mark.
6. **Climate profile:** the case pack's SNAPSHOT views for the climate unit
   (tcu/registry.yaml), or "no projection in raw-data" with public leads.
7. **Hazards:** public hazard data (FEMA National Risk Index where captured)
   and public hazard plans, link and cite only.
8. **Shared case and local case:** the shared case is the Columbia River
   Basin, as in the curriculum. The local case is a public, place-based climate
   story near campus, written from public agency sources, never speaking for a
   Nation.
9. **Local expert and knowledge holder slots:** the marked boxes in section 3.
10. **InterTribal and international policy primer:** the regional InterTribal
    organizations and national bodies the region's Nations publicly work
    through, named from their own public pages, plus the shared international
    layer (section 8).

## 8. The sovereignty primer (CCIC 200)

CCIC 200 is not a technical or data-science course. It is an early primer:
weather and climate, local impacts, ways of knowing, and sovereignty through
InterTribal and international policy, so students reach TCR 201 ready to act.
The primer runs as a thread through the weeks and as one page in each
minisite, in three rings:

1. **The Nation:** sovereignty, reserved rights, the trust responsibility, and
   self-determination, in plain words. Climate work is sovereignty work.
2. **InterTribal:** how Nations act together: national and regional
   InterTribal organizations, resolutions, consultation, and shared
   positions. The regional ring is a slot; scouts name the organizations from
   their own public pages, and nothing is said on any organization's behalf.
3. **International:** the United Nations Declaration on the Rights of
   Indigenous Peoples, the climate convention and its Local Communities and
   Indigenous Peoples Platform, the IPCC's treatment of Indigenous Knowledge,
   and the CARE Principles. Every date and article number is a verify row
   (tcu/core/verify.md) until opened from the issuer.

TCR 201 then puts the rings to work: policy watch, consultation, InterTribal
resolutions, and coordination, with hand-first tool labs.

## 9. Respect rules built into the template

- **D22 rule, applied everywhere in tcu/:** no learner speaks or acts as a
  Nation, council, Elder, or knowledge holder. Analytic roles are fine;
  quoting a Nation's own public words is fine; partners decline as themselves.
  Where the source curriculum has a role play of a Nation, council, or Elder
  (TCR 201 Weeks 6, 9, and 10; CCIC 200 Week 4), the core carries a neutral
  form: learners are analysts, planners, and staff writing questions, and a
  review panel hears the capstone as itself. (D22 and D28 are PENDING for
  curriculum/; the launch prompt's rule binds tcu/.)
- **Relatives, not resources.** Species lists are public ecology; the
  relationships are the Nation's.
- **A climate unit is not a voice.** A reservation-unit projection is a view of
  public data about a Nation's lands. It is labeled as public data, and it
  stays in private/ until the TCU and, where it applies, the chartering
  Nation review it (SEEDS consent level C2).
- **Boundaries are representations, not jurisdiction.** Any boundary shown
  comes from a public Census or federal representation and says so.
- **Hand first, then tools.** Every data view has a printable table, and every
  tool lab in TCR 201 starts by hand. Tools support and never replace Tribal
  decision-making.
- **Boarding-school history** (where it bears on a site) is handled plainly,
  sourced, without speculation, with a support-resource line on any page that
  carries it.

## 10. Data posture

Every data view carries one visible label and a caption naming its source,
issuer, capture date, and checksum.

| Label | Meaning | Rule |
|---|---|---|
| LIVE | A live public site or feed | Linked for the instructor to open outside class; never embedded; never run in class |
| SNAPSHOT | A dated, checksummed capture in the site's case pack | The only real data a page shows |
| TEACHING MODEL | Invented or simplified numbers that show a pattern | Says so on the view |

Case pack: `private/tcu/<slug>/data/<name>.<ext>` beside
`<name>.meta.json` with source, issuer, unit, scenarios, baseline and future
windows as the file states them, captured_at, SHA-256, and license as stated
(or "not stated"). A projection view always says "projection, not a
prediction" and names its scenario, period, and baseline. A blank is a hatched
grey "unknown", never zero; a total that includes a blank reads "at least".

## 11. What each site gets

Built by `tcu/engine/build.py` into `private/tcu/<slug>/build/`:

1. **Minisite** (`site/`): `index.html` (home with the review panel),
   `place.html` (place profile by eye, climate profile, hazards, local case),
   `ccic-200.html` and ten week pages, `tcr-201.html` and ten week pages,
   `primer.html` (sovereignty primer), `resources.html` (the scout-built
   resource packet: sources opened, leads not yet opened), `credits.html`
   (case pack, fonts, authors), and `timeline.html` where a site has a
   timeline file. Relative links only, no network calls, fonts copied from
   docs/fonts. Works from file:// and from any static host.
2. **Presentations:** `ccic-200-deck.html` and `tcr-201-deck.html`, each one
   self-contained file (fonts inlined), with the workshop's presenter keys:
   arrows or Space move, N speaker notes, T clock, H highlight pass.
3. **PowerPoint:** `ccic-200.pptx` and `tcr-201.pptx` from
   tcu/templates/pptx/, with speaker notes. The ATNI fonts fall back to
   system fonts where they are not installed.
4. **Zips:** `<slug>-minisite.zip` (the site folder, ready to upload) and
   `<slug>-source-kit.zip` (the site's own editable files plus the public
   core, engine, and templates, so the TCU can rebuild without this repo).

The home page's **review panel** counts what is still open on that site:
confirmation marks by Nation, local expert slots, unknown facts, open
sockets, unopened leads, and verify tags. It turns a TCU's review into a
short, concrete list.

Every page carries a visible "DRAFT FOR TCU REVIEW" band while
`draft: true`, and the author line.

## 12. File layout

Public (committed):

```text
tcu/
  README.md            how a TCU uses, edits, rebuilds, and uploads
  DESIGN.md            this file
  registry.yaml        the 40 sites, public facts only
  core/
    ccic-200/          syllabus.md, week-01.md ... week-10.md
    tcr-201/           syllabus.md, week-01.md ... week-10.md
    shared/            primer.md (sovereignty primer), respect.md
    verify.md          factual claims in the core, with sources and status
  engine/              build.py, check.py, mdlite.py, decks.py, pptx_deck.py
  templates/
    minisite/          page.html, site.css
    presentation/      deck.html
    pptx/              tcu-deck.pptx (built by make_template.py), README.md
    site/              site.yaml and deep-dive/*.md starters
```

Private (git-ignored, never committed):

```text
private/tcu/
  LEDGER.md            one line per run step
  STATUS.md            per site: built, checked, gaps, open marks, leads
  _nexus-index.md      locator-first index of NEXUS teaching material
  _review/             pilot and wave reviews
  _example/            the neutral template example site
  <slug>/
    site.yaml          the site's fact slots
    packet/            scout.md (Haskell adds four more)
    data/              case pack files, each with meta.json
    deep-dive/         place-profile.md, ccic-200-local.md, tcr-201-local.md
                       (timeline.yaml where a site has one)
    build/             site/, decks, .pptx, zips
```

## 13. Week file structure (the contract the engine reads)

Each `tcu/core/<course>/week-NN.md` starts with YAML front matter and uses
these level-2 headings, in this order, so the engine can build pages, decks,
and .pptx from one source:

```text
---
course: ccic-200
week: 3
title: Local Sensing and Environmental Observation
thread: "Part 1: How Does a Cloud Work?"
eyes: [frog, bird]
sockets:
  - id: field-site
    purpose: Candidate public field sites for the Field Observation Project
    eye: frog
    consent: C0
---
## Key lesson
## Key takeaway
## Learning objectives
## Before class
## Session shape        (table: time, module, what happens)
## Hands-on activity
## Local lesson         ({{socket:...}} calls live here)
## Check for Understanding   (three numbered items)
## Assignment
## Reflection           (prompt, then "Say it plain:")
## Guest or Elder slot
## Instructor notes
## Sovereignty thread   (CCIC 200 only, where the primer touches the week)
```

A heading may be empty only if the week has nothing for it; it is never
dropped, so every week reads the same way.

## 14. How a TCU edits and rebuilds its minisite

1. Open the source kit (or this repo's tcu/ folder plus the site folder).
2. Edit `site.yaml` (institution facts, course numbers, instructor) and the
   Markdown in `deep-dive/` (place profile and local lessons). Replace a
   marker only with your own words; replace a confirmation mark only with the
   Nation's recorded confirmation.
3. Run `python engine/build.py <slug>` (Python 3.10 or newer; python-pptx is
   needed only for the .pptx files, and the pages build without it).
4. Run `python engine/check.py <slug>`. It fails on an em dash, any page that
   loads an external URL, missing alt text, an unlabeled data view, a case
   pack file without its meta.json, or a leftover unresolved slot name.
5. Upload the contents of `<slug>-minisite.zip` to any static host, a learning
   management system's file area, or a campus web server; or open
   `index.html` from a USB drive with no network.

The shared core is read-only for a site. Improvements to it go back to
Patrick so every site benefits.

## 15. Design system

ATNI Climate design system only: League Spartan (display), Lexend Deca
(body), Cascadia Code (data); ATNI Red on black (`--base #010B13`, `--red
#E13D33`), with the workshop's existing tokens for marks (water blue, magenta).
No TCU logos, no new palettes, no new fonts (open question for Patrick: does a
TCU's minisite carry its own identity, and does it carry the ATNI Climate
lockup; this build carries neither, only the author line). Long pages also
print: a print stylesheet sets dark text on white and keeps every marker
readable in black and white.

Accessibility: WCAG 2.2 AA, full keyboard use, visible focus, screen-reader
text for every data view (a table beside every chart), reduced motion
respected (nothing moves that matters), tap targets at least 44 px, layouts
checked at 1920x1080, 1366x768, and 390 px wide.

## 16. Open questions for Patrick

1. Does the second grammar read as "lecture or presentation, Check for
   Understanding, module assignment, reflection" (the syllabi's words), and is
   the mapping in section 4 right?
2. TCU identity on each minisite: logos and the ATNI Climate lockup (section
   15).
3. Sites listed by IPEDS as Tribal colleges but not in Appendix A, and the
   reverse (run ledger, step 1). No site is added or dropped without Patrick.
4. Boundary cases for the climate unit: Keweenaw Bay (the campus point sits
   just outside the L'Anse Reservation polygon) and Stone Child (the campus
   point is in Rocky Boy's Off-Reservation Trust Land, which the cache does
   not hold). The rule gives the county; Patrick may choose the reservation
   unit.
5. Promotion: when a TCU and Nation have reviewed a site, what moves to the
   public tree, and under what license (proposed D32).
