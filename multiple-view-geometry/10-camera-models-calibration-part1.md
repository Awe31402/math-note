---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 10
lecture: Lecture 5 (Part 1) – Camera models and calibration
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/sae97GVUXcg
notes: MVG §6.1–6.2.1（書頁 153–163，PDF 頁 171–181）
---

# 第 10 集 · Lecture 5 (Part 1)：針孔相機模型、投影矩陣的解剖 [▶ 影片](https://youtu.be/sae97GVUXcg)

← 上一集：[09-robust-homography-part2](09-robust-homography-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[11-camera-models-calibration-part2](11-camera-models-calibration-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 10 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（1:00:19，Whisper `medium.en` 轉錄）＋ MVG §6.1–6.2.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 中心投影相機的兩大類](#1-中心投影相機的兩大類)
- [2. 基本針孔模型](#2-基本針孔模型)
  - [2.1 相似三角形](#21-相似三角形)
  - [2.2 名詞：相機中心、主軸、主點、主平面](#22-名詞相機中心主軸主點主平面)
  - [2.3 寫成矩陣：P = diag(f,f,1)[I | 0]](#23-寫成矩陣p--diagff1i--0)
- [3. 主點偏移：內參矩陣 K](#3-主點偏移內參矩陣-k)
- [4. 世界座標系：外參 R、t](#4-世界座標系外參-rt)
  - [4.1 推導 P = KR[I | −C̃]](#41-推導-p--kri--c)
  - [4.2 旋轉矩陣的性質](#42-旋轉矩陣的性質)
  - [4.3 內參、外參、自由度](#43-內參外參自由度)
- [5. 非正方形像素與斜切：11 個自由度](#5-非正方形像素與斜切11-個自由度)
- [6. 有限射影相機的解剖](#6-有限射影相機的解剖)
  - [6.1 P = M[I | M⁻¹p₄]](#61-p--mi--mp)
  - [6.2 相機中心 = P 的零空間](#62-相機中心--p-的零空間)
  - [6.3 P 的行：消失點、世界原點的像](#63-p-的行消失點世界原點的像)
  - [6.4 P 的列：主平面、軸平面](#64-p-的列主平面軸平面)
  - [6.5 主點與主軸方向](#65-主點與主軸方向)
  - [6.6 總表](#66-總表)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/sae97GVUXcg?t=0)

Lecture 5 的目標（三集合起來）：

| 目標 | 本集？ | 來源 |
|---|---|---|
| 用**針孔相機模型**描述相機投影 | ✅ | MVG §6.1 |
| 從投影矩陣找出相機中心、主平面、主點、主軸 | ✅ | MVG §6.2.1 |
| 用投影矩陣做點的前向、反向投影 | 第 11 集 | MVG §6.2.2 |
| 仿射相機的性質 | 第 11 集 | MVG §6.3 |
| 校正：求投影相機的內參、外參 | 第 11–12 集 | Zhang (2000) |

講者說內容取自 MVG 第 6 章、Ma Yi 書第 3 章，以及 Zhang Zhengyou〈A Flexible New Technique for Camera Calibration〉（T-PAMI 2000）。

**回顧** [▶ 01:18](https://youtu.be/sae97GVUXcg?t=78)：之前看了 $\mathbb{P}^2\to\mathbb{P}^2$、$\mathbb{P}^3\to\mathbb{P}^3$ 的變換。今天看**投影矩陣**：把 $\mathbb{P}^3$ 的幾何物件映到 $\mathbb{P}^2$。

---

## 1. 中心投影相機的兩大類

[▶ 02:23](https://youtu.be/sae97GVUXcg?t=143)

**中心投影（central projection）**：所有投影到影像平面的光線都**收斂到同一個投影中心**。

| 類別 | 相機中心 $C$ | 代表模型 |
|---|---|---|
| 有限中心 | 在 $\mathbb{R}^3$ 中有有限座標 | **射影相機（projective camera）** |
| 無窮遠中心 | 在無窮遠平面 $\boldsymbol{\pi}_\infty$ 上 | **仿射相機（affine camera）**（第 11 集） |

射影相機可以用最基本的**針孔相機模型（pinhole camera model）**定義。

---

## 2. 基本針孔模型

### 2.1 相似三角形

[▶ 03:53](https://youtu.be/sae97GVUXcg?t=233)

**設定**：

- 歐氏座標系：$x$、$y$ 軸，$z$ 軸朝外；投影中心 $C$ 在原點。
- **影像平面（image plane）**，也叫**焦平面（focal plane）**：平行於 $xy$ 平面，在 $z=f$ 處。$f$ 是**焦距（focal length）**。
- 3D 點 $\mathbf{X}$ 和 $C$ 連成光線，光線和影像平面的交點就是像點 $\mathbf{x}$。

**從側面看**（相似三角形）[▶ 05:14](https://youtu.be/sae97GVUXcg?t=314)：

- 大三角形：底 $Z$、高 $Y$（3D 點的座標）。
- 小三角形：底 $f$、高 = 像點的 $y$ 座標。
- 相似 → 小高 $=\dfrac{f}{Z}\cdot Y$。

同理 $x$ 方向：$fX/Z$。所以

$$
(X,Y,Z)^\mathsf{T}\ \longmapsto\ \left(\frac{fX}{Z},\ \frac{fY}{Z}\right)^\mathsf{T}
$$

（第三個座標永遠是 $f$，投影到 2D 時忽略。）

### 2.2 名詞：相機中心、主軸、主點、主平面

[▶ 06:51](https://youtu.be/sae97GVUXcg?t=411)

| 名詞 | 意義 |
|---|---|
| **相機中心（camera center）**／**光學中心（optical center）** | 所有光線交會的點 |
| **主軸（principal axis）** | 座標系的 $z$ 軸，垂直於影像平面 |
| **主點（principal point）** | 主軸和影像平面的交點 |
| **主平面（principal plane）** | 過相機中心、平行於影像平面的平面（就是 $xy$ 平面） |

### 2.3 寫成矩陣：P = diag(f,f,1)[I | 0]

[▶ 07:52](https://youtu.be/sae97GVUXcg?t=472)

用齊次座標，投影變成**線性映射**：

1. 3D 點加 1：$(X,Y,Z,1)^\mathsf{T}$。
2. 像點 $\left(\frac{fX}{Z},\frac{fY}{Z}\right)$ 把共同分母 $Z$ 放到第三個分量：齊次座標 $(fX,fY,Z)^\mathsf{T}$。
3. 寫成矩陣乘法：
$$
\begin{pmatrix}fX\\fY\\Z\end{pmatrix}=\begin{pmatrix}f&0&0&0\\0&f&0&0\\0&0&1&0\end{pmatrix}\begin{pmatrix}X\\Y\\Z\\1\end{pmatrix}
=\underbrace{\begin{pmatrix}f&&\\&f&\\&&1\end{pmatrix}}_{3\times3}\underbrace{\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}}_{[I\mid\mathbf{0}],\ 3\times4}\begin{pmatrix}X\\Y\\Z\\1\end{pmatrix}
$$

簡寫：

$$
\mathbf{x}=P\mathbf{X}
$$

- $\mathbf{x}$：$3\times1$ 齊次像點。
- $\mathbf{X}$：$4\times1$ 齊次 3D 點。
- $P$：$3\times4$ 齊次矩陣，叫**相機投影矩陣（camera projection matrix）**。

---

## 3. 主點偏移：內參矩陣 K

[▶ 11:03](https://youtu.be/sae97GVUXcg?t=663)

- 上面假設影像座標原點在主點（通常是影像中心）。
- 實際上影像原點可以在任何地方，例如**影像的一個角**。這時主點在影像座標裡是 $(p_x,p_y)$。
- 要補償這個平移：
$$
(X,Y,Z)^\mathsf{T}\ \longmapsto\ \left(\frac{fX}{Z}+p_x,\ \frac{fY}{Z}+p_y\right)^\mathsf{T}
$$

**齊次形式** [▶ 12:35](https://youtu.be/sae97GVUXcg?t=755)：

$$
\begin{pmatrix}fX+Zp_x\\fY+Zp_y\\Z\end{pmatrix}=\begin{pmatrix}f&0&p_x&0\\0&f&p_y&0\\0&0&1&0\end{pmatrix}\begin{pmatrix}X\\Y\\Z\\1\end{pmatrix}
$$

**分解** [▶ 13:17](https://youtu.be/sae97GVUXcg?t=797)：

$$
\mathbf{x}=K[I\mid\mathbf{0}]\mathbf{X}_{\text{cam}},\qquad K=\begin{pmatrix}f&0&p_x\\0&f&p_y\\0&0&1\end{pmatrix}
$$

- $K$ 叫**相機校正矩陣（camera calibration matrix）**，也常叫**相機內參矩陣（camera intrinsic matrix）**。
- 主點出現在 $K$ 的第三行。

---

## 4. 世界座標系：外參 R、t

### 4.1 推導 P = KR[I | −C̃]

[▶ 14:09](https://youtu.be/sae97GVUXcg?t=849)

- 上面的 3D 點是用**相機座標系**表示的。
- 實際上 3D 點常用某個任意的**世界座標系（world frame）**表示。相機座標系和世界座標系之間差一個剛體變換。

**符號**：

- $\tilde{\mathbf{C}}$：相機中心在世界座標系中的非齊次座標。
- $R$：世界座標系到相機座標系的旋轉（相機座標系的方向不一定和世界座標系對齊）。
- $\mathbf{X}=(X,Y,Z,1)^\mathsf{T}$：世界座標系中的 3D 點。

**把世界座標換成相機座標** [▶ 17:09](https://youtu.be/sae97GVUXcg?t=1029)：一個等距變換（第 02 集），旋轉 $R$、平移 $-R\tilde{\mathbf{C}}$：

$$
\mathbf{X}_{\text{cam}}=\begin{pmatrix}R & -R\tilde{\mathbf{C}}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\mathbf{X}
$$

> 以下**不是逐字稿內容**，是平移項的直覺：非齊次寫法 $\tilde{\mathbf{X}}_{\text{cam}}=R(\tilde{\mathbf{X}}-\tilde{\mathbf{C}})$——先把點相對相機中心平移，再轉到相機的方向。檢查：相機中心自己 $\tilde{\mathbf{X}}=\tilde{\mathbf{C}}$ 被送到相機座標原點。

**代進投影式** [▶ 17:58](https://youtu.be/sae97GVUXcg?t=1078)：

$$
\mathbf{x}=K[I\mid\mathbf{0}]\begin{pmatrix}R & -R\tilde{\mathbf{C}}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\mathbf{X}=K[R\mid -R\tilde{\mathbf{C}}]\mathbf{X}
$$

- $[I\mid\mathbf{0}]$ 的最後一行是 0，把等距矩陣的最後一列消掉。
- 把兩處的 $R$ 提出來 [▶ 26:16](https://youtu.be/sae97GVUXcg?t=1576)：

$$
\boxed{\ P=KR[I\mid-\tilde{\mathbf{C}}]\ }
$$

**更方便的寫法** [▶ 30:54](https://youtu.be/sae97GVUXcg?t=1854)：令 $\mathbf{t}=-R\tilde{\mathbf{C}}$，

$$
P=K[R\mid\mathbf{t}]
$$

### 4.2 旋轉矩陣的性質

[▶ 18:52](https://youtu.be/sae97GVUXcg?t=1132)

講者複習第 03 集：

- 旋轉矩陣是歐拉角（roll、pitch、yaw，3 個自由度）的**過度參數化（over-parameterization）**：9 個元素，只有 3 個自由度。
- 例如先繞 $z$（yaw，$\gamma$）、再繞 $y$（pitch）、最後繞 $x$（roll），串起來可以表示任何 3D 旋轉。
- 2D 旋轉矩陣（$2\times2$）只有 **1** 個自由度：平面內只能繞一個軸轉（yaw）。3D（$3\times3$）有 **3** 個。

**性質** [▶ 21:41](https://youtu.be/sae97GVUXcg?t=1301)：

1. $\det R=\pm1$，看座標系怎麼定：
   - **右手座標系**：四指從 $x$ 掃到 $y$，大拇指指 $z$。通常用這個。行列式 **+1**。
   - **左手座標系**：$x$、$y$ 方向一樣時，$z$ 指相反方向。行列式 **−1**。
2. **單位正交（orthonormal）**：$R^\mathsf{T}=R^{-1}$。
3. 各行兩兩垂直、長度 1：
   - 第一行定義 $x$ 軸、第二行定義 $y$ 軸、第三行定義 $z$ 軸。
   - 任一行 = 另兩行的外積（例如 $\mathbf{r}_3=\mathbf{r}_1\times\mathbf{r}_2$）。
   - 任兩行內積為 0。
4. 所以：**旋轉矩陣的三行就是座標系的基底**。

⚠️ 逐字稿缺字 [▶ 23:21](https://youtu.be/sae97GVUXcg?t=1401)：講者說「用**右手**座標系定義的旋轉矩陣行列式永遠是 −1」，應為**左手**。另外 Whisper 把 orthonormal 寫成 “octonormal”。

> 以下**不是逐字稿內容**：依第 03 集的定義，$SO(3)$ 的旋轉矩陣一律 $\det=+1$；$\det=-1$ 的正交矩陣包含一次鏡射（把右手系變成左手系），嚴格說不叫旋轉。

### 4.3 內參、外參、自由度

[▶ 27:16](https://youtu.be/sae97GVUXcg?t=1636)

$$
P=\underbrace{K}_{\text{內參}}\ \underbrace{R[I\mid-\tilde{\mathbf{C}}]}_{\text{外參}}
$$

| | 參數 | 為什麼這樣叫 |
|---|---|---|
| **內參（intrinsics）**／內部相機參數 | $K$ 裡的 $f,p_x,p_y$ | 在相機座標系下就定義好了，只和相機本身有關，不依賴世界座標系 |
| **外參（extrinsics）**／外部參數 | $R$、$\tilde{\mathbf{C}}$（或 $\mathbf{t}$） | 需要世界座標系才能定義 |

**自由度（目前的模型）** [▶ 28:05](https://youtu.be/sae97GVUXcg?t=1685)：$K$ 3 個（$f,p_x,p_y$）+ $R$ 3 個 + $\tilde{\mathbf{C}}$ 3 個 = **9**。

---

## 5. 非正方形像素與斜切：11 個自由度

[▶ 31:41](https://youtu.be/sae97GVUXcg?t=1901)

- 到目前為止假設像素是**正方形**。
- 製造誤差（鏡頭或感光元件）可能讓像素不是完美的正方形，$x$ 方向還可能有**斜切（skew）**。
- 補償兩件事：
  1. **兩個方向不同的焦距** $f_x$、$f_y$。
  2. $x$ 方向的**斜切參數** $s$。

$$
K=\begin{pmatrix}f_x & s & p_x\\ 0 & f_y & p_y\\ 0&0&1\end{pmatrix}
$$

（矩陣元素依 MVG 式 (6.10) 的位置寫出；逐字稿只說「$f_x$、$f_y$ 取代同一個焦距，加上 $x$ 方向的 $s$，主點不變」。）

**總自由度** [▶ 33:54](https://youtu.be/sae97GVUXcg?t=2034)：

| 部分 | 參數 | 自由度 |
|---|---|---|
| 內參 $K$ | $f_x,f_y,s,p_x,p_y$ | 5 |
| 旋轉 $R$ | 3 個歐拉角 | 3 |
| 平移 $\mathbf{t}$ | $t_x,t_y,t_z$ | 3 |
| **合計** | | **11** |

$$
P=K[R\mid\mathbf{t}]
$$

> 以下**不是逐字稿內容**，是自由度的另一個看法：$P$ 是 $3\times4$ 齊次矩陣，12 個元素少 1 個縮放，正好 11。所以一般的（左邊 $3\times3$ 非奇異）$P$ 都可以寫成這種形式。

【課本補充】（MVG §6.1）

- 不同焦距的物理來源：CCD 像素在兩個方向的密度不同，$m_x$、$m_y$（每單位長度的像素數）。$\alpha_x=fm_x$、$\alpha_y=fm_y$ 是以像素為單位的焦距（課堂寫成 $f_x,f_y$）。
- 一般相機的斜切 $s$ 通常是 0。

---

## 6. 有限射影相機的解剖

### 6.1 P = M[I | M⁻¹p₄]

[▶ 34:57](https://youtu.be/sae97GVUXcg?t=2097)

**有限射影相機**：中心投影、相機中心 $C$ 在世界座標系中有**有限**座標。

把 $P$ 寫成四行 $P=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_3\ \mathbf{p}_4]$，令 $M=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_3]$（左邊 $3\times3$）：

$$
P=[M\mid\mathbf{p}_4]=M\left[I\mid M^{-1}\mathbf{p}_4\right]
$$

- 乘回去：$M\cdot I=M$，$M\cdot M^{-1}\mathbf{p}_4=\mathbf{p}_4$。只是重新分解。
- 對有限相機，**$M$ 必須非奇異**，才有有限的相機中心。

> 以下**不是逐字稿內容**，是和 4.1 對照：$P=KR[I\mid-\tilde{\mathbf{C}}]$，所以 $M=KR$、$\mathbf{p}_4=-KR\tilde{\mathbf{C}}$。$K$ 和 $R$ 都可逆，所以 $M$ 可逆。

### 6.2 相機中心 = P 的零空間

[▶ 37:18](https://youtu.be/sae97GVUXcg?t=2238)

$$
P\mathbf{C}=\mathbf{0}
$$

- 意思：相機中心投影到沒有定義的點 $(0,0,0)^\mathsf{T}$。

**證明概要** [▶ 37:57](https://youtu.be/sae97GVUXcg?t=2277)：

1. 取一條通過相機中心 $\mathbf{C}$ 和任一點 $\mathbf{A}$ 的線——這就是一條投射到相機的**光線**。線上的點是 $\mathbf{X}(\lambda)=\lambda\mathbf{A}+(1-\lambda)\mathbf{C}$（第 04 集：兩點的張成）。
2. 投影：
$$
\mathbf{x}=P\mathbf{X}(\lambda)=\lambda P\mathbf{A}+(1-\lambda)P\mathbf{C}
$$
3. 這條光線上的**每一點**都投影到同一個像點 $P\mathbf{A}$（它們在同一條光線上）。
4. 要讓上式對所有 $\lambda$ 都等於 $P\mathbf{A}$（差縮放），第二項必須是 0 → $P\mathbf{C}=\mathbf{0}$。∎

（$\mathbf{X}(\lambda)$ 的參數化依 MVG §6.2.1 補上；逐字稿只說「由 $\mathbf{A}$、$\mathbf{C}$ 張成」。）

**公式** [▶ 57:23](https://youtu.be/sae97GVUXcg?t=3443)：

$$
\mathbf{C}=\begin{pmatrix}-M^{-1}\mathbf{p}_4\\ 1\end{pmatrix}
$$

**驗證**：$P\mathbf{C}=[M\mid\mathbf{p}_4]\begin{pmatrix}-M^{-1}\mathbf{p}_4\\1\end{pmatrix}=-MM^{-1}\mathbf{p}_4+\mathbf{p}_4=\mathbf{0}$ ✓

- 講者預告：之後看**無窮遠相機**時，$M$ 不可逆，相機中心在無窮遠，公式不同（第 11 集）。

### 6.3 P 的行：消失點、世界原點的像

[▶ 40:16](https://youtu.be/sae97GVUXcg?t=2416)

**前三行 = 世界座標軸方向的消失點**：

- 世界 $z$ 軸方向的無窮遠點是 $\mathbf{D}=(0,0,1,0)^\mathsf{T}$（最後一個分量 0 → 理想點；前三個是 $z$ 方向）。
- 投影：
$$
P\begin{pmatrix}0\\0\\1\\0\end{pmatrix}=[\mathbf{p}_1\ \mathbf{p}_2\ \mathbf{p}_3\ \mathbf{p}_4]\begin{pmatrix}0\\0\\1\\0\end{pmatrix}=\mathbf{p}_3
$$
- 所以 $\mathbf{p}_3$ 是 $z$ 軸的**消失點**。同理 $\mathbf{p}_1$（$x$ 軸，$(1,0,0,0)^\mathsf{T}$）、$\mathbf{p}_2$（$y$ 軸）。

**第四行 = 世界原點的像** [▶ 42:49](https://youtu.be/sae97GVUXcg?t=2569)：

$$
P\begin{pmatrix}0\\0\\0\\1\end{pmatrix}=\mathbf{p}_4
$$

### 6.4 P 的列：主平面、軸平面

[▶ 43:32](https://youtu.be/sae97GVUXcg?t=2612)

把 $P$ 寫成三列：$P=\begin{pmatrix}\mathbf{P}^{1\mathsf{T}}\\ \mathbf{P}^{2\mathsf{T}}\\ \mathbf{P}^{3\mathsf{T}}\end{pmatrix}$，每個 $\mathbf{P}^i$ 是 4 維向量——**都代表一個世界平面**。

**第三列 = 主平面** [▶ 44:06](https://youtu.be/sae97GVUXcg?t=2646)：

1. 主平面包含相機中心、平行於影像平面。主平面上的點，投影後會落在影像的**無窮遠線**上：
$$
P\mathbf{X}=\begin{pmatrix}x\\y\\0\end{pmatrix}
$$
2. 第三個分量是 $\mathbf{P}^{3\mathsf{T}}\mathbf{X}=0$。
3. 這正是「$\mathbf{X}$ 在平面 $\mathbf{P}^3$ 上」的關聯關係。
4. 所有主平面上的點都滿足它 → $\mathbf{P}^3$ **就是主平面**。

**第一、二列 = 軸平面（axis planes）** [▶ 46:13](https://youtu.be/sae97GVUXcg?t=2773)：

- $\mathbf{P}^1$：包含相機中心、以及影像上 $x=0$ 那條線（影像的 $y$ 軸）的平面。
- $\mathbf{P}^2$：包含相機中心、以及影像上 $y=0$ 那條線（影像的 $x$ 軸）的平面。

**證明（以 $\mathbf{P}^2$ 為例）** [▶ 47:24](https://youtu.be/sae97GVUXcg?t=2844)：

1. **平面上的點投影到 $y=0$**：設 $\mathbf{X}$ 在 $\mathbf{P}^2$ 上，$\mathbf{P}^{2\mathsf{T}}\mathbf{X}=0$。則
$$
P\mathbf{X}=\begin{pmatrix}\mathbf{P}^{1\mathsf{T}}\mathbf{X}\\ \mathbf{P}^{2\mathsf{T}}\mathbf{X}\\ \mathbf{P}^{3\mathsf{T}}\mathbf{X}\end{pmatrix}=\begin{pmatrix}x\\0\\w\end{pmatrix}
$$
   第二個分量是 0 → 像點在影像的 $x$ 軸（$y=0$）上。
2. **平面包含相機中心**：$P\mathbf{C}=\mathbf{0}$ → 每一列乘 $\mathbf{C}$ 都是 0 → $\mathbf{P}^{2\mathsf{T}}\mathbf{C}=0$ → $\mathbf{C}$ 在 $\mathbf{P}^2$ 上。∎

⚠️ 逐字稿缺字 [▶ 49:28](https://youtu.be/sae97GVUXcg?t=2968)：講者說「undefined point of one zero zero zero」，應為 $(0,0,0)^\mathsf{T}$。

### 6.5 主點與主軸方向

**主點** [▶ 50:46](https://youtu.be/sae97GVUXcg?t=3046)：

1. 第三列 $\mathbf{P}^3$ 是主平面。平面的前三個分量是**法向量**（第 04 集）。
2. 主軸垂直於主平面 → 主軸方向就是 $\mathbf{P}^3$ 的前三個分量，記作 $\hat{\mathbf{p}}^3$。
3. 把它當成無窮遠點 $(\hat{\mathbf{p}}^3,0)^\mathsf{T}$，它的像就是**主點**：
$$
\mathbf{x}_0=P\begin{pmatrix}\hat{\mathbf{p}}^3\\0\end{pmatrix}=M\mathbf{m}^3
$$
   $\mathbf{m}^{3\mathsf{T}}$ 是 $M$ 的第三列（$=\hat{\mathbf{p}}^{3\mathsf{T}}$）。

**主軸方向（決定哪一側在相機前方）** [▶ 53:14](https://youtu.be/sae97GVUXcg?t=3194)：

- 數學上，$P$ 能把空間中**所有**點投影到影像上；但實際上只有**相機前方那一半**的點看得到。
- 用**主軸向量**區分前後：
$$
\mathbf{v}=\det(M)\,\mathbf{m}^3
$$
- $\mathbf{m}^3$ 本身只確定到差一個**正負號**（$P$ 乘 $-1$ 還是同一個相機），不知道朝前還是朝後。
- $\det M$ 的正負號解決這個模糊。講者的直覺：$\det M$ 可以看成「$\mathbf{m}^1\times\mathbf{m}^2$ 再和 $\mathbf{m}^3$ 內積」的有號體積，正負號告訴你方向。

> 以下**不是逐字稿內容**，是為什麼 $\det(M)\mathbf{m}^3$ 不受 $P$ 的正負號影響（MVG §6.2.1）：$P\to-P$ 時 $\mathbf{m}^3\to-\mathbf{m}^3$，$\det M\to(-1)^3\det M=-\det M$，乘起來不變。驗證：$P=K[I\mid\mathbf{0}]$ 時 $M=K$、$\det K>0$、$\mathbf{m}^3=(0,0,1)^\mathsf{T}$，所以 $\mathbf{v}=(0,0,\det K)^\mathsf{T}$ 指向 $+z$，也就是相機前方。

### 6.6 總表

[▶ 57:14](https://youtu.be/sae97GVUXcg?t=3434)

（MVG Table 6.1；$P=[M\mid\mathbf{p}_4]$）

| 物件 | 怎麼從 $P$ 取得 |
|---|---|
| 相機中心 | $P\mathbf{C}=\mathbf{0}$；有限相機 $\mathbf{C}=\begin{pmatrix}-M^{-1}\mathbf{p}_4\\1\end{pmatrix}$；無窮遠相機 $\mathbf{C}=\begin{pmatrix}\mathbf{d}\\0\end{pmatrix}$，$M\mathbf{d}=\mathbf{0}$ |
| 世界軸的消失點 | 行 $\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3$ |
| 世界原點的像 | 行 $\mathbf{p}_4$ |
| 主平面 | 列 $\mathbf{P}^3$ |
| 軸平面 | 列 $\mathbf{P}^1$（含 $x=0$ 線）、$\mathbf{P}^2$（含 $y=0$ 線） |
| 主點 | $\mathbf{x}_0=M\mathbf{m}^3$ |
| 主軸方向 | $\mathbf{v}=\det(M)\mathbf{m}^3$，指向相機前方 |

（無窮遠相機那一格的公式依 MVG Table 6.1 補上。）

---

## 7. 一頁速查表

### 投影矩陣

| 公式 | 關鍵一步 |
|---|---|
| 針孔：$(X,Y,Z)\mapsto(fX/Z,\ fY/Z)$ | 相似三角形 |
| $\mathbf{x}=K[I\mid\mathbf{0}]\mathbf{X}_{\text{cam}}$ | 共同分母 $Z$ 放到第三分量 |
| $K=\begin{pmatrix}f_x&s&p_x\\0&f_y&p_y\\0&0&1\end{pmatrix}$（5 dof） | 主點偏移、非方形像素、斜切 |
| $\mathbf{X}_{\text{cam}}=\begin{pmatrix}R&-R\tilde{\mathbf{C}}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}\mathbf{X}$ | $\tilde{\mathbf{X}}_{\text{cam}}=R(\tilde{\mathbf{X}}-\tilde{\mathbf{C}})$ |
| $P=KR[I\mid-\tilde{\mathbf{C}}]=K[R\mid\mathbf{t}]$，$\mathbf{t}=-R\tilde{\mathbf{C}}$ | 11 dof = 5 + 3 + 3 |

### 解剖（$P=[M\mid\mathbf{p}_4]$，$M=KR$）

| 物件 | 公式 | 關鍵一步 |
|---|---|---|
| 相機中心 | $\mathbf{C}=(-M^{-1}\mathbf{p}_4,1)^\mathsf{T}$ | 光線上的點都投影到同一點 → $P\mathbf{C}=0$ |
| 消失點 | $\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3$ | $P(1,0,0,0)^\mathsf{T}=\mathbf{p}_1$ |
| 原點的像 | $\mathbf{p}_4$ | $P(0,0,0,1)^\mathsf{T}$ |
| 主平面 | $\mathbf{P}^3$ | 主平面上的點投影到 $w=0$ |
| 軸平面 | $\mathbf{P}^1,\mathbf{P}^2$ | 平面上的點 $x$ 或 $y$ 座標為 0；含 $\mathbf{C}$ |
| 主點 | $M\mathbf{m}^3$ | 主軸方向的無窮遠點之像 |
| 主軸 | $\det(M)\mathbf{m}^3$ | 正負號解決前後模糊 |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $P=K[R\mid\mathbf{t}]$ | 第 11 集（前向、反向投影、分解 $P$ 得 $K,R,\mathbf{t}$）；整門課 |
| 內參 $K$ | 第 11–12 集（Zhang 校正法）；第 13–15 集（$\omega=(KK^\mathsf{T})^{-1}$）；第 16–19 集（$F=K'^{-\mathsf{T}}EK^{-1}$） |
| 相機中心 = 零空間 | 第 16–19 集（極點 $\mathbf{e}'=P'\mathbf{C}$） |
| $P$ 的行是消失點 | 第 13–15 集（單視角量測：從消失點求 $K$） |
| 無窮遠相機 | 第 11 集（仿射相機） |
| 外參 $R,\mathbf{t}$ | 第 20–22 集（絕對位姿 PnP） |

---

## 附：本集一句話總結

> **針孔相機用相似三角形得到 $(fX/Z,fY/Z)$，寫成齊次座標就是線性的 $\mathbf{x}=P\mathbf{X}$；加上主點、非方形像素、斜切和世界座標系，得到 $P=K[R\mid\mathbf{t}]$（5 個內參 + 6 個外參 = 11 dof）；而 $P$ 本身就寫著相機的一切：零空間是相機中心、前三行是消失點、第四行是原點的像、第三列是主平面、$M\mathbf{m}^3$ 是主點。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 5 (Part 1) 錄影逐字稿（Whisper `medium.en`，1:00:19）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §6.1–6.2.1 整理。*
