---
course: Number Theory（2021 秋，線上錄影）
episode: 38
lecture: 2021-11-08 第 1 部
date: 2021-11-08
video: https://youtu.be/NtLY8zphbb4
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.6（p. 152–154）：Theorem 4.6.21 (⇐)、Corollary 4.6.22–4.6.23、Example 4.6.24–4.6.25、Theorem 4.6.26；§4.7 Lecture 27（p. 155–157）：Definition 4.7.1、Example 4.7.2、Definition 4.7.3–4.7.4、Theorem 4.7.5、Example 4.7.6–4.7.7、Theorem 4.7.8
---

# 第 38 集 · 有限體的計算、相伴元、不可約元與質元（PIDs, Euclidean Domains, and UFDs, Quick Overview, Part 1） [▶ 影片](https://youtu.be/NtLY8zphbb4)

← 上一集：[37-pids-factorization-eisenstein-2](37-pids-factorization-eisenstein-2.md) ｜ [總目錄](README.md) ｜ 下一集：[39-pids-euclidean-domains-ufds-2](39-pids-euclidean-domains-ufds-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 38 集（2021-11-08 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；結尾被切斷）＋ 講者講義 §4.6–4.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 不可約 ⇒ ⟨p(x)⟩ 極大（收尾）](#1-不可約--px-極大收尾)
- [2. 兩個推論](#2-兩個推論)
- [3. 在有限體裡算：用 α 代替陪集](#3-在有限體裡算用-α-代替陪集)
  - [3.1 Z₂[x]/⟨x³ + x + 1⟩：8 個元素](#31-zxx--x--1-8-個元素)
  - [3.2 R[x]/⟨x² + 1⟩：α 就是 i](#32-rxx--1-α-就是-i)
- [4. Z[x] 有唯一分解](#4-zx-有唯一分解)
- [5. 相伴元、不可約元、質元](#5-相伴元不可約元質元)
- [6. 例子：1 + √−3 不可約但不是質元](#6-例子1--3-不可約但不是質元)
- [7. Z[√d] 的範數](#7-zd-的範數)
- [8. 質元一定不可約](#8-質元一定不可約)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:02](https://youtu.be/NtLY8zphbb4?t=2)

收尾講義 Lecture 26（定理 4.6.21 的後半、推論、有限體的計算記號），然後進入 Lecture 27：**整環裡的整除**——相伴元、不可約元、質元。

（講者一開始說有學生來補考，他先去開考，讓大家趁機抄筆記。）

| 主題 | 時間 | 講義 |
|---|---|---|
| 定理 4.6.21 (⇐) | 00:02 | Thm 4.6.21 |
| 推論 | 07:10 | Cor 4.6.22–4.6.23 |
| $\alpha$ 記號、8 元素體 | 14:51 | Ex 4.6.24 |
| $\mathbb{R}[x]/\langle x^2+1\rangle$ | 27:31 | — |
| $\mathbb{Z}[x]$ 是 UFD | 31:47 | Thm 4.6.26 |
| 相伴、不可約、質 | 32:47 | Def 4.7.1 |
| $1+\sqrt{-3}$ | 40:49 | Ex 4.7.2、4.7.6 |
| 範數 | 54:51 | Def 4.7.4、Thm 4.7.5 |
| 質 ⇒ 不可約 | 57:16 | Thm 4.7.8 |

---

## 1. 不可約 ⇒ ⟨p(x)⟩ 極大（收尾）

[▶ 00:02](https://youtu.be/NtLY8zphbb4?t=2)

接第 37 集定理 4.6.21 的 (⇐)：設 $p(x)$ 在體 $F$ 上不可約，理想 $I$ 滿足 $\langle p\rangle\subseteq I\subseteq F[x]$。

1. **$F[x]$ 是 PID**（第 36 集）：$I = \langle g\rangle$ [▶ 01:04](https://youtu.be/NtLY8zphbb4?t=64)。
2. **$p\in\langle p\rangle\subseteq\langle g\rangle$** [▶ 02:06](https://youtu.be/NtLY8zphbb4?t=126)：講者說這是很多證明的一般步驟——「生成元本身在它生成的理想裡」。所以 $p = kg$。
3. $p$ 不可約，所以 $k$ 或 $g$ 是單位——**單位就是非零常數**，所以 $\deg k = 0$ 或 $\deg g = 0$。
4. $\deg k = 0$ [▶ 04:59](https://youtu.be/NtLY8zphbb4?t=299)：$p = cg$，所以 $\langle p\rangle = \langle g\rangle = I$。
5. $\deg g = 0$ [▶ 05:34](https://youtu.be/NtLY8zphbb4?t=334)：$g$ 是非零常數。任何 $f = c\cdot\frac1cf$，所以 $\langle g\rangle = F[x]$。「用單位生成理想，就得回整個環——像 $\langle 1\rangle = R$。」
6. 所以中間的理想只能是 $\langle p\rangle$ 或 $F[x]$，**$\langle p\rangle$ 是極大理想**。∎

【口頭】[▶ 04:15](https://youtu.be/NtLY8zphbb4?t=255) 講者一度不確定「不可約」的定義是否排除單位，「我現在有點慌」。（定義是排除的：不可約要求「不是 0、不是單位」，第 36 集。）

---

## 2. 兩個推論

> **推論**（講義 Corollary 4.6.22）[▶ 07:10](https://youtu.be/NtLY8zphbb4?t=430)：$p(x)$ 在 $F$ 上不可約 ⇒ $F[x]/\langle p(x)\rangle$ 是體。
> **證明**：不可約 ⇒ $\langle p\rangle$ 極大 ⇒ 環模極大理想是體（第 31 集）。

> **推論**（講義 Corollary 4.6.23）[▶ 08:11](https://youtu.be/NtLY8zphbb4?t=491)：$p(x)$ 在 $F$ 上不可約，$p\mid a(x)b(x)$，則 $p\mid a$ 或 $p\mid b$。

**證明** [▶ 09:43](https://youtu.be/NtLY8zphbb4?t=583)：

1. $p$ 不可約 ⇒ $\langle p\rangle$ 極大 ⇒ **質理想**（極大 ⇒ 質，第 31 集）。另一個看法：$F[x]/\langle p\rangle$ 是體，所以是整環，所以 $\langle p\rangle$ 是質理想。
2. $p\mid ab$ ⇒ $ab = kp\in\langle p\rangle$ [▶ 11:33](https://youtu.be/NtLY8zphbb4?t=693)。
3. 質理想：$a\in\langle p\rangle$ 或 $b\in\langle p\rangle$。
4. 也就是 $a = gp$ 或 $b = hp$：$p\mid a$ 或 $p\mid b$。∎

【口頭】[▶ 12:45](https://youtu.be/NtLY8zphbb4?t=765) 「我們現在有好多定義在飛：質理想、極大理想、不可約元素、單位……我想我們還沒定義**質元素**。」（第 5 節。）

講者說這個定理在證明 $\mathbb{Z}[x]$ 是唯一分解整環時很重要，唯一性就來自它，但「我們大概不會講那個證明的細節」。

---

## 3. 在有限體裡算：用 α 代替陪集

[▶ 14:51](https://youtu.be/NtLY8zphbb4?t=891)

講者說他在作業裡試著鼓勵這種記號，但講義沒寫：在商環裡**實際計算**時，用什麼記號好？

### 3.1 Z₂[x]/⟨x³ + x + 1⟩：8 個元素

（講義 Example 4.6.24）

**$x^3+x+1$ 在 $\mathbb{Z}_2$ 上不可約** [▶ 15:27](https://youtu.be/NtLY8zphbb4?t=927)：3 次，看有沒有根。$p(0) = 1$、$p(1) = 1+1+1 = 1$。沒有根，不可約（第 36 集）。

【課堂討論】[▶ 15:57](https://youtu.be/NtLY8zphbb4?t=957) 講者問：實數上有不可約的三次多項式嗎？**沒有**——由**中間值定理**，每個實係數三次多項式都會穿過 $x$ 軸，一定能提出一次因式。但在 $\mathbb{Z}_2$ 上情況不同。講者：在 $\mathbb{Q}$ 或 $\mathbb{Z}_n$ 上，可以有**任意高次**的不可約多項式。

所以 $\mathbb{Z}_2[x]/\langle x^3+x+1\rangle$ 是體。

**記號** [▶ 17:32](https://youtu.be/NtLY8zphbb4?t=1052)：寫 $x^3+x+1+\langle\cdots\rangle$「不是好記號」。改成令
$$\alpha = x+\langle x^3+x+1\rangle.$$

- 在商環裡 $x^3 = -x-1$，任何高次方都能壓成常數、$x$、$x^2$。所以每個元素是 $a+bx+cx^2+\langle\cdots\rangle$。
- 用 $\alpha$ 寫：**$a+b\alpha+c\alpha^2$**，「一點障眼法」，不用把理想寫出來。
- **規則**：$\alpha^3 = -\alpha-1$。

**有幾個元素？** [▶ 19:08](https://youtu.be/NtLY8zphbb4?t=1148)

【課堂討論】學生一開始說 6 種組合。講者：三位數的十進位數有幾個？1000 個（000 到 999）。這裡 $a,b,c$ 各有 2 種選擇，所以 $2^3 = 8$ 個：
$$0,\ 1,\ \alpha,\ 1+\alpha,\ \alpha^2,\ 1+\alpha^2,\ \alpha+\alpha^2,\ 1+\alpha+\alpha^2.$$
（講者列的時候漏了 $1+\alpha+\alpha^2$，「我漏了什麼？」最後補上。）

**乘法** [▶ 22:17](https://youtu.be/NtLY8zphbb4?t=1337)：例如
$$(1+\alpha)(1+\alpha^2) = 1+\alpha^2+\alpha+\alpha^3.$$
把 $\alpha^3$ 換成定義關係，再化簡（模 2，$1+1 = 0$）。

**反元素** [▶ 23:20](https://youtu.be/NtLY8zphbb4?t=1400)：這是體，非零元素都有反元素。由 $\alpha^3+\alpha = -1 = 1$（模 2）：
$$\alpha\,(\alpha^2+1) = 1.$$
所以 **$\alpha^{-1} = \alpha^2+1$**，$(\alpha^2+1)^{-1} = \alpha$。

【口頭】講者本來想問 $\alpha^2$ 的反元素，「那會是好作業題，但我作業都寫好了，運氣不好，只好放期末考」。

**一個正負號** [▶ 24:23](https://youtu.be/NtLY8zphbb4?t=1463)【Q&A】學生問：你說 $\alpha^3 = 1-\alpha$，怎麼來的？講者發現漏了負號：應該是 $\alpha^3 = -\alpha-1$（因為 $x^3+\langle\cdots\rangle = -x+\langle\cdots\rangle+(-1)+\langle\cdots\rangle$）。「好笑的是這不改變任何事」——在 $\mathbb{Z}_2$ 裡 $-1 = 1$。「很少有例子能犯這麼多錯卻不太需要改正。」

> 以下**不是逐字稿內容**，是把 $(1+\alpha)(1+\alpha^2)$ 算完：模 2 時 $\alpha^3 = \alpha+1$，
> $$1+\alpha+\alpha^2+\alpha^3 = 1+\alpha+\alpha^2+(\alpha+1) = \alpha^2.$$

> 【講義補充】Example 4.6.24（p. 153）的計算：$x\cdot x^2 = x^3 = x+1$、$x^2\cdot x^2 = x^2+x$、$(x+1)(x^2+x) = 1$。（所以 $x+1$ 和 $x^2+x$ 互為反元素。）

### 3.2 R[x]/⟨x² + 1⟩：α 就是 i

[▶ 27:31](https://youtu.be/NtLY8zphbb4?t=1651)

$x^2+1$ 在 $\mathbb{R}$ 上不可約。令 $\alpha = x+\langle x^2+1\rangle$，元素是 $a+b\alpha$（$a,b\in\mathbb{R}$），規則 $\alpha^2+1 = 0$。

**另一種看法** [▶ 29:05](https://youtu.be/NtLY8zphbb4?t=1745)：我們在實數上**添加一個新元素 $\alpha$**——「它原本不存在，是個新數」，滿足 $\alpha^2+1 = 0$。這**就是 $i$**。

**反元素**：$1 = -\alpha^2 = \alpha\cdot(-\alpha)$，所以 $\alpha^{-1} = -\alpha$。（就是 $\frac1i = -i$。）

講者 [▶ 30:12](https://youtu.be/NtLY8zphbb4?t=1812)：**定義多項式裡有常數項 1 的話**，就能很容易找到添加元素的反元素（像上面兩個例子那樣提出 $\alpha$）。

**作業提示** [▶ 30:44](https://youtu.be/NtLY8zphbb4?t=1844)：8 元素體是 $\mathbb{Z}_2$ 上模一個三次式，$2^3 = 8$。作業要造 **27 個元素的體**：在 $\mathbb{Z}_3[x]$ 裡找一個不可約三次式模掉，$a,b,c$ 各在 $\{0,1,2\}$ 裡，$3^3 = 27$。不用列出 27 個元素，只要構造它、論證它是體、為什麼有 27 個。（作業不做解答。）

---

## 4. Z[x] 有唯一分解

[▶ 31:47](https://youtu.be/NtLY8zphbb4?t=1907)

> **定理**（講義 Theorem 4.6.26）：$\mathbb{Z}[x]$ 裡每個非零、非單位的多項式都能寫成
> $$f(x) = b_1b_2\cdots b_s\,p_1(x)p_2(x)\cdots p_m(x),$$
> $b_i$ 是 0 次的不可約多項式（整數質數），$p_j$ 是正次數的不可約多項式；而且這個分解在順序和正負號之外唯一。

講者：「我沒有證明給你們看，只想讓你們知道。」

> 【講義補充】Theorem 4.6.26 的證明（p. 154）指向 Gallian，三個階段：(1) 先提出**內容**（係數的 gcd），用整數的質因數分解處理；(2) 剩下的本原多項式用簡單的歸納法分解成不可約因式；(3) 唯一性靠 Gauss 引理的多項式版本，加上 $\mathbb{Z}$ 的單位只有 $\pm1$。

---

## 5. 相伴元、不可約元、質元

[▶ 32:47](https://youtu.be/NtLY8zphbb4?t=1967)

講者說會改用投影片，但「這個我們該全部寫下來，很重要」。

> **定義**（講義 Definition 4.7.1）：$D$ 是整環，$a,b\in D$。
> 1. **相伴元**（associates）：存在單位 $u$ 使 $b = au$。
> 2. **不可約元**（irreducible）：$a$ 不是單位，而且每當 $a = cd$，$c$ 或 $d$ 是單位。
> 3. **質元**（prime）：$a\neq0$ 不是單位，而且 $a\mid bc$ ⇒ $a\mid b$ 或 $a\mid c$。

（【課堂討論】整環：有單位元素、可交換、沒有零因子。）

**跟整數的質數不一樣？** [▶ 35:39](https://youtu.be/NtLY8zphbb4?t=2139)【課堂討論】講者問：整數裡質數平常怎麼定義？學生：只被 1 和自己整除。講者：

- 那其實是**不可約**的定義（允許負因數的話，$p$ 的因數只有 $\pm1,\pm p$）。
- 這裡的「**質**」是我們在整數裡叫做 **Euclid 引理**的那個性質（$p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$，第 5 集）。
- 「抽象的意義跟你在 $\mathbb{Z}$ 裡熟悉的用法有點衝突，但這是標準定義。」

【Q&A】[▶ 36:52](https://youtu.be/NtLY8zphbb4?t=2212) 學生以為講者說「質 ⇔ 那個式子」。講者：這是定義（可以在每條加「若且唯若」）；**在很多常見的情況，質和不可約可以互換，但不總是**——下一個例子。

**相伴元的例子** [▶ 37:23](https://youtu.be/NtLY8zphbb4?t=2243)：

| 環 | 單位 | 相伴元 |
|---|---|---|
| $\mathbb{Z}$ | $\pm1$ | $5$ 和 $-5$（$5 = (-1)(-5)$）——一對一對 |
| $\mathbb{Z}[i]$ | $\pm1,\pm i$ | $3+2i$ 有 4 個：$\pm(3+2i)$、$\pm i(3+2i)$ |
| 體 $F$ | 所有非零元素 | **任意兩個非零元素都相伴** |

【課堂討論】[▶ 39:09](https://youtu.be/NtLY8zphbb4?t=2349) 講者要學生證明體裡 $b = \square\cdot c$（$c\neq0$）：學生答 $b = (bc^{-1})c$。講者：「單位越多，相伴元越多。」

> 【講義補充】Definition 4.7.1 後面（p. 155）：「不可約」和「質」在你的數學教育中常被互換，例如有些書把多項式的不可約因式叫「質因式」。在 $\mathbb{Z}$ 裡兩者等價，但**在一般的環裡不等價**。

---

## 6. 例子：1 + √−3 不可約但不是質元

[▶ 40:49](https://youtu.be/NtLY8zphbb4?t=2449)（講義 Example 4.7.2，出自 Gallian p. 313）

講者：「確保定義不只是從你身邊流過——要真的懂定義，需要例子，也需要反例來對照。」

在 $\mathbb{Z}[\sqrt{-3}]$ 裡（第 22 集，「課程有些重複，我盡量不全部重做」）。【Q&A】它是整環嗎？是，沒有零因子。

$$(1+\sqrt{-3})(1-\sqrt{-3}) = 1-(-3) = 4 = 2\cdot 2.$$

（講者一開始算成 2，「我掉了一個負號，是 4」。）

所以 $1+\sqrt{-3}$ **整除** $2\cdot 2$。

**但 $1+\sqrt{-3}\nmid 2$** [▶ 44:20](https://youtu.be/NtLY8zphbb4?t=2660)（講者讓學生自己證，他去發考卷）：假設 $(1+\sqrt{-3})(a+b\sqrt{-3}) = 2$。展開：
$$(a-3b)+(a+b)\sqrt{-3} = 2.$$
比較係數：$a-3b = 2$、$a+b = 0$。所以 $b = -a$，$a+3a = 4a = 2$，$a = \frac12$——**不是整數**。

所以 **$1+\sqrt{-3}$ 不是質元**：它整除 $2\cdot2$，卻不整除任何一個 2。

**但它是不可約的** [▶ 46:29](https://youtu.be/NtLY8zphbb4?t=2789)（講義 Example 4.7.6）：

【課堂討論】要用範數。學生：$N(a+b\sqrt{-3}) = a^2+3b^2$。

1. 設 $1+\sqrt{-3} = \alpha\beta$。範數有乘性（「一個半月前證的性質還是對的，想不到吧」）：$N(1+\sqrt{-3}) = 4 = N(\alpha)N(\beta)$。
2. $N(\alpha) = 1\iff\alpha$ 是單位。若 $\alpha,\beta$ 都不是單位，只能 $N(\alpha) = N(\beta) = 2$。
3. $a^2+3b^2 = 2$：$b\neq0$ 就已經 $\ge3$；$b=0$ 時 $a^2 = 2$ 沒有整數解 [▶ 50:04](https://youtu.be/NtLY8zphbb4?t=3004)。
4. 所以不可能，每個分解都有單位，**$1+\sqrt{-3}$ 不可約**。

講者 [▶ 51:04](https://youtu.be/NtLY8zphbb4?t=3064)：「所以在這個情況下，**質和不可約是有區別的**。」

（第 22 集：$\mathbb{Z}[\sqrt{-3}]$ 唯一分解失敗——$4 = 2\cdot 2 = (1+\sqrt{-3})(1-\sqrt{-3})$——根源就在這裡：有不可約元不是質元。）

【口頭】[▶ 53:43](https://youtu.be/NtLY8zphbb4?t=3223) 講者開投影機時開玩笑：「看到有人打瞌睡就馬上叫他做伏地挺身。」「$2+3i$ 個伏地挺身——對你們太複雜了？別開那種玩笑，不好笑。」

---

## 7. Z[√d] 的範數

[▶ 54:51](https://youtu.be/NtLY8zphbb4?t=3291)

> **定義**（講義 Definition 4.7.4）：$d$ 無平方因子，$N(a+b\sqrt d) = |a^2-db^2|$。

講者：加絕對值是為了同時處理 $d>0$ 和 $d<0$。$d<0$ 時就是 $a^2+|d|b^2$，不需要絕對值；Pell 方程那種 $d>0$ 才需要。

> 【講義補充】
>
> **Definition 4.7.3**（p. 155，取自 Dummit & Foote p. 270）：整環 $R$ 上任何滿足 $N(0) = 0$ 的函數 $N:R\to\mathbb{N}\cup\{0\}$ 都叫**範數**；若 $a\neq0$ 時 $N(a)>0$，叫**正範數**。
>
> **Theorem 4.7.5**（p. 156）：$N(a+b\sqrt d) = |a^2-db^2|$ 滿足
> 1. $N(x) = 0\iff x = 0$；
> 2. $N(xy) = N(x)N(y)$；
> 3. $x$ 是單位 $\iff N(x) = 1$；
> 4. $N(x)$ 是質數 ⇒ $x$ 不可約。
>
> 證明 (3)：$xy = 1$ ⇒ $1 = N(1) = N(x)N(y)$，整數乘積是 1 ⇒ $N(x) = 1$。(4)：$x = yz$ ⇒ $N(x) = N(y)N(z)$ 是質數 ⇒ 其中一個是 1 ⇒ 是單位。（跟第 15、18 集高斯整數的證明一樣。）

**Example 4.7.7** [▶ 55:21](https://youtu.be/NtLY8zphbb4?t=3321)：講者說證明不可約不總是那麼容易，這個例子是「迷宮裡轉角的下一個 boss」，步驟多一點，讓大家自己看。

> 【講義補充】Example 4.7.7（p. 156，Gallian p. 313 Example 2）：證 $7$ 在 $\mathbb{Z}[\sqrt5]$ 裡不可約。若 $7 = xy$ 非平凡，$N(x) = N(y) = 7$，即 $a^2-5b^2 = \pm7$。模 7 檢查，唯一解是 $a\equiv b\equiv0$，所以 $7\mid a$、$7\mid b$，$49\mid a^2-5b^2$——但它等於 $\pm7$，矛盾。講義說 Gallian 警告 $d>1$ 時在 $\mathbb{Z}[\sqrt d]$ 裡證東西比較麻煩。

---

## 8. 質元一定不可約

[▶ 57:16](https://youtu.be/NtLY8zphbb4?t=3436)

> **定理**（講義 Theorem 4.7.8）：**在整環裡，每個質元都是不可約元。**

**證明**：設 $a$ 是質元，$a = xy$。

1. $a\mid xy$（$xy = a$），所以 $a\mid x$ 或 $a\mid y$。
2. 設 $a\mid x$：$x = ab$。則 [▶ 57:51](https://youtu.be/NtLY8zphbb4?t=3471)
   $$x\cdot 1 = x = ab = (xy)b = x(yb).$$
3. **整環的消去律**（不是反元素存在）：$1 = yb$，所以 $y$ 是單位。
4. $a\mid y$ 的情況類似，$x$ 是單位。
5. 任意分解都有一個因式是單位，$a$ 不可約。∎

【課堂討論】[▶ 58:21](https://youtu.be/NtLY8zphbb4?t=3501) 講者問：這對 $\mathbb{Z}[\sqrt{-3}]$ 說了什麼？學生在想「不是質元」的情況。講者：這個定理**直接**說的是「質 ⇒ 不可約」；它的逆否是「**不是不可約 ⇒ 不是質**」。（影片在這裡被切斷，接第 39 集。）

> 以下**不是逐字稿內容**，是補一句：反方向「不可約 ⇒ 質」一般不成立（第 6 節的 $1+\sqrt{-3}$ 就是反例），但在 PID 裡成立——第 39 集。

---

## 9. 一頁速查表

**不可約 ⇒ $\langle p\rangle$ 極大**：$F[x]$ 是 PID，$I = \langle g\rangle$，$p = kg$ ⇒ $k$ 或 $g$ 是常數 ⇒ $I = \langle p\rangle$ 或 $F[x]$。

**推論**：$p$ 不可約 ⇒ $F[x]/\langle p\rangle$ 是體；$p\mid ab$ ⇒ $p\mid a$ 或 $p\mid b$。

**計算記號**：$\alpha = x+\langle p(x)\rangle$，元素寫成 $\alpha$ 的多項式，用 $p(\alpha) = 0$ 化簡。

| 體 | 元素 | 規則 | 例 |
|---|---|---|---|
| $\mathbb{Z}_2[x]/\langle x^3+x+1\rangle$ | $a+b\alpha+c\alpha^2$，8 個 | $\alpha^3 = \alpha+1$ | $\alpha^{-1} = \alpha^2+1$ |
| $\mathbb{R}[x]/\langle x^2+1\rangle$ | $a+b\alpha$ | $\alpha^2 = -1$ | $\alpha^{-1} = -\alpha$ |

實數上沒有不可約三次式（中間值定理）；$\mathbb{Q}$、$\mathbb{Z}_p$ 上有任意高次的不可約式。

**$\mathbb{Z}[x]$ 是 UFD**（不證）。

**三個定義**（整環 $D$）

| 名稱 | 條件 |
|---|---|
| 相伴 | $b = au$，$u$ 單位 |
| 不可約 | 非單位，$a = cd$ ⇒ $c$ 或 $d$ 是單位（整數的「只被 $\pm1,\pm p$ 整除」） |
| 質 | 非零非單位，$a\mid bc$ ⇒ $a\mid b$ 或 $a\mid c$（Euclid 引理） |

**質 ⇒ 不可約**（整環）。**關鍵一步**：$x = x(yb)$ ⇒（消去）$yb = 1$。

**不可約 ⇏ 質**：$\mathbb{Z}[\sqrt{-3}]$ 裡 $1+\sqrt{-3}$ 不可約（$a^2+3b^2 = 2$ 無解），但整除 $2\cdot2$、不整除 $2$（$4a = 2$）。

**範數** $N(a+b\sqrt d) = |a^2-db^2|$：乘性；單位 ⇔ $N=1$；$N$ 是質數 ⇒ 不可約。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 相伴與主理想：$\langle a\rangle = \langle b\rangle$ ⇔ $a,b$ 相伴 | 第 39 集 |
| PID 裡不可約 ⇔ 質 | 第 39 集 |
| Euclid 整環 ⇒ PID ⇒ UFD；$\mathbb{Z}[\sqrt{-5}]$ 不是 UFD | 第 39 集 |
| $F[x]/\langle p\rangle$ 的 $\alpha$ 記號 ⇒ $F(\alpha)$ | 第 40–43 集 |
| 有限體 $p^n$ 個元素 | 第 40–45 集 |

---

## 附：本集一句話總結

> **不可約多項式生成極大理想，所以 $F[x]/\langle p(x)\rangle$ 是體；計算時把 $x$ 的陪集記成 $\alpha$，用 $p(\alpha)=0$ 化簡，就能在 8 個元素的 $\mathbb{Z}_2[x]/\langle x^3+x+1\rangle$ 裡算反元素。在一般整環裡要分清楚三個概念：相伴（差一個單位）、不可約（不能非平凡分解）、質（整除乘積就整除其一）——質一定不可約，但 $\mathbb{Z}[\sqrt{-3}]$ 的 $1+\sqrt{-3}$ 不可約卻不是質。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-08 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.6–4.7 整理。*
