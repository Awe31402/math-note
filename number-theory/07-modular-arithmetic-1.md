---
course: Number Theory（2021 秋，線上錄影）
episode: 7
lecture: 2021-08-25 第 1 部
date: 2021-08-25
video: https://youtu.be/_F8TN0rLjuc
notes: Jones & Jones《Elementary Number Theory》§3.1（書頁 37–40，PDF 頁 52–55）：同餘定義、Lemma 3.1–3.2、同餘類、Z_n 與其運算；§2.4 數字判別法（書頁 32，PDF 頁 47）
---

# 第 7 集 · 模運算（上）（Modular Arithmetic, Part 1） [▶ 影片](https://youtu.be/_F8TN0rLjuc)

← 上一集：[06-fermat-numbers-mersenne-primes-sieve](06-fermat-numbers-mersenne-primes-sieve.md) ｜ [總目錄](README.md) ｜ 下一集：[08-modular-arithmetic-2](08-modular-arithmetic-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 7 集（2021-08-25 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；開頭幾句掉字，結尾被切斷）＋ Jones & Jones《Elementary Number Theory》§3.1、§2.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 同餘的定義](#1-同餘的定義)
  - [1.1 定義：餘數相同](#11-定義餘數相同)
  - [1.2 等價說法：n 整除差](#12-等價說法n-整除差)
- [2. 同餘是等價關係](#2-同餘是等價關係)
- [3. 同餘類](#3-同餘類)
  - [3.1 定義與例子](#31-定義與例子)
  - [3.2 各種記號](#32-各種記號)
  - [3.3 兩個類相等 ⇔ 代表元同餘](#33-兩個類相等--代表元同餘)
- [4. 同餘類的加減乘：well-defined](#4-同餘類的加減乘well-defined)
- [5. Z_n 與它的運算性質](#5-z_n-與它的運算性質)
- [6. 應用：數字判別法](#6-應用數字判別法)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

開始講**模運算**（modular arithmetic）：把整數換成它除以 $n$ 的餘數，在「餘數的世界」裡做加減乘。

| 主題 | 時間 | 課本 |
|---|---|---|
| 同餘的定義、$n\mid b-a$ | 00:01 | 定義、Lemma 3.1 |
| 等價關係 | 11:25 | Lemma 3.2 |
| 同餘類、記號 | 17:15 | p. 39–40 |
| 類相等 ⇔ 同餘 | 28:01 | p. 40 |
| 運算 well-defined | 35:33 | p. 40 |
| $\mathbb{Z}_n$ 的性質 | 44:56 | p. 40 |
| 數字判別法 | 50:59 | §2.4 |

講者用的編號（Proposition 4.11、4.12）是他自己講義的編號。

【口頭】以下約定：**$n$ 永遠是正整數**，沒說也一樣。$n=1$「大概可以但很蠢，基本上所有東西都是同一個點」。

---

## 1. 同餘的定義

### 1.1 定義：餘數相同

[▶ 00:01](https://youtu.be/_F8TN0rLjuc?t=1)

⚠️ 逐字稿缺字：開頭的定義字幕只剩「a is congruent... if a and b have same」。依接下來的證明（用「餘數相同」），定義是：

> **定義**：$a,b$ 是整數。若 $a$ 和 $b$ 除以 $n$ 的**餘數相同**，就說 $a$ **同餘**（congruent）於 $b$ 模 $n$，寫成
> $$a\equiv b\ (\mathrm{mod}\ n).$$

> 【課本補充】§3.1（p. 38）的定義相同：用除法演算法寫 $a=qn+r$、$b=q'n+r'$（$0\le r,r'<n$），$a\equiv b\ (\mathrm{mod}\ n)$ 就是 $r=r'$。課本也叫 $a$ 是 $b$ 模 $n$ 的**剩餘**（residue）。
>
> 課本開頭的兩個例子（p. 38）：
> - **100 天後星期幾？** $100 = 14\times 7+2$，所以跟 2 天後同一天。（$n=7$）
> - **$22051946$ 是平方數嗎？** 平方數除以 4 只會餘 0 或 1（第 3 集 Example 1.2）。$22051946 = 220519\times 100+46$，而 $100$ 是 4 的倍數，所以它除以 4 的餘數跟 $46$ 一樣，是 $2$。所以**不是**平方數。

### 1.2 等價說法：n 整除差

[▶ 01:03](https://youtu.be/_F8TN0rLjuc?t=63)

> **定理**：$a\equiv b\ (\mathrm{mod}\ n) \iff n\mid b-a$。

【口頭】講者其實**比較喜歡把這個當定義**：$a$ 和 $b$ 同餘，就是它們差一個 $n$ 的倍數，
$$b - a = nk,\qquad\text{或者更好：}\qquad b = a+nk\quad(k\in\mathbb{Z}).$$
「老實說我就是這樣想的：**從一個加上 $n$ 的某個倍數，可以走到另一個**。」

**證明 (⇒)** [▶ 03:07](https://youtu.be/_F8TN0rLjuc?t=187)

設 $a\equiv b$，用除法演算法：$a = q_1n+r$、$b=q_2n+r$（**同一個** $r$，因為假設餘數相同）。則
$$b-a = (q_2n+r)-(q_1n+r) = (q_2-q_1)\,n.$$
$r$ 消掉了，所以 $n\mid b-a$。

**證明 (⇐)** [▶ 04:49](https://youtu.be/_F8TN0rLjuc?t=289)

設 $n\mid b-a$，即 $b-a = nk$。用除法演算法：
$$a = q_1n+r_1,\qquad b=q_2n+r_2,\qquad 0\le r_1,r_2<n.$$

1. 算 $b-a$ [▶ 06:52](https://youtu.be/_F8TN0rLjuc?t=412)：
   $$b-a = (q_2-q_1)\,n + (r_2-r_1).$$
2. 它也等於 $nk$，所以
   $$(q_2-q_1-k)\,n = r_1-r_2.$$
3. 取絕對值 [▶ 08:48](https://youtu.be/_F8TN0rLjuc?t=528)。講者畫數線：$r_1,r_2$ 都在 $[0,n)$ 裡，所以它們的距離
   $$|r_1-r_2| < n.$$
4. **關鍵一步** [▶ 09:51](https://youtu.be/_F8TN0rLjuc?t=591)：左邊是 $n$ 乘以一個整數。如果那個整數不是 0，左邊的絕對值 $\ge n$，跟第 3 步矛盾。所以 $q_2-q_1-k=0$，於是 $r_1-r_2=0$，$r_1=r_2$。∎

【口頭】「證過這個很好，因為有時候能直接說『$a,b$ 同餘因為它們餘數一樣』真的很方便。」

> 【課本補充】§3.1 Lemma 3.1（p. 39）陳述 $n\mid(a-b)$（差的方向相反，因為 $n\mid x\iff n\mid -x$，無所謂）。證明一樣，課本的說法：「$-n$ 和 $n$ 之間（不含端點）唯一被 $n$ 整除的整數是 $0$。」

---

## 2. 同餘是等價關係

[▶ 11:25](https://youtu.be/_F8TN0rLjuc?t=685)

【口頭】從這裡起，同一段計算若都是模 $n$，講者就不每次寫「mod $n$」，在段落開頭講一次就好。

> **命題**：對所有整數 $x,y,z$（模 $n$）：
> 1. **反身性**（reflexive）：$x\equiv x$。
> 2. **對稱性**（symmetric）：$x\equiv y \Rightarrow y\equiv x$。
> 3. **遞移性**（transitive）：$x\equiv y$ 且 $y\equiv z \Rightarrow x\equiv z$。
>
> **推論**：模 $n$ 同餘是 $\mathbb{Z}$ 上的**等價關係**（equivalence relation）。

**證明**（都用 1.2 的定理：$n$ 整除差就同餘）[▶ 13:32](https://youtu.be/_F8TN0rLjuc?t=812)

1. $x-x = 0 = n\cdot 0$，所以 $n\mid x-x$，$x\equiv x$。
2. $x\equiv y$ ⇒ $y-x = nk$ ⇒ $x-y = n(-k)$ ⇒ $y\equiv x$。
3. $y-x = nk_1$、$z-y = nk_2$ ⇒
   $$z-x = (z-y)+(y-x) = nk_2+nk_1 = n(k_1+k_2)$$
   ⇒ $x\equiv z$。∎

【口頭】「如果我聰明一點，這些就是兩堂課前整除的論證，可以直接套。」

> 【課本補充】§3.1 Lemma 3.2（p. 39）就是這三條，證明各一行：$n\mid(a-a)$；$n\mid(a-b)\Rightarrow n\mid(b-a)$；$n\mid(a-b)$、$n\mid(b-c)$ ⇒ $n\mid(a-b)+(b-c)=a-c$。

---

## 3. 同餘類

### 3.1 定義與例子

[▶ 17:15](https://youtu.be/_F8TN0rLjuc?t=1035)

【課堂討論】講者問「等價關係對集合做了什麼？」學生答：**把集合切成不相交的等價類**（partition）。

> **定義**：$x$ 的**同餘類**（congruence class，等價類）
> $$[x] = \{\,y\in\mathbb{Z} : y\equiv x\ (\mathrm{mod}\ n)\,\} = \{\,x+nk : k\in\mathbb{Z}\,\}.$$
> $x$ 叫這個類的**代表元**（representative）。

第二個寫法就是「從 $x$ 加上 $n$ 的倍數能走到的所有數」。

**例子：模 2** [▶ 20:29](https://youtu.be/_F8TN0rLjuc?t=1229)——「從小學就跟著我們」的偶數與奇數：

$$[0] = \{0+2k\} = \{0,\pm2,\pm4,\dots\} = \text{偶數},\qquad [1] = \{1+2k\} = \{\pm1,\pm3,\pm5,\dots\} = \text{奇數}.$$

- **代表元不唯一**：$[0]=[2]$，$[1]=[-71]$（「來點怪的」）。
- $[0]\cup[1] = \mathbb{Z}$（每個整數不是偶數就是奇數）。
- $[0]\cap[1] = \varnothing$。

> **分割**（partition）[▶ 22:02](https://youtu.be/_F8TN0rLjuc?t=1322)：一群兩兩不相交的集合，聯集是整個集合。

**例子：模 4** [▶ 22:32](https://youtu.be/_F8TN0rLjuc?t=1352)：四個類 $[0],[1],[2],[3]$，分別是 $4k$、$4k+1$、$4k+2$、$4k+3$ 型的整數。互不相交，聯集是 $\mathbb{Z}$。

（第 6 集的「$4q+3$ 型質數」就是類 $[3]$ 裡的質數。）

> 【課本補充】p. 40：模 $n$ 恰好有 **$n$ 個**同餘類 $[0],[1],\dots,[n-1]$，對應除以 $n$ 的 $n$ 種可能餘數。沒有別的了，例如 $[n]=[0]$。$n=1$ 時所有整數都同餘，只有一個類 $\mathbb{Z}$。

### 3.2 各種記號

講者一路換了好幾種記號：

| 記號 | 意思 | 優缺點 |
|---|---|---|
| $\{y : y\equiv x\}$ | 集合寫法 | 最原始 |
| $[x]$ | 等價類 | **看不出模數** $n$ |
| $n\mathbb{Z}+x$ 或 $x+n\mathbb{Z}$ | **陪集**（coset）記號 [▶ 23:46](https://youtu.be/_F8TN0rLjuc?t=1426) | 模數一目瞭然 |
| $[x]_n$ | 加下標 [▶ 26:55](https://youtu.be/_F8TN0rLjuc?t=1615) | 同時用好幾個模數時用 |
| $\bar x$ | 上面加橫線 [▶ 46:41](https://youtu.be/_F8TN0rLjuc?t=2801) | 最好寫 |
| $x$ | 什麼都不加 | 「最後我們就直接寫 $x$」 |

**陪集記號的意思** [▶ 24:51](https://youtu.be/_F8TN0rLjuc?t=1491)：

- $n\mathbb{Z} = \{nk : k\in\mathbb{Z}\}$，$n$ 的所有整數倍。
- 一個集合 $S$ 加一個數 $k$：$S+k = \{s+k : s\in S\}$，每個元素都加 $k$。

【口頭】「這種知識能救一些大學生：在別的課他們寫出模糊沒意義的東西，我們會說『你不能把數加到集合上——除非你先定義』。」寫 $4\mathbb{Z}+1$ 還是 $1+4\mathbb{Z}$，在群論裡跟左陪集、右陪集有關，這裡只是風格問題。例如 $4\mathbb{Z}+1$ 和 $4\mathbb{Z}+5$ 是同一個集合。

**為什麼要標模數** [▶ 26:55](https://youtu.be/_F8TN0rLjuc?t=1615)：$[3]_3 = [0]_3$（3 除以 3 餘 0），但 $[3]_9\neq[0]_9$。只寫「$[3]$」會分不清。「模數重要時就把它標出來，這沒什麼深的。」

### 3.3 兩個類相等 ⇔ 代表元同餘

[▶ 28:01](https://youtu.be/_F8TN0rLjuc?t=1681)

> **命題**（講者 Prop 4.11）：$[x]=[y] \iff x\equiv y\ (\mathrm{mod}\ n)$。

【口頭】「如果有好好上過證明入門課，這早該講過了。這只是關於等價類的敘述，跟同餘的結構無關。」

**證明 (⇒)** [▶ 29:17](https://youtu.be/_F8TN0rLjuc?t=1757)：$[x]=[y]$，特別是 $[x]\subseteq[y]$。$x\equiv x$，所以 $x\in[x]\subseteq[y]$，也就是 $x\equiv y$。

**證明 (⇐)** [▶ 30:52](https://youtu.be/_F8TN0rLjuc?t=1852)：設 $x\equiv y$。任取 $z\in[x]$，則 $z\equiv x$（對稱性讓方向無所謂）。又 $x\equiv y$，由遞移性 $z\equiv y$，所以 $z\in[y]$。這證明 $[x]\subseteq[y]$。對稱地 $[y]\subseteq[x]$。所以 $[x]=[y]$。∎

**用途** [▶ 33:30](https://youtu.be/_F8TN0rLjuc?t=2010)：可以隨意**加減模數的倍數**，不改變類：

$$3+4\mathbb{Z} = 7+4\mathbb{Z};\qquad\text{模 } 11:\quad [20] = [9] = [-2].$$

---

## 4. 同餘類的加減乘：well-defined

[▶ 35:33](https://youtu.be/_F8TN0rLjuc?t=2133)

> **命題**（講者 Prop 4.12）：若 $[x]=[x']$ 且 $[y]=[y']$（模 $n$），則
> 1. $[x+y] = [x'+y']$
> 2. $[xy] = [x'y']$
> 3. $[x-y] = [x'-y']$
>
> 用陪集記號：$x+y+n\mathbb{Z} = x'+y'+n\mathbb{Z}$，其餘類推。

白話：**換一個代表元，加減乘的結果還是同一個類。**

**證明** [▶ 37:44](https://youtu.be/_F8TN0rLjuc?t=2264)：由 3.3，$x'=x+nk_1$、$y'=y+nk_2$。

1. **加法**：
   $$x'+y' = (x+nk_1)+(y+nk_2) = (x+y)+n(k_1+k_2).$$
   所以 $x'+y'\equiv x+y$，由 3.3，$[x'+y']=[x+y]$。
2. **乘法** [▶ 39:54](https://youtu.be/_F8TN0rLjuc?t=2394)：
   $$x'y' = (x+nk_1)(y+nk_2) = xy + n\,(k_1y+k_2x+nk_1k_2).$$
   所以 $x'y'\equiv xy$，$[x'y']=[xy]$。
3. 減法類似。∎

（講者把括號裡那串叫「笑臉」，畫出來被說像小精靈。）

> **定義（模運算）**[▶ 42:11](https://youtu.be/_F8TN0rLjuc?t=2531)：
> $$[x]+[y] = [x+y],\qquad [x]\cdot[y] = [xy].$$
> 陪集記號：$(x+n\mathbb{Z})+(y+n\mathbb{Z}) = x+y+n\mathbb{Z}$。（也可以加上減法。）

**為什麼需要上面的命題** [▶ 43:52](https://youtu.be/_F8TN0rLjuc?t=2632)：這個定義是**用代表元**定義的。如果換成別的代表元 $x',y'$ 會得到不同的類，那「$[x]+[y]$」就不是單一的值，**不是一個函數**。Prop 4.12 正好保證不會這樣——加法和乘法是 **well-defined**（定義良好）的。

> 【課本補充】p. 40 用同樣方式定義 $[a]+[b]$、$[a]-[b]$、$[a][b]$。課本特別說**除法**先不談：$a/b$ 不一定是整數，就沒有「$[a/b]$」可用。（除法在第 8 集起。）

---

## 5. Z_n 與它的運算性質

[▶ 44:56](https://youtu.be/_F8TN0rLjuc?t=2696)

> **定義**：模 $n$ 的同餘類全體記作
> $$\mathbb{Z}/n\mathbb{Z},\qquad\text{簡寫 } \mathbb{Z}_n.$$

模運算就是在 $\mathbb{Z}_n$ 上定義的加法和乘法。

**運算性質** [▶ 46:41](https://youtu.be/_F8TN0rLjuc?t=2801)（用 $\bar x$ 表示 $x$ 的類）：

| 性質 | 式子 |
|---|---|
| 加法交換 | $\bar x+\bar y = \bar y+\bar x$ |
| 乘法交換 | $\bar x\,\bar y = \bar y\,\bar x$ |
| 結合律 | $(\bar x+\bar y)+\bar z = \bar x+(\bar y+\bar z)$；$(\bar x\bar y)\bar z = \bar x(\bar y\bar z)$ |
| 分配律 | $\bar x(\bar y+\bar z) = \bar x\bar y+\bar x\bar z$ |
| 加法單位元素 | $\bar x+\bar 0 = \bar x$ |
| 乘法單位元素 | $\bar x\cdot\bar 1 = \bar x$ |

【口頭】「乘法可交換之後還寫兩條分配律，我一直覺得很蠢，但大家都這樣寫，我是同儕壓力的受害者。」

（這些都從 $\mathbb{Z}$ 的性質直接搬過來：例如 $\bar x+\bar y = \overline{x+y} = \overline{y+x} = \bar y+\bar x$。這一行**不是逐字稿內容**，是補上為什麼這些成立。）

**次方** [▶ 49:28](https://youtu.be/_F8TN0rLjuc?t=2968)：$\bar x\cdot\bar x = \overline{xx} = \overline{x^2}$。用歸納法，$\bar x^{\,k} = \overline{x^k}$。

⚠️ **注意**：**指數不能模 $n$ 化簡！** [▶ 50:29](https://youtu.be/_F8TN0rLjuc?t=3029) 底數可以隨便加減 $n$ 的倍數，但指數不行，「那邊發生的事比較複雜」。

> 以下**不是逐字稿內容**，是舉例說明為什麼指數不能直接模 $n$：模 $3$，$2^4 = 16\equiv 1$；但如果把指數 $4$ 換成 $4-3=1$，得 $2^1=2\not\equiv 1$。（指數真正的規則在第 9–12 集的群論和 Euler 定理。）

這些性質也都能用歸納法推廣到有限多項的和與積。

**【口頭】模運算到處都是** [▶ 50:59](https://youtu.be/_F8TN0rLjuc?t=3059)：

- 小孩說「2 + 2 = 12」？模某個數下可以讓它有意義。
- 【課堂討論】學生說：從開始數數就有模運算了，例如時間的循環。另一位學生說他在教三角函數，**同界角**（coterminal angles，差 $2\pi$ 或 $360°$ 的倍數）就是模運算的想法。

---

## 6. 應用：數字判別法

[▶ 52:05](https://youtu.be/_F8TN0rLjuc?t=3125)

**十進位表示**：一個整數 $x$ 寫成 $a_ka_{k-1}\cdots a_1a_0$（每個 $a_i$ 是 0 到 9 的數字），意思是
$$x = a_k\,10^k + a_{k-1}\,10^{k-1}+\cdots + a_1\,10 + a_0.$$

例子 [▶ 53:39](https://youtu.be/_F8TN0rLjuc?t=3219)：$352 = 3\cdot 10^2 + 5\cdot 10 + 2$，$a_2=3,a_1=5,a_0=2$。

【口頭】[▶ 56:05](https://youtu.be/_F8TN0rLjuc?t=3365) 講者一開始用 $n$ 表示這個整數，後來改成 $x$：「$n$ 完全是錯的字母，我想讓 $n$ 當模數。我中途換記號，大概是你們困惑的一半原因。」

**模 10** [▶ 54:12](https://youtu.be/_F8TN0rLjuc?t=3252)：$10^i\equiv 0$（$i\ge1$），所以
$$x\equiv a_0\ (\mathrm{mod}\ 10).$$
除以 10 的餘數就是**個位數**。（講者：「10 是最蠢的。」）

**模 9** [▶ 57:12](https://youtu.be/_F8TN0rLjuc?t=3432)：

1. **關鍵一步**：$10 = 1+9\equiv 1\ (\mathrm{mod}\ 9)$。
2. 所以 $10^k\equiv 1^k = 1$。
3. 所以
   $$x \equiv a_k+a_{k-1}+\cdots+a_1+a_0\ (\mathrm{mod}\ 9).$$

> **結論**：$x$ 除以 9 的餘數 = 各位數字和除以 9 的餘數。特別是：**$x$ 被 9 整除 ⇔ 數字和被 9 整除**。

例子 [▶ 58:19](https://youtu.be/_F8TN0rLjuc?t=3499)：

- $81$：$8+1=9$，是 9 的倍數。
- $54$：$5+4=9$，是 9 的倍數。
- $375$：$3+7+5=15\equiv 6\ (\mathrm{mod}\ 9)$。所以 $375$ 不是 9 的倍數，餘 6。（驗算：$375 = 41\cdot 9+6$。）

講者接著要講模 11（「11 也滿好的」），影片被切斷，接第 8 集。

> 【課本補充】§2.4（p. 32）用二項式定理得到同樣的結果：$10^i = (9+1)^i$ 展開後是 $9q+1$ 型，所以 $n = 9m + (a_k+\cdots+a_0)$。課本由此得到**被 3 整除 ⇔ 數字和被 3 整除**（因為 $3\mid 9$）。課本也說被 2 整除看 $a_0\in\{0,2,4,6,8\}$，被 5 整除看 $a_0\in\{0,5\}$。

---

## 7. 一頁速查表

**同餘**：$a\equiv b\ (\mathrm{mod}\ n)$ ⇔ 除以 $n$ 餘數相同 ⇔ $n\mid b-a$ ⇔ $b=a+nk$。

- **(⇐) 關鍵一步**：$(q_2-q_1-k)n = r_1-r_2$，右邊絕對值 $<n$，所以兩邊都是 0。

**等價關係**：反身、對稱、遞移。遞移的關鍵一步：$z-x=(z-y)+(y-x)$。

**同餘類**：$[x] = \{x+nk\} = x+n\mathbb{Z}$。模 $n$ 有 $n$ 個類 $[0],\dots,[n-1]$，兩兩不交，聯集是 $\mathbb{Z}$。

- $[x]=[y]$ ⇔ $x\equiv y$。
- 例：模 2 的類 = 偶數、奇數；模 11：$[20]=[9]=[-2]$。

**Well-defined**：$x'=x+nk_1$、$y'=y+nk_2$ ⇒

- $x'+y' = (x+y)+n(k_1+k_2)$
- $x'y' = xy+n(k_1y+k_2x+nk_1k_2)$

所以 $[x]+[y]=[x+y]$、$[x][y]=[xy]$ 不依代表元而定。

**$\mathbb{Z}_n=\mathbb{Z}/n\mathbb{Z}$**：加乘交換、結合、分配、有 $\bar0,\bar1$。$\bar x^{\,k}=\overline{x^k}$。**指數不能模 $n$。**

**數字判別法**：$x = \sum a_i10^i$。

- 模 10：$x\equiv a_0$。
- 模 9：$10\equiv1$ ⇒ $x\equiv\sum a_i$。例：$375\equiv 15\equiv 6$。
- 模 3：同模 9。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 模 11 的判別法、$\mathbb{Z}_n$ 的除法（乘法反元素） | 第 8 集 |
| 指數的規則（Fermat 小定理、Euler 定理） | 第 9–12 集 |
| 陪集 $x+n\mathbb{Z}$ | 第 9–10 集（群論、Lagrange 定理） |
| RSA：在 $\mathbb{Z}_n$ 裡算大次方 | 第 13–14 集 |
| 「模一個數」的推廣：商環 $R/I$ | 第 29–32 集 |

---

## 附：本集一句話總結

> **$a\equiv b\ (\mathrm{mod}\ n)$ 就是「餘數相同」，也就是「差是 $n$ 的倍數」。同餘是等價關係，把 $\mathbb{Z}$ 切成 $n$ 個同餘類；類的加法、乘法不依代表元而定，所以 $\mathbb{Z}_n$ 是個好的數系——只是指數不能模 $n$。**

---

*筆記依據 James S. Cook「Number Theory」2021-08-25 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與 Jones & Jones《Elementary Number Theory》§3.1、§2.4 整理。*
