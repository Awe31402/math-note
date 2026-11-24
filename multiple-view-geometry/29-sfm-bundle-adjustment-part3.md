---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 29
lecture: Lecture 10 (Part 3) – Structure-from-Motion (SfM) and bundle adjustment
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/m7sChPmkFjE
notes: MVG 附錄 A6.1–A6.2（書頁 597–602，PDF 頁 615–620）
---

# 第 29 集 · Lecture 10 (Part 3)：bundle adjustment 與四種迭代法（Newton、Gauss–Newton、梯度下降、LM） [▶ 影片](https://youtu.be/m7sChPmkFjE)

← 上一集：[28-sfm-bundle-adjustment-part2](28-sfm-bundle-adjustment-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[30-sfm-bundle-adjustment-part4](30-sfm-bundle-adjustment-part4.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 29 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（36:41，Whisper `medium.en` 轉錄）＋ MVG A6.1–A6.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Bundle adjustment 的目標函數](#1-bundle-adjustment-的目標函數)
- [2. 一般形式](#2-一般形式)
- [3. Jacobian 與 Hessian](#3-jacobian-與-hessian)
- [4. Newton 法](#4-newton-法)
- [5. Gauss–Newton 法](#5-gaussnewton-法)
- [6. 梯度下降](#6-梯度下降)
- [7. Levenberg–Marquardt](#7-levenbergmarquardt)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

初始重建（第 28 集）得到的相機和 3D 點有誤差。**bundle adjustment（BA）**把它們一起最佳化。本集講目標函數和四種迭代最佳化方法。

| 主題 | MVG |
|---|---|
| BA 目標函數 | §18.1、A6 |
| Newton、Gauss–Newton | A6.1 |
| 梯度下降、Levenberg–Marquardt | A6.2 |

---

## 1. Bundle adjustment 的目標函數

[▶ 00:00](https://youtu.be/m7sChPmkFjE?t=0)

**重投影誤差**：

- 第 $i$ 張圖的相機 $P_i$、第 $j$ 個 3D 點 $\mathbf{X}_j$、它在第 $i$ 張圖的觀測 $\mathbf{x}_{ij}$。
- $P_i$、$\mathbf{X}_j$ 都是估計出來的（雙視角幾何、PnP、三角化），有誤差 → 重投影點 $\hat{\mathbf{x}}_{ij}=\pi(P_i,\mathbf{X}_j)$ 不會剛好等於 $\mathbf{x}_{ij}$。
- 差 $\Delta\mathbf{z}_{ij}=\mathbf{x}_{ij}-\hat{\mathbf{x}}_{ij}$ 是**重投影誤差**。

**目標** [▶ 02:18](https://youtu.be/m7sChPmkFjE?t=138)：在**所有相機和所有 3D 點**上最小化：

$$
\min_{\{P_i\},\{\mathbf{X}_j\}}\ \sum_{i,j}\left\|\mathbf{x}_{ij}-\pi(P_i,\mathbf{X}_j)\right\|_W^2=\sum_{i,j}\Delta\mathbf{z}_{ij}^\mathsf{T}W_{ij}\Delta\mathbf{z}_{ij}
$$

- $\pi(P_i,\mathbf{X}_j)$：算 $P_i\mathbf{X}_j$，**別忘了除以第三個分量**，變成 $(x,y,1)$。
- $W$：量測誤差的共變異數，用來加權。

**參數個數** [▶ 04:07](https://youtu.be/m7sChPmkFjE?t=247)：$n$ 台相機各 12 個（$3\times4$），$m$ 個點各 3 個 → 參數向量 $\mathbf{p}$ 有 $12n+3m$ 維。

⚠️ 逐字稿缺字 [▶ 04:14](https://youtu.be/m7sChPmkFjE?t=254)：Whisper 寫「12m by 3m vector」，依上下文應為 $12n+3m$ 維。

---

## 2. 一般形式

[▶ 04:51](https://youtu.be/m7sChPmkFjE?t=291)

- 非線性函數關係 $\mathbf{x}=f(\mathbf{p})$：$\mathbf{p}\in\mathbb{R}^M$ 是要最佳化的參數，$\mathbf{x}\in\mathbb{R}^N$ 是量測向量。
- 量到的 $\mathbf{x}$ 近似真值 $\bar{\mathbf{x}}$。要找 $\hat{\mathbf{p}}$ 最滿足這個關係：
$$
\mathbf{x}=f(\hat{\mathbf{p}})-\boldsymbol{\epsilon}\quad\Longrightarrow\quad\boldsymbol{\epsilon}=f(\hat{\mathbf{p}})-\mathbf{x}
$$
- 在 BA 裡：$\mathbf{x}$ 是所有觀測像點，$\mathbf{p}$ 是所有相機和 3D 點，$f$ 是重投影函數 $\pi$。
- 最小化
$$
g(\mathbf{p})=\frac{1}{2}\|\boldsymbol{\epsilon}(\mathbf{p})\|^2=\frac{1}{2}\boldsymbol{\epsilon}^\mathsf{T}\boldsymbol{\epsilon}
$$

> 以下**不是逐字稿內容**：講者前面定義 $\boldsymbol{\epsilon}=f(\hat{\mathbf{p}})-\mathbf{x}$，後面講 Gauss–Newton 時又寫成 $\boldsymbol{\epsilon}=\mathbf{x}-f(\mathbf{p})$。兩種只差一個負號，會讓 Jacobian $\boldsymbol{\epsilon}_\mathbf{p}$ 差一個負號；本筆記統一用 $\boldsymbol{\epsilon}=f(\mathbf{p})-\mathbf{x}$，所以 $\boldsymbol{\epsilon}_\mathbf{p}=J=\partial f/\partial\mathbf{p}$。

---

## 3. Jacobian 與 Hessian

[▶ 07:48](https://youtu.be/m7sChPmkFjE?t=468)

在初值 $\mathbf{p}_0$ 附近用**泰勒展開**：

$$
g(\mathbf{p}_0+\boldsymbol{\delta})\approx g(\mathbf{p}_0)+g_\mathbf{p}\boldsymbol{\delta}+\frac{1}{2}\boldsymbol{\delta}^\mathsf{T}g_{\mathbf{pp}}\boldsymbol{\delta}
$$

- $g_\mathbf{p}=\left.\dfrac{\partial g}{\partial\mathbf{p}}\right|_{\mathbf{p}_0}$：一階導數。
- $g_{\mathbf{pp}}=\left.\dfrac{\partial^2g}{\partial\mathbf{p}^2}\right|_{\mathbf{p}_0}$：二階導數，叫 **Hessian**。

**Jacobian 矩陣** [▶ 09:53](https://youtu.be/m7sChPmkFjE?t=593)：$\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$，

$$
J=\begin{pmatrix}\dfrac{\partial f_1}{\partial x_1}&\cdots&\dfrac{\partial f_1}{\partial x_n}\\\vdots&&\vdots\\\dfrac{\partial f_m}{\partial x_1}&\cdots&\dfrac{\partial f_m}{\partial x_n}\end{pmatrix}\in\mathbb{R}^{m\times n},\qquad J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

- 第 $j$ 行：整個 $\mathbf{f}$ 對第 $j$ 個輸入的偏微分。

**Hessian 矩陣** [▶ 11:23](https://youtu.be/m7sChPmkFjE?t=683)：純量函數 $f$ 的二階偏導數：

$$
H_{ij}=\frac{\partial^2f}{\partial x_i\partial x_j},\qquad H\in\mathbb{R}^{n\times n}
$$

---

## 4. Newton 法

[▶ 12:25](https://youtu.be/m7sChPmkFjE?t=745)

**推導**：找 $\boldsymbol{\delta}$ 讓 $g(\mathbf{p}_0+\boldsymbol{\delta})$ 最小。對泰勒展開的 $\boldsymbol{\delta}$ 微分、設為 0：

- $g(\mathbf{p}_0)$ 和 $\boldsymbol{\delta}$ 無關 → 微分是 0。
- $g_\mathbf{p}\boldsymbol{\delta}$ → $g_\mathbf{p}$。
- $\frac{1}{2}\boldsymbol{\delta}^\mathsf{T}g_{\mathbf{pp}}\boldsymbol{\delta}$ → $g_{\mathbf{pp}}\boldsymbol{\delta}$。

$$
g_\mathbf{p}+g_{\mathbf{pp}}\boldsymbol{\delta}=\mathbf{0}\quad\Longrightarrow\quad g_{\mathbf{pp}}\boldsymbol{\delta}=-g_\mathbf{p}
$$

- 非齊次線性方程式 $A\mathbf{x}=\mathbf{b}$，用逆（或偽逆）解 $\boldsymbol{\delta}$。
- 更新 $\mathbf{p}_{i+1}=\mathbf{p}_i+\boldsymbol{\delta}_i$，重複直到收斂。

（$g_\mathbf{p}$ 當成行向量處理；講者沒區分行列。）

**直覺** [▶ 15:05](https://youtu.be/m7sChPmkFjE?t=905)（一維 $p$ 為例）：

- 在目前的點 $p_0$，用一條**二次曲線**近似 $g(p)$，跳到二次曲線的最低點當 $p_1$；再在 $p_1$ 近似、再跳……直到局部最小值。

**缺點**：

1. 只在**已經接近最小值**、而且附近真的像二次曲線時表現好（收斂很快）。離得遠時二次近似很差，開始時收斂很慢。
2. **Hessian 很難算**：要非線性函數的二階導數。

---

## 5. Gauss–Newton 法

[▶ 17:36](https://youtu.be/m7sChPmkFjE?t=1056)

用來避開 Hessian 的計算。

**一階導數**（連鎖律）[▶ 18:33](https://youtu.be/m7sChPmkFjE?t=1113)：$g=\frac{1}{2}\boldsymbol{\epsilon}^\mathsf{T}\boldsymbol{\epsilon}$，

$$
g_\mathbf{p}=\boldsymbol{\epsilon}_\mathbf{p}^\mathsf{T}\boldsymbol{\epsilon},\qquad\boldsymbol{\epsilon}_\mathbf{p}=\frac{\partial\boldsymbol{\epsilon}}{\partial\mathbf{p}}=\frac{\partial f(\mathbf{p})}{\partial\mathbf{p}}=J
$$

- $\mathbf{x}$ 和 $\mathbf{p}$ 無關，微分消失，只剩 $f$ 的 Jacobian。BA 裡 $f$ 就是重投影函數 $\pi$。

**二階導數** [▶ 19:54](https://youtu.be/m7sChPmkFjE?t=1194)：

$$
g_{\mathbf{pp}}=\boldsymbol{\epsilon}_\mathbf{p}^\mathsf{T}\boldsymbol{\epsilon}_\mathbf{p}+\boldsymbol{\epsilon}^\mathsf{T}\boldsymbol{\epsilon}_{\mathbf{pp}}
$$

- 第二項要 $\boldsymbol{\epsilon}$ 的二階導數，很貴；而且每次迭代都要算一次。
- **忽略第二項**：
$$
g_{\mathbf{pp}}\approx\boldsymbol{\epsilon}_\mathbf{p}^\mathsf{T}\boldsymbol{\epsilon}_\mathbf{p}=J^\mathsf{T}J
$$
- 用 Jacobian 的乘積近似 Hessian，只要算一次 Jacobian。

**正規方程式（normal equations）** [▶ 22:00](https://youtu.be/m7sChPmkFjE?t=1320)：代進 Newton 的 $g_{\mathbf{pp}}\boldsymbol{\delta}=-g_\mathbf{p}$：

$$
J^\mathsf{T}J\,\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}
$$

**加權版本** [▶ 22:26](https://youtu.be/m7sChPmkFjE?t=1346)：考慮量測的誤差共變異數 $\Sigma$：

$$
J^\mathsf{T}\Sigma^{-1}J\,\boldsymbol{\delta}=-J^\mathsf{T}\Sigma^{-1}\boldsymbol{\epsilon}
$$

- 講者留作練習：從 $\frac{1}{2}\boldsymbol{\epsilon}^\mathsf{T}\Sigma^{-1}\boldsymbol{\epsilon}$ 出發，同樣取一階、二階導數並忽略高階項。

（加權版本中的 $\Sigma^{-1}$ 依 MVG A6.1 寫出；逐字稿說成「$\boldsymbol{\epsilon}^\mathsf{T}\Sigma\boldsymbol{\epsilon}$」，應是指以共變異數的逆加權。）

**為什麼一定解得出來** [▶ 23:26](https://youtu.be/m7sChPmkFjE?t=1406)：

- $J^\mathsf{T}J$ 是一個矩陣乘自己的轉置 → **對稱、半正定**（$J$ 行滿秩時正定）。
- $\Sigma^{-1}$ 對稱正定 → $J^\mathsf{T}\Sigma^{-1}J$ 也對稱正定 → 可逆。
- 解出 $\boldsymbol{\delta}$，更新 $\mathbf{p}_{i+1}=\mathbf{p}_i+\boldsymbol{\delta}_i$，重複到收斂。

> 以下**不是逐字稿內容**，是正規方程式的另一個看法：Gauss–Newton 等於每一步把 $\boldsymbol{\epsilon}(\mathbf{p}+\boldsymbol{\delta})\approx\boldsymbol{\epsilon}+J\boldsymbol{\delta}$ 線性化，再解線性最小平方 $\min_{\boldsymbol{\delta}}\|\boldsymbol{\epsilon}+J\boldsymbol{\delta}\|^2$——它的正規方程式就是上式。

---

## 6. 梯度下降

[▶ 24:45](https://youtu.be/m7sChPmkFjE?t=1485)

- 不算 Hessian，只算**梯度** $g_\mathbf{p}=J^\mathsf{T}\boldsymbol{\epsilon}$，往**負梯度**方向走一步：
$$
\lambda\boldsymbol{\delta}=-g_\mathbf{p}=-J^\mathsf{T}\boldsymbol{\epsilon}
$$
  $1/\lambda$ 是步長（講者說 $\lambda$ 是控制步長的超參數）。
- 一維直覺：在 $p_0$ 算斜率，往下坡走一小步到 $p_1$，再算斜率……直到局部最小值。

**優缺點** [▶ 27:39](https://youtu.be/m7sChPmkFjE?t=1659)：

| 優點 | 缺點 |
|---|---|
| 最好算：只要一階導數 | 不是好的最小化方法：目標函數局部不平滑時會走**鋸齒狀**路徑，收斂很慢 |
| **離最小值很遠時仍然有用**（Newton 類在那裡可能不收斂） | |

⚠️ 逐字稿缺字：講者口述時把梯度下降的式子寫成 $\lambda\boldsymbol{\delta}=J^\mathsf{T}\boldsymbol{\epsilon}$（沒有負號）；往下坡走要有負號。

---

## 7. Levenberg–Marquardt

[▶ 28:43](https://youtu.be/m7sChPmkFjE?t=1723)

**想法**：結合 Gauss–Newton 和梯度下降，各取所長。

**增廣正規方程式**：在 $J^\mathsf{T}J$ 的對角加上 $\lambda$：

$$
\left(J^\mathsf{T}J+\lambda I\right)\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}
$$

**演算法** [▶ 29:45](https://youtu.be/m7sChPmkFjE?t=1785)：

1. **初值**：$\lambda=10^{-3}\times$（$J^\mathsf{T}J$ 對角元素的平均值）。
2. 解增廣正規方程式得 $\boldsymbol{\delta}$，試算 $\mathbf{p}_{\text{new}}=\mathbf{p}+\boldsymbol{\delta}$。
3. 算新的誤差 $\boldsymbol{\epsilon}(\mathbf{p}_{\text{new}})$，和上一步比：
   - **誤差變小**：接受 $\mathbf{p}_{\text{new}}$；$\lambda\leftarrow\lambda/10$（典型因子）。
   - **誤差變大**：**拒絕**這一步，$\mathbf{p}$ 保持不變；$\lambda\leftarrow\lambda\times10$，重新解增廣正規方程式。
4. 重複直到收斂。

⚠️ 逐字稿缺字：Whisper 把 Levenberg–Marquardt 寫成 “Leuvenberg-Macquaire”、“luverberg-makur”、“lower Markov”。

**為什麼這樣調 $\lambda$** [▶ 32:15](https://youtu.be/m7sChPmkFjE?t=1935)：

| $\lambda$ | 增廣方程式變成 | 什麼時候 | 理由 |
|---|---|---|---|
| **很小** | $J^\mathsf{T}J\boldsymbol{\delta}\approx-J^\mathsf{T}\boldsymbol{\epsilon}$：**Gauss–Newton** | 誤差一直在變小 → 大概已經接近最小值 | 接近最小值時函數像二次曲線，Gauss–Newton 收斂最快 |
| **很大** | $\lambda\boldsymbol{\delta}\approx-J^\mathsf{T}\boldsymbol{\epsilon}$：**梯度下降** | 誤差變大 → 離最小值還遠 | 遠處不像二次曲線，Gauss–Newton 可能不收斂；梯度下降雖然鋸齒狀，總比不收斂好 |

- LM 依每一步的誤差，在 Gauss–Newton 和梯度下降之間**自動切換**。
- $\lambda$ 越大，步長越短 → 最終一定能讓目標函數下降。

【課本補充】MVG A6.2：有些實作（例如 Numerical Recipes）用**乘法**增廣：$N_{ii}\leftarrow(1+\lambda)N_{ii}$（$N=J^\mathsf{T}J$），非對角不變——等於加上 $\lambda\,\mathrm{diag}(J^\mathsf{T}J)$，每個參數按它自己的尺度增廣。

（本集到 36:36 結束。）

---

## 8. 一頁速查表

### BA

$$
\min_{\{P_i\},\{\mathbf{X}_j\}}\sum_{i,j}\|\mathbf{x}_{ij}-\pi(P_i,\mathbf{X}_j)\|_W^2,\qquad\mathbf{p}\in\mathbb{R}^{12n+3m}
$$

### 四種方法（$g=\frac12\|\boldsymbol{\epsilon}\|^2$、$\boldsymbol{\epsilon}=f(\mathbf{p})-\mathbf{x}$、$J=\partial f/\partial\mathbf{p}$）

| 方法 | 更新方程式 | 關鍵一步 | 特性 |
|---|---|---|---|
| Newton | $g_{\mathbf{pp}}\boldsymbol{\delta}=-g_\mathbf{p}$ | 二階泰勒展開對 $\boldsymbol{\delta}$ 微分為 0 | 近處快；Hessian 貴；遠處差 |
| Gauss–Newton | $J^\mathsf{T}J\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}$（加權：$J^\mathsf{T}\Sigma^{-1}J\boldsymbol{\delta}=-J^\mathsf{T}\Sigma^{-1}\boldsymbol{\epsilon}$） | $g_{\mathbf{pp}}\approx J^\mathsf{T}J$（丟掉 $\boldsymbol{\epsilon}^\mathsf{T}\boldsymbol{\epsilon}_{\mathbf{pp}}$） | 不必算二階導數 |
| 梯度下降 | $\lambda\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}$ | 往負梯度走 | 遠處穩；近處鋸齒、慢 |
| LM | $(J^\mathsf{T}J+\lambda I)\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}$ | 誤差降 → $\lambda/10$（像 GN）；誤差升 → 拒絕、$\lambda\times10$（像 GD） | $\lambda_0=10^{-3}\cdot\overline{\mathrm{diag}(J^\mathsf{T}J)}$ |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $J^\mathsf{T}J$ 正規方程式 | 第 30 集（BA 的 Jacobian 很稀疏 → Schur 補） |
| LM | 第 30 集（稀疏 LM）；第 12 集、第 20 集回顧（校正、PnP 精修都用 LM） |
| 參數化（$12n+3m$） | 第 30 集（更好的參數化：旋轉用 3 個參數） |

---

## 附：本集一句話總結

> **bundle adjustment 就是對所有相機和 3D 點最小化重投影誤差 $\sum\|\mathbf{x}_{ij}-\pi(P_i,\mathbf{X}_j)\|^2$；Newton 法用二次近似但要算 Hessian，Gauss–Newton 用 $J^\mathsf{T}J$ 取代 Hessian 得正規方程式 $J^\mathsf{T}J\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}$，梯度下降只沿負梯度走，而 Levenberg–Marquardt 在對角加 $\lambda$：誤差下降就縮小 $\lambda$ 變成 Gauss–Newton、誤差上升就放大 $\lambda$ 變成梯度下降，兼顧近處的速度和遠處的穩定。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 10 (Part 3) 錄影逐字稿（Whisper `medium.en`，36:41）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 附錄 A6.1–A6.2 整理。*
