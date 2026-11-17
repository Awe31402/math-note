---
course: Number Theory（2021 秋，線上錄影）
episode: 6
lecture: Lecture 6
date: 待補（2021 秋）
video: https://youtu.be/5NCjLzWh7gQ
notes: Jones & Jones 沒有多項式輾轉相除法的專節；第 1 章開頭（書頁 1，PDF 頁 16）提到同樣的整除理論對多項式也成立
---

# 第 6 集 · Lecture 6：多項式的輾轉相除法與 Bézout、分母有理化 [▶ 影片](https://youtu.be/5NCjLzWh7gQ)

← 上一集：[05-bezout-gcd-lcm-diophantine](05-bezout-gcd-lcm-diophantine.md) ｜ [總目錄](README.md) ｜ 下一集：[07-fundamental-theorem-of-arithmetic](07-fundamental-theorem-of-arithmetic.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 6 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（44:52，自動字幕）＋ Jones & Jones 第 1 章引言
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 多項式長除法與除法演算法](#1-多項式長除法與除法演算法)
- [2. 整除與因式定理](#2-整除與因式定理)
- [3. 代數基本定理與實係數分解](#3-代數基本定理與實係數分解)
- [4. 多項式的 gcd 與輾轉相除法](#4-多項式的-gcd-與輾轉相除法)
- [5. 應用：分母有理化](#5-應用分母有理化)
- [6. 另一條路：Galois 共軛](#6-另一條路galois-共軛)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】本集的目的：讓你看到**整數能做的很多事，多項式也能做**，而且類比驚人地整齊 [▶ 00:00](https://youtu.be/5NCjLzWh7gQ?t=0)。最後拿來解一個中學代數問題：把含立方根、五次方根的分母有理化。

| 整數 | 多項式 |
|---|---|
| 除法演算法 $a=qb+r$，$0\le r<\lvert b\rvert$ | $a(x)=q(x)b(x)+r(x)$，$\deg r<\deg b$ |
| $b\mid a$ | $b(x)\mid a(x)$ |
| 算術基本定理（質因數分解） | 代數基本定理（分解成一次式） |
| gcd、輾轉相除法、Bézout | 同（gcd 取首一） |

> 【課本補充】Jones & Jones 第 1 章引言（p. 1）：這章的整除定義、方法、定理對其他「能加減乘」的對象也成立，例如多項式、高斯整數、四元數；代數裡統稱為**環論**（ring theory）。課本沒有多項式輾轉相除法的專節。

---

## 1. 多項式長除法與除法演算法

### 1.1 長除法

[▶ 00:34](https://youtu.be/5NCjLzWh7gQ?t=34)

例：$x^5+3x^4+2x^2+8$ 除以 $x^2-2$。餘式的次數比除式小時就停。

以下是筆記依多項式長除法重算的結果：
$$x^5+3x^4+2x^2+8 = (x^2-2)(x^3+3x^2+2x+8) + (4x+24).$$
逐步：$x^3$ → 剩 $3x^4+2x^3+2x^2+8$；$3x^2$ → 剩 $2x^3+8x^2+8$；$2x$ → 剩 $8x^2+4x+8$；$8$ → 剩 $4x+24$。

⚠️ 待確認：字幕說商是「x cubed plus 3x squared plus 2x plus 12」，但照題目算，商的常數項是 8、餘式是 $4x+24$。可能是字幕聽錯或題目抄錯。

意義 [▶ 01:04](https://youtu.be/5NCjLzWh7gQ?t=64)：長除法把**假分式**（improper rational function，分子次數 ≥ 分母）寫成多項式加**真分式**（proper，分子次數 < 分母）：
$$\frac{x^5+3x^4+2x^2+8}{x^2-2} = x^3+3x^2+2x+8 + \frac{4x+24}{x^2-2}.$$
用數論的風格改寫成乘法形式：$a(x) = q(x)\,b(x) + r(x)$。

### 1.2 除法演算法

[▶ 01:37](https://youtu.be/5NCjLzWh7gQ?t=97)

**定理（多項式除法演算法）**：若 $\deg b\le\deg a$，則存在**唯一**的多項式 $q(x)$、$r(x)$ 使
$$a(x) = q(x)\,b(x) + r(x),\qquad \deg r<\deg b \text{ 或 } r=0.$$

（係數取在哪裡，字幕沒明說；例子都是有理係數。以下**不是逐字稿內容**：要能做長除法，係數要能除以 $b$ 的首項係數，所以通常取係數在一個體裡，如 $\mathbb{Q}$、$\mathbb{R}$、$\mathbb{C}$。）

**零多項式的次數** [▶ 02:08](https://youtu.be/5NCjLzWh7gQ?t=128)：次數是「最高的非零係數」的次方，零多項式沒有非零係數。各書定義不同：$-1$、$-\infty$、或不定義。講者選 $-\infty$（「最有震撼效果」）。不這樣約定的話，一些次數公式會壞掉。

**證明（存在）** [▶ 03:12](https://youtu.be/5NCjLzWh7gQ?t=192)：令
$$S = \{\,a(x) - b(x)g(x) : g(x) \text{ 是多項式}\,\}.$$
- 若 $0\in S$：$a = bg$，商是 $g$、餘式是 0。
- 否則令 $T$ = $S$ 中多項式的次數集合，是 $\mathbb{N}_0$ 的非空子集合。由**良序原理**，取次數最小的 $r(x) = a(x)-b(x)q(x)$。
- 證 $\deg r<\deg b$（反證）：設 $\deg r = n\ge m=\deg b$，首項係數分別是 $r_n$、$b_m$。令
$$\bar r(x) = r(x) - \frac{r_n}{b_m}\,x^{n-m}\,b(x).$$
因為 $n-m\ge0$，$x^{n-m}$ 是多項式；這樣剛好消掉 $r$ 的首項 $r_nx^n$，所以 $\deg\bar r\le n-1$。但 $\bar r = a - b\left(q + \tfrac{r_n}{b_m}x^{n-m}\right)\in S$，次數比 $r$ 還小，矛盾。

唯一性講者略過，說和整數的計算類似。

【口頭】
- 真正的演算法是長除法；這定理只是保證長除法一定有答案。
- 不期待考試重現這個證明，只是邏輯完整、讓你在學生好奇時能解釋。幾乎每本好的抽象代數書都有，例如 Gallian《Contemporary Abstract Algebra》（講者大學用書），不過這裡的證法不是從那本來的 [▶ 04:51](https://youtu.be/5NCjLzWh7gQ?t=291)。

---

## 2. 整除與因式定理

[▶ 07:31](https://youtu.be/5NCjLzWh7gQ?t=451)

【口頭】本集暗號是「surprising」。

**定義**：若 $b(x) = j(x)\,a(x)$（$j(x)$ 是多項式），就說 $a(x)$ **整除** $b(x)$，寫 $a(x)\mid b(x)$；$b(x)$ 是 $a(x)$ 的倍式，$a(x)$ 是 $b(x)$ 的**因式**（factor）。

**因式定理**（factor theorem）[▶ 08:03](https://youtu.be/5NCjLzWh7gQ?t=483)：
$$(x-c)\mid f(x) \iff f(c)=0.$$

**證明**：
- (⇒) $f(x) = (x-c)g(x)$，代 $x=c$ 得 $f(c)=0$。
- (⇐) 由除法演算法，$f(x) = q(x)(x-c)+r(x)$。除式是一次，所以 $r$ 是常數（可能是 0）。代 $x=c$：$f(c) = q(c)\cdot0 + r = r$。由假設 $f(c)=0$，所以 $r=0$，$f(x) = q(x)(x-c)$。∎

---

## 3. 代數基本定理與實係數分解

[▶ 09:45](https://youtu.be/5NCjLzWh7gQ?t=585)

整數有算術基本定理（質因數分解，第 7 集）；多項式的類比是：

**代數基本定理**：每個複係數多項式都可以在 $\mathbb{C}$ 上分解成一次因式的乘積。

**實係數多項式**：非實數的根成對出現（共軛：$z$ 是根則 $\bar z$ 也是）。所以實係數多項式可以分解成
- 實一次因式 $x-c$，和
- 實二次因式 $(x-\alpha)^2+\beta^2$（$\beta\neq0$，就是一對共軛根 $\alpha\pm\beta i$）

的乘積（都可能重複）。

【口頭】
- 用配方法（第 1 集）可以判斷一個二次式能不能在實數上分解：配完剩「$+$」不能、剩「$-$」可以 [▶ 11:21](https://youtu.be/5NCjLzWh7gQ?t=681)。
- 代數基本定理的證明超出本課。Gauss 約 1800 年給出證明（一生給了好幾個）。證明一定要用一點分析：用 Galois 理論的證明只需要中間值定理；複分析的證明代數少、分析多 [▶ 11:54](https://youtu.be/5NCjLzWh7gQ?t=714)。講者這學期也在教複分析。

**例 1** [▶ 12:26](https://youtu.be/5NCjLzWh7gQ?t=746)：實係數 $f(x)$ 有根 $-2+3i$，則 $-2-3i$ 也是根，所以
$$\big(x-(-2+3i)\big)\big(x-(-2-3i)\big) = (x+2)^2 - (3i)^2 = (x+2)^2+9 = x^2+4x+13$$
是 $f$ 的因式。這是**不可約二次式**（irreducible quadratic；有人叫「質」二次式，講者偏好「不可約」，意思是在你用的數系裡不能再分解）。

**例 2** [▶ 14:08](https://youtu.be/5NCjLzWh7gQ?t=848)：$f(x) = x^3+3x^2+9x-13$，已知 $f(-2+3i)=0$。由例 1，$x^2+4x+13$ 是因式；用長除法求另一個因式：
$$x^3+3x^2+9x-13 = (x-1)(x^2+4x+13),$$
餘式 0（是因式的話一定要是 0）。

**例 3** [▶ 15:51](https://youtu.be/5NCjLzWh7gQ?t=951)：同一個 $f$，注意 $f(1) = 1+3+9-13 = 0$，由因式定理 $(x-1)\mid f$；長除法得到同樣的分解。

【口頭】講者不喜歡只教**綜合除法**（synthetic division）：它不適合除以高次多項式，長除法是大家都該會的技能，應該放回課程裡 [▶ 15:18](https://youtu.be/5NCjLzWh7gQ?t=918)。重點：**除法可以用來分解因式**。

---

## 4. 多項式的 gcd 與輾轉相除法

### 4.1 定義與用分解求 gcd

[▶ 16:24](https://youtu.be/5NCjLzWh7gQ?t=984)

**定義**：$a(x)$、$b(x)$ 的**最大公因式** $\gcd(a,b)$ 是次數最高的**首一**（monic，首項係數為 1）公因式。要求首一，答案才唯一。

**例**（用分解）[▶ 16:58](https://youtu.be/5NCjLzWh7gQ?t=1018)：
$$b(x) = (x-1)(x+2)(x^2+1)(x-4),\qquad a(x) = (x-1)^2(x+3)(x^2+1)(x-4).$$
共同因式是 $x-1$、$x^2+1$、$x-4$，所以
$$\gcd(a,b) = (x-1)(x^2+1)(x-4) = x^4-5x^3+5x^2-5x+4.$$
（講者用 Wolfram Alpha 乘開，免得算錯。）

### 4.2 用除法求 gcd

[▶ 18:04](https://youtu.be/5NCjLzWh7gQ?t=1084)

**引理**：若 $a(x) = b(x)q(x)+r(x)$，則 $\gcd(a,b) = \gcd(b,r)$。（證明和整數一樣：兩對的公因式相同。）

**多項式輾轉相除法**：反覆做長除法，**最後一個非零餘式**（除以首項係數變成首一）就是 gcd。

**同一個例子**：$a(x)\div b(x)$ 只要一步，商是 $x$ [▶ 18:37](https://youtu.be/5NCjLzWh7gQ?t=1117)：
$$a(x) - x\,b(x) = -3x^4+15x^3-15x^2+15x-12.$$
除以 $-3$ 變成首一：$x^4-5x^3+5x^2-5x+4$，和 4.1 的答案一樣。

（以下**不是逐字稿內容**，是依分解驗證的：$a = g\cdot(x-1)(x+3)$、$b = g\cdot(x+2)$，其中 $g$ 是 gcd；$(x-1)(x+3) = x(x+2)-3$，所以 $a - xb = -3g$，再除一次 $b\div(-3g)$ 餘式就是 0。）

【口頭】你可以完全分解再找共同因式，也可以用除法——或者用 Bill Cook 的網站偷懶 [▶ 19:43](https://youtu.be/5NCjLzWh7gQ?t=1183)。

### 4.3 例：$\gcd(x^7+3x+2,\ x^2-1)$ 與 Bézout

[▶ 20:20](https://youtu.be/5NCjLzWh7gQ?t=1220)

記 $A = x^7+3x+2$、$B = x^2-1$。

**第一步**：
$$x^7+3x+2 = (x^2-1)(x^5+x^3+x) + (4x+2).$$

**第二步**：
$$x^2-1 = (4x+2)\left(\tfrac14x-\tfrac18\right) - \tfrac34.$$
（檢查：$(4x+2)\left(\tfrac14x-\tfrac18\right) = x^2-\tfrac14$，所以餘式是 $-1+\tfrac14 = -\tfrac34$。）

餘式是非零常數，下一步餘式就是 0。非零常數除以自己變成首一就是 1，所以 $\gcd(A,B) = 1$。

⚠️ 逐字稿缺字：[▶ 20:55](https://youtu.be/5NCjLzWh7gQ?t=1255) 字幕先說「remainder is four x minus two」，後面都用 $4x+2$；照計算是 $4x+2$。

**反推得 Bézout** [▶ 22:37](https://youtu.be/5NCjLzWh7gQ?t=1357)：第二式乘 $-\tfrac43$：
$$1 = -\tfrac43(x^2-1) + (4x+2)\left(\tfrac13x-\tfrac16\right).$$
把第一式的 $4x+2 = A - B(x^5+x^3+x)$ 代入：
$$1 = \left(\tfrac13x-\tfrac16\right)A + \left[-\tfrac43 - \left(\tfrac13x-\tfrac16\right)(x^5+x^3+x)\right]B.$$
這就是多項式版的 **Bézout**：gcd 是 $A,B$ 的**多項式**線性組合 $u(x)A+v(x)B$。

（最後一行是筆記依講者的代入步驟整理的；講者在螢幕上一邊代一邊說「我很不會倒著代」。可以用 $x=\pm1$ 檢查：$B=0$，$A(1)=6$、$u(1)=\tfrac16$；$A(-1)=-2$、$u(-1)=-\tfrac12$；兩者乘積都是 1。）

【口頭】Bill Cook 網站上有「Euclidean algorithm for polynomials」，會列出除法步驟、gcd 和 Bézout 係數，講者用它對答案。**不建議不用工具做這種計算** [▶ 25:55](https://youtu.be/5NCjLzWh7gQ?t=1555)。

---

## 5. 應用：分母有理化

### 5.1 平方根：共軛

[▶ 26:27](https://youtu.be/5NCjLzWh7gQ?t=1587)

$$\frac{1}{2+\sqrt3} = \frac{2-\sqrt3}{(2+\sqrt3)(2-\sqrt3)} = \frac{2-\sqrt3}{4-3} = 2-\sqrt3.$$
計算機檢查：兩邊都是 $0.2679\ldots$。

### 5.2 立方根：共軛沒用

[▶ 28:12](https://youtu.be/5NCjLzWh7gQ?t=1692)

對 $\dfrac{1}{2+\sqrt[3]3}$ 乘 $\dfrac{2-\sqrt[3]3}{2-\sqrt[3]3}$，分母是 $4-\sqrt[3]9$，**立方根消不掉**。

【口頭】講者第一次被問到時也以為乘共軛就好，「這是有一點數學自信的人都會說的答案，但那自信沒有根據」；引用他社區大學老師的話：「這隻狗不會打獵」（this dog does not hunt）[▶ 28:45](https://youtu.be/5NCjLzWh7gQ?t=1725)。亞洲的數學書把這種根式叫 surd（不盡根）。

### 5.3 多項式方法

[▶ 29:21](https://youtu.be/5NCjLzWh7gQ?t=1761)

**在解什麼**：把 $\dfrac{1}{g(\alpha)}$（$\alpha$ 是某個根式）寫成分母沒有根式的形式。

**步驟**：
1. 找一個以 $\alpha$ 為根的多項式 $m(x)$（例如 $\alpha=\sqrt[3]3$ 用 $x^3-3$）。
2. 把分母寫成多項式 $g(x)$（例如 $2+x$）。
3. 用輾轉相除法／Bézout 找 $u(x)m(x) + v(x)g(x) = c$（$c$ 是非零常數；$m,g$ 的 gcd 是 1 才行）。
4. 代 $x=\alpha$：$m(\alpha)=0$，剩 $v(\alpha)g(\alpha) = c$，所以 $\dfrac1{g(\alpha)} = \dfrac{v(\alpha)}{c}$。

**例 1**：$\dfrac{1}{2+\sqrt[3]3}$ [▶ 29:56](https://youtu.be/5NCjLzWh7gQ?t=1796)

$x^3-3$ 除以 $x+2$：
$$x^3-3 = (x+2)(x^2-2x+4) - 11.$$
（因為 $(x+2)(x^2-2x+4) = x^3+8$。）代 $x=\sqrt[3]3$，左邊是 0：
$$11 = (2+\sqrt[3]3)\left(\sqrt[3]9-2\sqrt[3]3+4\right),$$
$$\frac{1}{2+\sqrt[3]3} = \frac{4-2\sqrt[3]3+\sqrt[3]9}{11}.$$

**例 2**：$\dfrac{\sqrt[5]2}{3-6\sqrt[5]2}$ [▶ 31:34](https://youtu.be/5NCjLzWh7gQ?t=1894)

- 多項式：$x^5-2$（$\sqrt[5]2$ 是根）；分母：$3-6x$。$\gcd(x^5-2,\,3-6x)=1$。
- 由 Bill Cook 網站，$x^5-2$ 的 Bézout 係數是 $-\tfrac{32}{63}$（另一個係數字幕沒唸）。代 $x=\sqrt[5]2$ 後 $x^5-2$ 那項消失，得到
$$\frac{1}{3-6\sqrt[5]2} = -\frac{1+2\sqrt[5]2+4\sqrt[5]4+8\sqrt[5]8+16\sqrt[5]{16}}{189}.$$

（以下**不是逐字稿內容**，是筆記用另一種方法驗證上式：令 $x=\sqrt[5]2$，$3-6x = 3(1-2x)$，而 $1-(2x)^5 = (1-2x)(1+2x+4x^2+8x^3+16x^4)$，$(2x)^5 = 32\cdot2 = 64$，所以 $(1-2x)(1+2x+\cdots+16x^4) = -63$，除以 $3\cdot(-63) = -189$ 即得。）

- 分子的 $\sqrt[5]2$ 本來就在該在的地方，先不管，最後再乘回去 [▶ 33:44](https://youtu.be/5NCjLzWh7gQ?t=2024)：
$$\sqrt[5]2\cdot(1+2\sqrt[5]2+4\sqrt[5]4+8\sqrt[5]8+16\sqrt[5]{16}) = 32 + \sqrt[5]2 + 2\sqrt[5]4 + 4\sqrt[5]8 + 8\sqrt[5]{16},$$
因為 $\sqrt[5]{16}\cdot\sqrt[5]2 = \sqrt[5]{32} = 2$。所以
$$\frac{\sqrt[5]2}{3-6\sqrt[5]2} = -\frac{32+\sqrt[5]2+2\sqrt[5]4+4\sqrt[5]8+8\sqrt[5]{16}}{189}.$$

【口頭】
- 如果你懷疑 Bill 的網站有病毒（「如果你開始懷疑我哥哥有什麼邪惡企圖」），也可以直接長除法，不難 [▶ 32:39](https://youtu.be/5NCjLzWh7gQ?t=1959)。
- 講者教過幾千個學生，只遇過大約三個能不靠理論做出這種題目。這可以當作練習長除法的有趣實驗課 [▶ 35:29](https://youtu.be/5NCjLzWh7gQ?t=2129)。

---

## 6. 另一條路：Galois 共軛

### 6.1 歷史

[▶ 36:02](https://youtu.be/5NCjLzWh7gQ?t=2162)

【口頭】
- 古人解出二次方程；14、15 世紀左右三次方程的解法出現，不久四次也解出來。
- 大家花了巨大努力想用根式解五次方程，失敗了。
- 1800 年代初，數學界漸漸明白五次方程沒有類似公式。大多數人認為 Abel 第一個證明。
- 約十年後（約 1830 年），Galois 創立 **Galois 理論**：說明哪些五次方程能用根式解、哪些不能。這也是**近代群論**的誕生。Galois 死於決鬥，講者記得是 19 或 21 歲。
- 群論的另一個來源是對稱性的研究。Galois 理論在一般抽象代數書的後面都有一章（例如 Gallian 第 32 章），但真的要學要一整門課 [▶ 38:48](https://youtu.be/5NCjLzWh7gQ?t=2328)。

### 6.2 共軛與範數

[▶ 39:22](https://youtu.be/5NCjLzWh7gQ?t=2362)

**複數共軛**是第一個 **Galois 共軛**的例子：
$$\frac1z = \frac{\bar z}{z\bar z} = \frac{x-iy}{x^2+y^2}.$$
乘共軛讓分母變實數；5.1 的 $2\pm\sqrt3$ 也是同樣的道理。

**$\mathbb{Q}(\sqrt2,\sqrt3)$** [▶ 40:31](https://youtu.be/5NCjLzWh7gQ?t=2431)：$x^2-2$ 和 $x^2-3$ 的**分裂體**（splitting field，讓它們完全分解的最小數系），元素形如
$$a+b\sqrt2+c\sqrt3+d\sqrt6,\qquad a,b,c,d\in\mathbb{Q}.$$
有四個 Galois 共軛（這個體的**自同構** automorphism，保持加法乘法的一對一對應）：

| 共軛 | $\sqrt2\mapsto$ | $\sqrt3\mapsto$ | $\sqrt6\mapsto$ |
|---|---|---|---|
| $\varepsilon$（什麼都不做） | $\sqrt2$ | $\sqrt3$ | $\sqrt6$ |
| $\alpha$ | $-\sqrt2$ | $\sqrt3$ | $-\sqrt6$ |
| $\beta$ | $\sqrt2$ | $-\sqrt3$ | $-\sqrt6$ |
| $\alpha\beta$ | $-\sqrt2$ | $-\sqrt3$ | $\sqrt6$ |

（$\sqrt6=\sqrt2\sqrt3$，所以翻 $\sqrt2$ 或 $\sqrt3$ 的號，$\sqrt6$ 也跟著翻。）

**範數**（norm）：$N(x) = \varepsilon(x)\,\alpha(x)\,\beta(x)\,\alpha\beta(x)$。四個乘起來**沒有根式**，是 $a,b,c,d$ 的四次式；講者用 Wolfram Alpha 算出來，並懷疑他抄的式子有一項 $b$ 的次方抄錯，應是 $b^4$ [▶ 42:10](https://youtu.be/5NCjLzWh7gQ?t=2530)。

**有理化** [▶ 43:14](https://youtu.be/5NCjLzWh7gQ?t=2594)：
$$\frac1x = \frac{\alpha(x)\,\beta(x)\,\alpha\beta(x)}{\varepsilon(x)\,\alpha(x)\,\beta(x)\,\alpha\beta(x)} = \frac{\alpha(x)\,\beta(x)\,\alpha\beta(x)}{N(x)}.$$
分母是有理數。講者的例子裡 $N(x)=4$，但 $x$ 的具體數字和範數公式字幕沒唸出，待補。

【口頭】這絕對不是教高中生的方法；講者覺得多項式方法比較好玩。這只是娛樂性的數學，不會考 [▶ 43:47](https://youtu.be/5NCjLzWh7gQ?t=2627)。

---

## 7. 一頁速查表

**多項式除法演算法**：$\deg b\le\deg a$ ⇒ 唯一 $q,r$，$a=qb+r$，$\deg r<\deg b$ 或 $r=0$。
- 關鍵：$S=\{a-bg\}$ 中取最低次 $r$；若 $\deg r\ge\deg b$，$\bar r = r-\frac{r_n}{b_m}x^{n-m}b$ 次數更低，矛盾。
- 約定 $\deg 0 = -\infty$。

**因式定理**：$(x-c)\mid f \iff f(c)=0$。關鍵：$f = q(x-c)+r$，$r=f(c)$。

**實係數分解**：一次 $x-c$ 和不可約二次 $(x-\alpha)^2+\beta^2$ 的乘積。根 $-2+3i$ ⇒ 因式 $x^2+4x+13$。

**gcd**：首一的最高次公因式。$\gcd(a,b)=\gcd(b,r)$；最後非零餘式（化成首一）就是 gcd。Bézout：$\gcd = u(x)a+v(x)b$。

**分母有理化**
1. $\alpha$ 的多項式 $m(x)$；分母 $g(x)$。
2. 求 $u\,m+v\,g = c$（非零常數）。
3. 代 $\alpha$：$\dfrac1{g(\alpha)} = \dfrac{v(\alpha)}c$。
- $x^3-3 = (x+2)(x^2-2x+4)-11$ ⇒ $\dfrac1{2+\sqrt[3]3} = \dfrac{4-2\sqrt[3]3+\sqrt[3]9}{11}$。
- $\dfrac1{3-6\sqrt[5]2} = -\dfrac{\sum_{k=0}^4 2^k\,2^{k/5}}{189}$（關鍵：$1-(2x)^5 = (1-2x)\sum (2x)^k$，$(2x)^5=64$）。

**Galois 共軛**：$\mathbb{Q}(\sqrt2,\sqrt3)$ 有 4 個（翻 $\sqrt2$、翻 $\sqrt3$ 的號）；$1/x = (\text{其他三個共軛之積})/N(x)$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 整數與多項式的類比 | 第 7 集（算術基本定理 ↔ 代數基本定理） |
| 因式定理、多項式的根 | 第 11 集（多項式的整數根）、第 13 集（多項式同餘、Lagrange 定理） |
| 複數共軛、不可約二次式 | 第 19 集（複數）、第 21–22 集（高斯整數、範數） |
| Galois 理論、三次方程的歷史 | 第 20 集（三次方程的解） |

---

## 附：本集一句話總結

> **多項式和整數一樣有除法演算法、因式、gcd、輾轉相除法和 Bézout（gcd 取首一）；利用 $u(x)m(x)+v(x)g(x)=c$ 再代入根式 $\alpha$（$m(\alpha)=0$），就能把乘共軛做不到的立方根、五次方根分母有理化。**

---

## ⚠️ 待確認清單

1. [▶ 00:34](https://youtu.be/5NCjLzWh7gQ?t=34) 長除法例子：字幕說商是 $x^3+3x^2+2x+12$，筆記照題目重算得商 $x^3+3x^2+2x+8$、餘式 $4x+24$，兩者不一致。
2. [▶ 43:14](https://youtu.be/5NCjLzWh7gQ?t=2594) Galois 共軛有理化的具體例子（$x$ 是哪個數、範數公式）字幕沒唸出，待補。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 6 錄影逐字稿（YouTube 自動字幕，44:52）與 Jones & Jones《Elementary Number Theory》第 1 章引言整理。*
