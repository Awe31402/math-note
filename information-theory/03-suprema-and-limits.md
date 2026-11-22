---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 3
lecture: "Lec03 Appendix A: Overview on Suprema and Limits A.1-A.4"
date: 待補
video: https://youtu.be/COzuZbzWOxY
notes: Alajaji & Chen 附錄 A §A.1–A.3（pp. 263–267，Definition A.1–Lemma A.17）
---

# 第 3 集 · Lec03 附錄 A：mutual information 的直覺、supremum 與 infimum [▶ 影片](https://youtu.be/COzuZbzWOxY)

← 上一集：[02](02-introduction-information-entropy-coding-theorems.md) ｜ [總目錄](README.md) ｜ 下一集：[04](04-review-suprema-limits-equivalence.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 3 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（41:27，whisper large-v3-turbo）＋ 課本附錄 A §A.1–A.3（pp. 263–267）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「實數」聽成「時數」，「supremum」聽成「Supremant／suprement」，「infimum」聽成「Infinament／Inferment／Informant」，「maximum」聽成「magnum」，「completeness axiom」聽成「completeness axis／Completion Axiom」，「空集合」聽成「空極核」，「threshold」聽成「stretch hold」，「ε（epsilon）」聽成「Epson／Absen」，「error」聽成「area」，「量度」聽成「良度」，「公設」聽成「公社」，「bound」聽成「bund」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Arbitrarily small ≠ exactly zero](#1-arbitrarily-small--exactly-zero)
- [2. Channel capacity 與 mutual information 的直覺](#2-channel-capacity-與-mutual-information-的直覺)
  - [2.1 傳送前，兩端都 uncertain](#21-傳送前兩端都-uncertain)
  - [2.2 Toy example：一維乾淨、一維全被雜訊吃掉](#22-toy-example一維乾淨一維全被雜訊吃掉)
- [3. 為什麼要複習數學](#3-為什麼要複習數學)
- [4. Supremum 與 completeness axiom](#4-supremum-與-completeness-axiom)
- [5. Supremum 的性質與 approximation property](#5-supremum-的性質與-approximation-property)
- [6. Maximum 和 supremum 不一樣](#6-maximum-和-supremum-不一樣)
- [7. Channel coding theorem = 證明一個 supremum](#7-channel-coding-theorem--證明一個-supremum)
- [8. Infimum 與 source coding theorem](#8-infimum-與-source-coding-theorem)
- [9. 有界性與 sup 的運算](#9-有界性與-sup-的運算)
- [10. Threshold 型集合的 sup 與 inf](#10-threshold-型集合的-sup-與-inf)
- [11. 預告：數列與極限](#11-預告數列與極限)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

前半段接續第 2 集，講「arbitrarily small」和 mutual information 的直覺；後半段開始附錄 A：**supremum、infimum** 以及它們和編碼定理證明的關係。

| 主題 | 課本 |
|---|---|
| arbitrarily small vs exactly zero、mutual information 直覺 | 課本沒有（老師口頭） |
| upper bound、supremum、completeness axiom、maximum | §A.1（pp. 263–264） |
| Observation A.5：channel coding theorem 是證明 sup | §A.1（p. 264） |
| infimum、minimum、Observation A.11 | §A.2（pp. 265–266） |
| 有界、sup 的運算、Lemma A.17 | §A.3（pp. 266–267） |
| 數列與極限 | §A.4（只預告，第 4 集講） |

---

## 1. Arbitrarily small ≠ exactly zero

[▶ 00:00](https://youtu.be/COzuZbzWOxY?t=0)

【口頭】老師說到目前為止上的不是數學，是**觀念**，而觀念才是這門課最重要的部分。

- 通訊理論和消息理論裡，**reliable** 有嚴格定義：錯誤率能做到**任意小（arbitrarily small）**——只要給無限大的複雜度。很多工程書寫的 reliable 不是這個意思。
- **任意小 ≠ 剛好是 0**。錯誤率 0 代表一次錯都不能發生（錯誤的機率是 0）。
  - 如果經理要「錯誤率 0、速度 1/3」，可以直接回答：做不到。
- 【口頭】第 1 集介紹的第七本書（Gallager）第二章有介紹 **zero-error capacity** $C_0$：錯誤率真的是 0 時的容量。大部分通道的 $C_0=0$，只有雜訊有特殊性質時才可能大於 0。
- Shannon 很聰明：他證明的是「任意小，但不是 0」，例如 $10^{-20}$、$10^{-40}$、$10^{-60}$。證明裡**一定要有一個 $\varepsilon$**，可以任意小，但不能是 0。這和第 5 節的 supremum 觀念直接相關。

**Capacity 的畫面** [▶ 02:01](https://youtu.be/COzuZbzWOxY?t=121)：每個有雜訊的通道都有一個能力上限 $C$。
- rate $>C$：錯誤率趨近 1。
- rate $<C$：錯誤率可以任意小（趨近 0）。

**定義（口述）** [▶ 03:03](https://youtu.be/COzuZbzWOxY?t=183)：對任何 noisy channel，**channel capacity = 最大的 reliable transmission rate**（錯誤率可任意小的最大傳送效能）。它只跟雜訊的統計特性有關，跟你的設計一點關係都沒有，是先天的。

---

## 2. Channel capacity 與 mutual information 的直覺

### 2.1 傳送前，兩端都 uncertain

[▶ 03:34](https://youtu.be/COzuZbzWOxY?t=214)

Shannon 用了 **mutual information（互資訊）** 這個名詞。【口頭】後來有人追溯歷史，好像在他之前已經有人用類似的名詞。Mutual 是「雙方的」：$X$ 是傳送端、$Y$ 是接收端，mutual information 是兩端**共享的 information**。

**好的 channel code** [▶ 04:34](https://youtu.be/COzuZbzWOxY?t=274)：接收端對傳送端（channel output 對 channel input）越 **certain** 越好——越確定你送的是 0 還是 1，錯誤率越低。

**關鍵**：這是在「還沒開始傳送之前」就要設計好的。
- 手機做好了、碼表設計好了，但使用者要送什麼，**傳送端也還不知道**（uncertain），接收端當然也不知道（uncertain）。
- 所以 input 和 output 在傳送前都是 uncertain。由三個公設，uncertainty 用 entropy 量。

**比喻** [▶ 05:40](https://youtu.be/COzuZbzWOxY?t=340)：假設算出 $X$ 的 uncertainty 是 8 bit，$Y$ 的是 6 bit；其中有 2 bit 是兩邊**共有的**。那就存在一個方法，可以每次送 2 bit 過去。這就是 mutual information 的概念——完全從 uncertainty 出發。

$$\text{uncertainty}=\text{information},\qquad \text{mutual information}=\text{mutual uncertainty}.$$

【口頭】人跟人溝通有三塊：我知道你不知道、你知道我不知道、兩個人都知道。要盡量用兩個人都知道的那塊來溝通，那塊越大越好。老師曾把 mutual information 翻成「**共識**」：共識越大，越容易溝通。共識怎麼量？用 entropy。這完全由機率（雜訊）決定。

### 2.2 Toy example：一維乾淨、一維全被雜訊吃掉

[▶ 08:14](https://youtu.be/COzuZbzWOxY?t=494)

**設定**：每次送一個二維向量 $X=(V_1,V_2)$（像 I domain、Q domain），每一維可以是 A 或 B。通道是自然界的，量出來是：
- 第 1 維：**完全沒有雜訊**，送 A 收 a、送 B 收 b。
- 第 2 維：被雜訊完全打掉，**永遠收到 b**。

**三種 uncertainty** [▶ 09:14](https://youtu.be/COzuZbzWOxY?t=554)：
- **Input uncertainty**：$V_1$、$V_2$ 都不知道是 A 還是 B → 兩維都 uncertain。
- **Output uncertainty**：第 2 維永遠是 b，是 deterministic（certain）；只有第 1 維（老師叫 $\Lambda_1$）uncertain。
- **Shared uncertainty（mutual uncertainty）**：只有第 1 維。

所以設計時要**用第 1 維，不要用第 2 維**。

**輸入的「角度」** [▶ 10:47](https://youtu.be/COzuZbzWOxY?t=647)：A 和 B 被使用的機率是可以設計的（例如碼裡 8 個 A、2 個 B）。改變比例 → 改變傳送端的 entropy → 改變 mutual information。要調到交集最大。

【口頭】溝通要有切入的角度，角度對才能產生最大的共識。Shannon 證明了：**找到最好的輸入角度、讓 mutual information 最大，那個最大值就是 channel capacity**。

**設計例子** [▶ 11:49](https://youtu.be/COzuZbzWOxY?t=709)：Jack（傳送）要送四個事件給 Mary（接收），即 2 bit。
- 第 2 維送不過去，設為 don't care。
- 用第 1 維送兩次：AA、AB、BA、BB 代表四個事件。
- 用 2 次 channel usage 帶 2 bit → **每次 channel usage 帶 1 bit**。

> ⚠️ 逐字稿缺字：原字幕「AA、ABB、ABB」，依「兩次帶四個 event」修正為 AA、AB、BA、BB。

**為什麼四個事件機率都是 1/4？** [▶ 12:19](https://youtu.be/COzuZbzWOxY?t=739) 前面接的是最好的壓縮器，輸出一定 uniform（第 2 集第 12 節）；不是 1/4 就表示壓縮沒做好。所以 source entropy 是 2 bit。

**結論** [▶ 13:51](https://youtu.be/COzuZbzWOxY?t=831)：Shannon 1948 年證明
$$\text{最好的 reliable transmission rate}=\text{最大的 mutual information（最大共識）}.$$
最大值取決於輸入角度（A、B 的使用機率）。上面例子 A、B 各用一半，不一定是最好的設計（老師沒有往下算）。

【口頭】整體脈絡：先想什麼是 information、下定義 → 三個公設得到 entropy → 用 entropy 定義 mutual information → 證明最好的傳送碼和數學上最大的 mutual information 一致。

---

## 3. 為什麼要複習數學

[▶ 14:52](https://youtu.be/COzuZbzWOxY?t=892)

【口頭】
- 直接講三大定律，裡面有些細節同學會不熟，所以先複習機率和一些邏輯（數學）上的東西。
- 老師在美國修課，所有課都拿 A，只有 information theory 拿 B——「要怪老師，因為老師不教這些」。後來自己慢慢搞懂、做這方面研究，才發現這些基礎很重要。所以從「蹲馬步」開始。

**第二個觀念**：information theory 都在**實數**的世界裡。傳輸率、壓縮率都是實數。我們關心的是實數集合的**上界**。

---

## 4. Supremum 與 completeness axiom

[▶ 16:28](https://youtu.be/COzuZbzWOxY?t=988)

傳輸速度越大越好：每個設計的速度都是一個做得到的實數，我們要找它們的「最小上界」。Shannon 探討的就是 transmission efficiency 的 least upper bound。

**Definition A.1（上界，upper bound）**（p. 263）：$u\in\mathbb R$ 是非空集合 $A\subset\mathbb R$ 的上界，若 $A$ 的每個元素都 $\le u$。此時說 $A$ **bounded above**：
$$A\text{ bounded above}\iff(\exists u\in\mathbb R)(\forall a\in A)\ a\le u.$$

**Definition A.2（最小上界，supremum）**（p. 263）：$A$ 非空。$s$ 叫 $A$ 的 supremum，記 $s=\sup A$，若
1. $s$ 是 $A$ 的上界；
2. 對 $A$ 的每個上界 $s'$，都有 $s\le s'$。

【口頭】least upper bound 聽起來有點 low，書裡全部用 supremum。只討論**非空**集合：找空集合的上界很怪。

**Completeness axiom（完備性公設，least upper bound property）** [▶ 17:58](https://youtu.be/COzuZbzWOxY?t=1078)：$\mathbb R$ 的任何非空、有上界的子集合，**一定有** supremum。
- 是公設，不證明。由它可得 supremum **唯一**（也不用證明）。
- 【口頭】不是所有體系都滿足。看論文時就知道大家都在這個公設底下玩，不用問「它有沒有證明 sup 存在」。

**反例：有理數不完備** [▶ 18:29](https://youtu.be/COzuZbzWOxY?t=1109)：如果傳輸速度只討論有理數，Shannon 的 capacity 證明可能出問題。集合
$$\{x\in\mathbb Q:\ x^2<2\}$$
有上界（例如 2），但**不存在有理數**是它的最小上界。

> 以下**不是逐字稿內容**，是補上的理由（老師只說結論）：最小上界若存在必須是 $\sqrt2$，但 $\sqrt2$ 不是有理數。具體說，若有理數 $s$ 是最小上界：$s^2=2$ 不可能；若 $s^2<2$，可以找到比 $s$ 稍大、平方仍 $<2$ 的有理數，$s$ 就不是上界；若 $s^2>2$，可以找到比 $s$ 稍小、平方仍 $>2$ 的有理數上界，$s$ 就不是最小的。

所以我們在實數裡工作。

**延伸實數（extended real numbers）** [▶ 20:29](https://youtu.be/COzuZbzWOxY?t=1229)：有些領域的最佳指標其實是無限大，所以把 $\pm\infty$ 也納進來：$\mathbb R\cup\{-\infty,\infty\}$。約定：
- $A$ 沒有上界 ⇒ $\sup A=\infty$；
- $\sup\emptyset=-\infty$。

課本也採用這個約定（p. 263）。

---

## 5. Supremum 的性質與 approximation property

[▶ 21:30](https://youtu.be/COzuZbzWOxY?t=1290)

**Property A.4（supremum 的性質）**（p. 264）：
1. 在延伸實數裡，任何集合的 supremum 都存在。
2. $(\forall a\in A)\ a\le\sup A$。
3. 若 $-\infty<\sup A<\infty$，則 $(\forall\varepsilon>0)(\exists a_0\in A)\ a_0>\sup A-\varepsilon$。
4. 若 $\sup A=\infty$，則 $(\forall L\in\mathbb R)(\exists b_0\in A)\ b_0>L$。
5. 若 $\sup A=-\infty$，則 $A$ 是空集合。

性質 2 就是「sup 是上界」，由定義直接得到。

**性質 3：approximation property（逼近性質）** [▶ 22:00](https://youtu.be/COzuZbzWOxY?t=1320)：
- 直覺：**supremum 可以無限逼近，但不一定達得到**。
- 證明（依定義）：若某個 $\varepsilon>0$ 找不到 $a_0>\sup A-\varepsilon$，那麼所有 $a\le\sup A-\varepsilon$，即 $\sup A-\varepsilon$ 也是上界；但它比 $\sup A$ 小，和「最小上界」矛盾。
- 【口頭】這就是 Shannon 只能證 arbitrarily small、不能證 exactly zero 的原因：他在 supremum 的世界裡玩，需要留一點點 $\varepsilon$。例如 capacity 是 $\frac13$，對 $\varepsilon=10^{-2},10^{-3},\dots,10^{-20}$ 都找得到做得到的 rate $a_0>\frac13-\varepsilon$，但 $\frac13$ 本身可能做不到。

**性質 4**：sup 是 $\infty$ 時，可以找到越來越大的元素。

---

## 6. Maximum 和 supremum 不一樣

[▶ 24:05](https://youtu.be/COzuZbzWOxY?t=1445)

**Definition A.3（maximum）**（p. 264）：若 $\sup A\in A$，就叫它 **maximum**，記 $\max A$。若 $\sup A\notin A$，說 maximum **不存在**。

**例子** [▶ 24:35](https://youtu.be/COzuZbzWOxY?t=1475)：
- $A=[0,1]$（老師說「0 到 1，1 有包含」）：$\max A=\sup A=1$。
- $A=(0,1)$：$\sup A=1$，但 maximum 不存在。

**Property A.6（maximum 的性質）**（p. 264）：$(\forall a\in A)\ a\le\max A$，且 $\max A\in A$。所以要證 $\alpha=\max A$，要證 (1) $\forall a\in A$，$a\le\alpha$；(2) $\alpha\in A$。

【口頭】工程上這個區分很重要：
- 用 **maximum／minimum** 描述，代表**做得到**。
- 做不到（或不知道做不做得到），只能用 **supremum／infimum**。
- 理論論文對這兩個字的用法很嚴格。

---

## 7. Channel coding theorem = 證明一個 supremum

[▶ 25:37](https://youtu.be/COzuZbzWOxY?t=1537)

**Achievable rate（可達速率）**：
- 某同學設計了一個 channel code，送一次平均帶 0.3 bit。因為已經做出來，0.3 叫 **achievable rate**（這只是描述性的字，不算專有名詞）。
- 另一家公司的工程師做到 0.32，0.32 也是 achievable rate。
- 令 $A$ = 所有 achievable rate 的集合。**Channel capacity = $\sup A$**。是 sup 而不是 max，因為 Shannon 的證明要少一個 $\varepsilon$。

**證明分兩部分** [▶ 27:42](https://youtu.be/COzuZbzWOxY?t=1662)：

1. **Forward part／direct part／achievability part（正向／可達性）**：
$$(\forall\varepsilon>0)(\exists a_0\in A)\ a_0>\alpha-\varepsilon.$$
   - 【口頭】叫 direct，是因為很直接：你說車子時速能跑 100 公里，就開給我看。
   - 就是 Property A.4 的性質 3：對任意小的 $\varepsilon$，都設計得出一個 rate 超過 $\alpha-\varepsilon$ 的碼。
2. **Converse part（反向）** [▶ 28:42](https://youtu.be/COzuZbzWOxY?t=1722)：
$$(\forall a\in A)\ a\le\alpha.$$
   - 要證明**所有人**都設計不出比 $\alpha$ 更好的碼。通常比較 tricky（比較難），因為要涵蓋所有設計。
   - 就是 Property A.4 的性質 2：$\alpha$ 是上界。

【課本補充】課本 Observation A.5（p. 264）就是這段的正式版本：channel coding theorem 通常是在證明某個有限實數 $\alpha$ 是集合 $A$ 的 supremum，所以要證 (A.1.1) 可達性 $(\forall\varepsilon>0)(\exists a_0\in A)\ a_0>\alpha-\varepsilon$ 和 (A.1.2) converse $(\forall a\in A)\ a\le\alpha$。(A.1.2) 說 $\alpha$ 是上界；(A.1.1) 說比 $\alpha$ 小的數都不是上界。

**如果要證的是 maximum** [▶ 29:15](https://youtu.be/COzuZbzWOxY?t=1755)：forward part 沒有 $\varepsilon$，要直接證明 $\alpha\in A$（真的有一個設計達到 $\alpha$）；converse 一樣。Shannon 的證明沒有這種 forward part。

【口頭】現在的證明常常五、六頁，一步一步看反而看不到這些細節，所以先把觀念抽出來講。

---

## 8. Infimum 與 source coding theorem

[▶ 30:48](https://youtu.be/COzuZbzWOxY?t=1848)

完全對偶的想法。**資料壓縮**：壓縮率越低越好，每個做得到的壓縮率是實數，它們有下界，要找**最大的下界**。

**Definition A.7（下界，lower bound）**（p. 265）：$\ell$ 是 $A$ 的下界，若 $A$ 的每個元素都 $\ge\ell$。
**Definition A.8（infimum）**：$\ell=\inf A$，若 $\ell$ 是下界，且對每個下界 $\ell'$ 都有 $\ell\ge\ell'$。
**Completeness axiom（greatest lower bound property）**：非空、有下界的實數集合一定有 infimum。延伸實數裡約定 $\inf\emptyset=\infty$；沒有下界則 $\inf A=-\infty$。
**Definition A.9（minimum）**：若 $\inf A\in A$，叫 $\min A$；否則 minimum 不存在。

**Property A.10（infimum 的性質）**（p. 265）：
1. 延伸實數裡 infimum 都存在。
2. $(\forall a\in A)\ a\ge\inf A$。
3. **approximation property for the infimum**：若 $|\inf A|<\infty$，則 $(\forall\varepsilon>0)(\exists a_0\in A)\ a_0<\inf A+\varepsilon$。
4. 若 $\inf A=-\infty$，則 $(\forall L)(\exists b_0\in A)\ b_0<L$。
5. 若 $\inf A=\infty$，則 $A$ 是空集合。

【口頭】例：infimum 是 $\frac13$，那 $\frac13+0.00001$、$\frac13+0.0000001$……一定做得到；但 $\frac13$ 本身做不做得到不知道，也不是要證明的。entropy 做不做得到也不一定——第 2 集的例子剛好有一個碼達到 $\frac74$。

**Source coding theorem 是證明一個 infimum** [▶ 32:53](https://youtu.be/COzuZbzWOxY?t=1973)：
- Forward（achievability）：$(\forall\varepsilon>0)(\exists a_0\in A)\ a_0<\alpha+\varepsilon$——你說壓縮率能到 1/60，就做給我看（要加一點點 $\varepsilon$）。
- Converse：$(\forall a\in A)\ a\ge\alpha$——對所有設計都是下界。

【課本補充】Observation A.11（pp. 265–266）：source coding theorem 通常是證明某個有限實數 $\alpha$ 是 $A$ 的 infimum，(A.2.1) 是 achievability，(A.2.2) 是 converse。

**為什麼用 sup/inf 而不是 max/min** [▶ 33:24](https://youtu.be/COzuZbzWOxY?t=2004)（【口頭】）：
- 直接證 minimum 要真的造出一個達到 $\alpha$ 的碼，太難；多一個 $\varepsilon$ 的空間，證明簡單很多。
- 工程師直覺是「一定要做到」（max/min 的思維）；數學家可以放寬到 sup/inf：「我不用剛好做到，加一個 $\varepsilon$」，證明的可能性就多很多。這是 Shannon 聰明的地方。
- 而且 Shannon 本來就沒有找到壓縮方法、傳送方法，只證存在性——這也是用 sup/inf 的理由。

**Property A.12**：$(\forall a\in A)\ a\ge\min A$，且 $\min A\in A$。

---

## 9. 有界性與 sup 的運算

[▶ 34:58](https://youtu.be/COzuZbzWOxY?t=2098)

這些性質之後會直接用，不證明。

**Definition A.13（bounded）**：同時有上界和下界叫 bounded，否則 unbounded。
**Lemma A.14**：$A$ bounded $\iff(\exists k\in\mathbb R)(\forall a\in A)\ |a|\le k$。

**Lemma A.15（單調性）**（p. 266）：$A\subset B$（都非空）⇒
$$\sup A\le\sup B,\qquad\inf A\ge\inf B.$$
- 【口頭】全班 60 人取 10 人，10 人中最高的一定不比 60 人中最高的高。之後會設計一些碼、取 subset，就直接用這個。
- 理由：$\sup B$ 是 $B$ 的上界，也就是 $A$ 的上界，所以 $\sup A\le\sup B$。

**Lemma A.16（集合運算）**（p. 266）：定義 $A+B=\{a+b\}$、$k\cdot A=\{ka\}$、$-A=\{-a\}$。
1. $A$、$B$ 都有上界 ⇒ $\sup(A+B)=\sup A+\sup B$。【口頭】兩個指標相加（或加權和）要最大：各自找最大再加起來就是最好。
2. $0<k<\infty$ ⇒ $\sup(k\cdot A)=k\cdot\sup A$。
3. $\sup A=-\inf(-A)$，$\inf A=-\sup(-A)$。

**注意：乘法不一定成立** [▶ 37:32](https://youtu.be/COzuZbzWOxY?t=2252)：$A\cdot B=\{ab\}$ 的 sup 不一定等於 $\sup A\cdot\sup B$。原因是有負數；指標都是正的就沒問題。課本（p. 267）說 $\sup(A\cdot B)>(\sup A)(\sup B)$ 和 $=$ 兩種都可能發生。

> 以下**不是逐字稿內容**，是補的例子（老師說投影片有範例，但沒唸出來）：$A=B=\{-2,-1\}$，$\sup A=\sup B=-1$，乘積 $(\sup A)(\sup B)=1$；但 $A\cdot B=\{4,2,1\}$，$\sup(A\cdot B)=4>1$。

---

## 10. Threshold 型集合的 sup 與 inf

[▶ 38:02](https://youtu.be/COzuZbzWOxY?t=2282)

【口頭】這部分不太會考（也沒辦法考），但對理解證明有幫助。

通訊、detection theory 常用 **threshold function（門檻函數）** 定義指標：把觀察值 $x$ 代進函數 $f$，跟門檻 $\varepsilon$ 比大小，比它小就要、比它大就不要。工程上很方便，第二部分會常這樣定義實數集合。

**Lemma A.17**（p. 267）：
1. $f:\mathbb R\to\mathbb R$ **非遞減（nondecreasing）** ⇒
$$\sup\{x:f(x)<\varepsilon\}=\inf\{x:f(x)\ge\varepsilon\},\qquad \sup\{x:f(x)\le\varepsilon\}=\inf\{x:f(x)>\varepsilon\}.$$
2. $f$ **非遞增** ⇒
$$\sup\{x:f(x)>\varepsilon\}=\inf\{x:f(x)\le\varepsilon\},\qquad \sup\{x:f(x)\ge\varepsilon\}=\inf\{x:f(x)<\varepsilon\}.$$

**要記的兩件事** [▶ 39:32](https://youtu.be/COzuZbzWOxY?t=2372)：
- 把「$<$」換成「$\ge$」，就可以把 sup 換成 inf（方便證明）。
- 「$<$」和「$\le$」得到的 sup **可能不相等**。兩者都一定存在（completeness axiom），但值可能不同。

> 以下**不是逐字稿內容**，是補的例子（對應課本 Fig. A.1）：取非遞減 $f$，在 $[1,2]$ 上 $f(x)=\varepsilon$，$x<1$ 時 $f<\varepsilon$，$x>2$ 時 $f>\varepsilon$。則 $\sup\{x:f(x)<\varepsilon\}=1$，但 $\sup\{x:f(x)\le\varepsilon\}=2$。

> 以下**不是逐字稿內容**，是依 $f$ 非遞減推論的證明關鍵：令 $L=\{x:f(x)<\varepsilon\}$、$U=\{x:f(x)\ge\varepsilon\}$。$f$ 非遞減 ⇒ 任何 $x\in L$、$y\in U$ 都有 $x<y$（否則 $x\ge y$ 推出 $f(x)\ge f(y)\ge\varepsilon$）。而且 $L\cup U=\mathbb R$。所以 $L$ 在左、$U$ 在右，中間的分界點同時是 $\sup L$ 和 $\inf U$。

---

## 11. 預告：數列與極限

[▶ 40:35](https://youtu.be/COzuZbzWOxY?t=2435)

Shannon 證明定理時用的是**一串碼**：把碼長越拉越長。例如：
- 用 1000 個輸入產生 800 個輸出；
- 要更接近（例如 0.32）時，用 1 萬個輸入產生 8000 個輸出；
- ……

每個長度有一個錯誤率，形成一個**數列**，要討論它的**極限**。這部分（§A.4）下一集講。（影片在這裡結束。）

---

## 12. 一頁速查表

**Supremum**
- 定義：最小上界。Completeness axiom：非空有上界 ⇒ sup 存在（且唯一）。$\mathbb Q$ 不完備：$\{x\in\mathbb Q:x^2<2\}$ 沒有有理數 sup。
- 延伸實數：沒上界 ⇒ $\sup=\infty$；$\sup\emptyset=-\infty$。
- 性質：$a\le\sup A$；**逼近性質** $(\forall\varepsilon>0)(\exists a_0\in A)\ a_0>\sup A-\varepsilon$（否則 $\sup A-\varepsilon$ 是更小的上界，矛盾）。

**Maximum**：$\sup A\in A$ 才叫 $\max A$。$[0,1]$：max = sup = 1；$(0,1)$：sup = 1，max 不存在。用 max/min = 做得到。

**Channel coding theorem（Obs. A.5）**：證 $\alpha=\sup A$（$A$ = achievable rates）
- Achievability：$(\forall\varepsilon>0)(\exists a_0\in A)\ a_0>\alpha-\varepsilon$。
- Converse：$(\forall a\in A)\ a\le\alpha$。

**Source coding theorem（Obs. A.11）**：證 $\alpha=\inf A$（$A$ = achievable compression rates）
- Achievability：$(\forall\varepsilon>0)(\exists a_0\in A)\ a_0<\alpha+\varepsilon$。
- Converse：$(\forall a\in A)\ a\ge\alpha$。

**Arbitrarily small ≠ 0**：sup 只保證無限逼近 → 證明要留 $\varepsilon$；zero-error capacity $C_0$ 通常是 0。

**運算**
- $A\subset B$ ⇒ $\sup A\le\sup B$，$\inf A\ge\inf B$。
- $\sup(A+B)=\sup A+\sup B$；$\sup(kA)=k\sup A$（$k>0$）；$\sup A=-\inf(-A)$。
- 乘法不一定：$A=B=\{-2,-1\}$ ⇒ $\sup(AB)=4>1$。

**Lemma A.17**（$f$ 非遞減）：$\sup\{f<\varepsilon\}=\inf\{f\ge\varepsilon\}$，$\sup\{f\le\varepsilon\}=\inf\{f>\varepsilon\}$；「$<$」和「$\le$」可能給不同值。

**Mutual information 直覺**：capacity = 調整輸入分布後最大的「共同 uncertainty」。例：一維乾淨、一維全錯 ⇒ 每次 channel use 帶 1 bit。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 數列、極限、limsup / liminf | 第 4 集（§A.4–A.5） |
| Mutual information 的正式定義 | 第 8 集（§2.2） |
| Infimum 與 source coding theorem 的 achievability / converse | 第 12 集（第 3 章） |
| Supremum 與 channel coding theorem、$C=\max I(X;Y)$ | 第 16–18 集（§4.3） |
| 調輸入分布求 capacity | 第 19 集（§4.5） |
| Threshold 型集合、Lemma A.17 | 第 32–35 集（第二部分） |

---

## 附：本集一句話總結

> **Capacity 是所有 achievable rate 的 supremum、壓縮極限是 infimum——它們只保證「無限逼近」不保證「達到」，所以 Shannon 的定理永遠帶著一個 $\varepsilon$：錯誤率任意小，但不是 0。**

---

*筆記依據陳伯寧老師「消息理論」Lec03 錄影逐字稿（whisper large-v3-turbo，41:27）與 Alajaji & Chen 課本附錄 A §A.1–A.3 整理。*
