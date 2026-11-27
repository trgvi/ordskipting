import sys,collections,json;sys.path.insert(0,'/home/claude/ordskipting/tools')
from prof import skipta
def cuts(s):
    n=0;c=[]
    for p in s.split('-')[:-1]: n+=len(p);c.append(n)
    return c
L,R=2,3
err=[]  # (word, wrong cut index, gold cuts)
tot=fr=0
for k in range(5):
    G=[l.strip() for l in open(f'held{k}.txt',encoding='utf-8') if l.strip()]
    V=skipta(f'd{k}.dic',[g.replace('-','') for g in G])
    for g,v in zip(G,V):
        w=g.replace('-','').lower();n=len(w)
        cv=[c for c in cuts(v) if L<=c<=n-R]; cg=set(c for c in cuts(g) if L<=c<=n-R)
        b=[0]+cv+[n];tot+=1
        # einstafsbútur: innri hluti af lengd 1
        fr_cuts=set()
        for a,bb in zip(b,b[1:]):
            if bb-a==1 and a>0 and bb<n: fr_cuts|={a,bb}
        if fr_cuts: fr+=1
        for c in fr_cuts:
            if c not in cg: err.append((w,c))
print('orð',tot,'með einstafsbút',fr,'rangir skiptistaðir í bútum',len(err))
json.dump(err,open('err.json','w'))
