---
course: Number Theory（2021 秋，線上錄影）
episode: 21
lecture: Lecture 20
date: 待補（2021 秋）
video: https://youtu.be/xjNSJ8G3dug
notes: Jones & Jones §10.1–10.3（書頁 191–201，PDF 頁 206–216）：Lemma 10.1、Theorem 10.2–10.3、Corollary 10.4、§10.2 高斯整數、Example 10.7、§10.3 開頭；講者說 $S_k$ 記號取自 Jones & Jones
---

# 第 21 集 · Lecture 20：平方和與高斯整數（Sums of Squares and Gaussian Integers） [▶ 影片](https://youtu.be/xjNSJ8G3dug)

← 上一集：[20-solution-of-the-cubic](20-solution-of-the-cubic.md) ｜ [總目錄](README.md) ｜ 下一集：[22-primes-and-gaussian-integers](22-primes-and-gaussian-integers.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 21 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（46:47，自動字幕）＋ Jones & Jones §10.1–10.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 高斯整數與範數](#1-高斯整數與範數)
- [2. 單位](#2-單位)
- [3. 除法演算法](#3-除法演算法)
- [4. 整除、高斯質數、相伴](#4-整除高斯質數相伴)
- [5. 平方和 S_k](#5-平方和-s_k)
- [6. 哪些數是高斯質數](#6-哪些數是高斯質數)
- [7. 唯一分解、gcd、Bézout](#7-唯一分解gcdbézout)
- [8. 高斯整數的輾轉相除](#8-高斯整數的輾轉相除)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 段落 | 內容 | 課本 |
|---|---|---|
| 1–3 | $\mathbb{Z}[i]$、範數 $N$、單位 $\pm1,\pm i$、除法演算法 | §10.2、Example 10.7 |
| 4–6 | 高斯質數；$N$ 是質數 ⇒ 高斯質數；$p$ 是高斯質數 ⇔ $p$ 不是兩平方和 | §10.2 p. 198–199 |
| 5 | $S_2$ 對乘法封閉 | Lemma 10.1 |
| 7–8 | 唯一分解、gcd、向量輾轉相除 | §10.2 |

本集的主要目標：對「什麼是高斯質數、什麼不是」建立初步直覺——有時結果令人意外 [▶ 11:48](https://youtu.be/xjNSJ8G3dug?t=708)。

---

## 1. 高斯整數與範數

[▶ 00:00](https://youtu.be/xjNSJ8G3dug?t=0)

**定義**：**高斯整數**（Gaussian integers）
$$\mathbb{Z}[i] = \{\,a+bi : a,b\in\mathbb{Z}\,\}\subset\mathbb{C}.$$
它是複數的子集合，所以加、減、乘、除、共軛都已經會了。

**定義**：**範數**（norm）
$$N(a+bi) = a^2+b^2 = z\bar z.$$
把高斯整數送到非負整數。

**性質**（講者說會當第一份作業）[▶ 01:38](https://youtu.be/xjNSJ8G3dug?t=98)：
1. $N(zw) = N(z)N(w)$；
2. $N(z)\ge0$；
3. $N(z) = 0\iff z = 0$。

（性質 1 就是上一集的 $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$ 平方。）

---

## 2. 單位

[▶ 01:38](https://youtu.be/xjNSJ8G3dug?t=98)

**定義**：$z\in\mathbb{Z}[i]$ 是**單位**，若存在 $w\in\mathbb{Z}[i]$ 使 $zw = 1$。
（和整數一樣：$\mathbb{Z}$ 的單位只有 $\pm1$；2 不是單位，因為 $\frac12\notin\mathbb{Z}$。）

**定理**：$\mathbb{Z}[i]$ 的單位恰好是 $1,-1,i,-i$——也就是**四次單位根**。

**證明** [▶ 03:16](https://youtu.be/xjNSJ8G3dug?t=196)：$zw = 1$，取範數：$N(z)N(w) = N(1) = 1$。兩個都是正整數（不能是 0，因為 $0\cdot(\cdot)\neq1$），所以 $N(z) = 1$：$a^2+b^2 = 1$，只有 $(a,b) = (\pm1,0)$ 或 $(0,\pm1)$。∎

【口頭】整數有兩個單位所以常有 $\pm$ 兩種選擇；高斯整數有四個單位，所以常有四種選擇 [▶ 04:22](https://youtu.be/xjNSJ8G3dug?t=262)。

---

## 3. 除法演算法

[▶ 04:54](https://youtu.be/xjNSJ8G3dug?t=294)

**例**：$a = 10+3i$、$b = 2+3i$。
1. 先在複數裡算 $a/b$（乘共軛有理化）：
$$\frac{10+3i}{2+3i} = \frac{(10+3i)(2-3i)}{13} = \frac{29-24i}{13}.$$
2. 找**最接近**的高斯整數：$\frac{29}{13}\approx\frac{26}{13} = 2$，$-\frac{24}{13}\approx-\frac{26}{13} = -2$，取 $q = 2-2i$。「接近」指實部、虛部都相差不超過 $\frac12$——總是辦得到。
3. $qb = (2-2i)(2+3i) = 10+2i$，餘數 $r = a-qb = i$。
4. $N(r) = 1<13 = N(b)$。

**定理（高斯整數的除法演算法）**：$a,b\in\mathbb{Z}[i]$、$b\neq0$，存在 $q,r\in\mathbb{Z}[i]$ 使
$$a = qb+r,\qquad r = 0 \text{ 或 } N(r)<N(b).$$

（以下**不是逐字稿內容**，是依「實部、虛部各差不超過 $\frac12$」補的理由：$\frac ab - q = \delta$，$\lvert\delta\rvert^2\le\frac14+\frac14 = \frac12$，所以 $N(r) = N(b\delta) = N(b)\lvert\delta\rvert^2\le\frac12N(b)<N(b)$。注意 $q$ 不一定唯一。）

> 【課本補充】§10.2（p. 196–198）：$\mathbb{Z}[i]$ 是**整環**（integral domain：$rs = 0\Rightarrow r = 0$ 或 $s = 0$），而且是**歐幾里得整環**（Euclidean domain，有一個大小函數 $d$ 讓除法演算法成立），取 $d(z) = N(z)$（Example 10.7）。課本的幾何證明：$b$ 的倍數 $qb$ 是邊長 $\lvert b\rvert$ 的正方形格子的頂點，每個點離某頂點最多 $\lvert b\rvert/\sqrt2$，所以 $d(r)\le\lvert b\rvert^2/2<d(b)$。

---

## 4. 整除、高斯質數、相伴

### 4.1 定義

[▶ 07:08](https://youtu.be/xjNSJ8G3dug?t=428)

- $z\mid w$（在 $\mathbb{Z}[i]$）：存在 $c$ 使 $w = cz$；$w$ 是 $z$ 的倍數。
- **高斯質數**（Gaussian prime）：$z$ 的因數只有單位和 $z$ 的相伴元。等價地：$z$ 的任何分解中，總有一個因數的範數是 1（是單位）。
- **相伴**（associates）：若有單位 $u$ 使 $z = uw$，則 $z,w$ 相伴。每個非零高斯整數有**四個**相伴元。

> 【課本補充】課本（p. 198）把這叫**不可約元**（irreducible）：不是 0 也不是單位、因數只有單位和相伴元。相伴是等價關係（因為單位形成乘法群）。

### 4.2 例：$1+i$

[▶ 08:22](https://youtu.be/xjNSJ8G3dug?t=502)

$N(1+i) = 2$。若 $1+i = z_1z_2$，則 $2 = N(z_1)N(z_2)$，只能是 $1\cdot2$ 或 $2\cdot1$，總有一個因數範數是 1。所以 $1+i$ 是高斯質數。

它也能寫成其他乘積，但總有一個因數是單位 [▶ 09:30](https://youtu.be/xjNSJ8G3dug?t=570)：
$$1+i = 1\cdot(1+i) = (-1)(-1-i) = (-i)(-1+i) = i(1-i).$$

⚠️ 講者板書一度把「$i\cdot(i-1)$」寫成等於 $1+i$，乘開發現是 $-1-i$，當場改符號 [▶ 10:07](https://youtu.be/xjNSJ8G3dug?t=607)。

**$1+i$ 的相伴元**：$1+i$、$-1-i$、$i(1+i) = -1+i$、$-i(1+i) = 1-i$。（講者說「我想應該有 $-1+i$，如果我沒算錯的話」[▶ 10:38](https://youtu.be/xjNSJ8G3dug?t=638)。）

### 4.3 例：2 和 3

[▶ 12:19](https://youtu.be/xjNSJ8G3dug?t=739)

- **2 不是高斯質數**：$2 = (1+i)(1-i)$，兩個因數範數都是 2，不是單位。**2 在整數裡是質數，在高斯整數裡不是。**

  （以下**不是逐字稿內容**：因為 $1-i = -i(1+i)$，所以其實 $2 = -i(1+i)^2$，2 是一個高斯質數的平方乘上單位。）
- **3 是高斯質數** [▶ 12:51](https://youtu.be/xjNSJ8G3dug?t=771)：若 $3 = z_1z_2$，則 $9 = N(z_1)N(z_2)$，可能是 $1\cdot9$、$3\cdot3$、$9\cdot1$。$1\cdot9$、$9\cdot1$ 沒問題（有單位）。要排除 $3\cdot3$，也就是證明 $a^2+b^2 = 3$ 無解：$1+1 = 2$、$1+4 = 5$、$4+4 = 8$、$4+0 = 4$……再大更不行。所以 3 是高斯質數。

【口頭】講者說前面某集證過關於平方和的事（例如平方數模 4），應該能拿來用，但他沒時間回去查：「我的記憶力不比從前，每次生小孩都掉一些記憶。」[▶ 14:32](https://youtu.be/xjNSJ8G3dug?t=872)（第 11 集證過平方數 mod 4 只能是 0、1，所以 $a^2+b^2\not\equiv3\ (\mathrm{mod}\ 4)$。）

【口頭】本集暗號是「the ace of spades」[▶ 15:05](https://youtu.be/xjNSJ8G3dug?t=905)。

### 4.4 整除與範數

[▶ 15:05](https://youtu.be/xjNSJ8G3dug?t=905)

**定理**：若 $\alpha\mid\beta$（在 $\mathbb{Z}[i]$），則 $N(\alpha)\mid N(\beta)$（在 $\mathbb{Z}$）。

**證明**：$\beta = c\alpha$ ⇒ $N(\beta) = N(c)N(\alpha)$。∎

【口頭】「這是很好的考題，不是威脅喔。」

---

## 5. 平方和 S_k

### 5.1 定義

[▶ 16:12](https://youtu.be/xjNSJ8G3dug?t=972)

（記號取自 Jones & Jones，但講者說他沒有精確照任何一本書，「主要是我的錯」。）

$$S_k = \{\,x_1^2+\cdots+x_k^2 : x_i\in\mathbb{Z}\,\}.$$
- $S_1$ = 平方數。
- $S_2 = \{0,1,2,4,5,8,\dots\}$：$0 = 0^2+0^2$、$1 = 0^2+1^2$、$2 = 1^2+1^2$、$4 = 0^2+2^2$、$5 = 1^2+2^2$、$8 = 2^2+2^2$。
- 3、6、7 **不在** $S_2$ 裡（找不到兩個整數平方和等於它們）。$S_2$ 到底是什麼？下一集也許會回答。

### 5.2 $S_2$ 對乘法封閉

[▶ 17:51](https://youtu.be/xjNSJ8G3dug?t=1071)

**定理**：$a,b\in S_2\Rightarrow ab\in S_2$。

【口頭】古希臘的 Diophantus 就知道，印度的 Brahmagupta 等人也知道（「還有另一位我不會唸名字的印度數學家」）。古人不是用高斯整數看的，講者用高斯整數 [▶ 17:51](https://youtu.be/xjNSJ8G3dug?t=1071)。

**證明**：$a = a_1^2+a_2^2$、$b = b_1^2+b_2^2$。**狡猾的一步**：把它們看成範數
$$a = N(a_1+ia_2),\qquad b = N(b_1+ib_2).$$
讓範數的乘法性做苦工：
$$ab = N\big((a_1+ia_2)(b_1+ib_2)\big) = N\big((a_1b_1-a_2b_2) + i(a_1b_2+a_2b_1)\big) = (a_1b_1-a_2b_2)^2+(a_1b_2+a_2b_1)^2.\ ∎$$

**例** [▶ 19:31](https://youtu.be/xjNSJ8G3dug?t=1171)：
- $5 = N(1+2i)$、$8 = N(2+2i)$：$40 = N\big((1+2i)(2+2i)\big) = N(-2+6i) = 4+36$。
- $200 = 5\cdot40$：
  - $(1+2i)(2+6i) = -10+10i$ ⇒ $200 = 10^2+10^2$；
  - $(1+2i)(-2+6i) = -14+2i$ ⇒ $200 = 14^2+2^2 = 196+4$。

  （把 $-2$ 換成 $2$ 不改變範數，但乘積不同。）

**寫成兩平方和的方式不唯一**；理解背後的高斯整數，就能找出各種寫法 [▶ 21:46](https://youtu.be/xjNSJ8G3dug?t=1306)。

【口頭】講者寫算式時少了一個括號：「我剛剛才罵完我小孩不補括號，最好在他們發現之前補上。」[▶ 20:04](https://youtu.be/xjNSJ8G3dug?t=1204)

> 【課本補充】Lemma 10.1（p. 192）就是這個恆等式 $(a_1^2+b_1^2)(a_2^2+b_2^2) = (a_1a_2-b_1b_2)^2+(a_1b_2+b_1a_2)^2$（10.1）；把 $b_1$ 換成 $-b_1$ 得另一個（10.2）。Example 10.2：$80 = 8\cdot10 = 4^2+8^2$。

### 5.3 $S_3$ 和 $S_4$

[▶ 22:21](https://youtu.be/xjNSJ8G3dug?t=1341)

依 Jones & Jones p. 201：
- $S_3$（三平方和）比較難，**不**對乘法封閉；Gauss 知道它的刻畫。
- $S_4$：**每個自然數都是至多四個平方的和**——Lagrange 1770 年的**四平方定理**。完整證明在某種意義上依賴**四元數**的結構（之後的集數），四元數證明 $S_4$ 對乘法封閉，就像高斯整數證明 $S_2$ 封閉。

> 【課本補充】§10.3（p. 201）：Gauss 證明 $n\in S_3\iff n\neq4^e(8k+7)$；例如 3、5 在 $S_3$ 但 15 不在。

---

## 6. 哪些數是高斯質數

### 6.1 範數是質數 ⇒ 高斯質數

**例**：$4+i$ [▶ 24:03](https://youtu.be/xjNSJ8G3dug?t=1443)：$N = 17$ 是質數，任何分解 $\alpha\beta$ 都有 $N(\alpha)N(\beta) = 17$，總有一個是 1。所以是高斯質數。

**定理**：若 $z = a+bi\neq0$ 且 $N(z) = a^2+b^2 = p$ 是質數，則 $z$ 和 $\bar z = a-bi$ 都是高斯質數。

**證明** [▶ 24:38](https://youtu.be/xjNSJ8G3dug?t=1478)：
- $z$：就是上面的例子寫成一般形式。
- $\bar z$：設 $\bar z = \lambda\delta$。取共軛：$z = \bar\lambda\,\bar\delta$。$z$ 是高斯質數，所以 $N(\bar\lambda) = 1$ 或 $N(\bar\delta) = 1$。而 $N(\bar\lambda) = \bar\lambda\lambda = N(\lambda)$，同理 $N(\bar\delta) = N(\delta)$。所以 $\lambda$ 或 $\delta$ 是單位。∎

**例** [▶ 26:49](https://youtu.be/xjNSJ8G3dug?t=1609)：$5+2i$：$N = 25+4 = 29$ 是質數，所以 $5\pm2i$ 是高斯質數。

這是造高斯質數的好方法，但不是全部：3 這種普通質數也是高斯質數；而不是每個普通質數都是高斯質數（如 2）。

### 6.2 普通質數何時是高斯質數

[▶ 27:21](https://youtu.be/xjNSJ8G3dug?t=1641)

**定理**：$p$ 是（自然數中的）質數。則
$$p \text{ 是高斯質數} \iff \text{不存在整數 } a,b \text{ 使 } p = a^2+b^2.$$

**證明**：
- (⇐) 設 $p$ 不是兩平方和，且 $p = \gamma_1\gamma_2$（在 $\mathbb{Z}[i]$）。$p = \bar p$，所以
$$p^2 = p\bar p = \gamma_1\gamma_2\,\overline{\gamma_1\gamma_2} = (\gamma_1\bar\gamma_1)(\gamma_2\bar\gamma_2) = N(\gamma_1)N(\gamma_2).$$
兩個自然數乘積是 $p^2$，只有 $(p^2,1)$、$(1,p^2)$、$(p,p)$ 三種。第三種表示 $N(\gamma_1) = p$，即 $p$ 是兩平方和，和假設矛盾。所以只能是前兩種，$\gamma_1$ 或 $\gamma_2$ 是單位，$p$ 是高斯質數。
- (⇒) 設 $p$ 是高斯質數，反證：若 $p = a^2+b^2$，則 $p = (a+bi)(a-bi)$，兩個因數範數都是 $p$，不是單位——和 $p$ 是高斯質數矛盾。∎

（講者找不到棕色筆，改用灰色筆；他一度寫成「兩個都是 1」，馬上改正 [▶ 29:01](https://youtu.be/xjNSJ8G3dug?t=1741)。）

**怎麼完整分類高斯質數？** 下一集（Lecture 21）回答 [▶ 31:15](https://youtu.be/xjNSJ8G3dug?t=1875)。

> 【課本補充】Jones & Jones 的結論（p. 193–199，第 22 集會用到）：
> - **Theorem 10.2**（Fermat 1640 敘述、Euler 1754 證明）：每個質數 $p\equiv1\ (\mathrm{mod}\ 4)$ 都是兩平方和。（證明用 $-1$ 是模 $p$ 的二次剩餘 + 無窮遞降。）
> - **Corollary 10.4**：質數 $p$ 是兩平方和 $\iff p = 2$ 或 $p\equiv1\ (\mathrm{mod}\ 4)$。
> - **Theorem 10.3**：正整數 $n$ 是兩平方和 $\iff$ 每個 $q\equiv3\ (\mathrm{mod}\ 4)$ 的質數在 $n$ 中的次數是偶數。例：$60 = 2^2\cdot3\cdot5$ 不是；$180 = 2^2\cdot3^2\cdot5 = 12^2+6^2$ 是。
> - 配合本節定理：$p\equiv3\ (\mathrm{mod}\ 4)$ 的質數都是高斯質數；$p = 2$ 或 $p\equiv1\ (\mathrm{mod}\ 4)$ 都會分解。

---

## 7. 唯一分解、gcd、Bézout

[▶ 31:49](https://youtu.be/xjNSJ8G3dug?t=1909)

**高斯整數的算術基本定理**：每個（非零、非單位的）高斯整數都能分解成高斯質數的乘積，而且**在相伴的意義下唯一**。講者不證，說證明類似整數的情形。

**例** [▶ 32:21](https://youtu.be/xjNSJ8G3dug?t=1941)：
$$5+31i = (1+i)(4+i)(5+2i).$$
（講者坦白：他是先挑這三個高斯質數乘起來得到 $5+31i$ 的；真的要分解高斯整數很痛苦。筆記驗證：$(1+i)(4+i) = 3+5i$，$(3+5i)(5+2i) = 5+31i$；三個因數的範數 2、17、29 都是質數。）

**「在相伴意義下唯一」的意思** [▶ 32:56](https://youtu.be/xjNSJ8G3dug?t=1976)：可以塞進 $1 = (-1)(-1)$ 或 $1 = (-i)(i)$，例如
$$5+31i = (-1-i)(-4-i)(5+2i) = (i-1)(4+i)(-i)(5+2i)\cdot\ldots$$
（把某兩個因數分別乘 $-1$、$-1$，或乘 $i$、$-i$。）分解不完全唯一，但很接近，只差單位。

【口頭】整數其實也一樣，只是我們不太在意：問「22 怎麼分解」，大家說 $2\cdot11$，但 $(-2)(-11)$、$(-1)(-22)$ 也是。整數有兩個單位、高斯整數有四個，所以有四種選擇 [▶ 33:29](https://youtu.be/xjNSJ8G3dug?t=2009)。

**例** [▶ 34:03](https://youtu.be/xjNSJ8G3dug?t=2043)：
- $12 = 2^2\cdot3 = (1+i)^2(1-i)^2\cdot3$。（3 是高斯質數；2 不是，要拆成 $(1+i)(1-i)$。）
- $45+18i = 9(5+2i) = 3^2(5+2i)$。

**gcd** [▶ 35:09](https://youtu.be/xjNSJ8G3dug?t=2109)：只能定義「**一個**」gcd——共有四個（差單位）。$d$ 是 $a,b$ 的一個 gcd，若 $d\mid a$、$d\mid b$，且對任何公因數 $\tilde d$ 有 $N(\tilde d)\le N(d)$。$\pm d$、$\pm id$ 都是合理的 gcd。

**Bézout**：$z,w$ 不全為 0，存在 $a,b\in\mathbb{Z}[i]$ 使 $az+bw = \gcd(z,w)$（向量輾轉相除法仍適用）。

**Euclid 引理**（講者不確定名字）[▶ 36:22](https://youtu.be/xjNSJ8G3dug?t=2182)：高斯質數 $\pi\mid\alpha\beta$ ⇒ $\pi\mid\alpha$ 或 $\pi\mid\beta$。證明和整數類似。

---

## 8. 高斯整數的輾轉相除

**例 1**：$z = 11+3i$、$w = 1-i$ [▶ 36:54](https://youtu.be/xjNSJ8G3dug?t=2214)
$$\frac{11+3i}{1-i} = \frac{(11+3i)(1+i)}{2} = \frac{8+14i}2 = 4+7i.$$
是高斯整數！餘數 0，所以 $w\mid z$，$\gcd(z,w) = w$。（「好尷尬。」）

**例 2**：$z = 11+3i$、$w = 2+3i$ [▶ 37:27](https://youtu.be/xjNSJ8G3dug?t=2247)

| 步驟 | 計算 |
|---|---|
| $z/w$ | $\frac{(11+3i)(2-3i)}{13} = \frac{31-27i}{13}\approx2-2i$，$q_1 = 2-2i$ |
| $r_1$ | $z-q_1w = (11+3i)-(10+2i) = 1+i$，$N(r_1) = 2<13$ |
| $w/r_1$ | $\frac{(2+3i)(1-i)}2 = \frac{5+i}2 = 2.5+0.5i\approx2$，$q_2 = 2$ |
| $r_2$ | $w-2r_1 = (2+3i)-(2+2i) = i$ |

餘數是單位，下一步就是 0（「我從不在乎那最後一步」），所以 $\gcd = i$（等價地 $= 1$，互質）。

【口頭】接近實數時就取實數，比較簡單 [▶ 39:09](https://youtu.be/xjNSJ8G3dug?t=2349)。

⚠️ 逐字稿缺字：[▶ 38:02](https://youtu.be/xjNSJ8G3dug?t=2282) 字幕說「13 minus 27 i over and 31 rather」，應為 $\frac{31-27i}{13}$。

**向量輾轉相除**：

| 數 | 組合 |
|---|---|
| $11+3i$ | $z$ |
| $2+3i$ | $w$ |
| $1+i$ | $z-(2-2i)w$ |
| $i$ | $w-2\big(z-(2-2i)w\big) = -2z+(5-4i)w$ |

所以 $-2(11+3i)+(5-4i)(2+3i) = i$（Bézout）。（筆記用 Python 驗證。）

**例 3**：$z = -4+2i$、$w = 3+2i$ [▶ 41:58](https://youtu.be/xjNSJ8G3dug?t=2518)
- $z/w = \frac{(-4+2i)(3-2i)}{13} = \frac{-8+14i}{13}\approx-1+i$，$q_1 = -1+i$；$q_1w = -5+i$，$r_1 = z-q_1w = 1+i$。
- $w/r_1 = \frac{5-i}2\approx2$，$q_2 = 2$；$r_2 = w-2r_1 = 1$。
- gcd 是 1，互質。

向量形式：$1 = w-2r_1 = w-2\big(z-(-1+i)w\big) = -2z+(-1+2i)w$。

⚠️ 逐字稿缺字：[▶ 41:58](https://youtu.be/xjNSJ8G3dug?t=2518) 字幕說 $z/w = \frac{-18+4i}{13}$，筆記重算為 $\frac{-8+14i}{13}$；$q_1 = -1+i$ 不受影響。

⚠️ 講者整理 Bézout 係數時一度寫錯（寫成 $2w$、忘了分配 2），自己改正為 $-2z+(-1+2i)w$ [▶ 44:45](https://youtu.be/xjNSJ8G3dug?t=2685)。

【口頭】
- 一般整數的向量輾轉相除可以直接用向量形式做，但高斯整數時講者發現要先把除法想一遍，再寫向量形式。找適合你的記法 [▶ 43:02](https://youtu.be/xjNSJ8G3dug?t=2582)。
- 作業會有一題最後非零餘數**不是**單位的 [▶ 42:30](https://youtu.be/xjNSJ8G3dug?t=2550)。

---

## 9. 一頁速查表

**$\mathbb{Z}[i]$ 與範數**：$N(a+bi) = a^2+b^2 = z\bar z$，$N(zw) = N(z)N(w)$。
- 單位 $= \{\pm1,\pm i\}$。關鍵：$N(z)N(w) = 1$ ⇒ $a^2+b^2 = 1$。
- 每個數有 4 個相伴元。$1+i$ 的：$\pm(1+i)$、$\pm(1-i)$。

**除法演算法**：$q$ = 最接近 $a/b$ 的高斯整數（實虛部各差 $\le\frac12$），$N(r)\le\frac12N(b)$。

**整除**：$\alpha\mid\beta\Rightarrow N(\alpha)\mid N(\beta)$。

**高斯質數判準**
- $N(z)$ 是質數 ⇒ $z$、$\bar z$ 是高斯質數（$1\pm i$、$4\pm i$、$5\pm2i$）。
- 質數 $p$：高斯質數 $\iff p\notin S_2$。關鍵：$p^2 = N(\gamma_1)N(\gamma_2)$，$(p,p)$ 情況表示 $p\in S_2$。
- $2 = (1+i)(1-i)$ 不是；3 是（$a^2+b^2\neq3$）。

**$S_2$ 對乘法封閉**：$ab = N\big((a_1+ia_2)(b_1+ib_2)\big)$。$200 = 10^2+10^2 = 14^2+2^2$。
- $S_4$ = 全部自然數（Lagrange 1770）；$S_3$ 不封閉。

**算術**：唯一分解（差單位）；gcd（四個）；Bézout；$\pi\mid\alpha\beta\Rightarrow\pi\mid\alpha$ 或 $\pi\mid\beta$。
- $5+31i = (1+i)(4+i)(5+2i)$；$12 = (1+i)^2(1-i)^2\cdot3$。
- $\gcd(11+3i,2+3i) = i$：$-2z+(5-4i)w = i$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 高斯質數的完整分類 | 第 22 集（$p\equiv1\ (4)$ 分解、$p\equiv3\ (4)$ 不分解） |
| $S_2$ 的刻畫 | 第 22 集、課本 Theorem 10.3 |
| 四平方定理、四元數 | 第 23 集（四元數） |
| 唯一分解在 $\mathbb{Z}[i]$ 成立 | 第 24 集（Kummer：唯一分解在分圓整數中可能失敗） |

---

## 附：本集一句話總結

> **高斯整數 $\mathbb{Z}[i]$ 有乘法的範數 $N(a+bi)=a^2+b^2$、四個單位 $\pm1,\pm i$、除法演算法，所以也有 gcd、Bézout 和唯一分解（差單位）；範數讓「兩平方和的積還是兩平方和」變得一行就證完，而普通質數 $p$ 在 $\mathbb{Z}[i]$ 中仍是質數恰好當 $p$ 不是兩平方和（3 是，$2=(1+i)(1-i)$ 不是）。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 20 錄影逐字稿（YouTube 自動字幕，46:47）與 Jones & Jones《Elementary Number Theory》§10.1–10.3 整理。*
