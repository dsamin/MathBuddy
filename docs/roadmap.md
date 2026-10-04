# MathBuddy — asset-first roadmap

**Planning draft · October 3, 2026 · No implementation phase is authorized by this document.**

## The intended outcome

A beautiful native iPad math app for ages four to eight, initially designed around a five-year-old: recognizable pictures, direct manipulation, short spoken prompts, meaningful animation, gentle help, and completion rewards that invite a little creative play. The current work defines the product, its assets and the detailed phase plan. Each phase will be selected and reviewed before its execution begins.

The recommended first experience is **Pip’s Picnic**: a child packs a basket, joins snacks brought by friends, shares some away, and grows a small garden. It offers one coherent setting and lets the same artwork support several mathematical ideas. The name, rabbit, picnic theme, voice and exact style remain proposals.

## What to review now

1. [Feature specification](feature-spec.md): product scope, learning activities, screens, rewards, parent features, native iPad requirements and concrete examples.
2. [Asset plan](asset-plan.md): what to create, production order, individual states, motion/audio briefs and review criteria.
3. This roadmap: the order of work, dependencies and the outcome of each stage.

The documents form a planning packet. The [review checkpoint](review-checkpoint.md) records the independent findings and links the detailed asset and native plans requested in this review. These documents are not a task queue to execute automatically.

## Phases and stopping points

| Phase | Work, when separately started | Reviewable result | Condition before moving on |
|---|---|---|---|
| **0 — Product agreement (current)** | Refine the first child experience, starting skills, theme, reward policy and native iPad constraints | Agreed feature spec, screen flow and asset inventory | Resolve the first-pilot decisions below; record what is chosen and what is deferred |
| **1 — Creative direction** | Produce a small character/style comparison, one learning-scene composition, a reward composition, a short motion study and a voice audition | A coherent art-and-audio direction board, with selected references | Review character appeal, object readability, calmness, voice and iPad composition; choose the direction before bulk generation |
| **2 — Pilot asset pack** | Produce the agreed artwork, reusable math pieces, required visual states, narration, effects and motion storyboards in reviewable batches | A complete approved asset pack for the first picnic experience, with manifest and handoff | Every essential asset and script is accounted for, technically checked and explicitly reviewed; remaining optional assets are clearly excluded |
| **3 — First native phase: one counting activity** | Review its detailed implementation plan; after that phase is requested, build Home → count three → small completion → leave/resume using approved assets | One polished native iPad interaction, with a focused demonstration and evidence | Touch, quantity, undo, gentle retry, narration, accessibility and interruption behavior pass the agreed checks; review before adding more activities |
| **4 — Complete the picnic loop** | Plan joining groups, taking away, session coordination, parent controls and the garden as bounded subphases; execute one at a time | A coherent short family pilot with saved progress and meaningful rewards | Each subphase meets its own acceptance criteria; the whole session works without scaffolding that only adults understand |
| **5 — Family validation and refinement** | Real iPad checks and short, willing child sessions; refine assets, prompts, motion and difficulty from observations | A family-tested first experience with recorded strengths and problems | The child can start, recover, understand the actions, enjoy the reward and stop naturally; remaining issues are resolved or clearly scoped |
| **6 — Curriculum expansion** | Choose one topic, specify it, make/review its assets, plan its implementation and then build it | Comparison and make-five first; later patterns, shapes, larger numbers, place value and other topics | Repeat the content → assets → phase plan → build → review cycle for each topic |

The user has now requested a detailed implementation plan alongside independent review and the asset inventory. Phase plans can be written now against explicit assumptions, while execution still depends on the earlier product and asset decisions. No phase is pre-approved for implementation. No dates or cost promises are attached before scope, device target and asset direction are selected.

## Phase 2 production batches

The batch order is deliberate; later art depends on earlier visual choices.

1. **Contracts and direction:** freeze the pilot content, asset IDs, screen composition, required layers, motion states, accessibility and exact draft scripts before production exports; audition the direction before mass production.
2. **Character and world:** approved Pip identity and pose set, environment layers, portrait/landscape crops.
3. **Learning pieces:** two countable object families, containers/mats, visible empty states, selection/help states and numeral style.
4. **Reward set:** pinwheel, freely available flower interaction, five proposed permanent decorations, placement and replay states.
5. **Motion and audio production:** use the already reviewed motion/layer briefs and scripts; produce the approved takes and test them against the scene compositions.
6. **Package and audit:** complete scene contact sheets, audio review playlist, content-to-asset matrix, source/export records and human decisions.

Batches can be reviewed individually. A rejected pose or line is replaced by a new take without regenerating the whole pack. “All assets first” means all essential assets for the **agreed pilot**, not every future topic for ages four to eight.

## Proposed build subphases after the asset pack

Phase 3 has a proposed plan for one count-three-from-a-larger-set activity. Review that plan and its selected assets before starting. Phase 4 can then be split into:

- **4A — Joining:** objects combine, remain countable, can be separated again, and support both pre-numeral and numeral variants.
- **4B — Taking away:** transfer a requested quantity, then reason about what remains; reversible actions and help preserve the story.
- **4C — Session and garden:** appropriate three-round sessions, permanent rewards, freely available toy play, duplicate-grant protection and a calm stopping point.
- **4D — Grown-ups and continuity:** starting band, three/five-round preference, sound/motion controls, truthful practice evidence, adult gate and complete resume behavior.

These are boundaries to discuss, not instructions to start coding. Persistence and accessibility needed for the counting phase are not postponed until 4D; that subphase completes the broader settings/reporting experience.

## How each individual phase will be planned

When we select a phase, its plan should contain:

- The child-visible outcome and explicit exclusions.
- Approved feature and asset IDs, with the exact versions to use.
- Tasks and ownership, including dependencies on earlier work.
- Acceptance scenarios, failure/recovery behavior and device/accessibility checks.
- A concrete review deliverable and stopping point.
- Evidence collected, unresolved issues and a separate decision about the next phase.

A successful build does not approve the artwork, educational content or next phase. Likewise, approving an illustration does not authorize app implementation.

## What carries over from Pebble

Pebble provides useful patterns for stable asset IDs, exact voice scripts, preserved masters, review manifests, separate human listening decisions, bounded implementation slices and evidence records. Its assets and implementation have sometimes progressed in parallel; MathBuddy will use the user's explicitly requested asset-first order. See the [refreshed Pebble workflow evidence](research/brightpebble-lessons.md).

Reuse the process and useful design principles first. Do not alter Pebble, assume its selected voice is approved here, or extract a shared code package while the two products are still taking shape.

## Decisions for our next review

| Decision | Working recommendation | What remains open |
|---|---|---|
| First world | One calm picnic garden | Keep Pip/rabbit/picnic, or select a more motivating theme |
| Starting skill | Small-set counting to three, then five | Confirm what your son already does comfortably; do not infer ability from age |
| Relationship to Pebble | Similar clarity and review process, distinct math world | Decide whether the visual identity should also feel like a sibling product |
| Input | Tap-to-move, with a later drag equivalent if it improves play | Evaluate through storyboards first, then the approved native counting phase |
| Reward | Permanent garden additions plus brief toy play | Confirm this is more appealing than a separate mini-game room |
| Sound | Calm prerecorded guide; optional spoken counting and light effects | Audition voice and delivery for MathBuddy; background music is deferred |
| iPad support | Native, landscape-led and portrait-capable | Confirm family iPad model/OS before executing the first native phase |

## Existing work

An experimental native pilot and draft assets were produced prematurely. They remain intact, clearly labeled in the [experiment register](experiments/README.md). They are not the approved design, an approved asset pack, or evidence that a roadmap phase is complete. We may later keep, revise or discard individual parts after review; the plan is not constrained by that experiment.
