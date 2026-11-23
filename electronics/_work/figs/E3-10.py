# E3-10 figures: Schmitt-trigger hysteresis; triangle/square oscillator; relaxation oscillator
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
V0, b = 10, 0.4
fig, axs = plt.subplots(1, 3, figsize=(10.5, 2.8))
t = np.linspace(0, 2, 2000); vi = 8*np.sin(2*np.pi*t); out = np.zeros_like(t); s = V0
for k, x in enumerate(vi):
    if s > 0 and x > b*V0: s = -V0
    elif s < 0 and x < -b*V0: s = V0
    out[k] = s
axs[0].plot(t, vi, color='#aaa', label='$v_i$'); axs[0].plot(t, out, color='#2a6fdb', lw=1.5, label='$v_o$')
axs[0].axhline(b*V0, color='#d9480f', ls=':', lw=1); axs[0].axhline(-b*V0, color='#d9480f', ls=':', lw=1)
axs[0].text(1.55, 4.6, '$+\\beta V_0$', color='#d9480f', fontsize=8); axs[0].text(1.55, -6.5, '$-\\beta V_0$', color='#d9480f', fontsize=8)
axs[0].set_title('Schmitt trigger：上升碰天花板、下降碰地板', fontsize=8.5); axs[0].legend(fontsize=7, frameon=False, loc='lower left')
tt = np.linspace(0, 3, 3000); vc = np.zeros_like(tt); sq = np.zeros_like(tt); v, s = -b*V0, V0; dt = tt[1]-tt[0]; slope = 2*b*V0/0.5
for k in range(len(tt)):
    v += (slope if s > 0 else -slope)*dt
    if v >= b*V0: s = -V0
    if v <= -b*V0: s = V0
    vc[k] = v; sq[k] = s
axs[1].plot(tt, sq, color='#2a6fdb', lw=1.2, label='方波'); axs[1].plot(tt, vc, color='#d9480f', lw=2, label='三角波（電容）')
axs[1].set_title('積分器 + Schmitt：$T = 4\\beta RC$', fontsize=8.5); axs[1].legend(fontsize=7, frameon=False, loc='lower left')
tau = 0.4; v, s = 0.0, V0; vr = np.zeros_like(tt); so = np.zeros_like(tt)
for k in range(len(tt)):
    v += (s - v)/tau*dt
    if s > 0 and v >= b*V0: s = -V0
    if s < 0 and v <= -b*V0: s = V0
    vr[k] = v; so[k] = s
axs[2].plot(tt, so, color='#2a6fdb', lw=1.2); axs[2].plot(tt, vr, color='#d9480f', lw=2)
axs[2].set_title('RC 鬆弛振盪：$T = 2RC\\ln\\frac{1+\\beta}{1-\\beta}$', fontsize=8.5)
for a in axs: a.set_xticks([]); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-10-digital-osc.svg')); plt.close(fig)
