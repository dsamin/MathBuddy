# Phase 2A branding evidence

## Context

Complete bounded BRAND-01/02 candidate production from the recovered icon; working name is **Pip’s Picnic**, pending human acceptance. This child owns only the two BRAND directories, new `world-brand-*` metadata and this evidence file. No recovered original, shared catalog/approval/task file, native application, provider selection or other phase changed by this child. No new icon generation occurred.

Actual starting HEAD: `35c121edb6515fb486b7cb72eceed7c71d08fb47`, branch `codex/phase-2a-world-wip`, worktree `/Users/devan/.codex/worktrees/8899/MathBuddy`. Phase originally approved input: `e48eb490711d9754b6b6e123f1e069aebfeae3d7`. Root phase agent owns final secret scan/checkpoint and integration; this child did not commit.

## Codebase Overview

BRAND-01 is a reproducible native typographic recipe with real text and an unchanged bundled **Rubik Bold, Version 1.100**, plus an editable text SVG embedding that exact font. It is not an outlined vector. The font name table identifies Hubert & Fischer and Hebrew characters by Meir Sadan, SIL OFL 1.1. The font came from Codex runtime **26.915.20218** LibreOfficeDev's `Contents/Resources/fonts/truetype/Rubik-Bold.ttf`. Its packaged `LICENSE` explicitly lists Rubik under Libre Hebrew and supplies the full OFL 1.1 text; both relevant excerpt and complete license are included. The exact upstream release commit was not fetched and is not claimed.

The required UIUX `--design-system` query was run: `python3 /Users/devan/Projects/.codex/skills/ui-ux-pro-max/scripts/search.py 'children learning playful soft storybook rounded picnic sage' --design-system -p "Pip’s Picnic provisional branding" -f markdown`. It advised rounded typography, but its indigo/claymorphism suggestions do not replace approved Direction B. Varela Round was an initial suggestion, not an approved selection. Fetching it failed with `curl: (6) Could not resolve host: raw.githubusercontent.com`; the required escalation wait was interrupted. This batch instead explicitly proposes local licensed Rubik, with human font acceptance pending, as root approved within provisional production scope. No additional network approval is needed for the completed deliverables.

BRAND-02 is a square opaque **1024×1024 RGB PNG**, downsampled from recovered **1254×1254 RGB** via Pillow LANCZOS. No crop, repaint, mask, rounded corners or composition alteration is applied. The original icon request, prompt and image remain preserved. Provider/model/rights remain exactly as recorded in the interrupted checkpoint; model was not exposed.

## Tasks

- [x] Read brief, interrupted checkpoint/handoff, BRAND rows and Prompt 2; inspect approved character selection and relevant lessons.
- [x] Inspect recovered icon before producing derived exports.
- [x] Save exact 1024² unmasked opaque export and 16/32/64/128 native-size PNGs with native-size and enlarged diagnostic sheet.
- [x] Bundle unchanged font, exact version/copyright/source/hash and OFL 1.1; save scalable native typography recipe with real text and editable font-embedded SVG.
- [x] Produce actual native-font-rendered transparent wordmark PNGs at 240/360/720/1100 canvas widths and combined branding sheet.
- [x] Decode dimensions/modes/bounds and inspect actual 1024 icon, icon small-size sheet and combined branding sheet using image viewer.
- [x] Run build, audit-only and repeated byte-equality reproduction; run `git diff --check`.
- [x] Notify focused review agent with actual artifact paths; root assembles independent review results and final checkpoint.

Actual visual observations: long cream/pink unbent ears, dark eyes, orange nose, green scarf and sage backdrop remain visible in the 1024 export, without text or props. At 16px rabbit ear/head/scarf silhouette remains recognizable; mouth/cheek detail is lost and eyes are only dark dots. At 32px eyes, orange nose and scarf become clearer; 64/128px retain distinct face and ear details. This is visual inspection of exported sizes, not physical-device or child-usability approval. At 240px wordmark canvas width, all letters/apostrophe are distinct and unclipped; 360/720px have clear rounded letterforms. Native recipe uses #365444, 140px at 1100×240 master, centered x550 with y160 baseline, default kerning and no added tracking. Eventual app must preserve real accessible name text.

## File Locations

All package paths below are relative to `assets/production/picnic-v1/`:

- `masters/images/BRAND-01/take-01/source/Rubik-Bold.ttf`
- `masters/images/BRAND-01/take-01/source/OFL-1.1.txt`
- `masters/images/BRAND-01/take-01/source/source-license-excerpt.txt`
- `masters/images/BRAND-01/take-01/wordmark-editable.svg`
- `masters/images/BRAND-01/take-01/wordmark-{240,360,720,1100}.png`
- `masters/images/BRAND-01/take-01/branding-sheet.png`
- `masters/images/BRAND-02/take-01/icon-1024.png`
- `masters/images/BRAND-02/take-01/icon-{16,32,64,128}.png`
- `masters/images/BRAND-02/take-01/icon-small-size-sheet.png`
- `metadata/world-brand-wordmark-recipe.json`
- `metadata/world-brand-build.py`
- `metadata/world-brand-file-audit.json`
- `metadata/world-brand-validation.json`
- This phase-owned `docs/orchestration/phases/2a-world/branding-evidence.md`.

No font download files were saved. Existing preserved `masters/images/BRAND-02/take-01/recovered-icon-original.png`, `requests/world-brand-icon-take-01.json`, `prompts/world-brand-icon-take-01.txt` are inputs, not child modifications.

## Acceptance Criteria

Commands executed from worktree root:

```sh
python3 assets/production/picnic-v1/metadata/world-brand-build.py
python3 assets/production/picnic-v1/metadata/world-brand-build.py --audit-only
git diff --check
```

All pass. Runtime: Python 3.11.7 / Pillow 12.1.1; native FreeType text rendering. Repeat build compared entire 16-file manifest before/after and was byte-identical. Audit checks every file hash, original preservation, RGB 1024² opacity, four small sizes, four transparent wordmark sizes and nonzero unclipped text bounds. Original request/prompt hashes were separately checked; no regeneration or overwrite.

Immutable SHA-256:

| File | SHA-256 |
|---|---|
| Recovered icon original | `1a6ea126084e074f33d1d6c5446ad5d134143e0598d9c55c0050f6a0cdbfb888` |
| Icon 1024 export | `1c354f164523c06f87795c6f5ed34db7aedd3b8098a1b46f001171b17627801f` |
| Original saved icon request | `613207b17637f884d90c626b56d2874810f4095403de6a9a500b1351c1e3e759` |
| Original saved icon prompt | `d1e3f21897dbf0db2f0336d08f94683494ad8667f5311e7a24c3ba3c2099d8f8` |
| Unmodified bundled Rubik Bold | `b1c36dfcbc5fe5011c552c76725c84d989a71d56440e8bfbfa0cb68b593dbad6` |
| Wordmark 1100 preview | `3f0bcddcd5f6e03818cf2fd8f9f0a39f18cf9d7287b3329f3bdd0c0787a158df` |

Technical candidate completeness passes. Final name, font/wordmark treatment, icon composition/identity suitability, target device, provider rights and human acceptance remain pending. Editable SVG portability is not verified across renderers; native recipe and actual PNG previews are the verified deliverable. No cross-renderer pixel-equality claim, outlined-vector claim, app integration or device selection is made.
