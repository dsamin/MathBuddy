#!/usr/bin/env python3
"""Generate the authored MathBuddy pilot narration once; preserve takes and metadata."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse, array, hashlib, json, math, os, re, shutil, subprocess, sys, wave
ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get('MATHBUDDY_VOICE_PYTHON', sys.executable)
SCRIPTS = {
 'welcome': "Hi, friend! Let's make something wonderful with Pip.",
 'count-3': 'Help Pip pack three berries. Tap a berry to put it in the basket.',
 'count-4': 'Help Pip pack four berries. Tap a berry to put it in the basket.',
 'count-5': 'Help Pip pack five berries. Tap a berry to put it in the basket.',
 'add-2-1': 'Here are two berries. One more joins. Put them together.',
 'add-1-2': 'Here is one berry. Two more join. Put them together.',
 'subtract-5-2': 'We have five berries. Give two berries to Pip.',
 'choose-total': 'How many berries are there altogether?',
 'choose-remaining': 'How many berries are left on your mat?',
 'help-count': "Let's count each berry, one at a time. You can change your answer.",
 'success': 'You did it! Look what you made.',
 'garden': 'A new pinwheel for your garden! Plant it, then tap it to spin.',
 'goodbye': 'That was lovely. Your garden will be here when you come back.',
 **{f'number-{n}':str(n)+'.' for n in range(1,7)}
}
DIRECTION = ('Speak as a warm, calm adult companion for a child aged five. Natural conversational US English, '
             'clear number words, gentle curiosity, moderate slightly slow pace, short natural pauses. '
             'No music, no character voices, no sing-song delivery, no added words. Say only the supplied text.')

RECOVERY_IDS = ('garden', 'goodbye', 'number-1', 'number-3', 'number-4', 'number-5', 'number-6')

def synthesize_once(key, req, master):
 env=os.environ.copy()
 try:
  proc=subprocess.run([PYTHON,str(ROOT/'scripts/generate_voice_clip.py'),str(req),str(master)],env=env,capture_output=True,text=True,timeout=80)
 except subprocess.TimeoutExpired:
  return {'id':key,'status':'generation-failed','failureCategory':'subprocess-timeout'}
 if proc.returncode:
  # Only retain the generator's intentionally safe exception class, never raw provider stderr.
  match=re.search(r'Google synthesis failed \(([A-Za-z_][A-Za-z_0-9]*)\)',proc.stderr)
  category=match.group(1) if match else 'unclassified-generator-error'
  return {'id':key,'status':'generation-failed','exitCode':proc.returncode,'failureCategory':category}
 return {'id':key,'status':'generated-master'}

def recover_missing_once():
 results=[]
 for key in RECOVERY_IDS:
  master=ROOT/'assets/audio/masters'/f'{key}.wav'
  marker=ROOT/'assets/audio/masters'/f'{key}.recovery-attempt.json'
  if master.exists():
   result={'id':key,'status':'existing-master-preserved'}
  elif marker.exists():
   result={'id':key,'status':'recovery-already-attempted'}
  else:
   marker.write_text(json.dumps({'assetID':key,'explicitRecoveryPass':True,'paidRequestAttempted':True})+'\n')
   result=synthesize_once(key,ROOT/'assets/audio/requests'/f'{key}.json',master)
   marker.write_text(json.dumps({'assetID':key,'explicitRecoveryPass':True,'paidRequestAttempted':True,**result},indent=2)+'\n')
  results.append(result)
  print(json.dumps(result),flush=True)
 (ROOT/'assets/audio/recovery-pass.json').write_text(json.dumps({'automaticPaidRetries':False,'sequential':True,'clips':results},indent=2)+'\n')

def generate(item):
 key,text=item
 request={'assetID':key,'text':text,'prompt':DIRECTION,'model':'gemini-2.5-pro-tts','voice':'Fenrir','language':'en-US'}
 req=ROOT/'assets/audio/requests'/f'{key}.json'; req.write_text(json.dumps(request,indent=2)+'\n')
 master=ROOT/'assets/audio/masters'/f'{key}.wav'
 attempt=ROOT/'assets/audio/masters'/f'{key}.attempt.json'
 if not master.exists():
  if attempt.exists():
   recovery=ROOT/'assets/audio/masters'/f'{key}.recovery-attempt.json'
   outcome=json.loads((recovery if recovery.exists() else attempt).read_text())
   return {'id':key,'status':'prior-attempt-not-retried','failureCategory':outcome.get('failureCategory','not-recorded-in-original-attempt')}
  attempt.write_text(json.dumps({'assetID':key,'paidRequestAttempted':True})+'\n')
  outcome=synthesize_once(key,req,master)
  attempt.write_text(json.dumps({'assetID':key,'paidRequestAttempted':True,**outcome},indent=2)+'\n')
  if outcome['status']=='generation-failed': return outcome
 with wave.open(str(master)) as wav:
  frames=wav.getnframes();rate=wav.getframerate(); channels=wav.getnchannels();width=wav.getsampwidth()
  samples=array.array('h',wav.readframes(frames))
  assert rate==24000 and channels==1 and width==2 and frames>0
  assert max(abs(x) for x in samples)>0
 dest=ROOT/'MathBuddy/Resources/Audio'/master.name
 shutil.copyfile(master,dest)
 return {'id':key,'status':'generated-bundled-draft','durationSeconds':round(frames/rate,3),'sha256':hashlib.sha256(master.read_bytes()).hexdigest(),'reviewStatus':'awaiting-human-listening'}

def effects():
 rate=24000
 for name,notes in {'pickup':[(660,.10)],'success':[(523.25,.13),(659.25,.13),(783.99,.22)],'reward':[(392,.13),(523.25,.13),(659.25,.13),(783.99,.34)]}.items():
  data=array.array('h')
  for frequency,duration in notes:
   count=int(rate*duration)
   for i in range(count):
    t=i/rate; envelope=min(t/.015,1)*max(0,1-t/duration)**2
    sample=.22*envelope*(math.sin(2*math.pi*frequency*t)+.18*math.sin(4*math.pi*frequency*t))
    data.append(int(32767*sample))
  path=ROOT/'MathBuddy/Resources/Audio'/f'effect-{name}.wav'
  with wave.open(str(path),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate);w.writeframes(data.tobytes())

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--recover-missing-once',action='store_true',help='One explicit sequential recovery pass for the seven failed first-batch clips; existing takes are preserved')
 args=parser.parse_args()
 if args.recover_missing_once:
  recover_missing_once()
  raise SystemExit(0)
 effects()
 with ThreadPoolExecutor(max_workers=2) as pool:
  results=list(pool.map(generate,SCRIPTS.items()))
 report={'provider':'Google Cloud Text-to-Speech','model':'gemini-2.5-pro-tts','voice':'Fenrir','source':'Authored MathBuddy scripts only; shared local provider authentication; no child data','reviewStatus':'Generated draft for native review, not approved for learning release','clips':results,'effects':'Three original synthesized PCM chimes, no third-party samples','automaticPaidRetries':False}
 (ROOT/'assets/audio/manifest.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'total':len(results),'bundled':sum(r['status']=='generated-bundled-draft' for r in results),'failed':[r['id'] for r in results if r['status']!='generated-bundled-draft']}))
