---
course: 電子學（三）（112 學年度）
episode: 12
lecture: Lec02 第七章 差動放大器 (2/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=-tpHGJxPH88
notes: 老師第 7 章 = Sedra/Smith 7e Ch9；§9.1 MOS 差動對 (p. 596)、§9.1.2 輸入共模範圍、§9.3 共模拒斥 (p. 627)、半電路
---

# 第 12 集 · 112-Lec02：差模與共模、輸入共模範圍、尾電流源的電阻、半電路（蹺蹺板） [▶ 影片](https://www.youtube.com/watch?v=-tpHGJxPH88)

← 上一集：[11](11-mos-bias-review-toward-diff-pair.md) ｜ [總目錄](../README.md) ｜ 下一集：[13](13-diff-amp-rss-cascode-level-shift-active-load.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 12 集（112 學年度 Lec02）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:01:44，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed. §9.1
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 把兩個輸入拆成差模和共模](#1-把兩個輸入拆成差模和共模)
- [2. 用疊加：直流、差模、共模分開算](#2-用疊加直流差模共模分開算)
- [3. 差模增益](#3-差模增益)
- [4. 理想電流源時共模輸出是 0](#4-理想電流源時共模輸出是-0)
- [5. 輸入共模範圍（ICMR）](#5-輸入共模範圍icmr)
- [6. 真實的電流源：$R_{SS}$](#6-真實的電流源r_ss)
- [7. 差模：中點是蹺蹺板的支點](#7-差模中點是蹺蹺板的支點)
- [8. 共模：每邊看到 $2R_{SS}$](#8-共模每邊看到-2r_ss)
- [9. 例：汲極間接負載、低電壓的現代差動對](#9-例汲極間接負載低電壓的現代差動對)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

正式分析 MOS 差動放大器：兩個輸入拆成**差模**和**共模**，各自的增益是多少；直流上共模輸入能放多大（ICMR）；尾電流源不理想時怎麼辦——用**半電路**最快。

---

## 1. 把兩個輸入拆成差模和共模

[▶ 00:30](https://youtu.be/-tpHGJxPH88?t=30)

MOS 差動對：兩顆源極相接、共用尾電流源 $I$，汲極各經 $R_D$ 接 $V_{DD}$。功能：把輸入的**差**放大。輸出可從任一邊拉。[▶ 01:32](https://youtu.be/-tpHGJxPH88?t=92)

任何兩個輸入都可以改寫成：[▶ 04:05](https://youtu.be/-tpHGJxPH88?t=245)

$$
v_1 = v_{cm} + \frac{v_{id}}{2},\quad
v_2 = v_{cm} - \frac{v_{id}}{2},
\qquad
v_{id} = v_1 - v_2,\quad
v_{cm} = \frac{v_1 + v_2}{2}
$$

$v_{id}$：**差模**（differential）信號；$v_{cm}$：**共模**（common-mode）信號。等效上就是在兩邊各放 $\pm\frac12v_{id}$，再加一個共同的 $v_{cm}$。[▶ 07:45](https://youtu.be/-tpHGJxPH88?t=465)

---

## 2. 用疊加：直流、差模、共模分開算

[▶ 08:17](https://youtu.be/-tpHGJxPH88?t=497)

信號源有：$V_{DD}$、$I$、$v_{id}$、$v_{cm}$。線性，所以一個一個算再相加（superposition）：

- **直流**（$v_{id} = v_{cm} = 0$）：完全對稱，$I$ 一人一半 → $V_{O1} = V_{O2} = V_{DD} - \frac12IR_D$。不管兩顆 $k$、$V_t$ 多少，只要一樣就對稱。[▶ 09:49](https://youtu.be/-tpHGJxPH88?t=589)
- 差模、共模：讓 $V_{DD}$、$I$ 都設 0（$V_{DD}$ 在頭上，接地；$I$ 開路）。[▶ 12:23](https://youtu.be/-tpHGJxPH88?t=743)

---

## 3. 差模增益

[▶ 13:24](https://youtu.be/-tpHGJxPH88?t=804)

只有 $\pm\frac12v_{id}$：一邊電流往上、一邊往下；尾電流源開路，兩個電流相加 = 0，大小一樣。走一圈：$\frac12v_{id} = v + v'$，對稱 → 每顆 $v_{gs} = \frac12v_{id}$。[▶ 16:28](https://youtu.be/-tpHGJxPH88?t=988)

小信號（複習）：$\frac12k(V_{GS} - V_t + v)^2$ 展開，$v \ll 2(V_{GS} - V_t)$（取 ≤ 0.2 倍）時才線性，$i = g_mv$。[▶ 18:39](https://youtu.be/-tpHGJxPH88?t=1119)

$$
v_{o1} = -\frac12g_mR_Dv_{id},
\qquad
v_{o2} = +\frac12g_mR_Dv_{id}
$$

單端差模增益 $A_d = \frac12g_mR_D$，兩個輸出大小一樣、相位相反。例 $k = 2$、1 mA：$g_m = 2$ mA/V（【口頭】$k = 2$ 只是好算，買來的 $k$ 大很多）。[▶ 27:02](https://youtu.be/-tpHGJxPH88?t=1622)

**條件**：$v_{id}$ 要夠小，否則不是線性放大器。[▶ 31:41](https://youtu.be/-tpHGJxPH88?t=1901)

---

## 4. 理想電流源時共模輸出是 0

[▶ 32:45](https://youtu.be/-tpHGJxPH88?t=1965)

只有 $v_{cm}$（兩邊同時加一樣的）：對稱，兩個交流電流一樣大、同方向；但底下尾電流源開路，兩個相加必須是 0 → 兩個都是 0 → **共模輸出 0**。[▶ 34:52](https://youtu.be/-tpHGJxPH88?t=2092)

$$
v_{o1,2} = V_{DD} - \frac12IR_D \mp \frac12g_mR_Dv_{id}
$$

---

## 5. 輸入共模範圍（ICMR）

[▶ 37:32](https://youtu.be/-tpHGJxPH88?t=2252)

例：5 V 和 5.01 V → $v_{id} = 0.01$ 夠小、可以放大；但共模是 5 V！共模其實是一個**直流**偏壓（大寫）——太大，MOS 跳出飽和區，前面的公式全都不對。[▶ 39:05](https://youtu.be/-tpHGJxPH88?t=2345)

**例**（±10 V、$k = 2$、$I = 2$ mA、$V_t = 1$）[▶ 44:16](https://youtu.be/-tpHGJxPH88?t=2656)：每顆 1 mA → $V_{GS} = 2$ V；尾電流鏡（$k$ 也取 2 倍）$V_{GS} = 2$ V、閘極 −8 V；汲極 5 V。共模 $V_{CM}$ 從 0 往上抬，源極跟著 $V_{CM} - 2$。

- **Q1、Q2 飽和**：$5 \ge V_{CM} - 1$ → $V_{CM} \le 6$ V。[▶ 47:52](https://youtu.be/-tpHGJxPH88?t=2872)
- **Q3（尾電流）飽和**：$V_{CM} - 2 \ge -8 - 1$ → $V_{CM} \ge -7$ V。[▶ 50:28](https://youtu.be/-tpHGJxPH88?t=3028)

$$
-7\ \text{V} \le V_{CM} \le 6\ \text{V}
$$

這叫**輸入共模範圍**（input common-mode range, ICMR）。[▶ 56:32](https://youtu.be/-tpHGJxPH88?t=3392)

【口頭】差動放大器能動有兩個條件，缺一不可：① 共模在 ICMR 內（直流偏壓正常）；② 差模滿足小信號近似。拿到一個差動放大器，第一件事就是看它的共模範圍。[▶ 55:01](https://youtu.be/-tpHGJxPH88?t=3301)

---

## 6. 真實的電流源：$R_{SS}$

[▶ 57:37](https://youtu.be/-tpHGJxPH88?t=3457)

實際電流源有 Early 效應的電阻 $r_o$；做成疊接（cascode）電流源，往下看是 $g_mr_o\cdot r_o$（前一章），很大但不是無窮大。統一用 $R_{SS}$ 表示尾電流源的輸出電阻。[▶ 1:00:09](https://youtu.be/-tpHGJxPH88?t=3609)

---

## 7. 差模：中點是蹺蹺板的支點

[▶ 1:02:13](https://youtu.be/-tpHGJxPH88?t=3733)

只加 $\pm\frac12v_{id}$，假設源極節點電壓 $v$、可能有電流流進 $R_{SS}$。兩邊 $v_{gs}$ 分別是 $\frac12v_{id} - v$ 和 $-\frac12v_{id} - v$，KCL：

$$
g_m\left(\tfrac12v_{id} - v\right) + g_m\left(-\tfrac12v_{id} - v\right) = \frac{v}{R_{SS}}
\quad\Longrightarrow\quad
v\left(2g_m + \frac{1}{R_{SS}}\right) = 0
\quad\Longrightarrow\quad
v = 0
$$

[▶ 1:08:32](https://youtu.be/-tpHGJxPH88?t=4112)

源極節點**交流電壓 = 0**，$R_{SS}$ 上沒有電流，有沒有它都一樣。【口頭】像蹺蹺板：一邊上去、一邊下來，中間的**支點**（pivot）不動。[▶ 1:11:07](https://youtu.be/-tpHGJxPH88?t=4267)

→ 差模增益完全不變，仍是 $\frac12g_mR_D$。而且可以直接把源極接地，**拆成左右兩個半電路**各自算：[▶ 1:17:22](https://youtu.be/-tpHGJxPH88?t=4642)

$$
v_{o1} = -g_mR_D\cdot\frac{v_{id}}{2}
$$

---

## 8. 共模：每邊看到 $2R_{SS}$

[▶ 1:19:30](https://youtu.be/-tpHGJxPH88?t=4770)

只加 $v_{cm}$（拿掉直流源，但 $R_{SS}$ 還在）。兩邊電流 $i$ 一樣（很小），$R_{SS}$ 流 $2i$：[▶ 1:22:38](https://youtu.be/-tpHGJxPH88?t=4958)

$$
v_{cm} = \frac{i}{g_m} + 2iR_{SS}
\quad\Longrightarrow\quad
i = \frac{v_{cm}}{1/g_m + 2R_{SS}} \approx \frac{v_{cm}}{2R_{SS}}
$$

（$g_mR_{SS} \ge g_mr_o \gg 1$——一顆 MOS 最大的增益就是 $g_mr_o$。）[▶ 1:25:14](https://youtu.be/-tpHGJxPH88?t=5114)

$$
v_{o1} = v_{o2} = -\frac{R_D}{2R_{SS}}v_{cm},
\qquad
A_{cm} = -\frac{R_D}{2R_{SS}}
$$

$R_{SS}$ 做到上萬倍大，共模增益就非常小，可以忽略，只剩差模。【口頭】共模電壓幾乎都跨在 $R_{SS}$ 上，浪費掉了。[▶ 1:29:21](https://youtu.be/-tpHGJxPH88?t=5361)

**共模半電路** [▶ 1:31:26](https://youtu.be/-tpHGJxPH88?t=5486)：把 $R_{SS}$ 拆成兩個 $2R_{SS}$ 並聯，每邊一個，中間沒電流可以切開——每邊是「源極接 $2R_{SS}$」的共源（源極退化）。

$$
v_{o1,2} = V_{DD} - \frac12IR_D - \frac{R_D}{2R_{SS}}v_{cm} \mp \frac12g_mR_Dv_{id}
$$

> 【課本補充】§9.3 (p. 627)：**共模拒斥比** CMRR $= |A_d/A_{cm}| = g_mR_{SS}$（單端），越大越好。

---

## 9. 例：汲極間接負載、低電壓的現代差動對

**正常一點的數字** [▶ 1:36:15](https://youtu.be/-tpHGJxPH88?t=5775)：$k$ 取大一點，$g_m = 20$ mA/V、$R_D = 5$ k → 兩個輸出 ∓50 倍。$R_{SS}$ 在差模時不用理它（支點）。[▶ 1:40:33](https://youtu.be/-tpHGJxPH88?t=6033)

**汲極之間接 $R_L$** [▶ 1:42:11](https://youtu.be/-tpHGJxPH88?t=6131)：差模時兩端一上一下，$R_L$ 中點也是支點 → 拆成兩個 $\frac12R_L$ 接地：

$$
A_d = \frac12g_m\left(R_D\parallel\tfrac12R_L\right)
$$

**現代低電壓版** [▶ 1:47:19](https://youtu.be/-tpHGJxPH88?t=6439)：電源 5 V / 0 V（現在 IC 電源最低是 0，最高約 5 V 以下）。$k = 200$、每顆 1 mA → $V_{GS} = 1 + \sqrt{2/200} = 1.1$ V；尾電流 2 mA（$k$ 取 400，$V_{GS}$ 也約 1.1 V）；汲極 3 V。[▶ 1:50:25](https://youtu.be/-tpHGJxPH88?t=6625)

- Q1、Q2 飽和：$3 \ge V_{CM} - 1$ → $V_{CM} \le 4$ V。[▶ 1:53:41](https://youtu.be/-tpHGJxPH88?t=6821)
- 尾電流管飽和：源極 $V_{CM} - 1.1 \ge 1.1 - 1$ → $V_{CM} \ge 1.2$ V。[▶ 1:54:45](https://youtu.be/-tpHGJxPH88?t=6885)

$$
1.2\ \text{V} \le V_{CM} \le 4\ \text{V}
$$

【口頭】範圍不包括 0，所以正弦信號（中心 0 V）**不能直接接**，要先墊一個在範圍內的直流（例如 2～3 V）。±10 V 的電路範圍包括 0，才可以直接接。[▶ 1:57:58](https://youtu.be/-tpHGJxPH88?t=7078)

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 拆分 | $v_{id} = v_1 - v_2$，$v_{cm} = \frac{v_1+v_2}{2}$ | |
| 直流 | $V_{DD} - \frac12IR_D$ | 對稱 |
| 差模 | $v_{o1,2} = \mp\frac12g_mR_Dv_{id}$ | 源極節點交流 0 |
| 共模（理想 $I$） | 0 | |
| 共模（$R_{SS}$） | $A_{cm} = -R_D/(2R_{SS})$ | 每邊 $2R_{SS}$ |
| CMRR | $g_mR_{SS}$ | |
| ICMR | 三顆都飽和 | 例 −7～6 V、1.2～4 V |
| 半電路 | 差模：中點接地；共模：每邊 $2R_{SS}$ | 蹺蹺板支點 |
| 汲極間 $R_L$ | 每邊 $R_D\parallel\frac12R_L$ | |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 半電路 | 之後所有差動電路 |
| 不匹配 → 共模變差模 | 下一集起：失配、偏移電壓 |
| ICMR | op amp 輸入級 |

---

## 附：本集一句話總結

> **兩個輸入可拆成差模 $v_{id}$ 和共模 $v_{cm}$：差模時兩邊一上一下，源極節點像蹺蹺板支點交流為 0，尾電流源有沒有電阻都一樣，每邊增益 $\mp\frac12g_mR_D$，可以直接用半電路；共模時每邊看到 $2R_{SS}$，增益只有 $-R_D/(2R_{SS})$；但共模其實是直流偏壓，要在輸入共模範圍內（三顆都飽和）電路才會動，例如 ±10 V 時 −7～6 V，5 V 電源時 1.2～4 V。**

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec02 錄影逐字稿（whisper，2:01:44）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
