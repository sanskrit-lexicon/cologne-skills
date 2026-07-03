# Sundara QA Reference

Use this reference for Sundarakanda annotation work in `CommentaryStrategies`.

## Source Files

- `CLAUDE.md`: layer definitions, target density, validation commands, and hard rules.
- `SUNDARA_COMMENTARY_RATIONALE.md`: decision-ledger rationale and acceptance regimes.
- `.ai_state.md`: latest completed runs, open follow-ups, and generated-output refresh needs.
- `data/lexical/ch{N}.json`, `ch{N}.rejected.json`, and `ch{N}.qa_removed.json` when present.
- `data/sundara_ch{N}_commentary_to_add.json` and book-level merged files for final totals.

## Acceptance Regimes

- Base notes close real gaps in the Russian prose/commentary apparatus.
- Lexical/etymological notes may gloss non-obvious terms, compounds, and etymologies even when the prose translation is clear.
- Cross-text notes are softer evidence and should keep `review_required:true`.

## Adversarial Gate

Reject candidates that are transparent participles, standard epithets, obvious compound sums, in-chapter root duplicates, or notes already covered by earlier first occurrences. A high rejection rate is a quality signal, not a failure.

Check at least:

- accepted note rationale;
- rejected candidate reason;
- chapter density;
- global lemma dedup impact;
- whether recap chapters are low because vocabulary was introduced earlier.

## Invariants

- Preserve rejected logs and QA removal logs.
- Preserve `review_required:true` on lexical/cross-text notes unless a human editor explicitly resolves that review.
- Do not treat low density in recap chapters as a gap without checking first-occurrence dedup.
- Do not change Leonov text while adjusting notes unless explicitly requested.

## Reporting

Report chapter number, accepted/rejected counts, density, notes added/removed/restored, dedup rationale, validation command/result, and generated outputs that still need refresh, such as enriched HTML or corpus summary counts.

## Example Tasks

- QA Sundara ch.27 lexical notes after a low rejection pass.
- Explain why a recap chapter is below the target density by design.
- Refresh documentation after the Phase-1 lexical layer changes note totals.
