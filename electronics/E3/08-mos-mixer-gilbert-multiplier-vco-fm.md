---
course: 電子學（三）前導課程（113 學年度）
episode: 08
lecture: Lec08 第六章 信號產生與處理電路 (3/5)
date: 113 學年度
video: https://www.youtube.com/watch?v=xHw1MxhZDIE
notes: 老師第 6 章；Gilbert 乘法器課本沒有完整推導（Sedra 網站補充）；VCO §18；積分器跟隨的觀念同電子學（二）第 8 集
---

# 第 08 集 · Lec08：MOS 混頻器、四象限類比乘法器、壓控電容與 VCO（FM）、「跟隨」的原理 [▶ 影片](https://www.youtube.com/watch?v=xHw1MxhZDIE)

← 上一集：[07](07-nonlinear-colpitts-hartley-mixer.md) ｜ [總目錄](../README.md) ｜ 下一集：[09](09-tracking-power-source-pll.md) →

> **課程**：電子學（三）前導課程，陽明交大 電子物理系，113 學年度 — 第 08 集
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:56:58，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. MOS 混頻器：AM 調變](#1-mos-混頻器am-調變)
- [2. 為什麼要「純」乘法器](#2-為什麼要純乘法器)
- [3. 兩層差動對：四象限乘法器](#3-兩層差動對四象限乘法器)
- [4. 直流偏壓與輸入、輸出的接法](#4-直流偏壓與輸入輸出的接法)
- [5. 壓控電容](#5-壓控電容)
- [6. 壓控振盪器與 FM](#6-壓控振盪器與-fm)
- [7. 「跟隨」的原理：比較 + 充電](#7-跟隨的原理比較--充電)
- [8. op amp 的亦步亦趨也是這樣](#8-op-amp-的亦步亦趨也是這樣)
- [9. 積分器做的電壓源，還缺大電流](#9-積分器做的電壓源還缺大電流)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

繼續通訊系統的電路：MOS 版的混頻器、能消掉多餘項的**純類比乘法器**；用乘法器做**壓控電容**，放進振盪器變成 **VCO**，產生 FM。最後回到「跟隨」（亦步亦趨）的基本原理，準備做大電流的電壓源。

---

## 1. MOS 混頻器：AM 調變

[▶ 00:31](https://youtu.be/xHw1MxhZDIE?t=31)

MOS 差動對（汲極電阻 $R$），差動輸入 $v$（小信號，一人一半）→ 單端輸出 $\frac12g_mRv$。每顆電流 $I/2$：

$$
g_m = \sqrt{2k\frac{I}{2}} = \sqrt{kI}
$$

[▶ 03:05](https://youtu.be/xHw1MxhZDIE?t=185)

尾電流源用電流鏡（例 1 mA），在尾電流那顆 MOS 的閘極加一個**很慢**的信號 $f(t)$（聲音，頻率遠小於載波）→ $I = I_0 + f(t)/R'$（$R'$ 是從那裡看下去的等效電阻）。[▶ 05:44](https://youtu.be/xHw1MxhZDIE?t=344)

$f$ 變得很慢，對差動對來說 $I$ 就像直流。代入並展開根號（調變量 ≪ 1）：[▶ 10:27](https://youtu.be/xHw1MxhZDIE?t=627)

$$
v_o = \frac12R\sqrt{kI_0}\left(1 + \frac{f(t)}{2I_0R'}\right)v
$$

$v = \sin\omega_ct$（載波）→ $A[1 + mf(t)]\sin\omega_ct$，**AM 信號**。頻譜：載波 + 兩邊聲音邊帶（$10^2$～$10^5$ rad/s 寬）。接收端用 tuner 整包抓出來，不要太寬。[▶ 13:33](https://youtu.be/xHw1MxhZDIE?t=813)

---

## 2. 為什麼要「純」乘法器

[▶ 17:16](https://youtu.be/xHw1MxhZDIE?t=1036)

上面的 AM 除了 $v\times f$ 的乘積，還多一根**載波本身**。做 FM 和各式信號處理需要**純粹的乘法器**（pure multiplier）：只有 $v_1v_2$。多的那根很靠近，不是拿個頻率選擇器就能去掉——只能讓它**正負號相反、互相抵消**。[▶ 18:20](https://youtu.be/xHw1MxhZDIE?t=1100)

---

## 3. 兩層差動對：四象限乘法器

[▶ 18:52](https://youtu.be/xHw1MxhZDIE?t=1132)

- **下層**：一個差動對，輸入 $v_2$，把尾電流 $I$ 分成 $\frac12I + i$ 和 $\frac12I - i$（$i = \frac12g_mv_2$，小信號）。[▶ 19:56](https://youtu.be/xHw1MxhZDIE?t=1196)
- **上層**：兩個差動對分別坐在這兩條電流上，都輸入 $v_1$；直流不同所以 $g_{m1} \ne g_{m2}$。[▶ 23:33](https://youtu.be/xHw1MxhZDIE?t=1413)
- **交叉接**：把上層兩對的集極（汲極）交叉相連，讓只和 $v_1$ 有關、或只和 $v_2$ 有關的項正負抵消。[▶ 24:33](https://youtu.be/xHw1MxhZDIE?t=1473)

取差動輸出 $v_{o2} - v_{o1}$：[▶ 27:12](https://youtu.be/xHw1MxhZDIE?t=1632)

$$
v_{o2} - v_{o1} = \frac12R\,(g_{m1} - g_{m2})\,v_1
$$

$g_{m1,2} = \sqrt{k\left(\frac12I \pm i\right)}$，用小信號展開根號，差值 $\propto i \propto v_2$：[▶ 29:53](https://youtu.be/xHw1MxhZDIE?t=1793)

$$
v_{o2} - v_{o1} = K\,v_1v_2
$$

$K$ 是由 $k$、$I$、$R$ 組成的常數。其他項全部抵消——**純類比乘法器**（pure analog multiplier）。【口頭】什麼都沒有，乾乾淨淨。[▶ 34:39](https://youtu.be/xHw1MxhZDIE?t=2079)

> 【課本補充】這個交叉耦合的兩層差動對叫 **Gilbert cell**（吉爾伯特乘法器），BJT 版用 tanh 特性推導。

---

## 4. 直流偏壓與輸入、輸出的接法

[▶ 36:11](https://youtu.be/xHw1MxhZDIE?t=2171)

上面寫的都是交流；實際要先有直流。

- 尾電流 2 mA（電流鏡接 −10 V），下層每顆 1 mA；$k = 2$ → $V_{GS} = 2$ V，下層源極 −2 V。[▶ 37:44](https://youtu.be/xHw1MxhZDIE?t=2264)
- 上層要疊在上面，每層都要留飽和的空間：上層閘極至少約 4 V，輸出 5 V 左右。[▶ 39:17](https://youtu.be/xHw1MxhZDIE?t=2357)
- **$v_1$ 要拆成 $5 \pm \frac12v_1$ 兩個輸入**：前面再放一個差動對，負載用二極體接法的 MOS（看進去 $1/g_m$），增益 $\frac12g_m\cdot\frac{1}{g_m} = \frac12$，剛好給出 $\pm\frac12v_1$；直流用約 3 V 的崩潰二極體墊高到 5 V。[▶ 42:26](https://youtu.be/xHw1MxhZDIE?t=2546)
- **輸出相減**：$v_{o2}$、$v_{o1}$ 都對地，接一個差動放大器（op amp 減法器）取 $v_{o2} - v_{o1}$。[▶ 48:11](https://youtu.be/xHw1MxhZDIE?t=2891)

最後得到兩個對地的輸入 $v_1$、$v_2$，輸出 $Kv_1v_2$。[▶ 49:44](https://youtu.be/xHw1MxhZDIE?t=2984)

---

## 5. 壓控電容

[▶ 50:18](https://youtu.be/xHw1MxhZDIE?t=3018)

**壓控電容**（voltage-controlled capacitance）：用電壓調電容值。MOS 閘極不吃電流，所以可以這樣接：電容一端接節點 $v$，另一端接乘法器輸出 $Kf(t)v$（乘法器兩個輸入是 $v$ 和 $f(t)$）。[▶ 52:56](https://youtu.be/xHw1MxhZDIE?t=3176)

電容電流：

$$
i = C\frac{d}{dt}\left[v - Kf(t)v\right]
$$

$f$（聲音，最高 $10^5$）比 $v$（FM 載波，幾百 MHz，$10^8$）慢至少三個數量級 → 微分時把 $f$ 當常數：[▶ 1:01:51](https://youtu.be/xHw1MxhZDIE?t=3711)

$$
i \approx C\left[1 - Kf(t)\right]\frac{dv}{dt},
\qquad
C_{\text{eff}} = C\left[1 - Kf(t)\right]
$$

從節點看進去的電容被 $f(t)$ 調變了。[▶ 1:05:04](https://youtu.be/xHw1MxhZDIE?t=3904)

---

## 6. 壓控振盪器與 FM

[▶ 1:06:06](https://youtu.be/xHw1MxhZDIE?t=3966)

把變壓器耦合振盪器 tank 裡的 $C$ 換成這個壓控電容（直流時電感短路，交流分析一樣）：[▶ 1:07:38](https://youtu.be/xHw1MxhZDIE?t=4058)

$$
\omega = \frac{1}{\sqrt{L_1C\left[1 - Kf(t)\right]}} \approx \omega_0\left[1 + \frac12Kf(t)\right]
$$

（調變要小：$Kf \ll 1$。）振盪頻率在 $\omega_0$ 附近跟著聲音一點點變——**壓控振盪器**（VCO, voltage-controlled oscillator），輸出就是 **FM 信號**。[▶ 1:12:27](https://youtu.be/xHw1MxhZDIE?t=4347)

【口頭】FM 的資訊在頻率，傳過來振幅被雜訊干擾沒關係，所以受雜訊影響比 AM 小。之後再講 FM、AM 解調。[▶ 1:16:00](https://youtu.be/xHw1MxhZDIE?t=4560)

> 【課本補充】實際 VCO 常用**變容二極體**（varactor，反向偏壓的接面電容 $C_j \propto 1/\sqrt{V_0 + V_R}$，見第 01 集）。

---

## 7. 「跟隨」的原理：比較 + 充電

[▶ 1:17:01](https://youtu.be/xHw1MxhZDIE?t=4621)

【口頭】很多電路需要讓一個電壓「亦步亦趨」跟著另一個。概念像兩個水桶：偵測兩個水位的**差**（detect difference），產生電流，去充電把差補掉，直到電流 0——穩態。[▶ 1:18:05](https://youtu.be/xHw1MxhZDIE?t=4685)

$$
v_o \to v_{\text{ref}},
\qquad
\tau = RC
$$

如果 $v_{\text{ref}}$ 會變，只要它變的頻率遠低於 $1/\tau$，$v_o$ 隨時跟得上。【口頭】我走得比你快，你往哪走我都跟得上。[▶ 1:24:21](https://youtu.be/xHw1MxhZDIE?t=5061)

---

## 8. op amp 的亦步亦趨也是這樣

[▶ 1:26:57](https://youtu.be/xHw1MxhZDIE?t=5217)

以前分析 op amp 從沒放電容；其實任何半導體元件的哪隻腳看進去都有電容。op amp（增益 $A$）比較兩端的差，乘 $A$ 產生電流去充負端的電容：[▶ 1:29:34](https://youtu.be/xHw1MxhZDIE?t=5374)

$$
\tau = \frac{RC}{A}
$$

$A$ 很大 → 電流很大 → 充得很快 → 一下就相等，這就是**虛短路**（virtual short）。加了 $R_1$、$R_2$ 的放大器，只要 $A$ 夠大，結果回到 $1 + R_2/R_1$。[▶ 1:38:23](https://youtu.be/xHw1MxhZDIE?t=5903)

【口頭】完全靠積分：一直積、一直積，非要兩個差值等於 0 不可。[▶ 1:39:26](https://youtu.be/xHw1MxhZDIE?t=5966)

---

## 9. 積分器做的電壓源，還缺大電流

[▶ 1:40:30](https://youtu.be/xHw1MxhZDIE?t=6030)

直接用 op amp **積分器**：比較 $v_r$（參考電壓，可調）和 $v_o$，差值產生電流 $\frac{v_r - v_o}{R}$ 去充電容，直到電流 0 → $v_o = v_r$，$\tau = RC$。[▶ 1:42:35](https://youtu.be/xHw1MxhZDIE?t=6155)

- 輸出被負載拉低 → 和 $v_r$ 不一樣 → 回授把它拉回來。可調的電壓源。[▶ 1:46:17](https://youtu.be/xHw1MxhZDIE?t=6377)
- 後面加放大器 $A$：$\tau = RC/A$，跟得更快。[▶ 1:48:20](https://youtu.be/xHw1MxhZDIE?t=6500)
- 目的是推小負載 $R_L$、提供大電流——但 op amp（741）輸出電流會飽和在約 ±20 mA，**電流驅動能力**（current driving capability）很差。[▶ 1:52:58](https://youtu.be/xHw1MxhZDIE?t=6778)

→ 下次在輸出加電流放大（BJT），電壓增益 1 沒關係（電壓前面已經放大），但能提供幾 A 的電流。[▶ 1:55:06](https://youtu.be/xHw1MxhZDIE?t=6906)

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| MOS 差動對 $g_m$ | $\sqrt{kI}$（每顆 $I/2$） | |
| MOS 混頻器 | $v_o = \frac12R\sqrt{kI_0}(1 + \frac{f}{2I_0R'})v$ | AM，多一根載波 |
| 四象限乘法器 | $v_{o2} - v_{o1} = Kv_1v_2$ | 兩層差動對交叉接 |
| 輸入拆分 | 差動對 + $1/g_m$ 負載：$\pm\frac12v_1$ | 加直流墊高 |
| 壓控電容 | $C_{\text{eff}} = C[1 - Kf(t)]$ | $f$ 慢，微分當常數 |
| VCO / FM | $\omega \approx \omega_0[1 + \frac12Kf(t)]$ | |
| 跟隨原理 | 比較差值 → 電流充電 → 差為 0 | $\tau = RC$ |
| op amp | $\tau = RC/A$ | 虛短路的來源 |
| 積分器電壓源 | $v_o \to v_r$ | 電流不夠 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 大電流電壓源 | 下一集：加 BJT 輸出級、穩壓 |
| 乘法器 | FM 解調、鎖相迴路 |
| VCO | 鎖相迴路（PLL） |

---

## 附：本集一句話總結

> **讓差動對的尾電流跟著聲音慢慢變，$g_m = \sqrt{kI}$ 就跟著變，得到 AM；兩層差動對交叉相接、取差動輸出，所有多餘項抵消，得到純乘法器 $Kv_1v_2$；電容一端接乘法器輸出就成了 $C[1-Kf(t)]$ 的壓控電容，放進振盪器就是 VCO，輸出 FM。所謂亦步亦趨，就是比較差值、產生電流充電直到差為 0（op amp 的 $\tau = RC/A$）；用積分器做的電壓源還缺大電流，下次加 BJT。**

---

*筆記依據陳振芳老師「電子學（三）前導課程」113 學年度 Lec08 錄影逐字稿（whisper，1:56:58）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
