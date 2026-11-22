---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 35
lecture: Lec35 第二部分 Chapter 4 Channel coding theorems and approximations of output statistics for arbitrary channels
date: 待補
video: https://youtu.be/kexuyKvHOGA
notes: 第二部分（information spectrum）課本沒有，只依逐字稿；名詞對照課本參考文獻 [396] Verdú–Han、[175] Han–Verdú
---

# 第 35 集 · Lec35 第二部分第 4 章：任意通道的 channel coding theorem 與 output statistics [▶ 影片](https://youtu.be/kexuyKvHOGA)

← 上一集：[34](34-measure-of-randomness-stochastic-processes.md) ｜ [總目錄](README.md)

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 35 集（最終集）
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:14:16，whisper large-v3-turbo）。第二部分**課本沒有**，數學式依老師口述重建
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：開頭「創作人Dию的 Gamages」是亂碼。「approximation of output statistics」聽成「apprasmation or opposite statistic／Approsmation of Output Distance」，「computer resolvable」聽成「computer reservable」，「Feinstein」聽成「Feynstein／Finescent」，「Gaussian」聽成「高宣／高濕／高薰」，「大數法則」聽成「大樹法則」，「Shannon」聽成「Shanen」，「Venn 圖」聽成「文式圖」，「epsilon」聽成「absent／absolent」，「codeword」聽成「co-word／Cover」，「twisted distribution」聽成「twist distribution」，「importance sampling」聽成「important sampling」，「Viterbi」正確，「MIMO」正確，「Verdú、Han」聽成「Verdue、Hunt」，「resolvability」聽成「resorbability」，「variable-length」聽成「Variolence」，「三大公設」聽成「三大公社」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼 output statistics 重要](#1-為什麼-output-statistics-重要)
- [2. 回到原點：information density](#2-回到原點information-density)
- [3. 問題設定與結果](#3-問題設定與結果)
- [4. Feinstein's lemma（forward）](#4-feinsteins-lemmaforward)
- [5. Feinstein 的證明：一個一個挑 codeword](#5-feinstein-的證明一個一個挑-codeword)
- [6. Converse：從最好的決定（MAP）出發](#6-converse從最好的決定map出發)
- [7. 例子：三輸入的通道](#7-例子三輸入的通道)
- [8. 證明 converse 的不等式](#8-證明-converse-的不等式)
- [9. Twisted distribution 與 importance sampling](#9-twisted-distribution-與-importance-sampling)
- [10. ε-capacity、capacity、strong capacity、separation](#10-ε-capacitycapacitystrong-capacityseparation)
- [11. 例子：二元加性雜訊](#11-例子二元加性雜訊)
- [12. Channel resolvability](#12-channel-resolvability)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 全課回顧](#14-全課回顧)

---

## 0. 這堂課要做什麼

最後一集：把 channel coding theorem 推廣到**任意通道**（沒有大數法則、non-stationary、triangular array），並連到 **approximation of output statistics**（channel resolvability）。
- **Forward**：**Feinstein's lemma**（1954）——不用 random coding，而是真的一個一個挑 codeword。
- **Converse**：從最好的決定（MAP）出發的錯誤率下界，用到一個簡單的不等式，再加上 **twisted distribution**。
- 結果：錯誤率 $\varepsilon$ 下的 capacity 就是 information density spectrum 的 quantile；**capacity** 是分布的**左端**、**strong capacity** 是右端。
- Source 和 channel 的兩條曲線不相交時才能 separation。

---

## 1. 為什麼 output statistics 重要

[▶ 00:00](https://youtu.be/kexuyKvHOGA?t=0)

【口頭】
- 數學上：給輸入分布 $P_{X^n}$，經過 $P_{Y^n|X^n}$，算得到輸出分布 $P_{Y^n}$——純數學。
- 實際上：你設計一個碼（例如 0000、0011……），每個 codeword 被用的機率 uniform（例如各 $\frac14$），這是 **computer resolvable**（實際寫得出來的）輸入；它也產生一個輸出分布。
- 我們希望兩個輸出分布**長得一樣**（variational distance 很小）——**approximation of output statistics**。
- 為什麼重要：後來發現**輸出分布才是決定錯誤率的重點**，不是輸入。Receiver 才決定接收好不好（receiver 比較難做，因為有雜訊 $Y|X$ 的不穩定性；傳送端比較好做）。
- Channel capacity 是找一個輸入分布，讓輸入和輸出的機率連動最大（輸入有一點改變，輸出馬上知道）。實際輸入不可能和它一樣，但只要**產生一樣的輸出分布**，就是好的碼——所以不需要高斯輸入，只要輸出很接近高斯就行。這就是「隔一層」的 resolvability。

---

## 2. 回到原點：information density

[▶ 03:38](https://youtu.be/kexuyKvHOGA?t=218)

- 以前 Shannon 的 capacity 都在大數法則下用 typical set 證明；現在雜訊可能太複雜、隨時間改變（non-stationary），根本沒有大數法則。甚至是 triangular array：用長度 1000 送很不好，長度 1200 反而剛好符合通道的某種特性。
- Shannon 三大公設得到 $\log\frac1P$。他定義通訊時用期望值的 Venn 圖（$I=H(X)+H(Y)-H(X,Y)$）——先取期望值再相減，在大數法則下剛好對。
- 現在不取期望值，先算**某一個 $x$、某一個 $y$ 的連動量**：
$$\log\frac1{P(x)}+\log\frac1{P(y)}-\log\frac1{P(x,y)}=\log\frac{P(x,y)}{P(x)P(y)}.$$
  這就是 **information density**（真正的 sufficient statistic），期望值就是 mutual information。
- 不收斂沒關係：把它當 **x 軸**（你關心的量），y 軸是錯誤率，畫
$$\frac1ni(X^n;Y^n):=\frac1n\log\frac{P_{X^nY^n}(X^n,Y^n)}{P_{X^n}(X^n)P_{Y^n}(Y^n)}=\frac1n\log\frac{P_{Y^n|X^n}(Y^n|X^n)}{P_{Y^n}(Y^n)}$$
  的 CDF；錯誤率 $10^{-5}$ 對到的 x 就是能達到的傳輸速度。
- 一般寫成後面的形式，因為接收端看的是 output distribution：$Y|X$ 和 $Y$ 之間的差異。

---

## 3. 問題設定與結果

[▶ 09:23](https://youtu.be/kexuyKvHOGA?t=563)

**$(n,M)$ 碼**：$M$ 個 message 對到長度 $n$ 的 codeword，接收端收到後猜回來；錯誤率是猜錯的機率。固定長度（實作上很少人做不定長度：封包要送 2000、3000 bit，接收端也知道）。
- 假設 message **uniform**：送之前都會做資料壓縮，最好的壓縮輸出一定是 uniform（不然還可以再壓，例如從 1000 壓到 700）。
- **Capacity**：錯誤率在 $n\to\infty$ 時為 0 的前提下，最大的 rate（用 limsup）。

**結果**（老師說 1993 年是 resolvability，1994 年 Verdú–Han 證明 capacity）：
$$C=\sup_{\boldsymbol X}\underline I(\boldsymbol X;\boldsymbol Y),$$
即 information density 分布的**左端**。
- Forward 用 **Feinstein's lemma**（Feinstein 在 1954 年左右的結果，不用大數法則就能證明存在性；當時沒什麼人注意，93、94 年大家才覺得它很重要）。
- Converse 是老師自己的結果。

【課本補充】課本參考文獻 [396] S. Verdú, T.S. Han, *A general formula for channel capacity*, IEEE Trans. IT 40(4)（1994）；老師與 Alajaji 的相關論文見 [72]–[76]（例如 [75] *Optimistic Shannon coding theorems for arbitrary single-user systems*）。

---

## 4. Feinstein's lemma（forward）

[▶ 11:24](https://youtu.be/kexuyKvHOGA?t=684)

**Lemma（Feinstein，依口述）**：對任何輸入分布 $P_{X^n}$、任何 $\gamma>0$，存在 $(n,M)$ 碼使
$$P_e\le\Pr\left[\frac1ni(X^n;Y^n)\le\frac1n\log M+\gamma\right]+e^{-n\gamma}.$$
- 【口頭】形式和資料壓縮的 lemma 完全一樣，但**證明完全不一樣**，比較長（要花 20 分鐘以上），很巧妙。
- 它把錯誤率和 information density 的統計現象串在一起：右邊是 information density 小於「你要的 rate 加一點點」的機率。
- 例：rate 2 bit/次，$\gamma=0.0001$，$e^{-n\gamma}\to0$；CDF 在 2.0001 處對到 $10^{-2}$，就一定存在一個方法以這個速度傳、錯誤率 $10^{-2}$。

---

## 5. Feinstein 的證明：一個一個挑 codeword

[▶ 14:26](https://youtu.be/kexuyKvHOGA?t=866)

【口頭】Feinstein 一開始就知道結果：information density 決定錯誤率。

**Step 0：好的集合**。令
$$G:=\left\{(x^n,y^n):\frac1ni(x^n;y^n)>\frac1n\log M+\gamma\right\},\qquad\nu:=P_{X^nY^n}(G^c)+e^{-n\gamma}.$$
- $G$ 是「正確」的集合：information density 大 = 連動好（例如送 QPSK 的 $(-1,-1)$ 得到某個 $y$，代入函數值大，就是好的 pair）。和 typical set 不同，這裡沒有「一對一」的現象。
- 若 $\nu\ge1$，不等式自動成立（錯誤率 $\le1$），所以只需處理 $\nu<1$。
- $P(G^c)<\nu$，即 $P(G)>1-\nu$——第一個重要式子。

**Step 1：對每個輸入看好的輸出**。$G_{x^n}:=\{y^n:(x^n,y^n)\in G\}$——固定輸入，把在好集合裡的 $y$ 集合起來。
- 「好的輸入」：$P_{Y^n|X^n}(G_{x^n}|x^n)>1-\nu$（正確率至少 $1-\nu$）。令 $A$ 是所有好輸入的集合。
- **$A$ 不是空集合**：否則每個 $x^n$ 都有 $P(G_{x^n}|x^n)\le1-\nu$，平均起來 $P(G)\le1-\nu$，和 $P(G)>1-\nu$ 矛盾。

**Step 2：一個一個挑（without replacement）**。
- 挑第一個 codeword $x_1\in A$，decoding 集合 $\Gamma_1:=G_{x_1}$。收到 $y\in\Gamma_1$ 就猜 $x_1$，外面不管。正確率 $>1-\nu$。
- **If possible**，挑第二個 $x_2$，使 $P\left(G_{x_2}\setminus\Gamma_1\,\middle|\,x_2\right)>1-\nu$，$\Gamma_2:=G_{x_2}\setminus\Gamma_1$——扣掉前面的，接收端解碼才不會 ambiguous（$n$ 大時交集的機率很低，好的集合裡 $x,y$ 幾乎又一對一）。
- 第 $i$ 個：$\Gamma_i:=G_{x_i}\setminus\bigcup_{j<i}\Gamma_j$，要求 $P(\Gamma_i|x_i)>1-\nu$。
- 【口頭】這和 random coding 不同：random coding 是 **with replacement**（第二個可以和第一個一樣，那就很糟、分不開）；這裡是真的在設計。
- Encoder：message $i\mapsto x_i$；decoder：$y\in\Gamma_i$ 就猜 $i$。每個 codeword 的錯誤率 $<\nu$。

**Step 3：一定挑得到 $M$ 個**（proof by contradiction）。假設最多只挑到 $N<M$ 個，令 $F:=\bigcup_{i=1}^N\Gamma_i$。
- **裡面**：$\Gamma_i\subseteq G_{x_i}$，在 $G$ 裡 $P_{Y|X}(y|x_i)>Me^{n\gamma}P_Y(y)$，所以 $P_Y(\Gamma_i)<\frac{1}{M}e^{-n\gamma}P(\Gamma_i|x_i)\le\frac{e^{-n\gamma}}M$。於是
$$P_{X^nY^n}\left(G\cap(\mathcal X^n\times F)\right)\le P_Y(F)<N\cdot\frac{e^{-n\gamma}}M<e^{-n\gamma}.$$
- **外面**：挑不到第 $N+1$ 個，代表對**每個** $x$，$P(G_x\setminus F|x)\le1-\nu$，平均 $P\left(G\cap(\mathcal X^n\times F^c)\right)\le1-\nu$。
- 相加：$P(G)<e^{-n\gamma}+1-\nu=1-P(G^c)$，即 $P(G)+P(G^c)<1$，矛盾。∎

> 以下**不是逐字稿內容**，是依口述的步驟補齊的推導細節（「裡面」的機率上界與最後的矛盾式）；老師口述是「這兩個機率相加……這個不等式就不成立」。

【口頭】
- 概念：**裡面和外面分開處理**——重點集合 $F$ 和外面不關心的部分（就像 typical set 裡外）。工程上不是要做完美，是要**抓重點**：選舉要先抓目標群眾、教學要抓整本書的重點。
- 設計方法：64 支天線要處理 64×64 的矩陣，要省成本，就用 information density 把比較小的忽略掉。
- 這個證明本身就是一個設計方法：例如 BPSK 經高斯雜訊，把所有 ±1 序列代入 information density、排序、分類、一個一個檢查。老師的團隊試過，$n$ 十幾（BSC）還能硬找；超過 20 左右現在的電腦就做不到了（要檢查的配對太多）。理論上可行，實作上要電腦非常快。

---

## 6. Converse：從最好的決定（MAP）出發

[▶ 38:56](https://youtu.be/kexuyKvHOGA?t=2336)

**要證**：不管怎麼設計，錯誤率有天然的界線——rate 減一點點（例如 2 變 1.999）對到的 CDF 值，再乘上 $(1-e^{-n\gamma})$（$\to1$）。證明方法：找**最好的**設計，最好的都比它大，差的當然也比它大。

**Lemma（依口述）**：$X$ 有限（8、16、32 個輸入），$Y$ 任意（可以是連續的，如高斯）。最好的錯誤率滿足
$$P_e\ge(1-\alpha)\Pr\left[P_{X|Y}(X|Y)\le\alpha\right].$$

**和 information density 的關係**：uniform 輸入 $P_X=\frac1M$，
$$P_{X|Y}(x|y)\le\alpha\iff\frac{P_{X|Y}(x|y)}{P_X(x)}\le M\alpha\iff\frac1ni(x;y)\le\frac1n\log M+\frac1n\log\alpha,$$
因為 $\log\frac{P_{X|Y}}{P_X}=\log\frac{P_{XY}}{P_XP_Y}=\log\frac{P_{Y|X}}{P_Y}$ 都是 information density 的不同寫法。取 $\alpha=e^{-n\gamma}$：
$$P_e\ge\left(1-e^{-n\gamma}\right)\Pr\left[\frac1ni(X^n;Y^n)\le\frac1n\log M-\gamma\right].$$

**為什麼寫成 $P_{X|Y}$**【口頭】：最好的決定是**事後機率**（MAP）——收到 $y=2.1$，猜 +1 還是 −1，看哪個機率高就猜誰，沒有更好的了。所以 $P_{X|Y}$ 的**排序**非常重要；好的集合 $G$ 從 decoder 的觀點就是看這個機率。uniform 輸入讓它自然和 information density 扯上關係（兩邊除以 $\frac1M$，只差常數），再取 $\frac1n\log$ 就和 code rate 扯上關係。

---

## 7. 例子：三輸入的通道

[▶ 50:46](https://youtu.be/kexuyKvHOGA?t=3046)

輸入 $\{0,1,2\}$ uniform，輸出 $\{0,1,2\}$，量測到的 $P_{Y|X}$：

| | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | 1 | 0 | 0 |
| $x=1$ | 1/2 | 1/2 | 0 |
| $x=2$ | 0 | 1/2 | 1/2 |

- $P_Y=\left(\frac12,\frac13,\frac16\right)$。
- 事後機率 $P_{X|Y}$（每個 column 和為 1）：$y=0$：$x=0$ 機率 $\frac23$、$x=1$ 機率 $\frac13$；$y=1$：$x=1,2$ 各 $\frac12$；$y=2$：$x=2$ 機率 1。
- 最好的猜法（MAP）：收到 0 猜 0；收到 1 猜 1 或 2（一樣，任意挑）；收到 2 猜 2。
- 正確率 $=\frac12\cdot\frac23+\frac13\cdot\frac12+\frac16\cdot1=\frac23$。

**一般化**：令 $h_1(y)\ge h_2(y)\ge h_3(y)$ 是 $P_{X|Y}(\cdot|y)$ 排序後的值（第一大、第二大、第三大）。最好的正確率
$$P_c=E_Y\left[h_1(Y)\right]$$
——對 $Y$ 取期望值，代的是**排序第一**的事後機率。

---

## 8. 證明 converse 的不等式

[▶ 56:53](https://youtu.be/kexuyKvHOGA?t=3413)

數學的量 $\Pr\left[P_{X|Y}(X|Y)>\alpha\right]=E_Y\left[\sum_jh_j(Y)\mathbf 1\{h_j(Y)>\alpha\}\right]$：把所有大於 $\alpha$ 的事後機率加起來（例如 $\alpha=\frac12$，例子裡 $y=0$ 時只有 $\frac23$ 進來；$\alpha=\frac13$ 以下就全部進來）。只取最大的那一個，只會更小：
$$E_Y\left[h_1(Y)\mathbf 1\{h_1(Y)>\alpha\}\right]\le\Pr\left[P_{X|Y}(X|Y)>\alpha\right].$$

**簡單的不等式**：對 $u\in[0,1]$，
$$u\le\alpha+(1-\alpha)\,u\,\mathbf 1\{u>\alpha\}.$$
- $u\le\alpha$：右邊是 $\alpha\ge u$。
- $u>\alpha$：右邊是 $\alpha+(1-\alpha)u$，這條直線在 $u=0$ 時是 $\alpha$、$u=1$ 時是 1，在 $[0,1]$ 上 $\ge u$。
- 【口頭】它就是「$u$ 和 $u\mathbf 1\{u>\alpha\}$ 之間的關係」的一個變形，是一個兩段的（piecewise）函數。

代 $u=h_1(Y)$、取期望值：
$$P_c=E[h_1(Y)]\le\alpha+(1-\alpha)E\left[h_1\mathbf 1\{h_1>\alpha\}\right]\le\alpha+(1-\alpha)\Pr[P_{X|Y}>\alpha],$$
所以 $P_e=1-P_c\ge(1-\alpha)\Pr[P_{X|Y}(X|Y)\le\alpha]$。∎

【口頭】這個證明的概念好像沒什麼特別，但它提供了很重要的結果：傳送速度 vs. 錯誤率的上界、下界都有了，最好的 $10^{-2}$ 錯誤率直接代這個 CDF 就得到，而且任何統計都能用。

---

## 9. Twisted distribution 與 importance sampling

[▶ 44:06](https://youtu.be/kexuyKvHOGA?t=2646)

老師的版本多一個參數 $\theta$：把事後機率取 $\theta$ 次方再 normalize，
$$h_j^{(\theta)}(y):=\frac{h_j(y)^\theta}{\sum_kh_k(y)^\theta}.$$
- 例：收到 $y=2$，$P(+1|y)=0.8$、$P(-1|y)=0.2$。取 $\theta=2$：$0.64$、$0.04$，和是 0.68 不是 1，normalize 成 $\frac{0.64}{0.68}\approx0.94$、$\frac{0.04}{0.68}\approx0.06$——**大的更大、小的更小**，兩者被拉開。$\theta=3$ 更快衝到 1 和 0。
- $h_1^{(\theta)}\ge h_1$（最大值被放大），所以用 $h_1^{(\theta)}\mathbf 1\{\cdot>\alpha\}$ 可以得到更好的界。最後取 $\theta=1$、$\alpha=e^{-n\gamma}$、uniform 輸入，就和 information density 接上。

> ⚠️ 待確認：[▶ 56:22](https://youtu.be/kexuyKvHOGA?t=3382) 加了 $\theta$ 之後的完整下界形式（$\theta$ 放在哪裡、和 $\alpha$ 的關係）逐字稿沒有寫出；上面只寫了 twisted 的定義和「最後代 $\theta=1$」。

**Twisted distribution 的工程應用：importance sampling**【口頭】[▶ 46:39](https://youtu.be/kexuyKvHOGA?t=2799)：
- 70、80 年代有人要看 memory order 很大（例如 2150 這個等級）的 convolutional code 的錯誤率，可能是 $10^{-20}$。要看到 100 個錯誤需要模擬約 $10^{22}$ 次；一年約 $3\times10^7$ 秒（老師口述說「一年才 86400 秒、$10^5$ 秒」是把一天的秒數講成一年），每秒 1000 次也只有 $10^{10}$ 的等級——做不出來。Viterbi 也太大。
- 解法：把**雜訊 twist**（放大會造成錯誤的那些雜訊），讓錯誤率變成 $10^{-5}$，做 $10^7$ 次模擬一天就做完。因為放大的倍率是自己設計的，可以**反推**真正的錯誤率。這叫 **importance sampling**——twist 的目標就是**凸顯**重要的 sample。

> ⚠️ 逐字稿缺字／口誤：[▶ 47:41](https://youtu.be/kexuyKvHOGA?t=2861) 「一年才 86400 秒，一年才 $10^5$ 秒」——86400 是一天的秒數；一年約 $3.15\times10^7$ 秒。

---

## 10. ε-capacity、capacity、strong capacity、separation

[▶ 61:25](https://youtu.be/kexuyKvHOGA?t=3685)

上下界合起來，得到 **ε-capacity**：錯誤率 $\varepsilon$ 下能達到的最大速度，就是 information density spectrum 在 $\varepsilon$ 的 quantile（老師記作 $I_\varepsilon(X;Y)$，取 sup over 輸入）：
$$C_\varepsilon=\sup_{\boldsymbol X}I_\varepsilon(\boldsymbol X;\boldsymbol Y).$$
- **Capacity**（$\varepsilon\to0$）：分布的**左端** $\sup\underline I$——Verdú–Han 證出來的，錯誤率可以 arbitrarily small。
- **Strong capacity** $C_{SC}$：分布的**右端** $\sup\bar I$——速度超過它，所有設計錯誤率都趨近 1。
- 對古典情形也都對（分布是 step function，兩端合一）。

**Information transmission theorem（廣義）**：畫 source 的 entropy density complementary CDF 和 channel 的 information density CDF。選一個 rate，錯誤率 = 壓縮的錯誤（source 曲線那塊）+ 傳輸的錯誤（channel 曲線那塊）。**兩條曲線沒有交集**時，在中間送一定可以完全沒有錯誤，壓縮和傳輸分開做——**separation principle**；有交錯就不能。

【口頭】從大數法則下的古典證明，到現代的廣義解釋，都回到 Shannon 三大公設的延伸。

---

## 11. 例子：二元加性雜訊

[▶ 63:59](https://youtu.be/kexuyKvHOGA?t=3839)

$Y=X\oplus Z$，uniform 輸入：
$$C=\log2-(\text{雜訊的固定長度壓縮極限})=\log2-\bar H(\boldsymbol Z).$$
- 【口頭】**能對付的雜訊，一定是你能壓縮的**：雜訊越豐富、越難壓縮，越難傳送；越好壓縮（你能拆解它、理解它、產生它），就越能傳送。壓縮和傳送的方法是一對一配合的。
- 傳統上先取期望值再加減，只得到上界和下界；現在先代函數 $\log\frac{P_{XY}}{P_XP_Y}$ 再畫 CDF，就合在一起。

**例 1：兩層式雜訊（Bernoulli(Z)，$Z\sim U[0,1]$）**：
- 雜訊用固定長度沒辦法壓縮（$\bar H=1$）⇒ **capacity = 0**，固定長度一個 bit 都送不過去。
- Strong capacity = 1：超過 1 錯誤率一定 100%。
- 但有 **ε-capacity**：工程上還能偷一點——錯誤率要求 $10^{-4}$ 時，還有一點傳送速度。
- 用 **variable-length 傳送碼**（有論文研究，實作上還沒做）可以對付：不定長度壓縮可到 0.72，所以大約有 $1-0.72$ bit/次。

> ⚠️ 逐字稿缺字／口誤：[▶ 67:03](https://youtu.be/kexuyKvHOGA?t=4023) 老師說「不定長度的壓縮可以達到 0.712……1 減掉 0.712……大概 0.2 左右個 bit，傳 10 次大概有兩個 bit」。第 34 集算的是 $\frac1{2\ln2}\approx0.72135$；$1-0.72135\approx0.28$ bit/次（傳 10 次約 2.8 bit）。

**例 2：non-stationary 獨立雜訊**：每個時間 0/1 的機率不同（例如 $P_1=(\frac12,\frac12)$、$P_2=(\frac23,\frac13)$ 交替）。大數法則會收斂，但收斂到**兩個**值（不同長度不同）。Capacity 要看 worst case（雜訊 entropy 最大的那個）；速度比它低，一定存在方法對每個長度都傳得很好。

---

## 12. Channel resolvability

[▶ 68:03](https://youtu.be/kexuyKvHOGA?t=4083)

【口頭】沒有證明，只講概念：
- 數學上有一個最好的輸入分布，讓輸入輸出 mutual information 最大；實際傳送是 computer generated 的碼。目標是兩者的**輸出**接近——理論證明了這樣會有一樣的錯誤率。
- 以前以為：最好的輸入是 0、1 各 $\frac12$，設計的碼 0、1 被用的機率也要各 $\frac12$。後來發現**不在輸入**：高斯雜訊下最好的輸入是高斯，但只要設計一個輸入讓輸出蠻接近高斯就可以了。

**Channel resolvability**（依口述）：存在一個實際可行的輸入（resolution 有限，長度 $n$ 大約花 $nR$ 次 random bit 產生），使輸出和預期輸出的 variational distance $<\varepsilon$——最小的這種 $R$。
- 資料壓縮是特例：無雜訊通道（送 1 得 1、送 0 得 0）時，兩者完全一樣；要讓傳送最有效率就是壓到最低，輸出就是最好的壓縮結果。
- **結果**：channel resolvability = **strong capacity**；channel mean-resolvability = **capacity**。

**Variable-length 傳送**【口頭】：
- 接收端不知道你送哪個 codeword、多長（例如 1、0、01、111 四個，有長有短），要同時猜長度和內容；串接起來（1、01、001……）更難。實作上有困難。
- 但理論上能達到更高的速度：訊息穩定（$X$、$Y$ 連動好）就短短傳一下，不穩定就多送一些。已經有論文證明它的 capacity 比 fixed-length 大。
- 理論走得比實作快：1948 年 Shannon 找到 capacity 公式，到 1998 年才做到，隔了 50 年。同學若很厲害，可以去想怎麼做到不定長度傳送——可能要五十年，等你七十歲搞不好還做不出來，搞不好要一百年。

---

## 13. 一頁速查表

**Information density**：$\frac1ni(X^n;Y^n)=\frac1n\log\frac{P_{Y^n|X^n}}{P_{Y^n}}=\frac1n\log\frac{P_{X^n|Y^n}}{P_{X^n}}$；期望值是 $I$。

**Feinstein（forward）**：存在碼 $P_e\le\Pr\left[\frac1ni\le\frac1n\log M+\gamma\right]+e^{-n\gamma}$。
- $G=\{i/n>\frac1n\log M+\gamma\}$、$\nu=P(G^c)+e^{-n\gamma}$；without replacement 挑 $x_i$ 使 $P(G_{x_i}\setminus\cup_{j<i}\Gamma_j|x_i)>1-\nu$。
- 挑不到 $M$ 個 ⇒ 裡面 $<e^{-n\gamma}$（$P_Y(\Gamma_i)<e^{-n\gamma}/M$）、外面 $\le1-\nu$ ⇒ $P(G)<1-P(G^c)$，矛盾。

**Converse**：$P_e\ge(1-\alpha)\Pr[P_{X|Y}(X|Y)\le\alpha]$。
- MAP：$P_c=E[h_1(Y)]$；$u\le\alpha+(1-\alpha)u\mathbf 1\{u>\alpha\}$。
- uniform 輸入、$\alpha=e^{-n\gamma}$：$P_e\ge(1-e^{-n\gamma})\Pr\left[\frac1ni\le\frac1n\log M-\gamma\right]$。
- Twisted：$h^\theta/\sum h^\theta$，大的更大（importance sampling 的原理）。

**結果**：$C_\varepsilon=\sup I_\varepsilon$（quantile）；$C=\sup\underline I$（左端，Verdú–Han 1994）；$C_{SC}=\sup\bar I$（右端）。
- 二元加性雜訊：$C=\log2-\bar H(\boldsymbol Z)$；Bernoulli(Z) 雜訊 $C=0$、$C_{SC}=1$。
- Separation：source 和 channel 曲線不交錯才行。
- Channel resolvability = strong capacity；mean-resolvability = capacity。

---

## 14. 全課回顧

| 部分 | 核心量 | 核心工具 |
|---|---|---|
| 第一部分（第 1–31 集） | $H$、$I$、$D$、$C$、$R(D)$（期望值） | 大數法則、typical set、random coding、Fano |
| 第二部分（第 32–35 集） | entropy／information density 的分布（spectrum） | quantile、Feinstein、MAP 排序、resolvability |

---

## 附：本集一句話總結

> **任意通道的 capacity 就是 information density $\frac1n\log\frac{P_{Y|X}}{P_Y}$ 分布的左端：forward 用 Feinstein 的「一個一個挑好的 codeword、扣掉已用的解碼區」證明存在，converse 用 MAP 排序加上一個兩段式的不等式；而真正決定錯誤率的是輸出統計——碼不必長得像最佳輸入，只要讓輸出長得像就好。**

---

## ⚠️ 待確認清單

1. [▶ 56:22](https://youtu.be/kexuyKvHOGA?t=3382) 加了 twisted 參數 $\theta$ 之後的完整 converse 下界形式逐字稿沒有寫出。

---

*筆記依據陳伯寧老師「消息理論」Lec35 錄影逐字稿（whisper large-v3-turbo，1:14:16）整理；第二部分課本沒有。*
