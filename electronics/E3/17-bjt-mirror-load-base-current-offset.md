---
course: 電子學（三）（112 學年度）
episode: 17
lecture: Lec07 第七章 差動放大器 (7/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=UOJl3pix1S0
notes: 老師第 7 章 = Sedra/Smith 7e Ch8、Ch9；§9.5.4 BJT 電流鏡負載差動放大器 (p. 651)、§9.4 系統偏移 (p. 637)、§8.2.3 BJT 電流鏡與基極電流補償 (p. 518)
---

# 第 17 集 · 112-Lec07：BJT 電流鏡負載差動放大器、共模範圍、基極電流造成的偏移與補償、BJT 疊接差動放大器 [▶ 影片](https://www.youtube.com/watch?v=UOJl3pix1S0)

← 上一集：[16](16-opamp-feedback-offset-bjt-diff-amp.md) ｜ [總目錄](../README.md) ｜ 下一集：[18](18-wilson-mirror-bjt-opamp-design-feedback-intro.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 17 集（112 學年度 Lec07）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:51:59，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`⚠️ 待確認` 查不清楚；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 差模增益：短路電流 × 輸出電阻](#1-差模增益短路電流--輸出電阻)
- [2. 共模增益](#2-共模增益)
- [3. 共模範圍：非常大](#3-共模範圍非常大)
- [4. 基極電流讓輸出偏 2 V](#4-基極電流讓輸出偏-2-v)
- [5. 補償：加一顆 BJT 幫電流鏡供基極電流](#5-補償加一顆-bjt-幫電流鏡供基極電流)
- [6. 兩級 BJT op amp 與模型](#6-兩級-bjt-op-amp-與模型)
- [7. BJT 疊接差動放大器](#7-bjt-疊接差動放大器)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

BJT 版的電流鏡負載差動放大器：增益、共模、共模範圍；BJT 才有的問題——**基極電流**讓電流鏡不對稱，造成輸出偏移，以及怎麼補償。最後是 BJT 疊接版。

---

## 1. 差模增益：短路電流 × 輸出電阻

[▶ 00:31](https://youtu.be/UOJl3pix1S0?t=31)

電路非常不對稱（電流鏡一邊拉回、一邊沒有），直接解很麻煩 → 做兩次。[▶ 01:35](https://youtu.be/UOJl3pix1S0?t=95)

**短路電流** [▶ 05:10](https://youtu.be/UOJl3pix1S0?t=310)：輸出短路後兩邊又對稱，尾節點是支點；電流鏡輸入端看進去非常小，左邊電流全部進去、鏡像到右邊，和右邊電流相加：

$$
i_{sc} = g_mv_{id},
\qquad
g_m = \frac{I_C}{V_T} = 40\ \text{mA/V}
$$

（MOS 例子是 2，BJT 大 20 倍。）[▶ 07:14](https://youtu.be/UOJl3pix1S0?t=434)

**輸出電阻**（$v_{id} = 0$）[▶ 08:18](https://youtu.be/UOJl3pix1S0?t=498)：從輸出加 $V_x$——

- 往下看 $Q_2$：射極接的是 $Q_1$ 那邊的 $r_e$（很小），套 BJT 疊接公式（$r_\pi$ 並聯很小的電阻）→ 約 $2r_{o2}$。[▶ 13:27](https://youtu.be/UOJl3pix1S0?t=807)
- 這個電流 $V_x/(2r_{o2})$ 也流進 $Q_1$、被電流鏡鏡像回輸出，再一個 $V_x/(2r_{o2})$。[▶ 15:31](https://youtu.be/UOJl3pix1S0?t=931)
- 往上 $r_{o4}$。

$$
\frac{1}{R_{out}} = \frac{1}{2r_{o2}} + \frac{1}{2r_{o2}} + \frac{1}{r_{o4}}
\quad\Longrightarrow\quad
R_{out} = r_{o2}\parallel r_{o4}
$$

$$
A_d = g_m(r_{o2}\parallel r_{o4}) = 40\times50 = 2000
$$

[▶ 19:09](https://youtu.be/UOJl3pix1S0?t=1149)

---

## 2. 共模增益

[▶ 20:42](https://youtu.be/UOJl3pix1S0?t=1242)

尾電流源有電阻 $R_{EE}$（至少 $r_o$），拆成兩個 $2R_{EE}$。每邊電流很小，大部分跨在 $R_{EE}$ 上。左邊電流經電流鏡複製到右邊，但 BJT 電流鏡有**基極電流**，複製過去的比原來少一點（除以 $1 + 2/\beta$）——兩個相減的差流進 $r_{o4}$：[▶ 25:25](https://youtu.be/UOJl3pix1S0?t=1525)

$$
A_{cm} \approx -\frac{r_{o4}}{\beta_P R_{EE}}
$$

例子裡共模增益約 0.01，差模 2000。【口頭】電路本來就不對稱（基極電流），一點點不對稱就造成共模增益，很合理。[▶ 29:37](https://youtu.be/UOJl3pix1S0?t=1777)

> ⚠️ 待確認：逐字稿這段的式子聽不完整，上式是依「鏡像電流少 $2/\beta$、差額流過 $r_{o4}$」整理的量級；課本 §9.5.4 (p. 651) 的 BJT 結果為 $A_{cm} \approx -\frac{r_{o4}}{\beta_P R_{EE}}$，兩者一致，但老師板書的係數待查。

---

## 3. 共模範圍：非常大

[▶ 30:40](https://youtu.be/UOJl3pix1S0?t=1840)

BJT 主動區要 $V_{CE} \ge 0.2$ V（0.2 是自己假設的，可能 0.1，甚至接近 0）。±10 V、1 mA：[▶ 31:43](https://youtu.be/UOJl3pix1S0?t=1903)

- Q1、Q2：集極約 $10 - 0.7 = 9.3$ V，射極 $V_{CM} - 0.7$，要 $9.3 - (V_{CM} - 0.7) \ge 0.2$ → $V_{CM} \le 9.8$ V。
- 尾電流管：射極 −10 V、集極 $V_{CM} - 0.7$，要 $\ge -10 + 0.2$ → $V_{CM} \ge -9.1$ V。

$$
-9.1\ \text{V} \le V_{CM} \le 9.8\ \text{V}
$$

**非常大**，幾乎到電源。[▶ 35:22](https://youtu.be/UOJl3pix1S0?t=2122)

---

## 4. 基極電流讓輸出偏 2 V

[▶ 35:53](https://youtu.be/UOJl3pix1S0?t=2153)

兩端輸入都接地。若不考慮基極電流：完全對稱，兩邊各 1 mA，兩個集極都 $10 - 0.7 = 9.3$ V。[▶ 39:28](https://youtu.be/UOJl3pix1S0?t=2368)

**考慮基極電流** [▶ 44:08](https://youtu.be/UOJl3pix1S0?t=2648)：左邊 1 mA 要分給二極體接法那顆的集極**和兩顆 PNP 的基極**（共 $2I_C/\beta$）→ 電流鏡複製到右邊的電流

$$
I_{C4} = \frac{I/2}{1 + 2/\beta}
$$

比右邊 NPN 要的 $I/2$ 少一點；差額 $\approx \frac{2}{\beta}\cdot\frac{I}{2}$ 流過 $r_{o4}$：[▶ 46:42](https://youtu.be/UOJl3pix1S0?t=2802)

$$
\Delta V_O \approx -\frac{2}{\beta}\cdot\frac{I}{2}\cdot r_{o4} = -\frac{2}{100}\times1\ \text{mA}\times100\ \text{k} = -2\ \text{V}
$$

輸出從 9.3 V 掉到 **7.3 V**。後面若再接一級共射，9.3 V 被當成 0.7 V 的基極偏壓來設計，現在 2.7 V 的差灌進去——完全不對。【口頭】MOS 沒有這個問題（閘極沒電流）。[▶ 50:26](https://youtu.be/UOJl3pix1S0?t=3026)

> 【課本補充】§9.4 (p. 637)：這叫**系統偏移**（systematic offset），來自電流鏡的 $2/\beta_P$ 誤差。

---

## 5. 補償：加一顆 BJT 幫電流鏡供基極電流

[▶ 52:58](https://youtu.be/UOJl3pix1S0?t=3178)

電流鏡兩顆 PNP 的基極不直接接到二極體那顆的集極，而是經一顆 **BJT（$Q_5$）的射極**供電，$Q_5$ 的基極接到左邊集極。基極電流要經過 $Q_5$，所以左邊只被抽走 $\frac{2I_C}{\beta(1+\beta)}$——多除一個 $\beta$：[▶ 54:32](https://youtu.be/UOJl3pix1S0?t=3272)

$$
\Delta V_O \approx -\frac{2\ \text{V}}{100} = -0.02\ \text{V}
$$

偏移變得很小。[▶ 55:34](https://youtu.be/UOJl3pix1S0?t=3334)

**小問題** [▶ 56:35](https://youtu.be/UOJl3pix1S0?t=3395)：$Q_5$ 只流兩個基極電流（1 mA/β 的量級，五十分之一 mA）——電流太小，$V_{BE}$ 不是 0.7 V，可能只有 0.56 V，兩邊又不對稱。→ $Q_5$ 射極再接一顆電阻到地（約 $0.7\ \text{V}/1\ \text{mA}$），讓它的電流在 1 mA 左右、$V_{BE}$ 回到約 0.7 V。代價是又多一點不對稱，但大部分問題都解決了。[▶ 1:01:13](https://youtu.be/UOJl3pix1S0?t=3673)

【口頭】做之前沒辦法知道每顆 $\beta$ 多少，這樣做總是可以解決大部分問題；面積（電流比）也可以用佈局調。**接回授之後**偏移的問題就都解決了。[▶ 1:07:36](https://youtu.be/UOJl3pix1S0?t=4056)

> 【課本補充】§8.2.3 (p. 518, Fig. 8.11)：這是**有基極電流補償的電流鏡**（current mirror with base-current compensation），電流傳輸比誤差從 $2/\beta$ 降到 $2/\beta^2$。

---

## 6. 兩級 BJT op amp 與模型

[▶ 1:10:43](https://youtu.be/UOJl3pix1S0?t=4243)

差動放大器 + 一級共射（PNP，電流源負載）：

- 第二級的輸入電阻 $r_\pi$ 很小，直接接會把第一級的 $r_o\parallel r_o$ 並聯掉、增益沒了 → 中間加一顆**射極隨耦器**（voltage follower）隔開，輸入電阻變 $(1+\beta)$ 倍。[▶ 1:12:46](https://youtu.be/UOJl3pix1S0?t=4366)
- 第二級電流取大一點（例 2 mA 或 10 mA），$g_m$ 變大、$r_o$ 變小，乘起來差不多。[▶ 1:16:25](https://youtu.be/UOJl3pix1S0?t=4585)

總增益約 $4\times10^6$。[▶ 1:17:58](https://youtu.be/UOJl3pix1S0?t=4678)

**模型** [▶ 1:18:30](https://youtu.be/UOJl3pix1S0?t=4710)：輸出電阻 = 最後兩顆 $r_o$ 並聯；輸入差動電阻（每邊 $\frac12v_{id}$、基極電流 $\frac{v_{id}/2}{r_\pi}$）：

$$
R_{id} = 2r_\pi = 5\ \text{k}\Omega
$$

---

## 7. BJT 疊接差動放大器

[▶ 1:23:51](https://youtu.be/UOJl3pix1S0?t=5031)

兩層：NPN 疊接放大 + PNP 疊接電流鏡負載。仍然不對稱，做兩次：

- 短路電流：共基入口 $r_e$ 很小，電流全部進去；短路後兩邊又是蹺蹺板 → $i_{sc} = g_mv_{id}$。[▶ 1:25:58](https://youtu.be/UOJl3pix1S0?t=5158)
- 輸出電阻：往下看疊接，底下那顆射極看到的是 $r_e$ 並 $r_\pi$ 之類 → 疊接公式 $\approx \beta_2r_{o2}$ 的一半（$\frac12\beta r_o$，因為鏡像那條路又分一份）；往上看 PNP 疊接 $\beta r_o$。[▶ 1:31:35](https://youtu.be/UOJl3pix1S0?t=5495)

$$
A_d \approx g_m\left[\tfrac12\beta_3r_{o3}\parallel\beta_4r_{o4}\right]
$$

$\beta$、$r_o$ 例 100、100 k → 增益非常大，**一級就夠了**（不疊接的要兩級）。[▶ 1:46:47](https://youtu.be/UOJl3pix1S0?t=6407)

【口頭】BJT 不要再堆一層，沒用（又被 $r_\pi$ 並掉）；MOS 可以一直疊。現在的 technology 尺寸越來越小，有時設計不出來，就要靠這些技巧。[▶ 1:48:52](https://youtu.be/UOJl3pix1S0?t=6532)

**回授的預告** [▶ 1:49:56](https://youtu.be/UOJl3pix1S0?t=6596)：$R_{id} = 5$ kΩ 好像很小，但接成電壓放大器（非反相）後，從輸入看進去變成 $R_{id}(1 + \beta A_d)$——非常大；輸出電阻則變得很小。這就是回授電路的特色，下一章講。

---

## 8. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 短路電流 | $g_mv_{id}$（$g_m$ = 40 mA/V） | 短路後對稱 |
| 輸出電阻 | $r_{o2}\parallel r_{o4}$ | $2r_{o2}$ 兩條路並聯 |
| 差模增益 | $g_m(r_{o2}\parallel r_{o4})$（例 2000） | |
| 共模增益 | $\approx -r_{o4}/(\beta_PR_{EE})$（例 ≈ 0.01） | 基極電流不對稱 |
| 共模範圍 | 例 −9.1～9.8 V | $V_{CE} \ge 0.2$ |
| 系統偏移 | $\Delta V_O \approx -\frac{2}{\beta}\frac{I}{2}r_{o4}$（例 −2 V） | |
| 補償 | 加 $Q_5$：誤差再除 $\beta$（例 −0.02 V） | $Q_5$ 射極加電阻 |
| 兩級 BJT op amp | 中間加射極隨耦器 | 例 $4\times10^6$ |
| 輸入電阻 | $R_{id} = 2r_\pi$ | 接回授後 ×$(1+\beta A_d)$ |
| BJT 疊接差動 | $g_m[\frac12\beta r_o\parallel\beta r_o]$ | 一級就夠 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 基極電流補償 | 741 等 BJT op amp |
| 回授改變 $R_{in}$、$R_{out}$ | 第 8 章負回授 |
| 射極隨耦器隔開 | 多級放大、輸出級 |

---

## 附：本集一句話總結

> **BJT 電流鏡負載差動放大器的短路電流 $g_mv_{id}$、輸出電阻 $r_{o2}\parallel r_{o4}$，增益約 2000，共模範圍幾乎到電源；但電流鏡兩顆 PNP 的基極電流讓鏡像少了 $2/\beta$，輸出偏移約 −2 V，加一顆 BJT 替電流鏡供基極電流就把誤差再除一個 $\beta$；疊接版一級就有很大增益，但 BJT 不能再往上疊；輸入電阻只有 $2r_\pi$，接成回授後會被放大 $(1+\beta A_d)$ 倍。**

---

## ⚠️ 待確認清單

1. 第 2 節共模增益的係數：逐字稿聽不完整，目前寫課本的 $-r_{o4}/(\beta_PR_{EE})$。

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec07 錄影逐字稿（whisper，1:51:59）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
