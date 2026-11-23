# E2-05 figures: center-tapped full-wave, bridge, diode regulator (+ model), zener regulator, full-wave ripple
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:   # center-tapped full wave: two sources in series, middle grounded
    s1 = elm.SourceSin().up().label('$v_s$', loc='top'); g = s1.start
    elm.Ground().at(g)
    s2 = elm.SourceSin().down().at(g).label('$v_s$', loc='top')
    elm.Line().right().at(s1.end).length(0.8); elm.Diode().right().length(1.8).label('$D_1$'); o = elm.Dot().label('$v_O$', loc='top')
    elm.Line().right().at(s2.end).length(0.8); elm.Diode().right().length(1.8).label('$D_2$', loc='bottom'); b = elm.Dot()
    elm.Line().up().at(b.center).toy(o.center[1])
    elm.Line().right().at(o.center).length(1.5); c = elm.Dot()
    elm.Capacitor().down().at(c.center).toy(g[1]).label('$C$', loc='bottom'); elm.Ground()
    elm.Line().right().at(c.center).length(1.5); elm.Resistor().down().toy(g[1]).label('$R$', loc='bottom'); elm.Ground()
    save(d, 'E2-05-center-tap')

with drawing() as d:   # bridge
    s = elm.SourceSin().up().label('$v_s$', loc='top')
    top = s.end; bot = s.start
    elm.Line().right().at(top).length(1.5); A = elm.Dot()
    elm.Line().right().at(bot).length(1.5); B = elm.Dot()
    # node P (+) to the right, node N (-) further
    P = (A.center[0]+2.5, A.center[1]+1.0); N = (A.center[0]+2.5, B.center[1]-1.0)
    elm.Diode().at(A.center).to(P).label('$D_1$')
    elm.Diode().at(B.center).to(P).label('$D_2$', loc='bottom')
    elm.Diode().at(N).to(A.center).label('$D_4$')
    elm.Diode().at(N).to(B.center).label('$D_3$', loc='bottom')
    elm.Line().right().at(P).length(2); o = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().at(o.center).toy(N[1]).label('$R$', loc='bottom'); elm.Line().left().tox(N[0])
    elm.Ground().at(N)
    save(d, 'E2-05-bridge')

with drawing() as d:   # diode regulator and its model
    v = elm.BatteryCell().up().reverse().label('$V_{DC}$ 10 V', loc='top'); elm.Ground().at(v.start)
    elm.Resistor().right().at(v.end).label('$R$ = 1 kΩ'); o = elm.Dot().label('$v_O$ ≈ 0.7 V', loc='top')
    elm.Diode().down().at(o.center).toy(v.start[1]).label('$I_Q$ ↓', loc='bottom'); elm.Ground()
    x0 = o.center[0] + 3.5
    v2 = elm.BatteryCell().up().reverse().at((x0, v.start[1])).label('$V_{DC}$', loc='top'); elm.Ground().at(v2.start)
    elm.Resistor().right().at(v2.end).label('$R$'); o2 = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().at(o2.center).length(1.4).label('$r_d$', loc='bottom')
    elm.BatteryCell().down().label('≈0.7 V', loc='bottom').toy(v2.start[1]); elm.Ground()
    save(d, 'E2-05-diode-regulator')

with drawing() as d:   # zener regulator
    v = elm.BatteryCell().up().reverse().label('$V_{DC}$', loc='top'); elm.Ground().at(v.start)
    elm.Resistor().right().at(v.end).label('$R$'); o = elm.Dot().label('$v_O ≈ V_{Z0}$', loc='top')
    elm.Zener().down().at(o.center).toy(v.start[1]).reverse().label('$r_z$ = 1 Ω', loc='bottom'); elm.Ground()
    save(d, 'E2-05-zener')

T = 1/60; tt = np.linspace(0, 3*T, 3000); vs = 10*np.abs(np.sin(2*np.pi*60*tt)); RC = 0.05
def env(src):
    vo = np.zeros_like(tt)
    for k in range(1, len(tt)): vo[k] = max(src[k], vo[k-1]*np.exp(-(tt[k]-tt[k-1])/RC))
    return vo
half = env(10*np.maximum(np.sin(2*np.pi*60*tt), 0)); full = env(vs)
fig, ax = plt.subplots(figsize=(5.6, 2.6))
ax.plot(tt*1e3, vs, color='#ddd', label='$|v_s|$'); ax.plot(tt*1e3, half, color='#aaa', ls='--', label='半波')
ax.plot(tt*1e3, full, color='#2a6fdb', lw=2, label='全波：漣波約減半')
ax.set_xlabel('$t$ (ms)'); ax.set_ylabel('V'); ax.set_ylim(0, 11); ax.legend(fontsize=7.5, frameon=False, loc='lower right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-05-fullwave-ripple.svg')); plt.close(fig)
