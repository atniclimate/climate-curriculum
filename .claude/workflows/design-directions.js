export const meta = {
  name: 'design-directions',
  description: 'Draft several genuinely different print-design directions in parallel, render each, score them with independent critics, and recommend one with grafts from the others',
  whenToUse: 'Starting or rethinking a print piece (event handout, a PDF cover or opener system) when Patrick should choose between rendered options',
  phases: [
    { title: 'Draft', detail: 'one print-designer per direction, each in its own folder' },
    { title: 'Critique', detail: 'two visual-critic lenses per direction' },
    { title: 'Recommend', detail: 'compare all directions; pick and graft' },
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

const results = await pipeline(
  DIRECTIONS,
  d => agent(
    `Design the ${piece} for the Columbia River Climate Change Teachers curriculum in this direction: ${d.angle}\n` +
    `Read ${brief} for content, constraints, and images, and the "Next session" section of planning/LAUNCH-PROMPT.md for the code map. ` +
    `Work only inside ${outDir}/${d.slug}/ (create it): a self-contained source there, rendered to PDF with Chrome headless as tools/print_pdf.py does (own --user-data-dir), ` +
    `then a PNG via python tools/contact_sheet.py. Do not edit tracked repo files. Use placeholder text exactly as the brief marks it; do not invent names or facts. ` +
    `Make it good enough that Patrick could choose it as is.`,
    { label: `draft:${d.slug}`, phase: 'Draft', agentType: 'print-designer', schema: DESIGN }),
  (draft, d) => draft && parallel(['type', 'image'].map(lens => () =>
    agent(`Critique ${draft.png} (source ${draft.source || draft.pdf}) through the ${lens} lens for the ${piece}. Direction intent: ${d.angle}`,
      { label: `critique:${d.slug}:${lens}`, phase: 'Critique', agentType: 'visual-critic', schema: CRIT })))
    .then(cs => ({ draft, critiques: cs.filter(Boolean) })),
)

const done = results.filter(r => r && r.draft)
log(`${done.length} of ${DIRECTIONS.length} directions rendered`)
const summary = done.map(r => ({
  slug: r.draft.slug, png: r.draft.png, pdf: r.draft.pdf, rationale: r.draft.rationale,
  scores: r.critiques.map(c => c.score), fixes: r.critiques.flatMap(c => c.fixes),
}))
phase('Recommend')
const rec = await agent(
  `You are choosing between rendered design directions for the ${piece}. Look at each PNG yourself before deciding. ` +
  `Data: ${JSON.stringify(summary)}\n` +
  `Return: the recommended direction and why in three sentences; the best idea to graft from each other direction; ` +
  `the ranked fix list for the winner (merge duplicates); and the questions only Patrick can answer.`,
  { label: 'recommend', phase: 'Recommend', agentType: 'visual-critic' })
return { directions: summary, recommendation: rec }
