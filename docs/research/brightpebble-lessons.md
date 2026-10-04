# BrightPebble lessons for MathBuddy

## Current planning reset — October 3, 2026

The user identifies Pebble as the parallel learning app. Its local project is `/Users/devan/Projects/BrightPebble`. The following workflow was checked in its current documents during this reset; no files in that project were changed.

| Verified practice | Evidence | MathBuddy application |
|---|---|---|
| Design review separates visual approval from native/content acceptance | [Review checkpoint](/Users/devan/Projects/BrightPebble/docs/review-checkpoint.md:3) | Record product and art decisions separately from builds |
| Asset work has its own scope, stable IDs, scripts, inventory and ownership; app/project edits are excluded from that task | [Asset task](/Users/devan/Projects/BrightPebble/tasks/asset-production.md:3) | Plan and review asset batches before starting MathBuddy's native phases |
| Masters, selected exports, exact prompts/requests, content/rights status and prior takes are retained | [Asset handoff](/Users/devan/Projects/BrightPebble/assets/production/core-5-v1/ASSET-HANDOFF.md:15) | Keep a versioned manifest and replacement history; do not overwrite rejected takes |
| Human listening and educational review are distinct from file integrity | [Asset review and acceptance](/Users/devan/Projects/BrightPebble/assets/production/core-5-v1/ASSET-HANDOFF.md:47) | Audition MathBuddy's voice; approve clarity and delivery separately from audio format checks |
| Each implementation slice has ownership, behavior references, tasks, checks and an explicit checkpoint | [Phase plan](/Users/devan/Projects/BrightPebble/docs/phase-1-implementation-plan.md:30) | Write a concrete plan for one selected phase; stop after its reviewable result |
| Actual test evidence and outstanding human/device work are documented separately | [Validation record](/Users/devan/Projects/BrightPebble/docs/phase-1-validation.md:279) | Do not equate compilation or screenshot rendering with child, voice or accessibility acceptance |

Pebble has allowed draft assets and native work to progress in parallel; it did not finish all asset approval before coding. MathBuddy adopts the useful separation of responsibilities while following the user's **stricter asset-first sequence**. The earlier Slice 1 snapshot below is historical and should not be treated as Pebble's current implementation status. No assumption is made that Pebble's chosen voice or illustrations are already approved for MathBuddy.

## Earlier research snapshot

Research snapshot: October 3, 2026. Read-only inspection of `/Users/devan/Projects/BrightPebble`; no sibling-project files changed. BrightPebble is under active development, and its uncommitted source advanced during this inspection. Evidence below distinguishes recorded native verification, observed source, user preferences, and proposed behavior. No child study, learning-efficacy result, or physical-iPad validation was found in the reviewed evidence.

## What has evidence behind it

| Finding | Evidence and status | MathBuddy implication |
|---|---|---|
| The native approach is feasible in this workspace. | `BrightPebble/docs/phase-1-validation.md:11–17,50–65` records Swift 6 / SwiftUI / Observation, iPad-only, no third-party dependencies, successful Debug and Release builds and a visible Simulator app. This is recorded evidence, not a build rerun for MathBuddy. | Prefer a native SwiftUI iPad app, with concrete local state and bundled content. Reconfirm toolchain/device details at implementation time. |
| Stable layouts and stable object identities matter. | `docs/phase-1-validation.md:71–83` records successful tap placement, retained tray placeholders, stable order across Home/Continue, portrait/large text review, and one reward after repeated completion/navigation. It also records fixes for disabled-control dimming and completion layout shifts. | Manipulatives should stay where the child expects. Reserve completion/feedback space; do not move the whole board when a label or reward appears. |
| Visual review must show actual options together. | `tasks/lessons.md:3–5` records the user's correction to show actual labeled previews inline, rather than relying on prose or earlier images. | Deliver comparable iPad screen mocks together and a navigable gallery. Make concept versus native status visible. |
| Human-like narration is an explicit preference. | `tasks/lessons.md:7–13` and `AGENTS.md:27–31` require natural prerecorded Google-generated narration, made externally and bundled offline; no native synthesized substitute. | Reuse the production approach as a candidate. Math-specific scripts, delivery, counting cadence and pronunciations need their own listening review. Existing provider acceptance is not approval of new clips or blanket authorization for new credential use. |
| Keep execution small and verification proportional. | `tasks/lessons.md:15–17` and `AGENTS.md:9–22` record the user's explicit rejection of TDD/excessive test churn, preference for a working visible slice and focused meaningful checks. | Begin with one complete math activity, then one short session. Verify in Simulator and with the child before building every topic or a generic engine. |

Paths in this document's evidence tables are relative to `/Users/devan/Projects/BrightPebble` unless fully qualified.

## Strong design decisions to carry over, with their limits

These are specified behaviors and early implementation patterns, not proven educational outcomes.

1. **A quiet board can still be playful.** One large picture/task in the center, generous space, an original supporting mascot, warm physical-looking pieces and a few clear controls. Keep decoration outside the reach path and still during choices. Short local responses can make success feel alive without constant bouncing. Source: `docs/design-system-spec.md:7,27–39,45`.
2. **Teach before judging.** A wrong valid answer gets gentle local feedback, not red flashes, harsh sounds, lost rewards or full-screen shaking. A missed/occupied/canceled drop is a motor event, not a wrong answer. Offer help after repeated deliberate errors; inactivity or replay does not automatically reveal answers. Source: `docs/core-game-spec.md:56,79–91`.
3. **Help has no reward penalty.** Child-requested assistance progresses from attention cue to specific hint to demonstration. Supported completion gets the same child-facing acknowledgment while the adult record distinguishes support. Source: `docs/core-game-spec.md:79–91,105–109`.
4. **Let a child leave well.** Pause offers Continue, Skip and Finish for now. Backgrounding suspends; it does not imply quitting. A summary counts completed, skipped and unfinished work truthfully. No countdown, speed prize, forced streak or automatic next round. Source: `docs/core-game-spec.md:40–44,76,107–109`.
5. **Audio serves the action.** Replay replaces speech; repeated taps do not queue speeches. Input remains usable during speech/celebration. Stop on pause/background/interruption, and return silently. One coordinator owns playback and invalidates old callbacks. Source: `docs/core-game-spec.md:95–101`; planned engineering contract in `docs/native-implementation-spec.md:53–61`.
6. **Accessibility shapes the activity.** Starting targets are 64×64 pt for child controls and 88×88 pt for movable learning pieces. Offer tap-select/tap-place alongside drag; use shape and position as well as color, stable focus, larger text, reduced motion, safe-area-aware portrait/landscape reflow. Never leak a hidden answer in a target's accessibility label. Source: `docs/design-system-spec.md:27–31,45–49`; `docs/core-game-spec.md:115–119`. These dimensions are starting design choices, not measured child usability results.
7. **Keep a small private footprint.** Local anonymous progress and bundled offline content are sufficient for the early app. No birthday, real name, microphone, precise touch trail or runtime provider call is needed. Record what the app can know: audio enabled/available is not proof the child heard it; completion is not mastery. Source: `docs/native-implementation-spec.md:11,31–39`.

## Where MathBuddy should deliberately go further

These are recommendations inferred for mathematics, not findings that BrightPebble already validated.

- **Make quantity visible and conserved.** Counting taps mark exactly one object; dragging does not duplicate it. Rearranging five apples still leaves five. Addition visibly joins two groups, subtraction moves objects away, equal sharing keeps the total unchanged. Decorative dots, fruit and stars must not be mistaken for countable task objects.
- **Show the idea in multiple forms.** A quantity can appear as physical objects, a structured five/ten frame, spoken number and numeral. Avoid a curriculum of merely matching numerals to attractive pictures. Later transfer tasks vary color, arrangement and story so success is less likely to be memorized art.
- **Separate age from readiness.** Ages four through eight cover a broad range. Start with an adult-chosen gentle entry and local observation of skills; do not label a child behind, diagnose ability or use age alone to unlock content. Keep the five-year-old's first experience very small.
- **Add creative reward play with a clear end.** BrightPebble's pebbles only acknowledge completion; a garden, tiny train scene or animal picnic would be a MathBuddy extension. Give a deterministic decorative choice after a small set of activities, then allow the child to leave. Help never lowers the reward. No countdown, randomized prize, purchase, energy refill, lost streak or inaccessible curriculum behind currency.
- **Specify accessible math variants honestly.** Describing a picture as “five ducks” can reveal a counting answer. Nonvisual counting may need individually discoverable objects or sound/tactile-oriented actions; that is an explicitly designed variant, not proof that an image label makes the original task equivalent.
- **Validate with the son before broadening.** Watch whether he knows what to touch, counts each item once, understands the help, can stop calmly and wants another session. These observations are usability evidence. Claims about retained learning require later transfer/revisit checks and broader evidence.

## Reuse prospects and boundaries

**Reuse the conventions first:** semantic color roles, custom native control semantics, explicit round/session identity, idempotent completion, stable object occurrence IDs, cancellation tokens, offline asset manifests with review status, and factual progress. Keep MathBuddy's math content and rules concrete until a second working activity demonstrates a shared need.

**Source exists but is changing:** the current uncommitted `BrightPebble/App/AppStore.swift:4–57` owns Home/game/pause/summary; `Game/GameSessionStore.swift:17–77` derives reward counts from completed rounds and guards stale advance events; `Game/WordRoundStore.swift:97–153,156–215` converges taps/drops on placement rules, separates neutral/wrong outcomes and implements the help ladder. `Views/WordGameView.swift:284–290,339–360` exposes positional labels, a raised dragged piece and Reduce Motion handling. These are candidates to study, not a stable shared library or a claim that current Slice 2 validation passed.

**Do not copy yet:** three-letter slot rules, phonics schemas, reading-specific support modes, broad future reducer/storage/audio designs that are still specifications, or an unreviewed asset pack. A new shared package would be premature. Reuse the existing production workflow without modifying BrightPebble while its session is active.

**Evidence ceiling:** `docs/phase-1-validation.md:97–105` explicitly limits the verified result to a silent, in-memory prototype and keeps audio, persisted recovery, child use, physical iPad use, full assistive use and learning validation open. The source tree now includes active work beyond that record; this review did not build or exercise it. Older checkpoint claims that no native app exists are superseded by the Slice 1 validation record; newer source alone does not prove a later milestone complete.
