---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 21
lecture: Lec21 4.6 Lossless joint source-channel coding and Shannon's separation principle
date: 待補
video: https://youtu.be/AQ2uBytKBeo
notes: Alajaji & Chen §4.6（pp. 141–149，Definition 4.29–Theorem 4.32、Fig. 4.8–4.9、joint vs separate 的討論）
---

# 第 21 集 · Lec21 §4.6：lossless joint source-channel coding 與 separation principle [▶ 影片](https://youtu.be/AQ2uBytKBeo)

← 上一集：[20](20-polar-codes-bec.md) ｜ [總目錄](README.md) ｜ 下一集：[22](22-differential-entropy-1.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 21 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（43:15，whisper large-v3-turbo）＋ 課本 §4.6（pp. 141–149）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Shannon」聽成「Shanen」，「rate-distortion theorem」聽成「ray distortion theorem／Rate Detortion Theorem」，「tandem」正確，「stationary ergodic」聽成「station ergatic」，「weak converse」聽成「week convert」，「Fano」聽成「phenols／Phenon／Phanel」，「Lempel–Ziv」聽成「Lample Zip」，「Venn diagram」聽成「Vin Diagram」，「公設」聽成「公社」，「typical set」聽成「Typical Say」，「Rayleigh fading」正確，「and fading」聽成「an fading」。開頭「講解,我們有個電子貼金,諸位商品」和開頭重複的幾句、結尾「優優獨播劇場」是 whisper 幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Shannon 的四個定律](#1-shannon-的四個定律)
- [2. 分開設計 vs 整合設計](#2-分開設計-vs-整合設計)
- [3. 核心結論：entropy rate vs capacity](#3-核心結論entropy-rate-vs-capacity)
- [4. 承接第 6 章：為什麼需要 rate-distortion](#4-承接第-6-章為什麼需要-rate-distortion)
- [5. 為什麼叫 separation principle](#5-為什麼叫-separation-principle)
- [6. Source-channel block code](#6-source-channel-block-code)
- [7. Theorem 4.30（rate-one）](#7-theorem-430rate-one)
- [8. Forward part：切一半](#8-forward-part切一半)
- [9. Converse part：Fano + DPI](#9-converse-partfano--dpi)
- [10. 一般 rate（m-to-n）與火星照片的例子](#10-一般-ratem-to-n與火星照片的例子)
- [11. 分開設計的代價：整合設計的好處](#11-分開設計的代價整合設計的好處)
- [12. 第 4 章總結](#12-第-4-章總結)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

把第一定律（壓縮）和第二定律（傳輸）**整合**：一個 source 能不能可靠地送過一個通道？答案只看兩個**分開計算**的量——source 的 entropy rate 和通道的 capacity——這就是 **separation principle**。最後討論整合設計在有限長度下的好處，並總結第 4 章。

| 主題 | 課本 |
|---|---|
| Separation principle 的意義、Fig. 4.8–4.9 | §4.6 開頭（pp. 141–142） |
| Source-channel block code | Definition 4.29（p. 143） |
| Rate-one 定理與證明 | Theorem 4.30（pp. 143–146） |
| 備註、一般 rate | Observation 4.31、Theorem 4.32（pp. 147–148） |
| Joint vs separate 的討論 | pp. 148–149 |

---

## 1. Shannon 的四個定律

[▶ 00:00](https://youtu.be/AQ2uBytKBeo?t=0)

Shannon 三大定律加一個整合定律，共四個：
1. **Source coding theorem**（70 年代叫第一定律）：無錯誤的壓縮極限是 entropy。
2. **Channel coding theorem**：capacity（Shannon 第一個提出的概念）。
3. **Rate-distortion theorem**（第三定律）：第 6 章再講，因為要先介紹 continuous channel（第 5 章）。
4. **Information transmission theorem**，又叫 **joint source-channel coding theorem**：不在三大定律裡，是**第一和第二定律的整合**。

---

## 2. 分開設計 vs 整合設計

[▶ 01:32](https://youtu.be/AQ2uBytKBeo?t=92)

**實際系統**（Fig. 4.8，p. 142）：先 source encoder 壓縮（遵守 source coding theorem，最少壓到 entropy；例如用 Lempel–Ziv），再 channel encoder；經過通道後先 channel decoding，再 source decoding。
- 最好的壓縮器輸出是 uniform——這就是設計 channel code 時假設輸入 uniform 的原因。
- source coding 和 channel coding 是**獨立的方塊**、分開做，叫 **separate design**；串在一起叫 **tandem system**。

**整合設計**（Fig. 4.9）：最近二、三十年有 **joint source-channel coding**——把壓縮和傳輸合在一起設計。
- 【口頭】source coding 把東西拿掉、channel coding 又把東西加回來，剛好相反——乾脆一起做：不該拿掉的就不要拿掉，搞不好這些 redundancy 可以幫忙對抗雜訊。
- 問題：整合設計能不能**增加** reliable transmission rate？

---

## 3. 核心結論：entropy rate vs capacity

[▶ 03:36](https://youtu.be/AQ2uBytKBeo?t=216)

有一個 source $V_1,V_2,\dots$ 要經過通道 $X\to Y$ 送過去，再解回來。中間是黑盒子，可以分開設計，也可以整合設計。回到最根本的問題：**這個 information 送不送得過去？**

- **$H(\mathbf V)<C$**：一定送得過去，**分開設計就可以**。
- **$H(\mathbf V)>C$**：一定送不過去，**整合設計也沒有用**——整合設計不會增加系統的傳輸能力。

【口頭】你可以先壓縮再加 redundancy，不管怎麼做，information 量（entropy rate）是根本，它絕對不能超過傳輸的 capacity；一超過就送不過去，錯誤率非常糟。

---

## 4. 承接第 6 章：為什麼需要 rate-distortion

[▶ 05:09](https://youtu.be/AQ2uBytKBeo?t=309)

【口頭】有些情形 source 的 entropy rate 就是大於 capacity：
- 例：在火星照一張照片要傳回地球，capacity 非常小，照片的量非常大。Shannon 告訴你送不回來。
- 那就**不把原始資料完全送回來**：加 **distortion**，丟掉一些。例：entropy rate 每秒 20 bit，capacity 只能每秒 5 bit，就丟掉 15 bit——自己決定哪些重要、哪些不重要，用一個 **distortion function** 衡量，在 distortion 最小的前提下送回來。
- rate 降低、distortion 增加，是一個 trade-off。這個 trade-off 的函數能不能用數學（有 log 的量）直接算出來？這就是 **Shannon 第三定律（rate-distortion theorem）**。
- 這一節講的是**無失真（lossless）**的版本。

---

## 5. 為什麼叫 separation principle

[▶ 07:10](https://youtu.be/AQ2uBytKBeo?t=430)

又叫 **separation theorem／separation principle**：
- **能不能送得過去的條件是分開的**：entropy rate 只和 source 有關（照片含多少 information，跟在哪裡送無關），capacity 只和 $P_{Y|X}$ 有關（管道能載多少，跟要送什麼 source 無關）。兩個完全獨立、可以分開計算的統計量，比大小就知道送不送得過去。
- 【口頭】有些問題的條件很複雜，要把所有參數帶進一個函數；這裡的充要條件完全切開：source 歸 source、channel 歸 channel。

【課本補充】課本（pp. 141–142）說「separation」有兩層意思：
1. **Functional separation**：充要條件只用「source 的最小壓縮率」和「channel 的 capacity」兩個分開的量，沒有同時依賴兩者的量。
2. **Operational separation**：forward 的證明就是把 source coding 和 channel coding 串起來——source code 只看 source 統計、channel code 只看 channel 統計——分開（tandem）的方案和一般的整合方案一樣好（就漸近的可靠傳輸而言）。
- 除了「最小壓縮率剛好等於 capacity」這個未解的情形，要嘛分開設計就做得到，要嘛根本做不到。
- 這個定理也叫 lossless information transmission theorem（p. 141 註 16）。

**條件**：forward part 假設 source **stationary ergodic**；converse part 只假設 source **stationary**。證的是 **weak converse**（用 Fano 不等式）；i.i.d. 通道時其實錯誤率會趨近 1。【口頭】例：capacity 每秒 5 bit、information 每秒 10 bit，錯誤率至少 $1-\frac12$，沒有任何方法做得更好。後續還有很多研究把 separation 推廣（source 和 channel 不限於 DMC 等），例如 1999 年還有人在做。

---

## 6. Source-channel block code

[▶ 11:13](https://youtu.be/AQ2uBytKBeo?t=673)

**Definition 4.29（source-channel block code）**（p. 143）：一個 $m$-to-$n$ 碼 $\mathcal C_{m,n}$：
- encoder 把 source 的 $m$-tuple $V^m$ 直接對應到 channel input $X^n$；
- decoder 把 $Y^n$ 對應回 $\hat V^m$；
- 錯誤率 $P_e=\Pr[\hat V^m\ne V^m]$。

【口頭】中間是黑盒子——裡面要分開做 mapping 是你的事。例：每看 3 個 source 送一次，對應到通道的 10 次使用。
- 比例 $\frac mn$（老師說叫 transmission efficiency，或 bandwidth expansion factor 的倒數）：每次 channel use 平均帶幾個 source symbol，越高越好。
- 現在大部分實作系統還是分開的；真正用整合設計的還不多。

---

## 7. Theorem 4.30（rate-one）

[▶ 12:50](https://youtu.be/AQ2uBytKBeo?t=770)

先看 $m=n$（每個 channel use 帶一個 source symbol）。

**Theorem 4.30**（p. 143）：離散 source $\{V_i\}$，有限字母 $\mathcal V$，entropy rate $H(\mathbf V)$；DMC 的 capacity $C$（兩者用同樣的 log 底）。
- **Forward**：source stationary ergodic、$H(\mathbf V)<C$ ⇒ 對任意 $0<\varepsilon<1$，存在 rate-one 碼序列 $\{\mathcal C_{m,m}\}$，$P_e(\mathcal C_{m,m})<\varepsilon$ for sufficiently large $m$。
- **Converse**：source stationary、$H(\mathbf V)>C$ ⇒ 任何 rate-one 碼序列都有
$$P_e(\mathcal C_{m,m})>(1-\varepsilon)\mu\quad\text{for sufficiently large }m,\qquad\mu=H_D(\mathbf V)-C_D,$$
$D=|\mathcal V|$，$H_D$、$C_D$ 用 $D$ 進位單位。即錯誤率 bounded away from zero。

【口頭】
- 不管怎麼討論，都要有**大數法則**的行為——這是 information theory 能用到很多領域的原因：做資料分析，收斂的行為非常重要。通道 DMC 有 typical set；source 雖不是 i.i.d.，帶進那個函數後一樣會收斂（有個數少、機率大的集合，取 log 平均趨近常數）。
- entropy rate 和 capacity 都是機率的量，跟設計、操作無關；比較時單位要一樣（都用 bit）。
- 怎麼證 forward 應該可以舉一反三：typical set 做 decoding、random coding、證明期望錯誤率趨近 0。怎麼設計不知道——那是 50 年後的事。
- **下界的意義**：以 bit 為單位，$\mu=\frac{H(\mathbf V)-C}{\log_2D}$。若 source 非常豐富（entropy rate 就是 $\log_2D$），$\mu=1-\frac C{\log_2D}$，就和之前的 $1-\frac CR$ 一樣：錯誤率的下限就是兩者的差。實際上是 strong converse（錯誤率趨近 1），這裡用簡單的方法證成 weak converse。

---

## 8. Forward part：切一半

[▶ 16:59](https://youtu.be/AQ2uBytKBeo?t=1019)

**不用重新證**：直接**分開設計**，用第一定律（source coding）和第二定律（channel coding）就夠了——兩者都已證明存在。

令 $\gamma:=C-H(\mathbf V)>0$，**各給一半**（課本 pp. 144–145）：
1. **Source coding**（Theorem 3.15）：存在壓縮碼把 $V^m$ 壓到 rate $<H(\mathbf V)+\frac\gamma2$，錯誤率 $<\frac\varepsilon2$。（壓到 entropy rate 加一點點。）
2. **Channel coding**（Theorem 4.11，用 **maximal** error probability 的版本）：rate $H(\mathbf V)+\frac\gamma2=C-\frac\gamma2<C$，存在 channel code 的**最大**條件錯誤率 $\lambda<\frac\varepsilon2$。
   - 【口頭】source 出來的 $M$ 個可能，要放進 channel code 的 $\bar M\ge M$ 個 codeword（例如 1 到 10 放進可容納 12 個的碼，11、12 不用）——碼的容量稍大，但只用其中一部分。
   - 【口頭】為什麼用 maximal error：source encoder 的輸出不一定 uniform，用平均錯誤率不夠；第 16 集講過 Shannon 的證明對最大錯誤率也成立（丟掉最差一半）。四個 codeword 的平均錯誤率是各乘 $\frac14$ 加起來；maximal 是四個裡最大的。
3. **串接**：encoder $=f_c\circ f_s$、decoder $=g_s\circ g_c$。

**錯誤率**：錯誤只會發生在 (a) source 壓縮本身就錯，或 (b) channel 把 source encoder 的輸出 $w$ 傳錯：
$$P_e\le\Pr[\text{source coding 錯}]+\sum_w\Pr[f_s(V^m)=w]\,\lambda_w<\frac\varepsilon2+\frac\varepsilon2=\varepsilon.$$
（第二項：每個 $\lambda_w\le\lambda<\frac\varepsilon2$，機率和最多 1。）

【口頭】例：$H=3$、$C=5$，就定 4——source 壓縮出來不超過 4，4 又比 5 小，channel coding 一定送得過去。

---

## 9. Converse part：Fano + DPI

[▶ 25:42](https://youtu.be/AQ2uBytKBeo?t=1542)

Converse 要證明**所有**設計（**包含整合設計**）都做不到，所以不能用切一半的方法——要用 Fano 不等式（跟怎麼設計無關，是一個純數學的不等式）。

（課本 pp. 145–146）任何 $m$-to-$m$ 碼：
$$\begin{aligned}
H(\mathbf V)&\le\frac1mH(V^m)\qquad(\text{stationary 時 }\tfrac1mH(V^m)\text{ 非遞增，極限比它小})\\
&=\frac1mH(V^m|\hat V^m)+\frac1mI(V^m;\hat V^m)\\
&\le\frac1m\left[1+P_e\log_2|\mathcal V|^m\right]+\frac1mI(V^m;\hat V^m)\qquad(\text{Fano，}h_b\le1)\\
&\le\frac1m+P_e\log_2|\mathcal V|+\frac1mI(X^m;Y^m)\qquad(\text{DPI：}V^m\to X^m\to Y^m\to\hat V^m)\\
&\le\frac1m+P_e\log_2|\mathcal V|+C.
\end{aligned}$$
- 第二行：mutual information 的定義（Venn 圖：$H(V)$ = 共有的 + 沒有共有的）。
- Fano：$H(V^m|\hat V^m)\le h_b(P_e)+P_e\log_2(|\mathcal V|^m-1)\le1+P_e\cdot m\log_2|\mathcal V|$。
- DPI：資料越處理、共識越少（傳話越傳資料越少）。移到 $X^m,Y^m$ 是為了用 $I(X^m;Y^m)\le mC$。
- 【口頭】這一頁完全沒有告訴你怎麼設計系統，對所有設計都對——這就是 Fano 不等式在消息理論裡那麼重要的原因（雖然它是沒發表、上課講義的內容）。

移項：
$$P_e\ge\frac{H(\mathbf V)-C}{\log_2|\mathcal V|}-\frac1{m\log_2|\mathcal V|}=H_D(\mathbf V)-C_D-\frac{\log_D2}m\ \ge(1-\varepsilon)\mu\quad(m\text{ 夠大}).$$
$\frac1m\to0$，$m$ 一大錯誤率不可能很好。∎

【口頭】這看起來是理論、有點枯燥，但它是很重要的里程碑。國外通訊研究所每年都開消息理論：學過這個概念的人和完全沒有的人，設計系統的出發點完全不一樣——知道傳輸真的有極限、必須抓到統計特性、有 typical set 的思維、知道為什麼有 log。

---

## 10. 一般 rate（m-to-n）與火星照片的例子

[▶ 31:22](https://youtu.be/AQ2uBytKBeo?t=1882)

**Theorem 4.32**（pp. 147–148）：$m$-to-$n_m$ 碼。
- **Forward**（source stationary ergodic）：若
$$\limsup_{m\to\infty}\frac m{n_m}<\frac C{H(\mathbf V)},$$
存在碼序列 $P_e<\varepsilon$。
- **Converse**（source stationary）：若 $\liminf\frac m{n_m}>\frac C{H(\mathbf V)}$，錯誤率 bounded away from zero。

等價地：$m\cdot H(\mathbf V)<n\cdot C$——要送的總 information 小於通道總能載的量。

**火星的例子**（【口頭】）[▶ 32:27](https://youtu.be/AQ2uBytKBeo?t=1947)：
- 每 1 萬個 source symbol 一組，每個帶 0.2 bit ⇒ 共 2000 bit。
- 火星回地球的 capacity 很糟（去量高斯雜訊的 variance 帶進公式就知道），每次 channel use 只能帶 0.1 bit。
- 要 $0.1\times n>2000$，所以 $n>20000$：用 2 萬次傳送還是送得回來——**用時間換**。例如一天送一張，十天送十張。
- 反過來：若照片需要 24 小時才送得回來，主管要你 20 小時送完，可以直接跟 NASA 的主管說：Shannon 已經證明這不可能，錯誤率幾乎是 1（實際上是 strong converse）。非常清楚的界線。

【課本補充】Observation 4.31（p. 147）：
- $H(\mathbf V)=C$ 時能不能可靠傳送，一般**不知道**（即使是 DMS）——因為 forward 用分開設計，source coding 的 rate 從**上方**逼近 entropy rate，channel coding 的 rate 從**下方**逼近 capacity。
- 定理直接適用 DMS（DMS 是 stationary ergodic）。
- Forward 的 stationary ergodic 可以放寬成 **information stable**；time-invariant irreducible Markov source（不一定 stationary）就是 information stable。

---

## 11. 分開設計的代價：整合設計的好處

[▶ 35:03](https://youtu.be/AQ2uBytKBeo?t=2103)

【口頭】
- 現在基本上是分開設計：有些老師專做資料壓縮、有些專做資料傳輸（老師屬於傳輸），各自設計、串在一起。**Separation principle 說這是可行的**——以 capacity 的角度，整合設計沒有好處；tandem design 沒有 risk。
- 整合設計比較難：需要同時懂壓縮和傳輸的研究者（或一群人），考量比較複雜。

**代價在有限長度** [▶ 36:35](https://youtu.be/AQ2uBytKBeo?t=2195)：
- rate 一樣（火星照片還是要一天），但**錯誤率趨近 0 的速度不同**：**整合設計趨近得比較快**（已經證明了）。
- 所以達到同樣的錯誤率（例如 $10^{-5}$），整合設計需要的長度比較短：火星例子在同樣比例下，分開設計要 2000 / 20000 的 buffer，整合設計可能只要 200 / 2000。
- ⇒ **delay 和 complexity 都比較低**，也比較省電——**green design**。無線通訊對電池消耗要求很高，所以有人在做整合設計。
- 已經證明：在 AWGN、Rayleigh fading 加上 output quantization 的通道下，有整合設計的方法比最好的分開設計好 **2 dB**。（好 3 dB 代表傳送能量是對方的一半就達到一樣的錯誤率；2 dB 約是一半多一點。）
- 但以 reliable transmission rate 的概念來說，沒有好處。

> ⚠️ 逐字稿缺字：[▶ 39:41](https://youtu.be/AQ2uBytKBeo?t=2381) 老師說投影片上「an fading」有錯字，應為「**and** fading」（Gaussian noise, fading and output quantization）。

【課本補充】課本（pp. 148–149）的整理：
- 分開設計的好處：可以分別研究壓縮和傳輸（無限 delay、複雜度下不犧牲最優性）；**模組化、彈性**——不同 source 送同一通道，只要改 source code；同一 source 送不同通道，只要改 channel code。
- Shannon 自己就說過：source 的 redundancy 若在接收端被利用，通常會有幫助。例如英文保留大部分 redundancy，即使相當比例的字母收錯，也能靠上下文重建。
- 有限長度／複雜度下，很多研究顯示整合設計更好。
- 即使在無限長度下，整合設計的 **error exponent** 可以到分開設計的兩倍——同樣效能、coding delay 減半（換算成二元 source 經過高斯雜訊、fading 和輸出量化的通道，省超過 2 dB 的功率）。
- **多用戶（multiterminal）系統一般不滿足 separation**（少數網路拓撲除外），整合設計更有利。

---

## 12. 第 4 章總結

[▶ 40:11](https://youtu.be/AQ2uBytKBeo?t=2411)

【口頭】
- **Reliable transmission**：錯誤率任意小，靠長度趨近無限大達到。
- 討論的是 DMC：雜訊彼此獨立 ⇒ 有大數法則的行為。雜訊 dependent 時，要有一條 clear cut 的 capacity，還是需要大數法則（例如 stationary 加上條件）。
- **Typical set** 是消息理論（通訊）引進的專有名詞，其實就是數學上的大數法則。
- Channel coding theorem 的證明步驟很複雜，抓兩個重點：**傳送端 random coding、接收端 typical set decoding**；**converse 用 Fano 不等式**（跟怎麼設計完全無關）。
- 有了公式 $C=\max_{P_X}I(X;Y)$ 之後，要對各種通道**導出真正的數字**：有的算不出來，例如 $Y=AX+Z$（$Z$ 是 AWGN、$A$ 是 Rayleigh fading），就算給參數也算不出每秒幾個 bit；完全對稱的就知道最佳輸入是 uniform；要正確詮釋 KKT 條件（什麼時候找到的解是真正最佳的）。
- Polar code（5G 一定要做的）、information transmission theorem。
- 三大定律的前兩個和整合定律都介紹完了。

---

## 13. 一頁速查表

**Separation principle（Thm 4.30、4.32）**
- $H(\mathbf V)<C$（rate-one）或 $\frac mn<\frac C{H(\mathbf V)}$ ⇒ 可靠傳送可達，而且**分開設計**就夠（source stationary ergodic）。
- $H(\mathbf V)>C$ ⇒ 任何設計（含整合）都 $P_e\ge(1-\varepsilon)\mu$，$\mu=H_D(\mathbf V)-C_D$（source stationary）。
- $H(\mathbf V)=C$：未知。
- Functional separation（條件只用兩個分開的量）＋ operational separation（tandem 就最優）。

**Forward**：$\gamma=C-H$，source code rate $<H+\frac\gamma2$、$P_e<\frac\varepsilon2$；channel code（maximal error）rate $C-\frac\gamma2$、$\lambda<\frac\varepsilon2$；總 $P_e<\varepsilon$。

**Converse**：
$$H(\mathbf V)\le\tfrac1mH(V^m)=\tfrac1mH(V^m|\hat V^m)+\tfrac1mI(V^m;\hat V^m)\le\tfrac1m+P_e\log_2|\mathcal V|+C.$$
（Fano + DPI $V^m\to X^m\to Y^m\to\hat V^m$ + $I(X^m;Y^m)\le mC$。）

**火星例子**：$mH=2000$ bit、$C=0.1$ ⇒ $n>20000$；用時間換 rate。

**整合設計**：rate 沒有好處；有限長度下錯誤率收斂更快 ⇒ delay、複雜度、耗電較低（2 dB 增益）；error exponent 可到兩倍；多用戶系統 separation 一般不成立。

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 連續 source、連續通道（differential entropy、Gaussian channel） | 第 22–26 集（第 5 章） |
| $H>C$ 時就要 lossy：rate-distortion | 第 27–29 集（第 6 章） |
| Lossy joint source-channel coding（$R(D)<C$） | 第 30 集（§6.5） |
| Shannon limit | 第 31 集（§6.6） |
| Information stable、一般化的 separation | 第 32–35 集（第二部分） |

---

## 附：本集一句話總結

> **一個 source 能不能可靠地送過一個通道，只要比兩個分開算的數字：source 的 entropy rate 和通道的 capacity——小於就能送（先壓縮再加保護碼的分開設計就夠），大於就怎麼設計都不行；整合設計不會提高可靠傳輸率，但在有限長度下收斂更快、更省電。**

---

*筆記依據陳伯寧老師「消息理論」Lec21 錄影逐字稿（whisper large-v3-turbo，43:15）與 Alajaji & Chen 課本 §4.6 整理。*
