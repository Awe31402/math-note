# E2-11 figures: JFET transfer curve + gm, common-source amp, CO2 sensor chain
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

IDSS, Voff = 4, -4
fig, ax = plt.subplots(figsize=(5.0, 3.0))
v = np.linspace(-4, 0, 200); ax.plot(v, IDSS*(1-v/Voff)**2, color='#2a6fdb', lw=2)
for vg in [0, -1, -2, -3]:
    idq = IDSS*(1-vg/Voff)**2; gm = 2*IDSS/abs(Voff)*(1-vg/Voff)
    ax.plot(vg, idq, 'o', color='#d9480f'); xx = np.array([vg-0.45, vg+0.45]); ax.plot(xx, idq+gm*(xx-vg), color='#d9480f', lw=1)
    ax.text(vg+0.08, idq+0.25, f'{idq:g} mA\n$g_m$={gm:g}', fontsize=7)
ax.set_xlabel('$V_{GS}$ (V)'); ax.set_ylabel('$I_D$ (mA)'); ax.set_xticks([-4, -3, -2, -1, 0]); ax.set_ylim(0, 5)
ax.set_title('$I_D = I_{DSS}(1 - V_{GS}/V_{GS,\\mathrm{off}})^2$，切線斜率 = $g_m$', fontsize=9); ax.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-11-transfer.svg')); plt.close(fig)

with drawing() as d:
    g0 = elm.Ground()
    elm.BatteryCell().up().reverse().label('$V_{GS}$', loc='bottom')
    elm.SourceSin().up().label('$v_s$', loc='bottom')
    elm.Line().right().length(1.2)
    j = elm.JFetN().right().anchor('gate').reverse()
    elm.Line().down().at(j.source).length(0.4); elm.Ground()
    elm.Resistor().up().at(j.drain).label('$R_D$', loc='bottom'); elm.Vdd().label('$V_{DD}$ = 10 V')
    elm.Line().right().at(j.drain).length(1.2); elm.Dot(open=True).label('$v_O$', loc='right')
    save(d, 'E2-11-common-source')

fig, ax = plt.subplots(figsize=(10, 2.6)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 2.6)
blocks = [('振盪器\n$V_{DC} + A\\sin\\omega t$', 0.1), ('V→I\n轉換器', 1.35), ('雷射', 2.6), ('樣品 CO₂\n$e^{-\\alpha d}$', 3.85),
          ('光偵測器\nI→V', 5.1), ('LC 調諧\n只留 $\\omega$', 6.35), ('AM 解調\n整流+低通', 7.6), ('log 放大\n+ 減法器', 8.85)]
for txt, x in blocks:
    ax.add_patch(FancyBboxPatch((x, 0.9), 1.0, 0.9, boxstyle='round,pad=0.03', fc='#e7f0ff', ec='#2a6fdb'))
    ax.text(x+0.5, 1.35, txt, ha='center', va='center', fontsize=7.5)
for (_, x1), (_, x2) in zip(blocks[:-1], blocks[1:]): ax.annotate('', (x2, 1.35), (x1+1.0, 1.35), arrowprops=dict(arrowstyle='->', color='#555'))
ax.text(4.35, 0.45, '$\\alpha = C\\,N_{CO_2}$', ha='center', fontsize=9, color='#d9480f')
ax.text(9.35, 0.45, '$v_O \\propto V_T\\alpha d$', ha='center', fontsize=9, color='#2f9e44')
ax.text(6.85, 2.2, '雜光、直流光都進來 → 用載波頻率 $\\omega$ 認出自己的光', ha='center', fontsize=8, color='#555')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-11-co2-chain.svg')); plt.close(fig)
