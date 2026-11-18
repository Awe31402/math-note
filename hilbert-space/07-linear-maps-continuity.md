---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 7
lecture: Lecture 7
date: 2023-01-30
video: https://youtu.be/JFophJDlb38 （part 1）、https://youtu.be/k2_MbjF7LEw （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.5，Definition 1.5.1–Theorem 1.5.9（書頁 25–29，PDF 頁 44–48）
---

# 第 7 集 · 線性映射與連續性（Linear Maps and Continuity） [▶ 影片](https://youtu.be/JFophJDlb38)

← 上一集：[06-banach-spaces-completion](06-banach-spaces-completion.md) ｜ [總目錄](README.md) ｜ 下一集：[08-bounded-maps-contraction](08-bounded-maps-contraction.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 7 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 27:32，自動字幕）＋ Debnath & Mikusiński §1.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 線性映射與相關集合](#1-線性映射與相關集合)
- [2. 連續映射](#2-連續映射)
- [3. 範數是連續的](#3-範數是連續的)
- [4. 連續的拓樸刻畫](#4-連續的拓樸刻畫)
- [5. 線性映射：一點連續 ⟹ 處處連續](#5-線性映射一點連續--處處連續)
- [6. 有界線性映射](#6-有界線性映射)
- [7. 定理：線性映射連續 ⟺ 有界](#7-定理線性映射連續--有界)
- [8. 算子範數：B(E₁,E₂) 是賦範空間](#8-算子範數be₁e₂-是賦範空間)
- [9. 定理：E₂ 完備 ⟹ B(E₁,E₂) 完備](#9-定理e₂-完備--be₁e₂-完備)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 線性映射、像、原像、值域、零空間、圖形 | Definition 1.5.1，pp. 25–26 |
| 連續映射（序列定義）；範數連續 | Definition 1.5.2、Example 1.5.3，p. 26 |
| 連續 ⟺ 開集原像是開集 ⟺ 閉集原像是閉集 | Theorem 1.5.4，p. 26 |
| 線性映射一點連續 ⟹ 處處連續 | Theorem 1.5.5，pp. 26–27 |
| 有界線性映射；連續 ⟺ 有界 | Definition 1.5.6、Theorem 1.5.7，p. 27 |
| 算子範數；$B(E_1,E_2)$ 是賦範空間 | Theorem 1.5.8，pp. 27–28 |
| $E_2$ 完備 ⟹ $B(E_1,E_2)$ 完備 | Theorem 1.5.9，pp. 28–29 |

---

## 1. 線性映射與相關集合

[▶ 01:09](https://youtu.be/JFophJDlb38?t=69) 課本 Definition 1.5.1 與 p. 25 的記號。

**線性映射（linear mapping）**：$L:E_1\to E_2$，滿足

$$L(\alpha x+\beta y)=\alpha L(x)+\beta L(y)\quad\text{對所有 } x,y\in E_1,\ \alpha,\beta\in\mathbb{F}.$$

課本常把 $L(x)$ 寫成 $Lx$。講者說他不習慣這樣，他「熱愛多餘的括號」。【口頭】

**相關集合**：

| 名稱 | 定義 | 住在哪 |
|---|---|---|
| $A$ 的像（image） | $L(A)=\{L(x):x\in A\}$ | $E_2$ |
| $B$ 的原像（inverse image） | $L^{-1}(B)=\{x\in E_1:L(x)\in B\}$ | $E_1$ |
| 值域（range） | $\mathcal{R}(L)=L(E_1)$ | $E_2$ |
| 零空間（null space） | $\mathcal{N}(L)=\{x\in E_1:L(x)=0\}=L^{-1}(\{0\})$ | $E_1$ |
| 圖形（graph） | $\mathcal{G}(L)=\{(x,y):x\in E_1,\ y=L(x)\}$ | $E_1\times E_2$ |

注意：$L^{-1}(B)$ 這個記號**不代表** $L$ 可逆。

講者說【口頭】[▶ 06:04](https://youtu.be/JFophJDlb38?t=364)：子空間的像和原像都是子空間，這些在大學線性代數證過，證明**完全不受空間是無限維影響**，子空間檢驗法照用。所以 $\mathcal R(L)$、$\mathcal N(L)$、$\mathcal G(L)$ 都是向量空間。

【Q&A】[▶ 07:15](https://youtu.be/JFophJDlb38?t=435) 學生問：$L(A)$ 和 $L^{-1}(B)$ 不可能都在 $E_1$ 裡吧？講者：對，$L(A)\subseteq E_2$，$L^{-1}(B)\subseteq E_1$，是他寫錯了。

【課本補充】課本有一段說明為什麼可以假設線性映射的定義域是向量空間：如果定義域 $D(L)$ 只是子集，可以唯一地把 $L$ 線性延拓到 $\operatorname{span}D(L)$。

---

## 2. 連續映射

[▶ 08:41](https://youtu.be/JFophJDlb38?t=521) 課本 Definition 1.5.2。

$E_1,E_2$ 是賦範空間（可以有各自的範數，課本兩個都寫 $\|\cdot\|$）。$F:E_1\to E_2$（不一定線性）**在 $x_0$ 連續**，意思是：對每個收斂到 $x_0$ 的數列 $(x_n)$，$F(x_n)\to F(x_0)$。也就是

$$\|x_n-x_0\|_{E_1}\to0\ \Longrightarrow\ \|F(x_n)-F(x_0)\|_{E_2}\to0.$$

在每一點都連續，就叫**連續**。講者強調這是**用數列定義的**連續。

---

## 3. 範數是連續的

[▶ 11:42](https://youtu.be/JFophJDlb38?t=702) 課本 Example 1.5.3。

**主張**：$f:E\to\mathbb{R}$，$f(x)=\|x\|$ 是連續的。

**證明**：設 $x_n\to x_0$。$\mathbb{R}$ 的範數是絕對值，所以要看

$$|f(x_n)-f(x_0)|=\big|\|x_n\|-\|x_0\|\big|\le\|x_n-x_0\|\to0.$$

中間用了**反向三角不等式**（第 2 集）。$x_0$ 任意，所以範數處處連續。∎

---

## 4. 連續的拓樸刻畫

[▶ 16:15](https://youtu.be/JFophJDlb38?t=975) 課本 Theorem 1.5.4。

$F:E_1\to E_2$。下面三條等價：

- (a) $F$ 連續；
- (b) 對 $E_2$ 中每個開集 $U$，$F^{-1}(U)$ 在 $E_1$ 中是開集；
- (c) 對 $E_2$ 中每個閉集 $S$，$F^{-1}(S)$ 在 $E_1$ 中是閉集。

講者說【口頭】：(b) 就是拓樸學裡連續的**定義**。這門課用數列定義連續，這個定理把兩種定義接起來。上週學生想用「開集的原像是開集」來論證，講者當時說「我們還不知道這個」；證明是作業，做完之後就能自由使用拓樸論證了。講者說：剛從實分析進拓樸的人常常還在用數列思考，他弟弟也經歷過。他自己證這種等價有時順手、有時卡住，其中一個方向通常要用反證法，「我比較偏建構派」。[▶ 17:31](https://youtu.be/JFophJDlb38?t=1051)

---

## 5. 線性映射：一點連續 ⟹ 處處連續

[▶ 19:47](https://youtu.be/JFophJDlb38?t=1187) 課本 Theorem 1.5.5。

**定理**：$L:E_1\to E_2$ 線性，且在某一點 $x_0$ 連續，則 $L$ 處處連續。

講者先不看課本，和學生一起推。

**證明**：任取 $x_1\in E_1$ 和收斂到 $x_1$ 的數列 $y_n\to x_1$。要證 $L(y_n)\to L(x_1)$。

1. **把數列搬到 $x_0$ 附近**：令 $z_n=y_n-x_1+x_0$。則 $z_n\to x_1-x_1+x_0=x_0$。（講者一開始寫成減 $x_0$，改正成加 $x_0$。）[▶ 22:59](https://youtu.be/JFophJDlb38?t=1379)
2. **用 $x_0$ 的連續**：$L(z_n)\to L(x_0)$。
3. **用線性拆開**：$L(z_n)=L(y_n)-L(x_1)+L(x_0)$。所以
   $$L(y_n)-L(x_1)=L(z_n)-L(x_0)\to0.$$
   即 $L(y_n)\to L(x_1)$。∎

課本的版本只有三行：$Lx_n-Lx=L(x_n-x+x_0)-Lx_0\to0$。

講者的心得【口頭】[▶ 28:08](https://youtu.be/JFophJDlb38?t=1688)：線性是「巨大的」條件，它把本來沒關係的點連起來。知道 $L$ 在一點的行為，就知道它在很多其他點的行為；例如知道 $L(x)$，就知道 $L(cx)=cL(x)$，在 $\mathbb{R}^2$ 裡整條直線上的值都知道了。

---

## 6. 有界線性映射

[▶ 28:43](https://youtu.be/JFophJDlb38?t=1723) 課本 Definition 1.5.6。

講者說「有界線性映射」一開始聽起來很可疑：線性代數裡的線性映射，$L(cx)=cL(x)$，$c$ 想多大就多大，怎麼可能有界？除非 $L(x)=0$。[▶ 30:03](https://youtu.be/JFophJDlb38?t=1803)

**定義**：線性映射 $L:E_1\to E_2$ 叫**有界（bounded）**，如果存在 $\alpha>0$ 使得

$$\|L(x)\|\le\alpha\|x\|\quad\text{對所有 } x\in E_1.$$

意思是：輸出的大小最多是輸入大小的某個倍數。所以「有界」不是說值域有界，而是說**放大倍率有界**。

**在單位球面上有界**【課堂討論】[▶ 32:07](https://youtu.be/JFophJDlb38?t=1927) 講者請學生把 $\|x\|$ 移到另一邊。$x\ne0$ 時兩邊除以 $\|x\|$，再把 $\frac1{\|x\|}$ 用線性放進 $L$ 裡：

$$\frac{\|L(x)\|}{\|x\|}=\left\|L\left(\frac{x}{\|x\|}\right)\right\|\le\alpha.$$

$u=\frac{x}{\|x\|}$ 是單位向量。所以有界 ⟺ $\|L(u)\|\le\alpha$ 對所有 $\|u\|=1$ 成立，也就是 **$L$ 在單位球面 $S(0,1)$ 上有界**。

講者說【口頭】[▶ 35:25](https://youtu.be/JFophJDlb38?t=2125)：賦範空間一般是無限延伸的，單位球面是衡量有界的「標準物件」：它上面有無限多點，卻捕捉了某種有限性。

---

## 7. 定理：線性映射連續 ⟺ 有界

[▶ 35:58](https://youtu.be/JFophJDlb38?t=2158) 課本 Theorem 1.5.7。

### (⟸) 有界 ⟹ 連續

設 $\|Lx\|\le\alpha\|x\|$，$x_n\to0$。則

$$\|L(x_n)\|\le\alpha\|x_n\|\to0,$$

所以 $L(x_n)\to0=L(0)$：$L$ 在 $0$ 連續。由第 5 節，$L$ 處處連續。∎

### (⟹) 連續 ⟹ 有界（反證）

[▶ 39:50](https://youtu.be/JFophJDlb38?t=2390)

1. **假設 $L$ 無界**：對每個 $n\in\mathbb{N}$，存在 $x_n$ 使
   $$\|L(x_n)\|>n\|x_n\|.$$
   （這說明 $x_n\ne0$。）
2. **構造**：
   $$y_n=\frac{x_n}{n\|x_n\|}.$$
3. **$y_n\to0$**：$\|y_n\|=\frac1n\to0$。講者用的是「純量數列乘向量數列」的極限律（第 2–3 集辛苦證的那條）。
4. **但 $L(y_n)$ 不趨近 $0$**：
   $$\|L(y_n)\|=\frac{1}{n\|x_n\|}\|L(x_n)\|>\frac{n\|x_n\|}{n\|x_n\|}=1.$$
5. $L$ 連續的話，$y_n\to0$ 應推出 $L(y_n)\to L(0)=0$。矛盾。∎

【課堂討論】[▶ 41:11](https://youtu.be/JFophJDlb38?t=2471) 學生問第 1 步是不是「無界」的嚴格否定。講者說：嚴格否定是「對每個 $\alpha>0$ 都有 $x$ 使 $\|Lx\|>\alpha\|x\|$」；課本取 $\alpha=n$，所以第 1 步是否定的**邏輯推論**，而且更具體（只挑自然數）。講者在第 4 步一度把 $\frac1n$ 寫到 $L$ 外面搞混，後來改正：$x_n$ 留在 $L$ 裡，用線性把係數提出來。[▶ 49:47](https://youtu.be/JFophJDlb38?t=2987)

**有限維 vs 無限維**[▶ 51:27](https://youtu.be/JFophJDlb38?t=3087)

課本說：有限維空間之間的線性映射都有界，所以都連續。講者問：那無限維空間裡有沒有**不連續**的線性映射？學生說應該有，講者說他得想一想；他提醒：剛才證的定理**沒有**假設有限維。

> 以下**不是逐字稿內容**，是依定理推論的例子：有。取 $P([0,1])$（一致範數），$D=\frac{d}{dx}$ 是線性的。$\|x^n\|=1$，但 $\|D(x^n)\|=\|nx^{n-1}\|=n$。所以沒有 $\alpha$ 能讓 $\|Dp\|\le\alpha\|p\|$，$D$ 無界，因此不連續。（直觀：$x^n/n$ 一致收斂到 0，但導數 $x^{n-1}$ 不收斂到 0。）

【課本補充】對線性映射，連續與**一致連續**等價。

---

## 8. 算子範數：B(E₁,E₂) 是賦範空間

[▶ 53:46](https://youtu.be/JFophJDlb38?t=3226) 課本 Theorem 1.5.8。

$B(E_1,E_2)$：所有從 $E_1$ 到 $E_2$ 的**有界**（等於連續）線性映射。運算逐點定義：

$$(L_1+L_2)x=L_1x+L_2x,\qquad(\lambda L)x=\lambda(Lx).$$

**定理**：$B(E_1,E_2)$ 是賦範空間，範數為

$$\|L\|=\sup_{\|x\|=1}\|Lx\|. \tag{1.14}$$

**向量空間**[▶ 56:14](https://youtu.be/JFophJDlb38?t=3374)：講者說線性映射的線性組合還是線性映射，無限維也一樣：$(cL_1+L_2)(\alpha x+\beta y)$ 用 $L_1,L_2$ 的線性展開再重組，就是 $\alpha(cL_1+L_2)x+\beta(cL_1+L_2)y$。（有界性也保持，由下面的三角不等式。）

**(a) $\|L\|=0\Rightarrow L=0$**[▶ 58:23](https://youtu.be/JFophJDlb38?t=3503)：$\|L\|=0$ 表示所有單位向量 $x$ 都有 $L(x)=0$。任取 $y\ne0$，

$$L(y)=L\left(\|y\|\frac{y}{\|y\|}\right)=\|y\|\,L\left(\frac{y}{\|y\|}\right)=\|y\|\cdot0=0.$$

又 $L(0)=0$。所以 $L$ 是零映射。

**(c) 三角不等式**[▶ part 2 01:10](https://youtu.be/k2_MbjF7LEw?t=70)：對 $\|x\|=1$，

$$\|L_1x+L_2x\|\le\|L_1x\|+\|L_2x\|\le\sup_{\|x\|=1}\|L_1x\|+\sup_{\|x\|=1}\|L_2x\|=\|L_1\|+\|L_2\|.$$

右邊與 $x$ 無關，所以左邊取 sup 也不超過它：$\|L_1+L_2\|\le\|L_1\|+\|L_2\|$。

講者說這裡用到 sup 的一個性質：若 $a(x)\le b(x)$ 對所有 $x$，則 $\sup a\le\sup b$；嚴格來說應該證一下。學生問能不能直接把三角不等式套在 sup 上；講者說要寫成上面這樣才對。課本 p. 28 頂端的證明跟講者的一樣。[▶ part 2 03:12](https://youtu.be/k2_MbjF7LEw?t=192)

（(b) $\|\lambda L\|=|\lambda|\|L\|$ 直接由 $\|\lambda Lx\|=|\lambda|\|Lx\|$ 取 sup 得到。）

**重要的不等式**【課本補充】：由 (1.14) 和第 6 節的正規化，

$$\|Lx\|\le\|L\|\,\|x\|\quad\text{對所有 } x\in E_1,$$

而且 $\|L\|$ 是使 $\|Lx\|\le\alpha\|x\|$ 成立的**最小**的 $\alpha$。講者在第 9 節說「這真該先寫成一個引理」。

課本把這個範數下的收斂叫**一致收斂（uniform convergence）**。講者口誤說成「一致收斂範數」。[▶ part 2 06:06](https://youtu.be/k2_MbjF7LEw?t=366)（一般書上叫它**算子範數**。）

---

## 9. 定理：E₂ 完備 ⟹ B(E₁,E₂) 完備

[▶ part 2 06:06](https://youtu.be/k2_MbjF7LEw?t=366) 課本 Theorem 1.5.9。

**定理**：$E_1$ 是賦範空間，$E_2$ 是 Banach 空間，則 $B(E_1,E_2)$ 是 Banach 空間。

注意：只要求**值域** $E_2$ 完備，$E_1$ 不需要。

又是完備性證明的模板（第 6 集）：候選極限 → 在空間裡 → 按範數收斂。

**Step 1：逐點 Cauchy。**[▶ part 2 08:37](https://youtu.be/k2_MbjF7LEw?t=517) $(L_n)$ 是 $B(E_1,E_2)$ 中的 Cauchy 數列，$x\in E_1$ 任意。

$$\|L_mx-L_nx\|=\|(L_m-L_n)x\|\le\|L_m-L_n\|\,\|x\|\to0\quad(m,n\to\infty).$$

講者提醒：這一步混用了兩種範數，左邊是 $E_2$ 的範數，$\|L_m-L_n\|$ 是剛定義的算子範數。他當場用正規化 $z=x/\|x\|$ 重新說明 $\|Tx\|\le\|T\|\|x\|$ 為什麼成立。[▶ part 2 10:26](https://youtu.be/k2_MbjF7LEw?t=626)

所以 $(L_nx)$ 是 $E_2$ 中的 Cauchy 數列。$E_2$ 完備，定義

$$Lx=\lim_{n\to\infty}L_nx.$$

**Step 2：$L\in B(E_1,E_2)$。**[▶ part 2 18:37](https://youtu.be/k2_MbjF7LEw?t=1117)

- 線性：課本說「顯然」（極限的線性）。
- 有界：Cauchy 數列有界（第 5 集 Lemma 1.4.4），所以有 $\alpha$ 使 $\|L_n\|\le\alpha$ 對所有 $n$。則
  $$\|Lx\|=\left\|\lim_nL_nx\right\|=\lim_n\|L_nx\|\le\alpha\|x\|.$$
  第二個等號用了**範數連續**（第 3 節）。

**Step 3：$\|L_n-L\|\to0$。**[▶ part 2 22:34](https://youtu.be/k2_MbjF7LEw?t=1354) 講者說：我們造出了 $L$，但還沒證它是數列的極限。

給 $\varepsilon>0$，取 $k$ 使 $m,n\ge k$ 時 $\|L_m-L_n\|<\varepsilon$。對 $\|x\|=1$：

$$\|L_mx-L_nx\|\le\|L_m-L_n\|\,\|x\|<\varepsilon.$$

**固定 $m$**，令 $n\to\infty$：$\|L_mx-Lx\|\le\varepsilon$，對所有 $m\ge k$ 和所有單位向量 $x$。所以取 sup：

$$\|L_m-L\|=\sup_{\|x\|=1}\|L_mx-Lx\|\le\varepsilon\quad(m\ge k).$$

$\varepsilon$ 任意，$L_m\to L$。∎

**講者的應用經驗**【Q&A】[▶ part 2 26:28](https://youtu.be/k2_MbjF7LEw?t=1588) 學生說在高等微積分裡見過算子範數。講者：對，證多變數導數的定理時會需要「線性映射的範數」，雖然那些空間看起來都是有限維的。

> 下一集講 §1.5 剩下的 Theorem 1.5.10–1.5.13，接著進 §1.6 壓縮映射。

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 線性映射 | $L(\alpha x+\beta y)=\alpha Lx+\beta Ly$ | 像、原像、$\mathcal R$、$\mathcal N$、$\mathcal G$ 都是子空間 |
| 連續（序列） | $x_n\to x_0\Rightarrow F(x_n)\to F(x_0)$ | |
| 範數連續 | $x\mapsto\|x\|$ | $\big|\|x_n\|-\|x\|\big|\le\|x_n-x\|$ |
| 拓樸刻畫 | 連續 ⟺ 開集原像開 ⟺ 閉集原像閉 | 作業 |
| 一點 ⟹ 處處 | 線性 + 在 $x_0$ 連續 ⟹ 連續 | $z_n=y_n-x_1+x_0\to x_0$，再用線性 |
| 有界 | $\|Lx\|\le\alpha\|x\|$ ⟺ 單位球面上有界 | 除以 $\|x\|$，係數放進 $L$ |
| 連續 ⟺ 有界 | Thm 1.5.7 | ⟸ $\|Lx_n\|\le\alpha\|x_n\|$；⟹ 反證，$y_n=\frac{x_n}{n\|x_n\|}$，$\|Ly_n\|>1$ |
| 無界例子 | $D=\frac d{dx}$ 在 $P([0,1])$ | $\|x^n\|=1$，$\|Dx^n\|=n$ |
| 算子範數 | $\|L\|=\sup_{\|x\|=1}\|Lx\|$ | $\|Lx\|\le\|L\|\|x\|$；$\|L\|$ 是最小的界 |
| $B(E_1,E_2)$ 完備 | $E_2$ Banach ⟹ $B(E_1,E_2)$ Banach | 逐點 Cauchy 定義 $Lx$；Cauchy 有界 ⟹ $L$ 有界；固定 $m$ 令 $n\to\infty$ |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 有界線性映射、算子範數 | 第 8 集：$\|Lx\|\le\|L\|\|x\|$ 反覆用；第 24 集起：Hilbert 空間上的算子 |
| $B(E,\mathbb{F})$（對偶空間，泛函） | 第 24 集：Riesz 表示定理 |
| $B(E_1,E_2)$ 完備 | 第 10 集：矩陣指數 $e^{tA}$ 在 $B(\mathbb{R}^n,\mathbb{R}^n)$ 中收斂 |
| 無界線性算子（如微分） | 第 26–29 集：無界算子、微分算子 |
| 拓樸刻畫的連續 | 之後的拓樸論證 |

---

## 附：本集一句話總結

> **對線性映射，連續、在一點連續、有界三件事等價——「有界」不是值域有界，而是放大倍率 $\|Lx\|/\|x\|$ 有界；這個最大倍率就是算子範數，使有界線性映射本身成為賦範空間，而且只要值域完備，這個空間就是 Banach 空間。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-01-30 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 27:32）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.5 整理。*
