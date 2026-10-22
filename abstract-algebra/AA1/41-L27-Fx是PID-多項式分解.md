---
course: Abstract Algebra I (Fall 2016)
episode: 41
lecture: L27
date: 2016-11-09
video: https://www.youtube.com/watch?v=uo8ogufaSKA
notes: AlgebraInotes_2018.pdf §4.5–4.6（p.143–154）
---

# 第 41 集 · L27：F[x] 是 PID、多項式的分解（一） [▶ 影片](https://www.youtube.com/watch?v=uo8ogufaSKA&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[40-L26-多項式]] ｜ [總目錄](../README.md) ｜ 下一集：[[42-答疑課-上]] →

> **課程**：Abstract Algebra I（Liberty University，Fall 2016）— 第 41 集，Lecture 27
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（50:34，自動字幕）＋ 講義 `AlgebraInotes_2018.pdf` §4.5 尾（PID）與 §4.6「Lecture 26: factorization of polynomials」（p.147–154）＋ Gallian 第 16 章尾、第 17 章。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：這堂老師沒用投影機，全寫黑板（「今天我好像沒什麼要證的」）。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. PID 與 F[x] 是 PID](#1-pid-與-fx-是-pid)
- [2. ℤ 的理想都是 nℤ](#2-ℤ-的理想都是-nℤ)
- [3. ℝ[x]/⟨x²+1⟩ ≅ ℂ 的完整證明](#3-ℝxx1--ℂ-的完整證明)
- [4. 可約與不可約——永遠要說「在哪裡」](#4-可約與不可約永遠要說在哪裡)
- [5. 2、3 次：可約 ⟺ 有根](#5-23-次可約--有根)
- [6. 容量、本原、首一](#6-容量本原首一)
- [7. 在 ℚ 上可約 ⇒ 在 ℤ 上可約](#7-在-ℚ-上可約--在-ℤ-上可約)
- [8. 模 p 不可約判別法](#8-模-p-不可約判別法)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/uo8ogufaSKA?t=0) 課前禱告。大選後第二天：「我們在哪？……**看來美國還在**。耶。」（掌聲。）

「Lecture 27 主要是**多項式的分解**——你們已經知道一點，今天會多加一些。在那之前，上一講還剩一點。」

---

## 1. PID 與 F[x] 是 PID

> **定義（主理想整環 principal ideal domain, PID）**（講義 Def 4.5.16）[▶ 01:00](https://youtu.be/uo8ogufaSKA?t=60)　整環 $R$，其中**每個理想都是主理想**：$I$ 是理想 ⇒ $I = \langle a\rangle = \{ra : r\in R\}$，某個 $a\in R$。

【課堂討論】「整環是什麼？」——「有單位元的交換環，**沒有零因子**。」

> **定理**（講義 Thm 4.5.17）[▶ 02:30](https://youtu.be/uo8ogufaSKA?t=150)　$F$ 是體 ⇒ $F[x]$ 是 PID。

**證明**
- $F[x]$ 是整環：上次證過。剩下：每個理想都是主理想。
- 設 $I$ 是理想。**$I = \{0\}$**：$= \langle0\rangle$，主理想 [▶ 04:00](https://youtu.be/uo8ogufaSKA?t=240)。
- **$I\neq\{0\}$**：令 $S = \{\deg f : f\in I,\ f\neq0\}$。
  - 要 $f\neq0$，「因為零多項式的次數沒定義」。次數是 $0,1,2,\dots$。
  - 【課堂討論】由**良序原理**，$S$ 有最小元，設為 $\deg g$ [▶ 05:00](https://youtu.be/uo8ogufaSKA?t=300)。
- **論證 $I = \langle g\rangle$**[▶ 06:00](https://youtu.be/uo8ogufaSKA?t=360)：
  - 取 $f\in I$。**除法算則**：$f = qg+r$，$r = 0$ 或 $\deg r<\deg g$。
  - $r = f-qg$ [▶ 07:00](https://youtu.be/uo8ogufaSKA?t=420)：$f\in I$；$g\in I$ ⇒ $qg\in I$（超級封閉）；差在 $I$（子環）。所以 $r\in I$。
  - 【課堂討論】「$r$ 能非零嗎？」——不能：$g$ 次數最小，$r\neq0$ 會矛盾。所以 $r = 0$，$f = qg\in\langle g\rangle$ [▶ 08:30](https://youtu.be/uo8ogufaSKA?t=510)。⇒ $I\subseteq\langle g\rangle$。
  - 反向 [▶ 09:30](https://youtu.be/uo8ogufaSKA?t=570)：「有點蠢」——$\langle g\rangle$ 是 $g$ 的倍數，$g\in I$，理想對乘法封閉 ⇒ $\langle g\rangle\subseteq I$。
  - 雙向包含 ⇒ $I = \langle g\rangle$。$\blacksquare$

> **定理**（講義 Thm 4.5.18）[▶ 10:30](https://youtu.be/uo8ogufaSKA?t=630)　$F$ 是體，$I\neq\{0\}$ 是 $F[x]$ 的理想，$g\in F[x]$。則 $I = \langle g\rangle$ $\iff$ $g$ 是 $I$ 中**次數最小**的非零多項式。

【口頭】[▶ 12:00](https://youtu.be/uo8ogufaSKA?t=720)「要找多項式環（**係數在體上**很重要）裡理想的生成元，**找次數最小的元素**就好。」（「這是 Gallian 的措辭，讓我有點困惑。」）

---

## 2. ℤ 的理想都是 nℤ

【課堂討論】[▶ 12:30](https://youtu.be/uo8ogufaSKA?t=750)「$\mathbb{Z}$ 的理想有哪些？」
- 學生：「質數？」老師：「$2\mathbb{Z}$ 是理想，2 是質數，好。$3\mathbb{Z}$ 也是。但 4 也行，一直下去——$n\mathbb{Z}$。問題是：**還有別的嗎？**」
- 答案：**沒有**。證明幾乎一樣：用良序原理取理想中最小的正元素，同樣的論證說明它生成整個理想。

【口頭】[▶ 13:30](https://youtu.be/uo8ogufaSKA?t=810)「我昨天問 **Smith 教授**：我跟你們做了形式多項式的構造，但總覺得『重點是什麼？』他說：它基本上給你一個**形式上等價於整數**的物件。想想我剛說的就開始有道理了：**能對多項式給的論證，大概也有對應的整數論證**。多項式的除法算則和整數的除法算則，證明非常像。整數和多項式之間的這種相互作用，我們之後會一直看到。」

---

## 3. ℝ[x]/⟨x²+1⟩ ≅ ℂ 的完整證明

[▶ 14:30](https://youtu.be/uo8ogufaSKA?t=870)（講義 Ex 4.5.19）

$\varphi:\mathbb{R}[x]\to\mathbb{C}$，$\varphi(f) = f(i)$。「我就宣稱 $\varphi$ 是環同態，不證。」

1. **核是理想**[▶ 15:30](https://youtu.be/uo8ogufaSKA?t=930)，在係數為體的多項式環裡 ⇒ $\ker\varphi = \langle g\rangle$，$g$ 是核中次數最小的。
2. **$g$ 不能是一次**[▶ 16:00](https://youtu.be/uo8ogufaSKA?t=960)：若 $mx+b\in\ker\varphi$，則 $mi+b = 0$，$b = -mi$——**實數等於純虛數**，荒謬（除非 $m = b = 0$）。
3. 所以生成元至少二次。$\varphi(x^2+1) = i^2+1 = 0$ ⇒ $x^2+1\in\ker\varphi$，而且是**次數最小**的 ⇒
$$\ker\varphi = \langle x^2+1\rangle.$$
4. **滿射**[▶ 19:00](https://youtu.be/uo8ogufaSKA?t=1140)：【課堂討論】「$a+bi$ 是誰的像？」學生：「$a+bx$。」「很好。」
5. **第一同構定理**：
$$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}.$$

【口頭】[▶ 19:30](https://youtu.be/uo8ogufaSKA?t=1170)「我們之前說它**看起來像**。這次是**完整的證明**。」學生：「你沒證 $\varphi$ 是環同態。」老師：「……說得對。除了那個細節之外完整。」（「完整，只是不完整。」全班笑。）

【口頭】[▶ 18:00](https://youtu.be/uo8ogufaSKA?t=1080)「有些作業題（Gallian 那些極大、主理想之類的）你們現在**還沒有這套技術**，所以有點難。但隨著理論發展，回頭看就會變簡單。這比較是給**下次考試**的讀書建議。」

---

## 4. 可約與不可約——永遠要說「在哪裡」

> **定義**（講義 Def 4.6.1）[▶ 20:30](https://youtu.be/uo8ogufaSKA?t=1230)　$D$ 是整環。非零、非單位的 $f\in D[x]$ **在 $D$ 上不可約（irreducible over $D$）**，若
> $$f = gh\ ⇒\ g\text{ 或 }h\text{ 是 }D[x]\text{ 的單位}.$$
> 非零、非單位、而且**不是**不可約的，叫**可約（reducible）**。

【口頭】[▶ 22:00](https://youtu.be/uo8ogufaSKA?t=1320)「這是這一章**最糟的句子**：『不是不可約的多項式是可約的』。」「我犯了這一章的**大罪**——遺漏之罪，而且很不幸，這對接下來至關重要：要說『**在 $D$ 上**』不可約。**脈絡非常重要。**」

【Q&A】[▶ 23:00](https://youtu.be/uo8ogufaSKA?t=1380) 學生問質數和不可約的關係。老師：「那很有趣，之後會講。**有時一樣，有時不一樣**，但在很多熟悉的情況下一樣。如果你的直覺『蜘蛛感應』在刺痛，也許該聽它。」

**例**（講義 Ex 4.6.2–4.6.5）

| 多項式 | 不可約 | 可約 | 原因 |
|---|---|---|---|
| $x^2+1$ [▶ 24:00](https://youtu.be/uo8ogufaSKA?t=1440) | $\mathbb{R}$、$\mathbb{Q}$ | $\mathbb{C}$、$\mathbb{Q}(i)$ | $(x+i)(x-i)$，需要 $i$ |
| $2x+4$ [▶ 25:00](https://youtu.be/uo8ogufaSKA?t=1500) | $\mathbb{Q}$ | $\mathbb{Z}$ | $2(x+2)$；2 在 $\mathbb{Z}$ 不是單位，在 $\mathbb{Q}$ 是 |
| $x^2-7$ [▶ 26:30](https://youtu.be/uo8ogufaSKA?t=1590) | $\mathbb{Q}$ | $\mathbb{R}$ | $(x+\sqrt7)(x-\sqrt7)$ |
| $x^2+1$ [▶ 28:30](https://youtu.be/uo8ogufaSKA?t=1710) | $\mathbb{Z}_3$ | $\mathbb{Z}_5$ | 見下 |

- 【口頭】「$2x+4$：$2(x+2)$ 在 $\mathbb{Q}$ 上不是**有趣的**分解，在 $\mathbb{Z}$ 上是。所以『你的環的**單位**是什麼』很重要。」
- **$\mathbb{R}[x]$ 的單位**[▶ 27:30](https://youtu.be/uo8ogufaSKA?t=1650)：就是非零常數。「沒辦法拿一個非常數多項式乘另一個多項式得到 1。」【Q&A】學生問 $x+2$ 為什麼不是單位：「沒有 $f$ 使 $(x+2)f(x) = 1$。單位就是有乘法反元素的。」
- **$x^2+1$ 在 $\mathbb{Z}_3$**[▶ 29:00](https://youtu.be/uo8ogufaSKA?t=1740)：【課堂討論】$f(0) = 1$、$f(1) = 2$、$f(2) = 5 = 2$。**沒有根** ⇒ 沒有一次因式（上次的因式定理）⇒ 不可約。
- **$x^2+1$ 在 $\mathbb{Z}_5$**[▶ 30:30](https://youtu.be/uo8ogufaSKA?t=1830)：$f(2) = 5 = 0$。或者用大多數人的做法：$1 = -4$，所以 $x^2+1 = x^2-4 = (x-2)(x+2) = (x-2)(x-3)$。可約。
- 【口頭】[▶ 32:00](https://youtu.be/uo8ogufaSKA?t=1920)「但你該抱怨：可約——**在哪裡**？在 $\mathbb{Z}_5$。可約和不可約**永遠、永遠、永遠**附著在你考慮的係數環上。」

---

## 5. 2、3 次：可約 ⟺ 有根

> **定理**（講義 Thm 4.6.6）[▶ 32:30](https://youtu.be/uo8ogufaSKA?t=1950)　$F$ 是體，$f\in F[x]$ 次數 2 或 3。則 $f$ 在 $F$ 上可約 $\iff$ $f$ 在 $F$ 中有根。

（老師寫的時候又差點漏掉「在 $F$ 上」：「我又來了。」）

**證明**[▶ 34:00](https://youtu.be/uo8ogufaSKA?t=2040)（「很好懂」）
- (⇒) 2 或 3 次的分解**一定有一次因式**；一次因式對應根。
- (⇐) 有根 $c$ ⇒ $f = (x-c)g$ ⇒ 可約。

「這把因式定理再往前推一點。**但推不了多遠——4 次就失效**。」

**警世故事**（講義 Ex 4.6.7）[▶ 35:00](https://youtu.be/uo8ogufaSKA?t=2100)
$$f(x) = x^4+14x^2+49 = (x^2+7)^2.$$
- 兩個非單位、次數較小的多項式相乘 ⇒ **可約**（在 $\mathbb{Q}$、$\mathbb{R}$ 上）。
- 但在 $\mathbb{R}$ 中**沒有根**（$x^2+7>0$）。（老師先說「在 $\mathbb{C}$ 上也……喔等等，刪掉」。）

---

## 6. 容量、本原、首一

[▶ 37:00](https://youtu.be/uo8ogufaSKA?t=2220)「Gallian 接下來的結果是整數和模 $p$ 整數之間的相互作用。**容量**的概念是證明的核心。」

> **定義**（講義 Def 4.6.8）　$f = a_nx^n+\cdots+a_1x+a_0\in\mathbb{Z}[x]$ 非零。
> - **容量（content）**：$\gcd(a_n,\dots,a_0)$。
> - **本原（primitive）**：容量為 1。
> - **首一（monic）**[▶ 39:30](https://youtu.be/uo8ogufaSKA?t=2370)：領導係數是 1。首一 ⇒ 本原。

**例**[▶ 38:30](https://youtu.be/uo8ogufaSKA?t=2310)：$2x^2+4x+8 = 2(x^2+2x+4)$，$\gcd(2,4,8) = 2$。容量 2；**提出容量後剩下的就是本原的**。「這剛好也是首一的。」

> **定理**（講義 Thm 4.6.10）[▶ 40:30](https://youtu.be/uo8ogufaSKA?t=2430)　**本原 × 本原 = 本原。**

「我說過今天沒什麼要證的，就延續這主題。」證明的想法「很漂亮」：
- 環同態可以**作用在係數上**，延伸成多項式環之間的同態：
$$\mathbb{Z}[x]\to\mathbb{Z}_p[x],\quad f\mapsto\bar f\ (\text{係數取模 }p).$$
- Gallian 用**上槓**表示。講義多打了一些，下次再談。

> 📘 講義的證明：若 $fg$ 不是本原，取質數 $p$ 整除它的容量，則 $\bar f\,\bar g = \overline{fg} = 0$ 在 $\mathbb{Z}_p[x]$。$\mathbb{Z}_p[x]$ 是整環 ⇒ $\bar f = 0$ 或 $\bar g = 0$ ⇒ $p$ 整除 $f$ 或 $g$ 的所有係數，與本原矛盾。

---

## 7. 在 ℚ 上可約 ⇒ 在 ℤ 上可約

> **定理（Gauss 引理的一種形式）**（講義 Thm 4.6.11）[▶ 42:00](https://youtu.be/uo8ogufaSKA?t=2520)　$f\in\mathbb{Z}[x]$。若 $f$ 在 $\mathbb{Q}$ 上可約，則在 $\mathbb{Z}$ 上可約。

**例**（講義 Ex 4.6.12）[▶ 43:00](https://youtu.be/uo8ogufaSKA?t=2580)「我給例子不給證明。」
$$6x^2+19x-7 = 6\left(x^2+\tfrac{19}6x-\tfrac76\right) = 6\left(x+\tfrac72\right)\left(x-\tfrac13\right)$$
在 $\mathbb{Q}$ 上分解。把 $6 = 2\cdot3$ 分配進去：
$$= (2x+7)(3x-1),$$
在 $\mathbb{Z}$ 上也可約。
- 「如果研究證明，基本上就是**剝掉每個因式的容量，再重新組合**——跟這例子做的一模一樣。那個證明我不知為何花了一小時打字。你們會讀它，讓我對人生感覺好一點。」（「其實我現在對人生感覺蠻好的，不知為何。」）

【口頭】[▶ 45:00](https://youtu.be/uo8ogufaSKA?t=2700)「老實說，我**還沒完全被這個定理說服**。我個人寧願直接在 $\mathbb{Z}$ 裡分解——幹嘛把分數扯進來？但它被用在別的定理裡，所以有它的用處。」

【Q&A】[▶ 45:30](https://youtu.be/uo8ogufaSKA?t=2730) 學生問反方向。老師：「脈絡重要：這裡從 $\mathbb{Z}$ 的多項式出發。確實有在 $\mathbb{Z}$ 上可約、在 $\mathbb{Q}$ 上不可約的——我的第二個例子 $2x+4$。」

---

## 8. 模 p 不可約判別法

> **定理（模 $p$ 不可約判別法）**（講義 Thm 4.6.13）[▶ 46:00](https://youtu.be/uo8ogufaSKA?t=2760)　$p$ 質數，$f\in\mathbb{Z}[x]$，$\deg f\ge1$。$\bar f$ 是係數模 $p$ 的多項式。若 $\bar f$ 在 $\mathbb{Z}_p$ 上不可約**而且 $\deg\bar f = \deg f$**，則 $f$ 在 $\mathbb{Q}$ 上不可約。

**例**[▶ 47:00](https://youtu.be/uo8ogufaSKA?t=2820)：$f = 3x^3+7x+2$。先說模 4——「喔，要質數，我的錯，用 5」——$\bar f = 3x^3+2x+2$ 在 $\mathbb{Z}_5[x]$。「當然你不用真的化簡，在 $\mathbb{Z}_5$ 裡直接用 7 也行。」

【口頭】[▶ 48:00](https://youtu.be/uo8ogufaSKA?t=2880)「重點**簡單得不得了**：約化後的多項式在 $\mathbb{Z}_p$ 上不可約 ⇒ 原本的在 $\mathbb{Z}$ 上不可約。**驚人的定理**。下次證。」

> 💬 課堂上的口頭陳述省略了「$\deg\bar f = \deg f$」，結論說成「在 $\mathbb{Z}$ 上不可約」；上面是講義（Gallian）的完整版本。

**例**[▶ 48:30](https://youtu.be/uo8ogufaSKA?t=2910)：$f = 30x^7+6x^2+3$，模 2……「這全都很臭。我**選得很差**。加個 $x$ 上去——好多了。」改成某個模 2 後變成 $x$ 的版本，宣稱「$x$ 在 $\mathbb{Z}_2$ 上不可約 ⇒ $f$ 在 $\mathbb{Z}$ 上不可約」。

> 💬 這個例子不符合定理條件：首項 $30\equiv0\ (\mathrm{mod}\ 2)$，次數從 7 掉下來，判別法**不能用**。用這個判別法，選的 $p$ 不能整除領導係數。講義的例子是 $29x^3+5x^2+2x+1$，模 2 得 $x^3+x^2+1$，在 $\mathbb{Z}_2$ 沒有根 ⇒ 不可約 ⇒ 原式在 $\mathbb{Q}$ 上不可約（講義 Ex 4.6.14）。

【口頭】[▶ 49:30](https://youtu.be/uo8ogufaSKA?t=2970)「沒有這些定理，我們得去想 7 次多項式怎麼分解成 4 次乘 3 次之類的。喔不，這好太多了。再過去還有 **Eisenstein 判別法**，下次講，更強大。」

---

## 9. 一頁速查表

### 9.1 PID

| 事實 | 關鍵一步 |
|---|---|
| $F[x]$ 是 PID | 取次數最小的 $g$；除法算則 $r = f-qg\in I$ ⇒ $r = 0$ |
| $\mathbb{Z}$ 的理想都是 $n\mathbb{Z}$ | 同樣的論證，取最小正元素 |
| $\ker(f\mapsto f(i)) = \langle x^2+1\rangle$ | 一次式不行（$mi+b\neq0$），$x^2+1$ 在核中 |
| $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$ | 第一同構定理；$a+bx\mapsto a+bi$ 滿射 |

### 9.2 不可約

| 判別 | 條件 | 結論 |
|---|---|---|
| 有根 | 體上，2 或 3 次 | 可約 $\iff$ 有根 |
| 4 次反例 | $(x^2+7)^2$ | 可約但無實根 |
| Gauss | $f\in\mathbb{Z}[x]$ | $\mathbb{Q}$ 上可約 ⇒ $\mathbb{Z}$ 上可約 |
| 模 $p$ | $\bar f$ 不可約、次數不變 | $f$ 在 $\mathbb{Q}$ 上不可約 |

| 多項式 | 不可約在 | 可約在 |
|---|---|---|
| $x^2+1$ | $\mathbb{Q},\mathbb{R},\mathbb{Z}_3$ | $\mathbb{C},\mathbb{Z}_5$ |
| $2x+4$ | $\mathbb{Q}$ | $\mathbb{Z}$ |
| $x^2-7$ | $\mathbb{Q}$ | $\mathbb{R}$ |

### 9.3 術語

| 中文 | English |
|---|---|
| 主理想整環 | principal ideal domain (PID) |
| 良序原理 | well-ordering principle |
| 不可約；可約 | irreducible; reducible (over $D$) |
| 容量 | content |
| 本原多項式 | primitive polynomial |
| 首一多項式 | monic polynomial |
| 模 $p$ 不可約判別法 | mod $p$ irreducibility test |
| Eisenstein 判別法 | Eisenstein's criterion |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **模 $p$ 判別法的證明、Eisenstein** | [[44-L28-整除與分解]] |
| **$\langle p(x)\rangle$ 極大 ⟺ $p$ 不可約** | [[44-L28-整除與分解]]（講義 Thm 4.6.21） |
| **質元 vs. 不可約元** | [[45-L29-不可約與質元-ED-PID-UFD]] |
| **$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$** | [[47-L30-擴張體]]：Kronecker 定理 |
| **多項式的不可約判別** | AA2 [[16-L13-除法算法與不可約性]]、[[17-L14-約化法與Eisenstein判別法]] |

---

## 附：本集一句話總結

> **體上的多項式環是 PID——任何理想都由它裡面次數最小的多項式生成（證明就是除法算則，跟 $\mathbb{Z}$ 的理想都是 $n\mathbb{Z}$ 一模一樣），由此 $f\mapsto f(i)$ 的核是 $\langle x^2+1\rangle$，完整證明 $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$；可約不可約永遠要說「在哪個環上」，2、3 次在體上可約恰好當有根（4 次就失效），而 Gauss 引理和模 $p$ 判別法讓我們把 $\mathbb{Q}$ 上的不可約性化成 $\mathbb{Z}$ 或 $\mathbb{Z}_p$ 上的問題。**

---

## ⚠️ 待確認清單

1. [▶ 48:30](https://youtu.be/uo8ogufaSKA?t=2910) 最後一個例子的完整多項式（字幕：「30x⁷ + 6x² + 3」，之後「加個 $x$」改成模 2 為 $x$ 的版本）。

---

*筆記依據 James S. Cook「Abstract Algebra I」(Fall 2016) Lecture 27 錄影逐字稿（YouTube 自動字幕，50:34）、講義 `AlgebraInotes_2018.pdf` §4.5–4.6（p.147–154）與 Gallian 第 16–17 章整理。*
