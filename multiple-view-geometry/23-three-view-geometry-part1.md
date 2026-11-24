---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 23
lecture: Lecture 9 (Part 1) – Three-view geometry from points and/or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/5wBKv74MtMc
notes: MVG §15.1 開頭（書頁 365–368，PDF 頁 383–386）
---

# 第 23 集 · Lecture 9 (Part 1)：從三條對應線推導 trifocal tensor [▶ 影片](https://youtu.be/5wBKv74MtMc)

← 上一集：[22-absolute-pose-part3](22-absolute-pose-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[24-three-view-geometry-part2](24-three-view-geometry-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 23 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（39:26，Whisper `medium.en` 轉錄）＋ MVG §15.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Trifocal tensor 是什麼](#1-trifocal-tensor-是什麼)
- [2. 為什麼兩個視角的線沒有約束、三個就有](#2-為什麼兩個視角的線沒有約束三個就有)
- [3. 標準相機與極點](#3-標準相機與極點)
- [4. 三個反投影平面](#4-三個反投影平面)
- [5. M 的 rank 是 2](#5-m-的-rank-是-2)
- [6. 推導 Tᵢ = aᵢb₄ᵀ − a₄bᵢᵀ](#6-推導-tᵢ--aᵢbᵀ--abᵢᵀ)
- [7. Trifocal tensor 的定義與記號](#7-trifocal-tensor-的定義與記號)
- [8. 參考視角的選擇](#8-參考視角的選擇)
- [9. 18 個自由度](#9-18-個自由度)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/5wBKv74MtMc?t=0)

Lecture 9 的目標（四集合起來）：

| 目標 | 本集？ | MVG |
|---|---|---|
| 從三個視角的點／線對應推導 **trifocal tensor** 約束 | ✅（從線推導） | §15.1 |
| 兩個視角之間的 homography 關係（從 trifocal tensor 推出） | 第 24 集 | §15.1.1 |
| 從 trifocal tensor 取出極點、極線 | 第 24–25 集 | §15.1.3 |
| 分解成相機矩陣、fundamental matrix | 第 25 集 | §15.1.4–15.1.5 |
| 從三視角的點／線對應計算 trifocal tensor | 第 26 集 | 第 16 章 |

講者說內容取自 MVG 第 15、16 章，有興趣可以看 Ma Yi 書第 8 章。

⚠️ 逐字稿缺字：Whisper 把 Hartley 寫成 “Tuckley”、Zisserman 寫成 “Zizerman”、Ma Yi 寫成 “Mahi”。

---

## 1. Trifocal tensor 是什麼

[▶ 01:28](https://youtu.be/5wBKv74MtMc?t=88)

- 上一講：fundamental matrix 描述**兩個**視角的幾何關係。
- **trifocal tensor**：類比 $F$，描述**三個**視角的幾何關係。
- 它包含三個視角之間**所有和場景結構無關**的射影幾何關係。
- 只要知道三張圖的對應（點–點–點、線–線–線，或點線混合），就能算出 trifocal tensor，再分解成相機矩陣、fundamental matrix 等。

**推導方式** [▶ 02:44](https://youtu.be/5wBKv74MtMc?t=164)：有很多種點／線組合可以推導，最後都得到同一個關係。本集從**線–線–線**對應推導。

---

## 2. 為什麼兩個視角的線沒有約束、三個就有

[▶ 03:16](https://youtu.be/5wBKv74MtMc?t=196)

三張圖裡有三條對應線 $\mathbf{l}$、$\mathbf{l}'$、$\mathbf{l}''$。每條影像線反投影成一個平面（第 13 集）。

**兩個視角** [▶ 04:15](https://youtu.be/5wBKv74MtMc?t=255)：

- $\mathbf{l}$、$\mathbf{l}'$ 各反投影成一個平面。
- 3D 中**任兩個平面總是交於一條線** → 不管 $\mathbf{l}$、$\mathbf{l}'$ 是什麼，都有一條 3D 線和它們一致。
- 所以**兩個視角的線對應沒有提供任何約束**。

（對比：兩個視角的**點**對應有約束 $\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$。）

**三個視角** [▶ 05:05](https://youtu.be/5wBKv74MtMc?t=305)：

- 第三條線 $\mathbf{l}''$ 也反投影成平面。
- 一般來說**三個平面不會交於同一條線**（一般交於一點）。
- 但 $\mathbf{l},\mathbf{l}',\mathbf{l}''$ 是對應線 → 三個平面**必須**交於同一條 3D 線 $L$。
- 這就是一個**約束**——它就是 trifocal tensor。

---

## 3. 標準相機與極點

[▶ 05:53](https://youtu.be/5wBKv74MtMc?t=353)

三個相機用標準形式：

$$
P=[I\mid\mathbf{0}],\qquad P'=[A\mid\mathbf{a}_4],\qquad P''=[B\mid\mathbf{b}_4]
$$

- $A$、$B$：$3\times3$；$\mathbf{a}_4$、$\mathbf{b}_4$：$3\times1$（各自的第四行）。
- 第一台相機的座標系 = 世界座標系。

**$\mathbf{a}_4$、$\mathbf{b}_4$ 是極點** [▶ 07:38](https://youtu.be/5wBKv74MtMc?t=458)：第一個相機中心 $\mathbf{C}=(0,0,0,1)^\mathsf{T}$ 在第二、三張圖的像：

$$
\mathbf{e}'=P'\mathbf{C}=[A\mid\mathbf{a}_4]\begin{pmatrix}0\\0\\0\\1\end{pmatrix}=\mathbf{a}_4,\qquad\mathbf{e}''=P''\mathbf{C}=\mathbf{b}_4
$$

---

## 4. 三個反投影平面

[▶ 10:23](https://youtu.be/5wBKv74MtMc?t=623)

用 $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$（第 13 集）：

$$
\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}=\begin{pmatrix}I\\\mathbf{0}^\mathsf{T}\end{pmatrix}\mathbf{l}=\begin{pmatrix}\mathbf{l}\\0\end{pmatrix},\qquad
\boldsymbol{\pi}'=P'^\mathsf{T}\mathbf{l}'=\begin{pmatrix}A^\mathsf{T}\mathbf{l}'\\\mathbf{a}_4^\mathsf{T}\mathbf{l}'\end{pmatrix},\qquad
\boldsymbol{\pi}''=P''^\mathsf{T}\mathbf{l}''=\begin{pmatrix}B^\mathsf{T}\mathbf{l}''\\\mathbf{b}_4^\mathsf{T}\mathbf{l}''\end{pmatrix}
$$

- $P^\mathsf{T}$ 是 $4\times3$。第一個平面的最後一個分量是 0（標準形式造成的）。

**疊成 $4\times3$ 矩陣** [▶ 13:37](https://youtu.be/5wBKv74MtMc?t=817)：

$$
M=[\boldsymbol{\pi},\ \boldsymbol{\pi}',\ \boldsymbol{\pi}'']=\begin{pmatrix}\mathbf{l} & A^\mathsf{T}\mathbf{l}' & B^\mathsf{T}\mathbf{l}''\\ 0 & \mathbf{a}_4^\mathsf{T}\mathbf{l}' & \mathbf{b}_4^\mathsf{T}\mathbf{l}''\end{pmatrix}
$$

- 三個平面不獨立（必須交於同一條線）→ $M$ **不滿秩**。下一節證明 rank **剛好是 2**。

---

## 5. M 的 rank 是 2

[▶ 14:38](https://youtu.be/5wBKv74MtMc?t=878)

1. 三個平面交於 3D 線 $L$。$L$ 上的點可以寫成兩點的組合：$\mathbf{X}=\alpha\mathbf{X}_1+\beta\mathbf{X}_2$。
2. $L$ 上每一點都在三個平面上：$\boldsymbol{\pi}^\mathsf{T}\mathbf{X}=\boldsymbol{\pi}'^\mathsf{T}\mathbf{X}=\boldsymbol{\pi}''^\mathsf{T}\mathbf{X}=0$，即
$$
M^\mathsf{T}\mathbf{X}=\mathbf{0}
$$
3. $\mathbf{X}_1$、$\mathbf{X}_2$ 都滿足 → $M^\mathsf{T}$ 的零空間至少 **2 維**。
4. $M^\mathsf{T}$ 是 $3\times4$，零空間 2 維 → **rank$(M)=2$**。

**意義** [▶ 19:26](https://youtu.be/5wBKv74MtMc?t=1166)：這個零空間條件（三平面交於一線）反過來對 $\mathbf{l},\mathbf{l}',\mathbf{l}''$ 加了一個約束。

---

## 6. 推導 Tᵢ = aᵢb₄ᵀ − a₄bᵢᵀ

[▶ 20:21](https://youtu.be/5wBKv74MtMc?t=1221)

**行之間線性相關**：rank 2 → 三行中有一行是另兩行的線性組合：

$$
\mathbf{m}_1=\alpha\mathbf{m}_2+\beta\mathbf{m}_3
$$

**用 $M$ 的那個 0** [▶ 22:39](https://youtu.be/5wBKv74MtMc?t=1359)：$M$ 的**最後一列第一行**是 0（標準形式造成的）。看最後一列：

$$
0=\alpha(\mathbf{a}_4^\mathsf{T}\mathbf{l}')+\beta(\mathbf{b}_4^\mathsf{T}\mathbf{l}'')
$$

一組明顯的解：

$$
\alpha=k\,(\mathbf{b}_4^\mathsf{T}\mathbf{l}''),\qquad\beta=-k\,(\mathbf{a}_4^\mathsf{T}\mathbf{l}')
$$

驗證：$k(\mathbf{b}_4^\mathsf{T}\mathbf{l}'')(\mathbf{a}_4^\mathsf{T}\mathbf{l}')-k(\mathbf{a}_4^\mathsf{T}\mathbf{l}')(\mathbf{b}_4^\mathsf{T}\mathbf{l}'')=0$ ✓。

⚠️ 逐字稿缺字 [▶ 23:12](https://youtu.be/5wBKv74MtMc?t=1392)：講者說「second row first column」是 0；依 $M$ 的形式（和 MVG），是**最後一列（第四列）第一行**。

**用到前三列** [▶ 25:43](https://youtu.be/5wBKv74MtMc?t=1543)：令 $k=1$（反正齊次）：

$$
\mathbf{l}=(\mathbf{b}_4^\mathsf{T}\mathbf{l}'')A^\mathsf{T}\mathbf{l}'-(\mathbf{a}_4^\mathsf{T}\mathbf{l}')B^\mathsf{T}\mathbf{l}''
$$

**取第 $i$ 個分量** [▶ 27:19](https://youtu.be/5wBKv74MtMc?t=1639)：$A^\mathsf{T}\mathbf{l}'$ 的第 $i$ 個分量是 $\mathbf{a}_i^\mathsf{T}\mathbf{l}'$（$\mathbf{a}_i$ 是 $A$ 的第 $i$ 行），同理 $B$：

$$
l_i=(\mathbf{l}''^\mathsf{T}\mathbf{b}_4)(\mathbf{a}_i^\mathsf{T}\mathbf{l}')-(\mathbf{l}'^\mathsf{T}\mathbf{a}_4)(\mathbf{b}_i^\mathsf{T}\mathbf{l}'')
$$

內積可以交換順序，把 $\mathbf{l}'^\mathsf{T}$ 放左邊、$\mathbf{l}''$ 放右邊：

$$
l_i=\mathbf{l}'^\mathsf{T}(\mathbf{a}_i\mathbf{b}_4^\mathsf{T})\mathbf{l}''-\mathbf{l}'^\mathsf{T}(\mathbf{a}_4\mathbf{b}_i^\mathsf{T})\mathbf{l}''=\mathbf{l}'^\mathsf{T}\underbrace{\left(\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}\right)}_{T_i}\mathbf{l}''
$$

$$
\boxed{\ T_i=\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T},\qquad l_i=\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''\ }
$$

- 每個 $T_i$ 是 $3\times3$。
- $l_i=\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''$ 叫**關聯關係（incidence relation）**：三條對應線經 $T_i$ 連起來。

---

## 7. Trifocal tensor 的定義與記號

[▶ 30:27](https://youtu.be/5wBKv74MtMc?t=1827)

> **Definition 15.1（MVG）** 三個矩陣 $\{T_1,T_2,T_3\}$ 構成（矩陣記號的）**trifocal tensor**。

**為什麼叫 tensor** [▶ 31:09](https://youtu.be/5wBKv74MtMc?t=1869)：

- 三個 $3\times3$ 矩陣疊起來（$T_1$ 在前、$T_2$ 在後、$T_3$ 再後），是一個 $3\times3\times3$ 的立方體。
- 1 維：向量；2 維：矩陣；**3 維：張量（tensor）**。
- 「trifocal」：關聯三個視角。

**簡寫** [▶ 32:41](https://youtu.be/5wBKv74MtMc?t=1961)：

$$
\mathbf{l}^\mathsf{T}=\mathbf{l}'^\mathsf{T}[T_1,T_2,T_3]\mathbf{l}''
$$

- 意思：$\mathbf{l}'^\mathsf{T}T_1\mathbf{l}''$、$\mathbf{l}'^\mathsf{T}T_2\mathbf{l}''$、$\mathbf{l}'^\mathsf{T}T_3\mathbf{l}''$ 三個數排成一列，就是 $\mathbf{l}^\mathsf{T}$（差縮放）。

---

## 8. 參考視角的選擇

[▶ 33:39](https://youtu.be/5wBKv74MtMc?t=2019)

- 上面用**第一個視角**當參考（第一台相機是 $[I\mid\mathbf{0}]$），得到 $\mathbf{l}^\mathsf{T}=\mathbf{l}'^\mathsf{T}[T_i]\mathbf{l}''$。
- 改用第二或第三個視角當參考：線的順序會換，而且得到**完全不同**的 trifocal tensor。
- 三個 tensor 之間有關係（同樣三個視角、同樣的 3D 線），但**關係不簡單**，講者不推導。
- 之後都用第一個視角當參考。

【課本補充】MVG §15.1：一般來說三個 tensor 是不同的；給定一個，可以算出其他兩個（透過相機矩陣），但沒有簡單的直接公式。

---

## 9. 18 個自由度

[▶ 36:07](https://youtu.be/5wBKv74MtMc?t=2167)

- $3\times3\times3=27$ 個元素，但只有 **18 個自由度**。
- **數法**：
  - 每個相機矩陣 11 dof（12 個元素少 1 個縮放）→ 三個獨立的相機共 $3\times11=33$。
  - 但三台相機被影像對應「黏」在一起：一個 $4\times4$ 射影變換 $H$（16 個元素少 1 個縮放 = 15 dof）作用在整個世界上，影像完全不變（第 17、19 集的射影模糊）。
  - $33-15=18$。

講者說「這條 3D 線因為射影平面有 15 個自由度」[▶ 38:04](https://youtu.be/5wBKv74MtMc?t=2284)。

> 以下**不是逐字稿內容**：15 個自由度屬於**射影世界座標系（3D 射影變換 $H$）**，不是 3D 線本身（3D 線只有 4 個自由度，第 04 集）。講者最後的說法「33 − 15 for the projective world frame」才是正確的意思。

【課本補充】MVG §15.1：27 個元素差縮放有 26 個獨立比值，但只有 18 個自由度 → 元素之間還要滿足 8 個獨立的代數約束。估計 tensor 時要處理這件事（第 26 集）。

（本集到 39:19 結束。）

---

## 10. 一頁速查表

| 項目 | 公式／內容 | 關鍵一步 |
|---|---|---|
| 為什麼需要三個視角 | 兩平面總交於一線（無約束）；三平面交於一線是約束 | — |
| 標準相機 | $P=[I\mid\mathbf{0}]$、$P'=[A\mid\mathbf{a}_4]$、$P''=[B\mid\mathbf{b}_4]$ | — |
| 極點 | $\mathbf{e}'=\mathbf{a}_4$、$\mathbf{e}''=\mathbf{b}_4$ | $P'(0,0,0,1)^\mathsf{T}$ |
| 反投影平面 | $(\mathbf{l};0)$、$(A^\mathsf{T}\mathbf{l}';\mathbf{a}_4^\mathsf{T}\mathbf{l}')$、$(B^\mathsf{T}\mathbf{l}'';\mathbf{b}_4^\mathsf{T}\mathbf{l}'')$ | $\boldsymbol{\pi}=P^\mathsf{T}\mathbf{l}$ |
| rank$(M)=2$ | $M^\mathsf{T}\mathbf{X}=0$ 對整條線成立 | 零空間 2 維 |
| $T_i$ | $\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}$ | $\alpha=\mathbf{b}_4^\mathsf{T}\mathbf{l}''$、$\beta=-\mathbf{a}_4^\mathsf{T}\mathbf{l}'$（用 $M$ 左下的 0） |
| 線關聯 | $l_i=\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''$；$\mathbf{l}^\mathsf{T}=\mathbf{l}'^\mathsf{T}[T_1,T_2,T_3]\mathbf{l}''$ | — |
| 自由度 | 18 = 33 − 15 | 三個相機 − 射影世界座標 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $T_i=\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}$ | 第 24 集（平面誘導的 homography、點線關聯） |
| 極點 $\mathbf{a}_4,\mathbf{b}_4$ | 第 25 集（從 tensor 取出極點、$F$、相機） |
| 18 dof、8 個內部約束 | 第 26 集（估計 trifocal tensor） |
| 線–線–線關聯 | 第 26 集（每組線對應給 2 條方程式） |

---

## 附：本集一句話總結

> **兩張圖的對應線沒有約束（兩平面總交於一線），三張圖才有——三條對應線反投影的三個平面必須交於同一條 3D 線，所以 $M=[\boldsymbol{\pi},\boldsymbol{\pi}',\boldsymbol{\pi}'']$ 是 rank 2；用標準相機 $P=[I\mid\mathbf{0}]$、$P'=[A\mid\mathbf{a}_4]$、$P''=[B\mid\mathbf{b}_4]$ 和 $M$ 左下角的 0，推出 $l_i=\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''$，$T_i=\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}$——這三個 $3\times3$ 矩陣就是 trifocal tensor，27 個元素但只有 18 個自由度。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 9 (Part 1) 錄影逐字稿（Whisper `medium.en`，39:26）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §15.1 整理。*
