# M01 — provisional pickup / return / settle study

Phase 1 comparison sample · October 3, 2026 · **Pending human review.**

This is a silent, direction-neutral motion schematic for Pip's Picnic. It is neither a selected illustration pack nor an implementation of the native iPad app. No existing experimental image, recording or app code was imported. The exact same scenario is used for normal and Reduced Motion.

- [Normal motion MP4](pickup-return-settle.mp4) · [GIF preview](pickup-return-settle.gif)
- [Reduced Motion MP4](reduced-motion.mp4) · [GIF preview](reduced-motion.gif)
- [Beginning / placed / returned contact sheet](storyboard-contact-sheet.png)
- [Reduced Motion contact sheet](reduced-motion-contact-sheet.png)
- [Actual decoded movie key frames](../review/decoded-key-frames.png)
- [Storyboard PDF](storyboard.pdf) · [actual PDF page preview](../review/pdf-pages/M01.png)
- [Motion and layer contract](brief.json) · [editable layer map](scene-layers.svg)
- [Normal timeline data](pickup-return-settle-timeline.json) · [Reduced Motion timeline data](reduced-motion-timeline.json)

The given target remains three berries in a separate, noninteractive reference card. There are five working berries. At 0.72 seconds, `CNT-01-piece-03` is moved from tray slot-03 to basket slot-01. At 2.88 seconds it returns to its original tray slot-03. The other four occurrences never move. The study deliberately ends with an empty basket and does not submit or complete the activity.

Normal motion uses 360 milliseconds of travel and 140 milliseconds of settle. Reduced Motion changes position immediately, keeps scale fixed at 1.0 and uses at most 120 milliseconds of a static outline. Both clips are 4.8 seconds, 1440 × 1080 pixels, 30 frames per second and contain no audio. The GIF previews are 960 × 720 pixels at approximately 15 frames per second and loop only as adult review conveniences. A future app must use the brief's per-action repeat limits, never this preview loop.

The ground, containers, target reference and stable occurrences are represented as editable named groups in `scene-layers.svg`. The Python renderer is the authoritative source for the detailed berry drawing, timeline, storyboards and encoded studies. The SVG is a schematic layer map; it does not constitute the final transparent layer exports.

Reproduce from the repository root with:

```sh
python3 scripts/phase1-motion-study.py
```

Authoring dependencies: Pillow, NumPy, SciPy, ffmpeg and ffprobe. `pdftoppm` renders the actual PDF previews; `pypdf`, when installed, measures their page counts. Arial is rasterized from the local OS for adult review annotations; no font file is bundled or selected as app typography. These are tooling dependencies, not app runtime dependencies.

Read [technical measurements](../review/technical-measurements.json) and [technical review notes](../review/technical-review.md) separately from [pending human decisions](../review/human-review.json). No technical result approves art, motion comfort, child usability or future native behavior.
