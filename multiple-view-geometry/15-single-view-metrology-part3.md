---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 15
lecture: Lecture 6 (Part 3) – Single view metrology
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/9TuPY67JBpo
notes: MVG §8.5 Example 8.18、§2.8.1（極點／極線）、§8.6–8.8（書頁 210–231，PDF 頁 228–249）
---

# 第 15 集 · Lecture 6 (Part 3)：三正方形校正、極點與極線、消失點與消失線、單張影像量高度、從 ω 求 K [▶ 影片](https://youtu.be/9TuPY67JBpo)

← 上一集：[14-single-view-metrology-part2](14-single-view-metrology-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[16-fundamental-essential-part1](16-fundamental-essential-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 15 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（1:00:41，Whisper `medium.en` 轉錄）＋ MVG §8.5、§2.8.1、§8.6–8.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 三個正方形的校正](#1-三個正方形的校正)
- [2. 極點、極線、共軛點](#2-極點極線共軛點)
- [3. 消失點](#3-消失點)
  - [3.1 定義與性質](#31-定義與性質)
  - [3.2 v = Kd](#32-v--kd)
  - [3.3 應用：從消失點求相機旋轉](#33-應用從消失點求相機旋轉)
  - [3.4 應用：兩條場景線的夾角](#34-應用兩條場景線的夾角)
  - [3.5 求消失點是雞生蛋問題](#35-求消失點是雞生蛋問題)
- [4. 消失線](#4-消失線)
  - [4.1 定義與性質](#41-定義與性質)
  - [4.2 已知 K 時消失線的三個用途](#42-已知-k-時消失線的三個用途)
- [5. 垂直關係：消失點和消失線之間](#5-垂直關係消失點和消失線之間)
- [6. 單張影像量測垂直線段的長度比](#6-單張影像量測垂直線段的長度比)
- [7. 從單張影像求 K](#7-從單張影像求-k)
- [8. Lecture 6 總結](#8-lecture-6-總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 三個正方形校正 $K$ | §8.5 Example 8.18 |
| 極點、極線、共軛（$\omega$ 的性質） | §2.8.1 |
| 消失點、消失線的定義和用途 | §8.6 |
| 單張影像的仿射量測（量高度） | §8.7 |
| 用消失點、消失線、內部約束求 $K$ | §8.8 |

---

## 1. 三個正方形的校正

[▶ 00:00](https://youtu.be/9TuPY67JBpo?t=0)

（接上一集的校正裝置。）

**步驟**：

1. 在每個正方形上設座標：四角是 $(0,0)$、$(1,0)$、$(0,1)$、$(1,1)$。
   - **尺度不重要**：要求的是 homography，然後用它投影 circular points；circular points 在相似變換下不動（第 05 集），所以絕對尺度無所謂。
2. 找出四角在影像上的位置，4 對對應點用線性方法求 $H=[\mathbf{h}_1\ \mathbf{h}_2\ \mathbf{h}_3]$。
3. 把正方形平面的 circular points $(1,\pm i,0)^\mathsf{T}$ 用 $H$ 投影 [▶ 01:54](https://youtu.be/9TuPY67JBpo?t=114)：
$$
H\begin{pmatrix}1\\\pm i\\0\end{pmatrix}=\mathbf{h}_1\pm i\,\mathbf{h}_2
$$
   這是 circular points 的像。
4. circular points 在 $\Omega_\infty$ 上 → 它們的像在 $\omega$ 上（雖然看不到）：
$$
(\mathbf{h}_1\pm i\mathbf{h}_2)^\mathsf{T}\omega(\mathbf{h}_1\pm i\mathbf{h}_2)=0
$$
5. 拆成實部和虛部，得兩條**對 $\omega$ 線性**的約束 [▶ 03:17](https://youtu.be/9TuPY67JBpo?t=197)：
$$
\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_2=0,\qquad \mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_1=\mathbf{h}_2^\mathsf{T}\omega\mathbf{h}_2
$$
6. $\omega$ 是對稱矩陣，6 個元素、差縮放 → 5 個自由度 → 需要 5 條以上。三個正方形（三個 homography）給 6 條 [▶ 04:20](https://youtu.be/9TuPY67JBpo?t=260)。正方形可以任意擺，**只要不在平行平面上**。
7. 疊成 $A\mathbf{w}=\mathbf{0}$ 解出 $\omega$，排回 $3\times3$，**Cholesky 分解**得 $K$。

⚠️ 逐字稿缺字 [▶ 03:26](https://youtu.be/9TuPY67JBpo?t=206)：Whisper 寫「h1 transpose multiplied by h2 equals to 0」，少了中間的 $\omega$。[▶ 03:47](https://youtu.be/9TuPY67JBpo?t=227) 講者說「也可以用 $\mathbf{h}_2^\mathsf{T}\omega\mathbf{h}_2$ 和 $\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_1$ 的外積等於 0」，意思不清楚；依 MVG 式 (8.12)，第二條就是兩者相減等於 0。

（這和第 12 集 Zhang 方法、第 12 集筆記裡的 MVG Example 8.18 是同一件事。）

---

## 2. 極點、極線、共軛點

[▶ 05:26](https://youtu.be/9TuPY67JBpo?t=326)

$\omega$ 是二次曲線，所以也遵守**極點–極線（pole–polar）關係**。

**動機**：兩個像點反投影成**互相垂直的光線**時，滿足 $\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2=0$（第 14 集）——這正是對 $\omega$「共軛」的關係。類似地，一個點和垂直於它的方向之間有 $\mathbf{l}=\omega\mathbf{x}$ 的極線關係。

**極線（polar line）** [▶ 07:41](https://youtu.be/9TuPY67JBpo?t=461)：

- 第 02 集：$\mathbf{x}$ 在 $C$ 上時，$\mathbf{l}=C\mathbf{x}$ 是切線。
- $\mathbf{x}$ **不在** $C$ 上（$\mathbf{x}^\mathsf{T}C\mathbf{x}\neq0$）時，$\mathbf{l}=C\mathbf{x}$ 還是一條線，叫 $\mathbf{x}$ 的**極線**；$\mathbf{x}$ 叫**極點（pole）**。
- **幾何**：從 $\mathbf{x}$ 向 $C$ 畫兩條切線，兩個切點的連線就是極線。
- $\mathbf{x}$ 在 $C$ 上時，極線退化成切線。

**證明** [▶ 09:47](https://youtu.be/9TuPY67JBpo?t=587)：

1. 兩個切點 $\mathbf{z}_1,\mathbf{z}_2$ 在 $C$ 上：$\mathbf{z}_i^\mathsf{T}C\mathbf{z}_i=0$。切線 $\mathbf{l}_1=C\mathbf{z}_1$、$\mathbf{l}_2=C\mathbf{z}_2$。
2. $\mathbf{x}$ 是兩條切線的交點：$\mathbf{x}=\mathbf{l}_1\times\mathbf{l}_2=(C\mathbf{z}_1)\times(C\mathbf{z}_2)$。
3. 恆等式 $(M\mathbf{a})\times(M\mathbf{b})=\det(M)\,M^{-\mathsf{T}}(\mathbf{a}\times\mathbf{b})$：
$$
\mathbf{x}=\det(C)\,C^{-\mathsf{T}}(\mathbf{z}_1\times\mathbf{z}_2)=\det(C)\,C^{-1}\mathbf{l}
$$
   （$C$ 對稱 → $C^{-\mathsf{T}}=C^{-1}$；$\mathbf{l}=\mathbf{z}_1\times\mathbf{z}_2$ 是兩切點的連線。）
4. $\det C$ 是常數 $k$：$\mathbf{x}=kC^{-1}\mathbf{l}$ → $\mathbf{l}=C\mathbf{x}$（差縮放）。∎

（恆等式的名稱是補上的；逐字稿只說「把 $C$ 提出來，外積分解得到 $\det(C)\,C^{-\mathsf{T}}$ 乘 $\mathbf{z}_1\times\mathbf{z}_2$」。）

**共軛點（conjugate points）** [▶ 12:23](https://youtu.be/9TuPY67JBpo?t=743)：

- 若 $\mathbf{y}$ 在 $\mathbf{x}$ 的極線 $\mathbf{l}_x=C\mathbf{x}$ 上：$\mathbf{y}^\mathsf{T}C\mathbf{x}=0$。
- 滿足 $\mathbf{y}^\mathsf{T}C\mathbf{x}=0$ 的兩點，叫對 $C$ **共軛**。
- **對稱**：$\mathbf{x}$ 在 $\mathbf{y}$ 的極線上 ⟺ $\mathbf{y}$ 在 $\mathbf{x}$ 的極線上。理由：$\mathbf{x}^\mathsf{T}C\mathbf{y}=\mathbf{y}^\mathsf{T}C\mathbf{x}$（$C$ 對稱），一個為 0 另一個也為 0。
- 【口頭】講者說投影片上的圖是照比例畫的，可以自己驗證。

**對偶**：兩條線 $\mathbf{l}$、$\mathbf{m}$ 對 $C$ 共軛，若 $\mathbf{l}^\mathsf{T}C^*\mathbf{m}=0$。

**套到 $\omega$ 上**：垂直光線的像點對 $\omega$ 共軛（$\mathbf{x}_1^\mathsf{T}\omega\mathbf{x}_2=0$）。

---

## 3. 消失點

### 3.1 定義與性質

[▶ 14:44](https://youtu.be/9TuPY67JBpo?t=884)

**幾何定義**：一條 3D 線的**消失點（vanishing point）**，是「通過**相機中心**、平行於這條線的光線」和影像平面的交點。

- 線上每一點投影到影像上；其中「往無窮遠走」的那個方向投影到的點，就是消失點 $\mathbf{v}$。
- 相機中心不動、只轉影像平面：同一個方向投影到新影像上的另一個消失點 $\mathbf{v}'$。

⚠️ 逐字稿缺字 [▶ 15:09](https://youtu.be/9TuPY67JBpo?t=909)：講者說「passing through the image center」，依 MVG 應為「camera centre」。[▶ 16:43](https://youtu.be/9TuPY67JBpo?t=1003) 「not the precision of the line」應為 **position**。

**性質**：

- 消失點**只依賴線的方向**，不依賴線的位置。
- 所以**一組平行線有共同的消失點**——拍成照片後，平行線交於一點。
- 兩個消失點連成一條**消失線**。

### 3.2 v = Kd

[▶ 17:52](https://youtu.be/9TuPY67JBpo?t=1072)

**代數（極限）**：

1. 3D 線：$\mathbf{X}(\lambda)=\mathbf{A}+\lambda\mathbf{D}$，$\mathbf{A}$ 是線上一點（齊次 $(\tilde{\mathbf{A}},1)$），$\mathbf{D}=(\mathbf{d}^\mathsf{T},0)^\mathsf{T}$ 是方向。
2. 標準相機 $P=K[I\mid\mathbf{0}]$ 投影：
$$
\mathbf{x}(\lambda)=P\mathbf{A}+\lambda P\mathbf{D}=\mathbf{a}+\lambda K\mathbf{d}
$$
3. $\lambda\to\infty$（沿線走到無窮遠），除以 $\lambda$：$\frac{1}{\lambda}\mathbf{a}+K\mathbf{d}\to K\mathbf{d}$。

$$
\boxed{\ \mathbf{v}=K\mathbf{d}\ }
$$

- 只依賴內參和**方向**，不依賴線上任何點的位置（和幾何定義一致）。

**射影觀點** [▶ 20:37](https://youtu.be/9TuPY67JBpo?t=1237)：消失點 = 平行線族和 $\boldsymbol{\pi}_\infty$ 的交點（理想點 $\mathbf{X}_\infty=(\mathbf{d}^\mathsf{T},0)^\mathsf{T}$）的像：

$$
\mathbf{v}=P\mathbf{X}_\infty=K[I\mid\mathbf{0}]\begin{pmatrix}\mathbf{d}\\0\end{pmatrix}=K\mathbf{d}
$$

【課本補充】MVG Result 8.20：一般相機下，方向 $\mathbf{d}$ 的消失點是 $\mathbf{v}=K\mathbf{d}$——其中 $\mathbf{d}$ 用相機座標表示。

**平行於影像平面的線** [▶ 22:07](https://youtu.be/9TuPY67JBpo?t=1327)：

- 平行於影像平面（$z=0$ 方向）的平行線，在影像上**還是平行**（消失點在無窮遠）。
- **反過來不一定對**：影像上平行的線，在場景中不一定平行。例如**主平面**上的線（第 10 集）：它們的交點投影到影像的無窮遠——兩條不平行的線，在影像上看起來平行。

> 以下**不是逐字稿內容**，是驗證：方向 $\mathbf{d}=(d_x,d_y,0)^\mathsf{T}$ 時 $K\mathbf{d}$ 的第三個分量是 0（$K$ 第三列是 $(0,0,1)$）→ 消失點在影像的無窮遠。

### 3.3 應用：從消失點求相機旋轉

[▶ 23:44](https://youtu.be/9TuPY67JBpo?t=1424)

**設定**：兩個視角 $P=K[I\mid\mathbf{0}]$、$P'=K[R\mid\mathbf{t}]$，$K$ 相同且已知。同一個方向在兩張圖上的消失點 $\mathbf{v}$、$\mathbf{v}'$。

- **不需要是純旋轉**（有平移也可以），但**求不出 $\mathbf{t}$**。

**推導** [▶ 25:12](https://youtu.be/9TuPY67JBpo?t=1512)：

1. 第一張：$\mathbf{v}=K\mathbf{d}$ → $\mathbf{d}=K^{-1}\mathbf{v}$。
2. 第二張：$\mathbf{v}'=K[R\mid\mathbf{t}]\begin{pmatrix}\mathbf{d}\\0\end{pmatrix}=KR\mathbf{d}$。令 $\mathbf{d}'=R\mathbf{d}$，則 $\mathbf{d}'=K^{-1}\mathbf{v}'$。（平移乘上 0，沒作用。）
3. 把 $\mathbf{d}$、$\mathbf{d}'$ **正規化成單位向量**（除以長度）。
4. $\mathbf{d}'=R\mathbf{d}$。

**需要幾個消失點** [▶ 27:29](https://youtu.be/9TuPY67JBpo?t=1649)：

- 每對消失點給 **2 個**獨立約束（齊次 3 維向量只有兩個比值有意義）。
- $R$ 有 **3** 個自由度。
- 所以需要**兩對**對應的消失點（$\mathbf{v}_1\leftrightarrow\mathbf{v}_1'$、$\mathbf{v}_2\leftrightarrow\mathbf{v}_2'$）。

講者後面又說「每對給一個約束、兩對給兩個約束」[▶ 28:23](https://youtu.be/9TuPY67JBpo?t=1703)，和前面「每對給兩個約束」不一致。

> 以下**不是逐字稿內容**，是依自由度推論的：單位方向向量 $\mathbf{d}'=R\mathbf{d}$ 給 2 個約束（單位向量只有 2 個自由度），兩對共 4 個 ≥ 3，足夠且多一個。所以「兩對消失點」的結論沒錯。MVG Example 8.21 也是用兩對消失點。

### 3.4 應用：兩條場景線的夾角

[▶ 28:45](https://youtu.be/9TuPY67JBpo?t=1725)

消失點也是影像上的點。已知 $K$，兩個消失點 $\mathbf{v}_1,\mathbf{v}_2$ 的方向就是兩組場景線的方向，夾角是

$$
\cos\theta=\frac{\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_2}{\sqrt{(\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_1)(\mathbf{v}_2^\mathsf{T}\omega\mathbf{v}_2)}},\qquad \omega=(KK^\mathsf{T})^{-1}
$$

（第 14 集的光線夾角公式。）

### 3.5 求消失點是雞生蛋問題

[▶ 29:56](https://youtu.be/9TuPY67JBpo?t=1796)【口頭】

- 知道消失點 → 很容易判斷哪些線屬於它。
- 知道哪些線屬於同一組平行線 → 很容易求交點得消失點。
- 但兩者**都不知道**，要同時求——**雞生蛋、蛋生雞**。
- 更糟：偵測到的線有雜訊，不會剛好交於一點。
- 講者不細講，只給參考文獻。

---

## 4. 消失線

### 4.1 定義與性質

[▶ 32:41](https://youtu.be/9TuPY67JBpo?t=1961)

- 一組**平行平面**都和 $\boldsymbol{\pi}_\infty$ 交於同一條線 $\mathbf{l}_\infty$。
- 這條線的像叫**消失線（vanishing line）**。
- **幾何**：通過相機中心、平行於場景平面的那個平面，和影像平面的交線。
- **只依賴平面的方向（法向）**，不依賴平面的位置。
- 平行於這個平面的直線，它們的消失點都**落在消失線上**（它們和 $\boldsymbol{\pi}_\infty$ 的交點都在 $\mathbf{l}_\infty$ 上）。

**計算** [▶ 40:31](https://youtu.be/9TuPY67JBpo?t=2431)：比求消失點容易——找兩個消失點，$\mathbf{l}=\mathbf{v}_1\times\mathbf{v}_2$。

### 4.2 已知 K 時消失線的三個用途

[▶ 36:14](https://youtu.be/9TuPY67JBpo?t=2174)

**(a) 平面相對相機的方向** [▶ 36:23](https://youtu.be/9TuPY67JBpo?t=2183)：

- 第 14 集：影像線反投影平面的法向 $\mathbf{n}=K^\mathsf{T}\mathbf{l}$。
- 消失線反投影成「通過相機中心、平行於場景平面」的平面 → 場景平面的法向就是
$$
\mathbf{n}=K^\mathsf{T}\mathbf{l}
$$

**(b) 只用消失線就能做度量校正** [▶ 37:46](https://youtu.be/9TuPY67JBpo?t=2266)：

- 知道法向 $\mathbf{n}=K^\mathsf{T}\mathbf{l}$ 後，找一個 homography（等同於一個純旋轉）把 $\mathbf{n}$ 轉到正對影像（垂直於影像平面）。
- 用它把影像扭轉成**正對（fronto-parallel）**的新影像。

**(c) 兩個場景平面的夾角** [▶ 39:18](https://youtu.be/9TuPY67JBpo?t=2358)：

- $\mathbf{n}_1=K^\mathsf{T}\mathbf{l}_1$、$\mathbf{n}_2=K^\mathsf{T}\mathbf{l}_2$，取內積：
$$
\cos\theta=\frac{\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_2}{\sqrt{(\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_1)(\mathbf{l}_2^\mathsf{T}\omega^*\mathbf{l}_2)}},\qquad\omega^*=KK^\mathsf{T}
$$
- 講者留作練習。

> 以下**不是逐字稿內容**：逐字稿只說「得到這個最終式子」。上式依 $\mathbf{n}_1^\mathsf{T}\mathbf{n}_2=\mathbf{l}_1^\mathsf{T}KK^\mathsf{T}\mathbf{l}_2=\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_2$ 推出，和 MVG §8.6.2 一致。

---

## 5. 垂直關係：消失點和消失線之間

[▶ 41:08](https://youtu.be/9TuPY67JBpo?t=2468)

（MVG §8.6.3）

**(i) 兩個垂直方向的消失點**：

$$
\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_2=0
$$

- 它們對 $\omega$ 共軛。來自夾角公式 $\cos90^\circ=0$。
- 例：$\mathbf{v}_1$ 是垂直於地面的方向的消失點，$\mathbf{v}_2$ 是地面上任一方向的消失點（它在地面消失線上）。

**(ii) 一條線垂直於一個平面**：線的消失點 $\mathbf{v}$ 和平面的消失線 $\mathbf{l}$ 滿足

$$
\mathbf{l}=\omega\mathbf{v},\qquad \mathbf{v}=\omega^*\mathbf{l}
$$

- 這是**極點–極線關係**（第 2 節）：$\mathbf{v}$ 是極點，$\mathbf{l}$ 是它對 $\omega$ 的極線。

**(iii) 兩個垂直平面的消失線**：

$$
\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_2=0
$$

- 來自 4.2(c) 的夾角公式 $\cos90^\circ=0$。

---

## 6. 單張影像量測垂直線段的長度比

[▶ 44:22](https://youtu.be/9TuPY67JBpo?t=2662)

（MVG §8.7 Result 8.24、Algorithm 8.1）

**在解什麼**：已知地面的**消失線** $\mathbf{l}$ 和**垂直方向的消失點** $\mathbf{v}$，量兩條**站在地面上的垂直線段**的實際長度比。

- 不能直接比影像上的長度：同樣高的東西，離相機越遠，在影像上越短。
- 給定：$\mathbf{l}$、$\mathbf{v}$；兩條線段的底 $\mathbf{b}_1,\mathbf{b}_2$、頂 $\mathbf{t}_1,\mathbf{t}_2$（影像上）。求 $d_2/d_1$（真實長度比）。

**步驟** [▶ 47:08](https://youtu.be/9TuPY67JBpo?t=2828)：

1. **把線段 1 的高度「搬」到線段 2 的位置**：
   - 兩個底點的連線 $\mathbf{b}_1\times\mathbf{b}_2$ 在地面上，和消失線交於 $\mathbf{u}$：
$$
\mathbf{u}=(\mathbf{b}_1\times\mathbf{b}_2)\times\mathbf{l}
$$
   - 從 $\mathbf{t}_1$ 往 $\mathbf{u}$ 畫線——在場景中它平行於地面上的 $\mathbf{b}_1\mathbf{b}_2$。這條線和線段 2 所在的直線 $\mathbf{l}_2=\mathbf{b}_2\times\mathbf{v}$ 交於
$$
\tilde{\mathbf{t}}_1=(\mathbf{t}_1\times\mathbf{u})\times\mathbf{l}_2
$$
   - $\tilde{\mathbf{t}}_1$ 在場景中和 $\mathbf{t}_1$ 一樣高（線段 1 的高度被平移到線段 2 的位置）。
2. **在線段 2 所在的直線上做 1D 射影變換**：這條線上有 4 個點 $\mathbf{b}_2$、$\tilde{\mathbf{t}}_1$、$\mathbf{t}_2$、$\mathbf{v}$。
   - 用 1D 座標：$\mathbf{b}_2$ 當原點 0，其他三點的座標是 $\tilde{t}_1$、$t_2$、$v$（到 $\mathbf{b}_2$ 的距離）。
   - 找 $H_{2\times2}$：$\mathbf{b}_2$（$(0,1)^\mathsf{T}$）不動、$\mathbf{v}$（$(v,1)^\mathsf{T}$）送到無窮遠 $(1,0)^\mathsf{T}$：
$$
H_{2\times2}=\begin{pmatrix}1&0\\1&-v\end{pmatrix}
$$
   - 這把影像中的直線映成 3D 中的垂直線（消失點回到無窮遠）。
3. **映射兩個頂點** [▶ 51:58](https://youtu.be/9TuPY67JBpo?t=3118)：
$$
H_{2\times2}\begin{pmatrix}\tilde{t}_1\\1\end{pmatrix}=\begin{pmatrix}\tilde{t}_1\\\tilde{t}_1-v\end{pmatrix},\qquad H_{2\times2}\begin{pmatrix}t_2\\1\end{pmatrix}=\begin{pmatrix}t_2\\t_2-v\end{pmatrix}
$$
4. 地面在 0，所以兩個高度是 $d_1\propto\frac{\tilde{t}_1}{\tilde{t}_1-v}$、$d_2\propto\frac{t_2}{t_2-v}$。取比：
$$
\frac{d_1}{d_2}=\frac{\tilde{t}_1(v-t_2)}{t_2(v-\tilde{t}_1)}
$$

（最後的比值依 MVG Algorithm 8.1 寫出；逐字稿只說「取兩者的比，得到用這兩個座標表示的式子」。）

> 以下**不是逐字稿內容**，是驗證 $H_{2\times2}$：$H(0,1)^\mathsf{T}=(0,-v)^\mathsf{T}\sim(0,1)^\mathsf{T}$ ✓（原點不動）；$H(v,1)^\mathsf{T}=(v,v-v)^\mathsf{T}=(v,0)^\mathsf{T}\sim(1,0)^\mathsf{T}$ ✓（消失點到無窮遠）。

**應用：量人的身高** [▶ 53:23](https://youtu.be/9TuPY67JBpo?t=3203)（MVG Example 8.25）：

- 場景中有一個已知高度的固定物體（例如一個櫃子，量一次就好）當線段 1。
- 人站在地上：腳 $\mathbf{b}_2$、頭頂 $\mathbf{t}_2$。
- 垂直消失點 $\mathbf{v}$ 用兩條垂直線（例如櫃子的兩個邊）求交點（可能在影像外）。
- 算出 $d_2/d_1$，乘上櫃子的實際高度 → 人的實際身高。

---

## 7. 從單張影像求 K

[▶ 55:26](https://youtu.be/9TuPY67JBpo?t=3326)

前面都是「已知 $K$ → 求場景性質」。反過來，**$K$ 未知時，用這些關係求 $\omega$**，再得 $K$。

**$\omega$ 的約束來源**（MVG Table 8.1）：

| 條件 | 約束 | 每個條件給幾條 |
|---|---|---|
| 兩個垂直方向的消失點 | $\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_2=0$ | 1 |
| 消失點 $\mathbf{v}$ 和垂直於它的平面的消失線 $\mathbf{l}$ | $\mathbf{l}=\omega\mathbf{v}$，寫成 $[\mathbf{l}]_\times\omega\mathbf{v}=\mathbf{0}$ | 2 |
| 已知度量結構的平面（正方形）的 homography | $\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_2=0$，$\mathbf{h}_1^\mathsf{T}\omega\mathbf{h}_1=\mathbf{h}_2^\mathsf{T}\omega\mathbf{h}_2$ | 2 |
| 斜切 $s=0$ | $\omega_{12}=\omega_{21}=0$ | 1 |
| 正方形像素（$s=0$ 且 $f_x=f_y$） | $\omega_{11}=\omega_{22}$ | 再 1 |

- **(ii) 的寫法** [▶ 56:41](https://youtu.be/9TuPY67JBpo?t=3401)：$\mathbf{l}=\omega\mathbf{v}$ 只差縮放，寫成「兩向量平行」$\mathbf{l}\times\omega\mathbf{v}=\mathbf{0}$，對 $\omega$ 線性，給 2 條。講者說要至少三組。
- **內部約束** [▶ 57:40](https://youtu.be/9TuPY67JBpo?t=3460)：$K$ 的 $s=0$ 代進 $\omega=(KK^\mathsf{T})^{-1}$，會得到 $\omega_{12}=\omega_{21}=0$；再加 $f_x=f_y$ 得 $\omega_{11}=\omega_{22}$。

> 以下**不是逐字稿內容**，是驗證 $s=0$ 的情況：$K=\begin{pmatrix}f_x&0&p_x\\0&f_y&p_y\\0&0&1\end{pmatrix}$，$K^{-1}=\begin{pmatrix}1/f_x&0&-p_x/f_x\\0&1/f_y&-p_y/f_y\\0&0&1\end{pmatrix}$，$\omega=K^{-\mathsf{T}}K^{-1}$ 的 $(1,2)$ 元素是 $K^{-1}$ 第一行和第二行的內積 $=\frac{1}{f_x}\cdot0+0\cdot\frac{1}{f_y}+0\cdot0=0$ ✓。$(1,1)=1/f_x^2$、$(2,2)=1/f_y^2$，$f_x=f_y$ 時相等 ✓。MVG 另外指出：$\omega^*=KK^\mathsf{T}$ 沒有這麼簡單的對應關係，所以約束要加在 $\omega$ 上。

**演算法**（MVG Algorithm 8.2）[▶ 58:40](https://youtu.be/9TuPY67JBpo?t=3520)：

1. 把 $\omega$ 的 6 個獨立元素排成向量 $\mathbf{w}$。
2. 每個約束都是 $\mathbf{a}^\mathsf{T}\mathbf{w}=0$ 的形式（對 $\mathbf{w}$ 線性）。
3. 任意組合，湊到 **5 條以上**（$\omega$ 有 5 個自由度），疊成 $A\mathbf{w}=\mathbf{0}$。
4. SVD 解 $\mathbf{w}$，排回 $\omega$。
5. Cholesky 分解得 $K$（上三角或下三角，對應 $K$）。

⚠️ 逐字稿缺字：Whisper 把 Cholesky 寫成 “kolowski”、把 pole–polar 寫成 “pro-polite”、把 orthogonal 寫成 “octagonal”。

【課本補充】MVG Example 8.27：三個互相垂直方向的消失點（例如建築物的三個主方向）給 3 條 (i) 類約束，加上「正方形像素」的 2 條內部約束，共 5 條，就能從**一張照片**求出 $K$。

---

## 8. Lecture 6 總結

[▶ 59:55](https://youtu.be/9TuPY67JBpo?t=3595)

1. 相機投影對平面、線、二次曲線、二次曲面的前向、反向作用（第 13 集）。
2. 固定相機中心、增加焦距、純旋轉對影像的影響（第 13 集）。
3. 絕對二次曲線的像的定義，以及用它校正內參（第 14–15 集）。
4. 消失點、消失線的定義，用它們求場景和相機的幾何性質（本集）。

---

## 9. 一頁速查表

### 極點／極線

| 公式 | 關鍵一步 |
|---|---|
| 極線 $\mathbf{l}=C\mathbf{x}$（$\mathbf{x}$ 在 $C$ 上時是切線） | $\mathbf{x}=C\mathbf{z}_1\times C\mathbf{z}_2=\det(C)C^{-1}(\mathbf{z}_1\times\mathbf{z}_2)$ |
| 共軛點 $\mathbf{y}^\mathsf{T}C\mathbf{x}=0$（對稱） | $C$ 對稱 |
| 共軛線 $\mathbf{l}^\mathsf{T}C^*\mathbf{m}=0$ | 對偶 |

### 消失點、消失線（$\omega=(KK^\mathsf{T})^{-1}$，$\omega^*=KK^\mathsf{T}$）

| 公式 | 關鍵一步 |
|---|---|
| $\mathbf{v}=K\mathbf{d}$ | $\lim_{\lambda\to\infty}(\mathbf{a}+\lambda K\mathbf{d})/\lambda$ |
| 兩對消失點 → $R$（$\mathbf{d}'=R\mathbf{d}$，$\mathbf{d}=K^{-1}\mathbf{v}$ 正規化） | 平移乘 0 沒作用 |
| 線夾角 $\cos\theta=\frac{\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_2}{\sqrt{\cdots}}$ | 第 14 集 |
| 消失線 $\mathbf{l}=\mathbf{v}_1\times\mathbf{v}_2$；平面法向 $\mathbf{n}=K^\mathsf{T}\mathbf{l}$ | 第 14 集 |
| 平面夾角 $\cos\theta=\frac{\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_2}{\sqrt{\cdots}}$ | $\mathbf{n}_1^\mathsf{T}\mathbf{n}_2=\mathbf{l}_1^\mathsf{T}KK^\mathsf{T}\mathbf{l}_2$ |

### 垂直關係

- 垂直方向：$\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_2=0$
- 線 ⊥ 面：$\mathbf{l}=\omega\mathbf{v}$（極點–極線）
- 面 ⊥ 面：$\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_2=0$

### 量高度（MVG Algorithm 8.1）

1. $\mathbf{u}=(\mathbf{b}_1\times\mathbf{b}_2)\times\mathbf{l}$
2. $\tilde{\mathbf{t}}_1=(\mathbf{t}_1\times\mathbf{u})\times(\mathbf{b}_2\times\mathbf{v})$
3. 在 $\mathbf{b}_2$ 為原點的 1D 座標：$\dfrac{d_1}{d_2}=\dfrac{\tilde{t}_1(v-t_2)}{t_2(v-\tilde{t}_1)}$；關鍵一步 $H_{2\times2}=\begin{pmatrix}1&0\\1&-v\end{pmatrix}$ 把 $\mathbf{v}$ 送到無窮遠。

### 從單張影像求 K

約束：垂直消失點 1 條、線⊥面 2 條、正方形 homography 2 條、$s=0$ 1 條、方形像素 1 條；湊 ≥5 條 → SVD → Cholesky。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 極點／極線、共軛 | 第 16–19 集（極線 $\mathbf{l}'=F\mathbf{x}$ 的名字和形式都類似） |
| $\mathbf{d}=K^{-1}\mathbf{v}$、$\mathbf{d}'=R\mathbf{d}$ | 第 16–19 集（$E$ 分解出 $R$）；第 20–22 集（PnP） |
| 從 $\omega$ 求 $K$ | Lecture 13 自校正（本播放清單沒有）；第 27–30 集（度量重建） |
| 1D 射影變換、交比 | 第 23–26 集（三視角幾何中的點轉移） |

---

## 附：本集一句話總結

> **$\omega$ 是二次曲線，所以有極點–極線和共軛關係：垂直方向的消失點 $\mathbf{v}_1^\mathsf{T}\omega\mathbf{v}_2=0$、線⊥面 $\mathbf{l}=\omega\mathbf{v}$、面⊥面 $\mathbf{l}_1^\mathsf{T}\omega^*\mathbf{l}_2=0$；消失點 $\mathbf{v}=K\mathbf{d}$ 只看方向，已知 $K$ 就能求旋轉、夾角、平面方向，甚至用消失線和垂直消失點量出人的身高；反過來 $K$ 未知時，把這些關係和三個正方形、零斜切、方形像素的約束湊滿 5 條，就能從單張照片解出 $\omega$、Cholesky 得 $K$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 6 (Part 3) 錄影逐字稿（Whisper `medium.en`，1:00:41）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §8.5、§2.8.1、§8.6–8.8 整理。*
