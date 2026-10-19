---
course: Abstract Algebra I (Fall 2016)
episode: 5
lecture: L4
date: 2016-09-05
video: https://www.youtube.com/watch?v=PHqmS3JUpf4
notes: AlgebraInotes_2018.pdf §1.1 Prequel 1（p.9–15）
---

# 第 5 集 · L4：除法算則、整除、gcd、輾轉相除法與 Bézout 等式 [▶ 影片](https://www.youtube.com/watch?v=PHqmS3JUpf4&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[04-L3-中心-中心化子-二面體群]] ｜ [總目錄](../README.md) ｜ 下一集：[[06-習題課-Gallian第2-3章]] →

> **課程**：Abstract Algebra I（Liberty University，Fall 2016）— 第 5 集，Lecture 4
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（52:23，自動字幕）＋ 講義 `AlgebraInotes_2018.pdf` §1.1「Prequel 1: integers」（p.9–15）。老師口頭說的編號（如「1.4.3」「Lemma 1.4.13」）是 2016 版講義，2018 版改成 1.1.x。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字，依講義補；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 除法算則](#1-除法算則)
- [2. 整除與質數](#2-整除與質數)
- [3. 整除的基本性質](#3-整除的基本性質)
  - [3.1 命題：四條性質](#31-命題四條性質)
  - [3.2 定理：線性組合、互相整除](#32-定理線性組合互相整除)
- [4. 公因數與最大公因數](#4-公因數與最大公因數)
- [5. 輾轉相除法](#5-輾轉相除法)
  - [5.1 關鍵引理：gcd(a,b) = gcd(b,r)](#51-關鍵引理gcdab--gcdbr)
  - [5.2 演算法](#52-演算法)
  - [5.3 例：gcd(100, 44)](#53-例gcd100-44)
- [6. 擴展輾轉相除法：倒推回去](#6-擴展輾轉相除法倒推回去)
  - [6.1 例：100 和 44](#61-例100-和-44)
  - [6.2 例：240 和 11](#62-例240-和-11)
- [7. Bézout 等式與模反元素](#7-bézout-等式與模反元素)
- [8. 【講義補充】Bézout 的推論與 Euclid 引理](#8-講義補充bézout-的推論與-euclid-引理)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/PHqmS3JUpf4?t=0) 課前禱告。

今天講**整數的基本數論**：除法算則、整除、最大公因數、輾轉相除法、Bézout 等式。這是講義的 Prequel 1（前傳 1）。目的是**下一講把模運算建立在嚴謹的基礎上**（L2 只是「貪心地宣稱」）。

【口頭】[▶ 18:43](https://youtu.be/PHqmS3JUpf4?t=1123)「對於一堂數論入門來說，這裡數字少得驚人。這批評很公平。讓我帶你們去一個快樂的地方——一個沒有字母、只有數字的地方。」

---

## 1. 除法算則

[▶ 00:00](https://youtu.be/PHqmS3JUpf4?t=0)

> **定理（非零除法算則 nonzero division algorithm）**　$a,b\in\mathbb{Z}$，$b\neq0$。則存在**唯一**的**商（quotient）** $q\in\mathbb{Z}$ 和**餘數（remainder）** $r\in\mathbb{Z}$，使得
> $$a = qb+r,\qquad 0\le r<|b|.$$

（學生問板書的驚嘆號：$\exists!$ 表示「存在唯一」[▶ 03:33](https://youtu.be/PHqmS3JUpf4?t=213)。）

**證明的想法**（課堂只講概念，細節在講義）[▶ 01:32](https://youtu.be/PHqmS3JUpf4?t=92)：
- 先做 $b>0$ 的情況：看集合 $\{a-nb\}$ 裡的非負整數，取**最小元素**，它就是餘數。
- 再稍微調整，處理 $b<0$。

> 📘 **講義 Theorem 1.1.2（正除法算則，$b>0$）的證明**：
>
> **存在性**：令 $R = \{a-nb : n\in\mathbb{Z},\ a-nb\ge0\}$，就是從 $a$ 加減 $b$ 的倍數能到達的非負整數。
> 1. $R$ 非空：取 $n = -|a|$，$a-nb = a+|a|b$。若 $a\ge0$ 顯然 $\ge0$；若 $a<0$，$a+|a|b = |a|(b-1)\ge0$（因為 $b\ge1$）。
> 2. 由**良序原理**（非負整數的非空子集有最小元素），$R$ 有最小元素 $r = a-nb$。
> 3. 若 $r\ge b$，則 $r' = a-(n+1)b = r-b\ge0$，$r'\in R$ 且 $r'<r$，矛盾。所以 $0\le r<b$。
>
> **唯一性**：設 $a = qb+r = q'b+r'$，$0\le r,r'<b$。則 $(q-q')b = r'-r$。若 $q\neq q'$，則 $|q-q'|\ge1$，$|r'-r|\ge b$。但 $r,r'\in[0,b)$，距離小於 $b$，矛盾。所以 $q = q'$，進而 $r = r'$。
>
> **$b<0$ 的情況**（Theorem 1.1.3）：對 $a$ 和 $-b>0$ 用上面的定理，得 $a = q'(-b)+r'$。取 $q = -q'$、$r = r'$。

> 📘 講義補充：
> - **除法就是重複減法**。例：$11 = 3\cdot3+2$，也就是 $\frac{11}{3} = 3+\frac23$。
> - $b>0$ 時 $q = \lfloor a/b\rfloor$（**地板函數**）。例：$\frac{324}{11} = 29.4545\ldots$ ⇒ $324 = 29\cdot11+5$。
> - $b<0$ 時用**天花板函數**：$456 = (-10)(-45)+6$，$\lceil456/(-10)\rceil = -45$。
> - 帶分數 $3\tfrac13$ 其實是 $3+\tfrac13$，「這個爛記號造成無數錯誤」。除法算則就是「假分數可以寫成整數加真分數」——你小時候就知道了。

---

## 2. 整除與質數

> **定義（整除 divides）**[▶ 02:32](https://youtu.be/PHqmS3JUpf4?t=152)　$a,b\in\mathbb{Z}$。如果存在 $c\in\mathbb{Z}$ 使得
> $$a = bc,$$
> 就說 **$b$ 整除 $a$**，寫作 $b\mid a$。這時也說 $b$ 是 $a$ 的**因數（factor）**、$a$ 是 $b$ 的**倍數（multiple）**。

**注意**[▶ 03:33](https://youtu.be/PHqmS3JUpf4?t=213)：$b\mid a$ **不是運算**，是一個**敘述**（對或錯）。不整除寫 $b\nmid a$。

> **定義（質數 prime）**[▶ 04:03](https://youtu.be/PHqmS3JUpf4?t=243)　$p\in\mathbb{N}$。如果「$n\mid p$ 推出 $n = p$ 或 $n = 1$」，就說 $p$ 是**質數**。

（老師正要讓大家填空，學生已經先說出「質數」。）白話：質數是只有 1 和自己兩個正因數的正整數。

> 📘 講義補充：
> - 每個 $b$ 都整除 $0$（$0 = b\cdot0$）；$b\mid b$（$b = b\cdot1$）；$1$ 整除每個整數。
> - 因數不唯一（$105 = 7\cdot15 = 3\cdot35 = (-1)(-105)$），但**質因數**在不計順序下唯一：$105 = 3\cdot5\cdot7$。

---

## 3. 整除的基本性質

### 3.1 命題：四條性質

[▶ 04:34](https://youtu.be/PHqmS3JUpf4?t=274)「希望這是複習。」老師用填空方式寫，邊證邊填。

> **命題**　$a,b,c,d,m\in\mathbb{Z}$。
> 1. $a\mid b$ 且 $b\mid c$ ⇒ $a\mid c$。
> 2. $a\mid b$ 且 $c\mid d$ ⇒ $ac\mid bd$。
> 3. $m\neq0$ 時，$ma\mid mb$ ⟺ $a\mid b$。
> 4. $d\mid a$ 且 $a\neq0$ ⇒ $|d|\le|a|$。

**證明 (1)**[▶ 06:37](https://youtu.be/PHqmS3JUpf4?t=397)

設 $a\mid b$、$b\mid c$。由定義，存在 $k,l\in\mathbb{Z}$ 使
$$b = ka,\qquad c = lb.$$
代入：
$$c = lb = l(ka) = (lk)a.$$
$lk\in\mathbb{Z}$，所以 $a\mid c$。$\blacksquare$

【課堂討論】[▶ 08:10](https://youtu.be/PHqmS3JUpf4?t=490) (2) 和 (3) 的空格由學生填出：$ac\mid bd$；$a\mid b$。

> 📘 **講義的證明**：
> - **(2)**：$b = ma$、$d = nc$ ⇒ $bd = (ma)(nc) = (mn)(ac)$，所以 $ac\mid bd$。
> - **(4)**：$a = md$。若 $m = 0$ 則 $a = 0$，矛盾，所以 $m\neq0$，$|m|\ge1$。於是 $|a| = |m||d|\ge|d|$。
> - (3) 講義留給讀者。

### 3.2 定理：線性組合、互相整除

[▶ 09:16](https://youtu.be/PHqmS3JUpf4?t=556)（老師：「我不知道為什麼這個叫定理、另一個叫命題。」）

> **定理**　$a_1,\dots,a_k,c\in\mathbb{Z}$。
> 1. 若 $c\mid a_i$ 對 $i = 1,\dots,k$ 都成立，則對任意 $u_1,\dots,u_k\in\mathbb{Z}$，
> $$c\mid(u_1a_1+u_2a_2+\cdots+u_ka_k).$$
> 2. $a\mid b$ 且 $b\mid a$ ⟺ $a = \pm b$。

**(1) 的白話**[▶ 10:17](https://youtu.be/PHqmS3JUpf4?t=617)：如果 $c$ 整除每個 $a_i$，那 $c$ 就整除它們的**任何整數線性組合**。（證明跟 (1) 的命題一樣，課堂略過；講義：$a_i = cm_i$ ⇒ $\sum u_ia_i = c\sum u_im_i$。）

**證明 (2)**[▶ 11:24](https://youtu.be/PHqmS3JUpf4?t=684)（「因為它有一個新想法」）

**(⇒)** 設 $a\mid b$、$b\mid a$。存在 $k,l\in\mathbb{Z}$ 使
$$b = ka,\qquad a = lb.$$

把 $b = ka$ 代入 $a = lb$ [▶ 11:55](https://youtu.be/PHqmS3JUpf4?t=715)：
$$a = l(ka) = (lk)a.$$

**情況 1：$a\neq0$**[▶ 12:33](https://youtu.be/PHqmS3JUpf4?t=753)。【課堂討論】學生建議兩邊除以 $a$：
$$1 = lk.$$
$l,k$ 是整數，乘積是 1，所以 $l = k = 1$ 或 $l = k = -1$ [▶ 13:04](https://youtu.be/PHqmS3JUpf4?t=784)。所以 $a = b$ 或 $a = -b$，即 $a = \pm b$。

**情況 2：$a = 0$**[▶ 13:35](https://youtu.be/PHqmS3JUpf4?t=815)。$a\mid b$ 就是 $0\mid b$，表示存在 $j$ 使
$$b = 0\cdot j = 0.$$
所以 $b = 0 = \pm a$ [▶ 14:39](https://youtu.be/PHqmS3JUpf4?t=879)。

「條條大路都通往 $a = \pm b$。」

**(⇐)**[▶ 15:10](https://youtu.be/PHqmS3JUpf4?t=910)「證明還沒完。」設 $a = \pm b$，則 $b = \pm a$。兩個式子都說明 $a,b$ 各是對方的 $\pm1$ 倍，所以互相整除。$\blacksquare$

**最重要的特例**[▶ 16:10](https://youtu.be/PHqmS3JUpf4?t=970)：$k = 2$ 的 (1)。

> **推論**　若 $c\mid x$ 且 $c\mid y$，則對所有 $a,b\in\mathbb{Z}$，$c\mid(ax+by)$。

這條在後面「反覆使用」。

---

## 4. 公因數與最大公因數

[▶ 16:42](https://youtu.be/PHqmS3JUpf4?t=1002)「這應該讓你們懷念起青春。你們還年輕，我在說什麼。」

> **定義**　$d\mid a$ 且 $d\mid b$，就說 $d$ 是 $a,b$ 的**公因數（common divisor）**。

> **定義**[▶ 17:12](https://youtu.be/PHqmS3JUpf4?t=1032)　$a,b\in\mathbb{Z}$，**不全為 0**。$a,b$ 的**最大公因數（greatest common divisor）** $\gcd(a,b)$ 就是所有公因數裡最大的那個。

**為什麼要「不全為 0」**：每個整數都整除 0，所以 $\gcd(0,0)$ 沒有最大值。

**為什麼定義得好**[▶ 18:13](https://youtu.be/PHqmS3JUpf4?t=1093)：由命題 (4)，因數的絕對值不會超過它整除的數（$a\neq0$ 時）。「這是常識：$a = bc$，$c$ 是整數，至少是 1（或 $-3$ 之類，但絕對值處理了）。」所以公因數有上界，最大的存在。

**例：$\gcd(105,90)$**[▶ 19:13](https://youtu.be/PHqmS3JUpf4?t=1153)：小時候的方法——質因數分解，挑共同的質因數。
$$105 = 3\cdot5\cdot7,\qquad 90 = 2\cdot3\cdot3\cdot5.$$
共同的：一個 3、一個 5。所以 $\gcd(105,90) = 15$。

**這方法的問題**[▶ 20:13](https://youtu.be/PHqmS3JUpf4?t=1213)：
- **質因數分解很難**。「整數分解成質數的困難，你們每天都在用」——**RSA 加密**就是建立在大數分解的困難上。
- 老師：「我怎麼知道 $105 = 3\cdot5\cdot7$？你會說：你從講義讀的。沒錯，被你抓到了。」
- （學生提到 Eratosthenes 篩法。）
- 講義還提到：比對兩個清單挑共同項也不容易。

所以需要更好的方法：**輾轉相除法**。

---

## 5. 輾轉相除法

[▶ 21:14](https://youtu.be/PHqmS3JUpf4?t=1274)「Euclid（對，就是平行線那位）給了我們這個演算法。很古老，但很流行。」

### 5.1 關鍵引理：gcd(a,b) = gcd(b,r)

老師講到一半發現 [▶ 28:59](https://youtu.be/PHqmS3JUpf4?t=1739)：「我把重點埋掉了。我太興奮，漏了一個很重要的引理。如果我先講它，你們會說『喔，廢話』。」

> **引理**（講義 Lemma 1.1.13）　$a,b,q,r\in\mathbb{Z}$。若 $a = qb+r$，則
> $$\gcd(a,b) = \gcd(b,r).$$

**證明**[▶ 30:00](https://youtu.be/PHqmS3JUpf4?t=1800)：證明 $\{a,b\}$ 和 $\{b,r\}$ 有**完全相同的公因數**。關鍵是改寫成 $r = a-qb$。
- 若 $d$ 整除 $a$ 和 $b$：由推論，$d\mid(a-qb) = r$。所以 $d$ 是 $b,r$ 的公因數。
- 若 $d$ 整除 $b$ 和 $r$：由推論，$d\mid(qb+r) = a$。所以 $d$ 是 $a,b$ 的公因數。

公因數集合一樣，最大的那個也一樣。$\blacksquare$

「幾乎直接從這個等式和因數的定義得到。」

### 5.2 演算法

[▶ 21:45](https://youtu.be/PHqmS3JUpf4?t=1305) 只要處理 $a,b\in\mathbb{N}$，因為
$$\gcd(a,b) = \gcd(\pm a,\pm b)$$
（四種正負號組合都一樣，「由已證的定理可得」）。

**Step 1**[▶ 22:15](https://youtu.be/PHqmS3JUpf4?t=1335)：對 $a,b$ 用除法算則：
$$a = q_1b+r_1,\qquad 0\le r_1<b.$$
- 若 $r_1 = 0$：$a = q_1b$，$b\mid a$。【課堂討論】$\gcd(a,b)$ 是多少？$b$ [▶ 22:47](https://youtu.be/PHqmS3JUpf4?t=1367)。

**Step 2**[▶ 23:17](https://youtu.be/PHqmS3JUpf4?t=1397)：若 $r_1\neq0$，對 $b,r_1$ 用除法算則（$r_1$ 扮演上一步 $b$ 的角色，$b$ 扮演 $a$ 的角色）：
$$b = q_2r_1+r_2,\qquad 0\le r_2<r_1.$$
- 若 $r_2 = 0$：

【課堂討論】[▶ 24:17](https://youtu.be/PHqmS3JUpf4?t=1457) 老師一開始說「那 $b$ 就是 gcd」，學生糾正 [▶ 24:51](https://youtu.be/PHqmS3JUpf4?t=1491)。老師：「你們把我騙去說了蠢話。」正確推理：
- $r_2 = 0$ 時 $b = q_2r_1$，所以 $r_1\mid b$，$\gcd(b,r_1) = r_1$ [▶ 26:24](https://youtu.be/PHqmS3JUpf4?t=1584)。
- 再由 $a = q_1b+r_1$ 和引理，$\gcd(a,b) = \gcd(b,r_1) = r_1$。

（學生提出另一個看法 [▶ 27:28](https://youtu.be/PHqmS3JUpf4?t=1648)：代入得 $a = q_1q_2r_1+r_1 = (q_1q_2+1)r_1$，所以 $r_1$ 也整除 $a$。老師：「如果我們先內化了那個命題，就不用走這些細節。」）

**Step 3 以後**[▶ 31:31](https://youtu.be/PHqmS3JUpf4?t=1891)：若 $r_2\neq0$，
$$r_1 = q_3r_2+r_3,\qquad 0\le r_3<r_2,$$
由引理 $\gcd(b,r_1) = \gcd(r_1,r_2)$，一路連回 $\gcd(a,b)$。一直做下去，直到餘數是 0。

【課堂討論】[▶ 33:04](https://youtu.be/PHqmS3JUpf4?t=1984)**為什麼一定會停？**學生答：餘數**嚴格遞減**。
$$b>r_1>r_2>r_3>\cdots\ge0,$$
都是非負整數，所以最多 $b$ 步就會到 0。

> **定理（輾轉相除法 Euclidean algorithm）**　$a,b\in\mathbb{N}$，$a>b$。反覆做除法，直到餘數為 0：
> $$
> \begin{aligned}
> a &= q_1b+r_1\\
> b &= q_2r_1+r_2\\
> r_1 &= q_3r_2+r_3\\
> &\ \ \vdots\\
> r_{n-1} &= q_{n+1}r_n+0.
> \end{aligned}
> $$
> 則 $\gcd(a,b) = r_n$，也就是**最後一個非零餘數**。

理由：$\gcd(a,b) = \gcd(b,r_1) = \gcd(r_1,r_2) = \cdots = \gcd(r_{n-1},r_n) = r_n$（最後一步因為 $r_n\mid r_{n-1}$）。

「我的講義比我剛才講的好一點。通常是這樣。」[▶ 33:34](https://youtu.be/PHqmS3JUpf4?t=2014)

### 5.3 例：gcd(100, 44)

[▶ 34:05](https://youtu.be/PHqmS3JUpf4?t=2045)「我用講義上的例子，以免做蠢事。」

| 步驟 | 除法 | 餘數 |
|---|---|---|
| 1 | $100 = 44\cdot2+12$ | $r_1 = 12$ |
| 2 [▶ 34:37](https://youtu.be/PHqmS3JUpf4?t=2077) | $44 = 12\cdot3+8$ | $r_2 = 8$ |
| 3 [▶ 35:07](https://youtu.be/PHqmS3JUpf4?t=2107) | $12 = 8\cdot1+4$ | $r_3 = 4$ |
| 4 [▶ 35:37](https://youtu.be/PHqmS3JUpf4?t=2137) | $8 = 4\cdot2+0$ | 停 |

最後一個非零餘數是 4，所以 $\gcd(100,44) = 4$。

【口頭】[▶ 36:08](https://youtu.be/PHqmS3JUpf4?t=2168)「注意，我們沒用質因數分解。好吧，至少沒有直接用——你可以捫心自問，也許你在哪裡偷偷用了質數。」

---

## 6. 擴展輾轉相除法：倒推回去

[▶ 36:08](https://youtu.be/PHqmS3JUpf4?t=2168) 輾轉相除法只給 gcd。**擴展輾轉相除法（extended Euclidean algorithm）**還告訴我們：gcd 可以寫成兩數的**整數線性組合**。

### 6.1 例：100 和 44

目標：找整數 $k,l$ 使 $4 = 100k+44l$。

**方法**[▶ 37:10](https://youtu.be/PHqmS3JUpf4?t=2230)：從下往上倒推。

⚠️ 課堂上老師先試了「從上往下展開」，把 100 寫成一大串括號 [▶ 37:40](https://youtu.be/PHqmS3JUpf4?t=2260)，結果越弄越亂。「我不夠聰明……這不是我要的。這沒那麼複雜，我應該看講義的。」「好吧，我已經示範了**不該**怎麼做。」[▶ 40:12](https://youtu.be/PHqmS3JUpf4?t=2412)

**正確做法**（學生引導）[▶ 40:12](https://youtu.be/PHqmS3JUpf4?t=2412)：從**倒數第二步**把 gcd 解出來，然後一步一步代換餘數。

1. 由第 3 步 $12 = 8\cdot1+4$：
$$4 = 12-8.$$
2. 由第 2 步 $44 = 12\cdot3+8$，得 $8 = 44-3\cdot12$。代入：
$$4 = 12-(44-3\cdot12) = 4\cdot12-44.$$
3. 由第 1 步 $100 = 44\cdot2+12$，得 $12 = 100-2\cdot44$。代入 [▶ 41:13](https://youtu.be/PHqmS3JUpf4?t=2473)：
$$4 = 4(100-2\cdot44)-44 = 4\cdot100-9\cdot44.$$

**答案**[▶ 41:43](https://youtu.be/PHqmS3JUpf4?t=2503)：
$$4 = 4\cdot100-9\cdot44.$$
（檢查：$400-396 = 4$ ✓）

**訣竅**：每一步只代換**一個餘數**，代完先合併同類項，**別急著把括號全部乘開**（「要抵抗把東西乘開的誘惑」[▶ 39:11](https://youtu.be/PHqmS3JUpf4?t=2351)）。

【口頭】[▶ 41:43](https://youtu.be/PHqmS3JUpf4?t=2503)「大部分人理解這個演算法沒什麼困難。但只看別人做，你不會真的懂，你得自己做幾次。大概做到第三個你就覺得無聊了。這個例子沒有什麼特別的花招，同樣的模式對任何數都行。」

### 6.2 例：240 和 11

[▶ 43:18](https://youtu.be/PHqmS3JUpf4?t=2598)「我欠你們第二個例子。」

**往下除**：

| 步驟 | 除法 |
|---|---|
| ① | $240 = 11\cdot21+9$（$11\cdot21 = 231$） |
| ② | $11 = 9\cdot1+2$ |
| ③ | $9 = 2\cdot4+1$ |
| ④ | $2 = 1\cdot2+0$ |

最後非零餘數是 1，所以 $\gcd(240,11) = 1$：**互質**[▶ 44:18](https://youtu.be/PHqmS3JUpf4?t=2658)。「不意外，你們不用算也知道。你們從小就對質因數分解有些感覺。」

【口頭】[▶ 44:48](https://youtu.be/PHqmS3JUpf4?t=2688)「我不是數論學家，兩個數的 gcd 對我個人來說不怎麼刺激。**有趣的是**：我們能用有系統的方法找到 $k,l$。」

**倒推**[▶ 45:19](https://youtu.be/PHqmS3JUpf4?t=2719)：目標 $1 = 240k+11l$。
1. 由 ③：$1 = 9-4\cdot2$。
2. 由 ②：$2 = 11-9$。代入：
$$1 = 9-4(11-9) = 5\cdot9-4\cdot11.$$
   【課堂討論】[▶ 46:20](https://youtu.be/PHqmS3JUpf4?t=2780) 學生提醒先合併成 $5\cdot9$，「這一步簡化很划算」。
3. 由 ①：$9 = 240-21\cdot11$。代入 [▶ 47:22](https://youtu.be/PHqmS3JUpf4?t=2842)：
$$1 = 5(240-21\cdot11)-4\cdot11 = 5\cdot240-105\cdot11-4\cdot11 = 5\cdot240-109\cdot11.$$

老師先算成 $-59$，然後發現 $5\cdot21 = 105$ 不是 55：「我是白痴，是 105。所以是 109，講義也是這樣寫，所以我大概是對的。講義通常是對的——除了不對的時候。」

**答案**：
$$1 = 5\cdot240-109\cdot11.$$
（檢查：$1200-1199 = 1$ ✓）

【Q&A】[▶ 48:22](https://youtu.be/PHqmS3JUpf4?t=2902) 學生問 $5\cdot9$ 的 5 怎麼來。老師：「這裡有一個 9，那裡有 4 個（負負得正），$4+1 = 5$。」

【口頭】[▶ 46:51](https://youtu.be/PHqmS3JUpf4?t=2811)「我本來想在教完數論之後馬上教這門課，因為這些東西會還在腦中。結果去年是另一位老師教數論，所以數論在我腦中已經消失了。」

---

## 7. Bézout 等式與模反元素

[▶ 48:52](https://youtu.be/PHqmS3JUpf4?t=2932)【課堂討論】老師問：「這個 $k,l$ 存在的事實叫什麼？誰會念那個名字？」學生：「Bézout。」

> **定理（Bézout 等式 Bézout's identity）**　$a,b\in\mathbb{Z}$，不全為 0。則存在 $x,y\in\mathbb{Z}$ 使
> $$ax+by = \gcd(a,b).$$
> 白話：**兩個整數的 gcd 永遠可以寫成它們的整數線性組合**。

（學生補充：$k,l$ 叫做 **Bézout 係數**。老師：「很好，我不知道這個。」）

**證明**：就是上面的倒推。講義 Thm 1.1.19 寫出一般形式（以 $r_3 = \gcd$ 為例，逐步代回 $r_1 = a-q_1b$、$r_2 = b-q_2r_1$、$r_3 = r_1-q_3r_2$）。講義也提醒：$x,y$ **不唯一**。

**跟模運算的關係**[▶ 49:53](https://youtu.be/PHqmS3JUpf4?t=2993)：「下次我要把模運算放在堅實的基礎上。如果順利，明天會一路講到怎麼算模係數的矩陣反矩陣。」但現在就能「摘一些低垂的果實」：

從 $1 = 5\cdot240-109\cdot11$ 出發，對不同的模數看：

| 模數 | 哪一項變成 0 | 得到 |
|---|---|---|
| 模 11 | $109\cdot11\equiv0$ | $5\cdot240\equiv1$，所以 $240^{-1}\equiv5\pmod{11}$ |
| 模 240 | $5\cdot240\equiv0$ | $-109\cdot11\equiv1$，所以 $11^{-1}\equiv-109\equiv131\pmod{240}$ |
| 模 109 | $109\cdot11\equiv0$ | $5\cdot240\equiv1$，所以 $5^{-1}\equiv240\equiv22\pmod{109}$ |

> ⚠️ 逐字稿缺字：這段板書字幕很亂（念出「250」「mod 5」之類）。上表是依 $1 = 5\cdot240-109\cdot11$ 重新整理的正確讀法，邏輯跟老師說的一樣：在某個模數下，把等式裡變成 0 的那一項拿掉，剩下「兩數乘積 = 1」，它們就互為反元素 [▶ 51:25](https://youtu.be/PHqmS3JUpf4?t=3085)。
>
> 順帶一提：$240 = 21\cdot11+9\equiv9\pmod{11}$，所以第一行就是 $9^{-1} = 5$ in $U(11)$——正是 L2 的例子 $9\cdot5 = 45\equiv1$。

**重點**：**Bézout 等式給出有系統地算模反元素的方法。**

【口頭】[▶ 51:55](https://youtu.be/PHqmS3JUpf4?t=3115)「當然，$n$ 小的時候直接猜就好。如果你用擴展輾轉相除法去算 3 在模 6 下的反元素——恭喜，你在浪費時間。」（而且 $\gcd(3,6) = 3$，根本沒有反元素。）「說到浪費時間，我不浪費你們的時間了。」

**附帶更正**[▶ 50:23](https://youtu.be/PHqmS3JUpf4?t=3023)：
- 上一講結尾 $D_3$ 的計算漏了一個 $f$，學生指出。「很容易修好，講義上的例子是對的。」（見 [[04-L3-中心-中心化子-二面體群]] 6.4。）
- L2 講義上 $U(4)$ 應該是 $U(10)$。

---

## 8. 【講義補充】Bézout 的推論與 Euclid 引理

這兩個結果課堂沒講，講義 p.15 有，後面很常用。

> **推論 1.1.20**　$\gcd(a,b) = 1$ ⟺ 存在 $x,y\in\mathbb{Z}$ 使 $ax+by = 1$。

**證明**：(⇒) 就是 Bézout。(⇐) 設 $ax+by = 1$，$d$ 是 $a,b$ 的公因數，$a = dj$、$b = dk$。則 $d(jx+ky) = 1$，所以 $d\mid1$，$d = \pm1$。因此 $\gcd(a,b) = 1$。$\blacksquare$

（L2 證明 $U(n)$ 是群時就用到這條。）

> **Euclid 引理（Lemma 1.1.21）**　$p$ 是質數。若 $p\mid ab$，則 $p\mid a$ 或 $p\mid b$。

講義說：直覺上，Euclid 引理說明質數「**不可摧毀**」。

**證明**：設 $p\mid ab$ 但 $p\nmid a$。
1. $p$ 是質數、不整除 $a$，所以 $\gcd(a,p) = 1$。
2. 由 Bézout，存在 $x,y$ 使 $ax+py = 1$。
3. 兩邊乘 $b$：$abx+pby = b$。
4. $p\mid ab$，寫 $ab = cp$。代入：$b = cpx+pby = p(cx+by)$。
5. 所以 $p\mid b$。$\blacksquare$

---

## 9. 一頁速查表

### 9.1 定義

| 名稱 | 定義 |
|---|---|
| 除法算則 | $b\neq0$ ⇒ 唯一的 $q,r$ 使 $a = qb+r$，$0\le r<\lvert b\rvert$ |
| $b\mid a$ | 存在 $c\in\mathbb{Z}$ 使 $a = bc$（是敘述，不是運算） |
| 質數 | $p\in\mathbb{N}$，正因數只有 1 和 $p$ |
| $\gcd(a,b)$ | 不全為 0 時，最大的公因數 |

### 9.2 定理與證明關鍵一步

| 結果 | 關鍵一步 |
|---|---|
| $a\mid b,\ b\mid c\Rightarrow a\mid c$ | $c = lb = l(ka) = (lk)a$ |
| $c\mid x,\ c\mid y\Rightarrow c\mid(ax+by)$ | 提出 $c$ |
| $a\mid b,\ b\mid a\Leftrightarrow a = \pm b$ | $a = lka$；$a\neq0$ 時 $lk = 1$；$a = 0$ 時 $b = 0\cdot j = 0$ |
| $a = qb+r\Rightarrow\gcd(a,b) = \gcd(b,r)$ | $r = a-qb$，兩組有相同的公因數 |
| 輾轉相除法 | 餘數嚴格遞減必停；$\gcd$ = 最後一個非零餘數 |
| Bézout：$ax+by = \gcd(a,b)$ | 從倒數第二式解出 gcd，逐步代回餘數 |
| $\gcd(a,b) = 1\Leftrightarrow ax+by = 1$ 有解 | (⇐) 公因數 $d$ 整除 1 |
| Euclid 引理 | $ax+py = 1$ 乘 $b$，兩項都被 $p$ 整除 |

### 9.3 兩個例子

$$\gcd(100,44) = 4 = 4\cdot100-9\cdot44.$$
$$\gcd(240,11) = 1 = 5\cdot240-109\cdot11.$$

### 9.4 用 Bézout 算模反元素

$ax+ny = 1$ ⇒ 模 $n$ 下 $ax\equiv1$ ⇒ $a^{-1}\equiv x\pmod n$。

### 9.5 術語

| 中文 | English |
|---|---|
| 除法算則 | division algorithm |
| 商；餘數 | quotient; remainder |
| 良序原理 | well-ordering principle |
| 整除；因數；倍數 | divides; factor/divisor; multiple |
| 質數 | prime |
| 公因數 | common divisor |
| 最大公因數 | greatest common divisor (gcd) |
| 互質 | relatively prime |
| 整數線性組合 | integer linear combination |
| 輾轉相除法 | Euclidean algorithm |
| 擴展輾轉相除法 | extended Euclidean algorithm |
| Bézout 等式；Bézout 係數 | Bézout's identity; Bézout coefficients |
| Euclid 引理 | Euclid's lemma |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **Bézout、模反元素** | [[07-L5-模運算基礎]]：$\mathbb{Z}_n$ 的嚴謹建立、模 $n$ 矩陣的反矩陣；回扣 [[02-L2-模運算與子群]] 的 $U(n)$ 是群 |
| **除法算則** | [[10-L7-循環群-下]]：循環群的子群是循環的（證明用除法算則）；[[40-L26-多項式]]：多項式的除法算則 |
| **gcd** | [[10-L7-循環群-下]]：$\langle a^k\rangle = \langle a^{\gcd(n,k)}\rangle$；[[25-L16-外直積與內直積]]：lcm |
| **Euclid 引理、質數** | [[26-L17-一點數論]]：中國剩餘定理、Fermat/Euler、RSA；[[44-L28-整除與分解]]、[[45-L29-不可約與質元-ED-PID-UFD]]：推廣到整環（質元、歐氏整環） |
| **RSA 與分解的困難** | [[26-L17-一點數論]] |

---

## 附：本集一句話總結

> **除法算則保證 $a = qb+r$（$0\le r<|b|$）；因為 $\gcd(a,b) = \gcd(b,r)$，反覆做除法、餘數嚴格遞減，最後一個非零餘數就是 gcd（輾轉相除法）；把過程倒推回去，就得到 Bézout 等式 $ax+by = \gcd(a,b)$——它讓我們有系統地算出模反元素，也推出 Euclid 引理。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra I」(Fall 2016) Lecture 4 錄影逐字稿（YouTube 自動字幕，52:23）與講義 `AlgebraInotes_2018.pdf` §1.1（p.9–15）整理。*
