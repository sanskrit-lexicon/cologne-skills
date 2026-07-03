# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

`cologne-skills` is the **portable, version-controlled cut** of the personal
`/cologne-*` Claude Code command family used across the Sanskrit Lexicon org
— published so the playbooks work on any machine and can be shared with
collaborators, instead of living only in a personal `~/.claude/commands/`.
Two parallel forms of the same content: `skills/<name>/SKILL.md` (portable
runbooks that both Codex and Claude Code can follow) and `.claude/commands/`
+ `.claude/agents/` (Claude Code's native command/agent format). This repo
has no application code, no build, and no CI — it's a documentation/playbook
repo distilled from a real security + maintenance pass across the org
(reflected-XSS sweep, SQLi/ReDoS hardening, CodeQL/Semgrep triage, GitHub
Actions audit).

## Common commands

There's nothing to build or test. To use a skill:

```sh
# As personal Claude Code commands (any repo, any session)
cp .claude/commands/cologne-*.md ~/.claude/commands/
# or symlink to stay in sync:
ln -s "$PWD/.claude/commands/"cologne-*.md ~/.claude/commands/

# As project-scoped commands (one specific repo only)
cp .claude/commands/cologne-*.md <target-repo>/.claude/commands/

# As Codex skills
cp -r skills/<name> ~/.codex/skills/
```

Then invoke by slash name, e.g. `/cologne-php-xss-sweep csl-santam`.

## Key directories / files

| Path | Purpose |
|---|---|
| `skills/<name>/SKILL.md` | Portable runbook form — one folder per skill, readable by Codex as a skill or by Claude Code as manual instructions; each includes an explicit Codex/Claude Code compatibility note |
| `.claude/commands/*.md` | Claude Code native command form of the same skills (`cologne-alert-triage`, `cologne-php-xss-sweep`, `cologne-preface-ocr`, `cologne-security-audit-all`, etc.) |
| `.claude/agents/*.md` | Read-only worker agents the skills fan out to — see Conventions |

## Conventions

- **PR-only, always.** Every skill branches off `origin/<default>` and never
  pushes the default branch directly — one tight PR per repo, no exceptions.
- **Resolve the default branch per repo**, don't assume — `gh api
  repos/{owner}/{name} --jq .default_branch` (not always `master`; e.g.
  `mw-dev` defaults to `main`).
- **Fork gotcha**: pass `--repo <owner>/<name>` explicitly to `gh pr create`,
  or a PR from a fork checkout may target the parent instead.
- **Check `origin/<default>` and open PRs first** before running a sweep — an
  external actor may already be running the same one; close duplicates
  rather than rebasing on top.
- **Windows/UTF-8**: every Python script sets
  `sys.stdout.reconfigure(encoding='utf-8')` and passes `encoding='utf-8'` to
  `subprocess.run`.
- **`/cologne-preface-ocr`'s vision-OCR playbook is load-bearing, not
  optional**: crop scans to native-resolution column-bands ≤1900px before
  reading — a downsampled full page yields fluent-but-fabricated text, not an
  error. Trust the toctree page order, keep Sanskrit/Devanāgarī verbatim,
  Cyrillic names stay Russian, omit digitizer stamps, never commit temp crops.
- **Worker agents in `.claude/agents/` are strictly read-only** — no
  Edit/Write, no `gh pr create/merge`, no `git push`. The skill or main loop
  does all mutation; a fanned-out agent can never itself modify a repo. Don't
  add write capability to one of these agents — that defeats the isolation
  the design relies on.
- **Prerequisites**: `gh` (authenticated, `repo` scope; `read:project` for
  project-board skills), `php` on PATH for `php -l` lint (Windows: alias
  XAMPP's `php.exe`), `python3`, and for `/cologne-preface-ocr` specifically:
  `curl` + Pillow (`pip install pillow`) — OCR itself uses the model's own
  vision, no Tesseract/OCR engine involved.

## What not to touch

- Nothing generated here — everything is authored playbook content. There is
  no build output to avoid hand-editing.
- Note the companion mechanical-batch skills (`cologne-codeql-all`,
  `cologne-dependabot-automerge-all`, the issue/tooling runbooks) and their
  `.deploy_*.py` helpers are **deliberately not yet included** here — they
  have machine-specific paths that need parameterizing first. Don't assume
  their absence is an oversight to silently "fix" by copying them in
  unparameterized.
