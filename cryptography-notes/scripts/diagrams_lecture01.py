"""Diagrams for lecture01_note.md.  Run: python3 scripts/diagrams_lecture01.py"""

from diagram_lib import ALT, ALT_EDGE, Fig, channel, tree

# 1. Cryptology family tree
tree("lecture01_cryptology_tree",
     ("Cryptology\n（密碼學）", [
         ("Cryptography\n（密碼編碼學）", [
             "Symmetric Ciphers\n（對稱式）",
             "Asymmetric Ciphers\n（非對稱式 = 公鑰）",
             "Protocols\n（協定）"]),
         "Cryptanalysis\n（密碼分析學）"]),
     leaf_w=3.4)

# 2. Crypto is one component of security
f = Fig(11, 4.2)
f.frame(0.3, 0.3, 10.7, 3.9, "Security（資訊安全）", ec="#555555", ls="-")
for x, s in [(1.8, "安全軟體"), (4.2, "安全作業系統"), (6.8, "安全硬體"), (9.0, "…")]:
    f.text(x, 3.0, s)
f.box(5.5, 1.5, "Cryptography", w=3.2, h=0.9, fc=ALT, ec=ALT_EDGE, weight="bold")
f.text(7.4, 1.5, "← 核心元件", ha="left", color=ALT_EDGE)
f.save("lecture01_security_cryptography")


# 3. Basic setting with eavesdropper
channel("lecture01_channel_oscar", enc="e( )", dec="d( )", key_label=None, oscar=True)
# 4. Symmetric setting with key over secure channel
channel("lecture01_channel_key", enc="e( )", dec="d( )")

# 5. Cryptanalysis taxonomy
tree("lecture01_cryptanalysis_tree",
     ("Cryptanalysis\n（密碼分析 / 攻擊）", [
         ("Classical Cryptanalysis\n（古典密碼分析）", [
             "Mathematical Analysis\n（數學 / 分析攻擊）",
             "Brute-Force Attacks\n（暴力攻擊）"]),
         "Social Engineering\n（社交工程）",
         "Implementation Attacks\n（實作攻擊）"]),
     leaf_w=3.6)
