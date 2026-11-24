---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 05
lecture: Lecture 3 – Continuation of the GKR Protocol and Corollaries
date: 2023-09-29（依第 03 集課務說明推定）
video: https://youtu.be/gp21TApWetE
notes: Thaler §4.5.5（書頁 55–57，PDF 頁 56–58）、§4.6.6（書頁 66–67，PDF 頁 67–68）、§4.2 末段 IP = PSPACE（書頁 41–42，PDF 頁 42–43）。OCW 本講無指定讀物。
---

# 第 05 集 · Lecture 3：GKR 續——拿掉 add/mult 的 oracle、IP = PSPACE [▶ 影片](https://youtu.be/gp21TApWetE)

← 上一集：[04-doubly-efficient-ip-part2](04-doubly-efficient-ip-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[06-pcp-via-gkr-part1](06-pcp-via-gkr-part1.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 05 集
> **講者**：**Rachel Zhang**（代課；Kalai 這週在德國）
> **來源**：YouTube 錄影逐字稿（1:21:47，MIT 上傳的真人字幕）＋ Thaler §4.2、§4.5.5、§4.6.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：這堂課講得比較口語、板書很多看不到，學生提問也多（有些問題講者留到下課私下討論）。下面的構造照口述重建；講者自己說「我對細節講得很鬆」的地方，筆記也照實標出。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧 GKR](#1-回顧-gkr)
- [2. 問題：驗證者怎麼拿到 add̃、mult̃](#2-問題驗證者怎麼拿到-addmult)
- [3. 想法：改用萬用電路](#3-想法改用萬用電路)
  - [3.1 萬用電路 U](#31-萬用電路-u)
  - [3.2 U 的深度和大小](#32-u-的深度和大小)
  - [3.3 U 的 add、mult 很好算](#33-u-的-addmult-很好算)
- [4. 剩下兩個問題](#4-剩下兩個問題)
  - [4.1 問題一：輸入變大了 → 用 log-space uniform](#41-問題一輸入變大了--用-log-space-uniform)
  - [4.2 問題二：要的是擴張，不只是 0/1 值 → 算術化](#42-問題二要的是擴張不只是-01-值--算術化)
- [5. IP = PSPACE（用 GKR）](#5-ip--pspace用-gkr)
  - [5.1 定理與為什麼 Shamir 的版本不夠](#51-定理與為什麼-shamir-的版本不夠)
  - [5.2 組態圖的轉移矩陣](#52-組態圖的轉移矩陣)
  - [5.3 反覆平方](#53-反覆平方)
  - [5.4 套用 GKR](#54-套用-gkr)
  - [5.5 Q&A：小空間 → 淺電路](#55-qa小空間--淺電路)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | Thaler |
|---|---|
| 回顧 GKR | §4.6 |
| 拿掉 $\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$ 的 oracle：萬用電路＋log-space uniform＋算術化 | §4.6.6 |
| 用 GKR 證明 IP = PSPACE，而且證明者是 $\mathrm{poly}(2^S)$ | §4.5.5 |

---

## 1. 回顧 GKR

[▶ 00:13](https://youtu.be/gp21TApWetE?t=13)

- 電路 $C$，深度 $d$、大小 $S$。把每一層的閘值取低次擴張 $\tilde{V}_0, \ldots, \tilde{V}_d$。
- 用 sum-check 把上層的宣稱化簡成下層的宣稱（每層兩個，「二對二」），一路到輸入層，驗證者自己算。
- 證明者 $\mathrm{poly}(S)$；驗證者 $d\cdot\mathrm{polylog}(S) + n\cdot\mathrm{polylog}(S)$。

【Q&A】[▶ 03:05](https://youtu.be/gp21TApWetE?t=185) **用同一組隨機數怎麼讓宣稱一直保持兩個？**
不對兩個宣稱各用獨立的隨機數跑 sum-check，而是同時用同一組。sum-check 最後要查的點是驗證者的隨機數決定的，所以兩個 sum-check 最後要查的是同樣的點。

Rachel 把第 03 集的關鍵等式寫在黑板上留著用。學生問 $\tilde{\chi}$ 是什麼：一個每個變數次數 $|H| - 1$ 的多項式，在小方塊上測試 $p$ 和 $z$ 是否相等（相等是 1，否則 0），然後取它的低次擴張。

---

## 2. 問題：驗證者怎麼拿到 add̃、mult̃

[▶ 06:08](https://youtu.be/gp21TApWetE?t=368)

上次 GKR 假設驗證者有 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ 的 oracle。今天前半的目標：**拿掉這個 oracle**。

【課堂討論】Rachel 問大家有什麼想法：

1. 學生（Arnan）：用電路的簡短描述**算術化**，自己算。→ 今天就是這樣做，等一下會看到。
2. 我們已經會 GKR 了，就**再委託一次**：把算 $\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$ 也丟給證明者證明。→ 這是 GKR 原論文的做法，今天不講。

**重點**：今天算出來的**不是**標準的（唯一的）低次擴張，而是另一個「次數還算低」、在小方塊上值一樣的多項式。

- 【口頭】上次 Leo 問過能不能用別的低次多項式，答案是可以，今天就是應用。
- 第 03 集的 GKR 分析只用到「在 $H^m$ 上值正確」和「次數低」，不需要唯一的那個。

> 【課本補充】Thaler §4.6.6：對一般的 log-space uniform 電路，不知道怎麼找到能在 polylog 時間算出的 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ 低次擴張。GKR 原論文的做法是兩階段：先對「模擬小空間圖靈機的標準電路」（連線很規則，$\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$ 可在 $O(\log S)$ 時間算）給協定；再對一般電路，把算 $\widetilde{\mathrm{add}}_i(r_i, b^{*}, c^{*})$、$\widetilde{\mathrm{mult}}_i(r_i, b^{*}, c^{*})$ 外包出去（因為 $C$ 是 log-space uniform，這些可在對數空間算，所以第一階段的協定適用）。Thaler 也提到很多有重複結構的電路（矩陣乘法、FFT 等）可以直接在 $O(\log S)$ 時間算。

---

## 3. 想法：改用萬用電路

[▶ 08:21](https://youtu.be/gp21TApWetE?t=501)

$C$ 的 $\mathrm{add}$、$\mathrm{mult}$ 太複雜，驗證者算不動。**想法**：換一個**算同樣東西、但描述簡單**的電路來跑 GKR。「描述簡單」是指 $\mathrm{add}$、$\mathrm{mult}$ 很好算。

### 3.1 萬用電路 U

**萬用電路**（universal circuit）$U$：輸入是 $C$ 的描述 $\langle C\rangle$ 和 $x$，輸出 $C(x)$。它模擬 $C$ 在 $x$ 上的計算。

**$\langle C\rangle$ 是什麼**（[▶ 10:37](https://youtu.be/gp21TApWetE?t=637)）：對每個位置 $(j, k, k')$，記錄 $C$ 在那裡有沒有 ADD 閘、有沒有 MULT 閘，也就是 $C_{\mathrm{add}}$、$C_{\mathrm{mult}}$ 的真值表。

- ⚠️ 逐字稿缺字：[▶ 16:06](https://youtu.be/gp21TApWetE?t=966) Rachel 一開始說描述大小是 $2^S$，學生質疑後改成「就是 $S$」，另一位學生再指出應是 $S^3$（三個參數），Rachel 同意。所以 $|\langle C\rangle| = O(S^3)$。
- 【Q&A】$p, w_1, w_2$ 原本是在一層內的編號，這裡可以讓它們跑遍所有閘，記號改一下就好。
- 【Q&A】[▶ 12:00](https://youtu.be/gp21TApWetE?t=720) **輸入層的 NOT 怎麼辦？**（GKR 只有 ADD、MULT。）把 $x$ 和它的否定 $1 - x$ 都放進輸入就好。

**模擬一個閘**（[▶ 13:22](https://youtu.be/gp21TApWetE?t=802)）：$U$ 要算 $C$ 第 $i$ 層閘 $j$ 的值。它不知道 $j$ 的輸入是哪兩個，所以**看前一層所有可能的組合**：

$$V_i(j) = \sum_{k, k'}\left[ C_{\mathrm{add}}(j, k, k')\left( V_{i+1}(k) + V_{i+1}(k') \right) + C_{\mathrm{mult}}(j, k, k')\,V_{i+1}(k)\,V_{i+1}(k') \right].$$

$C_{\mathrm{add}}$、$C_{\mathrm{mult}}$ 從輸入 $\langle C\rangle$ 讀。這和 GKR 的式子本質上一樣，只是現在是**用閘實作出來**的電路。

### 3.2 U 的深度和大小

[▶ 17:27](https://youtu.be/gp21TApWetE?t=1047)

- 學生（Gabe）：$U$ 的深度 = $C$ 的深度 × 每個「模擬小電路」的深度。
- 【課堂討論】小電路的深度？學生答 $\log S$。上面的大總和可以排成一棵**二元加法樹**，葉子有 $\mathrm{poly}(S)$ 個，所以深度 $O(\log S)$（最差 polylog）。
- 大小：$C$ 的每個閘換成一個 $\mathrm{poly}(S)$ 大小的小電路，所以 $|U| = \mathrm{poly}(S)$。

| | $C$ | $U$ |
|---|---|---|
| 深度 | $d$ | $d\cdot O(\log S)$ |
| 大小 | $S$ | $\mathrm{poly}(S)$ |

### 3.3 U 的 add、mult 很好算

[▶ 19:37](https://youtu.be/gp21TApWetE?t=1177)

$U$ 的結構非常規則。給 $U$ 裡一個閘的位置，很容易判斷它是什麼：
- 在某棵二元加法樹裡 → ADD 閘；
- 在葉子 → 對應 $C$ 的某個閘乘某些值，看是乘還是加……

**Claim**：存在大小 $\mathrm{polylog}(S)$ 的布林公式 $\varphi_{\mathrm{add}}$、$\varphi_{\mathrm{mult}}$，輸入 $U$ 中三個閘的位置，輸出它們之間是不是 ADD（MULT）連線。

所以驗證者可以自己算（不用 oracle）。原本 $C$ 是 log-space uniform，算 $\mathrm{add}$ 可能要 $\mathrm{poly}(S)$ 時間，太多；現在公式只有 polylog 大小。

【Q&A】[▶ 22:24](https://youtu.be/gp21TApWetE?t=1344) **$U$ 本身是 log-space uniform 嗎？公式存在，但要不要 advice？**
Rachel：大概是「log log-space uniform」。學生認為只要算出第幾層、在萬用電路的哪個位置，就能寫出那個公式，不需要 advice。

**小結**：把 $\mathrm{add}$、$\mathrm{mult}$ 複雜的 $C$ 換成簡單的 $U$，對 $U(\langle C\rangle, x)$ 跑 GKR。輸出一樣是 $C(x)$。

---

## 4. 剩下兩個問題

[▶ 23:47](https://youtu.be/gp21TApWetE?t=1427)

1. **輸入變大了**（學生 Arnan 指出）：$U$ 的輸入多了 $\langle C\rangle$，大小 $\mathrm{poly}(S)$。GKR 最後驗證者要算**輸入的低次擴張**，得讀完整個輸入，變成 $\mathrm{poly}(S)$ 時間，「回到原點」。
   - 【Q&A】[▶ 25:36](https://youtu.be/gp21TApWetE?t=1536) 驗證者只要算輸入層的幾個位元嗎？不，要算擴張，就得知道全部。
2. **擴張**（學生 Nikon 指出）：公式只能算 $\mathrm{add}$、$\mathrm{mult}$ 在**方塊上**的 0/1 值，GKR 需要的是它們在 $\mathbb{F}$ 上的**擴張**。

Rachel：「老實說，希望就只有這兩個問題。」

### 4.1 問題一：輸入變大了 → 用 log-space uniform

[▶ 27:39](https://youtu.be/gp21TApWetE?t=1659)

**Log-space uniform**：$C$ 有一個長度 $O(\log S)$ 的簡短描述 $\hat{C}$，和一個固定的圖靈機 $M$：$M$ 讀 $\hat{C}$，用 $O(\log S)$ **空間**（但可能跑 $S$ 時間），輸出 $C$ 的任何一個閘（的描述）。

【Q&A】[▶ 29:09](https://youtu.be/gp21TApWetE?t=1749) **直覺上為什麼需要這個？排除了哪些電路？**
Rachel：驗證者總得有辦法知道 $C$ 是什麼，所以 $C$ 要有短描述。台下的「本地複雜度理論學家」（Ted）補充：不能把一個隨機字串之類的東西硬寫進電路裡。

**做法**（[▶ 30:34](https://youtu.be/gp21TApWetE?t=1834)）：再加一個電路 $M'$（把 $M$ 展開成電路），輸入 $\hat{C}$，輸出整個 $\langle C\rangle$，接到 $U$ 前面。

$$C'(\hat{C}, x) := U\left( M'(\hat{C}), x \right).$$

對 $C'$ 跑 GKR。現在**輸入只有 $\hat{C}$（$O(\log S)$）和 $x$（$n$）**。

【Q&A】[▶ 31:56](https://youtu.be/gp21TApWetE?t=1916) **把 $M$ 展開，它跑 $S$ 時間，電路不就深度 $S$？**
Rachel：其實可以做到深度 $O(\log S)$、大小 $\mathrm{poly}(S)$，而且 $\mathrm{add}$、$\mathrm{mult}$ 也很簡單——「不是我要說服你們，是你們下課前要說服我。」（答案在第 5 節：小空間計算可以變成淺電路。）

- 學生追問：輸出 $\langle C\rangle$ 需要 $|C|$ 份 $M$ 的副本嗎？可以這樣想，或想成 $M$ 有一個輸出帶。
- 學生問：$\hat{C}$ 是長度 $\log S$ 嗎？是，例如一族電路 $C_1, C_2, \ldots$，描述可以只是「印出第幾個」。

**成本**：

| | |
|---|---|
| $C'$ 大小 | $\mathrm{poly}(S)$ |
| $C'$ 深度 | $d\cdot O(\log S) + O(\log S)$，和原本差 log 因子 |
| 輸入長度 | $O(\log S) + n$ |
| 證明者 | $\mathrm{poly}(S)$ |
| 驗證者 | （深度）$\cdot\mathrm{polylog} + $（輸入長度）$\cdot\mathrm{polylog}$ |

【Q&A】[▶ 36:43](https://youtu.be/gp21TApWetE?t=2203) **中間那層寫著 $\langle C\rangle$，很大；GKR 中途要算它的擴張？**
那是**證明者**的事，驗證者不用。另一位學生補充：Kalai 把每層都補到 $S$ 個閘，所以層大小不一樣也沒關係，$S$ 可以看成每層大小的上界。

### 4.2 問題二：要的是擴張，不只是 0/1 值 → 算術化

[▶ 37:32](https://youtu.be/gp21TApWetE?t=2252)

**有的**：布林公式 $\varphi_{\mathrm{add}}, \varphi_{\mathrm{mult}}:\{0,1\}^{3\log S'}\to\{0,1\}$，大小 polylog（$S' = |C'|$）。
**要的**：$\widetilde{\mathrm{add}}, \widetilde{\mathrm{mult}}:\mathbb{F}^{3m}\to\mathbb{F}$，在 $H^{3m}$ 上正確、次數低（$m = \log_{|H|}S'$）。

【課堂討論】做 #SAT 時做了什麼？學生答：**算術化**。

**Step 1：把 $H$ 的元素轉成位元**（[▶ 41:40](https://youtu.be/gp21TApWetE?t=2500)）。$\varphi$ 吃的是位元，GKR 給的是 $H$ 的元素。每個 $h\in H$ 對應 $\log|H|$ 個位元（它的二進位寫法）。每個位元都可以寫成 $h$ 的一個**次數 $\le |H| - 1$ 的多項式**（用 Lagrange 插值：在 $H$ 上取那個位元的值，再擴張）。

**Step 2：算術化 $\varphi$**：AND → $ab$，OR → $a + b - ab$，NOT → $1 - a$。

- ⚠️ 逐字稿缺字：[▶ 43:03](https://youtu.be/gp21TApWetE?t=2583) Rachel 一開始把 AND 和 OR 的對應寫反，自己改正。

**Step 3：組合**：把 Step 1 的多項式代進算術化的 $\varphi$（多項式合成）。

**次數**：【課堂討論】學生答「$2^{\text{深度}}$」。Rachel 用第 02 集的引理：算術化公式的次數總和 $\le$ 葉子數。每片葉子再代進一個 $|H| - 1$ 次的多項式，所以

$$\deg \lesssim \log S'\cdot|H|$$

（講者寫成「底層的閘數 $\log S'$ 乘 $|H|$」）。比真正的低次擴張（每變數 $|H| - 1$）多一個 log 因子，但對驗證者來說夠用。

【口頭】Rachel 叫它「low **enough** degree extension」：不是唯一的低次擴張，但次數夠低。

【Q&A】[▶ 40:07](https://youtu.be/gp21TApWetE?t=2407) **低次擴張不是唯一的嗎？** 唯一的是「每變數次數 $\le |H| - 1$」的那個。這裡次數比較高，所以不是它，但「夠低」。

【Q&A】[▶ 44:42](https://youtu.be/gp21TApWetE?t=2682)～[▶ 52:14](https://youtu.be/gp21TApWetE?t=3134) 一位學生對「一個 $H$ 元素變成很多位元」很困惑：
- 若 $H = \{0, 1\}$，轉換就是恆等映射，直接代進去。
- 另一位學生：「你就是在說『算術化』，而且是決定性的，只是得到的不是那個唯一的低次擴張。」Rachel：對。
- Rachel 解釋：$(h_1, \ldots, h_m)\in H^m$ 和 $\{0,1\}^{\log S'}$ 之間是**一一對應**（二進位寫法），資訊量守恆，不會撞在一起。先把 $\varphi$ 算術化（已經是大體上的多項式），再把轉換多項式代進去，就是多項式合成。
- 學生仍有疑問，Rachel 提議休息時私下討論。

> 以下**不是逐字稿內容**，是依第 03 集的 GKR 分析推論的：GKR 的 soundness 只依賴兩件事：(1) 在 $H^m$ 上，$\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$ 等於真的 0/1 連線函數（所以關鍵等式成立）；(2) sum-check 裡的多項式每變數次數低（soundness 錯誤和次數成正比）。換成「次數高一個 log 因子」的擴張，只讓 sum-check 的錯誤和通訊多一個 polylog 因子。

---

## 5. IP = PSPACE（用 GKR）

### 5.1 定理與為什麼 Shamir 的版本不夠

[▶ 52:14](https://youtu.be/gp21TApWetE?t=3134)

【課堂討論】
- **IP**：有互動式證明的語言。證明者無限強，驗證者多項式時間（所以證明也只有多項式長）。學生一開始說「計算受限的證明者」，Rachel 更正為無限強。
- **PSPACE**：多項式空間圖靈機能判定的語言。

**IP ⊆ PSPACE**（簡單方向）：模擬所有可能的對話紀錄，做一些計數。不細講。

**PSPACE ⊆ IP**：Shamir 1992。合起來 IP = PSPACE。

**從委託計算的角度看**（[▶ 55:14](https://youtu.be/gp21TApWetE?t=3314)）：這等於說任何多項式空間計算都能委託給雲端，請它跑 Shamir 的協定證明給你看。為什麼還不夠？**證明者時間**：

| | 證明者時間（空間 $S$ 的計算） |
|---|---|
| 直接算 | $2^{S}$（空間 $S$ 的計算最多跑這麼久） |
| Shamir | $2^{S^2}$ |
| 可能有後續工作 | $2^{S\log S}$（⚠️ 待確認：Rachel 說她和 Kalai 都不記得出處，「可能錯」） |
| **今天（用 GKR）** | $\mathrm{poly}(2^{S})$ |

> **定理**：用 GKR（無條件成立，不是假設），可以得到 IP = PSPACE，而且證明者時間 $\mathrm{poly}(2^{S})$、驗證者 $\mathrm{poly}(S)$。

所以對最難的 PSPACE 計算（真的要 $2^S$ 時間的），有有效的委託協定，而且是資訊理論安全的證明。

**開放問題**（[▶ 57:21](https://youtu.be/gp21TApWetE?t=3441)）：一般的「時間 $T$、空間 $S$」計算（$T$ 不一定是 $2^S$），能不能有證明者 $\mathrm{poly}(T)$ 的互動式證明？Rachel 說據她所知未知。還可以問更強的：線性額外負擔、加性額外負擔……

> 【課本補充】Thaler §4.2 末段：IP ⊆ PSPACE 的證明是算出最佳證明者策略和它讓驗證者接受的機率，都可以在多項式空間做到（時間是指數）。PSPACE ⊆ IP：Shamir 把 #SAT 協定推廣到 PSPACE 完全的 TQBF，Shen 給了更簡單的證明。

### 5.2 組態圖的轉移矩陣

[▶ 58:51](https://youtu.be/gp21TApWetE?t=3531)

設圖靈機 $M$ 用空間 $S$、時間 $T = 2^{S}$。要判斷 $M$ 在 $T$ 步內會不會到達接受組態。

直接展開成電路，深度會是 $2^{S}$，太深。**目標：深度 $\mathrm{poly}(S)$。**

**組態**（configuration）：一個組態包含
- 帶子內容：$\{0,1\}^{S}$；
- 讀寫頭位置：$S$ 種；
- 圖靈機的內部狀態（【Q&A】學生提醒要包含，Rachel：「很好的一點」）。

組態總數 $N = 2^{O(S)}$。

**轉移矩陣** $A$（$N\times N$）：

$$A_{ij} = 1 \iff \text{組態 } i \text{ 一步之後變成組態 } j.$$

- 【Q&A】學生：每一列只有一個 1？對，因為圖靈機是決定性的。
- **關鍵**：$A$ 的每個元素**很好算**。給兩個組態，用一個很小、很規則（uniform）的公式就能檢查是否差一步。這就是需要把讀寫頭位置放進組態的原因：知道頭在哪，只要比對附近幾格。

### 5.3 反覆平方

[▶ 65:26](https://youtu.be/gp21TApWetE?t=3926)

**$A^2$ 的意思**：

$$(A^2)_{ij} = \sum_k A_{ik}A_{kj}.$$

$A_{ik}A_{kj} = 1$ 當且僅當 $i\to k\to j$。所以 $(A^2)_{ij} = 1$ 當且僅當 $i$ 兩步走到 $j$（決定性，最多一條路）。一般地：

$$(A^{T})_{ij} = 1 \iff i \text{ 恰好 } T \text{ 步走到 } j.$$

- 【Q&A】[▶ 67:38](https://youtu.be/gp21TApWetE?t=4058) **「恰好」$T$ 步？** 對。可以讓接受組態到了就停在原地（自己指向自己），或改矩陣讓它可以「浪費時間」。

所以只要算 $(A^{T})_{\mathrm{start}, \mathrm{accept}}$。

【課堂討論】怎麼算 $A^{T}$？一個一個乘要深度 $T$。學生答：**反覆平方**（repeated squaring）：

$$A \to A^2 \to A^4 \to A^8 \to \cdots \to A^{T}.$$

**深度**：$\log T = O(S)$ 次平方。每次平方是矩陣乘法，每個元素是 $N$ 項的和，排成二元樹深度 $\log N = O(S)$。總深度約 $O(S)\cdot O(S) = \mathrm{poly}(S)$。

**大小**：每次矩陣乘法 $N^3 = 2^{O(S)}$，總共 $\mathrm{poly}(2^{S})$。

- ⚠️ 逐字稿缺字：[▶ 69:43](https://youtu.be/gp21TApWetE?t=4183) 字幕寫「you do one division, one multiplication」，依上下文是「一次加法、一次乘法」（矩陣乘法的乘積和）。

最上面：讀出 (start, accept) 那個元素。

### 5.4 套用 GKR

[▶ 71:52](https://youtu.be/gp21TApWetE?t=4312)

【課堂討論】

| | |
|---|---|
| 證明者 | $\mathrm{poly}(2^{S})$（學生答） |
| 驗證者 | $\mathrm{poly}(S)$（學生答） |

「這就是我們要證的。」

【Q&A】[▶ 72:39](https://youtu.be/gp21TApWetE?t=4359) **平方的成本在哪？** 每次平方佔電路的一些深度；做法就是矩陣乘法（每一列乘每一行再加起來）。

【Q&A】[▶ 74:05](https://youtu.be/gp21TApWetE?t=4445) **4.1 那個「把 $M$ 展開成深度 $\log S$ 電路」的作業怎麼做？**
Rachel：用剛剛的邏輯（不准用 IP）。那是這個構造的**縮小版**：$M$ 用 $\log S$ 空間、$S$ 時間，把所有參數取 log：
- 深度：$\mathrm{poly}(\text{空間}) = \mathrm{poly}(\log S)$；
- 大小：$\mathrm{poly}(2^{\text{空間}}) = \mathrm{poly}(S)$。

講者說「depth log S」，嚴格說是 polylog。

【Q&A】[▶ 75:27](https://youtu.be/gp21TApWetE?t=4527) **輸入（起始組態）怎麼放進去？** Rachel 喜歡的想法：整個電路做完才讀輸入，最後只讀 (input 組態, accepting 組態) 那個元素。學生：所以幾乎整個電路都不讀輸入。Rachel：對，只有最後。

> 【課本補充】Thaler §4.5.5 用的是另一條路（更簡單）：直接對組態圖的 $A$ 跑**矩陣乘冪協定**（§4.5.3），不經過一般的 GKR。驗證者最後要算 $\tilde{f}_A$ 在一個隨機點的值；組態圖結構很規則（每步只讀寫 $O(1)$ 格、頭最多移一格），所以能在 $O(s\cdot m)$ 時間算。成本：回合與通訊 $O(s\log N)$、驗證者 $O(s\log N + ms)$、證明者 $\mathrm{poly}(N)$。$s = \mathrm{poly}(m)$ 時就重新得到 IP = PSPACE。Thaler 也說 GKR 原論文是建一個算 $A^{2^s}$ 的算術電路，再套 GKR（第 6.4 節），就是本集的做法。
>
> Thaler 註腳 55：組態圖除了停機狀態的自環外是無環的，所以 $A$ 的任何次方都只有 0/1，不用擔心 mod $p$ 溢位。

### 5.5 Q&A：小空間 → 淺電路

【Q&A】[▶ 77:29](https://youtu.be/gp21TApWetE?t=4649) **所以可以抽出一個一般的事實：小空間計算可以變成低深度電路？**
Rachel：對，這是個有趣的敘述，她也是最近才知道。原本「又高又瘦」的計算，可以變成「又胖又矮」的電路。

【Q&A】[▶ 78:10](https://youtu.be/gp21TApWetE?t=4690) 學生：$A$ 不是輸入，而是由 $M$ 決定、寫死在電路裡，所以輸入可以很小（只描述起始狀態）。Rachel：對，圖靈機 $M$ 是有限大小，放進去沒關係。另一位：所以不用擔心內部複雜的 $\mathrm{add}$、$\mathrm{mult}$，因為結構就長這樣。

【Q&A】[▶ 78:51](https://youtu.be/gp21TApWetE?t=4731) **幾乎整個電路都不依賴輸入，為什麼不直接把頂層硬寫進去？**
Rachel：「說出要怎麼算，比真的算出來容易。」頂層是 $|C|$ 那麼大的字串，不能硬寫。學生總結：我們之所以能這樣做，是因為假設了 $C$ 有 log-space 的簡短描述。

【Q&A】[▶ 80:12](https://youtu.be/gp21TApWetE?t=4812) **polylog-space uniform 也行嗎？**
Rachel 不確定，大概不行：轉移矩陣大小是 $2^{\text{空間}}$，空間變大就很糟。學生：空間 $S$ 會變成深度約 $S^2$。Rachel：但重點是證明者時間，那才是我們做這一切的原因。

提早下課。

---

## 6. 一頁速查表

### 拿掉 add̃、mult̃ 的 oracle

1. **萬用電路** $U(\langle C\rangle, x) = C(x)$。$V_i(j) = \sum_{k,k'}[C_{\mathrm{add}}(j,k,k')(V_{i+1}(k) + V_{i+1}(k')) + C_{\mathrm{mult}}(j,k,k')V_{i+1}(k)V_{i+1}(k')]$，用二元樹實作。
   - 深度 $d\cdot O(\log S)$，大小 $\mathrm{poly}(S)$。
   - $U$ 的 $\mathrm{add}$、$\mathrm{mult}$ 有 polylog 大小的布林公式。
2. **輸入太大**：$|\langle C\rangle| = O(S^3)$。用 log-space uniform：$C' = U(M'(\hat{C}), x)$，$|\hat{C}| = O(\log S)$，$M'$ 是把 $M$ 展開的淺電路。
3. **要擴張**：位元 = $h$ 的 $|H| - 1$ 次多項式；算術化 $\varphi$；合成。次數 $\approx|H|\cdot\log S'$（「夠低」，不是唯一的 LDE）。

### IP = PSPACE（證明者 $\mathrm{poly}(2^S)$）

- 組態數 $N = 2^{O(S)}$；$A_{ij} = [i \to j \text{ 一步}]$，每個元素小公式可算。
- $(A^{T})_{ij} = [i \to j \text{ 恰 } T \text{ 步}]$。關鍵一步：$(A^2)_{ij} = \sum_k A_{ik}A_{kj}$。
- 反覆平方：$\log T = O(S)$ 次，每次深度 $O(S)$ → 總深度 $\mathrm{poly}(S)$，大小 $\mathrm{poly}(2^S)$。
- GKR：證明者 $\mathrm{poly}(2^S)$，驗證者 $\mathrm{poly}(S)$。比 Shamir 的 $2^{S^2}$ 好。
- 縮小版：log-space $M$ → polylog 深度、poly 大小的電路。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 完整的 GKR（無 oracle） | 第 06–07 集：PCP via GKR |
| 「夠低」的擴張也能用 | 之後所有用低次多項式編碼的地方 |
| $|H| = \log S$ 的參數 | 第 06 集：PCP 要 $|\mathbb{F}| = \mathrm{poly}|H|$ |

---

## 附：本集一句話總結

> **驗證者算不動原電路的 $\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$，就改對「萬用電路＋從簡短描述展開的電路」跑 GKR：它的連線用 polylog 大小的公式描述，算術化後就是夠低次的擴張；同一個「小空間 → 淺電路（反覆平方組態矩陣）」的技巧，也直接給出證明者只要 $\mathrm{poly}(2^S)$ 的 IP = PSPACE。**

---

## ⚠️ 待確認清單

1. [▶ 55:57](https://youtu.be/gp21TApWetE?t=3357) 「可能有後續工作讓 PSPACE 的證明者時間降到 $2^{S\log S}$」：Rachel 自己說不記得出處、可能是錯的。

---

*筆記依據 Rachel Zhang 代課的「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 3 錄影逐字稿（MIT 真人字幕，1:21:47）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§4.2、§4.5.5、§4.6.6 整理。*
