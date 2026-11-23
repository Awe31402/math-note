---
course: 電子學（三）前導課程（113 學年度）
episode: 04
lecture: Lec04 第五章 雙極性介面電晶體 BJT (4/5)
date: 113 學年度
video: https://www.youtube.com/watch?v=fo5khzpbwlM
notes: 老師第 5 章 = Sedra/Smith 7e Ch7；§7.3.3–7.3.6 共射、射極退化、共基、射極隨耦器 (p. 426–442)；§1.5 放大器模型；達靈頓 §13（輸出級）
---

# 第 04 集 · Lec04：BJT 四種組態（抓電壓還是抓電流）、電流鏡偏壓、功率放大、不用電容的差動輸出 [▶ 影片](https://www.youtube.com/watch?v=fo5khzpbwlM)

← 上一集：[03](03-bjt-saturation-bias-stability-emitter-resistor.md) ｜ [總目錄](../README.md) ｜ 下一集：[05](05-differential-amp-active-load-bjt-cascode.md) →

> **課程**：電子學（三）前導課程，陽明交大 電子物理系，113 學年度 — 第 04 集
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:58:32，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 以信號源為中心看放大器](#1-以信號源為中心看放大器)
- [2. 四種組態的 $R_{in}$、$R_{out}$](#2-四種組態的-r_inr_out)
- [3. BJT 電流鏡偏壓的共射極](#3-bjt-電流鏡偏壓的共射極)
- [4. 加 $R_E'$：抓電壓、增益穩定](#4-加-r_e抓電壓增益穩定)
- [5. 共基：電流隨耦器](#5-共基電流隨耦器)
- [6. 共集：電壓隨耦器與達靈頓](#6-共集電壓隨耦器與達靈頓)
- [7. 功率放大：共射 + 共集](#7-功率放大共射--共集)
- [8. 沒有放大器時的最大功率](#8-沒有放大器時的最大功率)
- [9. 拿掉電容：共射 + 共基共用電流源](#9-拿掉電容共射--共基共用電流源)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

和電子學（二）第 18–20 集 MOS 的內容平行，換成 BJT：四種接法各自「抓電壓還是抓電流、送出電壓還是電流」，用電流鏡偏壓組成完整電路，最後做功率放大和不用電容的差動輸出。

---

## 1. 以信號源為中心看放大器

[▶ 00:30](https://youtu.be/fo5khzpbwlM?t=30)

系統：信號源（內阻 $R_s$）→ 放大器 → 負載。

- **輸入端**：$R_i \gg R_s$ → 把 $v_s$ 全抓進來（grab voltage）；$R_i \ll R_s$ → 把電流 $i_s$ 全抓進來（grab current）。[▶ 01:36](https://youtu.be/fo5khzpbwlM?t=96)
- **輸出端**：從負載倒看回去，一定是電壓源串電阻或電流源並電阻。$R_{out}$ = 信號源拿掉後從輸出看回去的電阻。$R_{out} \approx 0$ → 理想電壓源；$R_{out} \to \infty$ → 理想電流源。[▶ 03:16](https://youtu.be/fo5khzpbwlM?t=196)

【口頭】「大、小」都是相對的：相對 $R_s$、相對負載。放大器把不理想的信號源**轉換**（transfer）成理想的電壓源或電流源。[▶ 09:00](https://youtu.be/fo5khzpbwlM?t=540)

---

## 2. 四種組態的 $R_{in}$、$R_{out}$

[▶ 11:04](https://youtu.be/fo5khzpbwlM?t=664)

| 組態 | $R_{in}$ | 抓 | $R_{out}$ | 送出 |
|---|---|---|---|---|
| 共射（CE） | $r_\pi$（2.5 k，不大不小） | 都不像 | ∞（不計 $r_o$） | 理想電流源 |
| 共射 + $R_E$ | $r_\pi + (1+\beta)R_E$（大） | 電壓 | ∞ | 理想電流源（轉導放大器） |
| 共基（CB） | $r_e = 1/g_m$（25 Ω，可更小） | 電流 | ∞ | 理想電流源（電流隨耦器） |
| 共集（CC） | $r_\pi + (1+\beta)R_L$（大） | 電壓 | $r_e + \frac{R_s}{1+\beta}$（小） | 理想電壓源（電壓隨耦器） |

- 共基：直流 1 mA → $r_e = 25\ \Omega$，10 mA → 2.5 Ω，100 mA → 0.25 Ω。[▶ 14:09](https://youtu.be/fo5khzpbwlM?t=849)
- 共射 $R_{out}$：信號源拿掉，$v_{be} = 0$，電流源 $g_mv = 0$ → 開路 → ∞（先不考慮 Early 效應 $r_o$）。[▶ 18:16](https://youtu.be/fo5khzpbwlM?t=1096)
- 共集 $R_{out}$：從射極加 $V_x$，基極電流 $I_x/(1+\beta)$ 流過 $R_s$ 和 $r_\pi$ → $R_{out} = \frac{r_\pi + R_s}{1+\beta} = r_e + \frac{R_s}{1+\beta}$；$\beta$ 大就很小。[▶ 24:09](https://youtu.be/fo5khzpbwlM?t=1449)

【口頭】沒有一個放大器全部通吃，要看信號源和負載來接。[▶ 28:49](https://youtu.be/fo5khzpbwlM?t=1729)

---

## 3. BJT 電流鏡偏壓的共射極

[▶ 29:51](https://youtu.be/fo5khzpbwlM?t=1791)

射極接定電流源（BJT 電流鏡），射極一定要接**大電容**到地，交流才有路走。[▶ 31:24](https://youtu.be/fo5khzpbwlM?t=1884)

**BJT 電流鏡** [▶ 32:26](https://youtu.be/fo5khzpbwlM?t=1946)：參考那顆基極接集極，$V_{BE} = 0.7$ V（電流差幾個數量級也還是約 0.7）。從 0 V 到 −10 V，1 mA → 參考電阻 9.3 kΩ。兩顆一樣（IC 裡做在一起很容易）→ 另一顆也是 1 mA。忽略基極電流（差 100 倍）。

**直流**：基極 0 V（經 $R_s$ 接信號源，直流 0）→ 射極 −0.7 V；$R_C = 5$ kΩ → 集極 5 V。可往上擺 5 V，往下到 $-0.7 + 0.2 = -0.5$ V，擺 5.5 V。電流鏡那顆集極 −0.7 V 遠在 −10 V 之上 → 主動區。[▶ 37:38](https://youtu.be/fo5khzpbwlM?t=2258)

**交流** [▶ 40:41](https://youtu.be/fo5khzpbwlM?t=2441)：

$$
\frac{v_o}{v_s} = -g_mR_C\frac{r_\pi}{R_s + r_\pi}
$$

【口頭】$g_m = I_C/V_T$ 由電流鏡固定的 1 mA 決定，不受 $\beta$ 影響；$\beta$ 只影響 $r_\pi$。[▶ 46:50](https://youtu.be/fo5khzpbwlM?t=2810)

輸出是理想電流源，所以接負載 $R_L$（要經電容，維持直流）時，若 $R_L \ll R_C$，增益變成 $-g_mR_L$，接喇叭就什麼都沒有。[▶ 43:46](https://youtu.be/fo5khzpbwlM?t=2626)

---

## 4. 加 $R_E'$：抓電壓、增益穩定

[▶ 49:59](https://youtu.be/fo5khzpbwlM?t=2999)

射極加一小段 $R_E' = 0.2$ kΩ（電容在它下面）→ $R_i = r_\pi + (1+\beta)R_E'$ 變大（例 22 k），可以假設 $R_i \gg R_s$，$v_s$ 全抓進來。[▶ 51:32](https://youtu.be/fo5khzpbwlM?t=3092)

$$
i_c \approx \frac{v_s}{r_e + R_E'} \approx \frac{v_s}{R_E'},
\qquad
\frac{v_o}{v_s} \approx -\frac{R_C}{R_E'} = -\frac{5}{0.2} = -25
$$

都是電阻，非常穩定。但 $R_E'$ 不要取太大，增益會掉——要取捨。[▶ 53:33](https://youtu.be/fo5khzpbwlM?t=3213)

---

## 5. 共基：電流隨耦器

[▶ 56:47](https://youtu.be/fo5khzpbwlM?t=3407)

基極接地，信號從射極進（經電容），射極底下是電流源。【口頭】要送到 LED、雷射時，輸出要的是電流（光和電流成正比）。[▶ 57:49](https://youtu.be/fo5khzpbwlM?t=3469)

- 電壓源輸入：$\dfrac{v_o}{v_s} = g_mR_C\dfrac{r_e}{R_s + r_e} \approx \dfrac{R_C}{R_s}$（$g_mr_e = 1$）。[▶ 1:00:24](https://youtu.be/fo5khzpbwlM?t=3624)
- 改用**電流源**輸入（光偵測器）：$r_e = 25\ \Omega \ll R_s$ → 電流全部流進射極、再從集極出來 → $i_o = i_s$，和 $R_s$ 無關。$R_{out} = \infty$。[▶ 1:02:31](https://youtu.be/fo5khzpbwlM?t=3751)

把不理想的電流源變成理想電流源（current follower）。要電壓就 $i_sR_C$，但負載不夠大還是會掉。[▶ 1:06:40](https://youtu.be/fo5khzpbwlM?t=4000)

---

## 6. 共集：電壓隨耦器與達靈頓

[▶ 1:08:44](https://youtu.be/fo5khzpbwlM?t=4124)

集極接 $V_{CC}$（交流地），信號進基極，射極輸出接電流源，再經電容到負載。

- $R_i = r_\pi + (1+\beta)R_L$ 大 → 抓電壓。[▶ 1:09:48](https://youtu.be/fo5khzpbwlM?t=4188)
- $v_o = v_s\dfrac{R_L}{r_e + R_L} \approx v_s$（要求 $r_e \ll R_L$）。[▶ 1:11:20](https://youtu.be/fo5khzpbwlM?t=4280)

**負載很小時**（喇叭 4 Ω、8 Ω）[▶ 1:12:56](https://youtu.be/fo5khzpbwlM?t=4376)：1 mA 的 $r_e = 25\ \Omega$ 比 4 Ω 大 → 把電流加到 100 mA，$r_e = 0.25\ \Omega$。另外 $(1+\beta)R_L$ 也要夠大：$R_L$ 很小時 $\beta = 100$ 也不夠，又買不到更大的 $\beta$ → 疊兩顆：**達靈頓**（Darlington），$\beta = \beta_1\beta_2$。[▶ 1:15:38](https://youtu.be/fo5khzpbwlM?t=4538)

$R_{out} = r_e + R_s/(1+\beta) \approx 0$ → 理想電壓源，增益 1。【口頭】這非常重要，等一下拿來用。[▶ 1:19:51](https://youtu.be/fo5khzpbwlM?t=4791)

---

## 7. 功率放大：共射 + 共集

[▶ 1:21:53](https://youtu.be/fo5khzpbwlM?t=4913)

正弦功率要對週期平均：$P = \frac12V_oI_o = \frac{V_o^2}{2R_L}$。要大功率，電壓要大、電流也要大 → $R_L$ 很小（幾 Ω）時電壓還要過得去。[▶ 1:23:30](https://youtu.be/fo5khzpbwlM?t=5010)

![共射級（R_C = 5 kΩ、射極 0.2 kΩ）直接推達靈頓射極隨耦器（β_1β_2），射極接電流源 I，輸出 v_O 推 R_L = 4 Ω 喇叭](../figures/E3-04-ce-darlington.svg)

- 第一級：共射 + $R_E' = 0.2$ k → 電壓放大 −25（前提：下一級輸入電阻 $\gg R_C$）。[▶ 1:26:36](https://youtu.be/fo5khzpbwlM?t=5196)
- 第二級：共集（達靈頓，$\beta_1\beta_2 = 10^4$）→ 輸入電阻夠大不負載第一級；$r_e$ 小於 4 Ω → 電壓不衰減送到喇叭。[▶ 1:29:40](https://youtu.be/fo5khzpbwlM?t=5380)

$$
P = \frac12\frac{(25v_s)^2}{R_L}
$$

【口頭】關鍵是最後的電壓隨耦器——直接接喇叭以前一定要接一個 voltage follower，保證電壓過得去，才有大電流。[▶ 1:34:49](https://youtu.be/fo5khzpbwlM?t=5689)

---

## 8. 沒有放大器時的最大功率

[▶ 1:37:52](https://youtu.be/fo5khzpbwlM?t=5872)

信號源（$v_s$、$R_s$）直接接 $R_L$：

$$
P = \frac12\left(\frac{v_sR_L}{R_s + R_L}\right)^2\frac{1}{R_L}
$$

$R_L$ 太大、太小都會變小；對 $R_L$ 微分 = 0 → **$R_L = R_s$** 時最大：$P_{\max} = \dfrac{v_s^2}{8R_s}$。[▶ 1:40:31](https://youtu.be/fo5khzpbwlM?t=6031)

例 $R_s = 1$ kΩ：就算匹配，功率也很小；和第 7 節（$625v_s^2/8$ 對 4 Ω）比差好幾個數量級。所以一定要有放大器。[▶ 1:42:04](https://youtu.be/fo5khzpbwlM?t=6124)

> 【課本補充】這就是**最大功率轉移定理**（maximum power transfer）。

---

## 9. 拿掉電容：共射 + 共基共用電流源

[▶ 1:44:11](https://youtu.be/fo5khzpbwlM?t=6251)

射極電容很大，IC 做不出來（面積就是錢）。共射的射極要一條交流的小電阻路徑——共基的射極正好是 $r_e$：把一顆共基接過來，兩個射極相接、共用 **2 mA** 電流源。[▶ 1:46:13](https://youtu.be/fo5khzpbwlM?t=6373)

- 直流：兩顆基極都 0 V → 射極都 −0.7 V，一樣 → 不需要電容；2 mA 一人一半。[▶ 1:48:49](https://youtu.be/fo5khzpbwlM?t=6529)
- 交流：$v_s$ 跨在兩個 $r_e$（各 25 Ω）上，一人一半 $v_s/2$。[▶ 1:51:57](https://youtu.be/fo5khzpbwlM?t=6717)

$$
v_{o1} = -\frac12g_mR_Cv_s,
\qquad
v_{o2} = +\frac12g_mR_Cv_s
$$

$g_m = 40$、$R_C = 5$ k → 各 ±100 倍。[▶ 1:55:05](https://youtu.be/fo5khzpbwlM?t=6905)

【口頭】好處：① 不需要大電容，對 IC 非常重要；② 得到一正一負的**互補**輸出，接到後面電路時會把一些不要的東西消掉。現在只有一端輸入，所以只拿到一半，下次再講。[▶ 1:56:40](https://youtu.be/fo5khzpbwlM?t=7000)

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 抓電壓 / 電流 | $R_i \gg R_s$ / $R_i \ll R_s$ | 相對信號源 |
| 理想電壓 / 電流源 | $R_{out} \to 0$ / $\infty$ | 相對負載 |
| CE | $R_i = r_\pi$，增益 $-g_mR_C\frac{r_\pi}{R_s + r_\pi}$ | |
| CE + $R_E'$ | $R_i = r_\pi + (1+\beta)R_E'$，增益 $\approx -R_C/R_E'$ | 例 −25 |
| CB | $R_i = r_e$，$i_o = i_s$ | 電流隨耦器 |
| CC | $R_i = r_\pi + (1+\beta)R_L$，$R_{out} = r_e + \frac{R_s}{1+\beta}$ | 電壓隨耦器 |
| 達靈頓 | $\beta = \beta_1\beta_2$ | 推小負載 |
| BJT 電流鏡 | 參考電阻 $= (V - 0.7)/I$ | 例 9.3 kΩ |
| 正弦功率 | $P = V_o^2/(2R_L)$ | |
| 最大功率轉移 | $R_L = R_s$，$P = v_s^2/(8R_s)$ | |
| CE + CB 共用尾電流 | 輸出 $\mp\frac12g_mR_Cv_s$ | 不用電容 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 共用尾電流源、互補輸出 | 下一集：差動放大器 |
| 電壓隨耦器推負載 | 輸出級（電子學（四）） |
| 四種放大器模型 | 回授的分類（電子學（四）） |

---

## 附：本集一句話總結

> **以信號源為中心看：$R_i$ 大抓電壓、小抓電流；$R_{out}$ 小送電壓、大送電流。共射（加 $R_E'$）抓電壓送電流、增益 $\approx -R_C/R_E'$；共基抓電流、變成理想電流源；共集（必要時用達靈頓）抓電壓、變成理想電壓源，讓 4 Ω 喇叭也拿得到電壓和功率；沒有放大器時最多只有 $v_s^2/(8R_s)$。把共射和共基的射極接在一起共用電流源，就不用大電容，還得到 $\mp\frac12g_mR_Cv_s$ 的互補輸出。**

---

*筆記依據陳振芳老師「電子學（三）前導課程」113 學年度 Lec04 錄影逐字稿（whisper，1:58:32）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
