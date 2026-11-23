"""Diagrams for lecture06_note.md.  Run: python3 scripts/diagrams_lecture06.py"""

from diagram_lib import ALT, ALT_EDGE, GRAY, PARTY, Fig

# DES key schedule
f = Fig(11, 9.4)
cx = 3.6
f.text(cx, 9.0, "k（64 bit）")
f.arrow((cx, 8.7), (cx, 8.15))
f.box(cx, 7.8, "PC-1", w=1.8, h=0.65)
f.arrow((cx, 7.45), (cx, 7.0), label="56", loff=0.12)
xc, xd = 1.8, 5.4
f.line((xc, 7.0), (xd, 7.0))
f.arrow((xc, 7.0), (xc, 6.65))
f.arrow((xd, 7.0), (xd, 6.65))
rows = [("$C_0$（28）", "$D_0$（28）", None),
        ("$C_1$", "$D_1$", "$LS_1$"),
        ("$C_2$", "$D_2$", "$LS_2$"),
        ("⋮", "⋮", None),
        ("$C_{16}$", "$D_{16}$", "$LS_{16}$")]
ys = [6.3, 4.8, 3.3, 2.15, 1.0]
keys = {1: "$k_1$（48）", 2: "$k_2$", 4: "$k_{16}$"}
for i, ((c, d, ls), y) in enumerate(zip(rows, ys)):
    if c == "⋮":
        f.text(xc, y, "⋮")
        f.text(xd, y, "⋮")
        continue
    f.box(xc, y, c, w=1.8, h=0.65, fc=ALT, ec=ALT_EDGE)
    f.box(xd, y, d, w=1.8, h=0.65, fc=ALT, ec=ALT_EDGE)
    if i in keys:
        f.box(8.1, y, "PC-2", w=1.3, h=0.6)
        f.arrow((xd + 0.9, y), (7.45, y))
        f.arrow((8.75, y), (9.3, y))
        f.text(9.4, y, keys[i], ha="left")
for i in range(1, len(rows)):
    y0, y1 = ys[i - 1], ys[i]
    top = y0 - (0.33 if rows[i - 1][0] != "⋮" else 0.25)
    bot = y1 + (0.33 if rows[i][0] != "⋮" else 0.25)
    lab = rows[i][2]
    f.arrow((xc, top), (xc, bot), label=lab, loff=0.12)
    f.arrow((xd, top), (xd, bot), label=lab, loff=0.12)
f.save("lecture06_key_schedule")

# Decryption peels the rounds off in reverse order
f = Fig(13, 10.2)
xa, xb = 2.6, 10.2
f.text(xa, 9.8, "Alice（加密）", weight="bold", color=PARTY["Alice"])
f.text(xb, 9.8, "Bob（解密）", weight="bold", color=PARTY["Bob"])
left = ["x", "[IP]", "[$R_1(e)$]", "[$R_2(e)$]", "⋮", "[$R_{16}(e)$]", "[$IP^{-1}$]", "y"]
right = ["y", "[IP]", "[$R_1(d)$]", "[$R_2(d)$]", "⋮", "[$R_{16}(d)$]", "[$IP^{-1}$]", "x ✔"]
ys = [9.1 - i * 1.15 for i in range(8)]


def column(x, items):
    for i, (it, y) in enumerate(zip(items, ys)):
        if it.startswith("["):
            f.box(x, y, it[1:-1], w=2.0, h=0.65)
        else:
            f.text(x, y, it)
        if i:
            h0 = 0.33 if items[i - 1].startswith("[") else 0.22
            h1 = 0.33 if it.startswith("[") else 0.22
            f.arrow((x, ys[i - 1] - h0), (x, y + h1))


column(xa, left)
column(xb, right)
# pairs that cancel each other
pairs = [(6, 1, ""), (5, 2, ""), (2, 5, ""), (1, 6, "")]
for li, ri, lab in pairs:
    f.line((xa + 1.0, ys[li]), (xb - 1.0, ys[ri]), color=ALT_EDGE, ls="--", lw=1.1)
f.text(xb + 1.2, ys[1], "← 抵銷加密端最後的 $IP^{-1}$", ha="left", size=9, color=GRAY)
f.text(xb + 1.2, ys[2], "倒轉 $R_{16}(e)$", ha="left", size=9, color=GRAY)
f.text(xb + 1.2, ys[3], "倒轉 $R_{15}(e)$", ha="left", size=9, color=GRAY)
f.text(xb + 1.2, ys[5], "倒轉 $R_1(e)$", ha="left", size=9, color=GRAY)
f.text((xa + xb) / 2, 0.45, "成對互相抵銷，像洋蔥一樣一層層剝回去", color=ALT_EDGE, size=10)
f.text((xa + xb) / 2, ys[7], "Alice 的 y 經網路送給 Bob →（右上）", color=GRAY, size=10)
f.save("lecture06_decryption_reverse")
