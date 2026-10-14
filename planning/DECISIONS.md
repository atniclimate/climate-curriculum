# Decisions

Open and settled decisions for the workshop. Claude proposes; Patrick rules.
Each entry: plain-language question, options, default, ruling.
Change "Ruling" from PENDING to the choice once Patrick decides. Never fill a
ruling on Patrick's behalf.

D1 to D7 come from the 10/14/2026 revision notes. D8 onward were added when the
launch prompt was reconciled with those notes.

---

## D1. Four Questions overview title
Options: "Four Questions, One River" (current) or "Four Directions, One River."
Default: Four Directions, One River.
See D8 and D9: Patrick's new title-slide line already opens with
"Four Directions, one River," which may settle this.
Ruling: PENDING

## D2. Where the Elder/Child line lives
Options: title slide only, or Ways of Knowing (S12) only.
Default: title slide only; remove from S12.
See D8: the new title-slide line carries the Elder/Child idea itself.
Current occurrences on the page: S1 paragraph, S2 blockquote, S12 "Where They
Meet" and S12 speaker notes.
Ruling: PENDING

## D3. Q1 card wording
Options: "forces" or "conditions"; "water vapor" or "moisture"; add the
balancing sentence ("The same arrangement builds fog in the valley...") or not.
Default: forces, water vapor, add the sentence.
Ruling: PENDING

## D4. New title for "Four Things You Might Hear" (S9)
Options: Listening Well; Who Is Speaking?; Before You Believe It; Hot, Cool, and Loud.
Default: Listening Well.
Ruling: PENDING

## D5. Attribution of "We are not born into this world; We are born out of it..."
Closely echoes Alan Watts. Options: credit on slide, credit in slide notes,
adapt, or leave as Patrick's phrasing.
Default: small attribution note in the slide notes.
Ruling: PENDING

## D6. Title for "Which Job Is It Doing?" (S16)
Options: What Job Is It Doing?; Name That Job; Sort the Work; Field Guide to Climate Action.
Default: What Job Is It Doing?
Ruling: PENDING

## D7. "Speed of Trust" credit
Associated with adrienne maree brown's "move at the speed of trust."
Options: on-slide credit, teacher-notes credit, none.
Default: no on-slide credit; mention in teacher notes.
Ruling: PENDING

---

## D8. Title slide (S1) text
Patrick supplied this line directly (LOCKED, his line breaks):

    Four Directions, one River. When you can communicate in a
    respectful way, where both an Elder and a Child can understand;
    this is the surest sign that you are able to share knowledge.

The revision notes offer a different DRAFT paragraph for S1 and keep a
separate Elder/Child blockquote. The locked line already carries both ideas.
Correction (10/14/2026, from the source): the blockquote ("Think... when both
an Elder and a Child can understand, then this is where learning happens.")
is on S2, above the Four Questions, not on S1. S1 has only the paragraph.
Options:
  A. Locked line replaces the S1 paragraph; the S2 blockquote is removed.
  B. Locked line replaces the S1 paragraph; the S2 blockquote stays.
Casing: "one River" as typed, or "One River" to match title case elsewhere.
Default: A, with "One River."
Ruling: PENDING

## D9. Second slide (S2) title
Patrick supplied (LOCKED): "To seek understanding is less about being told"
If S1 now opens with "Four Directions, One River," then using the same words
as the S2 title repeats it. Patrick's new title pairs naturally with the
locked series line at the bottom of S2 ("Learning happens best when we are
curious, not rushed...").
Options:
  A. S2 title becomes "To seek understanding is less about being told";
     "Four Directions, One River" lives on S1 only. (Settles D1.)
  B. Patrick's line becomes S2 subtitle under a D1 title.
Also: trailing punctuation as typed (none), or end with a period.
Default: A, no trailing punctuation.
Ruling: PENDING

## D10. Split source/template.html into modules
The cloud tool, constellation, zoom, and charts will make one template file
very large. Options:
  A. Split into source/slides/*.html, source/css/, source/js/; build.py
     stitches them into the same single offline docs/index.html.
  B. Keep one template file.
Default: A, done once, before the cloud rebuild, with the build output
verified byte-for-byte equivalent in behavior.
Ruling: PENDING

## D11. Animation libraries for cloud morphing
Options:
  A. Hand-written: metaball paths for cumuliform clouds plus simple
     point-interpolation tweens. No dependencies.
  B. Vendor flubber.js (check license) for path morphing.
  C. Vendor GSAP with MorphSVG (check current license terms first).
Default: A first; B only if A cannot do the job on a Chromebook.
Ruling: PENDING

## D12. Commit the planning/ folder?
GitHub Pages serves only docs/, so planning files will not appear on the
live site, but the repo is public.
Options: commit planning/; or add planning/ to .gitignore and keep it local.
Default: commit it; it is the development record.
Ruling: PENDING

## D13. Separate student pages (docs/students/) beyond the workshop
Options: build now; or later, after the workshop slides themselves become the
K-12 interactive.
Default: later.
Ruling: PENDING

## D14. Embedded videos (S11 lightbox, S17)
Videos need the internet, but the workshop must run offline.
Options: privacy-enhanced YouTube embeds (youtube-nocookie.com) that show a
poster image and a plain link when offline; or links only.
Default: privacy-enhanced embed with offline poster-and-link fallback;
creator permission recorded in MEDIA-CREDITS.md.
Ruling: PENDING

## D15. Graph engine for the Constellation (S20)
The notes call for reusing the engine from I:\community-connector, simplified.
Options: copy a trimmed version into source/js/ with a note of its origin;
or reimplement a small force layout informed by it.
Default: decide after the session reads community-connector and reports its
size, dependencies, and license.
Ruling: PENDING

---

D16 onward were added on 10/14/2026 from the deep review of the source; they
gate Phase 1 steps 1b and 1d.

## D16. Word budget for Part divider (Hall) slides
The stylesheet notes hall copy at forty words or fewer so it sits on the photo
scrim. The locked Q2, Q3, Q4 texts are 44 to 49 words; pairing them with other
lines (S7 thesis, S14 fire draft) reaches 60 to 95 words.
Options: dividers carry the Q text only and raise the budget to about 50
words, strengthening the scrim; or dividers carry a short form and the full Q
text stays on the S2 cards.
Default: Q text only, budget about 50 words, stronger scrim.
Ruling: PENDING

## D17. S3 Part One divider text
Options: Q1 locked card text; or the short thesis (DRAFT) "Temperature,
pressure, and water vapor. When they meet, a cloud is born."
Default: Q1 locked text, so every divider matches its S2 card.
Ruling: PENDING

## D18. S14 Part Three divider: the fire line
The notes offer DRAFT A, B, or C (spark and fire) to pair with Q3.
Options: A, B, or C on the divider with Q3; or Q3 on the divider and the
chosen fire line moves to S15 or the speaker notes.
Default: Q3 on the divider; fire line A in the speaker notes until the S17
Building a Fire work settles the metaphor.
Ruling: PENDING

## D19. Where the S10 DRAFT intro goes ("Every salmon carries a map home...")
The map and stop cards fill S10 at 1366x768; a visible paragraph would clip.
Options: speaker notes; first stop card; a short visible line with the rest
in the notes.
Default: speaker notes until the Phase 5 chart work reshapes the slide.
Ruling: PENDING

## D20. Scope of capitalizing "Knowledge"
The house style says capitalize Knowledge, but the guiding document and the
notes write "intergenerational knowledge" and "knowledge holders" in lower
case (5 places on the page now).
Options: capitalize every use; or capitalize only Indigenous Knowledge,
Traditional Knowledge, and similar proper uses.
Default: proper uses only.
Ruling: PENDING
