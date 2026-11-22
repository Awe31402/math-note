---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 16
lecture: "Lec16 Chapter 4: Data Transmission and Channel Capacity: 4.3 Block codes … (1/3)"
date: 待補
video: https://youtu.be/ieKSSWoxWoE
notes: Alajaji & Chen §4.1–4.3 前半（pp. 105–117，Definition 4.1–Theorem 4.9）
---

# 第 16 集 · Lec16 第 4 章 (1/3)：資料傳輸的原理、DMC、block code、jointly typical set [▶ 影片](https://youtu.be/ieKSSWoxWoE)

← 上一集：[15](15-universal-lossless-codes.md) ｜ [總目錄](README.md) ｜ 下一集：[17](17-channel-coding-theorem-achievability.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 16 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（42:15，whisper large-v3-turbo）＋ 課本 §4.1–4.3（pp. 105–117）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「quantize」聽成「框台」，「entanglement」正確，「賴青沂老師」可能被聽成「賴清姨」（無法核對，照字幕），「Sergio Verdú」聽成「Serdio Verdu」，「Te Sun Han」聽成「Tyson Hahn」，「discrete memoryless」聽成「discreet memories」，「consistent」正確，「crossover」聽成「cross over」，「erasure」聽成「erratial／Eratio」，「q-ary」聽成「Qery／Cure」，「Huffman」聽成「Hoffman／Hoppen」，「巨觀」聽成「聚觀」，「Proakis」聽成「Project」，「Shannon–McMillan–Breiman」聽成「Shanel-McMillan-Brennan」，「information stable」正確，「typical set」聽成「Typical set」（正確）。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 從壓縮到傳輸](#1-從壓縮到傳輸)
- [2. 選 codeword：讓接收端最少疑慮](#2-選-codeword讓接收端最少疑慮)
- [3. Reliable transmission 與「連動」](#3-reliable-transmission-與連動)
- [4. 系統圖：W 為什麼是 uniform](#4-系統圖w-為什麼是-uniform)
- [5. Discrete channel 與 DMC](#5-discrete-channel-與-dmc)
- [6. 常見的 DMC](#6-常見的-dmc)
- [7. Block code 與平均錯誤率](#7-block-code-與平均錯誤率)
- [8. 最大錯誤率：丟掉一半 codeword](#8-最大錯誤率丟掉一半-codeword)
- [9. Jointly typical set 與 joint AEP](#9-jointly-typical-set-與-joint-aep)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

進入 Shannon 真正要做的事：**有雜訊的資料傳輸**。這一集建立模型與工具：DMC、常見通道（BSC、BEC）、block code、平均與最大錯誤率、jointly typical set。下一集證明 channel coding theorem。

| 主題 | 課本 |
|---|---|
| 資料傳輸的原理、例子 | §4.1（pp. 105–107） |
| Discrete channel、DMC | Definition 4.1–4.2、Observation 4.3（pp. 107–109） |
| Identity、BSC、BEC、BSEC、q-ary | §4.2 例子（pp. 109–113） |
| Block code、平均錯誤率、最大錯誤率 | Definition 4.4–4.5、Observation 4.6（pp. 114–115） |
| Jointly typical set、joint AEP | Definition 4.7、Theorem 4.8–4.9（pp. 116–117） |

---

## 1. 從壓縮到傳輸

[▶ 00:00](https://youtu.be/ieKSSWoxWoE?t=0)

- 對 Shannon 來說，資料壓縮只是開始：它是**無雜訊的傳輸**（送 1 得 1、送 0 得 0），最有效率的傳輸就是壓縮。
- 他真正要做的是**有雜訊的傳輸**。因為有雜訊所以有錯誤率——這就是為什麼他考慮的壓縮也帶著錯誤率 $P_e$（只是趨近 0）；實際用的壓縮則是零錯誤的。
- **Channel capacity** 這個名詞是 Shannon 第一個提出的。

---

## 2. 選 codeword：讓接收端最少疑慮

[▶ 00:30](https://youtu.be/ieKSSWoxWoE?t=30)

**原理**：設計傳輸的 codeword，使接收端猜「你送的是哪一個」時**疑慮（ambiguity）最小**。

**例子**（課本 pp. 105–106）：二元輸入、輸出，送長度 2 的字：
$$P(y=0|00)=1,\quad P(y=0|01)=1,\quad P(y=1|10)=1,\quad P(y=1|11)=1.$$
（看起來沒有雜訊，但收到 0 不知道是 00 還是 01。）
- 事件 A 用 00、B 用 10：完全沒有 ambiguity。
- A 用 00、B 用 01：收到 0 完全不知道是 A 還是 B，只能猜，會猜錯。

**傳輸的角度**（【口頭】）：例如 physical layer 有 0°、90°、180°、270° 四種角度，量化後接收端只分得出兩種狀態。這時你會選 0° 和 180°，不會選 0° 和 90°——雖然實際上有那個角度，但不用。目的是 minimize ambiguity。**不會用全部的 $x$，會刻意選擇傳輸的角度。**

【口頭】老師說這一章的觀念很有趣，但證明有點複雜。

---

## 3. Reliable transmission 與「連動」

[▶ 03:07](https://youtu.be/ieKSSWoxWoE?t=187)

**Reliable transmission**：一般書上沒有明確定義；對 Shannon 來說就是**錯誤率可以任意小**——要 $10^{-5}$ 就有 $10^{-5}$、要 $10^{-6}$ 就有 $10^{-6}$，一定存在方法。目標：把 noisy channel 轉變成 reliable 的傳輸，**傳送速度越快越好**。

【口頭】工程上通常沒有「任意小」的概念，而是一個標準值，例如無線通訊設在 $10^{-4}$ 到 $10^{-5}$，已經夠用。Shannon 說：錯誤率一定能達到那個標準，問的是最大的傳輸速度。

**連動（common part）** [▶ 04:37](https://youtu.be/ieKSSWoxWoE?t=277)：
- 通道有一些狀態，但不一定全用。有些狀態**傳送端變了、接收端沒變**（傳送端轉了 90°，接收端完全一樣）——對傳輸沒有用。
- 傳送端有一點變化、接收端就一定有相對應、量得到的變化——這種**連動**的狀態才拿來傳輸，而且要讓連動最大。
- 還沒運作系統之前，傳送端、接收端都是隨機的，各有 entropy（information rate）。事情發生了就沒有 entropy：彩券開獎前充滿希望（機率不是 0），開了就是中或沒中。兩端共通、連動的部分就是 common part。
- 【口頭】quantum communication 也用連動：系上賴老師（逐字稿「賴清姨」）做 quantum communication，利用 **entanglement**：兩地的 bit 其實是同一個，這邊動那邊就即時動。
- **量化連動**：用三個公設定義的 information，兩端共有的量就是 **mutual information**。這名詞不是 Shannon 第一個用的，之前有論文隱約有這個概念，但他量化得最精準。

【課本補充】課本（p. 106）：設計者要利用傳送端與接收端之間**受雜訊影響最小的共同部分**；這些共同部分在機率上由 channel input 和 output 的 mutual information 刻畫。問題是：**在一個有雜訊的通道上，每次 channel use 最多能可靠地傳多少資訊？** 上例至少是 1 bit per channel use。

---

## 4. 系統圖：W 為什麼是 uniform

[▶ 08:11](https://youtu.be/ieKSSWoxWoE?t=491)

**Fig. 4.1**（p. 106）：
$$W\ \xrightarrow{\text{channel encoder}}\ X^n\ \xrightarrow{P_{Y^n|X^n}}\ Y^n\ \xrightarrow{\text{channel decoder}}\ \hat W.$$

- **通道**還沒有設計、沒有操作，就是一組機率：可能的輸入 $x^n$（例如 $n=3$、±1，有 8 種，用哪幾個還不知道），量出收到 $y^n$ 的機率——**conditional transition probability** $P_{Y^n|X^n}$（從一個地方轉移到另一個地方）。這是量出來、不能改的。
- **$W$** 是要傳的訊息。**假設 uniform**：$W$ 是最好的資料壓縮碼（例如 Huffman）的輸出，前面已經把不要的部分壓掉，所以 uniform。所有通訊設計都假設輸入 uniform（例如 3 bit 有 8 種狀態，每種 $\frac18$）。這是把資料壓縮和資料傳輸**分開來做**。
- **Channel encoder**：選最好的連動，使輸出一看到就知道送了哪一個；decoder 還原出 $\hat W$。

**Rate** [▶ 10:14](https://youtu.be/ieKSSWoxWoE?t=614)：$x_1,x_2,x_3$ 各算一次 **channel use**。例：用 5 次 channel use 帶 3 bit（在 $\mathcal X^5$ 中選 8 個連動最好的狀態），information rate $=\frac35=0.6$。Shannon 很有野心地問：錯誤率任意小時，**最大**的 information rate 是多少？

---

## 5. Discrete channel 與 DMC

[▶ 11:46](https://youtu.be/ieKSSWoxWoE?t=706)

**Definition 4.1（discrete channel）**（p. 107）：有限輸入字母 $\mathcal X$、有限輸出字母 $\mathcal Y$，以及一串 $n$ 維轉移分布 $\{P_{Y^n|X^n}(y^n|x^n)\}_{n=1}^\infty$，每個 $x^n$ 對 $y^n$ 加總為 1，而且這串分布是 **consistent** 的。

**Consistent**（【口頭】）[▶ 12:17](https://youtu.be/ieKSSWoxWoE?t=737)：二維分布把一維加總掉就得到另一維的 marginal。例如 $n+1$ 維的轉移機率把第 $n+1$ 個 $y$、$x$ 加總掉，就得到 $n$ 維的。
- 不一定成立：Verdú 和 Han 有些論文考慮 non-consistent 的情形——有些機率會「escape to infinity」，加總時沒算到。
- 我們考慮的是**巨觀**世界，一般不會有問題；微觀世界的機率才會有奇怪的現象。

**Definition 4.2（discrete memoryless channel, DMC）**（p. 107）：
$$P_{Y^n|X^n}(y^n|x^n)=\prod_{i=1}^nP_{Y|X}(y_i|x_i).$$
- DMC 完全由 $|\mathcal X|\times|\mathcal Y|$ 的**轉移矩陣** $Q=[p_{x,y}]$，$p_{x,y}=P_{Y|X}(y|x)$ 描述；每一列加總為 1（stochastic matrix）。
- memoryless：雜訊的統計特性不隨時間改變，送兩個的機率是各自相乘（條件獨立）。

【課本補充】Observation 4.3（p. 108）：DMC 條件等價於「目前輸出只和目前輸入有關，和過去的輸入、輸出無關」加上「過去的輸出不依賴目前的輸入」。這個定義**不允許 feedback**（有 feedback 時，目前輸入可以是過去輸出的函數）。

---

## 6. 常見的 DMC

[▶ 14:20](https://youtu.be/ieKSSWoxWoE?t=860)

**1. Identity（noiseless）channel**：$P(y|x)=1$ 若 $y=x$。送 1 得 1、送 0 得 0。
- 【口頭】這就是資料壓縮：**source coding theorem 是 channel coding theorem 的特例**。就像牛頓的慣性定律搞不好可以用其他定律解釋，但因為重要而獨立出來。

**2. Binary symmetric channel（BSC）** [▶ 15:21](https://youtu.be/ieKSSWoxWoE?t=921)：
$$Q=\begin{bmatrix}1-\varepsilon&\varepsilon\\\varepsilon&1-\varepsilon\end{bmatrix}.$$
- $\varepsilon$ 叫 **crossover probability**（從 1 cross 到 0）或 **(raw) bit error rate**——不做編碼、每次送一個 bit 時的原始錯誤率。$\varepsilon$ **不是** reliable 的（不能再小）。
- Symmetric：0 變 1 和 1 變 0 的機率一樣。
- 為什麼重要（【口頭】）：(1) 最簡化，模擬、實驗、分析都方便；(2) 有用——很多實際通道的行為都可以用 BSC 描述，研究結果能解釋實際現象，不是數學遊戲。幾乎所有研究都從它開始。課本（p. 110）：它能精確描述「加性無記憶高斯雜訊 + 二元對稱調變 + hard-decision 解調」。
- 送 00 得 00 的機率是 $(1-\varepsilon)^2$（memoryless，兩次獨立）。
- **加法表示**：$Y_i=X_i\oplus Z_i$（mod-2 加法），$Z_i$ i.i.d. Bernoulli($\varepsilon$)、和 $X$ 獨立。【口頭】好處：(1) 可以推廣到三元（mod 3）、四元的 symmetric channel；(2) 算 capacity 時，雜訊和輸入相加很好算（第 19 集）。加法其實就是一張 2 對 1 的表，可以是十進位或二進位的。

**3. Binary erasure channel（BEC）** [▶ 18:54](https://youtu.be/ieKSSWoxWoE?t=1134)：輸出 $\{0,E,1\}$，
$$Q=\begin{bmatrix}1-\alpha&\alpha&0\\0&\alpha&1-\alpha\end{bmatrix}.$$
- 送 0 只可能收到 0 或 **erasure** $E$（被消除了），$\alpha$ 叫 erasure probability。
- 收到 0 或 1 就百分之百對；收到 $E$ 完全不知道是 0 還是 1。
- 【口頭】要兩邊機率都是 $\alpha$ 才是真正的 erasure：若是 0.1 和 0.4，收到 $E$ 時還能知道比較可能來自哪個。uniform 最難猜。
- 很適合 model 網路封包：有 CRC，要嘛送對，要嘛 CRC 不過、不知道是什麼。課本（p. 110）：封包可能因壅塞被丟掉，接收端知道哪裡掉了，但不知道值。

**4. BSEC（binary symmetric erasure channel）**：同時有 crossover $\varepsilon$ 和 erasure $\alpha$（$\varepsilon+\alpha\le1$）。不對稱的版本叫 asymmetric channel with errors and erasures。

**5. $q$-ary symmetric channel**：$Y=X\oplus_qZ$（mod $q$ 加法）；正確機率 $1-\varepsilon$，其他 $q-1$ 個各 $\frac\varepsilon{q-1}$。【口頭】實作上最常碰到的雜訊是**相加的（additive noise）**。也有 $q$-ary erasure channel。

【口頭】只要記 BSC 和 BEC 這兩個最簡單的，考試也集中在這兩個。

---

## 7. Block code 與平均錯誤率

[▶ 22:31](https://youtu.be/ieKSSWoxWoE?t=1351)

**Definition 4.4（fixed-length data transmission code）**（p. 114）：$\mathcal C_n=(n,M)$，block length $n$、rate $\frac1n\log_2M$ message bits / channel use：
1. $M$ 個訊息；
2. Encoder $f:\{1,\dots,M\}\to\mathcal X^n$，codebook $\{f(1),\dots,f(M)\}$；
3. Decoder $g:\mathcal Y^n\to\{1,\dots,M\}$。
- 訊息 $W$ **uniform**：$\Pr[W=w]=\frac1M$。

【口頭】Shannon 那時考慮固定長度，現在的傳輸也還是固定長度。也有人考慮變長的傳輸碼：Princeton 的 Sergio Verdú（西班牙人，很多著名定理是他做的；後來因 MeToo 事件被迫辭職）證明變長傳輸的 capacity 可以比固定長度大很多，但實用上還沒真的用。他另一篇得 best paper 的經典論文是 **timing channel**：打國際電話一接起來就計費，那就不要接——用響一聲、響三聲來傳資料，中間有間隔做 error correction。電話公司很不高興，鈴聲後來改成隨機的（以前 circuit switch 可以控制）。但若 Shannon 還在，搞不好會想：有隨機就當成雜訊，先量一下，還是能轉成 reliable channel。

**Definition 4.5（average probability of error）**（p. 114）：
$$P_e(\mathcal C_n):=\frac1M\sum_{w=1}^M\lambda_w(\mathcal C_n),\qquad\lambda_w(\mathcal C_n):=\Pr[\hat W\ne W\mid W=w]=\sum_{y^n:\,g(y^n)\ne w}P_{Y^n|X^n}(y^n|f(w)).$$
- $\lambda_w$ 是送第 $w$ 個訊息時的條件錯誤率。乘 $\frac1M$ 是因為 $W$ uniform（最好的壓縮器輸出），所以 $P_e=\Pr[\hat W\ne W]$。

**記號** [▶ 26:39](https://youtu.be/ieKSSWoxWoE?t=1599)：$(n,M)$ code、$\mathcal C_n$、或操作上 $W\to f\to X^n\to Y^n\to g\to\hat W$，三種寫法都會用。

---

## 8. 最大錯誤率：丟掉一半 codeword

[▶ 27:09](https://youtu.be/ieKSSWoxWoE?t=1629)

**問題**：如果壓縮做得不好，$W$ 不是 uniform（例如 0.8、0.2），capacity 會不會變？

**Observation 4.6（maximal probability of error）**（p. 115）：更保守的標準
$$\lambda(\mathcal C_n):=\max_w\lambda_w(\mathcal C_n)\ \ge P_e(\mathcal C_n).$$
- 結論：**capacity 一樣**。任何加權平均的錯誤率都 ≤ 最大的；如果最大的都能任意小，任何先驗分布下的加權平均也能任意小。反過來，從 $P_e$ 任意小的碼可以造出 $\lambda$ 任意小、rate 幾乎一樣的碼。

**做法：丟掉一半 codeword**（【口頭】圖像說明）[▶ 29:43](https://youtu.be/ieKSSWoxWoE?t=1783)：
- 在 $\mathcal X^n$ 中選 $M=4$ 個連動最好的點。沒有雜訊時，四個 codeword 在 $\mathcal Y^n$ 各有一個接收值；接收端把 $\mathcal Y^n$ 切成四塊，落在哪塊就猜哪個。送第 1 個訊息的條件錯誤率 $\lambda_1$ = 落在其他三塊的機率。
- 丟掉 $\lambda_w$ 最大的兩個（離彼此太近、容易誤認的）。原本給它們的區域重新分給剩下的兩個，剩下的錯誤區域只會變小，所以新的條件錯誤率**只會變小**。
- 數字例子：$\lambda=(0.1,0.2,0.3,0.4)$，$P_e=0.25$。丟掉 0.3、0.4，留下的兩個（新的可能更小，例如 0.09、0.18）的最大值一定 ≤ 原本較大那一半的最小值 0.3 ≤ $2P_e$。

> 以下**不是逐字稿內容**，是把老師的圖像說法寫成數學：若 $P_e=\frac1M\sum_w\lambda_w\le\varepsilon$，則 $\lambda_w>2\varepsilon$ 的 codeword 不超過 $\frac M2$ 個（否則平均會超過 $\varepsilon$）。所以 $\lambda_w$ 最小的一半全部 $\le2\varepsilon$；只留這一半（解碼區域重新分配只會更好），新碼的 $\lambda\le2\varepsilon$。

- **Rate 損失**：$\frac1n\log_2\frac M2=\frac1n\log_2M-\frac1n$，只少 $\frac1n$。
- 【口頭】例：capacity 0.3 bit / channel use，送 $10^5$ 次帶 $3\times10^4$ bit；$n=100$ 時丟一半變 0.29，帶 $2.9\times10^4$ bit——少了一點點，但 $n\to\infty$ 時沒有差，capacity 完全一樣。
- 【口頭】這是 Shannon 最常用的技巧；實作上也有很多碼這樣做（Proakis 的書有例子）——為了讓效能變好，丟一半。

**結論**：雖然用 $\frac1M$ 計算，任何加權平均、甚至最差的 maximal error，reliable transmission rate 都一樣。

【課本補充】p. 115 註 3：這對轉移分布已知且傳輸期間不變的通道成立；對統計特性在 codeword 傳輸期間未知變化的通道（arbitrarily varying channels）不一定成立，本書不考慮。

---

## 9. Jointly typical set 與 joint AEP

[▶ 36:19](https://youtu.be/ieKSSWoxWoE?t=2179)

又看到熟悉的名字：資料傳輸也是「只抓機率大的那一群，其他丟掉」。

**壓縮 vs 傳輸**（【口頭】助記）：
- 資料壓縮：typical set 用在 **encoder**（encode 的 codebook 就是 typical set）。
- 資料傳輸：typical set 用在 **decoder**（**typical set decoding**）。
- 為什麼：壓縮沒有雜訊，encoder 和 decoder 一樣，在哪邊做都類似；傳輸有雜訊，連動要在接收端判斷。

**連動的集中現象**：$n$ 很大時，大數法則讓 $(x^n,y^n)$ 產生很準確的連動——送這個 sequence 幾乎百分之百收到另一個 sequence，跑到外面的機會很少。收到 $y_1^n$ 就猜 $x_1^n$，幾乎不會錯，不會跑去猜 $x_2^n$。Shannon 沒有找到最好的設計，是用連動思維加存在性證明。

**Definition 4.7（jointly $\delta$-typical set）**（p. 116）：對 $P_{X^n,Y^n}=\prod_iP_{X,Y}(x_i,y_i)$，
$$F_n(\delta):=\left\{(x^n,y^n):\ \left|-\tfrac1n\log_2P_{X^n}(x^n)-H(X)\right|<\delta,\ \left|-\tfrac1n\log_2P_{Y^n}(y^n)-H(Y)\right|<\delta,\ \left|-\tfrac1n\log_2P_{X^n,Y^n}(x^n,y^n)-H(X,Y)\right|<\delta\right\}.$$
（傳送端、接收端、連動端都要集中。）

**Theorem 4.8（joint AEP）**（p. 116）：$(X_i,Y_i)$ i.i.d.，則
$$-\tfrac1n\log_2P_{X^n}(X^n)\to H(X),\quad-\tfrac1n\log_2P_{Y^n}(Y^n)\to H(Y),\quad-\tfrac1n\log_2P_{X^n,Y^n}(X^n,Y^n)\to H(X,Y)$$
in probability（弱大數法則）。

【口頭】i.i.d. 時樣本平均收斂到期望值；stationary ergodic 也對；後來有人推廣到 **information stable channel**。看穿了道理，要的就是大數法則——一個收到 $y^n$ 就差不多知道 $x^n$ 的世界、一個很強的連動。這裡只需要 convergence in probability；第二部分會說 convergence in distribution 就夠了。

**Theorem 4.9（Shannon–McMillan–Breiman for pairs）**（p. 116）：任意 $\delta>0$，
1. $P_{X^n,Y^n}(F_n^c(\delta))<\delta$ for sufficiently large $n$；
2. $(1-\delta)2^{n(H(X,Y)-\delta)}\le|F_n(\delta)|\le2^{n(H(X,Y)+\delta)}$（下界要 $n$ 夠大，上界對所有 $n$）；
3. $(x^n,y^n)\in F_n(\delta)$ ⇒ $2^{-n(H(X,Y)+\delta)}<P_{X^n,Y^n}(x^n,y^n)<2^{-n(H(X,Y)-\delta)}$。

**意義**（【口頭】）：二維集合 $\mathcal X^n\times\mathcal Y^n$ 裡有一群 pair，機率很大，外面很小；encode、decode 只要管裡面，外面亂猜就好。裡面大約有 $2^{nH(X,Y)}$ 個，而且**每個一樣重要**（機率都約 $2^{-nH(X,Y)}$），不能丟掉任何一個。這個概念後來在 information theory 各個領域一直被用到。（影片在這裡結束。）

---

## 10. 一頁速查表

**原理**：選受雜訊影響最小的「連動」部分當 codeword，使接收端 ambiguity 最小；連動的量 = mutual information。

**Reliable**：錯誤率可任意小；目標是最大的 rate $\frac1n\log_2M$（bits / channel use）。

**模型**
- Discrete channel：有限 $\mathcal X,\mathcal Y$，consistent 的 $\{P_{Y^n|X^n}\}$。
- DMC：$P_{Y^n|X^n}=\prod P_{Y|X}(y_i|x_i)$，轉移矩陣 $Q$（列和為 1），無 feedback。
- Identity（= 壓縮）、BSC $Y=X\oplus Z$（$Z\sim$ Bern($\varepsilon$)）、BEC（$\alpha$）、BSEC、$q$-ary symmetric $Y=X\oplus_qZ$。

**Block code** $(n,M)$：$f:\{1..M\}\to\mathcal X^n$、$g:\mathcal Y^n\to\{1..M\}$，$W$ uniform。
- $\lambda_w=\Pr[g(Y^n)\ne w|X^n=f(w)]$；$P_e=\frac1M\sum\lambda_w$；$\lambda=\max\lambda_w$。
- 丟掉最差一半：$P_e\le\varepsilon$ ⇒ 剩下的 $\lambda\le2\varepsilon$，rate 只少 $\frac1n$ ⇒ capacity 不變。

**Jointly typical set**：$x^n$、$y^n$、$(x^n,y^n)$ 的經驗 entropy 都 $\delta$-接近 $H(X)$、$H(Y)$、$H(X,Y)$。
- $P(F_n^c)<\delta$；$|F_n|\approx2^{nH(X,Y)}$；每個機率 $\approx2^{-nH(X,Y)}$。
- 壓縮：typical set 在 encoder；傳輸：typical set 在 decoder。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Operational capacity、channel coding theorem（random coding + typical set decoding） | 第 17 集 |
| Weak converse（Fano）、strong converse | 第 18 集 |
| BSC、BEC 的 capacity；加法雜訊好算 | 第 19 集（§4.5） |
| BEC 上的 polar code | 第 20 集（§4.4） |
| $W$ uniform 的假設、source–channel separation | 第 21 集（§4.6） |
| 連續的 Gaussian channel | 第 24 集（§5.4） |

---

## 附：本集一句話總結

> **有雜訊的傳輸就是挑出「傳送端一動、接收端就一定跟著動」的連動狀態來送；用 DMC 描述通道、用 uniform 的訊息和平均錯誤率衡量好壞（丟掉最差一半就能換成最大錯誤率），而大數法則保證存在一個 jointly typical 的集合，讓接收端幾乎一定猜得對。**

---

*筆記依據陳伯寧老師「消息理論」Lec16 錄影逐字稿（whisper large-v3-turbo，42:15）與 Alajaji & Chen 課本 §4.1–4.3 整理。*
