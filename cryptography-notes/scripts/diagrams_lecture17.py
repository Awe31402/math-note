"""Diagrams for lecture17_note.md.  Run: python3 scripts/diagrams_lecture17.py"""

import matplotlib.pyplot as plt

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN, GREEN_EDGE, OUT, RED, Fig, protocol

# Hopping around the points of E: y^2 = x^3 + 2x + 2 mod 17, P = (5, 1)
MOD, A = 17, 2


def add(p, q):
    if p is None:
        return q
    if q is None:
        return p
    (x1, y1), (x2, y2) = p, q
    if x1 == x2 and (y1 + y2) % MOD == 0:
        return None
    if p == q:
        s = (3 * x1 * x1 + A) * pow(2 * y1, -1, MOD) % MOD
    else:
        s = (y2 - y1) * pow(x2 - x1, -1, MOD) % MOD
    x3 = (s * s - x1 - x2) % MOD
    return (x3, (s * (x1 - x3) - y1) % MOD)


pts = []
T = None
for k in range(1, 19):
    T = add(T, (5, 1))
    pts.append(T)
fig, ax = plt.subplots(figsize=(6.4, 5.6))
allx = [p[0] for p in pts]
ally = [p[1] for p in pts]
ax.scatter(allx, ally, s=25, color="#bbbbbb", zorder=2)
d = 6  # show the first hops and stop at T = dP
for k in range(d):
    p = pts[k]
    if k + 1 < d:
        q = pts[k + 1]
        ax.annotate("", xy=q, xytext=p,
                    arrowprops=dict(arrowstyle="-|>", color=BOX_EDGE, lw=1.1,
                                    shrinkA=5, shrinkB=5))
    if k + 1 < d:
        ax.scatter(*p, s=45, color=BOX_EDGE, zorder=3)
        ax.text(p[0] + 0.3, p[1] + 0.3, f"{k + 1}P", fontsize=10, color=BOX_EDGE)
ax.scatter(*pts[d - 1], s=90, color=RED, zorder=4)
ax.text(pts[d - 1][0], pts[d - 1][1] - 0.8, f"T = dP（d = {d}）\n跳了 d 次之後停在這裡",
        color=RED, fontsize=10, ha="right", va="top")
ax.set_xlim(-0.5, 17)
ax.set_ylim(-0.5, 17.5)
ax.set_xticks(range(0, 17, 2))
ax.set_yticks(range(0, 17, 2))
ax.grid(alpha=0.25)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y² = x³ + 2x + 2 mod 17：從 P = (5, 1) 一步步加 P", fontsize=11)
fig.tight_layout()
fig.savefig(OUT / "lecture17_point_hopping.png", facecolor="white")
plt.close(fig)
print("wrote images/lecture17_point_hopping.png")

protocol("lecture17_ecdh", ["Alice", "Bob"], [
    ("span", "（先約定曲線，例如用標準曲線）"),
    (("Alice", "選 a ∈ {2, …, #E − 1}\n$A = a \\cdot P = (x_A, y_A)$"),
     ("Bob", "選 b ∈ {2, …, #E − 1}\n$B = b \\cdot P = (x_B, y_B)$")),
    ("msg", "Alice", "Bob", "A"),
    ("msg", "Bob", "Alice", "B"),
    (("Alice", "$T_{AB} = a \\cdot B$"), ("Bob", "$T_{AB} = b \\cdot A$")),
], col_w=6.0)

# Layers of an ECC implementation
f = Fig(8, 4.4)
layers = [("4. 協定（ECDH、ECDSA）", GREEN, GREEN_EDGE),
          ("3. 純量乘法（Double-and-Add）", ALT, ALT_EDGE),
          ("2. 群運算（點加法、點倍增）", BOX, BOX_EDGE),
          ("1. 模運算（GF(p) 的 + − × ⁻¹）", "#f0f0f0", "#666666")]
for i, (s, fc, ec) in enumerate(layers):
    f.box(4.0, 3.8 - i * 1.0, s, w=7.0, h=0.85, fc=fc, ec=ec, round_=False)
f.save("lecture17_layers")
