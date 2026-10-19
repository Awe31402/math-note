---
course: Abstract Algebra II (Spring 2026)
episode: 20
lecture: L16
date: 2026-02-27
video: https://www.youtube.com/watch?v=NnwhqJ9vJw8
notes: 講義/AA2/Math422_Lecture16_FieldExtensions.pdf
---

# 第 20 集 · L16：擴張體基礎、Kronecker 定理 [▶ 影片](https://www.youtube.com/watch?v=NnwhqJ9vJw8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[19-複習-BossFight1]] ｜ [總目錄](../README.md) ｜ 下一集：[[21-L18-擴張體與分裂體]] →

## 本集概要

D&F §13.1，進入體論。主要動機：多項式在給定的體裡沒有根時，能不能造一個更大的體讓它有根？
- **特徵**再談；**質子體**（prime subfield）：$\mathbb{Q}$ 或 $\mathbb{F}_p$。
- **擴張體** $K/F$、**基礎體**；$K$ 是 $F$ 上的向量空間；**次數** $[K:F]$、**有限擴張**。
- 體同態不是零就是單射。
- **Kronecker 定理**：不可約 $p(x)$ 在 $K = F[x]/(p(x))$ 中有根 $\theta$；$1,\theta,\dots,\theta^{n-1}$ 是基底，$[K:F] = n$。
- **單擴張** $F(\alpha)$；$\mathbb{Q}(\sqrt[3]2)\cong\mathbb{Q}(\omega\sqrt[3]2)\cong\mathbb{Q}(\omega^2\sqrt[3]2)$——Galois 理論的核心。

> 📘 講義對應：Math422 Lecture 16「Field Extensions」；D&F §13.1（Thm 3、Thm 4）。

---

## 筆記

### 1. 特徵與質子體 [▶ 01:00](https://youtu.be/NnwhqJ9vJw8?t=60)

- $\operatorname{char}F = p$：使 $p\cdot1_F = 0$ 的最小正整數；體的特徵若非 0 必是**質數**（否則 $6\cdot1 = (2\cdot1)(3\cdot1) = 0$ 會產生零因子）。沒有這樣的 $p$ 就是特徵 0 [▶ 02:00](https://youtu.be/NnwhqJ9vJw8?t=120)。
- $m\cdot1+n\cdot1 = (m+n)\cdot1$、$(m\cdot1)(n\cdot1) = (mn)\cdot1$，所以 $\varphi(n) = n\cdot1_F$ 是環同態 $\mathbb{Z}\to F$。核是 0 或 $p\mathbb{Z}$，$\mathbb{Z}/\ker\varphi$ 嵌入 $F$ [▶ 04:00](https://youtu.be/NnwhqJ9vJw8?t=240)。再取分式體：特徵 0 得一份 $\mathbb{Q}$，特徵 $p$ 得一份 $\mathbb{Z}_p$。

> **定義**：$F$ 的**質子體**（prime subfield）是由 $1_F$ 生成的子體。它同構於 $\mathbb{Q}$ 或 $\mathbb{F}_p$（D&F 的記號，$= \mathbb{Z}/p\mathbb{Z}$）[▶ 07:00](https://youtu.be/NnwhqJ9vJw8?t=420)。

**例** [▶ 10:00](https://youtu.be/NnwhqJ9vJw8?t=600)
- $\mathbb{Q},\mathbb{R},\mathbb{C}$、有理函數體 $\mathbb{R}(x) = \{f/g\mid g\ne0\}$：質子體都是 $\mathbb{Q}$。（子體可以是整個體。）
- $\mathbb{Z}_p$；考試出過的 $\mathbb{Z}_2[x]/(x^2+x+1)$：質子體 $\mathbb{F}_2$。
- **特徵 $p$ 的無窮體**：$\mathbb{Z}_p(x)$，$\mathbb{Z}_p$ 上的有理函數。（老師一時懷疑它是否無窮——「在有限體上工作總讓我有點不自在，我比較習慣特徵 0。」它確實無窮：$1,x,x^2,\dots$ 互不相同。）

### 2. 擴張體與次數 [▶ 14:00](https://youtu.be/NnwhqJ9vJw8?t=840)

> **定義**：體 $K$ 包含子體 $F$，則 $K$ 是 $F$ 的**擴張體**，記 $K/F$，或畫成**體塔**（$K$ 在上、$F$ 在下）。$F$ 叫**基礎體**（base field）。

- $K$ 是 $F$ 上的**向量空間**：$F$ 中的純量乘 $K$ 中的向量還在 $K$ [▶ 15:30](https://youtu.be/NnwhqJ9vJw8?t=930)。

> **定義**：**次數** $[K:F] = \dim_FK$。有限的話叫**有限擴張**。

- $[\mathbb{C}:\mathbb{R}] = 2$（基底 $1,i$）[▶ 17:30](https://youtu.be/NnwhqJ9vJw8?t=1050)。
- $\mathbb{R}/\mathbb{Q}$ **不是**有限擴張：沒有有限個實數能用有理組合生出所有實數。任何體都是它質子體的擴張。

**體同態** [▶ 19:30](https://youtu.be/NnwhqJ9vJw8?t=1170)：體的理想只有 0 和全部（非零元素都是單位）。所以體同態 $\varphi:F\to F'$ 要嘛**恆為 0**，要嘛**單射**。「第 13 章一再用到；我忘記時要提醒我。」

### 3. Kronecker 定理 [▶ 22:00](https://youtu.be/NnwhqJ9vJw8?t=1320)

「也許是整門課我最喜歡的定理。」（D&F 不講歷史，但其他地方叫它 Kronecker 定理。）

> **定理**（D&F §13.1 Thm 3）：$F$ 是體，$p(x)\in F[x]$ 不可約（次數 $n$）。存在體 $K$，包含 $F$ 的同構副本，且 $p(x)$ 在 $K$ 中有根。把 $F$ 和它的副本視為同一，就得到 $F$ 的擴張，在其中 $p(x)$ 有根。

**證明** [▶ 26:00](https://youtu.be/NnwhqJ9vJw8?t=1560)：
1. $K = F[x]/(p(x))$。$p$ 不可約 ⇒ $(p(x))$ 極大 ⇒ $K$ 是體。（D&F 用圓括號，老師有時用角括號；老師不喜歡寫「$f(x)\bmod p(x)$」。）
2. **$F$ 的副本**：商映射 $\pi(f) = f+(p)$ 限制到常數多項式 $F$。$\pi(1) = 1+(p)\ne0$，不是零同態，所以單射。$\pi(F)\cong F$ [▶ 30:30](https://youtu.be/NnwhqJ9vJw8?t=1830)。
3. **根**：$\theta = x+(p(x))$（D&F 用 $\theta$）。$\theta^k = x^k+(p)$，所以
$$p(\theta) = a_n\theta^n+\cdots+a_1\theta+a_0 = p(x)+(p(x)) = (p(x)) = 0\ \text{在 }K\text{ 中}$$ [▶ 33:30](https://youtu.be/NnwhqJ9vJw8?t=2010)。

**$K$ 長什麼樣**（D&F Thm 4）[▶ 35:00](https://youtu.be/NnwhqJ9vJw8?t=2100)
- 任意 $a(x)+(p)$：除法算法 $a = p\,b+r$，$\deg r<n$，所以 $a(x)+(p) = r(x)+(p) = r_0+r_1\theta+\cdots+r_{n-1}\theta^{n-1}$ [▶ 37:30](https://youtu.be/NnwhqJ9vJw8?t=2250)。（「你的 b 看起來是降 b 調。」「那就寫尖一點。」）
- 所以 $1,\theta,\dots,\theta^{n-1}$ 張成 $K$。（$r$ 可能是 0，也可能某些係數為 0。）
- **線性獨立** [▶ 41:30](https://youtu.be/NnwhqJ9vJw8?t=2490)：若 $b_0+b_1\theta+\cdots+b_{n-1}\theta^{n-1} = 0$（$b_i$ 不全為 0），則 $b(x) = \sum b_ix^i$ 是次數 $\le n-1$ 的非零多項式，且 $b(x)+(p) = 0$，即 $b(x)\in(p(x))$。但 $n$ 次的 $p$ 不能整除次數更低的非零多項式，矛盾。
- 所以 $[K:F] = n$。知道基底，就能自然地在裡面計算。

### 4. 單擴張 [▶ 50:30](https://youtu.be/NnwhqJ9vJw8?t=3030)

> **定義**：$K$ 中，$F(\alpha,\beta,\dots)$ 是包含 $F$ 和 $\alpha,\beta,\dots$ 的**最小**子體（所有這種子體的交集仍是體）。$K = F(\alpha)$ 叫**單擴張**（simple extension）。

- 我們之前一直在用這記號，現在才給理由。
- $\mathbb{R}(\pi) = \mathbb{R}$（加進去的不必是新的）；$\mathbb{R}(i) = \mathbb{C}$ [▶ 52:30](https://youtu.be/NnwhqJ9vJw8?t=3150)。

### 5. 例：$x^3-2$ [▶ 47:30](https://youtu.be/NnwhqJ9vJw8?t=2850)

（學生提議 $x^2+1$、「$x^2+67$」——「玩得好」。）

$x^3-2$ 在 $\mathbb{Q}$ 上不可約（「在哪裡？」——學生：「$\mathbb{Q}$」，「很好！」）。在 $\mathbb{C}$ 上
$$x^3-2 = (x-\sqrt[3]2)(x-\omega\sqrt[3]2)(x-\omega^2\sqrt[3]2),\qquad\omega = e^{2\pi i/3} = \tfrac{-1+i\sqrt3}2.$$
$$\mathbb{Q}[x]/(x^3-2)\cong\mathbb{Q}(\theta),\quad\theta^3 = 2.$$
- $\mathbb{Q}(\sqrt[3]2)\cong\mathbb{Q}(\omega\sqrt[3]2)\cong\mathbb{Q}(\omega^2\sqrt[3]2)$ [▶ 54:00](https://youtu.be/NnwhqJ9vJw8?t=3240)。
- 第一個是 $\mathbb{R}$ 的子體，後兩個不是——作為集合**完全不同**，但都同構於 $\mathbb{Q}(\theta)$。
- **§13.1 的終極教訓**：不可約多項式的不同根，加進基礎體後得到同構的擴張——根之間有某種**對稱**。這就是 Galois 理論的核心 [▶ 55:30](https://youtu.be/NnwhqJ9vJw8?t=3330)。

> 💬 學生考完 Boss Fight 1 心情不好；老師：「我出考試是為了幫你學。考你已經會的東西就不有趣了。」[▶ 48:00](https://youtu.be/NnwhqJ9vJw8?t=2880)

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 質子體 | prime subfield | §1 |
| 有理函數體 | field of rational functions | §1 |
| 擴張體 | extension field | §2 |
| 基礎體 | base field | §2 |
| 體塔 | tower of fields | §2 |
| 次數（擴張的） | degree of an extension | §2 |
| 有限擴張 | finite extension | §2 |
| Kronecker 定理 | Kronecker's theorem | §3 |
| 單擴張 | simple extension | §4 |

## ⚠️ 待確認清單

（本集無）
