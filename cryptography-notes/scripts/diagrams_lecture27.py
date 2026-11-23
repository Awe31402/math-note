"""Diagrams for lecture27_note.md.  Run: python3 scripts/diagrams_lecture27.py"""

from diagram_lib import protocol

protocol("lecture27_hybrid_key_transport", ["Alice", "Bob"], [
    ("Bob", "產生 $(k_{pr}, k_{pub})$"),
    ("msg", "Bob", "Alice", "$k_{pub}$"),
    ("Alice", "隨機選 k（例如 128 bit）\n$y = e_{k_{pub}}(k)$"),
    ("msg", "Alice", "Bob", "y"),
    ("Bob", "$k = d_{k_{pr}}(y)$"),
    ("span", "之後雙方用 k 做 AES 加解密"),
], col_w=6.0)

protocol("lecture27_dh", ["Alice", "Bob"], [
    (("Alice", "$a = k_{pr,A}$\n$A = \\alpha^a$"), ("Bob", "$b = k_{pr,B}$\n$B = \\alpha^b$")),
    ("msg", "Alice", "Bob", "A"),
    ("msg", "Bob", "Alice", "B"),
    (("Alice", "$k_{AB} = B^a$"), ("Bob", "$k_{AB} = A^b$")),
], col_w=6.0)

protocol("lecture27_mitm", ["Alice", "Oscar", "Bob"], [
    (("Alice", "a,  $A = \\alpha^a$"), ("Bob", "b,  $B = \\alpha^b$")),
    ("msg", "Alice", "Oscar", "A", "攔截"),
    ("Oscar", "$\\tilde{A} = \\alpha^{o_1}$\n$\\tilde{B} = \\alpha^{o_2}$"),
    ("msg", "Oscar", "Bob", "$\\tilde{A}$"),
    ("msg", "Bob", "Oscar", "B", "攔截"),
    ("msg", "Oscar", "Alice", "$\\tilde{B}$"),
    (("Alice", "$k_{AO} = \\tilde{B}^a$"), ("Oscar", "$k_{AO} = A^{o_2}$\n$k_{BO} = B^{o_1}$"),
     ("Bob", "$k_{BO} = \\tilde{A}^b$")),
], col_w=5.4)

protocol("lecture27_mitm_reading", ["Alice", "Oscar", "Bob"], [
    ("Alice", "$y = AES_{k_{AO}}(x)$"),
    ("msg", "Alice", "Oscar", "y"),
    ("Oscar", "$x = AES^{-1}_{k_{AO}}(y)$　← 能讀\n（可以改 x）\n$y' = AES_{k_{BO}}(x)$"),
    ("msg", "Oscar", "Bob", "y'"),
    ("Bob", "$x = AES^{-1}_{k_{BO}}(y')$"),
], col_w=5.6)

protocol("lecture27_cert_user_keys", ["Alice", "CA"], [
    ("Alice", "產生 $k_{pr,A}$, $k_{pub,A}$"),
    ("msg", "Alice", "CA", "$RQST(k_{pub,A}, ID_A)$"),
    ("CA", "驗證 $ID_A$\n$s_A = sig_{k_{pr,CA}}(k_{pub,A}, ID_A)$\n$Cert_A = [(k_{pub,A}, ID_A), s_A]$"),
    ("msg", "CA", "Alice", "$Cert_A$"),
], col_w=6.4)

protocol("lecture27_cert_ca_keys", ["Alice", "CA"], [
    ("msg", "Alice", "CA", "$RQST(ID_A)$"),
    ("CA", "驗證 $ID_A$\n產生 $k_{pr,A}$, $k_{pub,A}$\n$s_A = sig_{k_{pr,CA}}(k_{pub,A}, ID_A)$\n"
           "$Cert_A = [(k_{pub,A}, ID_A), s_A]$"),
    ("msg", "CA", "Alice", "$Cert_A$, $k_{pr,A}$"),
], col_w=6.4)

protocol("lecture27_dh_with_certs", ["Alice", "Bob"], [
    (("Alice", "$a = k_{pr,A}$,  $A = \\alpha^a$\n$Cert_A = [(A, ID_A), s_A]$"),
     ("Bob", "$b = k_{pr,B}$,  $B = \\alpha^b$\n$Cert_B = [(B, ID_B), s_B]$")),
    ("msg", "Alice", "Bob", "$Cert_A$"),
    ("msg", "Bob", "Alice", "$Cert_B$"),
    (("Alice", "驗證憑證：\n$ver_{k_{pub,CA}}(Cert_B)$\n算會期金鑰：\n$k_{AB} = B^a$"),
     ("Bob", "驗證憑證：\n$ver_{k_{pub,CA}}(Cert_A)$\n算會期金鑰：\n$k_{AB} = A^b$")),
], col_w=6.4)

protocol("lecture27_cross_cert", ["Alice", "CA2"], [
    ("msg", "Alice", "CA2", "$RQST(Cert_{CA2})$"),
    ("msg", "CA2", "Alice", "$Cert_{CA2}$"),
    ("Alice", "$ver_{k_{pub,CA1}}(Cert_{CA2})$ ⇒ $k_{pub,CA2}$ 有效\n"
              "$ver_{k_{pub,CA2}}(Cert_B)$ ⇒ $k_{pub,B}$ 有效"),
], col_w=6.4)
