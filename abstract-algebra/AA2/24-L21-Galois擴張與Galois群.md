---
course: Abstract Algebra II (Spring 2026)
episode: 24
lecture: L21
date: 2026-03-11
video: https://www.youtube.com/watch?v=wtedDsycOZ8
notes: 講義/AA2/Math422_Lecture21_GaloisBeginnings.pdf
---

# 第 24 集 · L21：Galois 擴張與 Galois 群的基本定義 [▶ 影片](https://www.youtube.com/watch?v=wtedDsycOZ8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[23-L20-分圓體與Galois理論開始]] ｜ [總目錄](../README.md) ｜ 下一集：[[25-L22-Galois理論基本定理]] →

## 本集概要

D&F §14.1：
- $\mathrm{Aut}(K/F)$：固定 $F$ 的自同構，是子群。
- **自同構把根送到根**（同一個最小多項式的根）——「Galois 理論從這裡開始」。
- 例：$\mathrm{Aut}(\mathbb{Q}(\sqrt2)/\mathbb{Q})\cong\mathbb{Z}_2$；$\mathrm{Aut}(\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}) = 1$。
- **固定體** $K^H$；包含關係**反轉**。
- $|\mathrm{Aut}(E/F)|\le[E:F]$；**Galois 擴張**、**Galois 群** $\mathrm{Gal}(K/F)$；可分多項式的分裂體是 Galois 的。
- $\mathrm{Gal}(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q})\cong V_4$，以及各子群的固定體。

> 📘 講義對應：Math422 Lecture 21「Galois Beginnings」；D&F §14.1（Prop. 1–5、Cor. 6；p.561–562）。

---

## 筆記

### 1. 固定 $F$ 的自同構 [▶ 00:30](https://youtu.be/wtedDsycOZ8?t=30)

> **定義**：體 $K$ 到自己的同構叫**自同構**，全體記 $\mathrm{Aut}(K)$。$\sigma$ **固定** $x$，若 $\sigma x = x$。若 $\sigma$ 固定子體 $F$ 的每個元素，記 $\sigma\in\mathrm{Aut}(K/F)$——$K$ 的 **$F$-固定自同構**。

> **命題 1**：$\mathrm{Aut}(K/F)$ 是 $\mathrm{Aut}(K)$ 的子群 [▶ 02:30](https://youtu.be/wtedDsycOZ8?t=150)。

- $\mathrm{Aut}(K)$ 是群（同構的合成、反函數還是同構）。
- $\sigma,\tau\in\mathrm{Aut}(K/F)$、$x\in F$：$\sigma\tau x = \sigma x = x$；$x = \sigma^{-1}\sigma x = \sigma^{-1}x$；恆等映射固定一切，所以非空（學生提醒要證非空）。
- （「你們開心我就開心——這絕對是謊話。」老師說他信奉「對抗式教學法」。）

### 2. 自同構置換根 [▶ 06:30](https://youtu.be/wtedDsycOZ8?t=390)

> **命題 2**：$K/F$，$\alpha\in K$ 在 $F$ 上代數。對任意 $\sigma\in\mathrm{Aut}(K/F)$，$\sigma\alpha$ 也是 $m_{\alpha,F}$ 的根。等價地：$F[x]$ 中以 $\alpha$ 為根的多項式，也以 $\sigma\alpha$ 為根。

- 「$F$-固定自同構在**置換不可約多項式的根**。我覺得 Galois 理論是從這個命題開始的。」

**證明** [▶ 08:00](https://youtu.be/wtedDsycOZ8?t=480)：$\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0 = 0$，$a_j\in F$。兩邊作用 $\sigma$（「自己算，不要只抄」）：可加、可乘、$\sigma0 = 0$、$\sigma a_j = a_j$，
$$\sigma(a_j\alpha^j) = \sigma(a_j)\sigma(\alpha)^j = a_j(\sigma\alpha)^j,$$
所以 $(\sigma\alpha)^n+a_{n-1}(\sigma\alpha)^{n-1}+\cdots+a_0 = 0$。

### 3. 兩個例子 [▶ 13:30](https://youtu.be/wtedDsycOZ8?t=810)

（學生在畫「很棒的藝術」；老師女兒今天也在他手臂上畫畫。）

- 備註：特徵 0 的體的自同構**自動固定質子體 $\mathbb{Q}$**（$1\mapsto1$ 推下去），所以 $\mathrm{Aut}(K/\mathbb{Q}) = \mathrm{Aut}(K)$ [▶ 14:00](https://youtu.be/wtedDsycOZ8?t=840)。

**例 1：$K = \mathbb{Q}(\sqrt2)$**：自同構由 $\sqrt2$ 的去向決定，必須送到 $x^2-2$ 的根 $\pm\sqrt2$ [▶ 15:30](https://youtu.be/wtedDsycOZ8?t=930)：
- $1(a+b\sqrt2) = a+b\sqrt2$；$\sigma(a+b\sqrt2) = a-b\sqrt2$（像複數共軛，但不是）。
- $\sigma^2 = 1$。$\mathrm{Aut}(K/\mathbb{Q}) = \{1,\sigma\}\cong\mathbb{Z}_2$。

**例 2：$K = \mathbb{Q}(\sqrt[3]2)$**（3 次，Eisenstein）[▶ 17:30](https://youtu.be/wtedDsycOZ8?t=1050)：元素 $a+b\sqrt[3]2+c\sqrt[3]4$。$\tau$ 必須把 $\sqrt[3]2$ 送到 $x^3-2$ 的根：$\sqrt[3]2,\zeta_3\sqrt[3]2,\zeta_3^2\sqrt[3]2$。後兩個「就像那匹馬一樣不是真的（not real）」——老師引用幾年前飛機上大喊「那匹馬不是真的」的新聞（學生：「是 Violet 的媽媽嗎？」）。$K\subseteq\mathbb{R}$，所以只能送到 $\sqrt[3]2$：**只有恆等**。$\mathrm{Aut}(K/\mathbb{Q}) = 1$ [▶ 21:00](https://youtu.be/wtedDsycOZ8?t=1260)。

### 4. 固定體 [▶ 21:30](https://youtu.be/wtedDsycOZ8?t=1290)

- $K/F$ 有限 ⇒ $\mathrm{Aut}(K/F)$ 有限。擴張 ↦ 群；反方向，子群 ↦ **固定子體**。
- 老師用一個 D&F（至少目前）沒有的記號 $K^H$：「我以前教這段發現書上少了一個記號，有了它比較好掛概念。」

> **命題 3**：$H\le\mathrm{Aut}(K)$。被 $H$ 所有元素固定的 $K$ 中元素構成子體，記 $K^H$，叫 $H$ 的**固定體**（fixed field）[▶ 23:00](https://youtu.be/wtedDsycOZ8?t=1380)。

- 學生：「這比較像定義。」——「被你抓到，我在命題裡做定義。但要證它是體。」
- 證明（填空）：$h\in H$，$a,b\in K^H$：$h(a\pm b) = a\pm b$、$h(ab) = ab$、$h(a^{-1}) = a^{-1}$。（學生在填空處寫「軟軟的」。）[▶ 25:00](https://youtu.be/wtedDsycOZ8?t=1500)
- **陷阱題**：哪裡用到 $H$ 是子群？——沒用到，對任意子集都成立 [▶ 29:00](https://youtu.be/wtedDsycOZ8?t=1740)。

> **命題 4**（包含關係反轉，「有點令人驚訝，Galois 理論難的原因之一」）[▶ 29:30](https://youtu.be/wtedDsycOZ8?t=1770)：
> 1. $F_1\subseteq F_2\subseteq K$ ⇒ $\mathrm{Aut}(K/F_2)\le\mathrm{Aut}(K/F_1)$。
> 2. $H_1\le H_2\le\mathrm{Aut}(K)$ ⇒ $K^{H_2}\subseteq K^{H_1}$。

- (1)：$\sigma$ 固定 $F_2$，而 $F_1\subseteq F_2$，所以也固定 $F_1$。已知兩者都是群，只要證包含 [▶ 33:00](https://youtu.be/wtedDsycOZ8?t=1980)。
- (2)：$a\in K^{H_2}$，$\tau\in H_1\subseteq H_2$，所以 $\tau a = a$，$a\in K^{H_1}$。
- 記號：子群用 $\le$，子體就用 $\subseteq$（跟 D&F）。
- （老師期待 Spano 博士教 Jacob 抽象代數一：「一定很好笑。」）

### 5. Galois 擴張 [▶ 38:30](https://youtu.be/wtedDsycOZ8?t=2310)

> **命題 5**：$E$ 是 $f(x)\in F[x]$ 在 $F$ 上的分裂體。則 $|\mathrm{Aut}(E/F)|\le[E:F]$，$f$ 可分時取等號。

- 證明在 D&F p.561–562，「下次也許」。其實對任何有限擴張都有 $|\mathrm{Aut}(K/F)|\le[K:F]$；分裂體的情況特別有意思 [▶ 40:00](https://youtu.be/wtedDsycOZ8?t=2400)。

> **定義**：有限擴張 $K/F$ 是 **Galois 擴張**，若 $|\mathrm{Aut}(K/F)| = [K:F]$。此時 $\mathrm{Aut}(K/F)$ 記作 $\mathrm{Gal}(K/F)$，**Galois 群**。
> 若 $f$ 在 $F$ 上可分，$f$ 的 Galois 群就是它的分裂體的 Galois 群 [▶ 41:00](https://youtu.be/wtedDsycOZ8?t=2460)。

> **推論 6**：$K$ 是可分多項式 $f\in F[x]$ 在 $F$ 上的分裂體，則 $K/F$ 是 Galois 的。粗略說：**分裂體是 Galois 的** [▶ 43:00](https://youtu.be/wtedDsycOZ8?t=2580)。

- （「要把 67 加進來嗎？」——「她的電池剩 67%。」「我准了。」）
- 例 1 是 Galois：$x^2-2$ 的分裂體，$2 = 2$。例 2 不是：$[\mathbb{Q}(\sqrt[3]2):\mathbb{Q}] = 3\ne1$ [▶ 45:30](https://youtu.be/wtedDsycOZ8?t=2730)。

### 6. 例 3：$\mathbb{Q}(\sqrt2,\sqrt3)$ [▶ 47:30](https://youtu.be/wtedDsycOZ8?t=2850)

$K = \mathbb{Q}(\sqrt2,\sqrt3)$ 是 $(x^2-2)(x^2-3)$ 的分裂體（$\pm\sqrt2,\pm\sqrt3$ 都在），次數 4（之前算過）。由推論 6，Galois 群有 4 個元素。

- 基底 $1,\sqrt2,\sqrt3,\sqrt6$：$\tau(a+b\sqrt2+c\sqrt3+d\sqrt6) = a+b\,\tau\sqrt2+c\,\tau\sqrt3+d\,\tau\sqrt2\,\tau\sqrt3$。所以 $\tau$ 完全由 $\sqrt2$、$\sqrt3$ 的去向決定 [▶ 50:00](https://youtu.be/wtedDsycOZ8?t=3000)。
- 不能把 $\sqrt2$ 送到 $\sqrt3$：$\sqrt2$ 是 $x^2-2$ 的根，像也必須是 $x^2-2$ 的根 [▶ 52:30](https://youtu.be/wtedDsycOZ8?t=3150)。
- 四種「口味」：

| | $\sqrt2\mapsto$ | $\sqrt3\mapsto$ |
|---|---|---|
| $1$ | $\sqrt2$ | $\sqrt3$ |
| $\tau$ | $\sqrt2$ | $-\sqrt3$ |
| $\sigma$ | $-\sqrt2$ | $\sqrt3$ |
| $\sigma\tau$ | $-\sqrt2$ | $-\sqrt3$ |

- $\sigma^2 = \tau^2 = 1$，$\sigma\tau = \tau\sigma$。$\mathrm{Gal}(K/\mathbb{Q}) = \{1,\sigma,\tau,\sigma\tau\}\cong V_4$——**Klein 四元群**（D&F 叫「V 群」）[▶ 55:00](https://youtu.be/wtedDsycOZ8?t=3300)。也可以叫 $(x^2-2)(x^2-3)$ 的 Galois 群。
- 這次所有可能的組合都是自同構；一般不一定——生成元要送到生成元，但還得和其他結構相容 [▶ 56:30](https://youtu.be/wtedDsycOZ8?t=3390)。
- 預告：$\mathbb{Q}(\sqrt[3]2,\zeta_3)$（$x^3-2$ 的分裂體）的 Galois 群是 6 階，「我記得是 $S_3$」。

**固定體** [▶ 57:30](https://youtu.be/wtedDsycOZ8?t=3450)
- $K^{\{1,\sigma\}} = \mathbb{Q}(\sqrt3)$；$K^{\{1,\tau\}} = \mathbb{Q}(\sqrt2)$；$K^{\{1,\sigma\tau\}} = \mathbb{Q}(\sqrt6)$。
- 包含反轉的命題暗示：**體塔**和 **Galois 群的子群格**之間有有趣的對應——下次的主題，「也是開始變難的地方」。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 自同構群 | automorphism group | §1 |
| $F$-固定自同構 | automorphisms fixing $F$ | §1 |
| 固定體 | fixed field | §4 |
| Galois 擴張 | Galois extension | §5 |
| Galois 群 | Galois group | §5 |
| Klein 四元群 | Klein four-group ($V_4$) | §6 |

## ⚠️ 待確認清單

（本集無）
