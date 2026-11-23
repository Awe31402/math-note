---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-05
lecture: Least Squares – An Informal Introduction
date: 待補（2021 夏季學期）
video: https://youtu.be/r2cyMQ5NB1o
notes: MVG（Hartley & Zisserman 第 2 版）附錄 6 §A6.1（書頁 597–600，PDF 頁 615–618）
---

# 第 2-05 集 · 最小平方法：非正式入門（Least Squares） [▶ 影片](https://youtu.be/r2cyMQ5NB1o)

← 上一集：[2-03-slam-intro](2-03-slam-intro.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-07-icp-part1](2-07-icp-part1.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-05 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:01:09，Whisper `medium.en` 轉錄）＋ MVG 附錄 6
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 最小平方在解什麼](#1-最小平方在解什麼)
- [2. 問題設定](#2-問題設定)
- [3. 誤差函數](#3-誤差函數)
- [4. 為什麼要迭代](#4-為什麼要迭代)
- [5. 推導 Gauss-Newton](#5-推導-gauss-newton)
  - [5.1 線性化誤差](#51-線性化誤差)
  - [5.2 代入平方誤差](#52-代入平方誤差)
  - [5.3 加總所有觀測](#53-加總所有觀測)
  - [5.4 求二次式的最小值](#54-求二次式的最小值)
  - [5.5 演算法](#55-演算法)
- [6. 例子：里程計校正](#6-例子里程計校正)
- [7. 解線性方程組：Cholesky 分解](#7-解線性方程組cholesky-分解)
- [8. 和機率式狀態估計的關係](#8-和機率式狀態估計的關係)
- [9. 總結](#9-總結)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

圖式 SLAM 就是「用最小平方解 SLAM」。這集非正式但完整地推導**最小平方**和 **Gauss-Newton** 法，做一個里程計校正的例子，最後說明它和機率式狀態估計的關係。

---

## 1. 最小平方在解什麼

[▶ 00:51](https://youtu.be/r2cyMQ5NB1o?t=51)

- 解**超定**（overdetermined）系統的一般方法：**方程比未知數多**。
- 例：要估計一組參數，有一堆觀測。為了估得好，觀測通常比參數多。觀測有雜訊，所以**找不到**讓所有誤差都為零的參數，總會有小誤差。
- 目標：找參數，讓**誤差平方和最小**。
- 已經用了兩百多年，工程上很常見。
- SLAM 裡：觀測 = 感測資料（相機、雷射）和里程計；參數 = 各時刻的平台位姿、3D 地標位置。

**歷史** [▶ 03:16](https://youtu.be/r2cyMQ5NB1o?t=196)：Carl Friedrich Gauss 18 歲時發展出來；1801 年用它預測小行星**穀神星**（Ceres）未來的位置，首次證明它的價值。高斯本人也用它建地圖、測量點位。

【口頭】用最小平方建圖不是新東西。機器人學新的地方在於：觀測和限制的種類、要很快（線上而非離線）、資料關聯的挑戰。

---

## 2. 問題設定

[▶ 04:34](https://youtu.be/r2cyMQ5NB1o?t=274)

| 記號 | 意思 |
|---|---|
| $x$ | 狀態（未知數、參數） |
| $f_i(x)$ | **觀測函數**：假設知道狀態 $x$，預測應該看到什麼 |
| $\hat z_i = f_i(x)$ | **預測觀測** |
| $z_i$ | **實際觀測**（量測）：不一定直接量到 $x$，但和 $x$ 有關 |

**目標**：找出最能解釋所有觀測 $z_1, \dots, z_n$ 的狀態 $x$：讓預測觀測和實際觀測的差距平方和最小 [▶ 06:14](https://youtu.be/r2cyMQ5NB1o?t=374)。

- 使用者要提供的是觀測函數 $f$（取決於感測器的**模型**）；實際觀測取決於**實體**感測器。
- 把每對 $\hat z_i$、$z_i$ 相減、平方、加總，然後調整 $x$ 讓總和最小。

**例子：相機與 3D 點** [▶ 07:56](https://youtu.be/r2cyMQ5NB1o?t=476)：

- $x$ = 3D 特徵點的位置（例如 $(10, 2, 3)$）。
- 觀測 = 這些點投影到相機影像平面上的像素座標。
- $f$ = 從 3D 世界到 2D 影像的投影（輸入例如 $(1, 1, 1)$，告訴你會落在哪個像素）。
- 比較實際影像裡的像素和 $f$ 算出的像素，移動 3D 點讓差距最小。怎麼移動，就是這個方法要回答的。

---

## 3. 誤差函數

[▶ 09:38](https://youtu.be/r2cyMQ5NB1o?t=578)

**誤差向量**（第 $i$ 個觀測）：

$$
e_i(x) = z_i - f_i(x)
$$

**假設**：雜訊是**零平均的高斯**（沒有偏差），而且知道感測器多好：用**資訊矩陣** $\Omega_i$ 表示（= 共變異數矩陣的反矩陣，代表這個量測有多少資訊）。每個觀測可以有不同的 $\Omega_i$。

**平方誤差**（純量）：

$$
E_i(x) = e_i(x)^{\mathsf T}\, \Omega_i\, e_i(x)
$$

- $\Omega_i$ 當權重 → 這已經是**加權**最小平方。如果所有觀測不確定性都一樣，可以拿掉 $\Omega_i$。
- 粗體 $e_i$ 是向量，非粗體 $E_i$ 是純量（這裡用小寫 $e$ 和大寫 $E$ 區分）。

**總誤差** [▶ 12:35](https://youtu.be/r2cyMQ5NB1o?t=755)：

$$
F(x) = \sum_i E_i(x) = \sum_i e_i(x)^{\mathsf T}\, \Omega_i\, e_i(x)
$$

$$
x^* = \arg\min_x F(x)
$$

---

## 4. 為什麼要迭代

[▶ 13:46](https://youtu.be/r2cyMQ5NB1o?t=826)

- 一般很複雜，要用**數值方法**。
- $f$ 通常是**非線性**的 → 要迭代，而且**不保證**找到最小值。
- 需要好的**初始猜測**：離解太遠，多半找不到合理的解（對大多數真實的非線性問題）。
- 假設誤差函數在（希望是全域的）最小值附近夠**平滑**，初始猜測也夠近。
- 一般情況下**沒有保證**找到全域最佳解；有些特殊情況能談收斂保證。
- 做法：**迭代地局部線性化**：把函數當成線性的，一步一步走向最小值。

**每一輪** [▶ 16:04](https://youtu.be/r2cyMQ5NB1o?t=964)：

1. 在目前的初始猜測附近**線性化**誤差函數 $e_i$。
2. 代入平方誤差 → 得到**二次式**。
3. 求二次式的最小值：一階導數設為零、解方程（就像在學校求拋物線最低點）。
4. 但這個二次式只是近似 → 用新解當初始猜測，**重複**。

---

## 5. 推導 Gauss-Newton

### 5.1 線性化誤差

[▶ 17:27](https://youtu.be/r2cyMQ5NB1o?t=1047)

在初始猜測 $x$（這一輪是常數）附近，變數是偏移量 $\Delta x$（在初始猜測處為 0）。一階泰勒展開：

$$
e_i(x + \Delta x) \approx \underbrace{e_i(x)}_{=:\, e_i} + J_i\, \Delta x
$$

- $e_i$：在線性化點的誤差值（常數），簡寫。
- $J_i = \dfrac{\partial e_i(x)}{\partial x}$：**Jacobian**（多維的一階導數）。列對應函數的各分量，欄對應 $x$ 的各分量（1-10 第 10 節）。
- 原本非線性的誤差變成線性函數。這是**近似**。

### 5.2 代入平方誤差

[▶ 20:53](https://youtu.be/r2cyMQ5NB1o?t=1253)

$$
\begin{aligned}
E_i(x + \Delta x) &= e_i(x + \Delta x)^{\mathsf T}\, \Omega_i\, e_i(x + \Delta x) \\
&\approx (e_i + J_i \Delta x)^{\mathsf T}\, \Omega_i\, (e_i + J_i \Delta x) \\
&= e_i^{\mathsf T}\Omega_i e_i + e_i^{\mathsf T}\Omega_i J_i \Delta x + \Delta x^{\mathsf T} J_i^{\mathsf T}\Omega_i e_i + \Delta x^{\mathsf T} J_i^{\mathsf T}\Omega_i J_i \Delta x
\end{aligned}
$$

- 第 1 項：不含 $\Delta x$（常數）。
- 第 2、3 項：$\Delta x$ 的一次項。它們是純量，而且互為轉置（$\Omega_i$ 對稱），所以相等，合起來是 $2\, e_i^{\mathsf T}\Omega_i J_i \Delta x$。
- 第 4 項：$\Delta x$ 的二次項。

（第 2、3 項相等的理由是筆記補的：純量的轉置是自己，$(e^{\mathsf T}\Omega J\Delta x)^{\mathsf T} = \Delta x^{\mathsf T}J^{\mathsf T}\Omega^{\mathsf T}e = \Delta x^{\mathsf T}J^{\mathsf T}\Omega e$。）

**重新命名** [▶ 23:06](https://youtu.be/r2cyMQ5NB1o?t=1386)：

$$
c_i = e_i^{\mathsf T}\Omega_i e_i, \qquad
b_i^{\mathsf T} = e_i^{\mathsf T}\Omega_i J_i, \qquad
H_i = J_i^{\mathsf T}\Omega_i J_i
$$

$$
E_i(x + \Delta x) \approx c_i + 2\, b_i^{\mathsf T}\Delta x + \Delta x^{\mathsf T} H_i\, \Delta x
$$

到這裡唯一的近似是泰勒展開，其餘都只是重新整理，「沒有黑魔法」。

### 5.3 加總所有觀測

[▶ 25:02](https://youtu.be/r2cyMQ5NB1o?t=1502)

$\Delta x$ 對所有觀測都一樣，所以總和可以搬進各項：

$$
F(x + \Delta x) \approx \sum_i \bigl( c_i + 2\, b_i^{\mathsf T}\Delta x + \Delta x^{\mathsf T} H_i \Delta x \bigr) = c + 2\, b^{\mathsf T}\Delta x + \Delta x^{\mathsf T} H\, \Delta x
$$

$$
\boxed{\;b^{\mathsf T} = \sum_i e_i^{\mathsf T}\Omega_i J_i, \qquad H = \sum_i J_i^{\mathsf T}\Omega_i J_i\;}
$$

$b$ 是一次項係數的總和（向量），$H$ 是二次項係數的總和（矩陣）。整個問題變成一個大的**二次式**。

### 5.4 求二次式的最小值

[▶ 27:23](https://youtu.be/r2cyMQ5NB1o?t=1643)

**二次式的導數** [▶ 28:27](https://youtu.be/r2cyMQ5NB1o?t=1707)：對 $f(x) = x^{\mathsf T}Hx + b^{\mathsf T}x$，

$$
\frac{\partial f}{\partial x} = (H + H^{\mathsf T})\, x + b
$$

（類比一維：$hx^2 + bx$ 的導數是 $2hx + b$；矩陣時 $2h$ 變成 $H + H^{\mathsf T}$。常數項求導後消失。）

套到 $F$（$H$ 對稱）：

$$
\frac{\partial F(x + \Delta x)}{\partial \Delta x} \approx 2b + 2H\Delta x
$$

**設為零** [▶ 30:31](https://youtu.be/r2cyMQ5NB1o?t=1831)：

$$
0 = 2b + 2H\Delta x \quad\Rightarrow\quad \boxed{\;H\, \Delta x = -b\;}
$$

這是一個**線性方程組**，解出增量：

$$
\Delta x^* = -H^{-1} b
$$

實際上不會真的求 $H^{-1}$，有更好的方法（第 7 節）。

### 5.5 演算法

[▶ 31:47](https://youtu.be/r2cyMQ5NB1o?t=1907)

```
Algorithm Gauss_Newton(x_init):
  x = x_init
  repeat
    for each observation i:
      e_i = z_i - f_i(x);  J_i = ∂e_i/∂x       // 在目前的 x 重新線性化
    b = Σ_i J_iᵀ Ω_i e_i
    H = Σ_i J_iᵀ Ω_i J_i
    solve H Δx = -b                              // 線性方程組
    x = x + Δx
  until Δx ≈ 0
  return x
```

- 每一輪都要**重新線性化**：初始猜測一直在變（上一輪的解）。
- 迭代到 $\Delta x$ 幾乎為零 → 希望收斂到全域最佳（初始猜測好的話），但沒有保證。

【課本補充】MVG §A6.1（書頁 597–600，PDF 頁 615–618）把 Gauss-Newton 放在更大的脈絡裡（MVG 用 $\epsilon = f(P) - X$，符號和本集相反，但結構相同）：
- **牛頓法**：對代價 $g(P) = \tfrac12\|\epsilon(P)\|^2$ 做二階泰勒展開，解 $g_{PP}\Delta = -g_P$。其中 Hessian $g_{PP} = \epsilon_P^{\mathsf T}\epsilon_P + \epsilon^{\mathsf T}\epsilon_{PP}$。
- **Gauss-Newton**：假設 $\epsilon$ 接近線性，丟掉含二階導數的第二項，用 $J^{\mathsf T}J$ **近似** Hessian → $J^{\mathsf T}J\Delta = -J^{\mathsf T}\epsilon$（就是正規方程）。在最小值附近或 $\epsilon$ 接近線性時這是好近似。
- **加權**：量測有共變異數 $\Sigma_X$ 時，正規方程變成 $J^{\mathsf T}\Sigma^{-1}J\Delta = -J^{\mathsf T}\Sigma^{-1}\epsilon$（對應本集的 $\Omega = \Sigma^{-1}$）。
- **梯度下降**：把 Hessian 換成 $\lambda I$；單獨用收斂慢（鋸齒狀），但和 Gauss-Newton 結合就是 **Levenberg-Marquardt**（見 2-10）。

---

## 6. 例子：里程計校正

[▶ 33:30](https://youtu.be/r2cyMQ5NB1o?t=2010)

- 里程計：數輪子轉數算出平台位置。常有**系統性誤差**（輪胎氣壓不同 → 偏向一側；幾何不完美）。
- 想用最小平方**校正**掉系統性誤差。
- 假設有一段行駛資料：量到的里程計 $u_i$，以及**真值** $u_i^*$（可以來自機上感測器、SLAM、外部動作捕捉、光達、外部追蹤；怎麼來不重要）。

**模型**：校正後的里程計 = 一個 $3 \times 3$ 矩陣乘上量到的里程計：

$$
u_i' = \begin{bmatrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ x_{31} & x_{32} & x_{33} \end{bmatrix} u_i
$$

**狀態向量** [▶ 36:01](https://youtu.be/r2cyMQ5NB1o?t=2161)：矩陣的 9 個元素：$x = (x_{11}, x_{12}, \dots, x_{33})^{\mathsf T}$。

**誤差函數**：真值減掉校正後的值：

$$
e_i(x) = u_i^* - \begin{bmatrix} x_{11} & x_{12} & x_{13} \\ x_{21} & x_{22} & x_{23} \\ x_{31} & x_{32} & x_{33} \end{bmatrix} u_i
$$

**Jacobian** [▶ 37:07](https://youtu.be/r2cyMQ5NB1o?t=2227)：3 列（誤差是 3 維）× 9 欄（9 個未知數）。

- 例：第一個分量 $e_{i,1} = u_{i,x}^* - (x_{11}u_{i,x} + x_{12}u_{i,y} + x_{13}u_{i,\theta})$。對 $x_{11}$ 微分 → $-u_{i,x}$；對 $x_{12}$ → $-u_{i,y}$；對 $x_{13}$ → $-u_{i,\theta}$；對其他 6 個 → 0。

$$
J_i = \frac{\partial e_i(x)}{\partial x} = -\begin{bmatrix}
u_{i,x} & u_{i,y} & u_{i,\theta} & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & u_{i,x} & u_{i,y} & u_{i,\theta} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & u_{i,x} & u_{i,y} & u_{i,\theta}
\end{bmatrix}
$$

（負號是筆記依 $e = z - f$ 的定義補上的；講者口述「非零元素就是 $u$ 的分量」，沒提正負號。）

**重點** [▶ 39:40](https://youtu.be/r2cyMQ5NB1o?t=2380)：Jacobian 裡**沒有** $x$。一階導數是常數 → 函數**本來就是線性**的 → 不需要重新線性化、初始猜測無所謂，**一次迭代**就得到解。算 $H$、$b$，解線性方程組，得到 9 個參數，代回校正函數。

**問題與答案** [▶ 41:14](https://youtu.be/r2cyMQ5NB1o?t=2474)（講者自問自答）：

| 問題 | 答案 |
|---|---|
| 里程計完美時，參數長怎樣？ | 單位矩陣：這時 $u_i = u_i^*$，$X = I$ 讓誤差恆為零 |
| 至少要幾個量測？ | 9 個未知數，每個量測給 3 個方程 → **至少 3 個**，通常要更多 |
| 為什麼 $H$ 對稱？ | $H = \sum J^{\mathsf T}\Omega J$，$\Omega$ 是對稱（半）正定的共變異數反矩陣，$J^{\mathsf T}$ 和 $J$ 從兩邊夾，每一項都對稱，總和也對稱 |
| 量測的結構怎麼影響 $H$？ | Jacobian 的零元素 = 這個觀測和某個參數無關。一個觀測涉及的變數越少，$H$ 越**稀疏**。SLAM 裡一個觀測通常只聯繫很少的變數 → $H$ 很稀疏，之後會利用這點高效求解 |

---

## 7. 解線性方程組：Cholesky 分解

[▶ 45:04](https://youtu.be/r2cyMQ5NB1o?t=2704)

- 理論上 $\Delta x = -H^{-1}b$，但實務上**不會**求完整的反矩陣。
- 用矩陣分解（Cholesky、QR），或大型系統用共軛梯度法（conjugate gradients），看系統的性質。

**Cholesky 分解** [▶ 45:53](https://youtu.be/r2cyMQ5NB1o?t=2753)：$A$ 對稱正定，要解 $Ax = b$。

1. 分解 $A = LL^{\mathsf T}$，$L$ 是**下三角**矩陣（主對角線以上全為零）。
2. 方程變成 $L L^{\mathsf T} x = b$。令 $y = L^{\mathsf T}x$。
3. 先解 $Ly = b$：$L$ 下三角 → **前向代入**，很簡單。
4. 再解 $L^{\mathsf T}x = y$：$L^{\mathsf T}$ 上三角 → **後向代入**，也很簡單。

一個複雜的線性系統換成兩個簡單的三角系統；主要的計算花在分解本身。

（前向／後向代入的名稱是筆記補的；講者說「三角矩陣的系統很容易解」。）

**整理 Gauss-Newton 的流程** [▶ 48:19](https://youtu.be/r2cyMQ5NB1o?t=2899)：初始猜測（問題越非線性，初始猜測越要好；線性時無所謂）→ 算誤差函數的線性化（**設計者要做的工作**：求一階導數）→ 得到 $H$ 和 $b$（二次式求導設零後只剩這兩個）→ 解線性方程組（例如 Cholesky；可能很花計算）→ 新解當初始猜測，重複到收斂。

---

## 8. 和機率式狀態估計的關係

[▶ 50:24](https://youtu.be/r2cyMQ5NB1o?t=3024)

機率機器人學說要用機率分布表示狀態。但上面講的最小平方和機率有什麼關係？

**從機率出發** [▶ 51:44](https://youtu.be/r2cyMQ5NB1o?t=3104)：用貝氏定理和馬可夫假設（類似 1-03 的推導，但要整條軌跡，所以更簡單）：

$$
p(x_{0:t} \mid z_{1:t},\, u_{1:t}) = \eta\; p(x_0) \prod_t \bigl[\, p(x_t \mid x_{t-1}, u_t)\; p(z_t \mid x_t) \,\bigr]
$$

- $\eta$：貝氏定理的正規化常數；$p(x_0)$：先驗（時刻 0，沒有觀測或控制）；運動模型和觀測模型的乘積。
- 控制指令也可以很容易地當成一種觀測。

**取對數** [▶ 53:02](https://youtu.be/r2cyMQ5NB1o?t=3182)：乘積變加總：

$$
\log p(x_{0:t} \mid z_{1:t}, u_{1:t}) = \text{const} + \log p(x_0) + \sum_t \bigl[\, \log p(x_t \mid x_{t-1}, u_t) + \log p(z_t \mid x_t) \,\bigr]
$$

**假設全部是高斯** [▶ 53:52](https://youtu.be/r2cyMQ5NB1o?t=3232)：先驗、運動模型、觀測模型都是高斯。高斯的對數：

$$
\log \mathcal N(x;\, \mu, \Sigma) = \text{const} - \frac12 (x - \mu)^{\mathsf T}\Sigma^{-1}(x - \mu)
$$

把 $x - \mu$ 記作 $e$、$\Sigma^{-1}$ 記作 $\Omega$ → 就是 $-\tfrac12 e^{\mathsf T}\Omega e$，和前面的平方誤差同形。

（講者口述時沒寫 $\tfrac12$；係數不影響最大化／最小化的位置。）

代入：

$$
\log p(x_{0:t} \mid z_{1:t}, u_{1:t}) = \text{const} - \frac12 \Bigl( e_p^{\mathsf T}\Omega_p e_p + \sum_t e_{u_t}^{\mathsf T}\Omega_{u_t} e_{u_t} + \sum_t e_{z_t}^{\mathsf T}\Omega_{z_t} e_{z_t} \Bigr)
$$

（先驗、里程計、觀測各一組誤差項。）

**結論** [▶ 56:07](https://youtu.be/r2cyMQ5NB1o?t=3367)：

$$
\arg\max_x \log p = \arg\min_x \Bigl( e_p^{\mathsf T}\Omega_p e_p + \sum_t e_{u_t}^{\mathsf T}\Omega_{u_t} e_{u_t} + \sum_t e_{z_t}^{\mathsf T}\Omega_{z_t} e_{z_t} \Bigr)
$$

- **在獨立高斯的假設下，最小化平方誤差 = 最大化對數似然。**
- 解出最小平方的解，就是那個高斯分布的**平均值**（最可能的組態）。
- 也有方法從矩陣 $H$ 算出或近似**共變異數**（講者沒展開）。
- 前面的最小平方只有觀測項；這裡多了先驗和運動指令兩種項。

---

## 9. 總結

[▶ 57:49](https://youtu.be/r2cyMQ5NB1o?t=3469)

- 非正式但足以理解、足以拿來解標準最小平方問題的介紹。
- **Gauss-Newton**：解非線性問題的迭代法。用線性化把非線性誤差變成線性，平方誤差變成二次式，求最小值；因為線性化是近似，要迭代。
- 在一些假設下，誤差最小化 = 機率最大化。
- 很多領域都用最小平方（大地測量學特別常用）。
- 參考：任何數值計算或最佳化教科書；維基百科；《Probabilistic Robotics》講最小平方和機率式狀態估計的關係。不同社群的記號可能不同。

---

## 10. 一頁速查表

### 10.1 Gauss-Newton

| 步驟 | 公式 | 關鍵一步 |
|---|---|---|
| 誤差 | $e_i(x) = z_i - f_i(x)$ | — |
| 總誤差 | $F(x) = \sum_i e_i^{\mathsf T}\Omega_i e_i$ | $\Omega_i = \Sigma_i^{-1}$ |
| 線性化 | $e_i(x + \Delta x) \approx e_i + J_i\Delta x$，$J_i = \partial e_i/\partial x$ | 一階泰勒 |
| 二次式 | $F(x + \Delta x) \approx c + 2b^{\mathsf T}\Delta x + \Delta x^{\mathsf T}H\Delta x$ | 展開後兩個一次項相等 |
| 係數 | $b = \sum_i J_i^{\mathsf T}\Omega_i e_i$，$H = \sum_i J_i^{\mathsf T}\Omega_i J_i$ | — |
| 正規方程 | $H\Delta x = -b$ | 導數 $2b + 2H\Delta x = 0$ |
| 更新 | $x \leftarrow x + \Delta x$，重複到 $\Delta x \approx 0$ | 每輪重新線性化 |

### 10.2 解法與性質

| 項 | 內容 |
|---|---|
| 解 $H\Delta x = -b$ | Cholesky $H = LL^{\mathsf T}$：$Ly = -b$（前向）、$L^{\mathsf T}\Delta x = y$（後向） |
| $H$ 對稱 | $J^{\mathsf T}\Omega J$ 的和 |
| $H$ 稀疏 | 每個觀測只涉及少數變數 |
| 線性問題 | $J$ 不含 $x$ → 一次迭代 |
| GN vs. 牛頓（MVG） | GN 用 $J^{\mathsf T}J$ 近似 Hessian，丟掉二階導數項 |

### 10.3 機率連結

$$
\text{獨立高斯} \;\Rightarrow\; \arg\max_x p(x \mid z, u) = \arg\min_x \sum e^{\mathsf T}\Omega e
$$

關鍵一步：$\log\mathcal N = \text{const} - \tfrac12 e^{\mathsf T}\Omega e$。

### 10.4 里程計校正例子

| 項 | 內容 |
|---|---|
| 狀態 | $3 \times 3$ 矩陣的 9 個元素 |
| 誤差 | $e_i = u_i^* - Xu_i$ |
| Jacobian | $3 \times 9$，每列只有 3 個非零元素（$-u_i$ 的分量），不含 $x$ |
| 最少量測 | 3 |
| 完美時 | $X = I$ |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 最小平方、$H\Delta x = -b$ | 2-07 ICP（已知對應的閉式解）、2-10 ICP 的非線性最小平方 |
| Jacobian、重新線性化 | 2-10、2-11 位姿圖 |
| $H$ 的稀疏性 | 2-11、2-12（圖式 SLAM 的高效求解） |
| 資訊矩陣 $\Omega$ | 2-11（邊的權重）、2-15（強健核改變權重） |
| 最小平方 = 高斯下的最大似然 | 2-15（非高斯雜訊時要換成強健方法） |
| Levenberg-Marquardt | 2-10 |

---

## 附：本集一句話總結

> **最小平方：誤差 $e_i = z_i - f_i(x)$，最小化 $\sum e_i^{\mathsf T}\Omega_i e_i$。Gauss-Newton 每輪在目前的 $x$ 線性化 $e_i \approx e_i + J_i\Delta x$，得到二次式，解正規方程 $H\Delta x = -b$（$H = \sum J^{\mathsf T}\Omega J$、$b = \sum J^{\mathsf T}\Omega e$），更新後重複。在獨立高斯假設下，這等於求後驗的最大值（平均值）。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Least Squares 錄影逐字稿（Whisper `medium.en`，1:01:09）與 MVG 附錄 6 整理。*
