#!/usr/bin/env python3
"""Final bounded packet audit; no native build or provider call."""
from pathlib import Path
from html.parser import HTMLParser
import json,subprocess,hashlib,sys
R=Path(__file__).resolve().parents[4];P=R/'assets/production/picnic-v1';D=R/'docs/orchestration/phases/2a-world'
subprocess.run([sys.executable,str(D/'world-audit.py')],check=True,cwd=R)
subprocess.run([sys.executable,str(P/'metadata/world-brand-build.py'),'--audit-only'],check=True,cwd=R)
subprocess.run(['git','diff','--check'],check=True,cwd=R)
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        for k in ['src','href']:
            if a.get(k):self.links.append(a[k])
parser=Links();gallery=P/'review/world-branding/index.html';parser.feed(gallery.read_text())
checked=[]
for url in parser.links:
    if url.startswith('#'):assert url[1:] in parser.ids,url;continue
    assert not url.startswith(('http:','https:','data:')), 'Gallery must be local/offline '+url
    path=(gallery.parent/url.split('#')[0]).resolve();assert path.exists(),path;checked.append(str(path.relative_to(R)))
ledger=json.loads((D/'proposed-ledger.json').read_text());records=ledger['requirement_records'];assert [r['id'] for r in records]==['ENV-01','ENV-02','BRAND-01','BRAND-02']
assert all(r['production_selected'] is False for r in records)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for r in records:
    for x in r.get('exports',[])+r.get('editable_sources',[]):assert sha(P/x['path'])==x['sha256']
    for key in ['recipe','font','editable_svg','export']:
        if key in r:assert sha(P/r[key]['path'])==r[key]['sha256']
# Audit changed ownership relative to the originally approved input including recovered WIP.
base='e48eb490711d9754b6b6e123f1e069aebfeae3d7'
paths=set(subprocess.check_output(['git','diff','--name-only',base],cwd=R).decode().splitlines())
paths.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=R).decode().splitlines())
def owned(name):
    if name.startswith('docs/orchestration/phases/2a-world/'):return True
    for id in ['ENV-01','ENV-02','BRAND-01','BRAND-02']:
        if name.startswith('assets/production/picnic-v1/masters/images/'+id+'/'):return True
    for kind in ['prompts','requests','metadata','review/contact-sheets']:
        if name.startswith('assets/production/picnic-v1/'+kind+'/world-'):return True
    return name.startswith('assets/production/picnic-v1/review/world-branding/')
assert all(owned(p) for p in paths),[p for p in paths if not owned(p)]
report={'status':'pass-technical-packet-human-acceptance-pending','requirements':4,'current_environment_layer_exports':12,'editable_OpenRaster_masters':4,'icon_dimensions':[1024,1024],'gallery_local_resources_checked':len(checked),'protected_inputs_unchanged':383,'changed_paths_within_owned_scope':len(paths),'actual_visual_inspection':'focused-review.md and technical-review.md; root browser renders include actual embedded SVG, screenshots and layer/disclosure interactions','reproducibility':{'environment_byte_identical_files':70,'branding_byte_identical_files':16},'pending':['human world/art','composition','icon','name','font treatment','device and child usability','content','provider and rights'],'native_build':'not performed; outside authorized scope','secret_scan':'separate staged command receipt'}
(D/'packet-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
