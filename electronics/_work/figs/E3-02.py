# E3-02 figures: BJT input/output characteristics; hybrid-pi model
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.0))
Is = 1e-12*1e3  # mA so that 0.7 V gives ~1.4 mA
vbe = np.linspace(0, 0.8, 400); ic = 1e-15*np.exp(vbe/0.025)*1e3
axs[0].plot(vbe, ic, color='#2a6fdb', lw=2); axs[0].set_ylim(0, 3); axs[0].axvline(0.7, color='#d9480f', ls=':', lw=1)
axs[0].text(0.45, 2.3, '導通約 0.7 V\n（0.6–0.8 V 間）', fontsize=8, color='#d9480f')
axs[0].set_xlabel('$V_{BE}$ (V)'); axs[0].set_ylabel('$I_C$ (mA)'); axs[0].set_title('輸入：$I_C = I_se^{V_{BE}/V_T}$，非常陡', fontsize=9)
vce = np.linspace(0, 10, 500)
for ib, c in [(0.005, '#a5d8ff'), (0.01, '#4dabf7'), (0.015, '#2a6fdb'), (0.02, '#1864ab')]:
    icc = 100*ib*(1 - np.exp(-vce/0.06))
    axs[1].plot(vce, icc, color=c, lw=2, label=f'$I_B$ = {ib*1000:g} μA')
axs[1].axvline(0.2, color='#d9480f', ls=':', lw=1); axs[1].text(0.3, 2.2, '飽和區 $V_{CE} < 0.2$', fontsize=8, color='#d9480f')
axs[1].text(4, 2.2, '主動區：$I_C = \\beta I_B$', fontsize=8)
axs[1].set_xlabel('$V_{CE}$ (V)'); axs[1].set_ylabel('$I_C$ (mA)'); axs[1].set_ylim(0, 2.5); axs[1].legend(fontsize=7, frameon=False, loc='center right')
axs[1].set_title('輸出：用基極電流控制（$\\beta$ = 100）', fontsize=9)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E3-02-bjt-char.svg')); plt.close(fig)

with drawing() as d:
    b = elm.Dot(open=True).label('B', loc='left')
    elm.Line().right().length(1.0); n = elm.Dot()
    r = elm.Resistor().down().length(3).label('$r_\\pi$', loc='top').label('$v_{be}$', loc='bottom')
    e = elm.Dot()
    cx = n.center[0] + 3.0
    elm.Dot(open=True).at((cx, n.center[1])).label('C', loc='top')
    elm.SourceI().down().at((cx, n.center[1])).length(3).label('$g_mv_{be}$', loc='bottom')
    elm.Line().left().tox(e.center[0])
    elm.Line().down().at(e.center).length(0.6); elm.Dot(open=True).label('E', loc='bottom')
    save(d, 'E3-02-hybrid-pi')
