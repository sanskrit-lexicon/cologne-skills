# Skill Portability Reference

Use this reference when creating or updating user skills.

## Required Compatibility Rule

Every skill should include:

```markdown
## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.
```

## Portability Checklist

- Frontmatter has only `name` and `description` unless the system skill already uses approved metadata.
- Description says what the skill does and when to use it.
- Wording is agent-neutral: prefer "agent" over "Codex" when the instruction applies to both.
- `$skill-name` references are explained as workflow names.
- Tool instructions offer portable fallbacks: shell, `gh`, local files, APIs, or Markdown handoff.
- References are one level deep from `SKILL.md`.
- `agents/openai.yaml` still matches the skill.

## Avoid

- Codex-only UI directives as the sole execution path.
- Hidden assumptions about plugin availability.
- Extra `README.md`, `CHANGELOG.md`, or installation docs inside the skill.
- Duplicating long reference material in `SKILL.md` and references.

## Validation

Run:

```sh
python C:\Users\user\.codex\skills\.system\skill-creator\scripts\quick_validate.py <skill-folder>
```

Then grep for host-specific trigger wording, unresolved template placeholders, missing reference files, and absent `Compatibility Rule`.

## Example Tasks

- Port an older skill so Claude Code can use it as a Markdown runbook.
- Review a new skill for Codex-only assumptions.
- Regenerate stale `agents/openai.yaml` after changing a skill trigger.
