---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 21
lecture: Lecture 8 (Part 2) – Absolute pose estimation from points or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/8Nh1UeuD9-k
notes: 本集內容講者取自 Haralick 等人（IJCV 1994）回顧的 Grunert (1841) P3P 解法，以及〈Space resection: failure cases〉（1966）的退化分析；BRIEF 沒列這些論文，未查。MVG 沒有 P3P。
---

# 第 21 集 · Lecture 8 (Part 2)：已校正相機——Grunert P3P、絕對定向、退化情況 [▶ 影片](https://youtu.be/8Nh1UeuD9-k)

← 上一集：[20-absolute-pose-part1](20-absolute-pose-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[22-absolute-pose-part3](22-absolute-pose-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 21 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（43:02，Whisper `medium.en` 轉錄）；MVG 沒有對應內容，依 BRIEF 只靠逐字稿
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 已校正相機的兩階段做法](#1-已校正相機的兩階段做法)
- [2. 為什麼最少 3 個點](#2-為什麼最少-3-個點)
- [3. Grunert 三點法（P3P）](#3-grunert-三點法p3p)
  - [3.1 已知量：邊長與光線夾角](#31-已知量邊長與光線夾角)
  - [3.2 餘弦定理三條方程式](#32-餘弦定理三條方程式)
  - [3.3 消元成四次多項式](#33-消元成四次多項式)
  - [3.4 用伴隨矩陣求根](#34-用伴隨矩陣求根)
- [4. 絕對定向：對齊兩組 3D 點](#4-絕對定向對齊兩組-3d-點)
- [5. 退化情況](#5-退化情況)
  - [5.1 穩定性的判準：Jacobian 不能奇異](#51-穩定性的判準jacobian-不能奇異)
  - [5.2 兩種退化](#52-兩種退化)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/8Nh1UeuD9-k?t=0)

- 上一集：**未校正**相機（$K$ 未知）。
- 這集：**已校正**相機——$K$ 已知（焦距、主點都知道）。
- 講者要講三個方法（橫跨約 150 年），本集講第一個：Grunert 的三點法；Quan 四點法和 EPnP 在下一集。
- 【口頭】三個方法來自三篇論文，講者沿用各論文的符號，所以符號會有點混用（和上一集用 MVG 的符號不同）。

⚠️ 逐字稿缺字：Whisper 把 Hartley 寫成 “Tapley”、Grunert 寫成 “Gounet”、“Grunet”、“Granette”。

---

## 1. 已校正相機的兩階段做法

[▶ 01:05](https://youtu.be/8Nh1UeuD9-k?t=65)

符號（依 Haralick 等人的論文）：3D 點 $\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3$（世界座標），相機中心 $\mathbf{p}$。

1. **第一階段：求未知深度** $s_1,s_2,s_3$——相機中心到各點的距離 $s_i=\|\mathbf{p}_i-\mathbf{p}\|$。
   - 有了深度，就能寫出這三點在**相機座標系**的座標 $\mathbf{p}_i^C$。
2. **第二階段：絕對定向（absolute orientation）**——同樣三個點，一組在世界座標（已知）、一組在相機座標（剛算出），求對齊兩者的 $R$、$\mathbf{t}$。

---

## 2. 為什麼最少 3 個點

[▶ 04:02](https://youtu.be/8Nh1UeuD9-k?t=242)

- 未知的剛體變換：$R$ 3 個自由度（roll、pitch、yaw）+ $\mathbf{t}$ 3 個（$t_x,t_y,t_z$，有絕對尺度）= **6**。
- 每對 2D–3D 對應給 **2** 個獨立約束（上一集）。
- 所以最少 **3** 對對應點 → **P3P（perspective-3-point）**問題。
- 這個解法是德國科學家 **Grunert** 在 **1841** 年提出的（講者說約 150–160 年前；一位攝影測量學家）。

---

## 3. Grunert 三點法（P3P）

### 3.1 已知量：邊長與光線夾角

[▶ 05:53](https://youtu.be/8Nh1UeuD9-k?t=353)

**三角形的邊長**（從已知的 3D 點算）：

$$
a=\|\mathbf{p}_2-\mathbf{p}_3\|,\qquad b=\|\mathbf{p}_1-\mathbf{p}_3\|,\qquad c=\|\mathbf{p}_1-\mathbf{p}_2\|
$$

**像點**：$\mathbf{q}_i=(u_i,v_i)$（像素座標）。假設主點 $c_x=c_y=0$（影像中心為原點）：

$$
u_i=f\frac{x_i}{z_i},\qquad v_i=f\frac{y_i}{z_i}
$$

**光線的單位方向** [▶ 08:33](https://youtu.be/8Nh1UeuD9-k?t=513)：

$$
\mathbf{j}_i=\frac{1}{\sqrt{u_i^2+v_i^2+f^2}}\begin{pmatrix}u_i\\v_i\\f\end{pmatrix}
$$

（從相機中心指向像點 $\mathbf{q}_i$ 的單位向量。$K$ 已知 → $f$ 已知 → $\mathbf{j}_i$ 已知。）

**光線夾角** [▶ 09:20](https://youtu.be/8Nh1UeuD9-k?t=560)：

$$
\cos\alpha=\mathbf{j}_2\cdot\mathbf{j}_3,\qquad\cos\beta=\mathbf{j}_1\cdot\mathbf{j}_3,\qquad\cos\gamma=\mathbf{j}_1\cdot\mathbf{j}_2
$$

（$\alpha$ 是光線 2、3 的夾角，以此類推。）

**未知深度**：$\mathbf{p}_i$（在相機座標系）$=s_i\,\mathbf{j}_i$。

> 以下**不是逐字稿內容**，是一般主點的情況：$\mathbf{j}_i\propto K^{-1}(u_i,v_i,1)^\mathsf{T}$（第 14 集的光線方向）。主點為 0、無斜切、$f_x=f_y=f$ 時，$K^{-1}(u,v,1)^\mathsf{T}=(u/f,v/f,1)^\mathsf{T}\propto(u,v,f)^\mathsf{T}$，就是上式。

### 3.2 餘弦定理三條方程式

[▶ 11:40](https://youtu.be/8Nh1UeuD9-k?t=700)

相機中心和任兩個 3D 點組成一個三角形。以光線 2、3 為例：兩邊長 $s_2,s_3$（未知）、夾角 $\alpha$（已知）、對邊 $a$（已知）。**餘弦定理**：

$$
\begin{aligned}
s_2^2+s_3^2-2s_2s_3\cos\alpha&=a^2\\
s_1^2+s_3^2-2s_1s_3\cos\beta&=b^2\\
s_1^2+s_2^2-2s_1s_2\cos\gamma&=c^2
\end{aligned}
$$

- 三條方程式、三個未知數 $s_1,s_2,s_3$。

（方程式依講者描述的餘弦定理寫出；逐字稿只說「由餘弦定理得到這三條」。）

### 3.3 消元成四次多項式

[▶ 14:35](https://youtu.be/8Nh1UeuD9-k?t=875)

**Grunert 的技巧**：引入兩個輔助變數 $u,v$：

$$
s_2=u\,s_1,\qquad s_3=v\,s_1
$$

代入三條方程式，每條都把 $s_1^2$ 提出來，解成 $s_1^2$ 的形式：

$$
s_1^2=\frac{a^2}{u^2+v^2-2uv\cos\alpha}=\frac{b^2}{1+v^2-2v\cos\beta}=\frac{c^2}{1+u^2-2u\cos\gamma}
$$

（上式依代入後的代數整理寫出；逐字稿只說「把每條整理成 $s_1$ 為主體」。）

- 第一、二式相等 → 一條 $u,v$ 的方程式；第二、三式相等 → 另一條。（講者的編號是式 (6)、(7)。）
- 兩條方程式、兩個未知數 $u,v$。
- 從一條解出 $u$、代入另一條，**消去 $u$**，得到 $v$ 的**四次單變數多項式**：
$$
A_4v^4+A_3v^3+A_2v^2+A_1v+A_0=0
$$
- 係數 $A_i$ 是 $a,b,c,\cos\alpha,\cos\beta,\cos\gamma$ 的複雜式子；講者不推導，說有興趣可以自己驗證。

### 3.4 用伴隨矩陣求根

[▶ 16:57](https://youtu.be/8Nh1UeuD9-k?t=1017)

- 四次多項式最多有 **4 個實根**。
- 一種解法：**伴隨矩陣（companion matrix）**——把係數放進最後一行：
$$
C=\begin{pmatrix}0&0&0&-A_0/A_4\\1&0&0&-A_1/A_4\\0&1&0&-A_2/A_4\\0&0&1&-A_3/A_4\end{pmatrix}
$$
- **$C$ 的特徵值就是多項式的根**。$4\times4$ → 4 個特徵值 → 4 個解。
- 講者不推導，把它當成解四次方程式的工具。

（伴隨矩陣的元素依標準形式寫出；逐字稿只說「係數代進伴隨矩陣的最後一行」。）

> 以下**不是逐字稿內容**，是「特徵值 = 根」的一行理由：$\det(\lambda I-C)=\lambda^4+\frac{A_3}{A_4}\lambda^3+\frac{A_2}{A_4}\lambda^2+\frac{A_1}{A_4}\lambda+\frac{A_0}{A_4}$（沿最後一行展開可驗證），和原多項式只差一個 $A_4$ 倍數。

**回代** [▶ 19:01](https://youtu.be/8Nh1UeuD9-k?t=1141)：

1. 保留**實根** $v$。
2. 每個 $v$ 代回 (7) 解出 $u$ → 最多 4 組 $(u,v)$。
3. 代回 (5)（$s_1^2$ 的式子）求 $s_1$。
4. $s_2=us_1$、$s_3=vs_1$。
5. 相機座標系下的 3D 點：$\mathbf{p}_i'=s_i\mathbf{j}_i$。

- P3P 最多有 **4 組解**。

> 以下**不是逐字稿內容**，是實務補充：要挑出正確的解，通常用第 4 個點（重投影誤差最小的那組），或在 RANSAC 中用其他點的共識來挑。

---

## 4. 絕對定向：對齊兩組 3D 點

[▶ 21:10](https://youtu.be/8Nh1UeuD9-k?t=1270)

**問題**：$\mathbf{p}_i$（世界座標，已知）和 $\mathbf{p}_i'$（相機座標，剛求出）是同樣的點，求對齊兩者的剛體變換：

$$
\min_{R,\mathbf{t}}\ \sum_i\left\|\mathbf{p}_i-(R\mathbf{p}_i'+\mathbf{t})\right\|^2
$$

- Grunert 法只用 3 點，但**絕對定向對 3 個以上的點都適用**。

**步驟** [▶ 22:53](https://youtu.be/8Nh1UeuD9-k?t=1373)：

1. **去掉平移**：算兩組點的**重心**
$$
\bar{\mathbf{p}}=\frac{1}{n}\sum_i\mathbf{p}_i,\qquad\bar{\mathbf{p}}'=\frac{1}{n}\sum_i\mathbf{p}_i'
$$
   各自減掉重心：$\mathbf{r}_i=\mathbf{p}_i-\bar{\mathbf{p}}$、$\mathbf{r}_i'=\mathbf{p}_i'-\bar{\mathbf{p}}'$。現在兩組只差一個旋轉。
2. **算 $3\times3$ 矩陣**：
$$
M=\sum_i\mathbf{r}_i'\,\mathbf{r}_i^\mathsf{T}
$$
   （每點 $3\times1$ 乘 $1\times3$ 得 $3\times3$，全部加起來。）
3. **旋轉**：
$$
R=M\,Q^{-1/2},\qquad Q=M^\mathsf{T}M
$$
4. **平移**：補償旋轉之後，對齊兩組點的重心（例如 $\mathbf{t}=\bar{\mathbf{p}}-R\bar{\mathbf{p}}'$）。

**怎麼算 $Q^{-1/2}$** [▶ 27:06](https://youtu.be/8Nh1UeuD9-k?t=1626)：

- $Q=M^\mathsf{T}M$ 是**對稱**的 $3\times3$ 矩陣，SVD 寫成 $Q=V\Sigma V^\mathsf{T}$（左右一樣），$\Sigma=\mathrm{diag}(\lambda_1,\lambda_2,\lambda_3)$。
- $Q^{-1/2}=V\,\mathrm{diag}\left(\lambda_1^{-1/2},\lambda_2^{-1/2},\lambda_3^{-1/2}\right)V^\mathsf{T}$。

⚠️ 待確認 [▶ 25:05](https://youtu.be/8Nh1UeuD9-k?t=1505)：$M$ 和 $R$ 的方向。逐字稿說 $M=\sum\mathbf{r}_i'\mathbf{r}_i^\mathsf{T}$（相機點 × 世界點的轉置）、$R=MQ^{-1/2}$；平移那一步的寫法聽不清楚。

> 以下**不是逐字稿內容**，是依代數推論的方向檢查：令 $M=U\Sigma V^\mathsf{T}$，則 $MQ^{-1/2}=U\Sigma V^\mathsf{T}\cdot V\Sigma^{-1}V^\mathsf{T}=UV^\mathsf{T}$（$M$ 的極分解的正交部分）。最小化 $\sum\|\mathbf{r}_i-R\mathbf{r}_i'\|^2$ 等價於最大化 $\operatorname{tr}\left(R\sum\mathbf{r}_i'\mathbf{r}_i^\mathsf{T}\right)=\operatorname{tr}(RM)$，最大值在 $R=VU^\mathsf{T}=(UV^\mathsf{T})^\mathsf{T}$。所以若 $M=\sum\mathbf{r}_i'\mathbf{r}_i^\mathsf{T}$，**相機 → 世界**的旋轉是 $(MQ^{-1/2})^\mathsf{T}$；$MQ^{-1/2}$ 本身是世界 → 相機。投影片上哪一個是 $R$、平移怎麼寫，要看投影片確認。另外，若 $\det(UV^\mathsf{T})=-1$（點有雜訊或接近共面時可能發生），得到的是鏡射，要修正。

---

## 5. 退化情況

### 5.1 穩定性的判準：Jacobian 不能奇異

[▶ 28:38](https://youtu.be/8Nh1UeuD9-k?t=1718)

**換個角度看**：

- 第一階段把 $s_1,s_2,s_3$ 當未知數。
- 也可以把 $s_1,s_2,s_3$ 固定，把**相機中心 $(x,y,z)$** 當未知數——這其實就是第二階段在解的東西（$R,\mathbf{t}$ 決定相機中心）。
- 三條方程式改寫成相機中心的三條多項式方程式（講者說推導很複雜，跳過）：
$$
f_1(x,y,z)=0,\quad f_2(x,y,z)=0,\quad f_3(x,y,z)=0
$$

**一般的判準** [▶ 30:54](https://youtu.be/8Nh1UeuD9-k?t=1854)：$n$ 個未知數 $x_1,\dots,x_n$、$n$ 條方程式 $f_i(x_1,\dots,x_n)=0$。

- **解是穩定的（非退化）**：對函數做小擾動時，解不會「滑走」。
- **全微分（total derivative）** [▶ 33:39](https://youtu.be/8Nh1UeuD9-k?t=2019)：用連鎖律
$$
\frac{df_i}{dt}=\frac{\partial f_i}{\partial x_1}\frac{dx_1}{dt}+\cdots+\frac{\partial f_i}{\partial x_n}\frac{dx_n}{dt}
\quad\Longrightarrow\quad df_i=\sum_j\frac{\partial f_i}{\partial x_j}dx_j
$$
  （兩邊的 $dt$ 約掉。）
- 寫成矩陣：
$$
\begin{pmatrix}df_1\\\vdots\\df_n\end{pmatrix}=\underbrace{\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\cdots&\frac{\partial f_1}{\partial x_n}\\\vdots&&\vdots\\\frac{\partial f_n}{\partial x_1}&\cdots&\frac{\partial f_n}{\partial x_n}\end{pmatrix}}_{J}\begin{pmatrix}dx_1\\\vdots\\dx_n\end{pmatrix}
$$
- 方程式一直等於 0，所以 $df_i=0$：$J\,d\mathbf{x}=\mathbf{0}$。
- **穩定** ⟺ 唯一解是 $d\mathbf{x}=\mathbf{0}$ ⟺ **$J$ 滿秩**。
- 若 $J$ 奇異，就有非零的 $d\mathbf{x}$ 滿足 $J\,d\mathbf{x}=\mathbf{0}$——解可以沿某個方向移動而方程式仍成立 → 一整族解，或解不穩定。

### 5.2 兩種退化

[▶ 36:20](https://youtu.be/8Nh1UeuD9-k?t=2180)

對 Grunert 的三條方程式取全微分（結果直接引自論文，講者不推導）：

$$
M\begin{pmatrix}dx\\dy\\dz\end{pmatrix}=\mathbf{0},\qquad M=AB
$$

- $A$：$3\times3$，各列是**相機中心減各 3D 點**的座標差（$x-x_i$、$y-y_i$、$z-z_i$）。
- $B$：由 $s_1,s_2,s_3$ 和 $\cos\alpha,\cos\beta,\cos\gamma$ 組成。
- **退化 ⟺ $M$ 不滿秩**。

> 以下**不是逐字稿內容**：$A$ 的形式依講者口述「相機中心和各 3D 點的座標差」整理；$B$ 的確切形式逐字稿沒唸出來，以 Haralick 等人／原論文為準。

**退化一：三個 3D 點共線** [▶ 38:49](https://youtu.be/8Nh1UeuD9-k?t=2329)：

- $\mathbf{p}_1,\mathbf{p}_2,\mathbf{p}_3$ 在一條直線上；相機中心 $\mathbf{p}$ 在任何地方。
- 一條線加一個點總是決定一個平面 → 四個點共面。
- 把世界座標的 $xy$ 平面放在這個平面上 → 所有點的 $z$ 座標相同 → $A$ 的**最後一行變成 0** → $A$ 不滿秩 → $M=AB$ 不滿秩 → 退化。

**退化二：相機中心和三個 3D 點共面** [▶ 41:59](https://youtu.be/8Nh1UeuD9-k?t=2519)：

- 三個點本來就決定一個平面；若相機中心也在這個平面上 → 四點共面。
- 同樣的論證：$A$ 最後一行為 0 → 退化。

> 以下**不是逐字稿內容**，是直覺：相機中心和三個點共面時，三條光線都在同一個平面裡，三個像點在影像上共線——光線的夾角資訊不足以確定相機在平面外的位置。

（本集到 42:55 結束。）

---

## 6. 一頁速查表

### Grunert P3P

**在解什麼**：已知 $K$，3 對 2D–3D 對應，求相機位姿。

**步驟**：

1. 邊長 $a,b,c$（3D 點兩兩距離）；光線方向 $\mathbf{j}_i\propto(u_i,v_i,f)$；夾角 $\cos\alpha=\mathbf{j}_2\cdot\mathbf{j}_3$ 等。
2. 餘弦定理：$s_2^2+s_3^2-2s_2s_3\cos\alpha=a^2$ 等三條。
3. $s_2=us_1$、$s_3=vs_1$，消去 $s_1$、$u$ → $v$ 的四次多項式。
4. 伴隨矩陣特徵值 = 根（最多 4 組實解）；回代 $u$、$s_1$、$s_2$、$s_3$。
5. $\mathbf{p}_i'=s_i\mathbf{j}_i$，絕對定向得 $R,\mathbf{t}$。

**什麼時候會失敗**：三點共線；相機中心和三點共面；（以及多解時要額外的點來挑）。

### 絕對定向

1. 去重心：$\mathbf{r}_i=\mathbf{p}_i-\bar{\mathbf{p}}$、$\mathbf{r}_i'=\mathbf{p}_i'-\bar{\mathbf{p}}'$。
2. $M=\sum\mathbf{r}_i'\mathbf{r}_i^\mathsf{T}$；$Q=M^\mathsf{T}M=V\Sigma V^\mathsf{T}$；$Q^{-1/2}=V\Sigma^{-1/2}V^\mathsf{T}$。
3. $MQ^{-1/2}=UV^\mathsf{T}$（方向見待確認）。
4. 平移對齊重心。

### 穩定性

$J\,d\mathbf{x}=0$；$J$ 滿秩 ⟺ 穩定。P3P 中 $M=AB$，$A$ 的列是 $(\mathbf{c}-\mathbf{p}_i)^\mathsf{T}$，四點共面 → $A$ 奇異。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 兩階段（深度 → 絕對定向） | 第 22 集（Quan 四點法、EPnP 也是先求相機座標系下的點） |
| 絕對定向 | 第 22 集（EPnP 最後一步）；第 27–30 集（對齊重建） |
| P3P + RANSAC | 第 27–30 集（SfM 中加入新相機） |
| 退化判準（Jacobian 奇異） | 第 22 集（危險圓柱等更一般的退化） |
| 非透視 PnP | 第 35–37 集（廣義相機） |

---

## 附：本集一句話總結

> **相機已校正時，位姿只有 6 個自由度，3 對點就夠：Grunert（1841）用像點算出光線夾角、用 3D 點算出邊長，三個餘弦定理方程式消元成四次多項式（伴隨矩陣求根，最多 4 組解）得到三個深度，再用絕對定向（去重心、$M=\sum\mathbf{r}_i'\mathbf{r}_i^\mathsf{T}$、$MQ^{-1/2}$）對齊兩組點求 $R,\mathbf{t}$；三點共線或相機中心和三點共面時，Jacobian 奇異，問題退化。**

---

## ⚠️ 待確認清單

1. [▶ 25:05](https://youtu.be/8Nh1UeuD9-k?t=1505) 絕對定向中 $M=\sum\mathbf{r}_i'\mathbf{r}_i^\mathsf{T}$、$R=MQ^{-1/2}$ 得到的是「世界 → 相機」還是「相機 → 世界」的旋轉，以及平移的確切寫法，逐字稿聽不出來；依推論，$MQ^{-1/2}=UV^\mathsf{T}$ 是世界 → 相機，相機 → 世界要取轉置。

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 8 (Part 2) 錄影逐字稿（Whisper `medium.en`，43:02）整理；MVG 沒有對應內容。*
