# E2-14 figures: load line on output characteristics, VTC with regions
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.optimize import brentq
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
k, Vt, VDD, RD = 2, 1, 10, 5
def iD(vgs, vds):
    vov = vgs - Vt
    if vov <= 0: return 0.0
    return k*(vov*vds - vds**2/2) if vds < vov else k*vov**2/2
def vout(vi): return brentq(lambda vo: vo - (VDD - RD*iD(vi, vo)), 0, VDD) if vi > Vt else VDD
fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.1))
v = np.linspace(0, 10, 500)
for vgs, c in [(5, '#2a6fdb'), (2.317, '#2f9e44'), (2, '#f08c00'), (1.5, '#d9480f')]:
    axs[0].plot(v, [iD(vgs, x) for x in v], color=c, lw=1.8, label=f'$V_{{GS}}$ = {vgs} V')
axs[0].plot(v, (VDD - v)/RD, color='#c92a2a', lw=1.5, ls='--', label='負載線 $I_D = (V_{DD}-V_{DS})/R_D$')
for vgs in [2, 2.317, 5]:
    vo = vout(vgs); axs[0].plot(vo, (VDD-vo)/RD, 'o', color='k', ms=4)
axs[0].text(5.1, 1.1, 'Q (2 V)', fontsize=8); axs[0].text(1.4, 1.85, '剛進三極管', fontsize=8); axs[0].text(0.35, 2.2, '5 V', fontsize=8)
axs[0].set_xlabel('$V_{DS}$ (V)'); axs[0].set_ylabel('$I_D$ (mA)'); axs[0].set_ylim(0, 2.6); axs[0].legend(fontsize=6.5, frameon=False, loc='upper right')
vi = np.linspace(0, 5, 400); vo = [vout(x) for x in vi]
axs[1].plot(vi, vo, color='#2a6fdb', lw=2)
axs[1].axvspan(0, 1, color='#eee'); axs[1].axvspan(1, 2.317, color='#e7f5ff'); axs[1].axvspan(2.317, 5, color='#fff4e6')
axs[1].text(0.15, 1.5, '截止\n(off)', fontsize=8); axs[1].text(1.25, 1.5, '飽和\n放大', fontsize=8); axs[1].text(3.3, 3, '三極管', fontsize=8)
axs[1].plot(2, 5, 'o', color='k'); xx = np.array([1.75, 2.25]); axs[1].plot(xx, 5 - 10*(xx-2), color='#d9480f', lw=1.2)
axs[1].text(2.15, 5.6, 'Q：斜率 −10', fontsize=8, color='#d9480f'); axs[1].plot(2.317, 1.317, 'o', color='k', ms=4); axs[1].text(2.4, 1.5, '(2.317, 1.317)', fontsize=7.5)
axs[1].set_xlabel('$v_I = V_{GS}$ (V)'); axs[1].set_ylabel('$v_O = V_{DS}$ (V)')
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-14-loadline-vtc.svg')); plt.close(fig)
