---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 25
lecture: Lecture 9 (Part 3) – Three-view geometry from points and/or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/ofDScwvfSvM
notes: MVG §15.1.3–15.1.5（書頁 371–375，PDF 頁 389–393）、§15.2（書頁 376–379，PDF 頁 394–397）
---

# 第 25 集 · Lecture 9 (Part 3)：從 trifocal tensor 取出 F 和相機矩陣、張量記號 [▶ 影片](https://youtu.be/ofDScwvfSvM)

← 上一集：[24-three-view-geometry-part2](24-three-view-geometry-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[26-three-view-geometry-part4](26-three-view-geometry-part4.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 25 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（52:11，Whisper `medium.en` 轉錄）＋ MVG §15.1.3–15.1.5、§15.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Tᵢ 的代數性質](#1-tᵢ-的代數性質)
- [2. 取出 fundamental matrix](#2-取出-fundamental-matrix)
- [3. 取出相機矩陣](#3-取出相機矩陣)
  - [3.1 前兩台](#31-前兩台)
  - [3.2 陷阱：第三台不能照樣做](#32-陷阱第三台不能照樣做)
  - [3.3 正確求出第三台](#33-正確求出第三台)
  - [3.4 演算法總結](#34-演算法總結)
- [4. 張量記號](#4-張量記號)
  - [4.1 上標、下標、求和約定](#41-上標下標求和約定)
  - [4.2 Trifocal tensor 與 homography](#42-trifocal-tensor-與-homography)
  - [4.3 ε 張量](#43-ε-張量)
  - [4.4 關聯關係的張量形式](#44-關聯關係的張量形式)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| $T_i$ 的 rank、零空間、極點 | §15.1.3 |
| 從 tensor 求 $F_{21}$、$F_{31}$ | §15.1.4 |
| 從 tensor 求 $P$、$P'$、$P''$（和一個常見陷阱） | §15.1.5 |
| 張量記號 | §15.2 |

---

## 1. Tᵢ 的代數性質

[▶ 00:00](https://youtu.be/ofDScwvfSvM?t=0)

**rank 2**：$T_i=\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}$ 是**兩個外積的和** → rank 2（不滿秩）。

**右零向量 = 第三張圖的極線** [▶ 00:37](https://youtu.be/ofDScwvfSvM?t=37)：$T_i$ 的右零向量 $\mathbf{l}_i''$ 是第一張圖的點 $\mathbf{x}=\mathbf{e}_i$（$(1,0,0)$、$(0,1,0)$、$(0,0,1)$）在第三張圖的極線：

$$
\mathbf{l}_i''=\mathbf{e}''\times\mathbf{b}_i
$$

**證明** [▶ 01:38](https://youtu.be/ofDScwvfSvM?t=98)：

1. 第 16 集：第三張圖的極線 $\mathbf{l}''=[\mathbf{e}'']_\times P''P^+\mathbf{x}$。
2. $P=[I\mid\mathbf{0}]$ 的偽逆 $P^+=\begin{pmatrix}I\\\mathbf{0}^\mathsf{T}\end{pmatrix}$（滿足 $PP^+=I$）。
3. $P''P^+=[\mathbf{b}_1\ \mathbf{b}_2\ \mathbf{b}_3\ \mathbf{b}_4]\begin{pmatrix}I\\\mathbf{0}^\mathsf{T}\end{pmatrix}=[\mathbf{b}_1\ \mathbf{b}_2\ \mathbf{b}_3]$——最後一列的 0 把 $\mathbf{b}_4$ 消掉。
4. $\mathbf{x}=\mathbf{e}_i$ 像一個「**選擇器**」，挑出第 $i$ 行：$P''P^+\mathbf{e}_i=\mathbf{b}_i$。
5. 所以 $\mathbf{l}_i''=\mathbf{e}''\times\mathbf{b}_i$。∎

**極點** [▶ 04:50](https://youtu.be/ofDScwvfSvM?t=290)：三條極線 $\mathbf{l}_1'',\mathbf{l}_2'',\mathbf{l}_3''$ 交於 $\mathbf{e}''$ →
$$
\mathbf{e}''^\mathsf{T}[\mathbf{l}_1''\ \mathbf{l}_2''\ \mathbf{l}_3'']=\mathbf{0}^\mathsf{T}
$$
（$\mathbf{e}''$ 是三條極線疊成的矩陣的左零向量。）

**左零向量** [▶ 05:55](https://youtu.be/ofDScwvfSvM?t=355)：同理，$T_i$ 的左零向量是第二張圖的極線，三條交於 $\mathbf{e}'$。講者說推導照抄上面，留作練習。

**一般的 $\mathbf{x}$** [▶ 07:05](https://youtu.be/ofDScwvfSvM?t=425)：$\mathbf{e}_i$ 只是方便的特例。一般點 $\mathbf{x}$ 用
$$
M=\sum_ix^iT_i=x^1T_1+x^2T_2+x^3T_3
$$
- $M$ 也是 **rank 2**：三個 rank 2 矩陣的加權和（講者的說法）。
- $M$ 的右零向量是第三張圖的極線、左零向量是第二張圖的極線（第 24 集）。

> 以下**不是逐字稿內容**：「rank 2 矩陣的加權和還是 rank 2」一般不成立（兩個 rank 2 矩陣相加可以是 rank 3）。$M$ 是 rank 2 的真正理由是 $M=\left(\sum_ix^i\mathbf{a}_i\right)\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\left(\sum_ix^i\mathbf{b}_i\right)^\mathsf{T}=(A\mathbf{x})\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4(B\mathbf{x})^\mathsf{T}$，仍然是**兩個外積的和**。

---

## 2. 取出 fundamental matrix

[▶ 10:07](https://youtu.be/ofDScwvfSvM?t=607)

**推導**（同第 16 集的幾何推導：先轉點、再連極點）：

1. 第三張圖的線 $\mathbf{l}''$ 誘導第一 → 第二張圖的 homography（第 24 集）：$\mathbf{x}'=[T_1,T_2,T_3]\mathbf{l}''\,\mathbf{x}$。
2. 極線 = 轉過去的點和極點的連線：
$$
\mathbf{l}'=\mathbf{e}'\times\mathbf{x}'=[\mathbf{e}']_\times[T_1,T_2,T_3]\mathbf{l}''\,\mathbf{x}
$$
3. 所以
$$
F_{21}=[\mathbf{e}']_\times[T_1,T_2,T_3]\mathbf{l}''
$$
   （$[T_1,T_2,T_3]\mathbf{l}''$ 表示三行分別是 $T_1\mathbf{l}''$、$T_2\mathbf{l}''$、$T_3\mathbf{l}''$ 的矩陣。）

**選哪條 $\mathbf{l}''$** [▶ 14:27](https://youtu.be/ofDScwvfSvM?t=867)：

- 公式對**任何** $\mathbf{l}''$ 都成立。
- 但要避開**退化**：若 $\mathbf{l}''$ 落在某個 $T_i$ 的零空間（$T_i\mathbf{l}''=\mathbf{0}$），$F_{21}$ 就壞掉。$\mathbf{l}''$ 太**接近**零空間也不好——$F$ 的元素會很接近 0。
- **好選擇**：$\mathbf{l}''=\mathbf{e}''$（把極點的座標當成一條線）。它**垂直於**每個 $T_i$ 的右零向量（離退化最遠）。

**為什麼垂直** [▶ 17:43](https://youtu.be/ofDScwvfSvM?t=1063)：$T_i$ 的右零向量是極線 $\mathbf{l}_i''$，而 $\mathbf{e}''$ 在每條極線上 → $\mathbf{e}''^\mathsf{T}\mathbf{l}_i''=0$。把它看成兩個向量的內積 $=\|\mathbf{e}''\|\|\mathbf{l}_i''\|\cos\theta=0$ → $\theta=90^\circ$。

$$
\boxed{\ F_{21}=[\mathbf{e}']_\times[T_1,T_2,T_3]\mathbf{e}'',\qquad F_{31}=[\mathbf{e}'']_\times[T_1^\mathsf{T},T_2^\mathsf{T},T_3^\mathsf{T}]\mathbf{e}'\ }
$$

- $F_{31}$ 講者留作練習：角色互換、$T_i$ 取轉置。

（$F_{31}$ 的式子依 MVG 式 (15.8) 後的說明寫出。）

---

## 3. 取出相機矩陣

### 3.1 前兩台

[▶ 20:49](https://youtu.be/ofDScwvfSvM?t=1249)

- trifocal tensor 只描述**影像之間**的關係（關聯關係只牽涉 $\mathbf{l},\mathbf{l}',\mathbf{l}''$ 和 $T_i$），和 3D 物體無關 → **和 3D 射影變換無關**。
- 反過來說：從 tensor 求相機矩陣，**只能確定到差一個射影變換**。
- 所以可以把第一台固定成 $P=[I\mid\mathbf{0}]$。
- $F_{21}$ 已知，用第 17–18 集的結果（標準形式 $F=[\mathbf{a}]_\times A$ ⟹ $P'=[A\mid\mathbf{a}]$）：
$$
P'=\left[[T_1,T_2,T_3]\mathbf{e}''\ \middle|\ \mathbf{e}'\right]
$$
  （$\mathbf{a}=\mathbf{e}'$、$A=[T_1,T_2,T_3]\mathbf{e}''$。）
- $\{P,P'\}$ 的 fundamental matrix 就是 $F_{21}$（差射影模糊）。

### 3.2 陷阱：第三台不能照樣做

[▶ 24:20](https://youtu.be/ofDScwvfSvM?t=1460)

**誘惑**：既然 $F_{31}$ 也知道，就用同樣方法 $F_{31}=[\mathbf{b}_4]_\times B$ → $P''=\left[[T_1^\mathsf{T},T_2^\mathsf{T},T_3^\mathsf{T}]\mathbf{e}'\ \middle|\ \mathbf{e}''\right]$？

**這是錯的**（講者叫它 fallacy）。理由 [▶ 26:14](https://youtu.be/ofDScwvfSvM?t=1574)：

1. 選定 $P$、$P'$ 之後，用第一、二張圖的對應點**三角化**就能得到 3D 點 $\mathbf{X}$（第 19 集）。
2. 3D 點一旦固定，第三台相機就有 2D–3D 對應 $\mathbf{x}''\leftrightarrow\mathbf{X}$ → $P''$ 被**唯一決定**（第 20 集的 PnP，沒有射影模糊了）。
3. 所以 $P''$ 不能再「自由選擇」——它必須和已選的 $P'$ **相容**。照 $F_{31}$ 分解得到的 $P''$ 和 $P'$ 各自帶著自己的射影模糊，一般不相容。

- **一種做法**：三角化 + PnP。
- 但其實**不必重建 3D 點**，可以直接從 tensor 求 $P''$（下一節）。

⚠️ 逐字稿缺字：Whisper 把 fallacy 寫成 “fallen c”、“fallen sea”。

### 3.3 正確求出第三台

[▶ 29:09](https://youtu.be/ofDScwvfSvM?t=1749)

**回顧射影模糊**（第 17 集）：一般的 $P'$ 是 $\left[A+\mathbf{a}\mathbf{v}^\mathsf{T}\ \middle|\ \lambda\mathbf{a}\right]$。

- 這裡 $A=[T_1,T_2,T_3]\mathbf{e}''$、$\mathbf{a}=\mathbf{e}'$。
- 我們**選** $\mathbf{v}=\mathbf{0}$、$\lambda=1$，也就是 $\mathbf{a}_i=T_i\mathbf{e}''$（$P'$ 的第 $i$ 行）。
- 這個選擇**固定了射影世界座標系**，$P''$ 就唯一確定（差縮放）。

**推導** [▶ 32:16](https://youtu.be/ofDScwvfSvM?t=1936)：

1. 第 23 集：$T_i=\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}$，其中 $\mathbf{a}_4=\mathbf{e}'$、$\mathbf{b}_4=\mathbf{e}''$。
2. 代入 $\mathbf{a}_i=T_i\mathbf{e}''$：
$$
T_i=T_i\mathbf{e}''\mathbf{e}''^\mathsf{T}-\mathbf{e}'\mathbf{b}_i^\mathsf{T}
$$
3. 把 $\mathbf{e}'\mathbf{b}_i^\mathsf{T}$ 當主角：
$$
\mathbf{e}'\mathbf{b}_i^\mathsf{T}=T_i\mathbf{e}''\mathbf{e}''^\mathsf{T}-T_i=T_i\left(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I\right)
$$
4. 極點正規化成單位長度（$\mathbf{e}'^\mathsf{T}\mathbf{e}'=1$），兩邊左乘 $\mathbf{e}'^\mathsf{T}$ [▶ 34:39](https://youtu.be/ofDScwvfSvM?t=2079)：
$$
\mathbf{b}_i^\mathsf{T}=\mathbf{e}'^\mathsf{T}T_i\left(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I\right)\quad\Longrightarrow\quad\mathbf{b}_i=\left(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I\right)T_i^\mathsf{T}\mathbf{e}'
$$
5. 所以
$$
P''=\left[\left(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I\right)[T_1^\mathsf{T},T_2^\mathsf{T},T_3^\mathsf{T}]\mathbf{e}'\ \middle|\ \mathbf{e}''\right]
$$

- 這個 $P''$ 是**根據已選的 $P'$** 求出來的，沒有額外的射影模糊。

（第 4 步轉置後的形式依 MVG Algorithm 15.1 寫出；$(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I)$ 是對稱的，轉置不變。）

### 3.4 演算法總結

[▶ 36:17](https://youtu.be/ofDScwvfSvM?t=2177)（MVG Algorithm 15.1）

**給定**：$[T_1,T_2,T_3]$。

1. **極點**：$\mathbf{u}_i$、$\mathbf{v}_i$ 是 $T_i$ 的左、右零向量。
$$
\mathbf{e}'^\mathsf{T}[\mathbf{u}_1,\mathbf{u}_2,\mathbf{u}_3]=\mathbf{0}^\mathsf{T},\qquad\mathbf{e}''^\mathsf{T}[\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3]=\mathbf{0}^\mathsf{T}
$$
2. **Fundamental matrix**：$F_{21}=[\mathbf{e}']_\times[T_i]\mathbf{e}''$，$F_{31}=[\mathbf{e}'']_\times[T_i^\mathsf{T}]\mathbf{e}'$。
3. **相機**（極點正規化成單位長度）：$P=[I\mid\mathbf{0}]$，$P'=\left[[T_i]\mathbf{e}''\mid\mathbf{e}'\right]$，$P''=\left[(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I)[T_i^\mathsf{T}]\mathbf{e}'\mid\mathbf{e}''\right]$。

---

## 4. 張量記號

### 4.1 上標、下標、求和約定

[▶ 37:07](https://youtu.be/ofDScwvfSvM?t=2227)

$T_1,T_2,T_3$ 的寫法很笨重。改用**張量記號**：

- **點**（齊次行向量）：分量用**上標** $x^i$——**反變（contravariant）**指標。
- **線**（齊次列向量）：分量用**下標** $l_i$——**共變（covariant）**指標。
- **矩陣** $A$：$a^i_j$，上標 $i$ 是**列**、下標 $j$ 是**行**。

**求和約定（Einstein summation）** [▶ 39:13](https://youtu.be/ofDScwvfSvM?t=2353)：同一個指標同時出現在上標和下標，就表示對它**求和**，省略 $\sum$ 符號。

- 例：$\mathbf{x}'=A\mathbf{x}$ 寫成 $x'^i=a^i_jx^j$，意思是 $x'^i=\sum_ja^i_jx^j=a^i_1x^1+a^i_2x^2+a^i_3x^3$。
- 點在線上：$x^il_i=0$。

### 4.2 Trifocal tensor 與 homography

[▶ 40:57](https://youtu.be/ofDScwvfSvM?t=2457)

- trifocal tensor：$\mathcal{T}_i^{jk}$——下標 $i$ 選哪個矩陣 $T_i$；上標 $j$ 是列、$k$ 是行。即 $\mathcal{T}_i^{jk}=(T_i)_{jk}$。

**線關聯** [▶ 42:04](https://youtu.be/ofDScwvfSvM?t=2524)：

$$
l_i=l'_jl''_k\,\mathcal{T}_i^{jk}
$$

- $j$、$k$ 都上下重複 → 對 $j$、$k$ 求和。$i$ 沒有重複 → 是自由指標，結果有三個分量。
- $l'_j$ 和 $l''_k$ 沒有共同指標 → 它們之間只是純量乘法。

**Homography** [▶ 44:02](https://youtu.be/ofDScwvfSvM?t=2642)：第二張圖的線 $\mathbf{l}'$ 誘導第一 → 第三張的 homography：

$$
h^k_i=l'_j\,\mathcal{T}_i^{jk},\qquad x''^k=h^k_ix^i
$$

（講者口述「$i$ 是行、$k$ 是列」；依 $x''^k=h^k_ix^i$，上標 $k$ 是列、下標 $i$ 是行。）

### 4.3 ε 張量

[▶ 46:24](https://youtu.be/ofDScwvfSvM?t=2784)

$$
\epsilon_{rst}=\begin{cases}0 & r,s,t\ \text{有重複}\ (\text{例：}\epsilon_{112})\\ +1 & rst\ \text{是}\ 123\ \text{的偶排列}\ (\text{例：}\epsilon_{123},\ \epsilon_{312})\\ -1 & rst\ \text{是}\ 123\ \text{的奇排列}\ (\text{例：}\epsilon_{132})\end{cases}
$$

- $312$：$123\to132$（換一次）$\to312$（再換一次），共兩次 → 偶 → $+1$。
- $132$：換一次 → 奇 → $-1$。

**用途** [▶ 48:44](https://youtu.be/ofDScwvfSvM?t=2924)：

- **外積**：$\mathbf{c}=\mathbf{a}\times\mathbf{b}$，$c_i=\epsilon_{ijk}a^jb^k$。
- **反對稱矩陣**：$([\mathbf{a}]_\times)_{ik}=\epsilon_{ijk}a^j$（指標寫在下面時 $i$ 是列、$k$ 是行；寫在上面時相反）。

（外積和反對稱矩陣的指標式依 MVG §15.2 寫出；逐字稿只說「由這個式子給出」。）

> 以下**不是逐字稿內容**，是驗證一個分量：$c_1=\epsilon_{1jk}a^jb^k=\epsilon_{123}a^2b^3+\epsilon_{132}a^3b^2=a^2b^3-a^3b^2$，正是外積第一個分量。

### 4.4 關聯關係的張量形式

[▶ 50:17](https://youtu.be/ofDScwvfSvM?t=3017)

講者說用 $\epsilon$ 可以把第 24 集的關聯關係全部寫成張量形式，留作練習；並以其中一條說明怎麼讀：括號裡 $r$ 重複 → 對 $r$ 求和；再對 $i$、$j$、$k$ 求和；剩下自由指標 $s$ → 結果是一個 3 分量的零向量。

【課本補充】MVG §15.2 Table 15.3 的張量形式（叫 trilinearities，三線性關係；對應第 24 集的表）：

| 對應 | 張量形式 |
|---|---|
| 線–線–線 | $(l_r\epsilon^{ris})\,l'_jl''_k\,\mathcal{T}_i^{jk}=0^s$ |
| 點–線–線 | $x^il'_jl''_k\,\mathcal{T}_i^{jk}=0$ |
| 點–線–點 | $x^il'_j\,(x''^k\epsilon_{kqs})\,\mathcal{T}_i^{jq}=0_s$ |
| 點–點–線 | $x^i\,(x'^j\epsilon_{jpr})\,l''_k\,\mathcal{T}_i^{pk}=0_r$ |
| 點–點–點 | $x^i\,(x'^j\epsilon_{jpr})\,(x''^k\epsilon_{kqs})\,\mathcal{T}_i^{pq}=0_{rs}$ |

- 講者說明的那一條（括號裡對 $r$ 求和、剩 $s$）就是**線–線–線**。

（本集到 52:04 結束。）

---

## 5. 一頁速查表

### 從 tensor 取出幾何

| 物件 | 公式 | 關鍵一步 |
|---|---|---|
| $T_i$ | rank 2 | 兩個外積的和 |
| $T_i$ 右零向量 | 第三張極線 $\mathbf{e}''\times\mathbf{b}_i$（對應 $\mathbf{x}=\mathbf{e}_i$） | $P''P^+=[\mathbf{b}_1\mathbf{b}_2\mathbf{b}_3]$，$\mathbf{e}_i$ 選第 $i$ 行 |
| 極點 | $\mathbf{e}'^\mathsf{T}[\mathbf{u}_i]=0$，$\mathbf{e}''^\mathsf{T}[\mathbf{v}_i]=0$ | 極線交於極點 |
| $F_{21}$ | $[\mathbf{e}']_\times[T_i]\mathbf{e}''$ | $\mathbf{l}''=\mathbf{e}''$ 垂直於所有 $T_i$ 的右零向量 |
| $F_{31}$ | $[\mathbf{e}'']_\times[T_i^\mathsf{T}]\mathbf{e}'$ | 對稱 |
| $P'$ | $[[T_i]\mathbf{e}''\mid\mathbf{e}']$ | $F_{21}=[\mathbf{a}]_\times A$ |
| $P''$ | $[(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I)[T_i^\mathsf{T}]\mathbf{e}'\mid\mathbf{e}'']$ | $\mathbf{e}'\mathbf{b}_i^\mathsf{T}=T_i(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I)$，左乘 $\mathbf{e}'^\mathsf{T}$ |

**陷阱**：$P''$ 不能用 $F_{31}$ 自由分解——選定 $P'$ 就固定了射影座標系。

### 張量記號

- 點上標 $x^i$、線下標 $l_i$；上下重複指標自動求和。
- $l_i=l'_jl''_k\mathcal{T}_i^{jk}$；$h^k_i=l'_j\mathcal{T}_i^{jk}$，$x''^k=h^k_ix^i$。
- $\epsilon_{rst}$：重複 0、偶排列 +1、奇排列 −1；$c_i=\epsilon_{ijk}a^jb^k$。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 張量形式的關聯關係 | 第 26 集（每組對應給的線性方程式 $A\mathbf{t}=0$） |
| 從 tensor 取出 $\mathbf{e}',\mathbf{e}''$ | 第 26 集（代數最小化：用極點參數化 tensor，強制 18 dof） |
| $P,P',P''$ 一致的射影座標系 | 第 27–30 集（多視角 SfM 要讓所有相機在同一個座標系） |

---

## 附：本集一句話總結

> **每個 $T_i$ 是 rank 2，左右零向量分別是座標軸點在第二、三張圖的極線，三條極線的交點就是極點；有了極點，$F_{21}=[\mathbf{e}']_\times[T_i]\mathbf{e}''$、$F_{31}=[\mathbf{e}'']_\times[T_i^\mathsf{T}]\mathbf{e}'$，相機取 $P=[I\mid\mathbf{0}]$、$P'=[[T_i]\mathbf{e}''\mid\mathbf{e}']$——但 $P''$ 不能照 $F_{31}$ 自由分解，必須依已選的 $P'$ 算成 $[(\mathbf{e}''\mathbf{e}''^\mathsf{T}-I)[T_i^\mathsf{T}]\mathbf{e}'\mid\mathbf{e}'']$；最後用上下標加求和約定和 $\epsilon$ 張量，把所有關係寫得更緊湊。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 9 (Part 3) 錄影逐字稿（Whisper `medium.en`，52:11）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §15.1.3–15.1.5、§15.2 整理。*
