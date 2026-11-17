---
course: Number Theory（2021 秋，線上錄影）
episode: 3
lecture: Lecture 3
date: 待補（2021 秋）
video: https://youtu.be/Wl3coW1Sl8Y
notes: 講者照 Rotman《Journey into Mathematics》pp. 22–30；Jones & Jones 沒有二項式定理專節，§2.1 Example 2.2（書頁 21–22，PDF 頁 36–37）用到 $p\mid\binom{p}{i}$
---

# 第 3 集 · Lecture 3：二項式定理（Binomial Theorem） [▶ 影片](https://youtu.be/Wl3coW1Sl8Y)

← 上一集：[02-induction](02-induction.md) ｜ [總目錄](README.md) ｜ 下一集：[04-divisibility-euclidean-algorithm](04-divisibility-euclidean-algorithm.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 3 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（37:00，自動字幕）＋ Jones & Jones §2.1 Example 2.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Pascal 三角形](#1-pascal-三角形)
- [2. 二項式係數的定義與 Pascal 規則](#2-二項式係數的定義與-pascal-規則)
- [3. 階乘公式（Pascal）](#3-階乘公式pascal)
- [4. 二項式定理](#4-二項式定理)
- [5. 兩個求係數的例子](#5-兩個求係數的例子)
- [6. 為什麼叫「n 選 r」：計數](#6-為什麼叫n-選-r計數)
- [7. 二項式級數](#7-二項式級數)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說本集取材自 Rotman《Journey into Mathematics: An Introduction to Proofs》pp. 22–30 [▶ 00:00](https://youtu.be/Wl3coW1Sl8Y?t=0)。Jones & Jones 沒有二項式定理的專節，但之後會用到（見 §2 的課本補充）。

| 段落 | 內容 |
|---|---|
| 1–2 | Pascal 三角形；$\binom{n+1}{r}=\binom{n}{r-1}+\binom nr$ |
| 3 | $\binom nr = \frac{n!}{r!(n-r)!}$（歸納法證） |
| 4–5 | 二項式定理與求係數 |
| 6 | 組合意義（$r$ 元子集合） |
| 7 | 微積分的二項式級數、近似 $\sqrt{1.5}$ |

---

## 1. Pascal 三角形

[▶ 00:00](https://youtu.be/Wl3coW1Sl8Y?t=0)

展開 $(1+x)^n$：

| $n$ | $(1+x)^n$ | 係數 |
|---|---|---|
| 0 | $1$ | 1 |
| 1 | $1+x$ | 1 1 |
| 2 | $1+2x+x^2$ | 1 2 1 |
| 3 | $1+3x+3x^2+x^3$ | 1 3 3 1 |
| 4 | $1+4x+6x^2+4x^3+x^4$ | 1 4 6 4 1 |
| 5 | $1+5x+10x^2+10x^3+5x^4+x^5$ | 1 5 10 10 5 1 |

規律：**中間每個數 = 它上面兩個數的和**。例如 $1+2=3$、$1+3=4$、$4+6=10$。這叫 **Pascal 三角形**（Pascal's triangle）。

【口頭】它其實比 Pascal 早。Rotman 書裡有一張 1303 年的中國圖，就是這個三角形。講者順便指出中文數字很好認：一、二、三，「三加一」是四，「三加三」是六 [▶ 01:06](https://youtu.be/Wl3coW1Sl8Y?t=66)。講者猜別的古文明大概也發現過，因為它和計數問題有關。

---

## 2. 二項式係數的定義與 Pascal 規則

[▶ 02:46](https://youtu.be/Wl3coW1Sl8Y?t=166)

**定義**（Rotman 的作法）：寫
$$(1+x)^n = c_0 + c_1x + \cdots + c_nx^n,$$
定義**二項式係數**（binomial coefficient）$\binom nr$（讀作「$n$ 選 $r$」，*n choose r*）為 $x^r$ 的係數 $c_r$。

**例**：$(1+x)^5$ 裡 $x^4$ 的係數是 5，所以 $\binom54=5$；$x^1$ 的係數也是 5，所以 $\binom51=5$ [▶ 03:19](https://youtu.be/Wl3coW1Sl8Y?t=199)。

**定理 1（Pascal 規則）** [▶ 04:25](https://youtu.be/Wl3coW1Sl8Y?t=265)：
$$\binom{n+1}{r} = \binom{n}{r-1} + \binom{n}{r}.$$

**證明**：依定義，只要證「$(1+x)^{n+1}$ 裡 $x^r$ 的係數是 $c_{r-1}+c_r$」。
$$(1+x)^{n+1} = (1+x)(c_0+c_1x+\cdots+c_nx^n)$$
$$= c_0 + (c_1+c_0)x + (c_2+c_1)x^2 + \cdots + (c_r+c_{r-1})x^r + \cdots + c_nx^{n+1}.$$
$x^r$ 的係數來自兩處：$1\cdot c_rx^r$ 和 $x\cdot c_{r-1}x^{r-1}$。所以係數是 $c_r+c_{r-1}$。∎

（以下**不是逐字稿內容**，是依定義補的：在邊界 $r=0$ 或 $r=n+1$ 時，約定 $c_{-1}=c_{n+1}=0$，即 $\binom{n}{-1}=\binom{n}{n+1}=0$，公式照樣成立。）

**圖上看** [▶ 05:30](https://youtu.be/Wl3coW1Sl8Y?t=330)：$\binom40+\binom41 = 1+4 = 5 = \binom51$；$\binom41+\binom42 = 4+6 = 10 = \binom52$；依此類推。

> 【課本補充】Jones & Jones §2.1 Example 2.2（p. 21–22）用到二項式係數的一個數論性質：若 $p$ 是質數，則
> $$p \ \Big|\ \binom pi = \frac{p!}{i!\,(p-i)!}\qquad (i=1,\dots,p-1).$$
> 原因：分子有因數 $p$，分母 $i!(p-i)!$ 的每個因數都小於 $p$，不含 $p$。課本用它證明分圓多項式 $\Phi_p(x)=1+x+\cdots+x^{p-1}$ 不可約（之後的集數才會用到這類論證）。

---

## 3. 階乘公式（Pascal）

[▶ 06:38](https://youtu.be/Wl3coW1Sl8Y?t=398)

【口頭】講者自己習慣直接**用公式定義** $\binom nr$。這公式歸功於 Pascal（1623–1662，只活到 39 歲）。

**階乘**（factorial）遞迴定義 [▶ 07:12](https://youtu.be/Wl3coW1Sl8Y?t=432)：
$$0! = 1,\qquad (n+1)! = (n+1)\cdot n!.$$
$1!=1$，$2!=2$，$3!=6$，$4!=24$，$5!=120$，$6!=720$，$7!=5040$。長得很快。

**定理 2（Pascal）**：對 $n\ge0$、$0\le r\le n$，
$$\binom nr = \frac{n!}{r!\,(n-r)!}.$$

**證明**（對 $n$ 歸納，從 $n=0$ 開始）[▶ 08:54](https://youtu.be/Wl3coW1Sl8Y?t=534)
- **基底**：$n=0$：$\tfrac{0!}{0!\,0!}=1$，而 $(1+x)^0=1$ 的 $x^0$ 係數是 $1$。✓
- **歸納步驟**：設公式對 $n$ 成立。由定理 1 和歸納假設，
$$\binom{n+1}{r} = \binom{n}{r-1}+\binom nr = \frac{n!}{(r-1)!\,(n-r+1)!} + \frac{n!}{r!\,(n-r)!}.$$
（第一項：$n-(r-1) = n-r+1$。）

用階乘定義拆開：$(n-r+1)! = (n-r+1)\,(n-r)!$，$r! = r\,(r-1)!$。提出公因式 $\dfrac{n!}{(r-1)!\,(n-r)!}$：
$$= \frac{n!}{(r-1)!\,(n-r)!}\left[\frac{1}{n-r+1}+\frac1r\right] = \frac{n!}{(r-1)!\,(n-r)!}\cdot\frac{r+(n-r+1)}{r\,(n-r+1)}.$$
分子 $r+n-r+1 = n+1$。再把 $r$ 和 $(r-1)!$ 合成 $r!$、把 $(n-r+1)$ 和 $(n-r)!$ 合成 $(n-r+1)!$、把 $(n+1)$ 和 $n!$ 合成 $(n+1)!$：
$$= \frac{(n+1)!}{r!\,(n+1-r)!}.$$
這正是 $n+1$ 時的公式。∎

【口頭】本集暗號是「pirate」[▶ 11:40](https://youtu.be/Wl3coW1Sl8Y?t=700)。

---

## 4. 二項式定理

[▶ 12:11](https://youtu.be/Wl3coW1Sl8Y?t=731)

**系 1**：
$$(1+x)^n = \sum_{r=0}^{n}\binom nr x^r = \sum_{r=0}^n \frac{n!}{r!\,(n-r)!}x^r.$$
（只是把定義和定理 2 合起來，不用再證。）

**系 2（二項式定理，binomial theorem）**：對所有數 $a,b$ 和 $n\ge0$，
$$(a+b)^n = \sum_{r=0}^{n}\binom nr a^{n-r}b^r = \sum_{i+j=n}\binom{n}{j}a^ib^j.$$
每一項的次數和都是 $(n-r)+r=n$。

⚠️ 講者在 [▶ 12:44](https://youtu.be/Wl3coW1Sl8Y?t=764) 一度寫錯下標，自己改正：第二種寫法裡二項式係數的下標要配 $b$ 的次方 $j$（寫 $\binom ni$ 也對，因為 $\binom ni=\binom nj$，但講者改成 $j$ 比較保險）。

**證明** [▶ 13:50](https://youtu.be/Wl3coW1Sl8Y?t=830)
- 約定 $0^0=1$。若 $a=0$，兩邊都是 $b^n$。✓
- 設 $a\neq0$，令 $x=b/a$。由系 1：
$$\left(1+\frac ba\right)^n = \sum_{r=0}^n\binom nr\left(\frac ba\right)^r.$$
- 左邊 $= \left(\dfrac{a+b}{a}\right)^n = \dfrac{(a+b)^n}{a^n}$。
- 兩邊乘 $a^n$，把 $a^n$ 乘進有限和裡，用 $\dfrac{a^n}{a^r}=a^{n-r}$：
$$(a+b)^n = \sum_{r=0}^n\binom nr a^{n-r}b^r.\ ∎$$

【口頭】講者第一次看到這個是在 NC State 的證明導論課，老師也講了**多項式定理**（multinomial theorem，展開 $(a+b+c)^n$）和多項式係數，對應高維的「Pascal 金字塔」。本課不講，有興趣可以查（他說 Wikipedia 的數學條目通常不錯）[▶ 14:55](https://youtu.be/Wl3coW1Sl8Y?t=895)。

---

## 5. 兩個求係數的例子

【口頭】講者說作業有類似題目，所以示範兩題 [▶ 16:02](https://youtu.be/Wl3coW1Sl8Y?t=962)。

**例 1**：求 $(3x-y)^5$ 展開式中 $x^3y^2$ 的係數。

取 $a=3x$、$b=-y$、$n=5$：
$$(3x-y)^5 = \sum_{r=0}^5\binom5r(3x)^{5-r}(-y)^r = \sum_{r=0}^5\binom5r 3^{5-r}(-1)^r\,x^{5-r}y^r.$$
要 $x^3y^2$ → $r=2$。係數：
$$\binom52\cdot3^3\cdot(-1)^2 = 10\cdot27\cdot1 = 270.$$

**例 2**：求 $(3+2x)^{90}$ 展開式中 $x^{71}$ 的係數 [▶ 17:42](https://youtu.be/Wl3coW1Sl8Y?t=1062)。

取 $a=3$、$b=2x$、$n=90$：
$$(3+2x)^{90} = \sum_{r=0}^{90}\binom{90}{r}3^{90-r}(2x)^r = \sum_{r=0}^{90}\binom{90}{r}3^{90-r}2^r\,x^r.$$
取 $r=71$：
$$\binom{90}{71}\,3^{19}\,2^{71} = \frac{90!}{71!\,19!}\,3^{19}\,2^{71}.$$
【口頭】$\dfrac{90!}{71!} = 90\cdot89\cdots72$，分母還有 $19!$；講者試著約分，看不出漂亮的規律，就停在這個式子 [▶ 19:21](https://youtu.be/Wl3coW1Sl8Y?t=1161)。

【口頭】關於 Wolfram Alpha [▶ 20:32](https://youtu.be/Wl3coW1Sl8Y?t=1232)：
- 檢查大數字很好用，也可以列出例如「小於 200 的質數」。
- 但作業要用**理論**解。用暴力算出來的答案幾乎一定不是題目要的。可以用它處理無聊的計算部分。不確定就寄信問。

---

## 6. 為什麼叫「n 選 r」：計數

[▶ 21:07](https://youtu.be/Wl3coW1Sl8Y?t=1267)

【口頭】這個記號從 Euler 開始；Euler 原本在 $n$ 和 $r$ 中間有一條像分數線的東西，依 Rotman 的說法大約 50 年後才拿掉。

**組合意義**：若集合 $X$ 有 $n$ 個元素，「$r$ 元子集合」（$r$-subset）指有 $r$ 個元素的子集合。則
$$\binom nr = X \text{ 的 } r \text{ 元子集合個數}.$$

**單字的例子**：用 $n$ 個字母、不重複、**有順序**地排出 $r$ 個字母，叫一個「$r$ 字母單字」（不管字典裡有沒有）。個數是
$$\binom nr\cdot r!$$
（先選哪 $r$ 個字母，再排順序。）

⚠️ 講者一開始讀錯 Rotman 的書，說單字數是 $\binom nr$，後來在 [▶ 24:02](https://youtu.be/Wl3coW1Sl8Y?t=1442) 自己更正為 $\binom nr\cdot r!$。

**例**：字母表 $\{a,b,c,d\}$（$n=4$），3 字母單字有 $\binom43\cdot3! = 4\cdot6 = 24$ 個。
- 先選字母：$\{a,b,c\}$、$\{a,b,d\}$、$\{a,c,d\}$、$\{b,c,d\}$，共 $\binom43=4$ 種。
- 每種有 $3!=6$ 種排法，例如 $abc, acb, bac, bca, cab, cba$。

**用 $(1+x)^6$ 的係數** $1, 6, 15, 20, 15, 6, 1$ [▶ 27:22](https://youtu.be/Wl3coW1Sl8Y?t=1642)：
- 從 6 元素集合選 5 個：$\binom65=6$ 種。
- 從 6 個字母排 4 字母單字：$\binom64\cdot4! = 15\cdot24 = 360$ 個。
- 從 6 頂不同的帽子選 3 頂：$\binom63=20$ 種（3 字母單字共 $20\cdot3!=120$ 個，每 6 個對應同一組帽子）。

【口頭】「還好這不是組合學的課，我組合學常常出錯。」[▶ 29:41](https://youtu.be/Wl3coW1Sl8Y?t=1781)

---

## 7. 二項式級數

[▶ 30:16](https://youtu.be/Wl3coW1Sl8Y?t=1816)

**推導**：令 $f(x)=(1+x)^r$，$r$ 是任意實數。$f^{(n)}(x) = r(r-1)\cdots(r-n+1)(1+x)^{r-n}$，所以 $f^{(n)}(0) = r(r-1)\cdots(r-n+1)$。Maclaurin 級數（在 0 展開的 Taylor 級數）：
$$(1+x)^r = 1 + rx + \frac{r(r-1)}{2!}x^2 + \frac{r(r-1)(r-2)}{3!}x^3 + \cdots + \frac{r(r-1)\cdots(r-n+1)}{n!}x^n + \cdots$$

**和二項式定理的關係** [▶ 31:22](https://youtu.be/Wl3coW1Sl8Y?t=1882)：若 $r$ 是非負整數，$x^n$ 的係數上下同乘 $(r-n)(r-n-1)\cdots2\cdot1 = (r-n)!$：
$$\frac{r(r-1)\cdots(r-n+1)}{n!} = \frac{r!}{n!\,(r-n)!} = \binom rn.$$
- $r$ 是任意實數（$\tfrac12$、$\tfrac13$……）時，這是**無窮級數**。
- $r$ 是非負整數時，$(1+x)^r$ 是 $r$ 次多項式，微分 $r+1$ 次就是 0，所以級數在第 $r$ 項之後全為 0，**截斷成二項式定理**。所以二項式定理也可以用微積分推出來。

【口頭】二項式級數在微積分二常被忽略，但對 Newton 等微積分創始人很重要，因為它可以有效率地近似平方根、立方根 [▶ 32:30](https://youtu.be/Wl3coW1Sl8Y?t=1950)。

**收斂** [▶ 33:01](https://youtu.be/Wl3coW1Sl8Y?t=1981)：用比值檢驗（ratio test），係數比的極限是 1，所以級數在 $|x|<1$ 收斂；端點要看 $r$，講者不細講。

【口頭】注意：這只證了級數**收斂**，沒證它**等於** $(1+x)^r$。要證相等得證餘項趨近 0，微積分二幾乎不做。有些函數的 Taylor 級數收斂卻不等於原函數，留給分析課 [▶ 33:34](https://youtu.be/Wl3coW1Sl8Y?t=2014)。

**例 1**：$r=-1$ [▶ 34:08](https://youtu.be/Wl3coW1Sl8Y?t=2048)
$$(1+x)^{-1} = 1 + (-1)x + \frac{(-1)(-2)}{2!}x^2 + \frac{(-1)(-2)(-3)}{3!}x^3+\cdots = 1-x+x^2-x^3+\cdots$$
這就是首項 $1$、公比 $-x$ 的等比級數。

**例 2**：$r=\tfrac12$ [▶ 34:39](https://youtu.be/Wl3coW1Sl8Y?t=2079)
$$\sqrt{1+x} = 1 + \frac12x - \frac18x^2 + \frac1{16}x^3 - \cdots$$

**近似 $\sqrt{1.5}$**（$x=\tfrac12$）[▶ 35:11](https://youtu.be/Wl3coW1Sl8Y?t=2111)：
- 這是交錯級數（正負交替）。**交錯級數估計定理**：截斷後的誤差不超過下一項的絕對值。
- 取到 $x^2$ 項：$1 + \tfrac14 - \tfrac1{32} = 1.21875$。
- 下一項 $\tfrac1{16}\cdot\tfrac18 = 0.0078125\approx0.008$。
- 計算機：$\sqrt{1.5} = 1.224744871\ldots$，差 $\approx0.006$，確實小於 $0.0078$。

（以下**不是逐字稿內容**，是依數字推論的：字幕沒說 $x$ 是多少，但 $1.21875 = 1+\tfrac14-\tfrac1{32}$ 和 $1.2247\ldots=\sqrt{1.5}$ 都對應 $x=\tfrac12$。）

【口頭】級數是理解數論細緻問題的工具之一，主要用在解析數論，但本課偶爾也會用到 [▶ 36:16](https://youtu.be/Wl3coW1Sl8Y?t=2176)。

---

## 8. 一頁速查表

**定義與公式**
- $\binom nr$ = $(1+x)^n$ 中 $x^r$ 的係數 = $\dfrac{n!}{r!\,(n-r)!}$ = $n$ 元集合的 $r$ 元子集合數。
- $0!=1$，$(n+1)!=(n+1)\,n!$。

**Pascal 規則**：$\binom{n+1}{r} = \binom n{r-1}+\binom nr$。
關鍵一步：$(1+x)(c_0+\cdots+c_nx^n)$ 裡 $x^r$ 的係數 $= c_r + c_{r-1}$。

**階乘公式**（歸納）。關鍵一步：
$$\frac{n!}{(r-1)!(n-r)!}\left[\frac1{n-r+1}+\frac1r\right] = \frac{n!}{(r-1)!(n-r)!}\cdot\frac{n+1}{r(n-r+1)} = \frac{(n+1)!}{r!(n+1-r)!}.$$

**二項式定理**：$(a+b)^n = \displaystyle\sum_{r=0}^n\binom nr a^{n-r}b^r$。
關鍵一步：令 $x=b/a$ 代入 $(1+x)^n$ 的展開，兩邊乘 $a^n$。

**求係數**：寫出一般項 $\binom nr a^{n-r}b^r$，把常數和變數分開，解出 $r$。
- $(3x-y)^5$ 的 $x^3y^2$：$\binom52 3^3(-1)^2=270$。
- $(3+2x)^{90}$ 的 $x^{71}$：$\binom{90}{71}3^{19}2^{71}$。

**計數**：$n$ 個字母、不重複的 $r$ 字母有序單字數 $= \binom nr\, r!$。

**二項式級數**：$(1+x)^r = \displaystyle\sum_{n\ge0}\frac{r(r-1)\cdots(r-n+1)}{n!}x^n$，$|x|<1$。
- $r\in\mathbb{N}_0$ 時截斷成二項式定理。
- $\sqrt{1+x}=1+\tfrac x2-\tfrac{x^2}8+\tfrac{x^3}{16}-\cdots$；交錯級數誤差 ≤ 下一項。

**【課本】** $p$ 質數 ⇒ $p\mid\binom pi$，$1\le i\le p-1$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 二項式定理、$p\mid\binom pi$ | 第 7 集（Eisenstein 判別法證 $\Phi_p$ 不可約）；第 13 集的 Fermat 小定理講者用的是重排法和群論，沒有用二項式展開 |
| 二項式展開 | 第 20 集（三次方程的解） |
| 級數、交錯級數 | 解析數論方向（本課少用） |

---

## 附：本集一句話總結

> **$(1+x)^n$ 的係數排成 Pascal 三角形，滿足 $\binom{n+1}r=\binom n{r-1}+\binom nr$，並等於 $\frac{n!}{r!(n-r)!}$（歸納法證）；令 $x=b/a$ 就得到二項式定理，而它也是微積分二項式級數在指數為非負整數時「截斷」的特例。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 3 錄影逐字稿（YouTube 自動字幕，37:00）與 Jones & Jones《Elementary Number Theory》§2.1 整理；講者課堂內容取材自 Rotman《Journey into Mathematics》pp. 22–30。*
