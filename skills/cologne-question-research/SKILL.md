---
name: cologne-question-research
description: Research Sanskrit Lexicon / Cologne Digital Sanskrit Dictionaries editorial questions before changing source data. Use when an issue is labeled question, asks for scholarly judgment, compares readings across dictionaries or scans, lacks an exact correction, depends on the meaning of a local marker, abbreviation, tag, name, or editorial policy, or requires evidence before deciding whether a CDSL markup or text change is warranted.
---

# Cologne Question Research

## Core Rule

Separate evidence gathering from source editing. A question issue is complete only when the answer, uncertainty, and proposed next action are documented clearly enough for a human editor or later correction agent.

Before working, read `references/question-research-workflow.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Inspect the issue, repo status, `.ai_state.md`, and any cited files, scans, or dictionary entries.
2. State the research question in one sentence before collecting evidence.
3. Apply the semantic gate when a proposed correction depends on interpreting a marker, abbreviation, tag, name, or editorial convention:
   - State exactly what must be proven.
   - Check neighboring entries, parallel dictionaries, issue comments, source notes, scans, and generated output before recommending a patch.
   - If the meaning remains uncertain, classify as `needs-human-review`.
4. Gather primary local evidence first: source record, generated XML, scanned page references, neighboring entries, and parallel dictionary entries.
5. Use web research only for missing or external scholarly sources, and cite links used.
6. Classify the outcome:
   - `answer-only`: no data change is justified.
   - `ready-for-correction`: evidence supports a precise text, markup, or encoding change.
   - `ready-for-markup-batch`: evidence supports a recurring markup normalization.
   - `needs-human-review`: uncertainty remains or authority is insufficient.
7. If a correction is ready, leave an exact resume point for `$cologne-text-correction-pr` or `$cologne-markup-batch`; do not perform a risky edit in the same pass unless the user explicitly asked for it.
8. Update `.ai_state.md` with evidence checked, outcome, validation status if any, and the next issue or resume command.

## Output Shape

Lead with the conclusion, then list concise evidence. Preserve exact source snippets only as short quotes needed to identify the record. Include file paths, line numbers, issue links, scan page identifiers, and dictionary abbreviations whenever available.
