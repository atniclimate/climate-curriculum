# Launch Prompt

Paste the block below into the first Claude Code session in I:\climate-curriculum.
For later sessions, use the short "Resume" block at the bottom.

## First session

```
You are working in I:\climate-curriculum, a local clone of
github.com/atniclimate/climate-curriculum: the Columbia River Climate Change
Teachers curriculum and its interactive workshop "Understanding a Climate of
Change" (ATNI Climate; authors Patrick Freeland and Cayla Jones). I am Patrick.

The working rules, scope, and plan live in files, not in this prompt. Read
them first, in this order, and treat them as binding:
  1. CLAUDE.md                                (rules; precedence order)
  2. planning/revision-notes-2026-10-14.md    (scope source of truth)
  3. planning/PLAN.md                         (work order and STOP points)
  4. planning/DECISIONS.md                    (open decisions; you never rule)
  5. planning/VERIFY.md, MEDIA-CREDITS.md, VOICE-PASS.md, HANDOFF.md
Then read README.md, curriculum/, source/, and docs/index.html.

Two lines in this prompt are LOCKED (my words; keep them exactly):

  S1 title slide, these line breaks on wide screens:
    Four Directions, one River. When you can communicate in a
    respectful way, where both an Elder and a Child can understand;
    this is the surest sign that you are able to share knowledge.

  S2 title:
    To seek understanding is less about being told

How each one fits with the revision notes (casing, punctuation, whether the
old Elder/Child blockquote stays, what happens to "Four Questions, One
River") is open in DECISIONS D8, D9, D1, and D2.

=== PHASE 0: ORIENT (read only until step 5) ===
1. Create branch dev/revisions-2026-10 and tell me the git command you used,
   what it does, and what output to expect.
2. Run the build (python source/build.py; try python, py, python3) and
   compare its output to the committed docs/index.html. Report whether it
   matches. If not, STOP and show me what differs.
3. Slide inventory: a table of S-number, current title, and where each
   slide lives in source/template.html. Flag any place where the live site
   order differs from the S1 to S23 numbering in the revision notes.
4. Read I:\community-connector (READ ONLY; never edit that repo). Report its
   graph engine's size, dependencies, and license, for D15.
5. First commit: add the planning/ folder and CLAUDE.md as they are, plus a
   stable data-slide-id on every slide (e.g. s04-cloud-tool). Rebuild.
   No visible change to the page.
6. Decision walkthrough. Take me through only the decisions Phase 1 and 2
   need, ONE AT A TIME, in this order: D8, D9, D1, D2, D3, D12, D10. For
   each: the plain name and ID, a short narrative of what it changes on
   the page, concrete implications of each option, and the default ruling
   I can accept or change. Wait for my answer before the next one. Record
   my rulings in DECISIONS.md. Leave D4 to D7, D11, and D13 to D15 for
   when their phase comes up.

=== PHASE 1 AND ONWARD ===
Follow planning/PLAN.md from Phase 1, honoring every STOP. Additional
expectations:

Layout and blocking (Phase 1), all slides:
- The S1 lines hold my breaks at 1920x1080 and 1366x768 and read as an even
  stanza; on narrow screens (390px) they reflow with text-wrap: balance, no
  stranded single words.
- Headings use text-wrap: balance; body text uses text-wrap: pretty; body
  lines about 45 to 75 characters; consistent vertical rhythm and safe
  margins; no clipping at 1366x768 or on a projector; a scrim wherever text
  sits on a photo and fails contrast.
- Sibling cards render equal heights (grid, align-items: stretch) and their
  copy is balanced to the word targets in the notes.
- Report a before/after list by S-number and plain title.

Draft language: place DRAFT strings from the notes where the plan says to,
list every one in VOICE-PASS.md, and never present a DRAFT as final.

Facts and media: every factual claim gets a VERIFY.md row before it ships;
every photo, video, dataset, and library gets a MEDIA-CREDITS.md row with
its license confirmed on the item's own page.

K-12 interactivity: the slides themselves are the K-12 interactive (cloud
tool, gauges, reciprocal inquiry card, nested zoom, species cards,
constellation). Every interactive piece needs: keyboard and touch use,
screen-reader labels, prefers-reduced-motion, smooth performance on a
school Chromebook (test at 4x CPU throttle), and a low-tech classroom
version described in the slide notes. Separate student pages wait on D13.

Concept briefs (Phase 7): for S9, S12, S15, S16, and S17, write a one-page
brief each in planning/briefs/, with a sketch of the interaction, the
learning goal, and open questions for me. Do not build them.

At every STOP: show what changed (S-number and plain title), what is
waiting on me (decision ID with its plain name), and the next step.

At the end of the session: update PLAN.md checkboxes, add a HANDOFF.md
entry, commit, and give me the git commands to review the branch and push
it, explaining what each does and what output to expect. Do not push.
```

## Resume (later sessions)

```
Resume work on I:\climate-curriculum. Read CLAUDE.md, the top entry of
planning/HANDOFF.md, and planning/PLAN.md. Check DECISIONS.md for rulings I
have made since the last session. Tell me in a few lines where things stand
and what is next, then continue from the next unchecked item in PLAN.md,
honoring every STOP. Walk me through any newly needed decision one at a
time with a default ruling. End by updating PLAN.md and HANDOFF.md and
committing. Do not push.
```
