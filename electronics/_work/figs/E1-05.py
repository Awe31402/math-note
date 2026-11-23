# E1-05 figures: AC charging (low/high freq), capacitor reactance, RC low-pass response, voice band placement
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
def sv(fig, n): fig.tight_layout(); fig.savefig(os.path.join(OUT, n + '.svg')); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(7.8, 2.6))
t = np.linspace(0, 2, 500)
axs[0].plot(t, np.sin(np.pi*t), color='#888', lw=3, label='$v_s$'); axs[0].plot(t, 0.98*np.sin(np.pi*t-0.1), color='#2a6fdb', lw=1.5, label='$v_O$')
axs[0].set_title('$\\omega \\ll \\omega_0$（$T/2 \\gg \\tau$）：$v_O \\approx v_s$', fontsize=10)
axs[0].plot([0, 0.1], [-1.25, -1.25], color='#d9480f', lw=3); axs[0].text(0.15, -1.33, '$\\tau$', color='#d9480f')
t2 = np.linspace(0, 2, 500)
axs[1].plot(t2, np.sin(10*np.pi*t2), color='#888', lw=1.5, label='$v_s$'); axs[1].plot(t2, 0.1*np.sin(10*np.pi*t2-1.5), color='#2a6fdb', lw=2, label='$v_O$')
axs[1].set_title('$\\omega \\gg \\omega_0$（$T/2 \\ll \\tau$）：$v_O \\approx 0$', fontsize=10)
axs[1].plot([0, 1], [-1.25, -1.25], color='#d9480f', lw=3); axs[1].text(1.05, -1.33, '$\\tau$', color='#d9480f')
for a in axs: a.set_yticks([]); a.set_xticks([]); a.set_ylim(-1.5, 1.3); a.axhline(0, color='k', lw=0.5); a.legend(fontsize=8, frameon=False, loc='upper right'); a.spines[['top','right']].set_visible(False)
sv(fig, 'E1-05-ac-two-cases')

w = np.logspace(3, 7, 400); w0 = 1e5
fig, ax = plt.subplots(figsize=(4.8, 2.8))
ax.semilogx(w, 1/(1+w/w0), color='#2a6fdb', lw=2, label='忽略相位：$1/(1+\\omega/\\omega_0)$')
ax.semilogx(w, 1/np.sqrt(1+(w/w0)**2), color='#d9480f', lw=1.5, ls='--', label='精確：$1/\\sqrt{1+(\\omega/\\omega_0)^2}$')
for x in [1e4, 1e5, 1e6]: ax.axvline(x, color='gray', ls=':', lw=1)
ax.text(1e4*1.1, 1.03, '$0.1\\omega_0$', fontsize=8); ax.text(1e5*1.1, 1.03, '$\\omega_0$', fontsize=8); ax.text(1e6*1.1, 1.03, '$10\\omega_0$', fontsize=8)
ax.set_xlabel('$\\omega$ (rad/s)'); ax.set_ylabel('$|v_O/v_s|$'); ax.set_ylim(0, 1.12); ax.legend(fontsize=7.5, frameon=False, loc='lower left'); ax.spines[['top','right']].set_visible(False)
sv(fig, 'E1-05-lowpass-response')

fig, ax = plt.subplots(figsize=(4.2, 2.6))
ax.loglog(w, 1/(w*1e-9), color='#2a6fdb', lw=2); ax.axvline(1e5, color='gray', ls=':'); ax.axhline(1e4, color='gray', ls=':')
ax.text(1.2e5, 2e4, '$\\omega=10^5$ → 10 kΩ', fontsize=8)
ax.set_xlabel('$\\omega$ (rad/s)'); ax.set_ylabel('$1/\\omega C$ (Ω)，$C$ = 1 nF'); ax.spines[['top','right']].set_visible(False)
ax.text(1.3e3, 2e2, '高頻 → 0（短路）\n低頻 → ∞（開路）', fontsize=8)
sv(fig, 'E1-05-reactance')

w = np.logspace(1, 8, 400); w0 = 1e6
fig, ax = plt.subplots(figsize=(5.2, 2.7))
ax.semilogx(w, 1/np.sqrt(1+(w/w0)**2), color='#2a6fdb', lw=2)
ax.axvspan(1e2, 1e5, color='#2f9e44', alpha=0.15); ax.text(1.3e2, 0.5, '聲音 $10^2$–$10^5$ rad/s', fontsize=8)
ax.axvspan(1e7, 1e8, color='#d9480f', alpha=0.12); ax.text(1.1e7, 0.5, '高頻雜訊', fontsize=8)
ax.axvline(1e5, color='gray', ls=':'); ax.axvline(1e6, color='gray', ls=':'); ax.text(1.1e6, 1.03, '$\\omega_0=10^6$', fontsize=8)
ax.set_xlabel('$\\omega$ (rad/s)'); ax.set_ylabel('$|v_O/v_s|$'); ax.set_ylim(0, 1.12); ax.spines[['top','right']].set_visible(False)
sv(fig, 'E1-05-voice-band')
