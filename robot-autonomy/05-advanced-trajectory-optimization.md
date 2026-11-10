---
course: Stanford AA274A Principles of Robotic Autonomy（2019 秋）
episode: 5
lecture: Lecture 5（週五加課）
date: 待補（週五）
video: https://youtu.be/Izu4_AUiHyk
notes: 《Principles of Robot Autonomy》§2.2（書頁 61–69，PDF 頁 63–71）
---

# 第 5 集 · Lecture 5：進階軌跡最佳化——間接法（Advanced Trajectory Optimization） [▶ 影片](https://youtu.be/Izu4_AUiHyk)

← 上一集：[04-trajectory-tracking](04-trajectory-tracking.md) ｜ [總目錄](README.md) ｜ 下一集：[06-motion-planning-graph-search](06-motion-planning-graph-search.md) →

> **課程**：Stanford AA274A Principles of Robotic Autonomy I，2019 秋 — 第 5 集（週五研究所加課）
> **講者**：Marco Pavone（推斷：說自己和 Lagrange 一樣來自杜林、春季開最佳控制課）
> **來源**：YouTube 錄影逐字稿（1:17:45，Whisper `medium.en` 轉錄）＋《Principles of Robot Autonomy》§2.2
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 最佳控制問題回顧：無限維最佳化](#1-最佳控制問題回顧無限維最佳化)
- [2. 微分平坦屬於哪一類？](#2-微分平坦屬於哪一類)
- [3. 先熱身：有等式約束的有限維最佳化](#3-先熱身有等式約束的有限維最佳化)
  - [3.1 Lagrange 乘數法](#31-lagrange-乘數法)
  - [3.2 例子：圓上求 $x_1 + x_2$ 的最小值](#32-例子圓上求-x_1--x_2-的最小值)
- [4. 最佳控制的必要條件](#4-最佳控制的必要條件)
  - [4.1 Hamiltonian 與協態](#41-hamiltonian-與協態)
  - [4.2 方程與未知數的計數](#42-方程與未知數的計數)
  - [4.3 邊界條件：主方程](#43-邊界條件主方程)
- [5. 兩點邊界值問題與求解器](#5-兩點邊界值問題與求解器)
- [6. 自由終端時間：時間重新縮放](#6-自由終端時間時間重新縮放)
- [7. 完整例子：雙積分器、最小化時間＋控制量](#7-完整例子雙積分器最小化時間控制量)
- [8. 直接法與間接法的關係](#8-直接法與間接法的關係)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/Izu4_AUiHyk?t=0)

這是軌跡最佳化的最後一堂。微分平坦只求「可行、夠好」；但有時真的需要**最佳**的軌跡（最短時間、最少控制量或兩者折衷），這就是**最佳控制（optimal control）**。

今天深入**間接法**，給可以直接上手的做法（作業最後一題要用），最後談間接法和直接法的關係。

`【口頭】` 參考書：Kirk 的最佳控制教科書，有點舊，但嚴謹又好讀；最佳控制通常數學很重。

| 主題 | 課本 |
|---|---|
| 無約束必要條件 $\nabla f = 0$ | §2.2.1 |
| Lagrange 乘數法 | §2.2.2 |
| Pontryagin 最小原理、邊界條件 | §2.2.3 |
| 兩點邊界值問題、`solve_bvp` | §2.2.4 |
| 自由終端時間例子（雙積分器） | §2.2.4 Example 2.2.1（和本集同一題） |

---

## 1. 最佳控制問題回顧：無限維最佳化

[▶ 02:14](https://youtu.be/Izu4_AUiHyk?t=134)

$$
\begin{aligned}
\min_{u(\cdot)}\ & h\left( x(t_f), t_f \right) + \int_{t_0}^{t_f} g\left( x(t), u(t), t \right) dt \\
\text{s.t. }\ & \dot x = a(x, u, t), \quad u(t) \in U, \quad x(t_0) = x_0
\end{aligned}
$$

這週沒有狀態約束（障礙物下週處理）。

**為什麼比一般最佳化難**（[▶ 04:04](https://youtu.be/Izu4_AUiHyk?t=244)）：一般最佳化的決策變數是有限個 $x_1, x_2, x_3$；這裡要最佳化的是**函數** $u(t)$。$t$ 是連續的，每個 $t$ 都是一個決策變數，所以有不可數無限多個。函數空間是無限維的，所以叫**無限維問題（infinite-dimensional problem）**。不是「無限倍難」，但確實比較難。

標準設定是求**開迴路**控制 $u(t)$。兩類方法（第 3 集講過）：

- **間接法**：先寫出無限維問題的必要條件，再解它們（先最佳化，再離散化）。
- **直接法**：先離散化成有限維非線性最佳化，再解（先離散化，再最佳化）。

---

## 2. 微分平坦屬於哪一類？

[▶ 07:18](https://youtu.be/Izu4_AUiHyk?t=438)

- `【Q&A】` 微分平坦的方法屬於哪一類？→ **兩類都不是**。哲學上比較接近**直接法**，因為沒有寫必要條件，而是把問題轉成有限維問題（甚至一組線性方程）。但嚴格說，微分平坦解的是**可行性問題**，不是最佳化問題；雖然可以在平坦輸出空間加 jerk、snap 成本，引入一點最佳性。所以可以把它看成「不太嚴格要求最佳性的直接法特例」。

---

## 3. 先熱身：有等式約束的有限維最佳化

### 3.1 Lagrange 乘數法

[▶ 08:47](https://youtu.be/Izu4_AUiHyk?t=527)

**無約束**：$\min_{x \in \mathbb{R}^n} f(x)$。假設可微，必要條件是 $\nabla f(x) = 0$；解出所有滿足的點當候選，再挑成本最低的。這就是「先寫必要條件，再解」的流程，解的是非線性代數方程。

間接法在最佳控制上做一樣的事，只是必要條件複雜得多。老師不證明，而是類比有限維最佳化來解釋，而且要加上**等式約束**：

$$
\min_{x \in \mathbb{R}^n} f(x) \quad \text{s.t. } h_i(x) = 0,\ i = 1, \dots, m
$$

`【課堂討論】` [▶ 11:27](https://youtu.be/Izu4_AUiHyk?t=687) 為什麼加等式約束才比較像最佳控制？每個最佳控制問題都有的等式約束是哪一個？→ **運動方程** $\dot x = a(x, u, t)$。它是微分方程不是代數方程，但仍是等式約束。

- `【Q&A】` [▶ 12:52](https://youtu.be/Izu4_AUiHyk?t=772)（問一般也有不等式約束吧）→ 對，一般非線性最佳化有等式和不等式約束，也能推必要條件，最佳控制也可能有更複雜的約束、導出更複雜的必要條件，但超出本課範圍。這裡只講等式約束，是為了教學。

**Lagrange 理論**（[▶ 14:30](https://youtu.be/Izu4_AUiHyk?t=870)）：直接對著約束推理很難。想法是把約束**搬進成本函數**，用懲罰項懲罰違反約束，變成無約束問題——那我們就會寫必要條件了。定義 **Lagrangian**：

$$
L(x, \lambda) = f(x) + \sum_{i=1}^{m} \lambda_i\, h_i(x)
$$

$\lambda_1, \dots, \lambda_m$ 叫 **Lagrange 乘數**，是額外的決策變數，每個約束一個。

**定理（必要條件）**：若 $x^*$ 是局部最小值（且是**正則點 regular**——約束梯度線性獨立，一個溫和的技術條件），則存在 $\lambda^*$ 使 $(x^*, \lambda^*)$ 是 $L$ 的駐點：

$$
\frac{\partial L}{\partial x}(x^*, \lambda^*) = 0, \qquad \frac{\partial L}{\partial \lambda}(x^*, \lambda^*) = 0
$$

`【課堂討論】` [▶ 19:59](https://youtu.be/Izu4_AUiHyk?t=1199) 對 $\lambda_i$ 偏微分得到什麼？→ $h_i(x)$。所以 $\partial L/\partial\lambda = 0$ 就是**原本的約束**，保證點是可行的；$\partial L/\partial x = 0$ 那部分保證是局部極值。

**實務流程**：寫 Lagrangian → 找駐點（同時解 $x$ 和 $\lambda$）→ **丟掉 $\lambda$**（只是輔助變數）→ 剩下的 $x$ 就是候選解。

`【口頭】` Lagrange 不是法國人，是**義大利人**：本名 Lagrangia，生在杜林（老師的家鄉），大約 40 歲搬到法國，法國人叫他 Lagrange，聽起來比較法國。

【課本補充】§2.2.2 的幾何解釋：$\nabla f(x^*)$ 必須和「一階可行變化方向」的子空間 $\{\Delta x : \nabla h_i(x^*)^\top \Delta x = 0\}$ 正交；也就是沿著約束面移動時，成本的一階變化為 0，和無約束的 $\nabla f = 0$ 同一個意思。

### 3.2 例子：圓上求 $x_1 + x_2$ 的最小值

[▶ 21:44](https://youtu.be/Izu4_AUiHyk?t=1304)

$$
\min\ x_1 + x_2 \quad \text{s.t. } x_1^2 + x_2^2 = 2
$$

**幾何解法**：可行點是半徑 $\sqrt 2$ 的圓。成本的等值線 $x_1 + x_2 = c$ 是斜 45 度的直線。把直線盡量往左下推，但必須和圓相交，推到相切為止。由對稱性，切點是 $(-1, -1)$。

**Lagrange 解法**：

**Step 1**：寫 Lagrangian（一個約束 → 一個乘數）：

$$
L = x_1 + x_2 + \lambda\left( x_1^2 + x_2^2 - 2 \right)
$$

**Step 2**：駐點條件：

$$
\frac{\partial L}{\partial x_1} = 1 + 2\lambda x_1 = 0, \qquad
\frac{\partial L}{\partial x_2} = 1 + 2\lambda x_2 = 0, \qquad
\frac{\partial L}{\partial \lambda} = x_1^2 + x_2^2 - 2 = 0
$$

**Step 3**：3 個未知數、3 條方程。由前兩式 $x_1 = x_2 = -\dfrac{1}{2\lambda}$，代入第三式：

$$
\frac{1}{4\lambda^2} + \frac{1}{4\lambda^2} = 2 \;\Rightarrow\; \frac{1}{2\lambda^2} = 2 \;\Rightarrow\; \lambda^2 = \frac14 \;\Rightarrow\; \lambda = \pm\frac12
$$

- $\lambda = \frac12$：$x_1 = x_2 = -1$，成本 $-2$。
- $\lambda = -\frac12$：$x_1 = x_2 = 1$，成本 $2$。

**Step 4**：丟掉 $\lambda$，比較成本：最小值在 $(-1, -1)$，和幾何解一致。

> ⚠️ 逐字稿缺字 [▶ 27:25](https://youtu.be/Izu4_AUiHyk?t=1645)：Whisper 寫「x2 is equal to 1 minus 1 over 2 lambda」，多了一個「1」；由 $1 + 2\lambda x_2 = 0$ 應是 $x_2 = -\frac{1}{2\lambda}$。

`【口頭】` Lagrange 乘數其實帶有有用的資訊（例如**敏感度**：約束放鬆一點，最佳成本變多少），但本課只把它當工具。

**Q&A**

- `【Q&A】` [▶ 29:40](https://youtu.be/Izu4_AUiHyk?t=1780) 把解代回大寫 $L$ 會怎樣？→ 直覺上 Lagrangian 是「原成本＋約束懲罰」。在最小值處點是可行的，懲罰項為 0，$L$ 就等於原成本的最小值。
- `【Q&A】` [▶ 31:02](https://youtu.be/Izu4_AUiHyk?t=1862) 需要證明這是全域最小嗎？→ 這題可以：連續函數在緊緻集合（圓）上一定有最大、最小值，而它們都在 Lagrange 駐點裡，所以比一比就好。但不是總是這樣：就算無約束，若定義域有邊界，全域最小可能在**邊界**上，那裡梯度不必為 0。$\nabla f = 0$ 是必要條件的前提是點在定義域**內部**。

---

## 4. 最佳控制的必要條件

### 4.1 Hamiltonian 與協態

[▶ 32:45](https://youtu.be/Izu4_AUiHyk?t=1965)

類比 Lagrangian，定義 **Hamiltonian**：

$$
H\left( x, u, p, t \right) = g(x, u, t) + p^\top(t)\, a(x, u, t)
$$

- $g$ 對應有限維的 $f$（成本）。
- $a$ 是等式約束（運動方程）。
- $p(t)$ 扮演 Lagrange 乘數的角色，在最佳控制裡叫**協態（costate）**。兩個差別：名稱不同；而且它是**時間的函數**——原本的決策變數 $x, u$ 是函數，乘數也是函數很合理。

**必要條件**（老師不證明，課本稱 Pontryagin 最小原理）：

$$
\dot x^* = \frac{\partial H}{\partial p}, \qquad
\dot p^* = -\frac{\partial H}{\partial x}, \qquad
0 = \frac{\partial H}{\partial u}
$$

最後一條在無控制約束時成立；課本的一般形式是 $u^* = \arg\min_{u \in U} H(x^*, u, p^*, t)$。

做法和 Lagrange 一樣：解出 $x, u, p$，丟掉 $p$，剩下的是局部最佳的候選。麻煩的是：必要條件是一組**耦合的常微分方程**，不是代數方程。

**和 Lagrange 的相似處**：

1. $H$ 長得像 $L$：一項成本，一項懲罰「違反等式約束（運動方程）」。
2. `【課堂討論】` [▶ 36:33](https://youtu.be/Izu4_AUiHyk?t=2193) 對 $p$ 偏微分得到什麼？→ $a(x, u, t)$，所以 $\dot x = \partial H/\partial p$ 就是**運動方程**本身——正如 $\partial L/\partial\lambda = 0$ 就是約束。

### 4.2 方程與未知數的計數

[▶ 37:14](https://youtu.be/Izu4_AUiHyk?t=2234)

| | 有限維（Lagrange） | 最佳控制（Hamiltonian） |
|---|---|---|
| 未知數 | $x$：$n$ 個；$\lambda$：$m$ 個 → $n + m$ | $x(t)$：$n$ 個函數；$p(t)$：$n$ 個（每條狀態方程一個）；$u(t)$：$m$ 個 → $2n + m$ 個函數 |
| 方程 | $\partial L/\partial x$：$n$ 條；$\partial L/\partial\lambda$：$m$ 條 → $n + m$ | $\dot x$：$n$ 條 ODE；$\dot p$：$n$ 條 ODE；$\partial H/\partial u = 0$：$m$ 條代數方程 → $2n + m$ |

兩邊方程數都剛好等於未知數個數。

**但**：微分方程要有**邊界條件**才能定出積分常數。`【課堂討論】` [▶ 40:41](https://youtu.be/Izu4_AUiHyk?t=2441) 例如 $\dot x = x$ 的解是 $x = A e^t$，常數 $A$ 要靠初始條件定：$x(0) = A$。大致上每條一階 ODE 一個積分常數，所以這裡有 **$2n$ 個積分常數**。其中 $n$ 個來自初始條件 $x(t_0) = x_0$，另外 $n$ 個要從下面的主方程來。

### 4.3 邊界條件：主方程

[▶ 42:15](https://youtu.be/Izu4_AUiHyk?t=2535)

**主方程（老師稱 master equation）**（$h$ 是終端成本）：

$$
\left[ \frac{\partial h}{\partial x}\left( x^*(t_f), t_f \right) - p^*(t_f) \right]^\top \delta x_f
+ \left[ H\left( x^*(t_f), u^*(t_f), p^*(t_f), t_f \right) + \frac{\partial h}{\partial t}\left( x^*(t_f), t_f \right) \right] \delta t_f = 0
$$

- $\delta x_f$：終點狀態**允許的變化量**（終點固定 → 0；自由 → 任意）。
- $\delta t_f$：終端時間允許的變化量（固定時間，例如「10 秒後到」→ 0；自由，例如「越快越好」→ 任意）。

老師說這比較像記憶法而不是概念。用法：依情況代入 $\delta x_f$、$\delta t_f$：

**情況 1：$t_f$ 固定、$x_f$ 固定**（[▶ 45:00](https://youtu.be/Izu4_AUiHyk?t=2700)）。兩個變化量都是 0，主方程沒給資訊。但終點固定本身給了 $x(t_f) = x_f$，$n$ 條。合計 $n + n = 2n$ 條，剛好。

**情況 2：$t_f$ 自由、$x_f$ 固定**（[▶ 46:18](https://youtu.be/Izu4_AUiHyk?t=2778)，很常見：盡快到某點）。$\delta x_f = 0$，第一項消失；$\delta t_f$ 任意，要對所有 $\delta t_f$ 成立，係數必須為 0：

$$
H\left( x^*(t_f), u^*(t_f), p^*(t_f), t_f \right) + \frac{\partial h}{\partial t}\left( x^*(t_f), t_f \right) = 0
$$

加上 $x(t_0) = x_0$（$n$ 條）、$x(t_f) = x_f$（$n$ 條），共 $2n + 1$ 條。`【課堂討論】` 為什麼多一條？→ 因為 $t_f$ 也是未知數，要多一條方程定出最佳終端時間。

【課本補充】§2.2.3 列出全部四種情況：

| $t_f$ | $x(t_f)$ | 終端邊界條件 |
|---|---|---|
| 固定 | 固定 | $x^*(t_f) = x_f$ |
| 固定 | 自由 | $\frac{\partial h}{\partial x}(x^*(t_f), t_f) - p^*(t_f) = 0$ |
| 自由 | 固定 | $x^*(t_f) = x_f$，且 $H(t_f) + \frac{\partial h}{\partial t}(t_f) = 0$ |
| 自由 | 自由 | $\frac{\partial h}{\partial x} - p^*(t_f) = 0$（$n$ 條），且 $H(t_f) + \frac{\partial h}{\partial t} = 0$（1 條） |

---

## 5. 兩點邊界值問題與求解器

[▶ 49:08](https://youtu.be/Izu4_AUiHyk?t=2948)

平常碰到的多半是**初值問題**：所有條件都在起點（例如初始位置、初始速度）。最佳控制必要條件的解，有些條件在**起點**、有些在**終點**——這叫**兩點邊界值問題（TPBVP, two-point boundary value problem）**。`【口頭】` 「如果你覺得微分方程很難，這是吃了類固醇的難度。」要找的函數不只滿足微分方程，還要同時滿足兩端的條件。

幸好有求解器：Python 的 BVP solver（`scikits.bvp_solver`，作業最後一題用）；MATLAB 有 `bvp4c`（「但你們修這門課就不該用 MATLAB」）。

**示範（和最佳控制無關，只示範怎麼用）**（[▶ 51:18](https://youtu.be/Izu4_AUiHyk?t=3078)）：

$$
\dot z_1 = z_2, \qquad \dot z_2 = -\left| z_1 \right|, \qquad z_1(0) = 0, \qquad z_1(4) = -2
$$

> ⚠️ 待確認 [▶ 52:25](https://youtu.be/Izu4_AUiHyk?t=3145)：老師口頭說 $\dot z_2 = -|z_1|$，板書時寫成 $-z_1$，程式裡又是 $-|z_1|$。課本 §2.2.4 的同一個例子用 $\dot z_2 = -z_1$。

使用步驟（不抄程式）：

1. **寫微分方程的回呼函數**：傳回右手邊 $(z_2, -|z_1|)$。注意 Python 索引從 0 開始，$z_1$ 是 `z[0]`。
2. **寫邊界條件的殘差（residual）函數**：殘差 = 目前邊界值偏離邊界條件多少。把每個條件移項成「＝0」的形式：$z_1(0)$ 和 $z_1(4) + 2$。求解器會想辦法讓殘差變 0。
3. **定義問題**：幾條方程（2）、左邊界有幾個條件（1，所以右邊界也是 1）、積分區間 $[0, 4]$、上面兩個函數。
4. **給初始猜測**：通常給常數函數，例如 $z_1 \equiv 1$、$z_2 \equiv 0$；沒概念就給 0。
5. 呼叫求解器。

結果檢查：$\dot z_2 = -|z_1| \le 0$，所以 $z_2$ 一路下降；$z_1$ 的斜率和 $z_2$ 同號，$z_2 > 0$ 時上升、$z_2 < 0$ 時下降；兩端條件 $z_1(0) = 0$、$z_1(4) = -2$ 都滿足。

【課本補充】§2.2.4 介紹兩類數值方法：**打靶法（shooting）**——猜未知的邊界條件（例如初始協態），往前積分，反覆修正直到終點條件滿足；概念簡單，但時域長時數值不穩。**配置法（collocation）**——用參數化函數在一組配置點上近似解，變成大型非線性代數方程組；比較穩健，實務上常用。

---

## 6. 自由終端時間：時間重新縮放

[▶ 57:25](https://youtu.be/Izu4_AUiHyk?t=3445)

問題：幾乎所有 BVP 求解器都**假設 $t_f$ 已知**，但最佳控制常常 $t_f$ 是要最佳化的。

`【口頭】` 有一篇很好的文章整理了把「怪」兩點邊界值問題改寫成標準形式的各種技巧（課本 §2.2.4 引 Ascher 與 Russell）。最重要的就是處理自由 $t_f$，用的也是時間重新縮放。

**技巧**：

1. 引入新時間 $\tau = t / t_f$。不知道 $t_f$ 沒關係，反正 $t = t_f$ 時 $\tau = 1$，積分區間固定成 $[0, 1]$。
2. 把 $x(t)$ 看成 $x(\tau(t))$，連鎖律：

   $$
   \frac{dx}{dt} = \frac{dx}{d\tau}\frac{d\tau}{dt} = \frac{dx}{d\tau}\cdot\frac{1}{t_f}
   \quad\Longrightarrow\quad
   \frac{dx}{d\tau} = t_f\,\frac{dx}{dt}
   $$

   所以所有對 $t$ 的導數，換成對 $\tau$ 的導數時都**乘上 $t_f$**。
3. $t_f$ 是未知常數：加一個狀態變數 $r$，動態是平凡的 $\dot r = 0$，代表 $t_f$。求解器會自己找出讓邊界條件（包括主方程那條）成立的 $r$ 值。

---

## 7. 完整例子：雙積分器、最小化時間＋控制量

[▶ 61:07](https://youtu.be/Izu4_AUiHyk?t=3667)

**問題**（作業最後一題就是這種）：一個在直線上、有動量的質點（雙積分器 $\ddot x = u$），從 $x = 10$ 靜止出發，要停在原點：

$$
\min_{u,\ t_f}\ \frac12\alpha t_f^2 + \int_0^{t_f} \frac12\beta u^2\,dt
\quad\text{s.t. } \ddot x = u,\quad x(0) = 10,\ \dot x(0) = 0,\ x(t_f) = 0,\ \dot x(t_f) = 0
$$

成本是時間和控制量的組合（很常見），$t_f$ 自由。

> ⚠️ 待確認 [▶ 62:28](https://youtu.be/Izu4_AUiHyk?t=3748)：成本式子老師沒完整唸出；從後面「$h$ 對 $t$ 微分得 $\alpha t_f$」和 $H$ 裡的 $\frac12\beta u^2$ 推得終端成本是 $\frac12\alpha t_f^2$，與課本 Example 2.2.1 相同。

**Step 0：寫成一階系統。** 令 $x_1 = x$、$x_2 = \dot x$：

$$
\dot x_1 = x_2, \qquad \dot x_2 = u
$$

（標準技巧：二階 ODE 變成兩條一階 ODE。）兩條微分方程 → 兩個協態 $p_1, p_2$。

**Step 1：Hamiltonian。**

$$
H = \frac12\beta u^2 + p_1 x_2 + p_2 u
$$

**Step 2：必要條件。** $\partial H/\partial p$ 就是原動態，不重寫。

$$
\dot p_1 = -\frac{\partial H}{\partial x_1} = 0, \qquad
\dot p_2 = -\frac{\partial H}{\partial x_2} = -p_1, \qquad
\frac{\partial H}{\partial u} = \beta u + p_2 = 0 \;\Rightarrow\; u = -\frac{p_2}{\beta}
$$

代回去，得到 4 條 ODE：

$$
\dot x_1 = x_2, \qquad \dot x_2 = -\frac{p_2}{\beta}, \qquad \dot p_1 = 0, \qquad \dot p_2 = -p_1
$$

**Step 3：時間縮放。** 對 $\tau$ 的導數記為 $'$，每條都乘 $r$（$= t_f$），再加 $r' = 0$：

$$
x_1' = r\,x_2, \qquad x_2' = -r\,\frac{p_2}{\beta}, \qquad p_1' = 0, \qquad p_2' = -r\,p_1, \qquad r' = 0
$$

**Step 4：邊界條件。** 狀態給 4 條：

$$
x_1(0) = 10, \qquad x_2(0) = 0, \qquad x_1(1) = 0, \qquad x_2(1) = 0
$$

再從主方程（$t_f$ 自由、$x_f$ 固定 → 情況 2）：$\frac{\partial h}{\partial t} = \frac{\partial}{\partial t_f}\left( \frac12\alpha t_f^2 \right) = \alpha t_f$，所以

$$
\frac12\beta u(1)^2 + p_1(1)\,x_2(1) + p_2(1)\,u(1) + \alpha\, r = 0
$$

（把 $t_f$ 換成 $r$。）共 **5 條 ODE、5 個邊界條件**，積分區間 $[0, 1]$，可以丟給 BVP 求解器。

**程式結構**（[▶ 70:52](https://youtu.be/Izu4_AUiHyk?t=4252)，老師會放上程式碼）：狀態向量 $y = (x_1, x_2, p_1, p_2, r)$；$u = -y_3/\beta$（Python 索引）；每條動態乘上 $y_4$（即 $r$）；邊界條件函數放 4 條狀態條件和那條含 Hamiltonian 的「怪」條件。

**結果**（[▶ 72:48](https://youtu.be/Izu4_AUiHyk?t=4368)）：固定 $\beta$、改變 $\alpha$。$\alpha$ 越大 = 越在乎時間 → **到達時間 $t_f$ 越短**。這題其實有解析解（藍線），數值解（紅點）和它吻合，說明這個方法很準。

**演算法：間接法解最佳控制**

- **在解什麼**：求讓成本最小的開迴路控制 $u^*(t)$（可含自由 $t_f$）。
- **步驟**：
  1. 把動態寫成一階系統 $\dot x = a(x, u, t)$。
  2. 寫 $H = g + p^\top a$。
  3. 寫必要條件：$\dot x = \partial H/\partial p$、$\dot p = -\partial H/\partial x$、$\partial H/\partial u = 0$（解出 $u$ 用 $x, p$ 表示，代回去）。
  4. 由初始條件和主方程寫出 $2n$（或 $2n+1$）個邊界條件。
  5. $t_f$ 自由的話，做時間縮放 $\tau = t/t_f$，加狀態 $r$、$r' = 0$。
  6. 寫成標準形式交給 BVP 求解器（給合理的初始猜測）。
  7. 丟掉 $p$，得到候選的 $x^*(t)$、$u^*(t)$。
- **什麼時候會失敗**：
  - 兩點邊界值問題本身難解：求解器可能不收斂，對**初始猜測很敏感**（協態沒有物理直覺，很難猜）。
  - 只給**必要條件**：解出來的是候選，不保證是全域最小。
  - 有狀態約束、控制約束時，必要條件會複雜很多（本課不講）。
  - $\partial H/\partial u = 0$ 解不出 $u$ 的閉式時（或 $u$ 有上下限），要改用 $\arg\min_{u \in U} H$，更難處理。
  - 打靶法類的數值方法在長時域上可能不穩（課本）。

- `【Q&A】` [▶ 73:58](https://youtu.be/Izu4_AUiHyk?t=4438) Lagrange 法和 Hamiltonian 法的差別就在約束的種類？→ 對，前者是代數方程約束，後者是微分方程約束，所以必要條件要解微分方程。老師說先講有等式約束的最佳化，是為了讓 Hamiltonian 的條件看起來不那麼神祕。

---

## 8. 直接法與間接法的關係

[▶ 74:31](https://youtu.be/Izu4_AUiHyk?t=4471)

直接法把問題轉寫成有限維非線性最佳化（離散化運動方程和成本積分；第 3 集講過）。那它的解和間接法的解有什麼關係？

**關係**：對轉寫後的有限維問題寫出（Lagrange）必要條件，再讓時間步長 $h_i \to 0$，這些必要條件會**收斂到最佳控制問題的必要條件**（就是間接法用的那組）。

也就是說，走直接法的路，在步長很小時，它的必要條件就是間接法必要條件的離散版。`【口頭】` 這點常常沒人提，讓人以為兩種方法完全不同；其實它們緊密相連——本來就在解同一個問題。

`【口頭】` 考試範圍：**間接法會考（期中考）**；直接法和間接法的關係**不考**，只是補充。

下週：有約束（障礙物）的軌跡規劃 → 運動規劃演算法。

---

## 9. 一頁速查表

### 有限維

- 無約束：$\nabla f(x^*) = 0$（內部點的必要條件）。
- 等式約束：$L = f + \sum_i \lambda_i h_i$，$\partial L/\partial x = 0$、$\partial L/\partial\lambda = 0$（後者 = 原約束）。需正則點。
- 例：$\min x_1 + x_2$ s.t. $x_1^2 + x_2^2 = 2$ → $x_1 = x_2 = -\frac{1}{2\lambda}$、$\lambda = \pm\frac12$ → 最小值 $(-1, -1)$。

### 最佳控制（間接法）

$$
H = g + p^\top a, \qquad \dot x = \frac{\partial H}{\partial p}, \qquad \dot p = -\frac{\partial H}{\partial x}, \qquad \frac{\partial H}{\partial u} = 0
$$

- 計數：$2n + m$ 個未知函數 ＝ $2n$ 條 ODE ＋ $m$ 條代數方程；$2n$ 個積分常數。
- 主方程：$\left[ \frac{\partial h}{\partial x} - p \right]^\top_{t_f} \delta x_f + \left[ H + \frac{\partial h}{\partial t} \right]_{t_f} \delta t_f = 0$。

| $t_f$ | $x_f$ | 額外條件 |
|---|---|---|
| 固定 | 固定 | $x(t_f) = x_f$ |
| 固定 | 自由 | $p(t_f) = \partial h/\partial x$ |
| 自由 | 固定 | $x(t_f) = x_f$，$H(t_f) + \partial h/\partial t = 0$ |
| 自由 | 自由 | $p(t_f) = \partial h/\partial x$，$H(t_f) + \partial h/\partial t = 0$ |

### 自由 $t_f$ 的時間縮放

$\tau = t/t_f \in [0, 1]$，$\frac{dx}{d\tau} = t_f\frac{dx}{dt}$（關鍵：連鎖律）；加狀態 $r = t_f$，$r' = 0$。

### 雙積分器例子

$H = \frac12\beta u^2 + p_1 x_2 + p_2 u$ → $u = -p_2/\beta$、$\dot p_1 = 0$、$\dot p_2 = -p_1$；終端條件 $H(t_f) + \alpha t_f = 0$。$\alpha \uparrow$ ⇒ $t_f \downarrow$。

### 直接 vs. 間接

步長 → 0 時，直接法轉寫問題的必要條件 → 間接法的必要條件。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 有狀態約束的軌跡最佳化 | 第 6–7 集運動規劃 |
| 最佳控制、成本最小化 | 第 20 集決策（動態規劃、MDP） |
| 時間縮放技巧 | 第 4 集（同一個想法用在輸入上限） |
| Lagrange 乘數、有約束最佳化 | 之後相機校正等最佳化問題 |

---

## 附：本集一句話總結

> **間接法就是把 Lagrange 乘數法搬到函數空間：寫出 Hamiltonian $H = g + p^\top a$，必要條件變成一組狀態－協態微分方程，再加上由「主方程」決定的終端條件，就得到兩點邊界值問題；終端時間自由時用 $\tau = t/t_f$ 把區間固定成 $[0,1]$，就能丟給現成的 BVP 求解器。**

---

## ⚠️ 待確認清單

1. 上課日期待補（只知道是週五）。
2. [▶ 52:25](https://youtu.be/Izu4_AUiHyk?t=3145) BVP 示範的第二條方程是 $-|z_1|$ 還是 $-z_1$：老師口頭、板書不一致，課本用 $-z_1$。
3. [▶ 62:28](https://youtu.be/Izu4_AUiHyk?t=3748) 雙積分器例子的終端成本 $\frac12\alpha t_f^2$ 是由後續推導反推的，投影片原式沒唸出。

---

*筆記依據 Marco Pavone（推斷）「Stanford AA274A Principles of Robotic Autonomy（2019 秋）」Lecture 5 錄影逐字稿（Whisper `medium.en`，1:17:45）與《Principles of Robot Autonomy》§2.2 整理。*
