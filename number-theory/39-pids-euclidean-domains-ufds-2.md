---
course: Number Theory（2021 秋，線上錄影）
episode: 39
lecture: 2021-11-08 第 2 部
date: 2021-11-08
video: https://youtu.be/uqJKPJkNJks
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.7 Lecture 27（p. 157–158）：Theorem 4.7.9–4.7.10、Example 4.7.11；§4.8 Lecture 28（p. 159–164）：Definition 4.8.1、Example 4.8.2–4.8.5、Definition 4.8.6、Theorem 4.8.7–4.8.8、Corollary 4.8.9、Theorem 4.8.10、Corollary 4.8.11、Eisenstein 證明、Example 4.8.12
---

# 第 39 集 · PID 裡質 ⇔ 不可約、Euclid 整環 ⇒ PID ⇒ UFD（PIDs, Euclidean Domains, and UFDs, Quick Overview, Part 2） [▶ 影片](https://youtu.be/uqJKPJkNJks)

← 上一集：[38-pids-euclidean-domains-ufds-1](38-pids-euclidean-domains-ufds-1.md) ｜ [總目錄](README.md) ｜ 下一集：[40-extension-fields-1](40-extension-fields-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 39 集（2021-11-08 第 2 部，接第 38 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（32:37，自動字幕；講者後半改用投影片講講義）＋ 講者講義 §4.7–4.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 相伴元生成同一個理想](#1-相伴元生成同一個理想)
- [2. PID 裡：質 ⇔ 不可約](#2-pid-裡質--不可約)
- [3. 哪些是 PID？](#3-哪些是-pid)
- [4. Euclid 整環](#4-euclid-整環)
- [5. 歷史：從唯一分解到理想](#5-歷史從唯一分解到理想)
- [6. 唯一分解整環（UFD）](#6-唯一分解整環ufd)
- [7. 升鏈條件與 PID ⇒ UFD](#7-升鏈條件與-pid--ufd)
- [8. Euclid 整環 ⇒ PID，反方向都不對](#8-euclid-整環--pid反方向都不對)
- [9. Eisenstein 判別法的證明（更正）](#9-eisenstein-判別法的證明更正)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者改用投影機直接講講義，快速帶過 Lecture 27 剩下的部分和 Lecture 28：**Euclid 整環 ⇒ PID ⇒ UFD**。他想趕在這部講完，「下次要開始講擴張體，那個我想花多一點時間」。

---

## 1. 相伴元生成同一個理想

[▶ 00:33](https://youtu.be/uqJKPJkNJks?t=33)

> **定理**（講義 Theorem 4.7.9）：$R$ 是有單位元的交換環。
> - 若 $a,b$ 相伴，則 $\langle a\rangle = \langle b\rangle$。
> - 若 $R$ 是整環、$I = \langle a\rangle$，則 $I$ 的其他生成元都跟 $a$ 相伴。

講者：要知道整環裡一個主理想**所有可能的生成元**，只要看相伴元。

**例**：高斯整數裡 $\langle 3+2i\rangle$ 有 4 個生成元：$\pm(3+2i)$、$\pm i(3+2i)$——非零高斯整數恰有 4 個相伴元（自己加另外 3 個）。

講者說證明「不太刺激」，只是照相伴和主理想的定義直接論證，讓大家自己讀。

> 【講義補充】證明（p. 157）：
> - $b = au$ ⇒ $\langle b\rangle\subseteq\langle a\rangle$；$a = bu^{-1}$ ⇒ $\langle a\rangle\subseteq\langle b\rangle$。
> - $\langle c\rangle = \langle a\rangle$，$a\neq0$：$a = rc$、$c = sa$ ⇒ $a = (rs)a$ ⇒（消去律）$rs = 1$，$r$ 是單位。

**不是整環呢？** [▶ 02:05](https://youtu.be/uqJKPJkNJks?t=125) 講者的「招牌非整環」$\mathbb{Z}_6$：$\langle 2\rangle = \langle 4\rangle = \{0,2,4\}$。2 和 4 相伴嗎？$2\cdot5 = 10\equiv4$，而 5 是單位，**是相伴的**。所以第二部分在非整環也**可能**成立。真正的反例（同一個理想、生成元不相伴）要找「更奇怪的東西」——講義放了 math.stackexchange 的連結，「我放連結的反例，你可以放心它很醜，我懶得打」。

---

## 2. PID 裡：質 ⇔ 不可約

[▶ 03:35](https://youtu.be/uqJKPJkNJks?t=215)

> **定理**（講義 Theorem 4.7.10）：**在 PID 裡，一個元素是質元 ⇔ 它是不可約元。**

講者：上一個定理（第 38 集）說整環裡「質 ⇒ 不可約」；這次是 PID，**兩個方向都對**。

**證明**：

- **(⇒)**：PID 是整環，用第 38 集 Theorem 4.7.8。
- **(⇐)** [▶ 04:39](https://youtu.be/uqJKPJkNJks?t=279)：設 $a$ 不可約，$a\mid bc$。要證 $a\mid b$ 或 $a\mid c$。

1. 定義 $I = \{ax+by : x,y\in D\}$（$a$ 和 $b$ 的「線性組合」）。講者：「這個構造我在很多地方看過。」
2. **$I$ 是理想** [▶ 05:40](https://youtu.be/uqJKPJkNJks?t=340)：
   - 差：$(ax+by)-(ax'+by') = a(x-x')+b(y-y')\in I$；
   - 超級封閉：$r(ax+by) = a(rx)+b(ry)\in I$。
3. **PID**：$I = \langle d\rangle$ [▶ 06:42](https://youtu.be/uqJKPJkNJks?t=402)。
4. $a = a\cdot1+b\cdot0\in I$，所以 $a = rd$。$a$ 不可約 ⇒ $r$ 或 $d$ 是單位。
5. **$d$ 是單位**：$1 = dd'\in I$，所以 $1 = ax+by$。乘 $c$ [▶ 07:12](https://youtu.be/uqJKPJkNJks?t=432)：
   $$c = acx+(bc)y.$$
   $a\mid acx$（顯然），$a\mid bc$（假設），整除兩項就整除和，所以 **$a\mid c$**。
6. **$r$ 是單位** [▶ 07:42](https://youtu.be/uqJKPJkNJks?t=462)：$a = rd$ ⇒ $a,d$ 相伴 ⇒（Theorem 4.7.9）$\langle a\rangle = \langle d\rangle = I$。$b = a\cdot0+b\cdot1\in I = \langle a\rangle$，$b = a\lambda$，**$a\mid b$**。
7. 所以 $a$ 是質元。∎

> 以下**不是逐字稿內容**，是補一句對照：這就是第 4–5 集整數的論證——Bézout（$1 = ax+by$）乘 $c$ 推出 Euclid 引理。PID 的角色就是保證「$a,b$ 的線性組合」是一個主理想，相當於 gcd 存在。

> 【講義補充】講義（p. 158）：「PID 讓我們可以隨便互換質和不可約的概念。有點像那些新車，鼓勵你不要看路。」（註腳：「現在的廣告教我開車做白日夢很酷。」）

---

## 3. 哪些是 PID？

[▶ 08:43](https://youtu.be/uqJKPJkNJks?t=523)

**$\mathbb{Z}[\sqrt{-3}]$ 不是 PID**：第 38 集找到 $1+\sqrt{-3}$ 不可約但不是質元，跟定理 4.7.10 矛盾。

⚠️ 字幕這裡講者說「我們找到一個**質元**不是不可約元」，跟第 38 集的結論（**不可約但不是質**）相反；依第 38 集和定理 4.7.10 的邏輯，應該是「不可約但不是質」。屬口誤或字幕錯，不影響結論，所以不列進待確認清單。

**$\mathbb{Z}$ 是 PID** [▶ 09:14](https://youtu.be/uqJKPJkNJks?t=554)：講者說「我通常在這種課某個時候證它，不知道怎麼這次沒發生」（學生：「放期末考就好」）。證明方法：

1. 取 $\mathbb{Z}$ 的理想 $I\neq\{0\}$，看它的正元素。
2. **良序原理**取最小的正元素 $n$。
3. 論證 $n$ 生成全部（除法演算法，跟第 36 集 $F[x]$ 的證明一樣）。
4. 所以每個理想都是 $n\mathbb{Z}$。

**所以在 $\mathbb{Z}$ 裡質 ⇔ 不可約** [▶ 10:16](https://youtu.be/uqJKPJkNJks?t=616)——這就是為什麼新定義「不違反」整數的舊定義。

**$F[x]$（$F$ 體）是 PID**，所以多項式的不可約和質也可以互換。講者 [▶ 10:47](https://youtu.be/uqJKPJkNJks?t=647)：「這也幫你理解為什麼抽象代數花了一點時間才把這些概念分開——在大部分常見的例子裡，它們糾纏在一起。」

**$\mathbb{Z}[x]$ 不是 PID** [▶ 11:18](https://youtu.be/uqJKPJkNJks?t=678)：Gallian 的例子 $\langle 2,x\rangle$ 需要兩個生成元，找不到一個生成它。（但 $\mathbb{Z}[x]$ 是整環：整環上的多項式環還是整環。）

> 以下**不是逐字稿內容**，是補 $\langle 2,x\rangle$ 為什麼不是主理想：若 $\langle 2,x\rangle = \langle f\rangle$，則 $f\mid 2$，所以 $f = \pm1$ 或 $\pm2$。$f = \pm2$ 不行（$2\nmid x$）；$f = \pm1$ 則 $1\in\langle2,x\rangle$，即 $1 = 2g(x)+xh(x)$，代 $x = 0$ 得 $1 = 2g(0)$，整數裡不可能。

---

## 4. Euclid 整環

[▶ 11:48](https://youtu.be/uqJKPJkNJks?t=708)

> **定義**（講義 Definition 4.8.1）：整環 $D$ 是 **Euclid 整環**（Euclidean domain），如果有一個範數 $N$，使得對任何 $a,b\in D$、$b\neq0$，存在 $q,r$：
> $$a = qb+r,\qquad r = 0\ \text{或}\ N(r)<N(b).$$

也就是**有除法演算法，餘數用範數量起來比較小**。

講者說這些以前講過（第 16 集高斯整數的除法），會略過一些：

- **餘數不唯一**（講義 Ex 4.8.2）：$54 = 6\cdot8+6 = 7\cdot8-2$。
- **$F[x]$ 是 Euclid 整環**（Ex 4.8.3）[▶ 12:49](https://youtu.be/uqJKPJkNJks?t=769)，範數是**次數**——「這對我們是新的」。注意：這裡**單位是範數 0**（非零常數），不像 $\mathbb{Z}[\sqrt d]$ 是範數 1。「一般的範數不是每件事都一樣。」（次數的範數也不是乘性的：$\deg(fg) = \deg f+\deg g$。）
- **高斯整數是 Euclid 整環**（Ex 4.8.4），$N(a+bi) = a^2+b^2$，我們看過怎麼做除法。

> 【講義補充】Example 4.8.4（p. 159–160）的證明概要：把 $\frac{a+bi}{c+di}$ 當複數 $z$，取最近的格點 $q\in\mathbb{Z}[i]$。最壞情況 $z$ 在方格正中央，離 4 個格點都是 $\frac1{\sqrt2}$，所以 $\left|\frac r{c+di}\right|<\frac1{\sqrt2}$，$N(r)<\frac12N(c+di)$。換成 $\mathbb{Z}[\sqrt{-d}]$（$d$ 大）時這個幾何論證就壞了。

**理想的和、互極大** [▶ 13:49](https://youtu.be/uqJKPJkNJks?t=829)：講者說這是大家作業「幾乎做對」的東西。

- **理想的和**：$A+B = \{x+y : x\in A,\ y\in B\}$。
- 兩個高斯整數的 gcd 是單位時，$\langle\alpha\rangle+\langle\beta\rangle$ 是整個環。這種理想叫**互極大**（comaximal）。
- 「互極大是**互質**的理想版本」：整數 $a,b$ 互質 ⇒ $ak+bl = 1$ ⇒ $\langle a\rangle+\langle b\rangle = \mathbb{Z}$。

> 【講義補充】Example 4.8.5（p. 160）：在 $\mathbb{Z}[i]$ 對 $\alpha = 11+3i$、$\beta = 2+3i$ 做 Euclid 演算法：
> $$(\alpha,\beta)\to(\beta,\ \alpha-(2-2i)\beta) = (2+3i,\ 1+i)\to(1+i,\ -i).$$
> $-i$ 是單位，停。倒推得
> $$1 = (4+9i)(2+3i)+(1-3i)(11+3i),$$
> 所以 $\gcd = 1$（或 $-1,\pm i$），$\langle 11+3i\rangle+\langle 2+3i\rangle = \mathbb{Z}[i]$。

【Q&A】[▶ 15:22](https://youtu.be/uqJKPJkNJks?t=922) 學生：元素有「質」和「不可約」，理想有「質理想」，但沒有「不可約理想」，而是叫「極大理想」——元素和理想之間有某種對應。「我們在重新發現抽象代數很小眾的東西，**是不是因為數論學家看到太多連結和模式，才走向更抽象的代數？**」講者：「我想是的，這是很好的解釋。他們研究很難的問題，找到模式，想在最一般的情況下解釋模式什麼時候發生，這導向了抽象代數的計畫。」

---

## 5. 歷史：從唯一分解到理想

[▶ 16:23](https://youtu.be/uqJKPJkNJks?t=983)

講者（「我講課很馬基維利——壞事一次做完」，請大家再給他 10 分鐘）講講義 p. 161 的故事：

- **Euler、Lagrange** 已經在用代數整數，像高斯整數。
- 「高斯整數」這名字有點諷刺：**Gauss** 某種意義上更要為**遠離**這種論證負責。他的《算術研究》（Disquisitiones Arithmeticae）全用模運算，基本上不用這些花俏的數系。
- 我們看過高斯整數對 $4n+1$、$4n+3$ 型質數、平方和給出很漂亮的論證（第 15–20 集）；其他質數也有用其他數系的類似論證。
- Gauss 沒投入那種想法，因為他**知道唯一分解的問題**：有些數系失去唯一分解。
- 這**誘使 Lamé** 寫出費馬最後定理的錯誤證明——基於**分圓整數**的唯一分解。
- **Kummer** 引入**理想數**（ideal numbers）修正——「基本上是把理想提升為數」。
- **Dedekind** 把它充實起來，啟發了 **Emmy Noether**。

【口頭】[▶ 18:25](https://youtu.be/uqJKPJkNJks?t=1105) Noether 常對學生說「**一切都已經在 Dedekind 裡了**」（Es steht schon bei Dedekind）。講者：這低估了 Noether 的貢獻，「現代意義的抽象代數可以說是從 Noether 和她的學生開始的」，大約 1920 年代。「她比較早過世，好像是手術併發症，如果我沒記錯；不然她的名字在這個故事裡會大得多。」

講者：要修正唯一分解，**得用理想而不是數**——「這是我們要去的地方，感恩節後，大概是最後講的東西」。（第 46–47 集。）

---

## 6. 唯一分解整環（UFD）

[▶ 19:25](https://youtu.be/uqJKPJkNJks?t=1165)

> **定義**（講義 Definition 4.8.6）：整環 $D$ 是**唯一分解整環**（unique factorization domain，UFD），如果
> 1. 每個非零、非單位的元素都能寫成不可約元的乘積；
> 2. 分解在**順序和相伴**之外唯一：若 $x = x_1x_2\cdots x_n = y_1y_2\cdots y_n$，則存在單位 $u_1,\dots,u_n$ 使
> $$\{y_1,\dots,y_n\} = \{u_1x_1,\dots,u_nx_n\}$$
> （集合相等，不代表順序）。

講者：「我很喜歡這個寫法。我們一直在跟這個記號搏鬥，這是捕捉『重排之外唯一』很漂亮的方式。」兩種分解的因式要能一一配成相伴元。

（講義：$\mathbb{Z}$ 的單位 $\pm1$、$F[x]$ 的單位是非零常數，所以「相伴之外」很好理解。）

---

## 7. 升鏈條件與 PID ⇒ UFD

**升鏈條件** [▶ 20:28](https://youtu.be/uqJKPJkNJks?t=1228)：

> **定理**（講義 Theorem 4.8.7）：在 PID 裡，任何**嚴格遞增**的理想鏈 $I_1\subsetneq I_2\subsetneq\cdots$ 長度都有限。

講者：「看起來是很奇怪的話吧？證明會幫你解釋。」（講義說這個鏈條件論證來自 Noether 的影響。）

**證明**：

1. $I = I_1\cup I_2\cup\cdots$ 是理想（講者：「細節我沒寫，你可以試試：差、超級封閉。」）
2. PID：$I = \langle d\rangle$。
3. $d\in I$，所以 $d\in I_n$ 對某個 $n$ [▶ 21:30](https://youtu.be/uqJKPJkNJks?t=1290)。
4. 每個 $I_i\subseteq I = \langle d\rangle\subseteq I_n$。所以 $I_n$ 是最後一個——再往後就會有不由 $d$ 生成的東西，不可能。∎

講者 [▶ 22:34](https://youtu.be/uqJKPJkNJks?t=1354)：「如果你跟我一樣，第一次讀會想：這跟唯一分解到底有什麼關係？」

> **定理**（講義 Theorem 4.8.8）：**每個 PID 都是 UFD。**

（講義：「這大概是本學期最有趣的證明。」）

設 $a_0\neq0$、不是單位。計畫：

**(1) $a_0$ 的分解至少含一個不可約元** [▶ 23:35](https://youtu.be/uqJKPJkNJks?t=1415)：

- $a_0$ 不可約就做完了。
- 否則 $a_0 = a_1b_1$，$a_1$ 不是單位、$b_1\neq0$（$b_1$ 也不是單位）。$a_1$ 不可約就做完了；否則 $a_1 = a_2b_2$……
- $a_n = a_{n+1}b_{n+1}$ ⇒ $\langle a_n\rangle\subseteq\langle a_{n+1}\rangle$，而且**不相等**：$a_n,a_{n+1}$ 不相伴（$b_{n+1}$ 不是單位），用 Theorem 4.7.9 [▶ 24:37](https://youtu.be/uqJKPJkNJks?t=1477)。
- 升鏈條件 ⇒ 鏈 $\langle a_0\rangle\subsetneq\langle a_1\rangle\subsetneq\cdots\subsetneq\langle a_k\rangle$ 會停 ⇒ $a_k$ 不能再分 ⇒ **$a_k$ 不可約**，$a_0 = ra_k$。

講者：「對我來說這是極度狡猾的論證，我一百萬年也想不到。」

**(2) $a_0$ 能分解成不可約元的乘積** [▶ 25:09](https://youtu.be/uqJKPJkNJks?t=1509)：由 (1)，$a_0 = p_1c_1$（$p_1$ 不可約）。$c_1$ 不可約就做完；否則 $c_1 = p_2c_2$……又得到升鏈 $\langle a_0\rangle\subsetneq\langle c_1\rangle\subsetneq\langle c_2\rangle\subsetneq\cdots$，必須停，所以
$$a_0 = p_1p_2\cdots p_t.$$

（⚠️ 講義和講者都把第二條鏈寫成 $\langle a_0\rangle\subset\langle p_1\rangle\subset\langle p_2\rangle\subset\cdots$；以下**不是逐字稿內容**，是依 (2) 的構造推論的：會一直變大的是 $\langle c_1\rangle\subsetneq\langle c_2\rangle$（因為 $c_i = p_{i+1}c_{i+1}$、$p_{i+1}$ 不是單位），所以這裡寫成 $c_i$ 的鏈。結論不變，不列進待確認清單。）

講者 [▶ 26:14](https://youtu.be/uqJKPJkNJks?t=1574)：讓這些升鏈論證成立的關鍵是什麼？**PID**——升鏈條件的證明靠它。

**(3) 唯一性**：講者「饒過你們」，不講。

> 【講義補充】(3) 的證明（p. 162–163）：對 $t$ 歸納。$a_0 = p_1\cdots p_t = q_1\cdots q_s$。$p_1$ 不可約，在 PID 裡就是質元（Theorem 4.7.10），所以 $p_1\mid q_j$ 對某個 $j$，又 $q_j$ 不可約，$q_j = u_jp_1$（$u_j$ 單位）。消去 $p_1$（整環消去律），剩下 $t-1$ 個，用歸納假設。講義說幾乎照 Gallian p. 319–320。

**推論**（講義 Corollary 4.8.9）[▶ 26:48](https://youtu.be/uqJKPJkNJks?t=1608)：$F$ 是體 ⇒ $F[x]$ 是 UFD（$F[x]$ 是 PID，PID ⇒ UFD）。講者：「這就是為什麼多項式有唯一分解。不可思議的結果。」

---

## 8. Euclid 整環 ⇒ PID，反方向都不對

> **定理**（講義 Theorem 4.8.10）[▶ 27:20](https://youtu.be/uqJKPJkNJks?t=1640)：**每個 Euclid 整環都是 PID。**
> **推論**（Corollary 4.8.11）：每個 Euclid 整環都是 UFD。

講者：這不是剛才 UFD 那件事的推論；但證明「跟我們以前證過的很接近」，下次再看也行，「先把這張票帶回家：注意它在說什麼」。

> 【講義補充】Theorem 4.8.10 的證明（p. 163）：非零理想 $I$，良序原理取範數最小的 $x_0\in I$；$z = qx_0+r$，$r = z-qx_0\in I$，$r\neq0$ 會比 $x_0$ 範數小，矛盾，所以 $I = \langle x_0\rangle$。講義說：「這跟第 36 集 $F[x]$ 是 PID 的證明幾乎一樣。事後看，那個證明可以跳過，直接用次數當範數套這個一般結果。」

$$\text{Euclid 整環}\ \Rightarrow\ \text{PID}\ \Rightarrow\ \text{UFD}.$$

**反方向都不成立** [▶ 27:54](https://youtu.be/uqJKPJkNJks?t=1674)：

- **UFD ⇏ PID**：$\mathbb{Z}[x]$ 是 UFD（第 38 集），但 $\langle 2,x\rangle$ 不是主理想，所以不是 PID。
- **PID ⇏ Euclid 整環**：例子**難找得多**，講義放了連結。講者 [▶ 29:28](https://youtu.be/uqJKPJkNJks?t=1768)：因為 Euclid 整環的定義「滑溜得多」——要證明**不存在**某種範數，怎麼證？

（講者順口說「沒人用 ED 這個縮寫，不知道為什麼」。）

> 【講義補充】講義（p. 163）：「我期待你知道這些結果，但不期待你能造出一個不是 Euclid 整環的 PID。相反地，**知道 $\mathbb{Z}[x]$ 是 UFD 但不是 PID，正是你該知道的事。**」

> 【講義補充】Example 4.8.12（p. 164）：**$\mathbb{Z}[\sqrt{-5}]$ 不是 UFD**。範數 $a^2+5b^2$，單位只有 $\pm1$。
> $$46 = 2\cdot23 = (1+3\sqrt{-5})(1-3\sqrt{-5}).$$
> 四個因式兩兩不相伴，而且都不可約：$a^2+5b^2 = 2$ 和 $a^2+5b^2 = 23$ 都沒有整數解（$N(2) = 4$、$N(23) = 529$、$N(1\pm3\sqrt{-5}) = 46 = 2\cdot23$）。兩種分解不可能在相伴之外相同。

---

## 9. Eisenstein 判別法的證明（更正）

[▶ 30:01](https://youtu.be/uqJKPJkNJks?t=1801)

講者：「我擔心一件事——我在課堂上講 Eisenstein 時，**有沒有說 $p^2$ 不整除 $a_0$？** 我覺得抄的時候可能漏了。那是很重要的條件，我想我忽略了。」

正確的條件：

- $p\nmid a_n$（首項係數）；
- $p\mid a_{n-1},\dots,a_0$；
- **$p^2\nmid a_0$**（常數項）。

「我們用到的地方它是成立的，我很確定。」（第 36 集的例子 $13x^7+2x^6+4x^3+18x+2$：$4\nmid 2$；$\Phi_p(x+1)$：常數項 $p$，$p^2\nmid p$。）

【Q&A】[▶ 31:35](https://youtu.be/uqJKPJkNJks?t=1895) 學生：你剛說「$p^2$ 必須整除 $a_0$」？講者：「**必須不**整除，我的錯。是的，丟臉。」

**證明的想法**（講者說「很好懂，自己讀」）：

> 【講義補充】證明（p. 164，Gallian 歸功於 Richard Singer）：設 $f = gh$ 在 $\mathbb{Q}$ 上可約，由 Gauss 引理可設 $g,h\in\mathbb{Z}[x]$。
> 1. 模 $p$：$\bar f = \bar a_nx^n$（其他係數都被 $p$ 整除），所以 $\bar a_nx^n = \bar g\,\bar h$。
> 2. **$\mathbb{Z}_p$ 是體，$\mathbb{Z}_p[x]$ 是 UFD**；$x$ 是不可約元，所以 $x\mid\bar g$ 且 $x\mid\bar h$。
> 3. 所以 $\bar g(0) = \bar h(0) = 0$，即 $p\mid g(0)$、$p\mid h(0)$。
> 4. $a_0 = f(0) = g(0)h(0)$，所以 $p^2\mid a_0$，矛盾。∎

講者 [▶ 31:04](https://youtu.be/uqJKPJkNJks?t=1864)：關鍵是 $\mathbb{Z}[x]$ 不是 PID（⚠️ 字幕說「不是 UFD」，但 $\mathbb{Z}[x]$ 是 UFD，應是口誤），但把係數模 $p$ 後**就在體上的多項式環裡工作，那是 UFD**，「最後就逼出 $p^2$ 整除常數項，跟假設矛盾」。

> 以下**不是逐字稿內容**，是補第 2 步為什麼 $x$ 要同時整除兩個：$\bar g\bar h = \bar a_nx^n$，由唯一分解，$\bar g$、$\bar h$ 都是「常數 × $x$ 的次方」。$\deg g,\deg h\ge1$，而且 $\deg\bar g+\deg\bar h = n = \deg g+\deg h$，所以次數都沒降，$\bar g,\bar h$ 都至少含一個 $x$。

講者最後說：想把這些講完，因為**下次要開始講擴張體**，那個想多花時間。

---

## 10. 一頁速查表

**相伴與主理想**：相伴 ⇒ 同一個理想；整環裡主理想的生成元恰好是彼此的相伴元。

**PID 裡質 ⇔ 不可約**。**關鍵一步**：$I = \{ax+by\} = \langle d\rangle$；$d$ 單位 ⇒ $1 = ax+by$ ⇒ $c = acx+bcy$ ⇒ $a\mid c$；$r$ 單位 ⇒ $I = \langle a\rangle\ni b$ ⇒ $a\mid b$。

**升鏈條件**（PID）：嚴格遞增的理想鏈有限長。**關鍵一步**：$\bigcup I_k = \langle d\rangle$，$d$ 落在某個 $I_n$。

**PID ⇒ UFD**：一直分解產生嚴格遞增的主理想鏈，必須停 ⇒ 存在性；唯一性靠「不可約 = 質」。

$$\text{Euclid 整環}\Rightarrow\text{PID}\Rightarrow\text{UFD}\qquad(\text{反方向都不對})$$

| 環 | Euclid | PID | UFD | 備註 |
|---|---|---|---|---|
| $\mathbb{Z}$ | ✔（$|x|$） | ✔ | ✔ | 質 ⇔ 不可約 |
| $F[x]$ | ✔（次數） | ✔ | ✔ | 單位 = 非零常數 |
| $\mathbb{Z}[i]$ | ✔（$a^2+b^2$） | ✔ | ✔ | 4 個單位 |
| $\mathbb{Z}[x]$ | ✘ | ✘（$\langle2,x\rangle$） | ✔ | UFD ⇏ PID |
| $\mathbb{Z}[\sqrt{-3}]$ | ✘ | ✘ | ✘ | $1+\sqrt{-3}$ 不可約不是質 |
| $\mathbb{Z}[\sqrt{-5}]$ | ✘ | ✘ | ✘ | $46 = 2\cdot23 = (1+3\sqrt{-5})(1-3\sqrt{-5})$ |

**互極大**：$\langle a\rangle+\langle b\rangle = R$，互質的理想版本。

**Eisenstein**：$p\nmid a_n$、$p\mid a_j$（$j<n$）、**$p^2\nmid a_0$**。**關鍵一步**：模 $p$ 後 $\bar g\bar h = \bar a_nx^n$，在 UFD $\mathbb{Z}_p[x]$ 裡 $x$ 整除兩者 ⇒ $p^2\mid a_0$。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 擴張體 | 第 40–41 集 |
| $F[x]$ 是 UFD ⇒ 最小多項式 | 第 42–43 集 |
| 唯一分解失敗 ⇒ 改用理想（Kummer、Dedekind） | 第 46–47 集 |

---

## 附：本集一句話總結

> **相伴元生成同一個理想；在 PID 裡質和不可約是同一回事（證明就是 Bézout 推 Euclid 引理），所以整數和體上的多項式不必分清兩者。升鏈條件讓 PID 裡的分解必定停下，得到 PID ⇒ UFD；再加上 Euclid 整環 ⇒ PID，就是 Euclid ⇒ PID ⇒ UFD，反方向都不對（$\mathbb{Z}[x]$ 是 UFD 不是 PID）。講者也更正：Eisenstein 判別法要加上 $p^2\nmid a_0$。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-08 第 2 部錄影逐字稿（YouTube 自動字幕，32:37）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.7–4.8 整理。*
