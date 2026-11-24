---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 34
lecture: Lecture 11 (Part 4) – Two-view and multi-view stereo
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/YgOC9DjHyJs
notes: 平面誘導的 homography 對照 MVG §13.1（書頁 325–327，PDF 頁 343–345）；SGM、單張影像深度、平面掃描本身 MVG 沒有
---

# 第 34 集 · Lecture 11 (Part 4)：半全域匹配（SGM）、單張影像深度、平面掃描多視角 stereo [▶ 影片](https://youtu.be/YgOC9DjHyJs)

← 上一集：[33-stereo-part3](33-stereo-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[35-generalized-cameras-part1](35-generalized-cameras-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 34 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（31:01，Whisper `medium.en` 轉錄）＋ MVG §13.1（只對照 homography）
> **標記說明**：
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 半全域匹配（SGM）](#1-半全域匹配sgm)
  - [1.1 想法：多個方向的掃描線](#11-想法多個方向的掃描線)
  - [1.2 累積代價](#12-累積代價)
  - [1.3 取視差、次像素精度](#13-取視差次像素精度)
- [2. 單張影像的深度（深度學習）](#2-單張影像的深度深度學習)
- [3. 多視角 stereo：平面掃描](#3-多視角-stereo平面掃描)
  - [3.1 問題](#31-問題)
  - [3.2 輸入與相機](#32-輸入與相機)
  - [3.3 一族深度平面](#33-一族深度平面)
  - [3.4 平面誘導的 homography](#34-平面誘導的-homography)
  - [3.5 光度一致性代價、選平面](#35-光度一致性代價選平面)
- [4. Lecture 11 總結](#4-lecture-11-總結)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

| 方法 | 鄰居範圍 | 問題 |
|---|---|---|
| Block matching（第 33 集） | 單一像素 | 破碎 |
| 掃描線最佳化（第 33 集） | 一條掃描線 | 條紋 |
| 全域匹配（第 33 集） | 整張圖 | NP-complete |
| **半全域匹配**（本集） | 幾個方向的掃描線 | 介於中間、可解、結果不錯 |

再介紹用深度學習從**單張影像**估深度，最後用**平面掃描**做多視角 stereo。

---

## 1. 半全域匹配（SGM）

### 1.1 想法：多個方向的掃描線

[▶ 00:32](https://youtu.be/YgOC9DjHyJs?t=32)

- **半全域匹配（semi-global matching，SGM）**：沿**多個方向**做掃描線最佳化。
- 對參考影像一個像素，平滑約束不只考慮同一條掃描線上的鄰居，而是好幾個方向（例如 8 個或 16 個）上的鄰居。

### 1.2 累積代價

[▶ 01:30](https://youtu.be/YgOC9DjHyJs?t=90)

**總累積代價**：把每個方向 $\mathbf{r}$ 的代價加起來：

$$
S(p,d)=\sum_{\mathbf{r}}L_\mathbf{r}(p,d)
$$

**兩趟（two passes）**（典型的 8 方向實作）：

- **前向**：從影像一端掃，處理 4 個方向。
- **反向**：從另一端掃，處理另外 4 個方向。
- 每個像素有兩組 $S$ 值，加起來 = 8 個方向的總累積代價。

**每個方向的代價 $L_\mathbf{r}$** [▶ 03:28](https://youtu.be/YgOC9DjHyJs?t=208)：和第 33 集的掃描線動態規劃一樣，只是「前一個像素」換成沿方向 $\mathbf{r}$ 的前一個像素 $p-\mathbf{r}$：

- 一元項 $C(p,d)$：仍然是匹配代價（沿校正後的掃描線比 patch）。
- 平滑項：考慮 $p-\mathbf{r}$。水平方向就是同一條掃描線上的鄰居；對角方向就是斜對角的鄰居。

⚠️ 待確認 [▶ 03:36](https://youtu.be/YgOC9DjHyJs?t=216)：$L_\mathbf{r}$ 的式子講者只說「就是掃描線最佳化的動態規劃」，沒唸出投影片上的式子。

> 以下**不是逐字稿內容**，是 SGM 常見的寫法（和第 33 集的遞迴式同一個結構，平滑項換成 $0/P_1/P_2$）：
> $$
> L_\mathbf{r}(p,d)=C(p,d)+\min\left\{L_\mathbf{r}(p-\mathbf{r},d),\ L_\mathbf{r}(p-\mathbf{r},d\pm1)+P_1,\ \min_iL_\mathbf{r}(p-\mathbf{r},i)+P_2\right\}-\min_kL_\mathbf{r}(p-\mathbf{r},k)
> $$
> 最後減掉的 $\min_kL_\mathbf{r}(p-\mathbf{r},k)$ 對所有 $d$ 都一樣，不改變誰最小，只是防止累積值沿路徑一直變大。

### 1.3 取視差、次像素精度

[▶ 05:34](https://youtu.be/YgOC9DjHyJs?t=334)

- 每個像素 $p$ 得到一張一維表：每個視差的累積代價 $S(p,d)$。
- 取最小的：
$$
d_p=\arg\min_dS(p,d)
$$
- **次像素精度** [▶ 06:11](https://youtu.be/YgOC9DjHyJs?t=371)：視差是整數。用相鄰視差的代價**擬合曲線**或內插，得到連續值。講者舉的例子是雙線性內插（bilinear interpolation）。

> 以下**不是逐字稿內容**，是補充：沿視差這一個維度，常見作法是用 $d_p-1$、$d_p$、$d_p+1$ 三個代價擬合一條拋物線，取它的頂點當次像素視差。

**結果** [▶ 06:58](https://youtu.be/YgOC9DjHyJs?t=418)：和 $3\times3$ block matching（破碎）比，16 個方向的 SGM 平滑很多，又**沒有失去細節**，接近真值。

⚠️ 逐字稿缺字：講者總結時說「8 different directions or 60 different directions」，依前面的例子應是 **16** 個方向；“five grain detail” 應是 fine-grained detail。

---

## 2. 單張影像的深度（深度學習）

[▶ 07:38](https://youtu.be/YgOC9DjHyJs?t=458)

- 幾何上，深度只能從**兩張有重疊視野**的影像得到（第 16–19 集）。
- 但可以**從資料學習**：學一個函數 $f$，輸入**單張**影像 $I$，輸出每個像素的視差 $\hat D=f(I)$。$f$ 用**卷積神經網路（CNN）**。

**用左右一致性訓練** [▶ 09:01](https://youtu.be/YgOC9DjHyJs?t=541)（講者說是 CVPR 2017 的論文）：

- 訓練時有很多對**校準過的 stereo 影像** $I_L$、$I_R$。
- **同一個**網路分別吃 $I_L$、$I_R$，各自輸出 $D_L$、$D_R$。
- 已知 $D_L=x-x'$ → 由 $x$ 算出 $x'$ → 把影像**按視差平移像素**，就能從一張圖**重建**另一張圖。
- 重建出來的右圖應該等於真的右圖，反之亦然 → 當訓練損失。

**損失函數** [▶ 12:27](https://youtu.be/YgOC9DjHyJs?t=747)：

| 損失 | 意思 |
|---|---|
| **外觀匹配損失** | 原圖和重建圖盡量一樣。用 **L1**（對離群值強健）加上 **SSIM**（類似前面的相關性匹配代價） |
| **視差平滑損失** | 相鄰像素視差盡量相近：讓視差在 $x$、$y$ 方向的梯度小；同時考慮影像本身的梯度 |
| **左右視差一致性損失** | 兩個視差圖應該互相一致 |

⚠️ 待確認 [▶ 14:21](https://youtu.be/YgOC9DjHyJs?t=861)：講者對左右一致性損失的說法是「訓練時有校準的 stereo，可以用前面的方法算出視差圖，拿來和重建的視差比較」，這和上面「兩個預測的視差圖互相一致」不太一樣，以投影片為準。

> 以下**不是逐字稿內容**，是說明「同時考慮影像梯度」的常見作法：平滑項寫成 $|\partial_xd|\,e^{-|\partial_xI|}+|\partial_yd|\,e^{-|\partial_yI|}$——影像邊緣（$|\partial I|$ 大）處權重變小，允許深度在物體邊界跳動。

**結果** [▶ 14:48](https://youtu.be/YgOC9DjHyJs?t=888)：只用一張影像就得到相當接近真值的深度圖。幾何上 stereo 需要兩張圖，所以這很令人印象深刻。

---

## 3. 多視角 stereo：平面掃描

### 3.1 問題

[▶ 15:40](https://youtu.be/YgOC9DjHyJs?t=940)

- 多視角 stereo 是大規模 3D 重建的**最後一步**（第 27 集的流程）。
- **給定**：多張影像，以及 SfM 求出的相機位姿。
- **求**：**每張影像**的稠密深度圖 → 合起來得到稠密 3D 模型。
- 對比 SfM：SfM 只求相機位姿、三角化**稀疏**的對應點；這裡要每張圖**每個像素**的深度。
- 方法：**平面掃描（plane sweeping）**。

### 3.2 輸入與相機

[▶ 17:21](https://youtu.be/YgOC9DjHyJs?t=1041)

- $M$ 個 3D 平面（用來測試深度，「掃」過去的就是它們）。
- $N+1$ 張影像，相機位置來自 SfM；都已**去除徑向畸變**。
- 參考相機放在原點：$P_{\text{ref}}=K\left[I\mid\mathbf{0}\right]$。
- 第 $k$ 台相機（$k=1,\dots,N$）：
$$
P_k=K_k\left[R_k^\mathsf{T}\mid-R_k^\mathsf{T}\mathbf{C}_k\right]
$$
  $R_k$、$\mathbf{C}_k$ 是第 $k$ 台相機的旋轉和光心（相對參考相機）。

⚠️ 逐字稿缺字 [▶ 18:17](https://youtu.be/YgOC9DjHyJs?t=1097)：Whisper 寫「k multiplied by r and minus r transpose ck」。依「$R_k$ 是相機旋轉、$\mathbf{C}_k$ 是光心」的意思，旋轉部分應寫 $R_k^\mathsf{T}$，才和 $-R_k^\mathsf{T}\mathbf{C}_k$ 一致（相機座標 $=R_k^\mathsf{T}(\mathbf{X}-\mathbf{C}_k)$）。

### 3.3 一族深度平面

[▶ 19:04](https://youtu.be/YgOC9DjHyJs?t=1144)

在參考座標系中定義 $M$ 個平面：

$$
\boldsymbol{\Pi}_m=\begin{pmatrix}\mathbf{n}_m^\mathsf{T}&-d_m\end{pmatrix},\qquad m=1,\dots,M
$$

- 平面上的點滿足 $\mathbf{n}_m^\mathsf{T}\mathbf{X}=d_m$。
- $\mathbf{n}_m$：單位法向量；$d_m$：到原點的距離。

**正面平行（fronto-parallel）平面掃描** [▶ 19:49](https://youtu.be/YgOC9DjHyJs?t=1189)：

- $\mathbf{n}=(0,0,1)^\mathsf{T}$：平面垂直於參考相機的 $z$ 軸。
- $d_m$ 在 $[d_{\text{near}},d_{\text{far}}]$ 之間取一組離散值：第一個平面在 $d_{\text{near}}$，最後一個在 $d_{\text{far}}$。

### 3.4 平面誘導的 homography

[▶ 20:48](https://youtu.be/YgOC9DjHyJs?t=1248)

**想法**：

- 假設參考影像某個 patch 落在平面 $\boldsymbol{\Pi}_m$ 上（深度假設）。
- 平面 → 可以用 homography 把參考影像的 patch 轉到第 $k$ 張影像（第 8 集：平面場景的兩張影像差一個 homography）。
- 已知 $R_k$、$\mathbf{C}_k$、$\mathbf{n}_m$、$d_m$ → homography 確定：

$$
H_{\boldsymbol{\Pi}_m,P_k}=K_k\left(R_k^\mathsf{T}-\frac{R_k^\mathsf{T}\mathbf{C}_k\mathbf{n}_m^\mathsf{T}}{d_m}\right)K^{-1}
$$

> 以下**不是逐字稿內容**，是這個 homography 的推導（逐字稿只說「這個式子來自 homography 那一講」）：
> 1. 參考影像的點 $\mathbf{x}$ 反投影成光線 $\mathbf{X}=\lambda K^{-1}\mathbf{x}$。
> 2. 平面上的點滿足 $\mathbf{n}_m^\mathsf{T}\mathbf{X}=d_m$ → $\dfrac{\mathbf{n}_m^\mathsf{T}\mathbf{X}}{d_m}=1$。
> 3. 投到第 $k$ 張：$\mathbf{x}_k=K_kR_k^\mathsf{T}(\mathbf{X}-\mathbf{C}_k)$。把 $\mathbf{C}_k$ 乘上 $1=\mathbf{n}_m^\mathsf{T}\mathbf{X}/d_m$：
> $$
> \mathbf{x}_k=K_kR_k^\mathsf{T}\left(\mathbf{X}-\frac{\mathbf{C}_k\mathbf{n}_m^\mathsf{T}\mathbf{X}}{d_m}\right)=K_k\left(R_k^\mathsf{T}-\frac{R_k^\mathsf{T}\mathbf{C}_k\mathbf{n}_m^\mathsf{T}}{d_m}\right)\mathbf{X}
> $$
> 4. 代 $\mathbf{X}=\lambda K^{-1}\mathbf{x}$，$\lambda$ 是齊次座標的倍數，可以拿掉 → 上式。
>
> 這和 MVG §13.1 的形式 $H=K'\left(R-\mathbf{t}\mathbf{n}^\mathsf{T}/d\right)K^{-1}$（平面 $\mathbf{n}^\mathsf{T}\mathbf{X}+d=0$）一致：這裡 $R=R_k^\mathsf{T}$、$\mathbf{t}=-R_k^\mathsf{T}\mathbf{C}_k$、$d=-d_m$。

⚠️ 待確認：投影片上的正負號（$R_k^\mathsf{T}+\cdots$ 或 $R_k^\mathsf{T}-\cdots$）沒唸出來，取決於平面方程式的符號慣例；筆記依 $\mathbf{n}_m^\mathsf{T}\mathbf{X}=d_m$ 推導。

**轉移座標** [▶ 24:02](https://youtu.be/YgOC9DjHyJs?t=1442)：

$$
\begin{pmatrix}\tilde x\\\tilde y\\\tilde w\end{pmatrix}=H_{\boldsymbol{\Pi}_m,P_k}\begin{pmatrix}x\\y\\1\end{pmatrix},\qquad\text{影像座標 }\left(\frac{\tilde x}{\tilde w},\frac{\tilde y}{\tilde w}\right)
$$

- 對每個平面、每張影像都做一次：同一個參考 patch，在不同深度假設下被送到其他影像的不同位置。

### 3.5 光度一致性代價、選平面

[▶ 24:39](https://youtu.be/YgOC9DjHyJs?t=1479)

對參考像素 $(x,y)$ 和平面 $\boldsymbol{\Pi}_m$，把所有影像的絕對差加起來（也可以用前面講過的其他匹配代價）：

$$
C(x,y,\boldsymbol{\Pi}_m)=\sum_{k=1}^N\sum_{(i,j)\in W}\left|I_{\text{ref}}(x-i,y-j)-\beta_k\,I_k(\tilde x_k-i,\tilde y_k-j)\right|
$$

- $W$：視窗；$(\tilde x_k,\tilde y_k)$：$(x,y)$ 經 $H_{\boldsymbol{\Pi}_m,P_k}$ 轉到第 $k$ 張的位置。
- $\beta_k$：參考影像和第 $k$ 張之間的**增益比**，補償光照差異。

（式子依講者口述的各項意義寫出。）

**選平面** [▶ 27:06](https://youtu.be/YgOC9DjHyJs?t=1626)：

1. 對每個平面算 $C$（例如 $d_1=0.15$ 對應一個值……）。
2. 取 $C$ **最小**的平面——照這個平面轉移後，在所有影像都配得最好 → 它就是這個像素的正確深度。
3. 對參考影像每個像素都做 → 參考影像的深度圖。
4. 輪流讓**每張影像當參考**，用其他所有影像 → 每張影像都有稠密深度圖。

**深度** [▶ 28:09](https://youtu.be/YgOC9DjHyJs?t=1689)：正面平行的情況，選到平面 $\boldsymbol{\Pi}_m$ 的像素，深度就是 $d_m$（講者說用投影片上的式子直接算）。有了深度 → 3D 點 → 所有影像每個像素的**稠密點雲**。

> 以下**不是逐字稿內容**，是一般法向量時的深度：由 §3.4 的步驟 1、2，$\lambda\,\mathbf{n}_m^\mathsf{T}K^{-1}\mathbf{x}=d_m$。若 $K^{-1}\mathbf{x}$ 的第三個分量是 1，$\lambda$ 就是深度：
> $$
> Z=\frac{d_m}{\mathbf{n}_m^\mathsf{T}K^{-1}\mathbf{x}}
> $$
> 正面平行時 $\mathbf{n}_m=(0,0,1)^\mathsf{T}$，分母 $=1$，$Z=d_m$。

**結果** [▶ 28:40](https://youtu.be/YgOC9DjHyJs?t=1720)：影像越多，深度圖越好。2 張時仍有破碎；20 張時已經很平滑，接近真值。

---

## 4. Lecture 11 總結

[▶ 29:17](https://youtu.be/YgOC9DjHyJs?t=1757)

1. stereo 校正、沿掃描線找對應得到視差（第 31–32 集）。
2. 用相似三角形從視差算深度（第 33 集）。
3. Block matching → 破碎；掃描線最佳化 → 條紋；全域最佳化最好但 NP-complete（第 33 集）。
4. 折衷：**半全域匹配**，在多個方向（8 或 16 個）做動態規劃（本集）。
5. 多視角 stereo：**平面掃描**（本集）。

---

## 5. 一頁速查表

### SGM

| 項目 | 公式 | 關鍵一步 |
|---|---|---|
| 總代價 | $S(p,d)=\sum_\mathbf{r}L_\mathbf{r}(p,d)$ | 8（或 16）個方向，前向 4 + 反向 4 |
| 方向代價 | $L_\mathbf{r}$：沿 $\mathbf{r}$ 的掃描線動態規劃，前一個像素 $p-\mathbf{r}$ | 和第 33 集同一個 DP |
| 視差 | $d_p=\arg\min_dS(p,d)$；次像素用內插／擬合 | — |

### 單張影像深度

- CNN $\hat D=f(I)$；訓練用 stereo 對：按視差平移重建另一張圖。
- 損失：外觀（L1 + SSIM）、視差平滑、左右一致性。

### 平面掃描

| 項目 | 公式 |
|---|---|
| 相機 | $P_{\text{ref}}=K[I\mid\mathbf{0}]$、$P_k=K_k[R_k^\mathsf{T}\mid-R_k^\mathsf{T}\mathbf{C}_k]$ |
| 平面 | $\boldsymbol{\Pi}_m=(\mathbf{n}_m^\mathsf{T},-d_m)$；正面平行 $\mathbf{n}=(0,0,1)^\mathsf{T}$，$d_m\in[d_{\text{near}},d_{\text{far}}]$ |
| Homography | $H=K_k\left(R_k^\mathsf{T}-R_k^\mathsf{T}\mathbf{C}_k\mathbf{n}_m^\mathsf{T}/d_m\right)K^{-1}$（關鍵一步：$\mathbf{C}_k$ 乘上 $1=\mathbf{n}_m^\mathsf{T}\mathbf{X}/d_m$） |
| 代價 | $C(x,y,\boldsymbol{\Pi}_m)=\sum_k\sum_W\left|I_{\text{ref}}-\beta_kI_k(H\cdot)\right|$ |
| 深度 | 取 $C$ 最小的平面；正面平行 $Z=d_m$；一般 $Z=d_m/(\mathbf{n}_m^\mathsf{T}K^{-1}\mathbf{x})$ |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 稠密點雲（多視角 stereo 的輸出） | 第 38 集（點雲處理） |
| 用影像重建當訓練訊號 | 第 39 集（神經場：用渲染影像和真實影像比較來訓練） |
| 平面誘導 homography | 第 35–37 集（廣義相機）會用到相同的投影幾何 |

---

## 附：本集一句話總結

> **半全域匹配在 8 或 16 個方向上各做一次掃描線動態規劃、把代價加總後取最小視差，避開了條紋又不像全域匹配那樣 NP-complete；深度學習可以用 stereo 對的「平移重建另一張圖」當訓練訊號，學出從單張影像估深度；多視角 stereo 用平面掃描——在參考相機前放一族深度平面，每個平面誘導一個把參考 patch 送到其他影像的 homography，取所有影像光度一致性代價最小的平面當那個像素的深度。**

---

## ⚠️ 待確認清單

1. [▶ 03:36](https://youtu.be/YgOC9DjHyJs?t=216) SGM 每個方向代價 $L_\mathbf{r}$ 的投影片式子沒唸出；筆記列的是常見寫法，標為推論。
2. [▶ 14:21](https://youtu.be/YgOC9DjHyJs?t=861) 左右視差一致性損失的確切定義：講者的說法（和用傳統 stereo 算的視差比）和「兩個預測視差互相一致」不同。
3. [▶ 22:49](https://youtu.be/YgOC9DjHyJs?t=1369) 平面誘導 homography 中 $R_k^\mathsf{T}\mathbf{C}_k\mathbf{n}_m^\mathsf{T}/d_m$ 前面的正負號（投影片沒唸；筆記依 $\mathbf{n}_m^\mathsf{T}\mathbf{X}=d_m$ 推導為負號）。

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 11 (Part 4) 錄影逐字稿（Whisper `medium.en`，31:01）整理；homography 部分對照 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §13.1。*
