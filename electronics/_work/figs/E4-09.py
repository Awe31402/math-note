# E4-09: PWM generation: integrator ramps between Schmitt thresholds; audio input changes the slopes
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, mpl, clean
import numpy as np; plt = mpl()
beta, RC, dt = 0.4, 1.0, 1e-3
t = np.arange(0, 12, dt); vi = 1.8*np.sin(2*np.pi*t/12)
vc = np.empty_like(t); pw = np.empty_like(t); v, s = 2.5 - 2.5*beta, 5.0
for k, x in enumerate(vi):
    v += ((2.5 - x)/RC if s > 0 else -(2.5 + x)/RC)*dt
    if s > 0 and v >= 2.5 + 2.5*beta: s = 0.0
    if s == 0 and v <= 2.5 - 2.5*beta: s = 5.0
    vc[k], pw[k] = v, s
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.2, 3.8), sharex=True)
a1.plot(t, vc, color='#d9480f', lw=1.2, label='電容電壓（積分器）')
for y in (2.5 + 2.5*beta, 2.5 - 2.5*beta): a1.axhline(y, color='#666', ls=':', lw=1)
a1.text(12.1, 2.5 + 2.5*beta, '天花板', fontsize=7, va='center'); a1.text(12.1, 2.5 - 2.5*beta, '地板', fontsize=7, va='center')
a1.plot(t, 2.5 + vi, color='#999', lw=1, label=r'$2.5+v_i$（聲音）'); a1.legend(fontsize=7, frameon=False, loc='upper right', ncol=2)
a1.set_title(r'Schmitt 觸發器 + RC 積分：$v_i$ 改變充放電斜率', fontsize=8.5); a1.set_ylim(0.5, 5.2)
a2.fill_between(t, 0, pw, step='post', color='#2a6fdb', alpha=0.35, lw=0); a2.plot(t, pw, color='#2a6fdb', lw=0.8)
a2.plot(t, 2.5 + vi, color='#d9480f', lw=1.5, label=r'平均值 $5D = 2.5+v_i$'); a2.legend(fontsize=7, frameon=False, loc='upper right')
a2.set_title(r'PWM：$D = \frac{1}{2} + \frac{v_i}{5}$，聲音大時方波寬', fontsize=8.5)
a2.set_xticks([]); clean(a1, a2); fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E4-09-pwm.svg')); plt.close(fig)
