# E1-19 figures: open-loop vs closed-loop Bode (GBW), step response initial slope, slew-limited sine
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

w = np.logspace(0, 7, 400); Ad = 1e5; w0 = 10
fig, ax = plt.subplots(figsize=(5.4, 3.0))
ax.semilogx(w, 20*np.log10(Ad/np.sqrt(1+(w/w0)**2)), color='#888', lw=2, label='op amp 本身：$A_d = 10^5$，$\\omega_0 = 10$')
for G, c in [(100, '#2f9e44'), (10, '#2a6fdb'), (1, '#d9480f')]:
    wb = 1e6/G; ax.semilogx(w, 20*np.log10(G/np.sqrt(1+(w/wb)**2)), color=c, lw=1.8, label=f'回授增益 {G}：頻寬 $10^{{{int(np.log10(wb))}}}$')
ax.axvline(1e6, ls=':', color='gray'); ax.text(1.2e6, 60, '$\\omega_t = 10^6$', fontsize=8)
ax.set_xlabel('$\\omega$ (rad/s)'); ax.set_ylabel('dB'); ax.set_ylim(-10, 110); ax.legend(fontsize=7.5, frameon=False, loc='upper right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-19-gbw.svg')); plt.close(fig)

t = np.linspace(0, 5, 400)
fig, axs = plt.subplots(1, 2, figsize=(7.8, 2.7))
for G, tau, c in [(1, 1, '#d9480f'), (10, 10, '#2a6fdb')]:
    axs[0].plot(t, 0.1*G*(1-np.exp(-t/tau)), color=c, lw=2, label=f'增益 {G}')
axs[0].plot([0, 1], [0, 0.1], ls='--', color='k', lw=1); axs[0].text(1.05, 0.11, '起始斜率相同 $= v_i\\,\\omega_t$', fontsize=8)
axs[0].set_title('步階輸入 0.1 V：兩種增益的輸出', fontsize=9); axs[0].set_xlabel('$t$（單位 μs）'); axs[0].set_ylabel('$v_o$ (V)'); axs[0].legend(fontsize=8, frameon=False, loc='center right')
vin = np.array([0.1, 0.5, 0.8, 1.0, 1.5, 2.0]); slope = np.minimum(vin*1e6, 1e6)
axs[1].plot(vin, slope/1e6, 'o-', color='#2a6fdb'); axs[1].axhline(1, ls='--', color='#d9480f'); axs[1].text(0.1, 1.05, 'slew rate $10^6$ V/s', color='#d9480f', fontsize=8)
axs[1].set_title('起始斜率 vs 輸入大小（電壓追隨器）', fontsize=9); axs[1].set_xlabel('$v_i$ (V)'); axs[1].set_ylabel('斜率（$10^6$ V/s）'); axs[1].set_ylim(0, 1.25)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-19-step-slope.svg')); plt.close(fig)

dt = 1e-8; T = 2*np.pi/1e5; tt = np.arange(0, 2*T, dt); target = 15*np.sin(1e5*tt)
out = np.zeros_like(tt); SR = 1e6
for k in range(1, len(tt)):
    d = target[k] - out[k-1]; out[k] = out[k-1] + np.clip(d, -SR*dt, SR*dt)
fig, ax = plt.subplots(figsize=(5.4, 2.6))
ax.plot(tt*1e6, target, color='#bbb', ls='--', label='理想輸出 15 V（$\\omega = 10^5$）'); ax.plot(tt*1e6, out, color='#d9480f', lw=2, label='slew rate 限制後')
ax.plot(tt*1e6, 10*np.sin(1e5*tt), color='#2a6fdb', lw=1.2, label='10 V：剛好不受限')
ax.set_xlabel('$t$ (μs)'); ax.set_ylabel('V'); ax.legend(fontsize=7.5, frameon=False, loc='lower left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-19-slew-sine.svg')); plt.close(fig)
