# Pilot startup verification

## Context

The user's full-pilot orchestration request is active. Current execution is remaining Phase 2A plus independent voice-audition preflight. Native Phase 3, later dependent phases and all product review gates remain unadvanced.

## Codebase Overview

Integration checkout: `/Users/devan/Projects/MathBuddy`, branch `orchestration/mathbuddy-pilot`. Starting reviewed HEAD: `608e5b9`. Approved input checkpoint: `e48eb490711d9754b6b6e123f1e069aebfeae3d7`; audition brief checkpoint: `9ae9b6370a52e0c5dbac0d17e84911bce7213c33`; active-session tracker checkpoint: `885197b`.

Local session `turn_context` metadata independently confirms this master uses `gpt-6-astra` and both bounded worker sessions use `gpt-6.1-sol`. No model or permission settings were changed.

## Tasks

- Verified SHA-256 for five selected Pip exports, five originals, the pose sheet and Direction B board: 12/12 match.
- Reconciled live catalog identity/art fields with the recorded human selection. Preserved generation-time pending labels, provider originals, recipes, technical limitations, content/rights gates and the unapproved native experiment.
- Created master plan, 16-row phase tracker, protected baseline snapshot and two bounded five-section phase briefs before creating dependent worktrees.
- `git diff --check` and staged `gitleaks git --pre-commit --staged --redact --no-banner` passed for each master checkpoint. Initial generic-key finding was the SHA-256 value keyed by a secret-scan filename; changing evidence to explicit path/hash fields removed the false positive without suppressing the rule.
- Read-only SHA-256 comparison confirms 373 protected baseline files unchanged.
- Partitioned live narration IDs into 35/23/24/19 disjoint mappings, all 101 accounted for. Conditional missing counts are 31/22/24/19 only if the five relevant audition takes are individually accepted for reuse. This is planning only.
- Confirmed workers via `read_thread`. `list_threads` omitted new tasks; read-only app lifecycle logs resolved pending creation IDs to real thread IDs. No duplicate sessions were created.

## File Locations

| Session | Verified model | Thread | Worktree | State |
|---|---|---|---|---|
| MathBuddy Phase 2A World and Branding | gpt-6.1-sol | `01a10777-964b-7380-ad50-122d3de368d8` | `/Users/devan/.codex/worktrees/8899/MathBuddy` | Production started; optional progress-message tool awaiting app approval |
| MathBuddy Independent Voice Audition | gpt-6.1-sol | `01a10778-c025-7b13-99a6-a1886b801260` | `/Users/devan/.codex/worktrees/4c83/MathBuddy` | Preflight packet written; Git staging awaiting app approval |

The voice candidate packet is at `docs/orchestration/phases/1-voice-audition/decision-packet.md` in its worker worktree. Master read-only verification confirmed all ten request byte hashes and exact catalog inputs, with all ten expected recordings absent. No live synthesis/transcription or listening success is claimed. The worker still owes its checkpoint and final handoff.

Master also opened current official [model pricing](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts), [deprecations](https://developers.openai.com/api/docs/deprecations), [Services Agreement](https://openai.com/policies/services-agreement/) and [Service Terms](https://openai.com/policies/service-terms/) on October 4. The prepared dated TTS model remains listed but is deprecated with January 6, 2027 shutdown; no replacement was selected. Packet costs are explicitly token-scenario estimates, not a measured bill or guaranteed spending limit. Credential absence and every-take listening capability gaps are explicit. Human provider/rights choices remain pending.

## Acceptance Criteria

Startup sequencing, approved-input checkpointing, exact model/session creation and original preservation are verified. **Neither Phase 2A nor the audition is complete or human-accepted.** No phase output commit has been integrated yet.

Both new tasks inherited `on-request` approval and workspace-write sandbox policies. The master has a different permission profile. No setting change or bypass was attempted. Required app actions were presented to the user: dismiss the optional Phase 2A back-message (the master polls directly), and approve the audition task's explicit `git add` request because its shared Git index is outside its writable worktree. These are app permission gates, not renewed production-scope requests and not automatic-review rejections.

After those requests are resolved, resume the existing sessions; do not create replacements. Verify the returned full world packet and audition handoff, then present the relevant human decisions. Do not start 2B until the 2A world/composition review is accepted. Do not run native code/builds before complete 2E pack acceptance, explicit Phase 3 authorization and device/OS/adult-gate decisions. No Pebble change, Phase 6, push, publication or deployment occurred.
