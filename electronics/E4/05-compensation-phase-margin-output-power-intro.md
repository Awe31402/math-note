---
course: 電子學（四）（112 學年度）
episode: 5
lecture: Lec05 第九章 放大器頻率響應 (5/5) ＋ 第十章 高功率輸出級 (1/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=UvUpOBgrix0
notes: 老師第 9 章 = Sedra/Smith 7e Ch10–11；第 10 章 = Ch12。§11.9 波德圖看穩定度 (p. 885)、§11.10 頻率補償 (p. 889)、§12.1 輸出級分類 (p. 922)、§12.2 A 類輸出級 (p. 923)
---

# 第 5 集 · Lec05：主極點補償複習、兩級 op amp 實際算相位邊限（20° → 45°）；第十章開始：負載功率、阻抗匹配、射極隨耦器讓功率變大 [▶ 影片](https://www.youtube.com/watch?v=UvUpOBgrix0)

← 上一集：[04](04-mirror-load-doublet-opamp-poles-compensation.md) ｜ [總目錄](../README.md) ｜ 下一集：[06](06-follower-loading-class-a-b-ab-protection.md) →

> **課程**：電子學（四），陽明交大 電子物理系，112 學年度 — 第 5 集（Lec05）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:50:05，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：震盪條件與三極點例](#1-複習震盪條件與三極點例)
- [2. 主極點補償，更精確一點](#2-主極點補償更精確一點)
- [3. 實際的兩級 op amp：永遠穩定？](#3-實際的兩級-op-amp永遠穩定)
- [4. 相位邊限只有 20°：Miller 電容加倍](#4-相位邊限只有-20miller-電容加倍)
- [5. 第十章：負載上的功率](#5-第十章負載上的功率)
- [6. 共射放大器能給多少功率：阻抗匹配](#6-共射放大器能給多少功率阻抗匹配)
- [7. 加射極隨耦器：輸出電阻除 $(1+\beta)$](#7-加射極隨耦器輸出電阻除-1beta)
- [8. 不要匹配，要 $R_{out} \ll R_L$](#8-不要匹配要-r_out--r_l)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

把頻率補償收尾：用真實的兩級 op amp 數字算相位邊限。然後進第十章**高功率輸出級**：怎麼讓負載（喇叭）拿到大功率。

---

## 1. 複習：震盪條件與三極點例

[▶ 00:30](https://youtu.be/UvUpOBgrix0?t=30)

回授 $\frac{A_d}{1 + \beta A_d}$；拿掉輸入還有輸出 → $\beta A_d = -1$。一般電路：斷開迴路加測試信號，回來的 $-V_r/V_t = 1$，同一件事。兩個條件：[▶ 05:12](https://youtu.be/UvUpOBgrix0?t=312)

1. 相位 $\angle A_d = -180^\circ$（$\beta$ 是電阻，沒有角度）→ 找出震盪頻率（通常只有一個）。
2. 在那個頻率 $|\beta A_d| \ge 1$。

例 $A_d = \frac{10^4}{(1 + s/10^5)(1 + s/10^6)(1 + s/10^7)}$：$\omega_{180} \approx 3\times10^6$，$|A_d| \approx 10^2$ → $\beta < 1\%$，$\beta$ 越大越危險。[▶ 13:31](https://youtu.be/UvUpOBgrix0?t=811)

相位邊限 45°：在第二個極點（−135°）讓 $\beta|A_d| = 1$ → $\beta = \frac{\sqrt2}{10^3}$。[▶ 21:24](https://youtu.be/UvUpOBgrix0?t=1284)

---

## 2. 主極點補償，更精確一點

[▶ 22:58](https://youtu.be/UvUpOBgrix0?t=1378)

op amp 要能接成 $\beta = 1$（人家接成電壓隨耦器都不能震）。不能把低頻 $A$ 弄小，所以**把第一個極點往內移**。後面的極點和 $\omega_{180}$ 都不變。[▶ 25:01](https://youtu.be/UvUpOBgrix0?t=1501)

要在 $\omega_{P2} = 10^6$ 時 $|A_d| = 1$。新的第一極點 $\omega_{P1}' \ll \omega_{P2}$：[▶ 30:15](https://youtu.be/UvUpOBgrix0?t=1815)

$$
\frac{10^4}{\frac{\omega_{P2}}{\omega_{P1}'}\cdot\sqrt2\cdot\sqrt{1 + 0.01}} = 1
\quad\Longrightarrow\quad
\omega_{P1}' \approx \frac{\sqrt2\,\omega_{P2}}{10^4}
$$

上次忽略了 $\sqrt2$。概念上：**新的第一極點 × 低頻增益 ≈ 原來的第二極點**（−20 dB/dec 一直掉，剛好在第二極點掉光）。從 $10^5$ 移到約 $10^2$。[▶ 33:28](https://youtu.be/UvUpOBgrix0?t=2008)

三個電容中有一個最嚴重（給 $10^5$ 那個），IC 設計時在那裡多畫一個大電容。【口頭】增益越大越容易震——所以第一個最重要的電容一定要大，這叫頻率補償（frequency compensation）。[▶ 40:38](https://youtu.be/UvUpOBgrix0?t=2438)

---

## 3. 實際的兩級 op amp：永遠穩定？

[▶ 42:43](https://youtu.be/UvUpOBgrix0?t=2563)

我們的 CMOS op amp：低頻 $10^4$；第一極點 $2\times10^5$（Miller 造成，通常希望頻寬至少 $10^7$）；第二極點 $2\times10^9$；第一級的極零點對、第二級的右半平面零點（串 $1/g_{m6}$ 移到無窮遠）都忽略。第一級的主極點也在 $2\times10^9$ 附近 → 兩個極點重疊：[▶ 46:25](https://youtu.be/UvUpOBgrix0?t=2785)

$$
A_d(s) \approx \frac{10^4}{\left(1 + \frac{s}{2\times10^5}\right)\left(1 + \frac{s}{2\times10^9}\right)^2}
$$

**震盪頻率** [▶ 49:00](https://youtu.be/UvUpOBgrix0?t=2940)：第一極點貢獻約 −90°，剩下 90° 由重疊的兩個極點各 45° → $\omega_{180} = 2\times10^9$（就在第二極點）。

**大小** [▶ 52:08](https://youtu.be/UvUpOBgrix0?t=3128)：

$$
\left|A_d(2\times10^9)\right| \approx \frac{10^4}{10^4\cdot\sqrt2\cdot\sqrt2} = \frac12
$$

$\beta \le 1$ 時 $\beta|A_d| \le \frac12 < 1$ → **always stable**。【口頭】當初設計時雖沒從頻率去算，已經設計好了。[▶ 54:41](https://youtu.be/UvUpOBgrix0?t=3281)

---

## 4. 相位邊限只有 20°：Miller 電容加倍

[▶ 55:13](https://youtu.be/UvUpOBgrix0?t=3313)

穩定還不夠，要**夠安全**。$\beta = 1$ 時，找 $|A_d| = 1$ 的頻率，看相位離 −180° 多少：[▶ 57:50](https://youtu.be/UvUpOBgrix0?t=3470)

- 解 $|A_d(\omega)| = 1$ 要電腦算，約在 $10^9$ 量級；相位約 −160°。
- **相位邊限只有 20°**，稍微危險。【口頭】很多 IC 設計不能太靠近。[▶ 1:00:23](https://youtu.be/UvUpOBgrix0?t=3623)

**移到 45°** [▶ 1:01:25](https://youtu.be/UvUpOBgrix0?t=3685)：要相位 −135° 時 $|A_d| = 1$。第一極點 −90°，剩 45° 由兩個重疊極點各分 **22.5°**：

$$
\tan^{-1}\frac{\omega}{2\times10^9} = 22.5^\circ
\quad\Longrightarrow\quad
\omega \approx 0.8\times10^9
$$

在這個頻率要 $|A_d| = 1$：[▶ 1:05:38](https://youtu.be/UvUpOBgrix0?t=3938)

$$
\frac{10^4\,\omega_{P1}'}{0.8\times10^9}\cdot\frac{1}{1.16} \approx 1
\quad\Longrightarrow\quad
\omega_{P1}' \approx 10^5
$$

原本 $2\times10^5$ → 移到 $10^5$。這個極點就是 Miller 效應那顆電容造成的 → **把那顆電容畫成兩倍**，極點就減半。[▶ 1:08:48](https://youtu.be/UvUpOBgrix0?t=4128)

【口頭】做完要 check 頻率補償，一定要。沒做就一定死、不能用——op amp 就是要做回授用的。[▶ 1:11:21](https://youtu.be/UvUpOBgrix0?t=4281)

---

## 5. 第十章：負載上的功率

[▶ 1:12:55](https://youtu.be/UvUpOBgrix0?t=4375)

以前很少提 power。輸出 $v_o = V_o\sin\omega t$、$i_o = I_o\sin\omega t$，瞬時功率相乘有 $\sin^2\omega t = \frac12(1 - \cos2\omega t)$，對週期平均，cos 項積分為 0：[▶ 1:15:01](https://youtu.be/UvUpOBgrix0?t=4501)

$$
P_L = \frac12V_oI_o = \frac{V_o^2}{2R_L}
$$

$V_o$、$I_o$ 是**振幅**。$R_L$ 弄小功率就大——但不能讓 $V_o$ 也跟著變小，那就沒用了。[▶ 1:16:35](https://youtu.be/UvUpOBgrix0?t=4595)

---

## 6. 共射放大器能給多少功率：阻抗匹配

[▶ 1:17:07](https://youtu.be/UvUpOBgrix0?t=4627)

共射放大器，$V_{CC} = 10$ V、$R_C = 5$ k，偏壓讓集極在 5 V → 最大擺幅（full swing）5 V。[▶ 1:17:39](https://youtu.be/UvUpOBgrix0?t=4659)

畫 Thevenin 等效 [▶ 1:19:44](https://youtu.be/UvUpOBgrix0?t=4784)：

- 開路電壓 $v_{open} = -g_mv_sR_C$，最大只能到 5 V（信號再大也沒用）。[▶ 1:21:48](https://youtu.be/UvUpOBgrix0?t=4908)
- 輸出電阻：信號拿掉 → $R_{out} = R_C$。[▶ 1:22:19](https://youtu.be/UvUpOBgrix0?t=4939)

接 $R_L$：$P_L = \frac12\left(\frac{V_{open}R_L}{R_{out} + R_L}\right)^2\frac{1}{R_L}$。$R_L \to 0$ 或 $\infty$ 都是 0，中間有最大值。微分 = 0：[▶ 1:26:04](https://youtu.be/UvUpOBgrix0?t=5164)

$$
R_L = R_{out}
\quad\Longrightarrow\quad
P_{L,\max} = \frac{V_{open}^2}{8R_{out}}
$$

叫**阻抗匹配**（resistance matching）。例 $\frac{5^2}{8\times5\text{k}} \approx 0.6$ mW——很小。[▶ 1:28:39](https://youtu.be/UvUpOBgrix0?t=5319)

【口頭】共射增益可以很大（$g_m$ 很大），但 $R_L$ 一小就和 $R_C$ 並聯，$v_o$ 沒了。[▶ 1:29:42](https://youtu.be/UvUpOBgrix0?t=5382)

---

## 7. 加射極隨耦器：輸出電阻除 $(1+\beta)$

[▶ 1:31:17](https://youtu.be/UvUpOBgrix0?t=5477)

共射後面接一顆射極隨耦器（集極接最高電壓，射極接電流源）。

- 開路電壓不變：$v_{open} = -g_mv_sR_C$（隨耦器增益約 1，基極幾乎沒電流）。[▶ 1:33:56](https://youtu.be/UvUpOBgrix0?t=5636)
- 輸出電阻：$R_C$ 在基極，從射極看要除 $(1+\beta)$，再加 $r_e$：[▶ 1:35:29](https://youtu.be/UvUpOBgrix0?t=5729)

$$
R_{out} = \frac{R_C}{1 + \beta} + r_e,
\qquad
r_e = \frac{V_T}{I_E} = \frac{25\ \text{mV}}{10\ \text{mA}} = 2.5\ \Omega
$$

直流電流取大一點（10 mA）：【口頭】AC 信號要大，直流電流也要跟著大。[▶ 1:38:05](https://youtu.be/UvUpOBgrix0?t=5885)

匹配時 $P_{\max} = \frac{V_{open}^2}{8R_{out}}$，$R_{out}$ 小了約 100 倍 → **功率多約 100 倍**。[▶ 1:41:40](https://youtu.be/UvUpOBgrix0?t=6100)

---

## 8. 不要匹配，要 $R_{out} \ll R_L$

[▶ 1:43:42](https://youtu.be/UvUpOBgrix0?t=6222)

為了匹配去配電阻有點怪、不 practical。$R_L$（喇叭）是固定的，應該設計 $R_{out} = \frac{R_C}{1 + \beta} + r_e \ll R_L$，那麼 $v_o \approx v_{open}$：[▶ 1:45:20](https://youtu.be/UvUpOBgrix0?t=6320)

$$
P_L = \frac{V_{open}^2}{2R_L}
$$

例：喇叭 8 Ω（用 10 Ω 好算），$V_{open} = 5$ V：

$$
P_L = \frac{5^2}{2\times10} = 1.25\ \text{W}
$$

上瓦的功率，這就是目的。關鍵：輸出電阻要很小、電流要能給很大。後面就要來設計 high power 的輸出級。[▶ 1:49:01](https://youtu.be/UvUpOBgrix0?t=6541)

> 【課本補充】§12.1 (p. 922)：輸出級的要求是低輸出電阻、能送大電流給負載而不失真，同時效率要高；依導通角分為 A、B、AB、C 類。

---

## 9. 一頁速查表

| 項目 | 公式／重點 | 例 |
|---|---|---|
| 震盪 | $\angle A = -180^\circ$、$\lvert\beta A\rvert \ge 1$ | |
| 主極點補償 | $\omega_{P1}' \approx \sqrt2\,\omega_{P2}/A_0$ | $10^5 \to 10^2$ |
| 兩級 op amp | $\frac{10^4}{(1+s/2\times10^5)(1+s/2\times10^9)^2}$ | $\lvert A(\omega_{180})\rvert = 1/2$ |
| β = 1 相位邊限 | 約 20°（不夠） | |
| 改到 45° | 重疊極點各 22.5° → $\omega_{P1}' = 10^5$ | Miller 電容 ×2 |
| 負載功率 | $P_L = \frac{V_o^2}{2R_L}$（振幅） | |
| 阻抗匹配 | $R_L = R_{out}$，$P = \frac{V_{open}^2}{8R_{out}}$ | CE：0.6 mW |
| 射極隨耦器 | $R_{out} = \frac{R_C}{1+\beta} + r_e$ | 功率 ×100 |
| 實用 | $R_{out} \ll R_L$：$P = \frac{V_{open}^2}{2R_L}$ | 10 Ω：1.25 W |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 射極隨耦器輸出級 | 下一集：A 類輸出級、效率 |
| 大直流電流 | 功率消耗、散熱 |
| 補償電容 | op amp 設計（電子學後續） |

---

## 附：本集一句話總結

> **主極點補償的概念是「新第一極點 × 低頻增益 ≈ 原第二極點」；我們的兩級 op amp 因為第二極點有兩個重疊在 $2\times10^9$，在 $\omega_{180}$ 時增益只有 1/2，永遠穩定，但 $\beta = 1$ 時相位邊限只有 20°，把 Miller 那顆電容加倍、第一極點移到 $10^5$ 就有 45°。第十章開始：負載功率是 $V_o^2/2R_L$，共射放大器輸出電阻 $R_C$ 太大，就算阻抗匹配也只有零點幾 mW；後面接射極隨耦器讓輸出電阻變成 $R_C/(1+\beta) + r_e$，只要遠小於喇叭的 $R_L$，輸出電壓幾乎不掉，就能拿到上瓦的功率。**

---

*筆記依據陳振芳老師「電子學（四）」112 學年度 Lec05 錄影逐字稿（whisper，1:50:05）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
