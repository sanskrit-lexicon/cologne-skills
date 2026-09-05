_Created: 03-07-2026 · Last updated: 05-09-2026_

# AI State Journal Reference

Use this reference for repositories with a tracked `.ai_state.md`.

## Required Structure

Keep these sections, in this order:

```markdown
# Project Objective: [Global Goal]
## Next Steps (Queue)
## Current Work-In-Progress (WIP)
## Dev Notes & Hypotheses (Bugs, ideas, context)
## Completed (Recent only)
```

If the repo already uses emoji in the headings, preserve the repo's exact heading text.

## During Work

- Check off or move a logical sub-task when it is actually complete.
- Record persistent bugs, failed hypotheses, or changed approach under Dev Notes.
- Keep WIP focused on active work, not everything that could be done someday.
- Record validation commands with result, especially when a PR body or handoff will cite them.

## Handoff Cleanup

On session end or stop request:

- Move finished work to Completed.
- State blockers explicitly.
- Leave concrete Next Steps with file paths, issue/PR numbers, and commands.
- Remove stale WIP that is already completed or no longer intended.

## Boundaries

- Do not invent progress.
- Do not erase useful recent completed context just to make the file short.
- Do not modify unrelated source files while maintaining the journal.
- If the journal conflicts with repo facts, report the conflict and choose the evidence-backed state.

## Example Tasks

- Update `.ai_state.md` after a validation-only PR.
- Tidy a stale WIP section before handing off to another agent.
- Record that a build failed because of a known unrelated issue.

_Dr. Mārcis Gasūns_
