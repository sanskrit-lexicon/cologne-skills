# Markup Batch Workflow

Use this reference for Cologne dictionary tasks that normalize recurring markup while preserving source text.

## Preflight

- Run `git status --short --branch`.
- Read `.ai_state.md` if present and keep its required sections intact.
- Inspect the issue labels and milestone expectations. Markup issues belong under Structured Data.
- Identify the canonical source workflow before editing:
  - XML repos often use generated source XML and local validation scripts.
  - `csl-orig` corrections edit `csl-orig/v02/{dict}/{dict}.txt` and require an audit change file in `csl-corrections`.
  - Many repos use `python updateByLine.py <input> <changefile> <output>`.

## Pattern Discovery

- Use `rg` for exact bad patterns, tag names, abbreviations, and nearby record identifiers.
- Sample enough matches to prove the replacement rule is not overbroad.
- Check at least one negative example that should not change.
- When a pattern may be polysemous, prove positive and negative examples semantically, not only syntactically. For example, confirm whether an abbreviation such as `s. v.` is one unit, or whether a marker such as `<h>` has the intended local meaning.
- If the correct markup depends on unresolved meaning of `<ab>`, `<h>`, `<lex>`, `<info>`, or another local convention, stop and use `$cologne-question-research` before constructing a batch.
- Preserve line order and UTF-8 without BOM.

## Change Construction

- Prefer change files with paired old/new lines when the repo supports them.
- Use a short checked-in script only when a mechanical batch is too large or fragile for a hand-authored change file.
- Keep one markup family per batch, such as `<ls>` normalization, `<ab>` placement, `<lex>` content cleanup, or link splitting.
- Do not combine markup cleanup with translation, headword, or definition changes.

## Validation

- Run the smallest focused check first, such as a parser, unit test, or exact-pattern count.
- For `csl-orig`, run dictionary generation through `csl-pywork/v02/generate_dict.sh {dict} tempparent/{dict}` when available. On local Windows without XAMPP, `make_xml.py` reporting `All records parsed by ET` is the accepted XML validation signal.
- Verify no BOM: first three bytes must not be `efbbbf`.
- Record the exact validation command and result in `.ai_state.md`.

## Handoff

When stopping or handing off, record:

- issue or task identifier
- dictionary/repo and source files
- exact pattern changed
- files generated or intentionally not generated
- validation commands and outcome
- remaining candidates or blockers
