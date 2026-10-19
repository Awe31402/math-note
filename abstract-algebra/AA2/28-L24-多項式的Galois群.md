---
course: Abstract Algebra II (Spring 2026)
episode: 28
lecture: L24
date: 2026-03-27
video: https://www.youtube.com/watch?v=RrHAN9FtXHI
notes: 講義/AA2/Math422_Lecture24_GaloisGroupPolynomials.pdf
---

# 第 28 集 · L24：多項式的 Galois 群、一般多項式 [▶ 影片](https://www.youtube.com/watch?v=RrHAN9FtXHI&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[27-L23-Galois理論例子-上]] ｜ [總目錄](../README.md) ｜ 下一集：[[29-L25-Galois理論結語]] →

## 本集概要

- （D&F 沒有的）**Galois 反元素公式**：所有 Galois 共軛的乘積在基礎體裡；$z^{-1}$ = 非平凡共軛之積 ÷ 全部之積。$\mathbb{C}/\mathbb{R}$ 時就是 $\bar z/(z\bar z)$。
- Galois 群置換根 ⇒ 是 $S_n$ 的子群，$|G|\le n!$。$\mathbb{Q}(\sqrt2,\sqrt3)$：$V_4\le S_4$；$x^3-2$：剛好是 $S_3$。
- 有理化 $\dfrac1{1+3\sqrt2+4\sqrt3}$。
- **初等對稱函數**、**一般多項式**；係數 = $\pm$ 對稱函數。
- $F(x_1,\dots,x_n)/F(s_1,\dots,s_n)$ 是 Galois，群是 $S_n$；對稱有理函數是 $s_i$ 的有理函數。
- D&F Thm 32：**一般 $n$ 次多項式的 Galois 群是 $S_n$**——「一般的多項式」根之間沒有特殊關係。

> 📘 講義對應：Math422 Lecture 24「Galois Group of Polynomials」；D&F §14.6（Prop. 30、Cor. 31、Thm 32）。

---

## 筆記

### 1. Galois 反元素公式 [▶ 00:30](https://youtu.be/RrHAN9FtXHI?t=30)

（「這次有 D&F 沒有的東西。」）

設定：$f\in F[x]$ 可分、不可約，$E$ 是它的分裂體，根 $\alpha_1,\dots,\alpha_n$。$E/F$ 是 Galois，設 $[E:F] = p = |G|$，$G = \{\sigma_1 = 1,\sigma_2,\dots,\sigma_p\}$。

> **命題**：$z\in E$，則 $\displaystyle\prod_{i=1}^p\sigma_i(z)\in F$。$z\ne0$ 時
> $$z^{-1} = \frac{\prod_{i=2}^p\sigma_i(z)}{\prod_{i=1}^p\sigma_i(z)}.$$

- 可能是 D&F 的習題；是老師的弟弟建議的（上次那份「可怕計算」的 PDF 內容）[▶ 04:30](https://youtu.be/RrHAN9FtXHI?t=270)。
- **證明**：任取 $\tau\in G$。$\tau\prod\sigma_i(z) = \prod(\tau\sigma_i)(z)$。$\tau\sigma_1,\dots,\tau\sigma_p$ 仍是 $G$ 的全部元素（只是重排），乘法交換，所以乘積不變 [▶ 06:30](https://youtu.be/RrHAN9FtXHI?t=390)。被 $G$ 所有元素固定 ⇒ 在固定體 $F$ 裡。第二式直接移項（「別告訴 Spano」）。

**例 1**：$x^2+1$ 在 $\mathbb{R}$ 上，分裂體 $\mathbb{C}$，次數 2，$G = \{1,\sigma\}$，$\sigma$ = **複數共軛**。公式變成 $\dfrac1z = \dfrac{\bar z}{z\bar z}$——我們熟悉的複數反元素公式就是 Galois 反元素公式的特例 [▶ 09:00](https://youtu.be/RrHAN9FtXHI?t=540)。

### 2. Galois 群是 $S_n$ 的子群 [▶ 11:00](https://youtu.be/RrHAN9FtXHI?t=660)

$\sigma\in G$ 把根送到根，把根編號 $1,\dots,n$，就得到 $G\le S_n$。所以 $[E:F] = |G|\le n!$ [▶ 13:00](https://youtu.be/RrHAN9FtXHI?t=780)。

**例 2**：$(x^2-2)(x^2-3)$，根 $\alpha_1 = \sqrt2,\alpha_2 = -\sqrt2,\alpha_3 = \sqrt3,\alpha_4 = -\sqrt3$ [▶ 14:30](https://youtu.be/RrHAN9FtXHI?t=870)。
- $\sigma = (1\,2)$、$\tau = (3\,4)$、$\sigma\tau = (1\,2)(3\,4)$。$G\cong V_4\le S_4$。
- 「同一個例子做夠多次，終究會懂——D&F 也是這樣。」

**有理化**（「如果你有不受控的青少年需要消耗時間」）[▶ 17:30](https://youtu.be/RrHAN9FtXHI?t=1050)：
$$\frac1{1+3\sqrt2+4\sqrt3} = \frac{(1-3\sqrt2+4\sqrt3)(1+3\sqrt2-4\sqrt3)(1-3\sqrt2-4\sqrt3)}{\prod\text{全部 4 個共軛}} = \frac{-65-93\sqrt2+116\sqrt3+24\sqrt6}{769}.$$
- 三個非平凡共軛分別來自 $\sigma,\tau,\sigma\tau$。題目任何高中生都看得懂，但要用這套代數才知道為什麼能做。

**例 3**：$x^3-2$，根 $\alpha_1 = \sqrt[3]2$、$\alpha_2 = \rho\sqrt[3]2$、$\alpha_3 = \rho^2\sqrt[3]2$ [▶ 21:00](https://youtu.be/RrHAN9FtXHI?t=1260)。
- $\sigma = (1\,2\,3)$；$\tau = (2\,3)$——$\tau$ 就是**複數共軛**（「所以你們下學期要修複分析」——老師想看名單，但新系統在開課前看不到）。
- $\sigma^2 = (1\,3\,2)$、$\tau\sigma = (1\,3)$、$\tau\sigma^2 = (1\,2)$。$G$ **就是** $S_3$（$F = \mathbb{Q}$）[▶ 24:00](https://youtu.be/RrHAN9FtXHI?t=1440)。

### 3. 一般多項式 [▶ 25:00](https://youtu.be/RrHAN9FtXHI?t=1500)

一言以蔽之：**一般的多項式，Galois 群就是完整的 $S_n$**。例 3 才是典型；例 2 的根之間有特殊關係（互為相反數），所以只有 4 個元素而不是 24 個 [▶ 26:00](https://youtu.be/RrHAN9FtXHI?t=1560)。

> **定義**：不定元 $x_1,\dots,x_n$ 的**初等對稱函數**：
> $$s_1 = x_1+\cdots+x_n,\quad s_2 = \sum_{i<j}x_ix_j,\quad\dots,\quad s_n = x_1x_2\cdots x_n.$$
> $s_i$ = 所有 $i$ 個**相異**不定元乘積的和（不能重複，如 $x_1^2$ 不行）[▶ 27:00](https://youtu.be/RrHAN9FtXHI?t=1620)。

- 不定元彼此**交換**（$x_1x_2 = x_2x_1$）；具體構造時要把交換性放進去。非交換的不定元比較可怕 [▶ 30:00](https://youtu.be/RrHAN9FtXHI?t=1800)。

> **定義**：$n$ 次**一般多項式**是 $(x-x_1)(x-x_2)\cdots(x-x_n)$，根就是不定元。
> **斷言**：$(x-x_1)\cdots(x-x_n) = x^n-s_1x^{n-1}+s_2x^{n-2}-\cdots+(-1)^ns_n$ [▶ 31:30](https://youtu.be/RrHAN9FtXHI?t=1890)。

- 證明用歸納，不做（「別擔心」）；看小例子：
  - $n = 2$：$x^2-(x_1+x_2)x+x_1x_2$。
  - $n = 3$：$x^3-(x_1+x_2+x_3)x^2+(x_1x_2+x_1x_3+x_2x_3)x-x_1x_2x_3$。
- 「班上有工程雙主修——驗證到 3 就是工程師的證明。」[▶ 35:00](https://youtu.be/RrHAN9FtXHI?t=2100)
- 難點：$s_i$ 依賴 $n$（$n = 2$ 和 $n = 3$ 的 $s_1$ 不同），記號很麻煩，D&F 明智地省略了。

> 💬 學生提到「蜘蛛驚嚇」支線任務已完成、要為 Guthrie 老師烤東西；老師：「那就像替愛因斯坦做物理。」[▶ 36:30](https://youtu.be/RrHAN9FtXHI?t=2190)

### 4. 對稱函數的體 [▶ 37:30](https://youtu.be/RrHAN9FtXHI?t=2250)

令 $E = F(x_1,\dots,x_n)$（有理函數體）。
- $E$ 是 $(x-x_1)\cdots(x-x_n)$ 在 $F(s_1,\dots,s_n)$ 上的分裂體 ⇒ **Galois**。$F(s_1,\dots,s_n)\subseteq E$ 顯然；不一定相等——只拿到不定元的特定組合 [▶ 40:00](https://youtu.be/RrHAN9FtXHI?t=2400)。
- $\sigma\in S_n$ 誘導自同構 $x_i\mapsto x_{\sigma(i)}$，所以 $S_n\le\mathrm{Aut}(E)$ [▶ 41:00](https://youtu.be/RrHAN9FtXHI?t=2460)。
- 對稱函數被任何下標置換固定 ⇒ $F(s_1,\dots,s_n)\subseteq E^{S_n}$。
- 次數：$[E:E^{S_n}] = n!$，而 $[E:F(s_1,\dots,s_n)]\le n!$（分裂體）。所以兩者相等（學生 Shane 幫忙補上不等式；「這堂課的時間讓我腦袋……8:15 會更糟」——「你修過我 8:15 的課還一直抱怨」）[▶ 45:00](https://youtu.be/RrHAN9FtXHI?t=2700)。

> **命題 30**：$S_n$ 作用在 $F(x_1,\dots,x_n)$ 上的固定體是 $F(s_1,\dots,s_n)$。

> **定義**：有理函數 $f(x_1,\dots,x_n)$ 是**對稱的**，若 $f(x_{\sigma(1)},\dots,x_{\sigma(n)}) = f(x_1,\dots,x_n)$ 對所有 $\sigma\in S_n$（學生先答成反對稱）[▶ 48:00](https://youtu.be/RrHAN9FtXHI?t=2880)。

> **推論 31**：任何對稱（有理）函數都是 $s_1,\dots,s_n$ 的有理函數。

- 老師強調必須是**有理**函數：$\sin(x_1+\cdots+x_n)$ 對稱，但不是 $s_i$ 的有理函數 [▶ 50:30](https://youtu.be/RrHAN9FtXHI?t=3030)。證明：對稱函數在 $S_n$ 的固定體裡。
- 例：$(x_1-x_2)^2 = (x_1+x_2)^2-4x_1x_2 = s_1^2-4s_2$（先展開是壞的一步，應該讓 $s_1$ 出現）[▶ 52:00](https://youtu.be/RrHAN9FtXHI?t=3120)。
- 例：$x_1^2+x_2^2+x_3^2 = (x_1+x_2+x_3)^2-2(x_1x_2+x_1x_3+x_2x_3) = s_1^2-2s_2$。

> **定理 32**（D&F）：一般多項式 $x^n-s_1x^{n-1}+\cdots+(-1)^ns_n$ 在 $F(s_1,\dots,s_n)$ 上可分，Galois 群是 $S_n$ [▶ 54:30](https://youtu.be/RrHAN9FtXHI?t=3270)。

- 意思：係數之間沒有關係（$s_i$ 是不定元）時，Galois 群是完整的對稱群。書上還有一段補完論證被略過。

**預告** [▶ 56:00](https://youtu.be/RrHAN9FtXHI?t=3360)：回到當初的動機——五次方程能否用根式解。**根式擴張**連到之前定義的**可解群**，說明五次以上一般沒有類似二次公式的公式。「這是最後一堂 Galois 理論。」

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| Galois 反元素公式 | Galois inverse formula（課堂用語） | §1 |
| 複數共軛 | complex conjugation | §1 |
| 初等對稱函數 | elementary symmetric functions | §3 |
| 一般多項式 | general polynomial | §3 |
| 對稱函數 | symmetric function | §4 |
| 根式擴張 | radical extension | §4 |

## ⚠️ 待確認清單

（本集無）
