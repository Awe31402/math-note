---
course: 電子學（四）（112 學年度）
episode: 1
lecture: Lec01 第九章 放大器頻率響應 (1/5)
date: 112 學年度
video: https://www.youtube.com/watch?v=eDnJeI139DY
notes: 老師第 9 章 = Sedra/Smith 7e Ch10；§10.1 分立 CS/CE 放大器的低頻響應 (p. 699)、§10.1.2 短路時間常數法 (p. 707)、§10.2.1 MOSFET 內部電容 (p. 711)、§10.3.1 CS 高頻響應 (p. 722)、§10.3.3 Miller 定理 (p. 732)
---

# 第 1 集 · Lec01：RC 高通／低通、耦合電容與內部電容、三個頻段、短路時間常數法；兩級 op amp 的高頻與 Miller 效應 [▶ 影片](https://www.youtube.com/watch?v=eDnJeI139DY)

← 上一集：[E3-22](../E3/22-loop-gain-stability-phase-margin.md) ｜ [總目錄](../README.md) ｜ 下一集：[02](02-cs-two-poles-miller-source-follower-cd-cs.md) →

> **課程**：電子學（四），陽明交大 電子物理系，112 學年度 — 第 1 集（Lec01）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:05:08，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這學期要做什麼](#0-這學期要做什麼)
- [1. 串聯電容：高通](#1-串聯電容高通)
- [2. 耦合電容要多大](#2-耦合電容要多大)
- [3. 並聯小電容：低通](#3-並聯小電容低通)
- [4. 三個頻段：低頻、中頻、高頻](#4-三個頻段低頻中頻高頻)
- [5. 例：分立 CS 放大器的低頻響應](#5-例分立-cs-放大器的低頻響應)
- [6. 為什麼 3 dB ≈ 各極點相加](#6-為什麼-3-db--各極點相加)
- [7. 例：CE 放大器（電容耦在一起）](#7-例ce-放大器電容耦在一起)
- [8. 高頻：兩級 op amp 的第二級](#8-高頻兩級-op-amp-的第二級)
- [9. 只看 $C_{gd}$：Miller 效應](#9-只看-c_gdmiller-效應)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這學期要做什麼

[▶ 00:00](https://youtu.be/eDnJeI139DY?t=0)

電子學（四）：先講**放大器頻率響應**（第九章），再講怎麼做出大功率的**輸出級**（第十章）。【口頭】電子的應用太多，六學期也上不完。

---

## 1. 串聯電容：高通

[▶ 01:33](https://youtu.be/eDnJeI139DY?t=93)

信號源 $v_s$ 串 $R_1$、電容 $C$，負載 $R_2$。電容阻抗 $\frac{1}{sC}$，$s = j\omega$：

$$
\frac{v_o}{v_s} = \frac{R_2}{R_1 + R_2 + \frac{1}{sC}}
= \frac{R_2}{R_1 + R_2}\cdot\frac{s}{s + \frac{1}{(R_1 + R_2)C}}
$$

轉折頻率 $\omega_L = \dfrac{1}{(R_1 + R_2)C}$。[▶ 03:08](https://youtu.be/eDnJeI139DY?t=188)

- 低頻：電容**開路** → 輸出 0。
- 高頻：電容**短路** → 輸出 $\frac{R_2}{R_1 + R_2}$。[▶ 05:41](https://youtu.be/eDnJeI139DY?t=341)

**用看的求 RC** [▶ 06:42](https://youtu.be/eDnJeI139DY?t=402)：充電的 RC = 放電的 RC。信號源拿掉（短路），從電容兩端往外看的電阻：走一圈 $R_1$、$R_2$ 串聯 → $R = R_1 + R_2$。電路複雜時就這樣看，不要寫式子。

---

## 2. 耦合電容要多大

[▶ 08:45](https://youtu.be/eDnJeI139DY?t=525)

前一級電路可能有直流，要用電容**擋住**，不然放大器把直流也放大。這叫**耦合電容**（coupling capacitor）。

例：聲音最低 100 Hz（約 $10^2$），$R_1 + R_2 = 2$ kΩ。要讓轉折頻率比信號低：[▶ 10:50](https://youtu.be/eDnJeI139DY?t=650)

$$
\frac{1}{(2\times10^3)C} < 10^2
\quad\Longrightarrow\quad
C > 5\ \mu\text{F}
$$

（取 10 μF，轉折約 50。）【口頭】這麼大的水桶，AC 信號要對它充電其實很困難——所以信號直接過去。[▶ 12:22](https://youtu.be/eDnJeI139DY?t=742)

---

## 3. 並聯小電容：低通

[▶ 12:54](https://youtu.be/eDnJeI139DY?t=774)

電容改成**並在**負載上（很小，pF 等級）——這就是放大器裡的**內部電容**（internal capacitance）：氧化層是電容、PN 接面是電容。[▶ 13:56](https://youtu.be/eDnJeI139DY?t=836)

$$
\frac{v_o}{v_s} = \frac{R_2}{R_1 + R_2}\cdot\frac{1}{1 + s(R_1\parallel R_2)C}
$$

轉折 $\omega_H = \dfrac{1}{(R_1\parallel R_2)C}$。低頻可以過、高頻過不去（高頻電容短路）。例 1 k、1 k、1 pF → $\frac{1}{0.5\times10^3\times10^{-12}} = 2\times10^9$。[▶ 18:39](https://youtu.be/eDnJeI139DY?t=1119)

---

## 4. 三個頻段：低頻、中頻、高頻

[▶ 20:41](https://youtu.be/eDnJeI139DY?t=1241)

一個電路同時有耦合電容 $C_C$（大）和內部電容 $C_i$（小）。兩個一起寫數學會難很多，所以**分三個頻段**：[▶ 22:14](https://youtu.be/eDnJeI139DY?t=1334)

| 頻段 | $C_C$（大） | $C_i$（小） | 決定什麼 |
|---|---|---|---|
| 低頻 | 留著 | 開路 | $\omega_L$ |
| 中頻 | 短路 | 開路 | 中頻增益 $\frac{R_2}{R_1+R_2}$ |
| 高頻 | 短路 | 留著 | $\omega_H$ |

[▶ 25:48](https://youtu.be/eDnJeI139DY?t=1548)

【口頭】小電容是小水桶，充放電太容易，在低頻根本感受不到它；大電容是大水桶，在高頻充老半天都充不到電荷，兩頭沒有電壓 → 短路。[▶ 31:58](https://youtu.be/eDnJeI139DY?t=1918)

---

## 5. 例：分立 CS 放大器的低頻響應

[▶ 34:01](https://youtu.be/eDnJeI139DY?t=2041)

CS 放大器：輸入耦合電容 $C_1$（接 $R_G$ 給閘極偏壓）、源極電阻的旁路電容 $C_2$（讓 AC 信號直接到地，不然信號都跨在源極電阻上浪費掉）、輸出耦合電容 $C_3$ 接負載。都是 μF 以上。[▶ 36:33](https://youtu.be/eDnJeI139DY?t=2193)

（買來的分立 MOS 基底和源極接在一起。內部電容在低頻開路。）[▶ 40:10](https://youtu.be/eDnJeI139DY?t=2410)

MOS 閘極不吃電流，三個電容**不耦合**，可以個別算。信號源拿掉，從每個電容往外看：[▶ 42:46](https://youtu.be/eDnJeI139DY?t=2566)

$$
\omega_{P1} = \frac{1}{C_1(R_s + R_G)},
\qquad
\omega_{P2} = \frac{1}{C_2\left(R_S\parallel\frac{1}{g_m}\right)},
\qquad
\omega_{P3} = \frac{1}{C_3(R_D + R_L)}
$$

（源極往上看是 $1/g_m$。）[▶ 44:47](https://youtu.be/eDnJeI139DY?t=2687)

頻率圖：三個極點都在低頻，每碰到一個斜率再多 20 dB/dec。$1/g_m$ 很小 → $\omega_{P2}$ 通常最大。[▶ 48:22](https://youtu.be/eDnJeI139DY?t=2902)

**設計** [▶ 52:30](https://youtu.be/eDnJeI139DY?t=3150)：最低信號 $10^2$；$g_m = 2$ mA/V → $1/g_m = 500\ \Omega$；要 $\omega_{P2} < 10^2$ → $C_2$ 至少約 20 μF。旁路電容最重要、最大。

---

## 6. 為什麼 3 dB ≈ 各極點相加

[▶ 1:00:31](https://youtu.be/eDnJeI139DY?t=3631)

兩個低頻極點：$\left(\frac{s}{s + \omega_{P1}}\right)\left(\frac{s}{s + \omega_{P2}}\right)$。要它在 $\omega_L$ 等於單極點的 3 dB 值：

$$
\left(1 + \frac{\omega_{P1}^2}{\omega_L^2}\right)\left(1 + \frac{\omega_{P2}^2}{\omega_L^2}\right) = 2
$$

展開、丟掉 $\frac{\omega_{P1}^2\omega_{P2}^2}{\omega_L^4}$（極點差一個數量級以上時很小）→ [▶ 1:05:44](https://youtu.be/eDnJeI139DY?t=3944)

$$
\omega_L \approx \sqrt{\omega_{P1}^2 + \omega_{P2}^2 + \cdots} \approx \omega_{P1} + \omega_{P2} + \cdots
$$

不管幾個，3 dB 大概就是**所有個別 RC 倒數相加**（最大的那個占主導）。[▶ 1:07:17](https://youtu.be/eDnJeI139DY?t=4037)

> 【課本補充】§10.1.2 (p. 707)：**短路時間常數法**（short-circuit time constants）：$\omega_L \approx \sum_i \frac{1}{C_iR_i}$，$R_i$ 是其他電容**短路**時從 $C_i$ 看出去的電阻。

---

## 7. 例：CE 放大器（電容耦在一起）

[▶ 55:48](https://youtu.be/eDnJeI139DY?t=3348)

BJT 基極有電流，射極旁路電容和輸入耦合電容**耦在一起**，硬解數學很難。[▶ 59:00](https://youtu.be/eDnJeI139DY?t=3540)

辦法（approximation）：算某一個電容時，**其他電容短路**，一個一個求極點再相加。[▶ 1:08:24](https://youtu.be/eDnJeI139DY?t=4104)

- $C_1$：射極短路 → 基極看進去 $r_\pi$；$R = R_s + R_B\parallel r_\pi$。[▶ 1:10:02](https://youtu.be/eDnJeI139DY?t=4202)
- $C_E$：輸入短路 → 從射極看出去 $R_E\parallel\left[r_e + \frac{R_s\parallel R_B}{1+\beta}\right]$（基極電阻除 $1+\beta$）。[▶ 1:12:07](https://youtu.be/eDnJeI139DY?t=4327)
- $C_3$：$R_C + R_L$。[▶ 1:14:12](https://youtu.be/eDnJeI139DY?t=4452)

全部相加就是 $\omega_L$；射極那個電阻最小（除以 $1+\beta$，1 mA 時只有約 25 Ω）→ $C_E$ 要最大。[▶ 1:15:48](https://youtu.be/eDnJeI139DY?t=4548)

---

## 8. 高頻：兩級 op amp 的第二級

[▶ 1:17:51](https://youtu.be/eDnJeI139DY?t=4671)

重點在高頻——有時候真的要操作在很高頻。回到兩級 CMOS op amp：第一級差動（電流鏡負載）、第二級共源（電流源負載）。整個頻率響應決定在**共源那一級**。[▶ 1:22:08](https://youtu.be/eDnJeI139DY?t=4928)

（數值：第一級輸出電阻 $r_{o2}\parallel r_{o4} = 50$ k，當成第二級的 $R_s$；第二級 $g_m = 4$ mA/V、負載 $r_{o6}\parallel r_{o7} = 25$ k = $R_L$；兩級各 100 倍，共 $10^4$。）[▶ 1:24:15](https://youtu.be/eDnJeI139DY?t=5055)

**MOS 的內部電容** [▶ 1:28:21](https://youtu.be/eDnJeI139DY?t=5301)：$C_{gs}$、$C_{gd}$（氧化層），$C_{sb}$、$C_{db}$（PN 接面），一顆四個，pF 以下。IC 裡基底不和源極接：NMOS 基底接最負、PMOS 接最高。[▶ 1:30:53](https://youtu.be/eDnJeI139DY?t=5453)

兩端都是固定電壓（AC 地）的電容不充放電，拿掉。最後剩三個：[▶ 1:35:34](https://youtu.be/eDnJeI139DY?t=5734)

- $C_1 = C_{gs}$（輸入到地）。
- $C_3$：輸出到地（$C_{db}$ 等加在一起）。
- $C = C_{gd}$：**跨在輸入和輸出之間**。

**個別看** [▶ 1:43:51](https://youtu.be/eDnJeI139DY?t=6231)：

- 只有 $C_1$：$\omega = \frac{1}{R_sC_1} = \frac{1}{50\text{k}\times1\text{p}} = 2\times10^7$。
- 只有 $C_3$：$\omega = \frac{1}{R_LC_3} = 4\times10^7$。

---

## 9. 只看 $C_{gd}$：Miller 效應

[▶ 1:47:10](https://youtu.be/eDnJeI139DY?t=6430)

$C_{gd}$ 用看的看不出來，要算：從電容兩端加 $V_x$。電流 $I_x$ 在 $R_s$ 上產生 $I_xR_s$，跨到閘極再乘 $g_m$，變成很大的電流流過 $R_L$：[▶ 1:48:15](https://youtu.be/eDnJeI139DY?t=6495)

$$
R_x = R_s + R_L + g_mR_LR_s \approx R_s(1 + g_mR_L)
$$

$g_mR_L = 4\times25 = 100$：

$$
\omega_P = \frac{1}{C_{gd}R_s(1 + g_mR_L)} = \frac{1}{10^{-12}\times50\text{k}\times101} \approx 2\times10^5
$$

比 $C_1$ 單獨的 $2\times10^7$ **低了一百倍**——很不好，操作頻率稍微高一點就完了。電容等於被放大了 $(1 + g_mR_L)$ 倍——叫 **Miller 效應**（Miller 是人名）。原因是這一級在放大。[▶ 1:52:57](https://youtu.be/eDnJeI139DY?t=6777)

**還有一個零點** [▶ 1:54:35](https://youtu.be/eDnJeI139DY?t=6875)：$C_{gd}$ 讓輸入直接漏到輸出。令輸出 $v_o = 0$：流過 $C_{gd}$ 的電流 $= sC_{gd}v_{gs}$ 要等於 $g_mv_{gs}$ →

$$
s_z = \frac{g_m}{C_{gd}} = \frac{4\times10^{-3}}{10^{-12}} = 4\times10^9
$$

（右半平面零點）。碰到零點會往上 20 dB/dec，所以高頻不會降到 0：在很高頻 $C_{gd}$ 短路，輸出被輸入直接拉著。[▶ 2:01:50](https://youtu.be/eDnJeI139DY?t=7310)

【口頭】整個問題出在這個電容。輸入、輸出反相，電容兩端電壓差變得很大，要的電荷就很多很多——這就是 Miller 效應。下次講怎麼處理。[▶ 2:03:56](https://youtu.be/eDnJeI139DY?t=7436)

> 【課本補充】§10.3.3 (p. 732)：Miller 定理——跨接阻抗 $Z$、增益 $K$，可換成輸入端 $Z/(1-K)$、輸出端 $Z/(1-1/K)$；跨接電容等效為輸入端 $C(1 + g_mR_L')$。

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 串聯 $C$（高通） | $\omega_L = \frac{1}{(R_1+R_2)C}$ | 低頻開路 |
| 並聯 $C$（低通） | $\omega_H = \frac{1}{(R_1\parallel R_2)C}$ | 高頻短路 |
| 求 RC | 信號源拿掉，從電容看出去的電阻 | 用看的 |
| 三頻段 | 低頻 $C_i$ 開、中頻都簡化、高頻 $C_C$ 短 | |
| 耦合電容 | 例 $C > 5\ \mu$F | 擋直流 |
| CS 低頻 | $\omega_{P2} = \frac{1}{C_2(R_S\parallel 1/g_m)}$ 最大 | 旁路電容最大 |
| 3 dB 估計 | $\omega_L \approx \sum \omega_{Pi}$ | 其他電容短路 |
| CE 射極 | $R_E\parallel[r_e + \frac{R_s\parallel R_B}{1+\beta}]$ | |
| Miller | $R_x \approx R_s(1 + g_mR_L)$；$\omega_P = \frac{1}{C_{gd}R_s(1+g_mR_L)}$ | 低一百倍 |
| 零點 | $s_z = g_m/C_{gd}$ | 高頻不降到 0 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Miller 效應 | 下一集：三個電容一起解、開路時間常數 |
| 零點 | 高頻響應完整式 |
| 疊接 | 用疊接打掉 Miller 效應 |

---

## 附：本集一句話總結

> **串聯的大耦合電容造成低頻轉折 $\frac{1}{(R_1+R_2)C}$、並聯的小內部電容造成高頻轉折 $\frac{1}{(R_1\parallel R_2)C}$，所以把頻率分成低、中、高三段分開算；低頻 3 dB 約等於「其他電容短路」下各個 RC 倒數相加，CS 的源極旁路電容最關鍵；到了高頻，兩級 op amp 的共源級裡跨在閘汲之間的 $C_{gd}$ 被放大 $(1+g_mR_L)$ 倍（Miller 效應），極點從 $2\times10^7$ 掉到 $2\times10^5$，還帶來一個 $g_m/C_{gd}$ 的零點。**

---

*筆記依據陳振芳老師「電子學（四）」112 學年度 Lec01 錄影逐字稿（whisper，2:05:08）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
