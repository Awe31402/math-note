---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 19
lecture: Lecture 19
date: 2023-03-01
video: https://youtu.be/qA9AddZqUzQ （part 1）、https://youtu.be/6RNbsAF1Rcc （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.3 Example 3.3.7–Theorem 3.3.15（書頁 100–105，PDF 頁 119–124）
---

# 第 19 集 · 加權空間、Sobolev 空間、強收斂與弱收斂 [▶ 影片](https://youtu.be/qA9AddZqUzQ)

← 上一集：[18-inner-product-hilbert-spaces](18-inner-product-hilbert-spaces.md) ｜ [總目錄](README.md) ｜ 下一集：[20-orthogonal-systems](20-orthogonal-systems.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 19 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 9:12，自動字幕）＋ Debnath & Mikusiński §3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 加權 L² 空間](#1-加權-l²-空間)
- [2. Sobolev 空間](#2-sobolev-空間)
- [3. 強收斂與弱收斂](#3-強收斂與弱收斂)
- [4. 強收斂 ⟹ 弱收斂](#4-強收斂--弱收斂)
- [5. 內積對強收斂連續](#5-內積對強收斂連續)
- [6. 弱收斂 + 範數收斂 ⟹ 強收斂](#6-弱收斂--範數收斂--強收斂)
- [7. 只要在稠密集上檢查](#7-只要在稠密集上檢查)
- [8. 弱收斂數列有界](#8-弱收斂數列有界)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 加權 $L^2$ 空間 $L^{2,\rho}([a,b])$ | Example 3.3.7，pp. 100–101 |
| Sobolev 空間 $H^m(\Omega)$ | Example 3.3.8，pp. 101–102 |
| 強收斂、弱收斂 | Definition 3.3.9–3.3.10，p. 102 |
| 強 ⟹ 弱；內積的連續性 | Theorem 3.3.11–3.3.12，pp. 102–103 |
| 弱 + 範數 ⟹ 強；稠密集上檢查；弱收斂有界 | Theorem 3.3.13–3.3.15，pp. 103–105 |

講者說這兩個例子之後會讓人體會它們的重要性；Sobolev 空間「比較冒險一點」。[▶ 00:02](https://youtu.be/qA9AddZqUzQ?t=2)

---

## 1. 加權 L² 空間

[▶ 00:39](https://youtu.be/qA9AddZqUzQ?t=39) 課本 Example 3.3.7。

**權函數（weight function）** $\rho$：$[a,b]$ 上的可測函數，$\rho(x)>0$ **幾乎處處**。講者：「大部分是正的，也許有幾個點不乖。」上一集的 $L^2$ 就是 $\rho=1$ 的情形。

**空間**：$L^{2,\rho}([a,b])$ = 所有複值可測函數 $f$，使

$$\int_a^b|f(x)|^2\rho(x)\,dx<\infty.$$

**內積**[▶ 02:36](https://youtu.be/qA9AddZqUzQ?t=156)：

$$\langle f,g\rangle=\int_a^bf(x)\overline{g(x)}\rho(x)\,dx.$$

**是內積**[▶ 03:42](https://youtu.be/qA9AddZqUzQ?t=222)：

- 正定：$\langle f,f\rangle=\int|f|^2\rho$，正的東西積分是正的。若為 0，則 $f=0$ 幾乎處處。講者提醒：我們一直在處理的其實是「幾乎處處相等」的**等價類**，不是函數，這件事一直都在。
- 第一位置線性、第二位置共軛線性：由積分的線性和共軛的位置直接得到。

**完備性**（較技術）[▶ 05:31](https://youtu.be/qA9AddZqUzQ?t=331)：

1. $(f_n)$ 在 $L^{2,\rho}$ 中是 Cauchy：$\|f_m-f_n\|^2_{L^{2,\rho}}=\int|f_m-f_n|^2\rho\to0$。
2. **換到普通 $L^2$**：令 $F_n=f_n\sqrt\rho$。則
   $$\|F_m-F_n\|^2_{L^2}=\int\left|f_m\sqrt\rho-f_n\sqrt\rho\right|^2=\int|f_m-f_n|^2\rho=\|f_m-f_n\|^2_{L^{2,\rho}}.$$
   所以 $(F_n)$ 是 $L^2([a,b])$ 中的 Cauchy 數列。講者說：用權函數重新縮放，正是讓 $f_n$ 落進 $L^2$ 需要的。
3. $L^2([a,b])$ 完備（已證），所以 $F_n\to F\in L^2([a,b])$。
4. **候選極限**：$f=F/\sqrt\rho$。講者一開始說「除以 $\rho$」，算到一半發現不對：要除以 $\sqrt\rho$，平方後才會跑出一個 $\rho$。[▶ 13:23](https://youtu.be/qA9AddZqUzQ?t=803)
5. 則 $\|f_n-f\|^2_{L^{2,\rho}}=\int\left|\frac{F_n-F}{\sqrt\rho}\right|^2\rho=\|F_n-F\|^2_{L^2}\to0$，而且 $f\in L^{2,\rho}$。∎

**關鍵一步**：$f\mapsto f\sqrt\rho$ 是 $L^{2,\rho}$ 到 $L^2$ 的保距映射，完備性直接搬過來。

---

## 2. Sobolev 空間

[▶ 15:08](https://youtu.be/qA9AddZqUzQ?t=908) 課本 Example 3.3.8。

$\Omega$ 是 $\mathbb{R}^N$ 的開集，$m=1,2,\dots$。

### 多重指標記號

[▶ 17:25](https://youtu.be/qA9AddZqUzQ?t=1045)

**多重指標（multi-index）** $\alpha=(\alpha_1,\dots,\alpha_N)$，$\alpha_k$ 是**非負**整數，$|\alpha|=\alpha_1+\cdots+\alpha_N$，

$$D^\alpha f=\frac{\partial^{|\alpha|}f}{\partial x_1^{\alpha_1}\partial x_2^{\alpha_2}\cdots\partial x_N^{\alpha_N}}.$$

講者一開始不懂課本為什麼要列出所有 $N$ 個分量；他習慣不寫為 0 的。後來想通：允許 $\alpha_k=0$，一個記號就涵蓋所有偏導數。[▶ 20:37](https://youtu.be/qA9AddZqUzQ?t=1237)

**例**：$N=4$，$\alpha=(2,0,0,1)$，$|\alpha|=3$，$D^\alpha f=\dfrac{\partial^3f}{\partial x_1^2\partial x_4}$；0 的那幾個方向就不出現。（課本例：$N=2$，$\alpha=(2,1)$，$D^\alpha f=\frac{\partial^3f}{\partial x_1^2\partial x_2}$。）

**「$|\alpha|\le m$」涵蓋了什麼**[▶ 22:23](https://youtu.be/qA9AddZqUzQ?t=1343)：

- $|\alpha|=1$：只有一個分量是 1，就是所有一階偏導數。
- $|\alpha|=2$：兩個分量各是 1（混合偏導），或一個分量是 2（二階純偏導）。
- $|\alpha|=3$：三重混合、二階加一階、或三階純偏導。

「一個記號同時處理所有組合情況，非常漂亮。」講者說組合上很多，代數上跟對稱多項式是同一種東西。他說學生本來會在多變數分析課學到，學校沒開；他提到如果他當年沒離開、高等微積分課開成了，情況可能不同，「不過我認識了 Audric，所以都好」。

### 空間與內積

$\tilde H^m(\Omega)$：所有 $f\in C^m(\Omega)$（偏導數到 $m$ 階都存在且連續），使 $D^\alpha f\in L^2(\Omega)$ 對所有 $|\alpha|\le m$；也就是

$$\int_\Omega|D^\alpha f|^2<\infty\quad\text{對所有 }|\alpha|\le m.$$

**內積**[▶ 25:26](https://youtu.be/qA9AddZqUzQ?t=1526)：

$$\langle f,g\rangle=\int_\Omega\sum_{|\alpha|\le m}D^\alpha f\,\overline{D^\alpha g}.$$

【課本補充】例：$\Omega\subseteq\mathbb{R}^2$，$m=2$：

$$\langle f,g\rangle=\int_\Omega\left(f\bar g+f_x\bar g_x+f_y\bar g_y+f_{xx}\bar g_{xx}+f_{yy}\bar g_{yy}+f_{xy}\bar g_{xy}\right).$$

$\Omega=(a,b)\subset\mathbb{R}$：$\langle f,g\rangle=\int_a^b\sum_{n=0}^m\dfrac{d^nf}{dx^n}\overline{\dfrac{d^ng}{dx^n}}$。

**是內積**[▶ 27:57](https://youtu.be/qA9AddZqUzQ?t=1677)：偏導數線性、積分線性、和線性，加上共軛，就有共軛線性與共軛對稱。

**正定**：$\langle f,f\rangle=\int\sum_\alpha|D^\alpha f|^2$ 是一堆非負項的積分。講者一開始想要不要用到導數，後來說：如果 $f$ 在某點不為 0，因為 $f$ **連續**，它在那點的一個鄰域都不為 0，積分 $|f|^2$ 就有正的貢獻，矛盾。「根本不需要導數項。」[▶ 29:39](https://youtu.be/qA9AddZqUzQ?t=1779)

**不完備，取完備化**[▶ 30:13](https://youtu.be/qA9AddZqUzQ?t=1813)：$\tilde H^m(\Omega)$ 是內積空間但**不完備**（所以加了波浪號）。它的完備化記作

$$H^m(\Omega)$$

是 Hilbert 空間，叫 **Sobolev 空間**。它是更一般的 $W^{m,p}(\Omega)$ 的 $p=2$ 情形：$H^m(\Omega)=W^{m,2}(\Omega)$（§6.3）。Sergei Lvovich Sobolev（1908–1989）。

講者【口頭】[▶ 31:54](https://youtu.be/qA9AddZqUzQ?t=1914)：1989 年對他的意義是「開始看得出棒球卡是糟糕投資的那一年，我早該那時賣掉」。Sobolev 空間是**偏微分方程**分析的大本營之一。他說自己不是專家：PDE 一直出現在他的工作裡，但他從沒修過專門的 PDE 分析課，大學只修過「解」PDE 的課；之後會給學生看一些具體計算。PDE 是物理、工程、應用微積分的重要部分，學校沒開這門課很可惜。

---

## 3. 強收斂與弱收斂

[▶ 34:04](https://youtu.be/qA9AddZqUzQ?t=2044) 課本 Definition 3.3.9–3.3.10。

$E$ 是內積空間。

| | 定義 | 記號 |
|---|---|---|
| **強收斂（strong convergence）** | $\|x_n-x\|\to0$（誘導範數） | $x_n\to x$ |
| **弱收斂（weak convergence）** | $\langle x_n,y\rangle\to\langle x,y\rangle$ 對**每個** $y\in E$ | $x_n\xrightarrow{w}x$ |

講者：弱收斂看的是內積，強收斂就是我們平常的收斂。

---

## 4. 強收斂 ⟹ 弱收斂

[▶ 36:39](https://youtu.be/qA9AddZqUzQ?t=2199) 課本 Theorem 3.3.11。

**定理**：$x_n\to x$ ⟹ $x_n\xrightarrow{w}x$（同一個極限）。

**證明**（講者寫成 $\varepsilon$ 形式）：固定 $y\ne0$。給 $\varepsilon>0$，取 $N$ 使 $n\ge N$ 時 $\|x_n-x\|<\frac{\varepsilon}{\|y\|}$。則

$$|\langle x_n,y\rangle-\langle x,y\rangle|=|\langle x_n-x,y\rangle|\le\|x_n-x\|\,\|y\|<\varepsilon.$$

第一個等號是第一位置的可加性，接著用 **Schwarz**。

講者指出缺口：這只處理了 $y\ne0$。$y=0$ 時兩邊都是 0（任何向量跟 0 的內積是 0），零數列收斂到 0，所以也對。[▶ 40:42](https://youtu.be/qA9AddZqUzQ?t=2442)∎

【課本補充】反過來一般不成立，例子在 §3.4。另外：對固定的 $y$，$x\mapsto\langle x,y\rangle$ 是 $E$ 上的線性泛函，這個定理說它**連續**。

> 以下**不是逐字稿內容**，是預告 §3.4 的例子：$\ell^2$ 中 $e_n=(0,\dots,0,1,0,\dots)$（第 $n$ 位是 1）。對任何 $y\in\ell^2$，$\langle e_n,y\rangle=\bar y_n\to0$（$\sum|y_n|^2<\infty$），所以 $e_n\xrightarrow{w}0$；但 $\|e_n-0\|=1$，不強收斂。

---

## 5. 內積對強收斂連續

[▶ 41:52](https://youtu.be/qA9AddZqUzQ?t=2512) 課本 Theorem 3.3.12。

**定理**：$x_n\to x$、$y_n\to y$ ⟹ $\langle x_n,y_n\rangle\to\langle x,y\rangle$。

講者問學生猜結論；說自己被物理課累壞了。

**證明**：中間「加 0」再用三角不等式：

$$\begin{aligned}|\langle x_n,y_n\rangle-\langle x,y\rangle|&\le|\langle x_n,y_n\rangle-\langle x,y_n\rangle|+|\langle x,y_n\rangle-\langle x,y\rangle|\\&=|\langle x_n-x,y_n\rangle|+|\langle x,y_n-y\rangle|\\&\le\|x_n-x\|\,\|y_n\|+\|x\|\,\|y_n-y\|.\end{aligned}$$

講者提醒：第二位置雖然是共軛線性，**可加性**仍然成立，減法照常用（學生補充：也可以先取共軛把問題翻過去）。[▶ 43:43](https://youtu.be/qA9AddZqUzQ?t=2623)

**為什麼 $\to0$**（講者不寫 $\varepsilon$，只說明控制）：$\|x_n-x\|$、$\|y_n-y\|$ 能任意小；收斂數列有界，所以 $\|y_n\|\le K$；$\|x\|$ 只是個數。【課堂討論】學生提出取兩個指標的最大值，讓第一項 $<\frac\varepsilon{2K}\cdot K$、第二項 $<\|x\|\cdot\frac{\varepsilon}{2\|x\|}$；講者補充 $x=0$ 等特殊情況更簡單。[▶ 45:35](https://youtu.be/qA9AddZqUzQ?t=2735)∎

**推論 (3.9)**[▶ 46:46](https://youtu.be/qA9AddZqUzQ?t=2806)：取 $y_n=x_n$：

$$x_n\to x\ \Longrightarrow\ \|x_n\|=\sqrt{\langle x_n,x_n\rangle}\to\sqrt{\langle x,x\rangle}=\|x\|.$$

【課本補充】下一節會看到 Theorem 3.3.12 和 (3.9) 對**弱**收斂不一定成立（上面的 $e_n$：$e_n\xrightarrow{w}0$，但 $\|e_n\|=1\not\to0$）。

---

## 6. 弱收斂 + 範數收斂 ⟹ 強收斂

[▶ 47:57](https://youtu.be/qA9AddZqUzQ?t=2877) 課本 Theorem 3.3.13。

**定理**：$x_n\xrightarrow{w}x$ 而且 $\|x_n\|\to\|x\|$ ⟹ $x_n\to x$。

講者強調：$\|x_n\|\to\|x\|$ 不是 Hilbert 空間裡的收斂，是**實數**的收斂。

【課本補充】證明（課堂沒寫）：弱收斂取 $y=x$ 得 $\langle x_n,x\rangle\to\|x\|^2$。所以

$$\|x_n-x\|^2=\|x_n\|^2-2\operatorname{Re}\langle x_n,x\rangle+\|x\|^2\to\|x\|^2-2\|x\|^2+\|x\|^2=0.$$

---

## 7. 只要在稠密集上檢查

[▶ 48:30](https://youtu.be/qA9AddZqUzQ?t=2910) 課本 Theorem 3.3.14。

**定理**：$S\subseteq E$，$\operatorname{span}S$ 在 $E$ 中稠密。若 $(x_n)$ **有界**，而且 $\langle x_n,y\rangle\to\langle x,y\rangle$ 對每個 $y\in S$，則 $x_n\xrightarrow{w}x$。

講者：$\operatorname{span}S$ 是所有**有限**線性組合 $\sum_{i=1}^nc_is_i$。這定理說弱收斂只要對一個「張成稠密子空間」的集合檢查就好。在平面上兩個向量就張成整個平面，所以這在無限維才比較狡猾。[▶ 52:08](https://youtu.be/qA9AddZqUzQ?t=3128)

講者說證明是 $\varepsilon/3$ 論證，讓他想起「一致收斂的連續函數列極限連續」那個 $\varepsilon/3$ 證明（第 6 集）；跳過。

【課本補充】證明概要：對 $y\in\operatorname{span}S$ 由線性也成立。任取 $z\in E$，設 $\|x\|,\|x_n\|\le M$。取 $y_0\in\operatorname{span}S$ 使 $\|z-y_0\|<\frac{\varepsilon}{3M}$，再取 $n_0$ 使 $n>n_0$ 時 $|\langle x_n,y_0\rangle-\langle x,y_0\rangle|<\frac\varepsilon3$。則

$$|\langle x_n,z\rangle-\langle x,z\rangle|\le\underbrace{\|x_n\|\|z-y_0\|}_{<\varepsilon/3}+\underbrace{|\langle x_n,y_0\rangle-\langle x,y_0\rangle|}_{<\varepsilon/3}+\underbrace{\|x\|\|y_0-z\|}_{<\varepsilon/3}.$$

（「有界」這個假設就用在這裡。）

---

## 8. 弱收斂數列有界

[▶ 54:14](https://youtu.be/qA9AddZqUzQ?t=3254) 課本 Theorem 3.3.15。課本說證明「不初等」，要用 Banach–Steinhaus。

**定理**：Hilbert 空間中的弱收斂數列有界：$x_n\xrightarrow{w}x$ ⟹ 存在 $M$ 使 $\|x_n\|\le M$ 對所有 $n$。

**證明**[▶ 55:33](https://youtu.be/qA9AddZqUzQ?t=3333)：

1. 定義 $f_n:H\to\mathbb{C}$，$f_n(x)=\langle x,x_n\rangle$。

   【課堂討論】[▶ 59:37](https://youtu.be/qA9AddZqUzQ?t=3577) 學生指出 $x$ 要放在**第一個位置**，$f_n$ 才是線性泛函（放第二位置會是共軛線性）。講者同意。
2. **$f_n$ 是有界線性泛函**：課本說「由 Theorem 3.3.11」。講者讀到這句一開始想不通，後來說：「我讀到一句看不懂的話，通常是因為那句是個**主張**，下一段才會證。」最後他認為後面的論證本身就證明了有界。[▶ 57:39](https://youtu.be/qA9AddZqUzQ?t=3459)（由 Schwarz：$|f_n(x)|\le\|x\|\|x_n\|$。）
3. **逐點有界**：對每個 $x$，$\langle x_n,x\rangle\to\langle x,x\rangle$（弱收斂）。取共軛：$\langle x,x_n\rangle\to\langle x,x\rangle$。收斂數列有界，所以 $|f_n(x)|\le M_x$ 對所有 $n$。[▶ part 2 00:05](https://youtu.be/6RNbsAF1Rcc?t=5)
4. **Banach–Steinhaus**（第 8 集，$H$ 是 Banach 空間）：存在**一致**的 $M$ 使 $\|f_n\|\le M$ 對所有 $n$。講者：「他拿出了大砲……一個統領全部的常數。」[▶ part 2 02:29](https://youtu.be/6RNbsAF1Rcc?t=149)
5. **$\|f_n\|=\|x_n\|$**[▶ part 2 03:46](https://youtu.be/6RNbsAF1Rcc?t=226)：
   - 由 Schwarz，$|f_n(x)|\le\|x\|\|x_n\|$，所以 $\|f_n\|\le\|x_n\|$。
   - 另一方面 $f_n(x_n)=\langle x_n,x_n\rangle=\|x_n\|^2$，代入單位向量 $x_n/\|x_n\|$ 得值 $\|x_n\|$，所以 $\|f_n\|\ge\|x_n\|$。

   講者說要回到第 1 章算子範數的定義：$\|f_n\|=\sup_{\|x\|=1}|f_n(x)|$。
6. 所以 $\|x_n\|=\|f_n\|\le M$。∎

講者說他中途有點迷路，但「不懂的地方，回第 1 章看定義，一切就會歸位」。[▶ part 2 08:06](https://youtu.be/6RNbsAF1Rcc?t=486)

**下一堂**：正交與正規正交系統。講者：「我愛正交、愛正規正交，永遠不會膩。它們是最好的基底……無限維會有很多令人驚訝的定理。」

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 加權 $L^2$ | $\langle f,g\rangle=\int_a^bf\bar g\rho$，$\rho>0$ a.e. | $F=f\sqrt\rho$ 保距到 $L^2$；極限取 $F/\sqrt\rho$ |
| 多重指標 | $D^\alpha=\partial^{|\alpha|}/\partial x_1^{\alpha_1}\cdots\partial x_N^{\alpha_N}$ | $\alpha_k\ge0$ 一次涵蓋所有偏導 |
| Sobolev | $\tilde H^m$：$C^m$ 且 $D^\alpha f\in L^2$，$\langle f,g\rangle=\int\sum_{|\alpha|\le m}D^\alpha f\overline{D^\alpha g}$ | 不完備；完備化 $H^m=W^{m,2}$ |
| 強收斂 | $\|x_n-x\|\to0$ | |
| 弱收斂 | $\langle x_n,y\rangle\to\langle x,y\rangle$ ∀$y$ | |
| 強 ⟹ 弱 | Thm 3.3.11 | $|\langle x_n-x,y\rangle|\le\|x_n-x\|\|y\|$ |
| 內積連續 | $x_n\to x$, $y_n\to y$ ⟹ $\langle x_n,y_n\rangle\to\langle x,y\rangle$ | 加 0；收斂數列有界 |
| 範數連續 | $x_n\to x$ ⟹ $\|x_n\|\to\|x\|$ | 取 $y_n=x_n$ |
| 弱 + 範數 ⟹ 強 | Thm 3.3.13 | $\|x_n-x\|^2=\|x_n\|^2-2\operatorname{Re}\langle x_n,x\rangle+\|x\|^2$ |
| 稠密集檢查 | 有界 + 在 $S$ 上（$\overline{\operatorname{span}S}=E$）⟹ 弱收斂 | $\varepsilon/3$ |
| 弱收斂有界 | Thm 3.3.15 | $f_n=\langle\cdot,x_n\rangle$，Banach–Steinhaus，$\|f_n\|=\|x_n\|$ |
| 弱不推強 | $e_n\xrightarrow{w}0$，$\|e_n\|=1$ | §3.4 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 加權內積 | 第 20 集：Hermite、Laguerre 多項式是加權 $L^2$ 中的正交系統；第 30 集 Sturm–Liouville |
| 弱收斂的反例 $e_n$ | 第 20–21 集：正規正交數列 |
| $f_n=\langle\cdot,x_n\rangle$ 是有界泛函 | 第 24 集：Riesz 表示定理（每個有界泛函都長這樣） |
| Sobolev 空間 | 課本 §6.3、§6.5：橢圓邊界值問題的弱解（第 1 集講者提過） |

---

## 附：本集一句話總結

> **加權 $L^2$ 用 $f\sqrt\rho$ 就變回普通 $L^2$，所以完備；Sobolev 空間把導數也放進內積，完備化後是 PDE 的主場；強收斂（範數）推得出弱收斂（每個內積都收斂），反過來不行，但弱收斂加上範數收斂就是強收斂，而且靠 Banach–Steinhaus，弱收斂數列一定有界。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-01 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 9:12）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.3 整理。*
