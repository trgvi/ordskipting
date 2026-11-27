import json,collections,sys
err=json.load(open('err.json'))
T=[l.strip() for l in open('/home/claude/ordskipting/smidi/thjalfun-samanburdur.txt',encoding='utf-8') if l.strip()]
LR=[(l,r) for l in (1,2,3,4) for r in (1,2,3,4)]
def ctx(s,j,l,r):
    if j-l<0 or j+r>len(s): return None
    return s[j-l:j]+'|'+s[j:j+r]
good=collections.defaultdict(set)
for i,(w,c) in enumerate(err):
    s='.'+w+'.';j=c+1
    for l,r in LR:
        k=ctx(s,j,l,r)
        if k: good[k].add(i)
cand=set(good)
bad=collections.Counter()
for g in T:
    w=g.replace('-','').lower();s='.'+w+'.';n=0
    for p in g.split('-')[:-1]:
        n+=len(p);j=n+1
        for l,r in LR:
            k=ctx(s,j,l,r)
            if k in cand: bad[k]+=1
MINGOOD=int(sys.argv[1]);RATIO=float(sys.argv[2])
ok=[k for k in cand if len(good[k])>=MINGOOD and len(good[k])>=RATIO*bad[k]]
# gráðugt val: stystu/almennustu fyrst eftir þekju
chosen=[];covered=set()
for k in sorted(ok,key=lambda k:(-(len(good[k])-bad[k]),len(k))):
    newc=good[k]-covered
    if len(newc)>=MINGOOD and len(newc)>=RATIO*bad[k]: chosen.append(k);covered|=newc
print('valin mynstur',len(chosen),'þekja',len(covered),'af',len(err))
json.dump([(k,len(good[k])) for k in chosen],open(f'chosen_{MINGOOD}_{RATIO}.json','w'),ensure_ascii=False)
print([ (k,len(good[k]),bad[k]) for k in chosen[:15]])
