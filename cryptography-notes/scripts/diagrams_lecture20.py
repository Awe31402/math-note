"""Diagrams for lecture20_note.md.  Run: python3 scripts/diagrams_lecture20.py"""

import numpy as np

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN_EDGE, RED, Fig, protocol

# Signing every block separately
f = Fig(11, 3.4)
cols = [("$x_1$", "$s_1$"), ("$x_2$", "$s_2$"), ("$x_3$", "$s_3$"), ("…", "…"), ("$x_n$", "$s_n$")]
for i, (a, b) in enumerate(cols):
    x = 1.0 + i * 2.2
    f.text(x, 3.0, a)
    f.text(x, 0.4, b)
    if a == "…":
        continue
    f.arrow((x, 2.75), (x, 2.05))
    f.box(x, 1.7, "sig", w=1.2, h=0.65, fc=ALT, ec=ALT_EDGE)
    f.arrow((x, 1.35), (x, 0.65))
f.save("lecture20_sign_each_block")

# Hash first, then sign once
f = Fig(12, 6.6)
cx = 3.4
for i, s in enumerate(["$x_1$", "$x_2$", "$x_3$", "…", "$x_n$"]):
    x = 1.4 + i * 1.0
    f.text(x, 6.2, s)
    f.line((x, 5.95), (x, 5.6), (cx, 5.4))
f.text(6.6, 6.2, "（很長的訊息，例如 256 MB 的 PDF）", ha="left", color=GRAY, size=10)
f.arrow((cx, 5.4), (cx, 4.95))
f.box(cx, 4.6, "h", w=1.4, h=0.65)
f.text(cx + 1.0, 4.6, "雜湊函數", ha="left", color=GRAY, size=10)
f.arrow((cx, 4.25), (cx, 3.6))
f.text(cx, 3.35, "z")
f.text(cx + 1.0, 3.35, "（短、固定長度）", ha="left", color=GRAY, size=10)
f.arrow((cx, 3.1), (cx, 2.45))
f.box(cx, 2.1, "sig", w=1.4, h=0.65, fc=ALT, ec=ALT_EDGE)
f.text(cx - 1.6, 2.1, "$k_{pr}$", ha="right")
f.arrow((cx - 1.5, 2.1), (cx - 0.75, 2.1))
f.text(cx + 1.0, 2.1, "（很慢，但只做一次、而且輸入很短）", ha="left", color=GRAY, size=10)
f.arrow((cx, 1.75), (cx, 1.1))
f.text(cx, 0.85, "s")
f.save("lecture20_hash_then_sign")

protocol("lecture20_hash_sign_protocol", ["Alice", "Bob"], [
    ("msg", "Bob", "Alice", "$k_{pub,B}$"),
    ("Bob", "z = h(x)\n$s = sig_{k_{pr,B}}(z)$"),
    ("msg", "Bob", "Alice", "(x, s)"),
    ("Alice", "z' = h(x)\n$ver_{k_{pub,B}}(s, z')$ = true / false"),
], col_w=6.0)

# One-way property
f = Fig(9, 2.4)
f.text(1.0, 1.7, "x", size=13)
f.text(7.0, 1.7, "z", size=13)
f.text(1.0, 0.6, "x", size=13)
f.text(7.0, 0.6, "z", size=13)
f.arrow((6.6, 1.7), (1.4, 1.7), label="✘ 不可能", color=RED)
f.arrow((1.4, 0.6), (6.6, 0.6), label="h　（容易）", color=GREEN_EDGE)
f.save("lecture20_one_way")

protocol("lecture20_second_preimage_attack", ["Alice", "Oscar", "Bob"], [
    ("Bob", "$z = h(x_1)$\ns = sig(z)"),
    ("msg", "Bob", "Oscar", "$(x_1, s)$"),
    ("Oscar", "替換"),
    ("msg", "Oscar", "Alice", "$(x_2, s)$"),
    ("Alice", "$z' = h(x_2) = h(x_1)$\nver(s, z') = true ✔ ← 被騙了！"),
], widths=[6.0, 4.0, 4.6])

# Second preimage vs collision
f = Fig(13, 2.6)
f.text(0.3, 1.9, "第二原像：", ha="left", weight="bold")
f.text(0.3, 0.7, "碰撞：", ha="left", weight="bold")
f.text(3.2, 1.9, "$x_1$（固定、已給）", ha="left")
f.text(3.2, 0.7, "$x_1$ = ?", ha="left", color=RED)
f.text(7.0, 1.9, "$x_2$ = ?", ha="left", color=RED)
f.text(7.0, 0.7, "$x_2$ = ?", ha="left", color=RED)
f.text(9.0, 1.9, "→  $h(x_1) = h(x_2)$", ha="left")
f.text(9.0, 0.7, "→  $h(x_1) = h(x_2)$", ha="left")
f.save("lecture20_second_preimage_vs_collision")

protocol("lecture20_collision_attack", ["Alice", "Oscar", "Bob"], [
    ("msg", "Oscar", "Bob", "$x_1$"),
    ("Bob", "$z = h(x_1)$\ns = sig(z)"),
    ("msg", "Bob", "Oscar", "$(x_1, s)$"),
    ("Oscar", "替換"),
    ("msg", "Oscar", "Alice", "$(x_2, s)$"),
    ("Alice", "$h(x_2) = h(x_1)$ → 驗證通過 ✔"),
], widths=[6.0, 4.0, 4.6])

# Infinite input space onto finite output space
f = Fig(13, 4.4)
f.frame(0.3, 0.4, 5.5, 3.5, "輸入空間 X（無限大）", ec=BOX_EDGE, ls="-", fc=BOX)
f.frame(8.8, 1.2, 11.6, 3.0, "輸出空間 Z（$2^n$ 個值）", ec=ALT_EDGE, ls="-", fc=ALT)
for i in range(8):
    for j in range(4):
        f.dot(0.9 + i * 0.6, 0.85 + j * 0.65, r=0.06, color=BOX_EDGE)
for i in range(3):
    for j in range(2):
        f.dot(9.5 + i * 0.7, 1.7 + j * 0.7, r=0.06, color=ALT_EDGE)
f.arrow((5.8, 2.0), (8.5, 2.0), label="h")
f.save("lecture20_input_output_space")
