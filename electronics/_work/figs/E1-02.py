# E1-02 figures
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt

# max power transfer circuit
with drawing() as d:
    s = elm.SourceV().up().label('$V$', loc='top')
    elm.Ground().at(s.start)
    elm.Resistor().right().at(s.end).label('$R$')
    n = elm.Dot()
    elm.Resistor().down().at(n.center).label('$R_L$', loc='top')
    elm.Ground()
    save(d, 'E1-02-maxpower')

# P_L vs R_L plot
R = 1.0; RL = np.linspace(0, 8, 400); P = RL/(R+RL)**2
fig, ax = plt.subplots(figsize=(4.4, 2.8))
ax.plot(RL, P, color='#2a6fdb', lw=2)
ax.axvline(1, color='gray', ls='--', lw=1); ax.plot([1], [0.25], 'o', color='#d9480f')
ax.annotate('$R_L=R$, $P_{max}=V^2/4R$', (1, 0.25), (2.2, 0.22), arrowprops=dict(arrowstyle='->'))
ax.set_xlabel('$R_L / R$'); ax.set_ylabel('$P_L$  (單位 $V^2/R$)')
ax.set_ylim(0, 0.3); ax.spines[['top','right']].set_visible(False)
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-02-maxpower-plot.svg')); plt.close(fig)

# example: 10V, 5Ω, 10Ω || 10Ω, load RL
with drawing() as d:
    b = elm.BatteryCell().up().reverse().label('10 V', loc='top')
    elm.Ground().at(b.start)
    elm.Resistor().right().at(b.end).label('5 Ω')
    n = elm.Dot()
    elm.Resistor().down().at(n.center).label('10 Ω', loc='top'); elm.Ground()
    elm.Line().right().at(n.center).length(2.5); m = elm.Dot()
    elm.Resistor().down().at(m.center).label('10 Ω', loc='top'); elm.Ground()
    elm.Line().right().at(m.center).length(3); o = elm.Dot(open=True)
    elm.Resistor().down().at(o.center).label('$R_L$ ?', loc='top'); elm.Ground()
    save(d, 'E1-02-example')

# Thevenin and Norton forms
with drawing() as d:
    s = elm.SourceSin().up().label('$v_s(t)$', loc='top')
    elm.Ground().at(s.start)
    elm.Resistor().right().at(s.end).label('$R_s$')
    elm.Dot(open=True).label('$v_x$', loc='right')
    elm.Label().at((1.5, -1.6)).label('(a)')
    x0 = 7
    i = elm.SourceI().up().at((x0, 0)).label('$i_s(t)$', loc='top')
    elm.Ground().at(i.start)
    elm.Line().right().at(i.end).length(2.5); t = elm.Dot()
    elm.Resistor().down().at(t.center).label('$R_s$', loc='top'); elm.Ground()
    elm.Line().right().at(t.center).length(1.5)
    elm.Dot(open=True).label('$v_x$', loc='right')
    elm.Label().at((x0 + 1.8, -1.6)).label('(b)')
    save(d, 'E1-02-thevenin-norton')

# sensor: Vdc - R1 - node - R2(t) to ground, node -> amplifier input Ri
with drawing() as d:
    b = elm.BatteryCell().up().reverse().label('$V_{DC}$', loc='top')
    elm.Ground().at(b.start)
    elm.Resistor().right().at(b.end).label('$R_1$'); n = elm.Dot()
    elm.ResistorVar().down().at(n.center).label('$R_2(t)$', loc='top'); elm.Ground()
    elm.Line().right().at(n.center).length(3.5).label('$v_i$ →')
    elm.Resistor().down().label('$R_i$', loc='top'); elm.Ground()
    save(d, 'E1-02-sensor')
