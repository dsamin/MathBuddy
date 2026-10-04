# Phase 1 motion — technical findings

October 3, 2026 · Seven provisional motion/layer briefs · **Human review remains pending.**

The review inspected actual PDF pages and key frames decoded from both encoded MP4 files. It also measures all decoded frames using a controlled red-berry connected-component check. The full results are preserved in `technical-measurements.json`; this review is distinct from art, listening, child-use or native implementation acceptance.

## Concrete outputs inspected

- `M01…M07/brief.json`: seven exact register IDs and names, with triggers, named layers/z order, pivot coordinate contracts, start/middle/end states, durations, bounded repeat policy, rapid-input/interrupt behavior, Reduced Motion, sound cues and semantic ownership exclusions. All dependency IDs resolve to the existing register.
- `M01…M07/storyboard.pdf`: seven one-page, beginning/middle/end PDFs. Each actual PDF is decoded to `review/pdf-pages/M01…M07.png`; the combined preview is `all-storyboards-pdf-preview.png`.
- `M01/pickup-return-settle.mp4` and `M01/reduced-motion.mp4`: 1440 × 1080, 144 decoded frames, 30 fps, 4.8 seconds, no audio streams. Preview GIFs and editable timeline data are also preserved.
- `review/decoded-key-frames.png`: normal and Reduced Motion frames decoded at 0.00, 0.90, 1.13, 1.50, 3.00, 3.40 and 4.00 seconds.
- `M01/scene-layers.svg` and `scripts/phase1-motion-study.py`: editable schematic layer map and deterministic rendering source. No unapproved experiment was selected.

## Findings

The counting study retains a framed target model of three and five working occurrences. Piece-03 moves once to basket slot-01 and returns to tray slot-03. Its ID persists; no source/destination clone or fading fruit trail is rendered. The basket rim lies below every full fruit silhouette. The geometry data finds at least 70.04 pixels of conservative separation between working silhouettes, 51 pixels of clearance above the basket front and 12.91 pixels of clearance below the target card during normal travel. These measurements describe the 1440 × 1080 schematic, not physical iPad touch sizes.

All 144 actual decoded frames in each MP4 contain three reference-berry components and five working-berry components; minimum and maximum counts are identical across the clips. Identity and original-return-slot conservation are checked against the editable frame data; visual color components alone cannot establish occurrence identity. The reference is consistently labelled as given and noninteractive. The adult annotations and ID data are production review aids, not a proposed child-facing implementation.

The M02 storyboard shows two plus one as separate identities, joins them without an automatic total label, then restores their anchors through three returns/Undos. M03 shows a given transfer of two from five, leaves the assessed source remainder unlabelled, then restores the two transferred identities. M04 does not auto-place objects. M05 requires an explicit response before success presentation; celebration callbacks cannot record completion or grant a reward. M06 separates base/stem/rotor, defines a hub pivot and a bounded spin, and keeps bud/open as one flower identity. M07 uses aligned still-pose transitions with a direction-neutral rabbit proxy.

The Reduced Motion study has fixed scale and immediate accepted-action positions. The same target and five occurrences remain visible. There is no travel, spin, bounce, narration or semantic delay.

## Limits and next review

The seven JSON contracts specify future native semantics; they do not prove a native implementation exists or handles rapid input correctly. Only M01 has a timed study. Other motions have concrete static storyboards and proposed timings, with the final selected illustration pack, layer exports and exact production pivots still absent.

The supplied scene and PDF pages are flattened/vector schematics. The rabbit in M07 is a neutral motion proxy and must not become the selected Pip identity by accident. The two visual directions should be reviewed independently for character consistency. Actual-size iPad review, six occupied basket slots in each orientation, final layer alignment, child comprehension, motion comfort and human art approval remain future checks.

The source was refined during authoring to use the third berry's clear route, avoid target-card intersection and make multiple returns/Undos explicit. Earlier intermediate renders were not designated as selected assets. The final files in this checkpoint remain pending human review; there is no approved delivery manifest.
