# Jafngildi substrings.pl úr libhyphen: bætir við öllum hlutstrengjum mynstra með sameinuðum gildum
import sys,re
src,dst=sys.argv[1],sys.argv[2]
lines=open(src,encoding='utf-8').read().split('\n')
head=[lines[0]];meta=[];pats={}
def parse(l):
  key=re.sub(r'\d','',l);pts=[0]*(len(key)+1);j=0
  for ch in l:
    if ch.isdigit():pts[j]=int(ch)
    else:j+=1
  return key,pts
for l in lines[1:]:
  l=l.strip()
  if not l or l.startswith('%'):continue
  if re.match(r'^[A-Z]',l): meta.append(l);continue
  k,p=parse(l)
  if k in pats: pats[k]=[max(a,b) for a,b in zip(pats[k],p)]
  else: pats[k]=p
keys=set(pats)
for k in list(pats):
  for i in range(len(k)):
    for j in range(i+1,len(k)+1): keys.add(k[i:j])
maxlen=max(map(len,pats))
out={}
for k in keys:
  v=[0]*(len(k)+1)
  for i in range(len(k)):
    for j in range(i+1,min(len(k),i+maxlen)+1):
      q=pats.get(k[i:j])
      if q:
        for t,x in enumerate(q): v[i+t]=max(v[i+t],x)
  out[k]=v
def fmt(k,v): return ''.join((str(v[i]) if v[i] else '')+k[i] for i in range(len(k)))+(str(v[-1]) if v[-1] else '')
with open(dst,'w',encoding='utf-8') as f:
  f.write('\n'.join(head+meta)+'\n')
  for k in sorted(out): f.write(fmt(k,out[k])+'\n')
print(len(pats),'->',len(out))
