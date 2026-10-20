export const meta = {
  name: 'design-directions',
  description: 'Draft several genuinely different print-design directions in parallel, render each, score them with independent critics, and recommend one with grafts from the others',
  whenToUse: 'Starting or rethinking a print piece (event handout, a PDF cover or opener system) when Patrick should choose between rendered options',
  phases: [
    { title: 'Draft', detail: 'one print-designer per direction, each in its own folder' },
    { title: 'Critique', detail: 'two visual-critic lenses per direction' },
    { title: 'Recommend', detail: 'pick and graft; compare.png side by side for Patrick' },
  ],
}

// args: {
//   piece: 'event handout' | 'lessons cover and unit openers' | ...,
//   brief: 'private/handout/BRIEF.md',            // file the designers read
//   outDir: 'private/craft/directions/<piece>',   // git-ignored; one subfolder per direction
//   directions: [{slug, angle}],                  // optional; defaults below
// }
const piece = (args && args.piece) || 'event handout'
const brief = (args && args.brief) || 'private/handout/BRIEF.md'
const outDir = (args && args.outDir) || 'private/craft/directions/handout'
const DIRECTIONS = (args && args.directions) || [
  { slug: 'photo-forward', angle: 'The photograph carries the page: full-bleed or near-full-bleed image, a confident scrim, type set into the light. Feels like a place.' },
  { slug: 'typographic', angle: 'Type and the ATNI red carry the page: strong scale contrast, a disciplined grid, the photo as a band or inset. Feels like a field guide.' },
  { slug: 'map-mark', angle: 'The Columbia basin line map is the organizing mark (from source/columbia_svg.json), with the photo as texture or duotone behind it. Feels like a river system.' },
]

const DESIGN = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    source: { type: 'string', description: 'path of the HTML (or other) source for this direction' },
    pdf: { type: 'string' },
    png: { type: 'string', description: 'render of the page(s) at about 110 dpi' },
    rationale: { type: 'string' },
    open_questions: { type: 'array', items: { type: 'string' } },
  },
  required: ['slug', 'pdf', 'png', 'rationale'],
}
const CRIT = {
  type: 'object',
  properties: {
    score: { type: 'number', description: '1 to 10, how ready and how strong' },
    strengths: { type: 'array', items: { type: 'string' } },
    fixes: { type: 'array', items: { type: 'object', properties: { what: { type: 'string' }, fix: { type: 'string' }, severity: { type: 'string', enum: ['blocker', 'should', 'could'] } }, required: ['what', 'fix', 'severity'] } },
  },
  required: ['score', 'strengths', 'fixes'],
}

// The angles are starting points, not rules: the designer may push its direction wherever it gets stronger.
const results = await pipeline(
  DIRECTIONS,
  d => agent(
    `Design the ${piece} for the Columbia River Climate Change Teachers curriculum. Your direction: ${d.angle}\n` +
    `Read ${brief} for content, images, and print specs, and the "Next session" section of planning/LAUNCH-PROMPT.md for the code map. ` +
    `Other designers are working in parallel, so work only inside ${outDir}/${d.slug}/ (create it) and touch no tracked file: ` +
    `for the handout, a self-contained HTML source there; for PDF covers or openers, copy tools/print_pdf.py into your folder and point ROOT at the repo and OUT at your folder ` +
    `(the original writes the published docs/downloads PDFs). Render with Chrome headless using a --user-data-dir inside your folder, ` +
    `then python tools/contact_sheet.py <pdf> <png> (add --dpi 110 for a one-page piece). ` +
    `QR: use private/craft/qr/qr.svg if it exists, else a light tile at final size marked QR. ` +
    `Names and wording from the brief may appear in your private draft; keep every [confirm] and DRAFT mark visible; invent no names, facts, or cultural content. ` +
    `Make it good enough that Patrick could choose it as is.`,
    { label: `draft:${d.slug}`, phase: 'Draft', agentType: 'print-designer', schema: DESIGN }),
  (draft, d) => draft && parallel(['type', 'image'].map(lens => () =>
    agent(`Open ${draft.png} with the Read tool and critique it through the ${lens} lens for the ${piece} (source ${draft.source || draft.pdf}). Direction intent: ${d.angle}`,
      { label: `critique:${d.slug}:${lens}`, phase: 'Critique', agentType: 'visual-critic', schema: CRIT })))
    .then(cs => ({ draft, critiques: cs.filter(Boolean) })),
)

const done = results.filter(r => r && r.draft)
log(`${done.length} of ${DIRECTIONS.length} directions rendered`)
const summary = done.map(r => ({
  slug: r.draft.slug, png: r.draft.png, pdf: r.draft.pdf, rationale: r.draft.rationale,
  scores: r.critiques.map(c => c.score), fixes: r.critiques.flatMap(c => c.fixes),
}))
if (!done.length) throw new Error('no direction rendered; read the Draft agents\' output')
phase('Recommend')
const letters = done.map((r, i) => `${String.fromCharCode(65 + i)} = ${r.draft.slug}`).join(', ')
const [rec, compare] = await parallel([
  () => agent(
    `You are choosing between rendered design directions for the ${piece}. Open each PNG with the Read tool before deciding. ` +
    `Data: ${JSON.stringify(summary)}\n` +
    `Return: the recommended direction and why in three sentences; the best idea to graft from each other direction; ` +
    `the ranked fix list for the winner (merge duplicates); a content check of the winner (house style, Yakama Nation first in the acknowledgements, ` +
    `[confirm] and DRAFT marks still visible, no invented names); and the questions only Patrick can answer.`,
    { label: 'recommend', phase: 'Recommend', agentType: 'visual-critic' }),
  () => agent(
    `With Pillow, place these PNGs side by side at equal height on a white canvas, each labeled with its letter and slug in large type above it ` +
    `(${letters}): ${done.map(r => r.draft.png).join(', ')}. Save ${outDir}/compare.png and return only its path.`,
    { label: 'compare sheet', phase: 'Recommend', effort: 'low', model: 'sonnet' }),
])
return { directions: summary, compare, recommendation: rec }
