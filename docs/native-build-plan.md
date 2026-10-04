# Native iPad correction and first build

> **Historical, shelved experiment.** This plan was executed prematurely. It is not the approved roadmap and does not authorize more implementation. Start with the [asset-first roadmap](roadmap.md).

The assistant incorrectly interpreted the user's platform clarification as authorization to implement. This document records the resulting premature SwiftUI experiment; the current deliverable is the specification, asset plan and roadmap. No web view, JavaScript runtime, Capacitor, React Native, or bundled website is part of the app.

## Scope
- iPad-only SwiftUI app, iPadOS 18 baseline consistent with the available sibling-app Simulator; portrait and landscape layouts.
- Home, count from a larger set, visible addition, two-stage subtraction, garden reward, adult settings/progress.
- Native spring/movement animation and a finite pinwheel spin; respect system and in-app Reduce Motion.
- Stable piece identity, undo, gentle error recovery, assistance flags, local progress and interrupted-session recovery, idempotent rewards.
- Generated original raster mascot and garden illustrations in asset catalogs, with scalable native vector fruit/basket/pinwheel art for mathematical clarity and animation.
- Bundled audio effects and an explicit production-narration inventory. Natural prerecorded voice is the specified production direction; no silent substitution with system TTS.
- Parent access uses native device-owner authentication where available, with a clearly labeled Debug-only review entry for Simulator. No claim of release readiness without device testing.

## Work boundaries
1. Root: Xcode project, app entry point, integration, assets manifest, documentation, build and Simulator verification.
2. Native logic worker: Swift state/session/progress/persistence, focused logic checks.
3. Native UI worker: SwiftUI views and native vector artwork, based on agreed state API.
4. Artwork worker: image generation and asset-catalog integration for mascot and background; source prompts and asset manifest entries.

## Verification
- Compile Debug and Release with the installed Xcode toolchain using a per-command developer directory.
- Source/bundle check: no WebKit/WKWebView, JavaScript, remote asset URLs or third-party frameworks.
- Install in a dedicated MathBuddy iPad Simulator, inspect actual UI, perform the full loop, wrong-answer recovery, undo, garden revisit, and relaunch.
- Inspect landscape and portrait, Reduce Motion behavior, and accessibility labels. Report simulator evidence separately from physical-device and child validation.
- Inspect generated image files and confirm required resources are present in the built app bundle.
- Document delivered versus still-proposed curriculum/features/assets. Do not claim full ages-4–8 curriculum completion from this first build.
