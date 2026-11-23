"""Diagrams for lecture18_note.md.  Run: python3 scripts/diagrams_lecture18.py"""

from matplotlib.patches import Ellipse

from diagram_lib import BOX, BOX_EDGE, GRAY, GREEN_EDGE, PARTY, Fig, protocol, tree

tree("lecture18_course_map",
     ("密碼學", ["對稱式", "非對稱式", "協定"]),
     leaf_w=4.4, level_h=2.0,
     notes={"對稱式": "✔（DES、3DES、AES、操作模式、\n串流密碼、暴力攻擊……）",
            "非對稱式": "✔（RSA、離散對數、ECC\n—— 上週三剛結束）",
            "協定": "← 今天開始（2011 年 5 月 11 日）"})

# Signing and verifying
f = Fig(13, 5.6)
f.ax.add_patch(Ellipse((2.0, 4.4), 3.2, 1.6, fc=BOX, ec=BOX_EDGE, lw=1.3))
f.text(2.0, 5.45, "訊息空間（所有可能的訊息）", color=GRAY, size=10)
f.dot(2.0, 4.4)
f.text(2.2, 4.4, "x", ha="left")
f.box(6.2, 4.4, "$sig_k$", w=1.8)
f.arrow((2.4, 4.4), (5.3, 4.4))
f.arrow((7.1, 4.4), (8.6, 4.4))
f.text(8.7, 4.4, "y（簽章）", ha="left")
f.text(2.0, 2.4, "Alice", weight="bold", color=PARTY["Alice"])
f.text(10.4, 2.4, "Bob", weight="bold", color=PARTY["Bob"])
f.arrow((2.7, 2.4), (9.8, 2.4), label="(x, y)")
f.box(10.4, 0.8, "$ver_k(x, y)$", w=2.4)
f.arrow((10.4, 2.1), (10.4, 1.15))
f.arrow((11.6, 0.8), (12.2, 0.8))
f.text(12.3, 0.8, "true / false", ha="left", color=GREEN_EDGE)
f.save("lecture18_sign_verify")

protocol("lecture18_signature_protocol", ["Alice", "Bob"], [
    ("Alice", "產生 $k_{pr}$, $k_{pub}$"),
    ("msg", "Alice", "Bob", "$k_{pub}$"),
    ("Alice", "$s = sig_{k_{pr}}(x)$"),
    ("msg", "Alice", "Bob", "(x, s)"),
    ("Bob", "$ver_{k_{pub}}(x, s)$ = true / false"),
])

protocol("lecture18_rsa_signature", ["Alice", "Bob"], [
    ("Alice", "$k_{pr} = d$, $k_{pub} = (n, e)$"),
    ("msg", "Alice", "Bob", "(n, e)"),
    ("Alice", "$s = sig_{k_{pr}}(x) \\equiv x^d$ mod n"),
    ("msg", "Alice", "Bob", "(x, s)"),
    ("Bob", "$x' \\equiv s^e$ mod n\n$x' \\equiv x$ → 有效\nx′ ≢ x → 無效"),
], col_w=6.0)
