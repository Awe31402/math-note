---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 3
lecture: Lecture 3
date: 待補（週一）
video: https://youtu.be/duZJ2_ajLso
notes: 《Principles of Robot Autonomy》§2.2 開頭（書頁 61，變分法只有旁註）；KKT 課本沒有
---

# 第 3 集 · Lecture 3：變分法（Calculus of Variations） [▶ 影片](https://youtu.be/duZJ2_ajLso)

← 上一集：[02-optimization-theory](02-optimization-theory.md) ｜ [總目錄](README.md) ｜ 下一集：[04-indirect-methods](04-indirect-methods.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 3 集
> **講者**：Daniele Gammelli（Stanford 航太系 Autonomous Systems Lab 博士後）
> **來源**：YouTube 錄影逐字稿（1:22:57，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§2.2 開頭
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
- [1. 不等式約束與 KKT 條件（補完上一講）](#1-不等式約束與-kkt-條件補完上一講)
  - [1.1 問題與「有效約束」](#11-問題與有效約束)
  - [1.2 關鍵觀察：無效約束可以拿掉](#12-關鍵觀察無效約束可以拿掉)
  - [1.3 KKT 條件](#13-kkt-條件)
  - [1.4 例子：分情況討論](#14-例子分情況討論)
- [2. 間接法 vs 直接法](#2-間接法-vs-直接法)
- [3. 泛函的基本概念](#3-泛函的基本概念)
  - [3.1 泛函與線性泛函](#31-泛函與線性泛函)
  - [3.2 函數的範數：什麼叫兩個函數「接近」](#32-函數的範數什麼叫兩個函數接近)
  - [3.3 泛函的極值](#33-泛函的極值)
  - [3.4 增量、變分、可微](#34-增量變分可微)
- [4. 變分法基本定理](#4-變分法基本定理)
- [5. 最簡單的問題：推出 Euler 方程](#5-最簡單的問題推出-euler-方程)
  - [5.1 問題設定](#51-問題設定)
  - [5.2 Step 1：寫增量、泰勒展開](#52-step-1寫增量泰勒展開)
  - [5.3 Step 2：分部積分](#53-step-2分部積分)
  - [5.4 Step 3：邊界項消失](#54-step-3邊界項消失)
  - [5.5 Step 4：變分法基本引理 → Euler 方程](#55-step-4變分法基本引理--euler-方程)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/duZJ2_ajLso?t=5) 本集換人講：博士後 Daniele Gammelli。

【口頭】「我是義大利人。如果最佳控制學不好，至少你們會變成義大利口音專家。」

[▶ 02:18](https://youtu.be/duZJ2_ajLso?t=138) 回顧：上週定義了最佳控制問題（無限維），然後「開了一個括號」去看有限維最佳化：無約束 → $\nabla f=0$；等式約束 → Lagrange 乘數。

今天：

| 主題 | 課本 |
|---|---|
| 不等式約束、KKT 條件（補完上一講） | 課本沒有（§2.2.2 明說只講等式約束） |
| 間接法 vs 直接法 | 第 2 章開頭（書頁 60） |
| 泛函、範數、極值、變分 | 只有 §2.2 旁註 6 一段話 |
| 變分法基本定理、Euler 方程 | 課本沒有 |

**整集的主軸**：把有限維的每一步，**一對一**搬到無限維。

| 有限維（第 2 集） | 無限維（本集） |
|---|---|
| 函數 $f(x)$，$x\in\mathbb{R}^n$ | 泛函 $J(x)$，$x$ 是一個函數 $x(t)$ |
| 向量範數 → 鄰域 | 函數範數 → 鄰域 |
| 局部最小 | 泛函的局部最小 |
| 微分 $\nabla f^\top\Delta x$ | 變分 $\delta J$ |
| $\nabla f^\top\Delta x=0$ → $\nabla f=0$ | $\delta J=0$ → **Euler 方程** |

---

## 1. 不等式約束與 KKT 條件（補完上一講）

### 1.1 問題與「有效約束」

[▶ 03:20](https://youtu.be/duZJ2_ajLso?t=200) **不等式約束問題**（inequality constrained problem，ICP）：

$$
\begin{aligned}
\min_{x\in\mathbb{R}^n}\quad & f(x) \\
\text{s.t.}\quad & h_i(x)=0,\quad i=1,\dots,m \\
& g_j(x)\le 0,\quad j=1,\dots,r
\end{aligned}
$$

$f,h_i,g_j$ 都連續可微。

[▶ 04:21](https://youtu.be/duZJ2_ajLso?t=261) 不等式約束數學上難很多，可以講好幾堂。今天走「**捷徑**」：盡量重用上週等式約束的結果。工具是**有效約束**。

**定義** [▶ 04:54](https://youtu.be/duZJ2_ajLso?t=294)：對可行點 $x$，

- **有效約束**（active constraint）：等號成立的不等式約束，$g_j(x)=0$。集合記為 $A(x)$。
- **無效約束**（inactive constraint）：嚴格小於，$g_j(x)<0$。

**例子** [▶ 05:28](https://youtu.be/duZJ2_ajLso?t=328)：

$$\min\ x+y\quad\text{s.t.}\quad x\ge 0,\ \ y\ge 0,\ \ x+y\le 3$$

可行區是第一象限裡、直線 $x+y=3$ 下方的三角形。等高線是斜率 $-1$ 的直線，最小值在原點 $(0,0)$。

在 $(0,0)$：

| 約束 | 在 $(0,0)$ | 狀態 |
|---|---|---|
| 1：$x\ge 0$ | $x=0$ | 有效 |
| 2：$y\ge 0$ | $y=0$ | 有效 |
| 3：$x+y\le 3$ | $0<3$ | 無效 |

所以 $A(0,0)=\{1,2\}$。$A(x)$ 是一個**索引集合**，跟點有關。

【Q&A】[▶ 19:42](https://youtu.be/duZJ2_ajLso?t=1182) 學生問：怎麼判斷哪些有效？答：把點代進去，等號成立的就是有效。學生追問：如果點是 $(3,0)$？答：對，那就是約束 2 和 3 有效。

【Q&A】[▶ 18:09](https://youtu.be/duZJ2_ajLso?t=1089) 學生問這個例子裡的 $h$、$g$ 是什麼。答：沒有 $h$（沒有等式約束），三個都是 $g$。原本寫成 $\ge$，把符號翻過來就變成 $\le 0$ 的標準形式。

### 1.2 關鍵觀察：無效約束可以拿掉

[▶ 07:01](https://youtu.be/duZJ2_ajLso?t=421) 講者說「理解這個捷徑的腦力，大部分花在這裡」：

> 如果 $x^*$ 是 ICP 的局部最小值，那麼 $x^*$ 也是「**拿掉所有無效約束**」後那個問題的局部最小值。

**證明想法（反證法）** [▶ 07:33](https://youtu.be/duZJ2_ajLso?t=453)：

1. 假設 $x^*$ **不是**拿掉無效約束後的局部最小。
2. 那在 $x^*$ 附近，可以找到一點 $x'$，滿足剩下的約束，而且 $f(x')<f(x^*)$。
3. 無效約束在 $x^*$ 有「餘裕」（$g_j(x^*)<0$）。把鄰域取得夠小，無效約束在 $x'$ 也還是 $<0$。
4. 所以 $x'$ 滿足**原本所有**約束，又比 $x^*$ 好 → 跟「$x^*$ 是原問題局部最小」矛盾。

**結論** [▶ 10:05](https://youtu.be/duZJ2_ajLso?t=605)：在局部最小值，**有效的不等式約束可以當成等式約束**處理。

【Q&A】[▶ 10:37](https://youtu.be/duZJ2_ajLso?t=637) 一串學生追問「如果在邊界上，越過邊界函數可能更小，那這個說法還成立嗎？」。講者說不要太嚴格地看這個證明草稿；重點是**所有約束都要滿足**，只是在無效約束附近有餘裕可以動。這段討論字幕很亂，沒有得出明確結論。

### 1.3 KKT 條件

**從等式約束推過來** [▶ 13:46](https://youtu.be/duZJ2_ajLso?t=826)：上週等式約束的 Lagrangian 是 $L=f+\sum\lambda_i h_i$，條件是 $\nabla L=0$。現在把有效不等式約束當等式，加進來 [▶ 16:00](https://youtu.be/duZJ2_ajLso?t=960)：

$$\nabla f(x^*)+\sum_{i=1}^m\lambda_i^*\nabla h_i(x^*)+\sum_{j\in A(x^*)}\mu_j^*\nabla g_j(x^*)=0$$

等價寫法 [▶ 16:34](https://youtu.be/duZJ2_ajLso?t=994)：對**所有** $j=1,\dots,r$ 加總，但規定無效約束的 $\mu_j=0$。

另外還有一個條件 [▶ 17:06](https://youtu.be/duZJ2_ajLso?t=1026)：**不等式約束的乘數 $\mu_j\ge 0$**。為什麼要非負，有幾何解釋和證明，但超出本課範圍。

**KKT 定理** [▶ 22:17](https://youtu.be/duZJ2_ajLso?t=1337)（Karush–Kuhn–Tucker 條件）

> 定義 $L(x,\lambda,\mu)=f(x)+\sum_{i=1}^m\lambda_i h_i(x)+\sum_{j=1}^r\mu_j g_j(x)$。
>
> 設 $x^*$ 是 ICP 的局部最小值，$f,h,g$ 連續可微，且 $x^*$ 是**正則點**（等式約束和有效不等式約束的梯度線性獨立）。那麼存在**唯一**的乘數向量 $\lambda^*,\mu^*$，使得
> $$
> \begin{aligned}
> &\nabla_x L(x^*,\lambda^*,\mu^*)=0 \\
> &\mu_j^*\ge 0,\quad j=1,\dots,r \\
> &\mu_j^*=0,\quad j\notin A(x^*)
> \end{aligned}
> $$

> ⚠️ 逐字稿缺字 [▶ 22:49](https://youtu.be/duZJ2_ajLso?t=1369)：字幕寫「we assume that x of star is [INAUDIBLE]」，依後文應是 **regular**（正則）。講者口誤說 $\mu$「positive」，隨即改口為 non-negative（非負）。

> 以下**不是逐字稿內容**：「$\mu_j=0$ 對無效約束」常被寫成等價的 **互補鬆弛**（complementary slackness）$\mu_j^*\,g_j(x^*)=0$——有效時 $g_j=0$，無效時 $\mu_j=0$，兩者乘積都是 0。講者沒有用這個名字。

【Q&A】[▶ 23:21](https://youtu.be/duZJ2_ajLso?t=1401) 學生問：這樣是不是只檢查了邊界上的點？答：這是**必要**條件——所有局部最小值都要滿足它。（學生追問一個內部點的例子，講者說課後再私下討論。）

> 以下**不是逐字稿內容**，是依 KKT 定理推論的補充：學生擔心的內部點（沒有任何約束有效）並沒有被漏掉。那時 $A(x)=\varnothing$，所有 $\mu_j=0$，KKT 就退化成 $\nabla f=0$（加上等式約束項），也就是第 2 集的無約束條件。下面 1.4 的情況 2 正是這樣。

【Q&A】[▶ 24:54](https://youtu.be/duZJ2_ajLso?t=1494) 學生問：解是不是一定至少有一個約束有效？答：通常解落在目標函數和約束「拉扯」的地方，所以通常是。（但 1.4 的例子就是反例：最小值在內部。）

【Q&A】[▶ 31:58](https://youtu.be/duZJ2_ajLso?t=1918) 學生問：為什麼有效約束的 $\mu$ 要非負？答：有幾何解釋，但比較 tricky，超出範圍，可以給文獻。

### 1.4 例子：分情況討論

[▶ 25:28](https://youtu.be/duZJ2_ajLso?t=1528)

$$\min\ x^2+y^2\quad\text{s.t.}\quad g(x,y)=2x+y-2\le 0$$

> ⚠️ 逐字稿缺字 [▶ 25:28](https://youtu.be/duZJ2_ajLso?t=1528)：字幕寫「x squared plus **epsilon** squared」，依後面的梯度 $(2x,2y)$ 應為 $y^2$。

**梯度**：$\nabla f=(2x,2y)^\top$，$\nabla g=(2,1)^\top$。

不等式約束要**分情況**：有效或無效。

**情況 1：約束有效**（$2x+y=2$）[▶ 27:04](https://youtu.be/duZJ2_ajLso?t=1624)

$$\begin{pmatrix}2x\\2y\end{pmatrix}+\mu\begin{pmatrix}2\\1\end{pmatrix}=0\ \Rightarrow\ x=-\mu,\quad y=-\frac{\mu}{2}$$

代入 $2x+y=2$：

$$-2\mu-\frac{\mu}{2}=2\ \Rightarrow\ -\frac{5\mu}{2}=2\ \Rightarrow\ \mu=-\frac45$$

$\mu<0$，違反 $\mu\ge 0$ → **這種情況沒有候選點**。

> ⚠️ 逐字稿缺字 [▶ 28:14](https://youtu.be/duZJ2_ajLso?t=1694)：字幕寫「what we get is **2 mu equal to 2**」，中間步驟不清楚；最後的 $\mu=-4/5$ 和上面的計算一致。

**情況 2：約束無效**（$2x+y<2$）[▶ 29:19](https://youtu.be/duZJ2_ajLso?t=1759)

無效 → $\mu=0$ → $(2x,2y)=0$ → $x=y=0$。

檢查：$2\cdot 0+0=0<2$ ✓。**候選點 $(0,0)$。**

**幾何檢查** [▶ 30:26](https://youtu.be/duZJ2_ajLso?t=1826)：約束是直線 $2x+y=2$ 的一側；目標是以原點為中心的碗。原點在可行區裡，所以全域最小就是 $(0,0)$。

【Q&A】[▶ 30:26](https://youtu.be/duZJ2_ajLso?t=1826) 學生問：情況 2 為什麼 $\mu=0$？答：KKT 條件規定無效約束的乘數是 0。

【Q&A】[▶ 33:01](https://youtu.be/duZJ2_ajLso?t=1981) 學生問：情況 1 的結論是不是「不存在讓這個約束有效的候選點」？答：對。這就是用必要條件**過濾候選點**。

---

## 2. 間接法 vs 直接法

[▶ 34:06](https://youtu.be/duZJ2_ajLso?t=2046) 回到課程地圖。接下來 2–3 週在「**開迴路**」那一塊。先講**間接法**（約 3 堂），再講**直接法**。

| | 間接法（indirect） | 直接法（direct） |
|---|---|---|
| 口號 | **先最佳化，再離散化**（optimize then discretize） | **先離散化，再最佳化**（discretize then optimize） |
| 做法 | 推出最佳控制的必要條件（會是**微分方程**），再用數值解法解（解法本身要離散化） | 先把時間離散化（積分換成加總），再解有限維最佳化問題 |
| 歷史 | 60、70 年代最佳控制的起點 | 現代實務上的主流 |

（課本第 2 章開頭也用同樣的口號區分兩類方法。）

**為什麼還要學「古老」的間接法？** [▶ 37:51](https://youtu.be/duZJ2_ajLso?t=2271)

- 有時能給**解析或半解析解**。部署時機上幾乎不用計算，適合算力很有限的場合。**航太**大量使用。
- 常拿來給直接法當**初始猜測**。

【口頭】[▶ 38:23](https://youtu.be/duZJ2_ajLso?t=2303) 這些技術數學上很硬，教科書多半是數學家寫的，不一定符合控制工程師的需求。講者推薦投影片上的一本參考書，說它取得不錯的平衡。

> 推薦書名字幕沒唸出來。課本 §2.2 推薦變分法與最佳控制可看 Kirk [70]（*Optimal Control Theory: An Introduction*），是否同一本待確認。

**最佳控制問題回顧** [▶ 39:24](https://youtu.be/duZJ2_ajLso?t=2364)：找可容許控制 $u^*$，讓 $\dot x=f(x,u,t)$ 走出可容許軌跡 $x^*$，使泛函 $J$ 最小。

**變分法**（calculus of variations，CoV）[▶ 40:57](https://youtu.be/duZJ2_ajLso?t=2457)：微積分的推廣，用「**變分**」（variation）找**泛函**的極大極小。歷史比間接法更久，約 300–400 年。

【課本補充】課本 §2.2 旁註 6：變分法把古典微積分從函數推廣到泛函；核心想法是看候選函數被小擾動（變分）後泛函怎麼變，分析一階、高階效應來推必要條件。

---

## 3. 泛函的基本概念

[▶ 41:58](https://youtu.be/duZJ2_ajLso?t=2518) 講者說接下來 15 分鐘「有點無聊」，但要建立記號。

### 3.1 泛函與線性泛函

**泛函**（functional）[▶ 43:03](https://youtu.be/duZJ2_ajLso?t=2583)：

> 一個對應規則 $J$，把某個函數類別 $\Omega$（例如連續函數）裡的每個函數 $x$，對應到**唯一**一個實數 $J(x)$。

直覺：「函數的函數」。輸入是**一整個函數**（一整條訊號），輸出是一個數（衡量好壞）。

**例子** [▶ 43:34](https://youtu.be/duZJ2_ajLso?t=2614)：
$$J(x)=\int_{t_0}^{t_f}x(t)\,dt$$
（$t_0,t_f$ 就是兩個數，例如 3 和 6；$x$ 是任意連續函數。）

**線性泛函**（linear functional）滿足：

1. **齊次性**（homogeneity）：$J(\alpha x)=\alpha J(x)$
2. **可加性**（additivity）[▶ 44:39](https://youtu.be/duZJ2_ajLso?t=2679)：$J(x_1+x_2)=J(x_1)+J(x_2)$

兩者合起來叫**疊加性**（superposition）。

**例子是線性的** [▶ 45:09](https://youtu.be/duZJ2_ajLso?t=2709)：
$$J(\alpha x)=\int_{t_0}^{t_f}\alpha\,x(t)\,dt=\alpha\int_{t_0}^{t_f}x(t)\,dt=\alpha J(x)$$
可加性一樣簡單（積分可以拆開）。

### 3.2 函數的範數：什麼叫兩個函數「接近」

[▶ 45:45](https://youtu.be/duZJ2_ajLso?t=2745) 有限維定義最小值要用「鄰域」，鄰域要用「接近」，接近要用**範數**（norm）。函數也一樣。

**函數的範數** [▶ 46:17](https://youtu.be/duZJ2_ajLso?t=2777)：對每個 $x\in\Omega$ 給一個實數 $\|x\|$，滿足

1. $\|x\|\ge 0$，而且 $\|x\|=0$ ⟺ 對所有 $t$，$x(t)=0$
2. $\|\alpha x\|=|\alpha|\,\|x\|$，對所有實數 $\alpha$
3. 三角不等式：$\|x_1+x_2\|\le\|x_1\|+\|x_2\|$

**比較兩個函數 $y,z$ 有多接近** [▶ 47:18](https://youtu.be/duZJ2_ajLso?t=2838)：令 $x=y-z$，看 $\|x\|$。（是**差**的範數，不是各自的範數。）

**例子** [▶ 47:48](https://youtu.be/duZJ2_ajLso?t=2868)：連續函數可以用
$$\|x\|=\max_{t_0\le t\le t_f}|x(t)|$$
- 取絕對值的最大 → 一定 $\ge 0$。
- 等於 0 ⟺ 每個時間都是 0。
- 另外兩條留給你自己檢查。

【Q&A】[▶ 48:54](https://youtu.be/duZJ2_ajLso?t=2934) 學生問：範數跟「接近」怎麼連起來？答：有限維裡用範數量向量之間的距離。無限維就照搬直覺：用函數的範數量函數之間的距離，距離小就叫「接近」。

### 3.3 泛函的極值

[▶ 50:28](https://youtu.be/duZJ2_ajLso?t=3028)

> 泛函 $J$ 在 $x^*$（一整個函數）有**局部最小值**：存在 $\varepsilon>0$，使得所有滿足 $\|x-x^*\|<\varepsilon$ 的 $x\in\Omega$ 都有
> $$J(x)\ge J(x^*)$$

最大值把不等號翻過來。跟有限維一模一樣，只是 $x$ 換成函數。

【Q&A】[▶ 50:59](https://youtu.be/duZJ2_ajLso?t=3059) 學生問：我們要最佳化的是 $u$，為什麼寫 $x$？答：這裡 $x$ 是一般記號。實際上我們最佳化的都是控制訊號 $u$。

### 3.4 增量、變分、可微

[▶ 52:04](https://youtu.be/duZJ2_ajLso?t=3124) **回顧有限維**：

$$\Delta f=f(x+\Delta x)-f(x)=\underbrace{\nabla f(x)^\top\Delta x}_{\text{微分（線性部分）}}+\text{高階項}$$

$\Delta x$ 夠小時，線性部分主導。我們對**線性部分**加條件，得到 $\nabla f=0$。

**無限維照做** [▶ 53:41](https://youtu.be/duZJ2_ajLso?t=3221)：

**增量**（increment）：
$$\Delta J(x,\delta x)=J(x+\delta x)-J(x)$$

$\delta x$ 是 $x$ 的**變分**（一個函數）。

> 【Q&A】[▶ 54:52](https://youtu.be/duZJ2_ajLso?t=3292) 學生問：$\Delta J(x,\delta x)$ 中間的逗號是不是應該是加號？答：不是。這是把增量寫成「原函數 $x$」和「變分 $\delta x$」兩個東西的函數；它的值等於 $J(x+\delta x)-J(x)$。

**可微** [▶ 55:53](https://youtu.be/duZJ2_ajLso?t=3353)：把增量寫成

$$\Delta J(x,\delta x)=\delta J(x,\delta x)+g(x,\delta x)\cdot\|\delta x\|$$

- $\delta J$ 對 $\delta x$ 是**線性**的。
- 如果 $\displaystyle\lim_{\|\delta x\|\to 0}g(x,\delta x)=0$，就說 $J$ 在 $x$ **可微**，$\delta J$ 叫 $J$ 在 $x$ 的**變分**（variation）。

**為什麼這樣定義** [▶ 56:24](https://youtu.be/duZJ2_ajLso?t=3384)：

- 「隨便什麼東西都能寫成線性部分 + 其他」，重點在其他部分的性質。
- $g\to 0$ 乘上 $\|\delta x\|\to 0$ → 「其他」以**二次速度**趨近 0。
- $\delta J$ 是線性的 → 只以**一次速度**趨近 0。
- 所以 $\delta x$ 小時，增量 ≈ $\delta J$。跟有限維「微分主導」一樣。

> 以下**不是逐字稿內容**：投影片上 $g$ 的具體寫法字幕沒唸；上面「$g\cdot\|\delta x\|$」是依講者「something that goes to 0 times something that also goes to 0」寫出的標準形式（Kirk 書的寫法）。

【Q&A】[▶ 57:28](https://youtu.be/duZJ2_ajLso?t=3448) 學生問：這個定義是從泰勒展開來的嗎？答：好問題。目前講的都還**不能實際計算**，只是在搭舞台、跟有限維平行。下幾頁會示範怎麼算（答案是：會用到泰勒展開，見 5.2）。

【Q&A】[▶ 61:13](https://youtu.be/duZJ2_ajLso?t=3673) 學生問大寫 $\Delta J$ 和小寫 $\delta J$ 差在哪。答：$\Delta J$ 是**增量**（定義：兩個泛函值相減）；$\delta J$ 是**變分**，是逼近增量的**線性部分**，類比於微分。

【Q&A】[▶ 63:15](https://youtu.be/duZJ2_ajLso?t=3795) 學生問：$\delta x$ 不是 $x$ 對時間的變化吧？答：對。講者畫圖 [▶ 64:15](https://youtu.be/duZJ2_ajLso?t=3855)：$x(t)$ 是一條曲線，$\delta x(t)$ 本身是**另一條函數**，$x+\delta x$ 是把兩條加起來得到的新曲線。$\delta x$ 是「整條曲線的擾動」，不是時間上的增量。

---

## 4. 變分法基本定理

[▶ 59:04](https://youtu.be/duZJ2_ajLso?t=3544)

> **變分法基本定理**（fundamental theorem of calculus of variations）
>
> 設 $x(t)$ 是 $\Omega$ 裡的向量函數，$J(x)$ 是 $x$ 的可微泛函，且 $\Omega$ 裡的函數不受邊界限制。如果 $x^*$ 是**極值**（extremal），那麼 $J$ 在 $x^*$ 的變分必須為 0：
> $$\delta J(x^*,\delta x)=0\qquad\text{對所有夠小的可容許 }\delta x$$

- 證明很繁瑣、不太有啟發性，略過。
- **解讀** [▶ 60:08](https://youtu.be/duZJ2_ajLso?t=3608)：這就是有限維「$\nabla f^\top\Delta x=0$」的類比。
- 有限維裡，那個條件馬上變成可計算的 $\nabla f=0$。這裡**還不能直接算**，下一節把它變成可計算的東西。

---

## 5. 最簡單的問題：推出 Euler 方程

### 5.1 問題設定

[▶ 64:48](https://youtu.be/duZJ2_ajLso?t=3888) 「能想到最簡單的最佳控制問題」：

$$\min_{x}\ J(x)=\int_{t_0}^{t_f}g\left(x(t),\dot x(t),t\right)dt$$

- 沒有控制 $u$。可以想成**直接操縱狀態軌跡** $x(t)$。
- $g$ 二次可微。
- $t_0,t_f$ **固定**（週三會放寬）。
- $x(t_0)=x_0$、$x(t_f)=x_f$ **固定**。

### 5.2 Step 1：寫增量、泰勒展開

[▶ 67:21](https://youtu.be/duZJ2_ajLso?t=4041) 照定義：

$$\Delta J=\int_{t_0}^{t_f}\left[g\left(x+\delta x,\ \dot x+\delta\dot x,\ t\right)-g\left(x,\dot x,t\right)\right]dt$$

（兩個積分合併成一個。）記號：$\dot x=\dfrac{dx}{dt}$，$\delta\dot x=\dfrac{d}{dt}\delta x$。

【課堂討論】[▶ 68:58](https://youtu.be/duZJ2_ajLso?t=4138) 講者問：固定一個 $t$，要抽出線性部分，平常用什麼工具？學生答：**泰勒展開**。講者：對，這門課會一直用泰勒。

[▶ 69:29](https://youtu.be/duZJ2_ajLso?t=4169) 對第一項泰勒展開（$g_x=\partial g/\partial x$，$g_{\dot x}=\partial g/\partial\dot x$）：

$$\Delta J=\int_{t_0}^{t_f}\left[g+g_x\,\delta x+g_{\dot x}\,\delta\dot x+\text{(高階項)}-g\right]dt$$

第一項和最後一項抵銷 [▶ 70:01](https://youtu.be/duZJ2_ajLso?t=4201)。剩下三項裡，高階項顯然不是線性部分。所以：

$$\delta J=\int_{t_0}^{t_f}\left[g_x\left(x^*,\dot x^*,t\right)\delta x+g_{\dot x}\left(x^*,\dot x^*,t\right)\delta\dot x\right]dt$$

### 5.3 Step 2：分部積分

[▶ 71:32](https://youtu.be/duZJ2_ajLso?t=4292) 定理要的條件是「對所有 $\delta x$」，但現在式子裡還有 $\delta\dot x$。要把它也改寫成 $\delta x$。

**分部積分**（integration by parts）[▶ 73:41](https://youtu.be/duZJ2_ajLso?t=4421)：
$$\int u\,dv=uv-\int v\,du$$

對第二項，取 $u=g_{\dot x}$，$dv=\delta\dot x\,dt$（所以 $v=\delta x$）[▶ 74:12](https://youtu.be/duZJ2_ajLso?t=4452)：

$$\int_{t_0}^{t_f}g_{\dot x}\,\delta\dot x\,dt=\Big[g_{\dot x}\,\delta x\Big]_{t_0}^{t_f}-\int_{t_0}^{t_f}\delta x\,\frac{d}{dt}g_{\dot x}\,dt$$

代回去 [▶ 76:24](https://youtu.be/duZJ2_ajLso?t=4584)：

$$\delta J=\int_{t_0}^{t_f}\left[g_x-\frac{d}{dt}g_{\dot x}\right]\delta x\,dt+\Big[g_{\dot x}\,\delta x\Big]_{t_0}^{t_f}$$

### 5.4 Step 3：邊界項消失

[▶ 77:39](https://youtu.be/duZJ2_ajLso?t=4659) 因為 $x(t_0)$、$x(t_f)$ 固定，所有可容許的曲線都要通過這兩個端點 → $\delta x(t_0)=\delta x(t_f)=0$ → 邊界項 = 0。

剩下（必要條件 $\delta J=0$）：

$$\int_{t_0}^{t_f}\left[g_x\left(x^*,\dot x^*,t\right)-\frac{d}{dt}g_{\dot x}\left(x^*,\dot x^*,t\right)\right]\delta x(t)\,dt=0\qquad\text{對所有可容許 }\delta x$$

> ⚠️ 逐字稿缺字 [▶ 78:50](https://youtu.be/duZJ2_ajLso?t=4730)：字幕寫「times **dx dt** equal to 0」，依上下文應為「乘上 $\delta x(t)$，再對 $t$ 積分」。

### 5.5 Step 4：變分法基本引理 → Euler 方程

**變分法基本引理**（fundamental lemma of calculus of variations）[▶ 80:27](https://youtu.be/duZJ2_ajLso?t=4827)

> 若 $h$ 在 $[t_0,t_f]$ 上連續，且對所有（端點為 0 的）連續 $\delta x$ 都有
> $$\int_{t_0}^{t_f}h(t)\,\delta x(t)\,dt=0$$
> 那麼 $h(t)=0$ 在整個 $[t_0,t_f]$ 上成立。

**直覺** [▶ 81:29](https://youtu.be/duZJ2_ajLso?t=4889)：假設 $h$ 在某個時間 $t$ 是正的。那我可以「惡意地」挑一個 $\delta x$，只在那附近是正的、其他地方是 0。積分就會是正的，不是 0。所以 $h$ 只能處處為 0。

**套用** [▶ 82:05](https://youtu.be/duZJ2_ajLso?t=4925)：取 $h=g_x-\dfrac{d}{dt}g_{\dot x}$，得到

$$\boxed{\ g_x\left(x^*(t),\dot x^*(t),t\right)-\frac{d}{dt}\left[g_{\dot x}\left(x^*(t),\dot x^*(t),t\right)\right]=0,\qquad t\in[t_0,t_f]\ }$$

這叫 **Euler 方程**（Euler equation），是這個無限維問題的必要最佳性條件。注意它是一條**微分方程**（呼應「間接法的必要條件是微分方程」）。

【口頭】[▶ 82:05](https://youtu.be/duZJ2_ajLso?t=4925) 「當年花了 20 年，我們 45 分鐘就到了。」

> ⚠️ 待確認 [▶ 82:05](https://youtu.be/duZJ2_ajLso?t=4925)：字幕寫「we have fast tracked **Newton**. He basically took 20 years」。依上下文主角應是 Euler（方程以他命名），字幕可能聽錯，待確認。

下次（週三）會複習並繼續。

---

## 6. 一頁速查表

### KKT 條件（不等式約束）

$$\min f(x)\quad\text{s.t.}\quad h_i(x)=0,\ \ g_j(x)\le 0$$

| 項目 | 式子 |
|---|---|
| 有效集合 | $A(x)=\{j:g_j(x)=0\}$ |
| 關鍵觀察 | $x^*$ 是原問題局部最小 ⟹ 也是「拿掉無效約束」問題的局部最小（反證：無效約束有餘裕）→ 有效約束當等式 |
| Lagrangian | $L=f+\sum\lambda_i h_i+\sum\mu_j g_j$ |
| KKT（$x^*$ 正則） | $\nabla_x L=0$，$\mu_j\ge 0$，無效約束 $\mu_j=0$ |
| 用法 | 對每個不等式約束分「有效／無效」情況；有效時解出的 $\mu<0$ → 丟掉；無效時檢查約束是否真的 $<0$ |

### 有限維 ↔ 無限維

| 有限維 | 無限維 |
|---|---|
| $\|x\|$（向量） | $\|x\|$，例 $\max_t|x(t)|$（函數） |
| $\Delta f=\nabla f^\top\Delta x+\cdots$ | $\Delta J=\delta J+g\cdot\|\delta x\|$，$g\to 0$ |
| $\nabla f^\top\Delta x=0$ | $\delta J(x^*,\delta x)=0$（變分法基本定理） |
| $\nabla f=0$ | Euler 方程 |

### Euler 方程推導（$J=\int_{t_0}^{t_f}g(x,\dot x,t)\,dt$，端點固定）

1. 泰勒：$\delta J=\int\left(g_x\,\delta x+g_{\dot x}\,\delta\dot x\right)dt$
2. 分部積分：$\int g_{\dot x}\,\delta\dot x\,dt=\left[g_{\dot x}\delta x\right]_{t_0}^{t_f}-\int\delta x\,\frac{d}{dt}g_{\dot x}\,dt$
3. 端點固定 → $\delta x(t_0)=\delta x(t_f)=0$ → 邊界項消失
4. 基本引理（$\int h\,\delta x\,dt=0\ \forall\delta x$ ⟹ $h\equiv 0$）：

$$g_x-\frac{d}{dt}g_{\dot x}=0$$

### 間接 vs 直接

- 間接：先最佳化（推出微分方程形式的必要條件）再離散化（數值解）。可給解析解、適合算力少（航太）、可給直接法當初始猜測。
- 直接：先離散化（積分 → 加總）再最佳化（有限維 NLP）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Euler 方程、變分法 | 第 4 集：放寬端點和 $t_f$，加入動態約束，推到完整最佳控制問題 |
| 邊界項 $\left[g_{\dot x}\delta x\right]_{t_0}^{t_f}$ | 第 4 集：端點或 $t_f$ 自由時不會消失 → 變成**邊界條件**（課本 §2.2.3 式 2.17） |
| Lagrange 乘數 → 動態約束 | 第 4 集：Hamiltonian、協態、Pontryagin 最小原理 |
| KKT 條件 | 第 6 集直接法（解離散化後的有限維 NLP）；第 11–12 集 MPC（待確認） |
| 先離散化再最佳化 | 第 6 集直接法 |

---

## 附：本集一句話總結

> **把有限維「微分 = 0」搬到泛函上：算出增量的線性部分（變分 $\delta J$），用分部積分把 $\delta\dot x$ 換成 $\delta x$、端點固定讓邊界項消失，再用基本引理去掉積分，就得到必要條件 Euler 方程 $g_x-\frac{d}{dt}g_{\dot x}=0$——一條微分方程。**

---

## ⚠️ 待確認清單

1. 上課日期待補（字幕說「over the last week」，本集週一、下集週三）。
2. [▶ 38:23](https://youtu.be/duZJ2_ajLso?t=2303) 講者推薦的參考書名字幕沒唸，是否為 Kirk《Optimal Control Theory》待確認。
3. [▶ 55:53](https://youtu.be/duZJ2_ajLso?t=3353) 可微定義中「其他部分」的具體寫法是依標準教科書重建，待對照投影片。
4. [▶ 82:05](https://youtu.be/duZJ2_ajLso?t=4925) 「fast tracked Newton… took 20 years」的人名，可能是 Euler，待確認。

---

*筆記依據 Daniele Gammelli「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 3 錄影逐字稿（人工字幕，1:22:57）與《Principles of Robot Autonomy》§2.2 開頭整理。*
