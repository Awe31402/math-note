---
course: 電子學（三）（112 學年度）
episode: 18
lecture: Lec08 第七章 差動放大器 (8/8)（後段進入第八章）
date: 112 學年度
video: https://www.youtube.com/watch?v=Zwg7MGcYu4A
notes: 老師第 7、8 章 = Sedra/Smith 7e Ch8、Ch9、Ch11；§8.6.2 Wilson 電流鏡 (p. 560)、§11.1 回授的一般結構 (p. 808)、§11.2 負回授的性質 (p. 815)
---

# 第 18 集 · 112-Lec08：BJT 疊接電流鏡負載、Wilson 電流鏡、三級 BJT op amp 設計；負回授的基本三式 [▶ 影片](https://www.youtube.com/watch?v=Zwg7MGcYu4A)

← 上一集：[17](17-bjt-mirror-load-base-current-offset.md) ｜ [總目錄](../README.md) ｜ 下一集：[19](19-series-shunt-practical-beta-series-series.md) →

> **課程**：電子學（三），陽明交大 電子物理系，112 學年度 — 第 18 集（112 學年度 Lec08）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:56:02，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`⚠️ 待確認` 查不清楚；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. BJT 疊接 + 疊接電流鏡負載](#1-bjt-疊接--疊接電流鏡負載)
- [2. 基極電流的偏移又回來了](#2-基極電流的偏移又回來了)
- [3. Wilson 電流鏡：偏移小一個 $\beta$](#3-wilson-電流鏡偏移小一個-beta)
- [4. 三級 BJT op amp：直流設計](#4-三級-bjt-op-amp直流設計)
- [5. 功率、共模範圍](#5-功率共模範圍)
- [6. 交流：增益、輸入電阻、輸出電阻](#6-交流增益輸入電阻輸出電阻)
- [7. 第八章開始：負回授的基本三式](#7-第八章開始負回授的基本三式)
- [8. 回授讓輸入電阻變大、輸出電阻變小](#8-回授讓輸入電阻變大輸出電阻變小)
- [9. 回授讓頻寬變寬](#9-回授讓頻寬變寬)
- [10. 實際電路怎麼求 $A$、$R_i$、$R_o$：令 $\beta = 0$](#10-實際電路怎麼求-ar_ir_o令-beta--0)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

把差動放大器這章收尾：BJT 疊接電流鏡負載、Wilson 電流鏡、一個完整的三級 BJT op amp。然後進第八章**負回授**（feedback），寫出最基本的三個式子。

---

## 1. BJT 疊接 + 疊接電流鏡負載

[▶ 00:31](https://youtu.be/Zwg7MGcYu4A?t=31)

下面是疊接差動對，上面是疊接的電流鏡負載。照舊做兩次：

- **短路電流**：輸出短路，共基入口只有 $r_e = 1/g_m$，電流全部進去 → $i_{sc} = g_mv_{id}$。[▶ 01:32](https://youtu.be/Zwg7MGcYu4A?t=92)
- **輸出電阻** [▶ 03:03](https://youtu.be/Zwg7MGcYu4A?t=183)：往下看，底下那顆射極看到 $1/g_m$ 並 $r_\pi$，套疊接公式得 $\beta_3r_{o3}$；鏡像那條路再給一份一樣的電流 → 往下等效 $\frac12\beta_3r_{o3}$。往上看 PNP 疊接 $\beta_4r_{o4}$。

$$
R_{out} = \tfrac12\beta_3r_{o3}\parallel\beta_4r_{o4},
\qquad
A_d = g_mR_{out}
$$

[▶ 09:13](https://youtu.be/Zwg7MGcYu4A?t=553)

---

## 2. 基極電流的偏移又回來了

[▶ 09:46](https://youtu.be/Zwg7MGcYu4A?t=586)

沒有基極電流時，輸出直流 $= V_{CC} - 0.7 - 0.7$（兩個 $V_{EB}$）。考慮基極電流：電流鏡的集極電流是 $\frac{I/2}{1 + 2/\beta}$，和另一邊差一點，差額乘上很大的負載電阻 → 輸出偏很多。[▶ 12:50](https://youtu.be/Zwg7MGcYu4A?t=770)

【口頭】你根本不知道每顆 $\beta$ 多少，每一顆都跑掉，沒辦法控制；MOS 沒有這個問題。[▶ 14:55](https://youtu.be/Zwg7MGcYu4A?t=895)

---

## 3. Wilson 電流鏡：偏移小一個 $\beta$

[▶ 16:26](https://youtu.be/Zwg7MGcYu4A?t=986)

Wilson 只改上面的負載（下面差動對本來就有）。逐顆寫集極、射極、基極電流（射極 = 集極 × $\frac{1+\beta}{\beta}$，每到一個節點就少 $\frac{2}{1+\beta}$ 之類），整理後：[▶ 21:03](https://youtu.be/Zwg7MGcYu4A?t=1263)

$$
\Delta I \propto \frac{I}{\beta^2}
\qquad\text{（原本是 } \propto \frac{I}{\beta}\text{）}
$$

偏移電壓 = 差額 × 輸出電阻，**小了一個 $\beta$**（β = 100 就小 100 倍）。關鍵是靠多加的那一顆，兩邊的基極電流抵消掉大部分。[▶ 24:11](https://youtu.be/Zwg7MGcYu4A?t=1451)

**輸出電阻** [▶ 26:17](https://youtu.be/Zwg7MGcYu4A?t=1577)：從上面加 $V_x$，電流經疊接那顆下來（看到 $r_\pi$ 等級），一半一半分；輸出端的集極電流同時被鏡像回來……最後：

$$
R_{out,\text{Wilson}} \approx \tfrac12\beta r_o
$$

[▶ 40:50](https://youtu.be/Zwg7MGcYu4A?t=2450)

> 【課本補充】§8.6.2 (p. 560)：Wilson 電流鏡的電流傳輸比 $\frac{I_O}{I_{REF}} = \frac{1}{1 + 2/\beta^2}$，輸出電阻 $\approx \frac{\beta r_o}{2}$。

---

## 4. 三級 BJT op amp：直流設計

[▶ 41:20](https://youtu.be/Zwg7MGcYu4A?t=2480)

op amp 增益要很大 → 兩級差動放大再接輸出級。±10 V。

1. **第一級差動對**：尾電流 2 mA（電流鏡，射極約 −0.7 V → 電阻 $9.3\ \text{V}/2\ \text{mA}$），集極電阻讓集極約 5 V。[▶ 43:02](https://youtu.be/Zwg7MGcYu4A?t=2582)
2. **第二級差動對**：輸入是 5 V，集極約 7 V（比基極高 2 V，集基逆偏、保持主動區）。[▶ 44:35](https://youtu.be/Zwg7MGcYu4A?t=2675)
3. **準位移動**：7 V 直流太高，用射極電阻把直流降下來，例 1 mA 流過 2.3 kΩ 掉 2.3 V，讓下一顆的基極在設計值。【口頭】加電阻增益會稍微小一點，但必要。[▶ 46:08](https://youtu.be/Zwg7MGcYu4A?t=2768)
4. **輸出級**：為了讓輸出電阻很小，最後一定用**射極隨耦器**；直流輸出最好是 0（正中間，上下擺動範圍最大）。例 10.7 kΩ 讓那顆 1 mA；最後一顆 10 mA。[▶ 46:40](https://youtu.be/Zwg7MGcYu4A?t=2800)

> ⚠️ 待確認：各級電阻值（2.3 k、10.7 k、1 k 等）是依逐字稿拼湊的，板書的完整電路圖要回影片對照。

---

## 5. 功率、共模範圍

**功率** [▶ 49:47](https://youtu.be/Zwg7MGcYu4A?t=2987)：全部是直流算的。各支路電流相加（例 2 + 1 + 1 + 1 + 10 mA…）乘 20 V 就是這塊 IC 消耗的功率。最後一級直流要夠大——推出去的電流不可能比直流大（1 kΩ、10 mA → 送出去最多 10 mA）。[▶ 50:19](https://youtu.be/Zwg7MGcYu4A?t=3019)

**共模範圍** [▶ 52:57](https://youtu.be/Zwg7MGcYu4A?t=3177)：Q1、Q2 要 $V_{CE} \ge 0.2$：$5 - (V_{CM} - 0.7) \ge 0.2$ → $V_{CM} \le 5.5$ V；尾電流管 → $V_{CM} \ge -9.1$ V。

$$
-9.1\ \text{V} \le V_{CM} \le 5.5\ \text{V}
$$

[▶ 55:40](https://youtu.be/Zwg7MGcYu4A?t=3340)

---

## 6. 交流：增益、輸入電阻、輸出電阻

[▶ 57:44](https://youtu.be/Zwg7MGcYu4A?t=3464)

- **輸入電阻**：$\frac12v_{id}/r_\pi$ → $R_{id} = 2r_\pi$（1 mA、$\beta = 100$：$r_\pi = 2.5$ k → 5 kΩ）。[▶ 59:46](https://youtu.be/Zwg7MGcYu4A?t=3586)
- **第一級**：負載是集極電阻並聯第二級的 $r_\pi$（2.5 k），例 1.67 k → $\frac12\times40\times1.67 \approx 33$。[▶ 1:04:53](https://youtu.be/Zwg7MGcYu4A?t=4073)
- **第二級**、**準位移動 + 隨耦**：負載要考慮下一級看進去的 $r_\pi + (\beta+1)R_E$（射極電阻讓輸入電阻變大）。[▶ 1:07:29](https://youtu.be/Zwg7MGcYu4A?t=4049)
- 總增益約 **一萬八**（兩萬左右）。[▶ 1:12:48](https://youtu.be/Zwg7MGcYu4A?t=4368)

**輸出電阻** [▶ 1:13:18](https://youtu.be/Zwg7MGcYu4A?t=4398)：信號源拿掉，從輸出看回射極隨耦器：前一級的電阻除以 $(1+\beta)$ 再加 $r_e$（10 mA → 2.5 Ω）：

$$
R_o \approx \frac{10.7\ \text{k}}{101} + 2.5 \approx 109\ \Omega
$$

很小。模型：$R_{id} = 5$ kΩ、$A_d \approx 1.8\times10^4$、$R_o = 109\ \Omega$。接回授後 109 Ω 還會再除一個很大的數。[▶ 1:16:56](https://youtu.be/Zwg7MGcYu4A?t=4616)

---

## 7. 第八章開始：負回授的基本三式

[▶ 1:18:31](https://youtu.be/Zwg7MGcYu4A?t=4711)

模型：差動輸入電阻 $R_{id}$、受控源 $A_dv_{id}$、輸出電阻 $R_{od}$。輸出經 $R_2$、$R_1$ 回到**負端**（一定負端才是負回授），回授比例 $\beta = \frac{R_1}{R_1 + R_2}$（這個 $\beta$ 不是 BJT 的 $\beta$）。這是**電壓取樣、電壓相加**——電壓放大器。[▶ 1:21:07](https://youtu.be/Zwg7MGcYu4A?t=4867)

三個基本式（basic 3 equations）[▶ 1:22:40](https://youtu.be/Zwg7MGcYu4A?t=4960)：

$$
v_{id} = v_i - v_f,
\qquad
v_f = \beta v_o,
\qquad
v_o = A_dv_{id}
$$

消去：

$$
A_f = \frac{v_o}{v_i} = \frac{A_d}{1 + \beta A_d} \approx \frac1\beta = 1 + \frac{R_2}{R_1}
$$

增益少了 $1 + \beta A_d$ 倍。而 $v_f = \frac{\beta A_d}{1 + \beta A_d}v_i \approx v_i$：負端**跟著**正端走（虛短路）。[▶ 1:26:20](https://youtu.be/Zwg7MGcYu4A?t=5180)

---

## 8. 回授讓輸入電阻變大、輸出電阻變小

**輸入電阻** [▶ 1:27:22](https://youtu.be/Zwg7MGcYu4A?t=5242)：兩端電壓幾乎一樣 → $R_{id}$ 上幾乎沒電流：

$$
i_i = \frac{v_i - v_f}{R_{id}} = \frac{v_i}{(1 + \beta A_d)R_{id}}
\quad\Longrightarrow\quad
R_{if} = (1 + \beta A_d)R_{id}
$$

**輸出電阻** [▶ 1:32:09](https://youtu.be/Zwg7MGcYu4A?t=5529)：$v_i = 0$，從輸出加 $V_x$：受控源變成 $-\beta A_dV_x$，

$$
I_x = \frac{V_x - (-\beta A_dV_x)}{R_{od}} = \frac{(1 + \beta A_d)V_x}{R_{od}}
\quad\Longrightarrow\quad
R_{of} = \frac{R_{od}}{1 + \beta A_d}
$$

[▶ 1:35:23](https://youtu.be/Zwg7MGcYu4A?t=5723)

**意義** [▶ 1:37:28](https://youtu.be/Zwg7MGcYu4A?t=5848)：op amp 裡的東西都不穩定、跟溫度有關；回授後增益只靠電阻比。$R_{if}$ 很大 → 信號源內阻 $R_s$ 沒影響；$R_{of}$ 很小 → 負載 $R_L$ 沒影響。變成一個**理想的電壓放大器**（voltage-voltage amplifier）。【口頭】你負載小我照送，跟負載一點關係都沒有。[▶ 1:39:33](https://youtu.be/Zwg7MGcYu4A?t=5973)

---

## 9. 回授讓頻寬變寬

[▶ 1:42:09](https://youtu.be/Zwg7MGcYu4A?t=6129)

開迴路增益有頻寬：$A(\omega) = \dfrac{A_d}{1 + j\omega/\omega_0}$。代入 $\dfrac{A}{1 + \beta A}$，上下乘 $1 + j\omega/\omega_0$：

$$
A_f(\omega) = \frac{\dfrac{A_d}{1 + \beta A_d}}{1 + \dfrac{j\omega}{\omega_0(1 + \beta A_d)}}
$$

增益除 $1 + \beta A_d$、頻寬乘 $1 + \beta A_d$——兩個相乘不變，**增益頻寬積相同**，在同一點交 0 dB。[▶ 1:45:20](https://youtu.be/Zwg7MGcYu4A?t=6320)

信號頻率要在頻寬內，所以頻寬要比信號寬。回授後：增益穩定（跟溫度無關，電阻最好）、頻寬變寬、輸入電阻變大、輸出電阻變小——全部都是 $1 + \beta A_d$。[▶ 1:47:23](https://youtu.be/Zwg7MGcYu4A?t=6443)

> 【課本補充】§11.2 (p. 815)：負回授的性質——增益不敏感（desensitivity）、頻寬延伸 $\omega_{Hf} = \omega_H(1 + A_M\beta)$、抑制干擾、降低非線性失真。

---

## 10. 實際電路怎麼求 $A$、$R_i$、$R_o$：令 $\beta = 0$

[▶ 1:48:26](https://youtu.be/Zwg7MGcYu4A?t=6506)

實際題目直接解很難，要先求三個東西：$A_d$、$R_{id}$、$R_{od}$，然後代公式。

原則：**讓 $\beta = 0$**（沒有回授）——這就是「基本放大器」（basic amplifier）：[▶ 1:50:00](https://youtu.be/Zwg7MGcYu4A?t=6600)

- $R_{id}$：$\beta = 0$ 下的 $v_i/i_i$。
- $R_{od}$：$\beta = 0$、信號源為 0，從輸出看回去。
- $A_d$：$\beta = 0$ 下的 $v_o/v_i$。

求出來之後全部代 $1 + \beta A_d$ 的公式。實際怎麼讓 $\beta = 0$（又要保留回授網路的負載效應），下次看。[▶ 1:53:44](https://youtu.be/Zwg7MGcYu4A?t=6824)

> 【課本補充】§11.1 (p. 808)：一般回授結構 $A_f = \frac{A}{1 + A\beta}$，$A\beta$ 叫**迴路增益**（loop gain），$1 + A\beta$ 叫**回授量**（amount of feedback）。

---

## 11. 一頁速查表

| 項目 | 公式／重點 | 關鍵 |
|---|---|---|
| BJT 疊接 + 疊接鏡 | $R_{out} = \frac12\beta_3r_{o3}\parallel\beta_4r_{o4}$ | |
| Wilson 鏡 | 偏移 $\propto 1/\beta^2$；$R_{out} \approx \frac12\beta r_o$ | 小一個 $\beta$ |
| 三級 BJT op amp | 差動 → 差動 → 準位移動 → 射極隨耦 | 輸出直流 0 |
| 共模範圍 | 例 −9.1～5.5 V | |
| op amp 模型 | $R_{id} = 5$ k、$A_d \approx 1.8\times10^4$、$R_o \approx 109\ \Omega$ | |
| 基本三式 | $v_{id} = v_i - v_f$、$v_f = \beta v_o$、$v_o = A_dv_{id}$ | |
| 閉迴路增益 | $\frac{A_d}{1+\beta A_d} \approx \frac1\beta$ | |
| 輸入電阻 | $R_{if} = (1+\beta A_d)R_{id}$ | 電壓相加 |
| 輸出電阻 | $R_{of} = R_{od}/(1+\beta A_d)$ | 電壓取樣 |
| 頻寬 | $\omega_{0f} = \omega_0(1+\beta A_d)$ | 增益頻寬積不變 |
| 求法 | 令 $\beta = 0$ 求 $A_d$、$R_{id}$、$R_{od}$ | 基本放大器 |

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 令 $\beta = 0$ 的基本放大器 | 下一集：四種回授組態、負載效應 |
| 頻寬延伸 | 頻率響應、穩定度 |
| Wilson 鏡 | 高輸出電阻電流源 |

---

## 附：本集一句話總結

> **BJT 疊接 + 疊接電流鏡負載的輸出電阻是 $\frac12\beta r_o\parallel\beta r_o$，但基極電流讓輸出偏移，Wilson 電流鏡把偏移再縮小一個 $\beta$；三級 BJT op amp（差動、差動、準位移動、射極隨耦）增益約一萬八、輸入電阻 $2r_\pi$、輸出電阻約 109 Ω。接上負回授後，基本三式給出 $A_f = A_d/(1+\beta A_d) \approx 1/\beta$，輸入電阻乘、輸出電阻除、頻寬乘同一個 $1+\beta A_d$；實際電路先令 $\beta = 0$ 求出 $A_d$、$R_{id}$、$R_{od}$ 再代公式。**

---

## ⚠️ 待確認清單

1. 第 4 節三級 op amp 各級電阻值，需回影片看板書電路圖。

---

*筆記依據陳振芳老師「電子學（三）」112 學年度 Lec08 錄影逐字稿（whisper，1:56:02）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
