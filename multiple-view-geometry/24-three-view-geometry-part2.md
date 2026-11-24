---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 24
lecture: Lecture 9 (Part 2) – Three-view geometry from points and/or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/gQ1ge1fySIw
notes: MVG §15.1.1–15.1.3（書頁 368–374，PDF 頁 386–392）
---

# 第 24 集 · Lecture 9 (Part 2)：trifocal tensor 誘導的 homography、點線關聯、極線與極點 [▶ 影片](https://youtu.be/gQ1ge1fySIw)

← 上一集：[23-three-view-geometry-part1](23-three-view-geometry-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[25-three-view-geometry-part3](25-three-view-geometry-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 24 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（38:26，Whisper `medium.en` 轉錄）＋ MVG §15.1.1–15.1.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 平面誘導的 homography](#1-平面誘導的-homography)
- [2. 五種點線關聯](#2-五種點線關聯)
  - [2.1 線–線–線](#21-線線線)
  - [2.2 點–線–線](#22-點線線)
  - [2.3 點–線–點、點–點–線](#23-點線點點點線)
  - [2.4 點–點–點](#24-點點點)
  - [2.5 總表](#25-總表)
- [3. 從 tensor 取極線](#3-從-tensor-取極線)
- [4. 從 tensor 取極點](#4-從-tensor-取極點)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 一個視角的線，誘導另外兩個視角之間的 homography | §15.1.1 |
| 點和線的各種關聯關係 | §15.1.2 |
| 從 trifocal tensor 取出極線、極點 | §15.1.3 |

**記號**：$\mathbf{x}=(x^1,x^2,x^3)^\mathsf{T}$ 的分量用**上標**；$\mathbf{l}=(l_1,l_2,l_3)$ 的分量用**下標**（講者在 [▶ 12:14](https://youtu.be/gQ1ge1fySIw?t=734) 說明）。點在線上：$\mathbf{x}^\mathsf{T}\mathbf{l}=\sum_ix^il_i=0$。

---

## 1. 平面誘導的 homography

[▶ 00:00](https://youtu.be/gQ1ge1fySIw?t=0)

**想法**：

- 第二張圖上一條線 $\mathbf{l}'$ 反投影成平面 $\boldsymbol{\pi}'$。
- 這個平面誘導一個**第一張圖 ↔ 第三張圖**的 homography：把第一張圖的點 $\mathbf{x}$ 轉到第三張圖的 $\mathbf{x}''$（點在 $\boldsymbol{\pi}'$ 上）；也能轉線。
- 不需要先算出 3D 點或 3D 線。

> **Result 15.2（MVG）** 第二張圖的線 $\mathbf{l}'$ 誘導的第一 → 第三張圖 homography 是
> $$\mathbf{x}''=H_{13}(\mathbf{l}')\,\mathbf{x},\qquad H_{13}(\mathbf{l}')=\left[T_1^\mathsf{T}\mathbf{l}',\ T_2^\mathsf{T}\mathbf{l}',\ T_3^\mathsf{T}\mathbf{l}'\right]$$
> 對稱地，第三張圖的線 $\mathbf{l}''$ 誘導第一 → 第二張圖的 homography
> $$\mathbf{x}'=H_{12}(\mathbf{l}'')\,\mathbf{x},\qquad H_{12}(\mathbf{l}'')=\left[T_1\mathbf{l}'',\ T_2\mathbf{l}'',\ T_3\mathbf{l}''\right]$$

**證明** [▶ 02:37](https://youtu.be/gQ1ge1fySIw?t=157)：

1. 第 02 集：點的 homography $\mathbf{x}''=H\mathbf{x}$ 對應的線變換是 $\mathbf{l}=H^\mathsf{T}\mathbf{l}''$（把第三張圖的線轉回第一張）。逐分量：$l_i=\mathbf{h}_i^\mathsf{T}\mathbf{l}''$，$\mathbf{h}_i$ 是 $H$ 的第 $i$ 行。
2. 第 23 集的關聯關係：$l_i=\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''=(T_i^\mathsf{T}\mathbf{l}')^\mathsf{T}\mathbf{l}''$。
3. 比較 → $\mathbf{h}_i=T_i^\mathsf{T}\mathbf{l}'$。即 $H_{13}$ 的第 $i$ 行是 $T_i^\mathsf{T}\mathbf{l}'$。∎

$H_{12}$ 同理 [▶ 05:53](https://youtu.be/gQ1ge1fySIw?t=353)：$\mathbf{l}^\mathsf{T}=\mathbf{l}'^\mathsf{T}H_{12}$，和 $l_i=\mathbf{l}'^\mathsf{T}(T_i\mathbf{l}'')$ 比較，第 $i$ 行是 $T_i\mathbf{l}''$。

---

## 2. 五種點線關聯

### 2.1 線–線–線

[▶ 06:43](https://youtu.be/gQ1ge1fySIw?t=403)

$\mathbf{l}^\mathsf{T}=\mathbf{l}'^\mathsf{T}[T_1,T_2,T_3]\mathbf{l}''$ 只差一個未知縮放。兩邊和 $\mathbf{l}$ 取外積去掉縮放：

$$
\left(\mathbf{l}'^\mathsf{T}[T_1,T_2,T_3]\mathbf{l}''\right)[\mathbf{l}]_\times=\mathbf{0}^\mathsf{T}
$$

- $[T_1,T_2,T_3]$ 簡寫成 $[T_i]$。
- $\mathbf{l}'$ 和 $\mathbf{l}''$ 對稱，轉置也可以寫。
- 只剩對應線和 tensor，沒有其他未知數。

### 2.2 點–線–線

[▶ 09:10](https://youtu.be/gQ1ge1fySIw?t=550)

**幾何**：第一張圖是**點** $\mathbf{x}$，第二、三張是**線** $\mathbf{l}',\mathbf{l}''$。

- $\mathbf{l}',\mathbf{l}''$ 反投影的兩個平面交於 3D 線 $L$。
- 只有這兩個視角時沒有約束（任兩平面總交於一線）。
- 加上第一張圖的點：$\mathbf{x}$ 反投影的光線必須和 $L$ **相交**（3D 點在 $L$ 上）→ 有約束。

**推導** [▶ 11:43](https://youtu.be/gQ1ge1fySIw?t=703)：

1. $\mathbf{x}$ 在 $\mathbf{l}$ 上（$\mathbf{l}$ 是那條 3D 線在第一張圖的像）：$\sum_ix^il_i=0$。
2. 代 $l_i=\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''$：$\sum_ix^i\,\mathbf{l}'^\mathsf{T}T_i\mathbf{l}''=0$。
3. $\mathbf{l}'$、$\mathbf{l}''$ 和 $i$ 無關，提出來：

$$
\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)\mathbf{l}''=0
$$

- 本身就沒有縮放，不必取外積。

### 2.3 點–線–點、點–點–線

**點–線–點** [▶ 15:03](https://youtu.be/gQ1ge1fySIw?t=903)：第一張圖點 $\mathbf{x}$、第二張線 $\mathbf{l}'$、第三張點 $\mathbf{x}''$。

- $\mathbf{x}$ 和 $\mathbf{x}''$ 的光線交於 3D 點；這點在 $\mathbf{l}'$ 反投影的平面 $\boldsymbol{\pi}'$ 上。
- 所以 $\mathbf{x}$ 和 $\mathbf{x}''$ 由 $\boldsymbol{\pi}'$ 誘導的 homography 連起來（第 1 節）：
$$
\mathbf{x}''=H_{13}(\mathbf{l}')\mathbf{x}=\left[T_1^\mathsf{T}\mathbf{l}',T_2^\mathsf{T}\mathbf{l}',T_3^\mathsf{T}\mathbf{l}'\right]\mathbf{x}=\left(\sum_ix^iT_i^\mathsf{T}\right)\mathbf{l}'
$$
  （$\mathbf{l}'$ 是三行共用的，提出來；$x^i$ 推進去。）
- 和 $\mathbf{x}''$ 取外積去掉縮放 [▶ 18:46](https://youtu.be/gQ1ge1fySIw?t=1126)：

$$
\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)[\mathbf{x}'']_\times=\mathbf{0}^\mathsf{T}
$$

（寫成轉置的形式，依 MVG Table 15.1。）

**點–點–線** [▶ 19:43](https://youtu.be/gQ1ge1fySIw?t=1183)：第二張是點 $\mathbf{x}'$、第三張是線 $\mathbf{l}''$。同理（用 $H_{12}(\mathbf{l}'')$）：

$$
[\mathbf{x}']_\times\left(\sum_ix^iT_i\right)\mathbf{l}''=\mathbf{0}
$$

### 2.4 點–點–點

[▶ 20:18](https://youtu.be/gQ1ge1fySIw?t=1218)

三張圖都是點，三條光線交於同一個 3D 點。

**推導** [▶ 21:09](https://youtu.be/gQ1ge1fySIw?t=1269)：

1. 從點–線–點出發：$\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)[\mathbf{x}'']_\times=\mathbf{0}^\mathsf{T}$。
2. 讓 $\mathbf{l}'$ 是**通過 $\mathbf{x}'$ 的任何一條線**：$\mathbf{l}'=\mathbf{x}'\times\mathbf{y}'=[\mathbf{x}']_\times\mathbf{y}'$，$\mathbf{y}'$ 是線上另一點。
3. 代入：$\mathbf{y}'^\mathsf{T}[\mathbf{x}']_\times^\mathsf{T}\left(\sum_ix^iT_i\right)[\mathbf{x}'']_\times=\mathbf{0}^\mathsf{T}$。
4. 這對**任何** $\mathbf{y}'$ 都成立（任何通過 $\mathbf{x}'$ 的線都滿足點–線–點）→ 剩下的部分必須是零矩陣：

$$
[\mathbf{x}']_\times\left(\sum_ix^iT_i\right)[\mathbf{x}'']_\times=0_{3\times3}
$$

（$[\mathbf{x}']_\times^\mathsf{T}=-[\mathbf{x}']_\times$，負號不影響等於零。）

### 2.5 總表

[▶ 24:08](https://youtu.be/gQ1ge1fySIw?t=1448)（MVG Table 15.1）

| 對應 | 關係 | 獨立方程式數（MVG） |
|---|---|---|
| 線–線–線 | $\left(\mathbf{l}'^\mathsf{T}[T_i]\mathbf{l}''\right)[\mathbf{l}]_\times=\mathbf{0}^\mathsf{T}$ | 2 |
| 點–線–線 | $\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)\mathbf{l}''=0$ | 1 |
| 點–線–點 | $\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)[\mathbf{x}'']_\times=\mathbf{0}^\mathsf{T}$ | 2 |
| 點–點–線 | $[\mathbf{x}']_\times\left(\sum_ix^iT_i\right)\mathbf{l}''=\mathbf{0}$ | 2 |
| 點–點–點 | $[\mathbf{x}']_\times\left(\sum_ix^iT_i\right)[\mathbf{x}'']_\times=0_{3\times3}$ | 4 |

（「獨立方程式數」那一行依 MVG Table 15.1 補上；講者在第 26 集估計 tensor 時會用到。）

---

## 3. 從 tensor 取極線

[▶ 25:05](https://youtu.be/gQ1ge1fySIw?t=1505)

- 第一張圖一點 $\mathbf{x}$，反投影成光線；這條光線在第二、三張圖的投影就是**極線** $\mathbf{l}'$、$\mathbf{l}''$。

> **Result 15.3（MVG）** $\mathbf{x}$ 對應的極線 $\mathbf{l}'$、$\mathbf{l}''$ 滿足
> $$\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)=\mathbf{0}^\mathsf{T},\qquad\left(\sum_ix^iT_i\right)\mathbf{l}''=\mathbf{0}$$
> 也就是說，$\mathbf{l}'$ 和 $\mathbf{l}''$ 分別是 $3\times3$ 矩陣 $\sum_ix^iT_i$ 的**左、右零向量**。

**證明** [▶ 28:34](https://youtu.be/gQ1ge1fySIw?t=1714)：

1. 讓 $\mathbf{l}'$ 是極線：它反投影的平面 $\boldsymbol{\pi}'$ 是**極平面**——包含 $C$、$C'$ 和 $\mathbf{x}$ 的光線。
2. 第三張圖任取一條線 $\mathbf{l}''$，反投影成平面 $\boldsymbol{\pi}''$。它和極平面交於一條 3D 線 $L$。
3. $\mathbf{x}$ 的光線、$L$ 都在極平面裡 → 光線和 $L$ 相交 → $(\mathbf{x},\mathbf{l}',\mathbf{l}'')$ 滿足**點–線–線**關聯：
$$
\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)\mathbf{l}''=0
$$
4. 關鍵：**$\mathbf{l}''$ 是任意的**（沒有限制）。對所有 $\mathbf{l}''$ 都成立 → $\mathbf{l}'^\mathsf{T}\left(\sum_ix^iT_i\right)=\mathbf{0}^\mathsf{T}$。
5. 角色互換（讓 $\mathbf{l}''$ 是極線、$\mathbf{l}'$ 任意）→ $\left(\sum_ix^iT_i\right)\mathbf{l}''=\mathbf{0}$。∎

---

## 4. 從 tensor 取極點

[▶ 35:10](https://youtu.be/gQ1ge1fySIw?t=2110)

- $\mathbf{x}$ 在第一張圖上移動 → 第二張圖得到不同的極線 $\mathbf{l}'$，但**全部交於極點** $\mathbf{e}'$（第 16 集）。第三張圖同理，交於 $\mathbf{e}''$。
- 所以：多取幾個 $\mathbf{x}$，求出各自的極線，再求交點。

**方便的選擇** [▶ 36:33](https://youtu.be/gQ1ge1fySIw?t=2193)：$\mathbf{x}=(1,0,0)^\mathsf{T}$、$(0,1,0)^\mathsf{T}$、$(0,0,1)^\mathsf{T}$。

- $\mathbf{x}=(1,0,0)^\mathsf{T}$ 時 $\sum_ix^iT_i=T_1$——只要求 $T_1$ 的左、右零向量。
- 同理 $(0,1,0)^\mathsf{T}$ → $T_2$；$(0,0,1)^\mathsf{T}$ → $T_3$。

> **Result 15.4（MVG）** 第二張圖的極點 $\mathbf{e}'$ 是 $T_1,T_2,T_3$ 三個**左零向量**（三條極線）的共同交點；第三張圖的極點 $\mathbf{e}''$ 是三個**右零向量**的共同交點。

⚠️ 逐字稿缺字：Whisper 把 epipole 寫成 “epipode”。

> 以下**不是逐字稿內容**，是驗證 $T_i$ 的零向量是極線（用第 23 集的 $T_i=\mathbf{a}_i\mathbf{b}_4^\mathsf{T}-\mathbf{a}_4\mathbf{b}_i^\mathsf{T}$）：取 $\mathbf{l}'=\mathbf{a}_4\times\mathbf{a}_i=\mathbf{e}'\times\mathbf{a}_i$，則 $\mathbf{l}'^\mathsf{T}T_i=(\mathbf{l}'^\mathsf{T}\mathbf{a}_i)\mathbf{b}_4^\mathsf{T}-(\mathbf{l}'^\mathsf{T}\mathbf{a}_4)\mathbf{b}_i^\mathsf{T}=\mathbf{0}^\mathsf{T}$（$\mathbf{l}'$ 和 $\mathbf{a}_i$、$\mathbf{a}_4$ 都垂直）。這條線通過 $\mathbf{e}'=\mathbf{a}_4$——確實是極線。

【課本補充】MVG §15.1.3：實務上把三條極線疊成 $3\times3$ 矩陣，求它的零向量得極點（有雜訊時用 SVD）。

（本集到 38:19 結束。）

---

## 5. 一頁速查表

### Homography

| 由哪條線誘導 | 映射 | 第 $i$ 行 | 關鍵一步 |
|---|---|---|---|
| 第二張的 $\mathbf{l}'$ | 第一 → 第三：$\mathbf{x}''=H_{13}\mathbf{x}$ | $T_i^\mathsf{T}\mathbf{l}'$ | $l_i=\mathbf{h}_i^\mathsf{T}\mathbf{l}''$ 對比 $l_i=(T_i^\mathsf{T}\mathbf{l}')^\mathsf{T}\mathbf{l}''$ |
| 第三張的 $\mathbf{l}''$ | 第一 → 第二：$\mathbf{x}'=H_{12}\mathbf{x}$ | $T_i\mathbf{l}''$ | 同理 |

### 關聯關係

見第 2.5 節表。推導路線：線–線–線 →（$\mathbf{x}^\mathsf{T}\mathbf{l}=0$）點–線–線 →（homography）點–線–點、點–點–線 →（$\mathbf{l}'=[\mathbf{x}']_\times\mathbf{y}'$，$\mathbf{y}'$ 任意）點–點–點。

### 極線與極點

| 項目 | 公式 | 關鍵一步 |
|---|---|---|
| 極線 | $\mathbf{l}'$ = $\sum_ix^iT_i$ 的左零向量；$\mathbf{l}''$ = 右零向量 | 點–線–線對任意 $\mathbf{l}''$（或 $\mathbf{l}'$）成立 |
| 極點 | $\mathbf{e}'$ = $T_1,T_2,T_3$ 左零向量的交點；$\mathbf{e}''$ = 右零向量的交點 | 取 $\mathbf{x}=\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 極點 $\mathbf{e}',\mathbf{e}''$ | 第 25 集（從 tensor 求 $F_{21},F_{31}$、相機矩陣） |
| $H_{12}(\mathbf{l}'')$、$H_{13}(\mathbf{l}')$ | 第 25 集（$F_{21}=[\mathbf{e}']_\times[T_1,T_2,T_3]\mathbf{e}''$） |
| 五種關聯關係、方程式數 | 第 26 集（從點／線對應線性估計 tensor） |
| 點轉移 | 第 25–26 集（給兩張圖的點，預測第三張） |

---

## 附：本集一句話總結

> **trifocal tensor 裡藏著平面 homography：第二張圖的線 $\mathbf{l}'$ 誘導第一到第三張的 $H_{13}=[T_i^\mathsf{T}\mathbf{l}']$，第三張的線誘導 $H_{12}=[T_i\mathbf{l}'']$；從線–線–線一路推出點–線–線 $\mathbf{l}'^\mathsf{T}(\sum x^iT_i)\mathbf{l}''=0$、點–線–點、點–點–線、點–點–點五種關聯；而 $\sum x^iT_i$ 的左右零向量就是 $\mathbf{x}$ 在第二、三張圖的極線，取 $\mathbf{x}$ 為三個座標軸，$T_1,T_2,T_3$ 零向量的交點就是極點。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 9 (Part 2) 錄影逐字稿（Whisper `medium.en`，38:26）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §15.1.1–15.1.3 整理。*
