---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 20
lecture: Lecture 20
date: 2023-03-03
video: https://youtu.be/khrtd5tviZ8 （part 1）、https://youtu.be/ceidwJvy-Sw （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4，Definition 3.4.1–Theorem 3.4.8（書頁 105–111，PDF 頁 124–130）
---

# 第 20 集 · 正交系統：例子、Legendre 與 Hermite 多項式、Gram–Schmidt [▶ 影片](https://youtu.be/khrtd5tviZ8)

← 上一集：[19-weighted-sobolev-weak-convergence](19-weighted-sobolev-weak-convergence.md) ｜ [總目錄](README.md) ｜ 下一集：[21-orthonormal-sequences-fourier](21-orthonormal-sequences-fourier.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 20 集。這堂有訪客旁聽。
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 12:51，自動字幕）＋ Debnath & Mikusiński §3.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 正交系統與正規正交系統](#1-正交系統與正規正交系統)
- [2. 正交系統線性獨立](#2-正交系統線性獨立)
- [3. 正規正交數列、Kronecker δ](#3-正規正交數列kronecker-δ)
- [4. 例：ℓ² 的標準向量、複指數函數](#4-例ℓ²-的標準向量複指數函數)
- [5. 例：Legendre 多項式](#5-例legendre-多項式)
- [6. Gram–Schmidt 與 Legendre 多項式](#6-gramschmidt-與-legendre-多項式)
- [7. 例：Hermite 多項式](#7-例hermite-多項式)
- [8. Gram–Schmidt 正規正交化（一般形式）](#8-gramschmidt-正規正交化一般形式)
- [9. n 個向量的畢氏定理](#9-n-個向量的畢氏定理)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 基底 vs 正規正交基底的概念 | §3.4 開頭，p. 105 |
| 正交系統、正規正交系統 | Definition 3.4.1，p. 105 |
| 正交系統線性獨立 | Theorem 3.4.2，p. 106 |
| 正規正交數列、Kronecker δ | Definition 3.4.3，p. 106 |
| 例：$e_n$、$e^{inx}/\sqrt{2\pi}$、Legendre、Hermite | Example 3.4.4–3.4.7，pp. 106–109 |
| Gram–Schmidt | p. 110 |
| 畢氏定理（$n$ 個向量） | Theorem 3.4.8，pp. 110–111 |

開場講者跟學生討論了第 2 章作業第 9 題 (a) 的做法。[▶ 00:35](https://youtu.be/khrtd5tviZ8?t=35)

**課本的開場白**[▶ 01:52](https://youtu.be/khrtd5tviZ8?t=112)：向量空間的**基底**是線性獨立、而且用**有限**線性組合就能表示所有向量。在內積空間裡，**正規正交基底**重要得多：允許**無窮和**，並且把「線性獨立」換成「正交」。好處是：在所有重要的例子裡，正規正交基底都能具體寫出來。

【課本補充】例如 $L^2([-\pi,\pi])$ 有由簡單函數組成的**可數**正規正交基底；但它的（代數）基底一定**不可數**，而且只能證明存在、寫不出來。

---

## 1. 正交系統與正規正交系統

[▶ 02:25](https://youtu.be/khrtd5tviZ8?t=145) 課本 Definition 3.4.1。

內積空間 $E$ 中一族**非零**向量 $S$：

- 若 $S$ 中任兩個相異元素都正交（$x\perp y$），叫**正交系統（orthogonal system）**；
- 若再加上每個 $\|x\|=1$，叫**正規正交系統（orthonormal system）**。

講者說「system」這個用語讓他覺得怪，為什麼不說「集合」？他猜也許是要表示「有序」的集合；他對這個定義「有點不爽」。[▶ 04:03](https://youtu.be/khrtd5tviZ8?t=243)

**正規化**：$S$ 是正交系統，則 $S_1=\left\{\dfrac{x}{\|x\|}:x\in S\right\}$ 是正規正交系統。講者：「想要單位向量，就除以長度。」

**跟一組向量正交 ⟹ 跟它們的線性組合正交**[▶ 05:16](https://youtu.be/khrtd5tviZ8?t=316)：若 $x\perp y_j$（$j=1,\dots,n$），則

$$\left\langle x,\sum_{j=1}^nc_jy_j\right\rangle=\sum_{j=1}^n\bar c_j\langle x,y_j\rangle=0.$$

用第二位置的共軛線性。

---

## 2. 正交系統線性獨立

[▶ 07:08](https://youtu.be/khrtd5tviZ8?t=428) 課本 Theorem 3.4.2。

**定理**：正交系統是線性獨立的。

講者注意到：課本開頭說要用無窮和取代有限組合，但這裡**還是只用有限和**，「還沒兌現」。

**證明**：設 $\sum_{j=1}^nc_jy_j=0$，$y_j\in S$。跟它自己做內積：

$$0=\left\langle\sum_{i=1}^nc_iy_i,\sum_{j=1}^nc_jy_j\right\rangle=\sum_{i=1}^n\sum_{j=1}^nc_i\bar c_j\langle y_i,y_j\rangle.$$

正交性可以寫成 $\langle y_i,y_j\rangle=\|y_i\|^2\delta_{ij}$。【課堂討論】講者問 Kronecker δ 是什麼，學生答：$i=j$ 時 1、否則 0。它把雙重和「壓扁」成 $i=j$：[▶ 11:26](https://youtu.be/khrtd5tviZ8?t=686)

$$0=\sum_{i=1}^n|c_i|^2\|y_i\|^2.$$

非負項的和為 0，而 $\|y_i\|\ne0$（系統裡都是非零向量），所以每個 $c_i=0$。∎

講者【口頭】：這不是他在線性代數常用的證法；他通常拿線性組合跟某一個特定向量做內積，直接得到那個係數是 0。

> 以下**不是逐字稿內容**，是講者說的那種證法：對 $\sum c_jy_j=0$ 兩邊跟 $y_k$ 做內積，$0=\sum_jc_j\langle y_j,y_k\rangle=c_k\|y_k\|^2$，所以 $c_k=0$。

---

## 3. 正規正交數列、Kronecker δ

[▶ 13:59](https://youtu.be/khrtd5tviZ8?t=839) 課本 Definition 3.4.3。

構成正規正交系統的向量數列叫**正規正交數列（orthonormal sequence）**。正規正交可以寫成

$$\langle x_m,x_n\rangle=\delta_{mn}=\begin{cases}0, & m\ne n\\1, & m=n\end{cases} \tag{3.10}$$

應用上常用整數 $\mathbb{Z}$ 當指標。

---

## 4. 例：ℓ² 的標準向量、複指數函數

### Example 3.4.4

[▶ 16:52](https://youtu.be/khrtd5tviZ8?t=1012)

$$e_n=(0,\dots,0,1,0,\dots)\quad(\text{第 }n\text{ 位是 }1),\qquad (e_n)_j=\delta_{nj}.$$

$\{e_1,e_2,\dots\}$ 是 $\ell^2$ 中的正規正交系統。

### Example 3.4.5：複指數函數

[▶ 18:03](https://youtu.be/khrtd5tviZ8?t=1083)

$$\varphi_n(x)=\frac{e^{inx}}{\sqrt{2\pi}},\qquad n\in\mathbb{Z}$$

（$n$ 跑遍**所有**整數，不只正的）。$\{\varphi_n\}$ 是 $L^2([-\pi,\pi])$ 中的正規正交系統。

**驗證**[▶ 19:28](https://youtu.be/khrtd5tviZ8?t=1168)（講者用 $n,p$ 當指標）：取共軛把 $e^{ipx}$ 變成 $e^{-ipx}$，

$$\langle\varphi_n,\varphi_p\rangle=\frac1{2\pi}\int_{-\pi}^\pi e^{i(n-p)x}dx.$$

- $n\ne p$：
  $$=\frac{1}{2\pi}\cdot\frac{e^{i(n-p)\pi}-e^{-i(n-p)\pi}}{i(n-p)}=\frac{1}{2\pi}\cdot\frac{2i\sin((n-p)\pi)}{i(n-p)}=0,$$
  因為 $n-p$ 是整數，$\sin$ 在 $\pi$ 的整數倍是 0。【課堂討論】學生指出分子就是 $2i\sin$。
- $n=p$：被積函數是 1，$\frac1{2\pi}\cdot2\pi=1$。

講者：這是一組非常簡單的函數，「還有什麼比這更簡單？」可以用 cos、sin 寫成看起來更複雜的樣子。

---

## 5. 例：Legendre 多項式

[▶ 23:16](https://youtu.be/khrtd5tviZ8?t=1396) 課本 Example 3.4.6。

講者【口頭】：這是很多種**正交多項式**的第一個例子；它們通常都是為了解某個微分方程量身打造的。

**定義（Rodrigues 型公式）**：

$$P_0(x)=1,\qquad P_n(x)=\frac{1}{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n. \tag{3.11}$$

它們構成 $L^2([-1,1])$ 中的**正交**系統。

**正交性的證明**[▶ 25:34](https://youtu.be/khrtd5tviZ8?t=1534)：記 $p_n(x)=(x^2-1)^n$。課本的關鍵式：

$$\int_{-1}^1P_n(x)x^m\,dx=\frac{1}{2^nn!}\int_{-1}^1p_n^{(n)}(x)\,x^m\,dx. \tag{3.12}$$

講者：「他在丟一些知識給我們。」【課堂討論】他和學生一起想通：**分部積分**，$dv=p_n^{(n)}dx$、$u=x^m$。[▶ 29:19](https://youtu.be/khrtd5tviZ8?t=1759)

1. 對 $m<n$：$p_n=(x-1)^n(x+1)^n$ 在 $\pm1$ 有 $n$ 重根，所以 $p_n^{(k)}(\pm1)=0$（$k=0,\dots,n-1$）。分部積分的邊界項都是 0：
   $$\int_{-1}^1p_n^{(n)}x^m\,dx=-m\int_{-1}^1p_n^{(n-1)}x^{m-1}dx.$$
2. 重複 $m$ 次：
   $$=(-1)^mm!\int_{-1}^1p_n^{(n-m)}dx=(-1)^mm!\Big[p_n^{(n-m-1)}\Big]_{-1}^1=0.$$
   （學生指出要做到最後一步，講者一度數錯階數。）[▶ 32:57](https://youtu.be/khrtd5tviZ8?t=1977)
3. 所以 $\langle P_n,x^m\rangle=0$ 對 $m<n$（3.13）。講者：「這是什麼意思？$P_n$ 跟 $x^m$ 的內積是 0。」
4. $P_m$ 是 $m$ 次多項式，是 $1,x,\dots,x^m$ 的線性組合，所以 $m<n$ 時 $\langle P_n,P_m\rangle=0$（3.14）。∎

**正規化**[▶ 36:43](https://youtu.be/khrtd5tviZ8?t=2203)：課本最後給出 $\|P_n\|^2=\frac{2}{2n+1}$，所以

$$\sqrt{n+\tfrac12}\,P_n(x)$$

構成正規正交系統。講者驗證 $n=0$：$\hat P_0=\frac{1}{\sqrt2}$，$\int_{-1}^1\frac12dx=1$ ✓。

講者注意到課本沒有列出 $P_n$ 的具體公式，「有前十個的清單會讓我今天好過一點」。

> 以下**不是逐字稿內容**，是從 (3.11) 算出的前幾個：$P_0=1$，$P_1=x$，$P_2=\frac12(3x^2-1)$，$P_3=\frac12(5x^3-3x)$。

【課本補充】$\|P_n\|^2$ 的計算（pp. 107–108）：分部積分得 $\int_{-1}^1(1-x^2)^ndx=\frac{2^{2n+1}(n!)^2}{(2n)!(2n+1)}$，以及 $\int(p_n^{(n)})^2=(2n)!\int(1-x)^n(1+x)^ndx$（$p_n^{(2n)}=(2n)!$），合起來得 $\frac{2}{2n+1}$。

---

## 6. Gram–Schmidt 與 Legendre 多項式

【口頭】[▶ 35:29](https://youtu.be/khrtd5tviZ8?t=2129) 講者說他平常是這樣「發現」Legendre 多項式的：

從單項式 $\{1,x,x^2,x^3,\dots\}$ 出發，在 $L^2([-1,1])$ 的內積下做 **Gram–Schmidt**。

1. $\hat P_0=\frac1{\sqrt2}$（正規化 1）。
2. $\tilde P_1=x-\langle x,\hat P_0\rangle\hat P_0$。$\langle x,\hat P_0\rangle=\frac1{\sqrt2}\int_{-1}^1x\,dx=0$（奇函數），所以 $\tilde P_1=x$。課本 $P_1=\frac12\frac{d}{dx}(x^2-1)=x$，一樣。
3. $\tilde P_2=x^2-\langle x^2,\hat P_1\rangle\hat P_1-\langle x^2,\hat P_0\rangle\hat P_0$。講者解釋 Gram–Schmidt 就是「一直減掉不想要的部分」，也就是減掉在已經正交化的方向上的**投影（影子）**。[▶ 41:54](https://youtu.be/khrtd5tviZ8?t=2514)
   - $\langle x^2,\hat P_1\rangle\propto\int x^3=0$。
   - $\langle x^2,\hat P_0\rangle=\frac1{\sqrt2}\int_{-1}^1x^2dx=\frac{2}{3\sqrt2}$。
   - 所以 $\tilde P_2=x^2-\frac{2}{3\sqrt2}\cdot\frac1{\sqrt2}=x^2-\frac13$。

**跟課本比**[▶ 44:46](https://youtu.be/khrtd5tviZ8?t=2686)：課本

$$P_2=\frac18\frac{d^2}{dx^2}(x^2-1)^2=\frac32x^2-\frac12=\frac32\left(x^2-\frac13\right).$$

講者說：「它們不一樣」，用生成公式的「黑魔法」造的，跟直接對單項式做 Gram–Schmidt 造的「不是同樣的多項式」。

> 以下**不是逐字稿內容**，是依計算推論的：兩者只差一個**常數倍** $\frac32$，方向相同，都跟 $1,x$ 正交。Gram–Schmidt 每一步的方向是唯一確定的（只差常數倍）；兩者差別只在**正規化方式**：Gram–Schmidt 版本首項係數是 1（或正規化成長度 1），課本的 Legendre 多項式則是正規化成 $P_n(1)=1$。

講者的解釋【口頭】[▶ 47:22](https://youtu.be/khrtd5tviZ8?t=2842)：(3.13) 說 $P_n$ 跟 $1,x,\dots,x^{n-1}$ 都正交。Gram–Schmidt 是從 $x^n$ 減掉在**已正交化的**方向上的影子，不是直接減在 $1,x,\dots$ 上的。兩種方法是「從不同角度到同一個目標」：為 $L^2([-1,1])$ 造正規正交系統。（是不是**基底**？講者說還不知道，但確定是正規正交**系統**。）

**單項式本身不正交**[▶ 49:36](https://youtu.be/khrtd5tviZ8?t=2976)：$\langle x,x^3\rangle=\int_{-1}^1x^4\ne0$。但次數和為奇數時內積是 0（奇函數積分），所以**相鄰**的 $x^n,x^{n+1}$ 正交，隔一個的就不正交（例如 $\langle1,x^2\rangle=\int x^2\ne0$）。

---

## 7. 例：Hermite 多項式

[▶ 51:46](https://youtu.be/khrtd5tviZ8?t=3106) 課本 Example 3.4.7。

$$H_n(x)=(-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2}. \tag{3.18}$$

講者先懷疑「這不是多項式吧」，後來想通：微分 $e^{-x^2}$ 每次都產生 $e^{-x^2}$ 乘多項式，乘上 $e^{x^2}$ 就消掉，剩下多項式。

$$\varphi_n(x)=e^{-x^2/2}H_n(x)$$

構成 $L^2(\mathbb{R})$ 中的**正交**系統。

**正交性**[▶ 54:15](https://youtu.be/khrtd5tviZ8?t=3255)：

$$\langle\varphi_n,\varphi_m\rangle=(-1)^{n+m}\int_{-\infty}^\infty e^{x^2}\frac{d^n}{dx^n}e^{-x^2}\frac{d^m}{dx^m}e^{-x^2}dx.$$

講者描述（沒寫出）：反覆分部積分，把導數移過去；每次的邊界項都含 $e^{-x^2}$ 乘多項式，在 $\pm\infty$ 是 0（$x^ke^{-x^2}\to0$）。外面那個 $e^{x^2}$ 雖然會爆，但總有至少兩個 $e^{-x^2}$ 跟它抗衡。所以 $n\ne m$ 時內積是 0。

**正規化**[▶ 57:42](https://youtu.be/khrtd5tviZ8?t=3462)：講者說課本做了一個代數小技巧，然後「分部積分 $n$ 次」——「哪個分部積分？」他沒弄清楚，說「就讓它暫時保持神秘」。結果是

$$\|\varphi_n\|^2=2^nn!\sqrt\pi, \tag{3.21}$$

所以

$$\psi_n(x)=\frac{1}{\sqrt{2^nn!\sqrt\pi}}\,e^{-x^2/2}H_n(x)$$

構成正規正交系統。[▶ part 2 02:43](https://youtu.be/ceidwJvy-Sw?t=163)

【課本補充】正規化的那一步：$\|\varphi_n\|^2=\int e^{-x^2}H_n^2=\int e^{x^2}\left(\frac{d^n}{dx^n}e^{-x^2}\right)^2dx$。分部積分 $n$ 次（把一個 $\frac{d^n}{dx^n}e^{-x^2}$ 的導數全移到另一個因子 $e^{x^2}\frac{d^n}{dx^n}e^{-x^2}$ 上），得

$$\|\varphi_n\|^2=(-1)^n\int\frac{d^n}{dx^n}\left[e^{x^2}\frac{d^n}{dx^n}e^{-x^2}\right]e^{-x^2}dx.$$

方括號裡是 $(-1)^nH_n=(-2x)^n+\cdots$（$n$ 次多項式），它的 $n$ 階導數是常數 $(-1)^n2^nn!$。所以 $\|\varphi_n\|^2=2^nn!\int e^{-x^2}dx=2^nn!\sqrt\pi$。

**跟量子力學的關係**【口頭】[▶ part 2 03:16](https://youtu.be/ceidwJvy-Sw?t=196)：講者說這些計算很嚇人，但解 Schrödinger 方程時一定會碰到。學生記得 Griffiths 的量子力學課本在推導（諧振子）時提到 Hermite 多項式；講者補充：Legendre 多項式出現在**氫原子**。

講者也說：課本用「生成公式」定義 Legendre 和 Hermite 多項式，非常精簡；但應用上它們可能不是這樣自然出現的。[▶ part 2 04:25](https://youtu.be/ceidwJvy-Sw?t=265)

---

## 8. Gram–Schmidt 正規正交化（一般形式）

[▶ part 2 04:25](https://youtu.be/ceidwJvy-Sw?t=265) 課本 p. 110。

課本：上面的例子原本就正交，只要正規化。其實只要原本的數列**線性獨立**（不必正交），就能變成正規正交數列，方法叫 **Gram–Schmidt 正規正交化**。講者：「Gram 和 Schmidt 是兩個人——Jørgen Pedersen Gram（1850–1916）和 Erhard Schmidt（1876–1959），我以前不知道他們的名字。」

給線性獨立的 $(y_n)$，歸納定義：

$$w_1=y_1,\quad x_1=\frac{w_1}{\|w_1\|};\qquad w_k=y_k-\sum_{n=1}^{k-1}\langle y_k,x_n\rangle x_n,\quad x_k=\frac{w_k}{\|w_k\|}\quad(k\ge2).$$

講者：這正是他剛才對 Legendre 多項式做的公式；$\langle y_k,x_n\rangle x_n$ 就是 $y_k$ 在 $x_n$ 方向上的**正交投影**。課本用歸納法證 $(w_n)$ 正交，講者讓學生自己讀。

【課本補充】歸納的關鍵：設 $w_1,\dots,w_{k-1}$ 兩兩正交，對 $m<k$，
$$\langle w_k,w_m\rangle=\langle y_k,w_m\rangle-\frac{\langle y_k,w_m\rangle\langle w_m,w_m\rangle}{\|w_m\|^2}=0.$$
而且 $\operatorname{span}\{x_1,\dots,x_n\}=\operatorname{span}\{y_1,\dots,y_n\}$ 對每個 $n$。（線性獨立保證 $w_k\ne0$，能除。）

---

## 9. n 個向量的畢氏定理

[▶ part 2 08:29](https://youtu.be/ceidwJvy-Sw?t=509) 課本 Theorem 3.4.8。

**定理**：$x_1,\dots,x_n$ 兩兩正交，則

$$\left\|\sum_{k=1}^nx_k\right\|^2=\sum_{k=1}^n\|x_k\|^2. \tag{3.22}$$

**證明**（講者的版本，直接展開）：兩個和用不同的指標（講者強調這很重要）：

$$\left\langle\sum_{k=1}^nx_k,\sum_{j=1}^nx_j\right\rangle=\sum_{k=1}^n\sum_{j=1}^n\langle x_k,x_j\rangle=\sum_{j=1}^n\|x_j\|^2,$$

因為 $k\ne j$ 時 $\langle x_k,x_j\rangle=0$。∎

（課本用歸納法：把前 $n-1$ 項的和當一個向量，它跟 $x_n$ 正交，套兩個向量的畢氏定理。）

**下一堂**：Bessel 等式與不等式。講者說這節比他以為的長很多，今天停在這裡。下次前請收尾第 2 章作業；他會盡量準備好第一次考試（涵蓋第 1、2 章）的複習單。[▶ part 2 11:33](https://youtu.be/ceidwJvy-Sw?t=693)

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 正交系統 | 非零、兩兩正交；再加 $\|x\|=1$ 為正規正交 | 正規化 $x/\|x\|$ |
| 跟組合正交 | $x\perp y_j$ ⟹ $x\perp\sum c_jy_j$ | 第二位置共軛線性 |
| 線性獨立 | 正交系統線性獨立 | $\|\sum c_iy_i\|^2=\sum|c_i|^2\|y_i\|^2$ |
| Kronecker | $\langle x_m,x_n\rangle=\delta_{mn}$ | |
| $\ell^2$ | $e_n$ 正規正交 | |
| 複指數 | $\frac{e^{inx}}{\sqrt{2\pi}}$，$n\in\mathbb{Z}$，在 $L^2([-\pi,\pi])$ | $\int_{-\pi}^\pi e^{ikx}=0$（$k\ne0$） |
| Legendre | $P_n=\frac1{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n$，$\|P_n\|^2=\frac2{2n+1}$ | $p_n^{(k)}(\pm1)=0$；分部積分 $m$ 次 ⟹ $\langle P_n,x^m\rangle=0$ |
| Gram–Schmidt 版 | $1,x,x^2-\frac13,\dots$ | 跟 $P_n$ 只差常數倍 |
| Hermite | $H_n=(-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2}$，$\varphi_n=e^{-x^2/2}H_n$ | $\|\varphi_n\|^2=2^nn!\sqrt\pi$ |
| Gram–Schmidt | $w_k=y_k-\sum_{n<k}\langle y_k,x_n\rangle x_n$，$x_k=w_k/\|w_k\|$ | 減掉投影；span 不變 |
| 畢氏 | $\|\sum x_k\|^2=\sum\|x_k\|^2$ | 雙重和只剩對角項 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Bessel 不等式、廣義 Fourier 級數 | 第 21 集 |
| 正規正交數列弱收斂到 0 | 第 21 集（兌現第 19 集的承諾） |
| 複指數函數、三角函數 | 第 21–22 集：Fourier 級數、完備性 |
| Legendre、Hermite | 第 30 集：Sturm–Liouville；第 33–34 集：量子力學 |
| Gram–Schmidt | 第 23 集：可分 Hilbert 空間有可數正規正交基底 |

---

## 附：本集一句話總結

> **正交系統自動線性獨立；$\ell^2$ 的 $e_n$、$L^2([-\pi,\pi])$ 的 $e^{inx}/\sqrt{2\pi}$、$L^2([-1,1])$ 的 Legendre 多項式、$L^2(\mathbb{R})$ 的 Hermite 函數都是正交系統，正交性都靠積分（往往是反覆分部積分）驗證；而任何線性獨立的數列，都能用 Gram–Schmidt「減掉投影再正規化」變成正規正交——對單項式做，得到的就是（差常數倍的）Legendre 多項式。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-03 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 12:51）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4 整理。*
