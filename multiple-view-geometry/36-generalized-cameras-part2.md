---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 36
lecture: Lecture 12 (Part 2) – Generalized cameras
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/HuxLHhvdBLY
notes: MVG 沒有廣義相機；講者說本集依 Hongdong Li 等「A Linear Approach to Motion Estimation Using Generalized Camera Models」的記號（BRIEF 未列，未查）
---

# 第 36 集 · Lecture 12 (Part 2)：廣義極線幾何的三種退化情況與退化時的線性解法 [▶ 影片](https://youtu.be/HuxLHhvdBLY)

← 上一集：[35-generalized-cameras-part1](35-generalized-cameras-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[37-generalized-cameras-part3](37-generalized-cameras-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 36 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（45:33，Whisper `medium.en` 轉錄）
> **標記說明**：
> - `【口頭】` 講者口頭補充、投影片沒有
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 換個記號寫廣義極線約束](#1-換個記號寫廣義極線約束)
- [2. 秩和退化](#2-秩和退化)
- [3. 一般情況：秩 17](#3-一般情況秩-17)
- [4. 退化一：局部中心投影](#4-退化一局部中心投影)
- [5. 退化二：軸向相機](#5-退化二軸向相機)
- [6. 退化三：局部中心 + 軸向](#6-退化三局部中心--軸向)
- [7. 退化時的線性解法](#7-退化時的線性解法)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/HuxLHhvdBLY?t=0)

線性 17 點法不是對所有廣義相機配置都有效。三種退化配置：

1. **局部中心投影（locally central projection）**
2. **軸向相機（axial camera）**
3. **局部中心 + 軸向**

最後給一個在退化時仍然有效的線性演算法。

---

## 1. 換個記號寫廣義極線約束

[▶ 00:23](https://youtu.be/HuxLHhvdBLY?t=23)

照 Hongdong Li 論文的記號：

- 光線 $\mathbf{L}$ 的單位方向記為 $\mathbf{x}$，線上一點（通常取那台相機的光心）記為 $\mathbf{v}$：
$$
\mathbf{L}=\begin{pmatrix}\mathbf{x}\\\mathbf{v}\times\mathbf{x}\end{pmatrix}
$$
- 第 35 集的廣義極線約束 $\mathbf{L}'^\mathsf{T}\begin{pmatrix}E&R\\R&0\end{pmatrix}\mathbf{L}=0$ 改寫成：

$$
\mathbf{x}'^\mathsf{T}E\mathbf{x}+\mathbf{x}'^\mathsf{T}R\left(\mathbf{v}\times\mathbf{x}\right)+\left(\mathbf{v}'\times\mathbf{x}'\right)^\mathsf{T}R\mathbf{x}=0,\qquad E=\left[\mathbf{t}\right]_\times R
$$

- $R$、$\mathbf{t}$：兩個廣義相機視角之間的相對轉換。

（展開式依第 35 集的矩陣代入寫出；逐字稿只說「改寫成這個形式」。）

---

## 2. 秩和退化

[▶ 02:27](https://youtu.be/HuxLHhvdBLY?t=147)

- 足夠多的對應疊成 $A\mathbf{e}=\mathbf{0}$，$A\in\mathbb{R}^{n\times18}$，$\mathbf{e}=(\mathrm{vec}(E);\mathrm{vec}(R))\in\mathbb{R}^{18}$（前 9 個是 $E$，後 9 個是 $R$）。
- 要有**一參數族**解（差一個尺度），$\mathrm{rank}(A)$ 必須 $=17$。
- **退化**：$\mathrm{rank}(A)<17$ → 解有兩個以上參數，看退化有多嚴重。
- 一般地：若最多只有 $r$ 條線性獨立的方程式（秩不超過 $r$），解空間就是 $18-r$ 維。
  - 例：17 條獨立 → $18-17=1$ 參數族（第 35 集的情況）。

---

## 3. 一般情況：秩 17

[▶ 06:19](https://youtu.be/HuxLHhvdBLY?t=379)

- 相機是一組**沒有限制、一般位置**的光線 → 秩 17，17 組對應用 SVD 得唯一解。
- 多相機系統的例子：相機 $C_1$ 在視角 1 看到某個 3D 點，在視角 2 看到同一點的**不是 $C_1$**，是別台相機。也就是說，點**不是在同一台相機裡被追蹤**。

---

## 4. 退化一：局部中心投影

[▶ 08:12](https://youtu.be/HuxLHhvdBLY?t=492)

**配置**：每個點在兩個視角中都由**同一台相機**看到（例如六台相機的系統，點 1 一直由 $C_1$ 追蹤、點 2 一直由 $C_2$ 追蹤……）。

- 光線用綁在相機架上的座標表示 → 同一台相機在兩個視角的光心座標一樣：$\mathbf{v}_i'=\mathbf{v}_i$。
- 代入約束：
$$
\mathbf{x}_i'^\mathsf{T}E\mathbf{x}_i+\mathbf{x}_i'^\mathsf{T}R\left(\mathbf{v}_i\times\mathbf{x}_i\right)+\left(\mathbf{v}_i\times\mathbf{x}_i'\right)^\mathsf{T}R\mathbf{x}_i=0
$$

⚠️ 逐字稿缺字 [▶ 09:35](https://youtu.be/HuxLHhvdBLY?t=575)：講者說投影片上「這裡少了一個 prime」——應是 $\mathbf{x}_i'$、$\mathbf{v}_i'$。

**多出來的解** [▶ 11:35](https://youtu.be/HuxLHhvdBLY?t=695)：

- $(E,R)$ 本來就是解。
- $(E,R)=(0,I)$ **也是解**：代入後第一項消失，剩
$$
\mathbf{x}_i'\cdot\left(\mathbf{v}_i\times\mathbf{x}_i\right)+\left(\mathbf{v}_i\times\mathbf{x}_i'\right)\cdot\mathbf{x}_i=\left[\mathbf{x}_i',\mathbf{v}_i,\mathbf{x}_i\right]+\left[\mathbf{x}_i,\mathbf{v}_i,\mathbf{x}_i'\right]=0
$$
  （$[\mathbf{a},\mathbf{b},\mathbf{c}]=\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})$ 是純量三重積；交換兩個向量會變號，所以兩項互相抵消。）

**解空間** [▶ 12:48](https://youtu.be/HuxLHhvdBLY?t=768)：秩一般 $\ge16$（不會更低），完整解是**二參數族**：

$$
\left(E,R\right)\to\left(\lambda E,\ \lambda R+\mu I\right)
$$

- 代入約束 = $\lambda\times$（原約束，等於 0）$+\mu\times$（三重積，等於 0）→ 一定滿足。
- **模糊只在 $R$ 裡**：$E$ 仍然只差一個尺度；$R$ 不再能唯一決定。

**純平移時** [▶ 15:07](https://youtu.be/HuxLHhvdBLY?t=907)：$R=I$、$\mathbf{t}\ne\mathbf{0}$。

- 代入後，含 $\mathbf{v}_i$ 的兩項正好是上面的三重積，**消失**。
- 只剩 $\mathbf{x}_i'^\mathsf{T}E\mathbf{x}_i=0$——**退化成一般針孔相機的極線約束**。
- → 局部中心配置在純平移時，**永遠無法恢復平移的尺度**。

---

## 5. 退化二：軸向相機

[▶ 16:51](https://youtu.be/HuxLHhvdBLY?t=1011)

**配置**：所有光線都和**同一條直線（軸）**相交。

**實際例子** [▶ 17:41](https://youtu.be/HuxLHhvdBLY?t=1061)：

1. **Stereo 對**：兩台相機視野重疊很少（擺很遠）或一前一後。
   - 【口頭】**手機**：前鏡頭和後鏡頭，手機很薄，兩台相機幾乎在同一條軸上 → 軸向相機。
2. **光心共線的一組中心相機**：所有相機的光心在同一條軸上。
3. **非中心的反射折射（catadioptric）或魚眼相機**，沿共同的軸安裝。

- 前兩種每台相機本身是中心相機 → 同時是**局部中心 + 軸向**（§6）。

**反射折射、魚眼** [▶ 19:30](https://youtu.be/HuxLHhvdBLY?t=1170)：

- 反射折射相機：一台中心相機對著半球形鏡子；把鏡子當鏡頭，反射進來的光線不交於一點。
- 魚眼相機（例如手機外接的廣角鏡頭）：視野很廣，也可以當成光線不交於一點。
- 兩者都可視為**非中心相機**（細節不講）。

⚠️ 逐字稿缺字：Whisper 把 catadioptric 寫成 “catadioptic”。

**代數** [▶ 20:50](https://youtu.be/HuxLHhvdBLY?t=1250)：把參考原點放在**軸上**，$\mathbf{w}$ 是軸的單位方向：

$$
\mathbf{v}_i=\alpha_i\mathbf{w},\qquad\mathbf{v}_i'=\alpha_i'\mathbf{w}
$$

代入約束：

$$
\mathbf{x}_i'^\mathsf{T}E\mathbf{x}_i+\alpha_i\,\mathbf{x}_i'^\mathsf{T}R\left(\mathbf{w}\times\mathbf{x}_i\right)+\alpha_i'\left(\mathbf{w}\times\mathbf{x}_i'\right)^\mathsf{T}R\mathbf{x}_i=0
$$

**多出來的解** [▶ 22:38](https://youtu.be/HuxLHhvdBLY?t=1358)：$(E,R)=(0,\mathbf{w}\mathbf{w}^\mathsf{T})$。秩一般是 16，完整解：

$$
\left(E,R\right)\to\left(\lambda E,\ \lambda R+\mu\,\mathbf{w}\mathbf{w}^\mathsf{T}\right)
$$

講者沒證明，留給學生代回去驗證。

> 以下**不是逐字稿內容**，是這個驗證：代 $(0,\mathbf{w}\mathbf{w}^\mathsf{T})$，
> $$
> \alpha_i\left(\mathbf{x}_i'^\mathsf{T}\mathbf{w}\right)\underbrace{\mathbf{w}^\mathsf{T}\left(\mathbf{w}\times\mathbf{x}_i\right)}_{=0}+\alpha_i'\underbrace{\left(\mathbf{w}\times\mathbf{x}_i'\right)^\mathsf{T}\mathbf{w}}_{=0}\left(\mathbf{w}^\mathsf{T}\mathbf{x}_i\right)=0
> $$
> 因為 $\mathbf{w}\times\mathbf{a}$ 一定垂直於 $\mathbf{w}$。

- 同樣，**模糊只在 $R$ 裡**，$E$ 只差一個尺度。
- **重要** [▶ 25:03](https://youtu.be/HuxLHhvdBLY?t=1503)：模糊只落在 $R$，是因為**參考原點選在軸上**。原點不在軸上時，模糊會「溢出」到 $E$，但秩不足仍然存在。

---

## 6. 退化三：局部中心 + 軸向

[▶ 26:02](https://youtu.be/HuxLHhvdBLY?t=1562)

**配置**：一組中心相機（例如不重疊的相機對、或一排相機）都在同一條軸上，且每個點由同一台相機追蹤。

- 局部中心 → 同一台相機在兩個視角位置一樣：$\alpha_i=\alpha_i'$（相機剛性固定在軸上）。
- 代入：
$$
\mathbf{x}_i'^\mathsf{T}E\mathbf{x}_i+\alpha_i\left[\mathbf{x}_i'^\mathsf{T}R\left(\mathbf{w}\times\mathbf{x}_i\right)+\left(\mathbf{w}\times\mathbf{x}_i'\right)^\mathsf{T}R\mathbf{x}_i\right]=0
$$

**再多一個解** [▶ 27:46](https://youtu.be/HuxLHhvdBLY?t=1666)：$(E,R)=(0,[\mathbf{w}]_\times)$。

- 講者的直覺：兩項是同樣的東西，但 $\mathbf{x}$ 和 $\mathbf{w}$ 交換位置做外積 → 得到大小相等、方向相反的向量 → 加起來是 0。

> 以下**不是逐字稿內容**，是代數驗證：代 $R=[\mathbf{w}]_\times$，括號內為
> $$
> \mathbf{x}_i'\cdot\left(\mathbf{w}\times\left(\mathbf{w}\times\mathbf{x}_i\right)\right)+\left(\mathbf{w}\times\mathbf{x}_i'\right)\cdot\left(\mathbf{w}\times\mathbf{x}_i\right)
> $$
> 用 $\mathbf{w}\times(\mathbf{w}\times\mathbf{x})=\mathbf{w}(\mathbf{w}\cdot\mathbf{x})-\mathbf{x}$（$\|\mathbf{w}\|=1$）和 $(\mathbf{w}\times\mathbf{a})\cdot(\mathbf{w}\times\mathbf{b})=\mathbf{a}\cdot\mathbf{b}-(\mathbf{w}\cdot\mathbf{a})(\mathbf{w}\cdot\mathbf{b})$：
> $$
> \left[\left(\mathbf{w}\cdot\mathbf{x}_i'\right)\left(\mathbf{w}\cdot\mathbf{x}_i\right)-\mathbf{x}_i'\cdot\mathbf{x}_i\right]+\left[\mathbf{x}_i'\cdot\mathbf{x}_i-\left(\mathbf{w}\cdot\mathbf{x}_i'\right)\left(\mathbf{w}\cdot\mathbf{x}_i\right)\right]=0
> $$

**完整解：四參數族** [▶ 29:04](https://youtu.be/HuxLHhvdBLY?t=1744)：

$$
\left(E,R\right)\to\left(\alpha E,\ \alpha R+\beta I+\gamma\left[\mathbf{w}\right]_\times+\delta\,\mathbf{w}\mathbf{w}^\mathsf{T}\right)
$$

| 項 | 來自 |
|---|---|
| $\alpha(E,R)$ | 原本的解 |
| $\beta I$ | 局部中心 |
| $\gamma[\mathbf{w}]_\times$ | 局部中心 + 軸向 |
| $\delta\,\mathbf{w}\mathbf{w}^\mathsf{T}$ | 軸向 |

（這裡的 $\alpha,\beta,\gamma,\delta$ 是解的參數，和 $\alpha_i$ 不同。）

- 同樣假設原點在軸上，模糊才只落在 $R$；否則會溢出到 $E$，更難處理。
- $E$ 仍然唯一（差尺度）。之後**不需要**把 $E$ 分解成四組解，只取分解出的**兩個旋轉**。

---

## 7. 退化時的線性解法

[▶ 31:06](https://youtu.be/HuxLHhvdBLY?t=1866)

**問題**：秩 $<17$ 時，標準 SVD 取最後一個右奇異向量是**錯的**。

- 例如秩 16，解是 $\mathbf{v}_1+\gamma\mathbf{v}_2$（$V$ 的最後兩行）。
- 若忽略秩不足，SVD 照樣算得出來，但只拿最後一行 → 完全錯誤的解。

**關鍵觀察** [▶ 34:54](https://youtu.be/HuxLHhvdBLY?t=2094)：三種退化中，**$E$ 那部分都不受模糊影響**。

**演算法**：

**在解什麼**：不再解 $\min\|A\mathbf{e}\|$ s.t. $\|\mathbf{e}\|=1$（整個 18 維向量），而是
$$
\min\left\|A_E\mathbf{e}_E+A_R\mathbf{e}_R\right\|\quad\text{s.t.}\quad\left\|\mathbf{e}_E\right\|=1
$$
只約束 $E$ 的範數。

**步驟**：

1. **把 $A$ 拆成兩塊** [▶ 37:25](https://youtu.be/HuxLHhvdBLY?t=2245)：$A=\left[A_E\mid A_R\right]$，各 $n\times9$；約束變成
$$
A_E\mathbf{e}_E+A_R\mathbf{e}_R=\mathbf{0}
$$
2. **用 $\mathbf{e}_E$ 表示 $\mathbf{e}_R$**：移項 $A_R\mathbf{e}_R=-A_E\mathbf{e}_E$，用偽逆
$$
\mathbf{e}_R=-A_R^+A_E\mathbf{e}_E
$$
3. **代回、消去 $\mathbf{e}_R$** [▶ 39:01](https://youtu.be/HuxLHhvdBLY?t=2341)：
$$
A_E\mathbf{e}_E-A_RA_R^+A_E\mathbf{e}_E=\mathbf{0}\quad\Longrightarrow\quad\left(A_RA_R^+-I\right)A_E\,\mathbf{e}_E=\mathbf{0}
$$
   - $\left(A_RA_R^+-I\right)A_E$ 是**已知的** $n\times9$ 矩陣 → 仍是齊次線性方程式。
4. **SVD** 解 $\mathbf{e}_E$（$\|\mathbf{e}_E\|=1$）→ $E$ **沒有模糊**。
5. **分解 $E$** [▶ 41:14](https://youtu.be/HuxLHhvdBLY?t=2474)：照第 18 集，得兩個旋轉 $R$、$R'$。**不用**分解出來的平移（沒有尺度）。
6. **用廣義極線約束解 $\mathbf{t}$** [▶ 41:49](https://youtu.be/HuxLHhvdBLY?t=2509)：對每個 $R$ 分別代入，約束對 $\mathbf{t}$ 變成**線性**：
$$
A_t\begin{pmatrix}t_x\\t_y\\t_z\\1\end{pmatrix}=\mathbf{0}
$$
   SVD 取最後一個右奇異向量 $\lambda\mathbf{v}$，令最後一個元素 $=1$ 決定 $\lambda$ → 唯一的 $\mathbf{t}$。
   - 光線用帶公制尺度的外參算 → $\mathbf{t}$ 有**絕對尺度**（從 $E$ 分解則沒有）。
7. **挑解** [▶ 44:25](https://youtu.be/HuxLHhvdBLY?t=2665)：$(R,\mathbf{t})$、$(R',\mathbf{t}')$ 兩組，選讓 3D 點都在兩台相機**前方**的那組。

⚠️ 逐字稿缺字 [▶ 42:48](https://youtu.be/HuxLHhvdBLY?t=2568)：講者先說「讓最後一個元素為 0」，後面又說「最後一個元素等於 1」；依 $(t_x,t_y,t_z,1)$ 的形式應是 **1**。

> 以下**不是逐字稿內容**，是第 6 步為什麼對 $\mathbf{t}$ 線性：$R$ 固定後，$E=[\mathbf{t}]_\times R$ 對 $\mathbf{t}$ 線性，$\mathbf{x}'^\mathsf{T}[\mathbf{t}]_\times R\mathbf{x}=\mathbf{t}\cdot\left(R\mathbf{x}\times\mathbf{x}'\right)$；其餘兩項不含 $\mathbf{t}$，是已知常數，對應到向量的第 4 個分量 1。

**什麼時候會失敗**：$E$ 本身也模糊時（例如原點沒放在軸上，模糊溢出到 $E$）；純平移的局部中心配置（§4）仍然無法得到尺度。

> 以下**不是逐字稿內容**，是補充：第 6 步在純平移的局部中心配置下，含 $\mathbf{v}$ 的兩項為 0，方程式變成 $\mathbf{t}\cdot(\cdots)=0$ 的齊次形式，最後一個分量的係數全為 0，就無法用「最後一個元素為 1」定出尺度——和 §4 的結論一致。

---

## 8. 一頁速查表

**記號**：$\mathbf{L}=(\mathbf{x};\mathbf{v}\times\mathbf{x})$；約束 $\mathbf{x}'^\mathsf{T}E\mathbf{x}+\mathbf{x}'^\mathsf{T}R(\mathbf{v}\times\mathbf{x})+(\mathbf{v}'\times\mathbf{x}')^\mathsf{T}R\mathbf{x}=0$。

| 配置 | 條件 | 秩 | 解族 | 關鍵一步 |
|---|---|---|---|---|
| 一般 | 點由不同相機看到 | 17 | $\lambda(E,R)$ | — |
| 局部中心 | $\mathbf{v}_i'=\mathbf{v}_i$ | 16 | $(\lambda E,\lambda R+\mu I)$ | 三重積 $[\mathbf{x}',\mathbf{v},\mathbf{x}]+[\mathbf{x},\mathbf{v},\mathbf{x}']=0$ |
| 軸向 | $\mathbf{v}_i=\alpha_i\mathbf{w}$、$\mathbf{v}_i'=\alpha_i'\mathbf{w}$ | 16 | $(\lambda E,\lambda R+\mu\mathbf{w}\mathbf{w}^\mathsf{T})$ | $\mathbf{w}\perp\mathbf{w}\times\mathbf{a}$ |
| 局部中心 + 軸向 | 再加 $\alpha_i=\alpha_i'$ | — | $(\alpha E,\alpha R+\beta I+\gamma[\mathbf{w}]_\times+\delta\mathbf{w}\mathbf{w}^\mathsf{T})$ | 兩項大小相等方向相反 |

- 模糊只在 $R$（原點在軸上時）；$E$ 唯一（差尺度）。
- 局部中心 + 純平移 → 退化成針孔極線約束 → 無尺度。

**退化時的解法**：

| 步驟 | 公式 |
|---|---|
| 消去 $R$ | $\mathbf{e}_R=-A_R^+A_E\mathbf{e}_E$ → $(A_RA_R^+-I)A_E\mathbf{e}_E=0$，SVD，$\|\mathbf{e}_E\|=1$ |
| 旋轉 | 分解 $E$ → $R$、$R'$ |
| 平移 | 每個 $R$：$A_t(t_x,t_y,t_z,1)^\mathsf{T}=0$，SVD，最後元素 $=1$ |
| 挑解 | 點在前方 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 廣義相機的相對位姿 | 第 37 集（廣義相機的絕對位姿：2D–3D 點、線對應） |
| 用約束消去部分未知數再 SVD | 第 37 集（最小解的消去法） |

---

## 附：本集一句話總結

> **17 點法需要 $\mathrm{rank}(A)=17$；但若每個點都由同一台相機追蹤（局部中心），$(0,I)$ 也滿足約束，若所有光心在一條軸上（軸向），$(0,\mathbf{w}\mathbf{w}^\mathsf{T})$ 也滿足，兩者兼具時再加上 $(0,[\mathbf{w}]_\times)$——秩掉到 16 以下，模糊全落在 $R$、$E$ 仍唯一；所以改成只約束 $\|E\|=1$，用 $\mathbf{e}_R=-A_R^+A_E\mathbf{e}_E$ 消去 $R$ 後 SVD 求 $E$，分解出兩個旋轉，再把每個旋轉代回廣義極線約束線性解出帶絕對尺度的 $\mathbf{t}$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 12 (Part 2) 錄影逐字稿（Whisper `medium.en`，45:33）整理；MVG 無對應章節。*
