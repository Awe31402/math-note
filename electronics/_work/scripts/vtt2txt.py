import re,os,glob
# vtt2txt.py -> subs/<C>-<NN>-<id>.zh-TW.vtt to txt/<C>-<NN>.txt, [mm:ss] or [h:mm:ss] per ~30 s chunk
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
for f in sorted(glob.glob("subs/*.vtt")):
    out="txt/"+os.path.basename(f)[:5]+".txt"
    lines=open(f,encoding="utf-8").read().split("\n"); cur=None; buf=[]; res=[]
    def fmt(t): return f"[{t//3600}:{t%3600//60:02d}:{t%60:02d}]" if t>=3600 else f"[{t//60:02d}:{t%60:02d}]"
    for i,l in enumerate(lines):
        m=re.match(r"(?:(\d+):)?(\d+):(\d+)\.\d+ -->",l)
        if not m: continue
        h,mi,s=m.groups(); t=int(h or 0)*3600+int(mi)*60+int(s)
        txt=[]; j=i+1
        while j<len(lines) and lines[j].strip(): txt.append(re.sub(r"<[^>]+>","",lines[j].strip())); j+=1
        if cur is None or t-cur>=30:
            if buf: res.append(fmt(cur)+" "+" ".join(buf))
            cur=t; buf=[]
        buf+= [x for x in txt if x and (not buf or x!=buf[-1])]
    if buf: res.append(fmt(cur)+" "+" ".join(buf))
    open(out,"w",encoding="utf-8").write("\n".join(res)+"\n")
