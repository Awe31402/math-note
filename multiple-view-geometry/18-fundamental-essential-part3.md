---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 18
lecture: Lecture 7 (Part 3) – The fundamental and essential matrices
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/7QYq7qNkmtg
notes: MVG §9.5.2–9.6（書頁 254–259，PDF 頁 272–277）、§11.1–11.2（書頁 279–282，PDF 頁 297–300）
---

# 第 18 集 · Lecture 7 (Part 3)：從 F 求相機、essential matrix、分解 E、8 點法 [▶ 影片](https://youtu.be/7QYq7qNkmtg)

← 上一集：[17-fundamental-essential-part2](17-fundamental-essential-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[19-fundamental-essential-part4](19-fundamental-essential-part4.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 18 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（48:42，Whisper `medium.en` 轉錄）＋ MVG §9.5–9.6、§11.1–11.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 引理與定理的證明](#1-引理與定理的證明)
  - [1.1 引理 9.11](#11-引理-911)
  - [1.2 定理 9.10：相機只差一個 H](#12-定理-910相機只差一個-h)
- [2. 從 F 求一組相機](#2-從-f-求一組相機)
- [3. Essential matrix](#3-essential-matrix)
  - [3.1 正規化座標與定義](#31-正規化座標與定義)
  - [3.2 E = [t]× R](#32-e--t-r)
  - [3.3 性質：5 自由度、兩個奇異值相等](#33-性質5-自由度兩個奇異值相等)
- [4. 從 E 分解出 R 和 t](#4-從-e-分解出-r-和-t)
  - [4.1 用 SVD 和 W、Z](#41-用-svd-和-wz)
  - [4.2 四組解，挑點在兩相機前方的](#42-四組解挑點在兩相機前方的)
- [5. 8 點法求 F](#5-8-點法求-f)
  - [5.1 每對點一條線性方程式](#51-每對點一條線性方程式)
  - [5.2 強制 rank 2](#52-強制-rank-2)
  - [5.3 正規化 8 點法](#53-正規化-8-點法)
- [6. 8 點法求 E](#6-8-點法求-e)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 證明「同一個 $F$ 的相機只差一個 $4\times4$ 射影變換」 | §9.5.2 |
| 從 $F$ 寫出一組標準相機 | §9.5.3 |
| essential matrix 的定義、性質、分解成 $R,\mathbf{t}$ | §9.6 |
| 正規化 8 點法估計 $F$、$E$，強制 rank 2 | §11.1–11.2 |

---

## 1. 引理與定理的證明

### 1.1 引理 9.11

[▶ 00:00](https://youtu.be/7QYq7qNkmtg?t=0)

**敘述**（上一集）：$F=[\mathbf{a}]_\times A=[\tilde{\mathbf{a}}]_\times\tilde{A}$（rank 2）⟹ $\tilde{\mathbf{a}}=k\mathbf{a}$，$\tilde{A}=k^{-1}(A+\mathbf{a}\mathbf{v}^\mathsf{T})$。

**證明**：

1. **$\tilde{\mathbf{a}}$ 和 $\mathbf{a}$ 平行**：向量和自己的外積是 0：$\mathbf{a}^\mathsf{T}[\mathbf{a}]_\times=-([\mathbf{a}]_\times\mathbf{a})^\mathsf{T}=-(\mathbf{a}\times\mathbf{a})^\mathsf{T}=\mathbf{0}^\mathsf{T}$（用 $[\mathbf{a}]_\times^\mathsf{T}=-[\mathbf{a}]_\times$），所以
$$
\mathbf{a}^\mathsf{T}F=\mathbf{a}^\mathsf{T}[\mathbf{a}]_\times A=\mathbf{0}^\mathsf{T}
$$
   $\mathbf{a}$ 在 $F$ 的**左零空間**。同理 $\tilde{\mathbf{a}}^\mathsf{T}F=\mathbf{0}^\mathsf{T}$。$F$ 是 rank 2，左零空間是 1 維 → $\tilde{\mathbf{a}}=k\mathbf{a}$（$k\neq0$）。
2. **代回** [▶ 01:57](https://youtu.be/7QYq7qNkmtg?t=117)：
$$
[\mathbf{a}]_\times A=[k\mathbf{a}]_\times\tilde{A}=[\mathbf{a}]_\times(k\tilde{A})\quad\Longrightarrow\quad[\mathbf{a}]_\times(k\tilde{A}-A)=0
$$
3. **什麼矩陣被 $[\mathbf{a}]_\times$ 消成 0** [▶ 02:59](https://youtu.be/7QYq7qNkmtg?t=179)：$[\mathbf{a}]_\times M=0$ 表示 $M$ 的每一行 $\mathbf{m}_j$ 都滿足 $\mathbf{a}\times\mathbf{m}_j=\mathbf{0}$，即每一行都**平行於 $\mathbf{a}$**。所以 $M=\mathbf{a}\mathbf{v}^\mathsf{T}$（某個 $\mathbf{v}$）：
$$
k\tilde{A}-A=\mathbf{a}\mathbf{v}^\mathsf{T}\quad\Longrightarrow\quad\tilde{A}=k^{-1}(A+\mathbf{a}\mathbf{v}^\mathsf{T})\qquad\blacksquare
$$

（第 3 步「每一行平行於 $\mathbf{a}$」是補上的說明；講者說「向量和自己的外積是 0，所以可以寫成 $\mathbf{a}$ 乘任意 $\mathbf{v}^\mathsf{T}$」。）

### 1.2 定理 9.10：相機只差一個 H

[▶ 04:04](https://youtu.be/7QYq7qNkmtg?t=244)

兩組標準相機 $P=\tilde{P}=[I\mid\mathbf{0}]$、$P'=[A\mid\mathbf{a}]$、$\tilde{P}'=[\tilde{A}\mid\tilde{\mathbf{a}}]$ 給同一個 $F$。由引理：

$$
\tilde{P}'=\left[k^{-1}(A+\mathbf{a}\mathbf{v}^\mathsf{T})\ \middle|\ k\mathbf{a}\right]
$$

取 [▶ 05:51](https://youtu.be/7QYq7qNkmtg?t=351)

$$
H=\begin{pmatrix}k^{-1}I & \mathbf{0}\\ k^{-1}\mathbf{v}^\mathsf{T} & k\end{pmatrix}
$$

（$k$ 和 $\mathbf{v}$ 共 4 個自由度。）驗證：

- $PH=[I\mid\mathbf{0}]H=[k^{-1}I\mid\mathbf{0}]=k^{-1}\tilde{P}$ ✓（差縮放）
- $P'H=[A\mid\mathbf{a}]H=\left[k^{-1}A+k^{-1}\mathbf{a}\mathbf{v}^\mathsf{T}\ \middle|\ k\mathbf{a}\right]=\tilde{P}'$ ✓（講者留作練習）

所以兩組相機只差一個 $4\times4$ 非奇異的 $H$。∎

（$H$ 的矩陣和 $P'H$ 的乘開依 MVG Theorem 9.10 的證明補上；逐字稿只說「由這個形式的 $4\times4$ 矩陣相關」。）

---

## 2. 從 F 求一組相機

[▶ 08:19](https://youtu.be/7QYq7qNkmtg?t=499)

**判別條件**：

> **Result 9.12（MVG）** 非零矩陣 $F$ 是相機對 $(P,P')$ 的 fundamental matrix，若且唯若 $P'^\mathsf{T}FP$ 是**反對稱**的。

**理由** [▶ 09:20](https://youtu.be/7QYq7qNkmtg?t=560)：對所有 3D 點 $\mathbf{X}$，

$$
\mathbf{x}'^\mathsf{T}F\mathbf{x}=(P'\mathbf{X})^\mathsf{T}F(P\mathbf{X})=\mathbf{X}^\mathsf{T}(P'^\mathsf{T}FP)\mathbf{X}=0
$$

一個矩陣 $S$ 讓 $\mathbf{X}^\mathsf{T}S\mathbf{X}=0$ 對所有 $\mathbf{X}$ 成立，若且唯若 $S$ 反對稱。

**一組具體的解** [▶ 10:36](https://youtu.be/7QYq7qNkmtg?t=636)：

> **Result 9.14（MVG）**
> $$P=[I\mid\mathbf{0}],\qquad P'=\left[[\mathbf{e}']_\times F\ \middle|\ \mathbf{e}'\right]$$
> $\mathbf{e}'$ 是 $F$ 的左零向量（第二張圖的極點）。

⚠️ 逐字稿缺字 [▶ 11:10](https://youtu.be/7QYq7qNkmtg?t=670)：講者說最後一行是「第一個視角的極點」，應為**第二個視角**的極點 $\mathbf{e}'$（$\mathbf{e}'^\mathsf{T}F=0$）。

**驗證** [▶ 11:24](https://youtu.be/7QYq7qNkmtg?t=684)：令 $S=[\mathbf{e}']_\times$，

$$
P'^\mathsf{T}FP=\begin{pmatrix}(SF)^\mathsf{T}\\\mathbf{e}'^\mathsf{T}\end{pmatrix}F[I\mid\mathbf{0}]=\begin{pmatrix}F^\mathsf{T}S^\mathsf{T}F & \mathbf{0}\\\mathbf{e}'^\mathsf{T}F & 0\end{pmatrix}=\begin{pmatrix}F^\mathsf{T}S^\mathsf{T}F & \mathbf{0}\\\mathbf{0}^\mathsf{T} & 0\end{pmatrix}
$$

- $\mathbf{e}'^\mathsf{T}F=\mathbf{0}^\mathsf{T}$（左零空間）。
- $F^\mathsf{T}S^\mathsf{T}F$ 是反對稱的（$S$ 反對稱 → $M^\mathsf{T}SM$ 也反對稱）。
- 所以 $P'^\mathsf{T}FP$ 反對稱 → 這組相機合法。∎

> 以下**不是逐字稿內容**，是「$M^\mathsf{T}SM$ 反對稱」的一行驗證：$(M^\mathsf{T}SM)^\mathsf{T}=M^\mathsf{T}S^\mathsf{T}M=-M^\mathsf{T}SM$。

【課本補充】MVG Result 9.15：最一般的標準解是 $P'=\left[[\mathbf{e}']_\times F+\mathbf{e}'\mathbf{v}^\mathsf{T}\ \middle|\ \lambda\mathbf{e}'\right]$（$\mathbf{v}$ 任意 3 維向量、$\lambda$ 非零常數）——正好 4 個自由度，對應定理 9.10 裡 $H$ 的 4 個自由度（15 − 11 = 4：射影變換 15 dof，標準化掉第一個相機用了 11）。

---

## 3. Essential matrix

### 3.1 正規化座標與定義

[▶ 13:20](https://youtu.be/7QYq7qNkmtg?t=800)

- 到目前為止都是**未校正**的情況（不知道 $K,K'$）。
- 知道 $K,K'$ 時，把像點換成**正規化相機座標（normalized camera coordinates）**：
$$
\hat{\mathbf{x}}=K^{-1}\mathbf{x},\qquad\hat{\mathbf{x}}'=K'^{-1}\mathbf{x}'
$$
  （第 14 集：$K^{-1}\mathbf{x}$ 就是光線方向。）
- 在正規化座標下，對應條件寫成 [▶ 14:41](https://youtu.be/7QYq7qNkmtg?t=881)：
$$
\hat{\mathbf{x}}'^\mathsf{T}E\hat{\mathbf{x}}=0
$$
- 代回原始座標：$(K'^{-1}\mathbf{x}')^\mathsf{T}E(K^{-1}\mathbf{x})=\mathbf{x}'^\mathsf{T}\underbrace{K'^{-\mathsf{T}}EK^{-1}}_{F}\mathbf{x}=0$。

$$
\boxed{\ F=K'^{-\mathsf{T}}EK^{-1},\qquad E=K'^\mathsf{T}FK\ }
$$

- $E$ 叫 **essential matrix（本質矩陣）**。

### 3.2 E = [t]× R

[▶ 17:05](https://youtu.be/7QYq7qNkmtg?t=1025)

**證明**：

1. 標準相機 $P=K[I\mid\mathbf{0}]$、$P'=K'[R\mid\mathbf{t}]$。
2. 第 16 集：$F=[\mathbf{e}']_\times P'P^+$，$P^+=\begin{pmatrix}K^{-1}\\\mathbf{0}^\mathsf{T}\end{pmatrix}$、$\mathbf{C}=(0,0,0,1)^\mathsf{T}$。
3. 代入化簡：
$$
F=[K'\mathbf{t}]_\times K'RK^{-1}=K'^{-\mathsf{T}}[\mathbf{t}]_\times RK^{-1}
$$
   （第二個等號講者留作練習。）
4. 和 $F=K'^{-\mathsf{T}}EK^{-1}$ 比較：
$$
\boxed{\ E=[\mathbf{t}]_\times R\ }
$$

> 以下**不是逐字稿內容**，是第 3 步第二個等號的關鍵一步（MVG Result A4.3）：對可逆 $M$，$[M\mathbf{t}]_\times=\det(M)\,M^{-\mathsf{T}}[\mathbf{t}]_\times M^{-1}$。取 $M=K'$：$[K'\mathbf{t}]_\times K'RK^{-1}\propto K'^{-\mathsf{T}}[\mathbf{t}]_\times K'^{-1}K'RK^{-1}=K'^{-\mathsf{T}}[\mathbf{t}]_\times RK^{-1}$。

### 3.3 性質：5 自由度、兩個奇異值相等

[▶ 19:54](https://youtu.be/7QYq7qNkmtg?t=1194)

- **5 個自由度**：$R$ 3 個 + $\mathbf{t}$ 3 個 = 6；但 $\mathbf{t}$ 只確定到**整體尺度**（尺度模糊），減 1 → 5。
- **rank 2**：第三個奇異值為 0（和 $F$ 一樣）。
- **額外約束**：**前兩個奇異值相等**：$\operatorname{SVD}(E)=U\,\mathrm{diag}(\sigma,\sigma,0)\,V^\mathsf{T}$。

【課本補充】MVG Result 9.17：$3\times3$ 矩陣是 essential matrix，若且唯若它的兩個奇異值相等、第三個為 0。

> 以下**不是逐字稿內容**，是「兩個奇異值相等」的直覺：$EE^\mathsf{T}=[\mathbf{t}]_\times RR^\mathsf{T}[\mathbf{t}]_\times^\mathsf{T}=[\mathbf{t}]_\times[\mathbf{t}]_\times^\mathsf{T}$，和 $R$ 無關。$[\mathbf{t}]_\times$ 把垂直於 $\mathbf{t}$ 的平面內的向量旋轉 $90^\circ$ 並乘 $\|\mathbf{t}\|$，所以它在那個平面上的兩個奇異值都是 $\|\mathbf{t}\|$，沿 $\mathbf{t}$ 方向是 0。

---

## 4. 從 E 分解出 R 和 t

### 4.1 用 SVD 和 W、Z

[▶ 21:21](https://youtu.be/7QYq7qNkmtg?t=1281)

**想法**：$E=[\mathbf{t}]_\times R$，把 SVD 的 $U$、$V$ 拆成兩部分：

- 找 $Z$ 使 $UZU^\mathsf{T}$ 是**反對稱**的 → 當成 $[\mathbf{t}]_\times$。
- 找 $X$ 使 $UXV^\mathsf{T}$ 是**正交**的 → 當成 $R$。
- 相乘：$(UZU^\mathsf{T})(UXV^\mathsf{T})=U(ZX)V^\mathsf{T}$（$U^\mathsf{T}U=I$）。要等於 $E=U\,\mathrm{diag}(1,1,0)V^\mathsf{T}$ → 需要 $ZX=\mathrm{diag}(1,1,0)$。

**選擇** [▶ 24:44](https://youtu.be/7QYq7qNkmtg?t=1484)：

$$
W=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},\qquad Z=\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}
$$

- $ZW=\mathrm{diag}(1,1,0)$；$ZW^\mathsf{T}=\mathrm{diag}(-1,-1,0)$。
- $E$ 只確定到縮放（包括正負號），所以兩種都可以：$X=W$ 或 $X=W^\mathsf{T}$。

（$W$、$Z$ 的元素依 MVG §9.6.2 寫出；逐字稿只說「$Z$ 等於這個矩陣、$W$ 等於這個矩陣」。）

> 以下**不是逐字稿內容**，是驗證 $ZW$：$\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}$ ✓。$Z$ 反對稱（$Z^\mathsf{T}=-Z$），$W$ 是繞 $z$ 軸 $90^\circ$ 的旋轉（正交，$\det=1$）。

> **Result 9.18（MVG）** $E=U\,\mathrm{diag}(1,1,0)V^\mathsf{T}$，則
> $$[\mathbf{t}]_\times=UZU^\mathsf{T},\qquad \mathbf{t}=\pm\mathbf{u}_3,\qquad R=UWV^\mathsf{T}\ \text{或}\ UW^\mathsf{T}V^\mathsf{T}$$

- **$\mathbf{t}$** [▶ 26:10](https://youtu.be/7QYq7qNkmtg?t=1570)：$U$ 的**第三行**（加正負號）。

> 以下**不是逐字稿內容**，是 $\mathbf{t}=\pm\mathbf{u}_3$ 的理由：$[\mathbf{t}]_\times\mathbf{t}=\mathbf{0}$，而 $UZU^\mathsf{T}\mathbf{u}_3=UZ(0,0,1)^\mathsf{T}=U\mathbf{0}=\mathbf{0}$——$\mathbf{u}_3$ 是 $[\mathbf{t}]_\times$ 的零向量，所以 $\mathbf{t}\propto\mathbf{u}_3$。

- **右手座標系** [▶ 27:28](https://youtu.be/7QYq7qNkmtg?t=1648)：求出的 $R$ 要是右手系（$\det R=+1$）。若 $\det R<0$，就令 $R\leftarrow-R$。

### 4.2 四組解，挑點在兩相機前方的

[▶ 28:14](https://youtu.be/7QYq7qNkmtg?t=1694)

$\mathbf{t}$ 有 $\pm$ 兩種、$R$ 有兩種 → **四組** $P'$：

$$
P'=[UWV^\mathsf{T}\mid+\mathbf{u}_3],\quad[UWV^\mathsf{T}\mid-\mathbf{u}_3],\quad[UW^\mathsf{T}V^\mathsf{T}\mid+\mathbf{u}_3],\quad[UW^\mathsf{T}V^\mathsf{T}\mid-\mathbf{u}_3]
$$

**幾何意義** [▶ 28:57](https://youtu.be/7QYq7qNkmtg?t=1737)：對一個重建出來的 3D 點，四種情況是：

1. 在兩台相機**前方**；
2. 在兩台相機**後方**；
3. 在第一台前方、第二台後方；
4. 在第二台前方、第一台後方。

- **只有一組物理上正確**：點在**兩台相機前方**。
- **怎麼挑** [▶ 29:37](https://youtu.be/7QYq7qNkmtg?t=1777)：每組都三角化一些點，選**最多點在兩台相機前方**的那組（第 11 集的深度正負號判斷）。

【課本補充】MVG §9.6.3：$\mathbf{t}$ 換號 = 把基線方向反過來；$R$ 從 $UWV^\mathsf{T}$ 換成 $UW^\mathsf{T}V^\mathsf{T}$ = 第二台相機繞基線轉 $180^\circ$（twisted pair）。實際上只要測**一個**點就能決定。

---

## 5. 8 點法求 F

### 5.1 每對點一條線性方程式

[▶ 29:50](https://youtu.be/7QYq7qNkmtg?t=1790)

第 16 集說過：只用對應點就能求 $F$。設 $\mathbf{x}=(x,y,1)^\mathsf{T}$、$\mathbf{x}'=(x',y',1)^\mathsf{T}$，展開 $\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$：

$$
x'xf_{11}+x'yf_{12}+x'f_{13}+y'xf_{21}+y'yf_{22}+y'f_{23}+xf_{31}+yf_{32}+f_{33}=0
$$

- 對 $F$ 的元素是**線性**的。寫成內積：
$$
\begin{pmatrix}x'x&x'y&x'&y'x&y'y&y'&x&y&1\end{pmatrix}\mathbf{f}=0
$$
  $\mathbf{f}$ 是 $F$ 逐列排成的 9 維向量。
- 每對點給 **1** 條方程式。

（展開式依 MVG 式 (11.2) 寫出；逐字稿只說「展開後得到這個式子」。）

**疊起來** [▶ 31:48](https://youtu.be/7QYq7qNkmtg?t=1908)：

- $\mathbf{f}$ 有 9 個元素、差縮放 → 至少 **8** 對點：$8\times9$ 的 $A\mathbf{f}=\mathbf{0}$。
- 多於 8 對：疊成超定的 $m\times9$ 系統，最小平方解——點越多越準（對應點有雜訊）。
- 解法同 homography（第 08 集）：$A$ 的 SVD，$\mathbf{f}$ = $V$ 的最後一行。
- 和 homography 一樣，**要做資料正規化**。

### 5.2 強制 rank 2

[▶ 33:54](https://youtu.be/7QYq7qNkmtg?t=2034)

**問題**：線性解出來的 $F$（排回 $3\times3$）因為雜訊，一般**不是 rank 2**。

**後果** [▶ 34:55](https://youtu.be/7QYq7qNkmtg?t=2095)：

- 極點是 $F$ 的零空間。$F$ 滿秩 → 零空間只有 $\mathbf{0}$ → **極點不存在**。
- 把第一張圖的點轉成第二張圖的極線，**極線不會交於同一點**。

**解法** [▶ 37:15](https://youtu.be/7QYq7qNkmtg?t=2235)：找最接近 $F$ 的 rank 2 矩陣 $F'$：

$$
\min_{F'}\ \|F-F'\|_F\quad\text{subject to}\quad\det F'=0
$$

（$\|\cdot\|_F$ 是 Frobenius 範數。）

用 SVD 一步解：

1. $F=U\,\mathrm{diag}(r,s,t)\,V^\mathsf{T}$，$r\ge s\ge t$（一般三個都非零 → rank 3）。
2. 把最小奇異值 $t$ 設為 0：
$$
F'=U\,\mathrm{diag}(r,s,0)\,V^\mathsf{T}
$$
- 這同時最小化 Frobenius 範數，且第三個奇異值為 0 → rank 2。

⚠️ 逐字稿缺字 [▶ 39:41](https://youtu.be/7QYq7qNkmtg?t=2381)：講者說「pre-multiply by $U$ and post-multiply by $U^\mathsf{T}$」，應為 $V^\mathsf{T}$。Whisper 把 Frobenius 寫成 “frominess”。

### 5.3 正規化 8 點法

[▶ 40:02](https://youtu.be/7QYq7qNkmtg?t=2402)

**在解什麼**：給 $n\ge8$ 對對應點 $\mathbf{x}_i\leftrightarrow\mathbf{x}_i'$，求 $F$ 使 $\mathbf{x}_i'^\mathsf{T}F\mathbf{x}_i=0$。

**步驟**（MVG Algorithm 11.1）：

1. **正規化**（**必要**）：兩張圖各自用 $T$、$T'$ 把點的重心移到原點、平均距離 $\sqrt{2}$（同第 08 集）：$\hat{\mathbf{x}}_i=T\mathbf{x}_i$、$\hat{\mathbf{x}}_i'=T'\mathbf{x}_i'$。
2. **線性解**：用正規化的點組 $A\mathbf{f}=\mathbf{0}$，SVD 取最小奇異值的右奇異向量，得 $\hat{F}$。
3. **強制 rank 2**：$\hat{F}'=\arg\min\|\hat{F}-\hat{F}'\|_F$ s.t. $\det\hat{F}'=0$（SVD，最小奇異值設 0）。
4. **反正規化**：
$$
F=T'^\mathsf{T}\hat{F}'T
$$

（反正規化公式依 MVG Algorithm 11.1 寫出；逐字稿只說「記得反正規化」。）

> 以下**不是逐字稿內容**，是反正規化的推導：$\hat{\mathbf{x}}'^\mathsf{T}\hat{F}\hat{\mathbf{x}}=(T'\mathbf{x}')^\mathsf{T}\hat{F}(T\mathbf{x})=\mathbf{x}'^\mathsf{T}(T'^\mathsf{T}\hat{F}T)\mathbf{x}$。注意和 homography 的 $T'^{-1}\tilde{H}T$ 不同——$F$ 是雙線性形式。

**什麼時候會失敗**：

> 以下**不是逐字稿內容**，是依線性代數推論的：(a) 所有點都在**一個平面**上（或相機純旋轉）時，對應點由 homography 連起來，$A$ 的零空間大於 1 維，$F$ 不唯一（MVG §11.9 的退化配置）；(b) 有錯誤對應時，要先用 RANSAC（第 09 集）；(c) 不做正規化，結果非常不穩。

---

## 6. 8 點法求 E

[▶ 41:53](https://youtu.be/7QYq7qNkmtg?t=2513)

**在解什麼**：$K,K'$ 已知，求 $E$ 再分解出 $R,\mathbf{t}$。

**步驟**：

1. 正規化相機座標：$\hat{\mathbf{x}}_i=K^{-1}\mathbf{x}_i$、$\hat{\mathbf{x}}_i'=K'^{-1}\mathbf{x}_i'$。
2. 用 $\hat{\mathbf{x}}_i'^\mathsf{T}E\hat{\mathbf{x}}_i=0$ 組 $A\mathbf{e}=\mathbf{0}$（$\mathbf{e}$ 這裡是 $E$ 排成的 9 維向量，不是極點）。
   - 講者說：**不需要**再做第 5.3 節的資料正規化，因為已經用 $K$ 正規化過，座標都在單位尺度附近。
3. SVD 解出 $\mathbf{e}$，排回 $E$。
4. **強制 essential matrix 的約束**（見下）。
5. 分解 $E$ 得 $R,\mathbf{t}$（第 4 節），挑點在兩相機前方的那組。
6. 第二個相機：$P'=K'[R\mid\mathbf{t}]$（第一個是 $P=K[I\mid\mathbf{0}]$）。

**強制約束** [▶ 45:23](https://youtu.be/7QYq7qNkmtg?t=2723)：不只 rank 2，**前兩個奇異值還要相等**：

$$
\min_{\hat{E}}\ \|E-\hat{E}\|_F\quad\text{subject to}\quad\det\hat{E}=0,\ \sigma_1(\hat{E})=\sigma_2(\hat{E})
$$

1. $E=U\,\mathrm{diag}(a,b,c)\,V^\mathsf{T}$（一般 $a\ge b\ge c>0$）。
2. 最小的設 0，前兩個取平均：
$$
\hat{E}=U\,\mathrm{diag}\left(\frac{a+b}{2},\frac{a+b}{2},0\right)V^\mathsf{T}
$$

> 以下**不是逐字稿內容**，是補充：反正 $E$ 只確定到縮放，分解時也可以直接用 $\mathrm{diag}(1,1,0)$（第 4 節就是這樣）。

---

## 7. 一頁速查表

### 從 F 求相機

| 公式 | 關鍵一步 |
|---|---|
| 引理：$[\mathbf{a}]_\times A=[\tilde{\mathbf{a}}]_\times\tilde{A}$ ⟹ $\tilde{\mathbf{a}}=k\mathbf{a}$，$\tilde{A}=k^{-1}(A+\mathbf{a}\mathbf{v}^\mathsf{T})$ | $\mathbf{a},\tilde{\mathbf{a}}$ 都在 $F$ 的 1 維左零空間；$[\mathbf{a}]_\times M=0$ ⟹ $M=\mathbf{a}\mathbf{v}^\mathsf{T}$ |
| 同一個 $F$ 的相機只差 $H=\begin{pmatrix}k^{-1}I&\mathbf{0}\\k^{-1}\mathbf{v}^\mathsf{T}&k\end{pmatrix}$ | — |
| $F$ 合法 ⟺ $P'^\mathsf{T}FP$ 反對稱 | $\mathbf{X}^\mathsf{T}(P'^\mathsf{T}FP)\mathbf{X}=0\ \forall\mathbf{X}$ |
| $P=[I\mid\mathbf{0}]$，$P'=[[\mathbf{e}']_\times F\mid\mathbf{e}']$ | $\mathbf{e}'^\mathsf{T}F=0$；$F^\mathsf{T}S^\mathsf{T}F$ 反對稱 |

### Essential matrix

| 公式 | 關鍵一步 |
|---|---|
| $\hat{\mathbf{x}}'^\mathsf{T}E\hat{\mathbf{x}}=0$，$\hat{\mathbf{x}}=K^{-1}\mathbf{x}$ | — |
| $F=K'^{-\mathsf{T}}EK^{-1}$ | 代回原始座標 |
| $E=[\mathbf{t}]_\times R$ | $[K'\mathbf{t}]_\times K'\propto K'^{-\mathsf{T}}[\mathbf{t}]_\times$ |
| 5 dof；$\sigma_1=\sigma_2$、$\sigma_3=0$ | 尺度模糊；$EE^\mathsf{T}=[\mathbf{t}]_\times[\mathbf{t}]_\times^\mathsf{T}$ |
| $\mathbf{t}=\pm\mathbf{u}_3$，$R=UWV^\mathsf{T}$ 或 $UW^\mathsf{T}V^\mathsf{T}$ | $ZW=\mathrm{diag}(1,1,0)$；$\det R<0$ 則取 $-R$ |
| 4 組解，選點在兩相機前方的 | 深度正負號 |

### 8 點法

| | $F$ | $E$ |
|---|---|---|
| 輸入 | 像素座標 | $K^{-1}\mathbf{x}$ |
| 每對點 | $(x'x,x'y,x',y'x,y'y,y',x,y,1)\mathbf{f}=0$ | 同形式 |
| 正規化 | 必要（$T,T'$），最後 $F=T'^\mathsf{T}\hat{F}T$ | 不需要 |
| 強制約束 | $\mathrm{diag}(r,s,0)$ | $\mathrm{diag}\left(\frac{a+b}{2},\frac{a+b}{2},0\right)$ |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 從 $F$ 求 $P,P'$（射影模糊） | 第 19 集（射影重建 → 仿射 → 度量） |
| 分解 $E$、挑前方解 | 第 19 集（三角化）；第 27–30 集（SfM 初始化） |
| 8 點法 + RANSAC | 第 19 集（7 點法、最少點數）；第 27–30 集 |
| 正規化座標 $K^{-1}\mathbf{x}$ | 第 20–22 集（PnP 用光線方向） |

---

## 附：本集一句話總結

> **同一個 $F$ 的相機對一定只差一個 $4\times4$ 射影變換，最簡單的一組是 $P=[I\mid\mathbf{0}]$、$P'=[[\mathbf{e}']_\times F\mid\mathbf{e}']$；知道內參時改用正規化座標，得到 essential matrix $E=[\mathbf{t}]_\times R=K'^\mathsf{T}FK$（5 dof，兩個奇異值相等），用 SVD 和 $W$ 分解出 $\mathbf{t}=\pm\mathbf{u}_3$、$R=UW^{(\mathsf{T})}V^\mathsf{T}$ 四組解，選讓點落在兩相機前方的那組；$F$ 和 $E$ 都能用 8 點法線性估計，但事後要把奇異值修正成 rank 2（$E$ 還要前兩個相等），估 $F$ 時一定要先正規化。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 7 (Part 3) 錄影逐字稿（Whisper `medium.en`，48:42）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §9.5–9.6、§11.1–11.2 整理。*
