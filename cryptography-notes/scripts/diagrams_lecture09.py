"""Diagrams for lecture09_note.md.  Run: python3 scripts/diagrams_lecture09.py"""

from diagram_lib import ALT, ALT_EDGE, GRAY, PARTY, Fig, chain, tree

# ECB: each block on its own
f = Fig(8, 3.6)
for i in range(3):
    y = 3.0 - i * 1.1
    f.text(0.7, y, f"$x_{i + 1}$")
    f.arrow((1.1, y), (2.2, y))
    f.box(2.9, y, "E", w=1.2, h=0.7)
    f.arrow((3.5, y), (4.6, y))
    f.text(5.0, y, f"$y_{i + 1}$")
f.text(5.6, 0.8, "← 一塊接一塊，各自加密", ha="left", color=GRAY, size=10)
f.save("lecture09_ecb_blocks")

# Modes of operation
tree("lecture09_modes_tree",
     ("操作模式", [
         ("確定性\n(deterministic)", ["ECB"]),
         ("機率性\n(probabilistic)", [
             ("當區塊密碼用", ["CBC"]),
             ("當串流密碼用", ["OFB、CFB、CTR"])])]),
     leaf_w=3.4)

# ECB between Alice and Bob
f = Fig(16, 3.4)
f.text(0.8, 2.6, "Alice", weight="bold", color=PARTY["Alice"])
f.text(0.8, 0.8, "Bob", weight="bold", color=PARTY["Bob"])
for i in range(3):
    x = 2.2 + i * 4.6
    n = i + 1
    f.text(x, 2.6, f"$x_{n}$")
    f.arrow((x + 0.35, 2.6), (x + 0.95, 2.6))
    f.box(x + 1.6, 2.6, "$e_k$", w=1.3, h=0.65)
    f.arrow((x + 2.25, 2.6), (x + 2.85, 2.6))
    f.text(x + 3.15, 2.6, f"$y_{n}$")
    f.arrow((x + 3.15, 2.35), (x + 3.15, 1.05), color=GRAY)
    f.text(x, 0.8, f"$y_{n}$")
    f.arrow((x + 0.35, 0.8), (x + 0.95, 0.8))
    f.box(x + 1.6, 0.8, "$e_k^{-1}$", w=1.3, h=0.65)
    f.arrow((x + 2.25, 0.8), (x + 2.85, 0.8))
    f.text(x + 3.15, 0.8, f"$x_{n}$")
f.text(15.6, 1.7, "…")
f.save("lecture09_ecb_alice_bob")

# Probabilistic encryption: extra random r travels with y
f = Fig(14, 4.6)
f.text(2.2, 4.2, "x")
f.arrow((2.2, 3.95), (2.2, 3.2))
f.box(2.2, 2.6, "e", w=2.2, h=1.1, weight="bold")
f.text(1.6, 0.9, "k")
f.text(2.8, 0.9, "r（隨機）")
f.arrow((1.6, 1.15), (1.6, 2.05))
f.arrow((2.8, 1.15), (2.8, 2.05))
f.box(10.6, 2.6, "d", w=2.2, h=1.1, weight="bold")
f.text(10.6, 0.9, "k")
f.arrow((10.6, 1.15), (10.6, 2.05))
f.arrow((3.3, 2.85), (9.5, 2.85), label="y　（通道）")
f.arrow((3.3, 2.35), (9.5, 2.35), label="r　（通道）", lside="below")
f.arrow((11.7, 2.6), (12.8, 2.6))
f.text(13.1, 2.6, "x")
f.save("lecture09_probabilistic_enc")

# CBC
f = Fig(17, 4.0)
xs = [0.8, 6.2, 11.6]
for i, x in enumerate(xs):
    n = i + 1
    f.text(x, 1.5, f"$x_{n}$")
    f.arrow((x + 0.35, 1.5), (x + 1.08, 1.5))
    f.op(x + 1.3, 1.5)
    f.arrow((x + 1.52, 1.5), (x + 2.2, 1.5))
    f.box(x + 2.9, 1.5, "$e_k$", w=1.3, h=0.7)
    f.arrow((x + 3.55, 1.5), (x + 4.3, 1.5))
    f.text(x + 4.6, 1.5, f"$y_{n}$")
    if i < 2:
        f.arrow((x + 4.6, 1.25), (x + 4.6, 0.6), (xs[i + 1] + 1.3, 0.6),
                (xs[i + 1] + 1.3, 1.28), color=ALT_EDGE)
f.text(xs[0] + 1.3, 3.4, "IV")
f.arrow((xs[0] + 1.3, 3.15), (xs[0] + 1.3, 1.72))
f.text(9.0, 0.3, "前一塊密文回饋進下一塊", color=ALT_EDGE, size=10)
f.save("lecture09_cbc")

chain("lecture09_stream_cipher",
      ["金鑰", "[金鑰串流產生器]", "$s_i$", "(+)", "$y_i$"],
      below={3: "$x_i$"})

# OFB
f = Fig(16, 3.8)
y = 3.0
f.text(0.6, y, "IV")
f.arrow((1.0, y), (1.8, y))
for i in range(3):
    x = 2.5 + i * 4.3
    n = i + 1
    f.box(x, y, "$e_k$", w=1.3, h=0.7)
    f.arrow((x + 0.65, y), (x + 1.6, y))
    f.text(x + 1.9, y, f"$s_{n}$")
    f.arrow((x + 2.2, y), (x + 3.15, y))
    f.arrow((x + 1.9, y - 0.25), (x + 1.9, 1.22))
    f.op(x + 1.9, 1.0)
    f.text(x + 0.7, 1.0, f"$x_{n}$")
    f.arrow((x + 1.0, 1.0), (x + 1.68, 1.0))
    f.arrow((x + 2.12, 1.0), (x + 2.9, 1.0))
    f.text(x + 3.2, 1.0, f"$y_{n}$")
f.text(15.5, y, "…")
f.save("lecture09_ofb")
