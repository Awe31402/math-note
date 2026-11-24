---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 37
lecture: Lecture 12 (Part 3) – Generalized cameras
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/E-YXFI5xzNM
notes: MVG 沒有廣義相機；講者說點對應的部分取自他 2015 年的論文、線對應取自他 2016 年 ECCV 的論文（BRIEF 未列，未查）
---

# 第 37 集 · Lecture 12 (Part 3)：廣義相機的絕對位姿（點對應 gP3P、線對應） [▶ 影片](https://youtu.be/E-YXFI5xzNM)

← 上一集：[36-generalized-cameras-part2](36-generalized-cameras-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[38-point-cloud-processing](38-point-cloud-processing.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 37 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（41:42，Whisper `medium.en` 轉錄）
> **標記說明**：
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 點對應：問題](#1-點對應問題)
- [2. 距離約束](#2-距離約束)
- [3. 消去法解三個 λ](#3-消去法解三個-λ)
- [4. 求位姿、挑解](#4-求位姿挑解)
- [5. 線對應：問題](#5-線對應問題)
- [6. 用 Plücker 線表示 3D 線和影像線](#6-用-plücker-線表示-3d-線和影像線)
- [7. 解旋轉](#7-解旋轉)
- [8. 解平移](#8-解平移)
- [9. 兩種特殊情況](#9-兩種特殊情況)
- [10. Lecture 12 總結](#10-lecture-12-總結)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

廣義相機的**絕對位姿估計**：已知 3D 點（或 3D 線）在世界座標的位置和它們在影像上的像，求多相機系統的位姿。

| 對應 | 最少個數 | 方法 |
|---|---|---|
| 2D–3D **點** | 3 | 距離約束 → 8 次多項式 → 絕對定向 |
| 2D–3D **線** | 8 | 線性：先解 $R$（SVD），再解 $\mathbf{t}$（SVD） |

---

## 1. 點對應：問題

[▶ 00:00](https://youtu.be/E-YXFI5xzNM?t=0)

**給定**：

- 三組 2D–3D 對應：世界座標系 $F_W$ 中的 3D 點 $\mathbf{X}_1,\mathbf{X}_2,\mathbf{X}_3$，和它們的像 $\mathbf{x}_1,\mathbf{x}_2,\mathbf{x}_3$（各自在拍到它的那台相機上）。
- 每台相機相對廣義相機參考座標系 $F_G$ 的外參。

**求**：把多相機座標系 $F_G$ 帶到世界座標系 $F_W$ 的剛體轉換 $R$、$\mathbf{t}$。

和針孔相機的 PnP（第 20–22 集）是同一個問題，只是光線不交於一點。

---

## 2. 距離約束

[▶ 01:47](https://youtu.be/E-YXFI5xzNM?t=107)

**光線上的點**（第 35 集）：第 $i$ 條光線 $(\mathbf{q}_i;\mathbf{q}_i')$ 由外參 $R_{C_i}$、$\mathbf{t}_{C_i}$、像素座標和內參 $K$ 算出。3D 點在 $F_G$ 中是

$$
\mathbf{X}_i^G=\left(\mathbf{q}_i\times\mathbf{q}_i'\right)+\lambda_i\mathbf{q}_i
$$

- $\mathbf{q}_i\times\mathbf{q}_i'$：光線上離參考原點最近的點（從原點到光線的垂足）。
- $\lambda_i$：從那個點沿光線的**有號距離**。點要在相機前面，$\lambda_i$ 必須**為正**。

**距離不變** [▶ 03:32](https://youtu.be/E-YXFI5xzNM?t=212)：三個點兩兩的距離 $d_{12}$、$d_{23}$、$d_{13}$ 和用哪個座標系表示無關：

$$
\left\|\mathbf{X}_i^W-\mathbf{X}_j^W\right\|^2=\left\|\mathbf{X}_i^G-\mathbf{X}_j^G\right\|^2
$$

- 左邊：已知（世界座標給定）。
- 右邊代入光線上的點：
$$
d_{ij}^2=\left\|\left(\mathbf{q}_i\times\mathbf{q}_i'\right)+\lambda_i\mathbf{q}_i-\left(\mathbf{q}_j\times\mathbf{q}_j'\right)-\lambda_j\mathbf{q}_j\right\|^2
$$
- Plücker 座標都已知 → 唯一的未知數是 $\lambda$。
- 三對點 → **三條方程式、三個未知數** $\lambda_1,\lambda_2,\lambda_3$。

**展開** [▶ 06:09](https://youtu.be/E-YXFI5xzNM?t=369)：得三條多項式方程式 (A)、(B)、(C)，係數 $k$ 由已知的 $\mathbf{q}_i$、$\mathbf{q}_i'$ 和世界點間的距離組成。

> 以下**不是逐字稿內容**，是展開後的形狀：令 $\mathbf{b}_i=\mathbf{q}_i\times\mathbf{q}_i'$、$\|\mathbf{q}_i\|=1$，
> $$
> \lambda_i^2+\lambda_j^2-2\left(\mathbf{q}_i\cdot\mathbf{q}_j\right)\lambda_i\lambda_j+2\left(\mathbf{b}_i-\mathbf{b}_j\right)\cdot\left(\lambda_i\mathbf{q}_i-\lambda_j\mathbf{q}_j\right)+\left\|\mathbf{b}_i-\mathbf{b}_j\right\|^2-d_{ij}^2=0
> $$
> 每條都是兩個 $\lambda$ 的二次式。和針孔相機的 P3P（第 20 集 Grunert）比，多了一次項——因為光線不從同一點出發（$\mathbf{b}_i\ne\mathbf{b}_j$）。若所有 $\mathbf{b}_i=\mathbf{0}$，就退回 P3P 的形式（$\lambda_i$ 即到光心的距離）。

---

## 3. 消去法解三個 λ

[▶ 06:54](https://youtu.be/E-YXFI5xzNM?t=414)

**在解什麼**：三條二次方程式 (A)(B)(C) 的共同解。

**步驟**：

1. **從 (A)、(B) 消去 $\lambda_1$**：兩式都把 $\lambda_1$ 寫成主角，令它們相等 → 只含 $\lambda_2,\lambda_3$ 的多項式 $f(\lambda_2,\lambda_3)=0$。
2. **和 (C) 消去 $\lambda_2$** [▶ 08:07](https://youtu.be/E-YXFI5xzNM?t=487)：(C) 也只含 $\lambda_2,\lambda_3$ → 再消一次 → **只含 $\lambda_3$ 的一元多項式**，**8 次**：
$$
A\lambda_3^8+B\lambda_3^7+C\lambda_3^6+D\lambda_3^5+E\lambda_3^4+F\lambda_3^3+G\lambda_3^2+H\lambda_3+I=0
$$
   係數 $A,\dots,I$ 由已知的 $k$ 組成。
3. **解 $\lambda_3$** [▶ 09:13](https://youtu.be/E-YXFI5xzNM?t=553)：用**伴隨矩陣（companion matrix）**（第 20 集）。$8\times8$ 矩陣的 8 個特徵值 = 8 個根。
4. **回代求 $\lambda_2$** [▶ 09:48](https://youtu.be/E-YXFI5xzNM?t=588)：得到 $\lambda_2$ 的**二次方程式** → 配方法，2 個解。
5. **回代求 $\lambda_1$**：同樣是二次式，2 個解。

**解的個數** [▶ 10:47](https://youtu.be/E-YXFI5xzNM?t=647)：$8\times2\times2=32$ 組。

**淘汰** [▶ 11:09](https://youtu.be/E-YXFI5xzNM?t=669)：解多項式的根不保證是實數或正數。一組 $(\lambda_1,\lambda_2,\lambda_3)$ 只要有一個是**虛數或負數**就丟掉（$\lambda$ 是有號距離，必須為正）。實務上大部分的解都會被這樣淘汰。

**什麼時候會失敗**：三個點的配置使消去後的多項式係數退化；或剩下多組可行解無法分辨（下一節用額外的點挑）。（講者沒細講退化配置。）

---

## 4. 求位姿、挑解

[▶ 12:05](https://youtu.be/E-YXFI5xzNM?t=725)

1. 有了 $\lambda_1,\lambda_2,\lambda_3$ → 代回 $\mathbf{X}_i^G=(\mathbf{q}_i\times\mathbf{q}_i')+\lambda_i\mathbf{q}_i$，得三個點在 $F_G$ 的座標。
2. 現在同三個點有兩組座標（$F_W$ 和 $F_G$）→ **絕對定向（absolute orientation）**（第 21 集）求 $R$、$\mathbf{t}$。
3. **挑解** [▶ 13:34](https://youtu.be/E-YXFI5xzNM?t=814)：可能剩 $n$ 組可行解 $(R_1,\mathbf{t}_1),\dots,(R_n,\mathbf{t}_n)$。
   - 對每組解，把其他 3D 點從世界座標轉到相機座標，重投影回影像，算重投影誤差。
   - 誤差小於門檻的算**內點（inlier）**。
   - 內點最多的那組就是正確解。

---

## 5. 線對應：問題

[▶ 15:13](https://youtu.be/E-YXFI5xzNM?t=913)

- 和點的版本一樣，只是把 2D–3D **點**對應換成 2D–3D **線**對應：
  - $\mathbf{L}_j^W$：第 $j$ 條 3D 線，在世界座標 $F_W$。
  - $\mathbf{l}_j^C$：它在相機 $C$ 影像上的 2D 線。
- 例：三台相機剛性裝在一起，參考座標系 $F_G$，外參已知。
- **求**：$F_W$ 和 $F_G$ 之間的 $4\times4$ 剛體轉換 $\begin{pmatrix}R&\mathbf{t}\\\mathbf{0}_{1\times3}&1\end{pmatrix}$。

⚠️ 逐字稿缺字 [▶ 16:48](https://youtu.be/E-YXFI5xzNM?t=1008)：講者說投影片的 $4\times4$ 矩陣最後一列寫錯了，應是 $\mathbf{0}_{1\times3}$。

**記號**：$R_{WG}$、$\mathbf{t}_{WG}$ 把 $F_W$ 的點轉到 $F_G$（未知）；$R_{GC}$、$\mathbf{t}_{GC}$ 把 $F_G$ 的點轉到相機 $F_C$（外參，已知）。合起來

$$
R_{WC}=R_{GC}R_{WG},\qquad\mathbf{t}_{WC}=R_{GC}\mathbf{t}_{WG}+\mathbf{t}_{GC}
$$

（逐字稿的下標方向前後不一，例如有時說「$T_G^W$ 把廣義座標轉到世界」、有時說「把世界轉到相機」；本筆記統一用上面的定義。）

---

## 6. 用 Plücker 線表示 3D 線和影像線

### 3D 線

[▶ 17:47](https://youtu.be/E-YXFI5xzNM?t=1067)

- 這裡**不**用像素光線，而是直接用 Plücker 座標表示場景中的 3D 線和影像上的線。
- 3D 線段的兩個端點（世界座標，齊次）：$\mathbf{P}_A^W=(P_{Ax},P_{Ay},P_{Az},1)^\mathsf{T}$、$\mathbf{P}_B^W$。
- **這一節的 Plücker 向量把矩放前面**：
$$
\mathbf{L}^W=\begin{pmatrix}\mathbf{u}^W\\\mathbf{v}^W\end{pmatrix},\qquad\mathbf{v}^W=\frac{\mathbf{P}_B-\mathbf{P}_A}{\left\|\mathbf{P}_B-\mathbf{P}_A\right\|},\qquad\mathbf{u}^W=\mathbf{P}_A\times\mathbf{v}^W
$$
  （$\mathbf{P}_A$、$\mathbf{P}_B$ 在這裡取非齊次的 3 維部分。）

**轉到相機座標** [▶ 21:07](https://youtu.be/E-YXFI5xzNM?t=1267)：用 $6\times6$ 的 Plücker 轉換（矩在前的版本）：

$$
\mathbf{L}^C=\begin{pmatrix}R_{WC}&\left[\mathbf{t}_{WC}\right]_\times R_{WC}\\\mathbf{0}&R_{WC}\end{pmatrix}\mathbf{L}^W
$$

$$
\mathbf{U}^C=R_{WC}\mathbf{u}^W+\left[\mathbf{t}_{WC}\right]_\times R_{WC}\mathbf{v}^W,\qquad\mathbf{V}^C=R_{WC}\mathbf{v}^W
$$

（各塊依第 35 集的推導、配合矩在前的順序寫出；逐字稿只說「這是 Plücker 線的 $6\times6$ 轉換矩陣」。）

- $R_{WC}$、$\mathbf{t}_{WC}$ 可以分解成「世界 → 廣義」（未知）和「廣義 → 相機」（外參）兩個轉換的乘積。
- 同一條 Plücker 線的方向和矩**互相垂直**：$\mathbf{U}^C\cdot\mathbf{V}^C=0$。

### 影像線

[▶ 28:10](https://youtu.be/E-YXFI5xzNM?t=1690)

- 影像線兩個端點的**相機正規化座標** $\hat{\mathbf{p}}_A$、$\hat{\mathbf{p}}_B$（齊次）。
- 同樣寫成 Plücker 形式：
$$
\mathbf{v}^c=\frac{\hat{\mathbf{p}}_B-\hat{\mathbf{p}}_A}{\left\|\hat{\mathbf{p}}_B-\hat{\mathbf{p}}_A\right\|},\qquad\mathbf{u}^c=\hat{\mathbf{p}}_A\times\mathbf{v}^c
$$

**關鍵：$\mathbf{u}^c\parallel\mathbf{U}^C$** [▶ 31:04](https://youtu.be/E-YXFI5xzNM?t=1864)：

- 光心和 3D 線（或和影像線）張成一個**反投影平面**。
- $\mathbf{U}^C$（3D 線在相機座標的矩）是光心（原點）到線的向量與方向的外積 → 垂直於這個平面，是**平面的法向量**。
- $\mathbf{u}^c$（影像線的矩）同理，也是同一個平面的法向量。
- → 兩者**平行**：$\mathbf{U}^C=\lambda\,\mathbf{u}^c$。

---

## 7. 解旋轉

[▶ 30:06](https://youtu.be/E-YXFI5xzNM?t=1806)

**約束**：$\mathbf{U}^C\perp\mathbf{V}^C$，且 $\mathbf{U}^C\parallel\mathbf{u}^c$ → 用已知的 $\mathbf{u}^c$ 取代 $\mathbf{U}^C$：

$$
\mathbf{u}^{c\mathsf{T}}R_{WC}\mathbf{v}^W=0\quad\Longrightarrow\quad\mathbf{u}^{c\mathsf{T}}R_{GC}\,R_{WG}\,\mathbf{v}^W=0
$$

- 唯一的未知數是 $R_{WG}$（9 個元素）。
- 直覺：3D 線轉到相機座標後，方向一定**躺在反投影平面裡**，所以和平面法向量垂直。

**線性化** [▶ 33:12](https://youtu.be/E-YXFI5xzNM?t=1992)：

$$
\mathbf{a}^\mathsf{T}\mathbf{r}=0,\qquad\mathbf{r}=\mathrm{vec}\left(R_{WG}\right)\in\mathbb{R}^9
$$

- $\mathbf{a}^\mathsf{T}$（$1\times9$）由已知的 $\mathbf{u}^c$、$R_{GC}$、$\mathbf{v}^W$ 組成。
- **8 條以上**線對應疊成 $A\mathbf{r}=\mathbf{0}$（$A\in\mathbb{R}^{n\times9}$）→ SVD，取最小奇異值對應的右奇異向量。

> 以下**不是逐字稿內容**，是 $\mathbf{a}$ 的具體形式和一個實務補充：
> - 由 $\mathbf{p}^\mathsf{T}M\mathbf{q}=\left(\mathbf{q}^\mathsf{T}\otimes\mathbf{p}^\mathsf{T}\right)\mathrm{vec}(M)$（$\mathrm{vec}$ 按行堆疊），取 $\mathbf{p}=R_{GC}^\mathsf{T}\mathbf{u}^c$、$\mathbf{q}=\mathbf{v}^W$，得 $\mathbf{a}^\mathsf{T}=\mathbf{v}^{W\mathsf{T}}\otimes\left(R_{GC}^\mathsf{T}\mathbf{u}^c\right)^\mathsf{T}$。
> - SVD 的解只到一個尺度、也不保證是正交矩陣。實務上要再定尺度和正負號（例如令行列式為 $+1$），並投影到最近的旋轉矩陣（對 $3\times3$ 的解做 SVD $U\Sigma V^\mathsf{T}$，取 $UV^\mathsf{T}$）。逐字稿沒講這一步。

---

## 8. 解平移

[▶ 35:03](https://youtu.be/E-YXFI5xzNM?t=2103)

$R_{WG}$ 已知後：

1. 寫出平行關係 $\lambda\,\mathbf{u}^c=\mathbf{U}^C=R_{WC}\mathbf{u}^W+\left[\mathbf{t}_{WC}\right]_\times R_{WC}\mathbf{v}^W$，未知數是 $\lambda$ 和 $\mathbf{t}_{WC}$。
2. **消去 $\lambda$** [▶ 36:07](https://youtu.be/E-YXFI5xzNM?t=2167)：兩邊和 $\mathbf{u}^c$ 做外積（$\mathbf{u}^c\times\mathbf{u}^c=\mathbf{0}$）：
$$
\mathbf{u}^c\times\left(R_{WC}\mathbf{u}^W+\left[\mathbf{t}_{WC}\right]_\times R_{WC}\mathbf{v}^W\right)=\mathbf{0}
$$
3. 代 $\mathbf{t}_{WC}=R_{GC}\mathbf{t}_{WG}+\mathbf{t}_{GC}$（$\mathbf{t}_{GC}$ 是已知外參）→ 對 $\mathbf{t}_{WG}$ **線性**。
4. **疊起來** [▶ 36:32](https://youtu.be/E-YXFI5xzNM?t=2192)：8 條以上的對應（可以就是解旋轉用的那幾條）→
$$
B\begin{pmatrix}t_x\\t_y\\t_z\\1\end{pmatrix}=\mathbf{0}
$$
5. SVD → $\alpha\mathbf{v}$，令第 4 個元素 $=1$ 解出 $\alpha$ → **唯一**的 $\mathbf{t}$，沒有模糊。

---

## 9. 兩種特殊情況

[▶ 38:15](https://youtu.be/E-YXFI5xzNM?t=2295)

1. **只有一台相機**：所有線都由同一台相機看到 → 外參那一步消失，把廣義參考座標系對齊這台相機（$R_{GC}=I$、$\mathbf{t}_{GC}=\mathbf{0}$），其餘步驟不變。
2. **平行的 3D 線** [▶ 39:20](https://youtu.be/E-YXFI5xzNM?t=2360)：所有線的方向 $\mathbf{v}^W$ 都一樣 → $A$ 的秩**低於 8** → $R_{WG}$ 解不唯一。
   - 解法：選用來解方程式的 8 條線時，**檢查它們不互相平行**，略掉平行的那些。

⚠️ 逐字稿缺字 [▶ 39:41](https://youtu.be/E-YXFI5xzNM?t=2381)：Whisper 寫「rank of A will drop below A」，應是「drop below **8**」。

---

## 10. Lecture 12 總結

[▶ 40:38](https://youtu.be/E-YXFI5xzNM?t=2438)

1. 用 Plücker 線推導雙視角廣義相機的極線幾何（第 35 集）。
2. 用線性 17 點法求相對位姿（第 35 集）。
3. 17 點法的三種退化：局部中心投影、軸向相機、兩者合併；以及退化時唯一求出相對旋轉和平移的演算法（第 36 集）。
4. 用 2D–3D 點或線對應求廣義相機的絕對位姿（本集）。

---

## 11. 一頁速查表

### 點對應（廣義 P3P）

| 步驟 | 公式 | 關鍵一步 |
|---|---|---|
| 光線上的點 | $\mathbf{X}_i^G=(\mathbf{q}_i\times\mathbf{q}_i')+\lambda_i\mathbf{q}_i$，$\lambda_i>0$ | — |
| 距離約束 | $\|\mathbf{X}_i^G-\mathbf{X}_j^G\|^2=d_{ij}^2$，3 條 | 距離與座標系無關 |
| 消去 | (A)(B) 消 $\lambda_1$ → $f(\lambda_2,\lambda_3)$；和 (C) 消 $\lambda_2$ → $\lambda_3$ 的 8 次式 | 伴隨矩陣 |
| 解數 | $8\times2\times2=32$；丟掉虛數、負數 | $\lambda$ 是正的有號距離 |
| 位姿 | 絕對定向；內點最多者 | — |

### 線對應

| 步驟 | 公式 | 關鍵一步 |
|---|---|---|
| 3D 線 | $\mathbf{L}^W=(\mathbf{u}^W;\mathbf{v}^W)$，$\mathbf{u}^W=\mathbf{P}_A\times\mathbf{v}^W$ | 矩在前 |
| 轉換 | $\mathbf{U}^C=R_{WC}\mathbf{u}^W+[\mathbf{t}_{WC}]_\times R_{WC}\mathbf{v}^W$，$\mathbf{V}^C=R_{WC}\mathbf{v}^W$ | — |
| 影像線 | $\mathbf{u}^c=\hat{\mathbf{p}}_A\times\mathbf{v}^c$ | — |
| 平行 | $\mathbf{U}^C=\lambda\mathbf{u}^c$ | 都是反投影平面的法向量 |
| 旋轉 | $\mathbf{u}^{c\mathsf{T}}R_{GC}R_{WG}\mathbf{v}^W=0$ → $A\,\mathrm{vec}(R_{WG})=0$，≥8 條，SVD | $\mathbf{U}^C\perp\mathbf{V}^C$ |
| 平移 | $\mathbf{u}^c\times\mathbf{U}^C=0$ → $B(t_x,t_y,t_z,1)^\mathsf{T}=0$，SVD，第 4 元素 $=1$ | 外積消去 $\lambda$ |
| 特殊 | 單相機：外參 = 單位；平行線：秩 < 8，略掉 | — |

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 位姿估計（相機 → 世界） | 第 38 集（點雲配準：兩組點雲之間的剛體轉換） |
| 絕對定向 | 第 38 集（ICP 的每一步就是絕對定向） |

---

## 附：本集一句話總結

> **廣義相機的絕對位姿：用點時，把三個 3D 點寫成各自光線上的點 $(\mathbf{q}_i\times\mathbf{q}_i')+\lambda_i\mathbf{q}_i$，利用兩兩距離不隨座標系改變得三條二次方程式，消去成 $\lambda_3$ 的 8 次多項式，共 32 組解、丟掉虛數和負數，再用絕對定向得位姿、以內點數挑解；用線時，3D 線轉到相機座標後的矩和影像線的矩都是反投影平面的法向量，所以 $\mathbf{u}^{c\mathsf{T}}R_{GC}R_{WG}\mathbf{v}^W=0$ 對旋轉線性，8 條以上的線用 SVD 解 $R$，再用外積消去尺度、線性解出 $\mathbf{t}$；平行的 3D 線會讓秩不足，要略掉。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 12 (Part 3) 錄影逐字稿（Whisper `medium.en`，41:42）整理；MVG 無對應章節。*
