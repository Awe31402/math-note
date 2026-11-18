---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 27
lecture: Lecture 27
date: 2023-03-31
video: https://youtu.be/yt0J9KWyH9M （part 1）、https://youtu.be/1Vo0IsnHSDg （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.9，Definition 4.9.1–Theorem 4.9.8（書頁 186–190，PDF 頁 205–209）
---

# 第 27 集 · 本徵向量、譜、預解式 [▶ 影片](https://youtu.be/yt0J9KWyH9M)

← 上一集：[26-self-adjoint-normal-inverse](26-self-adjoint-normal-inverse.md) ｜ [總目錄](README.md) ｜ 下一集：[28-eigenvectors-finite-dim-review](28-eigenvectors-finite-dim-review.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 27 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 4:42，自動字幕）＋ Debnath & Mikusiński §4.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 本徵值與本徵向量](#1-本徵值與本徵向量)
- [2. 例：投影算子](#2-例投影算子)
- [3. 本徵空間、重數、退化](#3-本徵空間重數退化)
- [4. 例：積分算子 cos(t − y)](#4-例積分算子-cost--y)
- [5. 不是本徵值 ⟺ A − λI 可逆](#5-不是本徵值--a--λi-可逆)
- [6. 預解式、正則值、譜](#6-預解式正則值譜)
- [7. 例：乘法算子——有譜卻沒有本徵值](#7-例乘法算子有譜卻沒有本徵值)
- [8. 振動系統](#8-振動系統)
- [9. Neumann 級數](#9-neumann-級數)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

（一位學生在外地，講者說「如果你本來想加入，抱歉」。）

| 主題 | 課本 |
|---|---|
| 本徵值、本徵向量；投影的例子 | Definition 4.9.1、Example 4.9.2，p. 186 |
| 本徵空間、重數 | Theorem 4.9.3、Definition 4.9.4，pp. 186–187 |
| 積分算子的例子 | Example 4.9.5，p. 187 |
| 預解式、正則值、譜、譜半徑 | Definition 4.9.6，p. 188 |
| 乘法算子的譜 | Example 4.9.7，p. 188 |
| 振動系統 | (4.28)–(4.29)，pp. 188–189 |
| Neumann 級數 | Theorem 4.9.8，pp. 189–190 |

---

## 1. 本徵值與本徵向量

[▶ 00:35](https://youtu.be/yt0J9KWyH9M?t=35) 課本 Definition 4.9.1。

**定義**：$A$ 是複向量空間 $E$ 上的算子。複數 $\lambda$ 叫 $A$ 的**本徵值（eigenvalue）**，如果存在**非零**向量 $u$ 使

$$Au=\lambda u. \tag{4.23}$$

滿足 (4.23) 的**每個**向量叫對應 $\lambda$ 的**本徵向量（eigenvector）**；函數空間裡常叫**本徵函數（eigenfunction）**。

講者【口頭】[▶ 02:02](https://youtu.be/yt0J9KWyH9M?t=122)：這不完全是標準定義，課本很狡猾：它把 0 也算成本徵向量。大學線代課裡他會小心說「本徵空間裡只有本徵向量，例外是 0」；課本這樣定義就避開了這個討論。

---

## 2. 例：投影算子

[▶ 03:07](https://youtu.be/yt0J9KWyH9M?t=187) 課本 Example 4.9.2。講者說這個例子來自我們跳過的 §4.7，「這正是講它的理由」。

$S$ 是內積空間 $E$ 的子空間，$P_S$ 是投影到 $S$ 的算子（講者當作 $E\to E$）。寫 $z=s+x$，$s\in S$、$x\in S^\perp$，則 $P_Sz=s$。

- $u\in S$：$P_Su=u=1\cdot u$，所以 1 是本徵值，本徵空間是 $S$。
- $u\in S^\perp$：$P_Su=0=0\cdot u$，所以 0 是本徵值，本徵空間是 $S^\perp$。

【課本補充】只有 0 和 1：若 $P_Su=\lambda u$（$u\ne0$），由 $P_S^2=P_S$，$\lambda u=P_Su=P_S^2u=\lambda^2u$，所以 $\lambda=\lambda^2$，$\lambda\in\{0,1\}$。

**對角化**【口頭】[▶ 07:47](https://youtu.be/yt0J9KWyH9M?t=467)：若 $E$ 是 $n$ 維、$S$ 是 $m$ 維，$E=S\oplus S^\perp$。取基底 $\beta=\{v_1,\dots,v_m,w_1,\dots,w_{n-m}\}$（前 $m$ 個是 $S$ 的基底，後面是 $S^\perp$ 的）。算矩陣：把 $P_S$ 作用在每個基底向量上、取座標向量當一行：

$$[P_S]_\beta=\begin{pmatrix}I_m&0\\0&0\end{pmatrix}.$$

講者：我們把投影**對角化**了，這是一個**本徵基底**（每個基底元素都是本徵向量，本徵值 0 或 1）。不是每個變換都有本徵基底；這節和下一節要問的就是什麼時候能對角化。可以對角化時，整個空間是本徵空間的直和；而且之後會證：不同本徵值的本徵空間互相垂直（自伴時）。

【課本補充】課本強調：每個本徵向量只對應一個本徵值，但每個本徵值都有無限多個本徵向量（本徵向量的倍數還是本徵向量），而且可能有多個線性獨立的。

---

## 3. 本徵空間、重數、退化

[▶ 13:02](https://youtu.be/yt0J9KWyH9M?t=782) 課本 Theorem 4.9.3、Definition 4.9.4。

**Theorem 4.9.3**：對應同一個本徵值的所有本徵向量構成向量空間（證明是習題）。

講者：就算 $\lambda$ **不是**本徵值，$\{u:Au=\lambda u\}$ 也還是子空間——只是 $\{0\}$，「這是很蠢地成立」。[▶ 13:33](https://youtu.be/yt0J9KWyH9M?t=813)

**定義**：

- **本徵空間（eigenspace）**：對應 $\lambda$ 的所有本徵向量。
- **重數（multiplicity）**：本徵空間的維度。
- 重數 1：**簡單（simple）**或**非退化（nondegenerate）**。
- 重數 > 1：**多重（multiple）**或**退化（degenerate）**；這時維度也叫**退化度**。

講者【口頭】[▶ 15:52](https://youtu.be/yt0J9KWyH9M?t=952)：他不太喜歡這個用語，大學線代他會叫它**幾何重數（geometric multiplicity）**。物理裡退化的本徵值會帶來「樂趣」。

**投影的例子**：若 $S$ 是一條線（一維），本徵值 1 是簡單的；本徵值 0 大概是退化的——除非整個空間是二維，那時 0、1 都簡單。若 $S$ 超過一維，本徵值 1 就退化。

---

## 4. 例：積分算子 cos(t − y)

[▶ 17:39](https://youtu.be/yt0J9KWyH9M?t=1059) 課本 Example 4.9.5。

$L^2([0,2\pi])$ 上

$$(Au)(t)=\int_0^{2\pi}\cos(t-y)\,u(y)\,dy.$$

本徵值方程 $(Au)(t)=\lambda u(t)$。

**課堂的計算**[▶ 18:52](https://youtu.be/yt0J9KWyH9M?t=1132)：講者把核展開成 $\cos t\cos y-\sin t\sin y$，得

$$\lambda u(t)=\cos t\int_0^{2\pi}\cos y\,u(y)dy-\sin t\int_0^{2\pi}\sin y\,u(y)dy.$$

所以 $\lambda\ne0$ 時 $u$ 是 cos 和 sin 的線性組合：$u(t)=a\cos t+b\sin t$（$\lambda$ 可以吸收進 $a,b$）。代回去：$\cos t\sin t$ 的交叉項在兩個週期上積分為 0；$\int_0^{2\pi}\cos^2=\int_0^{2\pi}\sin^2=\pi$（講者的技巧：兩者在 $[0,2\pi]$ 上對稱，加起來 $\int1=2\pi$，各佔一半）。[▶ 23:45](https://youtu.be/yt0J9KWyH9M?t=1425)

得 $\lambda a=\pi a$、$\lambda b=-\pi b$（cos、sin 線性獨立，比較係數）。講者的結論：兩個本徵值 $\pi$ 和 $-\pi$，$\pi$ 的本徵函數是 cos，$-\pi$ 的本徵函數是 sin（及其倍數）。

> 以下**不是逐字稿內容**，是依課本修正：展開式的正負號寫反了。$\cos(t-y)=\cos t\cos y\,\mathbf{+}\,\sin t\sin y$（減號的是 $\cos(t+y)$）。正確的式子是
> $$\lambda u(t)=\cos t\int_0^{2\pi}\cos y\,u(y)dy+\sin t\int_0^{2\pi}\sin y\,u(y)dy,$$
> 代入 $u=a\cos t+b\sin t$ 得 $\pi a=\lambda a$、$\pi b=\lambda b$。所以（課本的結論）：
>
> - 唯一的**非零**本徵值是 $\lambda=\pi$，本徵函數是 $a\cos t+b\sin t$（$a,b$ 任意），本徵空間二維，**重數 2**（退化）。
> - 由 (4.25)，$\lambda=0$ 也是本徵值：所有跟 $\cos t$、$\sin t$ 都正交的函數，**重數無限**。
>
> 一個快速檢查：這個核滿足 $K(t,y)=\overline{K(y,t)}$（第 26 集），算子自伴，本徵值必須是實數——$\pm\pi$ 都是實數，所以這個檢查分不出來；但用 $\sin$ 直接代：$\int_0^{2\pi}\cos(t-y)\sin y\,dy=\pi\sin t$，確實是 $+\pi$。

講者【口頭】[▶ 26:06](https://youtu.be/yt0J9KWyH9M?t=1566)：有一個本徵向量就有無限多個（純量倍），因為我們在特徵 0 的體上；「如果你問有限特徵體上本徵向量怎麼運作，我會說去找別的教授。」他還說希望天堂裡也能做數學，「天堂應該充滿美好有價值的事物，我願意相信數學是其中之一」。

---

## 5. 不是本徵值 ⟺ A − λI 可逆

[▶ 27:14](https://youtu.be/yt0J9KWyH9M?t=1634) 課本 p. 187。

若 $\lambda$ 不是 $A$ 的本徵值，則 $A-\lambda I$ 可逆，反之亦然。

**講者的說明**：

- 若 $(A-\lambda I)^{-1}$ 存在，且 $Au=\lambda u$，即 $(A-\lambda I)u=0$。兩邊作用 $(A-\lambda I)^{-1}$（逆也是線性的，把 0 送到 0）：$u=0$。所以 $\lambda$ 不是本徵值。
- 反過來：如果有非零解，$A-\lambda I$ 不是一對一，就不可逆（否則逆是多值的）。

講者【口頭】[▶ 29:12](https://youtu.be/yt0J9KWyH9M?t=1752)：有限維時用**行列式** $\det(A-\lambda I)=0$；但無限維**不能**用行列式。「也許在可分 Hilbert 空間對無窮矩陣有辦法定義行列式……我在猜。」這就是無限維開始變有趣的地方。

【課本補充】有限維時，$\lambda$ 不是本徵值 ⟹ $(A-\lambda I)^{-1}$ **有界**（有限維上所有算子都有界）。無限維就複雜了——於是有下面的定義。

---

## 6. 預解式、正則值、譜

[▶ 29:43](https://youtu.be/yt0J9KWyH9M?t=1783) 課本 Definition 4.9.6。

$A$ 是賦範空間 $E$ 上的算子。

- **預解式（resolvent）**：$A_\lambda=(A-\lambda I)^{-1}$。
- **正則值（regular value）**：使 $A_\lambda$ **定義在整個 $E$ 上而且有界**的 $\lambda$。
- **預解集（resolvent set）** $\rho(A)$：所有正則值。
- **譜（spectrum）** $\sigma(A)=\mathbb{C}\setminus\rho(A)$。
- **譜半徑（spectral radius）**：$r(A)=\sup\{|\lambda|:\lambda\in\sigma(A)\}$。

講者把譜半徑說成「本徵值模的最小上界」。[▶ 33:20](https://youtu.be/yt0J9KWyH9M?t=2000)（精確說是**譜**中元素的模的上確界。）

**課本**：每個本徵值都在譜裡。但譜可能含有不是本徵值的點；非空的譜甚至可能**完全沒有**本徵值。講者：「所以不是『譜就是本徵值』那麼簡單……有點挑剔。」

---

## 7. 例：乘法算子——有譜卻沒有本徵值

[▶ 34:29](https://youtu.be/yt0J9KWyH9M?t=2069) 課本 Example 4.9.7。

$E=C([a,b])$，固定 $u\in C([a,b])$，

$$(Ax)(t)=u(t)x(t).$$

**求逆**[▶ 35:40](https://youtu.be/yt0J9KWyH9M?t=2140)：講者說課本直接丟出公式，表示我們一分鐘就能推出來。$(A-\lambda I)x=y$ 即 $(u-\lambda)x=y$，解出 $x$：

$$(A-\lambda I)^{-1}y(t)=\frac{y(t)}{u(t)-\lambda}.$$

講者的一般建議【口頭】：要找逆的公式，寫下公式，給輸出一個名字，然後**解出輸入**。

**譜**：當某個 $t\in[a,b]$ 使 $u(t)=\lambda$ 時就失敗。所以

$$\sigma(A)=\text{$u$ 的值域}.$$

講者假設 $u$ 是實值（他說課本似乎採取「實算子時把 $\mathbb{C}$ 換成 $\mathbb{R}$」的慣例，否則例子後面講不通）。[▶ 40:21](https://youtu.be/yt0J9KWyH9M?t=2421)

- **$u\equiv c$ 常數**：$Ax=cx$，$\lambda=c$ 是本徵值，每個非零函數都是本徵函數；$\rho(A)=\mathbb{R}\setminus\{c\}$，$\sigma(A)=\{c\}$。
- **$u$ 嚴格遞增**：$\sigma(A)=[u(a),u(b)]$，但 **$A$ 沒有任何本徵值**。

**為什麼沒有本徵值**【課堂討論】[▶ 44:21](https://youtu.be/yt0J9KWyH9M?t=2661)：若 $u(t)x(t)=\lambda x(t)$ 對所有 $t$，則 $(u(t)-\lambda)x(t)=0$。$\lambda$ 是固定的數，若它在值域裡，只有一個 $t_0$ 使 $u(t_0)=\lambda$（嚴格遞增）。其他點 $x(t)=0$，而 $x$ 連續，所以 $x(t_0)=0$ 也是。只有零函數。

講者：所以這個例子達成目的：譜非平凡，卻一個本徵值都沒有。

> 以下**不是逐字稿內容**，是補一句：在 $\lambda\in(u(a),u(b))$ 時，$A-\lambda I$ 是一對一的（沒有本徵向量），但 $\frac{y}{u-\lambda}$ 對很多 $y$ 不是連續函數（例如 $y=1$），所以逆不是定義在整個空間上——$\lambda$ 不是正則值。這是「一對一卻不映成」，只在無限維發生。

---

## 8. 振動系統

[▶ 46:53](https://youtu.be/yt0J9KWyH9M?t=2813) 課本 pp. 188–189。

課本：本徵值問題的主要來源之一是振動系統。古典力學的運動方程

$$\frac{d^2u}{dt^2}=Au. \tag{4.28}$$

講者舉例【口頭】：一串彈簧連在一起，運動方程可以寫成這樣，$A$ 是矩陣、$u$ 是各彈簧的座標。

若系統振動，猜 $u(t)=v\sin\omega t$（$v$ 固定）。微分兩次得 $-\omega^2v\sin\omega t$，要等於 $Av\sin\omega t$ 對所有 $t$，所以

$$Av=-\omega^2v. \tag{4.29}$$

$-\omega^2$ 是 $A$ 的本徵值，$v$ 是本徵向量。

講者【口頭】[▶ 49:23](https://youtu.be/yt0J9KWyH9M?t=2963)：他覺得在 PDE 裡「本徵值」這個詞有時用得不太精確，之後的課會講到。

---

## 9. Neumann 級數

[▶ 49:57](https://youtu.be/yt0J9KWyH9M?t=2997) 課本 Theorem 4.9.8。

講者：「複向量空間、Hilbert 空間、現在是 Banach 空間——我們什麼都有了。」

**定理**：$A$ 是 Banach 空間 $E$ 上的有界線性算子，$\|A\|<|\lambda|$。則 $A_\lambda=(A-\lambda I)^{-1}$ 是有界算子，

$$A_\lambda=-\sum_{n=0}^\infty\frac{A^n}{\lambda^{n+1}}, \tag{4.30}$$

$$\|A_\lambda\|\le\frac{1}{|\lambda|-\|A\|}. \tag{4.31}$$

講者：「這我好像沒教過。」證明不嚇人，約半頁。

**「形式上的胡說」**【口頭】[▶ 52:20](https://youtu.be/yt0J9KWyH9M?t=3140)：講者先像處理數字一樣推。他第一次試著提出 $A^{-1}$，發現不對（不能假設 $A$ 可逆），改成提出 $-\lambda$：

$$\frac{1}{A-\lambda I}=\frac{1}{-\lambda}\cdot\frac{1}{I-\frac1\lambda A}=-\frac1\lambda\sum_{n=0}^\infty\left(\frac{A}{\lambda}\right)^n=-\sum_{n=0}^\infty\frac{A^n}{\lambda^{n+1}}.$$

幾何級數要 $\left\|\frac A\lambda\right\|<1$，即 $\|A\|<|\lambda|$——這正是定理的前提。「我要做形式上的胡說，但不要太胡說。」

講者說：超數（super numbers，他的研究）求逆時也有類似的狀況：看起來像除以一個超數，形式上沒意義，但它告訴你要證什麼，然後去證那些估計。[▶ 57:19](https://youtu.be/yt0J9KWyH9M?t=3439)

**課本的證明**（講者描述）：

1. $\sum\left\|\frac{A^n}{\lambda^n}\right\|\le\sum\left(\frac{\|A\|}{|\lambda|}\right)^n<\infty$（幾何級數控制）。
2. $B(E,E)$ 完備（第 7 集），所以絕對收斂級數收斂到某個有界算子 $B=\sum\frac{A^n}{\lambda^n}$。
3. 驗證 $(A-\lambda I)B=-\lambda I=B(A-\lambda I)$（伸縮和），所以 $B$ 除以 $-\lambda$ 就是逆。
4. (4.31)：級數層次的三角不等式，再一次幾何級數：$\|A_\lambda\|\le\frac1{|\lambda|}\sum\left(\frac{\|A\|}{|\lambda|}\right)^n=\frac1{|\lambda|-\|A\|}$。

講者說存在性靠幾何級數，而幾何級數存在正是讓「形式胡說」合理的條件。學生提議用三角不等式推 (4.31)，講者：「謝謝你的建議，那很好玩。」[▶ 59:31](https://youtu.be/yt0J9KWyH9M?t=3571)

**特例**（$\lambda=1$ 的版本）[▶ part 2 00:01](https://youtu.be/1Vo0IsnHSDg?t=1)：課本說 (4.30) 叫 **Neumann 級數**（Carl Gottfried Neumann，1832–1925）；若 $\|A\|<1$，

$$(I-A)^{-1}=\sum_{n=0}^\infty A^n.$$

講者想了一下這怎麼從定理得到：定理給 $(A-I)^{-1}=-\sum A^n$，而若 $CB=BC=I$，則 $(-C)(-B)=I$，所以 $(-B)^{-1}=-B^{-1}$。「為什麼我沒把這出成線代作業？……如果課前沒講過，這是很好的考題，那種讓人說『我沒做出來』、看到答案後說『混蛋』的題目。」[▶ part 2 02:55](https://youtu.be/1Vo0IsnHSDg?t=175)

【課本補充】**Corollary 4.9.9**：$r(A)\le\|A\|$。也就是有界算子的所有本徵值都落在以原點為中心、半徑 $\|A\|$ 的閉圓盤裡。（因為 $|\lambda|>\|A\|$ 時 $\lambda$ 是正則值。）

講者：本徵向量和本徵值花不只一天「不丟臉」，今天到此。

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵 |
|---|---|---|
| 本徵值 | 有非零 $u$ 使 $Au=\lambda u$ | 課本把 0 也算進本徵向量集合 |
| 投影 | 本徵值只有 0、1；本徵空間 $S^\perp$、$S$ | $P_S^2=P_S\Rightarrow\lambda^2=\lambda$ |
| 對角化 | $[P_S]_\beta=\begin{pmatrix}I_m&0\\0&0\end{pmatrix}$ | 本徵基底 |
| 重數 | 本徵空間維度（幾何重數）；>1 為退化 | |
| 例 | $\int_0^{2\pi}\cos(t-y)u(y)dy$：$\lambda=\pi$（重數 2，cos 和 sin）、$\lambda=0$（重數無限） | $\cos(t-y)=\cos t\cos y+\sin t\sin y$ |
| 判準 | 不是本徵值 ⟺ $A-\lambda I$ 可逆 | 無限維沒有行列式 |
| 預解式 | $A_\lambda=(A-\lambda I)^{-1}$ | |
| 正則值 | $A_\lambda$ 定義在整個 $E$ 且有界 | |
| 譜 | $\sigma(A)=\mathbb{C}\setminus\rho(A)$ ⊇ 本徵值 | 可能沒有本徵值 |
| 乘法算子 | $\sigma(A)=u$ 的值域；$u$ 嚴格遞增時無本徵值 | $(A-\lambda I)^{-1}y=\frac{y}{u-\lambda}$ |
| 振動 | $u=v\sin\omega t$ ⟹ $Av=-\omega^2v$ | |
| Neumann | $\|A\|<|\lambda|$：$A_\lambda=-\sum\frac{A^n}{\lambda^{n+1}}$，$\|A_\lambda\|\le\frac1{|\lambda|-\|A\|}$ | 幾何級數；$B(E,E)$ 完備 |
| 推論 | $(I-A)^{-1}=\sum A^n$（$\|A\|<1$）；$r(A)\le\|A\|$ | |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 自伴算子的本徵值實、本徵向量正交 | 第 28 集（Theorem 4.9.10 起） |
| 緊緻自伴算子的本徵值 | 第 28–29 集：$\|A\|$ 或 $-\|A\|$ 是本徵值；譜定理 |
| 對角化、本徵基底 | 第 29 集：譜分解 |
| 振動系統、本徵值 $-\omega^2$ | 第 29–30 集：波動方程、分離變數 |
| Neumann 級數 | 課本 §5.2、§5.5：積分方程的逐次逼近（第 9 集的延伸） |

---

## 附：本集一句話總結

> **本徵值的定義跟有限維一樣，但無限維沒有行列式可用，所以改用預解式 $(A-\lambda I)^{-1}$：讓它在整個空間上有定義且有界的 $\lambda$ 是正則值，其餘的是譜——譜包含所有本徵值，卻可能一個本徵值都沒有（嚴格遞增函數的乘法算子）；而 $|\lambda|>\|A\|$ 時，預解式可以用 Neumann 幾何級數直接寫出來。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-31 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 4:42）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.9 整理。*
