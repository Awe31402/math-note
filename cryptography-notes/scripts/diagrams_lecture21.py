"""Diagrams for lecture21_note.md.  Run: python3 scripts/diagrams_lecture21.py"""

from diagram_lib import ALT, ALT_EDGE, BOX, BOX_EDGE, GRAY, GREEN, GREEN_EDGE, RED, Fig, chain, tree

# Collision
f = Fig(12, 2.8)
for y, n in [(2.2, 1), (0.6, 2)]:
    f.text(0.6, y, f"$x_{n}$")
    f.arrow((1.0, y), (2.2, y))
    f.box(2.9, y, "h", w=1.2, h=0.65)
    f.arrow((3.5, y), (4.7, y))
    f.text(5.3, y, f"$h(x_{n})$")
f.line((6.0, 2.2), (6.4, 2.2), (6.4, 0.6), (6.0, 0.6))
f.arrow((6.4, 1.4), (7.0, 1.4))
f.text(7.1, 1.4, "兩個（例如 160 bit）輸出一樣 → 碰撞", ha="left", color=RED)
f.save("lecture21_collision")

tree("lecture21_hash_families",
     ("雜湊函數", [
         "以區塊密碼為基礎\n(block cipher-based)",
         ("專用雜湊函數\n(dedicated)", ["MD4 家族：MD5、SHA-1、SHA-2\nSHA-3（新的）\n其他……"])]),
     leaf_w=5.0, level_h=2.2)

chain("lecture21_sha1_blackbox", ["任意長度的 x", "[SHA-1]", "160 bit"])

# Merkle-Damgard construction
f = Fig(17, 4.0)
f.text(0.7, 3.5, "x")
f.arrow((1.0, 3.5), (1.8, 3.5))
f.box(2.6, 3.5, "填充", w=1.4, h=0.6)
f.arrow((3.3, 3.5), (4.1, 3.5))
f.text(4.2, 3.5, "$x_1, x_2, …, x_n$", ha="left")
y = 0.9
f.text(0.7, y, "$H_0$")
xs = [2.6, 6.0, 9.4, 13.4]
labs = ["$x_1$", "$x_2$", "$x_3$", "$x_n$"]
outs = ["$H_1$", "$H_2$", "…", "$H_n = h(x)$"]
prev = 1.1
for x, l, o in zip(xs, labs, outs):
    f.box(x, y, "壓縮", w=1.5, h=0.75, fc=ALT, ec=ALT_EDGE)
    f.text(x, 2.4, l)
    f.arrow((x, 2.15), (x, y + 0.4))
    f.arrow((prev, y), (x - 0.78, y))
    f.text(x + 1.6, y, o, ha="center" if o != "$H_n = h(x)$" else "left")
    prev = x + 2.0
f.line((xs[1] + 1.6 + 0.4, y), (xs[1] + 1.6 + 0.4, y))
f.save("lecture21_merkle_damgard")

# Block cipher rounds with key schedule (abstract)
f = Fig(14, 3.6)
f.text(0.6, 3.0, "key")
f.arrow((1.0, 3.0), (1.8, 3.0))
f.box(2.9, 3.0, "金鑰排程", w=2.0, h=0.6)
f.arrow((3.9, 3.0), (4.6, 3.0))
xs = [5.4, 7.6, 11.2]
for x, k in zip(xs, ["$k_0$", "$k_1$", "$k_{s-1}$"]):
    f.text(x, 3.0, k)
    f.arrow((x, 2.75), (x, 1.35))
f.text(9.4, 3.0, "…")
f.text(0.6, 1.0, "m")
f.arrow((1.0, 1.0), (4.6, 1.0))
for x, r in zip(xs, ["第0輪", "第1輪", "第s-1輪"]):
    f.box(x, 1.0, r, w=1.6, h=0.7)
f.arrow((6.2, 1.0), (6.8, 1.0))
f.arrow((8.4, 1.0), (9.0, 1.0))
f.text(9.4, 1.0, "…")
f.arrow((9.8, 1.0), (10.4, 1.0))
f.arrow((12.0, 1.0), (12.7, 1.0))
f.text(12.8, 1.0, "輸出", ha="left")
f.text(7.0, 0.2, "區塊密碼（例如 AES、DES，抽象層次）", color=GRAY, size=10)
f.save("lecture21_block_cipher_rounds")

# SHA-1 compression function
f = Fig(16, 4.4)
f.text(1.0, 3.6, "$x_i$ (512 bit)")
f.arrow((2.2, 3.6), (3.0, 3.6))
f.box(4.1, 3.6, "訊息排程", w=2.0, h=0.6)
f.arrow((5.1, 3.6), (5.8, 3.6))
xs = [6.6, 8.8, 12.4]
for x, k in zip(xs, ["$W_0$", "$W_1$", "$W_{79}$"]):
    f.text(x, 3.6, k)
    f.arrow((x, 3.35), (x, 2.05))
f.text(10.6, 3.6, "…")
f.text(13.4, 3.6, "（各 32 bit）", ha="left", color=GRAY, size=10)
y = 1.7
f.text(1.0, y, "$H_{i-1}$ (160)")
f.arrow((2.2, y), (5.8, y))
for x, r in zip(xs, ["第0輪", "第1輪", "第79輪"]):
    f.box(x, y, r, w=1.6, h=0.7)
f.arrow((7.4, y), (8.0, y))
f.arrow((9.6, y), (10.2, y))
f.text(10.6, y, "…")
f.arrow((11.0, y), (11.6, y))
f.arrow((13.2, y), (13.88, y))
f.op(14.1, y, "box+")
f.arrow((14.32, y), (15.0, y))
f.text(15.1, y, "$H_i$", ha="left")
f.dot(3.2, y)
f.arrow((3.2, y), (3.2, 0.5), (14.1, 0.5), (14.1, y - 0.22), color=ALT_EDGE,
        label="前饋（feed-forward）", lside="below")
f.save("lecture21_sha1_compression")

# SHA-1: 4 stages of 20 rounds
f = Fig(14, 6.4)
f.text(7.0, 6.0, "$H_{i-1}$（160 bit）")
f.arrow((7.0, 5.7), (7.0, 5.25))
f.text(7.0, 5.0, "A　B　C　D　E")
f.text(1.2, 5.0, "$x_i$")
f.arrow((1.6, 5.0), (2.2, 5.0))
f.box(3.2, 5.0, "訊息排程", w=1.8, h=0.6)
stages = [("$W_0…W_{19}$", "第 1 階段（20 輪）：$f_1, K_1$"),
          ("$W_{20}…W_{39}$", "第 2 階段（20 輪）：$f_2, K_2$"),
          ("$W_{40}…W_{59}$", "第 3 階段（20 輪）：$f_3, K_3$"),
          ("$W_{60}…W_{79}$", "第 4 階段（20 輪）：$f_4, K_4$")]
for i, (w, s) in enumerate(stages):
    y = 4.0 - i * 0.85
    f.text(3.2, y, w, size=10)
    f.arrow((4.2, y), (4.9, y))
    f.box(7.6, y, s, w=5.2, h=0.65, fc=ALT, ec=ALT_EDGE)
f.line((3.2, 4.7), (3.2, 4.25))
f.arrow((7.0, 4.75), (7.0, 4.33))
f.arrow((7.6, 1.12), (7.6, 0.85))
f.text(7.6, 0.6, "逐字加法 mod $2^{32}$（加上 $H_{i-1}$）")
f.arrow((10.8, 0.6), (11.6, 0.6))
f.text(11.7, 0.6, "$H_i$（160 bit）", ha="left")
f.save("lecture21_sha1_stages")

# SHA-1 round function
f = Fig(13, 6.2)
xs = {"A": 1.2, "B": 3.4, "C": 5.6, "D": 7.8, "E": 10.0}
for k, x in xs.items():
    f.text(x, 5.8, k, weight="bold")
ys_ops = [4.6, 3.7, 2.8, 1.9]
xE = xs["E"]
for y in ys_ops:
    f.op(xE, y, "box+")
f.box(6.0, 4.6, "$f_t(B, C, D)$", w=2.4, h=0.6)
f.line((xs["B"], 5.55), (xs["B"], 0.9))
f.line((xs["C"], 5.55), (xs["C"], 4.9))
f.line((xs["D"], 5.55), (xs["D"], 4.9))
f.dot(xs["B"], 4.6)
f.arrow((xs["B"], 4.6), (4.8, 4.6))
f.arrow((7.2, 4.6), (xE - 0.22, 4.6))
f.arrow((xE, 5.55), (xE, 4.82))
f.dot(xs["A"], 3.7)
f.line((xs["A"], 5.55), (xs["A"], 0.9))
f.arrow((xs["A"], 3.7), (xE - 0.22, 3.7), label="<<< 5", lpos=0.12)
for y, lab in [(2.8, "$W_j$"), (1.9, "$K_t$")]:
    f.arrow((xE + 1.2, y), (xE + 0.22, y))
    f.text(xE + 1.3, y, lab, ha="left")
for y0, y1 in zip(ys_ops, ys_ops[1:]):
    f.arrow((xE, y0 - 0.22), (xE, y1 + 0.22))
f.line((xs["B"], 1.9), (xs["B"], 1.9))
f.box(xs["B"], 2.4, "<<< 30", w=1.3, h=0.5, fc="white", ec="#555555")
# outputs: rotate positions
y_out = 0.4
f.text(xs["A"], y_out, "新 B")
f.text(xs["B"], y_out, "新 C")
f.text(xs["C"], y_out, "新 D")
f.text(xs["D"], y_out, "新 E")
f.text(xE + 1.8, y_out, "新 A", color=RED)
f.arrow((xs["A"], 0.9), (xs["A"], 0.65))
f.arrow((xs["B"], 0.9), (xs["B"], 0.65))
f.line((xs["C"], 4.9), (xs["C"], 0.9))
f.arrow((xs["C"], 0.9), (xs["C"], 0.65))
f.line((xs["D"], 4.9), (xs["D"], 0.9))
f.arrow((xs["D"], 0.9), (xs["D"], 0.65))
f.arrow((xE, 1.68), (xE, 1.0), (xE + 1.8, 1.0), (xE + 1.8, 0.65), color=RED)
f.text(xE + 1.9, 1.4, "（從最右繞到最左）", ha="left", size=9, color=RED)
f.save("lecture21_sha1_round")

# SHA-1 padding
f = Fig(13, 2.8)
f.box(3.2, 1.4, "訊息 x", w=5.4, h=0.8, round_=False, fc=BOX, ec=BOX_EDGE)
f.box(7.5, 1.4, "1 0 0 … 0", w=3.2, h=0.8, round_=False, fc=ALT, ec=ALT_EDGE)
f.box(10.7, 1.4, "l", w=3.2, h=0.8, round_=False, fc=GREEN, ec=GREEN_EDGE)
f.text(3.2, 2.15, "l bits", size=10, color=GRAY)
f.text(7.5, 2.15, "k+1 bits", size=10, color=GRAY)
f.text(10.7, 2.15, "64 bits", size=10, color=GRAY)
f.text(6.95, 0.6, "總長是 512 的倍數", color=GRAY, va="top")
f.save("lecture21_padding")
