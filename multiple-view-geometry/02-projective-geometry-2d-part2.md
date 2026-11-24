---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 02
lecture: Lecture 1 (Part 2) – 2D and 1D projective geometry
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/gQ7IUS8NKCI
notes: MVG §2.2.3–2.5（書頁 30–46，PDF 頁 48–64）
---

# 第 02 集 · Lecture 1 (Part 2)：二次曲線、射影變換、變換階層、1D 射影幾何 [▶ 影片](https://youtu.be/gQ7IUS8NKCI)

← 上一集：[01-projective-geometry-2d-part1](01-projective-geometry-2d-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[03-rigid-motion-3d-projective-part1](03-rigid-motion-3d-projective-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 02 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（1:13:14，Whisper `medium.en` 轉錄）＋ MVG §2.2.3–2.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 二次曲線（conic）](#1-二次曲線conic)
  - [1.1 三種圓錐曲線](#11-三種圓錐曲線)
  - [1.2 齊次化與矩陣形式](#12-齊次化與矩陣形式)
  - [1.3 五個點決定一條二次曲線](#13-五個點決定一條二次曲線)
  - [1.4 切線 l = Cx](#14-切線-l--cx)
- [2. 對偶二次曲線](#2-對偶二次曲線)
- [3. 退化二次曲線](#3-退化二次曲線)
- [4. 射影變換（homography）](#4-射影變換homography)
  - [4.1 定義與定理](#41-定義與定理)
  - [4.2 矩陣形式與性質](#42-矩陣形式與性質)
  - [4.3 幾何意義：平面到平面的中心投影](#43-幾何意義平面到平面的中心投影)
  - [4.4 線和二次曲線怎麼變](#44-線和二次曲線怎麼變)
- [5. 變換階層](#5-變換階層)
  - [5.1 等距變換](#51-等距變換)
  - [5.2 相似變換](#52-相似變換)
  - [5.3 仿射變換](#53-仿射變換)
  - [5.4 射影變換](#54-射影變換)
  - [5.5 總表與分解](#55-總表與分解)
- [6. 1D 射影幾何與交比](#6-1d-射影幾何與交比)
- [7. Lecture 1 總結](#7-lecture-1-總結)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

接續第 01 集（點、線、對偶），本集講 Lecture 1 剩下的部分：

| 主題 | MVG |
|---|---|
| 二次曲線、對偶二次曲線、退化二次曲線 | §2.2.3 |
| 射影變換的定義、點／線／二次曲線怎麼變 | §2.3 |
| 變換階層：等距、相似、仿射、射影 | §2.4 |
| 1D 射影幾何、交比 | §2.5 |

---

## 1. 二次曲線（conic）

### 1.1 三種圓錐曲線

[▶ 00:00](https://youtu.be/gQ7IUS8NKCI?t=0)

- **二次曲線（conic）**：平面上由**二次多項式方程式**描述的曲線。
- 歐氏幾何裡有三種主要類型：**雙曲線（hyperbola）**、**橢圓（ellipse）**、**拋物線（parabola）**。另外還有**退化二次曲線（degenerate conic）**（第 3 節）。
- 它們都是**用不同方向的平面去切一對上下相對的圓錐**得到的，所以叫圓錐曲線（conic section）。

[▶ 01:01](https://youtu.be/gQ7IUS8NKCI?t=61) 怎麼切：

| 平面方向 | 得到 |
|---|---|
| 和圓錐的斜邊平行 | 拋物線 |
| 和圓錐底面平行 | 圓 |
| 稍微傾斜，但還接近底面方向 | 橢圓 |
| 和圓錐的垂直軸平行 | 雙曲線 |

【課本補充】（MVG §2.2.3）退化二次曲線來自**通過圓錐頂點**的平面。另外，在 2D 射影幾何裡，**所有非退化二次曲線在射影變換下都是等價的**——橢圓、拋物線、雙曲線可以互相變成對方。

### 1.2 齊次化與矩陣形式

[▶ 02:43](https://youtu.be/gQ7IUS8NKCI?t=163)

非齊次座標下的二次曲線方程式：

$$
ax^2+bxy+cy^2+dx+ey+f=0
$$

**齊次化**：照第 01 集的換算，把 $x\to x_1/x_3$、$y\to x_2/x_3$ 代進去，再整個乘上 $x_3^2$：

$$
ax_1^2+bx_1x_2+cx_2^2+dx_1x_3+ex_2x_3+fx_3^2=0
$$

寫成矩陣形式：

$$
\mathbf{x}^\mathsf{T}C\mathbf{x}=0,\qquad
C=\begin{pmatrix} a & b/2 & d/2\\ b/2 & c & e/2\\ d/2 & e/2 & f\end{pmatrix}
$$

**驗證**（展開一項看看）：$\mathbf{x}^\mathsf{T}C\mathbf{x}=\sum_{i,j}C_{ij}x_ix_j$。交叉項 $x_1x_2$ 出現兩次（$C_{12}$ 和 $C_{21}$），各 $b/2$，加起來是 $b\,x_1x_2$。其他交叉項同理。

- $C$ 是 **$3\times3$ 對稱矩陣**，是二次曲線的**齊次表示**。
- 只有元素之間的**比值**重要：$C$ 乘上非零常數 $k$，方程式 $=0$ 不變。和點、線的齊次表示一樣。
- **自由度 = 5**：可以看成比值 $a:b:c:d:e:f$（6 個數少 1 個縮放），或者對稱矩陣的 6 個獨立元素少 1 個縮放。

### 1.3 五個點決定一條二次曲線

[▶ 06:16](https://youtu.be/gQ7IUS8NKCI?t=376)

- 曲線上每個點 $(x_i,y_i)$ 給**一個**約束：
$$
ax_i^2+bx_iy_i+cy_i^2+dx_i+ey_i+f=0
$$
- 寫成內積：
$$
\begin{pmatrix} x_i^2 & x_iy_i & y_i^2 & x_i & y_i & 1\end{pmatrix}\mathbf{c}=0,\qquad \mathbf{c}=(a,b,c,d,e,f)^\mathsf{T}
$$
- $\mathbf{c}$ 有 6 個未知數，少 1 個縮放 → 5 個自由度 → **至少要 5 個約束 = 5 個點**。
- 把 5 個點的約束疊起來：
$$
A\mathbf{c}=\mathbf{0},\qquad A\ \text{是}\ 5\times6\ \text{矩陣}
$$
- $\mathbf{c}$ 落在 $A$ 的**零空間（null space）**裡。5 個點已知 → $A$ 已知 → 求 $A$ 的零空間就得到二次曲線。
- 【口頭】講者預告：之後的課會用 **SVD（奇異值分解）**求零空間。

【課本補充】（MVG §2.2.3）5 個點要在**一般位置（general position）**，二次曲線才是唯一的（差一個縮放）。「用求零空間來擬合幾何物件」這招，整本書會一直用。

### 1.4 切線 l = Cx

[▶ 09:17](https://youtu.be/gQ7IUS8NKCI?t=557)

- 一條線和二次曲線可能交於兩點、一點（切線）、或不相交。
- 這裡看**切線**的情況。

> **Result 2.7（MVG）** 二次曲線 $C$ 在點 $\mathbf{x}$（在 $C$ 上）的切線是 $\mathbf{l}=C\mathbf{x}$。

**證明** [▶ 10:07](https://youtu.be/gQ7IUS8NKCI?t=607)：

1. **$\mathbf{l}$ 通過 $\mathbf{x}$**：$\mathbf{l}^\mathsf{T}\mathbf{x}=(C\mathbf{x})^\mathsf{T}\mathbf{x}=\mathbf{x}^\mathsf{T}C^\mathsf{T}\mathbf{x}=\mathbf{x}^\mathsf{T}C\mathbf{x}=0$（$C$ 對稱，且 $\mathbf{x}$ 在曲線上）。
2. 如果 $\mathbf{l}$ 和曲線**只有一個接觸點**，它就是切線，證完。
3. 否則，假設 $\mathbf{l}$ 還碰到曲線上另一點 $\mathbf{y}$（[▶ 17:49](https://youtu.be/gQ7IUS8NKCI?t=1069)，講者在講完對偶二次曲線後才補這段）：
   - $\mathbf{y}$ 在曲線上：$\mathbf{y}^\mathsf{T}C\mathbf{y}=0$。
   - $\mathbf{y}$ 在 $\mathbf{l}$ 上：$\mathbf{x}^\mathsf{T}C\mathbf{y}=\mathbf{l}^\mathsf{T}\mathbf{y}=0$。
   - 對任意 $\alpha$，展開：
   $$
   (\mathbf{x}+\alpha\mathbf{y})^\mathsf{T}C(\mathbf{x}+\alpha\mathbf{y})=\underbrace{\mathbf{x}^\mathsf{T}C\mathbf{x}}_{0}+2\alpha\underbrace{\mathbf{x}^\mathsf{T}C\mathbf{y}}_{0}+\alpha^2\underbrace{\mathbf{y}^\mathsf{T}C\mathbf{y}}_{0}=0
   $$
   - $\mathbf{x}+\alpha\mathbf{y}$ 跑遍 $\mathbf{x}$、$\mathbf{y}$ 連線上的所有點 → **整條線都在曲線上**。
   - 那這條「曲線」已經不是橢圓、拋物線、雙曲線或圓了，它包含一條直線 → 是**退化**的。∎

所以對非退化二次曲線，$\mathbf{l}=C\mathbf{x}$ 一定只碰一點，是切線。

---

## 2. 對偶二次曲線

[▶ 11:42](https://youtu.be/gQ7IUS8NKCI?t=702)

- 上面定義的 $C$ 更精確的名字是**點二次曲線（point conic）**：它是一個關於**點**的方程式，5 個（或更多）點決定它。
- 第 01 集的點線對偶：$\mathbf{x}^\mathsf{T}\mathbf{l}=\mathbf{l}^\mathsf{T}\mathbf{x}=0$。很多點可以代表一條線，一條線也代表線上的很多點。
- 同樣地，二次曲線也可以用**切線**來決定：給夠多的切線，曲線就唯一確定。

**對偶二次曲線（dual conic）**，也叫**線二次曲線（line conic）**：

$$
\mathbf{l}^\mathsf{T}C^*\mathbf{l}=0
$$

| | 點二次曲線 $C$ | 對偶二次曲線 $C^*$ |
|---|---|---|
| 方程式 | $\mathbf{x}^\mathsf{T}C\mathbf{x}=0$ | $\mathbf{l}^\mathsf{T}C^*\mathbf{l}=0$ |
| 滿足方程式的是 | 曲線上的**點** | 曲線的**切線** |
| 自由度 | 5 | 5 |
| 決定它需要 | 5 個點 | 5 條線 |

**$C^*=C^{-1}$**（$C$ 非奇異時，差一個縮放）。

**證明** [▶ 14:56](https://youtu.be/gQ7IUS8NKCI?t=896)：

1. 由 Result 2.7，曲線上點 $\mathbf{x}$ 的切線是 $\mathbf{l}=C\mathbf{x}$。
2. $C$ 可逆 → $\mathbf{x}=C^{-1}\mathbf{l}$（切線 $\mathbf{l}$ 在哪一點碰到曲線）。
3. $\mathbf{x}$ 在曲線上，代入 $\mathbf{x}^\mathsf{T}C\mathbf{x}=0$：
$$
(C^{-1}\mathbf{l})^\mathsf{T}C(C^{-1}\mathbf{l})=\mathbf{l}^\mathsf{T}C^{-\mathsf{T}}CC^{-1}\mathbf{l}=\mathbf{l}^\mathsf{T}C^{-\mathsf{T}}\mathbf{l}=\mathbf{l}^\mathsf{T}C^{-1}\mathbf{l}=0
$$
   最後一步用 $C$ 對稱 → $C^{-\mathsf{T}}=C^{-1}$。
4. 所以 $C^*=C^{-1}$。∎

- 幾何上，對偶二次曲線也叫**二次曲線包絡（conic envelope）**：所有切線「包」出這條曲線（MVG Fig. 2.2）。

【課本補充】（MVG §2.2.3）記號 $C^*$ 其實是 $C$ 的**伴隨矩陣（adjoint）**（MVG 附錄 4.2）。$C$ 非奇異時伴隨矩陣和 $C^{-1}$ 只差一個縮放。

---

## 3. 退化二次曲線

[▶ 20:21](https://youtu.be/gQ7IUS8NKCI?t=1221)

**定義**：$C$ **不是滿秩**（$\operatorname{rank}C<3$）時，叫**退化二次曲線**。

從第 1.4 節：當某條線和曲線碰到兩點以上，整條線都在曲線上 → 退化。

**三種幾何情況**（平面通過圓錐頂點）[▶ 21:02](https://youtu.be/gQ7IUS8NKCI?t=1262)：

1. 平面只碰到兩個圓錐的**頂點**：曲線縮成一點（$\mathbf{x}=\mathbf{y}$）。
2. 平面剛好沿著圓錐的**斜邊**切：交出**一條線**。
3. 平面穿過頂點、切進兩個圓錐：交出**兩條相交的線**。

**退化點二次曲線**：

**(a) 兩條線，rank 2** [▶ 23:19](https://youtu.be/gQ7IUS8NKCI?t=1399)：

$$
C=\mathbf{l}\mathbf{m}^\mathsf{T}+\mathbf{m}\mathbf{l}^\mathsf{T}
$$

代進曲線方程式：

$$
\mathbf{x}^\mathsf{T}C\mathbf{x}=(\mathbf{x}^\mathsf{T}\mathbf{l})(\mathbf{m}^\mathsf{T}\mathbf{x})+(\mathbf{x}^\mathsf{T}\mathbf{m})(\mathbf{l}^\mathsf{T}\mathbf{x})=2(\mathbf{l}^\mathsf{T}\mathbf{x})(\mathbf{m}^\mathsf{T}\mathbf{x})
$$

- 等於 0 若且唯若 $\mathbf{l}^\mathsf{T}\mathbf{x}=0$ 或 $\mathbf{m}^\mathsf{T}\mathbf{x}=0$：點在 $\mathbf{l}$ 上或在 $\mathbf{m}$ 上。所以這條「曲線」就是兩條線。
- 寫成 $\mathbf{l}\mathbf{m}^\mathsf{T}+\mathbf{m}\mathbf{l}^\mathsf{T}$ 而不是只寫 $\mathbf{l}\mathbf{m}^\mathsf{T}$，是為了讓 $C$ **對稱**。

⚠️ 逐字稿缺字：講者說 $\mathbf{l}\mathbf{m}^\mathsf{T}$ 是 “dot product”，但 $\mathbf{l}\mathbf{m}^\mathsf{T}$ 是 $3\times3$ 矩陣，應為**外積（outer product）**。

【課本補充】（MVG Example 2.8）這個 $C$ 的零向量（null vector）是 $\mathbf{l}\times\mathbf{m}$，就是兩條線的交點。

**(b) 重複的線，rank 1** [▶ 25:09](https://youtu.be/gQ7IUS8NKCI?t=1509)：

$$
C=\mathbf{l}\mathbf{l}^\mathsf{T}\quad\Longrightarrow\quad \mathbf{x}^\mathsf{T}C\mathbf{x}=(\mathbf{l}^\mathsf{T}\mathbf{x})^2=0
$$

同一條線重疊兩次。

⚠️ 逐字稿缺字 [▶ 25:32](https://youtu.be/gQ7IUS8NKCI?t=1532)：Whisper 寫 “l transpose l plus l l transpose”。$\mathbf{l}^\mathsf{T}\mathbf{l}$ 是純量，加不了矩陣。依 MVG 和 (a) 的寫法（令 $\mathbf{m}=\mathbf{l}$），應為 $\mathbf{l}\mathbf{l}^\mathsf{T}+\mathbf{l}\mathbf{l}^\mathsf{T}=2\,\mathbf{l}\mathbf{l}^\mathsf{T}$，差一個縮放就是 $\mathbf{l}\mathbf{l}^\mathsf{T}$。

**退化對偶二次曲線**（對偶版本）[▶ 26:26](https://youtu.be/gQ7IUS8NKCI?t=1586)：

- **兩個點，rank 2**：$C^*=\mathbf{x}\mathbf{y}^\mathsf{T}+\mathbf{y}\mathbf{x}^\mathsf{T}$。它包含的是**通過 $\mathbf{x}$ 或通過 $\mathbf{y}$ 的所有線**（兩束線）。
- **重複的點，rank 1**。
- 講者不再證明：對偶原理保證點二次曲線證過的，線二次曲線也成立。

**注意** [▶ 28:11](https://youtu.be/gQ7IUS8NKCI?t=1691)：退化時 $C$ 不可逆，所以 **$C^*=C^{-1}$ 不再成立**。這個關係只在 $\operatorname{rank}C=3$ 時才對。

---

## 4. 射影變換（homography）

### 4.1 定義與定理

[▶ 28:40](https://youtu.be/gQ7IUS8NKCI?t=1720)

- **2D 射影幾何**研究射影平面在一群叫做**射影變換（projectivity）**的變換下**不變**的性質。
- 射影變換必須是**可逆**映射 $h:\mathbb{P}^2\to\mathbb{P}^2$：輸入 $\mathbb{P}^2$ 的點（或線、二次曲線），輸出還是 $\mathbb{P}^2$ 的。
- 可逆：能用 $h^{-1}$ 從輸出回到輸入。
- 同義詞：**projectivity = collineation（直射變換）= projective transformation = homography**。

【課本補充】MVG Definition 2.9：射影變換是可逆映射 $h$，使得 $\mathbf{x}_1,\mathbf{x}_2,\mathbf{x}_3$ 共線**若且唯若** $h(\mathbf{x}_1),h(\mathbf{x}_2),h(\mathbf{x}_3)$ 共線。課本還提到 Klein 的「Erlangen 綱領」：幾何就是研究在一群變換下不變的性質。

> **Theorem 2.10（MVG）** 映射 $h:\mathbb{P}^2\to\mathbb{P}^2$ 是射影變換，若且唯若存在**非奇異** $3\times3$ 矩陣 $H$，使得對 $\mathbb{P}^2$ 中任一點 $\mathbf{x}$，$h(\mathbf{x})=H\mathbf{x}$。

**部分證明**（只證「可逆線性映射 ⇒ 保持共線」；反方向難很多，跳過）[▶ 32:21](https://youtu.be/gQ7IUS8NKCI?t=1941)：

1. 設 $\mathbf{x}_1,\mathbf{x}_2,\mathbf{x}_3$ 在線 $\mathbf{l}$ 上：$\mathbf{l}^\mathsf{T}\mathbf{x}_i=0$，$i=1,2,3$。
2. $H$ 非奇異，插入 $H^{-1}H=I$：
$$
\mathbf{l}^\mathsf{T}H^{-1}H\mathbf{x}_i=0
$$
3. 令 $\mathbf{x}_i'=H\mathbf{x}_i$、$\mathbf{l}'=H^{-\mathsf{T}}\mathbf{l}$（所以 $\mathbf{l}'^\mathsf{T}=\mathbf{l}^\mathsf{T}H^{-1}$），上式就是 $\mathbf{l}'^\mathsf{T}\mathbf{x}_i'=0$。
4. 三個變換後的點都在 $\mathbf{l}'$ 上 → **共線性被保留**。∎

這呼應第 01 集開頭：形狀、角度、距離都會變，但直線還是直線。

### 4.2 矩陣形式與性質

[▶ 35:08](https://youtu.be/gQ7IUS8NKCI?t=2108)

$$
\begin{pmatrix} x_1'\\ x_2'\\ x_3'\end{pmatrix}=\begin{pmatrix} h_{11} & h_{12} & h_{13}\\ h_{21} & h_{22} & h_{23}\\ h_{31} & h_{32} & h_{33}\end{pmatrix}\begin{pmatrix} x_1\\ x_2\\ x_3\end{pmatrix},\qquad \mathbf{x}'=H\mathbf{x}
$$

$H$ 的性質：

- **非奇異**：要可逆。
- **齊次矩陣**：只有元素間的比值有意義。
- **8 個自由度**：9 個元素少 1 個縮放。講者說之後講 homography 估計時（Lecture 4）會更清楚。

### 4.3 幾何意義：平面到平面的中心投影

[▶ 36:29](https://youtu.be/gQ7IUS8NKCI?t=2189)

- 第 01 集：一條過原點的射線，和互相平行的平面 $k=1,2,\dots$ 相交，交點都代表**同一個點**。
- Homography 的意思：把平面換成**另一個不平行的平面**，同一條射線和兩個平面各交出一點 $\mathbf{x}$、$\mathbf{x}'$，它們的關係就是 $\mathbf{x}'=H\mathbf{x}$。

**什麼時候影像裡會出現 homography** [▶ 38:03](https://youtu.be/gQ7IUS8NKCI?t=2283)：不是所有情況都成立，要兩個條件：

1. **平面到平面**：點必須落在一個平面上。
2. **透視影像（perspective image）**：所有光線收斂到**同一點**（投影中心）。講者說之後的課會細講。

【課本補充】（MVG §2.3，Fig. 2.3、Example 2.12）

- 如果兩個平面上用的都是歐氏座標系，中心投影其實比一般射影變換更受限，叫**透視變換（perspectivity）**，只有 6 個自由度（MVG §A7.4）。
- 應用：把照片裡一面牆的四個窗角，對應到一個長方形的四個角 → 解出 $H$ → 對整張照片套 $H^{-1}$，就能「拉正」牆面（去除射影失真）。每對對應點給兩個線性方程式：
$$
x'(h_{31}x+h_{32}y+h_{33})=h_{11}x+h_{12}y+h_{13},\qquad y'(h_{31}x+h_{32}y+h_{33})=h_{21}x+h_{22}y+h_{23}
$$
  4 對點（任三點不共線）→ 8 條方程式 → 解出 $H$（差一個縮放）。不需要知道相機參數或平面的位姿。

### 4.4 線和二次曲線怎麼變

[▶ 39:20](https://youtu.be/gQ7IUS8NKCI?t=2360)

**點**：$\mathbf{x}'=H\mathbf{x}$

**線**：$\mathbf{l}'=H^{-\mathsf{T}}\mathbf{l}$（等價寫法 $\mathbf{l}'^\mathsf{T}=\mathbf{l}^\mathsf{T}H^{-1}$）

- 推導就是 4.1 的證明：要讓 $\mathbf{l}'^\mathsf{T}\mathbf{x}'=\mathbf{l}^\mathsf{T}H^{-1}H\mathbf{x}=\mathbf{l}^\mathsf{T}\mathbf{x}=0$ 繼續成立。

**二次曲線** [▶ 41:22](https://youtu.be/gQ7IUS8NKCI?t=2482)：

> **Result 2.13（MVG）** 在點變換 $\mathbf{x}'=H\mathbf{x}$ 下，二次曲線變成 $C'=H^{-\mathsf{T}}CH^{-1}$。

**證明** [▶ 42:21](https://youtu.be/gQ7IUS8NKCI?t=2541)：把 $\mathbf{x}=H^{-1}\mathbf{x}'$ 代進 $\mathbf{x}^\mathsf{T}C\mathbf{x}=0$：

$$
\mathbf{x}^\mathsf{T}C\mathbf{x}=(H^{-1}\mathbf{x}')^\mathsf{T}C(H^{-1}\mathbf{x}')=\mathbf{x}'^\mathsf{T}\underbrace{H^{-\mathsf{T}}CH^{-1}}_{C'}\mathbf{x}'=0
$$

這是 $\mathbf{x}'$ 的二次式，係數矩陣就是 $C'$。∎

【口頭】[▶ 43:49](https://youtu.be/gQ7IUS8NKCI?t=2629) 講者提醒投影片上某處「沒有 inverse」（投影片筆誤）。依上面推導，正確的是 $C'=H^{-\mathsf{T}}CH^{-1}$。

> **Result 2.14（MVG）** 在點變換 $\mathbf{x}'=H\mathbf{x}$ 下，對偶二次曲線變成 $C^{*\prime}=HC^*H^\mathsf{T}$。

講者沒證明，只提醒這裡假設 $C$ 滿秩（$C^*=C^{-1}$，非退化）。

> 以下**不是逐字稿內容**，是依 $C^*=C^{-1}$ 推論的關鍵一步：
> $$C^{*\prime}=(C')^{-1}=(H^{-\mathsf{T}}CH^{-1})^{-1}=HC^{-1}H^\mathsf{T}=HC^*H^\mathsf{T}$$
> （也可以仿照二次曲線的證明，把 $\mathbf{l}=H^\mathsf{T}\mathbf{l}'$ 代進 $\mathbf{l}^\mathsf{T}C^*\mathbf{l}=0$。）

---

## 5. 變換階層

[▶ 44:03](https://youtu.be/gQ7IUS8NKCI?t=2643)

一般的 $H$ 有 8 個自由度，兩個平面之間沒有特別關係。對 $H$ 加上限制，就得到幾種**特殊情況**，各自保留不同的幾何性質。從最特殊的開始往上走。

### 5.1 等距變換（isometry）

[▶ 44:09](https://youtu.be/gQ7IUS8NKCI?t=2649)

**保持歐氏距離**的變換。

$$
\begin{pmatrix} x'\\ y'\\ 1\end{pmatrix}=\begin{pmatrix} \epsilon\cos\theta & -\sin\theta & t_x\\ \epsilon\sin\theta & \cos\theta & t_y\\ 0 & 0 & 1\end{pmatrix}\begin{pmatrix} x\\ y\\ 1\end{pmatrix},\qquad \epsilon=\pm1
$$

- 左上 $2\times2$：**2D 旋轉**（rotation）；右上：**2D 平移**（translation）$(t_x,t_y)$。
- 點 $(x,y)$ 在新座標系（旋轉 $\theta$ 再平移）下的座標就是 $(x',y')$。
- 任兩點的距離 $d$，變換前後都一樣。
- **$\epsilon=1$**：**保持方向（orientation preserving）**，就是**歐氏變換（Euclidean transformation）**。
- **$\epsilon=-1$**：**反轉方向**，包含一次**鏡射（reflection）**。
- 講者說：旋轉矩陣和平移向量的細節，下一講在 3D 裡推導。
- **自由度 3**（1 個角度 + 2 個平移）。
- **不變量**：長度、角度、面積。

### 5.2 相似變換（similarity）

[▶ 50:39](https://youtu.be/gQ7IUS8NKCI?t=3039)

等距變換再加上**等向縮放（isotropic scaling）**：$x$、$y$ 方向放大同樣倍數。

$$
H_S=\begin{pmatrix} sR & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}
$$

- 也叫**等形變換（equiform transformation）**：**保持形狀**。
- 【口頭】例子：一個正方形，$R=I$、$t_x=2$、$s=2$ → 往 $x$ 方向移 2、放大 2 倍，還是正方形。
- **自由度 4**（等距的 3 + 縮放 1）。
- **不變量**：形狀、角度、**長度比**、**面積比**。

### 5.3 仿射變換（affinity）

[▶ 53:03](https://youtu.be/gQ7IUS8NKCI?t=3183)

非奇異線性變換再接一個平移：

$$
H_A=\begin{pmatrix} A & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix},\qquad A=\begin{pmatrix} a_{11} & a_{12}\\ a_{21} & a_{22}\end{pmatrix}\ \text{非奇異}
$$

- 不再有「旋轉矩陣」的限制，$A$ 的 4 個數可以是任何數，只要 $A$ 可逆（$H$ 才可逆）。
- **自由度 6**（$A$ 的 4 + 平移 2）。
- **3 對對應點**就能算出來：每對點給 2 個約束，$3\times2=6$。講者說細節留到 Lecture 4。
- **不變量**：**平行線**、**平行線段的長度比**、**面積比**。

**$A$ 的分解** [▶ 54:24](https://youtu.be/gQ7IUS8NKCI?t=3264)：

$$
A=R(\theta)\,R(-\phi)\,D\,R(\phi),\qquad D=\begin{pmatrix}\lambda_1 & 0\\ 0 & \lambda_2\end{pmatrix}
$$

**推導**（從 SVD）：

1. SVD：$A=UDV^\mathsf{T}$，$U$、$V$ 是正交矩陣，$D$ 是對角矩陣。
2. $V$ 正交 → $V^\mathsf{T}V=I$。在中間插進去：
$$
A=UDV^\mathsf{T}=U(V^\mathsf{T}V)DV^\mathsf{T}=(UV^\mathsf{T})(VDV^\mathsf{T})
$$
3. 兩個正交矩陣相乘還是正交矩陣 → $UV^\mathsf{T}=R(\theta)$，一個旋轉。
4. $V$ 是旋轉，寫成 $V=R(-\phi)$，則 $V^\mathsf{T}=V^{-1}=R(\phi)$。所以 $VDV^\mathsf{T}=R(-\phi)DR(\phi)$。∎

⚠️ 逐字稿缺字 [▶ 56:46](https://youtu.be/gQ7IUS8NKCI?t=3406)：Whisper 把 $V$ 寫成 “R of minus theta”，後面多處把 phi（$\phi$）寫成 “five”（例如「rotated by five degrees」）。依公式應為 $R(-\phi)$、旋轉 $\phi$。

講者說 $D$ 的對角元素是「奇異值，也就是 $A$ 的特徵值」。

> 以下**不是逐字稿內容**，是依線性代數推論的：奇異值一般**不等於**特徵值。只有 $A$ 對稱半正定時兩者才相同。這裡 $D$ 的元素就是 $A$ 的奇異值；$\lambda_1,\lambda_2$ 這個名字只是記號。

**幾何意義**（從右往左讀）[▶ 57:25](https://youtu.be/gQ7IUS8NKCI?t=3445)：

1. $R(\phi)$：先把座標軸轉 $\phi$。
2. $D$：沿著轉過的兩個軸，分別縮放 $\lambda_1$、$\lambda_2$（**非等向縮放**，把形狀拉扁）。
3. $R(-\phi)$：轉回原來的方向。
4. $R(\theta)$：最後再整體轉 $\theta$。

**直覺**：仿射變換 = 旋轉 + 「沿某兩個垂直方向各自拉長或壓扁」。這就是它比相似變換多出來的東西：兩個參數（拉伸方向 $\phi$、拉伸比例 $\lambda_1/\lambda_2$）。

### 5.4 射影變換（projectivity）

[▶ 1:00:03](https://youtu.be/gQ7IUS8NKCI?t=3603)

$$
H_P=\begin{pmatrix} A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}
$$

- 階層最高層，就是一般的非奇異 $3\times3$ 齊次矩陣。9 個元素都可以是任何數，$v$ 也可以是 0。
- **自由度 8**（9 少 1 個縮放）。
- **不能總是把它縮放成 $v=1$**：因為 $v$ 可能是 0。所以一般沒辦法把 $H_P$ 縮放成最後一列是 $(0,0,1)$ 的相似或仿射形式。
- **4 對對應點**就能算出來，任三點不能共線（在任一個平面上）：8 個自由度，每對點 2 個約束。細節在 Lecture 4。
- 2D 射影變換**分不出**保持方向或反轉方向。
- **不變量**：**接觸階數（order of contact）**（相交、相切）、**交比（cross ratio）**（第 6 節）。

### 5.5 總表與分解

[▶ 1:02:34](https://youtu.be/gQ7IUS8NKCI?t=3754)

| 群 | 矩陣 | 自由度 | 不變量 |
|---|---|---|---|
| 射影 | $\begin{pmatrix} A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}$ | 8 | 共線、共點、接觸階數（相交、相切）、交比 |
| 仿射 | $\begin{pmatrix} A & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ | 6 | 平行、平行線段長度比、面積比；**加上射影的全部** |
| 相似 | $\begin{pmatrix} sR & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ | 4 | 角度、長度比；**加上仿射的全部** |
| 歐氏 | $\begin{pmatrix} R & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ | 3 | 長度、面積；**加上相似的全部** |

（表格依 MVG Table 2.1 整理；講者的投影片有同一張總表，逐字稿只說「invariant properties are given here」。）

【課本補充】MVG Table 2.1 還列了：仿射保持 **$\mathbf{l}_\infty$**、**向量的線性組合（例如中點、質心）**；射影的接觸階數還包含反曲點（inflection）和尖點（cusp）。

**分解** [▶ 1:02:55](https://youtu.be/gQ7IUS8NKCI?t=3775)：任何射影變換可以拆成一串，每一個都比前一個在階層裡高一級：

$$
H=H_SH_AH_P=\begin{pmatrix} sR & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\begin{pmatrix} K & \mathbf{0}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\begin{pmatrix} I & \mathbf{0}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}=\begin{pmatrix} A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}
$$

- $H_S$：相似；$H_A$：仿射，其中 $K$ 是**上三角矩陣**；$H_P$：特殊形式的射影（左上是 $I$、右上是 $\mathbf{0}$）。
- $A=sRK+\mathbf{t}\mathbf{v}^\mathsf{T}$。
- **條件**：$v\neq0$ 時分解成立；選 $s>0$ 時分解唯一。
- 講者預告：這個分解怎麼和**無窮遠線**、**circular points** 的保持性質連起來，Lecture 3 會講。

【課本補充】MVG 式 (2.16) 規定 $K$ 正規化成 $\det K=1$。

> 以下**不是逐字稿內容**，是依矩陣乘法推論的關鍵一步：先算 $H_AH_P=\begin{pmatrix}K & \mathbf{0}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}$，再左乘 $H_S$：左上 $=sRK+\mathbf{t}\mathbf{v}^\mathsf{T}$，右上 $=v\mathbf{t}$，下排 $=(\mathbf{v}^\mathsf{T},v)$。右上是 $v\mathbf{t}$ 不是 $\mathbf{t}$；因為整個矩陣是齊次的，可以把 $H$ 先除以 $v$（所以需要 $v\neq0$）讓 $v=1$，這時右上就是 $\mathbf{t}$。

---

## 6. 1D 射影幾何與交比

[▶ 1:04:31](https://youtu.be/gQ7IUS8NKCI?t=3871)

**直覺**：在 2D，點 → 射線、線 → 平面，我們看的是「所有住在一個平面上的東西」。降一維：在 1D，看的是「所有住在一條線上的東西」——只有點（和那條線本身）。

**表示**：

- 點用 **2 維**齊次向量 $\bar{\mathbf{x}}=(x_1,x_2)^\mathsf{T}$。
- $x_2=0$：線上的**理想點**（無窮遠點）。

**1D 射影變換** [▶ 1:06:35](https://youtu.be/gQ7IUS8NKCI?t=3995)：

$$
\bar{\mathbf{x}}'=H_{2\times2}\,\bar{\mathbf{x}}
$$

- 把一條線上的點映到另一條線上。
- **自由度 3**（4 個元素少 1 個縮放）→ **3 對對應點**就能決定。

**交比（cross ratio）** [▶ 1:07:46](https://youtu.be/gQ7IUS8NKCI?t=4066)：

- 2D 射影變換保持的是「直線性」；1D 射影變換保持的是**交比**。
- 交比是 $\mathbb{P}^1$ **最基本的射影不變量**。

給 4 個點 $\bar{\mathbf{x}}_1,\dots,\bar{\mathbf{x}}_4$：

$$
\operatorname{Cross}(\bar{\mathbf{x}}_1,\bar{\mathbf{x}}_2,\bar{\mathbf{x}}_3,\bar{\mathbf{x}}_4)=\frac{|\bar{\mathbf{x}}_1\bar{\mathbf{x}}_2|\,|\bar{\mathbf{x}}_3\bar{\mathbf{x}}_4|}{|\bar{\mathbf{x}}_1\bar{\mathbf{x}}_3|\,|\bar{\mathbf{x}}_2\bar{\mathbf{x}}_4|},\qquad |\bar{\mathbf{x}}_i\bar{\mathbf{x}}_j|=\det\begin{pmatrix} x_{i1} & x_{j1}\\ x_{i2} & x_{j2}\end{pmatrix}=x_{i1}x_{j2}-x_{j1}x_{i2}
$$

- 每個行列式是一個數，整個交比是一個**純量**。
- **不變性**：四個點經過 $H_{2\times2}$ 之後，算出來的交比**一樣**：
$$
\operatorname{Cross}(\bar{\mathbf{x}}_1',\bar{\mathbf{x}}_2',\bar{\mathbf{x}}_3',\bar{\mathbf{x}}_4')=\operatorname{Cross}(\bar{\mathbf{x}}_1,\bar{\mathbf{x}}_2,\bar{\mathbf{x}}_3,\bar{\mathbf{x}}_4)
$$
- 講者把證明**留作練習**，提示：把 $\bar{\mathbf{x}}_i'=H\bar{\mathbf{x}}_i$ 代進交比，$H$ 會互相消掉。

> 以下**不是逐字稿內容**，是依講者提示推論的關鍵一步：$\det\begin{pmatrix} H\bar{\mathbf{x}}_i & H\bar{\mathbf{x}}_j\end{pmatrix}=\det\left(H\begin{pmatrix}\bar{\mathbf{x}}_i & \bar{\mathbf{x}}_j\end{pmatrix}\right)=\det H\cdot|\bar{\mathbf{x}}_i\bar{\mathbf{x}}_j|$。分子分母各有兩個行列式，$(\det H)^2$ 消掉。

【課本補充】（MVG §2.5）

- 交比的值和選哪個齊次代表無關（縮放在分子分母消掉）。
- 若四點都是有限點、且取 $x_2=1$，$|\bar{\mathbf{x}}_i\bar{\mathbf{x}}_j|$ 就是 $\bar{\mathbf{x}}_i$ 到 $\bar{\mathbf{x}}_j$ 的**有號距離**。所以交比是「比值的比值」：仿射變換保持長度比，射影變換連長度比都不保持，但保持交比。
- 其中一個點是理想點時，定義仍然成立。
- 2D 射影變換會在平面上任一條線上**誘導**出一個 1D 射影變換。

**幾何圖像** [▶ 1:09:35](https://youtu.be/gQ7IUS8NKCI?t=4175)：在 1D，一個點是「一條射線和一條線的交點」。$H_{2\times2}$ 把一條線變到另一條線，同一組射線在兩條線上交出的四個點，交比相同。

**共點線（concurrent lines）** [▶ 1:10:41](https://youtu.be/gQ7IUS8NKCI?t=4241)：

- 「一條線上的共線點」的**對偶**是「通過同一點的共點線」。所以共點線也有 $\mathbb{P}^1$ 的幾何，**四條共點線也有交比**。
- 四條通過同一點的線，被任何一條線截出的四個交點，交比都一樣。
- **投影解釋**：平面上的點 $\mathbf{x}_i$，經過投影中心 $\mathbf{c}$ 投影到同平面上的一條線 $\mathbf{l}$ 上，得到 $\bar{\mathbf{x}}_i$。這就是**把 2D 投影成 1D 影像**；這些像點的交比不變。

---

## 7. Lecture 1 總結

[▶ 1:12:39](https://youtu.be/gQ7IUS8NKCI?t=4359)

Lecture 1 學到：

1. 歐氏幾何和射影幾何的差別。
2. 用齊次座標表示射影空間中的點、線、二次曲線。
3. 點與線、二次曲線與對偶二次曲線的對偶關係。
4. 變換階層作用在點、線、二次曲線上。
5. 1D 射影幾何的性質。

---

## 8. 一頁速查表

### 二次曲線

| 公式 | 關鍵一步 |
|---|---|
| $\mathbf{x}^\mathsf{T}C\mathbf{x}=0$，$C$ 對稱，5 dof | 代 $x\to x_1/x_3$、$y\to x_2/x_3$，乘 $x_3^2$ |
| 5 點決定：$A_{5\times6}\mathbf{c}=0$ | 每點給一列 $(x^2,xy,y^2,x,y,1)$；$\mathbf{c}$ = 零空間 |
| 切線 $\mathbf{l}=C\mathbf{x}$ | $\mathbf{l}^\mathsf{T}\mathbf{x}=\mathbf{x}^\mathsf{T}C\mathbf{x}=0$；若再碰一點 $\mathbf{y}$ 則整條線在曲線上（退化） |
| 對偶 $\mathbf{l}^\mathsf{T}C^*\mathbf{l}=0$，$C^*=C^{-1}$ | $\mathbf{x}=C^{-1}\mathbf{l}$ 代回 $\mathbf{x}^\mathsf{T}C\mathbf{x}=0$ |
| 退化：rank 2 = 兩線 $\mathbf{l}\mathbf{m}^\mathsf{T}+\mathbf{m}\mathbf{l}^\mathsf{T}$；rank 1 = 重線 $\mathbf{l}\mathbf{l}^\mathsf{T}$ | $\mathbf{x}^\mathsf{T}C\mathbf{x}=2(\mathbf{l}^\mathsf{T}\mathbf{x})(\mathbf{m}^\mathsf{T}\mathbf{x})$ |
| 退化對偶：rank 2 = 兩點 $\mathbf{x}\mathbf{y}^\mathsf{T}+\mathbf{y}\mathbf{x}^\mathsf{T}$ | 退化時 $C^*\neq C^{-1}$ |

### 變換規則（點 $\mathbf{x}'=H\mathbf{x}$）

| 物件 | 變成 | 關鍵一步 |
|---|---|---|
| 線 | $\mathbf{l}'=H^{-\mathsf{T}}\mathbf{l}$ | $\mathbf{l}^\mathsf{T}H^{-1}H\mathbf{x}=0$ |
| 二次曲線 | $C'=H^{-\mathsf{T}}CH^{-1}$ | 代 $\mathbf{x}=H^{-1}\mathbf{x}'$ |
| 對偶二次曲線 | $C^{*\prime}=HC^*H^\mathsf{T}$ | 對 $C'$ 取逆 |

### 變換階層

| 群 | dof | 求解需要 | 新增的不變量 |
|---|---|---|---|
| 歐氏／等距 | 3 | — | 長度、面積 |
| 相似 | 4 | — | 角度、長度比、形狀 |
| 仿射 | 6 | 3 對點 | 平行、平行線段長度比、面積比 |
| 射影 | 8 | 4 對點（任三點不共線） | 共線、相切、交比 |

- 仿射分解：$A=R(\theta)R(-\phi)DR(\phi)$，關鍵一步 $UDV^\mathsf{T}=(UV^\mathsf{T})(VDV^\mathsf{T})$。
- 射影分解：$H=H_SH_AH_P$，$A=sRK+\mathbf{t}\mathbf{v}^\mathsf{T}$（$v\neq0$；$s>0$ 時唯一）。

### 1D

- $\bar{\mathbf{x}}=(x_1,x_2)^\mathsf{T}$，$H_{2\times2}$ 有 3 dof，3 對點決定。
- 交比 $\dfrac{|\bar{\mathbf{x}}_1\bar{\mathbf{x}}_2||\bar{\mathbf{x}}_3\bar{\mathbf{x}}_4|}{|\bar{\mathbf{x}}_1\bar{\mathbf{x}}_3||\bar{\mathbf{x}}_2\bar{\mathbf{x}}_4|}$ 不變；關鍵一步 $|H\bar{\mathbf{x}}_iH\bar{\mathbf{x}}_j|=\det H\,|\bar{\mathbf{x}}_i\bar{\mathbf{x}}_j|$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 射影變換 $\mathbf{x}'=H\mathbf{x}$、4 點決定 | 第 08–09 集（Lecture 4：DLT、強健 homography 估計） |
| 用零空間解齊次線性方程、SVD | 第 08 集（DLT）；整門課的估計問題 |
| 變換階層、分解 $H_SH_AH_P$ | 第 05–07 集（Lecture 3：從影像恢復仿射、度量性質） |
| 對偶二次曲線、$C^{*\prime}=HC^*H^\mathsf{T}$ | 第 05–07 集（circular points 的對偶二次曲線 $C_\infty^*$） |
| 2D 旋轉、平移 | 第 03–04 集（Lecture 2：3D 剛體運動） |
| 交比 | 第 13–15 集（Lecture 6：單視角量測） |
| 透視影像 = 中心投影 | 第 10–12 集（Lecture 5：相機模型） |

---

## 附：本集一句話總結

> **二次曲線用對稱矩陣 $C$ 表示（5 點決定、切線 $C\mathbf{x}$、對偶是 $C^{-1}$）；射影變換就是可逆的 $3\times3$ 矩陣，點、線、二次曲線各有自己的變法；從歐氏、相似、仿射到射影，自由度 3→4→6→8，保住的性質越來越少，最後只剩共線和交比。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 1 (Part 2) 錄影逐字稿（Whisper `medium.en`，1:13:14）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §2.2.3–2.5 整理。*
