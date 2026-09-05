_Created: 03-07-2026 · Last updated: 05-09-2026_

# CDSL Newsletter Workflow

Use this reference for paired work in:

- `C:\Users\user\Documents\GitHub\csl-guides`
- `C:\Users\user\Documents\GitHub\csl-newsletter`

## File Pairing

- `csl-guides/blog/YYYY-MM-DD-cdsl-newsletter-<month-or-annual>.md` is the public Docusaurus post.
- `csl-newsletter/<month><year>.md` or `annualYYYY.md` is the email/archive format.
- `csl-newsletter/readme.md` should keep monthly and annual archive sections accurate when new files are added.

## Draft Generation

Prefer explicit windows:

```sh
python scripts/draft-newsletter.py --since YYYY-MM-DD --until YYYY-MM-DD --output draft.md
```

Monthly examples use the first and last day of the target month. Annual examples use the relevant year window, with partial-year windows only when the issue or publication plan says so.

## Blog Requirements

Check frontmatter for slug, title, date, and newsletter tag. Keep slugs distinct between monthly and annual posts, for example `newsletter-2026-annual` versus monthly 2026 editions. Include `<!-- truncate -->` where existing posts expect it.

## Email Requirements

Keep email markdown concise and archive-friendly. If the generated activity log is too raw, leave or perform the manual step to replace it with 3-5 prose highlights, depending on the task.

## Validation

Use the relevant checks for the repo touched:

```sh
npm run build
python scripts/draft-newsletter.py --since YYYY-MM-DD --until YYYY-MM-DD --output draft.md
```

If a build is too expensive or fails for unrelated existing content, report the exact command, first failing reason, and whether the newsletter files themselves passed structural inspection.

## Example Tasks

- Draft the August 2026 CDSL newsletter with `--since 2026-08-01 --until 2026-08-31`.
- Add annual CDSL newsletter posts for a range of years.
- Prepare future monthly stubs with exact commands for month-end generation.

_Dr. Mārcis Gasūns_
