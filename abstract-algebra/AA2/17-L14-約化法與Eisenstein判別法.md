---
course: Abstract Algebra II (Spring 2026)
episode: 17
lecture: L14
date: 2026-02-18
video: https://www.youtube.com/watch?v=pUdxGE7-k_8
notes: 講義/AA2/Math422_Lecture14_IrreduciblePolynomialTheory.pdf
---

# 第 17 集 · L14：不可約判別——模 $p$ 約化與 Eisenstein [▶ 影片](https://www.youtube.com/watch?v=pUdxGE7-k_8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[16-L13-除法算法與不可約性]] ｜ [總目錄](../README.md) ｜ 下一集：[[18-L15-多項式理論完結]] →

## 本集概要

「更多多項式理論」（老師 2018 年 421 講義 Lecture 26，跟 Gallian）：
- 警示：$x^4+14x^2+49 = (x^2+7)^2$ 在 $\mathbb{R}$ 上可約卻沒有實根——4 次以上「無根 ⇒ 不可約」失效。
- **內容**（content）與**本原多項式**；**本原 × 本原 = 本原**（用模 $p$ 約化）。
- 環同態誘導多項式環的同態（**係數約化**）。
- 在 $\mathbb{Q}$ 上可約 ⇒ 在 $\mathbb{Z}$ 上可約。
- **模 $p$ 判別法**：約化後不可約且次數不變 ⇒ 原式在 $\mathbb{Q}$ 上不可約。例子；$x^4+1$ 的支線任務。
- **Eisenstein 判別法**；**分圓多項式** $\Phi_p$ 不可約（平移技巧）。
- $F[x]/(p(x))$ 是體；用 $x^4+x+1$ 造出 16 個元素的體，算反元素。

> 📘 講義對應：Math422 Lecture 14「More Polynomial Theory」= 老師 2018 年 421 講義 §4.6 Lecture 26（p.149 起，Ex 4.6.7–Thm 4.6.11 等）；Gallian p.297；Bill Cook 的講義（第 9 章總整理）。

---

## 筆記

### 1. 警示例子 [▶ 00:30](https://youtu.be/pUdxGE7-k_8?t=30)

> **例**（講義 Ex 4.6.7）：$f(x) = x^4+14x^2+49 = (x^2+7)^2$，在 $\mathbb{R}$ 上可約，但沒有實根。

- 上次的定理（2、3 次：可約 ⇔ 有根）不能延伸到 4 次。「到了四次，所有賭注都取消。」需要更多分析 [▶ 02:00](https://youtu.be/pUdxGE7-k_8?t=120)。

### 2. 內容與本原多項式 [▶ 02:30](https://youtu.be/pUdxGE7-k_8?t=150)

> **定義**（講義 Def 4.6.8）：非零 $f = a_nx^n+\cdots+a_0\in\mathbb{Z}[x]$ 的**內容**（content）是 $\gcd(a_0,\dots,a_n)$。內容為 1 的叫**本原多項式**（primitive polynomial）。

- 例「1 + i」（老師漏了一個例子，就把編號放進「另一個維度」：「這是我的課，我想怎麼編就怎麼編。」）：$3x+6$ 的內容是 3，$3x+6 = 3(x+2)$，$x+2$ 是本原的 [▶ 04:30](https://youtu.be/pUdxGE7-k_8?t=270)。
- **首一多項式都是本原的**：gcd 裡有個 1。任何係數是 1 也一樣。
- $3x^2+5x+7$ 也是本原（係數互質）。內容 = 「自然地從 $\mathbb{Z}[x]$ 多項式提出來的那個整數」。

> **定理**（講義 Thm 4.6.10；Gallian 稱為 Gauss 引理）：兩個本原多項式的積是本原的 [▶ 06:30](https://youtu.be/pUdxGE7-k_8?t=390)。

**證明**（反證——「我最不喜歡的證明方式，感覺很空」）：$f,g$ 本原，設 $fg$ 不本原，取質數 $p$ 整除 $fg$ 的內容：$fg = p\,h(x)$ [▶ 08:30](https://youtu.be/pUdxGE7-k_8?t=510)。把係數模 $p$：
$$0 = \overline{ph} = \bar f\cdot\bar g\quad\text{在 }\mathbb{Z}_p[x].$$
$\mathbb{Z}_p[x]$ 是整環，所以 $\bar f = 0$ 或 $\bar g = 0$，即 $p$ 整除 $f$ 或 $g$ 的每個係數，與本原矛盾 [▶ 17:00](https://youtu.be/pUdxGE7-k_8?t=1020)。

（老師給要約化的多項式取名「Pac-Man」，學生建議改用「oopsilon」。）

### 3. 係數約化同態 [▶ 13:30](https://youtu.be/pUdxGE7-k_8?t=810)

例：$f = 13x^3+2x^2+x+7$，模 7 得 $6x^3+2x^2+x$。要強調是 $\mathbb{Z}_7$ 的元素可以加橫線。

**一般構造** [▶ 14:00](https://youtu.be/pUdxGE7-k_8?t=840)：$\phi:R\to S$ 是環同態，則
$$\Psi(a_nx^n+\cdots+a_0) = \phi(a_n)x^n+\cdots+\phi(a_0)$$
是 $R[x]\to S[x]$ 的環同態（可加、可乘；$\phi$ 把 1 送到 1 時 $\Psi$ 也是）。最常用的是自然映射 $\mathbb{Z}\to\mathbb{Z}_p$。「這比內容更重要。」

> **定理**（講義 Thm 4.6.11）：$f\in\mathbb{Z}[x]$。若 $f$ 在 $\mathbb{Q}$ 上可約，則在 $\mathbb{Z}$ 上可約 [▶ 18:30](https://youtu.be/pUdxGE7-k_8?t=1110)。

**證明概要**：$f = g(x)h(x)$，$g,h\in\mathbb{Q}[x]$。乘上分母的最小公倍數，把係數變成整數，再用內容和「本原 × 本原 = 本原」整理（講義的證明假設 $f$ 首一）。
- 例：$6x^2+19x-7$。提出 6 得 $x^2+\frac{19}6x-\frac76 = (x+\frac72)(x-\frac13)$；把 6 拆成 $2\cdot3$ 分給兩個因式：$(2x+7)(3x-1)$ [▶ 22:30](https://youtu.be/pUdxGE7-k_8?t=1350)。（老師中途想配方：「我會配方不代表我應該配方。」）

### 4. 模 $p$ 判別法 [▶ 25:30](https://youtu.be/pUdxGE7-k_8?t=1530)

> **定理**：$p$ 質數，$f\in\mathbb{Z}[x]$，$\deg f\ge1$。若 $\bar f$ 在 $\mathbb{Z}_p$ 上不可約，且 $\deg\bar f = \deg f$，則 $f$ 在 $\mathbb{Q}$ 上不可約。

- 證明（投影）[▶ 41:30](https://youtu.be/pUdxGE7-k_8?t=2490)：反證。若在 $\mathbb{Q}$ 上可約，由上一個定理在 $\mathbb{Z}$ 上 $f = gh$，$\deg g,\deg h<\deg f$。約化得 $\bar f = \bar g\bar h$；次數相等這個條件保證這是**真的**分解，與 $\bar f$ 不可約矛盾。
- 「這是不可約性兩大工具之一，另一個是 Eisenstein。」

**例 3** [▶ 29:00](https://youtu.be/pUdxGE7-k_8?t=1740)：$f = 29x^3+5x^2+2x+1$。先試 $p = 2$（最簡單）：$\bar f = x^3+x^2+1$。$\bar f(0) = 1$、$\bar f(1) = 1+1+1 = 1$，沒有根；3 次，所以不可約。故 $f$ 在 $\mathbb{Q}$ 上不可約。
- 「別小看這個：無窮多個有理數裡沒有一個是它的根——我們只檢查了 $\mathbb{Z}_2$ 的兩個數就知道了。」[▶ 31:30](https://youtu.be/pUdxGE7-k_8?t=1890)

**例 4** [▶ 33:30](https://youtu.be/pUdxGE7-k_8?t=2010)：$f = 21x^3-3x^2+2x+8$。
- 模 2：$x^3+x^2 = x^2(x+1)$，可約——**沒用**。（約化後可約**不**代表原式可約；這個判別法只能證不可約。）
- 模 5：$x^3+2x^2+2x+3$。$\bar f(0),\dots,\bar f(4) = 3,3,3,4,2$，都不是 0，所以不可約。故 $f$ 在 $\mathbb{Q}$ 上不可約 [▶ 35:30](https://youtu.be/pUdxGE7-k_8?t=2130)。

> **支線任務**（10 分）：$x^4+1$ 在 $\mathbb{Q}$ 上不可約，但它模**每個**質數 $p$ 都可約 [▶ 36:00](https://youtu.be/pUdxGE7-k_8?t=2160)。

- 所以這個判別法失敗時什麼也說明不了。老師算過，大約三頁；「比 67 秒學會魔術方塊難多了」[▶ 43:00](https://youtu.be/pUdxGE7-k_8?t=2580)。
- 「reducible 和 irreducible 英文聽起來太像，腦中很難分開。」

**例 5**（講義）[▶ 43:30](https://youtu.be/pUdxGE7-k_8?t=2610)：一個有理係數的四次式，乘分母的最小公倍數後模 2 得 $x^4+x+1$。
- 四次式沒根只表示沒有一次因式；唯一可能是兩個**不可約二次式**的積。$\mathbb{Z}_2$ 上的二次式 $x^2$、$x^2+1 = (x+1)^2$、$x^2+x$ 都可約，**只有 $x^2+x+1$ 不可約**。
- 試 $(x^2+x+1)^2 = x^4+x^2+1\ne x^4+x+1$（比較係數會不相容）；或用長除法：$x^4+x+1$ 除以 $x^2+x+1$ 餘 1。所以 $x^4+x+1$ 不可約，原式在 $\mathbb{Q}$ 上不可約 [▶ 53:00](https://youtu.be/pUdxGE7-k_8?t=3180)。

### 5. Eisenstein 判別法 [▶ 45:00](https://youtu.be/pUdxGE7-k_8?t=2700)

> **定理**（Eisenstein 判別法）：$f = a_nx^n+\cdots+a_0\in\mathbb{Z}[x]$。若有質數 $p$ 使
> - $p\nmid a_n$；
> - $p\mid a_j$ 對所有 $j<n$；
> - $p^2\nmid a_0$，
>
> 則 $f$ 在 $\mathbb{Q}$ 上不可約。

- 「比模 $p$ 法更容易用，但對我來說更難記。」
- 例：$13x^7+2x^6+4x^3+18x+2$，$p = 2$：$2\nmid13$；$2\mid2,4,18,2$；$4\nmid2$。不可約 [▶ 46:30](https://youtu.be/pUdxGE7-k_8?t=2790)。

**分圓多項式** [▶ 47:00](https://youtu.be/pUdxGE7-k_8?t=2820)：$p$ 質數，
$$\Phi_p(x) = x^{p-1}+x^{p-2}+\cdots+x+1 = \frac{x^p-1}{x-1}$$
在 $\mathbb{Q}$ 上不可約。
- **平移技巧**：看 $f(x) = \Phi_p(x+1) = \dfrac{(x+1)^p-1}{x}$。用二項式定理展開，常數的 1 抵消，再除以 $x$，次數各降一：
$$f(x) = x^{p-1}+\binom p1x^{p-2}+\cdots+\binom p{p-1}.$$
  首項以外的係數都被 $p$ 整除，常數項 $\binom p{p-1} = p$ 不被 $p^2$ 整除。Eisenstein ⇒ $f$ 不可約 [▶ 49:00](https://youtu.be/pUdxGE7-k_8?t=2940)。
- 若 $\Phi_p = gh$ 是真分解，則 $\Phi_p(x+1) = g(x+1)h(x+1)$ 也是，矛盾。
- 一般原則：**把 $x$ 換成 $x+c$ 後不可約，原式就不可約**。對比較刁鑽的題目很常用 [▶ 51:00](https://youtu.be/pUdxGE7-k_8?t=3060)。
- 老師說這段代數之後很重要，下次再慢慢講一遍。

### 6. 用不可約多項式造體 [▶ 51:00](https://youtu.be/pUdxGE7-k_8?t=3060)

- $F$ 是體：$(p(x))$ 是 $F[x]$ 的極大理想 $\iff p(x)$ 在 $F$ 上不可約（之前證過）。
- **推論**：$p(x)$ 不可約 ⇒ $F[x]/(p(x))$ 是體。

**例**（老師特地為大家寫的）[▶ 52:30](https://youtu.be/pUdxGE7-k_8?t=3150)：$p(x) = x^4+x+1$ 在 $\mathbb{Z}_2$ 上不可約（§4 例 5）。令 $\beta = x+(p(x))$，體 $\mathbb{Z}_2[x]/(p(x))$。
- 元素是 $a_0+a_1\beta+a_2\beta^2+a_3\beta^3$（$a_i\in\mathbb{Z}_2$），共 $2^4 = 16$ 個 [▶ 54:30](https://youtu.be/pUdxGE7-k_8?t=3270)。乘法表 $16\times16 = 256$ 格（交換、有一列 0、乘 1 很簡單，所以沒那麼多）。
- $\beta^4+\beta+1 = 0$，模 2 下 $\beta(\beta^3+1) = \beta^4+\beta = 1$，所以 $\beta^{-1} = \beta^3+1$ [▶ 55:30](https://youtu.be/pUdxGE7-k_8?t=3330)。
- $\beta^{-2} = (\beta^3+1)^2 = \beta^6+1 = \beta^2(\beta+1)+1 = \beta^3+\beta^2+1$。（老師是在監考微分方程考試時摸索出來的；用 Google AI 產生的乘法表驗證——「Google 證明法，我一定是對的」。）
- 這是一個**特徵 2、有 16 個元素的體**——以前見過嗎？不可約多項式能造出無窮多種新例子 [▶ 58:00](https://youtu.be/pUdxGE7-k_8?t=3480)。

**講義** [▶ 58:30](https://youtu.be/pUdxGE7-k_8?t=3510)：老師的弟弟 Bill 給的講義，「D&F 第 9 章所有有趣內容的超濃縮總整理（除了 Gröbner 基）」，下次再談。

> 💬 學生在 Boss Fight 前緊張；老師：「如果考試你全都會，就學不到東西。我的目標是找出你不會的再解釋。」「你們都要畢業了，在乎成績幹嘛？」[▶ 33:00](https://youtu.be/pUdxGE7-k_8?t=1980)

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 內容 | content | §2 |
| 本原多項式 | primitive polynomial | §2 |
| Gauss 引理 | Gauss's lemma | §2 |
| 係數約化 | reduction of coefficients | §3 |
| 誘導同態 | induced homomorphism | §3 |
| 模 $p$ 判別法 | mod $p$ irreducibility test | §4 |
| Eisenstein 判別法 | Eisenstein's criterion | §5 |
| 分圓多項式 | cyclotomic polynomial | §5 |
| 平移技巧 | shift trick | §5 |

## ⚠️ 待確認清單

（本集無）
