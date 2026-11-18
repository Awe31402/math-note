---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 10
lecture: Lecture 10
date: 2023-02-06
video: https://youtu.be/WO-jjaREHCM （part 1）、https://youtu.be/b-CUtAqyrGE （part 2）
notes: 課本沒有這部分（講者離開課本的「繞道」）；用到第 1 章的 Banach 空間與絕對收斂（§1.4）
---

# 第 10 集 · 矩陣指數：繞道線性微分方程組 [▶ 影片](https://youtu.be/WO-jjaREHCM)

← 上一集：[09-existence-theorem-odes](09-existence-theorem-odes.md) ｜ [總目錄](README.md) ｜ 下一集：[11-lebesgue-step-functions](11-lebesgue-step-functions.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 10 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 9:10，自動字幕）；課本無對應章節，整集是 `【口頭】` 內容
> **標記說明**：
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Weierstrass M 檢驗（只提到）](#1-weierstrass-m-檢驗只提到)
- [2. 矩陣指數為什麼收斂](#2-矩陣指數為什麼收斂)
- [3. 線性微分方程組與降階](#3-線性微分方程組與降階)
- [4. 基本解矩陣](#4-基本解矩陣)
- [5. e^{tA} 是基本解矩陣](#5-eta-是基本解矩陣)
- [6. 例子：用 cosh、sinh 算 e^{tA}](#6-例子用-coshsinh-算-eta)
- [7. 特徵向量給出解](#7-特徵向量給出解)
- [8. Jordan 鏈與「魔法公式」](#8-jordan-鏈與魔法公式)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集講者說想花一兩天講「矩陣的分析」。這集就是：用 Banach 空間的工具證明**矩陣指數** $e^A$ 收斂，再說明它為什麼對研究所學生重要——它解線性微分方程組。下一集回到課本第 2 章。

| 主題 | 用到的課程內容 |
|---|---|
| $e^A$ 收斂 | 第 6 集：Banach 空間、Cauchy 數列 |
| $\|AB\|\le\|A\|\|B\|$、Banach 代數 | 第 7 集：算子範數的類比 |
| $x'=Ax$ 的解 | 第 9 集：Picard 迭代 |

---

## 1. Weierstrass M 檢驗（只提到）

[▶ 00:33](https://youtu.be/WO-jjaREHCM?t=33)

講者想先講 **Weierstrass M 檢驗**：一串函數構成的級數，如果每一項都被一個收斂的正數級數 $\sum M_k$ 控制（$|f_k|\le M_k$），則函數級數不只收斂，而且**一致收斂**。學生在複分析可能見過。

講者說他手上的版本是實值函數的，不確定更一般的版本能推廣到哪裡，要回去查，所以今天不講。他覺得這本書缺了一些實分析定理：極限交換順序、M 檢驗之類，「那不是這本書的風格」。[▶ 03:04](https://youtu.be/WO-jjaREHCM?t=184)

---

## 2. 矩陣指數為什麼收斂

[▶ 04:18](https://youtu.be/WO-jjaREHCM?t=258)

**定義**：$A$ 是 $n\times n$ 矩陣（實或複都可以），

$$e^A=I+A+\frac12A^2+\frac1{3!}A^3+\cdots=\sum_{k=0}^\infty\frac1{k!}A^k.$$

**問題**：加無限多個矩陣，有意義嗎？

**空間與範數**[▶ 05:22](https://youtu.be/WO-jjaREHCM?t=322)：$E=\mathbb{R}^{n\times n}$，

$$\|A\|=\sqrt{\operatorname{tr}(AA^T)}=\sqrt{\sum_{i,j}A_{ij}^2}.$$

講者說別被跡（trace）嚇到，這就是「所有元素平方和開根號」，叫 **Frobenius 範數**。Frobenius 是 19 世紀重要的數學家，可以說是第一個真正做 $n$ 維線性代數的人。$E$ 是 $n^2$ 維空間，有限維，所以是 Banach 空間（講者說「你們願意相信的話」）。

**關鍵不等式**[▶ 11:30](https://youtu.be/WO-jjaREHCM?t=690)：

$$\|AB\|\le\|A\|\,\|B\|.$$

講者說這有點像 Cauchy–Schwarz。

- 有乘法的向量空間叫**代數（algebra）**：乘法雙線性、結合，有單位元素。
- 如果範數和乘法這樣配合，而且空間完備，叫 **Banach 代數**。$\mathbb{R}^{n\times n}$ 是一個例子。
- 【課堂討論】講者問：由歸納法，$\|A^k\|$ 怎麼樣？學生答：$\|A^k\|\le\|A\|^k$。

**Cauchy 估計**[▶ 08:53](https://youtu.be/WO-jjaREHCM?t=533)：部分和 $S_n=\sum_{k=0}^n\frac{A^k}{k!}$。$m>n$ 時

$$\|S_m-S_n\|=\left\|\sum_{k=n+1}^m\frac{A^k}{k!}\right\|\le\sum_{k=n+1}^m\frac{\|A^k\|}{k!}\le\sum_{k=n+1}^m\frac{\|A\|^k}{k!}.$$

（講者說他的上下標會差 1，不在意的話照念。）

右邊是**實數**級數 $e^{\|A\|}=\sum\frac{\|A\|^k}{k!}$ 的部分和之差。這個實數級數收斂，所以它的部分和是 $\mathbb{R}$ 中的 Cauchy 數列：給 $\varepsilon$，$m,n$ 夠大時右邊 $<\varepsilon$，於是左邊也 $<\varepsilon$。$(S_n)$ 是 Cauchy 矩陣數列，$\mathbb{R}^{n\times n}$ 完備，所以 $e^A$ 存在。∎

講者說：這完全是這門課的拿手題型——賦範空間中的收斂；關鍵是「它是指數級數的尾巴」。

> 換成第 6 集的語言：$\sum\left\|\frac{A^k}{k!}\right\|\le e^{\|A\|}<\infty$，級數**絕對收斂**；Banach 空間中絕對收斂級數收斂（Theorem 1.4.9）。

---

## 3. 線性微分方程組與降階

[▶ 19:17](https://youtu.be/WO-jjaREHCM?t=1157)

講者「摘下分析的眼罩」，給一個方程組的速成課。

**例 1**：
$$\frac{dx}{dt}=x-y,\quad\frac{dy}{dt}=-x+y\qquad\Longleftrightarrow\qquad\frac{d}{dt}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}.$$

一般寫成 $\dfrac{d\vec r}{dt}=A\vec r$，$A$ 是常數矩陣。

**例 2：降階（reduction of order）**[▶ 21:29](https://youtu.be/WO-jjaREHCM?t=1289)：$x''+x=0$，$y''-y=0$。令

$$x_1=x,\quad x_2=x',\quad x_3=y,\quad x_4=y'.$$

則 $x_1'=x_2$，$x_2'=-x_1$，$x_3'=x_4$，$x_4'=x_3$：

$$\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}'=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}.$$

兩條二階方程換成四條一階方程，矩陣有分塊的樣子。三階方程也一樣：$x_1$ 是未知函數，$x_2$ 是導數，$x_3$ 是二階導數。所以**解 $\vec r'=A\vec r$ 就等於解任何齊次常係數線性微分方程（組）**，不管幾階。

加上初值 $\vec r(0)=\vec r_0$ 後，可以仿照上一集的 Picard 迭代用壓縮映射證明解存在。但實際對方程組做 Picard 迭代很嚇人，所以下面的方法很珍貴。[▶ 25:31](https://youtu.be/WO-jjaREHCM?t=1531)

---

## 4. 基本解矩陣

[▶ 26:04](https://youtu.be/WO-jjaREHCM?t=1564)

**理論**（講者說在 Nagle–Saff–Snider 第 9 章左右）：$A$ 是 $n\times n$ 矩陣，則 $\vec r'=A\vec r$ 有 $n$ 個**線性獨立**的解 $\vec r_1,\dots,\vec r_n$（不唯一），通解是

$$\vec r=c_1\vec r_1+\cdots+c_n\vec r_n=R\,\vec c,\qquad R=[\vec r_1|\cdots|\vec r_n].$$

- 線性獨立 ⟺ $\det R\ne0$。$\det R$ 是方程組的 **Wronskian**；方程組的 Wronskian 不需要導數，因為每一行已經是向量解。降階後的方程組和原來二階方程的 Wronskian 有關係。⚠️ 逐字稿缺字：字幕把 Wronskian 聽成「ronskian」。
- 每一行都是解的矩陣叫**解矩陣**；如果還可逆，叫**基本解矩陣（fundamental solution matrix）**。

**矩陣形式**[▶ 30:51](https://youtu.be/WO-jjaREHCM?t=1851)：每行 $\vec r_j'=A\vec r_j$，並排起來是

$$\frac{dR}{dt}=AR.$$

矩陣函數的導數 = 每個元素分別微分。所以找 $n$ 個行解，等於找一個滿足 $R'=AR$ 的矩陣。

---

## 5. e^{tA} 是基本解矩陣

### 5.1 是解矩陣

[▶ 32:45](https://youtu.be/WO-jjaREHCM?t=1965)

類比一變數：$y'=ay$ 的解是 $e^{at}$。猜 $R=e^{tA}$。收斂：剛才對任意 $A$ 證過，把 $A$ 換成 $tA$ 就好。

$$e^{tA}=I+tA+\frac{t^2}{2}A^2+\frac{t^3}{3!}A^3+\cdots$$

【Q&A】[▶ 34:01](https://youtu.be/WO-jjaREHCM?t=2041) 學生問能不能寫成 $(e^t)^A$。講者：我們只定義了「$e$ 的矩陣次方」，沒定義「$e^t$ 的矩陣次方」，這值得想但他不知道。

**逐項微分**[▶ 34:34](https://youtu.be/WO-jjaREHCM?t=2074)：

$$\frac{d}{dt}e^{tA}=A+tA^2+\frac{t^2}{2}A^3+\cdots=A\left(I+tA+\frac{t^2}{2}A^2+\cdots\right)=Ae^{tA}.$$

講者坦白：可以逐項微分需要一個分析定理（一致收斂的函數級數），課本沒有，他今天也沒證，「所以只是準嚴格」。他說：你當研究生帶微分方程課時這樣做，工程系學生不會眨眼。

### 5.2 可逆

[▶ 37:03](https://youtu.be/WO-jjaREHCM?t=2223)

【課堂討論】學生說 $n\times n$ 矩陣很多都不可逆，怎麼知道 $e^{tA}$ 可逆？講者先看一變數：$e^{at}e^{-at}=1$，所以 $e^{at}$ 可逆。矩陣呢？矩陣指數像普通指數，但不完全一樣。

**Baker–Campbell–Hausdorff 公式**[▶ 39:44](https://youtu.be/WO-jjaREHCM?t=2384)：

$$e^Ae^B=\exp\left(A+B+\frac12[A,B]+\frac1{12}\big([A,[A,B]]+[B,[B,A]]\big)+\cdots\right),\qquad[A,B]=AB-BA.$$

$[A,B]$ 叫**交換子（commutator）**，後面的項是交換子的交換子。講者記得 Hausdorff 的拼法，Campbell 的總是記不得。如果知道交換子怎麼算，就完全知道兩個指數形式的矩陣怎麼相乘。這是 **Lie 代數與 Lie 群**故事的一部分：$A,B$ 在 Lie 代數，$e^A,e^B$ 在 Lie 群。

**推論**：若 $AB=BA$，所有交換子都是 0，

$$e^Ae^B=e^{A+B}.$$

取 $B=-A$（$A$ 和 $-A$ 交換）：$e^Ae^{-A}=e^0=I$。所以

$$\left(e^{tA}\right)^{-1}=e^{-tA}.$$

**每個矩陣指數都可逆**。所以 $e^{tA}$ 是基本解矩陣，齊次方程組 $\vec r'=A\vec r$ 解完了。

**另一個看法**[▶ 42:41](https://youtu.be/WO-jjaREHCM?t=2561)：
$$\det e^A=e^{\operatorname{tr}A}>0.$$
跡是對角線元素之和。所以矩陣指數的行列式永遠是正的。

---

## 6. 例子：用 cosh、sinh 算 e^{tA}

[▶ 43:49](https://youtu.be/WO-jjaREHCM?t=2629)

例 1 的 $A=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}=I-J$，其中 $J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$。

1. $I$ 和 $J$ 交換，所以 $e^{tA}=e^{tI}e^{-tJ}$，不用動用 BCH。
2. $e^{tI}=e^tI$：對角矩陣的指數就是對角元素各自取指數（講者說是作業題）。
3. **$J$ 的次方**【課堂討論】[▶ 45:14](https://youtu.be/WO-jjaREHCM?t=2714)：$J^2=I$（講者一度算錯，學生糾正）。所以 $J^{2k}=I$，$J^{2k+1}=J$。
4. 用雙曲函數：$e^\theta=\cosh\theta+\sinh\theta$，cosh 是指數級數的偶次項，sinh 是奇次項。把它們推廣到矩陣（用冪級數定義）：
   $$e^{-tJ}=\cosh(-tJ)+\sinh(-tJ)=\cosh t\cdot I-\sinh t\cdot J,$$
   因為 cosh 只有偶次方（$J^{2k}=I$），sinh 只有奇次方（$J^{2k+1}=J$）。
5. 所以
   $$e^{tA}=e^t\begin{pmatrix}\cosh t&-\sinh t\\-\sinh t&\cosh t\end{pmatrix}.$$

兩行就是兩個線性獨立解：$e^t\begin{pmatrix}\cosh t\\-\sinh t\end{pmatrix}$、$e^t\begin{pmatrix}-\sinh t\\\cosh t\end{pmatrix}$。

> 以下**不是逐字稿內容**，是驗算：$e^t\cosh t=\frac{e^{2t}+1}{2}$，$e^t\sinh t=\frac{e^{2t}-1}{2}$，所以解是 $1$ 和 $e^{2t}$ 的組合。這符合 $A$ 的特徵值 $0$ 和 $2$。（字幕把結果念成「e^T cos T」，應是 cosh。）

講者說這個例子「很湊巧」能算。用冪級數硬算也不必含糊。

---

## 7. 特徵向量給出解

[▶ 51:01](https://youtu.be/WO-jjaREHCM?t=3061)

矩陣不漂亮時怎麼辦？學生修微分方程時學過特徵向量法。

**猜** $\vec r=e^{\lambda t}\vec u$（$\vec u$ 常向量）。代入：

$$\lambda e^{\lambda t}\vec u=Ae^{\lambda t}\vec u\quad\Longrightarrow\quad A\vec u=\lambda\vec u.$$

（$e^{\lambda t}\ne0$。）所以 $\vec u$ 是特徵值 $\lambda$ 的**特徵向量**。

**跟 $e^{tA}$ 的關係**[▶ 52:47](https://youtu.be/WO-jjaREHCM?t=3167)：$A\vec u=\lambda\vec u$ ⟹ $A^k\vec u=\lambda^k\vec u$（做兩次就能做 $k$ 次），所以

$$e^{tA}\vec u=\vec u+t\lambda\vec u+\frac{t^2\lambda^2}{2}\vec u+\cdots=e^{\lambda t}\vec u.$$

講者解釋：矩陣乘行向量 = 矩陣各行的線性組合；所以 $e^{\lambda t}\vec u$ 是 $e^{tA}$ 各行（函數）的線性組合，「藏在裡面」。

- $A$ **可對角化**（特徵向量夠多，構成基底）時，這樣的解夠用。
- 特徵值可能是複數：取複特徵解的實部、虛部，得到 sin、cos 乘指數。

---

## 8. Jordan 鏈與「魔法公式」

### 8.1 不可對角化的例子

[▶ 56:48](https://youtu.be/WO-jjaREHCM?t=3408)

$A=\begin{pmatrix}3&1\\0&3\end{pmatrix}$。

- $Ae_1=3e_1$：$e_1$ 是特徵值 3 的特徵向量。
- $Ae_2=$ 第二行 $=e_1+3e_2$，即 $(A-3I)e_2=e_1$。

所以 $(A-3I)e_1=0$、$(A-3I)e_2=e_1$、$(A-3I)^2e_2=0$。這叫 **Jordan 鏈**：$e_1$ 是特徵向量，$e_2$ 是 **2 階廣義特徵向量**。（有人讓鏈從特徵向量往上走，有人從最高階往下走。）

**Jordan 標準形**[▶ 59:06](https://youtu.be/WO-jjaREHCM?t=3546)：任何矩陣都有 Jordan 基底，$A=PJP^{-1}$（講者口述成 $P^{-1}AP$ 是 Jordan 形），$J$ 是分塊對角，每塊反映一個特徵值；可對角化時就是對角矩陣。講者說：這是線性代數的大定理，大學課常常不深入講，很可惜；它應該是線代課的焦點和結尾，因為它完全決定了什麼能做、什麼不能做。

### 8.2 魔法公式

[▶ part 2 00:43](https://youtu.be/b-CUtAqyrGE?t=43)

對任意數 $\lambda$（不一定是特徵值，可以是複數），$\lambda I$ 跟什麼都交換，所以

$$e^{tA}=e^{t\lambda I}e^{t(A-\lambda I)}=e^{\lambda t}\left(I+t(A-\lambda I)+\frac{t^2}{2}(A-\lambda I)^2+\cdots\right).$$

講者叫它「**魔法公式**」，因為它讓人看清楚為什麼特徵向量這麼好用：

- 若 $\vec u$ 是特徵值 $\lambda$ 的特徵向量，$(A-\lambda I)\vec u=0$，後面全是 0：$e^{tA}\vec u=e^{\lambda t}\vec u$。
- 若 $\vec u$ 在 Jordan 鏈裡，級數會**截斷**成有限項。

**算例**[▶ part 2 03:33](https://youtu.be/b-CUtAqyrGE?t=213)：上例，$\lambda=3$，作用在 $e_2$：

$$e^{tA}e_2=e^{3t}\left(e_2+t(A-3I)e_2+\frac{t^2}2(A-3I)^2e_2+\cdots\right)=e^{3t}(e_2+te_1)=\begin{pmatrix}te^{3t}\\e^{3t}\end{pmatrix}.$$

**驗算**：$x=te^{3t}$，$y=e^{3t}$。

- $y'=3e^{3t}=3y$ ✓。
- $3x+y=3te^{3t}+e^{3t}$，而 $x'=e^{3t}+3te^{3t}$ ✓。

**重根時的 $t$ 從哪裡來**[▶ part 2 06:32](https://youtu.be/b-CUtAqyrGE?t=392)：微分方程課說「特徵根重複時解多乘一個 $t$」。一個解釋是：對應的方程組不可對角化，需要 2 階廣義特徵向量，魔法公式就帶出 $te^{\lambda t}$。講者說至少有十種方法解釋這個 $t$。

**總結**[▶ part 2 07:05](https://youtu.be/b-CUtAqyrGE?t=425)：要解 $\vec r'=A\vec r$，學會找 Jordan 基底（滿足鏈條件的廣義特徵向量），餵給矩陣指數，解就跑出來。複特徵值時會成對出現 sin、cos 乘指數。非齊次問題也有方法。而一開始的收斂分析對**任何**矩陣都成立。

下一集講者「會乖乖的」，回到第 2 章 Lebesgue 積分。

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 矩陣指數 | $e^A=\sum_{k\ge0}A^k/k!$ | |
| 收斂 | Frobenius 範數 $\|A\|=\sqrt{\sum A_{ij}^2}$ | $\|A^k\|\le\|A\|^k$；被 $e^{\|A\|}$ 的尾巴控制 |
| Banach 代數 | 完備 + $\|AB\|\le\|A\|\|B\|$ | |
| 降階 | 高階線性 ODE ⟹ $\vec r'=A\vec r$ | $x_1=x,\ x_2=x',\dots$ |
| 基本解矩陣 | 每行是解且可逆；$R'=AR$ | $\det R$ = Wronskian |
| $e^{tA}$ 是解 | $\frac{d}{dt}e^{tA}=Ae^{tA}$ | 逐項微分（未證） |
| 可逆 | $AB=BA\Rightarrow e^Ae^B=e^{A+B}$；$(e^{tA})^{-1}=e^{-tA}$ | BCH 公式；$\det e^A=e^{\operatorname{tr}A}$ |
| 例 | $A=I-J$，$J^2=I$ | $e^{tA}=e^t(\cosh t\,I-\sinh t\,J)$ |
| 特徵向量 | $A\vec u=\lambda\vec u\Rightarrow e^{tA}\vec u=e^{\lambda t}\vec u$ | $A^k\vec u=\lambda^k\vec u$ |
| 魔法公式 | $e^{tA}=e^{\lambda t}\sum\frac{t^k}{k!}(A-\lambda I)^k$ | Jordan 鏈上級數截斷 |
| Jordan 例 | $A=\begin{pmatrix}3&1\\0&3\end{pmatrix}$ | $e^{tA}e_2=e^{3t}(e_2+te_1)$，重根的 $t$ |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 一致收斂的函數級數、逐項微分 | 第 13–14 集：Lebesgue 積分下的級數與極限交換 |
| 特徵值、特徵向量、對角化 | 第 27–29 集：Hilbert 空間算子的特徵值、譜定理 |
| $e^{tA}$、Lie 群 | 第 33–34 集：量子力學的時間演化 $e^{-itH/\hbar}$ |

---

## 附：本集一句話總結

> **矩陣指數 $e^A$ 收斂，因為在完備的矩陣空間裡它被實數級數 $e^{\|A\|}$ 控制；$e^{tA}$ 滿足 $R'=AR$ 而且可逆（$e^{-tA}$ 是反矩陣），所以是 $\vec r'=A\vec r$ 的基本解矩陣——而「魔法公式」$e^{tA}=e^{\lambda t}e^{t(A-\lambda I)}$ 說明了特徵向量與 Jordan 鏈為什麼能把它算出來。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-06 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 9:10）整理；本集內容課本沒有。*
