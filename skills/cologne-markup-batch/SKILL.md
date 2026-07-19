---
name: cologne-markup-batch
description: Prepare and execute Sanskrit Lexicon / Cologne Digital Sanskrit Dictionaries markup-normalization batches. Use when a GitHub issue or local task asks an agent to normalize XML-like tags, abbreviation markup, link markup, lexical markup, or recurring dictionary source patterns across CDSL repos such as csl-orig, PWG, PWK, MWS, AP90, SKD, VCP, WIL, SHS, or related correction staging repos, after any meaning-dependent marker, abbreviation, or tag interpretation has been resolved.
---

# Cologne Markup Batch

## Core Rule

Treat markup batches as correction work with a wider blast radius. Prefer small, inspectable batches; preserve dictionary text; and validate generated XML or ET parsing before considering the batch complete.

Before editing, read `references/markup-batch-workflow.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Inspect the issue, repo status, `.ai_state.md`, and candidate source files.
2. Classify the requested change as markup-only, text correction, encoding, bug, or editorial question.
3. Stop and switch skills when the task is not markup-only:
   - Use `$cologne-text-correction-pr` for dictionary wording/headword corrections.
   - Use `$cologne-question-research` for scholarly or editorial uncertainty.
4. Apply a markup-only preflight:
   - Continue only when the meaning of the tag, abbreviation, marker, or lexical convention is already clear.
   - If changes to `<ab>`, `<h>`, `<lex>`, `<info>`, or similar markup depend on interpreting dictionary meaning or editorial policy, use `$cologne-question-research` first.
5. Find examples with `rg`, then inspect nearby records before deciding the batch rule.
6. Create a minimal change file or script that records the exact before/after lines.
7. Apply the batch through the repo's established update workflow.
8. Validate with the narrowest available parser/checker, then run XML/ET generation when the source feeds dictionary XML.
9. Update `.ai_state.md` with the issue, files changed, validation command, and remaining candidates.
10. Commit logical milestones with `ai-wip:` when git access is available.

## Batch Boundaries

Prefer one issue, one dictionary, and one markup pattern per batch. Do not combine unrelated tag families just because they are easy to find in the same pass.

Do not silently edit scan-faithful files such as `printchange.txt` unless the task is explicitly about print deviation notes.
