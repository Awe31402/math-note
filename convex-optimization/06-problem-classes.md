---
course: Stanford EE364A Convex Optimization I（2023）
episode: 6
lecture: Lecture 6
date: 待補
video: https://youtu.be/d2jF3SXcFQ8
notes: 《Convex Optimization》§4.2.5–4.6（書頁 144–173，PDF 頁 158–187）
---

# 第 6 集 · Lecture 6：問題類別：LP、QP、SOCP、GP、SDP [▶ 影片](https://youtu.be/d2jF3SXcFQ8)

← 上一集：[05-convex-optimization-problems](05-convex-optimization-problems.md) ｜ [總目錄](README.md) ｜ 下一集：[07-vector-optimization-duality](07-vector-optimization-duality.md) →

> **課程**：Stanford EE364A Convex Optimization I，2023 — 第 6 集
> **講者**：Stephen Boyd
> **來源**：YouTube 錄影逐字稿（1:17:50，人工字幕 en-US）＋ Boyd & Vandenberghe《Convex Optimization》§4.2.5–4.6
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：擬凸最佳化的二分法](#1-複習擬凸最佳化的二分法)
- [2. 線性規劃（LP）](#2-線性規劃lp)
  - [2.1 例：飲食問題](#21-例飲食問題)
  - [2.2 例：分段線性最小化](#22-例分段線性最小化)
  - [2.3 例：多面體的 Chebyshev 中心](#23-例多面體的-chebyshev-中心)
- [3. 線性分式規劃](#3-線性分式規劃)
- [4. 二次規劃（QP）](#4-二次規劃qp)
- [5. 二次約束二次規劃（QCQP）](#5-二次約束二次規劃qcqp)
- [6. 二階錐規劃（SOCP）](#6-二階錐規劃socp)
- [7. 強健線性規劃](#7-強健線性規劃)
- [8. 幾何規劃（GP）](#8-幾何規劃gp)
- [9. 錐形式問題與半正定規劃（SDP）](#9-錐形式問題與半正定規劃sdp)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

「完成這趟問題類別的旋風之旅」。

| 主題 | 課本 |
|---|---|
| 擬凸最佳化的二分法（複習） | §4.2.5 |
| LP、飲食問題、分段線性、Chebyshev 中心 | §4.3、§4.3.1 |
| 線性分式規劃、von Neumann 成長模型 | §4.3.2 |
| QP、QCQP、隨機成本 LP | §4.4、§4.4.1 |
| SOCP、強健 LP | §4.4.2 |
| GP、懸臂樑 | §4.5 |
| 錐形式、SDP、LMI | §4.6 |

---

## 1. 複習：擬凸最佳化的二分法

[▶ 00:05](https://youtu.be/d2jF3SXcFQ8?t=5)

擬凸最佳化要小心：局部最佳不一定全域最佳。做法是用凸函數 $\phi_t$ 表示 $f_0$ 的 $t$-下水平集（見[第 5 集 §9](05-convex-optimization-problems.md#9-擬凸最佳化與二分法)）。$\phi_t$ 有完全一般的構造法，「沒什麼用，但有人問你怎麼來的，你永遠做得到」；通常問題本身會暗示。

例：$p(x)/q(x)$，$p\ge0$ 凸、$q>0$ 凹 [▶ 01:38](https://youtu.be/d2jF3SXcFQ8?t=98)：
- $t<0$：下水平集是空集，凸，不用管。
- $t\ge0$：$p/q\le t\iff p-tq\le0$。在腦中跑規則：$q$ 凹 → 乘正的 $t$ 還是凹 → 負號變凸 → 加上凸的 $p$，凸。

二分法 [▶ 03:42](https://youtu.be/d2jF3SXcFQ8?t=222)：每次解一個凸可行性問題，$p^\star$ 所在的「**無知區間**」（interval of ignorance）縮小一半。【口頭】「你每解一個凸可行性問題，就得到 $p^\star$ 的**一個位元**資訊。」

---

## 2. 線性規劃（LP）

[▶ 04:45](https://youtu.be/d2jF3SXcFQ8?t=285)

【口頭】有名字的問題類別「現在也許沒那麼重要了」，但有人只知道這些名字，所以你得知道。

$$
\begin{aligned}
\text{minimize}\quad & c^Tx+d\\
\text{subject to}\quad & Gx\preceq h\\
& Ax=b
\end{aligned}
$$

- 拿掉常數 $d$ 得到等價（不相等）的問題。換句話說：**在多面體上最小化線性函數**。
- 【口頭】[▶ 05:45](https://youtu.be/d2jF3SXcFQ8?t=345) 現代史從 1940 年代開始，但 **Fourier** 就寫過一篇 LP 的論文。有了電腦才變得有趣。

**圖** [▶ 06:18](https://youtu.be/d2jF3SXcFQ8?t=378)：可行集是多面體，每個面是一條線性不等式；$c^Tx$ 的等高線垂直於 $c$；沿 $-c$ 方向盡量走，停在某個頂點。

【口頭】[▶ 07:20](https://youtu.be/d2jF3SXcFQ8?t=440) 我們不在乎 2 變數的 LP（用眼睛就解了），在乎的是 1 萬變數、3 萬約束的 LP——「我保證此刻就有很多在跑」：排程、供應鏈……「我認為每個人都該知道它。」

### 2.1 例：飲食問題

[▶ 07:50](https://youtu.be/d2jF3SXcFQ8?t=470)

【口頭】約 1940、50 年代的歷史例子，據說來自軍方：怎麼用最便宜的方式讓士兵活下去。

- $x_j\ge0$：食物 $j$ 的份量。
- $a_{ij}$：一單位食物 $j$ 含營養素 $i$ 的量。
- $b_i$：健康飲食需要營養素 $i$ 至少 $b_i$。
- $c_j$：食物 $j$ 的單價。

$$
\begin{aligned}
\text{minimize}\quad & c^Tx\\
\text{subject to}\quad & Ax\succeq b,\quad x\succeq0
\end{aligned}
$$

【口頭】可以替每條約束加註解：「這是總成本」「份量不能為負」「這一列是蛋白質的最低量」。

**化成標準形式（只做這一次）** [▶ 10:24](https://youtu.be/d2jF3SXcFQ8?t=624)

【課堂討論】要寫成 $Gx\preceq h$，學生建議：**負號**。

$$Ax\succeq b\iff-Ax\preceq-b,\qquad x\succeq0\iff-x\preceq0$$

再**堆疊**：
$$G=\begin{pmatrix}-A\\-I\end{pmatrix},\qquad h=\begin{pmatrix}-b\\0\end{pmatrix}$$

【口頭】「以後再也不做這種事了。」現代語言會替你做。以前（或現在某些實習的地方）有人要花好幾週把問題手動轉成這種形式、還要記帳和除錯，這被戲稱為**矩陣填塞**（matrix stuffing）。

【Q&A】[▶ 11:59](https://youtu.be/d2jF3SXcFQ8?t=719) 學生問：轉換後是相同還是等價的問題？答：**等價**。轉換（或用 CS 的話：歸約）得到的問題不是同一個，是等價的。

延伸 [▶ 12:59](https://youtu.be/d2jF3SXcFQ8?t=779)：營養素有上限？可以。某些食物供應有限？當然可以。LP 的表達力很強。

### 2.2 例：分段線性最小化

[▶ 13:31](https://youtu.be/d2jF3SXcFQ8?t=811)

$$\text{minimize}\quad\max_{i=1,\dots,m}\left(a_i^Tx+b_i\right)$$

這是 LP 嗎？檢查目標是否線性——$m>1$ 時不是。但用**上圖形式**就能轉成 LP：

$$
\begin{aligned}
\text{minimize}\quad & t\\
\text{subject to}\quad & a_i^Tx+b_i\le t,\quad i=1,\dots,m
\end{aligned}
$$

約束說 $t$ 是那些仿射函數最大值的上界；最小化這個上界，同時調整 $x$。

【口頭】[▶ 15:02](https://youtu.be/d2jF3SXcFQ8?t=902) 你提出這個問題、有人問「怎麼解？」，懂的人會看著你說「**這是 LP 啊**」。「酷的人會預期你知道；其他人——天知道他們會怎麼做，我其實知道一些。」

### 2.3 例：多面體的 Chebyshev 中心

[▶ 15:33](https://youtu.be/d2jF3SXcFQ8?t=933)

又一個「集合的中心」（上次是良率中心）：多面體 $\mathcal{P}=\{x\mid a_i^Tx\le b_i,\ i=1,\dots,m\}$ 的 **Chebyshev 中心**是**最大內接球**的球心。

【口頭】[▶ 16:42](https://youtu.be/d2jF3SXcFQ8?t=1002) 聽到「線性規劃」，大腦該亮起平的東西：仿射、分段仿射。聽到「2 範數」，該亮起**圓的東西**：球、歐氏距離——「那部分絕不該存在講 LP 的部分附近」。（「我們真的把學生放進 MRI 檢查過——其實沒有，但可以。」）所以看到一個球，應該覺得「涉及二次的東西不會變成 LP」——但它就是。

**推導** [▶ 18:13](https://youtu.be/d2jF3SXcFQ8?t=1093)：球 $\mathcal{B}=\{x_c+u\mid\|u\|_2\le r\}$（參數：球心向量 $x_c$、半徑 $r>0$）。$\mathcal{B}\subseteq\mathcal{P}$ $\iff$ 球在每個半空間裡。

$$\sup_{\|u\|_2\le r}a_i^T(x_c+u)=a_i^Tx_c+r\|a_i\|_2$$

由 Cauchy–Schwarz，$a_i^Tu\le\|a_i\|_2\|u\|_2\le r\|a_i\|_2$，取 $u=ra_i/\|a_i\|_2$ 時等號成立（「Cauchy–Schwarz 是緊的」）。所以

$$
\begin{aligned}
\text{maximize}\quad & r\\
\text{subject to}\quad & a_i^Tx_c+r\|a_i\|_2\le b_i,\quad i=1,\dots,m
\end{aligned}
$$

【口頭】[▶ 20:17](https://youtu.be/d2jF3SXcFQ8?t=1217) 看到 2 範數應該閃黃燈「前方可能不是 LP」，但要冷靜看：變數是 $x_c$、$r$；$\|a_i\|_2$ 是**給定資料**，只是個正數。所以這是 **LP**——「也許我小題大作了」。實際結論：超大規模也能解。

【課堂討論】[▶ 21:18](https://youtu.be/d2jF3SXcFQ8?t=1278) Chebyshev 中心唯一嗎？有人說不唯一；學生舉例：**長方形**。對：內接最大的圓可以沿長邊滑動，很多位置都行。

---

## 3. 線性分式規劃

[▶ 22:20](https://youtu.be/d2jF3SXcFQ8?t=1340)

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)=\frac{c^Tx+d}{e^Tx+f}\\
\text{subject to}\quad & Gx\preceq h,\quad Ax=b
\end{aligned}
$$

（慣例：$\mathbf{dom}\,f_0=\{x\mid e^Tx+f>0\}$。）

- 擬凸問題 → 一定能用二分法、每步呼叫 LP 解法器解。
- 更酷的是 [▶ 22:50](https://youtu.be/d2jF3SXcFQ8?t=1370)：可以化成**單一個 LP**（大約 1950 年代末、60 年代初發現），引入新變數、重新參數化，和**透視轉換**有關。老師沒細講：「沒有人能看一眼就說『我完全看得出來』，這是一個**不顯然**的轉換。」之前的轉換（乘 $-1$ 翻轉不等式）都很顯然，這個不是；之後還有一堆不顯然的。

【課本補充】§4.3.2 的轉換。若可行集非空，原問題等價於 LP（變數 $y\in\mathbb{R}^n$、$z\in\mathbb{R}$）：
$$
\begin{aligned}
\text{minimize}\quad & c^Ty+dz\\
\text{subject to}\quad & Gy-hz\preceq0,\quad Ay-bz=0\\
& e^Ty+fz=1,\quad z\ge0
\end{aligned}
$$
- 原問題可行的 $x$ → 令 $y=\dfrac{x}{e^Tx+f}$、$z=\dfrac{1}{e^Tx+f}$，可行且 $c^Ty+dz=f_0(x)$。所以 LP 的最佳值 $\le$ 原問題。
- 反之 LP 可行的 $(y,z)$，$z\ne0$ 時 $x=y/z$ 可行、目標值相同；$z=0$ 時取原問題的可行點 $x_0$，$x_0+ty$（$t\to\infty$）的目標值趨近 $c^Ty+dz$。所以原問題的最佳值 $\le$ LP。

**廣義線性分式規劃** [▶ 23:51](https://youtu.be/d2jF3SXcFQ8?t=1431)：
$$f_0(x)=\max_{i=1,\dots,r}\frac{c_i^Tx+d_i}{e_i^Tx+f_i}$$
擬凸函數的 max 還是擬凸。老師說據他所知**只能用二分法**解。

**例：von Neumann 經濟成長模型** [▶ 24:23](https://youtu.be/d2jF3SXcFQ8?t=1463)（課本 Example 4.7）

- $x\succ0$：本期 $n$ 個部門的經濟活動水準；$x^+$：下一期。
- $x_i^+/x_i$：部門 $i$ 的成長率（1.06 = 鋼鐵業成長 6%；0.93 = 衰退 7%）。
- 經濟活動消耗、也生產 $m$ 種商品：活動水準 $x$ 消耗 $Bx$、生產 $Ax$（例：汽車業消耗鋼鐵等、生產汽車）。
- 模型：今年生產的東西「先寄存一年」，明年 1 月 1 日拿來用 → 下期消耗不超過本期生產：$Bx^+\preceq Ax$。
- 目標：**最大化各部門中最小的成長率**。

$$
\begin{aligned}
\text{maximize}\quad & \min_{i=1,\dots,n}x_i^+/x_i\\
\text{subject to}\quad & x^+\succeq0,\quad Bx^+\preceq Ax
\end{aligned}
$$

是廣義線性分式問題（把 max min 翻號成 min max）。

【口頭】[▶ 28:05](https://youtu.be/d2jF3SXcFQ8?t=1685)「我保證 10 個部門你就不可能手算出來」，但 1 萬個部門「你可以毫無問題地解」。也有很多變形，例如 10 期、有庫存。

> 老師中途一度疑惑「是不是少了 $x\succeq0$」，然後說它藏在分母（定義域）裡。課本：定義域 $x\succ0$；問題對 $(x,x^+)$ 齊次，可以把隱含約束 $x\succ0$ 換成明確的 $x\succeq\mathbf{1}$。

---

## 4. 二次規劃（QP）

[▶ 28:35](https://youtu.be/d2jF3SXcFQ8?t=1715)

大約 1950 年代初。「不管哪個領域，一定有人會說『那是個 QP』，所以你得知道。」

$$
\begin{aligned}
\text{minimize}\quad & \tfrac12x^TPx+q^Tx+r\\
\text{subject to}\quad & Gx\preceq h,\quad Ax=b
\end{aligned}
\qquad P\in\mathbf{S}^n_+
$$

約束和 LP 一樣（多面體），目標是**凸二次**。

**圖** [▶ 29:05](https://youtu.be/d2jF3SXcFQ8?t=1745)：LP 的等高線是超平面；QP 的等高線是**橢球面**（$P\succ0$；否則是退化橢球）。在最佳點，指向無約束最小點的 $-\nabla f_0$ 是可行集的**外法向量**——不然可以動一下 $x$ 做得更好。

【口頭】[▶ 30:11](https://youtu.be/d2jF3SXcFQ8?t=1811)
- 5 萬變數的 QP「什麼都不是」，可以可靠到嵌進控制系統每秒解 100 次、**失敗率 0**。
- **Falcon 9 第一節火箭降落**時一直在跑好幾個 QP，其中一個每秒 1,000 次，「而且不會失敗」。
- 超過一半的量化避險基金就只是在跑 QP，「此刻有好幾兆美元靠解 QP 在交易」。

**例 1：有界最小平方** [▶ 31:43](https://youtu.be/d2jF3SXcFQ8?t=1903)

$$\text{minimize }\|Ax-b\|_2^2\quad\text{s.t.}\quad l\preceq x\preceq u$$

沒有約束就是最小平方（線性代數）。關鍵是：**加了線性約束仍然完全可處理**。

【口頭】[▶ 32:13](https://youtu.be/d2jF3SXcFQ8?t=1933)「我保證有些領域不知道這件事。」每年都有人說「我們擬合參數，但有些參數必須在範圍內、必須非負」，然後發明一個超複雜的迭代方法——「正確答案是：老兄，**那是 QP**，解就對了，安靜。」

**例 2：保序回歸** [▶ 32:44](https://youtu.be/d2jF3SXcFQ8?t=1964)：最小平方加上 $x_1\le x_2\le\cdots\le x_n$。很好的**磨損模型**：噴射引擎再飛 1 萬小時後，拆開量關鍵間隙，不會比之前更好。統計裡叫**保序回歸**（isotonic regression），「有整本書寫它，我覺得很好笑」——對我們來說它就是 QP，下週開始你用一兩行 Python 就解了。只有在超大規模、或要嵌進安全關鍵系統時，才值得有意義地討論怎麼解。

**例 3：隨機成本的 LP** [▶ 34:18](https://youtu.be/d2jF3SXcFQ8?t=2058)

【口頭】**強健性**（robustness）的大圖：用最佳化時，你等於假設約束和目標「準確到 8 位有效數字」，用浮點數表示一切。做過真實工程的人都知道係數不可能知道那麼準：飲食問題的價格兩天前可能就變了；機械系統的楊氏模數第三位數「荒謬」；金融界的朋友說「我們的模型**符號對了**就很高興」。之後會詳談；這是**正則化**的全部內涵。

設成本 $c$ 是隨機向量，平均 $\bar c$、共變異數 $\Sigma$。可行（$Gx\preceq h$、$Ax=b$）是硬要求，但成本 $c^Tx$ 是隨機的：

$$
\begin{aligned}
\text{minimize}\quad & \bar c^Tx+\gamma x^T\Sigma x=\mathbf{E}\,c^Tx+\gamma\,\mathbf{var}(c^Tx)\\
\text{subject to}\quad & Gx\preceq h,\quad Ax=b
\end{aligned}
$$

- $\gamma>0$：**風險趨避參數**（risk aversion parameter）。目標叫**風險調整成本**（risk-adjusted cost）。$\gamma>0$ 時是 QP。
- 【口頭】更合理的是對變異數開根號（單位相同），但這樣也行。
- **$\gamma<0$ 叫風險追求**（risk-seeking）[▶ 37:54](https://youtu.be/d2jF3SXcFQ8?t=2274)：(A) 很蠢，「除非是某種追求刺激的娛樂設計」；(B) **不是 QP**，因為不再凸。

【口頭】[▶ 38:57](https://youtu.be/d2jF3SXcFQ8?t=2337) 把問題分成「好解／難解」×「合理／愚蠢」四格，並不是各 25%。很常見的是：**該解的問題剛好是能解的**；另外那些「(A) 你不該解，(B) 剛好你也解不了」。

---

## 5. 二次約束二次規劃（QCQP）

[▶ 39:30](https://youtu.be/d2jF3SXcFQ8?t=2370)

$$
\begin{aligned}
\text{minimize}\quad & \tfrac12x^TP_0x+q_0^Tx+r_0\\
\text{subject to}\quad & \tfrac12x^TP_ix+q_i^Tx+r_i\le0,\quad i=1,\dots,m\\
& Ax=b
\end{aligned}
\qquad P_i\in\mathbf{S}^n_+
$$

不等式從線性變成**凸二次**。「現在比較少聽到，但還是有人講。」

【課本補充】$P_i\succ0$ 時可行集是 $m$ 個橢球和一個仿射集的交集。

---

## 6. 二階錐規劃（SOCP）

[▶ 40:01](https://youtu.be/d2jF3SXcFQ8?t=2401)

「現代的，最近 25 年」。看起來像 QCQP，但不是；「看起來很無害，但能歸約到它的問題多到令人難以置信」。

$$
\begin{aligned}
\text{minimize}\quad & f^Tx\\
\text{subject to}\quad & \|A_ix+b_i\|_2\le c_i^Tx+d_i,\quad i=1,\dots,m\\
& Fx=g
\end{aligned}
$$

- $A_i=0$、$b_i=0$ 時每條約束就是線性不等式 → **SOCP 推廣 LP**。
- **是 2 範數，不是 2 範數的平方** [▶ 40:31](https://youtu.be/d2jF3SXcFQ8?t=2431)。【口頭】因為幾百年的數學訓練，看到 2 範數大家就想平方（可能有解析解、可微……），但主要只是歷史習慣。
- 名字的由來 [▶ 41:35](https://youtu.be/d2jF3SXcFQ8?t=2495)：約束說 $(A_ix+b_i,\ c_i^Tx+d_i)$ 這個仿射像落在二階錐 $\{(u,v)\mid\|u\|_2\le v\}$ 裡。
- 包含 QCQP、LP。

> ⚠️ 逐字稿缺字 [▶ 41:04](https://youtu.be/d2jF3SXcFQ8?t=2464)：字幕寫「very important point. This **is squared**」，依上下文（剛說完「是 2 範數，不是平方」）應為「is **not** squared」。

> 以下**不是逐字稿內容**，是依課本 §4.4.2 推論的「SOCP 包含 QCQP」：凸二次約束 $x^TPx+q^Tx+r\le0$（$P=L^TL$）可寫成 $\|Lx\|_2^2\le-q^Tx-r$，再用 $\|u\|_2^2\le s\iff\left\|(2u,\,1-s)\right\|_2\le1+s$ 寫成二階錐約束。

**SOCP 是凸最佳化的「位元組碼」** [▶ 42:06](https://youtu.be/d2jF3SXcFQ8?t=2526)

【口頭】
- 秘密：它大概包含了 100 個領域裡你想解的問題的 **95%**。你用 CVXPY 寫下 quad_over_lin、複雜的幾何平均等各種奇怪函數，它們會被**歸約成 SOCP** 再解。
- 對一大類問題，SOCP 就像**低階語言**、凸最佳化的 bytecode：你用高階形式寫問題 → 編譯成 SOCP → 解。
- 好處：全世界有人在做 SOCP 解法器，因為更大一群人在解他們不知道能歸約成 SOCP 的問題，「一切都配合得很好」。

> ⚠️ 逐字稿缺字 [▶ 42:38](https://youtu.be/d2jF3SXcFQ8?t=2558)：字幕寫「the **3-byte code**」，應為 **bytecode**（位元組碼）。

---

## 7. 強健線性規劃

[▶ 43:09](https://youtu.be/d2jF3SXcFQ8?t=2589)

上一個例子是**目標**不確定，這次是**不等式係數** $a_i$ 不確定：

$$\text{minimize }c^Tx\quad\text{s.t.}\quad a_i^Tx\le b_i,\ i=1,\dots,m$$

【口頭】飲食問題裡「每克食物有多少營養素？」——「看批次。6 月的不太一樣，週五那批和週四那批也不同」，差異可能相當大。把這些資料擬合一個橢球，然後要求「不管送來的食物營養含量是多少，這份飲食都要滿足最低健康要求」——這就是強健解。

兩種模型：

| | 確定性（最壞情況） | 隨機（機會約束） |
|---|---|---|
| 假設 | $a_i\in\mathcal{E}_i=\{\bar a_i+P_iu\mid\|u\|_2\le1\}$ | $a_i\sim\mathcal{N}(\bar a_i,\Sigma_i)$ |
| 要求 | 對所有 $a_i\in\mathcal{E}_i$，$a_i^Tx\le b_i$ | $\mathbf{prob}(a_i^Tx\le b_i)\ge\eta$ |

$\eta$ 典型值 [▶ 44:44](https://youtu.be/d2jF3SXcFQ8?t=2684)：0.9（相當鬆）、0.95、0.99，也可以 0.99999。

【口頭】[▶ 45:16](https://youtu.be/d2jF3SXcFQ8?t=2716)（老師自稱「奇怪的抱怨」）有人說「機率要大於 99.9%」很好笑：沒有任何領域真的那麼了解分布的**尾部**。但這仍是很好的問題：有人看你的程式碼說「哇，你們一定很了解尾分布」，正確答案是「不，我們的尾分布模型很爛，那只是代表『**拜託讓它成立**』」。

**確定性模型 → SOCP** [▶ 46:46](https://youtu.be/d2jF3SXcFQ8?t=2806)

$$\sup_{\|u\|_2\le1}(\bar a_i+P_iu)^Tx=\bar a_i^Tx+\sup_{\|u\|_2\le1}u^TP_i^Tx=\bar a_i^Tx+\|P_i^Tx\|_2$$

所以強健 LP 是

$$
\begin{aligned}
\text{minimize}\quad & c^Tx\\
\text{subject to}\quad & \bar a_i^Tx+\|P_i^Tx\|_2\le b_i,\quad i=1,\dots,m
\end{aligned}
$$

- 這次 2 範數的引數**含變數 $x$**（不像 Chebyshev 中心是資料），所以是真的 **SOCP 約束**。
- 【口頭】[▶ 48:17](https://youtu.be/d2jF3SXcFQ8?t=2897) 不管不確定性、把 $a_i$ 換成中間值 $\bar a_i$，就是 LP。但你會想「留一點**餘裕**以防 $a$ 晃動」——這個式子**精確告訴你要留多少**：$\|P_i^Tx\|_2$ 就是餘裕，而且它是 $x$ 的函數。$P_i$ 大的方向，就該避免 $x$ 往那裡走。

**隨機模型 → SOCP** [▶ 49:18](https://youtu.be/d2jF3SXcFQ8?t=2958)

$a_i^Tx$ 是高斯（高斯向量的線性函數），平均 $\bar a_i^Tx$、變異數 $x^T\Sigma_ix$。減平均除以標準差變成 $\mathcal{N}(0,1)$：

$$\mathbf{prob}(a_i^Tx\le b_i)=\Phi\left(\frac{b_i-\bar a_i^Tx}{\|\Sigma_i^{1/2}x\|_2}\right)$$

$\Phi$ 是標準常態 CDF。「看起來不像會變成 SOCP」——但 $\Phi$ **單調**，所以 [▶ 50:48](https://youtu.be/d2jF3SXcFQ8?t=3048)

$$\Phi(\cdot)\ge\eta\iff\frac{b_i-\bar a_i^Tx}{\|\Sigma_i^{1/2}x\|_2}\ge\Phi^{-1}(\eta)\iff\bar a_i^Tx+\Phi^{-1}(\eta)\,\|\Sigma_i^{1/2}x\|_2\le b_i$$

- **$\eta\ge1/2$ 時** $\Phi^{-1}(\eta)\ge0$，這是 SOCP 約束。
- $\eta<1/2$ 時 $\Phi^{-1}(\eta)<0$（老師估 $\Phi^{-1}(0.3)$「大概 $-1/2$，我編的」），2 範數前面是負號，**不凸**。

> 以下**不是逐字稿內容**：$\Phi^{-1}(0.3)\approx-0.52$，老師的估計很準。

【口頭】[▶ 51:48](https://youtu.be/d2jF3SXcFQ8?t=3108) 有人說「約束成立的機率 15% 對我就夠了」，你該叫他走開，他離開時你還可以喊：「那不但很蠢，而且你也解不了。」老師聽過最接近「風險追求」的例子是設計飛彈控制器的人：「已經發射了，反正不會回來也不會再用，有 10% 擊中機會就做」——「我勉強接受這是個應用，雖然不是社會正面的。」

---

## 8. 幾何規劃（GP）

[▶ 53:25](https://youtu.be/d2jF3SXcFQ8?t=3205)

【口頭】可以追溯到 1940 年代。GP **絕對不是凸問題**，但換個變數就變成凸的，可以擴展到巨大規模。之後在統計、控制也會看到這類「換變數後變凸」的問題。1960 年代整個領域都在講它、寫書，直到大約 **1980 年代**西方才發現它能化成凸問題；「我在莫斯科的朋友說 60 年代大家都知道。」

**術語（不要在錯的場合用）** [▶ 54:59](https://youtu.be/d2jF3SXcFQ8?t=3299)

| GP 術語 | 定義 |
|---|---|
| **單項式**（monomial） | $f(x)=cx_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}$，$c>0$，$a_i\in\mathbb{R}$，$x\succ0$ |
| **正項式**（posynomial） | 單項式的和：$f(x)=\sum_{k=1}^Kc_kx_1^{a_{1k}}\cdots x_n^{a_{nk}}$ |

【口頭】
- 這種乘積在很多工程領域叫**尺度律**（scaling law），例如和 Reynolds 數的關係。
- 數學裡「monomial」從 1820 年左右就有**唯一**的意義：變數的**整數**次方乘積，係數可正可負（$-3x_1^3x_2^2x_5$ 是可以在外面講的 monomial）。只有在 GP 的脈絡才能叫上面那個東西 monomial，「不然附近不懂 GP 的人會以為你是白痴」。
- 「posynomial」更糟——「不是我們編的，是 1960 年代取的名字」，大概是 positive + monomial。說這個字之前要確定聽得到的人都懂 GP；「你可以去數學系試試看」。

**幾何規劃**：

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x)\le1,\quad i=1,\dots,m\\
& h_i(x)=1,\quad i=1,\dots,p
\end{aligned}
$$

$f_i$ 是正項式，$h_i$ 是單項式，$x\succ0$ 是隱含的。

非常不凸，例如 $x_1^{1.3}x_2^{-0.3}=1$「上次我檢查時那可不是仿射」。60 年代有人手算解簡單的 GP。

**換成凸形式** [▶ 58:37](https://youtu.be/d2jF3SXcFQ8?t=3517)：令 $y_i=\log x_i$（$x_i=e^{y_i}$）。

- 單項式：$f(x)=ce^{a^Ty}$ → $\log f=a^Ty+\log c$，**仿射**。
- 正項式：$f(x)=\sum_ke^{a_k^Ty+b_k}$（$b_k=\log c_k$）→ $\log f=\log\sum_ke^{a_k^Ty+b_k}$，**log-sum-exp 合成仿射**，凸。

$$
\begin{aligned}
\text{minimize}\quad & \log\sum_{k=1}^{K_0}e^{a_{0k}^Ty+b_{0k}}\\
\text{subject to}\quad & \log\sum_{k=1}^{K_i}e^{a_{ik}^Ty+b_{ik}}\le0,\quad i=1,\dots,m\\
& Gy+d=0
\end{aligned}
$$

是凸問題，和原 GP **完全等價**。

【口頭】[▶ 59:39](https://youtu.be/d2jF3SXcFQ8?t=3579) 更酷的是：每個用 GP 的實務領域，都已經（有意或無意地）發現**應該用對數**。無線／纜線功率控制的工程師用**分貝**講功率——那就是 log；電路設計的元件庫尺寸是 0.5、1、1.4、2、4、8、16——他們心裡早就知道該用尺寸的 log。

【Q&A】[▶ 1:00:42](https://youtu.be/d2jF3SXcFQ8?t=3642) 學生問：目標和不等式的項數 $K$ 都一樣嗎？答（想了一下）：**不必一樣**，每個正項式項數可以不同（上式寫 $K_0$、$K_i$）。

**例：懸臂樑設計** [▶ 1:01:12](https://youtu.be/d2jF3SXcFQ8?t=3672)（課本 §4.5.4）

【口頭】老師在一本工程設計最佳化的書裡看到這個例子，書上的重點是「這問題**不是**凸的」——這句話是真的，但換對變數就凸了。老師說細節他「其實也辯護不了」。

- 樑分 $N$ 段，每段的寬 $w_i$、高 $h_i$ 是變數；尖端加垂直力 $F$。做得粗厚就很硬，推了幾乎不動；做得細就會彎很多。
- **目標**：總重（體積）$\sum_iw_ih_i$（各段單位長度）。
- **約束**：
  - 寬、高上下界；長寬比 $S_{\min}\le h_i/w_i\le S_{\max}$（可以是製造限制）。
  - 每段最大應力 $\sigma_i=6iF/(w_ih_i^2)\le\sigma_{\max}$（合理的失效模型）。
  - 尖端撓度 $y_1\le y_{\max}$（「加 10 千牛頓時下垂不超過 3 公分」）。

【課堂討論】[▶ 1:04:48](https://youtu.be/d2jF3SXcFQ8?t=3888) 「用公開場合能講的字」：總重 $\sum w_ih_i$ 是什麼函數？學生：**內積**。凸嗎？不凸，它是矩陣為 $\begin{pmatrix}0&\frac12I\\\frac12I&0\end{pmatrix}$ 的二次型（有負特徵值）。所以原問題不是凸問題。

- 應力、長寬比都是單項式；撓度由從尖端往回的遞迴算出（課本 (4.45)）：
$$v_i=12\left(i-\tfrac12\right)\frac{F}{Ew_ih_i^3}+v_{i+1},\qquad y_i=6\left(i-\tfrac13\right)\frac{F}{Ew_ih_i^3}+v_{i+1}+y_{i+1}$$
  （$v_{N+1}=y_{N+1}=0$）。歸納：單項式＋正項式 = 正項式，所以 $y_1$ 是（複雜的）正項式，整個問題是 GP。

**GP 的組合規則** [▶ 1:06:21](https://youtu.be/d2jF3SXcFQ8?t=3981)

【課堂討論】
| 運算 | 結果 |
|---|---|
| 單項式 × 單項式 | 單項式 |
| 單項式 + 單項式 | 正項式 |
| 正項式 × 正項式 | 正項式 |
| 正項式 ÷ 單項式 | 正項式 |
| 正數 ÷ 正項式 | **不知道**（不在這個類別裡） |

【口頭】[▶ 1:08:28](https://youtu.be/d2jF3SXcFQ8?t=4108) 這些可以寫在物件導向的領域專用語言裡，讓軟體替你轉換。「你編譯之後為什麼要去看 bytecode？」只有極少數人需要看。

**GP 的意義** [▶ 1:08:59](https://youtu.be/d2jF3SXcFQ8?t=4139)：它是「**非凸但可轉換成等價凸問題**」這一大類的第一個例子。

【口頭】[▶ 1:09:31](https://youtu.be/d2jF3SXcFQ8?t=4171) 老師很久以前到處演講，一張投影片說「這是控制裡一個問題，我不認為它是凸的」，講給幾千人聽過。在 Berkeley 講完後，同事 Andy 走過來：「你說可能不凸的那個問題，我可以給你看個東西嗎？」——一個「病態、瘋狂」的換變數：不用這個正定矩陣，改用它的逆；不用這些，改用逆乘那個……「為什麼有人要這樣做？」「看著。」兩行後就是凸的。「我一直在告訴全世界的人它不凸——」回頭看投影片，上面有個小註腳寫著「**可能**」。「所以我安全了。」之後他每次都講這個故事。

---

## 9. 錐形式問題與半正定規劃（SDP）

[▶ 1:10:31](https://youtu.be/d2jF3SXcFQ8?t=4231)

回到真正的凸問題，但約束變成**向量不等式**。

**錐形式問題**（conic form problem）：

$$
\begin{aligned}
\text{minimize}\quad & c^Tx\\
\text{subject to}\quad & Fx+g\preceq_K0\\
& Ax=b
\end{aligned}
$$

- $K=\mathbb{R}^m_+$：就是 LP 的學究寫法。
- $K$ = 二階錐的乘積：SOCP。
- $K=\mathbf{S}^k_+$：SDP。

**半正定規劃**（semidefinite program，SDP）[▶ 1:11:37](https://youtu.be/d2jF3SXcFQ8?t=4297)：

$$
\begin{aligned}
\text{minimize}\quad & c^Tx\\
\text{subject to}\quad & x_1F_1+x_2F_2+\cdots+x_nF_n+G\preceq0\\
& Ax=b
\end{aligned}
\qquad F_i,G\in\mathbf{S}^k
$$

- 如果 $F_i$、$G$ 是純量，這就是一條線性不等式（很蠢的 LP）；但它們是對稱矩陣，約束說這個仿射矩陣函數**半負定**。
- 這條約束叫 **LMI**（linear matrix inequality，線性矩陣不等式）。
- 多個 LMI 可以**對角堆疊**成一個。
- 【口頭】[▶ 1:11:37](https://youtu.be/d2jF3SXcFQ8?t=4297) 最近 20–25 年成為主流：理論電腦科學、物理……都在用。

【課堂討論】[▶ 1:12:40](https://youtu.be/d2jF3SXcFQ8?t=4360) 怎麼把 LP 寫成 SDP？學生：**對角矩陣**。對：$\mathbf{diag}(Gx-h)\preceq0\iff Gx\preceq h$，因為對角矩陣半負定 $\iff$ 對角元素都 $\le0$。所以 **SDP 推廣 LP**。

**SDP 也推廣 SOCP** [▶ 1:13:10](https://youtu.be/d2jF3SXcFQ8?t=4390)，不顯然，要透過 **Schur 補**（之後的作業有一題）。老師再提：統計的高斯條件化、電路把一些埠短路或開路後看剩下的部分——都是 Schur 補。

$$\|Ax+b\|_2\le c^Tx+d\iff\begin{pmatrix}(c^Tx+d)I&Ax+b\\(Ax+b)^T&c^Tx+d\end{pmatrix}\succeq0$$

右邊對 $x$ 是仿射的。理由：區塊矩陣 $\begin{pmatrix}tI&u\\u^T&t\end{pmatrix}$（$t>0$）半正定 $\iff$ Schur 補 $t-u^Tu/t\ge0\iff\|u\|_2^2\le t^2$。

> ⚠️ 逐字稿缺字 [▶ 1:13:43](https://youtu.be/d2jF3SXcFQ8?t=4423)：字幕寫「It also extends **SDP**. And-- sorry, SOCP」（老師自己口誤又改口），以及「**she** put that on one of the next coming homeworks」，可能是「we'll put」。

**例 1：特徵值最小化** [▶ 1:15:15](https://youtu.be/d2jF3SXcFQ8?t=4515)

$$\text{minimize}\quad\lambda_{\max}(A(x)),\qquad A(x)=A_0+x_1A_1+\cdots+x_nA_n,\ A_i\in\mathbf{S}^k$$

已知它是凸的，但「凸不代表顯然怎麼解」。等價的 SDP（就是 $\lambda_{\max}$ 的上圖）：

$$\text{minimize }t\quad\text{s.t.}\quad A(x)\preceq tI$$

因為 $\lambda_{\max}(A)\le t\iff A\preceq tI$。

【課堂討論】[▶ 1:15:45](https://youtu.be/d2jF3SXcFQ8?t=4545) 誰在別處聽過 SDP？一位學生在**理論電腦科學**；老師問「有人知道 SDP 除了理論上之外真的能解嗎？」——「其實不知道。」「我猜也是，我有很多那邊的朋友。」另一位在**統計**。「還不算完全主流，不然一半的人會舉手，但快了。」

**例 2：矩陣範數最小化** [▶ 1:16:47](https://youtu.be/d2jF3SXcFQ8?t=4607)

$$\text{minimize}\quad\|A(x)\|_2=\sigma_{\max}(A(x)),\qquad A(x)=A_0+x_1A_1+\cdots+x_nA_n,\ A_i\in\mathbb{R}^{p\times q}$$

同樣寫成 LMI。【課本補充】§4.6.3：

$$\text{minimize }t\quad\text{s.t.}\quad\begin{pmatrix}tI&A(x)\\A(x)^T&tI\end{pmatrix}\succeq0$$

因為 $\|A\|_2\le t\iff A^TA\preceq t^2I$（$t\ge0$），再用 Schur 補。

「結論是：**這些問題我們現在就是能解**。」下週還有一個很重要的最佳化主題，然後講**對偶**——「還是理論，但非常實用」。

---

## 10. 一頁速查表

### 問題類別階層

$$\text{LP}\subset\text{QP}\subset\text{QCQP}\subset\text{SOCP}\subset\text{SDP}$$

（GP 不在這條鏈上，它是換變數後的凸問題。）

| 類別 | 形式 | 備註 |
|---|---|---|
| LP | $\min c^Tx$ s.t. $Gx\preceq h$，$Ax=b$ | 多面體上的線性函數 |
| QP | $\min\tfrac12x^TPx+q^Tx$，$P\succeq0$，線性約束 | 等高線是橢球；Falcon 9、量化基金 |
| QCQP | 目標與不等式都是凸二次 | |
| SOCP | $\min f^Tx$ s.t. $\|A_ix+b_i\|_2\le c_i^Tx+d_i$ | **不是平方**；凸最佳化的 bytecode |
| GP | $\min$ 正項式 s.t. 正項式 $\le1$、單項式 $=1$ | $y=\log x$ → log-sum-exp |
| SDP | $\min c^Tx$ s.t. $\sum x_iF_i+G\preceq0$ | LMI |

### 轉換技巧

| 問題 | 轉成 | 關鍵一步 |
|---|---|---|
| $\min\max_i(a_i^Tx+b_i)$ | LP | 上圖：$a_i^Tx+b_i\le t$ |
| Chebyshev 中心 | LP | $\sup_{\|u\|\le r}a^T(x_c+u)=a^Tx_c+r\|a\|_2$ |
| 線性分式 | LP | $y=x/(e^Tx+f)$，$z=1/(e^Tx+f)$ |
| 廣義線性分式 | 二分法 | 擬凸 |
| 強健 LP（橢球） | SOCP | $\bar a^Tx+\|P^Tx\|_2\le b$ |
| 機會約束 LP（高斯，$\eta\ge\frac12$） | SOCP | $\bar a^Tx+\Phi^{-1}(\eta)\|\Sigma^{1/2}x\|_2\le b$ |
| GP | 凸 | $\log\sum e^{a_k^Ty+b_k}$ |
| LP | SDP | 對角矩陣 |
| SOCP | SDP | Schur 補：$\begin{pmatrix}tI&u\\u^T&t\end{pmatrix}\succeq0\iff\|u\|_2\le t$ |
| $\min\lambda_{\max}(A(x))$ | SDP | $A(x)\preceq tI$ |
| $\min\|A(x)\|_2$ | SDP | $\begin{pmatrix}tI&A(x)\\A(x)^T&tI\end{pmatrix}\succeq0$ |

### 其他

- 隨機成本：$\min\bar c^Tx+\gamma x^T\Sigma x$；$\gamma<0$（風險追求）不凸。
- GP 規則：單項式封閉於乘除；正項式封閉於加、乘、除以單項式。

---

## 11. 與後續集數的連結

> 以下**不是逐字稿內容**：依課本章節與老師預告推估，做到時再更新。

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 「下週一個很重要的最佳化主題」 | 第 7 集：向量最佳化（課本 §4.7） |
| 對偶 | 第 7 集起（課本第 5 章） |
| CVXPY 把問題編譯成 SOCP／錐形式 | 作業、DCP |
| 強健性、正則化 | 近似與擬合（課本第 6 章） |
| 機會約束、高斯 | 統計估計（課本第 7 章） |
| 最大內接球（Chebyshev 中心） | 幾何問題（課本 §8.5） |
| Schur 補、LMI | 附錄 A.5.5、SDP 應用 |
| 內點法怎麼解這些錐問題 | 課本第 11 章 |

---

## 附：本集一句話總結

> **LP ⊂ QP ⊂ QCQP ⊂ SOCP ⊂ SDP：每一類都能可靠地大規模求解。很多看起來不屬於某類的問題（分段線性、Chebyshev 中心、線性分式、強健與機會約束 LP、特徵值最小化）其實能轉換進去；GP 本身不凸，但取對數後變成 log-sum-exp 的凸問題。實務上 SOCP 就像凸最佳化的 bytecode，高階建模語言把你的問題編譯成它。**

---

*筆記依據 Stephen Boyd「Stanford EE364A Convex Optimization I（2023）」Lecture 6 錄影逐字稿（人工字幕，1:17:50）與 Boyd & Vandenberghe《Convex Optimization》§4.2.5–4.6 整理。*
