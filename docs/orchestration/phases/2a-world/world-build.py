#!/usr/bin/env python3
"""Reconstruct proposed Phase 2A raster-layer sources/exports without provider calls."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops
import json, hashlib, io, zipfile, math, sys
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[4]
PACK = ROOT / 'assets/production/picnic-v1'
PHASE = ROOT / 'docs/orchestration/phases/2a-world'
OUT = PACK / 'review/world-branding'
OUT.mkdir(parents=True, exist_ok=True)
META = PACK / 'metadata'
FONT = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 24)
SIZES = {'landscape': (2732,2048), 'portrait':(2048,2732)}
ROLES = ['distant','ground','foreground']
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save_json(path, value): path.write_text(json.dumps(value,indent=2)+'\n')
def png_bytes(im):
    b=io.BytesIO(); im.save(b,format='PNG'); return b.getvalue()
def px(rect,w,h):
    x,y,rw,rh=rect
    return (round(x*w),round(y*h),round((x+rw)*w),round((y+rh)*h))
def composite(layers):
    im=Image.new('RGBA',layers[0].size)
    for layer in layers: im=Image.alpha_composite(im,layer)
    return im

def safe_maps():
    catalog=json.loads((ROOT/'docs/planning/content-catalog.json').read_text())
    maps={}
    for orient in SIZES:
        common={'session-prompt':[.23,.025,.54,.07], 'given-reference':[.23,.12,.54,.17],
                'home':[.065,.025,.10,.075], 'listen':[.835,.025,.10,.075],
                'guide':[.065,.56,.15,.27], 'answer-choices':[.26,.805,.66,.055],
                'persistent-controls':[.24,.885,.70,.08]}
        if orient=='landscape':
            regs={'LAYOUT-COUNT':{'tray':[.26,.38,.31,.40],'basket':[.61,.38,.31,.40]},
                  'LAYOUT-TAKE':{'source-mat':[.26,.38,.31,.40],'friend-plate':[.61,.38,.31,.40]},
                  'LAYOUT-JOIN':{'left-group':[.26,.36,.31,.20],'right-group':[.61,.36,.31,.20],'shared-mat':[.34,.60,.53,.18]}}
        else:
            regs={'LAYOUT-COUNT':{'tray':[.26,.35,.66,.20],'basket':[.26,.59,.66,.20]},
                  'LAYOUT-TAKE':{'source-mat':[.26,.35,.66,.20],'friend-plate':[.26,.59,.66,.20]},
                  'LAYOUT-JOIN':{'left-group':[.26,.35,.31,.20],'right-group':[.61,.35,.31,.20],'shared-mat':[.30,.60,.59,.19]}}
        garden={'pinwheel-including-full-rotor':[.27,.36,.27,.26], 'free-flower-states':[.65,.36,.22,.25],
                'decor-01':[.27,.66,.12,.15], 'decor-02':[.41,.66,.12,.15],
                'decor-03':[.55,.66,.12,.15], 'decor-04-bunting':[.26,.30,.65,.045],
                'decor-05':[.70,.66,.20,.15], 'finish':[.40,.885,.34,.08]}
        projected={}
        for layout in catalog['layout_definitions']:
            lid=layout['id'];projected[lid]={}
            assert set(regs[lid])==set(layout['orientations'][orient]['regions'])
            for region, value in layout['orientations'][orient]['regions'].items():
                x,y,w,h=regs[lid][region]
                projected[lid][region]=[{'slot_id':s['slot_id'],'canvas_normalized_anchor':[x+s['normalized_anchor']['x']*w,y+s['normalized_anchor']['y']*h]} for s in value['slot_definitions']]
        union={**common}
        for layout,regions in regs.items():
            union.update({layout+'/'+key:rect for key,rect in regions.items()})
        union.update({'garden/'+key:rect for key,rect in garden.items()})
        maps[orient]={'canvas_px':SIZES[orient],'common':common,'working_regions':regs,'garden':garden,'union':union,'projected_slots':projected}
    return {'status':'proposed-phase-2a-composition-coordinates-not-canonical-screen-layout',
            'coordinates':'Top-left origin, x/y normalized to full orientation canvas. Rectangles [x,y,width,height]; pixel bounds round endpoints. Catalog slots remain region-relative. canvas_anchor=(rect.x+u*rect.width,rect.y+v*rect.height); pixels=(anchor.x*W,anchor.y*H). Same slot and instance IDs survive reproject; no rotation move inferred.',
            'clearance':'Foreground must have zero alpha in every semantic rectangle enlarged by 0.015 canvas units on each side. Worlds reserve union of all three activity families AND garden/M06/M07. Scene horizon sits above working pieces; reference has quiet sky. Diagnostic outlines are separate from art.',
            'device_limit':'80–88 pt touch-space, physical iPad, larger-text/native reflow and actual object/prop silhouette fit remain unverified until target device and Phase2B/2C assets exist. These pixels do not prove interaction usability.',
            'orientation_policy':'Distinct registered canvases from common independent source layers, not central crops of a flat board. Full distant source mapped to top 38%; full ground material mapped to canvas with analytic horizon mask; foreground source alpha bounding box reprojected to left/right edge strips. Raster sources resampled, not native-detail 2732 px provider output.',
            'orientations':maps}

def make_layers(asset,orient):
    w,h=SIZES[orient];folder=PACK/f'masters/images/{asset}/take-01'
    sources={'distant':folder/'recovered-distant-original.png','ground':folder/'ground-original.png','foreground':PACK/f'masters/images/{asset}/take-02/foreground-original.png'}
    original={key:Image.open(p).convert('RGBA') for key,p in sources.items()}
    distant=Image.new('RGBA',(w,h));distant.alpha_composite(original['distant'].resize((w,round(h*.38)),Image.Resampling.LANCZOS),(0,0))
    ground=original['ground'].resize((w,h),Image.Resampling.LANCZOS)
    # Author an editable alpha mask over the independent ground material, not a scene extraction.
    mask=Image.new('L',(w,h));md=ImageDraw.Draw(mask)
    points=[(round(i*w/200),round(h*(.337+.009*math.sin(i/200*math.pi*2+.3)))) for i in range(201)]
    md.polygon(points+[(w,h),(0,h)],fill=255);ground.putalpha(mask)
    source=original['foreground'];bounds=source.getchannel('A').point(lambda a: 255 if a > 1 else 0).getbbox()
    if not bounds: raise ValueError('Foreground source has no alpha contribution')
    if source.getchannel('A').getextrema()[0]!=0: raise ValueError('Foreground source lacks genuine transparency; tool repair required')
    crop=source.crop(bounds)
    foreground=Image.new('RGBA',(w,h));target=(round(w*.04),round(h*.57))
    edge=crop.resize(target,Image.Resampling.LANCZOS)
    foreground.alpha_composite(edge,(0,round(h*.43)))
    foreground.alpha_composite(edge.transpose(Image.Transpose.FLIP_LEFT_RIGHT),(w-target[0],round(h*.43)))
    layers=[distant,ground,foreground];recon=composite(layers)
    dest=PACK/f'masters/images/{asset}/take-02/{orient}';dest.mkdir(exist_ok=True)
    for role,im in zip(ROLES,layers):im.save(dest/f'{role}.png')
    recon.save(dest/'composite.png')
    # OpenRaster contains genuine full-size separate registered raster layers.
    xml=ET.Element('image',{'w':str(w),'h':str(h),'name':asset+' '+orient+' proposed take-02','version':'0.0.3'});stack=ET.SubElement(xml,'stack')
    for role,z in [('foreground',60),('ground',10),('distant',0)]:
        ET.SubElement(stack,'layer',{'name':role+' z'+str(z),'src':'data/'+role+'.png','x':'0','y':'0','opacity':'1.0','visibility':'visible','composite-op':'svg:src-over'})
    def entry(z,name,data,compress=zipfile.ZIP_DEFLATED):
        zi=zipfile.ZipInfo(name,(1980,1,1,0,0,0));zi.compress_type=compress;z.writestr(zi,data)
    with zipfile.ZipFile(dest/'editable.ora','w') as z:
        entry(z,'mimetype',b'image/openraster',zipfile.ZIP_STORED)
        entry(z,'stack.xml',ET.tostring(xml))
        for role,im in zip(ROLES,layers):entry(z,'data/'+role+'.png',png_bytes(im))
        entry(z,'mergedimage.png',png_bytes(recon));entry(z,'Thumbnails/thumbnail.png',png_bytes(recon.resize((256,round(256*h/w)),Image.Resampling.LANCZOS)))
    return {'asset_id':asset,'orientation':orient,'take_id':'take-02','canvas_px':[w,h], 'origin_px':[0,0], 'z_order':{'distant':0,'ground':10,'foreground':60},
            'sources':{k:{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'dimensions':list(original[k].size)} for k,p in sources.items()},
            'registration':{'distant':'whole source resized to [0,0,W,round(.38H)]','ground':'whole independent source resized W,H; alpha horizon y/H=.337+.009*sin(2*pi*x/W+.3)','foreground':{'source_alpha_crop_px':bounds,'bounds_threshold':'alpha > 1; faint alpha=1 dust outside silhouette excluded by crop only; retained pixels keep original alpha','placements_px':[[0,round(h*.43),*target],[w-target[0],round(h*.43),*target]],'right':'mirrored left source, same logical edge layer','crop':'Artwork intentionally reaches canvas edge; alpha bbox crop removes only transparent padding. No semantic crop.'}},
            'files':{f.name:sha(f) for f in dest.iterdir() if f.is_file()}}

def preview(asset,orient,maps):
    w,h=SIZES[orient];dest=PACK/f'masters/images/{asset}/take-02/{orient}'
    clean=Image.open(dest/'composite.png').convert('RGBA');scale=1000/w
    small=clean.resize((1000,round(h*scale)),Image.Resampling.LANCZOS)
    small.convert('RGB').save(OUT/f'{asset}-{orient}-clean.jpg',quality=94)
    # Transparent layers visible against checkerboard, full-canvas registration preserved.
    thumb_size=(500,round(500*h/w));sheet=Image.new('RGB',(1548,thumb_size[1]+105),'#fbf6ed');draw=ImageDraw.Draw(sheet)
    for i,role in enumerate(ROLES):
        check=Image.new('RGBA',thumb_size,'#f0e8dc');d=ImageDraw.Draw(check)
        for y in range(0,thumb_size[1],24):
            for x in range(0,500,24):
                if (x//24+y//24)%2:d.rectangle([x,y,x+23,y+23],fill='#d4dcda')
        layer=Image.open(dest/f'{role}.png').convert('RGBA').resize(thumb_size,Image.Resampling.LANCZOS)
        check=Image.alpha_composite(check,layer);sheet.paste(check.convert('RGB'),(i*516,80));draw.text((i*516+12,45),role+' / z'+str([0,10,60][i]),font=FONT,fill='#243e34')
    draw.text((12,8),asset+' '+orient+' — registered independent layers',font=FONT,fill='#243e34');sheet.save(OUT/f'{asset}-{orient}-exploded.png')
    for family in ['union','LAYOUT-COUNT','LAYOUT-JOIN','LAYOUT-TAKE','garden']:
        ann=small.copy();d=ImageDraw.Draw(ann)
        om=maps['orientations'][orient]
        rects=om['union'] if family=='union' else ({**om['common'],**om['working_regions'][family]} if family.startswith('LAYOUT') else {**om['common'],**om['garden']})
        for idx,(name,rect) in enumerate(rects.items()):
            x0,y0,x1,y1=px(rect,*small.size);color=['#284e83','#86395d','#345d32'][idx%3]
            d.rectangle([x0,y0,x1,y1],outline=color,width=3)
            # Numeric labels are diagnostic indexes, never baked into clean art.
            d.rectangle([x0,y0,x0+28,y0+25],fill='#fff9ef');d.text((x0+3,y0),str(idx+1),font=FONT,fill=color)
        ann.convert('RGB').save(OUT/f'{asset}-{orient}-{family}-clearance.jpg',quality=93)
        (OUT/f'{asset}-{orient}-{family}-legend.json').write_text(json.dumps({str(i+1):{'name':name,'rect':rect} for i,(name,rect) in enumerate(rects.items())},indent=2)+'\n')

if __name__=='__main__':
    maps=safe_maps();save_json(META/'world-safe-regions.json',maps)
    records=[]
    for asset in ['ENV-01','ENV-02']:
        for orient in SIZES:
            records.append(make_layers(asset,orient));preview(asset,orient,maps)
    save_json(META/'world-registration.json',{'status':'technical-candidate-human-acceptance-pending','source_kind':'six current separately generated original raster artworks; editable OpenRaster masters with independent registered layers; no claim of vector/editable-object source or articulated scene rig','reproduce':'python3 docs/orchestration/phases/2a-world/world-build.py (Pillow 12.1.1)','records':records})
    print('Built 12 independent registered orientation layers, four OpenRaster masters and diagnostic previews.')
