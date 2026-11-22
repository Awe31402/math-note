---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 33
lecture: Lec33 第二部分 Chapter 2 General data compression theorems
date: 待補
video: https://youtu.be/4GeJb46UNsw
notes: 第二部分（information spectrum）課本沒有，只依逐字稿；參考課本文獻 [172] Han, Information-Spectrum Methods in Information Theory
---

# 第 33 集 · Lec33 第二部分第 2 章：一般 source 的固定長度壓縮定理 [▶ 影片](https://youtu.be/4GeJb46UNsw)

← 上一集：[32](32-generalized-information-measures.md) ｜ [總目錄](README.md) ｜ 下一集：[34](34-measure-of-randomness-stochastic-processes.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 33 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（40:10，whisper large-v3-turbo）。第二部分**課本沒有**，數學式依老師口述重建
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：開頭 [00:00] 一大段是亂碼（混了俄、日、韓、葡、泰文）。「block code」聽成「Black Code」，「variable-length code」聽成「invariable lens code／Variance code／Vervalence Code／Variolence Code」，「Lempel–Ziv」聽成「LampleZip」，「Huffman」聽成「Hoffmann」，「asymptotic」聽成「Asympathic／Asymthetic」，「Kraft inequality」聽成「craft inequality／Creative Nequality」，「randomness」聽成「Randoness」，「codeword」聽成「coword／coord／core word」，「code rate」聽成「call rate／col rate」，「epsilon」聽成「absent／Ebsen／Epson」，「threshold」聽成「straight hold／stretch hold」，「Shannon–Fano–Elias」聽成「Shannon Phenol alias」，「Fano inequality」聽成「Pheno／Phenol inequality」，「Chernoff」聽成「chern of」，「Neyman–Pearson」聽成「Newan Pearson」，「supremum」聽成「suprement／Supplement」，「quantile」聽成「框台」，「stationary ergodic」聽成「Station organic／station ergatic」，「Te Sun Han」聽成「提升和」，「information-spectrum」聽成「information spectra」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 兩種壓縮：block code 與 variable-length code](#1-兩種壓縮block-code-與-variable-length-code)
- [2. 預告：混合 source 的例子](#2-預告混合-source-的例子)
- [3. 問題設定](#3-問題設定)
- [4. Forward lemma：錯誤率的上界](#4-forward-lemma錯誤率的上界)
- [5. 為什麼：它其實是在按機率排序](#5-為什麼它其實是在按機率排序)
- [6. Converse lemma：錯誤率的下界](#6-converse-lemma錯誤率的下界)
- [7. General source coding theorem](#7-general-source-coding-theorem)
- [8. Information stable](#8-information-stable)
- [9. 例子：Bernoulli(Θ) source](#9-例子bernoulliθ-source)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集是基礎準備，這一集開始講真正的操作：**任意統計（arbitrary statistics）的 source，用 block code（固定長度碼）壓縮，錯誤率 $\varepsilon$ 時最小的壓縮率是多少**。答案：就是 entropy density 的 spectrum 的 **quantile**——證明只有兩個 lemma、各幾行，**完全不用 typical set**。

【口頭】今天講第二章，可能會帶到第三章。第二章是 block code（錯誤率 asymptotically zero，比較差）；第三章從**寫程式的複雜度（randomness）**的角度看 variable-length code（錯誤率 exactly zero）。

---

## 1. 兩種壓縮：block code 與 variable-length code

[▶ 00:30](https://youtu.be/4GeJb46UNsw?t=30)

【口頭】
- **Block code**：例如 3 bit 有 8 種可能，選機率比較高的 4 個，其他都不要，3 bit 壓成 2 bit。一定會錯（沒辦法完全恢復），錯誤率是 **asymptotically zero**（$n$ 很大時幾乎是 0）。過去用大數法則找 typical set 證明。實際上沒有人在用 block code。
- **Variable-length code**：Lempel–Ziv、Huffman、PKZip、compress、arc 這些壓縮軟體都是。錯誤率要 **exactly zero**（壓成 zip 一定要完全恢復）。過去用 **Kraft inequality** 證明（樹狀壓縮要能完全解回來，$\sum2^{-\ell_i}\le1$）。
- 兩者的壓縮極限在古典情形都是 **entropy**。
- 現在沒有大數法則、typical set 沒用了。Block code 的廣義版本在第二章；variable-length code 本來以為要廣義的 Kraft inequality，後來發現不需要，第三章用全新的觀點（randomness、程式複雜度）來教：寫得出多好的程式，就能做多好的壓縮，一對一對應。

---

## 2. 預告：混合 source 的例子

[▶ 05:08](https://youtu.be/4GeJb46UNsw?t=308)

【口頭】一個黑箱子 source：裡面有很多個 i.i.d. source（0 的機率 0.2、1 的機率 0.8；0.3／0.7；0.4／0.6……），有一個**隨機的 switch** $U$ 挑一個出來送，你只看到 0101，不知道是從哪一個挑的。
- 用 **block code**，即使只要求錯誤率 asymptotically zero（比較鬆），這個 source **完全不能壓縮**：壓縮極限是 1。
- 用 **variable-length code**，錯誤率 exactly zero，卻**可以壓**：極限大約 0.8 幾 bit/bit——例如 0.89 就是 1000 bit 壓到 890 bit、10 萬壓到 8 萬 9，完全恢復。
- 很合理：block code 可以視為 variable-length code 的特例。
- 第二、三章最後會總結在這個例子。

> 來源衝突（兩邊都列）：[▶ 06:41](https://youtu.be/4GeJb46UNsw?t=401) 這裡老師說 variable-length 可壓到「0.8 左右／0.89」；第 34 集算同一類黑箱子 source（switch 的機率 $Z$ 在 $[0,1]$ uniform）時，給的數字是 $E[h_b(Z)]=\frac1{2\ln2}\approx0.72135$ bit/bit。這裡的 0.8 幾可能對應不同的 switch 分布，也可能是口誤。

---

## 3. 問題設定

[▶ 08:12](https://youtu.be/4GeJb46UNsw?t=492)

- Source：任意分布（大數法則不成立也沒關係），用 triangular array $\boldsymbol X=\left\{X^{(n)}\right\}$（粗體）表示；為了方便，字母有限。
- **$(n,M_n)$ block code**：選一個集合 $\mathcal C_n$，裡面 $M_n$ 個長度 $n$ 的 codeword，用 $\lceil\log_2M_n\rceil$ 個 bit 編 index。
- **Code rate** $\frac1n\log M_n$。例：$n=3$、$M_n=4$，rate $\frac23$ bit/source bit；$M_n=2$，rate $\frac13$。越低越好。
- **錯誤率** $P_e=\Pr\left[X^n\notin\mathcal C_n\right]$：沒被選到的就不管了。（古典時 $\mathcal C_n$ 就是 typical set，大約 $2^{nH}$ 個。）
- $T_\varepsilon(\boldsymbol X)$：錯誤率要求 $\varepsilon$ 時最小的可達壓縮率。$\varepsilon\to0$ 代表錯誤率 arbitrarily small；block code 的 $\varepsilon$ 不能等於 0（一定要丟掉一些，否則不能壓縮）。
- DMS 時早就知道答案是 entropy。

---

## 4. Forward lemma：錯誤率的上界

[▶ 12:16](https://youtu.be/4GeJb46UNsw?t=736)

【口頭】這個證明好像沒有證明——prove without proving：定義定完，答案就出來了。

**Lemma（forward）**：對任何 $n$、$M_n$，存在一個 $(n,M_n)$ block code，
$$P_e\le\Pr\left[\frac1n\log\frac1{P_{X^n}(X^n)}>\frac1n\log M_n\right].$$
- 右邊就是 entropy density 的 **complementary CDF** 在 code rate 處的值。所以只要這個量 $<\varepsilon$ 就做完了。
- 操作上關心的「錯誤率 vs. 壓縮率」，直接變成「隨機變數 $A_n$ 大於 $R$ 的機率」——x 軸是壓縮率、y 軸是錯誤率，就是 spectrum。

**證明**（一頁四行）：令
$$\mathcal A_n:=\left\{x^n:\frac1n\log\frac1{P_{X^n}(x^n)}\le\frac1n\log M_n\right\}.$$
- 關鍵觀察：$\frac1n\log\frac1{P(x^n)}\le\frac1n\log M_n\iff\frac1{P(x^n)}\le M_n\iff P(x^n)\ge\frac1{M_n}$（兩邊去掉 $\frac1n$ 和 log，是 if and only if）。
- 所以 $1\ge\Pr[\mathcal A_n]=\sum_{x^n\in\mathcal A_n}P(x^n)\ge|\mathcal A_n|\cdot\frac1{M_n}$，得 $|\mathcal A_n|\le M_n$。
- 取 $\mathcal C_n\supseteq\mathcal A_n$（把 $\mathcal A_n$ 全部放進去，不夠 $M_n$ 個就隨便補）。
- 錯誤率 $=\Pr[X^n\notin\mathcal C_n]\le\Pr[X^n\notin\mathcal A_n]$，就是右邊。∎

【口頭】直觀：用 $\frac1n\log M_n$ 當 threshold 時，能放幾個 codeword 非常清楚：rate $\frac23$（$n=3$）大約 4 個，rate $\frac13$ 大約 2 個。Block code 就是在數個數。

---

## 5. 為什麼：它其實是在按機率排序

[▶ 21:56](https://youtu.be/4GeJb46UNsw?t=1316)

$\frac1n\log\frac1{P(x^n)}$ 這個 x 軸的量：機率**小**的，倒數大、取 log 大，落在**右邊**；機率**大**的（例如 000）落在**左邊**。所以畫這個 CDF 其實是**把所有序列按機率排序**：機率大的在左、小的在右。

【口頭】
- 你只讓我選 4 個、又要錯誤率最小，最好的選擇很單純：**選機率最大的 4 個**，就做完了。
- Neyman–Pearson lemma 說 likelihood ratio test 就足夠找到最好的；資料壓縮用「機率倒數取 log」排序，就得到最好的壓縮碼。Shannon–Fano–Elias code 的長度也是機率倒數取 log——完全抓到 Shannon 的精神。
- Te Sun Han 的話：定義定對了、找到對的量，數學排序就對了。之後 channel capacity 的廣義版本也是按某個量排序。
- 有人批評 information spectrum 好像都在「玩定義」——沒錯，但關鍵是找到對的函數，**讓 x 軸完全反映你操作上關心的量**；這來自三大公設。

---

## 6. Converse lemma：錯誤率的下界

[▶ 18:52](https://youtu.be/4GeJb46UNsw?t=1132)

過去 converse 用 Fano inequality（和操作無關，所以對所有碼都成立）。現在也要和操作無關。

**Lemma（converse）**：對**任何** $(n,M_n)$ block code、任何 $\gamma>0$，
$$P_e\ge\Pr\left[\frac1n\log\frac1{P_{X^n}(X^n)}>\frac1n\log M_n+\gamma\right]-e^{-n\gamma}.$$
- 【口頭】$\gamma$ 是常數（例如 0.00001），只多加一點點；$n\to\infty$ 時 $e^{-n\gamma}\to0$。所以所有碼都一樣爛，錯誤率不可能比「code rate 多一點點處的 complementary CDF」好。
- 上下界一夾，$\gamma$ 任意小 ⇒ 最好的錯誤率就是 complementary CDF 在 code rate 的值。

**證明**（等價於證正確率的上界）：令 $\mathcal B_n:=\left\{x^n:\frac1n\log\frac1{P(x^n)}>\frac1n\log M_n+\gamma\right\}$。
$$\begin{aligned}
1-P_e=\Pr[X^n\in\mathcal C_n]&=\Pr[X^n\in\mathcal C_n\cap\mathcal B_n^c]+\Pr[X^n\in\mathcal C_n\cap\mathcal B_n]\\
&\le\Pr[X^n\in\mathcal B_n^c]+\sum_{x^n\in\mathcal C_n\cap\mathcal B_n}P(x^n).
\end{aligned}$$
- 第一項：兩個條件拿掉一個，機率只會變大。（【口頭】Chernoff 定理的證明也是這樣：用對的量大於、小於做交集。）
- 第二項：在 $\mathcal B_n$ 裡，$\frac1{P(x^n)}>M_ne^{n\gamma}$，即 $P(x^n)<\frac1{M_ne^{n\gamma}}$；$\mathcal C_n$ 最多 $M_n$ 個，所以第二項 $<M_n\cdot\frac1{M_ne^{n\gamma}}=e^{-n\gamma}$。
- 所以 $1-P_e\le1-\Pr[\mathcal B_n]+e^{-n\gamma}$。∎

【口頭】歷史上很多這種例子：推廣到最廣、沒有條件時，反而會想到最真正的精神，證明很簡單；再把限制加回來，得到局限的結果。

---

## 7. General source coding theorem

[▶ 28:00](https://youtu.be/4GeJb46UNsw?t=1680)

令 entropy density $h_n:=\frac1n\log\frac1{P_{X^n}(X^n)}$，inf-spectrum $\underline u(\theta):=\liminf_n\Pr[h_n\le\theta]$。依口述定義
$$\bar H_{1-\varepsilon}(\boldsymbol X):=\sup\{\theta:\underline u(\theta)\le1-\varepsilon\}.$$

**Theorem（general source coding theorem，固定長度）**：錯誤率 $\varepsilon$ 下最小的可達壓縮率
$$T_\varepsilon(\boldsymbol X)=\bar H_{1-\varepsilon}(\boldsymbol X).$$
——就是這個 spectrum 的 quantile。完全沒有 typical set，也不要求任何 typical-set 的行為；古典時極限 CDF 是 step function，結果一樣適用。

**Forward**（rate 取 $\bar H_{1-\varepsilon}+\gamma$）：由 forward lemma，$P_e\le\Pr[h_n>\bar H_{1-\varepsilon}+\gamma]=1-\Pr[h_n\le\bar H_{1-\varepsilon}+\gamma]$。
- 【口頭】比較 tricky 的地方：$\bar H_{1-\varepsilon}$ 是「$\underline u\le1-\varepsilon$ 的 **supremum**」，已經衝到極限、包含所有可能；再往右加一點 $\gamma$，$\underline u$ 就一定 **$>1-\varepsilon$**。代回去，$\limsup P_e<\varepsilon$。
- 全部都是定義來的。

**Converse**（proof by contradiction）：假設 rate 可以比 $\bar H_{1-\varepsilon}$ 還好，即存在 $\gamma>0$ 使 rate $\le\bar H_{1-\varepsilon}-4\gamma$ 且錯誤率 $\le\varepsilon$（$\bar H_{1-\varepsilon}=0$ 時不用證）。用 converse lemma（$\gamma$ 可任意取）：
$$P_e\ge\Pr\left[h_n>\bar H_{1-\varepsilon}-3\gamma\right]-e^{-n\gamma}\ge\Pr\left[h_n>\bar H_{1-\varepsilon}-2\gamma\right]-e^{-n\gamma}.$$
- $\bar H_{1-\varepsilon}-2\gamma$ 在 sup 的左邊，所以 $\underline u(\cdot)\le1-\varepsilon$，即 $\limsup\Pr[h_n>\cdot]\ge\varepsilon$；而且嚴格在 sup 左邊，可以得到錯誤率 $>\varepsilon$，矛盾。

**讀圖**：
- 錯誤率要 $\to0$：取 $\varepsilon\to0$，即 $1-\varepsilon\to1$，就是分布的**右端** $\bar H(\boldsymbol X)$（limsup in probability）。
- 混合 source 的例子算出來 $\bar H=1$：1000 bit 只能用 1000 bit 存——錯誤率要趨近 0 的 block code 在這個 source 上不可能壓縮。
- $h_n$ converge in probability 到常數時，CDF 是 step function，壓縮極限就是那個常數。

> ⚠️ 待確認：[▶ 29:32](https://youtu.be/4GeJb46UNsw?t=1772) 老師說的是「inf spectrum（小寫 u underbar，limit inf），所有小於 $1-\varepsilon$ 的取 supremum，記作 $\bar H_{1-\varepsilon}$」，上面照這個寫；和第 32 集重建的 $\bar U_\delta$（用 sup spectrum）記號可能不一致，需對照講義。

---

## 8. Information stable

[▶ 35:13](https://youtu.be/4GeJb46UNsw?t=2113)

【口頭】發現這個現象之後：壓縮極限是一個常數、而且有 **strong converse**（rate 低於某值錯誤率是 1、高於某值錯誤率是 0，像 Shannon 找到的臨界值），需要的條件可能比 stationary ergodic 還廣——只要 CDF 是 step function，就有 typical set 的現象。所以取了一個名字：

**Information stable**（依口述）：
$$\lim_{n\to\infty}\Pr\left[\left|\frac{h_n}{E[h_n]}-1\right|>\gamma\right]=0\quad\forall\gamma>0.$$
- 類似「$\frac1n\sum X_i$ 除以期望值、減 1 趨近 0」，只是代的是對的函數。
- 包含 i.i.d.、stationary ergodic；都有非常明顯的臨界現象。

更廣義時，壓縮極限是一個函數（CDF 的反函數）；若沒有臨界現象，就是一個帶狀的範圍（一片）。

---

## 9. 例子：Bernoulli(Θ) source

[▶ 37:14](https://youtu.be/4GeJb46UNsw?t=2234)

**設定**：0101 序列，$\Pr[X=1]=\Theta$，但 $\Theta$ 本身是**隨機變數**，在 $[0,1]$ 上 uniform。
- 【口頭】兩層的分布，有點像 hidden Markov chain（Markov chain 的機率本身也是隨機變數）。就是前面黑箱子的情形：不知道送出來的 1、0 機率是哪一個。
- 資料量一定比較豐富（比 $\Theta$ 是定值 $p$ 時），比較難壓縮。【口頭】也可以告訴你怎麼干擾別人：用這種 01 去干擾，比較難破解。

**結果**：entropy density 不收斂到常數，而是收斂到隨機變數 $h_b(\Theta)$。最好的壓縮率就是 $h_b(\Theta)$ 的 CDF 在 $1-\varepsilon$（正確率）處的 quantile。

> 以下**不是逐字稿內容**，是依上面的定理推論的：$\varepsilon\to0$ 時壓縮極限是 $h_b(\Theta)$ 分布的右端，$\Theta$ uniform 時 $h_b(\Theta)$ 可以任意接近 1（$\Theta$ 接近 $\frac12$），所以 block code 要錯誤率趨近 0 時**不能壓縮**（極限 1 bit/bit），和第 2 節的說法一致。

【口頭】總結：過去非 i.i.d.、很特別的 source 的壓縮極限，現在完全清楚。怎麼達到是另一件事，要後續用工程慢慢做——理論走在前面。

---

## 10. 一頁速查表

**Block code**：選 $M_n$ 個長度 $n$ 的 codeword，rate $\frac1n\log M_n$，$P_e=\Pr[X^n\notin\mathcal C_n]$。

**Forward lemma**：存在碼使 $P_e\le\Pr\left[h_n>\frac1n\log M_n\right]$，$h_n=\frac1n\log\frac1{P(X^n)}$。
- 關鍵：$h_n(x^n)\le\frac1n\log M_n\iff P(x^n)\ge\frac1{M_n}$，所以這種序列最多 $M_n$ 個，全部選進來。

**Converse lemma**：任何碼 $P_e\ge\Pr\left[h_n>\frac1n\log M_n+\gamma\right]-e^{-n\gamma}$。
- 關鍵：拆成 $\mathcal C_n\cap\mathcal B_n^c$ 和 $\mathcal C_n\cap\mathcal B_n$；後者每個機率 $<\frac1{M_ne^{n\gamma}}$，最多 $M_n$ 個。

**定理**：$T_\varepsilon(\boldsymbol X)=\bar H_{1-\varepsilon}(\boldsymbol X)=\sup\{\theta:\liminf_n\Pr[h_n\le\theta]\le1-\varepsilon\}$；$\varepsilon\to0$ 時是 $\bar H(\boldsymbol X)$（分布右端）。

**觀念**：$h_n$ 的 CDF = 按機率排序（大的在左）；選機率最大的 $M_n$ 個就是最好的 block code。

**Information stable**：$\Pr[|h_n/E h_n-1|>\gamma]\to0$ ⇒ step function、strong converse；包含 i.i.d.、stationary ergodic。

**Bernoulli(Θ)**：$h_n\to h_b(\Theta)$（隨機變數）；block code 錯誤率 $\to0$ 時不能壓縮；variable-length 可以（第 34 集）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Variable-length（exactly zero）壓縮、randomness、程式複雜度；Bernoulli(Z) 用 VL 可壓到約 0.72 | 第 34 集（第 3 章） |
| 同樣的「排序 + 兩個 lemma」用在一般 channel | 第 35 集（第 4 章） |

---

## 附：本集一句話總結

> **任意統計的 source 用固定長度碼壓縮時，畫出 $\frac1n\log\frac1{P(X^n)}$ 的分布——它其實就是把序列按機率排序——選機率最大的 $M_n$ 個就是最好的碼；兩個各幾行的 lemma 夾出：錯誤率 $\varepsilon$ 下的壓縮極限就是這個分布在 $1-\varepsilon$ 的 quantile，錯誤率趨近 0 時就是分布的右端。**

---

## ⚠️ 待確認清單

1. [▶ 29:32](https://youtu.be/4GeJb46UNsw?t=1772) $\bar H_{1-\varepsilon}$ 用 inf spectrum 定義（照口述），和第 32 集重建的記號可能不一致，需對照講義。

---

*筆記依據陳伯寧老師「消息理論」Lec33 錄影逐字稿（whisper large-v3-turbo，40:10）整理；第二部分課本沒有。*
