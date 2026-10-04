# Native asset production

> **Unapproved experimental assets.** This records files already generated, not the approved art direction or complete pilot inventory. Use the [asset plan](asset-plan.md) for future review and production. No new generation is underway.

Generated on 2026-10-03 (America/Los_Angeles). These are original, generated artwork candidates for the native MathBuddy iPad vertical slice. They are bundled in the Xcode asset catalog; no remote image download, browser rendering, or runtime image generation is involved.

## Delivery status

| Asset | Workspace file | Dimensions | Format | Status |
|---|---|---|---|---|
| PipWelcome | `MathBuddy/Assets.xcassets/PipWelcome.imageset/PipWelcome.png` | 1024 × 1536 | RGBA PNG | Generated, visually inspected, alpha verified; ready for native prototype integration |
| PipHappy | `MathBuddy/Assets.xcassets/PipHappy.imageset/PipHappy.png` | 1024 × 1536 | RGBA PNG | Generated from PipWelcome as the identity reference; alpha verified; ready for prototype integration |
| GardenBackground | `MathBuddy/Assets.xcassets/GardenBackground.imageset/GardenBackground.png` | 1536 × 1024 | RGB PNG | Generated, visually inspected; ready for prototype integration |
| PipIconArtwork | `MathBuddy/Assets.xcassets/PipIconArtwork.imageset/PipIconArtwork.png` | 1254 × 1254 | RGB PNG | Generated mascot icon concept retained for art review; not assigned as the installed app icon |
| AppIcon | `MathBuddy/Assets.xcassets/AppIcon.appiconset/AppIcon.png` | 1024 × 1024 | RGB PNG | Original native strawberry geometry rendered directly at the required dimensions; installed app icon |

The four image sets use a universal 1x entry so their actual pixel dimensions remain explicit. The AppIcon uses the universal iOS 1024 × 1024 catalog slot. The native view controls display size with aspect-fit for Pip and aspect-fill with clipping for scenery. Do not upscale a mascot beyond its native pixel resolution without inspecting it on the target iPad.

The mascot icon generator returned 1254 × 1254 pixels despite an exact 1024 × 1024 prompt, including on a second correction attempt. That candidate is preserved as a normal image set. The app instead uses an original strawberry icon produced from its own native vector shapes at exactly 1024 × 1024, without editing or resizing generated raster artwork.

Generation and technical inspection do not constitute parent/child approval or App Store readiness. Review Pip's scale, tone, recognizability, edge rendering, and the garden composition in the actual app on iPad. The larger curriculum, additional worlds, complete pose library, and approved narration/audio described in the feature specification have not been produced by this asset pass.

## Art direction and behavior

- Pip is a warm cream bunny with sage overalls, pink ear interiors, rosy cheeks, forest-green eyes, and an understated expression.
- The welcome and happy poses share the same portrait framing. The native app can crossfade between them, then use SwiftUI transform animation for a small nod or bounce. These PNGs are poses, not a skeletal or frame-sequence animation rig.
- Pip has an actual alpha channel. Keep the original PNG bytes and alpha; do not flatten on white or infer transparency from the RGB preview.
- The generated RGB behind fully transparent mascot pixels contains a dark fringe/glow. Those pixels have zero alpha and are not intended to render. Verify the composited result in the native app rather than judging a viewer that discards alpha.
- The garden is scenery only. It has no character, fruit, basket, pinwheel, UI, text, or task numbers. Its central grass remains clear for native reward interactions.
- The tiny flowers and distant scenery are decorative and must not be used as lesson count targets.
- Lesson fruit, basket, and interactive pinwheel are separate native vector views owned by the implementation; they are not baked into the raster art.

## Provenance

Mode: built-in image generation tool. No CLI/API fallback and no external stock imagery.

The installed AppIcon is a separate native code asset. `scripts/render-app-icon.swift` ports `StrawberryView`'s paths from `MathBuddy/Design/NativeIllustrations.swift` to CoreGraphics and uses the palette from `MathBuddy/Design/StorybookTheme.swift`. It renders the berry directly on an opaque cream 1024 × 1024 canvas and writes RGB PNG with ImageIO. Reproduce it from the repository root with `swift scripts/render-app-icon.swift`. There is no generated-raster input, post-generation resizing, or external asset dependency.

The earlier browser home study, `mockups/previews/01-home.jpg`, was visually inspected only for palette and character direction. It was not supplied as a generated-image edit target. PipWelcome and GardenBackground were new generations. PipHappy and PipIconArtwork used PipWelcome as their explicit character identity reference.

Original generated files remain in the local generation store. Exact selected source filenames:

- PipWelcome: `exec-f7bec026-27dd-4650-8f87-8403ec0d4a8a.png`
- PipHappy: `exec-2a432a24-1d0a-42a2-90df-79f8dd1cbd87.png`
- GardenBackground: `exec-66eca636-e8e0-49dd-8c07-a7c3bcfb711c.png`
- PipIconArtwork: `exec-71a10726-f9d0-40c9-8197-51a765be3d63.png`
- Unselected icon dimension correction: `exec-e22ff87d-08c7-411b-a8cd-5c2ac60b7b5f.png`

No generated output was retouched, resampled, flattened, or recolored after generation. The selected files were copied intact into the workspace.

## Technical validation

Image metadata was checked with macOS `sips` and Pillow in read-only inspection mode; each image-set JSON filename was resolved to an existing image. Results:

| Asset | Bytes | Alpha range | Fully transparent pixels |
|---|---:|---|---:|
| PipWelcome | 1,872,330 | 0–254 | 1,027,350 |
| PipHappy | 1,892,826 | 0–254 | 1,010,375 |
| GardenBackground | 2,632,805 | No alpha channel | Not applicable |
| PipIconArtwork | 1,800,342 | No alpha channel | Not applicable |
| AppIcon | 52,357 | No alpha channel | Not applicable |

The mascot interiors reach alpha 254 rather than 255, which is the generator's output. Native alpha compositing preserves it; no opacity normalization was applied.

Selected-file SHA-256 values:

```text
809a0ad83e7d9a2f8117009a85eb91c44935edc34729deec3f1e55fa5d5b26d5  PipWelcome.png
6365fd17dc551c0c08a75ac82a9169ffa784dedb5b7fd061472496eb988dae1c  PipHappy.png
c167b073584c1d5732202b31b6b3af7f8800576d1b14165aa88fdcc9c4ac2017  GardenBackground.png
df9e2db2eee5db3d79c833e0c93d60f518e4f18a772dca06e1b1dfe9590b04b6  PipIconArtwork.png
6963e8e1fbc6dd165fdfbed8cf9c6cd0f6f59009e862be8bba066f8758e7cbbd  AppIcon.png
```

## Exact prompt set

### PipWelcome

```text
Use case: illustration-story.
Asset type: original mascot artwork bundled inside a native iPad learning app for children ages 4–8.
Primary request: Pip, an original cream-colored bunny with long upright ears, soft pink ear interiors and rosy cheeks, tiny dark forest-green eyes, a small pink nose, a warm understated smile, and simple sage-green overalls. Full body, front-facing, standing calmly with one paw lifted in a gentle hello and the other at the side.
Style/medium: beautifully restrained children's storybook illustration with matte cut-paper shapes, softly rounded forms, very subtle paper grain, clean readable silhouette, warm and reassuring.
Composition: portrait full-body character centered, generous transparent margin all around, ears and feet completely inside the canvas. One character only, no props.
Color palette: warm ivory cream, soft sage, forest green details, dusty peach pink accents.
Constraints: actual transparent background. No shadow box, no ground, no scenery, no text, no numbers, no logo, no watermarks, no border, no fruit, no basket. This is a character asset, not an app screenshot.
```

### PipHappy

```text
Use case: identity-preserve.
Asset type: transparent alternate mascot pose for a native iPad learning app.
Input image: the supplied PipWelcome image is the edit target and character identity reference.
Primary request: change only Pip's arm pose and expression to a gently pleased celebration: both short paws raised out at shoulder height, with a slightly happier small smile. Keep the exact same cream bunny identity, head size, long upright ear shape and pink interiors, rosy cheeks, green eyes, pink nose, sage overalls with two honey buttons and pocket, matte paper-grain illustration style, lighting, body proportions and full-body framing. Feet stay planted, no jumping.
Composition: same portrait centered full-body character and generous margins. Everything outside the bunny must be genuinely transparent.
Constraints: preserve alpha transparency. No scenery, confetti, background, ground shadow, text, numbers, props, border, logo, watermark or glow box. One bunny only.
```

### GardenBackground

```text
Use case: illustration-story.
Asset type: wide landscape garden background bundled in a native iPad learning app for children ages 4–8.
Primary request: a calm welcoming garden made from softly rounded matte cut-paper shapes with delicate paper grain, matching a warm storybook world. Warm ivory cream sky over soft sage-green rolling grass. A small honey-colored cottage with terracotta roof sits at the far right edge. One large rounded sage tree with a warm brown trunk at the far left edge. A few small dusty coral and warm ivory flowers at the extreme lower edges.
Composition: landscape 3:2 or wider, full-bleed to every edge, horizon around halfway down. Leave the center and lower central half open uncluttered grass for a separate animated bunny and pinwheel overlay. Scenic depth is gentle and flat enough for a child to understand.
Palette: warm cream, sage greens, honey yellow, muted terracotta and dusty coral. Restful natural daylight.
Constraints: no characters, no text, no numbers, no fruit, no countable lesson objects, no basket, no pinwheel, no interface controls, no logos, no watermarks, no frames, no transparency. Produce artwork only, not a mockup or screenshot.
```

### PipIconArtwork

```text
Use case: identity-preserve.
Asset type: square app icon for the native MathBuddy iPad learning app.
Input image: PipWelcome is the character identity reference. Preserve Pip's recognizable cream bunny face, long ears with pink interiors, rosy peach cheeks, forest green eyes, small pink nose, and gentle smile; same warm matte paper-grain storybook illustration.
Primary request: compose a simple close-up of Pip's face and ears centered against a full-bleed solid soft sage-green background. The head and both ears fit comfortably in the square, with generous outer safe margin. Only a little of the sage overall straps may show at the bottom.
Composition: exactly square 1024×1024, simple readable silhouette that works at small app-icon size. All artwork edges are square; the operating system supplies its own rounded-corner mask.
Constraints: opaque image without any transparency. Do not draw rounded corners, outer borders, text, letters, numbers, logo, watermark, badges, decorative objects, glow, or drop shadows.
```

### Icon dimension correction (not selected)

```text
Use case: identity-preserve.
Re-export this exact supplied square bunny app icon with output dimensions exactly 1024 pixels wide and 1024 pixels high. This pixel size is required for an Apple asset catalog; do not return 1254 or 1536 pixels. Keep the same complete bunny face, both full ears, sage background, paper texture, warm palette, expression and composition. Do not change the artwork; only render at the required pixel dimensions. Keep all pixels opaque, square corners, no text or watermark.
```
