# E1-21 figures: base-drive waveforms for 0/1/2 diodes, push-pull with diodes, audio system block diagram
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw, schemdraw.elements as elm
from schemdraw import flow
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

t = np.linspace(0, 2, 800); vo = 1.5*np.sin(2*np.pi*t)
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.6), sharey=True)
for a, nd, title in zip(axs, [0, 1, 2], ['沒有二極體：跳 1.4 V', '一顆二極體：跳 0.7 V', '兩顆二極體：連續（但靜態有電流）']):
    up = vo + 0.7; dn = vo - 0.7 + 0.7*nd
    vb = np.where(vo >= 0, up, dn)
    a.plot(t, vo, color='#2a6fdb', lw=1.5, label='理想 $v_o$'); a.plot(t, vb, color='#d9480f', lw=2, label='op amp 輸出 $v_B$（上管基極）')
    a.set_title(title, fontsize=9); a.axhline(0, color='k', lw=0.5); a.set_xticks([]); a.spines[['top','right']].set_visible(False)
axs[0].legend(fontsize=7, frameon=False, loc='lower left'); axs[0].set_ylabel('V')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-21-vb-diodes.svg')); plt.close(fig)

with drawing() as d:   # push-pull with one diode between bases and R to -10 V
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(1); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().right().at(op.out).length(0.8); b1 = elm.Dot().label('$v_B$', loc='top')
    q1 = elm.BjtNpn(circle=True).anchor('base').at((b1.center[0]+1.0, b1.center[1]))
    elm.Line().right().at(b1.center).tox(q1.base[0])
    dd = elm.Diode().down().at(b1.center).length(2.8); b2 = elm.Dot()
    q2 = elm.BjtPnp(circle=True).anchor('base').at((b2.center[0]+1.0, b2.center[1]))
    elm.Line().right().at(b2.center).tox(q2.base[0])
    elm.Line().left().at(b2.center).length(1.2); elm.Resistor().down().length(2).label('$R$', loc='top'); elm.Vss().label('−10 V')
    elm.Line().up().at(q1.collector).length(0.6); elm.Vdd().label('+10 V')
    elm.Line().down().at(q2.collector).length(0.6); elm.Vss().label('−10 V')
    elm.Line().down().at(q1.emitter).toy((q1.emitter[1]+q2.emitter[1])/2); e = elm.Dot()
    elm.Line().up().at(q2.emitter).toy(e.center[1])
    elm.Line().right().at(e.center).length(1.5); o = elm.Dot().label('$v_o$', loc='top')
    elm.Resistor().down().at(o.center).label('$R_L$', loc='bottom'); elm.Ground()
    elm.Line().up().at(o.center).length(4.6); elm.Line().left().tox(op.in1[0]-0.6); elm.Line().down().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    save(d, 'E1-21-push-pull-diode')

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=11)
    m = flow.Box(w=2.2, h=1.3).label('麥克風\n$v_i$ + 2 V')
    flow.Arrow().right(1.0)
    h = flow.Box(w=2.2, h=1.3).label('CR 高通\n擋 2 V 直流')
    flow.Arrow().right(1.0)
    a1 = flow.Box(w=2.0, h=1.3).label('放大 ×10\n頻寬 $10^5$')
    flow.Arrow().right(1.0)
    a2 = flow.Box(w=2.0, h=1.3).label('放大 ×10\n頻寬 $10^5$')
    flow.Arrow().down(1.0).at(a2.S)
    lp = flow.Box(w=2.2, h=1.3).anchor('N').label('$R_0C_0$ 低通\n濾高頻雜訊')
    flow.Arrow().left(1.0).at(lp.W)
    out = flow.Box(w=2.6, h=1.3).anchor('E').label('推挽輸出級\nop amp + BJT')
    flow.Arrow().left(1.0).at(out.W)
    sp = flow.Box(w=1.6, h=1.3).anchor('E').label('喇叭\n4–8 Ω')
    save(d, 'E1-21-audio-system')
