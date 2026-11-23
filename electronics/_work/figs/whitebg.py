# add a white background rect to schemdraw SVGs (idempotent). usage: python3 whitebg.py file.svg ...
import re, sys
MARK = '<rect data-bg="white"'
def add_bg(path):
    s = open(path, encoding='utf-8').read()
    if MARK in s: return False
    m = re.search(r'<svg\b[^>]*>', s)
    vb = re.search(r'viewBox="([-\d.e]+)[ ,]+([-\d.e]+)[ ,]+([-\d.e]+)[ ,]+([-\d.e]+)"', m.group(0))
    if vb: x, y, w, h = vb.groups(); rect = f'{MARK} x="{x}" y="{y}" width="{w}" height="{h}" fill="white"/>'
    else: rect = f'{MARK} x="0" y="0" width="100%" height="100%" fill="white"/>'
    s = s[:m.end()] + rect + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s); return True
if __name__ == '__main__':
    n = sum(add_bg(p) for p in sys.argv[1:]); print(f'{n} files updated')
