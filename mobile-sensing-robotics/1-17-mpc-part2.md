---
course: Mobile Sensing and Robotics 1（Uni Bonn, Winter 2021/22）
episode: 1-17
lecture: Model Predictive Control – Part 2: Numerical Methods for MPC
date: 待補（2021/22 冬季學期）
video: https://youtu.be/TtGCEzYxM_A
notes: 《Probabilistic Robotics》沒有對應章節；只用逐字稿
---

# 第 1-17 集 · 模型預測控制（二）：MPC 的數值方法 [▶ 影片](https://youtu.be/TtGCEzYxM_A)

← 上一集：[1-16-mpc-part1](1-16-mpc-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[1-18-astar-planning](1-18-astar-planning.md) →

> **課程**：Mobile Sensing and Robotics 1，Uni Bonn，2021/22 冬季學期 — 第 1-17 集
> **講者**：Lasse Peters（開頭自我介紹）
> **來源**：YouTube 錄影逐字稿（1:12:37，Whisper `medium.en` 轉錄）。課本沒有這個主題，沒有次要來源。
> **標記說明**：
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單
>
> 本集很多公式在投影片上、逐字稿只有口述。凡是筆記自己寫出的矩陣與推導步驟，都會註明「以下不是逐字稿內容」。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：MPC 與內層的最佳化](#1-複習mpc-與內層的最佳化)
- [2. 簡化問題](#2-簡化問題)
- [3. 狀態消去：前向模擬](#3-狀態消去前向模擬)
- [4. LQR：線性動力學＋二次代價](#4-lqr線性動力學二次代價)
- [5. LQR 的批次解](#5-lqr-的批次解)
- [6. 最佳性原理與動態規劃](#6-最佳性原理與動態規劃)
- [7. LQR 的動態規劃解](#7-lqr-的動態規劃解)
  - [7.1 最後一步](#71-最後一步)
  - [7.2 往回一步：回饋增益](#72-往回一步回饋增益)
  - [7.3 往回一步：代價矩陣](#73-往回一步代價矩陣)
  - [7.4 演算法與比較](#74-演算法與比較)
- [8. 迭代 LQR（iLQR）](#8-迭代-lqrilqr)
  - [8.1 想法](#81-想法)
  - [8.2 演算法步驟](#82-演算法步驟)
  - [8.3 實務一：正則化](#83-實務一正則化)
  - [8.4 實務二：線搜尋](#84-實務二線搜尋)
  - [8.5 評論](#85-評論)
- [9. 總結與延伸閱讀](#9-總結與延伸閱讀)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

1-16 假設有工具（CasADi、JuMP）幫我們解 MPC 裡的最佳化問題。這集掀開黑盒子：

1. **狀態消去**：把有限制的問題變成無限制問題。
2. **LQR**（線性＋二次）兩種解法：**批次解**（一個大的最小平方）和**動態規劃**（逐步往回算）。
3. **迭代 LQR**（iLQR）：把非線性問題一再近似成 LQR 來解。

---

## 1. 複習：MPC 與內層的最佳化

[▶ 00:27](https://youtu.be/TtGCEzYxM_A?t=27)

- 每一刻看目前狀態，用模型規劃未來有限步（例如 20、30 或 50 步），最小化目標（例如偏離參考線少、沿賽道前進多）。
- 只執行第一個輸入，再重來。
- 本集重點：裡面那個**最佳化器**。

內層問題（預測時域 $T$）[▶ 02:54](https://youtu.be/TtGCEzYxM_A?t=174)：

$$
\begin{aligned}
\min_{x_{1:T},\, u_{1:T}}\quad & J(x_{1:T}, u_{1:T}) \\
\text{s.t.}\quad & x_{t+1} = f(x_t, u_t) && \text{（動力學可行，等式限制）} \\
& x_t \in \mathcal X,\; u_t \in \mathcal U && \text{（狀態、輸入限制）} \\
& x_1 = x_{\text{init}} && \text{（初始狀態）}
\end{aligned}
$$

- 動力學可行：例如車可以轉向、前後加速，但不能立刻橫移（輪胎不允許）。
- $x_{1:T}$、$u_{1:T}$ 表示所有狀態、輸入組成的序列。

---

## 2. 簡化問題

[▶ 06:21](https://youtu.be/TtGCEzYxM_A?t=381)

為了這集的範圍：

1. **拿掉**狀態和輸入限制 $\mathcal X$、$\mathcal U$，只留初始條件和動力學限制。
2. 假設目標是**時間可分離**的 [▶ 07:06](https://youtu.be/TtGCEzYxM_A?t=426)：

$$
J(x_{1:T}, u_{1:T}) = \sum_{t=1}^{T} g(x_t, u_t)
$$

這個假設對後面的工具很重要。

---

## 3. 狀態消去：前向模擬

[▶ 08:00](https://youtu.be/TtGCEzYxM_A?t=480)

**想法**：每個狀態都由前一個狀態透過動力學決定。初始狀態已知，所以所有未來狀態都可以寫成**控制的函數** → 只留控制當決策變數。

$$
\begin{aligned}
x_1 &= x_{\text{init}} \\
x_2 &= f(x_{\text{init}}, u_1) \\
x_3 &= f\bigl(f(x_{\text{init}}, u_1),\, u_2\bigr) \\
&\;\;\vdots
\end{aligned}
$$

定義**前向模擬函數** $F_t$ [▶ 10:21](https://youtu.be/TtGCEzYxM_A?t=621)：從時間 $t$ 的狀態出發、依序（開迴路）施加 $u_t, \dots, u_T$，得到的整條軌跡。$F_1(x_{\text{init}}, u_{1:T})$ 就是整條軌跡 $x_{1:T}$。

**改寫目標** [▶ 11:13](https://youtu.be/TtGCEzYxM_A?t=673)：

$$
\tilde J(u_{1:T};\, x_{\text{init}}) = J\bigl(F_1(x_{\text{init}}, u_{1:T}),\; u_{1:T}\bigr)
$$

$$
\min_{u_{1:T}} \tilde J(u_{1:T};\, x_{\text{init}})
$$

好處：

- 決策變數變少：只剩 $u_{1:T}$（$x_{\text{init}}$ 是固定的，不是決策變數）。
- **沒有限制**：初始條件和動力學限制都自動滿足，因為前向模擬一定產生動力學可行的狀態。

結果是一個**無限制最佳化問題**：一個代價地形（cost landscape），要找最低點 [▶ 13:07](https://youtu.be/TtGCEzYxM_A?t=787)。

- 一般**無法解析求解**，要用**迭代**方法：例如梯度下降（往負梯度方向走小步，找到局部最小值）或牛頓法。

**特例：凸二次代價** [▶ 14:16](https://youtu.be/TtGCEzYxM_A?t=856)：代價只到決策變數的平方項（多維是二次曲面，一維是拋物線），而且開口向上 → 可以**解析**求最小值：令梯度為零，直接跳到全域最小值。

---

## 4. LQR：線性動力學＋二次代價

[▶ 15:23](https://youtu.be/TtGCEzYxM_A?t=923)

**線性二次調節器**（linear quadratic regulator, LQR）：最佳控制問題的特例，動力學**線性**、代價**二次**。

$$
\begin{aligned}
\min_{x_{1:T},\, u_{1:T}}\quad & \sum_{t=1}^{T} \bigl( x_t^{\mathsf T} Q\, x_t + u_t^{\mathsf T} R\, u_t \bigr) \\
\text{s.t.}\quad & x_{t+1} = A\, x_t + B\, u_t \\
& x_1 = x_{\text{init}}
\end{aligned}
$$

- $x_t^{\mathsf T} Q x_t$：罰狀態**離原點**的偏差。
- $u_t^{\mathsf T} R u_t$：罰任何非零輸入。

**假設** [▶ 16:47](https://youtu.be/TtGCEzYxM_A?t=1007)：

| 矩陣 | 條件 | 意思 |
|---|---|---|
| $Q$ | 對稱、**半正定**（$Q = Q^{\mathsf T}$，特徵值 $\ge 0$） | — |
| $R$ | **正定**（特徵值 $> 0$） | 任何非零輸入都有正代價 |

（注意：這裡的 $Q$、$R$ 是代價權重，不是 1-10 Kalman 濾波的雜訊共變異數。）

---

## 5. LQR 的批次解

[▶ 17:21](https://youtu.be/TtGCEzYxM_A?t=1041)

**批次解**（batch solution）：用狀態消去，一次解出**整個時域**的所有控制。結果是一個線性最小平方問題。

**線性動力學的前向模擬** [▶ 17:51](https://youtu.be/TtGCEzYxM_A?t=1071)：

$$
x_1 = x_{\text{init}}, \qquad
x_2 = A x_{\text{init}} + B u_1, \qquad
x_3 = A(A x_{\text{init}} + B u_1) + B u_2 = A^2 x_{\text{init}} + AB u_1 + B u_2
$$

每一步都是「前一個式子左乘 $A$、再加上 $B u$」。一般地：

$$
x_t = A^{t-1} x_{\text{init}} + \sum_{j=1}^{t-1} A^{t-1-j} B\, u_j
$$

**堆疊成一個矩陣式** [▶ 18:53](https://youtu.be/TtGCEzYxM_A?t=1133)：把所有狀態疊成長向量 $X$、所有輸入疊成 $U$：

$$
X = \bar A\, x_{\text{init}} + \bar B\, U
$$

講者說可以自己確認這個矩陣式和逐步式一樣：例如 $x_1$ 是單位矩陣乘 $x_{\text{init}}$、其餘為零（沒施加輸入）；$x_2$ 是 $A x_{\text{init}} + B u_1$，其他 $u$ 都乘零。

以下**不是逐字稿內容**，是依上面的一般式寫出的 $\bar A$、$\bar B$（投影片上的矩陣逐字稿看不到）：

$$
\bar A = \begin{bmatrix} I \\ A \\ A^2 \\ \vdots \\ A^{T-1} \end{bmatrix}, \qquad
\bar B = \begin{bmatrix}
0 & 0 & \cdots & 0 & 0 \\
B & 0 & \cdots & 0 & 0 \\
AB & B & \cdots & 0 & 0 \\
\vdots & & \ddots & & \vdots \\
A^{T-2}B & A^{T-3}B & \cdots & B & 0
\end{bmatrix}
$$

（$\bar B$ 是下三角的分塊矩陣；最後一欄全為 0，因為 $u_T$ 不影響時域內的任何狀態。）

**堆疊的代價矩陣** [▶ 20:18](https://youtu.be/TtGCEzYxM_A?t=1218)：

$$
\bar Q = \operatorname{blockdiag}(Q, \dots, Q), \qquad \bar R = \operatorname{blockdiag}(R, \dots, R)
$$

$$
\bar J = X^{\mathsf T} \bar Q\, X + U^{\mathsf T} \bar R\, U
$$

看起來像單一時刻的代價，但代表**整個時域**的總代價。

**代入前向模擬** [▶ 21:43](https://youtu.be/TtGCEzYxM_A?t=1303)：把 $X$ 換成 $\bar A x_{\text{init}} + \bar B U$，整理後是 $U$ 的二次式：

$$
\tilde J(U) = U^{\mathsf T} H\, U + (\text{一次項}) + (\text{常數})
$$

以下**不是逐字稿內容**，是筆記展開的：

$$
\begin{aligned}
\tilde J(U) &= (\bar A x_{\text{init}} + \bar B U)^{\mathsf T} \bar Q (\bar A x_{\text{init}} + \bar B U) + U^{\mathsf T} \bar R U \\
&= U^{\mathsf T} \underbrace{(\bar B^{\mathsf T} \bar Q \bar B + \bar R)}_{H} U + 2\, x_{\text{init}}^{\mathsf T} \bar A^{\mathsf T} \bar Q \bar B\, U + x_{\text{init}}^{\mathsf T} \bar A^{\mathsf T} \bar Q \bar A\, x_{\text{init}}
\end{aligned}
$$

$H$ 和 $\bar R$ 一樣大（$mT \times mT$，$m$ = 輸入維度）。

**凸性** [▶ 23:39](https://youtu.be/TtGCEzYxM_A?t=1419)：$H$ 依構造是**正定**的（$R$ 正定、$Q$ 半正定）。

（理由，不是逐字稿內容：對任何 $U \ne 0$，$U^{\mathsf T} \bar B^{\mathsf T} \bar Q \bar B U = (\bar B U)^{\mathsf T} \bar Q (\bar B U) \ge 0$，而 $U^{\mathsf T} \bar R U > 0$，所以 $U^{\mathsf T} H U > 0$。）

所以代價地形開口向上，令梯度為零就得到全域最小值：

$$
\nabla_U \tilde J = 2 H U + 2 \bar B^{\mathsf T} \bar Q \bar A\, x_{\text{init}} = 0
\quad\Rightarrow\quad
U^* = -H^{-1} \bar B^{\mathsf T} \bar Q \bar A\, x_{\text{init}}
$$

（梯度和 $U^*$ 的式子是筆記依上面展開式算的；講者只說「令梯度為零，要用到 $H$ 的反矩陣」。）

**評論** [▶ 25:25](https://youtu.be/TtGCEzYxM_A?t=1525)：

- 優點：凸二次 → **解析解**，只要解一個線性方程組，比慢慢走向局部解有效率得多，而且是**全域**最佳。
- 缺點：要對 $mT \times mT$ 的大矩陣 $H$ 求反。時域 $T$ 很長時很貴。
- 能更好嗎？可以：**動態規劃**。

---

## 6. 最佳性原理與動態規劃

[▶ 26:27](https://youtu.be/TtGCEzYxM_A?t=1587)

利用動力學造成的**序列結構**，不只用來做前向模擬，也用來更有效率地「求 $H$ 的反矩陣」。

**最佳性原理**（principle of optimality）[▶ 27:18](https://youtu.be/TtGCEzYxM_A?t=1638)：

- 例子：從 A 到 C 的最佳路線經過 B。那麼這條路線的**尾段**（B → C）也一定是從 B 到 C 的最佳路線。
- 反證：如果 B → C 有另一條更便宜的路（灰色），那從 A 出發也會改走灰色那段，原本的路線就不是最佳了。矛盾。

**正式寫法** [▶ 29:04](https://youtu.be/TtGCEzYxM_A?t=1744)：若 $u_{1:T}^*$ 是最佳控制序列、產生狀態軌跡 $x^*$，則任何尾段 $u_{t:T}^*$ 也是以下**尾問題**的最佳解：

$$
\min_{u_{t:T}} J_t = \sum_{\tau = t}^{T} g(x_\tau, u_\tau)
\quad \text{s.t. 動力學},\; x_t = x_t^*
$$

$J_t$ 叫 **cost-to-go**（從 $t$ 到結束的代價）。

### 動態規劃的做法

[▶ 30:22](https://youtu.be/TtGCEzYxM_A?t=1822)

- 把問題拆成一連串比較好解的**尾問題**，從後面往前解。
- 例子：要到 C，但**不知道從哪裡出發**。
  1. 從 C 往回到某個中間時刻 $t$，**列舉**那時可能在的所有狀態；對每個狀態解「從這裡到 C」的最佳控制。
  2. 這時的控制不是一串固定數字，而是**狀態的函數**（要對所有可能狀態都算）。
  3. 同時記下**最佳 cost-to-go** $J_t^*(x)$：從這個狀態出發、照最佳方式走，還要付多少代價。例子裡三個狀態分別是 10、1、4。
- 再往回一步 [▶ 32:45](https://youtu.be/TtGCEzYxM_A?t=1965)：對更早時刻的每個狀態，最小化「到時刻 $t$ 的立即代價 + 從那裡開始的最佳 cost-to-go」。
  - 例：某條路到 B 可能代價較高，但 B 的 cost-to-go 很小，所以值得。
  - cost-to-go 很高的狀態（例子裡上面那個），就算很便宜就能到，也沒有人選它。
- 得到的是**回饋策略**（feedback strategy）：狀態 → 控制。代入初始狀態 A，就還原出原本的計畫 [▶ 34:24](https://youtu.be/TtGCEzYxM_A?t=2064)。

**看起來是壞主意？** [▶ 34:57](https://youtu.be/TtGCEzYxM_A?t=2097)

- 要對**所有**可能狀態都解，需要能把 $J_t^*$ 表示成狀態的函數。
- 天真做法：把狀態空間切成小格，每格解一次最佳控制，存成查表。
- 問題：要解的問題數**隨狀態維度指數成長**，還要決定怎麼離散化。
- 好消息：**LQR 是特例**，cost-to-go 和回饋策略都有封閉形式，算起來很有效率。

---

## 7. LQR 的動態規劃解

[▶ 37:03](https://youtu.be/TtGCEzYxM_A?t=2223)

### 7.1 最後一步

[▶ 37:21](https://youtu.be/TtGCEzYxM_A?t=2241)

最小的尾問題：只看最後一個時刻 $T$。

$$
\min_{u_T} \bigl( x_T^{\mathsf T} Q\, x_T + u_T^{\mathsf T} R\, u_T \bigr)
$$

- $x_T$ 給定（對這個最佳化來說是常數），只有一個決策變數 $u_T$。
- $R$ 正定 → 任何非零輸入都有正代價 → 最好就是**不施加輸入**：$u_T^* = 0$。（實務上常直接把最後一步的輸入拿掉，因為它一定是 0。）
- 最佳 cost-to-go：代入 $u_T = 0$：

$$
J_T^*(x) = x^{\mathsf T} P_T\, x, \qquad P_T = Q
$$

$P$ 是**要算出來**的 cost-to-go 矩陣；$Q$ 是題目**給定**的。

### 7.2 往回一步：回饋增益

[▶ 39:40](https://youtu.be/TtGCEzYxM_A?t=2380)

往回一步：最小化「現在的立即代價 + 下一步的最佳 cost-to-go」：

$$
\min_{u_{t},\, x_{t+1}} \Bigl( x_t^{\mathsf T} Q x_t + u_t^{\mathsf T} R u_t + J_{t+1}^*(x_{t+1}) \Bigr)
\quad \text{s.t.}\quad x_{t+1} = A x_t + B u_t
$$

1. 用同樣的前向模擬技巧把 $x_{t+1}$ 換成 $A x_t + B u_t$ → 只剩 $u_t$、沒有限制 [▶ 41:05](https://youtu.be/TtGCEzYxM_A?t=2465)。
2. 代入已知的 $J_{t+1}^*(x) = x^{\mathsf T} P_{t+1} x$：

$$
\min_{u_t} \Bigl( x_t^{\mathsf T} Q x_t + u_t^{\mathsf T} R u_t + (A x_t + B u_t)^{\mathsf T} P_{t+1} (A x_t + B u_t) \Bigr)
$$

3. 整理成：$x$ 的平方項、$u$ 的平方項、交叉項 [▶ 42:03](https://youtu.be/TtGCEzYxM_A?t=2523)。以下展開**不是逐字稿內容**：

$$
x_t^{\mathsf T}(Q + A^{\mathsf T} P_{t+1} A) x_t + u_t^{\mathsf T}(R + B^{\mathsf T} P_{t+1} B) u_t + 2\, u_t^{\mathsf T} B^{\mathsf T} P_{t+1} A\, x_t
$$

4. 對 $u_t$ 來說：第一項是常數、最後一項是一次項、中間是二次項。$R + B^{\mathsf T} P_{t+1} B$ 是「正定 + 半正定 = 正定」[▶ 42:31](https://youtu.be/TtGCEzYxM_A?t=2551) → 凸二次 → 令梯度為零：

$$
2(R + B^{\mathsf T} P_{t+1} B)\, u_t + 2 B^{\mathsf T} P_{t+1} A\, x_t = 0
$$

5. 解出 $u_t^*$，是狀態的**線性回饋** [▶ 43:31](https://youtu.be/TtGCEzYxM_A?t=2611)：

$$
\boxed{\;u_t^* = F_t\, x_t, \qquad F_t = -\bigl(R + B^{\mathsf T} P_{t+1} B\bigr)^{-1} B^{\mathsf T} P_{t+1} A\;}
$$

- 看到反矩陣就要問：能安全求反嗎？上面已確認它是正定的，可以 [▶ 44:01](https://youtu.be/TtGCEzYxM_A?t=2641)。
- 得到的回饋控制器可以在**任意狀態**求值：狀態乘上這個矩陣。

（第 4、5 步的梯度和 $F_t$ 式子是筆記依第 3 步的展開算的；講者說「把 $u^*$ 移到左邊整理」，公式在投影片上。）

### 7.3 往回一步：代價矩陣

[▶ 44:29](https://youtu.be/TtGCEzYxM_A?t=2669)

把 $u_t^* = F_t x_t$ 代回代價，得到的最佳 cost-to-go 還是狀態的二次式：

$$
J_t^*(x) = x^{\mathsf T} P_t\, x
$$

而且 $P_t$ 仍然**半正定**（由 $R$ 正定、$Q$ 半正定推得）[▶ 45:30](https://youtu.be/TtGCEzYxM_A?t=2730)。

以下**不是逐字稿內容**，是筆記代入展開的。代入 $u = F x$：

$$
P_t = Q + F_t^{\mathsf T} R F_t + (A + B F_t)^{\mathsf T} P_{t+1} (A + B F_t)
$$

（每一項都是半正定矩陣的「夾心」，所以 $P_t$ 半正定。）再用 $(R + B^{\mathsf T} P_{t+1} B) F_t = -B^{\mathsf T} P_{t+1} A$ 化簡，得到常見的 **Riccati 遞迴**：

$$
P_t = Q + A^{\mathsf T} P_{t+1} A - A^{\mathsf T} P_{t+1} B \bigl(R + B^{\mathsf T} P_{t+1} B\bigr)^{-1} B^{\mathsf T} P_{t+1} A
$$

（化簡步驟：展開第一式得 $Q + A^{\mathsf T} P A + F^{\mathsf T}(R + B^{\mathsf T} P B) F + F^{\mathsf T} B^{\mathsf T} P A + A^{\mathsf T} P B F$；把 $(R + B^{\mathsf T} P B)F = -B^{\mathsf T} P A$ 代入第三項，它等於 $-F^{\mathsf T} B^{\mathsf T} P A$，和第四項抵消；剩下 $A^{\mathsf T} P B F = -A^{\mathsf T} P B (R + B^{\mathsf T} P B)^{-1} B^{\mathsf T} P A$。）

### 7.4 演算法與比較

[▶ 45:59](https://youtu.be/TtGCEzYxM_A?t=2759)

```
Algorithm LQR_dynamic_programming(A, B, Q, R, T):
  P_T = Q
  for t = T-1 down to 1 do
    F_t = -(R + Bᵀ P_{t+1} B)⁻¹ Bᵀ P_{t+1} A
    P_t = Q + F_tᵀ R F_t + (A + B F_t)ᵀ P_{t+1} (A + B F_t)
  endfor
  return {F_t}                     // 執行時：u_t = F_t x_t
```

（講者說從最後一刻 $P_T = Q$ 開始，用剛推出的兩條式子一路往回遞迴。）

**小結** [▶ 47:22](https://youtu.be/TtGCEzYxM_A?t=2842)：把一個大的批次問題拆成 $T$ 個很小的**一步**最佳化，遞迴地一次算一個時刻的回饋策略。

| | 批次解 | 動態規劃 |
|---|---|---|
| 要求反的矩陣 | 一個 $mT \times mT$ | $T$ 個 $m \times m$ |
| 和時域 $T$ 的關係 | 矩陣隨 $T$ 變大 | 矩陣大小**固定**，總成本**線性**於 $T$ |
| 得到的 | 一串控制值（只對特定初始狀態有效，開迴路） | **回饋策略**，任意狀態都能求值 |

**回饋策略的好處** [▶ 49:10](https://youtu.be/TtGCEzYxM_A?t=2950)：能補償誤差。如果實際狀態偏了一點，不用重新解整個最佳化，只要在新的狀態估計上求值。

---

## 8. 迭代 LQR（iLQR）

### 8.1 想法

[▶ 49:39](https://youtu.be/TtGCEzYxM_A?t=2979)

- 處理**非線性**動力學、**非二次**代價。
- 想法：在目前的**操作點**把原問題局部近似成 LQR，解這個 LQR，往那個方向走一步，重複。
- 一維圖解 [▶ 50:32](https://youtu.be/TtGCEzYxM_A?t=3032)：
  - LQR 時可以直接算出全域最小值。
  - 非二次代價不能解析解。但可以在操作點（紅點）做**泰勒展開**，得到二次近似 → 一個 LQR → 解析解出它的最小值 → 走過去。
  - 新操作點再做二次近似、再走……重複夠多次就到一個**局部**最小值（可能不是全域的，例子裡另一邊還有一個更低的）。
- 這其實是**牛頓法**的特例，利用了最佳控制問題的特殊結構 [▶ 52:19](https://youtu.be/TtGCEzYxM_A?t=3139)。

### 8.2 演算法步驟

[▶ 52:39](https://youtu.be/TtGCEzYxM_A?t=3159)

**1. 初始猜測**：一串控制 $\bar u_{1:T}$，例如「慢慢往前開」。

**2. Rollout**：從初始狀態用前向模擬得到對應的狀態 $\bar x_{1:T}$（不是最佳的，只是某組控制的結果）。

**3. 線性化動力學** [▶ 53:44](https://youtu.be/TtGCEzYxM_A?t=3224)：在操作點 $(\bar x_t, \bar u_t)$ 做一階泰勒展開。把座標移到操作點：

$$
\delta x_t = x_t - \bar x_t, \qquad \delta u_t = u_t - \bar u_t
$$

$$
\delta x_{t+1} \approx A_t\, \delta x_t + B_t\, \delta u_t, \qquad
A_t = \left.\frac{\partial f}{\partial x}\right|_{\bar x_t, \bar u_t}, \quad
B_t = \left.\frac{\partial f}{\partial u}\right|_{\bar x_t, \bar u_t}
$$

- 這個仿射近似在操作點上完全吻合，離越遠可能偏越多。
- $A_t$：狀態稍微不同時，下一個狀態怎麼變（對 $x$ 的 Jacobian）。$B_t$：對 $u$ 的 Jacobian。
- （為什麼常數項消失，不是逐字稿內容：$\bar x_{t+1} = f(\bar x_t, \bar u_t)$ 本來就是 rollout 的結果，所以 $f(x_t, u_t) - \bar x_{t+1} \approx A_t \delta x_t + B_t \delta u_t$。）

**4. 二次近似代價** [▶ 56:25](https://youtu.be/TtGCEzYxM_A?t=3385)：在操作點擬合一個二次函數，讓**值**、**斜率**、**曲率**都和原代價吻合（二階泰勒展開）。寫成 $\delta x$、$\delta u$ 的函數，會有：

- 已經會處理的二次項（像 LQR 的 $Q$、$R$）；
- **額外的一次項**和常數。

講者說各項怎麼算「不細講」，就是泰勒展開。以下**不是逐字稿內容**，是二階泰勒展開的一般形式（下標代表偏導數）：

$$
g(\bar x + \delta x, \bar u + \delta u) \approx g + g_x^{\mathsf T}\delta x + g_u^{\mathsf T}\delta u + \tfrac12 \delta x^{\mathsf T} g_{xx} \delta x + \tfrac12 \delta u^{\mathsf T} g_{uu} \delta u + \delta u^{\mathsf T} g_{ux} \delta x
$$

**5. 擴充狀態把一次項塞進二次式** [▶ 57:55](https://youtu.be/TtGCEzYxM_A?t=3475)：

$$
z_t = \begin{bmatrix} \delta x_t \\ 1 \end{bmatrix}, \qquad
v_t = \begin{bmatrix} \delta u_t \\ 1 \end{bmatrix}
$$

- 動力學：$A_t$ 放在分塊對角矩陣的左上角，$B_t$ 下面補零。講者說可以自己確認它表示同樣的動力學。
- 代價：原本的一次項（仿射項）可以放進擴充後二次代價矩陣的非對角區塊；控制代價同理。
- 結果是**標準 LQR**，可以用批次或動態規劃解。

（為什麼可以，不是逐字稿內容：$\begin{bmatrix}\delta x \\ 1\end{bmatrix}^{\mathsf T}\begin{bmatrix} M & m \\ m^{\mathsf T} & c\end{bmatrix}\begin{bmatrix}\delta x \\ 1\end{bmatrix} = \delta x^{\mathsf T} M \delta x + 2 m^{\mathsf T}\delta x + c$，所以一次項 $g_x^{\mathsf T}\delta x$ 可以用 $m = \tfrac12 g_x$ 表示。交叉項 $g_{ux}$ 怎麼處理講者沒提，**待補**。）

**6. 解 LQR，往解的方向走一步** [▶ 59:32](https://youtu.be/TtGCEzYxM_A?t=3572)：得到局部近似的全域最佳 $\delta u^*$，更新：

$$
\bar u \leftarrow \bar u + \alpha\, \delta u^*, \qquad 0 < \alpha \le 1
$$

$\alpha = 1$ 就是直接走到近似問題的最小值；實務上可能走小一點（見 8.4）。

**7. 重複**：用新的控制再 rollout、再近似、再解……直到操作點**收斂**（相鄰兩次迭代的狀態不再改變）。

### 8.3 實務一：正則化

[▶ 1:01:12](https://youtu.be/TtGCEzYxM_A?t=3672)

- LQR 的推導假設 $R$ 正定、$P$ 半正定，所以 $R + B^{\mathsf T} P B$ 正定。
- 但在 iLQR 裡，這些矩陣不是我們選的，是從局部近似算出來的，不保證滿足。
- 問題：
  - 某個操作點的二次近似**沒有曲率** → 矩陣有零特徵值 → **不可逆**。
  - 更糟：在**極大值**附近，二次近似開口向下 → 令梯度為零找到的是**最大值**，更新方向是錯的。
- **正則化**（regularization）[▶ 1:02:55](https://youtu.be/TtGCEzYxM_A?t=3775)：加上一個縮放的單位矩陣：

$$
R + B^{\mathsf T} P B + \rho I
$$

  $\rho$ 要選得夠大，讓局部近似開口向上（把近似在這一點「往上彎」）→ 所有特徵值為正、可逆，而且往正確方向走。

### 8.4 實務二：線搜尋

[▶ 1:04:23](https://youtu.be/TtGCEzYxM_A?t=3863)

步長 $\alpha$ 的取捨：

- 大步：往目標前進多。
- 但泰勒近似只在操作點**附近**有效，走太遠模型就不準。
- 例：原代價因為強烈的非線性很快往上翹，但局部近似預測最小值在遠處。直接走 $\alpha = 1$，代價反而**增加** → 傷害收斂，甚至找不到局部最小值。

**線搜尋**（line search）[▶ 1:06:17](https://youtu.be/TtGCEzYxM_A?t=3977)：自適應地找好的 $\alpha$，方法是試不同的步長。

**回溯線搜尋**（backtracking line search）：

1. 試 $\alpha = 1$ → 代價增加，不接受。
2. 減半 $\alpha = 1/2$ → 不用重新算近似（LQR 問題不變），只要重新算代價。比較近了，但代價**下降得不夠多**（和原來差不多），仍不接受。
3. 再減半 $\alpha = 1/4$ → 步子小，但很接近局部最小值，代價有**足夠下降** → 接受。

只接受讓代價**顯著下降**的步子。

### 8.5 評論

[▶ 1:07:50](https://youtu.be/TtGCEzYxM_A?t=4070)

- **小結**：從初始控制出發，在對應操作點把非線性最佳控制問題近似成 LQR、解它、往解走一步，重複到收斂。
- 在機器人學裡是**有效率、很成熟**的非線性最佳控制演算法。
- 問題**夠平滑**時效果特別好；非線性很強、甚至有**接觸**（contact）時，泰勒展開不準，效果較差。自駕車這類問題很適合。
- 正則化和線搜尋對可靠性非常重要：沿賽道跑的機器人不能偶爾讓代價變大。
- 可以延伸處理**不等式限制**：例如**懲罰法**（penalty method），把限制寫成額外的代價項，並自適應地估計它們的權重 [▶ 1:09:29](https://youtu.be/TtGCEzYxM_A?t=4169)。

---

## 9. 總結與延伸閱讀

[▶ 1:09:57](https://youtu.be/TtGCEzYxM_A?t=4197)

1. 複習 MPC → 動機：內層的最佳化怎麼解。
2. 用前向模擬消去狀態變數和動力學限制 → 無限制最佳化。
3. LQR（線性＋二次）：
   - **批次解**：前向模擬 → 一個大的線性最小平方問題。
   - **動態規劃**：遞迴、很有效率，還給出回饋策略。
4. **iLQR**：把非線性問題反覆近似成局部 LQR，找到步進方向，走向局部最小值。

**延伸閱讀** [▶ 1:11:47](https://youtu.be/TtGCEzYxM_A?t=4307)：

- Francesco Borrelli 等《Predictive Control for Linear and Hybrid Systems》；Berkeley 的 MPC 課程材料。
- 數值背景、實務技巧、收斂保證：Nocedal & Wright《Numerical Optimization》。
- 最佳控制、軌跡最佳化、程式練習：MIT Russ Tedrake 的 Underactuated Robotics 課程。
- `⚠️ 待確認`：Whisper 寫 “Francesco Urelli”、“Notre-Dame and Wright”、“Russ Tedrick”，人名依發音推測。

---

## 10. 一頁速查表

### 10.1 狀態消去

| 項 | 公式 |
|---|---|
| 前向模擬 | $x_1 = x_{\text{init}}$，$x_{t+1} = f(x_t, u_t)$ |
| 無限制問題 | $\min_{u_{1:T}} \tilde J(u_{1:T}) = J(F_1(x_{\text{init}}, u_{1:T}), u_{1:T})$ |
| 線性情況 | $x_t = A^{t-1}x_{\text{init}} + \sum_{j<t} A^{t-1-j} B u_j$，$X = \bar A x_{\text{init}} + \bar B U$ |

### 10.2 LQR 批次解（推導為筆記補充）

| 項 | 公式 | 關鍵一步 |
|---|---|---|
| 代價 | $\bar J = X^{\mathsf T}\bar Q X + U^{\mathsf T}\bar R U$ | 分塊對角 |
| Hessian | $H = \bar B^{\mathsf T}\bar Q \bar B + \bar R \succ 0$ | $R \succ 0$ |
| 解 | $U^* = -H^{-1}\bar B^{\mathsf T}\bar Q\bar A\, x_{\text{init}}$ | 梯度為零 |
| 成本 | 求反 $mT \times mT$ | — |

### 10.3 LQR 動態規劃（推導為筆記補充）

| 項 | 公式 | 關鍵一步 |
|---|---|---|
| 終點 | $P_T = Q$，$u_T^* = 0$ | $R \succ 0$ |
| 回饋增益 | $F_t = -(R + B^{\mathsf T}P_{t+1}B)^{-1}B^{\mathsf T}P_{t+1}A$ | 對 $u$ 梯度為零 |
| 代價遞迴 | $P_t = Q + F_t^{\mathsf T}RF_t + (A + BF_t)^{\mathsf T}P_{t+1}(A + BF_t)$ | 代回 $u = Fx$ |
| Riccati 形式 | $P_t = Q + A^{\mathsf T}PA - A^{\mathsf T}PB(R + B^{\mathsf T}PB)^{-1}B^{\mathsf T}PA$ | 用最佳性條件化簡 |
| 控制 | $u_t = F_t x_t$ | 回饋策略 |
| 成本 | $T$ 個 $m \times m$ 求反，線性於 $T$ | — |

### 10.4 iLQR

| 步驟 | 內容 |
|---|---|
| 1–2 | 初始猜測 $\bar u$，rollout 得 $\bar x$ |
| 3 | $\delta x_{t+1} \approx A_t\delta x_t + B_t\delta u_t$，$A_t = \partial_x f$，$B_t = \partial_u f$ |
| 4 | 代價二階泰勒展開 |
| 5 | 擴充 $z = (\delta x, 1)$ 把一次項放進二次式 → 標準 LQR |
| 6 | 解出 $\delta u^*$，$\bar u \leftarrow \bar u + \alpha\delta u^*$ |
| 7 | 重複到收斂 |
| 正則化 | $R + B^{\mathsf T}PB + \rho I$，確保正定 |
| 線搜尋 | $\alpha = 1, \tfrac12, \tfrac14, \dots$ 直到代價足夠下降 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 動態規劃、最佳性原理、cost-to-go | 1-18 A*（cost-to-go、啟發函數）、1-19 MDP（價值迭代） |
| 線性最小平方、令梯度為零 | MSR2：2-05 最小平方 |
| 牛頓法、線性化、正則化、線搜尋 | MSR2：2-10 非線性最小平方（Gauss-Newton、Levenberg-Marquardt） |
| 回饋策略 vs. 開迴路序列 | 1-19 MDP 的策略（policy） |

---

## 附：本集一句話總結

> **消去狀態後，MPC 內層變成無限制最佳化。LQR 可以批次解（一個 $mT$ 維的線性方程組）或用動態規劃往回遞迴（$u_t = F_t x_t$，每步只求反 $m \times m$，還得到回饋策略）。非線性問題用 iLQR：反覆在操作點線性化動力學、二次近似代價、解 LQR、加正則化與線搜尋走一步。**

---

## ⚠️ 待確認清單

1. [▶ 1:11:52](https://youtu.be/TtGCEzYxM_A?t=4312) 延伸閱讀的作者：Whisper 寫 “Francesco Urelli”、“Notre-Dame and Wright”、“Russ Tedrick”，依發音推測為 Borrelli、Nocedal & Wright、Tedrake，待確認。

---

*筆記依據 Lasse Peters「Mobile Sensing and Robotics 1」Model Predictive Control Part 2 錄影逐字稿（Whisper `medium.en`，1:12:37）整理；本集沒有課本對應章節。*
