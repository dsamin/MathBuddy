#!/usr/bin/env python3
"""Reproduce the authorized PIP review exports; no artistic painting or app work.

Run from any directory with Python 3, Pillow, NumPy and SciPy.
--check computes PNGs in memory and compares every saved recipe output.
Default writes missing outputs only and refuses changed immutable outputs.
"""
from pathlib import Path
import argparse
import hashlib
import io
import json
import platform
import PIL
import numpy as np
import scipy
from scipy.ndimage import binary_dilation, label
from PIL import Image, ImageDraw, ImageFont

PACK = Path(__file__).resolve().parents[1]
SIZE = 1536
BASELINE = 1382
ANCHOR = (768, 1382.4)
SAFE = (154, 154, 1382, 1414)  # exclusive right/bottom
CORE_ALPHA = 32
TARGET_HEIGHT = 1180
NAMES = ['Idle welcome', 'Attentive pointing', 'Supportive thinking', 'Pleased', 'Farewell']
parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
args = parser.parse_args()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def save_bytes(path, data):
    if args.check:
        assert path.is_file() and path.read_bytes() == data, f'Reproduction mismatch: {path}'
    elif path.exists():
        assert path.read_bytes() == data, f'Refusing to overwrite changed take: {path}'
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

def png(im):
    buf = io.BytesIO()
    im.save(buf, format='PNG', compress_level=9)
    return buf.getvalue()

def bbox(mask):
    return list(Image.fromarray(mask.astype(np.uint8) * 255).getbbox())

def core_box(im):
    return bbox(np.array(im)[:, :, 3] >= CORE_ALPHA)

def foot_box(im):
    a = np.array(im)[:, :, 3]
    b = core_box(im)
    foot = a >= CORE_ALPHA
    foot[:b[3] - round((b[3] - b[1]) * .04)] = False
    return bbox(foot)

def resize_alpha(im, size):
    # Premultiplied interpolation prevents hidden RGB from bleeding into edges.
    return im.convert('RGBa').resize(size, Image.Resampling.LANCZOS).convert('RGBA')

def composite(im, bg):
    out = Image.new('RGBA', im.size, bg)
    out.alpha_composite(im)
    return out.convert('RGB')

def font(size):
    # Adult raster review only; no font file redistributed or app choice made.
    return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', size)

def heading(draw, xy, text, size=24, color='#22323b'):
    draw.text(xy, text, font=font(size), fill=color)

images = []
records = []
for n in range(1, 6):
    asset = f'PIP-{n:02}'
    take = PACK / f'masters/images/{asset}/take-01'
    source = take / 'original.png'
    with Image.open(source) as decoded:
        decoded.load()
        assert decoded.mode == 'RGBA', f'Actual alpha missing: {source}'
        original = decoded.copy()
    rgba = np.array(original)
    a = rgba[:, :, 3].copy()
    components, count = label(a >= CORE_ALPHA)
    counts = np.bincount(components.ravel())
    counts[0] = 0
    main_id = int(counts.argmax())
    assert np.count_nonzero(counts) == 1, 'Detached significant alpha requires provider repair'
    main = components == main_id
    # Minimal technical finishing: only quantization dust and distant low-alpha islands.
    # Retain >=2 alpha within four source pixels of the significant character.
    keep = (a >= 2) & binary_dilation(main, iterations=4)
    removed = (a > 0) & ~keep
    rgba[:, :, 3] = np.where(keep, a, 0)
    rgba[~keep, :3] = 0  # hidden RGB only, never visible colors
    cleaned = Image.fromarray(rgba)
    cb = core_box(cleaned)
    # One uniform similarity transform per pose; no warping, flipping or rotation.
    # Match the same visible ear-to-foot scale; record actual rounding/error below.
    scale = TARGET_HEIGHT / (cb[3] - cb[1])
    resized_size = tuple(round(x * scale) for x in original.size)
    scaled = resize_alpha(cleaned, resized_size)
    scb = core_box(scaled)
    fb = foot_box(scaled)
    source_foot_center_scaled = (fb[0] + fb[2]) / 2
    dx = round(ANCHOR[0] - source_foot_center_scaled)
    dy = BASELINE - (scb[3] - 1)
    # Full source fits on the canvas; this is padding rather than silhouette clipping.
    assert dx >= 0 and dy >= 0
    assert dx + scaled.width <= SIZE and dy + scaled.height <= SIZE
    aligned = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    aligned.alpha_composite(scaled, (dx, dy))
    output = take / 'aligned-review.png'
    out_bytes = png(aligned)
    save_bytes(output, out_bytes)
    aa = np.array(aligned)[:, :, 3]
    ab = bbox(aa > 0)
    core = core_box(aligned)
    feet = foot_box(aligned)
    foot_center = (feet[0] + feet[2]) / 2
    assert core[3] - 1 == BASELINE
    assert abs(foot_center - ANCHOR[0]) <= .5
    assert abs(core[3] - core[1] - TARGET_HEIGHT) <= 1
    assert ab[0] >= SAFE[0] and ab[1] >= SAFE[1] and ab[2] <= SAFE[2] and ab[3] <= SAFE[3]
    assert not np.any(aa[[0, -1], :]) and not np.any(aa[:, [0, -1]])
    rec = {
        'id': asset, 'pose': NAMES[n-1], 'take': 'take-01',
        'source': str(source.relative_to(PACK)), 'source_sha256': sha(source.read_bytes()),
        'source_mode': original.mode, 'source_canvas_px': list(original.size),
        'source_alpha_bounds_nonzero_exclusive': bbox(a > 0),
        'source_core_bounds_alpha_ge_32_exclusive': bbox(main),
        'source_quantization_dust_alpha_1_pixels': int(np.count_nonzero(a == 1)),
        'source_low_alpha_pixels_removed': int(np.count_nonzero(removed)),
        'source_max_alpha_removed': int(a[removed].max()),
        'export': str(output.relative_to(PACK)), 'export_sha256': sha(out_bytes),
        'export_canvas_px': [SIZE, SIZE], 'export_mode': 'RGBA',
        'uniform_scale_nominal': scale, 'resampled_size_px': list(resized_size),
        'rounded_scale_xy': [resized_size[0]/original.width, resized_size[1]/original.height],
        'translation_px': [dx, dy], 'rotation_deg': 0,
        'alpha_bounds_nonzero_exclusive': ab,
        'core_bounds_alpha_ge_32_exclusive': core,
        'core_height_px': core[3] - core[1],
        'foot_band_bounds_alpha_ge_32_exclusive': feet,
        'foot_center_x_px': foot_center,
        'foot_anchor_x_error_px': foot_center - ANCHOR[0],
        'visible_core_foot_baseline_row': core[3] - 1,
        'outer_antialias_last_row': ab[3] - 1,
        'alpha_min_max': [int(aa.min()), int(aa.max())],
        'transparent_pixels': int(np.count_nonzero(aa == 0)),
        'partial_alpha_pixels': int(np.count_nonzero((aa > 0) & (aa < 255))),
        'opaque_pixels': int(np.count_nonzero(aa == 255)),
        'significant_alpha_components': int(np.count_nonzero(np.bincount(label(aa >= 32)[0].ravel())[1:])),
        'safe_box_fit': True, 'canvas_edge_alpha_pixels': 0,
        'technical_registration': 'pass', 'human_art_identity_review': 'pending'
    }
    records.append(rec)
    images.append(aligned)

# Main five-pose sheet, same canvas sampling (no per-thumbnail auto-fit).
sheet = Image.new('RGB', (2000, 620), '#fff9ef')
d = ImageDraw.Draw(sheet)
heading(d, (30, 22), 'Pip’s Picnic · Direction B · five still-pose review candidates', 32)
heading(d, (30, 68), 'Identity / art approval pending · same 1536² canvas and foot anchor', 21)
for i, im in enumerate(images):
    x = i * 400
    sheet.paste(composite(resize_alpha(im, (380, 380)), '#fff9ef'), (x+10, 130))
    heading(d, (x+20, 104), f'PIP-{i+1:02}', 21)
    heading(d, (x+20, 523), NAMES[i], 21)
heading(d, (30, 575), 'Ear refinement: rounded unbent ears across all five. Review pixels do not prove physical iPad usability.', 20)
save_bytes(PACK / 'review/contact-sheets/pip-five-poses.png', png(sheet))

alpha_sheet = Image.new('RGB', (1800, 900), '#fff9ef')
d = ImageDraw.Draw(alpha_sheet)
heading(d, (20, 15), 'Decoded aligned RGBA · light and dark alpha inspection', 27)
for row, bg in enumerate(('#fff9ef', '#23303a')):
    for i, im in enumerate(images):
        x, y = i*360, 75+row*390
        alpha_sheet.paste(composite(resize_alpha(im, (350, 350)), bg), (x+5, y))
        heading(d, (x+15, y+355), f'PIP-{i+1:02} · {"light" if row == 0 else "dark"}', 19)
heading(d, (20, 866), 'Provider originals retained. Derived exports remove disclosed low-alpha dust; no RGB repaint or invented layers.', 18)
save_bytes(PACK / 'review/contact-sheets/pip-alpha-light-dark.png', png(alpha_sheet))

small = Image.new('RGB', (1500, 740), '#fff9ef')
d = ImageDraw.Draw(small)
heading(d, (20, 18), 'Small-size readability · pixels only · no device / touch / child-usability claim', 26)
for i in range(5):
    heading(d, (i*300+20, 66), f'PIP-{i+1:02} · {NAMES[i]}', 17)
for row, (size, y) in enumerate(((256, 108), (128, 405), (64, 604))):
    for i, im in enumerate(images):
        x = i*300+(300-size)//2
        small.paste(composite(resize_alpha(im, (size, size)), '#fff9ef'), (x, y))
        heading(d, (i*300+20, y+size+6), f'{size}×{size} canvas · ~{round(size*TARGET_HEIGHT/SIZE)}px silhouette', 15)
save_bytes(PACK / 'review/contact-sheets/pip-small-size.png', png(small))

diagnostic = Image.new('RGB', (1800, 490), '#fff9ef')
d = ImageDraw.Draw(diagnostic)
heading(d, (20, 15), 'Registration diagnostic · safe box / visible foot row / anchor', 27)
for i, im in enumerate(images):
    x, y, s = i*360+5, 70, 350/1536
    diagnostic.paste(composite(resize_alpha(im, (350,350)), '#fff9ef'), (x,y))
    d.rectangle((x+SAFE[0]*s,y+SAFE[1]*s,x+SAFE[2]*s,y+SAFE[3]*s), outline='#b0a18b',width=1)
    d.line((x,y+BASELINE*s,x+350,y+BASELINE*s), fill='#9d6eae',width=2)
    px, py = x+ANCHOR[0]*s, y+ANCHOR[1]*s
    d.ellipse((px-4,py-4,px+4,py+4),fill='#aa4455')
    heading(d, (x+10, 431), f'PIP-{i+1:02} · x error {records[i]["foot_anchor_x_error_px"]:+.1f}px',18)
save_bytes(PACK / 'review/contact-sheets/pip-registration.png', png(diagnostic))

# Actual output pixels, no rescale, for edge/ear/face/scarf review.
details = Image.new('RGB', (1500, 1000), '#fff9ef')
d = ImageDraw.Draw(details)
heading(d, (20, 15), '100% decoded edge details · ear tips and scarf tails on dark', 27)
for i, im in enumerate(images):
    core = core_box(im)
    # Ear tip at minimum significant-alpha row; include perimeter at 100%.
    ear = im.crop((core[0]+int((core[2]-core[0])*.55), core[1]-12,
                   core[0]+int((core[2]-core[0])*.55)+280, core[1]+268))
    scarf = im.crop((core[0]+80, 855, core[0]+360, 1135))
    x = i*300+10
    details.paste(composite(ear, '#23303a'), (x,80))
    details.paste(composite(scarf, '#23303a'), (x,400))
    heading(d, (x, 695), f'PIP-{i+1:02} · ear / scarf', 19)
    # Center face crop downsampled explicitly, independent of edge samples.
    face = im.crop((core[0]+140, 570, core[0]+600, 920))
    details.paste(composite(resize_alpha(face,(280,213)), '#fff9ef'),(x,745))
save_bytes(PACK / 'review/contact-sheets/pip-edge-details.png', png(details))

measurement = {
    'schema_version': 1, 'scope': 'PIP-01..05 review batch only',
    'recipe': 'metadata/pip-alignment-recipe.py',
    'recipe_sha256': sha(Path(__file__).read_bytes()),
    'dependencies': {'python': platform.python_version(), 'pillow': PIL.__version__,
                     'numpy': np.__version__, 'scipy': scipy.__version__},
    'coordinates': 'top-left origin; pixel rows integer; bounds right/bottom exclusive',
    'common_canvas_px': [SIZE, SIZE], 'common_mode': 'RGBA',
    'common_core_character_height_px': TARGET_HEIGHT, 'core_height_rounding_tolerance_px': 1,
    'core_definition': 'alpha >=32; excludes only low-opacity edge fringe',
    'common_safe_box_exclusive_px': list(SAFE),
    'common_anchor_normalized': [.5, .90], 'common_geometric_anchor_px': list(ANCHOR),
    'common_raster_foot_baseline_row': BASELINE, 'max_foot_center_rounding_error_px': .5,
    'alpha_finishing': 'Preserve original; export zeroes alpha=1 and low-alpha pixels more than four source pixels from main alpha>=32 silhouette. RGB only zeroed when alpha zero. No repaint, matte extraction, artistic warp or color adjustment.',
    'resampling': 'Pillow LANCZOS in premultiplied RGBa; uniform scale then integer translation into transparent canvas',
    'reproduction_command': 'python3 assets/production/picnic-v1/metadata/pip-alignment-recipe.py --check',
    'status': 'technical-registration-pass-human-approval-pending',
    'human_approval': False, 'records': records
}
save_bytes(PACK/'metadata/pip-alignment-measurements.json', (json.dumps(measurement,indent=2)+'\n').encode())
for rec in records:
    print(rec['id'], rec['export_canvas_px'], 'height', rec['core_height_px'],
          'baseline',rec['visible_core_foot_baseline_row'], 'anchor x error',rec['foot_anchor_x_error_px'],
          'bounds',rec['alpha_bounds_nonzero_exclusive'], 'sha256',rec['export_sha256'])
print('Reproduced and verified' if args.check else 'Saved immutable review exports and measurement records')
