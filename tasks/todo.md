> Active session: full pilot coordination under docs/orchestration/README.md. Five Pip poses approved; remaining Phase 2A starts in a separate Sol session. Native work remains gated. Earlier sections below are historical.

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
- [x] Initialize local Git and commit preserved meaningful work as a baseline; report remote status accurately. Baseline: `18b36ed`; no remote.
- [x] Read the planning packet and reconcile the focused review agent’s material dependencies. See `docs/reviews/2026-10-03-phase1-dependencies.md`.
- [x] Produce two comparable directions: identity/attentive/pleased poses, count-three from five with count-five consideration, garden with pinwheel/free flower/Finish, portrait and landscape, explicit sound-off target.
- [x] Preserve exact prompts, source takes, request/provenance and pending-human-review labels under the asset plan’s folders.
- [x] Produce a short pickup/return/settle motion study plus all seven provisional layer/motion contracts, with Reduced Motion alternatives.
- [x] Record unavailable natural voice generation and preserve ten ready-to-run requests, exact source snapshot and listening sheet.
- [ ] Outstanding: produce and inspect the ten actual voice audition takes after an authorized provider becomes available.
- [x] Inspect actual images and motion; audit quantity, identity, visibility and layer feasibility. Measure audio and verify actual wording where capability permits.
- [x] Record technical results separately from human art, listening, wording and provider/rights decisions.
- [x] Review and secret-scan the final diff, commit Phase 1 separately, and present sample links, hashes, limitations and recommendation. The separate checkpoint commit is reported in the final response.
- [x] Stop at Phase 1 review; no bulk pilot asset production, native edits/builds or Pebble changes.

### Pre-execution check-in
The requested comparison is bounded to warm paper illustration versus clean soft-shape storybook, using the same rabbit, count-three task and garden objects. The user has explicitly authorized these samples and both Git checkpoints. Full source/layer delivery belongs to a later reviewed phase; the sample boards will not be marked native-ready.

### Review results
Two directions × two preserved takes are reviewable; take-02 repairs Finish contrast. Seven provisional motion/layer briefs/storyboard PDFs and normal/Reduced Motion 4.8-second studies were actually decoded and reviewed. Ten voice requests match the catalog; all ten recordings are missing because credentials are unavailable. Technical findings are separate from pending human art/listening/provider decisions. No native edits/builds, bulk pilot generation or Pebble changes occurred. See `docs/reviews/2026-10-03-phase1-checkpoint.md`.

## 2026-10-03 — Direction B selection and next-step prompts

Scope: record the user's selection of B and provide the next steps/prompts. This turn does not execute Phase 2 or generate more media.

### Plan and acceptance checks
- [x] Record B as selected by the user, with the actual reference hash; preserve all original samples.
- [x] Keep character identity, individual asset, voice, motion and provider/rights decisions separate and pending.
- [x] Review phase dependencies with a focused agent and propose bounded next batches.
- [x] Prepare copy-ready prompts: five Pip poses; remaining world/branding; independent ten-take voice audition.
- [x] Verify selection metadata, links, source hashes and the changed review gallery; confirm no new media/native changes.
- [x] Inspect the diff and scan staged changes for secrets; save the documentation checkpoint with its hash reported in the final response.
- [x] Prepare the recommended first prompt and remaining choices for presentation; stop without starting a new asset batch.

### Pre-execution check-in
The user's “Lets go b. Provide me the next steps and prompts” selects the rendering direction and asks for planning deliverables. Recommend the five aligned character poses before dependent world/branding. Voice audition remains independent and needs a configured provider. Prompt submission later authorizes only its named batch.

### Review results
See [Direction B next steps and session prompts](../docs/plans/2026-10-03-direction-b-next-steps.md). The package audit passes with the explicit ten-recording gap: 48 JSON files parsed, source/prompt hashes match and 31 gallery/listening links resolve. All 25 local Markdown links in the touched documents resolve. Gallery selection labels match the decision record. No media or native files changed since the Phase 1 checkpoint. Focused review confirmed requirement counts and stopping points; the voice prompt now explicitly requires pre-run cost/terms review and AI-voice disclosure.


## 2026-10-03 — Focused gallery hook triage

Scope: review the four findings in the adult Phase 1 gallery only; preserve selected B, all sample media and future phase boundaries. Attribution was unknown; these are not classified as session regressions.

- [x] Inspect actual styles and browser hierarchy before editing.
- [x] Remove the unnecessary callout stripe; change status to sentence case and move uppercase header metadata to the footer.
- [x] Persist narrow file-scoped exceptions for the measured hierarchy false positive and intentional picnic paper background.
- [x] Confirm rendered changes, detector results and unchanged sample/native files; record triage and prepare the secret-scanned checkpoint.

### Review
[Triage report](../docs/reviews/2026-10-03-gallery-hook-triage.md): two fixes, two narrow exceptions, no standing findings. Browser confirmation passes at 1280×720; the detector’s single post-edit pass found only the waived typography/palette findings. Original sample media and native files are unchanged. The local checkpoint hash is reported in the final response.

## 2026-10-03 — Reconcile the supplied Direction B planning checkpoint

Scope: planning documents only. The three quoted execution prompts describe future separately submitted batches; their embedded authorization does not start generation in this turn. No provider requests, media generation, app edits/builds, commits or Pebble changes.

### Plan and acceptance checks
- [x] Inspect Git, applicable instructions and lessons; compare the supplied next-step plan with the saved planning checkpoint.
- [x] Verify the selected reference hash, ten immutable voice requests and missing production pose/audio outputs.
- [x] Obtain a focused independent review of dependencies, acceptance checks and approval boundaries.
- [x] Reconcile the primary review entry point with the recorded Direction B selection and recommended five-pose batch.
- [x] Verify local links, diff scope, unchanged production/experiment files and absence of sensitive values; record the review results.

### Pre-execution check-in
The saved next-step prompts already cover the requested bounded batches. Update the primary reading entry so it recommends the five-pose review after Direction B selection. Keep the original specification-review evidence identifiable as history and leave character identity, name, device, motion, voice and rights decisions pending.

### Review results
The independent review found no material mismatch between the supplied prompts and the saved plan. The selected Direction B reference and all ten voice request hashes match their records; production pose folders and WAV recordings remain absent. The primary checkpoint now recommends the separately requested five-pose batch and distinguishes rendering selection from pending identity/art decisions. Fifteen local Markdown links resolve, whitespace checks pass and the diff scan found no sensitive-value patterns. Only this task record and the primary checkpoint changed; the prompt document, media, app and experiments remain unchanged. No generation, provider requests, builds, commits or Pebble changes occurred.


## 2026-10-04 — Authorized Phase 2A character review batch

Scope: only PIP-01 idle-welcome, PIP-02 attentive-pointing, PIP-03 supportive-thinking, PIP-04 pleased and PIP-05 farewell. Direction B take-02 defines rendering; Pip’s Picnic and the attentive-reference ear refinement remain provisional. The user explicitly authorizes five-pose generation and a local Git checkpoint. Preserve existing dirty documentation and all experiments.

### Plan and acceptance checks
- [x] Inspect Git/instructions and lessons; read the selection/reference and M04/M05/M07. Save preflight hashes and obtain a focused review agent’s constraints.
- [x] Record this bounded plan and check in before any provider request.
- [x] Generate five transparent full-body stills with the same attentive-reference face/body/scarf/ears; preserve every original take and exact tool request.
- [x] Produce reproducible aligned RGBA review candidates on 1536 × 1536, fixed scale, safe box and foot anchor (0.5,0.90). No painted text, rig or sprite sequence.
- [x] Decode and measure actual alpha/bounds/baseline/anchor; inspect light/dark composites, anatomy, ears, scarf, crops, halos and identity.
- [x] Show all five in a labeled pose sheet and 256/128/64-pixel canvas readability previews; obtain focused independent review.
- [x] Register source/prompt/request/reference/recipe/output hashes and provenance; record technical results separately from pending human identity/art/content/rights.
- [x] Verify changed-file scope, prior file hashes, links and reproducibility; secret-scan the staged checkpoint, then commit locally.
- [x] Stop for character review without environments/branding/math/rewards/audio/motion/app/build/Pebble work.

### Pre-execution check-in
Five built-in image_gen calls, one pose per call, using only selected Direction B take-02 and the new pending idle pose as identity reference. Propose two rounded unbent ears, viewer-left splayed and viewer-right upright, based on the attentive sample; do not repeat the pleased sample’s folded ear. Shared provisional canvas/anchor matches M04/M05/M07. Technical alignment and preview composites may use deterministic Pillow export recipes; preserve provider originals and alpha, never repaint identity or fabricate separate character/shadow layers. A measured technical pass does not approve art or physical iPad usability.

### Review results
Five built-in provider takes and five aligned 1536² RGBA candidates exist with full requests/provenance. Actual light/dark, edge/detail, baseline/anchor and 256/128/64-pixel previews were inspected. The focused independent reviewer found no mandatory repair; thinking is calm and ears/scarf/identity coherent. Recipe --check reproduced all exports and sheets byte-for-byte. Canvas/core foot baseline/anchor/safe-box checks pass with disclosed one-pixel scale and 0.5-pixel center rounding. Generated originals are 1254², larger exports add no detail; tiny alpha finishing, subtle small-size expression and untested crossfades/device/child usability are explicit. Human identity/art/content/rights remain pending. See [character review](../assets/production/picnic-v1/review/contact-sheets/pip-character-review.md). Final scope audit confirms 330 protected prior files unchanged, all 51 document links resolve, whitespace checks pass and the staged gitleaks scan finds zero leaks. All batch work stops at human character review. The local checkpoint hash is reported in the final response.

## 2026-10-04 — Keep five poses and prepare Astra orchestration handoff

Scope: record the user's keep decision for all five current poses and prepare a copy-ready master prompt for the full pilot with human review checkpoints. This turn creates no phase sessions, media, native changes, builds or Git commits.

### Plan and acceptance checks
- [x] Read current phase requirements, review records, lessons and applicable handoff skill.
- [x] Confirm the requested orchestration scope: full pilot, with human review checkpoints.
- [x] Record human identity/art approval against the exact five take-01 files and hashes; preserve technical limitations and pending content/rights decisions.
- [x] Obtain focused sequence/dependency review and prepare one Astra master prompt with a separate GPT-6.1 Sol session per bounded phase.
- [x] Include actual Codex session creation, model identities, file ownership, durable handoffs, verification, review gates and native/family boundaries.
- [x] Verify approval hashes, links and planning-only diff; document results and present the prompt without starting orchestration.

### Pre-execution check-in
The user's “Yes keep all 5” accepts the five reviewed character poses and their shared ear construction. The follow-up scope choice is “Full pilot, with human review checkpoints.” Record that decision separately from immutable generation-time reviews. The future master may coordinate Phase 2A world/branding through Phase 5, using distinct phase sessions and recorded human approvals; Phase 6 expansion is excluded. Human review of the complete asset pack precedes authorization of the first native CNT-01 slice.

### Review results
The [character selection record](../assets/production/picnic-v1/metadata/pip-character-selection.json) pins all five take-01 original/aligned hashes; the live decision ledger records user identity/art approval while rights/content/delivery remain separate. The [Astra master prompt](../docs/plans/2026-10-04-astra-master-prompt.md) defines actual Codex sessions, phase worktrees, ownership, durable handoffs, integration and the full pilot review sequence. Focused review confirmed models, counts and native gates; refinements ensure approved inputs are committed before creating worktrees and include Switch Control in family validation. All 41 local Markdown links resolve, whitespace checks pass and the diff scan found no sensitive-value patterns. Only planning/decision/review records changed; source media and app files remain intact. This turn launched no phase sessions, provider requests, media generation, app edits/builds, commits or Pebble work.

## 2026-10-04 — Active full-pilot orchestration

- [x] Read the submitted master instructions, applicable instructions and lessons; inspect Git and recorded approval.
- [x] Verify all 12 pinned direction/character image hashes and preserve original media.
- [x] Reconcile current catalog identity/art status against the human selection, preserving generation-time evidence.
- [x] Write master plan, ownership, phase tracker and bounded Phase 2A brief.
- [x] Secret-scan and commit approved inputs before dependent worktree creation (`e48eb49`; zero gitleaks findings).
- [x] Create the separate GPT-6.1 Sol Phase 2A world/branding task from that checkpoint; direct thread read confirms active session `01a10777-964b-7380-ad50-122d3de368d8`.
- [ ] Prepare independent voice-audition provider/cost/rights/capability decision packet in its own Sol task.
- [ ] Verify returned Phase 2A artifacts, scope, hashes and source reproducibility; integrate a local candidate checkpoint.
- [ ] Present complete world/branding review packet for human acceptance, with precise open decisions.
- [ ] Advance remaining asset phases only as dependencies and named human gates permit.
- [ ] Present complete 2E pack; obtain explicit acceptance and CNT-01 Phase 3 authorization.
- [ ] Coordinate individually demonstrated native phases and physical-device/family evidence through Phase 5.

### Pre-execution check-in
The user's submitted master prompt authorizes sessions/worktrees, local checkpoints, integration and verification. Execute the saved scope without repeated routine permission. Four world/branding requirements are the first bounded production phase. Provider/voice/name/device/rights decisions remain open; native Phase 3 is not authorized yet.

### Review
Startup verified; see [startup review](../docs/orchestration/2026-10-04-startup-review.md). Exact Astra/Sol models and both active isolated sessions are confirmed. 12 selected image hashes match; 373 protected files remain unchanged. Voice preflight has ten matching requests and no recordings. App-level worker permissions currently pause the optional world back-message and audition Git staging; user action requested with exact reasons. Neither phase is accepted and native execution remains gated.

## 2026-10-04 — GitHub synchronization and engineering readiness audit

User now explicitly authorizes pushing all work to `dsamin/MathBuddy`, superseding the earlier no-push restriction for this synchronization. Production review, native execution, deployment and publication gates remain unchanged.

- [x] Inspect integration and both isolated phase worktrees; confirm workers are idle/interrupted before checkpointing.
- [x] Scan all existing Git history for secrets (9 commits, zero findings).
- [x] Preserve and checkpoint interrupted world sources and independent audition preflight on separate phase branches; do not imply human acceptance.
- [x] Update master tracker with accurate interrupted status and backup commits.
- [x] Push current main/integration and phase branches; verify remote SHAs and clean worktrees.
- [x] Complete a read-only engineering/iPad readiness audit and report remaining blockers.

### Pre-execution check-in
The remote is empty. Publish the current coordinated baseline on main and preserve partial phase work on separately labeled branches. The read-only readiness review does not start native Phase 3 or run an unauthorized build.

### Review
World backup `35c121e` preserves three decoded original source images with matching hashes; audition backup `63ff847` verifies ten exact requests and zero recordings. Both phase diffs pass whitespace and secret checks. The engineering audit finds the reviewed pilot not ready for iPad installation or family testing; see [readiness report](../docs/orchestration/2026-10-04-engineering-readiness.md). Remote synchronization verified: main and orchestration at `5b74db1`, world backup `35c121e`, audition backup `63ff847`; all remote heads matched and all three worktrees were clean. GitHub default branch is main. All 373 protected file hashes remain unchanged. The original bounded Sol world session has resumed; new production work follows this backup. No native implementation/build or device installation was performed.
