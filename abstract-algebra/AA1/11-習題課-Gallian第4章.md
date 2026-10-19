---
course: Abstract Algebra I (Fall 2016)
episode: 11
lecture: 習題課
date: 2016-09-13
video: https://www.youtube.com/watch?v=mUv_cTprS9c
notes: 無直接對應（Gallian 第 4 章習題）
---

# 第 11 集 · 習題課：Gallian 第 4 章 [▶ 影片](https://www.youtube.com/watch?v=mUv_cTprS9c&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[10-L7-循環群-下]] ｜ [總目錄](../README.md) ｜ 下一集：[[12-L8-置換與循環記號]] →

## 本集概要

- **無限階元素**：$\langle a^3\rangle$ 的生成元只有 $a^3$ 和 $a^{-3}$（類比 $3\mathbb{Z}$ 只有 $\pm3$）。
- **恰有三個子群的循環群**：$\{e\}$、$G$、一個 7 階子群，則 $|G| = 49$。注意題目「恰好三個」要理解成「三個**不同**的」。
- **$D_n$ 中 $d$ 階元素**（$d\neq 2$）恰有 $\varphi(d)$ 個；**2 階元素**：$n$ 奇數時 $n$ 個，偶數時 $n+1$ 個。用歸納法證明每個「旋轉 × 鏡射」都是 2 階。
- 循環子群無所不在：任何群裡 $\langle g\rangle$ 都是循環子群，例如 $GL(2,\mathbb{R})$ 和 $(M_{2\times2}(\mathbb{R}),+)$ 裡。

> ⚠️ 題號說明：課堂用的是 Gallian **第 5 版**。下面附上第 10 版對應的題號（找得到的話）。

---

## 筆記

### 題 1：$|a| = \infty$ 時 $\langle a^3\rangle$ 的所有生成元（Ch.4 #12）[▶ 00:30](https://youtu.be/mUv_cTprS9c?t=30)

（第 10 版也是 Ch.4 #12，p.89；前半問 $\mathbb{Z}$ 中 $\langle 3\rangle$ 的生成元。）

**先想整數版** [▶ 03:00](https://youtu.be/mUv_cTprS9c?t=180)：在 $(\mathbb{Z},+)$ 裡，$a$ 對應 $1$，$\langle a^3\rangle$ 對應 $3\mathbb{Z} = \{\dots,-6,-3,0,3,6,\dots\}$。
- $3$ 是生成元，$-3$ 也是（學生答出）[▶ 04:30](https://youtu.be/mUv_cTprS9c?t=270)。
- $6$ 不是：$6\mathbb{Z} = \{\dots,-12,-6,0,6,12,\dots\}\neq 3\mathbb{Z}$ [▶ 05:00](https://youtu.be/mUv_cTprS9c?t=300)。

**注意**：循環群**可以**是無限的，例如 $(\mathbb{Z},+)$ [▶ 02:30](https://youtu.be/mUv_cTprS9c?t=150)。上一講的定理大多是講**有限**循環群，這題只能自己想 [▶ 05:30](https://youtu.be/mUv_cTprS9c?t=330)。

**$a^{-3}$ 是生成元** [▶ 06:30](https://youtu.be/mUv_cTprS9c?t=390)：$\langle a^{-3}\rangle = \{(a^{-3})^k\} = \{a^{-3k}\}$，只是把 $k$ 換成 $-k$ 重新編號，和 $\langle a^3\rangle$ 是同一個集合。

**沒有別的生成元（反證法）** [▶ 07:30](https://youtu.be/mUv_cTprS9c?t=450)
- 任何 $\langle a^3\rangle$ 的元素都是 $a^{3l}$。$l = 0$ 給單位元素，只生成 $\{e\}$，不行。
- 設 $|l|>1$ 且 $\langle a^{3l}\rangle = \langle a^3\rangle$。$\langle a^{3l}\rangle = \{a^{3lj}\mid j\in\mathbb{Z}\}$。
- 要讓 $a^3$ 在裡面，需要 $a^3 = a^{3lj}$。因為 $|a| = \infty$，不同次方是不同元素，所以 $3 = 3lj$，也就是 $lj = 1$ [▶ 09:30](https://youtu.be/mUv_cTprS9c?t=570)。
- $|l|>1$ 時沒有整數 $j$ 滿足（例如 $l = 2$ 要 $j = 1/2$）[▶ 11:00](https://youtu.be/mUv_cTprS9c?t=660)。所以 $a^3\notin\langle a^{3l}\rangle$，矛盾。

**答案**：$\langle a^3\rangle$ 的生成元只有 $a^3$ 和 $a^{-3}$。$\blacksquare$

> 💬 老師說：反證法得到的矛盾通常是旁邊某個怪東西，這次矛盾的「正好就是要證的事」，很難得 [▶ 10:30](https://youtu.be/mUv_cTprS9c?t=630)。

### 題 2：恰有三個子群的循環群（Ch.4 #14）[▶ 11:00](https://youtu.be/mUv_cTprS9c?t=660)

（第 10 版也是 Ch.4 #14，p.89。）

> **題目**　循環群 $G$ 恰有三個子群：$G$ 本身、$\{e\}$、一個 7 階子群。$|G|$ 是多少？

**第一次嘗試** [▶ 13:00](https://youtu.be/mUv_cTprS9c?t=780)
- 由循環群基本定理，$7\mid |G|$，所以 $|G| = 7k$。
- 若 $k>1$，$k$ 也是 $|G|$ 的因數，就會有一個 $k$ 階子群 [▶ 14:30](https://youtu.be/mUv_cTprS9c?t=870)。
- 老師一開始得出 $|G| = 7$。

**學生質疑** [▶ 16:30](https://youtu.be/mUv_cTprS9c?t=990)：如果 $|G| = 7$，那「7 階子群」就是 $G$ 本身，三個子群其實只有兩個。

**修正：三個子群要互不相同** [▶ 17:30](https://youtu.be/mUv_cTprS9c?t=1050)
- $|G| = 7k$，$k>1$。$k$ 階子群必須就是那三個之一。
- 唯一不會多出新子群的辦法是 $k = 7$，所以 $|G| = 49$ [▶ 18:30](https://youtu.be/mUv_cTprS9c?t=1110)。
- 49 的正因數只有 $1,7,49$，正好對應三個子群：$\{e\}$、$\langle a^7\rangle$、$\langle a\rangle$（$a^{49} = e$）。
- 換成 $\mathbb{Z}_{49}$ 更好看：7 階子群是 $\langle 7\rangle = \{0,7,14,21,28,35,42\}$ [▶ 20:30](https://youtu.be/mUv_cTprS9c?t=1230)。

**答案**：$|G| = 49$。（第 10 版還問：7 換成質數 $p$ 呢？同理 $|G| = p^2$。）

**白話**：只要 $k$ 不是 7，就會多出一個不是 7 階的子群，和題目矛盾 [▶ 21:00](https://youtu.be/mUv_cTprS9c?t=1260)。

> 💬 老師：如果作業題目有這種歧義，請寄信問他 [▶ 22:00](https://youtu.be/mUv_cTprS9c?t=1320)。Gallian 說「exactly three subgroups」而且一個一個列出來，應該是指三個不同的。

### 題 3：$D_n$ 中 $d$ 階元素的個數（Ch.4 #25）[▶ 23:00](https://youtu.be/mUv_cTprS9c?t=1380)

（第 10 版為 Ch.4 #33，p.91。這題不是指定作業，只是推薦題；老師不想在習題課上做指定作業題。）

> **題目**　$d$ 是正整數，$d\neq 2$，$d\mid n$。證明 $D_n$ 中 $d$ 階元素恰有 $\varphi(d)$ 個。$D_n$ 有幾個 2 階元素？

**用作業的記號** [▶ 29:30](https://youtu.be/mUv_cTprS9c?t=1770)：$x$ 是旋轉、$y$ 是鏡射，
$$x^n = 1,\quad y^2 = 1,\quad (xy)^2 = 1.$$
（就是課堂的 $R$、$f$。）以 $D_5$ 為例：$\{1,x,x^2,x^3,x^4,\ y,xy,x^2y,x^3y,x^4y\}$。

#### 2 階元素有哪些？

**旋轉裡的 2 階元素** [▶ 27:30](https://youtu.be/mUv_cTprS9c?t=1650)
- $n$ **偶數**：$x^{n/2}$ 是轉 $180°$，$(x^{n/2})^2 = x^n = 1$，所以是 2 階。例如 $D_4$ 的 $R^2$。
- $n$ **奇數**：$n/2$ 不是整數，旋轉裡沒有 2 階元素 [▶ 30:00](https://youtu.be/mUv_cTprS9c?t=1800)。

**「旋轉 × 鏡射」都是 2 階** [▶ 32:30](https://youtu.be/mUv_cTprS9c?t=1950)

先試 $x^2y$：由 $(xy)^2 = 1$，得 $xy = (xy)^{-1} = y^{-1}x^{-1} = yx^{-1}$（**襪子鞋子 (socks-shoes)** 規則，且 $y^{-1} = y$）。用它算出 $(x^2y)^2 = 1$ [▶ 35:00](https://youtu.be/mUv_cTprS9c?t=2100)。

幾何直覺（學生說的）：轉、轉、翻，再轉、轉、翻，就回到原位 [▶ 35:30](https://youtu.be/mUv_cTprS9c?t=2130)。

**歸納法證明**（學生提議）[▶ 40:00](https://youtu.be/mUv_cTprS9c?t=2400)
- **主張**：$(x^ky)^2 = 1$ 對所有 $k\in\mathbb{N}$。
- **$k=1$**：就是關係式 $(xy)^2 = 1$ [▶ 40:30](https://youtu.be/mUv_cTprS9c?t=2430)。
- **歸納步驟** [▶ 42:00](https://youtu.be/mUv_cTprS9c?t=2520)：設 $(x^ky)^2 = 1$。用 $xy = yx^{-1}$：
$$(x^{k+1}y)^2 = x^k(xy)x^{k+1}y = x^k(yx^{-1})x^{k+1}y = x^ky\,x^ky = (x^ky)^2 = 1.$$

> 💬 更短的寫法：由 $yxy = x^{-1}$ 得 $yx^ky = x^{-k}$，所以 $(x^ky)^2 = x^k(yx^ky) = x^kx^{-k} = 1$。

老師說：先多算幾個，產生「相信它是對的」的種子，才有勇氣試歸納法 [▶ 44:00](https://youtu.be/mUv_cTprS9c?t=2640)。

**2 階元素個數** [▶ 44:30](https://youtu.be/mUv_cTprS9c?t=2670)
- $n$ 奇數：$n$ 個（所有 $x^ky$）。
- $n$ 偶數：$n+1$ 個（所有 $x^ky$，加上 $x^{n/2}$）。
- 順帶一提：$|D_n| = 2n$，所以**沒有奇數階的二面體群** [▶ 45:00](https://youtu.be/mUv_cTprS9c?t=2700)。

#### $d\neq 2$ 的情形 [▶ 46:00](https://youtu.be/mUv_cTprS9c?t=2760)

- 所有 $x^ky$（「旋轉 × 鏡射」）都是 2 階，所以 $d\neq 2$ 的元素**只能在旋轉裡**。
- 旋轉子群 $\{1,x,\dots,x^{n-1}\} = \langle x\rangle$ 是 $n$ 階**循環群** [▶ 48:30](https://youtu.be/mUv_cTprS9c?t=2910)。
- 上一講證過：$n$ 階循環群中 $d$ 階元素恰有 $\varphi(d)$ 個（$d\mid n$）。
- 所以 $D_n$ 中 $d$ 階元素恰有 $\varphi(d)$ 個。$\blacksquare$

**$D_n$ 不是循環群** [▶ 49:30](https://youtu.be/mUv_cTprS9c?t=2970)：它有不只一個 2 階元素。循環群最多只有一個 2 階元素，否則會有兩個不同的 2 階子群，違反循環群基本定理。但 $D_n$ **裡面**有循環子群，而且循環子群必須遵守循環群的規則。

### 補充：循環子群無所不在 [▶ 50:00](https://youtu.be/mUv_cTprS9c?t=3000)

任何群的任何元素 $g$ 都生成循環子群 $\langle g\rangle$（L3 證過）。
- $GL(2,\mathbb{R})$：例如 $\left\langle\begin{pmatrix}1&2\\3&4\end{pmatrix}\right\rangle$，就是這個矩陣和它反矩陣的所有次方 [▶ 51:00](https://youtu.be/mUv_cTprS9c?t=3060)。
- $(M_{2\times2}(\mathbb{R}),+)$（所有 $2\times2$ 實矩陣，加法）：$\left\langle\begin{pmatrix}a&b\\c&d\end{pmatrix}\right\rangle = \left\{n\begin{pmatrix}a&b\\c&d\end{pmatrix}\mid n\in\mathbb{Z}\right\}$，是無限循環子群 [▶ 53:00](https://youtu.be/mUv_cTprS9c?t=3180)。

**來自未來的評論** [▶ 53:30](https://youtu.be/mUv_cTprS9c?t=3210)：之後會學到，這些無限循環群其實「就是」整數，只是寫法很笨。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 無限循環群 | infinite cyclic group | [02:30](https://youtu.be/mUv_cTprS9c?t=150) |
| 重新編號 | reindexing | [06:30](https://youtu.be/mUv_cTprS9c?t=390) |
| 生成元與關係 | generators and relations | [30:30](https://youtu.be/mUv_cTprS9c?t=1830) |
| 襪子鞋子規則 | socks-shoes (property) | [33:30](https://youtu.be/mUv_cTprS9c?t=2010) |
| 數學歸納法 | mathematical induction | [38:00](https://youtu.be/mUv_cTprS9c?t=2280) |

## ⚠️ 待確認清單

（本集無）
