# Dependabot PR Triage Reference

Use this reference for dependency PRs in repos such as `csl-guides`, `RuWritingStyles`, `Systema-Sanscriticum`, and `SanskritKaraoke`.

## Risk Classes

- `patch-safe`: patch update, narrow dependency, normal release notes, lockfile scope expected, validation passes.
- `minor-needs-checks`: minor update or tooling package; run build/tests before recommending merge.
- `major-hold`: major update, framework/runtime migration, or peer dependency shift; do not merge without explicit migration review.
- `security-urgent`: security update; prioritize targeted validation and merge path.
- `tooling-sensitive`: Playwright, Vite, Docusaurus, LangChain, model providers, test runners, bundlers, and type systems; inspect regressions carefully.

## Inspection Checklist

- Confirm author is Dependabot.
- Record package, ecosystem, old/new versions, and semver class.
- Inspect changed files: manifest only, lockfile, generated files, or source changes.
- Read release-note bullets for runtime, API, type, CI, loader, browser, or Node/Python version changes.
- Check whether compatibility score, labels, or CI status are present.

## Minimal Validation

For npm/Docusaurus repos:

```sh
npm test
npm run build
```

Use the repo's actual scripts from `package.json`; do not invent missing commands. For Python repos, inspect `requirements*.txt`, `pyproject.toml`, or project docs, then run the narrowest available test or import/build check.

## Outcome Wording

Use one of:

- `merge`: validation passed and risk is low.
- `hold`: needs human review, broader CI, or upstream issue check.
- `close/ignore`: update is unwanted, incompatible, or superseded.
- `needs-fix`: acceptable update but local repo must change first.

Always include evidence: release-note signal, changed files, commands run, and residual risk.

## Example Tasks

- Triage a Dependabot axios patch bump.
- Review a Playwright patch update for test-loader regressions.
- Classify a LangChain provider update as tooling-sensitive before recommending merge.
