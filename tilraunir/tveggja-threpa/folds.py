import sys,hashlib;sys.path.insert(0,'/home/claude/ordskipting/tools')
from ohad import fjolskylda
T=[l.rstrip('\n') for l in open('/home/claude/ordskipting/smidi/thjalfun-samanburdur.txt',encoding='utf-8') if l.strip()]
K=5
def f(l): return int(hashlib.sha1(('cv:'+fjolskylda(l.replace('-',''))).encode()).hexdigest()[:8],16)%K
F=[f(l) for l in T]
for k in range(K):
    open(f'train{k}.latin1','w',encoding='latin-1').write('\n'.join(l for l,x in zip(T,F) if x!=k)+'\n')
    open(f'held{k}.txt','w',encoding='utf-8').write('\n'.join(l for l,x in zip(T,F) if x==k)+'\n')
print('ok')
