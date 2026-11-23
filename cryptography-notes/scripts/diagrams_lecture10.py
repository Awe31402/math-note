"""Diagrams for lecture10_note.md.  Run: python3 scripts/diagrams_lecture10.py"""

import numpy as np

from diagram_lib import ALT_EDGE, GRAY, RED, Fig, chain

chain("lecture10_double_enc",
      ["$x_1$", "[e]", "z", "[e]", "$y_1$"],
      above={1: "$k_L$", 3: "$k_R$"},
      caption={1: "左邊加密", 2: "中間值", 3: "右邊加密"})

chain("lecture10_triple_enc",
      ["x", "[e]", "a", "[e]", "b", "[e]", "y"],
      above={1: "$k_1$", 3: "$k_2$", 5: "$k_3$"})

# Many keys map x1 into ciphertext space; several land on y1
f = Fig(14, 6.2)
f.frame(0.3, 0.5, 4.3, 5.4, "明文空間 P（$2^{64}$ 個點）", ec=GRAY, ls="-")
f.frame(8.3, 0.5, 13.5, 5.4, "密文空間 C（$2^{64}$ 個點）", ec=GRAY, ls="-")
rng = np.random.default_rng(3)
for _ in range(40):
    f.dot(8.7 + rng.random() * 4.4, 0.8 + rng.random() * 4.3, r=0.04, color="#bbbbbb")
x1 = (2.2, 3.0)
f.dot(*x1, r=0.09)
f.text(1.7, 3.0, "$x_1$", ha="right")
y1 = (11.6, 2.4)
f.dot(*y1, r=0.12, color=RED)
f.text(11.85, 2.4, "$y_1$", ha="left", color=RED, weight="bold")
targets = [((9.6, 4.6), "$k_0$", False), ((10.4, 3.7), "$k_1$", False),
           (y1, "$k_T$", True), (y1, "$k^{(1)}$", True), (y1, "$k^{(2)}$", True)]
for i, (t, lab, hit) in enumerate(targets):
    c = RED if hit else "#555555"
    ty = t[1] + (i - 3) * 0.12 if hit else t[1]
    f.arrow((x1[0] + 0.15, x1[1]), (t[0] - 0.15, ty), color=c, lw=1.0)
    if not hit:
        f.dot(*t, r=0.08)
    mx = 5.6
    my = x1[1] + (ty - x1[1]) * (mx - x1[0]) / (t[0] - x1[0])
    f.text(mx, my + 0.05, lab, va="bottom", size=10, color=c,
           bbox=dict(fc="white", ec="none", pad=0.5))
f.text(10.9, 0.1, "$k_T$ 打到 $y_1$，\n但 $k^{(1)}, k^{(2)}, …$ 也打到", color=RED, size=10, va="top")
f.save("lecture10_key_space")

chain("lecture10_key_whitening",
      ["x", "(+)", "[$e_k$]", "(+)", "y"],
      below={1: "$k_1$", 3: "$k_2$"})
