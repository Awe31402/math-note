# E2-25 figure: VTC of CS amp with PMOS current-source load (Early effect, VA=100 V)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.optimize import brentq
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
k, Vt, VA, VDD, VSG = 2, 1, 100, 10, 2
def idn(vi, vo):
    ov = vi - Vt
    if ov <= 0: return 0
    return (k*(ov*vo - vo**2/2) if vo < ov else k/2*ov**2)*(1 + vo/VA)
def idp(vo):
    vsd = VDD - vo; ov = VSG - Vt
    return (k*(ov*vsd - vsd**2/2) if vsd < ov else k/2*ov**2)*(1 + vsd/VA)
def vout(vi): return brentq(lambda vo: idp(vo) - idn(vi, vo), 0, VDD)
vi = np.linspace(0, 3, 3000); vo = np.array([vout(x) for x in vi])
fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.0))
axs[0].plot(vi, vo, color='#2a6fdb', lw=2); axs[0].axvspan(1.96, 2.04, color='#ffe8cc')
axs[0].text(0.2, 8.0, '$Q_N$ off\n$Q_P$ 三極管', fontsize=8); axs[0].text(2.3, 1.2, '$Q_N$ 三極管', fontsize=8); axs[0].text(2.1, 6.0, '兩顆都飽和\n（放大窗）', fontsize=8, color='#d9480f')
axs[0].set_xlabel('$v_I$ (V)'); axs[0].set_ylabel('$v_O$ (V)'); axs[0].set_title('完整轉移特性', fontsize=9)
m = (vi > 1.9) & (vi < 2.1)
axs[1].plot(vi[m], vo[m], color='#2a6fdb', lw=2)
for x, y, t in [(1.96, 9, 'A (1.96, 9)'), (2.04, 1, 'B (2.04, 1)'), (2.0, 5, 'Q (2, 5)')]:
    axs[1].plot(x, y, 'o', color='#d9480f'); axs[1].text(x+0.005, y+0.3, t, fontsize=8)
axs[1].set_xlabel('$v_I$ (V)'); axs[1].set_title('放大窗只有 2 ± 0.04 V，斜率約 −100', fontsize=9)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-25-vtc-window.svg')); plt.close(fig)
print(vout(1.96), vout(2.0), vout(2.04))
