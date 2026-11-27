# Mælir orðskiptiskrá gegn prófunarsafni (orð með bandstrikum, UTF-8).
# Notar libhyphen beint, með sömu LEFTHYPHENMIN/RIGHTHYPHENMIN og skráin.
import sys,ctypes,re
V=set('aeiouyáéíóúýæö')
def les_min(dic):
    L=R=2
    for l in open(dic,encoding='utf-8').read().split('\n')[:5]:
        if l.startswith('LEFTHYPHENMIN'): L=int(l.split()[1])
        if l.startswith('RIGHTHYPHENMIN'): R=int(l.split()[1])
    return L,R
def skipta(dic,ord_):
    lib=ctypes.CDLL('libhyphen.so.0');lib.hnj_hyphen_load.restype=ctypes.c_void_p
    lib.hnj_hyphen_load.argtypes=[ctypes.c_char_p]
    lib.hnj_hyphen_hyphenate2.argtypes=[ctypes.c_void_p,ctypes.c_char_p,ctypes.c_int,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p]
    d=lib.hnj_hyphen_load(dic.encode());out=[]
    for w in ord_:
        b=w.lower().encode();n=len(b);hy=ctypes.create_string_buffer(n+5)
        r,p,c=ctypes.c_void_p(),ctypes.c_void_p(),ctypes.c_void_p()
        lib.hnj_hyphen_hyphenate2(d,b,n,hy,None,ctypes.byref(r),ctypes.byref(p),ctypes.byref(c))
        # libhyphen í UTF-8 ham skilar merkjum eftir stöfum, ekki bætum
        h=hy.raw[:n]
        out.append(''.join(ch+('-' if i<len(w)-1 and h[i]&1 else '') for i,ch in enumerate(w)))
    return out
def stadir(s,L,R):
    w=s.replace('-','');n=0;c=set()
    for p in s.split('-')[:-1]:
        n+=len(p)
        if L<=n<=len(w)-R: c.add(n)
    return c
def maela(dic,gull):
    L,R=les_min(dic);vel=skipta(dic,[g.replace('-','') for g in gull])
    rett=gott=rangt=vantar=brot=0;villur=[]
    for v,g in zip(vel,gull):
        a,b=stadir(v,L,R),stadir(g,L,R)
        gott+=len(a&b);rangt+=len(a-b);vantar+=len(b-a);rett+=a==b
        if a-b: villur.append((g,v))
        w=v.replace('-','');pos=sorted(a);parts=[w[i:j] for i,j in zip([0]+pos,pos+[len(w)])]
        brot+=any(not(set(x)&V) for x in parts)
    N=len(gull);P=gott/(gott+rangt) if gott+rangt else 1;Rc=gott/(gott+vantar) if gott+vantar else 1
    return dict(ord=N,heil_rett=rett/N*100,rangir=rangt,vantar=vantar,nakvaemni=P*100,heimt=Rc*100,samhljodabrot=brot),villur
if __name__=='__main__':
    dic=sys.argv[1]
    for f in sys.argv[2:]:
        G=[l.strip() for l in open(f,encoding='utf-8') if l.strip() and not l.startswith('#')]
        m,v=maela(dic,G)
        print(f"{f}: {m['ord']} orð | {m['heil_rett']:.1f}% heil orð rétt | nákvæmni {m['nakvaemni']:.2f}% | heimt {m['heimt']:.2f}% | {m['rangir']} rangir, {m['vantar']} vantar | {m['samhljodabrot']} samhljóðabrot")
