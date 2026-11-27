# Tekur út undantekningar (.orð.) sem tilheyra fjölskyldum í prófunarsöfnum.
import sys,re
sys.path.insert(0,__file__.rsplit('/',1)[0])
from ohad import fjolskylda
undant,ut=sys.argv[1],sys.argv[2];prof=sys.argv[3:]
keys={fjolskylda(l.strip().replace('-','')) for f in prof for l in open(f,encoding='utf-8') if l.strip()}
out=[];n=0
for l in open(undant,encoding='utf-8').read().split('\n'):
    if l.startswith('.') and l.endswith('.') and fjolskylda(re.sub(r'\d','',l).strip('.')) in keys: n+=1;continue
    out.append(l)
open(ut,'w',encoding='utf-8').write('\n'.join(out));print(f'{n} undantekningar teknar út vegna prófunarsafna')
