---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 9
lecture: Lecture 9
date: 2023-02-03
video: https://youtu.be/c-v8Q5pX0d4 （part 1）、https://youtu.be/AgLMm3gk9a0 （part 2）
notes: 講者照 Nagle、Saff、Snider《微分方程》第 13 章講；對應課本 Debnath & Mikusiński 3rd ed. §5.2 Theorem 5.2.1、5.2.5（書頁 218–222，PDF 頁 237–241）
---

# 第 9 集 · 微分方程的存在唯一性定理、反函數定理一瞥 [▶ 影片](https://youtu.be/c-v8Q5pX0d4)

← 上一集：[08-bounded-maps-contraction](08-bounded-maps-contraction.md) ｜ [總目錄](README.md) ｜ 下一集：[10-matrix-exponential](10-matrix-exponential.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 9 集。這堂只有一位學生在場，另一位去練習、事後看錄影。
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 4:50，自動字幕）＋ 講者發給學生的 Nagle–Saff–Snider 第 13 章（只依口述）＋ Debnath & Mikusiński §5.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 把初值問題改寫成積分方程](#1-把初值問題改寫成積分方程)
- [2. Picard 算子與 Picard 迭代](#2-picard-算子與-picard-迭代)
- [3. 例子：y′ = 2y](#3-例子y--2y)
- [4. 存在唯一性定理](#4-存在唯一性定理)
- [5. 證明](#5-證明)
- [6. 課本的版本（Lipschitz 條件）](#6-課本的版本lipschitz-條件)
- [7. 預告：矩陣分析與多變數反函數定理](#7-預告矩陣分析與多變數反函數定理)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集（錄影）證了 Banach 不動點定理。學生說證明「相對容易」，講者說今天要讓他更相信這個定理有多好用。[▶ 00:37](https://youtu.be/c-v8Q5pX0d4?t=37)

| 主題 | 來源 |
|---|---|
| 初值問題 ⟺ 積分方程 ⟺ Picard 算子的不動點 | Nagle–Saff–Snider 第 13 章；課本 §5.2 |
| Picard 迭代的例子 | Nagle–Saff–Snider |
| 存在唯一性定理與證明 | Nagle–Saff–Snider；課本 Theorem 5.2.5 |
| 多變數反函數定理的構想 | 口頭 |

---

## 1. 把初值問題改寫成積分方程

[▶ 01:10](https://youtu.be/c-v8Q5pX0d4?t=70)

**初值問題（initial value problem, IVP）**：

$$\frac{dy}{dx}=f(x,y(x)),\qquad y(x_0)=y_0.$$

兩邊從 $x_0$ 積到 $x$（積分變數改叫 $t$，因為 $x$ 已經當上限用了）：

$$y(x)=y_0+\int_{x_0}^xf(t,y(t))\,dt. \tag{★}$$

這叫**積分方程（integral equation）**：未知函數出現在積分號裡。

- (★) 的解和 IVP 的解是同一批：(★) 兩邊微分（微積分基本定理）就回到微分方程。
- 而且**初值已經內建**：代 $x=x_0$，積分變成 0，得 $y(x_0)=y_0$。講者說：從這點看，積分方程比微分方程好一點。[▶ 02:47](https://youtu.be/c-v8Q5pX0d4?t=167)

---

## 2. Picard 算子與 Picard 迭代

[▶ 03:21](https://youtu.be/c-v8Q5pX0d4?t=201)

定義一個作用在函數上的**算子**：

$$(Tg)(x)=y_0+\int_{x_0}^xf(t,g(t))\,dt.$$

（講者先用 $y$ 當輸入函數，後來改用 $g$ 比較不會混淆。）

**(★) 的解就是 $T$ 的不動點**：$Tg=g$。

**這就是整個招數**【口頭】[▶ 05:40](https://youtu.be/c-v8Q5pX0d4?t=340)：把問題改寫成某個算子的不動點問題；如果能找到一個環境讓這個算子是壓縮，就用 Banach 不動點定理得到解的存在（而且唯一）。

不動點定理的證明裡，解是迭代 $y_{n+1}=T(y_n)$ 的極限。在這裡這個函數數列叫 **Picard 迭代**。

---

## 3. 例子：y′ = 2y

[▶ 07:12](https://youtu.be/c-v8Q5pX0d4?t=432) 講者發的 Nagle–Saff–Snider 講義裡的例子。

$$\frac{dy}{dx}=2y,\qquad y(0)=1.\qquad (Ty)(x)=1+\int_0^x2y(t)\,dt.$$

從常數函數 $y_0(x)=1$ 開始：

$$\begin{aligned}y_1(x)&=1+\int_0^x2\,dt=1+2x,\\ y_2(x)&=1+\int_0^x2(1+2t)\,dt=1+2x+2x^2,\\ y_3(x)&=1+\int_0^x2(1+2t+2t^2)\,dt=1+2x+2x^2+\tfrac43x^3.\end{aligned}$$

講者提醒：每次都要記得積分裡那個 2，他自己常忘。（$y_3$ 的係數字幕聽不清，這裡是重算的。）

**跟真解比較**[▶ 10:21](https://youtu.be/c-v8Q5pX0d4?t=621)：學生修過微分方程，特徵根 $r=2$，解是 $y=e^{2x}$。它的 Maclaurin 展開

$$e^{2x}=1+2x+\frac{(2x)^2}{2!}+\frac{(2x)^3}{3!}+\cdots=1+2x+2x^2+\tfrac43x^3+\cdots$$

**Picard 迭代就是一項一項生出 $e^{2x}$ 的泰勒級數。**

**歷史**【口頭】[▶ 11:34](https://youtu.be/c-v8Q5pX0d4?t=694)：講義的註腳說，這個方法可追溯到 Liouville（1838，研究二階線性方程），後來 Caqué（1864）、Fuchs（1870）、Peano（1888）也用過，但因為 Picard 在 1890、1896 年關於逐次逼近的工作，名字跟了 Picard。Banach 不動點定理是 1922 年。講者說：Banach 出來時已經很多人在做這件事，他把它一般化、漂亮地寫成任意賦範空間的定理。⚠️ 逐字稿缺字：字幕把 Liouville 聽成「levo」、Caqué 聽成「J Kaku」，依人名推斷修正。

講者也提到：講義附錄裡的不動點定理是對實變函數寫的，不談「壓縮」，而是直接假設導數有界——就像上一集 Newton 法用導數有界推出壓縮。

---

## 4. 存在唯一性定理

[▶ 13:46](https://youtu.be/c-v8Q5pX0d4?t=826)

**定理**（講者照 Nagle–Saff–Snider 的版本）：設 $f$ 和 $\dfrac{\partial f}{\partial y}$ 在一個包含 $(x_0,y_0)$ 的開矩形 $R$ 上連續。則初值問題

$$\frac{dy}{dx}=f(x,y),\qquad y(x_0)=y_0$$

在某個區間 $(x_0-h,x_0+h)$（$h>0$）上有**唯一**解。而且這個解是 Picard 迭代的一致極限。

講者說：這就是微分方程課一開頭會「敘述」的那個定理。「沒有正常人會在微分方程課證它」。

---

## 5. 證明

### Step 1：放一個閉矩形，取界

[▶ 16:54](https://youtu.be/c-v8Q5pX0d4?t=1014)

在開矩形 $R$ 裡放一個包住 $(x_0,y_0)$ 的**閉**矩形：

$$R_1=\{(x,y):|x-x_0|\le h_1,\ |y-y_0|\le\alpha_1\}\subseteq R.$$

（$R$ 是開的，所以 $h_1,\alpha_1$ 存在。）$R_1$ 閉且有界，$f$ 和 $\partial f/\partial y$ 連續，由極值定理有常數 $M,L$ 使

$$|f(x,y)|\le M,\qquad\left|\frac{\partial f}{\partial y}(x,y)\right|\le L\qquad\text{在 } R_1 \text{ 上}.$$

### Step 2：選 $h$

[▶ 31:59](https://youtu.be/c-v8Q5pX0d4?t=1919)

$$h<\min\left\{h_1,\ \frac{\alpha_1}{M}\right\}\quad\text{而且}\quad h<\frac1L.$$

**為什麼要 $h<\alpha_1/M$（講者畫的「扇形」圖）**[▶ 32:33](https://youtu.be/c-v8Q5pX0d4?t=1953)：

- 從 $(x_0,y_0)$ 畫兩條線 $y=y_0\pm M(x-x_0)$，像一把扇子。
- 因為 $|f|\le M$，$Tg$ 的斜率最多 $M$，所以 $Tg$ 的圖形被夾在扇子裡。
- 扇子的線往上走 $\alpha_1$（碰到 $R_1$ 的上邊）時，往右走了多少？斜率 = $\frac{\Delta y}{\Delta x}$，$M=\frac{\alpha_1}{\Delta x}$，所以 $\Delta x=\frac{\alpha_1}{M}$。
- 所以只要 $|x-x_0|<\frac{\alpha_1}{M}$，$Tg$ 就不會跑出 $R_1$ 的上下邊。$h<h_1$ 則確保不跑出左右邊。

$h<1/L$ 的理由在 Step 5 才看得到。

### Step 3：函數的集合 $S$

[▶ 41:32](https://youtu.be/c-v8Q5pX0d4?t=2492)

令 $I=[x_0-h,x_0+h]$，

$$S=\{g\in C(I):\ \|g-y_0\|\le\alpha_1\},\qquad\|g-y_0\|=\max_{x\in I}|g(x)-y_0|.$$

範數就是我們用的一致範數（第 2 集），$y_0$ 當常數函數。講者：「終於，這就是讓 Picard 算子成為壓縮的函數集合。」

> 以下**不是逐字稿內容**，是補上不動點定理需要的條件：$S$ 是 $C(I)$ 中以 $y_0$ 為中心的閉球，所以是閉集；$C(I)$ 是 Banach 空間（第 6 集）。所以 $S$ 是 Banach 空間的閉子集，符合 Banach 不動點定理的條件。

講義裡的不動點定理版本（講者寫在黑板上）[▶ 22:11](https://youtu.be/c-v8Q5pX0d4?t=1331)：$S$ 如上，$G:S\to S$ 滿足 $\|G(w)-G(z)\|\le K\|w-z\|$（$0\le K<1$）對所有 $w,z\in S$。則 $G$ 有唯一不動點，而且從 $S$ 中任何 $y_0$ 出發的迭代都收斂到它。

### Step 4：$T$ 把 $S$ 映進 $S$

[▶ 27:01](https://youtu.be/c-v8Q5pX0d4?t=1621)

取 $g\in S$。對 $t\in I$：$|t-x_0|\le h<h_1$ 且 $|g(t)-y_0|\le\alpha_1$，所以 $(t,g(t))\in R_1$，$f(t,g(t))$ 有定義且 $|f(t,g(t))|\le M$。

- **$Tg$ 連續**：連續函數合成連續；變上限積分連續函數得到連續函數。講者說「積分通常讓東西更光滑」，這部分的理論課上還沒發展。[▶ 28:14](https://youtu.be/c-v8Q5pX0d4?t=1694)
- **$Tg$ 不跑出去**：設 $x>x_0$（另一邊同理），[▶ 30:04](https://youtu.be/c-v8Q5pX0d4?t=1804)
  $$|(Tg)(x)-y_0|=\left|\int_{x_0}^xf(t,g(t))\,dt\right|\le\int_{x_0}^x|f(t,g(t))|\,dt\le M|x-x_0|\le Mh<\alpha_1.$$
  第一個不等式是「積分的絕對值 ≤ 絕對值的積分」。取最大值得 $\|Tg-y_0\|\le\alpha_1$，所以 $Tg\in S$。

### Step 5：$T$ 是壓縮

[▶ 46:05](https://youtu.be/c-v8Q5pX0d4?t=2765)

取 $u,v\in S$：

$$|(Tu)(x)-(Tv)(x)|=\left|\int_{x_0}^x\Big[f(t,u(t))-f(t,v(t))\Big]dt\right|.$$

**對 $y$ 用均值定理**：固定 $t$，把 $f(t,\cdot)$ 看成 $y$ 的函數，有 $z(t)$ 介於 $u(t)$ 和 $v(t)$ 之間使

$$f(t,u(t))-f(t,v(t))=\frac{\partial f}{\partial y}(t,z(t))\,\big(u(t)-v(t)\big).$$

講者說這步很狡猾：其實是**對每個 $t$ 各用一次**均值定理，用了無限多次。[▶ 48:30](https://youtu.be/c-v8Q5pX0d4?t=2910)（$z(t)$ 介於兩個 $S$ 中函數的值之間，所以 $(t,z(t))\in R_1$，偏導數 $\le L$。）

$$\begin{aligned}|(Tu)(x)-(Tv)(x)|&\le L\left|\int_{x_0}^x|u(t)-v(t)|\,dt\right|\le L\,\|u-v\|\,|x-x_0|\\&\le Lh\,\|u-v\|.\end{aligned}$$

取最大值：$\|Tu-Tv\|\le K\|u-v\|$，其中 $K=Lh<1$——**這就是為什麼要 $h<1/L$**。

### Step 6：結論

由 Banach 不動點定理，$T$ 在 $S$ 中有唯一不動點，也就是 IVP 在 $I$ 上有一個解，而且它是 Picard 迭代的一致極限（$C(I)$ 的範數收斂 = 一致收斂）。

### 一個細節：「在 $S$ 中唯一」還不夠

[▶ 52:38](https://youtu.be/c-v8Q5pX0d4?t=3158)

講義說：上面只證了 IVP 在 $S$ **裡面**有唯一解，還沒證區間上的**每一個**解都落在 $S$ 裡。講者說：解的唯一性和不動點問題的唯一性「是稍微不同的事」，細節請看講義那一段（他說 p. 845，又說 A45）。⚠️ 待確認：講義頁碼。

> 以下**不是逐字稿內容**，是依證明推論的補洞：設 $\varphi$ 是 $I$ 內的任一解。若 $\varphi$ 離開 $S$，取第一個使 $|\varphi(x_1)-y_0|=\alpha_1$ 的點 $x_1$（設 $x_1>x_0$）。在 $[x_0,x_1]$ 上圖形在 $R_1$ 內，所以 $|\varphi'|=|f|\le M$，得 $\alpha_1=|\varphi(x_1)-y_0|\le M(x_1-x_0)\le Mh<\alpha_1$，矛盾。所以每個解都在 $S$ 裡，就等於那個唯一的不動點。

---

## 6. 課本的版本（Lipschitz 條件）

【課本補充】Theorem 5.2.5（Picard 存在唯一性定理），p. 221。

課本把 Banach 不動點定理改寫成方便應用的形式（Theorem 5.2.1，**壓縮映射定理**）：$S$ 是 Banach 空間的閉子集，$T:S\to S$ 壓縮，則 $Tx=x$ 在 $S$ 中恰有一解，而且 $x=\lim T^nx_0$（任意 $x_0\in S$），叫**逐次逼近法（method of successive approximations）**。

Picard 定理的假設比講義弱：不要求 $\partial f/\partial y$ 連續，只要求 $f$ 連續而且滿足 **Lipschitz 條件**

$$|f(x,y_1)-f(x,y_2)|\le K|y_1-y_2|.$$

證明結構一樣：在區間長度 $\varepsilon$ 夠小（$K\varepsilon<1$ 等）的地方，$T$ 把一個閉球映進自己，而且

$$\|T\varphi_1-T\varphi_2\|\le K\varepsilon\|\varphi_1-\varphi_2\|.$$

> 講義用 $\partial f/\partial y$ 有界 + 均值定理，其實就是**推出** Lipschitz 條件（$K=L$）。

---

## 7. 預告：矩陣分析與多變數反函數定理

【口頭】[▶ 55:08](https://youtu.be/c-v8Q5pX0d4?t=3308)

講者想離開課本一兩天，講**矩陣的分析**：數列的矩陣怎麼收斂等等。他說這在大學課程裡「沒有家」：線性代數課最後不會說「現在來做矩陣上的分析」，能讓學生學會特徵向量就不錯了。順便也想講**賦範空間上的微分**。

**多變數的線性化**：$F:\mathbb{R}^n\to\mathbb{R}^n$，

$$F(a+h)\approx F(a)+J_F(a)\,h,$$

$J_F$ 是 **Jacobian 矩陣**，各行是偏導數 $\frac{\partial F}{\partial x_1},\dots,\frac{\partial F}{\partial x_n}$（每個都是向量）。

**怎麼求反函數**【課堂討論】[▶ 58:32](https://youtu.be/c-v8Q5pX0d4?t=3512) 一變數：$y=e^x+3$，學生答：解出 $x$，$x=\ln(y-3)$。多變數也一樣要解 $\vec y=F(\vec x)$，但通常是 $n$ 條非線性方程，很麻煩。

**線性化再迭代**[▶ part 2 00:05](https://youtu.be/AgLMm3gk9a0?t=5)：已知 $F(x_0)=y_0$，先解線性化 $y\approx y_0+J_F(x_0)(x-x_0)$：

$$x=x_0+J_F(x_0)^{-1}(y-y_0),$$

然後反覆做。所以要求 **Jacobian 可逆**。

**反函數定理（inverse function theorem）**：

- 一變數：斜率不為 0（不在極大、極小點），就能局部反轉。
- 多變數：若 Jacobian 存在、偏導數在 $x_0$ 連續、$J_F(x_0)$ 可逆，則在 $x_0$ 附近有局部反函數，而且可以用壓縮映射的迭代**構造**它。
- 這不是「若且唯若」：有些函數不可微但仍可逆，只是定理用不上。

講者的看法【口頭】[▶ part 2 03:27](https://youtu.be/AgLMm3gk9a0?t=207)：壓縮映射不只告訴你「存在」，還給出理論上的構造程序。實際計算時通常不是好方法，但理論上非常好用：可以證明解具有你要的性質。他猜數值方法的理論充滿這種論證（他沒修過那門課，這些都是教書時自學的）。

---

## 8. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| IVP → 積分方程 | $y(x)=y_0+\int_{x_0}^xf(t,y(t))dt$ | 初值內建 |
| Picard 算子 | $(Tg)(x)=y_0+\int_{x_0}^xf(t,g(t))dt$ | 解 = 不動點 |
| Picard 迭代例 | $y'=2y$，$y(0)=1$ | $y_n$ = $e^{2x}$ 的泰勒部分和 |
| 定理 | $f,\partial_yf$ 在開矩形連續 ⟹ $(x_0-h,x_0+h)$ 上唯一解 | |
| 選 $h$ | $h<\min\{h_1,\alpha_1/M\}$，$h<1/L$ | $M=\max|f|$，$L=\max|\partial_yf|$ |
| $S$ | $\{g\in C(I):\|g-y_0\|\le\alpha_1\}$ | Banach 空間中的閉球 |
| $T:S\to S$ | $|Tg(x)-y_0|\le M|x-x_0|\le Mh<\alpha_1$ | 扇形圖 |
| 壓縮 | $\|Tu-Tv\|\le Lh\|u-v\|$ | 對 $y$ 用均值定理（每個 $t$ 一次） |
| 所有解都在 $S$ | 第一次離開時 $\alpha_1\le Mh<\alpha_1$ | |
| 課本版 | Lipschitz：$|f(x,y_1)-f(x,y_2)|\le K|y_1-y_2|$ | 壓縮映射定理 5.2.1 |
| 反函數迭代 | $x\leftarrow x_0+J_F(x_0)^{-1}(y-y_0)$ | Jacobian 可逆 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 矩陣的分析、線性化 | 第 10 集：矩陣指數、線性微分方程組 |
| 積分方程、逐次逼近 | 課本第 5 章（§5.3–5.5 Fredholm、Volterra 方程） |
| Picard 迭代 = 泰勒級數 | 第 10 集：$x'=Ax$ 的解 $e^{tA}x_0$ |
| 積分讓函數更光滑 | 第 11 集起：Lebesgue 積分 |

---

## 附：本集一句話總結

> **把初值問題寫成積分方程，就變成 Picard 算子的不動點問題；在一個夠小的區間上，用 $|f|\le M$ 保證算子不跑出一個閉球、用 $|\partial_yf|\le L$ 加均值定理保證它是壓縮，Banach 不動點定理就給出唯一解，而且 Picard 迭代一致收斂到它。**

---

## ⚠️ 待確認清單

1. [▶ 52:38](https://youtu.be/c-v8Q5pX0d4?t=3158) 講者引用 Nagle–Saff–Snider 第 13 章「所有解都在 $S$ 中」那一段的頁碼，字幕一次是「845」一次是「A45」；講者也不確定自己用的是第 4 還是第 5 版。

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-03 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 4:50）整理；定理與證明依講者口述的 Nagle–Saff–Snider 第 13 章，並對照 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.2。*
