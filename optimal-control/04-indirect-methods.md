---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 4
lecture: Lecture 4
date: 待補（週三）
video: https://youtu.be/7rejaoMWviw
notes: 《Principles of Robot Autonomy》§2.2.3（書頁 64–65，PDF 頁 66–67）
---

# 第 4 集 · Lecture 4：間接法（Indirect Methods） [▶ 影片](https://youtu.be/7rejaoMWviw)

← 上一集：[03-calculus-of-variations](03-calculus-of-variations.md) ｜ [總目錄](README.md) ｜ 下一集：[05-computational-methods](05-computational-methods.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 4 集
> **講者**：Daniele Gammelli（本集沒有自我介紹；依開場接續上一集、以及「last Monday」的說法推斷）
> **來源**：YouTube 錄影逐字稿（1:24:49，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§2.2.3
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
- [1. 再看 Euler 方程：兩端邊界值問題](#1-再看-euler-方程兩端邊界值問題)
- [2. 例子：兩點之間最短的路是直線](#2-例子兩點之間最短的路是直線)
- [3. 推廣一：終點或終端時間自由](#3-推廣一終點或終端時間自由)
  - [3.1 邊界條件方程](#31-邊界條件方程)
  - [3.2 例子：到直線 t = 5 的最短曲線](#32-例子到直線-t--5-的最短曲線)
- [4. 推廣二：微分約束與協態](#4-推廣二微分約束與協態)
- [5. 最佳控制的必要條件（控制無界）](#5-最佳控制的必要條件控制無界)
  - [5.1 問題](#51-問題)
  - [5.2 Hamiltonian 與三組條件](#52-hamiltonian-與三組條件)
  - [5.3 邊界條件與「要幾條」](#53-邊界條件與要幾條)
  - [5.4 間接法整理：在解什麼／步驟／什麼時候會失敗](#54-間接法整理在解什麼步驟什麼時候會失敗)
- [6. 例子：雙積分器，兼顧力氣和時間](#6-例子雙積分器兼顧力氣和時間)
- [7. 證明草稿：條件從哪來](#7-證明草稿條件從哪來)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/7rejaoMWviw?t=5) 課程地圖：還在「開迴路 → 間接法」。今天和下週一講間接法，下週三開始直接法，之後才到閉迴路。

**上一集回顧** [▶ 01:40](https://youtu.be/7rejaoMWviw?t=100)：

- 變分法基本定理：$x^*$ 是極值 ⟹ $\delta J(x^*,\delta x)=0$（類比有限維 $\nabla f^\top\Delta x=0$）。它重要，但**不能直接算**。
- 對簡化問題 $J=\int g(x,\dot x,t)\,dt$（端點固定）推出可計算的 **Euler 方程**（類比 $\nabla f=0$）。

今天：

| 主題 | 課本 |
|---|---|
| Euler 方程的性質、最短路徑例子 | 課本沒有 |
| 端點自由的邊界條件 | 課本沒有（變分法版本） |
| 微分約束、協態 | §2.2.3（協態類比 Lagrange 乘數） |
| 最佳控制必要條件（控制無界）＋邊界條件表 | §2.2.3（課本直接寫 PMP 的版本） |
| 雙積分器例子、證明草稿 | 課本沒有 |

---

## 1. 再看 Euler 方程：兩端邊界值問題

[▶ 04:11](https://youtu.be/7rejaoMWviw?t=251)

$$g_x\left(x^*,\dot x^*,t\right)-\frac{d}{dt}g_{\dot x}\left(x^*,\dot x^*,t\right)=0$$

- 它是**非線性常微分方程**，而且是**二階**的：$g_{\dot x}$ 本身含 $\dot x$，再對時間微分一次就出現 $\ddot x$。
- 它的邊界條件是**分開的**（split boundary conditions）[▶ 05:16](https://youtu.be/7rejaoMWviw?t=316)：一個在 $t_0$，一個在 $t_f$。

一般熟悉的 ODE 是 **Cauchy 問題**（初值問題）：所有條件都在起點（例如 $t=0$）。這裡條件「一半在頭、一半在尾」，叫**兩點邊界值問題**（two-point boundary value problem，TPBVP），比較難搞。

【Q&A】[▶ 05:46](https://youtu.be/7rejaoMWviw?t=346) 學生問：為什麼式子裡是 $\dot x$ 而不是控制序列？答：這是簡化問題，假設我們**直接控制狀態軌跡**。等一下會放寬，變成真正的最佳控制問題。

---

## 2. 例子：兩點之間最短的路是直線

[▶ 06:48](https://youtu.be/7rejaoMWviw?t=408) 在 $(t,x)$ 平面上，從 $(t_0,x_0)$ 到 $(t_f,x_f)$，找最短的曲線。

【口頭】「證明出它是直線，會讓我們很有成就感。」

**Step 1：寫出泛函** [▶ 07:58](https://youtu.be/7rejaoMWviw?t=478)

曲線長度 = 把小段弧長 $ds$ 積分起來。小段很短時用畢氏定理：

$$ds^2\approx dt^2+dx^2\ \Rightarrow\ ds=\sqrt{dt^2+dx^2}=dt\sqrt{1+\left(\frac{dx}{dt}\right)^2}=\sqrt{1+\dot x^2}\,dt$$

【口頭】「假設教室裡沒有數學家」——直接把 $dx/dt$ 寫成 $\dot x$。

$$J(x)=\int_{t_0}^{t_f}\sqrt{1+\dot x(t)^2}\,dt,\qquad g(x,\dot x)=\sqrt{1+\dot x^2}$$

**Step 2：算偏導數** [▶ 10:10](https://youtu.be/7rejaoMWviw?t=610)

- $g$ 不含 $x$ → $g_x=0$
- $g_{\dot x}=\dfrac12\left(1+\dot x^2\right)^{-1/2}\cdot 2\dot x=\dot x\left(1+\dot x^2\right)^{-1/2}$

**Step 3：算 $\frac{d}{dt}g_{\dot x}$** [▶ 11:47](https://youtu.be/7rejaoMWviw?t=707)（乘積法則＋鏈鎖法則）

$$
\begin{aligned}
\frac{d}{dt}g_{\dot x}&=\ddot x\left(1+\dot x^2\right)^{-1/2}+\dot x\cdot\left(-\frac12\right)\left(1+\dot x^2\right)^{-3/2}\cdot 2\dot x\ddot x \\
&=\frac{\ddot x}{\left(1+\dot x^2\right)^{1/2}}-\frac{\dot x^2\ddot x}{\left(1+\dot x^2\right)^{3/2}} \\
&=\frac{\ddot x\left(1+\dot x^2\right)-\dot x^2\ddot x}{\left(1+\dot x^2\right)^{3/2}}=\frac{\ddot x}{\left(1+\dot x^2\right)^{3/2}}
\end{aligned}
$$

**Step 4：Euler 方程** [▶ 14:05](https://youtu.be/7rejaoMWviw?t=845)

$$0-\frac{\ddot x}{\left(1+\dot x^2\right)^{3/2}}=0$$

分母永遠是正的，所以只能 $\ddot x=0$。邊界條件：$x(t_0)=x_0$、$x(t_f)=x_f$。

**Step 5：解** 【課堂討論】[▶ 15:14](https://youtu.be/7rejaoMWviw?t=914) 講者問 $\ddot x=0$ 積分出來是什麼？學生：直線。

$$x(t)=c_1t+c_2$$

二階 ODE 要兩個積分常數，正好用兩個邊界條件定出來。

**注意** [▶ 16:16](https://youtu.be/7rejaoMWviw?t=976)：嚴格說，我們只證明了直線是**最佳候選人**（必要條件）。要證明它真的是最小值，還要做二階論證。

---

## 3. 推廣一：終點或終端時間自由

### 3.1 邊界條件方程

[▶ 17:46](https://youtu.be/7rejaoMWviw?t=1066) 設定一樣，但：

- $x:\mathbb{R}\to\mathbb{R}^n$（向量函數，沒差別）。
- $g$ 二次可微。
- $t_0$、$x(t_0)$ **固定**。
- $t_f$、$x(t_f)$ **可能固定，也可能自由**。

**問題** [▶ 18:49](https://youtu.be/7rejaoMWviw?t=1129)：Euler 方程**仍然成立**，但少了邊界條件，定不出積分常數。

**解法**：用一條更精緻的邊界條件方程。字幕沒唸出式子，以下依講者描述（含 $\delta x_f$ 和 $\delta t_f$ 兩項，且「$t_f$ 固定、$x_f$ 自由」時剩下 $g_{\dot x}(t_f)=0$）寫出標準形式：

> 以下**不是逐字稿內容**，是依講者描述和標準教科書（Kirk）寫出的式子：
> $$g_{\dot x}\left(x^*(t_f),\dot x^*(t_f),t_f\right)^\top\delta x_f+\left[g\left(x^*(t_f),\dot x^*(t_f),t_f\right)-g_{\dot x}\left(\cdot\right)^\top\dot x^*(t_f)\right]\delta t_f=0$$

**怎麼用** [▶ 20:19](https://youtu.be/7rejaoMWviw?t=1219)：把 $\delta x_f$、$\delta t_f$「代換」成實際情況：

- 某個量**固定** → 它唯一可容許的變分是 0 → 那一項消失。
- 某個量**自由** → 它的變分任意 → 它的**係數**必須是 0。

**常見情況表** [▶ 21:22](https://youtu.be/7rejaoMWviw?t=1282)（投影片上的表，字幕只講了前兩列）：

| $t_f$ | $x(t_f)$ | 額外邊界條件 |
|---|---|---|
| 固定 | 固定 | $x(t_f)=x_f$（上一集和第 2 節的情況） |
| 固定 | **自由** | $g_{\dot x}(t_f)=0$ |
| 自由 | 固定 | （依上式）$g-g_{\dot x}^\top\dot x=0$ 在 $t_f$ |
| 自由 | 自由 | 兩個係數都 = 0 |

（後兩列不是逐字稿內容，是依上式代換推論的。）

【口頭】講者說今天大多只**陳述結果**，證明跟上一集的推導很像，不太有啟發性。

【Q&A】[▶ 23:33](https://youtu.be/7rejaoMWviw?t=1413) 學生問：為什麼表裡初始時間總是固定？答：最佳控制問題裡，你通常知道現在在哪、現在幾點。就算不是，也能平移問題，讓起點變成時間 0、狀態給定。

### 3.2 例子：到直線 t = 5 的最短曲線

[▶ 25:06](https://youtu.be/7rejaoMWviw?t=1506) 從 $x(0)=1$ 出發，到**直線 $t=5$ 上任一點**，最短的平滑曲線？

- $t_f=5$ **固定**，$x(t_f)$ **自由**。
- 直覺：水平線最短。

**Step 1**：成本和第 2 節一樣，Euler 方程一樣 → $x(t)=c_1t+c_2$。

**Step 2：用初始條件** [▶ 26:43](https://youtu.be/7rejaoMWviw?t=1603)：$x(0)=c_2=1$。

**Step 3：用表** [▶ 27:20](https://youtu.be/7rejaoMWviw?t=1640)：$t_f$ 固定、$x(t_f)$ 自由 → $g_{\dot x}(t_f)=0$：

$$\frac{\dot x(t_f)}{\sqrt{1+\dot x(t_f)^2}}=0\ \Rightarrow\ \dot x(t_f)=0$$

**Step 4** [▶ 29:12](https://youtu.be/7rejaoMWviw?t=1752)：$x(t)=c_1t+1$ → $\dot x(t)=c_1$ → $c_1=\dot x(t_f)=0$。

$$x(t)=1$$

水平線，符合直覺。

**多維** [▶ 31:01](https://youtu.be/7rejaoMWviw?t=1861)：函數是向量值時，Euler 方程和邊界條件**逐分量**套用。

【Q&A】[▶ 31:37](https://youtu.be/7rejaoMWviw?t=1897) 學生問：為什麼是 $x(t)=1$ 而不是「某個常數」？答：因為 $c_2$ 已經被初始條件定成 1，$c_1$ 被邊界條件定成 0。

---

## 4. 推廣二：微分約束與協態

[▶ 32:40](https://youtu.be/7rejaoMWviw?t=1960) 現在加入「把函數和它的導數綁在一起」的約束。

設 $w:\mathbb{R}\to\mathbb{R}^{n+m}$，要找極值 $w^*$，泛函 $J(w)=\int g(w,\dot w,t)\,dt$，約束有 $n$ 條：

$$f_i(w,\dot w,t)=0,\qquad i=1,\dots,n$$

只有 $m$ 個分量是獨立的。

**解讀** [▶ 33:45](https://youtu.be/7rejaoMWviw?t=2025)：$w$ 是「狀態（$n$ 維）＋控制（$m$ 維）」接在一起；約束就是**系統動態**，把 $m$ 個自由的控制和 $n$ 個狀態綁在一起。

【Q&A】[▶ 33:45](https://youtu.be/7rejaoMWviw?t=2025) 學生確認：原本 $x$ 是純量，現在改叫 $w$ 而且是向量，再加上這種約束？答：對。唯一新增的是這種約束。

**處理方式：跟有限維一樣** [▶ 34:47](https://youtu.be/7rejaoMWviw?t=2087)

有限維時：把約束乘上 Lagrange 乘數 $\lambda$ 加進目標函數，當成無約束問題。

這裡一樣，定義**增廣被積函數**（augmented integrand）：

$$g_a(w,\dot w,p,t)=g(w,\dot w,t)+p(t)^\top\left[f(w,\dot w,t)\right]$$

- $p(t)$ 是 Lagrange 乘數的類比，但它是**時間的函數**，不只是一個向量。
- 文獻叫它**協態**（costate）[▶ 35:52](https://youtu.be/7rejaoMWviw?t=2152)：每個狀態配一個協態函數，所以叫「co-state」。

**必要條件** [▶ 36:55](https://youtu.be/7rejaoMWviw?t=2215)：

1. 對 $g_a$ 套用 Euler 方程。
2. 約束本身要滿足（最優點一定可行）。

跟有限維「$\nabla_x L=0$、$\nabla_\lambda L=0$」完全對應。

【課本補充】課本 §2.2.3 旁註 9：「協態」這個名字強調每個狀態變數都有一個協態，類比有限維最佳化的 Lagrange 乘數。

---

## 5. 最佳控制的必要條件（控制無界）

[▶ 38:02](https://youtu.be/7rejaoMWviw?t=2282) 接下來的計畫：

1. **今天**：控制**無界**（沒有最大推力之類的限制）時的必要條件。
2. **下週一**：**Pontryagin 最小原理**（Pontryagin's Minimum Principle，PMP），推廣到控制**有界**。
3. 套到已知的例子，推出像 **bang-bang 控制**這種已知策略。
4. 解這些微分方程的**數值方法**。

[▶ 39:04](https://youtu.be/7rejaoMWviw?t=2344) 實務上：用必要條件推出微分方程和邊界條件 → 丟給**數值解法器** → 解出來。這就是「先最佳化、再離散化」的意思（離散化發生在解法器裡）。

### 5.1 問題

[▶ 40:06](https://youtu.be/7rejaoMWviw?t=2406)

$$
\begin{aligned}
\min_{u}\quad & J(u)=h\left(x(t_f),t_f\right)+\int_{t_0}^{t_f}g\left(x(t),u(t),t\right)dt \\
\text{s.t.}\quad & \dot x(t)=f\left(x(t),u(t),t\right),\quad x(t_0)=x_0\ \text{（$t_0$、$x_0$ 固定）}
\end{aligned}
$$

- $g$：運行成本，例如 $u^2$（不要猛踩油門）。
- $h$：終端成本，例如確保打到目標。
- **$J$ 只是 $u$ 的函數** [▶ 41:07](https://youtu.be/7rejaoMWviw?t=2467)：$u$ 是自由變數；對應的 $x$ 由動態隱含決定。

### 5.2 Hamiltonian 與三組條件

[▶ 42:11](https://youtu.be/7rejaoMWviw?t=2531) 講者分三步：陳述 → 例子 → 證明草稿。

**Hamiltonian**（把動態約束用協態加進成本）：

$$H\left(x,u,p,t\right)=g\left(x,u,t\right)+p^\top f\left(x,u,t\right)$$

**必要條件**：最優的 $(x^*,u^*,p^*)$ 要滿足

$$
\begin{aligned}
\dot x^*(t)&=\frac{\partial H}{\partial p}\left(x^*,u^*,p^*,t\right) &&\text{（$n$ 條 ODE）}\\
\dot p^*(t)&=-\frac{\partial H}{\partial x}\left(x^*,u^*,p^*,t\right) &&\text{（$n$ 條 ODE）}\\
0&=\frac{\partial H}{\partial u}\left(x^*,u^*,p^*,t\right) &&\text{（$m$ 條代數方程）}
\end{aligned}
$$

**第一條很直觀** [▶ 43:14](https://youtu.be/7rejaoMWviw?t=2594)：$H$ 對 $p$ 微分只剩 $f$，所以它就是「**要滿足動態**」。第二、三條比較不直觀，第 7 節推。

**實際用法** [▶ 43:44](https://youtu.be/7rejaoMWviw?t=2624)：

1. 寫出 $H$。
2. 寫出三組條件。
3. 用第三條（代數方程）把 $u$ 表示成 $x$、$p$ 的函數。
4. 代進前兩條 ODE。
5. 用邊界條件定積分常數。

【Q&A】[▶ 44:18](https://youtu.be/7rejaoMWviw?t=2658) 學生問協態 $p$ 是什麼。答：有限維時處理約束的方法是把約束乘上 Lagrange 乘數加進成本，當成無約束。協態在連續時間扮演**完全相同的角色**。

【Q&A】[▶ 49:34](https://youtu.be/7rejaoMWviw?t=2974) 學生問 $H$ 跟剛才的 $g_a$ 差在哪。答：直覺上一樣，都是把約束加進目標並懲罰。$g_a$ 是簡化情況的寫法，$H$ 是一般情況的正式寫法。另一位學生問 $H$ 是不是之前的 Lagrangian？答：可以理解成它的類比。

【Q&A】[▶ 48:32](https://youtu.be/7rejaoMWviw?t=2912) 學生說記號一直變很亂。答：之前把變分法當成獨立的數學工具，用 $x$ 或 $w$；現在跳到最佳控制，記號改成動態 $f$、狀態 $x$、控制 $u$。差別是：以前直接控制 $x$；現在控制 $u$，再**透過** $u$ 控制 $x$。

### 5.3 邊界條件與「要幾條」

**邊界條件方程**（投影片上的式子，字幕沒唸出；課本式 2.17 為同一式）：

$$\left[\frac{\partial h}{\partial x}\left(x^*(t_f),t_f\right)-p^*(t_f)\right]^\top\delta x_f+\left[H\left(x^*(t_f),u^*(t_f),p^*(t_f),t_f\right)+\frac{\partial h}{\partial t}\left(x^*(t_f),t_f\right)\right]\delta t_f=0$$

用法跟 3.1 一樣：固定的那一項消失，自由的那一項係數 = 0。

【課本補充】課本 §2.2.3 列出四種情況：

| $t_f$ | $x(t_f)$ | 邊界條件 |
|---|---|---|
| 固定 | 固定 | $x^*(t_f)=x_f$ |
| 固定 | 自由 | $\dfrac{\partial h}{\partial x}\left(x^*(t_f),t_f\right)-p^*(t_f)=0$ |
| 自由 | 固定 | $H\left(\cdot\right)\big|_{t_f}+\dfrac{\partial h}{\partial t}\left(x^*(t_f),t_f\right)=0$ |
| 自由 | 自由 | 兩個都要（$n$ 條＋1 條） |

**數一數** [▶ 51:10](https://youtu.be/7rejaoMWviw?t=3070)：

- $2n$ 條一階 ODE（$x$ 和 $p$）→ $2n$ 個積分常數 → 要 $2n$ 個邊界條件。
- $n$ 個來自初始條件 $x(t_0)=x_0$，另外 $n$ 個來自終端。
- 【課堂討論】[▶ 52:10](https://youtu.be/7rejaoMWviw?t=3130) 講者問：什麼時候要 $2n+1$ 個？答案（講者自己說）：$t_f$ **自由**時，多一個未知數 $t_f$ 要定。

【課本補充】課本：$2n$ 個 ODE ＋ $m$ 條代數方程；一半常數由 $x(t_0)$ 定，其餘 $n$（或 $t_f$ 自由時 $n+1$）由式 (2.17) 定。這是 TPBVP，特殊情況可解析解，一般用打靶法（shooting）或配置法（collocation）數值解。

### 5.4 間接法整理：在解什麼／步驟／什麼時候會失敗

**在解什麼**：連續時間最佳控制問題（控制無界）。間接法不直接搜尋 $u(t)$，而是先推出最優解必須滿足的**必要條件**（一組微分方程＋邊界條件），再解它。

**步驟**：

```
1. 高階動態 → 化成一階形式 ẋ = f(x,u,t)
2. 寫 Hamiltonian H = g + pᵀf（每個狀態一個協態）
3. 寫條件：ẋ = ∂H/∂p，ṗ = −∂H/∂x，0 = ∂H/∂u
4. 由 0 = ∂H/∂u 解出 u = u(x,p,t)，代回前兩組 ODE
5. 依 t_f、x(t_f) 固定或自由，查表得終端邊界條件
6. 解兩點邊界值問題（解析或丟給數值解法器）
7. 得到 x*, p*, u*（以及 t_f）
```

**什麼時候會失敗**：

| 情況 | 會怎樣 | 來源 |
|---|---|---|
| 只是必要條件 | 解出來的是**候選**，不保證最小；要再做二階論證或比較 | 第 2 節 |
| 邊界條件分在兩端 | 不是初值問題，數值上難解；解法器可能不收斂（講者：「祈禱解法器收斂」） | 第 1 節、第 6 節 |
| 控制有界（例如最大推力） | $\partial H/\partial u=0$ 不再適用 → 要用下一集的 PMP | 第 5 節 |
| 高階動態沒先化成一階 | 公式不能直接套 | 第 6 節 |

---

## 6. 例子：雙積分器，兼顧力氣和時間

[▶ 53:21](https://youtu.be/7rejaoMWviw?t=3201) 直線上的質點（質量 1），直接控制加速度：$\ddot x=u$。

- 起點：$x(0)=10$，$\dot x(0)=0$（在 10，靜止）。
- 終點：$x(t_f)=0$，$\dot x(t_f)=0$（到原點，靜止）。
- **$t_f$ 自由**。
- 成本 [▶ 54:55](https://youtu.be/7rejaoMWviw?t=3295)：
$$J=\frac12\alpha t_f^2+\frac12\int_0^{t_f}b\,u(t)^2\,dt$$
  - $\frac12 b\int u^2$：控制力氣。$b$ 大 → 比較小心地加速。
  - $\frac12\alpha t_f^2$：懲罰花太久。$\alpha$ 大 → 快速到達，即使多花力氣。

【Q&A】[▶ 56:33](https://youtu.be/7rejaoMWviw?t=3393) 學生問：$\frac12$ 和平方是固定這樣寫嗎？答：只是一種選擇。

【課本補充】這題就是課本 Example 2.2.1（書頁 67，出處 How [54] Example 6.1），課本把權重 $b$ 寫成 $\beta$。課本的做法是把它化成標準 TPBVP 形式，丟給 Python 的 `solve_bvp` 數值解。

【口頭】[▶ 56:33](https://youtu.be/7rejaoMWviw?t=3393) 為什麼這個例子有意思：它有真實問題的很多特徵（權衡力氣和時間、$t_f$ 自由要最佳化）。幾週前你可能不知道從哪開始，現在有一般方法了。

**Step 1：化成一階** [▶ 58:06](https://youtu.be/7rejaoMWviw?t=3486)

$$\dot x_1=x_2,\qquad \dot x_2=u\qquad\Rightarrow\qquad f=\begin{pmatrix}x_2\\u\end{pmatrix}$$

**Step 2：Hamiltonian** [▶ 59:10](https://youtu.be/7rejaoMWviw?t=3550)（兩個狀態 → 兩個協態 $p_1,p_2$）

$$H=\frac12 b u^2+p_1x_2+p_2u$$

**Step 3：條件** [▶ 61:28](https://youtu.be/7rejaoMWviw?t=3688)

- 狀態：$\dot x_1=x_2$，$\dot x_2=u$（就是動態）。
- 協態 [▶ 62:33](https://youtu.be/7rejaoMWviw?t=3753)：$\dot p_1=-\dfrac{\partial H}{\partial x_1}=0$，$\dot p_2=-\dfrac{\partial H}{\partial x_2}=-p_1$。
- 控制 [▶ 63:34](https://youtu.be/7rejaoMWviw?t=3814)：$\dfrac{\partial H}{\partial u}=bu+p_2=0\ \Rightarrow\ u=-\dfrac{p_2}{b}$。

【口頭】[▶ 64:46](https://youtu.be/7rejaoMWviw?t=3886) 一般做到這裡就停了：把條件和邊界條件丟給解法器，祈禱它收斂。為了練習，下面解析地解。

**Step 4：一路積分** [▶ 65:30](https://youtu.be/7rejaoMWviw?t=3930)

$$
\begin{aligned}
p_1&=c_1 \\
p_2&=-c_1t+c_2 \\
\dot x_2&=-\frac{p_2}{b}=\frac{1}{b}\left(c_1t-c_2\right)\ \Rightarrow\ x_2=\frac1b\left(\frac{c_1}{2}t^2-c_2t\right)+c_3 \\
\dot x_1&=x_2\ \Rightarrow\ x_1=\frac1b\left(\frac{c_1}{6}t^3-\frac{c_2}{2}t^2\right)+c_3t+c_4
\end{aligned}
$$

[▶ 67:54](https://youtu.be/7rejaoMWviw?t=4074) 講者先用 $x_2(0)=0$ 得 $c_3=0$，省得一直帶著它。

> ⚠️ 逐字稿缺字 [▶ 75:26](https://youtu.be/7rejaoMWviw?t=4526)：板書 $x_1$ 裡 $c_2$ 那項一開始少了 $\frac12$，學生指出後講者更正為 $\frac{c_2}{2}t^2$（上式已是更正後）。

**Step 5：五個未知數、五個條件** [▶ 70:07](https://youtu.be/7rejaoMWviw?t=4207)

未知：$c_1,c_2,c_3,c_4,t_f$。條件：

1. $x_1(0)=10$
2. $x_2(0)=0$
3. $x_1(t_f)=0$
4. $x_2(t_f)=0$
5. 第五條查表 [▶ 70:42](https://youtu.be/7rejaoMWviw?t=4242)：$x(t_f)$ 固定、$t_f$ 自由 → $H\big|_{t_f}+\dfrac{\partial h}{\partial t}\Big|_{t_f}=0$

**算第五條** [▶ 72:13](https://youtu.be/7rejaoMWviw?t=4333)：

$$H\big|_{t_f}=\frac12 b\,u(t_f)^2+p_1(t_f)\underbrace{x_2(t_f)}_{=0}+\underbrace{p_2(t_f)}_{=-b\,u(t_f)}u(t_f)=-\frac12 b\,u(t_f)^2$$

（$p_2=-bu$ 來自控制條件 $u=-p_2/b$。）

$h=\frac12\alpha t_f^2$ → $\dfrac{\partial h}{\partial t}\Big|_{t_f}=\alpha t_f$。所以

$$-\frac12 b\,u(t_f)^2+\alpha t_f=0$$

> ⚠️ 逐字稿缺字 [▶ 74:51](https://youtu.be/7rejaoMWviw?t=4491)：字幕寫「1 over 2 bu squared tf **plus** alpha tf must be equal to 0」，少了負號。依前一步 $H|_{t_f}=-\frac12 bu(t_f)^2$，應為 $-\frac12 bu(t_f)^2+\alpha t_f=0$。

**結果** [▶ 76:26](https://youtu.be/7rejaoMWviw?t=4586)：講者直接給出

$$t_f=\left(\frac{1800\,b}{\alpha}\right)^{1/5}$$

> 以下**不是逐字稿內容**，是補上的中間計算（講者跳過），用來驗證這個結果：
>
> 1. $x_1(0)=c_4=10$。
> 2. $x_2(t_f)=0$：$\dfrac{c_1}{2}t_f^2=c_2t_f\Rightarrow c_2=\dfrac{c_1t_f}{2}$。
> 3. $x_1(t_f)=0$：$\dfrac1b\left(\dfrac{c_1}{6}-\dfrac{c_1}{4}\right)t_f^3+10=0\Rightarrow -\dfrac{c_1t_f^3}{12b}=-10\Rightarrow c_1=\dfrac{120b}{t_f^3}$，$c_2=\dfrac{60b}{t_f^2}$。
> 4. $u(t)=\dfrac{c_1t-c_2}{b}=\dfrac{120t}{t_f^3}-\dfrac{60}{t_f^2}$，所以 $u(t_f)=\dfrac{60}{t_f^2}$。（$u$ 是時間的一次函數：先正後負，先加速再減速。）
> 5. 代入第五條：$\dfrac12 b\cdot\dfrac{3600}{t_f^4}=\alpha t_f\Rightarrow t_f^5=\dfrac{1800\,b}{\alpha}$ ✓

**直覺檢查** [▶ 76:58](https://youtu.be/7rejaoMWviw?t=4618)：

- $b$ 大（重視省力）→ $t_f$ 大 → 走慢一點。
- $\alpha$ 大（重視時間）→ $t_f$ 小 → 走快一點。

【Q&A】[▶ 78:03](https://youtu.be/7rejaoMWviw?t=4683) 學生問：$t_f$ 的式子裡還有 $u$，最後怎麼解？答：解法器會一起給你所有的 $(x,u,p)$。（字幕不清楚；上面補的計算顯示 $u(t_f)$ 本身可以寫成 $t_f$ 的函數，所以最後只剩 $t_f$ 一個未知數。）

【Q&A】[▶ 77:32](https://youtu.be/7rejaoMWviw?t=4652) 學生問：邊界條件表有直覺嗎，還是背起來就好？答：剛好接到下一頁（證明草稿）。

---

## 7. 證明草稿：條件從哪來

[▶ 78:34](https://youtu.be/7rejaoMWviw?t=4714) 回顧 Euler 方程的推法：從增量取線性部分（變分），再利用「$\delta x$ 可以任意選」推出被積函數 = 0。

**麻煩** [▶ 79:04](https://youtu.be/7rejaoMWviw?t=4744)：現在 $\delta x$ 和 $\delta u$ 透過動態**綁在一起**，不能各自任意變。

**簡化設定** [▶ 79:38](https://youtu.be/7rejaoMWviw?t=4778)：$h=0$，$t_f$ 和 $x(t_f)$ 固定。

**技巧：加 0** [▶ 80:10](https://youtu.be/7rejaoMWviw?t=4810)：

$$g_a\left(x,\dot x,u,p,t\right)=g\left(x,u,t\right)+p^\top\left[f\left(x,u,t\right)-\dot x\right]$$

最優點一定可行，所以 $f-\dot x=0$——等於加了 0。但這引入了協態 $p$，之後可以**聰明地選** $p$ 來簡化分析。

**變分** [▶ 81:15](https://youtu.be/7rejaoMWviw?t=4875)：照 Euler 方程的推法（泰勒展開＋分部積分消掉 $\delta\dot x$），$\delta J=0$ 變成

> 以下式子**不是逐字稿內容**：投影片上的式子字幕沒唸，講者只逐項說明；這是依說明寫出的形式。
> $$\int_{t_0}^{t_f}\left[\left(\frac{\partial g_a}{\partial x}-\frac{d}{dt}\frac{\partial g_a}{\partial\dot x}\right)^\top\delta x+\left(\frac{\partial g_a}{\partial u}\right)^\top\delta u+\left(\frac{\partial g_a}{\partial p}\right)^\top\delta p\right]dt=0$$

逐項看 [▶ 81:47](https://youtu.be/7rejaoMWviw?t=4907)：

| 項 | 算出來 |
|---|---|
| $\dfrac{\partial g_a}{\partial p}$ | $f-\dot x$（動態） |
| $\dfrac{\partial g_a}{\partial\dot x}$ | $-p$，所以 $-\dfrac{d}{dt}(-p)=\dot p$ |
| $\dfrac{\partial g_a}{\partial x}$ | $\dfrac{\partial g}{\partial x}+\left(\dfrac{\partial f}{\partial x}\right)^\top p=\dfrac{\partial H}{\partial x}$ |
| $\dfrac{\partial g_a}{\partial u}$ | $\dfrac{\partial g}{\partial u}+\left(\dfrac{\partial f}{\partial u}\right)^\top p=\dfrac{\partial H}{\partial u}$ |

**論證** [▶ 82:47](https://youtu.be/7rejaoMWviw?t=4967)：只有 $\delta u$ 能**自由**變（$\delta x$ 被 $\delta u$ 透過動態決定）。所以要把其他項都弄掉：

1. $\delta p$ 項：最優點可行 → $f-\dot x=0$ → 這項 = 0。（→ 條件一：$\dot x=\partial H/\partial p$）
2. $\delta x$ 項：$p$ 是我們自己加進來的，可以**選** $p$ 讓係數 = 0：$\dot p=-\partial H/\partial x$。（→ 條件二）
3. 剩下 $\int\left(\partial H/\partial u\right)^\top\delta u\,dt=0$，$\delta u$ 任意 → 基本引理 → $\partial H/\partial u=0$。（→ 條件三）

[▶ 83:48](https://youtu.be/7rejaoMWviw?t=5028) 這正好是三組必要條件。差別只是正式版用 $H$ 寫得比較漂亮。講者邀請大家自己對照。

---

## 8. 一頁速查表

### 變分法（直接控制 $x$）

| 項目 | 式子 |
|---|---|
| Euler 方程 | $g_x-\dfrac{d}{dt}g_{\dot x}=0$（二階 ODE，兩端邊界值） |
| $t_f$ 固定、$x_f$ 自由 | $g_{\dot x}(t_f)=0$ |
| 最短路徑 | $g=\sqrt{1+\dot x^2}$ → $\dfrac{d}{dt}g_{\dot x}=\dfrac{\ddot x}{(1+\dot x^2)^{3/2}}$ → $\ddot x=0$ → 直線 |
| 微分約束 | $g_a=g+p^\top f$，對 $g_a$ 用 Euler ＋ 約束成立 |

### 最佳控制必要條件（控制無界）

$$H=g+p^\top f$$

| 條件 | 式子 | 關鍵一步（第 7 節） |
|---|---|---|
| 狀態 | $\dot x^*=\partial H/\partial p$ | 最優點可行，$\delta p$ 項消失 |
| 協態 | $\dot p^*=-\partial H/\partial x$ | 選 $p$ 讓 $\delta x$ 項係數 = 0（$\partial g_a/\partial\dot x=-p$） |
| 控制 | $0=\partial H/\partial u$ | 只剩 $\delta u$ 自由 → 基本引理 |

### 邊界條件

$$\left[\frac{\partial h}{\partial x}-p\right]_{t_f}^\top\delta x_f+\left[H+\frac{\partial h}{\partial t}\right]_{t_f}\delta t_f=0$$

| $t_f$ | $x(t_f)$ | 條件 |
|---|---|---|
| 固定 | 固定 | $x(t_f)=x_f$ |
| 固定 | 自由 | $p(t_f)=\partial h/\partial x\,\big|_{t_f}$ |
| 自由 | 固定 | $\left(H+\partial h/\partial t\right)\big|_{t_f}=0$ |
| 自由 | 自由 | 兩者都要 |

條件數：$2n$ 條 ODE → $2n$ 個常數（$t_f$ 自由時再 +1）。

### 雙積分器例子

$\ddot x=u$，$10\to 0$（靜止到靜止），$J=\frac12\alpha t_f^2+\frac12 b\int u^2$：
$u=-p_2/b$ 是時間的一次函數；$t_f=\left(1800b/\alpha\right)^{1/5}$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\partial H/\partial u=0$（控制無界） | 第 5 集：控制有界 → Pontryagin 最小原理 $u^*=\arg\min_u H$ |
| bang-bang 控制 | 第 5 集（講者預告） |
| 兩點邊界值問題、數值解法器 | 第 5 集計算方法（打靶法等） |
| 雙積分器、最小能量 | 第 8 集 LQR（二次成本＋線性系統的閉迴路版本，待確認） |
| 協態 ↔ Lagrange 乘數 | 第 6 集直接法（離散化後的 KKT 乘數，待確認） |

---

## 附：本集一句話總結

> **最佳控制的間接法：寫 Hamiltonian $H=g+p^\top f$，要求 $\dot x=\partial H/\partial p$、$\dot p=-\partial H/\partial x$、$\partial H/\partial u=0$，再依 $t_f$、$x(t_f)$ 固定或自由查表補邊界條件，最後解一個兩點邊界值問題。協態 $p$ 就是動態約束的 Lagrange 乘數，選它是為了消掉不能自由變的 $\delta x$。**

---

## ⚠️ 待確認清單

1. 上課日期待補（週三）。
2. [▶ 20:19](https://youtu.be/7rejaoMWviw?t=1219) 變分法版本的邊界條件方程是依描述和 Kirk 寫法重建，待對照投影片；表的後兩列是推論的。
3. [▶ 81:15](https://youtu.be/7rejaoMWviw?t=4875) 證明草稿中 $\delta J$ 的完整式子是依講者逐項說明重建，待對照投影片。

---

*筆記依據 Daniele Gammelli「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 4 錄影逐字稿（人工字幕，1:24:49）與《Principles of Robot Autonomy》§2.2.3 整理。*
