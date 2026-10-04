# Engineering and iPad readiness — 2026-10-04

## Assessment
The reviewed pilot is **not ready for installation and family testing on an iPad**. A preserved native experiment exists and has historical simulator build evidence. That is useful groundwork, but it does not implement the approved pilot or establish a current signed physical-device build.

This was a read-only engineering audit of source, configuration, saved verification and the active phase tracker. No fresh native build, device installation, signing change or implementation was performed. The user’s asset acceptance and explicit CNT-01 authorization gates remain in force.

## Remaining work

| Area | Current evidence | Required before the relevant pilot gate |
| --- | --- | --- |
| Reviewed offline content | World/branding work is interrupted; audition has ten prepared requests and no recordings. Later asset phases and Phase 2E are not started. | Complete assets, narration, motion and review packets; verify 24 reviewed content records, 101 voice mappings and the offline delivery package. Obtain human pack acceptance. |
| First native slice | The preserved model defaults to mixed practice and begins with five-of-six counting, alongside joining and subtraction. | After explicit authorization, implement CNT-01 only: three berries from five, with help, undo, silence, recovery and resume. Demonstrate it before advancing. |
| Durable state and recovery | Experimental state uses `MathBuddy/progress-v1.json`; missing narration currently returns silently. | Use the reviewed pilot namespace, validate content/media references, handle damaged or missing state/media visibly, and verify interrupted-session restoration. |
| Learning, sessions and garden | Existing evidence uses aggregate counts; garden has a pinwheel and accumulating flowers. | Implement reviewed joining/taking-away checkpoints, action-only versus numeral evidence, bounded sessions and six distinct durable grant-once rewards through individually approved native phases. |
| Grown-up controls and accessibility | No completed reviewed continuity/accessibility phase. Historical review lists unverified interactions. | Complete the selected adult gate, sound/motion controls, honest summaries, reset/recovery, VoiceOver, Switch Control, Reduce Motion and touch alternatives. |
| Physical installation | Candidate project is iPad-only, iPadOS 18+, automatic signing, but no development team is configured in repository settings. No signed installable package or physical-install evidence found. | Choose the actual iPad and OS target, select the signing team, prepare a signed device build and prove installation/launch on that device. An external local signing setup has not been established by this audit. |
| Device and family validation | Oct 3 simulator Debug/Release build, install/launch and rule-script evidence exists. Most screenshots use seeded fixtures. No current physical-device run. | Verify real touch/audio flows, offline operation, relaunch/resume, orientations, split view, Dynamic Type, accessibility, performance and willing-child observations in Phase 5. |

## Evidence locations
- [Experiment status](../experiments/README.md), line 11: preserved/shelved native experiment.
- [Master tracker](phase-tracker.json): asset and native phases remain incomplete; human gates remain pending.
- [Native implementation plan](../plans/2026-10-03-native-pilot-implementation-plan.md), lines 25–35, 44–72, 150–154 and 318–322: device decisions, CNT-01 scope, storage/recovery, learning evidence and reward requirements.
- [Current models](../../MathBuddy/Model/MathBuddyModels.swift), lines 29–40 and 151–178: mixed practice, aggregate evidence and experimental sequence.
- [Current store](../../MathBuddy/Model/MathBuddyStore.swift), lines 16–21: experimental persistence namespace.
- [Current audio](../../MathBuddy/Audio/MathBuddyAudio.swift), lines 14–20: missing narration returns.
- [Current garden](../../MathBuddy/Views/GardenView.swift), lines 83–100: experimental reward presentation.
- [Project configuration](../../project.yml), lines 4–9 and 43–49; generated project: candidate deployment and automatic-signing settings, no configured development team.
- [Historical native verification](../verification/native/README.md), lines 9–15, 30 and 34–36: successful simulator checks and explicitly unverified interactions.
- [Shared Xcode scheme](../../MathBuddy.xcodeproj/xcshareddata/xcschemes/MathBuddy.xcscheme), lines 41–42: no test targets. Standalone rule scripts do not replace device interaction tests.

## Next authorized steps
Finish the bounded asset sessions and present concrete review packets, including the independent voice/provider decision packet. Native work begins only after full asset-pack acceptance and explicit authorization for CNT-01. Later native phases each require their own demonstration and approval to continue. The iPad/signing choices remain open and must be resolved before device installation; this audit does not select them for the user.
