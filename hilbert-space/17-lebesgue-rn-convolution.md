---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 17
lecture: Lecture 17
date: 2023-02-24
video: https://youtu.be/PLDNKV9UhPY （part 1）、https://youtu.be/R829HWhARDw （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.11 末、§2.12–2.15（書頁 70–84，PDF 頁 89–103）
---

# 第 17 集 · 複值函數、Lᵖ 空間、ℝᴺ 上的積分、摺積 [▶ 影片](https://youtu.be/PLDNKV9UhPY)

← 上一集：[16-riemann-vs-lebesgue](16-riemann-vs-lebesgue.md) ｜ [總目錄](README.md) ｜ 下一集：[18-inner-product-hilbert-spaces](18-inner-product-hilbert-spaces.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 17 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:11 whisper 轉錄，時間點可能差 1–2 秒；part 2 11:06 自動字幕）＋ Debnath & Mikusiński §2.11–2.15
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 可測函數（回顧）](#1-可測函數回顧)
- [2. 複值可積函數](#2-複值可積函數)
- [3. Lᵖ(ℝ) 空間](#3-lᵖℝ-空間)
- [4. L^∞ 與本質上確界](#4-l-與本質上確界)
- [5. ℝᴺ 上的 Lebesgue 積分](#5-ℝᴺ-上的-lebesgue-積分)
- [6. Fubini 定理](#6-fubini-定理)
- [7. 摺積](#7-摺積)
- [8. 摺積從哪裡來：Laplace 變換](#8-摺積從哪裡來laplace-變換)
- [9. 作業與考試](#9-作業與考試)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說今天是「綜覽模式」，挑最有趣的部分講，把第 2 章收尾。下週進 Hilbert 空間。

| 主題 | 課本 |
|---|---|
| 可測函數 | Definition 2.11.5–Theorem 2.11.7，pp. 70–71 |
| 複值可積函數 | §2.12，pp. 71–74 |
| $L^p(\mathbb{R})$、Hölder、Minkowski、完備性、$L^\infty$ | §2.13，pp. 74–77 |
| $\mathbb{R}^N$ 上的積分、Fubini | §2.14，pp. 78–82 |
| 摺積 | §2.15，pp. 82–84 |

---

## 1. 可測函數（回顧）

[▶ 00:00](https://youtu.be/PLDNKV9UhPY?t=0) 課本 Definition 2.11.5–Theorem 2.11.7。

- **可測集**：特徵函數局部可積；測度用特徵函數的積分定義。
- **可測函數（measurable function）**：存在階梯函數列 $f_n\to f$ a.e.。
- **Theorem 2.11.6**：可測函數構成向量空間；可測函數的絕對值、乘積都可測。
- **Theorem 2.11.7**：$f$ 可測、$|f|\le g$，$g$ 局部可積 ⟹ $f$ 局部可積。講者說這有點像複分析的 Weierstrass M 檢驗。

---

## 2. 複值可積函數

[▶ 01:28](https://youtu.be/PLDNKV9UhPY?t=88) 課本 §2.12。

考慮 $f:\mathbb{R}\to\mathbb{C}$。

- **複值階梯函數**：$f=\lambda_1\chi_{[a_1,b_1)}+\lambda_2\chi_{[a_2,b_2)}+\cdots$，【課堂討論】差別只在 $\lambda_k$ 是複數。積分照舊定義。
- **可積**：條件 (a)(b) 跟實值的一模一樣。講者：「全是照抄。」
- **Theorem 2.12.2**：$f$ 可積 ⟺ $\operatorname{Re}f$ 和 $\operatorname{Im}f$ 都可積，而且
  $$\int f=\int\operatorname{Re}f+i\int\operatorname{Im}f. \tag{2.27}$$

講者問學生實部、虛部的公式【口頭】[▶ 04:18](https://youtu.be/PLDNKV9UhPY?t=258)：

$$\operatorname{Re}f=\frac{f+\bar f}{2},\qquad\operatorname{Im}f=\frac{f-\bar f}{2i}.$$

**證明的核心**[▶ 05:15](https://youtu.be/PLDNKV9UhPY?t=315)：這節所有證明都歸結到 $|\operatorname{Re}z|\le|z|$、$|\operatorname{Im}z|\le|z|$：對複數組合有估計，就對實部、虛部有估計；反過來也能操作。

- **局部可積**：實部、虛部都局部可積。
- **Theorem 2.12.3、2.12.5**：複值可積（或局部可積）函數的絕對值 $|f|=\sqrt{(\operatorname{Re}f)^2+(\operatorname{Im}f)^2}$ 可積（局部可積），而且 $\left|\int f\right|\le\int|f|$。講者說這條在這裡比在實值時有趣。[▶ 06:34](https://youtu.be/PLDNKV9UhPY?t=394)

講者說這節「不太有趣」，因為二維性全在**值域**；真正難的在定義域。[▶ 09:53](https://youtu.be/PLDNKV9UhPY?t=593)

---

## 3. Lᵖ(ℝ) 空間

[▶ 07:13](https://youtu.be/PLDNKV9UhPY?t=433) 課本 §2.13。講者說這節他主要在意定義。

**定義**：$p>1$，$L^p(\mathbb{R})$ 是所有**複值、局部可積**、而且 $|f|^p\in L^1(\mathbb{R})$ 的函數。範數

$$\|f\|_p=\left(\int|f|^p\right)^{1/p}. \tag{2.28}$$

（$|f|=\sqrt{f\bar f}$ 是複數的模。）

講者【口頭】[▶ 09:12](https://youtu.be/PLDNKV9UhPY?t=552)：這是第 1 集的 $\ell^p$ 的**連續版**：$\ell^p$ 是對數列求和，這裡把求和換成積分。證明是範數用的也是 Hölder、Minkowski 那一套。

**Theorem 2.13.2（Hölder）**：$1<p,q<\infty$，$\frac1p+\frac1q=1$。若 $f\in L^p$、$g\in L^q$，則 $fg\in L^1$，而且

$$\|fg\|_1\le\|f\|_p\|g\|_q. \tag{2.29}$$

講者猜證明（pp. 74–75）跟第 1 章很像，但沒核對。

> 【課本補充】確實一樣：用第 1 集的 Young 不等式 $ab\le\frac{a^p}p+\frac{b^q}q$，代 $a=|f|/\|f\|_p$、$b=|g|/\|g\|_q$，再積分。

**Theorem 2.13.3（Minkowski）**：$\|f+g\|_p\le\|f\|_p+\|g\|_p$，就是這個範數的三角不等式。

**Theorem 2.13.4**[▶ 12:18](https://youtu.be/PLDNKV9UhPY?t=738)：$L^p(\mathbb{R})$（$1\le p<\infty$）**完備**，是 Banach 空間。講者說證明約一頁。

【課本補充】證明概要：在每個 $[-M,M]$ 上用 Hölder，$\int_{-M}^M|f_m-f_n|\le(2M)^{1/q}\|f_m-f_n\|_p$，所以是 $L^1([-M,M])$ 的 Cauchy 數列；用 Theorem 2.8.2 取幾乎處處收斂的子數列，對 $M=1,2,\dots$ 用**對角線法**取一個在整個 $\mathbb{R}$ 上幾乎處處收斂的子數列；再用 **Fatou 引理**證極限在 $L^p$ 裡且按範數收斂。

（課本也說：嚴格來說範數是定義在「幾乎處處相等的等價類」上，跟 §2.6 一樣。）

**$L^p(\Omega)$**[▶ 13:29](https://youtu.be/PLDNKV9UhPY?t=809)：$\Omega\subseteq\mathbb{R}$ 可測，$L^p(\Omega)$ 是 $\Omega$ 上所有複值可測函數、使 $\int_\Omega|f|^p<\infty$；範數 $\|f\|_p=\left(\int_\Omega|f|^p\right)^{1/p}$。【課堂討論】學生答範數的寫法，講者補充：差別只是在 $\Omega$ 上積分（局部可積那節的概念推廣到可測集）。講者承認：「這章後半我在細節上有點偷工減料……給的少，要求的也少。」

$L^p(\Omega)$ 可以看成 $L^p(\mathbb{R})$ 中在 $\Omega$ 外為 0 的函數構成的子空間：把函數在 $\Omega$ 外補 0，兩個積分一樣。[▶ 15:34](https://youtu.be/PLDNKV9UhPY?t=934)

---

## 4. L^∞ 與本質上確界

[▶ 16:51](https://youtu.be/PLDNKV9UhPY?t=1011) 課本 p. 77。

講者說他好像沒見過這個，「我過著與世隔絕的生活」。

**本質上確界（essential supremum）**：$\operatorname{ess\,sup}f$ = 使 $f\le M$ **幾乎處處**成立的最小 $M$；沒有這種 $M$ 就記作 $\infty$。

**$L^\infty(\mathbb{R})$**：所有 $\operatorname{ess\,sup}|f|<\infty$ 的可測函數，範數

$$\|f\|_\infty=\operatorname{ess\,sup}|f|. \tag{2.32}$$

【課堂討論】[▶ 18:17](https://youtu.be/PLDNKV9UhPY?t=1097) 學生說這像之前的一致範數。講者舉例：一個函數大多是 $\frac12$，但有十個點的值是 2、7、9，那本質上確界是 $\frac12$——它忽略那些孤立的大值（有限集是零集）。

【課本補充】$p=\infty$（$q=1$）時 Hölder、Minkowski 仍成立，所以 $L^\infty$ 是向量空間、(2.32) 是範數；$L^\infty(\mathbb{R})$ 也完備。

---

## 5. ℝᴺ 上的 Lebesgue 積分

[▶ 19:30](https://youtu.be/PLDNKV9UhPY?t=1170) 課本 §2.14。講者說：今天前面都是同一個調子，**這裡才是真正不同的**。

**為什麼複值不算「二維」**【口頭】[▶ 20:04](https://youtu.be/PLDNKV9UhPY?t=1204)：講者相信（沒核對）同樣能寫「向量值函數」的一節：只要值域是有限維、範數讓每個分量 $\le$ 整體範數，跟實部、虛部的做法一樣。複雜的東西都發生在**定義域**。把定義域變成多維才是另一種動物。課本從 1 維直接跳到 $N$ 維——講者說：「這整章是個歸納法，1 維是基本情況。」

**半開區間**（在 $\mathbb{R}^N$ 中）[▶ 22:57](https://youtu.be/PLDNKV9UhPY?t=1377)：

$$I=[a_1,b_1)\times\cdots\times[a_N,b_N), \tag{2.33}$$

即 $x\in I$ ⟺ $a_k\le x_k<b_k$ 對 $k=1,\dots,N$。

**測度**：

$$m(I)=(b_1-a_1)\cdots(b_N-a_N).$$

講者：「他的測度論露出來了。」$N=1$ 是長度，$N=2$ 是面積，$N=3$ 是長方體的體積——測度是長度、面積、體積的推廣。[▶ 25:27](https://youtu.be/PLDNKV9UhPY?t=1527)

**階梯函數**：

$$f=\lambda_1\chi_{I_1}+\cdots+\lambda_n\chi_{I_n},\qquad\int f=\lambda_1m(I_1)+\cdots+\lambda_nm(I_n). \tag{2.34}$$

講者提醒：大寫 $N$ 是固定的**維度**，小寫 $n$ 是階梯的**個數**，跟維度無關。他一開始寫錯了地方，用紅筆改正。[▶ 26:39](https://youtu.be/PLDNKV9UhPY?t=1599)

【課堂討論】講者問 $\int\chi_{I_1}$ 該是什麼：1 維時是 $b_1-a_1$，現在就是 $m(I_1)$，超體積。「測度決定了積分。」[▶ 28:20](https://youtu.be/PLDNKV9UhPY?t=1700)

**Definition 2.14.1**：實或複值函數 $f$ 在 $\mathbb{R}^N$ 上 Lebesgue 可積，條件 (a)(b) **逐字**跟 1 維一樣；$\int f=\sum\int f_n$；空間記作 $L^1(\mathbb{R}^N)$。

**Definition 2.14.2**：$f$ 局部可積，如果對每個有界區間 $I$，$f\chi_I$ 可積。講者說：有界集就是能放進夠大的球裡。[▶ 34:22](https://youtu.be/PLDNKV9UhPY?t=2062)

**可測集、測度、可測函數**：同 1 維。$\int_\Omega f=\int f\chi_\Omega$。

**例子**【口頭】[▶ 37:39](https://youtu.be/PLDNKV9UhPY?t=2259)：$\mathbb{R}^3$ 中的「板」$S=\mathbb{R}^2\times[2,3]$。$\chi_S$ 局部可積（所以 $S$ 可測），但不可積（體積無窮大），所以 $\mu(S)=\infty$。常數函數 1 在 $\mathbb{R}^N$ 上也局部可積——「局部可積不代表什麼」。

**$L^p(\mathbb{R}^N)$、$L^\infty(\mathbb{R}^N)$**：同 1 維。講者以為課本沒說完備，學生指出 (2.35) 那裡就說了：$L^p(\mathbb{R}^N)$ 是 Banach 空間，Hölder 成立。[▶ 44:26](https://youtu.be/PLDNKV9UhPY?t=2666)

講者【口頭】：「pp. 78–79 真的很酷，把整章壓縮成兩頁，看這套理論在 $\mathbb{R}^N$ 上重演一次。」

【課本補充】若 $\Omega$ 測度有限，$p\ge r$ 時 $L^p(\Omega)\subset L^r(\Omega)$。（跟第 2 集 $\ell^p$ 的包含方向相反。）

**題外話**【口頭】[▶ 44:26](https://youtu.be/PLDNKV9UhPY?t=2666)：講者在物理課問一題碰撞速度，學生答 7500 m/s（汽車 20 m/s、公車 10 m/s），他取笑了答案，事後覺得不該當眾取笑——「喜劇是危險的」。

---

## 6. Fubini 定理

[▶ 45:21](https://youtu.be/PLDNKV9UhPY?t=2721) 課本 Theorem 2.14.4。

**白話**：二重積分可以先對 $y$ 再對 $x$，或反過來。

【課本補充】Riemann 積分通常要假設 $f$ 連續（或分段連續）才能交換順序；Lebesgue 積分只要 $f$ 在矩形上**可積**就夠。

**定理（Fubini 定理的特例）**：$(a,b)$、$(c,d)$ 是有界或無界區間，$J=(a,b)\times(c,d)$，$f$ 在 $J$ 上可積。則

$$F(x)=\int_c^df(x,y)\,dy$$

在 $(a,b)$ 上**幾乎處處**有定義，$F$ 在 $(a,b)$ 上可積，而且

$$\int_Jf=\int_a^bF=\int_a^b\int_c^df(x,y)\,dy\,dx. \tag{2.38}$$

（對稱地也等於先對 $x$ 積分。）

講者【口頭】：他好奇 Fubini 真正證的是什麼定理，「一定不是書上這些，應該更一般」。證明兩頁；他猜本質是「Fubini 對階梯函數成立（矩形的面積 = 長 × 寬），再推到一般函數」。[▶ 46:03](https://youtu.be/PLDNKV9UhPY?t=2763)

> 【課本補充】確實如此：$f\simeq\sum\lambda_n\chi_{I_n}$，$I_n=[a_n,b_n)\times[c_n,d_n)$，$\chi_{I_n}(x,y)=\chi_{[a_n,b_n)}(x)\chi_{[c_n,d_n)}(y)$，所以 $\int\chi_{I_n}=\int\chi_{[a_n,b_n)}\cdot\int\chi_{[c_n,d_n)}$。逐項先對 $y$ 積分得 $F\simeq\sum\lambda_n\left(\int\chi_{[c_n,d_n)}\right)\chi_{[a_n,b_n)}$，兩邊積分相等。

---

## 7. 摺積

[▶ 46:50](https://youtu.be/PLDNKV9UhPY?t=2810) 課本 §2.15。講者說這個概念很重要，「不只今天」，之後還會再講。

**Theorem 2.15.1**：若 $f,g\in L^1(\mathbb{R})$，則 $f(x-y)g(y)$ 對幾乎所有 $x$ 是 $y$ 的可積函數。而且**摺積（convolution）**

$$(f*g)(x)=\int f(x-y)\,g(y)\,dy$$

是可積函數，

$$\int|f*g|\le\int|f|\int|g|. \tag{2.43}$$

講者說「對幾乎所有 $x$」讓他好奇那 $y$ 呢，「暫時放下懷疑」。證明靠 **Fubini 定理**，在平面上做積分。[▶ 49:45](https://youtu.be/PLDNKV9UhPY?t=2985)

> 以下**不是逐字稿內容**，是 (2.43) 的一行推導：由 Fubini（先證 $H(x,y)=f(x-y)g(y)$ 在 $\mathbb{R}^2$ 可積），
> $$\int|f*g|\le\iint|f(x-y)||g(y)|\,dy\,dx=\int|g(y)|\left(\int|f(x-y)|dx\right)dy=\int|f|\int|g|,$$
> 中間交換積分順序，內層用平移不變性 $\int|f(x-y)|dx=\int|f|$。

**Theorem 2.15.2**：$f*g=g*f$，**摺積可交換**。講者說這用到他跳過的變數代換定理。

> 以下**不是逐字稿內容**，是變數代換的一步：令 $u=x-y$，$(f*g)(x)=\int f(x-y)g(y)dy=\int f(u)g(x-u)du=(g*f)(x)$。

**Theorem 2.15.3**[▶ 50:21](https://youtu.be/PLDNKV9UhPY?t=3021)：若 $f$ 可積，$g$ 是**有界**的局部可積函數，則 $f*g$ 是**連續**函數。

講者原以為會說可積，結果是連續。課本給了明確的估計：$(f*g)(x+t)-(f*g)(x)$ 被一個 $f$ 的差的積分控制。講者先說「因為 $f$ 連續」，馬上改口：$f$ 不是連續，是**可積**，所以那個積分能控制。

> 以下**不是逐字稿內容**，是補上那個估計：設 $|g|\le M$。
> $$|(f*g)(x+t)-(f*g)(x)|\le\int|f(x+t-y)-f(x-y)||g(y)|dy\le M\int|\tau_{-t}f-f|\to0\quad(t\to0),$$
> 最後一步就是第 13 集 Theorem 2.4.3（平移的連續性）。摺積把「只是可積」的 $f$ 抹成連續函數。

【Q&A】講者問學生聽過摺積嗎，一位說聽過這個詞。[▶ 52:07](https://youtu.be/PLDNKV9UhPY?t=3127)

---

## 8. 摺積從哪裡來：Laplace 變換

【口頭】[▶ part 2 00:04](https://youtu.be/R829HWhARDw?t=4) 講者說他是在微分方程裡看到摺積的。

**Laplace 變換**：

$$\mathcal{L}\{y\}(s)=\int_0^\infty e^{-st}y(t)\,dt.$$

**例 1**[▶ part 2 00:38](https://youtu.be/R829HWhARDw?t=38)：

$$\mathcal{L}\{e^{at}\}=\int_0^\infty e^{-(s-a)t}dt=\left[\frac{-e^{-(s-a)t}}{s-a}\right]_0^\infty=\frac1{s-a}\qquad(s>a).$$

（講者笑說沒寫極限，「別告訴我微積分 II 的學生」。$s>a$ 時上限處是 0。）

**例 2：一次得到 cos 和 sin**[▶ part 2 02:25](https://youtu.be/R829HWhARDw?t=145)：上面的計算對複數也成立，令 $a=i\beta$：

$$\mathcal{L}\{e^{i\beta t}\}=\frac1{s-i\beta}=\frac{s+i\beta}{s^2+\beta^2}.$$

由 Euler 公式和積分的線性，左邊 $=\mathcal{L}\{\cos\beta t\}+i\mathcal{L}\{\sin\beta t\}$。比較實部、虛部：

$$\mathcal{L}\{\cos\beta t\}=\frac{s}{s^2+\beta^2},\qquad\mathcal{L}\{\sin\beta t\}=\frac{\beta}{s^2+\beta^2}.$$

**Laplace 變換解初值問題的流程**[▶ part 2 05:30](https://youtu.be/R829HWhARDw?t=330)：

1. 給一個初值問題（一階、二階、三階都可以）。
2. 取 Laplace 變換 → 得到 $Y(s)=\mathcal{L}\{y\}$ 的**代數方程**。
3. 代數解出 $Y(s)$。通常要做一大堆**部分分式**。
4. 取反 Laplace 變換得到 $y(t)$。

講者說：Laplace 變換的妙處是能把**不連續**的問題（分段定義、滿是階梯函數）當成連續的處理：一個分段問題變換到 $s$ 域變成單一問題，一次解出所有情況。

**摺積的角色**[▶ part 2 07:10](https://youtu.be/R829HWhARDw?t=430)：解出的 $Y(s)$ 常是乘積 $F(s)G(s)$。摺積有漂亮的性質：

$$\mathcal{L}^{-1}\{F(s)G(s)\}=f*g.$$

$s$ 域的**乘積**對應時間域的**摺積**，像一種同態。這對 **Green 函數**理論特別重要：常常其中一個函數刻畫系統，另一個刻畫外力。講者說：這幾乎是他知道的唯一方法來求某些反變換，例如 $\frac{1}{(\text{不可約二次式})^2}$，大概是 $\sin$ 跟自己的摺積之類。代價是要算一個「把一個函數平移後跟另一個函數相乘再積分」的積分，而且上限是變數。

> 以下**不是逐字稿內容**，是補一個記號上的差別：Laplace 變換用的摺積是 $(f*g)(t)=\int_0^tf(t-\tau)g(\tau)d\tau$。如果把 $f,g$ 在 $t<0$ 時定義成 0，這就是課本的 $\int_{-\infty}^\infty f(t-\tau)g(\tau)d\tau$。

**講者的用意**【口頭】[▶ part 2 09:31](https://youtu.be/R829HWhARDw?t=571)：這門課的高等分析其實生於微分方程。Fourier 說可以用 sin、cos 的和造出函數，這是他解波動方程和熱方程的關鍵；這個技巧（今天的 Fourier 分析）引發了一連串研究，才有 Cauchy 數列、完備性這些概念。所以他想不時把學生沒見過的微分方程問題帶進來，讓他們理解這些問題的起源。等講到 Hilbert 空間後再回來。

---

## 9. 作業與考試

[▶ 52:43](https://youtu.be/PLDNKV9UhPY?t=3163)

- 第 2 章到此結束。下週進 Hilbert 空間（「終於來到我們的課名」）。
- 給一週收尾第 2 章作業，再下一週考**第一次考試**。講者會給一份「可能的考題」清單：他的指導教授在高等課程裡都這樣做，他因此學到很多，總是準備好那些證明題。
- **第 2 章建議題目**（p. 85 起），約 10 題就夠，甚至不用那麼多：
  - 第 2 題（只要檢查向量空間的一條公理）
  - 第 4 題 (a)
  - 第 9 題
  - 第 14 題
  - 第 18 題
  - 第 20 題（講者：難，但很有名，值得玩一玩；構造不顯然，對將來的「情境意識」有幫助）
  - 第 31、32 題
  - 其他自選；也許第 44 題（摺積），講者有點猶豫。

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵 |
|---|---|---|
| 可測函數 | 階梯函數列 a.e. 收斂到它 | $|f|\le g$ 局部可積 ⟹ $f$ 局部可積 |
| 複值可積 | ⟺ 實部、虛部可積；$\int f=\int\operatorname{Re}f+i\int\operatorname{Im}f$ | $|\operatorname{Re}z|,|\operatorname{Im}z|\le|z|$ |
| $L^p(\mathbb{R})$ | 局部可積、$|f|^p\in L^1$；$\|f\|_p=(\int|f|^p)^{1/p}$ | $\ell^p$ 的連續版 |
| Hölder | $\|fg\|_1\le\|f\|_p\|g\|_q$ | Young 不等式 |
| 完備 | $L^p$ 是 Banach（$1\le p<\infty$） | 局部 $L^1$ Cauchy + 對角線 + Fatou |
| $L^\infty$ | $\|f\|_\infty=\operatorname{ess\,sup}|f|$ | 忽略零集上的值 |
| $\mathbb{R}^N$ | 區間 = 半開區間的積；$m(I)=\prod(b_k-a_k)$ | 其餘定義逐字照搬 |
| Fubini | $f\in L^1(J)$ ⟹ $\int_J f=\int_a^b\int_c^df\,dy\,dx$ | 對矩形的特徵函數成立再推廣 |
| 摺積 | $(f*g)(x)=\int f(x-y)g(y)dy$ | $\int|f*g|\le\int|f|\int|g|$（Fubini） |
| 可交換 | $f*g=g*f$ | $u=x-y$ |
| 連續 | $f\in L^1$、$g$ 有界 ⟹ $f*g$ 連續 | $\le M\int|\tau_{-t}f-f|\to0$ |
| Laplace | $\mathcal{L}\{e^{at}\}=\frac1{s-a}$；$\mathcal{L}^{-1}\{FG\}=f*g$ | 乘積 ↔ 摺積 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $L^2(\mathbb{R}^N)$、Hölder（$p=q=2$ 是 Cauchy–Schwarz） | 第 18 集：$L^2$ 是 Hilbert 空間 |
| $L^p(\Omega)$ | 第 19 集：加權空間、Sobolev 空間 |
| Fubini | 第 20 集起：正交函數的積分計算 |
| 摺積、Green 函數 | 第 31 集：Green 函數、Fourier 變換（摺積定理） |
| Laplace／Fourier 方法 | 第 29–31 集：邊界值問題、Fourier 變換 |

---

## 附：本集一句話總結

> **複值函數只是把實部虛部各做一次；$L^p$ 是 $\ell^p$ 的連續版，同樣靠 Hölder 與 Minkowski，而且完備；真正新的是把定義域換成 $\mathbb{R}^N$——只要把區間換成長方體、長度換成體積，整章逐字重演，還多了 Fubini 定理；用它證明的摺積把可積函數抹得更光滑，正是 Laplace 變換裡「乘積對應摺積」的那個運算。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-24 錄影逐字稿（part 1 whisper large-v3-turbo 轉錄 59:11；part 2 YouTube 自動字幕 11:06）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.11–2.15 整理。*
