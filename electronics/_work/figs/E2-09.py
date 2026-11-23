# E2-09 figures: depletion charge/field/potential, JFET channel, ID-VDS + RDS-VGS, AGC circuit
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import save, drawing, OUT
import schemdraw.elements as elm
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Noto Sans CJK JP', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 1. depletion: charge, field, potential (NA > ND so x1 < x2)
x1, x2 = 0.4, 1.0
x = np.linspace(-1.0, 1.6, 800)
rho = np.where((x > -x1) & (x < 0), -1/x1, 0) + np.where((x >= 0) & (x < x2), 1/x2, 0)
E = np.cumsum(rho)*(x[1]-x[0]); V = -np.cumsum(E)*(x[1]-x[0])
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.4))
axs[0].fill_between(x, rho, color='#2a6fdb', alpha=0.5, step='mid'); axs[0].set_title('電荷：$-qN_A$（寬 $x_1$）、$+qN_D$（寬 $x_2$）', fontsize=9)
axs[0].text(-0.95, -2.2, 'P', fontsize=10); axs[0].text(1.35, 0.6, 'N', fontsize=10)
axs[1].plot(x, E, color='#d9480f', lw=2); axs[1].set_title('電場：高斯定律，三角形，在接面最大', fontsize=9)
axs[2].plot(x, V, color='#2f9e44', lw=2); axs[2].set_title('電位：再積分，總差 $V_0$', fontsize=9)
for a in axs:
    a.axhline(0, color='k', lw=0.4); a.axvline(0, color='#888', lw=0.6, ls=':'); a.set_yticks([]); a.set_xticks([-x1, 0, x2]); a.set_xticklabels(['$-x_1$', '0', '$x_2$'])
    a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-09-depletion.svg')); plt.close(fig)

# 2. JFET channel cross-sections
fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.8))
def jfet(a, wl, wr, title):
    a.add_patch(Rectangle((0, 0), 4, 3, fc='#e7f0ff', ec='k'))
    a.add_patch(Rectangle((0, 2.6), 4, 0.4, fc='#ffd8a8', ec='k')); a.add_patch(Rectangle((0, 0), 4, 0.4, fc='#ffd8a8', ec='k'))
    a.add_patch(Polygon([(0, 2.6), (4, 2.6), (4, 2.6-wr), (0, 2.6-wl)], fc='#ddd', ec='none'))
    a.add_patch(Polygon([(0, 0.4), (4, 0.4), (4, 0.4+wr), (0, 0.4+wl)], fc='#ddd', ec='none'))
    a.text(1.6, 2.7, 'P+  gate', fontsize=7); a.text(1.6, 0.08, 'P+  gate', fontsize=7)
    a.text(-0.55, 1.4, 'S', fontsize=10); a.text(4.15, 1.4, 'D', fontsize=10)
    a.text(1.7, 1.42, 'N 通道', fontsize=8, color='#2a6fdb')
    a.set_xlim(-0.8, 4.6); a.set_ylim(-0.2, 3.2); a.axis('off'); a.set_title(title, fontsize=9)
jfet(axs[0], 0.3, 0.3, '$V_{GS}=0$，$V_{DS}$ 小：通道最寬')
jfet(axs[1], 0.75, 0.75, '$V_{GS}=-2$ V：空乏區變寬，通道變窄')
jfet(axs[2], 0.3, 1.08, '$V_{GS}=0$，$V_{DS}=4$ V：汲極端夾止')
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-09-jfet-channel.svg')); plt.close(fig)

# 3. ID-VDS curves and RDS-VGS
Vp = -4; K = 1
fig, axs = plt.subplots(1, 2, figsize=(8.6, 2.8))
vds = np.linspace(0, 8, 400)
for vgs, c in [(0, '#2a6fdb'), (-1, '#4dabf7'), (-2, '#f08c00'), (-3, '#d9480f')]:
    vov = vgs - Vp
    idv = np.where(vds < vov, K*(2*vov*vds - vds**2), K*vov**2)
    axs[0].plot(vds, idv, color=c, lw=2, label=f'$V_{{GS}}$ = {vgs} V')
axs[0].axhline(0, color='k', lw=2); axs[0].text(6.0, 0.5, '−4 V：夾止，0', fontsize=8)
vv = np.linspace(0, 8, 100); axs[0].plot(vv[vv <= 4], (vv[vv <= 4])**2, color='#888', ls=':', lw=1)
axs[0].text(0.3, 13.5, '歐姆區', fontsize=9); axs[0].text(5.2, 13.5, '放大（飽和）區', fontsize=9)
axs[0].set_xlabel('$V_{DS}$'); axs[0].set_ylabel('$I_D$'); axs[0].set_yticks([]); axs[0].legend(fontsize=7, frameon=False, loc='center right')
vg = np.linspace(-3.7, 0, 200); axs[1].plot(vg, 1/(1 - vg/4), color='#2a6fdb', lw=2)
axs[1].set_xlabel('$V_{GS}$ (V)'); axs[1].set_ylabel('$R_{DS}$'); axs[1].set_yticks([]); axs[1].set_xticks([-4, -3, -2, -1, 0])
axs[1].axvline(-4, color='#d9480f', ls=':', lw=1); axs[1].text(-3.95, 8, '→ ∞', color='#d9480f'); axs[1].set_title('歐姆區：反向偏壓越大 $R_{DS}$ 越大', fontsize=9)
for a in axs: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'E2-09-jfet-curves.svg')); plt.close(fig)

# 4. AGC circuit
with drawing() as d:
    d.config(fontsize=12)
    op = elm.Opamp(leads=True)
    elm.Line().left().at(op.in2).length(0.4); elm.Line().down().length(3.2); elm.Dot(open=True).label('$Af(t)$', loc='bottom')
    elm.Line().left().at(op.in1).length(1.2); n = elm.Dot()
    j = elm.ResistorVar().down().at(n.center).label('$R_{DS}$', loc='top', ofst=(0, 0.2)); elm.Ground()
    elm.Line().up().at(n.center).length(1.5); elm.Resistor().right().tox(op.out[0]+0.6).label('$R_2$'); elm.Line().down().toy(op.out[1])
    elm.Line().left().length(0.6)
    o = elm.Dot().at((op.out[0]+0.6, op.out[1])).label('$v_O$', loc='bottom')
    elm.Line().right().at(o.center).length(0.8)
    elm.Diode().right().label('super diode', loc='top', fontsize=9); p = elm.Dot()
    elm.Capacitor().down().at(p.center).label('$C$', loc='bottom'); elm.Ground()
    elm.Line().right().at(p.center).length(1.2); elm.Resistor().down().label('$R$', loc='bottom'); elm.Ground()
    elm.Line().right().at(p.center).length(2.6)
    fo = elm.Opamp(leads=True).anchor('in2').right().label('follower', loc='bottom', fontsize=9)
    elm.Line().left().at(fo.in1).length(0.4); elm.Line().up().length(1.2); elm.Line().right().tox(fo.out[0]+0.3); elm.Line().down().toy(fo.out[1]); elm.Line().left().tox(fo.out[0])
    elm.Line().right().at(fo.out).length(0.6); elm.Resistor().right().label('$R_I$'); m = elm.Dot()
    io = elm.Opamp(leads=True).anchor('in1').right()
    elm.Line().left().at(io.in2).length(0.5); elm.BatteryCell().down().reverse().label('$V_R$', loc='bottom'); elm.Ground()
    elm.Line().up().at(m.center).length(1.4); elm.Capacitor().right().tox(io.out[0]+0.4).label('$C_I$'); elm.Line().down().toy(io.out[1]); elm.Line().left().tox(io.out[0])
    elm.Line().right().at(io.out).length(0.6).label('$V_{GS}$', loc='top'); elm.Line().down().length(4.6)
    elm.Resistor().left().length(3).label('$R_G$ 10 kΩ', loc='bottom'); elm.Line().left().tox(n.center[0]-1.6); elm.Line().up().toy(n.center[1]-2.1)
    elm.Arrow().right().length(1.2).label('gate', loc='bottom', fontsize=9)
    save(d, 'E2-09-agc')
