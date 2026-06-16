---
description: Triage a Sanskrit Lexicon repo's CodeQL + Semgrep code-scanning alerts — classify real-vs-false-positive, fix the genuine ones (PR), and dismiss the rest with written justifications. Judgment — Sonnet/Opus tier.
---

# /cologne-alert-triage

Work a repo's open code-scanning alerts (CodeQL and/or Semgrep) down to zero noise: fix the genuinely-exploitable ones via PR, and **dismiss the false-positives and won't-fixes with a one-line written justification each** (reversible; visible in the Security tab). Avoids both extremes — leaving hundreds of red alerts, and bulk-dismissing without verifying.

Argument `$ARGUMENTS`: a repo name (e.g. `csl-apidev`). Use [`/cologne-security-audit-all`](cologne-security-audit-all.md) for the org-wide sweep.

---

## Conventions

- PR-only for fixes (branch off `origin/<default>`; mind the fork gotcha + the per-repo default branch).
- Windows encoding rules; write the dismissal/summary loop to a `.py` (it's many `PATCH` calls).
- **Dismiss != ignore.** Every dismissal carries `dismissed_reason` ∈ `false positive | won't fix | used in tests` + a `dismissed_comment` naming *why*. Never bulk-dismiss a whole repo without reading the flagged lines.

## 1. Map the terrain first

Summarize before diving — counts by **tool, rule, severity, and path** (paginate; the default page caps at 100 and hides the rest):

```sh
gh api --paginate "repos/{slug}/code-scanning/alerts?state=open&per_page=100" \
 --jq '.[] | "\(.tool.name)\t\(.rule.security_severity_level //.rule.severity)\t\(.rule.id)\t\(.most_recent_instance.location.path)"'
```

The shape tells you the strategy: a few hundred alerts dominated by one rule in one directory = a **scoping** problem (one `.semgrepignore`), not 300 individual fixes.

## 2. The biggest lever — scope out noise dirs

Most Semgrep volume is in **non-served code**. Check path concentration; if the bulk is under an archive/sample/test tree, add a `.semgrepignore` (gitignore syntax) at the repo root rather than patching files:

- `webbackup/` (csl-websanlexicon: 679 of 687 alerts were here — archived per-dict copies, not served)
- `sample/`, `simple-search/v1.*` dev iterations, `*_test.py`, `eval/`, trial/`api_trial*` scripts — non-production.

After the rescan, the noise alerts auto-close (the new SARIF supersedes them).

## 3. Real-vs-false-positive heuristics

| Pattern | Verdict |
|---|---|
| `php …echoed-request` / `printed-request` (Semgrep) in **served** `getword.php`/`query.php` | Real reflected-XSS → fix via [`/cologne-php-xss-sweep`](cologne-php-xss-sweep.md) |
| same, in `webbackup/`/`sample/`/dev iterations | won't-fix (non-served) → `.semgrepignore` or dismiss |
| `js/incomplete-(multi-character-)sanitization` in a **build script** escaping *trusted* dict XML/Markdown (`stripTags`, `mdCell`) | **false positive** — formatting helper, not a security sanitizer |
| `py/redos` on a regex in an `# not used` var / one-off `issue*/` script | won't-fix (unreachable, offline) |
| `py/flask-debug`, `py/stack-trace-exposure`, `py/regex-injection` in a `issues/issue*/serve_api.py` **prototype** | won't-fix (local investigation script, not deployed) |
| `py/overly-large-range` `[a-zA-z]` (the `A-z` range spans `[\]^_\``) | **real typo bug** → fix `A-z`→`A-Z` (one-char PR; also clears the alert) |
| `python.lang.security.use-defused-xml*` over the project's **own** dictionary XML in offline scripts | won't-fix (XXE needs attacker-controlled XML; these never ingest it) |
| `dangerous-subprocess` in a test script with hardcoded args | won't-fix |
| `mako-templates-detected` (note-level) | informational — leave |

When unsure, **read the flagged line and its data flow** before deciding. Cite the line in the dismissal comment.

## 4. Gotchas

- **Semgrep `echoed-request` is taint-mode**, not a syntactic check. It flags ANY `echo`/`json_encode` of `$_GET`-derived data and does NOT recognise a `preg_match` whitelist or `json_encode` as a sanitizer — **only `htmlentities`/`htmlspecialchars` on the echoed value clears it.** So a correctly-fixed line (whitelisted callback, `json_encode`d reflection) will RE-FLAG after a rescan → dismiss those residuals as false-positive-on-fixed-code.
- **CodeQL has no PHP analyzer** — php SAST belongs to Semgrep, never a CodeQL matrix. If you see `php` in a `codeql.yml` `strategy.matrix.language`, that's the bug, not an alert: drop it.
- **Verify before dismissing.** A finding flagged "X" may be a different X on closer read (a Firebase web key vs a Cloud key; a "Pali" comment that means "Pahlavi"). Confirm the actual context; reopen anything mis-dismissed.

## 5. Dismiss with reasons

For the FP/won't-fix set, `PATCH repos/{slug}/code-scanning/alerts/{n}` with `state=dismissed`, the reason, and a justification quoting the line. For a repo whose *entire* open set is one triaged category, dismiss-all-open is safe **only after** you've confirmed the complete list matches the expected rules+paths.

End with a short verdict table (real → PR; FP/won't-fix → dismissed, with counts). Keep maintainer-facing noise minimal.

## Agents (fan-out)

Pair with the read-only agent in [`.claude/agents/`](../agents/):

- **`adversarial-verifier`** — verify each non-trivial alert (CONFIRMED / PLAUSIBLE / REFUTED) before fixing OR dismissing. The bar to dismiss as a false-positive is a REFUTED vote that quotes the guard.
