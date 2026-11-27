# Setur saman tveggja þrepa skrá: þrep1 (samskeyti) + NEXTLEVEL + þrep2 (núverandi orðskipting)
import sys,re,subprocess,tempfile,os
T=__file__.rsplit('/',1)[0]
l1tex,l2dic,out=sys.argv[1:4];extra1=sys.argv[4] if len(sys.argv)>4 else None
tmp=tempfile.mkdtemp()
args=['python3','-I',f'{T}/pat2dic.py',l1tex,f'{tmp}/a.dic']+([extra1] if extra1 else [])
subprocess.run(args,check=True)
subprocess.run(['python3','-I',f'{T}/subst.py',f'{tmp}/a.dic',f'{tmp}/b.dic'],check=True,stdout=subprocess.DEVNULL)
def body(p): return [l for l in open(p,encoding='utf-8').read().split('\n')[1:] if l and not re.match(r'^[A-Z]',l)]
o=['UTF-8','LEFTHYPHENMIN 2','RIGHTHYPHENMIN 3','COMPOUNDLEFTHYPHENMIN 2','COMPOUNDRIGHTHYPHENMIN 2']+body(f'{tmp}/b.dic')+['NEXTLEVEL']+body(l2dic)
open(out,'w',encoding='utf-8').write('\n'.join(o)+'\n')
