import sys;sys.path.insert(0,'/home/claude/ordskipting/tools')
from prof import skipta,stadir
a,b,f=sys.argv[1:4]
G=[l.strip() for l in open(f,encoding='utf-8') if l.strip()]
A=skipta(a,[g.replace('-','') for g in G]);B=skipta(b,[g.replace('-','') for g in G])
better=worse=0;W=[];Bt=[]
for g,x,y in zip(G,A,B):
    ca,cb,cg=stadir(x,2,3),stadir(y,2,3),stadir(g,2,3)
    ea=len(ca-cg)*2+len(cg-ca);eb=len(cb-cg)*2+len(cg-cb)
    if eb>ea: W.append((g,x,y))
    elif eb<ea: Bt.append((g,x,y))
print('betra',len(Bt),'verra',len(W))
for r in W[:int(sys.argv[4]) if len(sys.argv)>4 else 30]: print('VERRA  gull',r[0],' A',r[1],' B',r[2])
for r in Bt[:15]: print('BETRA  gull',r[0],' A',r[1],' B',r[2])
