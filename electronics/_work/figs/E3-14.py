# E3-14: MOS diff pair large-signal transfer: iD1, iD2 vs vid
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl
import numpy as np; plt = mpl()
I, Vov = 1.0, 1.0                      # normalized: I = 1, V_OV = 1  -> full switching at sqrt(2) V_OV
x = np.linspace(-2, 2, 801); xm = np.sqrt(2)*Vov
r = np.clip(x/Vov*np.sqrt(np.clip(1 - (x/(2*Vov))**2*1, 0, None)), -1, 1)
r = np.where(np.abs(x) < xm, (x/Vov)*np.sqrt(1 - (x/Vov)**2/4), np.sign(x))
i1, i2 = I/2*(1 + r), I/2*(1 - r)
fig, ax = plt.subplots(figsize=(5.2, 3.0))
ax.plot(x, i1, color='#2a6fdb', lw=2, label='$i_{D1}$'); ax.plot(x, i2, color='#d9480f', lw=2, label='$i_{D2}$')
ax.plot(x, I/2 + I/(2*Vov)*x/1, color='#999', ls='--', lw=1, label='小信號直線 $\\frac{I}{2}+\\frac{g_m}{2}v_{id}$')
for s in (-1, 1): ax.axvline(s*xm, color='#666', ls=':', lw=1)
ax.text(xm+0.05, 0.08, '$\\sqrt{2}V_{OV}$', fontsize=8); ax.text(-xm-0.6, 0.08, '$-\\sqrt{2}V_{OV}$', fontsize=8)
ax.set_ylim(-0.05, 1.1); ax.set_xlabel('$v_{id}/V_{OV}$'); ax.set_ylabel('電流 / $I$')
ax.set_title('差動對大信號：電流在 $\\pm\\sqrt{2}V_{OV}$ 完全切到一邊', fontsize=9)
ax.legend(fontsize=7, frameon=False, loc='center right'); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-14-large-signal.svg')); plt.close(fig)
