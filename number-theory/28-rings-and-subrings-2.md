---
course: Number Theory（2021 秋，線上錄影）
episode: 28
lecture: 2021-10-18 第 2 部
date: 2021-10-18
video: https://youtu.be/uaPdoM88DgY
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.1 Lecture 21（p. 127–128）：Theorem 4.1.31、Definition 4.1.32、Theorem 4.1.33、Corollary 4.1.34、Example 4.1.35–4.1.36、Definition 4.1.37、Theorem 4.1.38–4.1.39
---

# 第 28 集 · 消去律、體、特徵（Rings, Rngs, Subrings and Subrngs, Basic Examples, Part 2） [▶ 影片](https://youtu.be/uaPdoM88DgY)

← 上一集：[27-rings-and-subrings-1](27-rings-and-subrings-1.md) ｜ [總目錄](README.md) ｜ 下一集：[29-ideals-factor-rings](29-ideals-factor-rings.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 28 集（2021-10-18 第 2 部，接第 27 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（22:06，自動字幕）＋ 講者講義 §4.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 消去律（收尾）與反例](#1-消去律收尾與反例)
- [2. 體](#2-體)
- [3. 有限整環一定是體](#3-有限整環一定是體)
- [4. 例子：Z_p、Z₃[i]、Q[√2]](#4-例子z_pzi-q2)
- [5. 特徵](#5-特徵)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

講完講義 Lecture 21：消去律、**體**、**有限整環是體**、**特徵**。

| 主題 | 時間 | 講義 |
|---|---|---|
| 消去律、$\mathbb{Z}_{10}$ 反例 | 00:02 | Thm 4.1.31 |
| 體 | 03:51 | Def 4.1.32 |
| 有限整環是體 | 05:36 | Thm 4.1.33 |
| $\mathbb{Z}_p$、$\mathbb{Z}_3[i]$、$\mathbb{Q}[\sqrt2]$ | 10:23 | Cor 4.1.34、Ex 4.1.35–4.1.36 |
| 特徵 | 14:05 | Def 4.1.37、Thm 4.1.38–4.1.39 |

---

## 1. 消去律（收尾）與反例

[▶ 00:02](https://youtu.be/uaPdoM88DgY?t=2)

接第 27 集：整環裡 $a\neq0$、$ab = ac$ ⇒ $b = c$。

**證明**：$ab-ac = a(b-c) = 0$。兩個東西乘起來是 0，其中 $a\neq 0$，「用消去法，另一個一定是 0，不然就有零因子，這是禁止的」。所以 $b-c = 0$。∎

**不是整環就不成立** [▶ 01:03](https://youtu.be/uaPdoM88DgY?t=63)：$\mathbb{Z}_n$（$n$ 合數）是反例的好來源。

例子（$\mathbb{Z}_{10}$）[▶ 01:34](https://youtu.be/uaPdoM88DgY?t=94)：
$$5\cdot 4 = 20\equiv 0,\qquad 5\cdot 8 = 40\equiv 0.$$
所以 $5\cdot4 = 5\cdot 8$，$5\neq0$，但 **$4\neq 8$**。$\mathbb{Z}_{10}$ 不是整環，沒有消去律。

（字幕只剩「four times five is equal to let's see here」和「this does not imply 4 equals 8」，上面依講者的結論補上算式。）

**消去律 ≠ 有反元素** [▶ 02:49](https://youtu.be/uaPdoM88DgY?t=169)：在 $\mathbb{Z}[x]$ 裡
$$(x^2+1)(x+3) = f(x)(x+3)\ \Longrightarrow\ f(x) = x^2+1,$$
但**不是**因為乘了 $(x+3)^{-1}$——$(x+3)^{-1}$ **不在** $\mathbb{Z}[x]$ 裡（「如果它存在，也在別的地方」）。講者：「警世故事。」

---

## 2. 體

[▶ 03:51](https://youtu.be/uaPdoM88DgY?t=231)

> **定義**（講義 Definition 4.1.32）：每個非零元素都是單位的、有單位元素的可交換環叫**體**（field）。

**體一定是整環嗎？** [▶ 04:36](https://youtu.be/uaPdoM88DgY?t=276)

【課堂討論】學生：零因子不可能是單位。講者：「對，因為我們今天早些做的那件事——我在課堂上解掉的那個作業題，哎呀。」（第 27 集第 3 節：單位和零因子不重疊。體裡每個非零元素都是單位，所以沒有零因子。）

講者也給另一個說法 [▶ 05:06](https://youtu.be/uaPdoM88DgY?t=306)：體裡 $ab = ac$、$a\neq0$，兩邊乘 $a^{-1}$ 就得 $b = c$。但他提醒：**整環的消去律不是靠反元素**，「我們偷偷繞過了那個狡猾的定理，它的證明看起來太簡單了，但就是那種漂亮的證明」。

---

## 3. 有限整環一定是體

[▶ 05:36](https://youtu.be/uaPdoM88DgY?t=336)

> **定理**（講義 Theorem 4.1.33）：每個**有限**整環都是體。

**證明**：設 $D$ 是有限整環。它本來就是有 1 的可交換環（整環的定義），只要檢查**每個非零元素都有反元素**。

1. 設 $a\in D$、$a\neq 0$。若 $a = 1$，$a^{-1} = 1$。
2. 否則看數列 [▶ 07:44](https://youtu.be/uaPdoM88DgY?t=464)
   $$a,\ a^2,\ a^3,\ a^4,\ \dots$$
   這是 $D$ 的子集合。$D$ 有限，所以這串**一定會繞回來**，否則就是有限集合的無限子集合，荒謬。（講者：它不一定變成 0，也不一定跑遍 $D$，但一定會重複。）
3. 所以 $a^i = a^j$ 對某些 $i>j$ 成立。
4. 於是 $a^{i-j} = 1$ [▶ 08:44](https://youtu.be/uaPdoM88DgY?t=524)，所以
   $$a^{-1} = a^{i-j-1}.$$
5. 每個非零元素都是單位，$D$ 是體。∎

> 以下**不是逐字稿內容**，是補一個講者帶過的細節：第 3 步到第 4 步要從 $a^i = a^j$ 消掉 $a^j$。$a\neq 0$ 而 $D$ 是整環，所以 $a^j\neq 0$（非零元素的乘積不是零），可以用**消去律**：$a^j\cdot a^{i-j} = a^j\cdot 1$ ⇒ $a^{i-j} = 1$。這裡用到的是整環的消去律，不是反元素——所以 Theorem 4.1.33 真的需要「整環」這個條件。

**無限整環不一定是體** [▶ 09:14](https://youtu.be/uaPdoM88DgY?t=554)：【課堂討論】講者問。答案：$\mathbb{Z}$——無限的整環，但 $2^{-1} = \frac12\notin\mathbb{Z}$，所以**不是體**。

> 【講義補充】講義說這個證明「迷人地簡單」（charmingly simple）。

---

## 4. 例子：Z_p、Z₃[i]、Q[√2]

**$\mathbb{Z}_p$ 是體**（講義 Corollary 4.1.34）[▶ 10:23](https://youtu.be/uaPdoM88DgY?t=623)：講者說他不寫了，「我們早就知道」：$U_p = \{1,2,\dots,p-1\}$，就是 $\mathbb{Z}_p$ 拿掉 0。

> 【講義補充】Corollary 4.1.34 的證明（p. 127）：$\mathbb{Z}_p$ 裡 $ab = 0$ 表示 $p\mid ab$，由 Euclid 引理（第 5 集）$p\mid a$ 或 $p\mid b$，所以沒有零因子。$\mathbb{Z}_p$ 是有限整環，由 Theorem 4.1.33 是體。

**$\mathbb{Z}_3[i]$**（Ex 4.1.35）[▶ 11:25](https://youtu.be/uaPdoM88DgY?t=685)：
$$\mathbb{Z}_3[i] = \{a+bi : a,b\in\mathbb{Z}_3\} = \{0,\,1,\,2,\,i,\,1+i,\,2+i,\,2i,\,1+2i,\,2+2i\}.$$

講者說「不讓你們無聊」，可以證明它是整環（講義 p. 127 有計算）。所以它是**有限整環 ⇒ 體**，有 **9 個元素**。

講者 [▶ 13:02](https://youtu.be/uaPdoM88DgY?t=782)：「這是新東西。」$\mathbb{Z}_9$ **不是**體（9 是合數），但這個 9 個元素的東西是體。

> 【講義補充】Example 4.1.35 的計算（p. 127）：設 $(x+yi)(a+bi) = (xa-yb)+i(xb+ya) = 0$。寫成矩陣
> $$\begin{pmatrix}x&-y\\y&x\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}.$$
> 若 $x+yi\neq0$，則 $x^2+y^2\neq 0$（在 $\mathbb{Z}_3$ 裡），矩陣可逆（乘它的伴隨矩陣再除以 $x^2+y^2$），所以 $a = b = 0$。沒有零因子。講義說這跟 Gallian p. 243 一樣，Gallian 有 8 個非零元素的乘法表。
>
> 以下**不是逐字稿內容**，是補一句為什麼 $x^2+y^2\neq0$：$\mathbb{Z}_3$ 裡平方只有 $0,1$，所以 $x^2+y^2 = 0$ 只能 $x=y=0$。（這跟「$-1$ 不是模 3 的平方」是同一件事；換成 $\mathbb{Z}_5[i]$ 就不行，因為 $1^2+2^2 = 5\equiv 0$。）

**$\mathbb{Q}[\sqrt2]$**（Ex 4.1.36）[▶ 13:35](https://youtu.be/uaPdoM88DgY?t=815)：$\{a+b\sqrt2 : a,b\in\mathbb{Q}\}$ 是體。講者不細講，說它是**擴張體**（extension field）的例子：有理數體**添加**一個東西 $\sqrt2$。

【口頭】添加已經在體裡的東西，只會得到原本的體。可以添加任何東西嗎？添加之後有什麼性質？「這些是我們想回答的有趣問題。」（第 40–45 集。）

> 【講義補充】Example 4.1.36 的計算（p. 128）：$\mathbb{Q}[\sqrt2]$ 對加乘封閉；若 $a+b\sqrt2\neq0$，
> $$\frac1{a+b\sqrt2} = \frac{a-b\sqrt2}{(a+b\sqrt2)(a-b\sqrt2)} = \frac{a}{a^2-2b^2}-\frac{b}{a^2-2b^2}\sqrt2.$$
> $a,b\in\mathbb{Q}$ 時 $a^2-2b^2\neq 0$（否則 $\sqrt2 = |a/b|$ 是有理數），所以反元素還在 $\mathbb{Q}[\sqrt2]$ 裡。講義說它比 $\mathbb{Q}$ 大，但比 $\mathbb{R}$ 小得多。（分母有理化，第 15 集高斯整數用過同一招。）

---

## 5. 特徵

[▶ 14:05](https://youtu.be/uaPdoM88DgY?t=845)

【課堂討論】講者問：聽過「特徵為零」（characteristic zero）嗎？學生說「我一直好奇那是什麼意思」。

> **定義**（Def 4.1.37）：環 $R$ 的**特徵**（characteristic）是使 $nx = 0$ **對所有** $x\in R$ 成立的**最小正整數** $n$，記 $\mathrm{char}(R) = n$。沒有這樣的 $n$，就說 $\mathrm{char}(R) = 0$。

講者：「你可能以為沒有的話是無限大，但我們說零。」

> **定理**（Thm 4.1.38）[▶ 15:36](https://youtu.be/uaPdoM88DgY?t=936)：$R$ 有單位元素 1。
> - 若 1 的（加法）階是無限，$\mathrm{char}(R) = 0$。
> - 若 1 的加法階是 $n$，$\mathrm{char}(R) = n$。

講者：「我其實不是靠定義記特徵，是靠這個定理記的。」

**證明** [▶ 16:41](https://youtu.be/uaPdoM88DgY?t=1001)：
$$nx = \underbrace{x+x+\cdots+x}_{n} = \underbrace{1x+1x+\cdots+1x}_{n} = (\underbrace{1+1+\cdots+1}_{n})\,x = (n\cdot 1)\,x.$$
（分配律。）所以若 $n\cdot 1 = 0$，則 $nx = 0x = 0$ 對所有 $x$。

- 這裡說的是 1 的**加法**階。「1 的乘法階很蠢，就是 1。」
- 1 的加法階是 $n$，表示 $n\cdot1 = 0$ 而更小的都不是 0，所以 $n$ 就是特徵。
- 1 的階無限時，同一條式子說明不可能有 $n$ 讓所有 $nx = 0$（取 $x=1$ 就矛盾）。

> **定理**（Thm 4.1.39）[▶ 18:57](https://youtu.be/uaPdoM88DgY?t=1137)：**整環的特徵是 0 或質數。**

**證明**：

1. 1 的階無限 ⇒ 特徵 0，做完。
2. 設 1 的加法階是 $n$，而 $n = st$（$1\le s,t\le n$）。則 [▶ 19:28](https://youtu.be/uaPdoM88DgY?t=1168)
   $$0 = n\cdot1 = (st)\cdot 1 = (s\cdot 1)(t\cdot 1).$$
3. 整環沒有零因子，所以 $s\cdot1 = 0$ 或 $t\cdot 1 = 0$。
4. 1 的階是 $n$（最小的），所以 $s = n$ 或 $t = n$。也就是說 $n$ 的因數只有 $1$ 和 $n$——**$n$ 是質數**。∎

（第 3 步的 $(st)\cdot 1 = (s\cdot1)(t\cdot1)$ 是分配律展開。講者說「它們不能都是 0……其中一個一定是 $n$，否則跟 1 的階是 $n$ 矛盾」。）

**例子** [▶ 20:32](https://youtu.be/uaPdoM88DgY?t=1232)：

| 環 | 特徵 | 理由 |
|---|---|---|
| $\mathbb{Z}_p$ | $p$ | 例：$\mathbb{Z}_3$ 裡 $1+1+1 = 0$，第一次等於 0 |
| $\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ | $0$ | 1 一直加永遠不會是 0 |
| $\mathbb{Z}_3[i]$ | $3$ | （以下**不是逐字稿內容**：1 的加法階是 3） |

【口頭】[▶ 21:32](https://youtu.be/uaPdoM88DgY?t=1292) 「我幾乎整個數學生涯都活在特徵零。唯一談到非零特徵的時候，就是在這種抽象代數課上——這就是我存在的本質。但不是每個人都這樣，有些人大部分時間活在**特徵 2**——那主要是資訊科學家。」

---

## 6. 一頁速查表

**消去律**（整環）：$a\neq0$、$ab=ac$ ⇒ $b=c$。**不用反元素**。反例（非整環）：$\mathbb{Z}_{10}$ 裡 $5\cdot4 = 5\cdot8 = 0$ 但 $4\neq8$。

**體**：有 1 的可交換環，每個非零元素都是單位。體 ⇒ 整環（單位不是零因子）。

**有限整環 ⇒ 體**。**關鍵一步**：$a,a^2,a^3,\dots$ 在有限集合裡一定重複，$a^i=a^j$ ⇒（消去）$a^{i-j}=1$ ⇒ $a^{-1}=a^{i-j-1}$。

- $\mathbb{Z}$：無限整環，不是體。
- $\mathbb{Z}_p$：體。
- $\mathbb{Z}_3[i]$：9 個元素的體（$\mathbb{Z}_9$ 不是體）。
- $\mathbb{Q}[\sqrt2]$：體（擴張體）；$\frac1{a+b\sqrt2} = \frac{a-b\sqrt2}{a^2-2b^2}$。

**特徵** $\mathrm{char}(R)$：最小 $n>0$ 使 $nx=0$ 對所有 $x$；沒有就是 0。

- = 1 的加法階（無限就是 0）。**關鍵一步**：$nx = (n\cdot1)x$。
- 整環的特徵是 0 或質數。**關鍵一步**：$0 = (st)\cdot1 = (s\cdot1)(t\cdot1)$，沒有零因子。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 理想、商環 $R/I$ | 第 29 集 |
| 「$R/I$ 是體 ⇔ $I$ 是極大理想」「$R/I$ 是整環 ⇔ $I$ 是質理想」 | 第 30–32 集 |
| 特徵 $p$ ⇒ 質子體 $\mathbb{Z}_p$；特徵 0 ⇒ 質子體 $\mathbb{Q}$ | 第 33–34 集 |
| 分式體（把整環擴成體，例如 $\mathbb{Z}\to\mathbb{Q}$） | 第 33–34 集 |
| $\mathbb{Z}_3[i]\cong\mathbb{Z}_3[x]/(x^2+1)$；擴張體 $\mathbb{Q}[\sqrt2]$ | 第 40–45 集 |

---

## 附：本集一句話總結

> **整環有消去律（不需要反元素）；每個非零元素都可逆的叫體。有限整環一定是體，因為 $a$ 的次方在有限集合裡會繞回來，$a^{i-j}=1$——所以 $\mathbb{Z}_p$ 和 9 個元素的 $\mathbb{Z}_3[i]$ 都是體。特徵是 1 的加法階，整環的特徵只能是 0 或質數。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-18 第 2 部錄影逐字稿（YouTube 自動字幕，22:06）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.1 整理。*
