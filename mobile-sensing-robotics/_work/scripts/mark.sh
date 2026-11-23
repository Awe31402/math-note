#!/bin/bash
# usage: mark.sh NUM FILE PENDING STATUS [NOTE]
cd /home/awe/disk/math-note/mobile-sensing-robotics
n="$1"; f="$2"; p="$3"; s="$4"; note="$5"
python3 -I - "$n" "$f" "$p" "$s" "$note" <<'PY'
import sys,re
n,f,p,s,note=sys.argv[1:6]
L=open('PROGRESS.md').read().split('\n')
for i,l in enumerate(L):
    if l.startswith(f'| {n} |'):
        c=[x.strip() for x in l.strip('|').split('|')]
        c[4]=s; c[5]=p; c[6]=f'[筆記]({f})'+(f'；{note}' if note else '')
        L[i]='| '+' | '.join(c)+' |'
open('PROGRESS.md','w').write('\n'.join(L))
PY
grep "^| $n |" PROGRESS.md
