---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-12
lecture: Graph-Based SLAM with Landmarks
date: 待補（2021 夏季學期）
video: https://youtu.be/mZBdPgBtrCM
notes: 《視覺 SLAM 十四講》第 2 版 §9.2（書頁 243–251，PDF 頁 266–274）；MVG §18.1（書頁 434–435，PDF 頁 452–453）
---

# 第 2-12 集 · 有地標的圖式 SLAM [▶ 影片](https://youtu.be/mZBdPgBtrCM)

← 上一集：[2-11-graph-slam-pose-graphs](2-11-graph-slam-pose-graphs.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-14-hierarchical-pose-graphs](2-14-hierarchical-pose-graphs.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-12 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（28:27，Whisper `medium.en` 轉錄）＋《視覺 SLAM 十四講》§9.2 ＋ MVG §18.1
> **標記說明**：
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習位姿圖](#1-複習位姿圖)
- [2. 地標圖：兩種節點、兩種邊](#2-地標圖兩種節點兩種邊)
- [3. 位姿–地標的邊](#3-位姿地標的邊)
  - [3.1 xy 感測器](#31-xy-感測器)
  - [3.2 只有方位的感測器](#32-只有方位的感測器)
- [4. H 的秩](#4-h-的秩)
- [5. Levenberg-Marquardt](#5-levenberg-marquardt)
- [6. 和光束法平差的關係](#6-和光束法平差的關係)
- [7. 總結](#7-總結)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

把 2-11 的位姿圖擴充：圖裡除了**位姿節點**，還有**地標節點**（環境中可辨認的點）。重點：新的「位姿–地標」邊長什麼樣、單一觀測的 **H 秩不足**，以及因此常改用 **Levenberg-Marquardt**。

---

## 1. 複習位姿圖

[▶ 00:27](https://youtu.be/mZBdPgBtrCM?t=27)

- 節點：機器人某時刻的位姿（2D：$x, y, \theta$；3D：$x, y, z$ 加三個角度）。
- 邊：節點間的空間約束（相對轉換），來自連續運動或閉合迴圈（虛擬觀測）。
- 約束會互相衝突（感測雜訊、不完美的資料關聯）→ 找讓誤差最小的組態。

---

## 2. 地標圖：兩種節點、兩種邊

[▶ 02:37](https://youtu.be/mZBdPgBtrCM?t=157)

- **地標**：環境中可以認出來的特定點。經典例子：開船在海灣裡，燈塔就是地標；要估燈塔位置和自己的位姿。
- **Victoria Park 資料集**（雪梨 ACFR 錄的）：車上的雷射掃描儀抓樹幹當地標。傳統上用在 EKF SLAM，也可以用圖式 SLAM [▶ 03:21](https://youtu.be/mZBdPgBtrCM?t=201)。

| | 種類 | 內容 |
|---|---|---|
| **節點** | 機器人位姿 | 位置＋朝向（2D 3 維、3D 6 維） |
| | 地標位置 | **只有位置**，沒有朝向（2D：$x, y$；3D：$x, y, z$） |
| **邊** | 位姿–位姿 | 里程計（或連續掃描匹配），和 2-11 一樣 |
| | 位姿–地標 | **地標觀測**：機器人從這個位姿看到這個地標 |

- 地標沒有朝向 → 位姿–地標的邊不是完整的轉換，和位姿–位姿的邊不同。
- 最佳化的想法不變：找節點（位姿＋地標）的新組態，讓所有約束的平方誤差和最小。差別只在圖的結構。

---

## 3. 位姿–地標的邊

[▶ 07:40](https://youtu.be/mZBdPgBtrCM?t=460)

記號：位姿 $x_i = (t_i, \theta_i)$，$t_i$ 是平移、$R_i$ 是朝向的旋轉矩陣；地標 $x_j$（2D 點）。

### 3.1 xy 感測器

感測器直接量出地標在機器人座標系中的相對位置 $(\Delta x, \Delta y)$（也可能是距離＋方位換算來的）。

**預測觀測** [▶ 08:43](https://youtu.be/mZBdPgBtrCM?t=523)：地標位置減掉機器人平移，再乘上機器人旋轉矩陣的轉置：

$$
\hat z_{ij} = R_i^{\mathsf T}\,(x_j - t_i) \quad \in \mathbb{R}^2
$$

**誤差**：預測 − 實際觀測

$$
e_{ij}(x_i, x_j) = R_i^{\mathsf T}(x_j - t_i) - z_{ij}
$$

- 注意維度不同：位姿 3 維（3D 是 6 維）、地標 2 維（3D 是 3 維）。
- 邊的形式取決於感測器。

### 3.2 只有方位的感測器

[▶ 10:07](https://youtu.be/mZBdPgBtrCM?t=607)

- **方位**（bearing）感測器：只告訴你地標在哪個**方向**，資訊比 xy 感測器少。像 2D 的相機：影像只有一列，看到地標的像素亮起來。
- 地標正前方 → 觀測 0；偏左 10° → 觀測 10°。
- 地標還是 2D 點，但觀測只有 1 維（講者口誤說成「2D 觀測」，從上下文和後面「一維函數」看應為 1 維）。

**預測觀測** [▶ 11:42](https://youtu.be/mZBdPgBtrCM?t=702)：

$$
\hat z_{ij} = \operatorname{atan2}\bigl( (x_j - t_i)_y,\ (x_j - t_i)_x \bigr) - \theta_i
$$

- $\operatorname{atan2}$ 給出全域座標中機器人到地標的角度（實作要用 atan2 才能處理所有象限）；減掉 $\theta_i$ 轉成機器人自己看到的角度。

**誤差**：$e_{ij} = \hat z_{ij} - z_{ij}$（1 維）。

| 邊 | 誤差維度 |
|---|---|
| 位姿–位姿（2D） | 3 |
| 位姿–地標，xy 感測器 | 2 |
| 位姿–地標，方位感測器 | 1 |

（實作時角度差要正規化到 $(-\pi, \pi]$；講者沒有提，以下不是逐字稿內容，是依角度週期性推論的提醒。）

---

## 4. H 的秩

[▶ 13:28](https://youtu.be/mZBdPgBtrCM?t=808)

- $H_{ij} = J_{ij}^{\mathsf T}\Omega_{ij}J_{ij}$。
- 線性代數：$\operatorname{rank}(A^{\mathsf T}A) = \operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$。$\Omega$ 滿秩時，$H_{ij}$ 的秩由 Jacobian 決定。

| 邊 | Jacobian 非零部分 | $\operatorname{rank}(H_{ij})$ |
|---|---|---|
| xy 感測器 | $2 \times 5$（機器人 $x, y, \theta$ ＋ 地標 $x, y$） | $\le 2$ |
| 方位感測器 | $1 \times 5$ | $\le 1$ |

→ 一個觀測最多只能固定 2（或 1）個自由度。

**例子：已知地標，定位機器人** [▶ 15:31](https://youtu.be/mZBdPgBtrCM?t=931)：

- **xy 觀測一次**：機器人可以在以地標為圓心的**圓**上任何位置；位置一定，朝向就定了（例如地標在正前方，每個可能位置都面向地標）。秩 2 → 固定 3 個參數中的 2 個，剩 1 維的解空間。
- **方位觀測一次**：機器人可以在平面上**任何位置**，位置一定，朝向就定了（都面向地標）。秩 1 → 至少要觀測 **3 個**地標才能固定位姿。

**整體**：

$$
\operatorname{rank}(H) \le \sum_{\langle i,j \rangle} \operatorname{rank}(H_{ij})
$$

- $H$ 是各約束加總 → 需要很多觀測才能讓 $H$ 滿秩。
- 為什麼要滿秩：才有**唯一解**。例：方位感測器只從一個地方看過某地標一次 → 只知道它在一條直線上，線上任何點都是解。

**問答（講者自問自答）** [▶ 20:09](https://youtu.be/mZBdPgBtrCM?t=1209)：要幾個地標觀測才能定出機器人位姿？

- 2D，xy 感測器：至少 **2** 個地標。
- 2D，方位感測器：至少 **3** 個。
- 3D：要固定 6 個自由度，依觀測而定（例如方位感測器一次固定兩個角度）。

**實務**：常常是**欠定**的，不保證滿秩。地標可能只被看過一次；兩次觀測之間也可能沒有里程計（那位姿圖也會有同樣問題；一直有里程計的話位姿圖沒事）。

---

## 5. Levenberg-Marquardt

[▶ 21:20](https://youtu.be/mZBdPgBtrCM?t=1280)

**阻尼**：把 $H\Delta x = -b$ 換成

$$
(H + \lambda I)\,\Delta x = -b
$$

- $I$ 滿秩 → 加上 $\lambda I$ 後很可能滿秩，可以解。
- $\lambda$ 小 → 不太改變原系統（但滿秩不代表條件數好）。
- $\lambda$ 可依解的品質調整。

**這是兩種方法的組合** [▶ 22:35](https://youtu.be/mZBdPgBtrCM?t=1355)：

- $H\Delta x = -b$：Gauss-Newton。
- $\Delta x = -b = -J^{\mathsf T}\Omega e$：殘差（$-e$）乘上資訊矩陣（依重要性加權），再乘 $J^{\mathsf T}$ 映到參數空間 → **最陡下降**。
- $(H + \lambda I)\Delta x = -b$：兩者的組合，$\lambda$ 決定最陡下降的成分多強 → **Levenberg-Marquardt**，能處理欠定系統。

**演算法** [▶ 24:01](https://youtu.be/mZBdPgBtrCM?t=1441)：

```
x = 初始猜測; λ = 初始阻尼
while not converged:
  (H, b) = buildLinearSystem(x)
  E = error(x)                 // 存起來，監控誤差升降
  x_old = x
  Δx = solveSparse((H + λI) Δx = -b)
  x = x + Δx
  if E < error(x):             // 誤差變大了
    x = x_old                  // 退回舊解
    λ = 2λ                     // 阻尼加倍
  else:                        // 誤差變小了
    λ = λ / 2                  // 減小阻尼
```

（講者口述「誤差變大就退回、阻尼加倍；變小就減小阻尼」；減小的倍數講者沒有明說，這裡寫 $/2$ 是對應「加倍」的推測。）

【課本補充】MVG §A6.2（見 2-10 筆記）：典型初值 $\lambda$ 取 $J^{\mathsf T}J$ 對角平均的 $10^{-3}$ 倍，倍數通常用 10。

---

## 6. 和光束法平差的關係

[▶ 25:35](https://youtu.be/mZBdPgBtrCM?t=1535)

- **光束法平差**（bundle adjustment，BA）：用影像做 SLAM，也就是用影像做 3D 重建。
- 一組**無序**影像、抽特徵點、假設特徵點對應已知 → 估相機位置和 3D 點。**不假設**有里程計。
- 最小化**重投影誤差**：把估計的 3D 點投影到 2D 影像平面，和量到的特徵位置比較。
- 沒有里程計 → 更常遇到欠定；要有足夠的重複觀測讓圖連通，否則圖會**斷成好幾塊**。
- 攝影測量從約 1950 年代就有解法。BA 可以看成有地標的圖式 SLAM 的特例；圖式 SLAM 通常再加里程計等資訊，但結構非常相似。

【課本補充】MVG §18.1（書頁 434–435，PDF 頁 452–453）：

- 3D 點 $X_j$、相機矩陣 $P^i$、第 $i$ 台相機看到的第 $j$ 點 $x_j^i$。量測有高斯雜訊時求最大概似解：

$$
\min_{\hat P^i,\, \hat X_j} \sum_{ij} d\bigl( \hat P^i \hat X_j,\ x_j^i \bigr)^2 \qquad (18.1)
$$

- 名稱由來：調整每個相機中心和 3D 點之間的「一束光線」。
- 優點：容忍缺資料、是真正的 ML 估計、可以給每個量測各自的共變異數，也能加先驗和限制。缺點：(i) 要好的初值；(ii) 參數很多：$n$ 點 $m$ 視角要最小化 $3n + 11m$ 個參數，LM 要分解 $(3n + 11m)$ 維方陣，大了就不可行。
- 解法：(i) 減少點或視角（之後再用後方交會、三角化補）或分組各自平差再合併；(ii) 交替最佳化相機和點；(iii) **稀疏方法**（附錄 6）。

【十四講補充】§9.2（書頁 243–251，PDF 頁 266–274）BA 的稀疏結構：

- 變數 $x = [T_1, \dots, T_m, p_1, \dots, p_n]^{\mathsf T}$；誤差項 $e_{ij}$ 只描述「在 $T_i$ 看到 $p_j$」，Jacobian 只有 $\partial e_{ij}/\partial T_i$（$2 \times 6$）和 $\partial e_{ij}/\partial p_j$（$2 \times 3$）兩塊非零（式 9.51）——和 2-11 的位姿圖同一個道理。
- $H = \sum J_{ij}^{\mathsf T}J_{ij}$ 分塊：$H_{11}$（相機）、$H_{22}$（路標）都是**對角塊矩陣**；$H_{12}$、$H_{21}$ 依觀測而定。$H$ 非對角的非零塊 ⇔ 圖中兩個變數之間有邊（像**鄰接矩陣**）。
- 例（圖 9-4）：相機 $C_1$ 看到 $P_1$～$P_4$，$C_2$ 看到 $P_3$～$P_6$。
- 路標遠多於相機 → $H$ 長得像**箭頭**（作者戲稱鎬形）。
- **Schur 消元**（邊緣化）：

$$
\begin{bmatrix} B & E \\ E^{\mathsf T} & C \end{bmatrix}
\begin{bmatrix} \Delta x_c \\ \Delta x_p \end{bmatrix} =
\begin{bmatrix} v \\ w \end{bmatrix}
\;\Longrightarrow\;
\bigl[ B - EC^{-1}E^{\mathsf T} \bigr]\Delta x_c = v - EC^{-1}w, \quad
\Delta x_p = C^{-1}(w - E^{\mathsf T}\Delta x_c)
$$

  $C$ 是 $3 \times 3$ 對角塊 → $C^{-1}$ 很好算。消元後 $S = B - EC^{-1}E^{\mathsf T}$ 的非對角非零塊 = 兩台相機有**共視**路標。機率上是 $P(x_c, x_p) = P(x_c \mid x_p)P(x_p)$（式 9.60）。$S$ 的條件數通常比 $H$ 小。

---

## 7. 總結

[▶ 27:22](https://youtu.be/mZBdPgBtrCM?t=1642)

- 從位姿圖擴充到有地標的一般圖：兩種節點（位姿、地標）、兩種邊（位姿–位姿、位姿–地標）。
- $H$ 的秩取決於 Jacobian 的維度；有地標時更常欠定 → 通常不用 Gauss-Newton，改用 **Levenberg-Marquardt**（Gauss-Newton ＋ 最陡下降）。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Levenberg-Markov”、“Levenbeck”，應為 **Levenberg-Marquardt**。

---

## 8. 一頁速查表

### 8.1 邊與誤差（2D）

| 邊 | 預測 $\hat z_{ij}$ | 誤差維度 | $\operatorname{rank}H_{ij}$ |
|---|---|---|---|
| 位姿–位姿 | $X_i^{-1}X_j$（2-11） | 3 | $\le 3$ |
| xy 感測器 | $R_i^{\mathsf T}(x_j - t_i)$ | 2 | $\le 2$ |
| 方位感測器 | $\operatorname{atan2}\bigl((x_j - t_i)_y, (x_j - t_i)_x\bigr) - \theta_i$ | 1 | $\le 1$ |

誤差 $e_{ij} = \hat z_{ij} - z_{ij}$。

### 8.2 秩

- $\operatorname{rank}(J^{\mathsf T}\Omega J) = \operatorname{rank}(J)$（$\Omega$ 滿秩）。關鍵一步：$J$ 只有 $k$ 列（$k$ = 誤差維度）⇒ 秩 $\le k$。
- $\operatorname{rank}(H) \le \sum \operatorname{rank}(H_{ij})$。
- 定位 2D 位姿（3 自由度）：xy 感測器至少 2 個地標、方位感測器至少 3 個。

### 8.3 Levenberg-Marquardt

| 項 | 內容 |
|---|---|
| 方程 | $(H + \lambda I)\Delta x = -b$ |
| $\lambda \to 0$ | Gauss-Newton |
| $\lambda$ 大 | $\Delta x \approx -b/\lambda$，最陡下降 |
| 誤差變大 | 退回舊解，$\lambda \times 2$ |
| 誤差變小 | 接受，$\lambda$ 減小 |

### 8.4 BA 與 Schur

$\min \sum d(\hat P^i\hat X_j, x_j^i)^2$；$H$ 箭頭形；$[B - EC^{-1}E^{\mathsf T}]\Delta x_c = v - EC^{-1}w$，再回代 $\Delta x_p$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 大圖的計算量 | 2-14 階層式位姿圖 |
| 錯誤的地標關聯 | 2-15 強健最小平方 |
| 相機投影、重投影誤差 | 2-24、2-27 相機模型、DLT |
| 方位觀測、三角化 | 2-29 以後（P3P、對極幾何） |

---

## 附：本集一句話總結

> **有地標的圖式 SLAM：圖裡多了只有位置的地標節點，以及「從位姿看到地標」的邊（xy 感測器 2 維、方位感測器 1 維）。單一觀測的 $H_{ij}$ 秩只有 2 或 1，整體常常欠定，所以改用 Levenberg-Marquardt $(H + \lambda I)\Delta x = -b$。光束法平差是它的特例（沒有里程計的影像版）。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Graph-Based SLAM with Landmarks 錄影逐字稿（Whisper `medium.en`，28:27）、《視覺 SLAM 十四講》§9.2 與 MVG §18.1 整理。*
