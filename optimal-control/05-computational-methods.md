---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 5
lecture: Lecture 5
date: 待補（第 3 週週一）
video: https://youtu.be/R4_fHzTo0IM
notes: 《Principles of Robot Autonomy》§2.2.3–2.2.4（書頁 64–67，PDF 頁 66–69）
---

# 第 5 集 · Lecture 5：Pontryagin 最小原理與計算方法（Computational Methods） [▶ 影片](https://youtu.be/R4_fHzTo0IM)

← 上一集：[04-indirect-methods](04-indirect-methods.md) ｜ [總目錄](README.md) ｜ 下一集：[06-direct-methods](06-direct-methods.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 5 集
> **講者**：Daniele Gammelli（本集沒有自我介紹；依接續上一集推斷）
> **來源**：YouTube 錄影逐字稿（1:18:04，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§2.2.3–2.2.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：控制無界的必要條件](#1-回顧控制無界的必要條件)
- [2. 為什麼控制有界會讓事情變難](#2-為什麼控制有界會讓事情變難)
- [3. Pontryagin 最小原理（PMP）](#3-pontryagin-最小原理pmp)
- [4. 例子：有界控制的最小能量問題](#4-例子有界控制的最小能量問題)
- [5. PMP 的額外條件](#5-pmp-的額外條件)
- [6. 三種典型問題](#6-三種典型問題)
  - [6.1 最短時間 → bang-bang](#61-最短時間--bang-bang)
  - [6.2 奇異弧](#62-奇異弧)
  - [6.3 最少燃料 → bang-off-bang](#63-最少燃料--bang-off-bang)
  - [6.4 最小能量 → 線性＋飽和](#64-最小能量--線性飽和)
- [7. 計算方法：解兩點邊界值問題](#7-計算方法解兩點邊界值問題)
  - [7.1 打靶法與配置法](#71-打靶法與配置法)
  - [7.2 用 solve_bvp](#72-用-solve_bvp)
  - [7.3 PMP 整理：在解什麼／步驟／什麼時候會失敗](#73-pmp-整理在解什麼步驟什麼時候會失敗)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/R4_fHzTo0IM?t=5) 第 3 週。今天和週三還在開迴路；下週進閉迴路。今天**收尾間接法**，週三開始直接法。

| 主題 | 課本 |
|---|---|
| 控制有界 → Pontryagin 最小原理 | §2.2.3 Theorem 2.2.3 |
| 例子：最小能量、最短時間、最少燃料 | 課本沒有 |
| PMP 額外條件、奇異弧 | 課本沒有 |
| 數值解 TPBVP：打靶法、配置法、`solve_bvp` | §2.2.4 |

【口頭】[▶ 02:10](https://youtu.be/R4_fHzTo0IM?t=130) 看典型問題有兩個目的：熟悉怎麼用條件，以及**觀察最佳控制長什麼樣子**。

---

## 1. 回顧：控制無界的必要條件

[▶ 03:11](https://youtu.be/R4_fHzTo0IM?t=191)

$$H=g+p^\top f$$

$$\dot x^*=\frac{\partial H}{\partial p},\qquad \dot p^*=-\frac{\partial H}{\partial x},\qquad 0=\frac{\partial H}{\partial u}$$

用第三條把 $u$ 寫成 $x,p$ 的函數，代進前兩條，再用邊界條件定積分常數。初始條件通常給定；終端的邊界條件看 $t_f$、$x(t_f)$ 固定或自由（上一集的「主邊界條件」和表）。

---

## 2. 為什麼控制有界會讓事情變難

[▶ 07:17](https://youtu.be/R4_fHzTo0IM?t=437) 實務上狀態和控制常常有界：

- **控制約束**：致動器有極限，推力不能無限大。
- **狀態約束**：例如避開障礙物。

本課**只處理控制有界**，不處理狀態約束 [▶ 07:49](https://youtu.be/R4_fHzTo0IM?t=469)，因為：

1. 數學會複雜很多。
2. 實務上間接法不是處理狀態約束的首選。

【口頭】[▶ 08:20](https://youtu.be/R4_fHzTo0IM?t=500) 實務做法：把問題當成**運動規劃**（motion planning），簡化動態、用幾何方式解軌跡，再用得到的洞見去引導間接法。

【Q&A】[▶ 08:50](https://youtu.be/R4_fHzTo0IM?t=530) 學生問：上一集雙積分器那題，算出 $t_f$ 是不是代表某個最佳控制？答：是，那題完整解出來了。解完微分方程就有 $x$、$p$，控制是它們的函數，代進去就得到控制形狀。學生追問：那題沒有約束，解出的控制有沒有可能違反某個界？答：當然可能，因為我們沒加約束。所謂「控制有界」是像 $|u|\le 1$ 這種限制。

**有限維的直覺** [▶ 10:57](https://youtu.be/R4_fHzTo0IM?t=657)

$$\Delta f=f(x+\Delta x)-f(x)\approx\nabla f(x)^\top\Delta x$$

局部最小 ⟹ 所有可容許的 $\Delta x$ 都有 $\Delta f\ge 0$。

- **無界**：$\Delta x$ 正負都可以 → $\nabla f^\top\Delta x\ge 0$ 且 $\le 0$ → $\nabla f=0$。
- **有界** [▶ 13:47](https://youtu.be/R4_fHzTo0IM?t=827)：函數定義在區間上，畫圖時兩個端點也可能是局部最小，但導數不是 0。

【課堂討論】[▶ 14:21](https://youtu.be/R4_fHzTo0IM?t=861) 講者問：左端點是不是局部最小？為什麼？學生：因為在允許的範圍內往任何地方走，函數都變大。講者：對。在左端點**只能往右走**；右端點只能往左走。

所以有界時，條件只能寫成 $\nabla f^\top\Delta x\ge 0$（對可容許的 $\Delta x$），不能推到 $=0$。

**無限維一樣** [▶ 15:52](https://youtu.be/R4_fHzTo0IM?t=952)

$\delta u$ 本身是一個函數 [▶ 16:58](https://youtu.be/R4_fHzTo0IM?t=1018)。講者畫圖：控制有上界 $\bar u$，某條 $u(t)$ 有時在界內、有時**貼在界上**。

- 在界內的時段：$\delta u$ 正負都可以。
- **貼在界上的時段**：只能往下變（往上就違反界）→ 變分是**單邊**的。

結論 [▶ 18:40](https://youtu.be/R4_fHzTo0IM?t=1120)：最佳控制有部分落在邊界上時，必要條件變成

$$\delta J(u^*,\delta u)\ge 0$$

而不是 $=0$。

【口頭】只要在約束下最佳化（例如時間），最佳控制**很常**有一段貼在邊界上。

【Q&A】[▶ 19:42](https://youtu.be/R4_fHzTo0IM?t=1182) 學生問：下面那張圖跟「只能往一個方向變」有什麼關係？答：推變分法基本定理時，關鍵是「可容許變分是任意的」。圖是在說明：控制貼在界上時，不能往正方向推（會違反界），所以變分不再任意，就推不出 $\delta J=0$。

---

## 3. Pontryagin 最小原理（PMP）

[▶ 21:22](https://youtu.be/R4_fHzTo0IM?t=1282) 有界控制的必要條件：把第三條**加強**。

> **Pontryagin 最小原理**（Pontryagin's Minimum Principle，PMP）
>
> 最優的 $(x^*,u^*,p^*)$ 滿足
> $$
> \begin{aligned}
> \dot x^*(t)&=\frac{\partial H}{\partial p}\left(x^*,u^*,p^*,t\right) \\
> \dot p^*(t)&=-\frac{\partial H}{\partial x}\left(x^*,u^*,p^*,t\right) \\
> H\left(x^*(t),u^*(t),p^*(t),t\right)&\le H\left(x^*(t),u(t),p^*(t),t\right)\quad\text{對所有可容許的 }u(t)
> \end{aligned}
> $$
> 以及上一集的邊界條件。

第三條等價寫法 [▶ 25:35](https://youtu.be/R4_fHzTo0IM?t=1535)：

$$u^*(t)=\arg\min_{u\in\mathcal{U}}H\left(x^*(t),u,p^*(t),t\right)$$

意思：$u^*$ 要是 Hamiltonian 的**全域最小值**（對 $u$），不只是駐點。

【課本補充】課本 Theorem 2.2.3（書頁 64）直接以這個形式陳述 PMP（$u^*(t)=\arg\min_{u\in\mathcal U}H$），沒有先講無界的版本。

【口頭】[▶ 22:22](https://youtu.be/R4_fHzTo0IM?t=1342) 從「$\delta J\ge 0$」跳到「最小化 $H$」中間有一大步，講者沒證明。重點是務實地會用。

**跟無界版本的關係** [▶ 27:14](https://youtu.be/R4_fHzTo0IM?t=1634)：想像把控制界放寬到完全不影響問題。那 $H$ 對 $u$ 的全域最小值一定也是駐點（$\partial H/\partial u=0$）。所以無界時，PMP 退化成上一集的條件。

【Q&A】[▶ 24:32](https://youtu.be/R4_fHzTo0IM?t=1472) 學生問：那個不等式是什麼意思？$u$ 不是最優、但 $x,p$ 是最優，這怎麼可能？答：把它看成「固定 $x^*$、$p^*$，只把 $H$ 當成 $u$ 的函數來最小化」。不等式是說 $u^*$ 比任何其他可容許 $u$ 都讓 $H$ 更小。

【Q&A】[▶ 28:48](https://youtu.be/R4_fHzTo0IM?t=1728) 學生問：$x$ 和 $u$ 互相耦合，怎麼能「假裝知道 $x^*$」去最小化 $H$？答：機制跟以前一樣：以前解代數方程把 $u$ 寫成 $x,p$ 的函數；現在改成**解一個最佳化問題**得到 $u(x,p)$，再代回去。只是比較複雜。

---

## 4. 例子：有界控制的最小能量問題

[▶ 24:02](https://youtu.be/R4_fHzTo0IM?t=1442)

$$
\begin{aligned}
\dot x_1&=x_2,\qquad \dot x_2=-x_2+u \\
J&=\frac12\int_{t_0}^{t_f}\left(x_1^2+u^2\right)dt \\
|u|&\le 1,\qquad t_f\ \text{固定},\ x(t_f)\ \text{自由}
\end{aligned}
$$

最小化控制平方（二次成本）的問題叫**最小能量**（minimum energy）問題。

> 系統方程是依 Hamiltonian 的展開式（$p_1x_2-p_2x_2+p_2u$）反推的；投影片原式字幕沒唸。

**Step 1：Hamiltonian** [▶ 30:23](https://youtu.be/R4_fHzTo0IM?t=1823)

$$H=\frac12\left(x_1^2+u^2\right)+p_1x_2+p_2\left(-x_2+u\right)=\frac12x_1^2+\frac12u^2+p_1x_2-p_2x_2+p_2u$$

**Step 2：對 $u$ 最小化 $H$** [▶ 32:00](https://youtu.be/R4_fHzTo0IM?t=1920)：只有 $\frac12u^2+p_2u$ 跟 $u$ 有關：

$$u^*=\arg\min_{|u|\le 1}\ \frac12u^2+p_2u$$

**Step 3：先不管界** [▶ 33:08](https://youtu.be/R4_fHzTo0IM?t=1988)：二次函數，令導數 = 0：$u+p_2=0\Rightarrow u=-p_2$。

**Step 4：分情況** [▶ 34:20](https://youtu.be/R4_fHzTo0IM?t=2060)：拋物線最低點在 $-p_2$，但只能在 $[-1,1]$ 裡選。

| 情況 | $u^*$ | 理由 |
|---|---|---|
| $-1\le -p_2\le 1$ | $-p_2$ | 最低點在允許範圍內 |
| $-p_2<-1$（即 $p_2>1$） | $-1$ | 拋物線在 $[-1,1]$ 上遞增，取左端 |
| $-p_2>1$（即 $p_2<-1$） | $1$ | 拋物線在 $[-1,1]$ 上遞減，取右端 |

【課堂討論】[▶ 35:54](https://youtu.be/R4_fHzTo0IM?t=2154) 講者問 $-p_2<-1$ 時最小值在哪？學生：$-1$。

【Q&A】[▶ 40:04](https://youtu.be/R4_fHzTo0IM?t=2404) 學生問那張拋物線圖的軸是什麼。答：橫軸 $u$，縱軸 $H$（當成 $u$ 的函數）。

**控制的形狀** [▶ 37:29](https://youtu.be/R4_fHzTo0IM?t=2249)：把 $u^*$ 畫成 $p_2$ 的函數——中間是斜率 $-1$ 的直線，兩邊**飽和**（saturate）在 $\pm1$。沒有界的話就只有那條直線。

【口頭】[▶ 36:57](https://youtu.be/R4_fHzTo0IM?t=2217) 間接法的強項之一：**不用真的解出微分方程**，就已經知道最佳控制的**結構**。不管 $p_2$ 最後是多少，控制一定長這個樣子。

【Q&A】[▶ 38:34](https://youtu.be/R4_fHzTo0IM?t=2314) 學生問：另外兩條條件呢？答：把 $u^*(p)$ 代進狀態、協態方程，再解析或數值解。這裡只做一半（只推出 $u$ 的形狀）。$t_f$ 等邊界條件用來定積分常數。

---

## 5. PMP 的額外條件

[▶ 41:08](https://youtu.be/R4_fHzTo0IM?t=2468) Pontryagin 等人依問題結構還推出更多必要條件。講者說對本課不太重要，只舉例：

| 條件 | 結論 |
|---|---|
| $t_f$ **固定**，且 $H$ 不顯式依賴 $t$ | $H\left(x^*,u^*,p^*\right)=$ 常數，$\forall t\in[t_0,t_f]$ |
| $t_f$ **自由**，且 $H$ 不顯式依賴 $t$ | $H\left(x^*,u^*,p^*\right)=0$，$\forall t\in[t_0,t_f]$ |

【口頭】條件越多越好：能把最佳解的結構描述得更清楚。

> ⚠️ 逐字稿缺字 [▶ 41:39](https://youtu.be/R4_fHzTo0IM?t=2499)：字幕寫「if the final time **and the Hamiltonian** is free」，依上下文應為「final time is free」。

---

## 6. 三種典型問題

[▶ 42:40](https://youtu.be/R4_fHzTo0IM?t=2560) 都用同一個系統——**控制仿射**（control-affine）系統：

$$\dot x=a(x,t)+B(x,t)\,u,\qquad M_i^-\le u_i\le M_i^+,\ i=1,\dots,m$$

- 對 $u$ 是**線性**的；對 $x$ 可以**非線性**（$a$、$B$ 可以是 $x$ 的非線性函數）。
- 很一般，但因為對 $u$ 線性，事情簡化很多。

**共同技巧** [▶ 46:21](https://youtu.be/R4_fHzTo0IM?t=2781)：把 $B$ 寫成行向量 $B=\left[b_1,\dots,b_m\right]$，則 $Bu=\sum_i b_iu_i$，所以

$$p^\top Bu=\sum_{i=1}^m\left(p^\top b_i\right)u_i$$

【Q&A】[▶ 44:43](https://youtu.be/R4_fHzTo0IM?t=2683) 學生問 $i$ 是什麼？答：$u$ 是 $m$ 維，$i$ 是第幾個控制分量。例如可以往不同方向加速，每個方向各有上下界。

### 6.1 最短時間 → bang-bang

[▶ 43:43](https://youtu.be/R4_fHzTo0IM?t=2623) 從任意 $x_0$ 盡快到原點：

$$J=\int_{t_0}^{t_f}1\,dt\quad(=t_f-t_0)$$

**Hamiltonian** [▶ 45:51](https://youtu.be/R4_fHzTo0IM?t=2751)：

$$H=1+p^\top a+\sum_{i=1}^m\left(p^\top b_i\right)u_i$$

**最小化** [▶ 47:28](https://youtu.be/R4_fHzTo0IM?t=2848)：只有最後一項含 $u$。各個 $u_i$ 互相獨立 → 最小化總和 = **各項分別最小化**：

$$u_i^*=\arg\min_{M_i^-\le u_i\le M_i^+}\left(p^\top b_i\right)u_i,\qquad i=1,\dots,m$$

一次函數在區間上的最小值在端點 [▶ 49:13](https://youtu.be/R4_fHzTo0IM?t=2953)：

$$
u_i^*=\begin{cases}
M_i^- & p^{*\top}b_i>0 \\
M_i^+ & p^{*\top}b_i<0 \\
\text{未定} & p^{*\top}b_i=0
\end{cases}
$$

【課堂討論】[▶ 49:46](https://youtu.be/R4_fHzTo0IM?t=2986) 講者問 $p^\top b_i>0$ 時選什麼？學生答負的那邊（下界）。講者問還漏了什麼？學生：0 的情況。

**為什麼叫 bang-bang** [▶ 52:57](https://youtu.be/R4_fHzTo0IM?t=3177)：控制永遠在極端值——要嘛全力加速，要嘛全力煞車。

【口頭】直覺：要最短時間，就「不要拖拖拉拉」，油門踩到底或煞車踩到底。

### 6.2 奇異弧

[▶ 50:46](https://youtu.be/R4_fHzTo0IM?t=3046) $p^\top b_i=0$ 時，PMP **完全沒告訴你**控制長怎樣。這叫**奇異弧**（singular arc）或奇異條件。

- 本課不處理奇異弧。
- 但要知道可能有某段時間 $p^\top b_i\equiv 0$，那段控制就沒被刻畫。
- 要更精密的數學才能處理；線性系統比較容易，非線性系統要看問題。
- 【口頭】[▶ 52:25](https://youtu.be/R4_fHzTo0IM?t=3145) 實際用間接法時，**大部分腦力都花在處理這種病態情況**。

【Q&A】[▶ 53:27](https://youtu.be/R4_fHzTo0IM?t=3207) 學生問：$p^\top b_i=0$ 是不是代表那個狀態不可控？答：不是。只是最佳性條件在那裡不給控制的資訊。

【Q&A】[▶ 53:57](https://youtu.be/R4_fHzTo0IM?t=3237) 學生問奇異弧是哪類問題才有？答：不特定於某類問題，只要用 PMP 都可能遇到。

【Q&A】[▶ 54:29](https://youtu.be/R4_fHzTo0IM?t=3269) 學生問：bang-bang 是從最小化 $H$ 推出來的，還是題目給的？答：推出來的。照食譜：寫 $H$ → 從第三條開始（最小化 $H$）→ 得到形狀。還沒解微分方程就已經知道是 bang-bang。

【口頭】[▶ 56:02](https://youtu.be/R4_fHzTo0IM?t=3362) 想深入奇異弧，推薦上週提的 Kirk 教科書。

> ⚠️ 逐字稿缺字 [▶ 56:32](https://youtu.be/R4_fHzTo0IM?t=3392)：字幕寫「the textbook from **Kurt**」，應為 **Kirk**（課本 §2.2 也引用 Kirk [70]）。

### 6.3 最少燃料 → bang-off-bang

[▶ 57:05](https://youtu.be/R4_fHzTo0IM?t=3425) 同一個系統和界，從 $x_0$ 到原點，**$t_f$ 固定**：

$$J=\int_{t_0}^{t_f}\sum_{i=1}^m c_i\,|u_i(t)|\,dt$$

最小化控制的**絕對值** → **最少燃料**（minimum fuel）問題（航太裡類似最小化推力）。

**Hamiltonian** [▶ 57:38](https://youtu.be/R4_fHzTo0IM?t=3458)：

$$H=\sum_{i=1}^m c_i|u_i|+p^\top a+\sum_{i=1}^m\left(p^\top b_i\right)u_i$$

**逐項最小化** [▶ 59:23](https://youtu.be/R4_fHzTo0IM?t=3563)：

$$\min_{u_i}\ c_i|u_i|+\left(p^\top b_i\right)u_i=\begin{cases}\left(c_i+p^\top b_i\right)u_i & u_i\ge 0\\[2pt] \left(-c_i+p^\top b_i\right)u_i & u_i\le 0\end{cases}$$

**分情況** [▶ 61:06](https://youtu.be/R4_fHzTo0IM?t=3666)（$c_i>0$）：

| 情況 | $u_i\ge 0$ 那支 | $u_i\le 0$ 那支 | $u_i^*$ |
|---|---|---|---|
| $p^\top b_i>c_i$ | 係數 $>0$ → 取 0 | 係數 $>0$ → 取 $M_i^-$（值為負，更小） | $M_i^-$ |
| $0<p^\top b_i<c_i$ | 係數 $>0$ → 取 0 | 係數 $<0$ → 取 0 | $0$ |
| $-c_i<p^\top b_i<0$ | （對稱） | | $0$ |
| $p^\top b_i<-c_i$ | （對稱） | | $M_i^+$ |

$$
u_i^*=\begin{cases}
M_i^- & p^{*\top}b_i>c_i \\
0 & -c_i<p^{*\top}b_i<c_i \\
M_i^+ & p^{*\top}b_i<-c_i
\end{cases}
$$

**為什麼叫 bang-off-bang** [▶ 64:56](https://youtu.be/R4_fHzTo0IM?t=3896)：控制只有「最小值／0／最大值」三種。

【口頭】直覺：盡快進入一個**滑行**（coasting）狀態——什麼都不做讓動態帶著走——最後再一次脈衝控制。這跟「省燃料」的目標相符。

【Q&A】[▶ 66:01](https://youtu.be/R4_fHzTo0IM?t=3961) 學生問第一種情況怎麼推的。答：兩支各自求最小，$u_i\ge0$ 那支在 0，$u_i\le 0$ 那支在 $M_i^-$；兩者比較，$M_i^-$ 那支更小。

【Q&A】[▶ 67:32](https://youtu.be/R4_fHzTo0IM?t=4052) 學生問：這題的奇異弧是不是除了 0，還有 $p^\top b_i=\pm c_i$？答：對，我們假設最佳控制不落在這些情況。

【Q&A】[▶ 67:32](https://youtu.be/R4_fHzTo0IM?t=4052) 學生問：bang-off-bang 有考慮總時間嗎？答：目標沒有明確最小化時間，但時間是**固定**的。

### 6.4 最小能量 → 線性＋飽和

[▶ 68:03](https://youtu.be/R4_fHzTo0IM?t=4083) 跟第 4 節同類，講者快速帶過。成本是 $\frac12\int u^\top Ru\,dt$，$R$ **正定且對角**，所以各分量解耦，逐項最小化，二次函數令導數為 0。

> 以下**不是逐字稿內容**，是依第 4 節的推法寫出的一般式（投影片原式字幕沒唸）：設 $R=\mathrm{diag}(r_1,\dots,r_m)$，逐項最小化 $\frac12r_iu_i^2+(p^\top b_i)u_i$：
> $$\tilde u_i=-\frac{p^{*\top}b_i}{r_i},\qquad u_i^*=\begin{cases}M_i^- & \tilde u_i<M_i^-\\ \tilde u_i & M_i^-\le\tilde u_i\le M_i^+\\ M_i^+ & \tilde u_i>M_i^+\end{cases}$$

形狀：界內線性、界外飽和（第 4 節那張圖）。

【Q&A】[▶ 69:38](https://youtu.be/R4_fHzTo0IM?t=4178) 學生問：為什麼可以選 $R$ 對角？答：$R$ 是我們自己定義成本時挑的，對角讓計算變簡單；但也可以選非對角。

**三種問題比較**：

| 問題 | 成本 | 控制形狀 |
|---|---|---|
| 最短時間 | $\int 1\,dt$ | bang-bang（只有上下界） |
| 最少燃料 | $\int\sum c_i|u_i|\,dt$ | bang-off-bang（上下界或 0） |
| 最小能量 | $\frac12\int u^\top Ru\,dt$ | 線性，超出界就飽和 |

---

## 7. 計算方法：解兩點邊界值問題

[▶ 70:12](https://youtu.be/R4_fHzTo0IM?t=4212) 到目前為止：要嘛解析解（上週），要嘛停在「把 $u$ 寫成 $x,p$ 的函數」。實務上會把它代回微分方程，丟給**數值解法器**。

### 7.1 打靶法與配置法

[▶ 70:44](https://youtu.be/R4_fHzTo0IM?t=4244) 解 TPBVP 的數值方法分兩類：

| 方法 | 做法 |
|---|---|
| **間接打靶法**（indirect shooting） | 把 TPBVP 當成**初值問題**：猜初始值（例如初始協態）→ 往前積分 → 看終點跟終端條件差多少（殘差）→ 反覆修正猜測 |
| **配置法**（collocation） | 用基底函數（例如多項式）近似解，只在一些特定點（**配置點**）強制滿足動態和邊界條件 |

【口頭】不用深究細節。打開解法器的黑盒子，裡面不是打靶就是配置。

【課本補充】課本 §2.2.4 補充兩者的優缺點：

- 打靶法概念簡單，但**數值不穩定**，時間長時尤其嚴重。
- 配置法把 TPBVP 變成一大組非線性代數方程，**比較穩健**，實務上很常用。
- 現成工具：Python `scikits.bvp_solver`、MATLAB `bvp4c`、SciPy `solve_bvp`。

### 7.2 用 solve_bvp

[▶ 72:51](https://youtu.be/R4_fHzTo0IM?t=4371) SciPy 的 `solve_bvp(fun, bc, t, z)`：

| 參數 | 意思 |
|---|---|
| `fun` | 微分方程右邊 $\dot z=g(z,t)$ |
| `bc` | 邊界條件，寫成**殘差**形式（= 0） |
| `t` | 時間網格（mesh），一串遞增的離散時間點 |
| `z` | 初始猜測；$z$ 把狀態和協態疊在一起 |

【課本補充】課本把標準形式寫成 $\dot z=g(z,t)$、$l\left(z(t_0),z(t_f)\right)=0$（式 2.18）。

**例子** [▶ 73:51](https://youtu.be/R4_fHzTo0IM?t=4431)：

$$\dot z_1=z_2,\qquad \dot z_2=-|z_1|,\qquad z_1(0)=0,\quad z_1(4)=-2$$

- 動態：Python 從 0 開始數，所以 `z[1]` 是 $z_2$、`-abs(z[0])` 是 $-|z_1|$。
- 邊界條件 [▶ 74:56](https://youtu.be/R4_fHzTo0IM?t=4496) 寫成殘差：$z_1(0)=0$ 和 $z_1(4)+2=0$。
- 時間網格：0 到 4，5 個點；初始猜測全 0。

**結果** [▶ 76:00](https://youtu.be/R4_fHzTo0IM?t=4560)：$z_1$ 從 0 開始、在 $t=4$ 結束於 $-2$（符合邊界條件）。$z_2$ 是 $z_1$ 的導數：$z_2>0$ 時 $z_1$ 上升，$z_2<0$ 時 $z_1$ 下降——目視檢查確實解對了。

【課本補充】課本 Algorithm 5 用同樣的邊界條件，但動態是 $\dot z_2=-z_1$（沒有絕對值）。

【Q&A】[▶ 76:35](https://youtu.be/R4_fHzTo0IM?t=4595) 學生問 $z_2$ 有沒有限制？答：這題沒有。$\dot z_2=-|z_1|\le 0$，所以 $z_2$ 一直在減少，圖上也看得到。它的起點和終點值都不受約束。

[▶ 72:17](https://youtu.be/R4_fHzTo0IM?t=4337) 講者預告：會用 `solve_bvp` 解上一集的雙積分器（質點在直線上）那題，下次（週三）收尾。

### 7.3 PMP 整理：在解什麼／步驟／什麼時候會失敗

**在解什麼**：控制**有界**（$u\in\mathcal U$）的連續時間最佳控制問題。PMP 給出最佳解必須滿足的必要條件。

**步驟**：

```
1. 化成一階形式 ẋ = f(x,u,t)
2. 寫 H = g + pᵀf
3. 對 u 最小化 H（固定 x、p）：u*(x,p,t) = argmin_{u∈U} H
   - 常用技巧：控制仿射＋獨立的界 → 各分量分開最小化
   - 一次函數 → 取端點（bang-bang）；二次函數 → 頂點再截斷（飽和）
4. 代回 ẋ = ∂H/∂p、ṗ = −∂H/∂x
5. 依 t_f、x(t_f) 查表補終端邊界條件（必要時加 PMP 額外條件）
6. 把狀態＋協態疊成 z，寫成 ż = g(z,t)、l(z(t₀),z(t_f)) = 0
7. 用 TPBVP 解法器（打靶或配置，例如 solve_bvp）
```

**什麼時候會失敗**：

| 情況 | 會怎樣 | 來源 |
|---|---|---|
| 奇異弧（$p^\top b_i\equiv 0$ 一段時間） | PMP 不給控制資訊，要更精密的分析 | 6.2 |
| 有狀態約束（例如避障） | 數學複雜很多；間接法不是首選 | 第 2 節 |
| 打靶法、時間長 | 數值不穩定 | 課本 §2.2.4 |
| 初始猜測差 | 解法器可能不收斂（`solve_bvp` 需要猜測） | 7.2 |
| 只是必要條件 | 得到候選解，不保證最優 | 上一集 |

---

## 8. 一頁速查表

### PMP

$$H=g+p^\top f,\qquad \dot x^*=\frac{\partial H}{\partial p},\qquad \dot p^*=-\frac{\partial H}{\partial x},\qquad u^*=\arg\min_{u\in\mathcal U}H(x^*,u,p^*,t)$$

- 關鍵一步：控制貼在界上時，變分只能單邊 → $\delta J\ge 0$ 而非 $=0$ → 加強成「全域最小化 $H$」。
- 界很鬆時 → 最小值是駐點 → 退化成 $\partial H/\partial u=0$。
- 額外條件：$H$ 不顯含 $t$ 時，$t_f$ 固定 → $H$ 為常數；$t_f$ 自由 → $H\equiv 0$。

### 控制仿射系統 $\dot x=a+\sum_i b_iu_i$，$M_i^-\le u_i\le M_i^+$

| 問題 | 成本 | $u_i^*$ |
|---|---|---|
| 最短時間 | $\int 1$ | $p^\top b_i>0\to M_i^-$；$<0\to M_i^+$（bang-bang） |
| 最少燃料（$t_f$ 固定） | $\int\sum c_i|u_i|$ | $p^\top b_i>c_i\to M_i^-$；$|p^\top b_i|<c_i\to 0$；$<-c_i\to M_i^+$（bang-off-bang） |
| 最小能量 | $\frac12\int u^\top Ru$，$R$ 對角 | $-p^\top b_i/r_i$ 截斷到 $[M_i^-,M_i^+]$（飽和） |
| 奇異弧 | — | 切換函數 $=0$（或 $=\pm c_i$）時未定 |

### 第 4 節例子

$\dot x_1=x_2$，$\dot x_2=-x_2+u$，$|u|\le 1$，$J=\frac12\int(x_1^2+u^2)$：
$u^*=\mathrm{sat}(-p_2)$，即 $-p_2$ 截斷到 $[-1,1]$。

### TPBVP 數值解

| | 打靶法 | 配置法 |
|---|---|---|
| 想法 | 猜初值 → 積分 → 修正 | 基底函數 + 配置點 → 代數方程組 |
| 優點 | 簡單 | 穩健 |
| 缺點 | 長時間不穩定 | 方程組大 |

`solve_bvp(fun, bc, t_mesh, z_guess)`：`bc` 寫成殘差 = 0。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 間接法收尾、計算方法 | 第 6 集：用 `solve_bvp` 解雙積分器（講者預告），然後直接法 |
| 配置法 | 第 6 集直接法（直接配置法，待確認） |
| 狀態約束交給運動規劃 | 課本第 4 章運動規劃（本課不講） |
| 二次成本、線性飽和 | 第 8 集 LQR（無界時的線性回饋） |
| bang-bang、最短時間 | 第 10 集可達性分析（最短時間到達，待確認） |

---

## 附：本集一句話總結

> **控制有界時，貼在界上的控制只能單邊變分，所以「$\partial H/\partial u=0$」要加強成「$u^*$ 全域最小化 $H$」（Pontryagin 最小原理）。對控制仿射系統，光看 $H$ 對 $u$ 的形狀就知道答案：最短時間是 bang-bang、最少燃料是 bang-off-bang、最小能量是線性加飽和；剩下的兩點邊界值問題交給打靶法或配置法。**

---

## ⚠️ 待確認清單

1. 上課日期待補（第 3 週週一）。
2. [▶ 24:02](https://youtu.be/R4_fHzTo0IM?t=1442) 第 4 節例子的系統方程是由 Hamiltonian 展開式反推的，待對照投影片。
3. [▶ 68:03](https://youtu.be/R4_fHzTo0IM?t=4083) 最小能量一般式（含 $r_i$）是推論的，待對照投影片。

---

*筆記依據 Daniele Gammelli「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 5 錄影逐字稿（人工字幕，1:18:04）與《Principles of Robot Autonomy》§2.2.3–2.2.4 整理。*
