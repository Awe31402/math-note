# E4-10: LR filter driven by a 0/5 V square wave: tau << T follows, tau >> T gives average + triangle ripple
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl, clean
import numpy as np; plt = mpl()
dt = 1e-3; t = np.arange(0, 60, dt); T = 1.0
def run(D, tau):
    vin = np.where((t % T) < D*T, 5.0, 0.0); v = np.zeros_like(t)
    for k in range(1, len(t)): v[k] = v[k-1] + (vin[k-1] - v[k-1])/tau*dt
    return vin, v
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 2.8))
vin, v = run(0.5, 0.05); m = t < 4
a1.plot(t[m], vin[m], color='#bbb', lw=1); a1.plot(t[m], v[m], color='#2a6fdb', lw=1.6); a1.set_title(r'$\tau \ll T$：輸出幾乎就是方波', fontsize=9)
D = np.where(t < 30, 0.5, 0.75); vin2 = np.where((t % T) < D*T, 5.0, 0.0); v2 = np.zeros_like(t)
for k in range(1, len(t)): v2[k] = v2[k-1] + (vin2[k-1] - v2[k-1])/4.0*dt
a2.plot(t, v2, color='#2a6fdb', lw=1.2); a2.axhline(2.5, color='#d9480f', ls=':', lw=1); a2.axhline(3.75, color='#d9480f', ls=':', lw=1)
a2.text(0.5, 2.7, r'$5D=2.5$', color='#d9480f', fontsize=8); a2.text(31, 3.95, r'$D$ 改成 0.75 → $5D=3.75$', color='#d9480f', fontsize=8)
a2.set_title(r'$\tau \gg T$：爬到平均值 $5D$，上面帶小三角波', fontsize=9)
for a in (a1, a2): a.set_xticks([]); a.set_ylabel('V')
clean(a1, a2); fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E4-10-lr-filter.svg')); plt.close(fig)
