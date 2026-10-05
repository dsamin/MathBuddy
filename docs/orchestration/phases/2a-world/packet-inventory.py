#!/usr/bin/env python3
"""List every owned changed path and its immutable bytes, excluding self-hash."""
from pathlib import Path
import subprocess,json,hashlib
R=Path(__file__).resolve().parents[4];D=R/'docs/orchestration/phases/2a-world';out=D/'packet-files.json';base='e48eb490711d9754b6b6e123f1e069aebfeae3d7'
paths=set(subprocess.check_output(['git','diff','--name-only',base],cwd=R).decode().splitlines())
paths.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=R).decode().splitlines());paths.add(str(out.relative_to(R)))
entries=[]
for name in sorted(paths):
    p=R/name;e={'path':name}
    if p==out:e['note']='Inventory lists itself; self-hash excluded to avoid circularity.'
    else:e.update({'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
    entries.append(e)
out.write_text(json.dumps({'scope_base':base,'status':'complete-owned-path-inventory','paths':entries},indent=2)+'\n');print('Inventory:',len(entries),'owned changed paths')
