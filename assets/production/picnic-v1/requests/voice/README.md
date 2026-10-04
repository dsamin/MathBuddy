# Phase 1 voice audition requests — recordings missing

**Pending human review. This package contains ten generation requests and zero recordings.** Cedar and Marin are provisional built-in OpenAI candidates. Neither has been heard or selected for MathBuddy. All wording, listening, candidate, provider and rights decisions remain pending. No production voice library is authorized by these requests.

The same five exact catalog lines are used for each candidate. Each take receives the same natural adult guide instructions, `gpt-4o-mini-tts-2025-12-15`, `en-US` pronunciation direction, speed `1.0` and WAV request. `en-US` is recorded as language metadata and in the instructions; it is not a separate unsupported API parameter. The provider's original WAV is to be preserved even if its channel, bit-depth or sample-rate format differs from the catalog's proposed master format. No finishing, selected export, loudness target or quality approval is claimed here.

- [Exact five-script snapshot](catalog-audition-snapshot.json) preserves the complete selected script records and the source catalog SHA-256.
- [Request manifest](request-manifest.json) lists all ten take IDs, request paths and hashes.
- Each `p1-<voice>-<script-ID>-t01.request.json` preserves exact input, provider settings, CLI job, expected future output, empty generation history and pending reviews.
- [Adult listening index](../../review/listening/index.html), [playlist](../../review/listening/playlist.json) and [worksheet](../../review/listening/adult-listening-worksheet.csv) explicitly mark all ten recordings missing.
- [Capability report](../../metadata/voice-capability.json) records the generation gap and technical request checks. The dry-run log validates request handling only; it contains no audio.

## Generation gap

`OPENAI_API_KEY` is unavailable. The OpenAI Python package is available, but a live request needs a locally configured key. Alternate Google credentials and `google.genai` are also unavailable. No credentials were obtained from another project, no secret values were read or saved, no provider call was made, and no system-voice substitute was generated.

If the user chooses OpenAI for these auditions, create/set `OPENAI_API_KEY` locally using the [OpenAI key page](https://platform.openai.com/api-keys); never paste the key into chat or a project file. Estimate the requested run's cost and review provider terms/rights before a requested run. Neither voice quality nor MathBuddy rights can be inherited from another app. A different user-selected authorized provider would need equivalent preserved exact requests.

## Reproducible bundled CLI workflow

The following commands are to be run from the MathBuddy project root **after the user chooses the generation provider and the live capability is available**. The speech skill's bundled CLI makes all provider calls; the small conversion only creates its temporary batch input. It does not generate speech.

```sh
mkdir -p tmp/speech
python3 - <<'PY'
import json
from pathlib import Path
request_dir = Path('assets/production/picnic-v1/requests/voice')
manifest = json.loads((request_dir / 'request-manifest.json').read_text())
batch_path = Path('tmp/speech/mathbuddy-phase1-voice.jsonl')
with batch_path.open('w') as batch:
    for item in manifest['requests']:
        request = json.loads(Path(item['request_path']).read_text())
        batch.write(json.dumps(request['cli_job'], ensure_ascii=False) + '\n')
PY

MATHBUDDY_TTS_CLI="$HOME/.codex/skills/speech/scripts/text_to_speech.py"
python3 "$MATHBUDDY_TTS_CLI" speak-batch \
  --input tmp/speech/mathbuddy-phase1-voice.jsonl \
  --out-dir assets/production/picnic-v1/masters/audio/en-US \
  --rpm 50 --dry-run
```

For a chosen live audition run, use the same bundled CLI command with `--dry-run` removed, then remove the temporary JSONL. Preserve the output at each request's `expected_master_path`. Record the actual generation time, provider/model/voice, original file measurements and SHA-256 in take provenance. Do not relabel a request as a generated take until the original audio exists and is inspected.

## Review after generation

First compare every recording's spoken words with its exact script, then perform adult listening review for natural guide delivery, pace, number pronunciation, unexpected speech/noise and clipping. Capture technical measurements separately. Keep rejected takes, identify a replacement with a new take ID, and rerun only the targeted replacement request. AI-generated voice disclosure is required when any generated audition is presented.

Selecting a candidate does not approve its individual takes, all 101 scripts, provider/rights, a production run or native implementation. Stop at the Phase 1 review checkpoint.
