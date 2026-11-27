import sys;sys.path.insert(0,'/home/claude/ordskipting/tools')
from prof import skipta,stadir
a,b,f=sys.argv[1:4]
G=[l.strip() for l in open(f,encoding='utf-8') if l.strip()]
A=skipta(a,[g.replace('-','') for g in G]);B=skipta(b,[g.replace('-','') for g in G])
nw=[];gone=[]
for g,x,y in zip(G,A,B):
    ca,cb,cg=stadir(x,2,3),stadir(y,2,3),stadir(g,2,3)
    if (cb-cg)-(ca-cg): nw.append((g,x,y))
    if (ca-cg)-(cb-cg): gone.append((g,x,y))
print('nýir rangir í',len(nw),'orðum; rangir horfnir í',len(gone))
for r in nw: print('NÝTT RANGT gull',r[0],' A',r[1],' B',r[2])
