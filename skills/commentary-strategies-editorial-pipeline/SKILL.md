---
name: commentary-strategies-editorial-pipeline
description: Synchronize and validate CommentaryStrategies publication state. Use when a GitHub issue, PR, or local task asks an agent to align manuscript frontmatter, ARTICLES/GTD/roadmap status, readiness gates, ORCID/email/byline metadata, forbidden-string rules, .ai_state.md, or scripts/validate.py outcomes in the CommentaryStrategies repository.
---

# CommentaryStrategies Editorial Pipeline

## Core Rule

Treat publication state as cross-file evidence, not a single-file edit. Before changing status, readiness, author metadata, or roadmap text, identify the article/A-number and verify all canonical tracking points that mention it.

Before editing, read `references/commentary-pipeline.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Inspect `CLAUDE.md`, `.ai_state.md`, and the relevant article/readiness files before deciding what state is canonical.
2. Resolve the target article number, manuscript path, cover/readiness files, and hub rows in `ARTICLES`, GTD, and roadmap documents.
3. Cross-check readiness number, status wording, ORCID, email, byline form, and open gates across every tracking point.
4. Apply only the smallest consistency fix needed; do not invent new readiness stages or close gates without evidence.
5. Run `python scripts/validate.py` after content edits and record the command/result in `.ai_state.md` or handoff notes.
6. If stopping before edits, leave exact discrepancies and candidate files for the next agent.

## Stop Conditions

Stop and report findings when the canonical state conflicts across sources, an article cannot be mapped to an A-number, a gate depends on author/editor sign-off, or validation fails for reasons outside the requested change.

## References

- Read `references/commentary-pipeline.md` for canonical files, hard rules, and validation expectations.
