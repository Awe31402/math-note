---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 28
lecture: Lecture 10 (Part 2) – Structure-from-Motion (SfM) and bundle adjustment
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/j3VSmUCKZDM
notes: 本集內容講者取自 CVPR 2017「Large-scale 3D Modeling」教學（BRIEF 沒列，未查）；MVG §18 只有多視角的分解法，沒有增量式／全域式 SfM
---

# 第 28 集 · Lecture 10 (Part 2)：增量式、全域式、階層式 SfM [▶ 影片](https://youtu.be/j3VSmUCKZDM)

← 上一集：[27-sfm-bundle-adjustment-part1](27-sfm-bundle-adjustment-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[29-sfm-bundle-adjustment-part3](29-sfm-bundle-adjustment-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 28 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（23:16，Whisper `medium.en` 轉錄）；MVG 沒有對應內容，依 BRIEF 只靠逐字稿
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 增量式 SfM](#1-增量式-sfm)
  - [1.1 選種子影像對](#11-選種子影像對)
  - [1.2 初始化前兩台相機](#12-初始化前兩台相機)
  - [1.3 一張一張加入](#13-一張一張加入)
- [2. 全域式 SfM](#2-全域式-sfm)
  - [2.1 問題：從相對位姿求絕對位姿](#21-問題從相對位姿求絕對位姿)
  - [2.2 旋轉平均：指數映射與對數映射](#22-旋轉平均指數映射與對數映射)
  - [2.3 線性化成最小平方](#23-線性化成最小平方)
  - [2.4 平移](#24-平移)
- [3. 階層式 SfM](#3-階層式-sfm)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/j3VSmUCKZDM?t=0)

場景圖建好之後，下一步是 SfM，得到稀疏 3D 重建。三種典型做法：

| 做法 | 本集 |
|---|---|
| **增量式（incremental）SfM** | 細講 |
| **全域式（global）SfM** | 簡介 |
| **階層式（hierarchical）SfM** | 簡介 |

---

## 1. 增量式 SfM

### 1.1 選種子影像對

[▶ 00:32](https://youtu.be/j3VSmUCKZDM?t=32)

從場景圖選兩張當起點，叫**種子影像對（seed pair）**：

1. **平移不能是 0**：排除純旋轉的影像對（純旋轉沒有視差，無法三角化；第 13 集）。從建場景圖時算的雙視角幾何就看得出來。
2. 符合條件的很多對中，選**內點數最多**的。
   - 理由：$F$、$E$ 的估計是最小平方，觀測（對應點）越多越準。

### 1.2 初始化前兩台相機

[▶ 01:51](https://youtu.be/j3VSmUCKZDM?t=111)

1. 估雙視角幾何：
   - 非平面場景：8 點法求 $F$ 或 $E$。
   - 平面場景：4 點法求 homography。
2. 分解成兩台相機的投影矩陣（第 18 集）。
3. **尺度設為 1**：$E$ 分解出的平移長度設成 1；$F$ 分解出的 $P'$ 也定一個尺度。（第 19 集：重建本來就有尺度模糊。）
4. 用 RANSAC 的內點對應**線性三角化**（第 19 集），得 3D 點 $\mathbf{X}_j$。
   - 記號：$\mathbf{x}_{ij}$ 是第 $j$ 個點在第 $i$ 張圖的像。
5. **bundle adjustment**：最佳化兩台相機和 3D 點，最小化重投影誤差（細節下兩集）。

### 1.3 一張一張加入

[▶ 04:09](https://youtu.be/j3VSmUCKZDM?t=249)

「增量式」：從種子對開始，**一次加一張**。

**加入第三張 $P_3$**：

1. 從場景圖選一張和已重建影像（例如 $P_2$）相連的影像當 $P_3$。
2. **2D–2D 對應**：$P_3$ 和 $P_2$ 之間的特徵配對（例如 SIFT）。
3. **2D–3D 對應** [▶ 05:51](https://youtu.be/j3VSmUCKZDM?t=351)：$P_2$ 上那個特徵點當初被用來三角化出某個 3D 點 → 所以 $P_3$ 上對應的特徵點就對應那個 3D 點。
4. **PnP** [▶ 06:40](https://youtu.be/j3VSmUCKZDM?t=400)：用 2D–3D 對應求 $P_3$（第 20–22 集）。因為 3D 點在世界座標系，$P_3$ 也在同一個世界座標系。
5. **三角化新點**：$P_2$、$P_3$ 之間還有其他（還沒有 3D 點的）對應，用已知的 $P_2,P_3$ 三角化，把新點加進場景。
6. 對 $P_4$、$P_5$……重複：2D–2D → 2D–3D → PnP → 三角化，直到場景圖裡所有影像都處理完。

**最後** [▶ 08:06](https://youtu.be/j3VSmUCKZDM?t=486)：對所有相機和所有 3D 點做**多視角 bundle adjustment**——每台相機把它看到的 3D 點重投影，最小化和觀測點的誤差。

⚠️ 逐字稿缺字：Whisper 把 bundle adjustment 寫成 “banded adjustment”。

> 以下**不是逐字稿內容**，是實務補充：增量式 SfM（例如 COLMAP）通常每加幾張就做一次局部或全域 BA，避免誤差累積；也常在加入新影像時用 RANSAC 搭配 P3P 剔除錯誤的 2D–3D 對應。

---

## 2. 全域式 SfM

### 2.1 問題：從相對位姿求絕對位姿

[▶ 09:04](https://youtu.be/j3VSmUCKZDM?t=544)

1. 對場景圖的**每一條邊**算相對位姿 $R_{ij},\mathbf{t}_{ij}$。
   - 可以用 $F$、$E$ 或 homography。實務上場景多半不是平面，不用 homography。
   - 相機已校正時用 $E$ 比較準：沒有射影模糊。
2. 現在有一張圖：節點是相機的**絕對位姿** $R_i,\mathbf{t}_i$（相對世界座標系 $F_W$，未知），邊是**相對位姿** $R_{ij},\mathbf{t}_{ij}$（已知）。
3. **問題**：給所有相對量測，求所有絕對位姿。

### 2.2 旋轉平均：指數映射與對數映射

[▶ 12:08](https://youtu.be/j3VSmUCKZDM?t=728)

**先求全域旋轉**：

$$
\min_{\{R_i\}}\ \sum_{(i,j)}d\left(R_{ij},\ R_iR_j^\mathsf{T}\right)
$$

- $R_iR_j^\mathsf{T}$：從待求的兩個絕對旋轉算出的相對旋轉。
- 希望它和**觀測到**的 $R_{ij}$ 越接近越好。

（目標函數的寫法依講者口述「$R_i$ 乘 $R_j$ 轉置，和觀測的 $R_{ij}$ 比較」；$d(\cdot,\cdot)$ 是兩個旋轉的差距，逐字稿沒說用哪種距離。）

**$SO(3)$ 和 3 維向量之間的轉換** [▶ 13:27](https://youtu.be/j3VSmUCKZDM?t=807)：

- 旋轉矩陣有 9 個元素但只有 3 個自由度。換成 3 維向量 $\boldsymbol{\omega}\in\mathbb{R}^3$ 比較好最佳化。
- **指數映射（exponential map）**：
$$
R=\exp\left([\boldsymbol{\omega}]_\times\right)
$$
  $[\boldsymbol{\omega}]_\times$ 是 $\boldsymbol{\omega}$ 的反對稱矩陣（第 03 集的 $\hat{\boldsymbol{\omega}}$）。
- **對數映射（logarithmic map）**（逆運算）：
$$
[\boldsymbol{\omega}]_\times=\log R
$$
- 講者說：給一個旋轉矩陣，$\boldsymbol{\omega}$ 由「這個式子」算出。

> 以下**不是逐字稿內容**：逐字稿沒唸出公式。標準的 Rodrigues 形式是
> $$R=I+\frac{\sin\theta}{\theta}[\boldsymbol{\omega}]_\times+\frac{1-\cos\theta}{\theta^2}[\boldsymbol{\omega}]_\times^2,\qquad\theta=\|\boldsymbol{\omega}\|$$
> 反過來：
> $$\theta=\arccos\frac{\operatorname{tr}R-1}{2},\qquad\boldsymbol{\omega}=\frac{\theta}{2\sin\theta}\begin{pmatrix}R_{32}-R_{23}\\R_{13}-R_{31}\\R_{21}-R_{12}\end{pmatrix}$$
> 幾何意義：$\boldsymbol{\omega}$ 的方向是旋轉軸、長度是旋轉角（軸角表示，axis-angle）。

### 2.3 線性化成最小平方

[▶ 15:46](https://youtu.be/j3VSmUCKZDM?t=946)

- 把 $R_{ij}=R_iR_j^\mathsf{T}$ 改寫成 $\boldsymbol{\omega}$ 的**線性**方程式：
$$
\boldsymbol{\omega}_{ij}=\boldsymbol{\omega}_j-\boldsymbol{\omega}_i
$$
- 把所有絕對旋轉疊成 $\boldsymbol{\omega}_{\text{global}}=(\boldsymbol{\omega}_1^\mathsf{T},\dots,\boldsymbol{\omega}_n^\mathsf{T})^\mathsf{T}$。每條邊一個方程式：
$$
A_{ij}\,\boldsymbol{\omega}_{\text{global}}=\boldsymbol{\omega}_{ij}
$$
  $A_{ij}$ 在第 $j$ 個位置是 $I$、第 $i$ 個位置是 $-I$、其他是 0（選擇器）。
- 所有邊疊起來：
$$
A\,\boldsymbol{\omega}_{\text{global}}=\boldsymbol{\omega}_{\text{relative}}
$$
  用**線性最小平方**解。
- 解出後用**指數映射**換回旋轉矩陣。

> 以下**不是逐字稿內容**：$\boldsymbol{\omega}_{ij}=\boldsymbol{\omega}_j-\boldsymbol{\omega}_i$ **只是近似**——旋轉不可交換，$\log(R_iR_j^\mathsf{T})$ 一般不等於 $\boldsymbol{\omega}_i-\boldsymbol{\omega}_j$（正負號也依 $R_{ij}$ 的定義而定），只有旋轉很小時才近似成立。實務上的旋轉平均（rotation averaging）會在每一步把目前的估計當基準、只線性化殘差的小旋轉，再迭代。另外整體有一個旋轉的規範自由度（gauge），通常固定一台相機 $R_1=I$。

### 2.4 平移

[▶ 18:33](https://youtu.be/j3VSmUCKZDM?t=1113)

- 類似地求全域平移，但多一個麻煩：每條邊的**相對平移尺度未知**（$E$ 只給方向）。
- 把觀測的 $\mathbf{t}_{ij}$ **正規化成長度 1**。
- 最小化：從待求的絕對平移算出的方向（$\mathbf{t}_i-\mathbf{t}_j$，也正規化）和觀測的 $\mathbf{t}_{ij}$ 之間的差。
- 同樣寫成 $A\mathbf{x}=\mathbf{b}$ 的最小平方，$\mathbf{x}$ 是所有絕對平移。

> 以下**不是逐字稿內容**：「$\mathbf{t}_i-\mathbf{t}_j$ 正規化」使問題變成非線性；常見的線性化是要求 $\mathbf{t}_i-\mathbf{t}_j$ 和 $\mathbf{t}_{ij}$ **平行**：$\mathbf{t}_{ij}\times(\mathbf{t}_i-\mathbf{t}_j)=\mathbf{0}$，對未知的 $\mathbf{t}_i$ 是線性的（再加上固定原點和整體尺度）。逐字稿說的方向差異究竟怎麼線性化，以 CVPR 2017 教學投影片為準。

**最後** [▶ 20:11](https://youtu.be/j3VSmUCKZDM?t=1211)：有了所有全域位姿 → 線性三角化得 3D 點 → bundle adjustment 精修。

---

## 3. 階層式 SfM

[▶ 20:43](https://youtu.be/j3VSmUCKZDM?t=1243)

1. **分群**：對場景圖做**階層式分群**，邊的權重 = 兩張圖的 RANSAC 內點數。每一群是一個連得很緊的子圖。
2. **各自重建**：每一群**獨立**做增量式 SfM，得到各自的相機位姿和 3D 點，各在自己的局部世界座標系 $F_{W_1}$、$F_{W_2}$……
3. **合併** [▶ 22:21](https://youtu.be/j3VSmUCKZDM?t=1341)：用**相似變換**把各群對齊到同一個座標系。
   - 群之間的 2D–2D 對應 → 3D–3D 對應 → **絕對定向**（第 21 集）求旋轉、平移。
   - 講者說：再用**一個點對應**就能求兩群之間的尺度差。
   - 合成一個一致的 3D 模型。

> 以下**不是逐字稿內容**，是補充：實務上尺度通常用多對 3D–3D 點的距離比（或 Umeyama 方法同時求 $R,\mathbf{t},s$）來穩健估計，而不是只用一個點。

---

## 4. 一頁速查表

| 做法 | 步驟 | 優點／缺點（推論） |
|---|---|---|
| **增量式** | 選種子對（平移非零、內點最多）→ $F$/$E$/$H$ 分解、尺度設 1 → 三角化 → BA → 每次加一張：2D–2D → 2D–3D → PnP → 三角化新點 → 最後全域 BA | 穩健；但順序處理慢、誤差會累積（漂移） |
| **全域式** | 每條邊算 $R_{ij},\mathbf{t}_{ij}$ → 旋轉平均（$\boldsymbol{\omega}$、$A\boldsymbol{\omega}_{\text{global}}=\boldsymbol{\omega}_{\text{rel}}$）→ 平移平均（單位方向）→ 三角化 → BA | 一次處理全部、誤差平均分攤；對錯誤的邊敏感 |
| **階層式** | 按內點數分群 → 每群增量式 → 絕對定向（相似變換）合併 | 可平行、適合大規模 |

（「優點／缺點」一欄不是逐字稿內容，是依各方法的步驟推論的。）

**指數／對數映射**：$R=\exp([\boldsymbol{\omega}]_\times)$、$[\boldsymbol{\omega}]_\times=\log R$；$\boldsymbol{\omega}$ = 軸 × 角。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| bundle adjustment | 第 29–30 集（Newton、Gauss–Newton、LM、稀疏結構） |
| 指數映射參數化旋轉 | 第 29–30 集（BA 中旋轉的參數化） |
| 相機位姿 + 稀疏點雲 | 第 31–34 集（稠密立體的輸入） |
| 絕對定向合併 | 第 38 集（點雲對齊） |

---

## 附：本集一句話總結

> **SfM 有三種做法：增量式從內點最多、有平移的種子對出發，三角化後每次用 2D–3D 對應做 PnP 加一張新相機、再三角化新點，最後 BA；全域式先算每條邊的相對位姿，用對數映射把旋轉換成 3 維向量做旋轉平均、再做平移平均，一次解出所有絕對位姿；階層式先按內點數分群各自重建，再用絕對定向（相似變換）把各群合併。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 10 (Part 2) 錄影逐字稿（Whisper `medium.en`，23:16）整理；MVG 沒有對應內容。*
