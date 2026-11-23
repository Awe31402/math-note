# E4-11: LRC low-pass: frequency response for several b, and step responses (over / critical / under damped)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl, clean
import numpy as np; plt = mpl()
w0 = 1.0; w = np.logspace(-1.5, 1.5, 600); t = np.linspace(0, 20, 1200)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 2.9))
for b, c, lab in ((4.0, '#2b8a3e', r'過阻尼 $b/2>\omega_0$'), (2.0, '#2a6fdb', r'臨界 $b/2=\omega_0$'), (0.4, '#d9480f', r'欠阻尼 $b/2<\omega_0$')):
    H = w0**2/((1j*w)**2 + b*1j*w + w0**2); a1.semilogx(w, 20*np.log10(abs(H)), color=c, lw=1.8, label=lab)
    if abs(b - 2*w0) < 1e-9: y = 1 - (1 + w0*t)*np.exp(-w0*t)
    else:
        r = np.roots([1, b, w0**2]).astype(complex); y = np.real(1 + (r[1]*np.exp(r[0]*t) - r[0]*np.exp(r[1]*t))/(r[0] - r[1]))
    a2.plot(t, y, color=c, lw=1.8)
a1.set_title(r'$\frac{\omega_0^2}{s^2+bs+\omega_0^2}$：$b$ 小 → 瘦、峰值 $\omega_0/b$', fontsize=9); a1.set_xlabel(r'$\omega/\omega_0$'); a1.set_ylabel('dB'); a1.set_ylim(-40, 15)
a1.legend(fontsize=7, frameon=False, loc='lower left'); a2.set_title('步階響應：欠阻尼會震一下再停', fontsize=9); a2.set_xticks([])
clean(a1, a2); fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E4-11-lrc-damping.svg')); plt.close(fig)
