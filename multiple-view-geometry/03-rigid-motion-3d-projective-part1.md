---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 03
lecture: Lecture 2 (Part 1) – Rigid body motion and 3D projective geometry
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/p05akAOSrUA
notes: 本集內容講者說取自 Ma Yi《An Invitation to 3-D Vision》第 2 章前半（BRIEF 沒列，未查）；MVG 只有 Table 3.2 的 3D 歐氏變換一列可對照（書頁 78，PDF 頁 96）
---

# 第 03 集 · Lecture 2 (Part 1)：3D 剛體運動——SO(3)、SE(3) [▶ 影片](https://youtu.be/p05akAOSrUA)

← 上一集：[02-projective-geometry-2d-part2](02-projective-geometry-2d-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[04-rigid-motion-3d-projective-part2](04-rigid-motion-3d-projective-part2.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 03 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（1:18:05，Whisper `medium.en` 轉錄）＋ MVG Table 3.2（只對照一列）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

（本集的剛體運動內容，講者說取自 Ma Yi 的書，MVG 幾乎沒有。依 BRIEF，本集主要只靠逐字稿。）

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 基本定義：點、向量](#1-基本定義點向量)
- [2. 內積與外積](#2-內積與外積)
  - [2.1 內積](#21-內積)
  - [2.2 外積與反對稱矩陣](#22-外積與反對稱矩陣)
- [3. 座標系與剛體運動](#3-座標系與剛體運動)
- [4. 只保持距離不夠：特殊歐氏變換](#4-只保持距離不夠特殊歐氏變換)
  - [4.1 保持距離 → 歐氏變換 E(3)](#41-保持距離--歐氏變換-e3)
  - [4.2 反例：鏡射](#42-反例鏡射)
  - [4.3 定義 SE(3)](#43-定義-se3)
  - [4.4 性質：保持角度、保持體積](#44-性質保持角度保持體積)
- [5. 旋轉矩陣與 SO(3)](#5-旋轉矩陣與-so3)
- [6. 歐拉角](#6-歐拉角)
- [7. 完整的剛體運動：SE(3) 齊次表示](#7-完整的剛體運動se3-齊次表示)
- [8. 運動的合成與反運動](#8-運動的合成與反運動)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/p05akAOSrUA?t=0)

Lecture 2 的目標（Part 1、Part 2 合起來）：

| 目標 | 本集？ | 來源 |
|---|---|---|
| 解釋**特殊歐氏群 SE(3)**，用它描述 3D 剛體運動 | ✅ | Ma Yi 第 2 章前半 |
| 在射影 3 維空間表示點和平面、點面對偶 | 下一集 | MVG 第 2 章末、第 3 章 |
| 用零空間、張成矩陣、Plücker 座標表示 3D 的線 | 下一集 | MVG §3.2 |
| 把 2D 的二次曲線推廣成 3D 的二次曲面（quadric） | 下一集 | MVG §3.2.4 |

⚠️ 逐字稿缺字：Whisper 把 Plücker 寫成 “Blucher's”。

---

## 1. 基本定義：點、向量

[▶ 01:51](https://youtu.be/p05akAOSrUA?t=111)

**3D 歐氏空間** $\mathbb{E}^3$：用笛卡兒座標 $X,Y,Z$ 描述的熟悉空間。

- 每個點對應 $\mathbb{R}^3$ 中一個向量 $\mathbf{X}=(X_1,X_2,X_3)^\mathsf{T}$，$X_i\in\mathbb{R}$。
- 這樣 $\mathbb{E}^3$ 和 $\mathbb{R}^3$ 之間有一對一的對應。

**向量** [▶ 04:01](https://youtu.be/p05akAOSrUA?t=241)：由兩個點 $p$、$q$ 決定的有方向箭頭。

- $p$ 的座標是 $\mathbf{X}$，$q$ 的座標是 $\mathbf{Y}$，那麼 $\mathbf{v}=\mathbf{Y}-\mathbf{X}$。
- 方向有關係：從 $p$ 到 $q$ 和從 $q$ 到 $p$ 是不同的向量。

⚠️ 逐字稿缺字 [▶ 05:23](https://youtu.be/p05akAOSrUA?t=323)：Whisper 寫 “V has the coordinate of Y-3”，依上下文應為 $\mathbf{v}=\mathbf{Y}-\mathbf{X}$。

兩種向量：

| | 束縛向量（bound vector） | 自由向量（free vector） |
|---|---|---|
| 起點重不重要 | 重要，由起點 $p$ 和終點 $q$ 一起決定 | 不重要 |
| 什麼時候算同一個 | — | $\mathbf{Y}-\mathbf{X}=\mathbf{Y}'-\mathbf{X}'$：長度一樣、方向一樣（平行） |

- 自由向量可以在空間中**平行移動**到任何地方。
- 不失一般性，可以把自由向量的起點放在原點（$\mathbf{X}=\mathbf{0}$），這時向量就等於終點 $\mathbf{Y}$。

**線性組合** [▶ 08:49](https://youtu.be/p05akAOSrUA?t=529)：所有向量形成一個線性空間。$\alpha\mathbf{v}+\beta\mathbf{u}$ 還是向量，落在 $\mathbf{v}$、$\mathbf{u}$ 張成的子空間裡（$\alpha$ 把 $\mathbf{v}$ 拉長或縮短）。

---

## 2. 內積與外積

### 2.1 內積

[▶ 10:33](https://youtu.be/p05akAOSrUA?t=633)

$$
\langle\mathbf{u},\mathbf{v}\rangle=\mathbf{u}^\mathsf{T}\mathbf{v}=u_1v_1+u_2v_2+u_3v_3
$$

- **量長度**：$\|\mathbf{v}\|=\sqrt{\langle\mathbf{v},\mathbf{v}\rangle}=\sqrt{v_1^2+v_2^2+v_3^2}$。
- **量角度**（兩個向量起點都在原點）：
$$
\cos\theta=\frac{\langle\mathbf{u},\mathbf{v}\rangle}{\|\mathbf{u}\|\|\mathbf{v}\|}
$$

⚠️ 逐字稿缺字：Whisper 多處把 angle 寫成 “anchor” 或 “anger”。

### 2.2 外積與反對稱矩陣

[▶ 13:07](https://youtu.be/p05akAOSrUA?t=787)

外積（cross product），講者也叫 outer product：

$$
\mathbf{u}\times\mathbf{v}=\begin{pmatrix} u_2v_3-u_3v_2\\ u_3v_1-u_1v_3\\ u_1v_2-u_2v_1\end{pmatrix}
$$

**右手定則**：四指指向 $\mathbf{u}$，往 $\mathbf{v}$ 掃過去，大拇指就是 $\mathbf{u}\times\mathbf{v}$ 的方向。

性質：

1. **對每個參數都是線性的** [▶ 14:30](https://youtu.be/p05akAOSrUA?t=870)：
$$
\mathbf{u}\times(\alpha\mathbf{v}+\beta\mathbf{w})=\alpha\,\mathbf{u}\times\mathbf{v}+\beta\,\mathbf{u}\times\mathbf{w}
$$
2. **垂直於兩個輸入** [▶ 15:50](https://youtu.be/p05akAOSrUA?t=950)：
$$
\langle\mathbf{u}\times\mathbf{v},\mathbf{u}\rangle=\langle\mathbf{u}\times\mathbf{v},\mathbf{v}\rangle=0
$$
   因為兩者夾角 $90^\circ$，$\cos90^\circ=0$。
3. **反交換** [▶ 17:26](https://youtu.be/p05akAOSrUA?t=1046)：$\mathbf{u}\times\mathbf{v}=-\mathbf{v}\times\mathbf{u}$（講者寫成 $(-\mathbf{v})\times\mathbf{u}$，用右手定則驗證）。
   - 意義：**外積定義了方向（orientation）**。

**外積寫成矩陣乘法** [▶ 18:49](https://youtu.be/p05akAOSrUA?t=1129)：

- 固定 $\mathbf{u}$，映射 $\mathbf{v}\mapsto\mathbf{u}\times\mathbf{v}$ 是 $\mathbb{R}^3\to\mathbb{R}^3$ 的**線性**映射，所以可以寫成一個 $3\times3$ 矩陣乘 $\mathbf{v}$：

$$
\mathbf{u}\times\mathbf{v}=\hat{\mathbf{u}}\,\mathbf{v},\qquad
\hat{\mathbf{u}}=\begin{pmatrix} 0 & -u_3 & u_2\\ u_3 & 0 & -u_1\\ -u_2 & u_1 & 0\end{pmatrix}
$$

> 以下**不是逐字稿內容**：逐字稿只說「照這個格式」，矩陣是依外積定義重建的。驗證第一列：$(0,-u_3,u_2)\cdot(v_1,v_2,v_3)=u_2v_3-u_3v_2$，和外積第一個分量一樣。

- $\hat{\mathbf{u}}$ 是**反對稱矩陣（skew-symmetric matrix）**：對角線為 0，$\hat{\mathbf{u}}^\mathsf{T}=-\hat{\mathbf{u}}$。

**右手座標系** [▶ 21:06](https://youtu.be/p05akAOSrUA?t=1266)：標準笛卡兒座標裡，$x$ 軸 × $y$ 軸 = $z$ 軸：

$$
\begin{pmatrix}1\\0\\0\end{pmatrix}\times\begin{pmatrix}0\\1\\0\end{pmatrix}=\begin{pmatrix}0\cdot0-0\cdot1\\ 0\cdot0-1\cdot0\\ 1\cdot1-0\cdot0\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix}
$$

---

## 3. 座標系與剛體運動

[▶ 22:20](https://youtu.be/p05akAOSrUA?t=1340)

- 任何**剛體（rigid body）**都可以綁上一個**右手正交座標系**，叫**物體座標系（object frame）**或**本體座標系（body frame）**，例如 $F_0$。
- 另外在世界裡固定一個**世界座標系（world frame）** $F_W$。
- 物體座標系跟著物體一起旋轉、平移；世界座標系不動。
- **剛體的運動 = 物體座標系相對世界座標系的運動**。

**例子：相機** [▶ 24:25](https://youtu.be/p05akAOSrUA?t=1465)：在相機上綁座標系 $F_C$，世界座標系 $F_W$ 事先選好。描述兩個座標系的關係需要兩個成分：

1. **平移向量（translation）**：從 $F_W$ 原點指到 $F_C$ 原點的 3 維向量。
2. **相對方向（rotation）**：把兩個原點對齊後，$F_C$ 的軸和 $F_W$ 的軸還差一個轉向，可以用 roll、pitch、yaw 三個角度描述；之後會看到它是一個 $3\times3$ 矩陣。

⚠️ 逐字稿缺字 [▶ 26:04](https://youtu.be/p05akAOSrUA?t=1564)：Whisper 寫 “rho, pitch and yaw”，應為 **roll**、pitch、yaw。後面 [▶ 1:01:25](https://youtu.be/p05akAOSrUA?t=3685) 的 “raw angle” 也是 roll。

---

## 4. 只保持距離不夠：特殊歐氏變換

### 4.1 保持距離 → 歐氏變換 E(3)

[▶ 26:50](https://youtu.be/p05akAOSrUA?t=1610)

**剛體運動的不變量**：剛體上**任兩點的距離不變**。

- 剛體上兩點 $p$、$q$，座標 $\mathbf{X}(t)$、$\mathbf{Y}(t)$，距離 $d=\|\mathbf{X}(t)-\mathbf{Y}(t)\|$ 對所有時間 $t$ 都是常數。
- **剛體運動**：一族映射 $g(t):\mathbb{R}^3\to\mathbb{R}^3$，描述剛體上每一點的座標怎麼隨時間變，同時滿足距離不變。
- 只看起點和終點（不管中間過程），去掉 $t$，叫**剛體位移（rigid body displacement）**：$\mathbf{X}\mapsto g(\mathbf{X})$。

**$g$ 也作用在向量上** [▶ 30:44](https://youtu.be/p05akAOSrUA?t=1844)：向量 $\mathbf{v}=\mathbf{Y}-\mathbf{X}$，

$$
g_*(\mathbf{v})=g(\mathbf{Y})-g(\mathbf{X})
$$

（變換後向量方向可能變了，但兩點距離不變。）

> 以下**不是逐字稿內容**：$g_*$ 這個記號是 Ma Yi 書的寫法，逐字稿只說「$g$ 也誘導出向量上的變換」。本筆記用 $g_*$ 區分作用在點和作用在向量上。

- 保持任兩點距離的映射，叫**歐氏變換（Euclidean transformation）**，全體記作 $E(3)$。

### 4.2 反例：鏡射

[▶ 32:36](https://youtu.be/p05akAOSrUA?t=1956)

**只保持距離，不足以描述剛體運動**：

- 平移可以靠「保持距離」描述，但**旋轉不行**。
- 反例：
$$
f:\begin{pmatrix} X_1\\ X_2\\ X_3\end{pmatrix}\mapsto\begin{pmatrix} X_1\\ X_2\\ -X_3\end{pmatrix}
$$
- 任兩點的距離都保持住了。
- 但物理上**做不到**：把第三個軸翻向，座標系就變成左手系，違反右手定則（四指從 $X_1$ 掃到 $X_2$，大拇指應該朝上，不是朝下）。
- 問題出在**方向（orientation）沒被保持**。

### 4.3 定義 SE(3)

[▶ 36:05](https://youtu.be/p05akAOSrUA?t=2165)

要排除鏡射，除了保持距離（向量的長度），還要**保持外積**（方向）。

> **定義（特殊歐氏變換）** 映射 $g:\mathbb{R}^3\to\mathbb{R}^3$ 是**剛體運動**，或叫**特殊歐氏變換（special Euclidean transformation）**，如果它保持**長度**和**外積**：
> 1. $\|g_*(\mathbf{v})\|=\|\mathbf{v}\|$，對所有向量 $\mathbf{v}$；
> 2. $g_*(\mathbf{u})\times g_*(\mathbf{v})=g_*(\mathbf{u}\times\mathbf{v})$，對所有向量 $\mathbf{u},\mathbf{v}$。
>
> 全體記作 $SE(3)$。

- 「special」的意思：**保持方向（orientation preserving）**。
- **為什麼叫「群」** [▶ 40:26](https://youtu.be/p05akAOSrUA?t=2426)：在合成下封閉——$g_1,g_2\in SE(3)$，則 $g_1g_2$ 也在 $SE(3)$ 裡。講者不深入群論。

### 4.4 性質：保持角度、保持體積

**保持內積、角度** [▶ 41:10](https://youtu.be/p05akAOSrUA?t=2470)：用**極化恆等式（polarization identity）**：

$$
\langle\mathbf{u},\mathbf{v}\rangle=\frac{1}{4}\left(\|\mathbf{u}+\mathbf{v}\|^2-\|\mathbf{u}-\mathbf{v}\|^2\right)
$$

> 以下**不是逐字稿內容**：逐字稿只說「投影片上這個式子」，沒有唸出來；上式是依講者描述（「把 $u_1,u_2,u_3$ 加 $v_1,v_2,v_3$ 代進範數，兩邊都得到 $u_1v_1+u_2v_2+u_3v_3$」）重建的標準形式。講者把驗證留作練習。關鍵一步：$\|\mathbf{u}\pm\mathbf{v}\|^2=\|\mathbf{u}\|^2\pm2\langle\mathbf{u},\mathbf{v}\rangle+\|\mathbf{v}\|^2$，相減得 $4\langle\mathbf{u},\mathbf{v}\rangle$。

- 右邊只用到長度，而 $g$ 保持長度 → $g$ 也保持內積：$\langle\mathbf{u},\mathbf{v}\rangle=\langle g_*(\mathbf{u}),g_*(\mathbf{v})\rangle$。
- 內積 $=\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$，長度不變、內積不變 → **夾角 $\theta$ 不變**。

**保持體積** [▶ 44:34](https://youtu.be/p05akAOSrUA?t=2674)：保持**三重積（triple product）**：

$$
\langle g_*(\mathbf{u}),\,g_*(\mathbf{v})\times g_*(\mathbf{w})\rangle=\langle\mathbf{u},\,\mathbf{v}\times\mathbf{w}\rangle
$$

- 理由：外積被保持（定義第 2 條），內積也被保持（上面）。
- **三重積 = 平行六面體的體積**（講者叫 cuboid）：
  - $\|\mathbf{a}\times\mathbf{b}\|$ = 底面積；
  - $\|\mathbf{c}\|\cos\phi$ = 高（$\phi$ 是 $\mathbf{c}$ 和 $\mathbf{a}\times\mathbf{b}$ 的夾角）；
  - 相乘 = 體積 = $|\langle\mathbf{a}\times\mathbf{b},\mathbf{c}\rangle|$。
- 所以剛體運動**保持體積**。

---

## 5. 旋轉矩陣與 SO(3)

[▶ 47:42](https://youtu.be/p05akAOSrUA?t=2862)

先只看旋轉：剛體繞固定點 $o$（原點）轉。世界座標系 $XYZ$（實線），物體座標系 $xyz$（虛線），兩者原點重合。物體繞某個軸 $\omega$ 轉。

**怎麼描述物體座標系 $C$ 的方向**：用三個正交向量

$$
\mathbf{r}_1=g_*(\mathbf{e}_1),\quad \mathbf{r}_2=g_*(\mathbf{e}_2),\quad \mathbf{r}_3=g_*(\mathbf{e}_3)
$$

- $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ 是世界座標系的基底向量（$x,y,z$ 軸）。
- $\mathbf{r}_i$ 就是轉完之後的物體座標軸，用世界座標表示。都是**單位向量**。

**旋轉矩陣** [▶ 51:11](https://youtu.be/p05akAOSrUA?t=3071)：把三個向量依序排成三行：

$$
R_{wc}=\begin{pmatrix} \mathbf{r}_1 & \mathbf{r}_2 & \mathbf{r}_3\end{pmatrix}\in\mathbb{R}^{3\times3}
$$

- 點 $p$ 在物體座標系的座標是 $\mathbf{X}_c$，則 $R_{wc}\mathbf{X}_c$ 就是它在世界座標系的座標。

**正交條件** [▶ 52:54](https://youtu.be/p05akAOSrUA?t=3174)：$\mathbf{r}_i$ 兩兩垂直、長度為 1：

$$
\mathbf{r}_i^\mathsf{T}\mathbf{r}_j=\begin{cases}1, & i=j\\ 0, & i\neq j\end{cases}
$$

- 不同軸夾角 $90^\circ$，$\cos90^\circ=0$；同一軸夾角 $0$，$\cos0=1$。

寫成矩陣：

$$
R^\mathsf{T}R=\begin{pmatrix}\mathbf{r}_1^\mathsf{T}\\ \mathbf{r}_2^\mathsf{T}\\ \mathbf{r}_3^\mathsf{T}\end{pmatrix}\begin{pmatrix}\mathbf{r}_1 & \mathbf{r}_2 & \mathbf{r}_3\end{pmatrix}=\begin{pmatrix}\mathbf{r}_1^\mathsf{T}\mathbf{r}_1 & \mathbf{r}_1^\mathsf{T}\mathbf{r}_2 & \cdots\\ \vdots & \ddots & \\ & & \mathbf{r}_3^\mathsf{T}\mathbf{r}_3\end{pmatrix}=I
$$

- 滿足 $R^\mathsf{T}R=RR^\mathsf{T}=I$ 的叫**正交矩陣（orthogonal matrix）**。
- 所以 **$R^{-1}=R^\mathsf{T}$**。

**右手系 → 行列式 +1** [▶ 55:27](https://youtu.be/p05akAOSrUA?t=3327)：$\mathbf{r}_1,\mathbf{r}_2,\mathbf{r}_3$ 是右手系，所以 $\det R=+1$。這叫**特殊正交矩陣（special orthogonal matrix）**。

$$
SO(3)=\left\{R\in\mathbb{R}^{3\times3}\ :\ R^\mathsf{T}R=I,\ \det R=+1\right\}
$$

- 「special」= 保持方向（$\det=+1$ 對應右手定則）。
- 傳統上，$3\times3$ 特殊正交矩陣就叫**旋轉矩陣（rotation matrix）**。

【口頭】[▶ 55:51](https://youtu.be/p05akAOSrUA?t=3351) 講者這裡說「和特殊歐氏群比較，那裡的 special 指的是保持距離」。這和第 4.3 節講者自己說的「special 指保持方向」不一致；依定義，兩處的 special 都是指**保持方向**（保持距離是 $E(3)$ 就有的）。應是口誤。

**旋轉保持內積和外積** [▶ 56:37](https://youtu.be/p05akAOSrUA?t=3397)：

- 內積：$\langle R\mathbf{v},R\mathbf{u}\rangle=\mathbf{v}^\mathsf{T}R^\mathsf{T}R\mathbf{u}=\mathbf{v}^\mathsf{T}\mathbf{u}$。
- 外積：$R\mathbf{v}\times R\mathbf{u}=R(\mathbf{v}\times\mathbf{u})$。講者只說「用反對稱矩陣展開、利用 $\mathbf{r}_i^\mathsf{T}\mathbf{r}_j$ 是 0 或 1」，留作練習。

---

## 6. 歐拉角

[▶ 58:30](https://youtu.be/p05akAOSrUA?t=3510)

旋轉矩陣可以用三個角度表示，這是**最小表示（minimal representation）**，叫**歐拉角（Euler angles）**。

| 角度 | 繞哪個軸 | 講者用的符號 |
|---|---|---|
| **yaw**（偏航） | $z$ 軸 | $\gamma$ |
| **pitch**（俯仰） | $y$ 軸 | $\beta$ |
| **roll**（翻滾） | $x$ 軸 | $\alpha$ |

- 正方向：大拇指指向軸，四指彎曲的方向。
- 講者逐一說明：繞 $z$ 轉時 $z$ 座標不變，只有 $x,y$ 平面裡的點換到新座標 $x_1,y_1$；繞 $y$ 轉時新 $z$ 軸在舊座標下有 $\cos\beta$、$\sin\beta$ 兩個分量；繞 $x$ 轉時新 $y$ 軸是 $\cos\alpha$（在舊 $y$）和 $\sin\alpha$（在舊 $z$）。

> 以下**不是逐字稿內容**：逐字稿沒有唸出矩陣元素，下面是依講者描述重建的標準基本旋轉矩陣（把新座標系的座標換成舊座標系的座標）：
> $$R_z(\gamma)=\begin{pmatrix}\cos\gamma & -\sin\gamma & 0\\ \sin\gamma & \cos\gamma & 0\\ 0 & 0 & 1\end{pmatrix},\quad R_y(\beta)=\begin{pmatrix}\cos\beta & 0 & \sin\beta\\ 0 & 1 & 0\\ -\sin\beta & 0 & \cos\beta\end{pmatrix},\quad R_x(\alpha)=\begin{pmatrix}1 & 0 & 0\\ 0 & \cos\alpha & -\sin\alpha\\ 0 & \sin\alpha & \cos\alpha\end{pmatrix}$$

**組合** [▶ 1:02:50](https://youtu.be/p05akAOSrUA?t=3770)：

- 三個角可以有很多種順序（roll→pitch→yaw、yaw→roll→pitch……）。
- 航空上描述飛機方向用一種特別的順序，叫 **Tait–Bryan 角**：先繞 $z$，再繞新的 $y'$，最後繞再新的 $x''$（$z$-$y'$-$x''$）。
- 講者把三個旋轉寫成 $R_{10}$（yaw）、$R_{21}$（pitch）、$R_{32}$（roll），串起來得到 $R_{30}$：給一個在最後座標系的點 $\mathbf{X}_3$，用 $R_{30}$ 乘它就得到它在原始座標系的座標。

> 以下**不是逐字稿內容**，是依「繞動軸依序 $z$-$y'$-$x''$ 旋轉」推論的：用上面那種「新 → 舊」的基本矩陣，結果是
> $$R=R_z(\gamma)\,R_y(\beta)\,R_x(\alpha)$$
> 一個在最後座標系的點，先用 $R_x$ 換到中間座標系，再用 $R_y$、$R_z$ 換回原始座標系。

⚠️ 待確認 [▶ 1:03:56](https://youtu.be/p05akAOSrUA?t=3836)：投影片上 $R_{10},R_{21},R_{32}$ 的下標方向（例如 $R_{10}$ 是「1 → 0」還是「0 → 1」）、以及三者相乘的順序，逐字稿聽不出來。上面的 $R_zR_yR_x$ 是推論。

⚠️ 逐字稿缺字：Whisper 把 Tait–Bryan 寫成 “tie brian”。

---

## 7. 完整的剛體運動：SE(3) 齊次表示

[▶ 1:04:53](https://youtu.be/p05akAOSrUA?t=3893)

**設定**：物體上一點 $p$。

- $\mathbf{X}_w$：$p$ 在世界座標系 $F_W$ 的座標。
- $\mathbf{X}_c$：$p$ 在物體（相機）座標系 $F_C$ 的座標。
- $\mathbf{t}_{wc}$：從 $F_W$ 原點到 $F_C$ 原點的平移向量（用世界座標表示）。
- $R_{wc}$：把 $F_C$ 的方向對齊到 $F_W$ 的旋轉。

**關係**：

$$
\mathbf{X}_w=R_{wc}\mathbf{X}_c+\mathbf{t}_{wc}
$$

- 先用 $R_{wc}$ 把 $\mathbf{X}_c$ 轉成和世界座標系同方向；
- 再加上平移，把兩個原點對齊。

**寫成齊次形式** [▶ 1:07:40](https://youtu.be/p05akAOSrUA?t=4060)：

$$
\begin{pmatrix}\mathbf{X}_w\\ 1\end{pmatrix}=\underbrace{\begin{pmatrix} R_{wc} & \mathbf{t}_{wc}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}}_{g_{wc}}\begin{pmatrix}\mathbf{X}_c\\ 1\end{pmatrix}
$$

- $(\mathbf{X}_c,1)^\mathsf{T}$ 就是 $p$ 的 3D **齊次座標**（第 01 集 2D 版的推廣）。
- $g$ 是 $4\times4$ 矩陣，最後一列是 $(0,0,0,1)$。這把「旋轉 + 平移」變成**一個線性映射**。

$$
SE(3)=\left\{g=\begin{pmatrix} R & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\ :\ R\in SO(3),\ \mathbf{t}\in\mathbb{R}^3\right\}
$$

**群的封閉性** [▶ 1:09:45](https://youtu.be/p05akAOSrUA?t=4185)：$g_1,g_2\in SE(3)$ → $g_1g_2\in SE(3)$。

> 以下**不是逐字稿內容**，是依矩陣乘法推論的關鍵一步：$\begin{pmatrix}R_1 & \mathbf{t}_1\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\begin{pmatrix}R_2 & \mathbf{t}_2\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}=\begin{pmatrix}R_1R_2 & R_1\mathbf{t}_2+\mathbf{t}_1\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$，且 $R_1R_2\in SO(3)$（$(R_1R_2)^\mathsf{T}R_1R_2=I$、$\det=1\cdot1$）。

**反矩陣** [▶ 1:10:28](https://youtu.be/p05akAOSrUA?t=4228)：

$$
g^{-1}=\begin{pmatrix} R^\mathsf{T} & -R^\mathsf{T}\mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}
$$

講者留作練習，提示是驗證 $g^{-1}g=I$。

> 以下**不是逐字稿內容**，是驗證的關鍵一步：$\begin{pmatrix}R^\mathsf{T} & -R^\mathsf{T}\mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}\begin{pmatrix}R & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}=\begin{pmatrix}R^\mathsf{T}R & R^\mathsf{T}\mathbf{t}-R^\mathsf{T}\mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}=I$。

【課本補充】MVG Table 3.2：3D 的歐氏變換 $\begin{pmatrix}R & \mathbf{t}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$ 有 **6 個自由度**（3 個旋轉 + 3 個平移），不變量是體積。下一集講 3D 變換階層時會再出現。

---

## 8. 運動的合成與反運動

[▶ 1:11:03](https://youtu.be/p05akAOSrUA?t=4263)

三個時刻 $t=1,2,3$ 的相機座標系 $F_1,F_2,F_3$。同一個點在三個座標系的座標是 $\mathbf{X}_1,\mathbf{X}_2,\mathbf{X}_3$（齊次）。

- 從 $F_1$ 換到 $F_2$：$\mathbf{X}_2=g_{21}\mathbf{X}_1$，$g_{21}=\begin{pmatrix}R_{21} & \mathbf{t}_{21}\\ \mathbf{0}^\mathsf{T} & 1\end{pmatrix}$。
- 從 $F_2$ 換到 $F_3$：$\mathbf{X}_3=g_{32}\mathbf{X}_2$。
- 也可以直接從 $F_1$ 換到 $F_3$：$\mathbf{X}_3=g_{31}\mathbf{X}_1$。

**合成規則** [▶ 1:14:18](https://youtu.be/p05akAOSrUA?t=4458)：代入

$$
\mathbf{X}_3=g_{32}\mathbf{X}_2=g_{32}g_{21}\mathbf{X}_1\quad\text{且}\quad \mathbf{X}_3=g_{31}\mathbf{X}_1\qquad\Longrightarrow\qquad g_{31}=g_{32}\,g_{21}
$$

**反運動** [▶ 1:15:20](https://youtu.be/p05akAOSrUA?t=4520)：

- $\mathbf{X}_2=g_{21}\mathbf{X}_1$，$\mathbf{X}_1=g_{12}\mathbf{X}_2$。
- 代入：$\mathbf{X}_2=g_{21}g_{12}\mathbf{X}_2$，要對所有點成立 → $g_{21}g_{12}=I$，即 $g_{12}=g_{21}^{-1}$。

**一般規則** [▶ 1:16:40](https://youtu.be/p05akAOSrUA?t=4600)：

- $g_{ij}$：把「在 $F_j$ 表示的點」換成「在 $F_i$ 表示」。記法：下標從右往左讀，$j\to i$。
- $g_{ik}=g_{ij}\,g_{jk}$（中間的 $j$ 「消掉」）。
- $g_{ij}^{-1}=g_{ji}$。

（本集在 1:18:02 這句話中途結束，下一集接續。）

---

## 9. 一頁速查表

### 外積

| 公式 | 關鍵一步 |
|---|---|
| $\mathbf{u}\times\mathbf{v}=\hat{\mathbf{u}}\mathbf{v}$，$\hat{\mathbf{u}}=\begin{pmatrix}0&-u_3&u_2\\u_3&0&-u_1\\-u_2&u_1&0\end{pmatrix}$ | 外積對 $\mathbf{v}$ 線性 → 可寫成矩陣 |
| $\hat{\mathbf{u}}^\mathsf{T}=-\hat{\mathbf{u}}$ | 反對稱 |
| $\langle\mathbf{u}\times\mathbf{v},\mathbf{u}\rangle=0$ | 垂直 |

### 群

| | 定義 | 自由度 |
|---|---|---|
| $E(3)$ | 保持距離（含鏡射） | — |
| $SO(3)$ | $R^\mathsf{T}R=I$，$\det R=+1$ | 3 |
| $SE(3)$ | 保持長度 **且** 保持外積；$g=\begin{pmatrix}R&\mathbf{t}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$ | 6 |

### SE(3) 保持的量

| 量 | 理由（關鍵一步） |
|---|---|
| 長度 | 定義 |
| 內積、角度 | 極化恆等式：內積只用長度表示 |
| 外積（方向） | 定義 |
| 體積 | 三重積 = 內積 + 外積 |

### 公式

- $\mathbf{X}_w=R_{wc}\mathbf{X}_c+\mathbf{t}_{wc}$
- $g^{-1}=\begin{pmatrix}R^\mathsf{T}&-R^\mathsf{T}\mathbf{t}\\\mathbf{0}^\mathsf{T}&1\end{pmatrix}$
- $g_{ik}=g_{ij}g_{jk}$，$g_{ij}^{-1}=g_{ji}$
- 歐拉角（Tait–Bryan，$z$-$y'$-$x''$）：$R=R_z(\gamma)R_y(\beta)R_x(\alpha)$（推論，見待確認）

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 3D 齊次座標 $(\mathbf{X},1)$ | 第 04 集（$\mathbb{P}^3$ 的點、平面、線、二次曲面） |
| $SE(3)$、$[R\mid\mathbf{t}]$ | 第 10–12 集（相機外參）；第 16–19 集（本質矩陣 $E=\hat{\mathbf{t}}R$）；第 20–22 集（絕對位姿） |
| 反對稱矩陣 $\hat{\mathbf{u}}$ | 第 08 集（DLT 用 $\mathbf{x}'\times H\mathbf{x}=0$）；第 16–19 集（$E$、$F$ 矩陣） |
| 運動合成 $g_{ik}=g_{ij}g_{jk}$ | 第 27–30 集（SfM 中串接多個相機位姿） |
| 3D 歐氏變換 6 dof | 第 04 集（3D 變換階層） |

---

## 附：本集一句話總結

> **剛體運動不只要保持距離，還要保持方向（外積），否則會混進鏡射；滿足這兩條的就是 $SE(3)$：旋轉 $R\in SO(3)$（$R^\mathsf{T}R=I$、$\det R=1$）加平移 $\mathbf{t}$，寫成 $4\times4$ 齊次矩陣後，座標換算、合成、反運動都只是矩陣乘法和求逆。**

---

## ⚠️ 待確認清單

1. [▶ 1:03:56](https://youtu.be/p05akAOSrUA?t=3836) Tait–Bryan 角投影片上 $R_{10},R_{21},R_{32}$ 的下標方向和相乘順序聽不出來；筆記寫的 $R=R_z(\gamma)R_y(\beta)R_x(\alpha)$ 是推論。

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 2 (Part 1) 錄影逐字稿（Whisper `medium.en`，1:18:05）整理；MVG 只對照 Table 3.2。*
