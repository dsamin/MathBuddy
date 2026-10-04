# MathBuddy native pilot implementation plan

**Planning draft · October 3, 2026 · No implementation or asset generation authorized.**

> For a future implementation agent: read the approved specification, asset handoff, `tasks/lessons.md` and the selected phase before acting. This is a reviewable plan, not an instruction to execute all phases. The user selects an individual phase after the preceding review checkpoint.

**Goal:** deliver a small, beautiful native iPad math experience through reviewed assets and individually demonstrated implementation phases, beginning with one count-three activity.

**Architecture:** SwiftUI presents authored content and semantic round state. Mathematical rules, saved progress, audio playback and presentation have separate responsibilities; animation and audio callbacks never determine an answer or grant a reward. Start with one concrete app store and small value types, without a generic game framework or shared Pebble package.

**Proposed stack:** Swift 6, SwiftUI, Observation, Foundation Codable, AVFoundation and LocalAuthentication if the adult-gate proposal is selected. No third-party runtime package is needed. The existing iPadOS 18/XcodeGen configuration is an experimental candidate, not an approved deployment decision.

**Inputs:** [feature specification](../feature-spec.md), [asset plan](../asset-plan.md), [roadmap](../roadmap.md), [asset production plan](../planning/asset-production-plan.md), [asset register](../planning/asset-register.csv), [content catalog](../planning/content-catalog.json), [voice script catalog](../planning/voice-script-catalog.json), [Pebble workflow evidence](../research/brightpebble-lessons.md), and [experiment register](../experiments/README.md).

## 1. Working agreement and decisions before execution

- Native SwiftUI iPad application; no WebView, HTML interface, JavaScript runtime, Capacitor or React Native wrapper. An adult asset-review gallery may be a separate web document and must never enter the app target.
- Asset-first order: agree product → choose direction → produce and review the essential pilot pack → select an individual native phase → implement and review that phase. Writing this detailed plan now does not advance those gates.
- Existing code, art, audio and recorded build results are unapproved experiments. Reuse requires an explicit keep/revise/discard decision against the reviewed requirements; no existing phase is credited as complete.
- Mirror Pebble's bounded slices and focused verification: build working behavior, then add meaningful regression checks. No mandatory TDD, coverage quota, per-view snapshot suite or UI automation framework. About four to six focused automated checks across the pilot are a useful starting point; add another only for a distinct material risk.
- A coordinator owns project configuration, shared interfaces, integration and phase records. One native worker owns the selected interaction. Add a separate audio/persistence worker only after interfaces and file ownership are stable. No agents modify Pebble.
- Keep technical validation, human asset/content/listening review, assistive-use review, physical-device use and child observation distinct. A build is not approval of educational claims or the next phase.
- No provider calls, credential setup, image/audio generation, code edits, builds, commits or publishing occur during this planning task. Later asset production and implementation each need their own selected scope.

| Decision | Recommendation to review | Required before |
|---|---|---|
| First topic | `CNT-01`: make three berries from five available | Creative composition approval |
| Creative direction | One picnic world; Pip, palette and voice remain candidates | Production batch 2A |
| Pilot asset boundary | Approve all essential assets for the agreed pilot; do not produce future curriculum packs | Native Phase 3 |
| OS/device floor | Consider iPadOS 18 if the family's actual iPad supports it; verify model, available OS and development toolchain | Native Phase 3 project task |
| Layout | Landscape-led, portrait-capable; mini-sized and 11-inch references; assess resizable windows rather than assume full-screen | Native Phase 3 layout task |
| Adult gate | Recommend device-owner authentication with an accessible system passcode alternative; decide behavior on a device without authentication configured before implementing the gate | Native Phase 3 minimal settings and Phase 4D full controls |
| Saved experimental work | New reviewed-pilot storage namespace; preserve experimental saves and evidence without importing them | Native Phase 3 persistence task |

The adult-gate choice cannot quietly become a hold gesture, a math question or an unprotected Release bypass. If the selected system policy is unavailable, remain on the child-safe route and explain the setup requirement to the adult. A different accessible fallback needs its own reviewed design.

## 2. Phase dependencies and review outputs

| Phase | Inputs | Reviewable output | Stop condition |
|---|---|---|---|
| **0 — Product review** | Source research, current specs, independent reviews | Resolved scope/decision record, reconciled feature/asset/content contracts | User reviews first topic, world and reward proposal |
| **1 — Creative direction** | Phase 0 choices | Small character/style comparisons, one learning composition, garden composition, motion sample and five-line voice audition | Choose a direction before bulk generation |
| **2 — Pilot assets** | Chosen direction and exact scripts | Batches 2A character/world, 2B math pieces, 2C rewards, 2D motion/audio, 2E verified handoff | Every essential pilot dependency has an approved selected take and content review |
| **3 — Counting first** | Reviewed pack, confirmed iPad target, selected phase | Home → `CNT-01` → completion → Home/leave/resume, with native motion/audio and accessible silent use | Show actual native evidence and unresolved hardware/human checks; review before 4A |
| **4A — Joining** | Phase 3 acceptance and reviewed joining variants | Reversible joining, action-only and numeral-total variants, truthful evidence | Review joining behavior before 4B |
| **4B — Taking away** | Phase 4A acceptance and reviewed taking-away variants | Reversible transfer, distinct remaining-total stage and presentation-only explanation replay | Review both representations and recovery before 4C |
| **4C — Session and garden** | Accepted activity families and reward pack | Curated three/five-round sessions, permanent rewards, free garden play, natural ending | Review durable completion/reward behavior before 4D |
| **4D — Grown-ups and continuity** | Earlier phase records | Full settings, honest summaries, adult gate, reset and complete resume matrix | Review complete pilot before family validation |
| **5 — Device and family validation** | Working complete pilot | Physical-iPad, assistive-use, listening and willing child observations; corrections | Record whether the pilot is ready to expand |
| **6 — Expansion** | Pilot observations and a selected new skill | One new topic specification, assets, implementation plan and later demonstration | Repeat the cycle; comparison and make-five are candidates |

Phase 3 loads only `CNT-01`; it does not expose a topic picker or pretend to implement the 24-variant pilot. The reviewed full catalog becomes selectable only as its activity families are implemented in Phase 4. Keep unavailable content out of child navigation.

## 3. Asset-to-native handoff contract

The planning catalogs define requirements; they are not production delivery manifests. Future production lives in `assets/production/picnic-v1/`:

| Proposed path | Responsibility |
|---|---|
| `catalog.json` | Full provenance, exact script/prompt, take history, technical checks and separate human/content/listening/rights decisions |
| `delivery/manifest.reviewed.json` | Only approved selected files, stable IDs, versions, relative paths and SHA-256 checksums |
| `delivery/content/content-catalog.json` | Reviewed `CNT-01…08`, `JOIN-01…08`, `TAKE-01…08` definitions and dependency references |
| `delivery/images/<ID>[-layer].png` | Selected image exports; independently moving pieces have separate layers |
| `delivery/audio/en-US/<ID>.m4a` | Selected offline clips with exact transcript references |
| `motion/M01…M07/brief.json` and `storyboard.pdf` | Trigger, layers, end state, cancellation and Reduced Motion behavior |
| `metadata/review-decisions.json` | Who selected which version, what remains rejected/deferred, and decision dates |

Native import copies only selected delivery files. Masters, prompts, provider requests, credentials, generation scripts, rejected takes and browser galleries stay outside the app bundle. Artwork IDs can map to Xcode image-set names; keep that mapping explicit in the bundle manifest. Text, numerals, hit regions and mathematical state remain native, separate from illustration pixels.

**Required checks at import:** unique IDs; relative paths confined to the bundle; matching checksum and selected version; decodable media; correct quantities/options; available objects at most six and target/operation totals within five; matching object-family wording; exact transcript/audio mapping; reviewed alternate layouts; and every dependency approved for its use. Zero and empty sets need explicit content review.

**Failure policy:** before a round starts, reject an invalid definition and choose only a reviewed valid alternative within the selected band. For Phase 3, with only one definition, show an unavailable state with Retry/Home. For an active or resumed round, preserve the exact checkpoint and offer Retry/Home; never silently replace it or record a child mistake. A missing optional decoration may be omitted while preserving ownership. A missing required voice/object/target representation is a content failure. Intentionally switching narration off is a supported setting, not missing content.

## 4. Proposed file responsibilities and interfaces

These are future file operations, not edits made by this plan. Review the experimental file first; keep compatible work or replace the smallest responsible section. Do not let its current API force the product design.

| File(s) under project root | Responsibility / future treatment |
|---|---|
| `project.yml`, `MathBuddy.xcodeproj/`, `MathBuddy/Info.plist`, `MathBuddy/MathBuddyApp.swift` | Coordinator: selected target, bundled resources, app lifecycle and test target |
| `MathBuddy/Model/MathBuddyModels.swift` | Extend/review value types: stable round/session IDs, object locations, settings and schema envelope; avoid storing presentation coordinates |
| `MathBuddy/Model/ActivityDefinition.swift` **new** | Codable reviewed content, skill/representation/band, assets, support steps and answer choices |
| `MathBuddy/Model/RoundRules.swift` **new** | Pure semantic transitions for move, undo, submit, join and help; no SwiftUI/audio/storage |
| `MathBuddy/Model/SkillEvidence.swift` **new** | Factual evidence with representation and support provenance; no mastery score |
| `MathBuddy/Model/MathBuddyStore.swift` | Main-actor coordinator; validate, apply, persist, publish; reject stale round events |
| `MathBuddy/Content/ContentCatalog.swift`, `AssetManifest.swift` **new** | Reviewed-only bundle loading and validation; one content/asset mapping |
| `MathBuddy/Persistence/ProgressStore.swift` **new** | Versioned local reads, atomic writes, preserved corrupt/future saves and explicit recovery |
| `MathBuddy/Audio/MathBuddyAudio.swift` | One voice lane, separate effects, cancellation, offline resources and silent return |
| `MathBuddy/Views/MathBuddyRootView.swift`, `ActivityView.swift` | Routes, Home, persistent control locations and current native learning board |
| `MathBuddy/Views/RecoveryView.swift`, `QuantityTargetView.swift` **new** | Honest unavailable/save-error recovery and visible quantity target for silent/pre-numeral use |
| `MathBuddy/Views/GardenView.swift`, `GrownUpsSheet.swift` | Phase 4 garden, settings, summaries and protected destructive actions |
| `MathBuddy/Design/StorybookTheme.swift`, `NativeIllustrations.swift` | Approved visual tokens and any reviewed native vector pieces; replace experimental art only deliberately |
| `MathBuddy/Model/SessionPlanner.swift`, `RewardLedger.swift` **new in 4C** | Curated eligible sequences and durable at-most-once reward decisions |
| `MathBuddy/Parent/AdultGate.swift` **new** | Selected native authentication policy, cancellation and unavailable behavior |
| `MathBuddy/Resources/Content/{asset-manifest,content-catalog}.json` **new** | Reviewed native delivery manifest and content snapshot |
| `MathBuddy/Resources/Audio/`, `MathBuddy/Assets.xcassets/` | Imported selected delivery versions only; remove unselected target membership |
| `MathBuddyTests/{CountingRules,ContentCatalog,ProgressStore,AudioCoordinator,ActivityEvidence,RewardLedger}Tests.swift` **new as needed** | Small high-value regression set using Swift Testing; no per-view snapshots |
| `docs/verification/phase-3-counting.md`, `phase-4a-joining.md`, `phase-4b-taking-away.md`, `phase-4c-session-garden.md`, `phase-4d-grownups.md`, `phase-5-family.md` **new at execution** | Actual evidence, asset versions, limitations and checkpoint result |

### Shared contract to agree before splitting native work

The following proposed interface names are the coordination contract. Implementers can simplify them during the selected phase review, but consumers and tests must change together.

```swift
// Model layer: Codable/Equatable value types, independent of SwiftUI.
typealias AssetID = String
typealias ContentID = String
typealias ObjectID = String                 // authored occurrence ID, not array position
enum ObjectLocation: String, Codable {
    case tray, basket
    case leftMat = "left-group", rightMat = "right-group"
    case sharedMat = "shared-mat", sourceMat = "source-mat"
    case friendPlate = "friend-plate"
}
enum RoundAction { case move(ObjectID, ObjectLocation), undo, submit, join, choose(Int), help, markForCounting(ObjectID) }
struct RoundTransition { let state: RoundState; let events: [RoundEvent] }
enum RoundEvent { case destinationCount(Int), prompt(AssetID), supported, completed }
enum RoundRules {
    static func apply(_ action: RoundAction, to state: RoundState,
                      definition: ActivityDefinition) -> RoundTransition
}

// Main-actor coordinator owns a single source of published state.
// All event handlers include the rendered round ID to reject stale taps/callbacks.
// send, startOrResume, goHome and retryPersistence are methods on MathBuddyStore.
// send(_ action: RoundAction, roundID: UUID)
// startOrResume()
// goHome()
// retryPersistence()

enum ProgressLoadResult { case empty, loaded(ProgressSnapshot), recovery(RecoveryIssue) }
protocol ProgressStoring {
    func load() throws -> ProgressLoadResult
    func save(_ snapshot: ProgressSnapshot) throws
    func resetAfterVerifiedBackup() throws
}

@MainActor protocol AudioPlaying {
    func playPrompt(_ id: AssetID, roundID: UUID)
    func playCount(_ value: Int, roundID: UUID)
    func playEffect(_ id: AssetID)
    func stopAll()
}
```

`ActivityDefinition` carries ID/version, skill, quantity band, given target, assessed outcome, authored object IDs/initial locations, response representation, object family, layout ID, answer options and prompt/help/asset IDs. A definition must distinguish the **given instruction** (“make three”) from the **unknown assessed answer** (“how many altogether”).

The raw region values above match the authored layout catalog. Each occurrence persists its region and stable slot ID, with its original region/slot retained for return and Undo. Native layout translates those IDs into the orientation's normalized anchors; absolute screen coordinates never enter saved mathematical state. Review any JSON-to-Swift field mapping explicitly at import rather than silently renaming the content contract.

`RoundState` carries definition ID/version, UUID, phase, object locations, reversible move history, persisted answer order, IDs deliberately marked for counting, delivered representation and per-checkpoint evidence. `RoundEvent` values request presentation only. `SkillEvidence` records content/version, skill, response mode, delivered representation, band and checkpoint records. Each applicable `CheckpointEvidence` identifies `makeSet`, `transferAmount`, `joinedTotal` or `remainingTotal`; it stores `firstSubmittedCorrect`, `submittedMissCount`, `highestSupport` (`none`, `cue`, `model`), `modeledCompletion`, completion state and durable completion ID. Taking-away transfer and remaining-total evidence are separate, and a later correct retry cannot overwrite an earlier miss.

Normal instruction/revoice, neutral acknowledgement, prompt replay, Undo and configured counting feedback are baseline scaffolds. An explicit focus cue raises support to `cue`; a modeled count/answer raises it to `model`. Preserve support through replay/Undo/relaunch. Record adult coaching only if explicitly reported; an absent report is unknown, not proof that no adult helped. Action-only joining records the joining experience and has no independent numerical-total result. Summaries say “without extra in-app help,” with the representation stated.

`ProgressSnapshot` is a Codable envelope containing `schemaVersion`, revision, settings, active session/checkpoint, evidence, reward ledger and pending reward reveal. `RecoveryIssue` distinguishes unreadable content, unsupported future schema and storage failure. Use a proposed new Application Support namespace `MathBuddy/ReviewedPilot/progress.json`; do not interpret an experimental save as reviewed-pilot progress. Unknown future schemas and corrupt files remain preserved and read-only until explicit adult recovery.

## 5. Review focus and the checks that own it

| High-impact condition | Expected behavior | Owning check |
|---|---|---|
| Fast repeated taps, Undo, resize and stale callbacks | Exactly the authored objects remain; semantic correctness and evidence cannot depend on motion | Phase 3 `quantityConservedAndSubmissionDeliberate`; native rapid-input demonstration |
| Force quit or failed save at success/reward boundary | Resume exact durable state; never show an unsaved entitlement or grant twice | Phase 3 `resumeAndSaveFailurePreserveState`; Phase 4C `grantExactlyOnceAfterDurableCompletion` |
| Narration off, pre-numeral response or assistive access | Given target remains understandable; hidden answer stays hidden; evidence names the delivered representation | Phase 3 manual silent/VoiceOver scenarios; Phase 4 `representationsAndHelpStayDistinct` |
| Missing/unapproved asset or mismatched script | New invalid content cannot start; active work is preserved behind Retry/Home | Phase 3 `requiredCoverageRejectsUnapprovedOrMissingContent` |
| Replay/rapid moves/background audio race | One current voice, no stale queue, no surprise resume, no input lock | Phase 3 `stalePlaybackNeverResumes` and manual audio demonstration |

## 6. Phase 0–2 tasks before native implementation

These tasks produce review artifacts only. Detailed production prompts and exact rows live in the asset production plan so there is one authoritative asset inventory.

- [ ] **0.1 Reconcile the review.** Record which product-review findings changed F01–F13, the 24 proposed variants, target-card representation, support policy and reward inventory. Output: consistent specification/catalogs and a short decision record; unresolved choices remain proposals.
- [ ] **0.2 Select the pilot boundary.** Review count-three first, full pilot later, device availability and the six-item reward limit. Output: selected scope and explicit deferred list; do not infer the son's ability from age.
- [ ] **1.1 Produce only the selected direction sample when requested.** Use the defined character, learning, garden, motion and five-line audition briefs. Output: comparable labeled samples and scripts; no bulk pack.
- [ ] **1.2 Review the direction.** Record character identity, countable-object recognition, scene calmness, portrait/landscape composition, target-card clarity and voice delivery decisions. Approve full state/layer/motion briefs and exact scripts before final exports or bulk recordings; batch 2D renders those already reviewed contracts. Output: selected style/version with revisions noted.
- [ ] **2.1–2.4 Produce/review batches 2A–2D individually.** Preserve take history and separate technical versus human decisions. Output: approved essential visual, content, motion and audio entries; no native import yet.
- [ ] **2.5 Audit batch 2E.** Resolve every essential scene-state-content dependency, listening decision, rights note and checksum. Output: reviewed delivery manifest and handoff. A row labeled draft or human-review-pending cannot satisfy the native gate.

**Checkpoint:** show the completed asset pack and the Phase 3 scope together. Only a later instruction to implement Phase 3 starts the tasks below.

## 7. Phase 3 — one native counting activity

**Outcome:** Home → give Pip three berries from five available → reversible correction/help → brief completion → Home/leave/resume. Only `CNT-01` is selectable. Include the platform foundations needed to make that one activity truthful and dependable; no garden entitlement, topic menu or full parent dashboard yet.

### Task 3.1 — Adopt the approved bundle and smallest native target

**Files:** project/app files, `Content/{ContentCatalog,AssetManifest}.swift`, `Resources/Content/`, selected image/audio target membership, `MathBuddyTests/ContentCatalogTests.swift`.

**Input/output:** reviewed handoff → `ContentCatalog.definition(id: ContentID) throws -> ActivityDefinition` and `AssetManifest.resolve(id: AssetID) throws -> URL`; Phase 3 eligibility is exactly `CNT-01` even if the reviewed full catalog is bundled for later use.

- [ ] Record the keep/revise/discard decision for each experimental file used by this task and confirm the actual family device/OS floor.
- [ ] Pin reviewed delivery versions and map their stable IDs to native resource paths. Validate quantity, transcript and selected-file references before exposing Play.
- [ ] Configure the iPad SwiftUI target and a small Swift Testing target; verify the built product contains no browser study, generator scripts, credentials or unselected draft clips.
- [ ] Add `requiredCoverageRejectsUnapprovedOrMissingContent()`: load a small valid catalog fixture, then change one required object to missing, one review status to draft and one transcript reference to wrong. Each fails eligibility; a missing optional decoration does not invalidate the learning definition.
- [ ] Build the native target using the future commands below. Record actual command, Xcode version, destination and resource-validation outcome in `phase-3-counting.md`.

**Acceptance:** `CNT-01` has a complete approved dependency closure; invalid resources cannot silently fall back to experimental media. No app/provider network calls are present.

### Task 3.2 — Make quantity state independent of movement

**Files:** `Model/{MathBuddyModels,ActivityDefinition,RoundRules,SkillEvidence,MathBuddyStore}.swift`, `MathBuddyTests/CountingRulesTests.swift`.

**Input/output:** approved `CNT-01` definition → `RoundRules.apply(_:to:definition:)`; the store exposes the exact persisted semantic state to the view.

- [ ] Create the round with five distinct authored IDs, all initially in the tray, target three and empty move history. Store locations instead of screen coordinates.
- [ ] Implement tray/basket movement and Undo. Reject unknown IDs, illegal locations, moves after success and events carrying a stale round ID. A touch itself does not submit an answer.
- [ ] Implement deliberate Done: two and four packed objects remain editable with neutral feedback; three completes once. An empty basket is a representable state even though this first target is three.
- [ ] Implement authored help without erasing attempts; first wrong submission preserves work, second offers support, and modeled completion remains marked as supported. Apply the checkpoint contract above: revoice/neutral retry are baseline, focused cue is `cue`, modeled answer is `model`. No inactivity-triggered answer reveal.
- [ ] Add `quantityConservedAndSubmissionDeliberate()`. Exercise place/return/Undo, fast same-object moves, wrong Done followed by recovery, an invalid object ID and repeated success. Assert five unique objects throughout, no evidence for a mere tap, and one completion record.

**Acceptance:** every semantic result can be checked without SwiftUI, animation timers or audio. Repeated submissions never increase completed practice twice.

### Task 3.3 — Draw the reviewed iPad board and silent target

**Files:** `Views/{MathBuddyRootView,ActivityView,QuantityTargetView}.swift`, `Design/{StorybookTheme,NativeIllustrations}.swift`.

**Input/output:** semantic state and approved composition → native controls and visible object locations; no mathematical writes from an animation completion.

- [ ] Render Home and one board with native Play, Home, Listen, Help, Undo and Done/Continue controls. Keep feedback/completion space reserved so controls do not jump after a response.
- [ ] Use individually visible objects and reviewed basket layers; expose at least 64-point child controls and non-overlapping object hit regions. Keep every packed object countable.
- [ ] Render the given target using the approved `REF-03` quantity-reference card with three matching fruit plus one-action picture cue. Keep this noninteractive reference visibly framed and separate from the actionable tray; label it as the requested amount. Preserve the `REF-00…05` mapping for later pilot content, including an explicit empty frame for zero. Save the actual delivered representation in evidence; quantity copying is not silently reported as spoken-only quantity making.
- [ ] Implement M01 pickup/return, M04 help and M05 completion using reviewed durations and state snapshots. System or parent Reduce Motion immediately selects the reviewed static/highlight version. Never wait for motion before accepting the next legitimate input.
- [ ] Reflow portrait/landscape using container geometry, safe areas and larger text. If a window cannot fit safe targets, preserve the round and show a clear resize/Home recovery state rather than shrink targets or overlap objects.
- [ ] Demonstrate count, over-pack, return, Undo, supported retry and completion in landscape/portrait. Capture actual native states; separately note that screenshots alone do not prove reachable touch targets.

**Acceptance:** a child can complete the task with taps and narration off; a visual target is available, the work area remains clear and rotation never changes the quantity.

### Task 3.4 — Integrate offline voice and interruption behavior

**Files:** `Audio/MathBuddyAudio.swift`, lifecycle wiring in `MathBuddyApp.swift` and store, `MathBuddyTests/AudioCoordinatorTests.swift`.

**Input/output:** reviewed voice IDs and semantic events → `AudioPlaying` methods; no audio completion event mutates round correctness.

- [ ] Implement separate narration, spoken-counting and effects settings. Listen replays the current authored prompt according to narration settings; the count toggle does not change replay behavior.
- [ ] Use one foreground voice lane. New prompt/help replaces the old voice. A real piece move, return or Undo cancels stale narration and, if enabled, plays the latest current destination quantity, including zero. Never queue a backlog of number words.
- [ ] Invalidate playback using a monotonically changing token plus round ID; completion, route change, background, interruption and audio-off stop stale voice/effects. Foreground return stays silent until a deliberate action.
- [ ] Add `stalePlaybackNeverResumes()` with a small controllable playback adapter: start prompt A, replace with count three, switch route, then deliver A's late completion. Assert no further playback and no round mutation. Repeat with narration off/counting on and the reverse.
- [ ] Manually play the selected clips offline; exercise rapid Listen/moves, zero after returning all objects, Undo, background and foreground. Record observed playback/cancellation separately from the already required human listening decision.

**Acceptance:** only the current voice is heard, silence remains fully usable and audio failure never freezes mathematical state. Missing required content uses the defined recovery path; no speech synthesis substitutes for an absent file.

### Task 3.5 — Preserve the first activity honestly

**Files:** `Persistence/ProgressStore.swift`, store/app lifecycle, `Views/RecoveryView.swift`, `MathBuddyTests/ProgressStoreTests.swift`.

**Input/output:** proposed `ProgressSnapshot` → atomic local save and `ProgressLoadResult`; use the reviewed-pilot namespace, leaving experimental save files untouched.

- [ ] Save a new snapshot for each semantic transition using an atomic write. Validate it before publishing completion/evidence; a failed write retains the last durable state and presents Retry/Home without claiming success was saved.
- [ ] Restore round ID, content version, object locations, move history, help, attempts, delivered representation and completed state. Returning Home or finishing early preserves unfinished work and earns nothing new.
- [ ] Preserve corrupt/unsupported future-schema originals. Do not downgrade, overwrite, silently reset or select new content during recovery. Adult reset requires a verified recovery copy before replacing progress; if the copy fails, leave the original intact.
- [ ] Add `resumeAndSaveFailurePreserveState()` with an isolated temporary directory. Save two objects, restore, Undo, fail a success save, retry, then relaunch. Assert exact state and one completion. Include a future-schema fixture whose original bytes must remain unchanged after attempted actions.
- [ ] Demonstrate force-quit/relaunch mid-round and after completion; inject a required-content failure on a saved round and confirm Retry/Home preserves its identity and work.

**Acceptance:** progress is either durably saved or clearly unsaved. No technical error counts as a child answer, and re-entry never creates a second completion.

### Task 3.6 — Review the complete first slice

**Files:** minimal adult control/gate shell, `docs/verification/phase-3-counting.md`; change implementation files only for material findings.

- [ ] Wire the selected adult gate to the small settings needed now: narration, spoken counts, effects and reduced motion. Show that this first slice has a fixed small-set entry using `CNT-01`; do not offer unimplemented operation bands or hide setup behind a Debug-only route. Test cancellation/unavailable behavior; do not invent an unapproved fallback.
- [ ] Check VoiceOver order and labels on the actual board. Announce the given target three; do not label an unknown future operation total. Discover each object by identity/location without revealing an answer through a group label. Moving an object preserves useful focus.
- [ ] Check larger text, non-color feedback, silence, Reduce Motion, airplane mode, portrait/landscape and compact-window recovery. Add a sequential accessible counting variant only after its content/representation is approved; labels alone do not prove equivalent learning assessment.
- [ ] Run the changed focused checks and Debug/Release build once after integration. Review against the approved composition; fix material discrepancies and rerun only affected checks.
- [ ] Show the actual count-three interaction, source/version list, evidence and named gaps. Mark physical-iPad/assistive/child checks pending when they were not performed.

**Stop at Phase 3.** A completed native counting slice is the review result, not authorization to implement joining or load the rest of the pilot.

## 8. Phase 4A — joining groups

**Outcome:** the child can combine and separate sets, then complete an action-only or numeral-total task appropriate to the selected starting band.

**Files:** `ActivityDefinition`, `RoundRules`, `SkillEvidence`, store and `ActivityView`; `MathBuddyTests/ActivityEvidenceTests.swift`; `docs/verification/phase-4a-joining.md`.

**Interfaces:** extend `RoundRules.apply` for `.join`, `.undo`, `.submit` and `.choose(Int)`; use the definition's representation rather than a separate implicit UI mode. Add reviewed `JOIN-01…08` eligibility only after their required presentation is implemented.

- [ ] **4A.1 Validate joining definitions.** Check left + right equals authored total, quantities are nonnegative/in band, zero groups have reviewed empty states, and answer options are unique with exactly one correct value. Persist authored option order for the round so resize/replay does not reshuffle it.
- [ ] **4A.2 Implement reversible groups.** Join moves the same IDs to the shared mat; Undo restores each original group. M02 depicts the transition but never decides when it is mathematically joined.
- [ ] **4A.3 Separate response evidence.** Action-only Done confirms all pieces joined and then models the relationship; it records a joining experience. A numeral variant presents options only after joining, records the child's submitted total, and reveals the equation only after confirmation. Joining itself must not automatically announce the assessed total. Deliberate `markForCounting` actions mark distinct object IDs and may voice the marked count as a normal scaffold; repeat touches do not count an object twice. A voice or accessibility label must not supply the unknown total before the child chooses to count or respond.
- [ ] **4A.4 Verify and demonstrate.** Add/extend `representationsAndHelpStayDistinct()`: same 2+1 content in the two representations must produce different evidence tags; help remains recorded through Undo/relaunch; late events from the previous round do nothing. Manually demonstrate join/separate, wrong-total recovery, a reviewed zero-group example, silent mode and Reduce Motion. Record evidence and stop for review.

## 9. Phase 4B — taking away

**Outcome:** transfer an amount, then distinguish that successful transfer from an independent answer about what remains.

**Files:** same rule/content/evidence/view files, `ActivityEvidenceTests.swift`, `docs/verification/phase-4b-taking-away.md`.

**Interfaces:** `.move(_, .friendPlate)` and Undo act only in the transfer stage; `.submit` validates transfer; `.choose(Int)` acts only in the remaining-total stage. Add a presentation-only `ExplanationSnapshot` value containing the before/after arrangement; its replay has no route to `RoundRules.apply` or reward mutation.

- [ ] **4B.1 Validate reviewed `TAKE-01…08`.** Check requested transfer ≤ initial set, remainder equals subtraction, zero/all-transfer variants have reviewed empty states and narration, and each definition declares whether it ends after transfer or assesses a remaining total.
- [ ] **4B.2 Implement the two checkpoints.** Transfer/return stays reversible until the correct transferred amount is confirmed. Its optional move feedback announces the friend's-plate count, not the unknown source remainder. Wrong transfer retains editing; correct transfer fixes that set before a numeral remaining-total choice. Wrong remaining total preserves the scene and offers appropriate source-mat support. The transfer and remainder each keep their own first submission, misses, highest support and modeled/completed state.
- [ ] **4B.3 Explain without changing saved work.** Current Listen repeats only the current instruction. Post-success explanation animates a copy of the before/after scene; interruption returns to exact saved state, preserving attempts/help/completion. No new completion can arise from replay.
- [ ] **4B.4 Verify and demonstrate.** Extend `representationsAndHelpStayDistinct()` with incorrect transfer, correct transfer/incorrect remainder, supported action-only completion and repeated explanation replay. Extend the restore check across both subtraction checkpoints. Demonstrate zero remaining, return/Undo, silent target representation and fast input, then record evidence and stop.

## 10. Phase 4C — sessions and the garden

**Outcome:** an appropriate short session ends with an honest permanent reward or existing garden play, and the child can leave naturally.

**Files:** new `Model/{SessionPlanner,RewardLedger}.swift`; models/store; `Views/{MathBuddyRootView,GardenView}.swift`; `MathBuddyTests/RewardLedgerTests.swift`; `docs/verification/phase-4c-session-garden.md`.

**Proposed interfaces:**

```swift
enum StartingBand: String, Codable { case smallSets, earlyOperations }
enum ResponsePreference: String, Codable { case picturesAndActions, numeralsComfortable }
// ParentSettings stores startingBand and responsePreference independently.
// Defaults: startingBand = .smallSets, responsePreference = .picturesAndActions.
// The adult's "Not sure" response maps to .picturesAndActions.
enum SessionPlanner {
    static func eligibleDefinitions(settings: ParentSettings,
                                    implemented: [ActivityDefinition]) -> [ActivityDefinition]
    static func make(settings: ParentSettings,
                     eligible: [ActivityDefinition]) throws -> SessionCheckpoint
}
struct RewardGrant: Codable, Equatable { let sessionID: UUID; let assetID: AssetID }
enum GrantOutcome { case new(RewardGrant), existing(RewardGrant), collectionComplete }
// RewardLedger.complete(sessionID: UUID, orderedRewards: [AssetID]) -> GrantOutcome
// The ledger mutation and completed session are saved in ONE ProgressSnapshot.
```

- [ ] **4C.1 Add curated selection.** Load implemented approved variants from the reviewed 24-definition catalog. Apply both `startingBand` and `responsePreference` using the eligibility table below; preserve every row's authored `mode`. Use three rounds by default and optional five; do not infer a new band, numeral comfort or mastery. Persist selected definition IDs/versions, modes, order and settings so continuation never changes the task underneath the child. If there is no valid curated sequence, show content-unavailable Retry/Home rather than substitute an unselected representation. There is no runtime easier-next switch or `VO-HELP-EASIER` promise in this pilot: its selected session stays pinned, and the adult can choose a different starting preference for the next new session.
- [ ] **4C.2 Finish deliberately.** Manual Continue advances once for the current completed round; a stale action cannot skip the next. Help and Finish for now exist; Skip does not. Early Finish preserves partial progress, awards no new item and keeps garden access. Starting over is an adult-confirmed action.
- [ ] **4C.3 Grant only after durable completion.** First eligible session grants pinwheel, then mushroom, lantern, stepping stone, bunting and birdhouse in the reviewed order. Persist the completed session ID, grant and pending reveal together before showing the earned item. Duplicate completion returns the same grant; a failed write shows no unsaved entitlement. A relaunch between save and reveal displays that same pending item.
- [ ] **4C.4 Add free and owned play.** Flower play is available on first garden visit. Owned toys remain playable, placement survives return/relaunch and one deliberate action triggers one finite motion. Once all six items are owned, show completion and familiar garden play without a new-item promise. Done for today and Play again remain clear.
- [ ] **4C.5 Verify and demonstrate.** Extend `representationsAndHelpStayDistinct()` with all four eligibility combinations below: unsure excludes numeral-plus-reference/total/remainder rows, smallSets never selects operations, numeral comfort adds only the reviewed numeric rows, and each chosen ID retains its authored mode across a preference change/resume. Test an empty eligible set yields content-unavailable, not a mode rewrite. Add `grantExactlyOnceAfterDurableCompletion()`: repeat final Continue, fail/retry the save, relaunch before reveal, revisit after placement, complete the sixth and seventh sessions, and finish early. Assert one entitlement per unique eligible session, none after the collection, no lost ownership, and no reward penalty for help. Demonstrate both session lengths, picture/action-only versus numeral-enabled selection, first-visit flower and collection-complete copy. Stop for review.

| Starting band | Response preference | Eligible authored rows from the reviewed catalog |
|---|---|---|
| `smallSets` | `picturesAndActions` / Not sure | Counting family only, `mode = quantity-reference` |
| `smallSets` | `numeralsComfortable` | Counting family only, `mode = quantity-reference` or `numeral-plus-reference` |
| `earlyOperations` | `picturesAndActions` / Not sure | Reviewed mixed sequence from counting `quantity-reference`, joining `action-only`, and taking-away `action-only` |
| `earlyOperations` | `numeralsComfortable` | The preceding eligible rows plus counting `numeral-plus-reference`, joining `numeral-total`, and taking-away `numeral-remainder` |

These rules filter catalog rows; they do not fabricate a new row or convert an existing ID between action-only and numeric modes. The catalog remains authoritative for the actual `CNT-01…08`, `JOIN-01…08` and `TAKE-01…08` assignments and reviewed layouts. Numeric comfort makes a numeric row eligible, not mandatory for every round. No unreviewed override is included in the pilot. Phase 3 remains fixed to `CNT-01` regardless of future preference support.

## 11. Phase 4D — grown-ups and complete continuity

**Outcome:** adults can choose a gentle entry and understand what was practiced, while the child can reliably resume.

**Files:** `Parent/AdultGate.swift`, `Views/GrownUpsSheet.swift`, `ParentSettings`, `SkillEvidence`, persistence/store; existing focused tests; `docs/verification/phase-4d-grownups.md`.

- [ ] **4D.1 Complete settings.** Offer independent choices for starting band (small-set counting or early operations, with a sample) and response preference (“Pictures and actions / Not sure” or “Comfortable with numeral choices”). Default to small sets plus pictures/actions. Save these as `ParentSettings.startingBand` and `.responsePreference`; do not infer numeral comfort from age, session count or success. Apply the Phase 4C eligibility rules, including action-only joining/taking-away for unsure early-operations users. Add three/five rounds, independent narration/spoken-count/effects toggles and calmer motion. Content/session changes apply to the next new session; active session settings/content modes remain pinned. Audio/motion toggles may apply immediately without discarding work.
- [ ] **4D.2 Report facts.** Summaries group skill × delivered representation × quantity band, keeping transfer and total checkpoints distinct, with sample sizes, supported completion and first-submission results. Incomplete work is not a completion, action-only joining is not independent total recognition, and silence/available audio is not evidence the child heard it. Say “without extra in-app help”; only a reported adult intervention can be recorded as coaching, while an absent report remains unknown. Add the physical-play suggestion without promising learning gains.
- [ ] **4D.3 Finish the gate and recovery.** Verify the selected native adult-gate path, accessible passcode alternative, cancellation/unavailable state, relock after background and explicit reset/restart confirmations. Reset must preserve a verified recovery copy before starting empty; no hold-only shortcut or same-math gate. Release contains no debug bypass.
- [ ] **4D.4 Complete the continuity matrix.** Restore Home, counting partial/success, joining before/after join, subtraction before/after transfer, pending reveal and placed garden. Extend `resumeAndSaveFailurePreserveState()` only for newly distinct cases: persisted settings/evidence and failed backup during reset. Confirm originals remain untouched on unreadable/future saves and that active missing content cannot trigger substitution.
- [ ] **4D.5 Review the complete pilot.** Exercise one end-to-end offline session, background/relaunch, early finish, garden, adult settings and truthful summary; run relevant checks and builds. Show actual evidence and unresolved family/hardware work. Stop before Phase 5.

## 12. Future build/check commands and evidence

**These commands are reference instructions for the selected implementation phase. They have not been run for this planning review.** Resolve the then-current installed Xcode path and Simulator inventory first; the old directory name may not match its actual Xcode version. Do not change global Xcode selection or use Pebble's active Simulator.

```sh
# Set this to an observed Xcode developer directory at execution time.
export DEVELOPER_DIR="$MATHBUDDY_XCODE_DEVELOPER_DIR"
xcodebuild -version
xcodebuild -project MathBuddy.xcodeproj -scheme MathBuddy -showdestinations

# Only if the phase's project review retains the existing XcodeGen workflow.
xcodegen generate --spec project.yml

# MATHBUDDY_IPAD_ID is a dedicated available iPad Simulator ID from that inventory.
xcodebuild -project MathBuddy.xcodeproj -scheme MathBuddy -configuration Debug \
  -destination "platform=iOS Simulator,id=$MATHBUDDY_IPAD_ID" \
  -derivedDataPath output/native-reviewed/DerivedData CODE_SIGNING_ALLOWED=NO build
xcodebuild -project MathBuddy.xcodeproj -scheme MathBuddy -configuration Release \
  -destination "platform=iOS Simulator,id=$MATHBUDDY_IPAD_ID" \
  -derivedDataPath output/native-reviewed/DerivedData CODE_SIGNING_ALLOWED=NO build

# The selected task adds this proposed Swift Testing target before this command exists.
xcodebuild -project MathBuddy.xcodeproj -scheme MathBuddy \
  -destination "platform=iOS Simulator,id=$MATHBUDDY_IPAD_ID" \
  -derivedDataPath output/native-reviewed/DerivedData \
  -only-testing:MathBuddyTests/CountingRulesTests \
  CODE_SIGNING_ALLOWED=NO test
```

For a different changed responsibility, select its named suite: `ContentCatalogTests`, `ProgressStoreTests`, `AudioCoordinatorTests`, `ActivityEvidenceTests` or `RewardLedgerTests`. Do not repeatedly run unchanged checks. Record real exit status and test result bundle; screenshots captured from seeded state do not establish a successful interactive journey. Simulator tool failures are named gaps, not grounds to claim unperformed interactions passed.

Every phase record includes context, relevant source/asset versions, tasks completed, exact files, acceptance results, command output locations, actual native captures and limitations. Keep physical hardware, VoiceOver/Switch Control, listening/content approval and child observation rows separate. Do not include secrets in logs or documentation.

## 13. Phase 5 — real-device and family review

**Files:** `docs/verification/phase-5-family.md`; update only responsible assets/content/native files after findings are reviewed.

- [ ] Check the family's actual iPad: reach, accidental touches, speaker/headphone level, interruptions, airplane mode from first launch, portrait/landscape, safe areas, larger text and Reduce Motion. Verify the chosen minimum device/OS, not just a powerful Simulator.
- [ ] Test VoiceOver and Switch Control paths with someone able to assess their usability; ensure given instructions are available and hidden assessed answers are not disclosed. Record representation differences honestly.
- [ ] Observe brief willing child sessions: starting, understanding the target, making/removing an extra object, using help, transferring to a different reviewed arrangement/object family, enjoying the garden and stopping. Record adult assistance; do not convert replay or enthusiasm into a learning-efficacy claim.
- [ ] Triage observations into asset, wording, interaction, accessibility or mathematical-content findings. Change the smallest responsible part, review any new asset take and repeat affected checks.
- [ ] Show the revised pilot and an explicit readiness assessment with unresolved issues. Stop; expansion is a separate choice.

## 14. Phase 6 — expand one skill at a time

Comparison/more-less-equal and make-five are the first proposed additions. Each begins with a short skill specification, examples including equal/zero where relevant, accessible/silent representations, exact asset/audio delta and child-observation goal. Produce and review that topic's assets before selecting its implementation plan. Larger numbers, patterns, shapes, measurement, place value, sharing and time/money remain later candidates, not hidden requirements of this pilot.

**Next checkpoint for this planning packet:** review the independent findings, first-pilot scope and asset inventory; choose the Phase 1 creative-direction sample. This document stops here. It does not start asset generation, modify the shelved app or authorize any native phase.
