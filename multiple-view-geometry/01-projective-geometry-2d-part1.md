---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 01
lecture: Lecture 1 (Part 1) – 2D and 1D projective geometry
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/LAHQ_qIzNGU
notes: MVG §2.1–2.2.2（書頁 25–30，PDF 頁 43–48）
---

# 第 01 集 · Lecture 1 (Part 1)：2D 射影幾何——齊次座標、點與線、對偶 [▶ 影片](https://youtu.be/LAHQ_qIzNGU)

← 上一集：（無） ｜ [總目錄](PROGRESS.md) ｜ 下一集：[02-projective-geometry-2d-part2](02-projective-geometry-2d-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 01 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（55:26，Whisper `medium.en` 轉錄）＋ MVG §2.1–2.2.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要學射影幾何](#1-為什麼要學射影幾何)
  - [1.1 我們看到的世界都經過射影變換](#11-我們看到的世界都經過射影變換)
  - [1.2 哪些性質會被破壞](#12-哪些性質會被破壞)
  - [1.3 唯一保住的性質：直線還是直線](#13-唯一保住的性質直線還是直線)
- [2. 歐氏幾何 vs. 射影幾何](#2-歐氏幾何-vs-射影幾何)
- [3. 齊次座標表示點](#3-齊次座標表示點)
  - [3.1 定義與換算](#31-定義與換算)
  - [3.2 無窮遠點](#32-無窮遠點)
  - [3.3 幾何模型：點 = 過原點的射線](#33-幾何模型點--過原點的射線)
- [4. 齊次座標表示線](#4-齊次座標表示線)
- [5. 點在線上：關聯關係](#5-點在線上關聯關係)
- [6. 自由度](#6-自由度)
- [7. 兩線交點、兩點連線：外積](#7-兩線交點兩點連線外積)
  - [7.1 兩線交點](#71-兩線交點)
  - [7.2 兩點連線](#72-兩點連線)
- [8. 平行線交於無窮遠點、無窮遠線](#8-平行線交於無窮遠點無窮遠線)
- [9. 對偶原理](#9-對偶原理)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/LAHQ_qIzNGU?t=0)

Lecture 1 的目標（Part 1 和 Part 2 合起來）：

| 目標 | 本集？ | MVG |
|---|---|---|
| 說得出歐氏幾何（Euclidean geometry）和射影幾何（projective geometry）的差別 | ✅ | §2.1 |
| 用齊次座標（homogeneous coordinates）表示 2D 的點、線 | ✅ | §2.2.1 |
| 用齊次座標表示二次曲線（conic） | 下一集 | §2.2.3 |
| 點與線的對偶（duality） | ✅ | §2.2.2 末 |
| 二次曲線與對偶二次曲線（dual conic） | 下一集 | §2.2.3 |
| 2D 變換階層（hierarchy of transformations）作用在點、線、二次曲線上 | 下一集 | §2.3–2.4 |

[▶ 01:00](https://youtu.be/LAHQ_qIzNGU?t=60) 講者說內容主要取自：

- Hartley & Zisserman《Multiple View Geometry in Computer Vision》**第 2 章**。
- Ma Yi 等人《An Invitation to 3-D Vision》**第 2 章**（本筆記不用這本，BRIEF 沒列）。

⚠️ 逐字稿缺字：Whisper 把 Zisserman 寫成 “Zizerman”。

---

## 1. 為什麼要學射影幾何

### 1.1 我們看到的世界都經過射影變換

[▶ 01:35](https://youtu.be/LAHQ_qIzNGU?t=95)

- 我們活在 3D 世界，這個世界遵守**歐氏幾何**，可以用笛卡兒座標（Cartesian coordinates）描述。
- 但只要睜開眼睛，看到的就是**經過射影變換（projective transformation）之後的樣子**：
  物體反射的光，經過眼睛匯聚到視網膜上，這個過程就是射影變換。
- 數位相機一樣：光投射到相機的感光元件上。講者說眼睛是「最強的相機」。

### 1.2 哪些性質會被破壞

[▶ 02:19](https://youtu.be/LAHQ_qIzNGU?t=139) 講者用一張建築物照片舉三個例子：

| 3D 世界裡 | 照片上 |
|---|---|
| 建築物上兩條**平行線**，永遠不會相交 | 在照片裡**相交於一個有限的點** |
| **長方形**的窗戶 | 變成「某種平行四邊形」 |
| **圓形**的時鐘面 | 變成**橢圓** |

> 以下**不是逐字稿內容**，是依「平行性不被保留」推論的：講者說長方形變成「某種平行四邊形」，但平行線既然會相交，嚴格說來長方形一般會變成**任意四邊形**（對邊不一定平行）。只有在仿射變換（下一集）下才保證是平行四邊形。

[▶ 05:05](https://youtu.be/LAHQ_qIzNGU?t=305) 再仔細看，下面這些量**全部不保留**：

- **角度**：平行線本來夾角 0，投影後相交、有夾角；本來夾角 $\theta$ 的兩線，投影後變成 $\theta'\neq\theta$。
- **距離**：兩點距離 $d$ 變成 $d'$；兩條線之間的距離也一樣。
- **距離的比值**：四個點形成兩段 $d_1$、$d_2$，投影後 $d_2'/d_1'\neq d_2/d_1$。

講者說：這些分析之後都可以用齊次座標寫成數學。

### 1.3 唯一保住的性質：直線還是直線

[▶ 07:49](https://youtu.be/LAHQ_qIzNGU?t=469)

- 角度、距離、比值都變了，那要怎麼研究射影變換？
- 答案：**直線性（straightness）被保留**。場景裡的直線，投影後還是直線。
- 這是對射影變換**最一般的要求**。於是可以反過來，**用「保持直線」來定義射影變換**：

$$
h:\ \mathbb{P}^2\to\mathbb{P}^2,\quad \text{把直線映到直線}
$$

這裡 $\mathbb{P}^2$ 是 2D 射影空間（projective space），之後會定義。講者暫時把這個映射叫 $H$。

- **射影幾何**更一般地研究：在射影變換下**不變（invariant）**的幾何性質。直線性是第一個例子，整門課還會看到其他不變量。

---

## 2. 歐氏幾何 vs. 射影幾何

[▶ 10:26](https://youtu.be/LAHQ_qIzNGU?t=626)

| | 歐氏幾何 | 射影幾何 |
|---|---|---|
| 類型 | **綜合幾何（synthetic geometry）**：公理法（axiomatic method） | **解析幾何（analytic geometry）**：用座標和代數 |
| 工具 | 圓規、直尺；例如量邊長再用餘弦定理、正弦定理算角度 | 座標、**線性代數** |
| 座標 | 笛卡兒座標，$\mathbb{R}^n$ | 齊次座標，$\mathbb{P}^n$ |
| 無窮遠 | 表示不了，只能當「例外情況」 | 用一組普通數字就能表示 |

【口頭】講者提到拉斐爾 1500 年代的畫（雅典學院），畫裡希臘學者用圓規和直尺解幾何題，說明歐氏幾何的歷史很長。

[▶ 13:19](https://youtu.be/LAHQ_qIzNGU?t=799) **射影幾何最重要的成果之一**：**無窮遠的幾何可以漂亮地表示出來**。

- 在歐氏空間裡，無窮遠的點、線、面沒辦法表示；硬要寫就得用「$\infty$」，在數學運算裡變成例外情況。
- 在齊次座標裡，無窮遠的點、線、面**只是一組普通的數字**，不需要特別處理。

---

## 3. 齊次座標表示點

### 3.1 定義與換算

[▶ 14:25](https://youtu.be/LAHQ_qIzNGU?t=865)

- 2D 歐氏空間的點：兩個實數 $(x,y)\in\mathbb{R}^2$。
- 2D 射影空間的點：**三個**實數，屬於 $\mathbb{R}^3$：

$$
\begin{pmatrix} kx \\ ky \\ k \end{pmatrix}\ \longleftrightarrow\ \begin{pmatrix} kx/k \\ ky/k \end{pmatrix}=\begin{pmatrix} x \\ y \end{pmatrix}
$$

- **齊次 → 笛卡兒**：前兩個分量除以第三個分量。
- 對所有 $k\neq0$，$(kx,ky,k)^\mathsf{T}$ 都代表**同一個點** $(x,y)$。也就是說 $(kx,ky,k)^\mathsf{T}=k\,(x,y,1)^\mathsf{T}$，$k$ 只是一個整體的縮放。

一般寫法 [▶ 33:24](https://youtu.be/LAHQ_qIzNGU?t=2004)：

$$
\mathbf{x}=\begin{pmatrix} x_1\\ x_2\\ x_3\end{pmatrix}\in\mathbb{P}^2\quad\longleftrightarrow\quad\begin{pmatrix} x_1/x_3\\ x_2/x_3\end{pmatrix}\in\mathbb{R}^2
$$

【課本補充】（MVG §2.2.1）

- 只差一個整體縮放的向量，視為**等價**。一個等價類叫做**齊次向量（homogeneous vector）**。
- $\mathbb{P}^2$ 的正式定義：$\mathbb{R}^3-\{(0,0,0)^\mathsf{T}\}$ 在這個等價關係下的**所有等價類**。
- 課本區分：**齊次座標** $(x_1,x_2,x_3)^\mathsf{T}$ 是 3 維向量；**非齊次座標（inhomogeneous coordinates）** $(x,y)^\mathsf{T}$ 是 2 維向量。
- 課本慣例：幾何物件一律用**行向量（column vector）**，粗體 $\mathbf{x}$ 是行向量，$\mathbf{x}^\mathsf{T}$ 是列向量。

### 3.2 無窮遠點

[▶ 16:50](https://youtu.be/LAHQ_qIzNGU?t=1010)

把第三個分量設為 $0$：

$$
\begin{pmatrix} x\\ y\\ 0\end{pmatrix}\ \longrightarrow\ \begin{pmatrix} x/0\\ y/0\end{pmatrix}=\infty
$$

- 換回笛卡兒座標會除以零，代表一個**無窮遠點（point at infinity）**。
- 在笛卡兒座標裡直接寫 $\infty$ 很不方便；在齊次座標裡只要「最後一個數是 0」，很乾淨。
- 一般來說，$\mathbb{R}^n$ 歐氏空間可以擴充成 $\mathbb{P}^n$ 射影空間，點用齊次向量表示。
- 【口頭】講者預告：下一講會把這套推廣到 3D，3D 有一些 2D 沒有的特殊性質，尤其是變換階層。

### 3.3 幾何模型：點 = 過原點的射線

[▶ 19:08](https://youtu.be/LAHQ_qIzNGU?t=1148)

把 $(x_1,x_2,x_3)$ 畫在 $\mathbb{R}^3$ 的 $xyz$ 座標裡：

- $(x,y,1)$、$(2x,2y,2)$、……、$(kx,ky,k)$ 都代表同一個點。
- 把它們連起來，是一條**通過原點的射線（ray）**。
- 所以：**$\mathbb{P}^2$ 的一個點 = $\mathbb{R}^3$ 中過原點的一條射線**。
- 射線和平面 $x_3=1$ 的交點，就是那個點的笛卡兒座標 $(x,y)$。
- $k$ 不必是整數，任何非零實數都可以（例如 $1.1$、$1.23$）。

在這個模型裡：

- **無窮遠點** $(x,y,0)$：躺在 $xy$ 平面上的向量。它們和平面 $x_3=1$ 平行，永遠碰不到。
- **無窮遠線** $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$（第 8 節推導）：講者說它對應 $z$ 軸上的向量。
  - 解釋：線對應一個平面，用平面的法向量表示（第 4 節）。$\mathbf{l}_\infty$ 對應的平面就是 $xy$ 平面，法向量是 $z$ 軸方向 $(0,0,1)$。
- **原點** $(0,0,0)$：**沒有定義**，齊次座標裡不用它。

【課本補充】MVG Fig. 2.1：$\mathbb{P}^2$ 的點和線分別是 $\mathbb{R}^3$ 中過原點的**射線**和**平面**。兩條不同的射線恰好決定一個平面，兩個平面恰好交於一條射線——對應「兩點決定一線、兩線交於一點」。

---

## 4. 齊次座標表示線

[▶ 23:07](https://youtu.be/LAHQ_qIzNGU?t=1387)

**幾何直覺**：

- 一條 2D 直線 $\mathbf{l}$ 和原點一起，張成 $\mathbb{R}^3$ 中一個**過原點的平面**。
- 一個平面可以用它的**法向量（normal vector）**表示。
- 所以：**線的齊次表示 = 那個平面的法向量**。

**代數**：2D 直線的方程式

$$
ax+by+c=0
$$

整理成高中熟悉的形式：

$$
y=-\frac{a}{b}x-\frac{c}{b}\quad(\text{即 } y=mx+c' \text{ 的形式})
$$

- $a,b$ 決定斜率，$c$ 跟 $y$ 截距有關。
- 不同的 $(a,b,c)$ 給出不同的線，所以**用係數向量表示線**，不必管 $x,y$：

$$
\mathbf{l}=\begin{pmatrix} a\\ b\\ c\end{pmatrix}
$$

**不是一對一** [▶ 27:41](https://youtu.be/LAHQ_qIzNGU?t=1661)：

- $k(ax+by+c)=0$ 和 $ax+by+c=0$ 是同一條線（$k$ 可以約掉）。
- 所以 $(a,b,c)^\mathsf{T}$ 和 $k(a,b,c)^\mathsf{T}$（$k\neq0$）代表**同一條線**——它們屬於同一個**等價類（equivalence class）**。
- 但當成普通向量，$(ka,kb,kc)^\mathsf{T}$ 對不同 $k$ 是不同的向量。這就是「齊次」和「普通向量」的差別。
- $(0,0,0)^\mathsf{T}$ 既不代表線也不代表點，講者叫它「singular point」。

**點和線長得一樣，意思不同**：

- 點 $(kx,ky,k)$：射線上的所有點，$k$ 決定在哪個平面上。
- 線 $(a,b,c)$：直線方程式的係數。

---

## 5. 點在線上：關聯關係

[▶ 29:51](https://youtu.be/LAHQ_qIzNGU?t=1791)

**關聯關係（incidence relation）**：點和線怎麼重合、相交。

點 $(x,y)$ 在線 $(a,b,c)$ 上，若且唯若 $ax+by+c=0$。寫成向量內積：

$$
ax+by+c=\begin{pmatrix} x & y & 1\end{pmatrix}\begin{pmatrix} a\\ b\\ c\end{pmatrix}=0
$$

注意 $(x,y,1)$ 剛好就是點的齊次座標，$(a,b,c)^\mathsf{T}$ 剛好就是線的齊次座標。

**縮放不影響** [▶ 32:01](https://youtu.be/LAHQ_qIzNGU?t=1921)：

$$
\begin{pmatrix} kx & ky & k\end{pmatrix}\left(k'\begin{pmatrix} a\\ b\\ c\end{pmatrix}\right)=kk'\,(ax+by+c)=0\iff ax+by+c=0
$$

- 這同時說明：「用 $(kx,ky,k)$ 對所有 $k$ 表示同一點」是**合理的定義**。

> **Result 2.1（MVG）** 點 $\mathbf{x}$ 在線 $\mathbf{l}$ 上 $\iff$ $\mathbf{x}^\mathsf{T}\mathbf{l}=0$。

- $\mathbf{x}^\mathsf{T}\mathbf{l}$ 就是內積（點積），$\mathbf{x}^\mathsf{T}\mathbf{l}=\mathbf{l}^\mathsf{T}\mathbf{x}$，順序可以交換。
- 這是本課第一個例子：**用線性代數描述射影幾何**。
- 順序可交換 → 點和線的角色可以互換 → 第 9 節的**對偶原理**。

---

## 6. 自由度

[▶ 35:26](https://youtu.be/LAHQ_qIzNGU?t=2126)

- **點**：2 個自由度（degrees of freedom, dof），就是 $x$ 和 $y$。
- **線**：也是 2 個自由度。雖然有 3 個數 $a,b,c$，但只有**兩個獨立比值** $a:b:c$ 有意義。
  - 寫成 $y=mx+c'$ 就看得出來：只有斜率 $m=-a/b$ 和截距 $c'=-c/b$ 兩個參數。

講者口誤 [▶ 36:19](https://youtu.be/LAHQ_qIzNGU?t=2179)：先說「$m$ 是 $b$ 除以 $c$」，馬上自己更正為「$c$ 也要除以 $b$」，結論是「$a/b$ 和 $c/b$ 這兩個比值」。正確寫法是上面那樣。

---

## 7. 兩線交點、兩點連線：外積

### 7.1 兩線交點

[▶ 36:48](https://youtu.be/LAHQ_qIzNGU?t=2208)

- 在射影平面上，**任兩條不同的線一定交於一點**，**包括平行線**（定義成交在無窮遠點）。

> **Result 2.2（MVG）** 兩條線 $\mathbf{l}$、$\mathbf{l}'$ 的交點是 $\mathbf{x}=\mathbf{l}\times\mathbf{l}'$。

**幾何直覺** [▶ 37:43](https://youtu.be/LAHQ_qIzNGU?t=2263)：

- 兩條線各自對應一個過原點的平面，法向量分別是 $\mathbf{l}$、$\mathbf{l}'$。
- 兩個平面相交於一條過原點的射線——那就是交點 $\mathbf{x}$。
- 這條射線同時垂直於兩個法向量 → 用右手定則，$\mathbf{l}\times\mathbf{l}'$ 正好是這個方向。

**代數證明** [▶ 40:12](https://youtu.be/LAHQ_qIzNGU?t=2412)：

1. 設 $\mathbf{v}=\mathbf{l}\times\mathbf{l}'$。外積的結果垂直於兩個輸入向量。
2. 兩個垂直向量的內積是 $0$：$\mathbf{a}\cdot\mathbf{b}=|\mathbf{a}||\mathbf{b}|\cos 90^\circ=0$。所以得到**三重純量積恆等式（triple scalar product identity）**：
$$
\mathbf{l}\cdot(\mathbf{l}\times\mathbf{l}')=\mathbf{l}'\cdot(\mathbf{l}\times\mathbf{l}')=0
$$
3. 把 $\mathbf{l}\times\mathbf{l}'$ 叫做 $\mathbf{x}$，上式就是 $\mathbf{l}^\mathsf{T}\mathbf{x}=0$ 且 $\mathbf{l}'^\mathsf{T}\mathbf{x}=0$。
4. 由 Result 2.1，$\mathbf{x}$ **同時在兩條線上**，所以它就是交點。∎

【課本補充】MVG Example 2.3：$x=1$ 寫成 $-x+1=0$，$\mathbf{l}=(-1,0,1)^\mathsf{T}$；$y=1$ 寫成 $-y+1=0$，$\mathbf{l}'=(0,-1,1)^\mathsf{T}$。

$$
\mathbf{l}\times\mathbf{l}'=\begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k}\\ -1 & 0 & 1\\ 0 & -1 & 1\end{vmatrix}=\begin{pmatrix} 0\cdot1-1\cdot(-1)\\ 1\cdot0-(-1)\cdot1\\ (-1)(-1)-0\cdot0\end{pmatrix}=\begin{pmatrix}1\\1\\1\end{pmatrix}
$$

換回笛卡兒座標是 $(1,1)$，正確。

### 7.2 兩點連線

[▶ 43:31](https://youtu.be/LAHQ_qIzNGU?t=2611)

> **Result 2.4（MVG）** 通過兩點 $\mathbf{x}$、$\mathbf{x}'$ 的線是 $\mathbf{l}=\mathbf{x}\times\mathbf{x}'$。

**幾何直覺**：兩點是兩條射線，它們張成一個過原點的平面；外積 $\mathbf{x}\times\mathbf{x}'$ 是這個平面的法向量，也就是那條線。

**代數證明**（同樣的技巧）：

$$
\mathbf{x}\cdot(\mathbf{x}\times\mathbf{x}')=0,\qquad \mathbf{x}'\cdot(\mathbf{x}\times\mathbf{x}')=0
$$

令 $\mathbf{l}=\mathbf{x}\times\mathbf{x}'$，上式就是 $\mathbf{x}^\mathsf{T}\mathbf{l}=\mathbf{x}'^\mathsf{T}\mathbf{l}=0$：兩點都在 $\mathbf{l}$ 上。∎

⚠️ 逐字稿缺字：Whisper 多次把 orthogonal 寫成 “octagonal”。

---

## 8. 平行線交於無窮遠點、無窮遠線

[▶ 45:43](https://youtu.be/LAHQ_qIzNGU?t=2743)

在笛卡兒座標裡，平行線的交點是個問題：要嘛「不相交」，要嘛「交在無窮遠」，算的時候會除以零。齊次座標沒有這個例外。

**兩條平行線**：

$$
ax+by+c=0,\qquad ax+by+c'=0\qquad\Longrightarrow\qquad \mathbf{l}=\begin{pmatrix}a\\b\\c\end{pmatrix},\ \mathbf{l}'=\begin{pmatrix}a\\b\\c'\end{pmatrix}
$$

- 改寫成 $y=-\frac{a}{b}x-\frac{c}{b}$：前兩個係數 $a,b$ 一樣 → 斜率一樣 → 平行，只有截距不同。

**交點**（逐步算外積）：

$$
\mathbf{l}\times\mathbf{l}'=\begin{pmatrix} b c'-c b\\ c a-a c'\\ ab-ba\end{pmatrix}=\begin{pmatrix} b(c'-c)\\ -a(c'-c)\\ 0\end{pmatrix}=(c'-c)\begin{pmatrix} b\\ -a\\ 0\end{pmatrix}
$$

- 去掉縮放因子 $(c'-c)$，交點是 $(b,-a,0)^\mathsf{T}$。
- 第三個分量是 $0$ → **無窮遠點**。換回笛卡兒座標是 $(b/0,\,-a/0)$，就是無窮遠。
- 結論：**兩條平行線交於無窮遠點**，齊次座標寫起來很乾淨。

**例子**（MVG Example 2.5）[▶ 49:01](https://youtu.be/LAHQ_qIzNGU?t=2941)：$x=1$ 和 $x=2$。

$$
\mathbf{l}=\begin{pmatrix}-1\\0\\1\end{pmatrix},\quad \mathbf{l}'=\begin{pmatrix}-1\\0\\2\end{pmatrix},\quad \mathbf{l}\times\mathbf{l}'=\begin{pmatrix} 0\cdot2-1\cdot0\\ 1\cdot(-1)-(-1)\cdot2\\ (-1)\cdot0-0\cdot(-1)\end{pmatrix}=\begin{pmatrix}0\\1\\0\end{pmatrix}
$$

- 最後一個分量是 $0$：無窮遠點。
- 前兩個分量 $(0,1)$：指向 $y$ 方向。
- 和圖一致：兩條線都沿 $y$ 方向，所以在 $y$ 方向的無窮遠相交。

**無窮遠線** [▶ 50:42](https://youtu.be/LAHQ_qIzNGU?t=3042)：

- 所有平行於 $(a,b,c)$ 的線（不論 $c$）都交於同一個**理想點（ideal point）** $(b,-a,0)^\mathsf{T}$。
- 所有理想點 $(x_1,x_2,0)^\mathsf{T}$ 都在**無窮遠線** $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$ 上，因為
$$
\begin{pmatrix}0&0&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\\0\end{pmatrix}=0
$$
- 所以：**任兩條平行線，都和無窮遠線交在同一個理想點**。

**理想點 = 方向** [▶ 51:37](https://youtu.be/LAHQ_qIzNGU?t=3097)：

- $(b,-a)$ 是線的**切向量（方向）**，$(a,b)$ 是線的**法向量**。
- 驗證兩者垂直：$(b,-a)\cdot(a,b)=ab-ba=0$。
- 線的方向改變（$a,b$ 改變）→ 理想點沿著 $\mathbf{l}_\infty$ 移動。
- 所以：**無窮遠線可以看成「平面上所有直線方向的集合」**。

**直覺**：無窮遠點不是「很遠很遠的某個地方」，它記錄的是**一個方向**。往同一方向的所有平行線，共用這個方向，所以共用同一個無窮遠點。

【課本補充】（MVG §2.2.2）

- 把 $\mathbb{R}^2$ 加上所有 $x_3=0$ 的點，就得到 $\mathbb{P}^2$。在 $\mathbb{P}^2$ 裡可以**不加條件**地說：兩條不同的線交於唯一一點，兩個不同的點決定唯一一條線。歐氏幾何做不到，平行線是例外。
- 純幾何（不用座標）的射影幾何裡，理想點和普通點**沒有任何區別**。但這本書有時會區分它們，把 $\mathbf{l}_\infty$ 當成特殊的線。

---

## 9. 對偶原理

[▶ 53:46](https://youtu.be/LAHQ_qIzNGU?t=3226)

觀察：

- 關聯方程式 $\mathbf{x}^\mathsf{T}\mathbf{l}=\mathbf{l}^\mathsf{T}\mathbf{x}=0$ 中，點和線都是 3 維向量，**位置可以互換**。
- 「兩線交點 $\mathbf{l}\times\mathbf{l}'$」和「兩點連線 $\mathbf{x}\times\mathbf{x}'$」是同一個公式，只是點和線交換。

> **Result 2.6 對偶原理（duality principle，MVG）** 2D 射影幾何的每一個定理，都有一個**對偶定理**：把原定理裡點和線的角色互換就得到。

**用處** [▶ 54:59](https://youtu.be/LAHQ_qIzNGU?t=3299)：只要證明了「兩線外積 = 交點」，就**不用再證**「兩點外積 = 連線」——對偶原理保證它成立。

【課本補充】（MVG §2.2.2）

- 套用對偶時，關聯的說法也要跟著翻譯。例如「通過兩點的線」對偶於「通過兩線的點」（也就是兩線的交點）。
- 對偶定理的證明，就是原證明的對偶版本。

（本集到 55:18 結束，下一集接著講二次曲線。）

---

## 10. 一頁速查表

### 齊次座標

| 物件 | 齊次表示 | 換回笛卡兒 | 自由度 |
|---|---|---|---|
| 點 | $\mathbf{x}=(x_1,x_2,x_3)^\mathsf{T}$，$\mathbf{x}\sim k\mathbf{x}$ | $(x_1/x_3,\ x_2/x_3)$ | 2 |
| 線 $ax+by+c=0$ | $\mathbf{l}=(a,b,c)^\mathsf{T}$，$\mathbf{l}\sim k\mathbf{l}$ | — | 2（比值 $a:b:c$） |
| 無窮遠點 | $(x_1,x_2,0)^\mathsf{T}$ | 除以 0 → 無窮遠 | 1（比值 $x_1:x_2$） |
| 無窮遠線 | $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$ | — | — |
| $(0,0,0)^\mathsf{T}$ | 不代表任何東西 | — | — |

**幾何模型**：點 = $\mathbb{R}^3$ 中過原點的射線；線 = 過原點的平面（用法向量表示）。

### 三個公式

| 公式 | 關鍵一步 |
|---|---|
| 點在線上：$\mathbf{x}^\mathsf{T}\mathbf{l}=0$ | $ax+by+c=(x,y,1)(a,b,c)^\mathsf{T}$ |
| 兩線交點：$\mathbf{x}=\mathbf{l}\times\mathbf{l}'$ | $\mathbf{l}\cdot(\mathbf{l}\times\mathbf{l}')=\mathbf{l}'\cdot(\mathbf{l}\times\mathbf{l}')=0$ → $\mathbf{x}$ 在兩線上 |
| 兩點連線：$\mathbf{l}=\mathbf{x}\times\mathbf{x}'$ | 同上，或直接用對偶原理 |

### 平行線

$$
(a,b,c)^\mathsf{T}\times(a,b,c')^\mathsf{T}=(c'-c)\,(b,-a,0)^\mathsf{T}
$$

- 交點第三分量為 0 → 無窮遠點。
- $(b,-a)$ = 線的方向；$\mathbf{l}_\infty$ = 所有方向的集合。

### 射影變換下

- **不保留**：角度、距離、距離比值、平行、圓。
- **保留**：直線性（直線 → 直線）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 齊次座標、射影空間 | 整門課的基礎；第 02 集把它用在二次曲線和變換上 |
| 無窮遠點、無窮遠線 $\mathbf{l}_\infty$ | 第 02 集（仿射變換保持 $\mathbf{l}_\infty$）；第 05–07 集（從影像恢復仿射、度量性質） |
| 對偶原理 | 第 02 集（二次曲線 vs. 對偶二次曲線）；第 03–04 集（3D 中點與平面對偶） |
| 外積求交點、連線 | 第 13–15 集（單視角量測、消失點、消失線）；第 16–19 集（極線） |
| 「保持直線」定義射影變換 | 第 02 集（射影變換 = 可逆的 $3\times3$ 矩陣） |

---

## 附：本集一句話總結

> **在齊次座標裡，2D 的點和線都是「差一個縮放就算一樣」的 3 維向量：點在線上是內積為 0，交點和連線都是外積；平行線的交點、無窮遠線也只是普通的向量，不必當例外處理。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 1 (Part 1) 錄影逐字稿（Whisper `medium.en`，55:26）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §2.1–2.2.2 整理。*
