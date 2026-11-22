---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 5
lecture: "Lec05 Appendix B: Overview in Probability and Random Processes"
date: 待補
video: https://youtu.be/wjEbKHV6UAg
notes: Alajaji & Chen 附錄 B §B.1–B.2（pp. 273–276，Definition B.1–B.2、Observation B.3）
---

# 第 5 集 · Lec05 附錄 B：σ-field、機率空間、隨機變數、隨機過程 [▶ 影片](https://youtu.be/wjEbKHV6UAg)

← 上一集：[04](04-review-suprema-limits-equivalence.md) ｜ [總目錄](README.md) ｜ 下一集：[06](06-statistical-properties-random-sources.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 5 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（34:51，whisper large-v3-turbo）＋ 課本附錄 B §B.1–B.2（pp. 273–276）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「實數」聽成「時數」，「公設」聽成「公社」，「量度」聽成「凉度／良度」，「聯集」聽成「連擊／連級」，「集合」聽成「即和」，「閉區間」聽成「B區間」，「補集合」聽成「補集額」，「Borel」聽成「Barrell」，「Lebesgue」聽成「Lebesgue」（正確），「Riemann」聽成「Reimann／里曼」，「additivity」聽成「Addictivity」，「probability measure」聽成「Property Major」，「probability space」聽成「Private Space／Propriet space／perispase」，「powerset」聽成「PowerShade」，「實變分析」聽成「十遍分析」，「約定俗成」聽成「約定成熟」。開頭 [00:00]「雙方的天使經驗」是 whisper 亂碼。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼機率要從集合開始](#1-為什麼機率要從集合開始)
- [2. σ-field 的三個公設](#2-σ-field-的三個公設)
- [3. 最大和最小的 σ-field](#3-最大和最小的-σ-field)
- [4. 為什麼一定是 countable](#4-為什麼一定是-countable)
- [5. 機率測度的三個公設](#5-機率測度的三個公設)
- [6. Borel σ-field](#6-borel-σ-field)
- [7. 隨機變數：映射到實數](#7-隨機變數映射到實數)
- [8. 隨機過程：同一個機率空間](#8-隨機過程同一個機率空間)
- [9. 為什麼大二機率不用講機率空間](#9-為什麼大二機率不用講機率空間)
- [10. 不映射到實數的情形](#10-不映射到實數的情形)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

複習機率的公設體系：**σ-field → 機率空間 $(\Omega,\mathcal F,P)$ → 隨機變數 → 隨機過程**。重點不是定義本身，而是**為什麼要這樣定義**。

| 主題 | 課本 |
|---|---|
| σ-field、power set | Definition B.1（p. 273） |
| 機率空間、countable additivity | Definition B.2（p. 274） |
| 隨機變數、Borel σ-field | §B.2（p. 274） |
| 分布函數 vs 機率空間 | Observation B.3（p. 275） |
| random vector、random process | §B.2（pp. 275–276） |

【口頭】機率現在是電機系必修；random process 雖然研究所不是必修，但幾乎是每個人進研究所的第一門課，每學期都開。這裡要說明消息理論怎麼用這些東西。Shannon 應該算是機率學家，他們從最基礎的性質（公設，axiom）去思考。

---

## 1. 為什麼機率要從集合開始

[▶ 01:02](https://youtu.be/wjEbKHV6UAg?t=62)

我們要算的是 **event（事件）** 的機率。
- 例：丟六面骰子，關心「出現 2、4、6 點」或「出現 4、5、6 點」的機率。
- 不管哪一種，event 都是一個**集合**。所以需要一套處理集合的體系，否則沒辦法處理機率。

【口頭】
- 機率空間在幾百年前可能有不同的想法，慢慢收斂到最基礎的性質；就像 Shannon 提出的 information 基本性質後來被公認為最重要的。
- 老師把 space 翻成「**體系**」而不是「空間」：體系包含操作。就像 linear space、vector space 不只是一群元素，加減乘除也要定義清楚。

機率體系是一個三元組（triple）：
1. **Sample space（樣本空間）** $\Omega$：所有可能出現的結果。骰子就是 1 到 6 點，不可能出現別的。
2. **Event space** $\mathcal F$：要處理的集合（event）們，要有合理的操作規則——就是 σ-field。
3. **Probability measure（機率測度）** $P$：量每個 event 的機率。

---

## 2. σ-field 的三個公設

[▶ 03:05](https://youtu.be/wjEbKHV6UAg?t=185)

**Definition B.1（σ-field，σ-algebra）**（p. 273）：$\mathcal F$ 是非空集合 $\Omega$ 的一些子集合組成的集合，若
1. $\Omega\in\mathcal F$；
2. **對補集封閉（closed under complementation）**：$A\in\mathcal F\Rightarrow A^c\in\mathcal F$；
3. **對可數聯集封閉（closed under countable unions）**：$A_i\in\mathcal F$（$i=1,2,3,\dots$）$\Rightarrow\bigcup_{i=1}^\infty A_i\in\mathcal F$。

**每一條的理由**（【口頭】）：
1. 「出現 1 到 6 點中某一點」的機率一定知道（100%），所以 $\Omega$ 一定在可操作的範圍內。
2. 能量「2、4、6 點」的機率（例如 0.8），就一定能量「1、3、5 點」的機率（0.2）——機率總和是 1。關心偶數時，潛意識裡也關心奇數。
3. 常常要處理事件的聯集：「明天下雨」或「股票漲」。聯集要在可操作範圍內，規則就要寫明。

**公設要越精簡越好** [▶ 07:13](https://youtu.be/wjEbKHV6UAg?t=433)：有的書還會寫「$\emptyset\in\mathcal F$」，但不需要：
- $\Omega\in\mathcal F$，由第 2 條，$\Omega^c=\emptyset\in\mathcal F$。
- 交集也不用寫：由 De Morgan 定律
$$\bigcap_{i=1}^\infty A_i=\left(\bigcup_{i=1}^\infty A_i^c\right)^c,$$
每個 $A_i^c\in\mathcal F$（第 2 條），聯集在 $\mathcal F$（第 3 條），再取補集還在 $\mathcal F$（第 2 條）。

【口頭】公設像法律條文，有一種潔癖：每一條都不可取代；如果某一條能用其他幾條證出來，就拿掉。這三條少一條，操作體系就不完美。

---

## 3. 最大和最小的 σ-field

[▶ 08:15](https://youtu.be/wjEbKHV6UAg?t=495)

- **最大**：$\Omega$ 的所有子集合，叫 **power set（冪集）**，記 $2^\Omega$。
  - 為什麼叫 power：子集合個數是指數。$\{1,2,3\}$ 的子集合有 $2^3=8$ 個（每個元素可要可不要）；四個元素有 16 個。
- **最小**：$\{\Omega,\emptyset\}$。三條都檢查得過：$\Omega$ 在裡面；兩者互為補集；聯集還是自己。最小的沒什麼用，只是幫助理解。
- **稍微有用的**：$\{\Omega,\emptyset,A,A^c\}$ 也是 σ-field。

【課本補充】課本（p. 273）：若 $A$ 是 $\Omega$ 的非空真子集，包含 $A$ 的**最小** σ-field 就是 $\{\Omega,\emptyset,A,A^c\}$。

無限集合也可以這樣定義 power set，只是沒辦法列出來。

---

## 4. 為什麼一定是 countable

[▶ 10:46](https://youtu.be/wjEbKHV6UAg?t=646)

無限大要分**可數（countable）**和**不可數（uncountable）**。第 3 條的 **countable** 很重要，不能拿掉：如果改成「對不可數聯集封閉」，量度時會量不出來——不可數個集合的和是 indeterminate（不確定）。【口頭】老師說在另一門課講得比較清楚，修實變分析也會知道。

---

## 5. 機率測度的三個公設

[▶ 11:46](https://youtu.be/wjEbKHV6UAg?t=706)

**Definition B.2（機率空間）**（p. 274）：三元組 $(\Omega,\mathcal F,P)$。$P:\mathcal F\to[0,1]$ 滿足
1. $0\le P(A)\le1$，對所有 $A\in\mathcal F$；
2. $P(\Omega)=1$；
3. **Countable additivity（可數可加性）**：$A_1,A_2,\dots$ 是 $\mathcal F$ 中**兩兩不相交**的集合（$A_i\cap A_j=\emptyset$，$i\ne j$），則
$$P\left(\bigcup_{k=1}^\infty A_k\right)=\sum_{k=1}^\infty P(A_k).$$

由這三條直接得到 $P(\emptyset)=0$。$\mathcal F$ 通常叫 **event space**，它的元素叫 **event**。

**理由**（【口頭】）：
1. 100% 一定發生、0% 一定不會發生，所有可能在中間（「1000%」是文學誇飾，不是數學）。
2. 涵蓋所有可能時，機率是 100%。
3. 骰子例子：「2、4 點」和「1、3 點」沒有交集，所以聯集的機率 = 各自機率相加。

**為什麼還是 countable** [▶ 12:46](https://youtu.be/wjEbKHV6UAg?t=766)：
- 0 加可數無限多次，答案是 0，數學上完全正確。
- 但如果對每個 $\varepsilon\in[0,1]$（不可數）都有一個 $a_\varepsilon=0$，把它們「全部加起來」——不可數個 0 加起來是多少，答案不知道。不小心就會出這種問題。
- 工程上也只能算可數個數的總和。

**Sub-additivity** [▶ 14:18](https://youtu.be/wjEbKHV6UAg?t=858)（【口頭】）：
- 所有工程和 information theory 的書都用 countable additivity（等號）。
- 但有機率學家改用不等號（sub-additivity）重新定義機率空間；老師的指導教授的論文就討論過。有些體系需要它：個別量再加起來，會比整包一起量多——例如量子世界有時「莫名其妙會多出來」。
- 通訊講的是**巨觀**、大數法則，在巨觀和數量很大的體系裡，都是等號。

---

## 6. Borel σ-field

[▶ 15:48](https://youtu.be/wjEbKHV6UAg?t=948)

工程上討論的都是實數。實數上常用的 σ-field 叫 **Borel σ-field**（Borel 是數學家）。

**定義**（課本 p. 274）：$\mathcal B(\mathbb R)$ 是包含 $\mathbb R$ 中**所有開區間**的**最小** σ-field。它的元素叫 **Borel set**。

**為什麼只寫開區間** [▶ 16:48](https://youtu.be/wjEbKHV6UAg?t=1008)：由 σ-field 的公設，開區間進來，閉區間、半開半閉區間自然就進來。
- 例：開區間 $(3,3.1)$ 在裡面，它的補集 $(-\infty,3]\cup[3.1,\infty)$ 也在裡面，再配合可數聯集、交集，各種區間都會進來。

**為什麼只用區間** [▶ 17:19](https://youtu.be/wjEbKHV6UAg?t=1039)：
- 我們只能在區間上量度、積分：區間 $(3,3.1)$ 的長度就是右端減左端 = 0.1。積分就建立在這種量度上。
- 存在不能用區間（或區間的可數聯集）表示的實數集合，已經有人造出來了。對那種集合做積分會出問題。
- 【口頭】二維的區間是正方形。不規則形狀量面積，可以用正方形去切、去逼近：**Riemann integral** 這樣做；用區間去逼近的、現在最廣的是 **Lebesgue integral**。重點：**我們只能處理區間，而且是可數個區間的聯集**（因為第 3 條是 countable union）。

> ⚠️ 待確認：[▶ 15:48](https://youtu.be/wjEbKHV6UAg?t=948) 和 [▶ 12:46](https://youtu.be/wjEbKHV6UAg?t=766) 老師說「呼應剛剛那個同學（問的問題）」，但同學的問題沒有錄到，無法寫成 Q&A；[▶ 04:07](https://youtu.be/wjEbKHV6UAg?t=247) 也突然插入一段解釋 $\sup_{k\ge n}a_k$ 記號（＝ $a_n,a_{n+1},\dots$ 的最大值）的話，可能是回答同學對上一集的提問。

---

## 7. 隨機變數：映射到實數

[▶ 18:52](https://youtu.be/wjEbKHV6UAg?t=1132)

**定義**（課本 p. 274）：定義在機率空間 $(\Omega,\mathcal F,P)$ 上的**隨機變數** $X$ 是實數值函數 $X:\Omega\to\mathbb R$，而且是 **measurable（可測，$\mathcal F$-measurable）** 的：
$$X^{-1}\left((-\infty,t]\right):=\{\omega\in\Omega:\ X(\omega)\le t\}\in\mathcal F,\quad\text{對每個實數 }t.$$

**為什麼要映射到實數** [▶ 19:23](https://youtu.be/wjEbKHV6UAg?t=1163)（【口頭】）：
- 叫「變數」是因為像代數裡要解的 unknown；叫「隨機」是因為有機率。
- $\Omega$ 可以是抽象集合，不必是數字。例如硬幣的正面、反面：沒有排序、不能加減。動物園裡第一個看到豬、貓、狗、羊的機率也一樣，動物不能排序。
- 工程上需要操作，所以把它映射到實數：正面 ↦ 0、反面 ↦ 1。之後就有 $1>0$ 可以排序，甚至做加減乘除。就像人要有身分證號碼，才能用電腦做很多操作。
- 實數才能比較大小，所以能寫 $X(\omega)\le t$。「正面 ≤ 3」很奇怪。

**例子** [▶ 21:28](https://youtu.be/wjEbKHV6UAg?t=1288)：正面 ↦ 0、反面 ↦ 1。$\{\omega: X(\omega)\le0.5\}$ 就是「正面」這個集合。這個集合要能量機率——這就是可測的意思。

**Inverse mapping 與 Borel set** [▶ 22:29](https://youtu.be/wjEbKHV6UAg?t=1349)：注意定義裡看的是區間 $(-\infty,t]$。一般來說，實數集合 $B$ 要能量機率，$B$ 必須是區間的可數聯集（Borel set）：
$$P_X(B):=\Pr[X\in B]=P\left(\omega\in\Omega:\ X(\omega)\in B\right),\qquad B\in\mathcal B(\mathbb R).$$
這個機率要回頭看原來的機率空間，因為 $X$ 是一個 mapping。

【課本補充】課本（p. 274）：$P_X(B)$ 對所有 Borel set $B$ 完全決定了 $X$，因為它決定了所有和 $X$ 有關的 event 的機率。

【口頭】大二機率直接給高斯的 pdf $\frac1{\sqrt{2\pi}\sigma}e^{-x^2/(2\sigma^2)}$，從來不講體系，因為那時還不需要 random process。

---

## 8. 隨機過程：同一個機率空間

[▶ 23:30](https://youtu.be/wjEbKHV6UAg?t=1410)

繞這一大圈，是為了讓 random process **well-defined（定義良好、數學上沒有缺陷）**。【口頭】就像公設要沒有缺陷，證到最後出現矛盾的公設就不能用。哲學也一樣：老子、孔子對天地各有說法，但各自不能自相矛盾。

**定義**（課本 p. 275）：**隨機過程（random process，random source）** 是**來自同一個機率空間**的一群隨機變數：
$$\{X_t,\ t\in I\},$$
$I$ 是 index set（可以任意）。

- 例：$I=\{1,2,3,4,5\}$，就看 $X_1,\dots,X_5$。
- 通訊一定要講序列：手機不會只用一次，會用好幾年。
- **Keyword：the same**。每個隨機變數一定要定義在**相同的**機率空間上，這樣才有數學上的完備性。

**index set 的種類** [▶ 25:37](https://youtu.be/wjEbKHV6UAg?t=1537)：
- $I$ 不可數（例如 $I=\mathbb R$）：**continuous-time** random process，例如量到的通訊波形。每個 $X_{1.3}$、$X_{2.6}$ 都是隨機變數。這門課只有第 5 章討論。
- 大部分討論 **discrete-time**：$I=\{1,2,\dots\}$，$X=\{X_n\}_{n=1}^\infty$。
- $I$ 只有一個元素（例如 $X_3$）：單一隨機變數。
- $I$ 有限（例如 $\{1,2,3\}$）：三維的 **random vector**。
- 重要的是連續無限多個：random process。

**為什麼要透過同一個機率空間？** [▶ 26:40](https://youtu.be/wjEbKHV6UAg?t=1600)
1. $\Omega$ 是抽象的，常常 **non-observable（看不到）**。例：量子裡電子正轉還是反轉，不是你直接看到的；儀器量出 $-1$、$+1$、$+2$、$-2$ 這些數字。真正發生機率的是裡面的 $\omega$。
2. **真正的重點**：只有這樣定義，random process 的 **joint distribution 才 well-defined**。

**說明** [▶ 27:41](https://youtu.be/wjEbKHV6UAg?t=1661)：給定 $(\Omega,\mathcal F,P)$，$X_1,X_5,X_9,\dots$ 都是 $\Omega\to\mathbb R$ 的 mapping。
- 這樣定義完，**不需要**再告訴你 $X_1$ 和 $X_5$、$X_1$ 和 $X_9$ 的關係——已經完整定義了。
- random process 有無限多個隨機變數，兩兩、三三、四四之間的關係不可能一一列出來。
- 要算 $\Pr[X_1=x_1,X_5=x_5,X_9=x_9]$：真正的機率發生在 $\Omega$，看集合
$$\{\omega:X_1(\omega)=x_1\}\cap\{\omega:X_5(\omega)=x_5\}\cap\{\omega:X_9(\omega)=x_9\}.$$
每個集合都在 $\mathcal F$ 裡（可測），三個的交集也一定在 $\mathcal F$（σ-field 公設），所以機率一定量得出來。

【課本補充】random vector $X^n=(X_1,\dots,X_n)$ 的聯合 cdf（p. 275）：
$$F_{X^n}(x^n)=P\left(\omega\in\Omega:\ X_i(\omega)\le x_i,\ i=1,\dots,n\right).$$
有限字母的 source 可以等價地用一串聯合 pmf 描述（p. 276）：$P_{X^n}(a^n)=\Pr[X_1=a_1,\dots,X_n=a_n]$，$n=1,2,\dots$。

---

## 9. 為什麼大二機率不用講機率空間

[▶ 29:43](https://youtu.be/wjEbKHV6UAg?t=1783)

1. 那時還沒有 random process 的需求，不用看無限多個隨機變數之間的聯合分布。
2. 有一個定理：給一個 random process（或一個 cdf），**一定能造出一個機率空間**讓它 well-defined。所以機率空間是**隱含存在**的。只要你能列出所有可能（所有聯合分布），就不必提機率空間。

【課本補充】課本 Observation B.3（p. 275）：給任一非負、非遞減、右連續、$\lim_{x\downarrow-\infty}F(x)=0$、$\lim_{x\uparrow\infty}F(x)=1$ 的函數 $F$，存在一個隨機變數和底層機率空間，使它的 cdf $\Pr[X\le x]$ 等於 $F$。所以可以直接用 cdf 定義隨機變數；但形式上，隨機變數還是定義在機率空間上。

**例子** [▶ 30:45](https://youtu.be/wjEbKHV6UAg?t=1845)：random process 的每個隨機變數**彼此獨立**、取值 0 或 1、機率各 $\frac12$。這樣就把所有可能講完了。
- 問：$\Pr[X_1=0,X_5=1,X_9=0]$？雖然沒直接告訴你，但由獨立性，
$$\Pr[X_1=0,X_5=1,X_9=0]=\tfrac12\cdot\tfrac12\cdot\tfrac12=\tfrac18.$$
- 能列出所有聯合分布，就不用提機率空間；它隱含在裡面，一定存在。

**CDF** [▶ 31:46](https://youtu.be/wjEbKHV6UAg?t=1906)：cumulative distribution function 是右連續（right continuous）、非遞減、左端 0、右端 1。複雜的體系列不出所有聯合分布時，還是要把最原始的機率空間寫出來。

---

## 10. 不映射到實數的情形

[▶ 32:16](https://youtu.be/wjEbKHV6UAg?t=1936)

有些書討論不映射到實數的隨機變數。問題是：沒辦法排序，就沒辦法畫 CDF。
- 例：正面 ↦ ×、反面 ↦ ○。你還是不知道 × 和 ○ 能不能相加、能不能排序，要另外告訴我它們的操作關係。
- 例：台北市男生比例 50.1%、女生 49.9%，你可能只想表示「男／女」的概念，而不是 ±1 或 1、0。但畫圖總要排列。
- **CDF 一定要能比較大小**：任何隨機變數都要給 CDF（pdf 是它的微分），所以要能排序。實數是完備的、能排序、能加減乘除，所以早期的隨機變數都映射到實數。
- 複數不能排序（$1+i$ 和 $1-i$ 誰大？），硬要排序可能產生理論上的小缺陷；通常把它當二維實數。
- 【口頭】老師以前研究英文字母的出現機率（做英文文件的資料壓縮），映射出來的是英文字母不是數字。排序不難，因為字母有約定俗成的順序 A、B、C、D；中文字就比較麻煩，每個人排法不同。（影片在這裡結束。）

【課本補充】課本 p. 276 註 2：更一般地，隨機變數可以是 $X:\Omega\to\mathcal X$，$\mathcal X$ 是一般集合，配一個 σ-field $\mathcal F_{\mathcal X}$，要求每個 $F\in\mathcal F_{\mathcal X}$ 都有 $X^{-1}(F)\in\mathcal F$。取 $\mathcal X=\mathbb R$ 就回到標準定義。有限字母的 source，字母可以用任何有限集合表示，不必是實數。

---

## 11. 一頁速查表

**σ-field**（三條，缺一不可）
1. $\Omega\in\mathcal F$；2. $A\in\mathcal F\Rightarrow A^c\in\mathcal F$；3. 可數聯集封閉。
- 推得：$\emptyset=\Omega^c\in\mathcal F$；$\bigcap A_i=\left(\bigcup A_i^c\right)^c\in\mathcal F$。
- 最大 $2^\Omega$（$|\Omega|=3$ 時有 8 個子集合）；最小 $\{\Omega,\emptyset\}$；含 $A$ 的最小 $\{\Omega,\emptyset,A,A^c\}$。

**機率測度**
$0\le P(A)\le1$；$P(\Omega)=1$；不相交 ⇒ $P\left(\bigcup A_k\right)=\sum P(A_k)$（countable additivity）。推得 $P(\emptyset)=0$。
- 為什麼 countable：不可數個 0 相加沒有定義。

**Borel σ-field** $\mathcal B(\mathbb R)$：含所有開區間的最小 σ-field；閉、半開區間自動在內。只能量區間（的可數聯集）。

**隨機變數**：$X:\Omega\to\mathbb R$，$\{\omega:X(\omega)\le t\}\in\mathcal F$ $\forall t$。$P_X(B)=P(X^{-1}(B))$。映射到實數是為了排序、運算、畫 CDF。

**隨機過程**：$\{X_t,t\in I\}$，**定義在同一個機率空間** ⇒ 所有聯合分布自動 well-defined（交集在 $\mathcal F$ 裡）。
- $I$ 有限：random vector；$I=\{1,2,\dots\}$：discrete-time；$I=\mathbb R$：continuous-time。

**Observation B.3**：任何合法的 cdf 都有對應的機率空間 ⇒ 能列出所有聯合分布就不必提機率空間。例：i.i.d. Bernoulli(1/2) ⇒ $\Pr[X_1=0,X_5=1,X_9=0]=\frac18$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| random process、shift、統計性質（stationary、Markov…） | 第 6 集（§B.3） |
| ergodicity、大數法則、中央極限定理 | 第 7 集（§B.5–B.6） |
| 離散隨機變數、pmf、entropy | 第 8 集起（第 2 章） |
| i.i.d. source（DMS） | 第 12 集（第 3 章） |
| continuous-time random process | 第 22–26 集（第 5 章） |

---

## 附：本集一句話總結

> **機率體系是 $(\Omega,\mathcal F,P)$：σ-field 規定哪些集合能量、機率測度規定怎麼量，兩者都用最精簡的公設；隨機變數把抽象的 $\omega$ 映射到能排序的實數，而隨機過程的所有隨機變數必須住在同一個機率空間，聯合分布才自動定義良好。**

---

## ⚠️ 待確認清單

1. [▶ 12:46](https://youtu.be/wjEbKHV6UAg?t=766) 老師兩次提到「呼應剛剛那個同學（問的問題）」，以及 [▶ 04:07](https://youtu.be/wjEbKHV6UAg?t=247) 突然解釋 $\sup_{k\ge n}a_k$ 記號，同學的問題本身沒錄到，無法寫成 Q&A。

---

*筆記依據陳伯寧老師「消息理論」Lec05 錄影逐字稿（whisper large-v3-turbo，34:51）與 Alajaji & Chen 課本附錄 B §B.1–B.2 整理。*
