"""Diagrams for lecture08_note.md.  Run: python3 scripts/diagrams_lecture08.py"""

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN, GREEN_EDGE, RED, Fig, chain

# Overall AES structure
f = Fig(11, 11.2)
cx = 4.6
f.text(cx, 10.8, "明文 x（128 bit）")
f.arrow((cx, 10.5), (cx, 10.02))
f.op(cx, 9.8)
f.text(cx - 1.1, 9.8, "$k_0$", ha="right")
f.arrow((cx - 1.0, 9.8), (cx - 0.22, 9.8))
f.text(cx + 0.5, 9.8, "← 金鑰加法層（金鑰白化）", ha="left", color=GRAY, size=10)


def round_box(top, title, steps, note_rows=()):
    h = 0.55 * len(steps) + 0.5
    f.frame(cx - 2.5, top - h, cx + 2.5, top, title, ec=BOX_EDGE, ls="-", fc=BOX)
    for i, s in enumerate(steps):
        col = RED if i in note_rows else "#222222"
        f.text(cx, top - 0.55 - i * 0.55, s, color=col)
    return top - h


f.arrow((cx, 9.58), (cx, 9.32))
b = round_box(9.1, "第 1 輪", ["Byte Substitution（S-box）", "ShiftRows", "MixColumn",
                              "⊕ $k_1$　金鑰加法"])
f.arrow((cx, b), (cx, b - 0.5))
f.text(cx, b - 0.8, "…（第 2 ~ $n_r - 1$ 輪相同）")
f.arrow((cx, b - 1.1), (cx, b - 1.38))
b2 = round_box(b - 1.6, "第 $n_r$ 輪（最後一輪）",
               ["Byte Substitution", "ShiftRows", "（沒有 MixColumn！）", "⊕ $k_{n_r}$"],
               note_rows=(2,))
f.arrow((cx, b2), (cx, b2 - 0.5))
f.text(cx, b2 - 0.8, "密文 y（128 bit）")
f.save("lecture08_aes_structure")

# Inside one AES round: 16 S-boxes, ShiftRows wiring, 4 MixColumns, key add
f = Fig(22, 9.0)
dx = 1.0
x0 = 0.9
xs = [x0 + i * dx for i in range(16)]
xs = [x + (i // 4) * 0.25 for i, x in enumerate(xs)]
for i, x in enumerate(xs):
    f.text(x, 8.6, f"$A_{{{i}}}$", size=10)
    f.arrow((x, 8.35), (x, 7.95))
    f.box(x, 7.65, "S", w=0.7, h=0.55, round_=False, fc=ALT, ec=ALT_EDGE)
    f.line((x, 7.37), (x, 7.05))
    f.text(x, 6.85, f"$B_{{{i}}}$", size=10)
f.text(xs[-1] + 0.8, 8.6, "← 輸入 16 byte", ha="left", size=10, color=GRAY)
f.text(xs[-1] + 0.8, 7.65, "← 16 個相同的 S-box", ha="left", size=10, color=GRAY)
# ShiftRows: column j of MixColumn takes B_{4j}, B_{4j+5}, B_{4j+10}, B_{4j+15}
order = [[(4 * j + 5 * r) % 16 for r in range(4)] for j in range(4)]
for j, col in enumerate(order):
    for r, src in enumerate(col):
        dst = xs[4 * j + r]
        f.line((xs[src], 6.6), (dst, 5.0), color=BOX_EDGE if src != dst else BOX_EDGE, lw=0.9)
f.text(xs[-1] + 0.8, 5.8, "← ShiftRows：\n　 byte 層級的置換（交叉接線）", ha="left", size=10, color=GRAY)
for j in range(4):
    a, b = xs[4 * j], xs[4 * j + 3]
    f.box((a + b) / 2, 4.5, "MixColumn", w=b - a + 0.8, h=1.0, fc=BOX, ec=BOX_EDGE)
    labs = " ".join(f"$B_{{{s}}}$" for s in order[j])
    f.text((a + b) / 2, 4.15, labs, size=8, color=GRAY)
f.text(xs[-1] + 0.8, 4.5, "← 4 個，每個 4 byte 進 4 byte 出", ha="left", size=10, color=GRAY)
for i, x in enumerate(xs):
    f.line((x, 4.0), (x, 3.65))
    f.text(x, 3.45, f"$C_{{{i}}}$", size=10)
    f.arrow((x, 3.2), (x, 2.42))
f.box((xs[0] + xs[-1]) / 2, 2.15, "⊕ $k_i$（16 byte 的子金鑰，逐 bit XOR）",
      w=xs[-1] - xs[0] + 0.9, h=0.55, fc=GREEN, ec=GREEN_EDGE)
f.arrow(((xs[0] + xs[-1]) / 2, 1.85), ((xs[0] + xs[-1]) / 2, 1.2))
f.text((xs[0] + xs[-1]) / 2, 0.9, "輸出 16 byte")
f.save("lecture08_aes_round")

chain("lecture08_sbox_two_steps",
      ["$A_i$", "[$GF(2^8)$ 求逆]", "$B'_i$", "[仿射轉換]", "$B_i$"])

# Worked example C2 -> 2F -> 25
f = Fig(14, 3.6)
y = 1.0
f.text(0.8, y, "C2", weight="bold")
f.box(4.1, y, "Table 4.2：$GF(2^8)$ 求逆", w=4.2)
f.text(7.4, y, "2F", weight="bold")
f.box(9.9, y, "仿射轉換", w=2.4)
f.text(12.6, y, "25", weight="bold")
f.arrow((1.2, y), (2.0, y))
f.arrow((6.2, y), (7.0, y))
f.arrow((7.8, y), (8.7, y))
f.arrow((11.1, y), (12.2, y))
f.arrow((0.8, y + 0.35), (0.8, 2.6), (12.6, 2.6), (12.6, y + 0.35), color=ALT_EDGE)
f.text(6.7, 2.75, "Table 4.3（S-box）一步直接給這個", va="bottom", color=ALT_EDGE)
f.save("lecture08_sbox_example")
