#!/usr/bin/env python3
"""Audit the five character candidates, provenance and unchanged prior files."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
from PIL import Image

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parents[2]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
ids = [f'PIP-{n:02}' for n in range(1, 6)]
preflight = read(PACK/'metadata/pip-character-preflight.json')
allowed = {
    'tasks/todo.md', 'docs/review-checkpoint.md', 'docs/planning/asset-register.csv',
    'assets/production/picnic-v1/catalog.json', 'assets/production/picnic-v1/README.md',
    'assets/production/picnic-v1/metadata/review-decisions.json',
    'assets/production/picnic-v1/metadata/provider-rights.json',
}
protected = []
changed = []
for p, digest in preflight['tracked_file_sha256'].items():
    actual = sha(ROOT/p)
    if p not in allowed:
        assert actual == digest, f'Out-of-scope mutation: {p}'
        protected.append(p)
    elif actual != digest:
        changed.append(p)

alignment = read(PACK/'metadata/pip-alignment-measurements.json')
review = read(PACK/'metadata/pip-character-review.json')
assert not review['production_selected'] and review['selectedTake'] is None
assert all(x['status'] == 'pending' and x['reviewer'] is None for x in review['human_reviews'].values())
assert alignment['common_anchor_normalized'] == [.5, .9]
assert alignment['common_safe_box_exclusive_px'] == [154,154,1382,1414]
assert alignment['recipe_sha256'] == sha(PACK/alignment['recipe'])
selection = read(PACK/'metadata/direction-selection.json')
assert sha(PACK/selection['artifact']) == selection['sha256']
catalog = read(PACK/'catalog.json')
assert catalog['delivery_manifest'] is None and catalog['voice_recording_count'] == 0
assert not (PACK/'delivery').exists()
measurements = {x['id']: x for x in alignment['records']}
records = {x['id']: x for x in catalog['records'] if x['id'] in ids}
assert set(records) == set(ids) and len([x for x in catalog['records'] if x['id'] in ids]) == 5
decoded = []
for id in ids:
    rec = records[id]
    m = measurements[id]
    assert rec['selectedTake'] is None and not rec['production_selected']
    assert rec['humanArtReview']['status'] == rec['humanIdentityReview']['status'] == rec['rightsDecision'] == 'pending'
    folder = PACK/f'masters/images/{id}/take-01'
    prov = read(folder/'provenance.json')
    request = read(PACK/prov['exact_request_file'])
    prompt = PACK/prov['exact_prompt_file']
    assert sha(prompt) == prov['exact_prompt_sha256']
    assert sha(PACK/prov['exact_request_file']) == prov['exact_request_sha256']
    assert prompt.read_text() == request['exact_arguments']['prompt']+'\n'
    assert request['exact_arguments']['transparent_background'] is True
    assert request['exact_arguments']['referenced_image_paths'] == [x['tool_argument_path'] for x in prov['references']]
    for ref in prov['references']:
        assert sha(PACK/ref['path']) == ref['sha256']
    for kind, key in [('original','original_file'), ('aligned','aligned_review_file')]:
        path = PACK/prov[key]
        expected = prov['original_sha256' if kind == 'original' else 'aligned_review_sha256']
        assert sha(path) == expected
        with Image.open(path) as im:
            im.load()
            assert im.mode == 'RGBA'
            a = im.getchannel('A')
            assert a.getextrema() == (0,255)
            if kind == 'aligned':
                assert im.size == (1536,1536)
                assert list(a.getbbox()) == m['alpha_bounds_nonzero_exclusive']
                assert m['visible_core_foot_baseline_row'] == 1382
                assert abs(m['foot_anchor_x_error_px']) <= .5
                assert abs(m['core_height_px']-1180) <= 1
                assert m['safe_box_fit'] and m['significant_alpha_components'] == 1
        decoded.append(str(path.relative_to(PACK)))
    assert sha(folder/'original.png') == m['source_sha256']
    assert sha(folder/'aligned-review.png') == m['export_sha256']
    assert sha(Path(prov['tool_generated_source'])) == prov['original_sha256']
    assert prov['human_art_review'] == prov['human_identity_review'] == 'pending'

rows = list(csv.DictReader((ROOT/'docs/planning/asset-register.csv').open()))
assert len(rows) == 196
for row in rows:
    if row['asset_id'] in ids:
        assert row['status'] == 'character-review-candidate-pending-human-approval'
        assert 'aligned-review.png' in row['existing_candidate_paths']
        assert row['human_review'].startswith('Pending:')

# All previous production media are protected by preflight. New media must be character-only.
new = subprocess.check_output(['git','ls-files','--others','--exclude-standard','-z'],cwd=ROOT,text=True).split('\0')
staged = subprocess.check_output(['git','diff','--cached','--name-only','--diff-filter=A','-z'],cwd=ROOT,text=True).split('\0')
for p in set(new+staged)-{''}:
    q = ROOT/p
    if q.suffix.lower() in {'.png','.jpg','.jpeg','.webp','.gif','.mp4','.wav','.m4a','.svg'}:
        assert ('/masters/images/PIP-' in p or '/review/contact-sheets/pip-' in p), f'Unrelated new media: {p}'
assert not list((PACK/'masters/audio').rglob('*.wav'))

link_count = 0
for p in [ROOT/'tasks/todo.md',ROOT/'docs/review-checkpoint.md',PACK/'README.md',
          PACK/'review/contact-sheets/pip-character-review.md']:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
        if target.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        target = target.split('#')[0]
        if not target:
            continue
        q = Path(target) if target.startswith('/') else p.parent/target
        assert q.exists(), f'Broken link: {p}: {target}'
        link_count += 1

for p in PACK.rglob('*.json'):
    read(p)
report = {
    'status':'pass-with-explicit-technical-limitations-human-approval-pending',
    'decoded_pose_files':decoded,'logical_character_records':5,'asset_register_rows':196,
    'protected_preexisting_files_unchanged':len(protected),'allowed_modified_preexisting_files':changed,
    'preexisting_dirty_documentation_preserved':preflight['preexisting_dirty_paths'],
    'markdown_links_resolved':link_count,'human_approvals_granted':0,
    'production_delivery_created':False,'voice_recordings_generated':0,
    'unrelated_media_or_native_changes':False,
    'reference_sha256':selection['sha256'],
    'recipe_sha256':sha(PACK/'metadata/pip-alignment-recipe.py'),
    'audit_script_sha256':sha(Path(__file__)),
}
(PACK/'metadata/pip-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
