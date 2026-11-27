# Býr til prof.jsx (InDesign) úr ord.txt, texti.txt og lotum. Keyrt: python3 prof-indesign/mynda.py
import sys,os,json,csv,random,unicodedata
H=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(H)
sys.path.insert(0,R+'/tools')
from prof import skipta,stadir
gull={}
for l in open(R+'/gogn/arnastofnun.txt',encoding='utf-8'):
    g=l.strip()
    if g: gull.setdefault(g.replace('-','').lower(),g)
till={}
for f in sorted(os.listdir(R+'/lotur')):
    if f.endswith('.tsv') and f[:3].isdigit() and 'yfirferd' not in f:
        for r in csv.DictReader(open(R+'/lotur/'+f,encoding='utf-8'),delimiter='\t'):
            if r.get('skipting'): till.setdefault(r['orð'].lower(),r['skipting'])
kaflar=[];cur=None
for l in open(H+'/ord.txt',encoding='utf-8'):
    l=unicodedata.normalize('NFC',l.strip())
    if not l or l.startswith('#') and not l.startswith('## '): continue
    if l.startswith('## '): cur=[l[3:],[]];kaflar.append(cur)
    else: cur[1].append(l)
seen={w.lower() for _,ws in kaflar for w in ws}
for f in sorted(os.listdir(R+'/lotur')):
    if f.endswith('.tsv') and f[:3].isdigit() and 'yfirferd' not in f:
        ws=[r['orð'] for r in csv.DictReader(open(R+'/lotur/'+f,encoding='utf-8'),delimiter='\t') if r['orð'].lower() not in seen]
        seen|={w.lower() for w in ws}
        nafn={'upplysingataekni':'upplýsingatækni','serhljoda-samskeyti':'sérhljóði við samskeyti'}.get(f[4:-4],f[4:-4])
        kaflar.append(['Lota '+f[:3]+' ('+nafn+')',ws])
rng=random.Random(2026);A=sorted(gull)
kaflar.append(['Úrtak úr lista Árnastofnunar (á alltaf að vera rétt)',[w for w in rng.sample(A,120) if len(w)>=7][:100]])
dic=R+'/utgafa/hyph_is_IS.dic'
allw=[w for _,ws in kaflar for w in ws]
vel=dict(zip(allw,skipta(dic,allw)))
def vaent(w):
    k=w.lower()
    if k in gull: g=gull[k];src='Á'
    elif k in till: g=till[k];src='T'
    else: return '',''
    out='';i=0
    for ch in g:
        if ch=='-': out+='-'
        else: out+=w[i];i+=1
    return out,src
rows=[]
for t,ws in kaflar:
    rows.append([t])
    for w in ws:
        v,s=vaent(w);m=vel[w];n=len(w)
        sv=sorted(stadir(m,2,3));mv='';i=0
        for k,ch in enumerate(w): mv+=ch+('-' if k+1 in sv else '')
        flag='≠' if v and stadir(v,2,3)!=set(sv) else ''
        rows.append([w,v,s,mv,flag])
texti=[l.strip() for l in open(H+'/texti.txt',encoding='utf-8') if l.strip()]
data={'kaflar':kaflar,'texti':texti,'vaent':rows}
js=open(H+'/sniðmát.jsx',encoding='utf-8').read().replace('/*GÖGN*/null',json.dumps(data,ensure_ascii=False))
open(H+'/profunarskjal.jsx','w',encoding='utf-8').write(js)
n=sum(len(ws) for _,ws in kaflar);print(len(kaflar),'kaflar,',n,'orð')
