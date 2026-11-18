---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 8
lecture: Lecture 8
date: 2023-02-01
video: https://youtu.be/XPeIgxjNzrQ （part 1）、https://youtu.be/1DTI0UNb0Rg （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.5 Theorem 1.5.10–1.5.13、§1.6（書頁 29–34，PDF 頁 48–53）；講者另用 C. H. Edwards Jr.《Advanced Calculus of Several Variables》約 p. 162 的 Newton 法
---

# 第 8 集 · 有界線性映射的延拓、壓縮映射定理、Newton 法 [▶ 影片](https://youtu.be/XPeIgxjNzrQ)

← 上一集：[07-linear-maps-continuity](07-linear-maps-continuity.md) ｜ [總目錄](README.md) ｜ 下一集：[09-existence-theorem-odes](09-existence-theorem-odes.md) →

> **課程**：Hilbert Spaces（2023 春）— 第 8 集。**這集是講者自己在家錄的影片**，沒有學生在場。
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 21:23 ＋ part 2 37:00，自動字幕）＋ Debnath & Mikusiński §1.5–1.6 ＋ 講者展示的 Edwards 筆記
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 稠密子空間上的有界線性映射可以唯一延拓](#1-稠密子空間上的有界線性映射可以唯一延拓)
- [2. 零空間與圖形是閉的](#2-零空間與圖形是閉的)
- [3. 一致有界原理（Banach–Steinhaus）](#3-一致有界原理banachsteinhaus)
- [4. 壓縮映射](#4-壓縮映射)
- [5. 例子：x³ − x − 1 = 0](#5-例子x³--x--1--0)
- [6. Banach 不動點定理](#6-banach-不動點定理)
- [7. 應用：修正的 Newton 法](#7-應用修正的-newton-法)
- [8. 應用：反函數定理的構想](#8-應用反函數定理的構想)
- [9. 預告：微分方程的存在唯一性](#9-預告微分方程的存在唯一性)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者在影片裡說「§1.4 和 §1.5」，對照課本實際是 §1.5 和 §1.6。[▶ 00:31](https://youtu.be/XPeIgxjNzrQ?t=31)

| 主題 | 課本 |
|---|---|
| 連續線性映射延拓到閉包 | Theorem 1.5.10，p. 29 |
| 零空間、圖形是閉的 | Theorem 1.5.11，p. 29 |
| Banach–Steinhaus（只敘述） | Theorem 1.5.12–1.5.13，pp. 30–31 |
| 壓縮映射 | Definition 1.6.2，p. 32 |
| $x^3-x-1=0$ 的例子 | Example 1.6.3、1.6.5，pp. 32–34 |
| Banach 不動點定理 | Theorem 1.6.4，p. 33 |
| 修正 Newton 法、反函數定理 | 課本無；Edwards |

---

## 1. 稠密子空間上的有界線性映射可以唯一延拓

[▶ 02:17](https://youtu.be/XPeIgxjNzrQ?t=137) 課本 Theorem 1.5.10。

**定理**：$L$ 是從賦範空間 $E_1$ 的子空間 $D(L)$ 到 Banach 空間 $E_2$ 的連續線性映射。則 $L$ 可以**唯一地**延拓成閉包 $\operatorname{cl}D(L)$ 上的連續線性映射。特別地，若 $D(L)$ 在 $E_1$ 中稠密，$L$ 可以唯一延拓到整個 $E_1$。

**證明**：

**Step 1：候選值。**[▶ 07:58](https://youtu.be/XPeIgxjNzrQ?t=478) 取 $x\in\operatorname{cl}D(L)$。由閉包的序列刻畫，有 $x_n\in D(L)$，$x_n\to x$。收斂數列是 Cauchy，所以

$$\|Lx_m-Lx_n\|=\|L(x_m-x_n)\|\le\|L\|\,\|x_m-x_n\|\to0.$$

（又是上一集的 $\|Lx\|\le\|L\|\|x\|$。）$(Lx_n)$ 是 $E_2$ 中的 Cauchy 數列，$E_2$ 完備，所以 $Lx_n\to z\in E_2$。定義

$$\tilde Lx=z=\lim_{n\to\infty}Lx_n.$$

講者提醒：要延拓的定義域是 $D(L)$，不是 $E_1$，他一度寫錯。[▶ 11:48](https://youtu.be/XPeIgxjNzrQ?t=708)

**Step 2：不依賴數列的選擇（well-defined）。**[▶ 14:35](https://youtu.be/XPeIgxjNzrQ?t=875) 若另一個 $y_n\in D(L)$ 也 $\to x$：

$$Ly_n=L(y_n-x_n)+Lx_n.$$

$y_n-x_n\to x-x=0$，$L$ 連續，所以 $L(y_n-x_n)\to L(0)=0$；而 $Lx_n\to z$。所以 $Ly_n\to z$。講者說：「這幾乎跟上一堂做的某件事一模一樣。」

**Step 3：是延拓，而且線性。**[▶ 16:46](https://youtu.be/XPeIgxjNzrQ?t=1006) 若 $x\in D(L)$，取常數數列 $x_n=x$，得 $\tilde Lx=Lx$，所以 $\tilde L$ 在 $D(L)$ 上就是 $L$。課本說 $\tilde L$「顯然」線性；講者認為這次「顯然」是正當的：閉包裡每一點都是 $D(L)$ 中數列的極限，$L$ 線性，極限也線性，所以 $\tilde L$ 線性。

**Step 4：連續（有界）。**[▶ 18:28](https://youtu.be/XPeIgxjNzrQ?t=1108) 取 $x\in\operatorname{cl}D(L)$，$\|x\|=1$，$x_n\in D(L)$，$x_n\to x$。範數連續，所以 $\|x_n\|\to\|x\|=1$。

$$\|\tilde Lx\|=\left\|\lim_nLx_n\right\|=\lim_n\|Lx_n\|\le\lim_n\|L\|\,\|x_n\|=\|L\|.$$

第二個等號用**範數連續**把極限拉出來。所以 $\tilde L$ 有界，因此連續，而且 $\|\tilde L\|=\|L\|$。∎

> 以下**不是逐字稿內容**，是補上的唯一性理由：若 $\hat L$ 是另一個連續延拓，則 $\hat Lx=\hat L(\lim x_n)=\lim\hat Lx_n=\lim Lx_n=\tilde Lx$（用 $\hat L$ 連續）。

---

## 2. 零空間與圖形是閉的

[▶ 02:50](https://youtu.be/XPeIgxjNzrQ?t=170) 課本 Theorem 1.5.11（證明是習題，講者只敘述）。

**定理**：$L:E_1\to E_2$ 連續線性，則零空間 $\mathcal N(L)$ 是閉子空間。若定義域 $D(L)$ 是閉的，則圖形 $\mathcal G(L)$ 是 $E_1\times E_2$ 的閉子空間。

> 以下**不是逐字稿內容**，是習題的簡短證法：
> - $\mathcal N(L)=L^{-1}(\{0\})$，$\{0\}$ 是閉集，連續映射下閉集的原像是閉的（上一集 Theorem 1.5.4）。
> - 圖形：設 $(x_n,Lx_n)\to(x,y)$。則 $x_n\to x$（$x\in D(L)$，因為定義域閉），由連續 $Lx_n\to Lx$；極限唯一，$y=Lx$。所以 $(x,y)\in\mathcal G(L)$。

---

## 3. 一致有界原理（Banach–Steinhaus）

[▶ 03:27](https://youtu.be/XPeIgxjNzrQ?t=207) 課本 Theorem 1.5.13。

**定理**：$\mathcal T$ 是一族從 **Banach 空間** $X$ 到賦範空間 $Y$ 的有界線性映射。若對每個 $x\in X$，存在常數 $M_x$ 使

$$\|Tx\|\le M_x\quad\text{對所有 } T\in\mathcal T,$$

則存在常數 $M>0$ 使 $\|T\|\le M$ 對所有 $T\in\mathcal T$。

白話：**逐點有界 ⟹ 一致有界**（算子範數一起有界）。也叫**一致有界原理（uniform boundedness principle）**。

講者說明為什麼不講證明【口頭】[▶ 04:33](https://youtu.be/XPeIgxjNzrQ?t=273)：

- 標準證法用 **Baire 綱定理**（Baire category theorem）。
- 課本改用 Jan Mikusiński（1970）的**對角定理**（Theorem 1.5.12，關於無窮矩陣 $(x_{ij})$），說它「簡單、不需新概念」。講者說：「美在觀者眼裡……任何從無窮矩陣開始的定理，也許簡單，但我不打算教。」他覺得這個結果比證明有趣。
- 他本來想用 Baire 綱定理證，但發現課本把它出成作業（用度量空間敘述），就留給學生。
- 他說自己研究裡也許該用這個原理。

---

## 4. 壓縮映射

[▶ part 2 00:02](https://youtu.be/1DTI0UNb0Rg?t=2) 課本 Definition 1.6.2。

**不動點（fixed point）**：$f(z)=z$ 的點 $z$。

**壓縮映射（contraction mapping）**：從賦範空間 $E$ 的子集 $A$ 到 $E$ 的映射 $f$，如果存在 $0<\alpha<1$ 使

$$\|f(x)-f(y)\|\le\alpha\|x-y\|\quad\text{對所有 } x,y\in A. \tag{1.16}$$

講者的意見【口頭】：他認為 $f$ 應該是從 $A$ 映到 $A$，課本這裡寫得不清楚；後面的不動點定理也確實要求 $F\to F$。

**壓縮映射是連續的**（$\varepsilon$-$\delta$ 證法）[▶ part 2 01:10](https://youtu.be/1DTI0UNb0Rg?t=70)：給 $\varepsilon>0$，取 $\delta=\varepsilon/\alpha$。若 $\|x-x_0\|<\delta$，則

$$\|f(x)-f(x_0)\|\le\alpha\|x-x_0\|<\alpha\cdot\frac\varepsilon\alpha=\varepsilon.$$

---

## 5. 例子：x³ − x − 1 = 0

[▶ part 2 02:19](https://youtu.be/1DTI0UNb0Rg?t=139) 課本 Example 1.6.3、1.6.5。

**把方程改寫成不動點問題** $Tx=x$，有好幾種寫法：

$$Tx=(1+x)^{1/3},\qquad Tx=x^3-1,\qquad Tx=\frac{1}{x^2-1}.$$

不動點就是方程的解。課本只用第一種。

**$[1,2]$ 裡有根**：令 $g(x)=x^3-x-1$，$g(1)=-1<0$，$g(2)=5>0$，$g$ 連續，由中間值定理有根。（講者補的論證。）

**$T(x)=(1+x)^{1/3}$ 在 $[1,2]$ 上是壓縮**[▶ part 2 04:37](https://youtu.be/1DTI0UNb0Rg?t=277)：

$$T'(x)=\frac13(1+x)^{-2/3}=\frac{1}{3(1+x)^{2/3}}.$$

分母在 $x=1$ 最小，所以在 $[1,2]$ 上
$$|T'(x)|\le\frac{1}{3\cdot2^{2/3}}=\frac{2^{1/3}}{6}\approx0.21<1.$$

由**均值定理**，對 $x,y\in[1,2]$ 有 $c$ 介於 $x,y$ 之間使 $\frac{Tx-Ty}{x-y}=T'(c)$，所以

$$|Tx-Ty|\le\frac{2^{1/3}}{6}|x-y|.$$

（也要 $T$ 把 $[1,2]$ 映進 $[1,2]$：$T(1)=2^{1/3}\approx1.26$，$T(2)=3^{1/3}\approx1.44$，$T$ 遞增。這點講者沒說。）課本說另外兩種寫法不是壓縮。

**迭代**[▶ part 2 06:27](https://youtu.be/1DTI0UNb0Rg?t=387)（Example 1.6.5，p. 34）：猜 $x_0=1$，反覆 $x_{n+1}=Tx_n$：

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $x_n$ | 1.2599 | 1.3123 | 1.3224 | 1.3243 | 1.3246 | 1.3247 | 1.3247 |

第 6 次迭代就準到小數點後四位：根 $\approx1.3247$。

講者：「用迭代解方程，這很怪，也很美，而且幾乎是我知道的每個存在定理的核心。」【口頭】[▶ part 2 08:43](https://youtu.be/1DTI0UNb0Rg?t=523)

---

## 6. Banach 不動點定理

[▶ part 2 09:18](https://youtu.be/1DTI0UNb0Rg?t=558) 課本 Theorem 1.6.4。

講者說這可能是本學期到目前為止**最重要**的定理，而且簡單到可以放進考試：「你們應該能證這個定理。」【口頭】

**定理（Banach 不動點定理）**：$F$ 是 Banach 空間 $E$ 的**閉**子集，$f:F\to F$ 是壓縮映射。則存在**唯一**的 $z\in F$ 使 $f(z)=z$。

**證明**：

**Step 1：迭代。** 任取 $x_0\in F$，令 $x_n=f(x_{n-1})$。（因為 $f$ 映進 $F$，整個數列都在 $F$ 裡。）

**Step 2：相鄰項的距離幾何遞減。**[▶ part 2 11:06](https://youtu.be/1DTI0UNb0Rg?t=666)

$$\|x_{n+1}-x_n\|=\|f(x_n)-f(x_{n-1})\|\le\alpha\|x_n-x_{n-1}\|\le\alpha^2\|x_{n-1}-x_{n-2}\|\le\cdots\le\alpha^n\|x_1-x_0\|. \tag{☆}$$

講者說要嚴格可以用歸納法，「大家都會做」。

**Step 3：Cauchy。**[▶ part 2 12:45](https://youtu.be/1DTI0UNb0Rg?t=765) 設 $m<n$。中間插入所有項，用三角不等式，再用 (☆)：

$$\begin{aligned}\|x_n-x_m\|&\le\|x_n-x_{n-1}\|+\|x_{n-1}-x_{n-2}\|+\cdots+\|x_{m+1}-x_m\|\\&\le\left(\alpha^{n-1}+\alpha^{n-2}+\cdots+\alpha^m\right)\|x_1-x_0\|\\&=\alpha^m\left(1+\alpha+\cdots+\alpha^{n-1-m}\right)\|x_1-x_0\|\\&<\alpha^m\sum_{k=0}^\infty\alpha^k\,\|x_1-x_0\|=\frac{\alpha^m}{1-\alpha}\|x_1-x_0\|.\end{aligned}$$

講者：「在一切有趣事物的核心，幾何級數出現了。」$0<\alpha<1$，所以右邊 $\to0$（$m\to\infty$）。$(x_n)$ 是 Cauchy 數列。

**Step 4：極限存在。**[▶ part 2 15:01](https://youtu.be/1DTI0UNb0Rg?t=901) $E$ 完備，$x_n\to z\in E$；$F$ 閉，所以 $z\in F$。

**Step 5：$z$ 是不動點。**

$$\|f(z)-z\|\le\|f(z)-x_n\|+\|x_n-z\|=\|f(z)-f(x_{n-1})\|+\|x_n-z\|\le\alpha\|z-x_{n-1}\|+\|x_n-z\|\to0.$$

所以 $\|f(z)-z\|=0$，$f(z)=z$。

**Step 6：唯一。**[▶ part 2 16:10](https://youtu.be/1DTI0UNb0Rg?t=970) 若 $f(w)=w$，則

$$\|z-w\|=\|f(z)-f(w)\|\le\alpha\|z-w\|.$$

$\alpha<1$，只有 $\|z-w\|=0$ 才可能。講者舉例：$\alpha=\frac12$ 時，$\|z-w\|\le\frac12\|z-w\|$ 只有在 $\|z-w\|=0$ 時成立。所以 $z=w$。∎

**講者的評語**【口頭】[▶ part 2 16:44](https://youtu.be/1DTI0UNb0Rg?t=1004)：很多定理充滿反證法，這個**完全沒有**，全是建構的，而且直接告訴你**怎麼迭代出解**。

**誤差估計**【口頭】[▶ part 2 22:50](https://youtu.be/1DTI0UNb0Rg?t=1370)：Edwards 的版本多了一條估計：第 $n$ 次迭代離不動點多遠，
$$\|x_n-z\|\le\frac{\alpha^n}{1-\alpha}\|x_1-x_0\|.$$
講者說「我想我們可以把它加到我們的定理上」。

> 以下**不是逐字稿內容**，是確認講者的猜測：在 Step 3 的 $\|x_n-x_m\|\le\frac{\alpha^m}{1-\alpha}\|x_1-x_0\|$ 中固定 $m$、令 $n\to\infty$（範數連續），得 $\|z-x_m\|\le\frac{\alpha^m}{1-\alpha}\|x_1-x_0\|$。就是這條估計。不用知道 $z$ 是多少，就能知道離它多遠。

【課本補充】$\alpha<1$ 不能放寬（p. 34）：

- 換成 $\alpha\le1$，定理不成立。
- 甚至換成嚴格不等式 $\|Tx-Ty\|<\|x-y\|$ 也不行。Example 1.6.6：$f(x)=x+e^{-x}$，$\mathbb{R}_+\to\mathbb{R}_+$。$f'(\xi)=1-e^{-\xi}\in[0,1)$，由均值定理 $|f(x)-f(y)|<|x-y|$；但沒有 $\alpha<1$ 對所有點都有效（$\xi\to\infty$ 時 $f'\to1$），而且 $f(x)=x$ 要求 $e^{-x}=0$，**沒有不動點**。

---

## 7. 應用：修正的 Newton 法

【口頭】[▶ part 2 17:50](https://youtu.be/1DTI0UNb0Rg?t=1070) 講者展示自己根據 C. H. Edwards Jr.《Advanced Calculus of Several Variables》（約 p. 162）寫的筆記，會分享給學生。他說是在這本書裡第一次真正體會壓縮映射有多重要。

### 7.1 天真的 Newton 法

[▶ part 2 18:57](https://youtu.be/1DTI0UNb0Rg?t=1137)

要解 $f(x)=0$，猜 $x_0$。不對的話，用**線性化**代替 $f$：

$$f(x)\approx f(x_0)+f'(x_0)(x-x_0).$$

令它等於 0 解出 $x_1=x_0-\dfrac{f(x_0)}{f'(x_0)}$。反覆做：

$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.$$

這很像壓縮映射的迭代。講者說：歷史上是反過來的，先有 Newton 法這類方法，Banach 等人才從中提煉出定理。

Edwards 叫這個「天真的」Newton 法：麻煩，而且一般不保證收斂。講者畫圖：可能從一點跳到另一點，切線斜率一樣，又跳回原點，永遠在兩點之間繞，到不了中間的零點。[▶ part 2 20:40](https://youtu.be/1DTI0UNb0Rg?t=1240)

### 7.2 修正版：固定斜率

[▶ part 2 21:13](https://youtu.be/1DTI0UNb0Rg?t=1273)

改成永遠用最大斜率 $M$ 往下走：

$$x_{n+1}=x_n-\frac{f(x_n)}{M}.$$

**定理（Edwards）**：$f:[a,b]\to\mathbb{R}$ 可微，$f(a)<0<f(b)$，且
$$0<m\le f'(x)\le M\quad\text{對所有 } x\in[a,b].$$
則對任何 $x_0\in[a,b]$，上面的迭代收斂到 $f(x)=0$ 在 $[a,b]$ 中的唯一根 $x^*$，而且

$$|x_n-x^*|\le\frac{|f(x_0)|}{m}\left(1-\frac mM\right)^n.$$

**為什麼根唯一**：$f'>0$，$f$ 嚴格遞增，沒有轉折點；中間值定理保證穿過 0，而且只穿一次。

**證明：$\varphi(x)=x-\dfrac{f(x)}{M}$ 是 $[a,b]$ 上的壓縮。**[▶ part 2 26:17](https://youtu.be/1DTI0UNb0Rg?t=1577)

1. $\varphi'(x)=1-\dfrac{f'(x)}{M}$。由 $m\le f'\le M$：
   $$0\le\varphi'(x)\le1-\frac mM=:k<1.$$
2. **映進 $[a,b]$**：$\varphi'\ge0$，$\varphi$ 不遞減。所以
   $$a<a-\frac{f(a)}{M}=\varphi(a)\le\varphi(x)\le\varphi(b)=b-\frac{f(b)}{M}<b.$$
   （用了 $f(a)<0$、$f(b)>0$。）講者強調：壓縮映射定理需要映進閉區間本身，這步就是在證這個。
3. **壓縮**：由均值定理（講者用的是 Carathéodory 定理，一種用差商函數刻畫可微的方法，說「用均值定理也行」），$|\varphi(x)-\varphi(y)|\le k|x-y|$。[▶ part 2 27:23](https://youtu.be/1DTI0UNb0Rg?t=1643)
4. **不動點就是根**：$x^*=\varphi(x^*)=x^*-\dfrac{f(x^*)}{M}$ ⟹ $f(x^*)=0$。
5. **誤差**：代入第 6 節的估計，$|x_1-x_0|=\dfrac{|f(x_0)|}{M}$，$1-k=\dfrac mM$：
   $$|x_n-x^*|\le\frac{k^n}{1-k}\cdot\frac{|f(x_0)|}{M}=\frac{|f(x_0)|}{m}\left(1-\frac mM\right)^n.$$
   （這行代數是補的，講者只說「代進去就得到」。）

講者：這是 Newton 法的改良，不只告訴你怎麼迭代，**每一步都知道離真解多遠**。[▶ part 2 29:01](https://youtu.be/1DTI0UNb0Rg?t=1741)

Edwards 的壓縮映射定理是 $[a,b]\to[a,b]$、範數是絕對值的版本，證明跟第 6 節「逐字一樣」，只是 $z,w$ 換成 $x^*,x^{**}$。

---

## 8. 應用：反函數定理的構想

【口頭】[▶ part 2 29:36](https://youtu.be/1DTI0UNb0Rg?t=1776)

稍微改一下，就能證**反函數定理**。

**問題**：$f(a)=b$，$y$ 接近 $b$。能不能找到 $x$ 使 $f(x)=y$？

**想法**：解 $f(x)-y=0$ 的線性化，固定用 $a$ 點的導數：

$$x_{n+1}=x_n-\frac{f(x_n)-y}{f'(a)},\qquad x_0=a.$$

**敘述（講者的版本）**：$f$ 連續可微，$f(a)=b$，$f'(a)\ne0$。則存在 $a$ 的鄰域 $U$ 和 $b$ 的鄰域 $V$，使得對每個 $y^*\in V$，上面的迭代在 $U$ 中收斂到某個 $x^*$，且 $f(x^*)=y^*$。

定義 $g(y)=$ 這個 $x$，則 $f,g$ 互為反函數。講者說：第一次看到時覺得「這根本是黑魔法」。反函數被定義成一串迭代的極限，於是可以從迭代證明反函數的性質（例如可微）。細節「現在不重要」，都在 Edwards 書裡。[▶ part 2 31:19](https://youtu.be/1DTI0UNb0Rg?t=1879)

---

## 9. 預告：微分方程的存在唯一性

[▶ part 2 32:27](https://youtu.be/1DTI0UNb0Rg?t=1947)

下次（週五）要用不動點定理證微分方程的存在唯一性定理。講者展示 Nagle、Saff、Snider《微分方程》（他手上大概是第 5 版）第 13 章，會寄 PDF 給學生：

- 定義一個**積分算子**，它的不動點正好是微分方程的解。
- 反覆套這個算子叫 **Picard 迭代**。
- 這個算子是壓縮 ⟹ 解存在且唯一。
- 第 13 章也有方程組的 Picard 定理、解的延拓。

講者：「我知道你們在微分方程課沒證過，因為沒有正常人會在那門課證存在唯一性定理。」【口頭】

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 延拓（Thm 1.5.10） | 連續線性 $L:D(L)\to$ Banach，唯一延拓到 $\operatorname{cl}D(L)$，$\|\tilde L\|=\|L\|$ | $\|Lx_m-Lx_n\|\le\|L\|\|x_m-x_n\|$ ⟹ $Lx_n$ Cauchy；換數列差 $L(y_n-x_n)\to0$ |
| 零空間閉 | $\mathcal N(L)=L^{-1}(\{0\})$ | 閉集原像閉 |
| Banach–Steinhaus | Banach 空間上，逐點有界 ⟹ $\sup\|T\|<\infty$ | 標準證法：Baire 綱定理 |
| 壓縮 | $\|f(x)-f(y)\|\le\alpha\|x-y\|$，$\alpha<1$ | 壓縮 ⟹ 連續（$\delta=\varepsilon/\alpha$） |
| Banach 不動點 | 閉集 $F$、$f:F\to F$ 壓縮 ⟹ 唯一不動點 | $\|x_{n+1}-x_n\|\le\alpha^n\|x_1-x_0\|$；幾何級數 ⟹ Cauchy |
| 誤差估計 | $\|x_m-z\|\le\frac{\alpha^m}{1-\alpha}\|x_1-x_0\|$ | Cauchy 估計中令 $n\to\infty$ |
| $\alpha<1$ 必要 | $x+e^{-x}$ 滿足嚴格 $<$ 但無不動點 | |
| 例 | $x^3-x-1=0$，$T=(1+x)^{1/3}$，$\alpha=2^{1/3}/6$ | 均值定理 |
| 修正 Newton | $x_{n+1}=x_n-f(x_n)/M$，$0<m\le f'\le M$ | $\varphi'=1-f'/M\in[0,1-m/M]$；誤差 $\frac{|f(x_0)|}{m}(1-\frac mM)^n$ |
| 反函數定理 | $x_{n+1}=x_n-\frac{f(x_n)-y}{f'(a)}$ | 反函數 = 迭代的極限 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Banach 不動點定理、Picard 迭代 | 第 9 集：微分方程存在唯一性；課本第 5 章（§5.2、§5.4 逐次逼近法） |
| 反函數定理 | 第 9 集（講者會再提一下） |
| 稠密子空間上延拓 | 第 31–32 集：Fourier 變換先在好函數上定義，再延拓到 $L^2$ |
| 一致有界原理 | 課本第 4 章（算子理論） |

---

## 附：本集一句話總結

> **壓縮映射把任意起點一步步拉近，相鄰距離像幾何級數遞減，所以迭代是 Cauchy 數列，在完備空間裡收斂到唯一的不動點——這個完全建構式的證明，同時給出解的算法和誤差估計，是 Newton 法、反函數定理和微分方程存在定理的共同核心。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-01 錄影逐字稿（YouTube 自動字幕，part 1 21:23 ＋ part 2 37:00）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.5–1.6 整理；Newton 法部分依講者展示的 Edwards 筆記之口述。*
