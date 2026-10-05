# Voice audition preflight handoff

## Context

Prepared checkpoint `63ff8475458ff8666dba26769c14eee9f8a6337e` is verified in the existing isolated worktree. Original base is `9ae9b6370a52e0c5dbac0d17e84911bce7213c33`. This reconciliation refreshes preflight evidence and completes the durable handoff. Provider/model/voice/wording/rights/spend choices remain open. Zero recordings and zero synthesis/transcription calls; no credential setup. The audition itself remains incomplete. Return in this session; do not message unrelated chats.

## Codebase Overview

Eventual native SwiftUI app bundles offline audio; the adult review player belongs outside it. Five lines × Cedar/Marin produce ten immutable proposed OpenAI requests with dated model `gpt-4o-mini-tts-2025-12-15`, WAV, speed 1.0 and identical instructions. Complete hashes, exact Unicode lines and absent paths are in `request-audit.json`. Read the active `brief.md`, not Prompt 3's future authorization template. Master owns tracker/tasks/canonical catalog/decisions; this phase writes only its own directory during preflight.

## Tasks

Preparation finished: current official sources, transparent cost scenarios, rights facts versus interpretation, safe credential presence checks, exact request verification and per-take inspection plan. Reconciliation adds a concrete retry limitation: bundled speech CLI `OpenAI()` inherits SDK automatic retries; `--attempts 1` does not enforce zero retries. No workaround was implemented.

Master must forward the human's provider/exact-model/voices/settings/wording selection, rights acceptance, spend/retry policy, credential route and separate transcription permission/model. Human every-take listening is required unless actual agent audio hearing is demonstrated. Then selected execution can preserve originals/provenance, inspect/transcribe ten takes, build a disclosed adult comparison player and stop for separate voice/wording/take/reuse/listening decisions. No bulk narration, app work, art, effects, Pebble, push, publish or deploy.

## File Locations

Worktree: `/Users/devan/.codex/worktrees/4c83/MathBuddy` on `codex/phase-1-voice-audition-wip` (initially detached). All reconciliation edits are inside `/Users/devan/.codex/worktrees/4c83/MathBuddy/docs/orchestration/phases/1-voice-audition/`:

- `decision-packet.md`: five exact lines, unchanged candidate controls, official source links accessed/rechecked October 4, rates/estimates/rights and human decisions; added retry gap.
- `capability-check.json`: refreshed presence-only check and SDK retry evidence; no secrets.
- `plan.md`: bounded checklist and reconciliation review.
- `handoff.md`: this five-section durable handoff.

Retained unchanged phase files: `brief.md`, `interrupted-handoff.md`, `request-audit.json`, `verify-preflight.py`. Read-only manifest: `/Users/devan/.codex/worktrees/4c83/MathBuddy/assets/production/picnic-v1/requests/voice/request-manifest.json`. No sample path exists because no take was produced. Future allowed paths are defined by the active brief. Replacement coordinator handoff was not found in this isolated checkout; no sibling checkout was searched or modified.

## Acceptance Criteria

Commands/results on October 4:

- `git show --stat 63ff847`: prepared checkpoint present, six phase files only, author Devan.
- `python3 docs/orchestration/phases/1-voice-audition/verify-preflight.py`: PASS, five complete catalog records, ten exact request byte hashes/settings, ten absent WAV masters, zero calls. Report remains unchanged.
- `git diff --check`: exit 0.
- `gitleaks git --log-opts=63ff847^..63ff847 --redact --no-banner`: exit 0; one commit, 27.01 KB, no leaks.
- Installed SDK signature inspection: OpenAI 2.24.0, `max_retries` default 2. Local CLI source inspection shows `OpenAI()` and a separate attempt loop; no provider initialization/call.
- `git diff --cached --check`: exit 0; `gitleaks git --pre-commit --staged --redact --no-banner`: exit 0, 7.72 KB scanned, no leaks. Full phase directory scan also passed, 38.69 KB and no leaks. Exact resulting commit is reported in the session final and can be resolved with `git log -1 --format=%H` when this handoff is the tip.

Catalog SHA-256: `eb7bb074d6356bd19609cd37e33578b1b3f78636f4651cf353e3e9224deb32ee`; snapshot: `f33cbc015cd528f5b1d67f691eeda8aead961d4ae6ddacde04da73489da727ef`; manifest: `53c93d751ae263b3f00caf3cbb17b35917a5c83d857d28776c449f4f8453ae5a`. All ten request hashes are preserved in `request-audit.json`.

Limitations: exact model deprecated, shutdown January 6, 2027 per official deprecation page; no authenticated availability test; credential absent; no demonstrated agent hearing, local ASR or actual take inspection; no enforced dollar/no-retry cap. Cost scenario $0.0126–$0.0606 synthesis plus estimated $0.0023–$0.0037 transcription is assumption-based and excludes retries/taxes, not a quote or approval. Sources and calculations are in the packet. These gaps are human decision inputs; preparation is not voice, wording, rights, listening or production reuse approval.
