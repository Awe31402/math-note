# E1-13 figures: integrator with Rf, Bode with/without Rf, differentiator (+R1), Bode, ringing, analog computer block diagram
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw, schemdraw.elements as elm
from schemdraw import flow
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def inv_amp(d, inelem, fb_parallel=None, label_in='$v_i$'):
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    return op, o, n

with drawing() as d:   # integrator with Rf
    op, o, n = inv_amp(d, None)
    elm.Resistor().left().at(n.center).label('$R$'); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Capacitor().right().tox(o.center[0]).label('$C$'); elm.Line().down().toy(o.center[1])
    elm.Line().up().at(n.center).length(3); elm.Resistor().right().tox(o.center[0]).label('$R_f$'); elm.Line().down().length(1.5)
    save(d, 'E1-13-integrator-rf')

with drawing() as d:   # differentiator with R1
    op, o, n = inv_amp(d, None)
    elm.Capacitor().left().at(n.center).label('$C$'); elm.Resistor().left().label('$R_1$'); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R$'); elm.Line().down().toy(o.center[1])
    save(d, 'E1-13-differentiator')

w = np.logspace(0, 6, 400); w1 = 1e3   # 1/RC
fig, axs = plt.subplots(1, 2, figsize=(8, 2.8))
axs[0].semilogx(w, 20*np.log10(w1/w), color='#888', lw=1.5, ls='--', label='沒有 $R_f$：純積分')
axs[0].semilogx(w, 20*np.log10(100/np.sqrt(1+(w/10)**2)), color='#2a6fdb', lw=2, label='有 $R_f$（$R_f = 100R$）')
axs[0].axvline(10, ls=':', color='gray'); axs[0].text(12, 45, '$1/R_fC$', fontsize=8); axs[0].axvline(1e3, ls=':', color='gray'); axs[0].text(1.2e3, 10, '$1/RC$', fontsize=8)
axs[0].text(1.2, 32, '放大', fontsize=9); axs[0].text(300, 5, '積分', fontsize=9)
axs[0].set_title('積分器', fontsize=10); axs[0].legend(fontsize=7.5, frameon=False, loc='lower left')
axs[1].semilogx(w, 20*np.log10(w/w1), color='#888', lw=1.5, ls='--', label='純微分：高頻一直放大')
axs[1].semilogx(w, 20*np.log10((w/w1)/np.sqrt(1+(w/1e5)**2)), color='#2a6fdb', lw=2, label='加 $R_1$（$R = 100R_1$）')
axs[1].axvline(1e5, ls=':', color='gray'); axs[1].text(1.2e5, -20, '$1/R_1C$', fontsize=8); axs[1].axvline(1e3, ls=':', color='gray'); axs[1].text(1.2e3, -40, '$1/RC$', fontsize=8)
axs[1].set_title('微分器', fontsize=10); axs[1].legend(fontsize=7.5, frameon=False, loc='upper left')
for a in axs: a.set_xlabel('$\\omega$ (rad/s)'); a.set_ylabel('dB'); a.spines[['top','right']].set_visible(False); a.set_ylim(-60, 60)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-13-bode.svg')); plt.close(fig)

t = np.linspace(0, 40, 2000); tri = 5 - np.where((t // 10) % 2 == 0, t % 10, 10 - t % 10)
sq = -np.where((t // 10) % 2 == 0, -1, 1)*1.0
ring = np.zeros_like(t)
for k in range(1, 4):
    t0 = 10*k; m = t >= t0; s = 2*(1 if k % 2 == 1 else -1)
    ring[m] += s*np.exp(-(t[m]-t0)/0.6)*np.cos(2*np.pi*(t[m]-t0)/0.5)
fig, axs = plt.subplots(2, 1, figsize=(5.4, 3.4), sharex=True)
axs[0].plot(t, tri, color='#888', lw=2); axs[0].set_title('輸入：±5 V 三角波', fontsize=9)
axs[1].plot(t, sq + ring*0.4, color='#d9480f', lw=1.5); axs[1].set_title('微分輸出：±1 V 方波，轉角處有高頻振盪（雜訊被放大）', fontsize=9)
axs[1].set_xlabel('$t$ (ms)')
for a in axs: a.spines[['top','right']].set_visible(False); a.axhline(0, color='k', lw=0.5)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-13-ringing.svg')); plt.close(fig)

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=12)
    s = flow.Circle(r=0.6).label('Σ')
    flow.Arrow().right(d.unit/2).label("$y''$", loc='top')
    i1 = flow.Box(w=2, h=1.2).label('積分\n$-\\int$')
    flow.Arrow().right(d.unit/2).label("$-y'$", loc='top')
    i2 = flow.Box(w=2, h=1.2).label('積分\n$-\\int$')
    flow.Arrow().right(d.unit/2).label('$y$', loc='top'); yo = elm.Dot()
    elm.Line().down().at(yo.center).length(2.2); elm.Line().left().tox(s.S[0]+0.3); flow.Arrow().up().toy(s.S[1]).label('$-k_1 y$', loc='left')
    elm.Line().down().at(i1.E).length(1.2); inv = flow.Box(w=1.6, h=1).anchor('N').label('反相').at((i1.E[0]+0.0, i1.E[1]-1.2))
    flow.Arrow().left().at(inv.W).tox(s.S[0]-0.3) ; elm.Line().up().toy(s.S[1]-0.0)
    flow.Arrow().right().at((s.W[0]-2.5, s.W[1])).to(s.W).label('$F_a/m$', loc='top')
    save(d, 'E1-13-analog-computer')
