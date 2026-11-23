"""Diagrams for lecture22_note.md.  Run: python3 scripts/diagrams_lecture22.py"""

from matplotlib.patches import Polygon

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN_EDGE, RED, Fig, chain

# Keccak / SHA-3 overview
f = Fig(18, 2.6)
f.frame(1.6, 0.3, 17.2, 2.2, "Keccak / SHA-3", ec=BOX_EDGE)
f.text(0.7, 1.15, "M")
f.arrow((1.0, 1.15), (2.2, 1.15))
f.box(4.1, 1.15, "前處理（填充）", w=3.6, h=0.7)
f.arrow((5.9, 1.15), (6.6, 1.15))
f.text(6.7, 1.15, "$x_0, x_1, …, x_{t-1}$", ha="left")
f.arrow((9.9, 1.15), (10.6, 1.15))
f.box(12.3, 1.15, "內部 Keccak", w=3.2, h=0.7, fc=ALT, ec=ALT_EDGE)
f.arrow((13.9, 1.15), (14.6, 1.15))
f.text(14.7, 1.15, "$y_0\\ (, y_1, y_2, …)$", ha="left")
f.save("lecture22_keccak_overview")

# Sponge construction: absorbing then squeezing
f = Fig(12, 10.0)
xl, xm, xr = 3.0, 6.6, 8.6
f.text(xl + 0.5, 9.7, "r bits", size=10, color=GRAY)
f.text((xm + xr) / 2 + 0.4, 9.7, "c bits", size=10, color=GRAY)
f.box((xl + xm) / 2 + 0.25, 9.0, "0", w=xm - xl + 1.5, h=0.7, round_=False, fc=BOX, ec=BOX_EDGE)
f.box(xm + 1.6, 9.0, "0", w=2.6, h=0.7, round_=False, fc=ALT, ec=ALT_EDGE)
f.text(10.4, 9.0, "初始狀態\nb = 1600 bit", ha="left", size=10, color=GRAY)
f.text(0.8, 9.0, "0")
f.arrow((1.1, 9.0), (2.2, 9.0))
xa, xc = 3.6, 8.2  # absorbing (r part) and capacity lines
y = 8.65
blocks = [("$x_0$", 7.6, 6.6), ("$x_1$", 5.4, 4.4)]
for lab, yx, yf in blocks:
    f.arrow((xa, y), (xa, yx + 0.22))
    f.line((xc, y), (xc, yf + 0.4))
    f.op(xa, yx)
    f.text(xa - 1.4, yx, lab, ha="right")
    f.arrow((xa - 1.3, yx), (xa - 0.22, yx))
    f.arrow((xa, yx - 0.22), (xa, yf + 0.4))
    f.box(5.9, yf, "f", w=6.0, h=0.8, weight="bold")
    y = yf - 0.4
f.text(xa, 3.55, "⋮")
f.text(xc, 3.55, "⋮")
f.line((xa, y), (xa, 3.85))
f.line((xc, y), (xc, 3.85))
yx = 2.9
f.op(xa, yx)
f.text(xa - 1.4, yx, "$x_{t-1}$", ha="right")
f.arrow((xa - 1.3, yx), (xa - 0.22, yx))
f.arrow((xa, 3.3), (xa, yx + 0.22))
f.line((xc, 3.3), (xc, 2.3))
f.arrow((xa, yx - 0.22), (xa, 2.3))
f.box(5.9, 1.9, "f", w=6.0, h=0.8, weight="bold")
f.text(9.2, 1.9, "← 吸收結束、擠壓開始", ha="left", size=10, color=RED)
f.arrow((xa, 1.5), (xa, 0.85))
f.text(xa, 0.6, "前 r bit → $y_0$ → 取前 n bit = SHA-3(M)", ha="left", va="center")
f.save("lecture22_sponge")

chain("lecture22_rounds",
      ["b bit", "[第 1 輪]", "[第 2 輪]", "…", "[第 $n_r$ 輪]", "b bit"],
      caption={4: "（SHA-3：$n_r$ = 24）"})

chain("lecture22_step_mappings",
      ["", "[θ]", "[ρ]", "[π]", "[χ]", "[ι]", ""], gap=0.7)

# Keccak state as a 5 x 5 x 64 block
f = Fig(9, 6.2)
s = 0.8
ox, oy = 1.6, 0.9
dx, dy = 1.4, 1.1  # depth offset
for i in range(6):
    f.line((ox + i * s, oy + 5 * s), (ox + i * s + dx, oy + 5 * s + dy), color=GRAY, lw=0.9)
for j in range(6):
    f.line((ox + 5 * s, oy + j * s), (ox + 5 * s + dx, oy + j * s + dy), color=GRAY, lw=0.9)
f.line((ox + dx, oy + 5 * s + dy), (ox + 5 * s + dx, oy + 5 * s + dy), color=GRAY, lw=0.9)
f.line((ox + 5 * s + dx, oy + dy), (ox + 5 * s + dx, oy + 5 * s + dy), color=GRAY, lw=0.9)
f.ax.add_patch(Polygon([(ox, oy + 5 * s), (ox + dx, oy + 5 * s + dy),
                        (ox + 5 * s + dx, oy + 5 * s + dy), (ox + 5 * s, oy + 5 * s)],
                       fc=ALT, ec="none", zorder=0))
f.ax.add_patch(Polygon([(ox + 5 * s, oy), (ox + 5 * s + dx, oy + dy),
                        (ox + 5 * s + dx, oy + 5 * s + dy), (ox + 5 * s, oy + 5 * s)],
                       fc="#f3e3cc", ec="none", zorder=0))
for i in range(5):
    for j in range(5):
        f.box(ox + i * s + s / 2, oy + j * s + s / 2, "", w=s, h=s, round_=False,
              fc=BOX, ec=BOX_EDGE, lw=1.0)
for i in range(5):
    f.text(ox + i * s + s / 2, oy - 0.3, f"x{i}", size=10)
    f.text(ox - 0.35, oy + i * s + s / 2, f"y {i}", size=10, ha="right")
f.arrow((ox + 5 * s + 0.2, oy - 0.1), (ox + 5 * s + dx + 0.2, oy + dy - 0.1), color=RED)
f.text(ox + 5 * s + dx + 0.3, oy + dy - 0.2, "z（深度，0…63）\n64 層", ha="left", color=RED, size=10)
f.save("lecture22_keccak_state")
