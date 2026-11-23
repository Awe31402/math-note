# E3-22: Bode plot of a 3-pole amplifier; oscillation point and 45-degree phase margin
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl
import numpy as np; plt = mpl()
w = np.logspace(3, 9, 800); s = 1j*w
A = 1e3/((1 + s/1e5)*(1 + s/1e6)*(1 + s/1e7))
mag, ph = 20*np.log10(abs(A)), np.unwrap(np.angle(A))*180/np.pi
w180 = w[np.argmin(abs(ph + 180))]
fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.2), sharex=True)
a1.semilogx(w, mag, color='#2a6fdb', lw=2); a1.set_ylabel('$|A|$ (dB)')
for p in (1e5, 1e6, 1e7): a1.axvline(p, color='#bbb', ls=':', lw=1)
a1.axvline(w180, color='#d9480f', ls='--', lw=1); a1.text(w180*1.1, 40, '$\\omega_{180}\\approx3\\times10^6$', color='#d9480f', fontsize=8)
a1.set_title('三個極點 $10^5, 10^6, 10^7$：在 $\\omega_{180}$ 時 $|\\beta A|$ 必須 < 1', fontsize=9)
a2.semilogx(w, ph, color='#2a6fdb', lw=2); a2.set_ylabel('相位 (°)'); a2.set_xlabel('$\\omega$ (rad/s)')
a2.axhline(-180, color='#d9480f', ls='--', lw=1); a2.axhline(-135, color='#2b8a3e', ls='--', lw=1)
a2.text(1.3e3, -128, '−135°：在 $\\omega_{p2}$ 讓 $|\\beta A|=1$ → 相位邊限 45°', color='#2b8a3e', fontsize=7.5)
a2.set_yticks([0, -90, -135, -180, -270])
for a in (a1, a2): a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-22-bode-3pole.svg')); plt.close(fig)
