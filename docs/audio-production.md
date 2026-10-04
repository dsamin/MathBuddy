# Offline narration and effects

> **Unapproved experimental recordings.** Provider and voice names below are provenance, not a MathBuddy selection or listening approval. Future work follows the audition and script review in the [asset plan](asset-plan.md). Do not run generation as part of the current planning task.

The native pilot contains 19 authored narration clips and three original synthesized chimes in `MathBuddy/Resources/Audio`. The spoken lines use Google Cloud Text-to-Speech, `gemini-2.5-pro-tts`, Fenrir, en-US, with a warm, calm adult direction consistent with the sibling project’s production approach. These are generated draft takes, awaiting human listening approval.

`assets/audio/requests/` contains the exact text and delivery direction. `assets/audio/masters/` preserves the original WAVs and provenance metadata. `assets/audio/manifest.json` records duration, hashes and review status. The single recorded recovery pass completed seven missing takes; no unbounded or automatic paid retry is enabled.

Every file was validated as nonempty 24 kHz mono 16-bit PCM, and narration bundle hashes match the masters. Format and file coverage checks do not establish pronunciation, prosody or child suitability. Review all takes before a family release. Number-word clips and count-four are supplied for upcoming variants; the current native touch-to-count interaction uses a gentle pickup cue.

The app plays only local files using AVAudioPlayer. It stops prior narration before a new instruction and stops audio on backgrounding and audio interruptions. It contains no provider SDK, account credential, speech synthesizer or production network request. A missing-file/playback notice remains separate from the math state.

## Regeneration

Use a local Python environment with `google-cloud-texttospeech` installed and set `GOOGLE_APPLICATION_CREDENTIALS` to your local service-account file outside the repository. Optionally set `MATHBUDDY_VOICE_PYTHON` to that Python executable. Never commit credentials. The one-clip producer accepts a request JSON and a new output WAV path and refuses to overwrite an existing take.

```sh
python scripts/generate_voice_clip.py assets/audio/requests/welcome.json /tmp/mathbuddy-welcome-new-take.wav
```

`produce-pilot-audio.py` checks existing masters and bundles them. It does not silently retry a recorded failed generation. The effects are original mathematical tone synthesis with no third-party samples.
