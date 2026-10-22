---
course: Abstract Algebra I (Fall 2016)
episode: 45
lecture: L29
date: 2016-11-14
video: https://www.youtube.com/watch?v=ry6f4PHRYMM
notes: AlgebraInotes_2018.pdf §4.7–4.8（p.155–164）
---

# 第 45 集 · L29：不可約與質元、歐氏整環、PID、UFD [▶ 影片](https://www.youtube.com/watch?v=ry6f4PHRYMM&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[44-L28-整除與分解]] ｜ [總目錄](../README.md) ｜ 下一集：[[46-答疑課]] →

> **課程**：Abstract Algebra I（Liberty University，Fall 2016）— 第 45 集，Lecture 29
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（52:48，自動字幕）＋ 講義 `AlgebraInotes_2018.pdf` §4.7 尾與 §4.8「Lecture 28: divisibility in integral domains II」（p.157–164）＋ Gallian 第 18 章。前半黑板，後半投影。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 7 在 ℤ[√5] 中不可約](#1-7-在-ℤ5-中不可約)
- [2. 整環中：質元 ⇒ 不可約](#2-整環中質元--不可約)
- [3. 相伴元與主理想的生成元](#3-相伴元與主理想的生成元)
- [4. PID 中：質元 ⟺ 不可約](#4-pid-中質元--不可約)
- [5. 歐氏整環](#5-歐氏整環)
  - [5.1 定義](#51-定義)
  - [5.2 ℤ：除法算則不唯一](#52-ℤ除法算則不唯一)
  - [5.3 F[x]：非乘性的範數](#53-fx非乘性的範數)
  - [5.4 高斯整數：幾何的除法算則](#54-高斯整數幾何的除法算則)
  - [5.5 在 ℤ[i] 做輾轉相除](#55-在-ℤi-做輾轉相除)
- [6. 互極大理想](#6-互極大理想)
- [7. Fermat 最後定理與 Lamé 的錯誤](#7-fermat-最後定理與-lamé-的錯誤)
- [8. 唯一分解整環 UFD](#8-唯一分解整環-ufd)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/ry6f4PHRYMM?t=0) 課前禱告。「上次開始走 Gallian 第 18 章，從例子接著。」

---

## 1. 7 在 ℤ[√5] 中不可約

[▶ 00:30](https://youtu.be/ry6f4PHRYMM?t=30)（講義 Ex 4.7.7）$\mathbb{Z}[\sqrt5] = \{a+b\sqrt5 : a,b\in\mathbb{Z}\}$。

設 $7 = xy$。範數乘性：
$$49 = N(7) = N(x)N(y).$$
$x,y$ 都不是單位 ⇒ $N(x) = N(y) = 7$ [▶ 01:30](https://youtu.be/ry6f4PHRYMM?t=90) ⇒ 要 $|a^2-5b^2| = 7$，即 $a^2-5b^2 = \pm7$。

**模 7**[▶ 02:30](https://youtu.be/ry6f4PHRYMM?t=150)：「這個整數方程想起來很煩，但**模 7 看**有成果得多。」整數解一定也是模 7 的解：
$$a^2-5b^2\equiv0\ (\mathrm{mod}\ 7).$$
- 「我不給你們看逐一檢查。$a,b$ 各 7 種，原則上 49 種情況。但利用它們是**平方**可以再減——1 和 6 模 7 平方一樣（6 是 $-1$）。」
- 結論：$a\equiv b\equiv0\ (\mathrm{mod}\ 7)$ [▶ 03:30](https://youtu.be/ry6f4PHRYMM?t=210)。

> 💬 補充：模 7 的平方是 $\{0,1,2,4\}$；$5b^2$ 的值是 $\{0,5,3,6\}$。只有 0 相同，所以 $a\equiv b\equiv0$。

- 那麼 $7\mid a$、$7\mid b$ [▶ 04:30](https://youtu.be/ry6f4PHRYMM?t=270) ⇒ $49\mid a^2$、$49\mid b^2$ ⇒ $49\mid a^2-5b^2$ ⇒ $49\mid N(x) = 7$。不可能。
- 所以 $x$ 或 $y$ 是單位 ⇒ **7 在 $\mathbb{Z}[\sqrt5]$ 中不可約**。

---

## 2. 整環中：質元 ⇒ 不可約

> **定理**（講義 Thm 4.7.8）[▶ 06:00](https://youtu.be/ry6f4PHRYMM?t=360)　整環中，每個質元都不可約。

（「這支筆沒水了。我得多練習。」）

**證明**[▶ 06:30](https://youtu.be/ry6f4PHRYMM?t=390)：$a$ 是質元，$a = xy$。目標：$x$ 或 $y$ 是單位。
- 質元 ⇒ $a\mid x$ 或 $a\mid y$。
- 設 $a\mid x$：$x = ab$ [▶ 08:00](https://youtu.be/ry6f4PHRYMM?t=480)。
- 寫一個平凡的式子：$x\cdot1 = x = ab = (xy)b = x(yb)$（結合律）。
- $a\neq0$（質元的定義）⇒ $x\neq0$（否則 $a = 0\cdot y = 0$）[▶ 09:00](https://youtu.be/ry6f4PHRYMM?t=540)。
- 整環的**消去律** ⇒ $1 = yb$ ⇒ **$y$ 是單位**。
- 同理 $a\mid y$ ⇒ $x$ 是單位。$\blacksquare$

---

## 3. 相伴元與主理想的生成元

> **定理**（講義 Thm 4.7.9）[▶ 10:30](https://youtu.be/ry6f4PHRYMM?t=630)
> 1. $R$ 有單位元的交換環：$a,b$ 相伴 ⇒ $\langle a\rangle = \langle b\rangle$。
> 2. $R$ 整環：$\langle a\rangle = \langle b\rangle$ ⇒ $a,b$ 相伴。

【口頭】[▶ 12:00](https://youtu.be/ry6f4PHRYMM?t=720)「在整環裡，要找一個主理想的**所有生成元**，只要看某個生成元的**相伴元**。這在整環之外不成立，但反例**相當複雜**。我跟 **Bill** 聊過，他認為大概得是**無限**的例子——有限環裡大概找不到。」

**(1) 證明**[▶ 12:30](https://youtu.be/ry6f4PHRYMM?t=750)：$a = bu$，$uu' = 1$。
- $\langle a\rangle = \{ra\} = \{rbu\} = \{b(ru)\}$。
- 它含 $b$（取 $r = u'$）；包含 $b$ 的最小理想是 $\langle b\rangle$ ⇒ $\langle b\rangle\subseteq\langle a\rangle$。
- 【口頭】[▶ 15:00](https://youtu.be/ry6f4PHRYMM?t=900)「怎麼論證……$r$ 任意，所以 $ru$ 可以打到環裡任何東西。我不講了，講義有**稍微好一點**的論證。」

**(2) 證明**[▶ 15:30](https://youtu.be/ry6f4PHRYMM?t=930)：$\langle a\rangle = \langle b\rangle$。
- $a\in\langle b\rangle$ ⇒ $a = br$；$b\in\langle a\rangle$ ⇒ $b = ar'$。
- 代入：$a = br = a(r'r)$ [▶ 16:30](https://youtu.be/ry6f4PHRYMM?t=990)。
- $a = 0$ ⇒ $b = 0$，相伴。$a\neq0$ ⇒ 消去：$r'r = 1$ ⇒ $r$ 是單位 ⇒ $a = br$ 相伴。$\blacksquare$

【口頭】[▶ 22:30](https://youtu.be/ry6f4PHRYMM?t=1350)「這個定理 **Gallian 沒有**，是我加的。似乎很重要——至少對作業：有些題要你從一個生成元找主理想之類的。知道不同生成元之間的關係很好。」

---

## 4. PID 中：質元 ⟺ 不可約

> **定理**（講義 Thm 4.7.10）[▶ 17:30](https://youtu.be/ry6f4PHRYMM?t=1050)　PID 中，元素是質元 $\iff$ 它不可約。

**證明**：PID 是整環 ⇒ 質元 ⇒ 不可約（§2）。

**(不可約 ⇒ 質元)**[▶ 19:30](https://youtu.be/ry6f4PHRYMM?t=1170)：$a$ 不可約，設 $a\mid bc$。
1. **造理想**[▶ 20:00](https://youtu.be/ry6f4PHRYMM?t=1200)：「證明很妙。」
$$I = \{ax+by : x,y\in D\}.$$
   「不難看出它是理想：差還是這種東西，也有超級封閉。講義有明確證明。」
2. PID ⇒ $I = \langle d\rangle$ [▶ 21:00](https://youtu.be/ry6f4PHRYMM?t=1260)。
3. $a = a\cdot1+b\cdot0\in I$ ⇒ $a = rd$。
4. $a$ 不可約 ⇒ $r$ 或 $d$ 是單位 [▶ 22:00](https://youtu.be/ry6f4PHRYMM?t=1320)。

**情況 1：$d$ 是單位**[▶ 23:00](https://youtu.be/ry6f4PHRYMM?t=1380)
- $1 = dd'\in I$ ⇒ $1 = ax+by$。
- 乘 $c$：$c = acx+bcy$。
- $a\mid acx$ 顯然；$a\mid bc$（假設）⇒ $a\mid c$ [▶ 24:30](https://youtu.be/ry6f4PHRYMM?t=1470)。✓

**情況 2：$r$ 是單位**[▶ 25:30](https://youtu.be/ry6f4PHRYMM?t=1530)
- $a = rd$ ⇒ $a$ 和 $d$ 相伴。（老師一度說成「$a$ 和 $r$」，學生糾正：「是 $d$。」「我是白痴。**D 代表 done**。」）
- §3 ⇒ $I = \langle d\rangle = \langle a\rangle$。
- $b = a\cdot0+b\cdot1\in I = \langle a\rangle$ ⇒ $a\mid b$ [▶ 27:00](https://youtu.be/ry6f4PHRYMM?t=1620)。✓

「不管哪種，我們都贏。」$\blacksquare$

【口頭】[▶ 29:30](https://youtu.be/ry6f4PHRYMM?t=1770)「PID 的好處是**混淆**不可約和質元——沒有區別。（當然**定義**上有區別：不可約是關於**分解**，質元是關於**整除**。）——Bradley 不在？Hugerworth 的評論……Bradley，希望你生病了——不對，我不該希望那樣。」

---

## 5. 歐氏整環

（換投影：「我花了幾分鐘把剩下章節的定義和定理都放進去了，還沒加例子和證明——剩下兩講的**骨架**已經在這裡了。」中間老師告訴兩位同學代數拓撲課的選課狀況。）

### 5.1 定義

> **定義（歐氏整環 Euclidean domain, ED）**（講義 Def 4.8.1）[▶ 30:30](https://youtu.be/ry6f4PHRYMM?t=1830)　整環 $D$，有**範數** $N:D\to\mathbb{N}\cup\{0\}$，而且有**除法算則**：對任何 $a$ 和 $b\neq0$，存在 $q,r$ 使
> $$a = qb+r,\quad r = 0\ \text{或}\ N(r)<N(b).$$

- 【口頭】「這跟 Gallian 的有點不同。如果你比較喜歡 Gallian 的定義，引用它也可以——我很確定它們等價。」
- Gallian 用「量度」$d$，條件 $d(a)\le d(ab)$ [▶ 31:30](https://youtu.be/ry6f4PHRYMM?t=1890)。若範數**乘性**，$N(a) = N(ab)/N(b)\le N(ab)$（$N(b)\ge1$），自動成立。
- 【口頭】[▶ 32:00](https://youtu.be/ry6f4PHRYMM?t=1920)「別弄得太抽象。真的就**三個例子**：整數、代數整數（$\mathbb{Z}[\sqrt d]$ 之類）、多項式。」
  - 整數：絕對值。$\mathbb{Z}[\sqrt d]$：$|a^2-db^2|$。多項式：次數。
  - Dummit & Foote 提到：任何體都是 ED，範數定成 0。「好吧，但沒什麼用。」

### 5.2 ℤ：除法算則不唯一

[▶ 33:30](https://youtu.be/ry6f4PHRYMM?t=2010)（講義 Ex 4.8.2）$N(x) = |x|$，乘性。單位 = 範數 1 = $\pm1$。

「這個歧義帶來除法算則裡一個你們可能沒想過的歧義：**餘數該是正的還是負的？**你們被灌輸要選正的。從抽象代數的觀點，那只是**特設的**選擇。」

$$54 = 6\cdot8+6 = 7\cdot8-2.$$
- （投影上原本是 50，老師改成 54 但沒改完 [▶ 34:30](https://youtu.be/ry6f4PHRYMM?t=2070)：「我試著用**意念**改它。經上說凡事都能——我的信心**不如芥菜種**。我想就算我能把 0 變成 4，也不太能榮耀基督吧。這是你們的**聖經整合**。」）
- （「$7\cdot8 = 56$——有些孩子……不夠多孩子。也許你們能改變這點。去學校工作，或嫁娶聰明人，你們選。」）
- ED 定義**兩種餘數都允許**，所以除法算則不唯一。
- 【口頭】[▶ 35:30](https://youtu.be/ry6f4PHRYMM?t=2130)「其實 $7\cdot8$ 比 $6\cdot8$ **更接近** 54。某種意義上，負的餘數是**更好**的餘數。」

### 5.3 F[x]：非乘性的範數

[▶ 36:00](https://youtu.be/ry6f4PHRYMM?t=2160)（講義 Ex 4.8.3）$N(f) = \deg f$。
- **不是乘性的**：$\deg(fg) = \deg f+\deg g$（是加的）。
- 單位是**非零常數**（0 次），不是「範數 1」的。「所以不能總是假設範數 1 給你單位——**乘性範數**才對。」
- 「還有其他非乘性範數的例子嗎？我沒有。放心。」

### 5.4 高斯整數：幾何的除法算則

[▶ 37:00](https://youtu.be/ry6f4PHRYMM?t=2220)（講義 Ex 4.8.4）$N(a+bi) = a^2+b^2$——到原點距離的平方（模的平方）。

「特別漂亮的例子：可以用複平面上**真正的幾何距離**來分析範數。」乘性來自複共軛的性質。**不顯然**的是除法算則：給 $a+bi$、$c+di$，要找高斯整數 $q$ 使餘數範數夠小。

**證明（幾何）**[▶ 38:00](https://youtu.be/ry6f4PHRYMM?t=2280)
1. 把它們當**複數**相除：$z = \dfrac{a+bi}{c+di}$，是複平面上一個點（座標有理數）。
2. 高斯整數是**格點**。取離 $z$ **最近**的格點當 $q$。
3. 最糟的情況：$z$ 在格子正中央，到四角的距離 $\sqrt{(1/2)^2+(1/2)^2} = 1/\sqrt2$ [▶ 39:30](https://youtu.be/ry6f4PHRYMM?t=2370)。所以 $|z-q|\le1/\sqrt2$。
   - （學生指出投影上漏了一個 1——「我用**白色**寫的。」）
4. 定義 $r = (a+bi)-q(c+di)$ [▶ 41:00](https://youtu.be/ry6f4PHRYMM?t=2460)。則
$$\frac{r}{c+di} = z-q\ ⇒\ |r|\le\frac{|c+di|}{\sqrt2}\ ⇒\ N(r)\le\frac{N(c+di)}{2}<N(c+di).\ \blacksquare$$

【課堂討論】[▶ 41:30](https://youtu.be/ry6f4PHRYMM?t=2490)「如果 $z = 3.7+4.9i$，你選哪個 $q$？」學生：「$4+5i$。」「很好，你們懂了。」

### 5.5 在 ℤ[i] 做輾轉相除

[▶ 42:30](https://youtu.be/ry6f4PHRYMM?t=2550)（講義 Ex 4.8.5）「『用數字？不會吧！』——是的，用數字。」

$\alpha = 11+3i$、$\beta = 2+3i$（「大部分人會寫 $2+3i$——我怎麼了？我知道很多事，這是其中之一」）。

1. $\alpha = (2-2i)\beta+(1+i)$ [▶ 44:30](https://youtu.be/ry6f4PHRYMM?t=2670)。「$2-2i$ 從哪來？**我完全不知道**，好一陣子沒做了。」驗算：$(2-2i)(2+3i) = 4+6i-4i+6 = 10+2i$；和 $11+3i$ 實部虛部各差 1，比 $2+3i$ 小。「這是 $\beta$ 的複數倍數能到的最接近了。」
   - 「這要一點**計算**。你可以直接做複數除法，從有理形式找該選什麼——就像用計算機找餘數：除、減掉整數部分、乘回去。或者有個好計算機直接告訴你。」
2. $\beta = (3+i)(1+i)+(-i)$ [▶ 46:00](https://youtu.be/ry6f4PHRYMM?t=2760)。
3. 餘數 $-i$ 是**單位**。整理成 $\alpha,\beta$ 的組合，乘 $i$ 得 $1 = (\cdots)\alpha+(\cdots)\beta$——「**Bézout 定理的類比**：$\alpha,\beta$ 的複線性組合給出 1。看起來有點神秘，但跟你們做過的沒什麼不同。」

---

## 6. 互極大理想

[▶ 47:00](https://youtu.be/ry6f4PHRYMM?t=2820)
- **互極大（comaximal）**：兩個理想相加是整個環。
- 類比**互質**：$\gcd(3,5) = 1$，由 Bézout 能把 1 寫成 3、5 的組合，所以 $\langle3\rangle+\langle5\rangle = \mathbb{Z}$。
- 「這個故事在更抽象的脈絡裡也成立：互極大理想扮演互質整數的角色。」

---

## 7. Fermat 最後定理與 Lamé 的錯誤

[▶ 48:00](https://youtu.be/ry6f4PHRYMM?t=2880)
- **Fermat 最後定理**：$n\ge3$ 時 $x^n+y^n = z^n$ 沒有正整數解。
- 特定的 $n$ 可以用特殊論證：例如 $x^3+y^3 = z^3$ 可在 $\mathbb{Z}[\sqrt{-3}]$ 之類的環裡證——「John Stillwell《Elements of Number Theory》裡有三頁血淋淋的計算。」Euler、Legendre 這些人這樣一個個擊破。
- **Gabriel Lamé**[▶ 49:00](https://youtu.be/ry6f4PHRYMM?t=2940)（「法國人，我念不對」）給了一個**錯誤證明**：用類似的環，但**假設了唯一分解**——那不成立。

**反例**（$\mathbb{Z}[\sqrt{-5}]$）[▶ 49:30](https://youtu.be/ry6f4PHRYMM?t=2970)
$$46 = 2\cdot23 = (1+3\sqrt{-5})(1-3\sqrt{-5}).$$
- 這些因數**都不可約**，而且 2、23 和右邊的因數**不相伴**。
- 違反唯一分解 ⇒ Lamé 的論證是錯的。「最有名的錯誤嘗試之一。」
- **Kummer** 其實在 Lamé 之前就指出這種分解歧義的危險，提出「**理想數（ideal numbers）**」；後來 **Dedekind** 把 Kummer 的工作「把 t 畫上橫、i 點上點」，和其他人一起證明了 Fermat 最後定理的**很多很多**情況 [▶ 51:30](https://youtu.be/ry6f4PHRYMM?t=3090)。
- 「Fermat 最後定理最終不是用這些證的，而是用**近來複雜得多**的東西。」

> 📘 筆記補充：$N(1\pm3\sqrt{-5}) = 1+45 = 46$，$N(2) = 4$，$N(23) = 529$。$a^2+5b^2 = 2$ 或 $23$ 無整數解，所以這四個都不可約。

---

## 8. 唯一分解整環 UFD

> **定義（唯一分解整環 unique factorization domain, UFD）**（講義 Def 4.8.6）[▶ 52:00](https://youtu.be/ry6f4PHRYMM?t=3120)　整環 $D$，每個非零非單位元素
> 1. 都能寫成**不可約元的乘積**；
> 2. 兩種這樣的分解，在**順序**和**相伴**的差別下相同。

「時間到了——等等，我們**幾乎**到了。」

> 📘 講義接下來（下次講）：PID 的升鏈條件（Thm 4.8.7）；**PID ⇒ UFD**（Thm 4.8.8）；$F[x]$ 是 UFD（Cor 4.8.9）；**ED ⇒ PID**（Thm 4.8.10）；ED ⇒ UFD（Cor 4.8.11）。

---

## 9. 一頁速查表

### 9.1 主要定理

| 定理 | 環 | 證明關鍵一步 |
|---|---|---|
| 質元 ⇒ 不可約 | 整環 | $x = x(yb)$，消去 ⇒ $yb = 1$ |
| 相伴 ⇒ $\langle a\rangle = \langle b\rangle$ | 交換有 1 | $\langle a\rangle\ni b$ |
| $\langle a\rangle = \langle b\rangle$ ⇒ 相伴 | 整環 | $a = a(r'r)$，消去 |
| 不可約 ⇒ 質元 | PID | $I = \langle a,b\rangle = \langle d\rangle$；$d$ 或 $r$ 是單位 |
| $\mathbb{Z}[i]$ 是 ED | — | 最近的格點，$\lvert z-q\rvert\le1/\sqrt2$ |

### 9.2 歐氏整環的三個例子

| 環 | 範數 | 乘性 | 單位 |
|---|---|---|---|
| $\mathbb{Z}$ | $\lvert x\rvert$ | ✓ | $\pm1$ |
| $F[x]$ | $\deg$ | ✗（加性） | 非零常數 |
| $\mathbb{Z}[i]$ | $a^2+b^2$ | ✓ | $\pm1,\pm i$ |

### 9.3 例子

| 例子 | 結論 | 關鍵一步 |
|---|---|---|
| $7\in\mathbb{Z}[\sqrt5]$ | 不可約 | $a^2-5b^2\equiv0\ (\mathrm{mod}\ 7)$ ⇒ $49\mid7$ |
| $54 = 6\cdot8+6 = 7\cdot8-2$ | 除法算則不唯一 | — |
| $11+3i$、$2+3i$ | 輾轉相除得單位 $-i$ | $q = 2-2i$、$3+i$ |
| $46$ 在 $\mathbb{Z}[\sqrt{-5}]$ | 兩種不可約分解 | 不是 UFD；Lamé 的錯誤 |

**層級**：ED ⇒ PID ⇒ UFD ⇒ 整環（下次證）。

### 9.4 術語

| 中文 | English |
|---|---|
| 歐氏整環 | Euclidean domain (ED) |
| 量度 | measure |
| 輾轉相除法 | Euclidean algorithm |
| 互極大 | comaximal |
| 理想數 | ideal numbers |
| 唯一分解整環 | unique factorization domain (UFD) |
| Fermat 最後定理 | Fermat's Last Theorem |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **ED ⇒ PID ⇒ UFD** | [[47-L30-擴張體]] 開頭 |
| **$\mathbb{Z}[i]$ 的除法算則、範數** | [[51-L33-代數在數論上的應用]]：兩平方和 |
| **Kummer、Dedekind、理想** | [[53-L35-代數整數與考試檢討]] |
| **UFD、PID** | AA2 [[11-L9-歐氏整環、相伴元與PID]]、[[13-L11-代數數論故事與UFD]] |

---

## 附：本集一句話總結

> **整環裡質元一定不可約，到了 PID 反過來也對（用 $\langle a,b\rangle = \langle d\rangle$ 分兩種情況）；相伴元生成同一個主理想；有除法算則的整環叫歐氏整環——整數用絕對值（餘數正負都行）、多項式用次數、高斯整數用 $a^2+b^2$（取最近格點，餘數範數至多一半）；而 $\mathbb{Z}[\sqrt{-5}]$ 中 $46 = 2\cdot23 = (1+3\sqrt{-5})(1-3\sqrt{-5})$ 說明唯一分解不是理所當然——Lamé 就栽在這裡，這引出了唯一分解整環的定義。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra I」(Fall 2016) Lecture 29 錄影逐字稿（YouTube 自動字幕，52:48）、講義 `AlgebraInotes_2018.pdf` §4.7–4.8（p.157–164）與 Gallian 第 18 章整理。*
