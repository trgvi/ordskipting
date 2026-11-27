# Listar orð úr gögnum sem skrá skiptir öðruvísi en gullið (orð með bandstrikum).
import sys;sys.path.insert(0,__file__.rsplit('/',1)[0])
from prof import skipta,stadir,les_min
dic,out=sys.argv[1],sys.argv[2];L,R=les_min(dic);bad=[]
for f in sys.argv[3:]:
    G=sorted({l.strip() for l in open(f,encoding='utf-8') if l.strip()})
    V=skipta(dic,[g.replace('-','') for g in G])
    bad+=[g for g,v in zip(G,V) if stadir(g,L,R)!=stadir(v,L,R)]
open(out,'w',encoding='utf-8').write('\n'.join(sorted(set(bad)))+'\n');print(len(set(bad)),'frávik')
