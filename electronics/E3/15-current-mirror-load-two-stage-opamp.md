---
course: 電子學（三）（112 學年度）
episode: 15
lecture: Lec05 第七章 差動放大器 (5/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=8couFozn__4
notes: 老師第 7 章 = Sedra/Smith 7e Ch9、Ch13；§9.5 電流鏡負載差動放大器 (p. 644)、§13.1 兩級 CMOS op amp (p. 996)
---

# 第 15 集 · 112-Lec05：電流鏡負載的差動放大器（單端拿到全部增益）、共模增益、兩級 CMOS op amp 設計 [▶ 影片](https://www.youtube.com/watch?v=8couFozn__4)

← 上一集：[14](14-diff-amp-active-cascode-folded-large-signal.md) ｜ [總目錄](../README.md) ｜ 下一集：[16](16-opamp-feedback-offset-bjt-diff-amp.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 15 集（112 學年度 Lec05）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:02:56，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 直流：兩邊一定對稱](#1-直流兩邊一定對稱)
- [2. 交流：不對稱，二極體那邊電壓幾乎不動](#2-交流不對稱二極體那邊電壓幾乎不動)
- [3. 硬解：輸出 $= g_m(r_{o2}\parallel r_{o4})v_{id}$](#3-硬解輸出--g_mr_o2parallel-r_o4v_id)
- [4. 用短路電流 × 輸出電阻：簡單很多](#4-用短路電流--輸出電阻簡單很多)
- [5. 共模增益](#5-共模增益)
- [6. 輸入共模範圍](#6-輸入共模範圍)
- [7. 兩級 op amp：再接一級共源](#7-兩級-op-amp再接一級共源)
- [8. 佈局：$L$ 和 $W$ 怎麼定](#8-佈局l-和-w-怎麼定)
- [9. 增益一萬、輸出電阻、op amp 模型](#9-增益一萬輸出電阻op-amp-模型)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

把上一集開頭的**電流鏡負載**差動放大器算完整，然後在後面接一級共源，做出一個增益上萬的**兩級 CMOS op amp**，並把每顆 MOS 的 $W$、$L$ 定出來。

---

## 1. 直流：兩邊一定對稱

[▶ 00:32](https://youtu.be/8couFozn__4?t=32)

PMOS 電流鏡：左邊閘極接汲極（一定要拉這條線給它電壓），右邊閘極接同一點。尾電流 $I$。

假設兩邊電流一樣（各 $I/2$）：左邊 PMOS $V_{SG}$ 由 $I/2$ 決定；右邊 PMOS 閘極電壓一樣、電流一樣 → $V_{SG}$ 也一樣 → 兩個汲極電壓都是 $V_{DD} - V_{SG}$。假設 → 結果自洽，所以兩邊就是對稱。【口頭】這個電路根本就是 100% 對稱，Early 效應的那一點點不用管。$V_{SG} \approx 2$ V → 兩個汲極約 8 V。[▶ 06:16](https://youtu.be/8couFozn__4?t=376)

---

## 2. 交流：不對稱，二極體那邊電壓幾乎不動

[▶ 10:23](https://youtu.be/8couFozn__4?t=623)

加 $\pm\frac12v_{id}$。直流對稱，交流**不對稱**：左邊有一條線拉回閘極，右邊沒有，兩邊差很多——尾節點**不是 0**（右邊電壓很大，經 $r_o$ 下來會有電流）。[▶ 11:29](https://youtu.be/8couFozn__4?t=689)

**二極體接法那邊看進去** [▶ 14:07](https://youtu.be/8couFozn__4?t=847)：

$$
R = \frac{1}{g_m}\parallel r_o \approx \frac{1}{g_m}
$$

$g_mr_o \gg 1$（假設 200）→ $1/g_m$ 比 $r_o$ 小兩百倍 → 左邊下來的電流全部進二極體那顆，不會走自己的 $r_o$；在閘極產生的電壓讓右邊 PMOS **複製一樣的電流**。[▶ 18:45](https://youtu.be/8couFozn__4?t=1125)

---

## 3. 硬解：輸出 $= g_m(r_{o2}\parallel r_{o4})v_{id}$

[▶ 21:20](https://youtu.be/8couFozn__4?t=1280)

設尾節點電壓 $v$，兩顆 NMOS 的電流 $g_m(\frac12v_{id} - v)$、$g_m(-\frac12v_{id} - v)$；左邊的電流被鏡像到右邊，和右邊 NMOS 的電流在輸出節點相遇，差額流進輸出電阻。寫出每個節點的 KCL，消掉小項（$R_{SS} \ge r_o$，$v/R_{SS}$ 比其他小 $g_mr_o$ 倍）。[▶ 22:58](https://youtu.be/8couFozn__4?t=1378)

結果：$v \approx \frac14v_{id}$（輸入等級），而輸出是它的幾百倍；[▶ 42:00](https://youtu.be/8couFozn__4?t=2520)

$$
v_o = g_m\left(r_{o2}\parallel r_{o4}\right)v_{id}
$$

例 $g_m = 2$、$r_o = 100$ k：$2\times50 = 100$。【口頭】硬解滿難的，那麼多東西；不要所有東西都硬解。[▶ 26:40](https://youtu.be/8couFozn__4?t=1600)

---

## 4. 用短路電流 × 輸出電阻：簡單很多

[▶ 45:08](https://youtu.be/8couFozn__4?t=2708)

**短路電流**：輸出短路 → 輸出和二極體那邊都約 0 V（二極體那邊電阻小 100 倍以上）→ 兩邊又對稱了，尾節點是支點、可以接地。[▶ 48:10](https://youtu.be/8couFozn__4?t=2890)

- 左邊 $\frac12g_mv_{id}$ 進電流鏡，複製到右邊。
- 右邊 NMOS 的 $\frac12g_mv_{id}$（方向配合）。
- 兩個在輸出相加：

$$
i_{sc} = g_mv_{id}
$$

[▶ 51:18](https://youtu.be/8couFozn__4?t=3078)

**輸出電阻**（$v_{id} = 0$）[▶ 52:49](https://youtu.be/8couFozn__4?t=3169)：

- 往上：$r_{o4}$（電流鏡那顆的閘極電壓不動）。
- 往下：$Q_2$ 的源極接著「$Q_1$ 那邊看進去的小電阻」（$1/g_{m1}$ 並 $2R_{SS}$ 之類），套疊接公式：$r_{o2}(1 + g_{m2}\cdot\frac{1}{g_{m1}}) \approx 2r_{o2}$；再考慮電流鏡那條路分流，最後等效為 $r_{o2}$。[▶ 57:00](https://youtu.be/8couFozn__4?t=3420)

$$
R_{out} = r_{o2}\parallel r_{o4},
\qquad
A_d = g_m\left(r_{o2}\parallel r_{o4}\right)
$$

和硬解一樣。【口頭】寧願做兩次，但兩次都很簡單。

> 【課本補充】§9.5 (p. 644)：電流鏡負載把差動輸出轉成**單端輸出**，而且單端就拿到全部的差模增益 $G_mR_o = g_m(r_{o2}\parallel r_{o4})$（電阻負載單端只有一半）。

---

## 5. 共模增益

[▶ 1:05:19](https://youtu.be/8couFozn__4?t=3919)

兩邊加一樣的 $v_{cm}$，尾電阻拆成兩個 $2R_{SS}$。每邊電流 $i \approx \frac{v_{cm}}{2R_{SS}}$（很小）。左邊電流進二極體 → 鏡像到右邊 → 和右邊 NMOS 的電流幾乎**抵消**：[▶ 1:12:47](https://youtu.be/8couFozn__4?t=4367)

$$
A_{cm} \approx -\frac{1}{2g_{m3}R_{SS}}
$$

（$g_{m3}$ 是電流鏡 PMOS。）比電阻負載的 $-R_D/(2R_{SS})$ 還小很多。差模要越大、共模越小越好。[▶ 1:16:50](https://youtu.be/8couFozn__4?t=4610)

---

## 6. 輸入共模範圍

[▶ 1:18:22](https://youtu.be/8couFozn__4?t=4702)

±10 V，NMOS $k = 2$、各 1 mA（尾電流 2 mA，$k = 4$），PMOS $k = 2$；汲極約 8 V。

- Q1、Q2 飽和：$8 \ge V_{CM} - 1$ → $V_{CM} \le 9$ V。[▶ 1:21:29](https://youtu.be/8couFozn__4?t=4889)
- 尾電流管飽和：$V_{CM} - 2 \ge -8 - 1$ → $V_{CM} \ge -7$ V。

$$
-7\ \text{V} \le V_{CM} \le 9\ \text{V}
$$

包括 0，可以直接接。[▶ 1:24:04](https://youtu.be/8couFozn__4?t=5044)

---

## 7. 兩級 op amp：再接一級共源

[▶ 1:25:07](https://youtu.be/8couFozn__4?t=5107)

差動放大器（電流鏡負載）輸出接第二級**共源**：PMOS 放大管（源極 10 V，閘極接第一級輸出約 8 V → $V_{SG} = 2$ V），汲極接 NMOS 電流源負載（電流鏡，到 −10 V）。[▶ 1:26:39](https://youtu.be/8couFozn__4?t=5199)

- 所有 $V_{GS}$ 都設計約 2 V（比 $V_t$ 多一點）。【口頭】千萬不能讓某顆 $V_{GS}$ = 8 V，那早就跳出去了，變數位。[▶ 1:29:46](https://youtu.be/8couFozn__4?t=5386)
- 下面都是定電流源，都由同一個電流鏡複製出來。
- **第二級的電流要配好**：PMOS 放大管的電流（含 Early 多出來的）要等於底下電流源的電流，輸出才會在中間（0 V，因為上下是 ±10 V）；配不好輸出會掉到 −8 附近，跳出去。[▶ 1:32:52](https://youtu.be/8couFozn__4?t=5572)

---

## 8. 佈局：$L$ 和 $W$ 怎麼定

[▶ 1:35:01](https://youtu.be/8couFozn__4?t=5701)

（複習 Early 效應：$V_{DS}$ 大，夾止點往內縮，有效 $L$ 變短 → 電流斜上去；$V_A = V_A'L$，$V_A' = 5$ V/μm 是製程參數；$r_o = V_A/I_Q$。）[▶ 1:38:07](https://youtu.be/8couFozn__4?t=5887)

- **$L$**：全部取 20 μm → $V_A = 100$ V（for all）。1 mA → $r_o = 100$ k；2 mA → 50 k。[▶ 1:42:10](https://youtu.be/8couFozn__4?t=6130)
- **$W$**：$k = \mu C_{ox}W/L$；$\mu_nC_{ox} = 0.1$、$\mu_pC_{ox} = 0.1/3$ mA/V²（電洞慢約 3 倍）。[▶ 1:45:20](https://youtu.be/8couFozn__4?t=6320)

| 電晶體 | 電流 | 需要的 $k$ | $W/L$ |
|---|---|---|---|
| 輸入 NMOS（Q1、Q2） | 1 mA | 2 | 20 |
| 尾電流 NMOS | 2 mA | 4 | 40 |
| 電流鏡 PMOS（Q3、Q4） | 1 mA | 2 | 60 |
| 第二級 PMOS | 2 mA | 4 | 120 |

（第二級電流取 2 mA 為例。）長度都一樣，寬度不同——因為要讓 $V_{GS}$ 都差不多。[▶ 1:49:29](https://youtu.be/8couFozn__4?t=6569)

---

## 9. 增益一萬、輸出電阻、op amp 模型

[▶ 1:50:31](https://youtu.be/8couFozn__4?t=6631)

- 第一級：$g_m(r_{o2}\parallel r_{o4}) = 2\times50 = 100$。
- 第二級：$-g_{m6}(r_{o6}\parallel r_{o7})$；2 mA 時 $g_m$ 大、$r_o$ 小，乘起來也約 100。[▶ 1:53:36](https://youtu.be/8couFozn__4?t=6816)

$$
A_d \approx 100\times100 = 10^4
$$

輸入是兩端相減 $v_{id}$——**已經是一個 op amp**，增益上萬。[▶ 1:55:45](https://youtu.be/8couFozn__4?t=6945)

**輸出電阻** [▶ 1:57:53](https://youtu.be/8couFozn__4?t=7073)：信號源拿掉，第二級放大管電流 0、電流源也開路，看回去 $r_{o6}\parallel r_{o7} = 50\parallel50 = 25$ kΩ——很大。

**op amp 模型** [▶ 1:59:57](https://youtu.be/8couFozn__4?t=7197)：差動輸入 $v_{id}$、受控源 $A_dv_{id}$ 串 $R_{out}$。【口頭】op amp 的特色就是要你接**負回授**，增益大、輸出電阻大都沒關係。（PMOS 輸入、NMOS 電流鏡的版本完全對稱，分析一樣。）

> 【課本補充】§13.1 (p. 996)：兩級 CMOS op amp（Miller op amp）就是這個架構，另外需要**米勒補償電容**來保證接回授時穩定（電子學（四））。

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 直流 | 兩邊對稱，汲極 $V_{DD} - V_{SG}$ | 例 8 V |
| 二極體那邊 | $1/g_m\parallel r_o \approx 1/g_m$ | 抓電流、複製 |
| 短路電流 | $i_{sc} = g_mv_{id}$ | 短路後又對稱 |
| 輸出電阻 | $r_{o2}\parallel r_{o4}$ | |
| 差模增益（單端） | $g_m(r_{o2}\parallel r_{o4})$ | 例 100 |
| 共模增益 | $\approx -1/(2g_{m3}R_{SS})$ | 鏡像抵消 |
| ICMR | 例 −7～9 V | |
| 兩級 op amp | $A_d \approx g_{m1}(r_{o2}\parallel r_{o4})\cdot g_{m6}(r_{o6}\parallel r_{o7})$ | 例 $10^4$ |
| 佈局 | $L$ 全 20 μm（$V_A = 100$ V）；$W/L$ 由 $k$ 定 | PMOS 寬 3 倍 |
| 輸出電阻 | $r_{o6}\parallel r_{o7}$（例 25 k） | 接負回授 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 兩級 op amp | 下一集起：不匹配、偏移、BJT 版 |
| 輸出直流要配 | 系統偏移電壓 |
| 負回授 | 第 8 章 |

---

## 附：本集一句話總結

> **電流鏡負載的差動放大器直流完全對稱，交流卻不對稱：二極體那邊只有 $1/g_m$，把左邊電流抓進來複製到右邊，和右邊電流相加，用短路電流 × 輸出電阻算得 $i_{sc} = g_mv_{id}$、$R_{out} = r_{o2}\parallel r_{o4}$，單端就拿到全部增益 $g_m(r_{o2}\parallel r_{o4})$，共模增益只剩 $-1/(2g_{m3}R_{SS})$；後面再接一級共源就是增益上萬的兩級 CMOS op amp，$L$ 全取 20 μm、$W$ 依所需 $k$ 定，PMOS 要寬三倍。**

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec05 錄影逐字稿（whisper，2:02:56）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
