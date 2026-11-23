# E1-20 figures: op-amp current limit waveform, super diode (npn in loop), push-pull output stage, waveforms
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

t = np.linspace(0, 2, 500); s = np.sin(2*np.pi*t)
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.4), sharey=True)
axs[0].plot(t, s, color='#bbb', ls='--', label='想要的 1 V'); axs[0].plot(t, np.clip(s, -0.13, 0.13), color='#d9480f', lw=2, label='op amp 直接推 10 Ω')
axs[0].set_title('只有 op amp：電流 13 mA → ±0.13 V', fontsize=9)
axs[1].plot(t, s, color='#bbb', ls='--'); axs[1].plot(t, np.maximum(s, 0), color='#2a6fdb', lw=2, label='只有 npn')
axs[1].set_title('npn 放在回授裡：只剩正半週', fontsize=9)
axs[2].plot(t, s, color='#2f9e44', lw=2, label='npn + pnp 推挽'); axs[2].set_title('推挽：完整重現', fontsize=9)
for a in axs: a.set_xticks([]); a.axhline(0, color='k', lw=0.5); a.legend(fontsize=7.5, frameon=False, loc='lower left'); a.spines[['top','right']].set_visible(False)
axs[0].set_ylabel('$v_o$ (V)')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-20-waveforms.svg')); plt.close(fig)

with drawing() as d:   # push-pull output stage inside op-amp loop
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(1); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().right().at(op.out).length(1.0); b = elm.Dot()
    q1 = elm.BjtNpn(circle=True).anchor('base').at((b.center[0]+0.8, b.center[1]+1.0))
    q2 = elm.BjtPnp(circle=True).anchor('base').at((b.center[0]+0.8, b.center[1]-1.0))
    elm.Line().up().at(b.center).toy(q1.base[1]); elm.Line().right().tox(q1.base[0])
    elm.Line().down().at(b.center).toy(q2.base[1]); elm.Line().right().tox(q2.base[0])
    elm.Line().up().at(q1.collector).length(0.8); elm.Vdd().label('+10 V')
    elm.Line().down().at(q2.collector).length(0.8); elm.Vss().label('−10 V')
    elm.Line().down().at(q1.emitter).toy(b.center[1]); e = elm.Dot()
    elm.Line().up().at(q2.emitter).toy(b.center[1])
    elm.Line().right().at(e.center).length(1.5); o = elm.Dot().label('$v_o$', loc='top')
    elm.Resistor().down().at(o.center).label('$R_L$（喇叭）', loc='bottom') if False else elm.Resistor().down().at(o.center).label('$R_L$', loc='bottom')
    elm.Ground()
    elm.Line().up().at(o.center).length(4.0); elm.Line().left().tox(op.in1[0]-0.6); elm.Line().down().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    save(d, 'E1-20-push-pull')
