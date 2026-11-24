---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 08
lecture: Lecture 4 (Part 1) – Robust homography estimation
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/W8vgVoQdwAM
notes: MVG §4.1（書頁 88–92，PDF 頁 106–110）、§4.4（書頁 104–109，PDF 頁 122–127）、Result 13.1（書頁 326，PDF 頁 344）；homography 存在的推導講者說取自 Ma Yi 書 §5.3（BRIEF 沒列，未查）
---

# 第 08 集 · Lecture 4 (Part 1)：homography 何時存在、DLT、資料正規化 [▶ 影片](https://youtu.be/W8vgVoQdwAM)

← 上一集：[07-circular-points-absolute-conic-part3](07-circular-points-absolute-conic-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[09-robust-homography-part2](09-robust-homography-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 08 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（56:48，Whisper `medium.en` 轉錄）＋ MVG §4.1、§4.4、Result 13.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. homography 什麼時候存在](#1-homography-什麼時候存在)
  - [1.1 情況一：場景是一個平面](#11-情況一場景是一個平面)
  - [1.2 情況二：無窮遠平面（或純旋轉）](#12-情況二無窮遠平面或純旋轉)
- [2. 需要幾對對應點](#2-需要幾對對應點)
- [3. DLT：直接線性變換](#3-dlt直接線性變換)
  - [3.1 用外積化成 A_i h = 0](#31-用外積化成-a_i-h--0)
  - [3.2 有雜訊時：最小平方解](#32-有雜訊時最小平方解)
  - [3.3 為什麼答案是 V 的最後一行](#33-為什麼答案是-v-的最後一行)
  - [3.4 演算法](#34-演算法)
  - [3.5 退化情況：三點共線](#35-退化情況三點共線)
- [4. 資料正規化](#4-資料正規化)
  - [4.1 問題：病態矩陣](#41-問題病態矩陣)
  - [4.2 怎麼正規化](#42-怎麼正規化)
  - [4.3 正規化 DLT 演算法](#43-正規化-dlt-演算法)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/W8vgVoQdwAM?t=0)

Lecture 4 的目標（兩集合起來）：

| 目標 | 本集？ | 來源 |
|---|---|---|
| 證明兩種情況下 homography 存在 | ✅ | Ma Yi §5.3；MVG Result 13.1 |
| DLT 估計 homography、資料正規化 | ✅ | MVG §4.1、§4.4 |
| 代數誤差、幾何誤差、Sampson 誤差，用在 homography 估計 | 下一集 | MVG §4.2 |
| RANSAC 強健估計 | 下一集 | MVG §4.7 |

講者說內容取自 MVG 第 3、4 章和 Ma Yi 書 §5.3。

⚠️ 逐字稿缺字：Whisper 把 Sampson 寫成 “Samson”、把 Multiple View Geometry 寫成 “Multivariable Geometry”、把 RANSAC 寫成 “RANSAT”。

**回顧** [▶ 00:58](https://youtu.be/W8vgVoQdwAM?t=58)：第 01–02 集看過中心投影下平面到平面的變換 $\mathbf{x}'=H\mathbf{x}$（$\mathbb{P}^2\to\mathbb{P}^2$）。今天看最一般的形式——射影變換，本講叫 **homography**——以及怎麼用 4 點 RANSAC 估計它。

---

## 1. homography 什麼時候存在

[▶ 02:21](https://youtu.be/W8vgVoQdwAM?t=141)

homography 是 $\mathbb{P}^2\to\mathbb{P}^2$ 的變換。兩張照片的對應點之間要能用一個 $H$ 連起來，只有兩種情況。

### 1.1 情況一：場景是一個平面

[▶ 02:41](https://youtu.be/W8vgVoQdwAM?t=161)

- 3D 世界裡一群點，**全部落在一個平面 $\boldsymbol{\pi}$ 上**。
- 3D 點 $\mathbf{X}$ 投影到相機 1、相機 2，得到像點 $\mathbf{x}_1$、$\mathbf{x}_2$。
- 這時存在一個 $H$，使所有對應點滿足 $\mathbf{x}_2=H\mathbf{x}_1$。

**推導** [▶ 04:38](https://youtu.be/W8vgVoQdwAM?t=278)：

**設定**：

- $\mathbf{X}_1$、$\mathbf{X}_2$：同一個 3D 點在相機座標系 1、2 中的座標。
- 剛體變換（第 03 集）：
$$
\mathbf{X}_2=R\mathbf{X}_1+\mathbf{t}\qquad(1)
$$
  $R$、$\mathbf{t}$ 是從座標系 1 到 2 的旋轉、平移。
- $\mathbf{n}$：平面 $\boldsymbol{\pi}$ 在相機座標系 1 中的**單位法向量**（$\|\mathbf{n}\|=1$）。
- $d$：平面到相機中心 $C_1$ 的**垂直距離**。

**平面方程式**（第 04 集的非齊次形式）[▶ 06:30](https://youtu.be/W8vgVoQdwAM?t=390)：

$$
\mathbf{n}^\mathsf{T}\mathbf{X}_1=n_1X+n_2Y+n_3Z=d
\quad\Longleftrightarrow\quad
\frac{1}{d}\mathbf{n}^\mathsf{T}\mathbf{X}_1=1\qquad(2)
$$

**技巧**：式 (2) 等於 1，所以可以乘在式 (1) 的任何地方。乘在 $\mathbf{t}$ 上：

$$
\mathbf{X}_2=R\mathbf{X}_1+\mathbf{t}\cdot\frac{1}{d}\mathbf{n}^\mathsf{T}\mathbf{X}_1=\left(R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}\right)\mathbf{X}_1
$$

**換成像點** [▶ 08:07](https://youtu.be/W8vgVoQdwAM?t=487)：

- 3D 點和它的像點在同一條過相機中心的射線上：$\mathbf{X}_1=\lambda_1\mathbf{x}_1$、$\mathbf{X}_2=\lambda_2\mathbf{x}_2$（$\lambda$ 是把像點向量拉長到 3D 點的倍數）。
- 代入：
$$
\lambda_2\mathbf{x}_2=\left(R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}\right)\lambda_1\mathbf{x}_1
\quad\Longrightarrow\quad
\mathbf{x}_2=\frac{\lambda_1}{\lambda_2}\left(R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}\right)\mathbf{x}_1
$$
- 忽略縮放：
$$
\boxed{\ \mathbf{x}_2\sim H\mathbf{x}_1,\qquad H=R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}\ }
$$

- $H$ 由兩相機的相對旋轉 $R$、平移 $\mathbf{t}$、平面的法向量 $\mathbf{n}$、距離 $d$ 決定。

> 以下**不是逐字稿內容**，是說明：這裡的 $\mathbf{x}$ 是相機座標系下的「正規化」像點（相當於內參 $K=I$）。有內參時要換成 $K'HK^{-1}$；相機模型在 Lecture 5（第 10–12 集）講。

【課本補充】MVG Result 13.1 從另一個角度給出同樣的事：兩相機 $P=[I\mid\mathbf{0}]$、$P'=[A\mid\mathbf{a}]$，平面 $\boldsymbol{\pi}=(\mathbf{v}^\mathsf{T},1)^\mathsf{T}$，平面誘導的 homography 是 $H=A-\mathbf{a}\mathbf{v}^\mathsf{T}$。對應到上式：$A=R$、$\mathbf{a}=\mathbf{t}$，平面 $\mathbf{n}^\mathsf{T}\mathbf{X}=d$ 寫成 $(-\mathbf{n}/d)^\mathsf{T}\mathbf{X}+1=0$，即 $\mathbf{v}=-\mathbf{n}/d$，所以 $H=R+\mathbf{t}\mathbf{n}^\mathsf{T}/d$，兩者一致。

### 1.2 情況二：無窮遠平面（或純旋轉）

[▶ 11:13](https://youtu.be/W8vgVoQdwAM?t=673)

- 3D 點落在**無窮遠平面** $\boldsymbol{\pi}_\infty$ 上，也就是場景**非常遠**。
- 例：衛星拍地球，地面上的東西都非常遠，地面就像在 $\boldsymbol{\pi}_\infty$ 上。
- 代入情況一的公式，令 $d\to\infty$：
$$
H=R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}\ \xrightarrow{\ d\to\infty\ }\ R
$$
- 第二項趨近 0，只剩旋轉。

**同樣的效果：純旋轉** [▶ 13:15](https://youtu.be/W8vgVoQdwAM?t=795)：

- 如果相機**只旋轉、不平移**（$\mathbf{t}=\mathbf{0}$），第二項也消失，$H=R$。
- 所以：**很遠的場景**，或**相機純旋轉**，兩張照片的對應點都由 homography 連起來（不管場景是不是平面）。

> 以下**不是逐字稿內容**，是常見應用（依公式推論）：手機拍全景照時原地轉身拍，就是純旋轉的情況，所以可以用 homography 把照片拼起來。

---

## 2. 需要幾對對應點

[▶ 14:02](https://youtu.be/W8vgVoQdwAM?t=842)

**問題**：兩張照片上有一些已知的對應點 $\mathbf{x}_i\leftrightarrow\mathbf{x}_i'$（同一個 3D 點在兩個視角的像），怎麼求 $H$？最少需要幾對？

**答案** [▶ 15:15](https://youtu.be/W8vgVoQdwAM?t=915)：看兩件事——$H$ 的自由度、每對點給幾個約束。

- $H$ 有 9 個元素，少 1 個縮放 → **8 個自由度**（第 01–02 集）。
- 每對對應點給 **2 個約束**。
- 所以需要 **4 對**：$4\times2=8$。

**最小解（minimal solution）** [▶ 16:20](https://youtu.be/W8vgVoQdwAM?t=980)：

- 剛好 4 對點時，$H$ 有**精確解**，叫**最小解**。
- 【口頭】最小解對 **RANSAC 迴圈**很重要：每次需要的點越多，RANSAC 需要的迴圈次數會**指數成長**（下一集細講）。

**雜訊** [▶ 17:00](https://youtu.be/W8vgVoQdwAM?t=1020)：

- 影像來自有雜訊的感光元件，對應點的位置不精確；找對應點的演算法也有誤差。
- 所以用**最小平方（least squares）**來壓低雜訊的影響。

---

## 3. DLT：直接線性變換

### 3.1 用外積化成 A_i h = 0

[▶ 17:54](https://youtu.be/W8vgVoQdwAM?t=1074)

**起點**：$\mathbf{x}_i'=H\mathbf{x}_i$，$i=1,\dots,4$。

- 未知數：$H$ 的 9 個元素（8 個自由度）。
- 已知：對應點 $\mathbf{x}_i,\mathbf{x}_i'$（例如用 SIFT、SURF 找到；講者說本課不細講）。
- **目標**：化成齊次線性方程式 $A\mathbf{h}=\mathbf{0}$，$\mathbf{h}$ 是 $H$ 的 9 個元素排成的 $9\times1$ 向量，$A$ 由已知的對應點組成。

**問題**：$\mathbf{x}_i'=H\mathbf{x}_i$ 只在差一個縮放下成立，不能直接當等式用。

**技巧：兩邊和 $\mathbf{x}_i'$ 取外積** [▶ 20:09](https://youtu.be/W8vgVoQdwAM?t=1209)：

$$
\mathbf{x}_i'\times H\mathbf{x}_i=\mathbf{x}_i'\times\mathbf{x}_i'=\mathbf{0}
$$

（任何向量和自己的外積是 0。這樣縮放就不重要了——兩個平行向量的外積是 0。）

**展開**：把 $H$ 的三列寫成 $\mathbf{h}^{1\mathsf{T}},\mathbf{h}^{2\mathsf{T}},\mathbf{h}^{3\mathsf{T}}$，$\mathbf{x}_i'=(x_i',y_i',w_i')^\mathsf{T}$：

$$
H\mathbf{x}_i=\begin{pmatrix}\mathbf{h}^{1\mathsf{T}}\mathbf{x}_i\\ \mathbf{h}^{2\mathsf{T}}\mathbf{x}_i\\ \mathbf{h}^{3\mathsf{T}}\mathbf{x}_i\end{pmatrix},\qquad
\mathbf{x}_i'\times H\mathbf{x}_i=\begin{pmatrix} y_i'\mathbf{h}^{3\mathsf{T}}\mathbf{x}_i-w_i'\mathbf{h}^{2\mathsf{T}}\mathbf{x}_i\\ w_i'\mathbf{h}^{1\mathsf{T}}\mathbf{x}_i-x_i'\mathbf{h}^{3\mathsf{T}}\mathbf{x}_i\\ x_i'\mathbf{h}^{2\mathsf{T}}\mathbf{x}_i-y_i'\mathbf{h}^{1\mathsf{T}}\mathbf{x}_i\end{pmatrix}
$$

**把 $\mathbf{h}$ 提出來**（用 $\mathbf{h}^{j\mathsf{T}}\mathbf{x}_i=\mathbf{x}_i^\mathsf{T}\mathbf{h}^j$）[▶ 21:18](https://youtu.be/W8vgVoQdwAM?t=1278)：

$$
\begin{pmatrix}\mathbf{0}^\mathsf{T} & -w_i'\mathbf{x}_i^\mathsf{T} & y_i'\mathbf{x}_i^\mathsf{T}\\ w_i'\mathbf{x}_i^\mathsf{T} & \mathbf{0}^\mathsf{T} & -x_i'\mathbf{x}_i^\mathsf{T}\\ -y_i'\mathbf{x}_i^\mathsf{T} & x_i'\mathbf{x}_i^\mathsf{T} & \mathbf{0}^\mathsf{T}\end{pmatrix}\begin{pmatrix}\mathbf{h}^1\\ \mathbf{h}^2\\ \mathbf{h}^3\end{pmatrix}=\mathbf{0}
$$

（外積展開和係數矩陣依 MVG 式 (4.1)–(4.3) 寫出；逐字稿只說「明確給出這個式子」「提出來得到這個線性形式」。）

**只有兩列獨立** [▶ 21:51](https://youtu.be/W8vgVoQdwAM?t=1311)：

- 係數矩陣是 $3\times9$，但只有**兩列線性獨立**。
- 講者說：$x_i'$ 乘第一列加 $y_i'$ 乘第二列，得到第三列（差一個縮放）。

> 以下**不是逐字稿內容**，是驗證：$x_i'\cdot(\text{列 1})+y_i'\cdot(\text{列 2})=\left(y_i'w_i'\mathbf{x}_i^\mathsf{T},\ -x_i'w_i'\mathbf{x}_i^\mathsf{T},\ (x_i'y_i'-y_i'x_i')\mathbf{x}_i^\mathsf{T}\right)=-w_i'\cdot(\text{列 3})$。

- 所以每對點給 **2 個約束**，取前兩列得 $2\times9$ 的 $A_i$：
$$
A_i\mathbf{h}=\mathbf{0},\qquad \mathbf{h}=(h_1,h_2,\dots,h_9)^\mathsf{T}
$$

**$w_i$ 通常取 1** [▶ 23:55](https://youtu.be/W8vgVoQdwAM?t=1435)：像點 $\mathbf{x}_i=(x_i,y_i,w_i)^\mathsf{T}$，通常除以 $w_i$ 變成 $(x_i/w_i,\ y_i/w_i,\ 1)^\mathsf{T}$。

**疊起來** [▶ 25:05](https://youtu.be/W8vgVoQdwAM?t=1505)：

$$
A=\begin{pmatrix}A_1\\ A_2\\ \vdots\\ A_N\end{pmatrix}\in\mathbb{R}^{2N\times9},\qquad A\mathbf{h}=\mathbf{0}
$$

- 4 對點是**最少**的要求。
- 用超過 4 對點疊起來，可以求對雜訊更強健的**最小平方解**。

### 3.2 有雜訊時：最小平方解

[▶ 26:01](https://youtu.be/W8vgVoQdwAM?t=1561)

- 對應點有雜訊 → $A\mathbf{h}=\mathbf{0}$ **沒有精確解**：就算找到最好的 $\mathbf{h}$，代回去也不會剛好是 0。
- 改成**最小化** $\|A\mathbf{h}\|$：
$$
\min_{\mathbf{h}}\ \|A\mathbf{h}\|\quad\text{subject to}\quad \|\mathbf{h}\|=1
$$
- **為什麼要約束 $\|\mathbf{h}\|=1$** [▶ 28:51](https://youtu.be/W8vgVoQdwAM?t=1731)：
  - 沒有約束的話，$\mathbf{h}=\mathbf{0}$ 會讓 $\|A\mathbf{h}\|=0$——這是沒用的**平凡解（trivial solution）**。
  - 而且 $H$ 的尺度本來就不知道，乾脆規定成 1。

⚠️ 逐字稿缺字 [▶ 28:01](https://youtu.be/W8vgVoQdwAM?t=1681)：講者說「subjected to the constraint of the norm of h equals to zero」，應為 **one**（後面講者自己說的是 1）。

### 3.3 為什麼答案是 V 的最後一行

[▶ 30:00](https://youtu.be/W8vgVoQdwAM?t=1800)

**答案**：對 $A$ 做 SVD，$\mathbf{h}$ = **最小奇異值**對應的**右奇異向量**。

**SVD 的形狀** [▶ 31:04](https://youtu.be/W8vgVoQdwAM?t=1864)：

$$
A_{2N\times9}=U_{2N\times2N}\ \Sigma_{2N\times9}\ V_{9\times9}^\mathsf{T}
$$

- $U$：左正交矩陣；$V$：右正交矩陣，行是 $\mathbf{v}_1,\dots,\mathbf{v}_9$。
- $\Sigma$：前 9 列的對角是奇異值 $\sigma_1\ge\sigma_2\ge\dots\ge\sigma_9$，其餘 $2N-9$ 列全是 0。

⚠️ 逐字稿缺字 [▶ 32:57](https://youtu.be/W8vgVoQdwAM?t=1977)：講者講一般 $n\times m$ 矩陣時，維度符號前後混用（例如說「$m>n$ 是高瘦矩陣」又說「左奇異向量 $m\times m$」）。依上面 $2N\times9$ 的具體例子理解即可：$U$ 的大小是列數 × 列數，$V$ 是行數 × 行數。

**沒有雜訊時** [▶ 34:05](https://youtu.be/W8vgVoQdwAM?t=2045)：精確解存在，$A$ 的 rank 剛好是 8，最小的奇異值 $\sigma_9=0$。

**有雜訊時** [▶ 35:43](https://youtu.be/W8vgVoQdwAM?t=2143)：rank 不是 8，$\sigma_9\neq0$。

**論證** [▶ 36:29](https://youtu.be/W8vgVoQdwAM?t=2189)：

1. $A=U\Sigma V^\mathsf{T}$，$V$ 正交（$V^{-1}=V^\mathsf{T}$）→ $AV=U\Sigma$。
2. 逐行看：$A\mathbf{v}_i=\sigma_i\mathbf{u}_i$。
3. 所以 $\|A\mathbf{v}_i\|=\sigma_i\|\mathbf{u}_i\|=\sigma_i$。
4. SVD 的奇異值由大到小排（Python、Matlab 都是），最小的是 $\sigma_9$ → 取 $\mathbf{h}=\mathbf{v}_9$，$\|A\mathbf{h}\|$ 最小。
5. $\mathbf{v}_9$ 是正交矩陣的一行，長度自動是 1 → 約束 $\|\mathbf{h}\|=1$ 自動滿足。

> 以下**不是逐字稿內容**，是補完論證（講者只比較了 $\mathbf{v}_i$ 這幾個候選，沒有證明其他單位向量不會更好）：任意單位向量可寫成 $\mathbf{h}=\sum_ic_i\mathbf{v}_i$，$\sum_ic_i^2=1$。則
> $$\|A\mathbf{h}\|^2=\Big\|\sum_ic_i\sigma_i\mathbf{u}_i\Big\|^2=\sum_ic_i^2\sigma_i^2\ \ge\ \sigma_9^2\sum_ic_i^2=\sigma_9^2$$
> （第二個等號用 $\mathbf{u}_i$ 互相正交、長度 1。）等號在 $\mathbf{h}=\pm\mathbf{v}_9$ 時成立。所以 $\mathbf{v}_9$ 是全域最小解。

### 3.4 演算法

[▶ 40:49](https://youtu.be/W8vgVoQdwAM?t=2449)

**在解什麼**：給 $N\ge4$ 對 2D–2D 對應點 $\mathbf{x}_i\leftrightarrow\mathbf{x}_i'$，求 $H$ 使 $\mathbf{x}_i'=H\mathbf{x}_i$。

**步驟**（基本 DLT，MVG Algorithm 4.1）：

1. 對每對點，算 $3\times9$ 係數矩陣，取前兩列得 $2\times9$ 的 $A_i$。
2. 把 $N$ 個 $A_i$ 疊成 $2N\times9$ 的 $A$。
3. SVD：$A=U\Sigma V^\mathsf{T}$。$\mathbf{h}$ = $V$ 的最後一行（對應最小奇異值）。
4. 把 9 維的 $\mathbf{h}$ 排回 $3\times3$ 的 $H$。

（但實務上一定要加第 4 節的正規化。）

### 3.5 退化情況：三點共線

[▶ 44:04](https://youtu.be/W8vgVoQdwAM?t=2644)

講者的說法：

- $\mathbf{h}$ 有 8 個自由度，要唯一解，$A$ 的 rank 必須是 8。
- 4 對點中如果**有 3 點共線**，這三點線性相關（任兩點就能推出第三點所在的線），獨立約束少於 8 → rank 掉到 8 以下 → 解不出 $\mathbf{h}$。
- 這叫**臨界配置（critical configuration）**或**退化情況（degeneracy）**。所以選點時要檢查。

**檢查共線** [▶ 46:16](https://youtu.be/W8vgVoQdwAM?t=2776)：兩點求線 $\mathbf{l}=\mathbf{x}_1\times\mathbf{x}_2$，第三點代入 $\mathbf{l}^\mathsf{T}\mathbf{x}_3$：等於 0 就共線，不等於 0 就不共線。

⚠️ 逐字稿缺字 [▶ 46:50](https://youtu.be/W8vgVoQdwAM?t=2810)：講者說「不等於 0 表示三點 not equals to 0」，應為「三點**不共線**」。

**來源差異**：MVG §4.1.3 的分析更細：

- 若 $\mathbf{x}_1,\mathbf{x}_2,\mathbf{x}_3$ 共線（在線 $\mathbf{l}$ 上），$H^*=\mathbf{x}_4'\mathbf{l}^\mathsf{T}$ 一定滿足那 8 條方程式（因為 $H^*\mathbf{x}_i=\mathbf{x}_4'(\mathbf{l}^\mathsf{T}\mathbf{x}_i)=\mathbf{0}$，$i=1,2,3$；$H^*\mathbf{x}_4\propto\mathbf{x}_4'$）。但它 rank 1，不是合法的射影變換。
- 若對應點 $\mathbf{x}_1',\mathbf{x}_2',\mathbf{x}_3'$ **不**共線：$H^*$ 是唯一解，不存在合法的 $H$（射影變換必須保持共線）。
- 若對應點也共線：還有其他解，解是一個 2 維族 $\alpha H^*+\beta H$，8 條方程式不獨立。
- 所以「解不存在」和「解不唯一」兩種情況都有；講者的說法是兩者的統稱。

---

## 4. 資料正規化

### 4.1 問題：病態矩陣

[▶ 46:56](https://youtu.be/W8vgVoQdwAM?t=2816)

**例子** [▶ 47:32](https://youtu.be/W8vgVoQdwAM?t=2852)：$\mathbf{x}=(x,y,w)=(100,100,1)$，$\mathbf{x}'$ 也是幾百、幾百、1。代進 $A_i$：

- 有些行是幾百的量級（例如 $w'\mathbf{x}^\mathsf{T}$ 的 $x,y$），
- 有些行是 1 的量級（例如 $w'w$），
- 有些行是兩個幾百相乘，$10^4$ 的量級（例如 $y'x$）。

這種各行量級差很多的矩陣叫**病態（ill-conditioned）**，會讓 SVD 的結果很糟。講者說證明超出本課範圍。

⚠️ 逐字稿缺字：Whisper 把 ill-conditioned 寫成 “U condition”。

**實驗** [▶ 49:03](https://youtu.be/W8vgVoQdwAM?t=2943)：

- 一張圖上選 5 個點，每次加上標準差 0.1 像素的高斯雜訊，做 100 次。
- 每次用這 5 點算 $H$，把點轉移到另一張圖。
- **沒正規化**：100 次轉移出來的點分布**很散**（誤差大）。
- **正規化後**：分布**很集中**（誤差小）。

### 4.2 怎麼正規化

[▶ 51:41](https://youtu.be/W8vgVoQdwAM?t=3101)

對每張圖的點各做一次相似變換：

1. **平移**：讓所有點的**重心（centroid）**移到原點。
2. **縮放**：整體縮放，讓所有點到原點的**平均距離是 $\sqrt{2}$**。

- 兩張圖**分別**做（各自有自己的重心和尺度）。
- 為什麼是 $\sqrt{2}$ [▶ 53:02](https://youtu.be/W8vgVoQdwAM?t=3182)：這樣「平均的點」大約是 $(1,1,1)^\mathsf{T}$，到原點距離 $\sqrt{1^2+1^2}=\sqrt{2}$。所有座標都在 1 的量級，$A$ 的各行就沒有量級差。

**正規化矩陣** [▶ 55:00](https://youtu.be/W8vgVoQdwAM?t=3300)：

$$
T_{\text{norm}}=\begin{pmatrix} s & 0 & -sc_x\\ 0 & s & -sc_y\\ 0&0&1\end{pmatrix},\qquad s=\frac{\sqrt{2}}{\bar{d}}
$$

- $(c_x,c_y)$：重心。
- $\bar{d}$：所有點到重心的平均距離。

> 以下**不是逐字稿內容**：逐字稿只說「這是正規化矩陣」「$s=\sqrt{2}/\bar{d}$」「先算重心 $c_x,c_y$」；矩陣元素是依「先平移 $-c$、再縮放 $s$」重建的。驗證：$T_{\text{norm}}(c_x,c_y,1)^\mathsf{T}=(sc_x-sc_x,\ sc_y-sc_y,\ 1)=(0,0,1)$，重心被送到原點。

⚠️ 逐字稿缺字 [▶ 55:00](https://youtu.be/W8vgVoQdwAM?t=3300)：講者說「three by one transformation matrix」，應為 $3\times3$。[▶ 55:55](https://youtu.be/W8vgVoQdwAM?t=3355) 「mean average distance is going to be 111」應為 $\sqrt{2}$（對應平均點 $(1,1,1)$）。

【課本補充】MVG §4.4：正規化不只是數值技巧。沒正規化的 DLT 結果會隨影像座標系的選擇而變（**不具不變性**）；正規化之後，結果和原始座標系無關。

### 4.3 正規化 DLT 演算法

[▶ 53:25](https://youtu.be/W8vgVoQdwAM?t=3205)

**在解什麼**：同 DLT，但結果穩定、準確。講者強調：**正規化不是選用的，是必要的**。

**步驟**（MVG Algorithm 4.2）：

1. **正規化**：
   - 第一張圖：算 $T$（重心、平均距離），$\tilde{\mathbf{x}}_i=T\mathbf{x}_i$。
   - 第二張圖：另算 $T'$，$\tilde{\mathbf{x}}_i'=T'\mathbf{x}_i'$。
   - $T\neq T'$：兩張圖的點分布不同（已經過 homography），重心和尺度不一樣。
2. **DLT**：用 $\tilde{\mathbf{x}}_i\leftrightarrow\tilde{\mathbf{x}}_i'$ 算 $\tilde{H}$。
3. **反正規化**：
$$
H=T'^{-1}\tilde{H}T
$$

> 以下**不是逐字稿內容**，是反正規化公式的推導（逐字稿只說「把這個變換套到 $\tilde{H}$ 上」）：$\tilde{\mathbf{x}}'=\tilde{H}\tilde{\mathbf{x}}$ → $T'\mathbf{x}'=\tilde{H}T\mathbf{x}$ → $\mathbf{x}'=T'^{-1}\tilde{H}T\mathbf{x}$。

**什麼時候會失敗**：

- 4 點中有 3 點共線（退化）。
- 點有大量**錯誤對應（outliers）**——DLT 是最小平方，一個錯得離譜的對應就能把結果拉歪。這要靠下一集的 **RANSAC**。
- 不做正規化 → 病態矩陣 → 結果不穩。

---

## 5. 一頁速查表

### homography 存在

| 情況 | $H$ | 關鍵一步 |
|---|---|---|
| 場景是平面 $\mathbf{n}^\mathsf{T}\mathbf{X}_1=d$ | $R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}$ | $\frac{1}{d}\mathbf{n}^\mathsf{T}\mathbf{X}_1=1$ 乘在 $\mathbf{t}$ 上 |
| 場景在 $\boldsymbol{\pi}_\infty$（很遠） | $R$ | $d\to\infty$ |
| 相機純旋轉 | $R$ | $\mathbf{t}=\mathbf{0}$ |

### DLT

| 項目 | 內容 |
|---|---|
| 自由度 / 每對點約束 / 最少點數 | 8 / 2 / 4 |
| 約束 | $\mathbf{x}_i'\times H\mathbf{x}_i=\mathbf{0}$ → $A_i\mathbf{h}=\mathbf{0}$，$A_i$ 取 $\begin{pmatrix}\mathbf{0}^\mathsf{T}&-w'\mathbf{x}^\mathsf{T}&y'\mathbf{x}^\mathsf{T}\\w'\mathbf{x}^\mathsf{T}&\mathbf{0}^\mathsf{T}&-x'\mathbf{x}^\mathsf{T}\end{pmatrix}$ |
| 第三列多餘 | $x'(\text{列1})+y'(\text{列2})=-w'(\text{列3})$ |
| 最小平方 | $\min\|A\mathbf{h}\|$ s.t. $\|\mathbf{h}\|=1$ |
| 解 | $\mathbf{h}=\mathbf{v}_9$（$V$ 的最後一行）；關鍵一步 $\|A\mathbf{h}\|^2=\sum c_i^2\sigma_i^2\ge\sigma_9^2$ |
| 退化 | 3 點共線；檢查 $(\mathbf{x}_1\times\mathbf{x}_2)^\mathsf{T}\mathbf{x}_3=0$ |

### 正規化（必要）

- $T=\begin{pmatrix}s&0&-sc_x\\0&s&-sc_y\\0&0&1\end{pmatrix}$，$s=\sqrt{2}/\bar{d}$：重心到原點、平均距離 $\sqrt{2}$。
- 兩張圖各自算 $T$、$T'$。
- 反正規化 $H=T'^{-1}\tilde{H}T$。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| DLT 只最小化代數誤差 | 第 09 集（代數誤差 vs. 幾何誤差 vs. Sampson 誤差） |
| 最小解、錯誤對應 | 第 09 集（RANSAC） |
| $H=R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}$ | 第 16–19 集（從 homography 分解出 $R,\mathbf{t}$）；第 10–12 集（加上內參 $K$） |
| 外積技巧 $\mathbf{x}\times P\mathbf{X}=0$ → DLT | 第 10–12 集（用 DLT 估計相機矩陣 $P$）；第 16–19 集（三角化） |
| SVD 求零空間、資料正規化 | 第 16–19 集（8 點法求 $F$，也要正規化） |
| 純旋轉 → homography | 第 10–12 集（純旋轉相機的校正） |

---

## 附：本集一句話總結

> **只有「場景是平面」或「場景極遠／相機純旋轉」時，兩張照片才由一個 homography $H=R+\frac{1}{d}\mathbf{t}\mathbf{n}^\mathsf{T}$ 連起來；估計它用 DLT：每對點經外積 $\mathbf{x}'\times H\mathbf{x}=0$ 給兩條線性方程式，4 對以上疊成 $A\mathbf{h}=0$，取 SVD 最小奇異值的右奇異向量——而且一定要先把兩張圖的點各自正規化（重心到原點、平均距離 $\sqrt{2}$）。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 4 (Part 1) 錄影逐字稿（Whisper `medium.en`，56:48）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §4.1、§4.4、Result 13.1 整理。*
