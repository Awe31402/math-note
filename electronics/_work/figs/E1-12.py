# E1-12 figures: Miller integrator, step/square responses, integrator Bode, offset model
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

with drawing() as d:
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    elm.Resistor().left().at(n.center).label('$R$').label('$i = v_i/R$ →', loc='bottom'); elm.Dot(open=True).label('$v_i$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Capacitor().right().tox(o.center[0]).label('$C$'); elm.Line().down().toy(o.center[1])
    save(d, 'E1-12-integrator')

fig, axs = plt.subplots(2, 2, figsize=(7.6, 4.2), sharex='col')
t = np.linspace(0, 16, 800)
vin = np.where(t < 10, 1, 0); vout = -np.minimum(t, 10)
axs[0,0].plot(t, vin, color='#888', lw=2); axs[0,0].set_title('輸入：1 V 持續 10 ms', fontsize=9)
axs[1,0].plot(t, vout, color='#2a6fdb', lw=2); axs[1,0].axhline(-13, ls=':', color='#d9480f'); axs[1,0].text(0.5, -12.3, '−13 V 飽和', fontsize=8, color='#d9480f')
axs[1,0].set_title('輸出：每 ms 掉 1 V，停在 −10 V', fontsize=9); axs[1,0].set_xlabel('$t$ (ms)')
t2 = np.linspace(0, 40, 800); sq = np.where((t2 // 10) % 2 == 0, 1, -1)
tri = 5 - np.where((t2 // 10) % 2 == 0, t2 % 10, 10 - t2 % 10)
axs[0,1].plot(t2, sq, color='#888', lw=2); axs[0,1].set_title('輸入：±1 V 方波，半週期 10 ms', fontsize=9)
axs[1,1].plot(t2, tri, color='#2a6fdb', lw=2); axs[1,1].set_yticks([-5, 0, 5]); axs[1,1].set_title('輸出：±5 V 三角波', fontsize=9); axs[1,1].set_xlabel('$t$ (ms)')
for a in axs.flat: a.spines[['top','right']].set_visible(False); a.axhline(0, color='k', lw=0.5)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-12-step-square.svg')); plt.close(fig)

w = np.logspace(1, 5, 200)
fig, ax = plt.subplots(figsize=(4.4, 2.6))
ax.semilogx(w, 20*np.log10(1e3/w), color='#2a6fdb', lw=2); ax.axvline(1e3, ls=':', color='gray'); ax.axhline(0, color='k', lw=0.5)
ax.text(1.1e3, 15, '$\\omega_0 = 1/RC = 10^3$', fontsize=8); ax.text(2e3, -30, '−20 dB/decade', fontsize=8)
ax.set_xlabel('$\\omega$ (rad/s)'); ax.set_ylabel('$|v_o/v_i|$ (dB)'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-12-integrator-bode.svg')); plt.close(fig)

t = np.linspace(0, 300, 400)
fig, ax = plt.subplots(figsize=(4.4, 2.4))
ax.plot(t, np.minimum(13, 5e-5/1e-3*t), color='#d9480f', lw=2); ax.axhline(13, ls=':', color='gray'); ax.text(5, 11.5, '+13 V 飽和', fontsize=8)
ax.set_xlabel('$t$ (s)'); ax.set_ylabel('$v_o$ (V)'); ax.set_title('只有 offset、沒有輸入：約 260 s 積到飽和', fontsize=9); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-12-offset-runaway.svg')); plt.close(fig)
