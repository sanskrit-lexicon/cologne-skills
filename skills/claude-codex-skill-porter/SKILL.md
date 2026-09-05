_Created: 03-07-2026 · Last updated: 05-09-2026_

---
name: claude-codex-skill-porter
description: Audit and update skills so they work in both Codex and Claude Code. Use when a local task asks an agent to create, port, review, or repair SKILL.md instructions, agents/openai.yaml metadata, bundled references, or skill wording that currently assumes only one agent host.
---

# Claude Codex Skill Porter

## Core Rule

Make skills portable runbooks. A skill should be usable by Codex through skill invocation and by Claude Code as ordinary Markdown instructions with local files, shell commands, GitHub CLI/API, and handoff notes.

Before editing, read `references/skill-portability.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Inspect the target skill's `SKILL.md`, `agents/openai.yaml`, and referenced resources.
2. Ensure frontmatter is agent-neutral and trigger-rich; replace host-specific wording that names only one agent host with "asks an agent" where accurate.
3. Add or repair `## Compatibility Rule`.
4. Convert host-specific instructions into portable alternatives when possible.
5. Keep resources minimal: no README, changelog, or extra docs unless directly needed by the skill.
6. Run `quick_validate.py` and report portability issues that remain.

## Stop Conditions

Stop and report when a skill depends on a host-only tool with no practical Claude Code equivalent, when a referenced resource is missing, or when changing behavior would exceed portability cleanup.

## References

- Read `references/skill-portability.md` for portability checklist and validation expectations.

_Dr. Mārcis Gasūns_
