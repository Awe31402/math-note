---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 05
lecture: Lecture 3 (Part 1) – Circular points and Absolute conic
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/T-p6d7av32Y
notes: MVG §2.7.1–2.7.3（書頁 47–54，PDF 頁 65–72）
---

# 第 05 集 · Lecture 3 (Part 1)：無窮遠線、仿射校正、circular points [▶ 影片](https://youtu.be/T-p6d7av32Y)

← 上一集：[04-rigid-motion-3d-projective-part2](04-rigid-motion-3d-projective-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[06-circular-points-absolute-conic-part2](06-circular-points-absolute-conic-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 05 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（57:17，Whisper `medium.en` 轉錄）＋ MVG §2.7.1–2.7.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 無窮遠線在仿射變換下不動](#1-無窮遠線在仿射變換下不動)
- [2. 射影變換把無窮遠拉到有限](#2-射影變換把無窮遠拉到有限)
- [3. 無窮遠線不動，但上面的點會動](#3-無窮遠線不動但上面的點會動)
- [4. 仿射校正：用消失線去除射影失真](#4-仿射校正用消失線去除射影失真)
  - [4.1 想法](#41-想法)
  - [4.2 求 H'_P](#42-求-hp)
  - [4.3 演算法](#43-演算法)
  - [4.4 怎麼把影像「拉過去」：反向映射](#44-怎麼把影像拉過去反向映射)
- [5. 反過來：用已知長度比求消失點](#5-反過來用已知長度比求消失點)
- [6. Circular points](#6-circular-points)
  - [6.1 定義：相似變換下不動的兩個點](#61-定義相似變換下不動的兩個點)
  - [6.2 為什麼叫 circular](#62-為什麼叫-circular)
- [7. Circular points 的對偶二次曲線 C*∞](#7-circular-points-的對偶二次曲線-c)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/T-p6d7av32Y?t=0)

Lecture 3 的目標（三集合起來）：

| 目標 | 本集？ | MVG |
|---|---|---|
| 用**無窮遠線**去除影像的**射影失真** | ✅ | §2.7.1–2.7.2 |
| 用 **circular points** 去除**仿射失真** | 定義 ✅；校正在下一集 | §2.7.3–2.7.5 |
| 無窮遠平面，以及它在仿射變換下的不變性 | 第 06–07 集 | §3.5 |
| 絕對二次曲線、絕對對偶二次曲面，以及它們在相似變換下的不變性 | 第 06–07 集 | §3.6–3.7 |

講者說內容取自 MVG 第 2 章和 Ma Yi 書第 2 章。

⚠️ 逐字稿缺字：Whisper 把 Hartley 寫成 “Partley”。

**整體路線** [▶ 01:06](https://youtu.be/T-p6d7av32Y?t=66)：

1. 找出影像中**無窮遠線的像** → 去除**射影**失真 → 剩下仿射失真。
2. 找出影像中 **circular points 的像** → 去除**仿射**失真 → 剩下相似失真。
3. 剩下的**相似失真**（整體旋轉、平移、縮放）**不可能去除**。

---

## 1. 無窮遠線在仿射變換下不動

[▶ 01:48](https://youtu.be/T-p6d7av32Y?t=108)

回憶第 01 集：$\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$。

> **Result 2.17（MVG）** 在射影變換 $H$ 下，$\mathbf{l}_\infty$ 是**不動線（fixed line）**，若且唯若 $H$ 是**仿射變換**。

**驗證**（「若」的方向）[▶ 03:26](https://youtu.be/T-p6d7av32Y?t=206)：線的變換是 $\mathbf{l}'=H^{-\mathsf{T}}\mathbf{l}$（第 02 集）。對仿射變換

$$
H_A=\begin{pmatrix} A & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}
\quad\Longrightarrow\quad
H_A^{-\mathsf{T}}=\begin{pmatrix} A^{-\mathsf{T}} & \mathbf{0}\\ -\mathbf{t}^\mathsf{T}A^{-\mathsf{T}} & 1\end{pmatrix}
$$

所以

$$
\mathbf{l}_\infty'=H_A^{-\mathsf{T}}\begin{pmatrix}0\\0\\1\end{pmatrix}=\begin{pmatrix}\mathbf{0}\\ 1\end{pmatrix}=\mathbf{l}_\infty
$$

（右邊只取到 $H_A^{-\mathsf{T}}$ 的最後一行。）

> 以下**不是逐字稿內容**，是依分塊矩陣推論的 $H_A^{-1}$：$H_A^{-1}=\begin{pmatrix}A^{-1} & -A^{-1}\mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$（乘回 $H_A$ 可驗證得 $I$），轉置就得到上面的 $H_A^{-\mathsf{T}}$。

- 仿射矩陣是**最一般的、滿足 $h_{31}=h_{32}=0$ 的線性變換**（最後一列是 $(0,0,1)$）。
- **意義**：只要在影像上找出 $\mathbf{l}_\infty$ 的像，就能恢復場景的**仿射性質**。

---

## 2. 射影變換把無窮遠拉到有限

[▶ 04:40](https://youtu.be/T-p6d7av32Y?t=280)

一般射影變換 $H_P=\begin{pmatrix} A & \mathbf{t}\\ \mathbf{v}^\mathsf{T} & v\end{pmatrix}$ 作用在無窮遠點上：

$$
H_P\begin{pmatrix}x_1\\x_2\\0\end{pmatrix}=\begin{pmatrix} A\begin{pmatrix}x_1\\x_2\end{pmatrix}\\ v_1x_1+v_2x_2\end{pmatrix}
$$

- 一般來說 $v_1,v_2\neq0$ → 第三個分量 $v_1x_1+v_2x_2\neq0$ → 變成**有限點**。
- 仿射變換時 $v_1=v_2=0$ → 第三個分量永遠是 0 → 無窮遠點還是無窮遠點。
- 意義：**場景裡的無窮遠點，拍成照片後會出現在影像的有限位置**（例如平行線在照片上交於一點）。

講者說「$v$ 永遠不能是 0，才是合法的射影矩陣」[▶ 05:28](https://youtu.be/T-p6d7av32Y?t=328)。

> 以下**不是逐字稿內容**：這和第 02 集講者自己說的「$v$ 可以是 0」不一致。依 MVG §2.4.4，$v$ 可以是 0（所以一般不能把 $H_P$ 縮放成 $v=1$）。這裡應是口誤。

**無窮遠線也一樣** [▶ 08:07](https://youtu.be/T-p6d7av32Y?t=487)：

$$
\mathbf{l}'=H_P^{-\mathsf{T}}\mathbf{l}_\infty
$$

一般前兩個分量不是 0（因為 $v_1,v_2\neq0$），所以 $\mathbf{l}'\neq(0,0,1)^\mathsf{T}$，變成**有限的線**。

> 以下**不是逐字稿內容**，是依分塊矩陣推論的關鍵一步：$H^{-\mathsf{T}}\mathbf{l}_\infty$ 是 $H^{-\mathsf{T}}$ 的第三行，也就是 $H^{-1}$ 的第三列。$H\mathbf{x}$ 的第三個分量是 $(\mathbf{v}^\mathsf{T},v)\mathbf{x}$，所以「$\mathbf{l}_\infty$ 的像」就是讓 $H^{-1}$ 第三列為 $(0,0,1)$ 的條件——只有 $\mathbf{v}=\mathbf{0}$ 時才成立。

**結論**：射影變換下，理想點和無窮遠線**不一定還在無窮遠**。

---

## 3. 無窮遠線不動，但上面的點會動

[▶ 09:45](https://youtu.be/T-p6d7av32Y?t=585)

- 仿射變換下 $\mathbf{l}_\infty$ 是不動的**線**，但它**不是逐點不動（not fixed pointwise）**。
- $\mathbf{l}_\infty$ 上的理想點 $\mathbf{x}_1,\mathbf{x}_2$，經過 $H_A$ 後還在 $\mathbf{l}_\infty$ 上（共線性保持），但可能換了位置、甚至換了順序。

**計算** [▶ 11:54](https://youtu.be/T-p6d7av32Y?t=714)：

$$
\begin{pmatrix} A & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\begin{pmatrix}x_1\\x_2\\0\end{pmatrix}=\begin{pmatrix} a_{11}x_1+a_{12}x_2\\ a_{21}x_1+a_{22}x_2\\ 0\end{pmatrix}
$$

- 還是理想點（第三個分量 0），但一般不是原來那個點：兩個分量都是 $x_1,x_2$ 的線性組合。

⚠️ 逐字稿缺字 [▶ 13:19](https://youtu.be/T-p6d7av32Y?t=799)：Whisper 寫 “a21 multiplied by x2 plus a22 multiplied by x2”，應為 $a_{21}x_1+a_{22}x_2$。

- 講者說：要是同一點，$A$ 乘出來必須是 $(x_1,x_2)$ 的共同倍數；例如 $A=kI$。

> 以下**不是逐字稿內容**，是依線性代數推論的精確說法：某一個理想點 $(x_1,x_2,0)$ 不動 ⟺ $(x_1,x_2)^\mathsf{T}$ 是 $A$ 的**特徵向量**。要讓 $\mathbf{l}_\infty$ 上**所有**點都不動，$A$ 必須是 $kI$。

---

## 4. 仿射校正：用消失線去除射影失真

### 4.1 想法

[▶ 15:00](https://youtu.be/T-p6d7av32Y?t=900)

- 兩組平行線各交於一個理想點 $\mathbf{x}_1$、$\mathbf{x}_2$；$\mathbf{l}_\infty$ 通過這兩點。
- 現實中，地平面的 $\mathbf{l}_\infty$ 就是**地平線（horizon）**。
- 拍成照片後（經過射影變換 $H_P$），$\mathbf{l}_\infty$ 變成影像上一條**有限的線** $\mathbf{l}$，叫**消失線（vanishing line）**；理想點變成有限點，叫**消失點（vanishing point）**（講者說之後的課會細講）。
- **目標**：找一個射影變換 $H_P'$，把 $\mathbf{l}$ 送回 $\mathbf{l}_\infty=(0,0,1)^\mathsf{T}$，消失點送回無窮遠。

**為什麼這樣就只剩仿射失真** [▶ 19:27](https://youtu.be/T-p6d7av32Y?t=1167)：

- 從原始場景到校正後的影像，整體變換是 $H_P'H_P$。
- 它把 $\mathbf{l}_\infty$ 送到 $\mathbf{l}_\infty$、平行線保持平行 → 由 Result 2.17，**它是仿射變換** $H_A$。
- 所以 $H_P'$ **去除了射影失真**，只剩**仿射失真**。

### 4.2 求 H'_P

[▶ 21:04](https://youtu.be/T-p6d7av32Y?t=1264)

設消失線 $\mathbf{l}=(l_1,l_2,l_3)^\mathsf{T}$，$l_3\neq0$。

**第一步：解出某個 $H_P$**。由 $\mathbf{l}=H_P^{-\mathsf{T}}\mathbf{l}_\infty$，移項得

$$
H_P^\mathsf{T}\mathbf{l}=\mathbf{l}_\infty=\begin{pmatrix}0\\0\\1\end{pmatrix}
$$

一個觀察得到的解 [▶ 23:14](https://youtu.be/T-p6d7av32Y?t=1394)：

$$
H_P^\mathsf{T}=\begin{pmatrix} 1 & 0 & -l_1/l_3\\ 0 & 1 & -l_2/l_3\\ 0 & 0 & 1/l_3\end{pmatrix}
$$

逐列驗證：

- 第一列：$1\cdot l_1+0\cdot l_2-\frac{l_1}{l_3}l_3=0$ ✓
- 第二列：$0+l_2-\frac{l_2}{l_3}l_3=0$ ✓
- 第三列：$0+0+\frac{1}{l_3}l_3=1$ ✓

（矩陣元素是依講者逐列驗證的口述「$l_1+0-l_1$」「$0+l_2-l_2$」「$0+0+1$」重建的。）

**第二步：組出 $H_P'$** [▶ 24:04](https://youtu.be/T-p6d7av32Y?t=1444)：

$$
H_A=H_P'H_P\quad\Longrightarrow\quad H_P'=H_AH_P^{-1}
$$

- $H_A$ 可以是**任意**仿射變換（$A$、$\mathbf{t}$ 隨便選），因為仿射變換本來就把 $\mathbf{l}_\infty$ 送回自己。

> 以下**不是逐字稿內容**，是依上面的 $H_P^\mathsf{T}$ 推論的 $H_P^{-1}$：
> $$H_P=\begin{pmatrix}1&0&0\\0&1&0\\-l_1/l_3&-l_2/l_3&1/l_3\end{pmatrix},\qquad H_P^{-1}=\begin{pmatrix}1&0&0\\0&1&0\\l_1&l_2&l_3\end{pmatrix}$$
> （驗證 $H_P H_P^{-1}$ 的第三列：$\left(-\frac{l_1}{l_3}+\frac{l_1}{l_3},\ -\frac{l_2}{l_3}+\frac{l_2}{l_3},\ \frac{l_3}{l_3}\right)=(0,0,1)$。）所以
> $$H_P'=H_A\begin{pmatrix}1&0&0\\0&1&0\\l_1&l_2&l_3\end{pmatrix}$$
> 這正是 MVG 式 (2.19)。檢查：$H_P'^{-\mathsf{T}}\mathbf{l}=\mathbf{l}_\infty$ ⟺ $H_P'^{\mathsf{T}}\mathbf{l}_\infty\propto\mathbf{l}$；$\begin{pmatrix}1&0&0\\0&1&0\\l_1&l_2&l_3\end{pmatrix}^\mathsf{T}(0,0,1)^\mathsf{T}=(l_1,l_2,l_3)^\mathsf{T}$ ✓。

**直覺**：$H_P'$ 的最後一列就是消失線 $\mathbf{l}^\mathsf{T}$。點 $\mathbf{x}$ 變換後的第三個分量是 $\mathbf{l}^\mathsf{T}\mathbf{x}$——在消失線上的點，第三個分量變成 0，被送到無窮遠。

【課本補充】MVG §2.7.2：這只需要指定一條線（2 個自由度），等於只決定了第 02 集分解鏈 $H_SH_AH_P$ 裡的射影部分。

### 4.3 演算法

[▶ 27:28](https://youtu.be/T-p6d7av32Y?t=1648)

**在解什麼**：一張平面（例如地板、牆面）的照片有射影失真（平行線會相交）。想讓平行線恢復平行。

**步驟**：

1. 在影像上找**兩組**在場景中平行的線。在影像上它們不再平行。
2. 每組延長後交於一個有限點：消失點 $\mathbf{v}_1$、$\mathbf{v}_2$（每個用兩線外積求）。
3. 消失線 $\mathbf{l}=\mathbf{v}_1\times\mathbf{v}_2=(l_1,l_2,l_3)^\mathsf{T}$。
4. 組出 $H_P'=H_A\begin{pmatrix}1&0&0\\0&1&0\\l_1&l_2&l_3\end{pmatrix}$。
5. 用 $H_P'$ 把整張影像**射影扭轉（projective warp）**，得到**仿射校正（affine rectified）**的影像。

**結果** [▶ 30:01](https://youtu.be/T-p6d7av32Y?t=1801)：

- 平行線恢復平行（交在無窮遠）。
- 平行線段的長度比也恢復。
- **但角度還是錯的**：場景裡的正方形磁磚，校正後直角看起來不是直角——仿射失真還在。

**什麼時候會失敗**：

- 逐字稿和課本沒有直接列失敗情況。
> 以下**不是逐字稿內容**，是依公式推論的：(a) 需要 $l_3\neq0$——消失線不能通過影像原點；(b) 兩組平行線必須方向不同，否則兩個消失點重合，連不出消失線；(c) 場景必須是**一個平面**，否則一個 $H$ 不能描述整張影像（MVG Example 2.12 提到地面和牆面要各用不同的 $H$）。

### 4.4 怎麼把影像「拉過去」：反向映射

[▶ 30:20](https://youtu.be/T-p6d7av32Y?t=1820)【口頭】

- **正向映射**：原圖每個像素 $\mathbf{x}$ 算 $\mathbf{x}'=H_P'\mathbf{x}$，把顏色搬過去。
  - 問題：映射不是一對一，新影像上會出現**洞**（某些位置沒有任何原像素對過來）。
- **反向映射**（實務做法）：新影像每個位置 $\mathbf{x}'$ 算 $\mathbf{x}=H_P'^{-1}\mathbf{x}'$，到原圖查那個位置的顏色（查表），填進來。
  - 這樣新影像每個像素都有值。

---

## 5. 反過來：用已知長度比求消失點

[▶ 34:08](https://youtu.be/T-p6d7av32Y?t=2048)

前面是「知道 $\mathbf{l}_\infty$ 的像 → 恢復仿射性質」。反過來，**知道仿射性質也能求出無窮遠點和無窮遠線**。

**設定**（MVG Example 2.19）：

- 影像上一條線上有三點 $a',b',c'$，對應 3D 世界中共線的 $a,b,c$。
- 已知世界中的長度比 $d(a,b):d(b,c)=a:b$（仿射性質）。

**步驟** [▶ 37:29](https://youtu.be/T-p6d7av32Y?t=2249)：

1. 在影像上量 $a'=d(a',b')$、$b'=d(b',c')$。
2. 在世界線上建 1D 座標，以 $a$ 為原點：
$$
a\to(0,1)^\mathsf{T},\qquad b\to(a,1)^\mathsf{T},\qquad c\to(a+b,1)^\mathsf{T}
$$
   影像線上同樣：$(0,1)^\mathsf{T}$、$(a',1)^\mathsf{T}$、$(a'+b',1)^\mathsf{T}$。
3. 求 1D 射影變換 $H_{2\times2}$，使 $a\mapsto a'$、$b\mapsto b'$、$c\mapsto c'$。
4. 世界線上的無窮遠點是 $(1,0)^\mathsf{T}$。它的像
$$
\mathbf{v}=H_{2\times2}\begin{pmatrix}1\\0\end{pmatrix}
$$
   就是影像上這條線的**消失點**。

【口頭】[▶ 41:15](https://youtu.be/T-p6d7av32Y?t=2475) 講者說：每對對應點給兩條方程式，兩對點就有四條方程式，夠解 $H_{2\times2}$ 的四個未知數；細節在 Lecture 4 講 homography 估計時再說。

> 以下**不是逐字稿內容**，是依第 02 集「$H_{2\times2}$ 有 3 個自由度、3 對點決定」推論的：$H_{2\times2}$ 有 4 個元素但差一個縮放，只有 3 個自由度。用齊次座標時，每對點 $\bar{\mathbf{x}}'\sim H\bar{\mathbf{x}}$ 只給**一條**獨立方程式（$x_1'(h_{21}x_1+h_{22}x_2)=x_2'(h_{11}x_1+h_{12}x_2)$），所以需要 MVG 寫的**三對點** $a,b,c$。講者「兩對點、四條方程式、四個未知數」的算法忽略了縮放。

【課本補充】MVG §2.7.2：也可以直接用**交比**——三個已知點加上無窮遠點組成四點，交比在投影下不變，就能解出消失點的位置。

---

## 6. Circular points

### 6.1 定義：相似變換下不動的兩個點

[▶ 44:29](https://youtu.be/T-p6d7av32Y?t=2669)

- 在任何**相似變換**下，$\mathbf{l}_\infty$ 上總有**兩個點不動**。這兩點叫 **circular points**（圓環點），也叫 **absolute points**，記作 $\mathbf{I}$、$\mathbf{J}$：

$$
\mathbf{I}=\begin{pmatrix}1\\ i\\ 0\end{pmatrix},\qquad \mathbf{J}=\begin{pmatrix}1\\ -i\\ 0\end{pmatrix}
$$

- $i$ 是虛數單位。$\mathbf{I}$、$\mathbf{J}$ 是一對**共軛複數的理想點**（第三個分量都是 0）。

> **Result 2.21（MVG）** circular points $\mathbf{I},\mathbf{J}$ 在射影變換 $H$ 下不動，若且唯若 $H$ 是**相似變換**。

**驗證「若」** [▶ 46:16](https://youtu.be/T-p6d7av32Y?t=2776)：

$$
H_S\mathbf{I}=\begin{pmatrix} s\cos\theta & -s\sin\theta & t_x\\ s\sin\theta & s\cos\theta & t_y\\ 0&0&1\end{pmatrix}\begin{pmatrix}1\\ i\\ 0\end{pmatrix}=\begin{pmatrix} s(\cos\theta-i\sin\theta)\\ s(\sin\theta+i\cos\theta)\\ 0\end{pmatrix}
$$

用歐拉公式 $e^{-i\theta}=\cos\theta-i\sin\theta$：

- 第一個分量：$s e^{-i\theta}$。
- 第二個分量：$s(\sin\theta+i\cos\theta)=s\,i(\cos\theta-i\sin\theta)=s\,i\,e^{-i\theta}$。

所以

$$
H_S\mathbf{I}=s e^{-i\theta}\begin{pmatrix}1\\ i\\ 0\end{pmatrix}=se^{-i\theta}\,\mathbf{I}\ \sim\ \mathbf{I}
$$

（差一個非零的複數倍，在齊次座標下是同一點。）$\mathbf{J}$ 同理。

⚠️ 逐字稿缺字 [▶ 47:12](https://youtu.be/T-p6d7av32Y?t=2832)：講者說「$e^{i\theta}=\cos\theta-i\sin\theta$」，應為 $e^{-i\theta}=\cos\theta-i\sin\theta$（$e^{i\theta}=\cos\theta+i\sin\theta$）。講者結論寫的 $e^{-i\theta}$ 是對的。

- **反方向也成立**：若 $\mathbf{I},\mathbf{J}$ 不動，則變換是相似變換。

【課本補充】（MVG §2.7.3）

- 上面驗證的是**保持方向**的相似變換。**鏡射會把 $\mathbf{I}$ 和 $\mathbf{J}$ 對調**。
- 反方向的證明 MVG 留作練習。

### 6.2 為什麼叫 circular

[▶ 48:55](https://youtu.be/T-p6d7av32Y?t=2935)

**每個圓都和 $\mathbf{l}_\infty$ 交於 circular points**。

推導：

1. 第 02 集的二次曲線 $ax_1^2+bx_1x_2+cx_2^2+dx_1x_3+ex_2x_3+fx_3^2=0$。圓的條件是 $a=c$、$b=0$；令 $a=1$：
$$
x_1^2+x_2^2+dx_1x_3+ex_2x_3+fx_3^2=0
$$
2. 和 $\mathbf{l}_\infty$ 的交點滿足 $x_3=0$，含 $x_3$ 的三項都消失：
$$
x_1^2+x_2^2=0
$$
3. 因式分解：$(x_1+ix_2)(x_1-ix_2)=0$ → $x_2=\pm i\,x_1$ → 交點是 $(1,i,0)^\mathsf{T}=\mathbf{I}$ 和 $(1,-i,0)^\mathsf{T}=\mathbf{J}$。

（圓的條件 $a=c$、$b=0$ 依 MVG 補上；講者只說「代進二次曲線方程式，這三項變成 0」。）

**直覺**：圓之所以是圓，是因為它在 $x$、$y$ 兩個方向「一視同仁」。$\mathbf{I}=(1,0,0)^\mathsf{T}+i(0,1,0)^\mathsf{T}$ 把兩個垂直方向打包成一個複數點。保住 $\mathbf{I},\mathbf{J}$ 就是保住「垂直」和「等長」的概念——這正是相似變換保持的東西（角度、長度比）。

【課本補充】（MVG §2.7.3）

- 歐氏幾何裡三點決定一個圓。用 circular points 可以換個算法：三點加上 $\mathbf{I}$、$\mathbf{J}$ 共五點，用第 02 集「五點決定二次曲線」的公式求圓。
- 下一節會看到：找出 circular points（或它的對偶），就能恢復**相似性質**（角度、長度比）。

---

## 7. Circular points 的對偶二次曲線 C*∞

[▶ 51:02](https://youtu.be/T-p6d7av32Y?t=3062)

- circular points 是用**點**定義的（圓和 $\mathbf{l}_\infty$ 的交點）。也可以用**線**定義它的對偶，是一條對偶二次曲線：

$$
C_\infty^*=\mathbf{I}\mathbf{J}^\mathsf{T}+\mathbf{J}\mathbf{I}^\mathsf{T}
$$

- 這是第 02 集見過的形式：**退化的、rank 2 的線二次曲線**，由所有通過 $\mathbf{I}$ 或 $\mathbf{J}$ 的線組成。

**在歐氏座標系下** [▶ 52:26](https://youtu.be/T-p6d7av32Y?t=3146)：代入 $\mathbf{I},\mathbf{J}$：

$$
\mathbf{I}\mathbf{J}^\mathsf{T}=\begin{pmatrix}1\\ i\\ 0\end{pmatrix}\begin{pmatrix}1 & -i & 0\end{pmatrix}=\begin{pmatrix}1&-i&0\\ i&1&0\\0&0&0\end{pmatrix},\qquad \mathbf{J}\mathbf{I}^\mathsf{T}=\begin{pmatrix}1&i&0\\ -i&1&0\\0&0&0\end{pmatrix}
$$

$$
C_\infty^*=\begin{pmatrix}2&0&0\\0&2&0\\0&0&0\end{pmatrix}\ \sim\ \begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}
$$

- 非對角元素全為 0，對角是 $(1,1,0)$。
- circular points 是複數點，是**虛的**，在現實中看不到。

**$C_\infty^*$ 在相似變換下不動** [▶ 53:44](https://youtu.be/T-p6d7av32Y?t=3224)：用第 02 集對偶二次曲線的變換規則 $C^{*\prime}=HC^*H^\mathsf{T}$：

$$
H_SC_\infty^*H_S^\mathsf{T}=\begin{pmatrix} sR & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\begin{pmatrix} I_2 & \mathbf{0}\\ \mathbf{0}^\mathsf{T} & 0\end{pmatrix}\begin{pmatrix} sR^\mathsf{T} & \mathbf{0}\\ \mathbf{t}^\mathsf{T} & 1\end{pmatrix}=\begin{pmatrix} s^2RR^\mathsf{T} & \mathbf{0}\\ \mathbf{0}^\mathsf{T} & 0\end{pmatrix}=s^2C_\infty^*\ \sim\ C_\infty^*
$$

> 以下**不是逐字稿內容**：逐字稿只說「前後乘上相似矩陣，算回自己」，中間的分塊乘法是依定義補上的。關鍵一步：中間矩陣右下是 0，把 $\mathbf{t}$ 全部消掉；$RR^\mathsf{T}=I$。

【課本補充】MVG Result 2.22：$C_\infty^*$ 在射影變換 $H$ 下不動，若且唯若 $H$ 是相似變換。

**$C_\infty^*$ 的性質（在任何射影座標系下）** [▶ 54:52](https://youtu.be/T-p6d7av32Y?t=3292)：

1. **4 個自由度**：$3\times3$ 齊次對稱矩陣有 5 個自由度，再加上「rank 2」也就是 $\det C_\infty^*=0$ 這個約束，$5-1=4$。
2. **$\mathbf{l}_\infty$ 是 $C_\infty^*$ 的零向量** [▶ 55:46](https://youtu.be/T-p6d7av32Y?t=3346)：
$$
C_\infty^*\mathbf{l}_\infty=\mathbf{I}(\mathbf{J}^\mathsf{T}\mathbf{l}_\infty)+\mathbf{J}(\mathbf{I}^\mathsf{T}\mathbf{l}_\infty)=\mathbf{0}
$$
   因為 circular points 在 $\mathbf{l}_\infty$ 上：$\mathbf{I}^\mathsf{T}\mathbf{l}_\infty=\mathbf{J}^\mathsf{T}\mathbf{l}_\infty=0$（例如 $(1,-i,0)\cdot(0,0,1)=0$）。

（本集到 57:08 結束，下一集接著講怎麼用 $C_\infty^*$ 量角度、做度量校正。）

---

## 8. 一頁速查表

### 無窮遠線與仿射校正

| 公式 | 關鍵一步 |
|---|---|
| $\mathbf{l}_\infty$ 不動 ⟺ $H$ 仿射 | $H_A^{-\mathsf{T}}$ 最後一行是 $(\mathbf{0},1)^\mathsf{T}$ |
| 射影變換：$H_P(x_1,x_2,0)^\mathsf{T}$ 第三分量 $=v_1x_1+v_2x_2\neq0$ | 理想點變有限點 |
| 消失線 $\mathbf{l}=\mathbf{v}_1\times\mathbf{v}_2$ | 兩組平行線的消失點連線 |
| $H_P'=H_A\begin{pmatrix}1&0&0\\0&1&0\\l_1&l_2&l_3\end{pmatrix}$ | 最後一列是 $\mathbf{l}^\mathsf{T}$ → 消失線上的點送到無窮遠 |
| 影像扭轉用反向映射 $\mathbf{x}=H'^{-1}\mathbf{x}'$ | 避免洞 |
| 長度比 → 消失點：$\mathbf{v}=H_{2\times2}(1,0)^\mathsf{T}$ | $0,a,a+b$ 對應 $0,a',a'+b'$ |

### Circular points

| 公式 | 關鍵一步 |
|---|---|
| $\mathbf{I}=(1,i,0)^\mathsf{T}$，$\mathbf{J}=(1,-i,0)^\mathsf{T}$ | 圓 $x_1^2+x_2^2+\dots=0$ 與 $x_3=0$ 相交 |
| $H_S\mathbf{I}=se^{-i\theta}\mathbf{I}$ | 歐拉公式 |
| 不動 ⟺ $H$ 相似 | — |
| $C_\infty^*=\mathbf{I}\mathbf{J}^\mathsf{T}+\mathbf{J}\mathbf{I}^\mathsf{T}\sim\operatorname{diag}(1,1,0)$ | 直接代入 |
| $H_SC_\infty^*H_S^\mathsf{T}=s^2C_\infty^*$ | 右下 0 消掉 $\mathbf{t}$；$RR^\mathsf{T}=I$ |
| $C_\infty^*$：4 dof，$C_\infty^*\mathbf{l}_\infty=\mathbf{0}$ | 5 dof − $\det=0$；$\mathbf{I},\mathbf{J}$ 在 $\mathbf{l}_\infty$ 上 |

### 失真階層

射影失真 —（找 $\mathbf{l}_\infty$ 的像）→ 仿射失真 —（找 $\mathbf{I},\mathbf{J}$ 的像）→ 相似失真（去不掉）。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $C_\infty^*$ | 第 06 集（用 $C_\infty^*$ 量角度、度量校正） |
| 2D 的 $\mathbf{l}_\infty$、$\mathbf{I},\mathbf{J}$ | 第 06–07 集（3D 版：無窮遠平面 $\boldsymbol{\pi}_\infty$、絕對二次曲線 $\Omega_\infty$） |
| 消失點、消失線 | 第 13–15 集（Lecture 6：單視角量測） |
| 1D homography、交比求消失點 | 第 13–15 集（單視角量測） |
| 影像扭轉、反向映射 | 第 08–09 集（homography 估計後的拼接）；第 31–34 集（stereo 校正） |
| 估計 $H$ 需要幾對點 | 第 08 集（DLT） |

---

## 附：本集一句話總結

> **仿射變換保住 $\mathbf{l}_\infty$，相似變換保住 circular points $\mathbf{I},\mathbf{J}$；所以在照片上找出消失線，用 $H_P'$（最後一列是消失線）把它送回 $(0,0,1)$，就能去掉射影失真、只剩仿射失真——要再去掉仿射失真，得靠 circular points 和它的對偶 $C_\infty^*=\operatorname{diag}(1,1,0)$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 3 (Part 1) 錄影逐字稿（Whisper `medium.en`，57:17）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §2.7.1–2.7.3 整理。*
