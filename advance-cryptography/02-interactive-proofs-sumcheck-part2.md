---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 02
lecture: Lecture 1 (Part 2) – Interactive Proofs and the Sum-Check Protocol
date: 待補（2023 秋季第一堂課，後半）
video: https://youtu.be/SRY3F9vtJHo
notes: Thaler §3.3（public coin，書頁 25–26，PDF 頁 26–27）、§4.2（書頁 39–42，PDF 頁 40–43）、§4.3（書頁 42–44，PDF 頁 43–45）、§3.5（書頁 28–30，PDF 頁 29–31）
---

# 第 02 集 · Lecture 1 (Part 2)：#SAT ∈ IP、雙重有效證明、低次擴張 [▶ 影片](https://youtu.be/SRY3F9vtJHo)

← 上一集：[01-interactive-proofs-sumcheck-part1](01-interactive-proofs-sumcheck-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[03-doubly-efficient-ip-part1](03-doubly-efficient-ip-part1.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 02 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:06:11，MIT 上傳的真人字幕）＋ Thaler《Proofs, Arguments, and Zero-Knowledge》§3.3、§3.5、§4.2、§4.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：黑板內容看不到，公式照口述重建並和 Thaler 對過。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Sum-check 是 public-coin 協定](#1-sum-check-是-public-coin-協定)
  - [1.1 證明者需要隨機嗎](#11-證明者需要隨機嗎)
  - [1.2 如果證明者事先知道 t₁](#12-如果證明者事先知道-t₁)
- [2. Soundness 的幾何直覺](#2-soundness-的幾何直覺)
- [3. #SAT ∈ IP](#3-sat--ip)
  - [3.1 問題：布林公式有幾個滿足賦值](#31-問題布林公式有幾個滿足賦值)
  - [3.2 算術化](#32-算術化)
  - [3.3 次數的界：Σ deg_i ≤ s](#33-次數的界σ-deg_i--s)
  - [3.4 成本與 soundness](#34-成本與-soundness)
  - [3.5 Q&A：體的特徵要多大、電路版 #SAT](#35-qa體的特徵要多大電路版-sat)
- [4. 雙重有效互動式證明](#4-雙重有效互動式證明)
- [5. 例子：數圖裡的三角形](#5-例子數圖裡的三角形)
- [6. 低次擴張（預告）](#6-低次擴張預告)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/SRY3F9vtJHo?t=0)

第一堂課的後半。講者先問大家速度（閉眼投票，結果是「Good」），然後：

| 主題 | Thaler |
|---|---|
| Sum-check 是 public-coin 協定；soundness 的幾何直覺 | §3.3 |
| 用 sum-check 證明 #SAT ∈ IP（算術化） | §4.2 |
| 雙重有效互動式證明的定義 | §4.3 開頭 |
| 數三角形：把圖寫成總和 | §4.3 |
| 低次擴張定理（只講敘述，證明下次） | §3.5 |

---

## 1. Sum-check 是 public-coin 協定

[▶ 00:45](https://youtu.be/SRY3F9vtJHo?t=45)

【口頭】上次忘了講的一個性質，之後會用到：

在 sum-check 裡，證明者送低次多項式，**驗證者只送隨機的體元素**（每輪 $\log|\mathbb{F}|$ 個隨機位元）。它不藏任何東西、不保留狀態。

> **Public-coin 協定**（公開硬幣協定）：驗證者的每一則訊息都只是**均勻隨機的位元**，擲完就公開送給證明者。

為什麼重要：之後可以用**密碼學把互動拿掉**（Fiat–Shamir，第 10 集起）。這招只對 public-coin 協定有用。

【Q&A】[▶ 04:10](https://youtu.be/SRY3F9vtJHo?t=250) **Public coin 是說證明者看得到這些位元嗎？**
證明者**事先**永遠看不到。如果在說話前就看到硬幣，他就能作弊。public coin 的意思是：驗證者擲了硬幣就直接送出，不對自己藏任何東西。

> 【課本補充】Thaler §3.3：一般 IP 的驗證者隨機性是**私有的**（private coin）。Goldwasser–Sipser [GS86] 證明 private coin 都能用 public coin 模擬（驗證者成本多項式放大、回合數稍增）。Thaler 書裡的 IP 本來就都是 public coin。

### 1.1 證明者需要隨機嗎

【Q&A】[▶ 02:07](https://youtu.be/SRY3F9vtJHo?t=127) **有沒有證明者也用隨機的協定？**

在這裡，證明者用隨機**沒有幫助**：

- 我們不信任的是證明者；驗證者永遠誠實。
- 證明者的硬幣可以**固定成最好的那一組**，直接寫死在他身上。這樣他就變成一個非一致（non-uniform）的機器（一個電路），而不是隨機機器。
- 驗證者需要隨機，是因為證明者送多項式時**不能知道**驗證者會問哪個 $t$。

證明者的隨機什麼時候有用？**要藏東西的時候**，也就是零知識證明（第 10–11 集）。

### 1.2 如果證明者事先知道 t₁

【Q&A】[▶ 05:45](https://youtu.be/SRY3F9vtJHo?t=345) **如果證明者事先知道所有隨機數會怎樣？**

他就能作弊，而且**只要知道 $t_1$ 就夠了**：

1. 宣稱總和是 $\beta$（假的）。
2. 找一個單變數多項式 $g_1$，滿足 $\sum_{h\in H} g_1(h) = \beta$，而且 $g_1(t_1) = s_1(t_1)$（和真的多項式在 $t_1$ 相等）。
3. 這樣化簡後的新宣稱 $\sum f(t_1, h_2, \ldots, h_m) = g_1(t_1)$ 是**真的**。之後一路誠實就好。

> 以下**不是逐字稿內容**，是依線性代數推論的：這樣的 $g_1$ 一定找得到。令 $g_1 = s_1 + c\cdot q$，其中 $q$ 是 $\le d$ 次、$q(t_1) = 0$、$\sum_{h\in H} q(h)\neq 0$ 的多項式（例如 $q(X) = X - t_1$，只要 $\sum_{h\in H}(h - t_1)\neq 0$），再調 $c$ 讓總和變成 $\beta$。

---

## 2. Soundness 的幾何直覺

[▶ 07:13](https://youtu.be/SRY3F9vtJHo?t=433)

【口頭】下課時一位學生（Chima）問的問題，講者給一個幾何解釋：

- 小方塊 $H^m$ 放在大空間 $\mathbb{F}^m$ 裡。要證明 $f$ 在小方塊所有點上的總和是 $\beta$。
- 如果宣稱是假的，把第一維固定在 $h_1$、$h_2$、……。總和是假的，代表**某一片**（某個 $h$）上的部分總和是假的。不知道是哪一片。
- 用糾錯性：「某一片是假的」⟹ 在**隨機點 $t_1$** 上，剩下 $m-1$ 維的總和高機率也是假的。現在忘掉原來的總和，只看 $t_1$ 這一片。
- 同樣的道理跳到 $t_2$、$t_3$……，每次往下一個維度，直到落在一個隨機點 $(t_1, \ldots, t_m)$，在那裡直接查 $f$。

---

## 3. #SAT ∈ IP

[▶ 08:41](https://youtu.be/SRY3F9vtJHo?t=521)

【口頭】「我給的例子都不只是例子，是特別設計來教東西的。不要想『喔是例子，忘掉』。」

### 3.1 問題：布林公式有幾個滿足賦值

[▶ 10:07](https://youtu.be/SRY3F9vtJHo?t=607)

- **布林公式**（Boolean formula）$\varphi$：$n$ 個變數，一棵**二元樹**。內部節點是 AND 或 OR，葉子是 $x_i$ 或 $\neg x_i$。同一個變數可以在很多葉子出現。
- **大小** $s$ = 葉子數（差不多是閘的數目，最多差 2 倍）。
- **#SAT**：$(\varphi, k)\in\#\mathrm{SAT}$ 當且僅當
$$\left| \left\{ x\in\{0,1\}^n : \varphi(x) = 1 \right\} \right| = k.$$

**公式 vs. 電路**（[▶ 12:23](https://youtu.be/SRY3F9vtJHo?t=743)）：

- 公式是樹：一個值要用兩次，就得**算兩次**。
- 電路（circuit）是任意的有向無環圖（DAG）：中間結果可以重複使用。
- 電路版的問題叫 #Circuit-SAT，是另一個問題（見 3.5）。

【口頭】#SAT 被認為非常難（你怎麼知道一個公式有幾個滿足賦值？）。所以能給它一個互動式證明很驚人，而且這個證明**就只是 sum-check**。

### 3.2 算術化

[▶ 13:43](https://youtu.be/SRY3F9vtJHo?t=823)

Sum-check 需要多項式，但 $\varphi$ 只是布林公式。方法叫**算術化**（arithmetization）：選一個很大的有限體 $\mathbb{F}$（大到 soundness 夠好），把每個閘換成 $\mathbb{F}$ 上的算術運算：

| 布林閘 | 算術化 | 檢查 $\{0,1\}$ 上相同 |
|---|---|---|
| $\mathrm{AND}(x, y)$ | $x\cdot y$ | 任何數乘 0 是 0，$1\cdot 1 = 1$ |
| $\mathrm{OR}(x, y)$ | $x + y - x\cdot y$ | 【課堂討論】學生先答 $x + y$，講者補：兩個都是 1 時會變 2，所以減 $xy$ |
| $\mathrm{NOT}(x)$ | $1 - x$ | 【課堂討論】學生答出 |

每個閘最多變成 3 個算術閘，所以大小只放大常數倍。

記算術化後的多項式為 $\tilde{\varphi}:\mathbb{F}^n\to\mathbb{F}$。

【Q&A】[▶ 18:15](https://youtu.be/SRY3F9vtJHo?t=1095) **OR 變成 $x + y - xy$ 後 $x$、$y$ 各用了兩次，這樣就不是樹了，沒關係嗎？**
沒關係。我們只需要**一開始**是公式（用來證次數的界）。算術化之後中間長怎樣不重要。講者謝謝學生指出這點。

【課堂討論】[▶ 18:58](https://youtu.be/SRY3F9vtJHo?t=1138) 講者問：現在要跑什麼 sum-check？學生答：把 $f$ 換成 $\tilde{\varphi}$。也就是證明

$$\sum_{(b_1, \ldots, b_n)\in\{0,1\}^n} \tilde{\varphi}(b_1, \ldots, b_n) = k.$$

**為什麼這就是對的宣稱**（[▶ 21:52](https://youtu.be/SRY3F9vtJHo?t=1312)）：在 $\{0,1\}^n$ 上，算術化的閘和 AND、OR、NOT 完全一樣，所以 $\tilde{\varphi}(x) = \varphi(x)$ 對所有 $x\in\{0,1\}^n$。在 $\{0,1\}$ 之外它是什麼值都無所謂。

這裡 $H = \{0, 1\}$，$m = n$。剩下只要確認次數 $d$ 夠小。

### 3.3 次數的界：Σ deg_i ≤ s

[▶ 20:24](https://youtu.be/SRY3F9vtJHo?t=1224)

> **Claim**：$\displaystyle\sum_{i=1}^{n}\deg_i(\tilde{\varphi}) \le s$，其中 $\deg_i$ 是變數 $x_i$ 的次數，$s$ 是 $\varphi$ 的葉子數。

特別地，每個變數的次數都 $\le s$。$s$ 是輸入大小，是多項式，所以夠小。

**證明**（對公式的深度歸納；**真的用到 $\varphi$ 是樹**）：

- **基底**：只有一片葉子 $x_i$ 或 $\neg x_i$。算術化是 $x_i$ 或 $1 - x_i$，次數總和 $= 1 = s$。
  - 講者口述的基底是「只有一個閘」，次數是 1。
- **歸納**：$\varphi = \varphi_1 \wedge \varphi_2$ 或 $\varphi_1 \vee \varphi_2$，大小分別是 $s_1$、$s_2$。
  - 因為是樹，兩棵子樹的葉子不重疊：$s = s_1 + s_2$。
  - AND：$\tilde{\varphi} = \tilde{\varphi}_1\cdot\tilde{\varphi}_2$。相乘時次數相加：
$$\deg_i(\tilde{\varphi}) \le \deg_i(\tilde{\varphi}_1) + \deg_i(\tilde{\varphi}_2).$$
  - OR：$\tilde{\varphi} = \tilde{\varphi}_1 + \tilde{\varphi}_2 - \tilde{\varphi}_1\tilde{\varphi}_2$。最高次的是乘積項，同樣的不等式成立。
  - 對 $i$ 加總，用歸納假設：
$$\sum_i \deg_i(\tilde{\varphi}) \le \sum_i \deg_i(\tilde{\varphi}_1) + \sum_i \deg_i(\tilde{\varphi}_2) \le s_1 + s_2 = s. \qquad\blacksquare$$

> 為什麼電路不行：電路裡一個子電路可以被用很多次，次數會一層一層**相乘**（例如連續平方 $k$ 次得到 $2^k$ 次），不再受葉子數控制。

> 【課本補充】Thaler §4.2 註腳 47 用同樣的歸納法證明這個 claim。

### 3.4 成本與 soundness

[▶ 28:29](https://youtu.be/SRY3F9vtJHo?t=1709)

對 $\tilde{\varphi}$ 跑 sum-check（$m = n$、$d\le s$、$H = \{0,1\}$）：

| 項目 | 結果 |
|---|---|
| Completeness | 1 |
| Soundness 錯誤 | $\le n\cdot s/|\mathbb{F}|$ |
| 驗證者時間 | 約 $n\cdot s\cdot\mathrm{polylog}|\mathbb{F}|$，加上最後自己算一次 $\tilde{\varphi}(t_1, \ldots, t_n)$（逐閘算，$O(s)$） |
| 證明者時間 | 指數，至少 $2^n$（【口頭】他總得數出有幾個滿足賦值） |

所以只要選 $|\mathbb{F}|\gg n\cdot s$ 來算術化。需要的話再重複來降低錯誤。

注意：這裡驗證者**不需要 oracle**，因為 $\tilde{\varphi}$ 有一個大小 $O(s)$ 的算術電路，自己就能算。

> 【課本補充】Thaler §4.2 用 $\sum_i\deg_i\le S$ 直接得到更緊的界：soundness 錯誤 $\le S/|\mathbb{F}|$（而不是 $nS/|\mathbb{F}|$），通訊 $O(S)$ 個體元素，驗證者 $O(S)$，證明者 $O(S^2\cdot 2^n)$（Table 4.2）。建議 $|\mathbb{F}|\ge S^4$，錯誤就 $\le 1/S^3$。
>
> 關鍵一步：sum-check 的錯誤其實是 $\sum_i \deg_i/|\mathbb{F}|$（每輪 $\deg_i/|\mathbb{F}|$ 再 union bound），講者用的 $m\cdot d$ 是它的上界。

### 3.5 Q&A：體的特徵要多大、電路版 #SAT

【Q&A】[▶ 29:57](https://youtu.be/SRY3F9vtJHo?t=1797) **sum-check 的加法一定是在那個體裡做嗎？**
這個問題本身沒有體：#SAT 只有 0、1 和 AND、OR。**體是我自己挑的**，為了能跑 sum-check。一般的 sum-check 問題，所有東西都在給定的體裡算；如果體不夠大（不夠遠大於 $md$），就換到擴張體 $\mathrm{GF}(p^n)$，成本只多 $n$ 的多項式（線性）倍。

【Q&A】[▶ 32:42](https://youtu.be/SRY3F9vtJHo?t=1962) **如果 $k$ 比體還大怎麼辦？**
選一個比 $k$ 大很多的體。學生指出：要的是**特徵**（characteristic）大，也就是質數 $p$ 本身要大。只把 $p$ 升到 $n$ 次方的擴張體不行，因為加法還是 mod $p$，而 $k$ 可能大到 $2^n$。

講者同意：選 $\mathrm{GF}(p)$，$p$ 是大質數，比 $k$ 大。驗證者時間只和 $\log|\mathbb{F}|$ 有關，所以 $p\approx 2^n$ 也沒問題。

【課堂討論】能不能用小特徵？講者說不確定，也許可以用**中國剩餘定理**（Chinese remainder theorem）：在很多個小質數上各跑一次，確認答案 mod 每個質數都對。學生們討論：計算量可能比較小（很多個小體的 $\log$ 的立方加起來，對比一個大體的 $\log$ 的立方），而且可以平行。講者沒有下結論。

> 【課本補充】Thaler §4.2 註腳 46：在大小 $p$ 的質數體上，$\sum g(x)$ 等於滿足賦值個數 **mod $p$**。最簡單的修法是選 $p > 2^n$；這樣的體元素仍可用多項式時間寫下和運算。

【Q&A】[▶ 34:07](https://youtu.be/SRY3F9vtJHo?t=2047) **這是做 #SAT 唯一簡單的方法嗎？**
講者認為這是最簡單的。接著講電路版：

- **#Circuit-SAT**：一樣數滿足賦值，但給的是電路（DAG）。它也在 IP 裡，因為它在 PSPACE 裡（逐一列舉 $x$，用小空間檢查），而 IP = PSPACE。
- 但直接算術化後**次數不小**，不能直接套 sum-check。要用 **degree reduction**（降次）技巧，這就是 Shamir 證明 IP = PSPACE 時讓事情變複雜的地方。
- #SAT（公式）次數一開始就很低，所以很漂亮。
- 【口頭】「你們應該要感恩一點。」（where's the gratitude?）

【Q&A】[▶ 35:27](https://youtu.be/SRY3F9vtJHo?t=2127) **給另一個問題（例如 permanent），能不能不先歸約到 #SAT、直接設計協定？**
講者：她知道的 IP 協定幾乎都走 sum-check。一位學生提到有一篇奇特的論文，原本想做 BPP 的資訊理論驗證、失敗了，卻用一個量子問題得到 #P ∈ IP，用的東西「有點像 sum-check」。講者說她不熟。
- ⚠️ 逐字稿缺字：論文作者名字聽不清楚（見待確認清單）。

【Q&A】[▶ 36:59](https://youtu.be/SRY3F9vtJHo?t=2219) 學生再確認：體的特徵必須大於滿足解的個數（這裡最多 $2^n$）？講者：對。

---

## 4. 雙重有效互動式證明

[▶ 39:07](https://youtu.be/SRY3F9vtJHo?t=2347)

**回顧**：到目前為止的 IP 只要求驗證者有效率。sum-check 和 #SAT 的證明者都是指數時間，「他也沒得選，他得做那些計算」。

【口頭】#SAT 也許還不夠讓人驚豔：公式本來就幾乎是低次多項式，算術化幾乎不用改，自然就是 sum-check。接下來要看一個**看起來完全不是低次**的問題，同時帶出雙重有效證明。

**動機**（[▶ 40:27](https://youtu.be/SRY3F9vtJHo?t=2427)）：「無限強的證明者不存在。」證明者比驗證者強（否則驗證者不需要他），但也不是無限強。證明者手上有一個問題，他不該花太多額外成本來說服驗證者。

這甚至對 **P 裡的問題**也有意義：例如一個語言要 $n^4$ 時間判定，我們希望驗證者只要線性時間。

> **定義（Doubly Efficient Interactive Proof）**：設 $L\in\mathrm{DTIME}(T)$（有一個決定性演算法在 $T(n)$ 時間判定 $L$，$n$ 是輸入長度）。$L$ 的雙重有效互動式證明是一個 IP，滿足：
> - **誠實證明者**的時間 $\le\mathrm{poly}(T)$。
> - **驗證者**的時間遠小於 $T$；理想上是準線性 $\tilde{O}(n) = n\cdot\mathrm{polylog}(n)$。

- $\tilde{O}$ 代表忽略 polylog 因子。
- 驗證者至少要讀輸入，但不該做比這多太多的事。
- 【口頭】理想上證明者也只有線性的額外負擔。「理論學家說 poly T，應用的人說 T 的線性，真正做應用的說不能超過 128 倍之類的。」
- 【口頭】這些在實務上很受重視，例如區塊鏈協定。Thaler 的書有章節講確切參數和實作，這門課不會講。
- 【Q&A】[▶ 44:38](https://youtu.be/SRY3F9vtJHo?t=2678) 學生問 $T$ 和 DTIME 的意思，講者解釋如上。$T$ 可以是 $n^4$、$n^{10}$、$n^{\log n}$ 等等。證明者既然要證明一件事是真的，自己就得知道它是真的，所以至少要跑 $T$ 時間。

> 【課本補充】Thaler §4.3 開頭：證明者多項式時間、驗證者線性時間的 IP 常叫 doubly-efficient，強調兩邊都有效率。

---

## 5. 例子：數圖裡的三角形

[▶ 46:02](https://youtu.be/SRY3F9vtJHo?t=2762)

【口頭】下週會給**所有低深度電路**的雙重有效證明（GKR）。先從一個例子開始。

**問題**：給圖 $G = (V, E)$，$n$ 個頂點，證明它恰好有 $k$ 個三角形。

- 這在 P 裡：檢查所有三個頂點的組合，$O(n^3)$ 時間。
- 目標：證明者大約 $n^3$（或多項式）時間，**驗證者線性時間**。
- 問題：這裡完全沒有多項式。「記得我說一切都能變成多項式嗎？這就是例子。」

**Step 1：把鄰接矩陣看成函數**（[▶ 48:04](https://youtu.be/SRY3F9vtJHo?t=2884)）

假設 $n$ 是 2 的次方。把頂點編號用二進位寫成 $\{0,1\}^{\log n}$ 的向量。

$$f:\{0,1\}^{\log n}\times\{0,1\}^{\log n}\to\{0,1\}, \qquad f(i, j) = 1 \iff (i, j)\in E.$$

**Step 2：把三角形數寫成總和**（[▶ 50:13](https://youtu.be/SRY3F9vtJHo?t=3013)）

$$k = \frac{1}{6}\sum_{i, j, \ell\in\{0,1\}^{\log n}} f(i, j)\cdot f(j, \ell)\cdot f(i, \ell).$$

- 三個邊都在時乘積是 1，否則至少一個因子是 0。
- $\frac{1}{6}$：每個三角形被它三個頂點的 $3! = 6$ 種排列各數一次。

【口頭】「看起來像 sum-check 了，但還沒有代數。」如果這是在有限體上、$f$ 又是低次多項式、體又夠大，就可以直接用 sum-check。

**為什麼證明者會是多項式時間**（[▶ 52:23](https://youtu.be/SRY3F9vtJHo?t=3143)）：sum-check 證明者的時間大約是 $|H|^m\times$（算一次函數的時間）。這裡總和只在 $\{0,1\}^{3\log n}$ 上：

$$|H|^m = 2^{3\log n} = n^3.$$

所以只要能把代數「放進來」，證明者就還是多項式時間。

**剩下的問題**：怎麼把 $f$ 變成低次多項式？答案是低次擴張。

> 【課本補充】Thaler §4.3 用**多線性擴張**（multilinear extension）$\tilde{f}_A$，對 $g(X, Y, Z) = \tilde{f}_A(X, Y)\,\tilde{f}_A(Y, Z)\,\tilde{f}_A(X, Z)$ 跑 sum-check。體選質數 $p\ge 6n^3$，確保 $6\Delta$ 不會在 mod $p$ 下溢位（三角形最多 $\binom{n}{3}\le n^3$ 個）。完整協定在下一集。

---

## 6. 低次擴張（預告）

[▶ 53:54](https://youtu.be/SRY3F9vtJHo?t=3234)

**回想矩陣乘法的例子**（第 01 集）：一列矩陣元素本來沒有代數，我們把它當成**單變數**多項式的係數，次數 $n-1$。

這裡做同樣的事，但改用**多變數**：

- 單變數：$n$ 個值 → 次數 $n-1$。驗證者時間和次數成正比，太慢。（鄰接矩陣有 $n^2$ 個值，次數會是 $n^2$。）
- 多變數：把 $n$ 個值**疊進一個方塊 $H^m$**，$|H|^m = n$。每個維度只有 $|H|$ 個值，所以每個變數的次數只要 $|H| - 1$。

> **定理（低次擴張, Low-Degree Extension, LDE）**：對任何函數 $f: H^m\to\{0,1\}$（不需要是多項式）和任何包含 $H$ 的有限體 $\mathbb{F}$，存在**唯一**的 $\tilde{f}:\mathbb{F}^m\to\mathbb{F}$ 使得
> 1. **擴張**：$\tilde{f}(x) = f(x)$ 對所有 $x\in H^m$（在小方塊上一致）；
> 2. **低次**：$\tilde{f}$ 每個變數的次數 $\le |H| - 1$。

- ⚠️ 逐字稿缺字：[▶ 59:01](https://youtu.be/SRY3F9vtJHo?t=3541) 字幕寫「$\tilde{f}$ from F to the n」，依上下文是 $\mathbb{F}^m$。
- 等價地：任何長度 $n = |H|^m$ 的 0/1 字串 $w$，都可以「摺」進 $H^m$（把 $\{1, \ldots, n\}$ 用 $H$ 進位表示），再擴張出去。
- $m = 1$ 時就是單變數的情形，次數 $n - 1$。
- **編碼單變數字串的兩種方法**（[▶ 63:18](https://youtu.be/SRY3F9vtJHo?t=3798)）：(1) 字串當**係數**；(2) 字串當多項式在 $1, 2, \ldots, n$ 的**值**。低次擴張用的是第 (2) 種。

**參數選法**（[▶ 64:43](https://youtu.be/SRY3F9vtJHo?t=3883)）：要 $|H|^m = n$，可以取 $|H| = \log n$，那麼

$$m = \frac{\log n}{\log\log n}, \qquad |H|^m = (\log n)^{\log n/\log\log n} = 2^{\log n} = n.$$

驗證者時間只和 $m$、$|H|$、$d = |H| - 1$ 有關，全都是 $\mathrm{polylog}(n)$。

- ⚠️ 逐字稿缺字：字幕寫「you can take n to be even smaller than log n... log n over log log n」，這裡的「n」應是 $m$。

**下次**：證明低次擴張定理，用在三角形上（很直接），再推到一般的低深度電路。

> 【課本補充】Thaler §3.5 主要講 $H = \{0,1\}$ 的特例，叫**多線性擴張**（multilinear extension, MLE）：任何 $f:\{0,1\}^v\to\mathbb{F}$ 有唯一的多線性擴張（每個變數次數 $\le 1$）
> $$\tilde{f}(x) = \sum_{w\in\{0,1\}^v} f(w)\,\chi_w(x), \qquad \chi_w(x) = \prod_{i=1}^{v}\left( x_iw_i + (1 - x_i)(1 - w_i) \right).$$
> 關鍵一步：$\chi_w(w) = 1$，$\chi_w(y) = 0$ 對其他 $y\in\{0,1\}^v$。唯一性的證明在下一集的筆記一起寫。

---

## 7. 一頁速查表

### Public coin

- 驗證者每則訊息都是均勻隨機位元，擲完就公開。Sum-check 是 public coin。
- 證明者用隨機沒幫助：把最好的硬幣寫死，變成電路。
- 證明者只要事先知道 $t_1$ 就能作弊：選 $g_1$ 使 $\sum_h g_1(h) = \beta$ 且 $g_1(t_1) = s_1(t_1)$。

### #SAT ∈ IP

- 算術化：$\mathrm{AND}\to xy$，$\mathrm{OR}\to x + y - xy$，$\mathrm{NOT}\to 1 - x$。在 $\{0,1\}$ 上與原本相同。
- 證明 $\sum_{b\in\{0,1\}^n}\tilde{\varphi}(b) = k$。
- $\sum_i\deg_i(\tilde{\varphi})\le s$。關鍵一步：樹的兩棵子樹葉子不重疊，$s = s_1 + s_2$；相乘時次數相加。
- Soundness $\le ns/|\mathbb{F}|$（Thaler：$\le s/|\mathbb{F}|$）。特徵 $p$ 要 $> 2^n$。
- 電路版次數會爆，要用 Shamir 的降次。

### 雙重有效 IP

- $L\in\mathrm{DTIME}(T)$：證明者 $\mathrm{poly}(T)$，驗證者 $\tilde{O}(n)$。

### 三角形

$$\#\triangle = \frac{1}{6}\sum_{i, j, \ell\in\{0,1\}^{\log n}} f(i, j)\,f(j, \ell)\,f(i, \ell).$$

證明者時間 $\approx |H|^m = 2^{3\log n} = n^3$。

### 低次擴張

- $f: H^m\to\{0,1\}$ ⟹ 唯一 $\tilde{f}:\mathbb{F}^m\to\mathbb{F}$，在 $H^m$ 上等於 $f$，每變數次數 $\le |H| - 1$。
- $|H| = \log n$、$m = \log n/\log\log n$ ⟹ $|H|^m = n$，次數和變數數都是 polylog。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Public coin | 第 10–13 集：Fiat–Shamir 只對 public-coin 協定有用 |
| 算術化 | 第 03–05 集：GKR 把電路的每一層算術化 |
| 低次擴張定理 | 第 03 集：證明＋用在三角形；之後 GKR、PCP 都用 |
| 雙重有效 IP | 第 03–05 集：GKR 協定 |
| Shamir 的降次、IP = PSPACE | 第 05 集：改用 GKR 證明 |
| 證明者的隨機用來藏東西 | 第 10–11 集：零知識證明 |

---

## 附：本集一句話總結

> **把布林公式「算術化」成低次多項式，sum-check 就直接給出 #SAT 的互動式證明；而要讓證明者也有效率，就得把沒有代數結構的資料（例如鄰接矩陣）用低次擴張摺進一個小方塊 $H^m$，讓總和只有多項式多項。**

---

## ⚠️ 待確認清單

1. [▶ 36:10](https://youtu.be/SRY3F9vtJHo?t=2170) 學生提到一篇「透過量子問題得到 #P ∈ IP」的論文，作者名字字幕聽不清楚。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 1 Part 2 錄影逐字稿（MIT 真人字幕，1:06:11）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§3.3、§3.5、§4.2、§4.3 整理。*
