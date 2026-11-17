---
course: Number Theory（2021 秋，線上錄影）
episode: 13
lecture: Lecture 13
date: 待補（2021 秋）
video: https://youtu.be/TyTUi2pe2sA
notes: Jones & Jones §3.1 Theorem 3.4（書頁 44，PDF 頁 59）；§4.1（書頁 65–71，PDF 頁 80–86）：Theorem 4.1、Corollary 4.2、Theorem 4.3、Corollary 4.4–4.5、Example 4.2–4.3、Theorem 4.6
---

# 第 13 集 · Lecture 13：Fermat 小定理與多項式同餘 [▶ 影片](https://youtu.be/TyTUi2pe2sA)

← 上一集：[12-chinese-remainder-theorem](12-chinese-remainder-theorem.md) ｜ [總目錄](README.md) ｜ 下一集：[14-group-of-units-euler-function](14-group-of-units-euler-function.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 13 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（46:41，自動字幕）＋ Jones & Jones §3.1、§4.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 模 n 同餘 ⇔ 模每個質數冪同餘](#1-模-n-同餘--模每個質數冪同餘)
- [2. 多項式同餘的怪現象](#2-多項式同餘的怪現象)
- [3. Lagrange 定理](#3-lagrange-定理)
- [4. Fermat 小定理](#4-fermat-小定理)
- [5. Wilson 定理](#5-wilson-定理)
- [6. 計算例子](#6-計算例子)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說證明照 Jones & Jones pp. 66–67 [▶ 08:53](https://youtu.be/TyTUi2pe2sA?t=533)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | $a\equiv b\ (\mathrm{mod}\ n)\iff$ 模每個 $p_i^{e_i}$ 同餘 | Theorem 3.4 |
| 2–3 | 多項式同餘；Lagrange 定理（模質數最多 $d$ 個根） | Theorem 4.1、Corollary 4.2 |
| 4 | Fermat 小定理（兩個證法）；$a^p\equiv a$ | Theorem 4.3、Corollary 4.4 |
| 5 | Wilson 定理 | Corollary 4.5 |
| 6 | 用 Fermat 小定理化簡大次方、高次多項式 | Example 4.2–4.3 |

---

## 1. 模 n 同餘 ⇔ 模每個質數冪同餘

[▶ 00:00](https://youtu.be/TyTUi2pe2sA?t=0)

【口頭】這件事之前「從縫隙漏掉了」，至少講得不夠。

**定理**：$n = p_1^{e_1}\cdots p_k^{e_k}$（質因數分解）。對整數 $a,b$：
$$a\equiv b\ (\mathrm{mod}\ n) \iff a\equiv b\ (\mathrm{mod}\ p_i^{e_i}) \text{ 對每個 } i.$$

**證明概要**：用**中國剩餘定理**（上一集）：$p_i^{e_i}$ 兩兩互質，同時滿足所有模 $p_i^{e_i}$ 的同餘，等於模它們的乘積 $n$ 同餘。

> 【課本補充】Theorem 3.4（p. 44）說這也可以直接證（用 Corollary 1.11：兩兩互質的數都整除 $a-b$，則乘積整除 $a-b$）。

**例** [▶ 01:06](https://youtu.be/TyTUi2pe2sA?t=66)：
- $50 = 2\cdot5^2$：$a\equiv b\ (\mathrm{mod}\ 50)\iff a\equiv b\ (\mathrm{mod}\ 2)$ 且 $(\mathrm{mod}\ 25)$。
- $588 = 4\cdot3\cdot49 = 2^2\cdot3\cdot7^2$：檢查 mod 4、mod 3、mod 49。

---

## 2. 多項式同餘的怪現象

[▶ 02:13](https://youtu.be/TyTUi2pe2sA?t=133)

**兩種看法** [▶ 02:46](https://youtu.be/TyTUi2pe2sA?t=166)：「$x^2-1\equiv0\ (\mathrm{mod}\ 8)$」和「$x^2-1 = 0$ 在 $\mathbb{Z}_8$」是同一個問題。

【口頭】講者說從這集之後他大概會停止畫橫線。

**怪現象 1：二次式有四個根**

在 $\mathbb{Z}_8$，代 $0,\dots,7$：$x = 1,3,5,7$ 都使 $x^2-1 = 0$（奇數平方 $\equiv1\ (\mathrm{mod}\ 8)$），偶數都不是。二次方程有**四個**解！

**怪現象 2：分解不唯一** [▶ 04:27](https://youtu.be/TyTUi2pe2sA?t=267)
$$x^2-1 = (x-1)(x+1) = (x-3)(x-5)\quad\text{在 }\mathbb{Z}_8.$$
（$(x-3)(x-5) = x^2-8x+15$，而 $8\equiv0$、$15\equiv-1$。）所以 $\mathbb{Z}_8$ 上的多項式沒有唯一分解。

**怪現象 3：$d$ 次式有 $n$ 個根** [▶ 05:34](https://youtu.be/TyTUi2pe2sA?t=334)：
$$nx^d + n(n-1)x^2 + n\equiv0\ (\mathrm{mod}\ n)$$
左邊不管 $x$ 是什麼都 $\equiv0$，所以 $n$ 個同餘類全是解。

**怪現象 4：看起來不重根，其實是重根** [▶ 06:07](https://youtu.be/TyTUi2pe2sA?t=367)：$x^2+1$ 在 $\mathbb{Z}_2$：$0$ 不是根、$1$ 是根。因為 $2\equiv0$，$x^2+1 = x^2-2x+1 = (x-1)^2$。

---

## 3. Lagrange 定理

### 3.1 敘述

[▶ 07:11](https://youtu.be/TyTUi2pe2sA?t=431)

前面的麻煩來自：模數不是質數（8），或係數全被模數整除。避開這兩點，事情就和熟悉的情況一樣：

**定理（Lagrange，多項式同餘）**：$p$ 是質數，$f(x) = a_dx^d+\cdots+a_1x+a_0$ 是整係數多項式，且**不是**所有 $a_i\equiv0\ (\mathrm{mod}\ p)$。則
$$f(x)\equiv0\ (\mathrm{mod}\ p)$$
最多有 $d$ 個同餘類解。

【口頭】嚴格說，只有 $a_d\not\equiv0$ 時才叫它「$d$ 次」同餘 [▶ 07:43](https://youtu.be/TyTUi2pe2sA?t=463)。（講者這時停下來拿口香糖。）

### 3.2 證明（對 $d$ 歸納）

[▶ 08:53](https://youtu.be/TyTUi2pe2sA?t=533)

- **基底** $d=0$：$f = a_0$，$a_0\not\equiv0$，沒有解（$\le0$ 個）。✓
- **歸納步驟**：設所有係數不全為 0（mod $p$）、次數 $\le d-1$ 的多項式最多有 $d-1$ 個根。
  - 若 $f(x)\equiv0$ 沒有解，完成。
  - 否則設 $f(a)\equiv0$，即 $p\mid f(a)$。計算
$$f(x)-f(a) = \sum_{i=0}^d a_i(x^i-a^i) = \sum_{i=1}^d a_i(x^i-a^i)$$
（$i=0$ 那項是 $1-1=0$）。
  - 對 $i\ge1$，**因式分解恆等式**：
$$x^i-a^i = (x-a)(x^{i-1}+ax^{i-2}+\cdots+a^{i-2}x+a^{i-1}).$$
（乘開後中間項兩兩相消，只剩 $x^i$ 和 $-a^i$。）
  - 每項提出 $x-a$：
$$f(x) = f(a) + (x-a)\,g(x),\qquad \deg g\le d-1.$$
  - $p$ 不整除 $g$ 的所有係數：否則 $p$ 也整除 $f(a)$ 和 $(x-a)g(x)$ 的所有係數，就整除 $f$ 的所有係數，矛盾。由歸納假設，$g(x)\equiv0$ 最多 $d-1$ 個根。
  - 若 $f(b)\equiv0$，則 $p\mid f(b)-f(a) = (b-a)g(b)$。$p$ 是質數，所以 $p\mid b-a$ 或 $p\mid g(b)$：要嘛 $b\equiv a$，要嘛 $b$ 是 $g$ 的根。總共最多 $1+(d-1) = d$ 個。∎

【口頭】講者說係數用 $a_i$、根也用 $a$，「如果重來我會換字母」[▶ 10:31](https://youtu.be/TyTUi2pe2sA?t=631)。

> 【課本補充】Theorem 4.1 的註解（p. 66）：
> - $f$ 可能比 $d$ 個根少：$x^2+1$ 在 $\mathbb{Z}_2$ 只有一個根、在 $\mathbb{Z}_3$ 沒有根。
> - 質數不可少：$x^2-1$ 在 $\mathbb{Z}_8$ 有四個根 $[1],[3],[5],[7]$；對合數 $n$，根的個數可以任意多。
> - 關鍵用到 $p$ 質數的地方：$p\mid(b-a)g(b)\Rightarrow p\mid b-a$ 或 $p\mid g(b)$（Lemma 2.1）。

### 3.3 推論

[▶ 13:45](https://youtu.be/TyTUi2pe2sA?t=825)

**推論**：$p$ 質數，若 $f(x) = a_dx^d+\cdots+a_0$ 在 $\mathbb{Z}_p$ 有**超過 $d$ 個**根，則 $p$ 整除每個係數 $a_i$。（就是 Lagrange 定理的逆否。）

**例** [▶ 14:20](https://youtu.be/TyTUi2pe2sA?t=860)：
- $13x\equiv0\ (\mathrm{mod}\ 13)$ 有 13 個解（一次式卻有 13 個根）。
- $20x^3+40x^2+20\equiv0\ (\mathrm{mod}\ 20)$ 有 20 個解。20 不是質數，不能直接套；但 $20 = 4\cdot5$，係數都被 4 和 5 整除，配合第 1 節的定理就行 [▶ 16:01](https://youtu.be/TyTUi2pe2sA?t=961)。

【口頭】從 $\mathbb{Z}_n$ 的角度看，這兩個例子很蠢：它們根本就是**零多項式**（13、20、40 在各自的 $\mathbb{Z}_n$ 都是 0），當然每個元素都是根。從「模 $n$ 同餘」的角度看才好像說了什麼 [▶ 17:07](https://youtu.be/TyTUi2pe2sA?t=1027)。

---

## 4. Fermat 小定理

### 4.1 敘述

[▶ 17:39](https://youtu.be/TyTUi2pe2sA?t=1059)

【口頭】Fermat 小定理和 Lagrange 定理沒有直接關係，「我沒有好的轉場」。

**定理（Fermat 小定理）**：$p$ 是質數、$a\not\equiv0\ (\mathrm{mod}\ p)$，則
$$a^{p-1}\equiv1\ (\mathrm{mod}\ p).$$

> 【課本補充】p. 67：別和**Fermat 最後定理**（第 11 章）搞混；Leibniz 也知道，第一個發表證明的是 Euler。

### 4.2 證法一：數論

[▶ 18:11](https://youtu.be/TyTUi2pe2sA?t=1091)

1. $\bar1,\bar2,\dots,\overline{p-1}$ 是 $\mathbb{Z}_p$ 所有非零元素（少的是 $\bar p = \bar0$）。
2. 乘上 $\bar a\neq\bar0$：$\bar a\cdot\bar1,\ \bar a\cdot\bar2,\ \dots,\ \bar a\cdot\overline{p-1}$ 也是**相異**的非零元素。
   - **為什麼相異**：$\bar a\neq\bar0$ ⇒ $\gcd(a,p)=1$ ⇒ $\bar a^{-1}$ 存在（第 10 集）。若 $\bar a\bar x = \bar a\bar y$，乘 $\bar a^{-1}$ 得 $\bar x = \bar y$。
3. 所以兩張表是同一組元素（順序不同），乘積相等：
$$\bar1\cdot\bar2\cdots\overline{p-1} = (\bar a\bar1)(\bar a\bar2)\cdots(\bar a\,\overline{p-1}) \ \Rightarrow\ \overline{(p-1)!} = \bar a^{p-1}\,\overline{(p-1)!}.$$
4. $(p-1)!$ 和 $p$ 互質，$\overline{(p-1)!}^{-1}$ 存在，兩邊乘它：$\bar1 = \bar a^{p-1}$，即 $a^{p-1}\equiv1\ (\mathrm{mod}\ p)$。∎

> 【課本補充】Proof B（p. 68）的例子：$p=5$、$a=3$：$3,6,9,12$ 分別 $\equiv3,1,4,2$，正好是 $1,2,3,4$ 重排。

### 4.3 證法二：群論

[▶ 21:00](https://youtu.be/TyTUi2pe2sA?t=1260)

【口頭】證法一其實也藏了一點群論，「群論無所不在」。

**群的複習**：
- **群**（group）：一個集合加一個二元運算，有單位元素、每個元素有反元素、滿足結合律（且運算封閉）。
- **元素的階**（order）：使 $x^n = e$ 的最小正整數 $n$（乘法寫法，$e$ 常寫 1）；加法群裡是使 $nx = 0$ 的最小正整數。

**例** [▶ 22:36](https://youtu.be/TyTUi2pe2sA?t=1356)：
- $U_{10} = \{\bar1,\bar3,\bar7,\bar9\}$（和 10 互質的同餘類）是乘法群：
  - $3^2 = 9$、$3^3 = 27\equiv7$、$3^4 = 81\equiv1$ → $\bar3$ 的階是 4。
  - $9^2 = 81\equiv1$ → $\bar9$ 的階是 2。
  - $\bar7$ 的階是 4；單位元素 $\bar1$ 的階是 1。
- $\mathbb{Z}_4$ 是加法群：$\bar1+\bar1+\bar1 = \bar3\neq\bar0$，$4\cdot\bar1 = \bar0$ → $\bar1$ 的階是 4；$\bar2+\bar2 = \bar0$ → $\bar2$ 的階是 2。

【口頭】$\mathbb{Z}_n$ 是**環**（有加法和乘法），同一個系統裡同時有加法群 $\mathbb{Z}_n$ 和乘法群 $U_n$（單位群）。之後主要談 $U_n$ [▶ 24:17](https://youtu.be/TyTUi2pe2sA?t=1457)。

**群論定理**：在 $n$ 階有限群裡，每個元素 $x$ 都滿足 $x^n = e$（加法寫法：$nx = 0$）。

【口頭】講者本想寫個短證明，結果發現需要這個、又需要那個——群論裡證明很短，但通往它的路有好幾章。他以前教數論時為了嚴謹寫了 70 頁的補充講義，這次不想這樣折磨大家 [▶ 25:21](https://youtu.be/TyTUi2pe2sA?t=1521)。概要：元素的階整除群的階，因為元素生成的循環子群的大小整除群的大小（**Lagrange 定理（群論）**）。

**檢查**：$U_{10}$（4 階）裡每個 $x^4 = 1$：$\bar9^2 = 1$ 所以 $\bar9^4 = 1$；$\bar9$ 的階 2 整除 4。$\mathbb{Z}_4$ 裡 $4x = 0$。

**證明 Fermat 小定理** [▶ 27:31](https://youtu.be/TyTUi2pe2sA?t=1651)：$a\not\equiv0$ ⇒ $\bar a$ 是單位，屬於 $U_p$。$p$ 是質數，除了 $\bar0$ 每個元素都和 $p$ 互質，所以 $|U_p| = p-1$。由群論定理，$\bar a^{p-1} = \bar1$。∎

【口頭】FLT 這個縮寫有點危險：多數人看到會想到**Fermat 最後定理**。那是本課最後一個要談的 Fermat 定理，敘述簡單、證明難得多，本課不證，只談它的證明 [▶ 28:39](https://youtu.be/TyTUi2pe2sA?t=1719)。

### 4.4 推論：$a^p\equiv a$

[▶ 29:16](https://youtu.be/TyTUi2pe2sA?t=1756)

**推論**：$p$ 質數，對**所有**整數 $a$，$a^p\equiv a\ (\mathrm{mod}\ p)$。也就是在 $\mathbb{Z}_p$ 裡 $x^p = x$ 對所有 $x$。

**證明**：$a\equiv0$ 時兩邊都是 0。$a\not\equiv0$ 時 $a^{p-1}\equiv1$，乘 $a$。∎

【口頭】這很有意思：可以把高次多項式**降次**。例如模 7 時 $x^7$ 就等於 $x$ [▶ 29:16](https://youtu.be/TyTUi2pe2sA?t=1756)。

---

## 5. Wilson 定理

[▶ 30:21](https://youtu.be/TyTUi2pe2sA?t=1821)

**定理（Wilson）**：整數 $n>1$ 是質數 $\iff (n-1)!\equiv-1\ (\mathrm{mod}\ n)$。

【口頭】講者說叫它「推論」有點牽強，其實是定理。Jones & Jones 說它最早由 Lagrange 在 1770 年證明。

**證明 (⇒)**：
- $p=2$：$1! = 1\equiv-1\ (\mathrm{mod}\ 2)$。✓
- $p$ 是奇質數。令
$$f(x) = (1-x)(2-x)\cdots(p-1-x) + 1 - x^{p-1}.$$
  1. **次數 $<p-1$**：乘積的最高次項是 $(-1)^{p-1}x^{p-1} = x^{p-1}$（$p-1$ 是偶數），和 $-x^{p-1}$ 消掉。記 $d = \deg f < p-1$。
  2. 對 $a = 1,\dots,p-1$：乘積含因子 $(a-a) = 0$；而 $1-a^{p-1}\equiv0$（Fermat 小定理）。所以 $f(a)\equiv0$。
  3. $f$ 有 $p-1>d$ 個根，由 Lagrange 的推論，$p$ 整除 $f$ 的所有係數，特別是常數項 $1\cdot2\cdots(p-1)+1 = (p-1)!+1$。所以 $(p-1)!\equiv-1$。

**證明 (⇐)** [▶ 33:10](https://youtu.be/TyTUi2pe2sA?t=1990)：設 $(n-1)!\equiv-1\ (\mathrm{mod}\ n)$。若 $m$ 是 $n$ 的因數，則也 $(n-1)!\equiv-1\ (\mathrm{mod}\ m)$（第 1 節的想法）。若 $1<m<n$，則 $m$ 是 $(n-1)!$ 的一個因數，$(n-1)!\equiv0\ (\mathrm{mod}\ m)$，而 $0\not\equiv-1\ (\mathrm{mod}\ m)$（$m>1$），矛盾。所以 $n$ 沒有真因數，是質數。∎

【口頭】Lagrange 定理不是用來證 Fermat 小定理的，而是和 Fermat 小定理**合起來**證 Wilson 定理——這就是本集要講 Lagrange 定理的原因 [▶ 34:21](https://youtu.be/TyTUi2pe2sA?t=2061)。

> 【課本補充】Theorem 4.6（p. 71）用 Wilson 定理證：奇質數 $p$，$x^2+1\equiv0\ (\mathrm{mod}\ p)$ 有解 $\iff p\equiv1\ (\mathrm{mod}\ 4)$。
> - 令 $k=(p-1)/2$。把 $(p-1)!$ 後半的因子 $p-i$ 換成 $-i$：$(p-1)!\equiv(-1)^k(k!)^2$。由 Wilson，$(k!)^2\equiv(-1)^{k+1}$。$p\equiv1\ (\mathrm{mod}\ 4)$ 時 $k$ 偶數，$x = k!$ 就是解。
> - $p\equiv3\ (\mathrm{mod}\ 4)$ 時 $k$ 奇數；若 $x^2\equiv-1$，則 $1\equiv x^{p-1} = (x^2)^k\equiv(-1)^k = -1$，矛盾。
>
> （這和第 8 集「$4q+1$ 型質數」、之後的二次剩餘有關。）

---

## 6. 計算例子

**例 1**：$2^{50}\bmod23$ [▶ 34:53](https://youtu.be/TyTUi2pe2sA?t=2093)

23 是質數，$2^{22}\equiv1$。$50 = 2\cdot22+6$：
$$2^{50} = (2^{22})^2\cdot2^6\equiv2^6 = 64 = 46+18\equiv18\ (\mathrm{mod}\ 23).$$

（也叫「化成模 23 的最小正剩餘」。從這裡起講者改用中括號記號。）

**例 2**：$3^{32}$ 在 $\mathbb{Z}_{11}$ [▶ 36:33](https://youtu.be/TyTUi2pe2sA?t=2193)

$[3]^{10} = [1]$，所以 $[3]^{30} = [1]$，$[3]^{32} = [3]^{30}[3]^2 = [9]$。

【口頭】不一定要 Fermat 小定理才算得出來，但它能省很多工 [▶ 37:07](https://youtu.be/TyTUi2pe2sA?t=2227)。

**例 3**：$30\mid a^{25}-a$ 對所有整數 $a$（Jones & Jones Example 4.2，p. 69）[▶ 37:41](https://youtu.be/TyTUi2pe2sA?t=2261)

$30 = 2\cdot3\cdot5$，由第 1 節，只要證模 2、3、5 都成立。
- **mod 5**：$x^5 = x$ 在 $\mathbb{Z}_5$，所以 $x^{25} = (x^5)^5 = x^5 = x$。
- **mod 3**：$x^3 = x$ 在 $\mathbb{Z}_3$，
$$x^{25} = (x^3)^8x = x^8\cdot x = x^9 = (x^3)^3 = x^3 = x.$$
- **mod 2**：直接代：$0^{25} = 0$、$1^{25} = 1$。

所以 $a^{25}\equiv a\ (\mathrm{mod}\ 30)$，即 $30\mid a^{25}-a$。

【口頭】講者在 mod 3 那裡示範兩種寫法：一種是同餘和等號混用，另一種全在 $\mathbb{Z}_3$ 裡寫等號，看你喜歡哪種 [▶ 40:23](https://youtu.be/TyTUi2pe2sA?t=2423)。

**例 4**：解 $x^{42}+13x^{26}+15x^{17}+1\equiv0\ (\mathrm{mod}\ 5)$ [▶ 41:28](https://youtu.be/TyTUi2pe2sA?t=2488)

【口頭】原則上可以直接代 $0,\pm1,\pm2$，但次方太高計算機可能受不了；如果次方是 420、2600 也一樣能用下面的方法 [▶ 42:36](https://youtu.be/TyTUi2pe2sA?t=2556)。

在 $\mathbb{Z}_5$ 用 $x^5 = x$ 反覆降次：
- $x^{42} = (x^5)^8x^2 = x^8x^2 = x^{10} = (x^5)^2 = x^2$。
- $x^{26} = (x^5)^5x = x^5x = x^2$。
- $15\equiv0$，那項消失；$13\equiv3$。

所以
$$x^{42}+13x^{26}+15x^{17}+1 = x^2+3x^2+1 = 4x^2+1\quad\text{在 }\mathbb{Z}_5.$$
代 $0,\pm1,\pm2$：$1$、$0$、$0$、$17\equiv2$、$2$……只有 $x=\pm1$ 是根。

（代數看法：$1\equiv-4$，所以 $4x^2+1 = 4x^2-4 = 4(x-1)(x+1)$。講者說他是先代數字找到根，才看出這個分解，不是反過來。）

**解**：$x\equiv1$ 或 $x\equiv4\ (\mathrm{mod}\ 5)$。

⚠️ 逐字稿缺字：[▶ 43:41](https://youtu.be/TyTUi2pe2sA?t=2621) 降次過程字幕有些混亂（例如「x to the 25th times x」、「5x to the 17」），筆記照最後的結果 $4x^2+1$ 重新寫出每一步。

【口頭】$x^p = x$ 的意義：在 $\mathbb{Z}_p$ 上，多項式的理論只到 $p$ 次以下才有趣；更高次都能降回 $<p$ 次——至少把多項式當**函數**看是這樣；當成形式多項式（不定元）就不一樣了 [▶ 45:21](https://youtu.be/TyTUi2pe2sA?t=2721)。

> 【課本補充】Example 4.3（p. 70）類似：$x^{17}+6x^{14}+2x^5+1\equiv0\ (\mathrm{mod}\ 5)$ 降成 $x^2+3x+1\equiv(x-1)^2$，唯一根 $x\equiv1$。Example 4.1：$2^{68}\equiv2^{14}\equiv6\ (\mathrm{mod}\ 19)$。

---

## 7. 一頁速查表

**拆模數**：$n = \prod p_i^{e_i}$ ⇒ $a\equiv b\ (\mathrm{mod}\ n)\iff a\equiv b\ (\mathrm{mod}\ p_i^{e_i})$ 對每個 $i$。

**多項式同餘的怪現象**（模數不是質數時）：$x^2-1$ 在 $\mathbb{Z}_8$ 有 4 個根、兩種分解。

**Lagrange 定理**：$p$ 質數、係數不全 $\equiv0$ ⇒ $f(x)\equiv0\ (\mathrm{mod}\ p)$ 最多 $d$ 個根。
- 關鍵：$f(x) = f(a)+(x-a)g(x)$；$p\mid(b-a)g(b)$ ⇒ $b\equiv a$ 或 $g(b)\equiv0$。
- 推論：超過 $d$ 個根 ⇒ $p$ 整除所有係數。

**Fermat 小定理**：$p\nmid a$ ⇒ $a^{p-1}\equiv1\ (\mathrm{mod}\ p)$。
- 證法一：$\{a,2a,\dots,(p-1)a\}$ 是 $\{1,\dots,p-1\}$ 的重排 ⇒ $(p-1)!\,a^{p-1}\equiv(p-1)!$。
- 證法二：$|U_p| = p-1$，群裡 $x^{|G|} = e$。
- 推論：$a^p\equiv a$ 對所有 $a$ ⇒ 模 $p$ 可降次（$x^p\to x$）。

**Wilson**：$n$ 質數 ⇔ $(n-1)!\equiv-1\ (\mathrm{mod}\ n)$。
- 關鍵：$f(x) = \prod_{i=1}^{p-1}(i-x)+1-x^{p-1}$ 次數 $<p-1$ 卻有 $p-1$ 個根 ⇒ 常數項 $(p-1)!+1\equiv0$。

**例**：$2^{50}\equiv18\ (\mathrm{mod}\ 23)$；$3^{32}\equiv9\ (\mathrm{mod}\ 11)$；$30\mid a^{25}-a$；$x^{42}+13x^{26}+15x^{17}+1\equiv4x^2+1\ (\mathrm{mod}\ 5)$，根 $x\equiv1,4$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 群、元素的階、$x^{\lvert G\rvert}=e$ | 第 14–15 集（單位群 $U_n$、Euler 定理 $a^{\phi(n)}\equiv1$） |
| Fermat 小定理 | 第 15 集（Euler 定理是推廣）、第 16 集（RSA 的正確性） |
| Lagrange 定理（多項式） | 第 15 集（原根的存在）、第 17–18 集（二次同餘） |
| $x^2\equiv-1\ (\mathrm{mod}\ p)$ ⇔ $p\equiv1\ (\mathrm{mod}\ 4)$ | 第 17–18 集（二次互反律）、第 21–22 集（平方和、高斯質數） |

---

## 附：本集一句話總結

> **模質數 $p$ 時，非零多項式最多有「次數」那麼多個根（Lagrange）；$\mathbb{Z}_p$ 的非零元素乘上 $a$ 只是重排，所以 $a^{p-1}\equiv1$（Fermat 小定理），因此 $x^p=x$ 可以把高次方降下來；兩者合起來證出 Wilson 定理 $(p-1)!\equiv-1\ (\mathrm{mod}\ p)$。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 13 錄影逐字稿（YouTube 自動字幕，46:41）與 Jones & Jones《Elementary Number Theory》§3.1、§4.1 整理。*
