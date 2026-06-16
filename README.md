# cologne-skills

Portable [Claude Code](https://claude.com/claude-code) skills for security and maintenance work across the [Sanskrit Lexicon](https://github.com/sanskrit-lexicon) (Cologne Digital Sanskrit Dictionaries) GitHub org.

These are the **shareable cut** of the personal `/cologne-*` command family — version-controlled so they work on any machine and can be shared with collaborators, instead of living only in a personal `~/.claude/commands/`. Each skill encodes a battle-tested playbook (escaping decision tables, false-positive heuristics, the gotchas) rather than a generic template.

## Skills

| Command | What it does |
|---|---|
| `/cologne-php-xss-sweep <repo\|all>` | Find + fix reflected-XSS / SQL-injection / injection in a repo's PHP web-frontend, with **context-correct escaping** (HTML body/attr → `htmlspecialchars`; JS-in-`<script>` → `json_encode(JSON_HEX_*)`; URL-in-JS-in-attribute → `urlencode`; JSONP → whitelist; SQL literal → prepared/`''`; PCRE → `preg_quote`). PR-only. |
| `/cologne-security-audit-all [nondict\|dict\|all]` | Org-wide audit: GitHub Actions (pwn-request / script-injection / token scope), committed secrets (incl. the Firebase-web-key vs Cloud-key trap), and SAST coverage. Read-mostly; PRs only for hardening. |
| `/cologne-alert-triage <repo>` | Triage a repo's CodeQL + Semgrep alerts: fix the genuinely-exploitable ones (PR), dismiss false-positives/won't-fixes with **written justifications**. Handles the Semgrep `echoed-request` taint-mode quirk and "php → Semgrep, never CodeQL". |

## Install

**As personal commands** (available in every Claude Code session, any directory):

```sh
# copy them
cp .claude/commands/cologne-*.md ~/.claude/commands/

# …or symlink, so they stay in sync with this repo
ln -s "$PWD/.claude/commands/"cologne-*.md ~/.claude/commands/
```

**As project commands** (available only when working inside a specific repo): copy the `.md` files into that repo's `.claude/commands/`.

Invoke with the slash name, e.g. `/cologne-php-xss-sweep csl-santam`.

## Prerequisites

- **GitHub CLI** (`gh`) authenticated with `repo` scope (and `read:project` for any project-board work).
- **`php`** on PATH for the `php -l` lint step (Windows: e.g. XAMPP's `C:\xampp\php\php.exe` — alias it to `php` or adjust the lint command).
- **`python3`** for the helper scans (enumeration, workflow-risk, secrets).

## Conventions baked in

- **PR-only**: branch off `origin/<default>`, never push the default branch; one tight PR per repo.
- **Resolve the default branch per repo** (`gh api repos/{owner}/{name} --jq .default_branch`) — it is not always `master` (e.g. `mw-dev` defaults to `main`).
- **Fork gotcha**: pass `--repo <owner>/<name>` to `gh pr create`, or a PR may target a parent fork.
- **Check `origin/<default>` + open PRs first** — an external actor may run the same sweep; close duplicates rather than rebasing.
- **Windows/UTF-8**: Python scripts set `sys.stdout.reconfigure(encoding='utf-8')` and pass `encoding='utf-8'` to `subprocess.run`.

## Provenance

Distilled from a security + maintenance pass across the Sanskrit Lexicon org (reflected-XSS sweep, SQLi/ReDoS hardening, CodeQL/Semgrep triage, GitHub Actions audit). The companion mechanical-batch skills (`cologne-codeql-all`, `cologne-dependabot-automerge-all`, the issue/tooling runbooks) and their `.deploy_*.py` helpers are not yet included here — they can be folded in once their machine-specific paths are parameterized.

## License

MIT — see [LICENSE](LICENSE).
