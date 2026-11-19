---
course: Number Theory（2021 秋，線上錄影）
episode: 3
lecture: 2021-08-18 第 1 部
date: 2021-08-18
video: https://youtu.be/qBrYneqX_vE
notes: Jones & Jones《Elementary Number Theory》§1.1（書頁 1–5，PDF 頁 16–20）：Theorem 1.1、Corollary 1.2、Exercise 1.3、Theorem 1.3、Corollary 1.4、gcd 定義、Lemma 1.5；§2.1 質數定義（書頁 19，PDF 頁 34）
---

# 第 3 集 · 整除、除法演算法（上）（Divisibility, Division Algorithm, Euclid's Algorithm, Part 1） [▶ 影片](https://youtu.be/qBrYneqX_vE)

← 上一集：[02-number-systems-properties-vs-construction](02-number-systems-properties-vs-construction.md) ｜ [總目錄](README.md) ｜ 下一集：[04-divisibility-euclid-algorithm-2](04-divisibility-euclid-algorithm-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 3 集（2021-08-18 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；結尾被切斷）＋ Jones & Jones《Elementary Number Theory》§1.1、§2.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 開場：數論的應用與兩則趣事](#1-開場數論的應用與兩則趣事)
- [2. 除法演算法](#2-除法演算法)
  - [2.1 從例子看起](#21-從例子看起)
  - [2.2 定理與存在性證明](#22-定理與存在性證明)
  - [2.3 唯一性（課堂跳過）](#23-唯一性課堂跳過)
  - [2.4 用 floor 算商：計算機做法](#24-用-floor-算商計算機做法)
  - [2.5 除數是負的：改用 ceiling](#25-除數是負的改用-ceiling)
- [3. 整除](#3-整除)
  - [3.1 定義：因數、倍數、質數](#31-定義因數倍數質數)
  - [3.2 整除的基本性質](#32-整除的基本性質)
  - [3.3 整除與整數線性組合](#33-整除與整數線性組合)
- [4. 最大公因數](#4-最大公因數)
  - [4.1 定義與存在](#41-定義與存在)
  - [4.2 小學的方法：質因數分解](#42-小學的方法質因數分解)
  - [4.3 關鍵引理 gcd(a,b) = gcd(b,r)](#43-關鍵引理-gcdab--gcdbr)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說今天的目標：整數、最大公因數、Euclid 演算法，以及一些關於質數的定理。實際上這部影片講到「$\gcd(a,b)=\gcd(b,r)$」就被切斷了，Euclid 演算法本身在第 4 集。

| 主題 | 時間 | 課本 |
|---|---|---|
| 數論的應用、趣事 | 00:41 | — |
| 除法演算法 | 06:13 | §1.1 Theorem 1.1、Corollary 1.2 |
| 整除、質數的定義 | 31:43 | §1.1 定義、§2.1 |
| 整除的性質 | 35:21 | Exercise 1.3、Theorem 1.3、Corollary 1.4 |
| 最大公因數 | 46:37 | §1.1 gcd 定義 |
| $\gcd(a,b)=\gcd(b,r)$ | 58:27 | Lemma 1.5 |

【口頭】[▶ 37:25](https://youtu.be/qBrYneqX_vE?t=1045) 講者說這一段他「部分照著 Jones & Jones《Elementary Number Theory》的精彩講法」。他差點拿這本當課本，上一位教這門課的老師就是用它。「是本扎實的小書，只是沒有 Stillwell 好玩。」

---

## 1. 開場：數論的應用與兩則趣事

[▶ 00:41](https://youtu.be/qBrYneqX_vE?t=41)

【口頭】作業：講者說前兩題「吠得比咬得兇」，看起來比實際難。

**數論的應用** [▶ 01:11](https://youtu.be/qBrYneqX_vE?t=71)：

- 第一次考試前會講密碼學。**公鑰加密**（public key encryption）是網路上幾乎所有安全機制的基礎，而它「完完全全是數論」。
- 【口頭】諷刺的是，19、20 世紀之交有些數論學家很得意自己的學問「完全沒有應用」。講者引用 **Dickson**（1874–1954）的話：「感謝上帝，數論沒有被任何應用玷污。」（"Thank God that number theory is unsullied by any application."）
  - ⚠️ 逐字稿缺字：字幕寫「leonard uh dickinson」。以下**不是逐字稿內容**，是依年份推論的：應是 Leonard Eugene **Dickson**。
- 【口頭】數論最主要的教學對象之一其實是**資訊系學生**。「離散數學其實就是初等數論」，例如不同進位制。

**「高等算術」的笑話** [▶ 03:38](https://youtu.be/qBrYneqX_vE?t=218)：

- 20 世紀初，數論常被叫做「**高等算術**」（higher arithmetic）。
- 【口頭】Serre 有一本很有名的書叫《A Course in Arithmetic》（字幕拼成 sayre / sarah）。講者聽他哥哥說的故事：紐約一位很厲害的數論學家在地鐵上讀這本書，一位老太太稱讚他「這把年紀還有勇氣回學校讀書」。講者說這本書「是史上最難的數學書之一」，但在老太太眼裡只是一個大人在學算術。講者說他知道這是紐約時報的文章，但有付費牆，沒能找到出處。

---

## 2. 除法演算法

### 2.1 從例子看起

[▶ 06:44](https://youtu.be/qBrYneqX_vE?t=404)

算 $11\div 3$：一直減 3，減到不能再減。

$$11-3=8,\qquad 8-3=5,\qquad 5-3=2.$$

減了 3 次，剩 2，而 $2<3$ 不能再減。所以

$$11 = 3\cdot 3 + 2,\qquad\text{也就是}\qquad \frac{11}{3} = 3+\frac23.$$

【口頭】數論、群論等等**比較喜歡左邊的寫法**（整數的等式），而不是右邊的分數。除法演算法就是在找這種寫法。

### 2.2 定理與存在性證明

[▶ 08:19](https://youtu.be/qBrYneqX_vE?t=499)

> **定理（除法演算法，division algorithm）**：若 $a,b$ 是整數且 $b>0$，則存在**唯一**的整數 $q$（商，quotient）和 $r$（餘數，remainder），使
> $$a = qb + r,\qquad 0\le r<b.$$

> 【課本補充】§1.1 Theorem 1.1（p. 2）陳述相同。課本的例子（Example 1.1）：$a=9,b=4$ 時 $9=2\cdot 4+1$，$q=2,r=1$；$a=-9,b=4$ 時 $q=-3,r=3$（因為 $-9 = (-3)\cdot 4 + 3$）。注意負數的餘數仍要在 $0$ 和 $b$ 之間。

**證明（存在性）** [▶ 09:31](https://youtu.be/qBrYneqX_vE?t=571)：用**良序原理**（well-ordering principle：自然數的任何非空子集合都有最小元素）。

想法就是 2.1 的例子：從 $a$ 一直減 $b$，減到最小、但還不是負的，那就是餘數。

**Step 1：造集合。** 令

$$R = \{\,a-nb \;:\; n\in\mathbb{Z},\ a-nb\ge 0\,\}.$$

$R$ 裡都是非負整數，所以 $R\subseteq\mathbb{N}_0$。

【口頭】$\mathbb{N}_0 = \{0,1,2,\dots\}$ 是講者臨時發明的記號，免得每次都要寫「包含 0 的自然數」。「文明世界有一半把 0 算進自然數，剩下不文明的那一半，像我，從 1 開始。」

**Step 2：$R$ 不是空的。** [▶ 13:15](https://youtu.be/qBrYneqX_vE?t=795)

【課堂討論】講者問「怎麼說服我 $R$ 不是空的？」學生先說「$0$ 在 $R$ 裡」、「取 $n=-1$」，講者指出我們不知道 $a$ 的正負，要分情況：

- **$a\ge 0$**：取 $n=0$，則 $a-0\cdot b = a\ge 0$，所以 $a\in R$。
- **$a<0$**：取 $n=a$ [▶ 15:24](https://youtu.be/qBrYneqX_vE?t=924)，則
  $$a - ab = a(1-b).$$
  $a<0$，而 $b\ge 1$ 所以 $1-b\le 0$。負數乘以非正數 $\ge 0$，所以 $a-ab\in R$。

（講者說「$1-b$ 是負的」；嚴格說 $b=1$ 時 $1-b=0$，乘積是 $0$，仍然 $\ge 0$，結論不變。）

**Step 3：取最小元素。** [▶ 16:32](https://youtu.be/qBrYneqX_vE?t=992) $R$ 是 $\mathbb{N}_0$ 的非空子集合，由良序原理，它有最小元素，叫它 $r$。因為 $r\in R$，存在某個 $n$ 使

$$r = a-nb,\qquad\text{即}\qquad a = nb + r.$$

令 $q=n$，就得到 $a=qb+r$，而且 $r\ge 0$。

**Step 4：證 $r<b$（反證）。** [▶ 18:35](https://youtu.be/qBrYneqX_vE?t=1115)

假設 $r\ge b$。令

$$r' = a-(n+1)b = (a-nb) - b = r-b.$$

- 因為 $r\ge b$，所以 $r'=r-b\ge 0$，而且 $r'$ 是 $a$ 減去 $b$ 的整數倍，所以 $r'\in R$。
- 但 $r' = r-b < r$（因為 $b>0$）。

這和「$r$ 是 $R$ 的最小元素」矛盾。所以 $0\le r<b$。∎

【口頭】講者說他「在看自己的筆記打字，搞亂了思路」，所以 $R$ 的定義一度猶豫要不要寫「$\ge 0$」還是「$>0$」。上面用 $\ge 0$（這樣餘數 $0$ 才包含在內）。

### 2.3 唯一性（課堂跳過）

[▶ 22:50](https://youtu.be/qBrYneqX_vE?t=1370)

講者說唯一性「我要跳過」，證明在他會貼出的 LaTeX 講義裡。

> 【課本補充】§1.1 Theorem 1.1 的唯一性證明（p. 2）：
> 假設 $a = qb+r = q'b+r'$，其中 $0\le r<b$、$0\le r'<b$。則
> $$r-r' = (q'-q)\,b.$$
> **關鍵一步**：若 $q'\neq q$，則 $|q'-q|\ge 1$，所以 $|r-r'|\ge b$。但 $r$ 和 $r'$ 都在 $0$ 到 $b-1$ 之間，兩者差距最多 $b-1$，矛盾。所以 $q'=q$，於是 $r'=r$。∎

### 2.4 用 floor 算商：計算機做法

[▶ 23:20](https://youtu.be/qBrYneqX_vE?t=1400)

當 $b>0$，把 $a=qb+r$ 除以 $b$：

$$\frac ab = q + \frac rb,\qquad 0\le\frac rb<1.$$

所以 $q$ 就是 $\dfrac ab$ 的**整數部分**：

$$q = \left\lfloor \frac ab\right\rfloor.$$

> **floor 函數**（地板函數）$\lfloor x\rfloor$：小於或等於 $x$ 的最大整數。

例子 [▶ 23:51](https://youtu.be/qBrYneqX_vE?t=1431)：

$$\lfloor -0.4\rfloor = -1,\qquad \lfloor\pi\rfloor = 3,\qquad \lfloor n+\varepsilon\rfloor = n\ \ (n\in\mathbb{Z},\ 0\le\varepsilon<1).$$

注意 $\lfloor -0.4\rfloor$ 是 $-1$，不是 $0$：floor 是**往下**取。

**計算機例子：$324\div 11$** [▶ 24:52](https://youtu.be/qBrYneqX_vE?t=1492)

1. 計算機：$324/11 = 29.4545\ldots$
2. 商：$q = \lfloor 29.4545\ldots\rfloor = 29$。
3. 餘數：$r = 324 - 29\cdot 11 = 324-319 = 5$。

所以 $324 = 29\cdot 11 + 5$。

【口頭】也可以用小數部分算：$11\times 0.4545\ldots$，計算機會給 $4.9995$ 之類的，「歪頭瞇眼看，就是 5」。但不用這麼麻煩：知道 $q=29$ 之後，直接 $a-qb$ 就是餘數。

### 2.5 除數是負的：改用 ceiling

[▶ 26:55](https://youtu.be/qBrYneqX_vE?t=1615)

**例子：$456\div(-10)$**

1. 計算機：$456/(-10) = -45.6 = -45 - 0.6$。
2. 「歪頭瞇眼」看出：$456 = (-45)(-10) + 6$。

所以 $q=-45$、$r=6$。

**這時 $q$ 不是 floor** [▶ 28:41](https://youtu.be/qBrYneqX_vE?t=1721)：$\lfloor -45.6\rfloor = -46$。$-45$ 是 **ceiling**（天花板函數）$\lceil x\rceil$：大於或等於 $x$ 的最小整數。

$$\left\lceil \frac{456}{-10}\right\rceil = \lceil -45.6\rceil = -45.$$

> 為什麼不能用 floor：若 $q=-46$，則 $r = 456-(-46)(-10) = 456-460 = -4<0$，餘數變負的，不合要求。

**一般版本** [▶ 29:42](https://youtu.be/qBrYneqX_vE?t=1782)：講者說 $b<0$ 的證明「只是記帳的問題」，他講義裡直接從正的版本借過來。

> **定理（非零除數版的除法演算法）**：若 $a,b$ 是整數且 $b\neq 0$，則存在唯一的整數 $q,r$，使
> $$a = qb+r,\qquad 0\le r<|b|.$$

例如 $b=-10$ 時 $r=6$，確實 $0\le 6<|-10|=10$。

> 【課本補充】§1.1 Corollary 1.2（p. 3）陳述相同。課本的證法：$b<0$ 時 $-b>0$，用 Theorem 1.1 得 $a = q^*(-b)+r$，$0\le r<-b$；令 $q=-q^*$ 就得 $a=qb+r$。課本也指出這時 $q = \lceil a/b\rceil$，跟講者的例子一致。

**【口頭】用詞** [▶ 56:26](https://youtu.be/qBrYneqX_vE?t=3386)：講者刻意不把 $b$ 叫「除數」（divisor），而說「dividing number」，因為說「$b$ 是 $a$ 的因數（divisor）」暗示餘數是 0，而這裡還不知道。

---

## 3. 整除

### 3.1 定義：因數、倍數、質數

[▶ 31:43](https://youtu.be/qBrYneqX_vE?t=1903)

> **定義（整除）**：$a,b$ 是整數。若存在整數 $c$ 使 $a = bc$，就說 **$b$ 整除 $a$**（$b$ divides $a$），寫成 $b\mid a$。這時 $b$ 是 $a$ 的**因數**（factor / divisor），$a$ 是 $b$ 的**倍數**（multiple）。

【口頭】$b\mid a$ 是一個**敘述**（對或錯），不是分數。

【口頭】[▶ 39:46](https://youtu.be/qBrYneqX_vE?t=2386) 講者說他習慣想「倍數」：「$a\mid c$」就想成「$c$ 是 $a$ 的倍數」。「這個 divides 的說法快把我逼瘋了。這也許證明我不是數論學家。」

> 【課本補充】§1.1（p. 3–4）提醒幾個容易搞錯的地方：**每個整數都整除 0**（因為 $0 = 0\cdot b$）；$1$ 整除每個整數；每個整數都整除自己。

**質數** [▶ 33:06](https://youtu.be/qBrYneqX_vE?t=1986)

講者先寫：若 $p\in\mathbb{N}$，且「$n\mid p$ 推得 $n=p$ 或 $n=1$」，就說 $p$ 是質數。然後說「這個定義**幾乎**正確」。

【課堂討論】[▶ 34:10](https://youtu.be/qBrYneqX_vE?t=2050) 少了什麼？問題在：**1 是質數嗎？** 照上面的定義，$1$ 的因數只有 $1$，所以 $1$ 會被算進去。學生說談質因數分解時不想讓 1 算進去。講者說他「相當確定」1 不是質數，但被問到有點動搖：「也許抽象代數學家說 1 不是質數，因為他們有抽象的質數定義；初等數論學家可能說 1 是，免得句子要多講幾個字。本課暫時『審查中』，但我想 1 不是質數。」

> 【課本補充】§2.1（p. 19）的定義把 1 排除了：**整數 $p>1$ 若唯一的正因數是 $1$ 和 $p$，就叫質數。** 本筆記之後都照這個定義。

### 3.2 整除的基本性質

[▶ 35:21](https://youtu.be/qBrYneqX_vE?t=2121)

> **命題**：$a,b,c,d,m$ 是整數。
> 1. 若 $a\mid b$ 且 $b\mid c$，則 $a\mid c$。
> 2. 若 $a\mid b$ 且 $c\mid d$，則 $ac\mid bd$。
> 3. 若 $m\neq 0$，則 $ma\mid mb \iff a\mid b$。
> 4. 若 $d\mid a$ 且 $a\neq 0$，則 $|d|\le|a|$。

（字幕在第 2 條的結論掉字；上面依課本 Exercise 1.3(b) 補上。）

- 第 3、4 條是**作業**（不做解答）。
- 【課本補充】這就是課本 §1.1 Exercise 1.3（p. 4）。

**證明第 1 條** [▶ 38:40](https://youtu.be/qBrYneqX_vE?t=2320)（學生選的）

1. $a\mid b$ ⇒ 存在整數 $n$ 使 $b = na$。
2. $b\mid c$ ⇒ 存在整數 $m$ 使 $c = mb$。
3. 把第 1 式代入第 2 式 [▶ 40:20](https://youtu.be/qBrYneqX_vE?t=2420)：
   $$c = mb = m(na) = (mn)\,a.$$
4. $mn$ 是整數，所以 $c$ 是 $a$ 的倍數，$a\mid c$。∎

講者說第 2 條的證明「很像」，沒做。

### 3.3 整除與整數線性組合

[▶ 40:52](https://youtu.be/qBrYneqX_vE?t=2452)

> **定理**（講者講義編號 Theorem 3.4）：$a_1,\dots,a_k,c$ 是整數。
> 1. 若 $c\mid a_i$ 對 $i=1,\dots,k$ 都成立，則對**所有**整數 $u_1,\dots,u_k$，
>    $$c \mid u_1a_1+u_2a_2+\cdots+u_ka_k.$$
> 2. $a\mid b$ 且 $b\mid a$ $\iff$ $a=\pm b$。

第 1 條白話：**$c$ 整除每個 $a_i$，就整除它們的任何整數線性組合**（integer linear combination）。「整除跟整數線性組合處得很好。」

> **推論**（講者講義編號 Corollary 3.5）[▶ 43:08](https://youtu.be/qBrYneqX_vE?t=2588)：若 $c\mid x$ 且 $c\mid y$，則對所有整數 $a,b$，
> $$c\mid ax+by.$$

講者說這是定理第 1 條 $k=2$ 的特例，證明一樣難但比較不笨重，所以證這個。

**證明** [▶ 44:16](https://youtu.be/qBrYneqX_vE?t=2656)

1. $c\mid x$、$c\mid y$ ⇒ 存在整數 $m,n$ 使 $x = mc$、$y = nc$。
2. 任取整數 $a,b$。代入：
   $$ax+by = a(mc)+b(nc) = (am+bn)\,c.$$
3. $am+bn$ 是整數，所以 $c\mid ax+by$。∎

【口頭】[▶ 43:42](https://youtu.be/qBrYneqX_vE?t=2622) 這些證明都差不多。有時要用到一個事實：**兩個整數相乘等於 1，只能是 $1\cdot 1$ 或 $(-1)(-1)$**。講者說這可以當作已知，或者用作業第 1、2 題的構造去證。

> 【課本補充】§1.1 Theorem 1.3（p. 4）就是講者的 Theorem 3.4，Corollary 1.4（p. 5）就是 Corollary 3.5。課本也證了第 2 條：
> - ($\Leftarrow$) $a=\pm b$ ⇒ $b = (\pm1)a$、$a = (\pm1)b$，互相整除。
> - ($\Rightarrow$) 設 $b = qa$、$a = q'b$。若 $b=0$ 則 $a = q'\cdot 0 = 0$，成立。若 $b\neq 0$：消去 $a$ 得 $b = qq'b$，兩邊消去 $b$ 得 $qq'=1$。**關鍵一步**：兩個整數乘積是 1，所以 $q,q'=\pm1$（課本用 Exercise 1.3(d)），因此 $a=\pm b$。

---

## 4. 最大公因數

### 4.1 定義與存在

[▶ 46:37](https://youtu.be/qBrYneqX_vE?t=2797)

> **定義**：若 $d\mid a$ 且 $d\mid b$，就說 $d$ 是 $a$ 和 $b$ 的**公因數**（common divisor）。

【口頭】「這個你們大概二、三年級就知道了。」

**為什麼一定有「最大的」** [▶ 47:26](https://youtu.be/qBrYneqX_vE?t=2846)：

- 由 3.2 的第 4 條，若 $d\mid a$ 且 $a\neq 0$，則 $|d|\le|a|$。
- 所以正的公因數只能在 $1$ 到 $\max(|a|,|b|)$ 之間。這是**有限多個**數。
- $1$ 永遠是公因數，所以這個有限集合不是空的，一定有最大的一個。

> **定義**：$a,b$ 的最大公因數記作 $\gcd(a,b)$（greatest common divisor）。

> 【課本補充】§1.1（p. 5）的定義寫得更精確：$a,b$ **不全為 0** 時，$\gcd(a,b)$ 是唯一滿足下面兩條的整數 $d$：
> 1. $d\mid a$ 且 $d\mid b$（是公因數）；
> 2. 若 $c\mid a$ 且 $c\mid b$，則 $c\le d$（沒有公因數比它大）。
>
> **$a=b=0$ 要排除**：每個整數都整除 0，所以每個整數都是 0 和 0 的公因數，沒有最大的。

### 4.2 小學的方法：質因數分解

[▶ 49:42](https://youtu.be/qBrYneqX_vE?t=2982)

**例子：$\gcd(105, 90)$**

1. 分解：
   $$105 = 3\cdot 35 = 3\cdot 5\cdot 7,\qquad 90 = 9\cdot 10 = 3\cdot 3\cdot 2\cdot 5.$$
2. 兩邊能配對的質因數盡量配：一個 $3$、一個 $5$。剩下的（另一個 $3$、$2$、$7$）配不起來。
3. $\gcd(105,90) = 3\cdot 5 = 15$。

**缺點** [▶ 51:27](https://youtu.be/qBrYneqX_vE?t=3087)：大數的**質因數分解很難**。所以對大數，這方法很糟。需要更好的方法——這就是 Euclid 演算法（第 4 集）。

> 【課本補充】§1.1（p. 5）提到另一個小學方法：**列出所有正因數**，挑共同的最大者。例如 $12$ 的正因數 $1,2,3,4,6,12$，$-18$ 的正因數 $1,2,3,6,9,18$，所以 $\gcd(12,-18)=6$。課本說 Euclid 演算法出自《幾何原本》第 VII 卷，約西元前 300 年。

【口頭】[▶ 54:24](https://youtu.be/qBrYneqX_vE?t=3264) 講者改用投影片（他網站上的「模運算補充講義」，從整數講起）趕進度。他說這些證明「完全是你們能懂的，可能是好的考題；考前我會預告」。「**我在課堂上講的定義，你都要會**，這是進階數學課 101。」

### 4.3 關鍵引理 gcd(a,b) = gcd(b,r)

[▶ 58:27](https://youtu.be/qBrYneqX_vE?t=3507)

> **引理**：若 $a,b,q,r$ 是整數，且 $a = qb+r$，則
> $$\gcd(a,b) = \gcd(b,r).$$

講者說「這很有意思」，開始證明，影片在中途被切斷，接第 4 集。

**證明想法**（講者講到的部分）[▶ 59:15](https://youtu.be/qBrYneqX_vE?t=3555)：

- $b$ 和 $r$ 的公因數 ⇒ 整除 $qb+r$（整數線性組合，用 3.3 的推論）⇒ 整除 $a$。
- 反過來，$a$ 和 $b$ 的公因數 ⇒ 整除 $a-qb = r$。

> 【課本補充】§1.1 Lemma 1.5（p. 5）的證明就是這樣，再補一句收尾：**所以 $(a,b)$ 和 $(b,r)$ 有完全一樣的公因數，最大的那個當然也一樣。** ∎

---

## 5. 一頁速查表

**除法演算法**

- $a,b\in\mathbb{Z}$、$b\neq 0$ ⇒ 存在唯一 $q,r$：$a=qb+r$，$0\le r<|b|$。
- **存在性關鍵一步**：$R=\{a-nb\ge 0\}$ 非空（$a\ge0$ 取 $n=0$；$a<0$ 取 $n=a$），取最小元素 $r$；若 $r\ge b$，則 $r-b\in R$ 更小，矛盾。
- **唯一性關鍵一步**：$r-r'=(q'-q)b$，$q\neq q'$ ⇒ $|r-r'|\ge|b|$，不可能。
- 算商：$b>0$ 時 $q=\lfloor a/b\rfloor$；$b<0$ 時 $q=\lceil a/b\rceil$。然後 $r=a-qb$。
- 例：$324=29\cdot 11+5$；$456=(-45)(-10)+6$；$-9=(-3)\cdot 4+3$。

**整除**

- $b\mid a$ ⇔ 存在 $c\in\mathbb{Z}$，$a=bc$。每個整數都整除 0。
- 質數：整數 $p>1$，正因數只有 $1$ 和 $p$（1 不是質數）。
- $a\mid b,\ b\mid c$ ⇒ $a\mid c$。**關鍵一步**：$c = mb = m(na) = (mn)a$。
- $a\mid b,\ c\mid d$ ⇒ $ac\mid bd$；$m\neq0$ 時 $ma\mid mb\iff a\mid b$；$d\mid a,\ a\neq0$ ⇒ $|d|\le|a|$。
- $c\mid x,\ c\mid y$ ⇒ $c\mid ax+by$。**關鍵一步**：$ax+by = (am+bn)c$。
- $a\mid b$ 且 $b\mid a$ ⇔ $a=\pm b$。**關鍵一步**：$qq'=1$ ⇒ $q=\pm1$。

**最大公因數**

- $a,b$ 不全為 0 時存在（正公因數在 $1$ 到 $\max(|a|,|b|)$ 之間，有限多個）。
- $\gcd(105,90)=15$（質因數分解；大數不適用）。
- $a=qb+r$ ⇒ $\gcd(a,b)=\gcd(b,r)$。**關鍵一步**：兩對數的公因數完全相同。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\gcd(a,b)=\gcd(b,r)$ → Euclid 演算法 | 第 4 集 |
| 整數線性組合、Bézout | 第 4–5 集 |
| 質數、質因數分解 | 第 5–6 集 |
| 除法演算法的餘數 → 模運算 | 第 7–8 集 |
| 公鑰加密 | 第 13–14 集（RSA） |
| 高斯整數的除法演算法 | 第 15–16 集 |
| 「1 是不是質數」的抽象版（單位 vs 質元素） | 第 17 集起、第 27 集起 |

---

## 附：本集一句話總結

> **除法演算法說：任何整數 $a$ 除以非零 $b$，都有唯一的商和 $0\le r<|b|$ 的餘數，存在性靠良序原理。整除跟整數線性組合處得很好，由此推出 $\gcd(a,b)=\gcd(b,r)$——這是 Euclid 演算法的基礎。**

---

*筆記依據 James S. Cook「Number Theory」2021-08-18 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與 Jones & Jones《Elementary Number Theory》§1.1、§2.1 整理。*
