"""Diagrams for lecture15_note.md.  Run: python3 scripts/diagrams_lecture15.py"""

from diagram_lib import ALT_EDGE, GRAY, Fig, protocol

protocol("lecture15_dh", ["Alice", "Bob"], [
    (("Alice", "a, $A = \\alpha^a$"), ("Bob", "b, $B = \\alpha^b$")),
    ("msg", "Alice", "Bob", "A"),
    ("msg", "Bob", "Alice", "B"),
    (("Alice", "$k_{AB} = B^a$"), ("Bob", "$k_{AB} = A^b$")),
])

protocol("lecture15_elgamal", ["Alice", "Bob"], [
    ("Bob", "選 p, α；私鑰 d\n$\\beta = \\alpha^d$"),
    ("msg", "Bob", "Alice", "$k_{pub} = (p, \\alpha, \\beta)$"),
    ("Alice", "選 i\n$k_E = \\alpha^i$　（臨時金鑰 ≈ DH 的 A）\n"
              "$k_M = \\beta^i$　（遮罩金鑰 ≈ DH 的 $k_{AB}$）\n$y = x \\cdot k_M$"),
    ("msg", "Alice", "Bob", "$(k_E, y)$"),
    ("Bob", "$k_M = k_E^d$\n$x = y \\cdot k_M^{-1}$"),
], col_w=7.0)

# Symmetric vs Elgamal inputs
f = Fig(12, 3.4)
f.text(0.3, 2.8, "對稱式：", ha="left", weight="bold")
f.text(2.3, 2.8, "x,  k", ha="left")
f.arrow((6.6, 2.8), (8.2, 2.8))
f.text(8.4, 2.8, "y", ha="left")
f.text(0.3, 1.8, "Elgamal：", ha="left", weight="bold")
f.text(2.3, 1.8, "x,  $k_{pub}(\\beta)$,  隨機的 i", ha="left")
f.arrow((6.6, 1.8), (8.2, 1.8))
f.text(8.4, 1.8, "y", ha="left")
f.arrow((5.75, 0.75), (5.75, 1.5), color=ALT_EDGE)
f.text(5.75, 0.5, "隨機化參數（randomizer）", color=ALT_EDGE, va="top")
f.save("lecture15_randomizer")
