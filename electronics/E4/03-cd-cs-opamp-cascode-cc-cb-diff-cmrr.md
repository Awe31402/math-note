---
course: 電子學（四）（112 學年度）
episode: 3
lecture: Lec03 第九章 放大器頻率響應 (3/5)
date: 112 學年度
video: https://www.youtube.com/watch?v=DXOygJ_gLGQ
notes: 老師第 9 章 = Sedra/Smith 7e Ch10；§10.5 CG 與疊接的高頻響應、§10.7 差動放大器的高頻響應 (p. 769)、§10.8 CD–CS、CC–CB (p. 779)
---

# 第 3 集 · Lec03：CD–CS 頻寬、op amp 中間插隨耦器、疊接打掉 Miller、BJT 的 CC–CB、差動放大器的頻率響應與 CMRR [▶ 影片](https://www.youtube.com/watch?v=DXOygJ_gLGQ)

← 上一集：[02](02-cs-two-poles-miller-source-follower-cd-cs.md) ｜ [總目錄](../README.md) ｜ 下一集：[04](04-mirror-load-doublet-opamp-poles-compensation.md) →

> **課程**：電子學（四），陽明交大 電子物理系，112 學年度 — 第 3 集（Lec03）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:01:03，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：CS 的 Miller 與 CD–CS](#1-複習cs-的-miller-與-cdcs)
- [2. 隨耦器本身的頻寬](#2-隨耦器本身的頻寬)
- [3. 兩級 op amp 中間插一個隨耦器](#3-兩級-op-amp-中間插一個隨耦器)
- [4. 第二招：疊接（cascode）](#4-第二招疊接cascode)
- [5. BJT 例：CC–CB](#5-bjt-例cccb)
- [6. 差動放大器：差模頻率響應](#6-差動放大器差模頻率響應)
- [7. 共模：尾電流源的電容讓 CMRR 很早就掉](#7-共模尾電流源的電容讓-cmrr-很早就掉)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

CS 增益高但頻寬差（Miller）。兩招解法：前面加**隨耦器**（橫的 cascade）、上面加**共閘**（直的 cascode）。再看差動放大器的頻率響應。

---

## 1. 複習：CS 的 Miller 與 CD–CS

[▶ 00:30](https://youtu.be/DXOygJ_gLGQ?t=30)

CS：$R_s = 50$ k、$R_L = r_{o6}\parallel r_{o7} = 25$ k、$g_m = 4$。$C_{gd}$ 搬到輸入端變成 $C(1 + g_mR_L)$，乘上很大的 $R_s$：[▶ 02:34](https://youtu.be/DXOygJ_gLGQ?t=154)

$$
\tau \approx CR_s(1 + g_mR_L) = 10^{-12}\times50\text{k}\times101
\quad\Longrightarrow\quad
\omega_H \approx 2\times10^5
$$

【口頭】要維持這麼高的電壓放大，充電就要很久，頻率就要很低。[▶ 02:03](https://youtu.be/DXOygJ_gLGQ?t=123)

**CD–CS** [▶ 06:15](https://youtu.be/DXOygJ_gLGQ?t=375)：前面的隨耦器把「大 $R_s$ 的不理想電壓源」變成「幾乎理想的電壓源」（串 $1/g_m$）。CS 那顆 $C_{gd}$ 看到：[▶ 10:51](https://youtu.be/DXOygJ_gLGQ?t=651)

$$
C\left[\frac{1}{g_m}(1 + g_mR_L) + R_L\right] \approx 2CR_L
$$

Miller 不見了（看回去的電阻變得很小）→ 頻寬回到約 $2\times10^7$。【口頭】頻寬越快越好。[▶ 15:30](https://youtu.be/DXOygJ_gLGQ?t=930)

---

## 2. 隨耦器本身的頻寬

[▶ 16:30](https://youtu.be/DXOygJ_gLGQ?t=990)

隨耦器負載用電阻 $R$（例 1 k）或電流源。最難處理的 $C_{gs}$（跨輸入輸出）：加 $V_x$ 求 $R_x$：[▶ 17:36](https://youtu.be/DXOygJ_gLGQ?t=1056)

$$
R_x = \frac{R_s + R}{1 + g_mR}
$$

$g_m = 4$、$R = 1$ k → 分母 5。$R$ 越大越好：若用電流源（$R$ 很大很大），極點 $\to g_m/C$，而且零點和極點抵消，完美隨耦，電容兩端等電位不充電。分母 $1 + g_mR$ 讓隨耦器的頻寬很寬。[▶ 23:49](https://youtu.be/DXOygJ_gLGQ?t=1429)

---

## 3. 兩級 op amp 中間插一個隨耦器

[▶ 24:21](https://youtu.be/DXOygJ_gLGQ?t=1461)

兩級 CMOS op amp（差動 + CS），第一級輸出到 CS 之間插一顆源極隨耦器（電流源負載）。IC 設計基底接最負（NMOS）。[▶ 26:25](https://youtu.be/DXOygJ_gLGQ?t=1585)

**沒有隨耦器時** [▶ 32:36](https://youtu.be/DXOygJ_gLGQ?t=1956)：頻寬決定在 CS（第一級的差動放大器不管），時間常數相加，Miller 那項主導 → $10^5$。

**直流偏壓要重新安排** [▶ 36:42](https://youtu.be/DXOygJ_gLGQ?t=2202)：隨耦器會讓直流位準移動一個 $V_{GS}$（2 V）。原本第一級輸出直流正好是第二級需要的 $V_{GS}$，插入隨耦器後要多加一顆 MOS（讓第一級電流鏡那邊也多一個 $V_{GS}$），電壓才對得上。差動對 100% 對稱。【口頭】直流和交流要分開看，分析頻率時把直流擦掉。[▶ 43:23](https://youtu.be/DXOygJ_gLGQ?t=2603)

**時間常數** [▶ 50:05](https://youtu.be/DXOygJ_gLGQ?t=3005)（全用 $C$）：

- 隨耦器輸入的 $C$ 看 $R_s$：$CR_s$。
- 隨耦器的 $C_{gs}$：$C\frac{R_s + R}{1 + g_mR}$，約 $\frac15CR_s$ 量級。
- CS 的 $C_{gd}$：$g_m$ 消掉，約 $2CR_L = CR_s$。[▶ 53:40](https://youtu.be/DXOygJ_gLGQ?t=3220)

全部約 $(1 + \frac15 + 1 + \cdots)CR_s$ → 頻寬約 $0.7\times10^7$，比原本 $2\times10^5$ 好約 35 倍。[▶ 56:49](https://youtu.be/DXOygJ_gLGQ?t=3409)

---

## 4. 第二招：疊接（cascode）

[▶ 57:52](https://youtu.be/DXOygJ_gLGQ?t=3472)

CS 上面接一顆**共閘**（閘極接固定電壓）。$R_s$ 一樣 50 k。

CS 那顆的 $C_{gd}$：Miller 的倍數是「CS 這一顆的增益」——它的負載是上面共閘從源極看進去的 $\frac{1}{g_m}$（很小）：[▶ 59:26](https://youtu.be/DXOygJ_gLGQ?t=3566)

$$
\left|A_{v1}\right| = g_m\cdot\frac{1}{g_m} = 1
\quad\Longrightarrow\quad
C_{gd}(1 + 1) = 2C_{gd}
$$

第一級根本沒有放大（只有 1 倍），$g_m$ 消掉，沒有 Miller。[▶ 1:01:30](https://youtu.be/DXOygJ_gLGQ?t=3690)

共閘那顆：閘極接 AC 地，它的 $C_{gd}$ 從輸出搬到地，沒有信號進來就沒有 Miller。[▶ 1:03:33](https://youtu.be/DXOygJ_gLGQ?t=3813) 中間節點的兩個電容看 $1/g_m$（幾百 Ω），時間常數很小（$10^9$ 量級）。輸出節點的電容看 $R_L$。[▶ 1:05:45](https://youtu.be/DXOygJ_gLGQ?t=3945)

總頻寬約 $10^7$；而增益 $-g_mR_{out}$，$R_{out}$ 是疊接看回去很大的電阻，增益很大。【口頭】上面接共閘會讓下面那顆沒有增益，但整個電路 overall 增益很大、頻寬也不錯。[▶ 1:10:27](https://youtu.be/DXOygJ_gLGQ?t=4227)

**cascade vs cascode** [▶ 1:12:01](https://youtu.be/DXOygJ_gLGQ?t=4321)：前面加隨耦器是**橫的** cascade；往上疊共閘是**直的** cascode。

---

## 5. BJT 例：CC–CB

[▶ 1:13:02](https://youtu.be/DXOygJ_gLGQ?t=4382)

BJT 和 MOS 幾乎一樣，舉一個例子。（BJT 電容 $C_\pi$、$C_\mu$ 的物理不推了。）兩顆 BJT 射極相接（像差動對），信號從 $Q_1$ 基極進（集極接 $V_{CC}$），$Q_2$ 基極接地，從 $Q_2$ 集極（負載 $R_L$）出——$Q_1$ 是共集、$Q_2$ 是共基。[▶ 1:14:37](https://youtu.be/DXOygJ_gLGQ?t=4477)

- 電流 $g_mv$ 從 $Q_1$ 射極全部流進 $Q_2$ 射極再出來 → 兩邊 $v_{be}$ 一樣大，兩個 $C_\pi$ **串聯**：$C_\pi/2$。[▶ 1:18:45](https://youtu.be/DXOygJ_gLGQ?t=4725)
- $Q_1$ 的 $C_\mu$：集極接 AC 地 → 沒有 Miller。$Q_2$ 的 $C_\mu$：基極接地 → 也沒有。[▶ 1:21:24](https://youtu.be/DXOygJ_gLGQ?t=4884)

**低頻增益** [▶ 1:24:57](https://youtu.be/DXOygJ_gLGQ?t=5097)：從輸入看進去是兩個 $r_\pi$（射極接射極），$v_s$ 先分壓到 $2r_\pi$，一半跨在 $Q_2$：

$$
A_0 = \frac{2r_\pi}{R_s + 2r_\pi}\cdot\frac12g_mR_L
$$

兩個極點：$\frac{1}{\frac{C_\pi}{2}(R_s\parallel2r_\pi)}$ 與 $\frac{1}{C_\mu R_L}$。都沒有 Miller，頻寬不錯。[▶ 1:30:44](https://youtu.be/DXOygJ_gLGQ?t=5444)

> 【課本補充】§10.8 (p. 779)：CC–CB（CD–CG）組態——沒有 Miller 效應的寬頻放大器。

---

## 6. 差動放大器：差模頻率響應

[▶ 1:32:46](https://youtu.be/DXOygJ_gLGQ?t=5566)

電阻負載的差動放大器，$\pm\frac12v_{id}$。差模時完全對稱，蹺蹺板，尾節點不動 → **AC 地**。[▶ 1:38:26](https://youtu.be/DXOygJ_gLGQ?t=5906)

所以看半電路就好：就是一個 CS，$C_{gd}$ 有 Miller。信號源電阻若很大，就在前面加隨耦器。若 $R_s = 0$，輸入電容沒影響（被電壓源直接驅動），只剩輸出端 $C_{gd} + C_{db}$ 看 $R$：[▶ 1:41:35](https://youtu.be/DXOygJ_gLGQ?t=6095)

$$
A_d(s) = \frac{g_mR}{1 + sC_LR}
$$

（還有一個很遠的零點，不理它。）

---

## 7. 共模：尾電流源的電容讓 CMRR 很早就掉

[▶ 1:43:42](https://youtu.be/DXOygJ_gLGQ?t=6222)

共模時尾節點會動。尾電流源有輸出電阻 $R_{SS}$ 和電容 $C_{SS}$（尾電流管汲極到地的電容、差動對兩個源極到基底的電容合在一起）。[▶ 1:47:53](https://youtu.be/DXOygJ_gLGQ?t=6473)

【口頭】IC 設計時要讓 $R_{SS}$（就是 $r_o$）很大：$r_o = V_A/I$，$V_A = V_A'L$，$V_A'$ 是台積電的固定參數 → channel 畫長一點。[▶ 1:48:26](https://youtu.be/DXOygJ_gLGQ?t=6506)

半電路：尾阻抗拆成兩個 $2R_{SS}$ 並 $C_{SS}/2$。$R_{SS}$ 很大時：[▶ 1:53:47](https://youtu.be/DXOygJ_gLGQ?t=6827)

$$
A_{cm}(s) \approx -\frac{R}{2R_{SS}}\left(1 + sC_{SS}R_{SS}\right)
$$

——多了一個**零點** $\omega_Z = \frac{1}{C_{SS}R_{SS}}$。$R_{SS}$ 很大 → 零點很低頻，共模增益一開始貼在地板（很好），但**很早**就往上升。[▶ 1:55:23](https://youtu.be/DXOygJ_gLGQ?t=6923)

**CMRR** [▶ 1:59:07](https://youtu.be/DXOygJ_gLGQ?t=7147)：$\text{CMRR} = |A_d/A_{cm}|$。過了 $\omega_Z$ 共模往上升，CMRR 開始往下掉；再過差模的極點又掉得更快。

$$
\text{CMRR}(s) \approx \frac{g_mR\cdot2R_{SS}/R}{(1 + sC_{SS}R_{SS})(1 + sC_LR)}
$$

兩個極點都不好。【口頭】後面講電流鏡負載會好一點。[▶ 2:00:39](https://youtu.be/DXOygJ_gLGQ?t=7239)

> 【課本補充】§10.7.1 (p. 769 起)：電阻負載 MOS 差動對——差模用半電路即可；共模的 $A_{cm}$ 在 $f_Z = \frac{1}{2\pi C_{SS}R_{SS}}$ 開始上升，CMRR 從那裡開始以 −20 dB/dec 下降。

---

## 8. 一頁速查表

| 項目 | 公式／重點 | 例 |
|---|---|---|
| CS（大 $R_s$） | $\tau \approx CR_s(1+g_mR_L)$ | $2\times10^5$ |
| CD–CS | CS 的 $C_{gd}$ 項 $\approx 2CR_L$ | $2\times10^7$ |
| 隨耦器 $C_{gs}$ | $R_x = \frac{R_s+R}{1+g_mR}$ | 越大 $R$ 越好 |
| op amp 插隨耦器 | 要多一顆 MOS 補 $V_{GS}$ 偏壓 | $0.7\times10^7$（35 倍） |
| 疊接 | 下面那顆增益 1 → $2C_{gd}$ | $10^7$、增益大 |
| CC–CB | $C_\pi$ 串聯成 $C_\pi/2$；$A_0 = \frac{2r_\pi}{R_s+2r_\pi}\cdot\frac12g_mR_L$ | 無 Miller |
| 差模 | 半電路 = CS；尾節點 AC 地 | |
| 共模 | $A_{cm} \approx -\frac{R}{2R_{SS}}(1+sC_{SS}R_{SS})$ | 零點 |
| CMRR | 從 $\frac{1}{C_{SS}R_{SS}}$ 開始掉 | channel 畫長 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 電流鏡負載的頻率響應 | 下一集 |
| 疊接 | 高頻 op amp 設計 |
| CMRR 頻率特性 | op amp 規格 |

---

## 附：本集一句話總結

> **CS 的 Miller 有兩招打掉：前面接隨耦器（橫的 cascade），讓 CS 看到的只是 $1/g_m$，兩級 op amp 中間插一顆（記得補一顆 MOS 讓直流偏壓對上）頻寬好約 35 倍；或上面疊共閘（直的 cascode），下面那顆增益只剩 1，$C_{gd}$ 只變兩倍，整體增益仍很大。BJT 的 CC–CB 兩個 $C_\pi$ 串聯、沒有 Miller。差動放大器的差模用半電路就是 CS；共模則因尾電流源的 $C_{SS}$ 在 $1/(C_{SS}R_{SS})$ 出現零點，共模增益很早就上升，CMRR 跟著往下掉。**

---

*筆記依據陳振芳老師「電子學（四）」112 學年度 Lec03 錄影逐字稿（whisper，2:01:03）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
