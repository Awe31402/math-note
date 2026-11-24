---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 06
lecture: Lecture 3 (Part 2) – Circular points and Absolute conic
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/tsO6VO1s_x8
notes: MVG §2.7.4–2.7.5（書頁 54–57，PDF 頁 72–75）
---

# 第 06 集 · Lecture 3 (Part 2)：用 C*∞ 量角度、度量校正 [▶ 影片](https://youtu.be/tsO6VO1s_x8)

← 上一集：[05-circular-points-absolute-conic-part1](05-circular-points-absolute-conic-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[07-circular-points-absolute-conic-part3](07-circular-points-absolute-conic-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 06 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（33:50，Whisper `medium.en` 轉錄）＋ MVG §2.7.4–2.7.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 射影平面上的角度](#1-射影平面上的角度)
  - [1.1 歐氏公式為什麼不行](#11-歐氏公式為什麼不行)
  - [1.2 加入 C*∞ 的公式](#12-加入-c-的公式)
  - [1.3 垂直條件](#13-垂直條件)
- [2. 從 C*∞ 的像恢復度量性質](#2-從-c-的像恢復度量性質)
  - [2.1 C*∞ 的像長什麼樣](#21-c-的像長什麼樣)
  - [2.2 用 SVD 直接求校正矩陣](#22-用-svd-直接求校正矩陣)
- [3. 度量校正 I：兩步法（先仿射、再度量）](#3-度量校正-i兩步法先仿射再度量)
- [4. 度量校正 II：一步法](#4-度量校正-ii一步法)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

接續第 05 集定義的 $C_\infty^*$（circular points 的對偶二次曲線）：

| 主題 | MVG |
|---|---|
| 用 $C_\infty^*$ 在射影平面上量角度 | §2.7.4 |
| 從 $C_\infty^*$ 的像去除射影 + 仿射失真（只剩相似失真） | §2.7.5 |
| 度量校正 I（兩步、分層法）、II（一步法） | Example 2.26、2.27 |

---

## 1. 射影平面上的角度

### 1.1 歐氏公式為什麼不行

[▶ 00:00](https://youtu.be/tsO6VO1s_x8?t=0)

兩條線 $\mathbf{l}=(l_1,l_2,l_3)^\mathsf{T}$、$\mathbf{m}=(m_1,m_2,m_3)^\mathsf{T}$，夾角 $\theta$。

- 第 01 集：線的**法向量**是前兩個分量，$(l_1,l_2)$ 和 $(m_1,m_2)$。
- 兩線夾角 = 兩法向量夾角，用內積：
$$
(l_1,l_2)\begin{pmatrix}m_1\\m_2\end{pmatrix}=\left\|(l_1,l_2)\right\|\left\|(m_1,m_2)\right\|\cos\theta
$$
$$
\cos\theta=\frac{l_1m_1+l_2m_2}{\sqrt{(l_1^2+l_2^2)(m_1^2+m_2^2)}}
$$

**問題** [▶ 02:46](https://youtu.be/tsO6VO1s_x8?t=166)：這個式子在射影變換下**沒有定義**。

- 線變換後 $\mathbf{l}'=H^{-\mathsf{T}}\mathbf{l}$、$\mathbf{m}'=H^{-\mathsf{T}}\mathbf{m}$，但不能直接把 $\mathbf{l}'$、$\mathbf{m}'$ 的前兩個分量代進去，算出變換後的真實角度。
- 所以這個式子在仿射或射影變換之後不能用。

【課本補充】MVG §2.7.4：原因是線的「前兩個分量」在射影變換下沒有良好的變換性質（它們不是張量）。

### 1.2 加入 C*∞ 的公式

[▶ 03:43](https://youtu.be/tsO6VO1s_x8?t=223)

把 $C_\infty^*$ 夾在中間，用**整個**齊次向量（三個分量都用）：

$$
\cos\theta=\frac{\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}}{\sqrt{(\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{l})(\mathbf{m}^\mathsf{T}C_\infty^*\mathbf{m})}}
$$

**在歐氏座標系下退化成原公式** [▶ 04:36](https://youtu.be/tsO6VO1s_x8?t=276)：代 $C_\infty^*=\operatorname{diag}(1,1,0)$：

$$
\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}=\begin{pmatrix}l_1&l_2&l_3\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}\begin{pmatrix}m_1\\m_2\\m_3\end{pmatrix}=l_1m_1+l_2m_2
$$

分母同理。

**好處：在射影變換下不變** [▶ 05:20](https://youtu.be/tsO6VO1s_x8?t=320)。

**證明**：點變換 $\mathbf{x}'=H\mathbf{x}$ 下，

- 線：$\mathbf{l}'=H^{-\mathsf{T}}\mathbf{l}$，所以 $\mathbf{l}'^\mathsf{T}=\mathbf{l}^\mathsf{T}H^{-1}$。
- 對偶二次曲線：$C_\infty^{*\prime}=HC_\infty^*H^\mathsf{T}$（第 02 集）。

分子變成

$$
\mathbf{l}'^\mathsf{T}C_\infty^{*\prime}\mathbf{m}'=\mathbf{l}^\mathsf{T}\underbrace{H^{-1}H}_{I}C_\infty^*\underbrace{H^\mathsf{T}H^{-\mathsf{T}}}_{I}\mathbf{m}=\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}
$$

- 分母形式一樣，也不變。
- $\mathbf{l}$、$\mathbf{m}$ 的縮放在分子分母間消掉。
- 所以：**只要在影像上找出 $C_\infty^*$ 的像，就能量出真實的歐氏角度**——不管影像經過什麼射影變換。

【課本補充】MVG Result 2.23：一旦在射影平面上找到 $C_\infty^*$，就能用上式量歐氏角度。

### 1.3 垂直條件

[▶ 08:21](https://youtu.be/tsO6VO1s_x8?t=501)

> **Result 2.24（MVG）** 若 $\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}=0$，則 $\mathbf{l}$、$\mathbf{m}$ 垂直。

- 直接從角度公式：$\theta=90^\circ$ → $\cos\theta=0$ → 分子為 0。
- 用途：場景裡已知垂直的兩條線，給出一個關於 $C_\infty^*$ 的**約束**。

⚠️ 逐字稿缺字：Whisper 把 orthogonal 寫成 “octagonal”。

【課本補充】（MVG §2.7.4）

- 幾何上，滿足 $\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}=0$ 的兩條線對 $C_\infty^*$ 是**共軛（conjugate）**的。
- 找到 $C_\infty^*$ 也能量**長度比**：三角形 $a,b,c$ 用上式算出兩個角的 $\cos$，再用正弦定理 $d(b,c):d(a,c)=\sin\alpha:\sin\beta$。

---

## 2. 從 C*∞ 的像恢復度量性質

### 2.1 C*∞ 的像長什麼樣

[▶ 09:03](https://youtu.be/tsO6VO1s_x8?t=543)

> **Result 2.25（MVG）** 一旦在射影平面上找到 $C_\infty^*$，就能把射影失真校正到**只差一個相似變換**。

**推導** [▶ 09:37](https://youtu.be/tsO6VO1s_x8?t=577)：點變換 $\mathbf{x}'=H\mathbf{x}$（$\mathbf{x}$ 在歐氏座標系，$\mathbf{x}'$ 在影像）。用第 02 集的分解 $H=H_PH_AH_S$：

$$
C_\infty^{*\prime}=(H_PH_AH_S)\,C_\infty^*\,(H_PH_AH_S)^\mathsf{T}=(H_PH_A)\underbrace{H_SC_\infty^*H_S^\mathsf{T}}_{=C_\infty^*\ (\text{第 05 集})}(H_PH_A)^\mathsf{T}=(H_PH_A)\,C_\infty^*\,(H_PH_A)^\mathsf{T}
$$

- 相似部分 $H_S$ 被 $C_\infty^*$「**吸收**」了，因為 $C_\infty^*$ 在相似變換下不變。
- 剩下 $H_P$、$H_A$，乘開得到（講者只說「得到這個最終矩陣」）：

$$
C_\infty^{*\prime}=\begin{pmatrix} KK^\mathsf{T} & KK^\mathsf{T}\mathbf{v}\\ \mathbf{v}^\mathsf{T}KK^\mathsf{T} & \mathbf{v}^\mathsf{T}KK^\mathsf{T}\mathbf{v}\end{pmatrix}
$$

（矩陣依 MVG 式 (2.23) 補上。）

> 以下**不是逐字稿內容**，是乘開的關鍵一步：取 $H_A=\begin{pmatrix}K&\mathbf{0}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$、$H_P=\begin{pmatrix}I&\mathbf{0}\\\mathbf{v}^\mathsf{T}&1\end{pmatrix}$，則 $H_PH_A=\begin{pmatrix}K&\mathbf{0}\\\mathbf{v}^\mathsf{T}K&1\end{pmatrix}$。$C_\infty^*=\begin{pmatrix}I&\mathbf{0}\\\mathbf{0}^\mathsf{T}&0\end{pmatrix}$ 把最後一行一列清零，所以
> $$(H_PH_A)C_\infty^*(H_PH_A)^\mathsf{T}=\begin{pmatrix}K\\\mathbf{v}^\mathsf{T}K\end{pmatrix}\begin{pmatrix}K^\mathsf{T}&K^\mathsf{T}\mathbf{v}\end{pmatrix}$$
> 就是上面的矩陣。

**結論** [▶ 11:22](https://youtu.be/tsO6VO1s_x8?t=682)：

- $C_\infty^*$ 的像決定了**射影部分 $\mathbf{v}$** 和**仿射部分 $K$**。
- **相似部分決定不了**：它被吸收進 $C_\infty^*$，沒有留下任何痕跡。
- 所以在影像上觀察到 $C_\infty^{*\prime}$，就能解出 $\mathbf{v}$ 和 $K$。

### 2.2 用 SVD 直接求校正矩陣

[▶ 13:03](https://youtu.be/tsO6VO1s_x8?t=783)

在影像上找到 $C_\infty^{*\prime}$ 後，對它做 SVD：

$$
C_\infty^{*\prime}=U\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}U^\mathsf{T}
$$

【口頭】講者複習 SVD [▶ 13:52](https://youtu.be/tsO6VO1s_x8?t=832)：

- 一般 $n\times m$ 矩陣 $A$ 的 SVD 是 $U\Sigma V^\mathsf{T}$，$U$ 是 $n\times n$、$\Sigma$ 是 $n\times m$ 對角、$V$ 是 $m\times m$；$U$、$V$ 是左、右正交矩陣。
- 對**對稱方陣** $C$，SVD 可以寫成 $U\Sigma U^\mathsf{T}$，左右兩個 $U$ 一樣。
- $\Sigma$ 的非零對角元素個數 = 矩陣的 **rank**。

講者說 $\Sigma$ 的元素是「特徵值」。

> 以下**不是逐字稿內容**，是依線性代數推論的：一般矩陣的奇異值不是特徵值。對稱**半正定**矩陣（例如 $C_\infty^{*\prime}=HC_\infty^*H^\mathsf{T}$，因為 $C_\infty^*$ 半正定）的奇異值才等於特徵值，SVD 才能寫成 $U\Sigma U^\mathsf{T}$。

- $C_\infty^*$ 是 rank 2（退化），所以 $C_\infty^{*\prime}$ 也是 rank 2，SVD 只有兩個非零奇異值，第三個是 0。
- 中間的 $\operatorname{diag}(1,1,0)$ 就是 $C_\infty^*$ → 和 $C_\infty^{*\prime}=HC_\infty^*H^\mathsf{T}$ 比對，**$H=U$**（差一個相似變換）。

> 以下**不是逐字稿內容**，是依 SVD 推論的補充：實際算出來的奇異值一般是 $(\sigma_1,\sigma_2,0)$，不剛好是 $(1,1,0)$。這時 $C_\infty^{*\prime}=U\operatorname{diag}(\sigma_1,\sigma_2,0)U^\mathsf{T}=\left(U\operatorname{diag}(\sqrt{\sigma_1},\sqrt{\sigma_2},1)\right)C_\infty^*\left(U\operatorname{diag}(\sqrt{\sigma_1},\sqrt{\sigma_2},1)\right)^\mathsf{T}$，所以 $H=U\operatorname{diag}(\sqrt{\sigma_1},\sqrt{\sigma_2},1)$。用 $H^{-1}$ 校正影像。MVG 寫的 $\operatorname{diag}(1,1,0)$ 是已經把這個縮放吸收掉的情況。

---

## 3. 度量校正 I：兩步法（先仿射、再度量）

[▶ 18:02](https://youtu.be/tsO6VO1s_x8?t=1082)

**在解什麼**：第 05 集用消失線做完仿射校正，影像裡平行線已經平行，但直角還不是直角（剩仿射失真）。現在要去掉仿射失真。

**設定** [▶ 19:46](https://youtu.be/tsO6VO1s_x8?t=1186)：

$$
C_\infty^{*\prime}=H_PH_AC_\infty^*H_A^\mathsf{T}H_P^\mathsf{T}
\quad\Longrightarrow\quad
\underbrace{H_P^{-1}C_\infty^{*\prime}H_P^{-\mathsf{T}}}_{C_\infty^{*\prime\prime}}=H_AC_\infty^*H_A^\mathsf{T}
$$

- $C_\infty^{*\prime\prime}$：**仿射校正後**的影像裡 $C_\infty^*$ 的像——射影失真已去掉，仿射失真還在。
- 目標：在仿射校正後的影像上找出 $C_\infty^{*\prime\prime}$，求出 $H_A$，去掉仿射失真。

**約束來源：一對垂直線** [▶ 22:14](https://youtu.be/tsO6VO1s_x8?t=1334)：

- 在仿射校正後的影像上，找兩條在**真實世界中垂直**的線 $\mathbf{l}'=(l_1',l_2',l_3')^\mathsf{T}$、$\mathbf{m}'=(m_1',m_2',m_3')^\mathsf{T}$。（在影像上看起來不垂直。）
- 每條線用線上兩點的外積求得。
- 垂直條件：
$$
\mathbf{l}'^\mathsf{T}C_\infty^{*\prime\prime}\mathbf{m}'=\mathbf{l}'^\mathsf{T}H_AC_\infty^*H_A^\mathsf{T}\mathbf{m}'=0
$$
- 代 $H_A=\begin{pmatrix}K&\mathbf{0}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$、$C_\infty^*=\operatorname{diag}(1,1,0)$（即 $\mathbf{v}=\mathbf{0}$ 的式 (2.23)）：
$$
\begin{pmatrix}l_1'&l_2'&l_3'\end{pmatrix}\begin{pmatrix}KK^\mathsf{T}&\mathbf{0}\\\mathbf{0}^\mathsf{T}&0\end{pmatrix}\begin{pmatrix}m_1'\\m_2'\\m_3'\end{pmatrix}=0
\quad\Longleftrightarrow\quad
\begin{pmatrix}l_1'&l_2'\end{pmatrix}S\begin{pmatrix}m_1'\\m_2'\end{pmatrix}=0,\qquad S=KK^\mathsf{T}
$$

**化成線性方程式** [▶ 25:05](https://youtu.be/tsO6VO1s_x8?t=1505)：

- $S$ 是 $2\times2$，4 個元素。$KK^\mathsf{T}$ **對稱** → $s_{12}=s_{21}$ → 只有 3 個獨立元素 $s_{11},s_{12},s_{22}$。
- 展開 $(l_1',l_2')S(m_1',m_2')^\mathsf{T}=l_1'm_1's_{11}+(l_1'm_2'+l_2'm_1')s_{12}+l_2'm_2's_{22}$：
$$
\begin{pmatrix} l_1'm_1' & l_1'm_2'+l_2'm_1' & l_2'm_2'\end{pmatrix}\mathbf{s}=0,\qquad \mathbf{s}=(s_{11},s_{12},s_{22})^\mathsf{T}
$$
- 每對垂直線給**一條**方程式。
- $\mathbf{s}$ 有 3 個未知數但差一個縮放 → 2 個自由度 → 需要**兩對垂直線**。
- 疊起來：$2\times3$ 矩陣乘 $\mathbf{s}$ 等於 0，又是 $A\mathbf{x}=\mathbf{0}$，求零空間得 $\mathbf{s}$。

⚠️ 逐字稿缺字 [▶ 25:37](https://youtu.be/tsO6VO1s_x8?t=1537)：講者先說「$K$ 是對稱矩陣」，馬上改口「$KK^\mathsf{T}$ 是對稱矩陣」。正確的是後者。

**從 $S$ 求 $K$** [▶ 27:47](https://youtu.be/tsO6VO1s_x8?t=1667)：$S=KK^\mathsf{T}$，$K$ 是 $S$ 的「平方根」，用 **Cholesky 分解**求。

- 有了 $K$ 就有 $H_A$，用它去掉仿射失真，只剩**相似失真**。
- 相似失真去不掉，除非知道 3D 場景中的對應點。

⚠️ 逐字稿缺字：Whisper 把 Cholesky 寫成 “kolinsky”。

【課本補充】（MVG Example 2.26）

- 仿射校正後，circular points 只剩 2 個自由度要決定，所以需要 2 個約束。
- 除了兩對直角，也可以用**一個圓**（在仿射校正後的影像裡是橢圓，它和已知的 $\mathbf{l}_\infty$ 的交點就是 circular points 的像），或**兩個已知長度比**。

**什麼時候會失敗**：

> 以下**不是逐字稿內容**，是依線性代數推論的：兩對垂直線給出的兩列必須線性獨立。例如兩對線方向一模一樣（兩對其實是同一組方向），兩列就成比例，零空間變成 2 維，解不出唯一的 $\mathbf{s}$。另外，$S$ 必須正定才能做 Cholesky；雜訊大時可能不成立。

---

## 4. 度量校正 II：一步法

[▶ 29:00](https://youtu.be/tsO6VO1s_x8?t=1740)

**在解什麼**：不先找消失線，直接在**原始透視影像**上一次去掉射影 + 仿射失真。

- 直接在透視影像上找 $C_\infty^{*\prime}$（含射影和仿射）：
$$
C_\infty^{*\prime}=\begin{pmatrix} KK^\mathsf{T} & KK^\mathsf{T}\mathbf{v}\\ \mathbf{v}^\mathsf{T}KK^\mathsf{T} & \mathbf{v}^\mathsf{T}KK^\mathsf{T}\mathbf{v}\end{pmatrix}
$$
- 未知數是 $K$（仿射）和 $\mathbf{v}$（射影）。

**約束** [▶ 30:23](https://youtu.be/tsO6VO1s_x8?t=1823)：在透視影像上找真實世界中垂直的線對 $\mathbf{l}'$、$\mathbf{m}'$，代進 $\mathbf{l}'^\mathsf{T}C_\infty^{*\prime}\mathbf{m}'=0$。

- 每對線給一條方程式，寫成 $1\times6$ 列向量乘 6 維未知向量 $\mathbf{c}=(a,b,c,d,e,f)^\mathsf{T}$。
- 講者的數法：$S$ 有 3 個未知、$\mathbf{v}$ 有 3 個未知，共 6 個。
- 6 個未知數差一個縮放 → 需要 **5 個約束**（5 對垂直線）。
- 疊成 $5\times6$ 矩陣乘 $\mathbf{c}$ 等於 0，用 SVD 求零空間。
- 解出 $\mathbf{c}$ 後，代回上式分解出 $K$、$\mathbf{v}$。

> 以下**不是逐字稿內容**：逐字稿沒唸出 $1\times6$ 列向量的內容。依 MVG Example 2.27，把 $C_\infty^{*\prime}$ 當成一般二次曲線寫成
> $$C_\infty^{*\prime}=\begin{pmatrix}a&b/2&d/2\\b/2&c&e/2\\d/2&e/2&f\end{pmatrix}$$
> 每對垂直線的約束是
> $$\left(l_1'm_1',\ \tfrac{l_1'm_2'+l_2'm_1'}{2},\ l_2'm_2',\ \tfrac{l_1'm_3'+l_3'm_1'}{2},\ \tfrac{l_2'm_3'+l_3'm_2'}{2},\ l_3'm_3'\right)\mathbf{c}=0$$
> 求出 $C_\infty^{*\prime}$ 後，用第 2.2 節的 SVD 得校正矩陣。

**名稱** [▶ 33:13](https://youtu.be/tsO6VO1s_x8?t=1993)：

- **兩步法**（先用 $\mathbf{l}_\infty$ 去射影失真，再用 $C_\infty^*$ 去仿射失真）也叫**分層法（stratified approach）**。
- **一步法**：直接在透視影像上找 $C_\infty^*$ 的像，一起解出 $H_P$ 和 $H_A$。

**比較**：

| | 兩步法 | 一步法 |
|---|---|---|
| 需要 | 兩組平行線（找消失線）+ 2 對垂直線 | 5 對垂直線 |
| 未知數 | 每步少（2 dof） | 一次 5 dof |
| 每步解 | $2\times3$ 零空間 | $5\times6$ 零空間 |

> 以下**不是逐字稿內容**，是依未知數個數推論的：一步法 5 對垂直線必須給出 5 個獨立約束；例如全部來自同一組兩個方向（同一個矩形的邊重複用）就會退化。另外解出的 $C_\infty^{*\prime}$ 應該是 rank 2，有雜訊時一般會是 rank 3，需要強制把最小奇異值設成 0。

（本集到 33:43 結束。）

---

## 5. 一頁速查表

### 角度

| 公式 | 關鍵一步 |
|---|---|
| $\cos\theta=\dfrac{\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}}{\sqrt{(\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{l})(\mathbf{m}^\mathsf{T}C_\infty^*\mathbf{m})}}$ | 歐氏座標下 $C_\infty^*=\operatorname{diag}(1,1,0)$ 退化成法向量內積 |
| 射影不變 | $\mathbf{l}^\mathsf{T}H^{-1}\cdot HC_\infty^*H^\mathsf{T}\cdot H^{-\mathsf{T}}\mathbf{m}$ |
| 垂直 ⟺ $\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}=0$ | $\cos90^\circ=0$ |

### C*∞ 的像

$$
C_\infty^{*\prime}=(H_PH_A)C_\infty^*(H_PH_A)^\mathsf{T}=\begin{pmatrix}KK^\mathsf{T}&KK^\mathsf{T}\mathbf{v}\\\mathbf{v}^\mathsf{T}KK^\mathsf{T}&\mathbf{v}^\mathsf{T}KK^\mathsf{T}\mathbf{v}\end{pmatrix}
$$

- 關鍵一步：$H_SC_\infty^*H_S^\mathsf{T}=C_\infty^*$（相似部分被吸收 → 永遠只能校正到差一個相似）。
- SVD：$C_\infty^{*\prime}=U\operatorname{diag}(1,1,0)U^\mathsf{T}$ → $H=U$。

### 度量校正

| 方法 | 每個約束 | 未知數 | 需要 |
|---|---|---|---|
| I 兩步（仿射校正後） | $(l_1m_1,\ l_1m_2+l_2m_1,\ l_2m_2)\,\mathbf{s}=0$，$S=KK^\mathsf{T}$ | 3（2 dof） | 2 對垂直線；$K$ = Cholesky$(S)$ |
| II 一步（原始影像） | $(l_1m_1,\frac{l_1m_2+l_2m_1}{2},l_2m_2,\frac{l_1m_3+l_3m_1}{2},\frac{l_2m_3+l_3m_2}{2},l_3m_3)\,\mathbf{c}=0$ | 6（5 dof） | 5 對垂直線 |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $C_\infty^*$、垂直約束 | 第 07 集（3D 版：絕對二次曲線 $\Omega_\infty$、絕對對偶二次曲面 $Q_\infty^*$） |
| 「用對偶二次曲線的像來量角度」 | 第 10–15 集（絕對二次曲線的像 $\omega$ 和相機內參 $K$：$\omega=(KK^\mathsf{T})^{-1}$） |
| $S=KK^\mathsf{T}$、Cholesky 分解求 $K$ | 第 10–12 集（相機校正：從 $\omega$ 求內參 $K$）；Lecture 13 自校正 |
| 疊約束、求零空間 | 第 08 集（DLT）；第 10–12 集（Zhang 校正法） |
| 分層法（先仿射再度量） | 第 27–30 集（射影重建 → 仿射 → 度量重建） |

---

## 附：本集一句話總結

> **把 $C_\infty^*$ 夾進內積，角度公式就在射影變換下不變；$C_\infty^*$ 的像裡藏著射影部分 $\mathbf{v}$ 和仿射部分 $K$（相似部分被吸收），所以每對已知垂直的線給一條線性約束——仿射校正後 2 對就夠（解 $S=KK^\mathsf{T}$ 再 Cholesky），從原始影像直接做則要 5 對。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 3 (Part 2) 錄影逐字稿（Whisper `medium.en`，33:50）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §2.7.4–2.7.5 整理。*
