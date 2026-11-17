---
course: Number Theory（2021 秋，線上錄影）
episode: 11
lecture: Lecture 11
date: 待補（2021 秋）
video: https://youtu.be/neymBRqoTZ8
notes: Jones & Jones §2.4 數字判別法（書頁 32–33，PDF 頁 47–48）；§3.1 Lemma 3.5、Example 3.7–3.8（書頁 44–45，PDF 頁 59–60）；Exercise 3.1
---

# 第 11 集 · Lecture 11：模運算的計算與多項式的整數根 [▶ 影片](https://youtu.be/neymBRqoTZ8)

← 上一集：[10-modular-arithmetic](10-modular-arithmetic.md) ｜ [總目錄](README.md) ｜ 下一集：[12-chinese-remainder-theorem](12-chinese-remainder-theorem.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 11 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（26:46，自動字幕）＋ Jones & Jones §2.4、§3.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 進位表示法](#1-進位表示法)
- [2. 9 的規則與八進位的 7 的規則](#2-9-的規則與八進位的-7-的規則)
- [3. 只看最後幾位數](#3-只看最後幾位數)
- [4. 多項式的整數根](#4-多項式的整數根)
- [5. 平方數的餘數與個位數](#5-平方數的餘數與個位數)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】講者補說上一集的暗號是「spoon」；本集暗號是「pokemon」[▶ 00:00](https://youtu.be/neymBRqoTZ8?t=0)、[▶ 26:24](https://youtu.be/neymBRqoTZ8?t=1584)。本集展示模運算對**普通算術**的應用，講者特別喜歡前幾頁：用模運算研究十進位數字的整除性。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1–2 | 9 的規則、八進位的 7 的規則 | §2.4（3 和 11 的規則） |
| 3 | 只需最後三位判斷是否被 40 整除；個位數 | — |
| 4 | 用 mod $m$ 證明多項式沒有整數根 | Lemma 3.5、Example 3.7–3.8 |
| 5 | 平方數 mod 4、mod 10 | Example 1.2、Exercise 3.1 |

---

## 1. 進位表示法

[▶ 00:34](https://youtu.be/neymBRqoTZ8?t=34)

**十進位表示**：$n = a_ka_{k-1}\cdots a_1a_0$（$0\le a_i\le9$）的意思是
$$n = a_k10^k + a_{k-1}10^{k-1} + \cdots + a_1\cdot10 + a_0.$$
（$a_1$ 在十位、$a_0$ 在個位。）

**$b$ 進位表示**：數字 $c_i\in\{0,1,\dots,b-1\}$，
$$n = (c_kc_{k-1}\cdots c_1c_0)_b = c_kb^k + \cdots + c_1b + c_0.$$

【口頭】「digit（數字）」這個字本身就帶有十進位的意味，講者說「我會克服它」；照理十進位也該寫 $(\cdots)_{10}$，但太煩了不寫 [▶ 01:46](https://youtu.be/neymBRqoTZ8?t=106)。

⚠️ 逐字稿缺字：字幕說數字取自「zero through b」，應為 $0$ 到 $b-1$。

---

## 2. 9 的規則與八進位的 7 的規則

### 2.1 9 的規則

[▶ 02:20](https://youtu.be/neymBRqoTZ8?t=140)

**命題**：$9\mid n \iff 9\mid$（$n$ 的數字和）。更強：
$$n \equiv a_k+a_{k-1}+\cdots+a_0\ (\mathrm{mod}\ 9).$$

**證明**：在 $\mathbb{Z}_9$ 裡，$\overline{10} = \bar1$，所以 $\overline{10^j} = \bar1^j = \bar1$。於是
$$\bar n = \bar a_k\,\overline{10^k}+\cdots+\bar a_1\,\overline{10}+\bar a_0 = \bar a_k+\cdots+\bar a_1+\bar a_0 = \overline{a_k+\cdots+a_0}.$$
所以 $n\equiv0\iff$ 數字和 $\equiv0\ (\mathrm{mod}\ 9)$。∎

【口頭】這比小時候的 9 的規則好一點：數字和也可以**先模 9 化簡** [▶ 04:34](https://youtu.be/neymBRqoTZ8?t=274)。

**例**：$n = 345677809$ [▶ 05:05](https://youtu.be/neymBRqoTZ8?t=305)

數字和 $3+4+5+6+7+7+8+0+9$。模 9 時湊 9 丟掉：$4+5 = 9\to0$；$9\to0$；剩下 $3+6+7+7+8+0 = 31$……講者的分組最後得到 4。（直接加：總和 49，$49 = 45+4$。）所以 $n$ 不被 9 整除，餘數是 4。

### 2.2 八進位的 7 的規則

[▶ 06:10](https://youtu.be/neymBRqoTZ8?t=370)

【口頭】講者在海軍工作過一年。資料有時不知道是十進位還是八進位，八進位的麻煩在於它看起來就像十進位（只用 0–7，沒有怪符號，也不只 0 和 1）。十六進位用 A–F 表示 10–15 [▶ 06:43](https://youtu.be/neymBRqoTZ8?t=403)。

**命題**：八進位數 $n = (a_k\cdots a_1a_0)_8$ 滿足
$$n\equiv a_k+\cdots+a_1+a_0\ (\mathrm{mod}\ 7).$$
理由同上：$8\equiv1\ (\mathrm{mod}\ 7)$，所以 $8^j\equiv1$。

**例** [▶ 07:49](https://youtu.be/neymBRqoTZ8?t=469)：$(3420137)_8$：$3+4+2+0+1+3+7 = 20\equiv6\ (\mathrm{mod}\ 7)$。不被 7 整除。

【口頭】類似的還有十進位的 11 的規則，可能當作業 [▶ 08:22](https://youtu.be/neymBRqoTZ8?t=502)。

> 【課本補充】§2.4（p. 32–33）：
> - **3 的規則**：$10^i = (9+1)^i = 9q+1$，所以 $n = 9m+\sum a_i$，$3\mid n\iff3\mid\sum a_i$。例：$21497$ 數字和 23，不被 3 整除。
> - **11 的規則**：$10^i = (11-1)^i = 11q+(-1)^i$，所以 $11\mid n\iff11\mid a_0-a_1+a_2-\cdots$（交錯和）。例：$21497$ 的交錯和 $7-9+4-1+2 = 3$，不被 11 整除。
> - 2 和 5 只看個位數。

---

## 3. 只看最後幾位數

### 3.1 被 40 整除

[▶ 08:54](https://youtu.be/neymBRqoTZ8?t=534)

**問題**：要看幾位數才能判斷 $40\mid n$？

$40 = 2^3\cdot5$。在 $\mathbb{Z}_{40}$：
- $\overline{100} = \overline{20}$；
- $\overline{1000} = \bar0$（$1000 = 25\cdot40$），所以 $j\ge3$ 時 $\overline{10^j} = \bar0$。

於是
$$\bar n = \overline{100a_2+10a_1+a_0} = \overline{20a_2+10a_1+a_0}.$$
所以
$$40\mid n\iff 20a_2+10a_1+a_0\equiv0\ (\mathrm{mod}\ 40).$$
**只需要最後三位數。**

⚠️ 逐字稿缺字：[▶ 09:27](https://youtu.be/neymBRqoTZ8?t=567) 字幕說「$10^j$ is zero bar for $j\ge4$」，但 $1000\equiv0$ 已經成立，應為 $j\ge3$；講者接著也說只需最低三位。

### 3.2 個位數

[▶ 10:35](https://youtu.be/neymBRqoTZ8?t=635)

個位數 = $n$ 模 10。

**例 1**：$9!+11!+13!$ 的個位數。$9! = 9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2$ 含 $2\cdot5 = 10$；$11!$、$13!$ 都含 10。三項都 $\equiv0$，個位數是 0。

【口頭】從 $5!$ 開始，階乘的個位數都是 0（$5!=120$、$6!=720$、$7!=5040$），所以這例子用常識就行 [▶ 12:16](https://youtu.be/neymBRqoTZ8?t=736)。

**例 2**：$3^{10}\cdot7^3\cdot2^8$ 的個位數 [▶ 12:48](https://youtu.be/neymBRqoTZ8?t=768)

模 10：
- $3^{10} = (3^2)^5 = 9^5\equiv(-1)^5 = -1$。
- $7\equiv-3$，$7^3\equiv(-3)^3 = -27$。
- $2^8 = 2^4\cdot2^4 = 16\cdot16\equiv6\cdot6$。

$$(-1)(-27)\cdot36 \equiv 27\cdot6 \equiv (-3)\cdot6 = -18\equiv2\ (\mathrm{mod}\ 10).$$
個位數是 2。（筆記用 Python 驗證：$3^{10}\cdot7^3\cdot2^8\bmod10 = 2$。）

【口頭】把 7 換成 $-3$、9 換成 $-1$ 這種「負代表」很好用；$2^8$ 拆成 $2^4\cdot2^4$「我也不知道為什麼，有時就是亂玩」[▶ 13:20](https://youtu.be/neymBRqoTZ8?t=800)。

---

## 4. 多項式的整數根

### 4.1 化簡多項式

[▶ 14:25](https://youtu.be/neymBRqoTZ8?t=865)

$f(x) = a_nx^n+\cdots+a_1x+a_0$，$a_i\in\mathbb{Z}$。定義模 $m$ 的**化簡多項式**（reduced polynomial）
$$\tilde f(x) = \bar a_nx^n+\cdots+\bar a_1x+\bar a_0,\qquad \bar a_i\in\mathbb{Z}_m.$$
（講者用 $n$ 表示次數、$m$ 表示模數。）

**關鍵觀察**：對任何整數 $c$，
$$\tilde f(\bar c) = \bar a_n\bar c^n+\cdots+\bar a_0 = \overline{a_nc^n+\cdots+a_0} = \overline{f(c)}.$$
所以若 $f(c) = 0$，則 $\tilde f(\bar c) = \bar0$。

**逆否**：若對**每個** $\bar c\in\mathbb{Z}_m$ 都有 $\tilde f(\bar c)\neq\bar0$，則 $f$ **沒有整數根** [▶ 16:09](https://youtu.be/neymBRqoTZ8?t=969)。（若有整數根 $c$，它一定落在某個同餘類 $\bar c$ 裡，使 $\tilde f(\bar c)=\bar0$。）

> 【課本補充】Lemma 3.5（p. 44）：若 $a\equiv b\ (\mathrm{mod}\ n)$，則 $f(a)\equiv f(b)\ (\mathrm{mod}\ n)$（由 $a^i\equiv b^i$ 逐項得到）。所以只要檢查一組完全剩餘系 $x_1,\dots,x_n$ 的 $f(x_i)$ 有沒有被 $n$ 整除。

### 4.2 例子

**例 1**：$f(x) = x^5-x^2+x-19$ [▶ 16:43](https://youtu.be/neymBRqoTZ8?t=1003)

- 為什麼用 mod 4：mod 2 時 $\tilde f(\bar1) = \overline{1-1+1-19} = \overline{-18} = \bar0$，方法失敗；mod 3 也不行。mod 4 是第一個成功的。
- 模 4：$-19 = -20+1\equiv1$，所以 $\tilde f(x) = x^5-x^2+x+\bar1$。

| $\bar c$ | $\bar0$ | $\bar1$ | $\bar2$ | $\bar3$ |
|---|---|---|---|---|
| $\tilde f(\bar c)$ | $\bar1$ | $\bar2$ | $\bar3$ | $\bar2$ |

（例：$\tilde f(\bar2) = 32-4+2+1 = 31\equiv3$。）沒有一個是 $\bar0$，所以 $f$ **沒有整數根**。

⚠️ 講者一開始說「所以在 $\mathbb{Z}$ 上不可約」，然後自己更正 [▶ 18:29](https://youtu.be/neymBRqoTZ8?t=1109)：這只證明**沒有整數根**，不能排除像（四次）×（一次以上）……例如二次乘三次那樣的分解；這留給抽象代數課。

> 【課本補充】課本 Example 3.7（p. 45）用的是 $x^5-x^2+x-3$（$-3\equiv-19\equiv1\ (\mathrm{mod}\ 4)$，化簡後一樣），並說明 4 是使這方法成功的最小模數；選模數要靠洞察、經驗或試誤，失敗時多試幾個，**不要**因此以為一定有根。

**例 2**：$f(x) = x^7+9x+3$ 沒有整數根 [▶ 19:37](https://youtu.be/neymBRqoTZ8?t=1177)

模 2：$\bar9 = \bar1$、$\bar3 = \bar1$，$\tilde f(x) = x^7+x+\bar1$。
- $\tilde f(\bar0) = \bar1$；
- $\tilde f(\bar1) = \bar1+\bar1+\bar1 = \bar1$。

都不是 $\bar0$，沒有整數根。

### 4.3 這方法的極限

[▶ 20:44](https://youtu.be/neymBRqoTZ8?t=1244)

Jones & Jones p. 45（Example 3.8）的例子：
$$f(x) = (x^2-13)(x^2-17)(x^2-221).$$
- 根 $\pm\sqrt{13},\pm\sqrt{17},\pm\sqrt{221}$ 都不是整數，所以**沒有整數根**。
- 但對**每個**模數 $n$，$f(x)\equiv0\ (\mathrm{mod}\ n)$ 都有解（課本 Example 7.16 會證）。所以這個方法對它**永遠找不到**合適的模數。

教訓：這方法只能用來證明「**沒有**整數根」；在 $\mathbb{Z}_n$ 有根（或可約）**不代表**在 $\mathbb{Z}$ 有根（或可約）[▶ 21:56](https://youtu.be/neymBRqoTZ8?t=1316)。

⚠️ 逐字稿缺字：[▶ 20:44](https://youtu.be/neymBRqoTZ8?t=1244) 字幕把第二個因式唸成「x squared minus 7」，後面講根時說「square root of 17」，課本是 $x^2-17$。字幕還說「which means f tilde has no zero in Z_n」，意思正好相反：$\tilde f$ 在每個 $\mathbb{Z}_n$ 都有零點。

---

## 5. 平方數的餘數與個位數

**平方數模 4** [▶ 22:29](https://youtu.be/neymBRqoTZ8?t=1349)：$x = n^2$ ⇒ $\bar x = \bar n^2$。在 $\mathbb{Z}_4$ 檢查：
$$\bar0^2=\bar0,\quad\bar1^2=\bar1,\quad\bar2^2=\bar0,\quad\bar3^2=\bar1.$$
所以平方數除以 4 餘 0 或 1。（第 4 集證過，這次更簡單。）

**平方數的個位數**（模 10）[▶ 23:02](https://youtu.be/neymBRqoTZ8?t=1382)：

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| $n^2$ | 0 | 1 | 4 | 9 | 16 | 25 | 36 | 49 | 64 | 81 |
| mod 10 | 0 | 1 | 4 | 9 | 6 | 5 | 6 | 9 | 4 | 1 |

平方數的個位數只可能是 **0, 1, 4, 5, 6, 9**。不管數多大都一樣：$365368^2$ 個位 4、$55551^2$ 個位 1、$873^2$ 個位 9 [▶ 24:08](https://youtu.be/neymBRqoTZ8?t=1448)。

（講者總結時字幕漏唸了 1，說成「0 4 5 6 or 9」；表格裡有 1。）

同樣可以用 $\bar0,\dots,\bar9$ 的立方找出立方數可能的個位數。

> 【課本補充】Exercise 3.1（p. 38）：證明平方數的個位數不可能是 2、3、7、8。Example 3.2：$22051946\equiv46\equiv2\ (\mathrm{mod}\ 4)$，所以不是平方數。

【口頭】掌握模運算後，很多具體的算術問題都能解決，否則會困難得多。這是 Gauss 天才的一部分：他精通同餘計算，所以能在很年輕時（講者說「不到我一半年紀」）寫出他的傑作 [▶ 25:50](https://youtu.be/neymBRqoTZ8?t=1550)。

---

## 6. 一頁速查表

**進位**：$n = \sum a_i10^i$；$b$ 進位 $n = \sum c_ib^i$，$0\le c_i<b$。

**數字規則**（關鍵：底數模 $m$ 的值）
- $10\equiv1\ (\mathrm{mod}\ 9)$ ⇒ $n\equiv$ 數字和（mod 9，也就 mod 3）。$345677809\equiv4$。
- $8\equiv1\ (\mathrm{mod}\ 7)$ ⇒ 八進位數 $\equiv$ 數字和（mod 7）。$(3420137)_8\equiv6$。
- 【課本】$10\equiv-1\ (\mathrm{mod}\ 11)$ ⇒ $n\equiv$ 交錯和（mod 11）。
- $1000\equiv0\ (\mathrm{mod}\ 40)$ ⇒ $n\equiv20a_2+10a_1+a_0$，只看最後三位。
- 個位數 = mod 10。$3^{10}7^32^8\equiv(-1)(-27)(36)\equiv2$。

**多項式的整數根**
- $\tilde f(\bar c) = \overline{f(c)}$。若某個 $m$ 使 $\tilde f$ 在 $\mathbb{Z}_m$ 沒有零點 ⇒ $f$ 沒有整數根。
- $x^5-x^2+x-19$（mod 4：值 1,2,3,2）；$x^7+9x+3$（mod 2：值 1,1）。
- 只證「沒有整數根」，不證不可約。
- 反例：$(x^2-13)(x^2-17)(x^2-221)$ 沒有整數根，但每個模數下都有根。

**平方數**：mod 4 餘 0、1；個位數只有 0, 1, 4, 5, 6, 9。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 化簡多項式、模 $m$ 的根 | 第 13 集（多項式同餘、Lagrange 定理） |
| $(x^2-13)(x^2-17)(x^2-221)$ 每個模數都有根 | 第 17–18 集（二次剩餘；課本 Example 7.16） |
| 平方數 mod 4 | 第 21 集（平方和：$4k+3$ 不是兩平方和） |
| 拆模數 $40 = 8\cdot5$ 的想法 | 第 12 集（中國剩餘定理；課本 Theorem 3.4） |

---

## 附：本集一句話總結

> **模運算把數字問題變成小計算：$10\equiv1\ (\mathrm{mod}\ 9)$ 給出 9 的規則、$1000\equiv0\ (\mathrm{mod}\ 40)$ 說只需看最後三位；而 $\tilde f(\bar c)=\overline{f(c)}$ 表示只要某個 $\mathbb{Z}_m$ 裡 $\tilde f$ 沒有零點，$f$ 就沒有整數根——但反過來不成立。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 11 錄影逐字稿（YouTube 自動字幕，26:46）與 Jones & Jones《Elementary Number Theory》§2.4、§3.1 整理。*
