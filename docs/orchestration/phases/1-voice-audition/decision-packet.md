# Voice audition preflight decision packet

Checked October 4, 2026 (America/Los_Angeles). **Preflight complete; provider unselected; zero recordings and zero synthesis/transcription calls.** No candidate has been heard or approved. This packet covers ten proposed requests only, not a production library.

## Exact proposed audition

| Script ID | Exact input (both candidates) |
| --- | --- |
| VO-WELCOME | Hello! Let’s get our picnic ready. |
| VO-COUNT-BERRY-03 | Put three berries in the basket. |
| VO-COUNT-TOO-MANY | There are too many. Tap a piece in the basket to give it back. |
| VO-JOIN-TOTAL | How many are on the shared mat? Choose a number. |
| VO-BYE | Bye for now. Your garden will be here. |

| Control | Cedar proposal | Marin proposal |
| --- | --- | --- |
| Provider | OpenAI Audio API | OpenAI Audio API |
| Exact model | gpt-4o-mini-tts-2025-12-15 | gpt-4o-mini-tts-2025-12-15 |
| Built-in voice ID | cedar | marin |
| Takes | Five, one per exact line | Five, one per exact line |
| Format / speed | WAV / 1.0 | WAV / 1.0 |
| Locale direction | en-US in metadata/instructions | en-US in metadata/instructions |
| Delivery controls | Identical instructions below | Identical instructions below |
| Heard quality / preference | Unknown; no recordings | Unknown; no recordings |

`en-US` is not a separate speech API parameter. Preserve curly apostrophe U+2019 in the welcome line. The exact shared instruction string is:

```text
Voice Affect: Natural adult guide; warm and composed.
Tone: Matter-of-fact, patient and friendly.
Pacing: Unhurried and clear; no singsong counting.
Pronunciation: Enunciate number words clearly in natural US English.
Delivery: Speak only the exact input text; add no speech, laughter or sound effects.
```

The complete hash list and absent expected output paths are in [request-audit.json](request-audit.json). Catalog SHA-256: `eb7bb074d6356bd19609cd37e33578b1b3f78636f4651cf353e3e9224deb32ee`; snapshot: `f33cbc015cd528f5b1d67f691eeda8aead961d4ae6ddacde04da73489da727ef`; manifest: `53c93d751ae263b3f00caf3cbb17b35917a5c83d857d28776c449f4f8453ae5a`. All ten request byte hashes match the manifest; all five complete snapshot records match the catalog; exact input, CLI fields and shared controls match. All ten expected WAV masters are absent. The old request/status/listening artifacts remain unchanged as history.

## Official availability and price evidence

All sources accessed October 4, 2026; model/deprecation/terms pages rechecked on reconciliation with checkpoint `63ff8475458ff8666dba26769c14eee9f8a6337e`. These are public documentation checks, **not authenticated account-access or endpoint-success checks**.

- [Model page](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts): exact dated snapshot listed, marked deprecated; published rates are $0.60 per million input text tokens and $12 per million output audio tokens. Free tier is unsupported.
- [Deprecations](https://developers.openai.com/api/docs/deprecations): October 1 notice schedules this exact snapshot's shutdown for January 6, 2027. The recommended replacement is `gpt-realtime-2.1-mini`; it is not selected here. A delayed audition must recheck availability. No automatic migration or alias substitution is authorized.
- [Speech API reference](https://developers.openai.com/api/reference/cli/resources/audio/subresources/speech/methods/create): exact snapshot, Cedar and Marin, instructions, WAV and speed 1.0 are documented. Input limit is 4,096 characters.
- [TTS guide](https://developers.openai.com/api/docs/guides/text-to-speech): Cedar/Marin are recommended for quality, voices optimized for English. Formats include MP3, Opus, AAC, FLAC, WAV and PCM. It requires clear AI-voice disclosure to end users. These facts do not establish which candidate suits MathBuddy.
- [Current pricing page](https://developers.openai.com/api/docs/pricing): its visible generation table emphasizes newer realtime models and omits this legacy TTS row. The exact model page supplies the legacy rate above; recheck billing before execution. Mini transcription is listed at approximately $0.003/minute.

**Estimate, not a quote or spending approval:** ten inputs contain 428 Unicode characters / 88 words, plus ten copies of the 302-character instruction string. At an assumed 100–150 words/minute plus 10–20 seconds of pauses across the ten takes, output might total roughly 45–73 seconds. There is no actual duration or exact token count yet; no tokenizer is installed. Do not price WAV bytes or characters as audio tokens.

Token-based scenario for all ten requests together: assume 1,000 input tokens including instructions and 1,000–5,000 output audio tokens. Cost = `0.60 × input_tokens / 1,000,000 + 12 × audio_tokens / 1,000,000`, or **$0.0126–$0.0606 USD**. This is a deliberately broad planning scenario, not a verified token-duration conversion; output tokens could exceed it. At 45–73 seconds, optional mini transcription adds about **$0.0023–$0.0037**, excluding minimum billing, taxes and retries. Proposed human-selected budget ceiling: **$0.10 for one ten-take pass plus one transcription per take**, no paid reruns. The CLI does not enforce a dollar cap. Its bundled client uses `OpenAI()` with SDK-default automatic retries (installed SDK 2.24.0: two retries); the CLI also has an attempt loop. `--attempts 1` alone does not disable SDK retries. Therefore a strict one-request/no-retry ceiling is currently an execution capability gap, not an enforced guarantee. Before calls, the master must resolve this through an explicitly approved skill-compatible retry control, or obtain human acceptance of retry exposure and a revised estimate. Do not modify the bundled CLI or create a replacement runner silently. Exact charges require provider usage/billing evidence. No cost incurred by audio generation/transcription in this session. Research/session costs are outside this estimate.

## Rights facts and separate human acceptance

[Services Agreement](https://openai.com/policies/services-agreement/), sections 4.1–4.4: customer retains input rights and receives OpenAI's output rights to the extent permitted by law; customer is responsible for input permissions and output suitability; output need not be unique. Content is not used to improve services unless the customer explicitly agrees. Check the actual account/order terms at the generation boundary.

[Service Terms](https://openai.com/policies/service-terms/), section 8: the noncommercial/standalone redistribution restriction concerns **ChatGPT Voice Output**. Proposed requests use the Audio API, not captured ChatGPT conversation audio. My reading is that this ChatGPT-specific restriction does not itself forbid bundling API-produced WAVs in MathBuddy; this is an interpretation, not legal advice, clearance, copyright assurance or human rights acceptance. Provider terms and AI disclosure still apply. No voice cloning, real-person likeness, third-party recording or child recording is proposed.

The human must separately accept the provider terms/rights basis for the audition and intended eventual bundled offline use. Choosing the audition provider does not approve production reuse, final voice, wording, every take, or distribution. Prompt 3's embedded authorization is only a future template.

## Local credential and inspection capability

Safe presence checks: `OPENAI_API_KEY` absent; `GOOGLE_APPLICATION_CREDENTIALS` absent; workspace `.env` and `.env.local` absent. No credential values printed/saved, no sibling-project files inspected, no setup performed. Presence would not prove validity, funds or permissions. OpenAI Python SDK available; Google genai SDK unavailable. No alternate provider was chosen or surveyed as an implicit substitute.

Python 3.11, NumPy, ffmpeg, ffprobe and afplay are present. ffmpeg's installed filter inventory contains `astats`, `silencedetect`, `volumedetect`, `ebur128` and `showwavespic`. Matplotlib, soundfile, tiktoken and local Whisper packages are absent; ffmpeg plus Python's wave/NumPy can cover file inspection and waveform export without them. These are inventory checks only: no actual audition file exists to decode or measure, and no playback has been tested.

**Listening gap:** this text session has no demonstrated local-audio hearing input for the agent. `afplay` or a browser player can let a human hear a take, but playback success does not prove the agent listened. API transcription is available in principle through the skill CLI, requires the selected credential/provider decision, and has not run. Local offline ASR is unavailable in the checked interpreter. Thus agent wording comparison can use authorized transcripts; every-take literal listening must be performed and recorded by a human, or a separately demonstrated audio-input capability must be established. Do not label transcript agreement as listening approval.

## Every-take inspection plan after authorization

1. Reverify hashes immediately before running. Use bundled `/Users/devan/.codex/skills/speech/scripts/text_to_speech.py` and OpenAI SDK only if the exact proposed provider/settings are selected. Prepare temporary JSONL from the immutable `cli_job` records; override only output paths to new audition take locations. Dry-run and verify payload equality. Originals, old missing-output records and rejected history stay intact. No silent substitutions or paid retries. If the exact model fails, preserve error and stop.
2. Save each provider original, SHA-256, request hash, selected decision reference, provider/model/voice, UTC timestamp, output path and sanitized result/error. Never save authorization headers or key values. New outputs go under `masters/audio/en-US/<script-ID>/` using distinct audition IDs; provenance under new `metadata/audition-*` paths. Confirm actual format rather than forcing proposed PCM16/24kHz onto the original.
3. For **each of ten actual outputs**, run ffprobe; fully decode using ffmpeg to a null sink; record codec, channels, sample rate, sample format, frames and duration. Save per-take `astats`/`volumedetect`/`ebur128` results and waveform PNG. Use `silencedetect=noise=-50dB:d=0.1` as a screening parameter and distinguish leading/trailing from internal pauses. Count samples near full scale on decoded PCM for clipping screening. A zero duration, decode error, long silent output, flat top or abrupt end triggers review, never automatic repair/acceptance. LUFS on tiny clips may be unreliable. Threshold flags are triage, not quality approval.
4. Transcribe **each actual WAV individually**, only if authorized, through `/Users/devan/.codex/skills/transcribe/scripts/transcribe_diarize.py` using the explicitly chosen model (skill default proposal: `gpt-4o-mini-transcribe`, deprecated with February 26, 2027 shutdown). Do not feed the expected wording as an ASR prompt. Preserve raw transcript, compare to exact requested words, and mark additions, omissions and uncertain number words. ASR cannot prove acoustic quality or exact punctuation; request text never counts as spoken evidence.
5. Build the adult comparison player in `review/listening/audition-v2/` with explicit “AI-generated voice” disclosure, exact request text, waveform/metrics/transcript links and unscored review fields. A human listens to **every** take for wording, number clarity, pacing, warmth, artifacts and suitability. Record take IDs and reviewer/date/outcome; unresolved hearing or ASR gaps remain explicit. Stop for separate voice, wording, individual-take, reuse and listening approvals. No bulk narration, effects or app integration.

## Decisions the master must forward before live requests

- Select a provider. If OpenAI is selected, explicitly select the exact deprecated snapshot and Cedar/Marin comparison, or request a separately reviewed replacement packet. Another provider requires new equivalent requests and cost/rights/capability review before calls.
- Accept or decline the rights/terms basis and required AI disclosure for audition and intended eventual offline bundling, with production reuse still pending.
- Approve these exact five Unicode lines, shared instructions, speed 1.0, WAV and ten-request scope; select a spend ceiling and retry policy, including the unresolved SDK retry control noted above.
- Decide the credential route (no local OpenAI key currently found). Any secure provisioning/local write requires a confirmed destination and explicit authorization; never paste a key in chat.
- Choose transcript inspection provider/model and permission to submit each generated take; confirm a human will listen to every take or establish actual agent hearing capability. Generation approval alone is not transcription approval.

No redundant permission question is being sent now: the completed packet goes to the master for the required human decision. Shared catalog, decisions, trackers, art and native code remain untouched.
