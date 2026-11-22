---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 4
lecture: Lec04 Review A.1-A.4, A.5 Equivalence
date: 待補
video: https://youtu.be/neKmWc1DrRA
notes: Alajaji & Chen 附錄 A §A.3–A.5（pp. 266–271，Lemma A.16–Theorem A.28）
---

# 第 4 集 · Lec04 附錄 A：數列極限、limsup / liminf、sufficiently large / infinitely often、等價敘述 [▶ 影片](https://youtu.be/neKmWc1DrRA)

← 上一集：[03](03-suprema-and-limits.md) ｜ [總目錄](README.md) ｜ 下一集：[05](05-probability-random-processes-overview.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 4 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（35:46，whisper large-v3-turbo）＋ 課本附錄 A §A.3–A.5（pp. 266–271）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「實數」聽成「時數」，「supremum」聽成「Supremant／suprement」，「infimum」聽成「Inferment／infinite」，「monotone」聽成「Molotone／Morotone」，「limsup」聽成「limit soup／limit super」，「條件」聽成「乘數」，「block length」聽成「Black Lens／blocknet」，「正負無限大」聽成「政府無限大」，「趨近」聽成「區區」，「有界」聽成「有介」，「實變分析」聽成「十遍分析」，「高等微積分」聽成「高維」，「Neyman–Pearson lemma」聽成「Newman-Pearson-Lama」，「likelihood ratio」聽成「Like-Ratial」，「ε」聽成「Epson／absor／absin」，「Cover」聽成「Colver／Culver」，「Blahut」聽成「Brackhood／Blackheart」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：Shannon 的思路與 mutual information](#1-回顧shannon-的思路與-mutual-information)
- [2. Minkowski sum 與 threshold 型集合](#2-minkowski-sum-與-threshold-型集合)
- [3. 為什麼要談數列：block length](#3-為什麼要談數列block-length)
- [4. 極限與 ±∞](#4-極限與-)
- [5. Monotone convergence theorem](#5-monotone-convergence-theorem)
- [6. limsup 與 liminf](#6-limsup-與-liminf)
- [7. 直覺：最大和最小的群集點](#7-直覺最大和最小的群集點)
- [8. Sufficiently large 與 infinitely often](#8-sufficiently-large-與-infinitely-often)
- [9. limsup / liminf 的性質（Lemma A.27）](#9-limsup--liminf-的性質lemma-a27)
- [10. 等價敘述（Theorem A.28）](#10-等價敘述theorem-a28)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

先回顧 Shannon 的思路，然後把附錄 A 講完：數列的極限、**limsup／liminf**、**sufficiently large／infinitely often**，以及證明時常用的**等價敘述**（證 $x<y+\varepsilon$ 代替證 $x\le y$）。

| 主題 | 課本 |
|---|---|
| Minkowski sum、threshold 型集合 | §A.3（Lemma A.16、A.17，pp. 266–267） |
| 極限、monotone convergence | §A.4（Definition A.18、Property A.19、Lemma A.20，pp. 268–269） |
| limsup、liminf、群集點 | Definition A.21、Lemma A.22、Property A.23–A.24（pp. 269–270） |
| sufficiently large、infinitely often | Definition A.25–A.26（p. 270） |
| Lemma A.27、Theorem A.28 | pp. 270–271 |

---

## 1. 回顧：Shannon 的思路與 mutual information

[▶ 00:00](https://youtu.be/neKmWc1DrRA?t=0)

- Shannon 先問「什麼是 information」，用三個公設（monotonicity、additivity、continuity）定義；唯一滿足的公式是 entropy：
$$H(X)=\sum_x P_X(x)\log\frac1{P_X(x)}.$$
接收端 $Y$ 的訊息量 $H(Y)$ 也這樣算；聯合分布 $P_{XY}$ 給出 $H(X,Y)$。
- **共有的訊息量** [▶ 03:36](https://youtu.be/neKmWc1DrRA?t=216)：用集合論想。$H(X)$、$H(Y)$ 是兩個圈，交集是 $X$、$Y$ 共有的訊息量。集合裡「交集 = 兩個集合的量相加，扣掉聯集」，所以
$$I(X;Y)=H(X)+H(Y)-H(X,Y).$$

> ⚠️ 逐字稿缺字：原字幕「HXY − HX − HY」，符號順序反了；依集合論的推論（$|A\cap B|=|A|+|B|-|A\cup B|$），應為 $H(X)+H(Y)-H(X,Y)$。正式定義在第 8 集。

- 最後證明：傳送端和接收端**最大的共有訊息量**，就是這個通道最大的 reliable transmission rate。

【口頭】
- 一開始就「定理、證明、定理、證明」，會看不到背後的整個思維體系。PhD 的 P 就是 philosophy：能圓融、不自相矛盾地解釋一件事，形成理論體系，才是重要的貢獻。
- 老師寫書時放了兩個附錄（A、B），因為很多學生理解定理時準備不夠，或者有背景但不知道背後在工程上的意義。

---

## 2. Minkowski sum 與 threshold 型集合

[▶ 07:43](https://youtu.be/neKmWc1DrRA?t=463)

【Q&A】（老師轉述上週同學的問題）兩個實數集合的「相加」怎麼定義？
- 答：歷史上有很多定義，這裡用 **Minkowski sum**：$A+B=\{a+b:\ a\in A,\ b\in B\}$（即課本 Lemma A.16 的定義）。
- 消息理論用它，是因為實數通常是一個**指標**（例如傳送速度）。不同集合代表能達到的傳送速度，把速度相加，就是 Minkowski sum 的思維。

**Threshold 型集合的工程意義** [▶ 08:44](https://youtu.be/neKmWc1DrRA?t=524)：
- 【口頭】在數學所修實變分析時，只有定理、證明，不講應用。這門課要看這些數學形式在工程上為什麼有用。
- 工程上最常見的操作是「大於或小於一個常數」（threshold）。最常見的 $f$ 是 **likelihood ratio（概似比）**。
- **Neyman–Pearson lemma**（所有 detection 課本都有）：兩個 hypothesis A、B。「真的是 A 誤認為 B」是第一類錯誤，「真的是 B 誤認為 A」是第二類錯誤。這個引理證明：
  1. 不可能同時改善兩類錯誤率；
  2. **likelihood ratio test 一定可以是最好的**：兩個機率 $P$、$Q$ 相除取 log，跟一個 threshold 比大小，就能達到最好的錯誤率。工程實作非常方便。
- 這類決定性的函數常是 monotone increasing 或 decreasing。取一個範圍的最大值時，為了避免去找真正的最大值，就用 supremum——它在延伸實數裡一定存在，不用證明。再配合 Lemma A.17：「$<\varepsilon$ 取 sup」= 「$\ge\varepsilon$ 取 inf」。

---

## 3. 為什麼要談數列：block length

[▶ 11:19](https://youtu.be/neKmWc1DrRA?t=679)

- 消息理論的書裡 $n$ 通常代表 **block length（區塊長度）**：封包長度、框架長度、編碼長度。
- block length 越長，實作複雜度越高，但效能越好。
- $a_n$ 可能是長度 $n$ 的錯誤率。Shannon 那時候探討的都是**極限**：$n\to\infty$ 時錯誤率會不會趨近 0、收斂多快。
- Reliable transmission rate 就是「碼長到無限長時，錯誤率可以趨近 0」。

---

## 4. 極限與 ±∞

[▶ 12:50](https://youtu.be/neKmWc1DrRA?t=770)

**Definition A.18（極限）**（p. 268）：$L$ 是 $\{a_n\}$ 的極限，若
$$(\forall\varepsilon>0)(\exists N)(\forall n>N)\quad |a_n-L|<\varepsilon.$$
記 $L=\lim_{n\to\infty}a_n$。沒有這樣的 $L$，就說極限不存在。

**Property A.19**（p. 268）：$\{a_n\}$、$\{b_n\}$ 都在 $\mathbb R$ 有極限，則
1. $\lim(a_n+b_n)=\lim a_n+\lim b_n$；
2. $\lim(\alpha a_n)=\alpha\lim a_n$；
3. $\lim(a_nb_n)=(\lim a_n)(\lim b_n)$。

**注意 ±∞** [▶ 13:20](https://youtu.be/neKmWc1DrRA?t=800)：
- 這些在有限時都對；出問題通常是 $\pm\infty$ 跑進來的時候。定理條件寫 $\mathbb R$，就代表不是 $\pm\infty$；寫 $\mathbb R\cup\{\pm\infty\}$ 時要特別注意。
- 【口頭】老師審論文的例子：有人證出 $C_n=2C_n+3$，就推得 $C_n=-3$。但如果 $C_n$ 其實是無限大，「$\infty=\infty+3$」也成立，推論就錯了。**變數一定要有界才能這樣移項。**
- 傳統數學／機率書：$\pm\infty$ **不算**極限，叫 **diverge（發散）**。
- 消息理論的書（Verdú、Han、Cover）為了方便，有時把 $\pm\infty$ 納進來，因為證明時很難一開始就知道會不會衝到 $\pm\infty$。讀書時要注意作者的約定。
- 衝到 $\infty$ 的意思：任給一個數（300、500、2000、3 萬），數列夠後面一定會超過它。

【課本補充】課本（pp. 268–269）的約定：若 $(\forall L)(\exists N)(\forall n>N)\ a_n>L$，說 $a_n$ diverges to $\infty$；為了方便，本書在延伸實數裡工作，說這種數列在 $\mathbb R\cup\{-\infty,\infty\}$ 中有極限。

---

## 5. Monotone convergence theorem

[▶ 15:53](https://youtu.be/neKmWc1DrRA?t=953)

**Lemma A.20（單調數列收斂）**（p. 269）：
- $\{a_n\}$ 對 $n$ **非遞減** ⇒ $\lim a_n$ 在 $\mathbb R\cup\{\pm\infty\}$ 中存在。若還有上界（$a_n\le L$），極限在 $\mathbb R$ 中存在。
- 非遞增的情形對稱（有下界 ⇒ 極限在 $\mathbb R$）。

【口頭】把 $\pm\infty$ 當作合理的極限，條件就簡單：單調一定收斂，只是可能收斂到 $\pm\infty$。不想納入 $\pm\infty$，就要加「有界」。

**極限不存在的例子** [▶ 16:25](https://youtu.be/neKmWc1DrRA?t=985)：$a_n=(-1)^n$，在 $+1$、$-1$ 之間跳，沒有極限。所以要引進 limsup、liminf。

---

## 6. limsup 與 liminf

[▶ 16:55](https://youtu.be/neKmWc1DrRA?t=1015)

**Definition A.21**（p. 269）：
$$\limsup_{n\to\infty}a_n:=\lim_{n\to\infty}\left(\sup_{k\ge n}a_k\right),\qquad \liminf_{n\to\infty}a_n:=\lim_{n\to\infty}\left(\inf_{k\ge n}a_k\right).$$
也有人寫成 $\overline{\lim}$、$\underline{\lim}$。

**為什麼一定存在？** [▶ 17:25](https://youtu.be/neKmWc1DrRA?t=1045)
- $\sup_{k\ge n}a_k$ 是集合 $\{a_n,a_{n+1},a_{n+2},\dots\}$ 的最大（sup）。
- $n$ 增加時，前面的項被拿掉，集合變小。小集合的 sup ≤ 大集合的 sup（Lemma A.15）。【口頭】四個數字的最大一定 ≥ 三個數字的最大。
- 所以 $\sup_{k\ge n}a_k$ 對 $n$ **非遞增**；由 monotone convergence theorem，外面的 lim **一定存在**（可能是 $\pm\infty$）。
- 同理 $\inf_{k\ge n}a_k$ 對 $n$ 非遞減，liminf 也一定存在。
- 這就是引進它們的目的：**不用討論存在性**。

【口頭】抓到這些小重點，看論文就看得懂，審別人論文時也知道怎麼抓毛病。

**Lemma A.22**（p. 269）：
$$\lim_{n\to\infty}a_n=L\iff\limsup_{n\to\infty}a_n=\liminf_{n\to\infty}a_n=L.$$

---

## 7. 直覺：最大和最小的群集點

[▶ 19:29](https://youtu.be/neKmWc1DrRA?t=1169)

【口頭】不用數學，用工程直觀想：
- 把數列每一項打點在數線上，例如 $1,0,-1,0,1,0,-1,0,\dots$。有些點會很密集地聚集：以那個點為中心畫多小的圈，都有無限多個點落進去。這種點叫 **clustering point（群集點）**。
- 一個數列的群集點可能有無限多個（無限多點可以切出無限多個集合，每個裡面還是無限多點）。
- **limsup = 最大的群集點，liminf = 最小的群集點。**
- 上例：limsup $=1$，liminf $=-1$，一看就知道，不用證明。
- 例：$a_n=-n$，群集點一直往負的方向跑，limsup = liminf $=-\infty$。有的書說極限是 $-\infty$，有的說極限不存在（因為不把 $\pm\infty$ 當極限），兩種都對。

【課本補充】課本（p. 271）用同一個例子：$a_n=\sin(n\pi/2)$ 得 $\{1,0,-1,0,1,0,-1,0,\dots\}$，群集點是 $-1,0,1$，limsup $=1$，liminf $=-1$。

---

## 8. Sufficiently large 與 infinitely often

[▶ 22:07](https://youtu.be/neKmWc1DrRA?t=1327)

**Property A.23（limsup 的性質）**（pp. 269–270）：
1. limsup 在延伸實數中永遠存在。
2. 若 $|\limsup a_m|<\infty$，則 $(\forall\varepsilon>0)(\exists N)(\forall n>N)\ a_n<\limsup a_m+\varepsilon$。（**每一個** $n>N$ 都成立。）
3. 若 $|\limsup a_m|<\infty$，則 $(\forall\varepsilon>0,\ \forall K)(\exists N>K)\ a_N>\limsup a_m-\varepsilon$。（只保證**一個** $N>K$。）

**畫圖想** [▶ 22:38](https://youtu.be/neKmWc1DrRA?t=1358)：
- 在 limsup 上方加一點點 $\varepsilon$ 畫一條線：中間的點可能會超過，但**最終所有的點都落在這條線以下**。蓋不住的話，它就不是 limsup。
- 在 limsup 下方減 $\varepsilon$ 畫一條線：不能保證之後永遠在線上方，只能保證**任何位置之後至少還有一點**在線上方。如果某個位置之後一點都沒有，limsup 就會比 $\limsup-\varepsilon$ 還小，矛盾。
- 【口頭】Shannon 證 capacity 就是這樣：不知道極限存不存在，就「加一點、減一點」，證明它被夾在中間。

**名詞**（Definition A.25、A.26，p. 270）[▶ 24:39](https://youtu.be/neKmWc1DrRA?t=1479)：
- **Sufficiently large（almost always）**：某性質對所有 $n>N$ 成立（對某個 $N$）。
- **Infinitely often（infinitely many）**：對每個 $K$，都有一個 $N>K$ 使性質成立。

【口頭】例：看 $n>2$ 萬之後，找到一點（例如 28000）成立；看 30 萬之後，又在 41 萬找到一點成立……每次只保證一個，所以會出現無限多次，但不保證永遠成立，中間會一直違反。

所以 Property A.23 的 2、3 可以改寫成（$|\limsup a_m|<\infty$，$\forall\varepsilon>0$）：
$$a_n<\limsup a_m+\varepsilon\ \text{ for all sufficiently large }n,\qquad a_n>\limsup a_m-\varepsilon\ \text{ for infinitely many }n.$$

**Property A.24（liminf，對稱）**（p. 270）：
$$a_n<\liminf a_m+\varepsilon\ \text{ for infinitely many }n,\qquad a_n>\liminf a_m-\varepsilon\ \text{ for all sufficiently large }n.$$
老師的口訣：liminf「減一點是 sufficiently large，加一點是 infinitely many」。

【口頭】用語的歷史 [▶ 25:39](https://youtu.be/neKmWc1DrRA?t=1539)：
- 全世界最常用的 Cover & Thomas，以及 Blahut、Gallager 的書，大量用 sufficiently large。老師數過，書裡出現 38 次。
- Infinitely often 在 Cover 的書裡只出現**一次**：早期都希望證明一個性質在 block length 超過某長度之後**永遠**成立。
- 後來的書比較常談 infinitely often：通訊做到某個程度後，要「長度夠長就永遠成立」越來越難；退而求其次，在某些 block length 成立，至少那些長度可以用。
- 數位通訊的書（QPSK、QAM）幾乎看不到這種敘述；消息理論的書處處可見，因為**不知道從哪一點開始成立**。

**Capacity 的例子** [▶ 28:13](https://youtu.be/neKmWc1DrRA?t=1693)：真正證的是 limsup。例如要錯誤率小於 $10^{-20}$，Shannon 證的是「長度超過某個值（老師舉 8000，通常是好幾萬）之後，永遠小於 $10^{-20}$」，但不知道是 8000、9000 還是 1 萬開始。

---

## 9. limsup / liminf 的性質（Lemma A.27）

[▶ 28:43](https://youtu.be/neKmWc1DrRA?t=1723)

**Lemma A.27**（pp. 270–271）：
1. $\liminf a_n\le\limsup a_n$。（最小的群集點 ≤ 最大的群集點。）
2. 若 $a_n\le b_n$ for all sufficiently large $n$，則 $\liminf a_n\le\liminf b_n$ 且 $\limsup a_n\le\limsup b_n$。
   - 【口頭】「長度 $n$ 夠大時這個系統永遠比那個好」，就這樣敘述——不講從哪一點開始，因為 Shannon 他們也不知道。
3. $\limsup a_n<r$ ⇒ $a_n<r$ for all sufficiently large $n$。（**嚴格小於，沒有等號**；理由：取 $\varepsilon=r-\limsup a_n>0$，用 Property A.23 的 2。）
4. $\limsup a_n>r$ ⇒ $a_n>r$ for infinitely many $n$。
5. 
$$\liminf a_n+\liminf b_n\le\liminf(a_n+b_n)\le\limsup a_n+\liminf b_n\le\limsup(a_n+b_n)\le\limsup a_n+\limsup b_n.$$
   - 【口頭】用群集點想：分開取最大群集點再相加，一定 ≥ 先相加再取最大群集點。
6. 若 $\lim a_n$ 存在，則 $\liminf(a_n+b_n)=\lim a_n+\liminf b_n$，$\limsup(a_n+b_n)=\lim a_n+\limsup b_n$。

**等號什麼時候成立** [▶ 31:48](https://youtu.be/neKmWc1DrRA?t=1908)：老師說只要其中一個數列有極限（limsup = liminf），第 5 點的四個不等式中有三個會變等號，有一個不一定。

> 以下**不是逐字稿內容**，是依第 6 點推論：若 $\lim a_n$ 存在，則 $\liminf a_n=\limsup a_n=\lim a_n$，第 5 點變成 $\lim a+\liminf b=\liminf(a+b)=\lim a+\liminf b\le\limsup(a+b)=\lim a+\limsup b$。第 1、2、4 個不等號變等號，第 3 個（$\lim a+\liminf b\le\lim a+\limsup b$）只有 $b_n$ 也有極限時才是等號。

> 以下**不是逐字稿內容**，是補的例子（老師說投影片「都有範例」但沒唸）：$a_n=(-1)^n$、$b_n=(-1)^{n+1}$。$a_n+b_n=0$，所以 $\liminf(a+b)=\limsup(a+b)=0$；但 $\liminf a+\liminf b=-2<0$，$\limsup a+\limsup b=2>0$。第 5 點最左、最右兩個不等號是嚴格的。

【口頭】老師喜歡考「請舉個例子」：能造出例子就代表懂了。看到不等式，就要問等號什麼時候成立。limsup／liminf 微積分通常不教、高等微積分才教，所以這裡介紹一下。

---

## 10. 等價敘述（Theorem A.28）

[▶ 32:50](https://youtu.be/neKmWc1DrRA?t=1970)

reliable、sufficiently large 這些不只是描述性的詞，而是有嚴格數學意義的。下面這些敘述都是 if and only if。

**Theorem A.28**（p. 271）：對任意 $x,y,a\in\mathbb R$，
1. $x<y+\varepsilon$ 對**所有** $\varepsilon>0$ $\iff$ $x\le y$；
2. $x<y-\varepsilon$ 對**某個** $\varepsilon>0$ $\iff$ $x<y$；
3. $x>y-\varepsilon$ 對所有 $\varepsilon>0$ $\iff$ $x\ge y$；
4. $x>y+\varepsilon$ 對某個 $\varepsilon>0$ $\iff$ $x>y$；
5. $|a|<\varepsilon$ 對所有 $\varepsilon>0$ $\iff$ $a=0$。

**為什麼要這樣證** [▶ 33:20](https://youtu.be/neKmWc1DrRA?t=2000)：
- 要證 $x\le y$，消息理論通常**不直接證**，而是證「$x<y+\varepsilon$，$\varepsilon$ 任意」。
- 【口頭】直接證 $a\le3$ 時，「可能等於」的情形比較難處理；證 $a<3.1$ 比較容易，因為嚴格小於比較好取捨，可以在 $\varepsilon$ 上做拆解。接著證 $a<3.01$、$a<3.001$……整個步驟都對，$\varepsilon$ 又任意小，結論就是 $a\le3$。
- 同理，要證**嚴格**小於，只要證存在**一個** $\varepsilon$（some）使 $x<y-\varepsilon$；「對所有 $\varepsilon$」得到的是帶等號的版本。
- channel capacity 的證明五、六頁，裡面很多脈絡就是這樣做的。老師說這與其說是數學技巧，不如說是想法。

> 以下**不是逐字稿內容**，是第 1 點的證明（課本也沒證）：(⇐) $x\le y<y+\varepsilon$。(⇒) 若 $x>y$，取 $\varepsilon=x-y>0$，得 $x<y+(x-y)=x$，矛盾。

**附錄 A 總結** [▶ 34:52](https://youtu.be/neKmWc1DrRA?t=2092)：supremum 的原始定義和直觀、limsup／liminf 和常見性質、為什麼敘述喜歡用 sufficiently large 和 infinitely often。

---

## 11. 一頁速查表

**極限**
- $\lim a_n=L$：$(\forall\varepsilon)(\exists N)(\forall n>N)\ |a_n-L|<\varepsilon$。和、純量倍、乘積的極限可拆（極限有限時）。
- 小心 $\pm\infty$：$C_n=2C_n+3\Rightarrow C_n=-3$ 只在 $C_n$ 有限時成立。
- **Monotone convergence**：單調 ⇒ 極限在 $\mathbb R\cup\{\pm\infty\}$ 存在；再加有界 ⇒ 在 $\mathbb R$。

**limsup / liminf**
- $\limsup a_n=\lim_n\sup_{k\ge n}a_k$：$\sup_{k\ge n}a_k$ 隨 $n$ 非遞增 ⇒ 一定存在。liminf 對稱。
- $\lim a_n=L\iff\limsup=\liminf=L$。
- 直覺：最大／最小的群集點。$1,0,-1,0,\dots$：limsup $=1$，liminf $=-1$。

**Sufficiently large / infinitely often**（$|\limsup a|<\infty$）
- $a_n<\limsup a+\varepsilon$ for all sufficiently large $n$（上方的線最終蓋住全部）。
- $a_n>\limsup a-\varepsilon$ for infinitely many $n$（下方的線之上永遠還有點）。
- liminf：加 $\varepsilon$ → infinitely often；減 $\varepsilon$ → sufficiently large。

**Lemma A.27**
- $\limsup a<r\Rightarrow a_n<r$ eventually；$\limsup a>r\Rightarrow a_n>r$ i.o.
- $\liminf a+\liminf b\le\liminf(a+b)\le\limsup a+\liminf b\le\limsup(a+b)\le\limsup a+\limsup b$。
- 反例：$a_n=(-1)^n$、$b_n=-a_n$ ⇒ 兩端嚴格。

**Theorem A.28（證明技巧）**
- 證 $x\le y$ ⟸ 證 $x<y+\varepsilon$ $\forall\varepsilon>0$（反證：取 $\varepsilon=x-y$）。
- 證 $x<y$ ⟸ 找一個 $\varepsilon>0$ 使 $x<y-\varepsilon$。
- $|a|<\varepsilon\ \forall\varepsilon\iff a=0$。

**Neyman–Pearson**：兩類錯誤不能同時改善；likelihood ratio test（$\log\frac PQ$ 比 threshold）是最好的。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 機率、隨機過程的基礎（附錄 B） | 第 5–7 集 |
| $I(X;Y)=H(X)+H(Y)-H(X,Y)$ 的正式定義 | 第 8 集（§2.2） |
| Neyman–Pearson、hypothesis testing | 第 11 集（§2.8） |
| sufficiently large、limsup 的錯誤率敘述 | 第 12 集（source coding theorem）、第 16–18 集（channel coding theorem） |
| $x<y+\varepsilon\Rightarrow x\le y$ 的證明手法 | 第 12、16–18、28 集的定理證明 |
| infinitely often、limsup/liminf 的一般化 | 第 32–35 集（第二部分） |

---

## 附：本集一句話總結

> **極限不一定存在，但 limsup／liminf 永遠存在（最大／最小的群集點）；消息理論的證明就靠「加一點 ε、減一點 ε」把目標夾住，並用 sufficiently large、infinitely often 精確地說「從某處以後永遠成立」或「一直會再成立」。**

---

*筆記依據陳伯寧老師「消息理論」Lec04 錄影逐字稿（whisper large-v3-turbo，35:46）與 Alajaji & Chen 課本附錄 A §A.3–A.5 整理。*
