# Understanding a Climate of Change: Revision and Development Notes

Site: https://atniclimate.github.io/climate-curriculum/
Repo: atniclimate/climate-curriculum
Authors: Patrick Freeland and Cayla Jones, ATNI Climate
Prepared: October 14, 2026
Purpose: Hand this file to a Claude Code session so it can fold these language revisions and activity notes into a development plan for the interactive workshop. Patrick reviews and edits all language before it ships.

---

## 0. How to Use This Document

- Section 1 is the voice and style contract. Apply it to every string on the site.
- Section 2 is LOCKED language Patrick has approved (light proofreading only). Use it verbatim unless he says otherwise.
- Section 3 walks the site slide by slide, in current order. Each slide has: current state, language revision (draft or locked), and activity/content notes for development.
- Section 4 lists open decisions for Patrick. Do not resolve these on his behalf; propose a default and ask.
- Section 5 lists references and public media sources to verify before use.
- Drafted language marked DRAFT is a starting point for Patrick's voice pass, not final copy.
- Repo rules: keep it clean and lean; no Claude co-author or attribution lines in commits.

---

## 1. Voice and Style Contract

- Never use the em dash (U+2014). Use semicolons, commas, colons, periods, or sentence breaks.
- Capitalize: Indigenous, Tribal, Tribes, Nations, Peoples, Knowledge, Elder, Beings. Patrick also capitalizes Trust in the Part Four line; keep it.
- Relational framing: who, how, when, why, with whom. "Relatives, not resources." Sovereignty is the organizing principle, not technical novelty.
- Succinct. Let sentences land. Layered prose with an occasional single short line for emphasis.
- Direct and encouraging; no hedging, no lecturing. "Gentle instruction": invite thinking about thinking.
- Audience is both teachers and students (K-8 readable, still deep). Plain words first; technical terms introduced as actions or images.
- Avoid common AI diction (no "delve," "tapestry," "journey" as filler, "unlock," "empower," etc.). Note: "journey" IS intentional for the salmon.
- Uniform text blocks: sibling cards on the same slide should carry roughly equal word counts so boxes render the same size. Target noted per slide.
- Scale language is Frog's Eye, Bird's Eye, Moon's Eye.
- The Elder/Child line ("when both an Elder and a Child can understand...") is already used; keep it in ONE place only (currently it appears on the title slide twice and again on Ways of Knowing). See Decision D2.

---

## 2. Locked Language (approved, proofread)

### 2.1 Series line (replaces the "There is no test here..." line on the Four Questions slide)

Patrick's text, proofread:

> Learning happens best when we are curious, not rushed. Education is not a race. A good question does not sit still, and the best questions lead to more questions; a trickle becomes a river.

Proofreading notes: "the best questions that lead to questions" tightened to "the best questions lead to more questions"; "a a trickle to a river" corrected. Alternate ending if Patrick prefers his original image: "...lead to more questions, the way a trickle finds its way to a river."

### 2.2 The Four Questions (card text on the overview slide and Part dividers)

Target: about 40 to 50 words per card so the four boxes render evenly. Word counts in brackets.

**1. How Does a Cloud Work?**

> A cloud forms when three forces converge: temperature drops, pressure shifts, and water vapor condenses. That is it; just relationships. Once you see that pattern, you start seeing it everywhere: connection. [32]

Proofreading notes for Patrick:
- "humidity condenses" changed to "water vapor condenses." Humidity is a measure of water vapor; the vapor is what condenses. Alternate: "moisture condenses."
- Temperature, pressure, and moisture are conditions more than forces. Optional: "three conditions converge." Keep "forces" if the rhythm matters more.
- "everywhere; connection" changed to a colon so the single word lands as the payoff.
- Card is short of target. Optional balancing sentence (DRAFT), inserted after "just relationships.": "The same arrangement builds fog in the valley, snow on the ridge, and storms off the coast." [brings card to ~48]

**2. How Do You Know What You Know?**

Patrick liked this one. Tightened to target length:

> Step outside. What feels different this season compared to last? What you notice in your backyard, your watershed, and your community connects to the graphs, maps, and numbers scientists use. Knowledge comes from many directions; some lives in data, some lives in the people and places closest to you. [49]

Thesis line (optional, italic): "What you notice with your own eyes matters. So does what others have learned before you."

**3. What Can We Do?**

> Words can be uncomfortable, and that is okay. Not knowing the language is not the same as not understanding. *Mitigation* is planting a tree. *Adaptation* is moving the garden to higher ground. *Resilience* is the community that rebuilds, remembers the past, and thinks of the generations ahead. [47]

Proofreading notes: comma added before "and thinks"; the three terms italicized so they read as the "big words" being unpacked.

**4. How Do We Work Together?** (heading line "Relationships Matter." stays)

> Relationships Matter. Relationships are built at the speed of Trust. Positive change starts with listening, then sharing what we know. Everyone carries responsibilities, but no one has to carry them alone. Everyone contributes something important; every perspective adds detail. That is how good work gets done. [46]

Proofreading notes: "doesn't have to carry them alone" given a subject ("no one has to"); period added at the end. Fully positive alternate for that sentence: "Everyone carries responsibilities, and we carry them together."

---

## 3. Slide by Slide

Slide order below follows the live site. "Current" summarizes what is there now.

### S1. Title Slide

Current: Title "Understanding a Climate of Change"; line "Four questions, one river. Shared with respectful communication so that both an Elder and a child can understand..." plus the Elder/Child blockquote.

Language: Keep title. The Elder/Child idea appears twice here; keep the blockquote and shorten the paragraph (see D2). DRAFT paragraph: "Four questions, one river. A workshop for teachers and students, shared so that each of us can pass it on."

### S2. Four Questions Overview

Current title: "Four Questions, One River."

Language:
- Title decision D1: "Four Questions, One River" (current) vs "Four Directions, One River" (Patrick's alternate).
- Replace the four card descriptions with Section 2.2 text.
- Replace the closing "There is no test here..." line with Section 2.1.
- Themes chip row: keep; update scale chip to "Scale: Frog's Eye, Bird's Eye, Moon's Eye."

Dev: enforce equal card heights in CSS (grid with align-items: stretch) as a backstop, but the copy itself is balanced.

### S3. Part One Divider

Current text is the old cloud question ("Have you ever looked up...").

Language: Replace with Q1 locked text (Section 2.2), or the short thesis form: "Temperature, pressure, and water vapor. When they meet, a cloud is born."

### S4. Cloud Tool: "Follow the Air from the Ocean over the Mountains" (#s4)

Current: ocean-to-Plateau cross section (Coast Range, Cascades), seasons, Atmospheric River toggle, sliders for coast air temperature and ocean humidity, "Warm the world 2 C," readouts.

Development notes (same functionality, better experience):

Controls and layout
- Simplify the control cluster. Fewer visible sliders at once; group them as Temperature, Pressure, Moisture (the three conditions from Q1), plus Season and a Wind/Jet Stream toggle.
- Use the wide side margins for a live "What is happening" panel: plain-language text that updates as sliders move (e.g., "The air is cooling as it climbs the Cascades. It can no longer hold all its water. Clouds are forming; rain on the windward side, a rain shadow beyond."). Large, readable type; one or two sentences at a time.
- The panel names the cloud type currently forming, its level (low, middle, high), and why.
- Keep the readouts (air temperature, water carried, water it can hold, reaching the ground) but visually tie them to the panel.

Cloud rendering
- Move beyond primitives (circles and ellipses). Each cloud type gets a shape vocabulary that matches its real structure, and clouds morph (tween) between types as conditions change rather than popping in and out.
- Cover the ten WMO genera by level (heights for temperate regions per the WMO International Cloud Atlas):
  - High (about 5 to 13 km): Cirrus (fibrous wisps), Cirrocumulus (small grains, ripples), Cirrostratus (thin veil, halo).
  - Middle (about 2 to 7 km): Altocumulus (rolls and patches), Altostratus (gray sheet, sun as through frosted glass), Nimbostratus (thick, rain-bearing layer).
  - Low (surface to about 2 km): Stratus (flat gray layer, fog lifted), Stratocumulus (lumpy layer), Cumulus (fair-weather heaps), Cumulonimbus (towering storm cloud with anvil; spans all levels).
- Add lenticular clouds (species lenticularis): smooth lens shapes standing over and downwind of peaks (Mount Rainier, Mount Hood, Mount Adams are perfect local anchors). Show they stay in place while wind flows through them.
- Multiple simultaneous layers: low, middle, and high decks visible together, each responding to its own temperature and wind.
- Techniques to evaluate (pick what performs well on school Chromebooks):
  - SVG path morphing between authored keyframe shapes per genus (interpolate path points; flubber.js or GSAP MorphSVG-style approach; confirm license).
  - Metaball/blob paths for cumuliform clouds (connected circles generated as a single path), which tween smoothly.
  - SVG feTurbulence + feDisplacementMap filters for soft edges and wispy texture (use sparingly; filters are expensive).
  - Canvas or WebGL noise-based layer if SVG is too slow; keep an SVG fallback.
  - Reference for the overall idea: "Procedural Cloudscapes" (Webanck et al., Computer Graphics Forum 2018) models cloud types over altitude and animates by morphing between keyframes rather than simulating physics. Same philosophy at a classroom scale.
- Art direction: soft, painterly, consistent with ATNI Climate design system; light from the sun side, shaded undersides on thick clouds; darker bases as clouds thicken toward rain.

New atmospheric features
- Jet stream and wind by altitude: animated streamlines or particles whose speed and direction vary by height. Show how wind shear stretches cirrus, builds lenticulars over peaks, and steers storms. Reference earth.nullschool.net (already linked) as the "real sky" companion.
- Sunlight as a storm driver: a sun-angle or time-of-day control. Surface heating builds rising thermals, cumulus grows into cumulonimbus in summer afternoons east of the Cascades. Tie to wildfire-season lightning without being alarming.
- Broader ocean on the left: more visible Pacific, with evaporation shown rising off warm water; atmospheric river arrives as a moisture plume.
- Keep the seasonal switch and sea-level-to-mountain landscape with rain vs snow line; snow line rises with "Warm the world 2 C."

Ask the room: keep "Which side of the mountains do you live on, and what does that mean for your rain and snow?"

### S5. Same Gauges, Longer Time

Current: four instruments (Rain Gauge, Thermometer, Water Quality, Soil), click for focus; "One reading is weather; thirty years of the same readings is climate."

Development notes:
- More interactive: students "take a reading" by clicking the gauge; readings stack into a growing record; after enough readings, a pattern line appears (weather becomes climate before their eyes).
- Show how data becomes knowledge, framed as a journey that parallels the salmon: a single reading leaves the gauge, travels upstream through a record, joins other readings, becomes a pattern, becomes knowledge someone acts on (e.g., a drought declaration on the Dynamic Drought Module). Visual: droplet or data point traveling a small river of steps: Reading, Record, Pattern, Knowledge, Decision.
- Keep links to earth.nullschool.net and the ATNI Dynamic Drought Module.

Language (DRAFT): "Every reading starts small, like a single drop. Gathered over years, the drops become a river of knowledge, and a river of knowledge can guide a decision."

### S6. Part One Carry Forward

Current: Key Lesson, Key Takeaway, three reflection questions.

New approach: reciprocal inquiry. Encourage first. The format models respect and reciprocity between teacher and student, or between partners.

Framing text (DRAFT):
> Let's carry this forward together. I'll ask you a question. If you don't know, that's okay; we'll talk it through until it makes sense. Then you ask me a question. If I don't know, we'll talk it through together. That is how we learn from each other.

Interaction: a card that flips between "My question for you" and "Your question for me," with a prompt bank students and teachers can draw from (e.g., "Why does it rain more on one side of the mountains?", "Where does a cloud go when it disappears?"). A "Let's talk it through" step reveals a gentle hint, not an answer.

Simplified questions (DRAFT):
1. What is one thing about clouds or weather that makes more sense now?
2. What surprised you?
3. What do you still wonder about?

Visual: soft cloud background graphics (reuse the new cloud art).

Key Lesson and Takeaway: keep content; tighten later in Patrick's voice pass.

### S7. Part Two Divider

Current: "With your own senses you can see the snow in the winter. How do we learn about weather and climate in the classroom, and in the media, and why do we trust them?"

Language: Replace or pair with the Q2 locked text (Section 2.2).

### S8. Frog's Eye, Bird's Eye, Moon's Eye

Current headings: "At the Water," "Above the Land," "The Whole Planet."

Language: Headings become simply Frog's Eye, Bird's Eye, Moon's Eye (remove the sub-labels). Equal-length text blocks, ~40 words each.

DRAFT copy:
- **Frog's Eye.** Up close, the river speaks through your hands and feet. Cold water, a fast current, a salmon holding in the shade of a log. Salmon need water cool enough and flowing enough to breathe, travel, and spawn; small changes here matter.
- **Bird's Eye.** From above, you see how it all connects. Snow on the ridge feeds the creek; the creek feeds the river; shade and side channels keep the water cool. A watershed is one body, and every part shapes the whole.
- **Moon's Eye.** From far away, the whole planet moves as one system. Oceans warm, the atmosphere carries heat and water across continents, and satellites measure snow and ice from space. What happens there reaches all the way back to the river.

Development notes:
- Nested zoom interaction ("powers of ten" feel): start on a single salmon in a frame. Click the fish and the view pulls back so the fish becomes a small part of a larger image (the stream reach), then the watershed, then the planet. Each zoom level shows the matching text block.
- Frog's Eye detail panel: salmon reliance on stream temperature and flow. Commonly cited guidance: water above roughly 68 F (20 C) is stressful for migrating salmon, and sustained warmer water can block migration or be lethal. Verify thresholds and source (EPA Pacific Northwest temperature guidance, CRITFC, NOAA Fisheries) before publishing.
- Needs further design thinking; this is a working outline.

### S9. Four Things You Might Hear (rework)

Current: four statements with Notice / Ask / Check scaffold.

New direction: shift from fact-checking claims to understanding HOW messages reach us and why some grab us before we think. Keep the Notice / Ask / Check scaffold; it is good.

Concept threads to develop:
- Hot and cool media (Marshall McLuhan): hot media fill in everything for you and leave little room to participate; cool media ask you to fill in the gaps and engage. Which do you learn more from? Which makes you feel more?
- Hype and the attention economy: feeds designed to keep you scrolling; outrage and fear travel faster than calm; the feeling arrives before the facts.
- Who is speaking for a place: listening to people who are not from a place, or do not know it, vs. those who live it and carry its knowledge. Who has the right to tell this story?
- Talking points: repeated phrases that stand in for thinking; noticing when someone is reciting rather than reasoning.

Title options: "Listening Well," "Who Is Speaking?", "Before You Believe It," "Hot, Cool, and Loud."

Framing text (DRAFT, voice pass needed):
> Some messages shout. Some whisper and ask you to lean in. Some come from people who know a place by heart; others come from far away, repeating what they were told. Before you carry a message forward, notice how it reached you and how it made you feel.

Activity ideas: sort example messages (a viral post, an Elder's story, a news headline, a talking point, a slow documentary) along two axes: hot to cool, and from-this-place to from-far-away. Keep the existing four statements as optional examples within the new frame.

### S10. The Journey Home becomes "The Salmon's Journey"

Current: Columbia Basin map with dams, Celilo Falls, August water temperature, SSP2-4.5 / SSP3-7.0, 2040-2069 / 2070-2099, flow at The Dalles.

Language: Title "The Salmon's Journey." Describe the natural pull home, the blockages, and the three jobs. DRAFT:
> Every salmon carries a map home. It is pulled upriver by memory, by scent, by something older than any of us. Along the way it meets dams, warm water, and low flows. Adaptation helps it get through what is already here. Mitigation keeps the river from getting harder. Resilience is opening the way home; when dams come down, the river remembers.

Notes:
- Tie Adaptation, Mitigation, Resilience explicitly to the journey (Patrick: RESILIENCE as dam removal). Real anchors to verify: Elwha River dam removals (completed 2014) and the Klamath River dam removals (completed 2024), with salmon returning in both.
- Second pass on language in Patrick's voice; current descriptions are placeholders.

Development notes:
- BUG: river lines do not align with the basemap; fix the SVG path registration.
- Projection visual: add a temperature time series, 1990 historical baseline with a shaded historic range band, smoothed averages for SSP2-4.5 and SSP3-7.0, and visible year-to-year variance so students see that a warmer average means more frequent extreme heat days and drought years. Mark the salmon stress threshold as a horizontal line.
- Data sources to evaluate: NorWeST stream temperature (USFS), Columbia River DART, CMIP6 downscaled projections used elsewhere in the ATNI portfolio. Cite clearly on the slide.

### S11. Relatives of the River (working draft)

Current: Patrick Luke quote (Yakama Nation, via Steve Robinson) and species display.

Language (DRAFT intro):
> These are our relatives. They have fed us, taught us, and carried our stories for generations. Each one needs something a little different from the river; when the river changes, each one feels it in its own way.

Development notes:
- More detail per species: Chinook, coho, sockeye, chum, steelhead, Pacific lamprey, white sturgeon, suckers (matching the Patrick Luke quote), with optional bull trout and freshwater mussels.
- Each card: what it needs (temperature, flow, habitat), when it travels, what threatens it, and a cultural note to be confirmed with Tribal partners.
- Color differentiation per species (consistent across this slide and The Salmon's Journey).
- Click a species to open a lightbox with photos or short video from publicly licensed sources. USFWS media library publishes many images marked Public Domain (including Pacific lamprey photos with Yakama Nation Fisheries staff). Check each item's license line and credit the photographer.
- Cultural content: confirm with each Nation before classroom use.

### S12. When Ways of Knowing Meet (new approach)

Current: three columns (Observation and Memory, Instruments, The Relatives Themselves) plus the Elder/Child line in "Where They Meet."

New direction: sensory, tactile, perspective-taking. Distinguish local knowledges from Traditional Knowledges; include intergenerational knowledge and lived experience; show frames of reference and where they converge.

Signature activity concept: "One Forest, Many Eyes" (working title)
- One illustrated or photographed forest scene. Students switch lenses and the SAME scene transforms:
  - Ecologist: species labeled and differentiated, canopy layers, snags, understory, signs of fire and water.
  - Artist: forms, shapes, light, color, rhythm; pareidolia (faces and figures hidden in bark and branches) as a playful layer.
  - Home: pathways, gathering places, berry patches, a favorite tree, memories pinned to places ("this is where Grandma showed me...").
  - Elder or Storyteller: names in the language (with permission), seasonal rounds, stories tied to places.
  - Child or Play: hiding spots, climbing trees, sounds, smells.
- "Where They Meet" overlay: toggle all lenses at once to show convergence; each lens sees something real the others miss.
- Tactile classroom version: students each describe the same object or outdoor spot from an assigned lens, then compare.
- Sensory prompts: what do you hear, smell, feel underfoot?

Language (DRAFT):
> The same forest is many places at once. An ecologist sees who lives here. An artist sees shape and light. A family sees home, with paths worn by generations. None of these is wrong. Where they meet, we see more than any one of us could alone.

Remove the Elder/Child line from this slide if it is kept on the title slide (D2).

### S13. Part Two Carry Forward

Current: Key Lesson, Key Takeaway, three questions.

Development notes: more approachable and accessible for different learning styles; follows up directly on the lesson (scale, media, salmon, ways of knowing). Offer choices for how to respond: say it, draw it, write it, act it out, or take a photo outside. Optionally reuse the reciprocal inquiry card from S6 for consistency.

Simplified questions (DRAFT):
1. Who do you trust to tell you about your river, and why?
2. What did you see differently today?
3. What is one question you want to take outside with you?

### S14. Part Three Divider: What Can We Do?

Current: "When people come to understanding, people take action..."

Patrick's direction: "When people come to understanding they can build upon shared values (no matter how few at first). This is the spark that builds into the fire. When people have the (energy and warmth / people take action)..."

DRAFT options:
- A: "When people come to understanding, they can build upon shared values, no matter how few at first. That is the spark. Shared work is the kindling. When people gather around the warmth, they take action."
- B: "Understanding is a spark. Shared values, even a few, are the tinder that catches it. Tend it together, and the fire gives warmth and light enough for everyone to act."
- C: "Every fire starts small. One shared value, one conversation, one person who understands. Feed it with care, and soon there is enough warmth to gather around and enough light to see the way forward."

Pair with Q3 locked text.

### S15. Three Jobs, Three Scales (complete overhaul)

Current: three columns (Adaptation, Mitigation, Resilience) with You / Family / Community bullets.

Development notes:
- Overhaul visually and interactively; currently text-heavy.
- Idea: a scale slider or zoom (You, Family, Community, Nation) that changes the scene while three "job" lenses highlight what each action does. Ties to Frog's Eye / Bird's Eye / Moon's Eye scale language.
- Use the Q3 images as anchors: planting a tree (Mitigation), moving the garden to higher ground (Adaptation), the community that rebuilds and remembers (Resilience).
- Keep the closing line idea (adapt now to be resilient; mitigate now for future generations) for Patrick's voice pass.

### S16. Which Job Is It Doing? (keep; polish)

Current: sort actions into A / M / R; no score; note that most actions do more than one job and some "solutions" cause harm without consent.

Patrick: great; reminds him of a kids' activity at a national park.

Title options: "What Job Is It Doing?", "Name That Job," "Sort the Work," "Field Guide to Climate Action."

Development notes:
- Visual flair: field-guide or Junior Ranger feel; badges or stamps for each job; cards that flip to reveal how an action does more than one job.
- Allow multi-select (an action can earn A, M, and R stamps).
- Close language pass in Patrick's voice. Keep the consent caveat and the Steve Robinson case attribution.

### S17. From Knowing to Doing (integrate "Building a Fire")

Current: six steps (Observe, Plan, Brief, Fund, Watch Policy, Act and Monitor) mapped to ATNI tools; sovereignty-first note.

Development notes: integrate Patrick's Building a Fire method; the metaphor maps cleanly onto the six steps. DRAFT mapping (Patrick to confirm and tune to real ideation-to-action examples):
- Spark: Observe; noticing what is changing (Dynamic Drought Module).
- Tinder: shared values; what matters most.
- Kindling: Plan and Brief; small, dry, ready pieces a council can catch (Plan Assessor).
- Fuel: Fund; the resources that keep it burning (TCR Policy Scanner).
- Air: Watch Policy; the conditions that let the fire breathe or smother it (Policy Sentinel).
- Tending: Act and Monitor; keep it going, carry the coals back to the start.
- Add space for embedded videos (YouTube via privacy-enhanced embeds) and links to articles showing real Tribal examples. Confirm permissions and that each video's creator allows embedding.
- Keep the sovereignty-first note verbatim.

### S18. Part Three Carry Forward

No changes requested. Include in the voice pass.

### S19. Part Four Divider: How Do We Work Together?

Current: quote "We will always be better than I ever will be." then "No single person, scientific report, or action plan has all the answers."

Language: Keep the quote. Replace the negative line with Q4 locked text (Section 2.2).

### S20. The Web Moves Together becomes a Constellation

Current: three rings (water at center, relatives, people and responsibilities) with "Send a Ripple" and a select-any-relative interaction.

Development notes:
- Rebuild using the graph engine from I:\community-connector (simplified). The dev session must inspect that repo first; this note does not describe its API.
- Rename concept: a constellation; nodes as stars.
- Better-mapped edges: relationships labeled and directional where meaningful (feeds, shelters, teaches, depends on).
- Click a node for real-world information (a species, a place, a role, an institution).
- Preset chains as buttons (e.g., Snowpack to River to Salmon to Families to Ceremony) that light up a path.
- Camera orbit to highlight a selected chain; constellation reconfigures around the selected node.
- KEEP the Ripple; Patrick likes it a lot. Improve the relationships it travels along.
- Ask the room stays: "Which relative are you closest to, and who holds you up?"

### S21. Part Four Carry Forward (closing words)

Language (locked, Patrick's line breaks):

> We are not born into this world;
> We are born out of it...

> Go Outside. Pay Attention.
> Be a Good Relative. Be a Good Ancestor.
> Be Kind to Others. Be Kind to Yourself.
> Together, we have all that we need.

Note D5 on attribution of the first line.

### S22. Into Your Classroom

Current: three cards (Grades 6 to 12; 200 Level; 201 Level), resource links, working-with-Tribes note.

Development notes:
- Add document downloads (lesson plans, syllabi) and email links for contact.
- Needs time with the source curriculum (Google Doc "Climate Change & The Tribes Curriculum": PF Presentation tab, 2025 Youth Summit tab, NESC 215 syllabus) to better position this slide. Defer detailed copy until then.
- Keep the working-with-Tribes respectfully note verbatim.

### S23. Carry One Question Forward / Evaluation

Defer. Patrick will revisit after everything else is done and context is clearer. Do not redesign yet.

---

## 4. Open Decisions for Patrick

D1. Overview title: "Four Questions, One River" (current) or "Four Directions, One River." Default: Four Directions, One River (ties to the four parts and to relational orientation).
D2. Where the Elder/Child line lives: title slide only, or Ways of Knowing only. Default: title slide blockquote only; remove from the title paragraph and from Ways of Knowing.
D3. Q1 wording: "forces" vs "conditions"; "water vapor" vs "moisture"; add the balancing sentence or not. Default: "forces," "water vapor," add the sentence.
D4. Four Things You Might Hear: new title. Default: "Listening Well."
D5. "We are not born into this world; we are born out of it" closely echoes Alan Watts ("You didn't come into this world. You came out of it"). Credit, adapt, or leave as Patrick's own phrasing. Default: add a small attribution note in the slide notes.
D6. Which Job title. Default: "What Job Is It Doing?"
D7. "Speed of Trust" phrasing is also associated with adrienne maree brown's "move at the speed of trust." Credit or not. Default: no on-slide credit; mention in teacher notes.

---

## 5. References and Media Sources (verify before use)

Clouds
- WMO International Cloud Atlas, levels and genera: https://cloudatlas.wmo.int/en/some-useful-concepts-levels.html
- WMO Cloud Atlas descriptions of each genus and orographic influences: https://cloudatlas.wmo.int/en/cl-0.html
- AMS Glossary, cloud classification (genera, species incl. lenticularis, varieties): https://glossary.ametsoc.org/wiki/Cloud_classification
- Webanck et al., "Procedural Cloudscapes," Computer Graphics Forum 37(2), 2018 (morphing-based cloud animation by altitude): https://diglib.eg.org/items/b21d012a-0de6-4a20-b448-986755dca608/full
- SVG metaball path technique: https://varun.ca/metaballs
- earth.nullschool.net for live wind and jet stream (already linked)

Salmon and water
- NorWeST stream temperature (USFS), Columbia River DART, Fish Passage Center, CRITFC (already linked), NOAA Fisheries
- EPA Region 10 temperature guidance for salmonids (verify thresholds)

Species media (public licensing)
- USFWS media library, many items marked Public Domain (e.g., Pacific lamprey): https://www.fws.gov/media/pacific-lamprey-2
- Wikimedia Commons: check each file's license and author line
- NOAA Fisheries image galleries: verify license per item

Curriculum sources
- Freeland and Jones, Understanding an Ever Changing Climate
- Steve Robinson, Climate Change and the Tribes: Columbia River Edition (draft); confirm case details with each Nation
- Google Doc "Climate Change & The Tribes Curriculum" (PF Presentation tab, 2025 Youth Summit tab, NESC 215 syllabus)

---

## 6. Suggested Work Order for the Development Plan

1. Language swap (low risk, high visibility): Sections 2.1 and 2.2 on S2, S3, S7, S14, S19; S8 headings; S10 title; S21 closing words.
2. Bug fix: river line alignment on The Salmon's Journey.
3. Cloud tool rebuild (largest effort): control simplification and side panel first, then cloud shape system, then layers, jet stream, sunlight, broader ocean.
4. Carry Forward pattern (S6, S13): build the reciprocal inquiry card once, reuse.
5. Salmon's Journey projection chart.
6. Frog's Eye nested zoom; Relatives of the River species cards and lightbox.
7. Constellation rebuild from community-connector engine.
8. Concept work needing Patrick's input before build: Four Things You Might Hear, Ways of Knowing forest lenses, Three Jobs overhaul, Building a Fire integration.
9. Deferred: Into Your Classroom, Evaluation.