---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 34
lecture: Lec34 第二部分 Chapter 3 Measure of randomness for stochastic processes
date: 待補
video: https://youtu.be/xKOHD7RHvqQ
notes: 第二部分（information spectrum）課本沒有，只依逐字稿
---

# 第 34 集 · Lec34 第二部分第 3 章：隨機過程的隨機性量度（resolvability）與不定長度壓縮 [▶ 影片](https://youtu.be/xKOHD7RHvqQ)

← 上一集：[33](33-general-data-compression-theorems.md) ｜ [總目錄](README.md) ｜ 下一集：[35](35-channel-coding-theorems-output-statistics.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 34 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:05:39，whisper large-v3-turbo）。第二部分**課本沒有**，數學式依老師口述重建
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：開頭「NHQ UK JANICE…governors」是亂碼。「三大公設」聽成「三個公社／三大公社」，「asymptotic equipartition」聽成「Asymthetic Equal Partition」，「complementary CDF」聽成「complementing CDF／Compromised CDF」，「variable-length」聽成「Value Length／Variolence」，「Kraft inequality」聽成「craft inequality」，「infinitely often」聽成「Infinite Orphan」，「resolvability」聽成「reservability／resorbability」，「Verdú、Han」聽成「Verdue、Hunt／漢」，「Knuth」聽成「Cnus／CANOOS」，「Shannon–Fano–Elias」聽成「Shannon Phenol Alias」，「Huffman」聽成「Hoffmann／Hoffman」，「codeword」聽成「Code War」，「complexity」聽成「compressive／compensity／Compressity」，「Te Sun Han」聽成「提升」，「大數法則」聽成「大樹法則」，「rand()」聽成「RND／RIND」，「C 語言」聽成「西語言」，「程式」偶爾聽成「城市」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：從三大公設到 spectrum](#1-複習從三大公設到-spectrum)
- [2. 兩個端點、infinitely often、generalized AEP](#2-兩個端點infinitely-oftengeneralized-aep)
- [3. 新觀點：寫程式產生隨機變數](#3-新觀點寫程式產生隨機變數)
- [4. 合成和拆解是同一件事](#4-合成和拆解是同一件事)
- [5. Resolution 與 M-type](#5-resolution-與-m-type)
- [6. 用 variational distance 逼近](#6-用-variational-distance-逼近)
- [7. Resolvability 與 mean-resolvability](#7-resolvability-與-mean-resolvability)
- [8. 結果：resolvability = sup-entropy rate](#8-結果resolvability--sup-entropy-rate)
- [9. 四個量與兩個等式](#9-四個量與兩個等式)
- [10. 例子：Bernoulli(Z) source](#10-例子bernoulliz-source)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集解決了**固定長度**壓縮（錯誤率 asymptotically zero）。這一集處理**不定長度**壓縮（錯誤率 exactly zero），但換一個全新的觀點：**寫程式產生一個隨機變數，最少要呼叫幾次 random bit？**
- 最差情形（worst case）的複雜度 = **resolvability** = **sup-entropy rate** $\bar H(\boldsymbol X)$ = 固定長度壓縮極限；
- 平均情形（average case）的複雜度 = **mean-resolvability** = entropy rate 的期望值 = 不定長度壓縮極限。

最後用 Bernoulli(Z) source 說明：固定長度**完全不能壓**（1 bit/bit），不定長度卻可以壓到 **0.72135** bit/bit。

---

## 1. 複習：從三大公設到 spectrum

[▶ 00:00](https://youtu.be/xKOHD7RHvqQ?t=0)

【口頭】Shannon 大約 23、24 歲開始想「什麼是訊息」，提出三個公設：
1. information 一定是機率的函數；
2. 獨立事件的 information 量相加；
3. 機率越小，訊息量越多。

由此證明 self-information 唯一的表示是 $\log\frac1{P(x)}$（底數 2 單位是 bit）。取期望值得到平均訊息量（entropy），而它和資料壓縮完全等效——因為當時看的 source 是 i.i.d.，有大數法則，所以有 typical set、AEP（集合很小、佔大部分機率、每個元素機率幾乎一樣）。Shannon 30 幾歲發表。

第二部分回到最原始的量：$\frac1n\log\frac1{P(X^n)}$（不再獨立，不能拆成乘積）的分布。畫 complementary CDF，錯誤率 $\varepsilon$ 對到的 x 就是壓縮率 $H_\varepsilon$——完全包含古典情形（古典時 CDF 是 step function：壓縮率低於 entropy 錯誤率就是 1，即 **strong converse**；高於 entropy 錯誤率趨近 0）。

**Bernoulli(Θ) 的例子**：$X_i\in\{0,1\}$，機率是 $\Theta$ 和 $1-\Theta$，$\Theta$（或 $\Theta_i$）uniform 在 $[0,1]$。【口頭】以後在其他領域碰到不穩定、裡面隱含一層機率（像 hidden Markov model）的資料，就要找**對的 sufficient statistic**——這裡就是三大公設定義出來的量。它收斂到分布 $h_b(\Theta)$，壓縮量是在正確率 $1-\varepsilon$ 處取反函數（CDF 畫的是正確率、complementary CDF 畫的是錯誤率，兩種畫法）。

---

## 2. 兩個端點、infinitely often、generalized AEP

[▶ 08:42](https://youtu.be/xKOHD7RHvqQ?t=522)

【口頭】為什麼有 weak 和 strong converse：大數法則下有一個集中值，超過那個值所有設計都很差（strong converse）。廣義時 complementary CDF 有**兩個端點**：
- 壓縮率小於左端：$n$ 大時所有方法錯誤率都接近 1，不用在這裡找好方法。（左端在大部分情況是 0……老師這裡的口述有點混亂，見下。）
- 壓縮率比右端大一點：一定存在工程方法讓錯誤率趨近 0。
- 中間：不同的現象。

> ⚠️ 待確認：[▶ 09:42](https://youtu.be/xKOHD7RHvqQ?t=582) 老師說「左邊 ……用 super bar X……比它小所有方法錯誤率接近 1」、「h underbar X……只要比它大一點點都存在方法讓錯誤率趨近 0」，和上一集「錯誤率趨近 0 的壓縮極限是右端 $\bar H$」的說法看起來把 $\underline H$、$\bar H$ 的位置講反了；依第 33 集的定理，錯誤率 $\to0$ 需要 rate $>\bar H$（右端），rate $<\underline H$（左端）錯誤率 $\to1$。

**Infinitely often**：統計量不一定對所有 $n$ 收斂，會散開——$n=1,3,5,7$ 收斂到一個值、$n=2,4,6,8$ 收斂到另一個值（白天、下午、晚上不同）。
- 超過右端：不管什麼時候，一定存在 universal 的方法讓錯誤率趨近 0。
- 在中間：一定要在**特定長度**（例如 $n=20,40,60$）做，不能在 25、26、27——**infinitely often**。【口頭】有些通訊管道確實發現某些特定長度特別適合，這提供了一個解釋。

**Generalized AEP**：古典 AEP 是「二值」的集合——外面機率都小於 $\delta$；裡面總和約 1、每個一樣高（例如裡面 10 人各 $\frac1{10}$、外面 100 人機率都很小）。沒有大數法則時，集合變成**有灰階**的：裡面有人機率大、有人小。所以叫 generalized AEP。
- 【口頭】這次某黨做的民調好像蠻符合大數法則，五家做出來都一樣——那很好，一般沒有這麼好的預期。

---

## 3. 新觀點：寫程式產生隨機變數

[▶ 13:16](https://youtu.be/xKOHD7RHvqQ?t=796)

【口頭】不定長度碼錯誤率是 0，直接做很難思考。先把壓縮擺一邊，看標題 **measure of randomness**：兩個隨機現象哪一個比較隨機？
- 過去：高斯比較隨機，因為同能量下 differential entropy 最大、最難壓縮。
- 這裡從另一個角度：**要合成它，要寫一個程式**。1993 年 **Han 和 Verdú** 提出 **resolvability**（resolve 一個問題：要做模擬，要寫程式產生這個分布）。他們證明 entropy 和 resolvability 有關。

**例：產生 $-1,0,+1$，機率 $\frac14,\frac12,\frac14$**。可以呼叫的工具：一個 fair random bit（C 語言的 `rand()` 給 0 到 1 的 uniform，簡化成給 0 或 1、各 $\frac12$）。呼叫 random bit 是程式裡最花時間的（和加減乘除不同等級），所以**程式複雜度 = 呼叫 random bit 的次數**。

```text
b ← random bit
if b = 正面: 輸出 0              （機率 1/2）
else:
    b ← random bit
    if b = 正面: 輸出 -1         （機率 1/4）
    else:        輸出 +1         （機率 1/4）
```

- 平均呼叫 **1.5** 次（$\frac12\cdot1+\frac12\cdot2$）；最差 **2** 次（不會跑不完）。
- 這個程式是 **optimal**：分布的 entropy $=\frac14\log_24+\frac12\log_22+\frac14\log_24=1.5$ bit，平均複雜度剛好等於 entropy。不可能寫出平均 1.4 次的程式。
- 【口頭】entropy 是數學量，和程式複雜度掛上等號：要產生這麼大的訊息量，至少要花 entropy 的時間。所以程式寫得好不好，就看有沒有達到 entropy 的呼叫次數。

**Definition（程式複雜度）**：給定分布，用**最有效率的 algorithm**（呼叫 random bit 次數最少）完全合成它，所需的呼叫次數。有兩種量度：**average case** 和 **worst case**。

【口頭】連續隨機變數（例如高斯）的 entropy 是無限大，要呼叫無限多次——沒辦法寫程式精確產生任何連續隨機變數，只能逼近。

---

## 4. 合成和拆解是同一件事

[▶ 20:03](https://youtu.be/xKOHD7RHvqQ?t=1203)

【口頭】
- **壓縮（compress）**：隨機變數給我，我把它拆解——把零件拆掉收起來，去掉 redundancy，收到最簡化。
- **產生（generate）**：給我目標分布，我寫程式產生 $X_1,X_2,\dots$——從箱子拿出零件合成，看起來像原來的樣子。
- 好比一個裝置，你會拆它就會裝它——這兩件事**完全等效**，壓縮極限也等效。
- **Worst case ↔ fixed-length** 壓縮；**average case ↔ variable-length** 壓縮。Average 比較好。
- i.i.d.（大數法則）時兩者相等：不定長度和固定長度壓縮極限一樣，程式的 average 和 worst case 也一樣。

---

## 5. Resolution 與 M-type

[▶ 22:35](https://youtu.be/xKOHD7RHvqQ?t=1355)

**M-type**：若分布的每個機率都能寫成 $\frac kM$（$k=0,1,\dots,M$），稱它是 M-type。

**Resolution（解析度）**：$\log M$（自然對數單位是 nat，以 2 為底單位是 bit）。
- 例：所有機率都是 $\frac{?}{64}$（$\frac3{64},\frac2{64},\frac7{64},\dots$）⇒ 用 6 個 bit 完全表示分布，resolution $\log_264=6$ bit。需要 128 為分母就是 7 bit。
- 【口頭】概念上 resolution 就是 **worst case complexity**：$2^{-L}$ 這種分母（例如 $\frac1{128},\frac6{128},\frac{21}{128}$）呼叫 7 次一定做得出來；$\frac14,\frac24,\frac34$ 呼叫 2 次一定可以。
- **M 無限大**：例如 0 的機率 $\frac1\pi$、1 的機率 $1-\frac1\pi$。$\pi$ 是無理數，$\frac1\pi$ 寫不成整數分之整數 ⇒ 寫程式**精確**產生它，在有限時間內做不完（會有機率一直跑下去）。機率都是有理數，就一定能寫出在有限時間完成的程式。

**3-type 的程式**（產生 1 的機率 $\frac23$、0 的機率 $\frac13$）：
```text
even ← false
loop:
    b ← random bit
    if b = 正面:
        if even = false: 輸出 1 並結束
        else:            輸出 0 並結束
    else:
        even ← not even      （反面就把旗標對調）
```
- 輸出 1：第一次就正面，或「偶數次反面再正面」：$\frac12+\frac18+\frac1{32}+\cdots=\frac{1/2}{1-1/4}=\frac23$。✓
- 【口頭】這證明 3-type 的程式寫得出來，但**不是最好的**：worst case 是無限大（一直丟反面雖然機率很小，但有機率跑不完）。理論上 worst case 應該是 $\log_23$ 的等級；2 的倍數比較好寫，3、5 的倍數比較難。老師自己想了一下還沒想出直觀的寫法。

> ⚠️ 逐字稿缺字：[▶ 28:46](https://youtu.be/xKOHD7RHvqQ?t=1726) 程式的細節（even 旗標的初值、正面時輸出 0 或 1 的對應）逐字稿不完整；上面依「機率加起來是 $\frac23$」的口述重建。

---

## 6. 用 variational distance 逼近

[▶ 25:40](https://youtu.be/xKOHD7RHvqQ?t=1540)

$\frac1\pi$ 寫不出來，就**逼近**：寫一個產生 $\left(\frac13,\frac23\right)$ 的程式，resolution $\log_23\approx1.58$ bit，一定能在有限時間完成。
- 這是**平均**量：要產生 1000 個，大約 $1000\log_23$ 次呼叫內要完成。
- 兩個分布的距離用 **variational distance**（個別機率相減取絕對值再加總，很嚴格，每一個都要檢查）：
$$\left|\tfrac13-\tfrac1\pi\right|+\left|\tfrac23-\left(1-\tfrac1\pi\right)\right|\approx0.03.$$
- 0.03 可以接受就用它；不夠就把 $M$ 拉大，解析度更高，但執行更久。

**Definition（$\varepsilon$-achievable resolution）**：存在 computer-resolvable（機率都是有理數）的 $\tilde X$，$\|X-\tilde X\|\le\varepsilon$，resolution $\le R+\gamma$（$\gamma$ 任意小）。$\varepsilon$ 越小程式越難寫。

**Definition（$\varepsilon$-achievable resolution rate）**：一般要產生一序列（模擬做 1 萬次、2 萬次）。$P_{\tilde X^n}$ 是 M-type，resolution rate 是平均 $\frac1n\log M$，要求 $\|X^n-\tilde X^n\|\le\varepsilon$（依口述）。

---

## 7. Resolvability 與 mean-resolvability

[▶ 33:59](https://youtu.be/xKOHD7RHvqQ?t=2039)

**$\varepsilon$-resolvability**：每個人都去寫程式，都滿足距離 $\le\varepsilon$，找**最有效率**的（你的要跑三天、我的跑兩天，我的比較好）——最小的 achievable resolution rate。這是 **worst case**。
**Resolvability** $S(\boldsymbol X)$：再讓 $\varepsilon\to0$（$n\to\infty$ 時）。【口頭】這裡 $\varepsilon$ 已經不是錯誤率，是兩個分布的差距。

**Mean-resolvability** $\bar S(\boldsymbol X)$：把 resolution（worst case）換成 **entropy**（average case）：要求 $\frac1nH(\tilde X^n)\le R+\gamma$，其他一樣。
- 【口頭】Han–Verdú 取名 **mean**（平均），應該是事先就意會到它和 entropy 有關：entropy 就是 self-information 的平均。
- 【口頭】$\varepsilon$ 不能是 0，只能趨近 0：在有限生命要看到結果，就不可能完全精確，但可以 asymptotically。

---

## 8. 結果：resolvability = sup-entropy rate

[▶ 39:36](https://youtu.be/xKOHD7RHvqQ?t=2376)

**歷史**【口頭】：1976 年 **Knuth**（寫了好幾本很有名的書，老師大二大三的演算法、資料結構就用他的書）就探討過：最好的程式平均呼叫次數
$$H(X)\le E[\text{呼叫次數}]\le H(X)+2.$$
沒辦法證明等於 entropy，但最多多 2 個 bit。1993 年 Han–Verdú 證明 worst case complexity 是 resolution。

**Lemma（by definition）**：$P_{\tilde X^n}$ 是 M-type ⇒ 每個非零機率 $\ge\frac1M$ ⇒
$$\frac1n\log\frac1{P_{\tilde X^n}(x^n)}\le\frac1n\log M\quad(\text{resolution rate}).$$
【口頭】這就是定義換個方式陳述（Te Sun Han 常說：定義對了，結果就對了）。解析度 $\frac1{128}$，怎麼可能需要超過 7 個 bit？

**Theorem（Han–Verdú）**：
$$S(\boldsymbol X)=\bar H(\boldsymbol X)\quad(\text{sup-entropy rate，分布散開後的最右端}).$$
- 證明：$\ge$ 和 $\le$ 兩邊（二一律），完全用定義，沒有 typical set。
- **把 variational distance 和 log 接起來**：variational distance 沒有 log，但 entropy 和通訊的 rate（$\log$ SNR）都和 log 有關（三大公設：獨立事件相乘、information 相加 ⇒ log）。所以需要一個不等式把 log 引進來；也有人改用 **divergence**（本身有 log）來定義距離，結果一樣（因為 $\varepsilon\to0$）。
- 例：若 $\bar H=1$，產生 0101 的 worst case 就是每個 1 bit——什麼都不用做（長度 1000 就是 1000 次）。

**Mean-resolvability**：
$$\bar S(\boldsymbol X)=\limsup_{n\to\infty}\frac1nH(X^n),$$
就是 $\frac1n\log\frac1{P(X^n)}$ 的**期望值**。
- 【口頭】散開的 CDF 取微分是 PDF，期望值落在分布中間；有大數法則時期望值和端點一樣。
- 證明需要另一個不等式：把「entropy 的差」和「variational distance」連起來（本質上是 log-sum inequality 的變形：先取絕對值相減，和先取 log 再相減有關係），用微積分證。
- 【口頭】Shannon 三大公設這麼簡單的思維，就抓到最重要的量：機率倒數取 log，取期望值，$n\to\infty$，就是平均要花的時間。

> ⚠️ 待確認：[▶ 53:01](https://youtu.be/xKOHD7RHvqQ?t=3181) 老師說 mean-resolvability「是 $\frac1nH(X^n)$ 在 $n\to\infty$」，沒說清楚是 lim、limsup 還是 liminf；上面依第 9 節「limit sup 找最大」的說法寫成 limsup。

---

## 9. 四個量與兩個等式

[▶ 55:07](https://youtu.be/xKOHD7RHvqQ?t=3307)

**壓縮的定義**（複習）：
- **固定長度**：找一個集合，落在外面的機率 $\to0$；集合裡每個用最多 $R$ 個 bit 描述。最小值記 $T(\boldsymbol X)$。
- **不定長度**：沒有錯誤率，每個序列都要 map 到一個 codeword，有長有短；長度大約和 $\log\frac1{P}$ 成正比（機率小的長、大的短——Shannon–Fano–Elias code 就是這樣；Huffman 是 bottom-up 設計，出發點不同，但都是機率導出長度）。平均碼長除以 $n$ 要 $\le R$，最小值記 $\bar T(\boldsymbol X)$。

**四個量**（散開的 CDF 圖）：
1. $\bar H(\boldsymbol X)$：sup-entropy rate（右端）；
2. $\underline H(\boldsymbol X)$：inf-entropy rate（左端）；
3. $\limsup\frac1nH(X^n)$：期望值的最大者；
4. $\liminf\frac1nH(X^n)$：期望值的最小者（每條線的期望值可能不一樣）。

**Theorem（Han–Verdú）**：
$$S(\boldsymbol X)=T(\boldsymbol X)=\bar H(\boldsymbol X),\qquad\bar S(\boldsymbol X)=\bar T(\boldsymbol X)=\limsup_{n\to\infty}\frac1nH(X^n).$$
- 寫程式（worst case）= 固定長度壓縮 = sup-entropy rate；
- 寫程式（average case）= 不定長度壓縮 = entropy rate 的期望值。
- 【口頭】worst case 的要求：程式對**每個長度**都要好——輸入參數 $n=10000$，產生 1 萬個（例如高斯），variational distance $<\varepsilon$；改成 10001 個、10002 個，還是 $<\varepsilon$。
- 【口頭】所以有人說：給我一個資料壓縮法，反向寫就是一個好的隨機變數產生器。老師曾給學生做專題：Huffman code 是好的壓縮，改寫成隨機變數產生器應該也是好的。

【口頭】考試不考證明，但會考概念（問答）：定義、程式的概念——例如當場寫一個產生 $\frac14,\frac12,\frac14$ 的程式應該寫得出來；$\frac13,\frac23$ 或 $\frac15,\frac25,\frac35$ 要 finite 就難了。

---

## 10. 例子：Bernoulli(Z) source

[▶ 61:15](https://youtu.be/xKOHD7RHvqQ?t=3675)

**設定**：要寫程式產生 0101 序列，產生 0 的機率是 $Z_i$、1 的機率 $1-Z_i$，$Z_i$ 是另一個隨機變數：pairwise independent、uniform 在 $[0,1]$（連續）。
- 【口頭】就是黑箱子：很多 i.i.d. 的 Bernoulli($t$)，有一個 selector 每個時間挑一個，你只看得到外面。

**計算**：$\frac1n\log\frac1{P(X^n)}$ 沒有大數法則，收斂到**隨機變數** $h_b(Z)$，$Z\sim U[0,1]$。
- 不定長度要用期望值，需要 converge in mean——確實也成立：
$$E[h_b(Z)]=\int_0^1h_b(z)\,dz=\frac1{2\ln2}\approx0.72135\text{ bits}.$$
- $\bar H=1$ bit（或 $\log2$ nat）：$h_b(Z)$ 可以任意接近 1。

> 以下**不是逐字稿內容**，是驗算：$\int_0^1-z\ln z\,dz=\frac14$，所以 $\int_0^1h_b(z)dz=\frac2{\ln2}\cdot\frac14=\frac1{2\ln2}\approx0.7213$ bit。

**結論**：
- **固定長度**、錯誤率 $\to0$：**不可能壓縮**。長度 1000 就要 1000 bit，什麼都不用做，直接存。
- **不定長度**、錯誤率 0：1000 bit 只要約 **721** bit，節省約 280 bit。有些 source 用不定長度確實壓得更好。
- **寫程式產生它**：worst case 每個 1 次（1000 個要呼叫 1000 次，有限）；平均只要約 721 次。

（這也回應了第 33 集預告的「黑箱子 source：block code 不能壓、variable-length 可以壓」。）

---

## 11. 一頁速查表

**程式複雜度** = 呼叫 fair random bit 的次數。例：$(\frac14,\frac12,\frac14)$ 平均 1.5 = entropy、最差 2——optimal。

**M-type、resolution**：機率都是 $\frac kM$ ⇒ resolution $\log M$（worst case）；無理數機率（$\frac1\pi$）無法在有限時間精確產生，用 variational distance $\le\varepsilon$ 的有理分布逼近。

**定義**：resolvability $S$（worst case，用 resolution）、mean-resolvability $\bar S$（average，用 entropy），$\varepsilon\to0$。

**Knuth–Yao 1976**：$H\le E[\text{呼叫次數}]\le H+2$。

**Han–Verdú 1993**：
- $S=T=\bar H$（worst case = 固定長度壓縮 = sup-entropy rate）。
- $\bar S=\bar T=\limsup\frac1nH(X^n)$（average = 不定長度壓縮 = entropy 的期望值）。
- 關鍵：M-type ⇒ $\frac1n\log\frac1P\le\frac1n\log M$；用不等式把 variational distance 和 log 接起來。

**合成 = 拆解**：產生隨機變數和壓縮是同一件事；壓縮器反向寫就是產生器。

**Bernoulli(Z)，$Z\sim U[0,1]$**：$h_n\to h_b(Z)$；固定長度極限 1（不能壓）、不定長度極限 $\frac1{2\ln2}\approx0.72135$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Source 的 complementary CDF 和 channel 的 CDF 相交與否 ⇒ 能不能傳 | 第 35 集（第 4 章） |
| 「找對的量、按它排序」用在 channel coding；output statistics 和 resolvability | 第 35 集 |

---

## 附：本集一句話總結

> **把「壓縮」反過來看成「寫程式產生隨機變數」：最差情形要呼叫的 random bit 數（resolvability）等於固定長度壓縮極限、也就是 $\log\frac1P$ 分布的右端；平均情形（mean-resolvability）等於不定長度壓縮極限、也就是它的期望值——所以像 Bernoulli(Z) 這種 source，固定長度完全不能壓，不定長度卻能壓到 0.72 bit/bit。**

---

## ⚠️ 待確認清單

1. [▶ 09:42](https://youtu.be/xKOHD7RHvqQ?t=582) 老師對兩個端點 $\underline H$、$\bar H$ 的操作意義的口述，看起來和第 33 集的定理位置相反。
2. [▶ 53:01](https://youtu.be/xKOHD7RHvqQ?t=3181) mean-resolvability 是 $\frac1nH(X^n)$ 的 lim、limsup 還是 liminf，口述不清楚（筆記寫 limsup）。

---

*筆記依據陳伯寧老師「消息理論」Lec34 錄影逐字稿（whisper large-v3-turbo，1:05:39）整理；第二部分課本沒有。*
