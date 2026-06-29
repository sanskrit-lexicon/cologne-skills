---
name: cologne-text-correction-pr
description: Prepare and validate Sanskrit Lexicon / Cologne Digital Sanskrit Dictionaries text-correction pull requests. Use when a GitHub issue or task asks an agent to fix dictionary source text, headwords, encoding/transliteration text, or typo/scan-error corrections using CDSL updateByLine/change-file workflows, especially for csl-orig or dictionary repos such as AP90, MWS, PWG, PWK, SKD, VCP, WIL, SHS, and related correction staging repos.
---

# Cologne Text Correction PR

## Core Rule

Never edit a dictionary source casually. Use the local repo's correction workflow and validate XML before proposing or pushing a correction. If the issue body does not clearly identify old text, new text, dictionary, and target record or line, post findings or ask for clarification instead of guessing.

For `csl-orig`, source files are read-only by default in this local environment. Do not modify, stage, commit, or push `csl-orig` files unless the current user request explicitly authorizes that specific source change. Without that authorization, produce research notes, an exact change plan, validation plan, handoff instructions, or a PR review recommendation instead.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Resolve the target repo, dictionary code, issue number, and source file.
   - Prefer issue metadata and body.
   - For csl-orig sources use `csl-orig/v02/<dict>/<dict>.txt`.
   - For dictionary repos, inspect local conventions before assuming paths.
2. Inspect the issue shape.
   - Run `python scripts/inspect_issue.py OWNER/REPO ISSUE_NUMBER` from this skill to summarize candidate file/line/change clues.
   - Read the full GitHub issue and comments when the summary is ambiguous.
3. Check the correction registry before editing.
   - Do this before writing a change file, preparing a regex batch, applying `updateByLine.py`, or touching any source file.
   - Search `csl-corrections` CFR/batch files for the same dictionary, L number, headword, old text, and new text.
   - Treat registry statuses such as `No change` as authoritative unless a maintainer explicitly reopens the decision.
   - Decide whether an accepted correction should be a plain replacement or an inline correction layer such as `{{old->new||YYYYMMDD|author|issue|}}`.
   - Record the registry check and decision in the batch readme or handoff notes.
4. Classify the issue.
   - `text-correction`: source text, definition, headword, typo, scan-error, print-change decision already made.
   - `encoding`: SLP1/IAST/AS rendering or transliteration correction.
   - `markup`: tag structure rather than text content; route to markup workflow instead.
   - `question`: scholarly/editorial uncertainty remains; do not patch.
   - If the old/new decision depends on interpreting a marker, abbreviation, tag, name, or local editorial convention, stop and use `$cologne-question-research` first.
5. Create a change file.
   - Use paired `old` / `new` lines with exact original text.
   - Use `ins` or `del` only when insertion/deletion is explicitly required.
   - Preserve UTF-8 without BOM.
6. Apply via the local updater.
   - Prefer the repo's local `updateByLine.py` or the shared CDSL copy.
   - For csl-orig/csl-corrections audit flow, follow the org-level `AGENTS.md` sequence exactly.
7. Validate.
   - Run the repo's XML/build validation.
   - On local Windows without XAMPP, `make_xml.py` reporting `All records parsed by ET` is acceptable when the repo docs say so.
   - Verify no UTF-8 BOM was introduced.
8. Commit and publish.
   - Stage only the correction, change file, validation notes, and required repo journal updates.
   - Commit with `ai-wip:` unless the user requested another convention.
   - Push and open or link the PR/issue as appropriate.

## Stop Conditions

Stop before editing when:

- the target is `csl-orig` and the current user request has not explicitly authorized that specific source change;
- the issue asks for human scan/scholarly judgment that has not been supplied;
- old/new text is not exact enough to target one record safely;
- the old/new text depends on unresolved interpretation of a marker, abbreviation, tag, name, or local editorial convention;
- `csl-corrections` CFR/batch registry already records the proposed correction as `No change`, rejected, deferred, or otherwise not to be applied;
- you have not determined whether the correction should preserve the original through inline correction-layer syntax rather than plain replacement;
- the source file is missing locally and cannot be fetched without changing scope;
- XML validation cannot be run or substituted with a documented local equivalent.

In those cases, leave a concise finding with the missing evidence and update the relevant GTD/handoff tracker.

## References

- Read `references/cdsl-correction-workflow.md` before touching csl-orig or csl-corrections.
- Use `scripts/inspect_issue.py` for a first-pass issue clue summary.
