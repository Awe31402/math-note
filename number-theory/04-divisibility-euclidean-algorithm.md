---
course: Number Theory（2021 秋，線上錄影）
episode: 4
lecture: Lecture 4
date: 待補（2021 秋）
video: https://youtu.be/cQABm2t4Paw
notes: Jones & Jones §1.1（書頁 1–7，PDF 頁 16–22）：Theorem 1.1、Corollary 1.2、Example 1.2、Exercise 1.3、Theorem 1.3、Corollary 1.4、Lemma 1.5、Theorem 1.6
---

# 第 4 集 · Lecture 4：整除與輾轉相除法（Divisibility and the Euclidean Algorithm） [▶ 影片](https://youtu.be/cQABm2t4Paw)

← 上一集：[03-binomial-theorem](03-binomial-theorem.md) ｜ [總目錄](README.md) ｜ 下一集：[05-bezout-gcd-lcm-diophantine](05-bezout-gcd-lcm-diophantine.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 4 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（40:48，自動字幕）＋ Jones & Jones §1.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 數線上的直覺](#1-數線上的直覺)
- [2. 用計算機找商和餘數](#2-用計算機找商和餘數)
- [3. 除法演算法](#3-除法演算法)
- [4. 應用：平方數除以 4](#4-應用平方數除以-4)
- [5. 整除](#5-整除)
- [6. 最大公因數](#6-最大公因數)
- [7. 輾轉相除法](#7-輾轉相除法)
- [8. 例子與反推（Bézout 預告）](#8-例子與反推bézout-預告)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】講者說：本集大部分取自 Jones & Jones，但講義寫得自成一體，沒有課本也看得懂 [▶ 12:41](https://youtu.be/cQABm2t4Paw?t=761)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1–3 | 除法演算法（存在、唯一） | §1.1 Theorem 1.1、Corollary 1.2 |
| 4 | 平方數除以 4 餘 0 或 1 | Example 1.2 |
| 5 | 整除的定義與性質 | Exercise 1.3、Theorem 1.3、Corollary 1.4 |
| 6 | gcd 的定義 | §1.1 定義 |
| 7–8 | 輾轉相除法；反推出 Bézout | Lemma 1.5、Theorem 1.6、Example 1.3–1.4 |

---

## 1. 數線上的直覺

[▶ 00:00](https://youtu.be/cQABm2t4Paw?t=0)

給整數 $a$ 和 $b>0$。在數線上，$a$ 一定夾在 $b$ 的兩個**相鄰**倍數之間：
$$q_-b \le a \le q_+b,\qquad q_+ = q_-+1.$$
兩個相鄰倍數相距 $b$，所以 $a$ 離兩端都不超過 $b$。令
$$r_\pm = a - q_\pm b,$$
則 $a = q_\pm b + r_\pm$，且 $|r_\pm| < b$（講者的說法）。

**例**：$a=50$、$b=11$ [▶ 01:36](https://youtu.be/cQABm2t4Paw?t=96)。$50$ 夾在 $44=4\cdot11$ 和 $55=5\cdot11$ 之間：
- $r_+ = 50-55 = -5$
- $r_- = 50-44 = 6$

---

## 2. 用計算機找商和餘數

[▶ 02:44](https://youtu.be/cQABm2t4Paw?t=164)

如果看不出 $a$ 夾在哪兩個倍數之間，就用計算機算 $a/b$ 的小數：

- **地板函數**（floor）$\lfloor x\rfloor$：$\le x$ 的最大整數。
- **天花板函數**（ceiling）$\lceil x\rceil$：$\ge x$ 的最小整數。

$50/11 = 4.5454\ldots$，所以 $\lfloor 50/11\rfloor = 4$、$\lceil 50/11\rceil=5$，這就是為什麼取 $4\cdot11$ 和 $5\cdot11$。

**例**：$a=53672$、$b=68$ [▶ 03:53](https://youtu.be/cQABm2t4Paw?t=233)
- $a/b = 789.294176\ldots$，所以 $q = 789$。
- $r = 53672 - 789\cdot68 = 53672-53652 = 20$。
- 所以 $53672 = 789\cdot68+20$。

⚠️ 逐字稿缺字：字幕有一處寫「553 672」，應為 53672。

【口頭】用地板函數當商，餘數就是非負的；用天花板函數當商，餘數就是非正的。傳統上要餘數為正，所以用地板——但這只是一種**習慣上的選擇** [▶ 05:00](https://youtu.be/cQABm2t4Paw?t=300)。

---

## 3. 除法演算法

### 3.1 敘述

[▶ 06:05](https://youtu.be/cQABm2t4Paw?t=365)

**定理（除法演算法，division algorithm）**：若 $a,b$ 是整數、$b>0$，則存在**唯一**一對整數 $q,r$ 使
$$a = qb + r,\qquad 0\le r<b.$$
$q$ 叫**商**（quotient），$r$ 叫**餘數**（remainder）。

【口頭】名字很怪：這其實是**存在性定理**，沒有給演算法。真正的演算法是上一節那個：算 $a/b$、取地板得 $q$、再算 $r=a-qb$。不過大家都叫它演算法，我們也跟著叫 [▶ 06:37](https://youtu.be/cQABm2t4Paw?t=397)。

> 【課本補充】課本 Theorem 1.1（p. 2）相同，並指出 $\dfrac ab = q + \dfrac rb$、$0\le\dfrac rb<1$，所以 $q = \lfloor a/b\rfloor$。例：$9 = 2\cdot4+1$；$-9 = (-3)\cdot4+3$（負數的餘數也要非負）。

### 3.2 證明

**存在** [▶ 07:10](https://youtu.be/cQABm2t4Paw?t=430)：令
$$S = \{\,a - nb : n\in\mathbb{Z}\,\}\cap\mathbb{N}_0$$
（$a$ 減去 $b$ 的倍數中，非負的那些）。

1. $S$ 非空：講者分 $a<0$ 和 $a\ge0$ 兩種情況各找一個元素。（課本的做法：取 $n=-|a|$，則 $a-nb = a+|a|b \ge a+|a|\ge0$。）
2. 由**良序原理**（第 2 集），$S$ 有最小元素，記作 $r = a-qb$。於是 $a = qb+r$，$r\ge0$。
3. 證 $r<b$（反證）：若 $r\ge b$，則
$$a-(q+1)b = r-b \ge 0,$$
所以 $r-b\in S$，但 $r-b<r$，和「$r$ 最小」矛盾。所以 $0\le r<b$。

**唯一** [▶ 09:23](https://youtu.be/cQABm2t4Paw?t=563)：設 $a = qb+r = q'b+r'$，$0\le r,r'<b$。相減：
$$r - r' = (q'-q)\,b.$$
- 若 $q'=q$，則 $r=r'$，完成。
- 若 $q'\neq q$，則 $|q'-q|\ge1$，所以 $|r-r'|\ge b$。但 $r,r'$ 都在 $[0,b)$ 裡，距離不可能 $\ge b$。矛盾。

所以 $q=q'$、$r=r'$。∎

### 3.3 推論：$b$ 可以是負數

[▶ 11:35](https://youtu.be/cQABm2t4Paw?t=695)

**推論**：若 $a,b$ 是整數、$b\neq0$，則存在唯一一對整數 $q,r$ 使
$$a = qb+r,\qquad 0\le r<|b|.$$

**證明**：$b>0$ 時 $|b|=b$，就是定理。設 $b<0$，則 $-b>0$，由定理有 $q',r'$ 使
$$a = q'(-b) + r',\qquad 0\le r'<-b.$$
令 $q=-q'$、$r=r'$，則 $a = qb+r$，且 $0\le r<-b = |b|$。∎

⚠️ 逐字稿缺字：字幕把餘數條件唸成「zero less than r」，應為 $0\le r$（$r=0$ 允許）。

> 【課本補充】Corollary 1.2（p. 3）補充：$b<0$ 時 $q = \lceil a/b\rceil$。

---

## 4. 應用：平方數除以 4

[▶ 13:13](https://youtu.be/cQABm2t4Paw?t=793)

（取自 Jones & Jones Example 1.2，p. 3。）

**定義**：若 $n=a^2$（$a$ 是整數），$n$ 叫**平方數**（square）。

**命題**：平方數除以 4，餘數是 0 或 1。

**證明**：由除法演算法，$a = 4q+r$，$r\in\{0,1,2,3\}$。於是
$$n = a^2 = (4q+r)^2 = 16q^2 + 8qr + r^2.$$
逐一代入：

| $r$ | $n$ | 餘數 |
|---|---|---|
| 0 | $4(4q^2)+0$ | 0 |
| 1 | $4(4q^2+2q)+1$ | 1 |
| 2 | $4(4q^2+4q+1)+0$ | 0 |
| 3 | $4(4q^2+6q+2)+1$ | 1 |

（例：$r=3$ 時 $16q^2+24q+9 = 4(4q^2+6q+2)+1$。）

因為除法演算法的**唯一性**，可以確定餘數就是 0 或 1。∎

【口頭】之後學了同餘（mod 4），會有更漂亮的論證取代這種寫法 [▶ 14:54](https://youtu.be/cQABm2t4Paw?t=894)。

> 【課本補充】Exercise 1.1 提示更短的證法：用 $b=2$，$a=2q$ 或 $2q+1$；Exercise 1.2 問平方數除以 3、5、6 的可能餘數（本集沒講）。

---

## 5. 整除

### 5.1 定義

[▶ 15:59](https://youtu.be/cQABm2t4Paw?t=959)

【口頭】除法演算法其實不是演算法；接下來的**輾轉相除法**才是貨真價實的演算法。先講整除。

**定義**：若 $a,b$ 是整數，且存在整數 $q$ 使 $a=qb$，就說 **$b$ 整除 $a$**（$b$ divides $a$），寫作 $b\mid a$。也說 $a$ 是 $b$ 的**倍數**（multiple）。不存在這樣的 $q$ 時寫 $b\nmid a$。

【口頭】注意：
- $b\mid a$ 是一個**敘述**（對或錯），不是分數 $b/a$ [▶ 16:32](https://youtu.be/cQABm2t4Paw?t=992)。
- 若 $b\mid a$（$b\neq0$），則 $a/b$ 真的是整數（就是那個 $q$）。這下一兩堂會用到好幾次。
- 每個 $b$ 都整除 $0$（$0 = 0\cdot b$），所以有些敘述要排除 0。

### 5.2 性質

[▶ 17:35](https://youtu.be/cQABm2t4Paw?t=1055)

| # | 性質 | 例子 |
|---|---|---|
| 1 | $a\mid b$ 且 $b\mid c$ $\Rightarrow$ $a\mid c$ | $3\mid9$、$9\mid45$ ⇒ $3\mid45$ |
| 2 | $a\mid b$ 且 $c\mid d$ $\Rightarrow$ $ac\mid bd$ | $7\mid14$、$4\mid20$ ⇒ $28\mid280$ |
| 3 | $m\neq0$：$a\mid b \iff ma\mid mb$ | |
| 4 | $d\mid a$ 且 $a\neq0$ $\Rightarrow$ $\lvert d\rvert\le\lvert a\rvert$（等號在 $d=\pm a$） | $13\mid169$，$13\le169$ |
| 5 | $c\mid a_1,\dots,a_k$ $\Rightarrow$ $c\mid a_1u_1+\cdots+a_ku_k$（任意整數 $u_i$） | |
| 6 | $a\mid b$ 且 $b\mid a$ $\iff$ $a=\pm b$ | |
| 7 | $c\mid a$ 且 $c\mid b$ $\Rightarrow$ $c\mid au+bv$（任意整數 $u,v$） | 5 的 $k=2$ 特例，最常用 |

【口頭】
- 性質 6：講者有一次叫學生證「$a=b$」，學生說證不出來，要有負號——他很高興 [▶ 19:51](https://youtu.be/cQABm2t4Paw?t=1191)。
- 大部分性質留作作業和考題，只證性質 1。

**證明性質 1** [▶ 20:24](https://youtu.be/cQABm2t4Paw?t=1224)：$a\mid b$、$b\mid c$，所以存在整數 $j,k$ 使 $b = aj$、$c=bk$。代入：
$$c = bk = (aj)k = a(jk).$$
$jk$ 是整數，所以 $a\mid c$。∎

【口頭】性質 6 的證明不太一樣，最後歸結到在整數裡解「某數的平方 = 1」或類似的方程，只有 $\pm1$ [▶ 21:28](https://youtu.be/cQABm2t4Paw?t=1288)。

> 【課本補充】課本把性質 1–4 放在 Exercise 1.3、性質 5–6 放在 Theorem 1.3、性質 7 放在 Corollary 1.4（p. 4–5），並證了 Theorem 1.3：
> - **(a)（性質 5）**：$a_i = q_ic$，所以 $\sum a_iu_i = \left(\sum q_iu_i\right)c$，括號內是整數。
> - **(b)（性質 6）**：若 $a=\pm b$ 顯然。反過來，$b=qa$、$a=q'b$。若 $b=0$ 則 $a=0$。若 $b\neq0$，消去 $a$ 得 $b=qq'b$，約掉 $b$ 得 $qq'=1$，由性質 4 得 $q,q'=\pm1$，所以 $a=\pm b$。

---

## 6. 最大公因數

[▶ 22:01](https://youtu.be/cQABm2t4Paw?t=1321)

**定義**：若 $d\mid a$ 且 $d\mid b$，$d$ 叫 $a,b$ 的**公因數**（common divisor）。對**不全為 0** 的 $a,b$，**最大公因數**（greatest common divisor）$d=\gcd(a,b)$ 是滿足下面兩條的整數：
1. $d\mid a$ 且 $d\mid b$（是公因數）；
2. 若 $c\mid a$ 且 $c\mid b$，則 $c\le d$（沒有公因數比它大）。

【口頭】
- 講者常用字母 $d$ 表示 gcd，但這不是通用規定。
- 板書第 2 條一開始寫錯（寫成 $c\mid$ 別的東西），講者當場改成 $c\mid a$ [▶ 23:06](https://youtu.be/cQABm2t4Paw?t=1386)。
- **為什麼不能全為 0**：每個整數都整除 0，若 $a=b=0$ 就沒有最大的公因數。不全為 0 時，由性質 4，公因數的大小有上界，所以最大公因數存在 [▶ 23:40](https://youtu.be/cQABm2t4Paw?t=1420)。

**小學的做法**：$\gcd(-12,20)$ [▶ 24:14](https://youtu.be/cQABm2t4Paw?t=1454)
- 12 的正因數：$1,2,3,4,6,12$
- 20 的正因數：$1,2,4,5,10,20$
- 公因數：$1,2,4$，最大是 $4$。所以 $\gcd(-12,20)=4$。

【口頭】數字大的時候，要列出所有因數就很麻煩。所以需要更好的方法——輾轉相除法，「從前人那裡偷來的」，最早可追溯到古希臘的 Euclid [▶ 24:47](https://youtu.be/cQABm2t4Paw?t=1487)。

> 【課本補充】§1.1（p. 5）：上界具體是 $\max(|a|,|b|)$；只要列**正**因數就夠。gcd 也寫作 $(a,b)$。Euclid 演算法出自約西元前 300 年《幾何原本》第 VII 卷。

---

## 7. 輾轉相除法

### 7.1 關鍵引理

[▶ 25:19](https://youtu.be/cQABm2t4Paw?t=1519)

**引理**：若 $a = qb + r$，則
$$\gcd(a,b) = \gcd(b,r).$$

**證明**：證明兩對數 $\{a,b\}$ 和 $\{b,r\}$ 的**公因數完全一樣**。
- 若 $d\mid a$、$d\mid b$：因為 $r = a - qb$，由性質 7，$d\mid r$。所以 $d$ 是 $b,r$ 的公因數。
- 若 $d\mid b$、$d\mid r$：因為 $a = qb+r$，由性質 7，$d\mid a$。所以 $d$ 是 $a,b$ 的公因數。

公因數一樣，最大的那個也一樣。∎

### 7.2 演算法

[▶ 27:40](https://youtu.be/cQABm2t4Paw?t=1660)

**在解什麼**：給兩個整數 $a,b$（不全為 0），求 $\gcd(a,b)$，不用列因數。

**步驟**（講者習慣讓 $a$ 是絕對值較大的那個）：反覆用除法演算法，每次「除數變被除數、餘數變除數」：
$$\begin{aligned}
a &= q_1b + r_1, & 0&<r_1<b\\
b &= q_2r_1 + r_2, & 0&<r_2<r_1\\
r_1 &= q_3r_2 + r_3, & 0&<r_3<r_2\\
&\ \ \vdots\\
r_{n-2} &= q_nr_{n-1} + 0.
\end{aligned}$$

**為什麼會停** [▶ 28:46](https://youtu.be/cQABm2t4Paw?t=1726)：
$$b > r_1 > r_2 > r_3 > \cdots \ge 0$$
是嚴格遞減的非負整數，不能一直減下去，所以某一步餘數一定是 0。

**結論**：$\gcd(a,b)$ = **最後一個非零餘數** $r_{n-1}$。

**為什麼**：由 7.1 引理一路傳下去，
$$\gcd(a,b) = \gcd(b,r_1) = \gcd(r_1,r_2) = \cdots = \gcd(r_{n-2},r_{n-1}) = r_{n-1},$$
最後一步是因為 $r_{n-1}\mid r_{n-2}$。

> 【課本補充】Theorem 1.6（p. 6）就是這個證明。課本還先化簡：$a=0$ 時 $d=|b|$；$\gcd(\pm a,\pm b)=\gcd(a,b)$，所以可設 $a>b>0$；最多 $b$ 步就會停。另外，看出某兩個相鄰餘數的 gcd 時就可以提早停（p. 7）。

---

## 8. 例子與反推（Bézout 預告）

### 8.1 $\gcd(20,12)$

[▶ 29:51](https://youtu.be/cQABm2t4Paw?t=1791)
$$\begin{aligned}
20 &= 1\cdot12 + 8\\
12 &= 1\cdot8 + 4\\
8 &= 2\cdot4 + 0
\end{aligned}$$
最後非零餘數是 $4$，所以 $\gcd(20,12)=4$。

【口頭】「$20 = 12\cdot1+8$」其實就是小學的 $\dfrac{20}{12} = 1\tfrac{8}{12}$，兩邊乘 12 而已，寫法看起來怪而已 [▶ 30:26](https://youtu.be/cQABm2t4Paw?t=1826)。這題用輾轉相除沒比較快，下一題才看得出好處。

### 8.2 $\gcd(1960, 247)$

[▶ 32:06](https://youtu.be/cQABm2t4Paw?t=1926)

用計算機找第一個商：$1960/247 = 7.93\ldots$，取 $q=7$，$1960-7\cdot247 = 231$。
$$\begin{aligned}
1960 &= 7\cdot247 + 231\\
247 &= 1\cdot231 + 16\\
231 &= 14\cdot16 + 7\\
16 &= 2\cdot7 + 2\\
7 &= 3\cdot2 + 1\\
2 &= 2\cdot1 + 0
\end{aligned}$$
最後非零餘數是 $1$，所以 $\gcd(1960,247)=1$。

**定義** [▶ 34:57](https://youtu.be/cQABm2t4Paw?t=2097)：$\gcd(a,b)=1$ 時，說 $a,b$ **互質**（relatively prime，又叫 coprime，兩個詞同義）。

### 8.3 反推：把 gcd 寫成 $a,b$ 的組合

[▶ 35:30](https://youtu.be/cQABm2t4Paw?t=2130)

下一集要講 **Bézout 定理**：gcd 一定可以寫成 $a$ 和 $b$ 的整數線性組合。做法是把上面的計算**倒著代回去**（「最後的要成為第一」）：
$$\begin{aligned}
1 &= 7 - 3\cdot2\\
  &= 7 - 3\,(16-2\cdot7) = 7\cdot7 - 3\cdot16\\
  &= 7\,(231-14\cdot16) - 3\cdot16 = 7\cdot231 - 101\cdot16\\
  &= 7\cdot231 - 101\,(247-231) = 108\cdot231 - 101\cdot247\\
  &= 108\,(1960-7\cdot247) - 101\cdot247 = 108\cdot1960 - 857\cdot247.
\end{aligned}$$
所以
$$1960\cdot108 + 247\cdot(-857) = 1.$$
檢查：$211680 - 211679 = 1$。✓

（中間各行是依講者口述的代換順序補完整的；講者只唸出頭尾，說這個計算讓他「很頭痛」，用修正液改過好幾次。）

【口頭】
- 不必仔細理解這種倒推。下一集有更好的方法：**向量輾轉相除法** [▶ 37:12](https://youtu.be/cQABm2t4Paw?t=2232)。
- 講者示範他哥哥 Bill Cook（Appalachian State 教授）網站 billcookmath.com 上的 Sage 小工具「Euclidean algorithm for integers」，輸入兩數就列出整個計算 [▶ 38:24](https://youtu.be/cQABm2t4Paw?t=2304)。作業 PDF 裡有連結。
- 但考試要能**自己用計算機手算**；工具只拿來對答案 [▶ 39:29](https://youtu.be/cQABm2t4Paw?t=2369)。

> 【課本補充】Example 1.3–1.4（p. 7–8）另一個例子：$\gcd(1492,1066)$：
> $1492 = 1\cdot1066+426$，$1066 = 2\cdot426+214$，$426 = 1\cdot214+212$，$214 = 1\cdot212+2$，$212 = 106\cdot2+0$，所以 gcd $=2$；倒推得 $2 = -5\cdot1492 + 7\cdot1066$。

---

## 9. 一頁速查表

**除法演算法**：$b\neq0$ ⇒ 唯一 $q,r$ 使 $a=qb+r$，$0\le r<|b|$。
- 存在：$S=\{a-nb\}\cap\mathbb{N}_0$ 的最小元素 $r$；若 $r\ge b$ 則 $r-b\in S$ 更小，矛盾。
- 唯一：$r-r'=(q'-q)b$，$q\neq q'$ 會使 $|r-r'|\ge b$，矛盾。
- 計算：$b>0$ 時 $q=\lfloor a/b\rfloor$，$r=a-qb$。

**平方數 mod 4**：$a=4q+r$ ⇒ $a^2 = 16q^2+8qr+r^2$，餘數只有 0、1。

**整除**：$b\mid a \iff a=qb$（$q\in\mathbb{Z}$）。
- 遞移：$b=aj$、$c=bk$ ⇒ $c=a(jk)$。
- 線性組合：$c\mid a$、$c\mid b$ ⇒ $c\mid au+bv$。
- $a\mid b$、$b\mid a$ ⇔ $a=\pm b$（關鍵：$qq'=1$ ⇒ $q=\pm1$）。
- $d\mid a\neq0$ ⇒ $|d|\le|a|$。

**gcd**：不全為 0；(1) 公因數，(2) 任何公因數 $\le d$。互質：$\gcd=1$。

**輾轉相除法**
- 引理：$a=qb+r$ ⇒ $\gcd(a,b)=\gcd(b,r)$。關鍵：兩對數的公因數相同（$r=a-qb$、$a=qb+r$）。
- 反覆除，餘數嚴格遞減必停；gcd = 最後非零餘數。
- 例：$\gcd(1960,247)=1$，$1960\cdot108-247\cdot857=1$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 反推得 $\gcd = au+bv$ | 第 5 集（向量輾轉相除法、Bézout 定理） |
| gcd、互質 | 第 5 集（lcm、線性丟番圖方程）、第 7 集（算術基本定理） |
| 輾轉相除法 | 第 6 集（多項式版本） |
| 除法演算法、餘數 | 第 10 集（模運算） |
| 平方數 mod 4 | 第 10 集起用同餘改寫；第 21 集（平方和） |

---

## 附：本集一句話總結

> **除法演算法（其實是存在唯一性定理，用良序原理證）保證 $a=qb+r$、$0\le r<|b|$；因為 $\gcd(a,b)=\gcd(b,r)$，反覆做除法、餘數不斷變小，最後一個非零餘數就是 gcd——這就是輾轉相除法，而倒著代回去還能把 gcd 寫成 $au+bv$。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 4 錄影逐字稿（YouTube 自動字幕，40:48）與 Jones & Jones《Elementary Number Theory》§1.1 整理。*
