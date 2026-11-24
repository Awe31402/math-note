---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 35
lecture: Lecture 12 (Part 1) – Generalized cameras
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/PUgr2VKlNbc
notes: MVG 沒有廣義相機；講者說內容取自 Pless「Using Many Cameras as One」、Hongdong Li 的廣義相機線性運動估計論文，以及講者自己 2015、2016 年的論文（BRIEF 未列，未查）。Plücker 線見第 3–4 集
---

# 第 35 集 · Lecture 12 (Part 1)：廣義相機、Plücker 光線、廣義極線幾何、17 點法、三角化 [▶ 影片](https://youtu.be/PUgr2VKlNbc)

← 上一集：[34-stereo-part4](34-stereo-part4.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[36-generalized-cameras-part2](36-generalized-cameras-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 35 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（55:11，Whisper `medium.en` 轉錄）
> **標記說明**：
> - `【口頭】` 講者口頭補充、投影片沒有
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 什麼是廣義相機](#1-什麼是廣義相機)
- [2. 為什麼用多相機系統](#2-為什麼用多相機系統)
- [3. 用 Plücker 線表示像素](#3-用-plücker-線表示像素)
  - [3.1 Plücker 向量回顧](#31-plücker-向量回顧)
  - [3.2 相機光心在參考原點](#32-相機光心在參考原點)
  - [3.3 相機光心不在原點](#33-相機光心不在原點)
- [4. 廣義極線幾何](#4-廣義極線幾何)
  - [4.1 把第一條光線轉到第二個座標系](#41-把第一條光線轉到第二個座標系)
  - [4.2 兩條光線相交的條件](#42-兩條光線相交的條件)
  - [4.3 廣義本質矩陣](#43-廣義本質矩陣)
- [5. 線性 17 點法](#5-線性-17-點法)
- [6. 三角化](#6-三角化)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/PUgr2VKlNbc?t=0)

Lecture 12 的目標：

| 目標 | 集數 |
|---|---|
| 用 Plücker 線推導**廣義極線幾何** | 本集 |
| 用**線性 17 點法**求兩個廣義相機視角的相對位姿 | 本集 |
| 廣義極線幾何的**退化情況**：局部中心投影、軸向相機、兩者合併 | 第 36 集 |
| 用 2D–3D 點或線對應求廣義相機的**絕對位姿** | 第 36–37 集 |

【口頭】[▶ 01:05](https://youtu.be/PUgr2VKlNbc?t=65) 這次講者不說「材料都不是我發明的」——其中兩部分是他自己的論文。四個參考：

1. Robert Pless「Using Many Cameras as One」：廣義極線幾何的推導。
2. Hongdong Li 等「A Linear Approach to Motion Estimation Using Generalized Camera Models」：三種退化情況。
3. 講者 2015 年的論文「Minimal Solutions for the Multi-Camera Pose Estimation Problem」：點對應的廣義位姿估計。
4. 講者 2016 年 ECCV 的論文：用線對應的非透視位姿估計。

⚠️ 逐字稿缺字：Whisper 把 Plücker 寫成 “Blucher”、“Plucker”、“pluker”、“proctor”、“looker”、“pluco”、“puckel”；把 Pless 寫成 “Plasse”；把 orthogonal 寫成 “octagonal”；把 omnidirectional 寫成 “only directional”。

---

## 1. 什麼是廣義相機

[▶ 02:13](https://youtu.be/PUgr2VKlNbc?t=133)

| | 針孔相機 | **廣義相機（generalized camera）** |
|---|---|---|
| 光線 | 全部交於**一個投影中心**（光心） | **不交於同一點**，位置任意 |
| 比喻 | — | 鏡頭是任意形狀，例如哈哈鏡 |

- 哈哈鏡鏡頭實際上不存在。
- 但可以用**多相機系統**實現：幾台相機**剛性**固定在一起，視野重疊很少或完全不重疊。
  - 例：講者做過的無人機，四台相機朝四個方向。
  - 例：自駕車，前、後各一台，兩側後照鏡各一台。
- 每台相機自己的光線交於自己的光心，但不同相機的光心**不是同一點** → 整體來看光線不交於一點 → 就是廣義相機。

---

## 2. 為什麼用多相機系統

[▶ 05:45](https://youtu.be/PUgr2VKlNbc?t=345)

**優點**：

1. **便宜、好維護**：
   - 光達（LiDAR，雷射感測器）有很多旋轉零件，機械越複雜越難維護、越容易故障。相機沒有活動零件。
   - 【口頭】自駕車上的光達一台約 6 萬美元；高階工業相機最多大約一千美元。
2. **自由選擇配置、擴大視野**：四台相機朝四個方向 → **360° 全景（omnidirectional）**。
3. **可以直接從極線幾何得到絕對尺度**（本集會推導）。

**絕對尺度** [▶ 07:49](https://youtu.be/PUgr2VKlNbc?t=469)：

| | 單一針孔相機（第 18 集） | 廣義相機 |
|---|---|---|
| 矩陣 | 本質矩陣 $E$ | **廣義本質矩陣（generalized essential matrix，GEM）** |
| 分解 | $R$、$\mathbf{t}$，$\mathbf{t}$ **只到尺度** | $R$、$\mathbf{t}$，$\mathbf{t}$ **有絕對（公制）尺度** |
| 自由度 | 5 | **6** |

**挑戰** [▶ 09:20](https://youtu.be/PUgr2VKlNbc?t=560)：

1. 相機之間視野**沒有或很少重疊** → 不能直接用 stereo。
2. 每台相機**各自**算本質矩陣、再想辦法合併？
   - 計算沒效率。
   - **得不到絕對尺度**：各自處理就沒用到相機之間已知的相對位置（外參），而這正是取得絕對尺度的關鍵。

**解法**：**廣義相機模型**，特別是**廣義極線幾何**。

---

## 3. 用 Plücker 線表示像素

[▶ 11:32](https://youtu.be/PUgr2VKlNbc?t=692)

- 針孔相機：所有光線交於光心 → 把參考座標系放在光心，每個像素就能用齊次座標 $(x,y,1)^\mathsf{T}$ 表示，彼此一致。
- 廣義相機：沒有共同的光心 → 不能方便地用一個座標系把像素寫成齊次點。
- 改法：在廣義相機上**任意**選一個參考座標系，把每個像素表示成一條**光線**，用 **Plücker 向量**寫。

### 3.1 Plücker 向量回顧

[▶ 14:06](https://youtu.be/PUgr2VKlNbc?t=846)

（第 3–4 集講過。）一條線寫成 6 維向量：

$$
\mathbf{L}=\begin{pmatrix}\mathbf{q}\\\mathbf{q}'\end{pmatrix},\qquad\mathbf{q}'=\mathbf{p}\times\mathbf{q}
$$

- $\mathbf{q}$：**方向**向量（相對參考座標系）。
- $\mathbf{q}'$：**矩（moment）**向量；$\mathbf{p}$ 是線上**任一點**。
- $\mathbf{q}'$ 由 $\mathbf{q}$ 的外積得到 → $\mathbf{q}\cdot\mathbf{q}'=0$。
- 剩下 5 個參數是**齊次**的：整體縮放不改變這條線。所以方便地把 $\mathbf{q}$ 取成**單位向量**，同時固定了尺度。

（矩的外積順序：逐字稿前後說法不一，有時說「$\mathbf{p}$ 和 $\mathbf{q}$ 的外積」，有時說「$\mathbf{q}$ 和 $\mathbf{p}$ 的外積」。本筆記統一用 $\mathbf{q}'=\mathbf{p}\times\mathbf{q}$，這樣下面「線上的點」公式才對得上。）

**線上的點** [▶ 17:46](https://youtu.be/PUgr2VKlNbc?t=1066)：

$$
\mathbf{X}(\alpha)=\left(\mathbf{q}\times\mathbf{q}'\right)+\alpha\,\mathbf{q}
$$

- $\mathbf{q}\times\mathbf{q}'$：線上**離參考原點最近**的點（基點）。
- $\alpha$：從基點沿 $\mathbf{q}$ 的**有號距離**——正的往 $\mathbf{q}$ 方向，負的往反方向。

> 以下**不是逐字稿內容**，是驗證 $\mathbf{q}\times\mathbf{q}'$ 是最近點：$\|\mathbf{q}\|=1$ 時，
> $$
> \mathbf{q}\times\left(\mathbf{p}\times\mathbf{q}\right)=\mathbf{p}\left(\mathbf{q}\cdot\mathbf{q}\right)-\mathbf{q}\left(\mathbf{q}\cdot\mathbf{p}\right)=\mathbf{p}-\left(\mathbf{q}\cdot\mathbf{p}\right)\mathbf{q}
> $$
> 這是把 $\mathbf{p}$ 減掉它沿 $\mathbf{q}$ 的分量——剩下的部分垂直於線，正是原點到線的垂足。

### 3.2 相機光心在參考原點

[▶ 19:41](https://youtu.be/PUgr2VKlNbc?t=1181)

- 參考座標系可以放在剛體上的任何地方。若放在某台相機 $C_i$ 的光心：
- 像素 $(x,y)$ 的方向 = **正規化相機座標**：
$$
\mathbf{q}\propto K_{C_i}^{-1}\begin{pmatrix}x\\y\\1\end{pmatrix}\quad(\text{再正規化成單位向量})
$$
- 所有光線都過原點 → 取 $\mathbf{p}=\mathbf{0}$ → $\mathbf{q}'=\mathbf{0}$。

### 3.3 相機光心不在原點

[▶ 22:40](https://youtu.be/PUgr2VKlNbc?t=1360)

- 參考座標系只能和**一台**相機的光心重合；其他相機的光線矩向量都不是 0。
- **假設**：
  - 每台相機都校準過（內參 $K_{C_i}$）。
  - 已知多相機系統的**外參** $R_{C_i}$、$\mathbf{t}_{C_i}$：把相機 $C_i$ 帶到參考座標系的相對轉換（用前面的校準方法求得）。

**方向** [▶ 24:54](https://youtu.be/PUgr2VKlNbc?t=1494)：

- $\tilde{\mathbf{q}}\propto K_{C_i}^{-1}(x,y,1)^\mathsf{T}$ 是相對**這台相機自己**的方向。
- 方向向量只需要**旋轉**到參考座標系：
$$
\mathbf{q}=R_{C_i}\tilde{\mathbf{q}}=R_{C_i}K_{C_i}^{-1}\begin{pmatrix}x\\y\\1\end{pmatrix}\quad(\text{正規化})
$$

**矩** [▶ 26:40](https://youtu.be/PUgr2VKlNbc?t=1600)：

- 線上方便的點：這台相機的**光心**，在參考座標系中就是 $\mathbf{t}_{C_i}$。
$$
\mathbf{q}'=\mathbf{t}_{C_i}\times\mathbf{q}
$$

⚠️ 逐字稿缺字 [▶ 26:14](https://youtu.be/PUgr2VKlNbc?t=1574)：Whisper 寫「pre-multiply with the rotation of the camera intrinsics」，依上下文是**外參**的旋轉 $R_{C_i}$。

**自駕車例子** [▶ 28:01](https://youtu.be/PUgr2VKlNbc?t=1681)【口頭】：

- 車上還有很多其他感測器，例如**慣性量測單元（IMU）**，量加速度和角度變化。
- IMU 取樣率最高（約 200 Hz），通常放在車子中間，適合當整套感測器的參考座標系 $V$。
- 所有相機的外參都相對 $V$。

---

## 4. 廣義極線幾何

[▶ 30:23](https://youtu.be/PUgr2VKlNbc?t=1823)

**設定**：

- 兩個廣義影像（視角 1、2），對應像素 $(x_1,y_1)$、$(x_2,y_2)$，都是同一個 3D 點 $\mathbf{X}$ 的像。
- 兩條光線：$\mathbf{L}_1=(\mathbf{q}_1;\mathbf{q}_1')$（相對視角 1 的參考座標系）、$\mathbf{L}_2=(\mathbf{q}_2;\mathbf{q}_2')$（相對視角 2）。
  - 同一套廣義相機移動時，外參在兩個視角都一樣；但這不是必要條件，只要知道參考座標系在哪就好。
- 兩條光線**一定相交**於 $\mathbf{X}$。
- 兩個參考座標系之間有相對轉換 $R$、$\mathbf{t}$。

**注意** [▶ 33:36](https://youtu.be/PUgr2VKlNbc?t=2016)：

| 符號 | 意思 |
|---|---|
| $R_{C_i}$、$\mathbf{t}_{C_i}$ | **外參**：每台相機相對廣義相機參考座標系 |
| $R$、$\mathbf{t}$ | **兩個視角**的參考座標系之間（要求的未知數） |

### 4.1 把第一條光線轉到第二個座標系

[▶ 34:29](https://youtu.be/PUgr2VKlNbc?t=2069)

兩條線要用**同一個**座標系表示。把 $\mathbf{L}_1$ 轉到視角 2：

$$
\tilde{\mathbf{L}}_1=\begin{pmatrix}R&\mathbf{0}\\\left[\mathbf{t}\right]_\times R&R\end{pmatrix}\mathbf{L}_1
$$

- $6\times6$ 矩陣：點的剛體轉換是 $4\times4$，Plücker 線是 $6\times6$。
- $\tilde{\mathbf{L}}_1$ 在 3D 世界裡還是同一條線，只是改用視角 2 的座標表示。

（逐字稿只說「這個 $6\times6$ 矩陣」，沒唸出各塊；上式依 $\mathbf{q}'=\mathbf{p}\times\mathbf{q}$ 補上。）

> 以下**不是逐字稿內容**，是 $6\times6$ 矩陣的推導：點的轉換 $\tilde{\mathbf{p}}=R\mathbf{p}+\mathbf{t}$，方向只旋轉 $\tilde{\mathbf{q}}=R\mathbf{q}$。於是
> $$
> \tilde{\mathbf{q}}'=\tilde{\mathbf{p}}\times\tilde{\mathbf{q}}=\left(R\mathbf{p}\right)\times\left(R\mathbf{q}\right)+\mathbf{t}\times R\mathbf{q}=R\left(\mathbf{p}\times\mathbf{q}\right)+\left[\mathbf{t}\right]_\times R\mathbf{q}=R\mathbf{q}'+\left[\mathbf{t}\right]_\times R\mathbf{q}
> $$
> 用到「旋轉保持外積」：$(R\mathbf{a})\times(R\mathbf{b})=R(\mathbf{a}\times\mathbf{b})$。

### 4.2 兩條光線相交的條件

[▶ 37:02](https://youtu.be/PUgr2VKlNbc?t=2222)

兩條 Plücker 線 $(\mathbf{q}_a;\mathbf{q}_a')$、$(\mathbf{q}_b;\mathbf{q}_b')$（同一座標系）**相交（或平行）**若且唯若

$$
\mathbf{q}_b\cdot\mathbf{q}_a'+\mathbf{q}_b'\cdot\mathbf{q}_a=0
$$

> 以下**不是逐字稿內容**，是這個條件的來源：取線 $a$ 上一點 $\mathbf{p}_a$、線 $b$ 上一點 $\mathbf{p}_b$。兩線共面（相交或平行）⟺ $(\mathbf{p}_a-\mathbf{p}_b)\cdot(\mathbf{q}_a\times\mathbf{q}_b)=0$。展開：
> $$
> \mathbf{p}_a\cdot\left(\mathbf{q}_a\times\mathbf{q}_b\right)-\mathbf{p}_b\cdot\left(\mathbf{q}_a\times\mathbf{q}_b\right)=\mathbf{q}_b\cdot\left(\mathbf{p}_a\times\mathbf{q}_a\right)+\mathbf{q}_a\cdot\left(\mathbf{p}_b\times\mathbf{q}_b\right)=\mathbf{q}_b\cdot\mathbf{q}_a'+\mathbf{q}_a\cdot\mathbf{q}_b'
> $$
> （用純量三重積的輪換：$\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})=\mathbf{c}\cdot(\mathbf{a}\times\mathbf{b})$。）

### 4.3 廣義本質矩陣

[▶ 37:51](https://youtu.be/PUgr2VKlNbc?t=2271)

代入：$b$ = 第二條光線，$\mathbf{q}_b=\mathbf{q}_2$、$\mathbf{q}_b'=\mathbf{q}_2'$；$a$ = 轉過來的第一條光線，$\mathbf{q}_a=R\mathbf{q}_1$、$\mathbf{q}_a'=R\mathbf{q}_1'+[\mathbf{t}]_\times R\mathbf{q}_1$：

$$
\mathbf{q}_2^\mathsf{T}\left(R\mathbf{q}_1'+\left[\mathbf{t}\right]_\times R\mathbf{q}_1\right)+\mathbf{q}_2'^\mathsf{T}R\mathbf{q}_1=0
$$

$$
\Longrightarrow\quad\mathbf{q}_2^\mathsf{T}E\mathbf{q}_1+\mathbf{q}_2^\mathsf{T}R\mathbf{q}_1'+\mathbf{q}_2'^\mathsf{T}R\mathbf{q}_1=0,\qquad E=\left[\mathbf{t}\right]_\times R
$$

**矩陣形式** [▶ 39:10](https://youtu.be/PUgr2VKlNbc?t=2350)：

$$
\boxed{\ \mathbf{L}_2^\mathsf{T}\begin{pmatrix}E&R\\R&\mathbf{0}\end{pmatrix}\mathbf{L}_1=0\ }
$$

- $E=[\mathbf{t}]_\times R$：就是一般針孔相機的**本質矩陣**（第 18 集）。
- 和 $\mathbf{x}'^\mathsf{T}E\mathbf{x}=0$ 形式一樣 → 叫**廣義極線約束（generalized epipolar constraint）**。

| | 針孔 | 廣義 |
|---|---|---|
| 對應 | $3\times1$ 像點 $\mathbf{x}$、$\mathbf{x}'$ | $6\times1$ Plücker 光線 $\mathbf{L}_1$、$\mathbf{L}_2$ |
| 矩陣 | $3\times3$ 本質矩陣 | $6\times6$ **廣義本質矩陣** |

> 以下**不是逐字稿內容**，是驗算：若兩個視角都是同一台針孔相機、參考座標放在光心，則 $\mathbf{q}_1'=\mathbf{q}_2'=\mathbf{0}$，約束退化成 $\mathbf{q}_2^\mathsf{T}E\mathbf{q}_1=0$——正是第 18 集的極線約束。

---

## 5. 線性 17 點法

[▶ 41:56](https://youtu.be/PUgr2VKlNbc?t=2516)

**未知數**：$E$ 有 9 個元素、$R$ 有 9 個元素 → **18 個**。

**線性化** [▶ 42:47](https://youtu.be/PUgr2VKlNbc?t=2567)：$\mathbf{L}_2^\mathsf{T}G\mathbf{L}_1=0$ 展開後對這 18 個元素是**線性**的：

$$
\mathbf{a}^\mathsf{T}\mathbf{g}=0
$$

- $\mathbf{g}\in\mathbb{R}^{18}$：$E$ 和 $R$ 的元素（未知）。
- $\mathbf{a}\in\mathbb{R}^{18}$：由已知的 $\mathbf{L}_1$、$\mathbf{L}_2$ 的元素組成。

**疊起來** [▶ 44:29](https://youtu.be/PUgr2VKlNbc?t=2669)：每組對應給一條方程式，$n$ 組疊成

$$
A\mathbf{g}=\mathbf{0},\qquad A\in\mathbb{R}^{n\times18}
$$

- 齊次線性方程式，18 個未知數差一個尺度 → 至少要 **17 組對應**。
- 用 SVD：$A=U\Sigma V^\mathsf{T}$，解是**最小奇異值對應的右奇異向量** $\mathbf{v}$ → 一族解 $\mathbf{g}=\lambda\mathbf{v}$。

**決定尺度 $\lambda$** [▶ 46:11](https://youtu.be/PUgr2VKlNbc?t=2771)：

- $F$、$E$、$H$ 都只能到尺度。但這裡**可以唯一決定** $\lambda$：
- $\mathbf{g}$ 的後 9 個元素是 $R$ → 它必須是正交矩陣、**行列式為 1**。
- 把 $\lambda v_{10},\dots,\lambda v_{18}$ 排成 $3\times3$ 的 $R(\lambda)$，令
$$
\det R(\lambda)=1
$$
  一個方程式、一個未知數 → 解出 $\lambda$。

> 以下**不是逐字稿內容**，是補充：$\det(\lambda V_R)=\lambda^3\det V_R$（$V_R$ 是 $\mathbf{v}$ 後 9 個元素排成的矩陣），所以 $\lambda=\left(\det V_R\right)^{-1/3}$，實數解唯一。

**得到 $\mathbf{t}$**：有了唯一的 $E$、$R$，照第 18 集分解 $E=[\mathbf{t}]_\times R$ 得 $\mathbf{t}$。

**為什麼有絕對尺度** [▶ 49:14](https://youtu.be/PUgr2VKlNbc?t=2954)：

- 光線 $\mathbf{L}_1$、$\mathbf{L}_2$ 是用已知外參算的，**$\mathbf{t}_{C_i}$ 有公制尺度**。
- 所以係數 $\mathbf{a}$ 已經帶著絕對尺度資訊；再加上 $\det R=1$ 的約束 → 尺度資訊傳到兩個視角的相對轉換 → $\mathbf{t}$ 沒有尺度模糊。

---

## 6. 三角化

[▶ 50:49](https://youtu.be/PUgr2VKlNbc?t=3049)

- 廣義相機不能用第 19 集的線性三角化。
- 改用 Plücker 線上的點公式。在視角 2 的座標系中，兩條光線上的點：
  - 光線 2：$\left(\mathbf{q}_2\times\mathbf{q}_2'\right)+\alpha_2\mathbf{q}_2$
  - 光線 1（先轉到視角 2）：$R\left(\mathbf{q}_1\times\mathbf{q}_1'\right)+\mathbf{t}+\alpha_1R\mathbf{q}_1$
- 兩條光線交於同一點 → 令兩者相等：
$$
R\left(\mathbf{q}_1\times\mathbf{q}_1'\right)+\mathbf{t}+\alpha_1R\mathbf{q}_1=\left(\mathbf{q}_2\times\mathbf{q}_2'\right)+\alpha_2\mathbf{q}_2
$$
- 只有 $\alpha_1$、$\alpha_2$ 兩個未知數，3 條方程式 → **超定的非齊次線性方程式**：
$$
\begin{pmatrix}R\mathbf{q}_1&-\mathbf{q}_2\end{pmatrix}\begin{pmatrix}\alpha_1\\\alpha_2\end{pmatrix}=\left(\mathbf{q}_2\times\mathbf{q}_2'\right)-R\left(\mathbf{q}_1\times\mathbf{q}_1'\right)-\mathbf{t}
$$
  用最小平方解，沒有模糊。
- 代回任一條線的式子得 3D 點：選視角 1 當重建座標系就用 $\left(\mathbf{q}_1\times\mathbf{q}_1'\right)+\alpha_1\mathbf{q}_1$；選視角 2 就用 $\left(\mathbf{q}_2\times\mathbf{q}_2'\right)+\alpha_2\mathbf{q}_2$。

⚠️ 逐字稿缺字 [▶ 52:58](https://youtu.be/PUgr2VKlNbc?t=3178)：講者說「方向向量要乘上旋轉**和平移**轉到第二個視角」。方向向量只需旋轉；平移 $\mathbf{t}$ 加在**基點**上。上面的式子依這個修正寫出。

（本集到 55:02 結束。）

---

## 7. 一頁速查表

| 項目 | 公式 | 關鍵一步 |
|---|---|---|
| Plücker 線 | $\mathbf{L}=(\mathbf{q};\mathbf{q}')$，$\mathbf{q}'=\mathbf{p}\times\mathbf{q}$，$\|\mathbf{q}\|=1$ | $\mathbf{q}\cdot\mathbf{q}'=0$ |
| 線上的點 | $(\mathbf{q}\times\mathbf{q}')+\alpha\mathbf{q}$ | $\mathbf{q}\times\mathbf{q}'$ = 最近點 |
| 像素 → 光線 | $\mathbf{q}=R_{C_i}K_{C_i}^{-1}(x,y,1)^\mathsf{T}$（正規化），$\mathbf{q}'=\mathbf{t}_{C_i}\times\mathbf{q}$ | 方向只旋轉；光心當線上的點 |
| 線的轉換 | $\begin{pmatrix}R&0\\[\mathbf{t}]_\times R&R\end{pmatrix}$ | $(R\mathbf{a})\times(R\mathbf{b})=R(\mathbf{a}\times\mathbf{b})$ |
| 相交條件 | $\mathbf{q}_b\cdot\mathbf{q}_a'+\mathbf{q}_b'\cdot\mathbf{q}_a=0$ | 共面 ⟺ 純量三重積為 0 |
| 廣義極線約束 | $\mathbf{L}_2^\mathsf{T}\begin{pmatrix}E&R\\R&0\end{pmatrix}\mathbf{L}_1=0$，$E=[\mathbf{t}]_\times R$ | 代入相交條件 |
| 17 點法 | $A\mathbf{g}=0$，$\mathbf{g}\in\mathbb{R}^{18}$，SVD → $\lambda\mathbf{v}$，$\det R(\lambda)=1$ | 18 未知數 − 1 尺度 = 17 |
| 絕對尺度 | $\mathbf{t}$ 公制 | 外參 $\mathbf{t}_{C_i}$ 有公制尺度 |
| 三角化 | $(R\mathbf{q}_1\ \ -\mathbf{q}_2)(\alpha_1,\alpha_2)^\mathsf{T}=\cdots$ | 兩條線上的點相等 |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 17 點法 | 第 36 集（哪些相機配置會讓 $A$ 的秩不足：局部中心、軸向） |
| Plücker 光線 | 第 36–37 集（廣義相機的絕對位姿：點對應、線對應） |
| 廣義相機的 SfM | 第 36 集 |

---

## 附：本集一句話總結

> **多相機系統的光線不交於一點，就是廣義相機；把每個像素寫成 Plücker 光線 $(\mathbf{q};\mathbf{t}_{C_i}\times\mathbf{q})$，兩個視角的對應光線必須相交，代入相交條件就得到廣義極線約束 $\mathbf{L}_2^\mathsf{T}\begin{pmatrix}E&R\\R&0\end{pmatrix}\mathbf{L}_1=0$；它對 $E$、$R$ 的 18 個元素是線性的，17 組對應用 SVD 解到一個尺度，再由 $\det R=1$ 定出尺度——因為外參帶公制尺度，平移 $\mathbf{t}$ 也有絕對尺度；三角化則是讓兩條光線上的點相等、解 $\alpha_1,\alpha_2$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 12 (Part 1) 錄影逐字稿（Whisper `medium.en`，55:11）整理；MVG 無對應章節。*
