---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 7
lecture: Lec07 B.5 Ergodicity and law of large numbers, B.6 Central limit theorem, B.7–B.8
date: 待補
video: https://youtu.be/NCnA-2U5skE
notes: Alajaji & Chen 附錄 B §B.4–B.8（pp. 282–296，Definition B.6–Example B.20）
---

# 第 7 集 · Lec07 B.4–B.8：收斂模式、大數法則、中央極限定理、Jensen、KKT [▶ 影片](https://youtu.be/NCnA-2U5skE)

← 上一集：[06](06-statistical-properties-random-sources.md) ｜ [總目錄](README.md) ｜ 下一集：[08](08-self-information-entropy-mutual-information.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 7 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:09:41，whisper large-v3-turbo）＋ 課本附錄 B §B.4–B.8（pp. 282–296）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「ergodic」聽成「ergatic／Argardia」，「大數法則」聽成「大樹法則／大處法則」，「law of large numbers」聽成「law of large geometry」，「block length」聽成「Black Lens」，「趨近」聽成「區域」，「Chebyshev」聽成「Chevyshev」，「Kolmogorov」聽成「Komagorov／Comargo」，「Birkhoff」聽成「Burkhoff／Berkhoff」，「Khinchin」聽成「Kinchen／Kintin」，「monotone」聽成「Molotone」，「dominated」聽成「Dominate」，「Jensen」聽成「gensent／genc」，「Karush」聽成「Korech／Karach／Corrèche」，「multipliers」聽成「Multiply」，「duality」聽成「Duity」，「affine」正確，「原點」聽成「遠點」，「斜率」聽成「斜律」，「截距」聽成「焦點」，「極值」聽成「集值／即時」，「實數」聽成「時數」，「實變」聽成「十遍」，「高斯」正確，「AWGN」聽成「相加白色高知杂讯」。結尾 [69:33]「優優獨播劇場」是 whisper 幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：我們要的是 time average → ensemble average](#1-回顧我們要的是-time-average--ensemble-average)
- [2. Typical set 的精神](#2-typical-set-的精神)
- [3. 五種收斂模式](#3-五種收斂模式)
  - [3.1 Pointwise vs almost sure：四面骰子的例子](#31-pointwise-vs-almost-sure四面骰子的例子)
  - [3.2 Almost sure（先取極限再取機率）](#32-almost-sure先取極限再取機率)
  - [3.3 In probability（先取機率再取極限）](#33-in-probability先取機率再取極限)
  - [3.4 In distribution 與 in rth mean](#34-in-distribution-與-in-rth-mean)
  - [3.5 極限的唯一性、monotone 與 dominated convergence](#35-極限的唯一性monotone-與-dominated-convergence)
- [4. 弱與強的大數法則](#4-弱與強的大數法則)
- [5. Ergodic theorem 就是強大數法則](#5-ergodic-theorem-就是強大數法則)
- [6. Stationary 但不 ergodic：ergodic decomposition](#6-stationary-但不-ergodicergodic-decomposition)
- [7. 中央極限定理](#7-中央極限定理)
- [8. Convexity、convex set、Jensen 不等式](#8-convexityconvex-setjensen-不等式)
- [9. Lagrange multipliers 與 KKT conditions](#9-lagrange-multipliers-與-kkt-conditions)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

把附錄 B 講完：隨機變數序列的**五種收斂模式**、**弱／強大數法則**、ergodic 和大數法則的關係、**中央極限定理**，以及求極值的工具 **convexity、Jensen 不等式、Lagrange multipliers 與 KKT conditions**。

| 主題 | 課本 |
|---|---|
| 五種收斂、Example B.7、唯一性 | §B.4 Definition B.6、Example B.7、Observation B.8（pp. 283–285） |
| Monotone／dominated convergence | Theorem B.9–B.10（p. 285） |
| Markov、Chebyshev 不等式、WLLN、SLLN | §B.5.1 Lemma B.11–B.12、Theorem B.13–B.14（pp. 286–289） |
| Ergodicity vs LLN、ergodic decomposition | §B.5.2（pp. 289–291） |
| CLT | §B.6 Theorem B.15（p. 291） |
| Convexity、Jensen | §B.7 Definition B.16–B.17、Theorem B.18（pp. 291–293） |
| Lagrange、KKT | §B.8 Definition B.19、Example B.20（pp. 293–296） |

---

## 1. 回顧：我們要的是 time average → ensemble average

[▶ 00:30](https://youtu.be/NCnA-2U5skE?t=30)

- 上次介紹的 stationary、i.i.d.、Markov、ergodic，重點只有一個：我們要的結果是 **time average 收斂到 ensemble average**。
- 期望值要不隨時間改變，所以需要 stationary；但真正要的是收斂。這就是**大數法則（law of large numbers, LLN）**的**結果**；大數法則研究的是**什麼條件**會讓它成立，stationary ergodic 只是其中一種重要條件。
- 【口頭】這對應到巨觀、big data。一次傳送只有成功或失敗兩種答案（deterministic）；傳 20 萬、30 萬次才有「機率」。Shannon 定理裡的 $n$ 就是 block length（傳送次數），一直在找 $n\to\infty$ 時的大數法則行為。這是**整本書貫穿的重點**。

---

## 2. Typical set 的精神

[▶ 03:03](https://youtu.be/NCnA-2U5skE?t=183)

大數法則是統計和機率的名詞；消息理論用的名詞是 **typical set（典型集合）**，只有消息理論的書和文獻才看到（50、60 年代取的名字）。

- 所有可能的嘗試中，有一個集合：落在**外面**的機率是 $\delta$、落在**裡面**的機率是 $1-\delta$，$\delta$ 可以任意小。我們要抓的就是這個集合。
- 不同作者定義不同（例如 Csiszár 的書和 Shannon 的論文定義方式不一樣），但共同特性是：這個集合的機率佔大部分（例如 99%）。
- **幸運的是這個集合通常很小**：例如 100 萬個元素中只有 2 萬個在裡面，卻佔了大部分機率。（只有在已經壓縮到極限的時候，它的數量才會很大。）
- 所以做訊號處理、資料壓縮時，外面的可以全部忽略，只注意裡面。這和 **importance sampling** 是同一個精神。
- 【口頭】比喻：財富集中在 2% 的人身上，抽稅只要抽那 2% 就好。

---

## 3. 五種收斂模式

[▶ 05:39](https://youtu.be/NCnA-2U5skE?t=339)

大數法則分 **strong（SLLN）** 和 **weak（WLLN）**。要區分強弱，先要知道隨機變數的收斂模式。

$\frac{X_1+\cdots+X_n}n$ 在 $n$ 還沒到無限大時是一個隨機變數（Jack 量的和 Mary 量的不一樣）；問題是它怎麼收斂。

**Definition B.6**（pp. 283–284）：$\{X_n\}$ 收斂到 $X$——
1. **Pointwise on $\Omega$**（$X_n\xrightarrow{p.w.}X$）：$\lim_nX_n(\omega)=X(\omega)$，**對所有** $\omega\in\Omega$。
2. **Almost surely／with probability 1**（$X_n\xrightarrow{a.s.}X$）：$P\{\omega:\lim_nX_n(\omega)=X(\omega)\}=1$。
3. **In probability**（$X_n\xrightarrow{p}X$）：對任意 $\varepsilon>0$，$\lim_n\Pr\{|X_n-X|>\varepsilon\}=0$。
4. **In $r$th mean**（$X_n\xrightarrow{L^r}X$）：$\lim_nE\left[|X-X_n|^r\right]=0$。
5. **In distribution**（$X_n\xrightarrow{d}X$）：$\lim_nF_{X_n}(x)=F_X(x)$，對 $F_X$ 的每個連續點 $x$。

**關係圖**（課本 p. 285）：
$$\text{p.w.}\Rightarrow\text{a.s.}\Rightarrow\text{in probability}\Rightarrow\text{in distribution},\qquad L^r\ (r\ge1)\Rightarrow\text{in probability}.$$
強的對了，弱的一定對。另外 a.s. 加上條件可推 $L^1$（Theorem B.9、B.10）。

【口頭】左邊這條（p.w. → a.s. → p → d）看的是**機率**；右邊的 $L^r$ 看的是**期望值**（整體加權平均）。通訊、系統、消息理論、大數法則講的都是左邊；只是有時借用期望值，因為 $L^r$ 收斂可以推出 in probability。typical set 看的是機率，不看期望值。

> 【口頭】老師說第二部分會講：**通訊其實只需要最弱的 convergence in distribution**。

### 3.1 Pointwise vs almost sure：四面骰子的例子

[▶ 10:21](https://youtu.be/NCnA-2U5skE?t=621)

**Example B.7**（p. 284）：$\Omega=\{0,1,2,3\}$，$\mathcal F=2^\Omega$，$P(0)=P(1)=P(2)=\frac13$，$P(3)=0$。定義 $X_n(\omega)=\frac\omega n$。
- 每個 $\omega$：$\frac0n,\frac1n,\frac2n,\frac3n\to0$。所以 $X_n\xrightarrow{p.w.}X$，$X(\omega)=0$。
- 【口頭】pointwise 其實不隨機：它只是一串函數（數字）收斂到另一個函數，是 deterministic 的。

**為什麼用機率空間定義隨機變數很方便** [▶ 12:54](https://youtu.be/NCnA-2U5skE?t=774)（【口頭】）：證明 $X_n-W_n$ 的性質時，如果只有分布，還要 $X_n$、$W_n$ 的 joint distribution 才能證；如果兩者都定義在同一個 mapping 上，就只是函數的證明，沒有隨機。老師說高等機率論那門課會更有感覺。

### 3.2 Almost sure（先取極限再取機率）

[▶ 14:24](https://youtu.be/NCnA-2U5skE?t=864)

再定義 $\tilde X(\omega)=0$（$\omega=0,1,2$）、$\tilde X(3)=1$。
- $\omega=3$ 時 $X_n(3)=\frac3n\to0\ne\tilde X(3)$，所以 $X_n$ **不** pointwise 收斂到 $\tilde X$。
- 但 $\omega=3$ 沒有機率，所以
$$\Pr\left\{\lim_nX_n=\tilde X\right\}=\sum_{\omega=0}^3P(\omega)\,\mathbf 1\left\{\lim_nX_n(\omega)=\tilde X(\omega)\right\}=\tfrac13+\tfrac13+\tfrac13+0=1.$$
$X_n\xrightarrow{a.s.}X$ 而且 $X_n\xrightarrow{a.s.}\tilde X$ 都成立。

> ⚠️ 逐字稿缺字：老師口述 $\tilde X(3)$ 的值聽起來像「3」，課本是 $\tilde X(3)=1$；只要不等於 0，結論一樣。

**記法**：almost sure 就是 **strong law of large numbers** 的收斂方式：**先取極限，再取機率**。有機率的部分都要收斂，沒機率的部分不在乎。
- 在極限端不能有任何機率遺漏，所以也叫 **with probability 1**（100%）。
- 【口頭】i.i.d. 雜訊、AWGN、memoryless channel、stationary ergodic，都滿足強大數法則。

### 3.3 In probability（先取機率再取極限）

[▶ 17:02](https://youtu.be/NCnA-2U5skE?t=1022)

**Weak law of large numbers** 的收斂方式：**先取機率，再取極限**。先看兩個隨機變數差距大於 $\varepsilon$ 的機率，再看這個機率在極限是否趨近 0。

【口頭】
- 「我 with probability 1 一定出來選總統」就是一定會選；「in probability」就表示不見得，有個機率。
- 通訊允許 in probability：通訊從來不要完美。例如無線通訊允許 bit error rate $10^{-5}$，有錯沒關係，只要錯很小就好。

### 3.4 In distribution 與 in rth mean

[▶ 18:33](https://youtu.be/NCnA-2U5skE?t=1113)

**In distribution**：只要 CDF 收斂。比 in probability 更弱：in probability 要先取差距；in distribution **連差距都不取**，差距可能很大，只要分布收斂。
- 例：$\frac{X_1+\cdots+X_n}n$ 收斂到常數（期望值）$\mu$。常數的 CDF 是 unit step function：比 $\mu$ 小機率 0，比 $\mu$ 大機率 1。左邊的 CDF 慢慢變成這個 step function，這就是我們要的。
- 【口頭】80 年代末、90 年代，大家漸漸理解通訊好像不需要 in probability，只需要 convergence in distribution，幾乎都能 work。

**In $r$th mean**：看差距絕對值的 $r$ 次方的期望值（整體表現）。成立則 in probability 一定成立，但 a.s. 不一定。

### 3.5 極限的唯一性、monotone 與 dominated convergence

[▶ 21:04](https://youtu.be/NCnA-2U5skE?t=1264)

**Observation B.8（唯一性）**（p. 285）：
1. p.w. 收斂到 $X$ 和 $Y$ ⇒ $X(\omega)=Y(\omega)$ 對所有 $\omega$。
2. a.s.（或 in probability，或 $L^r$）收斂到 $X$ 和 $Y$ ⇒ $\Pr\{X=Y\}=1$。
3. in distribution 收斂到 $X$ 和 $Y$ ⇒ $F_X=F_Y$。

**把 a.s. 和 $L^1$ 串起來**（【口頭】實變分析最重要的兩個收斂定理）[▶ 22:04](https://youtu.be/NCnA-2U5skE?t=1324)：

**Theorem B.9（monotone convergence）**：$X_n\xrightarrow{a.s.}X$，$Y\le X_n\le X_{n+1}$（對所有 $n$），$E[|Y|]<\infty$ ⇒ $X_n\xrightarrow{L^1}X$ ⇒ $E[X_n]\to E[X]$。
- 【口頭】要單調，而且出發點有界（不能衝到無限大），只要一端有界就好。

**Theorem B.10（dominated convergence）**：$X_n\xrightarrow{a.s.}X$，$|X_n|\le Y$（對所有 $n$），$E[|Y|]<\infty$ ⇒ $X_n\xrightarrow{L^1}X$ ⇒ $E[X_n]\to E[X]$。

**$L^1\Rightarrow$ 期望值收斂** 的證明（p. 286）：
$$\left|E[X_n]-E[X]\right|=\left|E[X_n-X]\right|\le E\left[|X_n-X|\right]\to0.$$

---

## 4. 弱與強的大數法則

[▶ 24:39](https://youtu.be/NCnA-2U5skE?t=1479)

【課本補充】兩個工具（pp. 286–287）：

**Lemma B.11（Markov 不等式）**：任意整數 $k>0$、實數 $\alpha>0$，
$$\Pr[|X|\ge\alpha]\le\frac1{\alpha^k}E\left[|X|^k\right].$$
證明：
$$E[|X|^k]=\int|x|^k\,dF_X(x)\ge\int_{|x|\ge\alpha}|x|^k\,dF_X(x)\ge\int_{|x|\ge\alpha}\alpha^k\,dF_X(x)=\alpha^k\Pr[|X|\ge\alpha].$$

**Lemma B.12（Chebyshev 不等式）**：$\Pr\left[|X-E[X]|\ge\alpha\right]\le\frac1{\alpha^2}\mathrm{Var}[X]$。（Markov 取 $k=2$，用在 $X-E[X]$。）

**Theorem B.13（Weak LLN）**（p. 288）：$\{X_n\}$ **uncorrelated**、共同平均 $\mu$。若
$$\lim_{n\to\infty}\frac1{n^2}\sum_{i=1}^n\mathrm{Var}[X_i]=0\quad\left(\text{等價於 }\tfrac{X_1+\cdots+X_n}n\xrightarrow{L^2}\mu\right),$$
則樣本平均 **in probability** 收斂到 $\mu$。
- 證明（Chebyshev）：
$$\Pr\left\{\left|\frac1n\sum_{i=1}^nX_i-\mu\right|\ge\varepsilon\right\}\le\frac1{\varepsilon^2}\mathrm{Var}\left[\frac1n\sum X_i\right]=\frac1{n^2\varepsilon^2}\sum_{i=1}^n\mathrm{Var}[X_i]\to0.$$
（uncorrelated 讓和的 variance = variance 的和。）
- 【口頭】這就是 $L^2$ 收斂推 in probability；有人叫它 **Chebyshev 大數法則**。

**Theorem B.14（Kolmogorov 強大數法則）**（p. 288）：$\{X_n\}$ **independent**、共同平均 $\mu$。若下列**任一**成立：
1. $X_n$ 同分布（即 i.i.d.）；或
2. $X_n$ square-integrable，且 $\displaystyle\sum_{i=1}^\infty\frac{\mathrm{Var}[X_i]}{i^2}<\infty$，

則 $\frac{X_1+\cdots+X_n}n\xrightarrow{a.s.}\mu$。

【口頭】
- Kolmogorov 是 20 世紀蘇聯數學家（老師說「19 世紀」），做了非常多東西，例如 Kolmogorov complexity；Cover 的書有一章專門介紹。
- 條件 1：例如 AWGN，每個 sample i.i.d.，強大數法則一定成立——工程上要的都有了。
- 條件 2：不同分布也行，只要 independent，且 variance 分別除以 $1,4,9,\dots$（後面除得越多）再加起來是有限的。
- 所以好像**不需要 stationary ergodic**。

【課本補充】(p. 288–289) 有些 independent 序列 WLLN 成立但 SLLN 不成立，因為 $\sum_{i=1}^n\frac{\mathrm{Var}[X_i]}{i^2}\ge\frac1{n^2}\sum_{i=1}^n\mathrm{Var}[X_i]$。Kolmogorov SLLN 可推廣到函數：$\frac1n\sum g(X_i)\xrightarrow{a.s.}E[g(X_1)]$；WLLN 不行，因為 $Y_i$、$Y_j$ uncorrelated 不代表 $g(Y_i)$、$g(Y_j)$ uncorrelated。

---

## 5. Ergodic theorem 就是強大數法則

[▶ 27:12](https://youtu.be/NCnA-2U5skE?t=1632)

- 強大數法則 = almost sure = with probability 1。
- Pointwise ergodic theorem（第 6 集 Theorem B.4）的結論是 with probability 1，所以**它也是一種強大數法則**：給的條件是 stationary ergodic。
- 歷史（【口頭】）：1931 年 Birkhoff 證出來，證明比較複雜；1933 年 Khinchin（蘇聯人，論文多用俄文寫，所以後來才被發現）重新證明、去掉枝微末節，並且馬上理解到 ergodic theorem 和大數法則是同一件事（"Khinchin understood at once the relation between the ergodic theorem and the law of large numbers"）。

**常見的誤解** [▶ 28:43](https://youtu.be/NCnA-2U5skE?t=1723)：
- 80 年代起有些書把結果當定義：「stationary process 若 time average 收斂到 ensemble average，就叫 ergodic」。大學部常用的課本和網路上很多這樣寫。
- 這樣學生會覺得 pointwise ergodic theorem「不用證了，結果就是定義」。
- 這在 30 年代的原始定義下是**錯的**：ergodic 原本是封閉體系、在裡面循環、從任何一點開始量都會量到所有現象（第 6 集）。
- 【口頭】那些書可能沒查先前的文獻；不過對工程方便，因為我們只要大數法則這個結果。

【課本補充】課本 §B.5.2（pp. 289–291）的整理：
- ergodicity **不需要** stationarity：non-stationary process 也可以 ergodic。
- 很多很好的物理模型不是 ergodic，卻滿足某種大數法則。
- 甚至 stationarity 也不是必要的：可以引入 asymptotically mean stationary；例如有限字母、time-invariant（不一定 stationary）的 irreducible Markov chain 就滿足大數法則。

**Ergodic 沒有有限維版本** [▶ 31:46](https://youtu.be/NCnA-2U5skE?t=1906)（【口頭】）：ergodic 講的是收斂，量測數量一定要到無限大；stationary 是統計特性不隨時間變，量 10 次、20 次都有意義。i.i.d.（例如 AWGN）一定是 stationary ergodic、也是 Markov，在關係圖的中間。結論：看到這些名詞不用太認真，**我們要的就是大數法則（甚至只要 convergence in distribution）**。

---

## 6. Stationary 但不 ergodic：ergodic decomposition

[▶ 33:18](https://youtu.be/NCnA-2U5skE?t=1998)

**量測的比喻**（【口頭】）：量一條河四季的流量，甲同學在河的這一端量，乙同學在另一端量。若流量符合大數法則，長期結果應該一樣；若只有 stationary 沒有 ergodic，兩人量的會不一樣——因為**量測點一放下去就不同了**。

**例子**（課本 pp. 290–291）：$\{A_n\}$、$\{B_n\}$ 是兩個 i.i.d. 二元序列，$\Pr\{A_n=0\}=\frac14$、$\Pr\{B_n=1\}=\frac14$（即 $A_n$ 為 1 的機率 $\frac34$，$B_n$ 為 1 的機率 $\frac14$）。$U$ 是等機率的二元隨機變數，三者獨立。
$$X_n=\begin{cases}A_n,&U=1\\B_n,&U=0\end{cases}\qquad\text{即 }X_n=U\cdot A_n+(1-U)\cdot B_n.$$

- **Stationary**：每個時間點統計特性完全一樣。
- **不是 ergodic**：若是 ergodic，相對頻率會收斂到
$$\Pr(X_n=1)=\Pr(U=1)\Pr(A_n=1)+\Pr(U=0)\Pr(B_n=1)=\tfrac12\cdot\tfrac34+\tfrac12\cdot\tfrac14=\tfrac12.$$
但實際上，甲（$U=1$）量到 1 的比例是 75%，乙（$U=0$）量到 25%。兩人都量得很認真、**都對**。所以
$$\frac1n\sum_{i=1}^nX_i\xrightarrow{a.s.}Y,\qquad\Pr\left(Y=\tfrac14\right)=\Pr\left(Y=\tfrac34\right)=\tfrac12,$$
收斂到一個隨機變數，和 ergodic theorem 矛盾。

**Ergodic decomposition theorem** [▶ 36:53](https://youtu.be/NCnA-2U5skE?t=2213)：在相當一般的條件下，**任何 stationary process 都是 stationary ergodic process 的混合（weighted sum）**。所以你觀察到的永遠是某一個 stationary ergodic 的結果——上例中你只能量到 $A_n$ 或 $B_n$，量不到 $X_n$。多個成分就是 $\sum_kU_k\,A_n^{(k)}$ 的形式。
- 這個定理必須用**原始**的 ergodic 定義看；如果用「ergodic ⟺ 大數法則成立」那種工程書定義，就沒有 ergodic decomposition theorem 可言。

【口頭】
- 第二部分會看到：黑箱子裡有一個 switch，每個人量測的觀點（裝置）不同，量到的 0、1 機率不同。傳統上這種資料被認為不可壓縮，但後來發現可以：例如 1000 bit 壓到 800 多 bit。這是 90 年代從 convergence in distribution 看出來的結果。
- 很多時候我們量到的只有 stationary，卻以為是 stationary ergodic。
- ergodic 和 stationary 有沒有關係？沒有。手機早上、晚上面對的雜訊統計略有不同也沒關係，只要長期符合大數法則，這一兩年都能用。

---

## 7. 中央極限定理

[▶ 39:30](https://youtu.be/NCnA-2U5skE?t=2370)

大數法則是除以 $n$；如果改成除以 $\sqrt n$，可能收斂到高斯。

**Theorem B.15（Central limit theorem）**（p. 291）：$\{X_n\}$ i.i.d.，有限的共同平均 $\mu$ 和變異數 $\sigma^2$，則
$$\frac1{\sqrt n}\sum_{i=1}^n(X_i-\mu)\xrightarrow{d}Z\sim\mathcal N(0,\sigma^2).$$
收斂是 **in distribution**。

【口頭】一定要 **finite energy（有限能量）**：只要能量有限，累加除以 $\sqrt n$ 就收斂到高斯，條件很鬆。若 mean 有限但 second moment 無限大，就不一定收斂到高斯，會收斂到別的東西。高等機率論課會教。

---

## 8. Convexity、convex set、Jensen 不等式

[▶ 41:03](https://youtu.be/NCnA-2U5skE?t=2463)

這三個在消息理論求極值時非常重要。

**Definition B.16（convex function）**（p. 292）：$\mathcal O\subset\mathbb R^m$ 是 convex set。$f:\mathcal O\to\mathbb R$ 在 $\mathcal O$ 上 **convex**，若對所有 $x,y\in\mathcal O$、$0\le\lambda\le1$，
$$f\left(\lambda x+(1-\lambda)y\right)\le\lambda f(x)+(1-\lambda)f(y).$$
只有 $\lambda=0$ 或 1 時等號成立，叫 strictly convex。
- 直覺：兩點拉一條直線，函數值在直線下面。
- **Definition B.17**：$-f$ convex 就叫 $f$ **concave**。
- 【課本補充】$\mathcal O=(a,b)$ 時，二階導數 $\ge0$（$>0$）⇒ convex（strictly convex），可由 Taylor 展開證明。

**為什麼重要**（【口頭】）：convex／concave 對求極值非常重要（convex optimization）。Shannon 的通訊問題：傳送端和接收端的「共識」（mutual information）跟輸入的角度（0、1 的使用比例）有關，要找最好的輸入角度讓共識最大。**很巧妙地，mutual information 對輸入分布剛好是 concave**，所以極值一定存在而且找得到。

**Convex set** [▶ 42:34](https://youtu.be/NCnA-2U5skE?t=2554)：集合中任兩點連成的線段還在集合裡（課本 p. 292 註 11：$\lambda x+(1-\lambda)y\in\mathcal O$）。有凹洞的集合求極值會有缺陷。

**例子** [▶ 43:35](https://youtu.be/NCnA-2U5skE?t=2615)：
- 二元輸入，0 的機率 $p$：要 maximize over $p\in[0,1]$，是 convex set（數線上任兩點拉直線都在裡面）。
- 三元輸入 0、1、2，機率 $(p,q,1-p-q)$：$p\ge0$、$q\ge0$、$1-p-q\ge0$，是二維的三角形，也是 convex set。
- 消息理論都在 convex set 上取極值，因為機率分布的集合就是 convex set。

**Theorem B.18（Jensen 不等式）**（p. 292）：$f$ 在 convex set $\mathcal O\subset\mathbb R^m$ 上 convex，$X$ 是取值在 $\mathcal O$ 內的隨機向量，則
$$E[f(X)]\ge f(E[X]).$$
若 $f$ strictly convex，等號成立 ⇒ $X=E[X]$ with probability 1。concave 時不等號反向。

**證明**（課本 pp. 292–293）：取通過 $(E[X],f(E[X]))$ 的 support hyperplane $y=a^Tx+b$，它整個在 $f$ 的圖形下方：$a^Tx+b\le f(x)$ 對所有 $x$。兩邊取期望值：
$$f(E[X])=a^TE[X]+b\le E[f(X)].$$
（$\mathcal O$ convex 保證 $E[X]\in\mathcal O$，所以 $f(E[X])$ 有定義。）

【口頭】
- 很多同學只背「先取函數再取期望 ≥ 先取期望再取函數」。注意 **convex 出現兩次**：convex function **over a convex set**。集合不是 convex 就會出問題，審論文時很容易抓到這種錯。
- 它的操作意義是**兩個操作對調**（像積分和微分對調不一定相等）。期望值是線性組合；工程上常把觀察值代進 threshold function，然後看統計行為，Jensen 給出效能的 bound。這個 bound 通常蠻 loose，但漸近來看很有用。
- strictly convex 時，等號只在 $X=E[X]$ with probability 1 時成立。

---

## 9. Lagrange multipliers 與 KKT conditions

[▶ 48:11](https://youtu.be/NCnA-2U5skE?t=2891)

【口頭】這是消息理論非常重要的技巧，做研究常用；一般的書常忽略 KKT，但學生應該學。

**名字的歷史**：Karush–Kuhn–Tucker。Cover & Thomas 的書只叫 Kuhn–Tucker conditions，少了一個 K：Kuhn 和 Tucker 1951 年合作推出這個條件，後來才發現 Karush 在 1939 年的碩士論文就發表了（老師先說 1936，後說 1939）。2000 年以後的書和 IEEE 都改稱 KKT，把 Karush 放第一個，還他公道。

**問題**（課本 (B.8.1)，p. 293）：
$$\min_{x\in Q}f(x),\qquad Q:=\{x\in\mathcal X:\ g_i(x)\le0,\ 1\le i\le m;\ h_j(x)=0,\ 1\le j\le\ell\}.$$
不等式限制都移項成 $\le0$；等式限制 $=0$。有限制的問題很難。

**Step 1：拿掉限制——Lagrange dual function** [▶ 51:14](https://youtu.be/NCnA-2U5skE?t=3074)（課本 (B.8.2)）：
$$L(\lambda,\nu):=\min_{x\in\mathcal X}\left(f(x)+\sum_{i=1}^m\lambda_ig_i(x)+\sum_{j=1}^\ell\nu_jh_j(x)\right).$$
- 注意範圍從 $Q$ 變成沒有限制的 $\mathcal X$（$Q\subset\mathcal X$）。沒有限制就能用微積分：微分 = 0。
- 它是衍生的 **dual problem**，**不一定等效**於原問題。
- $\lambda=(\lambda_i)$、$\nu=(\nu_j)$ 叫 **Lagrange multipliers**（不只一個，所以要加 s）。
- 【口頭】有人用非線性（例如二次）的方式加限制，收斂比較快。

**$L$ 對 $(\lambda,\nu)$ 是 concave** [▶ 53:46](https://youtu.be/NCnA-2U5skE?t=3226)：固定 $x$，$f(x)+\lambda g(x)$ 對 $\lambda$ 是一條直線（截距 $f(x)$、斜率 $g(x)$）。不同 $x$ 給不同直線；對所有直線取最小值（下包絡線），一定是 concave。concave 的最大值一定存在、一定找得到。

**$L$ 是原問題的下界** [▶ 55:46](https://youtu.be/NCnA-2U5skE?t=3346)（課本 (B.8.3)）：當 $\lambda_i\ge0$，
$$L(\lambda,\nu)\le\min_{x\in Q}\left(f(x)+\sum_i\lambda_ig_i(x)+\sum_j\nu_jh_j(x)\right)\le\min_{x\in Q}f(x).$$
- 第一個 ≤：$Q\subset\mathcal X$，在大範圍取 min 一定比在小範圍取 min 小。【口頭】三個人中最矮的，不會比其中兩個人中最矮的高。
- 第二個 ≤：在 $Q$ 裡 $h_j(x)=0$；$g_i(x)\le0$ 且 $\lambda_i\ge0$，所以 $\lambda_ig_i(x)\le0$，拿掉只會變大。
- **為什麼 $\lambda\ge0$**：$g\le0$ 乘上正數，正負號才不會變。

**Strong duality** [▶ 58:49](https://youtu.be/NCnA-2U5skE?t=3529)：$\max_{\lambda\ge0,\nu}L(\lambda,\nu)$ 可能**嚴格小於**原問題的最小值（有 gap）。若存在非負 $\tilde\lambda$ 和 $\tilde\nu$ 使等號成立，叫 **strong duality**。此時（課本 (B.8.4)）$x^*$ 同時達成兩邊，而且 $\tilde\lambda_ig_i(x^*)=0$。

**KKT conditions**（Definition B.19，p. 295）：點 $x$ 和 multipliers $\lambda,\nu$ 滿足
$$\begin{cases}g_i(x)\le0,\ \lambda_i\ge0,\ \lambda_ig_i(x)=0,&i=1,\dots,m\\h_j(x)=0,&j=1,\dots,\ell\\\displaystyle\frac{\partial f}{\partial x_k}(x)+\sum_{i=1}^m\lambda_i\frac{\partial g_i}{\partial x_k}(x)+\sum_{j=1}^\ell\nu_j\frac{\partial h_j}{\partial x_k}(x)=0,&k=1,\dots,n\end{cases}$$

**什麼時候 KKT 保證最佳** [▶ 63:23](https://youtu.be/NCnA-2U5skE?t=3803)：
- $f$、$g_i$ 都 **convex**，$h_j$ 是 **affine**，而且都可微 ⇒ strong duality 成立 $\iff$ KKT 成立（課本 pp. 294–295）。
  - **affine**：直線但不一定過原點；**linear** 是過原點的直線。
  - 要可微，是因為要加上 multipliers 再微分。
  - $\lambda_ig_i=0$：要嘛 $\lambda_i=0$，要嘛 $g_i=0$（限制剛好卡住）。
- $f,g,h$ 是任意函數 ⇒ KKT 只是 **necessary condition**：若 strong duality 成立，KKT 一定成立；但 KKT 成立不代表 gap = 0。只能拿來驗證。

**實際做法：三步驟** [▶ 60:50](https://youtu.be/NCnA-2U5skE?t=3650)：
1. 加上 Lagrange multipliers：$f(x)+\lambda g(x)+\nu h(x)$；
2. 對 $x$ 微分 = 0，得到最佳 $x$（是 $\lambda,\nu$ 的函數）；範圍是 convex set（例如三角形）就沒關係；
3. 找最好的 $\lambda,\nu$（concave，一定存在）。

**機率分布上的 KKT**（【課本補充】p. 295）：$x$ 是機率分布時，多了 $g_{m+k}(x)=-x_k\le0$ 和 $h_{\ell+1}(x)=\sum_kx_k-1=0$。由 $\lambda_{m+k}\ge0$、$\lambda_{m+k}x_k=0$ 得到最常見的形式：
$$\frac{\partial f}{\partial x_k}+\sum_i\lambda_i\frac{\partial g_i}{\partial x_k}+\sum_j\nu_j\frac{\partial h_j}{\partial x_k}+\nu_{\ell+1}\ \begin{cases}=0,&x_k>0\\\ge0,&x_k=0.\end{cases}$$

**例子：capacity** [▶ 66:28](https://youtu.be/NCnA-2U5skE?t=3988)（課本 Example B.20，pp. 295–296）：
$$f(x)=-\sum_{i=1}^n\sum_{j=1}^nx_iq_{i,j}\log\frac{q_{i,j}}{\sum_{i'}x_{i'}q_{i',j}},\qquad g_i(x)=-x_i\le0,\qquad h(x)=\sum_ix_i-1=0.$$
- $x_i$ 是輸入機率（例如 $(p,q,1-p-q)$），$q_{i,j}$ 是通道「送 $i$ 收到 $j$」的機率。$-f$ 就是 Shannon 的 mutual information（之後會講）。
- 要在三角形上 maximize mutual information = minimize 它的負號。
- 【口頭】上帝好像給了暗示：mutual information 加負號剛好是 convex，不等式限制是直線（convex），等式限制是 affine——全部符合。所以用 Lagrange multipliers，**保證找到真正最好的輸入分布**。

**總結** [▶ 68:33](https://youtu.be/NCnA-2U5skE?t=4113)：背景都介紹完了。stationary、ergodic、Markov 之後會用；收斂：strong law 是 a.s.，weak law 是 in probability，第二部分講 in distribution 和 $L^r$；重點是大數法則和中央極限定理；convex／concave、Jensen、KKT 是求極值的工具。

---

## 10. 一頁速查表

**五種收斂**
- p.w.：所有 $\omega$；a.s.：$P\{\lim X_n=X\}=1$（先極限後機率）；in prob.：$\Pr\{|X_n-X|>\varepsilon\}\to0$（先機率後極限）；$L^r$：$E|X_n-X|^r\to0$；in dist.：$F_{X_n}\to F_X$（連續點）。
- p.w. ⇒ a.s. ⇒ p ⇒ d；$L^r$ ⇒ p。
- 例 B.7：$\Omega=\{0,1,2,3\}$、$P(3)=0$、$X_n=\omega/n$ ⇒ a.s. 收斂到 $\tilde X$（$\tilde X(3)=1$），但不 p.w.。
- Monotone／dominated（有界 $E|Y|<\infty$）：a.s. ⇒ $L^1$ ⇒ $E[X_n]\to E[X]$（$|E X_n-E X|\le E|X_n-X|$）。

**不等式**：Markov $\Pr[|X|\ge\alpha]\le E|X|^k/\alpha^k$；Chebyshev $\Pr[|X-EX|\ge\alpha]\le\mathrm{Var}X/\alpha^2$。

**大數法則**
- WLLN（uncorrelated，$\frac1{n^2}\sum\mathrm{Var}X_i\to0$）：樣本平均 $\xrightarrow{p}\mu$。關鍵：Chebyshev。
- SLLN（Kolmogorov，independent，i.i.d. 或 $\sum\mathrm{Var}X_i/i^2<\infty$）：$\xrightarrow{a.s.}\mu$。
- Pointwise ergodic theorem = stationary ergodic 版的 SLLN。

**Ergodic decomposition**：stationary = stationary ergodic 的混合。例 $X_n=UA_n+(1-U)B_n$：平均 $\to Y\in\{\frac14,\frac34\}$（各 1/2），不是 $\frac12$。

**CLT**：i.i.d.、有限 $\mu,\sigma^2$ ⇒ $\frac1{\sqrt n}\sum(X_i-\mu)\xrightarrow{d}\mathcal N(0,\sigma^2)$。

**Jensen**：$f$ convex **over convex set** ⇒ $E f(X)\ge f(EX)$（support line 取期望）；strictly convex 時等號 ⇒ $X=EX$ a.s.

**Lagrange / KKT**
- $L(\lambda,\nu)=\min_{x\in\mathcal X}\left(f+\sum\lambda_ig_i+\sum\nu_jh_j\right)$：對 $(\lambda,\nu)$ concave；$\lambda\ge0$ 時 $\le\min_Qf$。
- Strong duality：等號成立。$f,g$ convex、$h$ affine、可微 ⇒ strong duality ⟺ KKT（$g\le0,\lambda\ge0,\lambda g=0,h=0,\nabla(f+\lambda g+\nu h)=0$）。
- 機率分布版：$\partial_k(\cdot)+\nu=0$ 若 $x_k>0$，$\ge0$ 若 $x_k=0$。
- 應用：capacity = 在機率單形上 maximize concave 的 mutual information。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Jensen、convexity | 第 8–11 集（entropy 的界、divergence 非負、convexity of information measures） |
| Typical set、WLLN | 第 12 集（AEP、source coding theorem） |
| Chebyshev、WLLN、jointly typical | 第 16–18 集（channel coding theorem） |
| KKT、mutual information concave | 第 19 集（計算 capacity）、第 25 集（water-filling） |
| CLT、高斯 | 第 22–26 集（第 5 章 Gaussian channel） |
| Ergodic decomposition、convergence in distribution | 第 32–35 集（第二部分） |

---

## 附：本集一句話總結

> **大數法則是「結果」——樣本平均收斂到期望值；強的是 a.s.（先極限後機率）、弱的是 in probability（先機率後極限），而通訊最後只需要更弱的 in distribution。求極值則靠 convex function over convex set：Jensen 給界，Lagrange＋KKT 保證找到最佳輸入分布。**

---

*筆記依據陳伯寧老師「消息理論」Lec07 錄影逐字稿（whisper large-v3-turbo，1:09:41）與 Alajaji & Chen 課本附錄 B §B.4–B.8 整理。*
