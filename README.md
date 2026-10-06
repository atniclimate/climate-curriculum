# Columbia River Climate Change Teachers Curriculum

Curriculum materials for the Columbia River Climate Change Teachers program, prepared by the Affiliated Tribes of Northwest Indians (ATNI) Climate Program. These materials center Indigenous Knowledge, Tribal sovereignty, and the Treaty-reserved relationships that bind the people, the salmon, and the river. They treat the plants, animals, and waters of the Columbia Basin as relatives, not resources.

> “Think… when both an Elder and a Child can understand, then this is where learning happens.”

The spine of every piece is *Understanding a Climate of Change: Understanding an Ever Changing Climate*, by Patrick Freeland and Cayla Jones, and its Four Questions: How does a cloud work? How do you know what you know? What can we do? How do we work together? Case material comes from Steve Robinson's *Climate Change and the Tribes: Columbia River Edition* (draft).

**Live workshop:** https://atniclimate.github.io/climate-curriculum/

## What is here

| Component | File | Audience |
|---|---|---|
| Guiding document and language revision | [`curriculum/Understanding-a-Climate-of-Change_Guiding-Document.md`](curriculum/Understanding-a-Climate-of-Change_Guiding-Document.md) | Authors, facilitators, editors |
| 1. Workshop: *Understanding a Climate of Change* | [`docs/index.html`](docs/index.html) | Educators, about 30 minutes |
| 2. Hands-on activities and lessons | [`curriculum/CRCCT_Grades6-12_Hands-On_Lessons.md`](curriculum/CRCCT_Grades6-12_Hands-On_Lessons.md) | Grades 6 to 12 |
| 3a. Climate Change in Indian Country (200 level) | [`curriculum/CCIC-200_Climate_Change_in_Indian_Country_Syllabus.md`](curriculum/CCIC-200_Climate_Change_in_Indian_Country_Syllabus.md) | Tribal Colleges and Universities |
| 3b. Tribal Climate Resilience (201 level) | [`curriculum/TCR-201_Tribal_Climate_Resilience_Syllabus.md`](curriculum/TCR-201_Tribal_Climate_Resilience_Syllabus.md) | Tribal Colleges and Universities, Tribal staff |

## The workshop

The workshop is a single interactive page of 23 slides that follows the Four Questions. Every interactive slide carries an "Ask the room" guiding question. It uses the ATNI Climate design system (League Spartan, Lexend Deca, and Cascadia Code; ATNI Red on black).

Interactive pieces:

- **Follow the air:** a slice of the land from the Pacific over the Coast Range and Cascades to the Columbia Plateau, with seasons, an atmospheric river, cloud types, rain and snow intensity, the snow line, the rain shadow, and a +2 °C comparison. A teaching model, not a forecast.
- **Frog's eye, bird's eye, moon's eye:** three scales of knowing.
- **The journey home:** the salmon's journey up the Columbia and Snake, or the upper Columbia, with the challenges at each stop and river futures under CMIP6 SSP2-4.5 and SSP3-7.0 (August water temperature and the shape of flow through the year). The futures are a working draft scaled from published studies; see the slide notes and replace with CMIP6 river runs when available.
- **Relatives of the river:** a working-draft species page (salmon, steelhead, Pacific lamprey, white sturgeon, eulachon, bull trout, suckers, freshwater mussels).
- The source check, the A/M/R sort, and the web of relatives.

Presenter keys:

- **Arrow keys or Space** move between slides
- **N** opens speaker notes
- **T** shows the clock
- **H** toggles the highlight pass

Background photos are set in one place, the `IMAGES` registry near the top of the page script. To swap a photo, drop the new file in `docs/img/` and update its path and credit there. Photo credits are blank until filled in; confirm rights for any photo not taken by ATNI staff before wider sharing.

The workshop runs offline too: download the `docs/` folder and open `index.html` in a browser.

### Folder layout

```
curriculum/   Lesson plans and syllabi (Markdown, meant to be edited)
docs/         The workshop, served by GitHub Pages
  fonts/      Subset web fonts
  img/        Background photos and ATNI marks
source/       Workshop build sources
  template.html       Page template with a __MAP__ placeholder (edit this)
  columbia_svg.json   Columbia River map (Natural Earth 1:10m, LCC projection)
  build.py            Rebuilds docs/index.html: python3 source/build.py
```

## Editing notes

These are working drafts. Before teaching from them:

- Items marked **[verify]** or listed in an editor's note need a fact check against current sources.
- Placeholders in brackets mark content only ATNI staff or a Tribe can supply, including Tribal-specific projections, place names, stories, and permissions. Do not fill these without the appropriate Tribal consultation.
- Funding and policy status changes quickly. The 2025 to 2026 status notes in the 201 syllabus were current as of 09/24/2026.

House style: capitalize Indigenous, Tribal, Tribes, Nations, Elder, Treaty, and First Foods; use the Oxford comma; write dates as MM/DD/YYYY; and never refer to Tribal Nations or Tribal people as "stakeholders."

## Related ATNI tools

The 201 course draws on ATNI Climate tools, including the [Dynamic Drought Module](https://atniclimate.github.io/dynamic-drought-module/), [policy-sentinel](https://github.com/atniclimate/policy-sentinel), and [land-use-analyzer](https://github.com/atniclimate/land-use-analyzer), as well as the TCR Policy Scanner and Plan Assessor.

## Data sovereignty

Tribal data shared through this program remains the property of the Tribe that shared it. Classroom use of any Tribe-specific material requires that Tribe's permission.
