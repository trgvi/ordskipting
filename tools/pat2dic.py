import sys
src,dst=sys.argv[1],sys.argv[2]
p=[l.strip() for l in open(src,encoding='latin-1') if l.strip()]
extra=open(sys.argv[3],encoding='utf-8').read() if len(sys.argv)>3 else ''
open(dst,'w',encoding='utf-8').write('UTF-8\nLEFTHYPHENMIN 2\nRIGHTHYPHENMIN 3\n'+'\n'.join(p)+'\n'+extra)
