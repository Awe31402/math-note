---
course: Abstract Algebra II (Spring 2026)
episode: 11
lecture: L9
date: 2026-02-06
video: https://www.youtube.com/watch?v=6gT1aL4h6I0
notes: 講義/AA2/Math422_Lecture9_EuclideanDomains.pdf
---

# 第 11 集 · L9：歐氏整環、相伴元、質元與不可約元 [▶ 影片](https://www.youtube.com/watch?v=6gT1aL4h6I0&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[10-L8-中國剩餘定理與分式體]] ｜ [總目錄](../README.md) ｜ 下一集：[[12-L10-PID、質元與不可約元]] →

## 本集概要

Dummit & Foote §8.1，加上老師 2018 年 421 講義 Lecture 27 的一部分：
- **範數**（norm）與**歐氏整環**（Euclidean domain，ED）：支援除法算法的整環。輾轉相除一定會停。
- 例：體（範數 0）、$\mathbb{Z}$（絕對值；餘數不唯一，因為單位有 $\pm1$）、$F[x]$（次數）、Gauss 整數 $\mathbb{Z}[i]$（$a^2+b^2$）；$\mathbb{Q}(\sqrt{-19})$ 的整數環**不是** ED。
- **相伴元**（associates）、**不可約元**（irreducible）、**質元**（prime）；**質元一定不可約**。
- 相伴元生成同一個主理想；整環中同一主理想的生成元互為相伴。
- 用 Bill Cook 的網站算多項式的擴充歐幾里得演算法。

> 📘 講義對應：Math422 Lecture 9「Euclidean Domains」；D&F §7.1、§8.1（p.277）；老師 2018 年 421 講義 Lecture 27（Thm 4.7.9、4.7.10）。

---

## 筆記

### 1. 範數與歐氏整環 [▶ 00:30](https://youtu.be/6gT1aL4h6I0?t=30)

（學生把 Euclidean domains 聽成「including domains」——「好沒禮貌」。）

> **定義**：整環 $R$ 上的函數 $N:R\to\mathbb{N}\cup\{0\}$，$N(0) = 0$，叫**範數**（norm）。若 $N(a)>0$ 對所有 $a\ne0$，叫**正範數**。

> **定義**：整環 $R$ 是**歐氏整環**（Euclidean domain），若有範數 $N$ 使得：對任意 $a,b\in R$、$b\ne0$，存在 $q,r\in R$，
> $$a = qb+r,\qquad r = 0\ \text{或}\ N(r)<N(b).$$
> $q$ 叫**商**（quotient），$r$ 叫**餘數**（remainder）[▶ 03:00](https://youtu.be/6gT1aL4h6I0?t=180)。

簡單說：**ED = 支援除法算法的整環**。（$b$ 書上沒名字，老師叫它「除數」；學生說叫「Bob」。）

**輾轉相除** [▶ 04:00](https://youtu.be/6gT1aL4h6I0?t=240)：
$$a = q_0b+r_0,\quad b = q_1r_0+r_1,\quad r_0 = q_2r_1+r_2,\ \dots,\ r_{n-1} = q_{n+1}r_n.$$
$r_n$ 是**最後一個非零餘數**。一定會停：$N(b)>N(r_0)>N(r_1)>\cdots\ge0$ 是嚴格遞減的非負整數列 [▶ 06:00](https://youtu.be/6gT1aL4h6I0?t=360)。
- 這裡的「範數」跟線性代數的範數差很遠（非零元素的範數也可能是 0），但在這種代數裡是標準用語。

### 2. 例子 [▶ 07:30](https://youtu.be/6gT1aL4h6I0?t=450)

**例 1：體都是 ED**。$N(x) = 0$。$a = (ab^{-1})b+0$，餘數永遠 0。「有點蠢，但值得一提。」反過來 ED 不一定是體。

**例 2：$\mathbb{Z}$**，$N(x) = |x|$ [▶ 09:00](https://youtu.be/6gT1aL4h6I0?t=540)。
- 幾何：取 $b>0$，區間 $[kb,(k+1)b)$ 分割實數線。$a$ 落在某一段：$kb\le a<(k+1)b$，所以 $0\le a-kb<b$。取 $q = k$、$r = a-kb$。
- **餘數不唯一** [▶ 12:00](https://youtu.be/6gT1aL4h6I0?t=720)：$a = qb+r$（$0<r<b$）也等於 $(q+1)b+(r-b)$，而 $|r-b| = b-r<b$。例：$30 = 7\cdot4+2 = 7\cdot5-5$。
- 想要唯一，就硬性規定餘數非負。兩種選擇的根源是 $\mathbb{Z}$ 的單位是 $\pm1$。所以 gcd「其實是兩個東西」：gcd 是 1，也是 $-1$。「強迫一切為正讓數論好做，但讓代數變醜。」[▶ 15:30](https://youtu.be/6gT1aL4h6I0?t=930)

> 💬 老師講正負號時被學生帶偏（「等等，我幹嘛聽你們的？」）[▶ 14:00](https://youtu.be/6gT1aL4h6I0?t=840)。

**例 3：$F[x]$**（$F$ 是體），$N(p) = \deg p$（$p\ne0$），$N(0) = 0$ [▶ 17:00](https://youtu.be/6gT1aL4h6I0?t=1020)。老師最喜歡的例子來源。
- 例（$\mathbb{Q}$ 上）：$x^4-5x^2+4 = (x^2-6)(x^2+1)+10$。$N(10) = 0<N(x^2+1) = 2$ [▶ 18:30](https://youtu.be/6gT1aL4h6I0?t=1110)。
- 學生猜範數是「導數」——其實是**次數**（「想太多了」）。
- 除法算法就是多項式長除法；正確性用良序原理證，和 421 證整數除法一樣 [▶ 21:00](https://youtu.be/6gT1aL4h6I0?t=1260)。

**例 4：Gauss 整數** $\mathbb{Z}[i] = \{a+bi\mid a,b\in\mathbb{Z}\}$，$N(a+bi) = a^2+b^2$ [▶ 22:00](https://youtu.be/6gT1aL4h6I0?t=1320)。
- 更一般：$d$ **無平方因子**（square-free，沒有大於 1 的平方因數；例如 100 不是，35 是），$\mathbb{Q}(\sqrt d)$ 裡的**整數環**（代數整數）用 $N(a+b\sqrt d) = a^2-db^2$ [▶ 22:30](https://youtu.be/6gT1aL4h6I0?t=1350)。（D&F §7.1；之後會回來。）
- 有時它是 ED（$d = -1$：Gauss 整數），有時不是：$d = -19$ **不是** ED，證明用「泛側因子」（universal side divisor），D&F p.277，不在課程範圍 [▶ 24:30](https://youtu.be/6gT1aL4h6I0?t=1470)。「證明東西不成立通常要多很多功夫。」

> 💬 補充（非課堂內容）：$d>0$ 時 $a^2-db^2$ 可能是負的，D&F 用的是絕對值 $|a^2-db^2|$。另外 $d = -19$ 的整數環是 $\mathbb{Z}[\frac{1+\sqrt{-19}}2]$，它對**任何**範數都不是 ED，但它是 PID（D&F §8.2）。

### 3. 相伴元、不可約元、質元 [▶ 25:30](https://youtu.be/6gT1aL4h6I0?t=1530)

之前對**理想**定義過這些詞，現在對**元素**定義（老師 2018 講義 Lecture 27 的開頭）。

> **定義**：$D$ 是整環，$a,b\in D$。
> 1. $a,b$ 是**相伴元**（associates），若有單位 $u$ 使 $b = au$。
> 2. $a$ 是**不可約元**（irreducible），若 $a$ 不是單位，且 $a = cd$ 時 $c$ 或 $d$ 是單位。
> 3. $a\ne0$ 是**質元**（prime），若 $a$ 不是單位，且 $a\mid bc$ 時 $a\mid b$ 或 $a\mid c$。

- 不可約 = 只允許「假的」分解（乘一個單位，只是換成相伴元）[▶ 28:00](https://youtu.be/6gT1aL4h6I0?t=1680)。
- 質元 = 把 **Euclid 引理**升格成定義 [▶ 29:30](https://youtu.be/6gT1aL4h6I0?t=1770)。
- 以前我們把「不可約」和「質」混用：大一代數說實數上不能分解的二次式是「質二次式」（prime quadratic）。為什麼可以？學生：「大一代數的學生不在乎。」「這是福音般的真理。」[▶ 30:00](https://youtu.be/6gT1aL4h6I0?t=1800)

> 💬 「我的果汁呢？」（Where's my juice）被學生聽成別的，「你們會害我被開除——或被取消營利，那更糟」；老師說應該加強周邊商品 [▶ 30:30](https://youtu.be/6gT1aL4h6I0?t=1830)。

> **定理**：整環中，質元一定是不可約元 [▶ 31:30](https://youtu.be/6gT1aL4h6I0?t=1890)。

**證明**：$a$ 是質元，$a = xy$。則 $a\mid xy$，所以 $a\mid x$ 或 $a\mid y$。
- 若 $a\mid x$：$x = ab$，所以 $x\cdot1 = x = ab = xyb$。$x\ne0$（否則 $a = 0$），由**消去律** $1 = yb$，$y$ 是單位 [▶ 34:00](https://youtu.be/6gT1aL4h6I0?t=2040)。
- 若 $a\mid y$：同理 $x$ 是單位。
- 所以 $a$ 的分解一定含單位，$a$ 不可約。「好考題：簡單，只要定義清楚。」

### 4. 相伴元與主理想 [▶ 36:00](https://youtu.be/6gT1aL4h6I0?t=2160)

> **定理**（2018 講義 Thm 4.7.9）：$R$ 是有 1 的交換環。
> 1. 若 $a,b$ 相伴，則 $\langle a\rangle = \langle b\rangle$。
> 2. 若 $R$ 是整環，且 $\langle a\rangle = \langle c\rangle$，則 $a,c$ 相伴。

- 老師 421 講義用 $\langle a\rangle$ 表示主理想（LaTeX 的 \langle、\rangle）[▶ 37:30](https://youtu.be/6gT1aL4h6I0?t=2250)。

> **定理**（2018 講義 Thm 4.7.10）：在**主理想整環**（PID）中，元素是質元 $\iff$ 它是不可約元 [▶ 39:30](https://youtu.be/6gT1aL4h6I0?t=2370)。

- 老師想講 D&F §8.1 的 Prop. 3（ED 和 PID 的連結），但手邊的講義不是要的那份，「不想講砸」，下次再說 [▶ 41:30](https://youtu.be/6gT1aL4h6I0?t=2490)。

**證明 Thm 4.7.9** [▶ 49:00](https://youtu.be/6gT1aL4h6I0?t=2940)
1. $a = bu$ ⇒ $b = au^{-1}$。$x = ar\in\langle a\rangle$ ⇒ $x = b(ur)\in\langle b\rangle$，所以 $\langle a\rangle\subseteq\langle b\rangle$；反向同理。「友善的考題。」
2. 若 $\langle a\rangle = 0$，$a = 0$，唯一的生成元是 0，自己和自己相伴 [▶ 50:30](https://youtu.be/6gT1aL4h6I0?t=3030)。否則 $a,c\ne0$，$a\in\langle c\rangle$、$c\in\langle a\rangle$：$a = rc$、$c = sa$，所以 $a = rsa$。由整環的消去律 $rs = 1$，$r,s$ 是單位，$a,c$ 相伴。
   - 老師承認講義沒寫清楚「這裡開始假設是整環」——「這個證明該扣 20%」[▶ 52:00](https://youtu.be/6gT1aL4h6I0?t=3120)。

### 5. 多項式的擴充歐幾里得演算法 [▶ 43:30](https://youtu.be/6gT1aL4h6I0?t=2610)

（學生的鄰居買了一套鼓。）

- 講義有 $\mathbb{Z}_7[x]$、$\mathbb{Z}_3[x]$ 上長除法的例子。$\mathbb{Z}_3$ 那個：餘數是 $x$ 還不能停（$N(x) = 1\ne0$），再除一次，最後非零餘數是常數（範數 0）[▶ 44:30](https://youtu.be/6gT1aL4h6I0?t=2670)。
- 像整數一樣，可以把 $a(x)$、$b(x)$ 的多項式線性組合寫成最後非零餘數（這例子是 1）。
- **老師的秘密武器**：搜尋「Bill Cook math extended Euclidean algorithm」——他哥哥做的網站，輸入兩個多項式，給出 gcd 和 Bézout 組合，可以改模數 [▶ 47:00](https://youtu.be/6gT1aL4h6I0?t=2820)。考試不能用；但考題說「這個多項式恆等式成立」時，它真的成立的機率大增。
- 哥哥是休假時做的——不過北卡州立大學的休假（sabbatical）被州議會禁了，所以叫「帶薪行政假」（學生：「不叫謀殺就不違法？」）。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 範數 | norm | §1 |
| 正範數 | positive norm | §1 |
| 歐氏整環 | Euclidean domain (ED) | §1 |
| 商 / 餘數 | quotient / remainder | §1 |
| Gauss 整數 | Gaussian integers | §2 |
| 無平方因子 | square-free | §2 |
| 代數整數 | algebraic integers | §2 |
| 泛側因子 | universal side divisor | §2 |
| 相伴元 | associates | §3 |
| 不可約元 | irreducible element | §3 |
| 質元 | prime element | §3 |
| 主理想整環 | principal ideal domain (PID) | §4 |
| 擴充歐幾里得演算法 | extended Euclidean algorithm | §5 |

## ⚠️ 待確認清單

（本集無）
