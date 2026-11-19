---
course: Number Theory（2021 秋，線上錄影）
episode: 25
lecture: 2021-10-13 第 1 部
date: 2021-10-13
video: https://youtu.be/5gAKNbqAIMM
notes: 講者照 Silverman《A Friendly Introduction to Number Theory》第 20–22 章；Jones & Jones 第 7 章（書頁 119–135，PDF 頁 134–150）：§7.2 Lemma 7.2–7.3、§7.3 Legendre 符號、Theorem 7.5–7.6、§7.4 Theorem 7.11、Example 7.9
---

# 第 25 集 · 二次互反律（上）（Quadratic Reciprocity, part 1） [▶ 影片](https://youtu.be/5gAKNbqAIMM)

← 上一集：[24-quaternions](24-quaternions.md) ｜ [總目錄](README.md) ｜ 下一集：[26-quadratic-reciprocity-2](26-quadratic-reciprocity-2.md) →

> **課程**：Number Theory（2021 秋）— 第 25 集（2021-10-13 第 1 部）。**這集是實體課堂錄影**（2021-10-13），有學生回答和提問；講者那天身體不太舒服。
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ Jones & Jones 第 7 章
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 三個問題](#1-三個問題)
- [2. 平方表與規律](#2-平方表與規律)
- [3. 二次剩餘與非剩餘](#3-二次剩餘與非剩餘)
- [4. 乘法規則與 Legendre 符號](#4-乘法規則與-legendre-符號)
- [5. 二次互反律](#5-二次互反律)
- [6. 歷史](#6-歷史)
- [7. 例子](#7-例子)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】講者決定這個主題暫時不照 Stillwell，改照 Joseph Silverman《A Friendly Introduction to Number Theory》（之前發過它的 Pell 方程那節）。Silverman 有三章（第 20–22 章，章都很短）講二次互反律。講者只挑重點、跳過冗長的證明，**目標是讓大家離開時清楚知道二次互反律到底在說什麼**——從中間跳進去只會看到一堆術語 [▶ 00:00](https://youtu.be/5gAKNbqAIMM?t=0)。

| 段落 | 內容 | 課本（Jones & Jones） |
|---|---|---|
| 1–3 | 平方剩餘；模 $p$ 恰有 $(p-1)/2$ 個 | §7.2、Lemma 7.3 |
| 4 | Legendre 符號；$\left(\frac ap\right)\left(\frac bp\right) = \left(\frac{ab}p\right)$ | §7.3、Theorem 7.5 |
| 5 | 二次互反律（含 $-1$、$2$ 的補充律） | §7.3–7.4、Theorem 7.11 |
| 7 | $(75/97)$、$(14/137)$、$(55/179)$ | Example 7.9 類似 |

---

## 1. 三個問題

[▶ 01:06](https://youtu.be/5gAKNbqAIMM?t=66)

之前解的是線性同餘 $ax\equiv c$ 和聯立同餘（中國剩餘定理）。二次互反律處理的是**同餘加上平方**的問題：

- **(a)** 3 是否同餘於某數的平方（模 7）？
- **(b)** $x^2\equiv-1\ (\mathrm{mod}\ 13)$ 有沒有解？
- **(c)** 對哪些質數 $p$，$x^2\equiv2\ (\mathrm{mod}\ p)$ 有解？

⚠️ 逐字稿缺字：字幕把 (b) 唸成「x congruent to minus 1 mod 13」、(c) 先唸成「x congruent to 2」，講者隨即說是 $x^2$。

**(a)** [▶ 03:21](https://youtu.be/5gAKNbqAIMM?t=201)：模 7 只要看 $0^2,\dots,6^2 = 0,1,4,9,16,25,36$，化簡得 $0,1,4,2,2,4,1$。**沒有 3**，所以不存在整數 $x$ 使 $x^2\equiv3\ (\mathrm{mod}\ 7)$。

**(b)** [▶ 05:39](https://youtu.be/5gAKNbqAIMM?t=339)：把 0 到 12 平方模 13，會發現 $x\equiv5$ 和 $x\equiv8$ 都是解：$5^2 = 25 = 26-1\equiv-1$，$8^2 = 64 = 65-1\equiv-1$。

**(c)** 等一下由互反律回答。

【口頭】有時逐一檢查就行，但接下來會看到一套技術，用非常巧妙的定理回答很多這類問題 [▶ 05:06](https://youtu.be/5gAKNbqAIMM?t=306)。

---

## 2. 平方表與規律

[▶ 06:51](https://youtu.be/5gAKNbqAIMM?t=411)

$b^2$ 模 5、7、11、13：

| $b$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mod 5 | 0 | 1 | 4 | 4 | 1 | | | | | | | | |
| mod 7 | 0 | 1 | 4 | 2 | 2 | 4 | 1 | | | | | | |
| mod 11 | 0 | 1 | 4 | 9 | 5 | 3 | 3 | 5 | 9 | 4 | 1 | | |
| mod 13 | 0 | 1 | 4 | 9 | 3 | 12 | 10 | 10 | 12 | 3 | 9 | 4 | 1 |

【口頭】Silverman 書的優點是有很多這種「數值插曲」。這不只是教學手法，某一類數論家實際上就是這樣工作：看大量數據、找規律 [▶ 09:08](https://youtu.be/5gAKNbqAIMM?t=548)。

【課堂討論】講者算表時唸錯幾次（例如 $5^2$ 模 7），學生糾正；講者問有什麼規律，學生回答：**有對稱性**——每一列從兩端往中間讀是一樣的（除了開頭的 0）[▶ 12:29](https://youtu.be/5gAKNbqAIMM?t=749)。Silverman 的說法：**除了 0，每個出現的平方值恰好出現兩次**。

---

## 3. 二次剩餘與非剩餘

### 3.1 定義

[▶ 14:16](https://youtu.be/5gAKNbqAIMM?t=856)

$p$ 是奇質數。
- **二次剩餘**（quadratic residue，QR）：**非零**、且同餘於某數平方的數（模 $p$）。
- **二次非剩餘**（non-residue，NR）：**非零**、且不同餘於任何平方的數。

0 不在討論範圍內（既不是 QR 也不是 NR）。

【課堂討論】講者問「懂 quadratic residue 這個說法嗎？」學生說不太懂。講者解釋：$\mathbb{Z}/n\mathbb{Z}$ 是「模 $n$ 的剩餘（residue）」的集合，剩餘就是**餘數**；「二次剩餘」就是某個平方的餘數——「二次」因為是平方，「剩餘」因為是餘數 [▶ 15:23](https://youtu.be/5gAKNbqAIMM?t=923)。

【課堂討論】「模 5 的非剩餘是？」學生：2 和 3。「模 7 的？」學生：3、5、6。「模 7 有幾個剩餘？」3 個——不是巧合 [▶ 22:45](https://youtu.be/5gAKNbqAIMM?t=1365)。

### 3.2 定理：恰好一半

**定理**：$p$ 奇質數。模 $p$ 恰有 $\frac{p-1}2$ 個二次剩餘、$\frac{p-1}2$ 個非剩餘。

**證明的有趣部分**（講者說「有趣對我來說就是簡單」）[▶ 16:30](https://youtu.be/5gAKNbqAIMM?t=990)：
$$(p-b)^2 = p^2 - 2pb + b^2\equiv b^2\ (\mathrm{mod}\ p).$$
所以
$$1^2\equiv(p-1)^2,\quad 2^2\equiv(p-2)^2,\quad\dots,\quad\left(\tfrac{p-1}2\right)^2\equiv\left(p-\tfrac{p-1}2\right)^2 = \left(\tfrac{p+1}2\right)^2.$$
非零的平方 $1^2,\dots,(p-1)^2$ 只會取到 $1^2,2^2,\dots,\left(\frac{p-1}2\right)^2$ 這些值，所以**最多** $\frac{p-1}2$ 個二次剩餘。

剩下較難的部分：證明這 $\frac{p-1}2$ 個值**互不相同**（講者略過，Silverman p. 144 有證明）。數值證據（上表）支持，但「不能用定理證明定理」[▶ 21:39](https://youtu.be/5gAKNbqAIMM?t=1299)。一旦證出恰有 $\frac{p-1}2$ 個 QR，非剩餘也恰有 $\frac{p-1}2$ 個（計數）。

（以下**不是逐字稿內容**，是依第 5 集「$p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$」補的一種證法：若 $a^2\equiv b^2$，則 $p\mid(a-b)(a+b)$，所以 $a\equiv\pm b$。$1\le a,b\le\frac{p-1}2$ 時 $a+b$ 介於 2 和 $p-1$ 之間，不被 $p$ 整除，所以 $a\equiv b$。）

> 【課本補充】Jones & Jones §7.2：二次剩餘的集合記作 $Q_n\subseteq U_n$，是 $U_n$ 的子群（Lemma 7.2：$1 = 1^2$；$s^2t^2 = (st)^2$；$(s^2)^{-1} = (s^{-1})^2$）。Lemma 7.3：若 $g$ 是模 $n$ 的原根（$n>2$），則 $Q_n$ 恰好是 $g$ 的**偶數次方**，是 $\phi(n)/2$ 階循環群。例：$n=7$、$g=3$：$3,2,6,4,5,1$，偶數次方 $2,4,1$ 就是 $Q_7$。

---

## 4. 乘法規則與 Legendre 符號

### 4.1 觀察

[▶ 25:34](https://youtu.be/5gAKNbqAIMM?t=1534)

**QR × NR**：$2\cdot5\equiv3\ (7)$；$5\cdot6\equiv8\ (11)$；$4\cdot5\equiv7\ (13)$；$10\cdot7\equiv5\ (13)$。結果 3、8、7、5 都是非剩餘。

**NR × NR**：$3\cdot5\equiv1\ (7)$；$6\cdot7\equiv9\ (11)$；$5\cdot11\equiv3\ (13)$；$7\cdot11\equiv12\ (13)$。結果都是剩餘。

【口頭】講者不喜歡 Silverman 用乘號「×」，「好俗氣」[▶ 26:09](https://youtu.be/5gAKNbqAIMM?t=1569)。

**規律**：
$$\text{QR}\times\text{QR} = \text{QR},\qquad\text{QR}\times\text{NR} = \text{NR},\qquad\text{NR}\times\text{NR} = \text{QR}.$$

**QR × QR 的代數證明** [▶ 29:33](https://youtu.be/5gAKNbqAIMM?t=1773)：$x^2\cdot y^2 = (xy)^2$。

【課堂討論】有學生說：「這有點像負號。」講者：「非常有智慧的評論。」——這正好引出 Legendre 符號 [▶ 30:04](https://youtu.be/5gAKNbqAIMM?t=1804)。

### 4.2 Legendre 符號

[▶ 30:40](https://youtu.be/5gAKNbqAIMM?t=1840)

**定義**：$p$ 奇質數，
$$\left(\frac ap\right) = \begin{cases}1 & a \text{ 是模 } p \text{ 的二次剩餘},\\ -1 & a \text{ 是模 } p \text{ 的非剩餘}.\end{cases}$$
**這不是分數**，是一個分情況定義的函數。

**乘法性**：
$$\left(\frac ap\right)\left(\frac bp\right) = \left(\frac{ab}p\right).$$
把三種情況（$1\cdot1$、$1\cdot(-1)$、$(-1)(-1)$）收成一個公式。講者強調：QR × QR 已證，其他兩種目前只有數值證據 [▶ 32:58](https://youtu.be/5gAKNbqAIMM?t=1978)。

> 【課本補充】§7.3（p. 123–125）：
> - 定義還加上 $\left(\frac ap\right) = 0$ 當 $p\mid a$。
> - $\left(\frac ap\right)$ 只依賴 $a$ 模 $p$ 的同餘類，所以**上面的數可以先模 $p$ 化簡**。
> - Corollary 7.4：$g$ 是原根時 $\left(\frac{g^i}{p}\right) = (-1)^i$。
> - Theorem 7.5（乘法性）證明：$a = g^i$、$b = g^j$，$\left(\frac{ab}p\right) = (-1)^{i+j} = (-1)^i(-1)^j$。
> - Theorem 7.6（**Euler 判別法**）：$\left(\frac ap\right)\equiv a^{(p-1)/2}\ (\mathrm{mod}\ p)$。

### 4.3 例：$(75/97)$

[▶ 33:30](https://youtu.be/5gAKNbqAIMM?t=2010)

75 是不是某數的平方（模 97）？不想用查表。
$$\left(\frac{75}{97}\right) = \left(\frac3{97}\right)\left(\frac5{97}\right)\left(\frac5{97}\right) = \left(\frac3{97}\right)\left(\frac5{97}\right)^2 = \left(\frac3{97}\right).$$
（$\left(\frac5{97}\right)$ 是 $\pm1$，平方是 1——**不用知道它是多少**。）
Silverman「從帽子裡變出兔子」：$10^2 = 100\equiv3\ (\mathrm{mod}\ 97)$，所以 $\left(\frac3{97}\right) = 1$。

**$75$ 是模 97 的二次剩餘。**

【口頭】要習慣：$\left(\frac3{97}\right)$ 是在問「有沒有某數的平方 $\equiv3$」，$10^2\equiv3$ 就回答了「有」[▶ 35:52](https://youtu.be/5gAKNbqAIMM?t=2152)。

---

## 5. 二次互反律

[▶ 38:31](https://youtu.be/5gAKNbqAIMM?t=2311)

【口頭】講者跳過 Silverman 的一章（會掃描給大家），直接講定理，才有時間做幾個例子再談歷史。「數學有『定律』嗎？」這名字取的時候很多東西都叫定律，像萬有引力定律 [▶ 39:04](https://youtu.be/5gAKNbqAIMM?t=2344)。

**定理（二次互反律，Law of Quadratic Reciprocity）**：$p,q$ 是相異奇質數。
1. **（$-1$ 的補充律）**
$$\left(\frac{-1}p\right) = \begin{cases}1 & p\equiv1\ (\mathrm{mod}\ 4),\\ -1 & p\equiv3\ (\mathrm{mod}\ 4).\end{cases}$$
2. **（$2$ 的補充律）**
$$\left(\frac2p\right) = \begin{cases}1 & p\equiv1 \text{ 或 } 7\ (\mathrm{mod}\ 8),\\ -1 & p\equiv3 \text{ 或 } 5\ (\mathrm{mod}\ 8).\end{cases}$$
3. **（互反律本身）**
$$\left(\frac qp\right) = \begin{cases}\left(\frac pq\right) & p\equiv1 \text{ 或 } q\equiv1\ (\mathrm{mod}\ 4),\\ -\left(\frac pq\right) & p\equiv3 \text{ 且 } q\equiv3\ (\mathrm{mod}\ 4).\end{cases}$$

【口頭】第 3 條「會讓你大吃一驚」：$p$ 和 $q$ **可以上下對調**。只要有一個 $\equiv1\ (\mathrm{mod}\ 4)$ 就能自由翻轉；兩個都 $\equiv3$ 時翻轉要加負號，這會完全改變結果 [▶ 42:02](https://youtu.be/5gAKNbqAIMM?t=2522)。

【課堂討論】講者問：第二種情況邏輯上該寫「或」還是「且」？學生答「且」——分情況定義的函數不能讓情況重疊又給不同答案。講者原本寫錯（寫成 $\equiv1$），學生指出，他改成 $\equiv3$：「我是白痴，不然就說不通了。」[▶ 42:35](https://youtu.be/5gAKNbqAIMM?t=2555)

⚠️ 逐字稿缺字：[▶ 40:44](https://youtu.be/5gAKNbqAIMM?t=2444) 2 的補充律字幕只唸到「1 if p is congruent to 1 or 7 mod 8 [……] or five mod eight」，中間 $-1$ 那半句掉了；筆記依標準敘述補成 $3$ 或 $5$。

**回答問題 (c)** [▶ 43:57](https://youtu.be/5gAKNbqAIMM?t=2637)：2 是模 $p$ 的二次剩餘 $\iff p\equiv1$ 或 $7\ (\mathrm{mod}\ 8)$。

**為什麼 $-1$ 的規則「不意外」** [▶ 44:32](https://youtu.be/5gAKNbqAIMM?t=2672)：$x^2\equiv-1\ (\mathrm{mod}\ p)$ 就是 $x^2+1\equiv0$，粗略地像「$x^2+1 = p$」（其實是 $p$ 的倍數）。【口頭】用講者說的「不嚴謹的邏輯」想高斯整數：哪些質數能寫成平方和？像 13（$=2^2+3^2$），正是 $\equiv1\ (\mathrm{mod}\ 4)$ 的那些。所以這個結果和高斯整數那邊的結果一定緊密相關。

> 【課本補充】Jones & Jones：
> - §4.1 Theorem 4.6（p. 71）用 **Wilson 定理**證了 $-1$ 的補充律：奇質數 $p$，$x^2+1\equiv0\ (\mathrm{mod}\ p)$ 有解 $\iff p\equiv1\ (\mathrm{mod}\ 4)$。（第 21 集用多項式的根證了同一件事，繞過 Wilson 定理。）
> - §7.4（p. 130）的表列出 $p,q\le19$ 的 $\left(\frac qp\right)$，幾乎對稱，例外正好是 $p\equiv q\equiv3\ (\mathrm{mod}\ 4)$。
> - Legendre 的等價寫法：$\left(\frac qp\right)\left(\frac pq\right) = (-1)^{\frac{p-1}2\cdot\frac{q-1}2}$。

---

## 6. 歷史

[▶ 46:12](https://youtu.be/5gAKNbqAIMM?t=2772)

【口頭】講者唸 Silverman 的說法：
- $\left(\frac{-1}p\right)$ 和 $\left(\frac2p\right)$ 書中已證；$\left(\frac qp\right)$ 和 $\left(\frac pq\right)$ 的關係有很多種證明，但**沒有一個容易**。Silverman 下一章給 Eisenstein 的證明（講者不打算發，除非大家真的想要）。
- Euler 和 Lagrange 最早敘述二次互反律；Gauss 在 1801 年的名著《算術研究》（*Disquisitiones Arithmeticae*，講者說他唸得很糟）給出第一個證明，那時 Gauss 大約 19 歲——「大概你們的年紀」。Gauss 一生找到七種證明。
- 19 世紀的數學家又陸續提出並證明了三次、四次互反律。
- 這些後來被 Hilbert、Artin 等人在約 1890 到 1920–30 年代發展的**類體論**（class field theory）涵蓋。
- 1960–70 年代，一些數學家提出一系列大幅推廣類體論的猜想，今天叫 **Langlands 綱領**。Andrew Wiles 1995 年證明的基本定理只是 Langlands 綱領的一小塊，卻足以解決 350 年的 **Fermat 最後定理**。「這些東西彼此的關聯比我們以為的還深。」

> 【課本補充】Jones & Jones p. 130 的說法略有不同：二次互反律由 **Euler 在 1783 年猜測**，Legendre 給了幾個不完整的證明，**Gauss 在 1795 年（18 歲）**自己發現並給出第一個正確證明。

---

## 7. 例子

### 7.1 $(14/137)$

[▶ 48:27](https://youtu.be/5gAKNbqAIMM?t=2907)

（講者先寫 $14/37$，覺得太簡單，改成 137。）
$$\left(\frac{14}{137}\right) = \left(\frac2{137}\right)\left(\frac7{137}\right).$$
- $137 = 17\cdot8+1\equiv1\ (\mathrm{mod}\ 8)$，所以 $\left(\frac2{137}\right) = 1$。
- $137\equiv1\ (\mathrm{mod}\ 4)$（$136 = 4\cdot34$），可以翻轉：$\left(\frac7{137}\right) = \left(\frac{137}7\right)$。翻轉後問的是模 7 的問題，比模 137 好得多。
- 上面的數可以模下面的數化簡：$137 = 140-3\equiv-3\equiv4\ (\mathrm{mod}\ 7)$。
- $4 = 2^2$ 是 QR，所以 $\left(\frac47\right) = 1$。

**$\left(\frac{14}{137}\right) = 1$，14 是模 137 的二次剩餘。**

【課堂討論】算 $136/4$ 時講者卡住（先說 23、又說 33），學生幫忙；算 $137\bmod7$ 時講者想的是 $-3$（因為 $140 = 20\cdot7$），學生說 4，兩者同餘 [▶ 52:56](https://youtu.be/5gAKNbqAIMM?t=3176)。

【口頭】「你總有 50% 的機率猜對——好吧也不一定，也許有學生故意填 0 來整我。」講者接著講了一段主日學小組的故事：有人問「一群沒經驗的年輕漁夫（使徒）改變世界的機率是多少？」他說是 100%，因為已經發生了；就像問他「你生四個男孩一個女孩的機率」——條件機率在所有條件都已滿足時就是 100% [▶ 54:51](https://youtu.be/5gAKNbqAIMM?t=3291)。

【口頭】「這是很怪的計算遊戲，我從沒做過任何和它有一點點像的計算。」[▶ 55:22](https://youtu.be/5gAKNbqAIMM?t=3322)

### 7.2 $(55/179)$（開頭）

[▶ 55:53](https://youtu.be/5gAKNbqAIMM?t=3353)
$$\left(\frac{55}{179}\right) = \left(\frac5{179}\right)\left(\frac{11}{179}\right).$$
- $5\equiv1\ (\mathrm{mod}\ 4)$，可翻轉：$\left(\frac5{179}\right) = \left(\frac{179}5\right) = \left(\frac45\right)$（$179 = 175+4$）。
- $11\equiv3$、$179\equiv3\ (\mathrm{mod}\ 4)$（$180$ 是 4 的倍數），兩個都 $\equiv3$，翻轉加負號：$\left(\frac{11}{179}\right) = -\left(\frac{179}{11}\right) = -\left(\frac3{11}\right)$（$179 = 176+3 = 16\cdot11+3$）。

【課堂討論】算 $179\bmod11$ 時，學生用拆數字的方法（「169……11 平方 121……」），講者用直式除法：「你的時間不多了先生——學校的方法打敗你了！你那沒用的 common core 算法……」然後道歉：其實學生做的正是 common core 主張的——把問題拆成用分配律和熟悉數字的小問題，這沒什麼不對；只是大家都該知道有個有效率、可靠、可以依靠的演算法（雖然它需要紙）。兩人都得到 3 [▶ 58:12](https://youtu.be/5gAKNbqAIMM?t=3492)。

剩下 $\left(\frac45\right)$ 和 $\left(\frac3{11}\right)$ 在下一集算完。

---

## 8. 一頁速查表

**二次剩餘**（$p$ 奇質數）：非零、同餘於平方。恰 $\frac{p-1}2$ 個 QR、$\frac{p-1}2$ 個 NR。
- 關鍵：$(p-b)^2\equiv b^2$，平方值只來自 $1,\dots,\frac{p-1}2$。
- 模 7：QR $= \{1,2,4\}$；模 11：$\{1,3,4,5,9\}$；模 13：$\{1,3,4,9,10,12\}$。

**Legendre 符號** $\left(\frac ap\right) = \pm1$（QR / NR）。
- 乘法性 $\left(\frac ap\right)\left(\frac bp\right) = \left(\frac{ab}p\right)$；平方因子消失：$\left(\frac{ab^2}p\right) = \left(\frac ap\right)$。
- 上面可以模 $p$ 化簡。
- 【課本】Euler 判別法 $\left(\frac ap\right)\equiv a^{(p-1)/2}$。

**二次互反律**（$p\ne q$ 奇質數）
- $\left(\frac{-1}p\right) = 1\iff p\equiv1\ (4)$。
- $\left(\frac2p\right) = 1\iff p\equiv\pm1\ (8)$。
- $\left(\frac qp\right) = \left(\frac pq\right)$，除非 $p\equiv q\equiv3\ (4)$，那時加負號。

**計算流程**：分解上面 → 去掉平方 → 2 和 $-1$ 用補充律 → 奇質數翻轉 → 上面模下面化簡 → 重複。
- $(75/97) = (3/97) = 1$（$10^2\equiv3$）。
- $(14/137) = (2/137)(137/7) = 1\cdot(4/7) = 1$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $(55/179)$ 的後半、$(299/397)$ | 第 26 集 |
| $\left(\frac{-1}p\right) = 1\iff p\equiv1\ (4)$ | 第 19–21 集（平方和、高斯質數） |
| 類體論、Langlands、Wiles | 第 23 集（Fermat 最後定理） |
| QR 是 $U_p$ 的子群 | 第 11–12 集（循環群、$U_p$ 的結構） |

---

## 附：本集一句話總結

> **模奇質數 $p$，非零的平方值恰有一半（$(p-b)^2\equiv b^2$）；Legendre 符號 $\left(\frac ap\right)=\pm1$ 是乘法的（「像負號」），而二次互反律說 $\left(\frac qp\right)$ 和 $\left(\frac pq\right)$ 相等、只有 $p\equiv q\equiv3\ (\mathrm{mod}\ 4)$ 時差一個負號——配合 $-1$ 和 $2$ 的補充律，就能一路翻轉、化簡算出任何 Legendre 符號。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-13 課堂錄影（上）逐字稿（YouTube 自動字幕，59:51）與 Jones & Jones《Elementary Number Theory》第 7 章整理；講者課堂內容取材自 Silverman《A Friendly Introduction to Number Theory》第 20–22 章。*
