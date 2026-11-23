"""Diagrams for lecture11_note.md.  Run: python3 scripts/diagrams_lecture11.py"""

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, RED, Fig

# Extended Euclidean algorithm: left = normal EA, right = extra bookkeeping
f = Fig(14, 5.4)
f.text(3.2, 5.0, "左邊（普通 EA）", weight="bold", color=BOX_EDGE)
f.text(10.6, 5.0, "右邊（額外工作）", weight="bold", color=ALT_EDGE)
rows = [("$r_0 = q_1 r_1 + r_2$", "$r_2 = s_2 r_0 + t_2 r_1$"),
        ("$r_1 = q_2 r_2 + r_3$", "$r_3 = s_3 r_0 + t_3 r_1$"),
        ("⋮", "⋮"),
        ("$r_{l-2} = q\\,r_{l-1} + r_l$", "$r_l = s_l r_0 + t_l r_1$"),
        ("$r_{l-1} = q\\,r_l + 0$", None)]
for i, (a, b) in enumerate(rows):
    y = 4.1 - i * 0.85
    if a == "⋮":
        f.text(3.2, y, "⋮")
        f.text(10.6, y, "⋮")
        continue
    f.box(3.2, y, a, w=4.6, h=0.62, fc=BOX, ec=BOX_EDGE)
    if b:
        f.box(10.6, y, b, w=4.6, h=0.62, fc=ALT, ec=ALT_EDGE)
        f.arrow((5.6, y), (8.2, y))
    else:
        f.text(5.8, y, "← 停", ha="left", color=RED)
f.save("lecture11_eea_columns")
