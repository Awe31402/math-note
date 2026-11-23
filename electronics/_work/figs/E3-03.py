# E3-03 figures: load line & saturation; biased CE amp with split emitter resistor
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(5.6, 3.0))
v = np.linspace(0, 10, 500)
for ib, c in [(0.005, '#a5d8ff'), (0.01, '#4dabf7'), (0.015, '#2a6fdb'), (0.0196, '#1864ab'), (0.03, '#0b3d75')]:
    ax.plot(v, np.minimum(100*ib, 100*ib)*(1-np.exp(-v/0.06)), color=c, lw=1.5)
ax.plot(v, (10 - v)/5, color='#d9480f', lw=2, ls='--', label='負載線 $I_C = (V_{CC} - V_{CE})/R_C$')
ax.plot(5, 1, 'o', color='k'); ax.text(5.2, 1.08, 'Q (5 V, 1 mA)', fontsize=8)
ax.plot(0.2, 1.96, 'o', color='#d9480f'); ax.text(0.4, 2.15, '$I_{C,sat}$ = 1.96 mA', fontsize=8, color='#d9480f')
ax.text(5.5, 2.75, '$I_B$ 再大，$I_C$ 也停在 1.96 mA', fontsize=8)
ax.set_xlabel('$V_{CE}$ (V)'); ax.set_ylabel('$I_C$ (mA)'); ax.set_ylim(0, 3.2); ax.legend(fontsize=7.5, frameon=False, loc='upper right')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-03-loadline.svg')); plt.close(fig)

with drawing() as d:
    g0 = elm.Ground()
    elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Resistor().right().label('$R_s$'); elm.Capacitor().right().label('$C_C$')
    n = elm.Dot(); elm.Line().right().length(0.6)
    q = elm.BjtNpn(circle=True).anchor('base')
    elm.Resistor().up().at(q.collector).label('$R_C$ 4 kΩ', loc='bottom'); elm.Vdd().label('10 V')
    elm.Line().right().at(q.collector).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    elm.Resistor().down().at(q.emitter).label('0.2 kΩ', loc='bottom'); m = elm.Dot()
    elm.Resistor().down().label('1.8 kΩ', loc='bottom'); elm.Ground()
    elm.Line().right().at(m.center).length(2.4); elm.Capacitor().down().label('$C_E$', loc='bottom'); elm.Ground()
    elm.Resistor().up().at(n.center).label('$R_1$ 270 kΩ', loc='top'); elm.Vdd().label('10 V')
    elm.Resistor().down().at(n.center).label('$R_2$ 158 kΩ', loc='top'); elm.Ground()
    save(d, 'E3-03-ce-split-re')
