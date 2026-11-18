---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 18
lecture: Lecture 18
date: 2023-02-27
video: https://youtu.be/qn2F4fts6Hw （part 1）、https://youtu.be/2o5AhLOnRfM （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.1–3.3 開頭（書頁 93–100，PDF 頁 112–119）
---

# 第 18 集 · 內積空間與 Hilbert 空間、誘導範數 [▶ 影片](https://youtu.be/qn2F4fts6Hw)

← 上一集：[17-lebesgue-rn-convolution](17-lebesgue-rn-convolution.md) ｜ [總目錄](README.md) ｜ 下一集：[19-weighted-sobolev-weak-convergence](19-weighted-sobolev-weak-convergence.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 18 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 19:13，自動字幕）＋ Debnath & Mikusiński §3.1–3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 內積的定義](#1-內積的定義)
- [2. 第二個位置是共軛線性](#2-第二個位置是共軛線性)
- [3. 內積空間的例子](#3-內積空間的例子)
- [4. 直積上的內積](#4-直積上的內積)
- [5. 誘導範數與 Schwarz 不等式](#5-誘導範數與-schwarz-不等式)
- [6. 三角不等式](#6-三角不等式)
- [7. 平行四邊形定律：不是每個範數都來自內積](#7-平行四邊形定律不是每個範數都來自內積)
- [8. 正交與畢氏定理](#8-正交與畢氏定理)
- [9. 實內積空間與角度](#9-實內積空間與角度)
- [10. Hilbert 空間](#10-hilbert-空間)
- [11. 兩個不完備的內積空間](#11-兩個不完備的內積空間)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說他很喜歡今天的內容。[▶ 00:01](https://youtu.be/qn2F4fts6Hw?t=1)

| 主題 | 課本 |
|---|---|
| 歷史 | §3.1，pp. 93–94 |
| 內積、例子 | Definition 3.2.1、Example 3.2.2–3.2.8，pp. 94–96 |
| 誘導範數、Schwarz、三角不等式 | Theorem 3.2.9、Corollary 3.2.10，pp. 96–97 |
| 平行四邊形定律、正交、畢氏定理 | Theorem 3.2.12–3.2.14，pp. 97–98 |
| Hilbert 空間、不完備的例子 | Definition 3.3.1、Example 3.3.2–3.3.6，pp. 99–100 |

**歷史**[▶ 01:05](https://youtu.be/qn2F4fts6Hw?t=65)：課本 §3.1：David Hilbert（1862–1943）在 1904–1910 年發表一系列論文（無窮多變數的二次型、積分方程），1912 年集結成書《Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen》。講者說德文書名念錯了，「你們可以取笑我」，並說這本書等於是「無限維分析」，從此帶動整個領域。【課本補充】後來 John von Neumann（1903–1957）給出 Hilbert 空間的公理化理論，發展出算子理論，為量子力學提供了數學基礎。

---

## 1. 內積的定義

[▶ 02:14](https://youtu.be/qn2F4fts6Hw?t=134) 課本 Definition 3.2.1。

$E$ 是**複**向量空間。映射 $\langle\cdot,\cdot\rangle:E\times E\to\mathbb{C}$ 叫**內積（inner product）**，如果對所有 $x,y,z\in E$、$\alpha,\beta\in\mathbb{C}$：

- (a) $\langle x,y\rangle=\overline{\langle y,x\rangle}$（**共軛對稱**：不是交換，是交換後取共軛）；
- (b) $\langle\alpha x+\beta y,z\rangle=\alpha\langle x,z\rangle+\beta\langle y,z\rangle$（**第一個位置線性**）；
- (c) $\langle x,x\rangle\ge0$；
- (d) $\langle x,x\rangle=0$ ⟹ $x=0$。

有內積的向量空間叫**內積空間（inner product space）**。講者說他叫 $\langle\cdot,\cdot\rangle$「lingle wrangle」。

【課本補充】也叫 pre-Hilbert space 或 unitary space。由 (a)，$\langle x,x\rangle=\overline{\langle x,x\rangle}$，所以 $\langle x,x\rangle$ 一定是**實數**——(c) 才有意義。講者也強調這點：一般的複內積不是實數，只有向量跟自己的內積才是。[▶ 20:58](https://youtu.be/qn2F4fts6Hw?t=1258)

---

## 2. 第二個位置是共軛線性

[▶ 04:34](https://youtu.be/qn2F4fts6Hw?t=274)

如果兩個位置都線性，叫**雙線性形式（bilinear form）**。內積不是：

$$\begin{aligned}\langle x,\alpha y+\beta z\rangle&=\overline{\langle\alpha y+\beta z,x\rangle}&&\text{(a)}\\&=\overline{\alpha\langle y,x\rangle+\beta\langle z,x\rangle}&&\text{(b)}\\&=\bar\alpha\,\overline{\langle y,x\rangle}+\bar\beta\,\overline{\langle z,x\rangle}\\&=\bar\alpha\langle x,y\rangle+\bar\beta\langle x,z\rangle.&&\text{(a)}\end{aligned}$$

用到：共軛的共軛是自己；和的共軛是共軛的和；積的共軛是共軛的積（複變課學過）。

所以第二個位置是**共軛線性**：純量提出來要取共軛。有人稱這種形式為 **sesquilinear form**（「1.5 倍線性」）。講者說它還是**可加的**：取 $\alpha=\beta=1$，$\langle x,y+z\rangle=\langle x,y\rangle+\langle x,z\rangle$。[▶ 06:48](https://youtu.be/qn2F4fts6Hw?t=408)

【課本補充】特別地 $\langle x,\alpha y\rangle=\bar\alpha\langle x,y\rangle$；取 $\alpha=0$ 得 $\langle0,y\rangle=\langle x,0\rangle=0$。

---

## 3. 內積空間的例子

[▶ 07:53](https://youtu.be/qn2F4fts6Hw?t=473)

| 例 | 空間 | 內積 |
|---|---|---|
| 3.2.2 | $\mathbb{C}$ | $\langle x,y\rangle=x\bar y$ |
| 3.2.3 | $\mathbb{C}^N$ | $\langle x,y\rangle=\sum_{k=1}^Nx_k\bar y_k$ |
| 3.2.4 | $\ell^2$（平方可和的複數列） | $\langle x,y\rangle=\sum_{k=1}^\infty x_k\bar y_k$ |
| 3.2.5 | 只有有限多個非零項的複數列 | 同 $\ell^2$ |
| 3.2.6 | $C([a,b])$（連續複值函數） | $\langle f,g\rangle=\int_a^bf(x)\overline{g(x)}dx$ |
| 3.2.7 | $L^2(\mathbb{R})$、$L^2(\mathbb{R}^N)$、$L^2(\Omega)$ | $\langle f,g\rangle=\int f\bar g$ |

**$\mathbb{C}^N$ 用矩陣寫**[▶ 08:27](https://youtu.be/qn2F4fts6Hw?t=507)：講者強烈建議寫成 $\langle x,y\rangle=x^T\bar y$，證性質時可以用矩陣乘法。例如

$$\langle x,\alpha y+\beta z\rangle=x^T\overline{(\alpha y+\beta z)}=x^T(\bar\alpha\bar y+\bar\beta\bar z)=\bar\alpha x^T\bar y+\bar\beta x^T\bar z.$$

**$\ell^2$**【課堂討論】[▶ 10:39](https://youtu.be/qn2F4fts6Hw?t=639)：講者問內積公式，學生答 $x_1\bar y_1+x_2\bar y_2+\cdots$，永不結束。學生問取 $y=x$ 會怎樣，講者：得到 $\sum|x_n|^2$。課本說 $\ell^2$ 在某種意義上是**最重要**的內積空間（Theorem 3.4.27）。

> 以下**不是逐字稿內容**，是補一句為什麼 $\ell^2$ 的內積級數收斂：由 Hölder（$p=q=2$），$\sum|x_k\bar y_k|\le\|x\|_2\|y\|_2<\infty$，絕對收斂。$L^2$ 的 $\int f\bar g$ 同理，$|f\bar g|\in L^1$。

**有限數列**[▶ 12:48](https://youtu.be/qn2F4fts6Hw?t=768)：講者說這像是「$\ell^2$ 裡的多項式」。兩個有限數列相加、乘純量還是有限數列，所以是 $\ell^2$ 的子空間，本身也是內積空間。

**$L^2(\mathbb{R})$**[▶ 15:47](https://youtu.be/qn2F4fts6Hw?t=947)：講者說驗證公理就是把 Lebesgue 積分的性質跟共軛對加法、乘法的規則結合起來。課本寫成 $\int_{-\infty}^\infty f(x)\overline{g(x)}dx$，「回到微積分的寫法」。講者說實際上他也常退回 Riemann 積分去想，「我還沒被 Lebesgue 的門徒完全收編」。

---

## 4. 直積上的內積

[▶ 17:27](https://youtu.be/qn2F4fts6Hw?t=1047) 課本 Example 3.2.8。

$(E_1,\langle\cdot,\cdot\rangle_1)$、$(E_2,\langle\cdot,\cdot\rangle_2)$ 是內積空間。在 $E=E_1\times E_2$ 上怎麼定義內積？

講者說：「這章我最喜歡的是充滿公式。」【課堂討論】學生先想交叉相乘，講者提醒：我們只能拿 $E_1$ 的向量跟 $E_1$ 的向量做內積。答案：**加起來**，

$$\langle(x_1,x_2),(y_1,y_2)\rangle=\langle x_1,y_1\rangle_1+\langle x_2,y_2\rangle_2.$$

**驗證 (d)**[▶ 19:42](https://youtu.be/qn2F4fts6Hw?t=1182)：設 $\langle(x_1,x_2),(x_1,x_2)\rangle=0$，即 $\langle x_1,x_1\rangle_1+\langle x_2,x_2\rangle_2=0$。兩項都是**非負實數**，和為 0 只能各自為 0。由 $E_1$、$E_2$ 的公理 (d)，$x_1=0$、$x_2=0$，所以 $(x_1,x_2)$ 是 $E$ 的零向量。（$E$ 的向量空間結構照直積的自然方式：逐分量加、逐分量乘純量。）

**跟點積的關係**[▶ 23:16](https://youtu.be/qn2F4fts6Hw?t=1396)：$\mathbb{R}$ 的內積是 $xy$；$\mathbb{R}^2=\mathbb{R}\times\mathbb{R}$ 用這個構造就得到 $x_1y_1+x_2y_2$，正是點積。可以歸納推到 $n$ 個。講者說：某種意義上點積就是「歸納地」誘導出來的自然內積。

【課本補充】$E_1$、$E_2$ 可以看成子空間 $E_1\times\{0\}$ 和 $\{0\}\times E_2$。

---

## 5. 誘導範數與 Schwarz 不等式

[▶ 24:28](https://youtu.be/qn2F4fts6Hw?t=1468)

**誘導範數（induced norm）**：

$$\|x\|=\sqrt{\langle x,x\rangle}.$$

有定義，因為 $\langle x,x\rangle$ 是非負實數；$\|x\|=0$ ⟺ $x=0$。

**齊次性**[▶ 25:37](https://youtu.be/qn2F4fts6Hw?t=1537)：

$$\|\alpha x\|=\sqrt{\langle\alpha x,\alpha x\rangle}=\sqrt{\alpha\bar\alpha\langle x,x\rangle}=|\alpha|\,\|x\|.$$

**三角不等式**要多花功夫。講者說：「要有點狡猾」，先證 Schwarz 不等式。

### Theorem 3.2.9（Schwarz 不等式）

[▶ 26:45](https://youtu.be/qn2F4fts6Hw?t=1605)

$$|\langle x,y\rangle|\le\|x\|\,\|y\|. \tag{3.1}$$

等號成立 ⟺ $x,y$ 線性相依。

講者【口頭】：一個好的線性代數學期一定要證這個；現在矩陣的東西被推到前面的課，「學生總是裝得比實際更笨」。他平常在實數情形用單位向量證；這裡照課本的方法，比較有效率。

**證明**（講者在黑板上代數算錯幾次再改正，下面是整理後的版本）：

1. $y=0$：兩邊都是 0。
2. $y\ne0$。對任意 $\alpha\in\mathbb{C}$：
   $$0\le\langle x+\alpha y,x+\alpha y\rangle=\langle x,x\rangle+\bar\alpha\langle x,y\rangle+\alpha\langle y,x\rangle+|\alpha|^2\langle y,y\rangle. \tag{3.2}$$
   第一步是公理 (c)；展開用第一位置線性、第二位置共軛線性。
3. 取 $\alpha=-\dfrac{\langle x,y\rangle}{\langle y,y\rangle}$（$y\ne0$，分母不為 0）[▶ 31:12](https://youtu.be/qn2F4fts6Hw?t=1872)。則 $\bar\alpha=-\dfrac{\langle y,x\rangle}{\langle y,y\rangle}$（講者：取共軛的效果是把 $x,y$ 對調），$|\alpha|^2=\dfrac{\langle x,y\rangle\langle y,x\rangle}{\langle y,y\rangle^2}$。代入：
   $$0\le\langle x,x\rangle-\frac{\langle y,x\rangle\langle x,y\rangle}{\langle y,y\rangle}-\frac{\langle x,y\rangle\langle y,x\rangle}{\langle y,y\rangle}+\frac{\langle x,y\rangle\langle y,x\rangle}{\langle y,y\rangle}.$$
4. 乘以 $\langle y,y\rangle>0$，而 $\langle x,y\rangle\langle y,x\rangle=\langle x,y\rangle\overline{\langle x,y\rangle}=|\langle x,y\rangle|^2$：
   $$0\le\langle x,x\rangle\langle y,y\rangle-|\langle x,y\rangle|^2.$$
   開根號即得 (3.1)。∎

講者說這就是 **Cauchy–Schwarz**，有限維、無限維都成立。[▶ 36:48](https://youtu.be/qn2F4fts6Hw?t=2208)

**等號成立的條件**：課本 pp. 96–97 有證，講者讓學生自己看。

【課本補充】
- 線性相依 ⟹ 等號：$x=\alpha y$ 時 $|\langle x,y\rangle|=|\alpha|\|y\|^2=\|x\|\|y\|$。
- 等號 ⟹ 線性相依：由 $\langle x,y\rangle\langle y,x\rangle=\langle x,x\rangle\langle y,y\rangle$，展開可得 $\big\|\langle y,y\rangle x-\langle x,y\rangle y\big\|^2=0$，所以 $\langle y,y\rangle x=\langle x,y\rangle y$，線性相依。

**關鍵一步**：$\|x+\alpha y\|^2\ge0$ 對所有 $\alpha$，取 $\alpha$ 讓它最小（就是 $x$ 減去在 $y$ 方向的投影）。

---

## 6. 三角不等式

[▶ 38:03](https://youtu.be/qn2F4fts6Hw?t=2283) 課本 Corollary 3.2.10。

$$\|x+y\|^2=\langle x+y,x+y\rangle=\|x\|^2+\langle x,y\rangle+\langle y,x\rangle+\|y\|^2.$$

**中間兩項**[▶ 39:25](https://youtu.be/qn2F4fts6Hw?t=2365)：$\langle y,x\rangle=\overline{\langle x,y\rangle}$。講者回顧：$u=a+ib$ 時 $u+\bar u=2a$，所以

$$\langle x,y\rangle+\overline{\langle x,y\rangle}=2\operatorname{Re}\langle x,y\rangle.$$

接著：

$$\|x+y\|^2=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2\le\|x\|^2+2|\langle x,y\rangle|+\|y\|^2\le\|x\|^2+2\|x\|\|y\|+\|y\|^2=(\|x\|+\|y\|)^2.$$

第一個 $\le$：複數的模 $\ge$ 實部（講者一度跳過這步，後來補上）；第二個 $\le$：Schwarz。兩邊都非負，開根號得 $\|x+y\|\le\|x\|+\|y\|$。∎

所以**每個內積空間都是賦範空間**（Definition 3.2.11）。

---

## 7. 平行四邊形定律：不是每個範數都來自內積

[▶ 43:39](https://youtu.be/qn2F4fts6Hw?t=2619)

**反問**：給一個賦範空間 $(E,\|\cdot\|)$，有沒有內積使 $\|x\|=\sqrt{\langle x,x\rangle}$？講者：「通常有，但不總是。」

### Theorem 3.2.12（平行四邊形定律）

[▶ 44:46](https://youtu.be/qn2F4fts6Hw?t=2686)

$$\|x+y\|^2+\|x-y\|^2=2\left(\|x\|^2+\|y\|^2\right). \tag{3.5}$$

講者把它叫成「極化恆等式（polarization identity）」——那其實是另一個公式（用範數反推內積）。證明直接，他沒寫。

【課本補充】證明：$\|x\pm y\|^2=\|x\|^2\pm\langle x,y\rangle\pm\langle y,x\rangle+\|y\|^2$，兩式相加，交叉項消掉。課本說：平行四邊形定律是賦範空間成為內積空間的**充分必要條件**（習題 12）。

**$\ell^1$ 型範數不來自內積**[▶ 45:58](https://youtu.be/qn2F4fts6Hw?t=2758)：講者說他相當確定 $\mathbb{R}^2$ 上的 $\|(x,y)\|_1=|x|+|y|$ 不能由內積誘導，想用平行四邊形定律當場示範，代進去卻得到 $4=4$，「我看不出問題……別在現場硬做了」。

> 以下**不是逐字稿內容**，是補上的反例：取 $x=(1,0)$、$y=(0,1)$。$\|x+y\|_1=\|x-y\|_1=2$，左邊 $=4+4=8$；右邊 $=2(1+1)=4$。$8\ne4$，平行四邊形定律不成立，所以 $\|\cdot\|_1$ 不來自任何內積。（講者大概是代了 $x=y$，那時兩邊恰好相等。）同樣的例子說明 $\ell^p$、$L^p$（$p\ne2$）都不是內積空間：Hilbert 空間是很特別的 Banach 空間。

---

## 8. 正交與畢氏定理

[▶ 49:20](https://youtu.be/qn2F4fts6Hw?t=2960) 課本 Definition 3.2.13、Theorem 3.2.14。

**正交（orthogonal）**：$x\perp y$ ⟺ $\langle x,y\rangle=0$。兩兩正交的集合叫**正交集**。

**對稱**：$x\perp y$ ⟹ $\langle y,x\rangle=\overline{\langle x,y\rangle}=\bar0=0$ ⟹ $y\perp x$。

**畢氏定理**[▶ 50:27](https://youtu.be/qn2F4fts6Hw?t=3027)：$x\perp y$ ⟹

$$\|x+y\|^2=\langle x+y,x+y\rangle=\|x\|^2+\langle x,y\rangle+\langle y,x\rangle+\|y\|^2=\|x\|^2+\|y\|^2.$$

講者：「我們剛在可能是無限維的情境下證了畢氏定理。」

【課本補充】課本說：能定義正交，是 Hilbert 空間理論跟一般 Banach 空間理論非常不同的地方。

---

## 9. 實內積空間與角度

[▶ 52:09](https://youtu.be/qn2F4fts6Hw?t=3129) 課本 p. 98。

**實內積空間**：內積是實數，(a) 變成對稱 $\langle x,y\rangle=\langle y,x\rangle$。前面所有定理照樣成立，把「複」換成「實」、$\mathbb{C}$ 換成 $\mathbb{R}$。**有限維的實內積空間叫歐氏空間（Euclidean space）**。

**角度**[▶ 56:17](https://youtu.be/qn2F4fts6Hw?t=3377)：實的情形，Schwarz 給出

$$-1\le\frac{\langle x,y\rangle}{\|x\|\|y\|}\le1\quad(x,y\ne0),$$

介於 $-1$ 和 1 之間的實數可以唯一寫成某個 $\theta\in[0,\pi]$ 的 cos，定義為 $x,y$ 之間的**角度**：

$$\cos\theta=\frac{\langle x,y\rangle}{\|x\|\|y\|}.$$

講者強調：這在**無限維**也能定義角度。

**複向量空間的角度**【口頭】[▶ 53:23](https://youtu.be/qn2F4fts6Hw?t=3203)：講者說他在線性代數有時也定義「複角度」，但比較隨意。混淆的來源：任何複向量空間也可以看成兩倍維度的實向量空間。

- 在 $\mathbb{C}$（複一維）中，$1$ 和 $i$ **線性相依**（$i=i\cdot1$），所以「複角度」該是 0。
- 但把 $\mathbb{C}$ 看成實向量空間 $\mathbb{R}^2$，$1$ 和 $i$ **互相垂直**，角度 90°。

所以複向量空間裡有兩種角度概念。他記得自己是對複內積取實部來定義複角度，「但不完全確定」。學生問：每個實向量空間都是偽裝的複向量空間嗎？講者：不是，只有偶數維才有希望（也許還有別的條件）。

---

## 10. Hilbert 空間

[▶ 58:29](https://youtu.be/qn2F4fts6Hw?t=3509) 課本 Definition 3.3.1。

【課堂討論】講者問 Hilbert 空間是什麼，學生答出缺的那個字：**完備**。

**Hilbert 空間** = **完備的內積空間**（對誘導範數完備）。

講者【口頭】：Hilbert 大概沒把它叫 Hilbert 空間，就像 Banach 也沒把它叫 Banach 空間。這是這門課的兩個大概念。

【Q&A】[▶ part 2 00:00](https://youtu.be/2o5AhLOnRfM?t=0) 學生問 Hilbert 和 Banach 的關係。講者：內積誘導範數，「完備的內積空間」就是對誘導範數完備。所以 **Hilbert ⟹ Banach**；但 Hilbert 空間是特別的 Banach 空間，不是每個 Banach 空間都是 Hilbert 空間。

**例子**[▶ part 2 01:27](https://youtu.be/2o5AhLOnRfM?t=87)：

| 空間 | Hilbert？ | 理由 |
|---|---|---|
| $\mathbb{C}$、$\mathbb{C}^N$ | ✓ | 完備（Example 3.3.2） |
| $\ell^2$ | ✓ | 第 6 集證過完備（Example 3.3.3） |
| $L^2(\mathbb{R})$、$L^2([a,b])$ | ✓ | Theorem 2.13.4（Example 3.3.6） |
| 有限數列 | ✗ | Example 3.3.4 |
| $C([a,b])$（$L^2$ 內積） | ✗ | Example 3.3.5 |

【Q&A】[▶ part 2 03:12](https://youtu.be/2o5AhLOnRfM?t=192) 學生問：如果把 $[a,b]$ 換成開區間 $(a,b)$，或是無界的區間，會不會出問題？講者說他不記得書上強調過這點；之前強調的是階梯函數用閉、開或半開區間都可以，但那跟「函數的定義域」是另一回事。他說：舉例說明為什麼不考慮這種情況（或它到底有沒有問題、要怎麼定義），會是個好練習。

> 以下**不是逐字稿內容**，是依第 2 章推論的：$(a,b)$ 和 $[a,b]$ 只差兩個點（零集），所以 $L^2((a,b))=L^2([a,b])$；$L^2(\mathbb{R})$ 也是 Hilbert 空間。這些都不會出問題。

---

## 11. 兩個不完備的內積空間

### Example 3.3.4：有限數列

[▶ part 2 05:30](https://youtu.be/2o5AhLOnRfM?t=330)

$$x_n=\left(1,\tfrac12,\tfrac13,\dots,\tfrac1n,0,0,\dots\right).$$

每個 $x_n$ 都是有限數列（「$\ell^2$ 裡的多項式」）。

**Cauchy**【課堂討論】[▶ part 2 06:37](https://youtu.be/2o5AhLOnRfM?t=397)：設 $n>m$，$x_n-x_m=(0,\dots,0,\frac1{m+1},\dots,\frac1n,0,\dots)$，前面相消。

$$\|x_n-x_m\|=\left(\sum_{k=m+1}^n\frac1{k^2}\right)^{1/2}\to0\quad(m,n\to\infty),$$

是收斂級數 $\sum\frac1{k^2}$ 的尾巴。（講者說課本的論證比他的更有說服力。）

**極限不在空間裡**[▶ part 2 09:19](https://youtu.be/2o5AhLOnRfM?t=559)：學生看出極限是 $(1,\frac12,\frac13,\dots)$。講者一度懷疑它在不在 $\ell^2$（想到調和級數發散），後來想通：$\ell^2$ 看的是**平方**和，

$$\left\|\left(1,\tfrac12,\tfrac13,\dots\right)\right\|_2=\sqrt{\sum\frac1{n^2}}=\sqrt{\frac{\pi^2}6}=\frac{\pi}{\sqrt6}<\infty.$$

所以極限在 $\ell^2$ 裡；它不在 $\ell^1$ 裡（調和級數）。但它有**無限多個**非零項，不是有限數列。所以有限數列空間是內積空間，不是 Hilbert 空間。

### Example 3.3.5：$C([0,1])$

[▶ part 2 12:11](https://youtu.be/2o5AhLOnRfM?t=731)

講者讓學生自己讀，在黑板上畫 Figure 3.1：

$$f_n(x)=\begin{cases}1, & 0\le x\le\frac12\\1-2n\left(x-\frac12\right), & \frac12\le x\le\frac12+\frac1{2n}\\0, & \frac12+\frac1{2n}\le x\le1\end{cases}$$

- $f_n$ 連續：先是 1，在 $\frac12$ 之後斜線降到 0，斜線越來越陡。
- **Cauchy**：課本給出 $\|f_n-f_m\|\le\left(\frac1n+\frac1m\right)^{1/2}\to0$。講者的直觀：相減只剩 $\frac12$ 附近的一個尖刺，高度最多 1、寬度趨近 0，平方再積分當然趨近 0。[▶ part 2 16:09](https://youtu.be/2o5AhLOnRfM?t=969)
- **逐點極限**：$[0,\frac12]$ 上是 1，$(\frac12,1]$ 上是 0——**不連續**，不在 $C([0,1])$ 裡。

所以 $C([0,1])$（配 $L^2$ 內積）不是 Hilbert 空間。對 $[a,b]$ 也能做一樣的例子。

**跟 $L^2([a,b])$ 的對比**[▶ part 2 17:15](https://youtu.be/2o5AhLOnRfM?t=1035)：$L^2([a,b])$ 比 $C([a,b])$ 大，那個階梯函數就在裡面，所以這個例子對它不構成問題；第 2 章已證它完備，而它的範數正是內積誘導的範數。

> 以下**不是逐字稿內容**，是一個對比：第 6 集說 $C([a,b])$ 配**最大值範數**是 Banach 空間；這裡配 **$L^2$ 範數**就不完備。同一個向量空間，換範數，完備與否會變。而 $L^2([a,b])$ 正是 $C([a,b])$ 對 $L^2$ 範數的完備化。

**下一堂**：§3.3 剩下的兩個例子（加權空間、Sobolev 空間），講者說它們對微分方程應用很重要；還有強收斂、弱收斂。§3.4 是正交與正規正交系統。「我們很快就要碰到在微分方程裡有很有趣應用的東西了……積分不在我的血液裡，我們回到線性了。」[▶ part 2 18:20](https://youtu.be/2o5AhLOnRfM?t=1100)

---

## 12. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 內積 | 共軛對稱、第一位置線性、$\langle x,x\rangle\ge0$、$=0\Rightarrow x=0$ | $\langle x,x\rangle$ 必為實數 |
| 第二位置 | $\langle x,\alpha y+\beta z\rangle=\bar\alpha\langle x,y\rangle+\bar\beta\langle x,z\rangle$ | 用 (a) 翻過去再翻回來 |
| 例 | $\mathbb{C}^N$：$x^T\bar y$；$\ell^2$：$\sum x_k\bar y_k$；$L^2$：$\int f\bar g$ | |
| 直積 | $\langle(x_1,x_2),(y_1,y_2)\rangle=\langle x_1,y_1\rangle_1+\langle x_2,y_2\rangle_2$ | 非負實數和為 0 ⟹ 各為 0 |
| 誘導範數 | $\|x\|=\sqrt{\langle x,x\rangle}$ | $\|\alpha x\|=\sqrt{\alpha\bar\alpha}\|x\|$ |
| Schwarz | $|\langle x,y\rangle|\le\|x\|\|y\|$，等號 ⟺ 線性相依 | $\|x+\alpha y\|^2\ge0$，$\alpha=-\frac{\langle x,y\rangle}{\langle y,y\rangle}$ |
| 三角不等式 | $\|x+y\|\le\|x\|+\|y\|$ | $2\operatorname{Re}\langle x,y\rangle\le2|\langle x,y\rangle|\le2\|x\|\|y\|$ |
| 平行四邊形 | $\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2)$ | ⟺ 範數來自內積 |
| 反例 | $\|\cdot\|_1$ 在 $\mathbb{R}^2$：$x=e_1$、$y=e_2$ 得 $8\ne4$ | |
| 畢氏 | $x\perp y\Rightarrow\|x+y\|^2=\|x\|^2+\|y\|^2$ | |
| 角度（實） | $\cos\theta=\frac{\langle x,y\rangle}{\|x\|\|y\|}$ | 無限維也能定義 |
| Hilbert | 完備的內積空間 | Hilbert ⟹ Banach，反之不然 |
| 不完備 | 有限數列：$(1,\frac12,\dots,\frac1n,0,\dots)\to(\frac1n)\notin$；$C([0,1])$：斜坡 → 階梯 | |

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 強收斂；弱收斂 $\langle x_n,y\rangle\to\langle x,y\rangle$ | 第 19 集 |
| 加權 $L^2$、Sobolev 空間 | 第 19 集；第 30 集 Sturm–Liouville（權函數） |
| 正交、畢氏定理 | 第 20–23 集：正交系統、Bessel、Parseval、投影定理 |
| $\ell^2$ 是「最重要」的例子 | 第 22–23 集：可分 Hilbert 空間都同構於 $\ell^2$ |
| Schwarz 不等式 | 第 24 集起：有界泛函、算子 |
| 複內積的慣例 | 第 33–34 集：量子力學的 bra-ket |

---

## 附：本集一句話總結

> **內積是會「共軛對稱、第一位置線性、正定」的抽象點積，它誘導出範數——三角不等式要靠 Schwarz 不等式；內積範數一定滿足平行四邊形定律，所以 $\ell^1$ 那種範數不來自內積；完備的內積空間就是 Hilbert 空間，$\ell^2$、$L^2$ 是，而有限數列、配 $L^2$ 內積的連續函數則不是。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-27 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 19:13）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.1–3.3 整理。*
