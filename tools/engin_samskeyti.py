# Þrep-1 bann: engin samskeyti í orðum sem hafa undantekningu (.orð.) eða eru talin upp í skrá (orð með bandstrikum).
import sys,re
out=[]
for f in sys.argv[2:]:
    for l in open(f,encoding='utf-8').read().split('\n'):
        l=l.strip()
        if l.startswith('.') and l.endswith('.'): w=re.sub(r'\d','',l).strip('.')
        elif l and not l.startswith('%') and not re.search(r'\d',l): w=l.replace('-','').lower()
        else: continue
        out.append('.'+'8'.join(w)+'.')
open(sys.argv[1],'w',encoding='utf-8').write('\n'.join(sorted(set(out)))+'\n');print(len(set(out)),'orð án samskeyta')
