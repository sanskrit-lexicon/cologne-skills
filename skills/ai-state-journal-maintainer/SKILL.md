_Created: 03-07-2026 · Last updated: 05-09-2026_

---
name: ai-state-journal-maintainer
description: Maintain repository .ai_state.md session journals. Use when a GitHub issue, PR, or local task asks an agent to update, audit, tidy, or hand off project state in .ai_state.md, especially for repos that track Next Steps, Current WIP, Dev Notes, and Completed recent work between Codex or Claude Code sessions.
---

# AI State Journal Maintainer

## Core Rule

Treat `.ai_state.md` as the shared session journal, not as a dumping ground. Keep it current, concise, and structured so the next agent can resume without re-discovering completed work.

Before editing, read `references/ai-state-journal.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Inspect the repo task, current `.ai_state.md`, recent git status/logs, and any issue/PR context that motivated the update.
2. Preserve the required section structure and move items between queue, WIP, notes, and completed instead of duplicating them.
3. Record validation commands and outcomes for completed work.
4. Keep completed history recent; summarize older detail when it stops helping the next session.
5. On handoff, leave concrete next steps, blockers, and exact resume files/commands.
6. Do not change source files just to make the journal prettier.

## Stop Conditions

Stop and ask or report when the project objective is unclear, `.ai_state.md` has conflicting active goals, or journal updates would imply source work that has not actually been done.

## References

- Read `references/ai-state-journal.md` for required structure, micro-milestone rules, and handoff style.

_Dr. Mārcis Gasūns_
