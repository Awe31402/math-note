---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 22
lecture: Lecture 8 (Part 3) – Absolute pose estimation from points or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/9peph2zvSyY
notes: 本集內容講者取自 Quan & Lan〈Linear N-point camera pose determination〉（T-PAMI 1999）和 Lepetit 等人 EPnP（IJCV 2009）；BRIEF 沒列這些論文，未查。MVG 沒有對應內容。
---

# 第 22 集 · Lecture 8 (Part 3)：Quan 線性四點法、線性 N 點法、EPnP [▶ 影片](https://youtu.be/9peph2zvSyY)

← 上一集：[21-absolute-pose-part2](21-absolute-pose-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[23-three-view-geometry-part1](23-three-view-geometry-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 22 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（57:21，Whisper `medium.en` 轉錄）；MVG 沒有對應內容，依 BRIEF 只靠逐字稿
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. P3P 的多解問題](#1-p3p-的多解問題)
- [2. Quan 線性四點法](#2-quan-線性四點法)
  - [2.1 六條雙變數多項式 → 三條四次多項式](#21-六條雙變數多項式--三條四次多項式)
  - [2.2 直接各自解不好](#22-直接各自解不好)
  - [2.3 線性化：At₅ = 0](#23-線性化at--0)
  - [2.4 用 tᵢtⱼ = tₖtₗ 解出 λ、ρ](#24-用-tₜ--tₜ-解出-λρ)
  - [2.5 回代與退化](#25-回代與退化)
- [3. 線性 N 點法](#3-線性-n-點法)
- [4. EPnP](#4-epnp)
  - [4.1 想法：四個控制點](#41-想法四個控制點)
  - [4.2 選世界座標的控制點、求權重 α](#42-選世界座標的控制點求權重-α)
  - [4.3 投影約束：Mx = 0](#43-投影約束mx--0)
  - [4.4 為什麼是線性複雜度](#44-為什麼是線性複雜度)
  - [4.5 用控制點間距離解 β](#45-用控制點間距離解-β)
  - [4.6 控制點共面的情況](#46-控制點共面的情況)
  - [4.7 最後一步：絕對定向](#47-最後一步絕對定向)
- [5. Lecture 8 總結](#5-lecture-8-總結)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 來源 |
|---|---|
| Quan 線性四點法（唯一解） | Quan & Lan, T-PAMI 1999 |
| 推廣到 N 點，以及它的 $O(n^3)$ 問題 | 同上 |
| EPnP：$O(n)$ 的 PnP | Lepetit 等人 |

---

## 1. P3P 的多解問題

[▶ 00:00](https://youtu.be/9peph2zvSyY?t=0)

- Grunert 三點法得到四次多項式 → **最多 4 組解**，不知道選哪一組。
- 實務做法：用**第 4 個點**挑——每組解得到一個 $P=K[R\mid\mathbf{t}]$，把第 4 個 3D 點投影上去，選**重投影誤差最小**的那組。
- 問題：既然一定要第 4 個點，能不能直接用 **4 點（或更多）**一次得到**唯一解**？——Quan 等人（1990 年代）說可以。

⚠️ 逐字稿缺字：Whisper 把 Quan 寫成 “Kwan”、“Kuan”；T-PAMI 寫成 “TIPAMI”。

---

## 2. Quan 線性四點法

### 2.1 六條雙變數多項式 → 三條四次多項式

[▶ 02:05](https://youtu.be/9peph2zvSyY?t=125)

回憶第 21 集的餘弦定理方程式。每條只含**兩個**未知深度：

$$
f_{ij}(s_i,s_j)=s_i^2+s_j^2-2s_is_j\cos\theta_{ij}-d_{ij}^2=0
$$

- $\theta_{ij}$：光線 $i,j$ 的夾角（已知）；$d_{ij}$：3D 點 $i,j$ 的距離（已知）。

（$f_{ij}$ 的寫法依第 21 集的三條方程式統一記號；逐字稿只說「每條只是兩個未知數的函數」。）

- **3 點**：$f_{12},f_{13},f_{23}$ 消去兩個深度 → $s_1$ 的多項式。令 $x=s_1^2$，得到 $x$ 的**四次多項式** $g(x)=0$（和 Grunert 一致）。
- **4 點** [▶ 04:14](https://youtu.be/9peph2zvSyY?t=254)：$\binom{4}{2}=6$ 條 $f_{ij}$。任取三條（含同一個 $s_1$ 的組合）可以消元出一條 $x$ 的四次多項式 → 得到 **3 條**四次多項式 $g(x)$、$g'(x)$、$g''(x)$。

> 以下**不是逐字稿內容**：講者說「六條取三條，$\binom{6}{3}$ 得三條」，算式不對（$\binom{6}{3}=20$）。依 Quan & Lan 的做法理解：以 $s_1$ 為主，三個三元組 $\{1,2,3\}$、$\{1,2,4\}$、$\{1,3,4\}$ 各給一條 $x=s_1^2$ 的四次多項式，共 3 條。

### 2.2 直接各自解不好

[▶ 06:16](https://youtu.be/9peph2zvSyY?t=376)

直覺做法：三條四次多項式各自解，再找共同解。三個缺點：

1. 解好幾個四次方程式很花時間。
2. 有雜訊時，三條各自的解**不會剛好一樣**，很難找共同解。
3. 最重要的：**沒有利用資料的冗餘**來提高穩定性。

### 2.3 線性化：At₅ = 0

[▶ 07:51](https://youtu.be/9peph2zvSyY?t=471)

把三條四次多項式疊起來，係數放進矩陣、$x$ 的各次方放進向量：

$$
\underbrace{\begin{pmatrix}a_4&a_3&a_2&a_1&a_0\\a_4'&a_3'&a_2'&a_1'&a_0'\\a_4''&a_3''&a_2''&a_1''&a_0''\end{pmatrix}}_{A,\ 3\times5}\underbrace{\begin{pmatrix}x^4\\x^3\\x^2\\x\\1\end{pmatrix}}_{\mathbf{t}_5}=\mathbf{0}
$$

- 把 $x^4,\dots,1$ 當成**五個獨立未知數** → 齊次線性方程式 $A\mathbf{t}_5=\mathbf{0}$。
- $A$ 是 $3\times5$，rank 最多 3；$\mathbf{t}_5$ 在 5 維空間 → **欠定**，零空間是 2 維。
- SVD：$A=U\Sigma V^\mathsf{T}$，最後兩個奇異值為 0 → 零空間由 $\mathbf{v}_4$、$\mathbf{v}_5$ 張成：
$$
\mathbf{t}_5=\lambda\mathbf{v}_4+\rho\mathbf{v}_5
$$
- 剩兩個未知數 $\lambda,\rho$。

### 2.4 用 tᵢtⱼ = tₖtₗ 解出 λ、ρ

[▶ 12:46](https://youtu.be/9peph2zvSyY?t=766)

**額外約束**：$\mathbf{t}_5$ 不是任意向量，它的分量是 $x$ 的各次方。把分量記作 $t_k=x^k$（$k=0,\dots,4$），則

$$
t_it_j=t_kt_l\qquad\text{只要}\ i+j=k+l
$$

- 例：$i=1,j=2,k=3,l=0$：$x\cdot x^2=x^3\cdot x^0=x^3$ ✓。

**代入** [▶ 14:11](https://youtu.be/9peph2zvSyY?t=851)：每個 $t_k=\lambda v_{4,k}+\rho v_{5,k}$。代進 $t_it_j-t_kt_l=0$，展開：

$$
(v_{4,i}v_{4,j}-v_{4,k}v_{4,l})\lambda^2+(v_{4,i}v_{5,j}+v_{5,i}v_{4,j}-v_{4,k}v_{5,l}-v_{5,k}v_{4,l})\lambda\rho+(v_{5,i}v_{5,j}-v_{5,k}v_{5,l})\rho^2=0
$$

（展開式依代入整理寫出；逐字稿只說「得到 $\lambda,\rho$ 的這種形式，係數由 $\mathbf{v}_4,\mathbf{v}_5$ 的分量組成」。）

- 所有滿足 $i+j=k+l$（$0\le i,j,k,l\le4$）的組合共 **7 條** [▶ 15:46](https://youtu.be/9peph2zvSyY?t=946)。
- 對 $\lambda^2,\lambda\rho,\rho^2$ 是**線性**的 → 疊成
$$
B\mathbf{y}=\mathbf{0},\qquad B\in\mathbb{R}^{7\times3},\quad\mathbf{y}=(\lambda^2,\lambda\rho,\rho^2)^\mathsf{T}
$$
- **超定**（7 條、3 個未知數），SVD 取最小奇異值的右奇異向量得 $\mathbf{y}=(y_0,y_1,y_2)$。

**從 $\mathbf{y}$ 得 $\lambda/\rho$** [▶ 17:31](https://youtu.be/9peph2zvSyY?t=1051)：

$$
\frac{\lambda}{\rho}=\frac{y_0}{y_1}=\frac{y_1}{y_2}
$$

- 兩個比值有雜訊時不一定相同，**取平均**。
- 再加一個約束：$\mathbf{t}_5$ 中「1」那個分量等於 1：$\lambda v_{4,0}+\rho v_{5,0}=1$。
- 兩條方程式、兩個未知數 → **唯一**解出 $\lambda,\rho$ → 唯一的 $\mathbf{t}_5$。

⚠️ 待確認 [▶ 18:48](https://youtu.be/9peph2zvSyY?t=1128)：講者先把 $\mathbf{t}_5$ 寫成 $(x^4,x^3,x^2,x,1)$，後來又說「$\mathbf{t}$ 的**第一個**元素等於 1」，兩者順序不一致。筆記的推導不依賴順序，只要用「1 那個分量」即可；投影片上的實際順序待確認。

### 2.5 回代與退化

[▶ 20:09](https://youtu.be/9peph2zvSyY?t=1209)

1. 從 $\mathbf{t}_5$ 的相鄰分量比值求 $x$（例如 $x=t_1/t_0$、$t_2/t_1$……共 **4 個**比值）。有雜訊時它們很接近，**取平均**。
2. $s_1=\sqrt{x}$；**丟掉負根**（深度必須為正）。
3. $s_1$ 代回 $f_{1j}(s_1,s_j)=0$ 求 $s_j$，再依序求其他深度。
4. 有了所有深度 → 相機座標下的 3D 點 → **絕對定向**（第 21 集）求 $R,\mathbf{t}$。

**唯一解** [▶ 21:55](https://youtu.be/9peph2zvSyY?t=1315)：$\lambda,\rho$、$x$ 都唯一 → 只要 4 點不退化，解唯一。

**退化** [▶ 22:23](https://youtu.be/9peph2zvSyY?t=1343)（同 P3P）：

1. 4 個點**共線**（和相機中心共面）。
2. 4 個點和**相機中心共面**。

---

## 3. 線性 N 點法

[▶ 23:09](https://youtu.be/9peph2zvSyY?t=1389)

**5 點**：

- $\binom{5}{2}=10$ 條 $f_{ij}$，得到 **6** 條四次多項式（講者的數法）。
- 疊成 $6\times5$ 的 $A\mathbf{t}_5=\mathbf{0}$——**超定**。要有非平凡解，rank 最多 4。
- SVD，$\mathbf{t}_5=\lambda\mathbf{v}_5$（最小奇異值的右奇異向量）。
- 用「1 那個分量等於 1」解出 $\lambda$ → 唯一 $\mathbf{t}_5$ → $x$ → $s_1$。

> 以下**不是逐字稿內容**，是「6 條」的一種數法：以 $s_1$ 為主，從其餘 4 個點中選 2 個和點 1 組成三元組，有 $\binom{4}{2}=6$ 個，每個給一條 $x=s_1^2$ 的四次多項式。一般 $n$ 點是 $\binom{n-1}{2}=\frac{(n-1)(n-2)}{2}$ 條——和講者下一段說的矩陣大小一致。

**一般 $n\ge4$ 點** [▶ 26:22](https://youtu.be/9peph2zvSyY?t=1582)：

- 解一個 $\frac{(n-1)(n-2)}{2}\times5$ 的 $A$ 的 SVD。
- **問題**：講者說這個 SVD 的整體複雜度是 $n$ 的**三次方** $O(n^3)$（證明略）——點很多時不實用。

---

## 4. EPnP

### 4.1 想法：四個控制點

[▶ 27:35](https://youtu.be/9peph2zvSyY?t=1655)

- Lepetit 等人提出 **EPnP（efficient PnP）**，複雜度是 $O(n)$——和點數**線性**。
- **核心想法**：不直接用每個點，而是用所有點定義**四個控制點（control points）**，用控制點來解位姿。
  - 四點是線性四點法需要的最少點數。
  - 不管 $n$ 多大，控制點永遠只有 4 個 → 未知數個數固定。
- 先看**四個控制點不共面**的情況。

⚠️ 逐字稿缺字：Whisper 把 EPnP 寫成 “EPMP”、Lepetit 寫成 “lepetti”。講者說論文是 2006 年（開頭說 IJCV 2009）。

**符號** [▶ 29:40](https://youtu.be/9peph2zvSyY?t=1780)：

- $\mathbf{p}_i^w$：第 $i$ 個 3D 點的世界座標（已知）。
- $\mathbf{c}_j^w$，$j=1,\dots,4$：控制點的世界座標。
- 每個點寫成控制點的**加權和**：
$$
\mathbf{p}_i^w=\sum_{j=1}^4\alpha_{ij}\mathbf{c}_j^w,\qquad\sum_{j=1}^4\alpha_{ij}=1
$$
- 在相機座標系用**同樣的權重**：
$$
\mathbf{p}_i^c=\sum_{j=1}^4\alpha_{ij}\mathbf{c}_j^c
$$
- **未知數**：相機座標系的控制點 $\mathbf{c}_j^c$——$4\times3=12$ 個。
- 【口頭】[▶ 31:46](https://youtu.be/9peph2zvSyY?t=1906) 這樣**完全避開了未知深度**：深度的個數隨點數成長，控制點的個數固定。

> 以下**不是逐字稿內容**，是「同樣的權重」為什麼成立：從世界座標到相機座標是剛體變換 $\mathbf{p}^c=R\mathbf{p}^w+\mathbf{t}$。因為 $\sum_j\alpha_{ij}=1$，$R\left(\sum_j\alpha_{ij}\mathbf{c}_j^w\right)+\mathbf{t}=\sum_j\alpha_{ij}(R\mathbf{c}_j^w+\mathbf{t})=\sum_j\alpha_{ij}\mathbf{c}_j^c$。權重和為 1 正是讓平移也能分配進去的條件。

### 4.2 選世界座標的控制點、求權重 α

[▶ 33:05](https://youtu.be/9peph2zvSyY?t=1985)

**選控制點**：

1. $\mathbf{c}_1^w$ = 所有世界點的**重心**。
2. 其他三個沿資料的**主軸（principal axes）**：
   - 共變異數矩陣：$V=\frac{1}{n}\sum_i(\mathbf{p}_i^w-\mathbf{c}_1^w)(\mathbf{p}_i^w-\mathbf{c}_1^w)^\mathsf{T}$（$3\times3$ 對稱）。
   - SVD：$V=U\Sigma U^\mathsf{T}$，$U$ 的三行是三個主軸方向。
   - 用三個主軸定出 $\mathbf{c}_2^w,\mathbf{c}_3^w,\mathbf{c}_4^w$。

> 以下**不是逐字稿內容**：逐字稿說「把三個主軸指定給 $\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_3$」，沒說具體怎麼放。EPnP 論文的常見做法是 $\mathbf{c}_{j+1}^w=\mathbf{c}_1^w+\sqrt{\sigma_j}\,\mathbf{u}_j$（從重心沿主軸方向走一個標準差）。確切做法以論文為準。

**求權重** [▶ 35:43](https://youtu.be/9peph2zvSyY?t=2143)：每個點各有一組 $\alpha_{i1},\dots,\alpha_{i4}$。寫成齊次形式：

$$
\begin{pmatrix}\mathbf{p}_i^w\\1\end{pmatrix}=\begin{pmatrix}\mathbf{c}_1^w&\mathbf{c}_2^w&\mathbf{c}_3^w&\mathbf{c}_4^w\\1&1&1&1\end{pmatrix}\begin{pmatrix}\alpha_{i1}\\\alpha_{i2}\\\alpha_{i3}\\\alpha_{i4}\end{pmatrix}
$$

- 4 條方程式、4 個未知數 → 直接解。
- 最後一列就是 $\sum_j\alpha_{ij}=1$，**不必另外加**。

### 4.3 投影約束：Mx = 0

[▶ 38:02](https://youtu.be/9peph2zvSyY?t=2282)

- 已知像點 $\mathbf{u}_i=(u_i,v_i)$、內參（論文記作 $A$，就是 $K$）。
- 投影：
$$
w_i\begin{pmatrix}u_i\\v_i\\1\end{pmatrix}=A\,\mathbf{p}_i^c=A\sum_{j=1}^4\alpha_{ij}\mathbf{c}_j^c,\qquad A=\begin{pmatrix}f_u&0&u_c\\0&f_v&v_c\\0&0&1\end{pmatrix}
$$
- **消去 $w_i$** [▶ 41:12](https://youtu.be/9peph2zvSyY?t=2472)：第三列給 $w_i=\sum_j\alpha_{ij}z_j^c$（$z_j^c$ 是控制點的 $z$ 座標）。代入前兩列，每個點得 **2 條**方程式：
$$
\begin{aligned}
\sum_j\left(\alpha_{ij}f_u\,x_j^c+\alpha_{ij}(u_c-u_i)\,z_j^c\right)&=0\\
\sum_j\left(\alpha_{ij}f_v\,y_j^c+\alpha_{ij}(v_c-v_i)\,z_j^c\right)&=0
\end{aligned}
$$
- 12 個未知數 $\mathbf{x}=(\mathbf{c}_1^{c\mathsf{T}},\dots,\mathbf{c}_4^{c\mathsf{T}})^\mathsf{T}$；$n$ 個點疊成
$$
M\mathbf{x}=\mathbf{0},\qquad M\in\mathbb{R}^{2n\times12}
$$

（$A$ 的元素和兩條方程式依消去 $w_i$ 的代數寫出；逐字稿只說「代進前兩列得到兩條獨立方程式」。）

### 4.4 為什麼是線性複雜度

[▶ 43:13](https://youtu.be/9peph2zvSyY?t=2593)

- 求 $M$ 的零空間：與其對 $2n\times12$ 的 $M$ 做 SVD，不如對 $M^\mathsf{T}M$（$12\times12$，大小固定）做——右奇異向量一樣。
- 最貴的一步是**算 $M^\mathsf{T}M$ 本身**，時間和 $n$ 成**線性**。
- 所以 EPnP 是 $O(n)$。

### 4.5 用控制點間距離解 β

[▶ 44:31](https://youtu.be/9peph2zvSyY?t=2671)

零空間的維度 $N$ 決定解的形式：$\mathbf{x}=\sum_{k=1}^N\beta_k\mathbf{v}_k$。

**額外約束**：**控制點之間的距離在任何座標系都一樣**：

$$
\|\mathbf{c}_i^c-\mathbf{c}_j^c\|^2=\|\mathbf{c}_i^w-\mathbf{c}_j^w\|^2
$$

- 右邊已知（世界控制點已選好）。
- 4 個控制點 → $\binom{4}{2}=6$ 條約束。

**$N=1$** [▶ 44:45](https://youtu.be/9peph2zvSyY?t=2685)：$\mathbf{x}=\beta\mathbf{v}$。

- 講者說：rank$(M)=11$，每點 2 條 → 需要 5.5 點，即 **6 點以上**時是這種情況。
- 任一對控制點的距離就夠解 $\beta$；用全部 6 對的加權（正規化）組合更穩。

**$N=2$** [▶ 47:49](https://youtu.be/9peph2zvSyY?t=2869)：$\mathbf{x}=\beta_1\mathbf{v}_1+\beta_2\mathbf{v}_2$。

- 講者說：rank$(M)=10$ → 5 點。
- 距離約束對 $\beta_{11}=\beta_1^2$、$\beta_{12}=\beta_1\beta_2$、$\beta_{22}=\beta_2^2$ 是線性的 → 6 條疊成**非齊次**線性方程式
$$
L\boldsymbol{\beta}=\boldsymbol{\rho},\qquad L\in\mathbb{R}^{6\times3},\quad\boldsymbol{\beta}=(\beta_{11},\beta_{12},\beta_{22})^\mathsf{T}
$$
  $\boldsymbol{\rho}$ 是 6 個世界距離的平方。
- 超定 → 用**偽逆**：$\boldsymbol{\beta}=L^+\boldsymbol{\rho}$，再求 $\beta_1,\beta_2$。

**$N=3$** [▶ 50:25](https://youtu.be/9peph2zvSyY?t=3025)：$\mathbf{x}=\beta_1\mathbf{v}_1+\beta_2\mathbf{v}_2+\beta_3\mathbf{v}_3$。

- 講者說：rank 9 → 4.5 點（實務上不會這樣取，通常至少 5 點）。
- 未知的 $\beta_{11},\beta_{12},\beta_{13},\beta_{22},\beta_{23},\beta_{33}$ 共 6 個，6 條約束 → $L$ 是 $6\times6$，$\boldsymbol{\beta}=L^{-1}\boldsymbol{\rho}$。

> 以下**不是逐字稿內容**：講者把 $N$ 和點數直接對應（6 點以上 → $N=1$）。這只在無雜訊、一般位置時成立；EPnP 論文的實際做法是**不管點數，都試 $N=1,2,3,4$**，各自算出位姿，選重投影誤差最小的那個——因為相機接近仿射（焦距長、場景小）時，$M^\mathsf{T}M$ 會有好幾個很小的特徵值，零空間「實際上」不只 1 維。

### 4.6 控制點共面的情況

[▶ 52:18](https://youtu.be/9peph2zvSyY?t=3138)

- 所有 3D 點在一個平面上時，四個控制點也共面，其中一個可以由其他三個表示 → 約束變少。
- 改用**三個**控制點（任三點總決定一個平面）：
  - 未知數 $3\times3=9$ 個，$M$ 變成 $2n\times9$。
  - 距離約束從 6 條減為 **3 條**（$\binom{3}{2}$）→ 只能處理 $N=1$、$N=2$ 兩種情況（同樣的方法）。

### 4.7 最後一步：絕對定向

[▶ 54:15](https://youtu.be/9peph2zvSyY?t=3255)

1. 解出 $\mathbf{c}_j^c$ 後，代回 $\mathbf{p}_i^c=\sum_j\alpha_{ij}\mathbf{c}_j^c$，得到所有點的相機座標。
2. 同一組點在世界座標 $\mathbf{p}_i^w$ 和相機座標 $\mathbf{p}_i^c$ 都知道了 → **絕對定向**（第 21 集）求 $R,\mathbf{t}$。

---

## 5. Lecture 8 總結

[▶ 55:23](https://youtu.be/9peph2zvSyY?t=3323)

1. 定義 PnP 相機位姿估計問題（第 20 集）。
2. **未校正**相機（$K$ 未知）：用 $n$ 對 2D–3D 點或線對應直接求投影矩陣（第 20 集）。
3. **已校正**相機（$K$ 已知）：
   - 三點法（Grunert）、四點法（Quan）：兩階段——先求深度，再用絕對定向求 $R,\mathbf{t}$（第 21 集、本集）。
   - EPnP：用四個控制點，複雜度 $O(n)$（本集）。
4. 退化情況：點全部共線（和相機中心共面）；點和相機中心共面（第 21 集、本集）。

---

## 6. 一頁速查表

### Quan 線性四點法

**在解什麼**：已知 $K$，4 對 2D–3D 對應，求唯一的相機位姿。

**步驟**：

1. 6 條 $f_{ij}(s_i,s_j)=0$ → 3 條 $x=s_1^2$ 的四次多項式。
2. 疊成 $A\mathbf{t}_5=0$（$3\times5$），$\mathbf{t}_5=(x^4,\dots,1)$；零空間 $\mathbf{t}_5=\lambda\mathbf{v}_4+\rho\mathbf{v}_5$。
3. 用 $t_it_j=t_kt_l$（$i+j=k+l$，7 條）→ $B(\lambda^2,\lambda\rho,\rho^2)^\mathsf{T}=0$（$7\times3$）→ $\lambda/\rho$。
4. 加上「1 那個分量等於 1」→ 唯一 $\lambda,\rho$ → $\mathbf{t}_5$ → $x$（比值取平均）→ $s_1=+\sqrt{x}$。
5. 回代其他深度 → 絕對定向。

**什麼時候會失敗**：點共線；點和相機中心共面。$n$ 很大時 $O(n^3)$ 太慢。

### EPnP

**在解什麼**：已知 $K$，$n\ge4$ 對對應，$O(n)$ 求位姿。

**步驟**：

1. 世界控制點：重心 + 三個主軸（共變異數矩陣 SVD）。
2. 每點解 $\begin{pmatrix}\mathbf{p}_i^w\\1\end{pmatrix}=\begin{pmatrix}\mathbf{c}_1^w&\cdots&\mathbf{c}_4^w\\1&\cdots&1\end{pmatrix}\boldsymbol{\alpha}_i$。
3. 每點 2 條：$\sum_j\alpha_{ij}(f_ux_j^c+(u_c-u_i)z_j^c)=0$、$\sum_j\alpha_{ij}(f_vy_j^c+(v_c-v_i)z_j^c)=0$ → $M\mathbf{x}=0$（$2n\times12$）。
4. $M^\mathsf{T}M$（$12\times12$）的零空間：$\mathbf{x}=\sum_k\beta_k\mathbf{v}_k$。
5. 距離約束 $\|\mathbf{c}_i^c-\mathbf{c}_j^c\|=\|\mathbf{c}_i^w-\mathbf{c}_j^w\|$：$N=1$ 直接解；$N=2,3$ 解 $L\boldsymbol{\beta}=\boldsymbol{\rho}$。
6. $\mathbf{p}_i^c=\sum_j\alpha_{ij}\mathbf{c}_j^c$ → 絕對定向。

**共面時**：3 個控制點、$M$ 是 $2n\times9$、3 條距離約束。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| EPnP、P3P + RANSAC | 第 27–30 集（SfM：已知 3D 點時加入新影像） |
| 「把未知量用固定個數的基底表示」 | 第 27–30 集（bundle adjustment 的參數化） |
| 絕對定向 | 第 27–30 集；第 38 集（點雲對齊、ICP） |
| 非透視 PnP | 第 35–37 集（Lecture 12：廣義相機） |

---

## 附：本集一句話總結

> **P3P 最多 4 組解，所以 Quan 用 4 點：三條四次多項式疊成 $A\mathbf{t}_5=0$，再用 $\mathbf{t}_5=(x^4,\dots,1)$ 各分量之間的 $t_it_j=t_kt_l$ 關係線性地解出唯一的深度；這推廣到 $n$ 點但要 $O(n^3)$。EPnP 改成把所有點寫成四個控制點的加權和，只求 12 個控制點座標：每點兩條線性方程式疊成 $M\mathbf{x}=0$，$M^\mathsf{T}M$ 永遠是 $12\times12$，再用控制點間距離不變解出零空間係數——整體 $O(n)$，最後一樣用絕對定向得到 $R,\mathbf{t}$。**

---

## ⚠️ 待確認清單

1. [▶ 18:48](https://youtu.be/9peph2zvSyY?t=1128) Quan 四點法中 $\mathbf{t}_5$ 的分量順序：講者先寫 $(x^4,x^3,x^2,x,1)$，後又說「第一個元素等於 1」，投影片上的實際順序待確認（不影響推導）。

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 8 (Part 3) 錄影逐字稿（Whisper `medium.en`，57:21）整理；MVG 沒有對應內容。*
