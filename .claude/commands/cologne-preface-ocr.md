---
description: OCR a Cologne dictionary's front matter (title pages, prefaces, abbreviation lists, addenda) from the csldoc scans into faithful Markdown, then add English + Russian translations, consolidated single-file editions, and a README index. Judgment / vision OCR — Opus tier. Arg = dictionary code (e.g. PWG, MW, AP90) or `all`.
---

# /cologne-preface-ocr

OCR and translate the **front matter** (Vorspann: title pages, forewords/prefaces, abbreviation lists, addenda/corrigenda) of a Cologne Digital Sanskrit Lexicon dictionary, starting from the csldoc scan pages.

Index of all dictionaries with front matter:
`https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/index.html`

Argument: a dictionary **code** (`PWG`, `MW`, `AP90`, `BUR`, `SKD`, …) or `all` to sweep every dictionary that has a preface index. Lower/upper case both fine; the URL code is lowercase.

This was first built for **PWG** (German), producing `PWG/prefaces/` with 27 pages × 3 languages + consolidated files. Reuse that as the reference output.

---

## Autonomy rules

- Execute all phases without per-page confirmation. Vision OCR, file writes, `curl`, Python, and (when asked) git commits/pushes are pre-approved.
- Every Python script: `sys.stdout.reconfigure(encoding='utf-8')` and `sys.stderr.reconfigure(encoding='utf-8')`.
- Write files UTF-8 **without BOM** (`open(f,'w',encoding='utf-8')`, not `utf-8-sig`).
- Commit only when the user asks. Never commit temporary crop images (see Phase 7 — this is the easiest mistake to make).

---

## Phase 0 — Resolve target

```
CODE=<arg lowercased>           # e.g. pwg, mw, ap90 ; PW dict's code is "pw"
BASE=https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build
INDEX=$BASE/dictionaries/index.html
IMG_BASE=$BASE/_images
```

Decide the **output repo / directory**. Many dict repos are cloned under `C:/Users/user/Documents/GitHub/`, but the repo name is not always the dict code:

| dict code | local repo | dict code | local repo |
|---|---|---|---|
| PWG | `PWG` | MW / MW72 / MWE | `MWS` (or `MW72`) |
| PW | `PWK` | AP90 | `AP90` |
| GRA | `GRA` | AP / AE | `AP` / `ApteES` |
| BUR/BOP/CAE/CCS/BOR/MD/INM/KRM/LRV/MCI/PUI/ACC/BHS | same-named repo |

Resolve by: exact repo match → repo whose `CLAUDE.md`/`readme` names that dictionary → else create a working dir `GitHub/prefaces_<code>/`. Output goes in `<repo>/prefaces/`.

For `all`: enumerate dictionary codes from the index page (the `href="<code>.html"` links), then run Phases 1–7 per code, skipping any with no preface index (Phase 1 returns nothing).

---

## Phase 1 — Discover the scan pages

The front-matter index for a dictionary is `dictionaries/prefaces/<code>pref.html`. It is a Sphinx toctree linking sub-pages `<code>pref/<code>prefNN.html`; **each sub-page embeds exactly one scan** `<img src="../../../_images/<file>.png">`.

```sh
# the section list (toctree labels = "Title, vol. 1", "Foreword, 1", "Abbreviations, 1", ...)
curl -s "$BASE/dictionaries/prefaces/${CODE}pref.html" | grep -oE 'href="[^"]+\.html"[^<]*</a>'
# for each sub-page NN, the embedded scan filename:
curl -s "$BASE/dictionaries/prefaces/${CODE}pref/${CODE}prefNN.html" | grep -oE '_images/[^"]+\.png'
```

Build a manifest of `(NN, section_label, scan_filename, sub_page_url)`. Note the section labels and which volume each belongs to (title pages reset the volume). **If `<code>pref.html` 404s or has no sub-pages, this dictionary has no front matter — skip it** (record that for `all`).

⚠️ The toctree order is the authoritative page order, and it is occasionally not the lexical order of the image filenames (PWG had `--06`/`--07` swapped between "Foreword 5" and "Abbreviations 1"). Trust the toctree, not the filename sort.

---

## Phase 2 — Download scans

```sh
mkdir -p <repo>/prefaces/scans
# for each scan in the manifest:
curl -s -o "<repo>/prefaces/scans/<file>.png" "$IMG_BASE/<file>.png"
```

---

## Phase 3 — OCR each page (the critical phase)

**Output**: one Markdown file per page `<code>prefNN.md` in `<repo>/prefaces/`, with this header then the transcription:

```yaml
---
source_scan: <file>.png
source_page: <section label, e.g. "Foreword, 1">
volume: <n>
source_url: <sub_page_url>
---

# <heading as printed, e.g. VORWORT.>
```

### THE non-negotiable OCR technique

The scans are 3000–6800 px. **The Read tool downsamples a whole page below legibility** — reading the full PNG yields confident-looking but *wrong* text (this is the single biggest failure mode). You MUST crop to native resolution first:

1. Detect single- vs **two-column** (most prefaces/abbreviation lists are two-column; title pages are single, centered).
2. With PIL, split a two-column page into LEFT and RIGHT columns, then cut each column into 3–6 **overlapping horizontal bands**. Find the true column boundaries — text clipped at the right edge means the column is wider than your crop (re-crop wider).
3. **Hard limit: every crop you Read must be ≤ ~1900 px on its longest side**, or the request is rejected ("image exceeds dimension limit"). Do **not** upscale a half-page 2× (that blows past 2000 px). To read tiny text, crop a *smaller native-resolution region*, don't enlarge.
4. Read LEFT bands top→bottom, then RIGHT bands. For stubborn Devanāgarī conjuncts, crop that word at 3× into its own ≤1900 px tile.
5. Delete the temp crops when done (Phase 7).

Reference crop helper:
```python
from PIL import Image
im = Image.open(png)                       # e.g. 3304 x 4673
cols = {'L':(150,1730),'R':(1700,3180)}    # adjust to real column edges
ys = [300, 1700, 3100, 4520]               # band boundaries (trim margins)
for cn,(x0,x1) in cols.items():
    for i in range(len(ys)-1):
        y0 = ys[i]-(60 if i else 0); y1 = ys[i+1]+60
        im.crop((x0,y0,x1,y1)).save(f'_crops/{cn}{i}.png')   # each ≤1900 px
```

### Transcription rules

- Transcribe the **source language faithfully in its original orthography** — do not modernize. Cologne dict prefaces are variously German (PWG, PW, SCH, CCS, GRA), English (MW, AP, AP90, MWE, MD, WIL, …), French (BUR, STC), Latin (BOP), or Sanskrit (SKD, VCP, ABCH, KRM). Detect from the scan. Preserve 19th-c. forms (German *Theil, Litteratur, dass, Maassstabe*; long ſ as s).
- **Sanskrit stays verbatim**: Devanāgarī in Unicode when confidently legible (else `[?]`); Roman transliteration with full diacritics (ā ī ū ṛ ṝ ḷ ṅ ñ ṭ ḍ ṇ ś ṣ ḥ ṃ); editorial romanization (ç, ǵ, â) as printed. Personal names and work titles verbatim.
- Reflow prose into paragraphs (one blank line between); keep title-page line breaks; preserve footnotes, signatures, places, dates, printed page numbers (`[page V]`).
- **Abbreviation-list pages** are `key = source-title` lists — render one entry per line preserving the pairing; keep keys/titles verbatim. **Addenda/corrigenda** are `headword + gloss + reference` entries — keep headwords/Devanāgarī/references verbatim.
- Mark unreadable `[illegible]`, uncertain `[?]`. **Never invent plausible text** — fidelity over completeness.
- **Omit the digitizer stamps**: the tiny running header (`Otto Böhtlingk & … : Sanskrit-Wörterbuch …`) and footer (`Institute of Indology & Tamil Studies, Cologne University … <date>`) are added to every scan and are *not* part of the original.

### Parallelize

Fan out subagents (`general-purpose`), each assigned a few pages with the **full cropping recipe and rules above embedded in the prompt** (subagents do not see this skill). Group light pages (titles) together; give dense forewords ≤2 pages each; give heavy addenda one each. Subagents only read text/images — but if one dies on an image-dimension/500 error, it ignored the ≤1900 px rule: redo that page yourself with proper crops. **Verify quality**: an agent that did few tool calls and flagged "faint/uncertain" probably skipped cropping — re-OCR those pages.

---

## Phase 4 — Translations (English + Russian)

For every page produce `<code>prefNN.en.md` and `<code>prefNN.ru.md` (separate per-language files). Header adds `language: en|ru` and `translation_of: <code>prefNN.md`.

- If the **source language is English**, skip `.en.md` (the base `.md` is already English) and note it in the README; always produce `.ru.md`.
- Translate the source prose faithfully in scholarly register. **Leave verbatim**: Devanāgarī/Sanskrit (any script), work titles, bibliographic abbreviation keys, reference numbers, and embedded foreign quotations (e.g. an English quotation inside German stays English; add a parenthetical RU rendering of surrounding prose only).
- Headings: `# VORWORT.`→ `# Foreword` / `# Предисловие`; `# Title…`→ localized.
- **Russian: personal names in Cyrillic, NO redundant Latin-in-parentheses** (the Latin form already lives in the source `.md`). Böhtlingk=Бётлингк, Roth=Рот, Weber=Вебер, Whitney=Уитни, Kern=Керн, Stenzler=Штенцлер, Schiefner=Шифнер, Müller=Мюллер, Lassen=Лассен, Aufrecht=Ауфрехт, Gildemeister=Гильдемейстер, Colebrooke=Колбрук, Wilson=Уилсон, Benfey=Бенфей, Pâṇini=Панини, Kâtyâyana=Катьяяна; Veda=Веда, Ṛgveda=Ригведа, Sanskrit=санскрит, Kaiserliche Akademie der Wissenschaften=Императорская Академия наук. Cyrillicize bylines and signatures too. **Bibliographic work-titles stay in their original script.**
- Translation agents are text-only (no image limits) — safe to fan out in larger groups.
- Then run one **consistency proofread** pass: normalize RU names, catch OCR typos in the source `.md`, and fix any EN↔RU meaning divergence by checking the source.

---

## Phase 5 — Consolidated single-file editions

Produce one file per language with **all pages in order** + a table of contents: `<code>pref_all.de.md` (use the real source-language tag: `.de`/`.en`/`.fr`/`.la`/`.sa`), `<code>pref_all.en.md`, `<code>pref_all.ru.md`. Generate with a script committed as `<repo>/prefaces/build_combined.py` so it is reproducible. Generic, data-driven version (reads each page's YAML — no hardcoded page list):

```python
import sys, os, re, glob
sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.environ.get('DICT', 'pwg')
# (suffix, outfile, doc title, page-word, src-word) ; add the source-language base as one entry
LANGS = {
  'src': ('.md',    f'{CODE}pref_all.SRC.md', 'Front matter — complete (source language)', 'Page',      'Source'),
  'en':  ('.en.md', f'{CODE}pref_all.en.md',  'Front matter — complete (English)',          'Page',      'Source (scan)'),
  'ru':  ('.ru.md', f'{CODE}pref_all.ru.md',  'Предварительные материалы — полностью (русский)', 'Страница', 'Источник (скан)'),
}
def split(text):  # drop opening YAML block + first H1; return (meta, body)
    meta={}; L=text.splitlines(); i=0
    if L and L[0].strip()=='---':
        i=1
        while i<len(L) and L[i].strip()!='---':
            m=re.match(r'\s*([A-Za-z_]+):\s*(.*)$', L[i])
            if m: meta[m.group(1)]=m.group(2).strip()
            i+=1
        i+=1
    while i<len(L) and not L[i].strip(): i+=1
    if i<len(L) and L[i].lstrip().startswith('# '): i+=1
    while i<len(L) and not L[i].strip(): i+=1
    return meta, '\n'.join(L[i:]).rstrip()
def slug(s):
    s=re.sub(r'[^\w\s-]','',s.lower(),flags=re.UNICODE); return re.sub(r'\s+','-',s.strip())
pages = sorted(glob.glob(os.path.join(HERE, f'{CODE}pref[0-9][0-9].md')))
for lang,(suf,outname,title,pw,srcw) in LANGS.items():
    out=[f'# {title}\n', f'Per-page files: `{CODE}prefNN{suf}`. Index: [README.md](README.md).\n', '## Contents\n']
    body=[]
    for de in pages:
        nn=re.search(r'(\d\d)\.md$', de).group(1)
        src=de[:-3]+suf if suf!='.md' else de
        if not os.path.exists(src): continue
        meta,txt=split(open(src,encoding='utf-8').read())
        h=f'{pw} {nn} — {meta.get("source_page","")} (vol. {meta.get("volume","?")})'
        out.append(f'- [{h}](#{slug(h)})')
        # demote in-body headings so the page heading stays the top level (H2)
        txt=re.sub(r'(?m)^(#{1,5})(\s)', r'#\1\2', txt)
        body.append(f'\n---\n\n## {h}\n\n<sub>{srcw}: [{meta.get("source_scan","")}]({meta.get("source_url","")})</sub>\n\n{txt}\n')
    open(os.path.join(HERE,outname),'w',encoding='utf-8').write('\n'.join(out+body).rstrip()+'\n')
    print('wrote', outname)
```
Run `DICT=<code> python build_combined.py`. Sanity-check: H2 count == 1 (TOC) + number of pages; any extra H2 means a page body has a stray `#`/`##` (fix the source page's heading level — that happened with PWG's addenda page, which used `#` for a sub-section that should be `##`).

---

## Phase 6 — README index

Write `<repo>/prefaces/README.md`: what this is (dictionary, editors, years, source URL), the three file-suffix conventions, a **Consolidated editions** table linking the `*_all.*` files and `build_combined.py`, and a **Contents** table — one row per page with Section / Vol. / source / en / ru links. Note source language, signatures/dates found, and that digitizer stamps were omitted. Use clickable Markdown links throughout (chat AND README; full blob URLs when referring on GitHub).

---

## Phase 7 — Cleanup, commit, push

**Cleanup first (do not skip):** delete every temporary crop dir/file before staging. Subagents scatter them (`_crops/`, `_tmp/`, `tmp_crops/`, loose `_*.png`, `scans/_tmp/`). Only these should remain tracked: `<code>prefNN.md|.en.md|.ru.md`, `<code>pref_all.*`, `build_combined.py`, `README.md`, and `scans/<dict>*.png`.

```sh
rm -rf <repo>/prefaces/**/_crops <repo>/prefaces/_tmp* <repo>/prefaces/tmp_crops <repo>/prefaces/scans/_tmp
rm -f  <repo>/prefaces/_*.png
git -C <repo> status --short prefaces        # eyeball: nothing but the keepers
```

Commit only when the user asks. If on the default branch, the user's PWG precedent committed straight to `master`; otherwise branch first. Stage `prefaces/`, commit with a message describing scope, and end with:
```
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
```
Push only if asked. If push is rejected (remote moved), `git fetch` + `git rebase origin/<branch>` (these commits only add new files → conflict-free) then push. If the working tree has an unrelated change blocking a rebase, `git stash` it, rebase/push, `git stash pop`.

---

## Gotchas (learned on PWG)

- Reading a downsampled full page → fluent but fabricated text. Always crop to native resolution. This is the #1 rule.
- Crop ≤1900 px/side; never upscale past 2000 px (hard API limit; killed several subagents).
- Trust the toctree order, not the image-filename sort.
- A foreword's place/date/signature may be split across the column foot (PWG vol.5 had **no** date; vol.7's date sat under the left column, names under the right). Don't invent a date.
- Don't commit temp crops (the first PWG commit accidentally swept in ~180 of them; had to be stripped before push).
- RU: Cyrillic names, no redundant Latin parens; keep work-titles in original script.
- Source ≠ German for most dicts — detect language; produce `.ru` always, `.en` only when source isn't English.
