---
course: 電子學（三）（112 學年度）
episode: 14
lecture: Lec04 第七章 差動放大器 (4/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=x5zWWhRF2J0
notes: 老師第 7 章 = Sedra/Smith 7e Ch8、Ch9；§9.1.3 大信號 MOS 差動對、§8.5.5 折疊疊接 (p. 555)、§9.5 電流鏡負載 (p. 644)
---

# 第 14 集 · 112-Lec04：電流源負載與疊接差動放大器、折疊疊接、源極退化換線性範圍、大信號特性、電流鏡負載 [▶ 影片](https://www.youtube.com/watch?v=x5zWWhRF2J0)

← 上一集：[13](13-diff-amp-rss-cascode-level-shift-active-load.md) ｜ [總目錄](../README.md) ｜ 下一集：[15](15-current-mirror-load-two-stage-opamp.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 14 集（112 學年度 Lec04）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:53:18，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 電流源負載：支點成立的條件](#1-電流源負載支點成立的條件)
- [2. 用短路電流 × 輸出電阻再算一次](#2-用短路電流--輸出電阻再算一次)
- [3. 疊接 + 疊接負載：增益上萬](#3-疊接--疊接負載增益上萬)
- [4. 折疊疊接](#4-折疊疊接)
- [5. 源極退化：增益換線性範圍](#5-源極退化增益換線性範圍)
- [6. 大信號特性](#6-大信號特性)
- [7. 數位用法：電流全部倒向一邊](#7-數位用法電流全部倒向一邊)
- [8. 電流鏡負載](#8-電流鏡負載)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

繼續把差動放大器的增益做大（電流源負載、疊接、折疊疊接），再看它的線性範圍和大信號行為，最後開始講**電流鏡負載**。

---

## 1. 電流源負載：支點成立的條件

[▶ 00:32](https://youtu.be/x5zWWhRF2J0?t=32)

差動對汲極接 PMOS 電流源（閘極固定電壓）。共模增益假設很小，只算差模：加 $\pm\frac12v_{id}$，拿掉直流源。[▶ 01:33](https://youtu.be/x5zWWhRF2J0?t=93)

假設尾節點仍是 0（蹺蹺板支點）：每邊電流 $i = \frac12g_mv_{id}$ 流進 $r_{on}\parallel r_{op}$：[▶ 06:08](https://youtu.be/x5zWWhRF2J0?t=368)

$$
v_{o1,2} = \mp\frac12g_m\left(r_{on}\parallel r_{op}\right)v_{id}
$$

$r_o = 100$ k → 例 $\frac12\times2\times50 = 50$；用 $r_o$ 當負載，比以前的電阻大很多。[▶ 13:49](https://youtu.be/x5zWWhRF2J0?t=829)

**支點成立的條件** [▶ 08:13](https://youtu.be/x5zWWhRF2J0?t=493)：兩邊電流必須大小一樣、方向相反（**互補對稱**）——不是「一樣」，也不是不對稱；任何一點不對稱，尾節點就有電流流進 $R_{SS}$，前面就全錯。這裡驗證確實對稱，假設成立。

---

## 2. 用短路電流 × 輸出電阻再算一次

[▶ 14:51](https://youtu.be/x5zWWhRF2J0?t=891)

拆半邊後輸出等效成 $i_{sc}$ 並 $R_{out}$：

- $i_{sc}$：輸出短路，$r_{on}$、$r_{op}$ 兩端都是 0，沒電流 → $i_{sc} = \frac12g_mv_{id}$。[▶ 17:55](https://youtu.be/x5zWWhRF2J0?t=1075)
- $R_{out}$：$v_{id} = 0$，電流源 0，看回去 $r_{on}\parallel r_{op}$。[▶ 20:32](https://youtu.be/x5zWWhRF2J0?t=1232)

結果一樣。【口頭】寧願做兩次，兩次都很簡單。[▶ 23:43](https://youtu.be/x5zWWhRF2J0?t=1423)

---

## 3. 疊接 + 疊接負載：增益上萬

[▶ 24:44](https://youtu.be/x5zWWhRF2J0?t=1484)

每邊 NMOS 上面再疊一顆（閘極固定直流）、負載也是 PMOS 疊接。差模時兩邊互補、尾節點仍是支點，拆半邊。[▶ 28:22](https://youtu.be/x5zWWhRF2J0?t=1702)

- **$i_{sc}$**：$\frac12g_mv_{id}$ 往上看共閘入口只有 $1/g_m$（往自己的 $r_o$ 走幾乎沒有，1% 走那邊也還是要加回來）→ 全部流出。[▶ 33:30](https://youtu.be/x5zWWhRF2J0?t=2010)
- **$R_{out}$**（$v_{id} = 0$）：往下是疊接 $r_{o1}\cdot g_{m2}r_{o2}$，往上同樣——算電阻時 P、N 模型完全一樣。[▶ 38:08](https://youtu.be/x5zWWhRF2J0?t=2288)

$$
A_d = \frac12g_m\left[(g_mr_o^2)\parallel(g_mr_o^2)\right] = \frac14(g_mr_o)^2
$$

例 $g_m = 2$、$r_o = 100$ k：$g_mr_o = 200$ → $10^4$，**上萬**。（【口頭】$k = 2$ 只是好算。）[▶ 41:41](https://youtu.be/x5zWWhRF2J0?t=2501)

再疊一層再乘 $g_mr_o$（百倍）→ $10^6$；但 $V_{DD}$ 和地之間的電壓不夠，疊不了那麼多層。[▶ 44:16](https://youtu.be/x5zWWhRF2J0?t=2656)

---

## 4. 折疊疊接

[▶ 45:20](https://youtu.be/x5zWWhRF2J0?t=2720)

把疊接的上面那層**折過去**：輸入 NMOS 的汲極不再往上疊 NMOS，而是接到一顆 **PMOS** 共閘（折疊後 N 要換成 P，電流方向才對），再往下接負載。好處：輸入共模範圍可以從最底到最高——**rail-to-rail**。[▶ 46:20](https://youtu.be/x5zWWhRF2J0?t=2780)

差模分析一樣：$i_{sc}$ 全部出來（共閘入口 $1/g_m$），$R_{out}$ 還是兩個 $g_mr_o^2$ 並聯 → $A_d \approx \frac14(g_mr_o)^2$。[▶ 57:13](https://youtu.be/x5zWWhRF2J0?t=3433)

【口頭】為什麼要折疊，等講到回授電路會比較清楚。[▶ 58:17](https://youtu.be/x5zWWhRF2J0?t=3497)

> 【課本補充】§8.5.5 (p. 555)：折疊疊接（folded cascode）讓輸出擺幅和共模範圍更寬，是 CMOS op amp 常用架構。

---

## 5. 源極退化：增益換線性範圍

[▶ 59:51](https://youtu.be/x5zWWhRF2J0?t=3591)

小信號條件 $\frac12v_{id} \le 0.2(V_{GS} - V_t)$；$k$ 很大時 $V_{GS} - V_t$ 很小，能放大的 $v_{id}$ 很窄。[▶ 1:01:54](https://youtu.be/x5zWWhRF2J0?t=3714)

每邊源極加 $R_S$：$\frac12v_{id} = \frac{i}{g_m} + iR_S$：[▶ 1:03:29](https://youtu.be/x5zWWhRF2J0?t=3809)

$$
A_d = \frac12\frac{g_mR}{1 + g_mR_S}
$$

增益掉 $(1 + g_mR_S)$ 倍。但 $v_{gs}$ 只是 $\frac12v_{id}$ 的 $\frac{1}{1 + g_mR_S}$：[▶ 1:06:39](https://youtu.be/x5zWWhRF2J0?t=3999)

$$
\frac{\frac12v_{id}}{1 + g_mR_S} \le 0.2(V_{GS} - V_t)
$$

**線性範圍大 $(1 + g_mR_S)$ 倍**——增益換線性。【口頭】有時候需要一個電路專門把電壓「縮小」，就是這個意思。[▶ 1:09:13](https://youtu.be/x5zWWhRF2J0?t=4153)

---

## 6. 大信號特性

[▶ 1:11:17](https://youtu.be/x5zWWhRF2J0?t=4277)

不接電阻，$i_1 = \frac12k(v_{GS1} - V_t)^2$、$i_2 = \frac12k(v_{GS2} - V_t)^2$，$i_1 + i_2 = I$：

$$
\sqrt{i_1} - \sqrt{i_2} = \sqrt{\frac{k}{2}}\,(v_{GS1} - v_{GS2}) = \sqrt{\frac{k}{2}}\,v_{id}
$$

（源極是同一點，閘極電壓差就是 $v_{id}$。）可解出 $i_1$、$i_2$ 對 $v_{id}$ 的函數。[▶ 1:13:21](https://youtu.be/x5zWWhRF2J0?t=4401)

- $v_{id} = 0$：各 $I/2$（例 2 mA → 各 1 mA）。
- 線性（小信號）只在 $|v_{id}| \le 2\times0.2(V_{GS} - V_t) = 0.4$ V（$k = 2$）。[▶ 1:17:02](https://youtu.be/x5zWWhRF2J0?t=4622)
- $|v_{id}|$ 到 $\sqrt{2I/k}$（例 $\sqrt2$ V）：電流**全部**倒向一邊，另一邊 0。[▶ 1:20:07](https://youtu.be/x5zWWhRF2J0?t=4807)

> 【課本補充】§9.1.3：$i_{D1,2} = \frac{I}{2} \pm \sqrt{kI}\frac{v_{id}}{2}\sqrt{1 - \frac{(v_{id}/2)^2}{I/k}}$，全切換在 $|v_{id}| = \sqrt{2}\,V_{OV}$。

---

## 7. 數位用法：電流全部倒向一邊

[▶ 1:21:10](https://youtu.be/x5zWWhRF2J0?t=4870)

例：2 mA 全部倒到左邊、$R_D = 5$ kΩ → 照算汲極 $10 - 10 = 0$ V，比 $V_G - V_t$ 低，不在飽和 → 用三極管區（電阻 $R_{DS}$）重算：汲極約 0.2 V，差不多 0。另一邊沒電流，10 V。[▶ 1:22:44](https://youtu.be/x5zWWhRF2J0?t=4964)

輸出不是 0 就是 10 V——**數位**用途，不是線性放大器（工作點跑出去了）。[▶ 1:26:53](https://youtu.be/x5zWWhRF2J0?t=5213)

---

## 8. 電流鏡負載

[▶ 1:27:54](https://youtu.be/x5zWWhRF2J0?t=5274)

直接把以前的**電流鏡**拿來當負載：左邊 PMOS 閘極接汲極（二極體接法），右邊 PMOS 閘極接同一點。不需要另外做定電流源。

**直流** [▶ 1:29:27](https://youtu.be/x5zWWhRF2J0?t=5367)：【口頭】增益很大的電路直流都很難算，Early 效應一點點就差很多。對稱時兩邊各 $I/2$，兩顆 PMOS $V_{SG}$ 一樣，汲極約 $V_{DD} - V_{SG}$（$V_{SG}$ 約 2 V）。IC 裡兩顆畫在一起，幾乎等電位。[▶ 1:34:10](https://youtu.be/x5zWWhRF2J0?t=5650)

**交流** [▶ 1:36:13](https://youtu.be/x5zWWhRF2J0?t=5773)：和以前完全不一樣——尾節點**不再是支點**：左邊被二極體接法的 MOS 拉住（電壓幾乎不動），右邊被放大很多，兩邊不對稱。要重新解。[▶ 1:37:15](https://youtu.be/x5zWWhRF2J0?t=5835)

**二極體接法那邊看進去** [▶ 1:43:03](https://youtu.be/x5zWWhRF2J0?t=6183)：加 $V$，電流 $g_mV + V/r_o$ → $R = \frac{1}{g_m}\parallel r_o \approx \frac{1}{g_m}$，很小（買 $k$ 大一點更小）→ 輸入電流全部被抓進去。另一顆 MOS 閘極一樣電壓，就複製出一樣的電流 → **電流鏡**：抓電流、複製電流。[▶ 1:48:12](https://youtu.be/x5zWWhRF2J0?t=6492)

右邊看進去是 $r_o$（很大），所以電流鏡把左邊的電流 $i_1$ 複製過去，和右邊的 $i_2$ 在輸出相遇。（完整推導下一集。）[▶ 1:51:19](https://youtu.be/x5zWWhRF2J0?t=6679)

---

## 9. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 電流源負載 | $A_d = \frac12g_m(r_{on}\parallel r_{op})$ | 互補對稱才有支點 |
| 疊接差動 | $\frac14(g_mr_o)^2$（例 $10^4$） | $i_{sc}$ 全出、$R_{out}$ 兩個 $g_mr_o^2$ 並聯 |
| 折疊疊接 | 增益相同；rail-to-rail 共模 | N 換 P |
| 源極退化 | 增益 ÷ $(1 + g_mR_S)$；線性範圍 × $(1 + g_mR_S)$ | |
| 大信號 | $\sqrt{i_1} - \sqrt{i_2} = \sqrt{k/2}\,v_{id}$ | 全切換在 $\sqrt{2I/k}$ |
| 線性範圍 | $v_{id}$ 在 $\pm 2\times0.2(V_{GS} - V_t)$ 內（例 ±0.4 V） | 小信號 |
| 數位用法 | 電流全倒一邊，輸出 0 / $V_{DD}$ | |
| 電流鏡負載 | 二極體側看進去 $1/g_m\parallel r_o$ | 抓電流、複製 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 電流鏡負載 | 下一集：完整分析（單端輸出得到全部增益） |
| 折疊疊接 | op amp、回授電路 |
| 大信號切換 | 比較器、數位邏輯 |

---

## 附：本集一句話總結

> **差動對加電流源負載，在兩邊互補對稱時尾節點仍是支點，增益 $\frac12g_m(r_{on}\parallel r_{op})$；疊接加疊接負載用短路電流 × 輸出電阻算得 $\frac14(g_mr_o)^2$，上萬倍，折疊疊接則讓共模範圍到 rail-to-rail；源極加 $R_S$ 讓增益掉 $(1+g_mR_S)$ 倍、線性範圍大同樣倍數；大信號下 $|v_{id}|$ 到 $\sqrt{2I/k}$ 電流全倒一邊變成數位開關；改用電流鏡當負載時支點不成立，二極體那邊只有 $1/g_m$，專門抓電流再複製到另一邊。**

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec04 錄影逐字稿（whisper，1:53:18）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
