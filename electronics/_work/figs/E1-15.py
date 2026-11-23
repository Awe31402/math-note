# E1-15 figures: transimpedance (I-V converter), daylight vs threshold, street-light system (final)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:   # I-V converter with photodiode model
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o = i_{ph}R$', loc='right')
    elm.Line().left().at(op.in1).length(1.5); n = elm.Dot()
    elm.Line().up().at(op.in1).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R$'); elm.Line().down().toy(o.center[1])
    elm.Line().left().at(n.center).length(2.0); m = elm.Dot()
    elm.Diode().down().at(m.center).reverse(); elm.Ground()
    elm.Line().left().at(m.center).length(2.0)
    s = elm.SourceI().down().label('$i_{ph}$', loc='bottom'); elm.Ground()
    save(d, 'E1-15-iv-converter')

t = np.linspace(0, 48, 500); v = 6 + 5*np.cos(2*np.pi*(t-12)/24)
fig, ax = plt.subplots(figsize=(5.4, 2.6))
ax.plot(t, v, color='#2a6fdb', lw=2, label='$i_{ph}R$（光強度）'); ax.axhline(5, color='#d9480f', ls='--'); ax.text(0.5, 5.3, '5 V 門檻', color='#d9480f', fontsize=8)
on = v < 5; ax.fill_between(t, 0, 0.6, where=on, color='#f59f00', alpha=0.6, step='mid', label='街燈 on')
ax.set_xticks([0, 12, 24, 36, 48]); ax.set_xticklabels(['半夜', '中午', '半夜', '中午', '半夜']); ax.set_ylabel('V'); ax.legend(fontsize=8, frameon=False, loc='upper right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-15-daylight.svg')); plt.close(fig)

with drawing() as d:   # comparator -> diode -> BJT emitter follower -> R -> relay with flyback diode
    d.config(fontsize=12)
    cmp = elm.Opamp(leads=True)
    elm.Line().left().at(cmp.in1).length(1); elm.Dot(open=True).label('$i_{ph}R$', loc='left')
    elm.Line().left().at(cmp.in2).length(0.5); elm.Vdd().label('5 V') if False else None
    elm.Line().left().at(cmp.in2).length(1); elm.Dot(open=True).label('5 V', loc='left')
    elm.Line().right().at(cmp.out).length(0.8); a = elm.Dot().label('±10 V', loc='top')
    q = elm.BjtNpn(circle=True).anchor('base').at((a.center[0]+1.2, a.center[1]))
    elm.Line().left().at(q.base).tox(a.center[0])
    elm.Line().up().at(q.collector).length(1); elm.Vdd().label('10 V')
    elm.Diode().down().at(q.emitter).length(2)
    elm.Resistor().down().label('$R$', loc='bottom'); k = elm.Dot()
    rl = elm.Inductor2().down().at(k.center).label('relay', loc='bottom'); elm.Ground()
    elm.Line().right().at(k.center).length(1.8)
    elm.Diode().up().reverse().toy(k.center[1]-3.0).label('flyback', loc='bottom') if False else None
    fb = elm.Diode().down().reverse().label('flyback', loc='bottom'); elm.Ground()
    save(d, 'E1-15-street-light')
