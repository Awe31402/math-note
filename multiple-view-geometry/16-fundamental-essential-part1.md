---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 16
lecture: Lecture 7 (Part 1) – The fundamental and essential matrices
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/eJnG1vwGJkE
notes: MVG §9.1–9.2（書頁 239–247，PDF 頁 257–265）
---

# 第 16 集 · Lecture 7 (Part 1)：極幾何與 fundamental matrix [▶ 影片](https://youtu.be/eJnG1vwGJkE)

← 上一集：[15-single-view-metrology-part3](15-single-view-metrology-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[17-fundamental-essential-part2](17-fundamental-essential-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 16 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（47:23，Whisper `medium.en` 轉錄）＋ MVG §9.1–9.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 極幾何的名詞](#1-極幾何的名詞)
  - [1.1 極線、極平面、基線、極點](#11-極線極平面基線極點)
  - [1.2 一參數族：極平面束、極線束](#12-一參數族極平面束極線束)
- [2. Fundamental matrix：幾何推導](#2-fundamental-matrix幾何推導)
- [3. Fundamental matrix：代數推導](#3-fundamental-matrix代數推導)
  - [3.1 F = [e']× P'P⁺](#31-f--e-pp)
  - [3.2 相機中心重合時失效](#32-相機中心重合時失效)
  - [3.3 例：校正過的雙目相機](#33-例校正過的雙目相機)
- [4. 對應條件 x'ᵀFx = 0](#4-對應條件-xᵀfx--0)
- [5. F 的性質](#5-f-的性質)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/eJnG1vwGJkE?t=0)

Lecture 7 的目標（四集合起來）：

| 目標 | 本集？ | MVG |
|---|---|---|
| 描述兩個視角之間的**極幾何（epipolar geometry）** | ✅ | §9.1 |
| fundamental matrix 的推導與性質 | ✅ | §9.2 |
| 用 8 點對應估計 fundamental／essential matrix | 第 17–18 集 | 第 11 章 |
| 從 $F$ 分解出兩個相機矩陣；從 $E$ 求 $R$、$\mathbf{t}$ | 第 17–18 集 | §9.5–9.6 |
| 線性三角化恢復 3D 結構；從未校正重建做分層重建 | 第 18–19 集 | 第 10、12 章 |

講者說內容取自 MVG 第 9、10、11 章和 Ma Yi 書第 6 章。

---

## 1. 極幾何的名詞

### 1.1 極線、極平面、基線、極點

[▶ 01:11](https://youtu.be/eJnG1vwGJkE?t=71)

兩張影像 $I$、$I'$，一個 3D 點同時被兩張看到。第一張圖上的像點是 $\mathbf{x}$。

- $\mathbf{x}$ 反投影成一條光線，3D 點可以在光線上任何地方（第 11 集）。
- 把這條光線投影到第二張圖，得到一條線 $\mathbf{l}'$，叫**極線（epipolar line）**。
- 3D 點在光線上任何地方 → 它在第二張圖的對應點 $\mathbf{x}'$ 可以在**極線上任何地方**。

| 名詞 | 定義 |
|---|---|
| **基線（baseline）** | 兩個相機中心 $C$、$C'$ 的連線 |
| **極平面（epipolar plane）** | 由反投影光線和基線張成的平面（包含基線） |
| **極點（epipole）** $\mathbf{e}$、$\mathbf{e}'$ | 基線和影像平面的交點 |

**極點的另外兩種看法** [▶ 03:28](https://youtu.be/eJnG1vwGJkE?t=208)：

1. **一個相機中心在另一個視角的像**：$\mathbf{e}$ 是 $C'$ 投影到第一張圖；$\mathbf{e}'$ 是 $C$ 投影到第二張圖。
2. **基線方向的消失點**：$\mathbf{e}$ 是從 $C$ 看基線方向的消失點；$\mathbf{e}'$ 同理。

⚠️ 逐字稿缺字：Whisper 把 epipole 寫成 “epipolar” 或 “epi-pole”。

### 1.2 一參數族：極平面束、極線束

[▶ 04:45](https://youtu.be/eJnG1vwGJkE?t=285)

- 每一對對應點都決定一個極平面。
- $C$、$C'$ 固定 → 只有一條基線 → 極點 $\mathbf{e}$、$\mathbf{e}'$ 固定。
- 所有極平面都**包含同一條基線** → 它們是**繞著基線轉的一參數族**（平面束，第 04 集）。
- 每個極平面和兩張影像各交出一條極線 $\mathbf{l}$、$\mathbf{l}'$（一對**對應極線**）。
- 所有極線都通過極點 → 極線也是**繞著極點轉的一參數族**（線束）。

---

## 2. Fundamental matrix：幾何推導

[▶ 08:17](https://youtu.be/eJnG1vwGJkE?t=497)

**目標**：找一個射影映射，把第一張圖的**點**映到第二張圖的**極線**。這個映射就是 **fundamental matrix** $F$。

**兩步** [▶ 09:06](https://youtu.be/eJnG1vwGJkE?t=546)：

1. **點 → 點**：假設 3D 點在某個平面 $\boldsymbol{\pi}$ 上。那麼 $\mathbf{x}$ 經過一個 homography 轉到第二張圖：
$$
\mathbf{x}'=H_\pi\mathbf{x}
$$
2. **點 → 線**：極線 $\mathbf{l}'$ 通過極點 $\mathbf{e}'$ 和 $\mathbf{x}'$，所以（第 01 集兩點連線）
$$
\mathbf{l}'=\mathbf{e}'\times\mathbf{x}'=\mathbf{e}'\times H_\pi\mathbf{x}=[\mathbf{e}']_\times H_\pi\mathbf{x}
$$

- $[\mathbf{a}]_\times$ 是外積的**反對稱矩陣**（第 03 集的 $\hat{\mathbf{a}}$）：$[\mathbf{a}]_\times\mathbf{b}=\mathbf{a}\times\mathbf{b}$。
$$
[\mathbf{a}]_\times=\begin{pmatrix}0&-a_3&a_2\\a_3&0&-a_1\\-a_2&a_1&0\end{pmatrix}
$$

**定義** [▶ 13:16](https://youtu.be/eJnG1vwGJkE?t=796)：

$$
\boxed{\ \mathbf{l}'=F\mathbf{x},\qquad F=[\mathbf{e}']_\times H_\pi\ }
$$

> **Result 9.1（MVG）** fundamental matrix 可以寫成 $F=[\mathbf{e}']_\times H_\pi$，$H_\pi$ 是經由任意平面 $\boldsymbol{\pi}$ 從第一張圖到第二張圖的轉移映射。

**和 homography 比較** [▶ 14:16](https://youtu.be/eJnG1vwGJkE?t=856)：

| | Homography | Fundamental matrix |
|---|---|---|
| 映射 | 點 → 點：$\mathbf{x}'=H\mathbf{x}$ | 點 → 線：$\mathbf{l}'=F\mathbf{x}$ |
| 平面 | 3D 點**必須**真的在一個平面上 | $\boldsymbol{\pi}$ 只是推導用的**虛擬平面**，3D 點不必在任何實際平面上 |

**F 是 rank 2** [▶ 16:13](https://youtu.be/eJnG1vwGJkE?t=973)：

- $[\mathbf{e}']_\times$ 是 rank 2：前兩列（含 $a_3,a_2$ 和 $a_3,a_1$）的線性組合能得到第三列，不可能滿秩。
- $H_\pi$ 是 rank 3（可逆，第 02 集）。
- rank 2 × rank 3 = rank 2 → **$F$ 是 rank 2**。

> 以下**不是逐字稿內容**，是「前兩列組合出第三列」的驗證：$a_1\cdot(\text{列 1})+a_2\cdot(\text{列 2})=(a_2a_3,\ -a_1a_3,\ -a_1a_2+a_1a_2)=-a_3\cdot(\text{列 3})$。

**幾何意義** [▶ 17:30](https://youtu.be/eJnG1vwGJkE?t=1050)：$F$ 把第一張圖（2D 射影平面 $\mathbb{P}^2$）映到第二張圖的**極線束**（1D 射影空間 $\mathbb{P}^1$）——$\mathbf{x}'$ 只能在一條線上動，是一維的。

---

## 3. Fundamental matrix：代數推導

### 3.1 F = [e']× P'P⁺

[▶ 18:39](https://youtu.be/eJnG1vwGJkE?t=1119)

兩個相機矩陣 $P$、$P'$。

1. **反投影光線**（第 11 集）：$\mathbf{X}(\lambda)=P^+\mathbf{x}+\lambda\mathbf{C}$，$P^+$ 是偽逆、$\mathbf{C}$ 是第一個相機中心。
2. **取光線上兩點** [▶ 20:10](https://youtu.be/eJnG1vwGJkE?t=1210)：
   - $\lambda=0$：$P^+\mathbf{x}$。
   - $\lambda\to\infty$：$\mathbf{C}$。
3. **投影到第二張圖**：
   - $P'P^+\mathbf{x}$；
   - $P'\mathbf{C}$——這就是極點 $\mathbf{e}'$（第一個相機中心在第二張圖的像）。
4. **極線**通過這兩點 [▶ 22:33](https://youtu.be/eJnG1vwGJkE?t=1353)：
$$
\mathbf{l}'=(P'\mathbf{C})\times(P'P^+\mathbf{x})=[\mathbf{e}']_\times P'P^+\mathbf{x}
$$

$$
\boxed{\ F=[\mathbf{e}']_\times P'P^+,\qquad \mathbf{e}'=P'\mathbf{C}\ }
$$

- **檢查尺寸** [▶ 24:12](https://youtu.be/eJnG1vwGJkE?t=1452)：$[\mathbf{e}']_\times$ $3\times3$、$P'$ $3\times4$、$P^+$ $4\times3$ → $3\times3$ ✓。
- **和幾何推導一致**：$H_\pi=P'P^+$。這個 homography 只由兩個相機矩陣決定——3D 點不需要在實際的平面上，再次說明它是虛擬的。

### 3.2 相機中心重合時失效

[▶ 25:53](https://youtu.be/eJnG1vwGJkE?t=1553)

- 若 $C=C'$：$\mathbf{e}'=P'\mathbf{C}=P'\mathbf{C}'=\mathbf{0}$（相機中心在自己的零空間裡）。
- $[\mathbf{0}]_\times=0$ → $F=0$，推導**失效**。
- （第 13 集：相機中心不動時，兩張圖只差一個 homography，沒有極幾何。）

### 3.3 例：校正過的雙目相機

[▶ 27:29](https://youtu.be/eJnG1vwGJkE?t=1649)

**設定**：**校正過的雙目相機（calibrated stereo rig）**——兩台相機固定在一個剛體上，內參 $K$、$K'$ 已知。世界座標系設在第一台相機：

$$
P=K[I\mid\mathbf{0}],\qquad P'=K'[R\mid\mathbf{t}]
$$

**算各項** [▶ 28:50](https://youtu.be/eJnG1vwGJkE?t=1730)：

- 偽逆（解 $PP^+=I$）：$P^+=\begin{pmatrix}K^{-1}\\\mathbf{0}^\mathsf{T}\end{pmatrix}$（$4\times3$）。
- 第一個相機中心：$\mathbf{C}=(0,0,0,1)^\mathsf{T}$（世界座標系和相機座標系對齊）。

代入 $F=[P'\mathbf{C}]_\times P'P^+$：

$$
F=[K'\mathbf{t}]_\times K'RK^{-1}=K'^{-\mathsf{T}}[\mathbf{t}]_\times RK^{-1}=K'^{-\mathsf{T}}RK^\mathsf{T}[KR^\mathsf{T}\mathbf{t}]_\times
$$

（各種等價形式依 MVG 式 (9.2) 寫出；逐字稿只說「化簡後 $F$ 由內參 $K,K'$ 和外參 $R,\mathbf{t}$ 表示」。）

> 以下**不是逐字稿內容**，是第一個等號的關鍵一步：$P'\mathbf{C}=K'[R\mid\mathbf{t}](0,0,0,1)^\mathsf{T}=K'\mathbf{t}$；$P'P^+=K'[R\mid\mathbf{t}]\begin{pmatrix}K^{-1}\\\mathbf{0}^\mathsf{T}\end{pmatrix}=K'RK^{-1}$。後面的等號用到 MVG Result A4.3：$[M\mathbf{a}]_\times\propto M^{-\mathsf{T}}[\mathbf{a}]_\times M^{-1}$。

**極點** [▶ 30:24](https://youtu.be/eJnG1vwGJkE?t=1824)：

- $P'=K'[R\mid\mathbf{t}]=K'R[I\mid-\tilde{\mathbf{C}}']$ → $\mathbf{t}=-R\tilde{\mathbf{C}}'$ → 第二個相機中心 $\tilde{\mathbf{C}}'=-R^\mathsf{T}\mathbf{t}$。
- 第一張圖的極點 = 第二個相機中心的像：
$$
\mathbf{e}=P\begin{pmatrix}-R^\mathsf{T}\mathbf{t}\\1\end{pmatrix}=K[I\mid\mathbf{0}]\begin{pmatrix}-R^\mathsf{T}\mathbf{t}\\1\end{pmatrix}=-KR^\mathsf{T}\mathbf{t}\ \sim\ KR^\mathsf{T}\mathbf{t}
$$
- 第二張圖的極點 = 第一個相機中心的像：
$$
\mathbf{e}'=P'\begin{pmatrix}\mathbf{0}\\1\end{pmatrix}=K'\mathbf{t}
$$

所以上面的 $F$ 也可以寫成 [▶ 32:54](https://youtu.be/eJnG1vwGJkE?t=1974)：

$$
F=[\mathbf{e}']_\times K'RK^{-1}=K'^{-\mathsf{T}}RK^\mathsf{T}[\mathbf{e}]_\times
$$

---

## 4. 對應條件 x'ᵀFx = 0

[▶ 33:37](https://youtu.be/eJnG1vwGJkE?t=2017)

- 前面是「已知 $\mathbf{x}$，求第二張圖的極線」。
- 反過來：已知一對**對應點** $\mathbf{x}\leftrightarrow\mathbf{x}'$，它們之間有什麼關係？

> **Result 9.3（MVG）** 對任一對對應點 $\mathbf{x}\leftrightarrow\mathbf{x}'$：
> $$\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$$

**證明** [▶ 35:11](https://youtu.be/eJnG1vwGJkE?t=2111)：

1. $\mathbf{x}'$ 在極線 $\mathbf{l}'=F\mathbf{x}$ 上。
2. 點在線上：$\mathbf{x}'^\mathsf{T}\mathbf{l}'=0$。
3. 代入：$\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$。∎

**為什麼重要** [▶ 36:12](https://youtu.be/eJnG1vwGJkE?t=2172)：

- **只用對應點就能算出 $F$**——不需要知道 3D 場景，也不需要知道相機位姿。
- 類比 homography：4 對對應點就能求 $H$。但 $F$ 是把點送到**包含對應點的極線**，不是送到對應點本身。
- 需要幾對點，之後講（第 17 集）。

【課本補充】MVG Definition 9.4：兩個相機中心不重合時，$F$ 是**唯一**滿足「對所有對應點 $\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$」的 $3\times3$、rank 2 齊次矩陣。

---

## 5. F 的性質

[▶ 37:52](https://youtu.be/eJnG1vwGJkE?t=2272)

**(i) 轉置** [▶ 38:05](https://youtu.be/eJnG1vwGJkE?t=2285)：$F$ 是相機對 $(P,P')$ 的 fundamental matrix，則 **$F^\mathsf{T}$ 是 $(P',P)$（順序對調）的**。

- 理由：$\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$ 整個轉置 → $\mathbf{x}^\mathsf{T}F^\mathsf{T}\mathbf{x}'=0$——現在第一個是 $\mathbf{x}$、矩陣是 $F^\mathsf{T}$。

**(ii) 極線** [▶ 40:18](https://youtu.be/eJnG1vwGJkE?t=2418)：

- 第一張圖的點 $\mathbf{x}$ → 第二張圖的極線 $\mathbf{l}'=F\mathbf{x}$。
- 第二張圖的點 $\mathbf{x}'$ → 第一張圖的極線 $\mathbf{l}=F^\mathsf{T}\mathbf{x}'$。
- 兩個都是關聯關係：$\mathbf{x}'^\mathsf{T}(F\mathbf{x})=0$（$\mathbf{x}'$ 在 $\mathbf{l}'$ 上）、$\mathbf{x}^\mathsf{T}(F^\mathsf{T}\mathbf{x}')=0$（$\mathbf{x}$ 在 $\mathbf{l}$ 上）。

⚠️ 逐字稿缺字 [▶ 41:06](https://youtu.be/eJnG1vwGJkE?t=2466)：講者說 $\mathbf{x}'$ 轉到第一張圖得「$\mathbf{l}'$」，應為 $\mathbf{l}$。

**(iii) 極點是零空間** [▶ 42:27](https://youtu.be/eJnG1vwGJkE?t=2547)：

1. 對任何點 $\mathbf{x}$（不是 $\mathbf{e}$），極線 $\mathbf{l}'=F\mathbf{x}$ 都通過 $\mathbf{e}'$：$\mathbf{e}'^\mathsf{T}(F\mathbf{x})=0$。
2. 也就是 $(\mathbf{e}'^\mathsf{T}F)\mathbf{x}=0$ 對所有 $\mathbf{x}$ 成立。
3. 所以 $\mathbf{e}'^\mathsf{T}F=\mathbf{0}^\mathsf{T}$——**$\mathbf{e}'$ 是 $F$ 的左零空間**。
4. 同理 $F\mathbf{e}=\mathbf{0}$——**$\mathbf{e}$ 是 $F$ 的右零空間**。

**(iv) 7 個自由度** [▶ 44:39](https://youtu.be/eJnG1vwGJkE?t=2679)：9 個元素，減 1（縮放，只有 8 個獨立比值），再減 1（rank 2 → $\det F=0$）= **7**。

**(v) 不是可逆的對應（not a proper correlation）** [▶ 45:23](https://youtu.be/eJnG1vwGJkE?t=2723)：

- 把點映到線的射影映射叫**對射（correlation）**。
- $F$ 雖然是 $3\times3$ 方陣，但 $\det F=0$、不可逆——映射只有一個方向，**沒有 $F^{-1}$**。

【課本補充】MVG §9.2.4：不可逆的幾何理由是，同一條極線 $\mathbf{l}$ 上的所有點都映到同一條 $\mathbf{l}'$——知道 $\mathbf{l}'$ 只能確定 $\mathbf{x}$ 在 $\mathbf{l}$ 上，不能確定是哪一點。

**唯一性** [▶ 46:47](https://youtu.be/eJnG1vwGJkE?t=2807)：從 $F=[\mathbf{e}']_\times P'P^+$ 看，**給定 $P$、$P'$，$F$ 是唯一的**。（反過來不成立，見第 17 集。）

**總表**（MVG Table 9.1）：

| 性質 | 公式 |
|---|---|
| 秩、自由度 | rank 2，7 dof |
| 對應條件 | $\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$ |
| 極線 | $\mathbf{l}'=F\mathbf{x}$，$\mathbf{l}=F^\mathsf{T}\mathbf{x}'$ |
| 極點 | $F\mathbf{e}=\mathbf{0}$，$F^\mathsf{T}\mathbf{e}'=\mathbf{0}$ |
| 一般相機 | $F=[\mathbf{e}']_\times P'P^+$，$\mathbf{e}'=P'\mathbf{C}$ |
| $P=K[I\mid\mathbf{0}]$、$P'=K'[R\mid\mathbf{t}]$ | $F=K'^{-\mathsf{T}}[\mathbf{t}]_\times RK^{-1}$ |

---

## 6. 一頁速查表

### 名詞

基線 $CC'$；極點 $\mathbf{e}=PC'$、$\mathbf{e}'=P'C$（= 基線方向的消失點）；極平面（含基線，一參數族）；極線（通過極點，一參數族）。

### Fundamental matrix

| 推導 | 結果 | 關鍵一步 |
|---|---|---|
| 幾何 | $F=[\mathbf{e}']_\times H_\pi$ | $\mathbf{l}'=\mathbf{e}'\times H_\pi\mathbf{x}$；$\boldsymbol{\pi}$ 是虛擬平面 |
| 代數 | $F=[\mathbf{e}']_\times P'P^+$ | 光線上兩點 $P^+\mathbf{x}$、$\mathbf{C}$ 投影到第二張圖再連線 |
| 雙目 | $F=[K'\mathbf{t}]_\times K'RK^{-1}=K'^{-\mathsf{T}}[\mathbf{t}]_\times RK^{-1}$ | $P^+=(K^{-1};\mathbf{0}^\mathsf{T})$，$\mathbf{C}=(0,0,0,1)^\mathsf{T}$ |

- $C=C'$ 時 $\mathbf{e}'=0$ → $F=0$。
- rank 2：rank$([\mathbf{e}']_\times)=2$ × rank$(H)=3$。

### 性質

$\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$；$(P',P)$ 的是 $F^\mathsf{T}$；$\mathbf{l}'=F\mathbf{x}$、$\mathbf{l}=F^\mathsf{T}\mathbf{x}'$；$F\mathbf{e}=0$、$\mathbf{e}'^\mathsf{T}F=0$；7 dof；不可逆。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$ | 第 17–18 集（8 點法、7 點法估計 $F$） |
| $F=K'^{-\mathsf{T}}[\mathbf{t}]_\times RK^{-1}$ | 第 17–18 集（essential matrix $E=[\mathbf{t}]_\times R$） |
| 給 $P,P'$ → $F$ 唯一 | 第 17 集（反過來：給 $F$，$P,P'$ 只確定到射影模糊） |
| 極點是零空間 | 第 17 集（標準相機對 $P'=[[\mathbf{e}']_\times F\mid\mathbf{e}']$） |
| 極線 | 第 31–34 集（stereo 沿極線搜尋對應）；第 23–26 集（三視角） |

---

## 附：本集一句話總結

> **兩個相機中心連成基線，所有極平面繞基線轉、所有極線繞極點轉；第一張圖的點經任意（虛擬）平面的 homography 轉過去再和極點連線，就得到極線 $\mathbf{l}'=F\mathbf{x}$，$F=[\mathbf{e}']_\times H_\pi=[\mathbf{e}']_\times P'P^+$；它是 rank 2、7 個自由度、不可逆的 $3\times3$ 矩陣，兩極點是它的左右零空間，而最重要的是對應點滿足 $\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$——只靠對應點就能求出 $F$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 7 (Part 1) 錄影逐字稿（Whisper `medium.en`，47:23）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §9.1–9.2 整理。*
