"""Diagrams for lecture04_note.md.  Run: python3 scripts/diagrams_lecture04.py"""

from diagram_lib import ALT, ALT_EDGE, Fig, chain

# Key stream generator = unknown box
chain("lecture04_keystream_generator",
      ["金鑰 k", "[？？？]", "$s_i$", "(+)", "$y_i$"],
      caption={1: "金鑰串流產生器"}, above={3: "$x_i$"})


def ffs(f, names, y, x0=1.2, step=2.4, w=1.6):
    xs = []
    for i, n in enumerate(names):
        x = x0 + i * step
        f.box(x, y, n, w=w, h=0.8, round_=False, fc=ALT, ec=ALT_EDGE)
        xs.append(x)
    for a, b in zip(xs, xs[1:]):
        f.arrow((a + w / 2, y), (b - w / 2, y))
    return xs


# Plain shift register
f = Fig(10, 1.6)
xs = ffs(f, ["FF2", "FF1", "FF0"], 0.8, x0=1.6)
f.arrow((0.2, 0.8), (xs[0] - 0.8, 0.8))
f.arrow((xs[-1] + 0.8, 0.8), (7.9, 0.8))
f.text(8.0, 0.8, "輸出 $s_i$", ha="left")
f.save("lecture04_shift_register")

# Degree-3 LFSR, feedback = FF1 xor FF0
f = Fig(10, 3.2)
y = 0.8
xs = ffs(f, ["FF2", "FF1", "FF0"], y, x0=1.6)
f.op(4.0 + 1.2, 2.6)
xo = 5.2
f.dot(xo, y)
f.line((xo, y), (xo, 2.38))  # tap between FF1 and FF0
f.dot(7.6, y)
f.arrow((xs[-1] + 0.8, y), (8.6, y))
f.text(8.7, y, "輸出 $s_i$", ha="left")
f.arrow((7.6, y), (7.6, 2.6), (5.42, 2.6))
f.arrow((4.98, 2.6), (0.6, 2.6), (0.6, y), (xs[0] - 0.8, y))
f.save("lecture04_lfsr_deg3")

# General LFSR of degree m with feedback coefficients p_i
f = Fig(14, 5.0)
y = 0.8
names = ["$FF_{m-1}$", "$FF_{m-2}$", "…", "$FF_1$", "$FF_0$"]
xs = [1.8, 4.4, 7.0, 9.4, 11.8]
for x, n in zip(xs, names):
    if n == "…":
        f.text(x, y, "…")
    else:
        f.box(x, y, n, w=1.8, h=0.8, round_=False, fc=ALT, ec=ALT_EDGE)
for a, b in zip(xs, xs[1:]):
    f.arrow((a + 0.9 if a != 7.0 else a + 0.3, y), (b - 0.9 if b != 7.0 else b - 0.3, y))
f.arrow((xs[-1] + 0.9, y), (13.2, y))
f.text(13.3, y, "輸出", ha="left")
# taps: outputs of each FF go up to a multiplier p_j, then into the XOR chain
yt, yx = 2.6, 4.2
taps = [(3.1, "$p_{m-1}$"), (5.7, "$p_{m-2}$"), (10.6, "$p_1$"), (12.8, "$p_0$")]
for i, (x, lab) in enumerate(taps):
    f.dot(x, y)
    f.arrow((x, y), (x, yt - 0.22))
    f.op(x, yt, "x")
    f.text(x + 0.3, yt, lab, ha="left", size=10)
    if i < len(taps) - 1:
        f.arrow((x, yt + 0.22), (x, yx - 0.22))
        f.op(x, yx)
    else:
        f.line((x, yt + 0.22), (x, yx))
f.arrow((12.8, yx), (10.82, yx))
f.arrow((10.38, yx), (8.6, yx))
f.text(8.1, yx, "…")
f.arrow((7.6, yx), (5.92, yx))
f.arrow((5.48, yx), (3.32, yx))
f.arrow((2.88, yx), (0.5, yx), (0.5, y), (0.9, y))
f.save("lecture04_lfsr_general")
