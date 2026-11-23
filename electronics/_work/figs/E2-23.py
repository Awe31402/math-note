# E2-23 figures: PWM generation; Early effect output curves
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
t = np.linspace(0, 1, 6000); f = 12
saw = 5*((t*f) % 1); V = 2.5 + 1.8*np.sin(2*np.pi*t)
pwm = np.where(V > saw, 5, 0)
fig, axs = plt.subplots(2, 1, figsize=(7.0, 3.6), sharex=True)
axs[0].plot(t, saw, color='#aaa', lw=0.8, label='鋸齒波 0–5 V（高頻）'); axs[0].plot(t, V, color='#d9480f', lw=2, label='$V = 2.5 + v_i$（聲音）')
axs[0].legend(fontsize=7.5, frameon=False, loc='upper right', ncol=2); axs[0].set_ylim(-0.3, 6.3); axs[0].set_yticks([0, 2.5, 5])
axs[1].plot(t, pwm, color='#2a6fdb', lw=0.8, label='PWM（工作週期 $D = V/5$）')
axs[1].plot(t, V, color='#2f9e44', lw=2, ls='--', label='低通取平均 $= 5D = V$')
axs[1].legend(fontsize=7.5, frameon=False, loc='upper right', ncol=2); axs[1].set_ylim(-0.3, 6.3); axs[1].set_yticks([0, 5])
for a in axs: a.spines[['top','right']].set_visible(False)
axs[1].set_xticks([])
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-23-pwm.svg')); plt.close(fig)

VA = 50; k = 2; Vt = 1
v = np.linspace(-VA, 12, 800)
fig, ax = plt.subplots(figsize=(6.0, 2.8))
for vgs, c in [(3, '#2a6fdb'), (2.5, '#4dabf7'), (2, '#f08c00')]:
    vov = vgs - Vt; IQ = k/2*vov**2
    sat = IQ*(1 + v/VA); vd = np.linspace(0, vov, 50)
    ax.plot(v[v >= vov], sat[v >= vov], color=c, lw=2, label=f'$V_{{GS}}$ = {vgs} V')
    ax.plot(vd, k*(vov*vd - vd**2/2)*(1 + vd/VA), color=c, lw=2)
    ax.plot(v[v < vov], sat[v < vov], color=c, lw=0.8, ls=':')
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.plot(-VA, 0, 'o', color='#d9480f'); ax.text(-VA+1, 0.25, '$-V_A$', color='#d9480f')
ax.set_xlabel('$V_{DS}$ (V)'); ax.set_ylabel('$I_D$ (mA)'); ax.set_xlim(-VA-3, 12); ax.set_ylim(-0.2, 5.5)
ax.set_title('飽和區斜上去，延長線交在 $-V_A$；斜率倒數 $r_o = V_A/I_Q$', fontsize=9)
ax.legend(fontsize=7, frameon=False, loc='upper left'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-23-early.svg')); plt.close(fig)
