---
course: Number Theory（2021 秋，線上錄影）
episode: 1
lecture: Lecture 1
date: 待補（2021 秋）
video: https://youtu.be/b-Irzbkw8Ok
notes: Jones & Jones《Elementary Number Theory》§11.2–11.3（書頁 218–220，PDF 頁 233–235）、附錄 A（書頁 239，PDF 頁 254）、附錄 B（書頁 243–245，PDF 頁 258–260）；本集大部分內容課本沒有
---

# 第 1 集 · Lecture 1：數系與代數（Numbers and Algebra） [▶ 影片](https://youtu.be/b-Irzbkw8Ok)

← 上一集：無 ｜ [總目錄](README.md) ｜ 下一集：[02-induction](02-induction.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 1 集
> **講者**：James Cook（⚠️ 待確認，見清單）
> **來源**：YouTube 錄影逐字稿（59:45，自動字幕）＋ Jones & Jones《Elementary Number Theory》§11.2–11.3、附錄 A、附錄 B
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 五個數系：N、Z、Q、R、C](#1-五個數系nzqrc)
  - [1.1 記號](#11-記號)
  - [1.2 大小：可數與不可數](#12-大小可數與不可數)
  - [1.3 結構：一層比一層多什麼](#13-結構一層比一層多什麼)
- [2. 數論的兩大方向](#2-數論的兩大方向)
- [3. 第一個例子：畢氏三元數組](#3-第一個例子畢氏三元數組)
- [4. 等價關係與奇偶](#4-等價關係與奇偶)
  - [4.1 等價關係、等價類](#41-等價關係等價類)
  - [4.2 例子：同奇偶](#42-例子同奇偶)
  - [4.3 奇偶的定義與證明示範](#43-奇偶的定義與證明示範)
- [5. 配方法](#5-配方法)
  - [5.1 幾何版：為什麼古人不要負根](#51-幾何版為什麼古人不要負根)
  - [5.2 古代沒有符號：九章算術的門](#52-古代沒有符號九章算術的門)
  - [5.3 代數版：三個例子](#53-代數版三個例子)
- [6. 數系怎麼蓋出來](#6-數系怎麼蓋出來)
  - [6.1 自然數：Peano 公理與 von Neumann 模型](#61-自然數peano-公理與-von-neumann-模型)
  - [6.2 整數：用數對模擬減法](#62-整數用數對模擬減法)
  - [6.3 有理數：分數體與 well-defined](#63-有理數分數體與-well-defined)
  - [6.4 實數：三條路與循環小數](#64-實數三條路與循環小數)
  - [6.5 複數：實數對與 2×2 矩陣](#65-複數實數對與-22-矩陣)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者自己說：頭幾堂課**還不太算數論**，是在打基礎 [▶ 13:42](https://youtu.be/b-Irzbkw8Ok?t=822)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | 五個數系各有什麼結構 | 附錄 B（體的定義） |
| 2 | 代數數論 vs 解析數論 | 無 |
| 3 | 畢氏三元數組 | §11.2–11.3 |
| 4 | 等價關係、奇偶的證明寫法 | 第 3 章才用到等價關係 |
| 5 | 配方法（幾何與代數） | 無 |
| 6 | 從集合論一路蓋出 N → Z → Q → R → C | 附錄 A 只講歸納法 |

---

## 1. 五個數系：N、Z、Q、R、C

### 1.1 記號

[▶ 00:00](https://youtu.be/b-Irzbkw8Ok?t=0)

| 記號 | 名稱 | 內容 |
|---|---|---|
| $\mathbb{N}$ | 自然數（natural numbers） | $1, 2, 3, 4, \dots$ |
| $\mathbb{Z}$ | 整數（integers） | 自然數、它們的負數、和 $0$ |
| $\mathbb{Q}$ | 有理數（rational numbers） | 分數 $a/b$，$a,b\in\mathbb{Z}$，$b\neq 0$ |
| $\mathbb{R}$ | 實數（real numbers） | 數線，又叫連續統（continuum） |
| $\mathbb{C}$ | 複數（complex numbers） | $a+bi$ |

- $\mathbb{Z}$ 來自德文 *Zahlen*（數）。⚠️ 逐字稿缺字：字幕寫「zalin」，應為 Zahlen。
- 本課的 $\mathbb{N}$ **從 1 開始**。【課本補充】課本附錄 A 也這樣定（$\mathbb{N}=\{1,2,3,\dots\}$），並註明有些作者把 0 也算進去（p. 239）。

【口頭】數論大多在研究自然數，特別是**質數**。但有時候要懂質數，反而要去看某些複數。例如之後會學的**高斯整數**（Gaussian integers，形如 $a+bi$、$a,b\in\mathbb{Z}$ 的複數）[▶ 01:06](https://youtu.be/b-Irzbkw8Ok?t=66)。

### 1.2 大小：可數與不可數

[▶ 01:38](https://youtu.be/b-Irzbkw8Ok?t=98)

用 $|A|$ 表示集合 $A$ 的**基數**（cardinality，就是「有多少個元素」的推廣）。兩個集合之間如果有**雙射**（bijection，一對一且映成的函數），就說它們一樣大。

$$|\mathbb{N}| = |\mathbb{Z}| = |\mathbb{Q}| \neq |\mathbb{R}| = |\mathbb{C}|$$

- 前三個是**可數**（countable）的；後兩個是**不可數**（uncountable）的。
- 怪的地方：$\mathbb{Q}$ 看起來比 $\mathbb{N}$ 大很多，其實一樣大。

【口頭】講者說基數和本課關係不大，只是讓大家知道；之後不會再講。

### 1.3 結構：一層比一層多什麼

[▶ 04:19](https://youtu.be/b-Irzbkw8Ok?t=259)

五個數系雖然有的一樣大，結構卻都不同。一層一層看：

**$\mathbb{N}$**：加法封閉（closed，兩個自然數相加還是自然數），加法有交換律、結合律。**但沒有 0**，也就是沒有加法單位元素（additive identity）。

**$\mathbb{Z}$**：多了 $0$（任何整數加 $0$ 不變），而且每個數都有負數（對取負封閉）。乘法也封閉。**但沒有乘法反元素**：例如 $2$ 的乘法反元素是 $\tfrac12$，不在 $\mathbb{Z}$ 裡。

**$\mathbb{Q}$**：每個**非零**數都有乘法反元素。這讓 $\mathbb{Q}$ 成為一個**體**（field）[▶ 05:24](https://youtu.be/b-Irzbkw8Ok?t=324)。$\mathbb{R}$ 和 $\mathbb{C}$ 也都是體。

> 【課本補充】課本附錄 B（p. 244–245）的定義：
> - **環**（ring，課本指有單位元素的交換環）：集合 $R$ 有加法和乘法，$(R,+)$ 是交換群（有 $0$、有負數、結合、交換），乘法交換、結合、對加法分配，且有 $1$（$r1=r$）。
> - **單位**（unit）：$r$ 是單位，若存在 $s$ 使 $rs=1$。
> - **體**（field）：每個 $r\neq 0$ 都是單位的環。
> - $\mathbb{Z}$ 是環但不是體；$\mathbb{Q}$、$\mathbb{R}$、$\mathbb{C}$ 是體；$\mathbb{Z}_n$ 在 $n$ 是質數時也是體（後面的集數會講）。

**$\mathbb{Q}$ 的缺點：不完備** [▶ 06:36](https://youtu.be/b-Irzbkw8Ok?t=396)

- **完備**（complete）：每個 Cauchy 數列（項與項之間越來越靠近的數列）在這個空間裡都有極限。
- 反例：$\sqrt2$ 的截斷小數
  $$1,\ 1.4,\ 1.41,\ 1.414,\ \dots$$
  每一項都是有理數（$\tfrac{14}{10}$、$\tfrac{141}{100}$、$\tfrac{1414}{1000}$……），但極限 $\sqrt2$ 不是有理數。
- 所以在 $\mathbb{Q}$ 上做微積分會出問題，例如**中間值定理**（intermediate value theorem）不成立——數線上有「洞」。
- 「$\sqrt2$ 是無理數」之後會用一整堂課證明（第 9 集）。

**$\mathbb{R}$ 的缺點：有些多項式方程沒有解** [▶ 09:19](https://youtu.be/b-Irzbkw8Ok?t=559)

- $\mathbb{R}$ 是完備的。
- 但 $x^2+1$ 在實數上不能分解。要用 $i$（$i^2=-1$）：
  $$x^2+1 = x^2 - i^2 = (x-i)(x+i).$$

**$\mathbb{C}$**：也完備，而且**代數基本定理**（fundamental theorem of algebra）說：每個複係數多項式都有根，所以可以完全分解成一次式 [▶ 10:27](https://youtu.be/b-Irzbkw8Ok?t=627)。

【口頭】講者提醒：「完備」這裡用了兩種意思——分析上的完備（Cauchy 數列收斂）和「多項式能完全分解」（正式名稱是代數封閉，algebraically closed）。

**序**：$\mathbb{Q}$ 和 $\mathbb{R}$ 有和加法、乘法相容的大小關係 $<$（有序體，ordered field）；$\mathbb{C}$ 沒有 [▶ 10:58](https://youtu.be/b-Irzbkw8Ok?t=658)。

| | 加法單位 0 | 負數 | 乘法反元素 | 完備 | 多項式都能分解 | 有序 |
|---|---|---|---|---|---|---|
| $\mathbb{N}$ | ✗ | ✗ | ✗ | — | ✗ | ✓ |
| $\mathbb{Z}$ | ✓ | ✓ | ✗ | — | ✗ | ✓ |
| $\mathbb{Q}$ | ✓ | ✓ | ✓（體） | ✗ | ✗ | ✓ |
| $\mathbb{R}$ | ✓ | ✓ | ✓（體） | ✓ | ✗ | ✓ |
| $\mathbb{C}$ | ✓ | ✓ | ✓（體） | ✓ | ✓ | ✗ |

---

## 2. 數論的兩大方向

[▶ 11:31](https://youtu.be/b-Irzbkw8Ok?t=691)

- **Diophantine 方程**（丟番圖方程）：在 $\mathbb{N}$ 或 $\mathbb{Z}$ 裡找解的方程。本課會看。
- 數論大致分兩派：
  - **代數數論**（algebraic number theory）
  - **解析數論**（analytic number theory）

【口頭】兩派不是互斥的，有重疊；數學的分類從來沒有學生想的那麼硬。本課**主要走代數那邊** [▶ 13:08](https://youtu.be/b-Irzbkw8Ok?t=788)：

- 解析數論要很深的複分析，超出本課程度。
- 講者假設大家會一些微積分、偶爾一點線性代數、基本代數。代數數論很多論證這樣就夠了。

---

## 3. 第一個例子：畢氏三元數組

[▶ 13:42](https://youtu.be/b-Irzbkw8Ok?t=822)

**定義**：**畢氏三元數組**（Pythagorean triple）是三個自然數 $(a,b,c)$，滿足
$$a^2+b^2=c^2.$$
每組對應一個三邊都是整數的直角三角形。

【口頭】歷史：講者翻了一本（不是本課課本的）書上的年表，畢達哥拉斯約西元前 569–500 年。但巴比倫人和幾乎所有有紀錄的古文明都研究過直角三角形，因為要蓋東西 [▶ 14:15](https://youtu.be/b-Irzbkw8Ok?t=855)。

**性質：放大還是三元數組** [▶ 15:23](https://youtu.be/b-Irzbkw8Ok?t=923)

幾何上：把三角形各邊乘 $\lambda>0$，得到相似三角形。代數上：

若 $a^2+b^2=c^2$，則
$$(\lambda a)^2+(\lambda b)^2 = \lambda^2(a^2+b^2) = \lambda^2c^2 = (\lambda c)^2.$$
所以 $\lambda$ 是自然數時，$(\lambda a,\lambda b,\lambda c)$ 也是畢氏三元數組。

**例**：$(3,4,5)$：$9+16=25$。乘 8 得 $(24,32,40)$：$576+1024=1600=40^2$。✓

【口頭】講者說這不是很厲害的例子，只是讓大家看「用代數從一個數論對象得到另一個」是什麼樣子。

> 【課本補充】§11.2–11.3（p. 218–220）
> - **畢氏定理的證明**（Figure 11.1）：邊長 $a+b$ 的正方形裡放四個直角三角形。一種放法剩下一個面積 $c^2$ 的正方形；另一種放法剩下面積 $a^2$ 和 $b^2$ 的兩個正方形。三角形面積不變，所以 $a^2+b^2=c^2$。
> - **本原**（primitive）三元數組：$\gcd(a,b,c)=1$（三數沒有大於 1 的公因數）。例如 $(3,4,5)$、$(5,12,13)$ 是本原的，$(6,8,10)$ 不是。
> - $(a,b,c)$ 本原 $\iff$ 任兩個互質。原因：若某質數整除其中兩個，由 $a^2+b^2=c^2$ 它也整除第三個。
> - **每個**三元數組都是某個本原三元數組乘上 $m\ge1$：$(ma,mb,mc)$。所以只要找出所有本原的就好。（這正是本節「放大」的反方向。）
> - 巴比倫泥板 Plimpton 322（約西元前 1900–1600 年）列了本原三元數組，例如 $(4961, 6480, 8161)$。
> - 本原三元數組的完整分類在 §11.5，後面「費馬最後定理」那集會用到。

---

## 4. 等價關係與奇偶

### 4.1 等價關係、等價類

[▶ 17:37](https://youtu.be/b-Irzbkw8Ok?t=1057)

本集最後蓋數系要用到等價關係，先複習。

**定義**：集合 $S$ 上的關係 $\sim$ 叫**等價關係**（equivalence relation），如果對所有 $x,y,z\in S$：

1. **反身**（reflexive）：$x\sim x$
2. **對稱**（symmetric）：$x\sim y \Rightarrow y\sim x$
3. **遞移**（transitive）：$x\sim y$ 且 $y\sim z \Rightarrow x\sim z$

**定義**：$x$ 的**等價類**（equivalence class）是所有和 $x$ 等價的元素：
$$[x] = \{\,y\in S : y\sim x\,\}.$$
$x$ 叫這個類的**代表**（representative）。代表**不唯一**：同一類裡任何元素都可以當代表 [▶ 18:44](https://youtu.be/b-Irzbkw8Ok?t=1124)。

### 4.2 例子：同奇偶

[▶ 19:17](https://youtu.be/b-Irzbkw8Ok?t=1157)

在 $\mathbb{Z}$ 上定 $x\sim y$ 若 $x,y$ **同奇偶**（parity，都是偶數或都是奇數）。

- $[1]$ = 所有奇數 $= 1+2\mathbb{Z}$
- $[2]$ = 所有偶數 $= 2\mathbb{Z}$

反身、對稱、遞移都很容易檢查。

**等價類會分割集合** [▶ 19:49](https://youtu.be/b-Irzbkw8Ok?t=1189)：等價關係的等價類把集合切成互不相交、合起來是全部的幾塊，叫**分割**（partition）。這裡：
$$\mathbb{Z} = 2\mathbb{Z}\ \cup\ (2\mathbb{Z}+1),\qquad 2\mathbb{Z}\cap(2\mathbb{Z}+1)=\varnothing.$$
（寫 $2\mathbb{Z}+1$ 或 $1+2\mathbb{Z}$ 都可以，加法可交換。）

### 4.3 奇偶的定義與證明示範

[▶ 20:54](https://youtu.be/b-Irzbkw8Ok?t=1254)

**定義**：
- 整數 $x$ 是**偶數**（even）$\iff$ 存在 $k\in\mathbb{Z}$ 使 $x=2k$。
- 整數 $x$ 是**奇數**（odd）$\iff$ 存在 $k\in\mathbb{Z}$ 使 $x=2k+1$。

（iff = if and only if，若且唯若。）

【口頭】講者要求：作業裡證明奇偶的題目**必須用這兩個定義**。

**命題**：偶數乘奇數是偶數。

**證明** [▶ 21:26](https://youtu.be/b-Irzbkw8Ok?t=1286)：設 $x$ 是偶數、$y$ 是奇數。依定義，存在 $k,j\in\mathbb{Z}$ 使
$$x=2k,\qquad y=2j+1.$$
那麼
$$xy = 2k(2j+1) = 2(2kj+k).$$
$2kj+k$ 是整數，所以 $xy\in 2\mathbb{Z}$，即 $xy$ 是偶數。∎

⚠️ 逐字稿缺字：[▶ 21:58](https://youtu.be/b-Irzbkw8Ok?t=1318) 字幕寫「y is equal to 2j since y is odd」，少了「+1」；下一句計算用的是 $2j+1$，筆記照計算寫。

---

## 5. 配方法

### 5.1 幾何版：為什麼古人不要負根

[▶ 22:30](https://youtu.be/b-Irzbkw8Ok?t=1350)

【口頭】不久之前，數學家還看不起負數，解多項式方程時會把負根丟掉。這個例子讓你懂中世紀數學家為什麼這樣想。這也是「配方」（completing the square，字面是「補成正方形」）名字的由來。

**解** $x^2+26x=27$，把每一項都看成**面積** [▶ 23:36](https://youtu.be/b-Irzbkw8Ok?t=1416)：

1. $x^2$ 是邊長 $x$ 的正方形；$26x$ 是 $26\times x$ 的長方形。兩塊面積合起來是 $27$。
2. 把長方形切成兩半，各是 $13\times x$，一塊貼在正方形右邊、一塊貼在下面。
3. 這樣右下角缺一塊 $13\times13$ 的小正方形。把它**補上**，就得到一個大正方形。
4. 大正方形面積 $= 27 + 169 = 196 = 14^2$，所以邊長是 $14$。
5. 大正方形邊長也是 $x+13$，所以 $x+13=14$，$x=1$。

在這種想法裡，$x$ 是一條邊的長度，**負數根本沒有意義**。對大約西元 1000–1500 年以前的數學家，方程只是幾何問題的記號，所以丟掉負根很自然。今天我們先想方程、忘了圖，才覺得奇怪 [▶ 26:26](https://youtu.be/b-Irzbkw8Ok?t=1586)。

### 5.2 古代沒有符號：九章算術的門

[▶ 28:10](https://youtu.be/b-Irzbkw8Ok?t=1690)

【口頭】現在的代數符號其實很新。講者引用 Rotman《Journey into Mathematics: An Introduction to Proofs》p. 57 引的一題，出自約 2000 年前中國的《九章算術》（*Nine Chapters on the Mathematical Art*）：

> 有一扇門，高和寬都不知道；有一根竿子，長度也不知道。橫著拿，差一些放不進去；直著拿，也差一些；斜著拿，剛好放進去。問門的高、寬、對角線各多少？

題目裡「差多少」的數字字幕沒聽清楚（講者自己也說排版有漏），待補。

重點是：**題目裡沒有任何方程**，全部用句子寫。中國、古歐洲、古印度都一樣——符號代數發明之前，數學都用文字寫。

### 5.3 代數版：三個例子

[▶ 29:50](https://youtu.be/b-Irzbkw8Ok?t=1790)

方法：$x^2+bx = \left(x+\tfrac b2\right)^2 - \tfrac{b^2}{4}$，再用**平方差** $A^2-B^2=(A-B)(A+B)$。

**例 1**：$x^2+26x-27=0$ [▶ 30:28](https://youtu.be/b-Irzbkw8Ok?t=1828)
$$x^2+26x-27 = (x+13)^2-169-27 = (x+13)^2-14^2 = (x+13-14)(x+13+14) = (x-1)(x+27).$$
根是 $x=1$ 和 $x=-27$（中世紀的人會丟掉後者）。

【口頭】這題直接因式分解也行，但**配方不用猜**。

**例 2**：分解 $2x^2+7x+1$（看成式子，不是方程）[▶ 32:09](https://youtu.be/b-Irzbkw8Ok?t=1929)

先提出 2：
$$2x^2+7x+1 = 2\left(x^2+\tfrac72x+\tfrac12\right).$$
$\tfrac72$ 的一半是 $\tfrac74$：
$$= 2\left[\left(x+\tfrac74\right)^2-\tfrac{49}{16}+\tfrac{8}{16}\right] = 2\left[\left(x+\tfrac74\right)^2-\tfrac{41}{16}\right].$$
把 $\tfrac{41}{16}$ 寫成平方 $\left(\tfrac{\sqrt{41}}{4}\right)^2$，用平方差：
$$= 2\left(x+\tfrac74-\tfrac{\sqrt{41}}4\right)\left(x+\tfrac74+\tfrac{\sqrt{41}}4\right).$$

【口頭】這個分解你不可能猜得出來。**配方是演算法**，不會出錯 [▶ 34:22](https://youtu.be/b-Irzbkw8Ok?t=2062)。

**例 3**：$x^2+4x+5$ [▶ 34:56](https://youtu.be/b-Irzbkw8Ok?t=2096)
$$x^2+4x+5 = (x+2)^2-4+5 = (x+2)^2+1.$$
- 只用實數：卡住了。配完方後剩下的是 **$+$** 正數，不能用平方差。這種叫**不可約**（irreducible，講者也叫「prime」）。
- 允許複數：$1=-i^2$，所以
$$(x+2)^2+1 = (x+2)^2-i^2 = (x+2-i)(x+2+i).$$

**判斷法**：配完方後，若剩 $(\cdots)^2 - (\text{正數})$，就能在實數上分解；若剩 $(\cdots)^2 + (\text{正數})$，實數上不可約 [▶ 35:28](https://youtu.be/b-Irzbkw8Ok?t=2128)。

---

## 6. 數系怎麼蓋出來

[▶ 36:33](https://youtu.be/b-Irzbkw8Ok?t=2193)

前面只是給了幾個字母。挑剔的人會問：你怎麼知道這些東西存在？下面看數學家怎麼**構造**它們。

### 6.1 自然數：Peano 公理與 von Neumann 模型

[▶ 37:05](https://youtu.be/b-Irzbkw8Ok?t=2225)

19 世紀第一次嚴格描述自然數，用的是 **Peano 公理**（Peano axioms）。⚠️ 逐字稿缺字：字幕寫「piano axioms」。

1. $1$ 是自然數。
2. 每個自然數 $x$ 都有一個**後繼**（successor）$S(x)$。
3. $1$ 不是任何自然數的後繼。
4. 若 $S(x)=S(y)$，則 $x=y$。
5. **歸納**（induction）：（下一集詳講。）

> 【課本補充】附錄 A（p. 239）的歸納原理：若 $P(1)$ 成立，且對所有 $n\in\mathbb{N}$，$P(n)\Rightarrow P(n+1)$，則 $P(n)$ 對所有 $n\in\mathbb{N}$ 成立。等價的集合版本：若 $A\subseteq\mathbb{N}$、$1\in A$、且 $n\in A\Rightarrow n+1\in A$，則 $A=\mathbb{N}$。

**von Neumann 構造**（用集合蓋出自然數）[▶ 38:12](https://youtu.be/b-Irzbkw8Ok?t=2292)：

- 用空集合代表 $0$：$0 = \varnothing$。
- 後繼定義為 $S(x) = x\cup\{x\}$。
- 於是
$$1 = S(0) = \varnothing\cup\{\varnothing\} = \{\varnothing\} = \{0\},$$
$$2 = S(1) = \{0,1\} = \{\varnothing,\{\varnothing\}\},$$
$$3 = S(2) = \{0,1,2\},\ \dots$$
- 每個數 = 比它小的所有數組成的集合。
- 用後繼函數可以定義加法和乘法；大小定義為 $x<y \iff x\subset y$。

注意：這裡從 $0$ 開始，和 Peano 公理那邊的「$1$ 是自然數」不同；講者沒有特別說明。

【口頭】講者提到的作業題（不做解答，只記講者的提示）[▶ 39:51](https://youtu.be/b-Irzbkw8Ok?t=2391)：
- (a) $x<y$ 且 $y<z \Rightarrow x<z$：因為 $<$ 定義成子集合，子集合有遞移性。
- (b) $x\le y$ 且 $y\le x \Rightarrow x=y$：兩邊互相包含，集合就相等。
- (c) $1\cdot x = x$：要用歸納法，要想一下。

【口頭】講者說這只是自然數的一個**模型**，不是說自然數「就是」那些集合；他自己想自然數時還是想 1、2、3、4。重點是：只要相信有集合，就能做出自然數 [▶ 40:56](https://youtu.be/b-Irzbkw8Ok?t=2456)。

### 6.2 整數：用數對模擬減法

[▶ 41:28](https://youtu.be/b-Irzbkw8Ok?t=2488)

想法：數對 $(a,b)$ 代表「$a-b$」。但只能用加法，不能用減法。

$a-b = c-d$ 換成加法就是 $a+d = b+c$。所以在 $\mathbb{N}_0\times\mathbb{N}_0$（$\mathbb{N}_0=\{0,1,2,\dots\}$）上定義
$$(a,b)\sim(c,d) \iff a+d = b+c.$$
等價類的集合 $(\mathbb{N}_0\times\mathbb{N}_0)/\!\sim$ 就是整數的模型。

加法、乘法的公式在螢幕上，字幕沒唸出。以下**不是逐字稿內容**，是依「$(a,b)$ 代表 $a-b$」推論的：
$$[(a,b)]+[(c,d)] = [(a+c,\ b+d)],\qquad [(a,b)]\cdot[(c,d)] = [(ac+bd,\ ad+bc)].$$
（因為 $(a-b)+(c-d) = (a+c)-(b+d)$，$(a-b)(c-d) = (ac+bd)-(ad+bc)$。）

【口頭】講者說這構造「很狡猾」，留作作業 [▶ 43:19](https://youtu.be/b-Irzbkw8Ok?t=2599)。

### 6.3 有理數：分數體與 well-defined

[▶ 43:19](https://youtu.be/b-Irzbkw8Ok?t=2599)

從整數造出**分數體**（field of fractions）。

令 $S = \{(a,b)\in\mathbb{Z}\times\mathbb{Z} : b\neq 0\}$（第二個分量不能是 0，所以 $S$ 只是 $\mathbb{Z}\times\mathbb{Z}$ 的子集合）。$(a,b)$ 代表分數 $a/b$。

同一個分數有無限多種寫法：$\tfrac12=\tfrac24=\tfrac36=\cdots$。交叉相乘相等就算同一個：
$$(a,b)\sim(c,d) \iff ad = bc.$$
這是 $S$ 上的等價關係。分數定義為等價類：
$$\frac ab = \{\,(c,d)\in S : (c,d)\sim(a,b)\,\}.$$

加法、乘法（字幕沒唸出公式，這裡寫標準定義）：
$$\frac ab+\frac cd = \frac{ad+bc}{bd},\qquad \frac ab\cdot\frac xy = \frac{ax}{by}.$$

**什麼是 well-defined（定義良好）** [▶ 44:57](https://youtu.be/b-Irzbkw8Ok?t=2697)：用等價類定義運算時，必須證明**結果和代表的選法無關**。換別的代表，答案要是同一個等價類。

**證明：乘法是 well-defined** [▶ 45:30](https://youtu.be/b-Irzbkw8Ok?t=2730)

設 $\dfrac ab=\dfrac{a'}{b'}$、$\dfrac xy=\dfrac{x'}{y'}$（同一個分數的兩種代表）。也就是
$$ab' = ba',\qquad xy' = yx'. \tag{$*$}$$
要證：
$$\underbrace{\frac{a'x'}{b'y'}}_{(1)} = \underbrace{\frac{ax}{by}}_{(2)},$$
也就是要證 $a'x'\cdot by = b'y'\cdot ax$。

計算：
$$a'x'\cdot by = (a'b)(x'y) = (ab')(xy') = (b'y')(ax).$$
第二個等號用 $(*)$：把 $a'b$ 換成 $ab'$，把 $x'y$ 換成 $xy'$。所以 (1) = (2)，乘法 well-defined。∎

【口頭】
- 講者的作業：證明加法也 well-defined、乘法交換、加法結合。「結合」的意思是 $\left(\tfrac ab+\tfrac cd\right)+\tfrac xy = \tfrac ab+\left(\tfrac cd+\tfrac xy\right)$，括號放哪裡不影響 [▶ 50:11](https://youtu.be/b-Irzbkw8Ok?t=3011)。
- 講者在 [▶ 46:36](https://youtu.be/b-Irzbkw8Ok?t=2796) 插了一句「secret word is juggernaut」，是給看影片的學生的暗號（播放清單另有一部「secret word」短片，筆記略過）。

### 6.4 實數：三條路與循環小數

[▶ 50:42](https://youtu.be/b-Irzbkw8Ok?t=3042)

實數的構造本質上是**分析**的。三種常見做法：

1. **完備化**（completion）：把有理數所有 Cauchy 數列的極限點加進來（用歐氏距離）。
2. **Dedekind 分割**（Dedekind cuts）：用集合做同一件事，19 世紀中期（約 1850 年代）。⚠️ 逐字稿缺字：字幕寫「data kind cuts」。講者說這方法「很狡猾」，沒有細講。
3. **小數展開**：實數 = 有小數展開的數。工程師常這樣定義。

【口頭】講者在本課採用第 3 種當工作定義，因為最不技術、最熟悉。嚴格來說要證明關於小數的命題，得證明收斂級數的加法、乘法，本課不做 [▶ 52:18](https://youtu.be/b-Irzbkw8Ok?t=3138)。

**小數展開**：小數點左邊有限多位，右邊可以無限多位：
$$x = d_m d_{m-1}\cdots d_0 . d_{-1}d_{-2}\cdots = \sum_{k\le m} d_k\,10^k .$$
一定有一個最高次的 10 的冪。例如
$$123.456456\ldots = 100+20+3+\tfrac4{10}+\tfrac5{100}+\tfrac6{1000}+\tfrac4{10^4}+\cdots$$

**定理**：小數展開**最後會循環**的實數，正好就是有理數 [▶ 53:24](https://youtu.be/b-Irzbkw8Ok?t=3204)。

關鍵工具是**等比級數**（geometric series）：
$$a + ar + ar^2 + \cdots = \frac{a}{1-r},\qquad |r|<1.$$

**例**：$x = 0.34555\ldots$（5 一直循環）[▶ 53:57](https://youtu.be/b-Irzbkw8Ok?t=3237)

拆成不循環和循環兩部分：
$$x = 0.34 + 0.00555\ldots$$
- 不循環部分：$0.34 = \dfrac{34}{100}$（拿掉小數點、除以 100）。
- 循環部分：$0.005+0.0005+0.00005+\cdots$，首項 $a=0.005$、公比 $r=\tfrac1{10}$：
$$\frac{0.005}{1-\frac1{10}} = \frac{5}{1000}\cdot\frac{10}{9} = \frac{5}{900}.$$
- 加起來：
$$x = \frac{34}{100}+\frac{5}{900} = \frac{306}{900}+\frac{5}{900} = \frac{311}{900}.$$

⚠️ 待確認：字幕把這個數唸成「100 1 thousand 245 0.3455555」，整數部分聽不清楚；筆記只用小數部分 $0.34555\ldots$ 示範，算法不受影響。另外字幕先說「a here is 0.05」、後面算式用 $0.005$；筆記照算式用 $0.005$。

【口頭】講者留的作業：找出小數展開為 $12.348348\ldots$（348 循環）的有理數，以及小數部分 $238095$ 循環的那個數（不做解答）[▶ 55:02](https://youtu.be/b-Irzbkw8Ok?t=3302)。

【口頭】三步之中，從 $\mathbb{Q}$ 到 $\mathbb{R}$ 是最難的。但沒有實數就沒有微積分。小數展開只比牛頓早大約 50 年——想想沒有小數要怎麼做近似計算 [▶ 56:38](https://youtu.be/b-Irzbkw8Ok?t=3398)。

### 6.5 複數：實數對與 2×2 矩陣

[▶ 57:11](https://youtu.be/b-Irzbkw8Ok?t=3431)

【口頭】這個構造有時歸功於 Gauss，有時歸功於 Argand（「Argand 平面」）。講者認為應該叫 Euler 平面，$i$ 這個記號是 Euler 1777 年用的。⚠️ 逐字稿缺字：字幕寫「argon」，應為 Argand。（講者說 Euler「在 1800 年代」做這些，但 Euler 1783 年就過世了，應是口誤，指 1700 年代。）

**定義**：複數 = 實數對 $(a,b)$，加法逐分量，乘法是「奇怪的乘法」。字幕沒唸出公式，以下是標準定義：
$$(a,b)(c,d) = (ac-bd,\ ad+bc).$$

兩個講者有唸出的檢查 [▶ 57:44](https://youtu.be/b-Irzbkw8Ok?t=3464)：
- $(1,0)(x,y) = (x,y)$：$(1,0)$ 就像數字 $1$。
- $(0,1)(0,1) = (0\cdot0-1\cdot1,\ 0\cdot1+1\cdot0) = (-1,0)$：就是 $-1$。

所以寫成 $a+bi$ 時，$i$ 由 $(0,1)$ 代表，而 $i^2=-1$。

**另一種模型：2×2 矩陣** [▶ 58:48](https://youtu.be/b-Irzbkw8Ok?t=3528)

把 $a+bi$ 對應到矩陣
$$a+bi \ \longleftrightarrow\ \begin{pmatrix} a & -b \\ b & a \end{pmatrix},\qquad i \ \longleftrightarrow\ \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
檢查：$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$。

【口頭】結語 [▶ 59:20](https://youtu.be/b-Irzbkw8Ok?t=3560)：這些構造不是說「數就是這些東西」。重點是**這樣的系統確實存在**，而且值得研究——這就是本學期要做的事。

---

## 7. 一頁速查表

**數系的結構**

| | 新多了什麼 | 還缺什麼 | 例子 |
|---|---|---|---|
| $\mathbb{N}$ | 加法、乘法封閉 | 0、負數 | — |
| $\mathbb{Z}$ | 0、負數（環） | 乘法反元素 | $2^{-1}\notin\mathbb{Z}$ |
| $\mathbb{Q}$ | 非零數有反元素（體） | 完備性 | $1, 1.4, 1.41,\dots\to\sqrt2\notin\mathbb{Q}$ |
| $\mathbb{R}$ | 完備、有序 | 多項式的根 | $x^2+1$ 無實根 |
| $\mathbb{C}$ | 代數封閉 | 序 | — |

基數：$|\mathbb{N}|=|\mathbb{Z}|=|\mathbb{Q}|$（可數）$\neq|\mathbb{R}|=|\mathbb{C}|$（不可數）。

**畢氏三元數組**
- $(a,b,c)$ 是三元數組 $\Rightarrow (\lambda a,\lambda b,\lambda c)$ 也是。關鍵：$(\lambda a)^2+(\lambda b)^2 = \lambda^2(a^2+b^2)=\lambda^2c^2$。
- 【課本】每個三元數組 = 本原三元數組 × $m$；本原 $\iff$ 任兩個互質。

**等價關係**
- 反身、對稱、遞移。等價類 $[x]=\{y: y\sim x\}$，代表不唯一。
- 等價類分割集合：$\mathbb{Z} = 2\mathbb{Z}\cup(2\mathbb{Z}+1)$。

**奇偶證明的寫法**
- 偶：$x=2k$；奇：$x=2k+1$。
- 偶 × 奇：$2k(2j+1) = 2(2kj+k)$。關鍵：把 2 提出來，括號裡是整數。

**配方法**
- $x^2+bx+c = \left(x+\tfrac b2\right)^2 - \left(\tfrac{b^2}4 - c\right)$，再用 $A^2-B^2=(A-B)(A+B)$。
- 剩 $-$正數 → 實數上可分解；剩 $+$正數 → 實數上不可約，複數上用 $B^2 = -(iB)^2$ 分解。
- $2x^2+7x+1 = 2\left(x+\tfrac{7-\sqrt{41}}{4}\right)\left(x+\tfrac{7+\sqrt{41}}{4}\right)$。

**數系的構造**

| 數系 | 構造 | 等價關係／運算 |
|---|---|---|
| $\mathbb{N}_0$ | von Neumann | $0=\varnothing$，$S(x)=x\cup\{x\}$，$x<y\iff x\subset y$ |
| $\mathbb{Z}$ | $(\mathbb{N}_0\times\mathbb{N}_0)/\!\sim$ | $(a,b)\sim(c,d)\iff a+d=b+c$ |
| $\mathbb{Q}$ | 分數體 | $(a,b)\sim(c,d)\iff ad=bc$；$\tfrac ab\cdot\tfrac xy=\tfrac{ax}{by}$ |
| $\mathbb{R}$ | Cauchy 完備化／Dedekind 分割／小數 | 循環小數 $\iff$ 有理數 |
| $\mathbb{C}$ | $\mathbb{R}^2$ 加奇怪乘法 | $(a,b)(c,d)=(ac-bd,ad+bc)$；或 $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$ |

- **Well-defined**：用等價類定義運算時，要證結果和代表無關。乘法的關鍵一步：$a'x'\cdot by=(a'b)(x'y)=(ab')(xy')=b'y'\cdot ax$。
- **循環小數 → 分數**：拆成不循環＋循環，循環部分用 $\dfrac a{1-r}$。例：$0.34\bar5 = \tfrac{34}{100}+\tfrac{5}{900}=\tfrac{311}{900}$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Peano 公理的歸納公理 | 第 2 集（Induction） |
| $\sqrt2$ 不是有理數 | 第 9 集（irrationality of √2） |
| 等價關係、等價類、代表、well-defined | 第 10 集起的模運算（同餘類 $\mathbb{Z}_n$） |
| 體、乘法反元素 | 第 14–15 集（單位群 $U_n$）；$\mathbb{Z}_p$ 是體 |
| 配方法、二次式 | 第 17–18 集（二次互反律）、第 20 集（三次方程） |
| 複數、$i^2=-1$ | 第 19 集（複數與單位根）、第 21–22 集（高斯整數） |
| 複數的 2×2 矩陣模型 | 第 23 集（四元數） |
| 畢氏三元數組 | 第 21 集（平方和）、第 24 集（費馬最後定理，課本 §11.5 分類） |


---

## 附：本集一句話總結

> **五個數系 N ⊂ Z ⊂ Q ⊂ R ⊂ C，每往上一層就補上前一層缺的東西（0 與負數、乘法反元素、完備性、多項式的根）；而且它們都能從集合出發，用「等價類」一步一步蓋出來——只是每次用等價類定義運算，都要檢查 well-defined。**

---

## ⚠️ 待確認清單

1. 講者姓名：依播放清單頻道和第 26 部影片標題「HAPPY BIRTHDAY JAMES!」推斷為 James Cook，本集逐字稿沒有自我介紹，待確認。
2. 上課日期：只知道是 2021 秋（第 17 集標題有 10-13-21），本集確切日期不明。
3. [▶ 53:57](https://youtu.be/b-Irzbkw8Ok?t=3237) 循環小數例子的整數部分字幕聽不清楚（「100 1 thousand 245 0.3455555」），筆記只用 $0.34555\ldots$。
4. [▶ 28:42](https://youtu.be/b-Irzbkw8Ok?t=1722) 九章算術「門」題中，竿子橫放、直放各差多少，字幕沒聽清楚，待補。

---

*筆記依據 James Cook（待確認）「Number Theory」Lecture 1 錄影逐字稿（YouTube 自動字幕，59:45）與 Jones & Jones《Elementary Number Theory》§11.2–11.3、附錄 A、附錄 B 整理。*
