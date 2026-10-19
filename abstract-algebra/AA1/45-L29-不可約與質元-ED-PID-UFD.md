---
course: Abstract Algebra I (Fall 2016)
episode: 45
lecture: L29
date: 2016-11-14
video: https://www.youtube.com/watch?v=ry6f4PHRYMM
notes: AlgebraInotes_2018.pdf §4.7–4.8（p.155–164）
---

# 第 45 集 · L29：不可約與質元、Euclid 整環、PID、UFD [▶ 影片](https://www.youtube.com/watch?v=ry6f4PHRYMM&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[44-L28-整除與分解]] ｜ [總目錄](../README.md) ｜ 下一集：[[46-答疑課]] →

## 本集概要

- 例：**7 在 $\mathbb{Z}[\sqrt5]$ 中不可約**（範數 + 模 7）。
- **整環中：質元 $\Rightarrow$ 不可約**。
- 相伴元生成同一個主理想；整環中，同一主理想的生成元彼此相伴。
- **PID 中：質元 $\iff$ 不可約**。
- **Euclid 整環 (ED)**：有範數、有除法算則。例：$\mathbb{Z}$（絕對值）、$F[x]$（次數）、**Gaussian 整數**（$a^2+b^2$；幾何證明除法算則）。在 $\mathbb{Z}[i]$ 中做輾轉相除。
- **互極大理想 (comaximal)**：類比互質。
- Fermat 最後定理的故事：**Lamé 的錯誤證明**假設了唯一分解；$\mathbb{Z}[\sqrt{-5}]$ 中 $46 = 2\cdot23 = (1+3\sqrt{-5})(1-3\sqrt{-5})$。Kummer 的理想數、Dedekind。
- **唯一分解整環 (UFD)** 的定義。

> 📘 講義對應：2018 講義 §4.7 尾與 §4.8 Lecture 28「divisibility in integral domains II」（p.155–164）；Gallian 第 18 章。

---

## 筆記

### 1. 7 在 $\mathbb{Z}[\sqrt5]$ 中不可約 [▶ 00:30](https://youtu.be/ry6f4PHRYMM?t=30)

（$\mathbb{Z}[\sqrt5] = \{a+b\sqrt5\mid a,b\in\mathbb{Z}\}$，$N(a+b\sqrt5) = |a^2-5b^2|$。）
- 設 $7 = xy$。範數乘性：$49 = N(x)N(y)$。若 $x,y$ 都不是單位，則 $N(x) = N(y) = 7$ [▶ 01:00](https://youtu.be/ry6f4PHRYMM?t=60)。
- 要解 $a^2-5b^2 = \pm7$。整數方程難想，**模 7** 看：$a^2-5b^2\equiv0\pmod7$ [▶ 02:30](https://youtu.be/ry6f4PHRYMM?t=150)。
- 逐一檢查（49 種，利用平方可以減少）：唯一解是 $a\equiv b\equiv0\pmod7$。
- 則 $49\mid a^2$、$49\mid5b^2$，所以 $49\mid N(x)$。但 $N(x) = 7$，矛盾 [▶ 05:00](https://youtu.be/ry6f4PHRYMM?t=300)。
- 所以 7 不可約。

> 💬 補充：模 7 的平方是 $\{0,1,2,4\}$，$5b^2$ 的值是 $\{0,5,3,6\}$，只有 0 相同，所以 $a\equiv b\equiv0$。

### 2. 質元 $\Rightarrow$ 不可約 [▶ 06:00](https://youtu.be/ry6f4PHRYMM?t=360)

> **定理（Gallian Thm 18.1）**　整環中，每個質元都是不可約元。

**證明** [▶ 06:30](https://youtu.be/ry6f4PHRYMM?t=390)
- 設 $a$ 是質元，$a = xy$。目標：$x$ 或 $y$ 是單位。
- $a\mid xy$，質元給 $a\mid x$ 或 $a\mid y$。
- 設 $a\mid x$：$x = ab$。則 $x\cdot1 = x = ab = (xy)b = x(yb)$ [▶ 08:30](https://youtu.be/ry6f4PHRYMM?t=510)。
- $a\neq0$ 所以 $x\neq0$（整環）。消去律：$1 = yb$，$y$ 是單位。
- $a\mid y$ 時同理 $x$ 是單位。$\blacksquare$

### 3. 相伴元與主理想（證明）[▶ 10:30](https://youtu.be/ry6f4PHRYMM?t=630)

> **定理**　$R$ 是有單位元的交換環。
> 1. $a,b$ 相伴 $\Rightarrow\langle a\rangle = \langle b\rangle$。
> 2. $R$ 是整環時：$\langle a\rangle = \langle b\rangle\Rightarrow a,b$ 相伴。

**意義**：在整環裡，要找一個主理想的所有生成元，只要看某個生成元的所有相伴元 [▶ 12:00](https://youtu.be/ry6f4PHRYMM?t=720)。整環以外不成立，但反例很複雜（老師的哥哥認為可能要無限的例子）。（這個定理 Gallian 沒有，老師加的，因為對作業有用。）

**(1)** [▶ 12:30](https://youtu.be/ry6f4PHRYMM?t=750)：$a = bu$，$uu' = 1$。$\langle a\rangle = \{rbu\} = \{b(ru)\}$。取 $r = u'$ 得 $b\in\langle a\rangle$，所以 $\langle b\rangle\subseteq\langle a\rangle$；反之顯然。（講義有更乾淨的論證。）

**(2)** [▶ 15:30](https://youtu.be/ry6f4PHRYMM?t=930)：$a\in\langle b\rangle$、$b\in\langle a\rangle$：$a = br$、$b = ar'$。所以 $a = ar'r$。
- $a = 0$ 則 $b = 0$。
- $a\neq0$：消去律得 $r'r = 1$，$r$ 是單位，$a,b$ 相伴。

### 4. PID 中質元 $\iff$ 不可約 [▶ 18:00](https://youtu.be/ry6f4PHRYMM?t=1080)

> **定理（Gallian Thm 18.2）**　PID 中，元素是質元 $\iff$ 它是不可約元。

**($\Rightarrow$)**：PID 是整環，用 §2。

**($\Leftarrow$)** [▶ 19:30](https://youtu.be/ry6f4PHRYMM?t=1170)：設 $a$ 不可約，$a\mid bc$。
- 令 $I = \{ax+by\mid x,y\in D\}$。它是理想（講義有證明）。PID：$I = \langle d\rangle$ [▶ 21:00](https://youtu.be/ry6f4PHRYMM?t=1260)。
- $a = a\cdot1+b\cdot0\in I$，所以 $a = rd$。$a$ 不可約：$r$ 或 $d$ 是單位。
- **$d$ 是單位** [▶ 23:00](https://youtu.be/ry6f4PHRYMM?t=1380)：$1\in I$，$1 = ax+by$。乘 $c$：$c = acx+bcy$。$a$ 整除兩項（$a\mid bc$），所以 $a\mid c$。
- **$r$ 是單位** [▶ 25:30](https://youtu.be/ry6f4PHRYMM?t=1530)：$a$、$d$ 相伴，由 §3 $I = \langle a\rangle$。$b = a\cdot0+b\cdot1\in I$，所以 $a\mid b$。
- 兩種情形都得到 $a\mid b$ 或 $a\mid c$。$\blacksquare$

> 💬 老師中途把「$a$ 和 $r$ 相伴」說錯，學生提醒是「$a$ 和 $d$」——「D 代表 done」[▶ 26:30](https://youtu.be/ry6f4PHRYMM?t=1590)。

**PID 的好處** [▶ 29:30](https://youtu.be/ry6f4PHRYMM?t=1770)：不可約和質元沒有差別。（不可約講的是「分解」；質元講的是「整除」。）

### 5. Euclid 整環 [▶ 30:30](https://youtu.be/ry6f4PHRYMM?t=1830)

> **定義（Euclid 整環 Euclidean domain）**　整環 $D$ 有範數 $N$，且有**除法算則**：任給 $a$、$b\neq0$，存在 $q,r$ 使 $a = qb+r$，且 $r = 0$ 或 $N(r)<N(b)$。

- Gallian 的定義用「測度」$d$，加一條 $d(a)\le d(ab)$。老師說兩者等價，喜歡哪個都行。乘性範數一定滿足 Gallian 的條件：$d(a) = d(ab)/d(b)\le d(ab)$ [▶ 31:30](https://youtu.be/ry6f4PHRYMM?t=1890)。
- **三個主要例子** [▶ 32:00](https://youtu.be/ry6f4PHRYMM?t=1920)：整數（絕對值）、代數整數 $\mathbb{Z}[\sqrt d]$（$|a^2-db^2|$）、多項式（次數）。
- Dummit & Foote 提到：任何體都是 ED（範數全取 0）——「好吧，但沒什麼用」[▶ 33:00](https://youtu.be/ry6f4PHRYMM?t=1980)。

**$\mathbb{Z}$** [▶ 33:30](https://youtu.be/ry6f4PHRYMM?t=2010)：$N = |\cdot|$，乘性。單位 $\pm1$（範數為 1）。
- 這帶來除法算則的**不唯一**：$54 = 6\cdot8+6 = 7\cdot8-2$ [▶ 34:30](https://youtu.be/ry6f4PHRYMM?t=2070)。小學教「餘數取正」只是**人為選擇**；從抽象代數看，$-2$ 這個餘數甚至更好（7×8 比 6×8 更接近 54）。

> 💬 投影上的數字本來是 50，老師改成 54 但沒改完：「我試著用意念改，經上說凡事都能——我的信心不如芥菜種。」[▶ 34:30](https://youtu.be/ry6f4PHRYMM?t=2070)

**$F[x]$** [▶ 36:00](https://youtu.be/ry6f4PHRYMM?t=2160)：範數是次數。**不是乘性**（$\deg(fg) = \deg f+\deg g$），單位是**非零常數**（次數 0）——所以「範數為 1 $\iff$ 單位」只對乘性範數成立。

**Gaussian 整數** [▶ 36:30](https://youtu.be/ry6f4PHRYMM?t=2190)：$N(a+bi) = a^2+b^2$，就是複數平面上到 0 的距離平方。乘性（共軛和模長平方的性質）。

**除法算則（幾何證明）** [▶ 37:30](https://youtu.be/ry6f4PHRYMM?t=2250)
- 給 $\alpha = a+bi$、$\beta = c+di\neq0$。在 $\mathbb{C}$ 裡算 $z = \alpha/\beta$，是一個有理座標的點。
- Gaussian 整數是格點。取**最近**的格點 $q$。最壞情況在正方形中心，離四個角都是 $\sqrt{(1/2)^2+(1/2)^2} = 1/\sqrt2$ [▶ 39:30](https://youtu.be/ry6f4PHRYMM?t=2370)。所以 $|z-q|<1$（其實 $\le1/\sqrt2$）。
- 令 $r = \alpha-q\beta$。則 $|r/\beta| = |z-q|\le1/\sqrt2$，所以 $N(r)\le N(\beta)/2<N(\beta)$ [▶ 42:00](https://youtu.be/ry6f4PHRYMM?t=2520)。
- 例：$z = 3.7+4.9i$，取 $q = 4+5i$（學生答對）[▶ 41:30](https://youtu.be/ry6f4PHRYMM?t=2490)。

> 💬 學生指出投影上漏了一個 1——老師說「我用白色寫的」[▶ 40:00](https://youtu.be/ry6f4PHRYMM?t=2400)。

**$\mathbb{Z}[i]$ 中的輾轉相除** [▶ 42:30](https://youtu.be/ry6f4PHRYMM?t=2550)：$\alpha = 11+3i$、$\beta = 2+3i$。
- $(2-2i)(2+3i) = 10+2i$，所以 $11+3i = (2-2i)\beta + (1+i)$。實部、虛部都差 1，$N(1+i) = 2<13 = N(\beta)$ [▶ 44:30](https://youtu.be/ry6f4PHRYMM?t=2670)。
- $(3+i)(1+i) = 2+4i$，所以 $2+3i = (3+i)(1+i) + (-i)$ [▶ 46:00](https://youtu.be/ry6f4PHRYMM?t=2760)。
- 倒推回去，把 $-i$ 寫成 $\alpha$、$\beta$ 的組合，再乘 $i$，得到 $1 = (\cdots)\alpha+(\cdots)\beta$——**Bézout 等式**的類比。
- 怎麼選商？用複數除法算出有理形式，取最近的格點；就像用計算機算整數除法的餘數 [▶ 45:30](https://youtu.be/ry6f4PHRYMM?t=2730)。

### 6. 互極大理想 [▶ 47:00](https://youtu.be/ry6f4PHRYMM?t=2820)

兩個理想相加得到整個環，叫**互極大 (comaximal)**。類比**互質**：$\langle3\rangle+\langle5\rangle = \mathbb{Z}$，因為 Bézout 給 $3x+5y = 1$。在更抽象的環裡，互極大理想扮演互質整數的角色。

### 7. Fermat 最後定理與唯一分解 [▶ 48:00](https://youtu.be/ry6f4PHRYMM?t=2880)

- **Fermat 最後定理**：$x^n+y^n = z^n$（$n\ge3$）沒有正整數解。
- 個別的 $n$ 可以用特殊方法擊破，例如 $n = 3$ 在 $\mathbb{Z}[\sqrt{-3}]$ 之類的環裡做，三頁的血腥計算（John Stillwell《Elements of Number Theory》）；Euler、Legendre 等人做過一些 [▶ 48:30](https://youtu.be/ry6f4PHRYMM?t=2910)。
- **Gabriel Lamé** 給過一個**錯誤證明**：他假設這類環有**唯一分解** [▶ 49:00](https://youtu.be/ry6f4PHRYMM?t=2940)。

**反例：$\mathbb{Z}[\sqrt{-5}]$** [▶ 49:30](https://youtu.be/ry6f4PHRYMM?t=2970)
$$46 = 2\cdot23 = (1+3\sqrt{-5})(1-3\sqrt{-5}).$$
- 四個因數都是**不可約**的；2、23 都不和 $1\pm3\sqrt{-5}$ 相伴。
- 所以有兩種本質不同的不可約分解，唯一分解失敗。
- **Kummer** 早就指出這個危險，提出「**理想數 (ideal numbers)**」；之後 **Dedekind** 把它嚴格化（就是今天的「理想」），和其他人一起證明了 Fermat 最後定理的許多情形 [▶ 51:30](https://youtu.be/ry6f4PHRYMM?t=3090)。
- 定理最終的證明靠的是近代複雜得多的東西。

### 8. 唯一分解整環 [▶ 52:00](https://youtu.be/ry6f4PHRYMM?t=3120)

> **定義（唯一分解整環 UFD）**　整環 $D$，每個非零、非單位的元素都能寫成不可約元的乘積；而且任兩個這樣的分解，在**重新排序**和**相伴**的意義下相同。

「我們幾乎講完了，信不信由你。」

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| Euclid 整環 | Euclidean domain (ED) | [30:30](https://youtu.be/ry6f4PHRYMM?t=1830) |
| 測度（Gallian） | measure | [31:00](https://youtu.be/ry6f4PHRYMM?t=1860) |
| 代數整數 | algebraic integers | [32:00](https://youtu.be/ry6f4PHRYMM?t=1920) |
| 互極大理想 | comaximal ideals | [47:00](https://youtu.be/ry6f4PHRYMM?t=2820) |
| Fermat 最後定理 | Fermat's Last Theorem | [48:00](https://youtu.be/ry6f4PHRYMM?t=2880) |
| 理想數 | ideal numbers (Kummer) | [51:30](https://youtu.be/ry6f4PHRYMM?t=3090) |
| 唯一分解整環 | unique factorization domain (UFD) | [52:00](https://youtu.be/ry6f4PHRYMM?t=3120) |

## ⚠️ 待確認清單

（本集無）
