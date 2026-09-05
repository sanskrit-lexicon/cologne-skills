_Created: 03-07-2026 · Last updated: 05-09-2026_

# CDSL Correction Workflow

Use this reference when preparing source-text corrections for Sanskrit Lexicon repositories.

## updateByLine Change Files

Most dictionary correction workflows use:

```sh
python updateByLine.py <input_file> <changefile> <output_file>
```

Change files use paired lines:

```text
1234 old exact original line text
1234 new exact replacement line text
```

Comments begin with `;`. Supported actions are `new`, `ins`, and `del`.

## csl-orig Audit Pattern

For csl-orig source corrections, use the Jim Funderburk / Dhaval Patel pattern:

0. Confirm the current user request explicitly authorizes the specific `csl-orig` source change. Without that authorization, stop at notes, an exact plan, or handoff.
1. Check `csl-corrections` CFR/batch history for the same dict/L/old/new correction before creating a change file, regex batch, or source edit. If it says `No change`, do not patch unless a maintainer explicitly reopens the decision.
2. Determine whether the accepted correction is a plain replacement or an inline correction layer such as `{{old->new||YYYYMMDD|author|issue|}}`.
3. Snapshot current source to a temp file.
4. Apply corrections with `updateByLine.py`.
5. Copy the result back into `csl-orig/v02/<dict>/<dict>.txt`.
6. Validate XML before committing.
7. Generate an audit-trail change file in `csl-corrections`.
8. Commit both affected repos.

Do not use `utf-8-sig`. Verify the first three bytes do not start with `efbbbf`.

## Semantic Uncertainty

Route to `$cologne-question-research` before editing when the proposed old/new replacement depends on interpreting a local marker, abbreviation, tag, personal name, encoding convention, or editorial policy. Do this even when the mechanical replacement looks straightforward.

## Local Validation

Prefer the repo's standard validation. On the local Windows setup, when XAMPP/xmllint is unavailable, `make_xml.py` success with `All records parsed by ET` is the accepted XML parse signal if the repo docs say so.

## PR/Issue Notes

Include:

- issue number and dictionary code;
- changed record/line numbers;
- before/after summary;
- validation command and result;
- any human decision that the change relies on.

_Dr. Mārcis Gasūns_
