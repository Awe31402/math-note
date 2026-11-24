---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 09
lecture: Lecture 4 (Part 2) – Robust homography estimation
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/v3322cNhCTk
notes: MVG §4.2（書頁 93–101，PDF 頁 111–119）、§4.5（迭代最小化）、§4.7–4.8（書頁 116–125，PDF 頁 134–143）
---

# 第 09 集 · Lecture 4 (Part 2)：代數誤差、幾何誤差、Sampson 誤差、RANSAC [▶ 影片](https://youtu.be/v3322cNhCTk)

← 上一集：[08-robust-homography-part1](08-robust-homography-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[10-camera-models-calibration-part1](10-camera-models-calibration-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 09 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（43:25，Whisper `medium.en` 轉錄）＋ MVG §4.2、§4.5、§4.7–4.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 代數誤差](#1-代數誤差)
- [2. 幾何誤差](#2-幾何誤差)
  - [2.1 單張影像的轉移誤差](#21-單張影像的轉移誤差)
  - [2.2 對稱轉移誤差](#22-對稱轉移誤差)
  - [2.3 重投影誤差](#23-重投影誤差)
- [3. Sampson 誤差](#3-sampson-誤差)
- [4. 迭代最小化](#4-迭代最小化)
- [5. 錯誤對應（outliers）](#5-錯誤對應outliers)
- [6. RANSAC](#6-ransac)
  - [6.1 用擬合直線說明](#61-用擬合直線說明)
  - [6.2 演算法](#62-演算法)
  - [6.3 三個參數怎麼選](#63-三個參數怎麼選)
  - [6.4 要試幾次：N 的公式](#64-要試幾次n-的公式)
  - [6.5 自適應決定 N](#65-自適應決定-n)
- [7. 強健 homography 估計完整流程](#7-強健-homography-估計完整流程)
- [8. Lecture 4 總結](#8-lecture-4-總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 代數誤差、幾何誤差（轉移、對稱轉移、重投影）、Sampson 誤差 | §4.2 |
| 用迭代法最小化幾何／Sampson 誤差 | §4.5 |
| RANSAC 強健估計、自適應決定迭代次數 | §4.7 |
| 強健 homography 估計的完整流程 | §4.8 |

---

## 1. 代數誤差

[▶ 00:00](https://youtu.be/v3322cNhCTk?t=0)

- 上一集的 DLT 最小化 $\|A\mathbf{h}\|$。令 $\boldsymbol{\epsilon}=A\mathbf{h}$，叫**殘差向量（residual vector）**。
- 每對點 $\mathbf{x}_i\leftrightarrow\mathbf{x}_i'$ 貢獻其中一段 $\boldsymbol{\epsilon}_i=A_i\mathbf{h}$（2 維）。它的長度叫**代數誤差（algebraic error）**或**代數距離（algebraic distance）**：
$$
d_{\text{alg}}(\mathbf{x}_i',H\mathbf{x}_i)^2=\|\boldsymbol{\epsilon}_i\|^2=\|A_i\mathbf{h}\|^2
$$
- 全部點的總代數誤差：
$$
\sum_id_{\text{alg}}(\mathbf{x}_i',H\mathbf{x}_i)^2=\sum_i\|A_i\mathbf{h}\|^2=\|A\mathbf{h}\|^2
$$

**優缺點** [▶ 01:47](https://youtu.be/v3322cNhCTk?t=107)：

| 缺點 | 優點 |
|---|---|
| 沒有幾何或統計上的意義——只是線性代數式子，不是影像上或 3D 裡真正的距離 | 線性解，**唯一** |
| 結果不如幾何誤差準 | 計算便宜 |

**用法** [▶ 02:42](https://youtu.be/v3322cNhCTk?t=162)：先用代數誤差（DLT + SVD）得到初始解，再用**幾何誤差**做**非線性最小化**來「精修」。

---

## 2. 幾何誤差

[▶ 03:57](https://youtu.be/v3322cNhCTk?t=237)

**幾何距離**：影像上**量到的**座標和**估計的**座標之間的差。

### 2.1 單張影像的轉移誤差

[▶ 04:05](https://youtu.be/v3322cNhCTk?t=245)

- 第一張圖的 $\mathbf{x}_i$ 用 $H$ 轉移到第二張圖，得 $H\mathbf{x}_i$。
- $H$ 是用有雜訊的資料估的，所以 $H\mathbf{x}_i$ 不會剛好落在觀測點 $\mathbf{x}_i'$ 上。
- **轉移誤差（transfer error）**：第二張圖上兩點的歐氏距離。

$$
\min_H\ \sum_id(\mathbf{x}_i',H\mathbf{x}_i)^2
$$

（$d(\cdot,\cdot)$ 是用非齊次座標算的歐氏距離。）

### 2.2 對稱轉移誤差

[▶ 05:56](https://youtu.be/v3322cNhCTk?t=356)

只看一個方向不太合理，兩個方向都算：

$$
\min_H\ \sum_i\left[d(\mathbf{x}_i,H^{-1}\mathbf{x}_i')^2+d(\mathbf{x}_i',H\mathbf{x}_i)^2\right]
$$

- 第一項：$\mathbf{x}_i'$ 用 $H^{-1}$ 轉回第一張圖的誤差。
- 第二項：$\mathbf{x}_i$ 用 $H$ 轉到第二張圖的誤差。
- 叫**對稱轉移誤差（symmetric transfer error）**。

### 2.3 重投影誤差

[▶ 07:55](https://youtu.be/v3322cNhCTk?t=475)

想法：找一個 $\hat{H}$ 和一組「**完美的**」對應點 $\hat{\mathbf{x}}_i\leftrightarrow\hat{\mathbf{x}}_i'$，使 $\hat{H}$ 把 $\hat{\mathbf{x}}_i$ **剛好**送到 $\hat{\mathbf{x}}_i'$；同時讓完美點離觀測點越近越好。

$$
\min_{\hat{H},\ \hat{\mathbf{x}}_i,\ \hat{\mathbf{x}}_i'}\ \sum_i\left[d(\mathbf{x}_i,\hat{\mathbf{x}}_i)^2+d(\mathbf{x}_i',\hat{\mathbf{x}}_i')^2\right]\quad\text{subject to}\quad \hat{\mathbf{x}}_i'=\hat{H}\hat{\mathbf{x}}_i\ \ \forall i
$$

- $\hat{\mathbf{x}}_i$、$\hat{\mathbf{x}}_i'$ 叫**輔助點（subsidiary points）**。
- **最準**：比對稱轉移誤差和代數誤差都準，因為不只最佳化 $H$，連「真正的點在哪」也一起最佳化。
- **最貴**：多了一堆要最佳化的變數（每個點的 $\hat{\mathbf{x}}_i$），和代數誤差的簡單差很多。

⚠️ 逐字稿缺字 [▶ 08:52](https://youtu.be/v3322cNhCTk?t=532)：講者說「transfer another point $\hat{\mathbf{x}}_i$ to exactly the point where I desire, which I call $\hat{\mathbf{x}}_i$」，第二個應為 $\hat{\mathbf{x}}_i'$。

**直覺**：觀測點有雜訊。重投影誤差問的是：「最少要把觀測點挪動多少，才能讓它們完全符合某個 homography？」挪動量就是誤差。

---

## 3. Sampson 誤差

[▶ 11:21](https://youtu.be/v3322cNhCTk?t=681)

**定位**：介於代數誤差和重投影誤差之間——計算量接近代數誤差，準確度接近重投影誤差。

**推導** [▶ 11:51](https://youtu.be/v3322cNhCTk?t=711)：

1. **把代數誤差看成點的函數**。對一對點，令 $\mathbf{X}=(x,y,x',y')^\mathsf{T}$（4 維），代數誤差 $A_i\mathbf{h}$ 是 $\mathbf{X}$ 的函數（因為 $A_i$ 由 $\mathbf{X}$ 組成）：
$$
\mathcal{C}_H(\mathbf{X})=A_i(\mathbf{X})\,\mathbf{h}
$$
2. **理想點**：$\hat{\mathbf{X}}$ 滿足 $\mathcal{C}_H(\hat{\mathbf{X}})=\mathbf{0}$。令誤差 $\boldsymbol{\delta}_\mathbf{X}=\hat{\mathbf{X}}-\mathbf{X}$（觀測值被雜訊偏移了多少）。這就是重投影誤差想求的東西。
3. **一階泰勒展開** [▶ 13:13](https://youtu.be/v3322cNhCTk?t=793)：
$$
\mathcal{C}_H(\mathbf{X}+\boldsymbol{\delta}_\mathbf{X})\approx\mathcal{C}_H(\mathbf{X})+\frac{\partial\mathcal{C}_H}{\partial\mathbf{X}}\boldsymbol{\delta}_\mathbf{X}=\mathbf{0}
$$
   令 $J=\dfrac{\partial\mathcal{C}_H}{\partial\mathbf{X}}$（Jacobian）、$\boldsymbol{\epsilon}=\mathcal{C}_H(\mathbf{X})$（代數誤差），得
$$
J\boldsymbol{\delta}_\mathbf{X}=-\boldsymbol{\epsilon}
$$
4. **問題變成**：找最短的 $\boldsymbol{\delta}_\mathbf{X}$，滿足這個線性約束：
$$
\min\ \|\boldsymbol{\delta}_\mathbf{X}\|\quad\text{subject to}\quad J\boldsymbol{\delta}_\mathbf{X}=-\boldsymbol{\epsilon}
$$
5. **解：右偽逆（right pseudo-inverse）** [▶ 14:49](https://youtu.be/v3322cNhCTk?t=889)：
$$
\boldsymbol{\delta}_\mathbf{X}=-J^\mathsf{T}(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}
$$
6. **Sampson 誤差**就是它的平方長度：
$$
\|\boldsymbol{\delta}_\mathbf{X}\|^2=\boldsymbol{\delta}_\mathbf{X}^\mathsf{T}\boldsymbol{\delta}_\mathbf{X}=\boldsymbol{\epsilon}^\mathsf{T}(JJ^\mathsf{T})^{-1}JJ^\mathsf{T}(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}=\boldsymbol{\epsilon}^\mathsf{T}(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}
$$

（公式依 MVG 式 (4.11)–(4.12) 寫出；逐字稿只說「由這個式子給出」。）

> 以下**不是逐字稿內容**，是步驟 5 的推導（MVG §4.2.6 用 Lagrange 乘子）：最小化 $\boldsymbol{\delta}^\mathsf{T}\boldsymbol{\delta}-2\boldsymbol{\lambda}^\mathsf{T}(J\boldsymbol{\delta}+\boldsymbol{\epsilon})$。對 $\boldsymbol{\delta}$ 微分設 0：$\boldsymbol{\delta}=J^\mathsf{T}\boldsymbol{\lambda}$。代回約束：$JJ^\mathsf{T}\boldsymbol{\lambda}=-\boldsymbol{\epsilon}$ → $\boldsymbol{\lambda}=-(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}$ → $\boldsymbol{\delta}=-J^\mathsf{T}(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}$。

**用在 homography** [▶ 15:42](https://youtu.be/v3322cNhCTk?t=942)：

- $\mathbf{X}=(x,y,x',y')^\mathsf{T}$：一對對應點。
- $\boldsymbol{\epsilon}=A_i\mathbf{h}$：2 維。
- $J$：2 維的 $\boldsymbol{\epsilon}$ 對 4 個變數各微分一次 → $2\times4$ 矩陣：
$$
J=\begin{pmatrix}\dfrac{\partial\boldsymbol{\epsilon}}{\partial x} & \dfrac{\partial\boldsymbol{\epsilon}}{\partial y} & \dfrac{\partial\boldsymbol{\epsilon}}{\partial x'} & \dfrac{\partial\boldsymbol{\epsilon}}{\partial y'}\end{pmatrix}
$$
- 講者給了第一個元素 $J_{11}$，其他留作練習。

> 以下**不是逐字稿內容**：$J_{11}$ 的式子逐字稿沒唸出來，依 MVG §4.2.6：$\boldsymbol{\epsilon}$ 的第一個分量是 $-w_i'\mathbf{x}_i^\mathsf{T}\mathbf{h}^2+y_i'\mathbf{x}_i^\mathsf{T}\mathbf{h}^3$，對 $x$ 微分得 $J_{11}=-w_i'h_{21}+y_i'h_{31}$。

- **閉式解**：Sampson 誤差可以直接算出來，不用迭代就能評估。

【課本補充】（MVG §4.2.6）

- 名字來自 Sampson（1982），他把這個近似用在二次曲線擬合。
- 如果約束本來就是 $\mathbf{X}$ 的線性函數（例如仿射變換），Sampson 誤差和幾何誤差**完全相同**。

---

## 4. 迭代最小化

[▶ 17:31](https://youtu.be/v3322cNhCTk?t=1051)

幾何誤差和 Sampson 誤差通常寫成**平方 Mahalanobis 距離**來最小化：

$$
\min_\mathbf{P}\ \|\mathbf{X}-f(\mathbf{P})\|_\Sigma^2
$$

- $\mathbf{X}$：量測向量（觀測值）。
- $\mathbf{P}$：要最佳化的參數。
- $f$：把參數映到預測量測的函數（$\mathbb{R}^M\to\mathbb{R}^N$）。
- $\Sigma$：量測誤差的共變異數矩陣；**不知道時設成 $I$**，就變成普通的平方歐氏距離。
- 這是**無約束連續最佳化**，用 **Gauss–Newton** 或 **Levenberg–Marquardt** 解。講者說細節留到 Lecture 10（bundle adjustment、structure from motion）。

⚠️ 逐字稿缺字：Whisper 把 Levenberg–Marquardt 寫成 “Levenberg-Macquaire”。

**四種誤差各自怎麼設定** [▶ 19:20](https://youtu.be/v3322cNhCTk?t=1160)：

| 誤差 | 量測向量 $\mathbf{X}$ | 參數 $\mathbf{P}$ | 映射 $f$ |
|---|---|---|---|
| 單張影像轉移 | $2N$ 維：所有 $\mathbf{x}_i'$（非齊次） | $H$ | $\mathbf{x}_i\mapsto H\mathbf{x}_i$（$\mathbf{x}_i$ 當固定輸入） |
| 對稱轉移 | $4N$ 維：所有 $\mathbf{x}_i,\mathbf{x}_i'$ | $H$ | $(H^{-1}\mathbf{x}_i',\ H\mathbf{x}_i)$——每張圖一項 |
| 重投影 | $4N$ 維：所有 $\mathbf{x}_i,\mathbf{x}_i'$ | $H$ 和所有 $\hat{\mathbf{x}}_i$ | $\hat{\mathbf{x}}_i\mapsto(\hat{\mathbf{x}}_i,\ H\hat{\mathbf{x}}_i)$ |
| Sampson | 每對點 $(x,y,x',y')$ | $H$ | 直接令 $\mathbf{X}-f(H)=\boldsymbol{\delta}_\mathbf{X}$，平方長度就是 Sampson 誤差 |

【課本補充】MVG §4.5：重投影誤差要最佳化 $2N+9$ 個參數（每點 2 個 + $H$ 的 9 個）；Sampson 誤差等於對每個 $H$ 直接用閉式算出那 $2N$ 個變數，所以只要最佳化 $H$。

---

## 5. 錯誤對應（outliers）

[▶ 23:06](https://youtu.be/v3322cNhCTk?t=1386)

- 到目前為止，假設對應點只有**小的量測雜訊**——最小平方法對這種小擾動很強健。
- 但實際上，**特徵點匹配會產生很多錯誤對應（outliers）**（講者投影片上用紅線標出）。
- 錯誤對應會**嚴重**干擾最小平方法，得到完全錯誤的解。
- 所以要在丟進最小平方之前，先找出並移除錯誤對應。

【口頭】[▶ 24:21](https://youtu.be/v3322cNhCTk?t=1461) 講者推薦網路上（YouTube）有一首描述 RANSAC 演算法的歌，說「聽得懂歌詞就完全懂 RANSAC 了」，並用歌裡的擬合直線例子來說明。

---

## 6. RANSAC

### 6.1 用擬合直線說明

[▶ 25:00](https://youtu.be/v3322cNhCTk?t=1500)

**問題**：給 $N$ 個點 $(x_i,y_i)$，找最佳直線 $y=mx+c$（求 $m$、$c$）。

**最小平方法** [▶ 26:01](https://youtu.be/v3322cNhCTk?t=1561)：

$$
\min_{m,c}\ \sum_i\left(y_i-(mx_i+c)\right)^2
$$

- 所有點都是**內點（inliers）**（只有微小雜訊）時，效果很好。
- 有**離譜的量測**時，因為是**平方**誤差，離得遠的點貢獻巨大的誤差，把解**拉離**真正的直線 → 最小平方法失敗。

**RANSAC 步驟（直線版）** [▶ 28:16](https://youtu.be/v3322cNhCTk?t=1696)：

1. **隨機選最小子集**：直線有 2 個未知數 $m,c$，所以選 **2 個點**。
2. **擬合假設**：代入 2 點解出 $m,c$，得一條假設直線。
3. **算誤差**：其他每個點到這條線的**垂直距離**。
4. **分類**：設門檻 $t$（講者寫 $\sigma_d$）。距離 $d<t$ → 內點；$d>t$ → 錯誤對應。這次假設的內點叫**支持集（support set）**。
5. **重複**：隨機選很多次 2 點，每次記下支持集的大小（基數）。
6. **選最好的**：支持集最大的那個假設。
7. **最後重估**：只用它的內點做一次最小平方，忽略所有錯誤對應。

### 6.2 演算法

[▶ 32:17](https://youtu.be/v3322cNhCTk?t=1937)

**在解什麼**：資料集 $S$ 含有錯誤對應，要強健地擬合一個模型。

**步驟**（MVG Algorithm 4.4）：

1. 從 $S$ 隨機選 $s$ 個資料點，擬合模型（產生假設）。
2. 找出距離模型小於門檻 $t$ 的點，叫**共識集（consensus set）** / 支持集。
3. 重複 $N$ 次，選共識集最大的那次。
4. 用那次的所有內點重新估計模型。

**什麼時候會失敗**：

- $N$ 太小 → 可能一次都沒選到「全是內點」的樣本。
- 門檻 $t$ 設太大 → 錯誤對應被當成內點；太小 → 好點被丟掉。
- 錯誤對應比例太高 → 需要的 $N$ 爆炸（見 6.4）。

> 以下**不是逐字稿內容**，是依演算法推論的補充：如果錯誤對應彼此「串通」（例如場景裡有兩個平面，各自都有很多一致的對應），RANSAC 會選到支持集最大的那一個模型，另一群好點反而被當成錯誤對應。

### 6.3 三個參數怎麼選

[▶ 34:04](https://youtu.be/v3322cNhCTk?t=2044)

| 參數 | 意義 | 通常怎麼選 |
|---|---|---|
| $s$ | 每次取幾個點 | **擬合模型所需的最少點數**：直線 2、homography 4 |
| $t$ | 內點／錯誤對應的距離門檻 | 憑經驗，或設成 **3σ** |
| $N$ | 試幾次 | 不能太小（可能找不到好解），不能太大（算不完）；用 6.4 的公式 |

【課本補充】MVG Table 4.2：假設量測誤差是標準差 $\sigma$ 的高斯雜訊，要讓 95% 的內點被接受，門檻是 $t^2=F_m^{-1}(0.95)\sigma^2$（$F_m$ 是自由度 $m$ 的 $\chi^2$ 分布）：

| 自由度 $m$ | 模型 | $t^2$ |
|---|---|---|
| 1 | 直線、fundamental matrix | $3.84\sigma^2$ |
| 2 | homography、相機矩陣 | $5.99\sigma^2$ |
| 3 | trifocal tensor | $7.81\sigma^2$ |

### 6.4 要試幾次：N 的公式

[▶ 35:27](https://youtu.be/v3322cNhCTk?t=2127)

窮舉所有樣本通常沒必要也做不到。RANSAC 原始論文給了一個統計公式。

**符號**：

- $w$：任選一點是**內點**的機率。
- $s$：每次選幾個點。
- $p$：希望「$N$ 次裡至少有一次選到的 $s$ 點全是內點」的機率（例如 0.99）。

**推導** [▶ 36:44](https://youtu.be/v3322cNhCTk?t=2204)：

1. 選到的 $s$ 點**全是內點**的機率：$w^s$。
2. **至少有一個錯誤對應**的機率：$1-w^s$。
3. $N$ 次**每次都至少有一個錯誤對應**（從來沒選到全內點）的機率：$(1-w^s)^N$。
4. 這等於 $1-p$：
$$
1-p=(1-w^s)^N
$$
5. 解出 $N$（兩邊取 log）：
$$
N=\frac{\log(1-p)}{\log(1-w^s)}
$$

**表格** [▶ 38:14](https://youtu.be/v3322cNhCTk?t=2294)：$N$ 對樣本大小 $s$ 和錯誤對應比例 $\epsilon=1-w$。

- $\epsilon=50\%$ 時，$s$ 從 2 到 8，$N$ 從 **17** 增加到 **1177**——**隨 $s$ 指數成長**。
- 所以 $s$ 要越小越好 → 用**最小點數**（上一集說的「最小解對 RANSAC 很重要」）。

> 以下**不是逐字稿內容**，是驗算表中兩個數（$p=0.99$）：$s=2$：$N=\log0.01/\log(1-0.25)=-4.605/-0.2877\approx16.006$，無條件進位得 17；$s=8$：$N=\log0.01/\log(1-1/256)=-4.605/-0.003914\approx1177$。MVG Table 4.3 列出完整表格。

- **$w$ 怎麼定**：可以取最壞情況 50%（一半是錯誤對應）。

### 6.5 自適應決定 N

[▶ 39:35](https://youtu.be/v3322cNhCTk?t=2375)

事先不知道 $w$ 時，邊跑邊更新：

1. 初始 $N=\infty$，計數器 sample_count $=0$。
2. 每次試驗：選樣本、算假設、數內點。
3. 用這次的內點比例更新 $w=\dfrac{\text{內點數}}{\text{總點數}}$（取目前看過最好的）。
4. 用新的 $w$ 重算 $N=\dfrac{\log(1-p)}{\log(1-w^s)}$。
5. sample_count 加 1。
6. sample_count $>N$ 就停。

（MVG Algorithm 4.5。）

---

## 7. 強健 homography 估計完整流程

[▶ 40:47](https://youtu.be/v3322cNhCTk?t=2447)

**在解什麼**：兩張圖之間的 homography，但對應點裡有錯誤對應。

**步驟**（MVG Algorithm 4.6 的課堂版本）：

1. **特徵點**：在兩張圖上各找特徵點（interest points）。
2. **初步對應（putative correspondences）**：用描述子（例如 SIFT、SURF）配對。這一步會有很多錯誤對應。
3. **RANSAC**，重複 $N$ 次（$N$ 自適應決定）：
   1. 隨機選 **4 對**對應點（homography 的最小集）。
   2. 用這 4 對算 $H$（DLT）。
   3. 其他每對對應點用 $H$ 轉移，算幾何誤差（**Sampson 誤差**或**對稱轉移誤差**）。
   4. 誤差 $<t$ 的算內點，數一數有幾個。
4. **選最好的 $H$**：內點最多的那個。
5. **重估**：用所有內點重新估計 $H$（例如正規化 DLT 再做非線性精修）。

⚠️ 逐字稿缺字 [▶ 41:50](https://youtu.be/v3322cNhCTk?t=2510)：講者說「compute the number of outliers ... which is lesser than D」，依上下文應為「數**內點**（誤差小於門檻的）」。

---

## 8. Lecture 4 總結

[▶ 43:04](https://youtu.be/v3322cNhCTk?t=2584)

1. 兩種情況下 homography 存在（第 08 集）。
2. 代數、幾何、Sampson 誤差的差別，用在 homography 估計上。
3. RANSAC 強健估計。

⚠️ 逐字稿缺字：Whisper 把 Sampson 寫成 “Samsung”、“Samson”、“sensor”。

---

## 9. 一頁速查表

### 四種誤差（由便宜到準）

| 誤差 | 式子 | 特點 |
|---|---|---|
| 代數 | $\sum_i\|A_i\mathbf{h}\|^2$ | 線性、唯一、便宜；沒幾何意義 → 當初值 |
| 單向轉移 | $\sum_id(\mathbf{x}_i',H\mathbf{x}_i)^2$ | 只看第二張圖 |
| 對稱轉移 | $\sum_i d(\mathbf{x}_i,H^{-1}\mathbf{x}_i')^2+d(\mathbf{x}_i',H\mathbf{x}_i)^2$ | 兩個方向 |
| Sampson | $\boldsymbol{\epsilon}^\mathsf{T}(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}$ | 重投影誤差的一階近似，閉式 |
| 重投影 | $\sum_id(\mathbf{x}_i,\hat{\mathbf{x}}_i)^2+d(\mathbf{x}_i',\hat{\mathbf{x}}_i')^2$，$\hat{\mathbf{x}}_i'=\hat{H}\hat{\mathbf{x}}_i$ | 最準、最貴（$2N+9$ 參數） |

**Sampson 關鍵一步**：$\mathcal{C}(\mathbf{X}+\boldsymbol{\delta})\approx\boldsymbol{\epsilon}+J\boldsymbol{\delta}=0$，求最短 $\boldsymbol{\delta}=-J^\mathsf{T}(JJ^\mathsf{T})^{-1}\boldsymbol{\epsilon}$（右偽逆）。

### RANSAC

| 項目 | 內容 |
|---|---|
| 參數 | $s$（最少點數）、$t$（門檻，約 $3\sigma$；MVG homography $t^2=5.99\sigma^2$）、$N$ |
| $N$ | $N=\dfrac{\log(1-p)}{\log(1-w^s)}$；關鍵一步 $1-p=(1-w^s)^N$ |
| 例 | $\epsilon=50\%$：$s=2$ → 17，$s=8$ → 1177 |
| 自適應 | 每次用最好的內點比例更新 $w$、重算 $N$，次數超過 $N$ 就停 |
| 最後 | 用最大共識集的所有內點重估 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 代數誤差當初值、幾何誤差精修 | 第 10–12 集（相機矩陣估計）；第 16–19 集（$F$ 的估計） |
| 重投影誤差 | 第 27–30 集（bundle adjustment 就是最小化所有相機、所有點的重投影誤差） |
| Gauss–Newton、Levenberg–Marquardt | 第 27–30 集（Lecture 10 細講） |
| Sampson 誤差 | 第 16–19 集（$F$ 矩陣的 Sampson 距離） |
| RANSAC、最小解 | 第 16–19 集（7 點／8 點法 + RANSAC）；第 20–22 集（P3P + RANSAC） |
| 門檻 $t^2=F_m^{-1}(\alpha)\sigma^2$ | 第 16–19 集（$F$ 是 $m=1$） |

---

## 附：本集一句話總結

> **DLT 最小化的是沒有幾何意義的代數誤差，只適合當初值；真正該最小化的是幾何誤差（轉移、對稱轉移、最準但最貴的重投影誤差），Sampson 誤差用一階近似把重投影誤差變成閉式；而遇到錯誤對應時，先用 RANSAC 反覆抽最少點數擬合、數內點、選共識最大的，再用內點重估——試驗次數 $N=\log(1-p)/\log(1-w^s)$ 隨樣本大小指數成長，所以要用最小解。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 4 (Part 2) 錄影逐字稿（Whisper `medium.en`，43:25）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §4.2、§4.5、§4.7–4.8 整理。*
