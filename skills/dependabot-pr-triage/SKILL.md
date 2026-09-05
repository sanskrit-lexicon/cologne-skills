_Created: 03-07-2026 · Last updated: 05-09-2026_

---
name: dependabot-pr-triage
description: Triage Dependabot dependency update pull requests across JavaScript and Python repositories. Use when a GitHub PR, issue, or local task asks an agent to inspect a Dependabot PR, classify patch/minor/major risk, evaluate release notes, choose minimal npm or Python validation commands, and recommend merge, hold, close, or follow-up work.
---

# Dependabot PR Triage

## Core Rule

Treat dependency updates as risk decisions. Do not merge or close based only on the version number; inspect the package ecosystem, update type, release notes, lockfile scope, and repo-specific validation surface.

Before acting, read `references/dependabot-triage.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Identify repo, PR number, package name, ecosystem, old version, new version, and update type.
2. Read Dependabot body, labels, changed files, and release notes or changelog excerpts.
3. Classify risk as patch-safe, minor-needs-checks, major-hold, security-urgent, or tooling-sensitive.
4. Run minimal repo-specific checks when local checkout is available; otherwise state the checks that should gate merge.
5. Recommend merge, hold, close, or follow-up with concise evidence and exact commands/results.
6. Do not alter Dependabot branches unless the user explicitly asks for a rebase, recreate, local fix, or merge.

## Stop Conditions

Stop and ask or report when the PR is not from Dependabot, release notes are unavailable for a risky update, validation cannot run locally, lockfile changes include unexpected packages, or the package is part of build/test infrastructure likely to affect CI.

## References

- Read `references/dependabot-triage.md` for risk classes, validation commands, and outcome wording.

_Dr. Mārcis Gasūns_
