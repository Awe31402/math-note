"""Diagrams for lecture05_note.md.  Run: python3 scripts/diagrams_lecture05.py"""

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, Fig, blackbox, chain, vchain

blackbox("lecture05_des_blackbox", "64 bit 明文 x", "64 bit 密文 y", "DES",
         "56 bit\n金鑰 k")

chain("lecture05_confusion_diffusion",
      ["x", "[混淆]", "[擴散]", "[混淆]", "[擴散]", "…", "y"], gap=0.8)

vchain("lecture05_des_structure",
       ["x（64 bit）", "[初始置換 IP]", "[第 1 輪]", "[第 2 輪]", "…",
        "[第 16 輪]", "[最終置換 $IP^{-1}$]", "y（64 bit）"],
       side={2: "$k_1$", 3: "$k_2$", 5: "$k_{16}$"}, step=1.0)

# One Feistel round
f = Fig(10, 8.0)
xl, xr = 2.2, 7.0
f.text(xl, 7.6, "$L_{i-1}$（32）")
f.text(xr, 7.6, "$R_{i-1}$（32）")
f.box(xr, 5.6, "f", w=1.6, h=0.9, weight="bold")
f.arrow((xr, 7.3), (xr, 6.05))
f.dot(xr, 6.7)
f.text(xr - 1.2, 5.6, "$k_i$ (48)", ha="right")
f.arrow((xr - 1.15, 5.6), (xr - 0.85, 5.6))
f.op(xl, 4.2)
f.arrow((xl, 7.3), (xl, 4.42))
f.arrow((xr, 5.15), (xr, 4.2), (xl + 0.22, 4.2), label="32", lpos=0.3)
# right half bypasses f
f.line((xr, 6.7), (xr + 1.6, 6.7), (xr + 1.6, 3.1), (xl, 1.6))
f.arrow((xl, 1.6), (xl, 0.95))
f.line((xl, 3.98), (xl, 3.1), (xr, 1.6))
f.arrow((xr, 1.6), (xr, 0.95))
f.text(xr + 1.0, 2.2, "左右交換", color=GRAY, size=10)
f.text(xl, 0.6, "$L_i$（32）")
f.text(xr, 0.6, "$R_i$（32）")
f.save("lecture05_feistel_round")

# The f-function
f = Fig(12, 9.6)
cx = 5.2
f.text(cx, 9.2, "$R_{i-1}$（32 bit）")
f.arrow((cx, 8.9), (cx, 8.25))
f.box(cx, 7.9, "擴展 E", w=3.0, h=0.7)
f.text(cx + 1.8, 7.9, "32 → 48", ha="left", color=GRAY, size=10)
f.arrow((cx, 7.55), (cx, 6.72), label="48")
f.op(cx, 6.5)
f.arrow((cx + 2.2, 6.5), (cx + 0.22, 6.5))
f.text(cx + 2.3, 6.5, "$k_i$（48 bit）", ha="left")
f.arrow((cx, 6.28), (cx, 5.45), label="48")
for i in range(8):
    x = 1.5 + i * 1.06
    f.box(x, 5.0, f"S{i + 1}", w=0.95, h=0.85, round_=False, fc=ALT, ec=ALT_EDGE)
f.text(10.2, 5.0, "每個 6 → 4", ha="left", color=GRAY, size=10)
f.arrow((cx, 4.55), (cx, 3.6), label="8 × 4 = 32")
f.box(cx, 3.25, "置換 P", w=3.0, h=0.7)
f.text(cx + 1.8, 3.25, "32 → 32", ha="left", color=GRAY, size=10)
f.arrow((cx, 2.9), (cx, 2.1))
f.text(cx, 1.8, "輸出（32 bit）")
f.save("lecture05_f_function")

# S-box input bits: outer bits pick row, inner bits pick column
f = Fig(9, 4.2)
labels = ["$b_1$", "$b_2$", "$b_3$", "$b_4$", "$b_5$", "$b_6$"]
for i, lab in enumerate(labels):
    outer = i in (0, 5)
    f.box(1.8 + i * 1.1, 2.6, lab, w=0.95, h=0.8, round_=False,
          fc=ALT if outer else BOX, ec=ALT_EDGE if outer else BOX_EDGE)
f.text(0.9, 2.6, "6 bit 輸入：", ha="right")
f.line((2.9, 3.15), (2.9, 3.35), (6.2, 3.35), (6.2, 3.15), color=BOX_EDGE)
f.text(4.55, 3.7, "中間 4 bit → 選「行」", color=BOX_EDGE)
f.line((1.8, 2.15), (1.8, 1.4), (7.3, 1.4), (7.3, 2.15), color=ALT_EDGE)
f.text(4.55, 1.0, "外側 2 bit → 選「列」", color=ALT_EDGE)
f.save("lecture05_sbox_bits")
