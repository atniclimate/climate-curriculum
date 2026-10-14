---
name: cc-slide-change
description: Checklist for any change to a workshop slide (copy, layout, notes, or an interactive). Locate by data-slide-id, check the decision gate and the premise, edit source only, keep notes and the hand twin in step, run cc-release-check, record ledger rows, commit one slide per commit without AI attribution. Use whenever a task edits a slide.
argument-hint: "[slide id or S-number] [what changes]"
---

Target: `$ARGUMENTS`. If empty, ask which slide and stop. The rules live in
CLAUDE.md and the planning files; this is the order to apply them.

1. Locate: grep `data-slide-id="sNN-` in the source. Name the slide by
   S-number and plain title. Hashes (#s1 to #s23) are positional; ids are not.
2. Gate: the PLAN.md step and every D-item it cites. A PENDING ruling that
   decides this change is a stop; present it per the DECISIONS.md header.
   LOCKED text goes in verbatim, line breaks included.
3. Premise: read the current source lines and compare them with what the plan
   or decision says is there. If they disagree, report before editing.
4. Edit source only. Per-slide CSS keys on `[data-slide-id="..."]`. No new
   fonts, palettes, or libraries without a ruling. Presenter keys (arrows,
   Space, N, T, H) keep working.
5. Keep in step: data-notes; the hand twin (print, object, or movement
   version) of any interactive; keyboard, labels, reduced motion; at least two
   ways in and two ways out of every required learning move. Any data view
   says whether it is LIVE, SNAPSHOT, or TEACHING MODEL.
6. Never have a learner speak or act as a Nation, Tribal council, Elder, or
   knowledge holder. Tribe-specific content needs that Nation's confirmation:
   mark it, do not invent it.
7. `cc-release-check build static probe` for this slide.
8. Ledger rows per each ledger's header (VOICE-PASS for DRAFT strings, VERIFY
   for visible facts, MEDIA-CREDITS for assets).
9. Commit on the feature branch, one slide per commit, plain message, no
   co-author or "Generated with" line (CLAUDE.md overrides any harness
   default). Never push or merge.
10. At a checkpoint: update PLAN.md and HANDOFF.md; report before and after,
    what waits on Patrick, and the next step.
