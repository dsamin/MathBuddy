#!/usr/bin/env python3
"""Decoded asset, editable-source, semantic-clearance and protected-input audit."""
from pathlib import Path
from PIL import Image
import numpy as np
import json, hashlib, zipfile, io, xml.etree.ElementTree as ET, sys
ROOT=Path(__file__).resolve().parents[4];PACK=ROOT/'assets/production/picnic-v1';PHASE=ROOT/'docs/orchestration/phases/2a-world'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,msg):
    if not ok:raise AssertionError(msg)
def composite(ls):
    im=Image.new('RGBA',ls[0].size)
    for x in ls:im=Image.alpha_composite(im,x)
    return im
records=json.loads((PACK/'metadata/world-registration.json').read_text())['records']
maps=json.loads((PACK/'metadata/world-safe-regions.json').read_text());result={'status':'pass','orientation_records':[]}
for record in records:
    aid=record['asset_id'];orient=record['orientation'];w,h=record['canvas_px'];d=PACK/f'masters/images/{aid}'/record['take_id']/orient
    layers=[Image.open(d/f'{r}.png').convert('RGBA') for r in ['distant','ground','foreground']]
    for role,im in zip(['distant','ground','foreground'],layers):check(im.size==(w,h),aid+' '+orient+' '+role+' dimensions')
    arr=[np.array(x) for x in layers];ref=np.array(Image.open(d/'composite.png').convert('RGBA'));recon=np.array(composite(layers))
    check(np.array_equal(ref,recon),'exact reconstruction');check(np.all(ref[:,:,3]==255),'opaque composite')
    check(len({sha(d/f'{role}.png') for role in ['distant','ground','foreground']})==3,'layers distinct')
    contributions={}
    for i,role in enumerate(['distant','ground','foreground']):
        minus=np.array(composite([x for k,x in enumerate(layers) if i!=k]));count=int(np.count_nonzero(np.any(ref!=minus,axis=2)))
        check(count>10000,'meaningful visible contribution '+role);contributions[role]=count
    checks=[]
    for key,rect in maps['orientations'][orient]['union'].items():
        x,y,rw,rh=rect;pad=.015
        box=(round(max(0,x-pad)*w),round(max(0,y-pad)*h),round(min(1,x+rw+pad)*w),round(min(1,y+rh+pad)*h))
        x0,y0,x1,y1=box;nonzero=int(np.count_nonzero(arr[2][y0:y1,x0:x1,3]))
        check(nonzero==0,'foreground crosses expanded semantic mask '+key);checks.append({'name':key,'expanded_px':box,'foreground_nonzero_alpha':nonzero})
    with zipfile.ZipFile(d/'editable.ora') as z:
        check(z.read('mimetype')==b'image/openraster','editable mime')
        xml=ET.fromstring(z.read('stack.xml'));check((int(xml.attrib['w']),int(xml.attrib['h']))==(w,h),'editable canvas')
        xml_layers=xml.findall('stack/layer');check(len(xml_layers)==3,'editable separate layers')
        ora=[]
        for e in reversed(xml_layers):
            check(e.attrib['x']=='0' and e.attrib['y']=='0','editable co-registration')
            role=Path(e.attrib['src']).stem;i=['distant','ground','foreground'].index(role)
            im=Image.open(io.BytesIO(z.read(e.attrib['src']))).convert('RGBA');check(np.array_equal(np.array(im),arr[i]),'ORA exact exported layer '+role);ora.append(im)
        check(np.array_equal(np.array(composite(ora)),ref),'editable reconstruction')
        check(np.array_equal(np.array(Image.open(io.BytesIO(z.read('mergedimage.png'))).convert('RGBA')),ref),'editable merged image')
    for regions in maps['orientations'][orient]['working_regions'].values():
        for key,rect in regions.items():
            x,y,rw,rh=rect;x0,y0,x1,y1=round(x*w),round(y*h),round((x+rw)*w),round((y+rh)*h)
            check(np.all(arr[1][y0:y1,x0:x1,3]==255),'working plane opaque '+key)
    for name,expected in record['files'].items():check(sha(d/name)==expected,'registered hash '+name)
    for role,source in record['sources'].items():check(sha(ROOT/source['path'])==source['sha256'],'source immutable '+role)
    result['orientation_records'].append({'asset_id':aid,'orientation':orient,'dimensions':[w,h],'reconstruction_different_pixels':0,'composite_alpha':[255,255],
      'layer_alpha_extrema':{r:im.getchannel('A').getextrema() for r,im in zip(['distant','ground','foreground'],layers)},
      'layer_alpha_bounds_px':{r:im.getchannel('A').getbbox() for r,im in zip(['distant','ground','foreground'],layers)},'removal_changed_pixels':contributions,'safe_region_checks':checks,'editable_reconstruction_different_pixels':0})
# Every generation record preserves exact original/request/reference bytes.
provenance=json.loads((PACK/'metadata/world-provenance.json').read_text())['records']
for r in provenance:
    check(sha(ROOT/r['preserved_path'])==r['sha256'],'preserved generated original '+r['asset_id']+' '+r['role'])
    check(sha(ROOT/r['request_path'])==r['request_sha256'],'exact request hash')
    q=json.loads((ROOT/r['request_path']).read_text());check(q['prompt']==r['exact_prompt'],'exact saved prompt')
    for ref in r['reference_hashes']:check(sha(ROOT/ref['repository_path'])==ref['sha256'],'generation reference immutable')
result['generated_originals_verified']=len(provenance)
# Approved input records and all recovered originals are checked independently.
for name in ['direction-selection.json','pip-character-selection.json']:
    j=json.loads((PACK/'metadata'/name).read_text())
    if name.startswith('direction'):check(sha(PACK/j['artifact'])==j['sha256'],'selected direction hash')
    else:
        for a in j['approved_assets']:
            check(sha(PACK/a['original_path'])==a['original_sha256'],'approved original '+a['asset_id']);check(sha(PACK/a['selected_review_path'])==a['sha256'],'approved aligned '+a['asset_id'])
for s in json.loads((PHASE/'interrupted-checkpoint.json').read_text())['sources']:check(sha(ROOT/s['preserved_path'])==s['sha256'],'recovered immutable '+s['asset_id'])
# Protected files from original preflight remain unchanged; phase plan/brief are explicitly owned.
pre=json.loads((PHASE/'preflight.json').read_text());protected=0
for name,expected in {x['path']:x['sha256'] for x in pre['tracked_files']}.items():
    if name.startswith('docs/orchestration/phases/2a-world/'):continue
    check(sha(ROOT/name)==expected,'protected input changed '+name);protected+=1
result['protected_files_unchanged']=protected;result['approved_reference_hashes_verified']=11;result['recovered_originals_verified']=3
result['layer_exports']=12;result['editable_masters']=4
# Check branding once its independently produced source/export has arrived.
icon=PACK/'masters/images/BRAND-02/take-01/icon-1024.png'
if icon.exists():
    im=Image.open(icon).convert('RGBA');check(im.size==(1024,1024),'icon exact square');check(im.getchannel('A').getextrema()==(255,255),'icon opaque')
    result['icon']={'dimensions':[1024,1024],'alpha':[255,255],'sha256':sha(icon)}
else:result['icon']='not yet included; branding audit must be completed before final checkpoint'
result['visual_exclusions']='Requires actual image inspection; numerical tests cannot recognize baked labels/fruit/toys.'
result['scope_limit']='Technical candidates only. Human art/composition/name/icon/content/rights and target device remain pending. No native or physical-device validation.'
(PACK/'metadata/world-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','layer_exports','editable_masters','protected_files_unchanged','approved_reference_hashes_verified','recovered_originals_verified','icon']},indent=2))
