import sys,json;sys.path.insert(0,'/home/claude/ordskipting/tools')
from prof import skipta,maela
def frag(dic,G):
    V=skipta(dic,[g.replace('-','') for g in G]);n=0
    for v in V:
        w=v.replace('-','');p=v.split('-')
        # sía eftir L=2,R=3 eins og InDesign
        c=[];m=0
        for x in p[:-1]:
            m+=len(x)
            if 2<=m<=len(w)-3: c.append(m)
        b=[0]+c+[len(w)]
        n+=any(bb-a==1 and a>0 and bb<len(w) for a,bb in zip(b,b[1:]))
    return n
dic=sys.argv[1]
for f in sys.argv[2:]:
    G=[l.strip() for l in open(f,encoding='utf-8') if l.strip()]
    m,_=maela(dic,G)
    print(f"{f.split('/')[-1]:14} heil {m['heil_rett']:.2f}% | rangir {m['rangir']} | vantar {m['vantar']} | einstafsbútar {frag(dic,G)}")
