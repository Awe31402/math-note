# E1-07 figures: complex-plane vector, low-pass and high-pass Bode plots
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(3.4, 3.0))
ax.annotate('', (3, 2), (0, 0), arrowprops=dict(arrowstyle='->', lw=2, color='#2a6fdb'))
ax.plot([3, 3], [0, 2], ls=':', color='gray'); ax.plot([0, 3], [2, 2], ls=':', color='gray')
ax.text(1.4, -0.35, '$a$'); ax.text(3.1, 1, '$b$'); ax.text(1.2, 1.25, '$\\sqrt{a^2+b^2}$', color='#2a6fdb', rotation=33)
ax.text(0.55, 0.12, '$\\theta$'); ax.axhline(0, color='k', lw=0.8); ax.axvline(0, color='k', lw=0.8)
ax.text(3.6, -0.3, 'Re'); ax.text(-0.45, 2.6, 'Im (j)')
ax.set_xlim(-0.6, 4); ax.set_ylim(-0.6, 2.8); ax.axis('off')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-07-phasor.svg')); plt.close(fig)

def bode(H, name, asym_mag, asym_ph):
    w = np.logspace(-2, 2, 400)
    fig, axs = plt.subplots(2, 1, figsize=(5.0, 4.2), sharex=True)
    axs[0].semilogx(w, 20*np.log10(abs(H(w))), color='#2a6fdb', lw=2, label='精確')
    axs[0].semilogx(w, asym_mag(w), color='#d9480f', lw=1.2, ls='--', label='直線近似')
    axs[0].set_ylabel('$|v_o/v_s|$ (dB)'); axs[0].set_ylim(-45, 5); axs[0].legend(fontsize=8, frameon=False)
    axs[1].semilogx(w, np.degrees(np.angle(H(w))), color='#2a6fdb', lw=2)
    axs[1].semilogx(w, asym_ph(w), color='#d9480f', lw=1.2, ls='--')
    axs[1].set_ylabel('相位 (°)'); axs[1].set_xlabel('$\\omega/\\omega_0$')
    for a in axs:
        a.axvline(1, color='gray', ls=':'); a.grid(True, which='major', alpha=0.3); a.spines[['top','right']].set_visible(False)
    return fig, axs

fig, axs = bode(lambda w: 1/(1+1j*w), 'lp', lambda w: np.where(w < 1, 0, -20*np.log10(w)),
                lambda w: np.where(w < 0.1, 0, np.where(w > 10, -90, -45-45*np.log10(w))))
axs[0].annotate('−3 dB', (1, -3), (2.5, 0), fontsize=8, arrowprops=dict(arrowstyle='->'))
axs[0].text(8, -30, '−20 dB/decade', fontsize=8); axs[1].set_yticks([0, -45, -90])
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-07-bode-lowpass.svg')); plt.close(fig)

fig, axs = bode(lambda w: 1j*w/(1+1j*w), 'hp', lambda w: np.where(w > 1, 0, 20*np.log10(w)),
                lambda w: np.where(w < 0.1, 90, np.where(w > 10, 0, 45-45*np.log10(w))))
axs[0].annotate('−3 dB', (1, -3), (0.25, 0), fontsize=8, arrowprops=dict(arrowstyle='->'))
axs[0].text(0.02, -30, '+20 dB/decade', fontsize=8); axs[1].set_yticks([0, 45, 90])
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-07-bode-highpass.svg')); plt.close(fig)
