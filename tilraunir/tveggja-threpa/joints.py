# Leiðir út samskeyti: skiptistaðir úr gulli þar sem allir hlutar eru sjálfstæð orð í orðasafninu.
# Fæstir hlutar vinna (heldur framleiðandi heilu frekar en fram|leiðandi).
import sys
lex_files=sys.argv[1:-2];src,out=sys.argv[-2],sys.argv[-1]
LEX=set()
for f in lex_files:
    for l in open(f,encoding='utf-8'):
        w=l.strip().replace('-','').lower()
        if w: LEX.add(w)
MIN=3
def seg(w,cuts):
    pts=[0]+cuts+[len(w)];n=len(pts)
    best={0:(0,[])}
    for j in range(1,n):
        for i in range(j):
            if i in best:
                p=w[pts[i]:pts[j]]
                if len(p)>=MIN and p in LEX and not (i==0 and j==n-1):
                    c=(best[i][0]+1,best[i][1]+[pts[j]])
                    if j not in best or c[0]<best[j][0]: best[j]=c
    # heila orðið án samskeyta ef engin skipting finnst
    if n-1 in best and best[n-1][0]>=2: return best[n-1][1][:-1]
    return []
O=[];nj=0
for l in open(src,encoding='utf-8'):
    g=l.strip()
    if not g: continue
    w=g.replace('-','');c=[];k=0
    for p in g.split('-')[:-1]: k+=len(p);c.append(k)
    j=seg(w.lower(),c);nj+=bool(j)
    s='';prev=0
    for x in j: s+=w[prev:x]+'-';prev=x
    O.append(s+w[prev:])
open(out,'w',encoding='utf-8').write('\n'.join(O)+'\n');print(len(O),'orð,',nj,'með samskeytum')
