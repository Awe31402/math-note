---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 6
lecture: Lecture 6
date: 2023-01-27
video: https://youtu.be/DRlR8CPAz1I （part 1）、https://youtu.be/61gx0FfCvhU （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.4，Example 1.4.6–完備化（書頁 20–25，PDF 頁 39–44）
---

# 第 6 集 · Banach 空間與完備化（Banach Spaces and Completions） [▶ 影片](https://youtu.be/DRlR8CPAz1I)

← 上一集：[05-riesz-lemma-unit-ball](05-riesz-lemma-unit-ball.md) ｜ [總目錄](README.md) ｜ 下一集：[07-linear-maps-continuity](07-linear-maps-continuity.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 6 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 20:07，自動字幕）＋ Debnath & Mikusiński §1.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 課前：有限維單位球緊緻的另一個嘗試](#1-課前有限維單位球緊緻的另一個嘗試)
- [2. ℓ² 是 Banach 空間](#2-ℓ²-是-banach-空間)
- [3. C([a,b]) 是 Banach 空間](#3-cab-是-banach-空間)
- [4. 級數與絕對收斂](#4-級數與絕對收斂)
- [5. 定理：完備 ⟺ 絕對收斂級數都收斂](#5-定理完備--絕對收斂級數都收斂)
- [6. 閉子空間](#6-閉子空間)
- [7. 完備化](#7-完備化)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| ℓ² 完備（課堂跳過） | Example 1.4.6，pp. 20–21 |
| $C([a,b])$ 完備 | Example 1.4.7，pp. 21–22 |
| 收斂級數、絕對收斂級數 | Definition 1.4.8，p. 22 |
| 完備 ⟺ 每個絕對收斂級數都收斂 | Theorem 1.4.9，pp. 22–23 |
| Banach 空間的閉子空間是 Banach 空間 | Theorem 1.4.10，p. 23 |
| 完備化 | pp. 23–25 |

---

## 1. 課前：有限維單位球緊緻的另一個嘗試

[▶ 00:03](https://youtu.be/DRlR8CPAz1I?t=3)

等另一位學生上線時，講者展示他對「有限維單位球緊緻」（上一集課本說是「簡單練習」）的新證法：

1. 單位球裡的數列 $x_j=\alpha_{1j}e_1+\cdots+\alpha_{nj}e_n$，範數用 $\|x\|_0=\sum|\alpha_i|$。
2. $B_j=\|x_j\|_0\le1$ 是有界實數列，用**一次** Bolzano–Weierstrass 取收斂子數列 $B_{j_p}$。
3. 講者主張：既然總和收斂，每個分量 $|\alpha_{k,j_p}|$ 也要收斂，「否則跟 $B_j$ 收斂矛盾」；令 $\beta_k$ 是分量的極限，$x=\beta_1e_1+\cdots+\beta_ne_n$，則 $\|x_{j_p}-x\|_0\to0$；而且 $\|x\|_0=\sum|\beta_k|=\lim B_{j_p}\le1$。

講者說他刻意避開「對每個分量各取子數列再串起來」，因為那讓他頭痛。

> 以下**不是逐字稿內容**，是依數學推論的：第 3 步不成立。總和收斂**不能**推出每個分量收斂，例如 $\mathbb{R}^2$ 中 $x_j$ 在 $e_1$、$e_2$ 之間交替，$B_j=1$ 一直收斂，但分量 $1,0,1,0,\dots$ 不收斂。所以還是要對每個分量各用一次 Bolzano–Weierstrass（共 $n$ 次，每次在上一次的子數列裡取）。完整證明見[第 5 集 §2.1](05-riesz-lemma-unit-ball.md#21-有限維--緊緻)。

講者也提到另一個思路：有限維空間的向量極限存在 ⟺ 每個分量的極限存在；如果先證了這個，這題很快。學生則提到用「連續映射下閉集的原像是閉的」。講者說這部分「看見森林比看見樹重要，少一些細節沒關係」。

---

## 2. ℓ² 是 Banach 空間

[▶ 14:12](https://youtu.be/DRlR8CPAz1I?t=852) 課本 Example 1.4.6。講者說「我略過細節」，所以下面是【課本補充】。

記號（上一集講過）：$\ell^2$ 中的數列是數列的數列，$a_n=(\alpha_{n,1},\alpha_{n,2},\dots)$。

**證明**：設 $(a_n)$ 是 $\ell^2$ 中的 Cauchy 數列。

**Step 1：每個座標是 Cauchy。** 給 $\varepsilon>0$，有 $n_0$ 使 $m,n\ge n_0$ 時

$$\sum_{k=1}^\infty|\alpha_{m,k}-\alpha_{n,k}|^2<\varepsilon^2. \tag{1.10}$$

固定 $k$，和裡面的一項不超過整個和，所以 $|\alpha_{m,k}-\alpha_{n,k}|<\varepsilon$。也就是第 $k$ 座標 $(\alpha_{n,k})_n$ 是 $\mathbb{C}$ 中的 Cauchy 數列。$\mathbb{C}$ 完備，令

$$\alpha_k=\lim_{n\to\infty}\alpha_{n,k},\qquad a=(\alpha_1,\alpha_2,\dots).$$

這是**候選極限**。還要證 (i) $a\in\ell^2$，(ii) $a_n\to a$。

**Step 2：讓 $m\to\infty$。** 由 (1.10)，對每個有限的 $K$，
$$\sum_{k=1}^K|\alpha_{m,k}-\alpha_{n,k}|^2<\varepsilon^2\quad(m,n\ge n_0).$$
有限和可以直接取極限 $m\to\infty$：$\sum_{k=1}^K|\alpha_k-\alpha_{n,k}|^2\le\varepsilon^2$。這對所有 $K$ 成立，再令 $K\to\infty$：

$$\sum_{k=1}^\infty|\alpha_k-\alpha_{n,k}|^2\le\varepsilon^2\quad(n\ge n_0). \tag{1.11}$$

（先截成有限和是補的；課本直接寫「讓 $m\to\infty$」。）

**Step 3：$a\in\ell^2$。** 由 (1.11)，$a-a_{n_0}\in\ell^2$；又 $a_{n_0}\in\ell^2$。由 Minkowski 不等式，
$$\|a\|_2\le\|a-a_{n_0}\|_2+\|a_{n_0}\|_2\le\varepsilon+\|a_{n_0}\|_2<\infty.$$

**Step 4：$a_n\to a$。** (1.11) 說 $n\ge n_0$ 時 $\|a-a_n\|_2\le\varepsilon$，$\varepsilon$ 任意，所以 $\|a-a_n\|_2\to0$。∎

**模板**：完備性證明幾乎都是這三步——(1) 用已知完備的空間（這裡是 $\mathbb{C}$）造出**候選極限**；(2) 證候選極限**在空間裡**；(3) 證**按範數收斂**到它。

---

## 3. C([a,b]) 是 Banach 空間

[▶ 15:22](https://youtu.be/DRlR8CPAz1I?t=922) 課本 Example 1.4.7。

$C([a,b])$：$[a,b]$ 上的連續實值函數（複值同理），範數 $\|f\|=\max_{[a,b]}|f(x)|$。講者說這個例子比 ℓ² 重要，因為它幫助理解一致收斂。

**證明**：

**Step 1：逐點 Cauchy，定義候選極限。**[▶ 16:29](https://youtu.be/DRlR8CPAz1I?t=989) 設 $(f_n)$ 是 Cauchy 數列。給 $\varepsilon>0$，有 $n_0$ 使 $m,n\ge n_0$ 時 $\|f_n-f_m\|<\varepsilon$。因為範數是最大值，

$$|f_n(x)-f_m(x)|<\varepsilon\quad\text{對所有 } m,n\ge n_0 \text{ 和所有 } x\in[a,b]. \tag{1.12}$$

講者解釋：最大值都 $<\varepsilon$，每一點的值當然也 $<\varepsilon$。所以對每個固定的 $x$，$(f_n(x))$ 是實數的 Cauchy 數列。$\mathbb{R}$ 完備，定義

$$f(x)=\lim_{n\to\infty}f_n(x).$$

這只定義了一個函數，**還不知道它連續**。[▶ 20:07](https://youtu.be/DRlR8CPAz1I?t=1207)

**Step 2：讓 $m\to\infty$。**[▶ 20:45](https://youtu.be/DRlR8CPAz1I?t=1245) 在 (1.12) 中令 $m\to\infty$：

$$|f_n(x)-f(x)|\le\varepsilon\quad\text{對所有 } n\ge n_0 \text{ 和所有 } x\in[a,b]. \tag{1.13}$$

**Step 3：$f$ 連續（$\varepsilon/3$ 論證）。**[▶ 22:10](https://youtu.be/DRlR8CPAz1I?t=1330) 固定 $x_0\in[a,b]$。$f_{n_0}$ 連續，所以有 $\delta>0$ 使 $|x_0-y|<\delta$ 時 $|f_{n_0}(x_0)-f_{n_0}(y)|<\varepsilon$。則

$$|f(x_0)-f(y)|\le|f(x_0)-f_{n_0}(x_0)|+|f_{n_0}(x_0)-f_{n_0}(y)|+|f_{n_0}(y)-f(y)|<\varepsilon+\varepsilon+\varepsilon=3\varepsilon.$$

第一、三項用 (1.13)，第二項用 $f_{n_0}$ 連續。講者說：一開始把每個 $\varepsilon$ 換成 $\varepsilon/3$ 重做，最後就得到 $<\varepsilon$。$x_0$ 任意，所以 $f$ 連續，$f\in C([a,b])$。

**Step 4：按範數收斂。** (1.13) 對所有 $x$ 成立，取最大值得 $\|f_n-f\|\le\varepsilon$（$n\ge n_0$）。所以 $f_n\to f$，也就是 $f_n$ **一致收斂**到 $f$。∎

講者的說明【口頭】：

- 很容易搞混哪個是 $n_0$、哪個是 $x_0$。整個證明的根基是：**範數直接給出函數值的 Cauchy 數列**。[▶ 26:10](https://youtu.be/DRlR8CPAz1I?t=1570)
- 這也重證了實分析的定理：**連續函數的一致極限是連續的**。一般實分析課講一致收斂，不會講這些「花俏配件」。[▶ 28:22](https://youtu.be/DRlR8CPAz1I?t=1702)
- **推廣**[▶ 26:44](https://youtu.be/DRlR8CPAz1I?t=1604)：函數值換成有限維向量空間，證明照樣成立。換成 Banach 空間值呢？證明用的是值域的完備性，但問題是 max 在 Banach 空間上有沒有意義——「這就是難處」。講者笑說這可以當考題。

> 以下**不是逐字稿內容**，是依證明推論的：在 Banach 空間 $V$ 中，$x\mapsto\|f(x)\|_V$ 是 $[a,b]$ 上的連續實函數（範數連續，見第 7 集），所以 max 一樣存在，證明照樣成立：$C([a,b];V)$ 也是 Banach 空間。

---

## 4. 級數與絕對收斂

[▶ 29:33](https://youtu.be/DRlR8CPAz1I?t=1773) 課本 Definition 1.4.8。

- 賦範空間 $E$ 中的級數 $\sum_{n=1}^\infty x_n$ **收斂**，如果部分和數列收斂：存在 $x\in E$ 使
  $$\|x_1+x_2+\cdots+x_n-x\|\to0.$$
  這時寫 $\sum_{n=1}^\infty x_n=x$。
- 如果 $\sum_{n=1}^\infty\|x_n\|<\infty$，叫**絕對收斂（absolutely convergent）**。

注意：$\sum\|x_n\|$ 是**實數級數**，$\sum x_n$ 是**向量空間裡的和**。[▶ 33:52](https://youtu.be/DRlR8CPAz1I?t=2032)

**絕對收斂不一定收斂**【課堂討論】[▶ 32:00](https://youtu.be/DRlR8CPAz1I?t=1920) 例子：上一集的 $P([0,1])$。令 $x_k=\frac{x^k}{k!}$（多項式），部分和就是 $P_n$。學生說明為什麼絕對收斂：

$$\sum_k\left\|\frac{x^k}{k!}\right\|=\sum_k\max_{[0,1]}\frac{x^k}{k!}=\sum_k\frac1{k!}=e<\infty.$$

但部分和不收斂到任何多項式（極限 $e^x$ 不在空間裡）。

---

## 5. 定理：完備 ⟺ 絕對收斂級數都收斂

[▶ 34:27](https://youtu.be/DRlR8CPAz1I?t=2067) 課本 Theorem 1.4.9。

**定理**：賦範空間 $E$ 是完備的 ⟺ $E$ 中每個絕對收斂級數都收斂。

### (⟹)

[▶ 36:24](https://youtu.be/DRlR8CPAz1I?t=2184)

設 $E$ 是 Banach 空間，$\sum\|x_n\|<\infty$。令 $s_n=x_1+\cdots+x_n$。在完備空間裡，只要證 $(s_n)$ 是 Cauchy 數列就夠了。

給 $\varepsilon>0$。$\sum\|x_n\|$ 收斂，所以它的**尾巴**能變小：取 $k$ 使 $\sum_{r=k+1}^\infty\|x_r\|<\varepsilon$。對 $m>n>k$：

$$\|s_m-s_n\|=\|x_{n+1}+\cdots+x_m\|\le\sum_{r=n+1}^m\|x_r\|\le\sum_{r=k+1}^\infty\|x_r\|<\varepsilon.$$

前 $n$ 項相消，再用三角不等式。所以 $(s_n)$ 是 Cauchy，收斂。∎

（講者把求和指標從 $n$ 換成 $r$，避免跟外面的 $n$ 撞名。）

### (⟸)

[▶ 41:38](https://youtu.be/DRlR8CPAz1I?t=2498)

設每個絕對收斂級數都收斂。取 Cauchy 數列 $(x_n)$，要證它收斂。

**Step 1：挑一個「跳得很快收斂」的子數列。** 對每個 $k$，Cauchy 給出 $p_k$ 使

$$\|x_m-x_n\|<2^{-k}\quad\text{對所有 } m,n\ge p_k.$$

可以假設 $p_1<p_2<\cdots$ 嚴格遞增（不然就把 $p_k$ 換成 $\max\{p_1,\dots,p_k\}+k$）。

**Step 2：差的級數絕對收斂。**[▶ 44:13](https://youtu.be/DRlR8CPAz1I?t=2653) 因為 $p_{k+1}>p_k$，兩個都 $\ge p_k$，所以 $\|x_{p_{k+1}}-x_{p_k}\|<2^{-k}$。

$$\sum_{k=1}^\infty\|x_{p_{k+1}}-x_{p_k}\|\le\sum_{k=1}^\infty2^{-k}=\frac{1/2}{1-1/2}=1<\infty.$$

講者說：用公比 $\frac12$ 的幾何級數是很典型的招數。【口頭】

**Step 3：子數列收斂。** 由假設，絕對收斂級數收斂。**伸縮和**（telescoping）：

$$x_{p_k}=x_{p_1}+(x_{p_2}-x_{p_1})+\cdots+(x_{p_k}-x_{p_{k-1}}),$$

右邊是 $x_{p_1}$ 加上一個收斂級數的部分和，所以 $x_{p_k}\to$ 某個 $x\in E$。講者說：就是在差的級數前面加上 $x_{p_1}$ 這一項。[▶ 46:45](https://youtu.be/DRlR8CPAz1I?t=2805)

**Step 4：整個數列收斂。**[▶ 48:02](https://youtu.be/DRlR8CPAz1I?t=2882)

$$\|x_n-x\|\le\|x_n-x_{p_n}\|+\|x_{p_n}-x\|\to0.$$

第一項：$p_n\ge n$，Cauchy 數列兩個指標都大時差很小；第二項：子數列收斂。∎

**關鍵一步**：Cauchy 數列只要**有一個收斂子數列**，整個數列就收斂。用 $2^{-k}$ 挑子數列，讓「差」的級數絕對收斂。

---

## 6. 閉子空間

[▶ 50:24](https://youtu.be/DRlR8CPAz1I?t=3024) 課本 Theorem 1.4.10。講者說證明很清楚，直接讀。

**定理**：Banach 空間的**閉**向量子空間本身是 Banach 空間。

**證明**：$F$ 是 Banach 空間 $E$ 的閉子空間，$(x_n)$ 是 $F$ 中的 Cauchy 數列。

1. 它也是 $E$ 中的 Cauchy 數列（同一個範數）。
2. $E$ 完備，所以 $x_n\to x\in E$。
3. $F$ 閉：$F$ 中數列的極限一定在 $F$ 裡（第 4 集：閉 ⟺ 序列閉）。所以 $x\in F$。∎

---

## 7. 完備化

[▶ 53:50](https://youtu.be/DRlR8CPAz1I?t=3230) 課本 pp. 23–25。

很多賦範空間不完備，但有一個一般的構造，把任何不完備的空間**形式上擴大**成完備的空間，叫**完備化（completion）**。

### 7.1 什麼叫一個完備化

[▶ 55:00](https://youtu.be/DRlR8CPAz1I?t=3300)

$(E,\|\cdot\|)$ 是賦範空間。賦範空間 $(\tilde E,\|\cdot\|_1)$ 叫 $E$ 的**一個**完備化（講者強調是「一個」，因為不唯一），如果：

- (a) 有一對一映射 $\Phi:E\to\tilde E$，而且線性：$\Phi(\alpha x+\beta y)=\alpha\Phi(x)+\beta\Phi(y)$；
- (b) 保持範數：$\|x\|=\|\Phi(x)\|_1$；
- (c) $\Phi(E)$ 在 $\tilde E$ 中稠密；
- (d) $\tilde E$ 完備。

**例子**【口頭】[▶ 57:59](https://youtu.be/DRlR8CPAz1I?t=3479)：把 $\mathbb{Q}$ 看成 $\mathbb{Q}$ 上的向量空間，範數是絕對值，它是賦範空間。它不完備：$1,\ 1.4,\ 1.41,\ 1.414,\dots$ 收斂到 $\sqrt2\notin\mathbb{Q}$。$\mathbb{Q}$ 對絕對值的完備化就是 $\mathbb{R}$。

### 7.2 構造：Cauchy 數列的等價類

[▶ part 2 00:02](https://youtu.be/61gx0FfCvhU?t=2)

**等價關係**：兩個 $E$ 中的 Cauchy 數列 $(x_n)$、$(y_n)$ 等價，如果
$$\lim_{n\to\infty}\|x_n-y_n\|=0.$$

講者說：定義等價類之前，先定義等價關係。

$$\tilde E=\{\text{$E$ 中 Cauchy 數列的等價類}\},\qquad [(x_n)]=\text{和 $(x_n)$ 等價的所有 Cauchy 數列}.$$

$\tilde E$ 的**一個點不是一個 Cauchy 數列**，而是一整類「彼此距離趨近 0」的 Cauchy 數列。例如 $\mathbb{Q}$ 中趨近 $\pi$ 的各種有理數列，彼此的差趨近 0，所以是同一個點。[▶ part 2 03:09](https://youtu.be/61gx0FfCvhU?t=189)

**嵌入 $\Phi$**[▶ part 2 05:29](https://youtu.be/61gx0FfCvhU?t=329)：$\Phi(x)=[(x,x,x,\dots)]$，常數數列。講者說：「用很蠢的方式」把原空間的元素放進來；收斂到 $x$ 的非常數數列也在同一類，常數數列只是一個代表。

**運算**【課堂討論】[▶ part 2 07:06](https://youtu.be/61gx0FfCvhU?t=426) 講者問怎麼加，學生答「數列相加就好」：

$$[(x_n)]+[(y_n)]=[(x_n+y_n)],\qquad\lambda[(x_n)]=[(\lambda x_n)].$$

**要檢查 well-defined**（跟模運算一樣，結果不能依賴代表的選擇）[▶ part 2 08:46](https://youtu.be/61gx0FfCvhU?t=526)：設 $(x_n)\sim(\bar x_n)$、$(y_n)\sim(\bar y_n)$，則

$$\|(x_n+y_n)-(\bar x_n+\bar y_n)\|\le\|x_n-\bar x_n\|+\|y_n-\bar y_n\|\to0,$$

所以 $(x_n+y_n)\sim(\bar x_n+\bar y_n)$。純量乘法同理。向量空間的其他公理（結合律、零、負元素）都可以一一檢查。

**範數**[▶ part 2 11:30](https://youtu.be/61gx0FfCvhU?t=690)：

$$\|[(x_n)]\|_1=\lim_{n\to\infty}\|x_n\|.$$

極限存在是 Lemma 1.4.4（Cauchy 數列的範數收斂）。講者說課本寫到這裡已經懶得寫雙層括號了。

【課本補充】不依賴代表：若 $(x_n)\sim(y_n)$，則 $\big|\|x_n\|-\|y_n\|\big|\le\|x_n-y_n\|\to0$，所以兩個極限相等。

**(a)(b)** 顯然：$\Phi$ 線性；$\|\Phi(x)\|_1=\lim\|x\|=\|x\|$，保範數所以一對一。

**(c) 稠密**[▶ part 2 14:02](https://youtu.be/61gx0FfCvhU?t=842)：課本說每個 $X=[(x_n)]$ 是 $\Phi(x_n)$ 的極限。

以下**不是逐字稿內容**，是課本這句的推導：$\|\Phi(x_n)-X\|_1=\lim_{m\to\infty}\|x_n-x_m\|$。$(x_n)$ 是 Cauchy，所以 $n$ 大時這個極限 $\le\varepsilon$。所以 $\Phi(x_n)\to X$。

**(d) 完備**：講者說沒時間，證明不難，寧可跳過細節強調大意。[▶ part 2 15:56](https://youtu.be/61gx0FfCvhU?t=956)

【課本補充】(d) 的證明（p. 24–25）：設 $(X_n)$ 是 $\tilde E$ 中的 Cauchy 數列。

1. 由稠密，對每個 $n$ 取 $x_n\in E$ 使 $\|\Phi(x_n)-X_n\|_1<\frac1n$。
2. $(x_n)$ 是 $E$ 中的 Cauchy 數列：
   $$\|x_n-x_m\|=\|\Phi(x_n)-\Phi(x_m)\|_1\le\|X_n-X_m\|_1+\frac1n+\frac1m.$$
3. 令 $X=[(x_n)]\in\tilde E$。則
   $$\|X_n-X\|_1\le\|X_n-\Phi(x_n)\|_1+\|\Phi(x_n)-X\|_1<\frac1n+\|\Phi(x_n)-X\|_1\to0,$$
   最後一項 $\to0$ 是 (c) 的推導。∎

### 7.3 完備化依賴範數

【口頭】[▶ part 2 16:32](https://youtu.be/61gx0FfCvhU?t=992)

- 這個構造很厲害：任何不完備的空間都能完備化。
- 更有趣的是：同一個空間用不同範數完備化，結果**可能不一樣**，不只是集合不同，數學結構也不同。
- 有限維空間不是好例子：$\mathbb{R}^n$、$\mathbb{C}^n$、矩陣空間本來就完備（所以可以用「檢查 Cauchy」來證收斂，很方便）。
- **例子**：$\mathbb{Q}$ 對普通絕對值完備化得到 $\mathbb{R}$；對 **$p$-進範數**完備化得到 **$p$-進數** $\mathbb{Q}_p$，跟實數完全不同。

### 進度

講者說按課表第 1 章應該今天結束，但他估計還要一週：至少一天講線性映射，一天講壓縮映射。第 1 章作業有約 50 題，後面各章約 30 題，不用全做，「做到有趣就好，別把自己累壞」。[▶ part 2 18:47](https://youtu.be/61gx0FfCvhU?t=1127)

---

## 8. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 完備性證明模板 | 候選極限 → 在空間裡 → 按範數收斂 | 先用已知完備的空間造候選極限 |
| ℓ² 完備 | 座標 Cauchy ⟹ $\alpha_k=\lim_n\alpha_{n,k}$ | (1.10) 截成有限和，$m\to\infty$ 再 $K\to\infty$；Minkowski 證 $a\in\ell^2$ |
| $C([a,b])$ 完備 | 逐點 Cauchy ⟹ $f(x)=\lim f_n(x)$ | (1.12) 令 $m\to\infty$ 得一致估計；$\varepsilon/3$ 證連續 |
| 級數 | 收斂：部分和收斂；絕對收斂：$\sum\|x_n\|<\infty$ | $P([0,1])$ 中 $\sum x^k/k!$ 絕對收斂但不收斂 |
| Thm 1.4.9 (⟹) | 完備 ⟹ 絕對收斂級數收斂 | $\|s_m-s_n\|\le\sum_{r>k}\|x_r\|$，部分和 Cauchy |
| Thm 1.4.9 (⟸) | 絕對收斂級數收斂 ⟹ 完備 | 挑 $p_k$ 使 $\|x_{p_{k+1}}-x_{p_k}\|<2^{-k}$；伸縮和；Cauchy + 收斂子數列 ⟹ 收斂 |
| 閉子空間 | Banach 的閉子空間是 Banach | Cauchy 在大空間收斂，閉 ⟹ 極限在子空間 |
| 完備化 | $\tilde E$ = Cauchy 數列等價類，$\|[(x_n)]\|_1=\lim\|x_n\|$ | $\Phi(x)$ = 常數數列；稠密：$\Phi(x_n)\to[(x_n)]$ |
| 完備化依賴範數 | $\mathbb{Q}$：絕對值 → $\mathbb{R}$；$p$-進範數 → $\mathbb{Q}_p$ | |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $C([a,b])$ 完備（一致範數） | 第 8–9 集：壓縮映射定理、微分方程存在定理需要完備空間 |
| 絕對收斂 ⟹ 收斂 | 第 10 集：矩陣指數 $e^A=\sum A^k/k!$ |
| 完備化 | 第 11–14 集：Lebesgue 積分可以看成階梯函數空間的完備化；第 18 集：內積空間的完備化是 Hilbert 空間 |
| ℓ² 完備 | 第 18 集起：ℓ² 是 Hilbert 空間的標準例子 |
| 「Cauchy + 收斂子數列 ⟹ 收斂」 | 第 14 集：$L^1$ 中範數收斂的數列有幾乎處處收斂的子數列 |

---

## 附：本集一句話總結

> **Banach 空間就是 Cauchy 數列都收斂的賦範空間：ℓ² 和 $C([a,b])$ 都是，證法都是「逐座標／逐點取極限，再證它在空間裡且按範數收斂」；完備性等價於「絕對收斂級數都收斂」；而任何不完備的空間都能用 Cauchy 數列的等價類完備化，就像從 ℚ 造出 ℝ。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-01-27 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 20:07）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.4 整理。*
