# E2-04 figures: superdiode, its waveforms, two-diode precision rectifier, peak rectifier + ripple
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:   # superdiode
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(1); elm.Dot(open=True).label('$v_I$', loc='left')
    elm.Diode().right().at(op.out).length(2).label('$v_{OP}$ →', loc='bottom', ofst=(-1.2, 0)); o = elm.Dot().label('$v_O$', loc='right')
    elm.Resistor().down().at(o.center).label('$R$', loc='bottom'); elm.Ground()
    elm.Line().up().at(o.center).length(2.0); elm.Line().left().tox(op.in1[0]-0.6); elm.Line().down().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    save(d, 'E2-04-superdiode')

with drawing() as d:   # two-diode precision rectifier (inverting)
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    elm.Resistor().left().at(n.center).label('$R_1$'); elm.Dot(open=True).label('$v_I$', loc='left')
    elm.Line().right().at(op.out).length(0.8); p = elm.Dot().label('$v_{OP}$', loc='bottom')
    elm.Line().up().at(n.center).length(1.4); a = elm.Dot()
    elm.Diode().right().tox(p.center[0]).label('$D_1$'); elm.Line().down().toy(p.center[1])
    elm.Line().up().at(a.center).length(1.4); b = elm.Dot()
    elm.Resistor().right().length(4).label('$R_2$'); o = elm.Dot().label('$v_O$', loc='right')
    elm.Diode().down().at(o.center).toy(p.center[1]+0.0).reverse().label('$D_2$', loc='bottom') if False else None
    elm.Line().down().at(o.center).length(1.0); elm.Diode().down().toy(p.center[1]).reverse().label('$D_2$', loc='bottom'); elm.Line().left().tox(p.center[0])
    elm.Line().right().at(o.center).length(2.0); elm.Resistor().down().label('$R$', loc='bottom'); elm.Ground()
    save(d, 'E2-04-precision-rectifier')

t = np.linspace(0, 3, 900); vi = np.sin(2*np.pi*t)
fig, axs = plt.subplots(1, 2, figsize=(8.4, 2.6))
axs[0].plot(t, vi, color='#bbb', label='$v_I$'); axs[0].plot(t, np.maximum(vi, 0), color='#2a6fdb', lw=2, label='$v_O$')
axs[0].plot(t, np.where(vi > 0, vi+0.7, -13)/6, color='#d9480f', lw=1.5, label='$v_{OP}$（縮小 6 倍畫）')
axs[0].set_title('super diode：負半週 op amp 飽和在 −13 V', fontsize=9); axs[0].legend(fontsize=7, frameon=False, loc='lower left')
axs[1].plot(t, vi, color='#bbb', label='$v_I$'); axs[1].plot(t, np.where(vi < 0, -2*vi, 0), color='#2a6fdb', lw=2, label='$v_O = -\\frac{R_2}{R_1}v_I$（負半週）')
axs[1].plot(t, np.where(vi >= 0, -0.7, -2*vi+0.7), color='#d9480f', lw=1.5, label='$v_{OP}$：不飽和')
axs[1].set_title('兩顆二極體：op amp 一直有回授', fontsize=9); axs[1].legend(fontsize=7, frameon=False, loc='upper right')
for a in axs: a.set_xticks([]); a.axhline(0, color='k', lw=0.5); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-04-superdiode-waves.svg')); plt.close(fig)

with drawing() as d:   # peak rectifier (transformer secondary shown as source)
    s = elm.SourceSin().up().label('$v_s$', loc='top'); elm.Ground().at(s.start)
    elm.Diode().right().at(s.end).length(2.5); o = elm.Dot().label('$v_O$', loc='top')
    elm.Capacitor().down().at(o.center).toy(s.start[1]).label('$C$', loc='bottom'); elm.Ground()
    elm.Line().right().at(o.center).length(2); elm.Resistor().down().toy(s.start[1]).label('$R$', loc='bottom'); elm.Ground()
    save(d, 'E2-04-peak-rectifier')

T = 1/60; tt = np.linspace(0, 3*T, 2000); vs = 10*np.sin(2*np.pi*60*tt); vo = np.zeros_like(tt); RC = 0.05
for k in range(1, len(tt)):
    dec = vo[k-1]*np.exp(-(tt[k]-tt[k-1])/RC)
    vo[k] = max(vs[k], dec)
fig, ax = plt.subplots(figsize=(5.6, 2.6))
ax.plot(tt*1e3, vs, color='#bbb', label='$v_s = V_p\\sin\\omega t$'); ax.plot(tt*1e3, vo, color='#2a6fdb', lw=2, label='$v_O$（忽略 0.7 V）')
ax.annotate('', (36.2, 10), (36.2, vo[np.searchsorted(tt*1e3, 36.2)]), arrowprops=dict(arrowstyle='<->', color='#d9480f')); ax.text(37, 8.3, '$V_r$', color='#d9480f')
ax.set_xlabel('$t$ (ms)'); ax.set_ylabel('V'); ax.set_ylim(-11, 12); ax.legend(fontsize=7.5, frameon=False, loc='lower left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-04-ripple.svg')); plt.close(fig)
