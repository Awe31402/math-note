# E2-16 figures: bias stability (fixed VGS vs RS bias line), CS amp with RS and bypass C
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
Vt = 1
fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.0), sharey=True)
v = np.linspace(1, 4.2, 300)
for a in axs:
    for k, c in [(2, '#2a6fdb'), (4, '#4dabf7'), (16, '#a5d8ff')]:
        a.plot(v, k/2*(v-Vt)**2, color=c, lw=1.8, label=f'$k$ = {k}')
    a.axvline(Vt, color='#888', lw=1.5, label='$k\\to\\infty$')
    a.set_xlim(0.8, 4.2); a.set_ylim(0, 3); a.set_xlabel('$V_{GS}$ (V)'); a.spines[['top','right']].set_visible(False)
axs[0].axvline(2, color='#d9480f', lw=1.5, ls='--'); axs[0].set_title('固定 $V_{GS}$ = 2 V：$k$ 變 2 倍電流就 2 倍', fontsize=9)
for k in [2, 4, 16]: axs[0].plot(2, k/2, 'o', color='#d9480f', ms=4)
axs[0].set_ylabel('$I_D$ (mA)'); axs[0].legend(fontsize=7, frameon=False, loc='upper right')
axs[1].plot(v, (4 - v)/2, color='#d9480f', lw=1.5, ls='--', label='偏壓線 $I_D = (V_G - V_{GS})/R_S$')
from scipy.optimize import brentq
for k in [2, 4, 16]:
    x = brentq(lambda g: k/2*(g-Vt)**2 - (4-g)/2, 1.0001, 4); axs[1].plot(x, (4-x)/2, 'o', color='#d9480f', ms=4)
axs[1].plot(1, 1.5, 'o', color='#d9480f', ms=4); axs[1].text(1.05, 1.6, '1.5 mA', fontsize=8); axs[1].text(2.05, 0.85, '1 mA', fontsize=8)
axs[1].set_title('加 $R_S$ = 2 kΩ：$k$ 從 2 到 ∞，電流只從 1 到 1.5 mA', fontsize=9); axs[1].legend(fontsize=7, frameon=False, loc='upper right')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-16-bias-stability.svg')); plt.close(fig)

with drawing() as d:
    g0 = elm.Ground()
    elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Capacitor().right().label('$C_C$'); elm.Line().right().length(0.8)
    n = elm.Dot()
    elm.Line().right().length(1.0)
    q = elm.NFet().anchor('gate').reverse()
    elm.Resistor().up().at(q.drain).label('$R_D$ 4 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(q.drain).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    s = elm.Dot().at(q.source)
    elm.Resistor().down().at(s.center).label('$R_S$ 2 kΩ', loc='bottom'); elm.Ground()
    elm.Line().right().at(s.center).length(2.8); elm.Capacitor().down().label('$C_S$', loc='bottom'); elm.Ground()
    elm.Resistor().up().at(n.center).label('$R_1$ 6 MΩ', loc='top'); elm.Vdd().label('10 V')
    elm.Resistor().down().at(n.center).label('$R_2$ 4 MΩ', loc='bottom'); elm.Ground()
    save(d, 'E2-16-rs-bypass')
