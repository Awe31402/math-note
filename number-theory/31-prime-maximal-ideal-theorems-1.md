---
course: Number Theory（2021 秋，線上錄影）
episode: 31
lecture: 2021-10-25 第 1 部
date: 2021-10-25
video: https://youtu.be/dcfaKtJTPUo
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.3 Lecture 23（p. 134–136）：Example 4.3.4–4.3.5、Theorem 4.3.6–4.3.7、Example 4.3.8；§4.4 Lecture 24（p. 137–138）：Definition 4.4.1、Example 4.4.2–4.4.4、Theorem 4.4.5–4.4.6；講義說 Example 4.3.4–4.3.5 照 Gallian p. 258–259
---

# 第 31 集 · 質理想與極大理想的定理、環同構（上）（Prime and Maximal Ideal Theorems, Ring Isomorphism, Part 1） [▶ 影片](https://youtu.be/dcfaKtJTPUo)

← 上一集：[30-prime-maximal-ideals-intro](30-prime-maximal-ideals-intro.md) ｜ [總目錄](README.md) ｜ 下一集：[32-prime-maximal-ideal-theorems-2](32-prime-maximal-ideal-theorems-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 31 集（2021-10-25 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；結尾被切斷）＋ 講者講義 §4.3–4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 直接證明 ⟨x² + 1⟩ 在 R[x] 裡是極大理想](#1-直接證明-x--1-在-rx-裡是極大理想)
- [2. ⟨x² + 1⟩ 在 Z₂[x] 裡不是質理想](#2-x--1-在-zx-裡不是質理想)
- [3. R/A 是整環 ⇔ A 是質理想](#3-ra-是整環--a-是質理想)
- [4. R/A 是體 ⇔ A 是極大理想](#4-ra-是體--a-是極大理想)
- [5. 極大 ⇒ 質，反過來不對](#5-極大--質反過來不對)
- [6. 環同態](#6-環同態)
- [7. 例子：自然映射、共軛、求值映射](#7-例子自然映射共軛求值映射)
- [8. 環同態的性質；核是理想（開頭）](#8-環同態的性質核是理想開頭)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:02](https://youtu.be/dcfaKtJTPUo?t=2)

講者先複習：理想（子 rng + 超級封閉）、商環 $R/A$（零是 $0+A = A$，單位元素是 $1+A$），還有上次的質理想、極大理想。「證明今天會用到，所以提醒一下。」

然後：證明上次預告的兩個大定理，再開始講義的 Lecture 24：**環同態**。

| 主題 | 時間 | 講義 |
|---|---|---|
| $\langle x^2+1\rangle$ 極大（直接證） | 03:12 | Ex 4.3.4 |
| $\mathbb{Z}_2[x]$ 的反例 | 11:41 | Ex 4.3.5 |
| 質理想 ⇔ 整環 | 15:03 | Thm 4.3.6 |
| 極大理想 ⇔ 體 | 22:03 | Thm 4.3.7 |
| 極大 ⇒ 質 | 38:43 | Ex 4.3.8 |
| 環同態 | 46:52 | Def 4.4.1 |
| 例子 | 50:06 | Ex 4.4.2–4.4.4 |
| 性質、核 | 55:21 | Thm 4.4.5–4.4.6 |

---

## 1. 直接證明 ⟨x² + 1⟩ 在 R[x] 裡是極大理想

[▶ 03:12](https://youtu.be/dcfaKtJTPUo?t=192)（講義 Example 4.3.4）

講者：「我很想跳過，但不會，我覺得過一遍對我們有益。這個有點難。」

> **主張**：$\langle x^2+1\rangle = \{(x^2+1)f(x) : f\in\mathbb{R}[x]\}$ 是 $\mathbb{R}[x]$ 的極大理想。

（講者說他講義用 $A$ 表示中間的理想，「很不幸的記號混亂」，課堂改用 $B$。）

**證明**：設理想 $B$ 滿足 $\langle x^2+1\rangle\subseteq B\subseteq\mathbb{R}[x]$ 且 $B\neq\langle x^2+1\rangle$。目標：$B = \mathbb{R}[x]$。

1. **找一個 $B$ 裡但不在 $\langle x^2+1\rangle$ 裡的 $f$** [▶ 04:12](https://youtu.be/dcfaKtJTPUo?t=252)。
2. **多項式除法**：$f(x) = q(x)(x^2+1)+r(x)$。
   - 餘數 $r\neq 0$，不然 $f$ 就在 $\langle x^2+1\rangle$ 裡。
   - $\deg r<2$，所以 $r(x) = ax+b$，$a,b$ 不全為 0。
3. **$ax+b\in B$** [▶ 05:45](https://youtu.be/dcfaKtJTPUo?t=345)：$ax+b = f(x)-q(x)(x^2+1)$。$f\in B$；$q(x)(x^2+1)\in\langle x^2+1\rangle\subseteq B$。理想對減法封閉。
4. **$a^2x^2-b^2\in B$** [▶ 07:58](https://youtu.be/dcfaKtJTPUo?t=478)：
   $$a^2x^2-b^2 = (ax+b)(ax-b).$$
   $ax+b\in B$、$ax-b\in\mathbb{R}[x]$，**超級封閉**。
5. **$a^2(x^2+1)\in B$**：它在 $\langle x^2+1\rangle\subseteq B$ 裡。
6. **相減** [▶ 09:01](https://youtu.be/dcfaKtJTPUo?t=541)：
   $$0\neq a^2+b^2 = (a^2x^2+a^2)-(a^2x^2-b^2)\in B.$$
   （$a,b$ 不全為 0，實數平方和大於 0。）
7. **$1\in B$** [▶ 10:07](https://youtu.be/dcfaKtJTPUo?t=607)：$\dfrac1{a^2+b^2}\in\mathbb{R}[x]$，超級封閉：$\dfrac1{a^2+b^2}(a^2+b^2) = 1\in B$。
8. 含 1 的理想就是整個環（第 29 集）。$B = \mathbb{R}[x]$。∎

講者：「這是**直接證明極大性**的典型論證。」

> 以下**不是逐字稿內容**，是補一句第 6 步為什麼要用實數：$a^2+b^2\neq0$ 靠的是「實數的平方和為 0 只有全為 0」。換成 $\mathbb{C}[x]$ 就不行（$x^2+1 = (x+i)(x-i)$ 在那裡可分解，理想不是極大的）。

---

## 2. ⟨x² + 1⟩ 在 Z₂[x] 裡不是質理想

[▶ 11:41](https://youtu.be/dcfaKtJTPUo?t=701)（講義 Example 4.3.5，「比較簡單」）

$\mathbb{Z}_2[x]$：係數在 $\mathbb{Z}_2$ 的多項式。

$$(x+1)^2 = x^2+2x+1 = x^2+1\quad(\text{因為 } 2 = 0).$$

- $(x+1)(x+1) = x^2+1\in\langle x^2+1\rangle$。
- 但 $x+1\notin\langle x^2+1\rangle$ [▶ 12:57](https://youtu.be/dcfaKtJTPUo?t=777)。

【課堂討論】講者問為什麼「顯然」？$x+1\in\langle x^2+1\rangle$ 表示 $x+1 = (x^2+1)f(x)$。「能做到嗎？顯然不能。」

所以兩個元素乘積在理想裡，但兩個都不在——**不是質理想**。

> 以下**不是逐字稿內容**，是補上「顯然不能」：$f\neq 0$ 時右邊次數至少 2，左邊次數 1；$f=0$ 時右邊是 0。都不等於 $x+1$。

（對照：在 $\mathbb{R}[x]$ 裡 $x^2+1$ 不能分解，理想是極大的；在 $\mathbb{Z}_2[x]$ 裡 $x^2+1 = (x+1)^2$ 可分解，理想連質的都不是。）

---

## 3. R/A 是整環 ⇔ A 是質理想

[▶ 15:03](https://youtu.be/dcfaKtJTPUo?t=903)

> **定理**（講義 Theorem 4.3.6）：$R$ 是有單位元素（unity，講者說就是「乘法單位元素的另一個名字」）的可交換環，$A$ 是理想。
> $$R/A\ \text{是整環}\iff A\ \text{是質理想}.$$

【課堂討論】講者問整環的特徵是什麼？學生：沒有零因子。

**(⇒)** [▶ 16:04](https://youtu.be/dcfaKtJTPUo?t=964) 設 $R/A$ 是整環。取 $a,b\in R$、$ab\in A$。

1. $ab\in A$，所以 $ab+A = A$——**這是 $R/A$ 的零** [▶ 18:23](https://youtu.be/dcfaKtJTPUo?t=1103)。
2. 而 $ab+A = (a+A)(b+A)$。兩個東西乘起來是零。
3. $R/A$ 是整環，所以 $a+A = A$ 或 $b+A = A$。
4. 也就是 $a\in A$ 或 $b\in A$。$A$ 是質理想。

**(⇐)** [▶ 19:55](https://youtu.be/dcfaKtJTPUo?t=1195) 設 $A$ 是質理想。取 $a,b\in R$、$(a+A)(b+A) = A$（乘積是零）。

1. $ab+A = A$，所以 $ab\in A$。
2. $A$ 是質理想，所以 $a\in A$ 或 $b\in A$。
3. 也就是 $a+A = A$ 或 $b+A = A$。沒有零因子。∎

【口頭】「這幾乎是雙條件證明。」（講者證到一半發現忘了說「設 $a,b$ 是 $R$ 的元素」，「蠢，但補上」。）

> 【講義補充】Theorem 4.3.6 的證明（p. 135）最後補上：$R/A$ 是有單位元素 $1+A$ 的可交換環（$(r+A)(s+A) = rs+A = sr+A$），所以是整環。
>
> 以下**不是逐字稿內容**：嚴格說還要 $R/A$ 不是零環，也就是 $1+A\neq A$，這需要 $A$ 是**真**理想——質理想的定義本來就要求真理想。

---

## 4. R/A 是體 ⇔ A 是極大理想

[▶ 22:03](https://youtu.be/dcfaKtJTPUo?t=1323)

> **定理**（講義 Theorem 4.3.7）：$R$ 是有單位元素的可交換環，$A$ 是理想。
> $$R/A\ \text{是體}\iff A\ \text{是極大理想}.$$

【課堂討論】講者問體是什麼？學生想到群的公理；講者：有單位元素的可交換環，每個非零元素有乘法反元素。

**應用** [▶ 23:04](https://youtu.be/dcfaKtJTPUo?t=1384)：有了這個定理，第 1 節的例子說 $\mathbb{R}[x]/\langle x^2+1\rangle$ 是體（我們也認得它就是 $\mathbb{C}$）。反過來：**認出商環同構於一個已知的體，就能證明理想是極大的**。「直接證極大性很痛苦；認出某個東西是我們早就知道的體，容易得多。這個定理很有用，能避開例子 4.3.4 的困難。」

講者：「這個證明長一點，但沒難多少。」

**(⇒)** [▶ 24:38](https://youtu.be/dcfaKtJTPUo?t=1478) 設 $R/A$ 是體。取理想 $B$，$A\subseteq B\subseteq R$、$A\neq B$。目標：$B = R$。（「跟今天第一個例子同樣的邏輯。」）

1. 取 $x\in B$、$x\notin A$ [▶ 26:15](https://youtu.be/dcfaKtJTPUo?t=1575)。所以 $x+A\neq A$，是體 $R/A$ 裡的**非零**元素。
2. 有反元素 $y+A$：$(x+A)(y+A) = 1+A$，即 $xy+A = 1+A$。
3. 所以 $1-xy\in A\subseteq B$ [▶ 27:51](https://youtu.be/dcfaKtJTPUo?t=1671)。
4. $x\in B$、$y\in R$，超級封閉：$xy\in B$ [▶ 28:26](https://youtu.be/dcfaKtJTPUo?t=1706)。
5. $1 = (1-xy)+xy\in B$。所以 $B = R$。$A$ 是極大理想。

講者 [▶ 29:56](https://youtu.be/dcfaKtJTPUo?t=1796)：「仔細看，邏輯跟第一個例子完全平行，只是第一個例子陷在 $\langle x^2+1\rangle$ 的技術細節裡。」

**(⇐)** [▶ 30:27](https://youtu.be/dcfaKtJTPUo?t=1827) 設 $A$ 是極大理想。取 $x\in R$、$x\notin A$（$x+A$ 是非零元素）。

（講者把板擦丟到黑板槽差點進，「我可以把 YouTube 頻道改成競技丟白板筆，成為這項運動的代言人」。）

1. **造一個理想** [▶ 32:01](https://youtu.be/dcfaKtJTPUo?t=1921)：
   $$B = \{\,xr+a : r\in R,\ a\in A\,\}.$$
   證明 $B$ 是理想，講者說會出成作業（「很友善的作業」）。
2. **$A\subseteq B$**：$a = x\cdot 0+a\in B$。
3. **$A\neq B$** [▶ 34:49](https://youtu.be/dcfaKtJTPUo?t=2089)：$x = x\cdot1+0\in B$，但 $x\notin A$。講者：「我想我講義的證明漏了這一步，壞壞壞。」
4. **由極大性**：$B = R$，所以 $1\in B$ [▶ 35:56](https://youtu.be/dcfaKtJTPUo?t=2156)。
5. 存在 $r\in R$、$a\in A$ 使 $xr+a = 1$。取陪集（$a$ 被吸進 $A$）：
   $$xr+A = 1+A,\qquad\text{即}\qquad(x+A)(r+A) = 1+A.$$
6. **任意**非零元素 $x+A$ 都有反元素 $r+A$。$R/A$ 是有 1 的可交換環，所以是體。∎

> 【講義補充】Theorem 4.3.7 的證明（p. 135–136）跟課堂一樣。講義的 (⇐) 確實是「By maximality of $A$ we have $B = R$」，沒有先檢查 $A\neq B$——就是講者說的漏洞（若 $B=A$，極大性給不出 $B=R$）。

---

## 5. 極大 ⇒ 質，反過來不對

[▶ 38:43](https://youtu.be/dcfaKtJTPUo?t=2323)

講者問：質理想和極大理想有什麼關係？

（中間講者又複習了一次理想的定義和超級封閉——「紀念我在 Liberty 的同事 Sprano 博士」——以及主理想。）

**極大 ⇒ 質** [▶ 42:03](https://youtu.be/dcfaKtJTPUo?t=2523)：

【課堂討論】講者問：體裡有零因子嗎？沒有。所以

$$A\text{ 極大}\overset{\text{4.3.7}}{\Longrightarrow}R/A\text{ 是體}\Longrightarrow R/A\text{ 是整環}\overset{\text{4.3.6}}{\Longrightarrow}A\text{ 是質理想}.$$

**質 ⇏ 極大** [▶ 43:12](https://youtu.be/dcfaKtJTPUo?t=2592)（講義 Example 4.3.8）：在 $\mathbb{Z}[x]$ 裡，

- **$\langle x\rangle$ 是質理想**：若 $a(x)b(x)\in\langle x\rangle$，則 $a(x)b(x) = x\,f(x)$，$x$ 一定整除其中一個（「多項式的性質」），所以 $a(x)\in\langle x\rangle$ 或 $b(x)\in\langle x\rangle$。
- **$\langle x\rangle$ 不是極大理想** [▶ 44:47](https://youtu.be/dcfaKtJTPUo?t=2687)：
  $$\langle x\rangle\subsetneq\langle 2,x\rangle\subsetneq\mathbb{Z}[x].$$
  - $\langle 2,x\rangle = \{2f(x)+xg(x)\}$ 包含 $\langle x\rangle$（取 $f=0$）。
  - $2\in\langle 2,x\rangle$ 但 $2\notin\langle x\rangle$。
  - $1\notin\langle 2,x\rangle$：「不可能湊出常數多項式 1」（常數項一定是偶數，第 29 集）。

講者：「所以質理想不自動是極大的，雖然在我們的經驗裡常常是。」

> 【講義補充】講義在 Example 4.4.9（p. 139，下一集）用同構定理重新看這個例子：$\varphi:\mathbb{Z}[x]\to\mathbb{Z}$、$\varphi(f) = f(0)$ 是映成的環同態，核是 $\langle x\rangle$，所以 $\mathbb{Z}[x]/\langle x\rangle\cong\mathbb{Z}$。$\mathbb{Z}$ 是整環但不是體，所以 $\langle x\rangle$ 是質的、不是極大的——不用直接檢查。

---

## 6. 環同態

[▶ 46:52](https://youtu.be/dcfaKtJTPUo?t=2812)

講者：「這帶我們到 Lecture 24。」

> **定義**（講義 Definition 4.4.1）：從環 $R$ 到環 $S$ 的**環同態**（ring homomorphism）是函數 $\varphi:R\to S$，滿足
> 1. $\varphi(a+b) = \varphi(a)+\varphi(b)$
> 2. $\varphi(ab) = \varphi(a)\varphi(b)$
> 3. $\varphi(1_R) = 1_S$
>
> **雙射**的環同態叫**環同構**（ring isomorphism），寫 $R\cong S$。從 $R$ 到自己的同構叫**自同構**（automorphism）。

【課堂討論】講者問同態是什麼，學生：「保持結構的映射。」講者：「保持公理。」

---

## 7. 例子：自然映射、共軛、求值映射

**自然映射**（Ex 4.4.2）[▶ 50:06](https://youtu.be/dcfaKtJTPUo?t=3006)：
$$\varphi:\mathbb{Z}\to\mathbb{Z}_n,\qquad\varphi(x) = [x]_n = x+n\mathbb{Z}.$$

推廣：$R$ 到商環 $R/A$ 的 $\varphi(x) = x+A$ 叫**自然映射**（natural map）或**陪集映射**（coset map），是環同態，「很容易檢查」。

> 【講義補充】Example 4.4.2 的腳註（p. 137）：反方向 $g([x]_n) = x$「相當失能」（不是 well-defined 的函數：$[0]_n = [n]_n$ 會被送到 $0$ 和 $n$）。

**複數共軛**（Ex 4.4.3，講義 p. 137）[▶ 51:40](https://youtu.be/dcfaKtJTPUo?t=3100)：$\varphi(z) = z^* = \bar z$（講者說講義用星號，很多課用橫線）。

- $\overline{z+w} = \bar z+\bar w$、$\overline{zw} = \bar z\,\bar w$、$\bar 1 = 1$。「勾勾勾。」所以是環同態。
- $\varphi(\varphi(z)) = z$：共軛兩次回到原點，$\varphi\circ\varphi = \mathrm{id}$，**它是自己的反函數**，所以是雙射。
- 所以共軛是 $\mathbb{C}$ 的**自同構**，而且**階為 2**。講者：「我問過你們 $\mathbb{Z}_n$ 有幾個某階的自同構——還記得那段不愉快嗎？這算是回到那裡。」

**求值映射**（Ex 4.4.4）[▶ 53:41](https://youtu.be/dcfaKtJTPUo?t=3221)：講者說這個「很有力，會在某些抽象討論中一直陪著我們」。$R$ 是環、$a\in R$：
$$\varphi_a:R[x]\to R,\qquad\varphi_a(f(x)) = f(a),$$
也就是 $\varphi_a(c_0+c_1x+\cdots+c_nx^n) = c_0+c_1a+\cdots+c_na^n$——「把 $x$ 換成 $a$」。

- 這是**求值映射**（evaluation map），滿足 1、2、3，是環同態——「從 $R$ 上的多項式到 $R$ 本身的自然環同態」。
- 有幾個求值映射？「看你的環多大」，每個 $a$ 一個。

> 【講義補充】Example 4.4.4（p. 137）的驗證：$\varphi_a((f+g)(x)) = (f+g)(a) = f(a)+g(a)$，$\varphi_a((fg)(x)) = f(a)g(a)$。講義說這是 Gallian p. 271 Example 3 的深化版。
>
> 以下**不是逐字稿內容**，是補一句：$(fg)(a) = f(a)g(a)$ 需要 $R$ **可交換**（$x$ 跟係數交換，$a$ 也要跟係數交換）；不可交換環上求值映射一般不是同態。

---

## 8. 環同態的性質；核是理想（開頭）

[▶ 55:21](https://youtu.be/dcfaKtJTPUo?t=3321)

> **定理**（講義 Theorem 4.4.5）：$\varphi:R\to S$ 是環同態，$A$ 是 $R$ 的子 rng，$B$ 是 $S$ 的理想。
> 1. $\varphi(nr) = n\varphi(r)$、$\varphi(r^n) = \varphi(r)^n$（性質 1、2 的歸納延伸）
> 2. $\varphi(A)$ 是 $S$ 的子 rng
> 3. 若 $A$ 是理想且 $\varphi$ 映成，則 $\varphi(A)$ 是 $S$ 的理想
> 4. $\varphi^{-1}(B)$ 是 $R$ 的理想
> 5. 若 $R$ 可交換，則 $\varphi(R)$ 可交換
> 6. $\varphi$ 是同構 $\iff$ $\varphi$ 映成且 $\ker\varphi = \{0\}$
> 7. 若 $\varphi$ 是同構，$\varphi^{-1}$ 也是同構

講者說「請自己讀，我真的不想寫出來」，只講重點；「這些不難證，大概會在 Mission 6 出一兩題」。

> 【講義補充】講義的證明（p. 138）：「跟群的證明類似。主要差別是乘法性質不能用反元素，但仔細看我們對群的證明，稍加修改就能用。」講義也說：**加法的核**決定單射，因為 $(R,+)$ 是交換群，這正是群論的「核平凡 ⇔ 單射」。

**核是理想**（講義 Theorem 4.4.6）[▶ 57:25](https://youtu.be/dcfaKtJTPUo?t=3445)：講者說「來真的證一個」。

> **定義**：$\ker\varphi = \{\,r\in R : \varphi(r) = 0\,\}$，被送到 0 的元素，也就是 $0$ 的原像。

【Q&A】[▶ 58:34](https://youtu.be/dcfaKtJTPUo?t=3514) 學生問：你在想群嗎？講者：群裡是送到單位元素的東西；這裡講的是**加法的核**。加法群可交換、子群自動正規，「我們所有商環的構造都是對加法陪集做的」。乘法的「核」（1 的原像）也可以想，一定含 1，含不含別的看映射。

講者：「我們要證核是理想，該怎麼做？」（影片在這裡被切斷，接第 32 集。）

> 【講義補充】Theorem 4.4.6 的證明（p. 138）：$a,b\in\ker\varphi$，則 $\varphi(a-b) = 0-0 = 0$；對 $r\in R$，$\varphi(ra) = \varphi(r)\cdot 0 = 0$、$\varphi(ar) = 0\cdot\varphi(r) = 0$。由理想判別法，$\ker\varphi$ 是理想。

---

## 9. 一頁速查表

**直接證 $\langle x^2+1\rangle$ 在 $\mathbb{R}[x]$ 極大**：$B$ 比它大 ⇒ 有餘數 $ax+b\in B$ ⇒ $(ax+b)(ax-b)\in B$ ⇒ $a^2(x^2+1)-(a^2x^2-b^2) = a^2+b^2\in B$ ⇒ $1\in B$。

**$\langle x^2+1\rangle$ 在 $\mathbb{Z}_2[x]$ 不是質**：$(x+1)^2 = x^2+1$，但 $x+1\notin\langle x^2+1\rangle$。

**兩個大定理**（$R$ 有 1 的可交換環，$A$ 理想）

| | 關鍵一步 |
|---|---|
| $R/A$ 整環 ⇔ $A$ 質 | $(a+A)(b+A) = ab+A$，「乘積是零」⇔「$ab\in A$」 |
| $R/A$ 體 ⇔ $A$ 極大 | (⇒) $xy+A = 1+A$ ⇒ $1 = (1-xy)+xy\in B$；(⇐) $B = \{xr+a\}\supsetneq A$ ⇒ $B=R$ ⇒ $xr+a = 1$ |

- 極大 ⇒ 質（體是整環）。
- 質 ⇏ 極大：$\langle x\rangle\subsetneq\langle2,x\rangle\subsetneq\mathbb{Z}[x]$。

**環同態**：保持加法、乘法、$1$。雙射 = 同構；到自己的同構 = 自同構。

| 例子 | 說明 |
|---|---|
| $\mathbb{Z}\to\mathbb{Z}_n$，$x\mapsto[x]_n$；$R\to R/A$，$x\mapsto x+A$ | 自然映射 |
| $\mathbb{C}\to\mathbb{C}$，$z\mapsto\bar z$ | 階 2 的自同構 |
| $R[x]\to R$，$f\mapsto f(a)$ | 求值映射 |

**性質**：同構 ⇔ 映成且 $\ker\varphi = \{0\}$；理想的原像是理想；$\ker\varphi$ 是理想。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 核是理想（證明）、第一同構定理、每個理想都是核 | 第 32 集 |
| $\varphi(n) = n\cdot 1$、質子體（$\mathbb{Z}_p$ 或 $\mathbb{Q}$） | 第 32–34 集 |
| 分式體 | 第 33–34 集 |
| 求值映射、因式定理 | 第 35 集 |
| $F[x]/\langle p(x)\rangle$ 是體 ⇔ $p$ 不可約 | 第 36–37、40–43 集 |

---

## 附：本集一句話總結

> **$R/A$ 是整環恰好在 $A$ 是質理想時，$R/A$ 是體恰好在 $A$ 是極大理想時——所以極大理想一定是質的，反過來不一定（$\langle x\rangle$ 在 $\mathbb{Z}[x]$ 裡）。這讓「證明理想極大」變成「認出商環是體」，例如 $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$。最後開始講環同態：自然映射、複數共軛、求值映射。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-25 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.3–4.4 整理。*
