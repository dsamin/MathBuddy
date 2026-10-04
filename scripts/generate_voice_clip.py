#!/usr/bin/env python3
"""Produce one draft Google voice clip locally; never ships in the iPad app."""
import argparse
import hashlib
import importlib.metadata
import io
import json
import os
from pathlib import Path
import sys
import wave
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path, help="JSON with text, prompt, model, voice, language")
    parser.add_argument("output", type=Path, help="New WAV file; existing files are preserved")
    args = parser.parse_args()
    output = args.output.resolve()
    sidecar = output.with_suffix(".json")
    if output.exists() or sidecar.exists():
        parser.error("Output already exists; choose a new take filename.")
    request = json.loads(args.request.read_text())
    for key in ("text", "prompt", "model", "voice", "language"):
        if not isinstance(request.get(key), str) or not request[key].strip():
            parser.error(f"Missing or invalid {key}.")
    credential = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not credential:
        env_file = ROOT / ".env.local"
        if env_file.is_file():
            for line in env_file.read_text().splitlines():
                if line.startswith("GOOGLE_APPLICATION_CREDENTIALS="):
                    credential = line.partition("=")[2].strip()
    if not credential:
        parser.error("Set GOOGLE_APPLICATION_CREDENTIALS in the environment or local .env.local.")
    credential_path = Path(credential).expanduser()
    if not credential_path.is_absolute():
        credential_path = ROOT / credential_path
    if not credential_path.is_file():
        parser.error("The configured service-account file is unavailable.")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(credential_path)
    try:
        from google.cloud import texttospeech
    except ImportError:
        parser.error("Install google-cloud-texttospeech in a local Python environment; see docs/audio-production.md.")
    try:
        client = texttospeech.TextToSpeechClient(
            client_options={"api_endpoint": "texttospeech.googleapis.com"}
        )
        result = client.synthesize_speech(
            input=texttospeech.SynthesisInput(text=request["text"], prompt=request["prompt"]),
            voice=texttospeech.VoiceSelectionParams(
                language_code=request["language"], name=request["voice"], model_name=request["model"]
            ),
            audio_config=texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16, sample_rate_hertz=24000
            ),
            retry=None,
            timeout=60,
        )
    except Exception as exc:
        # Provider/auth exceptions can include account details; report only the category.
        print(f"Google synthesis failed ({type(exc).__name__}); no audio approval recorded.", file=sys.stderr)
        return 1
    data = result.audio_content
    with wave.open(io.BytesIO(data), "rb") as wav:
        channels, width, rate, frames = wav.getnchannels(), wav.getsampwidth(), wav.getframerate(), wav.getnframes()
        if (channels, width, rate) != (1, 2, 24000) or frames == 0:
            raise ValueError("Unexpected or empty WAV response; no clip saved.")
    output.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "provider": "Google Cloud Text-to-Speech",
        "endpoint": "texttospeech.googleapis.com",
        "sdkVersion": importlib.metadata.version("google-cloud-texttospeech"),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "request": request,
        "sampleRate": rate, "channels": channels, "bitsPerSample": width * 8,
        "durationSeconds": round(frames / rate, 3),
        "sha256": hashlib.sha256(data).hexdigest(),
        "processing": "Original Google WAV; no silence trimming, tempo change or upsampling",
        "reviewStatus": "unreviewed", "listeningReview": None, "phonicsReview": None,
        "licenseReview": None, "disclosure": "AI-generated narration using Google Text-to-Speech",
    }
    with output.open("xb") as f:
        f.write(data)
    with sidecar.open("x") as f:
        json.dump(metadata, f, indent=2)
        f.write("\n")
    print(json.dumps({"output": str(output), "durationSeconds": metadata["durationSeconds"], "reviewStatus": "unreviewed"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
