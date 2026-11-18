---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 5
lecture: Lecture 5
date: 2023-01-25
video: https://youtu.be/0lfD2Hh21ec （part 1）、https://youtu.be/qsglycNTZm8 （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3 Theorem 1.3.33–1.3.34、§1.4 Definition 1.4.1–Example 1.4.6（書頁 18–21，PDF 頁 37–40）
---

# 第 5 集 · Riesz 引理：無限維的單位球不緊緻 [▶ 影片](https://youtu.be/0lfD2Hh21ec)

← 上一集：[04-closed-and-compact](04-closed-and-compact.md) ｜ [總目錄](README.md) ｜ 下一集：[06-banach-spaces-completion](06-banach-spaces-completion.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 5 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 33:26 ＋ part 2 31:52，自動字幕）＋ Debnath & Mikusiński §1.3–1.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Riesz 引理](#1-riesz-引理)
  - [1.1 敘述與圖像](#11-敘述與圖像)
  - [1.2 證明](#12-證明)
- [2. 定理：有限維 ⟺ 閉單位球緊緻](#2-定理有限維--閉單位球緊緻)
  - [2.1 有限維 ⟹ 緊緻](#21-有限維--緊緻)
  - [2.2 無限維 ⟹ 不緊緻](#22-無限維--不緊緻)
- [3. Cauchy 數列](#3-cauchy-數列)
- [4. Cauchy 但不收斂的例子：多項式空間](#4-cauchy-但不收斂的例子多項式空間)
- [5. Banach 空間](#5-banach-空間)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Riesz 引理 | Theorem 1.3.33，p. 18 |
| 有限維 ⟺ 閉單位球緊緻 | Theorem 1.3.34，pp. 18–19 |
| Cauchy 數列與等價條件 | Definition 1.4.1、Theorem 1.4.2，pp. 19–20 |
| Cauchy 但不收斂：多項式空間 | Example 1.4.3，p. 20 |
| Cauchy 數列的範數收斂 | Lemma 1.4.4，p. 20 |
| Banach 空間定義；ℓ² 開頭 | Definition 1.4.5、Example 1.4.6，p. 20 |

上一集最後看到：$C([0,1])$ 的閉單位球閉且有界，卻不緊緻（$x_n(t)=t^n$）。這一集證明這不是巧合：**無限維空間的閉單位球一定不緊緻**。

講者事後說他在 Riesz 引理上花了太多時間，而且覺得沒講清楚。[▶ part 2 31:10](https://youtu.be/qsglycNTZm8?t=1870) 下面把證明的每一步補齊。

---

## 1. Riesz 引理

### 1.1 敘述與圖像

[▶ 00:44](https://youtu.be/0lfD2Hh21ec?t=44) 課本 Theorem 1.3.33。⚠️ 逐字稿缺字：字幕把 Riesz 聽成「Reese's」。

**Riesz 引理（Riesz's lemma）**：$X$ 是賦範空間 $E$ 的**閉的真子空間**（closed proper subspace）。對每個 $\varepsilon\in(0,1)$，存在 $x_\varepsilon\in E$ 使得

$$\|x_\varepsilon\|=1\quad\text{而且}\quad\|x_\varepsilon-x\|\ge\varepsilon\ \ \text{對所有 } x\in X.$$

- **真子空間**：$X\ne E$。
- 白話：可以在**單位球面上**找到一點，它離整個子空間 $X$ 都至少 $\varepsilon$ 遠。

**圖像**【課堂討論】[▶ 02:31](https://youtu.be/0lfD2Hh21ec?t=151)：講者一開始畫錯，把 $X$ 想成整個空間。修正後：$X$ 是穿過原點的子空間（例如 $\mathbb{R}^2$ 裡的一條直線），$x_\varepsilon$ 在單位圓上，**不在** $X$ 上；從 $X$ 上任一點 $x$ 到 $x_\varepsilon$ 的位移向量 $x_\varepsilon-x$，長度都至少 $\varepsilon$。

> 以下**不是逐字稿內容**，是依圖像推論的：在 $\mathbb{R}^2$ 歐氏範數下，取 $x_\varepsilon$ 垂直於直線 $X$，距離就是 1，連 $\varepsilon=1$ 都做得到。一般的賦範空間沒有「垂直」，所以只能保證任意 $\varepsilon<1$。第 3 章的 Hilbert 空間有正交，那時又能做到 1。

### 1.2 證明

[▶ 07:19](https://youtu.be/0lfD2Hh21ec?t=439)

**Step 1：選一個不在 $X$ 裡的點，量它到 $X$ 的距離。**

因為 $X$ 是真子空間，可以取 $z\in E\setminus X$。令

$$d=\inf_{x\in X}\|z-x\|.$$

**為什麼 $d>0$**（講者和學生討論後的結論）：如果 $d=0$，就有 $x_n\in X$ 使 $\|z-x_n\|\to0$，即 $x_n\to z$。$X$ 是閉集，由上一集的定理（閉 ⟺ 序列閉），$z\in X$，矛盾。

> 「真子空間」用在這裡：保證 $z$ 存在。講者在 part 2 想過「證明哪裡用到真子空間」。[▶ part 2 05:05](https://youtu.be/qsglycNTZm8?t=305)

**Step 2：找一個「幾乎最近」的點 $x_0$。**[▶ 10:10](https://youtu.be/0lfD2Hh21ec?t=610)

存在 $x_0\in X$ 使

$$d\le\|z-x_0\|\le\frac d\varepsilon.$$

課堂上大家卡在右邊的不等式。理由如下：

- 左邊：$d$ 是所有 $\|z-x\|$ 的下確界，所以每個都 $\ge d$。
- 右邊：$\varepsilon\in(0,1)$，所以 $\frac d\varepsilon>d$（這裡用到 $d>0$）。$d$ 是**最大**下界，所以比 $d$ 大的數 $\frac d\varepsilon$ **不是**下界——一定有某個 $x_0\in X$ 使 $\|z-x_0\|<\frac d\varepsilon$。

講者用例子說明：$\varepsilon=\frac12$ 時，只要選一個跟 $z$ 距離在 $2d$ 以內的 $x_0$。[▶ 13:48](https://youtu.be/0lfD2Hh21ec?t=828)

**Step 3：正規化。**[▶ 15:00](https://youtu.be/0lfD2Hh21ec?t=900)

$$x_\varepsilon=\frac{z-x_0}{\|z-x_0\|}.$$

$z\ne x_0$（$z\notin X$），所以分母不是 0，而且 $\|x_\varepsilon\|=1$。

**Step 4：驗證距離。**[▶ 16:08](https://youtu.be/0lfD2Hh21ec?t=968) 對任意 $x\in X$：

$$\|x_\varepsilon-x\|=\left\|\frac{z-x_0}{\|z-x_0\|}-x\right\|=\frac{1}{\|z-x_0\|}\Big\|z-\big(x_0+\|z-x_0\|\,x\big)\Big\|.$$

【課堂討論】[▶ 17:57](https://youtu.be/0lfD2Hh21ec?t=1077) 學生指出關鍵：$x_0+\|z-x_0\|\,x$ **在 $X$ 裡**，因為 $x_0,x\in X$，而 $X$ 是子空間（子空間檢驗法：元素加上元素的純量倍還在裡面）。叫它 $x_1$，則 $\|z-x_1\|\ge d$（$d$ 的定義）。所以

$$\|x_\varepsilon-x\|\ge\frac{d}{\|z-x_0\|}\ge\frac{d}{d/\varepsilon}=\varepsilon.$$

第二個不等式用了 Step 2 的 $\|z-x_0\|\le\frac d\varepsilon$。∎

講者一開始以為這步是三角不等式，後來發現不是，只是「把範數提出來」再用 $d$ 的定義。[▶ 18:36](https://youtu.be/0lfD2Hh21ec?t=1116)

**關鍵一步**：幾乎最近的點 $x_0$ 只「差一點」最近，誤差比例由 $\varepsilon$ 控制；正規化後，任何 $x$ 的平移都還在 $X$ 裡，所以距離至少 $d$。

---

## 2. 定理：有限維 ⟺ 閉單位球緊緻

[▶ 21:39](https://youtu.be/0lfD2Hh21ec?t=1299) 課本 Theorem 1.3.34。講者說 Riesz 引理是這個定理的「關鍵樞紐」。

**定理**：賦範空間 $E$ 是有限維 ⟺ $E$ 的閉單位球 $\overline B(0,1)$ 是緊緻的。

（緊緻在這本書的意思是**序列緊緻**：每個數列都有收斂子數列，極限也在集合裡。見上一集。）

### 2.1 有限維 ⟹ 緊緻

[▶ 23:17](https://youtu.be/0lfD2Hh21ec?t=1397)

$\dim E=n$，基底 $e_1,\dots,e_n$。由第 3 集，所有範數等價，所以可以假設範數是

$$\|\alpha_1e_1+\cdots+\alpha_ne_n\|_0=|\alpha_1|+\cdots+|\alpha_n|.$$

（等價的範數有一樣的收斂，所以緊緻與否不變。）課本說：「證明這個範數的單位球緊緻是簡單的練習」。

【課堂討論】[▶ 24:58](https://youtu.be/0lfD2Hh21ec?t=1498) 講者問有沒有其他緊緻的判準。學生想到 **Bolzano–Weierstrass 定理**：實數中每個有界數列都有收斂子數列。

課堂上的嘗試：取單位球中的數列 $(x_n)$，令 $a_n=\|x_n\|$，這是有界實數列，用 Bolzano–Weierstrass 取收斂子數列 $a_{n_k}\to a_0$。課堂就停在「範數收斂」。講者在 part 2 開頭說：「可能只是我累了，但我好像漏了什麼。」[▶ part 2 00:10](https://youtu.be/qsglycNTZm8?t=10)

> 以下**不是逐字稿內容**，是依課本的提示補上的完整證明。課堂的論證有缺口：**範數收斂不代表向量收斂**（例如 $\mathbb{R}^2$ 中 $(1,0),(0,1),(1,0),(0,1),\dots$ 範數都是 1，但不收斂）。要對**每個座標**用 Bolzano–Weierstrass。
>
> 1. 設 $x_k=\alpha_{k,1}e_1+\cdots+\alpha_{k,n}e_n$，$\|x_k\|_0\le1$。則每個座標 $|\alpha_{k,i}|\le1$，都是有界數列。
> 2. 對第 1 個座標用 Bolzano–Weierstrass，取子數列使 $\alpha_{k,1}$ 收斂；在這個子數列裡再對第 2 個座標取子數列；……做 $n$ 次（有限次，這裡用到有限維）。得到一個子數列 $(x_{k_j})$，使每個座標 $\alpha_{k_j,i}\to\alpha_i$。
> 3. 令 $x=\alpha_1e_1+\cdots+\alpha_ne_n$。則 $\|x_{k_j}-x\|_0=\sum_{i=1}^n|\alpha_{k_j,i}-\alpha_i|\to0$。
> 4. 極限在單位球裡：$\|x\|_0=\sum|\alpha_i|=\lim_j\sum_i|\alpha_{k_j,i}|\le1$。∎

### 2.2 無限維 ⟹ 不緊緻

[▶ part 2 00:44](https://youtu.be/qsglycNTZm8?t=44) 這方向課本有完整證明。

**想法**：用 Riesz 引理（取 $\varepsilon=\frac12$）造一個數列，項都在單位球面上，彼此距離都 $\ge\frac12$。這種數列不可能有收斂子數列。

**Step 1**：任取 $x_1$ 使 $\|x_1\|=1$。

**Step 2**：$\operatorname{span}\{x_1\}$ 是閉的真子空間。由 Riesz 引理（$\varepsilon=\frac12$），有 $x_2$ 使 $\|x_2\|=1$、$\|x_2-x_1\|\ge\frac12$。[▶ part 2 03:23](https://youtu.be/qsglycNTZm8?t=203)

【課堂討論】[▶ part 2 05:05](https://youtu.be/qsglycNTZm8?t=305) 為什麼是**真**子空間？學生答：如果 $\operatorname{span}\{x_1\}=E$，那 $E$ 就是一維的，跟「無限維」矛盾。講者：「好問題……也許這正是有限維起作用的地方。」

**Step 3（歸納）**：已造出 $x_1,\dots,x_n$。$\operatorname{span}\{x_1,\dots,x_n\}$ 是閉的真子空間（$E$ 無限維，$n$ 個向量 span 不出全空間）。由 Riesz 引理，有 $x_{n+1}$ 使

$$\|x_{n+1}\|=1,\qquad\|x_k-x_{n+1}\|\ge\tfrac12\ \ (k=1,\dots,n).$$

所以整個數列滿足：$\|x_n\|=1$，而且 $m\ne n$ 時 $\|x_m-x_n\|\ge\frac12$。

> 以下**不是逐字稿內容**，是補上課本沒說明的一點：為什麼有限維子空間 $\operatorname{span}\{x_1,\dots,x_n\}$ 是**閉的**？因為有限維賦範空間是完備的（第 6 集會講完備；理由是在 $\|\cdot\|_0$ 下 Cauchy 數列的每個座標都是 Cauchy 實數列），而完備的子空間一定是閉的（極限唯一，又一定在子空間裡）。

**Step 4：沒有收斂子數列。**[▶ part 2 07:26](https://youtu.be/qsglycNTZm8?t=446) 假設子數列 $x_{p_n}\to x$。則

$$\frac12\le\|x_{p_n}-x_{p_{n+1}}\|\le\|x_{p_n}-x\|+\|x_{p_{n+1}}-x\|.$$

右邊兩項都應該 $\to0$，但總和永遠 $\ge\frac12$，矛盾。所以閉單位球不緊緻。∎

講者的總結【口頭】[▶ part 2 11:02](https://youtu.be/qsglycNTZm8?t=662)：這個構造每一步都用到「還有真子空間」。在有限維裡做，總有一步會用完真子空間，構造就斷了——所以有限維單位球緊緻，無限維不可能緊緻。上一集 $C([0,1])$ 的例子也是同一回事：$1,t,t^2,t^3,\dots$ 有點像這裡的 $x_1,x_2,\dots$。講者說他也還在弄懂這些關聯。

---

## 3. Cauchy 數列

[▶ part 2 13:54](https://youtu.be/qsglycNTZm8?t=834) 課本 §1.4。

講者說他對 Banach 空間比剛才的內容熟悉得多；上次碰到 Riesz 引理這類東西是研究所的泛函分析課。【口頭】

**定義 1.4.1（Cauchy 數列）**：賦範空間中的數列 $(x_n)$ 叫 **Cauchy 數列**，如果對每個 $\varepsilon>0$，存在 $M$，使得

$$\|x_m-x_n\|<\varepsilon\quad\text{對所有 } m,n>M.$$

白話：數列尾巴裡的項彼此越來越近。

**定理 1.4.2（等價條件）**[▶ part 2 16:15](https://youtu.be/qsglycNTZm8?t=975)：下面三條等價。

- (a) $(x_n)$ 是 Cauchy 數列；
- (b) 對任意兩個遞增正整數數列 $(p_n)$、$(q_n)$，$\|x_{p_n}-x_{q_n}\|\to0$；
- (c) 對任意遞增正整數數列 $(p_n)$，$\|x_{p_{n+1}}-x_{p_n}\|\to0$。

課本把證明留作習題。

**收斂 ⟹ Cauchy**，兩種證法：

- **課本（用 (b)）**[▶ part 2 18:30](https://youtu.be/qsglycNTZm8?t=1110)：$x_n\to x$，則
  $$\|x_{p_n}-x_{q_n}\|\le\|x_{p_n}-x\|+\|x_{q_n}-x\|\to0,$$
  因為收斂數列的子數列收斂到同一個極限。由 (b)，是 Cauchy。
- **講者（直接 $\varepsilon/2$）**【口頭】[▶ part 2 20:18](https://youtu.be/qsglycNTZm8?t=1218)：$\|x_m-x_n\|\le\|x_m-x\|+\|x-x_n\|$，取讓兩項都 $<\varepsilon/2$ 的指標的最大值，就 $<\varepsilon$。講者說課本這裡「有點在炫技」，展示 (b) 好用。

**反過來不一定成立**——下一節的例子。

---

## 4. Cauchy 但不收斂的例子：多項式空間

[▶ part 2 21:31](https://youtu.be/qsglycNTZm8?t=1291) 課本 Example 1.4.3。這是學生課前問的例子。

$P([0,1])$：$[0,1]$ 上的多項式，範數用一致收斂範數 $\|P\|=\max_{[0,1]}|P(x)|$。令

$$P_n(x)=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}.$$

$(P_n)$ 是 Cauchy 數列，但在 $P([0,1])$ 裡**不收斂**：它的「極限」是 $e^x$，不是多項式。

**Cauchy 的計算**[▶ part 2 22:44](https://youtu.be/qsglycNTZm8?t=1364)：設 $m>n$，

$$P_m(x)-P_n(x)=\frac{x^{n+1}}{(n+1)!}+\cdots+\frac{x^m}{m!}.$$

講者說：對任意 $\varepsilon$ 能找到 $M$ 讓它夠小，「看起來合理，但直接算很麻煩」；他猜可以把它看成 $e^x$ 部分和的**尾巴**，借用部分和收斂的結果。他沒做完。

以下**不是逐字稿內容**，是照講者的想法補完：

- 每一項在 $[0,1]$ 上都是非負遞增的，所以最大值在 $x=1$：
  $$\|P_m-P_n\|=\sum_{k=n+1}^m\frac1{k!}\le\sum_{k=n+1}^\infty\frac1{k!}.$$
- 右邊是收斂級數 $\sum\frac1{k!}=e$ 的尾巴，$n\to\infty$ 時趨近 0。所以 Cauchy。
- **為什麼不收斂到任何多項式**：由泰勒定理，$P_n\to e^x$ 在 $[0,1]$ 上一致收斂。如果 $P_n\to Q$（某個多項式）也在一致範數下，那在 $C([0,1])$ 裡極限唯一，$Q=e^x$。但 $e^x$ 不是多項式（多項式微分夠多次會變成 0，$e^x$ 不會）。矛盾。

講者的說明【口頭】[▶ part 2 26:00](https://youtu.be/qsglycNTZm8?t=1560)：放到更大的空間 $C([0,1])$ 裡，這個數列**就收斂**了，因為 $e^x$ 是 $[0,1]$ 上的連續函數。它在 $C([0,1])$ 裡，但不在 $P([0,1])$ 裡。所以多項式空間「缺了東西」。

**Lemma 1.4.4**[▶ part 2 26:37](https://youtu.be/qsglycNTZm8?t=1597)：若 $(x_n)$ 是 Cauchy 數列，則範數數列 $(\|x_n\|)$ 收斂。講者只說「這很重要，之後會用到」，沒寫證明。

【課本補充】證明：由反向三角不等式，
$$\big|\|x_m\|-\|x_n\|\big|\le\|x_m-x_n\|\to0,$$
所以 $(\|x_n\|)$ 是實數的 Cauchy 數列，而實數完備，所以收斂。推論：**Cauchy 數列有界**。

---

## 5. Banach 空間

[▶ part 2 26:37](https://youtu.be/qsglycNTZm8?t=1597) 課本 Definition 1.4.5。⚠️ 逐字稿缺字：字幕把 Banach 聽成「binoc / Avenox」，Cauchy 聽成「koshy」。

**定義**：賦範空間 $E$ 叫**完備（complete）**，如果 $E$ 中每個 Cauchy 數列都收斂到 $E$ 中的元素。完備的賦範空間叫 **Banach 空間**。

所以 $P([0,1])$（一致範數）**不是** Banach 空間。

### ℓ² 的記號（Example 1.4.6 的開頭）

[▶ part 2 27:56](https://youtu.be/qsglycNTZm8?t=1676)

課本要證 $\ell^2$ 完備。學生問：為什麼有**兩個下標**？講者解釋：

- $\ell^2$ 的一個「點」本身就是一個數列。
- 所以 $\ell^2$ 中的數列是「**數列的數列**」：
  $$a_1=(\alpha_{1,1},\alpha_{1,2},\alpha_{1,3},\dots),\quad a_2=(\alpha_{2,1},\alpha_{2,2},\alpha_{2,3},\dots),\ \dots$$
- 第一個下標 $n$ 是「第幾個點」，第二個下標 $k$ 是「這個點的第幾個座標」。

Cauchy 條件寫成：給 $\varepsilon>0$，存在 $n_0$，使 $m,n\ge n_0$ 時

$$\sum_{k=1}^\infty|\alpha_{m,k}-\alpha_{n,k}|^2<\varepsilon^2. \tag{1.10}$$

寫 $\varepsilon^2$ 是因為左邊是 2-範數的**平方**。完整證明下一集講。

---

## 6. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| Riesz 引理 | $X$ 閉真子空間，$\varepsilon\in(0,1)$ ⟹ 有單位向量 $x_\varepsilon$，$\|x_\varepsilon-x\|\ge\varepsilon$ ∀$x\in X$ | $z\notin X$，$d=\operatorname{dist}(z,X)>0$；取 $\|z-x_0\|\le d/\varepsilon$；$x_\varepsilon=\frac{z-x_0}{\|z-x_0\|}$；$x_0+\|z-x_0\|x\in X$ |
| $d>0$ | $X$ 閉 | $d=0$ ⟹ $X$ 中數列收斂到 $z$ ⟹ $z\in X$ |
| 有限維 ⟹ 球緊緻 | 用 $\|\cdot\|_0$ | 每個座標用 Bolzano–Weierstrass，共 $n$ 次 |
| 無限維 ⟹ 球不緊緻 | 數列 $\|x_n\|=1$、$\|x_m-x_n\|\ge\frac12$ | 反覆對 $\operatorname{span}\{x_1..x_n\}$ 用 Riesz；永遠是真子空間 |
| Cauchy | $\|x_m-x_n\|<\varepsilon$，$m,n>M$ | |
| 收斂 ⟹ Cauchy | | $\|x_m-x_n\|\le\|x_m-x\|+\|x-x_n\|$ |
| Cauchy ⟹ 範數收斂 | Lemma 1.4.4 | $\big|\|x_m\|-\|x_n\|\big|\le\|x_m-x_n\|$；Cauchy 數列有界 |
| Cauchy 不收斂 | $P([0,1])$ 中 $\sum_{k\le n}x^k/k!$ | $\|P_m-P_n\|=\sum_{n<k\le m}1/k!$；極限 $e^x$ 不是多項式 |
| Banach 空間 | 完備的賦範空間 | |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Banach 空間、ℓ² 完備 | 第 6 集（ℓ² 與 $C([a,b])$ 完備、完備化） |
| 「多項式空間不完備，放進更大的空間就完備」 | 第 6 集：完備化（completion） |
| Riesz 引理的「最近點」 | 第 23 集：Hilbert 空間的正交投影，最近點真的存在而且唯一 |
| 無限維的緊緻性失敗 | 第 27–29 集：緊緻算子 |

---

## 附：本集一句話總結

> **Riesz 引理說：閉的真子空間外面，單位球面上總有離它很遠的點。在無限維空間反覆使用它，就造出一串彼此距離都 ≥ ½ 的單位向量，所以閉單位球不可能緊緻——「閉且有界 ⟹ 緊緻」正好刻畫了有限維。接著進入 Banach 空間：每個 Cauchy 數列都收斂的賦範空間；多項式空間就不是。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-01-25 錄影逐字稿（YouTube 自動字幕，part 1 33:26 ＋ part 2 31:52）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3–1.4 整理。*
