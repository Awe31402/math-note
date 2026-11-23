import re, sys
src = open(sys.argv[1]).read().split('\n\n')
out = []
for b in src:
    m = re.match(r'(\d+:)?(\d+):(\d+)\.\d+ -->.*?\n(.*)', b.strip(), re.S)
    if m:
        h = int(m.group(1)[:-1]) if m.group(1) else 0
        s = h*3600 + int(m.group(2))*60 + int(m.group(3))
        ts = f"{s//3600}:{s%3600//60:02d}:{s%60:02d}" if s >= 3600 else f"{s//60:02d}:{s%60:02d}"
        out.append(f"[{ts}] " + m.group(4).replace('\n', ' '))
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
