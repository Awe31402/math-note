---
course: Number Theory（2021 秋，線上錄影）
episode: 5
lecture: Lecture 5
date: 待補（2021 秋）
video: https://youtu.be/BDf4V_l8e3E
notes: Jones & Jones §1.2–1.4（書頁 7–16，PDF 頁 22–31）：Theorem 1.7–1.8、Corollary 1.9–1.11、Exercise 1.8–1.9、Theorem 1.12、Theorem 1.13
---

# 第 5 集 · Lecture 5：向量輾轉相除法、Bézout 定理、gcd、lcm、線性丟番圖方程 [▶ 影片](https://youtu.be/BDf4V_l8e3E)

← 上一集：[04-divisibility-euclidean-algorithm](04-divisibility-euclidean-algorithm.md) ｜ [總目錄](README.md) ｜ 下一集：[06-polynomial-euclid-rationalization](06-polynomial-euclid-rationalization.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 5 集（播放清單第 6 部；第 5 部是 15 秒的「secret word」短片，略過）
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（57:34，自動字幕）＋ Jones & Jones §1.2–1.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 向量輾轉相除法](#1-向量輾轉相除法)
- [2. Bézout 定理與 gcd 的性質](#2-bézout-定理與-gcd-的性質)
- [3. 多個數的 gcd 與延伸 Bézout](#3-多個數的-gcd-與延伸-bézout)
- [4. 哪些數能寫成 ax+by](#4-哪些數能寫成-axby)
- [5. 互質及其推論](#5-互質及其推論)
- [6. 最小公倍數](#6-最小公倍數)
- [7. 線性丟番圖方程](#7-線性丟番圖方程)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | 向量輾轉相除法：邊算 gcd 邊記錄係數 | §1.2 Theorem 1.7 的證明方法 |
| 2 | Bézout 定理；$c\mid a,b\iff c\mid\gcd$ | Theorem 1.7、Exercise 1.8 |
| 3 | $\gcd(a,b,c)=\gcd(\gcd(a,b),c)$ | Exercise 1.9、1.11 |
| 4 | $ax+by$ 恰好是 $d$ 的倍數 | Theorem 1.8 |
| 5 | 互質、$\gcd(a/d,b/d)=1$、$a\mid bc\Rightarrow a\mid c$ | Corollary 1.9–1.11 |
| 6 | $\gcd\cdot\mathrm{lcm}=ab$ | §1.3 Theorem 1.12 |
| 7 | $ax+by=c$ 的全部整數解 | §1.4 Theorem 1.13 |

【口頭】講者說本集基本上是在走 Jones & Jones 第 1 章 [▶ 50:29](https://youtu.be/BDf4V_l8e3E?t=3029)。

---

## 1. 向量輾轉相除法

### 1.1 想法

[▶ 00:00](https://youtu.be/BDf4V_l8e3E?t=0)

上一集用「倒著代回去」把 gcd 寫成 $ax+by$，很容易算錯。**向量輾轉相除法**（vector Euclidean algorithm，又叫擴展輾轉相除法）是邊做輾轉相除、邊記錄**每個餘數是 $a,b$ 的什麼組合**。

**在解什麼**：給 $a,b$，同時求出 $d=\gcd(a,b)$ 和整數 $x,y$ 使 $d = ax+by$。

**步驟**：做一張兩欄的表，左欄是數字，右欄是「這個數 = $a,b$ 的什麼組合」。
1. 第一列 $a$，記作 $a$；第二列 $b$，記作 $b$。
2. 每一步：上上一列 $= q\times$ 上一列 $+$ 餘數。新的一列寫餘數；右欄做**一模一樣的運算**：
$$r_{\text{新}} = r_{\text{上上}} - q\, r_{\text{上}}\quad\Longrightarrow\quad (\text{組合})_{\text{新}} = (\text{組合})_{\text{上上}} - q\,(\text{組合})_{\text{上}}.$$
3. 餘數變 0 就停。最後一個非零餘數是 $d$，它右欄的組合就是 Bézout 係數。

【口頭】「數字那欄有什麼規律，字母那欄就要有一模一樣的規律」[▶ 07:12](https://youtu.be/BDf4V_l8e3E?t=432)。講者承認這不簡單，他自己也花了一陣子才懂：拿一題一列一列做，做到不看也能寫出下一列，就懂了 [▶ 07:46](https://youtu.be/BDf4V_l8e3E?t=466)。

### 1.2 例子

**$\gcd(20,12)$**（上一集的例子）[▶ 01:07](https://youtu.be/BDf4V_l8e3E?t=67)

| 數 | 組合 | 怎麼來 |
|---|---|---|
| 20 | $a$ | |
| 12 | $b$ | |
| 8 | $a-b$ | $20-1\cdot12$ |
| 4 | $b-(a-b) = 2b-a$ | $12-1\cdot8$ |
| 0 | | $8 = 2\cdot4$ |

所以 $4 = 2\cdot12 - 20$。

**$\gcd(1960,247)$**（上一集讓講者很頭痛的例子）[▶ 02:48](https://youtu.be/BDf4V_l8e3E?t=168)

| 數 | 組合 | 怎麼來 |
|---|---|---|
| 1960 | $a$ | |
| 247 | $b$ | |
| 231 | $a-7b$ | $1960-7\cdot247$ |
| 16 | $b-(a-7b) = -a+8b$ | $247-1\cdot231$ |
| 7 | $(a-7b)-14(-a+8b) = 15a-119b$ | $231-14\cdot16$ |
| 2 | $(-a+8b)-2(15a-119b) = -31a+246b$ | $16-2\cdot7$ |
| 1 | $(15a-119b)-3(-31a+246b) = 108a-857b$ | $7-3\cdot2$ |

所以 $1 = 108\cdot1960 - 857\cdot247$，和上一集倒推的結果一樣。（中間幾列的組合是依同樣規則補算的；講者說「不用我一列一列唸」。）

【口頭】Bill Cook 的網站也給出 $108\cdot1960 + (-857)\cdot247 = 1$。這種係數**不唯一**；但照輾轉相除法做，應該會得到和網站一樣的組合 [▶ 04:59](https://youtu.be/BDf4V_l8e3E?t=299)。

**$\gcd(100,42)$** [▶ 05:31](https://youtu.be/BDf4V_l8e3E?t=331)

| 數 | 組合 | 怎麼來 |
|---|---|---|
| 100 | $a$ | |
| 42 | $b$ | |
| 16 | $a-2b$ | $100-2\cdot42$ |
| 10 | $b-2(a-2b) = -2a+5b$ | $42-2\cdot16$ |
| 6 | $(a-2b)-(-2a+5b) = 3a-7b$ | $16-10$ |
| 4 | $(-2a+5b)-(3a-7b) = -5a+12b$ | $10-6$ |
| 2 | $(3a-7b)-(-5a+12b) = 8a-19b$ | $6-4$ |
| 0 | | $4=2\cdot2$ |

所以 $2 = 8\cdot100 - 19\cdot42 = 800-798$。✓（4 和 2 那兩列是依規則補的，講者只說「繼續做到 2」。）

**$\gcd(42,17)$**（比較簡單的，講者說也許該先教這個）[▶ 08:53](https://youtu.be/BDf4V_l8e3E?t=533)

| 數 | 組合 | 怎麼來 |
|---|---|---|
| 42 | $a$ | |
| 17 | $b$ | |
| 8 | $a-2b$ | $42-2\cdot17$ |
| 1 | $b-2(a-2b) = -2a+5b$ | $17-2\cdot8$ |

所以 $1 = -2\cdot42+5\cdot17 = -84+85$。✓（$5 = 1+(-2)(-2)$。）

**$\gcd(20,5)$**（很蠢的例子）[▶ 10:29](https://youtu.be/BDf4V_l8e3E?t=629)：$20 = 4\cdot5+0$。一個數是另一個的倍數時，gcd 就是較小的那個：$5 = 0\cdot20+1\cdot5$。順便看到 $a-4b=0$。

【口頭】講者的經驗：這比倒著代回去**容易太多** [▶ 10:29](https://youtu.be/BDf4V_l8e3E?t=629)。

---

## 2. Bézout 定理與 gcd 的性質

### 2.1 Bézout 定理

[▶ 02:15](https://youtu.be/BDf4V_l8e3E?t=135)

**定理（Bézout）**：若整數 $a,b$ 不全為 0，則存在整數 $x,y$ 使
$$\gcd(a,b) = ax+by.$$

⚠️ 逐字稿缺字：字幕把 Bézout 寫成「azus」「bizou's」「bazoo's」，都是 Bézout。

**兩種證法**：
1. 向量輾轉相除法本身就是構造性的證明。

   > 【課本補充】Theorem 1.7（p. 7–8）就是這樣證：從輾轉相除的倒數第二式 $r_{n-1} = r_{n-3}-q_{n-1}r_{n-2}$ 開始，一步步消去 $r_{n-2},r_{n-3},\dots$，最後只剩 $a,b$。
2. **良序原理**（講者的「註解」）[▶ 11:34](https://youtu.be/BDf4V_l8e3E?t=694)：集合 $\{ax+by : x,y\in\mathbb{Z}\}$ 中的**正**數形成 $\mathbb{N}$ 的非空子集合，所以有最小元素。第 4 節會證明這個最小元素就是 gcd。

### 2.2 命題 1：公因數整除 gcd

[▶ 12:05](https://youtu.be/BDf4V_l8e3E?t=725)

**命題 1**：$a,b$ 不全為 0。則
$$c\mid a \text{ 且 } c\mid b \iff c\mid\gcd(a,b).$$

**證明**：
- (⇒) 由 Bézout，$\gcd(a,b) = ax+by$。$c$ 整除 $a$ 和 $b$，由上一集的性質 7（整除線性組合），$c\mid ax+by = \gcd(a,b)$。
- (⇐) $\gcd(a,b)$ 是 $a,b$ 的公因數。$c\mid\gcd(a,b)$ 且 $\gcd(a,b)\mid a$，由遞移性 $c\mid a$；同理 $c\mid b$。∎

（這是課本 Exercise 1.8。）

---

## 3. 多個數的 gcd 與延伸 Bézout

### 3.1 命題 2

[▶ 13:11](https://youtu.be/BDf4V_l8e3E?t=791)

多個數的 gcd 定義和兩個數一樣：所有公因數中最大的。

**命題 2**：$\gcd(a,b,c) = \gcd(\gcd(a,b),\,c)$。

**證明**：令 $d = \gcd(\gcd(a,b),c)$。
1. **$d$ 是 $a,b,c$ 的公因數**：$d\mid\gcd(a,b)$，而 $\gcd(a,b)$ 整除 $a$ 和 $b$，所以 $d\mid a$、$d\mid b$；又 $d\mid c$。
2. **$d$ 最大**：設 $d''$ 也整除 $a,b,c$。由命題 1，$d''\mid a$、$d''\mid b$ 推出 $d''\mid\gcd(a,b)$。於是 $d''$ 是 $\gcd(a,b)$ 和 $c$ 的公因數，所以 $d''\le d$。

所以 $d=\gcd(a,b,c)$。∎

反覆用就得到更多個數的版本，例如 $\gcd(a,b,c,d) = \gcd(\gcd(\gcd(a,b),c),d)$。

【口頭】講者一度看不懂自己寫的四個數的括號，卡了一下才想通 [▶ 15:22](https://youtu.be/BDf4V_l8e3E?t=922)。

**例**：$\gcd(20,30,5,3)$ [▶ 16:39](https://youtu.be/BDf4V_l8e3E?t=999)
$$= \gcd(\gcd(\gcd(20,30),5),3) = \gcd(\gcd(10,5),3) = \gcd(5,3) = 1.$$

> 【課本補充】Exercise 1.9 和 Example 1.5（p. 9）：$\gcd(36,24,54,27)$：$\gcd(36,24)=12$，$\gcd(12,54)=6$，$\gcd(6,27)=3$。

### 3.2 延伸 Bézout

[▶ 17:45](https://youtu.be/BDf4V_l8e3E?t=1065)

**定理**：若 $a_1,\dots,a_n$ 不全為 0，則存在整數 $x_1,\dots,x_n$ 使
$$a_1x_1+\cdots+a_nx_n = \gcd(a_1,\dots,a_n).$$

**證明概要**：$\gcd(a_1,\dots,a_n) = \gcd(\gcd(a_1,a_2),a_3,\dots,a_n)$，一路拆成兩兩一組。每一組用 Bézout 寫成線性組合，再把前一組的組合代進去。整數線性組合代入整數線性組合，還是整數線性組合。講者說一般證明不有趣，用例子說明比較清楚。

**例**：$\gcd(300,17,56)$ [▶ 18:49](https://youtu.be/BDf4V_l8e3E?t=1129)
1. 向量輾轉相除：$\gcd(300,17) = 1 = -3\cdot300+53\cdot17$。
2. $\gcd(300,17,56) = \gcd(1,56) = 1 = 0\cdot56+1\cdot1$。
3. 把第 1 步的 1 代進去：
$$1 = 0\cdot56 + (-3\cdot300+53\cdot17) = -3\cdot300+53\cdot17+0\cdot56.$$
所以 $x=-3$、$y=53$、$z=0$。

【口頭】這例子不夠豐富：如果第 2 步的 gcd 不是 1（例如是 10），就得把第 1 步的組合乘上某個數再代入，兩次 Bézout 的係數會混在一起 [▶ 20:29](https://youtu.be/BDf4V_l8e3E?t=1229)。

**例**：$\gcd(200,15,60)$ [▶ 21:35](https://youtu.be/BDf4V_l8e3E?t=1295)
- $\gcd(200,15)=5 = 1\cdot200-13\cdot15$。
- $\gcd(5,60)=5 = 1\cdot5+0\cdot60$。
- 代入：$5 = 1\cdot200-13\cdot15+0\cdot60$。

**例**：$\gcd(200,60,70)$（終於三個係數都不是 0）[▶ 23:15](https://youtu.be/BDf4V_l8e3E?t=1395)
- $\gcd(200,60) = 20 = 1\cdot200-3\cdot60$。
- $\gcd(20,70) = 10 = -3\cdot20+1\cdot70$。
- 代入：
$$10 = -3\,(200-3\cdot60)+70 = -3\cdot200+9\cdot60+1\cdot70.$$
檢查：$-600+540+70=10$。✓（最後展開是依講者的代入補完的。）

【口頭】gcd 不管數的順序，可以利用這點簡化：**只要其中兩個數互質，gcd 就是 1**。講者說他有一題故意把順序弄得更難——例如 $\gcd(30,7,10)$，直接看 $\gcd(30,7)=1$ 就知道答案是 1 [▶ 24:21](https://youtu.be/BDf4V_l8e3E?t=1461)。

---

## 4. 哪些數能寫成 ax+by

[▶ 26:07](https://youtu.be/BDf4V_l8e3E?t=1567)

**定理**：$a,b$ 不全為 0，$d=\gcd(a,b)$。則
$$c = ax+by \text{ 對某些整數 } x,y \iff d\mid c.$$
而且 $d$ 是 $ax+by$ 能取到的**最小正值**。

**證明**：
- (⇒) $d\mid a$、$d\mid b$，所以 $d\mid ax+by=c$。
- (⇐) 設 $c = ld$。由 Bézout，$d = au+bv$。乘上 $l$：
$$c = ld = a(lu)+b(lv),$$
取 $x=lu$、$y=lv$。∎
- 最小正值：能寫成 $ax+by$ 的數恰好是 $d$ 的倍數，最小的正倍數是 $d$ 本身。

---

## 5. 互質及其推論

### 5.1 定義

[▶ 28:22](https://youtu.be/BDf4V_l8e3E?t=1702)

- $a,b$ **互質**（relatively prime / coprime）：$\gcd(a,b)=1$。
- $a_1,\dots,a_n$ **互質**：$\gcd(a_1,\dots,a_n)=1$。
- $a_1,\dots,a_n$ **兩兩互質**（mutually coprime）：對所有 $i\neq j$，$\gcd(a_i,a_j)=1$。

兩兩互質 ⇒ 互質，**反過來不對** [▶ 28:54](https://youtu.be/BDf4V_l8e3E?t=1734)：
$6,10,15$ 互質（$\gcd=1$），但 $\gcd(6,10)=2$、$\gcd(6,15)=3$、$\gcd(10,15)=5$，沒有一對互質。

### 5.2 推論 1

[▶ 29:29](https://youtu.be/BDf4V_l8e3E?t=1769)

**推論 1**：$a,b$ 互質 $\iff$ 存在整數 $x,y$ 使 $ax+by=1$。

**證明**：(⇒) Bézout。(⇐) 由第 4 節定理，$\gcd(a,b)\mid1$；正的 1 的因數只有 1。∎

【口頭】講者證明互質的東西時，**第一個想到的就是寫出 $ax+by=1$** [▶ 29:29](https://youtu.be/BDf4V_l8e3E?t=1769)。

### 5.3 推論 2

[▶ 30:36](https://youtu.be/BDf4V_l8e3E?t=1836)

**推論 2**：若 $\gcd(a,b)=d$，則
1. 對每個正整數 $m$，$\gcd(ma,mb) = md$；
2. $\gcd\!\left(\dfrac ad,\dfrac bd\right) = 1$。

**證明**：
1. $\gcd(ma,mb)$ 是 $max+mby = m(ax+by)$ 的最小正值；$ax+by$ 的最小正值是 $d$，所以答案是 $md$。（講者：不喜歡這證法可以用別的。）
2. $d\mid a$、$d\mid b$，所以 $a/d$、$b/d$ 是整數。$d = ax+by$ 兩邊除以 $d$：
$$1 = \frac ad\,x+\frac bd\,y.$$
由推論 1，$a/d$ 和 $b/d$ 互質。∎

⚠️ 逐字稿缺字：[▶ 32:18](https://youtu.be/BDf4V_l8e3E?t=1938) 字幕寫「1 is equal to d over a」，講者馬上改口為 $a/d$。

**例** [▶ 32:52](https://youtu.be/BDf4V_l8e3E?t=1972)：$\gcd(780,637)=13$；$780/13=60$、$637/13=49$，而 $\gcd(60,49)=1$。

### 5.4 推論 3

**為什麼需要互質** [▶ 33:24](https://youtu.be/BDf4V_l8e3E?t=2004)：
- 問題 1：$a\mid c$、$b\mid c$ ⇒ $ab\mid c$？**不一定**：$9\mid27$、$9\mid27$，但 $81\nmid27$。
- 問題 2：$a\mid bc$ ⇒ $a\mid c$？**不一定**：$10\mid100 = 50\cdot2$，但 $10\nmid2$。
- 但 $3\mid42$、$7\mid42$ ⇒ $21\mid42$ 成立；$5\mid70=7\cdot10$ ⇒ $5\mid10$ 成立。這兩組 $(3,7)$、$(5,7)$ 都互質。

**推論 3** [▶ 35:36](https://youtu.be/BDf4V_l8e3E?t=2136)：設 $a,b$ 互質。
1. 若 $a\mid c$ 且 $b\mid c$，則 $ab\mid c$。
2. 若 $a\mid bc$，則 $a\mid c$。

【口頭】直覺：$a$ 和 $b$ 沒有共同的部分，所以 $a$ 只能整除 $c$ [▶ 36:08](https://youtu.be/BDf4V_l8e3E?t=2168)。

**證明**：由 Bézout，$ax+by=1$。兩邊乘 $c$：
$$c = cax+cby.$$
1. $c = kb$、$c=ja$。在第一項把 $c$ 換成 $kb$、第二項把 $c$ 換成 $ja$：
$$c = (kb)ax + (ja)by = ab\,(kx+jy).$$
所以 $ab\mid c$。
2. $bc = ja$。第二項 $cby = (bc)y = jay$：
$$c = a(cx) + a(jy) = a\,(cx+jy).$$
所以 $a\mid c$。∎

【口頭】這些之後分析質數時會用到 [▶ 37:46](https://youtu.be/BDf4V_l8e3E?t=2266)。

> 【課本補充】推論 1、2、3 分別是課本 Corollary 1.9、1.10、1.11（p. 10–11）。課本證 1.11(b) 更短：$a\mid bc$ 且 $a\mid a$，所以 $a$ 整除線性組合 $cax+cby=c$。

---

## 6. 最小公倍數

### 6.1 定義

[▶ 38:19](https://youtu.be/BDf4V_l8e3E?t=2299)

**定義**：$a,b$ 不全為 0。**最小公倍數**（least common multiple）$l=\mathrm{lcm}(a,b)$ 是滿足下面兩條的自然數：
1. $a\mid l$ 且 $b\mid l$（是公倍數）；
2. 若 $c>0$、$a\mid c$、$b\mid c$，則 $c\ge l$。

> 【課本補充】§1.3（p. 12）要求 $a,b$ **都不為 0**（才有正的公倍數，例如 $|ab|$），由良序原理得最小正公倍數。也寫作 $[a,b]$。

### 6.2 定理：$\gcd\cdot\mathrm{lcm}=ab$

[▶ 38:53](https://youtu.be/BDf4V_l8e3E?t=2333)

**定理**：$a,b$ 正整數，$d=\gcd(a,b)$、$l=\mathrm{lcm}(a,b)$。則
$$dl = ab.$$

**證明**：寫 $a = dj$、$b=dk$（$j=a/d$、$k=b/d$ 是正整數）。則
$$\frac{ab}{d} = \frac{dj\cdot dk}{d} = djk.$$
證明 $djk$ 就是 $l$：
1. **是公倍數**：$djk = (dj)k = ak$，$djk = (dk)j = bj$。
2. **最小**：設 $c>0$ 是公倍數，$c = ma = nb$。由 Bézout，$d=ax+by$。看比值：
$$\frac{c}{djk} = \frac{cd}{dj\cdot dk} = \frac{cd}{ab} = \frac{c(ax+by)}{ab} = \frac cb\,x + \frac ca\,y = nx+my.$$
右邊是整數，左邊是正數，所以 $c = (nx+my)\,djk$，其中 $nx+my\ge1$，於是 $c\ge djk$。∎

【口頭】比較兩數大小時，看它們的**比值**常常有用 [▶ 41:02](https://youtu.be/BDf4V_l8e3E?t=2462)。

⚠️ 逐字稿缺字：[▶ 41:37](https://youtu.be/BDf4V_l8e3E?t=2497) 字幕「c is also equal to mb and nbm」說得含糊（還開了一個「mummy」的玩笑）；筆記照 $c=ma=nb$ 寫，所以 $c/b=n$、$c/a=m$。

**例** [▶ 42:43](https://youtu.be/BDf4V_l8e3E?t=2563)：
- $\mathrm{lcm}(780,637) = \dfrac{780\cdot637}{13} = 780\cdot49 = 38220$。小學的看法：$780=13\cdot60$、$637=13\cdot49$，共同的 13 只要一份，所以 $13\cdot60\cdot49$。
- $\gcd(20,110)=10$，$\mathrm{lcm}(20,110) = \dfrac{20\cdot110}{10} = 220$。

⚠️ 逐字稿缺字：字幕「30 38 220」應為 38220。

【口頭】小時候用質因數分解（因數樹）算 lcm，但**分解大數很難**；這個定理讓你只要用輾轉相除法算 gcd 就能得到 lcm [▶ 43:53](https://youtu.be/BDf4V_l8e3E?t=2633)。

---

## 7. 線性丟番圖方程

### 7.1 定理

[▶ 44:25](https://youtu.be/BDf4V_l8e3E?t=2665)

【口頭】本集暗號是「calculator」。丟番圖（Diophantus of Alexandria）約西元 300 年研究這些；西元 628 年印度也有很多相關成果。

**問題**：求 $ax+by=c$ 的整數解。

**定理**：$a,b$ 不全為 0，$d=\gcd(a,b)$。
- 若 $d\nmid c$，**無解**。
- 若 $d\mid c$，有無窮多解，全部是
$$x = x_0 + \frac{b}{d}\,n,\qquad y = y_0 - \frac ad\,n,\qquad n\in\mathbb{Z},$$
其中 $(x_0,y_0)$ 是任意一組特解。

> 【課本補充】Theorem 1.13（p. 13–14）：這結果約西元 628 年印度數學家 Brahmagupta 就知道了。課本也說 Diophantos 是 3 世紀的人。

**證明** [▶ 46:04](https://youtu.be/BDf4V_l8e3E?t=2764)
1. **有解 ⇔ $d\mid c$**：就是第 4 節的定理。
2. **找特解**：由 Bézout，$au+bv=d$。$c = dj$，乘 $j$：$a(ju)+b(jv) = c$，所以 $x_0=ju$、$y_0=jv$。（實際算題也是這樣：向量輾轉相除得 $d$ 的組合，再乘上倍數。）
3. **每個解都長這樣**：設 $(x,y)$ 是任一解。$ax+by = c = ax_0+by_0$，所以
$$a(x-x_0) = -b(y-y_0).$$
兩邊除以 $d$：
$$\frac ad\,(x-x_0) = -\frac bd\,(y-y_0). \tag{$*$}$$
設 $b\neq0$。$b/d$ 整除右邊，所以整除左邊。由推論 2，$\gcd(a/d,b/d)=1$；由推論 3(2)，$\dfrac bd\mid x-x_0$。所以存在整數 $n$ 使
$$x = x_0 + \frac bd\,n.$$
代回 $(*)$：$\dfrac ad\cdot\dfrac bd\,n = -\dfrac bd(y-y_0)$，兩邊除以 $b/d$ 得 $y = y_0 - \dfrac ad\,n$。∎

【口頭】講者說這個證明他以前覺得很神秘，但一路學到這裡就很好懂 [▶ 49:55](https://youtu.be/BDf4V_l8e3E?t=2995)。

> 【課本補充】課本還驗證了反方向：這些 $(x,y)$ 確實都是解，因為 $a\left(x_0+\tfrac{bn}{d}\right)+b\left(y_0-\tfrac{an}{d}\right) = ax_0+by_0 = c$。課本並把解法整理成四步：(1) 算 $d$；(2) 檢查 $d\mid c$，寫 $c=de$；(3) 用 Bézout 得 $au+bv=d$，特解 $x_0=ue$、$y_0=ve$；(4) 套通解公式（p. 15）。幾何意義：直線 $ax+by=c$ 經過整數格點 ⇔ $d\mid c$。

### 7.2 例子

**例**：$10x+2y=4$ [▶ 50:29](https://youtu.be/BDf4V_l8e3E?t=3029)
- $\gcd(10,2)=2$，$2\mid4$，有解。
- 猜一組：$x_0=2$、$y_0=-8$（$20-16=4$）。
- 通解：$x = 2+\tfrac22n = 2+n$，$y = -8-\tfrac{10}2n = -8-5n$。
- 檢查：$10(2+n)+2(-8-5n) = 20-16+10n-10n = 4$。✓

**例**：$3x+8y=13$ [▶ 52:11](https://youtu.be/BDf4V_l8e3E?t=3131)

3 和 8 互質，所以一定有解。這次不用猜，用向量輾轉相除。

【口頭】講者把 8 放第一列，標成 $b$、3 標成 $a$（「$ba$」），讓字母和定理裡 $x,y$ 的係數一致；原本寫成 $ab$ 搞混了，所以板書有修正液 [▶ 52:48](https://youtu.be/BDf4V_l8e3E?t=3168)。

| 數 | 組合 |
|---|---|
| 8 | $b$ |
| 3 | $a$ |
| 2 | $b-2a$ |
| 1 | $a-(b-2a) = 3a-b$ |

所以 $3\cdot3+8\cdot(-1) = 1$。乘 13：$3\cdot39+8\cdot(-13) = 13$，特解 $x_0=39$、$y_0=-13$。$d=1$，通解：
$$x = 39+8n,\qquad y = -13-3n.$$

**例**：$3x+6y=11$ [▶ 55:02](https://youtu.be/BDf4V_l8e3E?t=3302)
- $\gcd(3,6)=3$，$3\nmid11$，**沒有整數解**。
- 但有無窮多**有理數**解：$y = \dfrac{11-3x}{6}$，$x$ 取任何有理數。

【口頭】沒有解只是因為我們挑剔、只要整數。丟番圖方程要求很高：找整數解非常難，找有理數解稍微容易，找實數解更容易，找複數解輕而易舉 [▶ 56:41](https://youtu.be/BDf4V_l8e3E?t=3401)。下一集講多項式的輾轉相除法，用來把含立方根的分母有理化 [▶ 57:13](https://youtu.be/BDf4V_l8e3E?t=3433)。

---

## 8. 一頁速查表

**向量輾轉相除法**：每列記「數」和「$xa+yb$」。新列 = 上上列 $- q\times$ 上列，兩欄同做。最後非零餘數那列的係數就是 Bézout 係數。
- $1 = 108\cdot1960-857\cdot247$；$2 = 8\cdot100-19\cdot42$；$1 = -2\cdot42+5\cdot17$。

**Bézout**：$\gcd(a,b)=ax+by$。$\{ax+by\}$ = $d$ 的所有倍數；$d$ 是最小正值。
- 關鍵：$d\mid c$ ⇒ $c=ld=a(lu)+b(lv)$。

**gcd 的性質**
- $c\mid a,b \iff c\mid\gcd(a,b)$（關鍵：$c\mid ax+by$）。
- $\gcd(a,b,c)=\gcd(\gcd(a,b),c)$；延伸 Bézout 逐對代入。
- $\gcd(ma,mb)=m\gcd(a,b)$；$\gcd(a/d,b/d)=1$（關鍵：$1=\frac adx+\frac bdy$）。

**互質**：$\gcd(a,b)=1 \iff ax+by=1$。兩兩互質 ⇒ 互質，反之不然（6, 10, 15）。
- $a,b$ 互質：$a\mid c,b\mid c\Rightarrow ab\mid c$；$a\mid bc\Rightarrow a\mid c$。關鍵：$c = cax+cby$。

**lcm**：$\gcd(a,b)\cdot\mathrm{lcm}(a,b)=ab$。
- 關鍵：$\dfrac{c}{ab/d} = \dfrac{c(ax+by)}{ab} = \dfrac cbx+\dfrac cay\in\mathbb{Z}$。

**線性丟番圖方程** $ax+by=c$
- 有解 $\iff d\mid c$。
- 通解 $x=x_0+\frac bdn$，$y=y_0-\frac adn$。關鍵：$\frac ad(x-x_0)=-\frac bd(y-y_0)$，$\frac bd$ 與 $\frac ad$ 互質。
- 特解：向量輾轉相除得 $au+bv=d$，乘 $c/d$。
- $3x+8y=13$：$x=39+8n$，$y=-13-3n$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 輾轉相除法、Bézout | 第 6 集（多項式版本、分母有理化） |
| $a\mid bc$、互質 ⇒ $a\mid c$ | 第 7 集（質數版本 $p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$，算術基本定理唯一性） |
| 線性丟番圖方程 | 第 10–11 集（線性同餘 $ax\equiv b\ (\mathrm{mod}\ n)$） |
| 互質、$ab\mid c$ | 第 12 集（中國剩餘定理） |
| Bézout 求反元素 | 第 14–16 集（單位群、RSA 解密指數） |

---

## 附：本集一句話總結

> **向量輾轉相除法邊算 gcd 邊記錄係數，直接給出 Bézout 等式 $\gcd(a,b)=ax+by$；由此得到「$ax+by$ 恰好是 gcd 的倍數」、互質的判準 $ax+by=1$、$\gcd\cdot\mathrm{lcm}=ab$，以及線性丟番圖方程 $ax+by=c$ 的完整解：$d\mid c$ 才有解，通解是 $x_0+\frac bdn$、$y_0-\frac adn$。**

---

## ⚠️ 待確認清單

1. [▶ 24:21](https://youtu.be/BDf4V_l8e3E?t=1461) 講者說「我把題目弄得更難」的那個三數 gcd 例子，字幕只聽到「gcd of 37 and 10」和「gcd 30 and 7 is clearly one」，筆記推測是 $\gcd(30,7,10)$，待確認。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 5 錄影逐字稿（YouTube 自動字幕，57:34）與 Jones & Jones《Elementary Number Theory》§1.2–1.4 整理。*
