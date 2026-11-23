"""Diagrams for lecture19_note.md.  Run: python3 scripts/diagrams_lecture19.py"""

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, RED, Fig, protocol

protocol("lecture19_rsa_existential_forgery", ["Alice", "Oscar", "Bob"], [
    ("Bob", "$k_{pr} = d$, $k_{pub} = (n, e)$"),
    ("msg", "Bob", "Alice", "(n, e)"),
    ("Oscar", "1. 隨便選 $s \\in Z_n$\n2. 算 $x = s^e$ mod n"),
    ("msg", "Oscar", "Alice", "(x, s)「我是 Bob」"),
    ("Alice", "$x' = s^e$ mod n\n$x' = x$ → 有效！"),
], col_w=5.2)

# Padding layout
f = Fig(13, 2.6)
f.box(4.3, 1.6, "酬載 M：900 bit", w=7.0, h=0.9, round_=False, fc=BOX, ec=BOX_EDGE)
f.box(9.95, 1.6, "填充：124 個 1", w=4.3, h=0.9, round_=False, fc=ALT, ec=ALT_EDGE)
f.text(0.6, 1.6, "x（1024 bit）=", ha="right")
f.text(4.3, 0.75, "你真正要簽的東西", color=GRAY, size=10, va="top")
f.text(9.95, 0.75, "固定的 bit 圖樣", color=GRAY, size=10, va="top")
f.save("lecture19_padding")

protocol("lecture19_elgamal_existential_forgery", ["Alice", "Oscar", "Bob"], [
    ("msg", "Bob", "Alice", "$(p, \\alpha, \\beta)$"),
    ("Oscar", "1. 選整數 i, j，gcd(j, p−1) = 1\n2. 算簽章：\n"
              "$r \\equiv \\alpha^i \\cdot \\beta^j$ mod p\n"
              "$s \\equiv -r \\cdot j^{-1}$ mod (p−1)\n"
              "3. 算訊息：\n$x \\equiv s \\cdot i$ mod (p−1)"),
    ("msg", "Oscar", "Alice", "(x, (r, s))「我是 Bob」"),
    ("Alice", "$t \\equiv \\beta^r \\cdot r^s$ mod p\n$t \\equiv \\alpha^x$ → 有效！"),
], col_w=5.6)
