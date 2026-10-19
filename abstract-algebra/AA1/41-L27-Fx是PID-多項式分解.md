---
course: Abstract Algebra I (Fall 2016)
episode: 41
lecture: L27
date: 2016-11-09
video: https://www.youtube.com/watch?v=uo8ogufaSKA
notes: AlgebraInotes_2018.pdf §4.5–4.6（p.143–154）
---

# 第 41 集 · L27：$F[x]$ 是 PID、多項式的分解（一）[▶ 影片](https://www.youtube.com/watch?v=uo8ogufaSKA&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[40-L26-多項式]] ｜ [總目錄](../README.md) ｜ 下一集：[[42-答疑課-上]] →

## 本集概要

- **PID** 定義；**$F[x]$ 是 PID**（$F$ 是體）：理想由次數最小的非零多項式生成。類比：$\mathbb{Z}$ 的理想都是 $n\mathbb{Z}$。
- 例：$\varphi(f) = f(i)$，$\ker\varphi = \langle x^2+1\rangle$，所以 **$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$**（完整證明）。
- **可約 / 不可約 (reducible / irreducible)**——永遠要說「在哪個環上」。例：$x^2+1$、$2x+4$、$x^2-7$、$\mathbb{Z}_3$ vs $\mathbb{Z}_5$ 上的 $x^2+1$。
- **2、3 次多項式在體上可約 $\iff$ 有根**；4 次就失效：$(x^2+7)^2$。
- **容量 (content)**、**本原多項式 (primitive)**、**首一 (monic)**；本原 × 本原 = 本原。
- **在 $\mathbb{Q}$ 上可約 $\Rightarrow$ 在 $\mathbb{Z}$ 上可約**（Gauss 引理）。
- **模 $p$ 不可約判別法**（陳述）。

> 📘 講義對應：2018 講義 §4.5 尾與 §4.6 Lecture 26「factorization of polynomials」（p.143–154）；Gallian 第 16 章尾、第 17 章。

> 💬 大選後第二天，開場：「看來美國還在。」[▶ 00:00](https://youtu.be/uo8ogufaSKA?t=0)

---

## 筆記

### 1. 主理想整環 [▶ 01:00](https://youtu.be/uo8ogufaSKA?t=60)

> **定義**　**主理想整環 (PID)**：每個理想 $I$ 都是主理想（$I = \langle a\rangle = \{ra\mid r\in R\}$）的整環。

> **定理（Gallian Thm 16.3）**　$F$ 是體，則 $F[x]$ 是 PID。

**證明** [▶ 02:30](https://youtu.be/uo8ogufaSKA?t=150)
- 上次證過 $F[x]$ 是整環。剩下：每個理想都是主理想。
- $I = \{0\}$：由 $0$ 生成。
- $I\neq\{0\}$：看 $S = \{\deg f\mid f\in I,\ f\neq0\}$（零多項式沒有次數，所以要排除）。$S$ 是非空的非負整數集，由**良序原理**有最小元素，對應某個 $g(x)\in I$ [▶ 05:00](https://youtu.be/uo8ogufaSKA?t=300)。
- 任取 $f\in I$，除法算則：$f = qg+r$，$r = 0$ 或 $\deg r<\deg g$ [▶ 06:30](https://youtu.be/uo8ogufaSKA?t=390)。
- $r = f - qg$：$f\in I$，$qg\in I$（理想吸收乘法），差也在 $I$（子環）。若 $r\neq0$，它的次數比 $g$ 小，矛盾。所以 $r = 0$，$f = qg\in\langle g\rangle$ [▶ 08:00](https://youtu.be/uo8ogufaSKA?t=480)。
- 得 $I\subseteq\langle g\rangle$；反過來 $\langle g\rangle\subseteq I$ 因為 $g\in I$ 而理想對乘法封閉。所以 $I = \langle g\rangle$。$\blacksquare$

> **定理**　$F$ 是體，$I\neq\{0\}$ 是 $F[x]$ 的理想，$g\in F[x]$。則 $I = \langle g\rangle\iff g$ 是 $I$ 中**次數最小**的非零多項式 [▶ 10:30](https://youtu.be/uo8ogufaSKA?t=630)。

（這是 Gallian 的措辭，老師覺得有點繞。重點：係數要在**體**裡。）

**$\mathbb{Z}$ 的理想是什麼？** [▶ 12:30](https://youtu.be/uo8ogufaSKA?t=750)：學生答「質數」——$2\mathbb{Z}$、$3\mathbb{Z}$ 是例子，但 $4\mathbb{Z}$ 等等也是。答案：**只有 $n\mathbb{Z}$**，證明幾乎一樣（良序原理取最小的正元素）。
- 老師問同事 Smith 教授：形式多項式的建構有什麼意義？對方說它給你一個**形式上等同於整數**的物件。整數和多項式之間的交互作用（兩者的除法算則證明幾乎一樣）會一直出現 [▶ 13:30](https://youtu.be/uo8ogufaSKA?t=810)。

### 2. $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$（完整證明）[▶ 14:30](https://youtu.be/uo8ogufaSKA?t=870)

$\varphi:\mathbb{R}[x]\to\mathbb{C}$，$\varphi(f) = f(i)$（代值，是環同態）。
- $\ker\varphi$ 是 $\mathbb{R}[x]$ 的理想，$\mathbb{R}$ 是體，所以 $\ker\varphi = \langle g\rangle$，$g$ 是核中次數最小的 [▶ 15:30](https://youtu.be/uo8ogufaSKA?t=930)。
- **不可能是一次**：若 $mx+b\in\ker\varphi$，則 $mi+b = 0$，$b = -mi$——實數等於純虛數，荒謬（$m,b$ 不全為 0）[▶ 16:30](https://youtu.be/uo8ogufaSKA?t=990)。
- $\varphi(x^2+1) = i^2+1 = 0$，所以 $x^2+1\in\ker\varphi$，是最小次數 2 的元素。$\ker\varphi = \langle x^2+1\rangle$ [▶ 17:30](https://youtu.be/uo8ogufaSKA?t=1050)。
- **滿射**：$\varphi(a+bx) = a+bi$ [▶ 19:00](https://youtu.be/uo8ogufaSKA?t=1140)。
- 環的第一同構定理：
$$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}.$$

之前說它「看起來像」複數；這是完整證明（學生提醒：還沒驗證 $\varphi$ 是環同態，「好吧，完整但不完整」）[▶ 19:30](https://youtu.be/uo8ogufaSKA?t=1170)。

**對作業的提示** [▶ 18:00](https://youtu.be/uo8ogufaSKA?t=1080)：有些作業（極大、主理想等）現在做起來很吃力，因為工具還不夠；理論發展下去，回頭看會變簡單——這對準備下次考試有用。

### 3. 可約與不可約 [▶ 20:30](https://youtu.be/uo8ogufaSKA?t=1230)

> **定義（Gallian 第 17 章）**　$D$ 是整環。$f\in D[x]$ 是非零、非單位的多項式。若每當 $f = gh$（$g,h\in D[x]$），$g$ 或 $h$ 必為 $D[x]$ 的**單位**，則 $f$ **在 $D$ 上不可約 (irreducible over $D$)**。非零、非單位、又不是不可約的，叫**可約 (reducible)**。

- 老師說 Gallian 這句是本章最糟的句子；簡單說：不是不可約的就是可約 [▶ 22:00](https://youtu.be/uo8ogufaSKA?t=1320)。
- 他犯了「本章的大罪」：沒說「在 $D$ 上」。**可約性永遠綁定係數環** [▶ 23:00](https://youtu.be/uo8ogufaSKA?t=1380)。
- 和「質數」的關係：有時一樣有時不同，之後再談。「如果你的蜘蛛感應在響，大概是對的。」

**例 1：$x^2+1$** [▶ 24:00](https://youtu.be/uo8ogufaSKA?t=1440)
- 在 $\mathbb{R}$、$\mathbb{Q}$ 上不可約。
- 在 $\mathbb{C}$ 上可約：$(x+i)(x-i)$。在 $\mathbb{Q}(i) = \{a+bi\mid a,b\in\mathbb{Q}\}$ 上也可約。需要 $i$ 才能拆開。

**例 2：$2x+4 = 2(x+2)$** [▶ 25:00](https://youtu.be/uo8ogufaSKA?t=1500)
- 在 $\mathbb{Q}$ 上**不可約**：2 是 $\mathbb{Q}$ 的單位（反元素 $\frac12$），這不是「有意義的」分解。
- 在 $\mathbb{Z}$ 上**可約**：2 不是 $\mathbb{Z}$ 的單位。
- 「環裡的單位是什麼」很重要。

**例 3：$x^2-7 = (x+\sqrt7)(x-\sqrt7)$** [▶ 26:30](https://youtu.be/uo8ogufaSKA?t=1590)：在 $\mathbb{Q}$ 上不可約，在 $\mathbb{R}$ 上可約。
- $\mathbb{R}[x]$ 的單位就是非零常數：一個多項式乘另一個多項式要得到 1，只能是常數 [▶ 27:00](https://youtu.be/uo8ogufaSKA?t=1620)。
- 學生問 $x+2$ 為何不是單位：沒有 $f$ 使 $(x+2)f(x) = 1$ [▶ 28:00](https://youtu.be/uo8ogufaSKA?t=1680)。

**例 4：$x^2+1$ 在 $\mathbb{Z}_3$ 和 $\mathbb{Z}_5$ 上** [▶ 28:30](https://youtu.be/uo8ogufaSKA?t=1710)
- $\mathbb{Z}_3$：$f(0) = 1$、$f(1) = 2$、$f(2) = 5 = 2$。**沒有根**，所以沒有一次因式，**不可約**（上一講：體上，有根 $\iff$ 有一次因式）。
- $\mathbb{Z}_5$：$x^2+1 = x^2-4 = (x-2)(x+2) = (x-2)(x-3)$，**可約** [▶ 31:00](https://youtu.be/uo8ogufaSKA?t=1860)。（也可以直接代：$f(2) = f(3) = 0$。）

### 4. 2、3 次多項式 [▶ 32:30](https://youtu.be/uo8ogufaSKA?t=1950)

> **定理（Gallian Thm 17.1）**　$F$ 是體，$\deg f\in\{2,3\}$。$f$ 在 $F$ 上可約 $\iff f$ 在 $F$ 中有根。

**證明** [▶ 34:00](https://youtu.be/uo8ogufaSKA?t=2040)：2、3 次多項式若分解，因式中一定有**一次**的；一次因式對應一個根。反過來，有根 $c$ 就能提出 $x-c$。$\blacksquare$

**4 次就失效** [▶ 35:00](https://youtu.be/uo8ogufaSKA?t=2100)：
$$x^4+14x^2+49 = (x^2+7)^2.$$
在 $\mathbb{Q}$、$\mathbb{R}$ 上可約，但**沒有實根**。（老師一開始說「在 $\mathbb{C}$ 上也沒有根」，隨即劃掉——它在 $\mathbb{C}$ 上有根 $\pm i\sqrt7$ [▶ 36:00](https://youtu.be/uo8ogufaSKA?t=2160)。）

### 5. 容量、本原、首一 [▶ 37:00](https://youtu.be/uo8ogufaSKA?t=2220)

> **定義**　$f = a_nx^n+\cdots+a_0\in\mathbb{Z}[x]$，非零。
> - **容量 (content)**：$\gcd(a_n,\dots,a_0)$。
> - 容量為 1 時，$f$ 是**本原的 (primitive)**。
> - 首項係數為 1 時，$f$ 是**首一的 (monic)**。首一 $\Rightarrow$ 本原 [▶ 39:30](https://youtu.be/uo8ogufaSKA?t=2370)。

**例** [▶ 38:30](https://youtu.be/uo8ogufaSKA?t=2310)：$2x^2+4x+8 = 2(x^2+2x+4)$，容量 2；提出容量後剩下的是本原多項式（這裡還是首一的）。

> **Gauss 引理（Gallian 第 17 章）**　兩個本原多項式的乘積是本原的 [▶ 40:30](https://youtu.be/uo8ogufaSKA?t=2430)。

**證明的關鍵想法**：環同態 $\mathbb{Z}\to\mathbb{Z}_p$ 可以作用在**係數**上，給出環同態 $\mathbb{Z}[x]\to\mathbb{Z}_p[x]$，$f\mapsto\bar f$（係數模 $p$）。Gallian 用上橫線表示。細節在講義。

### 6. 在 $\mathbb{Q}$ 上可約 $\Rightarrow$ 在 $\mathbb{Z}$ 上可約 [▶ 42:00](https://youtu.be/uo8ogufaSKA?t=2520)

> **定理（Gallian Thm 17.2）**　$f\in\mathbb{Z}[x]$。若 $f$ 在 $\mathbb{Q}$ 上可約，則在 $\mathbb{Z}$ 上也可約（分解成兩個次數較低的整係數多項式）。

**例** [▶ 43:00](https://youtu.be/uo8ogufaSKA?t=2580)
$$6x^2+19x-7 = 6\left(x+\tfrac72\right)\left(x-\tfrac13\right) = (2x+7)(3x-1).$$
把 $6 = 2\cdot3$ 拆開分給兩個因式。證明就是這個想法：提出各因式的容量，再重新組合。

- 老師說他「其實還沒被這個定理說服」：為什麼要扯進分數？不如直接在 $\mathbb{Z}$ 上分解。但它會被用在其他定理裡 [▶ 45:00](https://youtu.be/uo8ogufaSKA?t=2700)。
- 學生問反方向：當然有在 $\mathbb{Z}$ 上可約、在 $\mathbb{Q}$ 上不可約的，例如 $2x+4$ [▶ 45:30](https://youtu.be/uo8ogufaSKA?t=2730)。

### 7. 模 $p$ 不可約判別法（陳述）[▶ 46:00](https://youtu.be/uo8ogufaSKA?t=2760)

> **定理（Gallian Thm 17.3）**　$p$ 是質數，$f\in\mathbb{Z}[x]$，$\deg f\ge1$。令 $\bar f\in\mathbb{Z}_p[x]$ 是係數模 $p$ 的多項式。若 $\deg\bar f = \deg f$ 且 $\bar f$ 在 $\mathbb{Z}_p$ 上不可約，則 $f$ 在 $\mathbb{Q}$ 上不可約。

> 💬 課堂上老師的陳述省略了「$\deg\bar f = \deg f$」的條件，結論說成「在 $\mathbb{Z}$ 上不可約」；上面是 Gallian 的完整版本。

**例：約化** [▶ 47:00](https://youtu.be/uo8ogufaSKA?t=2820)：$f = 3x^3+7x+2$，模 5 得 $\bar f = 3x^3+2x+2$。（老師一開始寫成模 4，「應該是質數，我的錯」。）

**例** [▶ 48:30](https://youtu.be/uo8ogufaSKA?t=2910)：老師舉 $30x^7+\cdots+3x+3$，模 2 剩 $x+1$，在 $\mathbb{Z}_2$ 上不可約，說「所以 $f$ 不可約」。

> 💬 這個例子不符合定理的條件：首項 $30\equiv0\pmod2$，次數從 7 掉到 1，判別法**不能用**。要用這個判別法，選的 $p$ 不能整除首項係數。

**好處**：不然要想七次多項式怎麼拆成四次乘三次等等。下次還有更強的 **Eisenstein 判別法** [▶ 50:00](https://youtu.be/uo8ogufaSKA?t=3000)。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 主理想整環 | principal ideal domain (PID) | [01:00](https://youtu.be/uo8ogufaSKA?t=60) |
| 良序原理 | well-ordering principle | [05:00](https://youtu.be/uo8ogufaSKA?t=300) |
| 不可約；可約 | irreducible; reducible (over $D$) | [20:30](https://youtu.be/uo8ogufaSKA?t=1230) |
| 容量 | content | [37:00](https://youtu.be/uo8ogufaSKA?t=2220) |
| 本原多項式 | primitive polynomial | [38:00](https://youtu.be/uo8ogufaSKA?t=2280) |
| 首一多項式 | monic polynomial | [39:30](https://youtu.be/uo8ogufaSKA?t=2370) |
| Gauss 引理 | Gauss's lemma | [40:30](https://youtu.be/uo8ogufaSKA?t=2430) |
| 模 $p$ 不可約判別法 | mod $p$ irreducibility test | [46:00](https://youtu.be/uo8ogufaSKA?t=2760) |
| Eisenstein 判別法 | Eisenstein's criterion | [50:00](https://youtu.be/uo8ogufaSKA?t=3000) |

## ⚠️ 待確認清單

1. [▶ 48:30](https://youtu.be/uo8ogufaSKA?t=2910) 最後一個例子的完整多項式（字幕：「30x⁷ + 6x² + 3」，之後改成含 $3x$ 的版本）。
