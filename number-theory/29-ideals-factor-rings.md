---
course: Number Theory（2021 秋，線上錄影）
episode: 29
lecture: 2021-10-20 第 1 部
date: 2021-10-20
video: https://youtu.be/J2_uWsESIcE
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.2 Lecture 22（p. 129–133）：Definition 4.2.1、Theorem 4.2.2、Example 4.2.3–4.2.4、Definition 4.2.5、Theorem 4.2.7、Example 4.2.8–4.2.9、Definition 4.2.10、Example 4.2.12–4.2.13、Theorem 4.2.14、Example 4.2.15–4.2.18；講義說本節跟 Gallian 第 14 章
---

# 第 29 集 · 理想、主理想、商環、例子（Ideals, Principal Ideals, Factor Ring, Examples） [▶ 影片](https://youtu.be/J2_uWsESIcE)

← 上一集：[28-rings-and-subrings-2](28-rings-and-subrings-2.md) ｜ [總目錄](README.md) ｜ 下一集：[30-prime-maximal-ideals-intro](30-prime-maximal-ideals-intro.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 29 集（2021-10-20 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；結尾被切斷）＋ 講者講義 §4.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 理想的定義：「超級封閉」](#1-理想的定義超級封閉)
- [2. 理想判別法與基本例子](#2-理想判別法與基本例子)
- [3. 主理想 ⟨a⟩](#3-主理想-a)
- [4. 多項式環裡的理想](#4-多項式環裡的理想)
- [5. 由好幾個元素生成的理想](#5-由好幾個元素生成的理想)
- [6. 子環但不是理想：可微函數](#6-子環但不是理想可微函數)
- [7. 商環 R/A](#7-商環-ra)
- [8. 例子：Z/3Z、矩陣、Z[i]/⟨2 − i⟩、R[x]/⟨x² + 1⟩](#8-例子z3z矩陣zi2--irxx--1)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:02](https://youtu.be/J2_uWsESIcE?t=2)

講者：「今天應該是一堂**理想的**（ideal）課——抱歉，很糟的雙關。我是說我們今天講理想。」什麼是理想？為什麼在乎？這是他「舊的 Lecture 22」。

**為什麼叫「理想」**（講義說的，課堂沒講）：

> 【講義補充】§4.2 開頭（p. 129）：你可能以為該叫「正規子環」，但這不是常用詞——「群論才是怪胎」。研究其他抽象代數系統時，能做自然商的子物件通常叫**理想**。這個名詞來自 19 世紀末的 **Kummer**：他引入「**理想數**」修補某些代數數的失敗（第 23 集）。後來 **Dedekind** 把 Kummer 有點模糊的工作整理清楚、嚴謹化。講義註腳說這是他讀 Stillwell 得知的。

| 主題 | 時間 | 講義 |
|---|---|---|
| 理想的定義 | 00:32 | Def 4.2.1 |
| 理想判別法 | 06:27 | Thm 4.2.2 |
| $n\mathbb{Z}$ | 09:35 | Ex 4.2.4 |
| 主理想 | 11:40 | Def 4.2.5、Thm 4.2.7 |
| 多項式的理想 | 16:47 | Ex 4.2.8–4.2.9 |
| 多元素生成 | 20:26 | Def 4.2.10、Ex 4.2.12 |
| 可微函數 | 24:41 | Ex 4.2.13 |
| 商環 | 28:29 | Thm 4.2.14 |
| 例子 | 46:23 | Ex 4.2.15–4.2.18 |

---

## 1. 理想的定義：「超級封閉」

[▶ 00:32](https://youtu.be/J2_uWsESIcE?t=32)

> **定義**（講義 Definition 4.2.1）：環 $R$ 的子 rng $A$，若對**每個** $r\in R$、$a\in A$，都有
> $$ar\in A\quad\text{且}\quad ra\in A,$$
> 就叫 $A$ 是 $R$ 的**理想**（ideal）。若 $A\neq R$，叫**真理想**（proper ideal）。

講者：「我說過不再講子 rng 了，抱歉，避不開。」

**「超級封閉」**（über-closure）[▶ 02:17](https://youtu.be/J2_uWsESIcE?t=137)：講者以前學校的同事這樣叫這個條件。圖像：$A$ 裡的東西乘上**整個 $R$ 的任何東西**，都還掉回 $A$，左邊右邊都要。

【口頭】「一開始有點不習慣，你可能以為兩邊都該在 $A$ 裡——有點不對稱。但這就是需要的。」

**為什麼用子 rng 而不是子環** [▶ 04:22](https://youtu.be/J2_uWsESIcE?t=262)：

- 子 rng：$a,b\in A$ ⇒ $ab,\ a\pm b\in A$。子環：再加上 $1\in A$。
- **如果 $1\in A$**：超級封閉給出 $r\cdot 1 = r\in A$ 對每個 $r\in R$，所以 **$A = R$**。

> **重點**：**真理想不能含單位元素**。含 1 的理想就是整個環。

（推論：真理想也不能含任何**單位** $u$，因為 $u^{-1}u = 1$ 也會在裡面。這一句**不是逐字稿內容**。）

【Q&A】[▶ 05:23](https://youtu.be/J2_uWsESIcE?t=323) 學生問：以前的課講過理想嗎？好像跟矩陣有關？講者：我想沒有在他的課講過。矩陣環確實可以有理想，但不是所有子集合都是，「我一時想不起來」。

> 【講義補充】Definition 4.2.1 後面（p. 129）：所以「rng 的概念其實比較自然：**正規子群的類比是理想子 rng**」。可交換環裡 $ar = ra$，只要檢查一邊。

---

## 2. 理想判別法與基本例子

> **理想判別法**（Theorem 4.2.2）[▶ 06:27](https://youtu.be/J2_uWsESIcE?t=387)：$R$ 的非空子集合 $A$，若
> 1. $a,b\in A$ ⇒ $a-b\in A$；
> 2. $a\in A$、$r\in R$ ⇒ $ar,\ ra\in A$（超級封閉），
>
> 則 $A$ 是 $R$ 的理想。

講者說證明「很明顯」：超級封閉自動給出**對乘法封閉**；加上減法封閉，由子 rng 判別法是子 rng；再加超級封閉就是理想。「這不是深刻的定理，只是檢查某個東西是不是理想的方法。」

**兩個「蠢」例子**（Ex 4.2.3）[▶ 08:33](https://youtu.be/J2_uWsESIcE?t=513)：對任何環 $R$，

- $A = \{0\}$：**平凡理想**（$0$ 乘任何東西是 $0$）。
- $A = R$：講者說「不真的（improper）理想」。

**$n\mathbb{Z}\subseteq\mathbb{Z}$ 是理想**（Ex 4.2.4）[▶ 09:35](https://youtu.be/J2_uWsESIcE?t=575)：

1. $a = nj$、$b = nk$ ⇒ $a-b = n(j-k)\in n\mathbb{Z}$。
2. $r\in\mathbb{Z}$ ⇒ $ra = r(nj) = n(rj)\in n\mathbb{Z}$（可交換，$ar$ 一樣）。

講者：「這裡我們**早就在談理想了**。」

---

## 3. 主理想 ⟨a⟩

[▶ 11:40](https://youtu.be/J2_uWsESIcE?t=700)

講者：「這個很重要，會陪我們到學期結束。」

> **定義**（Def 4.2.5）：$R$ 是有單位元素的可交換環，$a\in R$。$a$ 生成的**主理想**（principal ideal）
> $$\langle a\rangle = \{\,ar : r\in R\,\} = aR = Ra.$$

**例子**：$\langle n\rangle = n\mathbb{Z} = \mathbb{Z}n$。

> **定理**（Thm 4.2.7）[▶ 13:43](https://youtu.be/J2_uWsESIcE?t=823)：$\langle a\rangle$ 是理想。

講者：「你會說，你都叫它理想了，不就是理想嗎？光是取名字不能證明它是理想。」學生：「理想上（ideally）？」講者：「喔不。太可怕了。但我允許。」

**證明**：

1. $x = r_1a$、$y = r_2a$ ⇒ $x-y = (r_1-r_2)a\in\langle a\rangle$。
2. $r\in R$ ⇒ $rx = r(r_1a) = (rr_1)a\in\langle a\rangle$（$rr_1\in R$）。
3. $0 = 0\cdot a\in\langle a\rangle$，非空。∎

> 【講義補充】講義說這是線性代數「**span 是子空間**」定理的類比，是證明某些東西是理想的好方法。

---

## 4. 多項式環裡的理想

**$\langle x\rangle\subseteq\mathbb{R}[x]$**（Ex 4.2.8，講義 p. 130）[▶ 16:47](https://youtu.be/J2_uWsESIcE?t=1007)：
$$x\,(a_nx^n+\cdots+a_1x+a_0) = a_0x+a_1x^2+\cdots+a_nx^{n+1}.$$
所以 $\langle x\rangle$ = **常數項為 0** 的多項式。

**$\langle xy\rangle\subseteq\mathbb{R}[x,y]$**（Ex 4.2.9）[▶ 18:23](https://youtu.be/J2_uWsESIcE?t=1103)：$\mathbb{R}[x,y]$ 是**二元多項式**。$\langle xy\rangle$ 裡的東西都是 $xy\cdot g(x,y)$。

- $f = y+y^3+x^2y^2$ 在 $\mathbb{R}[x,y]$ 裡，但**不在** $\langle xy\rangle$ 裡（$y$、$y^3$ 不是 $xy$ 的倍數）。
- $x^2y^2 = xy\cdot xy$ **在** $\langle xy\rangle$ 裡。

【口頭】講者說他講義這裡有打字錯誤：寫成 $\langle x\rangle$，應該是 $\langle xy\rangle$。

> 【講義補充】講義 Example 4.2.9（p. 130）的文字前半段描述的確實是 $\langle x\rangle$（「常數項為零、沒有只含 $y$ 的項」），後半段才講 $\langle xy\rangle$——跟講者說的打字錯誤一致。

---

## 5. 由好幾個元素生成的理想

[▶ 20:26](https://youtu.be/J2_uWsESIcE?t=1226)

> **定義**（Def 4.2.10）：$R$ 有單位元素的可交換環，$a_1,\dots,a_n\in R$。
> $$\langle a_1,a_2,\dots,a_n\rangle = \{\,a_1r_1+a_2r_2+\cdots+a_nr_n : r_i\in R\,\}.$$

講者 [▶ 22:02](https://youtu.be/J2_uWsESIcE?t=1322)：**一個有好幾個生成元的理想，能不能改寫成主理想**？「這是個有趣、有時不簡單的問題。也許能，也許不能。」（第 36–39 集的 PID 就在問這個。）

**跟線性代數 span 的差別** [▶ 22:33](https://youtu.be/J2_uWsESIcE?t=1353)：講者想用 $\mathbb{R}\times\mathbb{R}$ 舉例，說「不太對」，然後講出差別：

- span $\{c_1v_1+\cdots+c_nv_n\}$：**純量** $c_i$ 來自體，**向量** $v_i$ 來自向量空間——兩種不同的東西。
- $\langle a_1,\dots,a_n\rangle$：$a_i$ 和 $r_i$ **都來自同一個環 $R$**，「在同一個結構層級」。

「有相似，也有不同。」

**例子：$\langle x,2\rangle\subseteq\mathbb{Z}[x]$**（Ex 4.2.12）[▶ 27:56](https://youtu.be/J2_uWsESIcE?t=1676)：元素是 $x\,h(x)+2\,j(x)$。看常數項：$xh(x)$ 沒有常數項，$2j(x)$ 的常數項是偶數。所以 $\langle x,2\rangle$ = **常數項是偶數**的整係數多項式。「之後就什麼都有可能，但常數項一定是偶數。」

> 【講義補充】Example 4.2.12（p. 130）的計算：$h = h_0+h_1x+\cdots$、$j = j_0+j_1x+\cdots$，
> $$xh(x)+2j(x) = 2j_0+(h_0+2j_1)x+\cdots.$$
>
> 以下**不是逐字稿內容**：$\langle x,2\rangle$ 是**不能寫成主理想**的經典例子。若 $\langle x,2\rangle = \langle f\rangle$，則 $f\mid 2$ 所以 $f$ 是常數 $\pm1$ 或 $\pm2$；$\pm1$ 會讓理想變成整個 $\mathbb{Z}[x]$（但 $1$ 的常數項是奇數，不在裡面），$\pm2$ 又不整除 $x$。所以 $\mathbb{Z}[x]$ 不是 PID（第 36–39 集）。

---

## 6. 子環但不是理想：可微函數

[▶ 24:41](https://youtu.be/J2_uWsESIcE?t=1481)（Ex 4.2.13）

$R = F(\mathbb{R},\mathbb{R})$（所有實函數，逐點加乘，第 27 集）。$A = C^1(\mathbb{R})$ = 可微函數。

- **子環**：$(f-g)' = f'-g'$ 存在、$(fg)' = f'g+fg'$ 存在，常數 1 可微。
- **不是理想**：$f = 1$（可微）乘上 $h(x) = |x|$（在 $R$ 裡，但不可微），$hf = |x|$ 在 0 不可微，不在 $A$ 裡。**超級封閉失敗**。

---

## 7. 商環 R/A

[▶ 28:29](https://youtu.be/J2_uWsESIcE?t=1709)

講者：「今天證明的重頭戲——我不讓它拖太久。」

> **定理**（Theorem 4.2.14）：$R$ 是環，$A$ 是子 rng。陪集的集合
> $$R/A = \{\,r+A : r\in R\,\}$$
> 配上
> $$(s+A)+(t+A) = (s+t)+A,\qquad (s+A)(t+A) = st+A$$
> 成為一個環 **$\iff$ $A$ 是理想**。這時 $R/A$ 叫 $R$ 對 $A$ 的**商環**（factor ring）。

**Step 0：加法早就沒問題** [▶ 33:25](https://youtu.be/J2_uWsESIcE?t=2005)

講者說他忘了在證明開頭講：$A$ 是子 rng，所以是 $(R,+)$ 的**加法子群**。$(R,+)$ 可交換，所以 $A$ 自動是**正規子群**（左右陪集相等）。

【課堂討論】講者問抽象代數有沒有教商群和正規子群？學生：有，正規子群就是「在共軛下封閉」。講者：另一個看法是左右陪集相等；加法可交換，所以自動成立。

所以 $R/A$ 在加法下已經是**商群**，加法 well-defined，而且 $s_1+A = s_2+A\iff s_2-s_1\in A$（群論早證過，講者說會出作業讓大家複習）。

（講者還是把加法 well-defined 驗了一遍 [▶ 36:32](https://youtu.be/J2_uWsESIcE?t=2192)：$s_2 = s_1+a_1$、$t_2 = t_1+a_2$，$(s_2+t_2)+A = (s_1+t_1)+(a_1+a_2)+A = (s_1+t_1)+A$，「$A$ 的元素被吸進 $A$」。「其實不用證，這是商群的結果。」）

**Step 1：乘法 well-defined——這裡需要超級封閉** [▶ 39:08](https://youtu.be/J2_uWsESIcE?t=2348)

設 $s_2 = s_1+a_1$、$t_2 = t_1+a_2$（$a_1,a_2\in A$）。

$$s_2t_2 = (s_1+a_1)(t_1+a_2) = s_1t_1 + a_1t_1 + s_1a_2 + a_1a_2.$$

- $a_1t_1\in A$、$s_1a_2\in A$：**超級封閉**（$A$ 的元素乘 $R$ 的元素）。
- $a_1a_2\in A$：子 rng。

所以 $s_2t_2+A = s_1t_1+A$。乘法跟代表元無關。

（講者：「S2T2 聽起來像《星際大戰》裡落選的機器人。」）

**Step 2：還要驗環的公理** [▶ 41:45](https://youtu.be/J2_uWsESIcE?t=2505)

到目前只說明 $R/A$ 是「有兩個運算的集合」。講者只講一個：

- **單位元素是 $1+A$**：$(1+A)(r+A) = 1r+A = r+A$。
- **零是 $0+A = A$** [▶ 47:59](https://youtu.be/J2_uWsESIcE?t=2879)（講者後來補的）。

其他（加法交換、乘法結合、分配律）「很直接」，看講義；講者說講義漏了一條分配律，「大概會出成作業」。

**Step 3：反方向——不是理想就壞掉** [▶ 43:55](https://youtu.be/J2_uWsESIcE?t=2635)

若 $A$ 不是理想，存在 $a\in A$、$r\in R$ 使 $ar\notin A$（或 $ra\notin A$）。那 Step 1 裡的 $a_1t_1$ 或 $s_1a_2$ 就丟不掉，**乘法不 well-defined**，不會得到商環。「**超級封閉是乘法 well-defined 的關鍵**。」

> 【講義補充】Theorem 4.2.14 反方向的具體版本（p. 131）：取 $a\in A$、$r\in R$ 使 $ar\notin A$。則 $a+A = 0+A$（同一個陪集），但
> $$(a+A)(r+A) = ar+A\neq A = 0r+A = (0+A)(r+A).$$
> 同一個陪集乘同一個陪集，得到兩個不同答案。講義也寫出結合律和一條分配律的驗證，「關鍵一步是用 $R$ 對應的分配律」。

**直覺** [▶ 47:59](https://youtu.be/J2_uWsESIcE?t=2879)：講者說商環的好直覺是「**把理想裡的所有東西重新定義成零**」，「把理想裡的一切壓扁成零」。

---

## 8. 例子：Z/3Z、矩陣、Z[i]/⟨2 − i⟩、R[x]/⟨x² + 1⟩

**$\mathbb{Z}/3\mathbb{Z}$**（Ex 4.2.15）[▶ 46:23](https://youtu.be/J2_uWsESIcE?t=2783)：陪集 $3\mathbb{Z},\ 1+3\mathbb{Z},\ 2+3\mathbb{Z}$。

【課堂討論】一起算乘法表：$3\mathbb{Z}$ 是零，乘什麼都是 $3\mathbb{Z}$；$1\cdot1 = 1$、$1\cdot2 = 2$、$2\cdot 2 = 4+3\mathbb{Z} = 1+3\mathbb{Z}$。

| $\times$ | $3\mathbb{Z}$ | $1+3\mathbb{Z}$ | $2+3\mathbb{Z}$ |
|---|---|---|---|
| $3\mathbb{Z}$ | $3\mathbb{Z}$ | $3\mathbb{Z}$ | $3\mathbb{Z}$ |
| $1+3\mathbb{Z}$ | $3\mathbb{Z}$ | $1+3\mathbb{Z}$ | $2+3\mathbb{Z}$ |
| $2+3\mathbb{Z}$ | $3\mathbb{Z}$ | $2+3\mathbb{Z}$ | $1+3\mathbb{Z}$ |

學生：「跟 $\mathbb{Z}_3$ 的表一樣。」講者 [▶ 49:34](https://youtu.be/J2_uWsESIcE?t=2974)：**$\mathbb{Z}_3$ 和 $\mathbb{Z}/3\mathbb{Z}$ 是同一隻動物的兩種記號**（同構）。一般地，**$\mathbb{Z}_n$ 就是商環 $\mathbb{Z}/n\mathbb{Z}$**。「以前沒這樣說，因為不知道商環是什麼。」

**矩陣**（Ex 4.2.16）[▶ 50:04](https://youtu.be/J2_uWsESIcE?t=3004)（回應學生想要的矩陣例子）：$R = \mathbb{Z}^{2\times2}$，$A$ = 元素全是偶數的 2×2 矩陣。$A$ 是理想。$R/A$ 是一個有 **16 個元素**的矩陣環。

> 【講義補充】Example 4.2.16（p. 132）：$X = 2X'$、$Y = 2Y'$ ⇒ $X-Y = 2(X'-Y')\in A$、$XZ = 2X'Z\in A$。陪集代表元可以取每個元素是 0 或 1 的矩陣：4 個位置各 2 種，$2^4 = 16$ 個不同陪集（Gallian 也這樣說）。

**$\mathbb{Z}[i]/\langle 2-i\rangle$**（Ex 4.2.17）[▶ 51:37](https://youtu.be/J2_uWsESIcE?t=3097)：講者說這個「更有意思，帶我們回到高斯整數」。

**關鍵**：$2-i\in\langle2-i\rangle$，所以
$$2+\langle 2-i\rangle = i+\langle 2-i\rangle.$$
在這個商環裡「**$i = 2$**」。（Conrad 會說「模理想 $\langle 2-i\rangle$」——就是我們跳過的那節。）所以 $a+bi$ 跟 $a+2b$ 是同一個陪集。

講者說「我希望能給你們更清楚的演算法」，然後列出陪集 [▶ 54:17](https://youtu.be/J2_uWsESIcE?t=3257)：
$$\langle 2-i\rangle,\quad 1+\langle 2-i\rangle,\quad 2+\langle 2-i\rangle,\quad 1+i+\langle 2-i\rangle = 3+\langle2-i\rangle,\quad 2+i+\langle 2-i\rangle.$$
講義用藍、綠、紅、黃、粉紅五種顏色畫在格子圖上（講義是黑白的，「一點幫助都沒有」）。

**幾何看法** [▶ 55:20](https://youtu.be/J2_uWsESIcE?t=3320)：在高斯平面上，$2-i$ 和 $i(2-i) = 1+2i$ 張出一個正方形（「基本區域」）。正方形裡的點 $0,1,2,1+i,2+i$ 就是代表元；其他點都能加上 $2-i$、$1+2i$ 的整數倍移進這個正方形。講者說他沒證，「但這是在發生什麼的草稿」。

> 【講義補充】Example 4.2.17（p. 132–133）：結論是 $\mathbb{Z}[i]/\langle 2-i\rangle = \{[0],[1],[2],[3],[4]\}$，其中 $[x] = x+\langle2-i\rangle$；$2+i+\langle 2-i\rangle = -1+\langle2-i\rangle$（就是 $[4]$）。講義說：「我對這個商的理解跟 Gallian 很不一樣」，大部分商環畫不出圖，但子環在 $\mathbb{C}$ 裡時可以直接看。
>
> 以下**不是逐字稿內容**，是補一個解釋：$N(2-i) = 5$，基本正方形面積是 5，所以恰有 5 個陪集。在商環裡 $i = 2$，$i^2 = -1$ 變成 $4 = -1$，也就是 $5 = 0$。所以 $\mathbb{Z}[i]/\langle2-i\rangle\cong\mathbb{Z}_5$——這跟第 18–20 集「$5 = (2+i)(2-i)$ 在 $\mathbb{Z}[i]$ 分裂」是同一件事。

**$\mathbb{R}[x]/\langle x^2+1\rangle$**（Ex 4.2.18）[▶ 58:39](https://youtu.be/J2_uWsESIcE?t=3519)：講者說「更有意思」。$x^2+1\in\langle x^2+1\rangle$，所以
$$x^2+\langle x^2+1\rangle = -1+\langle x^2+1\rangle.$$
可以把 $x^2$ 換成 $-1$。（影片在這裡被切斷，接第 30 集。）

> 【講義補充】Example 4.2.18 的後半（p. 133）：用多項式除法 $f(x) = q(x)(x^2+1)+r(x)$，$r(x) = ax+b$，所以每個陪集都有代表元 $a+bx$：
> $$\mathbb{R}[x]/\langle x^2+1\rangle = \{\,a+bx+\langle x^2+1\rangle : a,b\in\mathbb{R}\,\}.$$
> 乘法 $[a+bx][c+dx] = [(ac-bd)+(ad+bc)x]$——跟 $(a+bi)(c+di)$ 一模一樣，「$x$ 扮演 $i$」。例：$[1+2x+x^4+x^2] = [1+2x]$。講義說這是構造複數的許多方法之一，**Cauchy 在 1847 年**給的。

---

## 9. 一頁速查表

**理想** $A\subseteq R$：子 rng，加上**超級封閉** $ar, ra\in A$（$a\in A$、$r\in R$）。

- 判別：非空；$a-b\in A$；$ar,ra\in A$。
- **含 1 ⇒ $A=R$**（真理想不含單位）。
- 例：$\{0\}$、$R$、$n\mathbb{Z}\subseteq\mathbb{Z}$。

**主理想** $\langle a\rangle = aR$；**多元素** $\langle a_1,\dots,a_n\rangle = \{\sum a_ir_i\}$。

| 理想 | 描述 |
|---|---|
| $\langle n\rangle\subseteq\mathbb{Z}$ | $n\mathbb{Z}$ |
| $\langle x\rangle\subseteq\mathbb{R}[x]$ | 常數項為 0 |
| $\langle xy\rangle\subseteq\mathbb{R}[x,y]$ | $xy\cdot g$ |
| $\langle x,2\rangle\subseteq\mathbb{Z}[x]$ | 常數項是偶數（不是主理想） |

**子環 ≠ 理想**：可微函數 $\subseteq F(\mathbb{R},\mathbb{R})$（$1\cdot|x|$ 不可微）。

**商環** $R/A$（$A$ 是理想 ⇔ 是環）：$(s+A)(t+A) = st+A$；零 $= A$，單位 $= 1+A$。

- **關鍵一步**：$(s_1+a_1)(t_1+a_2) = s_1t_1+\underbrace{a_1t_1+s_1a_2+a_1a_2}_{\in A\text{（超級封閉）}}$。
- 直覺：把理想裡的東西壓成 0。

**例子**

| 商環 | 結構 |
|---|---|
| $\mathbb{Z}/n\mathbb{Z}$ | $=\mathbb{Z}_n$ |
| $\mathbb{Z}^{2\times2}/2\mathbb{Z}^{2\times2}$ | 16 個元素 |
| $\mathbb{Z}[i]/\langle2-i\rangle$ | 5 個元素 $\{0,1,2,3,4\}$（$i=2$） |
| $\mathbb{R}[x]/\langle x^2+1\rangle$ | $\{a+bx\}$，$x^2=-1$，就是 $\mathbb{C}$ |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\mathbb{R}[x]/\langle x^2+1\rangle$ 的後半 | 第 30 集 |
| 質理想、極大理想；$R/A$ 是整環／體的條件 | 第 30–32 集 |
| 環同態、第一同構定理（$\mathbb{Z}[i]/\langle2-i\rangle\cong\mathbb{Z}_5$ 的嚴格版） | 第 31–32 集 |
| PID：每個理想都是主理想嗎？ | 第 36–39 集 |
| $F[x]/\langle p(x)\rangle$ 造出擴張體 | 第 40–45 集 |
| 「理想修補了數」（Kummer、Dedekind） | 第 46–47 集 |

---

## 附：本集一句話總結

> **理想是對「乘上環裡任何元素」也封閉的子 rng（超級封閉），所以真理想不能含 1。正因為超級封閉，陪集的乘法 $(s+A)(t+A)=st+A$ 才 well-defined，$R/A$ 成為商環——把理想壓成零。$\mathbb{Z}_n$ 就是 $\mathbb{Z}/n\mathbb{Z}$；$\mathbb{Z}[i]/\langle2-i\rangle$ 有 5 個元素；$\mathbb{R}[x]/\langle x^2+1\rangle$ 就是複數。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-20 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.2 整理。*
