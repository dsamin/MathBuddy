# Five Pip poses — character review

October 4, 2026. Direction B is the selected rendering direction. These are five concrete review candidates; identity, art, content and provider/rights approval remain pending. Pip’s Picnic remains provisional.

Review the [five poses together](pip-five-poses.png), [light/dark alpha composites](pip-alpha-light-dark.png), [small-size previews](pip-small-size.png), [registration diagnostic](pip-registration.png) and [ear/scarf/face details](pip-edge-details.png).

| ID | Pose | Transparent aligned candidate | Preserved provider source |
|---|---|---|---|
| PIP-01 | Idle welcome | [RGBA](../../masters/images/PIP-01/take-01/aligned-review.png) | [Original](../../masters/images/PIP-01/take-01/original.png) |
| PIP-02 | Attentive pointing | [RGBA](../../masters/images/PIP-02/take-01/aligned-review.png) | [Original](../../masters/images/PIP-02/take-01/original.png) |
| PIP-03 | Supportive thinking | [RGBA](../../masters/images/PIP-03/take-01/aligned-review.png) | [Original](../../masters/images/PIP-03/take-01/original.png) |
| PIP-04 | Pleased | [RGBA](../../masters/images/PIP-04/take-01/aligned-review.png) | [Original](../../masters/images/PIP-04/take-01/original.png) |
| PIP-05 | Farewell | [RGBA](../../masters/images/PIP-05/take-01/aligned-review.png) | [Original](../../masters/images/PIP-05/take-01/original.png) |

Recommend reviewing these as one coherent identity candidate. The proposed ears stay rounded and unbent in every expression, based on the board’s attentive rabbit: viewer-left splayed, viewer-right more upright, coral inner insets. The face, cream proportions and green scarf stay consistent. Thinking reads calmly curious with a slight smile; pleased uses clasped paws and happy eyes; farewell is a small reassuring wave. The focused independent AI reviewer found no mandatory repair in this batch. That review does not grant human approval.

All five aligned PNGs decode as 1536×1536 RGBA. The alpha≥32 character height is 1180 pixels, with one-pixel resampling tolerance (PIP-02 measures 1181). The visible foot row is exactly 1382 across all five. The common normalized anchor `(0.5,0.90)` is geometric `(768,1382.4)`, matching M04/M05/M07. The midpoint of the bottom 4% core silhouette band differs from x768 by at most 0.5 pixels. All nonzero alpha fits the common exclusive safe box `[154,154,1382,1414]`; canvas edges are transparent. Full per-pose silhouette bounds and all source/export hashes are in the [measurements](../../metadata/pip-alignment-measurements.json).

The built-in image provider returned five 1254×1254 originals, rather than the requested canvas. These originals remain unchanged and individually hashed. Aligned exports use a disclosed alpha finishing rule, premultiplied Lanczos uniform resampling (about 6.3–7.4% enlargement of source pixels) and transparent padding. The larger canvas adds no generated detail. Finishing removes alpha=1 quantization dust and low-alpha pixels more than four source pixels from the main alpha≥32 character; the maximum removed alpha is only 2–5. Visible RGB is not repainted. Outer antialias extends a few rows below the visible baseline, to rows 1385–1387. Original dust is preserved in the sources. No conspicuous matte box, halo, crop, extra limb or painted text appeared in actual light/dark and edge inspection.

The [reproducible recipe](../../metadata/pip-alignment-recipe.py) records dependency versions and recreates every aligned PNG and five review sheets byte-for-byte. Run from the repository root:

```sh
python3 assets/production/picnic-v1/metadata/pip-alignment-recipe.py --check
python3 assets/production/picnic-v1/metadata/pip-verify.py
```

The [exact prompts and requests](../../prompts/) and per-take provenance retain original provider paths, reference hashes and tool arguments. [Tool response metadata](../../metadata/pip-tool-responses.json) preserves the returned source-path text. Model version, seed and cost are not exposed by the built-in tool; rights approval remains pending. One original take per pose was generated; none was overwritten or rejected.

At 256×256 canvas size (~197-pixel silhouette), expressions and gestures are readable. At 128×128 (~98-pixel silhouette), identity, scarf and gesture remain recognizable but expressions are subtle. At 64×64 (~49-pixel silhouette), welcome/thinking/pleased are not reliably distinguishable. These are pixel previews, not physical iPad usability evidence. They do not establish native touch, accessibility, motion or child comprehension.

The pivot is a silhouette registration reference, not an anatomical joint. Common height and feet do not guarantee pixel-matched internal landmarks or clean native crossfades. This batch supplies flattened transparent whole-character stills; no rig, sprite sequence, editable body/ear/scarf layers or separate M07 shadow is delivered. Motion briefs remain provisional and unchanged.

Technical results and human decisions are recorded separately in the [character review record](../../metadata/pip-character-review.json). No candidate is selected into `delivery/`. Every previous take and experiment remains preserved. No environment, branding, math piece, reward, audio, later phase, native modification/build or Pebble change began.

The next decision is to **keep or revise this face, proportions, scarf and consistent attentive-reference ears across all five**. Record that human decision before dependent world/branding production.
