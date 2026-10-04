# Phase 1 — creative-direction review checkpoint

October 3, 2026. Two concrete visual directions and the independent motion deliverables are ready for human review. The natural voice audition remains incomplete: all ten takes are missing because cloud speech credentials are unavailable. This checkpoint does not approve the identity, asset pack, implementation or next roadmap phase.

## Samples together

Open the [adult review gallery](../../assets/production/picnic-v1/review/index.html), or serve the sample package locally and visit `http://127.0.0.1:8873/review/index.html` while that server is running. [Package guide](../../assets/production/picnic-v1/README.md) provides exact source paths and review boundaries.

| Sample | Current pending review file |
|---|---|
| A — warm paper illustration | [Direction A take-02](../../assets/production/picnic-v1/masters/images/DIRECTION-A/take-02/board.png) |
| B — clean soft-shape storybook | [Direction B take-02](../../assets/production/picnic-v1/masters/images/DIRECTION-B/take-02/board.png) |
| Pickup / return / settle | [Normal MP4](../../assets/production/picnic-v1/motion/M01/pickup-return-settle.mp4) and [Reduced Motion MP4](../../assets/production/picnic-v1/motion/M01/reduced-motion.mp4) |
| Seven provisional motion/layer contracts | [Actual PDF previews](../../assets/production/picnic-v1/motion/review/all-storyboards-pdf-preview.png); each `motion/M01…M07/` contains `brief.json` and `storyboard.pdf` |
| Two-candidate voice comparison | [Listening sheet](../../assets/production/picnic-v1/review/listening/index.html); ten exact requests, zero recordings |

Both boards compare the same two Pip poses, count-three from five, landscape and portrait layouts, pinwheel/free flower/Finish garden, and static five-from-six stress inset. They are flattened 1536 × 1024 art sheets; the panels show reflow but are not measured native device layouts. No production layer pack is implied.

## Technical findings

- Independent inspection of original and revised boards counted five working berries and three reference berries in both count orientations; six working/five reference in the stress inset. Baskets are empty and separate; no working fruit silhouette is obscured.
- The framed miniature target and basket arrow give a sound-off set-construction goal. The target copies are not part of the working set. This does not establish numeral recognition or abstract recall.
- Pip’s face/body/cream fur/sage scarf remain consistent. The pleased pose bends one ear; this is an unresolved identity/pose choice. Replay’s circular arrow is ambiguous and needs a clearer playback glyph/label in a selected native design.
- Original white Finish text had weak sampled contrast. Take-02 uses dark lettering, approximately 6.3–6.5:1 on sampled glyph-core regions. Both original takes, exact prompts and immutable source hashes are retained. This is a raster sample measurement, not native accessibility certification.
- Both actual motion clips decode to 144 frames, 30 fps, 4.8 seconds, 1440 × 1080, silence. Actual decoded key frames and PDF pages were inspected. Five working IDs are conserved, the three-berry target remains separate, the same moved occurrence returns to its original slot, and Reduced Motion uses immediate positions with fixed scale.
- Seven provisional briefs cover named layers, pivots, occlusion, timing, finite repeats, rapid retargeting/interruption, silent resume, Reduced Motion and semantic-state ownership. A copied count-only orientation description was corrected per motion role before final checkpointing. The briefs specify behavior; rapid-input/native cancellation/portrait rotation have not been exercised in an app.
- All ten voice requests match the five original catalog texts exactly, including punctuation/Unicode. A bundled speech CLI dry-run parsed ten jobs with no provider calls. Exact requests and hashes are evidence about request preparation; actual audio wording, level and intelligibility cannot be checked because no audio exists.
- `python3 scripts/verify-phase1-samples.py` checks image/source/prompt hashes, actual image decoding, seven PDF/brief contracts, decoded movie dimensions/frames/silence, local gallery links, exact voice requests, pending decisions and baseline source boundaries. See the [file audit](../../assets/production/picnic-v1/metadata/file-audit.json).

The adult gallery was checked in the local browser at 1280 × 720: both 1536 × 1024 boards loaded and aligned; both 4.8-second videos loaded; no horizontal overflow. All 31 local HTML links resolve. This verifies the review viewer only.

Detailed findings: [independent visual review](../../assets/production/picnic-v1/review/contact-sheets/independent-visual-review.md), [motion review](../../assets/production/picnic-v1/motion/review/technical-review.md), [technical validation](../../assets/production/picnic-v1/metadata/validation.json).

## Human decisions and generation gap

Working recommendation: **B — clean soft shapes**, because the simpler scenery gives clearer separation around the math. A remains a viable paper-texture alternative. The next decision is to choose/revise the art direction and decide whether Pip’s ears can bend between poses.

Theme/rabbit appeal, art, actual-size object clarity, motion comfort, wording, voice/listening and provider/rights decisions remain pending in a [separate decision record](../../assets/production/picnic-v1/metadata/review-decisions.json). No human reviewer/date/selection was fabricated.

Natural audition capability: `OPENAI_API_KEY` is absent. Alternate Google credential configuration and SDK are unavailable. No credentials were obtained, no sibling credential store was inspected and no local synthetic stand-in was substituted. Cedar/Marin are proposed OpenAI candidates from the installed speech workflow, not selected voices. The user can choose/configure an authorized provider later; then produce and listen to the preserved five lines × two candidates before selecting a voice. All ten takes remain outstanding.

Final transparent/aligned poses, environment layers, basket front/back and toy pivots are future Phase 2 work after direction review. Native/device/assistive-use/audio cancellation and child observations remain future separately requested phases. No learning or usability efficacy is claimed.

## Checkpoints and scope evidence

Initial preservation commit: `18b36ed4e1ad7264520af349e6a55bb3b3daafe8`. No GitHub URL was supplied. The repository has no remote and no push was attempted. Existing meaningful work remains preserved; experiments retain their unapproved status. Small assets fit ordinary Git; oversized build caches and local credentials stay excluded.

Phase 1 deliverables are committed separately from that baseline. Both checkpoints are subject to whitespace and redacted staged secret scans. No attribution footer or contributor trailer is included. The final response supplies the second commit hash.

Baseline comparison confirms no change in `MathBuddy/`, `MathBuddy.xcodeproj/`, `project.yml`, existing `assets/audio/`, `mockups/` or experiment labels. No app build, native implementation, bulk pilot production, approved delivery manifest or Pebble change occurred. The 196 logical requirements, 24 variants and 101 scripts remain planning inventory.

Stop at this review checkpoint. Direction selection does not automatically begin Phase 2 or any native phase.
