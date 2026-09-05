_Created: 03-07-2026 · Last updated: 05-09-2026_

---
name: publication-readiness-auditor
description: Audit article or manuscript publication readiness across project trackers. Use when a GitHub issue, PR, or local task asks an agent to verify submission readiness, status numbers, author metadata, ORCID/email/byline, cover letters, open gates, journal-specific requirements, roadmap consistency, or handoff notes for scholarly publication projects.
---

# Publication Readiness Auditor

## Core Rule

Audit before editing. Publication readiness is a claim across manuscript, cover letter, readiness checklist, project hub, roadmap, and journal gates; do not mark an item ready based on one file.

Before editing, read `references/publication-readiness.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Identify the publication unit: article number, title, target journal, manuscript path, and related cover/readiness docs.
2. Inspect project rules, `.ai_state.md`, and all trackers that mention the unit.
3. Cross-check readiness score, status text, author metadata, byline form, ORCID/email, open gates, and sign-off state.
4. Separate factual fixes from author/editor decisions; do not close decision gates without evidence.
5. Run the repo's validation or document why no validation applies.
6. Report a readiness verdict: ready, not ready, inconsistent, or blocked, with exact files and next actions.

## Stop Conditions

Stop and report when target journal requirements are unknown, author sign-off is needed, metadata sources conflict, or readiness depends on external archival/editorial work.

## References

- Read `references/publication-readiness.md` for audit checklist, verdicts, and handoff format.

_Dr. Mārcis Gasūns_
