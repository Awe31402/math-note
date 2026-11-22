---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 19
lecture: Lec19 4.5 Calculating channel capacity, 4.5.1 Symmetric, Weakly Symmetric …
date: 待補
video: https://youtu.be/G0hGPooSN3E
notes: Alajaji & Chen §4.5（pp. 131–141，Definition 4.15–Observation 4.28）
---

# 第 19 集 · Lec19 §4.5：算 capacity——對稱、弱對稱、準對稱通道與 KKT 條件 [▶ 影片](https://youtu.be/G0hGPooSN3E)

← 上一集：[18](18-channel-coding-converse-fano.md) ｜ [總目錄](README.md) ｜ 下一集：[20](20-polar-codes-bec.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 19 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（43:22，whisper large-v3-turbo）＋ 課本 §4.5（pp. 131–141）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「weakly symmetric」聽成「weekly symmetric」，「quasi-symmetric」聽成「quieside／Quisi-symmetric」，「erasure」聽成「erratial」，「row」聽成「rho／roll」，「column」聽成「Colent／Colon」，「McEliece」聽成「McLeese」，「upper bound」聽成「upper bond」，「biased」聽成「BIOS」，「Kuhn–Tucker」聽成「Kuhn-Tarker／Quintaker／twin-cutter」，「Lagrange multipliers」聽成「Lagrange Multiplier」（正確），「Sergio Verdú」聽成「Sergio Verdu」，「Polar code」聽成「Polder Code」，「斜率」聽成「邪律／斜律」，「AWGN」聽成「相加白色高斯雜訊」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Shannon 之後的工作：一個一個算 capacity](#1-shannon-之後的工作一個一個算-capacity)
- [2. 對稱通道與弱對稱通道](#2-對稱通道與弱對稱通道)
- [3. 弱對稱通道的 capacity](#3-弱對稱通道的-capacity)
- [4. BSC 與 q-ary symmetric channel](#4-bsc-與-q-ary-symmetric-channel)
- [5. 準對稱通道](#5-準對稱通道)
- [6. BEC 與 BSEC](#6-bec-與-bsec)
- [7. 單一輸入的 mutual information](#7-單一輸入的-mutual-information)
- [8. Capacity 的 KKT 條件](#8-capacity-的-kkt-條件)
- [9. 證明：微分就是 self-information](#9-證明微分就是-self-information)
- [10. KKT 的幾何意義](#10-kkt-的幾何意義)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

Shannon 證明了 $C=\max_{P_X}I(X;Y)$，但沒告訴你各種通道的 $C$ 到底是多少。這一集：
1. 什麼樣的通道，**uniform 輸入**就達到 capacity（symmetric → weakly symmetric → quasi-symmetric），並得到 closed form；
2. 一般情形用 **KKT 條件**判斷最佳輸入：用到的輸入，各自的 mutual information 都等於 $C$。

| 主題 | 課本 |
|---|---|
| 對稱、弱對稱通道 | Definition 4.15、Lemma 4.16、Observation 4.17（pp. 132–134） |
| BSC、q-ary symmetric | Example 4.18–4.19（p. 134） |
| 準對稱通道、BEC、BSEC | Definition 4.20、Lemma 4.21、Example 4.22–4.23（pp. 135–137） |
| 單一輸入的 MI、KKT | §4.5.2 Definition 4.24、Lemma 4.25、Example 4.26–4.27、Observation 4.28（pp. 137–141） |

---

## 1. Shannon 之後的工作：一個一個算 capacity

[▶ 00:00](https://youtu.be/G0hGPooSN3E?t=0)

【口頭】
- Shannon 1948 年做完後，大家開始問：我們關心的傳送管道 capacity 是多少、可以傳多快？再下一步是設計碼達到它（更難）。後續發表了很多論文。
- Shannon 只證了一般公式。DMC 時 $\frac1n\max I(X^n;Y^n)$ 會變成 $\max I(X;Y)$；不是 DMC 時應該看整個 $X^n$ 到 $Y^n$ 的訊息量。
- 例：**AWGN** $Y=X+N$，後人算出 $C=\frac12\log_2(1+\text{SNR})$；最佳輸入是**高斯**（$X$ 可以取 $-\infty$ 到 $\infty$）。若 $X$ 只能是 ±1，就是另一個很複雜的式子（McEliece 他們有導）。
- 意義：算出極限（例如每次傳送 0.8 bit、每次 0.1 ms，就能換算成 Mbps），就能看自己的設計離 Shannon 的理論值多近——這就是後續工程一直在做的。
- 很多通道的 capacity 到現在還算不出來，例如 **fading channel** 只有上下界；最近還有論文在算光學傳輸通道的 capacity。
- 【口頭】Machine learning 的書會有一章 information theory，常強調「讓 entropy 最大化」這些事後定義的東西，但背後的道理其實是大數法則。

**第一步**：$P_{Y|X}$ 是量出來的，要找最好的 $P_X^*$。先問：什麼通道的最佳輸入是 uniform？——**對稱**的通道。

---

## 2. 對稱通道與弱對稱通道

[▶ 01:34](https://youtu.be/G0hGPooSN3E?t=94)

**直覺**（【口頭】）：送哪個輸入，接收端「感覺都一樣」——每個輸入撒到輸出的統計樣子都一樣，只是重排。這時讓共識最大的自然是 uniform（0、1 各 $\frac12$；0、1、2 各 $\frac13$），typical set 裡一對一的 pair 最多。這也反映到真正的設計：012 出現的頻率最好一樣。

**Definition 4.15**（p. 132）：轉移矩陣 $Q=[p_{x,y}]$（$|\mathcal X|\times|\mathcal Y|$）。
- **Symmetric**：$Q$ 的**列彼此是重排**，而且**行彼此也是重排**。（全對稱：輸入的感覺、輸出的感覺都對稱，限制很嚴。）
- **Weakly symmetric**：列彼此是重排，而且**所有行和相等**。

Symmetric ⇒ weakly symmetric。

**例子**（課本 p. 132）：
- Symmetric：BSC、$q$-ary symmetric channel，以及
$$Q=\begin{bmatrix}0.4&0.1&0.5\\0.5&0.4&0.1\\0.1&0.5&0.4\end{bmatrix}.$$
- Weakly symmetric（不是 symmetric）：
$$Q=\begin{bmatrix}0.5&0.25&0.25&0\\0.5&0.25&0.25&0\\0&0.25&0.25&0.5\\0&0.25&0.25&0.5\end{bmatrix}$$
  （列是重排；行和都是 1，但行不是彼此的重排。）

【口頭】老師說後來發現不需要全對稱，**只要列是重排、行和是常數**（weakly symmetric）就夠了——他要找的就是「輸入 uniform 就達到最好傳送速度」的通道。

---

## 3. 弱對稱通道的 capacity

[▶ 10:49](https://youtu.be/G0hGPooSN3E?t=649)

**Lemma 4.16**（p. 133）：弱對稱通道的 capacity 由 **uniform 輸入**達到，而且
$$C=\log_2|\mathcal Y|-H(q_1,q_2,\dots,q_{|\mathcal Y|}),$$
$(q_1,\dots,q_{|\mathcal Y|})$ 是 $Q$ 的任一列（各列只是重排，entropy 一樣）。

**直覺**（【口頭】）[▶ 11:21](https://youtu.be/G0hGPooSN3E?t=681)：
- 例：輸入 0、1、2、3（四個旋轉角度），但接收端的 sensor 很便宜，只能回報 0 或 1。輸入最多 2 bit（uniform 時；大家都有機會被送最好——季後賽如果有一隊奪冠機率超高就不好看，entropy 很低），但接收端最多分辨 1 bit：$I\le H(Y)\le\log_2|\mathcal Y|$。
- 第二項 $H(q_1,q_2)$ 是**雜訊的訊息量**：$q_1=0.99$、$q_2=0.01$（很偏），它很小，能傳的多；$q_1=q_2=\frac12$，它是 1，$C=1-1=0$，完全不能傳——符合直覺。

**證明**（課本 p. 133）：
$$I(X;Y)=H(Y)-H(Y|X)=H(Y)-\sum_xP_X(x)H(Y|X=x).$$
- 每一列都是重排，所以 $H(Y|X=x)=H(q_1,\dots,q_{|\mathcal Y|})$ 對每個 $x$ 都一樣——**是常數，跟輸入分布無關**（每個輸入對雜訊的影響都一樣）。所以 $H(Y|X)=H(q_1,\dots)$。
- 於是 $I(X;Y)=H(Y)-H(q_1,\dots)\le\log_2|\mathcal Y|-H(q_1,\dots)$，等號 iff $Y$ uniform。
- **輸入 uniform ⇒ 輸出 uniform**：$P_Y(y)=\sum_x\frac1{|\mathcal X|}p_{x,y}=\frac1{|\mathcal X|}\times(\text{行和})$，而行和都相等，所以 $P_Y$ 是常數，即 uniform。上界達到。∎

【口頭】AWGN 送 ±1 也是對稱的：$Y|X$ 只是平移（高斯 variance 一樣，mean 在 +1 或 −1），所以 ±1 各 $\frac12$ 達到 capacity——只要是平移就對。

【課本補充】Observation 4.17（p. 134）：若弱對稱通道是方陣（$|\mathcal X|=|\mathcal Y|$），它其實是 symmetric。

---

## 4. BSC 與 q-ary symmetric channel

[▶ 18:27](https://youtu.be/G0hGPooSN3E?t=1107)

**Example 4.18（BSC）**（p. 134）：hard decision 後送 ±1 就變成 BSC（0、1 只是代號）。
$$C=\log_22-H(1-\varepsilon,\varepsilon)=1-h_b(\varepsilon),$$
最佳輸入 0、1 各 $\frac12$。

**Example 4.19（$q$-ary symmetric）**（p. 134）：
$$C=\log_2q-H\left(1-\varepsilon,\tfrac\varepsilon{q-1},\dots,\tfrac\varepsilon{q-1}\right)=\log_2q+\varepsilon\log_2\frac\varepsilon{q-1}+(1-\varepsilon)\log_2(1-\varepsilon).$$
$q=2$ 時回到 BSC；$\varepsilon=0$ 時是無雜訊的 $q$-ary identity channel，$C=\log_2q$。

【口頭】早期的設計都達不到這麼快，都比它小。

---

## 5. 準對稱通道

[▶ 19:27](https://youtu.be/G0hGPooSN3E?t=1167)

uniform 輸入達到 capacity，一定要 weakly symmetric 嗎？**不是**。有些通道不對稱，但 uniform 還是最好。

**Definition 4.20（quasi-symmetric）**（p. 135）：$Q$ 可以**沿著行（column）切成** $m$ 個弱對稱的子矩陣 $Q_1,\dots,Q_m$（$\mathcal Y_1\cup\cdots\cup\mathcal Y_m=\mathcal Y$、互不相交）。

symmetric ⇒ weakly symmetric ⇒ quasi-symmetric。

【口頭】
- 例：輸出 0–4，把行切成 $\{0,1,2\}$ 和 $\{3,4\}$ 兩個 sub-channel，各自是 weakly symmetric，就叫 quasi-symmetric。
- 特性：**輸入 uniform 能達到 capacity，但輸出不會是 uniform**（因為不對稱）。若要求輸入、輸出都 uniform，那就是 weakly symmetric。
- 各本書對 quasi-symmetric 的定義有些差距；目的都是找「輸入 uniform 就達到 capacity」的通道。課本的定義比另一本書廣一點。

**Lemma 4.21**（p. 135）：準對稱通道的 capacity 由 uniform 輸入達到，
$$C=\sum_{i=1}^ma_iC_i,$$
- $a_i:=\sum_{y\in\mathcal Y_i}p_{x,y}$ = $Q_i$ 任一列的和（因為 $Q_i$ 弱對稱，和 $x$ 無關）；
- $C_i=\log_2|\mathcal Y_i|-H\left(\tfrac1{a_i}Q_i\text{ 的任一列}\right)$：把 $Q_i$ 每項除以 $a_i$ 變成合法的轉移矩陣後，這個弱對稱 sub-channel 的 capacity。

【口頭】直覺：傳送時，有一定比例（$a_i$）的時候是往第 $i$ 個 sub-channel 送。證明和前面類似（用 ≤，每列都一樣），最後代 uniform 發現達到上界。

---

## 6. BEC 與 BSEC

[▶ 24:04](https://youtu.be/G0hGPooSN3E?t=1444)

**Example 4.22（BEC）**（p. 136）：切成 $\{0,1\}$ 和 $\{E\}$ 兩組：
$$Q_1=\begin{bmatrix}1-\alpha&0\\0&1-\alpha\end{bmatrix},\qquad Q_2=\begin{bmatrix}\alpha\\\alpha\end{bmatrix}.$$
- $a_1=1-\alpha$，$C_1=\log_22-H(1,0)=1$。
- $a_2=\alpha$，$C_2=\log_21-0=0$（只有一個輸出，帶不了任何 information）。
$$C=(1-\alpha)\cdot1+\alpha\cdot0=1-\alpha.$$

**為什麼大家喜歡用 BEC 驗證**（【口頭】）[▶ 25:38](https://youtu.be/G0hGPooSN3E?t=1538)：
- 公式非常漂亮、直觀：$\alpha=0.2$，80% 送得到、20% 被 erase，能送的就是 0.8。傳送速度低於 80% 一定存在錯誤率任意小的方法；超過 80% 一定不可能——被 erase 之後對 0 和 1 機會一樣，完全沒辦法回復。$\alpha=0.3$ 就是 0.7。公式裡沒有 entropy。
- BSC 才是真正通訊系統比較常用的（hard decision 後沒有 erasure），但 $1-h_b(\varepsilon)$ 你要查表、畫圖，不容易直觀看出 $\varepsilon=0.1$ 或 0.2 時是多少。
- 所以很多驗證（例如之後的 polar code）用 BEC。

**Example 4.23（BSEC）**（p. 137）：一樣切成 $\{0,1\}$ 和 $\{E\}$：
$$C=(1-\alpha)\left[1-h_b\left(\frac\varepsilon{1-\alpha}\right)\right].$$
$\alpha=0$ 時回到 BSC 的 $1-h_b(\varepsilon)$；$\varepsilon=0$ 時回到 BEC 的 $1-\alpha$。

【口頭】AWGN 也用同樣的方法證（之後會算）。還可以再介紹很多常見通道，但概念都一樣。

---

## 7. 單一輸入的 mutual information

[▶ 28:08](https://youtu.be/G0hGPooSN3E?t=1688)

**Definition 4.24（mutual information for a specific input symbol）**（p. 137）：
$$I(x;Y):=\sum_yP_{Y|X}(y|x)\log_2\frac{P_{Y|X}(y|x)}{P_Y(y)},\qquad I(X;Y)=\sum_xP_X(x)I(x;Y).$$
固定一個輸入 $x$，看它到所有可能 $y$ 的「連動量」。（老師也叫它 self-information。）

---

## 8. Capacity 的 KKT 條件

[▶ 28:39](https://youtu.be/G0hGPooSN3E?t=1719)

**Lemma 4.25（KKT conditions for channel capacity）**（p. 138）：DMC 的輸入分布 $P_X$ 達到 capacity **iff** 存在常數 $C$ 使
$$I(x;Y)=C\quad\forall x:P_X(x)>0;\qquad I(x;Y)\le C\quad\forall x:P_X(x)=0.$$

**意義**（【口頭】）：
- 輸入有 0、1、2、3。找到最好的輸入分布後，可能 $P^*(1)=P^*(3)=0$——這兩個**不用**，因為用了對傳送端和接收端的連動、共識完全沒有幫助。
- **凡是機率是正的輸入，各自和輸出的連動量完全相等，而且就等於 capacity**。例：BEC 最佳輸入是 0、1 各 $\frac12$，可以預測 $I(0;Y)=I(1;Y)=1-\alpha$。「訊息量都一樣，所以一樣地使用。」
- 只要我要用你，我們能傳的訊息量都一樣；不然我就不用你。

**(⇐) 很容易**：若條件成立，$I(X;Y)=\sum_xP_X(x)I(x;Y)=\sum_{x:P_X(x)>0}P_X(x)\cdot C=C$。（老師說「if 沒問題」，converse 用微分證。）

【課本補充】**Example 4.27**（p. 140）：三元輸入、二元輸出，
$$Q=\begin{bmatrix}1&0\\\frac12&\frac12\\0&1\end{bmatrix}.$$
不是 quasi-symmetric。猜最佳輸入是 $\left(\frac12,0,\frac12\right)$——因為 $x=1$ 收到 0 或 1 的機率一樣，沒用。此時 $P_Y=(\frac12,\frac12)$，$I(0;Y)=I(2;Y)=1$、$I(1;Y)=0\le1$，KKT 成立，所以 $C=1$ bit。

【課本補充】**Example 4.26**：quasi-symmetric 通道可以直接驗證 uniform 輸入滿足 KKT（留作習題）。**Observation 4.28**：比 quasi-symmetric 更大的一類「T-symmetric」通道——$T(x)=I(x;Y)-\log_2|\mathcal X|$（uniform 輸入下）和 $x$ 無關——也正是 uniform 達到 capacity 的充要條件（由 KKT 直接得到）。例：$Q=\begin{bmatrix}\frac13&\frac13&\frac13\\\frac16&\frac16&\frac23\end{bmatrix}$ 是 T-symmetric 但不是 quasi-symmetric；但 T-symmetric 一般沒有簡單的 closed form。

---

## 9. 證明：微分就是 self-information

[▶ 32:18](https://youtu.be/G0hGPooSN3E?t=1938)

【口頭】先排除極端：$P_X(x)=1$、其他都 0，只能送一種，沒有變化就沒辦法帶訊息，$I=0$，不會是極值。

**Lagrange multipliers**（第 7 集的方法）：要在 $p_0+p_1+p_2=1$、$p_i\ge0$ 下 maximize $I(P_X,P_{Y|X})$。
- 好處：分布集合是 convex set，$I$ 對 $P_X$ concave，取最大值很容易。
- 把限制放進去：
$$I(P_X,P_{Y|X})+\lambda\left(\sum_xP_X(x)-1\right),$$
  現在 $p_0,p_1,p_2\in\mathbb R$ 沒有限制範圍，可以直接微分。總和本來就是 1，乘上 $\lambda$ 是 0，極值不變；最後答案是 $\lambda$ 的函數。
- 對每個 $P_X(x)$ 偏微分 = 0，解聯立方程。concave，所以符合 KKT，就是真正最好的解。

**微分的結果**：$\lambda$ 那項的偏微分就是 $\lambda$。mutual information 的偏微分（用乘積法則和 $\frac{d}{dx}\log f=\frac{f'}f$，整理後）是
$$\frac{\partial I(P_X,P_{Y|X})}{\partial P_X(x)}=I(x;Y)-\log_2e.$$

【口頭】**要記得：mutual information 對輸入分布的微分，剛好是單一輸入的 mutual information（self-information）。** Capacity 的微分是很重要的思維。
- 另一個例子：90 年代後期 Princeton 的 Sergio Verdú 等人（I-MMSE）證明：加性高斯雜訊下（輸入可以是 ±1、BPSK、QPSK，不必連續），mutual information 對傳送 power 的微分，剛好等於「收到 $y$ 對 $x$ 做 mean square error estimation」的量。以前很少人從這個角度探討。

【課本補充】課本的證明（p. 139）：$I$ 對 $P_X$ concave；在內部點最大值發生 iff 微分 = 0，在邊界（$P_X(x)=0$）iff 微分 ≤ 0。即
$$I(x;Y)=-\lambda+\log_2e\ \ (P_X(x)>0),\qquad I(x;Y)\le-\lambda+\log_2e\ \ (P_X(x)=0),$$
令 $C=-\lambda+\log_2e$ 即得 (4.5.9)。

---

## 10. KKT 的幾何意義

[▶ 40:24](https://youtu.be/G0hGPooSN3E?t=2424)

【口頭】
- 微分是斜率。橫軸調某個 $P_X(x_0)$、縱軸是 $I$，斜率就是 $I(x_0;Y)$（減一個常數）。
- 對每個 $P_X(x_0)\in[0,1]$ 都是 concave，極值出現在微分 = 0 的地方，或在邊界 $P_X(x_0)=0$（斜率 ≤ 0）。
- 不會出現在 $P_X(x_0)=1$：那時其他都是 0，$I=0$，不是極值。
- 所以：機率是 0 的那些，斜率 ≤ 0（$I(x;Y)\le C$），不會是 capacity；機率在 0 和 1 之間的那些，對應的值都是 $C$——「大家高度都一樣」。

---

## 11. 一頁速查表

**對稱性**：symmetric（列、行都重排）⇒ weakly symmetric（列重排、行和相等）⇒ quasi-symmetric（行可切成弱對稱子矩陣）。這三類 uniform 輸入都達到 capacity。

**Weakly symmetric**：$C=\log_2|\mathcal Y|-H(\text{一列})$。
- 關鍵：$H(Y|X=x)$ 對每個 $x$ 一樣 ⇒ $I=H(Y)-\text{常數}$；uniform 輸入 ⇒ $P_Y\propto$ 行和 ⇒ uniform 輸出。
- BSC：$C=1-h_b(\varepsilon)$。
- $q$-ary：$C=\log_2q+\varepsilon\log_2\frac\varepsilon{q-1}+(1-\varepsilon)\log_2(1-\varepsilon)$。

**Quasi-symmetric**：$C=\sum_ia_iC_i$，$a_i$ = $Q_i$ 的列和，$C_i$ = 正規化後子通道的 capacity。輸出不一定 uniform。
- BEC：$C=(1-\alpha)\cdot1+\alpha\cdot0=1-\alpha$。
- BSEC：$C=(1-\alpha)[1-h_b(\frac\varepsilon{1-\alpha})]$。

**KKT（Lemma 4.25）**
- $I(x;Y)=\sum_yP(y|x)\log\frac{P(y|x)}{P_Y(y)}$；$I(X;Y)=\sum P_X(x)I(x;Y)$。
- 最佳 ⟺ $I(x;Y)=C$（$P_X(x)>0$）、$\le C$（$P_X(x)=0$）。
- 關鍵：$\frac{\partial I}{\partial P_X(x)}=I(x;Y)-\log_2e$，Lagrange：$=-\lambda$。
- 例：$Q=[1,0;\frac12,\frac12;0,1]$ ⇒ $P_X^*=(\frac12,0,\frac12)$，$C=1$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| BEC capacity $1-\alpha$ | 第 20 集（polar code on BEC） |
| Capacity 和 source entropy 比較 | 第 21 集（§4.6） |
| AWGN：$\frac12\log(1+\text{SNR})$、高斯輸入最佳 | 第 24 集（§5.4） |
| KKT、water-filling | 第 25 集（§5.5 parallel Gaussian channels） |
| 用 KKT 求 rate-distortion function | 第 29 集（§6.4） |
| $I$ 對 power 的微分（I-MMSE） | 第 26 集附近（老師口頭提到） |

---

## 附：本集一句話總結

> **對稱的通道（每個輸入對雜訊的感覺都一樣）讓 uniform 輸入就是最佳，capacity 直接是 $\log|\mathcal Y|-H(\text{一列})$，BSC 是 $1-h_b(\varepsilon)$、BEC 是 $1-\alpha$；一般通道則用 KKT：被用到的每個輸入，它單獨和輸出的連動量都剛好等於 $C$。**

---

*筆記依據陳伯寧老師「消息理論」Lec19 錄影逐字稿（whisper large-v3-turbo，43:22）與 Alajaji & Chen 課本 §4.5 整理。*
