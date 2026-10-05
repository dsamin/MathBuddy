# Phase 2A world and branding handoff

## Context

**Runtime reproduction correction complete; ready for master candidate integration review; human acceptance remains pending.** Completed ENV-01, ENV-02, BRAND-01 and BRAND-02 only. Originals, exact requests/references and prior takes are retained. The focused reviewer found crown clipping in the first foreground take; separate tool-authored repairs resolved it. The original runtime passed focused technical review. The master subsequently found and resolved a cross-runtime byte reproduction mismatch by using the exact original runtime; see Acceptance Criteria below.

- Worktree: `/Users/devan/.codex/worktrees/8899/MathBuddy`.
- Actual initial HEAD and approved input: `e48eb490711d9754b6b6e123f1e069aebfeae3d7` (initially detached).
- Resumed backup HEAD: `35c121edb6515fb486b7cb72eceed7c71d08fb47`.
- Branch actually used for checkpoints: `codex/phase-2a-world-wip`.
- **Final production packet commit: `99d78cac3f5cf6397e3479c5013cf3ddf53bb638`.** The documentation-only commit carrying this completed handoff follows that packet commit; obtain its exact ID with `git log -1 --format=%H -- docs/orchestration/phases/2a-world/handoff.md`. It is also returned in the phase session’s final response. This avoids a circular self-commit hash in the committed file.
- No further push occurred. Shared tracker/catalog/decisions and all 383 protected tracked inputs are unchanged. Master owns integration and all human decisions.

## Codebase Overview

Current ENV candidate take is **take-02**. Each of two worlds has distant scenery z0, ground z10 and edge foreground z60 in 2732×2048 landscape and 2048×2732 portrait: twelve genuine independently meaningful registered PNG layers. Four `editable.ora` files contain the three corresponding editable full-canvas raster layers; exact merged images reconstruct from those layers. Source is six separately generated current raster artworks, original PNGs, explicit masks/registration and the rebuild script. First foreground takes, first assemblies and first diagnostic previews remain preserved.

The provider produced 1536×1024 distant/ground and 1254×1254 foreground originals. Production exports resample and reproject them. Editable source is raster/OpenRaster, not vector objects, a painting-stroke document or a rig. Model version, seed and provider cost were not exposed; generation itself is not claimed reproducible. Recorded original/request/reference bytes and export reconstruction are verified.

`world-safe-regions.json` authors proposed canvas rectangles from the live catalog’s **region-relative** slots and qualitative reflow. Both worlds reserve the union of COUNT/JOIN/TAKE working regions, quantity-reference/session space, guide/choice/control/Home/Listen, plus M06/M07 garden rotor/flower states/five decoration/Finish regions. Foreground alpha is zero in each rectangle enlarged by 1.5% per side; each working plane remains opaque. No baked Pip, math pieces, labels, numerals, UI, toys or earned decoration appears in the backgrounds. These maps do not approve screen layouts, actual future prop fit, 80–88 pt touch targets, larger-text/native reflow, child usability or a family iPad.

BRAND-01 is a provisional **Pip’s Picnic** native typography recipe and editable text SVG with the exact bundled **Rubik Bold Version 1.100**, source/hash/copyright and complete SIL OFL 1.1. The original font download was unavailable; this explicit local provisional font choice is documented and awaits human acceptance. SVG embeds the font but has no outlined-vector or cross-renderer pixel-equivalence claim; actual SVG rendering was inspected in the local browser. BRAND-02 is opaque, unmasked 1024² RGB, reproducibly resized from the unchanged recovered 1254² icon, with 16/32/64/128 native-size checks. At 16px facial detail is limited; rabbit/ear/scarf silhouette remains recognizable.

## Tasks

- [x] Exact preflight/reference/protected-input snapshot and phase-local plan.
- [x] Twelve current registered layers and four editable OpenRaster sources with six preserved current artworks; historical takes retained.
- [x] Licensed scalable provisional branding recipe/icon and native-size previews.
- [x] Four clean composites, four exploded sheets, twenty separate diagnostic clearances/legends, overall contact sheet and adult gallery.
- [x] Decode/hash/alpha/contribution/reconstruction/clearance tests and actual pixel inspections.
- [x] Focused independent review; rounded-crown repair verified.
- [x] Environment rebuild: 70 files byte-identical. Branding rebuild: 16 files byte-identical (including final trimmed license excerpt).
- [x] Scope/protected-file/whitespace/staged secret checks and local production packet checkpoint.
- [x] Complete handoff and proposed master-ledger entries; stop at master review.

Master should inspect the gallery/clearances, review `proposed-ledger.json`, and integrate only this bounded packet. It does not select final delivery or unlock another phase. Keep world/art, composition, font/wordmark, icon, final name, device, content and provider/rights decisions pending until their respective human reviews. No native work, audio, other assets, Pebble, publishing or deployment was performed.

## File Locations

**Exact touched paths and SHA-256 inventory:** `docs/orchestration/phases/2a-world/packet-files.json`, covering all owned changes relative to the approved input (including recovered backup files): **215 hashed files plus one unhashed self-inventory entry = 216 entries**. It lists itself without a self-hash. Asset bytes are fixed by the production packet commit above; handoff bookkeeping is refreshed in the following documentation commit.

Primary samples (paths below are relative to the worktree):

- `assets/production/picnic-v1/review/world-branding/index.html` — adult gallery; layer toggles, four orientations, twenty diagnostic views/legends, actual SVG and branding sheets. All 35 image resources loaded in browser; all 55 local resource links validated. Gallery inspected at 1280px/390px with no overflow; narrow disclosure/Join legend and layer toggle were exercised. Browser viewport override restored.
- `assets/production/picnic-v1/review/contact-sheets/world-branding-overview.png` — inspected overview.
- `assets/production/picnic-v1/masters/images/ENV-01/take-02/landscape/` and `portrait/` — current picnic layers, composite and ORA.
- `assets/production/picnic-v1/masters/images/ENV-02/take-02/landscape/` and `portrait/` — current garden layers, composite and ORA.
- `assets/production/picnic-v1/masters/images/BRAND-01/take-01/` — font/license, editable SVG, 240/360/720/1100 previews and branding sheet.
- `assets/production/picnic-v1/masters/images/BRAND-02/take-01/` — preserved original, exact 1024 icon and small-size sheet.
- `assets/production/picnic-v1/metadata/world-provenance.json`, `world-registration.json`, `world-safe-regions.json`, `world-audit.json`, `world-brand-*.json` — exact requests/references/original/output hashes and technical metadata.
- `docs/orchestration/phases/2a-world/focused-review.md`, `technical-review.md`, `branding-evidence.md`, `packet-audit.json`, `validation-receipt.json`, `reproducibility.json`, `branding-reproducibility.json`, `proposed-ledger.json` — actual findings, commands/results and master integration proposal.

Selected immutable hashes (complete layer/source/hash inventory lives in metadata and packet-files.json):

| Package-relative file | SHA-256 |
|---|---|
| `masters/images/ENV-01/take-02/landscape/composite.png` | `10bbdee46409ccc6eb493e6339329882e4ca4f3c7cc0b93a5ce8caabae3d5b3e` |
| `masters/images/ENV-01/take-02/portrait/composite.png` | `1086bffc0a39cb3895b98b18674b138a6be808e3b3fc41b24cb6e717b6e8a66e` |
| `masters/images/ENV-02/take-02/landscape/composite.png` | `7fea1c0cc80fba272dd1543d841b09086c1544d4a29b86976290c17b19771be2` |
| `masters/images/ENV-02/take-02/portrait/composite.png` | `3f1c706e2555e749985831c9c0dc9a1a96d23f889d7b1c886ebd0719e34ac39f` |
| `masters/images/BRAND-02/take-01/icon-1024.png` | `1c354f164523c06f87795c6f5ed34db7aedd3b8098a1b46f001171b17627801f` |
| `masters/images/BRAND-02/take-01/recovered-icon-original.png` | `1a6ea126084e074f33d1d6c5446ad5d134143e0598d9c55c0050f6a0cdbfb888` |
| `masters/images/BRAND-01/take-01/source/Rubik-Bold.ttf` | `b1c36dfcbc5fe5011c552c76725c84d989a71d56440e8bfbfa0cb68b593dbad6` |

## Acceptance Criteria

Commands from the worktree root and observed results:

```sh
python3 docs/orchestration/phases/2a-world/world-build.py
python3 assets/production/picnic-v1/metadata/world-brand-build.py
python3 docs/orchestration/phases/2a-world/packet-audit.py
python3 docs/orchestration/phases/2a-world/packet-inventory.py
git diff --check
git diff --cached --check
gitleaks git --pre-commit --staged --redact --no-banner
```

- On the original runtime, repeated environment/branding builds reproduced 70/16 files byte-for-byte, respectively; cross-runtime byte equality is not established. Runtime is recorded in the branding manifest (final root verification Python 3.11.7, Pillow 12.1.1).
- Final packet audit passes four records, twelve dimensionally correct current RGBA layers, four exact editable reconstructions, opaque composites/icon, separate visible contributions, zero foreground intersection with all reserved masks, opaque working ground, exact source/request/reference hashes, eleven approved reference image hashes, three recovered originals and all 383 protected files.
- Actual source/output/composite/exploded/diagnostic/branding inspection and focused independent review pass; no unresolved routine technical findings. Staged whitespace found only an extra trailing empty line in a derived license excerpt; trimmed it while retaining the exact font/full OFL, then rebuilt/re-audited.
- Before production packet commit, `git diff --check` and `git diff --cached --check` pass; staged gitleaks exits 0, no leaks found, approximately 564055 bytes of staged patch text scanned. The completed handoff/documentation checkpoint is secret-scanned separately.
- Master integration proposal only: canonical catalog, shared tasks/tracker, decisions, provider-rights ledger, experiments/native code and original approved/recovered media are untouched. No delivery selection exists.

**Remaining decisions/limits:** world/art and composition acceptance; provisional Rubik/wordmark/icon approval; final name and family iPad; content/child/assistive-use review; generated-art provider/rights. Future prop/motion/native/device validation remains with its authorized phase. Background source resolution and raster-editability limits are disclosed above. Master may review candidate integration with the documented runtime; the packet is not human accepted or app-ready.

### Runtime correction and independent repeat check

The earlier generic `python3` command was insufficient to specify a reproducible environment. On this worktree it resolves through `/Users/devan/.pyenv/shims/python3` to the exact executable below, using user-site Pillow. No environment installation or global configuration was changed. Preserve user-site loading (do not use `-s`, `-I` or `PYTHONNOUSERSITE`) and verify the imported library path/version before building. Merely pinning Python or Pillow's version alone is not a proof of binary equivalence: native FreeType/compression libraries and the diagnostic Arial font also matter. These are observed local prerequisites and fingerprints, not a portable lockfile or promise that an independently installed wheel matches.

Observed original runtime (read-only probe after master's correction):

```json
{
  "executable": "/Users/devan/.pyenv/versions/3.11.7/bin/python3",
  "python": "3.11.7 (main, Nov 17 2024, 23:47:19) [Clang 16.0.0 (clang-1600.0.26.4)]",
  "platform": "macOS-27.0.1-arm64-arm-64bit",
  "architecture": "arm64",
  "pillow": "12.1.1",
  "PIL_location": "/Users/devan/.local/lib/python3.11/site-packages/PIL/__init__.py",
  "FreeType": "2.14.1",
  "python_zlib_build": "1.2.12",
  "python_zlib_runtime": "1.2.12",
  "Pillow_zlib": "1.3.1.zlib-ng",
  "jpeg": "6.2",
  "fingerprints": [
    {
      "path": "/Users/devan/.pyenv/versions/3.11.7/bin/python3",
      "sha256": "9663bbbce23869e208a4dc6349ff942e4ce334e28a616b184ef8f331edde7f07"
    },
    {
      "path": "/Users/devan/.local/lib/python3.11/site-packages/PIL/__init__.py",
      "sha256": "43828e12947b4bf5ec8f7d1fbceb2f47de311295f8294b15794c1a54fd5f53cd"
    },
    {
      "path": "/Users/devan/.local/lib/python3.11/site-packages/PIL/_imaging.cpython-311-darwin.so",
      "sha256": "0cbcfe94ca3181d011f4da90c46870e48412731d2c3fc26ee070079c7e0d9a4f"
    },
    {
      "path": "/Users/devan/.local/lib/python3.11/site-packages/PIL/_imagingft.cpython-311-darwin.so",
      "sha256": "148611bdd653915acde3722252504507ef890bad30c938bc7bfa304fd4102ac2"
    },
    {
      "path": "/Users/devan/.local/lib/python3.11/site-packages/PIL/.dylibs/libfreetype.6.dylib",
      "sha256": "5613ea09621a02368135ec414290d4b2af82bacfabd88404479540b8ecd1c8c8"
    },
    {
      "path": "/Users/devan/.local/lib/python3.11/site-packages/PIL/.dylibs/libz.1.3.1.zlib-ng.dylib",
      "sha256": "d98508d8cdc78e09ede96dce052544e408a457fe65125ccb53ee58f0d3f53a16"
    },
    {
      "path": "/System/Library/Fonts/Supplemental/Arial.ttf",
      "sha256": "525979822591a3447cfc49d943d6f7683508e25543407871c0ed8fed05fd2bd9"
    }
  ]
}
```

`otool -L` confirms `_imagingft` loads Pillow's `.dylibs/libfreetype.6.dylib` and `_imaging` loads `.dylibs/libz.1.3.1.zlib-ng.dylib`; Python's own zlib 1.2.12 is distinct from Pillow's PNG codec. Font rendering also uses the bundled unchanged Rubik binary listed above; Arial is used for adult diagnostic labels.

Master reported 23 differing file hashes out of 86 after rebuilding its independent clone with `/Users/devan/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`. A read-only probe confirms that executable currently imports Python 3.12.14 / Pillow 12.3.0 / FreeType 2.14.3, with Pillow zlib 1.3.1.zlib-ng. This differs from the original environment. The dependency differences explain why portable byte equality cannot be assumed; master confirmed ENV-02 ground had encoding-only differences (zero differing decoded pixels), while wordmark glyphs had actual raster differences.

A fresh independent copy was extracted from checkpoint `b2fd05d6d0cfb62d832f1ff6c6e701ccb7de46c9` into `/private/tmp/mathbuddy-phase2a-runtime-check`, separate from both preserved candidates and master's clone. Both rebuilds exited 0 there using the exact original executable:

```sh
cd /private/tmp/mathbuddy-phase2a-runtime-check
/Users/devan/.pyenv/versions/3.11.7/bin/python3.11 docs/orchestration/phases/2a-world/world-build.py
/Users/devan/.pyenv/versions/3.11.7/bin/python3.11 assets/production/picnic-v1/metadata/world-brand-build.py
```

Compared every retained hash in the original `reproducibility.json` (70) and `branding-reproducibility.json` (16) against that fresh copy: **86 compared, zero mismatches**. Neither receipt's original asset hash set was refreshed, and no candidate output or original was regenerated. This proves same-runtime repeatability in an independent copy, not cross-runtime reproduction. Master independently repeated all 70+16 hashes using `/Users/devan/.pyenv/versions/3.11.7/bin/python3.11` with zero mismatches and cleared the runtime reproduction blocker. That is the resolved executable behind the `python3` path above (`Path(sys.executable).resolve()`). Master may proceed with candidate integration; all human approvals remain pending.

Correction lesson within the owned phase: reproducibility commands must name the exact executable, imported library locations, native codec/font versions and dependency fingerprints; qualify byte-equality claims by runtime. Inventory count must distinguish hashed files from its unhashed self-entry. Shared `tasks/lessons.md` is reserved to master and was not edited.
