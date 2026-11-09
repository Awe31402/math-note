---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 2
lecture: Lecture 2
date: 待補（第 1 集週一、本集週三）
video: https://youtu.be/FbkNYklySak
notes: 《Principles of Robot Autonomy》§2.2.1–2.2.2（書頁 61–64，PDF 頁 63–66）
---

# 第 2 集 · Lecture 2：最佳化理論（Optimization Theory） [▶ 影片](https://youtu.be/FbkNYklySak)

← 上一集：[01-course-overview](01-course-overview.md) ｜ [總目錄](README.md) ｜ 下一集：[03-calculus-of-variations](03-calculus-of-variations.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 2 集
> **講者**：Marco Pavone（本集沒有自我介紹；依第 1 集和「as discussed on Monday」的接續推斷）
> **來源**：YouTube 錄影逐字稿（1:19:02，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§2.2.1–2.2.2
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 無約束問題的必要條件](#1-無約束問題的必要條件)
  - [1.1 一階條件：梯度 = 0](#11-一階條件梯度--0)
  - [1.2 二階條件：Hessian 半正定](#12-二階條件hessian-半正定)
  - [1.3 NOC 定理，和為什麼要「開集合」](#13-noc-定理和為什麼要開集合)
  - [1.4 充分條件：Hessian 正定](#14-充分條件hessian-正定)
- [2. 凸函數](#2-凸函數)
  - [2.1 凸集合與凸函數的定義](#21-凸集合與凸函數的定義)
  - [2.2 為什麼凸很好](#22-為什麼凸很好)
- [3. 演算法：梯度法](#3-演算法梯度法)
  - [3.1 為什麼往負梯度走，函數會變小](#31-為什麼往負梯度走函數會變小)
  - [3.2 下降方向 d 怎麼選](#32-下降方向-d-怎麼選)
  - [3.3 步長 α 怎麼選](#33-步長-α-怎麼選)
  - [3.4 本集沒細講的部分](#34-本集沒細講的部分)
  - [3.5 梯度法整理：在解什麼／步驟／什麼時候會失敗](#35-梯度法整理在解什麼步驟什麼時候會失敗)
- [4. 等式約束問題](#4-等式約束問題)
  - [4.1 兩種處理約束的想法](#41-兩種處理約束的想法)
  - [4.2 Lagrange 乘數定理](#42-lagrange-乘數定理)
  - [4.3 例子：在圓上最小化 x₁ + x₂](#43-例子在圓上最小化-x₁--x₂)
  - [4.4 幾何意義一：等高線相切](#44-幾何意義一等高線相切)
  - [4.5 幾何意義二：梯度垂直於可行變動](#45-幾何意義二梯度垂直於可行變動)
  - [4.6 正則點條件與證明方向](#46-正則點條件與證明方向)
  - [4.7 Lagrangian 函數](#47-lagrangian-函數)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/FbkNYklySak?t=5) 上一集（週一）最後定義了**非線性最佳化問題**（nonlinear optimization problem）：

$$\min_{x\in\mathbb{R}^n} f(x)$$

決策變數（decision variable）$x$ 是有限維的向量。也定義了：

- **局部最小值**（local minimum）$x^*$：在 $x^*$ 附近一小圈（鄰域）裡，所有點都滿足 $f(x)\ge f(x^*)$。
- **全域最小值**（global minimum）$x^*$：**所有**點都滿足 $f(x)\ge f(x^*)$。

老師強調：這不是最佳化課，是最佳控制課。但古典最佳化的很多想法，之後會**原封不動搬到最佳控制**。所以今天先把有限維的情況弄懂。

今天的主題：

| 主題 | 課本 |
|---|---|
| 無約束問題的必要條件（梯度 = 0、Hessian 半正定） | §2.2.1 |
| 充分條件、凸函數 | 課本沒有 |
| 梯度法（找最小值的演算法） | 課本沒有 |
| 等式約束、Lagrange 乘數 | §2.2.2 |

不等式約束（KKT 條件）老師說**下次才講**，本集沒有。

---

## 1. 無約束問題的必要條件

### 1.1 一階條件：梯度 = 0

**什麼是必要條件？** [▶ 01:06](https://youtu.be/FbkNYklySak?t=66)

**必要最佳性條件**（necessary optimality condition，NOC）的意思是：

> 如果 $x^*$ 是局部最小值，**那麼**某件事一定成立。

用法是當「**過濾器**」：

- 某個點**不滿足** NOC → 它**絕對不可能**是局部最小值，丟掉。
- 某個點**滿足** NOC → 它**只是候選人**，不保證是最小值。

**怎麼推？** [▶ 02:07](https://youtu.be/FbkNYklySak?t=127)

想法：假設 $x^*$ 已經是局部最小值，然後把它稍微推一下（擾動 perturbation $\Delta x$），看會發生什麼事。

**Step 1：一階泰勒展開。** 如果 $f$ 可微，$\Delta x$ 很小時：

$$f(x^*+\Delta x)\approx f(x^*)+\nabla f(x^*)^\top \Delta x$$

這裡梯度（gradient）的定義是 [▶ 04:12](https://youtu.be/FbkNYklySak?t=252)：

$$\nabla f(x)=\left(\frac{\partial f}{\partial x_1},\ \frac{\partial f}{\partial x_2},\ \dots,\ \frac{\partial f}{\partial x_n}\right)^\top$$

【口頭】課堂上轉置會寫成 $^\top$ 或 $'$（prime），兩個意思一樣。

**Step 2：用「局部最小」的定義。** [▶ 05:20](https://youtu.be/FbkNYklySak?t=320) $x^*$ 是局部最小，所以往旁邊走一點點，函數值只會變大或不變：

$$f(x^*+\Delta x)-f(x^*)\ge 0$$

代入 Step 1：

$$\nabla f(x^*)^\top\Delta x=\sum_{i=1}^n \frac{\partial f(x^*)}{\partial x_i}\,\Delta x_i\ \ge\ 0 \quad\text{對所有夠小的 }\Delta x$$

**Step 3：挑幾個特別的 $\Delta x$。** [▶ 07:58](https://youtu.be/FbkNYklySak?t=478) 上式對**所有**夠小的 $\Delta x$ 都要成立。那就挑最簡單的：只有第 $i$ 個分量不是 0。

- 取 $\Delta x=\varepsilon e_i$（$\varepsilon>0$ 很小，$e_i$ 是第 $i$ 個單位向量）→ $\varepsilon\,\dfrac{\partial f}{\partial x_i}\ge 0$ → $\dfrac{\partial f}{\partial x_i}\ge 0$
- 取 $\Delta x=-\varepsilon e_i$ → $-\varepsilon\,\dfrac{\partial f}{\partial x_i}\ge 0$ → $\dfrac{\partial f}{\partial x_i}\le 0$

**Step 4：** [▶ 09:31](https://youtu.be/FbkNYklySak?t=571) 一個數同時 $\ge 0$ 又 $\le 0$，只能是 0。每個 $i$ 都這樣，所以：

$$\boxed{\nabla f(x^*)=0}$$

滿足 $\nabla f(x)=0$ 的點叫**駐點**（stationary point）。

**為什麼只是「必要」？** [▶ 10:35](https://youtu.be/FbkNYklySak?t=635) 一維的圖：局部最小值的地方導數是 0；但**局部最大值**的地方導數也是 0。所以「導數 = 0」擋不掉最大值。

### 1.2 二階條件：Hessian 半正定

[▶ 11:37](https://youtu.be/FbkNYklySak?t=697) 再往下展開一階：

$$f(x^*+\Delta x)-f(x^*)\approx \nabla f(x^*)^\top\Delta x+\frac12\,\Delta x^\top \nabla^2 f(x^*)\,\Delta x$$

$\nabla^2 f$ 叫 **Hessian**（海森矩陣），就是把所有二階偏導數排成的矩陣：$\left[\nabla^2 f\right]_{ij}=\dfrac{\partial^2 f}{\partial x_i\,\partial x_j}$。

> ⚠️ 逐字稿缺字 [▶ 03:41](https://youtu.be/FbkNYklySak?t=221)：字幕寫「This is the **action** of the function f」，應為「the **Hessian** of the function f」。
>
> 【課本補充】課本的二階項有係數 $\tfrac12$；老師口述時沒有特別提。係數不影響下面的結論。

[▶ 12:07](https://youtu.be/FbkNYklySak?t=727) 推法跟一階一樣：

1. 左邊 $\ge 0$（局部最小的定義）。
2. 一階項已經證明是 0（因為 $\nabla f(x^*)=0$）。
3. 剩下：$\Delta x^\top\nabla^2 f(x^*)\,\Delta x\ge 0$，而且 $\Delta x$ 可以是任何方向。

「對任何向量 $v$ 都有 $v^\top A v\ge 0$」**正好就是半正定**（positive semidefinite）的定義。所以：

$$\boxed{\nabla^2 f(x^*)\succeq 0}$$

### 1.3 NOC 定理，和為什麼要「開集合」

[▶ 12:38](https://youtu.be/FbkNYklySak?t=758) **定理（無約束局部最小值的必要條件）**

> 設 $x^*$ 是 $f:\mathbb{R}^n\to\mathbb{R}$ 的無約束局部最小值，且 $f$ 在一個包含 $x^*$ 的**開集合**上是 $C^1$（連續可微）。那麼
> $$\nabla f(x^*)=0\qquad\text{（一階 NOC）}$$
> 如果再加上 $f$ 是 $C^2$（二次連續可微），那麼
> $$\nabla^2 f(x^*)\succeq 0\qquad\text{（二階 NOC）}$$

（課本 Theorem 2.2.1，式 (2.6)(2.7)。）

**為什麼要開集合？** [▶ 13:45](https://youtu.be/FbkNYklySak?t=825)

**開集合**（open set）粗略說：每個點周圍都還有一小顆球在集合裡面。也就是說，**不含邊界**。

反例 [▶ 14:20](https://youtu.be/FbkNYklySak?t=860)：$f$ 只定義在 $[a,b]$ 上，而且一路往上升。那 $a$ 是局部最小值（往允許的方向走，函數都變大），可是 $f'(a)\ne 0$。

原因：$a$ 在**邊界**上，只能往右走，不能往左走。Step 3 裡「取 $-\varepsilon e_i$」那一步就不能做了。

所以 NOC 只對**定義域內部**的點有用。

【Q&A】[▶ 14:51](https://youtu.be/FbkNYklySak?t=891) 學生問：開集合是不是代表「沒有約束」？
答：不是。像開區間 $(a,b)$ 有上下界，但不含端點。重點只是「不要挑定義域邊界上的點」。如果定義域是整個 $\mathbb{R}^n$，它沒有邊界，自然是開集合，定理直接成立。（[▶ 15:26](https://youtu.be/FbkNYklySak?t=926) 中間有另一個人幫忙解釋：「Basically, you don't want to pick points that are on the boundary of your domain.」）

### 1.4 充分條件：Hessian 正定

[▶ 16:57](https://youtu.be/FbkNYklySak?t=1017) 能不能反過來，給一個「**只要**成立，**就一定**是局部最小」的條件？

老師只給直覺：把「半正定」加強成「**正定**」（positive definite，$\nabla^2 f(x^*)\succ 0$，即 $v\ne 0$ 時 $v^\top A v>0$）。

直覺：梯度 = 0 而且 Hessian 正定 → $x^*$ 附近的函數長得像一個**碗**。一離開 $x^*$，函數值馬上變大。

> 以下**不是逐字稿內容**，是依口述和標準教科書寫法重建的定理文字（投影片上的原文字幕沒有唸出來）：
>
> **充分條件**：若 $f$ 在包含 $x^*$ 的開集合上是 $C^2$，且 $\nabla f(x^*)=0$、$\nabla^2 f(x^*)\succ 0$，則 $x^*$ 是（嚴格）局部最小值。

【口頭】嚴格證明要多做一點：泰勒展開還有誤差項，要用極限論證把它壓掉。老師沒有做。

【口頭】[▶ 18:02](https://youtu.be/FbkNYklySak?t=1082) 實際用法：先找出所有梯度 = 0 的點（假設找到 6 個），再一個一個代進去算函數值，或用其他論證判斷哪個是最小。

課本 §2.2.1 只寫到必要條件，沒有充分條件。

---

## 2. 凸函數

> 本節課本沒有，全部來自課堂口述。

### 2.1 凸集合與凸函數的定義

**凸集合**（convex set）[▶ 19:03](https://youtu.be/FbkNYklySak?t=1143)

> 集合 $C\subseteq\mathbb{R}^n$ 是凸的：任取兩點 $x,y\in C$，連起來的線段整條都在 $C$ 裡。
> $$\alpha x+(1-\alpha)y\in C,\qquad \forall\, x,y\in C,\ \alpha\in[0,1]$$

[▶ 19:33](https://youtu.be/FbkNYklySak?t=1173) 圓盤是凸的。腰子形（凹進去一塊）不是：挑凹口兩邊的點，線段會跑出集合。

**凸函數**（convex function）[▶ 20:03](https://youtu.be/FbkNYklySak?t=1203)

> $C$ 是凸集合。$f:C\to\mathbb{R}$ 是凸函數：
> $$f\left(\alpha x+(1-\alpha)y\right)\le \alpha f(x)+(1-\alpha)f(y),\qquad \forall\, x,y\in C,\ \alpha\in[0,1]$$

（字幕只說「if this condition holds」，式子寫在投影片上。上式是依接下來的圖說明寫出的標準定義。）

**圖的意思** [▶ 20:38](https://youtu.be/FbkNYklySak?t=1238)：

- 左邊 $f(\alpha x+(1-\alpha)y)$：在 $x,y$ 中間某點，函數圖形的高度。
- 右邊 $\alpha f(x)+(1-\alpha)f(y)$：連接 $(x,f(x))$ 和 $(y,f(y))$ 的**弦**，在同一點的高度。
- 凸 = **弦永遠在圖形上面**（或貼著）。

像碗一樣往上彎的函數是凸的；有一段往下彎的就不是（弦會跑到圖形下面）。

**嚴格凸**（strictly convex）：上面的不等式在 $x\ne y$、$\alpha\in(0,1)$ 時是嚴格的 $<$。

### 2.2 為什麼凸很好

[▶ 22:17](https://youtu.be/FbkNYklySak?t=1337) 凸函數還是**非線性**函數，但行為非常好：

1. **局部最小 = 全域最小。** 一般非線性函數可能有很多局部最小值，只有其中一些是全域最小；凸函數不會有這個問題。
2. **嚴格凸 → 全域最小值最多只有一個。**
   > ⚠️ 逐字稿缺字 [▶ 22:49](https://youtu.be/FbkNYklySak?t=1369)：字幕寫「there is **at least at most** one global minimum」，老師是口誤後改口，意思是「**最多**一個」。
3. **凸且可微 → $\nabla f(x^*)=0$ 是 $x^*$ 為全域最小值的「充分且必要」條件。**

第 3 點好在兩個地方 [▶ 23:23](https://youtu.be/FbkNYklySak?t=1403)：

- 梯度 = 0 從「必要」升級成「**充分**」。
- 而且是**全域**最優，不只局部。

【口頭】直覺：算梯度只是看函數在一個點附近的樣子（很「局部」的測試），卻能告訴你**整個函數**的事。所以凸函數在計算上容易很多。

【Q&A】[▶ 23:54](https://youtu.be/FbkNYklySak?t=1434) 學生問凸函數可不可微的問題（字幕大部分 [INAUDIBLE]）。老師說之後再回來談。

【口頭】[▶ 24:25](https://youtu.be/FbkNYklySak?t=1465) 預告：之後解開迴路最佳控制問題（算軌跡）時，有一個很紅的做法——**把問題凸化，解一個凸最佳化問題，得到新解，再凸化，一直重複**。這是機器人軌跡最佳化最常用的方法之一。

> ⚠️ 逐字稿缺字：字幕寫「successively **complexify** a function」，依上下文應為「**convexify**」（凸化）。

**NOC 的三個用途**（老師小結）[▶ 24:57](https://youtu.be/FbkNYklySak?t=1497)：

1. 過濾候選點。
2. 當作**演算法**的基礎（下一節）。
3. 敏感度分析（sensitivity analysis）：問題的參數（例如機器人的質量）變一點，最佳解會變多少。這超出本課範圍。

---

## 3. 演算法：梯度法

> 本節課本沒有，全部來自課堂口述。

[▶ 25:36](https://youtu.be/FbkNYklySak?t=1536) 用 NOC 把所有 $\nabla f=0$ 的點找出來，常常很麻煩。我們想要能**直接算出候選點**的計算方法。

**迭代法**（iterative method）[▶ 27:12](https://youtu.be/FbkNYklySak?t=1632)：

1. 從一個初始猜測 $x^0$ 開始（沒概念就猜原點）。
2. 用某個規則，一直產生新的猜測 $x^1, x^2, \dots$
3. 希望每次函數值都下降：$f(x^0)\ge f(x^1)\ge f(x^2)\ge\cdots$
4. 更新夠多次以後，希望已經到（或很接近）局部最小值。

問題是：**這個更新規則怎麼設計？** 答案還是用一階泰勒展開。

### 3.1 為什麼往負梯度走，函數會變小

[▶ 29:47](https://youtu.be/FbkNYklySak?t=1787) 現在在 $x$。定義新的猜測（$\alpha>0$）：

$$x_\alpha = x-\alpha\,\nabla f(x)$$

$\alpha$ 越大，離 $x$ 越遠。

**推導** [▶ 31:04](https://youtu.be/FbkNYklySak?t=1864)：$\alpha$ 夠小時，

$$
\begin{aligned}
f(x_\alpha) &\approx f(x)+\nabla f(x)^\top (x_\alpha - x) \\
&= f(x)+\nabla f(x)^\top\left(-\alpha\,\nabla f(x)\right) \\
&= f(x)-\alpha\,\nabla f(x)^\top\nabla f(x) \\
&= f(x)-\alpha\,\|\nabla f(x)\|^2
\end{aligned}
$$

最後一步用 $v^\top v=\|v\|^2$（向量和自己的內積 = 長度平方）。

**關鍵** [▶ 32:45](https://youtu.be/FbkNYklySak?t=1965)：

- 如果 $\nabla f(x)=0$：你已經在候選點了。
- 如果 $\nabla f(x)\ne 0$：$\|\nabla f(x)\|^2>0$，所以 $-\alpha\|\nabla f(x)\|^2<0$，所以 $f(x_\alpha)<f(x)$。**找到一個讓函數變小的方向了。**

> ⚠️ 逐字稿缺字 [▶ 30:31](https://youtu.be/FbkNYklySak?t=1831)：老師在圖上說「x plus gradient of f leads you here」。依前一句的公式，更新是 $x$ **減** $\alpha\nabla f$；「plus」應是指先畫出梯度向量，再往反方向走。

【課堂討論】[▶ 33:17](https://youtu.be/FbkNYklySak?t=1997) 老師問：照公式，$\alpha$ 越大函數降越多，那為什麼不直接取 $\alpha=10^6$？

- 學生：會跳過最小值（skip over the minimum）。
- 另一個學生：因為那是近似。
- 老師：對。一階近似**只在 $x$ 附近**成立。走太遠，近似就不能代表真正的函數了，結果可能**衝過頭**（overshoot）。如果近似一直成立，函數就能被無限降低，這顯然不對。

### 3.2 下降方向 d 怎麼選

**一般化** [▶ 34:51](https://youtu.be/FbkNYklySak?t=2091)：不一定要沿著負梯度。一般寫成

$$x_\alpha=x+\alpha d,\qquad \text{只要 }\ \nabla f(x)^\top d<0$$

$d$ 叫**下降方向**（descent direction）。$d=-\nabla f(x)$ 是特例。只要內積是負的，照 3.1 一樣的推導，$f(x_\alpha)<f(x)$。

**幾何意義** [▶ 36:32](https://youtu.be/FbkNYklySak?t=2192)

- **等高線**（level set）：$\{x: f(x)=c\}$。在平面上畫出 $c_1<c_2<c_3$ 的一圈一圈曲線。
- 梯度**垂直於等高線**，指向函數變大的方向。
- $\nabla f^\top d<0$ ⟺ $d$ 和梯度夾角**大於 90°**。也就是「往下坡那半邊」的任何方向都可以。

**梯度法**（gradient method）[▶ 38:07](https://youtu.be/FbkNYklySak?t=2287)：

$$x^{k+1}=x^k+\alpha^k d^k$$

- 上標 $k$ 是第幾次迭代，**不是**次方。
- 如果 $\nabla f(x^k)\ne 0$、$\nabla f(x^k)^\top d^k<0$、$\alpha^k>0$ 而且**選得夠小心**，就保證下降。

【Q&A】[▶ 39:10](https://youtu.be/FbkNYklySak?t=2350) 學生問：把二階項也考慮進來，保證還成立嗎？
答：可以。一種是也用 Hessian 的資訊（下面馬上講），另一種是用更精細的近似設計更複雜的演算法。本課走前者。

**常見選法：$d=-D\nabla f$** [▶ 40:40](https://youtu.be/FbkNYklySak?t=2440)

$$d^k=-D^k\,\nabla f(x^k),\qquad D^k\succ 0\ \text{（正定矩陣）}$$

為什麼一定是下降方向：$\nabla f^\top d=-\nabla f^\top D\,\nabla f<0$（$D$ 正定，前面有負號）。

> ⚠️ 逐字稿缺字 [▶ 41:11](https://youtu.be/FbkNYklySak?t=2471)：字幕寫「we've chosen **d** to be positive definite」，依式子應是大寫矩陣 **$D$** 正定。

兩個常見選擇 [▶ 41:11](https://youtu.be/FbkNYklySak?t=2471)：

| 選法 | $D$ | 名字 |
|---|---|---|
| 1 | $I$（單位矩陣） | 最陡下降法（steepest descent），就是沿負梯度走 |
| 2 | $\left(\nabla^2 f(x^k)\right)^{-1}$ | 牛頓法（Newton's method），用 Hessian |

（「最陡下降法」「牛頓法」這兩個名字老師在字幕裡沒有說出來，是通用名稱。）

**為什麼要用 Hessian？圓 vs 橢圓** [▶ 41:41](https://youtu.be/FbkNYklySak?t=2501)

- **等高線是圓**（例如 $f=x_1^2+x_2^2$）：負梯度**直接指向**最小值（原點）。走幾步就到。
- **等高線是拉長的橢圓** [▶ 43:17](https://youtu.be/FbkNYklySak?t=2597)：負梯度垂直於橢圓，**不指向**中心。結果會一直**之字形**（zigzag）來回走，很慢。

【口頭】Hessian 帶有**曲率**（curvature）的資訊，讓演算法「認得出」這兩種問題不一樣，選比較好的方向。

**代價** [▶ 44:49](https://youtu.be/FbkNYklySak?t=2689)：用 Hessian 每一步都要算二階導數矩陣。

- 好處：方向比較準，**迭代次數**變少。
- 壞處：**每一步**貴很多。
- 問題很大時，可能划不來。

【口頭】這個「演算法要多精緻 vs. 多快」的取捨，整門課會一直出現。

### 3.3 步長 α 怎麼選

[▶ 45:50](https://youtu.be/FbkNYklySak?t=2750) 三種：

| 規則 | 做法 | 優點 | 缺點 |
|---|---|---|---|
| **最小化法則**（minimization rule） | $\alpha^k=\arg\min_{\alpha\ge 0} f(x^k+\alpha d^k)$ | 每步降最多 | 每步要解一個一維最佳化 |
| **固定步長**（constant） | 例如永遠 $\alpha=0.1$ | 最簡單 | 可能**發散**，或收斂很慢 |
| **遞減步長**（diminishing） | $\alpha^k\to 0$，但 $\sum_k\alpha^k=\infty$ | 先大步後小步 | 參數要調 |

**遞減步長的直覺** [▶ 46:51](https://youtu.be/FbkNYklySak?t=2811)

- 一開始離最小值很遠 → 大步跳，快速前進。可能會衝過頭。
- 靠近以後 → 步子越來越小，不會在最小值附近一直來回震盪，做最後的微調。
- 為什麼要 $\sum_k\alpha^k=\infty$：如果 $\alpha$ 太快變 0，總共走的距離有限，可能**還沒走到就停了**。加總無限大 = 保證「必要時可以走很遠」。

【Q&A】[▶ 48:25](https://youtu.be/FbkNYklySak?t=2905) 學生問：第一步的 $\alpha$ 怎麼選？
答：基本上是猜。有很多超參數（hyperparameter）要調。下降方向的選法比較有原理；步長比較靠經驗。

### 3.4 本集沒細講的部分

[▶ 49:26](https://youtu.be/FbkNYklySak?t=2966) 老師點名但跳過（他說這些可以講半學期）：

1. **收斂性**：每一步會下降，不代表最後會到最小值。有一些條件可以保證收斂到**駐點**（梯度 = 0 的點）。
2. **何時停**（termination rule）[▶ 50:00](https://youtu.be/FbkNYklySak?t=3000)：
   - 固定跑 100 次就停；或
   - $|f(x^{k+1})-f(x^k)|<\varepsilon$ 就停（沒什麼進步了，不要再浪費計算）。
3. **收斂速度**（convergence rate）[▶ 50:32](https://youtu.be/FbkNYklySak?t=3032)：跟初始點、步長怎麼選有關。

**不用導數的方法**（derivative-free methods）[▶ 51:03](https://youtu.be/FbkNYklySak?t=3063)：

- **座標下降法**（coordinate descent）：輪流沿著每個座標軸方向做最小化。
- **Nelder–Mead 法**：完全不用算導數。

### 3.5 梯度法整理：在解什麼／步驟／什麼時候會失敗

**在解什麼**：無約束問題 $\min_{x\in\mathbb{R}^n} f(x)$，$f$ 可微。目標是找到一個**駐點**（局部最小值的候選人），不用把所有 $\nabla f=0$ 的點解出來。

**步驟**（虛擬碼）：

```
輸入：初始猜測 x⁰、步長規則、停止條件
k ← 0
重複：
    1. 算梯度 g = ∇f(xᵏ)
    2. 選下降方向 dᵏ = −Dᵏ g（Dᵏ 正定；Dᵏ = I 或 Hessian 的反矩陣）
    3. 選步長 αᵏ > 0（最小化法則／固定／遞減）
    4. xᵏ⁺¹ ← xᵏ + αᵏ dᵏ
    5. 若滿足停止條件，結束；否則 k ← k + 1
輸出：xᵏ
```

**什麼時候會失敗**：

| 情況 | 會怎樣 | 來源 |
|---|---|---|
| 步長太大 | 一階近似失效，衝過頭；固定步長可能發散 | 課堂 |
| 遞減步長降太快 | 總距離有限，走不到最小值就停 | 課堂 |
| 等高線很扁（橢圓） | 最陡下降法之字形，很慢 | 課堂 |
| 問題維度很大 | 牛頓法每步要算 Hessian，太貴 | 課堂 |
| 函數非凸 | 只保證到**駐點**，可能是局部最小、甚至鞍點，不一定是全域最小 | 依 1.1、2.2 推論 |

---

## 4. 等式約束問題

[▶ 51:35](https://youtu.be/FbkNYklySak?t=3095) 為什麼要學約束：最佳控制**至少**有一個約束——**動力學**（dynamics）。

【口頭】[▶ 52:05](https://youtu.be/FbkNYklySak?t=3125) 「你可以盡量最佳化，但開 Fiat 500 就是開不出 Ferrari 的性能。」系統的物理限制本身就是約束。

解約束問題的關鍵概念是 **Lagrange 乘數**（Lagrange multiplier），之後在最佳控制裡也會再出現。本集不做證明，只給直覺。

### 4.1 兩種處理約束的想法

[▶ 52:37](https://youtu.be/FbkNYklySak?t=3157)

1. **懲罰法**（penalty viewpoint）：把約束搬進目標函數，違反就罰分。滿足約束 → 罰 0；不滿足 → 成本飆高。這樣就把**有約束**問題變成**無約束**問題。
2. **可行位移法** [▶ 53:08](https://youtu.be/FbkNYklySak?t=3188)：照第 1 節的推法，但這次不能隨便亂推 $\Delta x$——有些方向會違反約束，不允許。要先定義什麼叫「**允許的位移**」，再推必要條件。

### 4.2 Lagrange 乘數定理

**問題** [▶ 53:38](https://youtu.be/FbkNYklySak?t=3218)：

$$
\begin{aligned}
\min_{x\in\mathbb{R}^n}\quad & f(x) \\
\text{subject to}\quad & h_i(x)=0,\quad i=1,\dots,m
\end{aligned}
$$

$f,h_i:\mathbb{R}^n\to\mathbb{R}$ 都是連續可微。把 $m$ 個約束寫成向量 $\mathbf{h}(x)=\left(h_1(x),\dots,h_m(x)\right)^\top$，約束就是 $\mathbf{h}(x)=0$。

【口頭】本課粗體 = 向量。

**定理（直接講結論）** [▶ 54:41](https://youtu.be/FbkNYklySak?t=3281)：

> 如果 $x^*$ 是局部最小值，那麼存在 $m$ 個數 $\lambda_1,\dots,\lambda_m$（**Lagrange 乘數**，一個約束一個），使得
> $$\nabla f(x^*)+\sum_{i=1}^m \lambda_i\,\nabla h_i(x^*)=0$$

（還需要一個技術條件，見 4.6。）

**跟無約束比** [▶ 55:45](https://youtu.be/FbkNYklySak?t=3345)：如果沒有約束（$m=0$），右邊的和不見了，就回到 $\nabla f(x^*)=0$。所以這是「梯度 = 0」的升級版：**梯度加上約束梯度的線性組合 = 0**。

> ⚠️ 逐字稿缺字 [▶ 55:45](https://youtu.be/FbkNYklySak?t=3345)：字幕寫「we recover the condition **greater than or equal to 0**」，依上下文應為「gradient **equal to** 0」。

### 4.3 例子：在圓上最小化 x₁ + x₂

[▶ 56:15](https://youtu.be/FbkNYklySak?t=3375)

$$
\begin{aligned}
\min\quad & f(x)=x_1+x_2 \\
\text{s.t.}\quad & h(x)=x_1^2+x_2^2-2=0
\end{aligned}
$$

可行集合（feasible set）是半徑 $\sqrt 2$ 的圓。只能在圓上挑點，要讓 $x_1+x_2$ 最小。

**Step 1：算梯度** [▶ 57:47](https://youtu.be/FbkNYklySak?t=3467)

$$\nabla f=\begin{pmatrix}1\\1\end{pmatrix},\qquad \nabla h=\begin{pmatrix}2x_1\\2x_2\end{pmatrix}$$

**Step 2：寫 Lagrange 條件**（只有一個約束，一個 $\lambda$）

$$\begin{pmatrix}1\\1\end{pmatrix}+\lambda\begin{pmatrix}2x_1\\2x_2\end{pmatrix}=0$$

**Step 3：不夠的方程式** 【課堂討論】[▶ 59:58](https://youtu.be/FbkNYklySak?t=3598)

老師問：未知數有 $x_1,x_2,\lambda$ 三個，方程式只有兩條，第三條從哪來？
學生答出來：$x$ 本身要**可行**，也就是要在圓上：$x_1^2+x_2^2=2$。

**Step 4：解** [▶ 60:31](https://youtu.be/FbkNYklySak?t=3631)

由 Step 2：
$$1+2\lambda x_1=0,\quad 1+2\lambda x_2=0\ \Rightarrow\ x_1=x_2=-\frac{1}{2\lambda}$$

代入約束：
$$\frac{1}{4\lambda^2}+\frac{1}{4\lambda^2}=2\ \Rightarrow\ \frac{1}{2\lambda^2}=2\ \Rightarrow\ \lambda^2=\frac14\ \Rightarrow\ \lambda=\pm\frac12$$

**Step 5：兩個候選點** [▶ 62:14](https://youtu.be/FbkNYklySak?t=3734)

| $\lambda$ | $(x_1,x_2)$ | $f=x_1+x_2$ |
|---|---|---|
| $+\tfrac12$ | $(-1,-1)$ | $-2$ ← **最小** |
| $-\tfrac12$ | $(1,1)$ | $2$（其實是最大） |

> ⚠️ 逐字稿缺字 [▶ 61:32](https://youtu.be/FbkNYklySak?t=3692)：字幕寫「if lambda is equal to **12**」，應為 $\lambda=\tfrac12$（代回 $x_1=-1/(2\lambda)=-1$ 可驗證）。

**驗算**（不是逐字稿內容，是代回檢查）：在 $(-1,-1)$，$\nabla h=(-2,-2)^\top$，$\nabla f+\tfrac12\nabla h=(1,1)^\top+(-1,-1)^\top=0$ ✓。

**$\lambda$ 是拿來幹嘛的？** [▶ 62:45](https://youtu.be/FbkNYklySak?t=3765) 照今天的講法，$\lambda$ 只是**工具**：用來湊出足夠的方程式。解完、找到 $x$ 之後就丟掉。

【口頭】老師補一句：「其實 Lagrange 乘數本身是有意義的」，但沒展開。
【課本補充】課本 §2.2.2 開頭提到：Lagrange 乘數能告訴你「約束稍微改變時，最佳成本會變多少」（敏感度）。課本這裡也沒展開。

**方程式數量一定剛好** [▶ 63:16](https://youtu.be/FbkNYklySak?t=3796)：Lagrange 條件 $n$ 條 + 約束 $m$ 條 = $n+m$ 條；未知數 $x$ 有 $n$ 個 + $\lambda$ 有 $m$ 個 = $n+m$ 個。但方程式可能是**非線性**的，解起來不一定容易。

### 4.4 幾何意義一：等高線相切

[▶ 63:48](https://youtu.be/FbkNYklySak?t=3828) 目標函數的等高線 $x_1+x_2=c$ 是斜率 $-1$ 的直線 $x_2=c-x_1$。往右上 $c$ 變大。

想像把直線**往左下推**，讓 $c$ 越來越小，但還要碰得到圓 [▶ 64:54](https://youtu.be/FbkNYklySak?t=3894)：

- $c=0$：直線穿過原點，跟圓交兩點。
- $c=-1$：還是交兩點。
- $c=-2$：剛好**切**在 $(-1,-1)$。
- $c<-2$：碰不到圓了，沒有可行點。

所以最小值就在**相切點**。

**為什麼相切 ⟺ Lagrange 條件** [▶ 68:02](https://youtu.be/FbkNYklySak?t=4082)（一個約束的情況）：

1. Lagrange 條件說 $\nabla f=-\lambda\nabla h$，也就是兩個梯度**共線**（collinear）。
2. 梯度垂直於自己的等高線。
3. 兩個梯度共線 → 兩條等高線（目標的、約束的）在那點**方向相同** → **相切**。

在 $(-1,-1)$：$\nabla f=(1,1)$，$\nabla h=(-2,-2)$，確實共線 [▶ 69:34](https://youtu.be/FbkNYklySak?t=4174)。

【口頭】[▶ 70:05](https://youtu.be/FbkNYklySak?t=4205) 「相切」就是「不能再推了」的幾何說法：再推一點，就跟可行集合分開了。

一般 $m$ 個約束時：$\nabla f(x^*)$ 落在約束梯度 $\nabla h_1,\dots,\nabla h_m$ **張成的子空間**裡。

【Q&A】[▶ 65:54](https://youtu.be/FbkNYklySak?t=3954) 學生問：為什麼有兩個 $\lambda$？一個最大、一個最小？
答：對。這只是**駐點**的必要條件，分不出最大或最小。代另一個 $\lambda$ 會得到最大值。

【Q&A】[▶ 66:25](https://youtu.be/FbkNYklySak?t=3985) 學生問：如果 $\lambda=0$，是不是代表約束不重要？
答：不是。約束永遠重要，因為只能從可行集合裡挑點。而且 Lagrange 條件講的是約束的**梯度**，不是約束本身，所以 $\lambda=0$ 不能直接解讀成約束的什麼性質。

### 4.5 幾何意義二：梯度垂直於可行變動

[▶ 70:37](https://youtu.be/FbkNYklySak?t=4237) 老師說這個講法他覺得更清楚。

**一階可行變動的子空間** [▶ 71:08](https://youtu.be/FbkNYklySak?t=4268)：

$$V(x^*)=\left\{\Delta x\ :\ \nabla h_i(x^*)^\top\Delta x=0,\ i=1,\dots,m\right\}$$

**為什麼叫「可行」** [▶ 71:38](https://youtu.be/FbkNYklySak?t=4298)：

$$h(x^*+\Delta x)\approx \underbrace{h(x^*)}_{=0\ (x^*\text{ 可行})}+\underbrace{\nabla h(x^*)^\top\Delta x}_{=0\ (\Delta x\in V)}=0$$

所以沿 $V(x^*)$ 裡的方向走，到一階為止還是滿足約束。

**Lagrange 條件 ⟹ 梯度垂直於 $V$** [▶ 72:43](https://youtu.be/FbkNYklySak?t=4363)：取 $\Delta x\in V(x^*)$，

$$\nabla f(x^*)^\top\Delta x=-\sum_{i=1}^m\lambda_i\,\underbrace{\nabla h_i(x^*)^\top\Delta x}_{=0}=0$$

**跟無約束比較** [▶ 73:49](https://youtu.be/FbkNYklySak?t=4429)：

| | 允許的 $\Delta x$ | 必要條件 |
|---|---|---|
| 無約束 | 任何方向 | $\nabla f^\top\Delta x=0$ 對所有 $\Delta x$ → $\nabla f=0$ |
| 等式約束 | 只有 $V(x^*)$ 裡的 | $\nabla f^\top\Delta x=0$ 對所有 $\Delta x\in V(x^*)$ → Lagrange 條件 |

【口頭】同一個想法，只是現在不能考慮所有位移，只能考慮「到一階還滿足約束」的位移。

### 4.6 正則點條件與證明方向

**完整定理** [▶ 74:51](https://youtu.be/FbkNYklySak?t=4491)（課本 Theorem 2.2.2）

> 設 $x^*$ 是 $f$ 在約束 $h_i(x)=0$（$i=1,\dots,m$）下的局部最小值，而且約束梯度 $\nabla h_1(x^*),\dots,\nabla h_m(x^*)$ **線性獨立**。那麼存在**唯一**的向量 $\lambda=(\lambda_1,\dots,\lambda_m)^\top$（Lagrange 乘數向量），使得
> $$\nabla f(x^*)+\sum_{i=1}^m\lambda_i\,\nabla h_i(x^*)=0$$

約束梯度線性獨立的可行點叫**正則點**（regular point）。

【口頭】如果約束梯度不線性獨立，這就**不再是**必要條件了。老師不展開，只提醒：**拿到候選點時，記得檢查約束梯度是否線性獨立。**

**怎麼證明** [▶ 75:56](https://youtu.be/FbkNYklySak?t=4556)（只講方向）：

1. **懲罰法**：把約束搬進成本，懲罰不可行，再取極限。
2. **消去法**：用 $m$ 條約束把 $m$ 個變數寫成另外 $n-m$ 個的函數，變成無約束問題。比較直觀但記帳很煩（老師說「三頁分析」）。

【口頭】推薦書：Dimitri Bertsekas 的非線性最佳化教科書，想深入收斂速度、Lagrange 定理證明、技術條件可以看。

> ⚠️ 逐字稿缺字 [▶ 76:28](https://youtu.be/FbkNYklySak?t=4588)：老師口述書名為「Nonlinear **Optimization**」。課本參考文獻 [13] 寫的是 D. Bertsekas, *Nonlinear **Programming***, Athena Scientific, 2016，應是同一本。

### 4.7 Lagrangian 函數

[▶ 76:58](https://youtu.be/FbkNYklySak?t=4618) 好記的寫法（之後最佳控制也會用）：

$$L(x,\lambda)=f(x)+\sum_{i=1}^m\lambda_i\,h_i(x)$$

把約束乘上 $\lambda$「抬進」成本，然後**假裝它是無約束問題**，對所有變數令梯度 = 0：

$$
\begin{aligned}
\nabla_x L(x^*,\lambda^*) &= \nabla f(x^*)+\sum_{i=1}^m\lambda_i^*\,\nabla h_i(x^*)=0 &&\leftarrow\ n\ \text{條，就是 Lagrange 條件} \\
\nabla_\lambda L(x^*,\lambda^*) &= \mathbf{h}(x^*)=0 &&\leftarrow\ m\ \text{條，就是約束本身}
\end{aligned}
$$

$n+m$ 條方程式，$n+m$ 個未知數。（課本式 (2.12)(2.13)。）

[▶ 78:32](https://youtu.be/FbkNYklySak?t=4712) 下次：簡短看**不等式約束**（會導出 KKT 條件，字幕此處 [INAUDIBLE]），然後進入第一個最佳控制主題。

---

## 5. 一頁速查表

### 必要／充分條件（無約束，$x^*$ 在定義域內部）

| 條件 | 式子 | 關鍵一步 |
|---|---|---|
| 一階必要 | $\nabla f(x^*)=0$ | $\nabla f^\top\Delta x\ge 0$，取 $\Delta x=\pm\varepsilon e_i$ → 每個偏導 $\ge 0$ 且 $\le 0$ |
| 二階必要 | $\nabla^2 f(x^*)\succeq 0$ | 一階項 = 0，剩 $\Delta x^\top\nabla^2 f\,\Delta x\ge 0$ 對所有方向 = 半正定定義 |
| 二階充分 | $\nabla f=0$ 且 $\nabla^2 f\succ 0$ → 嚴格局部最小 | 正定 → 附近像碗；嚴格證明要處理泰勒誤差項 |
| 邊界陷阱 | 邊界點可以是最小但 $\nabla f\ne 0$ | 只能往一側推，$-\varepsilon e_i$ 不允許 |

### 凸

- 凸集合：$\alpha x+(1-\alpha)y\in C$。
- 凸函數：$f(\alpha x+(1-\alpha)y)\le\alpha f(x)+(1-\alpha)f(y)$（弦在圖形上方）。
- 凸 → 局部最小 = 全域最小；嚴格凸 → 最多一個全域最小；凸且可微 → $\nabla f=0$ ⟺ 全域最小。

### 梯度法

$$x^{k+1}=x^k+\alpha^k d^k,\qquad \nabla f(x^k)^\top d^k<0,\qquad \alpha^k>0$$

- 為什麼下降：$f(x+\alpha d)\approx f(x)+\alpha\,\nabla f^\top d<f(x)$（$\alpha$ 小）。$d=-\nabla f$ 時下降量 $\approx\alpha\|\nabla f\|^2$。
- $d=-D\nabla f$，$D\succ 0$：$D=I$ 最陡下降；$D=(\nabla^2 f)^{-1}$ 牛頓法（方向準、每步貴）。
- 步長：最小化法則／固定（可能發散）／遞減（$\alpha^k\to 0$、$\sum\alpha^k=\infty$）。

### 等式約束

$$\min f(x)\quad \text{s.t.}\quad h_i(x)=0,\ i=1,\dots,m$$

| 項目 | 式子 |
|---|---|
| Lagrange 條件（$x^*$ 正則） | $\nabla f(x^*)+\sum_i\lambda_i\nabla h_i(x^*)=0$，$\lambda$ 唯一 |
| 正則點 | $\nabla h_1(x^*),\dots,\nabla h_m(x^*)$ 線性獨立 |
| 一階可行變動 | $V(x^*)=\{\Delta x:\nabla h_i(x^*)^\top\Delta x=0\ \forall i\}$ |
| 等價說法 | $\nabla f(x^*)\perp V(x^*)$（關鍵一步：$\nabla f^\top\Delta x=-\sum\lambda_i\nabla h_i^\top\Delta x=0$） |
| 幾何 | 一個約束時，$\nabla f\parallel\nabla h$ → 等高線相切 |
| Lagrangian | $L=f+\sum\lambda_i h_i$；$\nabla_x L=0$（$n$ 條）、$\nabla_\lambda L=0$（$m$ 條） |
| 解法 | Lagrange 條件 + 約束本身，共 $n+m$ 條聯立 |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 必要最佳性條件（NOC）當過濾器 | 第 3 集變分法、第 4 集間接法：無限維版本的 NOC（課本 §2.2.3 Pontryagin 最小原理） |
| Lagrange 乘數、Lagrangian | 最佳控制的**協態**（costate）$p(t)$ 和 **Hamiltonian** $H=g+p^\top f$（課本 §2.2.3 說協態「類比於 Lagrange 乘數」） |
| 不等式約束 | 下一集開頭（KKT 條件，老師預告） |
| 反覆凸化、解凸問題 | 第 5、6 集計算方法／直接法（老師預告：機器人軌跡最佳化最常用的做法之一） |
| 梯度法、牛頓法、Hessian | 第 8 集 LQR 類演算法（待確認是否用到）；第 18 集 RL 策略最佳化（梯度上升） |
| 敏感度分析 | 老師說超出本課範圍 |

---

## 附：本集一句話總結

> **最小值的必要條件，都是同一招：「在最小值附近往允許的方向推一下，函數不能變小」。沒有約束時得到 $\nabla f=0$；有等式約束時，只能沿可行方向推，得到 $\nabla f+\sum\lambda_i\nabla h_i=0$。**

---

## ⚠️ 待確認清單

1. 上課日期：只知道第 1 集是週一、本集是週三，確切日期待補。
2. [▶ 16:57](https://youtu.be/FbkNYklySak?t=1017) 充分條件定理的投影片原文字幕沒唸出；筆記寫的是標準版本（含「嚴格」局部最小），待對照投影片。
3. [▶ 20:03](https://youtu.be/FbkNYklySak?t=1203) 凸函數不等式寫在投影片上，筆記依圖說明寫出標準定義，待對照投影片。
4. 第 6 節「梯度法、牛頓法在第 8 集 LQR 是否用到」是依集名推測，做到第 8 集時確認。

---

*筆記依據 Marco Pavone「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 2 錄影逐字稿（人工字幕，1:19:02）與《Principles of Robot Autonomy》§2.2.1–2.2.2 整理。*
