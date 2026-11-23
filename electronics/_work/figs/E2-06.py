# E2-06 figures: ripple with zener, op amp + BJT regulator, AM rectified waveform, spectrum
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 1. decay toward 0 vs toward Vz0
t = np.linspace(0, 1/60, 400); RC = 0.02; Vp = 10; Vz = 5
fig, ax = plt.subplots(figsize=(5.4, 2.6))
ax.plot(t*1e3, Vp*np.exp(-t/RC), color='#aaa', ls='--', label='只有 $R$：趨近 0')
ax.plot(t*1e3, (Vp-Vz)*np.exp(-t/RC)+Vz, color='#2a6fdb', lw=2, label='接崩潰二極體：趨近 $V_{Z0}$')
ax.axhline(Vz, color='#d9480f', lw=0.8, ls=':'); ax.text(0.3, 4.3, '$V_{Z0}$ = 5 V', color='#d9480f', fontsize=8)
ax.set_xlabel('$t$ (ms)，從峰值開始放電'); ax.set_ylabel('$v$ (V)'); ax.set_ylim(0, 10.5)
ax.legend(fontsize=7.5, frameon=False, loc='upper right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-06-zener-decay.svg')); plt.close(fig)

# 2. op amp + BJT regulator
with drawing() as d:
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(2.5); z = elm.Dot().label('$V_{Z0}$', loc='top')
    elm.Zener().down().at(z.center).reverse().length(2); elm.Ground()
    elm.Resistor().up().at(z.center).length(2).label('$R$', loc='bottom'); elm.Dot(open=True).label('$V_{DC}$', loc='top')
    elm.Line().right().at(op.out).length(0.8)
    q = elm.BjtNpn(circle=True).anchor('base').label('BJT', loc='right')
    elm.Line().up().at(q.collector).length(1); elm.Dot(open=True).label('$V_{DC}$', loc='top')
    elm.Line().down().at(q.emitter).length(0.8); o = elm.Dot().label('$v_O$', loc='right')
    elm.Line().right().at(o.center).length(1.5); elm.Resistor().down().label('$R_L$', loc='bottom'); elm.Ground()
    elm.Resistor().down().at(o.center).label('$R_2$', loc='bottom'); m = elm.Dot()
    elm.Resistor().down().label('$R_1$', loc='bottom'); elm.Ground()
    elm.Line().left().at(m.center).tox(op.in1[0]-0.6); elm.Line().up().toy(op.in1[1]); elm.Line().right().tox(op.in1[0])
    save(d, 'E2-06-opamp-bjt-regulator')

# 3. AM waveform and rectified
tt = np.linspace(0, 1, 4000); fm, fc, m = 1, 30, 0.5
am = (1+m*np.sin(2*np.pi*fm*tt))*np.sin(2*np.pi*fc*tt)
fig, axs = plt.subplots(1, 2, figsize=(8.4, 2.5), sharey=True)
axs[0].plot(tt, am, color='#2a6fdb', lw=0.8); axs[0].plot(tt, 1+m*np.sin(2*np.pi*fm*tt), color='#d9480f', lw=1, ls='--', label='包絡 $A[1+mf(t)]$')
axs[0].set_title('AM 信號（$m$ = 0.5，1.5A 到 0.5A）', fontsize=9); axs[0].legend(fontsize=7, frameon=False, loc='lower left')
rect = np.maximum(am, 0)
axs[1].plot(tt, rect, color='#2a6fdb', lw=0.8, label='整流後')
axs[1].plot(tt, (1+m*np.sin(2*np.pi*fm*tt))/np.pi, color='#d9480f', lw=2, label='低通後 $\\frac{A}{\\pi}[1+mf(t)]$')
axs[1].set_title('整流 → 低通濾波', fontsize=9); axs[1].legend(fontsize=7, frameon=False, loc='lower left')
for a in axs: a.set_xticks([]); a.axhline(0, color='k', lw=0.5); a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-06-am-rectify.svg')); plt.close(fig)

# 4. spectrum after rectification
fig, ax = plt.subplots(figsize=(5.8, 2.4))
def band(x, h, c):
    ax.fill_between([x-0.12, x+0.12], 0, h, color=c, alpha=0.6)
ax.vlines(0, 0, 1/np.pi, color='#2a6fdb', lw=3); ax.text(0.05, 0.33, 'DC $A/\\pi$', fontsize=8)
ax.fill_between([0.02, 0.15], 0, 0.5/np.pi, color='#d9480f', alpha=0.7); ax.text(0.18, 0.17, '聲音 $Am/\\pi$', fontsize=8, color='#d9480f')
for k, h in [(1, 0.25), (2, 0.2), (4, 0.08), (6, 0.05)]: band(k, h, '#888')
ax.plot([0, 0.5, 0.8], [0.42, 0.42, 0.0], color='#2f9e44', lw=1.5); ax.text(0.5, 0.44, '低通濾波器', color='#2f9e44', fontsize=8)
ax.set_xticks([0, 1, 2, 4, 6]); ax.set_xticklabels(['0', '$f_c$', '$2f_c$', '$4f_c$', '$6f_c$'])
ax.set_yticks([]); ax.set_xlim(-0.2, 6.6); ax.set_ylim(0, 0.5); ax.spines[['top','right','left']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-06-am-spectrum.svg')); plt.close(fig)
