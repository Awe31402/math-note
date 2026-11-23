# E2-07 figures: push-pull current amp, vOP waveforms for 0/1/2 diodes, parallel RLC tuner + response
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:   # op amp + complementary BJT push-pull with feedback
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(1); elm.Dot(open=True).label('$v_I$', loc='left')
    elm.Line().right().at(op.out).length(1); b = elm.Dot().label('$v_{OP}$', loc='bottom')
    elm.Line().up().at(b.center).length(1.2); elm.Line().right().length(0.6)
    qn = elm.BjtNpn(circle=True).anchor('base').label('NPN', loc='right')
    elm.Line().down().at(b.center).length(1.2); elm.Line().right().length(0.6)
    qp = elm.BjtPnp(circle=True).anchor('base').label('PNP', loc='right')
    elm.Line().up().at(qn.collector).length(0.6); elm.Vdd().label('+15 V')
    elm.Line().down().at(qp.collector).length(0.6); elm.Vss().label('−15 V')
    elm.Line().at(qn.emitter).to(qp.emitter); 
    o = elm.Dot().at(((qn.emitter[0]+qp.emitter[0])/2, (qn.emitter[1]+qp.emitter[1])/2))
    elm.Line().right().at(o.center).length(1.5); oo = elm.Dot().label('$v_O$', loc='top')
    elm.Resistor().down().at(oo.center).label('$R_L$', loc='bottom'); elm.Ground()
    elm.Line().up().at(oo.center).length(4.6); elm.Line().left().tox(op.in1[0]-0.6); elm.Line().down().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    save(d, 'E2-07-push-pull')

t = np.linspace(0, 2, 2000); vo = 3*np.sin(2*np.pi*t)
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.5), sharey=True)
cases = [('沒有二極體：每次過零跳 1.4 V', np.where(vo >= 0, vo+0.7, vo-0.7)),
         ('一顆二極體：負半週跳 0.7 V', np.where(vo >= 0, vo+0.7, vo)),
         ('兩顆二極體：連續，不用跳', vo+0.7)]
for a, (ttl, vop) in zip(axs, cases):
    a.plot(t, vo, color='#2a6fdb', lw=1.5, label='理想 $v_O$'); a.plot(t, vop, color='#d9480f', lw=1.5, label='op amp 要給的 $v_{OP}$')
    a.set_title(ttl, fontsize=9); a.axhline(0, color='k', lw=0.5); a.set_xticks([]); a.spines[['top','right']].set_visible(False)
axs[0].legend(fontsize=7, frameon=False, loc='lower left')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-07-crossover.svg')); plt.close(fig)

with drawing() as d:   # receiver tuner: current source || L || C || R -> voltage amp
    s = elm.SourceI().up().label('$i_s$', loc='top'); elm.Ground().at(s.start)
    elm.Line().right().at(s.end).length(2); n1 = elm.Dot()
    elm.Inductor2().down().toy(s.start[1]).label('$L$', loc='bottom')
    elm.Line().right().at(n1.center).length(2); n2 = elm.Dot()
    elm.Capacitor().down().toy(s.start[1]).label('$C$', loc='bottom')
    elm.Line().right().at(n2.center).length(2); n3 = elm.Dot().label('$v$', loc='top')
    elm.Resistor().down().toy(s.start[1]).label('$R$', loc='bottom')
    elm.Line().left().at((n3.center[0], s.start[1])).tox(s.start[0])
    elm.Line().right().at(n3.center).length(1.0)
    elm.Opamp(leads=True).anchor('in2').right().label('$A_v$', loc='center')
    save(d, 'E2-07-tuner')

w0 = 1.0; R = 1; Q = 20; C = Q/(w0*R); L = 1/(w0**2*C)
w = np.linspace(0.8, 1.2, 1500); Z = 1/(1/R + 1j*w*C + 1/(1j*w*L))
fig, axs = plt.subplots(1, 2, figsize=(8.4, 2.6))
axs[0].plot(w, np.abs(Z), color='#2a6fdb', lw=2); axs[0].axhline(1/np.sqrt(2), color='#d9480f', lw=0.8, ls=':')
axs[0].text(0.81, 0.73, '$R/\\sqrt{2}$', color='#d9480f', fontsize=8)
B = 1/(R*C); axs[0].annotate('', (w0-B/2, 0.707), (w0+B/2, 0.707), arrowprops=dict(arrowstyle='<->', color='#2f9e44'))
axs[0].text(w0+B/2+0.005, 0.6, '$B = 1/RC$', color='#2f9e44', fontsize=8)
axs[0].set_title('$|Z|$：在 $\\omega_0 = 1/\\sqrt{LC}$ 最大，等於 $R$', fontsize=9)
axs[1].plot(w, np.degrees(np.angle(Z)), color='#2a6fdb', lw=2); axs[1].set_yticks([-90, -45, 0, 45, 90])
axs[1].set_title('相位：+90° → 0° → −90°（$\\pm 45°$ 在頻寬兩端）', fontsize=9)
for a in axs: a.set_xticks([w0]); a.set_xticklabels(['$\\omega_0$']); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-07-tuner-response.svg')); plt.close(fig)
