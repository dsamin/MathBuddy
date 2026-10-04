# MathBuddy — a little world built with math

**Feature proposal v0.4 · October 3, 2026 · For product review; asset-first planning, no implementation underway**

Working name: **MathBuddy**. Recommended first chapter: **Pip’s Picnic**. Audience: children roughly four to eight, with the first experience centered on a five-year-old. The eventual product must be a proper native iPad app, with native interaction and animation. The current deliverable is this feature specification, an [asset plan](asset-plan.md), and a [phased roadmap](roadmap.md).

## Brief and current boundary

The user wants to agree on the overall experience, then produce and review individual assets, then plan and build individual phases, using Pebble’s learning-app workflow as a reference. Native iPad is a platform requirement, not permission to start implementation during specification work.

The earlier native pilot, browser studies, generated art and audio are **unapproved experiments**. They have been preserved, not selected as the product baseline. Their existence does not approve the design, satisfy the planned asset inventory, or mark a roadmap phase complete. See the [experiment register](experiments/README.md). No new app code or assets are part of this planning reset.

**Confirmed intent:** fun, simple, beautiful, picture-led early math; meaningful animation; appealing completion rewards; native iPad; ages four to eight with an initial focus on the user's son; assets before individually planned implementation phases.

**Proposals to review:** picnic theme and rabbit guide, calm storybook direction, garden reward format, small-set counting entry point, three-round default and tap-to-move. Voice, exact art style, device support target and the child's starting quantity band remain open.

## Feature map

| ID | Feature | Proposed first-pilot behavior | Later scope / boundary |
|---|---|---|---|
| **F01** | Welcoming home | One obvious Play action, My garden, unobtrusive adult entry; resume saved work | Theme/name/character are review choices |
| **F02** | Make a quantity | Select three, then five objects from a larger set; undo and recover from over/under-counting | Broader count/match 0–10 after its content review |
| **F03** | Joining groups | Combine visible sets; separate again; distinguish action-only and total-recognition variants | Counting-on and larger totals later |
| **F04** | Taking away | Transfer a requested quantity, then reason about the remainder; distinct checks | Larger quantities and story problems later |
| **F05** | Support and feedback | Repeat instruction, visual help, reversible moves, calm retry, no lost rewards | Adaptation rules require separate evaluation |
| **F06** | Appropriate sessions | Adult-selected starting band; three rounds by default, optional five; familiar success and variation | Mixed count/add/sub is a review example, not mandatory for beginners |
| **F07** | Garden and toy rewards | Free flower play; predictable pinwheel and small decoration set; no currencies or penalties | Additional toys need their own content/asset plans |
| **F08** | Pictures and motion | Recognizable countable pieces; spatial join/share animations; finite character reactions | Full required states are in the asset plan |
| **F09** | Audio | Auditioned prerecorded prompts, optional spoken counting and light effects; replay and silence work | Background music deferred |
| **F10** | Grown-ups | Starting band, session length, audio/motion controls, honest practice evidence and protected reset | No mastery/age-ranking claims; sharing/export deferred |
| **F11** | Continuity and offline use | Local profile, saved round/object state, owned rewards, reliable offline play | Multi-child accounts and cloud sync deferred |
| **F12** | iPad and accessibility | Native controls/animation, landscape-led and portrait-capable layouts, generous touch targets, non-color cues and accessible alternatives | Real-device and assistive-use checks follow approved implementation |
| **F13** | Curriculum growth | First-pilot feature set remains small | Comparison/make-five next; later shapes, patterns, measurement, place value, sharing and time/money |

The remaining sections define these features in detail. [The roadmap](roadmap.md) determines the proposed order. The user has now requested an independent review and a detailed implementation plan; the resulting plan remains a proposal and does not start execution.

## 1. The experience we are building

A child helps a friendly rabbit prepare a picnic. Counting packs the basket. Joining groups makes enough snacks for friends. Taking some away shares the food. After a short adventure, the child adds something to a little garden and plays with it.

The promise: **“I can make things happen with numbers.”**

The child should be able to understand the next action through a picture, one short spoken sentence, and a gentle demonstration. A successful first experience means curiosity, control, and understanding—not speed or a perfect score. Your request establishes the priorities: simple, beautiful, illustrated, animated, rewarding, and fun. The picnic theme and entry level are proposals until we review them with your son.

The supplied [Muse spec](https://muse.ai/s/kids-math-app-spec-sheet-yxv6w0xmnadsxe) is a good starting point. [The source review](research/source-review.md) records exactly what to keep and change. [BrightPebble lessons](research/brightpebble-lessons.md) separates decisions and implementation observations from evidence actually demonstrated.

## 2. Three possible structures

| Structure | What the child experiences | Strength | Cost / risk |
|---|---|---|---|
| **One growing picnic garden — recommended** | Three little jobs help Pip; the garden changes | Coherent, calm, small art scope, visible ownership | Requires good activity variation so the theme stays fresh |
| A shelf of independent math toys | Choose a counting toy, shape toy, number toy | Immediate freedom, useful for repeat play | Harder to guide a beginner; larger menu and more distinct art |
| An adventure map with several themed worlds | Travel between forest, dinosaurs, and space | More long-term variety, stronger older-child appeal | More content, transitions, progression complexity, and asset work |

Start with the garden and preserve the underlying skill model so later chapters can change the setting. Do not build a multi-world engine first. A small “choose a toy” shelf can become free play after the core learning loop works.

## 3. Product principles

1. **The math is visible.** Objects actually move, combine, or leave; the result is never just an unexplained green tick.
2. **One task, one obvious action.** Large working area, short prompt, replay control, help, and a calm way home.
3. **Children can change their minds.** Undo a move; rearrange; try again. A wrong answer never removes a reward or saddens the mascot.
4. **Help supports play; evidence describes support honestly.** Guided completion earns the same scene reward. Parent progress distinguishes it from an unassisted attempt.
5. **Rewards extend what was created.** One garden addition and optional toy play; no currencies, surprise rarity, lives, streak penalties, or purchases in play.
6. **Learning grows by ability.** Age ranges guide content planning, not labels displayed to the child or automatic placement.
7. **A complete small experience beats a catalog.** Prove one activity and one reward before producing a large content library.

IES recommends developmental progressions for early number learning and monitoring what children understand. That supports a skill sequence and varied examples; it does not validate this app or any proposed mastery threshold. [IES practice guide](https://ies.ed.gov/ncee/wwc/practiceguide/18).

## 4. Scope: family pilot, first release, expansion

| Milestone | Included | Evidence needed before moving on |
|---|---|---|
| **First native slice** | One authored count-three-from-a-larger-set activity, original Pip art, prompt replay, tap-to-move, undo, help, one tiny completion moment | Child can begin and recover from a mistake; animation, audio, and touch are dependable on a real iPad |
| **Family pilot** | Count, join, take away; one garden; three-round session; one local profile; local resume; adult settings; a small set of authored variants | The whole session is enjoyable across several days; repeated taps and interruptions do not duplicate rewards |
| **First broader release** | Count/match 0–10, more/less/equal, make-5, addition/subtraction within 5; optional within-10 variants only after validation; parent evidence summary | Separate skills function, asset/audio coverage is complete, accessibility and device checks pass, and a small mixed-ability family pilot succeeds |
| **Later chapters** | Numbers through 20, make-10, patterns, shapes, measurement, place value, equal groups, fair sharing, simple time and money | Each new skill has a developmental sequence, reviewed examples, and usable interaction—not just a themed quiz |

**Defer:** child accounts, cloud sync, leaderboards, live AI tutor, microphone input, handwriting recognition, subscriptions, user-created content, a multiplayer mode, and multi-child profiles. A physical-object activity suggested to the parent is a small addition, not a separate content platform.

Comparison is deliberately outside the first three-loop family pilot but inside the proposed broader first release. This resolves the conflicting launch/later labels in the source spec.

## 5. Growing from four to eight

These are flexible entry points. A child can be exploring operations while still practicing shape language. The adult can choose a band; no birthdate is required.

| Track / approximate audience | Mathematical ideas | Tactile activity examples | Order of representation |
|---|---|---|---|
| **Discover · roughly 4–5** | One-to-one counting, quantity 0–5 then 10, matching numerals, more/less/equal, simple sorting, basic shapes | Pack 3 berries from a larger tray; match cups to friends; find an empty plate; sort leaves | Objects → spoken quantity → numeral |
| **Build · roughly 5–6** | Parts of 5/10, joining and taking away, counting on, simple repeating patterns, number order to 20 | Two friends bring 2 and 1 snacks; finish a red-yellow-red-yellow bunting; make 5 with two baskets | Objects → five/ten frame or number path → equation |
| **Explore · roughly 6–8** | Add/subtract within 20; tens/ones and two-digit numbers; measurement; shape composition; equal groups and sharing; later halves/quarters, clock and money concepts | Bundle 10 sticks into a fence panel; give 12 berries equally to 3 baskets; measure a bridge in equal blocks; build a shape mosaic | Manipulatives → diagram → symbols and short story |

These are a proposed product progression, not a claim of complete grade coverage. Kindergarten standards explicitly include one-to-one counting, cardinality, zero, and unchanged quantity after rearrangement. Grade-two base-ten work is a useful reference for later place-value scope. [Kindergarten counting](https://www.thecorestandards.org/Math/Content/K/CC/), [grade-two place value](https://www.thecorestandards.org/Math/Content/2/NBT/).

First-release zero examples must work visually: an empty plate is a valid set, with no impossible demand to “tap every object.” Comparison examples vary spacing and item size so a longer-looking row is not always the larger quantity. Shape examples vary rotation and size. Numerical difficulty and motor difficulty are separate controls.

## 6. Information architecture and session rhythm

```text
Grown-up first setup → Child home
                         ├─ Play with Pip → 3 appropriate rounds
                         │                   └─ garden addition → optional toy play
                         │                                        └─ Done / Play again
                         ├─ My garden → revisit and arrange owned items
                         └─ Grown-ups → adult gate → progress and settings

From every round: replay prompt / help / undo where relevant / pause and leave
On return: resume the saved scene, with an optional prompt replay
```

**Home:** Pip and the current garden, one large Play action, smaller My garden action. No skill dashboard, long map, age selector, or badge shelf competing for attention.

**Activity:** home/pause at top left; three neutral pebbles showing session position; audio replay; one short prompt; a large tactile canvas. Help and confirmation sit in a consistent lower area. Numerals appear only when relevant to the learning objective.

**Session:** a familiar success, focused practice, then a related variation within the chosen response mode. A beginning counter may receive three counting rounds. The review mockup intentionally demonstrates count → add → subtract so adults can compare mechanics; that is not an assessment-based production sequence.

**Duration:** aim initially for roughly 3–6 minutes including exploration and the reward, with no child-facing timer. This is a design target to measure, not a developmental recommendation. Adults may select 3 or 5 rounds. Leaving early saves progress and is treated neutrally.

Three is the default shown in diagrams and mockups; native session indicators reflect the selected length. While the pilot collection is incomplete, one reward is granted per completed configured session; after that, the completion celebration leads to existing garden play. A partially completed session keeps its rounds and unfinished work; returning resumes it. The pilot offers Help and Finish for now, not Skip. Finishing early grants no new session item but never removes prior items or access to the garden. A parent may restart a saved session, with a confirmation explaining that only unfinished-session work is cleared.

## 7. Activity specifications and concrete examples

### A. Pack the picnic — making a set

**Goal:** create the requested quantity from a larger available set. First variant: “Give Pip 3 berries.” Later review example: “Pack 5 berries,” with six available. For the proposed pilot, targets stay within 0–5 and available sets within 0–6; spoken counting must cover six when a child over-packs.

1. Pip looks toward the basket; the prompt plays once. All fruit are still while the child thinks.
2. Tap a berry to move it into the basket; tapping a packed berry returns it. Dragging is an optional equivalent in the native trial, never the only input.
3. Optional spoken counting names the current basket quantity after each accepted placement, return or Undo, including zero. A newer action replaces the pending count; never queue stale number words behind rapid taps. Prompt replay and help have their own explicit voice priority described below.
4. The child taps Done. Exactly the requested quantity succeeds. A first miss gets a neutral retry; after another miss, offer a specific add/return cue or counting model. Keep the current work editable and record the support actually delivered.
5. On success, the basket settles and Pip gives a brief appreciative reaction. Continue is child-controlled.

**Audio-off / pre-numeral path:** show a persistent, framed, noninteractive quantity-reference card for the given target (three matching fruit for three; an explicit empty frame for zero) plus a one-action picture cue. Keep reference objects visually separate from the movable task objects. This is a quantity-copy representation, recorded separately from acting on a spoken number. The same card and action cue must be available with spoken counting off. Joining and taking-away action-only variants use picture cues for the requested action; a remaining-total quiz must never show a reference card containing its answer.

**Avoid:** starting with exactly five objects and treating “tap all” as evidence of choosing five. Matching a numeral is a separate variant, not a mandatory extra question on every round.

**Acceptance:** repeated taps cannot duplicate objects; every move is reversible; over- and under-counts stay recoverable; zero works as a valid answer; object identity survives rotation/resume; completion cannot fire twice.

### B. Friends bring snacks — addition

**Goal:** join two groups and understand the total. “Two berries. One more joins. How many now?”

1. Show two on one mat and one on another, with clear space between groups.
2. The child joins the groups by tapping a large Join action or moving the incoming object.
3. All three remain countable; the child may touch them to count.
4. In the numeral-matching variant, offer 2, 3, and 4. Vary option placement in native content, avoiding a fixed correct slot.
5. After the correct total, reveal **2 + 1 = 3** aligned to the scene. At the earliest level, narration says the relationship without requiring equation reading.

**Before numeral recognition:** the task is explicitly “Put all the berries together.” The child joins the objects and taps Done; success checks that all objects are on the shared mat. Count the combined set together and show the relationship. Record this as an action-only joining experience; record extra help separately when it was actually delivered before completion. Post-success explanation does not rewrite that evidence. Total recognition is assessed only in a numeral or separately authored quantity-choice variant.

**Hint ladder:** revoice the question → highlight each group → model counting all with the child. The child may finish with help or choose Finish for now. Do not promise an easier next example in the fixed pilot sequence; adaptive selection is a later proposal. Do not ask a second unrelated question while feedback is playing.

### C. Share the snacks — subtraction

**Goal:** connect taking away to the remaining quantity. Five berries on a mat; “Give 2 berries to our friend.”

1. The child moves two berries to a separate friend's plate; the starting set is visible before any movement.
2. Transferred fruit remain visible but muted and spatially separate, so the child can revisit the story.
3. Ask “How many are left here?” Indicate the source mat; let the child count the three remaining berries.
4. Reveal **5 − 2 = 3** after confirmation. Replay reconstructs the visual explanation without wiping earned progress.

There are two checkpoints in the numeral variant. First, Done checks that exactly two objects were transferred; too few or too many keeps the scene editable and points to the friend's plate. After that succeeds, the transferred set is fixed and the child chooses the remaining total from 2, 3, or 4. A mistaken remaining-total answer preserves the scene and offers counting help. In the earliest variant, completing the transfer ends the task and the app models counting what remains; record it as a taking-away experience, not independent subtraction fluency.

Prompt replay only repeats the current instruction. A separate post-success explanation replay is presentation-only: it shows a copy of the before/after sequence, cannot apply semantic moves or award completion, and returns to the exact saved state if interrupted. Never erase attempts or assistance flags on replay.

**Acceptance:** returning a berry updates the scene and count; repeated input cannot remove too many during a transition; no negative quantities in this band; missing animation/audio never blocks the mathematical state.

### D. Equal picnic plates — comparison, broader release

Two plates hold 3 and 4 objects. “Which has more?” Later: two differently spaced sets of 4 and “Are they the same?” Children can pair objects across sets before answering. Treat “equal” as its own objective, not an occasional distractor.

### E. Make five — composition, broader release

Five visible spaces on a picnic tray; two are filled. “How many more will make five?” The child fills the three empty spaces. Later hide the guide spaces after a demonstration and try a new arrangement. This provides a bridge from counting all to reasoning about parts.

## 8. Feedback, help, and evidence of learning

**Do not infer a misconception from one mis-tap.** Keep touch errors distinct from submitted mathematical answers. Provide immediate physical feedback for a press, but evaluate only a deliberate confirmation or numeral choice.

After the first wrong submitted answer, give a brief neutral response and preserve the work. After another, offer a visual support or model. Help is always available; a child may finish with support or leave. No endless loop requiring an answer they do not understand.

Store evidence for a **skill × representation × quantity band**, including content ID, actual instruction delivery/visible reference mode, response mode, whether the first submitted answer was correct, additional help used, and completion. Record at least spoken-target quantity making, visual-reference quantity copying, action-only joining/taking-away, and numeral total recognition as distinct experiences. A spoken prompt plus visible quantity reference belongs to the visual-reference category, not the unsupported spoken-target category. Built-in visible objects/spoken counting are the normal scaffold; describe success as “without extra help in this activity,” not proof of mental arithmetic.

**Evidence event contract (proposed):** keep separate records for making a set, checking the transferred amount, and answering a joined/remaining total. Each applicable checkpoint records its first submitted answer result, submitted-miss count, highest in-app support level (`none`, `cue`, `model`), whether completion was modeled, and its completion state. A correct retry does not rewrite the first submission. Action-only joining is a completed joining experience; it has no independent numerical-total result. Taking-away amount and remainder results must not be collapsed into one first-answer flag.

Normal instruction/revoice, neutral acknowledgement, prompt replay, Undo and configured counting feedback are baseline supports, not extra help. A specific attention cue or structured hint raises support to `cue`; a modeled count/answer raises it to `model`. Presentation-only replay preserves the evidence. Adult coaching is recorded only if explicitly reported; silence in the log does not prove no adult helped. Parent copy says “without extra in-app help,” with the representation stated, rather than claiming independence or mastery. Each help/feedback script declares its role before it is recorded.

The first pilot uses adult-selected bands and curated sequences. The following optional progression rule is a **later evaluation proposal**, outside the initial pilot requirement:

- Keep the most recent 8 eligible attempts per skill/band, alongside lifetime practice counts.
- Exclude incomplete rounds, input accidents, and modeled examples from independent-success decisions.
- Suggest trying the next quantity variant after at least 6 first-answer successes without extra help across at least 2 sessions and at least 2 arrangements.
- On 2 consecutive submitted misses or help-heavy rounds, make the next item easier in the same skill; do not erase progress or display a demotion.
- Adjust only within the adult-approved band. A new band is a parent suggestion, not an invisible jump.
- These numbers are tunable product hypotheses, not validated educational cutoffs. No “mastered” label in the first release.

Use parent language such as “Made groups of five from a picture in 4 of 6 recent tries without extra help; practiced 2 with help.” Action-only joining/taking-away completions are described as experiences, not correct numerical answers. Count a first-answer attempt only for a task that actually requests and receives a mathematical answer; assistance and attempts remain unchanged by presentation-only replay. A diagram of objects and one plain sentence are enough. Avoid percentages without sample size and broad claims such as “ahead for age.”

## 9. Rewards that remain fun

A completed configured session—three rounds by default, optionally five—earns **one predictable, non-consumable garden object while the agreed pilot collection is incomplete**, including when the child used help. Show the actual next item before the reveal; no random chest or rarity. Once the pilot collection is complete, use a clear completion celebration and optional garden play; never promise an item that does not exist.

Examples:

| Garden addition | Short play payoff | Why it fits |
|---|---|---|
| Pinwheel | Place it, tap once to spin, then it settles | Visible cause-and-effect; child chooses whether to repeat |
| Watering can | Tap three thirsty flowers to water them; each blooms once | Familiar counting-like action without another scored test |
| Picnic instrument | Tap three wooden keys to play a little tune | A creative reward without scarcity or performance pressure |
| Kite | Choose a color and watch one short flight | Ownership and a clear ending |

The proposed family pilot uses a pinwheel plus five permanent decorations. The first completion grants the pinwheel, the next five grant the reviewed decorations, and later completions return to familiar garden play without promising a new unproduced item. This finite pilot reward policy remains a review decision. There is always something freely available in My garden, even before the first completed session. Earned toys remain playable; never require more exercises to refill energy. After the reveal, “Done for today” and “Play again” are equally clear. The mascot never pleads for more play.

Creation-based motivation is our design choice. Pok Pok documents calm, open-ended toys without winning or losing; that is a useful reference for the garden area, not evidence that our explicit learning activities should remove all feedback. [Pok Pok FAQ](https://playpokpok.com/faqs/).

## 10. Visual, motion, audio, and accessibility direction

**Art:** warm storybook garden with tactile paper-like forms, soft shadows, a cream rabbit, rounded trees, real recognizable fruit, and lightly imperfect silhouettes. Reserve visual detail for the world; keep the working area uncluttered. Pip should be expressive without exaggerated distress or constant attention-seeking movement.

**Palette:** warm cream `#FFF9EC`; dark forest text `#234D39`; coral action accent `#D95D47`; butter yellow and sky blue as supporting scene colors. Text/control combinations must be checked independently—an attractive palette is not a contrast guarantee. Child numerals need clearly distinct 1/7 and 6/9. Native typography can use SF Rounded with tested sizes; browser review uses local rounded fallbacks.

**iPad:** landscape-led but usable in portrait. Validate on an iPad mini-sized layout and an 11-inch layout, including safe areas. Primary child targets aim for at least 64 pt; object hit regions should not overlap. No precision dragging, hover-only interaction, Pencil dependency, or tiny gesture-only exits. Separate working objects from toolbar hit areas.

| Moment | Proposed motion | Reduced Motion alternative |
|---|---|---|
| Press | Small depression, about 100 ms | Color/outline change |
| Move item | 200–300 ms clear movement into destination | Immediate placement with brief highlight |
| Join/take away | 350–500 ms spatial explanation | Discrete before/after with the same grouping cues |
| Completion | 1–2 seconds, then settle; continuation remains clear | Static pleased pose and text/audio |
| Reward | One short spin or bloom, repeat only on request | Static finished state |

No automatic bouncing fruit during solving. Narration, spoken counting, and effects have separate controls. Background music is deferred for the first pilot; if introduced later, it will have its own control. One voice lane at a time; replay cancels stale audio. No microphone is needed. Silence and interruption must not freeze the activity.

**Audio arbitration contract (proposed):** a new instruction, Help or explicit Replay replaces the previous voice; any semantic object move cancels stale instruction/help speech and, when spoken counting is enabled, announces only the latest relevant group count. Count uses basket quantity; transfer uses the quantity on the friend’s plate; deliberate touch-to-count in a numeral question uses the set the child has marked, without counting a repeated touch twice. Joining never automatically announces an assessed total before the child has chosen to count or answer. Success, pause, route changes and interruption cancel pending voices; resume does not play an old queue. Optional effects are quiet and never mask a spoken number. Prompt replay is available independently of spoken counting. When narration is muted, the visible reference/action cue remains usable; actual presentation is recorded in the evidence.

**BrightPebble carry-over:** its preference for natural prerecorded narration should be auditioned here, with any chosen provider used during asset production only. Bundle the approved files in the app. Do not change that project's provider or assume its voice is already approved for MathBuddy.

Provide labels for objects and destinations, a tap-based equivalent to dragging, meaningful VoiceOver order, non-color feedback, larger text layouts, optional sound, and system Reduce Motion support. Apple's guidance and SwiftUI expose accessibility expectations and the reduced-motion setting; native checks remain required. [Apple accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [SwiftUI Reduce Motion](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion).

**Accessible math is a content requirement:** the given target (for example, “make five”) must remain available to the child. Accessibility labels must not reveal an assessed result (for example, the combined or remaining total) before the response. Expose individual discoverable objects with position and state, and destinations such as “shared mat” or “friend's plate.” Keep focus stable after a move and announce only its result. For nonvisual counting, author a sequential object or sound-based variant; do not claim it measures the same skill simply because the screen has labels. Test that accessible names and option annotations do not accidentally disclose the correct assessed answer. Help may deliberately model it, but that use of support must be recorded. A visible/audio target reference used in quantity making is not an answer leak; it changes the representation being practiced.

## 11. Grown-ups

First-pilot setup offers small-set counting or early operations within five, with a sample scene, and asks whether numeral choices are comfortable. “Not sure” selects picture-supported/action-only variants. A preference for numeral choices enables those authored variants; it does not diagnose the child. “Not sure” starts easy. Counting-to-ten setup belongs to the broader release after that content exists. No diagnostic claim or mandatory exact age.

The grown-up area contains:

- A short evidence-based summary of skills practiced and assistance used, clearly labeled when there is not enough evidence yet.
- Starting band and session length; separate audio controls and a calmer-animation option.
- Local progress reset with explicit confirmation. Garden-image export is deferred; if added later, it belongs behind the adult gate.
- One physical-play suggestion: “At snack time, make five pieces in two different groups.”

Use an adult gate for settings and external actions; do not rely on the same arithmetic the child is learning. Native planning must choose and test an adult-level gate with an accessible alternative. A hold-only gesture is not proof of adulthood. The review mockup explicitly labels its gate as a demonstration.

The app's intended audience of 4–8 is distinct from App Store age rating and Kids category age bands. Apple lists Kids bands of 5 and under, 6–8, and 9–11 and requires gates for relevant adult actions. Decide store metadata during release planning based on the shipped content. [Apple Kids guidance](https://developer.apple.com/kids/).

## 12. Native architecture proposal

Use **SwiftUI** for screens, accessible controls, layout, and restrained animation; **AVFoundation** for bundled narration/effects; and one on-device persistence layer. The detailed pilot plan proposes a small versioned Codable file; reassess storage only if later requirements justify it. Confirm the family's iPadOS support target before implementation. No network or runtime model is required for lesson selection.

| Boundary | Responsibility |
|---|---|
| Content definitions | Authored skill, valid quantities, layout seed, correct outcome, support steps, asset/audio keys |
| Round state | Stable object IDs and locations, current phase, undo, answer checking, assistance flags |
| Session coordinator | Choose the configured number of appropriate rounds (3 by default), pause/resume, completion state |
| Audio coordinator | One foreground prompt, optional count feedback, interruption/cancellation, replay |
| Local progress store | Versioned skill evidence, session checkpoint, owned items, settings |
| Scene/reward presentation | Draw the world from state and grant at most one eligible new item per completion ID; handle a complete pilot collection honestly |

Suggested small value types: `ActivityDefinition`, `RoundState`, `SkillEvidence`, `SessionCheckpoint`, `GardenInventory`, `ParentSettings`. Keep rendering separate from scoring so resizing or animation does not change an answer. Avoid a generic game framework until a second real activity proves the need.

Round flow: `prompting → interacting → checking → supportedRetry | success → continue`. Prompt audio completion must not be a prerequisite for entering interaction. Pause cancels audio and saves stable state; resume restores it without awarding a reward twice. Use a durable completion ID for reward grants. App termination between completion and reveal must recover the same reward.

Content requirements: validate nonnegative quantities, correct totals, unique answer options, quantity-band limits, asset availability, transcript/audio correspondence, and valid layouts. A missing decoration should degrade gracefully; a missing required learning object should block that content variant and select a known-good one.

Automatic variant substitution is allowed only before a round starts. If an active or resumed round has a missing required asset, preserve its checkpoint and offer Retry or Home. A deliberate restart may select another valid variant; do not count a technical failure as a child error or silently replace partial work.

Share patterns with BrightPebble first: audio cancellation, state separation, accessible controls, and visual QA. Do not extract or couple a shared package while both apps are still changing. Its spelling mechanics are not a reusable math engine.

## 13. Art and content budget for the family pilot

- One guide, Pip: idle, attentive, thinking/supporting, pleased, farewell poses.
- Two countable object families for the pilot, each with clear silhouettes and no decorative extras that could be counted by mistake; a third is deferred.
- One meadow/picnic environment; basket, two grouping mats, friend's plate, garden placement area.
- Pinwheel plus approximately five scene decorations; all permanent and visible.
- An initial authoring set of about 24 reviewed variants across the three families; parameter ranges should be curated, not blindly randomized.
- Short prompts and feedback with transcripts, duration, provider/license notes, and local filenames. Exact recording count follows the content manifest; do not produce a huge voice pack before auditioning.

The [asset plan](asset-plan.md) expands this budget into stable IDs, all required visual states, layers, screen compositions, motion briefs, exact script families and separate technical/human review records. Approve a small direction sample first, then the complete agreed pilot pack before its implementation phases. Existing experimental artwork and recordings are only candidates.

## 14. Review and acceptance plan

### Child observation — before content expansion

Run several brief sessions when the child is willing, with an adult observing rather than coaching every step. Treat this as product usability evidence, not a learning study.

1. Show Home. Can he identify how to start?
2. Give a simple counting task. Does he understand tap-to-move without adult rescue? Compare drag in a separate native prototype.
3. Try a deliberate extra object. Can he remove it and recover calmly?
4. Use a new arrangement or object family. Can he transfer the quantity idea?
5. Compare a garden addition with a short toy payoff. What does he revisit voluntarily?
6. Offer a natural stopping point. Can he finish without a confusing exit or emotional pressure?
7. Later, try the same quantity with physical objects. Record what the child actually did, including help.

Record observations as short notes: prompt understood, adult help, mistaken taps, mathematical response, frustration, reward interest, and stopping. Do not infer learning gains from replay count alone.

### Native engineering gates

Verify mathematical state, duplicate completion handling, the complete tap-only flow, Undo, wrong-answer recovery, background/foreground and force-quit resume, narration cancellation, audio-off behavior, Reduce Motion, VoiceOver, dynamic text, portrait/landscape, and airplane mode from first launch. If dragging is later included, also verify tap/drag equivalence. Use focused checks for these risks rather than a large test suite around decorative UI. Document observed behavior on simulator and real hardware separately.

### Historical experiments and their limits

The browser and native experiments can supply visual discussion material. They were produced before agreement on the intended sequence and do not establish an approved product direction. Technical evidence from them remains in the [experiment register](experiments/README.md); it must not be treated as learning validation, asset approval or completion of the new roadmap.

Current acceptance is a clear, consistent planning packet with explicit proposals and dependencies. Asset review follows when that work is selected. Native acceptance applies only to separately planned implementation phases.

## 15. Decisions to make together

1. Is the calm picnic garden the right emotional world, or would dinosaurs or space be more motivating?
2. Is his current entry point small-set counting, counting to ten, or early operations?
3. Does tap-to-move feel satisfying enough, or should direct dragging be central with a tap alternative?
4. Is a garden object plus short toy play more appealing than standalone reward games?
5. Should MathBuddy share Pebble’s visual identity, or only its clarity and production/review process?
6. Confirm the family iPad model/OS before executing the first native phase; the implementation plan may state a provisional support assumption.
7. Review the art/voice direction sample, then approve the agreed pilot asset pack before a detailed build plan is executed. The plan can be written and reviewed now with these dependencies explicit.

These decisions refine this concrete proposal. The next work to select is the creative-direction sample, after reviewing the spec and asset inventory; no implementation or new asset generation starts automatically.
