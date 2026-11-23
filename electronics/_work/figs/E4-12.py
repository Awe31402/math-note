# E4-12: hysteretic current control of the laser driver, and non-overlapping (dead-time) gate drive
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl, clean
import numpy as np; plt = mpl()
dt = 1e-3; t = np.arange(0, 6, dt); i = np.zeros_like(t); s = 1
Ic, If, up, dn = 10.5, 9.5, 8.0, 4.0
for k in range(1, len(t)):
    i[k] = i[k-1] + (up if s else -dn)*dt*(1 if i[k-1] > 5 else 6)
    if s and i[k] >= Ic: s = 0
    if not s and i[k] <= If: s = 1
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.8, 2.9))
a1.plot(t, i, color='#2a6fdb', lw=1.4)
a1.axhline(Ic, color='#d9480f', ls=':', lw=1); a1.axhline(If, color='#d9480f', ls=':', lw=1); a1.axhline((Ic + If)/2, color='#2b8a3e', ls='--', lw=1)
a1.text(0.1, Ic + 0.2, r'$I_{ceil}$', fontsize=8, color='#d9480f'); a1.text(0.1, If - 0.8, r'$I_{floor}$', fontsize=8, color='#d9480f')
a1.text(3.2, (Ic + If)/2 - 1.6, r'平均 ≈ $V_R/(RA)$', fontsize=8, color='#2b8a3e'); a1.set_ylim(0, 12)
a1.set_title('遲滯電流控制：電流在天花板與地板間來回', fontsize=9); a1.set_xticks([]); a1.set_ylabel('A')
tt = np.linspace(0, 4, 2000); vin = ((tt > 0.5) & (tt < 2.5)).astype(float); dly = 0.25
vb = ((tt > 0.5 + dly) & (tt < 2.5 + dly)).astype(float)
OR, AND = np.maximum(vin, vb), np.minimum(vin, vb)
for k, (y, lab, c) in enumerate(((vin, r'$v_A$ 輸入', '#666'), (vb, r'$v_B$（RC 延遲）', '#999'), (OR, 'OR → PMOS 閘極（晚關）', '#d9480f'), (AND, 'AND → NMOS 閘極（晚開）', '#2a6fdb'))):
    a2.plot(tt, y*0.8 - 1.2*k, color=c, lw=1.6); a2.text(4.05, -1.2*k + 0.3, lab, fontsize=7.5, color=c)
for x in (0.5, 0.75, 2.5, 2.75): a2.axvline(x, color='#ddd', lw=0.8, zorder=0)
a2.set_title('死區時間：一顆先關、另一顆才開', fontsize=9); a2.axis('off'); a2.set_xlim(0, 6.6)
clean(a1); fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E4-12-laser-deadtime.svg')); plt.close(fig)
