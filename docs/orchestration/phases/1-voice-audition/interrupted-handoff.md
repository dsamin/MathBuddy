# Independent audition preflight checkpoint

## Context
The user requested backup of all current work. This interrupted session prepared a decision packet; it did not synthesize an audition or select a provider or voice. The master checkpointed the existing preflight after verifying all ten exact requests and absent recordings.

## Codebase Overview
The isolated Sol phase is based on 9ae9b6370a52e0c5dbac0d17e84911bce7213c33. This directory owns the preflight, capability evidence and offline verifier. The master owns the tracker and human decision routing.

## Tasks
Present the complete preflight decision packet. Obtain the required provider, model, rights and cost decisions through the master before live requests. Preserve exact scripts, settings and provenance. Then produce five lines for each of two explicitly chosen voices, technically verify ten recordings and obtain individual listening decisions. Do not silently substitute candidates or treat preparation as a completed audition.

## File Locations
- `docs/orchestration/phases/1-voice-audition/decision-packet.md`
- `docs/orchestration/phases/1-voice-audition/capability-check.json`
- `docs/orchestration/phases/1-voice-audition/request-audit.json`
- `docs/orchestration/phases/1-voice-audition/verify-preflight.py`
- `assets/production/picnic-v1/requests/voice/request-manifest.json`

## Acceptance Criteria
The offline verifier passes five complete source records, ten exact request hashes/settings and ten absent masters. Zero provider calls and zero recordings. Preflight-only status remains explicit; voice, wording, rights and reuse remain pending. The full audition is incomplete.
