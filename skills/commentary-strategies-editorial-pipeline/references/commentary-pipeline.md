# CommentaryStrategies Pipeline Reference

Use this reference for `C:\Users\user\Documents\GitHub\CommentaryStrategies`.

## Canonical Inputs

- `CLAUDE.md`: repo rules, corpus integrity commands, hard forbidden strings, and source/generated-file boundaries.
- `.ai_state.md`: current publication queue, completed milestones, open gates, and recent cross-check decisions.
- Article manuscripts and cover/readiness files under `articles/`.
- Hub files such as `ARTICLES`, GTD, and `PUBLICATION_ROADMAP_2026Q3.md` when present in the workspace or sibling planning repos.

## Cross-Check Targets

- Readiness status must use the current `N/5 - <stage>` vocabulary from the hub, not ad hoc draft labels.
- ORCID and email should match the canonical author source used by the repo, usually `Uprava/AUTHOR.md` when cited in `.ai_state.md`.
- Byline form may differ by journal requirement; treat Cyrillic-vs-Latin form as an explicit gate, not an automatic correction.
- Roadmap and GTD mentions must not contradict source manuscript/readiness files.
- `.ai_state.md` must record validation status and the exact discrepancy closed or left open.

## Hard Rules

- Never add the false Leonov attribution `М.: Наука, 2022`; use the repo-approved ongoing translation/editorial wording.
- Preserve the correct oblique form `Парибка`.
- Do not add a fifth analytical axis without explicit user permission.
- Do not treat generated web-asset dumps or archives as primary source unless the task explicitly targets them.

## Validation

Run after content edits:

```sh
python scripts/validate.py
```

Also run `python scripts/derive_urn.py --check` when corpus records or generated TEI/pages are touched. If validation flags pre-existing unrelated issues, record them separately and do not hide them with unrelated edits.

## Handoff Shape

Report the article/A-number, files checked, canonical state chosen, discrepancies fixed, validation result, and any remaining author/editor gates.

## Example Tasks

- Align A21 readiness across manuscript/readiness files, `ARTICLES`, GTD, and roadmap.
- Remove a forbidden Leonov attribution and make `scripts/validate.py` green.
- Normalize all manuscript `status:` fields to the hub readiness vocabulary.
