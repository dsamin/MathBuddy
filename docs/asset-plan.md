# MathBuddy — pilot asset plan

**Proposed inventory · October 3, 2026 · Production has not been approved.**

This defines the art, motion, audio and learning content to review before implementing the agreed first native iPad experience. It does not start generation. The existing images, sounds and native pieces are unapproved candidates recorded separately in the [experiment register](experiments/README.md).

## Detailed production packet

The [asset production plan](planning/asset-production-plan.md) expands this overview into an exact [asset register](planning/asset-register.csv), [24-variant content catalog](planning/content-catalog.json), and [draft voice-script catalog](planning/voice-script-catalog.json). They define requirements and proposed scripts; no production files or approvals are implied.

## Creative brief

Recommend a warm illustrated picnic garden: recognizable fruit, tactile paper textures, a friendly expressive guide, simple rounded controls and a quiet working area. Detail belongs around the scene; countable objects must remain clear. The same character identity, lighting, scale and visual language should carry across Home, activities, help and rewards.

Review two or three deliberately different directions in Phase 1, then choose one. The current cream/forest/coral watercolor direction is one candidate, not an approved palette. Do not derive the final design from whichever experimental files already exist.

**Native delivery constraint:** illustrations are scene components; text, numbers, hit areas and state stay separate. A complete screen exported as a single image is not the app's interface. Layer objects that must move independently. A flat pose image can support a crossfade or small transform; it is not an articulated character rig.

## Small direction sample — before the full pack

Produce only these when Phase 1 is selected:

- One guide identity sheet with consistent front/three-quarter proportions and an attentive/pleased comparison.
- One learning scene showing three and five individually countable objects at iPad viewing size.
- One garden reward composition with a pinwheel and a clear stopping action.
- A short storyboard or motion study for pickup, return and a settling celebration.
- A voice audition using the same five short lines across candidates: welcome, count-three, gentle correction, joining question and goodbye.

Review character appeal, readability, silhouette/scale consistency, voice warmth, number clarity and whether the scene feels inviting without competing with the task. A sample direction decision precedes mass generation.

## Production dependencies before final assets

Freeze the proposed content IDs, target/response representations, scripts, screen compositions and state/layer/motion briefs before final exports or bulk recording. In particular, sound-off play needs a noninteractive target reference, and mathematical objects need unobscured, independently movable layers. The asset register and exact draft catalogs in `docs/planning/` make these dependencies checkable; human approval remains a separate step.

## Proposed full pilot inventory

Stable IDs below describe logical assets. Export counts depend on the selected native rendering method and animation design; this is not a claim that every row equals one PNG.

| IDs / family | Proposed scope | Required states and purpose | Review evidence |
|---|---|---|---|
| **PIP-01…05** | Five core poses: idle/welcome, attentive/pointing, supportive/thinking, pleased, farewell | Consistent identity, gaze and scale; neutral encouragement after mistakes; beginning/end poses for each motion | Pose contact sheet on light/dark test grounds and in lesson compositions |
| **ENV-01…02** | Picnic working scene and garden scene, sharing one visual world | Foreground/background layers; clear object area; portrait and landscape compositions; safe regions for controls | Annotated iPad composition sheets, including mini-sized and larger-text layouts |
| **OBJ-BERRY / OBJ-APPLE** | Two recognizable object families; berry and apple are candidates | Available, pressed, moving, placed, returned, counting-highlighted, help-highlighted, completed; color remains clear when input is disabled | Every pilot quantity 0–6 including overshoot; alternate arrangements; no decorative duplicates that look countable; larger quantities are later scope |
| **PROP-BASKET** | Basket with back/front layers or equivalent vector treatment | Empty/full; counts stay visible; rim and handle do not obscure the quantity | Packing and returning sequence with every object identifiable |
| **PROP-MAT-A/B / PROP-PLATE** | Two group mats and a friend's plate | Separate/joined groups; source/destination distinction; empty group; non-color labels or cues | Count, joining and taking-away storyboards |
| **NUM-00…06 / MARKS** | Numerals 0–5 for pilot learning targets and 6 for overshoot feedback; broader target quantities later and +, −, = in native text/vector form | Normal/focused/selected states; legible 1/7 and 6/9; no equation before the intended reveal | Numeral sheet at intended size; quantity and equation compositions |
| **UI-CORE** | Play, home/pause, listen, undo, help, confirm/continue, finish and adult-entry symbols; session dots | Normal/pressed/disabled/focused states with generous hit regions | Screen contact sheets; accessibility names and intent |
| **REF-00…05** | Quantity-reference cards for given targets, including an empty frame for zero | Match the active object family; clearly framed/noninteractive; usable without narration or numeral reading; never depict an assessed joined/remaining answer | Sound-off counting/sharing storyboard; separately tagged quantity-copy evidence |
| **CUE-DEMO** | A gentle demonstration hand/path or highlight | Show one action, then disappear; never obscure a target or keep prompting indefinitely | A storyboard for first interaction and help |
| **REWARD-PINWHEEL** | One interactive toy with separate base/stem/rotor as needed | Preview, available-to-place, placed, activated, settled, revisited; no endless automatic spin | Placement and one complete spin sequence, plus Reduced Motion alternative |
| **REWARD-FLOWER** | One freely available garden interaction | Idle, touched, bloom and settled; accessible before any earned reward | First-visit garden composition and short toy-play storyboard |
| **DECOR-01…05** | Five permanent decorative additions, proposed | Distinct, placeable and visible; e.g. mushroom, lantern, stepping stone, bunting and birdhouse | Garden progression sheet with uncluttered placement slots |
| **BRAND-01** | Wordmark treatment and app-icon direction | Consistent with chosen guide/world; icon identity remains clear at small size | Small-size icon sheet; final export happens after direction approval |

**Reward coverage proposal:** first completed session earns the pinwheel; the next five earn the five reviewed decorations. After that initial set is complete, completion offers a familiar garden play moment without promising an unmade new object. No reward disappears and no play requires refilling energy. Review this bounded pilot policy before producing the reward pack.

## Screen-to-asset map

| Scene | Essential visual assets | Essential audio/motion |
|---|---|---|
| Home / return | Pip idle, garden composition, Play/Garden/Adult controls | Welcome or resume line; restrained greeting |
| Counting | Object family, basket layers, prompt/control treatment | Target prompt; pickup/return; too-few/too-many help; optional spoken counts; completion |
| Joining | Two mats, both object families available as variants, numerals/equation | Join/separate sequence; total prompt; counting help; explanation |
| Taking away | Starting mat, friend's plate, objects, quantity choices | Transfer/return; transferred-set check; remaining-quantity prompt; explanation |
| Help / success | Supporting/pleased poses, focus cue, relevant math pieces | Authored help steps; non-overlapping guidance; finite celebration |
| Garden / goodbye | Background layers, owned toy/decor, free flower, farewell pose | Reveal/place/play/settle; clear goodbye; no pleading to continue |
| Grown-ups | Simple native layout and labels, optional small guide accent | No decorative audio needed; full text remains understandable silently |

## Motion specifications

Each motion brief must name the trigger, layers, starting/ending state, approximate duration, repeat policy, behavior during rapid input/interruption and a Reduced Motion version. Timing ranges below are proposed starting points for review.

| Motion ID | Meaning shown | Proposed behavior | Reduced Motion / interruption |
|---|---|---|---|
| **M01 Pickup / return** | One object changes location | 200–300 ms; destination remains clear; input cannot clone an object | Immediate placement plus highlight; restore the saved location |
| **M02 Join / separate** | Two sets become one and can separate | 350–500 ms; every object remains visible and retains identity | Before/after grouping; undo restores the original sets |
| **M03 Share / remaining** | Some objects move away; source quantity changes | Separate transfer and remaining-total moments; no automatic extra question during motion | Static source/destination states with clear focus |
| **M04 Help** | Demonstrate or count one object at a time | Brief focused cue; no decorative motion competing with the explanation | Sequential highlight or accessible alternative |
| **M05 Completion** | Appreciate effort and show the mathematical result | 1–2 seconds maximum target, then settle; Continue remains obvious | Pleased pose and calm highlight |
| **M06 Garden toy** | Place a reward and choose to play | One spin/bloom per deliberate action; clear end | Static settled toy or brief state change |
| **M07 Greeting / farewell** | Establish a friendly beginning/end | One restrained gesture; no ongoing idle demand for attention | Still pose; no pressure to return |

Review storyboards or short clips before app integration. Keep quantities, reward grants and learning evidence independent of animation timing. Final touch feel, playback and interruption behavior must still be verified later in the native app.

## Voice and sound inventory

Use exact reviewed scripts with stable IDs. File count follows the selected lesson variants, not the size of the experimental voice pack.

| Family | Script coverage |
|---|---|
| **VO-WELCOME / RESUME / BYE** | Enter, return to saved work, pause/leave and a calm ending |
| **VO-COUNT** | Targets within the agreed band; basket instruction; too few/too many; return/undo explanation |
| **VO-NUMBER-00…06** | Clear number words including zero and six for over-packing; cover the maximum available set, not just correct targets; extend through ten for the broader release and confirm in-context sequencing |
| **VO-JOIN** | Initial groups, join action, total question, counting support and the final relationship |
| **VO-SHARE** | Initial quantity, requested transfer, transfer-check feedback, remaining-total question and explanation |
| **VO-HELP** | Revoice, focus and model; separate scripts for each activity. Easier-next-example narration is deferred with adaptive selection |
| **VO-REWARD** | Accurate reward preview, earned item, placement, garden replay and collection-complete messaging |
| **SFX-CORE** | Subtle pickup, placement/return, confirmation, reward and toy cues; avoid startling error sounds |

Prompts, optional spoken counting and effects have separate controls in the proposal. **Background music is deferred for the first pilot**; no music pack is required. Voice provider and voice identity are selected only after the MathBuddy audition. A provider choice already made for Pebble does not approve the same choice here.

Human listening review covers exact wording, mathematical correctness, natural pacing, warmth, number pronunciation, pauses, absence of unintended speech/noise and consistent loudness. Technical checks cover decoding, durations, unwanted clipping, file references and integrity. Record these as separate decisions. A clean waveform does not establish a good teaching voice.

## Content accompanies the assets

The draft catalog enumerates **24 authored variants** for the complete family pilot: eight quantity-making, eight joining and eight taking-away variants. These are proposed content definitions, not 24 independently painted screens. Reuse the approved components across reviewed arrangements and two object families.

Proposed pilot targets are within 0–5 and available sets within 0–6. Any later increase to available objects requires a matching spoken-count/feedback coverage review, even if the correct answer remains five.

Each variant records the instruction representation actually delivered (spoken target versus visible quantity reference), the support role of each feedback script, and separate transfer/total checkpoints where relevant.

Each variant records the learning objective, quantity band, starting objects, expected action, answer representation, support sequence, asset/audio IDs, accessibility treatment and acceptance example. Separate pre-numeral action experiences from independent total-recognition questions. Review zero and empty sets explicitly before including those variants. Do not infer mathematical equivalence from attractive artwork.

## Review record and handoff

Proposed production location, once that work is requested: `assets/production/picnic-v1/`, with masters, exports, scripts, motion briefs, review sheets and a manifest. Existing experimental files remain separate in status.

Each manifest entry should contain: stable ID, intended scene/feature, mathematical versus decorative role, version/take, exact prompt or transcript, source/export paths, dimensions/format or duration, layer/motion dependencies, accessibility notes, provider/rights notes, technical-check result, human-review decision/date and replacement history.

Track decisions independently: **draft → technical check complete → human review pending → approved / revise / rejected**. A new take preserves the old one and its notes. Every essential dependency for the agreed pilot must be approved before its native phase uses it. Optional deferred assets cannot silently remain promised features.

The final handoff includes the contact sheets, listening playlist, state coverage matrix, selected exports, transcripts and motion specifications. Later device findings may require revisions; asset approval is a production baseline, not proof that integration or child usability already works.

## Existing candidates

Two Pip poses, one garden background, icon studies, native vector pieces, 19 voice clips and three effects already exist from the premature experiment. All remain **unapproved candidates**. They do not cover this full inventory, and they do not decide the theme, voice, rendering approach or reward policy. Audit them against the approved direction before deciding what, if anything, to reuse.
