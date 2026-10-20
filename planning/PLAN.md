# Development Plan

Source of truth for scope: planning/revision-notes-2026-10-14.md.
Decisions: planning/DECISIONS.md. Fact checks: planning/VERIFY.md.
Credits: planning/MEDIA-CREDITS.md. Patrick's voice pass: planning/VOICE-PASS.md.

Status marks: [ ] not started, [~] in progress, [x] done, [hold] waiting on Patrick.
STOP points: the session pauses and waits for Patrick's review.

Slide ids: every slide carries data-slide-id (s01-title ... s23-close); the
inventory is the ids in the source (`grep -n data-slide-id source/template.html`).
Navigation hashes (#s1 to #s23) are still by position, so a reorder changes them.
Skills: cc-release-check, cc-slide-change (project); curriculum-design-check and
the curriculum-specialist agent (user level).

## Gates used at every step
- Build: `python source/build.py` (UTF-8, LF). A refactor or markup-only change
  must leave the built page identical apart from the intended attributes.
- Viewports: 1920x1080, 1366x768, 390x844, notes closed and open. Probe for
  clipped `.inner.fit` content, hall lines that break somewhere other than the
  intended `<br>`, tap targets under 44x44, and unequal sibling card heights.
  Probe and screenshots live outside docs/ (scratchpad or planning/).
- Word balance: count sibling-card words before each STOP.
- Ledgers: every DRAFT in VOICE-PASS, every fact in VERIFY, every photo, font,
  dataset, and library in MEDIA-CREDITS.

## Phase 0. Orient (read only)
- [x] Read CLAUDE.md, this folder, README, curriculum/, source/, docs/index.html
- [x] Confirm build reproduces committed docs/index.html (needed a UTF-8 fix to build.py; committed separately)
- [x] Slide inventory: S-number, current title, location in source
- [x] Add stable data-slide-id to every slide (first commit); slide comments renumbered to S-numbers
- [x] Read I:\community-connector (read only) and report engine size, deps, license (for D15)
- [hold] Decision walkthrough: deferred by Patrick to the next session; suggested order in DECISIONS.md (D21 first)
- [x] Environment review team, source library, references, two Codex reviews (10/14/2026; see HANDOFF)

## Workshop readiness track (D21 ruled 10/20/2026: 30-minute ATNI slot; page and DDM walkthrough, Q&A; resources downloadable)
Branch dev/workshop-polish-2026-10. Done 10/20/2026:
- [x] Interface polish (Phase 1g subset): 44px tap targets, 12px text floor, equal .carry cards, S1 h1, reduced motion for .pulse and .story, credit contrast, faster slide fade, next-photo preload, larger S20 hit areas
- [x] D25 factual corrections on the slides and in both curriculum documents; VERIFY rows V4, V16, V17, V24, V29, V30, V53, V55, V58, V60 to V64; VOICE-PASS VP1 to VP8
- [x] Copy-edit of the Grades 6-12 lessons and the guiding document
- [x] Print-ready PDFs in docs/downloads/ (tools/print_pdf.py); Lesson 4.3 printed marked DRAFT per D22 note
- [x] Merged to main by Patrick (0d037c3); Pages built 10/20/2026
- [ ] One-page full-color event handout: abstract, cited papers, QR code, acknowledgements (Yakama Nation first); brief in private/handout/BRIEF.md (local); Patrick approves names and copy by 10/21
- [ ] Photographic covers and openers for both PDFs (stripped copies in private/print-assets/; MEDIA-CREDITS rows when published)
- [ ] S22: link the PDFs and the handout (notes placeholder asks where teachers download files)
- [ ] Patrick: printer (office or print shop with bleed), QR library (segno), credit lines, DesignCraft 0.10.0 upgrade
- [ ] Route identity: which slides and handouts, how many minutes, what equipment (D21, D24)
- [ ] Safety and integrity on that route: known corrections (D25), Goldendale role play out of anything distributed (D22), S23 session-only reflections (D23), uncredited photos replaced or hidden
- [ ] Teacher outcomes (three, observable) and a handoff card; one hand twin
- [ ] cc-release-check route + sheet: run sheet with 15/30/60-minute variants, printed fallback, projector-only plan
- [ ] Offline folder rehearsal on a school Chromebook and projector, network off
- [ ] STOP: Patrick's release decision

## Phase 1. Language and layout (low risk, high visibility), one commit per step
- [ ] 1a S1 locked line (D8) and S2 together: locked title (D9/D1), blockquote (D2), Four Questions cards (notes 2.2, D3), series line (notes 2.1), scale chip. S1 needs a 62ch override and `<br>` stanza markup; the S1 display becomes the page's h1 with no visual change
- [ ] 1b Dividers S3, S7, S14, S19 with Q1 to Q4 locked text (needs D16 hall word budget, D17 S3 form, D18 S14 fire draft)
- [ ] 1c S8 headings to Frog's Eye, Bird's Eye, Moon's Eye; DRAFT card copy (~40 words each)
- [ ] 1d S10 title to "The Salmon's Journey"; README follows; DRAFT intro placement per D19
- [ ] 1e S21 closing words, Patrick's line breaks (D5 note if ruled)
- [ ] 1f S12 Elder/Child removal and speaker-notes rewrite (per D2)
- [ ] 1g Layout and accessibility pass, all slides: text-wrap balance/pretty, 45 to 75 character lines, hall scrims, sub-12px text floors at 390px, 44px tap targets, `.pulse` and `.story li` under reduced motion, `.credit` contrast, equal heights for `.carry`, `.sort`, `.webwrap` (currently align-items:start)
- [ ] 1h Ledgers: VOICE-PASS rows for every DRAFT placed; VERIFY backfill for facts already live (mark "inherited"); MEDIA-CREDITS rows for 15 photos and 3 fonts
- [ ] STOP

## Phase 2. Fixes and foundation
- [ ] 2a S10 river lines registered to basemap. Likely cause: drawHeat() samples 8 straight chords per stop regardless of length, so the heat band cuts corners (up to 24 units on the Salmon River leg). Fix with length-proportional sampling; confirm on both routes and all futures
- [ ] 2b Source split (if D10 = A), alone in its commit, gated on an identical build
- [ ] STOP

Phases 3, 5, and 6 and the D10 split are after the workshop, and both Codex
reviews advise waiting for teacher evidence before the largest builds (cloud
taxonomy, nested zoom, video lightbox, constellation camera). Build the
smallest causal model first; genera become an optional field guide.

## Phase 3. Cloud tool rebuild (S4), in sub-steps, STOP after each
- [ ] 3a Controls grouped (Temperature, Pressure, Moisture, Season, Wind) and live "What is happening" panel. Note: the model has no pressure input today (pressure comes from elevation); a Pressure control needs a physical hook or it is decorative
- [ ] 3b Cloud shape system for ten genera plus lenticular; morphing between types (D11)
- [ ] 3c Multiple layers (low, middle, high)
- [ ] 3d Jet stream and wind by altitude
- [ ] 3e Sun angle / time of day; summer thermals east of the Cascades
- [ ] 3f Broader Pacific, evaporation, atmospheric river plume; snow line with +2 C

## Phase 4. Gauges and Carry Forward pattern
- [ ] S5 gauges: take a reading, record grows, pattern appears; Reading to Record to Pattern to Knowledge to Decision
- [ ] Reciprocal inquiry card built once, used on S6 and S13 (S18 voice pass only)
- [ ] S13 response choices: say, draw, write, act, photo outside

## Phase 5. Salmon and relatives
- [ ] Species colors defined once as CSS custom properties, shared by S10 and S11
- [ ] S10 projection chart with threshold line
- [ ] S8 nested zoom (fish, reach, watershed, planet)
- [ ] S11 species cards, consistent species colors with S10, lightbox (D14)

## Phase 6. Constellation (S20)
- [ ] Rebuild per D15; labeled directional edges; node info; preset chains; camera orbit; keep the Ripple. Baseline: the current web's keyboard, aria-live, and reduced-motion behavior

## Phase 7. Concept briefs only (Patrick input before build) [hold]
- [ ] S9 Listening Well (hot and cool media, who speaks for a place); update the Lesson 2.1 cross-reference in the notes
- [ ] S12 One Forest, Many Eyes
- [ ] S15 Three Jobs, Three Scales overhaul
- [ ] S16 field-guide polish, multi-select stamps
- [ ] S17 Building a Fire mapping

## Phase 8. Place-based modules [hold until D27]
Seed inventory: planning/modules/SEEDS.md. One concept brief per module:
planning/modules/briefs/<id>.md. Decisions: planning/modules/PACKET-D27.md
(D27, D28 to D34 proposed). No authoring before 10/25/2026; no structural work
on the workshop page and no merge to main 10/21 to 10/24/2026. Module author:
Patrick A. Freeland, with ATNI Climate (not owner); license per D32.
Proposed build order (pilot first, per D27's default; the rest by readiness
and consent, each gated as noted):
- [hold] 8a Pilot: m-columbia-missing-is-not-zero (A; S; C0). Paper set by hand first, then the one-screen companion; build.py extended only as far as one flat docs/<id>.html needs (D27b); cc-slide-change for any socket-slide note; cc-release-check build, static, probe, offline; VERIFY, MEDIA-CREDITS, VOICE-PASS rows
- [hold] STOP: Patrick rehearses the pilot; then rules D27d (module skill or not)
- [hold] 8b m-columbia-three-jobs (I; S; C0 neutral cards). One card file shared with s16's neutral cards
- [hold] 8c m-columbia-reading-to-record (C; M; C0). Case pack after D31
- [hold] 8d m-cascades-rain-shadow (B; M; C1). D31, D33
- [hold] 8e m-columbia-snow-water-bank (D; M; C1). D31, D33; F1 (2015 precipitation) checked first
- [hold] 8f m-columbia-hazard-chain (K; M, or S as teaching model only; C0). CCIC Week 7 minutes split with 8e
- [hold] 8g m-columbia-coordination-web (L; M; C0). After D28; doors card legal rows checked
- [hold] 8h m-columbia-carbon-circle (J; M; C0). D31 (NOAA and Scripps terms)
- [hold] 8i m-columbia-now-and-ahead (F; M; C0 basin). D29, D31
- [hold] 8j m-columbia-listening-well (G; S; C0). After D4
- [hold] 8k m-columbia-ask-before-you-share (H; S; C0 method). After D30 and D28 item 3
- [hold] 8l m-columbia-salmon-relay (E; M; C1, Station 6 C2). After D25, D31 (DART), and the host Nation's word on Station 6
One module per session unless Patrick says otherwise.

## Deferred
- S22 Into Your Classroom (needs time with the source Google Doc)
- S23 Evaluation
- Student pages layer (D13)
- Hash URLs by slide id instead of position (only if Patrick wants it)
