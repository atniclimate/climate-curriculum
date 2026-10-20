// Viewport and accessibility probe for docs/index.html. Read-only: loads the built page over file://.
// Run:  playwright-cli open  then  playwright-cli run-code --filename probe.js  then  playwright-cli close
// Returns JSON: per viewport x notes state x slide, only the slides with findings, plus 4x-throttled frame stats.
async page => {
  // shortcut: path is this machine's clone; change it (or serve docs/ on 127.0.0.1) elsewhere.
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
