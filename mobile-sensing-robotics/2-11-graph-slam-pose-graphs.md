---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-11
lecture: Graph-based SLAM using Pose Graphs
date: 待補（2021 夏季學期）
video: https://youtu.be/uHbRKvD8TWg
notes: 《視覺 SLAM 十四講》第 2 版 §10.2（書頁 270–272，PDF 頁 293–295）
---

# 第 2-11 集 · 用位姿圖做圖式 SLAM [▶ 影片](https://youtu.be/uHbRKvD8TWg)

← 上一集：[2-10-icp-part3](2-10-icp-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-12-graph-slam-landmarks](2-12-graph-slam-landmarks.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-11 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:11:55，Whisper `medium.en` 轉錄）＋《視覺 SLAM 十四講》§10.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者提問、自己回答
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

（BRIEF 原本列「PR 第 14 章？」。查過：MSR1 用的 PR 草稿版 PDF 裡找不到 GraphSLAM／pose graph 的章節，所以本集不引 PR。）

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 位姿圖是什麼](#1-位姿圖是什麼)
- [2. 前端與後端](#2-前端與後端)
- [3. 節點與邊](#3-節點與邊)
  - [3.1 里程計邊與虛擬量測邊](#31-里程計邊與虛擬量測邊)
  - [3.2 齊次座標](#32-齊次座標)
  - [3.3 資訊矩陣](#33-資訊矩陣)
- [4. 誤差函數](#4-誤差函數)
- [5. Jacobian 的稀疏性](#5-jacobian-的稀疏性)
- [6. H 和 b 的稀疏結構](#6-h-和-b-的稀疏結構)
- [7. 演算法](#7-演算法)
- [8. 一維小例子：規範自由度](#8-一維小例子規範自由度)
- [9. 固定變數、不確定性](#9-固定變數不確定性)
- [10. 總結](#10-總結)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

用 2-05 的**最小平方**（Gauss-Newton）解 SLAM：把機器人走過的位姿放成一張**位姿圖**（pose graph），用 2-07～2-10 的 ICP 結果當邊，調整所有位姿讓總誤差最小。重點：**H 矩陣是稀疏的**，所以大問題也解得動。

前備：會 Gauss-Newton，知道 ICP 輸出什麼 [▶ 01:45](https://youtu.be/uHbRKvD8TWg?t=105)。

---

## 1. 位姿圖是什麼

[▶ 00:00](https://youtu.be/uHbRKvD8TWg?t=0)

- 圖式 SLAM：近年最流行的 SLAM 方法，本質上是**最小平方**。位姿圖版本**不用地標**，全部化約到位姿（或說地標被邊緣化掉了）。
- 好維護、對各種觀測很有彈性 → 光達 SLAM、RGB-D 相機等的標準工具；比單一房間大的建圖系統，背後通常都是位姿圖。
- 最小平方：解**超定**系統（方程比未知數多）。未知數 = 機器人位姿；方程 = 來自觀測和控制的**約束**。目標：找讓平方誤差和最小的位姿組態。

**直覺** [▶ 03:25](https://youtu.be/uHbRKvD8TWg?t=205)：

1. 機器人移動，每隔一段時間（例如每秒，或每走 3、5 公尺）建立一個**位姿**變數（三角形）。位姿 = 2D 的 $(x, y, \theta)$，或 3D 的位置加三個角度。
2. 相鄰位姿之間有**約束**，來自運動：例如數輪子轉了幾圈 →「位姿 2 離位姿 1 大約 1 公尺」。不確定（可能 1.02 公尺、95 公分……），所以是**軟約束**。也可以來自掃描匹配（ICP 對齊相鄰掃描）。
3. 機器人回到以前去過的地方 → **閉合迴圈**（loop closing）：用 ICP 對齊現在和以前的掃描，得到**不相鄰**位姿之間的約束（2-07 稱為**虛擬觀測**）。
4. 不再是一條鏈，而是一張**圖** → 位姿圖。

**衝突的約束** [▶ 09:25](https://youtu.be/uHbRKvD8TWg?t=565)：里程計說「下一個位姿離這裡 1 公尺」，閉合迴圈的觀測說「這個位姿應該挪一點」→ 互相衝突 → 找讓總誤差最小的組態。

**例子** [▶ 10:05](https://youtu.be/uHbRKvD8TWg?t=605)：Patrick Pfaff 建的 2D 雷射地圖。只用里程計 → 同一個房間被畫在好幾個地方，完全不能用。建出位姿圖、最佳化後 → 用修正後的位姿畫佔據網格地圖（1-05），一致的地圖。最佳化時**可以先忘掉地圖**，只管位姿；位姿知道了，建圖就簡單。

【十四講補充】§10.2.1（書頁 270）：BA 裡特徵點占了最佳化問題的絕大部分；收斂的點變化很小，外點已被剔除，繼續最佳化它們費力不討好 → 最佳化幾次後把特徵點固定住，只當作位姿的約束；再進一步完全不管路標，只留關鍵幀軌跡 → **位姿圖**。一個關鍵幀常關聯數百個關鍵點，即時 BA 的規模一般只有幾萬個點，所以大場景要嘛像滑動窗口那樣丟掉歷史，要嘛像位姿圖那樣捨棄路標、只留位姿之間的邊。

---

## 2. 前端與後端

[▶ 12:39](https://youtu.be/uHbRKvD8TWg?t=759)

| | 前端（front-end） | 後端（back-end） |
|---|---|---|
| 做什麼 | 原始感測資料 → 約束 | 約束 → 最佳化圖 → 修正後的位姿 |
| 例子 | ICP：輸出 $R$、$t$（加上不確定性） | 本集的最小平方 |

- 實際上兩者互動：前端建立關聯 → 後端最佳化 → 用最佳化後的地圖做新的資料關聯。
- 本集**只講後端**；前端想成 ICP 即可（要做好還需要比 vanilla ICP 多一點東西）。

---

## 3. 節點與邊

[▶ 14:24](https://youtu.be/uHbRKvD8TWg?t=864)

- **節點** $x_1, \dots, x_n$：時間 $t_i$ 的機器人位姿（2D 是 3 維、3D 是 6 維向量）。整個圖的狀態 $x = (x_1^{\mathsf T}, \dots, x_n^{\mathsf T})^{\mathsf T}$。
- **邊**：連兩個節點，說「這兩個位姿應該有這樣的相對關係」。

### 3.1 里程計邊與虛擬量測邊

[▶ 15:27](https://youtu.be/uHbRKvD8TWg?t=927)

| 邊 | 何時 | 來源 |
|---|---|---|
| **連續邊** $x_i \to x_{i+1}$ | 機器人從 $x_i$ 走到 $x_{i+1}$ | 里程計（運動模型：差速、Ackermann……，1-06、1-07），或增量 ICP。機率上是移動量的平均估計 |
| **任意邊** $x_i \to x_j$（$j \neq i+1$） | 兩處看到同一塊環境 | 感測器：對齊兩處的掃描 → **虛擬量測** |

**虛擬量測** [▶ 17:11](https://youtu.be/uHbRKvD8TWg?t=1031)：

- $x_i$ 實際上看不到未來的 $x_j$；但兩處都看到同一塊環境，把兩次掃描疊起來（ICP），就知道「從 $x_i$ 看，$x_j$ 在哪」。
- 這是**完整的轉換**（平移＋旋轉），不只是距離。
- 視覺的版本：相對定向，例如五點、八點演算法（2-33～2-37）。本集只用 ICP。

### 3.2 齊次座標

[▶ 19:29](https://youtu.be/uHbRKvD8TWg?t=1169)

- 大寫字母 = 齊次轉換矩陣。$X_i$：位姿 $x_i$ 在全域座標系中的轉換。
- **相對轉換**：

$$
X_i^{-1}X_{i+1} \;=\; \text{從 } x_i \text{ 看 } x_{i+1}, \qquad
X_i^{-1}X_j \;=\; \text{從 } x_i \text{ 看 } x_j
$$

複習 [▶ 20:49](https://youtu.be/uHbRKvD8TWg?t=1249)：

- $n$ 維空間用 $n+1$ 維表示：$(x, y, z) \mapsto (x, y, z, 1)$；反過來 $(x, y, z, w) \mapsto (x/w, y/w, z/w)$。
- 好處：一個矩陣就能表示所有仿射（甚至射影）轉換；剛體轉換是其子集。平移、旋轉都是矩陣，串接 = 相乘。

$$
\text{平移} = \begin{bmatrix} I_3 & t \\ 0^{\mathsf T} & 1 \end{bmatrix}, \qquad
\text{旋轉} = \begin{bmatrix} R & 0 \\ 0^{\mathsf T} & 1 \end{bmatrix}
$$

- 在歐氏座標裡寫串接麻煩得多。詳見講者的齊次座標課。

### 3.3 資訊矩陣

[▶ 24:27](https://youtu.be/uHbRKvD8TWg?t=1467)

- 約束有雜訊（里程計通常比雷射差，但雷射也有雜訊）。
- $\Omega_{ij}$：邊 $(i, j)$ 的**資訊矩陣**（共變異數的反矩陣），代表多相信這個觀測。值越大 → 不確定性越小 → 這條邊在最佳化中越重要。
- 在最小平方中就是誤差的**權重**：資訊大一倍的邊，影響也大一倍。

【課堂討論】[▶ 25:59](https://youtu.be/uHbRKvD8TWg?t=1559) 講者問兩個問題，自己回答：

1. **ICP 和里程計哪個 $\Omega$ 大？** 一般室內建圖：雷射掃描比里程計可靠 → ICP 邊的共變異數較小、資訊矩陣較大。但如果掃描儀不準、環境很動態，或在里程計上下了很多工夫（冗餘系統、好的動力學模型，例如自駕車），也可能反過來。
2. **又長又沒特徵的走廊，ICP 的 $\Omega$ 長什麼樣？** 左右（看得到牆）和朝向很準；**沿走廊方向**很難估 → 共變異數橫向很窄、沿走廊方向拉得很長。看共變異數就知道感測器實際提供了什麼資訊；某方向不確定性大，最小平方的結果在那方向的不確定性也大。

---

## 4. 誤差函數

[▶ 28:53](https://youtu.be/uHbRKvD8TWg?t=1733)

一條邊：

- 目前的圖組態：$x_i$、$x_j$ 在某處。
- 觀測 $z_{ij}$（例如 ICP）加上不確定性：從 $x_i$ 看，$x_j$ 應該在哪。
- 兩者不一致 → **誤差**，要把所有邊的誤差都壓向零（只有一條邊很容易，難在全部一起）。
- 每條邊存：平均觀測 $z_{ij}$ ＋ 資訊矩陣 $\Omega_{ij}$。

總誤差（2-05 的形式）[▶ 31:11](https://youtu.be/uHbRKvD8TWg?t=1871)：

$$
F(x) = \sum_{\langle i,j \rangle} e_{ij}^{\mathsf T}\,\Omega_{ij}\,e_{ij}, \qquad e_{ij} = e_{ij}(x_i, x_j)
$$

**關鍵**：每個 $e_{ij}$ 只依賴 $x_i$ 和 $x_j$，和其他狀態無關 → 之後要利用這點。

**狀態向量** [▶ 32:20](https://youtu.be/uHbRKvD8TWg?t=1940)：所有位姿接起來，很長的向量：$(x_1, y_1, \theta_1, x_2, y_2, \theta_2, \dots)$；3D 則是位置加三個角度（或其他 6 自由度表示）。

**單一約束的誤差** [▶ 33:39](https://youtu.be/uHbRKvD8TWg?t=2019)：

$$
\boxed{\;e_{ij}(x_i, x_j) = \mathrm{t2v}\!\left( Z_{ij}^{-1}\,\bigl( X_i^{-1}X_j \bigr) \right)\;}
$$

- $X_i^{-1}X_j$：依**圖**，從 $x_i$ 看 $x_j$（正向走一次）。
- $Z_{ij}^{-1}$：依**觀測**走回來（反向）。
- 走完一圈和起點的差就是誤差。
- **t2v**（transformation to vector）：齊次矩陣 → 向量，2D 是 $3 \times 3$ 矩陣 → $(x, y, \theta)$；**v2t** 反過來。最小平方要用向量。

**誤差何時為零** [▶ 36:36](https://youtu.be/uHbRKvD8TWg?t=2196)：觀測和圖的相對組態一樣 → $Z_{ij}^{-1}X_i^{-1}X_j = I$ → $\mathrm{t2v}(I) = (0, 0, 0)$。

【十四講補充】§10.2.2（書頁 270–272）用李群李代數寫同一件事：

- 相對運動 $\Delta\xi_{ij} = \xi_i^{-1} \circ \xi_j = \ln\bigl( T_i^{-1}T_j \bigr)^\vee$，或 $T_{ij} = T_i^{-1}T_j$（式 10.2、10.3）。
- 誤差 $e_{ij} = \ln\bigl( T_{ij}^{-1}T_i^{-1}T_j \bigr)^\vee$（式 10.4）——就是講者的 $\mathrm{t2v}(Z_{ij}^{-1}X_i^{-1}X_j)$，$\ln(\cdot)^\vee$ 扮演 t2v 的角色。
- 對 $\xi_i$、$\xi_j$ 各加左擾動，用伴隨性質 $\exp\bigl( (\mathrm{Ad}(T)\xi)^\wedge \bigr) = T\exp(\xi^\wedge)T^{-1}$ 把擾動移到右邊，得到 Jacobian：

$$
\frac{\partial e_{ij}}{\partial \delta\xi_i} = -\mathcal{J}_r^{-1}(e_{ij})\,\mathrm{Ad}(T_j^{-1}), \qquad
\frac{\partial e_{ij}}{\partial \delta\xi_j} = \mathcal{J}_r^{-1}(e_{ij})\,\mathrm{Ad}(T_j^{-1})
$$

- $\mathcal{J}_r$ 太複雜，常近似：誤差接近零時取 $I$，或 $\mathcal{J}_r^{-1}(e_{ij}) \approx I + \tfrac12 \begin{bmatrix} \phi_e^\wedge & \rho_e^\wedge \\ 0 & \phi_e^\wedge \end{bmatrix}$（式 10.11）。但每條邊的觀測互不一致，最佳化後誤差也不一定接近零，直接設 $I$ 會有一些損失。
- 總目標 $\min \tfrac12 \sum_{i,j \in \mathcal{E}} e_{ij}^{\mathsf T}\Sigma_{ij}^{-1}e_{ij}$（式 10.12），用 Gauss-Newton 或 LM 解，可用 Ceres 或 g2o。

---

## 5. Jacobian 的稀疏性

[▶ 37:44](https://youtu.be/uHbRKvD8TWg?t=2264)

Gauss-Newton 步驟（2-05）：定義誤差 → 線性化 → 二次式、一階導數設零 → 解線性方程 → 更新 → 重複。

- 齊次矩陣裡有 $\sin$、$\cos$ → 非線性 → 要算 Jacobian：坐下來用紙筆算，或用能自動／數值微分的框架。
- **$e_{ij}$ 依賴所有狀態嗎？** 不，只依賴 $x_i$、$x_j$ [▶ 39:43](https://youtu.be/uHbRKvD8TWg?t=2383)。
- 函數不依賴某變數 → 對它的偏導是零 → Jacobian **幾乎全是零**：

$$
J_{ij} = \frac{\partial e_{ij}(x)}{\partial x} = \Bigl[\; 0 \;\cdots\; 0 \;\; \underbrace{A_{ij}}_{\partial e_{ij}/\partial x_i} \;\; 0 \;\cdots\; 0 \;\; \underbrace{B_{ij}}_{\partial e_{ij}/\partial x_j} \;\; 0 \;\cdots\; 0 \;\Bigr]
$$

- 例：狀態 10,000 維，一條邊只連兩個位姿 → 只有 6 個（2D）維度非零，其他 10,000 − 6 維都是零。
- 【口頭】講者說這是整份投影片**最重要的一張**：有了它才能有效解真實世界的 SLAM [▶ 43:06](https://youtu.be/uHbRKvD8TWg?t=2586)。

---

## 6. H 和 b 的稀疏結構

[▶ 43:23](https://youtu.be/uHbRKvD8TWg?t=2603)

$$
b_{ij}^{\mathsf T} = e_{ij}^{\mathsf T}\Omega_{ij}J_{ij}, \qquad
H_{ij} = J_{ij}^{\mathsf T}\Omega_{ij}J_{ij}
$$

**一條邊**：

- $b_{ij}$：只有第 $i$、$j$ 塊非零。
- $H_{ij}$：只有四塊非零：$ii$、$jj$、$ij$、$ji$（$ij$ 和 $ji$ 互為轉置）。

$$
b_{ij} = \begin{bmatrix} \vdots \\ A_{ij}^{\mathsf T}\Omega_{ij}e_{ij} \\ \vdots \\ B_{ij}^{\mathsf T}\Omega_{ij}e_{ij} \\ \vdots \end{bmatrix}, \qquad
H_{ij} = \begin{bmatrix} \ddots & & & \\ & A_{ij}^{\mathsf T}\Omega_{ij}A_{ij} & \cdots & A_{ij}^{\mathsf T}\Omega_{ij}B_{ij} \\ & \vdots & \ddots & \vdots \\ & B_{ij}^{\mathsf T}\Omega_{ij}A_{ij} & \cdots & B_{ij}^{\mathsf T}\Omega_{ij}B_{ij} \\ & & & \ddots \end{bmatrix}
$$

（分塊寫法依 2-05 的 $H = J^{\mathsf T}\Omega J$、$b = J^{\mathsf T}\Omega e$ 代入 $J_{ij}$ 的稀疏形式展開。）

**全部加總** [▶ 46:02](https://youtu.be/uHbRKvD8TWg?t=2762)：

- $b = \sum b_{ij}$：每個節點都有約束 → **稠密**。
- $H = \sum H_{ij}$：$n^2$ 塊中每條邊只填四塊 → **稀疏**：
  - 對角塊；
  - 緊鄰對角線的塊（相鄰位姿，里程計邊）；
  - 少數遠離對角線的塊（**閉合迴圈**）。
- $H$ 可以看成圖的**鄰接矩陣**。
- 環境越大通常越稀疏：一棟有上百個房間的建築，在房間裡只看得到這個房間，只有從走廊看得到少數幾個房間。

**實作** [▶ 48:50](https://youtu.be/uHbRKvD8TWg?t=2930)：

- 用稀疏矩陣表示 $H$（數學工具箱有現成的，否則自己確保填對塊）。
- **稀疏 Cholesky 分解**比一般 Cholesky 快得多；其他演算法也多有稀疏版本。這是能在合理時間內解出來的原因。
- 自己建系統時 [▶ 50:20](https://youtu.be/uHbRKvD8TWg?t=3020)：對每條邊只算 $e_{ij}$、$A_{ij}$、$B_{ij}$（其他確定是零，不用碰），再把小塊**加到正確位置**：

$$
\begin{aligned}
\bar b_i &\mathrel{+}= A_{ij}^{\mathsf T}\Omega_{ij}e_{ij}, &\quad \bar b_j &\mathrel{+}= B_{ij}^{\mathsf T}\Omega_{ij}e_{ij}, \\
\bar H_{ii} &\mathrel{+}= A_{ij}^{\mathsf T}\Omega_{ij}A_{ij}, &\quad \bar H_{ij} &\mathrel{+}= A_{ij}^{\mathsf T}\Omega_{ij}B_{ij}, \\
\bar H_{ji} &\mathrel{+}= B_{ij}^{\mathsf T}\Omega_{ij}A_{ij}, &\quad \bar H_{jj} &\mathrel{+}= B_{ij}^{\mathsf T}\Omega_{ij}B_{ij}
\end{aligned}
$$

---

## 7. 演算法

[▶ 51:31](https://youtu.be/uHbRKvD8TWg?t=3091)

```
optimize(x):
  while not converged:          // 例如更新量夠小
    (H, b) = buildLinearSystem(x)   // 上面的分塊加總
    Δx = solveSparse(H Δx = -b)     // 稀疏 Cholesky
    x = x + Δx
  return x
```

- 結果：讓所有約束平方誤差和最小的圖組態。
- 之後直接拿這些位姿去**建圖**（這一步已經不是 SLAM，只是已知位姿的建圖）。

---

## 8. 一維小例子：規範自由度

[▶ 53:10](https://youtu.be/uHbRKvD8TWg?t=3190)

一維世界、兩個節點、一個觀測：「$x_2$ 在 $x_1$ 前方 1 公尺」。

| 量 | 值 |
|---|---|
| 初始猜測 | $x = (x_1, x_2) = (0, 0)$ |
| 觀測 | $z_{12} = 1$ |
| 資訊 | $\Omega = 2$（由講者的 $b = (2, -2)$ 反推） |
| 誤差（觀測 − 預測） | $e_{12} = z_{12} - (x_2 - x_1) = 1 - 0 = 1$ |
| Jacobian | $J_{12} = \left[ \dfrac{\partial e}{\partial x_1},\ \dfrac{\partial e}{\partial x_2} \right] = [\,1,\ -1\,]$ |

$$
b = J^{\mathsf T}\Omega e = \begin{bmatrix} 2 \\ -2 \end{bmatrix}, \qquad
H = J^{\mathsf T}\Omega J = \begin{bmatrix} 2 & -2 \\ -2 & 2 \end{bmatrix}
$$

**問題** [▶ 56:13](https://youtu.be/uHbRKvD8TWg?t=3373)：$\det H = 2 \cdot 2 - (-2)(-2) = 0$ → **秩不足**，無法求反。

**原因**：約束是**相對**的，只說兩點相距多遠，沒說它們在全域座標系的哪裡 → 缺少參考座標系，也就是**規範自由度**（gauge freedom）。

- `⚠️ 逐字稿缺字`：Whisper 寫 “god freedom”，應為 **gauge freedom**。

**解法**：固定一個節點，例如加一個**先驗**：「第一個節點的更新量為 0」。像一個以第一個節點為參考座標系的高斯約束，加在 $H$ 上就是 $H_{11} \mathrel{+}= 1$：

$$
H = \begin{bmatrix} 3 & -2 \\ -2 & 2 \end{bmatrix}, \quad \det H = 6 - 4 = 2 \neq 0
$$

$$
\Delta x = -H^{-1}b = -\frac12 \begin{bmatrix} 2 & 2 \\ 2 & 3 \end{bmatrix}\begin{bmatrix} 2 \\ -2 \end{bmatrix} = -\frac12 \begin{bmatrix} 0 \\ -2 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

（$H^{-1}$ 和中間步驟是照講者給的 $H$、$b$ 補算的；講者只說結果「節點 1 不動、節點 2 移動 1」。）

→ 新組態 $(0, 1)$，正好符合觀測。

**一般情況** [▶ 59:04](https://youtu.be/uHbRKvD8TWg?t=3544)：

- 約束再多也一樣秩不足，因為全域參考座標系沒固定。
- 除非有 GPS 之類固定全域座標的感測器；否則要選一個節點（例如 $x_0$）當參考，加先驗「$x_0$ 是 $(0, 0, 0)$」，其他都相對它。

**實際系統** [▶ 1:00:14](https://youtu.be/uHbRKvD8TWg?t=3614)：機器人邊走邊建圖（黑色障礙、白色空地）。回到之前去過的地方時，起點建的地圖和現在建的有一點偏移 → 地圖會**抖一下**：最小平方根據新觀測挪動節點。閉合迴圈越多，抖動越小（修正已經做過了）。整個系統：ICP 對齊相鄰掃描建圖，靠近以前去過的地方時跑 ICP 找好的匹配，找到就加閉合迴圈約束 → 一個簡單的雷射 SLAM 系統。

---

## 9. 固定變數、不確定性

### 9.1 固定變數

[▶ 1:02:24](https://youtu.be/uHbRKvD8TWg?t=3744)

- 先驗只是**軟約束**，其他約束可能把節點拉走。
- 想讓某變數**完全固定**：建好整個系統後，**刪掉 $H$ 中對應的列和行**（以及 $\Delta x$、$b$ 中對應的元素），再解。
- 為什麼可以：**資訊形式**下的高斯**條件化**就是直接切出資訊矩陣的一部分（資訊濾波器學過）；$H$ 就是整個問題的資訊矩陣 → 刪掉列和行 = 以「這些變數固定」為條件。

### 9.2 不確定性

[▶ 1:05:27](https://youtu.be/uHbRKvD8TWg?t=3927)

- 在收斂、線性化的近似下，$H$ 是整體估計的**資訊矩陣** → $H^{-1}$ 是**共變異數**。
- 問題：$H^{-1}$ 通常是**稠密**的，求反代價高。通常只需要主對角塊，有比較有效率的特殊算法。

**相對不確定性** [▶ 1:06:51](https://youtu.be/uHbRKvD8TWg?t=4011)：

- 找閉合迴圈時，常要的是「目前位姿相對某個舊位姿」的不確定性，不是全域的。
- 算 $x_j$ 相對 $x_i$ 的不確定性：**固定 $x_i$**（刪掉 $H$ 中 $x_i$ 的列和行），求反，取 **$jj$ 塊** = 以 $x_i$ 為參考時 $x_j$ 的共變異數。也有只算這一塊的有效方法。
- 例：機器人算所有節點相對自己的不確定性，決定要檢查哪些節點做閉合迴圈。地圖品質已經很好時，只有少數節點需要檢查。

---

## 10. 總結

[▶ 1:09:08](https://youtu.be/uHbRKvD8TWg?t=4148)

- 本集：SLAM 的**後端**，用最小平方解位姿圖 SLAM。位姿圖只含位姿，不含地標（一般的 SLAM 圖應該要有，見 2-12）。
- 關鍵：**$H$ 稀疏** → 數千、數萬、甚至數百萬變數也能有效解；否則線上系統做不到。
- 今天很多 SLAM（和部分定位）系統都用位姿圖：線上建圖、最佳化（有些只最佳化最近一段、有些近似、有些用**階層式**架構省計算（2-14）、有些用聰明的離群值剔除處理未知資料關聯（2-15））。核心和本集很像。
- 函式庫：**g2o**、**GTSAM**、**Ceres** 最流行。但課程實習要從頭自己做 2D 位姿圖 SLAM，親手推所有 Jacobian。
- `⚠️ 逐字稿缺字`：Whisper 寫 “gtsem or seras”，應為 **GTSAM**、**Ceres**。

---

## 11. 一頁速查表

### 11.1 位姿圖

| 元素 | 意義 |
|---|---|
| 節點 $x_i$ | 時間 $t_i$ 的位姿（2D：$(x, y, \theta)$） |
| 邊 $(z_{ij}, \Omega_{ij})$ | 從 $x_i$ 看 $x_j$ 的相對轉換觀測＋資訊矩陣 |
| 連續邊 | 里程計、增量 ICP |
| 閉合迴圈邊 | ICP 對齊非相鄰位姿的掃描（虛擬量測） |

### 11.2 誤差與目標

$$
e_{ij} = \mathrm{t2v}\!\left( Z_{ij}^{-1}X_i^{-1}X_j \right), \qquad
x^* = \arg\min_x \sum_{\langle i,j \rangle} e_{ij}^{\mathsf T}\Omega_{ij}e_{ij}
$$

關鍵一步：圖說的相對轉換 $X_i^{-1}X_j$ 和觀測 $Z_{ij}$ 一致 ⇔ $Z_{ij}^{-1}X_i^{-1}X_j = I$ ⇔ $e_{ij} = 0$。

### 11.3 稀疏結構

| 量 | 一條邊的非零塊 | 全部加總 |
|---|---|---|
| $J_{ij}$ | $A_{ij}$（第 $i$ 塊）、$B_{ij}$（第 $j$ 塊） | — |
| $b$ | $i$、$j$ | 稠密 |
| $H$ | $ii$、$ij$、$ji$、$jj$ | 稀疏（像鄰接矩陣） |

關鍵一步：$e_{ij}$ 只依賴 $x_i, x_j$ ⇒ 對其他變數偏導為零 ⇒ $J_{ij}$ 只有兩塊 ⇒ $J^{\mathsf T}\Omega J$ 只有四塊。

### 11.4 求解

| 步驟 | 做法 |
|---|---|
| 解 | $H\Delta x = -b$，稀疏 Cholesky |
| 規範自由度 | 固定一個節點（先驗 $H_{11} \mathrel{+}= I$，或刪列行） |
| 完全固定變數 | 刪掉 $H$ 的對應列和行（＝資訊形式的條件化） |
| 共變異數 | $H^{-1}$（稠密、貴；常只取對角塊） |
| 相對不確定性 | 固定 $x_i$ → 求反 → 取 $jj$ 塊 |

### 11.5 一維例子

$e = 1$，$J = [1, -1]$，$\Omega = 2$ → $H = \begin{bmatrix} 2 & -2 \\ -2 & 2 \end{bmatrix}$ 奇異；加先驗後 $\begin{bmatrix} 3 & -2 \\ -2 & 2 \end{bmatrix}$，$\Delta x = (0, 1)$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 位姿圖只有位姿 | 2-12 加入地標 |
| $H$ 稀疏、分塊加總 | 2-12（地標的稀疏結構，Schur 補） |
| 大圖計算量 | 2-14 階層式位姿圖 |
| 錯的閉合迴圈、離群值 | 2-15 強健最小平方 |
| 虛擬量測的視覺版本 | 2-33～2-37 相對定向（五點、八點演算法） |

---

## 附：本集一句話總結

> **位姿圖 SLAM：節點是位姿、邊是相對轉換觀測（里程計、ICP），誤差 $e_{ij} = \mathrm{t2v}(Z_{ij}^{-1}X_i^{-1}X_j)$，用 Gauss-Newton 最小化。每條邊只碰兩個節點 → Jacobian 只有兩塊、$H$ 只多四塊 → $H$ 稀疏，用稀疏 Cholesky 很快。記得固定一個節點，否則 $H$ 秩不足（規範自由度）。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Graph-based SLAM using Pose Graphs 錄影逐字稿（Whisper `medium.en`，1:11:55）與《視覺 SLAM 十四講》§10.2 整理。*
