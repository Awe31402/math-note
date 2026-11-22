---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 12
lecture: "Lec12 Chapter 3: Lossless Data Compression: 3.1 Principles of data compression"
date: 待補
video: https://youtu.be/k721w58jKLE
notes: Alajaji & Chen §3.1–3.2（pp. 55–73，Definition 3.1–Theorem 3.15 及 redundancy 的討論）
---

# 第 12 集 · Lec12 第 3 章：block code、AEP、Shannon source coding theorem、entropy rate [▶ 影片](https://youtu.be/k721w58jKLE)

← 上一集：[11](11-convexity-information-measures-hypothesis-testing.md) ｜ [總目錄](README.md) ｜ 下一集：[13](13-variable-length-codes-kraft-inequality.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 12 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:34:33，whisper large-v3-turbo）＋ 課本 §3.1–3.2（pp. 55–73）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「lossless」聽成「Losy／Lawsey」，「Shannon」聽成「Shanen／Gannon／學能」，「block length」聽成「black hole／blockland」，「平均碼長」聽成「平均碼糖」，「grade（等第）」聽成「等地」，「DMS（discrete memoryless source）」聽成「discreet memories」，「tuple」正確，「probability measure」聽成「probability major」，「nats」聽成「nets」，「D-ary」聽成「diary／theory」，「Shannon–McMillan–Breiman」聽成「Shannon, Macmillan, Brayman」，「asymptotic equipartition property」聽成「Asymthetic Equal Partition Property」，「Chebyshev」聽成「臺皮血乎」，「Blahut」聽成「Breakwood」，「ε」聽成「absent／Epson」，「Lempel–Ziv」聽成「Lampol Zip／lamp-zip」，「Cesàro mean」聽成「sacero mean／saceral mean」，「Morse」聽成「密碼打電報的碼」，「redundancy」聽成「reundancy」。開頭 [00:00]「音樂曲時節好 詳細的解答應」是 whisper 幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 壓縮問題與平均碼長](#1-壓縮問題與平均碼長)
- [2. 固定碼長、變長碼與 segmentation](#2-固定碼長變長碼與-segmentation)
- [3. Block code 是「有損」的、為什麼還要學](#3-block-code-是有損的為什麼還要學)
- [4. DMS 與 (n, M) block code](#4-dms-與-n-m-block-code)
- [5. 壓縮率與單位](#5-壓縮率與單位)
- [6. Typical set 的想法與例子](#6-typical-set-的想法與例子)
- [7. AEP（Shannon–McMillan–Breiman）](#7-aepshannonmcmillanbreiman)
- [8. AEP 的推論：equipartition](#8-aep-的推論equipartition)
- [9. Shannon source coding theorem](#9-shannon-source-coding-theorem)
- [10. Forward part 的證明](#10-forward-part-的證明)
- [11. Strong converse 的證明](#11-strong-converse-的證明)
- [12. 討論：rate = entropy、uniform 不能壓、weak converse](#12-討論rate--entropyuniform-不能壓weak-converse)
- [13. Stationary source 與 entropy rate](#13-stationary-source-與-entropy-rate)
- [14. Stationary ergodic、Markov source](#14-stationary-ergodicmarkov-source)
- [15. 好的壓縮器、redundancy](#15-好的壓縮器redundancy)
- [16. 一頁速查表](#16-一頁速查表)
- [17. 與後續集數的連結](#17-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】前面是基礎，第 3 章開始講**操作**——完全從操作開始，和數學一點關係都沒有。先講 Shannon 第一定律：**lossless data compression**。

| 主題 | 課本 |
|---|---|
| 平均碼長、固定／變長碼、segmentation | §3.1（pp. 55–57） |
| DMS、$(n,M)$ block code | Definition 3.1–3.2、Observation 3.3（pp. 57–58） |
| AEP 與推論 | Theorem 3.4–3.5（pp. 59–61） |
| Shannon source coding theorem | Theorem 3.6、Table 3.1（pp. 62–66） |
| Entropy rate、Cesàro mean | §3.2.2 Definition 3.8–Theorem 3.11（pp. 66–68） |
| 一般化 AEP、stationary ergodic 版 | Theorem 3.14–3.15（p. 70） |

---

## 1. 壓縮問題與平均碼長

[▶ 00:00](https://youtu.be/k721w58jKLE?t=0)

**問題**：你是工程師。有三個 outcome A、B、C，機率 $\frac12,\frac14,\frac14$。請設計一個方法把它們存起來，讓**平均所需的 storage 最小**。

一種存法：A → 0、B → 10、C → 11。平均碼長
$$1\cdot\tfrac12+2\cdot\tfrac14+2\cdot\tfrac14=1.5\text{ bits}.$$

**機率從哪來**：每一次觀察是 deterministic；觀察 10 萬次，大約一半是 A、1/4 是 B、1/4 是 C，才有統計。所以「平均碼長 1.5」是說 10 萬次需要約 $10^5\times1.5$ bit 的容量。

Shannon 要問：這是不是最好的設計？

---

## 2. 固定碼長、變長碼與 segmentation

[▶ 02:02](https://youtu.be/k721w58jKLE?t=122)

**分類**：
- **變長碼（variable-length code）**：碼長不一樣，例如 0、10、11。一般常用的都是變長碼，例如打電報的摩斯碼（E 最短）。
- **固定碼長（fixed-length code）**：例如 00、01、10。它是變長碼的 subclass。**Shannon 考慮的是固定碼長**；變長碼是後來的。

**Segmentation** [▶ 03:03](https://youtu.be/k721w58jKLE?t=183)：觀察 ABCAAB，固定碼長存成 00 01 10 00 00 01。10 萬次觀察產生 20 萬個 bit，不可能一次處理，所以要切割。

【課本補充】課本的例子（p. 56）：班上 100 個同學，每人成績 A、B、C。
- 一次處理全部：$3^{100}$ 種組合，需要 $\lceil\log_23^{100}\rceil=159$ bits，要一台電腦一次吃 159 bit。
- 若編碼器一次只能處理 16 bits：每 10 人一組，$\lceil\log_23^{10}\rceil=16$ bits；100 人共 160 bits，buffer 和複雜度簡單多了。
- 名詞：A、B、C 叫 source symbol；0、1 叫 code symbol（bit）；一組 source symbol 叫 **sourceword**，編碼後叫 **codeword**。

一個區塊叫一個 **block**，之後常見的名詞 **block length**。Shannon 1948 考慮的就是 **block code**。

---

## 3. Block code 是「有損」的、為什麼還要學

[▶ 05:39](https://youtu.be/k721w58jKLE?t=339)

壓縮的操作有 **block code**（每個區塊固定長度、彼此獨立壓縮，實作方便）和 **tree code**（區塊之間有關聯）。

**重點**：block code 的壓縮**是有損失的**，只是損失在 block length → ∞ 時**漸近（asymptotically）趨近 0**。

**既然實作很少用 block code 壓縮，為什麼要學？**（【口頭】）
- **資料壓縮是資料傳輸的特例**：通道沒有雜訊時，要讓傳輸效率最好，就是把所有額外的部分壓掉、送過去、完全解回來。所以 block code 壓縮是之後做傳輸的基礎。
- 實際的資料壓縮軟體（PKZip、compress……）都是**變長碼**，而且**完全無損（completely lossless）**——錯誤率 100% 是 0，所以變長碼完全不討論錯誤率。
- 有雜訊的傳輸都是 block 在傳（接收端知道區塊大小），所以 channel capacity 是 block code 的 capacity；傳輸會有錯，例如無線通訊標準是 bit error rate $10^{-5}$——長期經驗顯示這個錯誤率使用者感受不到。

---

## 4. DMS 與 (n, M) block code

[▶ 09:41](https://youtu.be/k721w58jKLE?t=581)

**Definition 3.1（discrete memoryless source, DMS）**（p. 57）：$\{X_n\}$ i.i.d.，字母集 $\mathcal X$ **有限**，
$$P_{X^n}(x_1,\dots,x_n)=\prod_{i=1}^nP_X(x_i).$$
- discrete：量化過的（±1、±3）。
- memoryless：統計上的 i.i.d.——不用記得過去（independent），也不用知道現在幾點（identically distributed，統計特性不隨時間變）。
- 下標都寫 $X$，代表來自同一個分布。
- 【口頭】有限字母在 Shannon 早期證明裡很重要；到第二部分（90 年代）會發現有沒有 finite 都不重要。

**Definition 3.2（$(n,M)$ block code）**（p. 58）：block length $n$、size $M$ 的區塊碼是 $M$ 個 $n$-tuple 的集合 $\mathcal C_n=\{c_1,\dots,c_M\}\subset\mathcal X^n$。

- 例：$n=3$、$M=2$，source 是 $\{0,1\}$，可選 $\{000,111\}$。
- **順序 $(n,M)$**（【口頭】）：有的書（Cover、Yeung）寫 $(M,n)$，看書要注意。老師用 $(n,M)$ 的理由：先決定的參數放前面。$M$ 是 $n$ 的函數，因為要固定 **rate**：例如 rate $\frac12$，$n=10$ 時 $M=2^5=32$（送 10 次帶 5 bit）；$n=20$ 時 $M=2^{10}=1024$。
- **Codebook 定義在 source 上，不在 binary 上** [▶ 16:51](https://youtu.be/k721w58jKLE?t=1011)：例如英文 $n=3$、$M=2$，codebook 可能是 $\{\text{AAA},\text{ABC}\}$。理由：我們分析的機率在 source 上；壓縮完的 0/1 統計特性不一定（只有最好的壓縮器，輸出才是 i.i.d. uniform；MPEG、JPEG 壓出來的 0、1 絕對不平均）。
- $c_m$ 叫 **reproduction／reconstruction word**（或 sourceword）：人要看的是 AAA，00100 解壓縮回來要重建成 AAA。
- 叫 **tuple** 不叫 vector：AAA 沒有向量的運算結構。（機率空間也叫 3-tuple／triple。）

**Observation 3.3**（p. 58）：$M$ 個 reproduction word 可以用 $k=\lceil\log_2M\rceil$ 個 bit 編號（binary index）。
- **Encoder** $f:\mathcal X^n\to\{0,1\}^k$：$n$ 個 source 變成 $k$ 個 bit；**decoder** $g$：把 $k$ 個 bit 轉回 source。都是固定長度到固定長度。
- 也可以用 D 進位（例如 4 個位階的裝置）。

---

## 5. 壓縮率與單位

[▶ 22:59](https://youtu.be/k721w58jKLE?t=1379)

**Rate**：
$$R=\frac kn=\frac1n\log_2M\quad\text{bits / source symbol}.$$
例：每 3 個 source 用 1 個 bit，rate $\frac13$。

- 以 2 為底：**bits**；以 $D$ 為底：$D$-ary code symbols（例如 $D=256$，或用 16 進位 0–F 設計，實際存成 1111、0000）。
- 以 $e$ 為底：**nats**。【口頭】理由是數學方便：$\ln x\le x-1$ 不用乘常數。早期很多書用 nats；這本書大多用 binary，和實際操作一致。

---

## 6. Typical set 的想法與例子

[▶ 25:02](https://youtu.be/k721w58jKLE?t=1502)

**Shannon 的想法**：$n=10$、英文 26 字母加空白共 27 個，有 $27^{10}$ 種 source。由大數法則（i.i.d.），存在一個集合：
- 裡面的機率約 $1-\delta$，外面約 $\delta$；
- **壓縮只要管裡面，外面不要理**。例如錯誤率要求 $10^{-5}$，就找一個外面機率小於 $10^{-5}$ 的集合。

這就是 **$\delta$-typical set**（Chernoff–Stein lemma 那裡已經用過）。【口頭】名字的意思：在外面看，最典型、最常出現的；看不到非典型的。

**大數法則的形式** [▶ 28:06](https://youtu.be/k721w58jKLE?t=1686)：令 $Y_i=-\log_2P_X(X_i)$——把機率本身當函數（丟骰子 2 點機率 1/3，「2」帶進去就得 1/3），再取 log。$X_i$ i.i.d. ⇒ $Y_i$ i.i.d.，$E[Y_i]=H(X)$。由大數法則，
$$\frac{Y_1+\cdots+Y_n}n=-\frac1n\log_2P_{X^n}(X^n)\to H(X).$$
【口頭】Shannon 從機率那邊抓了概念，再取一個新名字。

**例子**（課本 Table 3.1，p. 63）[▶ 30:07](https://youtu.be/k721w58jKLE?t=1807)：$n=2$、$\delta=0.4$，source $\{A,B,C,D\}$，機率 $0.4,0.3,0.2,0.1$。
$$H(X)=0.4\log\tfrac1{0.4}+0.3\log\tfrac1{0.3}+0.2\log\tfrac1{0.2}+0.1\log\tfrac1{0.1}\approx1.846\text{ bits}.$$
（計算 entropy 跟操作無關、跟怎麼壓縮無關，只看機率。）

檢查 AA：$\left|-\frac12(\log_20.4+\log_20.4)-H\right|=|1.322-1.846|\approx0.525>0.4$，所以 AA **不在** typical set。

16 個 sourceword 中：
- **在** $F_2(0.4)$ 的 7 個：AB(0.317)、AC(0.025)、BA(0.317)、BB(0.109)、BC(0.183)、CA(0.025)、CB(0.183)；
- 不在的 9 個：AA(0.525)、AD(0.475)、BD(0.683)、CC(0.475)、CD(0.975)、DA(0.475)、DB(0.683)、DC(0.975)、DD(1.475)。

裡面 7 個的總機率約 0.61，外面 9 個約 0.39。【口頭】$n=2$ 還談不上大數法則（通常要上萬、上十萬），但已經看得出來；$n$ 越大，外面的機率越少、裡面的個數比例越少。

**編碼** [▶ 33:09](https://youtu.be/k721w58jKLE?t=1989)：
- 裡面的 7 個各給一個 ID：001、010、…、111（3 bits）。
- 外面的全部 map 到預設的 000——解壓縮解不回來（ambiguous），只能亂猜，不理它。

---

## 7. AEP（Shannon–McMillan–Breiman）

[▶ 34:11](https://youtu.be/k721w58jKLE?t=2051)

**Theorem 3.4（Shannon–McMillan–Breiman；asymptotic equipartition property, AEP）**（p. 59）：$\{X_n\}$ 是 DMS，則
$$-\frac1n\log_2P_{X^n}(X_1,\dots,X_n)\to H(X)\quad\text{in probability},$$
即對任意 $\delta>0$，$\lim_{n\to\infty}\Pr\left[\left|-\frac1n\log_2P_{X^n}(X^n)-H(X)\right|>\delta\right]=0$。

- 證明：i.i.d. ⇒ $-\frac1n\log_2P_{X^n}(X^n)=\frac1n\sum_i[-\log_2P_X(X_i)]$，再用弱大數法則。
- 【口頭】19 世紀數學家就知道會收斂；in probability 就是 weak law（strong law 是 with probability 1）。
- 也叫 **entropy stability property**（課本 p. 59 註 4）。

**Weakly $\delta$-typical set**（p. 60）：
$$F_n(\delta):=\left\{x^n\in\mathcal X^n:\ \left|-\frac1n\log_2P_{X^n}(x^n)-H(X)\right|\le\delta\right\}.$$
$-\frac1n\log_2P_{X^n}(x^n)$ 叫 $x^n$ 的「apparent entropy」（經驗平均 self-information）；typical 就是它離真正的 entropy 不超過 $\delta$。

---

## 8. AEP 的推論：equipartition

[▶ 35:42](https://youtu.be/k721w58jKLE?t=2142)

**為什麼叫 equipartition**（【口頭】）：
- 世界的財富集中在 2% 的人身上，而且**這些人對我們來說都一樣有錢**（Bill Gates 可能覺得別人比他有錢，但我們看起來都一樣）。
- typical set 裡的機率約 1，每個元素的機率差不多（例如 8 個人各約 1/8）——**equal partition**。
- 操作意義：做無損壓縮時，**裡面的每一個都不能忽略，大家都一樣重要**。如果裡面還有 M 型分布（3 個人比另外 5 個人有錢 10 倍），你就會犧牲那 5 個；但事實上不能。

**Theorem 3.5（consequence of the AEP）**（p. 60）：DMS、任意 $\delta>0$，
1. 若 $x^n\in F_n(\delta)$：$2^{-n(H(X)+\delta)}\le P_{X^n}(x^n)\le2^{-n(H(X)-\delta)}$。
2. $P_{X^n}(F_n^c(\delta))<\delta$，for sufficiently large $n$。
3. $|F_n(\delta)|\le2^{n(H(X)+\delta)}$ 對**所有** $n$；$|F_n(\delta)|>(1-\delta)2^{n(H(X)-\delta)}$ for sufficiently large $n$。

所以：typical set 大約有 $2^{nH(X)}$ 個元素，每個機率約 $2^{-nH(X)}$。

**證明**：
- (1) 直接由定義：$|-\frac1n\log P-H|\le\delta$，乘 $-n$、取 2 的次方。【口頭】集合用機率本身定義，結果就出來了——「immediate consequence of the definition」。韓太舜的 preface：定義定對了，證明就簡單。這個觀念到 90 年代、2000 年後還在發酵。
- (2) AEP；或用 Chebyshev（課本 p. 60）：
$$P_{X^n}(F_n^c(\delta))\le\frac{\sigma_X^2}{n\delta^2}<\delta\quad\text{當 }n>\frac{\sigma_X^2}{\delta^3},\qquad\sigma_X^2=\mathrm{Var}[-\log_2P_X(X)].$$
- (3)【口頭】總共一塊錢、每人約 0.1 元，就知道約 10 個人。
$$1\ge\sum_{x^n\in F_n(\delta)}P_{X^n}(x^n)\ge|F_n(\delta)|\,2^{-n(H+\delta)}\ \Rightarrow\ |F_n(\delta)|\le2^{n(H+\delta)}\quad(\text{對所有 }n),$$
$$1-\delta<\sum_{x^n\in F_n(\delta)}P_{X^n}(x^n)\le|F_n(\delta)|\,2^{-n(H-\delta)}\quad(\text{要 }n\text{ 夠大，才有 }1-\delta<P(F_n)).$$

**$\delta$ 和 $n$ 的關係**（【口頭】）[▶ 39:48](https://youtu.be/k721w58jKLE?t=2388)：$\delta$ 是半徑，可以任意小，但 $n$ 要夠大。$\delta$ 從 0.1 變 0.01，$n$ 大概要大 10 倍。例：$H\approx1.8$、$\delta=0.0001$，上下界幾乎一樣。

---

## 9. Shannon source coding theorem

[▶ 45:56](https://youtu.be/k721w58jKLE?t=2756)

【口頭】Blahut 的書叫第一定律；但「第一」沒有資訊，後來叫 **Shannon source coding theorem**（資料壓縮定理）。

**Theorem 3.6**（pp. 62–63）：整數 $D>1$，DMS 的 entropy 為 $H_D(X)$。
- **Forward part（achievability）**：對任意 $0<\varepsilon<1$，存在 $0<\delta<\varepsilon$ 和一串 $D$-ary block code $\{\mathcal C_n=(n,M_n)\}$，使
$$\limsup_{n\to\infty}\frac1n\log_DM_n\le H_D(X)+\delta,$$
而且 $P_e(\mathcal C_n)<\varepsilon$ for all sufficiently large $n$。
- **Strong converse part**：對任意 $0<\varepsilon<1$，任何滿足
$$\limsup_{n\to\infty}\frac1n\log_DM_n<H_D(X)$$
的 block code 序列，都有 $P_e(\mathcal C_n)>1-\varepsilon$ for all sufficiently large $n$。

其中 $P_e(\mathcal C_n)=P_{X^n}\{x^n:g(f(x^n))\ne x^n\}$。

**意義**（【口頭】）：
- 條件只要 DMS（i.i.d.）——其實只要 source 滿足大數法則，下面全部成立；需要的就是「一個個數很少但機率很大的集合」。
- Forward：只要存在一個方法（全班最高 180 公分，找到一個 180 公分的人就好）。**$\delta<\varepsilon$ 的理由**：typical set 外面全錯，所以外面的機率 $\delta$ 一定要小於錯誤率要求 $\varepsilon$。
- 要「一串」碼，是因為 $n\to\infty$——這也是 Shannon 理論被詬病的地方。
- Shannon 沒辦法到達 entropy，但能無限接近（$H+\delta$，$\delta$ 任意小，例如 $1.8+0.0001$）。
- **Strong converse**：$H=1.8$，一本書 10 萬個字母需要約 18 萬 bit；若想只用 16 萬 bit（rate 1.6），**全世界所有方法**錯誤率都會趨近 1，對任意 $\varepsilon$ 都成立。Shannon 發現了一條天然的界線：entropy。
- Converse 也是 for sufficiently large $n$：$n$ 小的時候還是有機會做一些事。

【課本補充】p. 62 註 7：forward 等價於存在碼序列使 $\limsup P_e=0$；一般的 converse 只需證 $\limsup P_e>0$，strong converse 給出更強的 $\limsup P_e=1$。

---

## 10. Forward part 的證明

[▶ 53:34](https://youtu.be/k721w58jKLE?t=3214)

（只證 $D=2$。）給定 $0<\varepsilon<1$，取 $0<\delta<\varepsilon$，並取 $n>\frac2\delta$。

**編碼**：用半徑 $\frac\delta2$ 的 typical set
$$x^n\mapsto\begin{cases}x^n\text{ 的 binary index（不是全 0）},&x^n\in F_n(\delta/2)\\\text{全 0 codeword},&x^n\notin F_n(\delta/2).\end{cases}$$

**Rate**：
$$M_n=|F_n(\delta/2)|+1\le2^{n(H+\delta/2)}+1<2\cdot2^{n(H+\delta/2)}<2^{n(H+\delta)}.$$
（最後一步：$n>\frac2\delta$ ⇒ $\frac{n\delta}2>1$ ⇒ $2<2^{n\delta/2}$。）所以 $\frac1n\log_2M_n<H+\delta$。

**錯誤率**：只有 typical set 外面會錯，由 AEP，$P_e\le P_{X^n}(F_n^c(\delta/2))<\frac\delta2<\varepsilon$ for sufficiently large $n$。∎

【口頭】$n>\frac2\delta$ 告訴你：錯誤率要求小 10 倍，長度就要拉長 10 倍（這是 Shannon 證明給的充分條件）。後來有人研究最少要多長，大致上就是這個數量級。

---

## 11. Strong converse 的證明

[▶ 57:11](https://youtu.be/k721w58jKLE?t=3431)

Converse 要涵蓋**所有**壓縮方法，比較 tricky。

**關鍵觀察** [▶ 59:44](https://youtu.be/k721w58jKLE?t=3584)：
- 壓縮就是 mapping。一對一的部分解壓縮沒問題；**只有兩個以上 source 對到同一個 codeword 時才會錯**——block code 要壓縮，就一定有多對一（1024 種狀況用 8 個 bit）。
- 多對一時，解壓縮只能選其中一個；被選中的那個解得對，其他都錯。
- 所以：令 $S_n$ = 會被正確解壓縮的 sourceword 集合，則
$$|S_n|\le M_n.$$
（例：20 個 source 對到 18 個 codeword，最多 18 個解得對。）這對所有方法都成立。

**證明**：rate 嚴格小於 $H$，取 $\delta>0$ 使 $\limsup\frac1n\log_2M_n<H-2\delta$；則 sufficiently large $n$ 時 $|S_n|\le M_n<2^{n(H-2\delta)}$。

正確率拆成和 typical set $F_n(\delta)$ 的「交集外面」和「交集裡面」：
$$\begin{aligned}
1-P_e&=P_{X^n}(S_n)=P_{X^n}(S_n\cap F_n^c(\delta))+P_{X^n}(S_n\cap F_n(\delta))\\
&\le P_{X^n}(F_n^c(\delta))+|S_n|\cdot\max_{x^n\in F_n(\delta)}P_{X^n}(x^n)\\
&<\delta+2^{n(H-2\delta)}\cdot2^{-n(H-\delta)}=\delta+2^{-n\delta}.
\end{aligned}$$
- 外面：整個 typical set 外面的機率 $<\delta$。
- 裡面：每個元素機率 $\le2^{-n(H-\delta)}$（equipartition），個數 $\le|S_n|$。【口頭】每個人約 0.1 元，交集抓到 8 個人就抓到 0.8。故意選 $2\delta$，就是為了和 $\delta$ 消掉剩 $2^{-n\delta}$。
- 取 $\delta\le\frac\varepsilon2$，$n$ 夠大時 $2^{-n\delta}<\frac\varepsilon2$，所以 $1-P_e<\varepsilon$，即 $P_e>1-\varepsilon$。∎

【口頭】回想整個證明的概念：typical set 太重要了。任何壓縮方法和它的交集都不可以太少——裡面每一個都要好好對待，否則抓不到壓縮的重點，錯誤率就會趨近 1。

---

## 12. 討論：rate = entropy、uniform 不能壓、weak converse

[▶ 67:56](https://youtu.be/k721w58jKLE?t=4076)

**Ultimate data compression rate**：用 limsup 是因為 Shannon 看的是 $n$ 很大的情形。
- rate > $H$：存在方法，錯誤率任意接近 0（typical set）。
- rate < $H$：任何方法錯誤率趨近 1（strong converse，也用 typical set 證）。
- rate **剛好 =** $H$：Shannon 的定理沒說。【口頭】有人證明：從上往下逼近 entropy，錯誤率可以趨近 0；從下往上就不行。

【課本補充】Fig. 3.3（p. 65 的 Observation 3.7）把這個畫成錯誤率 vs rate 的階梯圖。

**什麼時候不能壓縮** [▶ 70:00](https://youtu.be/k721w58jKLE?t=4200)：binary i.i.d. uniform，$H=1$。typical set 個數 $2^{nH}=2^n$——就是整個集合（$n=10$ 時 1024 個，每個機率 $2^{-10}$），大家都一樣重要，不能壓縮。entropy 小於 1（例如 0.2）時集合才變小。

**Weak vs strong converse** [▶ 72:32](https://youtu.be/k721w58jKLE?t=4352)：
- Weak converse：只證錯誤率**不能任意小**，有一個正的下限（例如 0.2）。
- 沒有大數法則的 source（例如 non-stationary、non-ergodic），就可能只有 weak converse，壓縮極限也不同。

**Stationary 但非 ergodic** [▶ 73:32](https://youtu.be/k721w58jKLE?t=4412)（【口頭】）：
- 一般 stationary 序列的 $\frac1n\sum Y_i$ 收斂到隨機變數，不是期望值。
- 但這裡帶的函數很特別——它自己的機率取 log。只要 stationary（不需要 ergodic），$-\frac1n\log P_{X^n}(X^n)$ 的**期望值** $\frac1nH(X^n)$ 會收斂到一個常數，叫 **entropy rate**；它就是壓縮極限，同樣的證明可以推過去。
- 連 stationary 都沒有：收斂到一個分布，壓縮極限是 sup-entropy rate（第二部分）。

> 老師在這段說「只要 stationary，它還是會收斂到一個常數」；課本對 stationary ergodic 才給 AEP（Theorem 3.14）。stationary（不 ergodic）時一定存在的是 entropy rate 這個極限（Theorem 3.11），AEP 不一定成立。

---

## 13. Stationary source 與 entropy rate

[▶ 76:08](https://youtu.be/k721w58jKLE?t=4568)

**Definition 3.8（entropy rate）**（pp. 66–67）：
$$H(\mathbf X):=\lim_{n\to\infty}\frac1nH(X^n)$$
（若極限存在）。不獨立，所以 $H(X^n)$ 不能拆成單一字母（沒有 single-letter representation），$n$ 大時幾乎算不出來。【口頭】以前請學生寫程式算，算到 $n=20$ 就算不下去了。對 stationary source 它一定存在。

**Lempel–Ziv 的連結**（【口頭】）：1977、1978 年的 Lempel–Ziv 壓縮，對所有 stationary source 都能漸近壓到 entropy rate。它證明的重點：**stationary source 可以用 Markov source 逼近**——$k$ 階 Markov 近似 $P(x_n|x_{n-1},\dots,x_{n-k})$，$k\to\infty$ 時就是原來的分布。（例：$P(x_1,x_2,x_3)=P(x_1)P(x_2|x_1)P(x_3|x_1,x_2)$，一階近似把最後一項換成 $P(x_3|x_2)$。）Lampel–Ziv 用過去預測未來。證明在 Cover 的書，本課不教。

**Lemma 3.9**（p. 67）：stationary source 的 $H(X_n|X_{n-1},\dots,X_1)$ 對 $n$ 非遞增，而且有下界 0，所以極限存在。
$$H(X_n|X_{n-1},\dots,X_1)\le H(X_n|X_{n-1},\dots,X_2)=H(X_{n-1}|X_{n-2},\dots,X_1).$$
- 第一步：少一個條件，不確定性只會增加（conditioning 不增加 entropy 的反向）。
- 第二步：stationary，window 往前挪一格分布不變。
- 再用 monotone convergence theorem。

**Lemma 3.10（Cesàro mean）**（p. 67）：$a_n\to a$ ⇒ $b_n=\frac1n\sum_{i=1}^na_i\to a$。

**Theorem 3.11**（p. 68）：stationary source 的 entropy rate 一定存在，而且
$$H(\mathbf X)=\lim_{n\to\infty}H(X_n|X_{n-1},\dots,X_1).$$
證明：chain rule $\frac1nH(X^n)=\frac1n\sum_{i=1}^nH(X_i|X^{i-1})$，右邊每項收斂（Lemma 3.9），再用 Cesàro mean。

**定義 vs 結果**（【口頭】）：為什麼不直接用 $\lim H(X_n|X^{n-1})$ 當定義？因為 $\frac1nH(X^n)$ 才符合 Shannon 原本的想法——給你 8 個事件，算總資訊量再除以 8，才是平均資訊量。只是剛好和「用過去預測下一個」相等（Markov 逼近 stationary）。

**例子** [▶ 84:24](https://youtu.be/k721w58jKLE?t=5064)：
- **i.i.d.**：$H(X^n)=nH(X)$ ⇒ entropy rate $=H(X)$。backward compatible：Shannon 1948 證的就是 i.i.d. 的情形。
- **一階 stationary Markov**：$H(X_n|X^{n-1})=H(X_n|X_{n-1})=H(X_2|X_1)$ ⇒ entropy rate $=H(X_2|X_1)\le H(X_2)$。
  - 【口頭】為什麼 Markov 的壓縮率比 $H(X_2)$ 小？因為和過去有關：這個畫面到下一個畫面很相關，不用再壓有關聯的部分，只要壓「給定前一個畫面後額外增加的訊息」。

---

## 14. Stationary ergodic、Markov source

[▶ 87:32](https://youtu.be/k721w58jKLE?t=5252)

【課本補充】**Theorem 3.14（一般化 AEP）**（p. 70）：stationary ergodic source 滿足 $-\frac1n\log_2P_{X^n}(X^n)\to H(\mathbf X)$（almost surely）。**Theorem 3.15**：stationary ergodic source 的 source coding theorem，把 $H(X)$ 換成 entropy rate，forward 和 strong converse 都成立。

【口頭】
- i.i.d. 是 stationary ergodic 的特例。ergodic 在數學上非常難驗證；目前能驗證的是 Markov。
- Ergodic decomposition（第 7 集）：stationary source 是 stationary ergodic 的混合，所以平均不收斂到期望值。
- **有限狀態、irreducible、stationary 的 Markov source 一定是 ergodic**（回到最早數學上的 ergodic 定義）。irreducible：轉移機率讓每個 state 都不會消失（例如 8 個 state 經過多步後都還有機率出現）。

---

## 15. 好的壓縮器、redundancy

[▶ 90:34](https://youtu.be/k721w58jKLE?t=5434)

**最好的壓縮器輸出 asymptotically i.i.d. uniform**：最好的壓縮結果不能再被壓縮 ⇒ typical set 充滿整個空間 ⇒ 輸出約 i.i.d. uniform。所以看到 0、1 個數差很多，那個壓縮器**一定不是最好的**（即 the output of a perfect data compressor is i.i.d.，if and only if）。

**Redundancy** 分兩部分 [▶ 91:35](https://youtu.be/k721w58jKLE?t=5495)：
1. **Intra-sourceword**（字母本身不均勻）：0、1 機率不是 1/2，只看 marginal 就能壓。可以壓掉的量 $\log_2|\mathcal X|-H(X)$。
2. **Inter-sourceword**（前後相關，memory）：例如影像壓縮考慮前後 frame。可以額外壓掉 $H(X)-H(\mathbf X)$（一階 Markov 就是 $H(X_2)-H(X_2|X_1)$）。
- **Total redundancy** $=\log_2|\mathcal X|-H(\mathbf X)$。
- 【口頭】壓得好的影片，每個畫面的 0、1 看起來亂、uniform，前後也沒有關係。

**例子**：
- i.i.d. uniform：完全不能壓。
- i.i.d. 但 non-uniform：只要壓 marginal。
- 對稱的 Markov（marginal 已是 uniform）：只能壓 memory。
- 不對稱的 Markov：兩種都要壓才最好。

---

## 16. 一頁速查表

**設定**：DMS（i.i.d.、有限字母）；$(n,M)$ block code，rate $\frac1n\log_2M$；$P_e=\Pr\{g(f(X^n))\ne X^n\}$。Block code 是漸近無損；變長碼完全無損。

**AEP（Thm 3.4）**：$-\frac1n\log_2P_{X^n}(X^n)\to H(X)$ in prob.（$=\frac1n\sum-\log P_X(X_i)$ + WLLN）。

**Typical set** $F_n(\delta)=\{|-\frac1n\log_2P_{X^n}(x^n)-H|\le\delta\}$（Thm 3.5）
1. $2^{-n(H+\delta)}\le P(x^n)\le2^{-n(H-\delta)}$（equipartition）；
2. $P(F_n^c)<\delta$（Chebyshev：$n>\sigma^2/\delta^3$）；
3. $(1-\delta)2^{n(H-\delta)}<|F_n|\le2^{n(H+\delta)}$。
- 例：$(0.4,0.3,0.2,0.1)$，$H\approx1.846$，$n=2,\delta=0.4$：7 個在內（機率 0.61），9 個在外。

**Source coding theorem（Thm 3.6）**
- Forward：typical set 編號、其餘 → 全 0；$M_n\le2^{n(H+\delta/2)}+1<2^{n(H+\delta)}$（$n>2/\delta$），$P_e<\delta/2<\varepsilon$。
- Strong converse：$|S_n|\le M_n<2^{n(H-2\delta)}$；$1-P_e\le P(F_n^c)+|S_n|2^{-n(H-\delta)}<\delta+2^{-n\delta}$ ⇒ $P_e\to1$。
- Rate = $H$：要從上方逼近。

**Entropy rate**
- $H(\mathbf X)=\lim\frac1nH(X^n)=\lim H(X_n|X^{n-1})$（stationary：條件 entropy 遞減 + Cesàro mean）。
- i.i.d.：$H(X)$；一階 Markov：$H(X_2|X_1)$。
- Stationary ergodic：AEP 和 source coding theorem 都用 entropy rate 成立。有限、irreducible、stationary Markov ⇒ ergodic。

**Redundancy**：intra $=\log|\mathcal X|-H(X)$；inter $=H(X)-H(\mathbf X)$；total $=\log|\mathcal X|-H(\mathbf X)$。最好的壓縮器輸出 ≈ i.i.d. uniform。

---

## 17. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 變長碼、完全無損、Kraft 不等式 | 第 13 集（§3.3.1–3.3.2） |
| Huffman、Shannon–Fano–Elias 等前綴碼 | 第 14 集（§3.3.3） |
| Lempel–Ziv（universal 壓縮） | 第 15 集（§3.3.4） |
| Typical set 證明手法 | 第 16–18 集（channel coding theorem，jointly typical） |
| Source entropy vs capacity（joint source-channel） | 第 21 集（§4.6） |
| Sup-entropy rate、information spectrum | 第 33 集（第二部分 Chapter 2） |

---

## 附：本集一句話總結

> **大數法則讓 $-\frac1n\log P(X^n)$ 收斂到 entropy：機率幾乎全部集中在約 $2^{nH}$ 個「一樣重要」的 typical sequence 上——只編號它們，rate 就能壓到 $H+\delta$、錯誤率任意小；壓到 $H$ 以下，任何方法都抓不住 typical set，錯誤率趨近 1。**

---

*筆記依據陳伯寧老師「消息理論」Lec12 錄影逐字稿（whisper large-v3-turbo，1:34:33）與 Alajaji & Chen 課本 §3.1–3.2 整理。*
