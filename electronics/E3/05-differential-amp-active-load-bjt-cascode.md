---
course: 電子學（三）前導課程（113 學年度）
episode: 05
lecture: Lec05 第五章 雙極性介面電晶體 BJT (5/5)
date: 113 學年度
video: https://www.youtube.com/watch?v=cHLyWg2a74c
notes: 老師第 5 章最後一集 = Sedra/Smith 7e Ch8、Ch9；§9.2 BJT 差動對 (p. 614)、§8.3.1 電流源負載 (p. 525)、§8.5.6 BJT 疊接 (p. 557)
---

# 第 05 集 · Lec05：差動放大器、電流源負載（增益 2000）、輸出直流的控制、BJT 疊接（增益 20 萬） [▶ 影片](https://www.youtube.com/watch?v=cHLyWg2a74c)

← 上一集：[04](04-bjt-configurations-power-amplifier.md) ｜ [總目錄](../README.md) ｜ 下一集：[06](06-oscillator-conditions-rlc-transformer.md) →

> **課程**：電子學（三）前導課程，陽明交大 電子物理系，113 學年度 — 第 05 集
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:58:33，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 從共射 + 共基到差動放大器](#1-從共射--共基到差動放大器)
- [2. 輸入電阻 $2r_\pi$](#2-輸入電阻-2r_pi)
- [3. 兩個輸入：放大差值](#3-兩個輸入放大差值)
- [4. 負載接在兩個輸出之間](#4-負載接在兩個輸出之間)
- [5. 增益要更大：$R_C$ 做不大](#5-增益要更大r_c-做不大)
- [6. 電流源負載與 Early 電阻：增益 2000](#6-電流源負載與-early-電阻增益-2000)
- [7. 輸出直流控制不了，怎麼調](#7-輸出直流控制不了怎麼調)
- [8. 短路電流 × 輸出電阻與 BJT 疊接](#8-短路電流--輸出電阻與-bjt-疊接)
- [9. 疊接電流源負載：增益 20 萬](#9-疊接電流源負載增益-20-萬)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

把上一集「共射 + 共基共用電流源」正式變成**差動放大器**；接著用電流源負載和疊接把增益推到 op amp 等級（$10^5$），並面對輸出直流控制不了的問題。BJT（第 5 章）到這裡結束。

---

## 1. 從共射 + 共基到差動放大器

[▶ 00:00](https://youtu.be/cHLyWg2a74c?t=0)

（複習）射極隨耦器：$r_e = V_T/I$ 很小，電流越大越小 → 電壓全部過去，推小負載得到大功率。[▶ 01:33](https://youtu.be/cHLyWg2a74c?t=93)

共射的射極需要一條小電阻的交流路徑 → 接一顆共基（射極看進去就是 $r_e$），兩邊對稱：直流兩個射極都 −0.7 V，電容根本不需要；兩個 1 mA 電流源合成 2 mA。也可以讓右邊汲極也接 $R_C$（5 kΩ），兩邊直流都 5 V。[▶ 04:13](https://youtu.be/cHLyWg2a74c?t=253)

交流（小信號近似成立）：$v$ 跨在兩個 $r_e$ 上，一人一半：[▶ 09:27](https://youtu.be/cHLyWg2a74c?t=567)

$$
v_{o1} = 5 - \frac12g_mR_Cv,
\qquad
v_{o2} = 5 + \frac12g_mR_Cv
$$

一進兩出、互補輸出，沒有電容，適合 IC。[▶ 14:15](https://youtu.be/cHLyWg2a74c?t=855)

---

## 2. 輸入電阻 $2r_\pi$

[▶ 15:46](https://youtu.be/cHLyWg2a74c?t=946)

加入信號源內阻 $R_s$。左邊電晶體 $v_{be} = v/2$，基極電流 $= \frac{v/2}{r_\pi}$：

$$
R_i = \frac{v}{i_b} = 2r_\pi
$$

（1 mA、$\beta = 100$ → $r_\pi = 2.5$ k → $R_i = 5$ k。）增益多一個分壓：[▶ 19:59](https://youtu.be/cHLyWg2a74c?t=1199)

$$
\frac{v_{o}}{v_s} = \mp\frac12g_mR_C\cdot\frac{2r_\pi}{R_s + 2r_\pi}
$$

這個電路叫**差動放大器**（differential amplifier），後面非常重要：類比放大器的第一級通常就是它。[▶ 22:02](https://youtu.be/cHLyWg2a74c?t=1322)

---

## 3. 兩個輸入：放大差值

[▶ 22:35](https://youtu.be/cHLyWg2a74c?t=1355)

右邊基極也接一個輸入 $v_2$。用疊加，左邊射極電流往下、右邊就往上：

$$
v = \frac{v_1 - v_2}{2}\ \text{跨在每個}\ r_e,
\qquad
v_{o1} = 5 - \frac12g_mR_C(v_1 - v_2),
\quad
v_{o2} = 5 + \frac12g_mR_C(v_1 - v_2)
$$

**放大兩個輸入的差值**，前提是差值夠小（小信號）。例 $g_m = 40$、$R_C = 5$ k：$\frac12\times200 = 100$ 倍。[▶ 24:07](https://youtu.be/cHLyWg2a74c?t=1447)

> 【課本補充】§9.2 (p. 614)：BJT 差動對差模增益 $A_d = g_mR_C$（差動輸出）或 $\frac12g_mR_C$（單端輸出）；兩輸入相同的部分叫共模（common mode），理想上不被放大。

---

## 4. 負載接在兩個輸出之間

[▶ 27:45](https://youtu.be/cHLyWg2a74c?t=1665)

兩個輸出之間接 $R_L$：兩端一個上升、一個等量下降 → $R_L$ **中點**的交流電壓始終 0（交流地）。把 $R_L$ 拆成兩個 $\frac12R_L$、中點接地：[▶ 30:22](https://youtu.be/cHLyWg2a74c?t=1822)

$$
\text{每一邊的負載} = R_C \parallel \tfrac12R_L
$$

【口頭】這種增益一兩百、幾百，要怎麼用？接**回授電路**，特性就會變得很好。[▶ 33:24](https://youtu.be/cHLyWg2a74c?t=2004)

---

## 5. 增益要更大：$R_C$ 做不大

[▶ 34:26](https://youtu.be/cHLyWg2a74c?t=2066)

共射 $A_v = -g_mR_C$。$R_C$ 加大？直流 $V_{CE} = V_{CC} - I_CR_C$ 要 ≥ 0.2 V：$R_C$ 從 5 k 加到 10 k，$V_{CE} = 0$，跳出主動區。$R_C$ 頂多 6、7 k，沒什麼用。[▶ 38:35](https://youtu.be/cHLyWg2a74c?t=2315)

---

## 6. 電流源負載與 Early 電阻：增益 2000

[▶ 40:37](https://youtu.be/cHLyWg2a74c?t=2437)

負載換成**定電流源**（constant current load），放在頭上，用 PNP 電流鏡（10 V、參考電阻 9.3 k → 1 mA，忽略基極電流）。[▶ 41:38](https://youtu.be/cHLyWg2a74c?t=2498)

**Early 效應** [▶ 43:44](https://youtu.be/cHLyWg2a74c?t=2624)：BJT 也有，$I_C$-$V_{CE}$ 斜上去：$r_o = V_A/I_Q$，例 $V_A = 100$ V、1 mA → 100 kΩ。【口頭】100 kΩ 若用電阻做要拉很長，不划算；用一顆很小的 BJT 就有。[▶ 45:53](https://youtu.be/cHLyWg2a74c?t=2753)

交流：電流源開路，只剩兩顆的 $r_o$ 並聯：[▶ 49:27](https://youtu.be/cHLyWg2a74c?t=2967)

$$
A_v = -g_m(r_{on}\parallel r_{op}) = -40\times50 = -2000
$$

前面 5 k 時是 200，現在上千。還要再乘信號源和 $r_\pi$ 的分壓。

---

## 7. 輸出直流控制不了，怎麼調

[▶ 50:58](https://youtu.be/cHLyWg2a74c?t=3058)

交流增益沒問題，**直流**才是大問題。NPN 放大管的電流由基極分壓偏壓決定：$I_{QN} = \beta\left(\frac{V_{CC} - 0.7}{R_1} - \frac{0.7}{R_2}\right)$，$\beta$ 做出來以前根本不知道 → 不可控制（uncontrolled parameter）。[▶ 52:29](https://youtu.be/cHLyWg2a74c?t=3149)

疊加：[▶ 54:33](https://youtu.be/cHLyWg2a74c?t=3273)

$$
V_O = V_{CC}\frac{r_{on}}{r_{on} + r_{op}} + (I_{QP} - I_{QN})(r_{on}\parallel r_{op})
$$

例：$r_o$ 都 100 k，兩個電流差 10%（0.1 mA）→ $0.1\times50 = 5$ V，輸出從 5 V 跳到 10 V，不能放大。【口頭】IC 設計不能靠運氣。[▶ 58:46](https://youtu.be/cHLyWg2a74c?t=3526)

**調電流鏡電阻** [▶ 1:01:26](https://youtu.be/cHLyWg2a74c?t=3686)：$V_{CC} = V_{EB} + I_QR$，$R \to R + \Delta R$，小量乘小量丟掉、$\Delta V_{EB} = \Delta I_Q/g_m$：

$$
\Delta I_Q\left(\frac{1}{g_m} + R\right) = -I_Q\Delta R
\quad\Longrightarrow\quad
\frac{\Delta I_Q}{I_Q} \approx -\frac{\Delta R}{R}
$$

（$R = 9.3$ k ≫ $1/g_m$。）R 調幾 %，電流就變幾 %，調到兩個電流幾乎一樣，輸出回到 5 V。[▶ 1:07:41](https://youtu.be/cHLyWg2a74c?t=4061)

**感受一下** [▶ 1:09:44](https://youtu.be/cHLyWg2a74c?t=4184)：兩顆 $I_s$ 一樣、$V_{BE}$ 都剛好 0.7 V 才會都是 1 mA；要精準給到這種電壓根本不可能。輸入直流只要多 1 mV（當作小信號）：$\Delta V_O = -2000\times0.001 = -2$ V → 輸出從 5 V 變 3 V。[▶ 1:13:48](https://youtu.be/cHLyWg2a74c?t=4428)

【口頭】一定要能控制輸出電壓，IC 電路才做得出來。我們的目標是做一個增益很大的 IC 電路。[▶ 1:15:51](https://youtu.be/cHLyWg2a74c?t=4551)

---

## 8. 短路電流 × 輸出電阻與 BJT 疊接

[▶ 1:16:54](https://youtu.be/cHLyWg2a74c?t=4614)

**方法**（電子學（二）第 26 集）：$v_o = i_{sc}R_{out}$。$i_{sc}$：輸出短路；$R_{out}$：所有信號源設 0，倒看回去。驗算共射 + 理想電流源：$i_{sc} = -g_mv$、$R_{out} = r_o$。[▶ 1:22:11](https://youtu.be/cHLyWg2a74c?t=4931)

**BJT 疊接**（共射 $Q_1$ + 共基 $Q_2$）[▶ 1:24:45](https://youtu.be/cHLyWg2a74c?t=5085)：

- $i_{sc}$：$g_{m1}v$ 往上看 $Q_2$ 射極只有 $r_e = 25\ \Omega$，往旁邊是 $r_{o1} = 100$ k → 99% 往上 → $i_{sc} \approx -g_{m1}v$，一點都沒減少。[▶ 1:29:23](https://youtu.be/cHLyWg2a74c?t=5363)
- $R_{out}$（信號源拿掉，從輸出加 $V_x$）：$I_x$ 流進 $Q_2$ 射極節點，分到 $r_{\pi2}\parallel r_{o1}$ 上產生 $v = I_x(r_{\pi2}\parallel r_{o1})$；$Q_2$ 的電流源 $g_{m2}v$ 加上 $I_x$ 流過 $r_{o2}$：[▶ 1:36:40](https://youtu.be/cHLyWg2a74c?t=5800)

$$
R_{out} = (r_{\pi2}\parallel r_{o1})\left(1 + g_{m2}r_{o2}\right) + r_{o2}
\approx g_{m2}r_{\pi2}r_{o2} = \beta r_o
$$

（$r_{\pi2} = 2.5$ k ≪ $r_{o1}$，並聯得 $r_\pi$；$r_\pi = \beta/g_m$。）多一個 $\beta = 100$ 倍。[▶ 1:39:50](https://youtu.be/cHLyWg2a74c?t=5990)

**和 MOS 不同** [▶ 1:43:24](https://youtu.be/cHLyWg2a74c?t=6204)：再疊一顆，還是要和上面那顆的 $r_\pi$ 並聯，大不上去——BJT 疊接最多到 $\beta r_o$。MOS 閘極沒電流，可以一直疊、越疊越大。所以沒有人疊三顆 BJT。

> 【課本補充】Sedra §8.5.6 (p. 557)：BJT 疊接 $R_o \approx \beta r_o$ 是上限，因為 $r_\pi$ 有限；MOS 沒有這個限制。

---

## 9. 疊接電流源負載：增益 20 萬

[▶ 1:45:26](https://youtu.be/cHLyWg2a74c?t=6326)

放大管是疊接（$\beta r_o$），負載若只用一顆 PNP 電流源（$r_{op} = 100$ k），並聯後得小的——白做了。[▶ 1:47:27](https://youtu.be/cHLyWg2a74c?t=6447)

→ 上面也做成 **PNP 疊接電流源**：往上看也是 $\beta r_o$。（交流模型 NPN、PNP 一樣；所有直流源拿掉。）[▶ 1:48:27](https://youtu.be/cHLyWg2a74c?t=6507)

$$
A_v = -g_{m1}\left[(\beta r_o)\parallel(\beta r_o)\right] = -40\times\frac{100\times100\ \text{k}}{2} = -2\times10^5
$$

**20 萬倍**——這就是我們要的 op amp 等級增益。【口頭】疊接電路一定要用「短路電流 × $R_{out}$」來做才容易。[▶ 1:57:11](https://youtu.be/cHLyWg2a74c?t=7031)

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 差動放大器 | $v_{o1,2} = V \mp \frac12g_mR_C(v_1 - v_2)$ | 放大差值 |
| 輸入電阻 | $2r_\pi$ | |
| 負載跨兩輸出 | 每邊 $R_C\parallel\frac12R_L$ | 中點交流地 |
| $R_C$ 上限 | $V_{CE} \ge 0.2$ V | 增益做不大 |
| BJT $r_o$ | $V_A/I_Q$（100 V、1 mA → 100 k） | Early 效應 |
| 電流源負載 | $-g_m(r_{on}\parallel r_{op})$（−2000） | |
| 輸出直流 | $V_{CC}\frac{r_{on}}{r_{on}+r_{op}} + (I_{QP}-I_{QN})(r_{on}\parallel r_{op})$ | 差 10% → 5 V |
| 調整 | $\Delta I_Q/I_Q \approx -\Delta R/R$ | 電流鏡電阻 |
| BJT 疊接 $R_{out}$ | $\approx \beta r_o$ | 上限，不能再疊 |
| 疊接 + 疊接負載 | $-g_m(\beta r_o/2)$（$2\times10^5$） | op amp 等級 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 差動放大器 | 電子學（三）第 7 章、op amp 第一級 |
| 輸出直流 + 高增益 | 負回授（第 8 章） |
| 疊接 | 運算放大器內部 |

---

## 附：本集一句話總結

> **共射加共基、射極相接共用電流源就是差動放大器：輸入電阻 $2r_\pi$，兩個輸出 $V \mp \frac12g_mR_C(v_1 - v_2)$ 放大差值；$R_C$ 受直流限制做不大，改用電流源負載靠 Early 電阻得到 $-g_m(r_o\parallel r_o) = -2000$，但輸出直流隨電流不匹配亂跑，要靠調電流鏡電阻來修；再用 BJT 疊接（$R_{out} \approx \beta r_o$）配疊接電流源負載，增益達 20 萬，這就是 op amp 要的。**

---

*筆記依據陳振芳老師「電子學（三）前導課程」113 學年度 Lec05 錄影逐字稿（whisper，1:58:33）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
