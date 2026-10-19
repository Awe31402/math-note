---
course: Abstract Algebra I (Fall 2016)
episode: 19
lecture: L12（第 2 段）
date: 2016-09-28
video: https://www.youtube.com/watch?v=YRCtHmEfxFw
notes: AlgebraInotes_2018.pdf §3.1 Lecture 11（p.82–87）
---

# 第 19 集 · L12（下）：陪集與 Lagrange 定理 [▶ 影片](https://www.youtube.com/watch?v=YRCtHmEfxFw&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[18-L12-陪集與Lagrange定理-上]] ｜ [總目錄](../README.md) ｜ 下一集：[[20-答疑課]] →

## 本集概要

- **左陪集** $aH$、**右陪集** $Ha$（加法群寫 $a+H$）。
- 例：$S_3$ 中 $H = \{(1),(13)\}$ 的三個左陪集。
- **陪集的性質**：$a\in aH$；$aH = H\iff a\in H$；兩個陪集**要嘛相等、要嘛不相交**；$aH = bH\iff a^{-1}b\in H$；所有陪集一樣大。
- **Lagrange 定理**：有限群中，子群的階整除群的階；左陪集個數 $= |G|/|H|$，叫**指數** $[G:H]$。
- 推論：**質數階的群是循環群**。

> 📘 講義對應：2018 講義 §3.1 Lecture 11「cosets and Lagrange's Theorem」（p.82–87）；Gallian 第 7 章（陪集性質引理、Thm 7.1 Lagrange 定理、Cor 2）。

---

## 筆記

### 1. 陪集的定義 [▶ 00:00](https://youtu.be/YRCtHmEfxFw?t=0)

設 $H\subseteq G$（先**不**假設 $H$ 是子群），$a\in G$。

> **定義**
> - **左陪集 (left coset)**：$aH = \{ah\mid h\in H\}$
> - **右陪集 (right coset)**：$Ha = \{ha\mid h\in H\}$
>
> $a$ 叫這個陪集的**代表元 (representative)**。

- 老師一開始想說「含 $a$ 的左陪集」，隨即更正：$H$ 不是子群時，$aH$ 不一定含 $a$，所以只能說「代表元為 $a$」[▶ 00:30](https://youtu.be/YRCtHmEfxFw?t=30)。
- **加法群**：寫成 $a+H$、$H+a$；加法群是交換的，兩者相等 [▶ 01:30](https://youtu.be/YRCtHmEfxFw?t=90)。
- $|aH|$ 表示集合 $aH$ 的元素個數。

### 2. 例：$S_3$，$H = \{(1),(13)\}$ [▶ 03:00](https://youtu.be/YRCtHmEfxFw?t=180)

（跟著 Gallian 的例子。）

| 代表元 | 左陪集 |
|---|---|
| $(1)$ 或 $(13)$ | $\{(1),(13)\} = H$ |
| $(12)$ 或 $(132)$ | $\{(12),(132)\}$ |
| $(23)$ 或 $(123)$ | $\{(23),(123)\}$ |

計算（由右往左）：
- $(13)H = \{(13),(13)(13)\} = \{(13),(1)\} = H$，因為換位的階是 2 [▶ 04:30](https://youtu.be/YRCtHmEfxFw?t=270)。
- $(12)(13) = (132)$，所以 $(12)H = \{(12),(132)\}$ [▶ 05:00](https://youtu.be/YRCtHmEfxFw?t=300)。
- $(132)(13) = (12)$，所以 $(132)H = (12)H$ [▶ 05:30](https://youtu.be/YRCtHmEfxFw?t=330)。
- $(23)(13) = (123)$，所以 $(23)H = (123)H = \{(23),(123)\}$ [▶ 06:00](https://youtu.be/YRCtHmEfxFw?t=360)。

六個元素全用完，共**三個**陪集，每個 2 個元素，互不相交 [▶ 07:00](https://youtu.be/YRCtHmEfxFw?t=420)。這裡 $H = \langle(13)\rangle$ 是子群。

### 3. 代表元在自己的陪集裡 [▶ 08:00](https://youtu.be/YRCtHmEfxFw?t=480)

> **定理**　若 $H\le G$，則 $a\in aH$ 且 $a\in Ha$。

**證明**：$e\in H$（子群），所以 $a = ae\in aH$、$a = ea\in Ha$。$\blacksquare$

若 $H$ 不是子群，就沒有這個保證 [▶ 09:00](https://youtu.be/YRCtHmEfxFw?t=540)。

### 4. 陪集的性質 [▶ 09:30](https://youtu.be/YRCtHmEfxFw?t=570)

> **定理（Gallian 第 7 章「陪集性質」引理）**　$H\le G$，$a,b\in G$。
> 1. $aH = H\iff a\in H$
> 2. $aH = bH$ 或 $aH\cap bH = \varnothing$
> 3. $aH = bH\iff a^{-1}b\in H$
> 4. $|aH| = |bH|$
> 5. $aH = Ha\iff H = aHa^{-1}$
> 6. $aH\le G\iff a\in H$

（老師說他的編號和 Gallian 差一個。也開玩笑說捨不得從 Gallian 撕頁：「這本不是微積分課本那種粗用工具，是藝術品」[▶ 10:30](https://youtu.be/YRCtHmEfxFw?t=630)。）

**證明 (1)** [▶ 13:00](https://youtu.be/YRCtHmEfxFw?t=780)
- ($\Rightarrow$) $a = ae\in aH = H$。
- ($\Leftarrow$) 設 $a\in H$。
  - $aH\subseteq H$：$x\in aH$ 則 $x = ah$，$a,h\in H$，子群封閉，$x\in H$ [▶ 14:30](https://youtu.be/YRCtHmEfxFw?t=870)。
  - $H\subseteq aH$：$y\in H$ 則 $y = a(a^{-1}y)$，而 $a^{-1}y\in H$，所以 $y\in aH$ [▶ 17:00](https://youtu.be/YRCtHmEfxFw?t=1020)。

> 💬 老師中途把兩個方向寫重複了，學生提醒才改 [▶ 16:00](https://youtu.be/YRCtHmEfxFw?t=960)。

**證明 (2)** [▶ 18:00](https://youtu.be/YRCtHmEfxFw?t=1080)　只要證：若交集**非空**，則相等。
- 取 $x\in aH\cap bH$：$x = ah_1 = bh_2$。
- 解出 $b = xh_2^{-1} = ah_1h_2^{-1}$。因為 $h_1h_2^{-1}\in H$，所以 $b\in aH$ [▶ 20:00](https://youtu.be/YRCtHmEfxFw?t=1200)。
- 任取 $y = bh_3\in bH$：$y = ah_1h_2^{-1}h_3\in aH$。所以 $bH\subseteq aH$ [▶ 22:30](https://youtu.be/YRCtHmEfxFw?t=1350)。
- $a$、$b$ 地位對稱，同理 $aH\subseteq bH$。$\blacksquare$

**證明 (3)** [▶ 24:30](https://youtu.be/YRCtHmEfxFw?t=1470)

（加法版：$a+H = b+H\iff b-a\in H$。和模運算的同餘一樣。）
- ($\Rightarrow$) $b\in bH = aH$，所以 $b = ah$，$a^{-1}b = h\in H$ [▶ 26:30](https://youtu.be/YRCtHmEfxFw?t=1590)。
- ($\Leftarrow$) $a^{-1}b = h\in H$，所以 $b = ah\in aH$。又 $b\in bH$，所以 $aH\cap bH\neq\varnothing$，由 (2) 得 $aH = bH$ [▶ 28:00](https://youtu.be/YRCtHmEfxFw?t=1680)。

> 💬 老師一開始走錯路，推出 $ab^{-1}\in H$（對，但不是要的）[▶ 26:00](https://youtu.be/YRCtHmEfxFw?t=1560)。

**證明 (4)** [▶ 31:00](https://youtu.be/YRCtHmEfxFw?t=1860)：定義 $\varphi:aH\to bH$，$\varphi(ah) = bh$。它是一對一且映成（反映射是 $bh\mapsto ah$），所以兩個集合一樣大。

（(5)、(6) 課堂沒證。）

### 5. Lagrange 定理 [▶ 32:00](https://youtu.be/YRCtHmEfxFw?t=1920)

> **定理（Lagrange 定理；Gallian Thm 7.1）**　$G$ 是有限群，$H\le G$。則 $|H|$ 整除 $|G|$。而且 $H$ 的不同左（或右）陪集的個數是 $|G|/|H|$。

**檢查例子** [▶ 33:30](https://youtu.be/YRCtHmEfxFw?t=2010)：$|S_3| = 6$，$|H| = 2$，陪集 $6/2 = 3$ 個 ✓。

**證明** [▶ 34:00](https://youtu.be/YRCtHmEfxFw?t=2040)（老師最喜歡的證明之一，「美得很簡單」）
- 每個元素 $g$ 都在某個陪集裡（$g\in gH$）。
- 由性質 (2)，陪集兩兩相等或不相交。所以 $G$ 是**互不相交**的陪集的聯集：
$$G = a_1H\cup a_2H\cup\cdots\cup a_kH,\qquad a_iH\cap a_jH = \varnothing\ (i\neq j).$$
  可以取 $a_1 = e$，第一塊就是 $H$ [▶ 36:00](https://youtu.be/YRCtHmEfxFw?t=2160)。
- 同一個陪集可能有不同的代表元（例如 $(12)H = (132)H$），但每個元素只屬於**一個**陪集 [▶ 35:00](https://youtu.be/YRCtHmEfxFw?t=2100)。
- 由性質 (4)，每塊都有 $|H|$ 個元素。數一數：
$$|G| = |H| + |a_2H| + \cdots + |a_kH| = k|H|.$$
- 所以 $|H|$ 整除 $|G|$，而陪集個數 $k = |G|/|H|$。$\blacksquare$

**老師的評論** [▶ 37:30](https://youtu.be/YRCtHmEfxFw?t=2250)：如果能重來，他會在循環群之前先證這個；循環群的一些結果用它會簡單很多。

> **定義（指數 index）**　$H$ 在 $G$ 中的左陪集個數記作 $[G:H]$。有限群時，Lagrange 定理說
> $$[G:H] = \frac{|G|}{|H|}.$$

**無限群** [▶ 38:30](https://youtu.be/YRCtHmEfxFw?t=2310)：不能數個數，但陪集仍然把 $G$ **分割**成互不相交的部分。這點很重要。

### 6. 推論：質數階的群是循環群 [▶ 39:00](https://youtu.be/YRCtHmEfxFw?t=2340)

> **推論（Gallian Cor 2 of Thm 7.1）**　$|G| = p$ 是質數，則 $G$ 是循環群。

**證明** [▶ 39:30](https://youtu.be/YRCtHmEfxFw?t=2370)
- 取 $a\in G$，$a\neq e$。
- $\langle a\rangle\le G$，由 Lagrange，$|\langle a\rangle|$ 整除 $p$，只能是 $1$ 或 $p$。
- $a\neq e$，所以 $|\langle a\rangle|\neq1$。因此 $|\langle a\rangle| = p$，即 $\langle a\rangle = G$。$\blacksquare$

**例**：任何 17 階的群都是循環群。這是以前得不到的結果，而且得來不費力 [▶ 40:30](https://youtu.be/YRCtHmEfxFw?t=2430)。陪集的概念「已經大大回本」，之後會更強大。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 陪集；左陪集；右陪集 | coset; left coset; right coset | [00:30](https://youtu.be/YRCtHmEfxFw?t=30) |
| 代表元 | representative | [01:00](https://youtu.be/YRCtHmEfxFw?t=60) |
| 不相交 | disjoint | [11:00](https://youtu.be/YRCtHmEfxFw?t=660) |
| Lagrange 定理 | Lagrange's Theorem | [32:00](https://youtu.be/YRCtHmEfxFw?t=1920) |
| 不相交聯集 | disjoint union | [34:00](https://youtu.be/YRCtHmEfxFw?t=2040) |
| 指數 | index $[G:H]$ | [37:30](https://youtu.be/YRCtHmEfxFw?t=2250) |

## ⚠️ 待確認清單

（本集無）
