---
course: 電子學（三）（112 學年度）
episode: 16
lecture: Lec06 第七章 差動放大器 (6/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=6Atm6UlZqOg
notes: 老師第 7 章 = Sedra/Smith 7e Ch2、Ch9、Ch13；§2.3 非反相放大器、§9.4 直流偏移 (p. 637)、§9.2 BJT 差動對 (p. 614)、§8.5.6 BJT 疊接 (p. 557)
---

# 第 16 集 · 112-Lec06：兩級 op amp 接負回授、輸入直流與共模範圍、偏移電壓被回授壓掉、BJT 差動放大器與疊接 [▶ 影片](https://www.youtube.com/watch?v=6Atm6UlZqOg)

← 上一集：[15](15-current-mirror-load-two-stage-opamp.md) ｜ [總目錄](../README.md) ｜ 下一集：[17](17-bjt-mirror-load-base-current-offset.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 16 集（112 學年度 Lec06）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:04:23，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. op amp 模型：$A_d = 10^4$、$R_o = 25$ kΩ](#1-op-amp-模型a_d--104r_o--25-kω)
- [2. 接成非反相放大器](#2-接成非反相放大器)
- [3. 例：用齊納二極體做乾淨的直流電壓](#3-例用齊納二極體做乾淨的直流電壓)
- [4. 回授下小信號條件自動成立](#4-回授下小信號條件自動成立)
- [5. 輸入帶大直流：加電容、注意共模範圍](#5-輸入帶大直流加電容注意共模範圍)
- [6. 偏移電壓：開迴路飄 5 V，回授後幾乎沒了](#6-偏移電壓開迴路飄-5-v回授後幾乎沒了)
- [7. 5 V 單電源 op amp 的接法](#7-5-v-單電源-op-amp-的接法)
- [8. BJT 差動放大器](#8-bjt-差動放大器)
- [9. BJT 疊接：最多 $\beta r_o$](#9-bjt-疊接最多-beta-r_o)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

把上一集的兩級 CMOS op amp 拿來用：接負回授後增益、輸出電阻、偏移電壓都不是問題了。再看 BJT 版的差動放大器。

---

## 1. op amp 模型：$A_d = 10^4$、$R_o = 25$ kΩ

[▶ 00:32](https://youtu.be/6Atm6UlZqOg?t=32)

第一級 $g_m(r_{o2}\parallel r_{o4}) = 2\times50 = 100$；第二級 2 mA → $g_m = 4$、$r_o\parallel r_o = 25$ k → 100。總共 $A_d = 10^4$。[▶ 03:39](https://youtu.be/6Atm6UlZqOg?t=219)

輸出電阻：信號源拿掉，第二級兩顆都只剩 $r_o$ → $25$ kΩ。[▶ 07:13](https://youtu.be/6Atm6UlZqOg?t=433)

模型：差動輸入 → 受控源 $A_d(v_+ - v_-)$ 串 $R_o$。【口頭】這麼大一個電路，以後解題就換成這個模型。[▶ 09:49](https://youtu.be/6Atm6UlZqOg?t=589)

---

## 2. 接成非反相放大器

[▶ 10:21](https://youtu.be/6Atm6UlZqOg?t=621)

op amp 真的要用，一定接**負回授**。輸出經 $R_2$、$R_1$ 分壓回負端：$v_- = \beta v_o$，$\beta = \dfrac{R_1}{R_1 + R_2}$。【口頭】MOS 版比 BJT 好的地方：輸入端沒有電流。[▶ 13:30](https://youtu.be/6Atm6UlZqOg?t=810)

考慮 $R_o$：$R_o$ 上的壓降是「回授電流 × 25 k」，回授電流 $= v_-/R_1$。比起 $A_dv_-$（$10^4$ 倍），這一項只有 $\frac{25\ \text{k}}{R_1}$ 量級——除非 $R_1$ 放一兩 Ω（那電流大到根本供不起），否則可以忽略。[▶ 16:01](https://youtu.be/6Atm6UlZqOg?t=961)

$$
\frac{v_o}{v_+} = \frac{A_d}{1 + \beta A_d} \approx \frac1\beta = 1 + \frac{R_2}{R_1}
$$

$\beta$ 頂多幾分之一，$\beta A_d \gg 1$。增益完全由**電阻比**決定，$A_d$、$R_o$ 都消失了。[▶ 22:08](https://youtu.be/6Atm6UlZqOg?t=1328)

> 【課本補充】§2.3：非反相放大器閉迴路增益 $G = \frac{A}{1 + A\beta}$；$A$ 很大時 $G \approx 1/\beta$。

---

## 3. 例：用齊納二極體做乾淨的直流電壓

[▶ 25:17](https://youtu.be/6Atm6UlZqOg?t=1517)

整流濾波得到的直流很差（漣波、60 Hz 雜訊）。用崩潰二極體：2 V、崩潰後斜率倒數 1 Ω，串 1 kΩ → 雜訊只剩 1/1000。但如果直接拿分壓，雜訊和分壓比一起過來，沒用。[▶ 26:50](https://youtu.be/6Atm6UlZqOg?t=1610)

→ 2 V 接到 op amp 正端，增益 3（$\beta = 1/3$）：

$$
v_o = \frac{\beta A_d}{1 + \beta A_d}\cdot\frac1\beta\cdot2 \approx 6\ \text{V}
$$

不能超過 ±10 V（電源極限）。負端自己被回授拉到 2 V——兩端都是 2 V，**共模 2 V**，要在輸入共模範圍內（−7～9 V）。這就是為什麼要算 ICMR。[▶ 32:31](https://youtu.be/6Atm6UlZqOg?t=1951)

---

## 4. 回授下小信號條件自動成立

[▶ 35:05](https://youtu.be/6Atm6UlZqOg?t=2105)

差動對要線性，$\frac12v_{id} \le 0.2(V_{GS} - V_t)$。接回授後：

$$
v_{id} = v_+ - v_- = \frac{v_+}{1 + \beta A_d}
$$

例 2 V 輸入 → $v_{id} = 2/(1 + 10^4/3) \approx 0.6$ mV，遠小於 0.2 V，毫無問題。【口頭】接了回授，這個問題根本不是問題，1000% 自己滿足——這就是為什麼 op amp 增益要夠大。[▶ 39:15](https://youtu.be/6Atm6UlZqOg?t=2355)

---

## 5. 輸入帶大直流：加電容、注意共模範圍

[▶ 40:46](https://youtu.be/6Atm6UlZqOg?t=2446)

輸入是正弦但帶 4 V 直流，增益 3 → 輸出要 12 V，超過 10 V，op amp **飽和**，第二級跳出去。[▶ 43:53](https://youtu.be/6Atm6UlZqOg?t=2633)

改法：正端接一個電阻到地，信號經**電容**進來。電容充到 4 V 停止（穩態不再有電流），正端直流 0、只剩交流 $v_s$ → 輸出 $\frac1\beta v_s$。電容要對信號頻率短路。也要注意共模範圍（例 −7～9 V）。【口頭】直流很容易用電容砍掉，交流讓它過。[▶ 45:28](https://youtu.be/6Atm6UlZqOg?t=2728)

---

## 6. 偏移電壓：開迴路飄 5 V，回授後幾乎沒了

[▶ 50:39](https://youtu.be/6Atm6UlZqOg?t=3039)

以前不敢碰的問題：IC 廠做得再好，兩顆 MOS 不可能完全一樣。第二級放大管和電流源的電流只要差一點點（疊加：$\Delta I\times(r_o\parallel r_o)$），例如第一級輸出從 8 V 偏一點點 0.05 V、乘上第二級增益——**開迴路輸出直流就往上飄 5 V**。這叫**偏移**（offset）。[▶ 52:13](https://youtu.be/6Atm6UlZqOg?t=3133)

**接回授之後** [▶ 1:00:59](https://youtu.be/6Atm6UlZqOg?t=3659)：模型加一項輸出偏移 $V_{\text{off}}$：

$$
v_o = A_d(v_+ - \beta v_o) + V_{\text{off}}
\quad\Longrightarrow\quad
v_o = \frac{A_d}{1 + \beta A_d}v_+ + \frac{V_{\text{off}}}{1 + \beta A_d}
$$

5 V 的偏移被 $1 + \beta A_d$（三千多）除掉，剩幾 mV。【口頭】這就是為什麼我們做 op amp 都不算直流——接回授後這個問題不存在。[▶ 1:05:33](https://youtu.be/6Atm6UlZqOg?t=3933)

**等效看法** [▶ 1:08:37](https://youtu.be/6Atm6UlZqOg?t=4117)：把 $V_{\text{off}}/A_d$ 當成一個串在正端的小電壓源（**輸入偏移電壓** $V_{OS}$），op amp 本身就變成沒有偏移的理想 op amp。輸出偏移 $= V_{OS}/\beta$——很小。

> 【課本補充】§9.4 (p. 637)：輸入偏移電壓 $V_{OS}$ 來自 $R_D$、$W/L$、$V_t$ 的不匹配；把輸出偏移除以差模增益就是 $V_{OS}$。

---

## 7. 5 V 單電源 op amp 的接法

[▶ 1:16:51](https://youtu.be/6Atm6UlZqOg?t=4611)

±10 V 的 op amp 共模範圍包括 0；買 5 V / 0 V 的 op amp，共模範圍不包括 0 → 輸入一端接地、另一端接正弦（中心 0 V），共模就在範圍外，不能用。[▶ 1:18:54](https://youtu.be/6Atm6UlZqOg?t=4734)

改法 [▶ 1:20:25](https://youtu.be/6Atm6UlZqOg?t=4825)：

1. 正端用兩個電阻從 5 V 分壓出 **2.5 V**（不要買電池），信號經電容接進來 → 正端 = 2.5 V + $v_s$。
2. 若負端回授用 $R_1$ 直接接地，2.5 V 也會被放大（例 10 倍）→ 25 V，飽和。所以 $R_1$ 下面**串電容**：電容充到 2.5 V 後，直流增益變 1 → 輸出直流 2.5 V（正中間，最重要）；交流增益 $1 + R_2/R_1$。[▶ 1:21:25](https://youtu.be/6Atm6UlZqOg?t=4885)

輸出 $= 2.5\ \text{V} + \left(1 + \frac{R_2}{R_1}\right)v_s$，在中心點擺動。頻寬問題之後再講。[▶ 1:24:32](https://youtu.be/6Atm6UlZqOg?t=5072)

---

## 8. BJT 差動放大器

[▶ 1:25:32](https://youtu.be/6Atm6UlZqOg?t=5132)

兩顆 NPN 射極相接，尾電流 2 mA（BJT 電流鏡，電阻調出 2 mA），集極 5 kΩ 接 10 V。每顆 1 mA → $g_m = I_C/V_T = 40$ mA/V。[▶ 1:28:09](https://youtu.be/6Atm6UlZqOg?t=5289)

- 差模：$A_d = \frac12g_mR_C = \frac12\times40\times5 = 100$。共模：同 MOS，跨在 $R_{EE}$ 上，很小。[▶ 1:29:44](https://youtu.be/6Atm6UlZqOg?t=5384)
- **差模輸入電阻**（MOS 沒有的）：每邊 $v_{be} = \frac12v_{id}$，基極電流 $\frac{v_{id}/2}{r_\pi}$：[▶ 1:33:22](https://youtu.be/6Atm6UlZqOg?t=5602)

$$
R_{id} = 2r_\pi = 5\ \text{k}\Omega
$$

很小（MOS 是無窮大），之後接回授再看影響。

- **主動負載**（PNP 電流源）：$A_d = \frac12g_m(r_o\parallel r_o) = \frac12\times40\times50\ \text{k} = 1000$。[▶ 1:40:33](https://youtu.be/6Atm6UlZqOg?t=6033)
- **共模範圍**：要讓 $V_{CE} \ge 0.2$ V（主動區）；BJT 的 $V_{BE}$ 只有 0.7 V，範圍可以很接近電源。要兩邊都到軌，就再並一組 PNP 差動對（NPN、PNP 並在一起）。[▶ 1:42:34](https://youtu.be/6Atm6UlZqOg?t=6154)

> 【課本補充】§9.2.4：BJT 差動對 $R_{id} = 2r_\pi$；有射極電阻 $R_e$ 時 $R_{id} = (\beta+1)(2r_e + 2R_e)$。

---

## 9. BJT 疊接：最多 $\beta r_o$

[▶ 1:47:43](https://youtu.be/6Atm6UlZqOg?t=6463)

（複習）共基看進去 $r_e = 25\ \Omega$；疊接從頂端看下去：$I_x$ 流過 $r_\pi\parallel r_{o1}$（基極有 $r_\pi$ 會漏電流）…

$$
R_{out} = (r_{\pi2}\parallel r_{o1})(1 + g_{m2}r_{o2}) + r_{o2} \approx g_{m2}r_{\pi2}r_{o2} = \beta r_o
$$

[▶ 1:53:49](https://youtu.be/6Atm6UlZqOg?t=6829)

再疊一顆，上面那顆的 $r_\pi$ 又並聯進來，大不上去——【口頭】這是 BJT 和 MOS 很大的不同，MOS 可以一直疊。[▶ 1:57:27](https://youtu.be/6Atm6UlZqOg?t=7047)

**BJT 疊接差動放大器 + 疊接負載** [▶ 1:58:32](https://youtu.be/6Atm6UlZqOg?t=7112)：短路電流 $\frac12g_mv_{id}$ 全部出來（共基入口 $r_e$ 很小）；輸出電阻 $(\beta r_o)\parallel(\beta r_o)$：

$$
A_d = \frac12g_m\cdot\frac{\beta r_o}{2} = \frac12\times40\times\frac{100\times100\ \text{k}}{2} = 10^5
$$

[▶ 2:03:36](https://youtu.be/6Atm6UlZqOg?t=7416)

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| op amp 模型 | $A_d(v_+ - v_-)$ 串 $R_o$（例 $10^4$、25 k） | |
| 非反相 | $\frac{A_d}{1+\beta A_d} \approx 1 + \frac{R_2}{R_1}$ | $R_o$ 可忽略 |
| 回授下差模輸入 | $v_{id} = v_+/(1+\beta A_d)$ | 小信號自動成立 |
| 輸入大直流 | 電容 + 電阻到地 | 避免飽和、守 ICMR |
| 偏移 | 輸出偏移 ÷ $(1+\beta A_d)$；$V_{OS} = V_{\text{off}}/A_d$ | 回授壓掉 |
| 單電源 op amp | 正端墊 2.5 V；$R_1$ 串電容讓直流增益 1 | 輸出在中心 |
| BJT 差動 | $A_d = \frac12g_mR_C$（例 100）；$R_{id} = 2r_\pi$ | |
| BJT 主動負載 | $\frac12g_m(r_o\parallel r_o)$（例 1000） | |
| BJT 疊接 | $R_{out} \approx \beta r_o$，不能再疊 | |
| BJT 疊接差動 | $\frac14g_m\beta r_o$（例 $10^5$） | |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 負回授壓掉偏移 | 第 8 章負回授 |
| $R_{id}$、$R_o$ 的影響 | 回授對輸入、輸出電阻的改變 |
| 單電源偏壓 | 實際電路設計 |

---

## 附：本集一句話總結

> **兩級 op amp（$A_d = 10^4$、$R_o = 25$ k）接成非反相放大器後增益只剩 $1 + R_2/R_1$，$R_o$ 的影響可以忽略、差動輸入只剩 $v_+/(1+\beta A_d)$ 小信號自動成立；開迴路時不匹配讓輸出飄 5 V，接回授後被 $1+\beta A_d$ 除掉，等效為一個很小的輸入偏移 $V_{OS}$；輸入帶大直流要用電容隔開並守住共模範圍，5 V 單電源則把輸入墊到 2.5 V、回授電阻串電容。BJT 差動放大器增益 $\frac12g_mR_C$，但輸入電阻只有 $2r_\pi$，疊接最多到 $\beta r_o$，疊接差動放大器約 $10^5$。**

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec06 錄影逐字稿（whisper，2:04:23）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
