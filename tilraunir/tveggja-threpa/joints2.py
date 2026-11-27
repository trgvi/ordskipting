# Samskeyti, útgáfa 2: fæstir hlutar; jafntefli leyst með tíðni orðhluta í öðrum samsetningum.
import sys,collections,math
lexf,src,out=sys.argv[1:4];MIN=int(sys.argv[4]) if len(sys.argv)>4 else 4
LEX={l.strip().replace('-','').lower() for l in open(lexf,encoding='utf-8') if l.strip()}
def allsegs(w,cuts):
    pts=[0]+cuts+[len(w)];n=len(pts);res=[]
    def rec(i,acc):
        if i==n-1:
            if len(acc)>=2: res.append(acc[:])
            return
        for j in range(i+1,n):
            p=w[pts[i]:pts[j]]
            if len(p)>=MIN and p in LEX and not(i==0 and j==n-1):
                acc.append((pts[i],pts[j]));rec(j,acc);acc.pop()
    rec(0,[]);return res
rows=[]
for l in open(src,encoding='utf-8'):
    g=l.strip()
    if not g: continue
    w=g.replace('-','');c=[];k=0
    for p in g.split('-')[:-1]: k+=len(p);c.append(k)
    S=allsegs(w.lower(),c)
    if S: m=min(len(s) for s in S);S=[s for s in S if len(s)==m]
    rows.append((w,S))
F=collections.Counter()
for w,S in rows:
    for s in S:
        for a,b in s: F[w.lower()[a:b]]+=1/len(S)
O=[];nj=0;tie=0
for w,S in rows:
    if not S: O.append(w);continue
    if len(S)>1: tie+=1
    best=max(S,key=lambda s:min(F[w.lower()[a:b]] for a,b in s))
    nj+=1;O.append('-'.join(w[a:b] for a,b in best))
open(out,'w',encoding='utf-8').write('\n'.join(O)+'\n');print(len(O),'orð,',nj,'með samskeytum,',tie,'jafntefli')
