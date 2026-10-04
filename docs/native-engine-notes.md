# Native session and persistence implementation

> **Historical, shelved experiment.** These notes describe existing code, not an approved product baseline. The active work is the [feature specification](feature-spec.md) and [asset-first roadmap](roadmap.md).

The native app uses an `@MainActor @Observable MathBuddyStore` with Codable value models. No rendering, audio timing, animation completion, or network call decides mathematical correctness. All authored object IDs stay fixed for a round; packing and sharing change a set of locations.

## Implemented behavior

- Default mixed session: make five from six berries; join two and one; transfer two from five, then answer how many remain. The five-round setting adds count-three and join-one-and-two. Counting-only uses three or five authored subset-counting examples.
- Counting and transfer moves are reversible. Undo after joining separates the groups. Success freezes the round; Continue is a deliberate action. Subtraction checks the transfer before offering the remaining-quantity question.
- A wrong submitted answer retains the scene. Help models correct placements or names and explains the total. Two submitted misses trigger this support automatically. Assistance remains recorded after Undo and relaunch.
- Progress starts at zero. Each completed round increments its activity's completion count once and its help count if support was used. “Without extra help” does not claim a first-try correct answer, mental arithmetic, fluency, or mastery. Incomplete rounds do not increment statistics. Current-session evidence also retains submission count and first-submission correctness.
- Settings changes apply to the next session. Home and Finish for now preserve unfinished work. Starting over and resetting progress require confirmation in the adult UI.
- Final Continue saves a completion UUID and garden entitlement in the same atomic JSON file. Repeated Continue, reopening the garden, and relaunch cannot duplicate that completion. The first pilot toy is a permanent pinwheel; later sessions are counted without presenting a wider toy catalog as implemented. Pinwheel placement persists.

## Persistence

The version-1 JSON checkpoint is stored in the app's Application Support directory at `MathBuddy/progress-v1.json`. It includes route, settings, round state/history, statistics, and garden inventory. Each semantic action writes the small checkpoint atomically. The app performs no external synchronization. Save failures appear through `storageNotice`, while current in-memory work remains usable.

Decoded checkpoints are validated before use. An unreadable or unsupported save is preserved; normal actions cannot overwrite it. The adult can explicitly reset local progress to recover. This is format validation, not a migration framework; future schema versions need a deliberate migration.

## Focused verification

Compile and run the standalone harness from the repository root:

```sh
swiftc -swift-version 6 -parse-as-library MathBuddy/Model/MathBuddyModels.swift MathBuddy/Model/MathBuddyStore.swift scripts/check-native-rules.swift -o /tmp/mathbuddy-rule-checks
/tmp/mathbuddy-rule-checks
```

The harness uses an isolated temporary directory and checks invalid object IDs, wrong-answer recovery, undo, assistance preservation, exact relaunch state, duplicate completion, both subtraction checkpoints, reward grants after three/five rounds, counting-only content, zero-valued definitions, and read/write failure handling. It does not prove physical iPad interaction, VoiceOver usability, animation quality, learning gains, or the full proposed ages-four-to-eight curriculum.

Verified October 3, 2026: Swift 6 typechecking and the compiled rule harness passed on the available macOS toolchain. App-build and Simulator evidence belong in the root native verification record.
