"""Rebuild provisional brand review assets; never writes recovered originals."""
from pathlib import Path
import argparse,base64,hashlib,json,platform
from PIL import Image, ImageDraw, ImageFont, __version__ as pillow_version
ROOT=Path(__file__).resolve().parents[1]
B1=ROOT/'masters/images/BRAND-01/take-01'
B2=ROOT/'masters/images/BRAND-02/take-01'
RECIPE=ROOT/'metadata/world-brand-wordmark-recipe.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def wordmark(width):
 r=json.loads(RECIPE.read_text()); scale=width/1100
 im=Image.new('RGBA',(width,round(240*scale)),(0,0,0,0))
 font=ImageFont.truetype(str(B1/r['font']['filename']),round(140*scale))
 ImageDraw.Draw(im).text((round(550*scale),round(160*scale)),r['text'],anchor='ms',font=font,fill=r['recipe']['color'])
 return im

def build():
 r=json.loads(RECIPE.read_text());assert sha(B1/r['font']['filename'])==r['font']['sha256']
 data=base64.b64encode((B1/r['font']['filename']).read_bytes()).decode()
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 240" role="img" aria-labelledby="title"><title id="title">Pip’s Picnic — provisional wordmark</title><style>@font-face{{font-family:PicnicRubik;src:url(data:font/ttf;base64,{data}) format('truetype');font-weight:700;}}text{{font-family:PicnicRubik;font-weight:700;}}</style><text x="550" y="160" text-anchor="middle" font-size="140" fill="#365444">Pip’s Picnic</text></svg>'''
 (B1/'wordmark-editable.svg').write_text(svg+'\n')
 for w in (240,360,720,1100):wordmark(w).save(B1/f'wordmark-{w}.png')
 origin=B2/'recovered-icon-original.png';assert sha(origin)=='1a6ea126084e074f33d1d6c5446ad5d134143e0598d9c55c0050f6a0cdbfb888'
 im=Image.open(origin);assert im.size==(1254,1254) and im.mode=='RGB'
 im.resize((1024,1024),Image.Resampling.LANCZOS).convert('RGB').save(B2/'icon-1024.png')
 sheet=Image.new('RGB',(1000,450),'#faf7ee');d=ImageDraw.Draw(sheet)
 font=ImageFont.truetype(str(B1/'source/Rubik-Bold.ttf'),18)
 d.text((24,18),'Provisional icon · native sizes + enlarged pixel inspection',font=font,fill='#34463c')
 for x,n in zip([30,265,500,735],[16,32,64,128]):
  small=im.resize((n,n),Image.Resampling.LANCZOS).convert('RGB');small.save(B2/f'icon-{n}.png')
  sheet.paste(small,(x,90));sheet.paste(small.resize((192,192),Image.Resampling.NEAREST),(x,240));d.text((x,56),f'{n} × {n}',font=font,fill='#34463c')
 sheet.save(B2/'icon-small-size-sheet.png')
 sheet=Image.new('RGB',(1300,1000),'#faf7ee');d=ImageDraw.Draw(sheet)
 font=ImageFont.truetype(str(B1/'source/Rubik-Bold.ttf'),24)
 d.text((48,30),'BRAND-01 / BRAND-02 · provisional review',font=font,fill='#365444')
 d.text((48,82),'Rubik Bold 1.100 · working name only · human acceptance pending',font=ImageFont.truetype(str(B1/'source/Rubik-Bold.ttf'),20),fill='#365444')
 sheet.paste(Image.open(B2/'icon-1024.png').resize((400,400),Image.Resampling.LANCZOS),(48,146))
 wm=wordmark(720);sheet.paste(wm,(502,242),wm)
 d.text((502,416),'Editable text + licensed bundled font; no outline claim.',font=ImageFont.truetype(str(B1/'source/Rubik-Bold.ttf'),18),fill='#365444')
 for y,w in zip((588,693,798),(240,360,720)):
  wm=wordmark(w);sheet.paste(wm,(48,y),wm);d.text((900,y+12),f'{w}px width',font=font,fill='#365444')
 d.text((48,948),'Icon, name, font, device targets and provider rights remain pending.',font=ImageFont.truetype(str(B1/'source/Rubik-Bold.ttf'),20),fill='#365444')
 sheet.save(B1/'branding-sheet.png')
 files=[p for folder in (B1,B2) for p in sorted(folder.rglob('*')) if p.is_file()]
 manifest={'status':'technical-only-human-acceptance-pending','runtime':{'python':platform.python_version(),'pillow':pillow_version,'resample':'Pillow Resampling.LANCZOS','typography':'Pillow FreeType native font rendering; editable SVG embeds same unmodified font but is not outlined'},'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]}
 (ROOT/'metadata/world-brand-file-audit.json').write_text(json.dumps(manifest,indent=2)+'\n')
 audit()
def audit():
 r=json.loads(RECIPE.read_text());assert sha(B1/r['font']['filename'])==r['font']['sha256']
 a=json.loads((ROOT/'metadata/world-brand-file-audit.json').read_text())
 for entry in a['files']:assert sha(ROOT/entry['path'])==entry['sha256'],entry['path']
 im=Image.open(B2/'icon-1024.png');im.load();assert im.size==(1024,1024) and im.mode=='RGB'
 for n in (16,32,64,128):
  im=Image.open(B2/f'icon-{n}.png');im.load();assert im.size==(n,n) and im.mode=='RGB'
 for w in (240,360,720,1100):
  im=Image.open(B1/f'wordmark-{w}.png');im.load();assert im.size==(w,round(240*w/1100)) and im.mode=='RGBA'
  bbox=im.getbbox();assert bbox and bbox[0]>0 and bbox[2]<im.width and bbox[1]>0 and bbox[3]<im.height
 result={'status':'pass-technical-only','checks':['all manifest hashes match','original icon preserved','1024 square icon RGB fully opaque','four decoded opaque small sizes','four decoded transparent wordmark sizes with unclipped bounds','font hash and license bundled'],'human_acceptance':'pending','SVG_note':'Native text recipe is acceptance deliverable. SVG is editable text and embeds the same font; no outlined-vector or cross-renderer equivalence claim.'}
 (ROOT/'metadata/world-brand-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--audit-only',action='store_true');args=parser.parse_args()
 audit() if args.audit_only else build()
