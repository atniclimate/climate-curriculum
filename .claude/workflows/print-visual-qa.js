export const meta = {
  name: 'print-visual-qa',
  description: 'Render a print PDF, critique every page through three lenses in parallel, run a mechanical preflight, and return one ranked fix list',
  whenToUse: 'After a print PDF or the event handout changes, before showing Patrick or sending to a printer',
  phases: [
    { title: 'Render', detail: 'pages to PNG, grouped for critics' },
    { title: 'Critique', detail: 'type, image, and content lenses per group' },
    { title: 'Preflight', detail: 'fonts, ppi, metadata, links, EXIF' },
    { title: 'Synthesize', detail: 'dedupe and rank' },
  ],
}

// args: { pdf: 'docs/downloads/<file>.pdf', pages?: '1-8,26', group?: 6, outDir?: 'private/craft/qa/<pdf stem>' }
// Cost: 3 Opus critics per group of pages, plus render, preflight, and synthesis. A full 33-page pass is about 21 agents;
// pass `pages` for the pages that changed.
const pdf = args && args.pdf
if (!pdf) throw new Error('pass args.pdf')
const group = args.group || 6
const stem = pdf.split(/[\\/]/).pop().replace(/\.pdf$/i, '')
const outDir = args.outDir || `private/craft/qa/${stem}`  // one folder per PDF so two runs never overwrite each other's p01.png

phase('Render')
const rendered = await agent(
  `Run: python tools/contact_sheet.py ${pdf} ${outDir} --each --dpi 110` + (args.pages ? ` --pages ${args.pages}` : '') +
  `. Return the list of PNG paths it printed, in page order. If it fails, return an empty list.`,
  { label: 'render', phase: 'Render', effort: 'low', model: 'sonnet', schema: { type: 'object', properties: { pngs: { type: 'array', items: { type: 'string' } } }, required: ['pngs'] } })
const pngs = (rendered && rendered.pngs) || []
if (!pngs.length) throw new Error(`no pages rendered from ${pdf}`)
const groups = []
for (let i = 0; i < pngs.length; i += group) groups.push(pngs.slice(i, i + group))
log(`${pngs.length} pages in ${groups.length} groups`)

const FINDINGS = {
  type: 'object',
  properties: { findings: { type: 'array', items: { type: 'object', properties: {
    page: { type: 'string' }, where: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' },
    severity: { type: 'string', enum: ['blocker', 'should', 'could'] } }, required: ['page', 'problem', 'fix', 'severity'] } } },
  required: ['findings'],
}

const [critiques, preflight] = await Promise.all([
  pipeline(groups, g => parallel(['type', 'image', 'content'].map(lens => () =>
    agent(`Open each of these rendered pages of ${pdf} with the Read tool and critique them through the ${lens} lens: ${g.join(', ')}`,
      { label: `${lens}:${g[0].split(/[\\/]/).pop()}`, phase: 'Critique', agentType: 'visual-critic', schema: FINDINGS })))),
  agent(`Preflight ${pdf}.`, { label: 'preflight', phase: 'Preflight', agentType: 'print-preflight' }),
])

const all = critiques.flat().filter(Boolean).flatMap(r => r.findings)
log(`${all.length} raw findings`)
phase('Synthesize')
const ranked = await agent(
  `Merge duplicate findings, drop any you can refute by looking at the PNG, and rank the rest blocker, should, could. ` +
  `Return a short table: page, problem, fix, severity. Findings: ${JSON.stringify(all)}\nPreflight report: ${preflight}`,
  { label: 'synthesize', phase: 'Synthesize', agentType: 'visual-critic' })
return { pdf, pages: pngs.length, findings: all.length, ranked, preflight }
