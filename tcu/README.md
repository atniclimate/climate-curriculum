# TCU Templates: CCIC 200 and TCR 201 for every Tribal College

This folder turns one shared climate pathway into a template set for each
Tribal College and University (TCU) and each Northwest Indian College
extended campus site, 40 sites in all (`registry.yaml`):

- **CCIC 200, Climate Change in Indian Country:** an early primer on weather
  and climate, local impacts, ways of knowing, and sovereignty through
  InterTribal and international policy.
- **TCR 201, Tribal Climate Resilience:** adaptation, mitigation, resilience,
  and policy action, with hand-first tool labs.

Module author: Patrick A. Freeland (module author), with ATNI Climate. Built on
*Understanding a Climate of Change*, by Patrick Freeland and Cayla Jones; Steve
Robinson's *Climate Change and the Tribes: Columbia River Edition* (draft); and
NESC 215, Climate Change in Indian Country, Northwest Indian College.
Licensing is set later.

Status: template draft. Every site's own files are DRAFT FOR TCU REVIEW and
stay private until that TCU, and where it applies the chartering Nation, has
reviewed them. How the pieces fit is in `DESIGN.md`.

## What is shared and what is yours

| Shared (the same at every site) | Yours (your TCU's own files) |
|---|---|
| `core/`: both syllabi, twenty weeks, the sovereignty primer, the respect page, and the verify list | `site.yaml`: your institution's facts, course numbers, region, and local case |
| `engine/`: the build and check scripts | `deep-dive/`: your place profile and local lessons (the sockets each week calls) |
| `templates/`: page, deck, and PowerPoint templates | `packet/`: the resource packet scouts built from public sources |
| | `data/`: your case pack, every file with its meta.json |

The shared weeks stay the same everywhere. Your local lessons plug into the
sockets each week names. If you want to change a shared week, send the idea to
Patrick so every site can benefit.

Marks on the pages are invitations, not gaps to hide:

- `[LOCAL EXPERT: TCU faculty or knowledge holder]`: teaching that belongs to
  your faculty, local experts, and knowledge holders.
- `[NEEDS TRIBAL CONFIRMATION: <Nation>]`: only that Nation supplies or
  approves this. Replace it only with the Nation's recorded confirmation.
- `[PLACEHOLDER: ...]`: your institution supplies it.
- A hatched "unknown" box: a fact no public source gave us. Unknown is never
  zero.

The home page of each minisite counts these marks in a review panel, so a
review starts from a short, concrete list.

## How to use your minisite

1. Unzip `<slug>-minisite.zip`. Open `index.html` in any browser. It works
   with no internet: no page loads anything from the network, and nothing a
   student types leaves the page.
2. To publish it, upload the folder's contents to any static web host, your
   learning management system's file area, or a campus web server.
3. The two presentations (`ccic-200-deck.html`, `tcr-201-deck.html`) are
   single files that carry their own fonts. Keys: arrows or Space move, N
   speaker notes, T clock, H highlight pass.
4. The PowerPoint files (`ccic-200.pptx`, `tcr-201.pptx`) carry the same
   slides and notes. If the ATNI fonts are not installed, PowerPoint uses a
   fallback font.

## How to edit and rebuild

You need Python 3.10 or newer with PyYAML. python-pptx is needed only for the
.pptx files; the pages build without it.

```powershell
# 1. Unzip the source kit; it holds tcu\core, tcu\engine, tcu\templates, and tcu\sites\<slug>.
Expand-Archive .\<slug>-source-kit.zip -DestinationPath .\kit
cd .\kit

# 2. Edit your files (any text editor):
#    tcu\sites\<slug>\site.yaml and tcu\sites\<slug>\deep-dive\*.md

# 3. Rebuild. Prints the counts of open marks when it finishes.
python tcu\engine\build.py <slug>

# 4. Check. Prints "<slug>: pass" or lists each problem and exits 1.
python tcu\engine\check.py <slug>
```

The rebuilt site is in `tcu\sites\<slug>\build\site\`, with a fresh
`<slug>-minisite.zip` beside it.

The check fails on an em dash, any page that loads an external URL, an image
or chart without a text alternative, a data view without its LIVE, SNAPSHOT,
or TEACHING MODEL label, a case-pack file without its meta.json, or a leftover
`{{slot}}`. Links to public sources are fine.

## Writing local lessons

Each shared week names its sockets in its front matter (for example,
`core/ccic-200/week-03.md` names `field-site`). In
`deep-dive/ccic-200-local.md`, a section headed exactly
`## socket: week-03/field-site` fills it. Leave a section out and the page
shows an open "Local lesson slot" instead, which is a fine state to be in.

- Public facts carry their source and the date you opened it.
- Plants, animals, and waters are relatives, not resources. A species list is
  public ecology; the relationships are the Nation's.
- No learner speaks or acts as a Nation, council, Elder, or knowledge holder.
  Learners work as themselves, as analysts, or by reading a Nation's own
  public words.
- Every data view is labeled. Live sites are opened outside class; in class,
  pages show dated SNAPSHOT files from `data/`.

## For the ATNI build machine

- `engine/data_profile.py <slug>` captures a site's case pack from the build
  machine's raw-data store and public services, and seeds `site.yaml`.
- `engine/build.py --all` and `engine/check.py --all` build and check every
  site under `private/tcu/`.
- Site folders live in the git-ignored `private/tcu/` and are never committed.
