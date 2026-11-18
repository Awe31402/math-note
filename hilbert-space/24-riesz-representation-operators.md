---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 24
lecture: Lecture 24
date: 2023-03-22
video: https://youtu.be/t45OJy4Ef9U （part 1）、https://youtu.be/AHF6I0ja9Xk （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.7（書頁 132–134，PDF 頁 151–153）、§4.1–4.2（書頁 145–151，PDF 頁 164–170）
---

# 第 24 集 · Riesz 表示定理、Hilbert 空間上的算子 [▶ 影片](https://youtu.be/t45OJy4Ef9U)

← 上一集：[23-separable-orthogonality](23-separable-orthogonality.md) ｜ [總目錄](README.md) ｜ 下一集：[25-bilinear-forms-adjoint](25-bilinear-forms-adjoint.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 24 集（春假後第一堂）
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 14:20，自動字幕）＋ Debnath & Mikusiński §3.7、§4.1–4.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Riesz 表示定理](#1-riesz-表示定理)
- [2. 例 1：取出某一個分量](#2-例-1取出某一個分量)
- [3. 例 2：在一點取值，不是有界的](#3-例-2在一點取值不是有界的)
- [4. 例 3：積分泛函](#4-例-3積分泛函)
- [5. Riesz 表示定理的證明（課堂跳過）](#5-riesz-表示定理的證明課堂跳過)
- [6. 算子與算子範數](#6-算子與算子範數)
- [7. ℂᴺ 上的算子就是矩陣](#7-ℂᴺ-上的算子就是矩陣)
- [8. 更多例子：微分、積分、乘法算子](#8-更多例子微分積分乘法算子)
- [9. 算子的乘積](#9-算子的乘積)
- [10. 可分空間上的有界算子是無窮矩陣](#10-可分空間上的有界算子是無窮矩陣)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說第一次考試他很快就會改完（學生說至少要兩週，講者說「學生在身邊會讓我改快一點」）。他以為第 3 章結束了，但 Riesz 表示定理是第 4 章很多東西的基礎，所以回頭講。[▶ 01:10](https://youtu.be/t45OJy4Ef9U?t=70)

| 主題 | 課本 |
|---|---|
| Riesz 表示定理與例子 | Example 3.7.1–3.7.3、Theorem 3.7.7，pp. 132–134 |
| 算子、算子範數 | §4.1–4.2 開頭，pp. 145–146 |
| $\mathbb{C}^N$ 上的算子 = 矩陣 | Example 4.2.2，pp. 146–147 |
| 微分、積分、乘法算子；不交換的算子 | Example 4.2.3–4.2.7，pp. 147–150 |
| $\|AB\|\le\|A\|\|B\|$；無窮矩陣 | Theorem 4.2.8–4.2.9，pp. 150–151 |

---

## 1. Riesz 表示定理

[▶ 01:43](https://youtu.be/t45OJy4Ef9U?t=103) 課本 Theorem 3.7.7。

**定理**：$H$ 是 Hilbert 空間，$f$ 是 $H$ 上的**有界線性泛函**。則存在**唯一**的 $x_0\in H$ 使

$$f(x)=\langle x,x_0\rangle\quad\text{對所有 }x\in H,$$

而且 $\|f\|=\|x_0\|$。

【課堂討論】[▶ 02:52](https://youtu.be/t45OJy4Ef9U?t=172)

- Hilbert 空間：學生答「完備的內積空間」；講者補充：內積誘導範數。
- **線性泛函**：從 $H$ 到純量體（這裡取 $\mathbb{C}$）的線性映射（定義在 p. 29，比 Hilbert 空間更一般，任何向量空間都可以）。
- **有界**：學生給出兩種等價說法：(1) $|f(x)|\le\alpha$ 對所有單位向量 $x$；(2) $|f(x)|\le\alpha\|x\|$ 對所有 $x$。

講者【口頭】[▶ 04:51](https://youtu.be/t45OJy4Ef9U?t=291)：這不是我們最早學的「有界」（上面放一個數就好），而是「一個數乘上輸入的長度」，是更細緻的有界概念。

$x_0$ 有時叫做 **Riesz 向量**（課本叫 **representer**，代表元）。講者說：「我可能讀太多 Peter 的笑話了」（他十歲左右的姪子會寄笑話給他）。

---

## 2. 例 1：取出某一個分量

[▶ 05:27](https://youtu.be/t45OJy4Ef9U?t=327) 課本 Example 3.7.3。

$H=\mathbb{C}^n$，固定 $n_0\in\{1,\dots,n\}$，

$$f(x_1,\dots,x_n)=x_{n_0}.$$

顯然是線性泛函。而且

$$f(x)=\langle x,e_{n_0}\rangle=x^T\overline{e_{n_0}}=x^Te_{n_0}=x_{n_0},$$

$e_{n_0}$ 的第 $i$ 分量是 $\delta_{n_0i}$（實向量，共軛不變）。所以 Riesz 向量是 $x_0=e_{n_0}$。

**範數**【課堂討論】[▶ 09:32](https://youtu.be/t45OJy4Ef9U?t=572)：$\|f\|=\sup_{\|x\|=1}|x_{n_0}|$。單位向量的每個分量的模都 $\le1$（不可能有分量是 2 而總長是 1）。上確界在 $x=e_{n_0}$ 時取到（其實是最大值），所以 $\|f\|=1=\|e_{n_0}\|=\|x_0\|$。✓

---

## 3. 例 2：在一點取值，不是有界的

[▶ 12:40](https://youtu.be/t45OJy4Ef9U?t=760) 課本 Example 3.7.2。

$H=L^2(a,b)$，固定 $t_0\in(a,b)$，

$$f(x)=x(t_0).$$

**線性**【課堂討論】：$f(x+cy)=(x+cy)(t_0)=x(t_0)+cy(t_0)$，函數的加法是逐點定義的。

**不有界**[▶ 16:24](https://youtu.be/t45OJy4Ef9U?t=984)：講者先複習 $L^2(a,b)$ 的內積 $\int_a^bx\bar y$，範數 $\|x\|=\sqrt{\int_a^b|x(t)|^2dt}$。單位向量就是 $\int_a^b|x|^2=1$。

講者問：為什麼 $|f(x)|=|x(t_0)|$ 不能被控制？

- **Lebesgue 的論證**[▶ 20:13](https://youtu.be/t45OJy4Ef9U?t=1213)：Lebesgue 積分不在乎函數在一點的值。拿一個積分為 1 的函數，把它在 $t_0$ 的值改成「一兆」，積分還是 1（只改了一點，幾乎處處相等）。所以 $x(t_0)$ 可以任意大，而 $\|x\|$ 不變。
- **比較不「濫用」Lebesgue 的論證**：考慮越來越尖的帳篷函數，在 $a,b$ 之間，面積（或範數）維持固定，高度卻要多高有多高（變窄就好）。極限會逼近 **Dirac δ**，但在那之前，帳篷的值任意大而積分有界。「積分有界不推出函數有界。」

> 以下**不是逐字稿內容**，是補一句：嚴格說，$L^2$ 的元素是等價類，「在一點的值」本來就沒有定義（第 14 集 §2.6 課本也說了）；課本說它「線性但不有界」，是指在有定義的函數上。這正是 Riesz 表示定理的反面：如果它有界，就會有一個 $x_0\in L^2$ 使 $x(t_0)=\int x\bar x_0$，那個 $x_0$ 得是 δ 函數，而 δ 不在 $L^2$ 裡。

---

## 4. 例 3：積分泛函

[▶ 22:31](https://youtu.be/t45OJy4Ef9U?t=1351) 課本 Example 3.7.1。

$H=L^2((a,b))$，

$$f(x)=\int_a^bx(t)\,dt.$$

令 $x_0(t)=1$（常數函數），$x_0\in L^2(a,b)$，而且

$$\langle x,x_0\rangle=\int_a^bx(t)\overline{1}\,dt=\int_a^bx(t)\,dt=f(x).$$

講者：「這蠢到不行，那就是常數函數 1。」

**為什麼有界**【課堂討論】[▶ 25:29](https://youtu.be/t45OJy4Ef9U?t=1529)：講者先跟學生想直接比較 $\left|\int_ax\right|$ 和 $\int|x|^2$（試了常數函數，比較 $(b-a)^2$ 跟 $b-a$），「陷在雜草裡」。學生提醒：既然 $f(x)=\langle x,x_0\rangle$，就用內積的定理。講者：「好觀點！我們不需要做這些。」

$$|f(x)|=|\langle x,x_0\rangle|\le\|x\|\,\|x_0\|\qquad\text{（Cauchy–Schwarz）}.$$

所以有界，$\alpha=\|x_0\|=\sqrt{\int_a^b1\,dt}=\sqrt{b-a}$（當然 $b>a$）。[▶ 33:02](https://youtu.be/t45OJy4Ef9U?t=1982)

**一般原則**：任何 $f(x)=\langle x,x_0\rangle$ 都是有界線性泛函（Schwarz）；Riesz 表示定理說，在 Hilbert 空間裡，**反過來**也成立。

---

## 5. Riesz 表示定理的證明（課堂跳過）

[▶ 34:09](https://youtu.be/t45OJy4Ef9U?t=2049)

講者說證明不難，用到 Lemma 3.7.5（非零有界線性泛函的零空間的正交補是一維的），由此做一個投影公式。「現在你們知道定理是什麼，比知道證明更重要。」他講它是因為第 4 章有類似的定理，「我要你們看到這是一個更一般想法的第一個例子」。[▶ 37:06](https://youtu.be/t45OJy4Ef9U?t=2226)

【課本補充】

**Lemma 3.7.5**：$f$ 是 $H$ 上非零的有界線性泛函，則 $\dim\mathcal N(f)^\perp=1$。

證明：$f$ 連續，$\mathcal N(f)$ 是閉的真子空間，所以 $\mathcal N(f)^\perp\ne\{0\}$。取非零 $x_1,x_2\in\mathcal N(f)^\perp$，它們不在零空間裡，$f(x_1),f(x_2)\ne0$，有 $a\ne0$ 使 $f(x_1+ax_2)=0$。所以 $x_1+ax_2\in\mathcal N(f)\cap\mathcal N(f)^\perp=\{0\}$，$x_1,x_2$ 線性相依。

**Theorem 3.7.7 的證明**：

1. $f=0$：取 $x_0=0$。
2. $f\ne0$：取單位向量 $z_0\in\mathcal N(f)^\perp$。對任意 $x$：
   $$x=\big(x-\langle x,z_0\rangle z_0\big)+\langle x,z_0\rangle z_0.$$
   後項在 $\mathcal N(f)^\perp$（一維，由 $z_0$ 張成）；前項是 $x$ 減掉在 $z_0$ 方向的投影，在 $\mathcal N(f)$ 裡（因為 $H=\mathcal N(f)\oplus\mathcal N(f)^\perp$）。所以 $f$ 作用在前項是 0：
   $$f(x)=\langle x,z_0\rangle f(z_0)=\left\langle x,\overline{f(z_0)}z_0\right\rangle.$$
   令 $x_0=\overline{f(z_0)}z_0$。
3. **唯一**：若 $\langle x,x_0\rangle=\langle x,x_1\rangle$ 對所有 $x$，取 $x=x_0-x_1$ 得 $\|x_0-x_1\|^2=0$。
4. **$\|f\|=\|x_0\|$**：Schwarz 給 $\|f\|\le\|x_0\|$；又 $\|x_0\|^2=f(x_0)\le\|f\|\|x_0\|$。

【課本補充】反例（Example 3.7.4）：在**不完備**的「有限數列」空間中，$f(x)=\sum\frac{x_n}{n}$ 是有界線性泛函，但沒有該空間中的 $(z_n)$ 使 $f(x)=\langle x,(z_n)\rangle$（需要的 $z_n=\frac1n$ 有無限多個非零項）。所以完備性必要。課本也說：$H^*=H$（更精確：同構），Hilbert 空間的對偶空間就是它自己。

---

## 6. 算子與算子範數

[▶ 37:38](https://youtu.be/t45OJy4Ef9U?t=2258) 課本 §4.1–4.2。

**第 4 章：Hilbert 空間上的線性算子**。**線性算子**就是線性變換。講者說：常用「算子」這個詞，是因為例子多半是函數空間，而「函數的函數」通常叫算子，例如微分算子：吃進一個函數，吐出新函數。

課本用 $A$ 表示算子（講者說他習慣用 $A$ 表示矩陣）。$A:H\to H$：

$$\|A\|=\sup_{\|x\|=1}\|Ax\|\qquad\text{（算子範數）}.$$

**有界**：$\|Ax\|\le K\|x\|$；等價於在單位球面上有界。

**跟剛才的差別**[▶ 39:27](https://youtu.be/t45OJy4Ef9U?t=2367)：線性**泛函**是 $H\to$ 純量體；線性**算子**是 $H\to H$。

**簡單例子**（Example 4.2.1）：恆等算子 $I$（$\|I\|=1$）、零算子 $0$（$\|0\|=0$）、恆等算子的純量倍 $\alpha I$。

【課本補充】課本：算子有界 ⟺ 連續（§1.5）；求算子的範數通常比證它有界難得多。

---

## 7. ℂᴺ 上的算子就是矩陣

[▶ 40:00](https://youtu.be/t45OJy4Ef9U?t=2400) 課本 Example 4.2.2。講者：「在一個例子裡做十分之一的線性代數。」

$T:\mathbb{C}^n\to\mathbb{C}^n$ 線性。$\{e_1,\dots,e_n\}$ 是標準正規正交基底。

**標準矩陣**：寫 $Te_i=\sum_{j=1}^na_{ji}e_j$，這是矩陣的第 $i$ 行。（講者用 $a_{ji}$，課本用 $\alpha_{ij}=\langle Ae_j,e_i\rangle$，指標順序相反但意思一樣。）

**用內積取出係數**[▶ 42:27](https://youtu.be/t45OJy4Ef9U?t=2547)：

$$\langle Te_i,e_k\rangle=\sum_ja_{ji}\langle e_j,e_k\rangle=\sum_ja_{ji}\delta_{jk}=a_{ki}.$$

和在第一個位置，所以可以直接拉出來。學生問為什麼第一個位置這麼好用，講者：這是內積的定義；第二個位置是共軛線性（第 3 章第 1 題作業）。

**作用在一般向量**：$x=\sum_i\lambda_ie_i$，

$$Tx=\sum_i\lambda_iTe_i=\sum_j\left(\sum_ia_{ji}\lambda_i\right)e_j,\qquad\langle Tx,e_k\rangle=\sum_ia_{ki}\lambda_i.$$

講者說這跟 Riesz 定理「在道德上」很像：線性映射的作用由一組數乘上分量的和完全捕捉。[▶ part 2 03:32](https://youtu.be/AHF6I0ja9Xk?t=212)

### 有界性：兩個估計

【課堂討論】[▶ 48:49](https://youtu.be/t45OJy4Ef9U?t=2929)

**講者的估計**：$\|x\|=1$ ⟹ 每個 $|\lambda_i|\le1$。由三角不等式，

$$\|Tx\|\le\sum_{i,j}|\lambda_i||a_{ji}|\|e_j\|\le\sum_{i,j}|a_{ji}|=:K.$$

所以 $T$ 有界，$\|T\|\le K$。

學生問這是不是 $\|T\|$ 本身。講者：不是，這只是上界；$\|T\|$ 是上確界，所以 $\le K$。[▶ 54:00](https://youtu.be/t45OJy4Ef9U?t=3240)

**課本的估計**：

$$\|A\|\le\sqrt{\sum_{i,j}|\alpha_{ij}|^2}.$$

學生覺得兩者一樣；講者：「平方不是線性的，它們不一樣，但我想兩個都對，只是理由不同。」他接著寫出 $\|Tx\|^2=\sum_j\left|\sum_i\lambda_ia_{ji}\right|^2$（第 $j$ 分量的模平方加起來），說兩個都在他的研究裡用過。[▶ part 2 00:03](https://youtu.be/AHF6I0ja9Xk?t=3)

> 以下**不是逐字稿內容**，是課本那個估計的推導：對每個 $j$ 用 Cauchy–Schwarz，
> $$\left|\sum_ia_{ji}\lambda_i\right|^2\le\left(\sum_i|a_{ji}|^2\right)\left(\sum_i|\lambda_i|^2\right)=\sum_i|a_{ji}|^2\cdot\|x\|^2,$$
> 對 $j$ 加總得 $\|Tx\|^2\le\left(\sum_{i,j}|a_{ji}|^2\right)\|x\|^2$。這個界（Frobenius 範數，第 10 集用過）比講者的 $\sum|a_{ji}|$ 好，因為 $\sqrt{\sum c^2}\le\sum c$。

**結論**：$\mathbb{C}^N$ 上（因此任何有限維 Hilbert 空間上）的算子都有界；算子和 $N\times N$ 矩陣一一對應。

---

## 8. 更多例子：微分、積分、乘法算子

[▶ part 2 03:32](https://youtu.be/AHF6I0ja9Xk?t=212) 講者只提到，說「這些例子很重要，請自己讀，做幾題作業就沒問題」。

【課本補充】

**微分算子**（Example 4.2.3）：$Df=f'$，定義域 $\{f\in L^2([-\pi,\pi]):f'\in L^2\}$（$L^2$ 的真子空間）。**不有界**：$f_n=\sin nx$，$\|f_n\|=\sqrt\pi$，$\|Df_n\|=\|n\cos nx\|=n\sqrt\pi$。

**積分算子**（Example 4.2.4）：$(Tx)(s)=\int_a^bK(s,t)x(t)dt$，$K$ 叫**核（kernel）**。若 $\iint|K|^2<\infty$，則 $T$ 在 $L^2([a,b])$ 上有界，$\|T\|\le\sqrt{\iint|K(s,t)|^2dtds}$（證明：對內層積分用 Schwarz）。——這是矩陣例子的「連續版」：$\sum_i a_{ji}\lambda_i$ 變成 $\int K(s,t)x(t)dt$。

**乘法算子**（Example 4.2.5）：$(Ax)(t)=z(t)x(t)$，$z\in C([a,b])$ 叫乘子。$\|Ax\|\le\max|z|\cdot\|x\|$，有界。

**不交換的算子**[▶ part 2 05:52](https://youtu.be/AHF6I0ja9Xk?t=352)：講者說課本給了「微分 vs 乘以 $x$」不交換的例子，這對量子力學很重要。

【課本補充】Example 4.2.6：$A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$、$B=\begin{pmatrix}0&1\\0&0\end{pmatrix}$，$AB\ne BA$。Example 4.2.7：$(Af)(x)=xf(x)$、$D=\frac{d}{dx}$，$AD\ne DA$。

> 以下**不是逐字稿內容**，是算出來的差：$(DA-AD)f=(xf)'-xf'=f$，即 $DA-AD=I$。量子力學裡位置算子 $x$ 和動量算子 $-i\hbar\frac{d}{dx}$ 的交換子 $[x,p]=i\hbar$ 就是這個。

【課本補充】課本 p. 149 的運算規則：$A+B=B+A$、$A(BC)=(AB)C$、$(A+B)C=AC+BC$ 等；但**一般不成立** $A(B+C)=AB+AC$（因為定義域問題：$\mathcal D(AB)=\{x\in\mathcal D(B):Bx\in\mathcal D(A)\}$）。

---

## 9. 算子的乘積

[▶ part 2 05:52](https://youtu.be/AHF6I0ja9Xk?t=352) 課本 Theorem 4.2.8。

算子的**乘積** $AB$ 就是合成：$(AB)x=A(Bx)$。

**定理**：有界算子的乘積有界，而且

$$\|AB\|\le\|A\|\,\|B\|.$$

【課本補充】證明：$\|ABx\|\le\|A\|\|Bx\|\le\|A\|\|B\|\|x\|$。（第 10 集矩陣指數用的就是這個。）

---

## 10. 可分空間上的有界算子是無窮矩陣

[▶ part 2 06:57](https://youtu.be/AHF6I0ja9Xk?t=417) 課本 Theorem 4.2.9。講者說「這才是我今天想講到的」。

**定理**：可分無限維 Hilbert 空間上的有界算子可以用**無窮矩陣**表示。

講者要對比三件事：Riesz 表示定理（$f(x)=\langle x,x_0\rangle$）、剛才 $\mathbb{C}^n$ 上的公式、這個定理。「讀這些時，我覺得它們在道德上是同一回事。」[▶ part 2 07:37](https://youtu.be/AHF6I0ja9Xk?t=457)

【課堂討論】講者問可分無限維 Hilbert 空間是什麼，學生答：有完備的正規正交系統（推廣意義下的正規正交基底）$e_1,e_2,\dots$。所以每個 $x=\sum_{i=1}^\infty\lambda_ie_i$：有限和換成無窮級數。

**證明的構想**（講者的寫法）[▶ part 2 10:26](https://youtu.be/AHF6I0ja9Xk?t=626)：寫 $Te_i=\sum_{j=1}^\infty a_{ji}e_j$（無窮標準矩陣的第 $i$ 行）。跟 $e_k$ 做內積，級數可以拉出來（內積的性質），Kronecker δ 留下

$$\langle Te_i,e_k\rangle=a_{ki}.$$

講者：「其實可以反過來用這個來**定義**矩陣元素，也許更好。」$k,i$ 都從 1 跑到無窮，所以是無窮矩陣——「兩個方向都延伸的數列」。

【課本補充】課本的證明：令 $\alpha_{ij}=\langle Ae_j,e_i\rangle$。對 $x\in H$，

$$Ax=A\left(\lim_n\sum_{j=1}^n\langle x,e_j\rangle e_j\right)=\lim_n\sum_{j=1}^n\langle x,e_j\rangle Ae_j=\sum_{j=1}^\infty\langle x,e_j\rangle Ae_j,$$

第二個等號用 $A$ **連續**（有界）把極限拿出來、再用線性。所以

$$\langle Ax,e_i\rangle=\sum_{j=1}^\infty\alpha_{ij}\langle x,e_j\rangle.$$

講者【口頭】[▶ part 2 11:43](https://youtu.be/AHF6I0ja9Xk?t=703)：「這是很好的處境：雖然是無限維，卻跟有限維那麼像。」有限維上所有算子都有界；可分無限維的有界算子本質上也是這樣，只是把 $\sum^n$ 換成 $\sum^\infty$。

**下一堂**：雙線性泛函與二次型。講者說今天犧牲了太多例子，那些沒寫在黑板上的例子請自己讀。

---

## 11. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| Riesz 表示 | 有界線性泛函 $f(x)=\langle x,x_0\rangle$，唯一，$\|f\|=\|x_0\|$ | $\dim\mathcal N(f)^\perp=1$；$x_0=\overline{f(z_0)}z_0$ |
| 反方向 | $\langle\cdot,x_0\rangle$ 必有界 | Cauchy–Schwarz |
| 例：取分量 | $f(x)=x_{n_0}=\langle x,e_{n_0}\rangle$，$\|f\|=1$ | |
| 例：取點值 | $x\mapsto x(t_0)$ 在 $L^2$ 上不有界 | 尖帳篷；代表元得是 δ |
| 例：積分 | $\int_a^bx=\langle x,1\rangle$，$\|f\|=\sqrt{b-a}$ | |
| 完備必要 | 有限數列空間上 $\sum x_n/n$ 無代表元 | |
| 算子範數 | $\|A\|=\sup_{\|x\|=1}\|Ax\|$ | |
| $\mathbb{C}^N$ | 算子 ↔ 矩陣，$\alpha_{ij}=\langle Ae_j,e_i\rangle$ | $\|A\|\le\sqrt{\sum|\alpha_{ij}|^2}$（Schwarz） |
| 微分 | 不有界：$\|D\sin nx\|=n\|\sin nx\|$ | |
| 積分算子 | $\|T\|\le\sqrt{\iint|K|^2}$ | 矩陣的連續版 |
| 不交換 | $DA-AD=I$（$A=x\cdot$） | 量子力學 $[x,p]=i\hbar$ |
| 乘積 | $\|AB\|\le\|A\|\|B\|$ | |
| 無窮矩陣 | 可分空間上 $\langle Ax,e_i\rangle=\sum_j\alpha_{ij}\langle x,e_j\rangle$ | $A$ 連續，極限可拿出 |

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Riesz 表示定理 | 第 25 集：有界雙線性泛函 $\varphi(x,y)=\langle Ax,y\rangle$、伴隨算子的存在；Lax–Milgram 定理 |
| 矩陣 $\alpha_{ij}=\langle Ae_j,e_i\rangle$ | 第 25 集：伴隨算子 = 共軛轉置 |
| 微分算子不有界 | 課本 §4.11 無界算子；第 29–30 集邊界值問題 |
| 積分算子 | 課本 §4.8 緊緻算子；第 31 集 Green 函數 |
| $[x,p]$ | 第 33–34 集：量子力學、不確定性原理 |

---

## 附：本集一句話總結

> **Riesz 表示定理說：Hilbert 空間上每個有界線性泛函都只是「跟某個固定向量做內積」，範數也一樣（取點值之所以不有界，正是因為它的代表元得是不在 $L^2$ 裡的 δ）；同樣的精神延伸到算子：$\mathbb{C}^N$ 上的算子就是矩陣 $\langle Ae_j,e_i\rangle$，可分無限維 Hilbert 空間上的有界算子就是無窮矩陣。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-22 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 14:20）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.7、§4.1–4.2 整理。*
