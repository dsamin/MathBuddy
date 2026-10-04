#!/usr/bin/env python3
"""Audit review media, exact requests, pending decisions and Phase 1 boundaries."""
from pathlib import Path
import hashlib
import json
import subprocess
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from PIL import Image
import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'assets/production/picnic-v1'

def read(p):
    return json.loads(p.read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.urls.append(value)

json_files = list(PACK.rglob('*.json'))
for p in json_files:
    read(p)
images = []
for p in sorted(PACK.rglob('*')):
    if p.suffix.lower() in ('.png', '.gif', '.jpg'):
        with Image.open(p) as im:
            im.load()
            images.append({'path': str(p.relative_to(PACK)), 'dimensions': list(im.size),
                           'format': im.format, 'frames': getattr(im, 'n_frames', 1)})
for d in ('A', 'B'):
    for take in ('take-01', 'take-02'):
        directory = PACK / f'masters/images/DIRECTION-{d}/{take}'
        p = directory / 'board.png'; m = read(directory / 'provenance.json')
        assert sha(p) == m['sha256']
        assert sha(PACK / m['prompt']) == m['prompt_sha256']
        assert m['human_art_review'] == 'pending'
        with Image.open(p) as im:
            assert im.size == (1536, 1024)

scripts = read(ROOT / 'docs/planning/voice-script-catalog.json')
by_id = {s['id']: s for s in scripts['scripts']}
manifest = read(PACK / 'requests/voice/request-manifest.json')
assert len(manifest['requests']) == 10 and manifest['recordings_generated'] == 0
voices = {}
for entry in manifest['requests']:
    path = ROOT / entry['request_path']; r = read(path)
    assert sha(path) == entry['request_sha256']
    assert r['provider_request']['input'] == r['exact_script'] == r['cli_job']['input'] == by_id[entry['script_id']]['exact_script']
    assert not (ROOT / r['expected_master_path']).exists()
    voices.setdefault(entry['script_id'], set()).add(entry['voice'])
assert set(voices) == set(scripts['audition_script_ids'])
assert all(v == {'cedar', 'marin'} for v in voices.values())
assert not list((PACK / 'masters/audio').rglob('*.wav'))

motion = []
required = ('layers', 'triggers', 'start_state', 'middle_state', 'end_state', 'duration_ms',
            'repeat_policy', 'global_interrupts', 'reduced_motion', 'occlusion_contract',
            'semantic_state_ownership', 'sound_cues')
for n in range(1, 8):
    directory = PACK / f'motion/M{n:02}'
    brief = read(directory / 'brief.json')
    assert brief['asset_id'] == f'M{n:02}'
    orientation = brief['coordinate_system']['orientation_policy']
    expected = {1:'LAYOUT-COUNT',2:'LAYOUT-JOIN',3:'LAYOUT-TAKE',4:'active',5:'active',6:'garden',7:'guide'}[n]
    assert expected.lower() in orientation.lower()
    assert all(brief.get(k) for k in required)
    assert all(layer.get('pivot') for layer in brief['layers'])
    assert brief['status'] == 'provisional-pending-human-review' and brief['selected_take'] is None
    pdf = pdfium.PdfDocument(str(directory / 'storyboard.pdf'))
    assert len(pdf) == 1
    page = pdf.get_page(0); bitmap = page.render(scale=.2)
    assert bitmap.width > 0 and bitmap.height > 0
    bitmap.close(); page.close(); pdf.close()
    motion.append({'id': brief['asset_id'], 'layer_count': len(brief['layers']), 'pdf_decoded': True})

videos = []
for name in ('pickup-return-settle.mp4', 'reduced-motion.mp4'):
    p = PACK / 'motion/M01' / name
    result = subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-show_streams', '-show_format',
                             '-of', 'json', str(p)], check=True, capture_output=True, text=True)
    probe = json.loads(result.stdout)
    video = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    assert not any(s['codec_type'] == 'audio' for s in probe['streams'])
    assert (video['width'], video['height']) == (1440, 1080)
    assert int(video['nb_read_frames']) == 144 and abs(float(probe['format']['duration']) - 4.8) < .01
    videos.append({'path': str(p.relative_to(PACK)), 'sha256': sha(p), 'dimensions': [1440, 1080],
                   'decoded_frames': 144, 'duration_seconds': 4.8, 'audio_streams': 0})

link_count = 0
for p in PACK.rglob('*.html'):
    parser = Links(); parser.feed(p.read_text())
    for value in parser.urls:
        url = urlsplit(value)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (p.parent / unquote(url.path)).resolve()
        assert target.is_file(), f'Broken local link in {p.relative_to(PACK)}: {value}'
        link_count += 1
assert not (PACK / 'delivery').exists()
decisions = read(PACK / 'metadata/review-decisions.json')
assert not decisions['production_selected']
selection_path = PACK / 'metadata/direction-selection.json'
if selection_path.exists():
    selection = read(selection_path)
    selected = [d for d in decisions['decisions'] if d['status'] == 'selected']
    assert len(selected) == 1 and selected[0]['kind'] == 'art-direction'
    assert selection['status'] == 'selected-by-user' and selection['reviewer'] == 'user'
    assert selection['artifact'] == 'masters/images/DIRECTION-B/take-02/board.png'
    assert sha(PACK / selection['artifact']) == selection['sha256']
for decision in decisions['decisions']:
    if decision['kind'] == 'art-direction' and decision['status'] == 'selected':
        assert decision['reviewer'] == 'user'
        assert decision['selected_artifact'] == 'masters/images/DIRECTION-B/take-02/board.png'
        assert selection_path.exists()
    else:
        assert decision['status'] == 'pending' and decision['reviewer'] is None
boundary = subprocess.run(['git', 'diff', '18b36ed', '--', 'MathBuddy/', 'MathBuddy.xcodeproj/',
                           'project.yml', 'mockups/', 'assets/audio/', 'docs/experiments/'],
                          cwd=ROOT, check=True, capture_output=True, text=True)
assert not boundary.stdout
report = {'status': 'technical-audit-pass-with-explicit-voice-gap', 'json_files_parsed': len(json_files),
          'decoded_images': images, 'image_sources_and_prompts_hash_match': True,
          'motion_contracts': motion, 'videos': videos, 'html_local_links_resolve': link_count,
          'voice_requests_exact': 10, 'actual_audio_recordings': 0, 'actual_audio_wording': 'not-checkable-no-recordings',
          'human_decisions': 'Direction B selected; other decisions pending' if any(d['status'] == 'selected' for d in decisions['decisions']) else 'all pending', 'approved_delivery_exists': False,
          'baseline_native_and_experiments_unchanged': True,
          'visual_quantity_review': 'manual inspection recorded separately; not inferred from file existence',
          'motion_geometry_review': 'see motion/review/technical-measurements.json; native behavior not tested'}
output = PACK / 'metadata/file-audit.json'; output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('decoded_images','motion_contracts','videos')}, indent=2))
