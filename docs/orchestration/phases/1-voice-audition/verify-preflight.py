"""Offline input audit only. Never imports provider SDKs or makes requests."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PHASE = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest_path = ROOT / 'assets/production/picnic-v1/requests/voice/request-manifest.json'
manifest = json.loads(manifest_path.read_text())
catalog_path = ROOT / manifest['source_catalog_path']
snapshot_path = ROOT / manifest['snapshot_path']
catalog = json.loads(catalog_path.read_text())
snapshot = json.loads(snapshot_path.read_text())
assert digest(catalog_path) == manifest['source_catalog_sha256']
assert digest(snapshot_path) == manifest['snapshot_sha256']
records = {s['id']: s for s in catalog['scripts']}
assert len(snapshot['scripts']) == 5
assert all(s == records[s['id']] for s in snapshot['scripts'])
assert len(manifest['requests']) == 10
rows = []
for item in manifest['requests']:
    path = ROOT / item['request_path']
    request = json.loads(path.read_text())
    assert digest(path) == item['request_sha256']
    text = records[item['script_id']]['exact_script']
    expected = dict(model=manifest['model'], voice=item['voice'], input=text,
                    instructions=manifest['same_instructions'], response_format='wav', speed=1.0)
    assert request['provider_request'] == expected
    assert request['exact_script'] == text
    assert request['cli_job'] == {**expected, 'out': f"{item['script_id']}/{item['take_id']}.wav"}
    assert request['provenance']['script_text_sha256'] == hashlib.sha256(text.encode()).hexdigest()
    assert request['generation_attempts'] == []
    assert request['actual_master_path'] is None and request['actual_recording_sha256'] is None
    assert request['generated_at'] is None
    assert not (ROOT / request['expected_master_path']).exists()
    rows.append({**item, 'verified': True, 'expected_master_path': request['expected_master_path'], 'output_exists': False})
assert {(x['script_id'], x['voice']) for x in rows} == {(s['id'], v) for s in snapshot['scripts'] for v in ['cedar', 'marin']}
inputs = [manifest_path, catalog_path, snapshot_path,
          ROOT/'docs/planning/asset-production-plan.md', ROOT/'docs/plans/2026-10-03-direction-b-next-steps.md',
          ROOT/'tasks/lessons.md', ROOT/'assets/production/picnic-v1/metadata/voice-capability.json',
          ROOT/'assets/production/picnic-v1/metadata/provider-rights.json']
inputs += sorted((ROOT/'assets/production/picnic-v1/review/listening').glob('*'))
report = {'checked_date': '2026-10-04', 'status': 'preflight-only', 'source_hashes': {str(p.relative_to(ROOT)): digest(p) for p in inputs if p.is_file()},
          'requests': rows, 'exact_lines': [{'id':s['id'], 'text':s['exact_script']} for s in snapshot['scripts']],
          'total_input_characters_excluding_instructions':sum(len(s['exact_script']) for s in snapshot['scripts'])*2,
          'total_words_excluding_instructions':sum(len(s['exact_script'].split()) for s in snapshot['scripts'])*2,
          'recordings':0, 'provider_calls':0, 'checks':'all assertions passed'}
(PHASE/'request-audit.json').write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
print('PASS: five complete catalog records, ten exact request hashes/settings, ten absent masters; zero provider calls.')
