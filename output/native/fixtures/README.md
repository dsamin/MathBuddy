# Native rendering fixtures

These ten saved-state inputs are produced by real MathBuddyStore methods in isolated temporary storage.
They contain no user data. Answers, object placement, phases, statistics, and rewards result from real
model transitions. UUIDs and timestamps are produced by the store. Each fixture is reloaded through
MathBuddyStore and compared before export; authored scene states are repeatable.

Loading a fixture and capturing its native screen proves rendering of that saved state. It does not
demonstrate taps, dragging, audio, animation timing, accessibility interaction, or a complete UI flow.
Screenshots made from these files must be described as fixture-based native render checks.

Regenerate from the repository root:

```sh
swiftc -swift-version 6 -parse-as-library MathBuddy/Model/MathBuddyModels.swift MathBuddy/Model/MathBuddyStore.swift scripts/make-review-fixtures.swift -o /tmp/mathbuddy-review-fixtures
/tmp/mathbuddy-review-fixtures output/native/fixtures
```
