---
course: Abstract Algebra II (Spring 2026)
episode: 17
lecture: L14
date: 2026-02-18
video: https://www.youtube.com/watch?v=pUdxGE7-k_8
notes: 講義/AA2/Math422_Lecture14_IrreduciblePolynomialTheory.pdf
---

# 第 17 集 · L14：不可約判別——模 $p$ 約化與 Eisenstein [▶ 影片](https://www.youtube.com/watch?v=pUdxGE7-k_8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[16-L13-除法算法與不可約性]] ｜ [總目錄](../README.md) ｜ 下一集：[[18-L15-多項式理論完結]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 17 集，Lecture 14
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:27，自動字幕）＋ 手寫講義 `Math422_Lecture14_IrreduciblePolynomialTheory.pdf`（8 頁：前 6 頁是 2018 講義 §4.6 Lecture 26 p.149–154，後 2 頁新寫），主要依 Gallian 第 17 章。前半黑板，後半投影。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 警世故事：四次式沒有根也可能可約](#0-警世故事四次式沒有根也可能可約)
- [1. 容度與本原多項式](#1-容度與本原多項式)
- [2. 本原 × 本原 = 本原；係數約化同態](#2-本原--本原--本原係數約化同態)
- [3. ℚ 上可約 ⇒ ℤ 上可約](#3-ℚ-上可約--ℤ-上可約)
- [4. 模 p 約化判別法](#4-模-p-約化判別法)
- [5. Eisenstein 判別法；分圓多項式](#5-eisenstein-判別法分圓多項式)
- [6. 不可約 ⟺ 極大；16 元素的體](#6-不可約--極大16-元素的體)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 警世故事：四次式沒有根也可能可約

[▶ 00:30](https://youtu.be/pUdxGE7-k_8?t=30) 課前禱告。「Lecture 14，我取名『**更多多項式理論**』。大方向是：多項式**可約還是不可約**？怎麼判斷？」

**例 1**（講義 p.1，Example 4.6.7）[▶ 01:00](https://youtu.be/pUdxGE7-k_8?t=60)：
$$f(x) = x^4+14x^2+49 = (x^2+7)^2$$
在 $\mathbb{R}$ 上**可約**，但**沒有實根**。

⚠️ 逐字稿缺字：自動字幕把中間項記成「$4x^2$」，但 $(x^2+7)^2 = x^4+14x^2+49$，以講義為準。

【口頭】[▶ 02:00](https://youtu.be/pUdxGE7-k_8?t=120)「**別騙自己**以為上堂課最後的定理管得比它實際更遠。2、3 次多項式在體上沒有根 ⇒ 不可約；但**四次式就一切都不算數了**，要更多分析。」

---

## 1. 容度與本原多項式

> **定義**（講義 p.1，Def 4.6.8）[▶ 02:30](https://youtu.be/pUdxGE7-k_8?t=150)　非零 $f(x) = a_nx^n+\cdots+a_1x+a_0\in\mathbb{Z}[x]$ 的**容度（content）**是 $\gcd(a_0,a_1,\dots,a_n)$。容度為 1 的叫**本原多項式（primitive polynomial）**。

**例**（講義 Example 4.6.9）[▶ 04:00](https://youtu.be/pUdxGE7-k_8?t=240)（老師把例子編成「例 1+i」：「我去了**另一個維度**。這是我的課，我想怎麼編號就怎麼編。」）
- $3x+6$ 不是本原的：容度 3，$3x+6 = 3(x+2)$，而 $x+2$ 是本原的。
- **首一（monic）多項式都是本原的**：$\gcd(1,\dots) = 1$。其實只要**任何**係數是 1 就是。
- $3x^2+5x+7$ 本原（係數互質）。
- 「容度的想法：找出**自然地從整係數多項式提出來**的那個整數。」

---

## 2. 本原 × 本原 = 本原；係數約化同態

> **定理**（講義 p.1，Thm 4.6.10）[▶ 06:30](https://youtu.be/pUdxGE7-k_8?t=390)　兩個本原多項式的乘積是本原的。

（「這是我的 Lecture 26，大量建立在 **Gallian** 上——還是 Gallion？我不在乎。我是說我在乎，但**不夠**到去改我的錯。」）【講義補充】「Gallian 叫它 **Gauss 引理**，考慮到 Gauss 的成就，這名字不太有描述性。」

**證明**[▶ 07:00](https://youtu.be/pUdxGE7-k_8?t=420)：$f,g$ 本原，設 $fg$ 不是。【課堂討論】「什麼證法？」學生：「**歸納**。」「抱歉，不是。我確定這裡某處有歸納，我們會找到——但不是這個。這是我**最不喜歡**的證法：**反證**。感覺好空虛。」
- 取 $p$ 是 $fg$ 容度的質因數：$fg = p\,h(x)$。
- **係數約化**[▶ 09:00](https://youtu.be/pUdxGE7-k_8?t=540)：$\overline{c_0+c_1x+\cdots+c_nx^n} = \bar c_0+\bar c_1x+\cdots+\bar c_nx^n\in\mathbb{Z}_p[x]$。（老師想用 Pac-Man 當函數名；學生說用 **oopsilon**。「我本來要改成**海綿寶寶**。」學生：「Detexify 畫笑臉就找得到 Pac-Man 符號。」）
- 約化是**同態**：$0 = \overline{ph} = \overline{fg} = \bar f\cdot\bar g$。
- 【課堂討論】[▶ 17:00](https://youtu.be/pUdxGE7-k_8?t=1020)「$\mathbb{Z}_p[x]$ 是什麼樣的環？」（老師作勢拿 Nerf 槍。）「**整環**。」⇒ $\bar f = 0$ 或 $\bar g = 0$ ⇒ $p$ 整除 $f$（或 $g$）的**每個係數** ⇒ 不是本原，矛盾。$\blacksquare$

**例**[▶ 12:30](https://youtu.be/pUdxGE7-k_8?t=750)：$f = 13x^3+2x^2+x+7$ 模 7：$\bar f = 6x^3+2x^2+x$。「如果特別在意區分物件類型，我會在係數上畫橫線。」

**一般構造**（講義 p.1）[▶ 14:00](https://youtu.be/pUdxGE7-k_8?t=840)：環同態 $\phi:R\to S$ **自然誘導** $\Psi:R[x]\to S[x]$，
$$\Psi(a_nx^n+\cdots+a_0) = \phi(a_n)x^n+\cdots+\phi(a_0).$$
它保持加法、乘法（$\phi$ 把 1 送到 1 時也保持 1）。最常見的就是 $\phi(k) = [k]_p:\mathbb{Z}\to\mathbb{Z}_p$ 這個**商映射**。「這個想法比容度**更重要**——作業裡你們看過一點，**強調『一點』**。」

---

## 3. ℚ 上可約 ⇒ ℤ 上可約

> **定理**（講義 p.1–2，Thm 4.6.11）[▶ 18:30](https://youtu.be/pUdxGE7-k_8?t=1110)　$f(x)\in\mathbb{Z}[x]$。若 $f$ 在 $\mathbb{Q}$ 上可約，則在 $\mathbb{Z}$ 上可約。

**證明概要**（「**強調概要**」）[▶ 19:30](https://youtu.be/pUdxGE7-k_8?t=1170)：
- $\mathbb{Q}$ 是體，非零常數都是單位，所以 $\mathbb{Q}$ 上可約就是 $f = gh$，$g,h$ 次數較小。
- 【課堂討論】[▶ 21:30](https://youtu.be/pUdxGE7-k_8?t=1290)「係數是有理數，怎麼變整數？」學生：「乘……」「最懶的做法：乘上**所有分母的乘積**。」學生：「**最小公倍數**。」「那是**最不懶**的做法。」乘完得到 $\mathbb{Z}$ 上的兩個多項式乘積，左邊多一個整數倍。
- 【講義補充】細節（monic 情形）：$a$、$b$ 是 $h$、$g$ 分母的最小公倍數，$abf = (ah)(bg) = c_hh_1\cdot c_gg_1$，$h_1g_1$ 本原（上一定理）⇒ $abf$ 的容度是 $c_hc_g$；$f$ 首一 ⇒ 容度是 $ab$ ⇒ $ab = c_hc_g$ ⇒ $f = h_1g_1$，次數不變。非首一時先提出容度。

**例 2**（講義 p.2，Example 4.6.12）[▶ 22:30](https://youtu.be/pUdxGE7-k_8?t=1350)：
$$6x^2+19x-7 = 6\Big(x+\tfrac72\Big)\Big(x-\tfrac13\Big) = (2x+7)(3x-1).$$
把 6 拆成 $2\cdot3$ 分給兩個因子，$\mathbb{Q}$ 上的分解就變成 $\mathbb{Z}$ 上的。（老師中途開始配方：「我在幹嘛？**停**。能配方不代表該配方。」）「實務上，這例子一開始就看出 $(2x+7)(3x-1)$ 容易多了。」

【口頭】[▶ 25:00](https://youtu.be/pUdxGE7-k_8?t=1500)「引入容度主要是為了證這個定理——而我**沒給你們完整證明**，抱歉。」

---

## 4. 模 p 約化判別法

> **定理**（講義 p.2，Thm 4.6.13）[▶ 25:30](https://youtu.be/pUdxGE7-k_8?t=1530)　$p$ 質數，$f(x)\in\mathbb{Z}[x]$、$\deg f\ge1$。若 $\bar f\in\mathbb{Z}_p[x]$ **在 $\mathbb{Z}_p$ 上不可約**且 **$\deg\bar f = \deg f$**，則 $f$ 在 $\mathbb{Q}$ 上不可約。

（中間學生在玩手機惡作劇，「應該是 Shane。」）「這是判別不可約**非常重要**的工具。兩大工具：這個，和 **Eisenstein 判別法**。」

**證明**（講義 p.2）[▶ 41:00](https://youtu.be/pUdxGE7-k_8?t=2460)：設 $f$ 在 $\mathbb{Q}$ 上可約 ⇒（Thm 4.6.11）$f = gh$，$g,h\in\mathbb{Z}[x]$、次數都 $<\deg f$。約化：$\bar f = \bar g\bar h$。首項係數可能被 $p$ 整除，所以 $\deg\bar g\le\deg g$——但
$$\deg\bar g\le\deg g<\deg f = \deg\bar f,$$
$\bar h$ 同理 ⇒ $\bar f$ 有**真正的**分解，矛盾。「**次數相等**的條件就用在這裡。」

**例 3**（講義 Example 4.6.14）[▶ 29:00](https://youtu.be/pUdxGE7-k_8?t=1740)：$f = 29x^3+5x^2+2x+1$。
- 「**最容易的質數是 2**，能用就先試 2。」$\bar f = x^3+x^2+1$。
- $\bar f(0) = 1$、$\bar f(1) = 1+1+1 = 1$ ⇒ 沒有根，3 次 ⇒ **$\mathbb{Z}_2$ 上不可約** ⇒ $f$ 在 $\mathbb{Q}$ 上不可約。
- 【口頭】[▶ 31:30](https://youtu.be/pUdxGE7-k_8?t=1890)「別小看這結果：它表示在**無窮多**個有理數裡，**沒有一個**是這個三次式的根。我們只檢查了 $\mathbb{Z}_2$ 的**兩個**數就知道。這定理**真的很好**。」

**例 4**（講義 Example 4.6.15，Gallian p.299）[▶ 33:30](https://youtu.be/pUdxGE7-k_8?t=2010)：$f = 21x^3-3x^2+2x+8$。
- 模 2：$\bar f = x^3+x^2 = x^2(x+1)$，**可約**——「$\mathbb{Z}_2$ 幫不上忙。而且**模 $p$ 可約不代表 $\mathbb{Z}$ 上可約**，這方法**只能證不可約**。」
- 跳過 3，試**模 5**：$\bar f = x^3+2x^2+2x+3$（「用正數比較好算」）。
$$\bar f(0) = 3,\ \bar f(1) = 3,\ \bar f(2) = 3,\ \bar f(3) = -1 = 4,\ \bar f(4) = 2$$
  ⇒ 沒有根 ⇒ $\mathbb{Z}_5$ 上不可約 ⇒ $f$ 在 $\mathbb{Q}$ 上不可約。

**支線任務**（講義 Example 4.6.16，標「SIDE QUEST! +10」）[▶ 36:00](https://youtu.be/pUdxGE7-k_8?t=2160)：
$$x^4+1\ \text{在 }\mathbb{Q}\text{ 上不可約，但對**每個**質數 }p,\ \bar f\text{ 在 }\mathbb{Z}_p\text{ 上都可約}.$$
- 「實際算出來**很可怕**。這定理**有效時很好**，無效時**什麼都不代表**：所有質數都失敗**不代表** $\mathbb{Q}$ 上可約。」
- [▶ 43:00](https://youtu.be/pUdxGE7-k_8?t=2580)「支線任務值 **10 分**。這比 67 秒學會魔術方塊**難多了**。我以前算過，大概三頁。」

（[▶ 32:30](https://youtu.be/pUdxGE7-k_8?t=1950) 關於考試的閒聊：「如果你考試時什麼都會，你就**學不到東西**。」學生：「沒有期末考可以替換成績。」「你們都要畢業了，**還在乎成績幹嘛**？」）

【口頭】[▶ 39:00](https://youtu.be/pUdxGE7-k_8?t=2340)「英文的 reducible 和 irreducible **聽起來太像**了，我腦中常把它們混在一起。」

**例 5**（講義 Example 4.6.17）[▶ 43:30](https://youtu.be/pUdxGE7-k_8?t=2610)：$f = \frac37x^4-\frac27x^2+\frac9{35}x+\frac35$，乘最小公倍數 35：$h = 15x^4-10x^2+9x+21$。模 2：$\bar h = x^4+x+1$。
- 沒有根 ⇒ 沒有一次因子。四次式，所以**只可能**有二次因子，而且必須是**不可約**二次式（否則四次式就有根）。
- $\mathbb{Z}_2$ 上的二次式：$x^2$、$x^2+x$ 有根 0；$x^2+1$ 有根 1（$1+1 = 0$）⇒ **唯一**不可約二次式是 $x^2+x+1$。
- 設 $(x^2+x+1)(x^2+ax+b) = x^4+x+1$ ⇒ $a+1 = 0$、$b+a+1 = 0$、$a+b = 0$、$b = 1$——前兩式給 $b = 0$，最後給 $b = 1$，**不一致** ⇒ 不是因子 ⇒ $\bar h$ 不可約 ⇒ $f$ 在 $\mathbb{Q}$ 上不可約。「不喜歡這個？課後面有更好的看法，**放輕鬆**。」

---

## 5. Eisenstein 判別法；分圓多項式

> **Eisenstein 判別法**（講義 p.3，Thm 4.6.18）[▶ 45:00](https://youtu.be/pUdxGE7-k_8?t=2700)　$f(x) = a_nx^n+\cdots+a_0\in\mathbb{Z}[x]$。若有質數 $p$ 使
> $$p\nmid a_n,\qquad p\mid a_j\ (j = 0,\dots,n-1),\qquad p^2\nmid a_0,$$
> 則 $f$ 在 $\mathbb{Q}$ 上不可約。

- 「另一把**大槍**。比約化**更容易用**，但（至少對我）比較**難記**——只看係數。條件很多，要習慣。」
- 【講義補充】證明延後；老師覺得 Gallian p.321 Example 4 的論證比 p.300 的反證有趣（另一個證明見 [[13-L11-代數數論故事與UFD]] 講義 p.8）。

**例 6**（講義 Example 4.6.19）[▶ 46:30](https://youtu.be/pUdxGE7-k_8?t=2790)：$13x^7+2x^6+4x^3+18x+2$，$p = 2$：$2\nmid13$；$2\mid2,4,18,2$（以及係數 0）；$4\nmid2$ ⇒ 在 $\mathbb{Q}$ 上不可約。

**分圓多項式**[▶ 47:00](https://youtu.be/pUdxGE7-k_8?t=2820)（學生：「我就在想這個。」）
- 【講義補充】$S = 1+x+\cdots+x^{p-1}$，$S-xS = 1-x^p$ ⇒ $S = \frac{x^p-1}{x-1}$（等比級數的推導）。$\Phi_p(x) = x^{p-1}+\cdots+x+1$ **定義**為第 $p$ 個分圓多項式。

> **定理**（講義 p.4，Thm 4.6.20）　$p$ 質數 ⇒ $\Phi_p(x) = x^{p-1}+x^{p-2}+\cdots+x+1$ 在 $\mathbb{Q}$ 上不可約。

**證明**[▶ 48:30](https://youtu.be/pUdxGE7-k_8?t=2910)（「我想下次**慢慢**走一遍——這代數之後對我們很重要。」學生：「還有 8 分鐘。」「你們在**搞什麼**？我有 12 分鐘。」）
- **平移技巧**：令 $f(x) = \Phi_p(x+1)$。二項式定理：
$$f(x) = \frac{(x+1)^p-1}{(x+1)-1} = \frac1x\Big(x^p+\binom p1x^{p-1}+\cdots+\binom p{p-1}x+1-1\Big) = x^{p-1}+px^{p-2}+\cdots+p.$$
- 除首項外每個係數 $\binom pk$ 都被 $p$ 整除，常數項 $p$ 不被 $p^2$ 整除 ⇒ **Eisenstein** ⇒ $f$ 不可約。
- 若 $\Phi_p = gh$（次數 $<p-1$），則 $f(x) = g(x+1)h(x+1)$ 也可約，矛盾。$\blacksquare$
- 【口頭】[▶ 51:00](https://youtu.be/pUdxGE7-k_8?t=3060)「**平移**是另一招：把 $x$ 換成 $x+$ 常數。平移後不可約 ⇒ 原來的不可約。比較難的題常用。」

---

## 6. 不可約 ⟺ 極大；16 元素的體

> **定理**（講義 p.4，Thm 4.6.21）[▶ 51:00](https://youtu.be/pUdxGE7-k_8?t=3060)　$F$ 體，$p(x)\in F[x]$。$\langle p(x)\rangle$ 是 $F[x]$ 的極大理想 $\iff$ $p(x)$ 在 $F$ 上不可約。

> **推論**（講義 Cor 4.6.22）　$p(x)$ 在 $F$ 上不可約 ⇒ $F[x]/\langle p(x)\rangle$ 是**體**。

「我們證過了嗎？……證過了，好。再走一遍證明會很好，但不是今天。」

【講義補充】講義 p.4–5 的證明和推論：
- (⇒) $p = gh$，$\langle p\rangle\subseteq\langle g\rangle$，由極大性 $\langle g\rangle = \langle p\rangle$（$\deg g = \deg p$）或 $= F[x]$（$g$ 是常數）。(⇐) $F[x]$ 是 PID，$\langle p\rangle\subseteq\langle g\rangle$ ⇒ $p = kg$，不可約 ⇒ $k$ 或 $g$ 是常數。
- **Cor 4.6.23**：$p$ 不可約、$p\mid ab$ ⇒ $p\mid a$ 或 $p\mid b$（極大 ⇒ 質理想）。「這是證 $\mathbb{Z}[x]$ 是 UFD 的關鍵。」
- **Thm 4.6.26**：$\mathbb{Z}[x]$ 中每個非零非單位 $f = b_1\cdots b_s\,p_1(x)\cdots p_m(x)$（$b_i$ 是質數、$p_j$ 是正次數不可約多項式），在排序與 $\pm$ 下唯一。證明見 Gallian。
- **E7**：$x^3+x+1$ 在 $\mathbb{Z}_2$ 上不可約 ⇒ $\mathbb{Z}_2[x]/\langle x^3+x+1\rangle$ 是 **8 元素的體**，規則 $x^3 = x+1$，例如 $(x+1)(x^2+x) = 1$。
- **E8**：$\mathbb{Z}_3[x]/\langle x^2+1\rangle\cong\mathbb{Z}_3[i]$，**9 元素的體**。

**例 9：16 元素的體**（講義 p.7–8，新寫）[▶ 52:00](https://youtu.be/pUdxGE7-k_8?t=3120)「這是我**特地為你們寫的**，真的很酷。」$p(x) = x^4+x+1\in\mathbb{Z}_2[x]$。
- **不可約**：$p(0) = p(1) = 1$ ⇒ 沒有一次因子 ⇒ 只能有不可約二次因子，唯一候選 $x^2+x+1$。長除法：
$$x^4+x+1 = (x^2+x+1)(x^2-x)+1,$$
  餘數 1 ⇒ 不整除 ⇒ $p$ 不可約。
- 令 $\beta = x+\langle p(x)\rangle$：
$$\mathbb{Z}_2[x]/\langle x^4+x+1\rangle = \{a\beta^3+b\beta^2+c\beta+d : a,b,c,d\in\mathbb{Z}_2\}.$$
  【課堂討論】[▶ 54:30](https://youtu.be/pUdxGE7-k_8?t=3270)「多大？」「**16**——四個獨立的東西各取兩個值。」（「我列到一半……還有三個，假設我沒重複。我**組合學很爛**。」）
- 乘法表 $16\times16 = 256$ 個乘積（交換、有一行一列是 0、乘 1 很簡單，所以沒那麼多）。
- $\beta^4+\beta+1 = 0$ ⇒ $\beta(\beta^3+1) = 1$ ⇒ **$\beta^{-1} = 1+\beta^3$**、$(\beta^3+1)^{-1} = \beta$。
- **$(\beta^2)^{-1}$**[▶ 56:00](https://youtu.be/pUdxGE7-k_8?t=3360)：從 $\beta^2\cdot\beta^2 = 1+\beta$ 兩邊乘 $\beta^{-1} = 1+\beta^3$、一路化簡，得
$$(\beta^2)^{-1} = 1+\beta^2+\beta^3.$$
  （驗算：$\beta^2+\beta^4+\beta^5 = \beta^2+(1+\beta)+(\beta+\beta^2) = 1$。）「一定有更快的方法，這只是我在**微分方程的學生考試受苦時**摸索出來的。」
- [▶ 57:00](https://youtu.be/pUdxGE7-k_8?t=3420) 投影 Google 算出的乘法表，在 $\beta^2$ 那一行找到 1 的位置：「看！就是我找到的。**Google 證明法**，我一定是對的。」（學生：「Google AI。」）「我還沒想到怎麼把這表**印成合理的樣子**分享給你們。」
- 【口頭】[▶ 58:00](https://youtu.be/pUdxGE7-k_8?t=3480)「任何不可約多項式，商掉它生成的理想就給你一個**新的體**。你們以前有過**16 個元素、特徵 2**（任何東西加自己是 0）的體嗎？我想這是**新的**。有**無窮無盡**的新例子可以找。」

**預告**[▶ 58:30](https://youtu.be/pUdxGE7-k_8?t=3510)：「這份講義是我**弟弟 Bill** 的。我跟他說在講多項式不可約，他說『我有份講義，很好，你該用』。我在微分方程考試時讀了，也確信它**非常非常好**：D&F 第 9 章所有有趣內容的**超濃縮、近乎完整**的複習——除了 Gröbner 基。」→ [[18-L15-多項式理論完結]]

---

## 7. 一頁速查表

### 7.1 判別不可約的工具

| 工具 | 條件 | 結論 |
|---|---|---|
| 2、3 次（體上） | 沒有根 | 不可約（4 次以上**不行**：$(x^2+7)^2$） |
| 本原 × 本原 | | 本原（Gauss 引理） |
| $\mathbb{Q}$ 可約 ⇒ $\mathbb{Z}$ 可約 | | 乘分母、比容度 |
| 模 $p$ 約化 | $\bar f$ 不可約、$\deg\bar f = \deg f$ | $f$ 在 $\mathbb{Q}$ 上不可約（**只能證不可約**） |
| Eisenstein | $p\nmid a_n$、$p\mid a_j$、$p^2\nmid a_0$ | $f$ 在 $\mathbb{Q}$ 上不可約 |
| 平移 | $f(x+c)$ 不可約 | $f$ 不可約 |
| 不可約 ⟺ 極大 | $p$ 在 $F$ 上不可約 | $F[x]/\langle p\rangle$ 是體 |

### 7.2 例子

| 多項式 | 方法 | 結論 |
|---|---|---|
| $29x^3+5x^2+2x+1$ | 模 2 無根 | 不可約 |
| $21x^3-3x^2+2x+8$ | 模 2 失敗、模 5 無根 | 不可約 |
| $x^4+1$ | 每個 $p$ 都可約 | 仍在 $\mathbb{Q}$ 上不可約 |
| $15x^4-10x^2+9x+21$ | 模 2：$x^4+x+1$ 無根、$x^2+x+1\nmid$ | 不可約 |
| $13x^7+2x^6+4x^3+18x+2$ | Eisenstein $p = 2$ | 不可約 |
| $\Phi_p(x)$ | 平移 + Eisenstein | 不可約 |
| $x^4+x+1$ over $\mathbb{Z}_2$ | | 16 元素的體，$\beta^{-1} = 1+\beta^3$ |

### 7.3 術語

| 中文 | English |
|---|---|
| 容度 | content |
| 本原多項式 | primitive polynomial |
| 首一多項式 | monic polynomial |
| Gauss 引理 | Gauss's lemma |
| 模 $p$ 約化 | reduction mod $p$ |
| Eisenstein 判別法 | Eisenstein's criterion |
| 分圓多項式 | cyclotomic polynomial |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **Bill 的講義：第 9 章總複習** | [[18-L15-多項式理論完結]] |
| **$F[x]/\langle p\rangle$ 是體、有限體** | [[20-L16-擴張體基礎與Kronecker定理]]、[[21-L18-擴張體與分裂體]] |
| **分圓多項式** | [[23-L20-分圓體與Galois理論開始]] |
| **特徵 2 的體** | [[22-L19-可分擴張]] |

---

## 附：本集一句話總結

> **四次以上沒有根不代表不可約（$(x^2+7)^2$）；引入容度與本原多項式，證明本原 × 本原 = 本原，所以 $\mathbb{Q}$ 上可約 ⇒ $\mathbb{Z}$ 上可約；由此得到兩把大槍——模 $p$ 約化（$\bar f$ 不可約且次數不降 ⇒ $f$ 在 $\mathbb{Q}$ 上不可約，但反之不成立，$x^4+1$ 在每個 $\mathbb{Z}_p$ 都可約）和 Eisenstein 判別法（配合平移證明 $\Phi_p$ 不可約）；最後用不可約 ⟺ 極大，從 $x^4+x+1$ 造出 16 元素、特徵 2 的體。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 14 錄影逐字稿（YouTube 自動字幕，59:27）與手寫講義 `Math422_Lecture14_IrreduciblePolynomialTheory.pdf`（2018 講義 §4.6，依 Gallian 第 17 章）整理。*
