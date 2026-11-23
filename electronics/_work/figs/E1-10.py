# E1-10 figures: op-amp transfer characteristic + comparator, follower, non-inverting, inverting, summer, difference amp
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axs = plt.subplots(1, 2, figsize=(7.6, 2.6))
x = np.linspace(-1, 1, 400); axs[0].plot(x, np.clip(1e3*x, -10, 10), color='#2a6fdb', lw=2)
axs[0].set_xlabel('$v_+ - v_-$'); axs[0].set_ylabel('$v_o$ (V)'); axs[0].axhline(0, color='k', lw=0.5); axs[0].axvline(0, color='k', lw=0.5)
axs[0].text(0.15, 8, '飽和 +10 V（天花板）', fontsize=8); axs[0].text(-0.95, -8.5, '飽和 −10 V（地板）', fontsize=8); axs[0].set_xticks([])
t = np.linspace(0, 2, 400); axs[1].plot(t, 3*np.sin(2*np.pi*t), color='#888', label='$v_i$'); axs[1].plot(t, 10*np.sign(np.sin(2*np.pi*t)), color='#d9480f', lw=2, label='$v_o$')
axs[1].set_title('比較器：sine 進、方波出', fontsize=10); axs[1].legend(fontsize=8, frameon=False, loc='lower left'); axs[1].set_xticks([])
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-10-transfer-comparator.svg')); plt.close(fig)

def opamp(d):
    return elm.Opamp(leads=True)

with drawing() as d:   # voltage follower
    op = opamp(d)
    elm.Line().left().at(op.in2).length(1); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Wire('|-').at(o.center).to(op.in1).shape('n') if False else None
    elm.Line().up().at(o.center).length(1.5); elm.Line().left().tox(op.in1[0]-0.5); elm.Line().down().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    save(d, 'E1-10-follower')

with drawing() as d:   # non-inverting amplifier
    op = opamp(d)
    elm.Line().left().at(op.in2).length(1); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    elm.Resistor().left().at(n.center).length(2).label('$R_1$', loc='top'); elm.Ground()
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R_2$'); elm.Line().down().toy(o.center[1])
    save(d, 'E1-10-noninverting')

with drawing() as d:   # inverting amplifier
    op = opamp(d)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    elm.Resistor().left().at(n.center).label('$R_1$'); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R_2$'); elm.Line().down().toy(o.center[1])
    save(d, 'E1-10-inverting')

with drawing() as d:   # non-inverting summer
    op = opamp(d)
    elm.Line().left().at(op.in2).length(0.5); p = elm.Dot()
    elm.Resistor().left().at(p.center).label('$R_3$'); elm.Dot(open=True).label('$v_1$', loc='left')
    elm.Line().down().at(p.center).length(1); elm.Resistor().left().label('$R_4$', loc='bottom'); elm.Dot(open=True).label('$v_2$', loc='left')
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R_2$'); elm.Line().down().toy(o.center[1])
    elm.Resistor().left().at(n.center).length(2).label('$R_1$', loc='top'); elm.Ground()
    save(d, 'E1-10-summer')

with drawing() as d:   # difference amplifier
    op = opamp(d)
    elm.Line().left().at(op.in2).length(0.5); p = elm.Dot()
    elm.Resistor().left().at(p.center).label('$R_1$', loc='bottom'); elm.Dot(open=True).label('$v_1$', loc='left')
    elm.Resistor().down().at(p.center).label('$R_2$', loc='bottom'); elm.Ground()
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    elm.Resistor().left().at(n.center).label('$R_3$'); elm.Dot(open=True).label('$v_2$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R_4$'); elm.Line().down().toy(o.center[1])
    save(d, 'E1-10-difference')

with drawing() as d:   # source with Rs -> follower -> RL
    s = elm.SourceSin().up().label('$v_s$', loc='top'); elm.Ground().at(s.start)
    elm.Resistor().right().at(s.end).label('$R_s$')
    op = elm.Opamp(leads=True).anchor('in2')
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='top')
    elm.Line().up().at(o.center).length(1.5); elm.Line().left().tox(op.in1[0]-0.5); elm.Line().down().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    elm.Resistor().down().at(o.center).label('$R_L$', loc='bottom'); elm.Ground()
    save(d, 'E1-10-buffered-source')
