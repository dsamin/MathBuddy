# Native iPad verification — October 3, 2026

> **Historical experiment evidence.** These checks do not approve the product, its assets, or any phase of the current [asset-first roadmap](../../roadmap.md). The experiment is shelved.

The deliverable is `MathBuddy.xcodeproj`, a native SwiftUI application. The earlier HTML design study is outside the Xcode target and app bundle.

## Proven

- Debug and Release compile successfully for iOS Simulator using installed Xcode 27.0 (build 27A266a), SDK 27.0, deployment target iPadOS 18.
- Installed and launched on a dedicated **MathBuddy Review / iPad Pro 11-inch (M4), iOS 18.3.1** Simulator. The existing BrightPebble Simulator was not changed.
- Native home screen rendered and was visually inspected. Nine further scene screenshots use saved-state fixtures produced by the real Swift session engine and reloaded by the app.
- Focused Swift 6 rule checks passed: reversible moves, valid object identity, incorrect-answer recovery, help evidence, both subtraction checkpoints, counting-only and mixed three/five-round sessions, saved resume, duplicate-completion protection, and visible storage failure handling.
- The built Release bundle declares only device family `2` (iPad), contains compiled native assets plus 19 narration clips and three effects, and matches every narration master hash.
- Source and built-bundle checks found no WebKit, JavaScriptCore, HTML/JavaScript/CSS payload, provider credential, or runtime networking implementation. The Simulator review entry is absent from the Release binary.
- Native resource/bundle audit: [bundle-audit.json](bundle-audit.json). Render provenance: [render-checks.json](render-checks.json).

The build emits only an App Intents metadata-extraction warning because this app has no App Intents dependency.

## Native screenshots

These are actual Simulator captures, not browser mockups or generated screen designs.

- [Home](01-home-portrait.png)
- [Counting in progress](count-partial-portrait.png) · [Counting complete](count-success-portrait.png)
- [Addition: separate groups](addition-before-portrait.png) · [Addition: joined](addition-after-portrait.png)
- [Subtraction: transfer](subtraction-before-portrait.png) · [Subtraction: remaining group](subtraction-after-portrait.png)
- [Earned reward](garden-unplaced-portrait.png) · [Garden with pinwheel](garden-placed-portrait.png)
- [Goodbye](goodbye-portrait.png)

The fixture generator is `scripts/make-review-fixtures.swift`; its ten checkpoints live under ignored `output/native/fixtures`. Captures temporarily seeded only the dedicated MathBuddy Simulator's app data; its previous checkpoint was restored afterward. Fixture images demonstrate layout, object quantities and resource loading. They do **not** demonstrate successful taps, gestures, audio listening, or animation playback.

## Remaining verification

Apple's Device Hub viewer remained at **“Installing system components…”** during the review. The Simulator backend can run the app and capture frames, but interactive access through the viewer was unavailable. No claim is made that the full touch flow, native parent gate, VoiceOver, landscape, split-view, large Dynamic Type, or reduced-motion behavior passed interactive testing.

Before a family build: run the full flow on an iPad, listen to every voice take, test landscape/portrait and interruption/resume, inspect VoiceOver order, test the native parent gate and confirm reward/undo gestures. Evaluate learning and enjoyment with the child; the app has no demonstrated learning efficacy claim.

## Reproduce builds

On this machine the installed Xcode folder retains an older name. Use a per-command developer directory; the global developer selection was not changed.

```sh
DEVELOPER_DIR=/Users/devan/Applications/Xcode_26.3.app/Contents/Developer xcodebuild \
  -project MathBuddy.xcodeproj -scheme MathBuddy -configuration Debug \
  -destination 'platform=iOS Simulator,id=C8ABB3DC-68E7-41A1-9A08-E0DEDA066D55' \
  -derivedDataPath DerivedData CODE_SIGNING_ALLOWED=NO build
```

Change Debug to Release for the second configuration. Build logs are in ignored `output/native/`. Physical-device installation needs your signing team. The broader proposed ages-four-to-eight curriculum remains a roadmap, separate from this working native pilot.
