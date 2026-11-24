---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 13
lecture: Lecture 6 (Part 1) – Single view metrology
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/D6Pm5id_LK4
notes: MVG §8.1–8.4（書頁 195–208，PDF 頁 213–226）
---

# 第 13 集 · Lecture 6 (Part 1)：相機對平面／線／二次曲線的作用、相機中心的重要性 [▶ 影片](https://youtu.be/D6Pm5id_LK4)

← 上一集：[12-camera-models-calibration-part3](12-camera-models-calibration-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[14-single-view-metrology-part2](14-single-view-metrology-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 13 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（54:24，Whisper `medium.en` 轉錄）＋ MVG §8.1–8.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 相機對平面的作用：homography](#1-相機對平面的作用homography)
- [2. 相機對線的作用](#2-相機對線的作用)
  - [2.1 前向投影](#21-前向投影)
  - [2.2 反向投影：π = Pᵀl](#22-反向投影π--pᵀl)
- [3. 相機對二次曲線的作用：反投影成錐](#3-相機對二次曲線的作用反投影成錐)
- [4. 光滑曲面的輪廓](#4-光滑曲面的輪廓)
- [5. 二次曲面投影成二次曲線：C* = PQ*Pᵀ](#5-二次曲面投影成二次曲線c--pqpᵀ)
- [6. 相機中心的重要性](#6-相機中心的重要性)
  - [6.1 相機中心固定 → homography](#61-相機中心固定--homography)
  - [6.2 只改焦距：放大](#62-只改焦距放大)
  - [6.3 純旋轉：共軛旋轉](#63-純旋轉共軛旋轉)
  - [6.4 移動相機中心：運動視差](#64-移動相機中心運動視差)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/D6Pm5id_LK4?t=0)

Lecture 6 的目標（三集合起來）：

| 目標 | 本集？ | MVG |
|---|---|---|
| 相機投影對平面、線、二次曲線、二次曲面的作用 | ✅ | §8.1–8.3 |
| 固定相機中心、增加焦距、純旋轉對影像的影響 | ✅ | §8.4 |
| 用絕對二次曲線的像校正相機內參 | 第 14 集 | §8.5 |
| 消失點、消失線，用它們求場景和相機的幾何性質 | 第 14–15 集 | §8.6–8.8 |

講者說內容主要取自 MVG 第 8 章。

**回顧**：上一講看了 $P$（$3\times4$）對**點**的作用：前向投影（3D → 2D）、反向投影（2D 點 → 光線）。今天看 $P$ 對**平面、線、二次曲線、二次曲面**的前向和反向投影。

---

## 1. 相機對平面的作用：homography

[▶ 02:05](https://youtu.be/D6Pm5id_LK4?t=125)

- 3D 平面 $\boldsymbol{\pi}$。和上一講校正時一樣，把世界座標的 $XY$ 平面放在 $\boldsymbol{\pi}$ 上 → 平面上的點 $\mathbf{X}_\pi=(X,Y,0,1)^\mathsf{T}$。
- 投影：
$$
\mathbf{x}=P\mathbf{X}_\pi=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_3\ \mathbf{p}_4]\begin{pmatrix}X\\Y\\0\\1\end{pmatrix}=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_4]\begin{pmatrix}X\\Y\\1\end{pmatrix}
$$
- $Z=0$ 把第三行 $\mathbf{p}_3$ 消掉。
- 兩邊都是 3 維齊次向量 → 平面和影像之間是一個 $3\times3$ **homography**：
$$
H=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_4]
$$
- 第 08 集：這個 homography 可以用 4 對對應點求出來。

【課本補充】MVG Example 8.1：已校正的相機 $P=K[R\mid\mathbf{t}]$，$Z=0$ 平面到影像的 homography 是 $H=K[\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{t}]$（就是第 12 集 Zhang 方法用的那個）。

---

## 2. 相機對線的作用

### 2.1 前向投影

[▶ 04:45](https://youtu.be/D6Pm5id_LK4?t=285)

**幾何**：3D 線 $L$ 和相機中心一起張成一個平面 $\boldsymbol{\pi}$；$\boldsymbol{\pi}$ 和影像平面的交線就是 $L$ 的像 $\mathbf{l}$。

**代數** [▶ 05:42](https://youtu.be/D6Pm5id_LK4?t=342)：

- $L$ 上兩點 $\mathbf{A}$、$\mathbf{B}$，$L$ 上所有點是 $\mathbf{X}(\mu)=\mathbf{A}+\mu\mathbf{B}$（第 04 集：兩點的張成）。
- 每一點投影：
$$
\mathbf{x}(\mu)=P\mathbf{X}(\mu)=P\mathbf{A}+\mu P\mathbf{B}=\mathbf{a}+\mu\mathbf{b}
$$
- $\mathbf{a}=P\mathbf{A}$、$\mathbf{b}=P\mathbf{B}$ 是兩個端點的像。所以 3D 線的像是**通過 $\mathbf{a}$、$\mathbf{b}$ 的 2D 線**。

### 2.2 反向投影：π = Pᵀl

[▶ 09:12](https://youtu.be/D6Pm5id_LK4?t=552)

- $P$ 是 $3\times4$，沒有反矩陣 → 不能從 $\mathbf{l}$ 唯一恢復 3D 線。
- **幾何**：影像上的線 $\mathbf{l}$ 反投影成一個**平面** $\boldsymbol{\pi}$。這個平面上的**任何一條 3D 線**都會投影到同一條 $\mathbf{l}$。

> **Result 8.2（MVG）** 經 $P$ 映到影像線 $\mathbf{l}$ 的空間點的集合，是平面 $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$。

**證明** [▶ 11:16](https://youtu.be/D6Pm5id_LK4?t=676)：

1. 像點 $\mathbf{x}$ 在 $\mathbf{l}$ 上 ⟺ $\mathbf{x}^\mathsf{T}\mathbf{l}=0$（第 01 集）。
2. 3D 點 $\mathbf{X}$ 投影成 $\mathbf{x}=P\mathbf{X}$。代入：
$$
(P\mathbf{X})^\mathsf{T}\mathbf{l}=\mathbf{X}^\mathsf{T}(P^\mathsf{T}\mathbf{l})=0
$$
3. 這正是「$\mathbf{X}$ 在平面 $P^\mathsf{T}\mathbf{l}$ 上」（第 04 集）。所以 $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$。∎

講者說「$P$ 最大 rank 是 3」，接著說「如果是無窮遠相機、有限相機……rank 會是 2」[▶ 09:46](https://youtu.be/D6Pm5id_LK4?t=586)。

> 以下**不是逐字稿內容**：這段口述前後不一。依第 10–11 集：有限相機和仿射相機的 $P$（$3\times4$）rank 都是 3；仿射相機 rank 2 的是左邊 $3\times3$ 的 $M$。$P$ 不可逆的原因是它不是方陣。

---

## 3. 相機對二次曲線的作用：反投影成錐

[▶ 13:06](https://youtu.be/D6Pm5id_LK4?t=786)

- 影像上的二次曲線 $C$，曲線上每一點反投影成一條光線。所有光線合起來是一個**錐（cone）**。
- 第 04 集：錐是**退化的二次曲面**（$4\times4$ 矩陣不滿秩）。

> **Result 8.6（MVG）** 在相機 $P$ 下，二次曲線 $C$ 反投影成錐
> $$Q_{\text{co}}=P^\mathsf{T}CP$$

**證明** [▶ 15:13](https://youtu.be/D6Pm5id_LK4?t=913)：

1. 像點 $\mathbf{x}$ 在 $C$ 上 ⟺ $\mathbf{x}^\mathsf{T}C\mathbf{x}=0$。
2. 代 $\mathbf{x}=P\mathbf{X}$：
$$
(P\mathbf{X})^\mathsf{T}C(P\mathbf{X})=\mathbf{X}^\mathsf{T}(P^\mathsf{T}CP)\mathbf{X}=0
$$
3. 這是「$\mathbf{X}$ 在二次曲面 $P^\mathsf{T}CP$ 上」。幾何上它就是那個錐。∎

**相機中心是錐的頂點，在零空間裡** [▶ 18:27](https://youtu.be/D6Pm5id_LK4?t=1107)：

$$
Q_{\text{co}}\mathbf{C}=P^\mathsf{T}C\underbrace{P\mathbf{C}}_{\mathbf{0}}=\mathbf{0}
$$

**例子**（MVG Example 8.7）[▶ 19:26](https://youtu.be/D6Pm5id_LK4?t=1166)：標準相機 $P=K[I\mid\mathbf{0}]$（世界座標系和相機座標系對齊）：

$$
Q_{\text{co}}=P^\mathsf{T}CP=\begin{pmatrix}K^\mathsf{T}\\\mathbf{0}^\mathsf{T}\end{pmatrix}C\begin{pmatrix}K & \mathbf{0}\end{pmatrix}=\begin{pmatrix}K^\mathsf{T}CK & \mathbf{0}\\\mathbf{0}^\mathsf{T} & 0\end{pmatrix}
$$

- 最後一列、最後一行全是 0 → 不滿秩 → **退化二次曲面（錐）**。零向量是 $(0,0,0,1)^\mathsf{T}$——相機中心在原點。

---

## 4. 光滑曲面的輪廓

[▶ 20:56](https://youtu.be/D6Pm5id_LK4?t=1256)

任意光滑曲面 $S$ 透過中心投影成像：

- 從相機中心出發、**和曲面相切**的光線，碰到曲面的那些點組成一條曲線，叫**輪廓生成線（contour generator）** $\Gamma$。
- 這些光線和影像平面的交線，叫**視輪廓（apparent contour）** $\gamma$，也叫**外形（outline）**或**側影（profile）**。
- 前向投影：$\Gamma$（3D）→ $\gamma$（2D）。反向投影：$\gamma$ 上每點連回相機中心的光線都和 $S$ 相切。

**仿射相機** [▶ 23:35](https://youtu.be/D6Pm5id_LK4?t=1415)：沒有投影中心，所有光線平行；反投影的光線和曲面相切、彼此平行。輪廓生成線、視輪廓照樣可以定義。

**誰依賴什麼** [▶ 24:13](https://youtu.be/D6Pm5id_LK4?t=1453)：

| | 依賴 | 不依賴 |
|---|---|---|
| 輪廓生成線 $\Gamma$ | 相機中心和曲面的相對位置 | 影像平面 |
| 視輪廓 $\gamma$ | 相機中心、曲面，**還有影像平面的位置** | — |

- $\Gamma$ 只由「從相機中心出發、和曲面相切的光線」決定，跟影像平面放哪裡沒關係。
- $\gamma$ 是這些光線和影像平面的交線，影像平面一動，交線就變。

---

## 5. 二次曲面投影成二次曲線：C* = PQ*Pᵀ

[▶ 26:25](https://youtu.be/D6Pm5id_LK4?t=1585)

> **Result 8.9（MVG）** 在相機 $P$ 下，二次曲面 $Q$ 的外形是二次曲線 $C$，用對偶表示：
> $$C^*=PQ^*P^\mathsf{T}$$

**為什麼用對偶（線）二次曲線**：外形 $C$ 的每條切線反投影成一個平面，而這個平面正是二次曲面 $Q$ 的**切平面**。

**證明** [▶ 27:12](https://youtu.be/D6Pm5id_LK4?t=1632)：

1. 和外形 $C$ 相切的線滿足 $\mathbf{l}^\mathsf{T}C^*\mathbf{l}=0$（第 02 集）。
2. 線 $\mathbf{l}$ 反投影成平面 $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$（第 2.2 節），這平面和 $Q$ 相切，所以滿足 $\boldsymbol{\pi}^\mathsf{T}Q^*\boldsymbol{\pi}=0$（第 04 集）。
3. 代入：
$$
(P^\mathsf{T}\mathbf{l})^\mathsf{T}Q^*(P^\mathsf{T}\mathbf{l})=\mathbf{l}^\mathsf{T}(PQ^*P^\mathsf{T})\mathbf{l}=0
$$
4. 和第 1 步比較：$C^*=PQ^*P^\mathsf{T}$。∎

---

## 6. 相機中心的重要性

[▶ 28:24](https://youtu.be/D6Pm5id_LK4?t=1704)

**直覺**：

- 物體上每一點和相機中心連成光線（光走直線），影像是這束光線和影像平面的交點。
- 相機中心 $C$ 和影像平面的方向就是相機的**外參**（$R$、$\mathbf{t}$）；影像平面離相機中心的距離是**焦距**。
- 三件事都會改變影像：
  1. **移動相機中心**（方向不變）：光線方向變了 → 影像變。
  2. **相機中心不動、轉影像平面**：光線和平面的交點變了 → 影像變。
  3. **改焦距**（$f_1\to f_2$）：影像平面前後移 → 影像變。
- 問題：這些變化在數學上長什麼樣？

### 6.1 相機中心固定 → homography

[▶ 31:17](https://youtu.be/D6Pm5id_LK4?t=1877)

- 相機中心不動時，同一個 3D 點在兩張影像上的像，都在**同一條光線**上 → 兩張影像由一個平面射影變換（homography）連起來。
- 所以兩張影像**射影等價**，有相同的射影性質。相機可以看成一個**射影成像裝置**，用來量測「以相機中心為頂點的光線錐」的射影性質。

**推導** [▶ 32:28](https://youtu.be/D6Pm5id_LK4?t=1948)：兩張影像 $I$、$I'$，相機中心相同：

$$
P=KR[I\mid-\tilde{\mathbf{C}}],\qquad P'=K'R'[I\mid-\tilde{\mathbf{C}}]
$$

1. $KR$ 是可逆的 $3\times3$（$R$ 正交、$K$ 可逆）。從第一式：$[I\mid-\tilde{\mathbf{C}}]=(KR)^{-1}P$。
2. 代入第二式：$P'=K'R'(KR)^{-1}P$。
3. 對任一 3D 點：
$$
\mathbf{x}'=P'\mathbf{X}=K'R'(KR)^{-1}\underbrace{P\mathbf{X}}_{\mathbf{x}}=K'R'(KR)^{-1}\mathbf{x}
$$
4. 兩邊都是 3 維齊次向量，在同一個 $\mathbb{P}^2$：
$$
\boxed{\ \mathbf{x}'=H\mathbf{x},\qquad H=K'R'(KR)^{-1}\ }
$$

【口頭】[▶ 36:07](https://youtu.be/D6Pm5id_LK4?t=2167) 講者提醒投影片上少了兩個 prime（應為 $\mathbf{x}'=H\mathbf{x}$、$H=K'R'\cdots$）。

### 6.2 只改焦距：放大

[▶ 36:22](https://youtu.be/D6Pm5id_LK4?t=2182)

- 只改焦距 $f$（假設沒有斜切、$f_x=f_y=f$），其他都不變。
- **幾何**：影像平面沿主軸前後移。兩點 $\mathbf{x}_1,\mathbf{x}_2$ 的距離隨焦距變大而變大 → **影像放大（magnification）**。

**推導** [▶ 38:46](https://youtu.be/D6Pm5id_LK4?t=2326)：

$$
\mathbf{x}=K[I\mid\mathbf{0}]\mathbf{X},\qquad \mathbf{x}'=K'[I\mid\mathbf{0}]\mathbf{X}
$$

插入 $K^{-1}K=I$：

$$
\mathbf{x}'=K'K^{-1}\underbrace{K[I\mid\mathbf{0}]\mathbf{X}}_{\mathbf{x}}=K'K^{-1}\mathbf{x}
\quad\Longrightarrow\quad H=K'K^{-1}
$$

**焦距是唯一的差別時** [▶ 42:00](https://youtu.be/D6Pm5id_LK4?t=2520)：放大倍率 $k=f'/f$，主點 $\tilde{\mathbf{x}}_0$ 不變：

$$
H=K'K^{-1}=\begin{pmatrix}kI & (1-k)\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T} & 1\end{pmatrix}
$$

（矩陣依 MVG §8.4.1 寫出；逐字稿只說「算出來是這個形式」。）

> 以下**不是逐字稿內容**，是驗證：$K=\begin{pmatrix}fI&\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$、$K'=\begin{pmatrix}kfI&\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$，$K^{-1}=\begin{pmatrix}\frac1fI&-\frac1f\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$。相乘：左上 $kI$，右上 $-k\tilde{\mathbf{x}}_0+\tilde{\mathbf{x}}_0=(1-k)\tilde{\mathbf{x}}_0$。

**幾何意義**：$H$ 把點 $\tilde{\mathbf{x}}$ 送到 $k\tilde{\mathbf{x}}+(1-k)\tilde{\mathbf{x}}_0$——沿著從主點放射出去的直線往外推。

**把 $K'$ 當主角** [▶ 43:09](https://youtu.be/D6Pm5id_LK4?t=2589)：

$$
K'=HK=K\begin{pmatrix}k&&\\&k&\\&&1\end{pmatrix}
$$

講者的推導：把 $K$ 寫成 $\begin{pmatrix}A&\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$（$A$ 是焦距的對角部分），乘出來
$$
HK=\begin{pmatrix}kI&(1-k)\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}\begin{pmatrix}A&\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}=\begin{pmatrix}kA&k\tilde{\mathbf{x}}_0+(1-k)\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}=\begin{pmatrix}kA&\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}
$$
右上的主點項 $k\tilde{\mathbf{x}}_0-k\tilde{\mathbf{x}}_0+\tilde{\mathbf{x}}_0=\tilde{\mathbf{x}}_0$ 消回原樣，只有焦距部分乘了 $k$。

- 結論：**變焦 $k$ 倍 = $K$ 右乘 $\mathrm{diag}(k,k,1)$**。

### 6.3 純旋轉：共軛旋轉

[▶ 44:43](https://youtu.be/D6Pm5id_LK4?t=2683)

只有旋轉改變，其他都不變：

$$
\mathbf{x}=K[I\mid\mathbf{0}]\mathbf{X},\qquad \mathbf{x}'=K[R\mid\mathbf{0}]\mathbf{X}
$$

插入 $K^{-1}K$：

$$
\mathbf{x}'=KRK^{-1}\underbrace{K[I\mid\mathbf{0}]\mathbf{X}}_{\mathbf{x}}=KRK^{-1}\mathbf{x}
\quad\Longrightarrow\quad H=KRK^{-1}
$$

> 以下**不是逐字稿內容**，是中間一步：$K[R\mid\mathbf{0}]=KR[I\mid\mathbf{0}]=KRK^{-1}\cdot K[I\mid\mathbf{0}]$。

**共軛旋轉（conjugate rotation）** [▶ 47:37](https://youtu.be/D6Pm5id_LK4?t=2857)：$H=KRK^{-1}$ 這種形式在文獻上叫共軛旋轉。

- $H$ 和 $R$ **相似**（差一個 $K$ 的共軛），所以**特徵值相同**（差一個尺度 $\mu$）：
$$
\{\mu,\ \mu e^{i\theta},\ \mu e^{-i\theta}\}
$$
- **用途** [▶ 48:27](https://youtu.be/D6Pm5id_LK4?t=2907)：兩張純旋轉的照片，
  1. 找 4 對對應點，算出 $H$。
  2. 求 $H$ 的特徵值，除掉共同尺度 → $1,e^{i\theta},e^{-i\theta}$。
  3. 從複數特徵值的相位讀出**旋轉角 $\theta$**。

【課本補充】MVG Example 8.12：把 $H$ 縮放成 $\det H=1$ 時 $\mu=1$。同樣地，旋轉軸方向也可以從 $H$ 的實特徵向量求出（$H$ 的實特徵向量是旋轉軸的消失點）。

> 以下**不是逐字稿內容**，是「特徵值相同」的一行理由：若 $R\mathbf{v}=\lambda\mathbf{v}$，則 $H(K\mathbf{v})=KRK^{-1}K\mathbf{v}=\lambda K\mathbf{v}$。旋轉矩陣的特徵值是 $1,e^{\pm i\theta}$（第 07 集的例子）。

### 6.4 移動相機中心：運動視差

[▶ 50:02](https://youtu.be/D6Pm5id_LK4?t=3002)

講者說這部分下一講（fundamental matrix、essential matrix、極幾何）細講，這裡只講概念。

- **前三種情況**（改 $K$、改 $R$、或都改，但相機中心不動）：兩張影像只由 homography 連起來——所有關係都只在影像點之間（$\mathbb{P}^2$），**得不到任何 3D 結構的資訊**。
- **移動相機中心**（例如 $K$、$R$ 都不變，只把 $C$ 移到 $C'$）：
  - 同一個 3D 點 $\mathbf{X}$ 在兩張影像上的像 $\mathbf{x}$、$\mathbf{x}'$，是兩條光線（$C$–$\mathbf{x}$、$C'$–$\mathbf{x}'$）交於 $\mathbf{X}$ 決定的。
  - **不再是 homography**：$\mathbf{x}$ 和 $\mathbf{x}'$ 的關係除了依賴兩個相機中心，還依賴**3D 點的深度**。
  - 例：把 $\mathbf{X}$ 沿著第一張圖的光線往遠處移，它在第一張圖上的像不變，但在第二張圖上的像**會變**。這叫**運動視差（motion parallax）**。
- 結論：移動相機中心後，兩張影像的對應點同時帶有**3D 結構**和**相機運動**的資訊。給一組對應點，求相機的旋轉、平移並恢復 3D 結構——就是之後課程的 **structure from motion（SfM）**。

【課本補充】MVG Fig. 8.6：純旋轉時，在第一張圖重疊的不同深度的點（杯緣和貓身），在第二張圖還是重疊——沒有運動視差；加上平移後，它們就分開了。

（本集到 54:17 結束。）

---

## 7. 一頁速查表

### P 對各種物件的作用

| 物件 | 前向 | 反向 | 關鍵一步 |
|---|---|---|---|
| 點 | $\mathbf{x}=P\mathbf{X}$ | 光線 | — |
| 平面（$Z=0$） | $H=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_4]$ | $H^{-1}$ | $Z=0$ 消掉 $\mathbf{p}_3$ |
| 線 | $\mathbf{a}+\mu\mathbf{b}$，$\mathbf{a}=P\mathbf{A}$ | 平面 $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$ | $(P\mathbf{X})^\mathsf{T}\mathbf{l}=\mathbf{X}^\mathsf{T}P^\mathsf{T}\mathbf{l}$ |
| 二次曲線 | — | 錐 $Q_{\text{co}}=P^\mathsf{T}CP$，$Q_{\text{co}}\mathbf{C}=0$ | $(P\mathbf{X})^\mathsf{T}C(P\mathbf{X})$ |
| 二次曲面 | 外形 $C^*=PQ^*P^\mathsf{T}$ | — | 切線反投影成切平面 |
| 光滑曲面 | 視輪廓 $\gamma$ | 輪廓生成線 $\Gamma$ | $\Gamma$ 不依賴影像平面 |

### 相機中心固定時的 homography

| 改變 | $H$ |
|---|---|
| 一般（$K,R$ 都變） | $K'R'(KR)^{-1}$ |
| 只改焦距 $k=f'/f$ | $K'K^{-1}=\begin{pmatrix}kI&(1-k)\tilde{\mathbf{x}}_0\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$；$K'=K\,\mathrm{diag}(k,k,1)$ |
| 純旋轉 | $KRK^{-1}$（共軛旋轉），特徵值 $\{\mu,\mu e^{\pm i\theta}\}$ |
| 移動相機中心 | **不是** homography，依賴深度（運動視差） |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$ | 第 14 集（消失線反投影成場景平面的法向）；第 16–19 集（極線反投影成極平面） |
| $Q_{\text{co}}=P^\mathsf{T}CP$、$C^*=PQ^*P^\mathsf{T}$ | 第 14 集（$\Omega_\infty$ 的像 $\omega$、$Q_\infty^*$ 的像 $\omega^*=KK^\mathsf{T}$） |
| $H=KRK^{-1}$ | 第 14 集（$\omega$ 在純旋轉下不變）；全景拼接 |
| 運動視差、移動相機中心 | 第 16–19 集（極幾何、$F$、$E$）；第 27–30 集（SfM） |

---

## 附：本集一句話總結

> **相機把平面映成 homography、把影像線反投影成平面 $P^\mathsf{T}\mathbf{l}$、把影像二次曲線反投影成以相機中心為頂點的錐 $P^\mathsf{T}CP$、把二次曲面投影成 $C^*=PQ^*P^\mathsf{T}$；只要相機中心不動，不管怎麼變焦（$K'K^{-1}$）或旋轉（$KRK^{-1}$），兩張影像都只差一個 homography、看不出深度——唯有移動相機中心才會出現運動視差，帶來 3D 資訊。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 6 (Part 1) 錄影逐字稿（Whisper `medium.en`，54:24）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §8.1–8.4 整理。*
