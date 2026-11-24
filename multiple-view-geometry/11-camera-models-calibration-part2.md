---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 11
lecture: Lecture 5 (Part 2) – Camera models and calibration
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/oyGCk4idsaU
notes: MVG §6.2.2–6.3.4（書頁 161–175，PDF 頁 179–193）；RQ 分解見 MVG 附錄 A4.1.1
---

# 第 11 集 · Lecture 5 (Part 2)：反向投影、深度、分解 P、仿射相機 [▶ 影片](https://youtu.be/oyGCk4idsaU)

← 上一集：[10-camera-models-calibration-part1](10-camera-models-calibration-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[12-camera-models-calibration-part3](12-camera-models-calibration-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 11 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（51:12，Whisper `medium.en` 轉錄）＋ MVG §6.2.2–6.3.4、附錄 A4.1.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 前向投影](#1-前向投影)
- [2. 反向投影：像點 → 光線](#2-反向投影像點--光線)
- [3. 點的深度](#3-點的深度)
- [4. 分解 P 得到 K、R、C](#4-分解-p-得到-krc)
  - [4.1 相機中心：SVD](#41-相機中心svd)
  - [4.2 K 和 R：RQ 分解](#42-k-和-rrq-分解)
- [5. 為什麼說相機是「射影」裝置](#5-為什麼說相機是射影裝置)
- [6. 仿射相機（無窮遠相機）](#6-仿射相機無窮遠相機)
  - [6.1 最後一列是 (0,0,0,1)](#61-最後一列是-0001)
  - [6.2 分解與自由度](#62-分解與自由度)
  - [6.3 為什麼叫「仿射」](#63-為什麼叫仿射)
  - [6.4 三種仿射相機](#64-三種仿射相機)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 射影相機對點的作用：前向投影、反向投影 | §6.2.2 |
| 點的深度（在相機前方還是後方） | §6.2.3 |
| 把 $P$ 分解成 $K$、$R$、$\mathbf{C}$ | §6.2.4、A4.1.1 |
| 歐氏 vs. 射影空間：相機是射影裝置 | §6.2.5 |
| 仿射相機：正交、縮放正交、弱透視 | §6.3 |

---

## 1. 前向投影

[▶ 00:00](https://youtu.be/oyGCk4idsaU?t=0)

- 3D 點 $\mathbf{X}$ 投影成像點：$\mathbf{x}=P\mathbf{X}$（$\mathbb{P}^3\to\mathbb{P}^2$）。
- 對無窮遠點 $\mathbf{D}=(\mathbf{d}^\mathsf{T},0)^\mathsf{T}$（$\mathbf{d}$ 是方向）：
$$
\mathbf{x}=P\mathbf{D}=[M\mid\mathbf{p}_4]\begin{pmatrix}\mathbf{d}\\0\end{pmatrix}=M\mathbf{d}
$$
- 最後一個分量是 0，所以 $P$ 的最後一行沒作用，**只有 $M$ 起作用**。結果就是方向 $\mathbf{d}$ 的**消失點**。

---

## 2. 反向投影：像點 → 光線

[▶ 02:09](https://youtu.be/oyGCk4idsaU?t=129)

**問題**：已知 $P$ 和影像上一點 $\mathbf{x}$，3D 點在哪裡？

- **不可能恢復確切位置**：$P$ 是 $3\times4$，不是滿秩方陣，**沒有反矩陣**。
- 能得到的是**一族解**：通過 $\mathbf{x}$ 和相機中心的**整條光線**。光線上任何一點都投影到同一個 $\mathbf{x}$。

**光線由兩點張成** [▶ 04:26](https://youtu.be/oyGCk4idsaU?t=266)：

1. **相機中心** $\mathbf{C}$：$P\mathbf{C}=\mathbf{0}$。
2. **另一點** $P^+\mathbf{x}$，$P^+$ 是 $P$ 的**偽逆（pseudo-inverse）**：
$$
P^+=P^\mathsf{T}(PP^\mathsf{T})^{-1}
$$

$$
\mathbf{X}(\lambda)=P^+\mathbf{x}+\lambda\mathbf{C}
$$

（偽逆公式和光線式依 MVG 式 (6.13) 寫出；逐字稿只說「偽逆由這個式子給出」。）

**驗證 $P^+\mathbf{x}$ 在光線上**：$P(P^+\mathbf{x})=PP^\mathsf{T}(PP^\mathsf{T})^{-1}\mathbf{x}=\mathbf{x}$ ✓。$P\mathbf{C}=\mathbf{0}$，所以 $P\mathbf{X}(\lambda)=\mathbf{x}$ 對所有 $\lambda$ 都成立。

講者把第二個點描述成「從相機中心指向像點的方向（理想點）」，並驗證它等於 $\begin{pmatrix}M^{-1}\mathbf{x}\\0\end{pmatrix}$：

$$
P\begin{pmatrix}M^{-1}\mathbf{x}\\0\end{pmatrix}=[M\mid\mathbf{p}_4]\begin{pmatrix}M^{-1}\mathbf{x}\\0\end{pmatrix}=MM^{-1}\mathbf{x}+\mathbf{0}=\mathbf{x}
$$

**來源差異**：MVG 把這兩個當成**兩種不同的寫法**：

- 一般相機：$\mathbf{X}(\lambda)=P^+\mathbf{x}+\lambda\mathbf{C}$。$P^+\mathbf{x}$ 一般**不是**無窮遠點。
- 有限相機（$M$ 可逆）：光線和 $\boldsymbol{\pi}_\infty$ 的交點是 $\mathbf{D}=\begin{pmatrix}M^{-1}\mathbf{x}\\0\end{pmatrix}$，於是
$$
\mathbf{X}(\mu)=\mu\begin{pmatrix}M^{-1}\mathbf{x}\\0\end{pmatrix}+\begin{pmatrix}-M^{-1}\mathbf{p}_4\\1\end{pmatrix}=\begin{pmatrix}M^{-1}(\mu\mathbf{x}-\mathbf{p}_4)\\1\end{pmatrix}
$$
- 講者把兩者合在一起講，說 $P^+\mathbf{x}$「是一個理想點、等於 $M^{-1}\mathbf{x}$」——依 MVG，理想點是 $(M^{-1}\mathbf{x},0)^\mathsf{T}$，不是 $P^+\mathbf{x}$。兩種寫法都給出同一條光線。

**相機中心** [▶ 06:36](https://youtu.be/oyGCk4idsaU?t=396)：$\mathbf{C}=\begin{pmatrix}-M^{-1}\mathbf{p}_4\\1\end{pmatrix}$，$P\mathbf{C}=-\mathbf{p}_4+\mathbf{p}_4=\mathbf{0}$（第 10 集）。

---

## 3. 點的深度

[▶ 07:44](https://youtu.be/oyGCk4idsaU?t=464)

**問題**：已知 3D 點 $\mathbf{X}=(X,Y,Z,T)^\mathsf{T}$ 和 $P$，求它的**深度**：$\mathbf{X}$ 投影到主軸上，離相機中心多遠。

$$
\operatorname{depth}(\mathbf{X};P)=\frac{\operatorname{sign}(\det M)\,w}{T\,\|\mathbf{m}^3\|}
$$

- $P\mathbf{X}=w(x,y,1)^\mathsf{T}$，$w$ 是像點的尺度。
- $\mathbf{m}^{3\mathsf{T}}$：$M$ 的第三列。

**證明**（設 $T=1$）[▶ 09:38](https://youtu.be/oyGCk4idsaU?t=578)：

1. **$w$ 是什麼**：$P\mathbf{X}=\begin{pmatrix}\mathbf{P}^{1\mathsf{T}}\mathbf{X}\\\mathbf{P}^{2\mathsf{T}}\mathbf{X}\\\mathbf{P}^{3\mathsf{T}}\mathbf{X}\end{pmatrix}=\begin{pmatrix}wx\\wy\\w\end{pmatrix}$，所以
$$
w=\mathbf{P}^{3\mathsf{T}}\mathbf{X}
$$
2. **減掉相機中心不影響**：$\mathbf{P}^{3\mathsf{T}}\mathbf{C}=0$（$\mathbf{C}$ 在零空間），所以
$$
w=\mathbf{P}^{3\mathsf{T}}(\mathbf{X}-\mathbf{C})
$$
3. **換成非齊次**：$\mathbf{X}=(\tilde{\mathbf{X}},1)^\mathsf{T}$、$\mathbf{C}=(\tilde{\mathbf{C}},1)^\mathsf{T}$，相減後最後一個分量是 0，$\mathbf{P}^3$ 的最後一個元素不起作用：
$$
w=\mathbf{m}^{3\mathsf{T}}(\tilde{\mathbf{X}}-\tilde{\mathbf{C}})
$$
4. **內積的幾何意義**：$\mathbf{a}\cdot\mathbf{b}=\|\mathbf{a}\|\|\mathbf{b}\|\cos\theta$：
$$
w=\|\mathbf{m}^3\|\,\|\tilde{\mathbf{X}}-\tilde{\mathbf{C}}\|\cos\theta
$$
   $\theta$ 是主軸方向 $\mathbf{m}^3$ 和「相機中心到點」向量的夾角。
5. **深度** = $\|\tilde{\mathbf{X}}-\tilde{\mathbf{C}}\|\cos\theta$（點到相機中心的向量在主軸上的投影）= $w/\|\mathbf{m}^3\|$。
6. **加上正負號**：$\mathbf{m}^3$ 的方向只確定到正負號（第 10 集），乘上 $\operatorname{sign}(\det M)$ 讓「正」= 主軸指向相機前方。∎

**用途** [▶ 14:50](https://youtu.be/oyGCk4idsaU?t=890)：判斷點在**相機前方還是後方**。

- 主軸朝前（正）、點在前面（$w>0$）→ 深度 > 0：在前方。
- 主軸方向和點的方向相反 → 一正一負 → 深度 < 0：在後方。

【課本補充】MVG §6.2.3：若把 $P$ 正規化成 $\det M>0$、$\|\mathbf{m}^3\|=1$，則 $w$ 直接就是深度。

---

## 4. 分解 P 得到 K、R、C

[▶ 16:36](https://youtu.be/oyGCk4idsaU?t=996)

**問題**：給一個 $3\times4$ 的 $P=[M\mid\mathbf{p}_4]=KR[I\mid-\tilde{\mathbf{C}}]$，找出全部 11 個參數：$\mathbf{C}$、$R$、$K$（$f_x,f_y,s,p_x,p_y$）。

### 4.1 相機中心：SVD

[▶ 17:46](https://youtu.be/oyGCk4idsaU?t=1066)

- $P\mathbf{C}=\mathbf{0}$。
- 把 $P$ 看成三列：$\mathbf{P}^3$ 是主平面，$\mathbf{P}^1,\mathbf{P}^2$ 是軸平面。$\mathbf{C}$ 是**三個平面的交點**。
- 用 SVD：$P=U\Sigma V^\mathsf{T}$，$\mathbf{C}$ = 最小奇異值對應的右奇異向量（$V$ 的最後一行）。

【課本補充】MVG §6.2.4 給了直接公式：$\mathbf{C}=(X,Y,Z,T)^\mathsf{T}$，其中 $X=\det[\mathbf{p}_2,\mathbf{p}_3,\mathbf{p}_4]$、$Y=-\det[\mathbf{p}_1,\mathbf{p}_3,\mathbf{p}_4]$、$Z=\det[\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_4]$、$T=-\det[\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3]$。講者說「算出來 $\mathbf{C}$ 的元素由這個式子給出」，應指此式。

### 4.2 K 和 R：RQ 分解

[▶ 20:07](https://youtu.be/oyGCk4idsaU?t=1207)

- $P=[M\mid-M\tilde{\mathbf{C}}]$，$M=KR$。
- $K$ 是**上三角矩陣**；$R$ 是**正交矩陣**。
- 所以問題變成：把 $M$ 分解成「上三角 × 正交」——**RQ 分解（RQ decomposition）**。

**怎麼做（講者的版本）** [▶ 21:46](https://youtu.be/oyGCk4idsaU?t=1306)：

1. $M=\mathcal{R}Q$（$\mathcal{R}$ 上三角、$Q$ 正交）→ 右乘 $Q^\mathsf{T}$：$MQ^\mathsf{T}=\mathcal{R}$。
2. $Q$ 是旋轉，用 roll、pitch、yaw 三個角表示——**三個未知數**。$M$ 已知。
3. $MQ^\mathsf{T}$ 是 $3\times3$，給 9 條方程式。其中下三角的 **3 個元素必須是 0**（右下角相機矩陣裡還是 1）。
4. 用那三個 0 解出三個角。（講者說加上右下的 1 共四條，是超定的；用三個 0 就夠。）
5. **額外約束**：$K$ 的對角（焦距）必須**嚴格為正**，用來挑選正確的解。

**讀出內參** [▶ 24:07](https://youtu.be/oyGCk4idsaU?t=1447)：$K=\begin{pmatrix}f_x&s&p_x\\0&f_y&p_y\\0&0&1\end{pmatrix}$ 的五個未知數直接從上三角矩陣讀出來。

⚠️ 逐字稿缺字 [▶ 24:31](https://youtu.be/oyGCk4idsaU?t=1471)：講者說「apply a QR decomposition on M」，依前文應為 **RQ** 分解。

【課本補充】MVG 附錄 A4.1.1 的做法和講者一樣：用三個 **Givens 旋轉**（分別繞 $x$、$y$、$z$ 軸）依序把 $M$ 的下三角元素消成 0。

> 以下**不是逐字稿內容**，是補充說明：RQ 分解得到的 $K$ 右下角一般不是 1，要把 $K$ 除以 $K_{33}$ 正規化。另外 RQ 分解有正負號模糊：$K\,\mathrm{diag}(\pm1,\pm1,\pm1)\cdot\mathrm{diag}(\pm1,\pm1,\pm1)\,R$ 都成立，所以用「對角為正」來固定。

---

## 5. 為什麼說相機是「射影」裝置

[▶ 24:54](https://youtu.be/oyGCk4idsaU?t=1494)

- 到目前為止，推導相機矩陣都用**歐氏**座標系（相機座標、世界座標都是歐氏的）。那為什麼一直說相機是 $\mathbb{P}^3\to\mathbb{P}^2$ 的**射影**裝置？
- 把 $P$ 拆成三段：

$$
P=\underbrace{H_{3\times3}}_{\text{2D 射影變換}}\ \underbrace{[I\mid\mathbf{0}]}_{3\times4}\ \underbrace{H_{4\times4}}_{\text{3D 射影變換}}
$$

1. **$H_{4\times4}$** 直接作用在 3D 點 $\mathbf{X}$ 上：可以是 $\mathbb{P}^3$ 的**任意射影變換**（Lecture 2、3）。
2. **$[I\mid\mathbf{0}]$**：只是把最後一維拿掉，從 $\mathbb{P}^3$ 變成 $\mathbb{P}^2$。本身不做任何變換。
3. **$H_{3\times3}$**：已經在 $\mathbb{P}^2$ 了，可以再套一個**任意 2D homography**（把一張影像變成另一張，$\mathbf{x}'=H\mathbf{x}$）。

- 所以整個相機投影應該看成一個**射影**操作。

【課本補充】MVG §6.2.5：這說明只用影像（不知道歐氏結構）時，重建出來的世界最多只能確定到差一個 3D 射影變換——這是之後「射影重建」的根據。

---

## 6. 仿射相機（無窮遠相機）

### 6.1 最後一列是 (0,0,0,1)

[▶ 28:59](https://youtu.be/oyGCk4idsaU?t=1739)

**仿射相機（affine camera）**：相機中心在**無窮遠**。

$$
P_A=\begin{pmatrix} m_{11}&m_{12}&m_{13}&t_1\\ m_{21}&m_{22}&m_{23}&t_2\\ 0&0&0&1\end{pmatrix}
$$

**為什麼最後一列是 $(0,0,0,1)$** [▶ 29:45](https://youtu.be/oyGCk4idsaU?t=1785)：

- 第 10 集：$P$ 的第三列是**主平面**，包含相機中心。
- 仿射相機的相機中心在 $\boldsymbol{\pi}_\infty$ 上，主平面也就是 $\boldsymbol{\pi}_\infty=(0,0,0,1)^\mathsf{T}$。
- 所以 $\mathbf{P}^3=\boldsymbol{\pi}_\infty$。

**相機中心是理想點** [▶ 30:57](https://youtu.be/oyGCk4idsaU?t=1857)：

$$
\mathbf{C}=\begin{pmatrix}\mathbf{d}\\0\end{pmatrix},\qquad M_{2\times3}\,\mathbf{d}=\mathbf{0}
$$

- $\mathbf{d}$ 是相機中心的方向；$M_{2\times3}$ 是 $M$ 的前兩列。
- **驗證** [▶ 32:09](https://youtu.be/oyGCk4idsaU?t=1929)：$P_A\mathbf{C}$ 的第三個分量是 $(0,0,0,1)\cdot(\mathbf{d},0)=0$；前兩個分量是 $M_{2\times3}\mathbf{d}+\mathbf{t}\cdot0=\mathbf{0}$。所以 $P_A\mathbf{C}=\mathbf{0}$ ✓。

**$M$ 奇異** [▶ 33:03](https://youtu.be/oyGCk4idsaU?t=1983)：$M$ 的最後一列是 0 → $M$ 只有兩列線性獨立 → 奇異。（這正是第 10 集說的「$M$ 不可逆 → 相機中心在無窮遠」。）

### 6.2 分解與自由度

**三段分解（仿射版）** [▶ 33:34](https://youtu.be/oyGCk4idsaU?t=2014)：

$$
P_A=\underbrace{H_{3\times3}^{A}}_{\text{2D 仿射}}\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\end{pmatrix}\underbrace{H_{4\times4}^{A}}_{\text{3D 仿射}}
$$

- 和第 5 節的射影版比較：
  - 兩邊的 $H$ 都變成**仿射**（無窮遠點經過它仍在無窮遠）。
  - 中間的投影矩陣：原本 $[I\mid\mathbf{0}]$（射影投影）；現在第三、四行對調，零行換到第三行——這是**正交投影（orthographic projection）**：直接丟掉 $z$ 座標。

⚠️ 逐字稿缺字：Whisper 把 orthographic 多處寫成 “octographic”。

**和射影相機同樣形式的分解** [▶ 35:15](https://youtu.be/oyGCk4idsaU?t=2115)：

$$
P_A=\underbrace{\begin{pmatrix}\alpha_x&s&0\\0&\alpha_y&0\\0&0&1\end{pmatrix}}_{K_{2\times2}\text{ 部分}}\underbrace{\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\end{pmatrix}}_{\text{正交投影}}\underbrace{\begin{pmatrix}R&\mathbf{t}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}}_{\text{剛體}}=\begin{pmatrix}\alpha_x&s\\0&\alpha_y\end{pmatrix}\text{ 作用在 }\begin{pmatrix}\mathbf{r}^{1\mathsf{T}}&t_1\\\mathbf{r}^{2\mathsf{T}}&t_2\end{pmatrix}\text{ 上}
$$

- 正交投影的第三行是 0 → 把 $R$ 的第三列 $\mathbf{r}^{3\mathsf{T}}$ 去掉，只留前兩列；同樣把 $t_z$ 去掉，只留 $t_1,t_2$。
- 文獻上常把**主點設成 0**：仿射相機沒有射影失真，乾脆把主點放在場景重心。

（$K$ 的元素位置依 MVG 式 (6.27) 寫出；逐字稿只說「縮放、斜切、主點」。）

**自由度 = 8** [▶ 37:47](https://youtu.be/oyGCk4idsaU?t=2267)：

| 部分 | 自由度 |
|---|---|
| 內參 $\alpha_x,\alpha_y,s$ | 3 |
| 旋轉（只用前兩列） | 3 |
| $t_1,t_2$ | 2 |
| **合計** | **8**（對比射影相機 11） |

- 直接數 $P_A$：8 個「不是 0 也不是 1」的元素。

**為什麼只用 $R$ 的兩列還是 3 個自由度** [▶ 38:34](https://youtu.be/oyGCk4idsaU?t=2314)：三列不是線性獨立的——$\mathbf{r}^3=\mathbf{r}^1\times\mathbf{r}^2$，所以任兩列就包含了全部 3 個自由度。

講者說「$P_A$ 只有 rank 2」[▶ 39:46](https://youtu.be/oyGCk4idsaU?t=2386)，對比射影相機的 $M$ rank 3。

> 以下**不是逐字稿內容**，是依線性代數推論的：rank 2 的是 $P_A$ 左邊的 $3\times3$ 子矩陣 $M$（最後一列為 0）。$P_A$ 本身（$3\times4$）的第三列 $(0,0,0,1)$ 和前兩列獨立，rank 是 3。

### 6.3 為什麼叫「仿射」

[▶ 40:16](https://youtu.be/oyGCk4idsaU?t=2416)

**性質 1：無窮遠點投影到影像的無窮遠點**：

$$
P_A\begin{pmatrix}X\\Y\\Z\\0\end{pmatrix}=\begin{pmatrix}x\\y\\0\end{pmatrix}
$$

最後一列 $(0,0,0,1)$ 乘上最後分量為 0 的向量，永遠是 0。

**性質 2：世界中的平行線投影成影像中的平行線** [▶ 42:15](https://youtu.be/oyGCk4idsaU?t=2535)：

- 兩條平行線交於無窮遠點 $(X,Y,Z,0)^\mathsf{T}$。
- 由性質 1，投影後交點還在無窮遠 → 影像中兩線仍然平行。

這兩點說的是同一件事：$P_A$ 保持仿射性質。

### 6.4 三種仿射相機

[▶ 43:54](https://youtu.be/oyGCk4idsaU?t=2634)

**(a) 正交投影（orthographic projection）**：

- 物體直接投影到影像，**不縮放**——就是丟掉 $z$（深度）。
- 所有光線互相平行；延長後交在無窮遠——相機中心在 $\boldsymbol{\pi}_\infty$ 上，符合仿射相機。
- **完全忽略深度**：人站在近處或遠處，投影出來都一樣大。
- $K=I$（沒有縮放）：
$$
P=\begin{pmatrix}\mathbf{r}^{1\mathsf{T}}&t_1\\\mathbf{r}^{2\mathsf{T}}&t_2\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}
$$
- **自由度 5**：$8-3$（去掉 $\alpha_x,\alpha_y,s$）；或直接數 $\mathbf{r}^1,\mathbf{r}^2$ 共 3 + $t_1,t_2$ 共 2。
- **$M$ 的特徵** [▶ 47:01](https://youtu.be/oyGCk4idsaU?t=2821)：最後一列 0；前兩列**正交**且**單位長度**；$t_3=1$。

**(b) 縮放正交投影（scaled orthographic projection）** [▶ 47:40](https://youtu.be/oyGCk4idsaU?t=2860)：

- 兩步：先正交投影到一個虛擬影像平面，再**等向縮放** $k$（兩個方向放大或縮小同樣倍數，沒有斜切）。
$$
P=\begin{pmatrix}k&&\\&k&\\&&1\end{pmatrix}\begin{pmatrix}\mathbf{r}^{1\mathsf{T}}&t_1\\\mathbf{r}^{2\mathsf{T}}&t_2\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}
$$
- **自由度 6**：正交的 5 + 縮放 1。
- **$M$ 的特徵** [▶ 49:35](https://youtu.be/oyGCk4idsaU?t=2975)：最後一列 0；前兩列正交且**等長**；把 $P$ 縮放成右下為 1 時，$t_3$ 那個位置變成 $1/k$。

⚠️ 逐字稿缺字 [▶ 48:29](https://youtu.be/oyGCk4idsaU?t=2909)：講者說「先正交投影，再接一個透視投影（受縮放作用）」，依上下文應為「再接一個**縮放**」；縮放正交投影裡沒有透視投影。

> 以下**不是逐字稿內容**：「$t_3=1/k$」依 MVG §6.3.4 的說法理解為：把 $\mathrm{diag}(k,k,1)\cdot[\dots]$ 整體除以 $k$（齊次矩陣可以縮放），使前兩列變回單位長度，這時右下角變成 $1/k$。

**(c) 弱透視投影（weak perspective projection）** [▶ 49:53](https://youtu.be/oyGCk4idsaU?t=2993)：

- 和縮放正交類似，但兩個方向**縮放不同**：$x$ 方向 $\alpha_x$、$y$ 方向 $\alpha_y$。
$$
P=\begin{pmatrix}\alpha_x&&\\&\alpha_y&\\&&1\end{pmatrix}\begin{pmatrix}\mathbf{r}^{1\mathsf{T}}&t_1\\\mathbf{r}^{2\mathsf{T}}&t_2\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}
$$
- **自由度 7**：正交的 5 + 兩個縮放。
- **$M$ 的特徵**：最後一列 0；前兩列正交，但**不需要等長**。

**比較表**：

| 相機 | $K$ 部分 | 自由度 | $M$ 前兩列 |
|---|---|---|---|
| 正交 | $I$ | 5 | 正交、單位長 |
| 縮放正交 | $\mathrm{diag}(k,k,1)$ | 6 | 正交、等長 |
| 弱透視 | $\mathrm{diag}(\alpha_x,\alpha_y,1)$ | 7 | 正交 |
| 一般仿射 | $\begin{pmatrix}\alpha_x&s&0\\0&\alpha_y&0\\0&0&1\end{pmatrix}$ | 8 | 無限制 |

【課本補充】MVG §6.3.2：仿射相機是射影相機在「物體深度變化遠小於物體到相機距離」時的近似（例如用長焦鏡頭拍遠處的物體）。

（本集到 51:08 結束。）

---

## 7. 一頁速查表

### 射影相機對點的作用（$P=[M\mid\mathbf{p}_4]$）

| 公式 | 關鍵一步 |
|---|---|
| 前向：$\mathbf{x}=P\mathbf{X}$；無窮遠點 $\mathbf{x}=M\mathbf{d}$ | 最後分量 0 → $\mathbf{p}_4$ 沒作用 |
| 反向：$\mathbf{X}(\lambda)=P^+\mathbf{x}+\lambda\mathbf{C}$，$P^+=P^\mathsf{T}(PP^\mathsf{T})^{-1}$ | $PP^+=I$、$P\mathbf{C}=0$ |
| 有限相機：$\mathbf{X}(\mu)=\begin{pmatrix}M^{-1}(\mu\mathbf{x}-\mathbf{p}_4)\\1\end{pmatrix}$ | 光線交 $\boldsymbol{\pi}_\infty$ 於 $(M^{-1}\mathbf{x},0)$ |
| 深度：$\dfrac{\operatorname{sign}(\det M)\,w}{T\|\mathbf{m}^3\|}$ | $w=\mathbf{P}^{3\mathsf{T}}(\mathbf{X}-\mathbf{C})=\mathbf{m}^{3\mathsf{T}}(\tilde{\mathbf{X}}-\tilde{\mathbf{C}})$ |

### 分解

| 求什麼 | 方法 |
|---|---|
| $\mathbf{C}$ | $P$ 的零空間（SVD 最後一個右奇異向量） |
| $K$、$R$ | $M=KR$ 做 RQ 分解（Givens 旋轉消下三角）；對角取正 |
| 射影觀點 | $P=H_{3\times3}[I\mid\mathbf{0}]H_{4\times4}$ |

### 仿射相機

- 最後一列 $(0,0,0,1)$ = 主平面是 $\boldsymbol{\pi}_\infty$；$\mathbf{C}=(\mathbf{d},0)^\mathsf{T}$，$M_{2\times3}\mathbf{d}=0$；$M$ rank 2。
- 無窮遠點 → 無窮遠點；平行 → 平行。
- 自由度：正交 5、縮放正交 6、弱透視 7、一般 8。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 反向投影光線 | 第 16–19 集（極線：一張圖的點反投影成光線，投到另一張圖成極線）；三角化 |
| 深度正負號 | 第 16–19 集（從 $E$ 分解出四組 $R,\mathbf{t}$，用「點在兩相機前方」挑出正確的一組） |
| RQ 分解 | 第 12 集（DLT 估計 $P$ 後分解出 $K,R$） |
| $P=H[I\mid\mathbf{0}]H_{4\times4}$ | 第 16–19 集、第 27–30 集（射影重建的模糊） |
| 仿射相機 | 第 27–30 集（仿射因式分解 Tomasi–Kanade，若有講） |
| $M\mathbf{d}$ = 消失點 | 第 13–15 集（單視角量測） |

---

## 附：本集一句話總結

> **相機把點往前投很簡單，往回投只能得到一條光線（相機中心加上 $P^+\mathbf{x}$ 或 $(M^{-1}\mathbf{x},0)$）；$w$ 配上 $\operatorname{sign}(\det M)$ 告訴你點在前還後；$P$ 可以用 SVD 求中心、RQ 分解拆出 $K$ 和 $R$；把相機中心推到無窮遠就得到最後一列是 $(0,0,0,1)$ 的仿射相機，它保持平行，依縮放方式分成正交（5）、縮放正交（6）、弱透視（7）、一般仿射（8）。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 5 (Part 2) 錄影逐字稿（Whisper `medium.en`，51:12）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §6.2.2–6.3.4、附錄 A4.1.1 整理。*
