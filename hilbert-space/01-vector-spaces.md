---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 1
lecture: Lecture 1
date: 2023-01-16
video: https://youtu.be/gQZxz7p8KTY （part 1）、https://youtu.be/h3qIa7X1btQ （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.1–1.2（書頁 1–8，PDF 頁 20–27）
---

# 第 1 集 · Lecture 1：向量空間（Vector Spaces） [▶ 影片](https://youtu.be/gQZxz7p8KTY)

← 上一集：無 ｜ [總目錄](README.md) ｜ 下一集：[02-normed-spaces](02-normed-spaces.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 1 集
> **講者**：James Cook（⚠️ 待確認，見清單）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 0:46，自動字幕）＋ Debnath & Mikusiński《Hilbert Spaces with Applications》§1.1–1.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 課程地圖](#1-課程地圖)
- [2. 向量空間的定義](#2-向量空間的定義)
  - [2.1 老師的寫法：加法是交換群](#21-老師的寫法加法是交換群)
  - [2.2 課本的寫法](#22-課本的寫法)
- [3. 例子](#3-例子)
  - [3.1 Rᴺ 與 Cᴺ](#31-rᴺ-與-cᴺ)
  - [3.2 函數空間](#32-函數空間)
  - [3.3 子空間：C(Ω)、Cᵏ(Ω)、C^∞(Ω)、P(Ω)](#33-子空間cωcᵏωcωpω)
  - [3.4 可微但導數不連續的函數](#34-可微但導數不連續的函數)
  - [3.5 數列空間](#35-數列空間)
  - [3.6 ℓᵖ 空間](#36-ℓᵖ-空間)
- [4. Hölder 與 Minkowski 不等式](#4-hölder-與-minkowski-不等式)
  - [4.1 Young 不等式](#41-young-不等式)
  - [4.2 Hölder 不等式](#42-hölder-不等式)
  - [4.3 Minkowski 不等式](#43-minkowski-不等式)
- [5. 直積](#5-直積)
- [6. 線性獨立、span、基底、維度](#6-線性獨立span基底維度)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

第一堂課。先講整門課的地圖，再從課本第一節開始：複習向量空間，看一堆例子，特別是**函數空間**和**數列空間**——這些就是之後 Banach 空間、Hilbert 空間的主角。

| 主題 | 課本 |
|---|---|
| 課程地圖：各章在講什麼 | 目錄、§1.1 |
| 向量空間定義 | Definition 1.2.1，p. 2 |
| 例子：Rᴺ、Cᴺ、函數空間 | Example 1.2.2–1.2.3，p. 3 |
| 子空間：C(Ω)、Cᵏ(Ω)、C^∞(Ω)、P(Ω) | Example 1.2.4，p. 4 |
| 數列空間、ℓᵖ 空間 | Example 1.2.5–1.2.6，pp. 4–5 |
| Hölder、Minkowski 不等式（課堂跳過） | Theorem 1.2.7–1.2.8，pp. 5–7 |
| 直積 | Example 1.2.9，p. 7 |
| 線性獨立、span、基底、維度 | pp. 7–8 |

講者的起點：兩位學生都修過實分析（課本用 Bartle），所以這門課當成「第二門分析課」，直接從課本開頭往下教。[▶ 00:04](https://youtu.be/gQZxz7p8KTY?t=4)

---

## 1. 課程地圖

[▶ 01:44](https://youtu.be/gQZxz7p8KTY?t=104)

講者說的書名是「Introduction to Hilbert Spaces with Applications」，作者 Lokenath Debnath 和 Piotr Mikusiński。⚠️ 逐字稿缺字：字幕把作者名聽成「loknath debnath and Peter mccoons makoonski」。我們手上的 PDF 是第 3 版，書名是《Hilbert Spaces with Applications》。版本是否相同見待確認清單。

這本書定位在「大學高年級到研究所入門」，也是這門課要的程度。各章安排：

| 章 | 主題 | 講者的說法 |
|---|---|---|
| 1 | 賦範向量空間（normed vector spaces） | 今天開始。重點例子是函數空間。章末是壓縮映射與 **Banach 不動點定理**，講者想用它證一個存在唯一性定理：「分析裡大部分有趣的存在唯一性定理，某種意義上都來自壓縮映射」。【口頭】 |
| 2 | Lebesgue 積分 | 比 Riemann 積分更好用的積分理論（見下面的例子）。§2.10 比較兩者。 |
| 3 | 內積空間、Hilbert 空間 | 抽象的「點積」。 |
| 4 | Hilbert 空間上的線性算子 | |
| 5 | 積分方程、微分方程的應用 | 主要是證明微分方程課裡「直接拿來用」的存在唯一性。講者可能提前到第 1 章末就講。 |
| 6 | 廣義函數與偏微分方程 | 講者提到 §6.5 的「橢圓邊界值問題的弱解」，是比較成熟的微分方程觀點，他自己也想多學。【口頭】 |
| 7 | 量子力學的數學基礎 | **選這本書的真正原因**：兩位學生都對量子力學有興趣。物理課常常「只教記號」，這一章把框架講清楚，例如 Schrödinger 繪景和 Heisenberg 繪景的差別。【口頭】 |
| 8 | 小波 | 不教。 |
| 9 | 最佳化與其他應用 | 不教，有時間可能講 §9.2 的 Gâteaux 與 Fréchet 微分。⚠️ 逐字稿缺字：字幕是「the guitar … and for shade differentials」，依課本目錄 §9.2 修正。 |

### 幾個名詞先給定義

講者在地圖裡先用文字說了兩個定義，正式定義在後面幾集：

- **Cauchy 數列**：項跟項之間越來越近的數列。精確說，對每個 $\varepsilon>0$，存在 $N$，使得 $m,n>N$ 時 $\|x_m-x_n\|<\varepsilon$。
- **完備（complete）**：空間裡每個 Cauchy 數列都收斂到空間**裡面**的點。
- **Banach 空間** = 完備的賦範向量空間（complete normed linear space）。
- **Hilbert 空間** = 完備的內積空間。

⚠️ 逐字稿缺字：字幕把 Banach 聽成「Bannock / binoc / banoc」，Lebesgue 聽成「lebay / lesbiscu」，Cauchy 聽成「koshy」。

### 為什麼需要 Lebesgue 積分：一個例子【口頭】

[▶ 03:23](https://youtu.be/gQZxz7p8KTY?t=203)

微積分裡有一條「顯然」的性質：

$$\int_a^b f\,dx+\int_b^c f\,dx=\int_a^c f\,dx.$$

微積分課都是畫圖帶過：左邊面積加右邊面積。可是如果真的**從 Riemann 積分的定義**證，要把 $[a,c]$ 的分割拆成 $[a,b]$ 和 $[b,c]$ 兩段的分割，再重新編號，講者說這「出奇地技術性」，他花了很久才寫出來。換成 Lebesgue 的觀點，這件事幾乎一行就證完。

講者也提醒：這本書有不少地方用複數。有些東西在實數上做，有些在複數上做。[▶ 05:39](https://youtu.be/gQZxz7p8KTY?t=339)

---

## 2. 向量空間的定義

### 2.1 老師的寫法：加法是交換群

[▶ 14:32](https://youtu.be/gQZxz7p8KTY?t=872)

課本用 $\mathbb{F}$ 代表純量的體（field）：$\mathbb{F}=\mathbb{R}$ 或 $\mathbb{C}$。寫 $\mathbb{F}$ 的定理代表「實數、複數都成立」。

**向量空間（vector space）**：一個非空集合 $E$，加上兩個運算

- 加法 $E\times E\to E$，$(x,y)\mapsto x+y$；
- 純量乘法（scalar multiplication）$\mathbb{F}\times E\to E$，$(\lambda,x)\mapsto \lambda x$。

講者在黑板上寫的規則（部分沒唸出來，依口述重建）：

1. $x+y=y+x$
2. $(x+y)+z=x+(y+z)$
3. $x+0=x$
4. $-x+x=0$
5. $c(x+y)=cx+cy$
6. $(a+b)x=ax+bx$
7. $a(bx)=(ab)x$
8. $1x=x$

[▶ 16:16](https://youtu.be/gQZxz7p8KTY?t=976) 講者的讀法：

- **2、3、4 說的是**：只看加法的話，$E$ 是一個**群（group）**。群就是「有一個運算，滿足結合律，有單位元素（這裡是 $0$），每個元素都有反元素（這裡是 $-x$）」。
- **再加上 1**：這個群是**交換群（abelian group）**，也就是運算可以交換順序。講者說：習慣上只要用「$+$」當符號，就默認是交換的。【口頭】
- **5、6 是兩種「分配律」**。講者說它們不完全是分配律，因為一邊是純量、一邊是向量，它們其實是在**定義**純量乘法要怎麼跟加法相處。[▶ 17:23](https://youtu.be/gQZxz7p8KTY?t=1043)
- **8 不能省**：體裡的數字 $1$ 乘上向量，必須得到原來的向量。

$\mathbb{F}=\mathbb{R}$ 叫**實向量空間**，$\mathbb{F}=\mathbb{C}$ 叫**複向量空間**。

### 2.2 課本的寫法

【課本補充】Definition 1.2.1，p. 2。

課本的規則是 (a)–(g)：(a) 交換律、(b) 結合律、(d)–(g) 同上面 5–8。差別在 (c)：

> (c) 對任意 $x,y\in E$，存在 $z\in E$ 使得 $x+z=y$。

課本**沒有**直接假設零向量和負向量，而是從 (c) 推出來。

**零向量存在而且唯一。**

1. 先固定一個 $x$。由 (c)（取 $y=x$），有某個 $z_x$ 使得 $x+z_x=x$。
2. 這個 $z_x$ 對**每個** $y$ 都有效：由 (c) 取 $w$ 使 $x+w=y$，則
   $$y+z_x=(x+w)+z_x=(x+z_x)+w=x+w=y.$$
   （中間用了 (a)、(b) 換順序。）
3. 唯一：如果 $z_1,z_2$ 都有這個性質，則 $z_1+z_2=z_1$（$z_2$ 的性質），也 $z_1+z_2=z_2$（$z_1$ 的性質，配合交換律）。所以 $z_1=z_2$。

這個唯一的元素記作 $0$。同樣的論證可證 (c) 裡的 $z$ 唯一，記作 $y-x$；$-x$ 定義成 $0-x$。

課本接著列出幾個簡單性質：$\lambda\ne 0$ 且 $\lambda x=0$ ⟹ $x=0$；$x\ne 0$ 且 $\lambda x=0$ ⟹ $\lambda=0$；$0x=0$；$(-1)x=-x$。

**兩種寫法是一樣的。** 以下**不是逐字稿內容**，是依課本定義推論的：

- 老師的寫法 ⟹ 課本的 (c)：取 $z=y+(-x)$，則 $x+z=x+(-x)+y=0+y=y$。
- 課本的寫法 ⟹ 老師的 3、4：上面已證出 $0$；取 $y=0$，(c) 給出 $z$ 使 $x+z=0$，這就是 $-x$。

---

## 3. 例子

### 3.1 Rᴺ 與 Cᴺ

[▶ 17:57](https://youtu.be/gQZxz7p8KTY?t=1077)

⚠️ 逐字稿缺字：這段字幕很亂（「um RN number two CN um oh oh yeah I don't know where I am I'm infinitely different」），依課本 Example 1.2.2 重建。

- $\{0\}$ 是向量空間。
- $\mathbb{R}$、$\mathbb{C}$ 是最簡單的非平凡向量空間。$\mathbb{C}$ 可以看成實向量空間，也可以看成複向量空間。
- $\mathbb{R}^N=\{(x_1,\dots,x_N):x_i\in\mathbb{R}\}$，$\mathbb{C}^N=\{(z_1,\dots,z_N):z_i\in\mathbb{C}\}$。
- 【課本補充】$\{(z_1,z_2,z_1+z_2):z_1,z_2\in\mathbb{C}\}$ 也是（它是 $\mathbb{C}^3$ 的子空間）。

### 3.2 函數空間

[▶ 19:20](https://youtu.be/gQZxz7p8KTY?t=1160) 對應課本 Example 1.2.3。

講者用比課本稍微抽象的寫法：$S$ 是任意集合，$V$ 是 $\mathbb{F}$ 上的向量空間，令

$$E=\{f: S\to V\}\quad(\text{所有從 } S \text{ 到 } V \text{ 的函數}).$$

課本用 $X$ 代替 $S$、用 $E$ 代替 $V$，而且沒有給這個集合名字（後來用 $\mathcal{F}$）。

【課堂討論】[▶ 19:59](https://youtu.be/gQZxz7p8KTY?t=1199) 講者問：函數要怎麼加？學生答：「就照平常那樣。」也就是**逐點（pointwise）**定義：

$$(f+g)(s)=f(s)+g(s),\qquad (\lambda f)(s)=\lambda f(s),\qquad \text{對所有 } s\in S.$$

**為什麼這樣就是向量空間**：加法和純量乘法都發生在函數**取值的地方** $V$ 裡，而 $V$ 本來就是向量空間，所以 $V$ 的每條規則逐點搬過來就成立。

**零向量**：把每個 $s$ 都送到 $V$ 的零向量的常數函數。[▶ 21:05](https://youtu.be/gQZxz7p8KTY?t=1265)（學生答：「零是常數函數。」）

講者強調這個例子**非常一般**【口頭】：[▶ 32:24](https://youtu.be/gQZxz7p8KTY?t=1944)

- $S$ 可以是**任何集合**，$S$ 本身不需要有加法或任何線性結構。
- $V$ 可以換成任何向量空間，就得到矩陣值函數、向量值函數……不只複數值函數。

【課本補充】$\mathbb{R}^N$ 和 $\mathbb{C}^N$ 本身也是函數空間：$\mathbb{R}^N$ 就是所有 $\{1,\dots,N\}\to\mathbb{R}$ 的函數，第 $i$ 個座標 = 函數在 $i$ 的值。

### 3.3 子空間：C(Ω)、Cᵏ(Ω)、C^∞(Ω)、P(Ω)

[▶ 22:18](https://youtu.be/gQZxz7p8KTY?t=1338) 對應課本 Example 1.2.4，p. 4。

**子空間（subspace）**：$E_1\subseteq E$，而且對任意 $\alpha,\beta\in\mathbb{F}$、$x,y\in E_1$，$\alpha x+\beta y\in E_1$。子空間自己也是向量空間。

**開集（open set）**[▶ 23:30](https://youtu.be/gQZxz7p8KTY?t=1410)：$\Omega\subseteq\mathbb{R}^N$ 是開集，意思是 $\Omega$ 裡每一點都是**內點（interior point）**：每個 $x\in\Omega$ 都有一個以 $x$ 為中心、用歐氏距離量的小球 $\{y:|y-x|<\varepsilon\}$ 整個落在 $\Omega$ 裡。講者說：嚴格定義在課本 p. 14 附近（§1.3），p. 4 就先用了，先靠直覺。【口頭】

設 $\Omega$ 是 $\mathbb{R}^N$ 的開集。下面都是「所有 $\Omega\to\mathbb{C}$ 函數」這個空間的子空間：

| 記號 | 內容 |
|---|---|
| $C(\Omega)$ | 在 $\Omega$ 上連續的複值函數 |
| $C^k(\Omega)$ | 偏導數到 $k$ 階都存在而且連續 |
| $C^\infty(\Omega)$ | 所有階的偏導數都存在（而且連續）；講者叫它「光滑（smooth）」 |
| $P(\Omega)$ | $N$ 變數多項式（當成 $\Omega$ 上的函數） |

[▶ 26:30](https://youtu.be/gQZxz7p8KTY?t=1590) 關於 $C^k$：課本原文是「continuous partial derivatives of order $k$」。講者說這有好幾種講法，課本的是最不技術性的；也可以說「$k$ 次連續可微」。⚠️ 逐字稿缺字：講者接下來那句（「K derivatives not partial derivatives」）字幕不清楚。這裡照一般慣例：**所有** $\le k$ 階的偏導數都存在且連續。

**為什麼 $C^\infty$ 的導數自動連續？**【課堂討論】[▶ 29:20](https://youtu.be/gQZxz7p8KTY?t=1760) 學生說 $C^\infty$ 就是「光滑」、「Jacobian 很好」。講者解釋：如果每一階都能再微分，那第 $k$ 階導數可微，而**可微 ⟹ 連續**，所以每一階都連續。

> 以下**不是逐字稿內容**，是依多變數微積分推論的：這個論證在一變數時完全正確。多變數時要小心：**偏導數存在**不保證連續（例如 $f(x,y)=xy/(x^2+y^2)$，$f(0,0)=0$，兩個偏導數在原點都存在，但 $f$ 在原點不連續）。所以 $C^\infty(\Omega)$ 一般定義成 $\bigcap_k C^k(\Omega)$，也就是每一階偏導數都存在**而且連續**。

**怎麼證它們是子空間：子空間檢驗法**【課堂討論】[▶ 29:58](https://youtu.be/gQZxz7p8KTY?t=1798)

取 $f,g$ 在子空間裡、$c$ 是純量，檢查 $cf+g$ 還在裡面。例如 $C(\Omega)$：連續函數相加、乘常數還是連續（極限律）。$C^k$ 也一樣，因為微分是線性的：$\partial^\alpha(cf+g)=c\,\partial^\alpha f+\partial^\alpha g$，兩個連續函數的線性組合還是連續。

【Q&A】[▶ 31:13](https://youtu.be/gQZxz7p8KTY?t=1873) 學生問：連續函數乘上純量之後，它不是回不到 $\Omega$ 裡嗎？講者答：不需要回到 $\Omega$。要回到的是 $C(\Omega)$——乘完還是一個「定義在 $\Omega$ 上的連續函數」，所以還在 $C(\Omega)$ 裡。（$\Omega$ 是函數的**定義域**，$C(\Omega)$ 才是向量空間。）

**實的還是複的？**[▶ 31:48](https://youtu.be/gQZxz7p8KTY?t=1908) 課本的函數取值在 $\mathbb{C}$，講者說他傾向把這些當成實向量空間，但兩種看法都可以；也可以把 $\mathbb{C}$ 換成 $\mathbb{R}$。

【課本補充】包含關係：$P(\mathbb{R}^N)\subseteq C^\infty(\mathbb{R}^N)\subseteq C^k(\mathbb{R}^N)\subseteq C(\mathbb{R}^N)$，前者都是後者的子空間。**子空間的交集還是子空間，但聯集一般不是。**

### 3.4 可微但導數不連續的函數

【口頭】[▶ 27:04](https://youtu.be/gQZxz7p8KTY?t=1624)

為什麼 $C^1$ 要求導數**連續**，不只要求導數存在？因為有函數處處可微，但導數不連續。講者畫了一個被「包絡線」夾住、在 $0$ 附近震盪的 $\sin(1/x)$ 型函數：震盪被夾到 $0$，所以在 $0$ 可微；但導數在 $0$ 不連續。

以下**不是逐字稿內容**，是依講者的描述補上的標準例子：

$$f(x)=\begin{cases}x^2\sin(1/x), & x\ne0\\ 0, & x=0\end{cases}$$

- 在 $0$：$f'(0)=\lim_{h\to0}\dfrac{h^2\sin(1/h)}{h}=\lim_{h\to0}h\sin(1/h)=0$（因為 $|h\sin(1/h)|\le|h|$）。包絡線就是 $\pm x^2$。
- 在 $x\ne0$：$f'(x)=2x\sin(1/x)-\cos(1/x)$。$x\to0$ 時第一項 $\to0$，第二項 $\cos(1/x)$ 在 $-1$ 和 $1$ 之間一直跳，沒有極限。
- 所以 $f$ 處處可微，但 $f'$ 在 $0$ 不連續：$f\notin C^1$。

講者補充：也可以做出「$C^1$ 但不是 $C^2$」的例子，而且一維能做的，二維、三維都能做。

### 3.5 數列空間

[▶ 33:45](https://youtu.be/gQZxz7p8KTY?t=2025) 對應課本 Example 1.2.5，p. 4。

把函數空間的 $S$ 換成自然數 $\mathbb{N}$：函數 $x:\mathbb{N}\to\mathbb{C}$ 就是一個複數數列 $(x_1,x_2,\dots)$，$x_n=x(n)$。

加法和純量乘法是**逐項**的：

$$(x_1,x_2,\dots)+(y_1,y_2,\dots)=(x_1+y_1,x_2+y_2,\dots),\qquad \lambda(x_1,x_2,\dots)=(\lambda x_1,\lambda x_2,\dots).$$

講者強調【口頭】：這**就是**函數的逐點加法，只是記號不同。$(x+y)_n=x_n+y_n$ 寫成函數就是 $(x+y)(n)=x(n)+y(n)$。[▶ 35:31](https://youtu.be/gQZxz7p8KTY?t=2131)

講者說這是「課本的 Example 4」。⚠️ 我們手上第 3 版的編號是 Example 1.2.5（1.2.4 是上一節的 $C(\Omega)$），見待確認清單。

【課本補充】所有有界複數列是所有複數列的真子空間；所有收斂複數列又是有界複數列的真子空間。

課本記號：$(x_n)$ 是數列本身，$\{x_n:n\in\mathbb{N}\}$ 是它的**值的集合**。後者可以是有限集（例如 $(1,0,1,0,\dots)$ 的值集合是 $\{0,1\}$）。

### 3.6 ℓᵖ 空間

[▶ 37:15](https://youtu.be/gQZxz7p8KTY?t=2235) 對應課本 Example 1.2.6，pp. 4–5。

**定義**：$p\ge1$（$p\ge1$ 是課本寫的），

$$\ell^p=\left\{(z_n): z_n\in\mathbb{C},\ \sum_{n=1}^\infty|z_n|^p<\infty\right\}.$$

講者叫它們「$p$ 次可和（$p$-summable）數列」。

這裡的 $|z_n|$ 是複數的**模（modulus）**：$z_n=x_n+iy_n$ 時 $|z_n|=\sqrt{x_n^2+y_n^2}$。講者順口提到：共軛複數，數學課本寫 $\bar z$（bar），物理課本寫 $z^*$（star）。【口頭】[▶ 38:30](https://youtu.be/gQZxz7p8KTY?t=2310)

**為什麼 $\ell^p$ 是子空間？「一點都不明顯」。**[▶ 39:45](https://youtu.be/gQZxz7p8KTY?t=2385)

$\ell^p$ 是「所有複數列」的子集，所以用子空間檢驗法：要證 $(x_n),(y_n)\in\ell^p$、$c\in\mathbb{C}$ 時，$(cx_n)\in\ell^p$ 而且 $(x_n+y_n)\in\ell^p$。

**純量乘法**（容易）[▶ 44:19](https://youtu.be/gQZxz7p8KTY?t=2659)：

$$\sum_{n=1}^\infty|cx_n|^p=\sum_{n=1}^\infty|c|^p|x_n|^p=|c|^p\sum_{n=1}^\infty|x_n|^p<\infty.$$

第二個等號（常數提到級數外面）講者說「就用微積分 II，雖然當時沒證」。真正的理由【口頭】[▶ 43:46](https://youtu.be/gQZxz7p8KTY?t=2626)：級數 = 部分和的極限；$c$ 乘級數的部分和 = $c$ 乘原級數的部分和；原部分和收斂，所以 $c$ 倍也收斂。最後靠的是**數列極限的線性**。

**加法**（難）[▶ 45:28](https://youtu.be/gQZxz7p8KTY?t=2728)：靠 **Minkowski 不等式**

$$\left(\sum_{n=1}^\infty|x_n+y_n|^p\right)^{1/p}\le\left(\sum_{n=1}^\infty|x_n|^p\right)^{1/p}+\left(\sum_{n=1}^\infty|y_n|^p\right)^{1/p}.$$

右邊兩項都有限，所以左邊有限，$(x_n+y_n)\in\ell^p$。

所以 $\ell^p$ 是子空間。講者說它是「特別有趣的子空間」。課本在 pp. 5–7 用 Hölder 不等式證 Minkowski，講者這堂**跳過**[▶ 46:37](https://youtu.be/gQZxz7p8KTY?t=2797)，證明補在第 4 節。

**順帶一提：子空間 = 子群**【口頭】[▶ 40:18](https://youtu.be/gQZxz7p8KTY?t=2418)

學生提到線性代數課用「子群」的符號寫子空間。講者說這很合理：子空間一定是加法的子群。而且因為向量空間的加法是**交換群**，每個子群都是**正規子群（normal subgroup）**，所以線性代數裡**任何**子空間都能拿來做商空間（quotient space）；群論裡只有正規子群才能做商群。

---

## 4. Hölder 與 Minkowski 不等式

【課本補充】Theorem 1.2.7–1.2.8，pp. 5–7。講者跳過，但這是 ℓᵖ 是向量空間的關鍵，所以完整寫出來。

**共軛指數**：$p>1$，$q>1$，$\frac1p+\frac1q=1$。例如 $p=q=2$；$p=3$ 時 $q=3/2$。由 $\frac1p=1-\frac1q$ 兩邊乘 $q$ 得

$$\frac qp=q-1. \tag{★}$$

### 4.1 Young 不等式

**主張**：對所有 $a,b\ge0$，

$$ab\le\frac{a^p}{p}+\frac{b^q}{q}. \tag{1.1}$$

**Step 1：一個單變數不等式。** 對 $0\le x\le1$，$x^{1/p}\le\frac xp+\frac1q$。

令 $g(x)=\frac xp+\frac1q-x^{1/p}$。則 $g(1)=\frac1p+\frac1q-1=0$，而且對 $0<x<1$，

$$g'(x)=\frac1p-\frac1p x^{\frac1p-1}=\frac1p\left(1-x^{\frac1p-1}\right)\le0,$$

因為 $\frac1p-1<0$，所以 $x^{\frac1p-1}\ge1$。$g$ 在 $[0,1]$ 遞減，$g(x)\ge g(1)=0$。（這步課本只說「First observe that」，推導是補的。）

**Step 2：代入。** 先假設 $a^p\le b^q$ 且 $b>0$。令 $x=a^p/b^q\in[0,1]$，代入 Step 1：

$$\frac{a}{b^{q/p}}\le\frac1p\frac{a^p}{b^q}+\frac1q.$$

由 (★)，$-\frac qp=1-q$，所以左邊是 $ab^{1-q}$。兩邊乘 $b^q$：

$$ab\le\frac{a^p}{p}+\frac{b^q}{q}.$$

$b=0$ 時左邊是 $0$，顯然成立。$b^q\le a^p$ 的情形把 $a,b$ 和 $p,q$ 的角色對調，同樣論證。所以 (1.1) 對所有 $a,b\ge0$ 成立。

### 4.2 Hölder 不等式

**定理 1.2.7（Hölder）**：$p,q$ 共軛。若 $(x_n)\in\ell^p$、$(y_n)\in\ell^q$，則

$$\sum_{n=1}^\infty|x_ny_n|\le\left(\sum_{n=1}^\infty|x_n|^p\right)^{1/p}\left(\sum_{n=1}^\infty|y_n|^q\right)^{1/q}.$$

**證明**：如果 $(x_n)$ 或 $(y_n)$ 全是 $0$，兩邊都是 $0$。以下假設都不全為 $0$。

固定 $n$（取夠大，讓兩個有限和都 $>0$）。記

$$A_n=\left(\sum_{k=1}^n|x_k|^p\right)^{1/p},\qquad B_n=\left(\sum_{k=1}^n|y_k|^q\right)^{1/q}.$$

對每個 $1\le j\le n$，在 (1.1) 代入 $a=|x_j|/A_n$、$b=|y_j|/B_n$：

$$\frac{|x_j|\,|y_j|}{A_nB_n}\le\frac1p\frac{|x_j|^p}{A_n^p}+\frac1q\frac{|y_j|^q}{B_n^q}.$$

對 $j=1,\dots,n$ 加起來。右邊第一項加起來是 $\frac1p\cdot\frac{A_n^p}{A_n^p}=\frac1p$，第二項是 $\frac1q$：

$$\frac{\sum_{j=1}^n|x_j||y_j|}{A_nB_n}\le\frac1p+\frac1q=1.$$

所以 $\sum_{j=1}^n|x_jy_j|\le A_nB_n$。令 $n\to\infty$，$A_n,B_n$ 遞增收斂到右邊的兩個因子，得證。∎

**關鍵一步**：先**正規化**（除以範數），讓 Young 不等式右邊加起來恰好是 $\frac1p+\frac1q=1$。

### 4.3 Minkowski 不等式

**定理 1.2.8（Minkowski）**：$p\ge1$。若 $(x_n),(y_n)\in\ell^p$，則

$$\left(\sum_{n=1}^\infty|x_n+y_n|^p\right)^{1/p}\le\left(\sum_{n=1}^\infty|x_n|^p\right)^{1/p}+\left(\sum_{n=1}^\infty|y_n|^p\right)^{1/p}.$$

**證明**：$p=1$ 就是逐項用三角不等式 $|x_n+y_n|\le|x_n|+|y_n|$ 再加起來。

$p>1$：取 $q$ 使 $\frac1p+\frac1q=1$。下面先對**有限和**（$n=1$ 到 $N$）做，最後再令 $N\to\infty$。課本直接寫無窮和；用有限和是為了確保下面除的數有限。記 $S_N=\sum_{n=1}^N|x_n+y_n|^p$。

1. 拆一個因子出來，用三角不等式：
   $$S_N=\sum_{n=1}^N|x_n+y_n|\,|x_n+y_n|^{p-1}\le\sum_{n=1}^N|x_n|\,|x_n+y_n|^{p-1}+\sum_{n=1}^N|y_n|\,|x_n+y_n|^{p-1}.$$
2. 兩個和各用一次 Hölder（$|x_n|$ 用 $p$ 次方，$|x_n+y_n|^{p-1}$ 用 $q$ 次方）：
   $$\sum_{n=1}^N|x_n|\,|x_n+y_n|^{p-1}\le\left(\sum_{n=1}^N|x_n|^p\right)^{1/p}\left(\sum_{n=1}^N|x_n+y_n|^{q(p-1)}\right)^{1/q}.$$
   $|y_n|$ 那一項同理。
3. 由 (★)，$q(p-1)=qp-q=p$（因為 $qp=p+q$）。所以 $\sum|x_n+y_n|^{q(p-1)}=S_N$：
   $$S_N\le\left[\left(\sum_{n=1}^N|x_n|^p\right)^{1/p}+\left(\sum_{n=1}^N|y_n|^p\right)^{1/p}\right]S_N^{1/q}.$$
4. $S_N=0$ 時不用證。$S_N>0$ 時兩邊除以 $S_N^{1/q}$，左邊變成 $S_N^{1-1/q}=S_N^{1/p}$：
   $$S_N^{1/p}\le\left(\sum_{n=1}^N|x_n|^p\right)^{1/p}+\left(\sum_{n=1}^N|y_n|^p\right)^{1/p}\le\|x\|_p+\|y\|_p.$$
5. 右邊跟 $N$ 無關，令 $N\to\infty$ 得證。∎

**關鍵一步**：把 $|x+y|^p$ 拆成 $|x+y|\cdot|x+y|^{p-1}$，用 Hölder 後**同一個量 $S$ 出現在兩邊**，再除掉。

【課本補充】下一節（§1.3，Example 1.3.4）會說：Minkowski 不等式其實就是 ℓᵖ 範數 $\|z\|_p=\left(\sum|z_n|^p\right)^{1/p}$ 的**三角不等式**。

---

## 5. 直積

[▶ 47:48](https://youtu.be/gQZxz7p8KTY?t=2868) 對應課本 Example 1.2.9，p. 7。

**有限個**：$E_1,\dots,E_n$ 是同一個體上的向量空間，

$$E_1\times\cdots\times E_n=\{(x_1,\dots,x_n): x_i\in E_i\},$$

運算逐分量做。學生說「就是平常那樣」。

**任意多個**[▶ 48:22](https://youtu.be/gQZxz7p8KTY?t=2902)：課本更進一步，對任意**指標集（index set）** $J$，每個 $j\in J$ 給一個向量空間 $E_j$，定義

$$\prod_{j\in J}E_j=\left\{x: J\to\bigcup_{j\in J}E_j\ \middle|\ x(j)\in E_j\ \text{對所有 } j\in J\right\}.$$

運算照函數空間（§3.2）逐點定義。

> 課本原文寫「$x(j)\in X_j$」，前後文都是 $E_j$，應是筆誤。

**為什麼要用函數定義**【口頭】[▶ 51:28](https://youtu.be/gQZxz7p8KTY?t=3088)：$J=\{1,2,3,\dots\}$ 時還能寫成列表 $(x_1,x_2,\dots)$。但如果 $J=\mathbb{R}$，元素太多列不完，列表記號就失效了，只能寫成 $x=(x_\alpha)_{\alpha\in\mathbb{R}}$，$\alpha$ 是實數參數。「函數 $x:J\to\cdots$」這個定義不管 $J$ 多大都能用。

---

## 6. 線性獨立、span、基底、維度

[▶ 52:36](https://youtu.be/gQZxz7p8KTY?t=3156) 對應課本 pp. 7–8。

**線性組合**：$x=\alpha_1x_1+\cdots+\alpha_kx_k$。

**線性獨立（linearly independent）**：$S\subseteq E$ 線性獨立，意思是對**每個** $k$、**任意**相異的 $x_1,\dots,x_k\in S$，

$$c_1x_1+\cdots+c_kx_k=0\ \Longrightarrow\ c_1=c_2=\cdots=c_k=0.$$

講者強調「對所有 $k$」：$k=1,2,3,\dots$ 都要成立。[▶ 53:45](https://youtu.be/gQZxz7p8KTY?t=3225)課本的說法：無限集合線性獨立 = 它的**每個有限子集**都線性獨立。

> 「相異」是補上的：如果允許 $x_1=x_2$，則 $1\cdot x_1+(-1)\cdot x_2=0$，任何集合都不會線性獨立。課本說「有限子集」就隱含了相異。

**span**[▶ 54:28](https://youtu.be/gQZxz7p8KTY?t=3268)：

$$\operatorname{span}S=\left\{\sum_{i=1}^k c_ix_i\ :\ k\in\mathbb{N},\ x_i\in S,\ c_i\in\mathbb{F}\right\}.$$

**有限**線性組合的全體。強調純量的話寫 $\operatorname{span}_{\mathbb{F}}S$。【課本補充】$\operatorname{span}S$ 是包含 $S$ 的**最小**子空間。

**基底（basis）**[▶ 56:15](https://youtu.be/gQZxz7p8KTY?t=3375)：$\beta$ 線性獨立且 $\operatorname{span}\beta=E$。

**維度**[▶ 56:46](https://youtu.be/gQZxz7p8KTY?t=3406)：如果 $E$ 有有限基底，那**所有**基底的元素個數都一樣。這個數叫 $\dim E$。講者說：這是線性代數的大定理，可惜線代課常常沒證。不能一個空間既是 8 維又是 10 維。沒有有限基底的空間叫**無限維**。

### 有限 vs 無限的差別【口頭】

[▶ 58:25](https://youtu.be/gQZxz7p8KTY?t=3505)

- **$S$ 有限時**（例如 5 個元素），只要檢查這 5 個的線性組合就好，較少個數的情形自動成立。理由：如果其中 2 個有非平凡組合等於 $0$，把另外 3 個的係數補 $0$，就得到 5 個的非平凡組合等於 $0$，矛盾。
- **$S$ 無限時**，要檢查**任意有限**線性組合，所以定義裡要寫「對所有 $k$」。
- **重要**：在無限維空間裡，你可能以為線性獨立要用**級數**（無限和）來判斷。**不是**。線性獨立、span、基底講的永遠是**有限**線性組合。[▶ 58:59](https://youtu.be/gQZxz7p8KTY?t=3539)

### 無限維的「維度」【口頭】

[▶ 57:19](https://youtu.be/gQZxz7p8KTY?t=3439)

更一般地，任兩個基底的**基數（cardinality，集合大小）**相同。所以無限維空間也能定義維度，用基數代替數字。例如：有一個可數基底，就不會有另一個不可數基底。講者說這門課大概用不到，而且他說「我不太確定」。

> 以下**不是逐字稿內容**，是依線性代數的標準結果補充的：「任兩個基底基數相同」是對的，是標準定理（無限的情形要用選擇公理保證基底存在）。

### 課本的其他例子【課本補充】

- $\mathbb{R}^N$ 的 $e_1=(1,0,\dots,0),\dots,e_N=(0,\dots,0,1)$ 線性獨立；單項式 $1,x,x^2,\dots$ 線性獨立。
- **線性獨立跟體有關**：在 $\mathbb{C}$ 裡，$1$ 和 $i$ 在 $\mathbb{R}$ 上線性獨立（$a+bi=0$，$a,b$ 實數 ⟹ $a=b=0$），但在 $\mathbb{C}$ 上不獨立（$i\cdot1+(-1)\cdot i=0$）。
- 所以 $\mathbb{C}^N$ 當實向量空間是 $2N$ 維，當複向量空間是 $N$ 維。
- $\mathbb{R}^3$ 的三組基底：$\{(1,0,0),(0,1,0),(0,0,1)\}$、$\{(0,1,1),(1,0,1),(1,1,0)\}$、$\{(1,2,3),(1,3,5),(3,2,3)\}$。
- $C(\Omega)$、$C^k(\mathbb{R}^N)$、$C^\infty(\mathbb{R}^N)$ 都是無限維。

### 下一堂預告

[▶ part 2 00:02](https://youtu.be/h3qIa7X1btQ?t=2)：今天大致講完 §1.2。下一堂進 §1.3 賦範空間：介紹幾種範數，例如**一致收斂的範數**，也會講**逐點收斂 vs 一致收斂**，這是實分析課沒講完的部分。

---

## 7. 一頁速查表

### 向量空間

| 項目 | 內容 | 關鍵 |
|---|---|---|
| 定義 | $(E,+)$ 是交換群，加上 4 條純量乘法規則 | 課本用「$x+z=y$ 有解」代替零向量與負向量，兩者等價 |
| 零向量唯一 | $z_1=z_1+z_2=z_2$ | 兩個都當零向量用一次 |
| 子空間檢驗 | $x,y\in E_1$ ⟹ $\alpha x+\beta y\in E_1$ | 只要檢查封閉性 |
| 交集 / 聯集 | 子空間交集是子空間，聯集一般不是 | |

### 例子

| 空間 | 運算 | 為什麼是向量空間 |
|---|---|---|
| $\{f:S\to V\}$ | 逐點 $(f+g)(s)=f(s)+g(s)$ | 運算在 $V$ 裡做，$V$ 的規則逐點搬過來；$S$ 不需要結構 |
| $C(\Omega)$、$C^k(\Omega)$、$C^\infty(\Omega)$、$P(\Omega)$ | 逐點 | 連續、微分都是線性的 |
| 數列空間 | 逐項 | = 函數空間取 $S=\mathbb{N}$ |
| $\ell^p$（$p\ge1$） | 逐項 | 純量：$\sum|cx_n|^p=|c|^p\sum|x_n|^p$；加法：Minkowski |
| $\prod_{j\in J}E_j$ | 逐點 | 定義成函數 $x:J\to\bigcup E_j$，$x(j)\in E_j$ |

### 不等式（$\frac1p+\frac1q=1$）

| 名稱 | 式子 | 證明關鍵一步 |
|---|---|---|
| Young | $ab\le\frac{a^p}{p}+\frac{b^q}{q}$ | $x^{1/p}\le\frac xp+\frac1q$（$0\le x\le1$），代 $x=a^p/b^q$ |
| Hölder | $\sum|x_ny_n|\le\|x\|_p\|y\|_q$ | 正規化後套 Young，右邊加起來 $=\frac1p+\frac1q=1$ |
| Minkowski | $\|x+y\|_p\le\|x\|_p+\|y\|_p$ | $|x+y|^p=|x+y|\cdot|x+y|^{p-1}$，Hölder，用 $q(p-1)=p$，兩邊除以 $S^{1/q}$ |

### 線性代數

| 項目 | 內容 |
|---|---|
| 線性獨立 | 每個**有限**子集都獨立（相異元素、所有 $k$） |
| span | 所有**有限**線性組合；包含 $S$ 的最小子空間 |
| 基底 | 線性獨立 + span 是全空間 |
| 維度 | 有限基底時個數唯一；一般情形基數唯一 |
| 注意 | 無限維時線性獨立**不用**級數判斷 |
| 跟體有關 | $\dim_{\mathbb{R}}\mathbb{C}^N=2N$，$\dim_{\mathbb{C}}\mathbb{C}^N=N$ |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 函數空間、$C(\Omega)$ | 第 2 集起放上範數（一致收斂範數）；§1.3 |
| $\ell^p$、Minkowski 不等式 | 第 2 集：Minkowski = ℓᵖ 範數的三角不等式；第 6 集：完備性 |
| 開集的嚴格定義 | 第 2、4 集（§1.3 開球、開集、緊緻） |
| Cauchy 數列、完備、Banach 空間 | 第 6 集（Banach spaces and completions） |
| 壓縮映射、存在唯一性 | 第 8–9 集 |
| Lebesgue 積分 | 第 11–17 集（第 2 章） |
| 有限線性組合的基底 | 第 21–22 集：Hilbert 空間的「正交基底」允許無限和，跟這裡的基底不一樣 |
| 量子力學 | 第 33–34 集（第 7 章） |

---

## 附：本集一句話總結

> **向量空間就是「加法是交換群、純量乘法守規矩」；最重要的例子是函數空間——運算逐點做，定義域可以是任何集合。ℓᵖ 是子空間這件事不顯然，要靠 Minkowski 不等式（由 Young → Hölder → Minkowski 一路推出）。而無限維空間的線性獨立和基底，講的仍然只是有限線性組合。**

---

## ⚠️ 待確認清單

1. 講者姓名：依頻道、開場禱告的風格推斷為 James Cook（Liberty University），本集沒有自我介紹，待確認。
2. [▶ 00:36](https://youtu.be/gQZxz7p8KTY?t=36) 講者用的課本版本：他說的書名是「Introduction to Hilbert Spaces with Applications」，我們的 PDF 是第 3 版《Hilbert Spaces with Applications》。p. 4、pp. 6–7、Example 1.2.6、p. 14 都對得上，但他說數列空間是「Example 4」（[▶ 32:55](https://youtu.be/gQZxz7p8KTY?t=1975)），第 3 版是 Example 1.2.5。可能是口誤，也可能版本不同。

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」Lecture 1（2023-01-16）錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 0:46）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.1–1.2 整理。*
