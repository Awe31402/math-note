# E1-14 figures: pn junction & barrier, diode IV, photodetector model, open-circuit (voltage-reading) case
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, axs = plt.subplots(2, 1, figsize=(5.6, 4.2), gridspec_kw={'height_ratios': [1.1, 1]})
ax = axs[0]; ax.add_patch(plt.Rectangle((0, 0), 4, 2, fc='#fde2e2', ec='k')); ax.add_patch(plt.Rectangle((4, 0), 4, 2, fc='#e2ebfd', ec='k'))
ax.add_patch(plt.Rectangle((3, 0), 2, 2, fc='#f1f1f1', ec='k', ls='--'))
rng = np.random.default_rng(1)
for x, y in rng.uniform([0.2, 0.2], [2.8, 1.8], (14, 2)): ax.plot(x, y, 'o', mfc='none', mec='#c92a2a', ms=7)
for x, y in rng.uniform([5.2, 0.2], [7.8, 1.8], (14, 2)): ax.plot(x, y, '.', color='#1c7ed6', ms=9)
for y in [0.4, 1.0, 1.6]: ax.text(3.35, y-0.1, '⊖', fontsize=11); ax.text(4.35, y-0.1, '⊕', fontsize=11)
ax.annotate('', (3.3, 2.25), (4.7, 2.25), arrowprops=dict(arrowstyle='->')); ax.text(3.85, 2.35, '$E$')
ax.text(0.0, -0.45, 'p（硼，free hole ○）', fontsize=9); ax.text(5.3, -0.45, 'n（磷，free electron ●）', fontsize=9); ax.text(3.15, -0.45, '空乏區', fontsize=9)
ax.set_xlim(-0.2, 8.2); ax.set_ylim(-0.7, 2.7); ax.axis('off')
x = np.linspace(0, 8, 400); Ec = 1.0 + 1.0/(1+np.exp((x-4)/0.35))
axs[1].plot(x, Ec, color='#2a6fdb', lw=2, label='導帶 $E_c$'); axs[1].plot(x, Ec-1.12, color='#d9480f', lw=2, label='價帶 $E_v$')
axs[1].annotate('', (1, 2.0), (1, 0.88), arrowprops=dict(arrowstyle='<->')); axs[1].text(1.1, 1.4, '$E_g$', fontsize=9)
axs[1].annotate('', (6.5, 2.0), (6.5, 1.0), arrowprops=dict(arrowstyle='<->')); axs[1].text(6.6, 1.45, '$qV_0$（電子要爬的山）', fontsize=8)
axs[1].set_xlim(-0.2, 8.2); axs[1].set_yticks([]); axs[1].set_xticks([]); axs[1].legend(fontsize=8, frameon=False, loc='lower left')
for s in ['top','right']: axs[1].spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-14-pn-junction.svg')); plt.close(fig)

v = np.linspace(-0.3, 0.8, 400); i = 1e-14*(np.exp(v/0.025)-1)*1e3
fig, ax = plt.subplots(figsize=(4.2, 2.8))
ax.plot(v, np.clip(i, -1, 20), color='#2a6fdb', lw=2); ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_xlabel('$v$ (V)'); ax.set_ylabel('$i$ (mA)'); ax.set_ylim(-1, 12); ax.text(0.42, 8, '約 0.7 V\n導通（mA 級）', fontsize=8); ax.text(-0.28, 1, '反向：幾乎沒電流', fontsize=8)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E1-14-diode-iv.svg')); plt.close(fig)

with drawing() as d:
    s = elm.SourceI().up().label('$i_{ph}$', loc='top')
    elm.Ground().at(s.start)
    elm.Line().right().at(s.end).length(2.5); n = elm.Dot()
    dd = elm.Diode().down().at(n.center).label('$R_s$', loc='bottom'); elm.Ground()
    elm.Line().right().at(n.center).length(2.5); o = elm.Dot().label('$v$', loc='top')
    elm.Resistor().down().at(o.center).label('$R_i$', loc='bottom'); elm.Ground()
    save(d, 'E1-14-photodetector-model')
