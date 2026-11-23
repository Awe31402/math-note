"""Diagrams for lecture16_note.md.  Run: python3 scripts/diagrams_lecture16.py"""

import matplotlib.pyplot as plt
import numpy as np

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, OUT, RED, Fig

# Services x mathematical structures
f = Fig(14, 4.2)
cols = ["金鑰交換", "加密", "數位簽章"]
xs = [5.2, 7.9, 10.6]
f.text(7.9, 3.75, "服務（security services）", color=GRAY)
for x, c in zip(xs, cols):
    f.text(x, 3.15, c, weight="bold")
rows = [("DL in $Z_p^*$", ["DH", "Elgamal", "Elgamal 簽章 / DSA"], "← 到目前為止做的", BOX, BOX_EDGE),
        ("DL on EC", ["ECDH", "EC-Elgamal", "ECDSA"], "← 今天開始", ALT, ALT_EDGE)]
for i, (name, cells, note, fc, ec) in enumerate(rows):
    y = 2.3 - i * 1.0
    f.text(2.0, y, name, weight="bold")
    for x, c in zip(xs, cells):
        f.box(x, y, c, w=2.5, h=0.7, fc=fc, ec=ec, size=10)
    f.text(12.1, y, note, ha="left", size=10, color=ec)
f.text(2.0, 0.35, "↑ 數學結構", color=GRAY)
f.save("lecture16_services_table")

# Point addition on a real elliptic curve: y^2 = x^3 - 3x + 5
a, b = -3, 5
fig, ax = plt.subplots(figsize=(6.4, 6.0))
ys = np.linspace(-5.5, 5.5, 2000)
# plot by solving for x numerically along y is awkward; use implicit contour
X, Y = np.meshgrid(np.linspace(-3, 4.2, 800), np.linspace(-6, 6, 800))
ax.contour(X, Y, Y**2 - X**3 - a * X - b, levels=[0], colors=[BOX_EDGE], linewidths=2)
P = (-2.0, np.sqrt(-8 + 6 + 5))
Q = (0.5, np.sqrt(0.125 - 1.5 + 5))
s = (Q[1] - P[1]) / (Q[0] - P[0])
x3 = s**2 - P[0] - Q[0]
y3 = s * (P[0] - x3) - P[1]
Rp = (x3, -y3)
xx = np.linspace(-2.8, x3 + 0.6, 10)
ax.plot(xx, P[1] + s * (xx - P[0]), color="#555555", lw=1.3)
ax.plot([x3, x3], [-y3, y3], color=RED, lw=1.2, ls="--")
for pt, lab, c, off in [(P, "P", "#222222", (-0.35, 0.3)), (Q, "Q", "#222222", (-0.1, 0.4)),
                        (Rp, "R′（第三個交點）", "#555555", (0.15, 0.25)),
                        ((x3, y3), "R = P + Q\n（R′ 對 x 軸鏡射）", RED, (0.15, -0.6))]:
    ax.plot(*pt, "o", color=c, ms=8, zorder=5)
    ax.text(pt[0] + off[0], pt[1] + off[1], lab, color=c, fontsize=11)
ax.text(-2.7, P[1] + s * (-0.7) + 0.55, "割線", color="#555555", fontsize=10)
ax.axhline(0, color="#999999", lw=0.8)
ax.axvline(0, color="#999999", lw=0.8)
ax.set_xlim(-3, 4.2)
ax.set_ylim(-6, 6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y² = x³ − 3x + 5 上的點加法 P + Q", fontsize=11)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "lecture16_point_addition.png", facecolor="white")
plt.close(fig)
print("wrote images/lecture16_point_addition.png")
