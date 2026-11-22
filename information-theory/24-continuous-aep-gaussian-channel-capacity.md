---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 24
lecture: Lec24 5.3 AEP for continuous memoryless sources, 5.4 Capacity for discrete-time memoryless Gaussian channel
date: 待補
video: https://youtu.be/wVTBjnPhjlE
notes: Alajaji & Chen §5.3–5.4（pp. 183–196，Theorem 5.23–Observation 5.35）
---

# 第 24 集 · Lec24 §5.3–5.4：連續 source 的 AEP、capacity-cost function、Gaussian channel 的 coding theorem [▶ 影片](https://youtu.be/wVTBjnPhjlE)

← 上一集：[23](23-differential-entropy-joint-divergence-mutual-info.md) ｜ [總目錄](README.md) ｜ 下一集：[25](25-parallel-gaussian-channels-water-filling.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 24 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:06:00，whisper large-v3-turbo）＋ 課本 §5.3–5.4（pp. 183–196）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Shannon」聽成「Shanon」，「stationary ergodic」聽成「Stational Ergotic」，「asymptotic equipartition」聽成「Asymptatic Equal Partition」，「volume」正確，「cost constraint」聽成「Cost Contraint」，「supremum」聽成「Supremant」，「convex set」聽成「comvac set／comeback set」，「time sharing」正確，「Laplacian」正確，「Cauchy distribution」聽成「Colchie Distribution」，「Poisson」聽成「剖重」，「infinitely divisible」聽成「Infinite Divisible」，「Fano」聽成「final／Phenol」，「non-coherent」正確，「實數」聽成「時數」。開頭「昨晚 晚上」、「增 rappelle」是亂碼。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 連續 source 的 AEP：算體積](#1-連續-source-的-aep算體積)
- [2. 沒有限制的連續輸入，capacity 是無限大](#2-沒有限制的連續輸入capacity-是無限大)
- [3. Cost constraint 與 capacity-cost function](#3-cost-constraint-與-capacity-cost-function)
- [4. C(P) 是 concave：time sharing](#4-cp-是-concavetime-sharing)
- [5. Gaussian channel 的 capacity](#5-gaussian-channel-的-capacity)
- [6. 連續通道的 block code](#6-連續通道的-block-code)
- [7. Theorem 5.32：Gaussian channel 的 coding theorem](#7-theorem-532gaussian-channel-的-coding-theorem)
- [8. Forward part：多出來的 power constraint](#8-forward-part多出來的-power-constraint)
- [9. Converse part：Fano + concavity](#9-converse-partfano--concavity)
- [10. 高斯雜訊讓 capacity 最小](#10-高斯雜訊讓-capacity-最小)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

把 channel coding theorem 推廣到**連續**通道：先講連續 source 的 AEP（數不了個數，改算**體積**），再說明連續輸入一定要加 **cost（power）constraint**，定義 **capacity-cost function** $C(P)$ 並證明它 concave；算出 AWGN 的 $C(P)=\frac12\log_2(1+\frac P{\sigma^2})$，證明 coding theorem，最後證明高斯雜訊讓 capacity 最小。

| 主題 | 課本 |
|---|---|
| 連續 AEP、typical set、體積 | §5.3 Theorem 5.23–5.26（pp. 183–184） |
| 連續無記憶通道、capacity-cost function | Definition 5.27–5.28（pp. 184–185） |
| $C(P)$ concave | Lemma 5.29（pp. 185–186） |
| AWGN 模型與 capacity | (5.4.7)–(5.4.13)（pp. 186–188） |
| Block code、coding theorem | Definition 5.31、Theorem 5.32（pp. 189–193） |
| 高斯雜訊最小化 capacity | Theorem 5.33（p. 194） |
| Fading channel | Observation 5.35（pp. 195–196） |

---

## 1. 連續 source 的 AEP：算體積

[▶ 00:00](https://youtu.be/wVTBjnPhjlE?t=0)

【口頭】回到 Shannon 的 channel coding theorem for continuous source：它一定要有 **AEP** 的行為。你分析的大數據若不收斂（收集 10 萬、20 萬、30 萬筆，發現根本不是 stationary ergodic），就不用分析了——要能量測，一定要有大數法則。
- DMC（雜訊仍然獨立）時有某種形式的 AEP。
- 連續的 $X$、$Y$、$Z$ 從 $-\infty$ 到 $\infty$ 都有可能，**不能數個數**，只能算**體積**：存在一個體積很小、但佔很大機率的集合。裡面每一點機率大約一樣重要（幾乎 uniform，不能再壓縮）——equal partition。

**Theorem 5.23（連續無記憶 source 的 AEP）**（p. 184）：i.i.d. 連續 source，
$$-\frac1n\log_2f_X(X_1,\dots,X_n)\to E[-\log_2f_X(X)]=h(X)\quad\text{in probability}.$$
（獨立 ⇒ pdf 相乘、取 log 相加、除以 $n$ 取平均 ⇒ 大數法則；至少要 in probability，之後會說 in distribution 就夠。）

**Definition 5.24（typical set）**：$F_n(\delta):=\left\{x^n\in\mathbb R^n:\left|-\frac1n\log_2f_X(x^n)-h(X)\right|<\delta\right\}$。

**Definition 5.25（體積）**：$\mathrm{Vol}(A):=\int_Adx_1\cdots dx_n$。

**Theorem 5.26**（p. 184）：
1. $n$ 夠大時 $P_{X^n}(F_n(\delta))>1-\delta$；
2. $\mathrm{Vol}(F_n(\delta))\le2^{n(h(X)+\delta)}$（所有 $n$）；
3. $\mathrm{Vol}(F_n(\delta))\ge(1-\delta)2^{n(h(X)-\delta)}$（$n$ 夠大）。

【口頭】體積大約是 $2^{nh(X)}$。注意 differential entropy 可以是負的，例如 $h=-2$，體積是 $2^{-2n}$——這和 entropy（一定是正的）不太一樣，但數學都對，證明方法完全一樣（用定義）。

---

## 2. 沒有限制的連續輸入，capacity 是無限大

[▶ 05:05](https://youtu.be/wVTBjnPhjlE?t=305)

【口頭】假設雜訊 $N\sim\mathcal N(0,1)$。
- 輸入限制在 ±1，單位時間只能送 1 bit。
- 若允許輸入是 $-\infty$ 到 $\infty$ 的任何值：要送 2 bit，就用 ±1、±2 四個位階；要錯誤率任意小，就把它們乘 10、乘 40……間距拉到 ±100、±300，variance 只有 1 的雜訊完全不發生影響。要送多少 bit 就切多少位階。
- 所以**沒有限制的連續輸入，capacity 是無限大**（就像連續 source 的 entropy 是無限大），沒有意義。代價是 **power**。

---

## 3. Cost constraint 與 capacity-cost function

[▶ 07:38](https://youtu.be/wVTBjnPhjlE?t=458)

所以一定要加 **cost constraint**（power constraint）：對每個傳送的 $n$-tuple，
$$\frac1n\sum_{i=1}^nt(x_i)\le P.$$
- $t(x)=x^2$：**average power constraint**（平方代表能量，例如 $\frac1{100}\sum x_i^2\le1$）——通訊上用這個。
- $t(x)=|x|$：光學的能量限制（first moment）。
- 也可以是 peak 限制（每個都在 ±1 之內）。
- 【口頭】平均限制不限制個別：$x_1$ 可以很大（例如 100），其他就要很小。

**Definition 5.27（離散時間、連續、無記憶通道）**（pp. 184–185）：輸入、輸出字母是 $\mathbb R$ 的子集，轉移 pdf 滿足 $f_{Y^n|X^n}(y^n|x^n)=\prod_if_{Y|X}(y_i|x_i)$（沒有 feedback）。

**Definition 5.28（capacity-cost function）**（p. 185）：
$$C(P):=\sup_{F_X:\ E[t(X)]\le P}I(X;Y).$$
- 【口頭】為什麼是 $E[t(X)]\le P$：大數法則下，長度很長時 $\frac1n\sum t(x_i)$ 會趨近期望值，所以限制就變成期望值的限制。在這個限制下能達到的最大共識就是 capacity。
- 這是數學（information capacity）；接著要證明它在操作上也對。

---

## 4. C(P) 是 concave：time sharing

[▶ 11:12](https://youtu.be/wVTBjnPhjlE?t=672)

【口頭】有些性質對應用很重要。**Concavity** 很重要，第五代行動通訊就用到。

**Lemma 5.29**（pp. 185–186）：若 $C(P)$ 對每個 $P$ 有限，則 $C(P)$ 對 $P$ **非遞減且 concave**（因此連續、嚴格遞增）。

- **遞增**：給越多 power，能選的輸入分布越多（原本的都包含在內），取 sup 只會更大。
- **Concave** 的意義：**time sharing**——30% 時間用 power 1、70% 時間用 power 2，達到的速度是兩點連線上的點（平均 power 1.7）。若直接給你平均 1.7 自由調配，可以達到曲線上的點，**比 time sharing 更好**（但比較難做：1 和 2 也許有固定方法，任意調要做得更好比較難）。

**證明**（照課本）：令 $F_{X_1}$、$F_{X_2}$ 分別在 $P_1$、$P_2$ 下讓 $I$ 接近 sup（因為加了限制，不確定集合還是 compact／convex set，保險起見用 sup，所以只能保證 $I(F_{X_i},f_{Y|X})\ge C(P_i)-\varepsilon$）。time sharing 的分布 $F_{X_\lambda}=\lambda F_{X_1}+(1-\lambda)F_{X_2}$ 滿足 $E[t(X_\lambda)]\le\lambda P_1+(1-\lambda)P_2$，所以
$$\begin{aligned}
C(\lambda P_1+(1-\lambda)P_2)&\ge I(F_{X_\lambda},f_{Y|X})\\
&\ge\lambda I(F_{X_1},f_{Y|X})+(1-\lambda)I(F_{X_2},f_{Y|X})\qquad(I\text{ 對輸入分布 concave})\\
&\ge\lambda C(P_1)+(1-\lambda)C(P_2)-\varepsilon.
\end{aligned}$$
$\varepsilon\to0$ 即得。

【口頭】
- 「$I$ 對第一個參數（輸入分布）concave」是 Shannon 找到這個公式後一個很漂亮的巧合：要 maximize，剛好 concave，可以用 KKT／Lagrange 找最好的解。
- 第四代以前多半要 orthogonal 傳輸，只能 time sharing；第五代不做 orthogonal 傳輸，就是要偷到這個「曲線高於連線」多出來的部分。
- 有趣的現象：雜訊是高斯時最好的輸入也是高斯——**要騙過敵人，就要長得跟它一樣**；歷史上的交戰也是這樣。

---

## 5. Gaussian channel 的 capacity

[▶ 21:54](https://youtu.be/wVTBjnPhjlE?t=1314)

**模型**（(5.4.8)，p. 186）：$Y_i=X_i+Z_i$，$Z_i$ i.i.d. $\mathcal N(0,\sigma^2)$、與輸入獨立（discrete-time AWGN），average power constraint $\frac1n\sum x_i^2\le P$。

**計算**：
$$\begin{aligned}
I(X;Y)&=h(Y)-h(Y|X)=h(Y)-h(X+Z|X)\\
&=h(Y)-h(Z|X)\qquad(\text{平移不變})\\
&=h(Y)-h(Z)\qquad(Z\text{ 和 }X\text{ 獨立}).
\end{aligned}$$
- 【口頭】**加性雜訊**這個性質之所以重要，就在這裡：實際通訊碰到的都是相加雜訊。
- $h(Z)=\frac12\log_2(2\pi e\sigma^2)$ 是自然界的，不能改。
- 要讓 $h(Y)$ 最大——**輸出越豐富越好**：輸入有一點微小的變化，輸出就有連動的變化，細節越多越能了解 $X$。
- $E[Y^2]=E[X^2]+\sigma^2\le P+\sigma^2$，同 variance 下高斯的 $h$ 最大：
$$h(Y)\le\frac12\log_2\left(2\pi e(P+\sigma^2)\right).$$
- **何時等號**：要 $Y=X+Z$ 是高斯。高斯加高斯還是高斯（高斯是大數法則的收斂行為；獨立的小現象加起來還是高斯），所以只要 **$X\sim\mathcal N(0,P)$**，$Y\sim\mathcal N(0,P+\sigma^2)$。

$$C(P)=\frac12\log_2\left(2\pi e(P+\sigma^2)\right)-\frac12\log_2(2\pi e\sigma^2)=\boxed{\frac12\log_2\left(1+\frac P{\sigma^2}\right)}\ \text{bits / channel use}.$$

【口頭】
- 非常有名的公式，第一個導出來的就是 AWGN 下的公式。要達到一定要用**高斯輸入**——實作上不可能（輸入一會 0.3、一會 −0.6、3.2、−6.8，太細微），實際是 ±1、±3、±5。但它是一個指標：輸入只有 power 限制、沒有量化限制時的理論最大值。
- 其他通道也一樣：雜訊是 Laplacian（光學），就用光學最好的輸入。這類大數法則下量出來的分布（Poisson 加 Poisson、Cauchy 加 Cauchy……）屬於 **infinitely divisible** 的一族，都有「加起來同型」的性質。
- 畫出來確實是 concave。

---

## 6. 連續通道的 block code

[▶ 29:37](https://youtu.be/wVTBjnPhjlE?t=1777)

**Definition 5.31**（p. 189）：$(n,M)$ 碼，codeword $c=(c_1,\dots,c_n)\in\mathbb R^n$——不再限 ±1、±3，例如代表 00 的 codeword 可能是 $(0.2,0.8,-0.2,-0.8,0.66,\dots)$——而且**每個 codeword 都要滿足**
$$\frac1n\sum_{i=1}^nc_i^2\le P.$$
Decoder 從收到的實數猜送了哪個 message。

【口頭】實作上幾乎不可能這樣設計（每個值都要調），為什麼要調這些數字？是要逼近高斯的樣子：小的值多、大的值少。

---

## 7. Theorem 5.32：Gaussian channel 的 coding theorem

[▶ 31:09](https://youtu.be/wVTBjnPhjlE?t=1869)

**Theorem 5.32（Shannon's coding theorem for the memoryless Gaussian channel）**（p. 190）：AWGN，power constraint $P$、noise variance $\sigma^2$，$C(P)=\frac12\log_2(1+\frac P{\sigma^2})$。
- **Forward**：對任意 $\varepsilon\in(0,1)$，存在 $0<\gamma<2\varepsilon$ 和 block code 序列，$\frac1n\log_2M_n>C(P)-\gamma$，**每個 codeword 滿足 power constraint**，且 $P_e<\varepsilon$（$n$ 夠大）。
- **Converse**：codeword 都滿足 power constraint 的碼序列，若 $\liminf\frac1n\log_2M_n>C(P)$，錯誤率 bounded away from zero。

【口頭】
- 例：$P=2$ W，$C(P)$ 也許是 1.8，那 1.79、1.799 都做得到——$C(P)-\gamma$ 的速度、錯誤率任意小（reliable）。
- Converse：rate 是 $2C$ 時，錯誤率至少 $1-\frac12=\frac12$。這裡用 Fano 證 weak converse；實際上 AWGN 是 **strong converse**：一超過 capacity，最好的方法錯誤率也趨近 1——天然的界線。

---

## 8. Forward part：多出來的 power constraint

[▶ 33:45](https://youtu.be/wVTBjnPhjlE?t=2025)

兩個熟悉的想法：
1. **Random coding**（Shannon 不知道怎麼設計，1948 到 1998 年才在 AWGN 上真正達到）：隨機產生碼，算錯誤率的期望值；平均 $<\varepsilon$ ⇒ 存在一個碼 $<\varepsilon$（全班平均低於 80 分，一定有人低於 80）。
2. **Typical set decoding**：$n$ 很大時輸入、輸出形成一對一的 pair（$x_1\leftrightarrow y_1$、$x_2\leftrightarrow y_2$），外面機率 $\delta$ 很小、亂猜沒關係；裡面 AEP，每個一樣重要。

**新的條件**：每個 codeword 都要滿足 $\frac1n\sum c_i^2\le P$。
- 【口頭】怎麼讓隨機產生的碼自動符合？用**大數法則**：若 $c_i$ 依某分布 i.i.d. 產生、$E[c_i^2]$ 比 $P$ 小一點，$n$ 大時 $\frac1n\sum c_i^2$ 會集中在期望值附近，幾乎都符合。

**技巧：目標是 $P-\xi$ 而不是 $P$**（課本 pp. 190–192）：
- 因為 $C(\cdot)$ concave 且遞增 ⇒ **連續**（若有 jump，兩邊各取一點拉直線會掉到曲線下面，違反 concave）。所以可以選很小的 $\xi>0$ 使 $C(P)-C(P-\xi)<\frac\gamma2$，於是 $C(P-\xi)-\frac\gamma2>C(P)-\gamma$。
- 選 $M_n$ 讓 $\frac1n\log_2M_n$ 落在適當的區間，$\delta=\frac\gamma8$。
- 隨機選碼用達到 $C(P-\xi)$ 的高斯分布（$E[X^2]=P-\xi<P$），i.i.d.。
- 【口頭】圖像：$\frac1n\sum X_i^2$ 的分布以 $P-\xi$ 為中心，$n$ 越大越窄，最後 99.9999% 的機率都落在 $P$ 的左邊——power constraint 自動符合。

**Step 1（code construction）多一個規則**：隨機產生的 codeword 若**違反** power constraint（機率很小，但連續分布從 $-\infty$ 到 $\infty$，例如產生出 8.2、80.3、……、−92.1），就**整個換成全 0**（全 0 一定滿足）。
- 【口頭】例：$M=4$、$n=10$，隨機產生 40 個實數；檢查每個 codeword 的平均平方，有一個大於 1，就把它換成 0。兩個都被換成 0 時這個碼很爛（接收端分不開），但發生機率很低。
- 【口頭】當 $n$ 很大（例如 18 萬），用亂數產生的碼其實都還不錯，有人做過；但 $n$ 很大處理負擔大，一般還是要在合理長度找好設計。

**錯誤率**：比離散情形多一項——令 $\mathcal E_0$ 是「有 codeword 違反 power constraint」的事件，一旦發生就當整個系統錯（錯誤率當 1）。
$$E[P_e]\le\Pr[\mathcal E_0]+\Pr[\text{沒有人和 }Y^n\text{ jointly typical}]+\Pr[\text{別人也 jointly typical}].$$
- 後兩項和離散證明一樣，都很小。
- 第一項：由大數法則，$\Pr\left[\frac1n\sum X_i^2>P\right]\to0$（期望值是 $P-\xi$）。
- 【口頭】證明時把積分範圍拆成 $\mathcal E_0$ 和 $\mathcal E_0^c$，在 $\mathcal E_0$ 上放大成整個範圍，就只多這一項。

**為什麼限制要寫成平均**（【口頭】）[▶ 53:11](https://youtu.be/wVTBjnPhjlE?t=3191)：$\frac1n\sum c_i^2$ 這種**平均（可加）**的形式才有大數法則。若限制是 $\max c_i^2\le P$ 或其他函數，可能就沒有這麼好的性質。剛好工程上的 cost constraint 也是平均——數學需要和工程需求一致。之後 rate-distortion 的 distortion 也要是「每個 distortion 加起來平均」的形式，同樣是為了大數法則。

---

## 9. Converse part：Fano + concavity

[▶ 55:45](https://youtu.be/wVTBjnPhjlE?t=3345)

（課本 pp. 192–193）對所有設計都要成立，所以用 Fano。
- **DPI**（連續也對）：$W\to X^n\to Y^n$，$I(W;Y^n)\le I(X^n;Y^n)$。
- **$W$ uniform**：假設做壓縮的人用最好的壓縮方法，輸出一定 uniform（否則沒壓好），所以 $H(W)=\log_2M_n$。
- **用 concavity**：
$$I(X^n;Y^n)\le\sum_{i=1}^nI(X_i;Y_i)\le\sum_{i=1}^nC(P_i)=n\cdot\frac1n\sum_iC(P_i)\le nC\left(\frac1n\sum_iP_i\right)\le nC(P),$$
  其中 $P_i=E[X_i^2]$，$\frac1n\sum P_i\le P$。
  - 第一步：一起談判（joint）比各自談判的總和小——各自談會重複傳。
  - 第三步：$C$ concave——$n$ 個點的平均（權重 $\frac1n$）落在曲線下方（三點連成三角形、四點連成四邊形，都在 concave 曲線下面）。
  - 【口頭】這是連續通道多出來的步驟：連續通道一定要談 cost constraint。
- **Fano**：
$$\log_2M_n=H(W)=H(W|Y^n)+I(W;Y^n)\le1+P_e\log_2M_n+nC(P),$$
  移項得 $P_e\ge1-\frac{C(P)+1/n}{\frac1n\log_2M_n}$，$n$ 大時就是 $1-\frac C R$——rate 比 $C(P)$ 大就不可能錯誤率任意小。∎

【口頭】這個定義量（$\frac12\log(1+P/\sigma^2)$）終於有了操作上的意義：average power $\le P$ 下最大的可靠傳輸率。

---

## 10. 高斯雜訊讓 capacity 最小

[▶ 62:54](https://youtu.be/wVTBjnPhjlE?t=3774)

**Theorem 5.33**（p. 194）：任何加性雜訊（有 pdf、mean 0、variance $\sigma^2$）的離散時間連續無記憶通道，在 power constraint $P$ 下，
$$C(P)\ge\frac12\log_2\left(1+\frac P{\sigma^2}\right).$$
即雜訊不是高斯時 capacity **比較大**——**高斯是最難對付的雜訊**（在相同雜訊能量下）。

【口頭】證明：兩個通道，一個是高斯雜訊、一個不是。碰到不等式就相減、展開 mutual information，裡面一定有 log，再用 FI 或 log-sum 就做完了（中間步驟要稍微調整），不用背。

**Log scale**（【口頭】）：
- 有人證明，不管是不是高斯，capacity-cost function 大多和 $\log(\text{SNR})$ 成比例。
- 但有些通道是 **log-log**：例如 fading 未知、無法對付的 **non-coherent fading channel**，$n$ 很大時是 log-log scale——用能量換傳輸速度換得更辛苦。老師說這應該是 David Shea（逐字稿音譯）他們做的。

> ⚠️ 待確認：[▶ 65:28](https://youtu.be/wVTBjnPhjlE?t=3928) 「David Shea 他們做出來的」人名聽不清楚，課本這一節沒有提到 log-log 的結果。

【課本補充】Observation 5.35（pp. 195–196）：memoryless fading channel $Y_i=A_iX_i+Z_i$（$A_i$ 通常是 Rayleigh 或 Rician，$E[A_i^2]=1$）。若 decoder 知道 fading 係數（decoder side information，例如用 pilot 訊號估計），capacity 是 $\max I(X;Y|A)$，可以像 AWGN 一樣算；另有 encoder、decoder 都知道 fading 的情形。

---

## 11. 一頁速查表

**連續 AEP**：$-\frac1n\log_2f(X^n)\to h(X)$；typical set 體積 $\approx2^{nh(X)}$（$(1-\delta)2^{n(h-\delta)}\le\mathrm{Vol}\le2^{n(h+\delta)}$），機率 $>1-\delta$。

**為什麼要 cost constraint**：無限制的連續輸入可以把位階間距拉到無限大，capacity $=\infty$；代價是 power。

**Capacity-cost function**：$C(P)=\sup_{E[t(X)]\le P}I(X;Y)$；遞增、concave（time sharing 在曲線下方）⇒ 連續。

**AWGN**：$Y=X+Z$，$Z\sim\mathcal N(0,\sigma^2)$，$\frac1n\sum x_i^2\le P$。
- $I=h(Y)-h(Z)$（平移不變 + 獨立）；$h(Y)\le\frac12\log_2(2\pi e(P+\sigma^2))$。
- $C(P)=\frac12\log_2(1+\frac P{\sigma^2})$，由 $X\sim\mathcal N(0,P)$ 達到。

**Coding theorem（Thm 5.32）**
- Forward：random coding 用 $\mathcal N(0,P-\xi)$；違反 power constraint 的 codeword 換成 0；多一項 $\Pr[\frac1n\sum X_i^2>P]\to0$（大數法則）；$C$ 連續保證 $C(P-\xi)\approx C(P)$。
- Converse：$I(X^n;Y^n)\le\sum C(P_i)\le nC(\frac1n\sum P_i)\le nC(P)$（concave）+ Fano ⇒ $P_e\gtrsim1-\frac CR$。
- 限制必須是平均（可加）形式，才有大數法則。

**Thm 5.33**：同 variance 的加性雜訊中，高斯讓 capacity 最小：$C(P)\ge\frac12\log_2(1+\frac P{\sigma^2})$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 多個平行高斯通道、分配 power（water-filling） | 第 25 集（§5.5） |
| 相關的平行高斯通道、非高斯雜訊、band-limited 波形通道 | 第 26 集（§5.6–5.8） |
| Distortion 也要是可加的形式（大數法則） | 第 27–28 集（第 6 章） |
| Shannon limit（BER vs $E_b/N_0$） | 第 31 集（§6.6） |

---

## 附：本集一句話總結

> **連續通道不加限制就能無限傳，所以要用平均 power 限制定義 $C(P)=\sup_{E[X^2]\le P}I(X;Y)$；它是 concave 的，對 AWGN 等於 $\frac12\log_2(1+P/\sigma^2)$，由高斯輸入達到——證明只比離散多一步：讓隨機碼的平均功率靠大數法則自動落在限制內；而高斯雜訊正是讓這個值最小的雜訊。**

---

## ⚠️ 待確認清單

1. [▶ 65:28](https://youtu.be/wVTBjnPhjlE?t=3928) non-coherent fading channel 的 capacity 是 log-log scale，老師說是「David Shea 他們」做的，人名聽不清、課本這一節沒有。

---

*筆記依據陳伯寧老師「消息理論」Lec24 錄影逐字稿（whisper large-v3-turbo，1:06:00）與 Alajaji & Chen 課本 §5.3–5.4 整理。*
