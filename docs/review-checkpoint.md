# MathBuddy — independent review and planning checkpoint

**October 4, 2026 · Authorized character batch complete for review · Human identity/art approval pending**

The [five Pip poses](../assets/production/picnic-v1/review/contact-sheets/pip-five-poses.png) are ready together, with [small-size previews](../assets/production/picnic-v1/review/contact-sheets/pip-small-size.png) and a [technical review / limitations](../assets/production/picnic-v1/review/contact-sheets/pip-character-review.md). Only `PIP-01…05` were generated. The attentive-reference unbent ears are proposed consistently across the set. All five aligned candidates are 1536×1536 RGBA with a shared foot baseline and anchor; provider originals, exact requests and reproducible export recipes are preserved. Human identity, art, content and rights decisions remain pending. No other media or native/Pebble work began.

**Preserved October 3 planning checkpoint — earlier scope and evidence below.**

**Recorded October 3 planning status:** Direction B, take-02 is selected for the rendering direction. The [bounded next-step prompts](plans/2026-10-03-direction-b-next-steps.md) are the current execution handoff; submitting that planning document does not start any batch. At that checkpoint, the recommended next batch was five aligned Pip poses (`PIP-01…05`), followed by human character review. Ten voice requests exist and all ten recordings remain missing. Character identity, final name, individual assets, motion, voice and provider/rights decisions remain pending. The specification-review evidence below is preserved from the earlier checkpoint.

The user requested independent agent review of the specifications, a complete account of the assets needed, and a detailed implementation plan following the Pebble workflow. Three agents handled product review, asset/content planning, and native implementation planning. Their outputs were reconciled into the current proposal. Existing app code and experimental assets remain unapproved and unchanged.

## Read in this order

1. [Independent specification review](reviews/2026-10-03-spec-review.md) — findings against the earlier v0.3 packet; preserved as the original review.
2. [Updated feature specification](feature-spec.md) — v0.4 proposal with more precise learning, accessibility, audio and evidence contracts.
3. [Asset production plan](planning/asset-production-plan.md) — proposed production sequence and exact draft catalogs, before any generation.
4. [Detailed native implementation plan](plans/2026-10-03-native-pilot-implementation-plan.md) — proposed responsibilities, interfaces, tasks, tests and review checkpoints for future execution.
5. [Overall roadmap](roadmap.md) — how the phases fit together.

## Pilot at a glance

The proposed first world is a picnic garden: make a set, join snacks, share some away, then enjoy a permanent garden addition. Three rounds are the default; five is an adult option. The activities use native touch controls, offline voice and short, purposeful motion. The full ages-four-to-eight curriculum follows later, one topic at a time.

| Planning inventory | Proposed quantity |
|---|---:|
| Artwork requirements: character poses, worlds, pieces, props and rewards | 22 |
| Native design definitions: controls, numerals, quantity cards, layouts and related treatments | 36 |
| Motion briefs with normal and Reduced Motion behavior | 7 |
| Exact draft voice scripts | 101 |
| Sound effects | 6 |
| Authored activity variants | 24: eight per activity family |

These are **196 logical requirements**, not 196 images. Layer exports and replacement takes are tracked within their requirement. All remain proposals requiring the relevant art, content or listening review. See the [enumerated register](planning/asset-register.csv).

```mermaid
flowchart LR
    A[Review product and scope] --> B[Choose art and voice direction]
    B --> C[Produce and review pilot asset batches]
    C --> D[Build one selected native phase]
    D --> E[Review the actual iPad experience]
    E --> F[Select the next phase]
```

The first native phase has one complete task: make three berries from five available, including help, Undo, silence, completion and resume. Joining, taking away, sessions/rewards and the full parent area follow as separate phases.

## Findings and disposition

| Review finding | Resolution in this planning packet | What still requires review or execution |
|---|---|---|
| **R1 — Approximate content count was not a production ledger** | Enumerate the 24 proposed variants and connect their visual, voice, support and mathematical dependencies in the content/voice catalogs and asset register | Review the exact examples and scripts; produce only the selected, approved assets |
| **R2 — First-slice quantity scope was ambiguous** | Phase 3 is strictly the single count-three-from-five variant `CNT-01`. The full family pilot includes reviewed targets 0–5 with at most six available objects, including explicit zero cases | Confirm the child's starting point; remaining catalog integration is later pilot work, not silently added to Phase 3 |
| **R3 — Assistance and first-answer evidence lacked exact rules** | Separate checkpoint results, first submission, submitted misses, `none`/`cue`/`model` support, modeled completion and delivered representation. Replay/Undo do not erase history | Review parent wording; test the contracts in the owning native phase; do not infer absent adult help |
| **R4 — Silent pre-numeral play and accessible targets were incomplete** | Add quantity-reference cards and picture/action cues; distinguish reference-copying from spoken-target tasks; give the requested quantity without revealing a total being assessed | Review sound-off and nonvisual storyboards before production; later assistive-use checks remain separate from visual review |
| **R5 — Counting audio could become stale or misleading** | Specify one voice lane, latest-state counting, return/Undo/zero coverage, deliberate counting during questions, replay/cancellation and interruption behavior | Listen to approved takes and test rapid input in the native phase; a file check does not establish that speech was heard or understood |
| **R6 — Layer/motion details arrived after final art** | Put content, scripts, composition, layers, anchors, motion states and static alternatives before final exports and bulk recording | Review the briefs, then validate produced art and sound against them; native interaction still follows later |

The original review suggested adding five within the first counting slice. The reconciled plan deliberately keeps that first slice smaller—one authored count-three task—so a complete interaction can be reviewed before expanding content. This is a planning recommendation, not a user approval.

A second integration review identified two further requirements: explicit eligibility for picture/action-only versus numeral-answer content, and reusable layout definitions with stable object occurrences in every content row. The catalogs and implementation plan now specify these. Easier-next-example narration is deferred with adaptive selection, so the fixed pilot sequence makes no unsupported promise.

## Decisions still belonging to the user

| Decision | Working recommendation | Needed before |
|---|---|---|
| Theme, guide and final name | Pip's Picnic, one friendly rabbit, a calm garden remain provisional; review five aligned poses next | Dependent world/branding production and final naming approval |
| Visual relationship to Pebble | Direction B rendering is selected; use the reviewed sample's clarity and a distinct math world | Individual character/world approval; selection does not approve experimental assets |
| Starting ability / response modes | Count-three first; picture-supported/action-only when unsure; numeral questions only when comfortable | Final content selection and child-facing build configuration |
| Voice | Audition warm prerecorded delivery using the same short scripts across candidates | Batch recording; no inherited voice approval |
| Reward collection | Pinwheel plus five permanent decorations, free flower play; honest end-of-collection behavior | Reward art production |
| Target iPad / OS and adult gate | Review the implementation plan's provisional native assumptions on the actual family device | Executing the first native phase |

These open choices do not block writing or reviewing the plan. They do block treating a proposed direction as an approved production baseline. No default here is a submitted answer on the user's behalf.

## Evidence must remain separate

| Evidence class | What it establishes | Current status |
|---|---|---|
| Document review and dependency audit | Scope consistency, mathematical catalog integrity and planned coverage | 23 planning checks passed; [audit record](planning/validation-report.json) |
| Art approval | Character identity, composition, object clarity and states | Direction B rendering selected; character identity and individual assets remain pending |
| Voice/content approval | Correct scripts, understandable numbers, delivery and suitability | Not granted |
| Native engineering checks | State, interaction, persistence, offline behavior and rendering | Future phase work; old experiment checks do not close this row |
| Physical-device / assistive-use checks | Actual touch, orientation, sound, VoiceOver and Reduce Motion behavior | Future phase work |
| Child observation | Whether the child can begin, recover, enjoy and stop | Future family pilot; no efficacy claim |

The audit checked exact IDs and script uniqueness, arithmetic and answer options, all 97 authored object occurrences, both orientation layouts, content/voice dependencies, finite rewards, local document links and existing candidate paths. All 149 tracked app, project, asset, script and mockup files match the pre-review snapshot, with no additions or deletions in those tracked areas. No app build or generated-media check is claimed by this planning audit.

## Recommended next step

**Review the five aligned character candidates now.** Direction B take-02 remains selected. Decide whether to keep or revise the face, body, scarf and consistent attentive-reference unbent ears across `PIP-01…05`. The [pose review](../assets/production/picnic-v1/review/contact-sheets/pip-character-review.md) separates measured technical checks from pending human approval. Dependent world/branding remains a later separately requested batch. See the [copy-ready prompts and acceptance criteria](plans/2026-10-03-direction-b-next-steps.md).

Prompt 2 follows a recorded human character decision. Prompt 3 independently completes the ten missing audition recordings only when the user chooses OpenAI for that audition and credentials are configured locally. Each batch stops at its own human review checkpoint. The first native phase remains `CNT-01` and requires a separate request after essential asset review.
