---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-29
lecture: Camera Calibration using Zhang's Method
date: 待補（2021 夏季學期）
video: https://youtu.be/-9He7Nu3u8s
notes: MVG §8.5（書頁 208–212，PDF 頁 226–230）
---

# 第 2-29 集 · 用張正友法校正相機 [▶ 影片](https://youtu.be/-9He7Nu3u8s)

← 上一集：[2-27-dlt](2-27-dlt.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-31-p3p-grunert](2-31-p3p-grunert.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-29 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（41:22，Whisper `medium.en` 轉錄）＋ MVG §8.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

（BRIEF 列 MVG §8.5、§8.8。查過：§8.5 的「絕對二次曲線的像」正好就是本集的矩陣 $B$，已引用；§8.8 是用消失點從單張影像求 $K$，和本集方法不同，未引用。）

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 棋盤格與每張影像自己的座標系](#1-棋盤格與每張影像自己的座標系)
- [2. Z = 0：從 P 到單應矩陣 H](#2-z--0從-p-到單應矩陣-h)
- [3. 用 DLT 的方法估 H](#3-用-dlt-的方法估-h)
- [4. 為什麼不能用 QR 拆 H](#4-為什麼不能用-qr-拆-h)
- [5. 從 H 到 K：四個步驟](#5-從-h-到-k四個步驟)
  - [5.1 寫下約束](#51-寫下約束)
  - [5.2 定義 B](#52-定義-b)
  - [5.3 解 b](#53-解-b)
  - [5.4 Cholesky 分解得 K](#54-cholesky-分解得-k)
- [6. 需要幾張影像、幾個點](#6-需要幾張影像幾個點)
- [7. 非線性參數](#7-非線性參數)
- [8. 總結](#8-總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

**相機校正**：只估**內參**（校正矩陣 $K$），不管相機在哪（DLT 則同時估內外參）。而且不需要已知 3D 控制點，只要一張印出來的**棋盤格**。

- 張正友（Zhang）二十多年前提出，今天是相機校正的標準方法之一，很多校正工具箱都用這個想法。
- 前備：要先懂 DLT（2-27）。張正友法前面幾步和 DLT 一樣，只有最後拆矩陣那一步不同。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Sanck”、“Tsang”、“Tung”、“Sankt”，都是 **Zhang**（張正友）。

---

## 1. 棋盤格與每張影像自己的座標系

[▶ 02:49](https://youtu.be/-9He7Nu3u8s?t=169)

- 棋盤格：黑白圖案印出來，貼在**平的**東西上（木板、紙板，只要平）。拿著它在相機前「跳舞」，拍很多張。
- 已知：棋盤格的尺寸和結構，以及它是**一個平面**（關鍵性質）。
- 跑角點偵測（2-17）找出棋盤格的角點 → 很多點觀測；知道每個點在棋盤格上的哪裡，但**不知道**它們在 3D 世界中的位置。

**技巧** [▶ 04:41](https://youtu.be/-9He7Nu3u8s?t=281)：

- 每張影像定義**自己的**座標系：讓棋盤格就是 $xy$ 平面。
- → 所有角點的 $Z = 0$；$X, Y$ 由印出的格子尺寸得知。
- 座標系每張影像都不同，但同一張影像內相同；這樣就足以估出內參。

---

## 2. Z = 0：從 P 到單應矩陣 H

[▶ 06:09](https://youtu.be/-9He7Nu3u8s?t=369)

$$
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix} = K\,[\,\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol r_3\ \boldsymbol t\,]\begin{bmatrix} X \\ Y \\ 0 \\ 1 \end{bmatrix}
= K\,[\,\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol t\,]\begin{bmatrix} X \\ Y \\ 1 \end{bmatrix}
$$

- $Z = 0$ → $R$ 的第三欄 $\boldsymbol r_3$ 永遠乘到 0，**不需要**；把它和點的第三個座標一起刪掉。
- 定義 $3 \times 3$ 的 **單應矩陣**（homography）：

$$
\boxed{\;H = [\,\boldsymbol h_1\ \boldsymbol h_2\ \boldsymbol h_3\,] = K\,[\,\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol t\,]\;}
$$

- $K$：所有影像共用；$H$（含 $\boldsymbol r_1, \boldsymbol r_2, \boldsymbol t$）：每張影像各自不同（同一張影像的所有角點共用）[▶ 08:08](https://youtu.be/-9He7Nu3u8s?t=488)。

---

## 3. 用 DLT 的方法估 H

[▶ 09:04](https://youtu.be/-9He7Nu3u8s?t=544)

- 和 DLT 的步驟完全一樣：把 $H$ 的 9 個元素 $h_{11}, \dots, h_{33}$ 向量化，用影像座標和棋盤格座標算係數。
- 只是從 $3 \times 4$ 的 $P$（12 維）變成 $3 \times 3$ 的 $H$（9 維）：DLT 係數向量中和 $Z$ 有關的三個元素劃掉：

$$
\boldsymbol a_{x_i}^{\mathsf T} = (-X_i,\ -Y_i,\ -1,\ 0,\ 0,\ 0,\ x_iX_i,\ x_iY_i,\ x_i), \qquad
\boldsymbol a_{y_i}^{\mathsf T} = (0,\ 0,\ 0,\ -X_i,\ -Y_i,\ -1,\ y_iX_i,\ y_iY_i,\ y_i)
$$

（由 2-27 的 $\boldsymbol a_{x_i}, \boldsymbol a_{y_i}$ 刪掉 $Z_i$ 的三欄得到。）

- 堆疊後用 **SVD** 解齊次系統，取最小奇異值的奇異向量 → $H$。

**幾個點？** [▶ 12:02](https://youtu.be/-9He7Nu3u8s?t=722)：$H$ 是 $3 \times 3$（9 個元素），齊次只定到比例 → **8 個自由度**；每個點給 2 個方程 → **每張影像至少 4 個點**。

---

## 4. 為什麼不能用 QR 拆 H

[▶ 13:18](https://youtu.be/-9He7Nu3u8s?t=798)

- DLT 中，$P$ 的左 $3 \times 3$ 塊 $= KR$，三角矩陣乘旋轉矩陣 → QR 分解剛好適用。
- 這裡 $[\,\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol t\,]$ **不是旋轉矩陣**：第三欄被平移 $\boldsymbol t$ 取代了 → 不能用 QR。
- 這是張正友法和 DLT 分道揚鑣的地方：沒有現成的分解能利用這些性質，要**手動**利用 $\boldsymbol r_1, \boldsymbol r_2$ 的約束。

---

## 5. 從 H 到 K：四個步驟

[▶ 15:55](https://youtu.be/-9He7Nu3u8s?t=955)

```
1. 寫下約束：r1、r2 是旋轉矩陣的兩欄
2. 定義 B = K⁻ᵀ K⁻¹（約束裡反覆出現）
3. 用約束建線性系統，SVD 解出 B 的元素
4. Cholesky 分解 B → K
```

### 5.1 寫下約束

[▶ 18:04](https://youtu.be/-9He7Nu3u8s?t=1084)

- $K$ 是上三角、對角元素都不為零 → **可逆**。左乘 $K^{-1}$：

$$
[\,\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol t\,] = K^{-1}[\,\boldsymbol h_1\ \boldsymbol h_2\ \boldsymbol h_3\,]
\quad\Rightarrow\quad
\boldsymbol r_1 = K^{-1}\boldsymbol h_1, \qquad \boldsymbol r_2 = K^{-1}\boldsymbol h_2
$$

（$H$ 已知，$K$ 未知，所以還不能直接算。）

- $\boldsymbol r_1, \boldsymbol r_2$ 是旋轉矩陣的欄 → **單位正交**：

$$
\boldsymbol r_1^{\mathsf T}\boldsymbol r_2 = 0, \qquad \lVert\boldsymbol r_1\rVert = \lVert\boldsymbol r_2\rVert = 1
$$

- 代入 [▶ 21:05](https://youtu.be/-9He7Nu3u8s?t=1265)：

$$
\boldsymbol h_1^{\mathsf T}K^{-\mathsf T}K^{-1}\boldsymbol h_2 = 0, \qquad
\boldsymbol h_1^{\mathsf T}K^{-\mathsf T}K^{-1}\boldsymbol h_1 - \boldsymbol h_2^{\mathsf T}K^{-\mathsf T}K^{-1}\boldsymbol h_2 = 0
$$

（第二式由 $\boldsymbol r_1^{\mathsf T}\boldsymbol r_1 = \boldsymbol r_2^{\mathsf T}\boldsymbol r_2$ 移項得到。）

- 已知的 $\boldsymbol h$、未知的 $K$，都等於零。

### 5.2 定義 B

[▶ 23:13](https://youtu.be/-9He7Nu3u8s?t=1393)

$$
B = K^{-\mathsf T}K^{-1} \qquad (\text{對稱、正定})
\quad\Rightarrow\quad
\boldsymbol h_1^{\mathsf T}B\boldsymbol h_2 = 0, \qquad \boldsymbol h_1^{\mathsf T}B\boldsymbol h_1 - \boldsymbol h_2^{\mathsf T}B\boldsymbol h_2 = 0
$$

- **關鍵**：$B$ 是「矩陣的轉置乘矩陣」→ 對稱正定矩陣可以用 **Cholesky 分解**拆成三角矩陣乘它的轉置 $B = AA^{\mathsf T}$。令 $A = K^{-\mathsf T}$ → 知道 $B$ 就能直接得到 $K$（再求個 $3 \times 3$ 反矩陣）[▶ 25:13](https://youtu.be/-9He7Nu3u8s?t=1513)。

【課本補充】MVG §8.5（書頁 210–211）：$B = K^{-\mathsf T}K^{-1} = (KK^{\mathsf T})^{-1}$ 正是**絕對二次曲線的像**（image of the absolute conic，IAC）$\omega$（結果 8.17）。它只和內參有關，和相機的朝向、位置無關。找到 $\omega$ 就能用 Cholesky 分解得到 $K$（上三角、對角為正）。

### 5.3 解 b

[▶ 25:31](https://youtu.be/-9He7Nu3u8s?t=1531)

- $B$ 對稱 → 只有 **6 個未知數**：

$$
B = \begin{bmatrix} B_{11} & B_{12} & B_{13} \\ B_{12} & B_{22} & B_{23} \\ B_{13} & B_{23} & B_{33} \end{bmatrix}, \qquad
\boldsymbol b = (B_{11}, B_{12}, B_{22}, B_{13}, B_{23}, B_{33})^{\mathsf T}
$$

（$\boldsymbol b$ 也只定到比例。）

- 兩個約束都能寫成「係數向量 × $\boldsymbol b$ = 0」：

$$
\boldsymbol h_i^{\mathsf T}B\boldsymbol h_j = \boldsymbol v_{ij}^{\mathsf T}\boldsymbol b
\quad\Rightarrow\quad
\begin{bmatrix} \boldsymbol v_{12}^{\mathsf T} \\ (\boldsymbol v_{11} - \boldsymbol v_{22})^{\mathsf T} \end{bmatrix}\boldsymbol b = \mathbf 0
$$

- 講者說 $\boldsymbol v_{ij}$ 的元素都是 $H$ 的元素、可以直接由約束推出，但沒有念出來。以下不是逐字稿內容，是把 $\boldsymbol h_i^{\mathsf T}B\boldsymbol h_j$ 展開推得的（$h_{ik}$ 表示 $\boldsymbol h_i$ 的第 $k$ 個元素）：

$$
\boldsymbol v_{ij} = \bigl(\, h_{i1}h_{j1},\ \ h_{i1}h_{j2} + h_{i2}h_{j1},\ \ h_{i2}h_{j2},\ \ h_{i3}h_{j1} + h_{i1}h_{j3},\ \ h_{i3}h_{j2} + h_{i2}h_{j3},\ \ h_{i3}h_{j3} \,\bigr)^{\mathsf T}
$$

  （驗證：$\boldsymbol h_i^{\mathsf T}B\boldsymbol h_j = \sum_{k,l} h_{ik}B_{kl}h_{jl}$；對角項 $B_{kk}$ 的係數是 $h_{ik}h_{jk}$，非對角 $B_{kl} = B_{lk}$ 的係數是 $h_{ik}h_{jl} + h_{il}h_{jk}$。）

- 每張影像給一個 $2 \times 6$ 矩陣 → 至少要 **3 張**才有 $6 \times 6$。$n$ 張堆成 $2n \times 6$ 的 $V$（第 $2k-1$、$2k$ 列來自第 $k$ 張）[▶ 29:01](https://youtu.be/-9He7Nu3u8s?t=1741)：

$$
V\boldsymbol b = \mathbf 0, \qquad V \in \mathbb R^{2n \times 6}
$$

- 解法同 DLT：限制 $\lVert\boldsymbol b\rVert = 1$（排除零解），SVD，取**最小奇異值**對應的奇異向量 $\boldsymbol b^*$（理想奇異值是 0，實際量測有雜訊不是 0）。

【課本補充】MVG §8.5 例 8.18（書頁 211）的「簡單校正裝置」是同一個想法：三個（不平行、不必正交）平面上的正方形，各求一個單應 $H$；平面的 circular points 經 $H$ 映成 $\boldsymbol h_1 \pm i\boldsymbol h_2$，它們必須落在 $\omega$ 上；把 $(\boldsymbol h_1 \pm i\boldsymbol h_2)^{\mathsf T}\omega(\boldsymbol h_1 \pm i\boldsymbol h_2) = 0$ 拆成實部和虛部：

$$
\boldsymbol h_1^{\mathsf T}\omega\boldsymbol h_2 = 0, \qquad \boldsymbol h_1^{\mathsf T}\omega\boldsymbol h_1 = \boldsymbol h_2^{\mathsf T}\omega\boldsymbol h_2 \qquad (8.12)
$$

——和講者從「$\boldsymbol r_1, \boldsymbol r_2$ 單位正交」推出的兩個約束**完全相同**。$\omega$ 由 5 個以上這種方程定到比例，再用 Cholesky 分解得 $K$。好處：不需要量測 3D 座標。圖 8.12 的例子（1024 × 768 影像）：$K = \begin{bmatrix} 1108.3 & -9.8 & 525.8 \\ 0 & 1097.8 & 395.9 \\ 0 & 0 & 1 \end{bmatrix}$。

### 5.4 Cholesky 分解得 K

[▶ 30:59](https://youtu.be/-9He7Nu3u8s?t=1859)

$$
\boldsymbol b^* \to B, \qquad B = AA^{\mathsf T}\ (\text{Cholesky}), \qquad A = K^{-\mathsf T}\ \Rightarrow\ K = (A^{\mathsf T})^{-1}
$$

（講者只說「對 $B$ 做 Cholesky 分解得到 $K$」。以下不是逐字稿內容，是依推導補的實作提醒：$\boldsymbol b^*$ 只定到比例和**正負號**，若解出的 $B$ 不是正定，要先乘 $-1$；最後把 $K$ 除以 $K_{33}$ 讓右下角為 1。）

---

## 6. 需要幾張影像、幾個點

[▶ 31:07](https://youtu.be/-9He7Nu3u8s?t=1867)

| 量 | 自由度 | 每單位給的方程 | 需要 |
|---|---|---|---|
| $H$（每張影像） | 8（9 元素 − 比例） | 每點 2 個 | 每張 ≥ **4 點** |
| $B$（共用） | 5（6 元素 − 比例） | 每張影像 2 個 | ≥ **3 張影像** |

- 為什麼比 DLT 多工作、還要多張影像：要拆的矩陣不是「三角 × 旋轉」，只知道其中兩欄來自旋轉矩陣 → 只能得到每張 2 個約束，所以至少 3 張 [▶ 32:35](https://youtu.be/-9He7Nu3u8s?t=1955)。
- 得到 $K$ 的 5 個線性參數 = 相機校正的第一步。

---

## 7. 非線性參數

[▶ 33:52](https://youtu.be/-9He7Nu3u8s?t=2032)

- 2-24：校正矩陣左邊再乘一個位置相依的位移（考慮非線性誤差），例如**桶形畸變**（或反向的枕形，或兩者組合）。
- 模型例：

$$
x' = x\,(1 + q_1 r^2 + q_2 r^4)
$$

  $r$ = 像素到光軸（主點）的距離，越遠修正越強。廣角鏡頭特別需要。

**最小平方估計** [▶ 36:06](https://youtu.be/-9He7Nu3u8s?t=2166)：最小化**重投影誤差**——每張影像、每個點，「實際量到的位置」和「依參數投影應該在的位置」的距離平方和：

$$
\min_{K,\ \boldsymbol q,\ \{R_n, \boldsymbol t_n\}} \sum_{n=1}^{N}\sum_{i} \bigl\lVert \boldsymbol x_{ni} - \hat{\boldsymbol x}(K, \boldsymbol q, R_n, \boldsymbol t_n, \boldsymbol X_i) \bigr\rVert^2
$$

（講者說「對所有影像、每張影像的每個點求和，量到的位置減去應該在的位置」；把每張影像的外參也列為最佳化變數是依「投影需要位姿」補上的。）

- 要初始猜測：非線性參數設為 0，用上面的張正友直接解當作 $K$ 的初值（直接解不需要迭代）。
- 再跑最小平方，更新校正矩陣和非線性參數。
- 例 [▶ 37:45](https://youtu.be/-9He7Nu3u8s?t=2265)：輸入影像中棋盤格的線因桶形畸變而彎曲；套用校正參數後變成完美的直線。

---

## 8. 總結

[▶ 38:18](https://youtu.be/-9He7Nu3u8s?t=2298)

- 用棋盤格校正相機，假設針孔模型 $\mathbf x = P\mathbf X$。
- 第一步：張正友法估校正矩陣的 5 個線性參數；第二步：用非線性最小平方加上非線性參數。
- 棋盤格讓校正很容易：不需要有已知 3D 點的校正室；印一張紙、貼在平的硬板上、在相機前展示就行。
- 【口頭】要確保相機影像的**每個部分**都看過棋盤格 [▶ 39:28](https://youtu.be/-9He7Nu3u8s?t=2368)。
- 很多標準工具箱都用棋盤格；了解內部原理，就知道為什麼需要一定數量的影像、用了哪些假設、矩陣怎麼拆。
- 解齊次線性系統非常常見，有很多實際應用。
- 參考：張正友的原始論文（記號和講者不同）；更深入可看 Förstner 和 Wrobel 的 *Photogrammetric Computer Vision*（有 DLT、不確定性等嚴謹描述）。
- `⚠️ 逐字稿缺字`：Whisper 寫 “first-known Robles book”，推測為 **Förstner & Wrobel** 的書。

---

## 9. 一頁速查表

### 9.1 流程

| 步驟 | 做法 |
|---|---|
| 1 | 每張影像：棋盤格平面當 $Z = 0$，角點偵測 |
| 2 | 每張影像：$H = K[\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol t]$，DLT 式（9 維、≥4 點）＋ SVD |
| 3 | 每張影像兩列：$\boldsymbol v_{12}^{\mathsf T}$、$(\boldsymbol v_{11} - \boldsymbol v_{22})^{\mathsf T}$ |
| 4 | ≥3 張堆成 $V\boldsymbol b = 0$，SVD 取最小奇異向量 |
| 5 | $B = K^{-\mathsf T}K^{-1}$，Cholesky → $K$ |
| 6 | 非線性參數設 0 當初值，最小化重投影誤差（LM） |

### 9.2 關鍵式

$$
\boldsymbol h_1^{\mathsf T}B\boldsymbol h_2 = 0, \qquad \boldsymbol h_1^{\mathsf T}B\boldsymbol h_1 = \boldsymbol h_2^{\mathsf T}B\boldsymbol h_2, \qquad B = K^{-\mathsf T}K^{-1} = \omega
$$

關鍵一步：$\boldsymbol r_1 = K^{-1}\boldsymbol h_1$、$\boldsymbol r_2 = K^{-1}\boldsymbol h_2$ 單位正交 → 代入就是兩個對 $B$ **線性**的方程。

$$
\boldsymbol v_{ij} = (h_{i1}h_{j1},\ h_{i1}h_{j2} + h_{i2}h_{j1},\ h_{i2}h_{j2},\ h_{i3}h_{j1} + h_{i1}h_{j3},\ h_{i3}h_{j2} + h_{i2}h_{j3},\ h_{i3}h_{j3})^{\mathsf T}
$$

（筆記推導。）

### 9.3 計數

$H$：8 自由度 → 每張 ≥ 4 點；$B$：5 自由度、每張 2 方程 → ≥ 3 張。

### 9.4 和 DLT 比較

| | DLT | 張正友 |
|---|---|---|
| 求 | 內參＋外參（11） | 內參（5，再加非線性） |
| 需要 | ≥6 個**不共平面**的已知 3D 點 | 平面棋盤格，≥3 張影像 |
| 拆矩陣 | QR（$KR$） | 約束 → $B$ → Cholesky |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 已校正相機（已知 $K$） | 2-31 P3P、2-33～2-37 本質矩陣 |
| 單應矩陣 $H$ | 2-37（平面場景的退化） |
| 重投影誤差最小化 | 2-12 光束法平差 |

---

## 附：本集一句話總結

> **張正友法：把棋盤格平面當 $Z = 0$，每張影像的投影化成單應 $H = K[\boldsymbol r_1\ \boldsymbol r_2\ \boldsymbol t]$（DLT 式求，≥4 點）；$\boldsymbol r_1, \boldsymbol r_2$ 單位正交給出兩個對 $B = K^{-\mathsf T}K^{-1}$ 線性的約束，≥3 張影像用 SVD 解出 $B$，Cholesky 分解得 $K$；最後以此為初值，最小化重投影誤差加入畸變參數。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Camera Calibration using Zhang's Method 錄影逐字稿（Whisper `medium.en`，41:22）與 MVG §8.5 整理。*
