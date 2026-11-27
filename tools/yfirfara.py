# Yfirfer tillogur.tsv: snið, Unicode, tvítekningar, samanburður við gögn og vél.
# Notkun: python3 tools/yfirfara.py tillogur.tsv utgafa/hyph_is_IS.dic gogn/arnastofnun.txt gogn/thjalfun.txt > skyrsla.tsv
import sys,unicodedata,collections
sys.path.insert(0,__file__.rsplit('/',1)[0])
from prof import skipta,stadir,les_min
till,dic=sys.argv[1],sys.argv[2];gagnaskrar=sys.argv[3:]
L,R=les_min(dic)
til={}
for f in gagnaskrar:
    for l in open(f,encoding='utf-8'):
        g=l.strip()
        if g: til.setdefault(g.replace('-','').lower(),g)
DALKAR=['orð','skipting','orðhlutar','heimild','öryggi']
rows=[];seen=set();teljari=collections.Counter()
lines=open(till,encoding='utf-8').read().split('\n')
if lines and lines[0].split('\t')==DALKAR: lines=lines[1:]
for nr,l in enumerate(lines,2):
    if not l.strip(): continue
    l2=unicodedata.normalize('NFC',l);c=l2.split('\t')
    flokkar=[];ath=[]
    if l2!=l: ath.append('NFC-samræmt')
    if len(c)!=5:
        rows.append((nr,l,'',['ÓGILT'],[f'{len(c)} dálkar, á að vera 5']));continue
    o,s,h,heim,oryg=[x.strip() for x in c]
    if not o or '-' in o or ' ' in o: flokkar.append('ÓGILT');ath.append('orð vantar eða inniheldur bandstrik/bil')
    if s and s.replace('-','')!=o: flokkar.append('ÓGILT');ath.append('skipting passar ekki við orð')
    if h and h.replace('+','')!=o: ath.append('orðhlutar passa ekki við orð')
    if oryg not in ('hátt','miðlungs','lágt'): flokkar.append('ÓGILT');ath.append('öryggi ógilt')
    if not heim: flokkar.append('ÓGILT');ath.append('heimild vantar')
    if o.lower() in seen: flokkar.append('ÓGILT');ath.append('tvítekið')
    seen.add(o.lower())
    vel=skipta(dic,[o])[0] if o else ''
    if o.lower() in til: flokkar.append('FYRIRLIGGJANDI');ath.append('í gögnum: '+til[o.lower()])
    else: flokkar.append('NÝTT')
    if not s: flokkar.append('ÓLEYST')
    elif 'ÓGILT' not in flokkar:
        a,b=stadir(vel,L,R),stadir(s,L,R)
        if a==b: flokkar.append('SAMHLJÓÐA')
        else:
            flokkar.append('ÓSAMMÁLA')
            if a-b: ath.append('vélin skiptir þar sem tillagan gerir það ekki')
            if b-a: ath.append('tillagan skiptir þar sem vélin gerir það ekki')
    rows.append((nr,o,vel,flokkar,ath))
print('lína\torð\tvél\tflokkar\tathugasemd')
for nr,o,vel,f,a in rows:
    teljari.update(f);print(f'{nr}\t{o}\t{vel}\t{",".join(f)}\t{"; ".join(a)}')
print('\n# '+' · '.join(f'{k}: {v}' for k,v in sorted(teljari.items())),file=sys.stderr)
