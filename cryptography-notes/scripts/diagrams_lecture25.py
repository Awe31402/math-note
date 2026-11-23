"""Diagrams for lecture25_note.md.  Run: python3 scripts/diagrams_lecture25.py"""

from diagram_lib import ALT, ALT_EDGE, GRAY, Fig, protocol

protocol("lecture25_signature_protocol", ["Alice", "Bob"], [
    ("Bob", "$(k_{pr}, k_{pub})$"),
    ("msg", "Bob", "Alice", "$k_{pub}$"),
    ("Bob", "$s = sig_{k_{pr}}(x)$"),
    ("msg", "Bob", "Alice", "(x, s)"),
    ("Alice", "$ver_{k_{pub}}(x, s)$ = true / false"),
])

protocol("lecture25_mac_protocol", ["Alice", "Bob"], [
    ("span", "k ←—— 共享的秘密金鑰 ——→ k"),
    ("Bob", "$m = MAC_k(x)$"),
    ("msg", "Bob", "Alice", "(x, m)"),
    ("Alice", "$m' = MAC_k(x)$\nm' =? m"),
])


def compress_chain(f, y, x0, inputs, tail="m", iv=True, step=2.4):
    if iv:
        f.text(x0 - 1.0, y, "IV")
        f.arrow((x0 - 0.7, y), (x0 - 0.75, y))
    xs = []
    prev = x0 - 0.7
    for i, inp in enumerate(inputs):
        x = x0 + i * step
        if inp == "…":
            f.text(x, y, "…")
            f.arrow((prev, y), (x - 0.4, y))
            prev = x + 0.4
            continue
        f.box(x, y, "壓縮", w=1.4, h=0.7, fc=ALT, ec=ALT_EDGE)
        f.arrow((prev, y), (x - 0.72, y))
        f.text(x, y - 1.3, inp)
        f.arrow((x, y - 1.05), (x, y - 0.37))
        prev = x + 0.7
        xs.append(x)
    f.arrow((prev, y), (prev + 0.9, y))
    f.text(prev + 1.0, y, tail, ha="left")
    return xs


# Secret prefix MAC: m = h(k || x)
f = Fig(14, 2.8)
compress_chain(f, 2.0, 1.8, ["k", "$x_1$", "$x_2$", "…", "$x_n$"])
f.save("lecture25_secret_prefix")

protocol("lecture25_length_extension", ["Alice", "Oscar", "Bob"], [
    ("Bob", "$m = h(k \\| x_1 \\| … \\| x_n)$"),
    ("msg", "Bob", "Oscar", "(x, m)", "攔截"),
    ("Oscar", "$x_O = (x_1, …, x_n, x_{n+1})$\n$m_O = h(m \\| x_{n+1})$"),
    ("msg", "Oscar", "Alice", "$(x_O, m_O)$"),
    ("Alice", "$m' = h(k \\| x_1 \\| … \\| x_{n+1})$\n$m' = m_O$ → 有效！"),
], widths=[5.6, 5.6, 5.0])

# HMAC: inner and outer hash
f = Fig(16, 6.4)
xs = compress_chain(f, 4.8, 2.4, ["$k^+ \\oplus ipad$", "$x_1$", "$x_2$", "…", "$x_n$"],
                    tail="內層輸出")
y2 = 0.9
f.text(1.4, y2, "IV")
f.arrow((1.7, y2), (1.68, y2))
f.box(2.4, y2, "壓縮", w=1.4, h=0.7, fc=ALT, ec=ALT_EDGE)
f.text(2.4, y2 + 1.3, "$k^+ \\oplus opad$")
f.arrow((2.4, y2 + 1.05), (2.4, y2 + 0.37))
xe = xs[-1]
f.box(xe, y2, "壓縮", w=1.4, h=0.7, fc=ALT, ec=ALT_EDGE)
f.arrow((3.1, y2), (xe - 0.72, y2))
f.arrow((xe + 1.6 + 0.4, 4.45), (xe + 1.6 + 0.4, 2.0), (xe, 2.0), (xe, y2 + 0.37))
f.arrow((xe + 0.7, y2), (xe + 1.6, y2))
f.text(xe + 1.7, y2, "HMAC", ha="left", weight="bold")
f.save("lecture25_hmac")
