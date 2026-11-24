---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 04
lecture: Lecture 2 (Part 2) – Rigid body motion and 3D projective geometry
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/wpqTPTQcNAM
notes: MVG §3.1–3.2.4、§3.4（書頁 65–78，PDF 頁 83–96）
---

# 第 04 集 · Lecture 2 (Part 2)：3D 射影幾何——點、平面、線、二次曲面 [▶ 影片](https://youtu.be/wpqTPTQcNAM)

← 上一集：[03-rigid-motion-3d-projective-part1](03-rigid-motion-3d-projective-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[05-circular-points-absolute-conic-part1](05-circular-points-absolute-conic-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 04 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（44:26，Whisper `medium.en` 轉錄）＋ MVG §3.1–3.2.4、§3.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 從 2D 推廣到 3D：哪裡一樣、哪裡不一樣](#1-從-2d-推廣到-3d哪裡一樣哪裡不一樣)
- [2. P³ 的點與射影變換](#2-p³-的點與射影變換)
- [3. 平面](#3-平面)
  - [3.1 平面的齊次表示、點面對偶](#31-平面的齊次表示點面對偶)
  - [3.2 三點決定一個平面](#32-三點決定一個平面)
  - [3.3 三個平面決定一個點](#33-三個平面決定一個點)
  - [3.4 平面上的點：X = Mx](#34-平面上的點x--mx)
- [4. 線（一）：零空間與張成表示](#4-線一零空間與張成表示)
- [5. 線（二）：Plücker 座標](#5-線二plücker-座標)
- [6. 二次曲面與對偶二次曲面](#6-二次曲面與對偶二次曲面)
- [7. 3D 變換階層](#7-3d-變換階層)
- [8. Lecture 2 總結](#8-lecture-2-總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

接續第 03 集的剛體運動，本集講 3D 射影幾何：

| 主題 | MVG |
|---|---|
| $\mathbb{P}^3$ 的點、射影變換 | §3.1 |
| 平面、點面對偶 | §3.2.1 |
| 線：零空間／張成表示、Plücker 座標 | §3.2.2 |
| 二次曲面、對偶二次曲面 | §3.2.3–3.2.4 |
| 3D 變換階層 | §3.4 |

---

## 1. 從 2D 推廣到 3D：哪裡一樣、哪裡不一樣

[▶ 00:00](https://youtu.be/wpqTPTQcNAM?t=0)

- 很多 $\mathbb{P}^3$ 的性質是 $\mathbb{P}^2$ 的**直接推廣**。例如 2D 點 $(x_1,x_2,1)$，3D 點就多加一維：$(x_1,x_2,x_3,1)$。
- 但**多一維會冒出新性質**：
  - 在射影平面上，**兩條線一定相交**（平行的話交在無窮遠）。
  - 在 3D 裡，兩條線**不一定相交**，即使它們不平行。例如一條線在另一條線的下方（$z$ 方向錯開），永遠碰不到。這種線叫**歪斜線（skew lines）**。

---

## 2. P³ 的點與射影變換

[▶ 01:46](https://youtu.be/wpqTPTQcNAM?t=106)

**點**：4 維齊次向量

$$
\mathbf{X}=(X_1,X_2,X_3,X_4)^\mathsf{T}\ \longleftrightarrow\ \left(\frac{X_1}{X_4},\frac{X_2}{X_4},\frac{X_3}{X_4}\right)^\mathsf{T}
$$

- 縮放不重要。換回非齊次座標：前三個除以 $X_4$。
- $X_4=0$：**無窮遠點**，和 2D 一樣。

**射影變換** [▶ 03:07](https://youtu.be/wpqTPTQcNAM?t=187)：

$$
\mathbf{X}'=H\mathbf{X},\qquad H\ \text{是非奇異}\ 4\times4\ \text{矩陣}
$$

- $H$ 是齊次的，**15 個自由度**（16 個元素少 1 個縮放）。
- 和 2D 一樣，它是**直射變換（collineation）**：共線的點變換後還是共線。
- 保持**關聯關係**（例如點在線上、線和平面的交點）和**接觸階數**。

---

## 3. 平面

### 3.1 平面的齊次表示、點面對偶

[▶ 05:06](https://youtu.be/wpqTPTQcNAM?t=306)

- 平面在 2D 射影空間裡不是獨立的物件（所有東西都在一個平面上）；在 3D 裡平面是一種物件。
- 平面方程式：
$$
\pi_1X+\pi_2Y+\pi_3Z+\pi_4=0
$$
- 齊次化：代 $X\to X_1/X_4$、$Y\to X_2/X_4$、$Z\to X_3/X_4$，乘 $X_4$：
$$
\pi_1X_1+\pi_2X_2+\pi_3X_3+\pi_4X_4=0\quad\Longleftrightarrow\quad \boldsymbol{\pi}^\mathsf{T}\mathbf{X}=0
$$
- **點在平面上 ⟺ $\boldsymbol{\pi}^\mathsf{T}\mathbf{X}=0$**。這和 2D 的「點在線上 ⟺ $\mathbf{l}^\mathsf{T}\mathbf{x}=0$」完全類比。
- 所以在 3D，**點和平面是對偶的**（2D 是點和線對偶）。

**自由度**：只有 $\pi_1:\pi_2:\pi_3:\pi_4$ 三個獨立比值 → **3 個自由度**。

**幾何意義** [▶ 07:33](https://youtu.be/wpqTPTQcNAM?t=453)：

- 前三個分量 $(\pi_1,\pi_2,\pi_3)$ 是**平面的法向量** $\mathbf{n}$。
- 非齊次寫法（$X_4=1$）：
$$
\mathbf{n}^\mathsf{T}\tilde{\mathbf{X}}+d=0,\qquad \mathbf{n}=(\pi_1,\pi_2,\pi_3)^\mathsf{T},\ \tilde{\mathbf{X}}=(X,Y,Z)^\mathsf{T},\ d=\pi_4
$$
- 原點到平面的距離是 $d/\|\mathbf{n}\|$。

**變換** [▶ 08:51](https://youtu.be/wpqTPTQcNAM?t=531)：點 $\mathbf{X}'=H\mathbf{X}$ 時，

$$
\boldsymbol{\pi}'=H^{-\mathsf{T}}\boldsymbol{\pi}
$$

講者留作練習，提示用 $\boldsymbol{\pi}^\mathsf{T}\mathbf{X}=0$。

> 以下**不是逐字稿內容**，是依講者提示推論的關鍵一步（和第 02 集 2D 線的推導一樣）：$\boldsymbol{\pi}'^\mathsf{T}\mathbf{X}'=\boldsymbol{\pi}^\mathsf{T}H^{-1}H\mathbf{X}=\boldsymbol{\pi}^\mathsf{T}\mathbf{X}=0$。

**幾何關係一覽** [▶ 09:30](https://youtu.be/wpqTPTQcNAM?t=570)：

- **三個不共線的點**唯一決定一個平面。
- **一條線和一個不在線上的點**決定一個平面。
- **兩個不同的平面**交於唯一一條線（類比 2D 的兩線交於一點）。
- **三個不同的平面**交於唯一一點。

### 3.2 三點決定一個平面

[▶ 10:22](https://youtu.be/wpqTPTQcNAM?t=622)

三個點 $\mathbf{X}_i$ 都在平面 $\boldsymbol{\pi}$ 上：$\mathbf{X}_i^\mathsf{T}\boldsymbol{\pi}=0$，$i=1,2,3$。疊起來：

$$
\begin{pmatrix}\mathbf{X}_1^\mathsf{T}\\ \mathbf{X}_2^\mathsf{T}\\ \mathbf{X}_3^\mathsf{T}\end{pmatrix}\boldsymbol{\pi}=\mathbf{0}
$$

- 這是 $3\times4$ 矩陣乘 $4\times1$ 向量等於零，就是熟悉的 $A\mathbf{x}=\mathbf{0}$。
- **一般位置**（三點線性獨立）：矩陣 **rank 3** → 右零空間是 **1 維** → $\boldsymbol{\pi}$ 唯一確定（差一個縮放）。
- **rank 2**（三點線性相關 = **共線**）：零空間是 **2 維**。
  - 這時有一整束平面都包含這三點：所有**繞著那條線轉的平面**，叫**平面束（pencil of planes）**，那條線是軸。

### 3.3 三個平面決定一個點

[▶ 13:38](https://youtu.be/wpqTPTQcNAM?t=818)

對偶地，三個平面 $\boldsymbol{\pi}_i$ 的交點 $\mathbf{X}$ 滿足

$$
\begin{pmatrix}\boldsymbol{\pi}_1^\mathsf{T}\\ \boldsymbol{\pi}_2^\mathsf{T}\\ \boldsymbol{\pi}_3^\mathsf{T}\end{pmatrix}\mathbf{X}=\mathbf{0}
$$

| 矩陣 rank | 幾何情況 |
|---|---|
| 3 | 三平面交於**唯一一點** |
| 2 | 沒有唯一交點；交成一條線，或兩兩交成幾條線（講者說有四種配置） |
| 1 | 三個平面**互相平行**（講者的說法） |

- rank 3 的那個點同時在三個平面上——這就是**點面對偶**的體現。

> 以下**不是逐字稿內容**，是依線性代數推論的補充：rank 1 表示三個 $\boldsymbol{\pi}_i$ 是同一個平面（差縮放）。在射影空間裡，三個不同的平行平面其實交於無窮遠的一條線，對應的矩陣是 rank 2。講者「rank 1 = 平行」的說法較寬鬆。

### 3.4 平面上的點：X = Mx

[▶ 14:57](https://youtu.be/wpqTPTQcNAM?t=897)

平面 $\boldsymbol{\pi}$ 上的點可以寫成

$$
\mathbf{X}=M\mathbf{x},\qquad M=\begin{pmatrix}\mathbf{m}_1 & \mathbf{m}_2 & \mathbf{m}_3\end{pmatrix}\in\mathbb{R}^{4\times3},\quad \mathbf{x}=(x_1,x_2,x_3)^\mathsf{T}
$$

- 展開：$\mathbf{X}=x_1\mathbf{m}_1+x_2\mathbf{m}_2+x_3\mathbf{m}_3$，是 $M$ 三行的**線性組合**。
- $M$ 的三行張成平面這個子空間；平面上任一點都是它們的線性組合。
- 因為 $M\mathbf{x}$ 在平面上，關聯關係給 $\boldsymbol{\pi}^\mathsf{T}M=\mathbf{0}^\mathsf{T}$。也就是說，**$M$ 的三行張成 $\boldsymbol{\pi}^\mathsf{T}$ 的零空間**。
- $\mathbf{x}$ 就是「這一點在平面上的座標」（線性組合的係數）。

**$M$ 不唯一**，一種選法 [▶ 17:44](https://youtu.be/wpqTPTQcNAM?t=1064)：若 $\boldsymbol{\pi}=(a,b,c,d)^\mathsf{T}$ 且 $a\neq0$，

$$
M^\mathsf{T}=\begin{pmatrix}\mathbf{p} & I_{3\times3}\end{pmatrix},\qquad \mathbf{p}=\left(-\frac{b}{a},-\frac{c}{a},-\frac{d}{a}\right)^\mathsf{T}
$$

（$\mathbf{p}$ 的形式依 MVG §3.2.1 式 (3.7) 後的說明補上；逐字稿只說「$\mathbf{p}$ 是這個」。）講者留作練習：驗證 $\boldsymbol{\pi}^\mathsf{T}M=\mathbf{0}^\mathsf{T}$。

> 以下**不是逐字稿內容**，是驗證的關鍵一步：$M$ 的第 $j$ 行是 $(p_j,\mathbf{e}_j^\mathsf{T})^\mathsf{T}$，所以 $\boldsymbol{\pi}^\mathsf{T}M$ 的第 1 個分量是 $a\cdot(-b/a)+b=0$，第 2、3 個同理。

---

## 4. 線（一）：零空間與張成表示

[▶ 18:12](https://youtu.be/wpqTPTQcNAM?t=1092)

- 線由**兩點的連線**或**兩平面的交線**定義。
- **3D 的線有 4 個自由度** [▶ 18:51](https://youtu.be/wpqTPTQcNAM?t=1131)：固定兩個平面，線穿過兩個平面各一點；每一點在自己的平面上可以往兩個方向動（2 個自由度），$2+2=4$。
- 用齊次向量表示 4 個自由度的東西，要 5 維向量，很**彆扭**。所以介紹兩種替代表示。

⚠️ 逐字稿缺字 [▶ 19:22](https://youtu.be/wpqTPTQcNAM?t=1162)：Whisper 寫「2 plus 2 will give us two degrees of freedom」，依上下文應為 **four**。

**張成表示（span representation）** [▶ 19:57](https://youtu.be/wpqTPTQcNAM?t=1197)：

兩個不重合的點 $\mathbf{A}$、$\mathbf{B}$，

$$
W=\begin{pmatrix}\mathbf{A}^\mathsf{T}\\ \mathbf{B}^\mathsf{T}\end{pmatrix}\in\mathbb{R}^{2\times4}
$$

- **$W^\mathsf{T}$ 的列空間（span）**：$\lambda\mathbf{A}+\mu\mathbf{B}$，是線上所有的點，叫**點束（pencil of points）**。
- **$W$ 的 2 維右零空間**：所有包含這條線的平面，叫**平面束**。
- 換兩個點 $\mathbf{A}'$、$\mathbf{B}'$（沿線移動，各是 $\mathbf{A}$、$\mathbf{B}$ 的線性組合），張成的空間不變 → 代表**同一條線**。

**為什麼零空間是平面束** [▶ 21:59](https://youtu.be/wpqTPTQcNAM?t=1319)：設 $\mathbf{P}$、$\mathbf{Q}$ 是 $W$ 零空間的基底。

1. $W\mathbf{P}=\mathbf{0}$ → $\mathbf{A}^\mathsf{T}\mathbf{P}=\mathbf{B}^\mathsf{T}\mathbf{P}=0$ → 平面 $\mathbf{P}$ 包含 $\mathbf{A}$ 和 $\mathbf{B}$。
2. 同理平面 $\mathbf{Q}$ 也包含 $\mathbf{A}$ 和 $\mathbf{B}$。
3. $\mathbf{A}$、$\mathbf{B}$ 同時在兩個平面上 → 它們連成的線就是**兩平面的交線**。
4. 任何 $\mathbf{P}$、$\mathbf{Q}$ 的線性組合也是包含這條線的平面。

**對偶表示** [▶ 24:31](https://youtu.be/wpqTPTQcNAM?t=1471)：用兩個平面

$$
W^*=\begin{pmatrix}\mathbf{P}^\mathsf{T}\\ \mathbf{Q}^\mathsf{T}\end{pmatrix}
$$

- $W^{*\mathsf{T}}$ 的張成空間：平面束。
- $W^*$ 的 2 維零空間：線上的點束。

**兩種表示的關係** [▶ 26:12](https://youtu.be/wpqTPTQcNAM?t=1572)：

$$
W^*W^\mathsf{T}=WW^{*\mathsf{T}}=\mathbf{0}_{2\times2}
$$

展開就是 $\mathbf{P}^\mathsf{T}\mathbf{A}=\mathbf{P}^\mathsf{T}\mathbf{B}=\mathbf{Q}^\mathsf{T}\mathbf{A}=\mathbf{Q}^\mathsf{T}\mathbf{B}=0$：兩點都在兩平面上。

**用零空間算「連」與「交」** [▶ 26:48](https://youtu.be/wpqTPTQcNAM?t=1608)：

- **線 $W$ + 不在線上的點 $\mathbf{X}$ → 平面**：
$$
\begin{pmatrix} W\\ \mathbf{X}^\mathsf{T}\end{pmatrix}\boldsymbol{\pi}=\begin{pmatrix}\mathbf{A}^\mathsf{T}\\ \mathbf{B}^\mathsf{T}\\ \mathbf{X}^\mathsf{T}\end{pmatrix}\boldsymbol{\pi}=\mathbf{0}
$$
  三個點都在平面上，$\boldsymbol{\pi}$ 就是這個 $3\times4$ 矩陣的零空間。
- **線 $W^*$ + 不包含它的平面 $\boldsymbol{\pi}$ → 點**（對偶）：
$$
\begin{pmatrix} W^*\\ \boldsymbol{\pi}^\mathsf{T}\end{pmatrix}\mathbf{X}=\begin{pmatrix}\mathbf{P}^\mathsf{T}\\ \mathbf{Q}^\mathsf{T}\\ \boldsymbol{\pi}^\mathsf{T}\end{pmatrix}\mathbf{X}=\mathbf{0}
$$
  交點同時在三個平面上。

【課本補充】MVG §3.2.2 還有第二種表示叫 **Plücker 矩陣** $L=\mathbf{A}\mathbf{B}^\mathsf{T}-\mathbf{B}\mathbf{A}^\mathsf{T}$（$4\times4$ 反對稱、rank 2），本集沒講。

---

## 5. 線（二）：Plücker 座標

[▶ 29:06](https://youtu.be/wpqTPTQcNAM?t=1746)

講者的定義：線通過兩點 $\mathbf{A}$、$\mathbf{B}$（這裡指 3 維非齊次座標），**Plücker 線座標**是 6 維向量

$$
\mathcal{L}=\begin{pmatrix}\mathbf{d}\\ \mathbf{m}\end{pmatrix},\qquad \mathbf{d}=\mathbf{B}-\mathbf{A}\ (\text{方向}),\qquad \mathbf{m}=\mathbf{A}\times\mathbf{B}\ (\text{力矩向量，moment})
$$

- 前三個是線的**方向**；後三個是兩點的外積，叫**力矩向量（moment vector）**。
- 【口頭】講者說：之後講**廣義相機（generalized camera，非中心投影的相機）**時（Lecture 12）會用到。

**兩線相交的條件** [▶ 30:39](https://youtu.be/wpqTPTQcNAM?t=1839)：線 $\mathcal{L}$（過 $\mathbf{A},\mathbf{B}$）和 $\hat{\mathcal{L}}$（過 $\hat{\mathbf{A}},\hat{\mathbf{B}}$）

- 相交 ⟺ 四點**共平面** ⟺ 兩線共面（共面之後就變成 2D，兩線一定相交）。
- 判斷：
$$
\det\begin{pmatrix}\mathbf{A} & \mathbf{B} & \hat{\mathbf{A}} & \hat{\mathbf{B}}\end{pmatrix}=0
$$
  （這裡 $\mathbf{A}$ 等是 4 維齊次座標。）
- 講者說這個行列式展開後是「兩個內積的和」，跳過推導，留作練習。

> 以下**不是逐字稿內容**：逐字稿沒唸出那兩個內積。依講者的 $(\mathbf{d},\mathbf{m})$ 定義，標準結果是
> $$\det\begin{pmatrix}\mathbf{A} & \mathbf{B} & \hat{\mathbf{A}} & \hat{\mathbf{B}}\end{pmatrix}=\pm\left(\mathbf{d}\cdot\hat{\mathbf{m}}+\hat{\mathbf{d}}\cdot\mathbf{m}\right)$$
> 所以兩線相交 ⟺ $\mathbf{d}\cdot\hat{\mathbf{m}}+\hat{\mathbf{d}}\cdot\mathbf{m}=0$（正負號依 $\mathbf{m}$ 取 $\mathbf{A}\times\mathbf{B}$ 或 $\mathbf{B}\times\mathbf{A}$，不影響「是否為 0」）。

【口頭】[▶ 32:25](https://youtu.be/wpqTPTQcNAM?t=1945) 講者的直覺說明：兩條線共平面時，它們的力矩向量「方向一樣」，所以內積和行列式為 0。

**來源差異**：MVG §3.2.2 的 Plücker 座標定義不同：取 Plücker 矩陣 $L$ 的六個非零元素 $\{l_{12},l_{13},l_{14},l_{23},l_{42},l_{34}\}$，相交條件寫成

$$
\det\begin{pmatrix}\mathbf{A} & \mathbf{B} & \hat{\mathbf{A}} & \hat{\mathbf{B}}\end{pmatrix}=l_{12}\hat{l}_{34}+\hat{l}_{12}l_{34}+l_{13}\hat{l}_{42}+\hat{l}_{13}l_{42}+l_{14}\hat{l}_{23}+\hat{l}_{14}l_{23}=(\mathcal{L}|\hat{\mathcal{L}})
$$

（MVG Result 3.5：$(\mathcal{L}|\hat{\mathcal{L}})=0$ ⟺ 兩線共面、相交。）兩種寫法的六個數是同一組量的不同排列（$\mathbf{d}$、$\mathbf{m}$ 的分量對應 $l_{ij}$，可能差正負號）。

**對偶性質** [▶ 33:00](https://youtu.be/wpqTPTQcNAM?t=1980)：

- 兩線分別是平面 $\mathbf{P},\mathbf{Q}$ 和 $\hat{\mathbf{P}},\hat{\mathbf{Q}}$ 的交線：相交 ⟺ $\det\begin{pmatrix}\mathbf{P} & \mathbf{Q} & \hat{\mathbf{P}} & \hat{\mathbf{Q}}\end{pmatrix}=0$。直接由點面對偶得到。
- 一條是兩平面的交線、另一條是兩點的連線，類似的關係也成立。

【課本補充】MVG 式 (3.14)：$\mathcal{L}$ 是 $\mathbf{P},\mathbf{Q}$ 的交線、$\hat{\mathcal{L}}$ 是 $\mathbf{A},\mathbf{B}$ 的連線時，$(\mathcal{L}|\hat{\mathcal{L}})=(\mathbf{P}^\mathsf{T}\mathbf{A})(\mathbf{Q}^\mathsf{T}\mathbf{B})-(\mathbf{Q}^\mathsf{T}\mathbf{A})(\mathbf{P}^\mathsf{T}\mathbf{B})$。另外，一個 6 維向量要代表一條線，必須滿足 $(\mathcal{L}|\mathcal{L})=0$（**Klein 二次曲面**約束）——這就是為什麼 6 個數只有 4 個自由度（少 1 個縮放、少 1 個約束）。

---

## 6. 二次曲面與對偶二次曲面

[▶ 34:22](https://youtu.be/wpqTPTQcNAM?t=2062)

**二次曲面（quadric）**：

$$
\mathbf{X}^\mathsf{T}Q\mathbf{X}=0,\qquad Q\ \text{是}\ 4\times4\ \text{對稱矩陣}
$$

- 和二次曲線 $C$ 類比，只是 $3\times3\to4\times4$。
- 常常不區分矩陣 $Q$ 和它定義的曲面，直接叫「二次曲面 $Q$」。

**性質**（直接從二次曲線推廣）[▶ 35:22](https://youtu.be/wpqTPTQcNAM?t=2122)：

| | 二次曲線 $C$ | 二次曲面 $Q$ |
|---|---|---|
| 大小 | $3\times3$ 對稱 | $4\times4$ 對稱 |
| 獨立元素 | 6 | 10 |
| 自由度 | 5 | **9** |
| 決定它需要 | 5 點 | **9 點**（一般位置） |
| 奇異時 | 退化，可由更少的點決定 | 退化，可由更少的點決定 |

**平面截二次曲面 = 二次曲線** [▶ 36:55](https://youtu.be/wpqTPTQcNAM?t=2215)：

1. 平面 $\boldsymbol{\pi}$ 上的點寫成 $\mathbf{X}=M\mathbf{x}$（第 3.4 節）。
2. 代進 $\mathbf{X}^\mathsf{T}Q\mathbf{X}=0$：
$$
\mathbf{x}^\mathsf{T}\underbrace{M^\mathsf{T}QM}_{C}\mathbf{x}=0
$$
3. 尺寸：$M^\mathsf{T}$ 是 $3\times4$、$Q$ 是 $4\times4$、$M$ 是 $4\times3$ → $C$ 是 $3\times3$。
4. 這正是二次曲線的方程式 → 交線是**二次曲線** $C=M^\mathsf{T}QM$。

**變換** [▶ 39:20](https://youtu.be/wpqTPTQcNAM?t=2360)：點 $\mathbf{X}'=H\mathbf{X}$ 時，

$$
Q'=H^{-\mathsf{T}}QH^{-1}
$$

**證明**：

1. 從 $\mathbf{X}'^\mathsf{T}Q'\mathbf{X}'=0$ 出發，代 $\mathbf{X}'=H\mathbf{X}$：$\mathbf{X}^\mathsf{T}H^\mathsf{T}Q'H\mathbf{X}=0$。
2. 這是 $\mathbf{X}$ 的二次式，所以 $Q=H^\mathsf{T}Q'H$。
3. 把 $H$ 移到另一邊：$Q'=H^{-\mathsf{T}}QH^{-1}$。∎

**對偶二次曲面** [▶ 40:23](https://youtu.be/wpqTPTQcNAM?t=2423)：

- 點面對偶 → 可以定義一個關於**平面**的方程式：
$$
\boldsymbol{\pi}^\mathsf{T}Q^*\boldsymbol{\pi}=0
$$
  滿足它的平面是 $Q$ 的**切平面**。
- $Q^*$ 是 $Q$ 的**伴隨矩陣（adjoint）**；$Q$ 可逆時 $Q^*=Q^{-1}$（差縮放）。
- 伴隨矩陣：$\operatorname{adj}(A)=C^\mathsf{T}$，$C$ 是 $A$ 的**餘因子矩陣（cofactor matrix）**。
- 變換規則講者留作練習，「和上面一樣的方法證明」。

> 以下**不是逐字稿內容**，是依 MVG §3.2.3 和第 02 集的對偶二次曲線補上的：$Q^{*\prime}=HQ^*H^\mathsf{T}$。關鍵一步：$Q^{*\prime}=(Q')^{-1}=(H^{-\mathsf{T}}QH^{-1})^{-1}=HQ^{-1}H^\mathsf{T}$。

**常見二次曲面** [▶ 41:28](https://youtu.be/wpqTPTQcNAM?t=2488)：

- 橢球面（ellipsoid）
- 單葉雙曲面（hyperboloid of one sheet）
- 雙葉雙曲面（hyperboloid of two sheets）
- 橢圓錐面（elliptic cone）
- 橢圓拋物面（elliptic paraboloid）
- 雙曲拋物面（hyperbolic paraboloid）

**來源差異**：講者說橢圓錐面「是退化的二次曲面，rank 只有 1」；MVG Fig. 3.4 說錐面的矩陣是 **rank 3**（零向量是錐的頂點）。rank 1 的 $4\times4$ 對稱矩陣是 $\boldsymbol{\pi}\boldsymbol{\pi}^\mathsf{T}$，代表一個重複的平面，不是錐面——所以依 MVG，錐面應為 rank 3。

【課本補充】（MVG §3.2.3–3.2.4）

- $\boldsymbol{\pi}=Q\mathbf{X}$ 是點 $\mathbf{X}$ 對 $Q$ 的**極平面（polar plane）**；$\mathbf{X}$ 在 $Q$ 上時，$Q\mathbf{X}$ 就是 $Q$ 在 $\mathbf{X}$ 的切平面（類比 2D 的切線 $C\mathbf{x}$）。
- 二次曲面分**直紋（ruled）**和**非直紋**兩類：直紋曲面包含直線。非退化的直紋曲面是單葉雙曲面（含兩族直線）。錐面（rank 3）和兩個平面（rank 2）是兩種最重要的退化二次曲面，都是直紋的。

---

## 7. 3D 變換階層

[▶ 42:06](https://youtu.be/wpqTPTQcNAM?t=2526)

2D 階層的直接推廣，$3\times3\to4\times4$：

| 群 | 矩陣 | 自由度 | 不變量 |
|---|---|---|---|
| 射影 | $\begin{pmatrix} A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}$ | 15 | 曲面接觸時的相交、相切 |
| 仿射 | $\begin{pmatrix} A & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ | 12 | （本集未講，見課本補充） |
| 相似 | $\begin{pmatrix} sR & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ | 7 | （本集未講，見課本補充） |
| 歐氏 | $\begin{pmatrix} R & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ | 6 | （本集未講，見課本補充） |

- $A$ 是 $3\times3$，$\mathbf{t}$ 是 $3\times1$。
- 相似、歐氏的 $R\in SO(3)$、$\mathbf{t}\in\mathbb{R}^3$。歐氏變換就是第 03 集的**剛體運動** $SE(3)$。
- 講者只說了射影 15、相似 7、歐氏 6 的自由度；仿射 12 依 MVG Table 3.2 補上。

【課本補充】MVG Table 3.2 的不變量：

- 仿射（12 dof）：平面的平行、體積比、質心、**無窮遠平面 $\boldsymbol{\pi}_\infty$**。
- 相似（7 dof）：**絕對二次曲線 $\Omega_\infty$**（Lecture 3 的主題）。
- 歐氏（6 dof）：體積。

---

## 8. Lecture 2 總結

[▶ 43:46](https://youtu.be/wpqTPTQcNAM?t=2626)

1. $SE(3)$ 群，用來描述 3D 剛體運動（第 03 集）。
2. 在 $\mathbb{P}^3$ 表示點、平面，點面對偶。
3. 用兩種方式表示 3D 的線：零空間／張成矩陣、Plücker 座標。
4. 把 2D 二次曲線的性質推廣到二次曲面。

---

## 9. 一頁速查表

### 點、平面

| 公式 | 關鍵一步 |
|---|---|
| $\mathbf{X}=(X_1,\dots,X_4)^\mathsf{T}$，$X_4=0$ 是無窮遠點 | 前三個除以 $X_4$ |
| 點在平面上 $\boldsymbol{\pi}^\mathsf{T}\mathbf{X}=0$；平面 3 dof | 齊次化 $\pi_1X+\pi_2Y+\pi_3Z+\pi_4=0$ |
| 法向量 $(\pi_1,\pi_2,\pi_3)$，原點距離 $\pi_4/\|\mathbf{n}\|$ | — |
| 三點 → 平面：$[\mathbf{X}_1^\mathsf{T};\mathbf{X}_2^\mathsf{T};\mathbf{X}_3^\mathsf{T}]\boldsymbol{\pi}=0$ | rank 3 → 1 維零空間；rank 2 → 共線、平面束 |
| 三平面 → 點：$[\boldsymbol{\pi}_1^\mathsf{T};\boldsymbol{\pi}_2^\mathsf{T};\boldsymbol{\pi}_3^\mathsf{T}]\mathbf{X}=0$ | 對偶 |
| 平面上的點 $\mathbf{X}=M\mathbf{x}$，$\boldsymbol{\pi}^\mathsf{T}M=0$ | $M^\mathsf{T}=[\mathbf{p}\mid I]$，$\mathbf{p}=(-b/a,-c/a,-d/a)^\mathsf{T}$ |

### 線（4 dof）

| 表示 | 內容 |
|---|---|
| $W=[\mathbf{A}^\mathsf{T};\mathbf{B}^\mathsf{T}]$ | 列空間 = 點束；零空間 = 平面束 |
| $W^*=[\mathbf{P}^\mathsf{T};\mathbf{Q}^\mathsf{T}]$ | 列空間 = 平面束；零空間 = 點束 |
| $W^*W^\mathsf{T}=0$ | 兩點都在兩平面上 |
| Plücker（講者版）$(\mathbf{d},\mathbf{m})=(\mathbf{B}-\mathbf{A},\ \mathbf{A}\times\mathbf{B})$ | 相交 ⟺ $\det[\mathbf{A},\mathbf{B},\hat{\mathbf{A}},\hat{\mathbf{B}}]=0$ ⟺ $\mathbf{d}\cdot\hat{\mathbf{m}}+\hat{\mathbf{d}}\cdot\mathbf{m}=0$ |

### 變換規則（點 $\mathbf{X}'=H\mathbf{X}$，$H$ 是 $4\times4$，15 dof）

| 物件 | 變成 | 關鍵一步 |
|---|---|---|
| 平面 | $\boldsymbol{\pi}'=H^{-\mathsf{T}}\boldsymbol{\pi}$ | $\boldsymbol{\pi}^\mathsf{T}H^{-1}H\mathbf{X}=0$ |
| 二次曲面 | $Q'=H^{-\mathsf{T}}QH^{-1}$ | 代 $\mathbf{X}'=H\mathbf{X}$ 得 $Q=H^\mathsf{T}Q'H$ |
| 對偶二次曲面 | $Q^{*\prime}=HQ^*H^\mathsf{T}$ | 對 $Q'$ 取逆 |

### 二次曲面

- $\mathbf{X}^\mathsf{T}Q\mathbf{X}=0$，9 dof，9 點決定。
- 平面截面：$C=M^\mathsf{T}QM$。
- 對偶：$\boldsymbol{\pi}^\mathsf{T}Q^*\boldsymbol{\pi}=0$，$Q^*=\operatorname{adj}Q$（可逆時 $=Q^{-1}$）。

### 3D 階層自由度

射影 15 → 仿射 12 → 相似 7 → 歐氏 6。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 3D 變換階層、相似變換保持 $\Omega_\infty$ | 第 05–07 集（Lecture 3：無窮遠平面、絕對二次曲線） |
| 對偶二次曲面 $Q^*$、$Q^{*\prime}=HQ^*H^\mathsf{T}$ | 第 05–07 集（絕對對偶二次曲面 $Q_\infty^*$） |
| 點面對偶、三平面交點 | 第 13–15 集（單視角量測、消失線） |
| 兩點連線、平面束 | 第 16–19 集（極平面：包含基線的平面束） |
| Plücker 座標 | 第 35–37 集（Lecture 12：廣義相機） |
| 用零空間解 $A\mathbf{x}=0$ | 第 08 集（DLT）；整門課的估計問題 |

---

## 附：本集一句話總結

> **3D 射影幾何把 2D 的一切多加一維：點和平面是 4 維齊次向量且互為對偶，線有 4 個自由度、要用兩點／兩平面的張成或 Plücker 座標表示，二次曲面是 $4\times4$ 對稱矩陣；射影變換變成 $4\times4$（15 dof），各物件的變換規則和 2D 一模一樣。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 2 (Part 2) 錄影逐字稿（Whisper `medium.en`，44:26）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §3.1–3.2.4、§3.4 整理。*
