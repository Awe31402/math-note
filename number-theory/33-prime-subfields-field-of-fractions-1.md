---
course: Number Theory（2021 秋，線上錄影）
episode: 33
lecture: 2021-10-27 第 1 部
date: 2021-10-27
video: https://youtu.be/zqSMBhwWN4c
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.4 Lecture 24（p. 139–141）：Theorem 4.4.10、Corollary 4.4.11–4.4.13、Definition 4.4.14、Theorem 4.4.15（分式體的構造）；講義說構造照 Gallian p. 277–278
---

# 第 33 集 · 質子體、分式體的構造（上）（Prime Subfields, Field of Fractions Construction, Part 1） [▶ 影片](https://youtu.be/zqSMBhwWN4c)

← 上一集：[32-prime-maximal-ideal-theorems-2](32-prime-maximal-ideal-theorems-2.md) ｜ [總目錄](README.md) ｜ 下一集：[34-prime-subfields-field-of-fractions-2](34-prime-subfields-field-of-fractions-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 33 集（2021-10-27 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；結尾被切斷）＋ 講者講義 §4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. n ↦ n·1 是環同態](#1-n--n1-是環同態)
- [2. 每個環裡都藏著 Z_n 或 Z](#2-每個環裡都藏著-z_n-或-z)
- [3. Steinitz 定理與質子體](#3-steinitz-定理與質子體)
- [4. 分式體：想法](#4-分式體想法)
- [5. Step 1：形式分數與等價關係](#5-step-1形式分數與等價關係)
- [6. Step 2：加法、乘法是 well-defined 的](#6-step-2加法乘法是-well-defined-的)
- [7. Step 3：零、一、反元素](#7-step-3零一反元素)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/zqSMBhwWN4c?t=5)

還在講環同態，接著要講**質子體**和**分式體**——講者第 32 集說的「這部分課程的高潮之一」：用嚴格數學**造出有理數**。

| 主題 | 時間 | 講義 |
|---|---|---|
| $n\mapsto n\cdot1$ | 00:36 | Thm 4.4.10 |
| 環裡的 $\mathbb{Z}_n$ 或 $\mathbb{Z}$ | 04:14 | Cor 4.4.11 |
| $\mathbb{Z}\to\mathbb{Z}_m$ | 11:44 | Cor 4.4.12 |
| Steinitz 定理、質子體 | 14:34 | Cor 4.4.13、Def 4.4.14 |
| 分式體 | 20:22 | Thm 4.4.15 |

---

## 1. n ↦ n·1 是環同態

[▶ 00:36](https://youtu.be/zqSMBhwWN4c?t=36)

> **定理**（講義 Theorem 4.4.10）：若 $R$ 是有單位元素 1 的環，則
> $$\varphi:\mathbb{Z}\to R,\qquad\varphi(n) = n\cdot1$$
> 是環同態。

（$n\cdot 1$ = 1 自己加 $n$ 次；$n$ 是負的就加 $-1$。）

要證三件事 [▶ 01:38](https://youtu.be/zqSMBhwWN4c?t=98)，翻成這個 $\varphi$ 就是：
$$(m+n)\cdot1 = m\cdot1+n\cdot1,\qquad(mn)\cdot1 = (m\cdot1)(n\cdot1),\qquad 1\cdot 1 = 1.$$

講者說細節「相當繁瑣」（要用遞迴定義），不做；Gallian 有明確的證明。

【口頭】[▶ 03:14](https://youtu.be/zqSMBhwWN4c?t=194) **別被記號騙了**：$\varphi(1) = 1$ 左邊的 1 是**整數** 1，右邊的 1 是 $R$ 的單位元素——可能是矩陣、多項式、各種東西。「兩個我都寫 1，小心。」

> 【講義補充】Theorem 4.4.10（p. 139）說證明在 Gallian p. 274–275。

---

## 2. 每個環裡都藏著 Z_n 或 Z

[▶ 04:14](https://youtu.be/zqSMBhwWN4c?t=254)

> **推論**（講義 Corollary 4.4.11）：$R$ 是環。
> - 若 $\mathrm{char}(R) = n>0$，$R$ 有一個子環同構於 $\mathbb{Z}_n$。
> - 若 $\mathrm{char}(R) = 0$，$R$ 有一個子環同構於 $\mathbb{Z}$。

（**特徵**，第 28 集：1 加自己幾次會變 0；永遠不會就是 0。例：$\mathbb{Z}_n$ 特徵 $n$，$\mathbb{Z}$ 特徵 0。）

**證明** [▶ 06:22](https://youtu.be/zqSMBhwWN4c?t=382)：令
$$S = \{\,k\cdot 1 : k\in\mathbb{Z}\,\}$$
（1 的所有倍數）。這正是第 1 節 $\varphi$ 的**像**。

**核** [▶ 07:23](https://youtu.be/zqSMBhwWN4c?t=443)：$\ker\varphi = \{k\in\mathbb{Z} : k\cdot1 = 0\}$。

- 特徵 $n$：$k\cdot 1 = 0\iff n\mid k$，所以 $\ker\varphi = n\mathbb{Z}$。
- 特徵 0：只有加 0 次才是 0，$\ker\varphi = \{0\}$。

**第一同構定理**（第 32 集）[▶ 08:36](https://youtu.be/zqSMBhwWN4c?t=516)：$\mathbb{Z}/\ker\varphi\cong\varphi(\mathbb{Z}) = S$。

- 特徵 $n$：$\mathbb{Z}/n\mathbb{Z} = \mathbb{Z}_n\cong S$。
- 特徵 0：$\mathbb{Z}/\{0\}\cong S$，而 $\mathbb{Z}/\{0\}\cong\mathbb{Z}$。∎

【口頭】[▶ 10:42](https://youtu.be/zqSMBhwWN4c?t=642) $R/\{0\}\cong R$「很容易證，但模掉零很討厭」：形式上它只是把每個元素包進大括號——等價類都是單元素集合。嚴格說不是同一個物件，「但就代數而言，$R/\{0\}$ 就是 $R$」。

> **推論**（講義 Corollary 4.4.12）[▶ 11:44](https://youtu.be/zqSMBhwWN4c?t=704)：$\varphi:\mathbb{Z}\to\mathbb{Z}_m$，$\varphi(x) = [x]_m = x+m\mathbb{Z}$ 是環同態。

講者：這我們早就知道了；這個推論的重點是說「它也是第 1 節那種構造的例子」，因為
$$[x]_m = x\cdot[1]_m.$$
例如 $[3]_7 = [1]_7+[1]_7+[1]_7 = 3\cdot[1]_7$。（講者：「我開始後悔這個記號了，還好我們平常不用方括號加下標，算起來很笨重。」）

> 【講義補充】Corollary 4.4.12 後面（p. 139）：「$[x]_m = x\cdot[1]_m$」這個計算觀察是很多題目的核心，例如為什麼從 $\mathbb{Z}_n$ 到 $\mathbb{Z}_k$ 的同態都長成 $[x]_n\mapsto[mx]_k$。

---

## 3. Steinitz 定理與質子體

[▶ 14:34](https://youtu.be/zqSMBhwWN4c?t=874)

> **推論（Steinitz，1910）**（講義 Corollary 4.4.13）：
> - 若 $F$ 是特徵 $p$ 的體，$F$ 有一個子體同構於 $\mathbb{Z}_p$。
> - 若 $F$ 是特徵 0 的體，$F$ 有一個子體同構於 $\mathbb{Q}$。

（第 28 集：整環——所以體——的特徵只能是 0 或質數 $p$。）

**構造** [▶ 15:47](https://youtu.be/zqSMBhwWN4c?t=947)：用第 2 節的 $S = \{k\cdot1\}$，令
$$S_{\mathbb{Q}} = \{\,ab^{-1} : a,b\in S,\ b\neq0\,\}.$$
$F$ 是體，非零元素都有反元素，所以這有意義。特徵 0 時它同構於 $\mathbb{Q}$；特徵 $p$ 時同樣的寫法同構於 $\mathbb{Z}_p$。

講者：「這是推論，大概有更巧妙的證明。我對證明沒那麼有興趣——不是說它難，是我想往下走。」重點是它讓我們能做下面的定義：

> **定義**（講義 Definition 4.4.14）[▶ 18:35](https://youtu.be/zqSMBhwWN4c?t=1115)：體 $F$ 中**被所有其他子體包含**的那個子體，叫 $F$ 的**質子體**（prime subfield）。

**由 Steinitz 定理：質子體在同構意義下只能是 $\mathbb{Z}_p$ 或 $\mathbb{Q}$** [▶ 18:35](https://youtu.be/zqSMBhwWN4c?t=1115)。

**為什麼** [▶ 19:15](https://youtu.be/zqSMBhwWN4c?t=1155)：

- 任何子體都含 1。
- 有了 1，就能把 1 一直加自己，造出這個體的「整數」；在體裡又能取反元素。
- 所以任何子體都自動包含 $S_{\mathbb{Q}}$（或 $S_{\mathbb{Z}_p}$）。「**有了 1，就逃不掉**。」

> 【講義補充】Definition 4.4.14 後面（p. 139）：特徵 0 的體，最小的子體是 $\mathbb{Q}$；特徵 $p$ 的體，最小的子體是 $\mathbb{Z}_p$。

---

## 4. 分式體：想法

[▶ 20:22](https://youtu.be/zqSMBhwWN4c?t=1222)

講者：「現在的重頭戲：分式體。」

> **定理**（講義 Theorem 4.4.15）：$D$ 是整環，則存在一個體 $F$，它有一個子環同構於 $D$。這個 $F$ 叫 $D$ 的**分式體**（field of fractions）。

【課堂討論】[▶ 22:07](https://youtu.be/zqSMBhwWN4c?t=1327) 講者問整環是什麼？學生：可交換、有單位元素、**沒有零因子**。講者：「沒有零因子是大的那個。」

**幕後的想法** [▶ 22:40](https://youtu.be/zqSMBhwWN4c?t=1360)：我們熟悉有理數，
$$\frac ab = \frac cd\iff ad = bc.$$
我們要**把有理數的構造形式化**。

- **不寫分數**：用分數記號會讓人覺得「在假設我們要證的東西」。講者說這是一種「成年禮」：說服自己沒有偷偷假設。
- 改寫成**有序對** $(a,b)$，暫時代表「$a/b$」，並規定 $(a,b)\sim(c,d)\iff ad = bc$。

> 【講義補充】講義（p. 140）說構造照 Gallian p. 277–278，「我可能會改一下記號。Gallian 的記號是我們最終要用的，但一開始要跟熟悉的東西切割，免得假設了不該假設的」。講義腳註：「是的，直覺上我們想讓 $(a,b)$ 代表分數 $a/b$，不管那是什麼意思……當然 $a/b = c/d$ 給出 $ad = bc$，所以這樣定義。」

---

## 5. Step 1：形式分數與等價關係

[▶ 24:42](https://youtu.be/zqSMBhwWN4c?t=1482)

令
$$S = \{\,(a,b) : a,b\in D,\ b\neq 0\,\}$$
——「形式分數的集合」（$D$ 不必是實數或複數，只是個整環）。定義
$$(a,b)\sim(c,d)\iff ad = bc.$$

**第一件事：證明 $\sim$ 是等價關係**，因為分式體會是**等價類的集合**。

- **反身** [▶ 26:14](https://youtu.be/zqSMBhwWN4c?t=1574)：$(a,b)\sim(a,b)$ 因為 $ab = ba$（可交換）。
- **對稱** [▶ 26:46](https://youtu.be/zqSMBhwWN4c?t=1606)：$ad = bc$ ⇒ $cb = da$ ⇒ $(c,d)\sim(a,b)$。（講者一度搞混字母，「我有一個解釋危機，從中間碰頭吧」。）
- **遞移** [▶ 29:02](https://youtu.be/zqSMBhwWN4c?t=1742)：設 $ad = bc$、$cf = de$，要證 $af = be$。

**遞移的證明**（講者照講義抄，「這種東西很容易迷路」）[▶ 30:35](https://youtu.be/zqSMBhwWN4c?t=1835)：
$$(ad)f = (bc)f = b(cf) = b(de).$$
可交換，所以 $(af)d = (be)d$。

**為什麼能消掉 $d$？** [▶ 31:48](https://youtu.be/zqSMBhwWN4c?t=1908)【課堂討論】不能除——「我們不知道任何東西是單位」。$(c,d)\in S$，所以 $d\neq 0$；**$D$ 是整環，有消去律**（第 27–28 集）。所以 $af = be$。

講者：「**這就是為什麼需要整環**——遞移性要用到它，在這之前都沒用到。」

**等價類** [▶ 33:51](https://youtu.be/zqSMBhwWN4c?t=2031)：
$$[a,b] = \{\,(c,d)\in S : (c,d)\sim(a,b)\,\}.$$
方括號是等價類，$F = S/\!\sim$ 是等價類的集合——「一個集合的集合」。

---

## 6. Step 2：加法、乘法是 well-defined 的

[▶ 35:34](https://youtu.be/zqSMBhwWN4c?t=2134)

**幕後的想法**：小時候學的分數，
$$\frac ab+\frac cd = \frac{ad+bc}{bd},\qquad\frac ab\cdot\frac cd = \frac{ac}{bd}.$$

所以**定義** [▶ 36:07](https://youtu.be/zqSMBhwWN4c?t=2167)：
$$[a,b]+[c,d] = [ad+bc,\ bd],\qquad [a,b]\,[c,d] = [ac,\ bd].$$

$b,d\neq 0$，整環裡 $bd\neq 0$，所以右邊還在 $S$ 裡，「好兆頭」。

**要檢查 well-defined** [▶ 37:17](https://youtu.be/zqSMBhwWN4c?t=2237)：元素的標籤不唯一，規則不能依標籤而定。設
$$[a,b] = [a',b'],\quad [c,d] = [c',d'],\qquad\text{即}\qquad ab' = ba',\quad cd' = dc'.$$

**加法**：要證 $(a'd'+b'c',\ b'd')\sim(ad+bc,\ bd)$，也就是
$$(ad+bc)\,b'd' = bd\,(a'd'+b'c').$$
講者照講義算 [▶ 42:33](https://youtu.be/zqSMBhwWN4c?t=2553)：
$$(ad+bc)\,b'd' = (ab')(dd')+(cd')(bb') = (ba')(dd')+(dc')(bb') = bd\,(a'd'+b'c').$$
第二個等號**兩個假設都用上**。講者：「其實不難，只要找到用上你手上東西的方法。」

（講者說這種證明「需要再多兩塊黑板」，也抱怨自己「在證明中間寫出要證的東西」——「你們這樣做我很抓狂，我現在也在做，很壞的習慣」。）

**乘法** [▶ 45:25](https://youtu.be/zqSMBhwWN4c?t=2725)：要證 $(ac)(b'd') = (bd)(a'c')$。
$$(ac)(b'd') = (ab')(cd') = (ba')(dc') = (bd)(a'c').$$
所以乘法跟代表元無關。

講者 [▶ 47:39](https://youtu.be/zqSMBhwWN4c?t=2859)：這只說明它們是函數、是二元運算；**還要證它們滿足體的公理**。

---

## 7. Step 3：零、一、反元素

講者說時間不夠全做，「挑重點」。

**零** [▶ 48:09](https://youtu.be/zqSMBhwWN4c?t=2889)：$[0,b]$（取 $b=1$ 比較具體）。
$$[0,1]+[a,b] = [0\cdot b+1\cdot a,\ 1\cdot b] = [a,b].$$
（講者算的時候一度寫錯，「你們騙了我」。）加法可交換「聽起來像作業題」。

**一** [▶ 50:21](https://youtu.be/zqSMBhwWN4c?t=3021)：【課堂討論】講者問：要讓 $a/b$ 等於 1，$a,b$ 該怎麼選？學生：相等。講者：要具體，我們手上一定有的是 $1$，所以取 $[1,1]$：
$$[1,1]\,[a,b] = [1a,\ 1b] = [a,b].$$

**反元素** [▶ 51:55](https://youtu.be/zqSMBhwWN4c?t=3115)

【課堂討論】講者問：體和整環的主要差別是什麼？學生說「完備」「沒有洞」。講者：「不一定，$\mathbb{Z}_p$ 一堆洞。」答案是：**每個非零元素都有乘法反元素**。

設 $[a,b]\neq 0$。（$[0,1] = [0,b]$，所以非零就是 $a\neq 0$。）學生想用 $a^{-1},b^{-1}$，講者：「我們不知道 $a^{-1}$、$b^{-1}$ 存在——這個構造的重點就是它們可能不存在。」

反元素是 $[b,a]$（$a\neq0$，所以 $(b,a)\in S$）：
$$[a,b]\,[b,a] = [ab,\ ba] = [1,1],$$
因為 $(ab)\cdot1 = (ba)\cdot1$（可交換）。

講者也提一個引理 [▶ 56:46](https://youtu.be/zqSMBhwWN4c?t=3406)：$[a,b] = [ac,bc]$（$c\neq0$）。

**總結** [▶ 57:17](https://youtu.be/zqSMBhwWN4c?t=3437)：其他性質（交換、結合、分配）講者說會出作業，「講義第 141 頁大概全都有證明，我其實該做，但我會忍住」。

從整環造出新集合 $F$：每個非零元素有乘法反元素、加法可交換、乘法對加法分配……這就是**分式體**。以後寫
$$[a,b] = \frac ab,\qquad F = \left\{\frac ab : a,b\in D,\ b\neq 0\right\}.$$

**還差一件事** [▶ 59:29](https://youtu.be/zqSMBhwWN4c?t=3569)：$F$ 怎麼包含一個同構於 $D$ 的子環？（影片在這裡被切斷，接第 34 集。）

> 【講義補充】Theorem 4.4.15 的證明（p. 141）還做了：
> - **加法結合**：$[a,b]+([c,d]+[e,f]) = [adf+(cf+de)b,\ bdf]$ 和 $([a,b]+[c,d])+[e,f] = [(ad+bc)f+ebd,\ bdf]$ 展開相同。
> - **零的另一種寫法**：$[a,b]+[0,x] = [ax,bx] = [a,b]$（$x\neq0$），因為 $(ax,bx)\sim(a,b)$。
> - 乘法結合、分配律留給讀者。
> - **嵌入**：$\varphi(x) = [x,1]$ 是單射的環同態（$[x,1] = 0\Rightarrow x = 0$；$[x+y,1] = [x,1]+[y,1]$、$[xy,1] = [x,1][y,1]$），所以 $D\cong\varphi(D)$。

---

## 8. 一頁速查表

**$n\mapsto n\cdot1$**：$\mathbb{Z}\to R$ 的環同態。像 $S = \{k\cdot1\}$，核是 $n\mathbb{Z}$（特徵 $n$）或 $\{0\}$（特徵 0）。

- 第一同構定理 ⇒ $R$ 含 $\mathbb{Z}_n$（特徵 $n$）或 $\mathbb{Z}$（特徵 0）。
- $[x]_m = x\cdot[1]_m$。

**Steinitz（1910）**：特徵 $p$ 的體含 $\mathbb{Z}_p$；特徵 0 的體含 $\mathbb{Q}$。**質子體**（所有子體的交）只能是 $\mathbb{Z}_p$ 或 $\mathbb{Q}$。**關鍵一步**：任何子體含 1，就含所有 $k\cdot1$ 和它們的商。

**分式體**（$D$ 整環）

| 步驟 | 內容 | 關鍵 |
|---|---|---|
| 1 | $S = \{(a,b) : b\neq0\}$，$(a,b)\sim(c,d)\iff ad=bc$ | 遞移性要用**消去律**（所以要整環） |
| 2 | $[a,b]+[c,d] = [ad+bc,bd]$，$[a,b][c,d] = [ac,bd]$ | well-defined：$(ad+bc)b'd' = (ab')dd'+(cd')bb'$，代換 $ab'=ba'$、$cd'=dc'$ |
| 3 | 零 $[0,1]$；一 $[1,1]$；$[a,b]^{-1} = [b,a]$（$a\neq0$） | $[ab,ba] = [1,1]$ |
| 4 | $D\hookrightarrow F$，$x\mapsto[x,1]$ | 單射同態 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 嵌入 $x\mapsto[x,1]$；$1/2 = 3/6$ 的意義；分式體的例子 | 第 34 集 |
| 有理函數體 $F(x)$；特徵 $p$ 的無限體 $\mathbb{Z}_p(x)$ | 第 34 集 |
| 多項式環 $R[x]$ 的構造 | 第 35 集 |
| 質子體 ⇒ 每個體都是 $\mathbb{Q}$ 或 $\mathbb{Z}_p$ 的擴張體 | 第 40–45 集 |

---

## 附：本集一句話總結

> **把 1 一直加自己，任何環裡都藏著 $\mathbb{Z}_n$ 或 $\mathbb{Z}$；在體裡再取倒數，就得到質子體 $\mathbb{Z}_p$ 或 $\mathbb{Q}$。分式體的構造則是把「分數」寫成有序對 $(a,b)$、規定 $(a,b)\sim(c,d)\iff ad=bc$——遞移性需要整環的消去律——再照小學的分數規則定義加乘、驗證 well-defined，就從任何整環造出一個體。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-27 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.4 整理。*
