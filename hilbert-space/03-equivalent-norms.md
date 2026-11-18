---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 3
lecture: Lecture 3
date: 2023-01-20
video: https://youtu.be/g3jpEdzJSCM
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3，Definition 1.3.9–1.3.15（書頁 11–14，PDF 頁 30–33）
---

# 第 3 集 · 範數等價（Equivalent Norms） [▶ 影片](https://youtu.be/g3jpEdzJSCM)

← 上一集：[02-normed-spaces](02-normed-spaces.md) ｜ [總目錄](README.md) ｜ 下一集：[04-closed-and-compact](04-closed-and-compact.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 3 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（57:16，自動字幕）＋ Debnath & Mikusiński §1.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 收斂數列有界](#1-收斂數列有界)
- [2. 範數等價的定義](#2-範數等價的定義)
- [3. 等價的判準：夾在兩個常數之間](#3-等價的判準夾在兩個常數之間)
- [4. 引理：線性獨立向量的下界](#4-引理線性獨立向量的下界)
- [5. 定理：有限維空間的所有範數都等價](#5-定理有限維空間的所有範數都等價)
- [6. 範數誘導的度量](#6-範數誘導的度量)
- [7. 開球、閉球、球面，以及不同範數的單位圓](#7-開球閉球球面以及不同範數的單位圓)
- [8. 開集、閉集預告](#8-開集閉集預告)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 收斂數列有界（補上次的缺口） | 課本無專門編號 |
| 範數等價的定義 | Definition 1.3.9，p. 11 |
| 等價 ⟺ $\alpha\|x\|_1\le\|x\|_2\le\beta\|x\|_1$ | Theorem 1.3.11，p. 12 |
| 線性獨立向量的下界引理 | Lemma 1.3.12，pp. 12–13 |
| 有限維空間所有範數等價 | Theorem 1.3.13，p. 13 |
| 度量、開球、閉球、球面、單位圓 | p. 13、Definition 1.3.14、Example 1.3.15，p. 14 |

---

## 1. 收斂數列有界

[▶ 00:06](https://youtu.be/g3jpEdzJSCM?t=6)

上一集證 $\lambda_nx_n\to\lambda x$ 時卡在這裡（見[第 2 集 §5](02-normed-spaces.md#5-賦範空間中的收斂)）。

**定理**：若 $x_n\to x$，則存在 $M>0$ 使得 $\|x_n\|\le M$ 對所有 $n$。也就是：**收斂數列有界**。

**證明**（講者說跟實分析裡的證明一樣）：

1. 取 $\varepsilon=1$。因為收斂，有 $N$ 使 $n\ge N$ 時 $\|x_n-x\|<1$。
2. $n\ge N$ 時：
   $$\|x_n\|=\|(x_n-x)+x\|\le\|x_n-x\|+\|x\|<1+\|x\|.$$
3. 前面只有有限多項 $x_1,\dots,x_{N-1}$，取
   $$M=\max\{\|x_1\|,\dots,\|x_{N-1}\|,\ 1+\|x\|\}.$$
   （第 3 步講者沒寫出來，是補的。）∎

純量數列也一樣有界。

**怎麼用來完成上次的證明**【口頭】[▶ 03:48](https://youtu.be/g3jpEdzJSCM?t=228)：要三個 $M$——一個讓 $x_n$ 那項變小，一個讓 $\lambda_n$ 那項變小，一個讓數列有界——取三者最大值。講者說他微積分 I 筆記的附錄有乘積極限律的論證可以參考。（完整寫法見[第 2 集 §5](02-normed-spaces.md#5-賦範空間中的收斂)。）

---

## 2. 範數等價的定義

[▶ 06:01](https://youtu.be/g3jpEdzJSCM?t=361) 課本 Definition 1.3.9。

同一個向量空間 $E$ 上的兩個範數 $\|\cdot\|_1$、$\|\cdot\|_2$ 叫**等價（equivalent）**，如果它們定義**同樣的收斂**：對 $E$ 中任何數列 $(x_n)$ 和任何 $x\in E$，

$$\|x_n-x\|_1\to0\iff\|x_n-x\|_2\to0.$$

課本 Example 1.3.10：$\mathbb{R}^2$ 上 $\sqrt{x^2+y^2}$、$|x|+|y|$、$\max\{|x|,|y|\}$ 三個範數等價。課本把它們編號成 1、2、3，跟講者上次的下標 $2,1,\infty$ 不一樣。[▶ 07:08](https://youtu.be/g3jpEdzJSCM?t=428)

講者強調：「定義同樣的收斂」才是概念上要記的；下面的不等式只是好用的判準。[▶ 20:32](https://youtu.be/g3jpEdzJSCM?t=1232)

---

## 3. 等價的判準：夾在兩個常數之間

[▶ 07:39](https://youtu.be/g3jpEdzJSCM?t=459) 課本 Theorem 1.3.11。

**定理**：$\|\cdot\|_1$ 與 $\|\cdot\|_2$ 等價 ⟺ 存在正數 $\alpha,\beta$ 使得

$$\alpha\|x\|_1\le\|x\|_2\le\beta\|x\|_1\quad\text{對所有 } x\in E. \tag{★}$$

課本說這個條件常常被直接拿來當等價的定義。

### (⟸) 用夾擠定理

[▶ 09:02](https://youtu.be/g3jpEdzJSCM?t=542) 課本只說「clearly」，講者用夾擠定理（squeeze theorem）證。

- 設 $\|x_n-x\|_1\to0$。由 (★) 右半，
  $$0\le\|x_n-x\|_2\le\beta\|x_n-x\|_1\to0,$$
  夾擠得 $\|x_n-x\|_2\to0$。
- 反方向：設 $\|x_n-x\|_2\to0$。由 (★) 左半，
  $$0\le\|x_n-x\|_1\le\frac1\alpha\|x_n-x\|_2\to0.$$

講者說：這個雙邊不等式讓你**兩個方向都能夾**。（課堂上有學生提議用 $\varepsilon$ 直接證，講者選擇夾擠，避開細節。）[▶ 10:30](https://youtu.be/g3jpEdzJSCM?t=630)

### (⟹) 反證法

[▶ 13:21](https://youtu.be/g3jpEdzJSCM?t=801)

設兩個範數等價。只證 $\alpha$ 存在（$\beta$ 同理）。

1. **假設沒有這樣的 $\alpha$**：也就是對每個 $\alpha>0$，都有 $x$ 使 $\alpha\|x\|_1>\|x\|_2$。取 $\alpha=\frac1n$，對每個 $n\in\mathbb{N}$ 得到 $x_n$ 使
   $$\frac1n\|x_n\|_1>\|x_n\|_2.$$
   （這說明 $\|x_n\|_1>0$，所以 $x_n\ne0$，於是 $\|x_n\|_2>0$。）
2. **正規化再縮小**：令
   $$y_n=\frac{1}{\sqrt n}\cdot\frac{x_n}{\|x_n\|_2}.$$
3. **在 2-範數下 $y_n\to0$**：$\|y_n\|_2=\frac{1}{\sqrt n}\to0$。
4. **在 1-範數下 $y_n$ 不收斂到 0**：
   $$\|y_n\|_1=\frac{\|x_n\|_1}{\sqrt n\,\|x_n\|_2}>\frac{n\|x_n\|_2}{\sqrt n\,\|x_n\|_2}=\sqrt n.$$
   第一步用了第 1 步的不等式 $\|x_n\|_1>n\|x_n\|_2$。
5. $\|y_n\|_1>\sqrt n\to\infty$，所以 $\|y_n-0\|_1\not\to0$；但 $\|y_n-0\|_2\to0$。這跟「等價」矛盾。∎

講者說他前一天讀時完全懂，上黑板才又卡了一下。[▶ 18:18](https://youtu.be/g3jpEdzJSCM?t=1098)

**關鍵一步**：用 $\frac1{\sqrt n}$ 調配——乘 $\frac{1}{\sqrt n}$ 讓 2-範數趨近 0，而原本的 $n$ 倍差距只被吃掉一半，1-範數仍然 $>\sqrt n$ 爆掉。

---

## 4. 引理：線性獨立向量的下界

[▶ 22:25](https://youtu.be/g3jpEdzJSCM?t=1345) 課本 Lemma 1.3.12。

講者說他以前常說「有限維所有範數等價」，但從沒在課堂證過，所以今天特別有意思。

**引理**：若 $x_1,\dots,x_n$ 是賦範空間 $E$ 中線性獨立的元素，則存在常數 $c>0$ 使得

$$\|\alpha_1x_1+\cdots+\alpha_nx_n\|\ge c\left(|\alpha_1|+\cdots+|\alpha_n|\right)\quad\text{對所有 }\alpha_1,\dots,\alpha_n\in\mathbb{R}. \tag{1.8}$$

（課本與講者都寫實數係數。）

**證明**：

**Step 1：化成單位「菱形」上的問題。**[▶ 24:19](https://youtu.be/g3jpEdzJSCM?t=1459)

- 若 $|\alpha_1|+\cdots+|\alpha_n|=0$，所有 $\alpha_i=0$，兩邊都是 $0$，任何 $c$ 都成立。
- 若 $s=|\alpha_1|+\cdots+|\alpha_n|>0$，(1.8) 兩邊除以 $s$，令 $\beta_i=\alpha_i/s$。則
  $$|\beta_1|+\cdots+|\beta_n|=\frac{|\alpha_1|+\cdots+|\alpha_n|}{s}=1.$$
  所以 (1.8) 等價於
  $$\|\beta_1x_1+\cdots+\beta_nx_n\|\ge c\quad\text{只要 }|\beta_1|+\cdots+|\beta_n|=1. \tag{1.9}$$

講者提醒：$\beta_i$ 不是任意的數，它們是除出來的，所以絕對值加起來剛好是 1——這就是為什麼要先排除和為 0 的情況。[▶ 27:14](https://youtu.be/g3jpEdzJSCM?t=1634)

**Step 2：一個連續函數。**[▶ 28:23](https://youtu.be/g3jpEdzJSCM?t=1703)

$$f:\mathbb{R}^n\to\mathbb{R},\qquad f(\beta_1,\dots,\beta_n)=\|\beta_1x_1+\cdots+\beta_nx_n\|.$$

講者說 $f$ 連續，因為它是連續運算的合成：$\mathbb{R}^n$ 上的加法、純量乘法連續，取範數也連續。直接用 $\varepsilon$ 證連續可以當作業。

以下**不是逐字稿內容**，是直接證法：由反向三角不等式和三角不等式，
$$|f(\beta)-f(\beta')|\le\left\|\sum_i(\beta_i-\beta_i')x_i\right\|\le\max_i\|x_i\|\cdot\sum_i|\beta_i-\beta_i'|,$$
右邊 $\to0$（當 $\beta'\to\beta$），所以 $f$ 連續。

**Step 3：定義域 $B$ 是閉且有界的。**[▶ 30:43](https://youtu.be/g3jpEdzJSCM?t=1843)

$$B=\{(\beta_1,\dots,\beta_n)\in\mathbb{R}^n:|\beta_1|+\cdots+|\beta_n|=1\}.$$

講者說這不一定「顯然」，畫 $n=2$ 的圖：第一象限 $\beta_1+\beta_2=1$，第二象限 $-\beta_1+\beta_2=1$，……四段合起來是一個**菱形**。曲線在 $\mathbb{R}^2$ 中是閉的；一般來說用**等式**定義的集合通常是閉的（他說這句話斷章取義可能是錯的）。菱形可以放進夠大的球，所以有界。

以下**不是逐字稿內容**，是一般 $n$ 的理由：$B$ 是連續函數 $\beta\mapsto\sum|\beta_i|$ 在閉集 $\{1\}$ 的原像，所以是閉集；每個 $|\beta_i|\le1$，所以有界。

**Step 4：最小值大於 0。**[▶ 33:34](https://youtu.be/g3jpEdzJSCM?t=2014)

$B$ 閉且有界（緊緻），$f$ 連續 ⟹ $f$ 在 $B$ 上取到最小值。這個最小值**不能是 0**：

- 若某個 $\beta\in B$ 使 $f(\beta)=0$，即 $\|\beta_1x_1+\cdots+\beta_nx_n\|=0$；
- 只有零向量範數為 0，所以 $\beta_1x_1+\cdots+\beta_nx_n=0$；
- 由**線性獨立**，$\beta_1=\cdots=\beta_n=0$；
- 但 $\beta\in B$ 要求 $\sum|\beta_i|=1$，矛盾。

【課堂討論】[▶ 34:18](https://youtu.be/g3jpEdzJSCM?t=2058) 學生一開始說「這跟 $\ge c$ 矛盾」，講者指出那正是要證的，不能用。講者再釐清：線性獨立是推理的**中間一步**（從「組合為 0」推到「係數全 0」）；真正的**矛盾**是係數絕對值和應該是 1。

**Step 5**：令 $c=\min_{\beta\in B}f(\beta)>0$，(1.9) 成立。∎

---

## 5. 定理：有限維空間的所有範數都等價

[▶ 37:28](https://youtu.be/g3jpEdzJSCM?t=2248) 課本 Theorem 1.3.13。

**定理**：若 $E$ 有限維，則 $E$ 上任兩個範數都等價。

**證明的策略**：等價是一種「傳遞」的關係，所以只要證**每個範數都跟某一個固定的範數等價**。

**Step 1：用基底造一個範數。**[▶ 38:40](https://youtu.be/g3jpEdzJSCM?t=2320) 取基底 $\{e_1,\dots,e_n\}$（講者強調這是抽象基底，不是行向量），定義

$$\|\alpha_1e_1+\cdots+\alpha_ne_n\|_0=|\alpha_1|+\cdots+|\alpha_n|.$$

講者說：有基底就能造一個讓基底長度都是 1 的範數，方法「很蠢」，就是係數絕對值加起來。在 $\mathbb{R}^n$ 也能這樣做，但距離跟歐氏距離對不上。驗證它是範數留給大家。【口頭】

**Step 2：上界（三角不等式）。**[▶ 40:56](https://youtu.be/g3jpEdzJSCM?t=2456) $\|\cdot\|$ 是任意範數，$x=\alpha_1e_1+\cdots+\alpha_ne_n$：

$$\|x\|\le|\alpha_1|\|e_1\|+\cdots+|\alpha_n|\|e_n\|\le\max\{\|e_1\|,\dots,\|e_n\|\}\left(|\alpha_1|+\cdots+|\alpha_n|\right)=\beta\|x\|_0,$$

其中 $\beta=\max\{\|e_1\|,\dots,\|e_n\|\}$。第一步用三角不等式和 (b)。

**Step 3：下界（引理）。**[▶ 44:38](https://youtu.be/g3jpEdzJSCM?t=2678) 基底線性獨立，套 Lemma 1.3.12：存在 $\alpha>0$ 使

$$\|x\|=\|\alpha_1e_1+\cdots+\alpha_ne_n\|\ge\alpha\left(|\alpha_1|+\cdots+|\alpha_n|\right)=\alpha\|x\|_0.$$

講者說：引理用現在的記號寫，**就是** $\|x\|\ge c\|x\|_0$。

**Step 4**：$\alpha\|x\|_0\le\|x\|\le\beta\|x\|_0$，由 Theorem 1.3.11，$\|\cdot\|$ 與 $\|\cdot\|_0$ 等價。任意兩個範數都跟 $\|\cdot\|_0$ 等價，所以彼此等價。∎

講者：「其實沒那麼難，真的很酷。為什麼我以前不教這個證明？……這是我新的最愛證明之一。」【口頭】[▶ 46:01](https://youtu.be/g3jpEdzJSCM?t=2761)

> 以下**不是逐字稿內容**，是依證明推論的提醒：證明的關鍵是 Step 4 用到的「閉且有界 ⟹ 連續函數取到最小值」，這只在**有限維**（$\mathbb{R}^n$）成立。下一集會看到：無限維空間裡單位球不是緊緻的，定理也就不成立。

---

## 6. 範數誘導的度量

[▶ 46:34](https://youtu.be/g3jpEdzJSCM?t=2794) 課本 p. 13。

**定義**：$d:E\times E\to\mathbb{R}$，$d(x,y)=\|x-y\|$。

性質：

1. **對稱**：$d(x,y)=\|x-y\|=\|-(y-x)\|=\|y-x\|=d(y,x)$。
2. **$d(x,y)=0\iff x=y$**：$d(x,x)=\|0\|=0$；反過來 $\|x-y\|=0$ ⟹ $x-y=0$ ⟹ $x=y$。講者強調「不只是 $d(x,x)=0$，還要相異點距離不為 0」。[▶ 48:25](https://youtu.be/g3jpEdzJSCM?t=2905)
3. **三角不等式**：
   $$d(x,y)+d(y,z)=\|x-y\|+\|y-z\|\ge\|(x-y)+(y-z)\|=\|x-z\|=d(x,z).$$
   範數的三角不等式直接給出距離的三角不等式。

**度量空間（metric space）**：集合 $S$ 配上一個距離函數，滿足上面三條。

【課本補充】範數定義的收斂和這個度量定義的收斂一樣。度量決定一個拓樸，所以所有「用開集定義的概念」（拓樸概念）都有了；課本選擇直接用範數定義這些概念，不先繞道度量。

---

## 7. 開球、閉球、球面，以及不同範數的單位圓

[▶ 50:13](https://youtu.be/g3jpEdzJSCM?t=3013) 課本 Definition 1.3.14，p. 14。

$x\in E$，$r>0$：

$$B(x,r)=\{y\in E:\|y-x\|<r\}\ (\text{開球}),\quad \overline{B}(x,r)=\{y\in E:\|y-x\|\le r\}\ (\text{閉球}),\quad S(x,r)=\{y\in E:\|y-x\|=r\}\ (\text{球面}).$$

$x$ 是中心，$r$ 是半徑。講者說球面是邊界，「邊界」之後在拓樸裡會正式學。

**不同範數的單位圓**【口頭】[▶ 52:38](https://youtu.be/g3jpEdzJSCM?t=3158)（課本 Example 1.3.15、Figure 1.2 有圖）

在 $\mathbb{R}^2$ 畫 $S(0,1)$：

| 範數 | $\{(x,y):\|(x,y)\|=1\}$ |
|---|---|
| $\|\cdot\|_2$ | 真正的圓 $x^2+y^2=1$ |
| $\|\cdot\|_1$ | 菱形 $|x|+|y|=1$ |
| $\|\cdot\|_p$，$p=3,4,\dots$ | 介於圓和正方形之間，$p$ 越大越方 |
| $\|\cdot\|_\infty$ | 正方形 $\max\{|x|,|y|\}=1$ |

講者開玩笑：哲學家說「不能化圓為方」，在 sup 範數下圓**就是**方的。[▶ 54:19](https://youtu.be/g3jpEdzJSCM?t=3259)

---

## 8. 開集、閉集預告

[▶ 54:53](https://youtu.be/g3jpEdzJSCM?t=3293)

- 有了範數 → 有度量 → 有開球。
- **開集**：集合裡每一點都能找到一個以它為中心、整個包含在集合裡的開球。
- 這樣的點叫**內點**，所有內點構成集合的**內部（interior）**。集合等於自己的內部 ⟺ 開集。
- **閉集**：補集是開集。
- 這是拓樸式的定義；另外還有用數列定義的「序列閉」，下一堂講。

**一個更難的問題**【口頭】[▶ 55:26](https://youtu.be/g3jpEdzJSCM?t=3326)：給一個度量空間，什麼時候這個度量是由某個範數誘導的？如果根本不是向量空間，當然不行。就算是向量空間，也有度量不能寫成範數的例子。講者說他講到這裡有點混淆（想到內積和範數的關係），要趕去開會，就在這裡停下。

> 以下**不是逐字稿內容**，是依範數公理推論的一個判準：範數誘導的度量一定滿足 $d(x+z,y+z)=d(x,y)$（平移不變）和 $d(\lambda x,\lambda y)=|\lambda|d(x,y)$（齊次）。例如離散度量（$x\ne y$ 時 $d=1$）不齊次，所以不來自任何範數。

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 收斂有界 | $x_n\to x$ ⟹ $\sup\|x_n\|<\infty$ | $\varepsilon=1$；$\|x_n\|<1+\|x\|$；前面有限項取 max |
| 範數等價 | 定義同樣的收斂 | |
| 判準（Thm 1.3.11） | 等價 ⟺ $\alpha\|x\|_1\le\|x\|_2\le\beta\|x\|_1$ | ⟸ 夾擠；⟹ 反證，$y_n=\frac{x_n}{\sqrt n\|x_n\|_2}$ |
| 引理（Lem 1.3.12） | 線性獨立 ⟹ $\|\sum\alpha_ix_i\|\ge c\sum|\alpha_i|$ | 正規化到菱形 $B$；$f$ 連續、$B$ 緊緻取最小值；最小值 $=0$ 違反線性獨立 |
| 定理（Thm 1.3.13） | 有限維所有範數等價 | 跟 $\|\sum\alpha_ie_i\|_0=\sum|\alpha_i|$ 比：上界用三角不等式，下界用引理 |
| 誘導度量 | $d(x,y)=\|x-y\|$ | 對稱、正定、三角不等式都從範數來 |
| 球 | $B(x,r)$、$\overline B(x,r)$、$S(x,r)$ | $\mathbb{R}^2$ 單位圓：$\|\cdot\|_1$ 菱形、$\|\cdot\|_2$ 圓、$\|\cdot\|_\infty$ 正方形 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 開集、閉集、序列閉 | 第 4 集 |
| 「閉且有界 ⟹ 緊緻」只在有限維成立 | 第 4–5 集：無限維單位球不緊緻 |
| 有限維子空間 | 第 5 集（Riesz 引理類論證）、第 6 集（有限維子空間是完備的） |
| 範數夾在常數之間 | 第 7–8 集：有界線性算子 $\|Tx\|\le K\|x\|$ |

---

## 附：本集一句話總結

> **兩個範數等價 ⟺ 能被兩個正常數互相夾住；在有限維空間，任何範數都能跟「係數絕對值和」互夾——上界靠三角不等式，下界靠「連續函數在緊緻的菱形上取到正的最小值」，而這一步正是無限維會失敗的地方。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-01-20 錄影逐字稿（YouTube 自動字幕，57:16）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3 整理。*
