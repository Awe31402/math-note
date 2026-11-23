# E1-11 figures: instrumentation amplifier, right-leg drive, op-amp limits
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:
    d.config(fontsize=12)
    A1 = elm.Opamp(leads=True).flip().anchor('in2').at((0, 3))      # flipped: + on top? we use in2 as + input
    A2 = elm.Opamp(leads=True).anchor('in2').at((0, -3))
    elm.Line().left().at(A1.in2).length(1); elm.Dot(open=True).label('$v_1$', loc='left')
    elm.Line().left().at(A2.in2).length(1); elm.Dot(open=True).label('$v_2$', loc='left')
    # feedback R2 each
    elm.Line().left().at(A1.in1).length(0.5); n1 = elm.Dot()
    elm.Line().left().at(A2.in1).length(0.5); n2 = elm.Dot()
    elm.Line().right().at(A1.out).length(0.8); o1 = elm.Dot().label("$v_1'$", loc='top')
    elm.Line().right().at(A2.out).length(0.8); o2 = elm.Dot().label("$v_2'$", loc='bottom')
    elm.Wire('|-').at(n1.center).to((o1.center[0], n1.center[1]-1.2)) if False else None
    elm.Line().down().at(n1.center).length(1.0); k1 = elm.Dot()
    elm.Resistor().right().tox(o1.center[0]).label('$R_2$', loc='bottom'); elm.Line().up().toy(o1.center[1])
    elm.Line().up().at(n2.center).length(1.0); k2 = elm.Dot()
    elm.Resistor().right().tox(o2.center[0]).label('$R_2$'); elm.Line().down().toy(o2.center[1])
    r1 = elm.ResistorVar().down().at(k1.center).to(k2.center).label('$R_1$', loc='bottom')
    elm.Dot().at(r1.center).label('中點', loc='left') if False else elm.Line().left().at(r1.center).length(1.2)
    elm.Dot(open=True).label('$v_{cm}$', loc='left')
    # difference stage
    B = elm.Opamp(leads=True).right().anchor('in1').at((9.0, 0.5))
    elm.Resistor().right().at(o1.center).to((7.0, o1.center[1])).label('$R_3$')
    elm.Line().down().toy(B.in1[1]); m = elm.Dot(); elm.Line().right().tox(B.in1[0])
    elm.Resistor().right().at(o2.center).to((7.6, o2.center[1])).label('$R_3$', loc='bottom'); q = elm.Dot()
    elm.Line().up().at(q.center).toy(B.in2[1]); elm.Line().right().tox(B.in2[0])
    elm.Resistor().down().at(q.center).label('$R_4$', loc='bottom'); elm.Ground()
    elm.Line().right().at(B.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().up().at(m.center).length(2.2); elm.Resistor().right().tox(o.center[0]).label('$R_4$'); elm.Line().down().toy(o.center[1])
    save(d, 'E1-11-instrumentation')

v = np.linspace(-2.5, 2.5, 400)
fig, ax = plt.subplots(figsize=(4.4, 2.8))
ax.plot(v, np.clip(10*v, -13, 13), color='#2a6fdb', lw=2); ax.axhline(13, ls=':', color='gray'); ax.axhline(-13, ls=':', color='gray')
ax.text(-2.4, 11, '+13 V 飽和', fontsize=8); ax.text(0.8, -12, '−13 V 飽和', fontsize=8)
ax.axvline(1.3, ls='--', color='#d9480f', lw=1); ax.axvline(-1.3, ls='--', color='#d9480f', lw=1); ax.text(1.35, 2, '±1.3 V', color='#d9480f', fontsize=8)
ax.set_xlabel('$v_i$ (V)'); ax.set_ylabel('$v_o$ (V)'); ax.set_title('增益 10 倍的非反相放大器', fontsize=10); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-11-saturation.svg')); plt.close(fig)

t = np.linspace(0, 2, 500)
fig, ax = plt.subplots(figsize=(4.6, 2.4))
ax.plot(t, 15*np.sin(2*np.pi*t), color='#bbb', ls='--', label='想要的 $10v_i$（±15 V）'); ax.plot(t, np.clip(15*np.sin(2*np.pi*t), -13, 13), color='#d9480f', lw=2, label='實際輸出（被切在 ±13 V）')
ax.set_yticks([-13, 0, 13]); ax.set_xticks([]); ax.legend(fontsize=7.5, frameon=False, loc='lower left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-11-clipping.svg')); plt.close(fig)
