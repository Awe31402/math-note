"""Diagrams for lecture13_note.md.  Run: python3 scripts/diagrams_lecture13.py"""

from matplotlib.patches import Ellipse

from diagram_lib import BOX, BOX_EDGE, GRAY, RED, Fig, channel, protocol

channel("lecture13_key_problem", key_label="？？？", key_color=RED)

protocol("lecture13_dh", ["Alice", "Bob"], [
    ("span", "（公開：p, α）"),
    (("Alice", "選私鑰 a ∈ {2, …, p−2}（隨機）\n算公鑰 $A = \\alpha^a$ mod p"),
     ("Bob", "選私鑰 b ∈ {2, …, p−2}（隨機）\n算公鑰 $B = \\alpha^b$ mod p")),
    ("msg", "Alice", "Bob", "A"),
    ("msg", "Bob", "Alice", "B"),
    (("Alice", "$k_{AB} = B^a$ mod p"), ("Bob", "$k_{AB} = A^b$ mod p")),
], col_w=6.5)

# A group: a set G with an operation ○
f = Fig(9, 3.6)
f.ax.add_patch(Ellipse((2.8, 1.8), 4.6, 3.0, fc=BOX, ec=BOX_EDGE, lw=1.4))
f.text(1.2, 2.8, "G", weight="bold", size=14, color=BOX_EDGE)
for (x, y, s) in [(2.2, 2.2, "a"), (3.6, 2.2, "b"), (2.9, 1.1, "c")]:
    f.dot(x, y, r=0.07)
    f.text(x + 0.2, y + 0.05, s, ha="left")
f.text(5.6, 2.4, "一團（可能有限的）元素", ha="left", color=GRAY)
f.text(5.6, 1.4, "a ○ b = c", ha="left", size=13)
f.save("lecture13_group")
