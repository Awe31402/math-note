---
course: 電子學（四）（112 學年度）
episode: 12
lecture: Lec12 第十章 高功率輸出級 (8/8)
date: 112 學年度
video: https://www.youtube.com/watch?v=lE0Riev-pKk
notes: 老師第 10 章 = Sedra/Smith 7e Ch12、Ch14；§12.9 D 類 (p. 967)、§14.3 CMOS 反相器 (p. 1114)；本集的遲滯電流控制與死區時間電路課本沒有直接對應
---

# 第 12 集 · Lec12：大功率雷射驅動器——電流感測 + Schmitt 觸發器的遲滯電流控制、平均電流 $\approx V_R/(RA)$；CMOS 開關同時導通會燒掉，用 RC 延遲 + 邏輯閘做死區時間 [▶ 影片](https://www.youtube.com/watch?v=lE0Riev-pKk)

← 上一集：[11](11-lrc-response-pwm-dc-supply-bridge.md) ｜ [總目錄](../README.md) ｜ 下一集：（本課程最後一集）

> **課程**：電子學（四），陽明交大 電子物理系，112 學年度 — 第 12 集（Lec12）
> **講者**：陳振芳 老師
> **來源**：YouTube 錄影逐字稿（1:23:05，whisper）＋ Sedra & Smith《Microelectronic Circuits》7th ed.
> **標記說明**：`【口頭】` 老師口頭補充；`【課本補充】` 課本有、課堂沒講；`⚠️ 待確認` 查不清楚；`[▶ mm:ss]` 影片時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 雷射要的是電流](#1-雷射要的是電流)
- [2. 開機暫態與穩態](#2-開機暫態與穩態)
- [3. 感測電流：很小的電阻 + 放大 $A$](#3-感測電流很小的電阻--放大-a)
- [4. 遲滯電流控制：電流在天花板和地板之間](#4-遲滯電流控制電流在天花板和地板之間)
- [5. 天花板、地板與平均電流](#5-天花板地板與平均電流)
- [6. 數值例：1 V 給 10 A](#6-數值例1-v-給-10-a)
- [7. 控制雷射光強度](#7-控制雷射光強度)
- [8. CMOS 開關的大問題：同時導通](#8-cmos-開關的大問題同時導通)
- [9. 死區時間：RC 延遲 + OR／AND](#9-死區時間rc-延遲--orand)
- [10. CMOS 邏輯閘怎麼做](#10-cmos-邏輯閘怎麼做)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 整門課的收尾](#12-整門課的收尾)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

最後一個高功率電路：**大功率雷射驅動器**（high power laser driver）。然後補上 CMOS 開關的一個實際問題：上下兩顆不能同時導通。

---

## 1. 雷射要的是電流

[▶ 00:00](https://youtu.be/lE0Riev-pKk?t=0)

前面的 D 類可以給很大的電流，但它控制的是電壓。雷射要的是**電流**，而且要和雷射的負載 $R_L$ 無關。[▶ 01:03](https://youtu.be/lE0Riev-pKk?t=63)

架構：CMOS 反相器（開關）→ 電感 $L$ → 雷射（並一個電容 $C$）。PWM 的 0／5 V 經電感積分成電流。[▶ 02:04](https://youtu.be/lE0Riev-pKk?t=124)

---

## 2. 開機暫態與穩態

[▶ 03:07](https://youtu.be/lE0Riev-pKk?t=187)

假設開關一直接 5 V。$t = 0$：電容沒電荷、電感沒電流（$i_L = 0$）。電感兩端 5 V，電流開始上升、對電容充電；電容電壓上升後電感兩端的電壓差變小，電流就平下來。[▶ 07:13](https://youtu.be/lE0Riev-pKk?t=433)

穩態（和時間無關）：電容開路、電感短路 → $v_o = 5$ V，$I = 5/R_L$——和 $R_L$ 有關，不是我們要的。所以要加控制。[▶ 11:19](https://youtu.be/lE0Riev-pKk?t=679)

---

## 3. 感測電流：很小的電阻 + 放大 $A$

[▶ 12:53](https://youtu.be/lE0Riev-pKk?t=773)

比較器只能比電壓，所以要把電流轉成電壓：雷射下面串一顆**很小很小的電阻 $R$**（例 0.05 Ω，實際上是一整片薄片，不是一根電阻）。電壓很小，再放大 $A$ 倍：[▶ 13:26](https://youtu.be/lE0Riev-pKk?t=806)

$$
v_s = RA\cdot i
$$

送進 **Schmitt 觸發器**（兩個 level 的比較器，有天花板和地板），另一端接設定電壓 $V_R$。電壓圖和電流圖長得一樣，只差一個常數 $RA$。[▶ 15:27](https://youtu.be/lE0Riev-pKk?t=927)

---

## 4. 遲滯電流控制：電流在天花板和地板之間

[▶ 16:29](https://youtu.be/lE0Riev-pKk?t=989)

- 開關接 5 V：電流上升，$v_s$ 上升，一直到碰到**天花板**。[▶ 18:02](https://youtu.be/lE0Riev-pKk?t=1082)
- 比較器翻轉 → 開關接 0（中間經反相器，不需要很大的 $k$）→ 電流開始下降（斜率 $-v_o/L$）。同時門檻變成**地板**。[▶ 20:36](https://youtu.be/lE0Riev-pKk?t=1236)
- 電流降到地板 → 又翻回 5 V → 上升……

電流就在 $I_{\text{ceil}} = \frac{V_{\text{ceil}}}{RA}$ 和 $I_{\text{floor}} = \frac{V_{\text{floor}}}{RA}$ 之間來回，是一個三角波。【口頭】關鍵就是一定要有天花板和地板（Schmitt 觸發器）。[▶ 25:48](https://youtu.be/lE0Riev-pKk?t=1548)

一樣：$(5 - v_o)T_1 = v_oT_2$ → $v_o = 5D$——PWM 的平均值。電流 = 平均值 + 平均為 0 的三角波；LC 讓它們分開，雷射拿到平均電流。[▶ 32:34](https://youtu.be/lE0Riev-pKk?t=1954)

---

## 5. 天花板、地板與平均電流

[▶ 27:22](https://youtu.be/lE0Riev-pKk?t=1642)

Schmitt 觸發器用 $R_1$、$R_2$ 正回授，$\beta = \frac{R_1}{R_1 + R_2}$（通常取很小，例 1/10）：

$$
V_{\text{ceil}} = V_R(1 - \beta) + 5\beta,
\qquad
V_{\text{floor}} = V_R(1 - \beta)
$$

平均電流 = 天花板和地板的一半：[▶ 36:09](https://youtu.be/lE0Riev-pKk?t=2169)

$$
I_{avg} = \frac{I_{\text{ceil}} + I_{\text{floor}}}{2}
= \frac{V_R(1 - \beta) + 2.5\beta}{RA}
\approx \frac{V_R}{RA}
\quad(\beta \ll 1)
$$

雷射電流**只由 $V_R$ 決定**，和雷射的負載無關。[▶ 39:47](https://youtu.be/lE0Riev-pKk?t=2387)

> ⚠️ 待確認：天花板、地板的式子是依逐字稿「讓這裡等於 0 先算 $R_2$ 那項」的口述整理，$V_R$ 接哪一端（係數 $1-\beta$）需看板書確認。

---

## 6. 數值例：1 V 給 10 A

[▶ 40:20](https://youtu.be/lE0Riev-pKk?t=2420)

$R = 0.05\ \Omega$、$A = 2$ → $RA = 0.1\ \Omega$。$V_R = 1$ V：

$$
I_{avg} = \frac{1\ \text{V}}{0.1\ \Omega} = 10\ \text{A}
$$

雷射負載在這個時間點例如 0.2 Ω → 雷射電壓 2 V → PWM 佔空比自動變成 $\frac25$。[▶ 50:05](https://youtu.be/lE0Riev-pKk?t=3005)

限制：雷射上的電壓不能超過 5 V（電源），要在 0～5 V 之間 PWM 才能正常運作。[▶ 42:54](https://youtu.be/lE0Riev-pKk?t=2574)

> ⚠️ 待確認：逐字稿說「0.05 乘 20 大概就是 0.1」，放大倍數 $A$ 是 2 還是 20 不清楚；依 $V_R = 1$ V 得 10 A，$RA = 0.1\ \Omega$ 這點一致。

---

## 7. 控制雷射光強度

[▶ 51:07](https://youtu.be/lE0Riev-pKk?t=3067)

只要 $V_R$ 不變，電流就不變。光和電流成正比，要控制雷射光強度就是控制電流 → 改 $V_R$：把 $V_R$ 升到 2 V 就 20 A；在某個時間把 $V_R$ 提高，天花板、地板一起往上移，電流跟著上去；降下來也一樣。[▶ 52:38](https://youtu.be/lE0Riev-pKk?t=3158)

這整套就是 laser driver。【口頭】這麼大的雷射看你做什麼，有時候是打骨頭的；實際使用還要加保護電路（protection circuit）。這個電路也是在做積分——把差值積分。[▶ 54:45](https://youtu.be/lE0Riev-pKk?t=3285)

---

## 8. CMOS 開關的大問題：同時導通

[▶ 56:48](https://youtu.be/lE0Riev-pKk?t=3408)

CMOS 反相器當開關：大電流流過時沒有壓差，所以沒有功率消耗——這是它的特色。[▶ 57:18](https://youtu.be/lE0Riev-pKk?t=3438)

但輸入從 0 上升到 5 V 總要一段時間。上升的過程中，NMOS 已經開始導通、PMOS 還沒關掉——**兩顆同時導通**。$k$ 很大、$R_{DS}$ 很小，5 V 直接經兩顆很小的電阻接到地：[▶ 59:50](https://youtu.be/lE0Riev-pKk?t=3590)

$$
I = \frac{5\ \text{V}}{2R_{DS}}\ \text{非常大}
$$

這麼大的電流乘 5 V，直接**燒壞**。所以上下兩顆不能在同一個時間切換：要先讓一顆 off，延遲一段時間，另一顆才 on。[▶ 1:01:23](https://youtu.be/lE0Riev-pKk?t=3683)

---

## 9. 死區時間：RC 延遲 + OR／AND

[▶ 1:04:30](https://youtu.be/lE0Riev-pKk?t=3870)

兩個閘極分開驅動，各自要有一段時間延遲（死區時間，dead time）：

1. 輸入 $v_A$ 經 RC 充放電得到慢一點的 $v_B$（上升、下降都要一段時間，過一半才算高／低）。[▶ 1:05:32](https://youtu.be/lE0Riev-pKk?t=3932)
2. $v_A$、$v_B$ 進 **OR 閘**：只要一個高就高 → 上升時馬上高、下降時要等兩個都低才低（**晚關**）。[▶ 1:07:06](https://youtu.be/lE0Riev-pKk?t=4026)
3. $v_A$、$v_B$ 進 **AND 閘**：只要一個低就低 → 下降時馬上低、上升時要等兩個都高才高（**晚開**）。[▶ 1:09:45](https://youtu.be/lE0Riev-pKk?t=4185)

一個送 PMOS、一個送 NMOS：上升時保證 PMOS 先 off，NMOS 才 on；下降時 NMOS 先 off，PMOS 才 on。中間有一段兩顆都 off 的時間。[▶ 1:11:47](https://youtu.be/lE0Riev-pKk?t=4307)

> 以下**不是逐字稿內容**，是依電路功能推論的：實務上這叫「非重疊閘極驅動」（non-overlapping gate drive），死區時間由 RC 時間常數決定；死區期間電感電流會經 MOS 的本體二極體續流。

---

## 10. CMOS 邏輯閘怎麼做

[▶ 1:12:51](https://youtu.be/lE0Riev-pKk?t=4371)

CMOS 閘：下面 NMOS、上面 PMOS。**NMOS 並聯、PMOS 串聯**（或相反），一定要互補，不然會同時導通短路。[▶ 1:13:22](https://youtu.be/lE0Riev-pKk?t=4402)

- NMOS 並聯 + PMOS 串聯 → 任一輸入高，輸出就被拉到地：這是 **NOR**（OR 再反相）。再接一個反相器才是 **OR**。[▶ 1:16:28](https://youtu.be/lE0Riev-pKk?t=4588)
- NMOS 串聯 + PMOS 並聯 → **NAND**；再反相才是 **AND**。[▶ 1:20:03](https://youtu.be/lE0Riev-pKk?t=4803)

【口頭】這些邏輯閘不是用來拉電流的，用一般小 $k$ 的 MOS 就好，不會有剛剛那種大電流燒壞的問題（切換瞬間的短路電流很小）。[▶ 1:18:01](https://youtu.be/lE0Riev-pKk?t=4681)

前面加了這個延遲電路，整個才完整，沒有它會燒壞。[▶ 1:22:09](https://youtu.be/lE0Riev-pKk?t=4929)

> 【課本補充】§14.3 (p. 1114)：CMOS 邏輯閘的上拉網路（PUN，PMOS）和下拉網路（PDN，NMOS）互為對偶——PDN 並聯則 PUN 串聯。

---

## 11. 一頁速查表

| 項目 | 公式／重點 | 例 |
|---|---|---|
| 開機穩態 | $C$ 開路、$L$ 短路，$I = 5/R_L$ | 與負載有關，不要 |
| 電流感測 | 小電阻 $R$ × 放大 $A$ | $RA = 0.1\ \Omega$ |
| 遲滯控制 | 電流在 $I_{\text{ceil}}$、$I_{\text{floor}}$ 間來回 | Schmitt |
| 平均電流 | $\frac{V_R(1-\beta) + 2.5\beta}{RA} \approx \frac{V_R}{RA}$ | 1 V → 10 A |
| 佔空比 | 自動 = $v_{\text{laser}}/5$ | 0.2 Ω：2/5 |
| 光強控制 | 改 $V_R$ | |
| 同時導通 | $5/(2R_{DS})$ 燒壞 | |
| 死區時間 | RC 延遲 + OR（晚關）+ AND（晚開） | |
| CMOS 閘 | NMOS 並 + PMOS 串 = NOR；反之 NAND | 再反相得 OR／AND |

---

## 12. 整門課的收尾

| 觀念 | 出處 |
|---|---|
| 頻率響應、Miller、補償 | [E4-01](01-low-frequency-coupling-caps-miller-intro.md)～[E4-05](05-compensation-phase-margin-output-power-intro.md) |
| A／B／AB 類輸出級 | [E4-06](06-follower-loading-class-a-b-ab-protection.md) |
| 741、穩壓 IC | [E4-07](07-ic-power-amp-regulator-741-bias.md)、[E4-08](08-741-dc-bias-gain-cmrr-offset.md) |
| D 類、PWM、交換式電源 | [E4-09](09-class-d-pwm-schmitt-inverter-lc-filter.md)～[E4-11](11-lrc-response-pwm-dc-supply-bridge.md) |

---

## 附：本集一句話總結

> **大功率雷射驅動器用 CMOS 開關 + LC，但要控制的是電流：用一片很小的電阻感測電流、放大 $A$ 倍送進 Schmitt 觸發器，電流就在天花板與地板之間來回，平均電流 $\approx V_R/(RA)$（例 1 V → 10 A），和雷射負載無關、佔空比自動調整，改 $V_R$ 就控制光強度；CMOS 開關切換的瞬間上下兩顆會同時導通、$5/(2R_{DS})$ 的電流直接燒掉，所以要用 RC 延遲加 OR、AND 閘做出死區時間，讓一顆先關、另一顆才開。**

---

## ⚠️ 待確認清單

1. 第 5 節天花板、地板式子中 $V_R$ 的係數。
2. 第 6 節放大倍數 $A$ 是 2 還是 20。

---

*筆記依據陳振芳老師「電子學（四）」112 學年度 Lec12 錄影逐字稿（whisper，1:23:05）與 Sedra & Smith《Microelectronic Circuits》7th ed. 整理。*
