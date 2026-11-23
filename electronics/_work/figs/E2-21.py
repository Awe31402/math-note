# E2-21 figures: spectrum of MOS ohmic-region modulator current, PMOS common-source amp
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(6.0, 2.5))
for x, h, c, t in [(0, 1.0, '#888', 'DC 2 mA'), (0.4, 0.5, '#d9480f', '$8v_2$ 聲音'), (5, 0.35, '#2a6fdb', '$0.5v_1$ 載波')]:
    ax.vlines(x, 0, h, color=c, lw=3); ax.text(x+0.1, h+0.03, t, fontsize=8, color=c)
for x in [4.6, 5.4]: ax.vlines(x, 0, 0.2, color='#2a6fdb', lw=3)
ax.text(4.2, 0.25, '$2v_1v_2$', fontsize=8, color='#2a6fdb')
ax.plot([3.2, 3.8, 6.5], [0, 0.8, 0.8], color='#2f9e44', lw=1.2); ax.text(3.9, 0.85, '高通濾波器只留 AM', fontsize=8, color='#2f9e44')
ax.set_xticks([0, 0.4, 5]); ax.set_xticklabels(['0', '$\\omega_m$', '$\\omega_c$']); ax.set_yticks([]); ax.set_ylim(0, 1.2)
ax.spines[['top','right','left']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-21-modulator-spectrum.svg')); plt.close(fig)

with drawing() as d:   # PMOS CS amp
    g0 = elm.Ground()
    elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Resistor().right().label('$R_s$'); elm.Capacitor().right().label('$C$')
    n = elm.Dot(); elm.Line().right().length(1.0)
    q = elm.PFet().anchor('gate').reverse().label('PMOS', loc='right', ofst=(0.6, 0))
    elm.Line().up().at(q.source).length(0.6); elm.Vdd().label('10 V')
    dd = elm.Dot().at(q.drain)
    elm.Resistor().down().at(dd.center).label('$R_D$ 5 kΩ', loc='bottom'); elm.Ground()
    elm.Line().right().at(dd.center).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    elm.Resistor().up().at(n.center).label('$R_1$ 2 MΩ', loc='top'); elm.Vdd().label('10 V')
    elm.Resistor().down().at(n.center).label('$R_2$ 8 MΩ', loc='bottom'); elm.Ground()
    save(d, 'E2-21-pmos-cs')
