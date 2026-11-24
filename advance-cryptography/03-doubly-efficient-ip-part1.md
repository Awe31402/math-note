---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 03
lecture: Lecture 2 (Part 1) – Doubly Efficient Interactive Proofs
date: 待補（2023 秋季第二堂課）
video: https://youtu.be/db1xAyO4YgM
notes: Thaler §2.4（書頁 18，PDF 頁 19）、§3.5（書頁 28–30，PDF 頁 29–31）、§4.3（書頁 42–44，PDF 頁 43–45）、§4.6.1–4.6.4（書頁 57–62，PDF 頁 58–63）
---

# 第 03 集 · Lecture 2 (Part 1)：低次擴張定理、數三角形、GKR 協定（上） [▶ 影片](https://youtu.be/db1xAyO4YgM)

← 上一集：[02-interactive-proofs-sumcheck-part2](02-interactive-proofs-sumcheck-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[04-doubly-efficient-ip-part2](04-doubly-efficient-ip-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 03 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:53:23，MIT 上傳的真人字幕）＋ Thaler §2.4、§3.5、§4.3、§4.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：黑板內容看不到，公式照口述重建並和 Thaler 對過。這集講者在黑板上有幾處寫錯、被學生抓到後當場修正，筆記寫的是修正後的版本，並註明修正過程。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 低次擴張定理](#1-低次擴張定理)
  - [1.1 敘述](#11-敘述)
  - [1.2 m = 1：Lagrange 插值](#12-m--1lagrange-插值)
  - [1.3 多變數的公式](#13-多變數的公式)
  - [1.4 證明：擴張、次數、唯一](#14-證明擴張次數唯一)
  - [1.5 Q&A：算術化也能擴張？單項式能少一點嗎？](#15-qa算術化也能擴張單項式能少一點嗎)
- [2. 數三角形的雙重有效證明](#2-數三角形的雙重有效證明)
  - [2.1 協定與成本](#21-協定與成本)
  - [2.2 Q&A：更簡單的協定（送 A² 和 A³）](#22-qa更簡單的協定送-a²-和-a³)
- [3. 為什麼低次擴張這麼重要](#3-為什麼低次擴張這麼重要)
- [4. GKR 協定（上）](#4-gkr-協定上)
  - [4.1 目標](#41-目標)
  - [4.2 假設：分層、fan-in 2、每層 S 個閘](#42-假設分層fan-in-2每層-s-個閘)
  - [4.3 天真的做法為什麼不行](#43-天真的做法為什麼不行)
  - [4.4 參數：H = log S、m = log S / log log S](#44-參數h--log-sm--log-s--log-log-s)
  - [4.5 證明者要算什麼](#45-證明者要算什麼)
  - [4.6 關鍵等式：把第 i 層寫成第 i+1 層的總和](#46-關鍵等式把第-i-層寫成第-i1-層的總和)
  - [4.7 修正：χ 要對兩個參數都是低次](#47-修正χ-要對兩個參數都是低次)
  - [4.8 跑 sum-check 之後驗證者剩下什麼](#48-跑-sum-check-之後驗證者剩下什麼)
  - [4.9 問題：一個宣稱變成兩個](#49-問題一個宣稱變成兩個)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:13](https://youtu.be/db1xAyO4YgM?t=13)

**課務**：

- 下週放假，沒課。
- 9 月 29 日講者去德國，由 Rachel（坐在後面的那位）代課。
- 10 月 6 日：Oded Regev 來講他新的量子分解演算法（改進 Shor 演算法）。這堂課直接移去聽他的演講。前一小時給一般理論聽眾，後面再講細節。

**回顧**（[▶ 02:17](https://youtu.be/db1xAyO4YgM?t=137)）：sum-check 協定（「證明系統的基本功」）、#SAT 的 IP（算術化）、雙重有效 IP 的定義、三角形問題的開頭。

【口頭】講者建議還沒熟 sum-check 的人去看 Thaler 的綜述，以及這門課的 scribe notes。

**本集**：

| 主題 | Thaler |
|---|---|
| 低次擴張定理＋證明 | §2.4（單變數）、§3.5（多線性） |
| 數三角形 | §4.3 |
| GKR 協定的前半：把一層的宣稱化簡成下一層 | §4.6.1–4.6.4 |

【口頭】低次擴張定理和 sum-check 合起來，「幾乎所有東西都是它們的推論」。

---

## 1. 低次擴張定理

### 1.1 敘述

[▶ 05:48](https://youtu.be/db1xAyO4YgM?t=348)

> **定理（低次擴張, LDE）**：$H$ 是任意集合，$\mathbb{F}$ 是包含 $H$ 的有限體。對**任何**函數 $f: H^m\to\{0,1\}$，存在**唯一**的多項式 $\tilde{f}:\mathbb{F}^m\to\mathbb{F}$ 使得
> 1. $\tilde{f}(x) = f(x)$ 對所有 $x\in H^m$；
> 2. $\tilde{f}$ 每個變數的次數 $\le |H| - 1$。

- 「任何函數」：$f$ 不需要是多項式，就是一串 $|H|^m$ 個任意的位元，排成一個方塊。
- **視覺化**：一堆位元坐在小方塊 $H^m$ 上。定理說可以把它唯一地延伸到大空間 $\mathbb{F}^m$，在小方塊上值不變，而且每個變數次數是 $|H| - 1$。
- $H = \{0, 1\}$ 時，每個變數次數 $\le 1$，叫**多線性擴張**（multilinear extension）。

【口頭】為什麼這麼強：它讓你從**任意一串位元**走到一個**低次多項式**。低次多項式有很多結構，例如可以跑 sum-check。常見用法：拿任意序列 → 取低次擴張 → 跑 sum-check。

### 1.2 m = 1：Lagrange 插值

[▶ 12:44](https://youtu.be/db1xAyO4YgM?t=764)

$m = 1$ 時，這就是 **Lagrange 插值定理**（Lagrange interpolation）：任何 $f: H\to\{0,1\}$ 有唯一的 $\tilde{f}:\mathbb{F}\to\mathbb{F}$，次數 $\le |H| - 1$，在 $H$ 上等於 $f$。公式：

$$\tilde{f}(x) = \sum_{h\in H} f(h)\,\chi_h(x),$$

其中 $\chi_h$ 在 $H$ 上是「指示函數」：對每個 $h'\in H$，$\chi_h(h') = 1$ 若 $h' = h$，否則 0。明確寫出來：

$$\chi_h(x) = \prod_{h'\in H,\ h'\neq h}\frac{x - h'}{h - h'}.$$

- 次數：分子有 $|H| - 1$ 個一次因式，所以次數 $|H| - 1$。
- $x = h$：每個分數都是 1，乘積是 1。
- $x = h''\neq h$（$h''\in H$）：分子有一項 $(h'' - h'') = 0$，乘積是 0。

- ⚠️ 逐字稿缺字：[▶ 16:59](https://youtu.be/db1xAyO4YgM?t=1019) 講者先說「sum over h′」，馬上改成「multiplication」，是乘積不是總和。字幕寫「H prime minus x」，分子正確寫法是 $x - h'$（或 $h' - x$ 配 $h' - h$，兩者相同）。

【Q&A】[▶ 14:50](https://youtu.be/db1xAyO4YgM?t=890) 學生問 $f(h)$ 前面是不是要放「反元素」。講者和學生一起代入檢查：$\tilde{f}(h^{*}) = \sum_h f(h)\chi_h(h^{*})$，只有 $h = h^{*}$ 那項不是 0，所以等於 $f(h^{*})$。不需要反元素。

> 【課本補充】Thaler §2.4 Lemma 2.3 是同一個單變數 Lagrange 插值。

### 1.3 多變數的公式

[▶ 18:25](https://youtu.be/db1xAyO4YgM?t=1105)

$$\tilde{f}(z) = \sum_{(h_1, \ldots, h_m)\in H^m} f(h_1, \ldots, h_m)\,\chi_{h_1, \ldots, h_m}(z), \qquad z\in\mathbb{F}^m,$$

$$\chi_{h_1, \ldots, h_m}(x_1, \ldots, x_m) = \prod_{i=1}^{m}\chi_{h_i}(x_i).$$

$\chi_{h_1, \ldots, h_m}$ 在 $H^m$ 上只在 $(h_1, \ldots, h_m)$ 那點是 1，其他點是 0。

> 【課本補充】Thaler §3.5 Lemma 3.6 是 $H = \{0, 1\}$ 的版本：$\chi_w(x) = \prod_{i=1}^{v}\left( x_iw_i + (1 - x_i)(1 - w_i) \right)$。代入 $H = \{0,1\}$ 的單變數公式：$\chi_1(x) = \frac{x - 0}{1 - 0} = x$，$\chi_0(x) = \frac{x - 1}{0 - 1} = 1 - x$，正好就是 $xw + (1-x)(1-w)$。

### 1.4 證明：擴張、次數、唯一

[▶ 20:43](https://youtu.be/db1xAyO4YgM?t=1243)

**(1) 是擴張**：任取 $h^{*} = (h_1^{*}, \ldots, h_m^{*})\in H^m$，代入：

$$\tilde{f}(h^{*}) = \sum_{h\in H^m} f(h)\prod_{i=1}^{m}\chi_{h_i}(h_i^{*}).$$

$\prod_i \chi_{h_i}(h_i^{*}) = 1$ 當且僅當每個 $h_i = h_i^{*}$，否則是 0。所以只剩一項：$\tilde{f}(h^{*}) = f(h^{*})$。

**(2) 次數**：$x_i$ 只出現在 $\chi_{h_i}(x_i)$ 這個因子裡，它的次數是 $|H| - 1$。加總不會提高次數。所以 $\deg_i(\tilde{f})\le |H| - 1$。

**(3) 唯一**（[▶ 22:55](https://youtu.be/db1xAyO4YgM?t=1375)）：用單變數的唯一性推出多變數的唯一性。

假設有兩個不同的擴張。相減得到 $g:\mathbb{F}^m\to\mathbb{F}$，滿足：
- $g\neq 0$（兩個多項式不同）；
- $g = 0$ 在 $H^m$ 上（兩個都擴張同一個 $f$）；
- 每個變數次數 $\le |H| - 1$。

要推出矛盾：在小方塊裡找到一點讓 $g\neq 0$。

- $g\neq 0$，所以存在 $(t_1, \ldots, t_m)\in\mathbb{F}^m$ 使 $g(t_1, \ldots, t_m)\neq 0$。
- **第 1 步**：看單變數多項式 $X\mapsto g(X, t_2, \ldots, t_m)$。它在 $X = t_1$ 不是 0，所以不是零多項式；次數 $\le |H| - 1$。如果它在整個 $H$ 上都是 0，那它和零多項式是同一個函數在 $H$ 上的兩個擴張，違反單變數的唯一性。所以存在 $h_1\in H$ 使 $g(h_1, t_2, \ldots, t_m)\neq 0$。
- **第 2 步**：看 $X\mapsto g(h_1, X, t_3, \ldots, t_m)$。在 $X = t_2$ 不是 0，同理存在 $h_2\in H$ 使 $g(h_1, h_2, t_3, \ldots, t_m)\neq 0$。
- 一直做下去，得到 $g(h_1, \ldots, h_m)\neq 0$，但 $(h_1, \ldots, h_m)\in H^m$，矛盾。$\blacksquare$

【口頭】講義（notes）裡有正式的歸納證明，「但上課這樣就夠了，不然會有點無聊」。

> 【課本補充】Thaler §3.5 對多線性的情形用另一種證明：若多線性 $h$ 在 $\{0,1\}^v$ 上全為 0 但不是零多項式，取次數最小的一項 $t$，把 $t$ 裡的變數設 1、其他設 0，得到的點上只有 $t$ 不為 0，矛盾。

### 1.5 Q&A：算術化也能擴張？單項式能少一點嗎？

【Q&A】[▶ 10:02](https://youtu.be/db1xAyO4YgM?t=602) **把 $f$ 的電路算術化，不也能得到低次的擴張？**
對，如果 $f$ 本身已經是一個深度 $D$ 的電路，算術化後次數大約 $2^{D}$。#SAT 就是這樣做的。但：
- 這需要假設 $f$ 有結構（低深度）。定理是對**任何**位元序列都成立。
- 學生追問唯一性：算術化得到的擴張可以不一樣，但次數不會是最小的。講者：「要拿到最小的次數，就得這樣做。」

【Q&A】[▶ 29:17](https://youtu.be/db1xAyO4YgM?t=1757) **能不能用計數論證證唯一性？**
（每個變數次數 $\le |H| - 1$ 的多項式，係數有 $|H|^m$ 個，和函數 $H^m\to\mathbb{F}$ 的個數一樣。）講者說大概也可以。

【Q&A】[▶ 29:58](https://youtu.be/db1xAyO4YgM?t=1798) Vinod 替算術化說話：**算術化的版本在任何點都能很快算，但這個 $\tilde{f}$ 要算一個點，就得把整個方塊加一遍。**
講者：「100% 對。」算 $\tilde{f}$ 一點要 $|H|^m$ 時間，很沒效率。但這個定理會用在算術化不能用的場合。

【Q&A】[▶ 30:39](https://youtu.be/db1xAyO4YgM?t=1839) **能不能把單項式個數壓少？**
一般不行：如果 $f$ 可以是任何函數，有 $2^{|H|^m}$ 種可能，用計數論證，多項式至少要有那麼多單項式才存得下資訊。而且在實際用法裡，$f$ **真的沒有結構**。但在一些情形可以少一點，之後會用到。

---

## 2. 數三角形的雙重有效證明

### 2.1 協定與成本

[▶ 32:44](https://youtu.be/db1xAyO4YgM?t=1964)

**設定**：圖有 $n$ 個頂點，鄰接矩陣是 $n^2$ 個位元。直接數三角形要 $n^3$。驗證者「可憐的傢伙」只能讀圖，跑 $\tilde{O}(n^2)$ 時間。證明者要說服他：三角形數是 $\beta$。

1. $f:\{0,1\}^{\log n}\times\{0,1\}^{\log n}\to\{0,1\}$ 是鄰接矩陣。取它的低次擴張 $\tilde{f}$，因為 $H = \{0,1\}$，它是**多線性**的。
2. 三角形數：
$$\beta = \frac{1}{6}\sum_{i, j, k\in\{0,1\}^{\log n}} f(i, j)\,f(j, k)\,f(i, k) = \frac{1}{6}\sum_{i, j, k\in\{0,1\}^{\log n}}\tilde{f}(i, j)\,\tilde{f}(j, k)\,\tilde{f}(i, k).$$
   第二個等號：總和只在小方塊上，在那裡 $\tilde{f} = f$。
3. $g(i, j, k) := \tilde{f}(i, j)\tilde{f}(j, k)\tilde{f}(i, k)$ 是多項式，**每個變數次數 2**（每個變數出現在兩個因子裡，各是 1 次）。對 $g$ 跑 sum-check，證明總和是 $6\beta$。

**成本**：

| 項目 | 結果 | 理由 |
|---|---|---|
| 變數數 $m$ | $3\log n$ | |
| 次數 $d$ | 2 | |
| 通訊 | polylog | $m\cdot d\cdot\log|\mathbb{F}|$ |
| 驗證者 | $\tilde{O}(n^2)$ | 最後要算 $g$ 在一個隨機點的值，也就是算 $\tilde{f}$ 在 3 個點。用 1.3 的公式，每個要加 $n^2$ 項 |
| 證明者 | 約 $n^5$ | $|H|^m = n^3$ 個點 × 算一次 $\tilde{f}$ 要 $n^2$，再乘 log 因子 |

【口頭】這門課不追 polylog 因子，全部放進 $\tilde{O}$。

【Q&A】[▶ 41:15](https://youtu.be/db1xAyO4YgM?t=2475) **證明者不是應該 $n^3$ 嗎？**
講者算一下，承認證明者其實是 $n^5$ 左右。但仍是多項式額外負擔，所以算雙重有效。學生問能不能降到 $n^3$（或矩陣乘法的 $n^{\omega}$）：講者說最近有一系列很好的工作能讓證明者做到線性時間，所以 $n^3$ 應該做得到；這個特定協定行不行她不確定。
- ⚠️ 逐字稿缺字：字幕寫「the work of Dan Sung and friends」，名字可能聽錯（見待確認清單）。

> 【課本補充】Thaler §4.3：體選質數 $p\ge 6n^3$，確保 $6\Delta$ 在 mod $p$ 下不會溢位。Thaler 的協定用 sum-check 的「證明者時間隨輪數幾何遞減」分析和多線性擴張的結構，證明者可以做到 $O(n^3)$。

### 2.2 Q&A：更簡單的協定（送 A² 和 A³）

【Q&A】[▶ 42:36](https://youtu.be/db1xAyO4YgM?t=2556) 學生問：**這個協定回合數是 $\log n$，能更少嗎？**

講者說上次 Gabe 就指出有個**簡單得多**的協定（如果只在乎驗證者時間、不在乎通訊量）：

1. 證明者送 $A_2 := A^2$ 和 $A_3 := A^3$（$A$ 是鄰接矩陣，驗證者已經有）。
2. 驗證者用第 01 集的 Freivalds 隨機檢查確認 $A_2 = A\cdot A$、$A_3 = A_2\cdot A$，每個 $O(n^2)$。
3. 三角形數由 $A^3$ 的跡（trace）算出。

只要兩則訊息，但通訊量是 $n^2$（不是 polylog）。

- 以下**不是逐字稿內容**，是依線性代數推論的：講者說「三角形數就是 $\mathrm{tr}(A^3)$」，精確地說 $\mathrm{tr}(A^3) = \sum_i (A^3)_{ii}$ 是長度 3 的封閉路徑數，每個三角形被數 6 次（3 個起點 × 2 個方向），所以三角形數 $= \mathrm{tr}(A^3)/6$。

學生：「這很漂亮，但我不滿意。」（想要通訊量也小。）講者：有一篇很漂亮的工作（字幕記為「R, R, R」）做到**常數回合**，用它大概能得到很好的參數，細節她要想一下。

> 【課本補充】「R, R, R」對得上 Thaler §4.5.5 末段引用的 **[RRR16]**（Reingold、Rothblum、Rothblum, 2016）：Thaler 稱它是一個突破性的複雜度結果，給 P 一個很不一樣的 IP，避開了「證明者得探索所有組態」的低效率，而且**只要常數回合**。（作者全名是依 [RRR16] 這個引用標籤和講者說的「R, R, R」對起來的；Thaler 正文只寫標籤。）

---

## 3. 為什麼低次擴張這麼重要

[▶ 46:05](https://youtu.be/db1xAyO4YgM?t=2765)

【口頭】三角形只是動機例子：鄰接矩陣完全沒有結構，但用低次擴張就能加上結構，再用 sum-check。

更一般的想法是**糾錯碼**：「如果你作弊，你就得處處作弊。」錯誤會擴散。證明系統的目的就是**抓作弊的證明者**，所以很自然地會想要某種編碼：在一處作弊，就得在處處作弊。接下來的 GKR 就是這樣用的。

【口頭】[▶ 47:29](https://youtu.be/db1xAyO4YgM?t=2849) 三小時的課很累又很技術，講者讓大家投票：休息兩次（每小時一次）還是一次長的。結果休息兩次，現在先休息 5 分鐘。

---

## 4. GKR 協定（上）

### 4.1 目標

[▶ 48:10](https://youtu.be/db1xAyO4YgM?t=2890)

【口頭】到目前為止的應用（#SAT、三角形）都是**計數**問題。你可能以為 sum-check 只能數東西。接下來要說明：光靠低次擴張＋sum-check，就能給**所有低深度電路**雙重有效的證明。

**設定**：電路 $C$，大小 $S$（閘的數目，很大），深度 $d$（很小）。證明者要說服驗證者 $C(x) = 1$。

**目標**：

| | |
|---|---|
| 驗證者時間、通訊 | $d\cdot\mathrm{polylog}(S)$ |
| 證明者時間 | $\mathrm{poly}(S)$（他總得算一次電路） |

- 【Q&A】[▶ 49:30](https://youtu.be/db1xAyO4YgM?t=2970) 電路大小就是閘的數目？是。
- **連讀電路都不夠快**（[▶ 50:11](https://youtu.be/db1xAyO4YgM?t=3011)）：驗證者時間遠小於 $S$，所以 $C$ 必須有簡短的描述。假設 $C$ 是 **log-space uniform**：有一個用 $O(\log S)$ 空間的圖靈機能產生這個電路。【口頭】現在先別管這個，要到很後面才會處理。
- 【Q&A】[▶ 61:01](https://youtu.be/db1xAyO4YgM?t=3661) 驗證者看不到整個電路，怎麼辦？講者：「很複雜，之後會看到。」他會用這個 uniform 描述來幫忙。

**高層想法**（[▶ 51:39](https://youtu.be/db1xAyO4YgM?t=3099)）：把「輸出是 1」的宣稱，化簡成「下一層的某件事」的宣稱，再化簡成更下一層……一直到**輸入層**，驗證者自己就能檢查。

> 【課本補充】Thaler §4.6.2 Table 4.4（原始 GKR [GKR08]，log-space uniform 分層算術電路，大小 $S$、深度 $d$、$n$ 個輸入）：通訊 $d\cdot\mathrm{polylog}(S)$ 個體元素；回合 $d\cdot\mathrm{polylog}(S)$；驗證者 $O(n + d\cdot\mathrm{polylog}(S))$；證明者 $\mathrm{poly}(S)$；soundness 錯誤 $O(d\log(S)/|\mathbb{F}|)$。Thaler 也提到應用：NC（polylog 時間平行演算法）裡的問題都有 polylog 深度的 log-space uniform 電路，所以都有多項式時間證明者、線性時間驗證者的 IP。

### 4.2 假設：分層、fan-in 2、每層 S 個閘

[▶ 52:22](https://youtu.be/db1xAyO4YgM?t=3142)

都不失一般性：

1. **分層**（layered）：輸出閘在第 0 層，輸入在第 $d$ 層。第 $i$ 層的閘只接到第 $i+1$ 層的閘。
   - 做法：如果某條線跳過好幾層，就插入「複製」用的假閘（dummy gate），一層一層往上傳。
2. **Fan-in 2**：每個閘只有兩個輸入（[▶ 103:21](https://youtu.be/db1xAyO4YgM?t=6201) 講者補充的假設）。深度多一個 log 因子。
3. **每層恰好 $S$ 個閘**（[▶ 64:30](https://youtu.be/db1xAyO4YgM?t=3870)）：不夠就補值為 0 的假閘。「沒人會看它們，只是讓符號簡單。」

### 4.3 天真的做法為什麼不行

[▶ 56:11](https://youtu.be/db1xAyO4YgM?t=3371)

假設證明者說輸出是 1，其實是 0，輸出閘是 AND。

- 證明者等於宣稱兩個子閘都是 1。至少一個其實是 0（是假宣稱）。
- 驗證者**隨機選一個子閘**，叫證明者證明它。再往下選、再往下選，直到輸入層，證明者就卡住了。

問題：每一層只有 1/2 的機率選到「假的那個」。（例如 AND 閘值是 0、宣稱是 1，可能只有一個子閘是 0。）$d$ 層下來，抓到的機率只有 $2^{-d}$。

【口頭】「這很爛。」
- ⚠️ 逐字稿缺字：[▶ 58:11](https://youtu.be/db1xAyO4YgM?t=3491) 講者說「1 over 2 to the d is the size of the circuit」，意思應是：$d$ 可以到 $\log S$ 的等級，$2^{-d}$ 可能小到 $1/S$。

**真正的想法**：不要一個閘一個閘地問，改問**整層的編碼**（整層值的低次擴張）的某件事。如果證明者在這一層作弊，他在下一層的編碼也高機率作弊。從一層的編碼走到下一層的編碼，用的就是 **sum-check**。

### 4.4 參數：H = log S、m = log S / log log S

[▶ 65:13](https://youtu.be/db1xAyO4YgM?t=3913)

每層 $S$ 個值，要放進方塊 $H^m$，需要 $|H|^m = S$。兩種選法：

| 選法 | $|H|$ | $m$ |
|---|---|---|
| 二進位（Thaler 用的） | 2 | $\log S$ |
| 講者這學期用的 | $\log S$ | $\dfrac{\log S}{\log\log S}$ |

檢查第二種：$(\log S)^{\log S/\log\log S} = \left( 2^{\log\log S} \right)^{\log S/\log\log S} = 2^{\log S} = S$ ✓。

**為什麼要這麼怪的參數**（[▶ 68:50](https://youtu.be/db1xAyO4YgM?t=4130)）：

- Sum-check 的 soundness 是 $m\cdot d/|\mathbb{F}|$，所以 $|\mathbb{F}|$ 至少要比 $m$ 大。
- 之後做 **PCP**（第 06 集）時，希望 $|\mathbb{F}| = \mathrm{poly}(|H|)$，否則 PCP 會變成超多項式大小。
- 如果 $H = \{0,1\}$，那 $|\mathbb{F}|$ 只能是常數，但 $m = \log S$ 不是常數，soundness 錯誤會大於 1，什麼都得不到。

【Q&A】[▶ 70:53](https://youtu.be/db1xAyO4YgM?t=4253) **GKR 本身需要這樣嗎？**
不需要。GKR 是互動的，從來不會把整個東西寫下來，可以用 $H = \{0,1\}$ 和很大的 $\mathbb{F}$。講者猶豫過要不要先用 $\{0,1\}$ 教，但反正之後要換參數，而且「這類參數很常出現，習慣一下比較好」。整堂課的內容用 $H = \{0,1\}$、$m = \log S$ 去理解也完全成立。

【口頭】講者開玩笑說 Rachel 代課時會講到為什麼——「Rachel 心想：糟了，我答應了什麼。」

### 4.5 證明者要算什麼

[▶ 61:42](https://youtu.be/db1xAyO4YgM?t=3702)

協定開始前，證明者：

1. **算術化** $C$：AND → 乘、OR → $x + y - xy$。現在只有 ADD 和 MULT 閘。
2. 對輸入 $x$ **算出所有閘的值**（都還是 0/1）。
3. 對每一層 $i$，把閘編號成 $H^m$ 的元素，定義
$$V_i: H^m\to\{0,1\}, \qquad V_i(p) = \text{第 } i \text{ 層、編號 } p \text{ 的閘在輸入 } x \text{ 上的值}.$$
4. 算出每層的**低次擴張** $\tilde{V}_i:\mathbb{F}^m\to\mathbb{F}$。

**電路的連線函數**（[▶ 77:19](https://youtu.be/db1xAyO4YgM?t=4639)）：對每層 $i$ 定義

$$\mathrm{add}_i, \mathrm{mult}_i: H^m\times H^m\times H^m\to\{0,1\},$$

$\mathrm{add}_i(p, w_1, w_2) = 1$ 當且僅當第 $i$ 層的閘 $p$ 是 ADD 閘，而且輸入是第 $i+1$ 層的閘 $w_1$、$w_2$。$\mathrm{mult}_i$ 同理。這兩個函數只跟**電路**有關，跟輸入、跟證明者的宣稱都無關。

- ⚠️ 逐字稿缺字：講者一開始把定義域寫成 $\{0,1\}^{3\log S}$，[▶ 84:36](https://youtu.be/db1xAyO4YgM?t=5076) 自己更正：「我要一致，既然用 $H$，就全都是 $H$。」

### 4.6 關鍵等式：把第 i 層寫成第 i+1 層的總和

[▶ 74:26](https://youtu.be/db1xAyO4YgM?t=4466)

協定從證明者的宣稱開始：輸出層的那個（真的）閘 $z_0$ 的值是 $v_0$（這裡是 1）。也就是 $\tilde{V}_0(z_0) = v_0$。

一般地，假設目前的宣稱是 $\tilde{V}_i(z^{*}) = v_i^{*}$，$z^{*}\in\mathbb{F}^m$（之後的 $z^{*}$ 會在擴張裡，不在小方塊裡）。

**Step 1**：低次擴張的定義

$$\tilde{V}_i(z^{*}) = \sum_{p\in H^m} V_i(p)\,\chi(p, z^{*}).$$

**Step 2**：每個閘的值由下一層決定。【課堂討論】講者問 MULT 閘的值是什麼，學生答 $V_{i+1}(w_1)\cdot V_{i+1}(w_2)$：

$$V_i(p) = \sum_{w_1, w_2\in H^m}\left[ \mathrm{add}_i(p, w_1, w_2)\left( V_{i+1}(w_1) + V_{i+1}(w_2) \right) + \mathrm{mult}_i(p, w_1, w_2)\,V_{i+1}(w_1)\,V_{i+1}(w_2) \right].$$

（若 $p$ 是 ADD 閘、輸入 $w_1, w_2$，只有那一項的 $\mathrm{add}_i = 1$，其他全是 0。）

- ⚠️ 逐字稿缺字：[▶ 81:44](https://youtu.be/db1xAyO4YgM?t=4904) 講者先寫成 $V_i$，學生提醒應為 $V_{i+1}$。

**Step 3**：合併，再把 0/1 函數換成它們的低次擴張（在小方塊上值不變，所以總和不變）：

$$\boxed{\tilde{V}_i(z^{*}) = \sum_{p, w_1, w_2\in H^m}\tilde{\chi}(p, z^{*})\left[ \widetilde{\mathrm{add}}_i(p, w_1, w_2)\left( \tilde{V}_{i+1}(w_1) + \tilde{V}_{i+1}(w_2) \right) + \widetilde{\mathrm{mult}}_i(p, w_1, w_2)\,\tilde{V}_{i+1}(w_1)\,\tilde{V}_{i+1}(w_2) \right]}$$

【口頭】「我們想證明第 $i$ 層的事，結果寫成了第 $i+1$ 層元素的總和。這正是我們要的。」證明「某個東西等於一個總和」用什麼？**Sum-check。**

**這是低次多項式嗎**（[▶ 83:54](https://youtu.be/db1xAyO4YgM?t=5034)）：

- 變數：$p, w_1, w_2$，共 $3m$ 個。$m = \log S/\log\log S$，很小。
- 每個 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$、$\tilde{V}_{i+1}$、$\tilde{\chi}$ 每個變數次數 $\le |H| - 1$。
- 乘起來：$w_1$ 同時出現在 $\widetilde{\mathrm{mult}}_i$ 和 $\tilde{V}_{i+1}(w_1)$ 裡，次數最多約 $2(|H| - 1)$。講者說「$2H - 1$，還是很小，大約兩個 log」。

【口頭】「所以 GKR 協定是什麼？Sum-check。就這樣。」

> 【課本補充】Thaler §4.6.4 Lemma 4.7 用的是 $H = \{0,1\}$ 和多線性擴張，而且**不對 $p$ 加總**：
> $$\tilde{W}_i(z) = \sum_{b, c\in\{0,1\}^{k_{i+1}}}\left[ \widetilde{\mathrm{add}}_i(z, b, c)\left( \tilde{W}_{i+1}(b) + \tilde{W}_{i+1}(c) \right) + \widetilde{\mathrm{mult}}_i(z, b, c)\,\tilde{W}_{i+1}(b)\,\tilde{W}_{i+1}(c) \right].$$
> 這可行是因為 $\widetilde{\mathrm{add}}_i$ 在第一組變數上是**多線性**的（Remark 4.3）：$\sum_p \chi(p, z)\,\mathrm{add}_i(p, b, c)$ 本身就是 $\mathrm{add}_i$ 對第一個參數的多線性擴張。Remark 4.4 說 GKR 原論文用的是比較複雜的式子（就像講者這裡多加一個 $\sum_p\chi(p, z)$），好處是 $\mathrm{add}_i$、$\mathrm{mult}_i$ 的擴張不必在第一組變數上是多線性。

### 4.7 修正：χ 要對兩個參數都是低次

[▶ 90:26](https://youtu.be/db1xAyO4YgM?t=5426)

學生（Vinod 等）抓到一個問題：前面的 $\chi_p(z)$ 是用 Lagrange 公式定義的，$p$ 出現在**分母**（$h_i - h'$），所以它**不是 $p$ 的多項式**。但 sum-check 會對 $p$ 加總、在 $p$ 上代入隨機體元素，需要對 $p$ 也是低次。

講者當場修正：

- 把 $\chi$ 看成**兩個參數**的函數 $\chi(h, z)$，$h, z\in\mathbb{F}^m$：
$$\chi(h_1, \ldots, h_m, z_1, \ldots, z_m) = \prod_{i=1}^{m}\chi_1(h_i, z_i).$$
- $\chi_1$ 是一個**雙變數**多項式，兩個變數次數都 $\le |H| - 1$。它在 $H\times H$ 上定義為：$\chi_1(h, z) = 1$ 若 $h = z$，否則 0。在 $\mathbb{F}\times\mathbb{F}$ 上就取它的**唯一低次擴張**（由低次擴張定理保證存在且唯一）。
- 所以 $\chi$ 在 $H^m\times H^m$ 上是「相等」的指示函數，對所有 $2m$ 個變數都是低次。

【Q&A】[▶ 98:25](https://youtu.be/db1xAyO4YgM?t=5905) 學生：$\chi_1$ 不是「多項式的比值」嗎？講者：不是。它就是**定義**成 $H\times H$ 上相等指示函數的那個唯一低次擴張，本身就是雙變數多項式。Vinod 總結：「之前的寫法 $h$ 在分母，不是多項式；這個是。」

> 以下**不是逐字稿內容**，是依低次擴張定理推論的：明確地，$\chi_1(h, z) = \sum_{a\in H}\chi_a(h)\,\chi_a(z)$（$\chi_a$ 是 1.2 的單變數 Lagrange 基底）。在 $H\times H$ 上它等於 $[h = z]$，兩個變數次數都 $\le |H| - 1$，所以就是那個唯一擴張。$H = \{0,1\}$ 時是 $hz + (1-h)(1-z)$，和 Thaler 的 $\chi_w(x)$ 一樣，只是 $w$ 也當變數。

【Q&A】[▶ 105:31](https://youtu.be/db1xAyO4YgM?t=6331) 學生建議：$z^{*}$ 是固定的，能不能沿用原本的 $\chi$ 寫在下標？講者：原本固定的是 $H^m$ 的點；這裡會在擴張裡，所以要保留兩個參數的版本。

### 4.8 跑 sum-check 之後驗證者剩下什麼

[▶ 86:05](https://youtu.be/db1xAyO4YgM?t=5165)

在第 $i$ 層，對 4.6 的方框式子跑 sum-check（$3m$ 個變數）。

**關鍵觀察**：sum-check 結束時，驗證者要在**一個點**上算那個多項式，而那個點是**驗證者自己選的隨機點**。GKR 裡沒有 oracle，所以要靠這個觀察。

記驗證者在 sum-check 裡選的隨機數為 $(r_0, r_1, r_2)\in(\mathbb{F}^m)^3$（分別取代 $p, w_1, w_2$）。sum-check 最後化簡成一個宣稱：

$$\tilde{\chi}(r_0, z^{*})\left[ \widetilde{\mathrm{add}}_i(r_0, r_1, r_2)\left( \tilde{V}_{i+1}(r_1) + \tilde{V}_{i+1}(r_2) \right) + \widetilde{\mathrm{mult}}_i(r_0, r_1, r_2)\,\tilde{V}_{i+1}(r_1)\,\tilde{V}_{i+1}(r_2) \right] = \gamma,$$

$\gamma$ 是 sum-check 最後一輪得到的值。

- ⚠️ 逐字稿缺字：講者黑板上把隨機數記為 $Z_0, Z_1, Z_2$，和宣稱裡的固定點 $Z_i$ 撞名。學生很困惑，[▶ 104:45](https://youtu.be/db1xAyO4YgM?t=6285) 講者說「抱歉，那些應該加星號」：固定的那個是 $z^{*}$，隨機的是驗證者選的。筆記改用 $z^{*}$ 和 $r_0, r_1, r_2$ 區分。

**驗證者要算的東西**：

| 項 | 誰算 |
|---|---|
| $\tilde{\chi}(r_0, z^{*})$ | 驗證者自己算（明確公式） |
| $\widetilde{\mathrm{add}}_i(r_0, r_1, r_2)$、$\widetilde{\mathrm{mult}}_i(r_0, r_1, r_2)$ | **先假設驗證者有 oracle**（只和電路有關）。原論文叫「bare bones protocol」。【口頭】壞消息：就算有 uniform 描述，我們也不知道怎麼算；下次處理 |
| $\tilde{V}_{i+1}(r_1)$、$\tilde{V}_{i+1}(r_2)$ | 驗證者算不出來 |

**怎麼辦**（[▶ 109:41](https://youtu.be/db1xAyO4YgM?t=6581)）：

1. 驗證者叫證明者告訴他兩個值：$\tilde{V}_{i+1}(r_1) = v_{i+1,1}^{*}$、$\tilde{V}_{i+1}(r_2) = v_{i+1,2}^{*}$。
2. 驗證者把這兩個值代進上面的式子，檢查是否等於 $\gamma$。

**為什麼可靠**：

- 如果一開始的宣稱 $v_i^{*}$ 是假的，由 sum-check 的 soundness，$\gamma$ 高機率也是假的（不等於真正的值）。
- 如果證明者老實報出真的 $\tilde{V}_{i+1}(r_1)$、$\tilde{V}_{i+1}(r_2)$，代進去會得到**真的值**，不等於假的 $\gamma$，被拒絕。
- 所以證明者要不被當場拒絕，**至少一個值要說謊**。

【Q&A】[▶ 111:56](https://youtu.be/db1xAyO4YgM?t=6716) 學生：所以他要給兩個值？講者：對。

### 4.9 問題：一個宣稱變成兩個

[▶ 112:39](https://youtu.be/db1xAyO4YgM?t=6759)

「流了很多汗」之後，我們確實從第 $i$ 層走到第 $i+1$ 層。代價：

1. 奇蹟似地假設驗證者能算 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$。
2. **一個關於第 $i$ 層的宣稱，變成兩個關於第 $i+1$ 層的宣稱。**

學生：「這不就回到原點了嗎？」（每層加倍，$d$ 層變成 $2^d$ 個宣稱，跟天真做法一樣糟。）講者：「沒錯。現在是休息的好時機。」解法在第 04 集。

> 【課本補充】Thaler §4.6.4「Reducing to Verification of a Single Point」：取通過 $b^{*}$、$c^{*}$ 的唯一直線 $\ell:\mathbb{F}\to\mathbb{F}^{k_{i+1}}$，$\ell(0) = b^{*}$、$\ell(1) = c^{*}$；證明者送 $\tilde{W}_{i+1}$ 限制在 $\ell$ 上的單變數多項式 $q$；驗證者檢查 $q(0)$、$q(1)$，再取隨機 $r^{*}$，把兩個宣稱化成一個：$\tilde{W}_{i+1}(\ell(r^{*})) = q(r^{*})$。（下一集的內容。）

---

## 5. 一頁速查表

### 低次擴張

- $f: H^m\to\{0,1\}$ ⟹ 唯一 $\tilde{f}:\mathbb{F}^m\to\mathbb{F}$，在 $H^m$ 上等於 $f$，每變數次數 $\le |H| - 1$。
- 公式：$\tilde{f}(z) = \sum_{h\in H^m} f(h)\prod_{i=1}^{m}\chi_{h_i}(z_i)$，$\chi_h(x) = \prod_{h'\neq h}\frac{x - h'}{h - h'}$。
- $H = \{0,1\}$：$\chi_w(x) = \prod_i\left( x_iw_i + (1-x_i)(1-w_i) \right)$（多線性）。
- 唯一性關鍵一步：差 $g\neq 0$ 在某點 $(t_1, \ldots, t_m)$ 不為 0；逐座標用單變數唯一性把 $t_j$ 換成某個 $h_j\in H$，仍不為 0，最後落在 $H^m$ 裡，矛盾。
- 算一點要 $|H|^m$ 時間；一般而言單項式不能更少（計數論證）。

### 數三角形

- $\sum_{i,j,k}\tilde{f}(i,j)\tilde{f}(j,k)\tilde{f}(i,k) = 6\beta$，每變數次數 2，$m = 3\log n$。
- 驗證者 $\tilde{O}(n^2)$（算 $\tilde{f}$ 三個點）；證明者 $\mathrm{poly}(n)$。
- 簡單替代：送 $A^2, A^3$，Freivalds 檢查，三角形數 $= \mathrm{tr}(A^3)/6$。

### GKR（上）

- 假設：分層、fan-in 2、每層 $S$ 個閘、log-space uniform。
- 參數：$|H| = \log S$、$m = \log S/\log\log S$（為了之後 PCP 要 $|\mathbb{F}| = \mathrm{poly}|H|$）。
- 關鍵等式：
$$\tilde{V}_i(z^{*}) = \sum_{p, w_1, w_2\in H^m}\tilde{\chi}(p, z^{*})\left[ \widetilde{\mathrm{add}}_i\cdot(\tilde{V}_{i+1}(w_1) + \tilde{V}_{i+1}(w_2)) + \widetilde{\mathrm{mult}}_i\cdot\tilde{V}_{i+1}(w_1)\tilde{V}_{i+1}(w_2) \right].$$
  關鍵一步：$\tilde{V}_i$ 的定義 + 閘的值由下一層決定 + 把 0/1 函數換成擴張（小方塊上不變）。
- $\chi(h, z)$ 要對 $h$、$z$ 都是低次：$\chi_1$ = $H\times H$ 上相等指示函數的唯一低次擴張。
- 一層 sum-check 後：驗證者算 $\tilde{\chi}$，（假設）查 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$，向證明者要 $\tilde{V}_{i+1}(r_1)$、$\tilde{V}_{i+1}(r_2)$。假的宣稱 ⟹ 至少一個值是假的。
- 問題：一個宣稱 → 兩個宣稱。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 一個宣稱變兩個 | 第 04 集：用直線把兩個宣稱合成一個 |
| $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ 怎麼算 | 第 04–05 集：處理 log-space uniform |
| $|H| = \log S$ 的參數 | 第 06 集：用 GKR 做 PCP |
| 低次擴張定理 | GKR、PCP、之後所有用到多項式編碼的地方 |
| 「作弊就得處處作弊」 | 第 06–09 集：PCP、Kilian–Micali |

---

## 附：本集一句話總結

> **任何一串位元都能唯一地擴張成每個變數低次的多項式；GKR 用這個把「第 $i$ 層某點的擴張值」寫成「第 $i+1$ 層擴張值的總和」，再用 sum-check 一層一層往輸入走——但每走一層，一個宣稱會變成兩個，這要下一集解決。**

---

## ⚠️ 待確認清單

1. [▶ 42:36](https://youtu.be/db1xAyO4YgM?t=2556) 字幕「the work of Dan Sung and friends」（讓證明者線性時間的工作），名字可能聽錯。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 2 Part 1 錄影逐字稿（MIT 真人字幕，1:53:23）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§2.4、§3.5、§4.3、§4.6 整理。*
