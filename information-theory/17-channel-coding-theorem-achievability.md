---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 17
lecture: Lec17 4.3 Block codes for data transmission over DMCs (2/3)
date: 待補
video: https://youtu.be/yUzJwqftyTU
notes: Alajaji & Chen §4.3（pp. 117–122，Definition 4.10、Theorem 4.11 及 forward part 的證明）
---

# 第 17 集 · Lec17 §4.3 (2/3)：operational capacity、channel coding theorem、random coding 證明 [▶ 影片](https://youtu.be/yUzJwqftyTU)

← 上一集：[16](16-block-codes-dmc-channel-capacity-1.md) ｜ [總目錄](README.md) ｜ 下一集：[18](18-channel-coding-converse-fano.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 17 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（58:43，whisper large-v3-turbo）＋ 課本 §4.3（pp. 117–122）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「asymptotic」聽成「syntactic」，「Asymptotic Equipartition」聽成「Asymptotic Equal Partition」，「大數法則」聽成「大樹法則」，「Fano」聽成「final」，「Karush」聽成「Koresh」，「compact」聽成「comebacks」，「ε」聽成「absent／Absinthe」，「Turbo code」聽成「Turbo Coal」，「LDPC」聽成「LDPP」，「with replacement」聽成「with displacement／WithRespacement」，「marginal」正確，「stationary ergodic」聽成「Station Ergatic」，「Cover」正確，「careful」聽成「careless」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 兩個關鍵想法：typical set decoding 與 random coding](#1-兩個關鍵想法typical-set-decoding-與-random-coding)
- [2. 回顧 joint AEP](#2-回顧-joint-aep)
- [3. Operational capacity vs information capacity](#3-operational-capacity-vs-information-capacity)
- [4. Shannon's channel coding theorem](#4-shannons-channel-coding-theorem)
- [5. Weak converse 的下界](#5-weak-converse-的下界)
- [6. 為什麼 max 存在](#6-為什麼-max-存在)
- [7. Forward part 證明：準備](#7-forward-part-證明準備)
- [8. Step 1：random code construction](#8-step-1random-code-construction)
- [9. Step 2：條件錯誤率](#9-step-2條件錯誤率)
- [10. Step 3：平均錯誤率的期望值](#10-step-3平均錯誤率的期望值)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】今天是通訊傳輸**最重要的基礎理論**。定義 operational capacity，敘述 Shannon's channel coding theorem，並完整證明 **forward part**：用 **random coding** 選 encoder、用 **typical set decoding** 當 decoder，證明所有隨機碼的平均錯誤率趨近 0。

| 主題 | 課本 |
|---|---|
| Joint AEP 回顧 | Theorem 4.9（p. 116） |
| Operational capacity | Definition 4.10（p. 117） |
| Channel coding theorem | Theorem 4.11（pp. 117–118） |
| Forward part 的三步證明 | pp. 118–122 |

---

## 1. 兩個關鍵想法：typical set decoding 與 random coding

[▶ 00:00](https://youtu.be/yUzJwqftyTU?t=0)

**Typical set（解決 decoder）**：
- 送 $x^n$ 收到 $y^n$ 都是隨機的，你知道的只有量出來、不能改的條件機率。Shannon 發現存在一個小小的 **pair 集合**：送 $x_1^n$ 幾乎只會收到 $y_1^n$、送 $x_2^n$ 幾乎只會收到 $y_2^n$（漸近地）——形成**很集中的一對一**。
- 解碼：看到 $y_1^n$ 就猜 $x_1^n$，幾乎不會錯；集合外面機率低，亂猜也不影響。
- 【口頭】在大數法則的世界裡，$n$ 很大時傳送端和接收端好像形成了一個 **identity channel**。
- 要有聯合分布，還需要 $P_{X^n}$：$P_{X^n}P_{Y^n|X^n}=P_{X^n,Y^n}$。通道 i.i.d.、輸入也 i.i.d. ⇒ 聯合分布 i.i.d. ⇒ 有大數法則。
- 集合裡一對一的 pair 越多，傳得越快：8 對就每次送 3 bit，16 對就 4 bit。pair 的個數由 $P_{X^n}$ 的選擇決定——所以要**找最好的輸入分布，讓這種 pair 最多**。

**Random coding argument（解決 encoder）** [▶ 04:12](https://youtu.be/yUzJwqftyTU?t=252)：
- 要證明全班有人考 97 分，第一種做法是找到那個人；第二種是算平均——平均 ≥ 97 就一定有人 ≥ 97。
- 全班平均要到 97 不太可能，但可以用**加權平均**：給每個同學一個權重（機率），分數高的權重大，只要加權平均約 97，就一定有人超過 97。
- 對應：每個傳輸設計（碼）有一個錯誤率。找適當的權重（好碼權重大、爛碼權重小），若**加權平均錯誤率可以任意小**，就一定存在一個碼錯誤率任意小。
- 聰明的地方：權重怎麼找？**讓機率自然發生**——$n\to\infty$。
- 【口頭】這個思維後來被很多其他領域拿來用。

---

## 2. 回顧 joint AEP

[▶ 08:18](https://youtu.be/yUzJwqftyTU?t=498)

- Typical set 就是經驗 entropy 趨近 entropy（$-\frac1n\log P$ 的期望值就是 entropy，平均趨近期望值就是大數法則）。曾經有人用不同的 typical set 證，都對——只要找到對的 typical set。
- **AEP**：除了外面機率趨近 0，**裡面每個 pair 的機率幾乎一樣**（約 $2^{-nH(X,Y)}$），一樣重要、不能忽略任何一個（8 個就各 $\frac18$）；個數約 $2^{nH(X,Y)}$。
- 【口頭】Cover 的書有一章講經濟學，老師覺得比較 controversial：只要有人在裡面就有一窩蜂的現象（大家要嘛都不出門、要嘛一起出門，公路蓋再好也會塞車），就不會有大數法則。大數法則要每個人是獨立思考、互不影響的個體，收斂出來的意見才正確。
- 【口頭】抓到這個概念就學到這門課的精髓了；基本的沒學通就一直證很多定理，只會更混淆。

---

## 3. Operational capacity vs information capacity

[▶ 10:53](https://youtu.be/yUzJwqftyTU?t=653)

【口頭】課本把兩者**分開定義**：Shannon 用三個公設定義 entropy，純機率、純數學，跟操作無關；後來才找到它的操作意義——壓縮極限。capacity 也一樣。早期的書沒區分，有點混淆。

**Definition 4.10（operational capacity）**（p. 117）：rate $R$ 對 discrete channel 是 **achievable** 的，若存在一串 $(n,M_n)$ channel code $\mathcal C_n$ 使
$$\liminf_{n\to\infty}\frac1n\log_2M_n\ge R\quad\text{且}\quad\lim_{n\to\infty}P_e(\mathcal C_n)=0.$$
**Operational capacity** $C_{op}$ = 所有 achievable rate 的 supremum。

- 例：$n=10$、$M=8$（3 bit），code rate $\frac3{10}=0.3$ bit / channel use。
- liminf 是最小的極限點；錯誤率要任意小（reliable）。
- 【口頭】要真的找到傳輸碼很難。1948、49 年離 Shannon capacity 非常遠，差 8 dB、10 dB 以上，根本不知道怎麼達到。

**Information capacity**：用 mutual information 數學算出來的
$$C:=\max_{P_X}I(X;Y)=\max_{P_X}I(P_X,P_{Y|X}).$$

Shannon 的貢獻：**兩者相等**。所以設計一個碼若達到 $C$，就一定是最好的、不能再改善。這也表示 Shannon 的三大公設是對的，真正抓到了訊息傳輸、壓縮的量。

---

## 4. Shannon's channel coding theorem

[▶ 14:28](https://youtu.be/yUzJwqftyTU?t=868)

**Mutual information 是兩個機率的函數**（【口頭】要記得）：
$$I(P_X,P_{Y|X})=\sum_x\sum_yP_X(x)P_{Y|X}(y|x)\log_2\frac{P_{Y|X}(y|x)}{\sum_{x'}P_X(x')P_{Y|X}(y|x')}.$$
- 參數一：輸入角度 $P_X$（可以調）；參數二：量測出來的雜訊 $P_{Y|X}$（不能動）。
- 最大的連動量：接收端從 $y_1^n$ 跳到 $y_2^n$，就知道傳送端從 $x_1^n$ 跳到 $x_2^n$。找最好的輸入角度讓連動 pair 最多，就是最大傳輸量 $C$。
- 這個 maximization 數學上一定可以做：對 $P_X$ concave，極值存在且唯一，可以用 Lagrange multiplier 或 KKT 解。

**Theorem 4.11（Shannon's channel coding theorem）**（pp. 117–118）：DMC，有限輸入 $\mathcal X$、有限輸出 $\mathcal Y$，$C:=\max_{P_X}I(X;Y)$。
- **Forward part（achievability）**：對任意 $0<\varepsilon<1$，存在 $\gamma>0$ 和一串 block code $\{\mathcal C_n=(n,M_n)\}$，
$$\liminf_{n\to\infty}\frac1n\log_2M_n\ge C-\gamma,\qquad P_e(\mathcal C_n)<\varepsilon\ \text{for sufficiently large }n.$$
- **Converse part**：對任意 $0<\varepsilon<1$，任何滿足 $\liminf\frac1n\log_2M_n>C$ 的 block code 序列，
$$P_e(\mathcal C_n)>(1-\varepsilon)\mu\quad\text{for sufficiently large }n,$$
其中 $\mu=1-\frac CR>0$（見下一節）；即錯誤率 **bounded away from zero**。

【口頭】
- Forward：要等於 $C$ 很難證，所以證 $C-\gamma$（$C-0.001$），$\gamma$ 任意小——傳輸速度可以任意接近 capacity，錯誤率任意小。例：capacity 10 Mbps，一定存在方法傳 9.9、9.99、9.999 Mbps。
- Converse：和 source coding 不同，這裡證的是 **weak converse**（用 Fano 不等式類似的方法）；source coding 那邊是 strong converse。

---

## 5. Weak converse 的下界

[▶ 18:37](https://youtu.be/yUzJwqftyTU?t=1117)

畫錯誤率對 rate 的圖：
- $R<C$：錯誤率可以趨近 0（長度越拉越長就好）。
- $R>C$：錯誤率有天然的下限 $1-\frac CR$。
- 【口頭】例：capacity 10 Mbps，但 spec 要你在這種雜訊下傳 20 Mbps，錯誤率至少 $1-\frac{10}{20}=\frac12$，所有設計都不可能做得比 50% 好——非常明白的天然界線。
- 實際上在 DMC（例如 AWGN）下也有 **strong converse**：rate 超過 capacity，錯誤率趨近 1。第二部分會用另一個方法證明。
- 定理寫 $(1-\varepsilon)\mu$ 而不是 $\mu$：消息理論為了證明方便都證小一點點（要證大於 3，就證大於 2.9、2.99、2.999……），$\varepsilon$ 任意小時 $1-\varepsilon$ 趨近 1。

---

## 6. 為什麼 max 存在

[▶ 21:44](https://youtu.be/yUzJwqftyTU?t=1304)

Information capacity 是兩個（高維）機率的函數——就是數學。例：輸入 0、1、2、3，就是四個非負、加總為 1 的數上做 maximization。

【課本補充】p. 117 註 5：固定 $P_{Y|X}$，$I(P_X,P_{Y|X})$ 對 $P_X$ **concave 且連續**（對 variational distance 和歐氏距離）；所有輸入分布的集合是 $\mathbb R^{|\mathcal X|}$ 的 **compact（closed and bounded）** 子集。所以 supremum 達得到，可以寫 max。

【口頭】
- 連續一定跟距離有關，要給距離的量度：機率用 variational distance 或 divergence。之後要用 Lagrange multiplier 微分，所以數學上要嚴謹。
- **Closed and bounded 為什麼重要**：取極值時兩個端點都要進來。若範圍不是閉的，函數可能在邊界突然跳起來，極值就取不到。機率 0 和 1 都可以（extreme point，某個機率是 0 或 1）。不過通常極值不在邊界——傳送端最好每個值都用到。

---

## 7. Forward part 證明：準備

[▶ 24:17](https://youtu.be/yUzJwqftyTU?t=1457)

【口頭】證明好幾頁，大概要一節課。抓到概念，後面所有消息理論的證明都是類似的概念。

- Forward 要**證明存在**一個好的設計（不必最好），達到 $C$ 減一點點的速度、錯誤率任意小。
- 實際的傳輸碼是 **deterministic** 的（例如 00 → 90°、11 → 0°……）。1948 年根本不知道怎麼傳，所以 Shannon 用 **implicit（隱含）** 的方式證明：給每個設計 $\mathcal C_n$ 一個被選到的機率，算錯誤率的**期望值**（有的碼錯誤率 0.008、有的 0.8），證明 weighted average 趨近 0。
- 【口頭】因為是 random coding，表示「自然發生」：碼夠長時，隨機找大部分都很好——後來發現是對的。1993 年第一代 **Turbo code** 是第一個在 Shannon capacity **0.7 dB 以內**的碼，基本概念就是非常長（65536 的 1/3 碼，一個 block 約 18 萬 bit），模擬效果非常好、很隨機。後來發現只要夠長，隨機碼幾乎都不錯；但這麼長實作有困難。1998 年左右的 LDPC 一開始也很長，後來要解決的是短碼怎麼做好。

**Case $C=0$** [▶ 27:52](https://youtu.be/yUzJwqftyTU?t=1672)：例如 BSC 的 $\varepsilon=\frac12$（收到 0 來自 0 或 1 的機率一樣），這個通道完全不能用，information capacity 是 0。forward part trivially 成立：取 $M_n=1$（都送同一個，接收端亂猜），$\frac1n\log_21=0\ge0-\gamma$，錯誤率 0。所以只要考慮 $C>0$。
- 【口頭】$C=0$ 也不一定 hopeless：有些通道加 feedback 會變正；之後會介紹 $\varepsilon$-capacity（允許一點錯誤率）。

**參數**（課本 pp. 118–119）：
- 給定 $\varepsilon\in(0,1)$，取 $\gamma\in(0,\min\{4\varepsilon,C\})$。【口頭】$\gamma$ 和 $\varepsilon$ 連動：錯誤率要求越低，$\gamma$ 要越小。乘 4 是為了證明方便——後面要切成幾項加起來小於 $\varepsilon$。$\gamma<C$ 才讓 $C-\gamma>0$。
- $n$ 夠大時，選整數 $M_n$ 使
$$C-\frac\gamma2\ge\frac1n\log_2M_n>C-\gamma.$$
- $\delta:=\frac\gamma8$（八分之一不重要，切幾份加起來小於 $\varepsilon$ 就好）。
- $P_{\hat X}$：達到 capacity 的輸入分布，$C=I(P_{\hat X},P_{Y|X})$。輸入用乘積分布 $P_{\hat X^n}(x^n)=\prod_iP_{\hat X}(x_i)$，對應輸出 $P_{\hat Y^n}$。因為通道 memoryless，$\{(\hat X_i,\hat Y_i)\}$ 也是 i.i.d.：
$$P_{\hat X^n,\hat Y^n}(x^n,y^n)=\prod_iP_{\hat X}(x_i)P_{Y|X}(y_i|x_i).$$
  - 【口頭】改輸入的機率會改輸出的機率；要獨立，是因為**要大數法則**——要存在一個個數少、機率大的集合。i.i.d. 是保證大數法則的一種狀態，但不是唯一（stationary ergodic、Markov 都可以），重要的是結果。大數法則的行為讓科學變成可以操作。

---

## 8. Step 1：random code construction

[▶ 35:30](https://youtu.be/yUzJwqftyTU?t=2130)

**Encoder**：依 $P_{\hat X^n}$ **獨立、可重複地（with replacement）** 選 $M_n$ 個 channel input 當 codebook $\mathcal C_n=\{c_1,\dots,c_{M_n}\}$；$f_n(m)=c_m$。

**例子**（【口頭】）：BSC 最好的輸入角度是 0、1 各 $\frac12$（很對稱，0、1 個數要差不多；第 19 集會算）。要 $M_n=4$ 個長度 6 的 codeword：每一個 bit 都隨機丟，0、1 各 $\frac12$。所以任何一個 codeword 被選到的機率是 $2^{-6}$。
- **With replacement**：允許兩個 codeword 一樣（機率 $2^{-6}\cdot2^{-6}$），這種碼錯誤率一定很糟（接收端分不開）。但沒關係——它在加權平均裡佔的比例非常少，大部分都很好。

**Decoder（typical set decoding）**：
$$g_n(y^n)=\begin{cases}m,&c_m\text{ 是 }\mathcal C_n\text{ 中唯一一個滿足 }(c_m,y^n)\in F_n(\delta)\text{ 的 codeword}\\\text{任意一個},&\text{其他情形}.\end{cases}$$
- 收到 $y^n$（例如 6 個實數值），檢查 4 個 codeword 中**哪一個和它 jointly typical**。$n$ 很大時機率上只會有一個，就猜它。
- 沒有人或超過一個人和它 jointly typical，就亂猜（反正機率很小，當作錯）。

**每個 codebook 被選到的機率**（課本 p. 120）：共有 $|\mathcal X|^{nM_n}$ 種可能的 codebook，
$$\Pr[\mathcal C_n]=\prod_{m=1}^{M_n}P_{\hat X^n}(c_m).$$

【口頭】哪個是最好的不知道，所以證明期望值。從 1948 年到 1998 年才在 AWGN 上達到 Shannon capacity；很多其他通道到現在還做不到。

---

## 9. Step 2：條件錯誤率

[▶ 41:41](https://youtu.be/yUzJwqftyTU?t=2501)

送第 $m$ 個訊息，什麼時候會錯？兩種情形：
1. **沒有人跟我 jointly typical**：$(c_m,y^n)\notin F_n(\delta)$——只能亂猜，當作錯（所以是 ≤）。
2. **有別人也跟我 jointly typical**：存在 $m'\ne m$ 使 $(c_{m'},y^n)\in F_n(\delta)$。

這已經包含了所有可能出錯的情形：
$$\lambda_m(\mathcal C_n)\le\sum_{y^n:\,(c_m,y^n)\notin F_n(\delta)}P_{Y^n|X^n}(y^n|c_m)+\sum_{m'\ne m}\ \sum_{y^n:\,(c_{m'},y^n)\in F_n(\delta)}P_{Y^n|X^n}(y^n|c_m).$$

記號：$F_n(\delta|x^n):=\{y^n:(x^n,y^n)\in F_n(\delta)\}$——所有和 $x^n$ jointly typical 的 $y^n$。

**對第 $m$ 個 codeword 的選法取期望值**（課本 p. 121）：codebook 是隨機選的，所以 $\lambda_m$ 本身是隨機的。第 $m$ 個 codeword 有 $|\mathcal X|^n$ 種可能（BSC 例子 64 種，每種 uniform），且和其他 codeword 的選法獨立：
$$\sum_{c_m}P_{\hat X^n}(c_m)\lambda_m(\mathcal C_n)\le P_{\hat X^n,\hat Y^n}(F_n^c(\delta))+\sum_{m'\ne m}\ \sum_{c_m}\ \sum_{y^n\in F_n(\delta|c_{m'})}P_{\hat X^n}(c_m)P_{Y^n|X^n}(y^n|c_m).$$
- **第一項**：$P_{\hat X^n}P_{Y|X}$ 就是最好的輸入角度下的聯合分布，summation 在 typical set 外面——就是 typical set 外面的機率，$n$ 很大時非常小。
  - 【口頭】所以只要長度夠長（幾萬、幾十萬），隨便設計只要「夠亂」、而且亂度要對（BSC 要 0、1 差不多；用 0.1、0.9 去設計就不好），錯誤率就會很小。

---

## 10. Step 3：平均錯誤率的期望值

[▶ 47:50](https://youtu.be/yUzJwqftyTU?t=2870)

$$E_{\mathcal C_n}[P_e(\mathcal C_n)]=\sum_{\mathcal C_n}\Pr[\mathcal C_n]P_e(\mathcal C_n)=\sum_{c_1}\cdots\sum_{c_{M_n}}P_{\hat X^n}(c_1)\cdots P_{\hat X^n}(c_{M_n})\left(\frac1{M_n}\sum_{m=1}^{M_n}\lambda_m(\mathcal C_n)\right).$$
- $\frac1{M_n}$ 隱含「每個 codeword 被送的機率一樣」（uniform）；每個 codeword 的選法獨立，所以機率相乘。【口頭】在他之前沒人這樣想，這是開啟全新思維的貢獻。
- 把 $\frac1{M_n}\sum_m$ 移到外面。對第 $m$ 個 codeword 的 summation 就是 Step 2 算的；其他 codeword 的 summation 和它無關，機率和為 1，消掉。

**第一項** [▶ 49:55](https://youtu.be/yUzJwqftyTU?t=2995)：$P_{\hat X^n,\hat Y^n}(F_n^c(\delta))<\delta$（$n$ 夠大）。而 $\delta=\frac\gamma8<\frac{4\varepsilon}8=\frac\varepsilon2$，所以第一項 $<\frac\varepsilon2$。
- 【口頭】第一項 $<\frac\varepsilon2$、第二項 $<\frac\varepsilon2$，加起來 $<\varepsilon$——那些 $\frac18$、$\frac12$、4 倍都是為了湊這個數字，但有邏輯脈絡。Cover 等書不在乎這些數字，隨便寫，有些其實是錯的（不 careful），但證明基本上是對的。

**第二項** [▶ 51:26](https://youtu.be/yUzJwqftyTU?t=3086)：對每個 $m'\ne m$，
$$\sum_{c_m}\sum_{c_{m'}}P_{\hat X^n}(c_{m'})P_{\hat X^n}(c_m)\sum_{y^n\in F_n(\delta|c_{m'})}P_{Y^n|X^n}(y^n|c_m).$$
- 意義：$y^n$ 是送 $c_m$ 收到的，卻跑去跟**別人** $c_{m'}$ jointly typical。【口頭】大數法則發生時都是一對一，幾乎不會有一對二，所以這項機率會趨近 0。
- 其他 codeword 的 summation 都消掉，只剩 $c_m$、$c_{m'}$、$y^n$ 三個。
- 對 $c_m$ 加總：$\sum_{c_m}P_{\hat X^n}(c_m)P_{Y^n|X^n}(y^n|c_m)=P_{\hat Y^n}(y^n)$——輸出的 marginal。
- 所以變成 $\sum_{(c_{m'},y^n)\in F_n(\delta)}P_{\hat X^n}(c_{m'})P_{\hat Y^n}(y^n)$：**兩個 marginal 相乘、在 jointly typical set 上加總**。在 typical set 裡：
  - $P_{\hat X^n}(c_{m'})\le2^{-n(H(\hat X)-\delta)}$、$P_{\hat Y^n}(y^n)\le2^{-n(H(\hat Y)-\delta)}$；
  - 個數 $|F_n(\delta)|\le2^{n(H(\hat X,\hat Y)+\delta)}$。
$$\Rightarrow\ \le2^{n(H(\hat X,\hat Y)+\delta)}\,2^{-n(H(\hat X)-\delta)}\,2^{-n(H(\hat Y)-\delta)}=2^{-n(I(\hat X;\hat Y)-3\delta)}=2^{-n(C-3\delta)}.$$
  - 【口頭】$H(X,Y)-H(X)-H(Y)=-I(X;Y)$：mutual information 出現了。要讓這項小，$I$ 要正而且越大越好——共識越大，錯誤率越小。

- 共有 $M_n-1$ 個 $m'$：
$$\text{第二項}\le(M_n-1)2^{-n(C-3\delta)}<2^{n(C-\gamma/2)}2^{-n(C-3\delta)}=2^{n(C-4\delta)}2^{-n(C-3\delta)}=2^{-n\delta}.$$
  （$M_n\le2^{n(C-\gamma/2)}$，而 $\frac\gamma2=4\delta$。）
- 【口頭】這就是為什麼 $M_n$ 要選在 $2^{n(C-\gamma)}$ 和 $2^{n(C-\gamma/2)}$ 之間：$+4\delta$ 和 $-3\delta$ 一消剩 $-\delta$。因為沒辦法證剛好等於 $C$，所以留一點空間。$\delta$ 很小沒關係，$n\to\infty$ 時 $2^{-n\delta}\to0$，一定可以小於 $\frac\varepsilon2$。

**結論**：$n$ 夠大時 $E_{\mathcal C_n}[P_e(\mathcal C_n)]<\varepsilon$，所以**至少存在一個** codebook $\mathcal C_n^*$ 使 $P_e(\mathcal C_n^*)<\varepsilon$，而它的 rate $>C-\gamma$。∎（影片在這裡結束。）

---

## 11. 一頁速查表

**Operational capacity**：$R$ achievable ⟺ 存在 $(n,M_n)$ 碼，$\liminf\frac1n\log M_n\ge R$、$P_e\to0$；$C_{op}=\sup R$。

**Information capacity**：$C=\max_{P_X}I(P_X,P_{Y|X})$（$I$ 對 $P_X$ concave、連續；分布集合 compact ⇒ max 存在）。

**Theorem 4.11**：$C_{op}=C$。
- Forward：$\forall\varepsilon$，rate $\ge C-\gamma$、$P_e<\varepsilon$。
- Weak converse：rate $R>C$ ⇒ $P_e>(1-\varepsilon)(1-\frac CR)$（第 18 集）。例：$C=10$、$R=20$ ⇒ $P_e\ge\frac12$。

**Forward 證明**
- 參數：$\gamma<\min\{4\varepsilon,C\}$；$C-\frac\gamma2\ge\frac1n\log M_n>C-\gamma$；$\delta=\frac\gamma8$；$P_{\hat X}$ 達到 capacity，i.i.d. 選碼。
- Random coding：依 $P_{\hat X^n}$ 獨立、可重複選 $M_n$ 個 codeword；$\Pr[\mathcal C_n]=\prod P_{\hat X^n}(c_m)$。
- Typical set decoding：唯一一個和 $y^n$ jointly typical 的 codeword。
- 錯誤 = (沒人 typical) + (別人也 typical)。
- $E[P_e]\le P(F_n^c)+(M_n-1)\sum_{F_n}P_{\hat X^n}P_{\hat Y^n}<\delta+2^{n(C-4\delta)}2^{-n(C-3\delta)}=\delta+2^{-n\delta}<\varepsilon$。
- 關鍵一步：$\sum_{F_n}P_XP_Y\le2^{n(H(X,Y)+\delta)}2^{-n(H(X)-\delta)}2^{-n(H(Y)-\delta)}=2^{-n(I-3\delta)}$。
- 平均 $<\varepsilon$ ⇒ 存在一個碼 $<\varepsilon$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Converse（Fano 不等式）、strong converse、zero-error | 第 18 集 |
| 求 $\max_{P_X}I$：對稱通道、KKT | 第 19 集（§4.5） |
| 真正構造出達到 capacity 的碼：polar code | 第 20 集（§4.4） |
| Random coding、typical set 用在 joint source-channel | 第 21 集（§4.6） |
| 連續通道的 random coding（Gaussian） | 第 24 集（§5.4） |
| Rate-distortion 的 random coding 證明 | 第 28 集（§6.3） |

---

## 附：本集一句話總結

> **Shannon 不去造好碼，而是「隨機選碼 + 看誰和收到的序列 jointly typical」：出錯只有兩種——沒人 typical（機率 <δ）或別人也 typical（機率約 $M_n2^{-nI}$）——只要 rate 比 $C=\max I(X;Y)$ 小一點，所有隨機碼的平均錯誤率就趨近 0，所以一定存在一個好碼。**

---

*筆記依據陳伯寧老師「消息理論」Lec17 錄影逐字稿（whisper large-v3-turbo，58:43）與 Alajaji & Chen 課本 §4.3 整理。*
