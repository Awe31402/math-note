---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 2
lecture: Lec02 Chapter 1: Introduction
date: 待補
video: https://youtu.be/Adt1yzIxgns
notes: Alajaji & Chen《An Introduction to Single-User Information Theory》§1.1–1.2（pp. 1–4）；預告 §2.1.1（Theorem 2.1，pp. 5–6）、Definition 2.2（p. 8）、§3.3.2 Theorem 3.31（pp. 86–87）
---

# 第 2 集 · Lec02 Chapter 1：Shannon 的思路、entropy、兩大編碼定理的想法 [▶ 影片](https://youtu.be/Adt1yzIxgns)

← 上一集：[01](01-overview-philosophy-of-information-theory.md) ｜ [總目錄](README.md) ｜ 下一集：[03](03-suprema-and-limits.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 2 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:09:59，whisper large-v3-turbo）＋ 課本 §1.1–1.2（pp. 1–4）、§2.1.1（pp. 5–6）、§3.3.2（pp. 86–87）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Shannon」聽成「宣人／學能／Shenen」，「公設」聽成「公社」，「量度」聽成「良度」，「倒數」聽成「導數」，「碼長」聽成「馬長／碼碼」，「codebook」聽成「co-book」，「criterion」聽成「quiteteron／Quiterion」，「code rate」聽成「Co-rate」，「Rényi」聽成「Rini／Rheny」，「i.i.d.」聽成「RID」，「asymptotic」聽成「asynthetic」，「趨近」聽成「趨勁」，「複雜度」聽成「負雜度」，「錯誤率」聽成「抽率／抽入率」。以下一律用正確的字，不再逐一標。

> 【口頭】老師說：這一章原本有放在課本裡，後來和另一位作者討論，覺得有點囉嗦就刪短了（課本現在的第 1 章只有 4 頁）。但老師覺得它很重要，所以上課還是從這裡講起。投影片沒有公開，公式是從口述和課本重建的。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Shannon 先下定義：information 是「不知道的事」](#1-shannon-先下定義information-是不知道的事)
- [2. 怎麼表示訊息：code 與 codebook](#2-怎麼表示訊息code-與-codebook)
- [3. Compactness：用平均碼長比較兩個碼](#3-compactness用平均碼長比較兩個碼)
- [4. 工程做法 vs Shannon 做法](#4-工程做法-vs-shannon-做法)
- [5. 量測訊息的三個公設](#5-量測訊息的三個公設)
- [6. Self-information 與 entropy](#6-self-information-與-entropy)
- [7. Information theory 是一套思考方法](#7-information-theory-是一套思考方法)
- [8. 「好的碼」要看用途：指數成本與 Rényi entropy](#8-好的碼要看用途指數成本與-rényi-entropy)
- [9. 通道編碼的想法：重複碼與 code rate](#9-通道編碼的想法重複碼與-code-rate)
- [10. 通訊系統模型與分開設計](#10-通訊系統模型與分開設計)
- [11. 壓縮率與 entropy rate](#11-壓縮率與-entropy-rate)
- [12. 最好的壓縮碼，輸出是均勻的](#12-最好的壓縮碼輸出是均勻的)
- [13. 傳輸率與平均錯誤率](#13-傳輸率與平均錯誤率)
- [14. Reliable transmission rate](#14-reliable-transmission-rate)
- [15. 一頁速查表](#15-一頁速查表)
- [16. 與後續集數的連結](#16-與後續集數的連結)

---

## 0. 這堂課要做什麼

這一集不推導定理，而是講 **Shannon 是怎麼想的**：先下定義、再找公設、再證明，最後得到「不用知道怎麼設計，就能算出最好的設計有多好」。

| 主題 | 課本 |
|---|---|
| 什麼是 information、code、codebook | 課本沒有（老師口頭） |
| 三個公設 → self-information、entropy | §2.1.1（pp. 5–6）預告 |
| 指數成本、Rényi entropy | §3.3.2 Theorem 3.31（pp. 86–87）預告 |
| 通訊系統方塊圖、source/channel encoder | §1.2（pp. 2–4） |
| 壓縮率、傳輸率、reliable rate | §1.2 預告；第 3、4 章正式講 |

---

## 1. Shannon 先下定義：information 是「不知道的事」

[▶ 00:00](https://youtu.be/Adt1yzIxgns?t=0)

通訊要把 information（資訊、訊息）從甲地送到乙地。Shannon 先問：**什麼是 information？** 沒有定義，後面的討論就會空泛。

- 他的答案是 **uncertainty（不確定性、未知）**：**接收端不知道的事，才是訊息**。
- 例子：你已經確定「現在在下雨」（I'm certain），那我再告訴你「現在在下雨」，對你就不是 information。

【口頭】老師說這是做研究的基本功：**先下定義**。每個人定義不同，出發點不同，結果就不同。老師也提到投影片上引用的是 Shannon 論文第 6 節的標題，中間那個字就是 uncertainty。

---

## 2. 怎麼表示訊息：code 與 codebook

[▶ 02:00](https://youtu.be/Adt1yzIxgns?t=120)

第二個問題：**怎麼表示（representation）訊息**，讓它方便儲存（store）和傳輸。

- 古代用結繩記事、旗語：打三個結代表什麼，雙方要先講好。
- 英文用 26 個字母串起來代表一個字。
- 數位系統用 **code（碼）**：0、1 串起來，每一串代表一個訊息。code 就像一種語言，可以有很多種設計。

**Codebook（碼本）** [▶ 04:04](https://youtu.be/Adt1yzIxgns?t=244)：所有可能被送出的 0/1 串列成的表，像一本字典（dictionary）。書上常把 book 省略，只寫 code。

- 每一串叫一個 **codeword（碼字）**；串裡每個符號叫 letter 或 alphabet 裡的一個元素。
- 【口頭】老師當兵時編過密碼表：查表就知道 1001 代表什麼，就能和友軍通訊。

**Shannon 的基本假設** [▶ 05:36](https://youtu.be/Adt1yzIxgns?t=336)：

1. 傳送端和接收端**都有同一本 codebook**。
2. 接收端**不知道的只有一件事**：這次送的是哪一個 codeword。
3. 例子：codebook 有五個 codeword（逐字稿念成一長串「00110110111110011101」，可能是 00110、11011、…），接收端知道只會是這五個之一，只是要做 detection（偵測）猜是哪個。

就像和外國人講英文：你知道他講的字都在字典裡，只是不知道他下一個要講哪個字。

【口頭】這些看起來很 trivial，但 Shannon 的厲害就在於把所有事情條列清楚、系統化，才得到 conclusive（決定性的）結果。

---

## 3. Compactness：用平均碼長比較兩個碼

[▶ 08:11](https://youtu.be/Adt1yzIxgns?t=491)

不同語言表達同一件事，有的精簡、有的囉嗦。工程上要**精簡（compactness）**，因為精簡 = 儲存空間少、傳輸時間短。

【口頭】compactness 是古典的用字（CD = Compact Disc），後來的書都改說 **compression（壓縮）** 或 lossless compression。老師說 Blahut 的書用的就是 compactness。

> ⚠️ 逐字稿缺字：原字幕「Blackheart 的書，就是我講的 EYEG 的系主任」。第 1 集 [▶ 18:47](https://youtu.be/i4uhVp_IJE8?t=1127) 老師介紹「Breha 的書，之前是 UIUC 的電機系主任」→ 應為 **Blahut** 的書（EYEG = UIUC 的 ECE）。

**為什麼會有機率？** [▶ 09:44](https://youtu.be/Adt1yzIxgns?t=584)
通訊系統不是只用一次。手機用 10 萬次，或 1000 萬人各送一次，統計下來就會有「50% 的時候送訊息 1、25% 送訊息 2…」。所以設計要看**大量使用下的平均**。

【口頭】老師強調：這門課的證明**全部用同一個方法——大數法則（law of large numbers）**，和其他書略有不同。通訊在乎的是整體平均效能，個別某人比較差沒關係。

**例子**：四個訊息（event）$e_1,e_2,e_3,e_4$，機率 $\frac12,\frac14,\frac18,\frac18$。

| 訊息 | 機率 | Code 1 | Code 2 |
|---|---|---|---|
| $e_1$ | 1/2 | 00 | 0 |
| $e_2$ | 1/4 | 01 | 10 |
| $e_3$ | 1/8 | 10 | 110 |
| $e_4$ | 1/8 | 11 | 111 |

> ⚠️ 逐字稿缺字：原字幕「00011、0011」與「1010、110、110 跟 11」。依後面 [▶ 58:36](https://youtu.be/Adt1yzIxgns?t=2316) 的計算（第一個 bit 是 0 只可能是 $e_1$；$e_2$ 送「10」）和課本常用例，修正為上表。

平均碼長（average codeword length）$\bar\ell=\sum_i p_i\,\ell_i$：

- Code 1：每個長度都是 2，所以 $\bar\ell_1=2$。1000 萬人要 2000 萬 bit。
- Code 2：
$$\bar\ell_2=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=\tfrac12+\tfrac12+\tfrac38+\tfrac38=\tfrac74=1.75.$$
1000 萬人只要 1750 萬 bit，少很多。所以 Code 2 **more compact**。

---

## 4. 工程做法 vs Shannon 做法

[▶ 12:46](https://youtu.be/Adt1yzIxgns?t=766)

問題：給定機率，**最好（most compact）的碼是哪一個？**

**工程做法（engineering view，straightforward approach）**：把所有可能的設計都列出來，每個都算平均碼長，挑最小的。
- 訊息種類少時還行；種類一多，是做不完的苦工（tedious work）。
- 【口頭】就像比價台北市 10 萬家 hotel——定義很清楚，但做不到。「the definition leads us to nowhere」。

**Shannon 做法（alternative approach）** [▶ 14:18](https://youtu.be/Adt1yzIxgns?t=858)：**不知道最好的設計是什麼，但先算出最好的設計的平均碼長是多少。**
- 如果某個碼的平均碼長剛好等於這個數字，它就是最好的，不用再找。
- 【口頭】比喻：已知全班最高是 190 公分，你發現旁邊同學 190 公分，就能確定他是最高的（可能有人跟他一樣高，但沒人更高）。
- 當時大家都說不可能，Shannon 說可以——這是他偉大的貢獻。

做法：去**量測訊息（measure of information）**，再證明這個訊息量就是最好壓縮的平均碼長。

---

## 5. 量測訊息的三個公設

[▶ 16:24](https://youtu.be/Adt1yzIxgns?t=984)

這一步**純粹是機率，跟工程無關**（probabilistic view）。Shannon 先提出三個 **axiom（公設）**：公設不證明，同意就在同一套公設下推導。

【口頭】例子：歐氏幾何的公設「兩條平行線不相交」；投影幾何的公設是「任兩條線交於一點、任兩點決定一條線」（平行線交在無限遠點）。不同公設建立不同的體系。

設事件 $E$ 的機率是 $p$，它帶的訊息量是 $I(p)$。

1. **單調性（monotonicity）** [▶ 17:57](https://youtu.be/Adt1yzIxgns?t=1077)：機率越大，訊息量越小；機率越小，訊息量越大。
   - 【口頭】有的書用 **surprise（驚訝程度）** 來說：0.1% 的事發生了，衝擊大；「明天 80% 會下雨」真的下雨，不太驚訝。uncertainty 只說「不知道」，surprise 才區分「不知道的程度」。
2. **可加性（additivity）** [▶ 18:59](https://youtu.be/Adt1yzIxgns?t=1139)：兩個**獨立**事件同時發生，訊息量直接相加：$I(p_1p_2)=I(p_1)+I(p_2)$。
   - 例子：明天下不下雨、明天股票漲不漲，兩者無關。「又下雨又漲」的訊息量 = 兩者相加。
   - 【口頭】已經發生的事（昨天下不下雨）沒有機率可談，不是 information。
3. **連續性（continuity）** [▶ 20:32](https://youtu.be/Adt1yzIxgns?t=1232)：機率 0.19999 變成 0.20001，訊息量只會微小改變。

**結論**：唯一同時滿足三個公設的函數是
$$I(p)=-\log_2 p=\log_2\frac1p,$$
單位叫 **bit**（以 2 為底）。【口頭】老師說這是 Shannon 論文第 6 節的 Theorem 2；Cover 的書不給證明，但老師覺得很重要，會在**定理 2.1** 證給大家看。

【課本補充】課本 Theorem 2.1（p. 6）的完整敘述：
> 定義在 $p\in[0,1]$ 上、滿足 (1) $I(p)$ 對 $p$ 單調遞減，(2) $I(p)$ 在 $0\le p\le1$ 連續，(3) $I(p_1\times p_2)=I(p_1)+I(p_2)$ 的函數，**只有** $I(p)=-c\cdot\log_b p$，其中 $c>0$ 是常數，底數 $b>1$。

取 $c=1$、$b=2$ 就是 bit。證明在第 8 集。

**為什麼會出現 log？** [▶ 23:03](https://youtu.be/Adt1yzIxgns?t=1383) 重點在第二個公設：獨立事件的機率**相乘**，訊息量要**相加**；相乘變相加，就是 log。【口頭】所以任何分析對象只要有這三個性質，最後都會出現 entropy——這就是 entropy 在熱力學、寫程式、機器學習等領域一再出現的原因。

---

## 6. Self-information 與 entropy

[▶ 23:34](https://youtu.be/Adt1yzIxgns?t=1414)

Shannon 不看設計，只看機率。每個事件發生時帶給你的訊息量叫 **self-information（自資訊）**：

| 訊息 | 機率 | $I=\log_2\frac1p$ |
|---|---|---|
| $e_1$ | 1/2 | 1 bit |
| $e_2$ | 1/4 | 2 bit |
| $e_3$ | 1/8 | 3 bit |
| $e_4$ | 1/8 | 3 bit |

> ⚠️ 逐字稿缺字：原字幕「第四個事件帶四個 bit」。$e_4$ 機率是 1/8，$\log_2 8=3$，應為 3 bit（口誤或聽錯）。

**Entropy（熵）** = self-information 的期望值：每個事件平均帶多少訊息。
$$H=\sum_i p_i\log_2\frac1{p_i}=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=\tfrac74.$$

【課本補充】課本 Definition 2.2（p. 8）：離散隨機變數 $X$（pmf 為 $P_X$）的 entropy 是 $H(X)=-\sum_{x\in\mathcal X}P_X(x)\log_2 P_X(x)$。名字是 Shannon 從統計力學借來的，因為式子和 Boltzmann 的 entropy 一樣（§1.1 註 1，p. 1）。

**重點** [▶ 24:37](https://youtu.be/Adt1yzIxgns?t=1477)：$H=7/4$，剛好等於 Code 2 的平均碼長！Shannon 證明這不是巧合：

> **最好的碼的平均碼長 = source entropy。**

所以：
- 只要知道機率，就能算出最好設計的平均碼長，不必知道怎麼設計。
- Code 2 的平均碼長已經等於 entropy → Code 2 是最好的，沒人能做得更好。

Shannon 證明了「最好的平均碼長」（工程觀點）和「訊息量 entropy」（機率觀點）**完全等效（equivalent）**。

---

## 7. Information theory 是一套思考方法

[▶ 26:11](https://youtu.be/Adt1yzIxgns?t=1571)

從此大家學會用類似的步驟分析各種問題，這門學問叫 **information theory**：它指的是一套**分析的思維體系**。

【口頭】老師的看法：
- 這個體系比定理本身更重要：先想什麼是訊息 → 下定義 → 找公設 → 證明 → 得到和實際設計接上的漂亮結果。
- 很多老師從定義和第一定律直接開始證明。Cover 的書的缺點是：證明完就結束，不討論證明方法、延伸和背後的概念。

**理論極限 vs 真的做到** [▶ 29:19](https://youtu.be/Adt1yzIxgns?t=1759)：Shannon 1948 年證明了極限存在、算得出來，但沒告訴你怎麼設計。

- 【口頭】Channel coding theorem 的 capacity 1948 年就有了，但花了約 50 年才在加性白高斯雜訊（AWGN）通道上做到接近 capacity。
- 1993 年 Turbo code（法國 Berrou 等人）做到離極限約 0.7 dB。
- 1996 年英國 MacKay 的碼更接近（逐字稿「接近 0.0dB」）。
- 1998 年在 Boston 有 50 週年慶祝會，紀念終於在 AWGN 通道上達到 Shannon 的極限。其他通道還沒做到。

> ⚠️ 待確認：[▶ 29:50](https://youtu.be/Adt1yzIxgns?t=1790) 「接近 0.0dB」聽不清楚，可能指「離 Shannon limit 不到 0.1 dB」之類；年份老師自己也改口（1998／1996／1993）。

---

## 8. 「好的碼」要看用途：指數成本與 Rényi entropy

[▶ 31:24](https://youtu.be/Adt1yzIxgns?t=1884)

1948 年的結果是決定性的，但研究沒做完：**「好」的標準跟應用有關（application dependent）**。

- Shannon 的標準：**平均碼長**最小。
- **延遲敏感（delay sensitive）**的應用：要**最長碼長**最小。因為接收端不知道你送哪個，必須等最長的碼長才能確定送完了。這時 Shannon 的定理不能直接用，要重新開發，但可以用同樣的思路。
- 用 Code 1、Code 2 比：看平均碼長，Code 2 好；看最長碼長，Code 1 好（Code 2 最長是 3，是 Code 1 的 1.5 倍）。
- 也可以加上**成本（cost／penalty）**，要平均成本最小。

**指數成本** [▶ 33:59](https://youtu.be/Adt1yzIxgns?t=2039)：碼長 $\ell$ 的成本是 $2^{t\ell}$（$t>0$ 是任意實數）。例如 $t=1$：碼長 1 成本 2、碼長 2 成本 $2^2$、碼長 3 成本 $2^3$。

【口頭】碼越長，delay 越大、記憶空間越大，有些應用的成本真的隨長度指數成長，只是指數不一定是 1，可以是 0.5、1.5。

要讓平均成本 $\sum_i p_i2^{t\ell_i}$ 最小。因為 $t$ 是常數，取 log 再除以 $t$ 不改變誰最小，所以改成最小化
$$L(t)=\frac1t\log_2\left(\sum_i p_i\,2^{t\ell_i}\right).$$

**算兩個碼** [▶ 36:06](https://youtu.be/Adt1yzIxgns?t=2166)：
- Code 1：$L_1(t)=\frac1t\log_2 2^{2t}=2$，常數。
- Code 2：$L_2(t)=\frac1t\log_2\left(\frac12 2^{t}+\frac14 2^{2t}+\frac14 2^{3t}\right)$。

> 以下**不是逐字稿內容**，是依上式推論的檢查：$t=1$ 時括號 $=1+1+2=4$，$L_2(1)=\log_2 4=2=L_1$。$t$ 越大，$2^{3t}$ 那項越重，$L_2$ 越大。所以交叉點在 $t=1$。

結論（老師）：$t>1$ 時 Code 1 較好；$0<t<1$ 時 Code 2 較好。**哪個碼好，見仁見智，看應用。**

**兩個極限** [▶ 36:37](https://youtu.be/Adt1yzIxgns?t=2197)：
- $t\to0$：$L(t)\to$ 平均碼長 $\sum_i p_i\ell_i$（Shannon 的情形）。
- $t\to\infty$：$L(t)\to$ 最長碼長 $\max_i\ell_i$。

所以 Shannon 的結果和「最長碼長」都是這個 formulation 的特例。

**Campbell 1965 與 Rényi entropy** [▶ 37:07](https://youtu.be/Adt1yzIxgns?t=2227)：Campbell 照 Shannon 的方法證明：最好的設計，其成本 $L(t)$ 達到的是 **Rényi entropy**
$$H_\alpha=\frac1{1-\alpha}\log_2\left(\sum_i p_i^{\alpha}\right),\qquad \alpha=\frac1{1+t},$$
代入 $1-\alpha=\frac t{1+t}$，就是老師念的形式
$$\frac{1+t}{t}\log_2\left(\sum_i p_i^{1/(1+t)}\right).$$
叫 Rényi entropy of order $\frac1{1+t}$。$t\to0$（$\alpha\to1$）時就是 Shannon entropy。

> ⚠️ 逐字稿缺字：「Long Campbell」→ Lorne L. Campbell（課本參考文獻 [67]：L.L. Campbell, *A coding theorem and Rényi's entropy*, Inf. Control 8, 1965）。「Cesar」→ Csiszár。

【口頭】
- Campbell 是 Queen's University 的教授，老師去拜訪過他，現在 91 歲還在做研究。
- Rényi 是匈牙利人，已過世；第 1 集介紹的第六本書的作者 Csiszár 是他的學生。
- 公式本身沒什麼，重要的是物理意義：Shannon 的方法照樣可用——給機率就能算出最好的成本。
- entropy 的定義有十幾種，各自是不同應用情境下的最好設計。後來的研究如 constrained capacity、mismatch capacity（接收端某些資訊是錯的），2015 年還有人在做，都用同一套思維。

【課本補充】課本 §3.3.2 Theorem 3.31（pp. 86–87）的正式說法是**漸近的、每符號平均**：對 DMS（離散無記憶信源）和 $n$ 階 D-ary 可唯一解碼碼，定義 $L_n(t)=\frac1t\log_D\sum_{x^n}P_{X^n}(x^n)D^{t\ell(c_{x^n})}$。
- 對任意 $\varepsilon>0$，$n$ 夠大時存在碼使 $\frac1nL_n(t)\le H_\alpha(X)+\varepsilon$；
- 反之，任何可唯一解碼碼的 $\frac1nL_n(t)$ 都不會小於 $H_\alpha(X)$。

詳細在第 15 集附近（3.3.2 節）。

---

## 9. 通道編碼的想法：重複碼與 code rate

[▶ 39:12](https://youtu.be/Adt1yzIxgns?t=2352)

第一定律（資料壓縮，source coding theorem）講完，接著是**第二定律：channel coding theorem**，講資料傳輸（data transmission），通道一定有雜訊（noisy channel）。

設定：
- 傳送的訊息是事先定義好的（雙方有 codebook）。
- 希望錯誤率可以接受。

**降低 code rate** [▶ 40:13](https://youtu.be/Adt1yzIxgns?t=2413)：雜訊會讓對方認錯，所以送慢一點。
- **3 次重複碼（3-time repetition code）**：1 送 111，0 送 000。
- 接收端用多數決（majority rule）：三個 bit 只錯一個，還能更正回來；錯兩個就錯了。這叫錯誤更正碼（error-correcting code）。
- 實體層（physical layer）每送一個 bit 要 10 ms（固定）。重複 3 次後，送一個 information bit 要 30 ms，變慢了。

**Code rate（碼率）** [▶ 41:45](https://youtu.be/Adt1yzIxgns?t=2505)：Shannon 把實體層抽象掉，只看「用幾次通道帶一個 bit」。
- 3 次帶 1 bit → code rate $=\frac13$ bit per **channel usage**（通道使用次數）。4 次帶 1 bit → $\frac14$。
- 跟 bit per second 一致：知道每次 channel usage 是 10 ms，一除就得到 bit/s。
- 也叫 **efficiency**：1 information bit per 3 channel bits。

**Shannon 的問題** [▶ 43:20](https://youtu.be/Adt1yzIxgns?t=2600)：雜訊量好了、不能改（fix a noisy channel）。**什麼設計能讓這個通道有最大的 efficiency？** 同樣先把理論值找出來，前提是**錯誤率可以任意小（arbitrarily small error）**：$10^{-1}$、$10^{-2}$、$10^{-3}$……要多小有多小，而 code rate 固定不變。

---

## 10. 通訊系統模型與分開設計

[▶ 44:20](https://youtu.be/Adt1yzIxgns?t=2660)

資訊傳輸在觀念上就是一連串**函數映射（function mapping）**：

$$Z\ \xrightarrow{\ f\ }\ U\ \xrightarrow{\ g\ }\ X$$

- $Z$：原本要送的事件（source），有機率、有 entropy。
- **Source encoder** $U=f(Z)$：壓縮，**去掉 redundancy（冗餘）**。
  - 【口頭】例子：中文字切掉一半你還認得，另一半就是 redundancy。壓到最好，剩下的量就是 entropy。
- **Channel encoder** $X=g(U)$：通常是一對一（多對一的話接收端分不出來，是自找麻煩）。
- 合起來 $X=g(f(Z))=h(Z)$。設計 $h$ 叫 **joint source-channel coding（聯合信源通道編碼）**。

**什麼時候要合起來設計？** [▶ 47:24](https://youtu.be/Adt1yzIxgns?t=2844)（【口頭】）
- 分開做兩次 mapping 有結構和實作上的問題。各自最好，合起來**不一定**最好。
- 通道**有記憶（memory）**、雜訊前後相關（dependent）時，合起來設計效能較好，複雜度也常較低（只做一次 mapping）。
- Shannon 那篇論文處理的是**無記憶**的雜訊（如 AWGN），合起來沒好處，只增加複雜度 → **分開設計（separate design）**就是最好的，所以他分成兩個定理。
- 所以系上有老師專做通道傳輸、有老師專做資料壓縮；現在漸漸要合起來設計了。

【課本補充】課本 §1.2（pp. 2–3）的方塊圖 Fig. 1.1：
- 傳送端：Source → Source Encoder → Channel Encoder → Modulator → Physical Channel。
- 接收端：Demodulator → Channel Decoder → Source Decoder → Destination。
- 本書把 modulator + physical channel + demodulator 合成一個**離散時間通道（discrete channel）**，用一串條件機率分布描述。
- Source 被建模成隨機過程（見附錄 B）；channel encoder 加 redundancy，通常用代數結構。
- 本書的三個目標：(1) 無雜訊時，用最少的 encoder 符號代表每個 source 符號（無失真或失真 $\le D$）；(2) 在有雜訊通道上、錯誤率任意小時，最大能傳多少資訊率；(3) 保證 source 經過有雜訊通道後在失真 $D$ 內重建。

**連續傳輸** [▶ 48:56](https://youtu.be/Adt1yzIxgns?t=2936)：source encoder 處理的是一長串事件（一支手機連續送，或 1000 萬人各送一次），是大數行為。壓縮後的量要變少（1000 bit 壓成 600 bit），而且這 600 bit 沒有多餘的部分——量就是 entropy。

**Channel encoder 做相反的事** [▶ 49:58](https://youtu.be/Adt1yzIxgns?t=2998)：$X$ 會被雜訊干擾，所以要**加回 redundancy**（保護碼）。但這是**結構性、有目的**地加，用來對抗特定的雜訊，讓系統能 reliably transmit。

【口頭】通訊是系統科學，得到好處就要付代價。Shannon 證明裡的代價是**複雜度**：rate 維持 1/3，錯誤率要 $10^{-20}$，系統複雜度會指數遞增。但只要 1/3 小於 channel capacity，就一定做得到。

---

## 11. 壓縮率與 entropy rate

[▶ 51:59](https://youtu.be/Adt1yzIxgns?t=3119)

**Shannon 第一編碼定理（source coding）** 的單位：$n$ 個 $Z$ 壓成 $k$ 個 $U$。$Z$、$U$ 不一定是 0/1，例如 $U$ 可以是 0、1、2、3。

$$\text{compression rate}=\frac{\text{number of }U}{\text{number of }Z}=\frac kn\quad\textbf{越低越好}.$$

例子：100 個 $Z$ 壓成 25 個 $U$，壓縮率 $\frac14$（平均一個 $U$ 帶四個 $Z$ 的訊息）。

【口頭】老師特別強調「壓縮率越低越好」，因為下一頁的傳輸率剛好倒過來，越高越好。

**假設** [▶ 53:30](https://youtu.be/Adt1yzIxgns?t=3210)：Shannon 證明的是連續傳送，用大數法則，所以假設 $Z_1,Z_2,\dots$ 是 **i.i.d.（independent and identically distributed，獨立同分布）**：每個獨立，機率模型都一樣（例如 1000 萬人用手機的習慣彼此獨立）。

**結果**：最好的碼的最低壓縮率 = source entropy，不需要知道設計。注意 **log 的底數 = $U$ 可能值的個數**：$U$ 是 0/1 就用 $\log_2$；$U$ 是 0、1、2、3 就用 $\log_4$。

**Entropy rate** [▶ 54:31](https://youtu.be/Adt1yzIxgns?t=3271)：因為講的是連續的大數平均，真正要的是
$$\lim_{n\to\infty}\frac1nH(Z_1,\dots,Z_n),$$
叫 entropy rate。$Z$ 是 i.i.d. 時，它就等於單一個 $Z$ 的 entropy。

---

## 12. 最好的壓縮碼，輸出是均勻的

[▶ 56:05](https://youtu.be/Adt1yzIxgns?t=3365)

**怎麼驗證一個壓縮碼好不好？** 看它的輸出。

**觀念**：最好的壓縮碼，輸出 $U$（0/1 串）的 entropy 一定是 **1**（每 bit 帶 1 bit）。
- 理由：如果輸出 entropy 是 0.8，代表每個 bit 只帶 0.8 bit 訊息。由 Shannon 定理，1000 bit 的輸出還能再壓成約 800 bit，而且不失真——那原來的壓縮就不是最好的。
- 輸出 entropy = 1 ⟺ 0 和 1 機率都是 $\frac12$（uniform）：
$$\tfrac12\log_2 2+\tfrac12\log_2 2=1.$$

**例子驗證** [▶ 58:06](https://youtu.be/Adt1yzIxgns?t=3486)：用第 3 節的 Code 2（$e_1\mapsto0$、$e_2\mapsto10$、$e_3\mapsto110$、$e_4\mapsto111$），$Z_1,Z_2,\dots$ i.i.d.，機率 $\frac12,\frac14,\frac18,\frac18$。平均碼長 = entropy = 7/4，是最好的碼。

**第 1 個輸出 bit $U_1$**：$U_1=0$ 只有一種可能——$Z_1=e_1$（其他三個碼字都以 1 開頭）。
$$\Pr(U_1=0)=\Pr(Z_1=e_1)=\tfrac12,\qquad \Pr(U_1=1)=\tfrac12.$$

**第 2 個輸出 bit $U_2$** [▶ 59:06](https://youtu.be/Adt1yzIxgns?t=3546)：$U_2=0$ 有兩種可能：
1. $Z_1=e_2$：碼字「10」，第二個 bit 是 0。機率 $\frac14$。
2. $Z_1=e_1$ 且 $Z_2=e_1$：輸出「0 0」。$Z_1,Z_2$ 獨立，機率 $\frac12\cdot\frac12=\frac14$。

$$\Pr(U_2=0)=\tfrac14+\tfrac14=\tfrac12.$$

【口頭】這不是巧合，是觀念告訴你的。第 3、4、5…個 bit 也都是 uniform；而且每個 $U_k$ 和之前的 $U$ **統計上完全獨立**。老師說本來有提供證明，留給同學自己做。

**Summary** [▶ 61:40](https://youtu.be/Adt1yzIxgns?t=3700)：以平均碼長為標準的最好壓縮碼，輸出是 **asymptotically i.i.d. uniform（漸近獨立均勻）**。

- 為什麼說「漸近」：Shannon 的證明讓 $n,k\to\infty$（這也是他的定理被詬病的地方）。實作都是有限長度（1 GB 的檔案還是有限）。$n,k$ 很大時，輸出的 0、1 個數應該差不多，看不出下一個是 0 還是 1。
- 如果平均碼長**剛好等於** entropy（像上面的例子），輸出就**正好** i.i.d. uniform。一般平均碼長會稍大於 entropy，要 $n,k\to\infty$ 才逼近。
- 實用判斷：**輸出越像 uniform，壓縮越好**。【口頭】現在實際的壓縮碼輸出通常不像 uniform，因為有複雜度等其他考量；Shannon 假設複雜度可以無限大。

---

## 13. 傳輸率與平均錯誤率

[▶ 63:44](https://youtu.be/Adt1yzIxgns?t=3824)

**Channel code 剛好倒過來**：$k$ 個 $U$ 編成 $n$ 個 $X$。

$$\text{code rate（transmission rate）}=\frac{\text{number of }U}{\text{number of }X}=\frac kn\quad\textbf{越高越好}.$$

- 分子都是 $U$。壓縮率 $\frac{\#U}{\#Z}$ 越小越好；傳輸率 $\frac{\#U}{\#X}$ 越大越好。
- 每個 $X$ 帶的 bit 越多越好。三個 $X$ 帶一個 $U$ 就是 $\frac13$。老師說（$U$、$X$ 都是 0/1 時）最大就是 1。
- 目標：錯誤率任意小（criterion）的前提下，efficiency 最大。

**平均錯誤率（average decoding error）** [▶ 64:45](https://youtu.be/Adt1yzIxgns?t=3885)：$U$ 是長度 $k$ 的 0/1 串，有 $2^k$ 種可能（例如 1000 bit 壓成 600 bit，就有 $2^{600}$ 種）。每一種被送時都可能錯，錯誤率是用最好的 decoder 算的。
$$P_e=\frac1{2^k}\sum_{u\in\{0,1\}^k}\Pr\left(\text{解碼錯誤}\mid u\text{ 被送出}\right).$$
例子：$k=3$，看 000 到 111 八種，每個乘 $\frac18$。

> ⚠️ 逐字稿缺字：「最好的 Max Molecular Decoder」。推測是 maximum-likelihood（ML）decoder；在輸入均勻時，ML 和最小錯誤率的 MAP decoder 相同，所以不影響結論。

**為什麼每個 $u$ 都乘 $\frac1{2^k}$？** [▶ 65:46](https://youtu.be/Adt1yzIxgns?t=3946)
- 一般書上直接寫這個公式，不解釋。
- 理由：假設 source encoder 是 **optimal** 的，由第 12 節，它的輸出是 uniform。所以分析 channel code 時，輸入就假設 uniform。
- 所以資料壓縮要做好；channel encoder 的設計標準就是「接在最好的 source encoder 後面」。
- 【口頭】如果接的不是最好的壓縮碼，輸入不 uniform，channel encoder 的設計就該改——有人在研究這個問題。

---

## 14. Reliable transmission rate

[▶ 66:48](https://youtu.be/Adt1yzIxgns?t=4008)

一般書上沒給「reliable」的定義，它其實就是 **arbitrarily small error**。

【口頭】老師的比喻：
1. 經理要你設計系統：錯誤率 $\frac1{10}$（送 10 次對 9 次就好），速度 $\frac13$。若每次傳送 1 ms，$\frac13$ 就是約 333 bit per second。你做出來了。
2. 競爭對手變強，錯誤率要 1%，速度不能變。Shannon 說做得到，只是複雜度高一點。
3. 再變成千分之一，code rate 還是不變——還是做得到。

**定義（口述）**：如果 code rate $R$ **固定不變**，而錯誤率**要多小就能多小**（存在這樣的設計），$R$ 就叫 **reliable transmission rate**，它的錯誤率叫 arbitrarily small。
- Shannon 證明的是**存在性**。
- 代價是複雜度：證明裡碼長要趨近無限長。
- 【口頭】1993 年第一個接近 Shannon limit（約 0.7 dB）的 Turbo code，碼長是 $65536\times3$，老師說「18 萬」，用的是非常長的碼。

> 以下**不是逐字稿內容**，是算術檢查：$65536\times3=196{,}608$，約 20 萬，不是 18 萬。

**Shannon 要找的** [▶ 69:19](https://youtu.be/Adt1yzIxgns?t=4159)：在這個通道上，能達到 arbitrarily small error 的 code rate 裡**最大的那一個**——也就是 channel capacity。（影片在這裡結束。）

【課本補充】課本 §1.2（p. 4）提到：附錄 A 的 Observation A.5 把「集合的上確界（supremum）」和通道編碼定理的證明連起來——capacity 就是所有 reliable rate 的 sup。這正是下一集（附錄 A）要講的。

---

## 15. 一頁速查表

**Shannon 的思路**
定義（information = uncertainty）→ 表示（code、codebook）→ 公設 → 證明 → 「不用知道設計，就算得出最好的設計多好」。

**三個公設 → self-information**
- 單調遞減、連續、獨立相加 $I(p_1p_2)=I(p_1)+I(p_2)$。
- 唯一解：$I(p)=-c\log_b p$（$c>0$，$b>1$）；取 $\log_2$，單位 bit。
- 關鍵：機率相乘 ↔ 訊息相加 ⇒ log。

**Entropy**
$$H=\sum_i p_i\log_2\frac1{p_i}.$$
例：$\left(\frac12,\frac14,\frac18,\frac18\right)$ → $H=\frac12+\frac12+\frac38+\frac38=\frac74$。

**最好的平均碼長 = entropy**
Code 2 = {0, 10, 110, 111}：$\bar\ell=\frac74=H$ ⇒ 最好。Code 1 = {00, 01, 10, 11}：$\bar\ell=2$。

**指數成本（Campbell）**
- $L(t)=\frac1t\log_2\sum_i p_i2^{t\ell_i}$；$t\to0$ 是平均碼長，$t\to\infty$ 是最長碼長。
- 最好的成本 = Rényi entropy $H_\alpha=\frac1{1-\alpha}\log_2\sum_ip_i^\alpha$，$\alpha=\frac1{1+t}$。
- 例：$L_1(t)=2$；$L_2(1)=\log_2(1+1+2)=2$ ⇒ $t>1$ Code 1 好，$t<1$ Code 2 好。

**系統模型**
$Z\xrightarrow{f}U\xrightarrow{g}X$，$h=g\circ f$。無記憶通道 ⇒ 分開設計就最好（separation）；有記憶 ⇒ joint 可能更好。

**兩種 rate**
- 壓縮率 $\frac{\#U}{\#Z}$，越低越好，極限 = entropy rate $\lim\frac1nH(Z^n)$（log 底 = $U$ 的字母數）。
- 傳輸率 $\frac{\#U}{\#X}$，越高越好，極限 = capacity。

**最好的壓縮碼輸出 uniform**
- 輸出 entropy < 1 ⇒ 還能再壓 ⇒ 不是最好。
- 例：$\Pr(U_1=0)=\Pr(Z_1=e_1)=\frac12$；$\Pr(U_2=0)=\Pr(Z_1=e_2)+\Pr(Z_1=Z_2=e_1)=\frac14+\frac14=\frac12$。

**平均錯誤率**
$P_e=\frac1{2^k}\sum_u\Pr(\text{error}\mid u)$；乘 $\frac1{2^k}$ 是因為前面接 optimal source encoder，輸入均勻。

**Reliable rate**
rate 固定、錯誤率要多小有多小（代價：複雜度、碼長 → ∞）。Capacity = 最大的 reliable rate。

---

## 16. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| supremum、極限、「最大的 reliable rate」 | 第 3、4 集（附錄 A） |
| i.i.d.、大數法則、隨機過程 | 第 5–7 集（附錄 B） |
| 三個公設、Theorem 2.1 的證明、entropy | 第 8 集（§2.1） |
| 最好的壓縮率 = entropy（source coding theorem） | 第 12 集（第 3 章） |
| 前綴碼、Huffman code | 第 13、14 集 |
| 指數成本、Rényi entropy（Theorem 3.31） | 第 13–15 集（§3.3） |
| Channel coding theorem、capacity、reliable rate | 第 16–19 集（第 4 章） |
| Turbo/Polar 等接近 capacity 的碼 | 第 20 集（Polar codes） |
| Joint source-channel coding、separation principle | 第 21 集（§4.6）、第 30 集（§6.5） |

---

## 附：本集一句話總結

> **Shannon 不去找最好的碼，而是先證明「最好的碼有多好」：最好的平均碼長就是 entropy，最好的傳輸率就是 capacity。這套「定義 → 公設 → 極限」的思路，才是 information theory 真正的核心。**

---

## ⚠️ 待確認清單

1. [▶ 29:50](https://youtu.be/Adt1yzIxgns?t=1790) 「接近 0.0dB」的確切意思，以及 MacKay／Turbo code 的年份（老師口述反覆修正）。

---

*筆記依據陳伯寧老師「消息理論」Lec02 錄影逐字稿（whisper large-v3-turbo，1:09:59）與 Alajaji & Chen 課本 §1.1–1.2、§2.1.1、§3.3.2 整理。*
