# Direction B — next steps and bounded session prompts

**October 3, 2026 · Direction B selected by the user · Planning only in this turn.**

The selected reference is [Direction B, take-02](../../assets/production/picnic-v1/masters/images/DIRECTION-B/take-02/board.png): clean soft shapes, warm color and clear separation between the illustration and the math. The [decision record](../../assets/production/picnic-v1/metadata/direction-selection.json) records the selection. Pip’s Picnic remains a working concept. The final name, detailed character identity, individual assets, motion and voice decisions remain open.

## Recommended order

1. **Five Pip poses first.** Produce only `PIP-01…05`, review them together, and settle face/body/scarf/ear consistency. Recommend using the attentive pose’s ear construction consistently; this is a proposed refinement for review, not an additional user decision already made.
2. **World and branding next.** After the character review, produce `ENV-01…02` and `BRAND-01…02`. Confirm the family iPad and final name before final device exports and naming approval. Provisional canvases and the working name can support review while those choices are pending.
3. **Finish the voice audition independently.** Ten request files already exist, but no recordings exist. Cedar/Marin with OpenAI are prepared candidates, not a selected provider or voice. Use the third prompt only if that provider choice is wanted and credentials are configured locally.

Each prompt below starts a separately bounded batch when the user submits it. This document does not start generation. Stop after each batch’s review checkpoint. Later work follows the asset plan: 2B math pieces/interface → 2C garden assets → 2D motion/audio → 2E package audit. The first native phase remains `CNT-01` only and requires a separate request after essential asset review.

## Prompt 1 — five aligned Pip poses

```text
Continue MathBuddy in /Users/devan/Projects/MathBuddy.

1. Context
I selected Direction B: clean soft-shape storybook. Execute only the character
portion of Phase 2A: PIP-01 through PIP-05. This is a review batch, not final
approval of the identity. Pip’s Picnic remains the working concept.
I authorize this bounded image-generation batch and a local Git checkpoint.

2. Codebase Overview
The eventual app is native SwiftUI with native motion and bundled offline audio.
Existing app code and experimental media remain preserved and unapproved.
Use the approved rendering direction in DIRECTION-B/take-02/board.png, not
experimental assets as an implicitly approved production source.

3. Tasks
- Inspect Git/instructions; review lessons and update tasks/todo.md with scope
  and acceptance checks before generation. Use a focused review agent.
- Produce PIP-01 idle-welcome, PIP-02 attentive-pointing, PIP-03 supportive-thinking,
  PIP-04 pleased and PIP-05 farewell as five aligned transparent still poses.
- Preserve the reference’s face, body proportions, cream coloring and scarf.
  Propose consistent ear construction based on the attentive reference rather
  than a new ear shape for each expression. Mark this identity refinement
  pending human review. Supportive-thinking must feel calm, never disappointed.
- Use a common provisional 1536×1536 RGBA canvas, character scale, foot baseline,
  safe box and anchor/pivot. No articulated rig, sprite sequence or text.
- Preserve every original take, exact prompt, generation/edit request, reference,
  source path, hash and provider provenance using the asset plan’s folders.
  Keep alignment/export recipes reproducible; do not overwrite rejected takes.
- Inspect decoded outputs and alpha on light/dark backgrounds. Measure canvas,
  silhouette bounds, baseline and anchor consistency; inspect ears, scarf,
  anatomy, crops, halos and identity across all five poses. Show a labeled pose
  sheet and small-size readability previews. Preview pixels do not prove
  physical iPad usability. Report capability gaps instead of inventing layers.
- Record technical results separately from human art/identity approval. Present
  all five together with a recommendation, then create a secret-scanned checkpoint.
- Stop for character review. Do not produce environments, branding, math pieces,
  rewards, audio or later phases. Do not modify/build the app or change Pebble.

4. File Locations
Read tasks/lessons.md, tasks/todo.md, docs/review-checkpoint.md,
docs/planning/asset-production-plan.md, docs/planning/asset-register.csv,
docs/plans/2026-10-03-direction-b-next-steps.md and
assets/production/picnic-v1/metadata/direction-selection.json.
Reference: assets/production/picnic-v1/masters/images/DIRECTION-B/take-02/board.png.
Review motion/M04, M05 and M07 under assets/production/picnic-v1/.
Deliver into assets/production/picnic-v1/prompts/, masters/images/PIP-01…05/,
review/contact-sheets/ and metadata/ according to the folder contract.

5. Acceptance Criteria
Five concrete transparent poses, common alignment record, preserved provenance,
actual image/alpha inspection and a review sheet. Human approvals remain pending.
Final response: sample links, technical limitations, commit hash and the next
identity decision. No unrelated media or native implementation has begun.
```

## Prompt 2 — layered world and branding

Use this after the character batch has a recorded human decision. If that decision is missing, reconcile it before producing dependent artwork.

```text
Continue MathBuddy in /Users/devan/Projects/MathBuddy.

1. Context
Continue Direction B after the five-pose character review. Execute only the
remaining Phase 2A requirements: ENV-01, ENV-02, BRAND-01 and BRAND-02.
I authorize this bounded asset batch and a local Git checkpoint. Read the latest
character decision; do not infer identity approval from a technical pass.

2. Codebase Overview
Native SwiftUI is the eventual application. This batch creates source artwork,
layer exports and branding recipes only. Preserve all experimental app/media.
Use selected B and reviewed character references with their actual recorded scope.

3. Tasks
- Inspect Git/instructions; update tasks/todo.md with acceptance checks. Read the
  asset register and provisional motion contracts before painting dependent layers.
- Produce ENV-01 picnic-working-scene and ENV-02 garden-scene, each with distant
  scenery, ground plane and edge foreground in landscape and portrait: 12 actual
  registered layer exports total, with editable/reproducible source composition.
- Provisional canvases are 2732×2048 landscape and 2048×2732 portrait. Inspect
  project context for the intended family iPad; if unknown, keep device targets
  and final exports pending rather than claiming these canvases cover every iPad.
- Reserve clear semantic working regions, framed quantity-reference space,
  guide/control areas and garden toy/Finish areas in both orientations. Use
  diagnostic outlines from existing layout/motion records to review clearances.
  Do not bake UI, labels, numerals, lesson fruit, Pip, rewards or earned decorations
  into backgrounds. No decorative duplicates that look like countable pieces.
- Deliver BRAND-01 as a reproducible wordmark/type recipe with font provenance,
  and BRAND-02 as an opaque 1024×1024 square icon without a baked platform mask.
  Use Pip’s Picnic as the explicitly provisional name unless I have selected a
  final name in this session. Do not represent the working name as final approval.
- Preserve all takes, prompts/requests, sources, layer registration, safe regions,
  hashes and provenance in the asset plan’s folders. Inspect actual layer alpha,
  composite reconstruction, crops and both orientations. Show a layer-exploded
  sheet, clean composites and separate annotated clearance previews. A flattened
  board or three copies of it do not satisfy the three-layer requirement.
- If the available tool cannot deliver true registered layers or editable source,
  report that precise gap and continue independent branding/review deliverables.
- Separate technical checks from human world, name, icon and composition decisions.
  Use a focused review agent, scan the diff for secrets and checkpoint the batch.
- Stop at the Phase 2A world/branding review. Do not start Phase 2B/2C, audio,
  final motion, native app edits/builds or Pebble changes.

4. File Locations
Read tasks/lessons.md, tasks/todo.md, docs/feature-spec.md,
docs/planning/asset-production-plan.md, docs/planning/asset-register.csv,
docs/planning/content-catalog.json, docs/plans/2026-10-03-direction-b-next-steps.md.
Reference assets/production/picnic-v1/metadata/ and the latest reviewed PIP sources.
Review all seven briefs in assets/production/picnic-v1/motion/.
Deliver into that package’s prompts/, masters/images/ENV-01…02/ and BRAND-01…02/,
review/contact-sheets/ and metadata/. Keep approved delivery separate from candidates.

5. Acceptance Criteria
Four logical requirement records, 12 real environment layers, source/registration
records, branding sheet and both orientation previews with technical findings.
Unresolved name/device/layer limitations are explicit. No approval is inferred.
Final response includes samples, commit hash and the decisions needed next.
```

## Prompt 3 — finish the ten voice audition takes

This can run alongside character/world review. Submitting this prompt selects OpenAI for this audition only; it does not select a final voice or approve the remaining narration. Credentials must be configured locally, never pasted into a prompt.

```text
Continue MathBuddy in /Users/devan/Projects/MathBuddy.

1. Context
Complete only the missing Phase 1 voice audition. I choose OpenAI for this
audition and authorize ten takes using the prepared Cedar and Marin requests,
plus a local Git checkpoint. No final voice or full narration pack is approved.

2. Codebase Overview
Natural prerecorded audio will eventually be bundled for offline native playback.
Ten exact request files and a listening sheet exist; zero recordings were produced.
Keep the two candidates comparable with the same model, delivery instructions,
locale and five catalog lines. Preserve all request/take history.

3. Tasks
- Inspect Git/instructions, speech skill and existing voice requests; update
  tasks/todo.md. Check configured credentials without printing them. Do not obtain
  keys from sibling projects, commit secrets or substitute system speech.
- Use the prepared Cedar/Marin requests, five lines each. If their provider/model
  is unavailable, report the exact capability gap and prepare alternatives for
  review rather than silently changing provider, voice or wording.
- Before live requests, estimate the ten-take cost and record the provider's
  current terms/rights review using official sources. Keep the human rights
  decision separate; do not imply a pending decision has already been made.
- Exact lines, including punctuation:
  VO-WELCOME: Hello! Let’s get our picnic ready.
  VO-COUNT-BERRY-03: Put three berries in the basket.
  VO-COUNT-TOO-MANY: There are too many. Tap a piece in the basket to give it back.
  VO-JOIN-TOTAL: How many are on the shared mat? Choose a number.
  VO-BYE: Bye for now. Your garden will be here.
- Preserve original WAV takes, exact requests, script snapshot, model/voice/locale,
  delivery instructions, generation date, source paths, hashes, cost information
  where available and provider/rights notes. Do not overwrite rejected recordings.
- Decode every take; measure duration, format, silence, clipping/levels and inspect
  waveform. Listen/transcribe every actual output against the catalog verbatim;
  request text alone does not establish what was spoken. Record any inaccessible
  listening/transcription capability as a limitation, not an exact-wording pass.
- Update the adult comparison player with both voices in the same line order,
  preserved originals and any disclosed playback-level adjustment. Separate
  technical checks from human warmth, pacing, wording and provider/rights choices.
  Clearly disclose in the player and final presentation that these are AI-generated
  audition voices.
- Present the ten takes together with findings; secret-scan and checkpoint.
- Stop at voice selection. Do not record the remaining 96 lines, sound effects,
  artwork or app changes. Do not change Pebble.

4. File Locations
Read tasks/lessons.md, tasks/todo.md, docs/planning/voice-script-catalog.json,
docs/planning/asset-production-plan.md and
assets/production/picnic-v1/requests/voice/README.md and request-manifest.json.
Use assets/production/picnic-v1/requests/voice/ for immutable requests,
masters/audio/en-US/<script-ID>/<take>.wav for original takes,
review/listening/ for comparison and metadata/ for provenance/results.

5. Acceptance Criteria
Ten actual decoded takes, exact-wording evidence or explicit gaps, a functioning
comparison player and complete provenance. Human voice/wording/rights decisions
remain pending. Final response: listening link, findings, cost/gap and commit hash.
No full narration pack or native implementation has begun.
```

## Current planning checkpoint

Direction selection is recorded; new media generation has not begun. The ten voice recordings are still missing. The first recommended execution prompt is **Prompt 1**. Character review then determines whether to keep the proposed ear construction or request a focused repair before dependent scenes and branding.
