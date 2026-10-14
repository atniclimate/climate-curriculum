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
separate Elder/Child blockquote. The locked line already carries both ideas,
so keeping the blockquote would repeat the Elder/Child thought on one slide.
Options:
  A. Locked line replaces both the paragraph and the blockquote.
  B. Locked line replaces the paragraph; keep the blockquote.
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
