---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 2
lecture: Lecture 2
date: 2023-01-18
video: https://youtu.be/XJHFQUdO4ss （part 1）、https://youtu.be/DV3I-ujKfm8 （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3（書頁 8–11，PDF 頁 27–30）
---

# 第 2 集 · Lecture 2：賦範空間（Normed Linear Spaces） [▶ 影片](https://youtu.be/XJHFQUdO4ss)

← 上一集：[01-vector-spaces](01-vector-spaces.md) ｜ [總目錄](README.md) ｜ 下一集：[03-equivalent-norms](03-equivalent-norms.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 2 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 18:12，自動字幕）＋ Debnath & Mikusiński §1.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 範數的定義](#1-範數的定義)
- [2. 從定義推出的兩個性質](#2-從定義推出的兩個性質)
- [3. 範數的例子](#3-範數的例子)
- [4. 賦範空間](#4-賦範空間)
- [5. 賦範空間中的收斂](#5-賦範空間中的收斂)
- [6. 一致收斂 vs 逐點收斂](#6-一致收斂-vs-逐點收斂)
- [7. 逐點收斂不能用範數描述](#7-逐點收斂不能用範數描述)
- [8. 預告：範數誘導的度量與拓樸](#8-預告範數誘導的度量與拓樸)
- [9. 題外話：超數與四元數](#9-題外話超數與四元數)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 範數定義、$\|x\|\ge0$、反向三角不等式 | Definition 1.3.1，pp. 8–9 |
| $\mathbb{C}^N$ 的三種範數、$C(\Omega)$ 的最大值範數、$\ell^p$ 範數 | Example 1.3.2–1.3.4，p. 9 |
| 賦範空間、收斂、極限律 | Definition 1.3.5–1.3.6，pp. 9–10 |
| 一致收斂 = 最大值範數下的收斂 | Example 1.3.7，pp. 10–11 |
| 逐點收斂沒有對應的範數 | Example 1.3.8，p. 11 |

開場講者提到：課本的向量空間定義比他平常教的「邏輯上更精簡」，所以他當作公理的東西，在課本裡變成要證的結論，這就是第一章前幾題作業的來源（見[第 1 集 §2.2](01-vector-spaces.md#22-課本的寫法)）。他也說對沒在課堂證 Hölder、Minkowski 有點過意不去，其中一個是作業題。[▶ 00:03](https://youtu.be/XJHFQUdO4ss?t=3)

---

## 1. 範數的定義

[▶ 01:13](https://youtu.be/XJHFQUdO4ss?t=73) 課本 Definition 1.3.1。

**範數（norm）**：從向量空間 $E$ 到 $\mathbb{R}$ 的函數 $x\mapsto\|x\|$，滿足

- (a) $\|x\|=0$ ⟹ $x=0$；
- (b) $\|\lambda x\|=|\lambda|\,\|x\|$，對所有 $x\in E$、$\lambda\in\mathbb{F}$；
- (c) $\|x+y\|\le\|x\|+\|y\|$（**三角不等式**）。

講者說他常把範數叫「長度」：範數就是把空間裡的「長度」推廣到任意數學物件。純量體對我們來說是 $\mathbb{R}$ 或 $\mathbb{C}$；他順口說也許可以在有限體或 $p$-進體上做類似的事。【口頭】[▶ 02:51](https://youtu.be/XJHFQUdO4ss?t=171)

---

## 2. 從定義推出的兩個性質

### 2.1 範數非負

[▶ 03:25](https://youtu.be/XJHFQUdO4ss?t=205)

講者自己的筆記會**直接假設** $\|x\|\ge0$（也就是範數是 $E\to[0,\infty)$ 的函數）。課本沒有假設，而是證出來。講者說這跟向量空間定義是同一回事：有的定義重教學（把性質直接寫明），有的定義重邏輯精簡。【口頭】

**證明**：

1. 由 (b) 取 $\lambda=0$：$\|0\|=\|0\cdot x\|=0\cdot\|x\|=0$。
2. 把 $0$ 寫成 $x-x$，用 (c)：
   $$0=\|0\|=\|x-x\|\le\|x\|+\|-x\|.$$
3. 由 (b) 取 $\lambda=-1$：$\|-x\|=|-1|\,\|x\|=\|x\|$。（這裡用到 $(-1)x=-x$，第 1 集的課本性質。）
4. 所以 $0\le2\|x\|$，即 $\|x\|\ge0$。∎

### 2.2 反向三角不等式

[▶ 06:08](https://youtu.be/XJHFQUdO4ss?t=368)

$$\big|\,\|x\|-\|y\|\,\big|\le\|x-y\|.$$

講者課前只準備到一半，在課堂上和學生一起推。

1. 加減 $y$：$\|x\|=\|(x-y)+y\|\le\|x-y\|+\|y\|$，所以
   $$\|x\|-\|y\|\le\|x-y\|. \tag{i}$$
2. $x,y$ 角色互換：$\|y\|=\|(y-x)+x\|\le\|y-x\|+\|x\|$。又 $\|y-x\|=\|-(x-y)\|=\|x-y\|$，所以
   $$\|y\|-\|x\|\le\|x-y\|. \tag{ii}$$
3. 分兩種情況。若 $\|x\|-\|y\|\ge0$，左邊的絕對值就是 (i) 的左邊；若 $<0$，絕對值是 (ii) 的左邊。兩種情況都 $\le\|x-y\|$。∎

再配上三角不等式，得到一整串常用的估計：

$$\big|\,\|x\|-\|y\|\,\big|\le\|x-y\|\le\|x\|+\|y\|.$$

講者的提醒【口頭】[▶ 12:07](https://youtu.be/XJHFQUdO4ss?t=727)：做抽象估計時要記住這一族不等式。例如分母有 $\|x-y\|$，想把分數放大就要把分母縮小，這時就用左邊那條。

---

## 3. 範數的例子

### 3.1 Cᴺ 的三種範數

[▶ 12:40](https://youtu.be/XJHFQUdO4ss?t=760) 課本 Example 1.3.2。$z=(z_1,\dots,z_N)\in\mathbb{C}^N$：

$$\|z\|_2=\sqrt{|z_1|^2+\cdots+|z_N|^2}\ (\text{歐氏範數}),\qquad \|z\|_1=|z_1|+\cdots+|z_N|,\qquad \|z\|_\infty=\max\{|z_1|,\dots,|z_N|\}.$$

下標 $1,2,\infty$ 是講者加的【口頭】，課本沒有命名。他說這跟 ℓᵖ 有關：把 ℓᵖ 的數列**截斷**成有限長，就是 $\mathbb{C}^N$，所以 $\|\cdot\|_1$、$\|\cdot\|_2$ 是 ℓᵖ 範數的有限版；$\|\cdot\|_\infty$ 是「$p\to\infty$」的版本。同時用好幾種範數時，最好用下標區分。

**驗證 (b)**（講者示範）[▶ 14:58](https://youtu.be/XJHFQUdO4ss?t=898)：$\lambda z$ 的每個分量乘了 $\lambda$，

$$\|\lambda z\|_2=\sqrt{|\lambda|^2|z_1|^2+\cdots+|\lambda|^2|z_N|^2}=|\lambda|\sqrt{|z_1|^2+\cdots+|z_N|^2}=|\lambda|\,\|z\|_2.$$

另外兩個同理。

學生問最大值（maximum）和上確界（supremum）的差別。講者：maximum 就是「最大的那個元素」，必須存在於集合裡；supremum 定義得更仔細（最小上界，不一定取得到），很快會用到。[▶ 15:30](https://youtu.be/XJHFQUdO4ss?t=930)

### 3.2 C(Ω) 的最大值範數

[▶ 16:01](https://youtu.be/XJHFQUdO4ss?t=961) 課本 Example 1.3.3。

$\Omega\subseteq\mathbb{R}^N$ 是**閉而且有界**的集合：

- **閉（closed）**：補集是開集。也就是把 $\Omega$ 挖掉後，剩下的每一點都能放一個小球在剩下的區域裡。
- **有界（bounded）**：能找到一個夠大的球把 $\Omega$ 包住。

$$\|f\|=\max_{x\in\Omega}|f(x)|,\qquad f\in C(\Omega).$$

**為什麼 max 存在**[▶ 17:44](https://youtu.be/XJHFQUdO4ss?t=1064)：

1. $\mathbb{R}^N$ 裡閉且有界 ⟹ **緊緻（compact）**（Heine–Borel 定理）。
2. $f$ 連續，絕對值連續，所以 $|f|$ 連續（連續函數的合成）。
3. 緊緻集上的連續實函數取得最大值（極值定理）。所以 max 存在，$\|f\|$ 有定義。

**為什麼是範數**（講者說是「揮揮手」的說明）[▶ 18:52](https://youtu.be/XJHFQUdO4ss?t=1132)：乘一個數，最大值跟著乘那個數的絕對值；三角不等式對絕對值成立，再跟「取最大值」配合，就得到函數範數的三角不等式。

以下**不是逐字稿內容**，是把講者的說明寫成完整步驟：

- (a)：$\|f\|=0$ ⟹ 所有 $x$ 都 $|f(x)|\le0$ ⟹ $f\equiv0$。
- (b)：$\max_x|\lambda f(x)|=\max_x|\lambda||f(x)|=|\lambda|\max_x|f(x)|$。
- (c)：對每個 $x$，$|f(x)+g(x)|\le|f(x)|+|g(x)|\le\|f\|+\|g\|$。右邊與 $x$ 無關，所以左邊取 max 也 $\le\|f\|+\|g\|$。

講者也說：這些他沒證的東西大多是「簡單但沒什麼趣味」的作業題。

### 3.3 ℓᵖ 範數

[▶ 19:30](https://youtu.be/XJHFQUdO4ss?t=1170) 課本 Example 1.3.4。

$$\|z\|_p=\left(\sum_{n=1}^\infty|z_n|^p\right)^{1/p},\qquad z=(z_n)\in\ell^p,\ p\ge1.$$

**Minkowski 不等式就是這個範數的三角不等式。**[▶ 21:41](https://youtu.be/XJHFQUdO4ss?t=1301)

講者提的問題【口頭】[▶ 20:17](https://youtu.be/XJHFQUdO4ss?t=1217)：這是一整族空間。$p=2$ 可和的數列也 $p=3$ 可和嗎？反過來呢？他說他不知道答案，只是問問。

以下**不是逐字稿內容**，是依 ℓᵖ 定義推論的：

- **$p<q$ ⟹ $\ell^p\subseteq\ell^q$。** 若 $\sum|z_n|^p<\infty$，則 $|z_n|\to0$，所以有 $N$ 使 $n>N$ 時 $|z_n|<1$。這時 $|z_n|^q=|z_n|^p\,|z_n|^{q-p}\le|z_n|^p$，比較審斂法得 $\sum|z_n|^q<\infty$。
- **反過來不對。** 例如 $z_n=1/n$：$\sum1/n^2<\infty$，所以 $z\in\ell^2$；但 $\sum1/n=\infty$，所以 $z\notin\ell^1$。

---

## 4. 賦範空間

課本 Definition 1.3.5。**賦範空間（normed space）**：帶有一個範數的向量空間，記成一對 $(E,\|\cdot\|)$。向量空間也叫**線性空間（linear space）**，所以也叫 normed linear space，講者簡寫成 NLS。[▶ 21:41](https://youtu.be/XJHFQUdO4ss?t=1301)

**為什麼要寫成一對**[▶ 22:15](https://youtu.be/XJHFQUdO4ss?t=1335)：同一個向量空間可以放不同的範數（例如 $\mathbb{C}^N$ 上的三種），所以要指明用哪一個。

**預設範數**【課堂討論】[▶ 23:22](https://youtu.be/XJHFQUdO4ss?t=1402)：講者問 $\mathbb{R}^N$ 的慣例是什麼，學生答：歐氏範數。$\|x\|=\sqrt{x\cdot x}$。講者說用點積寫是「偷跑到第 3 章」。Example 1.3.3、1.3.4 的範數也是各自空間的預設範數。

【課本補充】賦範空間的子空間，限制同一個範數，也是賦範空間。

---

## 5. 賦範空間中的收斂

[▶ 24:32](https://youtu.be/XJHFQUdO4ss?t=1472) 課本 Definition 1.3.6。

有了範數就能量距離：$\|x-y\|$ 是 $x$ 到 $y$ 的距離。

**定義**：$(x_n)$ 在 $(E,\|\cdot\|)$ 中**收斂**到 $x\in E$，意思是對每個 $\varepsilon>0$，存在 $M$，使得 $n\ge M$ 時 $\|x_n-x\|<\varepsilon$。記作 $x_n\to x$ 或 $\lim_{n\to\infty}x_n=x$。

課本說「存在一個數 $M$」，講者習慣說「存在自然數 $M$」。[▶ 26:27](https://youtu.be/XJHFQUdO4ss?t=1587)這跟實數列收斂的定義一模一樣，只是**絕對值換成範數**。

課本接著說：「用實數列的收斂，定義更簡單：$x_n\to x$ 就是 $\|x_n-x\|\to0$（在 $\mathbb{R}$ 中）」。講者讀到這句時覺得是筆誤，認為那裡應該是絕對值，不然只是在重複。[▶ 27:33](https://youtu.be/XJHFQUdO4ss?t=1653)

> 以下**不是逐字稿內容**，是依課本原文判斷的：課本這句讀起來沒有錯。它的意思是把向量的收斂化成**實數列** $a_n=\|x_n-x\|$ 收斂到 $0$。

### 收斂的基本性質（極限律）

[▶ 28:06](https://youtu.be/XJHFQUdO4ss?t=1686) 課本 p. 10 列出三條，說「證法跟 $\mathbb{R}$ 一樣」：

1. 收斂數列的極限唯一。
2. $x_n\to x$、$\lambda_n\to\lambda$（$\lambda_n,\lambda$ 是純量）⟹ $\lambda_nx_n\to\lambda x$。
3. $x_n\to x$、$y_n\to y$ ⟹ $x_n+y_n\to x+y$。

**3 的證明**【課堂討論】[▶ 30:04](https://youtu.be/XJHFQUdO4ss?t=1804)：學生提出做法，講者寫下。

給 $\varepsilon>0$。取 $M_x$ 使 $n\ge M_x$ 時 $\|x_n-x\|<\varepsilon/2$，取 $M_y$ 使 $n\ge M_y$ 時 $\|y_n-y\|<\varepsilon/2$。令 $M=\max\{M_x,M_y\}$。$n\ge M$ 時

$$\|(x_n+y_n)-(x+y)\|=\|(x_n-x)+(y_n-y)\|\le\|x_n-x\|+\|y_n-y\|<\tfrac\varepsilon2+\tfrac\varepsilon2=\varepsilon.\ ∎$$

**2 的證明**（課堂只做到一半）[▶ 32:57](https://youtu.be/XJHFQUdO4ss?t=1977)

講者說這條比較難：當 $E=\mathbb{R}$ 時，它就變成「乘積的極限 = 極限的乘積」，那本來就不簡單。他試著加減一項：

$$\lambda_nx_n-\lambda x=(\lambda_n-\lambda)x_n+\lambda(x_n-x),$$

所以

$$\|\lambda_nx_n-\lambda x\|\le|\lambda_n-\lambda|\,\|x_n\|+|\lambda|\,\|x_n-x\|.$$

學生指出：接下來需要「**收斂數列有界**」。講者同意，說「這不簡單」，停在這裡。他提到微積分裡 $\lim f\cdot g$ 也有同樣的困難，他後來在維基百科看到一個漂亮的巧妙論證，放進了自己的微積分筆記。[▶ 36:35](https://youtu.be/XJHFQUdO4ss?t=2195)

以下**不是逐字稿內容**，是把課堂的思路補完：

- **收斂數列有界**：取 $\varepsilon=1$，有 $M$ 使 $n\ge M$ 時 $\|x_n-x\|<1$，所以 $\|x_n\|\le\|x_n-x\|+\|x\|<1+\|x\|$。前面有限多項各有一個值，取 $K=\max\{\|x_1\|,\dots,\|x_{M-1}\|,1+\|x\|\}$，則所有 $\|x_n\|\le K$。
- **完成證明**：給 $\varepsilon>0$。取 $M_1$ 使 $n\ge M_1$ 時 $|\lambda_n-\lambda|<\dfrac{\varepsilon}{2K}$；取 $M_2$ 使 $n\ge M_2$ 時 $\|x_n-x\|<\dfrac{\varepsilon}{2(|\lambda|+1)}$。$n\ge\max\{M_1,M_2\}$ 時
  $$\|\lambda_nx_n-\lambda x\|<\frac{\varepsilon}{2K}\cdot K+|\lambda|\cdot\frac{\varepsilon}{2(|\lambda|+1)}<\varepsilon.$$
  （分母寫 $|\lambda|+1$ 是為了 $\lambda=0$ 時也能用。）∎
- **1（極限唯一）**：若 $x_n\to x$ 且 $x_n\to y$，則 $\|x-y\|\le\|x-x_n\|+\|x_n-y\|\to0$。所以 $\|x-y\|=0$，由 (a) 得 $x=y$。∎

---

## 6. 一致收斂 vs 逐點收斂

課本開始問反過來的問題：先有一種收斂，能不能找到一個範數剛好描述它？有時可以（Example 1.3.7），有時不行（Example 1.3.8）。

### 6.1 一致收斂

[▶ 39:00](https://youtu.be/XJHFQUdO4ss?t=2340) 課本 Example 1.3.7。

講者先複習：$\mathbb{R}^N$ 中閉且有界的集合是緊緻的（Heine–Borel，學生在實分析學過 $\mathbb{R}$ 的版本）。緊緻有不同的定義：拓樸的定義是「每個開覆蓋都有有限子覆蓋」，另外還有用數列定義的「序列緊緻」，後面會講。[▶ 40:09](https://youtu.be/XJHFQUdO4ss?t=2409)

**定義**：$\Omega$ 閉且有界，$f_1,f_2,\ldots\in C(\Omega)$。$(f_n)$ **一致收斂（uniformly convergent）**到 $f$，意思是對每個 $\varepsilon>0$，存在 $n_0$，使得

$$|f(x)-f_n(x)|<\varepsilon\quad\text{對所有 } x\in\Omega \text{ 和所有 } n\ge n_0.$$

**課本的主張**[▶ 43:08](https://youtu.be/XJHFQUdO4ss?t=2588)：$(f_n)$ 一致收斂到 $f$ ⟺

$$\|f_n-f\|=\max_{x\in\Omega}|f_n(x)-f(x)|\to0.$$

所以最大值範數也叫**一致收斂範數（uniform convergence norm）**。

講者說這裡同時有兩件複雜的事：一是 $n\to\infty$，二是要掃過空間裡**所有的** $x$。[▶ 44:00](https://youtu.be/XJHFQUdO4ss?t=2640)

以下**不是逐字稿內容**，是課本說「easy to see」那步的推導：

- (⟸) 若 $\|f_n-f\|<\varepsilon$，則每個 $x$ 都有 $|f_n(x)-f(x)|\le\max|f_n-f|<\varepsilon$。
- (⟹) 若所有 $x$ 都 $|f_n(x)-f(x)|<\varepsilon$，在緊緻集上 max 是某一點取到的值，所以 $\max|f_n-f|<\varepsilon$。

### 6.2 逐點收斂

[▶ 45:21](https://youtu.be/XJHFQUdO4ss?t=2721)

**定義**：$(f_n)$ **逐點收斂（pointwise convergent）**到 $f$，意思是對**每個** $t$，$|f_n(t)-f(t)|\to0$，也就是 $\lim_{n\to\infty}f_n(t)=f(t)$。

**差別在 $n_0$ 能不能跟著點改變**[▶ 48:32](https://youtu.be/XJHFQUdO4ss?t=2912)：

| | $n_0$ 依賴什麼 |
|---|---|
| 逐點收斂 | 對每個 $t$ 可以選**不同的** $n_0(t)$ |
| 一致收斂 | **同一個** $n_0$ 要對所有 $t$ 都有效 |

**圖像**【口頭】[▶ 49:45](https://youtu.be/XJHFQUdO4ss?t=2985)：在 $f$ 的圖形上下畫一條寬 $\pm\varepsilon$（例如 $\pm\frac14$）的帶子。一致收斂：$n$ 夠大之後，$f_n$ 的**整條圖形**都要擠進帶子裡；前面的 $f_1$ 可以亂七八糟。逐點收斂：只看一個點，在那一點過了某個 $n$ 之後夠靠近就好，但那個 $n$ 不必對所有點都有效。講者說課本 p. 15 有類似的圖。

講者的看法【口頭】[▶ 52:05](https://youtu.be/XJHFQUdO4ss?t=3125)：一致收斂有很多好定理，逐點收斂沒有。逐點收斂是比較直覺、會先想到的概念，但課本接下來的例子在說：它其實是一種「不自然」的收斂。

---

## 7. 逐點收斂不能用範數描述

[▶ 52:38](https://youtu.be/XJHFQUdO4ss?t=3158) 課本 Example 1.3.8，p. 11。

**主張**：$C([0,1])$ 上**不存在**範數 $\|\cdot\|$，使得

$$\|f_n-f\|\to0\iff f_n(t)\to f(t)\ \text{對每個 } t\in[0,1]. \tag{1.7}$$

**證明（反證法）**：假設有這樣的範數。

**Step 1：帳篷函數。**[▶ 55:29](https://youtu.be/XJHFQUdO4ss?t=3329)

$$g_n(t)=\begin{cases}2^nt, & 0\le t\le2^{-n}\\ 2-2^nt, & 2^{-n}\le t\le2^{1-n}\\ 0, & \text{其他}\end{cases}$$

講者的建議【口頭】：分析書裡看到這種式子，先**畫圖**。

- $n=1$：從 $0$ 以斜率 $2$ 爬到 $t=\frac12$ 的高度 $1$，再以斜率 $-2$ 下降到 $t=1$ 的 $0$。一個尖峰。
- $n=4$：在 $[0,\frac1{16}]$ 爬到 $1$，在 $[\frac1{16},\frac18]$ 降回 $0$，之後都是 $0$。

所以 $g_n$ 是一頂**高度 1、越來越窄、往 $0$ 擠的帳篷**。

**Step 2：正規化。**[▶ 59:33](https://youtu.be/XJHFQUdO4ss?t=3573) $g_n$ 不是零函數，所以 $\|g_n\|\ne0$。令

$$f_n=\frac{g_n}{\|g_n\|}.$$

講者說：除以自己的長度，長度就變成 1；物理課會寫成 $\hat g$。這個正規化的技巧本節後面還會再用。[▶ part 2 00:01](https://youtu.be/DV3I-ujKfm8?t=1) 所以 $\|f_n\|=1$，$\|f_n-0\|=1\not\to0$：在這個範數下 $f_n$ **不收斂到零函數**。

**Step 3：可是 $f_n$ 逐點收斂到 $0$。**[▶ part 2 01:48](https://youtu.be/DV3I-ujKfm8?t=108)

- $t=0$：$g_n(0)=0$，所以 $f_n(0)=0$。
- $t>0$：只要 $2^{1-n}<t$，$t$ 就在帳篷右邊，$g_n(t)=0$，所以 $f_n(t)=0$。$n$ 夠大之後一直是 $0$。

講者說這裡「有個小缺口」：我們不知道這個假想範數的公式，所以不知道 $\|g_n\|$ 是多少，$f_n$ 的尖峰高度 $1/\|g_n\|$ 可能很大。[▶ part 2 03:01](https://youtu.be/DV3I-ujKfm8?t=181)他接著說明為什麼不影響：**每個固定的 $t>0$，$n$ 夠大後 $f_n(t)$ 恰好等於 $0$**，不管乘上的常數多大都一樣。

**Step 4：矛盾。** 由 (1.7)，逐點收斂到 $0$ ⟹ $\|f_n-0\|\to0$。但 $\|f_n\|=1$。矛盾。∎

【課堂討論】[▶ part 2 16:55](https://youtu.be/DV3I-ujKfm8?t=1015) 學生覺得奇怪：極限是 $0$，可是帳篷一直在。講者說要分清楚「**函數在某點的值是 0**」和「**函數是零函數**」。範數為 $0$ ⟺ 是零函數，要在整個 $[0,1]$ 都等於 $0$。對每個有限的 $n$，總有一頂帳篷，所以 $f_n$ 永遠不是零函數；但每一個固定點最後都變成 $0$。

---

## 8. 預告：範數誘導的度量與拓樸

[▶ part 2 04:16](https://youtu.be/DV3I-ujKfm8?t=256) 下一堂講**範數等價**：在有限維空間，所有範數給出同樣的收斂。

講者先預告 §1.3 後半【口頭】：

- 每個賦範空間都有**度量（metric，距離函數）** $d(x,y)=\|x-y\|$：
  - 對稱：$\|x-y\|=\|y-x\|$；
  - $d(x,x)=\|0\|=0$（今天證過）；
  - 三角不等式。
- 有了度量就有**度量拓樸（metric topology）**：一個集合是開集，意思是每一點都是內點，也就是能用這個距離畫一個 $\varepsilon$ 球放進去。
- 有限維時，各種範數誘導的拓樸**全都一樣**：在 2-範數下開，等價於在 sup 範數下開，等價於在 1-範數下開。
- **無限維時不是這樣**，不同的收斂方式會開始不同。

---

## 9. 題外話：超數與四元數

【口頭】[▶ part 2 07:17](https://youtu.be/DV3I-ujKfm8?t=437)

- **超數（super numbers）**：講者博士論文的研究對象。像 ℓᵖ，是無窮級數，係數是複數，乘上 **Grassmann 生成元**的乘積。Grassmann 生成元**反交換**：$\eta_1\eta_2=-\eta_2\eta_1$，所以 $\eta_1\eta_1=0$。研究時他們一度不確定該用 1-範數還是 2-範數，後來相信兩者等價，但他現在也記不清當時的根據。
- **四元數（quaternions）**：$t+ai+bj+ck$，$i^2=j^2=k^2=-1$，$ij=k=-ji$。講者說：兩個四元數相乘，純量部分是點積，向量部分是叉積。（以下**不是逐字稿內容**，是依 $i^2=j^2=k^2=-1$ 推論的：精確地說，兩個純向量四元數 $u,v$ 相乘得 $uv=-u\cdot v+u\times v$，純量部分是**負的**點積。）
  - 四元數「幾乎是體」：每個非零元素都有乘法反元素，但乘法**不交換**，所以叫**除環（skew field）**。
  - 四元數的範數**可乘**：$|zw|=|z||w|$。由此可推出**四平方和恆等式**。一般的結合代數通常只有次可乘：$\|zw\|\le C\|z\|\|w\|$。
- 講者的猜想：超數也像四元數，是一個無限維的除環（每個非零超數有反元素），但他還沒證出來。他也在找學生一起研究超流形的拓樸問題。

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 範數 | (a) $\|x\|=0\Rightarrow x=0$；(b) $\|\lambda x\|=|\lambda|\|x\|$；(c) 三角不等式 | |
| 非負 | $\|x\|\ge0$ | $0=\|x-x\|\le\|x\|+\|-x\|=2\|x\|$ |
| 反向三角 | $\big|\|x\|-\|y\|\big|\le\|x-y\|$ | $\|x\|=\|(x-y)+y\|$，再 $x\leftrightarrow y$ |
| $\mathbb{C}^N$ | $\|\cdot\|_1,\|\cdot\|_2,\|\cdot\|_\infty$ | 預設是歐氏 $\|\cdot\|_2$ |
| $C(\Omega)$，$\Omega$ 閉有界 | $\|f\|=\max_\Omega|f|$ | max 存在：Heine–Borel + 極值定理 |
| $\ell^p$ | $\|z\|_p=(\sum|z_n|^p)^{1/p}$ | 三角不等式 = Minkowski |
| $\ell^p$ 包含 | $p<q\Rightarrow\ell^p\subseteq\ell^q$ | 尾巴 $|z_n|<1$，$|z_n|^q\le|z_n|^p$ |
| 收斂 | $\|x_n-x\|\to0$ | 實數列定義把 $|\cdot|$ 換成 $\|\cdot\|$ |
| 和的極限 | $x_n+y_n\to x+y$ | $\varepsilon/2$ + 三角不等式 |
| 純量積的極限 | $\lambda_nx_n\to\lambda x$ | 加減 $\lambda x_n$；需要「收斂數列有界」 |
| 一致收斂 | $\max|f_n-f|\to0$ | 同一個 $n_0$ 對所有點有效 |
| 逐點收斂 | 每個 $t$：$f_n(t)\to f(t)$ | $n_0$ 可依 $t$ 改變 |
| 逐點收斂無範數 | 反證：帳篷 $g_n$ 正規化成 $f_n$ | $\|f_n\|=1$ 但 $f_n(t)\to0$ 逐點 |
| 誘導度量 | $d(x,y)=\|x-y\|$ | 開集 = 每點是內點 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 範數等價、有限維所有範數等價 | 第 3 集（equivalent norms） |
| 開集、閉集、緊緻、序列緊緻 | 第 4–5 集 |
| 一致收斂範數、$C(\Omega)$ | 第 6 集：$C(\Omega)$ 是 Banach 空間；第 9 集：微分方程存在定理 |
| 正規化 $g/\|g\|$ 的技巧 | 第 3 集（範數等價的證明，Theorem 1.3.11） |
| 逐點收斂 vs 範數收斂 | 第 14 集（幾乎處處收斂 vs 範數收斂） |

---

## 附：本集一句話總結

> **範數是抽象的「長度」，三條公理就能推出非負與反向三角不等式；有了範數就有收斂。最大值範數剛好描述一致收斂，但逐點收斂不能被任何範數描述——正規化後的窄帳篷函數，長度永遠是 1，卻逐點收斂到 0。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」Lecture 2（2023-01-18）錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 18:12）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3 整理。*
