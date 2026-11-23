---
course: 電子學（三）（112 學年度）
episode: 13
lecture: Lec03 第七章 差動放大器 (3/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=MkpisPznUfU
notes: 老師第 7 章 = Sedra/Smith 7e Ch9；§9.3 共模拒斥 (p. 627)、§9.5 電流鏡負載差動放大器 (p. 644)、§8.5 疊接；輸入偏壓（位準移位）是老師自己的例子
---

# 第 13 集 · 112-Lec03：讓 $R_{SS}$ 變大（疊接、op amp 電流源）、單電源時怎麼偏壓輸入、主動負載與疊接差動放大器 [▶ 影片](https://www.youtube.com/watch?v=MkpisPznUfU)

← 上一集：[12](12-diff-amp-cm-dm-icmr-half-circuit.md) ｜ [總目錄](../README.md) ｜ 下一集：[14](14-diff-amp-active-cascode-folded-large-signal.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 13 集（112 學年度 Lec03）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（2:12:16，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 定電流源偏壓的好處：輸入可以帶直流](#1-定電流源偏壓的好處輸入可以帶直流)
- [2. 差動對 = 兩倍的單邊電路](#2-差動對--兩倍的單邊電路)
- [3. 差模、共模（複習）](#3-差模共模複習)
- [4. 讓 $R_{SS}$ 變大：疊接電流源](#4-讓-r_ss-變大疊接電流源)
- [5. op amp 做的理想電流源](#5-op-amp-做的理想電流源)
- [6. 單電源：共模範圍不含 0](#6-單電源共模範圍不含-0)
- [7. 位準移位：給輸入墊 5 V](#7-位準移位給輸入墊-5-v)
- [8. 現代低電壓差動對](#8-現代低電壓差動對)
- [9. 主動負載與疊接差動放大器](#9-主動負載與疊接差動放大器)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

1. 再看一次為什麼用定電流源偏壓、差動對的共模範圍。
2. 共模增益 $-R_D/(2R_{SS})$ 要小 → 想辦法讓 $R_{SS}$ 很大。
3. 實務問題：單電源時輸入怎麼偏壓。
4. 把增益做大：主動負載、疊接 → op amp。

---

## 1. 定電流源偏壓的好處：輸入可以帶直流

[▶ 00:30](https://youtu.be/MkpisPznUfU?t=30)

單顆共源、源極接電流源（+ 電容）：輸入直接加直流 $V_{DC}$，電容自己充到源極 $= V_{DC} - 2$ V，電流還是 1 mA。條件：放大管 $5 \ge V_{DC} - 1$、電流鏡那顆 $V_{DC} - 2 \ge -9$ → $-7 \le V_{DC} \le 6$。[▶ 07:05](https://youtu.be/MkpisPznUfU?t=425)

在範圍內，信號源帶直流都不影響，交流照樣放大。【口頭】這是定電流源偏壓最大的優點；以前的分壓偏壓一定要電容擋直流，不擋就跳出去。[▶ 11:49](https://youtu.be/MkpisPznUfU?t=709)

---

## 2. 差動對 = 兩倍的單邊電路

[▶ 15:55](https://youtu.be/MkpisPznUfU?t=955)

兩顆共用 2 mA 電流源、各 1 mA，汲極 5 kΩ 接 10 V。對稱，兩邊能加的直流一樣多——就是**共模範圍** −7～6 V，很大（電源 ±10 V）。[▶ 18:59](https://youtu.be/MkpisPznUfU?t=1139)

---

## 3. 差模、共模（複習）

[▶ 23:41](https://youtu.be/MkpisPznUfU?t=1421)

- 直流：$V_{DD} - \frac12IR_D = 5$ V。
- 差模：尾節點電壓 0（假設兩電流一樣，得到兩電壓一樣 → $R_{SS}$ 沒電流 → 自洽），直接接地算半電路：$v_o = \mp\frac12g_mR_Dv_{id}$；$\frac12v_{id} \le 0.2(V_{GS} - V_t)$。[▶ 30:03](https://youtu.be/MkpisPznUfU?t=1803)
- 共模：$i = \frac{v_{cm}}{1/g_m + 2R_{SS}} \approx \frac{v_{cm}}{2R_{SS}}$（$R_{SS} \ge r_o$，$g_mr_o \gg 1$；一顆 MOS 再怎麼接負載，增益頂多 $g_mr_o$）→ $A_{cm} = -\frac{R_D}{2R_{SS}}$。[▶ 47:50](https://youtu.be/MkpisPznUfU?t=2870)

**差動放大器要好用**，差模那項要遠大於共模那項——$R_{SS}$ 不夠大就有問題。[▶ 53:28](https://youtu.be/MkpisPznUfU?t=3208)

---

## 4. 讓 $R_{SS}$ 變大：疊接電流源

[▶ 54:58](https://youtu.be/MkpisPznUfU?t=3298)

單顆電流源 MOS：$V_A = 100$ V、2 mA → $r_o = 50$ kΩ。疊兩顆（cascode）：從頂端加 $V_x$，$I_x$ 流過 $r_{o1}$ 產生 $I_xr_{o1}$，上面那顆 $v_{gs} = -I_xr_{o1}$ 產生 $g_{m2}r_{o1}I_x$，加 $I_x$ 流過 $r_{o2}$：[▶ 57:00](https://youtu.be/MkpisPznUfU?t=3420)

$$
R_{SS} = r_{o1} + r_{o2} + g_{m2}r_{o2}r_{o1} \approx (g_mr_o)\,r_o
$$

約大 100 倍 → 共模增益小 100 倍以下。【口頭】IC 裡不能做大電阻（要拉很長），就自己畫疊接。[▶ 1:02:43](https://youtu.be/MkpisPznUfU?t=3763)

---

## 5. op amp 做的理想電流源

[▶ 1:04:46](https://youtu.be/MkpisPznUfU?t=3886)

尾電流源換成：MOS 源極接電阻 $R$ 到 $-V_{DD}$，op amp 正端接一個自己定的電壓 $V$，負端接 MOS 源極，輸出推閘極。負回授 → 虛短路 → $R$ 上電壓固定 → 電流 $= V/R$，不管上面共模怎麼變都不變——**理想電流源**。[▶ 1:05:48](https://youtu.be/MkpisPznUfU?t=3948)

共模輸入抬高，其他點電壓會變，但電流不變 → 共模增益沒了，變成完美的差動放大器。【口頭】做實驗時多一個電阻、一個 op amp 就好。[▶ 1:10:24](https://youtu.be/MkpisPznUfU?t=4224)

---

## 6. 單電源：共模範圍不含 0

[▶ 1:11:58](https://youtu.be/MkpisPznUfU?t=4318)

【口頭】做實驗準備兩台電源（±10 V）很麻煩，多一台就多很多錢。改成單一 10 V、底下接地（電流鏡 $k = 4$、2 mA、$V_{GS} = 2$ V）：[▶ 1:12:59](https://youtu.be/MkpisPznUfU?t=4379)

- Q1、Q2：$5 \ge V_{CM} - 1$ → $V_{CM} \le 6$ V。
- Q3：$V_{CM} - 2 \ge 2 - 1$ → $V_{CM} \ge 3$ V。

$$
3\ \text{V} \le V_{CM} \le 6\ \text{V}
$$

**不包括 0**：一端接地、另一端接 $v_i$ 時，共模 $= \frac12v_i \approx 0$，根本不在範圍內，電路不能用；接小小的交流也不行。[▶ 1:18:13](https://youtu.be/MkpisPznUfU?t=4693)

→ 兩端都墊 5 V（大約在範圍中間），再疊交流 $\pm\frac12v_i$。但接兩台 5 V 電源不合理。[▶ 1:21:51](https://youtu.be/MkpisPznUfU?t=4911)

---

## 7. 位準移位：給輸入墊 5 V

[▶ 1:24:25](https://youtu.be/MkpisPznUfU?t=5065)

在前面加一級電路產生「5 V + 交流」：一個差動對（2 mA 電流源，閘極接地 + 接 $v_s$），汲極負載用**二極體接法的 MOS**，上面再串一顆約 3 V 的**崩潰二極體**到 10 V。[▶ 1:26:28](https://youtu.be/MkpisPznUfU?t=5188)

- 直流：$10 - 3 - 2 = 5$ V，兩邊都是 5 V，很穩。[▶ 1:28:02](https://youtu.be/MkpisPznUfU?t=5282)
- 交流：7 V 那點交流接地；二極體接法的 MOS 看進去是 $1/g_m$，差動對電流 $\frac12g_mv_s$ 乘 $1/g_m$ → 輸出 $5 \pm \frac12v_s$。[▶ 1:31:10](https://youtu.be/MkpisPznUfU?t=5470)

兩個輸出共模 5 V、差模 $v_s$，接到後面的差動放大器就對了。增益在第二級。要別的直流就自己設計（換崩潰電壓）。[▶ 1:34:49](https://youtu.be/MkpisPznUfU?t=5689)

---

## 8. 現代低電壓差動對

[▶ 1:37:59](https://youtu.be/MkpisPznUfU?t=5879)

電源 5 V / 0 V，$k = 200$（尾電流 $k = 400$、2 mA），所有 $V_{GS} = 1.1$ V；汲極設 3 V（$R_D = 2$ kΩ）。

- Q1、Q2：$3 \ge V_{CM} - 1$ → $V_{CM} \le 4$ V。
- 尾電流管：$V_{CM} - 1.1 \ge 0.1$ → $V_{CM} \ge 1.2$ V。

$$
1.2\ \text{V} \le V_{CM} \le 4\ \text{V}
$$

[▶ 1:43:07](https://youtu.be/MkpisPznUfU?t=6187)

一端接地 → 共模幾乎 0，遠超出範圍；取一半（約 2.5 V）大概最好。$g_m = 20$ mA/V、$R_D = 2$ k → $A_d = \frac12\times20\times2 = 20$。【口頭】之後看應用就知道，它通常接回授，功能是偵測兩點電壓差。[▶ 1:48:16](https://youtu.be/MkpisPznUfU?t=6496)

---

## 9. 主動負載與疊接差動放大器

[▶ 1:49:51](https://youtu.be/MkpisPznUfU?t=6591)

**PMOS 電流源負載**（閘極接固定直流）：交流時電流源開路，只剩 $r_{op}$；尾節點是支點接地：[▶ 1:53:56](https://youtu.be/MkpisPznUfU?t=6836)

$$
A_d = \frac12g_m\left(r_{on}\parallel r_{op}\right)
$$

負載是 Early 電阻（50 k、100 k），增益很大；兩邊互補。【口頭】只考慮上面的 $r_{op}$、不管下面的 $r_{on}$ 就太離譜了。[▶ 1:55:32](https://youtu.be/MkpisPznUfU?t=6932)

**疊接差動放大器 + 疊接負載** [▶ 1:58:40](https://youtu.be/MkpisPznUfU?t=7120)：每邊 NMOS 疊接（閘極偏壓例 2、4 V 之類）、PMOS 疊接負載。用**短路電流 × 輸出電阻**：

- 短路電流：$\frac12g_mv_{id}$ 往上看共閘入口只有 $1/g_m$，全部流出。[▶ 2:03:26](https://youtu.be/MkpisPznUfU?t=7406)
- 輸出電阻：往下 $g_mr_o\cdot r_o$、往上也是 $g_mr_o\cdot r_o$，並聯（交流模型不分 N、P）。[▶ 2:08:14](https://youtu.be/MkpisPznUfU?t=7694)

$$
A_d = \frac12g_m\left[(g_mr_o^2)\parallel(g_mr_o^2)\right] = \frac14(g_mr_o)^2
$$

增益上萬。把兩個輸入的差放很大——就是 **op amp**。[▶ 2:10:48](https://youtu.be/MkpisPznUfU?t=7848)

> 【課本補充】§9.5 (p. 644)：主動負載差動對常用電流鏡負載（單端輸出也拿到全部差模增益 $g_m(r_{o2}\parallel r_{o4})$），是 op amp 輸入級的標準做法。

---

## 10. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| 定電流源偏壓 | 輸入可帶直流（例 −7～6 V） | 電容自己調 |
| 共模增益 | $-R_D/(2R_{SS})$ | 要 $R_{SS}$ 大 |
| 疊接 $R_{SS}$ | $\approx g_mr_o\cdot r_o$ | 大 100 倍 |
| op amp 電流源 | $I = V/R$ | 理想，$A_{cm} \to 0$ |
| 單電源 ICMR | 例 3～6 V（不含 0） | 輸入要墊直流 |
| 位準移位 | 差動對 + $1/g_m$ 負載 + 崩潰二極體 → $5 \pm \frac12v_s$ | |
| 5 V 電源 ICMR | 1.2～4 V | 輸入墊約一半 |
| 電阻負載 | $A_d = \frac12g_mR_D$（例 20） | |
| 主動負載 | $\frac12g_m(r_{on}\parallel r_{op})$ | |
| 疊接差動 | $\frac14(g_mr_o)^2$ | op amp 等級 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 疊接、主動負載 | op amp 內部設計 |
| 輸入偏壓 / 位準移位 | 多級放大器 |
| 不匹配 | 下一集：失配與偏移 |

---

## 附：本集一句話總結

> **差動放大器的共模增益 $-R_D/(2R_{SS})$ 要小，所以尾電流源要做成疊接（$R_{SS} \approx g_mr_o\cdot r_o$）或用 op amp 做成理想電流源；單電源時輸入共模範圍不包含 0，要先用一級位準移位電路（差動對 + $1/g_m$ 負載 + 崩潰二極體）把輸入墊到範圍中間；負載換成 PMOS 電流源增益是 $\frac12g_m(r_{on}\parallel r_{op})$，再用疊接 + 疊接負載就到 $\frac14(g_mr_o)^2$，這就是 op amp。**

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec03 錄影逐字稿（whisper，2:12:16）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
