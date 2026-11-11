---
course: Stanford EE364A Convex Optimization I（2023）
episode: 3
lecture: Lecture 3
date: 待補
video: https://youtu.be/1menqhfNzzo
notes: 《Convex Optimization》§2.4.2、§2.5–2.6（書頁 45–57，PDF 頁 59–71）；§3.1、§3.2.1–3.2.2（書頁 67–80，PDF 頁 81–94）
---

# 第 3 集 · Lecture 3：分離超平面、對偶錐、凸函數（Convex Functions） [▶ 影片](https://youtu.be/1menqhfNzzo)

← 上一集：[02-convex-sets](02-convex-sets.md) ｜ [總目錄](README.md) ｜ 下一集：[04-convex-functions-2](04-convex-functions-2.md) →

> **課程**：Stanford EE364A Convex Optimization I，2023 — 第 3 集
> **講者**：Stephen Boyd
> **來源**：YouTube 錄影逐字稿（1:20:28，人工字幕 en-US）＋ Boyd & Vandenberghe《Convex Optimization》§2.5–2.6、§3.1–3.2
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 開場與複習：最小、極小](#1-開場與複習最小極小)
- [2. 分離超平面定理](#2-分離超平面定理)
- [3. 支撐超平面](#3-支撐超平面)
- [4. 對偶錐](#4-對偶錐)
- [5. 用對偶錐刻畫最小與極小元素](#5-用對偶錐刻畫最小與極小元素)
- [6. 凸函數的定義](#6-凸函數的定義)
- [7. 凸函數的例子](#7-凸函數的例子)
- [8. 限制在直線上](#8-限制在直線上)
- [9. 延伸值延拓](#9-延伸值延拓)
- [10. 一階條件：全域下界](#10-一階條件全域下界)
- [11. 二階條件與例子](#11-二階條件與例子)
- [12. 下水平集與上圖](#12-下水平集與上圖)
- [13. Jensen 不等式](#13-jensen-不等式)
- [14. 怎麼證明函數是凸的：凸性的微積分](#14-怎麼證明函數是凸的凸性的微積分)
- [15. 一頁速查表](#15-一頁速查表)
- [16. 與後續集數的連結](#16-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 最小／極小元素（複習） | §2.4.2 |
| 分離與支撐超平面 | §2.5 |
| 對偶錐、用對偶錐刻畫最小／極小 | §2.6.1、§2.6.3 |
| 凸函數定義、例子、限制在直線上、延伸值 | §3.1.1–3.1.2、§3.1.5 |
| 一階、二階條件 | §3.1.3–3.1.4 |
| 下水平集、上圖、Jensen | §3.1.6–3.1.8 |
| 保凸運算：非負加權和、仿射合成 | §3.2.1–3.2.2 |

課本 §2.6.2（對偶廣義不等式、擇一定理）本集沒講。

---

## 1. 開場與複習：最小、極小

[▶ 00:05](https://youtu.be/1menqhfNzzo?t=5)

- 週五交的作業只用到週二的內容。Homework 1 有些部分相當難，「這不是週四晚上才做的作業」，要**慢慢品嚐**。在一題卡了幾小時就**先走開**，完全沒關係。
- 【口頭】[▶ 01:09](https://youtu.be/1menqhfNzzo?t=69) 以前的學生說：寫 Homework 1、2 時完全不知道在幹嘛，到 Homework 8、9 拿來擬合模型、最佳化網路流量時才「全懂了」。
- 這週繼續「**數學苦行**」（slog），週五結束；下週「太陽就出來了」。

**複習** [▶ 02:11](https://youtu.be/1menqhfNzzo?t=131)：廣義不等式實務上幾乎只用兩個錐——非負象限（比較向量）和半正定錐（比較對稱矩陣）。好記號會讓你想起實數不等式，「很多性質保留、有些不保留」；最重要的差別是**不是全序**。

**下確界** [▶ 04:46](https://youtu.be/1menqhfNzzo?t=286)：無限集合的 min 換成**下確界**（infimum，inf）。不熟就把它當 min，「只是適用於無限集合的 min」。

最小 vs 極小（見[第 2 集 §7.3](02-convex-sets.md#73-最小元素與極小元素)）：最小元素若存在則唯一——「證明之前要說 *a* minimum，證明之後才能說 *the* minimum」[▶ 05:47](https://youtu.be/1menqhfNzzo?t=347)。圖中 $S_2$ 左下邊界那段線上的每個點都是極小點；邊界內部的點不是，因為有可比較、更小、又不相等的點。

【Q&A】[▶ 06:52](https://youtu.be/1menqhfNzzo?t=412) 學生問：換一個錐，極小點會不一樣？答：**最小、極小永遠是相對於某個特定的錐**。老師在 $\mathbb{R}^2$ 畫一個比象限窄的錐，問 $x_2$ 對它還是極小嗎？有學生猜不是，有學生說是。老師畫出 $x_2-K$ 和 $S_2$ 的交集，只有 $x_2$ 一點，所以**仍是極小**。

> 以下**不是逐字稿內容**，是推論的：錐越窄，$x-K$ 越小，越容易只交在 $x$ 一點，所以「對窄錐是極小」比「對寬錐是極小」更容易成立。

---

## 2. 分離超平面定理

[▶ 08:22](https://youtu.be/1menqhfNzzo?t=502)

【口頭】很有名，看起來很無害，但「可以合理地主張我們做的每件事都只建立在它上面」。

**定理**（課本 §2.5.1）：$C$、$D$ 是非空、**不相交**的凸集（$C\cap D=\varnothing$），則存在 $a\ne0$ 和 $b$ 使

$$a^Tx\le b\ \ \forall x\in C,\qquad a^Tx\ge b\ \ \forall x\in D$$

即超平面 $\{x\mid a^Tx=b\}$ 把兩者分開。機器學習裡叫「**線性可分**」（linearly separable）。

- 【口頭】[▶ 09:55](https://youtu.be/1menqhfNzzo?t=595) 它是很多**經濟學**的基礎，例如之後的「無套利」（no arbitrage）就會是這樣一張圖（只是不在 2 維）。
- 變體非常多（例如什麼時候能**嚴格分離**），「你不需要知道，腦中有這張圖就好」。證明「不太難，我們不做」。

【課本補充】§2.5.1 特殊情況的證明：假設 $C$、$D$ 的距離 $\mathrm{dist}(C,D)=\inf\{\|u-v\|_2\mid u\in C,v\in D\}$ 為正，而且存在達到距離的點 $c\in C$、$d\in D$。令

$$a=d-c,\qquad b=\frac{\|d\|_2^2-\|c\|_2^2}{2}$$

超平面是 $c$、$d$ 連線的**垂直平分面**。要證 $f(x)=a^Tx-b$ 在 $D$ 上非負（$C$ 上非正同理）：若有 $u\in D$ 使 $f(u)<0$，可以寫 $f(u)=(d-c)^T\left(u-d+\tfrac12(d-c)\right)=(d-c)^T(u-d)+\tfrac12\|d-c\|_2^2$，所以 $(d-c)^T(u-d)<0$。這表示從 $d$ 往 $u$ 走一小步，$\frac{d}{dt}\|d+t(u-d)-c\|_2^2\big|_{t=0}=2(d-c)^T(u-d)<0$，距離會變小；而 $D$ 凸，$d+t(u-d)\in D$，和 $d$ 是 $D$ 中離 $C$ 最近的點矛盾。

【Q&A】[▶ 10:57](https://youtu.be/1menqhfNzzo?t=657) 學生問投影片上的 **singleton** 是什麼？答：**單元素集合**（只有一個元素的集合），是「高級 BBC 數學」，每個人都該會講一點。

---

## 3. 支撐超平面

[▶ 11:57](https://youtu.be/1menqhfNzzo?t=717)

**支撐超平面**（supporting hyperplane）：集合 $C$（不一定凸）邊界上一點 $x_0$，超平面 $\{x\mid a^Tx=a^Tx_0\}$（$a\ne0$）通過 $x_0$，而且 $C$ 整個落在其中一側：$a^Tx\le a^Tx_0$ 對所有 $x\in C$。直覺上是在 $x_0$ **相切**。（邊界不知道定義就用眼睛看。）

**支撐超平面定理**：$C$ 非空凸，則**邊界上每一點**都有支撐超平面。

【課堂討論】[▶ 12:58](https://youtu.be/1menqhfNzzo?t=778)：
- 光滑邊界上的點：有一個支撐超平面（切線）。
- **角**（kink）上的點：有幾個？學生答：**不只一個**。對。
- 非凸集合凹進去的點：**沒有**支撐超平面。

**部分逆命題** [▶ 13:29](https://youtu.be/1menqhfNzzo?t=809)：若集合在邊界每一點都有支撐超平面，則它是凸的。

【課本補充】§2.5.2：支撐超平面定理可由分離定理推出——$C$ 內部非空時，對 $\{x_0\}$ 和 $\mathbf{int}\,C$ 用分離定理；內部為空時 $C$ 落在一個較低維的仿射集裡，包含該仿射集的超平面就是（平凡的）支撐超平面。逆命題要求集合**閉、內部非空**。

---

## 4. 對偶錐

[▶ 14:00](https://youtu.be/1menqhfNzzo?t=840)

**先看線性代數的版本**：子空間 $V$ 的**正交補**（orthogonal complement）
$$V^\perp=\{y\mid y^Tx=0\ \ \forall x\in V\}$$

對偶錐是同一個概念，只是把等式換成不等式。【口頭】「數學上我們做的事就是**帶有不對稱的線性代數**。」

**定義**（課本 (2.19)）：錐 $K$ 的**對偶錐**（dual cone）
$$K^*=\{y\mid x^Ty\ge0\ \ \forall x\in K\}$$
即和 $K$ 中**每個**向量內積非負（夾角不超過 90°）的向量。

**例子**（老師在 $\mathbb{R}^2$ 黑板上逐一討論）：

| $K$ | $K^*$ | 說明 |
|---|---|---|
| $\{0\}$ | $\mathbb{R}^2$ | 【課堂討論】[▶ 16:33](https://youtu.be/1menqhfNzzo?t=993) 學生答 $\mathbb{R}^2$：任何向量和 0 內積都是 0 $\ge0$ |
| $\mathbb{R}^2$ | $\{0\}$ | 只有 0 和所有向量內積都非負 |
| 射線 $\{tv\mid t\ge0\}$ | 半空間 $\{y\mid v^Ty\ge0\}$ | 【課堂討論】[▶ 19:12](https://youtu.be/1menqhfNzzo?t=1152) 學生答「和它正交的那個半空間」，老師帶大家逐點檢查 |
| $\mathbb{R}^n_+$ | $\mathbb{R}^n_+$ | **自對偶**（self-dual）[▶ 21:12](https://youtu.be/1menqhfNzzo?t=1272) |

**「小 ↔ 大」與「做兩次回到原點」** [▶ 17:07](https://youtu.be/1menqhfNzzo?t=1027)

【口頭】
- 錐越小，對偶錐越大：$\{0\}$ 最小 → 對偶是全空間；射線是「很尖的小錐」→ 對偶是半空間，「鈍到不能再鈍」。像 Fourier 轉換：時間上很窄的訊號，頻譜很寬。
- **共軛類概念做兩次會回到原來**：複數的共軛的共軛是自己；$V^{\perp\perp}=V$。「$V^{\perp\perp}$ 是『和所有正交於 $V$ 中所有向量的向量都正交的向量』——你可以假裝懂，但我不懂，沒有人類能懂」；用強大的記號久了就習慣了。$\{0\}^{**}=\{0\}$ 也一樣。

【課本補充】§2.6.1 更多例子與性質：
- 子空間 $V$ 的對偶錐是 $V^\perp$。
- $\mathbf{S}^n_+$ 自對偶（內積 $\mathrm{tr}(XY)$）。證明：若 $Y\not\succeq0$，有 $q$ 使 $q^TYq=\mathrm{tr}(qq^TY)<0$，取 $X=qq^T\succeq0$ 得 $\mathrm{tr}(XY)<0$；反之若 $X,Y\succeq0$，寫 $X=\sum_i\lambda_iq_iq_i^T$（$\lambda_i\ge0$），$\mathrm{tr}(YX)=\sum_i\lambda_iq_i^TYq_i\ge0$。
- 範數錐 $\{(x,t)\mid\|x\|\le t\}$ 的對偶是**對偶範數**錐 $\{(u,v)\mid\|u\|_*\le v\}$，$\|u\|_*=\sup\{u^Tx\mid\|x\|\le1\}$。
- $K^*$ 永遠是閉凸錐；$K_1\subseteq K_2\Rightarrow K_2^*\subseteq K_1^*$（「小 ↔ 大」的精確版）；$K$ 閉凸時 $K^{**}=K$。
- 幾何：$y\in K^*\iff-y$ 是在原點支撐 $K$ 的超平面的法向量。

【口頭】[▶ 20:42](https://youtu.be/1menqhfNzzo?t=1242) 有些對偶錐要真的證明，會用到 Cauchy–Schwarz 之類，「最好留給作業」。

---

## 5. 用對偶錐刻畫最小與極小元素

[▶ 22:12](https://youtu.be/1menqhfNzzo?t=1332)

設 $K$ 是真錐，$\lambda\succ_{K^*}0$ 表示 $\lambda\in\mathbf{int}\,K^*$（$K=\mathbb{R}^n_+$ 時就是 $\lambda$ 每個分量都 $>0$）。

| 結論 | 意思（$K=\mathbb{R}^n_+$ 時） |
|---|---|
| $x$ 是 $S$ 的**最小元素** $\iff$ 對**所有** $\lambda\succ_{K^*}0$，$x$ 是 $\lambda^Tz$ 在 $S$ 上的**唯一**最小化者 | 不管用什麼正權重加權，最小化結果都是同一個 $x$ [▶ 23:14](https://youtu.be/1menqhfNzzo?t=1394) |
| 若 $\lambda\succ_{K^*}0$ 且 $x$ 最小化 $\lambda^Tz$（$z\in S$），則 $x$ 是**極小元素** | 任取正權重，最小化加權和，**保證**得到極小點 [▶ 23:44](https://youtu.be/1menqhfNzzo?t=1424) |

【口頭】第二條你在別處看過：多目標最佳化時把各目標用非負權重加起來最小化，得到 **Pareto 最佳**解。之後會詳細講。

【Q&A】[▶ 24:15](https://youtu.be/1menqhfNzzo?t=1455) 學生問 $z$ 是什麼？答：**啞變數**（dummy variable），$f(z)=\lambda^Tz$，換成你喜歡的字母都行。

【Q&A】[▶ 24:45](https://youtu.be/1menqhfNzzo?t=1485) 學生問 $\lambda$ 是什麼意思？答：任何在對偶不等式下為正的向量。「現在很怪又沒脈絡，不用太擔心。」

【課本補充】§2.6.3 的證明與注意事項：
- **極小那條**：設 $\lambda\succ_{K^*}0$、$x$ 最小化 $\lambda^Tz$，但 $x$ 不極小，即有 $z\in S$、$z\ne x$、$z\preceq_Kx$。則 $x-z\in K\setminus\{0\}$，而 $\lambda\in\mathbf{int}\,K^*$ 對 $K$ 中非零向量內積**嚴格**為正，所以 $\lambda^T(x-z)>0$，即 $\lambda^Tz<\lambda^Tx$，矛盾。
- **逆命題一般不成立**：極小點不一定是任何 $\lambda$ 的加權和最小化者（課本 Figure 2.25，非凸集合凹進去的極小點）。但若 $S$ **凸**，每個極小點都是某個**非零** $\lambda\succeq_{K^*}0$ 的最小化者（用分離超平面定理證）；這裡不能加強成 $\lambda\succ_{K^*}0$。
- 這些刻畫**不需要** $S$ 凸（逆命題除外）。

**例：生產集** [▶ 24:45](https://youtu.be/1menqhfNzzo?t=1485)（課本 Example 2.27）

- 要生產一種產品，有很多生產方法；每種方法對應一個資源用量向量（這裡是燃料、人工）。所有可行方法構成**生產集** $P$。
- 資源都**有正價值**，所以左下方越好。

【課堂討論】[▶ 25:46](https://youtu.be/1menqhfNzzo?t=1546) 老師指著 $P$ 內部一點問「這樣經營如何？」有學生說「不有效率」（not efficient）。老師：「技術名詞是：那是**愚蠢的選擇**。」因為存在另一點用更少燃料、更少人工做出同樣產品。有人問「你又不知道燃料和人工的價格」——「只要價格是正的，這個就比較好。」

- 極小元素 = **Pareto 最佳**、**有效率**的生產方法；極小元素構成**有效生產前緣**（efficient production frontier）。
- 【課本補充】用任意正價格 $\lambda\succ0$ 最小化總成本 $\lambda^Tx$，得到的方法一定是 Pareto 最佳（上一段的結論）；$\lambda_i$ 就是資源 $i$ 的價格。

---

## 6. 凸函數的定義

[▶ 27:18](https://youtu.be/1menqhfNzzo?t=1638)

$f:\mathbb{R}^n\to\mathbb{R}$ 是**凸函數**（convex function）若**定義域** $\mathbf{dom}\,f$（$f$ 有定義的點）是凸集，而且

$$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y),\qquad\forall x,y\in\mathbf{dom}\,f,\ 0\le\theta\le1$$

- 幾何：連接 $(x,f(x))$、$(y,f(y))$ 的**弦**（chord）在圖形上方。
- 老師的說法：**非負曲率**；曲率為 0 是仿射函數。「凸性就是在講**二階導數的符號**。」
- **凹**（concave）：$-f$ 是凸的（往下彎）。
- **嚴格凸**（strictly convex）：$x\ne y$、$0<\theta<1$ 時不等式嚴格成立。
- 讀法 [▶ 28:50](https://youtu.be/1menqhfNzzo?t=1730)：**「混合的 $f$ ≤ $f$ 的混合」**。

> ⚠️ 逐字稿缺字 [▶ 28:19](https://youtu.be/1menqhfNzzo?t=1699)：字幕寫「the **sine** of the second derivative」，應為 **sign**（符號）。

---

## 7. 凸函數的例子

**在 $\mathbb{R}$ 上** [▶ 28:50](https://youtu.be/1menqhfNzzo?t=1730)：怎麼檢查？「**在腦中畫出來**」。（「除非你被一群不友善的數學家審問，不能畫圖，才要真的證。」）

| 凸 | 凹 |
|---|---|
| 仿射 $ax+b$（弦就在線上，等號成立） | 仿射 $ax+b$ |
| 指數 $e^{ax}$（$a$ 任意實數） | 冪 $x^\alpha$，$0\le\alpha\le1$，$x>0$（例：$\sqrt x$、$x^{0.7}$） |
| 冪 $x^\alpha$，$\alpha\ge1$ 或 $\alpha\le0$，$x>0$（例：$1/x$） | 對數 $\log x$，$x>0$ |
| $\lvert x\rvert^p$，$p\ge1$ | |
| 負熵 $x\log x$，$x>0$（0 附近很陡，在 $x=1$ 為 0） | 熵 $-x\log x$ |

**在 $\mathbb{R}^n$ 上** [▶ 31:29](https://youtu.be/1menqhfNzzo?t=1889)：
- 仿射 $a^Tx+b$：**既凸又凹**（曲率 0 剛好在邊界上）。
- **任何範數**都是凸的。例如 $p$ 範數 $\|x\|_p=\left(\sum_i|x_i|^p\right)^{1/p}$，$p\ge1$：
  - $\|x\|_2$：平方和開根號。
  - $\|x\|_3$：三次方和開立方，「用來做什麼？我不知道」。
  - $\|x\|_1=\sum_i|x_i|$：很多應用合理。
  - $\|x\|_\infty=\max_i|x_i|$。

【課本補充】範數凸的一行證明：$\|\theta x+(1-\theta)y\|\le\|\theta x\|+\|(1-\theta)y\|=\theta\|x\|+(1-\theta)\|y\|$（三角不等式＋齊次性）。

**在矩陣上** [▶ 33:03](https://youtu.be/1menqhfNzzo?t=1983)：引數是矩陣，例如行列式、跡、矩陣範數。

**矩陣上的仿射函數**：$f(X)=\mathrm{tr}(A^TX)+b$。$\mathrm{tr}(A^TB)$ 其實就是兩個矩陣的**內積** [▶ 34:05](https://youtu.be/1menqhfNzzo?t=2045)。老師現場驗證：把 $A$、$B$ 寫成行 $a_j$、$b_j$，$A^TB$ 的 $(j,j)$ 元素是 $a_j^Tb_j$，所以

$$\mathrm{tr}(A^TB)=\sum_{j}a_j^Tb_j=\sum_{i,j}A_{ij}B_{ij}$$

有人寫成 $\mathrm{vec}(A)^T\mathrm{vec}(B)$（vec 把矩陣元素依某順序排成向量；不是標準記號但大家懂）。

**譜範數**（spectral norm，誘導 2 範數）[▶ 36:10](https://youtu.be/1menqhfNzzo?t=2170)：
$$f(X)=\|X\|_2=\sigma_{\max}(X)=\left(\lambda_{\max}(X^TX)\right)^{1/2}$$
凸（範數的性質）。【口頭】維度大於 5 時寫不出解析式：要解 $\det(X^TX-\lambda I)=0$，至少五次多項式，沒有求根公式——但這不妨礙大家一直在用。

---

## 8. 限制在直線上

[▶ 37:12](https://youtu.be/1menqhfNzzo?t=2232)

$$f\text{ 凸}\iff g(t)=f(x+tv)\text{ 對所有 }x\in\mathbf{dom}\,f\text{、所有 }v\text{ 都凸（}\mathbf{dom}\,g=\{t\mid x+tv\in\mathbf{dom}\,f\}\text{）}$$

$g$ 是單變數函數，可以畫出來用眼睛看。

【口頭】[▶ 37:42](https://youtu.be/1menqhfNzzo?t=2262) 又一個街頭方法：隨機產生直線、畫出限制後的函數；只要看到一點點不凸就宣布「不凸」。只能證偽。

**例：$\log\det X$ 是凹的**（$\mathbf{dom}=\mathbf{S}^n_{++}$）[▶ 38:13](https://youtu.be/1menqhfNzzo?t=2293)

【口頭】這件事一百多年前就知道了（「1905 年，那時『凸』這個詞才出現 10–15 年」），而 $\det$ 是有 $n!$ 項的瘋狂多項式。

【課堂討論】[▶ 38:43](https://youtu.be/1menqhfNzzo?t=2323) 老師問：實際上怎麼算 $\log\det$？學生：寫出行列式？老師：那有 $n!$ 項。學生：**算特徵值**再取 log 加總。老師：可以；不用特徵值的精確方法是 **Cholesky 分解** $X=LL^T$，然後 $\log\det X=2\sum_i\log L_{ii}$，是 $O(n^3)$，「$n^3$ 比 $n!$ 好多了」。

**證明**（課本 §3.1.5）[▶ 40:50](https://youtu.be/1menqhfNzzo?t=2450)：任取 $X\in\mathbf{S}^n_{++}$、對稱（不一定正定）的方向 $V$，看 $g(t)=\log\det(X+tV)$。

$$
\begin{aligned}
g(t)&=\log\det\left(X^{1/2}\left(I+tX^{-1/2}VX^{-1/2}\right)X^{1/2}\right)\\
&=\log\det X+\log\det\left(I+tX^{-1/2}VX^{-1/2}\right)\\
&=\log\det X+\sum_{i=1}^n\log(1+t\lambda_i)
\end{aligned}
$$

$\lambda_i$ 是 $X^{-1/2}VX^{-1/2}$ 的特徵值（對稱但不一定正）。每個 $\log(1+t\lambda_i)$ 對 $t$ 是凹的（不論 $\lambda_i$ 正負：二階導數 $-\lambda_i^2/(1+t\lambda_i)^2\le0$），凹函數的和是凹的，所以 $g$ 凹，於是 $\log\det$ 凹。

【口頭】[▶ 40:17](https://youtu.be/1menqhfNzzo?t=2417) 懂資訊理論的人可以這樣證：$\log\det$ 是高斯變數的熵，混合高斯配上某個著名的資訊不等式。「但那對一般人太怪了。」

> ⚠️ 逐字稿缺字 [▶ 41:52](https://youtu.be/1menqhfNzzo?t=2512)：字幕寫「log **debt** x」，應為 **log det**。

---

## 9. 延伸值延拓

[▶ 42:53](https://youtu.be/1menqhfNzzo?t=2573)

【口頭】用「街頭電腦科學」的方言說：呼叫 $f(x)$，$x$ 在定義域內就回傳一個數（例如 $-11$）；在定義域外，應該回傳 OOD（out of domain）、NA、NaN 之類，「再呼叫十次你評估這個函數的權限就被撤銷」。

**延伸值延拓**（extended-value extension）$\tilde f$：定義域外就令它為 $+\infty$。

$$\tilde f(x)=\begin{cases}f(x)&x\in\mathbf{dom}\,f\\+\infty&x\notin\mathbf{dom}\,f\end{cases}$$

凸性不等式對 $\tilde f$ 照樣成立（約定 $\infty$ 的算術），而且這是之後**表達約束**的一種方式。

> ⚠️ 逐字稿缺字 [▶ 44:56](https://youtu.be/1menqhfNzzo?t=2696)：字幕寫「IEEE **488**」，浮點數標準（有 $\pm\infty$）是 **IEEE 754**；488 是儀器匯流排標準。

【課本補充】§3.1.2：$\tilde f$ 是凸的 $\iff$ $f$ 凸（含定義域凸）。這讓「定義域凸」這個條件自動包含在不等式裡：若 $\mathbf{dom}\,f$ 不凸，就找得到 $\theta x+(1-\theta)y$ 在定義域外，左邊是 $\infty$、右邊有限，不等式不成立。

---

## 10. 一階條件：全域下界

[▶ 45:27](https://youtu.be/1menqhfNzzo?t=2727)

**記號** [▶ 45:58](https://youtu.be/1menqhfNzzo?t=2758)：梯度 $\nabla f(x)=\left(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n}\right)$。老師只用一種向量記號：括號加逗號 $(a,b,c)$ 就是**垂直堆疊**（行向量）。

【Q&A】學生問：梯度慣例是行向量（column vector）嗎？答：**對**。

【口頭】[▶ 46:28](https://youtu.be/1menqhfNzzo?t=2788) 有人在同一篇論文混用好幾種向量寫法，「他們就會被評判」。

**一階 Taylor 近似** [▶ 46:59](https://youtu.be/1menqhfNzzo?t=2819)：
$$\hat f(y)=f(x)+\nabla f(x)^T(y-x)$$
是 $y$ 的仿射函數，在 $y=x$ 時等於 $f(x)$；微積分說 $y$ 靠近 $x$ 時 $\hat f\approx f$，誤差是距離的**平方**等級。

**一階條件**（$f$ 可微、定義域開）：

$$f\text{ 凸}\iff f(y)\ge f(x)+\nabla f(x)^T(y-x)\quad\forall x,y\in\mathbf{dom}\,f$$

**一階 Taylor 近似是全域下界**（global underestimator）。

【口頭】[▶ 48:02](https://youtu.be/1menqhfNzzo?t=2882)（老師說這是**整門課的重點**）
- 1770 年的微積分就知道 Taylor 近似在附近很準——那是**局部**的陳述，「要多近？那要看……」，變得複雜又模糊。
- 這裡是**全域**的：永遠是下界。**從局部資訊得到全域不等式**。
- 梯度為零時，一般函數你只知道「往任何方向走一小步函數會上升」，但不知道某個你沒看過的地方有沒有更小的值；**凸函數不可能有**。
- [▶ 49:06](https://youtu.be/1menqhfNzzo?t=2946) 老師曾跟人說「這是最好的電路設計」，對方說「你怎麼可能知道？哪來的狂妄？」——「因為它就是真的。」歸根究柢就是這張圖。
- [▶ 50:38](https://youtu.be/1menqhfNzzo?t=3038) 第六週時你會解幾千個變數的問題然後說「最佳值 3.1」，意思是 $\mathbb{R}^{\text{幾千}}$ 裡**任何**可行的 $x$ 目標值都 $\ge3.1$——「想想那是多瘋狂的陳述」。

【課本補充】§3.1.3：一階條件的推論——若 $\nabla f(x)=0$，則 $f(y)\ge f(x)$ 對所有 $y$，即 $x$ 是**全域最小**。證明方向「凸 ⇒ 下界」（一維）：$f(x+t(y-x))\le(1-t)f(x)+tf(y)$，$0<t\le1$，移項除以 $t$：
$$f(y)\ge f(x)+\frac{f(x+t(y-x))-f(x)}{t}$$
令 $t\to0^+$，右邊趨於 $f(x)+f'(x)(y-x)$。多維情形對 $g(t)=f(x+t(y-x))$ 套用即可。

---

## 11. 二階條件與例子

[▶ 51:08](https://youtu.be/1menqhfNzzo?t=3068)

$f$ 二次可微，**Hessian** $\nabla^2f(x)_{ij}=\dfrac{\partial^2f}{\partial x_i\partial x_j}$ 是對稱矩陣。

$$f\text{ 凸}\iff\nabla^2f(x)\succeq0\quad\forall x\in\mathbf{dom}\,f$$

（定義域要是開集。）$n=1$ 時就是 $f''\ge0$。Hessian 是**曲率**的度量。例：熵 $-x\log x$ 微分兩次得 $-1/x\le0$，所以凹 [▶ 52:09](https://youtu.be/1menqhfNzzo?t=3129)。

【課本補充】若 $\nabla^2f(x)\succ0$ 對所有 $x$，則 $f$ **嚴格凸**；逆命題不成立（例：$f(x)=x^4$ 嚴格凸但 $f''(0)=0$）。

**例 1：二次函數** [▶ 53:10](https://youtu.be/1menqhfNzzo?t=3190)

$$f(x)=\tfrac12x^TPx+q^Tx+r,\qquad P\in\mathbf{S}^n$$
$$\nabla f(x)=Px+q,\qquad\nabla^2f(x)=P$$

$P$ 不對稱時可換成對稱部分 $(P+P^T)/2$，函數不變。**曲率是常數**；凸 $\iff P\succeq0$。

**例 2：最小平方目標** [▶ 54:11](https://youtu.be/1menqhfNzzo?t=3251)

$$f(x)=\|Ax-b\|_2^2,\qquad\nabla f(x)=2A^T(Ax-b),\qquad\nabla^2f(x)=2A^TA\succeq0$$

（梯度就是正規方程裡的東西。）任何 $A$ 都凸。

**例 3：二次除以線性** [▶ 54:43](https://youtu.be/1menqhfNzzo?t=3283)

$$f(x,y)=\frac{x^2}{y},\qquad y>0$$

老師說這是「**大多數人完全不知道的最簡單凸函數**」。固定 $y$ 對 $x$ 凸（$x^2$ 的正倍數），固定 $x$ 對 $y$ 凸（$1/y$ 的常數倍），但更強的是**聯合凸**（jointly convex）：

$$\nabla^2f(x,y)=\frac{2}{y^3}\begin{pmatrix}y\\-x\end{pmatrix}\begin{pmatrix}y\\-x\end{pmatrix}^T\succeq0$$

Hessian 是**秩 1** 的半正定矩陣：曲面上每一點都有一個方向是平的、一個方向在彎 [▶ 55:47](https://youtu.be/1menqhfNzzo?t=3347)。

> 以下**不是逐字稿內容**，是驗算：$f_{xx}=2/y$，$f_{xy}=-2x/y^2$，$f_{yy}=2x^2/y^3$；$\frac{2}{y^3}\begin{pmatrix}y^2&-xy\\-xy&x^2\end{pmatrix}$ 正好相符。

【Q&A】[▶ 56:17](https://youtu.be/1menqhfNzzo?t=3377) 學生問：聯合凸是否表示對各變數分別凸？答：**是**——固定一個變數就是限制在某條直線上。但**逆命題是錯的**，而且很重要。

【課堂討論】[▶ 56:48](https://youtu.be/1menqhfNzzo?t=3408) 老師要反例。學生說「鞍形」。老師：差不多，看你往哪個方向走。他的例子：
$$f(x,y)=xy=\begin{pmatrix}x\\y\end{pmatrix}^T\frac12\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}$$
固定 $y$：對 $x$ 線性（凸）；固定 $x$：對 $y$ 線性（凸）。但圖形是鞍形，不凸。

那個矩陣半正定嗎？學生說用特徵值，答「$-1$ 和 $1$」，有 $-1$ 就結束了。另一位學生提出性質：**半正定矩陣的每個元素絕對值不超過對應兩個對角元素的幾何平均**，$|X_{ij}|\le\sqrt{X_{ii}X_{jj}}$。這裡 $1\le\sqrt{0\cdot0}$ 不成立，所以不是半正定 [▶ 59:32](https://youtu.be/1menqhfNzzo?t=3572)。（中間後排學生說看不清楚黑板，老師重寫。）

> 學生答的 $\pm1$ 是 $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ 的特徵值；乘上 $\frac12$ 之後是 $\pm\frac12$。結論（有負特徵值，不半正定）不變。

**例 4：log-sum-exp** [▶ 1:00:03](https://youtu.be/1menqhfNzzo?t=3603)

$$f(x)=\log\sum_{k=1}^ne^{x_k}$$

每個領域都以為是自己發明的：機器學習叫 **softmax**；學生補充統計物理裡的 Boltzmann 函數（老師：「那很學究」）；電機的「**dB 合成公式**」[▶ 1:01:06](https://youtu.be/1menqhfNzzo?t=3666)：幾路功率分別是 $-11$ dBm、$+13$、$+14$，總功率是多少？懂這個方言的電機工程師會算。

【課堂討論】老師問有沒有人會講這個方言，有一位學生從小在家講。

**為什麼凸**：Hessian 是兩項：一個半正定的對角矩陣，**減去**一個秩 1 矩陣。「你希望是兩個半正定的和，但有負號」，還是半正定，要證明（老師沒做）。

【課本補充】§3.1.5 的證明。令 $z_k=e^{x_k}$，
$$\nabla^2f(x)=\frac{1}{\mathbf{1}^Tz}\mathbf{diag}(z)-\frac{1}{(\mathbf{1}^Tz)^2}zz^T$$
對任意 $v$：
$$v^T\nabla^2f(x)v=\frac{\left(\sum_kz_kv_k^2\right)\left(\sum_kz_k\right)-\left(\sum_kv_kz_k\right)^2}{\left(\sum_kz_k\right)^2}\ge0$$
因為由 Cauchy–Schwarz（向量 $a_k=v_k\sqrt{z_k}$、$b_k=\sqrt{z_k}$）：$\left(\sum_ka_kb_k\right)^2\le\left(\sum_ka_k^2\right)\left(\sum_kb_k^2\right)$。

**為什麼叫 softmax** [▶ 1:03:12](https://youtu.be/1menqhfNzzo?t=3792)：它是 $\max$ 的光滑近似。若某個 $x_k$ 比其他都大 3，取指數後它比其他大 $e^3$ 倍以上，總和主要來自它，取 log 回到原尺度就接近它。

【課本補充】精確的界：$\max_kx_k\le\log\sum_ke^{x_k}\le\max_kx_k+\log n$。

> 以下**不是逐字稿內容**，是依 dB 定義推論的：dB 合成公式是 $10\log_{10}\sum_i10^{P_i/10}$，就是換了底數和尺度的 log-sum-exp。
>
> ⚠️ 逐字稿缺字 [▶ 1:01:06](https://youtu.be/1menqhfNzzo?t=3666)：字幕寫「the **220** times log base 10」，應為「**10**（功率）或 20（振幅）times log base 10」。

**例 5：幾何平均** [▶ 1:03:43](https://youtu.be/1menqhfNzzo?t=3823)
$$f(x)=\left(\prod_{k=1}^nx_k\right)^{1/n},\quad x\succ0$$
是**凹**的（證法類似）。

---

## 12. 下水平集與上圖

[▶ 1:04:15](https://youtu.be/1menqhfNzzo?t=3855)

「凸」用在集合和函數上，兩者有連結。【口頭】有凹函數，但**沒有「凹集合」**這種東西，不要這樣說。

**下水平集**（sublevel set）[▶ 1:04:45](https://youtu.be/1menqhfNzzo?t=3885)：
$$C_\alpha=\{x\in\mathbf{dom}\,f\mid f(x)\le\alpha\}$$
$f$ 是最小化的目標時，$C_\alpha$ 是「表現在 $\alpha$ 或更好」的所有點。

- **凸函數的下水平集是凸的**。
- 【課本補充】逆命題不成立：例如 $-e^x$ 不凸（其實是凹），但每個下水平集都是區間（凸）。下水平集都凸的函數叫**擬凸**（quasiconvex，§3.4）。

**上圖**（epigraph）[▶ 1:05:45](https://youtu.be/1menqhfNzzo?t=3945)："epi" = 上面。$f$ 的**圖形**是 $\mathbb{R}^{n+1}$ 中的 $\{(x,f(x))\mid x\in\mathbf{dom}\,f\}$；上圖是圖形上方的所有點：
$$\mathbf{epi}\,f=\{(x,t)\in\mathbb{R}^{n+1}\mid x\in\mathbf{dom}\,f,\ f(x)\le t\}$$

$$f\text{ 凸}\iff\mathbf{epi}\,f\text{ 是凸集}$$

這才是函數凸性和集合凸性之間**真正的連結**。

**例：最大概似的下水平集** [▶ 1:06:46](https://youtu.be/1menqhfNzzo?t=4006)

【口頭】用最小化負對數概似（negative log likelihood）擬合統計模型，$x$ 是參數。負對數概似的下水平集（= 對數概似的上水平集）是「概似超過某值」的參數集合，有很漂亮的統計解釋：靠近最大概似點時，很難有人說你的模型不一樣。

【課堂討論】[▶ 1:08:49](https://youtu.be/1menqhfNzzo?t=4129) 老師問：從最大概似點稍微退一點，上水平集長什麼樣？學生：**信賴區間**。老師：對，但在多維是什麼**形狀**？——**橢球**，曲率由 **Fisher 資訊矩陣**給出。老師隨即道歉「太怪了」。

---

## 13. Jensen 不等式

[▶ 1:09:19](https://youtu.be/1menqhfNzzo?t=4159)

【口頭】Jensen 約 120 年前推廣了凸性的概念。大家早就用這類不等式證明各種東西，他只是整理起來：「我發現這 14 個人用的是同一個論證」。

- **基本形式**：就是凸函數的定義，$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)$。
- **期望值形式** [▶ 1:10:19](https://youtu.be/1menqhfNzzo?t=4219)：任何隨機變數 $z$，
$$f(\mathbf{E}\,z)\le\mathbf{E}\,f(z)$$
  基本形式是 $z$ 以機率 $\theta$、$1-\theta$ 取 $x$、$y$ 的特例。

**解釋：抖動有害、風險有害** [▶ 1:10:50](https://youtu.be/1menqhfNzzo?t=4250)

【口頭】$x$ 是標稱值加上零平均的擾動，經過凸函數 $f$。如果 $f$ 是仿射的，平均值剛好對應過去。但凸函數在任一點都在切線上方，所以**不論往上還是往下抖，都在切線（仿射估計）上方**，平均起來 $\mathbf{E}f(x)$ 一定 $\ge f(\mathbf{E}x)$。「也許沒講清楚，但這是我的詮釋。」

【課本補充】§3.1.8：寫成有限和就是 $f\left(\sum_i\theta_ix_i\right)\le\sum_i\theta_if(x_i)$（$\theta_i\ge0$、$\sum\theta_i=1$）。§3.1.9 用它導出很多不等式，例如算術–幾何平均不等式 $\sqrt{ab}\le(a+b)/2$（對凹函數 $\log$ 用 Jensen），本集沒講。

---

## 14. 怎麼證明函數是凸的：凸性的微積分

[▶ 1:12:56](https://youtu.be/1menqhfNzzo?t=4376)

【口頭】這是「往合理的東西前進的開始」。如果是數學課，可以整學期看各種有趣的凸集——「那其實不太好」。我們要像**微積分**一樣做；這不只是數學上正確的想法，還會讓一切**在程式碼裡 100% 可操作**。

| 方法 | 評價 |
|---|---|
| 用定義 | 極少數、被逼到沒辦法才用 |
| 算 Hessian | 也不要，除非超簡單。例：要證 $\log\det$ 凹，對矩陣求 Hessian 是**四個指標** $(i,j,k,l)$ 的張量 [▶ 1:14:29](https://youtu.be/1menqhfNzzo?t=4469)，「只有機械系（應力應變張量）和某些物理學家真的會處理」；100×100 矩陣有 5,000 個變數，要驗證 5,000×5,000 的半正定…… |
| **原子＋組合規則** | **正確的做法** |

**原子**：$\log$ 凹、$\exp$ 凸、log-sum-exp 凸、$\log\det$ 凹……大約 20、30、50 個 [▶ 1:15:31](https://youtu.be/1menqhfNzzo?t=4531)。

**規則**：有些簡單到令人麻木（兩個凸函數相加還是凸——「往上彎加往上彎還是往上彎」），有些不顯然。
- 【口頭】[▶ 1:16:33](https://youtu.be/1menqhfNzzo?t=4593) 課本當成四條分開教的規則，**其實是同一條**（之後講）。它也是**寫程式自動驗證凸性**的核心規則，約兩週後你就會用到。
- 這叫**構造式凸性分析**（constructive convexity analysis）：「證明凸性的過程中沒有梯度受到傷害。」

**規則 1：非負縮放** [▶ 1:17:34](https://youtu.be/1menqhfNzzo?t=4654)：$f$ 凸、$\alpha\ge0$ ⇒ $\alpha f$ 凸（3.7 倍的凸函數，曲率乘 3.7）。

**規則 2：和** [▶ 1:18:05](https://youtu.be/1menqhfNzzo?t=4685)：$f_1,f_2$ 凸 ⇒ $f_1+f_2$ 凸（也可推廣到無限和、積分）。

**規則 3：和仿射函數合成**：$f$ 凸 ⇒ $f(Ax+b)$ 凸。

【課本補充】規則 3 的一行證明：令 $g(x)=f(Ax+b)$，
$$g(\theta x+(1-\theta)y)=f\left(\theta(Ax+b)+(1-\theta)(Ay+b)\right)\le\theta g(x)+(1-\theta)g(y).$$

**例：對數障礙函數**（log barrier）[▶ 1:18:35](https://youtu.be/1menqhfNzzo?t=4715)

$$f(x)=-\sum_{i=1}^m\log\left(b_i-a_i^Tx\right),\qquad\mathbf{dom}\,f=\{x\mid a_i^Tx<b_i,\ i=1,\dots,m\}$$

- 之後的課會用到。不等式必須**嚴格**，不然 log 沒意義。本課 $\log$ 的定義域是 $\mathbb{R}_{++}$（複變課不是，「看社交脈絡」）。
- **為什麼凸**——老師說「你到第三週就會這樣想」：
  1. $b_i-a_i^Tx$ 是仿射；**凹函數合成仿射是凹的** → $\log(b_i-a_i^Tx)$ 凹。
  2. **凹函數的和是凹的**。
  3. **負號把凹變成凸**。

【口頭】[▶ 1:19:36](https://youtu.be/1menqhfNzzo?t=4776)「你會不假思索地這樣做，就像剖析英文句法。」

**範數合成仿射**：$\|Ax+b\|$ 是凸的（範數是凸的，合成仿射）。

---

## 15. 一頁速查表

### 分離、支撐、對偶錐

| 概念 | 內容 | 關鍵一步 |
|---|---|---|
| 分離超平面 | $C\cap D=\varnothing$ 凸 ⇒ $\exists a\ne0,b$：$a^Tx\le b$ on $C$，$\ge b$ on $D$ | 取最近點 $c,d$，$a=d-c$，垂直平分面 |
| 支撐超平面 | 凸集邊界每點都有 $a\ne0$：$a^Tx\le a^Tx_0\ \forall x\in C$ | 由分離定理（$\{x_0\}$ vs $\mathbf{int}\,C$） |
| 對偶錐 | $K^*=\{y\mid x^Ty\ge0\ \forall x\in K\}$ | 小錐 ↔ 大對偶；$K^{**}=K$（閉凸） |
| 自對偶 | $\mathbb{R}^n_+$、$\mathbf{S}^n_+$ | $\mathrm{tr}(qq^TY)=q^TYq$ |
| 最小元素 | $\iff\forall\lambda\succ_{K^*}0$，$x$ 是 $\lambda^Tz$ 的唯一最小化者 | |
| 極小元素 | $\lambda\succ_{K^*}0$ 的最小化者必是極小（Pareto） | $x-z\in K\setminus\{0\}\Rightarrow\lambda^T(x-z)>0$ |

### 凸函數

| 判準 | 式子 |
|---|---|
| 定義 | $\mathbf{dom}\,f$ 凸，$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)$ |
| 直線限制 | $f$ 凸 $\iff$ $t\mapsto f(x+tv)$ 凸 |
| 一階 | $f(y)\ge f(x)+\nabla f(x)^T(y-x)$：**局部資訊 → 全域下界**；$\nabla f(x)=0\Rightarrow$ 全域最小 |
| 二階 | $\nabla^2f(x)\succeq0$ |
| 上圖 | $f$ 凸 $\iff\mathbf{epi}\,f$ 凸 |
| 下水平集 | $f$ 凸 ⇒ $\{x\mid f(x)\le\alpha\}$ 凸（逆不成立） |
| Jensen | $f(\mathbf{E}z)\le\mathbf{E}f(z)$ |

### 常見原子

| 函數 | 凸／凹 | 關鍵一步 |
|---|---|---|
| $e^{ax}$、$x^\alpha$（$\alpha\ge1$ 或 $\le0$）、$\lvert x\rvert^p$（$p\ge1$）、$x\log x$ | 凸 | 二階導數 $\ge0$ |
| $x^\alpha$（$0\le\alpha\le1$）、$\log x$、$-x\log x$ | 凹 | 二階導數 $\le0$ |
| 任何範數、$\sigma_{\max}(X)$ | 凸 | 三角不等式＋齊次 |
| $\tfrac12x^TPx+q^Tx+r$ | 凸 $\iff P\succeq0$ | $\nabla^2=P$ |
| $\|Ax-b\|_2^2$ | 凸 | $\nabla^2=2A^TA$ |
| $x^2/y$（$y>0$） | 凸 | $\nabla^2=\frac{2}{y^3}(y,-x)(y,-x)^T$ |
| $\log\sum e^{x_k}$ | 凸 | Cauchy–Schwarz |
| $(\prod x_k)^{1/n}$ | 凹 | |
| $\log\det X$ | 凹 | 限制在直線：$\log\det X+\sum\log(1+t\lambda_i)$ |

### 組合規則（本集）

- $\alpha f$（$\alpha\ge0$）、$f_1+f_2$、$f(Ax+b)$ 保凸。
- 讀法例：$-\sum\log(b_i-a_i^Tx)$ = 「凹∘仿射 = 凹 → 和 = 凹 → 負號 = 凸」。
- 分別凸 $\not\Rightarrow$ 聯合凸（反例 $xy$）；半正定 ⇒ $|X_{ij}|\le\sqrt{X_{ii}X_{jj}}$。

---

## 16. 與後續集數的連結

> 以下**不是逐字稿內容**：依課本章節與老師預告推估，做到時再更新。

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 更多組合規則（逐點 max、合成、最小化、透視）、「四條規則其實是同一條」 | 第 4 集（課本 §3.2） |
| 共軛函數、擬凸、對數凹 | 第 4 集（課本 §3.3–3.5） |
| 一階條件 → 最佳性條件 | 課本 §4.2.3 |
| 分離超平面 → 對偶、強對偶、擇一定理、無套利 | 課本第 5 章 |
| 極小元素 = 加權和最小化 → 純量化、Pareto | 課本 §4.7 |
| 對數障礙函數 | 內點法（課本第 11 章） |
| log-sum-exp | 幾何規劃（課本 §4.5）、邏輯回歸 |
| 用程式自動驗證凸性 | 約兩週後（DCP、CVXPY） |
| Fisher 資訊、信賴橢球 | 統計估計（課本第 7 章） |

---

## 附：本集一句話總結

> **凸集可以用超平面分開、在邊界有支撐超平面；把正交補的等式換成不等式就是對偶錐，用它可以把「找 Pareto 點」變成「最小化正權重的加權和」。凸函數 = 弦在圖形上方 = 上圖是凸集 = 一階 Taylor 近似是全域下界——最後這條讓我們從局部資訊得到全域結論，是整門課的核心。證明凸性要用「原子＋規則」，不要算 Hessian。**

---

*筆記依據 Stephen Boyd「Stanford EE364A Convex Optimization I（2023）」Lecture 3 錄影逐字稿（人工字幕，1:20:28）與 Boyd & Vandenberghe《Convex Optimization》§2.4–2.6、§3.1–3.2 整理。*
