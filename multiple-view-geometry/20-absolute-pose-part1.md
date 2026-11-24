---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 20
lecture: Lecture 8 (Part 1) – Absolute pose estimation from points or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/C5L7LnNL4oo
notes: MVG §7.1–7.2（書頁 178–184，PDF 頁 196–202）；校正相機的演算法講者取自論文（BRIEF 沒列，未查）
---

# 第 20 集 · Lecture 8 (Part 1)：PnP 問題、未校正相機的 DLT（點與線） [▶ 影片](https://youtu.be/C5L7LnNL4oo)

← 上一集：[19-fundamental-essential-part4](19-fundamental-essential-part4.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[21-absolute-pose-part2](21-absolute-pose-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 20 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（46:11，Whisper `medium.en` 轉錄）＋ MVG §7.1–7.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. PnP 問題](#1-pnp-問題)
- [2. 未校正相機：DLT 求 P](#2-未校正相機dlt-求-p)
  - [2.1 每對點兩條方程式](#21-每對點兩條方程式)
  - [2.2 最少 5½ 對點](#22-最少-5-對點)
  - [2.3 代數誤差與兩種正規化約束](#23-代數誤差與兩種正規化約束)
  - [2.4 幾何誤差精修](#24-幾何誤差精修)
  - [2.5 資料正規化：2D 和 3D 都要](#25-資料正規化2d-和-3d-都要)
  - [2.6 演算法](#26-演算法)
  - [2.7 從 P 得到相機位姿](#27-從-p-得到相機位姿)
- [3. 用線對應求 P](#3-用線對應求-p)
  - [3.1 線性約束](#31-線性約束)
  - [3.2 線的幾何誤差](#32-線的幾何誤差)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/C5L7LnNL4oo?t=0)

Lecture 8 的目標（三集合起來）：

| 目標 | 本集？ | 來源 |
|---|---|---|
| 定義 **perspective-n-point（PnP）**相機位姿估計問題 | ✅ | — |
| 未校正相機：用 n 個點或線的 2D–3D 對應求位姿 | ✅ | MVG 第 7 章 |
| 校正相機的三個演算法：Grunert 三點法、Quan 四點法、EPnP | 第 21–22 集 | 論文 |
| PnP 的退化情況 | 第 22 集 | 論文 |

講者列的來源：

- 未校正相機：MVG 第 7 章。
- Grunert 三點法：Haralick 等人〈Review and analysis of solutions of the three point perspective pose estimation problem〉（IJCV 1994），回顧原本以德文寫的論文。
- Quan 四點法：〈Linear N-point camera pose determination〉（T-PAMI 1999）。
- EPnP：Lepetit 等人（IJCV 2009）。
- 退化分析：〈Space resection: failure cases〉（Photogrammetric Record 1966）。

⚠️ 逐字稿缺字：Whisper 把 PnP 寫成 “PMP”、Grunert 寫成 “Grunet”、Lepetit 寫成 “Lapetit”、Hartley 寫成 “Hartling”。

---

## 1. PnP 問題

[▶ 02:07](https://youtu.be/C5L7LnNL4oo?t=127)

**給定**：

- 一組 3D 點 $\mathbf{X}_1,\dots,\mathbf{X}_n$（齊次座標 $(X,Y,Z,W)$），用**世界座標系** $F_W$ 表示。
- 每個 3D 點在影像上的像 $\mathbf{x}_1,\dots,\mathbf{x}_n$（齊次座標，相機座標系 $F_C$）。
- 這叫 **2D–3D 對應**。

**求**：相機的**位姿（pose）**——相機座標系在世界座標系中的旋轉 $R$ 和平移 $\mathbf{t}$。

- 這個問題叫 **perspective-n-point（PnP）問題**。
- 「perspective」：用的是射影（中心投影）相機，所有光線交於一點。
- 【口頭】之後（Lecture 12）會看**非透視（non-perspective）PnP**：廣義相機，光線不通過同一個投影中心（例如任意形狀的鏡頭）。

---

## 2. 未校正相機：DLT 求 P

### 2.1 每對點兩條方程式

[▶ 04:39](https://youtu.be/C5L7LnNL4oo?t=279)

- **未校正**：內參 $K$ 未知。要求的 $R$、$\mathbf{t}$ 也未知。
- 乾脆把它們全部放進 $3\times4$ 的投影矩陣 $P$：**12 個未知數**。
- 目標：找 $P$，使每個 3D 點 $\mathbf{X}_i$ 投影到給定的像點 $\mathbf{x}_i$。

**去掉縮放**（同第 08 集 homography 的外積技巧）[▶ 05:48](https://youtu.be/C5L7LnNL4oo?t=348)：

$$
\gamma\mathbf{x}_i=P\mathbf{X}_i\quad\Longrightarrow\quad\mathbf{x}_i\times P\mathbf{X}_i=\mathbf{0}
$$

- 展開成 3 條方程式，$P$ 排成 12 維向量 $\mathbf{p}$，係數矩陣是 $3\times12$。
- 和 homography 一樣，**只有 2 條獨立**，丟掉第三條：
$$
\begin{pmatrix}\mathbf{0}^\mathsf{T} & -w_i\mathbf{X}_i^\mathsf{T} & y_i\mathbf{X}_i^\mathsf{T}\\ w_i\mathbf{X}_i^\mathsf{T} & \mathbf{0}^\mathsf{T} & -x_i\mathbf{X}_i^\mathsf{T}\end{pmatrix}\begin{pmatrix}\mathbf{p}^1\\\mathbf{p}^2\\\mathbf{p}^3\end{pmatrix}=\mathbf{0}
$$
  （$\mathbf{p}^{j\mathsf{T}}$ 是 $P$ 的第 $j$ 列；$\mathbf{x}_i=(x_i,y_i,w_i)^\mathsf{T}$。）
- $n$ 對點疊成 $2n\times12$ 的 $A$：
$$
A\mathbf{p}=\mathbf{0}
$$

（$2\times12$ 矩陣的元素依 MVG 式 (7.2) 寫出；逐字稿只說「展開得到這個矩陣形式」。）

### 2.2 最少 5½ 對點

[▶ 08:20](https://youtu.be/C5L7LnNL4oo?t=500)

- $\mathbf{p}$ 有 12 個元素、差縮放 → **11 個自由度**。要非平凡解，$A$ 的 rank 必須是 11。
- 每對點 2 條約束 → 需要 $11/2=5.5$ 對。
- 「半對」的意思：第 6 對點只用它的**一條**方程式。實際上**至少要 6 對點**。

**解**：$A$ 的 SVD，$\mathbf{p}$ = $V$ 的最後一行（最小奇異值）。

- 有雜訊時，最好用**多於 6 對**點。

【課本補充】MVG §7.1 的退化配置：(i) 相機中心和所有點在同一條**扭曲三次曲線（twisted cubic）**上；(ii) 所有點在「一個平面 ∪ 一條通過相機中心的直線」上。這時 $P$ 不能唯一確定。

### 2.3 代數誤差與兩種正規化約束

[▶ 11:41](https://youtu.be/C5L7LnNL4oo?t=701)

有雜訊時 $A\mathbf{p}\neq\mathbf{0}$，改成最小化 $\|A\mathbf{p}\|$。要加一個正規化約束，否則 $\mathbf{p}=\mathbf{0}$ 是平凡解。

**選項一**（本課採用）：$\|\mathbf{p}\|=1$——和 homography（$\|\mathbf{h}\|=1$）、fundamental matrix（$\|\mathbf{f}\|=1$）一樣。

**選項二** [▶ 14:03](https://youtu.be/C5L7LnNL4oo?t=843)：$\|\hat{\mathbf{p}}^3\|=1$——$\hat{\mathbf{p}}^3$ 是 $P=[M\mid\mathbf{p}_4]$ 中 $M$ 的**第三列**（$P$ 第三列的前三個元素）。這是 homography 和 $F$ 沒有的選項。

- **為什麼可以** [▶ 14:57](https://youtu.be/C5L7LnNL4oo?t=897)：第 11 集的深度公式 $\operatorname{depth}=\dfrac{\operatorname{sign}(\det M)\,w}{T\,\|\mathbf{m}^3\|}$。規定 $\|\mathbf{m}^3\|=1$，$w$ 就有深度的意義。
- **怎麼做** [▶ 16:45](https://youtu.be/C5L7LnNL4oo?t=1005)：SVD 解出 $\mathbf{p}=\lambda\mathbf{v}$（一族解），取對應 $\hat{\mathbf{p}}^3$ 的三個元素，令其長度為 1，解出 $\lambda$。

【課本補充】MVG §7.2.1：用選項二時，代數誤差有幾何解釋（和幾何誤差相差一個深度相關的因子）。

### 2.4 幾何誤差精修

[▶ 17:42](https://youtu.be/C5L7LnNL4oo?t=1062)

- 用代數解當初值，再最小化**重投影誤差**：
$$
\min_P\ \sum_id(\mathbf{x}_i,P\mathbf{X}_i)^2
$$
  $P\mathbf{X}_i=\hat{\mathbf{x}}_i$ 是用估計的 $P$ 重投影的點，一般不會和觀測點 $\mathbf{x}_i$ 重合。
- 幾何誤差**有物理意義**，結果比代數誤差準（第 09 集）。
- 無約束連續最佳化，用 **Levenberg–Marquardt** 或 **Gauss–Newton**（講者說在 bundle adjustment 那講細講）。

⚠️ 逐字稿缺字：Whisper 把 Levenberg–Marquardt 寫成 “luvermmert-makur”、“luverberg macquardt”；bundle adjustment 寫成 “budget adjustment”。

【課本補充】MVG Algorithm 7.1 叫這個方法 **Gold Standard 演算法**（假設 3D 點非常準確、只有像點有誤差）。

### 2.5 資料正規化：2D 和 3D 都要

[▶ 20:29](https://youtu.be/C5L7LnNL4oo?t=1229)

- $A$ 要條件良好，SVD 才準（第 08 集）。
- 3D 點可能用很遠的世界座標系表示、有的近有的遠；2D 點也可能分布不均——都會讓 $A$ 的各行量級差很多。
- 所以 **2D 和 3D 都要正規化**：

| | 2D（像點） | 3D（世界點） |
|---|---|---|
| 矩陣 | $T$（$3\times3$） | $U$（$4\times4$） |
| 平移 | 重心到原點 | 重心到原點 |
| 縮放 | 平均距離 $\sqrt{2}$：$s=\sqrt{2}/\bar{d}$ | 平均距離 $\sqrt{3}$：$s=\sqrt{3}/\bar{d}$ |

（講者說「root mean square 距離」，又說 $s$ 是除以「平均距離」；MVG 用 RMS 距離。）

【課本補充】MVG §7.1：這種 3D 正規化適用於點相對集中、深度變化不大的情況；若點離相機的距離差很多（例如延伸到很遠），要改用 MVG 第 4 章習題 (iii) 的方法。

### 2.6 演算法

[▶ 26:10](https://youtu.be/C5L7LnNL4oo?t=1570)

**在解什麼**：$n\ge6$ 對 2D–3D 點對應 $\mathbf{x}_i\leftrightarrow\mathbf{X}_i$，求 $P$ 使重投影誤差 $\sum_id(\mathbf{x}_i,P\mathbf{X}_i)^2$ 最小。

**步驟**：

1. **正規化**：$\tilde{\mathbf{x}}_i=T\mathbf{x}_i$、$\tilde{\mathbf{X}}_i=U\mathbf{X}_i$。
2. **線性解（DLT）**：組 $A\tilde{\mathbf{p}}=\mathbf{0}$，在 $\|\tilde{\mathbf{p}}\|=1$ 下用 SVD 求 $\tilde{P}$。
3. **幾何精修**：用 LM 最小化 $\sum_id(\tilde{\mathbf{x}}_i,\tilde{P}\tilde{\mathbf{X}}_i)^2$。
4. **反正規化**：
$$
P=T^{-1}\tilde{P}U
$$

> 以下**不是逐字稿內容**，是反正規化的推導：$\tilde{\mathbf{x}}=\tilde{P}\tilde{\mathbf{X}}$ → $T\mathbf{x}=\tilde{P}U\mathbf{X}$ → $\mathbf{x}=T^{-1}\tilde{P}U\mathbf{X}$。

### 2.7 從 P 得到相機位姿

[▶ 30:30](https://youtu.be/C5L7LnNL4oo?t=1830)

$P=K[R\mid\mathbf{t}]=KR[I\mid-\tilde{\mathbf{C}}]$，要拆出 $K$、$R$、$\mathbf{t}$：

1. **$K$ 和 $R$**：$M=KR$，用 **RQ 分解**（第 11 集）。
2. **相機中心**：$P$ 的最後一行 $\mathbf{p}_4=-M\tilde{\mathbf{C}}$，3 條方程式解 3 個未知數。
3. **平移的尺度** [▶ 32:26](https://youtu.be/C5L7LnNL4oo?t=1946)：$\|\mathbf{p}\|=1$ 的約束把 $P$ 的尺度丟掉了，所以 $\mathbf{t}$ 只確定到差一個尺度。
   - 但 3D 點的位置是**已知的絕對座標** → 提供絕對尺度。
   - 講者的做法：反投影光線 $\mathbf{X}(\lambda)=P^+\mathbf{x}+\lambda\mathbf{C}$，已知的 3D 點在這條光線上，用它解出 $\lambda$（深度），再把 $\mathbf{t}/\|\mathbf{t}\|$ 乘上這個尺度。

⚠️ 逐字稿缺字 [▶ 31:24](https://youtu.be/C5L7LnNL4oo?t=1884)：講者說分解方法是「lecture four」講的，依本播放清單應為 Lecture 5（第 11 集）。

> 以下**不是逐字稿內容**，是另一種看法：$P$ 只差一個整體縮放 $\lambda$，$\lambda P=\lambda K[R\mid\mathbf{t}]$。RQ 分解後把 $K$ 正規化成 $K_{33}=1$（並讓對角為正、$\det R=+1$），整體縮放就被吸收掉，得到的 $\mathbf{t}$ 自動是正確尺度——因為 3D 點本身是公制座標。

---

## 3. 用線對應求 P

### 3.1 線性約束

[▶ 35:16](https://youtu.be/C5L7LnNL4oo?t=2116)

**設定**：給 2D 影像線和它們對應的 3D 線，求 $P$（同樣的目標）。

1. 3D 線用線上兩點 $\mathbf{X}_0$、$\mathbf{X}_1$（齊次）表示。
2. 影像線 $\mathbf{l}$ 反投影成平面 $P^\mathsf{T}\mathbf{l}$（第 13 集）。
3. 3D 線在這個平面上 → 它的兩個點都在平面上：
$$
\mathbf{l}^\mathsf{T}P\mathbf{X}_j=0,\qquad j=0,1
$$
4. 每個 $j$ 給 **1 條**對 $P$ 線性的方程式 → 每對線對應給 **2 條**。

講者說展開後是 $3\times12$ 矩陣、只有兩列獨立 [▶ 39:31](https://youtu.be/C5L7LnNL4oo?t=2371)。

> 以下**不是逐字稿內容**：依 MVG §7.1，$\mathbf{l}^\mathsf{T}P\mathbf{X}_j=0$ 本身就是一條純量方程式（不是 3 條），兩個 $j$ 直接給 2 條。寫成 $\mathbf{p}$ 的線性式：$\mathbf{l}^\mathsf{T}P\mathbf{X}_j=\sum_{r}l_r\,\mathbf{p}^{r\mathsf{T}}\mathbf{X}_j=(l_1\mathbf{X}_j^\mathsf{T},\ l_2\mathbf{X}_j^\mathsf{T},\ l_3\mathbf{X}_j^\mathsf{T})\,\mathbf{p}=0$。

5. $n$ 對線疊成 $2n\times12$ 的 $A\mathbf{p}=\mathbf{0}$，同樣在 $\|\mathbf{p}\|=1$（首選）或 $\|\hat{\mathbf{p}}^3\|=1$ 下用 SVD 解。
6. 線和點的約束可以**混在一起**疊。

（第 6 點依 MVG §7.1 補上。）

⚠️ 逐字稿缺字 [▶ 37:07](https://youtu.be/C5L7LnNL4oo?t=2227)：講者說反投影平面是「lecture five」講的，依本播放清單應為 Lecture 6（第 13 集）。

### 3.2 線的幾何誤差

[▶ 43:12](https://youtu.be/C5L7LnNL4oo?t=2592)

講者介紹他自己幾年前在 ECCV 發表的定義：

1. 3D 線的兩個端點 $\mathbf{X}_{i0}$、$\mathbf{X}_{i1}$ 用 $P$ 重投影：$\hat{\mathbf{x}}_{i0}=P\mathbf{X}_{i0}$、$\hat{\mathbf{x}}_{i1}=P\mathbf{X}_{i1}$。
2. 量兩個重投影端點到**觀測的影像線** $\mathbf{l}_i$ 的垂直距離 $d_0$、$d_1$。
3. $d_0=d_1=0$ 表示重投影出來的線段**剛好落在**觀測線上。
4. **長度偏差**：只把 $d_0+d_1$ 加起來，會偏好短線——同樣小的角度誤差，長線端點離得遠，誤差大；短線誤差小。
5. 所以**用 3D 線的長度正規化**誤差。

> 以下**不是逐字稿內容**：逐字稿沒唸出公式。依描述，可以寫成類似 $\sum_i\dfrac{d_0^2+d_1^2}{\|\tilde{\mathbf{X}}_{i1}-\tilde{\mathbf{X}}_{i0}\|}$ 的形式；點到線距離是 $d=\dfrac{|\mathbf{l}^\mathsf{T}\hat{\mathbf{x}}|}{\hat{w}\sqrt{l_1^2+l_2^2}}$（$\hat{\mathbf{x}}=(\hat{x},\hat{y},\hat{w})^\mathsf{T}$）。確切的正規化方式（平方與否、長度怎麼量）以講者論文為準。

（本集到 46:04 結束。）

---

## 4. 一頁速查表

### PnP

- 給 $n$ 對 $\mathbf{x}_i\leftrightarrow\mathbf{X}_i$，求相機的 $R$、$\mathbf{t}$（未校正時連 $K$ 一起）。

### 未校正 DLT

| 項目 | 內容 |
|---|---|
| 未知數 | $P$ 的 12 個元素，11 dof |
| 每對點 | $\mathbf{x}_i\times P\mathbf{X}_i=0$ → 2 條（$2\times12$） |
| 最少 | 5½ 對（實際 6 對，第 6 對只用一條） |
| 約束 | $\|\mathbf{p}\|=1$（首選）或 $\|\hat{\mathbf{p}}^3\|=1$（深度意義） |
| 正規化 | 2D：重心到原點、RMS $\sqrt{2}$；3D：重心到原點、RMS $\sqrt{3}$ |
| 精修 | LM 最小化 $\sum_id(\mathbf{x}_i,P\mathbf{X}_i)^2$（Gold Standard） |
| 反正規化 | $P=T^{-1}\tilde{P}U$ |
| 位姿 | RQ($M$) → $K,R$；$\mathbf{p}_4=-M\tilde{\mathbf{C}}$ → $\tilde{\mathbf{C}}$；3D 點給絕對尺度 |

### 線對應

- $\mathbf{l}^\mathsf{T}P\mathbf{X}_j=0$，$j=0,1$ → 每對線 2 條；可和點混用。
- 幾何誤差：兩端點重投影到觀測線的距離，用 3D 線長正規化（避免偏好短線）。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 已校正 PnP | 第 21 集（Grunert P3P）；第 22 集（Quan 4 點法、EPnP） |
| 6 點 DLT 當最小解 + RANSAC | 第 21–22 集（P3P + RANSAC 才是校正相機的常用法） |
| 退化配置 | 第 22 集（PnP 退化：危險圓柱等） |
| 非透視 PnP | 第 35–37 集（Lecture 12：廣義相機） |
| 重投影誤差精修 | 第 27–30 集（bundle adjustment） |

---

## 附：本集一句話總結

> **PnP 是「已知 3D 點和它們的像，求相機位姿」；相機未校正時把 $K,R,\mathbf{t}$ 全塞進 $P$，每對點經 $\mathbf{x}\times P\mathbf{X}=0$ 給兩條線性方程式，至少 6 對點（5½）就能用 SVD 解出 $P$——記得 2D 正規化到 $\sqrt{2}$、3D 正規化到 $\sqrt{3}$，再用重投影誤差精修、RQ 分解出 $K$ 和 $R$；3D 線也行：兩端點都在影像線的反投影平面上，$\mathbf{l}^\mathsf{T}P\mathbf{X}_j=0$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 8 (Part 1) 錄影逐字稿（Whisper `medium.en`，46:11）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §7.1–7.2 整理。*
