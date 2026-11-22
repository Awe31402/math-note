---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 32
lecture: Lec32 第二部分 Preface and Introduction；Chapter 1 Generalized information measures for arbitrary systems with memory
date: 待補
video: https://youtu.be/0xfSWofioio
notes: 第二部分（information spectrum）課本沒有，只依逐字稿；名詞對照課本參考文獻 [172] Han、[396] Verdú–Han
---

# 第 32 集 · Lec32 第二部分第 1 章：任意系統的廣義資訊量（spectrum、quantile、inf／sup rate）[▶ 影片](https://youtu.be/0xfSWofioio)

← 上一集：[31](31-shannon-limit-communication-systems.md) ｜ [總目錄](README.md) ｜ 下一集：[33](33-general-data-compression-theorems.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 32 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（55:33，whisper large-v3-turbo）。這一集是第二部分，**課本沒有**，數學式依老師口述與投影片描述重建
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：開頭「文化學歷史……教授」是亂碼。「triangular array」正確，「Billingsley」聽成「Biliensly」，「quantile」聽成「框台／匡台／框材」，「percentile」正確，「supremum」聽成「Supremant／supplement」，「Proakis」聽成「Prokeys」，「傅立葉轉換」聽成「負列轉換／inverse friction form」，「Neyman–Pearson」聽成「Newman-Pearson」，「Chernoff」聽成「Churnoff」，「output statistics」聽成「Opus Statistic」，「高斯」聽成「高圈／高宣」，「QAM」聽成「框」，「Shannon」聽成「Shanen」，「step function」聽成「State Function」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 觀念：看的是「機率代入的函數」](#1-觀念看的是機率代入的函數)
- [2. 為什麼要推廣：沒有 typical set 了](#2-為什麼要推廣沒有-typical-set-了)
- [3. 最廣義的模型：triangular array](#3-最廣義的模型triangular-array)
- [4. Spectrum 與 quantile](#4-spectrum-與-quantile)
- [5. Inf／sup spectrum、liminf／limsup in probability](#5-infsup-spectrumliminflimsup-in-probability)
- [6. 三個例子：entropy、information、divergence rate](#6-三個例子entropyinformationdivergence-rate)
- [7. 性質：DPI、獨立輸入最佳](#7-性質dpi獨立輸入最佳)
- [8. 插曲：output statistics](#8-插曲output-statistics)
- [9. 例一：二元加性雜訊通道](#9-例一二元加性雜訊通道)
- [10. 例二：雜訊會瞬間消失](#10-例二雜訊會瞬間消失)
- [11. 例三：non-stationary 的獨立雜訊](#11-例三non-stationary-的獨立雜訊)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】第二部分感覺理論性很深，有點像進到相對論的時代；但介紹之後會發現概念不難。

未來的統計現象**有 memory**（和過去有強烈的連結）、**不再 identically distributed**（每次機率都可能變，arbitrary）。在這種環境下，怎麼得到有操作意義的理論？本集先定義工具：
- **triangular array**（最廣義的模型）、
- **spectrum**（完整的統計描述，就是 CDF）、**quantile**、
- **inf／sup spectrum**、**liminf／limsup in probability**，
- 並用它們定義 **inf／sup entropy rate、information rate、divergence rate**，最後算三個二元通道的例子。

---

## 1. 觀念：看的是「機率代入的函數」

[▶ 00:32](https://youtu.be/0xfSWofioio?t=32)

【口頭】統計時不會直接拿觀察值分析，而是代入一個**對的函數**。
- 民調：支持記 1、不支持記 0，平均的是這個函數值。
- 通訊上，對的函數是**機率**：擲骰子觀察到 3 點，用的不是「3」這個值，而是「3 點發生的機率」。骰子六面畫的是 1～6 點，還是一隻豬、一隻羊、一隻孔雀，都不重要。用 ±1 還是 0、2 傳，capacity 都一樣。
- 對 Shannon 來說，三大公設告訴我們函數是「**機率倒數取 log**」——所以要看的是這個量的 CDF。

**記號：真的機率 vs. 代入的機率**：$P_X$ 是真正發生的機率，但代入函數的可以是**另一個**機率 $P_{\hat X}$（另一個人誤認的分布）。例：公平骰子每面 $\frac16$，但你代入 $\left(\frac14,\frac12,\frac14,0,\dots\right)$。誤認機率在操作上要付出代價，這個代價由對應的 CDF 完全決定。（例如 $P_{XY}$ 是真的，代入的是 $P_{\hat X\hat Y}$。）

---

## 2. 為什麼要推廣：沒有 typical set 了

[▶ 05:05](https://youtu.be/0xfSWofioio?t=305)

- Shannon 的 entropy 是**期望值**；資料壓縮的極限是 $\frac1nH(X^n)$ 收斂到的值——前提是大數法則、極限存在。
- Stationary ergodic 沒問題；但 **time-varying 或 non-stationary** 時，typical set 不能用了：不再存在一個很小、佔很大機率、裡面每個元素一樣重要的集合，證明都不能用。
- 要推廣，就推廣到**最廣義的統計現象**；重點仍是能解釋工程上的操作現象。

**兩個 index**【口頭】：90 年代開始想，統計現象可能有兩個 index——一個是時間 $t$、一個是空間 $n$（多天線），是二維的統計事件。問題一樣：區塊變大時，**最好的壓縮率**是多少？

---

## 3. 最廣義的模型：triangular array

[▶ 07:06](https://youtu.be/0xfSWofioio?t=426)

【口頭】機率書（例如 Billingsley）都有一章講 **triangular array**：
- 你決定每 10 個觀察處理一次，收到 $X_1^{(10)},\dots,X_{10}^{(10)}$；另一個人 buffer 大、每 20 個處理一次，收到 $X_1^{(20)},\dots,X_{20}^{(20)}$。兩者的統計現象可以**不一樣**（處理的區塊大，黏滯性可能不同）。
- **Sequence**（傳統）：把 20 維的分布積分掉其中 10 維，會回到原來的 10 維分布（consistent，是 marginal）——一個維度一直往上延伸。
- **Triangular array**：積分掉之後**不一定**回到原來的分布，所以要用上標 $X^{(n)}=\left(X_1^{(n)},\dots,X_n^{(n)}\right)$ 標出區塊長度。排起來是三角形，所以叫 triangular array。
- 上標沒有排除傳統情形（是 marginal 也沒關係）。
- 這種模型叫 **arbitrary system**。【口頭】很幸運，這樣反而不會造成分析困難——因為它是觀念。

---

## 4. Spectrum 與 quantile

[▶ 11:41](https://youtu.be/0xfSWofioio?t=701)

**Spectrum** 原意是**光譜**：白光經過三稜鏡，把紅橙黃綠藍靛紫拉開，並告訴你每種顏色佔多少能量——**完整的解釋**。
- 機率上：骰子的六個機率全部告訴你（少一個可以，因為和為 1；少兩個就不完整），就是完整的統計描述。用 **CDF**（累積量）表示也一樣，可以還原每個機率。所以 CDF 也叫 spectrum。
- 通訊的頻譜也叫 spectrum：時域訊號經傅立葉轉換到頻域，每個頻率的分量都告訴你，經反轉換完全還原，沒有資料損失。

**Quantile**（和 **percentile** 類似）：
- Percentile：從機率的角度把事件切成 100 份，每份機率 1%。
- Quantile：在 **y 軸（機率）上均勻切割**，再對回 x 軸。例如切 10 等份，每一段 x 範圍的機率都是 $\frac1{10}$。
- 【口頭】為什麼要介紹：**從 quantile 拉回來就是傳輸量**——在錯誤率 $10^{-5}$ 處拉一條水平線，對回 x 軸，就是存在操作方法能達到的傳輸速度或壓縮極限。

**定義**：$A_n$ 是一個隨機變數（之後會是 $\frac1n\log\frac1{P_{Z^n}(Z^n)}$ 這類量），它的 spectrum 是 $\Pr[A_n\le\theta]$。【口頭】選「機率倒數取 log、再取 $\frac1n$」是因為三大公設告訴我它和 information 量有關；別的問題要找自己的公設、自己最關心的量。

---

## 5. Inf／sup spectrum、liminf／limsup in probability

[▶ 16:46](https://youtu.be/0xfSWofioio?t=1006)

**為什麼要 inf 和 sup**【口頭】：Verdú 他們的論文舉過一個循環性的通道：早上、下午、晚上不一樣，但早上和隔天早上很像。$n=10$ 可能早上就送完，$n=20$ 涵蓋到下午，$n=30$ 涵蓋到晚上，$n=40$ 又回到早上。於是 $n=10,40,70,\dots$ 收斂到一條 CDF，$n=20,50,80,\dots$ 收斂到另一條。取 liminf 和 limsup，把最大和最小都拉進來——是一個**範圍**。

**Inf／sup spectrum**（依口述重建）：
$$\underline u(\theta):=\liminf_{n\to\infty}\Pr[A_n\le\theta],\qquad\bar u(\theta):=\limsup_{n\to\infty}\Pr[A_n\le\theta].$$

**Quantile**（CDF 不一定有反函數，所以用 quantile）：
$$\underline U_\delta:=\sup\{\theta:\underline u(\theta)\le\delta\},\qquad\bar U_\delta:=\sup\{\theta:\bar u(\theta)\le\delta\}.$$
- 【口頭】CDF 遞增，畫一條水平線，小於它的都在一邊。取**小於等於 $\delta$ 的最大值**，而且用 **sup** 不用 max——因為極限可能不連續、會跳。古典的 Shannon 定理就是不連續（只收斂到一點），水平線在 $10^{-5}$ 處和曲線沒有交點，只能取 sup。

**兩個操作上的指標**：
$$\underline U:=\text{liminf in probability}=\sup\left\{\theta:\lim_{n\to\infty}\Pr[A_n<\theta]=0\right\},$$
$$\bar U:=\text{limsup in probability}=\inf\left\{\theta:\lim_{n\to\infty}\Pr[A_n>\theta]=0\right\}.$$
- $\underline U$：分布的**最左端**（往左一點點機率都是 0）——錯誤率要**任意小**（arbitrarily small，reliable transmission）時，最廣義情況下能達到的傳送量。
- $\bar U$：分布的**最右端**——超過它就不要想了，錯誤率都是 1。
- 記號：上面一槓（bar）是比較大的、下面一槓（underbar）是比較小的。$\delta\to0$ 時 $\underline U_\delta\to\underline U$。

【口頭】
- 廣義的 big data 分析，資料量那麼大，怎麼保證每筆都獨立？所以大部分都是散開的，但你知道一個範圍——這是觀念上很重要的突破。
- 老師曾被統計年會邀去演講，他們還不太能理解，主要因為能和操作扯上關係的範例不多；通訊已經把這個觀念和操作完全等效。
- 課本（講義）裡有兩個隨機變數相加時 underbar／superbar 之間關係的定理（雜訊會加在一起），課堂跳過。

> ⚠️ 待確認：上面 $\underline u,\bar u,\underline U_\delta,\bar U_\delta,\underline U,\bar U$ 的精確寫法是依口述和 Han 的 information-spectrum 慣例重建；老師講義的原式（例如 $\le$ 或 $<$、是否用 $\sup$）沒有看到。

---

## 6. 三個例子：entropy、information、divergence rate

[▶ 26:27](https://youtu.be/0xfSWofioio?t=1587)

把 $A_n$ 換成對的量，就得到有操作意義的量：

| $A_n$ | 名稱 | 操作意義 |
|---|---|---|
| $\frac1n\log\frac1{P_{X^n}(X^n)}$（**entropy density**） | inf／sup **entropy rate** $\underline H(X)$、$\bar H(X)$；$\underline H_\delta$、$\bar H_\delta$ | 壓縮極限 |
| $\frac1n\log\frac{P_{X^nY^n}(X^n,Y^n)}{P_{X^n}(X^n)P_{Y^n}(Y^n)}$（**information density**） | inf／sup **information rate** $\underline I(X;Y)$、$\bar I(X;Y)$ | 傳輸極限 |
| $\frac1n\log\frac{P_{X^n}(X^n)}{P_{\hat X^n}(X^n)}$（normalized **log-likelihood ratio**） | inf／sup **divergence rate** | hypothesis testing 的 error exponent |

- 【口頭】「mutual」字太多，所以簡稱 **information rate**；它是傳送端和接收端共有的 information。
- 【口頭】Density 指的是機率密度——想知道這個量發生每個值的機率。圖的 y 軸是機率（0 到 1），**x 軸是操作量**：找對了函數，從 quantile 對回 x 軸就是實際的結果（壓縮量、傳輸量）。
- 【口頭】Log-likelihood ratio：Neyman–Pearson lemma 說它是 detection 的基本量；Chernoff–Stein 說它代表 Neyman–Pearson 最好的 error exponent。廣義時 error exponent 也是一個範圍。
- 重要的兩個量：$\underline H$ 和 $\bar H$——帶狀的最左端和最右端（對應 $\bar H_\delta$ 在 $\delta\to1$ 和 $\underline H_\delta$ 在 $\delta\to0$ 的極限）。

**批評：只在 $n\to\infty$**【口頭】[▶ 30:04](https://youtu.be/0xfSWofioio?t=1804)：這些都發生在 $n$ 趨近無限大（Shannon 的 typical set 也是）。超過極限時 $n$ 很大所有方法都很差，但 $n$ 小時說不定可以偷一點——現在有人在做 **finite-length information theory**，找一個小小的 niche。現在有些通訊傳輸長度很短，現象不太一樣。

---

## 7. 性質：DPI、獨立輸入最佳

[▶ 31:04](https://youtu.be/0xfSWofioio?t=1864)

**古典 vs. 廣義**：
- 古典：$I(X;Y)=H(Y)-H(Y|X)=H(X)+H(Y)-H(X,Y)$，Venn 圖解釋共有的連動。
- 廣義：$\underline I(X;Y)$ 是 information density 分布的最左端。例如 $\underline I=2.1$ bit/次，送 2.0 就一定做得到、錯誤率任意小。但它**不再等於** $H(Y)-H(Y|X)$ 這種形式，只有不等式，大約是
$$\underline H(Y)-\bar H(Y|X)\le\underline I(X;Y)\le\cdots$$
  ——因為分布拉開了（arbitrary statistics），會落在中間。

> ⚠️ 待確認：[▶ 32:37](https://youtu.be/0xfSWofioio?t=1957) 老師說 $\underline I$「會小於等於……underbar 減掉 underbar……扣掉 superbar，會在中間」，不等式的完整形式（哪一邊是上界、哪一邊是下界）逐字稿不清楚。

**檢驗量對不對**：必須完全符合操作經驗。
- **Data processing lemma**：$X\to Y\to Z$，$\underline I(X;Y)\ge\underline I(X;Z)$（對 quantile 也成立）——$Z$ 對 $X$ 的了解是透過 $Y$ 傳話，共識不會比較高。用機率就能直接證明。
- **Optimality of independent input**：雜訊（通道）若每個時間獨立，讓 $\underline I$ 最大的輸入只要**獨立**就夠了，不需要考慮 dependent。【口頭】又是「要對抗雜訊，就要長得像雜訊」：雜訊高斯 ⇒ 高斯輸入；雜訊獨立 ⇒ 獨立輸入。
- 【口頭】Water-filling 和經驗不符，是因為假設了高斯輸入——實際是 BPSK、QPSK，數學很漂亮但答案不對。公式一定要符合你的應用情境。

---

## 8. 插曲：output statistics

[▶ 38:40](https://youtu.be/0xfSWofioio?t=2320)

Information density 常寫成
$$\frac1n\log\frac{P_{Y^n|X^n}(Y^n|X^n)}{P_{Y^n}(Y^n)},$$
它完全由輸出端決定。【口頭】
- 數學上：量測到通道 $P_{Y^n|X^n}$，假設一個輸入分布，得到 joint，積分掉 $X^n$ 得到 $P_{Y^n}$——純數學。
- 實際上**沒有輸入分布**：送的是 BPSK、QPSK、16-QAM 這種 deterministic 的對應（00 送 90°、01 送 180°），只是每點機率 uniform，於是得到一個實際的輸出分布 $Q_{Y^n}$。要達到 capacity，$Q_{Y^n}$ 要和達到 capacity 時的 $P_{Y^n}$ **很像**。
- 所以重點**在輸出不在輸入**：高斯雜訊下不必用高斯輸入，只要讓輸出長得像高斯。這叫 **output statistics**（有一篇論文就研究這個；課本參考文獻 [175] Han & Verdú, *Approximation theory of output statistics*）。
- 合理的解釋：錯誤率在輸出端決定，**receiver 比較重要**。兩個不同的輸入方法（±1、±3 vs. 90°、180°、270°、360°），若輸出端看到的統計現象一樣，效能就一樣。最後一集會講。

【口頭】有人研究輸入會改變雜訊的情形（某些記憶體存取裝置）、送 10 次只收到 8 次（輸入會消失）、送 10 次收到 12 個（多出來）的通道——都是少數應用，但有趣味；那時「雜訊和輸入獨立」的假設就不能用。

---

## 9. 例一：二元加性雜訊通道

[▶ 42:45](https://youtu.be/0xfSWofioio?t=2565)

**設定**：輸入、輸出、雜訊都是 0/1，$Y^n=X^n\oplus Z^n$，雜訊統計特性可以隨 $n$ 改變（arbitrary）、但和輸入獨立；輸入 uniform i.i.d.。

- 加性（可逆）：$P_{Y^n|X^n}(y^n|x^n)=P_{Z^n}(y^n\oplus x^n)$——給 $X$、給 $Y$ 就百分之百知道 $Z$。
- 輸入 uniform ⇒ 輸出 uniform：$P_{Y^n}(y^n)=2^{-n}$。
- 代入（自然對數）：
$$\frac1n\log\frac{P_{Y^n|X^n}(Y^n|X^n)}{P_{Y^n}(Y^n)}=\log2-\frac1n\log\frac1{P_{Z^n}(Z^n)}.$$
  information density = $\log2$ 減掉**雜訊的 entropy density**。

【口頭】傳輸量 = 1（bit 為單位）減掉雜訊的豐富程度：雜訊越散、越豐富，越難預測，對我影響越大；越集中越好。完全吻合實際概念。（這就是 entropy power 的概念：直接影響傳送量的是雜訊的 entropy。）

**計算 quantile**（依口述）：
$$\Pr\left[\log2-h_n(Z)\le\theta\right]=\Pr\left[h_n(Z)\ge\log2-\theta\right],\qquad h_n(Z):=\frac1n\log\frac1{P_{Z^n}(Z^n)}.$$
令 $\theta=\log2-\beta$，把常數 $\log2$ 提到 sup 外面、負號提出來 sup 變 inf；再把「大於等於一個數的最小值」改寫成「小於一個數的最大值」（連續時兩者相等），就變成雜訊 spectrum 的 quantile：
$$\text{（錯誤率 }\varepsilon\text{ 的傳輸量）}=\log2-\text{（雜訊 entropy spectrum 在 }1-\varepsilon\text{ 的 quantile）}.$$
最後用 $<$ 和 $\le$ 的差別得到上下界，結果是等號：最廣義的統計現象，定義對了也完全正確。

> ⚠️ 待確認：[▶ 44:48](https://youtu.be/0xfSWofioio?t=2688) 結果用的是 inf 還是 sup spectrum（$\underline H$ 還是 $\bar H$ 的 quantile）、下標是 $1-\varepsilon$ 還是 $\varepsilon$，逐字稿沒說清楚；以下**不是逐字稿內容**，是依「$\Pr[i\le R]=\Pr[h\ge\log2-R]$」推論的：錯誤率 $\varepsilon$ 下的傳輸量對應雜訊 entropy density 分布中「上尾機率為 $\varepsilon$」的那一點，即 CDF 在 $1-\varepsilon$ 的 quantile。

---

## 10. 例二：雜訊會瞬間消失

[▶ 47:52](https://youtu.be/0xfSWofioio?t=2872)

**設定**：雜訊有機率 $\beta$ 瞬間**全部是 0**（沒有雜訊），機率 $1-\beta$ 是一般的 Bernoulli($p$) i.i.d.——不再 i.i.d.、不再 stationary。【口頭】這樣的雜訊我們過去不知道怎麼傳，現在也不知道怎麼傳，但知道傳輸極限。

- 雜訊 entropy density $\frac1n\log\frac1{P(Z^n)}$ 的極限只有兩個值：全 0 時 → 0（機率 $\beta$）；否則 → $h_b(p)$（機率 $1-\beta$）。Spectrum 是兩階的階梯。
- Information density（bit）$=1-$（雜訊 entropy density）：值為 1（機率 $\beta$）或 $1-h_b(p)$（機率 $1-\beta$）。

**讀圖**（x 軸是操作量、y 軸是機率）：
- 錯誤率要求 $\varepsilon$ 很小：最多傳 $1-h_b(p)$ bit/次。
- 錯誤率可以放寬到 $1-\beta$ 以上（例如 $1-\beta+\varepsilon$）：**一定存在方法**每次傳 1 bit。

> 以下**不是逐字稿內容**，是依上面的分布推論的：rate $R<1-h_b(p)$ 時錯誤率可任意小；$1-h_b(p)<R<1$ 時最好的錯誤率是 $\Pr[\text{information density}\le R]=1-\beta$。

【口頭】怎麼做到還不知道，可能要花 50 年；但只要雜訊有瞬間為 0 的情形，操作極限就完全知道，目標很清楚。

---

## 11. 例三：non-stationary 的獨立雜訊

[▶ 50:55](https://youtu.be/0xfSWofioio?t=3055)

**設定**：$Z_1,Z_2,\dots$ **獨立**，但每個時間 1 的機率 $p_i$ 不一樣（早上、下午、晚上不同；例如 0.8、0.7、0.8、0.4……）。【口頭】就像高斯雜訊每個時間 variance 不一樣、SNR 隨時間變。90 年代以前，光這麼簡單的 binary channel 我們都無法理解；現在可以完全解釋。

- 獨立 ⇒ joint 還是乘積（只是每個不一樣：$0.8\times0.7\times0.8\times0.4\cdots$），取 log 相加；但 $p_i$ 沒有固定的極限，平均不一定收斂到一個常數，會集中到**好幾個**值。
- 例：奇數時間 $p_i=0.8$、偶數時間 $p_i=0.6$ ⇒ 極限是兩條 step function，一條在 $h_b(0.8)$、一條在 $h_b(0.6)$（最小和最大的 entropy）。一般可能有很多條，但都是 step function；集中點叫 **crossing point**。
- Capacity：$\log2$ 減掉雜訊的範圍。
  - 速度低於 $\log2-$（最大的雜訊 entropy）：一定存在方法，對**所有長度**錯誤率都趨近 0。
  - 速度高於 $\log2-$（最小的雜訊 entropy）：不可能，$n$ 大時所有方法都很差。
  - 中間：只有某些長度好——例如只看 $n=2,4,6,8,\dots$，不看 $1,3,5,7,\dots$（雜訊比較差的情況），要找剛好對齊到好狀態的特定長度。

（這就是 liminf／limsup 兩個極限點的操作意義。）

---

## 12. 一頁速查表

**觀念**：統計看的是「機率代入對的函數」的分布；information 的函數是 $\log\frac1P$。

**Triangular array**：$X^{(n)}=(X_1^{(n)},\dots,X_n^{(n)})$，不同區塊長度的分布不必 consistent；最廣義的 arbitrary system。

**Spectrum** = CDF（完整的統計描述）；**quantile** = 在 y 軸切、對回 x 軸（$\sup\{\theta:\text{CDF}(\theta)\le\delta\}$）。

**Inf／sup**：$\underline u(\theta)=\liminf\Pr[A_n\le\theta]$、$\bar u(\theta)=\limsup\Pr[A_n\le\theta]$；$\underline U$（liminf in prob.）= 分布最左端（錯誤率任意小的極限）、$\bar U$（limsup in prob.）= 最右端（超過則錯誤率 1）。

**三種 density → rate**：entropy density → $\underline H,\bar H$（壓縮）；information density → $\underline I,\bar I$（傳輸）；log-likelihood ratio → divergence rate（error exponent）。

**性質**：DPI 對 $\underline I$ 成立；無記憶通道下獨立輸入最佳；information density 寫成 $\log\frac{P_{Y|X}}{P_Y}$（output statistics：重點在輸出長得像）。

**例子**（二元加性雜訊，uniform 輸入）：information density $=\log2-$ 雜訊 entropy density。
- 雜訊有 $\beta$ 機率消失：$\varepsilon$ 小時 $1-h_b(p)$；錯誤率容許 $\ge1-\beta$ 時 1 bit。
- 奇偶時間 $p=0.8/0.6$：兩條 step，$\log2-h_b(\cdot)$ 的範圍；中間的 rate 只在特定長度可達。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Entropy density 的 spectrum ⇒ 一般 source 的壓縮定理 | 第 33 集（第 2 章） |
| 隨機過程的隨機性量度（resolvability 等） | 第 34 集（第 3 章） |
| Information density 的 $\underline I$ ⇒ 一般 channel 的 capacity；output statistics | 第 35 集（第 4 章） |

---

## 附：本集一句話總結

> **沒有大數法則時，把「機率倒數取 log」這類量的整個分布（spectrum）畫出來：用 triangular array 容許任意的統計，取 liminf／limsup 得到一個範圍，從 y 軸的錯誤率拉 quantile 對回 x 軸就是操作極限——entropy density 管壓縮、information density 管傳輸、log-likelihood ratio 管偵測。**

---

## ⚠️ 待確認清單

1. [▶ 16:46](https://youtu.be/0xfSWofioio?t=1006) inf／sup spectrum、quantile、liminf／limsup in probability 的精確定義是依口述與 Han 的慣例重建，沒有看到老師講義原式。
2. [▶ 32:37](https://youtu.be/0xfSWofioio?t=1957) $\underline I(X;Y)$ 和 $\underline H$、$\bar H$ 之間不等式的完整形式逐字稿不清楚。
3. [▶ 44:48](https://youtu.be/0xfSWofioio?t=2688) 例一的結果是 inf 還是 sup spectrum、下標是 $1-\varepsilon$ 還是 $\varepsilon$，逐字稿沒說清楚。

---

*筆記依據陳伯寧老師「消息理論」Lec32 錄影逐字稿（whisper large-v3-turbo，55:33）整理；第二部分課本沒有。*
