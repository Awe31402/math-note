---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 30
lecture: Lecture 10 (Part 4) – Structure-from-Motion (SfM) and bundle adjustment
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/J5OX0hipzd4
notes: MVG 附錄 A6.3（書頁 602–606，PDF 頁 620–624）、A6.6–A6.7（書頁 612–618，PDF 頁 630–636）
---

# 第 30 集 · Lecture 10 (Part 4)：稀疏 LM、Schur 補、bundle adjustment 的稀疏結構、填入問題 [▶ 影片](https://youtu.be/J5OX0hipzd4)

← 上一集：[29-sfm-bundle-adjustment-part3](29-sfm-bundle-adjustment-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[31-stereo-part1](31-stereo-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 30 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（39:28，Whisper `medium.en` 轉錄）＋ MVG A6.3、A6.6–A6.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 問題：正規方程式太大](#1-問題正規方程式太大)
- [2. 把參數分成兩組](#2-把參數分成兩組)
- [3. Schur 補](#3-schur-補)
- [4. Bundle adjustment 的稀疏結構](#4-bundle-adjustment-的稀疏結構)
  - [4.1 Jacobian 的哪些地方是 0](#41-jacobian-的哪些地方是-0)
  - [4.2 J^T J 是鄰接矩陣](#42-jtj-是鄰接矩陣)
  - [4.3 為什麼 Schur 補特別划算](#43-為什麼-schur-補特別划算)
- [5. 解線性方程式：LU、QR、Cholesky](#5-解線性方程式luqrcholesky)
- [6. 填入問題與重新排序](#6-填入問題與重新排序)
- [7. 開源工具](#7-開源工具)
- [8. Lecture 10 總結](#8-lecture-10-總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 稀疏 LM：參數分組、Schur 補 | A6.3 |
| 多影像 BA 的稀疏結構 | A6.6 |
| 解稀疏線性方程式、填入問題 | A6.7 |

---

## 1. 問題：正規方程式太大

[▶ 00:00](https://youtu.be/J5OX0hipzd4?t=0)

- LM 每次迭代都要解 $J^\mathsf{T}J\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}$（非齊次線性方程式 $A\mathbf{x}=\mathbf{b}$，$\mathbf{x}=A^{-1}\mathbf{b}$）。
- 直接求逆是 **$O(N^3)$**，$N=12\times(\text{相機數})+3\times(\text{3D 點數})$——3D 點常常上百萬。
- 好在 $J^\mathsf{T}J$ 有**稀疏的分塊結構**可以利用。

---

## 2. 把參數分成兩組

[▶ 01:40](https://youtu.be/J5OX0hipzd4?t=100)

$$
\mathbf{p}=\begin{pmatrix}\mathbf{a}\\\mathbf{b}\end{pmatrix}
$$

- BA 裡：$\mathbf{a}$ = 所有**相機**參數，$\mathbf{b}$ = 所有 **3D 點**參數。

**Jacobian 分塊** [▶ 02:48](https://youtu.be/J5OX0hipzd4?t=168)：

$$
J=\frac{\partial\hat{\mathbf{x}}}{\partial\mathbf{p}}=\left[A\mid B\right],\qquad A=\frac{\partial\hat{\mathbf{x}}}{\partial\mathbf{a}},\quad B=\frac{\partial\hat{\mathbf{x}}}{\partial\mathbf{b}}
$$

**正規方程式分塊** [▶ 03:32](https://youtu.be/J5OX0hipzd4?t=212)：

$$
\begin{pmatrix}A^\mathsf{T}A & A^\mathsf{T}B\\ B^\mathsf{T}A & B^\mathsf{T}B\end{pmatrix}\begin{pmatrix}\boldsymbol{\delta}_\mathbf{a}\\\boldsymbol{\delta}_\mathbf{b}\end{pmatrix}=\begin{pmatrix}\boldsymbol{\epsilon}_A\\\boldsymbol{\epsilon}_B\end{pmatrix}
$$

- 右邊也分兩塊：$\boldsymbol{\epsilon}_A=-A^\mathsf{T}\boldsymbol{\epsilon}$ 只和 $\mathbf{a}$ 有關、$\boldsymbol{\epsilon}_B=-B^\mathsf{T}\boldsymbol{\epsilon}$ 只和 $\mathbf{b}$ 有關。
- 記號：非對角塊 $W=A^\mathsf{T}B$（左下是 $W^\mathsf{T}$）；對角塊加上 LM 的 $\lambda$ 後記作 $U^*$、$V^*$：

$$
\begin{pmatrix}U^* & W\\ W^\mathsf{T} & V^*\end{pmatrix}\begin{pmatrix}\boldsymbol{\delta}_\mathbf{a}\\\boldsymbol{\delta}_\mathbf{b}\end{pmatrix}=\begin{pmatrix}\boldsymbol{\epsilon}_A\\\boldsymbol{\epsilon}_B\end{pmatrix}
$$

（$U^*=U+\lambda I$、$V^*=V+\lambda I$ 的意思依 MVG A6.3 補上；$\boldsymbol{\epsilon}_A,\boldsymbol{\epsilon}_B$ 的正負號依第 29 集的 $J^\mathsf{T}J\boldsymbol{\delta}=-J^\mathsf{T}\boldsymbol{\epsilon}$。）

---

## 3. Schur 補

[▶ 04:48](https://youtu.be/J5OX0hipzd4?t=288)

**消去 $\boldsymbol{\delta}_\mathbf{b}$**：兩邊左乘

$$
\begin{pmatrix}I & -WV^{*-1}\\ \mathbf{0} & I\end{pmatrix}
$$

得到

$$
\begin{pmatrix}U^*-WV^{*-1}W^\mathsf{T} & \mathbf{0}\\ W^\mathsf{T} & V^*\end{pmatrix}\begin{pmatrix}\boldsymbol{\delta}_\mathbf{a}\\\boldsymbol{\delta}_\mathbf{b}\end{pmatrix}=\begin{pmatrix}\boldsymbol{\epsilon}_A-WV^{*-1}\boldsymbol{\epsilon}_B\\\boldsymbol{\epsilon}_B\end{pmatrix}
$$

- 右上變成 0（$W-WV^{*-1}V^*=0$）。

**第一列只剩 $\boldsymbol{\delta}_\mathbf{a}$** [▶ 05:30](https://youtu.be/J5OX0hipzd4?t=330)：

$$
\boxed{\ \left(U^*-WV^{*-1}W^\mathsf{T}\right)\boldsymbol{\delta}_\mathbf{a}=\boldsymbol{\epsilon}_A-WV^{*-1}\boldsymbol{\epsilon}_B\ }
$$

- $U^*-WV^{*-1}W^\mathsf{T}$ 叫 **Schur 補（Schur complement）**。
- 這個方程式比原來的**小很多**：只有 $\boldsymbol{\delta}_\mathbf{a}$（相機參數），不是 $\boldsymbol{\delta}_\mathbf{a}$ 和 $\boldsymbol{\delta}_\mathbf{b}$ 合起來。
- 而且係數矩陣**稀疏**，可以用各種分解法高效率地解。

**再回代求 $\boldsymbol{\delta}_\mathbf{b}$** [▶ 07:36](https://youtu.be/J5OX0hipzd4?t=456)：第二列

$$
V^*\boldsymbol{\delta}_\mathbf{b}=\boldsymbol{\epsilon}_B-W^\mathsf{T}\boldsymbol{\delta}_\mathbf{a}
$$

**更新** [▶ 08:18](https://youtu.be/J5OX0hipzd4?t=498)：$\mathbf{a}\leftarrow\mathbf{a}+\boldsymbol{\delta}_\mathbf{a}$、$\mathbf{b}\leftarrow\mathbf{b}+\boldsymbol{\delta}_\mathbf{b}$。$\lambda$ 照一般 LM 的規則調整（第 29 集），重複到收斂。

⚠️ 逐字稿缺字：Whisper 把 Schur 寫成 “Shear”。

---

## 4. Bundle adjustment 的稀疏結構

[▶ 09:27](https://youtu.be/J5OX0hipzd4?t=567)

關鍵：**不同相機的參數之間沒有交互作用**，**不同 3D 點之間也沒有**。

### 4.1 Jacobian 的哪些地方是 0

[▶ 09:47](https://youtu.be/J5OX0hipzd4?t=587)

**記號**：

- 第 $i$ 個 3D 點的觀測 $\mathbf{X}_i=(\mathbf{x}_{i1}^\mathsf{T},\mathbf{x}_{i2}^\mathsf{T},\dots)^\mathsf{T}$——它在各張圖的像。
  - 下標**不必連續**：允許**缺資料**（不是每張圖都看得到每個點），例如在第 1、2、5 張圖被看到。
- 相機參數 $\mathbf{a}_j$（第 $j$ 台，例如 12 維）；3D 點參數 $\mathbf{b}_i$。
- 重投影點 $\hat{\mathbf{x}}_{ij}$：第 $i$ 個點在第 $j$ 台相機的像。

**偏導數** [▶ 12:08](https://youtu.be/J5OX0hipzd4?t=728)：

$$
\frac{\partial\hat{\mathbf{x}}_{ij}}{\partial\mathbf{a}_k}=0\ \ (k\neq j),\qquad\frac{\partial\hat{\mathbf{x}}_{ij}}{\partial\mathbf{b}_k}=0\ \ (k\neq i)
$$

- 一個重投影點只依賴**那一台相機**和**那一個 3D 點**。

**例子** [▶ 14:28](https://youtu.be/J5OX0hipzd4?t=868)：第一台相機看到 4 個點 $\hat{\mathbf{x}}_{11},\dots,\hat{\mathbf{x}}_{14}$（講者的示意圖）。

- 對 $\mathbf{a}_1$（$P_1$）偏微分：非零。對 $\mathbf{a}_2$、$\mathbf{a}_3$：全是 0。
- $\hat{\mathbf{x}}_{11}$ 只依賴第一個 3D 點 $\mathbf{X}_1$，對其他點偏微分都是 0。
- Jacobian 大部分是 0，只有少數塊非零——**非常稀疏**。

### 4.2 JᵀJ 是鄰接矩陣

[▶ 19:07](https://youtu.be/J5OX0hipzd4?t=1147)

- $J^\mathsf{T}J=\begin{pmatrix}U&W\\W^\mathsf{T}&V\end{pmatrix}$：
  - $U$（相機–相機）、$V$（點–點）都是**分塊對角**（不同相機之間、不同點之間沒有交互作用）。
  - $W$（相機–點）的塊非零 ⟺ 那台相機看到那個點。
- 【口頭】[▶ 22:02](https://youtu.be/J5OX0hipzd4?t=1322) $J^\mathsf{T}J$ 其實就是「相機–點」關係圖的**鄰接矩陣（adjacency matrix）**：例如點 A 被相機 1、2 看到、點 B 被相機 1、2、4 看到，這些關係就是 $W$ 裡哪些塊非零。

【課本補充】MVG A6.6：$V$ 是分塊對角，每個 3D 點一個 $3\times3$ 塊 → $V^{*-1}$ 只要對每個 $3\times3$ 塊各自求逆，非常便宜。

### 4.3 為什麼 Schur 補特別划算

[▶ 24:21](https://youtu.be/J5OX0hipzd4?t=1461)

- 一般重建中，**相機數遠少於 3D 點數**。
- Schur 補把方程式縮成只含相機參數的 $12n\times12n$（$n$ 台相機），而不是 $(12n+3m)\times(12n+3m)$。
- $V^*$ 分塊對角、對稱正定 → 逆一定存在且好算。
- 解出 $\boldsymbol{\delta}_\mathbf{a}$ 後，$\boldsymbol{\delta}_\mathbf{b}$ 對每個點各自回代。

---

## 5. 解線性方程式：LU、QR、Cholesky

[▶ 26:27](https://youtu.be/J5OX0hipzd4?t=1587)

$A\mathbf{x}=\mathbf{b}$ 的常用分解（講者說大學線性代數教過，推薦 Gilbert Strang《Introduction to Linear Algebra》和他的線上課）：

| 分解 | 寫法 | 怎麼解 |
|---|---|---|
| **LU** | $A=LU$（下三角 × 上三角） | 令 $\mathbf{y}=U\mathbf{x}$：先解 $L\mathbf{y}=\mathbf{b}$（**前向代入**：從第一個元素往下），再解 $U\mathbf{x}=\mathbf{y}$（**回代**：從最後一個元素往上） |
| **QR** | $A=QR$（正交 × 三角） | $Q^{-1}=Q^\mathsf{T}$：$R\mathbf{x}=Q^\mathsf{T}\mathbf{b}$，再回代；不必求逆 |
| **Cholesky** | $A=LL^\mathsf{T}$（$A$ 對稱正定） | 同 LU；**LM 的正規方程式最常用** |

- 也有迭代法：**共軛梯度（conjugate gradient）**、**Gauss–Seidel**。

⚠️ 逐字稿缺字：Whisper 把 Gauss–Seidel 寫成 “Gauss-Snyder”；把 orthogonal 寫成 “octagonal”。

---

## 6. 填入問題與重新排序

[▶ 30:52](https://youtu.be/J5OX0hipzd4?t=1852)

**填入（fill-in）**：

- 對一個**稀疏**的 $A$ 直接做 Cholesky 分解 $A=LL^\mathsf{T}$，得到的 $L$ 常常比 $A$ **稠密得多**。
- $L$ 越稠密，前向代入／回代越慢。

**解法：用置換矩陣重新排序** [▶ 32:18](https://youtu.be/J5OX0hipzd4?t=1938)：

- 改分解 $P^\mathsf{T}AP$。$P$ 是**置換矩陣（permutation matrix）**：元素只有 0、1，每列、每行恰好一個 1——只是把列和行重新排列。
- **找最好的排序是 NP-complete**，只能用近似演算法：
  - 最小度（minimum degree）
  - 行近似最小度（column approximate minimum degree）
  - 反向 Cuthill–McKee（reverse Cuthill–McKee）
  - 巢狀剖分（nested dissection）

⚠️ 逐字稿缺字：Whisper 把 Cuthill–McKee 寫成 “McCutcheon-Mckee”。

**講者的例子** [▶ 34:13](https://youtu.be/J5OX0hipzd4?t=2053)：

- 一個稀疏矩陣，重新排序前後非零元素個數不變（只是換位置）。
- 直接 Cholesky：$L$ 約有 606,000 個非零元素。
- 重新排序後再 Cholesky：例如最小度排序約 52,988 個；反向 Cuthill–McKee 約 78,120 個。
- 這個例子裡**巢狀剖分**最好。
- 非零元素越少，每次迭代解正規方程式越快。

> 以下**不是逐字稿內容**：逐字稿中幾個數字（「18,441」、「8.28%」）和上面的數字之間的關係口述不清楚；這個例子看起來像 Matlab 稀疏矩陣排序的示範，確切數字以投影片為準，重點是「重新排序可大幅減少填入」。

---

## 7. 開源工具

[▶ 37:46](https://youtu.be/J5OX0hipzd4?t=2266)【口頭】

不必從頭寫：

| 工具 | 常見用途 |
|---|---|
| **Ceres Solver**（Google） | 電腦視覺社群做 SfM 最常用 |
| **g2o** | 機器人社群，視覺 SLAM |
| **GTSAM** | 機器人社群，視覺 SLAM |

⚠️ 逐字稿缺字：Whisper 把 Ceres 寫成 “series”。

---

## 8. Lecture 10 總結

[▶ 38:21](https://youtu.be/J5OX0hipzd4?t=2301)

1. 大規模 3D 重建的流程：資料關聯、SfM（稠密立體留到下一講）（第 27 集）。
2. 用強健雙視角幾何和詞袋演算法做資料關聯（第 27 集）。
3. 用雙視角幾何、PnP、線性三角化初始化 3D 重建（第 28 集）。
4. bundle adjustment 的定義，用 Newton、Gauss–Newton、LM 做 BA（第 29 集、本集）。

---

## 9. 一頁速查表

### 稀疏 LM

| 步驟 | 公式 |
|---|---|
| 分組 | $\mathbf{p}=(\mathbf{a};\mathbf{b})$，$J=[A\mid B]$ |
| 正規方程式 | $\begin{pmatrix}U^*&W\\W^\mathsf{T}&V^*\end{pmatrix}\begin{pmatrix}\boldsymbol{\delta}_\mathbf{a}\\\boldsymbol{\delta}_\mathbf{b}\end{pmatrix}=\begin{pmatrix}\boldsymbol{\epsilon}_A\\\boldsymbol{\epsilon}_B\end{pmatrix}$ |
| Schur 補 | $(U^*-WV^{*-1}W^\mathsf{T})\boldsymbol{\delta}_\mathbf{a}=\boldsymbol{\epsilon}_A-WV^{*-1}\boldsymbol{\epsilon}_B$（左乘 $\begin{pmatrix}I&-WV^{*-1}\\0&I\end{pmatrix}$） |
| 回代 | $V^*\boldsymbol{\delta}_\mathbf{b}=\boldsymbol{\epsilon}_B-W^\mathsf{T}\boldsymbol{\delta}_\mathbf{a}$ |

### BA 稀疏性

- $\partial\hat{\mathbf{x}}_{ij}/\partial\mathbf{a}_k=0$（$k\ne j$）、$\partial\hat{\mathbf{x}}_{ij}/\partial\mathbf{b}_k=0$（$k\ne i$）。
- $U$、$V$ 分塊對角；$W$ = 相機–點可見性（鄰接矩陣）。
- 相機數 ≪ 點數 → Schur 補只解 $12n\times12n$；$V^{*-1}$ 逐點 $3\times3$ 求逆。

### 解線性系統

- LU／QR／Cholesky（$LL^\mathsf{T}$，LM 最常用）；迭代：共軛梯度、Gauss–Seidel。
- 填入：$P^\mathsf{T}AP$ 重新排序（最小度、COLAMD、反向 Cuthill–McKee、巢狀剖分；最佳排序是 NP-complete）。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 相機位姿 + 稀疏點雲（BA 的輸出） | 第 31–34 集（Lecture 11：稠密雙視角、多視角立體） |
| 稀疏最佳化 | 第 38–39 集（點雲處理、神經場中的最佳化） |
| 非線性最小平方 | 第 35–37 集（廣義相機的位姿估計精修） |

---

## 附：本集一句話總結

> **直接解 BA 的正規方程式是 $O(N^3)$，但參數可以分成相機 $\mathbf{a}$ 和 3D 點 $\mathbf{b}$：每個重投影點只依賴一台相機、一個點，所以 $J^\mathsf{T}J$ 的 $U$、$V$ 是分塊對角、$W$ 只在「相機看得到點」處非零；用 Schur 補先解小得多的相機方程式 $(U^*-WV^{*-1}W^\mathsf{T})\boldsymbol{\delta}_\mathbf{a}=\cdots$，再逐點回代 $\boldsymbol{\delta}_\mathbf{b}$，解線性系統時用 Cholesky 並重新排序避免填入——實務上直接用 Ceres、g2o、GTSAM。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 10 (Part 4) 錄影逐字稿（Whisper `medium.en`，39:28）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 附錄 A6.3、A6.6–A6.7 整理。*
