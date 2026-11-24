---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 39
lecture: Neural Field Representations（實體課錄影，學期最後一堂）
date: 待補（學期最後一堂課）
video: https://youtu.be/a5hbNFRxZT4
notes: 本講內容全部來自論文（講者說共 14 篇），MVG 沒有對應章節。只依逐字稿
---

# 第 39 集 · 神經場：NeRF、體積渲染、泛化與加速、SDF、SDF 結合體積渲染、可動畫的人體 [▶ 影片](https://youtu.be/a5hbNFRxZT4)

← 上一集：[38-point-cloud-processing](38-point-cloud-processing.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：（無，最後一集）

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 39 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（2:45:46，Whisper `medium.en` 轉錄；實體課，有學生互動）
> **標記說明**：
> - `【口頭】` 講者口頭補充、投影片沒有
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 新視角合成](#1-新視角合成)
- [2. NeRF](#2-nerf)
  - [2.1 輸入輸出](#21-輸入輸出)
  - [2.2 位置編碼](#22-位置編碼)
  - [2.3 體積渲染](#23-體積渲染)
  - [2.4 離散化與由粗到細取樣](#24-離散化與由粗到細取樣)
- [3. 限制一：不能泛化](#3-限制一不能泛化)
  - [3.1 多平面影像（MPI）](#31-多平面影像mpi)
  - [3.2 MINE：平面取樣的 NeRF](#32-mine平面取樣的-nerf)
  - [3.3 IBRNet](#33-ibrnet)
- [4. 限制二：太慢](#4-限制二太慢)
  - [4.1 PlenOctree：球諧函數](#41-plenoctree球諧函數)
  - [4.2 Plenoxels：不用神經網路](#42-plenoxels不用神經網路)
  - [4.3 Instant NGP：可學的雜湊編碼](#43-instant-ngp可學的雜湊編碼)
- [5. 符號距離場（SDF）](#5-符號距離場sdf)
  - [5.1 定義與變形](#51-定義與變形)
  - [5.2 DeepSDF](#52-deepsdf)
  - [5.3 NeRF vs. SDF](#53-nerf-vs-sdf)
- [6. SDF 結合體積渲染](#6-sdf-結合體積渲染)
  - [6.1 VolSDF](#61-volsdf)
  - [6.2 NeuS](#62-neus)
- [7. 不知道相機位姿：BARF](#7-不知道相機位姿barf)
- [8. 動態人體](#8-動態人體)
  - [8.1 標準空間與線性混合蒙皮](#81-標準空間與線性混合蒙皮)
  - [8.2 Animatable NeRF](#82-animatable-nerf)
  - [8.3 SNARF：前向蒙皮與求根](#83-snarf前向蒙皮與求根)
  - [8.4 Neural Human Performer](#84-neural-human-performer)
- [9. 總結](#9-總結)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與前面集數的連結](#11-與前面集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/a5hbNFRxZT4?t=0)

1. **神經輻射場（neural radiance field，NeRF）**和**體積渲染（volume rendering）**。
2. 原始 NeRF（ECCV 2020，2020 年 6 月上 arXiv）的兩個限制：**不能泛化到新場景**、**訓練和渲染都很慢**，以及各種改進。
3. **符號距離場（SDF）**：表面更精準，但需要 3D 真值當監督。
4. 2021 年底的 **VolSDF**、**NeuS**：把 SDF 轉成體積密度 → 不需要 3D 真值和遮罩，只要多視角影像就能自我監督。
5. 用 NeRF 和 SDF 學**可動畫、可泛化的動態人體**（數位分身，用於元宇宙、AR/VR）。

【口頭】講者說本講要談 14 篇論文，多到要用兩頁投影片列；顯式表示（例如上週沒講完的部分）因為已經 110 頁投影片，沒時間講。

---

## 1. 新視角合成

[▶ 07:30](https://youtu.be/a5hbNFRxZT4?t=450)

- 回顧（第 38 集）：參數式表面是 2D → 3D 的映射；隱式表面是函數的零水平集。本講專注於**連續的隱式表示**：NeRF 和 SDF——目前電腦視覺和圖學界最熱門的兩種。

**新視角合成（novel view synthesis）** [▶ 09:38](https://youtu.be/a5hbNFRxZT4?t=578)：

- 給一張（或幾張）影像，合成**其他視角**看到的影像。
- 和生成模型（GAN、擴散模型、VAE、normalizing flow）**不同**：生成模型可以「幻想」任何東西；新視角合成必須**符合那個真實場景**——是在視角之間內插或外插，不是幻想。
- 【口頭】例子：電影《駭客任務》主角跳到半空中凍結、鏡頭環繞一圈。用一排同步相機拍，相機仍是離散的；要讓鏡頭平滑移動，就要在相機之間做新視角合成。
- 這個問題和 3D 視覺一樣古老，只是最近才發現可以用神經網路做。

---

## 2. NeRF

### 2.1 輸入輸出

[▶ 13:48](https://youtu.be/a5hbNFRxZT4?t=828)

**想法**：把整個 3D 場景**編碼在一個 MLP 的權重裡**（連 CNN 都不是）。

$$
F_\Theta:\left(\mathbf{x},\mathbf{d}\right)\mapsto\left(\mathbf{c},\sigma\right)
$$

- **輸入 5 維**：3D 位置 $\mathbf{x}\in\mathbb{R}^3$（光線上的取樣點）＋ 2D 觀看方向 $\mathbf{d}$（球座標的兩個角度）。
- **輸出 4 維**：顏色 $\mathbf{c}$（RGB）＋**體積密度** $\sigma$。

**顏色會隨視角改變** [▶ 15:30](https://youtu.be/a5hbNFRxZT4?t=930)：

- 同一點從不同角度看，反射進眼睛的光不同 → 顏色略有差異（輻射）。細節屬於電腦圖學的 **BRDF**（雙向反射分佈函數）。
- NeRF 正好是 3D 視覺和電腦圖學的結合。

**體積密度** [▶ 16:44](https://youtu.be/a5hbNFRxZT4?t=1004)：

- 光線在這點被擋住的「速率」——可以想成這點**有多被佔據**。
- 完全被佔據（不透明物體）→ 光完全被擋 → 密度最高。
- **和觀看方向無關**：你看、我看，被佔據的點都一樣被佔據。

**網路結構** [▶ 19:41](https://youtu.be/a5hbNFRxZT4?t=1181)：$\sigma$ **只由 $\mathbf{x}$** 決定；之後才加入 $\mathbf{d}$ 輸出顏色。

⚠️ 逐字稿缺字：Whisper 把 NeRF 寫成 “nerve”、“NERF”、“none”；radiance 寫成 “radians”、“gradients”、“resonance”；BRDF 寫成 “DRDF”。

### 2.2 位置編碼

[▶ 20:41](https://youtu.be/a5hbNFRxZT4?t=1241)

- 直接輸入 $(\mathbf{x},\mathbf{d})$：5 維輸入表達力不夠，網路抓不到**高頻**細節，渲染出來很模糊。
- 改成先過**位置編碼（positional encoding）**——傅立葉基底：

$$
\gamma(p)=\left(\sin\left(2^0\pi p\right),\cos\left(2^0\pi p\right),\dots,\sin\left(2^{L-1}\pi p\right),\cos\left(2^{L-1}\pi p\right)\right)
$$

- 對每一維分別編碼，串接起來 → 把低維輸入升到高維：前面是低頻、後面是高頻分量。
- 這樣訓練後能抓到高頻，渲染變得銳利。

（式子依講者說的「$2^0\pi$ 到 $2^{L-1}\pi$ 的 sin、cos」寫出。）

### 2.3 體積渲染

[▶ 22:43](https://youtu.be/a5hbNFRxZT4?t=1363)

**光線**：從相機中心 $\mathbf{o}$ 沿方向 $\mathbf{d}$：

$$
\mathbf{r}(t)=\mathbf{o}+t\mathbf{d}
$$

**像素的期望顏色**：從 $t_n$（近）積分到 $t_f$（遠）：

$$
C(\mathbf{r})=\int_{t_n}^{t_f}T(t)\,\sigma\left(\mathbf{r}(t)\right)\mathbf{c}\left(\mathbf{r}(t),\mathbf{d}\right)dt,\qquad T(t)=\exp\left(-\int_{t_n}^{t}\sigma\left(\mathbf{r}(s)\right)ds\right)
$$

三項 [▶ 24:39](https://youtu.be/a5hbNFRxZT4?t=1479)：

| 項 | 意思 |
|---|---|
| $\mathbf{c}(\mathbf{r}(t),\mathbf{d})$ | 這一點、從這個方向看的顏色（網路輸出） |
| $\sigma(\mathbf{r}(t))$ | 在這一點**撞到粒子**的機率（有多被佔據） |
| $T(t)$ | **穿透率（transmittance）**：光從 $t_n$ 走到 $t$ **都沒撞到粒子**的機率，沿路累積 |

（$T(t)$ 的式子依講者說「穿透率是體積密度的函數、沿光線累積」寫出標準形式；逐字稿沒唸出。）

- 網路輸出的小 $\mathbf{c}$ 只是**一個點**的顏色；像素看到的顏色 $C$ 是整條光線上很多點累積的。
- 【口頭】[▶ 25:40](https://youtu.be/a5hbNFRxZT4?t=1540) 例子：天上的雲看起來有層次，不是平的——雲是半透明的，眼睛收到的是光穿過雲時所有樣本顏色的累積。這就是體積渲染在做的事；只把一個點投回影像，做不出半透明物體。

**自我監督** [▶ 17:51](https://youtu.be/a5hbNFRxZT4?t=1071)：多視角影像中每個像素都有真值顏色；渲染出的 $C$ 和真值比較就能訓練——不需要 3D 真值。

### 2.4 離散化與由粗到細取樣

[▶ 28:15](https://youtu.be/a5hbNFRxZT4?t=1695)

- 電腦上不能真的積分，要沿光線**取樣**。這也是 NeRF 慢的原因：每個像素都要取很多樣本，百萬像素的影像就要上億次查詢。
- 用光線上的樣本近似積分（講者說「均勻取樣」、用類似矩形法的求積規則，推導在論文補充材料）：

$$
\hat C(\mathbf{r})=\sum_{i=1}^{N}T_i\left(1-\exp\left(-\sigma_i\delta_i\right)\right)\mathbf{c}_i,\qquad T_i=\exp\left(-\sum_{j=1}^{i-1}\sigma_j\delta_j\right)
$$

- $\mathbf{c}_i$、$\sigma_i$：第 $i$ 個樣本的網路輸出；$\delta_i$：相鄰樣本之間的距離。
- 因為顏色是按密度（多透明或多不透明）沿光線疊加的 → 渲染看起來立體、不平。

⚠️ 逐字稿缺字 [▶ 29:48](https://youtu.be/a5hbNFRxZT4?t=1788)：Whisper 寫 “Portugal rule”，應是求積規則（quadrature rule）。

> 以下**不是逐字稿內容**，是離散式的直覺：$1-\exp(-\sigma_i\delta_i)$ 是「光在第 $i$ 段被擋下」的機率（記為 $\alpha_i$）；$T_i$ 是「前面都沒被擋」的機率。兩者相乘就是「光恰好停在第 $i$ 段」的機率，當作 $\mathbf{c}_i$ 的權重。

**由粗到細（coarse-to-fine）** [▶ 51:46](https://youtu.be/a5hbNFRxZT4?t=3106)（講者在講 MINE 時補充）：

- 在空的空間取樣沒意義，應該在**表面附近**密集取樣。但一開始不知道表面在哪。
- **第一階段**：粗取樣，省計算；渲染品質不好，但讓網路大致知道表面在哪。
- **第二階段**：在表面附近細取樣 → 加快訓練、提升品質。

【口頭】[▶ 31:40](https://youtu.be/a5hbNFRxZT4?t=1900) 這麼簡單的方法卻有這麼好的結果，震撼了整個社群。講者認為近十年的浪潮是 AlexNet → GAN → 3D 點雲 → 現在的 NeRF；但要對 NeRF 做出重大改進，需要深厚的 3D 視覺基礎。

---

## 3. 限制一：不能泛化

[▶ 33:43](https://youtu.be/a5hbNFRxZT4?t=2023)

- 訓練 NeRF 等於**對一個場景過擬合**。
- 原因：輸入只有 $(\mathbf{x},\mathbf{d})$，**完全不含影像資訊**——網路只是在記憶。給它新的影像也沒用。
- **要泛化，輸入就必須包含影像（或影像特徵）。**

### 3.1 多平面影像（MPI）

[▶ 34:46](https://youtu.be/a5hbNFRxZT4?t=2086)

- **多平面影像（multiplane images，MPI）**：大約同時期的工作，受**平面掃描**（第 34 集）啟發。
- 網路吃**一張影像**，輸出 $D$ 張和參考相機**正面平行**的平面影像（$d=1,\dots,D$），每張有顏色和 **alpha**（類似密度），代表場景的一個切片。
- 新視角：用 **homography** 把每張平面投到新視角（第 34 集），再做 **alpha 合成**（加權和）。
- 要多張平面而不是一張：只用一張會很平、沒有深度感和陰影。
- **能泛化**：網路 $F$ 的輸入是影像本身。
- **限制** [▶ 41:15](https://youtu.be/a5hbNFRxZT4?t=2475)：平面是**離散**的，中間有間隙 → **量化誤差**，從其他視角渲染時品質下降。
- 【口頭】MPI 的渲染是 BRDF 渲染方程式的一種簡化（只是按 alpha 的加權和）；講者說 NeRF 和他們的論文也都是從那個方程式出發、用不同方式簡化。

### 3.2 MINE：平面取樣的 NeRF

[▶ 42:11](https://youtu.be/a5hbNFRxZT4?t=2531)（講者實驗室）

【口頭】故事：

- NeRF 一上 arXiv，講者就跟學生說這會是下一個大東西，但它不能泛化。
- 第一個想法：影像先過 CNN 得到特徵圖，把光線經過的那個像素的特徵也輸入 MLP。試了真的能泛化。
- 正要寫論文投 CVPR 時，幾天前有人把 **pixelNeRF** 放上 arXiv——完全同樣的想法，只好放棄。

**MINE 的想法**：

| | NeRF | MPI | MINE |
|---|---|---|---|
| 取樣 | 沿**光線**取樣點，連續 | 離散的平面 | 取樣**深度**（連續），每個深度輸出**整張平面** |
| 泛化 | ✗ | ✓（輸入影像） | ✓（輸入影像） |

- 網路：編碼器吃來源影像；解碼器以**逆深度**為條件，輸出那個深度上整張影像平面每個像素的顏色和**體積密度** $\sigma$（不是 alpha）。
  - 用**逆深度**：直接用深度表示不了很遠的點。
  - 逆深度也做頻率編碼，否則只有一個數值，渲染會模糊。【口頭】這和「頻譜偏差（spectral bias）」有關。
- 渲染：用 **NeRF 的渲染方程式**（考慮穿透率），不是 MPI 的簡化版。
- 名字：MI 來自 multiplane images，NE 來自 NeRF。

**損失** [▶ 54:31](https://youtu.be/a5hbNFRxZT4?t=3271)：

- 拿繞著靜態場景拍的影片，取一幀當來源，渲染到其他幀當目標。
- **重建損失**：L1 ＋ SSIM（結構相似度）。
- **深度平滑損失**：讓顏色梯度和深度梯度平滑（第 34 集的單張影像深度也用過）。
- 先做 **SfM**，用稀疏深度監督；用 SfM 的尺度把深度正規化（尺度校準損失）。

**結果** [▶ 56:25](https://youtu.be/a5hbNFRxZT4?t=3385)：比 MPI 好（連續，沒有量化間隙）。KITTI 街景很難——車子一直直線前進，視差很小，容易退化，但仍做得不錯。

⚠️ 逐字稿缺字：Whisper 把 pixelNeRF 寫成 “pixel”，MINE 寫成 “mine”、“MI”。

### 3.3 IBRNet

[▶ 57:56](https://youtu.be/a5hbNFRxZT4?t=3476)

同樣的原則：輸入用**影像特徵**。需要**已知相機位姿**（到目前為止的方法都需要；BARF 後面講）。

**步驟**：

1. 目標視角附近有多張**來源影像**，各自過 2D 網路得特徵圖。
2. 目標光線上的每個取樣點，投到各來源影像，取特徵 $\mathbf{f}_1,\dots,\mathbf{f}_n$。
3. 算這些特徵的**平均** $\boldsymbol{\mu}$ 和**變異數** $\mathbf{v}$；把每個 $\mathbf{f}_i$ 和 $(\boldsymbol{\mu},\mathbf{v})$ 串接 → 同時有**局部**（單張）和**全域**（多視角）資訊，「多視角感知」。
4. 過一個類似 PointNet 的 MLP，得新特徵 $\mathbf{f}_i'$ 和權重；**加權池化**（不是 max pool）→ 再過 MLP → **密度特徵** $\mathbf{f}_\sigma$。
5. **光線 Transformer** [▶ 1:00:08](https://youtu.be/a5hbNFRxZT4?t=3608)：同一條光線上所有樣本的 $\mathbf{f}_\sigma$ 一起送進去（位置編碼 + 多頭自注意力）→ 每個樣本的 $\sigma$。
   - 理由：同一條光線上的密度互相影響——要知道哪裡是空的、哪裡有其他物體，才能得到平滑一致的密度。
6. **顏色** [▶ 1:06:25](https://youtu.be/a5hbNFRxZT4?t=3985)：特徵和**方向差** $\Delta\mathbf{d}_i$（目標方向 vs. 第 $i$ 個來源視角方向）串接，MLP 輸出**混合權重**。這一點的顏色 = 來源影像對應像素顏色的**加權和**——**不預測顏色，而是聚合顏色**。
7. 再用 NeRF 渲染方程式沿光線累積得像素顏色。

- **優點**：能泛化；因為顏色是從附近視角聚合的，不會偏太遠 → 品質高、強健。
- **缺點** [▶ 1:08:47](https://youtu.be/a5hbNFRxZT4?t=4127)：**單一視角不行**（算不出可靠的 $\boldsymbol{\mu}$、$\mathbf{v}$）。講者實驗室測過，至少要 3 張附近的視角。

【口頭】講者實驗室在泛化的 SfM／BA 工作中用了 IBRNet；另一篇合成到真實的轉移工作（ContraNeRF）則把光線 Transformer 換成跨視角光線的對比學習。

⚠️ 逐字稿缺字：Whisper 把 IBRNet 寫成 “IDRNet”、“IVRNet”。

---

## 4. 限制二：太慢

[▶ 1:10:18](https://youtu.be/a5hbNFRxZT4?t=4218)

- 訓練和渲染都要取大量樣本。原始 NeRF 訓練時每張影像只取約 1000 個點（不渲染整張圖），仍要至少約 3 天。

**渲染為什麼慢** [▶ 1:12:00](https://youtu.be/a5hbNFRxZT4?t=4320)：

- 顏色**依賴觀看方向** → 不能**快取**：每換一個視角，所有點都要重新查網路。
- 密度和方向無關 → 可以快取。
- **想法**：把顏色和方向**解耦**，就能快取，渲染變快。

### 4.1 PlenOctree：球諧函數

[▶ 1:14:52](https://youtu.be/a5hbNFRxZT4?t=4492)

- **球諧函數（spherical harmonics）** $Y_\ell^m$：3D 球面上的「傅立葉基底」。
- 顏色寫成係數和基底的線性組合：
$$
\mathbf{c}(\mathbf{d})=\sum_{\ell,m}\mathbf{k}_\ell^m\,Y_\ell^m(\mathbf{d})
$$
  - 依賴方向的部分在 $Y_\ell^m$——有**封閉形式**，不用學。
  - 網路改成輸出係數 $\mathbf{k}$——**和方向無關** → 可以和密度一起快取。
- 換視角時只要重算 $Y_\ell^m(\mathbf{d})$，不必再跑網路。
- 只快取被佔據的地方（表面附近），存成**八元樹（octree）**，查詢也很快。
- **缺點** [▶ 1:20:40](https://youtu.be/a5hbNFRxZT4?t=4840)：**渲染**快了，**訓練**幾乎一樣慢（網路輸入輸出維度沒變，只是學的東西稍微簡單一點；講者說論文稱大約快 10%）。

（球諧展開式依講者「係數 $k$ 和球諧基底的線性組合」寫出。）

⚠️ 逐字稿缺字：Whisper 把 PlenOctree 寫成 “10.3”、“panel tree”、“Plano 3”，Plenoxels 寫成 “10.0”、“Planoxer”，octree 寫成 “top tree”。

### 4.2 Plenoxels：不用神經網路

[▶ 1:21:44](https://youtu.be/a5hbNFRxZT4?t=4904)（同一作者，CVPR 2022）

- **完全不要神經網路** → 沒有訓練時間，只有**最佳化**。
- 把空間切成規則的**體素格**，每個頂點存密度和球諧係數。
- 光線上的點：用周圍 **8 個頂點**的值做三線性內插。
- 直接最佳化這些格點值，損失 = **重建誤差** ＋ **總變差（total variation）**（相鄰格子的值不要差太多）。
- 新視角：用最佳化好的係數渲染，球諧依新方向重算。
- 【口頭】[▶ 1:24:59](https://youtu.be/a5hbNFRxZT4?t=5099) 只要約 **11 分鐘**最佳化，渲染 **15 fps**——機器人界常說 ≥13 fps 就算即時。品質甚至比 NeRF 好，因為球諧很能抓顏色變化。
- **缺點** [▶ 1:26:40](https://youtu.be/a5hbNFRxZT4?t=5200)：每個場景都要重新最佳化；沒有用到資料驅動、深度網路的優勢。

### 4.3 Instant NGP：可學的雜湊編碼

[▶ 1:26:54](https://youtu.be/a5hbNFRxZT4?t=5214)（SIGGRAPH 2022）

- 訓練從幾天降到幾分鐘、甚至幾秒；渲染也快。

**觀察** [▶ 1:28:19](https://youtu.be/a5hbNFRxZT4?t=5299)：

- 原始 NeRF 拿掉頻率編碼，高頻全失 → 編碼很重要（把 5 維升到高維）。
- 但頻率編碼本身**不學習**。→ 把學習的負擔**移到編碼上**。

**講者轉述論文的實驗**：

| 編碼 | NeRF MLP 參數 | 編碼參數 | 品質 |
|---|---|---|---|
| 頻率編碼 | 大 | 0 | 好 |
| 稠密空間格點 | 降到約 10k | 約 33.6M | 差不多 |
| 稠密多解析度格點 | 約 10k | 約 16.3M | 差不多，訓練快很多 |

**為什麼快** [▶ 1:33:42](https://youtu.be/a5hbNFRxZT4?t=5622)：

- 大 MLP 是全連接的：每次反向傳播都要更新**所有**參數。
- 空間編碼的參數**按空間排列**：一條光線只會用到、也只需更新**它經過的地方**的參數。
- 前向推論也只碰光線經過的參數。

**多解析度雜湊表** [▶ 1:35:41](https://youtu.be/a5hbNFRxZT4?t=5741)：

- 規則格點要找出光線經過的參數不夠有效率 → 用**雜湊表**（query / key）查詢和更新。
- **多解析度**：例如兩層（細、粗）。點 $\mathbf{x}$ 在每一層取包圍它的格點（2D 時 4 個）的特徵，內插；各層結果**串接**（再加一個可學的偏差）→ 送進小 MLP。
- 更新 $\mathbf{x}$ 時只動附近幾個參數，其他都不受影響 → 檢索、更新都很有效率；MLP 可以縮得很小。
- 【口頭】訓練 1 秒就能看出 gigapixel 影像的樣子，60 秒後可以放大到很細的解析度。

**缺點** [▶ 1:41:05](https://youtu.be/a5hbNFRxZT4?t=6065)【課堂討論】：

- 講者問：缺點是什麼？學生答：**不能泛化**。
- 講者問：為什麼特別難泛化？學生大意是參數和空間位置綁在一起。講者說對：要泛化 NeRF 就要讓它依賴輸入影像，但這裡所有學到的參數都**纏結**在空間位置 $\mathbf{x}$ 和方向上，很難解開。

---

## 5. 符號距離場（SDF）

### 5.1 定義與變形

[▶ 1:42:40](https://youtu.be/a5hbNFRxZT4?t=6160)

- 任一點 $\mathbf{x}$ 到表面的**最近距離**；外部為**正**、內部為**負**、表面上為 0（零水平集）。例：Stanford 兔子。
- 封閉表面才分得出內外，**開放表面會有問題**。

| 變形 | 意思 |
|---|---|
| **佔據（occupancy）** | 0 到 1，水平集取 1 或 0.5；沒有距離資訊 |
| **無號距離（unsigned）** | 只管距離，不管內外 |
| **截斷 SDF（truncated）** | 離表面很遠時距離會無限大 → 超過最大值就截斷 |

### 5.2 DeepSDF

[▶ 1:44:58](https://youtu.be/a5hbNFRxZT4?t=6298)（2019，第一個用深度網路學 SDF）

- SDF 就是一個函數 $f_\theta(\mathbf{x})=s$，用深度網路參數化，直接迴歸連續的 SDF 值；零水平集就是物體表面。
- **難處**：深度網路不擅長迴歸**無界**的值。

**三種變體** [▶ 1:46:18](https://youtu.be/a5hbNFRxZT4?t=6378)：

1. **單一形狀**：輸入 $(x,y,z)$，輸出 SDF。
   - 訓練需要**真實 SDF 值**（3D 物體當監督）。
   - 用 **clamp**（截斷在 $\delta$）避免無界。
   - 形狀資訊都在網路權重裡 → 對一個形狀過擬合，不能用在其他形狀。
2. **加上隱碼（latent code）**：輸入 $(\mathbf{x},\mathbf{z})$，形狀資訊從網路移到隱碼；換新形狀時網路固定、只最佳化隱碼。
3. **自解碼器（auto-decoder）** [▶ 1:50:02](https://youtu.be/a5hbNFRxZT4?t=6602)：沒有編碼器；訓練時**同時最佳化**網路參數 $\theta$ 和每個形狀的隱碼 $\mathbf{z}_i$，加上隱碼的正則化項（讓隱碼不要變化太大）。推論時網路固定，只最佳化新形狀的隱碼（$d$ 維，比整個網路容易得多）。

**自解碼器的好處** [▶ 1:51:36](https://youtu.be/a5hbNFRxZT4?t=6696)：

- 變體 1 要**完整**形狀才能訓練好；變體 3 的形狀資訊在隱碼裡 → 可以用**不完整**的形狀片段訓練。
- 能處理**部分觀測**，容易適應沒看過的新形狀。

> 以下**不是逐字稿內容**，是 DeepSDF 損失的常見寫法（講者口述了各項，沒唸式子）：
> $$
> \min_{\theta,\{\mathbf{z}_i\}}\sum_i\left(\sum_j\left|\mathrm{clamp}\left(f_\theta(\mathbf{z}_i,\mathbf{x}_j),\delta\right)-\mathrm{clamp}\left(s_j,\delta\right)\right|+\frac{1}{\sigma^2}\left\|\mathbf{z}_i\right\|^2\right)
> $$

### 5.3 NeRF vs. SDF

[▶ 1:53:36](https://youtu.be/a5hbNFRxZT4?t=6816)

| | NeRF | SDF |
|---|---|---|
| 渲染 | **體積渲染**，可用影像自我監督 | 只能**表面渲染**（例如沿光線做球面追蹤 sphere tracing，找到零水平集），結果是平的 |
| 監督 | 只要多視角影像 | DeepSDF 等需要 **3D 真值** |
| 幾何 | 取密度的水平集也能得到 3D，但**很雜訊**——NeRF 沒有任何東西顯式建模表面 | **顯式建模表面**，表面表示好得多 |

- SDF 沒有體積密度 → 沒有穿透率（穿透率是密度的函數）→ 不能做體積渲染。
- → 近一年的方向：**把 SDF 和輻射場結合**。

---

## 6. SDF 結合體積渲染

### 6.1 VolSDF

[▶ 1:55:24](https://youtu.be/a5hbNFRxZT4?t=6924)

**想法**：找一個函數把 SDF 值轉成體積密度，就能做體積渲染。

$$
\sigma(\mathbf{x})=\alpha\,\Psi_\beta\left(-d_\Omega(\mathbf{x})\right)
$$

- $d_\Omega(\mathbf{x})$：SDF（內負外正）。
- $\Psi_\beta$：**Laplace 分佈的累積分佈函數（CDF）**，$\alpha$、$\beta$ 是可學參數。論文有很長的證明。

**為什麼合理** [▶ 1:57:33](https://youtu.be/a5hbNFRxZT4?t=7053)：

- 離物體很遠（外部）：$d>0$ 很大，$-d$ 很負 → 在 CDF 的左尾 → 密度很小。
- 靠近零水平集：密度逐漸上升。
- 在物體內部：$-d>0$ → 密度更高（光完全被擋）。
- 整個函數**可微** → 可以放進網路學 $\alpha$、$\beta$。

- 代入 NeRF 的渲染方程式：穿透率 $T$、不透明度 $O=1-T$（類似 CDF）、對它微分得機率密度 → 渲染方程式裡的 $\sigma$ 全換成 SDF 的函數 → 可以用影像**體積渲染**來監督 SDF，**不需要 3D 真值**。

**Eikonal 正則化** [▶ 2:01:20](https://youtu.be/a5hbNFRxZT4?t=7280)（講者說所有 SDF 論文都用）：

$$
\left\|\nabla d_\Omega(\mathbf{x})\right\|=1
$$

- 往表面每走一單位，SDF 就減少一 → 梯度大小必須是 1。
- 反向傳播本來就會算梯度 → 直接加這個約束 → 表面平滑。
- NeRF 的密度沒有水平集的概念，沒辦法這樣正則化 → 所以雜訊多。

**之前的方法** [▶ 2:02:45](https://youtu.be/a5hbNFRxZT4?t=7365)：

- **IDR**：直接從 SDF 表面渲染，不按密度累積顏色 → 要知道表面在哪 → 需要 2D **遮罩**（所以 IDR 結果沒有背景）。需要精確遮罩，不實用。
- 同期有三篇：VolSDF、NeuS、**UNISURF**。VolSDF 的做法：轉成體積渲染，像 NeRF 一樣訓練，同時可以正則化 SDF。

⚠️ 逐字稿缺字：Whisper 把 NeuS 寫成 “news”、“UNICEF”（講者說 NeuS 時有時口誤成 UNISURF），VolSDF 寫成 “volume SDF”、“SVM”。

### 6.2 NeuS

[▶ 2:04:24](https://youtu.be/a5hbNFRxZT4?t=7464)

- 渲染方程式是顏色的加權和，權重 $w(t)=T(t)\sigma(t)$（就是 NeRF 的方程式）。
- NeuS 說要把 SDF 放進去，權重必須滿足**兩個條件**：
  1. **無偏（unbiased）**：權重的峰值必須落在 SDF $=0$ 的表面 $t^*$ 上。
  2. **遮擋感知（occlusion-aware）** [▶ 2:05:47](https://youtu.be/a5hbNFRxZT4?t=7547)：兩個深度 $t_0<t_1$ 的 SDF 值相同時，$w(t_0)>w(t_1)$——光先經過 $t_0$，後面的已經被擋住，不該累積那麼多。
- **直接沿用 NeRF 的形式**（例如用 logistic 密度這種單峰分佈當 $\sigma$）[▶ 2:07:38](https://youtu.be/a5hbNFRxZT4?t=7658)：權重峰值和表面之間有**偏移** → 渲染的顏色不是來自表面。
- NeuS 改用另一個量 $\rho$ 取代 $\sigma$ → 權重峰值落在表面上；兩個條件都滿足（論文有證明，講者用兩個表面的一維例子說明）。

【口頭】[▶ 2:09:27](https://youtu.be/a5hbNFRxZT4?t=7767) 講者仔細看後發現：NeuS 的 $\rho$ 不再是單峰，而是 **S 形曲線**——和 VolSDF 選的 Laplace CDF **本質上是同一件事**，兩篇其實提出幾乎一樣的東西。

> 以下**不是逐字稿內容**，是 NeuS 中 $\rho$ 的形式（講者沒唸）：$\Phi_s$ 是 sigmoid，$f$ 是 SDF，
> $$
> \rho(t)=\max\left(\frac{-\frac{d}{dt}\Phi_s\left(f\left(\mathbf{r}(t)\right)\right)}{\Phi_s\left(f\left(\mathbf{r}(t)\right)\right)},\ 0\right)
> $$
> 光線從外往內穿過表面時，$\Phi_s(f)$ 從 1 降到 0，$\rho$ 從 0 迅速上升——正是 S 形。

---

## 7. 不知道相機位姿：BARF

[▶ 2:12:17](https://youtu.be/a5hbNFRxZT4?t=7937)

NeRF 需要**已知相機位姿**。**BARF**（bundle-adjusting NeRF）假設位姿**不完美**，把 bundle adjustment 和 NeRF 一起做；但仍需要某種初值。

**從 2D 影像對齊說起** [▶ 2:12:58](https://youtu.be/a5hbNFRxZT4?t=7978)：

$$
\min_{\mathbf{p}}\sum_{\mathbf{x}}\left\|I_2\left(W(\mathbf{x};\mathbf{p})\right)-I_1(\mathbf{x})\right\|^2
$$

- $W$ 用位姿 $\mathbf{p}$ 把一張圖的 patch 扭到另一張；最小化**光度一致性誤差**。
- Gauss–Newton（第 29 集）：$A=J^\mathsf{T}J$，$\Delta\mathbf{p}=-(J^\mathsf{T}J)^{-1}J^\mathsf{T}\mathbf{e}$；Jacobian 用數值微分（加一個小 $\delta$ 再相減、相除）。

**把一張影像換成 NeRF** [▶ 2:14:26](https://youtu.be/a5hbNFRxZT4?t=8066)：

- 一邊改成用網路渲染出來的影像，和真實影像比 → 同時最佳化**網路參數**和**所有視角的位姿**。
- Jacobian 不再用數值微分，而是**反向傳播**。
- 光線上的點 $\mathbf{x}$ 和方向 $\mathbf{d}$ 都依賴相機位姿 → 寫成位姿的函數一起最佳化。
- 不是最小化重投影誤差，而是最小化渲染影像和真實影像的**光度一致性**。

**問題：位置編碼的高頻主導 Jacobian** [▶ 2:18:32](https://youtu.be/a5hbNFRxZT4?t=8312)：

- 對位置編碼微分，第 $k$ 個頻率的導數會乘上 $2^k\pi$ → **高頻分量主導 Jacobian** → 一開始就被高頻帶走，低頻沒機會被最小化。
- **解法**：每個頻率帶乘上一個權重，由 $0$ 到 $L$ 的控制參數決定：訓練初期把高頻壓掉，只用低頻；之後逐漸加回高頻（**由粗到細**）。

**BARF 的缺點** [▶ 2:20:43](https://youtu.be/a5hbNFRxZT4?t=8443)：

- 不能泛化（輸入仍是 $\mathbf{x}$ 和方向）。
- 更新的是相對全域座標系的**絕對位姿** → 需要相當好的初值。

【口頭】講者實驗室的做法：用 IBRNet 取代 NeRF（可泛化）；並受全域 SfM（第 28 集）啟發，改成更新**相對位姿**——相對位姿有界、網路比較好學 → **不需要初值**，隨機初始化也行。

---

## 8. 動態人體

[▶ 2:22:07](https://youtu.be/a5hbNFRxZT4?t=8527)

- 若能建模並操控人體，就有**數位分身**：掃描一個人、建 NeRF 或 SDF 模型，再讓它可動畫 → 放進元宇宙控制。
- **問題**：NeRF 需要靜態場景和已知相機位姿。人在動（例如跳舞），手上的點 $t=1$ 在這、$t=2$ 在那——相機不動也不知道對應關係。

### 8.1 標準空間與線性混合蒙皮

[▶ 2:23:53](https://youtu.be/a5hbNFRxZT4?t=8633)

- **觀測空間（observation space）**：任意姿勢。
- **標準空間（canonical space）**：**T 字姿勢**。
- 觀測空間光線上的點 → 映射到標準空間 → 在標準空間取對應的特徵 → 用 NeRF 得顏色和密度 → 放回觀測空間渲染。

**線性混合蒙皮（linear blend skinning，LBS）** [▶ 2:25:34](https://youtu.be/a5hbNFRxZT4?t=8734)：

$$
\mathbf{x}_o=\sum_{k=1}^{K}w_k\left(\mathbf{x}_c\right)G_k\,\mathbf{x}_c\qquad(\text{標準}\to\text{觀測})
$$

$$
\mathbf{x}_c=\left(\sum_{k=1}^{K}w_k\left(\mathbf{x}_o\right)G_k\right)^{-1}\mathbf{x}_o\qquad(\text{觀測}\to\text{標準，近似})
$$

- $G_k$：第 $k$ 根骨頭（關節之間）的轉換；$w_k$：**混合權重**，本身是點的函數。

（式子依講者口述的「混合權重的線性組合；反方向就把整個東西求逆」寫出。）

⚠️ 逐字稿缺字 [▶ 2:26:22](https://youtu.be/a5hbNFRxZT4?t=8782)：講者說投影片上反方向的式子「有個打字錯誤」，權重的引數和 $\mathbf{x}'$ 的位置應對調；上式依這個修正寫出。

### 8.2 Animatable NeRF

[▶ 2:26:41](https://youtu.be/a5hbNFRxZT4?t=8801)

- $G_k$ 用 **SMPL** 模型（參數化人體模型）從影像估出來，固定。
- SMPL 是**幾乎沒穿衣服**的人體；衣服是相對它的偏差 → 網路預測混合權重的**偏差** $\Delta w$，加在 SMPL 的權重上。
- 標準空間中用 NeRF 學顏色和密度。
- 再學一個從標準空間回到觀測空間的權重；兩個方向的權重應該一致 → 當正則化。
- **可動畫**：給不同的姿勢 → 從標準空間取特徵、映到想要的姿勢 → **新視角**和**新姿勢**都能渲染（仍在積極研究，品質還不完美）。

**兩個限制** [▶ 2:31:37](https://youtu.be/a5hbNFRxZT4?t=9097)：

1. **新姿勢要最佳化**：混合權重是觀測空間 $\mathbf{x}$ 的函數 → 換姿勢要對新姿勢（由 SMPL 算出）重新最佳化隱碼。
2. **不能泛化到新的人**：網路輸出一個標準空間，綁定這個人的身分。

### 8.3 SNARF：前向蒙皮與求根

[▶ 2:32:33](https://youtu.be/a5hbNFRxZT4?t=9153)

**解決限制 1**：讓混合權重是**標準空間** $\mathbf{x}_c$ 的函數（和輸入姿勢無關）→ 能泛化到不同姿勢。這其實是**更正確**的 LBS。

- 代價：要從觀測點 $\mathbf{x}_o$ 找標準點 $\mathbf{x}_c^*$，但權重 $w(\mathbf{x}_c^*)$ 依賴輸出本身 → **沒有封閉解**，要**求根**：
$$
\sum_kw_k\left(\mathbf{x}_c^*\right)G_k\,\mathbf{x}_c^*-\mathbf{x}_o=\mathbf{0}
$$
- 用 **Newton–Raphson** 或論文提出的**擬 Newton 法**，迭代很多次；可以同時解多個對應點（多個初值）。
- **訓練** [▶ 2:37:18](https://youtu.be/a5hbNFRxZT4?t=9438)：對權重網路參數微分時需要 $\partial\mathbf{x}_c^*/\partial\sigma_w$，而 $\mathbf{x}_c^*$ 是求根的結果 → 要用**隱函數微分（implicit differentiation）**；每次反向傳播都要先求根找到操作點。
- **為什麼更正確** [▶ 2:39:22](https://youtu.be/a5hbNFRxZT4?t=9562)：不求逆時，$\mathbf{x}$ 出現在等號兩邊，要知道 $\mathbf{x}$ 才能算權重。Animatable NeRF 直接假設整個東西可逆、把權重改成觀測點的函數，是很大的近似。
- 很慢，但結果較好，**極端姿勢**也能正確輸出。
- SNARF 只做 **SDF**（沒有新視角合成），可以用不同姿勢參數推論表面。

⚠️ 逐字稿缺字：Whisper 把 SNARF 寫成 “snuff”、root finding 寫成 “root mining”。

### 8.4 Neural Human Performer

[▶ 2:40:56](https://youtu.be/a5hbNFRxZT4?t=9656)

**解決限制 2**（泛化到新的人）：

- 不用 T 字姿勢（它綁定身分）。
- 多視角、多時間步：每個時間步都可估 SMPL，知道頂點索引 → 知道不同時間的頂點對應。
- 直接從**影像**取特徵（不存在 T 字姿勢上）。
- 兩個 Transformer [▶ 2:42:33](https://youtu.be/a5hbNFRxZT4?t=9753)：
  1. **時間 Transformer**：融合同一點在不同時間的特徵。
  2. **多視角 Transformer**：和各視角重投影取得的特徵做交叉注意力 → 最終特徵。
- MLP 從最終特徵輸出密度和顏色。
- 講者說是目前最好的結果之一，但仍需要很多視角。（NeurIPS，講者不確定是去年還是前年。）

⚠️ 逐字稿缺字：Whisper 把 NeurIPS 寫成 “Nurex”。

---

## 9. 總結

[▶ 2:44:55](https://youtu.be/a5hbNFRxZT4?t=9895)

1. 神經輻射場與體積渲染。
2. NeRF 的問題：泛化、效率，以及緩解的方法。
3. 符號距離場，和 NeRF 比較。
4. 把兩者結合：用體積渲染自我監督，同時保持 SDF 的表面精度。
5. 用 NeRF 和 SDF 做可動畫、可泛化的動態人體。

講者以此結束整個學期。

---

## 10. 一頁速查表

### NeRF

| 項目 | 公式 | 關鍵一步 |
|---|---|---|
| 網路 | $F_\Theta(\mathbf{x},\mathbf{d})=(\mathbf{c},\sigma)$；$\sigma$ 只看 $\mathbf{x}$ | 密度與視角無關 |
| 位置編碼 | $\gamma(p)=(\sin2^k\pi p,\cos2^k\pi p)_{k=0}^{L-1}$ | 升維抓高頻 |
| 渲染 | $C=\int T\sigma\mathbf{c}\,dt$，$T=e^{-\int\sigma}$ | 雲的層次感 |
| 離散 | $\hat C=\sum_iT_i(1-e^{-\sigma_i\delta_i})\mathbf{c}_i$，$T_i=e^{-\sum_{j<i}\sigma_j\delta_j}$ | 停在第 $i$ 段的機率 |
| 取樣 | 粗 → 細（表面附近密集） | — |

### 改進

| 問題 | 方法 | 關鍵想法 |
|---|---|---|
| 泛化 | MPI | 輸入影像 → 離散平面 + alpha 合成（量化誤差） |
| | MINE | 連續逆深度 → 整張平面的 $(\mathbf{c},\sigma)$，NeRF 渲染 |
| | IBRNet | 多視角特徵 $(\mathbf{f}_i,\boldsymbol{\mu},\mathbf{v})$、光線 Transformer 出 $\sigma$、聚合來源顏色；需 ≥3 視角 |
| 速度 | PlenOctree | $\mathbf{c}=\sum\mathbf{k}Y(\mathbf{d})$，係數可快取；八元樹 |
| | Plenoxels | 無網路，體素格球諧 + 三線性內插，重建 + TV；11 分鐘、15 fps |
| | Instant NGP | 多解析度雜湊編碼（可學），MLP 縮小；只更新光線經過的參數；不能泛化 |

### SDF

| 項目 | 內容 |
|---|---|
| 定義 | 到表面最近距離，外正內負，零水平集 = 表面 |
| DeepSDF | 單一形狀／隱碼／自解碼器（同時最佳化 $\theta$、$\mathbf{z}_i$；推論只最佳化 $\mathbf{z}$）；需 3D 真值；clamp |
| VolSDF | $\sigma=\alpha\Psi_\beta(-d)$，Laplace CDF |
| NeuS | 權重無偏、遮擋感知；$\rho$ 為 S 形 |
| 正則化 | Eikonal $\|\nabla d\|=1$ |

### 位姿與人體

| 方法 | 關鍵想法 |
|---|---|
| BARF | 渲染 vs. 真實的光度一致性，Jacobian 用反向傳播；頻率帶由粗到細 |
| LBS | $\mathbf{x}_o=\sum_kw_k(\mathbf{x}_c)G_k\mathbf{x}_c$ |
| Animatable NeRF | SMPL 權重 + 網路學 $\Delta w$；逆向近似；新姿勢要最佳化、綁定身分 |
| SNARF | 權重在標準空間 → 求根（Newton／擬 Newton）+ 隱函數微分；只做 SDF |
| Neural Human Performer | 無 T 字姿勢；時間 + 多視角 Transformer |

---

## 11. 與前面集數的連結

（最後一集，改列用到的前面觀念。）

| 本集觀念 | 前面在哪裡 |
|---|---|
| MPI 的 homography 投影 | 第 34 集（平面掃描） |
| BARF 的 Gauss–Newton、$J^\mathsf{T}J$ | 第 29 集（bundle adjustment） |
| 相對位姿比絕對位姿好學 | 第 28 集（全域 SfM、旋轉平均） |
| SfM 稀疏深度監督（MINE） | 第 27–30 集 |
| 隱式表示、八元樹 | 第 38 集 |
| 光度一致性損失（L1、SSIM、平滑） | 第 32、34 集 |

---

## 附：本集一句話總結

> **NeRF 用一個 MLP 把 $(\mathbf{x},\mathbf{d})$ 映到顏色和體積密度，靠位置編碼抓高頻、靠沿光線累積 $T\sigma\mathbf{c}$ 的體積渲染用影像自我監督；它不能泛化（輸入不含影像，MPI、MINE、IBRNet 改用影像特徵）、又慢（PlenOctree 用球諧讓顏色可快取、Plenoxels 乾脆不用網路、Instant NGP 把學習移到可學的多解析度雜湊編碼）；SDF 的表面更準卻需要 3D 真值，VolSDF、NeuS 把 SDF 轉成密度後就能體積渲染、加上 Eikonal 正則化；BARF 讓位姿和 NeRF 一起最佳化，而動態人體則靠標準空間與線性混合蒙皮（SNARF 用求根做正確的前向蒙皮）。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Neural Field Representations 錄影逐字稿（Whisper `medium.en`，2:45:46）整理；MVG 無對應章節，論文本身未查閱。*
