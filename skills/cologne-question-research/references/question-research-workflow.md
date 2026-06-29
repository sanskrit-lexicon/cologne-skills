# Question Research Workflow

Use this reference for Cologne dictionary issues where the right answer is not yet a precise source edit.

## Evidence Order

1. Issue text, screenshots, comments, and labels.
2. Local dictionary source record and neighboring records.
3. Generated XML or display output, if the repo has it.
4. Scan references named in the record, issue, or dictionary metadata.
5. Parallel dictionaries in sibling repos or `csl-orig/v02`.
6. External scholarly references only when local evidence is insufficient.

## Local Search

- Use `rg` for headwords, record ids, abbreviations, and distinctive phrases.
- Prefer exact transliteration and then variants only after confirming the dictionary's encoding.
- Check sibling dictionaries when the issue asks about meaning, citation, root, gender, or morphology.
- Do not infer from one dictionary when the issue is about print fidelity in another; inspect the relevant scan or source note.

## Semantic Gate Signals

Pause before recommending a source edit when the patch depends on what a local convention means.

- Treat tags and markers as dictionary-local until proven otherwise. For example, `<h>` may mark homonyms in one context and hierarchy or another local convention elsewhere.
- Treat abbreviations as complete units. For example, confirm whether `s. v.` is the abbreviation rather than normalizing only `<ab>v.</ab>`.
- Treat bulk name or encoding replacements as evidence questions first. For example, a proposed `sAyanaH` -> `sAyaNaH` batch needs context checks, negative examples, and prior correction-history review before it becomes a mechanical correction.
- Prefer neighboring records, issue comments, source notes, scans, generated display/XML, and parallel dictionaries over pattern appearance alone.

## Decision Labels

- `answer-only`: evidence resolves the issue without a source change.
- `ready-for-correction`: the next agent can make a specific line-level edit.
- `ready-for-markup-batch`: the problem is recurring markup normalization.
- `needs-human-review`: the evidence is ambiguous or requires scholarly judgment.
- `blocked`: required scan, source repo, or external access is missing.

## Reporting

Write a compact research note with:

- conclusion and decision label
- source paths and line numbers inspected
- scan or external links used
- exact proposed correction if one is ready
- validation that was run, or why validation was not applicable
- next resume point for a correction or markup skill

Update `.ai_state.md` with the same decision so future sessions do not repeat the research.
