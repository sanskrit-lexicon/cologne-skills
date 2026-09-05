_Created: 03-07-2026 · Last updated: 05-09-2026_

---
name: cdsl-newsletter-publisher
description: Prepare Cologne Digital Sanskrit Lexicon newsletter blog posts and email drafts. Use when a GitHub issue, PR, or local task asks an agent to create or update monthly or annual CDSL newsletters across csl-guides and csl-newsletter, including draft-newsletter.py date windows, Docusaurus blog frontmatter, email markdown files, archive/readme synchronization, and build checks.
---

# CDSL Newsletter Publisher

## Core Rule

Keep the web blog and email archive in sync. Monthly and annual newsletters should use precise date windows, correct Docusaurus frontmatter, matching email markdown, and explicit validation notes.

Before editing, read `references/newsletter-workflow.md`.

## Compatibility Rule

Write and follow this skill so it works in both Codex and Claude Code. Treat `$skill-name` references as workflow names: in Codex, invoke the skill when available; in Claude Code, read the named skill's `SKILL.md` and follow its instructions manually. Do not rely on Codex-only tools or UI features when a shell, GitHub CLI/API, local files, or plain Markdown handoff would work.

## Workflow

1. Resolve whether the task is monthly, annual, or stub preparation, and identify the exact date window.
2. Inspect both `csl-guides` and `csl-newsletter` before deciding which files must move together.
3. Use or verify `scripts/draft-newsletter.py --since YYYY-MM-DD --until YYYY-MM-DD` when generating activity summaries.
4. Create or update Docusaurus blog posts and email markdown with matching title/date/archive intent.
5. Sync newsletter archive/readme sections when adding new annual or monthly files.
6. Run the smallest relevant script/build checks and record any manual prose-editing step still required.

## Stop Conditions

Stop and report when the date window is ambiguous, the corresponding blog/email pair cannot be identified, generated activity needs human prose selection, or Docusaurus build failures are unrelated to the newsletter change.

## References

- Read `references/newsletter-workflow.md` for file naming, date windows, and validation expectations.

_Dr. Mārcis Gasūns_
