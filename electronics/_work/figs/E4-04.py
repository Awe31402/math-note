# E4-04: dominant-pole compensation: move first pole 1e5 -> 1e2 so |A| = 1 at the second pole
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl, clean
import numpy as np; plt = mpl()
w = np.logspace(0, 8, 800); s = 1j*w
A1 = 1e4/((1 + s/1e5)*(1 + s/1e6)*(1 + s/1e7)); A2 = 1e4/((1 + s/1e2)*(1 + s/1e6)*(1 + s/1e7))
fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.2), sharex=True)
for A, c, lab in ((A1, '#d9480f', r'補償前 $\omega_{p1}=10^5$'), (A2, '#2a6fdb', r"補償後 $\omega_{p1}'=10^2$")):
    a1.semilogx(w, 20*np.log10(abs(A)), color=c, lw=2, label=lab)
    a2.semilogx(w, np.unwrap(np.angle(A))*180/np.pi, color=c, lw=2)
a1.axhline(0, color='#666', lw=0.8); a1.axvline(1e6, color='#2b8a3e', ls=':', lw=1)
a1.text(1.3e6, -75, r'$\omega_{p2}$：$|A|=1$', color='#2b8a3e', fontsize=8)
a1.set_ylabel(r'$|A|$ (dB)'); a1.legend(fontsize=7.5, frameon=False); a1.set_title(r'主極點補償（$\beta=1$，相位邊限 45°）', fontsize=9)
a2.axhline(-180, color='#d9480f', ls='--', lw=1); a2.axhline(-135, color='#2b8a3e', ls='--', lw=1); a2.axvline(1e6, color='#2b8a3e', ls=':', lw=1)
a2.set_yticks([0, -90, -135, -180, -270]); a2.set_ylabel('相位 (°)'); a2.set_xlabel(r'$\omega$ (rad/s)'); clean(a1, a2)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E4-04-dominant-pole.svg')); plt.close(fig)
