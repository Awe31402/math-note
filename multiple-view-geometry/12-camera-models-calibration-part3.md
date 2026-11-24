---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 12
lecture: Lecture 5 (Part 3) – Camera models and calibration
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/77kpTQUfIBg
notes: Zhang 校正法講者取自 Zhang (2000) 論文（BRIEF 沒列，未查）；可對照 MVG §8.5 Example 8.18（書頁 210–211，PDF 頁 228–229）；鏡頭畸變對照 MVG §7.4（書頁 189–193，PDF 頁 207–211）
---

# 第 12 集 · Lecture 5 (Part 3)：Zhang 棋盤格校正法、鏡頭畸變 [▶ 影片](https://youtu.be/77kpTQUfIBg)

← 上一集：[11-camera-models-calibration-part2](11-camera-models-calibration-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[13-single-view-metrology-part1](13-single-view-metrology-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 12 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（34:31，Whisper `medium.en` 轉錄）＋ MVG §8.5 Example 8.18、§7.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 校正（resectioning）與工具](#1-校正resectioning與工具)
- [2. Zhang 方法：棋盤格 → homography](#2-zhang-方法棋盤格--homography)
- [3. 從 homography 得到 K 的約束](#3-從-homography-得到-k-的約束)
- [4. 解 B，再用 Cholesky 得 K](#4-解-b再用-cholesky-得-k)
- [5. 解外參](#5-解外參)
- [6. 鏡頭畸變](#6-鏡頭畸變)
  - [6.1 徑向畸變、切向畸變](#61-徑向畸變切向畸變)
  - [6.2 Brown 模型](#62-brown-模型)
  - [6.3 用重投影誤差一起最佳化](#63-用重投影誤差一起最佳化)
  - [6.4 去畸變：查表](#64-去畸變查表)
- [7. Lecture 5 總結](#7-lecture-5-總結)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/77kpTQUfIBg?t=0)

- 射影相機 $P=K[R\mid\mathbf{t}]$ 有 11 個自由度：$K$ 5 個（內參）+ $R$、$\mathbf{t}$ 各 3 個（外參）。
- 「百萬美元問題」：怎麼求出這 11 個參數？答案是**校正（calibration）**。

| 主題 | 來源 |
|---|---|
| Zhang 棋盤格校正法 | Zhang (2000)；MVG Example 8.18 |
| 徑向、切向畸變的模型與估計 | Brown (1971)；MVG §7.4 |

---

## 1. 校正（resectioning）與工具

[▶ 00:53](https://youtu.be/77kpTQUfIBg?t=53)

- 校正也常叫**相機後方交會（camera resectioning）**：求出組成投影矩陣的內參和外參。
- 最簡單、最常用的方法：用一個 **2D 校正圖案**——圓點圖案，或更常見的**棋盤格（checkerboard）**。
- 要把圖案**印出來、貼在一塊平板上**（必須是平面，原因見下）。
- 講者主要講 Zhang Zhengyou〈A Flexible New Technique for Camera Calibration〉（T-PAMI 2000）。

⚠️ 逐字稿缺字：Whisper 把 Zhang Zhengyou 寫成 “Kang Sen Yeo”、“Zhang Zhenyu”、“Tanzanio”；把 T-PAMI 寫成 “Tipami”。

**開源工具** [▶ 01:52](https://youtu.be/77kpTQUfIBg?t=112)【口頭】：都基於 Zhang 的論文。

- **Bouguet 校正工具箱**（Matlab，作者是 Bouguet）。
- 後來有人改寫成 C++，現在 **OpenCV** 也有（講者投影片寫 2.4 版，說現在可能已經 3 點多或 4）。也有 Python 版。
- Bouguet 工具箱也被移植到 Matlab 的影像處理工具箱（付費）。

---

## 2. Zhang 方法：棋盤格 → homography

[▶ 02:54](https://youtu.be/77kpTQUfIBg?t=174)

**步驟一：在棋盤格上建世界座標系**：

- 把世界座標的 $XY$ 平面放在棋盤格平面上 → 棋盤格上**所有點的 $Z=0$**。
- 偵測棋盤格的**角點**，每個角點的世界座標是 $(X,Y,0,1)^\mathsf{T}$。

**步驟二：代入投影式** [▶ 03:42](https://youtu.be/77kpTQUfIBg?t=222)：

$$
s\begin{pmatrix}x\\y\\1\end{pmatrix}=K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{r}_3\ \mathbf{t}]\begin{pmatrix}X\\Y\\0\\1\end{pmatrix}=K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]\begin{pmatrix}X\\Y\\1\end{pmatrix}
$$

- $s$：未知的尺度（把像點寫成正規化齊次座標時提出來的）。
- $Z=0$ 乘上 $R$ 的第三行 $\mathbf{r}_3$ → $\mathbf{r}_3$ 和 $Z$ 都可以拿掉。

**這是一個 homography** [▶ 05:30](https://youtu.be/77kpTQUfIBg?t=330)：

- 從棋盤格平面（$\mathbb{P}^2$）映到影像（$\mathbb{P}^2$），**平面到平面** → 就是第 08 集的 homography：
$$
H=[\mathbf{h}_1\ \mathbf{h}_2\ \mathbf{h}_3]=\lambda K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]
$$
  （講者寫成 $sH=K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]$，只是尺度放在哪一邊的差別。）
- **已知**：像點 $(x,y)$（從影像偵測）、世界點 $(X,Y)$（棋盤格每格大小已知，例如 1 cm × 1 cm，也知道有幾格、黑白怎麼排 → 角點一對一對應）。
- **未知**：$H$ 和尺度。
- 每個視角用至少 4 對角點，以 DLT（第 08 集）求出 $H$。

---

## 3. 從 homography 得到 K 的約束

[▶ 07:44](https://youtu.be/77kpTQUfIBg?t=464)

從 $sH=K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]$ 逐行看：

$$
\mathbf{r}_1=sK^{-1}\mathbf{h}_1,\qquad \mathbf{r}_2=sK^{-1}\mathbf{h}_2
$$

- $\mathbf{r}_1,\mathbf{r}_2$ 還不知道，但它們是旋轉矩陣的前兩行，**單位正交**（第 03 集）。這給出兩個約束：

**約束 1：垂直** [▶ 08:42](https://youtu.be/77kpTQUfIBg?t=522)：$\mathbf{r}_1^\mathsf{T}\mathbf{r}_2=0$

$$
\mathbf{h}_1^\mathsf{T}K^{-\mathsf{T}}K^{-1}\mathbf{h}_2=0\qquad(1)
$$

**約束 2：等長** [▶ 09:06](https://youtu.be/77kpTQUfIBg?t=546)：$\mathbf{r}_1^\mathsf{T}\mathbf{r}_1=\mathbf{r}_2^\mathsf{T}\mathbf{r}_2$

$$
\mathbf{h}_1^\mathsf{T}K^{-\mathsf{T}}K^{-1}\mathbf{h}_1=\mathbf{h}_2^\mathsf{T}K^{-\mathsf{T}}K^{-1}\mathbf{h}_2\qquad(2)
$$

（$s^2$ 在兩邊同時出現，約掉。）

【口頭】[▶ 09:29](https://youtu.be/77kpTQUfIBg?t=569) 講者預告：$K^{-\mathsf{T}}K^{-1}$ 就是下一講的**絕對二次曲線的像** $\omega$。

【課本補充】MVG §8.5 Example 8.18 用 circular points 解釋同一件事：

- 平面上的 circular points $(1,\pm i,0)^\mathsf{T}$ 經 $H$ 投影成 $\mathbf{h}_1\pm i\mathbf{h}_2$。
- 它們一定落在絕對二次曲線的像 $\omega=(KK^\mathsf{T})^{-1}$ 上（第 07 集：圓和 $\Omega_\infty$ 交於 circular points）：$(\mathbf{h}_1\pm i\mathbf{h}_2)^\mathsf{T}\omega(\mathbf{h}_1\pm i\mathbf{h}_2)=0$。
- 展開取虛部、實部，正好得到 (1)、(2)。
- MVG 的版本是三個不平行平面上各一個正方形（Fig. 8.12），每個正方形給兩條約束；Zhang 的版本是同一個棋盤格在不同姿態下拍好幾張——數學一樣。

> 以下**不是逐字稿內容**，是展開的關鍵一步：$(\mathbf{h}_1+i\mathbf{h}_2)^\mathsf{T}\omega(\mathbf{h}_1+i\mathbf{h}_2)=\left(\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_1-\mathbf{h}_2^\mathsf{T}\omega\mathbf{h}_2\right)+2i\,\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_2$（用 $\omega$ 對稱）。實部、虛部都要是 0。

---

## 4. 解 B，再用 Cholesky 得 K

[▶ 09:54](https://youtu.be/77kpTQUfIBg?t=594)

**令** $B=K^{-\mathsf{T}}K^{-1}$（$3\times3$）：

- $B$ **對稱**。
- $B$ **正定**：它可以看成「一個矩陣的平方」，特徵值嚴格為正。
- 對稱 → 只有 6 個獨立元素，排成 6 維向量 $\mathbf{b}$。

**化成線性方程式** [▶ 10:38](https://youtu.be/77kpTQUfIBg?t=638)：

- (1) 變成 $\mathbf{h}_1^\mathsf{T}B\mathbf{h}_2=0$；(2) 移項成 $\mathbf{h}_1^\mathsf{T}B\mathbf{h}_1-\mathbf{h}_2^\mathsf{T}B\mathbf{h}_2=0$。
- 兩者都對 $\mathbf{b}$ 線性，疊起來：
$$
A\mathbf{b}=\mathbf{0},\qquad A\in\mathbb{R}^{2\times6}\ (\text{一個視角})
$$
- $A$ 由 homography 的元素（$\mathbf{h}_1,\mathbf{h}_2$）組成；$\mathbf{b}$ 是 $K$ 的未知數。

> 以下**不是逐字稿內容**：逐字稿沒唸出 $A$ 的元素。依雙線性形式直接展開（$\mathbf{b}=(B_{11},B_{12},B_{22},B_{13},B_{23},B_{33})^\mathsf{T}$，$h_{ik}$ 是 $\mathbf{h}_i$ 的第 $k$ 個分量）：
> $$\mathbf{h}_i^\mathsf{T}B\mathbf{h}_j=\mathbf{v}_{ij}^\mathsf{T}\mathbf{b},\quad \mathbf{v}_{ij}=\begin{pmatrix}h_{i1}h_{j1}\\ h_{i1}h_{j2}+h_{i2}h_{j1}\\ h_{i2}h_{j2}\\ h_{i3}h_{j1}+h_{i1}h_{j3}\\ h_{i3}h_{j2}+h_{i2}h_{j3}\\ h_{i3}h_{j3}\end{pmatrix}$$
> 每個視角的兩列是 $\mathbf{v}_{12}^\mathsf{T}$ 和 $(\mathbf{v}_{11}-\mathbf{v}_{22})^\mathsf{T}$。

**需要幾個視角** [▶ 12:12](https://youtu.be/77kpTQUfIBg?t=732)：

- $\mathbf{b}$ 有 6 個未知數；每個視角給 2 條方程式 → **至少 3 個視角**。
- 做法：相機固定，**拿著棋盤格在相機前移動**（或固定棋盤格、移動相機），拍至少 3 張不同姿態。

⚠️ 逐字稿缺字 [▶ 12:19](https://youtu.be/77kpTQUfIBg?t=739)：講者說「one of the point correspondence here is going to give us a 2×6 entry in A」，依上下文應為「每個**視角**（每個 homography）」給 $2\times6$。

> 以下**不是逐字稿內容**，是自由度的細節：$\mathbf{b}$ 差一個縮放，所以只有 5 個自由度；3 個視角給 6 條方程式，已經超過 5。Zhang 論文另外指出：若假設斜切 $s=0$，2 個視角就夠。

**解** [▶ 14:50](https://youtu.be/77kpTQUfIBg?t=890)：

- 3 個視角疊成 $6\times6$ 的 $A$。對 $A$ 做 SVD，$\mathbf{b}$ = 最小奇異值對應的右奇異向量（第 08 集的最小平方解）。
- 對應點有雜訊，$A$ 不精確 → **拍越多張越好**，約束越多，$\mathbf{b}$ 越準。

**從 $B$ 得 $K$** [▶ 16:03](https://youtu.be/77kpTQUfIBg?t=963)：

1. 把 $\mathbf{b}$ 排回對稱矩陣 $B$。
2. $B=K^{-\mathsf{T}}K^{-1}=(KK^\mathsf{T})^{-1}$，所以 $B^{-1}=KK^\mathsf{T}$。
3. 對 $B^{-1}$ 做 **Cholesky 分解**，得到三角矩陣 $K$。

⚠️ 逐字稿缺字 [▶ 16:29](https://youtu.be/77kpTQUfIBg?t=989)：Whisper 寫「equivalent to K transpose K inverse」，依 $B=K^{-\mathsf{T}}K^{-1}$ 應為 $B^{-1}=KK^\mathsf{T}$。

> 以下**不是逐字稿內容**，是補充：標準 Cholesky 分解給的是「下三角 × 其轉置」$LL^\mathsf{T}$；$K$ 是上三角，所以實作上要用「上三角版」的分解（例如把矩陣的列、行順序都反過來做 Cholesky 再反回來），或直接對 $B$ 做 Cholesky 得 $K^{-\mathsf{T}}$ 再求逆。最後把 $K$ 除以 $K_{33}$。$B$ 要正定；SVD 解出的 $\mathbf{b}$ 可能差一個負號，若 $B$ 負定就整體乘 $-1$。

---

## 5. 解外參

[▶ 17:04](https://youtu.be/77kpTQUfIBg?t=1024)

- $K$ 對所有視角都一樣。但**每個視角有自己的** $R_i$、$\mathbf{t}_i$（相機固定時，棋盤格每次的位姿都不同）。
- 從 $sH=K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]$（每個視角各用自己的 $H$）：
$$
\mathbf{r}_1=sK^{-1}\mathbf{h}_1,\qquad \mathbf{r}_2=sK^{-1}\mathbf{h}_2,\qquad \mathbf{r}_3=\mathbf{r}_1\times\mathbf{r}_2,\qquad \mathbf{t}=sK^{-1}\mathbf{h}_3
$$
- **唯一的未知數 $s$** [▶ 19:04](https://youtu.be/77kpTQUfIBg?t=1144)：因為 $\|\mathbf{r}_1\|=1$，
$$
s=\frac{1}{\|K^{-1}\mathbf{h}_1\|}
$$
- 代回去就得到每個視角的 $\mathbf{r}_1,\mathbf{r}_2,\mathbf{r}_3,\mathbf{t}$。

（$s$ 的公式依「$\|\mathbf{r}_1\|=1$」寫出；逐字稿只說「取這個的範數必須等於 1，就能解出 $s$」。）

> 以下**不是逐字稿內容**，是補充：有雜訊時，$[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{r}_3]$ 一般不是精確的旋轉矩陣。Zhang 論文用 SVD 把它投影到最近的旋轉矩陣（$R=UV^\mathsf{T}$）。

---

## 6. 鏡頭畸變

### 6.1 徑向畸變、切向畸變

[▶ 19:58](https://youtu.be/77kpTQUfIBg?t=1198)

到目前求了 11 個參數。還有一組未知數：**鏡頭畸變（lens distortion）**。手機、單眼、口袋相機拍的照片都看得到某種畸變。

**徑向畸變（radial distortion）** [▶ 20:36](https://youtu.be/77kpTQUfIBg?t=1236)：最常見。

- 很凸的鏡頭（例如**魚眼鏡頭**）特別明顯，一般鏡頭也有。
- **負徑向畸變**：像素往中心擠。
- **正徑向畸變**（更常見）：沿徑向往外拉。
- 正常影像應該每個像素都是規則排列的。

**切向畸變（tangential distortion）** [▶ 21:18](https://youtu.be/77kpTQUfIBg?t=1278)：比較少見，多出現在便宜相機。

- 原因：製造不精確，**感光元件和鏡頭沒有平行對齊**（可能是感光元件歪了，也可能是鏡頭歪了），光線無法正確對焦。

【課本補充】MVG §7.4：焦距越短（鏡頭越便宜），徑向畸變越明顯；影像邊緣的直線會被拍成曲線。

### 6.2 Brown 模型

**徑向畸變** [▶ 22:20](https://youtu.be/77kpTQUfIBg?t=1340)：

- $\mathbf{x}=(x,y)$：沒有畸變時的像點；$\mathbf{y}$：有畸變後的位置。
- 找一個參數化函數 $f$，$\mathbf{y}=f(\mathbf{x})$。Brown〈Close-range camera calibration〉（1971）提出：
$$
\begin{pmatrix}x_r\\y_r\end{pmatrix}=\left(1+k_1r^2+k_2r^4+k_5r^6\right)\begin{pmatrix}x\\y\end{pmatrix},\qquad r^2=x^2+y^2
$$
- $k_1,k_2,k_5$：徑向畸變參數，校正時要求出來。

**切向畸變** [▶ 24:19](https://youtu.be/77kpTQUfIBg?t=1459)：

- 不是直接給畸變後的位置，而是給一個**位移量** $d\mathbf{x}$，加在徑向畸變的結果上：
$$
\mathbf{x}_d=\begin{pmatrix}x_r\\y_r\end{pmatrix}+d\mathbf{x}
$$
- $d\mathbf{x}$ 是 $\mathbf{x}$ 的函數，用到 $r^2=x^2+y^2$，多兩個參數 $k_3,k_4$。

> 以下**不是逐字稿內容**：逐字稿沒唸出 $d\mathbf{x}$ 的式子。依 Brown 模型的常見寫法（也是 Bouguet 工具箱用 $k_1\dots k_5$ 這種編號時的寫法）：
> $$d\mathbf{x}=\begin{pmatrix}2k_3xy+k_4(r^2+2x^2)\\ k_3(r^2+2y^2)+2k_4xy\end{pmatrix}$$
> 這個式子沒有用 BRIEF 列的來源核對過，見待確認清單。

- **合計 5 個畸變參數**：$k_1,k_2,k_5$（徑向）、$k_3,k_4$（切向）。

（$k_1,k_2,k_5$ 為徑向、$k_3,k_4$ 為切向是講者的編號 [▶ 26:19](https://youtu.be/77kpTQUfIBg?t=1579)。）

【課本補充】MVG §7.4 的徑向模型寫法不同：$\begin{pmatrix}x_d\\y_d\end{pmatrix}=L(\tilde{r})\begin{pmatrix}\tilde{x}\\\tilde{y}\end{pmatrix}$，$L(r)=1+\kappa_1r+\kappa_2r^2+\kappa_3r^3+\cdots$（泰勒展開），$L(0)=1$。畸變中心常取主點，但不一定剛好重合。MVG 還提到另一種求 $L(r)$ 的方法：要求「場景中的直線在校正後的影像裡是直的」，不需要校正板（適合有很多直線的城市場景）。

### 6.3 用重投影誤差一起最佳化

[▶ 26:55](https://youtu.be/77kpTQUfIBg?t=1615)

**怎麼求 $k_1\dots k_5$**：用**迭代精修**（最大概似估計），放在最後一步。

1. 先用 Zhang 方法求出 $K$ 和每個視角的 $R_i,\mathbf{t}_i$。
2. 最小化**重投影誤差**：
$$
\min_{K,\ \{R_i,\mathbf{t}_i\},\ k_1,\dots,k_5}\ \sum_i\sum_j\left\|\mathbf{x}_{ij}-\pi\left(K,R_i,\mathbf{t}_i,k_1,\dots,k_5,\mathbf{X}_j\right)\right\|^2
$$
   - $\mathbf{X}_j$：棋盤格上第 $j$ 個角點。
   - $\mathbf{x}_{ij}$：它在第 $i$ 張影像上的觀測位置。
   - $\pi$：投影函數——先用 $P_i=K[R_i\mid\mathbf{t}_i]$ 投影（假設完美、無畸變），再丟進畸變函數得到畸變後的位置。
3. 這是**無約束連續最佳化**，用 **Levenberg–Marquardt** 解（講者說細節在 bundle adjustment 那講）。
4. **初值**：$K,R_i,\mathbf{t}_i$ 用 Zhang 方法的結果；畸變參數**初始化為 0**——它們通常很小、接近 0，所以 0 是很好的初值。
5. 結果：所有內參、外參、畸變參數的新估計。

⚠️ 逐字稿缺字：Whisper 把 Levenberg–Marquardt 寫成 “lower Markov”。

（目標函數是依講者描述「$\pi$ 是投影函數、$\mathbf{x}_{ij}$ 是第 $i$ 張圖第 $j$ 點、最小化平方誤差」寫出的。）

**為什麼要這一步** [▶ 31:01](https://youtu.be/77kpTQUfIBg?t=1861)：

- 重投影誤差是**幾何誤差**（第 09 集）。
- Zhang 方法解 $A\mathbf{b}=\mathbf{0}$ 是**代數誤差**，比較不準。
- 最後做一次重投影誤差最小化，校正結果準很多。

### 6.4 去畸變：查表

[▶ 32:01](https://youtu.be/77kpTQUfIBg?t=1921)

- 知道畸變函數 $f$（無畸變 → 有畸變）後，就能做**鏡頭畸變校正（lens distortion correction）**。
- **查表法**（和第 05 集的反向映射同樣的想法）：
  1. 對**去畸變後**影像的每個像素 $\mathbf{x}$，算出 $\mathbf{y}=f(\mathbf{x})$——它在原始（有畸變）影像中的位置。
  2. 建成查表（lookup table）。
  3. 到原始影像的 $\mathbf{y}$ 取顏色，填進 $\mathbf{x}$。

⚠️ 逐字稿缺字：Whisper 把 lookup table 寫成 “lookout table”。

---

## 7. Lecture 5 總結

[▶ 33:22](https://youtu.be/77kpTQUfIBg?t=2002)

1. 用針孔相機模型描述相機投影（第 10 集）。
2. 從投影矩陣找出相機中心、主平面、主點、主軸（第 10 集）。
3. 用投影矩陣做前向、反向投影（第 11 集）。
4. 常見仿射相機的性質和定義（第 11 集）。
5. Zhang 方法校正內參、外參（本集）。
6. 徑向、切向畸變：怎麼校正出參數、怎麼去除畸變（本集）。

---

## 8. 一頁速查表

### Zhang 校正法

**在解什麼**：求相機內參 $K$（5 dof）和每張照片的外參。

**步驟**：

1. 棋盤格平面設 $Z=0$；拍 $\ge3$ 張不同姿態。
2. 每張用角點對應求 homography $H=[\mathbf{h}_1\ \mathbf{h}_2\ \mathbf{h}_3]\sim K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]$（DLT）。
3. 每張給兩條約束（$B=K^{-\mathsf{T}}K^{-1}$）：
   - $\mathbf{h}_1^\mathsf{T}B\mathbf{h}_2=0$（$\mathbf{r}_1\perp\mathbf{r}_2$）
   - $\mathbf{h}_1^\mathsf{T}B\mathbf{h}_1=\mathbf{h}_2^\mathsf{T}B\mathbf{h}_2$（$\|\mathbf{r}_1\|=\|\mathbf{r}_2\|$）
4. 疊成 $A\mathbf{b}=0$（$\mathbf{b}$ 是 $B$ 的 6 個元素），SVD 求 $\mathbf{b}$。
5. $B^{-1}=KK^\mathsf{T}$ → Cholesky 得 $K$。
6. 外參：$s=1/\|K^{-1}\mathbf{h}_1\|$，$\mathbf{r}_1=sK^{-1}\mathbf{h}_1$，$\mathbf{r}_2=sK^{-1}\mathbf{h}_2$，$\mathbf{r}_3=\mathbf{r}_1\times\mathbf{r}_2$，$\mathbf{t}=sK^{-1}\mathbf{h}_3$。
7. 畸變參數初始 0，全部參數一起最小化重投影誤差（LM）。

**什麼時候會失敗**：

> 以下**不是逐字稿內容**，是依約束推論的：所有照片裡棋盤格都平行（只有平移、沒有轉動），每張給的約束都一樣，$A$ 退化。棋盤格要有明顯不同的傾斜角度。

### 鏡頭畸變

| 種類 | 原因 | 模型 |
|---|---|---|
| 徑向 | 鏡頭曲率（魚眼最明顯） | $(1+k_1r^2+k_2r^4+k_5r^6)\,\mathbf{x}$ |
| 切向 | 感光元件與鏡頭不平行 | $+d\mathbf{x}(k_3,k_4)$ |

- 求法：重投影誤差 $\sum_{ij}\|\mathbf{x}_{ij}-\pi(\cdot)\|^2$，LM，畸變初值 0。
- 去畸變：對輸出每個像素算 $f(\mathbf{x})$，到原圖查表。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $B=K^{-\mathsf{T}}K^{-1}=\omega$（絕對二次曲線的像） | 第 13–15 集（Lecture 6：$\omega$、從消失點校正） |
| circular points 的像在 $\omega$ 上 | 第 13–15 集 |
| 重投影誤差 + LM | 第 27–30 集（bundle adjustment） |
| 已知 $K$ 的相機 | 第 16–19 集（本質矩陣 $E$ 需要已知 $K$）；第 20–22 集（PnP 假設已校正） |
| 去畸變 | 之後所有多視角幾何都假設針孔模型（先去畸變） |

---

## 附：本集一句話總結

> **Zhang 方法把平面棋盤格放在 $Z=0$，每張照片就是一個 homography $H\sim K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]$；利用 $\mathbf{r}_1,\mathbf{r}_2$ 單位正交，每張給兩條關於 $B=K^{-\mathsf{T}}K^{-1}$ 的線性約束，三張以上就能用 SVD 解 $B$、Cholesky 得 $K$、再逐張算外參；最後把徑向、切向畸變參數（初值 0）和所有參數一起最小化重投影誤差。**

---

## ⚠️ 待確認清單

1. [▶ 24:19](https://youtu.be/77kpTQUfIBg?t=1459) 切向畸變位移 $d\mathbf{x}$ 的式子逐字稿沒唸出來；筆記寫的 $d\mathbf{x}=\left(2k_3xy+k_4(r^2+2x^2),\ k_3(r^2+2y^2)+2k_4xy\right)^\mathsf{T}$ 是依 Brown／Bouguet 常見寫法補上，未用 BRIEF 列的來源（MVG §7.4 只有徑向模型）核對，也不確定投影片上的參數編號是否完全一致。

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 5 (Part 3) 錄影逐字稿（Whisper `medium.en`，34:31）整理；對照 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §8.5 Example 8.18、§7.4。*
