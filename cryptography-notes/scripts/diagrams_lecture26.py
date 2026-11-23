"""Diagrams for lecture26_note.md.  Run: python3 scripts/diagrams_lecture26.py"""

from diagram_lib import GRAY, GREEN_EDGE, PARTY, RED, Fig, protocol, tree

# Alice and Bob share k
f = Fig(10, 2.4)
f.text(1.0, 1.6, "Alice", weight="bold", color=PARTY["Alice"])
f.text(8.6, 1.6, "Bob", weight="bold", color=PARTY["Bob"])
f.arrow((1.8, 1.6), (7.9, 1.6), label="$e_k(x) = y$")
f.text(1.0, 0.7, "k")
f.text(8.6, 0.7, "k")
f.save("lecture26_shared_key")

tree("lecture26_key_establishment",
     ("金鑰建立", ["金鑰傳送\n(key transport)", "金鑰協議\n(key agreement)"]),
     leaf_w=3.6)

# KDF
f = Fig(11, 2.8)
f.text(0.9, 2.2, "$k_{AB}$")
f.text(0.9, 0.7, "r")
f.line((1.5, 2.2), (2.6, 2.2), (2.6, 1.45))
f.line((1.3, 0.7), (2.6, 0.7), (2.6, 1.45))
f.arrow((2.6, 1.45), (3.8, 1.45))
f.box(4.8, 1.45, "KDF", w=2.0, h=0.75)
f.arrow((5.8, 1.45), (7.0, 1.45))
f.text(7.1, 1.45, "$k_{ses}$", ha="left")
f.text(1.6, 0.25, "（r 不是秘密）", ha="left", color=GRAY, size=10)
f.save("lecture26_kdf")

protocol("lecture26_nonce_session_key", ["Alice", "Bob"], [
    ("Bob", "產生 nonce r"),
    ("msg", "Bob", "Alice", "r"),
    (("Alice", "$k_{ses} = e_{k_{AB}}(r)$"), ("Bob", "$k_{ses} = e_{k_{AB}}(r)$")),
])

protocol("lecture26_kdc_basic", ["Alice", "KDC", "Bob"], [
    (("Alice", "KEK: $k_A$"), ("KDC", "KEK: $k_A$, $k_B$"), ("Bob", "KEK: $k_B$")),
    ("msg", "Alice", "KDC", "$RQST(ID_A, ID_B)$"),
    ("KDC", "產生隨機 $k_{ses}$\n$y_A = e_{k_A}(k_{ses})$\n$y_B = e_{k_B}(k_{ses})$"),
    ("msg", "KDC", "Alice", "$y_A$, $y_B$"),
    ("Alice", "$k_{ses} = e^{-1}_{k_A}(y_A)$\n$y = e_{k_{ses}}(x)$"),
    ("msg", "Alice", "Bob", "y, $y_B$"),
    ("Bob", "$k_{ses} = e^{-1}_{k_B}(y_B)$\n$x = e^{-1}_{k_{ses}}(y)$"),
], col_w=5.0)

# No perfect forward secrecy
f = Fig(13, 2.8)
f.arrow((0.4, 1.8), (12.4, 1.8))
f.text(12.5, 1.8, "時間", ha="left")
f.line((6.0, 1.4), (6.0, 2.2), color=RED, lw=2)
f.text(6.0, 2.45, "$k_A$ 外洩", color=RED, va="bottom")
f.text(3.0, 1.2, "過去\n（全部都能被解密！）", color=RED, va="top")
f.text(9.2, 1.2, "之後換新金鑰，未來安全", color=GREEN_EDGE, va="top")
f.save("lecture26_forward_secrecy")

protocol("lecture26_kdc_attack", ["Alice", "Oscar", "KDC", "Bob"], [
    (("Alice", "KEK: $k_A$"), ("Oscar", "KEK: $k_O$"), ("KDC", "KEK: $k_A, k_B, k_O$"),
     ("Bob", "KEK: $k_B$")),
    ("msg", "Alice", "Oscar", "$RQST(ID_A, ID_B)$"),
    ("Oscar", "換掉成"),
    ("msg", "Oscar", "KDC", "$RQST(ID_A, ID_O)$"),
    ("KDC", "隨機 $k_{ses}$\n$y_A = e_{k_A}(k_{ses})$\n$y_O = e_{k_O}(k_{ses})$"),
    ("msg", "KDC", "Alice", "$y_A$, $y_O$"),
    ("Alice", "$k_{ses} = e^{-1}_{k_A}(y_A)$\n$y = e_{k_{ses}}(x)$"),
    ("msg", "Alice", "Oscar", "y, $y_O$", "攔截"),
    ("Oscar", "$k_{ses} = e^{-1}_{k_O}(y_O)$\n$x = e^{-1}_{k_{ses}}(y)$"),
], col_w=4.6)

protocol("lecture26_kerberos", ["Alice", "KDC", "Bob"], [
    (("Alice", "KEK: $k_A$"), ("KDC", "KEK: $k_A$, $k_B$"), ("Bob", "KEK: $k_B$")),
    ("Alice", "產生 nonce $r_A$"),
    ("msg", "Alice", "KDC", "$RQST(ID_A, ID_B, r_A)$"),
    ("KDC", "產生隨機 $k_{ses}$\n產生有效期限 T\n$y_A = e_{k_A}(k_{ses}, r_A, T, ID_B)$\n"
            "$y_B = e_{k_B}(k_{ses}, ID_A, T)$"),
    ("msg", "KDC", "Alice", "$y_A$, $y_B$"),
    ("Alice", "$(k_{ses}, r'_A, T, ID_B) = e^{-1}_{k_A}(y_A)$\n檢查 $r'_A = r_A$\n檢查 $ID_B$\n"
              "檢查有效期限 T\n產生時間戳記 $T_S$\n$y_{AB} = e_{k_{ses}}(ID_A, T_S)$"),
    ("msg", "Alice", "Bob", "$y_{AB}$, $y_B$"),
    ("Bob", "$(k_{ses}, ID_A, T) = e^{-1}_{k_B}(y_B)$\n$(ID'_A, T_S) = e^{-1}_{k_{ses}}(y_{AB})$\n"
            "檢查 $ID'_A = ID_A$\n檢查有效期限 T\n檢查時間戳記 $T_S$"),
    ("msg", "Alice", "Bob", "$y = e_{k_{ses}}(x)$"),
    ("Bob", "$x = e^{-1}_{k_{ses}}(y)$"),
], col_w=6.0)
