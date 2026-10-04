# MathBuddy — reviewed asset requirements and production plan

**Review proposal · October 3, 2026 · No production, provider request, app change or build is authorized by this document.**

The next step is a small direction review, followed by individually reviewed asset batches. The existing native pilot, pictures and recordings remain unapproved experiments. They are useful comparison material, not an accepted starting point. This plan follows the useful parts of Pebble's process while preserving the user's stricter order: specification → assets → one detailed native phase → review.

## 1. Authoritative planning package

| File | Purpose | Exact proposed scope |
|---|---|---|
| [Asset register](asset-register.csv) | Enumerated requirements, states/layers, exports, dependencies, reviews and candidate status | **196 logical rows** |
| [Content catalog](content-catalog.json) | Exact quantities, modes, checkpoints, help, evidence, voices and asset links | **24 authored variants: 8 count, 8 join, 8 take away** |
| [Voice script catalog](voice-script-catalog.json) | Every unique exact draft line, context, support classification and references | **101 distinct spoken recordings** after exact-script deduplication |
| [Overall feature specification](../feature-spec.md) | Product and learning behavior, F01–F13 | Pilot quantities 0–5, at most 6 available pieces |
| [Roadmap](../roadmap.md) | Phase 0–6 sequence and review boundaries | Phase 3 starts with **CNT-01 only** |
| [Native phase implementation plan](../plans/2026-10-03-native-pilot-implementation-plan.md) | Proposed tasks and acceptance scenarios after the asset gate | Planning only; no instruction to start code |

A logical row is not a PNG or a generated take. Six copies of one berry in a lesson use one approved illustration and six stable occurrences. A number glyph and a control-state recipe are native design requirements, not generated bitmap files. A voice row becomes a preserved master and one selected playback export; multiple auditions or replacement takes do not create new logical script IDs.

The 196 rows contain **58 visual/interface/layout requirements, 7 motion briefs, 6 sound effects, 24 content records and 101 voice scripts**. The existing experimental media do not satisfy these counts by their mere existence. No future shapes, comparisons, make-five lessons, music or ages-six-to-eight curriculum media are hidden in this pilot estimate.

## 2. Independent review findings

The original asset outline had the right world and categories but was not production-ready: it named families without exact content quantities, did not enumerate recordings, and placed motion late enough to risk painting incompatible layers. The register and catalogs address those gaps as review proposals.

- **Silent play needs a visible goal.** `REF-00` through `REF-05` specify the requested count or transfer using a framed, noninteractive quantity model. Each works with both object families. Zero is an intentionally empty model, not missing artwork. A reference never reveals an assessed joining total or remainder. Evidence records that a visual model was provided.
- **One gesture is not one learning claim.** Joining all pieces and transferring the requested amount are valid early experiences. They do not establish an independently answered total or subtraction result. The catalog records action-only and numeral modes separately, with separate transfer and remainder checkpoints.
- **Configured support and extra help differ.** Ordinary instruction/replay, Undo and enabled current-count narration are not extra help. Specific cues and modeled counting have explicit metadata. Action-only is a representation, not a default `helpUsed` flag. Post-success explanations cannot rewrite earlier response evidence.
- **Every possible spoken count is covered.** Number clips include zero through six, so returns, Undo and over-packing can say the actual current count. Replace stale numbers with the latest count; do not play a FIFO backlog after rapid taps. This move/return policy applies to the counting basket and transferred set only. Joining never automatically speaks its assessed total; the source remainder is also withheld. Deliberate unique-object self-counting is a separately recorded baseline scaffold; requested modeled counting is help.
- **Rewards have a finite promise.** A free flower is available immediately. Completed sessions one through six grant a pinwheel, mushroom, lantern, stepping stone, bunting and birdhouse. Later sessions lead to existing garden play. The scripts never promise a seventh unmade object. This order remains a parent-review proposal.
- **Layer and motion contracts precede final illustration export.** Basket front/back, pinwheel rotor/pivot, flower states and environment safe regions are decided before full art production. Phase 2D verifies the resulting motion package; it is not when those requirements are first discovered.
- **Natural voice remains a separate review.** Pebble's provider/voice is a candidate, not approval of MathBuddy's scripts or performances. Existing files must pass transcript comparison and listening review if proposed for reuse.

The style search was run through `ui-ux-pro-max` with the SwiftUI context as required by workspace instructions. Its generic chatbot/landing-page suggestions were unsuitable for this brief and have not been adopted. The existing warm storybook palette remains one direction to compare, not an approved system.

## 3. Complete pilot inventory and quantities

| Batch | IDs | Logical requirements | Production definition |
|---|---|---:|---|
| 2A — Character/world/identity | `PIP-01…05`, `ENV-01…02`, `BRAND-01…02` | **9** | Five aligned still poses; two layered environments; wordmark recipe; app icon |
| 2B — Learning pieces/interface | `OBJ-BERRY/APPLE`, four `PROP-*`, `REF-00…05`, `NUM-00…06`, three `MARK-*`, sixteen `UI-*`, `CUE-DEMO`, three `LAYOUT-*` | **42** | Two reusable countable families, containers, target references, native symbols and control states, help cue |
| 2C — Garden | `REWARD-PINWHEEL`, `REWARD-FLOWER`, `DECOR-01…05` | **7** | One earned toy, one free toy and five permanent decorations |
| 2D — Motion/sound | `M01…07`, six `SFX-*`, 101 `VO-*` | **114** | Seven final briefs/storyboards, six subtle effects, exact approved narration |
| 2E — Content/package | `CNT-01…08`, `JOIN-01…08`, `TAKE-01…08` | **24** | Approved records referencing the preceding assets and scripts |
| **Total** | | **196** | Logical requirements; no claim of 196 media files |

Proposed export rules, subject to the selected art direction:

- **Pip:** five transparent poses on the same canvas with consistent scale, foot baseline, gaze and anchor. The provisional source canvas is 1536 × 1536. These are still poses for restrained transforms/crossfades, not an articulated rig or sprite-frame sequence.
- **Environments:** three aligned layers per scene—distant scenery, ground plane and edge foreground—with portrait and landscape composition. That is six selected layer exports per scene, twelve across both scenes. Provisional composition canvases are 2732 × 2048 and 2048 × 2732; confirm the family device and smallest supported iPad before final export. Preserve editable higher-resolution masters. Never bake labels, controls, numerical answers or countable lesson fruit into a background.
- **Objects:** one selected 1024 × 1024 transparent base or approved scalable equivalent per family. Eight states use the same identity with native overlays/transforms: available, pressed, moving, placed, returned, count-highlighted, help-highlighted and completed. Review six simultaneous occurrences at intended iPad size.
- **Props:** basket front/back are independently rendered. Source/incoming mats and the friend's plate have different positions and non-color cues. A full basket must not conceal individual quantities. Native vector props are acceptable if their approved design and state definitions are delivered.
- **References/numerals/controls:** author native component recipes and contact sheets. Six target quantities × two object families are twelve reference examples, not twelve additional generated image assets. Seven numerals cover zero through six. Equations appear only at their approved reveal point.
- **Toys:** pinwheel has base, stem and rotor layers with a shared pivot map. Flower has aligned bud/open states. Every decoration has placement bounds and a stable anchor. Garden contact sheets show all six earned items plus the free flower without crowding.
- **Audio:** 101 narration masters and 101 selected playback files; six effect masters and six selected playback files. Those are **107 logical audio assets**, before audition/replacement takes. Preserve original WAV masters; proposed delivery is mono AAC `.m4a`. Technical finishing cannot substitute for listening acceptance or repair a clipped source performance.

The existing experiment supplies possible references for `PIP-01`, `PIP-04`, `ENV-02`, the icon, berry/basket/pinwheel vector ideas, six number recordings and three effects. These are labeled in the CSV with real paths. The other experimental recordings remain in the experiment archive but are not mapped to exact new scripts without transcript review. A flattened garden candidate does not fulfill the newly required layer exports.

## 4. Proposed content, with honest representation

All 24 records are draft examples for mathematical and child-language review. They are not 24 separately illustrated screens or a compulsory sequence. A beginner can receive counting-only sessions; operations become eligible only in the selected band. Zero examples remain explicitly flagged for content review.

| ID | Family | Exact quantities | Mode | Earliest proposed phase |
|---|---|---|---|---|
| CNT-01 | berry | make 3 from 5 | quantity-reference | Phase 3 only |
| CNT-02 | berry | make 5 from 6 | quantity-reference | Phase 4 |
| CNT-03 | apple | make 1 from 3 | quantity-reference | Phase 4 |
| CNT-04 | apple | make 2 from 4 | numeral-plus-reference | Phase 4 |
| CNT-05 | berry | make 4 from 6 | numeral-plus-reference | Phase 4 |
| CNT-06 | apple | make 0 from 3 | quantity-reference | Phase 4 |
| CNT-07 | berry | make 3 from 6 | numeral-plus-reference | Phase 4 |
| CNT-08 | apple | make 5 from 6 | numeral-plus-reference | Phase 4 |
| JOIN-01 | berry | 2 + 1 = 3 | action-only | Phase 4 |
| JOIN-02 | apple | 1 + 1 = 2 | action-only | Phase 4 |
| JOIN-03 | berry | 1 + 2 = 3 | numeral-total | Phase 4 |
| JOIN-04 | apple | 2 + 2 = 4 | numeral-total | Phase 4 |
| JOIN-05 | berry | 3 + 2 = 5 | numeral-total | Phase 4 |
| JOIN-06 | apple | 0 + 3 = 3 | action-only | Phase 4 |
| JOIN-07 | berry | 4 + 0 = 4 | numeral-total | Phase 4 |
| JOIN-08 | apple | 2 + 3 = 5 | action-only | Phase 4 |
| TAKE-01 | berry | 5 − 2 = 3 | numeral-remainder | Phase 4 |
| TAKE-02 | apple | 3 − 1 = 2 | action-only | Phase 4 |
| TAKE-03 | berry | 4 − 1 = 3 | numeral-remainder | Phase 4 |
| TAKE-04 | apple | 2 − 2 = 0 | action-only | Phase 4 |
| TAKE-05 | berry | 5 − 0 = 5 | numeral-remainder | Phase 4 |
| TAKE-06 | apple | 1 − 1 = 0 | numeral-remainder | Phase 4 |
| TAKE-07 | berry | 5 − 3 = 2 | action-only | Phase 4 |
| TAKE-08 | apple | 4 − 2 = 2 | numeral-remainder | Phase 4 |

`CNT-01` is the sole first native slice: make three berries from five available. `CNT-02` and all other variants belong to the later family pilot. The wider catalog uses targets zero through five and a maximum available set of six. Numbers beyond that are not implied by the asset pack.

For count and transfer goals, a quantity card makes the instruction intelligible with all audio off. Numeral-plus-reference still does **not** prove independent numeral recognition: the child also sees a quantity model and may hear the target. Numeral-total/remainder mode requires an explicit number choice, but configured spoken counting or requested modeled help can limit the independence of that response; both are recorded. Action-only variants finish their action and then model the relationship without inventing a missing total answer.

Three shared layout definitions, `LAYOUT-COUNT`, `LAYOUT-JOIN` and `LAYOUT-TAKE`, define semantic regions and six numbered slots per region in both orientations. Every variant lists its authored occurrence templates, initial region/slot and original return anchor. These are native arrangement rules in normalized region coordinates, not screenshot pixel positions. A runtime round namespaces the template IDs and keeps each identity across movement/resume. The Phase 1 composition review must confirm actual-size spacing; normalized coordinates alone do not prove child touch usability.

Answer-option arrays in the JSON are authored sets. A later native plan may deterministically permute them once per round and persist that order. Do not move choices after an error or always place the correct choice in the same slot. Object IDs and locations stay stable across Undo, pause, rotation and resume.

## 5. Exact narration plan

The script catalog has no unresolved runtime quantity templates. Every variant's initial parameters and result are written as an exact line. Deduplication yields:

| Family | Unique recordings | Why |
|---|---:|---|
| Shared navigation, help, feedback and garden lines | **36** | Welcome/resume/pause/leave, current-checkpoint help, neutral first-miss feedback, completion, play and finite-collection messages |
| Number words zero through six | **7** | Actual current destination count, including return/Undo/overshoot |
| Named reward previews and earned-item lines | **12** | Six predictable items × preview/earned |
| Counting instructions/results | **14** | Seven unique family/target pairs × instruction/result; the two berry-three variants share recordings |
| Joining instructions/results | **16** | Eight exact pairs × instruction/relationship |
| Taking-away instructions/results | **16** | Eight exact transfers × instruction/relationship |
| **Total** | **101** | Unique exact scripts; no generated recordings in this task |

The five audition lines are exactly:

1. `VO-WELCOME`: “Hello! Let’s get our picnic ready.”
2. `VO-COUNT-BERRY-03`: “Put three berries in the basket.”
3. `VO-COUNT-TOO-MANY`: “There are too many. Tap a piece in the basket to give it back.”
4. `VO-JOIN-TOTAL`: “How many are on the shared mat? Choose a number.”
5. `VO-BYE`: “Bye for now. Your garden will be here.”

Compare at most two voice candidates using those same five lines: ten audition takes, five logical scripts. If the selected five performances are accepted and fit the final scripts, they count toward the 101; the remaining **96 unique lines** are then produced. Rejected takes stay preserved. Provider/model, voice, locale, delivery prompt, cost estimate and terms/rights decision are recorded before a requested production run. Nothing in this document initiates a provider call or assumes permission from the parallel Pebble task.

`VO-RETRY-NEUTRAL` says “Not quite yet. Have another look.” on the first valid submitted miss without extra-help attribution. Later directional feedback is offered as a cue; modeled counting is explicit help. Invalid motor events are not submitted math misses. The previously proposed smaller-next-example line is **deferred** because the pilot has no approved adaptive sequence; the current Help, Home and Finish actions remain available.

One voice lane prevents overlap. Explicit replay replaces speech; requested help cancels prompts/counts; a changed object location invalidates a pending number. Normal move-count narration covers the basket or friend’s plate, not assessed joined totals or remainders. A real semantic move, return or Undo cancels stale prompt/help/count speech and may speak only the latest basket or friend-plate count when enabled. The child can deliberately request help again. Input is never locked and no old move count is queued. Joining and remainder checkpoints still withhold automatic assessed totals; only deliberate self-count or requested modeled help can count them. Navigation/background/interruption stops playback and returns silently. Separate narration, spoken-count and effect controls are required. Accessibility announcements must not compete with the prerecorded lane.

Each script records `support_class` (`none`, `cue`, `model`) and context exceptions. A configured “Three.” after a move is ordinary feedback; the same clip in requested step-by-step help is part of a model. Post-success explanations are presentation only. Every checkpoint defines `firstSubmittedCorrect`, `missCount`, `highestSupport`, `modeledCompletion`, `completion`, `deliveredRepresentation` and `spokenCountUsed`. Parent evidence retains support separately for transfer and remainder; ordinary action-only completion does not automatically become “with help.”

## 6. Production sequence and stopping points

### Phase 0 — Finish review of this packet

Resolve the small product choices that affect expensive work: picnic/rabbit theme, whether MathBuddy visually resembles Pebble, the child's starting quantity band, the finite garden reward proposal, preferred voice direction and supported family iPad. Confirm the 24 examples and exact scripts as the first-pilot scope or amend them before generation. Register content, art direction, provider and implementation decisions separately.

**Deliverable:** reviewed specification, selected scope, catalog version and a decision record. **Stop:** no bulk art, recordings or app work follows automatically.

### Phase 1 — Small art, motion and voice audition

When requested, prepare two deliberately different visual directions using the same content: a character identity sheet with attentive/pleased comparison, one count-three/count-five iPad composition, one garden composition with pinwheel/free flower/Finish, and a pickup-return-settle storyboard. Compare a warm paper illustration direction with a cleaner soft-shape storybook direction; do not add extra themes or characters merely to make the comparison larger.

Alongside those boards, draft the seven motion contracts with named layers, pivots, occlusion rules, start/end states, proposed duration, repeat policy, interrupt/rapid-input behavior and Reduced Motion equivalents. Review the contracts before producing the final layer pack. This is motion specification, not a native app or production animation engine.

Audition two voices with the five fixed lines above. Include a silent scene comparison so attractive narration cannot mask a confusing visual goal. The review sheet has distinct decisions for character, objects, composition, motion, voice, wording and provider/rights.

**Deliverable:** two comparable direction boards, seven provisional motion/layer contracts, ten voice audition takes if two candidates are selected for production, an adult listening sheet and recorded selections. **Stop:** choose/revise the direction; approval of a voice does not approve every later recording.

### Phase 2A — Character, environments and identity

Produce the nine logical requirements listed above only in the selected direction. Preserve each take and generation prompt. Review all five Pip poses together; check that the supportive pose is calm and never disappointed. Review both scene orientations with safe regions and intended iPad-size controls overlaid. Approve the motion-compatible anchors and layers before export.

**Deliverable:** nine requirement records, aligned pose sheet, layered scene sources/exports, icon/wordmark sheet and art decisions. **Stop:** repair identity, crops or layer errors before making more props in a wrong direction.

### Phase 2B — Math pieces, reference cards and controls

Produce the 42 definitions/components. Review berry and apple sets at zero, one, three, five and six; show their availability/selection/help/completion states without changing recognizable quantity. Test basket visibility and source/destination separation in static storyboards. Show `REF-00…05` with both families, plus the numeral and control state sheets.

**Deliverable:** selected object/prop media, native design recipes, actual-size contact sheets, state coverage and anchors. **Stop:** require clear counting and a complete silent goal before moving to visual decoration.

### Phase 2C — Reward collection

Produce the earned pinwheel, free flower and five decorations. Review the seven-item full garden, the empty/first-visit garden, one complete spin/bloom cycle and the state after the sixth earned item. Reserve placement bounds so future re-entry cannot hide a control or math target. The optional reward remains available after leaving math early; only the new completion item depends on a completed session.

**Deliverable:** seven requirement records, toy layers/states and progression sheet with exact reward-script links. **Stop:** confirm the reward feels appealing, has a clear end and makes only promises covered by the pack.

### Phase 2D — Finish motion and sound

Finalize the seven briefs/storyboards against the selected layers, then produce the remaining approved voice lines in small batches. Suggested review order: navigation/counting/number words; joining; taking away including zero; rewards and collection complete. These are review groups of the 101 catalog entries, not extra script families. Produce six subtle effects. Background music remains excluded.

For every line, record the exact spoken text, take ID, request, provider/model/voice, source file and selected export. Listen to all selected files in context, not just a random sample. Check words, number pronunciation, pauses, warmth, unexpected speech/noise and level. A noisy/clipped source is rerecorded or rejected; quieting its export does not clear the original problem. Keep technical and listening decisions distinct.

**Deliverable:** all seven final motion packages, 101 approved script/recording mappings, six effect mappings, masters, selected exports and review decisions. **Stop:** no missing line is silently replaced by native speech synthesis, remote synthesis or a misleading generic phrase.

### Phase 2E — Package, audit and hand off

Validate every dependency in all 24 content records against selected assets. Check arithmetic, options, zero cases, given targets versus assessed answers, silent instructions, support labels and finite reward scripts. Confirm no unreviewed experiment, unused take, credential or production utility is in the selected-delivery folder. A native illustration recipe must have a selected design version even when it produces no media file.

**Deliverable:** the reviewed full pilot pack, contact sheets, listening review, native component/motion specifications, decision ledger and handoff. **Stop:** this closes asset readiness only. The user separately selects the first implementation phase; successful media validation does not start it.

## 7. Schemas, naming and future folder contract

Planning files are present now. The following `assets/production/picnic-v1/` tree is a **future proposed location**, not a claim that this pack exists:

```text
catalog.json                         Full logical inventory, provenance and reviews
prompts/                             Exact image prompts, per take
requests/                            Exact voice requests, no credentials
masters/images/<ID>/<take>/           Preserved image sources and layers
masters/audio/en-US/<ID>/<take>.wav   Preserved original recordings
motion/M01…M07/brief.json              Layer/pivot/timing/interrupt/static contracts
motion/M01…M07/storyboard.pdf          Reviewed beginning/middle/end states
review/contact-sheets/                Actual-size scenes and visual states
review/listening/                     Adult playlist and notes
metadata/review-decisions.json        Separate human and technical decisions
metadata/validation.json              Counts, dependency checks and file measurements
metadata/provider-rights.json         Provider/source/license decision
metadata/replacement-history.json     Superseded takes and reasons
delivery/manifest.reviewed.json       Only selected approved versions and hashes
delivery/images/                     Native-ready layers or image assets
delivery/audio/en-US/<ID>.m4a          One selected playback export per script/effect
delivery/content/content-catalog.json Reviewed version of the 24 records
delivery/design/native-components.json Native-only glyph/control/reference recipes
```

IDs are semantic and stable across takes. Examples: `PIP-03`, `OBJ-BERRY`, `REF-03`, `CNT-01`, `VO-COUNT-BERRY-03`, `M01`. Source take paths may add `v01-t01`, but a replacement does not rename the logical asset. Layer suffixes are explicit, such as `REWARD-PINWHEEL-rotor.png`, and the manifest records pivot coordinates in a named coordinate system. Never overwrite a rejected master or silently update a selected export behind an existing hash.

A full catalog record must include:

```json
{
  "id": "PIP-03",
  "version": 1,
  "selectedTake": null,
  "featureIDs": ["F05", "F08"],
  "sceneIDs": ["help"],
  "role": "decorative-supporting-character",
  "dependencies": ["M04"],
  "sourcePaths": [],
  "exportPaths": [],
  "layerAnchors": {},
  "exactPromptOrTranscript": null,
  "providerModelVoiceOrSource": null,
  "rightsDecision": "pending",
  "technicalReview": {"status": "not-run", "evidence": null},
  "humanArtReview": {"status": "pending", "reviewer": null, "date": null},
  "humanContentReview": {"status": "pending", "reviewer": null, "date": null},
  "humanListeningReview": {"status": "not-applicable", "reviewer": null, "date": null},
  "replacementOf": null,
  "decisionNotes": []
}
```

Audio records additionally carry exact script ID, locale, sample rate/channels, duration and cue needs. Motion records name all layers, triggers, start/end state, total duration, interruption result, maximum repeats, Reduced Motion alternative and semantic-state exclusions. Native-only designs carry a versioned recipe path instead of pretending a raster export is missing.

The reviewed delivery manifest pins each approved record to an immutable selected file or native design recipe, SHA-256, actual format/dimensions/duration, dependency IDs and the separate review-decision references. The future importer must reject missing media, duplicate IDs, unapproved selections and unresolved dependencies. Its Swift compatibility is not claimed until the selected native phase actually validates it.

Each human decision records artifact ID/version/take, review kind, reviewer, date, approve/revise/reject and notes. Technical measurements are separate fields, not a stage that automatically becomes approval. The CSV currently marks all human reviews pending.

## 8. Acceptance and evidence for the asset pack

Technical checks:

- Every required logical ID exists exactly once; content/audio/native-design dependencies resolve; the six-session reward mapping is finite and complete.
- All selected media decode. Alpha is genuine where required; the icon is opaque; layer dimensions and pivots match their reviewed recipe. No label or arithmetic answer is accidentally painted into a scene.
- Every audio export maps to one exact script or original effect definition. Durations, channels, checksums and source/finishing history are recorded; no missing number-zero or number-six file remains.
- The catalog has eight examples per activity, valid arithmetic/options and correct phase assignment. Every count/transfer has a silent quantity goal; no hidden total leaks through accessibility labels or target cards.
- No runtime service, provider SDK, credential, unselected take, generated review screenshot or experiment folder is part of delivery. A browser review gallery, if later requested, is an adult production tool and never the iPad app.

Human checks:

- Review the five character poses and every selected illustration at actual iPad viewing size, including all object/reference states and portrait compositions.
- Listen to all 101 selected narration lines and six effects. Confirm exact wording, intelligible numbers, natural delivery, consistency and absence of unwanted sound.
- Review the 24 examples and their evidence claims. Approve or revise zero, joining-empty and subtract-zero examples explicitly.
- Review each motion as a finite sequence, including rapid reversal, interruption and Reduced Motion. Verify that still scenes still communicate the math.
- Record rights/provider acceptance for this pack and the selected outputs. No provider decision from Pebble is silently inherited.

The pack is ready for the selected native phase only when every essential entry has approved applicable human/content/listening/rights decisions and completed technical checks. Physical-device touch, audio cancellation in the actual app, assistive use and child comprehension are later native/family evidence; asset review cannot claim them.

## 9. Pebble evidence and boundaries

Pebble's [asset task](/Users/devan/Projects/BrightPebble/tasks/asset-production.md) separates media ownership from app code. Its [core asset handoff](/Users/devan/Projects/BrightPebble/assets/production/core-5-v1/ASSET-HANDOFF.md) retains stable IDs, exact requests, masters, selected exports, replacement takes, technical measurements and distinct listening/content decisions. Its [review checkpoint](/Users/devan/Projects/BrightPebble/docs/review-checkpoint.md) separates design selection from native/content acceptance. These are observed workflow practices, not proof that every Pebble asset has final human approval.

No Pebble source or media was modified or imported during this planning review. MathBuddy adopts the process, not the assumption that another app's selected character, voice, educational data or validation is automatically suitable here.

## 10. Verification of this planning delivery

The planning JSON and CSV were parsed locally. Three layout definitions and every occurrence’s initial region/slot were also checked. The proposed 24 variants contain eight entries per activity; all arithmetic, quantity limits, answer sets, asset references and voice references were checked. The 101 scripts are exact-text unique. All mapped experimental candidate paths were checked for existence. This verifies planning consistency, not media quality or an implemented app. No image/audio generation, external provider request, native source change or app build occurred in this task.
