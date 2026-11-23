# E2-03 figures: current components, log & exp amplifiers, rectifier + battery charging, multiplier blocks
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw, schemdraw.elements as elm
from schemdraw import flow
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

W = 0.3; xn = np.linspace(W/2, 3, 200); xp = np.linspace(-3, -W/2, 200); tot = 220
Jp_n = 100*np.exp(-(xn-W/2)/0.8); Jn_p = 120*np.exp((xp+W/2)/0.8)
fig, ax = plt.subplots(figsize=(6.0, 2.8))
ax.plot(xn, Jp_n, color='#c92a2a', lw=2, label='電洞電流 $J_p$'); ax.plot(xn, tot-Jp_n, color='#1c7ed6', lw=2, label='電子電流 $J_n$')
ax.plot(xp, Jn_p, color='#1c7ed6', lw=2); ax.plot(xp, tot-Jn_p, color='#c92a2a', lw=2)
ax.plot([-W/2, W/2], [120, 120], color='#1c7ed6', lw=2); ax.plot([-W/2, W/2], [100, 100], color='#c92a2a', lw=2)
ax.axhline(tot, color='k', lw=1.5, ls='--', label='總電流（處處 220）'); ax.axvspan(-W/2, W/2, color='#eee')
ax.set_xticks([]); ax.set_ylabel('每秒通過的載子數'); ax.set_ylim(0, 250); ax.legend(fontsize=8, frameon=False, loc='center left', bbox_to_anchor=(0.0, 0.45)); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-03-current-components.svg')); plt.close(fig)

def inv(d):
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.5); elm.Ground()
    elm.Line().right().at(op.out).length(1); o = elm.Dot().label('$v_o$', loc='right')
    elm.Line().left().at(op.in1).length(0.5); n = elm.Dot()
    return op, o, n
with drawing() as d:
    op, o, n = inv(d)
    elm.Resistor().left().at(n.center).label('$R$'); elm.Dot(open=True).label('$v_{in}$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Diode().right().tox(o.center[0]); elm.Line().down().toy(o.center[1])
    save(d, 'E2-03-log-amp')
with drawing() as d:
    op, o, n = inv(d)
    elm.Diode().left().at(n.center).reverse(); elm.Dot(open=True).label('$v_{in}$', loc='left')
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(o.center[0]).label('$R$'); elm.Line().down().toy(o.center[1])
    save(d, 'E2-03-exp-amp')

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=11)
    a = flow.Box(w=2.0, h=1.0).label('log amp'); elm.Line().left().at(a.W).length(0.8); elm.Dot(open=True).label('$v_1$', loc='left')
    b = flow.Box(w=2.0, h=1.0).at((0, -1.8)).anchor('W').label('log amp'); elm.Line().left().at(b.W).length(0.8); elm.Dot(open=True).label('$v_2$', loc='left')
    s = flow.Box(w=1.8, h=1.0).at((3.5, -0.4)).anchor('W').label('加法器')
    elm.Wire('-|').at(a.E).to(s.N) if False else elm.Line().at(a.E).to((s.W[0], s.W[1]+0.25))
    elm.Line().at(b.E).to((s.W[0], s.W[1]-0.25))
    flow.Arrow().right(1.0).at(s.E); e = flow.Box(w=2.0, h=1.0).label('exp amp')
    flow.Arrow().right(1.0).at(e.E); elm.Dot(open=True).label('$-K v_1 v_2$', loc='right')
    save(d, 'E2-03-multiplier')

fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.6))
v = np.linspace(-2, 3, 200); axs[0].plot(v, np.maximum(v-0.7, 0), color='#2a6fdb', lw=2); axs[0].set_xlabel('$v_I$ (V)'); axs[0].set_ylabel('$v_O$ (V)')
axs[0].set_title('半波整流轉移特性', fontsize=9); axs[0].text(0.75, 0.1, '0.7', fontsize=8)
t = np.linspace(0, 2, 500); vi = 3*np.sin(2*np.pi*t)
axs[1].plot(t, vi, color='#bbb', lw=1.2, label='$v_I$'); axs[1].plot(t, np.maximum(vi-0.7, 0), color='#d9480f', lw=2, label='$v_O$'); axs[1].set_title('只剩正半週（少 0.7 V）', fontsize=9); axs[1].legend(fontsize=8, frameon=False)
vs = 15*np.sin(2*np.pi*t); axs[2].plot(t, vs, color='#2a6fdb', lw=1.5); axs[2].axhline(12.7, color='#d9480f', ls='--'); axs[2].text(1.1, 13.3, '12.7 V', fontsize=8, color='#d9480f')
axs[2].fill_between(t, 12.7, vs, where=vs > 12.7, color='#2f9e44', alpha=0.4); axs[2].set_title('充電池：只有綠色那段在充', fontsize=9)
for a in axs: a.spines[['top','right']].set_visible(False); a.axhline(0, color='k', lw=0.5)
for a in axs[1:]: a.set_xticks([])
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-03-rectifier.svg')); plt.close(fig)
