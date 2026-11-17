---
course: Number Theory（2021 秋，線上錄影）
episode: 7
lecture: Lecture 7
date: 待補（2021 秋）
video: https://youtu.be/jBbFBFjwocQ
notes: Jones & Jones §2.1（書頁 19–24，PDF 頁 34–39）：Lemma 2.1、Corollary 2.2、Eisenstein 判別法、Example 2.1–2.2、Theorem 2.3、Lemma 2.4
---

# 第 7 集 · Lecture 7：算術基本定理（Fundamental Theorem of Arithmetic） [▶ 影片](https://youtu.be/jBbFBFjwocQ)

← 上一集：[06-polynomial-euclid-rationalization](06-polynomial-euclid-rationalization.md) ｜ [總目錄](README.md) ｜ 下一集：[08-structure-of-primes](08-structure-of-primes.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 7 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（43:00，自動字幕）＋ Jones & Jones §2.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 質數與合數](#1-質數與合數)
- [2. 質數與整除](#2-質數與整除)
- [3. Eisenstein 判別法](#3-eisenstein-判別法)
- [4. 算術基本定理](#4-算術基本定理)
- [5. 用質因數分解做計算](#5-用質因數分解做計算)
- [6. 恰好整除與 m 次方](#6-恰好整除與-m-次方)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】講者說這幾集「相當緊密地照著 Jones & Jones 走」，喜歡課本的證明就直接照抄 [▶ 12:00](https://youtu.be/jBbFBFjwocQ?t=720)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | 質數、合數；只需試到 $\sqrt n$ | §2.1 定義 |
| 2 | $p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$ | Lemma 2.1、Corollary 2.2、Exercise 2.1 |
| 3 | Eisenstein 判別法 | §2.1 p. 21–22 |
| 4 | 算術基本定理 | Theorem 2.3 |
| 5–6 | 用分解算 gcd、lcm；$p^e\Vert n$；互質之積為 $m$ 次方 | p. 23–24、Lemma 2.4 |

---

## 1. 質數與合數

### 1.1 定義

[▶ 00:00](https://youtu.be/jBbFBFjwocQ?t=0)

**定義**：整數 $p>1$ 叫**質數**，如果它的正因數只有 $1$ 和 $p$。（所以 $1$ 不是質數；第一個質數是 2，然後 3……）

【口頭】這定義有點隨意：7 的因數其實是 $\pm1$、$\pm7$，不只兩個。只看正因數是長久的慣例，讓討論簡單一點；在抽象代數的大架構裡，這算整數的特殊之處 [▶ 00:33](https://youtu.be/jBbFBFjwocQ?t=33)。

若 $n\mid p$ 且 $n,p$ 都是正的，則 $0<n\le p$。所以要檢查 $p$ 是否為質數，只要試 $2,3,\dots,p-1$ 是否整除 $p$——但還能做得更好。

**定義** [▶ 02:11](https://youtu.be/jBbFBFjwocQ?t=131)：整數 $n$ 叫**合數**（composite），如果存在 $1<a,b<n$ 使 $n=ab$。（不允許 $a$ 或 $b$ 是 1，否則 $n = 1\cdot n$ 太無聊；要是「真正」拆成兩個較小的數。）

### 1.2 只要試到 $\sqrt n$

**命題 1** [▶ 02:43](https://youtu.be/jBbFBFjwocQ?t=163)：若 $n$ 是合數，則存在 $a$ 使 $a\mid n$ 且 $1<a\le\sqrt n$。

**證明**：$n=ab$，$1<a,b<n$。若 $a>\sqrt n$ 且 $b>\sqrt n$，則
$$n = ab > \sqrt n\cdot\sqrt n = n,$$
矛盾。所以 $a,b$ 中至少一個 $\le\sqrt n$。∎

所以要判斷 $n$ 是不是質數（**質數判定**，primality testing），只要試到 $\sqrt n$（可以用計算機估）。

**例** [▶ 04:20](https://youtu.be/jBbFBFjwocQ?t=260)：
- $n=42$：$\sqrt{42}\approx6.48$，只要試 $2,3,4,5,6$。其實試到 2 就知道不是質數。
- $n=35$：$\sqrt{35}\approx5.91$，試 $2,3,4,5$。2、3、4 不整除，5 整除：$35 = 5\cdot7$，合數。

【口頭】除了 2，偶數都不是質數，所以找質數時應該只看奇數——講者說他接下來兩集常常忘記這個改進 [▶ 04:53](https://youtu.be/jBbFBFjwocQ?t=293)。

---

## 2. 質數與整除

### 2.1 命題 2

[▶ 05:56](https://youtu.be/jBbFBFjwocQ?t=356)

**命題 2**：$p$ 質數，$a,b$ 整數（不必是正的）。
1. 要嘛 $p\mid a$，要嘛 $\gcd(a,p)=1$（互質）。
2. 若 $p\mid ab$，則 $p\mid a$ 或 $p\mid b$（也可能兩個都整除）。

**證明**：
1. $\gcd(a,p)$ 是 $p$ 的正因數，只能是 $1$ 或 $p$。若是 $p$，則 $p\mid a$；若是 $1$，互質。
2. 設 $p\mid ab$ 且 $p\nmid a$，證 $p\mid b$。由 (1)，$\gcd(a,p)=1$。由 Bézout，存在 $u,v$ 使
$$au+pv = 1.$$
乘 $b$：
$$abu + pbv = b.$$
$p\mid ab$，所以 $p\mid abu$；$p\mid pbv$ 顯然。所以 $p$ 整除兩項之和 $b$。∎

【口頭】整除對質數特別好用，比一般的數好 [▶ 09:18](https://youtu.be/jBbFBFjwocQ?t=558)。（對照第 5 集：$10\mid 50\cdot2$ 但 $10\nmid2$；換成質數就不會發生。）

### 2.2 命題 3：推廣到多個因數

[▶ 09:50](https://youtu.be/jBbFBFjwocQ?t=590)

**命題 3**：$p$ 質數，若 $p\mid a_1a_2\cdots a_k$，則存在某個 $j$ 使 $p\mid a_j$。

【口頭】質數不能「跨坐」：不會一半在 $a_1$、一半在 $a_2$。

**證明**（對 $k$ 歸納）：
- **基底** $k=2$：命題 2(2)。
- **歸納步驟**：設對 $k$ 成立。若 $p\mid a_1\cdots a_{k+1}$，令 $a = a_1\cdots a_k$、$b = a_{k+1}$。由命題 2(2)，$p\mid a$ 或 $p\mid b$。
  - $p\mid a_{k+1}$：完成。
  - $p\mid a_1\cdots a_k$：由歸納假設，$p\mid a_j$，某個 $1\le j\le k$。

兩種情況都有 $j\in\{1,\dots,k+1\}$。∎

### 2.3 命題 4

[▶ 12:00](https://youtu.be/jBbFBFjwocQ?t=720)

**命題 4**：$p$ 質數，若 $p\mid a^k$，則 $p\mid a$，因而 $p^k\mid a^k$。

**證明**：$a^k = a\cdot a\cdots a$（$k$ 個），由命題 3（所有 $a_j=a$），$p\mid a$。接著直接用定義：$a = pj$ ⇒ $a^k = (pj)^k = p^kj^k$，所以 $p^k\mid a^k$。∎

（也可以反覆用第 4 集的性質「$a\mid b$、$c\mid d$ ⇒ $ac\mid bd$」。講者說：對那個性質不熟的話，直接從定義證就好 [▶ 14:11](https://youtu.be/jBbFBFjwocQ?t=851)。）

【口頭】本集暗號是「wizard」[▶ 14:45](https://youtu.be/jBbFBFjwocQ?t=885)。

> 【課本補充】命題 2、3、4 分別是課本 Lemma 2.1、Corollary 2.2、Exercise 2.1（p. 20–21）。課本另外指出：$p$ 不是質數時兩部分都可能錯，例如 $p=4$、$a=6$、$b=10$（$4\mid60$ 但 $4\nmid6$、$4\nmid10$；且 $4\nmid6$ 但 $\gcd(6,4)=2\neq1$）。

---

## 3. Eisenstein 判別法

### 3.1 整係數多項式的可約性

[▶ 14:45](https://youtu.be/jBbFBFjwocQ?t=885)

稍微離題，看質數在**整係數多項式的不可約性**上的應用。

**定義**：整係數多項式 $f(x)$ 在 $\mathbb{Z}$ 上**可約**（reducible），如果存在**非常數**的整係數多項式 $g(x),h(x)$ 使 $f(x) = g(x)h(x)$；否則叫**不可約**（irreducible）。

【口頭】這就是補救代數課裡那種「只准用整數」的因式分解 [▶ 15:18](https://youtu.be/jBbFBFjwocQ?t=918)。

### 3.2 判別法

[▶ 16:23](https://youtu.be/jBbFBFjwocQ?t=983)

**Eisenstein 判別法**（Eisenstein's criterion）：$f(x) = a_0+a_1x+\cdots+a_nx^n$，$a_i\in\mathbb{Z}$。若有質數 $p$ 使
1. $p\mid a_0, a_1, \dots, a_{n-1}$；
2. $p\nmid a_n$；
3. $p^2\nmid a_0$；

則 $f(x)$ 在 $\mathbb{Z}$ 上不可約。

【口頭】$f$ 首一時 $a_n=1$，條件 2 自動成立；講者說他常常忘了檢查這條 [▶ 16:55](https://youtu.be/jBbFBFjwocQ?t=1015)。

**證明**（反證）[▶ 18:13](https://youtu.be/jBbFBFjwocQ?t=1093)：設
$$f(x) = g(x)h(x),\quad g = b_0+b_1x+\cdots+b_sx^s,\quad h = c_0+c_1x+\cdots+c_tx^t,\quad s,t\ge1.$$
1. **常數項**：$a_0 = b_0c_0$。$p\mid a_0$、$p^2\nmid a_0$，所以 $p$ 恰好整除 $b_0,c_0$ 其中一個（若兩個都整除，$p^2\mid b_0c_0$）。$b$、$c$ 地位對稱，**不失一般性**設 $p\mid b_0$、$p\nmid c_0$。
2. **首項**：$a_n = b_sc_t$。$p\nmid a_n$，所以 $p\nmid b_s$。
3. 所以存在最小的 $i\le s$ 使 $p\nmid b_i$，而 $p\mid b_0,\dots,b_{i-1}$。
4. 看 $x^i$ 的係數：
$$a_i = b_0c_i + b_1c_{i-1} + \cdots + b_{i-1}c_1 + b_ic_0.$$
因為 $i\le s<n$（$t\ge1$），$p\mid a_i$。除了最後一項，每一項都含 $b_0,\dots,b_{i-1}$ 之一，都被 $p$ 整除。所以 $p\mid b_ic_0$。
5. 由命題 2(2)，$p\mid b_i$ 或 $p\mid c_0$。前者和 $i$ 的選法矛盾；後者和第 1 步矛盾。∎

【口頭】一般要證整係數多項式不可約很可怕：要考慮所有可能的分解。Eisenstein 讓你幾乎不費力就得到很多例子 [▶ 22:04](https://youtu.be/jBbFBFjwocQ?t=1324)。

### 3.3 例子

**例 1：任意高次的不可約多項式** [▶ 22:38](https://youtu.be/jBbFBFjwocQ?t=1358)
$$f(x) = x^n + 9x + 3\quad(n\ge2).$$
取 $p=3$：$3\mid a_0=3$、$3\mid a_1=9$，其他中間係數都是 0（$3\mid0$，「對但有點蠢」）；$3\nmid a_n=1$；$9\nmid3$。所以 $f$ 不可約。$n$ 任意 ⇒ **有任意高次的整係數不可約多項式**。

**例 2：分圓多項式** [▶ 24:18](https://youtu.be/jBbFBFjwocQ?t=1458)

$p$ 質數，**$p$ 次分圓多項式**（cyclotomic polynomial；和「單位根」有關，之後會再談）：
$$\Phi_p(x) = 1+x+x^2+\cdots+x^{p-1}.$$
**命題**：$\Phi_p(x)$ 在 $\mathbb{Z}$ 上不可約。

**證明**：
1. **換變數的技巧**：令 $f(x) = \Phi_p(x+1)$。若 $\Phi_p = gh$，則 $f(x) = g(x+1)h(x+1)$ 也可約。所以只要證 $f$ 不可約。
2. $x^p-1 = (x-1)(x^{p-1}+\cdots+x+1)$，所以 $\Phi_p(x) = \dfrac{x^p-1}{x-1}$。
3. 代 $x+1$，用二項式定理（第 3 集）：
$$f(x) = \frac{(x+1)^p-1}{x} = x^{p-1} + \binom{p}{p-1}x^{p-2} + \cdots + \binom p2x + \binom p1.$$
（兩個 1 消掉，再除以 $x$。）
4. 檢查 Eisenstein（用質數 $p$）：首項係數 1，$p\nmid1$；中間係數 $\binom pi$（$1\le i\le p-1$）都被 $p$ 整除；常數項 $\binom p1 = p$，$p^2\nmid p$。所以 $f$ 不可約，$\Phi_p$ 也不可約。∎

【口頭】幾集之後會有第二個檢查可約性的工具；Eisenstein 是第一個 [▶ 27:07](https://youtu.be/jBbFBFjwocQ?t=1627)。

> 【課本補充】課本把 Eisenstein 放在 §2.1（p. 21），證明相同；Example 2.1：$x^3-4x+2$ 用 $p=2$ 不可約；Example 2.2 就是上面的 $\Phi_p$。課本說 $\binom pi$ 被 $p$ 整除的理由：$\binom pi = \dfrac{p!}{i!(p-i)!}$，分子有 $p$、分母沒有。

---

## 4. 算術基本定理

[▶ 27:43](https://youtu.be/jBbFBFjwocQ?t=1663)

**定理（算術基本定理，Fundamental Theorem of Arithmetic）**：每個整數 $n>1$ 都有**質數冪分解**（prime-power factorization）
$$n = p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k},$$
其中 $p_1,\dots,p_k$ 是**相異**質數、$e_i\ge1$；而且這分解**除了因數的順序之外是唯一的**。

（例：$200 = 2^3\cdot5^2$，也可寫 $5^2\cdot2^3$，但沒有別的分解。——課本的例子。）

### 4.1 存在（強歸納）

[▶ 28:29](https://youtu.be/jBbFBFjwocQ?t=1709)

- **基底**：$2 = 2^1$。
- **歸納步驟**：設 $2,\dots,n-1$ 都有質數冪分解。若 $n$ 是質數，$n=n^1$。否則 $n = ab$，$1<a,b<n$。由歸納假設 $a,b$ 都有分解，相乘，再把相同質數的冪合併，就得到 $n$ 的分解。

（這就是第 2 集的論證。）

### 4.2 唯一

[▶ 29:37](https://youtu.be/jBbFBFjwocQ?t=1777)

【口頭】講者說他講義上的唯一性證明「普普通通」，可以寫得更好；下面照課本 Theorem 2.3（p. 22–23）的寫法整理，和講者的想法相同。

設
$$n = p_1^{e_1}\cdots p_k^{e_k} = q_1^{f_1}\cdots q_l^{f_l},$$
$p_i$ 相異、$q_j$ 相異，指數都是正的。

1. $p_1\mid n = q_1^{f_1}\cdots q_l^{f_l}$。由命題 3，$p_1\mid q_j$ 對某個 $j$。$q_j$ 是質數、$p_1\neq1$，所以 $p_1 = q_j$。重新編號設 $j=1$。
2. 兩邊同除以 $p_1$：
$$p_1^{e_1-1}p_2^{e_2}\cdots p_k^{e_k} = q_1^{f_1-1}q_2^{f_2}\cdots q_l^{f_l}.$$
3. 重複這個「配對、約掉」的步驟。若 $e_1\neq f_1$（例如 $e_1<f_1$），約掉 $e_1$ 次之後，右邊還有 $p_1$、左邊沒有了，但 $p_1$ 整除右邊，所以整除左邊某個 $p_i$（$i\ge2$），和 $p_i$ 相異矛盾。所以 $e_1=f_1$。
4. 一直做下去。若一邊的質數先用完，那時會得到「$1$ = 一些質數的乘積」，不可能（質數 $>1$）。所以兩邊同時用完：$k=l$，配對後 $p_i=q_i$、$e_i=f_i$。∎

⚠️ 講者板書在 [▶ 31:18](https://youtu.be/jBbFBFjwocQ?t=1878) 把 $q_j$ 寫成 $f_j$，自己更正；又為了區分下標臨時發明了「$j''$」記號（「抱歉，這很蠢」）。

---

## 5. 用質因數分解做計算

[▶ 33:00](https://youtu.be/jBbFBFjwocQ?t=1980)

【口頭】這叫「算術」基本定理，因為很多算術問題知道分解就能解決。這些小時候學過，只是現在記號比較嚇人 [▶ 33:36](https://youtu.be/jBbFBFjwocQ?t=2016)。

**技巧**：把 $a,b$ 的所有相異質因數合成一張表 $p_1,\dots,p_k$，允許指數為 0，兩數就能用**同一組質數**寫：
$$a = p_1^{e_1}\cdots p_k^{e_k},\qquad b = p_1^{f_1}\cdots p_k^{f_k},\qquad e_i,f_i\ge0.$$

| 運算 | 結果 |
|---|---|
| $ab$ | 指數相加 $e_i+f_i$ |
| $a/b$（若 $b\mid a$） | 指數相減 $e_i-f_i$ |
| $a^m$ | 指數乘 $m$ |
| $\gcd(a,b)$ | 指數取 $\min(e_i,f_i)$ |
| $\mathrm{lcm}(a,b)$ | 指數取 $\max(e_i,f_i)$ |

**例** [▶ 34:08](https://youtu.be/jBbFBFjwocQ?t=2048)：
$$a = 31500 = 2^2\cdot3^2\cdot5^3\cdot7,\qquad b = 13475 = 5^2\cdot7^2\cdot11.$$
統一成 $2,3,5,7,11$：
$$a = 2^2\,3^2\,5^3\,7^1\,11^0,\qquad b = 2^0\,3^0\,5^2\,7^2\,11^1.$$
- $\gcd = 2^0\,3^0\,5^{\min(3,2)}\,7^{\min(1,2)}\,11^0 = 5^2\cdot7 = 175$。
- $\mathrm{lcm} = 2^2\,3^2\,5^3\,7^2\,11 = 2425500$。
- 檢查：$ab/175 = 2425500$，和第 5 集的定理 $\gcd\cdot\mathrm{lcm}=ab$ 一致。

⚠️ 逐字稿缺字：[▶ 36:19](https://youtu.be/jBbFBFjwocQ?t=2179) 字幕在 lcm 那裡唸成「eleven squared」，但 $b$ 裡只有 $11^1$，而且算出的數字 $2425500$ 對應的是 $11^1$。

**用分解重證 $\gcd\cdot\mathrm{lcm}=ab$** [▶ 37:24](https://youtu.be/jBbFBFjwocQ?t=2244)：
$$\gcd\cdot\mathrm{lcm} = \prod_i p_i^{\min(e_i,f_i)+\max(e_i,f_i)} = \prod_i p_i^{e_i+f_i} = ab,$$
因為 $\min(e,f)+\max(e,f)$ 一個是 $e$、另一個是 $f$，和總是 $e+f$。

【口頭】但分解大數**很花時間**（課本也這麼說），所以第 5 集用輾轉相除法的方法在實務上更好。

---

## 6. 恰好整除與 m 次方

### 6.1 恰好整除

[▶ 37:57](https://youtu.be/jBbFBFjwocQ?t=2277)

**定義**：若 $p^e\mid n$ 但 $p^{e+1}\nmid n$，就說 $p^e$ **恰好整除** $n$（exactly divides），寫 $p^e\,\Vert\,n$。也就是 $p^e$ 是 $n$ 的分解裡 $p$ 的那一項。

**例** [▶ 38:30](https://youtu.be/jBbFBFjwocQ?t=2310)：$1250 = 10\cdot125 = 2\cdot5^4$，所以 $2\,\Vert\,1250$、$5^4\,\Vert\,1250$。

**命題**（講者說「與其說是例子，不如說是定理」）：$p_1,\dots,p_s$ 相異質數，
$$n = p_1^{e_1}\cdots p_s^{e_s} \iff p_j^{e_j}\,\Vert\,n \text{ 對每個 } j.$$

> 【課本補充】p. 23：$2^3\Vert200$、$5^2\Vert200$、$p^0\Vert200$（$p\neq2,5$）。若 $p^e\Vert a$、$p^f\Vert b$，則 $p^{e+f}\Vert ab$、$p^{me}\Vert a^m$ 等。

### 6.2 互質之積是 $m$ 次方

[▶ 39:41](https://youtu.be/jBbFBFjwocQ?t=2381)

**定理**：$a_1,\dots,a_s$ 是兩兩互質的正整數，若 $a_1a_2\cdots a_s = x^m$，則每個 $a_j$ 都是 $m$ 次方：存在 $x_j$ 使 $a_j = x_j^m$。

**證明**：
1. $a_i$ 兩兩互質 ⇒ 它們**沒有共同的質因數**。所以把每個 $a_j$ 分解，所有質數合起來是一張相異質數的表，每個質數只屬於一個 $a_j$。
2. $x = q_1^{f_1}\cdots q_t^{f_t}$，所以 $x^m = q_1^{mf_1}\cdots q_t^{mf_t}$。
3. 由分解的**唯一性**，$a_1\cdots a_s$ 分解裡的每個質數冪 $p^e$ 都要對上某個 $q_k^{mf_k}$，所以 $e = mf_k$ 是 $m$ 的倍數。
4. 每個 $a_j$ 的所有指數都是 $m$ 的倍數，把 $m$ 提出來，$a_j$ 就是某數的 $m$ 次方。∎

【口頭】講者道歉這個證明下標太多，他喜歡記號；Jones & Jones 的論證只有一段話、沒有記號，看得懂的話更好 [▶ 42:34](https://youtu.be/jBbFBFjwocQ?t=2554)。

> 【課本補充】Lemma 2.4（p. 23–24）要求 $m\ge2$，證法：正整數是 $m$ 次方 ⇔ 分解中每個指數都被 $m$ 整除；$a$ 的因數 $a_i$ 兩兩互質時，$a_i$ 裡的每個 $p^e$ 也是 $a$ 裡 $p$ 的完整冪次，所以 $m\mid e$。
> - **互質不能省**：$24$ 和 $54$ 都不是平方數，但 $24\cdot54 = 1296 = 36^2$。
> - 課本說這引理在 $m=2$ 時之後非常有用。
> - 緊接著的 Corollary 2.5（若 $m$ 不是平方數，$\sqrt m$ 是無理數）屬於第 9 集的內容。

---

## 7. 一頁速查表

**質數與合數**
- 質數：$p>1$，正因數只有 $1,p$。合數：$n=ab$，$1<a,b<n$。
- 合數必有因數 $1<a\le\sqrt n$。關鍵：$a,b>\sqrt n$ ⇒ $ab>n$。

**質數整除**
- $p\mid a$ 或 $\gcd(a,p)=1$。
- $p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$。關鍵：$au+pv=1$，乘 $b$：$b = abu+pbv$。
- $p\mid a_1\cdots a_k\Rightarrow p\mid a_j$（歸納）。$p\mid a^k\Rightarrow p^k\mid a^k$。

**Eisenstein**：$p\mid a_0,\dots,a_{n-1}$，$p\nmid a_n$，$p^2\nmid a_0$ ⇒ 在 $\mathbb{Z}$ 上不可約。
- 關鍵：$p$ 恰整除 $b_0,c_0$ 之一；取最小 $i$ 使 $p\nmid b_i$，由 $a_i$ 得 $p\mid b_ic_0$，矛盾。
- $x^n+9x+3$（$p=3$）；$\Phi_p(x+1) = \frac{(x+1)^p-1}{x}$（係數 $\binom pi$）。

**算術基本定理**：$n>1$ 唯一寫成 $p_1^{e_1}\cdots p_k^{e_k}$。
- 存在：強歸納（合數 $=ab$）。唯一：$p_1\mid\prod q_j^{f_j}$ ⇒ $p_1=q_j$，約掉，重複。

**用分解計算**：乘→指數加；$\gcd$→min；$\mathrm{lcm}$→max。$\min+\max = e+f$ ⇒ $\gcd\cdot\mathrm{lcm}=ab$。
- $31500 = 2^23^25^37$，$13475 = 5^27^211$：gcd $175$，lcm $2425500$。

**恰好整除**：$p^e\Vert n$ ⇔ $p^e\mid n$、$p^{e+1}\nmid n$。

**兩兩互質之積 = $m$ 次方 ⇒ 每個都是 $m$ 次方**。關鍵：質因數不共用 + 唯一分解 ⇒ 指數都是 $m$ 的倍數。反例（不互質）：$24\cdot54=36^2$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 質數、試除到 $\sqrt n$ | 第 8 集（質數的結構、質數判定） |
| 算術基本定理、Corollary 2.5 | 第 9 集（$\sqrt2$ 是無理數） |
| 分圓多項式 $\Phi_p$ | 第 19 集（單位根） |
| 多項式的可約性 | 第 11、13 集（多項式的整數根、多項式同餘） |
| 互質之積為平方 ⇒ 各為平方（$m=2$） | 第 21 集（平方和）、第 24 集（畢氏三元數組分類、費馬最後定理） |
| $p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$ | 第 22 集（高斯質數，類比的性質） |

---

## 附：本集一句話總結

> **質數的關鍵性質是「$p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$」（由 Bézout 得到）；它推出算術基本定理的唯一性，讓 gcd、lcm 變成指數取 min、max，也給出 Eisenstein 判別法（例如分圓多項式 $\Phi_p$ 不可約）和「兩兩互質之積為 $m$ 次方則各為 $m$ 次方」。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 7 錄影逐字稿（YouTube 自動字幕，43:00）與 Jones & Jones《Elementary Number Theory》§2.1 整理。*
