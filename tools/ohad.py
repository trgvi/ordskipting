# Býr til fast óháð lokaprófunarsafn með heilum orðafjölskyldum utan þjálfunar.
# Fjölskylda = nálgaður stofn síðasta orðhluta + allt á undan (sjá fjolskylda()).
import sys,random,hashlib,unicodedata
END=sorted('''ingunum ingarnar ingunni ingunum ingana ingarinnar inganna ingum ingin ingu ingar inga ing
unum unni unin unar una un
anna arnar ana ann ans an inn inum ins inni innar ina inu in ið
urnar urinn urnum urum urs ur
ri rar ra rum ir ar um i a u s r'''.split(),key=len,reverse=True)
def fjolskylda(w):
    w=w.lower()
    for e in END:
        if w.endswith(e) and len(w)-len(e)>=4: return w[:-len(e)]
    return w
def hopur(key,hl=.02):
    # fast, endurtakanlegt: sama fjölskylda lendir alltaf í sama safni
    h=int(hashlib.sha1(('ordskipting:'+key).encode()).hexdigest()[:8],16)/0xffffffff
    return 'lokaprof' if h<hl else 'throun' if h<2*hl else 'thjalfun'
if __name__=='__main__':
    full,train,odir=sys.argv[1:4]; hl=float(sys.argv[4]) if len(sys.argv)>4 else .02
    F=[unicodedata.normalize('NFC',l.strip()) for l in open(full,encoding='utf-8') if l.strip()]
    S={'lokaprof':set(),'throun':set()}
    for g in F:
        h=hopur(fjolskylda(g.replace('-','')),hl)
        if h in S: S[h].add(g)
    utan={fjolskylda(g.replace('-','')) for s in S.values() for g in s}
    T=[l.rstrip('\n') for l in open(train,encoding='utf-8') if l.strip()]
    kept=[l for l in T if fjolskylda(l.replace('-','')) not in utan]
    for k,v in S.items(): open(f'{odir}/{k}.txt','w',encoding='utf-8').write('\n'.join(sorted(v))+'\n')
    open(f'{odir}/thjalfun-samanburdur.txt','w',encoding='utf-8').write('\n'.join(kept)+'\n')
    for k,v in S.items(): print(f'{k}: {len(v)} orð í {len({fjolskylda(g.replace("-","")) for g in v})} fjölskyldum')
    print(f'þjálfun: {len(T)} -> {len(kept)}')
