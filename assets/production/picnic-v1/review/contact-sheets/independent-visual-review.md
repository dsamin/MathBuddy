# Independent Phase 1 visual technical review

**Status: technical observations recorded; art, child-use, listening and human decisions remain pending.** Neither direction nor take is selected for production. Take 02 is the current gallery comparison candidate for each direction; all take 01 files and prompts remain preserved.

## Review method and inputs

Reviewed the original pixels with `view_image` for each of the four complete boards, and read the exact take 01 direction prompts and take 02 contrast-repair prompts. This review did not use the builder's visual conclusions. Quantity counts and layout findings below come from visual inspection; metadata and approximate contrast come from read-only Pillow inspection. No image was edited in this review.

- Direction A: [take 01](../../masters/images/DIRECTION-A/take-01/board.png), [take 02](../../masters/images/DIRECTION-A/take-02/board.png).
- Direction B: [take 01](../../masters/images/DIRECTION-B/take-01/board.png), [take 02](../../masters/images/DIRECTION-B/take-02/board.png).
- Exact prompts: [A original](../../prompts/direction-a-take-01.txt), [A repair](../../prompts/direction-a-take-02.txt), [B original](../../prompts/direction-b-take-01.txt), [B repair](../../prompts/direction-b-take-02.txt).

All four files are opaque RGB PNGs at 1536 × 1024. The take 02 revisions preserve the observed quantities, regions, poses, orientation arrangements, labels and garden toys. They are generated sibling revisions; this is a semantic preservation finding, not a claim that every other pixel is identical.

## Mathematical and composition findings

| Check | Observed in both current take 02 candidates |
|---|---|
| Counting landscape | Exactly five complete working strawberries, arranged three above two. A separately bordered target card contains exactly three much smaller strawberry icons, an arrow and a basket pictogram. Working source tray is left of an empty destination basket. |
| Counting portrait | Exactly five complete working strawberries and exactly three target icons. The source tray is above the empty basket: a vertical reflow rather than a landscape crop. |
| Later five-quantity stress panel | Exactly six working strawberries in a three-by-two grid, and exactly five small reference strawberries arranged three above two. Destination basket is empty. |
| Visibility and separation | No working fruit is hidden by the basket, mascot, other fruit or scene edge. Source, destination and reference regions remain visibly distinct. No additional decorative berries occur outside those regions. |
| Sound-off goal | The three-berry pictorial reference and basket arrow show the target without a spoken prompt or numeral. Child recognition of the reference card as a goal rather than extra playable fruit still needs a human/child review. |
| Garden landscape and portrait | One large four-blade pinwheel with a central hub and stem, one large flower, Pip at the edge, and a separate fully visible Finish control. Small scenery flowers read as decoration, not extra large rewards. |
| Native composition considerations | Home/replay sit above the workspace and Undo/Help/Done remain below it in both counting orientations. Garden Finish remains below the toys in both orientations. These illustrations do not prove exact iPad safe areas, hit sizes, split-view behavior or native layout. |

No mathematical quantity failure was observed in either current candidate. These are initial-state static compositions; they do not prove the visibility of every intermediate basket state, rapid movement or completed group.

## Character identity and visual differences

Cream fur, pink ear interiors, dark oval eyes, terracotta nose, peach cheeks, pear-shaped body and sage neckerchief remain recognizable across the attentive/pleased poses and scene appearances. No disappointed expression is shown. The attentive pose points gently; the pleased pose clasps its paws calmly.

**Unresolved identity detail:** one ear changes from an upright/diagonal shape in the attentive pose to a bent/floppy shape in the pleased pose. This remains in both directions and both takes. Before a final identity pack, either freeze that silhouette or obtain an explicit human decision allowing this ear movement; do not silently call the identity geometry invariant.

Direction A uses visibly richer paper texture and painterly scenery. Direction B simplifies foliage and backgrounds into broader smooth forms; the working fruit separates from the scenery more clearly. These observations support recommending B for the next comparison decision, but artistic appeal and the desired relationship to Pebble remain human choices.

## Contrast repair and remaining control semantics

The original take 01 garden buttons used white Finish lettering on coral fills. Representative sampled contrast was approximately 2.48:1 for A and 2.61:1 for B. The take 02 outputs visibly replace both Finish labels with dark ink and retain the exact word.

Read-only sample checks on take 02 found approximate dark glyph-core/fill contrast of **6.49:1 / 6.37:1** in A landscape/portrait and **6.33:1 / 6.38:1** in B landscape/portrait. Method: sample coral fill at `(250, 940)` or `(750, 942)`; inspect Finish text rectangles `(280, 932, 350, 953)` or `(778, 932, 842, 953)`; calculate sRGB relative luminance using median RGB among the darkest third of text-region pixels with luminance below 0.1. Texture and antialiasing vary across pixels. These approximate raster findings confirm the direction of the repair; they do not certify a future editable native control's contrast.

The circular-back replay symbol could be interpreted as Undo/reset. A later design should establish clearer replay semantics and accessible naming. This is a follow-up design concern, not evidence that the static quantity target is wrong.

## Production limits and pending decisions

The boards flatten every character, object, scene, control and label into one opaque image. They provide no transparent production exports, separated basket rear/front layers, stable object anchors, named pivots, pinwheel rig, editable text or inspected motion frames. In later production, basket interior/rear/rim separation must preserve all counted fruit; pinwheel blades must rotate around an agreed hub; native text and controls must remain editable. The provisional motion/layer briefs require their own review.

Human decisions remain open for art direction, Pip's final ear geometry/pose flexibility, texture/scenery density, reference-card comprehension, toy appeal and replay-icon semantics. This review provides no listening judgment, voice selection, provider/rights approval, child suitability approval or product approval. No Phase 2 asset batch or native implementation is authorized by these findings.
