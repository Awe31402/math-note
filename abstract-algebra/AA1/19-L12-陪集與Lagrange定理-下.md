---
course: Abstract Algebra I (Fall 2016)
episode: 19
lecture: L12
date: 2016-09-28
video: https://www.youtube.com/watch?v=YRCtHmEfxFw
notes: AlgebraInotes_2018.pdf §3.1 Lecture 11（p.82–87）
---

# 第 19 集 · L12（下）：陪集的性質、Lagrange 定理 [▶ 影片](https://www.youtube.com/watch?v=YRCtHmEfxFw&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[18-L12-陪集與Lagrange定理-上]] ｜ [總目錄](../README.md) ｜ 下一集：[[20-答疑課]] →

> **課程**：Abstract Algebra I（Liberty University，Fall 2016）— 第 19 集，Lecture 12（接續上一集）
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（41:16，自動字幕）＋ 講義 `AlgebraInotes_2018.pdf` §3.1「Lecture 11: cosets and Lagrange's Theorem」（p.82–87）＋ Gallian p.135 的引理。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字，依講義補；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 陪集的定義](#1-陪集的定義)
- [2. 例：S₃ 裡 H = {(1), (13)} 的陪集](#2-例s₃-裡-h--1-13-的陪集)
- [3. 定理：a 在自己的陪集裡](#3-定理a-在自己的陪集裡)
- [4. 陪集的性質（Gallian 引理）](#4-陪集的性質gallian-引理)
  - [4.1 aH = H ⟺ a ∈ H](#41-ah--h--a--h)
  - [4.2 陪集要嘛相等、要嘛不相交](#42-陪集要嘛相等要嘛不相交)
  - [4.3 aH = bH ⟺ a⁻¹b ∈ H](#43-ah--bh--a¹b--h)
  - [4.4 每個陪集一樣大](#44-每個陪集一樣大)
  - [4.5 【講義補充】其餘兩條](#45-講義補充其餘兩條)
- [5. Lagrange 定理](#5-lagrange-定理)
- [6. 推論：質數階的群是循環的](#6-推論質數階的群是循環的)
- [7. 【講義補充】更多例子與推論](#7-講義補充更多例子與推論)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

接續上一集（設備沒電中斷）。今天的正題：**陪集**，然後證明 **Lagrange 定理**。

> 📘 講義前言：陪集的概念不新——我們建 $\mathbb{Z}_n$ 時就用過：$[k] = k+n\mathbb{Z}$，$\mathbb{Z}_n$ 的加法其實是在**加整數的集合**。陪集有兩個主要用途：(1) **群裡的計數問題**（今天：Lagrange 定理）；(2) **造商群**（下一講）。講義也提到 Dedekind 是最早在這種層次思考的數學家之一（1858 年用集合——Dedekind 分割——建構實數）。

---

## 1. 陪集的定義

[▶ 00:00](https://youtu.be/YRCtHmEfxFw?t=0)

> **定義（陪集 coset）**　$G$ 是群，$H\subseteq G$（**先不要求是子群**），$a\in G$。
> - **左 $H$-陪集**，代表元 $a$：$aH = \{ah : h\in H\}$。
> - **右 $H$-陪集**，代表元 $a$：$Ha = \{ha : h\in H\}$。
>
> $|aH|$、$|Ha|$ 表示它們的元素個數 [▶ 02:00](https://youtu.be/YRCtHmEfxFw?t=120)。

【口頭】[▶ 00:30](https://youtu.be/YRCtHmEfxFw?t=30)「我沒說 $H$ 是子群。它可能是，也可能不是，我暫時不承諾。」[▶ 01:00](https://youtu.be/YRCtHmEfxFw?t=60)「本來想說『包含 $a$ 的左陪集』——等等，誰說它包含 $a$？如果 $H$ 不是子群，不一定包含。所以就說『**代表元**是 $a$ 的左陪集』。」

**加法群**[▶ 01:30](https://youtu.be/YRCtHmEfxFw?t=90)【課堂討論】陪集長什麼樣？$a+H$ 和 $H+a$。（加法群通常交換，所以兩者相等。）

---

## 2. 例：S₃ 裡 H = {(1), (13)} 的陪集

[▶ 03:00](https://youtu.be/YRCtHmEfxFw?t=180)「我照書上的例子，我很喜歡。」
$$G = S_3,\qquad H = \{(1),(1\,3)\}.$$

逐一計算左陪集（乘法從右往左）：

| 代表元 | 陪集 | 計算 |
|---|---|---|
| $(1)$ | $\{(1),(1\,3)\}$ | 就是 $H$ |
| $(1\,3)$ [▶ 04:00](https://youtu.be/YRCtHmEfxFw?t=240) | $\{(1\,3),(1)\}$ | $(1\,3)^2 = (1)$（換位的階是 2） |
| $(1\,2)$ [▶ 04:30](https://youtu.be/YRCtHmEfxFw?t=270) | $\{(1\,2),(1\,3\,2)\}$ | $(1\,2)(1\,3)$：$1\to3\to3$、$3\to1\to2$、$2\to2\to1$ ⇒ $(1\,3\,2)$ |
| $(1\,3\,2)$ [▶ 05:00](https://youtu.be/YRCtHmEfxFw?t=300) | $\{(1\,3\,2),(1\,2)\}$ | $(1\,3\,2)(1\,3) = (1\,2)$ |
| $(2\,3)$ [▶ 06:00](https://youtu.be/YRCtHmEfxFw?t=360) | $\{(2\,3),(1\,2\,3)\}$ | $(2\,3)(1\,3)$：$1\to3\to2$、$2\to2\to3$、$3\to1\to1$ ⇒ $(1\,2\,3)$ |
| $(1\,2\,3)$ | $\{(1\,2\,3),(2\,3)\}$ | 短計算 |

$S_3$ 六個元素都當過代表元了 [▶ 07:00](https://youtu.be/YRCtHmEfxFw?t=420)。所以只有**三個不同的陪集**：
$$H = \{(1),(1\,3)\},\quad(1\,2)H = \{(1\,2),(1\,3\,2)\},\quad(2\,3)H = \{(2\,3),(1\,2\,3)\}.$$

**觀察**：
- $(1\,2)H = (1\,3\,2)H$：同一個陪集可以用不同的代表元。
- 三個陪集**互不相交**，聯集是整個 $S_3$。
- 每個陪集都有 **2 個**元素。

【課堂討論】[▶ 07:30](https://youtu.be/YRCtHmEfxFw?t=450)「這個 $H$ 有什麼特別的，是我在定義裡沒承諾的？」答：**$H$ 是子群**——事實上是循環子群 $\langle(1\,3)\rangle$。

---

## 3. 定理：a 在自己的陪集裡

[▶ 08:00](https://youtu.be/YRCtHmEfxFw?t=480)「今天許多定理裡的第一個。」

> **定理**　若 $H\le G$，則 $a\in aH$ 且 $a\in Ha$。

「答案閉著眼睛都會。」**證明**[▶ 08:30](https://youtu.be/YRCtHmEfxFw?t=510)：$H$ 是子群，所以 $e\in H$。
$$a = ae\in aH,\qquad a = ea\in Ha.\qquad\blacksquare$$

**為什麼要子群**[▶ 09:00](https://youtu.be/YRCtHmEfxFw?t=540)：如果 $H$ 不是子群，代表元**不保證**在陪集裡——「你可能把每個元素都乘離 $a$，永遠回不來。」

---

## 4. 陪集的性質（Gallian 引理）

[▶ 09:30](https://youtu.be/YRCtHmEfxFw?t=570)（Gallian p.135 的引理；老師稱為定理。）

> **定理**（講義 Prop 3.1.2）　$H\le G$，$a,b\in G$。
> 1. $aH = H\iff a\in H$。
> 2. $aH = bH$ 或 $aH\cap bH = \varnothing$（要嘛相等，要嘛不相交）。
> 3. $aH = bH\iff a^{-1}b\in H$。
> 4. $|aH| = |bH|$。
> 5. $aH = Ha\iff H = aHa^{-1}$。
> 6. $aH\le G\iff a\in H$。

（講義把「$a\in aH$」列為 (i)，所以講義的編號是 (ii)–(vii)；課堂編號少一。）

【口頭】[▶ 10:30](https://youtu.be/YRCtHmEfxFw?t=630)「我應該把這頁撕下來，但我不忍心撕 Gallian。微積分課本不一樣——這不是微積分課本，比較像**藝術品**，不是粗糙的工具。」[▶ 12:30](https://youtu.be/YRCtHmEfxFw?t=750)「第 6 條好像沒必要，但無所謂。」

### 4.1 aH = H ⟺ a ∈ H

[▶ 13:00](https://youtu.be/YRCtHmEfxFw?t=780)

**(⇒)** 設 $aH = H$。$a = ae\in aH = H$。（「這幾乎就是剛才的定理。」）

**(⇐)**[▶ 14:00](https://youtu.be/YRCtHmEfxFw?t=840) 設 $a\in H$。
- **$aH\subseteq H$**：設 $x\in aH$，$x = ah$，$h\in H$。$a\in H$、$h\in H$，$H$ 是子群，所以 $x = ah\in H$ [▶ 15:00](https://youtu.be/YRCtHmEfxFw?t=900)。
- **$H\subseteq aH$**[▶ 16:00](https://youtu.be/YRCtHmEfxFw?t=960)：設 $y\in H$。
$$y = a(a^{-1}y),$$
  而 $a^{-1}\in H$、$y\in H$，所以 $a^{-1}y\in H$，$y\in aH$ [▶ 17:00](https://youtu.be/YRCtHmEfxFw?t=1020)。

（老師中途寫反了包含方向，學生指出：「如果看到什麼，就說出來。」[▶ 16:30](https://youtu.be/YRCtHmEfxFw?t=990)）

所以 $aH = H$。$\blacksquare$

### 4.2 陪集要嘛相等、要嘛不相交

[▶ 18:00](https://youtu.be/YRCtHmEfxFw?t=1080)**策略**：證明「若 $aH\cap bH\neq\varnothing$，則 $aH = bH$」。「這合邏輯吧？」

設 $x\in aH\cap bH$ [▶ 19:00](https://youtu.be/YRCtHmEfxFw?t=1140)。存在 $h_1,h_2\in H$ 使
$$x = ah_1 = bh_2.$$

【課堂討論】「這說 $a$ 和 $b$ 有什麼關係？」
$$b = xh_2^{-1} = ah_1h_2^{-1}.$$
$h_1h_2^{-1}\in H$，所以 **$b\in aH$**[▶ 20:00](https://youtu.be/YRCtHmEfxFw?t=1200)。

（老師想直接用 4.1 推出，然後發現不行：「不，我錯了。你們的方向對。」）

**證 $bH\subseteq aH$**[▶ 21:00](https://youtu.be/YRCtHmEfxFw?t=1260)：設 $y\in bH$，$y = bh_3$。
$$y = bh_3 = (xh_2^{-1})h_3 = (ah_1)h_2^{-1}h_3 = a(h_1h_2^{-1}h_3)\in aH.$$
（「我不該擦掉剛才的東西，我是白痴。」）

**反方向**[▶ 23:00](https://youtu.be/YRCtHmEfxFw?t=1380)：同理 $aH\subseteq bH$。「敘述對 $a$、$b$ 是對稱的，能對 $a$ 證就能對 $b$ 證，所以『同理』不算什麼跳躍。」

所以 $aH = bH$。$\blacksquare$

（中間手機響了：「一位以前在這裡工作的老師，他的手機會不時打給我——十次大概有一次是真的要跟我講話。我歡迎這種電話。我們這裡沒人像他那樣深刻地理解拓樸，很可惜。」）

### 4.3 aH = bH ⟺ a⁻¹b ∈ H

[▶ 24:00](https://youtu.be/YRCtHmEfxFw?t=1440)「**實際操作上，這就是檢查陪集相等的方法。**」

**加法版**[▶ 24:30](https://youtu.be/YRCtHmEfxFw?t=1470)【課堂討論】：$a+H = b+H\iff -a+b\in H$，也就是 **$b-a\in H$**。（這正是 $\mathbb{Z}_n$ 的「$a\equiv b\iff n\mid(b-a)$」。）

**(⇒)**[▶ 25:00](https://youtu.be/YRCtHmEfxFw?t=1500)

老師第一次：$a\in aH = bH$ ⇒ $a = bh$ ⇒ $h = b^{-1}a$……「我沒證出我要的，但這是真的。」[▶ 26:00](https://youtu.be/YRCtHmEfxFw?t=1560)（得到的是 $b^{-1}a\in H$。）

**換一條路**：$b\in bH = aH$ ⇒ 存在 $h_2\in H$ 使 $b = ah_2$ ⇒
$$h_2 = a^{-1}b\in H.\ ✓$$
「如果一開始選這條路，馬上就得到我們要的。抱歉，計畫不周。」

**(⇐)**[▶ 27:30](https://youtu.be/YRCtHmEfxFw?t=1650) 設 $a^{-1}b = h\in H$。則 $b = ah$ [▶ 28:30](https://youtu.be/YRCtHmEfxFw?t=1710)。
- $b\in bH$（第 3 節）。
- $b = ah\in aH$。
- 所以 $b\in aH\cap bH$，交集不空 [▶ 29:00](https://youtu.be/YRCtHmEfxFw?t=1740)。
- 由 4.2，$aH = bH$。$\blacksquare$

> 📘 講義的 (⇐) 更直接：$b = ah$ ⇒ $bH = ahH = aH$（因為 $hH = H$，由 4.1）。

### 4.4 每個陪集一樣大

[▶ 30:00](https://youtu.be/YRCtHmEfxFw?t=1800)「怎麼證 $|aH| = |bH|$？在例子裡是對的：2、2、2。」「我得看一下時間……其實我可以很快證完。」

**定義映射**[▶ 31:00](https://youtu.be/YRCtHmEfxFw?t=1860)：
$$\varphi:aH\to bH,\qquad\varphi(ax) = bx\quad(x\in H).$$
「不難看出這是一對一的映射。所以這兩個集合的大小一定一樣：一個元素對到一個元素。」

> 📘 講義的版本：$f(x) = ba^{-1}x$。
> - **映成**：任意 $bh\in bH$，$f(ah) = ba^{-1}ah = bh$。
> - **一對一**：$ba^{-1}x = ba^{-1}y$ ⇒ 左乘 $(ba^{-1})^{-1}$ ⇒ $x = y$。
> - 雙射 ⇒ $|aH| = |bH|$。

特別地，$|aH| = |eH| = |H|$：**每個陪集都跟 $H$ 一樣大**。

### 4.5 【講義補充】其餘兩條

課堂沒時間證，講義有：

**(5) $aH = Ha\iff H = aHa^{-1}$**
- (⇒) $x = aha^{-1}$。$ah\in aH = Ha$，所以 $ah = ka$，$k\in H$。$x = kaa^{-1} = k\in H$。另一方向類似。
- (⇐) $aH = a(a^{-1}Ha) = Ha$。（講義證的是 $a^{-1}Ha = H$ 版本，等價。）

**(6) $aH\le G\iff a\in H$**
- (⇒) 子群含 $e$，所以存在 $h\in H$ 使 $ah = e$，即 $a = h^{-1}\in H$。
- (⇐) $a\in H$ ⇒ $aH = H\le G$。

---

## 5. Lagrange 定理

[▶ 32:00](https://youtu.be/YRCtHmEfxFw?t=1920)「這帶我們到**最宏偉的定理**：」

> **定理（Lagrange 定理）**　$G$ 是**有限群**，$H\le G$。則
> $$|H|\ \text{整除}\ |G|.$$
> 而且 $H$ 在 $G$ 中**不同的左（或右）陪集**的個數是
> $$\frac{|G|}{|H|}.$$

**驗證例子**[▶ 33:30](https://youtu.be/YRCtHmEfxFw?t=2010)：$|H| = 2$，$|S_3| = 6$，$6/2 = 3$——正好是我們找到的三個陪集。

**證明**[▶ 33:30](https://youtu.be/YRCtHmEfxFw?t=2010)【口頭】「這是我在這門課**最喜歡**的證明之一。美得簡單。」

1. **$G$ 是陪集的不相交聯集**[▶ 34:00](https://youtu.be/YRCtHmEfxFw?t=2040)：
$$G = a_1H\cup a_2H\cup\cdots\cup a_kH,\qquad a_iH\cap a_jH = \varnothing\ (i\neq j).$$
   **為什麼可以這樣寫**[▶ 34:30](https://youtu.be/YRCtHmEfxFw?t=2070)：
   - 每個 $a\in G$ 至少在一個陪集裡：$a\in aH$（第 3 節）。
   - 陪集要嘛相等、要嘛不相交（4.2），所以每個元素**恰好在一個**陪集裡。
   - 同一個陪集可以有不同的標籤（例如 $(1\,2)H = (1\,3\,2)H$），「但包含 $(1\,2)$ 的陪集只有一個」[▶ 35:00](https://youtu.be/YRCtHmEfxFw?t=2100)。
   - $G$ 有限，所以只有有限多個。
2. 不失一般性，令 $a_1 = e$，第一個就是 $H$ 本身 [▶ 36:00](https://youtu.be/YRCtHmEfxFw?t=2160)。
3. 由 4.4，$|a_iH| = |H|$ 對每個 $i$。
4. **數一數**[▶ 36:30](https://youtu.be/YRCtHmEfxFw?t=2190)：
$$|G| = |H|+|a_2H|+\cdots+|a_kH| = \underbrace{|H|+\cdots+|H|}_{k\text{ 個}} = k|H|.$$
5. 所以 $|H|\mid|G|$，而且陪集個數 $k = |G|/|H|$。$\blacksquare$

【口頭】[▶ 37:00](https://youtu.be/YRCtHmEfxFw?t=2220)「希望你們欣賞這個論證有多簡單。如果我能照我的意思，我會在講循環群**之前**證它——用它可以更容易地證明循環群的某些事。不過循環群的那些也沒那麼難。」

> **定義（指數 index）**[▶ 37:30](https://youtu.be/YRCtHmEfxFw?t=2250)　$H$ 在 $G$ 中不同陪集的個數，記作 $[G:H]$。

Lagrange 定理可以改寫：
$$[G:H] = \frac{|G|}{|H|}\quad(G\text{ 有限}).$$

**無限群**[▶ 38:30](https://youtu.be/YRCtHmEfxFw?t=2310)：「無限的情況不能數數，但陪集**仍然把群分割**成互不相交的塊。這個在無限情況下仍然有意義。」

> 📘 講義：Lagrange 在群論完整成形**之前**就發現了這個定理，就像之前的 Ruffini。「在數學裡，我們常常先找到大故事的一部分，才知道整個故事。現在的 **Langlands 綱領**也有類似的事。」
>
> 講義也提醒：「**加入 Lagrange 定理是改變遊戲規則的事。**」之前作業第 28 題，有人在只知道 $G$ 交換時假設 $G$ 循環，老師不滿意——「回頭看，如果當時已經知道 Lagrange 定理，那個（當時錯的）解法也許是對的。這門課的挑戰之一是追蹤工具箱裡有什麼。」

---

## 6. 推論：質數階的群是循環的

[▶ 39:00](https://youtu.be/YRCtHmEfxFw?t=2340)

> **推論**　質數階的群是循環群。

**證明**[▶ 39:30](https://youtu.be/YRCtHmEfxFw?t=2370)：設 $|G| = p$，$p$ 質數。取 $a\in G$，$a\neq e$。
1. $\langle a\rangle\le G$，由 Lagrange，$|\langle a\rangle|$ 整除 $p$ [▶ 40:00](https://youtu.be/YRCtHmEfxFw?t=2400)。
2. $p$ 是質數，所以 $|\langle a\rangle| = 1$ 或 $p$。
3. $a\neq e$，所以 $|a|\neq1$ [▶ 40:30](https://youtu.be/YRCtHmEfxFw?t=2430)。
4. 因此 $|\langle a\rangle| = p$，$\langle a\rangle = G$。$\blacksquare$

【口頭】「所以如果你給我一個 17 階的群，它是循環的。這是我們以前沒有的，而且得到它一點都不難。陪集的概念**已經在大大地回本了**，而且會一直這樣。這是非常非常強大的概念。」

> 📘 講義補充：證明也顯示**每個非單位元素都是生成元**。

---

## 7. 【講義補充】更多例子與推論

**例**（講義 Ex 3.1.3、3.1.5）：
- $\mathbb{Z}_6$，$H = \langle3\rangle = \{0,3\}$：陪集 $\{0,3\}$、$\{1,4\}$、$\{2,5\}$。$[\mathbb{Z}_6:H] = 3$。
- $\mathbb{Z}_{100}$，$H = \{0,20,40,60,80\}$：20 個陪集 $H,1+H,\dots,19+H$。$[\mathbb{Z}_{100}:H] = 20$。

**線性代數裡的陪集**（Ex 3.1.6–3.1.7）：
- $Ax = b$ 的解集是 $x_p+\operatorname{Null}(A)$——**非齊次方程組的解集是一個陪集**。
- 子空間 $W$ 的陪集 $p+W$ 是把 $W$ 平移到 $p$ 的平行物件。$\mathbb{R}^2$ 裡過原點的直線 $W$，陪集就是所有平行線；它們由 $W^\perp$ 上的點標記。

**$SL(n,\mathbb{R})$ 的陪集**（Ex 3.1.8）：
$$gSL(n,\mathbb{R}) = SL(n,\mathbb{R})g = \{B : \det B = \det g\}.$$
「特殊線性群的陪集就是**行列式相同的矩陣**所成的集合。」（左右陪集相同。）

**推論**：
- **Cor 3.1.10**：有限群中，**$|a|$ 整除 $|G|$**（因為 $|a| = |\langle a\rangle|$）。
- **Cor 3.1.12**：有限群中，**$a^{|G|} = e$**。（$|G| = k|a|$，$a^{|G|} = (a^{|a|})^k = e$。）

**7 階以下的群分類**（§3.1.1）：
- 1、2、3、5、7 階：質數（或 1），只有循環群。
- **4 階**：有 4 階元素 ⇒ $\cong\mathbb{Z}_4$；沒有 ⇒ 三個非單位元素都是 2 階，Cayley 表被**逼成** Klein 四元群的樣子 ⇒ $\cong\mathbb{Z}_2\times\mathbb{Z}_2$。
- **6 階**：$\cong\mathbb{Z}_6$ 或 $S_3$（細節留給讀者）。

| 階 | 代表 |
|---|---|
| 1 | $\{e\}$ |
| 2 | $\mathbb{Z}_2$ |
| 3 | $\mathbb{Z}_3$ |
| 4 | $\mathbb{Z}_4$、$\mathbb{Z}_2\times\mathbb{Z}_2$ |
| 5 | $\mathbb{Z}_5$ |
| 6 | $\mathbb{Z}_6$、$S_3$ |
| 7 | $\mathbb{Z}_7$ |

例：$|A_3| = 3$，所以 $A_3\cong\mathbb{Z}_3$——「不需要寫出同構，因為所有 3 階群都同構。」

---

## 8. 一頁速查表

### 8.1 定義

| 名稱 | 內容 |
|---|---|
| 左陪集 | $aH = \{ah : h\in H\}$；加法 $a+H$ |
| 右陪集 | $Ha = \{ha : h\in H\}$ |
| 指數 | $[G:H]$ = 不同陪集的個數 |

### 8.2 陪集性質（$H\le G$）

| 性質 | 關鍵一步 |
|---|---|
| $a\in aH$ | $a = ae$ |
| $aH = H\iff a\in H$ | ⇐：$ah\in H$；$y = a(a^{-1}y)$ |
| 相等或不相交 | $x = ah_1 = bh_2$ ⇒ $b = ah_1h_2^{-1}$ ⇒ $bh_3 = a(h_1h_2^{-1}h_3)$ |
| $aH = bH\iff a^{-1}b\in H$ | ⇒：$b\in aH$；⇐：$b\in aH\cap bH$ |
| $\lvert aH\rvert = \lvert bH\rvert = \lvert H\rvert$ | $ax\mapsto bx$ 是雙射 |
| $aH = Ha\iff aHa^{-1} = H$ | 講義 |
| $aH\le G\iff a\in H$ | 講義 |

**加法版**：$a+H = b+H\iff b-a\in H$。

### 8.3 Lagrange 定理與推論

| 結果 | 關鍵一步 |
|---|---|
| $\lvert H\rvert$ 整除 $\lvert G\rvert$；$[G:H] = \lvert G\rvert/\lvert H\rvert$ | $G$ = 不相交的陪集聯集，每個 $\lvert H\rvert$ 個元素 ⇒ $\lvert G\rvert = k\lvert H\rvert$ |
| $\lvert a\rvert$ 整除 $\lvert G\rvert$ | $\lvert a\rvert = \lvert\langle a\rangle\rvert$ |
| $a^{\lvert G\rvert} = e$ | $\lvert G\rvert = k\lvert a\rvert$ |
| 質數階 ⇒ 循環 | 非單位元素的階整除 $p$，不是 1，所以是 $p$ |

### 8.4 術語

| 中文 | English |
|---|---|
| 陪集；左陪集；右陪集 | coset; left coset; right coset |
| 代表元 | representative |
| 指數 | index $[G:H]$ |
| Lagrange 定理 | Lagrange's Theorem |
| 分割 | partition |
| 不相交聯集 | disjoint union |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **陪集、$aH = Ha$** | [[21-L13-商群與直積]]：正規子群（$aH = Ha$ 對所有 $a$）、商群 $G/H$ |
| **$aH = bH\iff a^{-1}b\in H$** | [[21-L13-商群與直積]]：商群運算的良定義；[[20-答疑課]]：良定義 |
| **Lagrange 定理** | [[24-答疑課]]：Lagrange 習題；[[28-L19-軌道穩定子定理]]：$\lvert G\rvert = \lvert\mathcal O(x)\rvert\lvert G_x\rvert$ 就是 $[G:G_x] = \lvert G\rvert/\lvert G_x\rvert$ |
| **$a^{\lvert G\rvert} = e$** | [[26-L17-一點數論]]：Fermat 小定理、Euler 定理（取 $G = U(n)$） |
| **Lagrange 逆命題不成立** | [[22-L14-邁向第一同構定理]]：$A_4$ 沒有 6 階子群 |
| **小階群分類** | [[22-L14-邁向第一同構定理]]、[[31-答疑課]]：6 階群 |
| **左乘作用的軌道是右陪集** | [[27-L18-群作用]] |

---

## 附：本集一句話總結

> **子群 $H$ 的陪集 $aH$ 有三個關鍵性質：包含自己的代表元、要嘛相等要嘛不相交（$aH = bH\iff a^{-1}b\in H$）、而且每個都跟 $H$ 一樣大；所以有限群 $G$ 被切成 $k$ 塊大小都是 $|H|$ 的陪集，$|G| = k|H|$——這就是 Lagrange 定理，立刻推出元素的階整除群的階、$a^{|G|} = e$、質數階的群一定循環。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra I」(Fall 2016) Lecture 12 後半錄影逐字稿（YouTube 自動字幕，41:16）與講義 `AlgebraInotes_2018.pdf` §3.1（p.82–87）整理。*
