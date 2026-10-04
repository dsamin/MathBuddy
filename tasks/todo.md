# MathBuddy design review — 2026-10-03

## Current work — independent review and detailed implementation planning

- [x] Confirm review/planning-only scope and preserve application/asset files.
- [x] Obtain a fresh independent review of the feature spec, pedagogy assumptions, scope and phase boundaries.
- [x] Create a complete pilot asset register, exact content/script coverage and production dependencies.
- [x] Draft a detailed phase-by-phase implementation plan with ownership, interfaces, checks and stopping points.
- [x] Reconcile review findings into the spec and plans; record open user choices without implying approval.
- [x] Verify cross-document coverage, asset references and unchanged experiment files; deliver the review packet.

**Authorized now:** independent agent review, asset requirements/inventory, and detailed planning. **Not started:** artwork/audio generation, app code, builds or phase execution.

### Review result — independent review and planning

- Three agents delivered an independent spec review, the exact asset/content/voice inventories, and a detailed native phase plan. A focused second review caught response-mode eligibility and authored layout/occurrence gaps; both were resolved in the proposal.
- Updated the specification to v0.4: one count-three-from-five first phase, visible quantity references for silent play, per-checkpoint evidence, neutral retry versus help, current-action audio rules and finite rewards.
- Inventory: 196 logical requirements, including 22 artwork requirements, 36 native design definitions, seven motion briefs, six effects, 24 authored variants and 101 unique voice scripts. These are requirements, not produced media.
- Detailed native plan specifies phase ownership, files, interfaces, meaningful checks, failure behavior and individual review checkpoints. Native region identifiers were reconciled with the authored catalog.
- [Planning audit](../docs/planning/validation-report.json): 23 checks passed; 77 local links checked, 97 occurrences verified, and all 149 protected experiment files unchanged with no additions/deletions. This does not establish runtime behavior, media quality, educational efficacy or user approval.
- [Review checkpoint](../docs/review-checkpoint.md) is the primary reading entry. Recommended next work is the small Phase 1 creative-direction sample, when selected. No new assets, app code, builds, provider requests, commits or Pebble changes occurred.

## Prior completed work — specification and asset-first planning reset

- [x] Acknowledge implementation overreach and stop app/asset production.
- [x] Record the correction and distinguish platform requirements from permission to build.
- [x] Refresh Pebble workflow lessons from its current planning and asset-review documents.
- [x] Reset the product spec to proposed features, with clear first-pilot and later scope.
- [x] Write the asset inventory, review criteria, generation batches and motion/audio requirements.
- [x] Write a phase roadmap with dependencies and review outcomes; leave individual build plans for later.
- [x] Make planning documents the README entry point; label earlier code/art/audio as unapproved experiments.
- [x] Review documentation consistency and report the plan without starting execution.

**Boundary for this turn:** documents only. No app changes, builds, deployments, paid generation, or changes to Pebble. Existing experiment files stay intact so nothing is lost; they create no commitment to reuse them.

## Historical native experiment — built prematurely; not the approved roadmap
- [x] Confirm the prior deliverable contains no native target; record the native-only requirement in lessons.
- [x] Write the native scope and verification plan in `docs/native-build-plan.md`.
- [x] Build the SwiftUI session engine and native screens.
- [x] Generate and bundle artwork and native visual/audio assets; record completeness.
- [x] Compile Debug and Release; verify no embedded web implementation.
- [x] Run and inspect actual native portrait screens in a dedicated iPad Simulator; verify persistence in the rule harness.
- Deferred with the shelved experiment: interactive iPad/Simulator pass, landscape, VoiceOver, parent gate and audible review. This is not an active task.
- [x] Replace README's primary entry point with the native project and record native evidence.

## Brief
Review the supplied Muse spec and BrightPebble lessons. Propose a beautiful, simple native iPad math app for ages 4–8, initially tuned for a five-year-old, with illustrated activities, purposeful animation, and completion rewards. The current deliverable is a feature specification, asset-first production plan and staged roadmap. The native experiment was built beyond the requested scope and is not the product baseline.

## Plan
- [x] Inspect workspace, shared instructions, and available project history.
- [x] Read the supplied Muse artifact in the browser.
- [x] Gather evidence from BrightPebble and primary learning/platform sources.
- [x] Review the original spec: keep, change, resolve contradictions, defer.
- [x] Write the feature specification, example flows, age progression, and native architecture proposal.
- [x] Create illustrated, interactive iPad mockups for home, counting, addition, subtraction, rewards, and grown-ups.
- [x] Verify the mockup paths and inspect layout at iPad dimensions.
- [x] Record review findings and deliver the spec plus mockups for discussion.

## Scope and assumptions
- Native iPad is a platform constraint. The user has explicitly requested planning and assets before any phase of app implementation.
- BrightPebble is the related app based on matching active project context; read it without changing it.
- MathBuddy is a working app name. Pip’s Picnic is the source concept; names and themes remain review decisions.
- The cross-project notebook at `~/.Codex/IDEAS.md` was not present; no substitute notebook created.
- Child capability and theme preferences are optional questions pending a response.

## Review

### Specification review
- The supplied artifact was fully read in the browser after the web text reader could not access it.
- Read-only BrightPebble research is recorded with source paths and the limits of its existing verification.
- Primary IES, curriculum, and Apple sources checked; no efficacy claim carried into the proposal.
- Independent review found and resolved five details: early-level answer paths, configured session/reward length, accessible answer leakage, safe active-content failure handling, and presentation-only explanation replay.
- Documentation relative links, placeholder scan, and whitespace check passed.
- No credentials, attribution trailers, or generated-by footers were added.

### Earlier browser mockup verification (historical)
- `node --check mockups/app.js`: passed.
- Browser flow: Home → Count → Add → Take away → Garden → plant pinwheel → spin → Done for today → Home passed.
- Count: submitting 0 gives a recoverable hint; all 6 gives an over-count hint; removing one produces 5 and permits completion.
- Addition and subtraction: incorrect numeral, gentle feedback, correction to 3, and post-success equations passed.
- Adult gate shows its prototype limitation; sample stage selection, Reduced Motion toggle, and Reset demo passed.
- Fixed answer-revealing accessibility group labels. Final accessibility tree exposes three individual Berry images in the shared/remaining mat; hidden moved-object ghosts are excluded.
- Replaced ambiguous progress bars with explicitly illustrative tries with and without help.
- Fixed parent-content clipping and the aspect-ratio/min-height interaction that made portrait frames too wide.
- Checked all 6 scenes at 1194×834, 1024×768, 834×1194, and 744×1133 browser viewports: 24 layout checks; no horizontal document overflow or clipped button bounds. Browser scrollbar accounts for some smaller measured inner widths.
- Runtime warning/error log was empty at final inspection.
- Saved six full-page screenshots in `mockups/previews/`; geometry evidence is `mockups/previews/layout-checks.json`.
- Visual inspection covered Home, Count, operations, Garden, and Grown-ups; final parent controls are fully visible. Temporary viewport overrides were reset.
- Audible output, native VoiceOver, real iPad performance, native persistence, and child learning were not validated. No production app was built.
- Local review server: `http://127.0.0.1:8766/mockups/`. Direct-file alternative: `mockups/index.html`.

### Native correction review
- Built iPad-only SwiftUI target, with native views/animations, JSON persistence, original illustration/vector assets and offline narration/effects.
- Corrected XcodeGen target device-family defaults, read-only system accessibility environment misuse, parent-sheet background relocking and garden narration conditions.
- Debug and Release builds pass; Release bundle audit proves iPad-only, no web payload/runtime, no credentials and complete 19+3 audio coverage.
- Swift 6 executable rule harness passes. Native Simulator installation/launch succeeds; portrait screenshots were inspected.
- Apple's Device Hub component installer blocked live viewer input; saved-state rendering is explicitly separated from unverified touch/animation/accessibility tests. See docs/verification/native/README.md.
- Full future curriculum and human voice/child/device acceptance are not claimed complete.

### Planning reset review — current deliverable
- Refreshed Pebble workflow evidence from its actual review checkpoint, asset task/handoff and individual phase plan; kept its existing work untouched.
- Made the feature spec, new asset plan and new roadmap the primary artifacts. Existing code, art, audio and verification are explicitly shelved/unapproved, with no deletion or relocation.
- Defined a direction audition, pilot asset batches, state/layer coverage, motion briefs, script families and separate technical/human review decisions.
- Reconciled the finite pilot reward collection, deferred music/adaptation/sharing, small-set parent choices, overshoot audio through six, and optional dragging checks.
- Independent review found and resolved the three scope/coverage issues above. Checked local Markdown links across 14 documents; no broken references.
- This turn changed planning/documentation only. No app code, builds, asset generation, provider requests or Pebble changes were made. The planning packet is complete for review; no product/asset/build-phase approval is implied.

## 2026-10-03 — Authorized Git baseline and Phase 1 direction samples

Scope: establish a local checkpoint, then execute only the small creative-direction comparison. No GitHub URL supplied. Pip’s Picnic is provisional. Existing native code, art, recordings and browser studies stay preserved and unapproved. The 196 requirements and 24 variants remain planning inventory.

### Plan and acceptance checks
- [x] Inspect applicable instructions and all meaningful project files; audit ignore rules, binary sizes and staged secrets.
- [ ] Initialize local Git and commit preserved meaningful work as a baseline; report remote status accurately.
- [ ] Read the planning packet and reconcile the focused review agent’s material dependencies.
- [ ] Produce two comparable directions: identity/attentive/pleased poses, count-three from five with count-five consideration, garden with pinwheel/free flower/Finish, portrait and landscape, explicit sound-off target.
- [ ] Preserve exact prompts, source takes, request/provenance and pending-human-review labels under the asset plan’s folders.
- [ ] Produce a short pickup/return/settle motion study plus all seven provisional layer/motion contracts, with Reduced Motion alternatives.
- [ ] Produce two candidates × the same five catalog audition lines if a generation capability is available; otherwise record the specific gap and preserve ready-to-run requests.
- [ ] Inspect actual images and motion; audit quantity, identity, visibility and layer feasibility. Measure audio and verify actual wording where capability permits.
- [ ] Record technical results separately from human art, listening, wording and provider/rights decisions.
- [ ] Review and secret-scan the final diff, commit Phase 1 separately, and present sample links, hashes, limitations and recommendation.
- [ ] Stop at Phase 1 review; no bulk pilot asset production, native edits/builds or Pebble changes.

### Pre-execution check-in
The requested comparison is bounded to warm paper illustration versus clean soft-shape storybook, using the same rabbit, count-three task and garden objects. The user has explicitly authorized these samples and both Git checkpoints. Full source/layer delivery belongs to a later reviewed phase; the sample boards will not be marked native-ready.

### Review results
Pending execution and technical inspection. Human selections remain pending.
