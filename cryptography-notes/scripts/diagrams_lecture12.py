"""Diagrams for lecture12_note.md.  Run: python3 scripts/diagrams_lecture12.py"""

from diagram_lib import GRAY, GREEN, GREEN_EDGE, RED, Fig, channel, protocol

channel("lecture12_symmetric_channel")

protocol("lecture12_pubkey_basic", ["Alice", "Bob"], [
    ("Bob", "$k_{pub}$, $k_{pr}$\n（產生金鑰對）"),
    ("msg", "Bob", "Alice", "$k_{pub}$"),
    ("Alice", "$y = e_{k_{pub}}(x)$"),
    ("msg", "Alice", "Bob", "y"),
    ("Bob", "$x = d_{k_{pr}}(y)$"),
])

protocol("lecture12_rsa_example", ["Alice", "Bob"], [
    (("Alice", "x = 4"), ("Bob", "p = 3, q = 11, n = 33, Φ = 20\ne = 3, d = 7")),
    ("msg", "Bob", "Alice", "$k_{pub}$ = (33, 3)"),
    ("Alice", "$y = 4^3 = 64 \\equiv 31 $ (mod 33)"),
    ("msg", "Alice", "Bob", "y = 31"),
    ("Bob", "$x = 31^7 \\ \\mathrm{mod}\\  33 = 4$ ✔"),
], col_w=6.0)

# Prime generation loop
f = Fig(16, 3.4)
y = 2.4
f.box(1.1, y, "TRNG", w=1.6)
f.box(4.6, y, "產生隨機整數 $\\tilde{p}$", w=3.6)
f.box(8.6, y, "質數測試", w=2.2, fc="#fdf1e2", ec="#c77c1e")
f.text(11.4, y, "是質數", color=GREEN_EDGE)
f.box(14.0, y, "輸出 p", w=1.8, fc=GREEN, ec=GREEN_EDGE)
f.arrow((1.9, y), (2.8, y))
f.arrow((6.4, y), (7.5, y))
f.arrow((9.7, y), (10.6, y))
f.arrow((12.2, y), (13.1, y))
f.arrow((8.6, y - 0.4), (8.6, 0.8), (4.6, 0.8), (4.6, y - 0.4), color=RED)
f.text(6.6, 0.55, "不是 → 重來", color=RED, va="top")
f.save("lecture12_prime_generation")
