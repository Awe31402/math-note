---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 21
lecture: Lecture 21
date: 2023-03-06
video: https://youtu.be/79SK7YY1fzo （part 1）、https://youtu.be/vDg-M1YmLCk （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4，Theorem 3.4.9–Definition 3.4.13（書頁 111–114，PDF 頁 130–133）
---

# 第 21 集 · Bessel 不等式、廣義 Fourier 級數、正規正交基底 [▶ 影片](https://youtu.be/79SK7YY1fzo)

← 上一集：[20-orthogonal-systems](20-orthogonal-systems.md) ｜ [總目錄](README.md) ｜ 下一集：[22-orthonormal-basis-parseval](22-orthonormal-basis-parseval.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 21 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 20:33，自動字幕）＋ Debnath & Mikusiński §3.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Bessel 等式與不等式](#1-bessel-等式與不等式)
- [2. 幾何意義：投影與最佳逼近](#2-幾何意義投影與最佳逼近)
- [3. 正規正交數列弱收斂到 0，但不強收斂](#3-正規正交數列弱收斂到-0但不強收斂)
- [4. 廣義 Fourier 級數](#4-廣義-fourier-級數)
- [5. Theorem 3.4.10：Σαₙxₙ 收斂 ⟺ Σ|αₙ|² < ∞](#5-theorem-3410σαₙxₙ-收斂--σαₙ²--)
- [6. 收斂但收斂到錯的東西](#6-收斂但收斂到錯的東西)
- [7. 完備的正規正交數列](#7-完備的正規正交數列)
- [8. 正規正交基底](#8-正規正交基底)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Bessel 等式與不等式 | Theorem 3.4.9，pp. 111–112 |
| 最佳逼近；正規正交數列弱收斂到 0 | p. 112 |
| 廣義 Fourier 級數 | (3.27)，p. 112 |
| $\sum\alpha_nx_n$ 收斂 ⟺ $\sum|\alpha_n|^2<\infty$ | Theorem 3.4.10，pp. 112–113 |
| 收斂到錯的元素 | Example 3.4.11，p. 113 |
| 完備的正規正交數列、正規正交基底 | Definition 3.4.12–3.4.13，pp. 113–114 |

講者說上次證過 $n$ 個向量的畢氏定理（「很簡單，你們自己也會」），今天從 Bessel 開始。[▶ 00:34](https://youtu.be/79SK7YY1fzo?t=34)

---

## 1. Bessel 等式與不等式

[▶ 01:15](https://youtu.be/79SK7YY1fzo?t=75) 課本 Theorem 3.4.9。

**定理**：$x_1,\dots,x_n$ 是內積空間 $E$ 中的正規正交集，則對每個 $x\in E$：

$$\left\|x-\sum_{k=1}^n\langle x,x_k\rangle x_k\right\|^2=\|x\|^2-\sum_{k=1}^n|\langle x,x_k\rangle|^2, \tag{3.23}$$

$$\sum_{k=1}^n|\langle x,x_k\rangle|^2\le\|x\|^2. \tag{3.24}$$

講者：「我們終於說正規正交**集**了，真希望我們有定義它。」

**Step 1：畢氏定理。**[▶ 03:48](https://youtu.be/79SK7YY1fzo?t=228) 對任意複數 $\alpha_1,\dots,\alpha_n$，因為 $x_k$ 正規正交，

$$\left\|\sum_{k=1}^n\alpha_kx_k\right\|^2=\sum_{k=1}^n\|\alpha_kx_k\|^2=\sum_{k=1}^n|\alpha_k|^2.$$

**Step 2：直接展開。**[▶ 04:24](https://youtu.be/79SK7YY1fzo?t=264) 講者先用自己的方法：令 $\alpha_k=\langle x,x_k\rangle$，展開（兩個和用不同指標 $k,j$）：

$$\begin{aligned}\left\|x-\sum_k\alpha_kx_k\right\|^2&=\langle x,x\rangle-\sum_j\bar\alpha_j\langle x,x_j\rangle-\sum_k\alpha_k\langle x_k,x\rangle+\sum_k\sum_j\alpha_k\bar\alpha_j\langle x_k,x_j\rangle.\end{aligned}$$

- $\langle x,x_j\rangle=\alpha_j$，所以第二項是 $\sum_j|\alpha_j|^2$；
- $\langle x_k,x\rangle=\bar\alpha_k$，所以第三項也是 $\sum_k|\alpha_k|^2$；
- $\langle x_k,x_j\rangle=\delta_{kj}$，最後一項壓成 $\sum_k|\alpha_k|^2$。

（講者中途搞混了 $j,k$，後來改正；也抱怨隔壁一群女生在嘻笑，「像在夏令營」。）

$$=\|x\|^2-2\sum_j|\alpha_j|^2+\sum_j|\alpha_j|^2=\|x\|^2-\sum_j|\langle x,x_j\rangle|^2.$$

這就是 (3.23)。

**Step 3：不等式。**[▶ 10:47](https://youtu.be/79SK7YY1fzo?t=647) 講者先想用反向三角不等式，繞了一圈後說：「我太用力了。」(3.23) 左邊是**範數的平方**，所以 $\ge0$：

$$0\le\|x\|^2-\sum_{k=1}^n|\langle x,x_k\rangle|^2,$$

移項即 (3.24)。∎

【課本補充】課本的證法：對**任意** $\alpha_k$ 展開，得

$$\left\|x-\sum_k\alpha_kx_k\right\|^2=\|x\|^2-\sum_k|\langle x,x_k\rangle|^2+\sum_k|\langle x,x_k\rangle-\alpha_k|^2, \tag{3.25}$$

再取 $\alpha_k=\langle x,x_k\rangle$。講者說：「他用了不同的方法推，隨便啦，都行。」[▶ 17:13](https://youtu.be/79SK7YY1fzo?t=1033)

---

## 2. 幾何意義：投影與最佳逼近

【口頭】[▶ 13:43](https://youtu.be/79SK7YY1fzo?t=823)

- $x_1,\dots,x_n$ 不一定是基底，只是正規正交集。
- $\sum\langle x,x_k\rangle x_k$ 是把 $x$ 在 $\operatorname{span}\{x_1,\dots,x_n\}$ 方向上的分量挑出來。如果它們是基底，就拿回整個 $x$。
- **跟 Gram–Schmidt 的關係**：若 $x\notin\operatorname{span}\{x_1,\dots,x_n\}$，令 $y=x-\sum\langle x,x_k\rangle x_k$。則 $y$ 跟所有 $x_k$ 正交，$\{x_1,\dots,x_n,y/\|y\|\}$ 是更大的正規正交系統——這正是 Gram–Schmidt 的下一步。若 $x$ 已經在 span 裡，就把 $x$ 寫回成基底的線性組合。

**最佳逼近**[▶ 17:13](https://youtu.be/79SK7YY1fzo?t=1033)：由 (3.25)，最後一項 $\sum|\langle x,x_k\rangle-\alpha_k|^2\ge0$，所以 $\|x-\sum\alpha_kx_k\|$ 在 $\alpha_k=\langle x,x_k\rangle$ 時**最小**。也就是：

> 用 $x_1,\dots,x_n$ 的線性組合逼近 $x$，最好的係數是 $\alpha_k=\langle x,x_k\rangle$。

講者說這是在論證**最小平方法**。課本說：正規正交系統的這個性質，是很多逼近技術的基礎。

---

## 3. 正規正交數列弱收斂到 0，但不強收斂

[▶ 19:49](https://youtu.be/79SK7YY1fzo?t=1189)

若 $(x_n)$ 是正規正交**數列**，在 (3.24) 中令 $n\to\infty$：

$$\sum_{k=1}^\infty|\langle x,x_k\rangle|^2\le\|x\|^2. \tag{3.26}$$

講者先想到用上一集「弱收斂有界」那類深的定理，然後說：「我們不需要深魔法……這很尷尬。」[▶ 22:27](https://youtu.be/79SK7YY1fzo?t=1347) 右邊有限，所以左邊的級數**收斂**；由**第 $n$ 項檢驗**，

$$|\langle x,x_k\rangle|^2\to0\quad\Longrightarrow\quad\langle x,x_k\rangle\to0.$$

（複數數列的模趨近 0 ⟺ 它本身趨近 0。）這對每個 $x$ 成立，所以

$$x_n\xrightarrow{w}0.$$

**正規正交數列弱收斂到 0。**（第 19 集說的弱不推強的例子就在這裡。）

**不強收斂**[▶ 24:13](https://youtu.be/79SK7YY1fzo?t=1453)：課本：「另一方面，因為 $\|x_n\|=1$，正規正交數列不強收斂。」

【課堂討論】講者想用三角不等式說明：若 $x_n\to x$，$\big|\|x_n\|-\|x\|\big|\le\|x_n-x\|\to0$，所以 $\|x\|=1$……他看例子 $e^{inx}/\sqrt{2\pi}$ 覺得直觀上懂，但說不出「為什麼 $\|x_n\|=1$ 就禁止強收斂」，「如果你們想到了再告訴我」，往下走。[▶ 30:47](https://youtu.be/79SK7YY1fzo?t=1847)

> 以下**不是逐字稿內容**，是補上的兩種理由：
>
> 1. **極限只能是 0，但範數是 1**：若 $x_n\to x$ 強收斂，則也弱收斂到 $x$。但已知 $x_n\xrightarrow{w}0$。弱極限唯一（若 $\langle x,y\rangle=\langle0,y\rangle=0$ 對所有 $y$，取 $y=x$ 得 $x=0$），所以 $x=0$。可是強收斂推出 $\|x_n\|\to\|x\|=0$，跟 $\|x_n\|=1$ 矛盾。（講者的三角不等式那步推出 $\|x\|=1$，正好跟 $x=0$ 衝突。）
> 2. **不是 Cauchy**：$m\ne n$ 時由畢氏定理 $\|x_n-x_m\|^2=\|x_n\|^2+\|x_m\|^2=2$，任兩項距離都是 $\sqrt2$。

---

## 4. 廣義 Fourier 級數

[▶ 31:33](https://youtu.be/79SK7YY1fzo?t=1893) 課本 (3.27)。

(3.26) 說 $\sum|\langle x,x_k\rangle|^2$ 收斂，也就是數列 $(\langle x,x_n\rangle)_n\in\ell^2$。所以**正規正交數列誘導一個從 $E$ 到 $\ell^2$ 的映射**。

**廣義 Fourier 級數（generalized Fourier series）**：

$$x\sim\sum_{n=1}^\infty\langle x,x_n\rangle x_n. \tag{3.27}$$

$\alpha_n=\langle x,x_n\rangle$ 叫 $x$ 對 $(x_n)$ 的**廣義 Fourier 係數**。Fourier（1768–1830）。

講者【口頭】[▶ 34:34](https://youtu.be/79SK7YY1fzo?t=2074)：$\sum_{k=1}^n\langle x,x_k\rangle x_k$ 是第 $n$ 個「Fourier 近似」；Bessel 等式**明確給出**它的誤差，而且被 $\|x\|$ 控制。他說他一開始是用有限維的角度想，但其實不只如此。「我愛這些東西……只要知道內積怎麼運作，大部分都能直接算出來，真的很酷。」

課本：這組係數對任何有限個 $x_n$ 給出最佳逼近。但一般**不知道**級數 (3.27) 收不收斂；下一個定理說，空間**完備**就保證收斂。

---

## 5. Theorem 3.4.10：Σαₙxₙ 收斂 ⟺ Σ|αₙ|² < ∞

[▶ 38:31](https://youtu.be/79SK7YY1fzo?t=2311)

**定理**：$(x_n)$ 是 **Hilbert 空間** $H$ 中的正規正交數列，$(\alpha_n)$ 是複數列。則

$$\sum_{n=1}^\infty\alpha_nx_n\ \text{收斂}\iff\sum_{n=1}^\infty|\alpha_n|^2<\infty,$$

而且這時

$$\left\|\sum_{n=1}^\infty\alpha_nx_n\right\|^2=\sum_{n=1}^\infty|\alpha_n|^2. \tag{3.28}$$

講者：「這不意外，這基本上是無限版的畢氏定理。」

**關鍵式**[▶ 40:37](https://youtu.be/79SK7YY1fzo?t=2437)：對 $m>k>0$，由畢氏定理

$$\left\|\sum_{n=k}^m\alpha_nx_n\right\|^2=\sum_{n=k}^m|\alpha_n|^2. \tag{3.29}$$

講者：我們在看級數的**尾巴**，這是典型論證；要想辦法用到空間的完備性。

**(⟸)**：令 $s_m=\sum_{n=1}^m\alpha_nx_n$。若 $\sum|\alpha_n|^2<\infty$，(3.29) 右邊是收斂級數的一段尾巴，能任意小，所以 $(s_m)$ 是 Cauchy 數列。【課堂討論】學生補上：$H$ 完備，所以 $s_m$ 收斂。[▶ 43:56](https://youtu.be/79SK7YY1fzo?t=2636)

**(⟹)**[▶ 47:28](https://youtu.be/79SK7YY1fzo?t=2848)：若 $\sum\alpha_nx_n$ 收斂，課本說 (3.29) 推出 $\sum|\alpha_n|^2$ 收斂，「因為 $\sigma_m=\sum_{n=1}^m|\alpha_n|^2$ 是 $\mathbb{R}$ 中的 Cauchy 數列」。

講者不懂為什麼要扯到實數的完備性：「這個收斂就表示範數收斂，範數的平方也收斂，所以這就是我們要證的。」學生解釋：複數的模是實數。講者：「我同意，但他看的是部分和 $\sigma_m$……我不認為我有貢獻什麼，往下走。」[▶ 52:08](https://youtu.be/79SK7YY1fzo?t=3128)

> 以下**不是逐字稿內容**，是兩種證法的說明：
>
> - **課本的證法**：$s_m$ 收斂 ⟹ $(s_m)$ 是 Cauchy ⟹ 由 (3.29)，$\sigma_m-\sigma_{k-1}=\|s_m-s_{k-1}\|^2$ 能任意小 ⟹ $(\sigma_m)$ 是 $\mathbb{R}$ 中的 Cauchy 數列 ⟹（$\mathbb{R}$ 完備）收斂。
> - **講者的直覺也對**：由有限畢氏定理 $\|s_m\|^2=\sigma_m$。$s_m\to s$ 而範數連續（第 19 集），所以 $\sigma_m=\|s_m\|^2\to\|s\|^2$，收斂。這同時也證了 (3.28)。兩種都行，第二種更短。

**(3.28)**：在 (3.29) 取 $k=1$、令 $m\to\infty$。講者：「我覺得每個部分我都在做這件事，所以一定是我沒看清楚什麼。」他的總結：問題在**收斂**——給定左邊收斂，怎麼知道右邊收斂，上面那些論證就在處理這個。[▶ 53:16](https://youtu.be/79SK7YY1fzo?t=3196)

**要點**【口頭】[▶ 52:40](https://youtu.be/79SK7YY1fzo?t=3160)：在 Hilbert 空間裡，用正規正交數列寫的級數 $\sum\alpha_nx_n$ 收斂，**若且唯若**係數平方可和。

---

## 6. 收斂但收斂到錯的東西

[▶ 53:48](https://youtu.be/79SK7YY1fzo?t=3228) 課本 Example 3.4.11。

由 Theorem 3.4.10 和 (3.26)，在 Hilbert 空間中 $\sum\langle x,x_n\rangle x_n$ 對每個 $x$ 都收斂。但**可能收斂到不是 $x$ 的元素**。

$H=L^2([-\pi,\pi])$，$x_n(t)=\frac{1}{\sqrt\pi}\sin nt$（$n=1,2,\dots$），是正規正交集。取 $x(t)=\cos t$：

$$\sum_{n=1}^\infty\langle x,x_n\rangle x_n(t)=\sum_{n=1}^\infty\left(\frac1{\sqrt\pi}\int_{-\pi}^\pi\cos t\sin nt\,dt\right)\frac{\sin nt}{\sqrt\pi}=\sum_{n=1}^\infty0\cdot\sin nt=0\ne\cos t.$$

講者：被積函數是偶函數乘奇函數 = 奇函數，在對稱區間上積分為 0。[▶ 56:16](https://youtu.be/79SK7YY1fzo?t=3376)

講者：級數**收斂**，但「做得很差」——收斂不代表是好的逼近。Bessel 等式照樣成立，只是級數是零級數，變成「$\|\cos\|^2=\|\cos\|^2$，耶，對啦，誰在乎」。[▶ 57:56](https://youtu.be/79SK7YY1fzo?t=3476)

（原因：$\{\sin nt\}$ 少了 cos 那一半，不夠「完整」。）

---

## 7. 完備的正規正交數列

[▶ part 2 01:23](https://youtu.be/vDg-M1YmLCk?t=83) 課本 Definition 3.4.12。

**定義**：$E$ 中的正規正交數列 $(x_n)$ 叫**完備（complete）**，如果對每個 $x\in E$，

$$x=\sum_{n=1}^\infty\langle x,x_n\rangle x_n. \tag{3.30}$$

講者覺得「complete」這個詞用在這裡很糟（跟空間的完備撞名）。上面的 $\{\sin nt/\sqrt\pi\}$ 就**不完備**，因為 $\cos t\in L^2$ 卻表示不出來。

**等號的意思**[▶ part 2 02:33](https://youtu.be/vDg-M1YmLCk?t=153)：右邊是無窮級數，所以 (3.30) 是指

$$\lim_{n\to\infty}\left\|x-\sum_{k=1}^n\langle x,x_k\rangle x_k\right\|=0,$$

也就是**部分和按範數收斂到 $x$**。

**在 $L^2([-\pi,\pi])$ 中**[▶ part 2 04:00](https://youtu.be/vDg-M1YmLCk?t=240)：$f=\sum\langle f,f_n\rangle f_n$ 的意思是

$$\lim_{n\to\infty}\int_{-\pi}^\pi\left|f(t)-\sum_{k=1}^n\alpha_kf_k(t)\right|^2dt=0,\qquad\alpha_k=\int_{-\pi}^\pi f(t)\overline{f_k(t)}dt.$$

課本：這一般**不**推出逐點收斂，所以不能說 $f(x)=\sum\alpha_nf_n(x)$。

講者的解釋【口頭】[▶ part 2 07:16](https://youtu.be/vDg-M1YmLCk?t=436)：積分只能給「幾乎處處」相等；所以對 $L^2$ 函數算出 Fourier 係數，級數在「大部分地方」吻合，但「可能有有限個點不吻合」。

> 以下**不是逐字稿內容**，是依第 2 章推論的補充：$L^2$ 範數收斂一般連「幾乎處處」都推不出來（第 14 集的打字機數列是 $L^1$ 版本的例子），只能保證**某個子數列**幾乎處處收斂（Theorem 2.8.2 的類比）。不吻合的點也不一定是有限個，只能說是零集。

---

## 8. 正規正交基底

[▶ part 2 08:24](https://youtu.be/vDg-M1YmLCk?t=504) 課本 Definition 3.4.13。

**定義**：內積空間 $E$ 中的正規正交系統 $B$ 叫**正規正交基底（orthonormal basis）**，如果每個 $x\in E$ 都有**唯一**的表示

$$x=\sum_{n=1}^\infty\alpha_nx_n,\qquad\alpha_n\in\mathbb{C},\ x_n\text{ 是 }B\text{ 中相異元素}.$$

講者【口頭】[▶ part 2 10:24](https://youtu.be/vDg-M1YmLCk?t=624)：線性代數的基底是「生成集」，但用的是**有限**線性組合；這裡不再假設有限，把「生成」推廣到**級數**。這就是開頭說的「無窮和取代有限組合」終於兌現。

**完備的正規正交數列是正規正交基底**[▶ part 2 11:34](https://youtu.be/vDg-M1YmLCk?t=694)：講者說這可能是全書最重要的一節，很長。表示的存在就是「完備」的定義，所以只要證**唯一**。

講者的證法：設 $x=\sum\alpha_kx_k$。$s_n=\sum_{k\le n}\langle x,x_k\rangle x_k\to x$，$s_n^\alpha=\sum_{k\le n}\alpha_kx_k\to x$，所以

$$s_n-s_n^\alpha=\sum_{k=1}^n\big(\langle x,x_k\rangle-\alpha_k\big)x_k\to0,\qquad\text{故}\quad\sum_{k=1}^n|\langle x,x_k\rangle-\alpha_k|^2\to0$$

（畢氏定理）。非負項的和趨近 0，每項都要是 0：$\alpha_k=\langle x,x_k\rangle$。

講者又說：其實有更「低科技」的看法——係數公式 $\langle x,x_k\rangle$ 本來就由 $x$ 和數列決定，沒什麼好爭的；「數學家喜歡在不必要的地方證唯一性……也許數學家都是千禧世代，想要獨一無二。」[▶ part 2 18:25](https://youtu.be/vDg-M1YmLCk?t=1105)

> 以下**不是逐字稿內容**，是說明為什麼唯一性證明不是多餘的：定義裡的表示 $x=\sum\alpha_nx_n$ 是**任意**係數，不是預先規定 $\alpha_n=\langle x,x_n\rangle$。要證的是：只要能這樣寫，係數就**必定**是 $\langle x,x_n\rangle$。快一點的證法：$\langle\cdot,x_k\rangle$ 連續，所以 $\langle x,x_k\rangle=\lim_n\langle s_n^\alpha,x_k\rangle=\alpha_k$。

【課本補充】課本的證法（$\alpha$、$\beta$ 兩種表示）：由 Theorem 3.4.10，$0=\|x-x\|^2=\left\|\sum(\alpha_n-\beta_n)x_n\right\|^2=\sum|\alpha_n-\beta_n|^2$，所以 $\alpha_n=\beta_n$。另外：完備正規正交數列的有限線性組合 $\operatorname{span}\{x_1,x_2,\dots\}$ 在 $E$ 中稠密。

**考試與其他**[▶ 59:10](https://youtu.be/79SK7YY1fzo?t=3550)：時間太晚了；下次不能拖堂（講者要去教會）。第一次考試時間在討論：可能春假後的週一，或這週五。講者也提到想開始講 Lie 代數（跟一位學生的另一個計畫）。

**動機**【口頭】[▶ part 2 19:33](https://youtu.be/vDg-M1YmLCk?t=1173)：我們越來越接近應用。這些 Fourier 係數的積分，就是解**波動方程**時要算的：給定波的初始形狀，算出係數，用 sin 和 cos 的和來模擬波。「我們在打造一台機器，用來分析這類問題的分析學議題。」

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| Bessel 等式 | $\|x-\sum\langle x,x_k\rangle x_k\|^2=\|x\|^2-\sum|\langle x,x_k\rangle|^2$ | 展開；$\langle x_k,x_j\rangle=\delta_{kj}$ |
| Bessel 不等式 | $\sum|\langle x,x_k\rangle|^2\le\|x\|^2$ | 左邊是範數平方 $\ge0$ |
| 最佳逼近 | $\alpha_k=\langle x,x_k\rangle$ 使 $\|x-\sum\alpha_kx_k\|$ 最小 | (3.25) 多一項 $\sum|\langle x,x_k\rangle-\alpha_k|^2$ |
| 弱收斂到 0 | 正規正交數列 $x_n\xrightarrow{w}0$ | 無窮 Bessel + 第 $n$ 項檢驗 |
| 不強收斂 | $\|x_n-x_m\|=\sqrt2$ | 或：極限必為 0 卻 $\|x_n\|=1$ |
| 廣義 Fourier 級數 | $x\sim\sum\langle x,x_n\rangle x_n$；係數 $\in\ell^2$ | |
| Thm 3.4.10 | Hilbert 空間：$\sum\alpha_nx_n$ 收斂 ⟺ $\sum|\alpha_n|^2<\infty$；$\|\sum\alpha_nx_n\|^2=\sum|\alpha_n|^2$ | $\|\sum_k^m\alpha_nx_n\|^2=\sum_k^m|\alpha_n|^2$；完備 |
| 收斂到錯的 | $\{\sin nt/\sqrt\pi\}$ 展開 $\cos t$ 得 0 | 奇函數積分 |
| 完備正規正交數列 | $x=\sum\langle x,x_n\rangle x_n$ ∀$x$（範數收斂） | 不推出逐點收斂 |
| 正規正交基底 | 每個 $x$ 唯一寫成 $\sum\alpha_nx_n$ | 完備 ⟹ 基底：$\sum|\alpha_n-\beta_n|^2=0$ |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 完備 ⟺ 基底 ⟺ Parseval | 第 22 集：Theorem 3.4.14、Parseval 公式 |
| 三角函數系完備 | 第 22 集：Fourier 級數的例子 |
| 映射 $x\mapsto(\langle x,x_n\rangle)\in\ell^2$ | 第 23 集：可分 Hilbert 空間同構於 $\ell^2$ |
| 最佳逼近 = 投影 | 第 23 集：正交補、投影定理 |
| Fourier 係數與波動方程 | 第 29–30 集：分離變數法、Sturm–Liouville |

---

## 附：本集一句話總結

> **Bessel 等式精確算出「用正規正交集投影逼近 $x$」的誤差，而且投影係數 $\langle x,x_k\rangle$ 就是最佳逼近；它也推出正規正交數列弱收斂到 0 卻不強收斂。在 Hilbert 空間裡 $\sum\alpha_nx_n$ 收斂恰好等於 $\sum|\alpha_n|^2<\infty$，所以 Fourier 級數總會收斂——但可能收斂到別的東西，除非正規正交數列「完備」，那時它就是正規正交基底。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-06 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 20:33）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4 整理。*
