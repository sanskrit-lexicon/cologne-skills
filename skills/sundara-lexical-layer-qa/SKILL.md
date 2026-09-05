_Created: 03-07-2026 · Last updated: 05-09-2026_

---
name: sundara-lexical-layer-qa
description: Review and maintain Sundara lexical, etymology, and cross-text annotation layers in CommentaryStrategies. Use when a GitHub issue, PR, or local task asks an agent to QA lexical notes, rejected candidates, density targets, adversarial gate behavior, lemma deduplication, review_required flags, recap-chapter low yield, or generated Sundara corpus/HTML counts.
---

# Sundara Lexical Layer QA

## Core Rule

Preserve the quality gate. Accepted lexical notes should be non-obvious, evidence-backed, deduplicated at the intended scope, and marked for human review when the layer requires it. Rejected candidates are evidence, not trash.

Before editing or judging notes, read `references/sundara-qa.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Inspect `CLAUDE.md`, `SUNDARA_COMMENTARY_RATIONALE.md`, `.ai_state.md`, and the target `data/lexical/` chapter files.
2. Identify the layer: base, lexical/etymological, or cross-text; do not mix acceptance criteria between layers.
3. Check accepted notes against the adversarial gate and rejected logs before adding, removing, or restoring notes.
4. Preserve `review_required:true` where the layer is explicitly marked for human editorial review.
5. Recompute or report density and dedup implications when changing chapter totals or book totals.
6. Run `python scripts/validate.py` after data/content edits and record any generated corpus/HTML refresh still needed.

## Stop Conditions

Stop and leave a research note when evidence is insufficient, a note requires Sanskrit-commentary OCR not yet available, a low-yield recap chapter may be correct by design, or a change would remove rejected-candidate audit evidence.

## References

- Read `references/sundara-qa.md` for QA regimes, acceptance criteria, and reporting expectations.

_Dr. Mārcis Gasūns_
