---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 07
lecture: Lecture 3 (Part 3) – Circular points and Absolute conic
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/k63Bi74Meyc
notes: MVG §3.5–3.7（書頁 79–85，PDF 頁 97–103）
---

# 第 07 集 · Lecture 3 (Part 3)：無窮遠平面、絕對二次曲線、絕對對偶二次曲面 [▶ 影片](https://youtu.be/k63Bi74Meyc)

← 上一集：[06-circular-points-absolute-conic-part2](06-circular-points-absolute-conic-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[08-robust-homography-part1](08-robust-homography-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 07 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（34:12，Whisper `medium.en` 轉錄）＋ MVG §3.5–3.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 無窮遠平面 π∞](#1-無窮遠平面-π)
  - [1.1 定義與平行性](#11-定義與平行性)
  - [1.2 π∞ 在仿射變換下不動](#12-π-在仿射變換下不動)
  - [1.3 兩點說明，與一個例子](#13-兩點說明與一個例子)
- [2. 絕對二次曲線 Ω∞](#2-絕對二次曲線-ω)
  - [2.1 定義](#21-定義)
  - [2.2 Ω∞ 在相似變換下不動](#22-ω-在相似變換下不動)
  - [2.3 性質](#23-性質)
  - [2.4 用 Ω∞ 量兩線夾角](#24-用-ω-量兩線夾角)
- [3. 絕對對偶二次曲面 Q*∞](#3-絕對對偶二次曲面-q)
- [4. Lecture 3 總結](#4-lecture-3-總結)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

把第 05–06 集的 2D 概念推廣到 3D：

| 2D（第 05–06 集） | 3D（本集） | 不動的條件 | MVG |
|---|---|---|---|
| 無窮遠線 $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$ | **無窮遠平面** $\boldsymbol{\pi}_\infty=(0,0,0,1)^\mathsf{T}$ | 仿射 | §3.5 |
| circular points $\mathbf{I},\mathbf{J}$ | **絕對二次曲線** $\Omega_\infty$ | 相似 | §3.6 |
| $C_\infty^*$ | **絕對對偶二次曲面** $Q_\infty^*$ | 相似 | §3.7 |

---

## 1. 無窮遠平面 π∞

### 1.1 定義與平行性

[▶ 00:00](https://youtu.be/k63Bi74Meyc?t=0)

**標準位置**：

$$
\boldsymbol{\pi}_\infty=(0,0,0,1)^\mathsf{T}
$$

- 這是 2D $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$ 的直接推廣。
- $\boldsymbol{\pi}_\infty$ 包含所有**理想點** $\mathbf{D}=(X_1,X_2,X_3,0)^\mathsf{T}$。
- 驗證：$\boldsymbol{\pi}_\infty^\mathsf{T}\mathbf{D}=0\cdot X_1+0\cdot X_2+0\cdot X_3+1\cdot0=0$。
- 這些理想點代表**方向**：從有限空間指向無窮遠。

⚠️ 逐字稿缺字 [▶ 00:41](https://youtu.be/k63Bi74Meyc?t=41)：Whisper 寫 “x1, x2, x3, and x0”，應為 $(X_1,X_2,X_3,0)$。

**用 $\boldsymbol{\pi}_\infty$ 判斷仿射性質（平行）** [▶ 01:30](https://youtu.be/k63Bi74Meyc?t=90)：

- **兩個平面平行** ⟺ 它們的交線在 $\boldsymbol{\pi}_\infty$ 上。
- **一條線和另一條線（或一個平面）平行** ⟺ 交點在無窮遠（在 $\boldsymbol{\pi}_\infty$ 上）。
- 例：兩條平行線交於理想點 $\mathbf{D}=(X_1,X_2,X_3,0)^\mathsf{T}$，它在 $\boldsymbol{\pi}_\infty$ 上。

### 1.2 π∞ 在仿射變換下不動

[▶ 02:41](https://youtu.be/k63Bi74Meyc?t=161)

> **Result 3.7（MVG）** $\boldsymbol{\pi}_\infty$ 在射影變換 $H$ 下是不動平面，若且唯若 $H$ 是**仿射變換**。

**驗證**（講者的「簡單證明」）：平面的變換是 $\boldsymbol{\pi}'=H^{-\mathsf{T}}\boldsymbol{\pi}$（第 04 集），$H_A$ 是 $4\times4$：

$$
H_A^{-\mathsf{T}}\boldsymbol{\pi}_\infty=\begin{pmatrix}A^{-\mathsf{T}} & \mathbf{0}\\ -\mathbf{t}^\mathsf{T}A^{-\mathsf{T}} & 1\end{pmatrix}\begin{pmatrix}0\\0\\0\\1\end{pmatrix}=\begin{pmatrix}\mathbf{0}\\1\end{pmatrix}=\boldsymbol{\pi}_\infty
$$

（$H_A^{-\mathsf{T}}$ 的分塊形式和第 05 集 2D 版一樣，只是 $A$ 換成 $3\times3$；講者只說「代進去算回 $\boldsymbol{\pi}_\infty$」。）

【課本補充】MVG 說證明和 2D 的 Result 2.17 類比。

### 1.3 兩點說明，與一個例子

[▶ 03:43](https://youtu.be/k63Bi74Meyc?t=223)

**說明 1**：$\boldsymbol{\pi}_\infty$ 在仿射變換下只是**整體不動（fixed as a set）**，**不是逐點不動**。

- 和 $\mathbf{l}_\infty$ 一樣：變換後它還是 $\boldsymbol{\pi}_\infty$，但上面的點可能換位置，只是都還在 $\boldsymbol{\pi}_\infty$ 裡。

**說明 2** [▶ 04:37](https://youtu.be/k63Bi74Meyc?t=277)：在**某個特定**的仿射變換下（例如某個歐氏運動），除了 $\boldsymbol{\pi}_\infty$ 之外，**可能還有其他平面也不動**。但**只有 $\boldsymbol{\pi}_\infty$ 對所有仿射變換都不動**。

**例子**（MVG Example 3.8）[▶ 05:40](https://youtu.be/k63Bi74Meyc?t=340)：繞 $z$ 軸轉 $\theta$、沒有平移：

$$
H_E=\begin{pmatrix}\cos\theta & -\sin\theta & 0 & 0\\ \sin\theta & \cos\theta & 0 & 0\\ 0&0&1&0\\0&0&0&1\end{pmatrix}
$$

- 旋轉矩陣第三行是 $(0,0,1)$（繞 $z$ 軸）；平移是 $\mathbf{0}$。
- 幾何上：**垂直於 $z$ 軸的平面**（$XY$ 平面族）轉完還是同一個平面 → **不動**。
- 但不是逐點不動：平面上的點（不在軸上的）繞著畫圓。

**代數：不動平面 = 特徵向量** [▶ 07:08](https://youtu.be/k63Bi74Meyc?t=428)：

- 平面 $\mathbf{V}$ 不動，意思是變換後只差一個縮放：
$$
H^{-\mathsf{T}}\mathbf{V}=\lambda\mathbf{V}
$$
- 這正是**特徵方程式** $A\mathbf{x}=\lambda\mathbf{x}$：特徵向量經過 $A$ 只被縮放、不改方向。
- 所以**不動平面就是 $H^{-\mathsf{T}}$（等價地，$H^\mathsf{T}$）的特徵向量**。

> 以下**不是逐字稿內容**，是依特徵方程式推論的關鍵一步：$H^{-\mathsf{T}}\mathbf{V}=\lambda\mathbf{V}$ 兩邊左乘 $H^\mathsf{T}$ 得 $H^\mathsf{T}\mathbf{V}=\lambda^{-1}\mathbf{V}$，所以 $H^{-\mathsf{T}}$ 和 $H^\mathsf{T}$ 的特徵向量相同。MVG 的寫法是「$H^\mathsf{T}$ 的特徵向量」。

**這個例子的特徵向量** [▶ 09:45](https://youtu.be/k63Bi74Meyc?t=585)：$4\times4$ 矩陣有四個特徵向量：

- $\mathbf{E}_1$、$\mathbf{E}_2$：**虛的**，不對應真實平面，忽略。
- $\mathbf{E}_3=(0,0,1,0)^\mathsf{T}$：法向量是 $z$ 軸方向的平面。
- $\mathbf{E}_4=(0,0,0,1)^\mathsf{T}$：就是 $\boldsymbol{\pi}_\infty$。

【課本補充】MVG：特徵值是 $\{e^{i\theta},e^{-i\theta},1,1\}$。

- $\mathbf{E}_3$、$\mathbf{E}_4$ 的特徵值相同（**退化**），所以它們的任何線性組合也是特徵向量 → 一整個**不動平面束**，由 $\mathbf{E}_3$、$\mathbf{E}_4$ 張成。

> 以下**不是逐字稿內容**，是依線性組合推論的直覺：$\alpha\mathbf{E}_3+\beta\mathbf{E}_4=(0,0,\alpha,\beta)^\mathsf{T}$，就是平面 $\alpha Z+\beta=0$，也就是 $Z=$ 常數——所有垂直於 $z$ 軸的平面（$\alpha=0$ 時是 $\boldsymbol{\pi}_\infty$）。

- **這個平面束的軸** [▶ 11:23](https://youtu.be/k63Bi74Meyc?t=683)：垂直於 $z$ 軸的平面和 $\boldsymbol{\pi}_\infty$ 的**交線**。用第 04 集的對偶表示，這條線是 $W^*=\begin{pmatrix}\mathbf{E}_3^\mathsf{T}\\\mathbf{E}_4^\mathsf{T}\end{pmatrix}$。
- 它的零空間由 $(1,0,0,0)^\mathsf{T}$、$(0,1,0,0)^\mathsf{T}$ 張成——$x$、$y$ 方向的無窮遠點。它們的線性組合就是這條無窮遠線上的所有點。

**預告** [▶ 13:07](https://youtu.be/k63Bi74Meyc?t=787)【口頭】：

- **未校正的雙視角重建**：兩張不同視角的照片 → 求相對旋轉、平移 → 三角化 → 得到的 3D 結構只能確定到差一個**射影**變換（用 fundamental matrix 和三角化演算法）。
- 找出 $\boldsymbol{\pi}_\infty$ 後，可以去掉射影模糊，只剩**仿射**模糊。

> 以下**不是逐字稿內容**：講者說這在「Lecture 6」講。依本播放清單，fundamental matrix 是 **Lecture 7**（第 16–19 集），SfM 重建是 Lecture 10（第 27–30 集）；Lecture 6 是單視角量測。講者可能用的是舊版課程編號。

【課本補充】MVG §3.5：把重建中找到的 $\boldsymbol{\pi}_\infty$ 用射影變換送到標準位置 $(0,0,0,1)^\mathsf{T}$ 之後，重建和真實場景之間只差一個不動 $\boldsymbol{\pi}_\infty$ 的變換，由 Result 3.7 它是仿射的，於是可以直接量仿射性質。這和第 05 集 2D 的仿射校正完全類比。

---

## 2. 絕對二次曲線 Ω∞

### 2.1 定義

[▶ 14:07](https://youtu.be/k63Bi74Meyc?t=847)

- 2D：任何圓都和 $\mathbf{l}_\infty$ 交於 circular points $\mathbf{I},\mathbf{J}$。
- 3D：**絕對二次曲線（absolute conic）** $\Omega_\infty$ 是**落在 $\boldsymbol{\pi}_\infty$ 上的一條點二次曲線**。

**定義**：在度量座標系（$\boldsymbol{\pi}_\infty=(0,0,0,1)^\mathsf{T}$）下，$\Omega_\infty$ 上的點滿足**兩條**方程式：

$$
X_1^2+X_2^2+X_3^2=0,\qquad X_4=0
$$

- $X_4=0$：點在 $\boldsymbol{\pi}_\infty$ 上。
- $X_1^2+X_2^2+X_3^2=0$：只有複數解。

**對 $\boldsymbol{\pi}_\infty$ 上的方向**（$X_4=0$），第一條方程式寫成：

$$
\begin{pmatrix}X_1&X_2&X_3\end{pmatrix}I_{3\times3}\begin{pmatrix}X_1\\X_2\\X_3\end{pmatrix}=0
$$

- 所以 $\Omega_\infty$ 對應**矩陣 $C=I$ 的二次曲線**。
- 它由**純虛點**組成，現實中看不到。

**自由度的意義** [▶ 16:31](https://youtu.be/k63Bi74Meyc?t=991)：$\Omega_\infty$ 是「在仿射座標系中確定度量性質，所需的 **5 個額外自由度**」的幾何表示。

⚠️ 逐字稿缺字：Whisper 寫 “in an affine conic”，依 MVG 應為 “in an affine coordinate frame”。

> 以下**不是逐字稿內容**，是依第 03–04 集的自由度推論的：3D 仿射 12 dof、相似 7 dof，差 5；這 5 個自由度正好是 $\boldsymbol{\pi}_\infty$ 上一條二次曲線的自由度（第 02 集：二次曲線 5 dof）。

### 2.2 Ω∞ 在相似變換下不動

[▶ 16:43](https://youtu.be/k63Bi74Meyc?t=1003)

> **Result 3.9（MVG）** $\Omega_\infty$ 在射影變換 $H$ 下是不動的二次曲線，若且唯若 $H$ 是**相似變換**。

**證明**（「只若」方向）[▶ 16:58](https://youtu.be/k63Bi74Meyc?t=1018)：

1. $\Omega_\infty$ 在 $\boldsymbol{\pi}_\infty$ 上 → 能保持 $\Omega_\infty$ 的變換一定保持 $\boldsymbol{\pi}_\infty$。
2. 由 Result 3.7，保持 $\boldsymbol{\pi}_\infty$ 的變換一定是仿射的：
$$
H_A=\begin{pmatrix}A & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix},\quad A\ \text{是}\ 3\times3
$$
3. 限制在 $\boldsymbol{\pi}_\infty$ 上，$\Omega_\infty$ 是矩陣 $I$。二次曲線的變換規則（第 02 集 $C'=H^{-\mathsf{T}}CH^{-1}$）用在 $\boldsymbol{\pi}_\infty$ 上，作用的是 $A$：
$$
A^{-\mathsf{T}}IA^{-1}=I\quad(\text{差縮放})
$$
4. 兩邊取逆：$AA^\mathsf{T}=I$（差縮放）。
5. 所以 $A^{-1}=A^\mathsf{T}$（差縮放）——這是第 03 集旋轉矩陣的**正交**條件。$A$ 是**縮放過的旋轉**（或縮放過的旋轉加鏡射）。
6. $H_A$ 的左上是縮放旋轉、最後一列是 $(0,0,0,1)$ → $H_A$ 是**相似變換**。∎

> 以下**不是逐字稿內容**，是步驟 3 的補充說明：$\boldsymbol{\pi}_\infty$ 上的點 $(\mathbf{d},0)$ 經過 $H_A$ 變成 $(A\mathbf{d},0)$，所以在 $\boldsymbol{\pi}_\infty$ 上，$H_A$ 的作用就是 $3\times3$ 的 $A$（平移 $\mathbf{t}$ 對方向沒有作用）。

### 2.3 性質

[▶ 20:29](https://youtu.be/k63Bi74Meyc?t=1229)

雖然 $\Omega_\infty$ 沒有實點，它有一般二次曲線的所有性質。

1. **整體不動、不是逐點不動**：相似變換下，$\Omega_\infty$ 上的一點可能移到 $\Omega_\infty$ 上的另一點，但**不會被送出 $\Omega_\infty$**。

⚠️ 逐字稿缺字 [▶ 21:16](https://youtu.be/k63Bi74Meyc?t=1276)：講者說「might be mapped off the conic but it will not be outside the conic, it will still remain inside the conic」，前後矛盾。依 MVG，應為「**不會**被送到二次曲線之外」。

2. **所有的圓都和 $\Omega_\infty$ 交於兩點** [▶ 21:30](https://youtu.be/k63Bi74Meyc?t=1290)：
   - 圓所在的平面（支撐平面）$\boldsymbol{\pi}$ 和 $\boldsymbol{\pi}_\infty$ 交於一條線（這就是 $\boldsymbol{\pi}$ 的 $\mathbf{l}_\infty$）。
   - 這條線和 $\Omega_\infty$ 交於兩點。
   - 這兩點就是平面 $\boldsymbol{\pi}$ 的 **circular points** $\mathbf{I},\mathbf{J}$。
   - 這把第 05 集的 2D 概念和 3D 連起來。

3. **所有的球都和 $\boldsymbol{\pi}_\infty$ 交於 $\Omega_\infty$** [▶ 22:39](https://youtu.be/k63Bi74Meyc?t=1359)。

> 以下**不是逐字稿內容**，是依球面方程式推論的關鍵一步（和第 05 集「圓交 $\mathbf{l}_\infty$」同理）：球面 $X_1^2+X_2^2+X_3^2+(\text{含}\ X_4\ \text{的項})=0$，令 $X_4=0$ 只剩 $X_1^2+X_2^2+X_3^2=0$，正是 $\Omega_\infty$。

### 2.4 用 Ω∞ 量兩線夾角

[▶ 22:53](https://youtu.be/k63Bi74Meyc?t=1373)

- 兩條線的方向 $\mathbf{d}_1$、$\mathbf{d}_2$（3 維向量）。在 $\boldsymbol{\pi}_\infty$ 上，它們就是兩條線各自的**理想點**（交 $\boldsymbol{\pi}_\infty$ 的點）。
- 歐氏座標下，夾角是 $\cos\theta=\dfrac{\mathbf{d}_1^\mathsf{T}\mathbf{d}_2}{\sqrt{(\mathbf{d}_1^\mathsf{T}\mathbf{d}_1)(\mathbf{d}_2^\mathsf{T}\mathbf{d}_2)}}$。
- 在**任何射影座標系**下，改寫成：

$$
\cos\theta=\frac{\mathbf{d}_1^\mathsf{T}\Omega_\infty\mathbf{d}_2}{\sqrt{(\mathbf{d}_1^\mathsf{T}\Omega_\infty\mathbf{d}_1)(\mathbf{d}_2^\mathsf{T}\Omega_\infty\mathbf{d}_2)}}
$$

- $\Omega_\infty$ 是 $\boldsymbol{\pi}_\infty$ 上代表絕對二次曲線的矩陣（度量座標系下是 $I$，就退化回歐氏公式）。
- **兩方向垂直** ⟺ $\mathbf{d}_1^\mathsf{T}\Omega_\infty\mathbf{d}_2=0$。

（歐氏公式和射影公式依 MVG §3.6 式 (3.22)–(3.23) 補上；逐字稿只說「內積給出夾角」「用絕對二次曲線優雅地表示」。）

**預告** [▶ 24:47](https://youtu.be/k63Bi74Meyc?t=1487)【口頭】：

- Lecture 5：**絕對二次曲線的像（image of the absolute conic）**可以用來恢復**相機內參**，也就是相機校正。
- Lecture 6（講者的說法）：絕對二次曲線和無窮遠平面可以在重建後去掉仿射模糊，把 3D 重建恢復到只差一個尺度。

---

## 3. 絕對對偶二次曲面 Q*∞

[▶ 25:33](https://youtu.be/k63Bi74Meyc?t=1533)

**定義**：$\Omega_\infty$ 的對偶是 3D 中一個**退化的對偶二次曲面**，叫**絕對對偶二次曲面（absolute dual quadric）**，記作 $Q_\infty^*$。

- **幾何上**：$Q_\infty^*$ 由所有**和 $\Omega_\infty$ 相切的平面**組成。
  - $\Omega_\infty$ 是點二次曲線（由點定義）；$Q_\infty^*$ 由切平面定義。
- $\Omega_\infty$ 是 $Q_\infty^*$ 的「邊緣」，所以 $Q_\infty^*$ 也叫**邊緣二次曲面（rim quadric）**。

**代數** [▶ 26:43](https://youtu.be/k63Bi74Meyc?t=1603)：$4\times4$ 齊次矩陣，**rank 3**，標準形式

$$
Q_\infty^*=\begin{pmatrix} I_{3\times3} & \mathbf{0}\\ \mathbf{0}^\mathsf{T} & 0\end{pmatrix}
$$

- 對比：$\Omega_\infty$ 只是 $I_{3\times3}$；$Q_\infty^*$ 是 $I$ 外面補一行一列 0。

**自由度 = 8** [▶ 27:14](https://youtu.be/k63Bi74Meyc?t=1634)：$4\times4$ 對稱矩陣 10 個獨立元素，減去縮放（1）和 $\det=0$（1），$10-2=8$。

> **Result 3.10（MVG）** $Q_\infty^*$ 在射影變換 $H$ 下不動，若且唯若 $H$ 是**相似變換**。

**證明** [▶ 27:55](https://youtu.be/k63Bi74Meyc?t=1675)：對偶二次曲面的變換是 $Q^{*\prime}=HQ^*H^\mathsf{T}$（第 04 集）。任意射影變換 $H=H_PH_AH_S=\begin{pmatrix}A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}$：

$$
HQ_\infty^*H^\mathsf{T}=\begin{pmatrix}A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}\begin{pmatrix}I & \mathbf{0}\\ \mathbf{0}^\mathsf{T} & 0\end{pmatrix}\begin{pmatrix}A^\mathsf{T} & \mathbf{v}\\ \mathbf{t}^\mathsf{T} & v\end{pmatrix}=\begin{pmatrix}AA^\mathsf{T} & A\mathbf{v}\\ \mathbf{v}^\mathsf{T}A^\mathsf{T} & \mathbf{v}^\mathsf{T}\mathbf{v}\end{pmatrix}
$$

（乘開的結果是依分塊乘法補上的；逐字稿只說「得到這個矩陣」。）

要等於 $Q_\infty^*=\begin{pmatrix}I&\mathbf{0}\\\mathbf{0}^\mathsf{T}&0\end{pmatrix}$（差縮放）：

1. 左上 $AA^\mathsf{T}=I$（差縮放）→ $A$ 是**縮放過的正交矩陣**（旋轉乘縮放）。
2. 其他項 $A\mathbf{v}$、$\mathbf{v}^\mathsf{T}\mathbf{v}$ 都要是 0 → $\mathbf{v}=\mathbf{0}$。
3. 所以 $H=\begin{pmatrix}sR & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$，是**相似變換**。∎

> **Result 3.11（MVG）** $\boldsymbol{\pi}_\infty$ 是 $Q_\infty^*$ 的零向量。

**驗證** [▶ 30:12](https://youtu.be/k63Bi74Meyc?t=1812)：度量座標系下

$$
Q_\infty^*\boldsymbol{\pi}_\infty=\begin{pmatrix}I&\mathbf{0}\\\mathbf{0}^\mathsf{T}&0\end{pmatrix}\begin{pmatrix}0\\0\\0\\1\end{pmatrix}=\mathbf{0}
$$

**在任何射影變換後仍成立** [▶ 31:06](https://youtu.be/k63Bi74Meyc?t=1866)：$Q^{*\prime}=HQ_\infty^*H^\mathsf{T}$、$\boldsymbol{\pi}'=H^{-\mathsf{T}}\boldsymbol{\pi}_\infty$，

$$
Q^{*\prime}\boldsymbol{\pi}'=HQ_\infty^*\underbrace{H^\mathsf{T}H^{-\mathsf{T}}}_{I}\boldsymbol{\pi}_\infty=H\left(Q_\infty^*\boldsymbol{\pi}_\infty\right)=\mathbf{0}
$$

**兩平面夾角** [▶ 31:46](https://youtu.be/k63Bi74Meyc?t=1906)：

> **Result 3.12（MVG）**
> $$\cos\theta=\frac{\boldsymbol{\pi}_1^\mathsf{T}Q_\infty^*\boldsymbol{\pi}_2}{\sqrt{(\boldsymbol{\pi}_1^\mathsf{T}Q_\infty^*\boldsymbol{\pi}_1)(\boldsymbol{\pi}_2^\mathsf{T}Q_\infty^*\boldsymbol{\pi}_2)}}$$

（公式依 MVG Result 3.12 補上；逐字稿只說「由這個式子給出」。）

**證明**：

1. 兩平面寫成 $\boldsymbol{\pi}_1=(\mathbf{n}_1^\mathsf{T},d_1)^\mathsf{T}$、$\boldsymbol{\pi}_2=(\mathbf{n}_2^\mathsf{T},d_2)^\mathsf{T}$（法向量 + 距離）。
2. 歐氏座標下兩平面夾角就是法向量夾角：$\cos\theta=\dfrac{\mathbf{n}_1^\mathsf{T}\mathbf{n}_2}{\sqrt{(\mathbf{n}_1^\mathsf{T}\mathbf{n}_1)(\mathbf{n}_2^\mathsf{T}\mathbf{n}_2)}}$。
3. 代入標準形式的 $Q_\infty^*$：$\boldsymbol{\pi}_1^\mathsf{T}Q_\infty^*\boldsymbol{\pi}_2=\mathbf{n}_1^\mathsf{T}\mathbf{n}_2$——$d_1,d_2$ 被 $Q_\infty^*$ 補的 0 消掉。兩式相同。∎

- 平面和 $Q_\infty^*$ 一起做射影變換，角度不變——講者留作練習：把 $H$ 代進去，會互相消掉（和第 06 集 $C_\infty^*$ 量角度的證明一樣）。

---

## 4. Lecture 3 總結

[▶ 33:18](https://youtu.be/k63Bi74Meyc?t=1998)

1. 用 $\mathbf{l}_\infty$ 和 circular points 去除影像的射影和仿射失真（第 05–06 集）。
2. 無窮遠平面，以及它在仿射變換下的不變性。
3. 絕對二次曲線、絕對對偶二次曲面，以及它們在相似變換下的不變性。
4. 用 $\Omega_\infty$、$Q_\infty^*$、$\boldsymbol{\pi}_\infty$ 在 3D 中去除仿射、射影模糊，留到相機校正（講者說 Lecture 5）和 fundamental matrix（講者說 Lecture 6）再講。

---

## 5. 一頁速查表

### 2D ↔ 3D 對照

| | 2D | 3D |
|---|---|---|
| 仿射下不動 | $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$ | $\boldsymbol{\pi}_\infty=(0,0,0,1)^\mathsf{T}$ |
| 相似下不動（點） | $\mathbf{I},\mathbf{J}=(1,\pm i,0)^\mathsf{T}$ | $\Omega_\infty$：$X_1^2+X_2^2+X_3^2=0,\ X_4=0$（$C=I$） |
| 相似下不動（對偶） | $C_\infty^*=\operatorname{diag}(1,1,0)$，rank 2，4 dof | $Q_\infty^*=\operatorname{diag}(1,1,1,0)$，rank 3，8 dof |
| 零向量 | $C_\infty^*\mathbf{l}_\infty=\mathbf{0}$ | $Q_\infty^*\boldsymbol{\pi}_\infty=\mathbf{0}$ |
| 量角度 | 兩線 $\dfrac{\mathbf{l}^\mathsf{T}C_\infty^*\mathbf{m}}{\sqrt{\cdots}}$ | 兩線方向 $\dfrac{\mathbf{d}_1^\mathsf{T}\Omega_\infty\mathbf{d}_2}{\sqrt{\cdots}}$；兩平面 $\dfrac{\boldsymbol{\pi}_1^\mathsf{T}Q_\infty^*\boldsymbol{\pi}_2}{\sqrt{\cdots}}$ |

### 證明的關鍵一步

| 結果 | 關鍵一步 |
|---|---|
| $\boldsymbol{\pi}_\infty$ 不動 ⟺ 仿射 | $H_A^{-\mathsf{T}}$ 最後一行是 $(\mathbf{0},1)^\mathsf{T}$ |
| 不動平面 = $H^\mathsf{T}$ 的特徵向量 | $H^{-\mathsf{T}}\mathbf{V}=\lambda\mathbf{V}$ |
| $\Omega_\infty$ 不動 ⟺ 相似 | 先要保持 $\boldsymbol{\pi}_\infty$（→ 仿射），再 $A^{-\mathsf{T}}IA^{-1}=I$ → $AA^\mathsf{T}=I$ |
| $Q_\infty^*$ 不動 ⟺ 相似 | $HQ_\infty^*H^\mathsf{T}=\begin{pmatrix}AA^\mathsf{T}&A\mathbf{v}\\\mathbf{v}^\mathsf{T}A^\mathsf{T}&\mathbf{v}^\mathsf{T}\mathbf{v}\end{pmatrix}$ → $AA^\mathsf{T}=I$、$\mathbf{v}=\mathbf{0}$ |
| $Q^{*\prime}\boldsymbol{\pi}'=\mathbf{0}$ 對任何 $H$ | $H^\mathsf{T}H^{-\mathsf{T}}=I$ |
| 兩平面夾角 | $Q_\infty^*$ 的 0 消掉距離 $d$，只剩法向量內積 |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 絕對二次曲線的像 $\omega$ | 第 10–12 集（Lecture 5：相機校正、$\omega=(KK^\mathsf{T})^{-1}$）；第 13–15 集（單視角量測） |
| $\boldsymbol{\pi}_\infty$ 去除射影模糊 | 第 16–19 集（fundamental matrix、射影重建）；第 27–30 集（SfM：射影 → 仿射 → 度量重建） |
| $Q_\infty^*$ | Lecture 13 自校正（auto-calibration，本播放清單沒有）；第 27–30 集 |
| 不動平面 = 特徵向量 | 第 13–15 集（消失點、消失線） |
| 圓交 $\Omega_\infty$ 於 circular points | 第 10–12 集（Zhang 校正法：平面上的 circular points 投影到 $\omega$ 上） |

---

## 附：本集一句話總結

> **3D 版的「無窮遠」：$\boldsymbol{\pi}_\infty=(0,0,0,1)^\mathsf{T}$ 只在仿射變換下不動，落在它上面的虛二次曲線 $\Omega_\infty$（矩陣 $I$）和它的對偶 $Q_\infty^*=\operatorname{diag}(1,1,1,0)$ 只在相似變換下不動；把它們夾進內積就能在任何射影座標系下量線和平面的夾角，之後會用來做相機校正和把射影重建升級成度量重建。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 3 (Part 3) 錄影逐字稿（Whisper `medium.en`，34:12）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §3.5–3.7 整理。*
