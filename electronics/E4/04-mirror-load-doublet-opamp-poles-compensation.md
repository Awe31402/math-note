---
course: 電子學（四）（112 學年度）
episode: 4
lecture: Lec04 第九章 放大器頻率響應 (4/5)
date: 112 學年度
video: https://www.youtube.com/watch?v=RUoG3SQOdAI
notes: 老師第 9 章 = Sedra/Smith 7e Ch10、Ch11；§10.7.2 電流鏡負載差動對的高頻響應 (p. 769 起)、§11.9 波德圖看穩定度 (p. 885)、§11.10 頻率補償 (p. 889)
---

# 第 4 集 · Lec04：電流鏡負載差動對的頻率響應（極零點對）、兩級 op amp 的兩個極點與零點消除、震盪條件數值例、相位邊限、主極點補償 [▶ 影片](https://www.youtube.com/watch?v=RUoG3SQOdAI)

← 上一集：[03](03-cd-cs-opamp-cascode-cc-cb-diff-cmrr.md) ｜ [總目錄](../README.md) ｜ 下一集：[05](05-compensation-phase-margin-output-power-intro.md) →

> **課程**：電子學（四），陽明交大 電子物理系，112 學年度 — 第 4 集（Lec04）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:08:08，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 電流鏡負載差動對：剩哪些電容](#1-電流鏡負載差動對剩哪些電容)
- [2. 短路電流：電流鏡那條路有一個極零點對](#2-短路電流電流鏡那條路有一個極零點對)
- [3. 第一級的完整頻率響應](#3-第一級的完整頻率響應)
- [4. 第二級 CS：把右半平面零點移到無窮遠](#4-第二級-cs把右半平面零點移到無窮遠)
- [5. 兩級 op amp 的極點](#5-兩級-op-amp-的極點)
- [6. 接回授後的震盪條件](#6-接回授後的震盪條件)
- [7. 數值例：三個極點](#7-數值例三個極點)
- [8. 相位邊限 45°](#8-相位邊限-45)
- [9. 電壓隨耦器（β = 1）：主極點補償](#9-電壓隨耦器β--1主極點補償)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

整個電子學都繞著 CMOS 兩級 op amp。這集把它的頻率響應整個做完：第一級（電流鏡負載差動對）、第二級（CS）；再看接回授後會不會震、怎麼補償。

---

## 1. 電流鏡負載差動對：剩哪些電容

[▶ 00:32](https://youtu.be/RUoG3SQOdAI?t=32)

低頻 $A_d = g_m(r_{o2}\parallel r_{o4})$。每顆 MOS 四個電容；基底：NMOS 接最負、PMOS 接最高。兩端固定（AC 地）的拿掉。[▶ 02:08](https://youtu.be/RUoG3SQOdAI?t=128)

- **電流鏡二極體那邊的節點**：二極體接法看進去 $\frac{1}{g_{m3}}\parallel r_o\parallel r_o \approx \frac{1}{g_{m3}}$，很小。這個節點上的電容（$Q_3$、$Q_4$ 的 $C_{gs}$、$Q_1$ 的 $C_{gd}$、汲極到基底等）合成 $C_3$。這裡的 Miller 只有約 1 倍。[▶ 05:17](https://youtu.be/RUoG3SQOdAI?t=317)
- **尾節點**的電容只影響共模（上一集）；差模時尾節點是 AC 地。[▶ 08:51](https://youtu.be/RUoG3SQOdAI?t=531)
- **輸出節點**：看到 $r_{o2}\parallel r_{o4}$（很大），電容合成 $C_4$。輸入那顆的 $C_{gd}$ 跨在輸入和輸出之間，有 Miller。[▶ 17:40](https://youtu.be/RUoG3SQOdAI?t=1060)

【口頭】第一級的 $k$（$W/L$）比較小，面積小，電容也小。[▶ 21:41](https://youtu.be/RUoG3SQOdAI?t=1301)

---

## 2. 短路電流：電流鏡那條路有一個極零點對

[▶ 23:47](https://youtu.be/RUoG3SQOdAI?t=1427)

照舊做兩次：先短路電流、再輸出阻抗。輸出短路 → 對稱，尾節點 0。

- 右邊 $Q_2$ 直接給 $\frac12g_mv_{id}$。
- 左邊 $Q_1$ 的 $\frac12g_mv_{id}$ 流進電流鏡節點，被 $\frac{1}{g_{m3}}$ 和 $C_3$ 分掉：節點電壓 $v = \frac{i}{g_{m3} + sC_3}$，鏡像到右邊是 $g_{m4}v$（$g_{m4} = g_{m3}$）。[▶ 26:21](https://youtu.be/RUoG3SQOdAI?t=1581)

$$
i_{sc} = \frac12g_mv_{id}\left[1 + \frac{1}{1 + sC_3/g_{m3}}\right]
= g_mv_{id}\cdot\frac{1 + s\frac{C_3}{2g_{m3}}}{1 + s\frac{C_3}{g_{m3}}}
$$

[▶ 29:29](https://youtu.be/RUoG3SQOdAI?t=1769)

一個極點 $\frac{g_{m3}}{C_3}$、一個零點 $\frac{2g_{m3}}{C_3}$（剛好兩倍）。物理意義：頻率很高時 $C_3$ 短路，鏡像那一半沒了，只剩右邊那一半 → 一定先掉一半（極點）再平（零點）。[▶ 32:04](https://youtu.be/RUoG3SQOdAI?t=1924)

---

## 3. 第一級的完整頻率響應

[▶ 33:09](https://youtu.be/RUoG3SQOdAI?t=1989)

輸出阻抗：$r_{o2}\parallel r_{o4}$ 並 $C_4$。乘起來：

$$
A_d(s) = g_m(r_{o2}\parallel r_{o4})\cdot\frac{1 + s\frac{C_3}{2g_{m3}}}{\left(1 + s\frac{C_3}{g_{m3}}\right)\left(1 + sC_4(r_{o2}\parallel r_{o4})\right)}
$$

[▶ 34:40](https://youtu.be/RUoG3SQOdAI?t=2080)

數值（$r_{o2}\parallel r_{o4} = 50$ k、電容 pF）：主極點 $\frac{1}{C_4\cdot50\text{k}} = 2\times10^7$；電流鏡極點約 $2\times10^9$、零點 $4\times10^9$，很遠。[▶ 36:18](https://youtu.be/RUoG3SQOdAI?t=2178)

> 【課本補充】§10.7.2：電流鏡負載差動對有一個極零點對（pole-zero doublet）$f_P = g_{m3}/2\pi C_m$、$f_Z = 2f_P$，幾乎互相抵消；主極點由輸出節點 $C_L(R_o)$ 決定。

---

## 4. 第二級 CS：把右半平面零點移到無窮遠

[▶ 40:27](https://youtu.be/RUoG3SQOdAI?t=2427)

第二級 CS 才是真正嚴重的（Miller）。兩級合在一起，CS 的 $R_s$ 就是第一級的 $r_{o2}\parallel r_{o4}$，第一級輸出的 $C_4$ 和 CS 的 $C_{gs}$ 並在一起。[▶ 45:44](https://youtu.be/RUoG3SQOdAI?t=2744)

CS 有零點 $\frac{g_{m6}}{C_2}$（$C_2 = C_{gd}$）。**消掉它**：在 $C_2$ 串一顆電阻 $R$。令輸出 = 0，流過 $R$–$C_2$ 的電流 $\frac{v}{R + 1/sC_2}$ 要等於 $g_{m6}v$：[▶ 50:54](https://youtu.be/RUoG3SQOdAI?t=3054)

$$
s_z = \frac{1}{C_2\left(\frac{1}{g_{m6}} - R\right)}
\quad\Longrightarrow\quad
R = \frac{1}{g_{m6}}\ \text{時零點跑到無窮遠}
$$

$R$ 很小（$1/g_m$），不太影響其他東西。[▶ 52:58](https://youtu.be/RUoG3SQOdAI?t=3178)

> 【課本補充】§13.1.5 (p. 1002)：兩級 CMOS op amp 的 Miller 補償電容 $C_C$ 串一個電阻 $R$，令 $R = 1/g_{m6}$ 把傳輸零點移到無窮遠。

---

## 5. 兩級 op amp 的極點

**第一極點** [▶ 55:00](https://youtu.be/RUoG3SQOdAI?t=3300)：時間常數相加，Miller 那項主導：

$$
\frac{1}{\omega_{P1}} \approx C_2\left[R_s(1 + g_{m6}R_L) + R_L\right] + (C_1 + C_4)R_s + C_3R_L,
\quad R_s = r_{o2}\parallel r_{o4},\ R_L = r_{o6}\parallel r_{o7}
$$

$\omega_{P1} \approx 2\times10^5$（以前算過）。[▶ 58:38](https://youtu.be/RUoG3SQOdAI?t=3518)

**第二極點** [▶ 59:41](https://youtu.be/RUoG3SQOdAI?t=3581)：$C_2$ 短路後，閘汲接在一起，所有電容看 $\frac{1}{g_{m6}}$（並上很大的電阻）：

$$
\omega_{P2} \approx \frac{g_{m6}}{C_1 + C_3 + C_4}
\approx \frac{4\times10^{-3}}{3\times10^{-12}} \approx 1.3\times10^9
$$

[▶ 1:03:23](https://youtu.be/RUoG3SQOdAI?t=3803)

**整個 op amp**：第一級增益 × 第二級增益（共 $10^4$），乘上第一級的極零點對、第二級的兩個極點。畫起來：兩個極點（第一級主極點和第二級的第一極點）幾乎在一起，之後掉更陡，碰到零點稍緩。[▶ 1:08:01](https://youtu.be/RUoG3SQOdAI?t=4081)

---

## 6. 接回授後的震盪條件

[▶ 1:10:37](https://youtu.be/RUoG3SQOdAI?t=4237)

op amp 接回授：$\frac{v_o}{v_i} = \frac{A_d}{1 + \beta A_d}$。若分母 $1 + \beta A_d = 0$，沒有輸入也有輸出 → **震盪**：[▶ 1:15:56](https://youtu.be/RUoG3SQOdAI?t=4556)

$$
\beta A_d = -1:\quad
\left|\beta A_d\right| = 1,\quad \angle\beta A_d = -180^\circ
$$

（寫 −180° 不寫 +180°：高頻時相位是往下掉的。）$\beta$ 是純電阻，角度 0°，所以就是 $A_d$ 的角度到 −180°。[▶ 1:18:01](https://youtu.be/RUoG3SQOdAI?t=4681)

和「斷開迴路加測試信號」是同一件事：$\beta A_d = -V_r/V_t = -1$ 代表回來的信號和送出去的**同相、一樣大**——一度都不可以差。[▶ 1:22:09](https://youtu.be/RUoG3SQOdAI?t=4929)

【口頭】實際上一開始越震越大，到最後增益一定會飽和；這個數學式描述不出時間上的變化。[▶ 1:29:32](https://youtu.be/RUoG3SQOdAI?t=5372)

---

## 7. 數值例：三個極點

[▶ 1:27:58](https://youtu.be/RUoG3SQOdAI?t=5278)

$$
A_d(s) = \frac{10^4}{\left(1 + \frac{s}{10^5}\right)\left(1 + \frac{s}{10^6}\right)\left(1 + \frac{s}{10^7}\right)}
$$

**相位** [▶ 1:31:03](https://youtu.be/RUoG3SQOdAI?t=5463)：$-\tan^{-1}\frac{\omega}{10^5} - \tan^{-1}\frac{\omega}{10^6} - \tan^{-1}\frac{\omega}{10^7} = -180^\circ$。一個極點最多 −90°、兩個最多 −180°（在無窮遠）→ 一定在第二、第三極點之間；算出 $\omega_{180} \approx 3\times10^6$。增益在這裡從正轉為負。[▶ 1:35:42](https://youtu.be/RUoG3SQOdAI?t=5742)

**大小** [▶ 1:37:48](https://youtu.be/RUoG3SQOdAI?t=5868)：

$$
\left|A_d(\omega_{180})\right| = \frac{10^4}{\sqrt{1 + 30^2}\sqrt{1 + 3^2}\sqrt{1 + 0.3^2}} \approx \frac{10^4}{30\times3.2\times1.04} \approx 10^2
$$

不震的條件 $\beta\left|A_d\right| < 1$ → **$\beta < 1\%$**。接到 1%、或接近都不行。[▶ 1:39:49](https://youtu.be/RUoG3SQOdAI?t=5989)

---

## 8. 相位邊限 45°

[▶ 1:41:55](https://youtu.be/RUoG3SQOdAI?t=6115)

$\beta = 1\%$ 剛好站在懸崖邊（−180°、大小 1）。要留**寬裕程度**：讓 $|\beta A_d|$ 在相位 −135° 時就掉到 1，離 −180° 有 45°——**相位邊限**（phase margin）。[▶ 1:45:36](https://youtu.be/RUoG3SQOdAI?t=6336)

第二個極點處相位剛好約 −135°（−90° − 45°），所以讓 $|\beta A_d(\omega_{P2})| = 1$：[▶ 1:49:10](https://youtu.be/RUoG3SQOdAI?t=6550)

$$
\left|A_d(10^6)\right| = \frac{10^4}{\sqrt{1 + 10^2}\sqrt{2}\sqrt{1 + 0.1^2}} \approx 700
\quad\Longrightarrow\quad
\beta \approx \frac{1}{700}
$$

比 1% 更小。【口頭】也不要離太遠，回授的好處都靠 $1 + \beta A_d$。[▶ 1:46:36](https://youtu.be/RUoG3SQOdAI?t=6396)

---

## 9. 電壓隨耦器（β = 1）：主極點補償

[▶ 1:51:45](https://youtu.be/RUoG3SQOdAI?t=6705)

op amp 賣給別人，人家最常接成**電壓隨耦器**，$\beta = 1$——一定震。所以 op amp 必須設計到 $\beta = 1$ 也不震（相位邊限 45°）。[▶ 1:52:49](https://youtu.be/RUoG3SQOdAI?t=6769)

不能把 $A_d = 10^4$ 弄小（回授的好處都要 $1 + \beta A_d$）。辦法：**把第一個極點往內移**（畫一個很大的電容），讓增益提早掉。[▶ 1:54:56](https://youtu.be/RUoG3SQOdAI?t=6896)

- 往內移後，第二、第三極點和 $\omega_{180}$ 不動。[▶ 1:59:34](https://youtu.be/RUoG3SQOdAI?t=7174)
- 要在 $\omega_{P2} = 10^6$ 時 $|A_d| = 1$。只有一個極點的區域，**增益頻寬積**固定：[▶ 2:02:06](https://youtu.be/RUoG3SQOdAI?t=7326)

$$
A_0\,\omega_{P1}' = 1\times\omega_{P2}
\quad\Longrightarrow\quad
\omega_{P1}' = \frac{10^6}{10^4} = 10^2
$$

原本 $10^5$ → 要移到 $10^2$，差三個數量級 → 那個電容要畫成原來的 **1000 倍**。[▶ 2:04:41](https://youtu.be/RUoG3SQOdAI?t=7481)

【口頭】我們都操作在低頻，低頻還有 $10^4$ 的增益，所以沒關係。[▶ 2:07:17](https://youtu.be/RUoG3SQOdAI?t=7637)

> 【課本補充】§11.10 (p. 889)：主極點補償（dominant-pole compensation）——引入或下移一個極點，使 $|A\beta|$ 在下一個極點處降到 0 dB；Miller 補償則利用 Miller 效應用小電容達到大等效電容，同時把 $\omega_{P2}$ 推高（極點分離）。

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 例 |
|---|---|---|
| 鏡像極零點對 | 極點 $g_{m3}/C_3$、零點 $2g_{m3}/C_3$ | $2\times10^9$、$4\times10^9$ |
| 第一級 | $g_m(r_{o2}\parallel r_{o4})\cdot\frac{1+sC_3/2g_{m3}}{(1+sC_3/g_{m3})(1+sC_4R_o)}$ | 主極點 $2\times10^7$ |
| 消零點 | $C_{gd}$ 串 $R = 1/g_{m6}$ | 零點 → ∞ |
| op amp 第一極點 | Miller 主導 | $2\times10^5$ |
| op amp 第二極點 | $g_{m6}/(C_1+C_3+C_4)$ | $1.3\times10^9$ |
| 震盪 | $\beta A = -1$：大小 1、相位 −180° | |
| 三極點例 | $\omega_{180} \approx 3\times10^6$；$\lvert A\rvert \approx 100$ | $\beta < 1\%$ |
| 相位邊限 45° | $\lvert\beta A(\omega_{P2})\rvert = 1$ | $\beta \approx 1/700$ |
| β = 1 補償 | $\omega_{P1}' = \omega_{P2}/A_0$ | $10^2$，電容 ×1000 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 頻率補償 | 下一集：補償電容放哪、Miller 補償 |
| 極點分離 | op amp 設計 |
| 第十章 | 輸出級 |

---

## 附：本集一句話總結

> **電流鏡負載差動對的電流鏡節點只看到 $1/g_{m3}$，帶來一對很遠、幾乎抵消的極零點（零點是極點的兩倍），主極點在輸出節點 $C_4(r_{o2}\parallel r_{o4})$；第二級 CS 的右半平面零點可以在 $C_{gd}$ 串一顆 $1/g_{m6}$ 的電阻移到無窮遠，第一極點由 Miller 主導（$2\times10^5$）、第二極點約 $g_{m6}/\sum C$。接回授時 $\beta A = -1$ 就震：三極點例子 $\omega_{180} \approx 3\times10^6$、$|A| \approx 100$，$\beta$ 要小於 1%，留 45° 相位邊限更要約 1/700；要能接成 $\beta = 1$ 的電壓隨耦器，就把第一極點用大電容移到 $\omega_{P2}/A_0 = 10^2$（電容 1000 倍）。**

---

*筆記依據陳振芳老師「電子學（四）」112 學年度 Lec04 錄影逐字稿（whisper，2:08:08）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
