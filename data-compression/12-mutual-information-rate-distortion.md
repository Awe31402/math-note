---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 12
lecture: Lecture 12
date: 2023-11-06
video: https://youtu.be/9Fv8PlpPUCI
notes: 投影片 slide_12_2023.pdf（6 頁，只有小考）；本集主要是白板講課。《Elements of Information Theory》§2.4、§10.2–10.3（書頁 303–315）
---

# 第 12 集 · Lecture 12：互資訊、率失真函數（Mutual Information; Rate-Distortion Function） [▶ 影片](https://youtu.be/9Fv8PlpPUCI)

← 上一集：[11-lossy-compression-quantization](11-lossy-compression-quantization.md) ｜ [總目錄](README.md) ｜ 下一集：[13-gaussian-rd-transform-coding](13-gaussian-rd-transform-coding.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 12 集
> **講者**：Tsachy Weissman（Pulkit Tandon 結尾補充）
> **來源**：YouTube 錄影逐字稿（1:24:50，人工字幕 en-US）＋ 投影片 `slide_12_2023.pdf`（只有小考）＋ Cover & Thomas §2.4、§10.2–10.4。本集是白板課，公式依口述和課本重建。
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：熵、聯合熵、條件熵](#1-回顧熵聯合熵條件熵)
- [2. 互資訊](#2-互資訊)
- [3. 有損壓縮的設定](#3-有損壓縮的設定)
- [4. Shannon 的率失真定理](#4-shannon-的率失真定理)
- [5. 例 1：Bernoulli 來源、Hamming 失真](#5-例-1bernoulli-來源hamming-失真)
- [6. 例 2：高斯來源、平方誤差](#6-例-2高斯來源平方誤差)
- [7. 為什麼是 $\frac12\log\frac1D$：球體覆蓋](#7-為什麼是-frac12logfrac1d球體覆蓋)
- [8. 上一講小考（投影片）](#8-上一講小考投影片)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】[▶ 00:05](https://youtu.be/9Fv8PlpPUCI?t=5) 這週 office hour 改到週四同一時間，讓大家可以去投票。

[▶ 00:47](https://youtu.be/9Fv8PlpPUCI?t=47) 延續 Pulkit 開始的有損壓縮，講**率失真理論**和**率失真函數**：它是熵的類比和推廣。熵是無損壓縮根本極限的答案；率失真函數是**有損壓縮根本極限**的答案 [▶ 01:38](https://youtu.be/9Fv8PlpPUCI?t=98)。

| 主題 | 課本 |
|---|---|
| 熵、聯合熵、條件熵回顧 | §2.1–2.2 |
| 互資訊 | §2.4、§2.6 |
| 率失真定理 | §10.2 |
| Bernoulli、高斯的率失真函數 | §10.3 |

---

## 1. 回顧：熵、聯合熵、條件熵

### 1.1 熵

[▶ 02:12](https://youtu.be/9Fv8PlpPUCI?t=132) $X$ 是取值於有限字母集的離散隨機變數（隨機物件）[▶ 02:48](https://youtu.be/9Fv8PlpPUCI?t=168)：

$$H(X)=\sum_xP(X=x)\log_2\frac1{P(X=x)}.$$

[▶ 03:34](https://youtu.be/9Fv8PlpPUCI?t=214) 意義：資料若 iid 來自 $X$ 的分布，就算用很大的區塊、想盡辦法，最好也只能到每符號 $H(X)$ 位元。

### 1.2 聯合熵

[▶ 04:43](https://youtu.be/9Fv8PlpPUCI?t=283) $(X,Y)$ 是一對離散隨機變數：

$$H(X,Y)=\sum_{x,y}P(X=x,Y=y)\log\frac1{P(X=x,Y=y)}.$$

[▶ 05:29](https://youtu.be/9Fv8PlpPUCI?t=329) 沒什麼新的：把這一對當成**一個**隨機物件，取值在「配對」的字母集上，算它的熵。意義：資料是 iid 的配對時，最好每對 $H(X,Y)$ 位元 [▶ 06:45](https://youtu.be/9Fv8PlpPUCI?t=405)。

### 1.3 條件熵

[▶ 06:45](https://youtu.be/9Fv8PlpPUCI?t=405)

$$H(X\mid Y)=\sum_yP(Y=y)\,H(X\mid Y=y),\qquad H(X\mid Y=y)=\sum_xP(x\mid y)\log\frac1{P(x\mid y)}.$$

[▶ 09:09](https://youtu.be/9Fv8PlpPUCI?t=549) $H(\cdot)$ 雖然寫成隨機變數的函數，其實是**分布的函數**；$H(X\mid Y=y)$ 裡扮演機率質量函數的是條件分布 $P(\cdot\mid y)$ [▶ 09:46](https://youtu.be/9Fv8PlpPUCI?t=586)。[▶ 11:17](https://youtu.be/9Fv8PlpPUCI?t=677) 這些全都是**數字**，不是隨機變數（講者說他知道這個記號有時讓人混淆）。

[▶ 11:53](https://youtu.be/9Fv8PlpPUCI?t=713) 性質：**條件降低熵**，$H(X\mid Y)\le H(X)$。直覺上，知道 $Y$ 平均只會減少對 $X$ 的不確定性 [▶ 12:48](https://youtu.be/9Fv8PlpPUCI?t=768)；特定的 $y$ 可能讓你更困惑，但平均而言不會 [▶ 13:23](https://youtu.be/9Fv8PlpPUCI?t=803)。

[▶ 14:03](https://youtu.be/9Fv8PlpPUCI?t=843) 意義：若 $(X_i,Y_i)$ iid，而 $Y$ 序列是編碼器、解碼器都知道的**旁資訊**（side information），壓 $X$ 最好每符號 $H(X\mid Y)$ 位元。資訊只會有幫助，因為你總可以忽略它 [▶ 14:50](https://youtu.be/9Fv8PlpPUCI?t=890)。

---

## 2. 互資訊

### 2.1 定義

[▶ 15:32](https://youtu.be/9Fv8PlpPUCI?t=932) 今天最重要的新量：**互資訊**（mutual information）。記作 $I(X;Y)$（用分號是歷史原因，講者說他自己也不完全懂為什麼）[▶ 16:30](https://youtu.be/9Fv8PlpPUCI?t=990)。對離散隨機變數 [▶ 17:06](https://youtu.be/9Fv8PlpPUCI?t=1026)：

$$I(X;Y)\triangleq H(X)+H(Y)-H(X,Y).$$

### 2.2 其他寫法

[▶ 18:53](https://youtu.be/9Fv8PlpPUCI?t=1133) 用鏈鎖律 $H(X,Y)=H(X)+H(Y\mid X)$ [▶ 19:49](https://youtu.be/9Fv8PlpPUCI?t=1189)：

$$I(X;Y)=H(Y)-H(Y\mid X).$$

同理用 $H(X,Y)=H(Y)+H(X\mid Y)$ [▶ 20:29](https://youtu.be/9Fv8PlpPUCI?t=1229)：

$$I(X;Y)=H(X)-H(X\mid Y).$$

### 2.3 性質

1. **對稱** [▶ 20:29](https://youtu.be/9Fv8PlpPUCI?t=1229)：$I(X;Y)=I(Y;X)$。從定義看：兩個熵相加與順序無關；$H(X,Y)=H(Y,X)$，因為熵不受字母集元素重新標記或排序影響 [▶ 21:24](https://youtu.be/9Fv8PlpPUCI?t=1284)。
2. **非負** [▶ 22:06](https://youtu.be/9Fv8PlpPUCI?t=1326)：$I(X;Y)\ge0$，由 $H(X)-H(X\mid Y)$ 和條件降低熵。
3. **用相對熵表示**（講者最喜歡的寫法；可能是作業，否則等 EE376）[▶ 22:48](https://youtu.be/9Fv8PlpPUCI?t=1368)：
$$I(X;Y)=D\left(P_{X,Y}\,\|\,P_X\times P_Y\right),$$
也就是聯合分布和「各自保有邊際分布但互相獨立」的乘積分布之間的相對熵 [▶ 23:22](https://youtu.be/9Fv8PlpPUCI?t=1402)。

【課本補充】性質 3 的推導（§2.4 式 2.28–2.39 的方法）：

$$
\begin{aligned}
H(X)-H(X\mid Y)&=\sum_{x,y}P(x,y)\log\frac1{P(x)}-\sum_{x,y}P(x,y)\log\frac1{P(x\mid y)}\\
&=\sum_{x,y}P(x,y)\log\frac{P(x\mid y)}{P(x)}=\sum_{x,y}P(x,y)\log\frac{P(x,y)}{P(x)P(y)}=D\left(P_{XY}\|P_XP_Y\right).
\end{aligned}
$$

由 $D\ge0$ 也再次得到非負，等號當且僅當 $P(x,y)=P(x)P(y)$。

### 2.4 為什麼喜歡相對熵的寫法

[▶ 24:06](https://youtu.be/9Fv8PlpPUCI?t=1446)

1. **直覺**：互資訊衡量**相依程度** [▶ 24:41](https://youtu.be/9Fv8PlpPUCI?t=1481)。越相依，聯合分布離獨立的乘積分布越遠，互資訊越大；**只有獨立時互資訊才是 0** [▶ 25:19](https://youtu.be/9Fv8PlpPUCI?t=1519)。
2. **可以推廣** [▶ 25:19](https://youtu.be/9Fv8PlpPUCI?t=1519)：熵對連續隨機變數沒有意義（是無限大），但**互資訊對任何分布都有定義** [▶ 26:03](https://youtu.be/9Fv8PlpPUCI?t=1563)：離散、連續、實數、抽象函數空間、整條樣本路徑都行。因為兩個（不一定是機率質量函數的）分布之間總可以談相對熵，聯合分布和邊際乘積之間也就總有相對熵 [▶ 26:36](https://youtu.be/9Fv8PlpPUCI?t=1596)。

[▶ 27:51](https://youtu.be/9Fv8PlpPUCI?t=1671) 今天先專注在離散的情況，之後「請相信我，它能推廣到一般的、包括連續的隨機變數」。

[▶ 28:29](https://youtu.be/9Fv8PlpPUCI?t=1709) 互資訊在很多領域被當成好用的相依性度量；但更根本的是，**它回答了有損壓縮最基本的問題** [▶ 29:13](https://youtu.be/9Fv8PlpPUCI?t=1753)。

---

## 3. 有損壓縮的設定

### 3.1 編碼器、解碼器

[▶ 29:13](https://youtu.be/9Fv8PlpPUCI?t=1753) 先回顧無損的設定 [▶ 30:12](https://youtu.be/9Fv8PlpPUCI?t=1812)：

```
X1 ... Xn ──> [編碼器] ──> m 位元 ──> [解碼器] ──> Y1 ... Yn
```

- **無損**：解碼器必須還原**完全一樣**的 $X_1,\dots,X_n$ [▶ 30:59](https://youtu.be/9Fv8PlpPUCI?t=1859)。
- **有損** [▶ 31:36](https://youtu.be/9Fv8PlpPUCI?t=1896)：解碼器輸出的 $Y_1,\dots,Y_n$（重建）可以不同，但希望差不多。

### 3.2 失真

[▶ 32:10](https://youtu.be/9Fv8PlpPUCI?t=1930) 通常給一個**逐符號**的失真準則 $d(x,y)$（比較第 $i$ 個分量和第 $i$ 個重建），再取平均 [▶ 32:49](https://youtu.be/9Fv8PlpPUCI?t=1969)。資料是機率性的，所以取期望值 [▶ 33:23](https://youtu.be/9Fv8PlpPUCI?t=2003)：

$$D=\mathbb{E}\left[\frac1n\sum_{i=1}^nd(X_i,Y_i)\right]\qquad\text{（每符號期望失真）}.$$

例子 [▶ 34:06](https://youtu.be/9Fv8PlpPUCI?t=2046)：

| 失真 | 定義 | 適合 |
|---|---|---|
| **Hamming** | $d(x,y)=\mathbf 1\{x\ne y\}$：一樣就 0，不一樣就 1 [▶ 34:41](https://youtu.be/9Fv8PlpPUCI?t=2081) | 離散資料 |
| **平方誤差** | $d(x,y)=(x-y)^2$ [▶ 36:04](https://youtu.be/9Fv8PlpPUCI?t=2164) | 實數值（感測器量測） |

[▶ 36:43](https://youtu.be/9Fv8PlpPUCI?t=2203) 例：基因資料是四種鹼基，Hamming 失真很合理：「我願意偶爾錯一個鹼基，只要能比無損壓縮（要熵那麼多）少用很多位元」[▶ 37:24](https://youtu.be/9Fv8PlpPUCI?t=2244)。

### 3.3 率

[▶ 37:24](https://youtu.be/9Fv8PlpPUCI?t=2244) 和無損一樣：

$$R=\frac mn\quad\text{位元／符號}.$$

[▶ 38:52](https://youtu.be/9Fv8PlpPUCI?t=2332) 無損時（Hamming 失真 = 0），若 $X_i$ iid，最小的率是 $H(X)$。

### 3.4 問題

[▶ 39:26](https://youtu.be/9Fv8PlpPUCI?t=2366)

> **要讓失真不超過 $D$，最少需要多少率？** 記作 $R(D)$。

【課堂討論】[▶ 40:24](https://youtu.be/9Fv8PlpPUCI?t=2424) $D=0$ 時最小的率是什麼？大家齊聲：**熵**。[▶ 40:24](https://youtu.be/9Fv8PlpPUCI?t=2424) 但如果用 Hamming 失真、願意承受 $D=0.1$（重建只對 90%），應該能用**少於熵**的率 [▶ 41:13](https://youtu.be/9Fv8PlpPUCI?t=2473)。

[▶ 42:05](https://youtu.be/9Fv8PlpPUCI?t=2525) $R(D)$ 是允許**任何**方案（任意複雜、用任意大的區塊）最佳化後的最小率。

---

## 4. Shannon 的率失真定理

[▶ 42:54](https://youtu.be/9Fv8PlpPUCI?t=2574) Shannon 漂亮、精確、定量地回答了這個問題。

> **率失真定理**（iid 來源）[▶ 43:28](https://youtu.be/9Fv8PlpPUCI?t=2608)：若 $X_i$ iid $\sim X$，則
> $$R(D)=\min_{P_{Y\mid X}:\ \mathbb{E}[d(X,Y)]\le D}I(X;Y).$$

[▶ 44:11](https://youtu.be/9Fv8PlpPUCI?t=2651) 就像無損時 iid 來源的最小率是 $H(X)$，有損時是：在所有「期望失真不超過 $D$」的 $(X,Y)$ 聯合分布裡，最小化 $X$ 和重建變數 $Y$ 的互資訊。

[▶ 44:59](https://youtu.be/9Fv8PlpPUCI?t=2699) 說得更明確：$X$ 的分布是給定的，是來源的特性，你控制不了；所以這個最小化其實是在**所有條件分布 $P_{Y\mid X}$** 上進行，限制是 $\mathbb{E}[d(X,Y)]\le D$ [▶ 45:34](https://youtu.be/9Fv8PlpPUCI?t=2734)。最後 $R(D)$ 只是 $X$ 分布的泛函。

【課本補充】§10.2（書頁 306–307）定義**資訊率失真函數** $R^{(I)}(D)=\min_{p(\hat x\mid x):\sum p(x)p(\hat x\mid x)d(x,\hat x)\le D}I(X;\hat X)$，Theorem 10.2.1 證明對 iid 來源它等於（操作意義的）率失真函數。可達性在 §10.5 用隨機碼本證明，反向在 §10.4。

---

## 5. 例 1：Bernoulli 來源、Hamming 失真

### 5.1 設定與答案

[▶ 47:09](https://youtu.be/9Fv8PlpPUCI?t=2829) $X\sim\mathrm{Ber}(p)$，不失一般性 $p\le\frac12$（否則把 0、1 對調）[▶ 47:47](https://youtu.be/9Fv8PlpPUCI?t=2867)。失真用 Hamming [▶ 48:25](https://youtu.be/9Fv8PlpPUCI?t=2905)。

[▶ 48:25](https://youtu.be/9Fv8PlpPUCI?t=2905) 這是個**很小的低維最佳化問題**：重建 $Y$ 顯然也是二元的，只要最佳化一個二元變數給另一個二元變數的條件分布，最多兩個參數，還能用對稱性 [▶ 49:44](https://youtu.be/9Fv8PlpPUCI?t=2984)。算出來（細節在講義、下學季）[▶ 50:22](https://youtu.be/9Fv8PlpPUCI?t=3022)：

$$
R(D)=\begin{cases}h_2(p)-h_2(D),&0\le D\le p,\\[2pt]0,&D>p.\end{cases}
$$

$h_2(q)$ 是**二元熵函數**：$\mathrm{Ber}(q)$ 的熵，在 $q=\frac12$ 時最大為 1，對 $\frac12$ 對稱的拱形 [▶ 51:01](https://youtu.be/9Fv8PlpPUCI?t=3061)。

【課本補充】§10.3.1 Theorem 10.3.1（書頁 307–309）就是這個結果，證明分兩步：(1) 對任何滿足 $\Pr(X\ne\hat X)\le D$ 的 $\hat X$，$I(X;\hat X)=H(X)-H(X\mid\hat X)=h(p)-H(X\oplus\hat X\mid\hat X)\ge h(p)-H(X\oplus\hat X)\ge h(p)-h(D)$（$D\le\frac12$）；(2) 構造一個「反向通道」讓 $X=\hat X\oplus Z$、$Z\sim\mathrm{Ber}(D)$ 和 $\hat X$ 獨立，達到等號。

### 5.2 檢查

[▶ 52:34](https://youtu.be/9Fv8PlpPUCI?t=3154) 畫出來：

- **$D=0$** [▶ 53:07](https://youtu.be/9Fv8PlpPUCI?t=3187)：$R(0)=h_2(p)-h_2(0)=h_2(p)$，就是來源的熵（無損壓縮）[▶ 54:18](https://youtu.be/9Fv8PlpPUCI?t=3258)。✓
- **$D\ge p$** [▶ 54:18](https://youtu.be/9Fv8PlpPUCI?t=3258)：$R=0$。不用告訴我任何資訊，我直接重建成**全 0**；來源只有機率 $p$ 是 1，所以每個分量錯的機率是 $p$，期望 Hamming 失真就是 $p$ [▶ 54:53](https://youtu.be/9Fv8PlpPUCI?t=3293)。✓

### 5.3 凸性：時間分享的直線在曲線上方

[▶ 55:25](https://youtu.be/9Fv8PlpPUCI?t=3325) 這條曲線是**凸的**，這不是巧合，**所有率失真函數都是凸的**。

[▶ 56:01](https://youtu.be/9Fv8PlpPUCI?t=3361) 看中點：失真 $\frac p2$、率 $\frac{h_2(p)}2$ 這一點 [▶ 56:34](https://youtu.be/9Fv8PlpPUCI?t=3394)，為什麼一定在 $R(D)$ 上方？因為它對應一個很蠢的方案 [▶ 57:11](https://youtu.be/9Fv8PlpPUCI?t=3431)：

- **前一半資料無損描述**：要每符號 $h_2(p)$ 位元，但只有一半資料，平均下來是 $\frac{h_2(p)}2$。
- **後一半什麼都不說**，重建成全 0：失真 $p$，但只在一半資料上，平均下來 $\frac p2$ [▶ 57:46](https://youtu.be/9Fv8PlpPUCI?t=3466)。

這是在兩個端點之間做**時間分享**（time-sharing）[▶ 57:46](https://youtu.be/9Fv8PlpPUCI?t=3466)；顯然有更聰明的方法，能一路做到曲線上。

> 以下**不是逐字稿內容**，是代入數字看差距：取 $p=\frac12$。時間分享在 $D=0.25$ 要率 $0.5$；但 $R(0.25)=1-h_2(0.25)\approx1-0.811=0.189$。最佳方案只要時間分享的不到四成。

【課本補充】§10.4 Lemma 10.4.1（書頁 316）：$R(D)$ 是 $D$ 的非遞增凸函數。凸性的證明用互資訊對條件分布的凸性。

---

## 6. 例 2：高斯來源、平方誤差

### 6.1 答案

[▶ 59:06](https://youtu.be/9Fv8PlpPUCI?t=3546) $X\sim\mathcal N(0,1)$，$X_i$ iid，失真用**平方誤差** [▶ 59:45](https://youtu.be/9Fv8PlpPUCI?t=3585)。

[▶ 1:00:21](https://youtu.be/9Fv8PlpPUCI?t=3621) 「奇蹟」：這表面上是**無限維**的最佳化問題（要對實數值 $Y$ 給 $X$ 的條件密度最佳化），卻能明確解出來，而且不難，因為高斯分布和平方誤差很搭，加上一些最大熵性質（下學季講）[▶ 1:01:07](https://youtu.be/9Fv8PlpPUCI?t=3667)：

$$
R(D)=\begin{cases}\dfrac12\log_2\dfrac1D,&0<D\le1,\\[4pt]0,&D>1.\end{cases}
$$

【課本補充】§10.3.2 Theorem 10.3.2（書頁 310–311）的一般形式：$X\sim\mathcal N(0,\sigma^2)$ 時 $R(D)=\frac12\log\frac{\sigma^2}D$（$0\le D\le\sigma^2$）。

### 6.2 檢查

[▶ 1:02:11](https://youtu.be/9Fv8PlpPUCI?t=3731)

- **$D\ge1$** [▶ 1:02:55](https://youtu.be/9Fv8PlpPUCI?t=3775)：來源變異數是 1。不用任何位元，重建成全 0，期望平方誤差就是變異數 1 [▶ 1:03:36](https://youtu.be/9Fv8PlpPUCI?t=3816)。✓
- **$D\to0$** [▶ 1:04:18](https://youtu.be/9Fv8PlpPUCI?t=3858)：$R\to\infty$。連續來源的熵是無限大（上一講說過）；要越來越精細地描述，就要越來越多位元，要精確就得無限多位元 [▶ 1:04:50](https://youtu.be/9Fv8PlpPUCI?t=3890)。

### 6.3 失真率函數

[▶ 1:04:50](https://youtu.be/9Fv8PlpPUCI?t=3890) 反過來問：每符號最多 $R$ 位元時，最小失真是多少？**失真率函數**（distortion–rate function）[▶ 1:05:53](https://youtu.be/9Fv8PlpPUCI?t=3953)：

$$D(R)=2^{-2R}.$$

（由 $R=\frac12\log\frac1D$ 解出 $D$。）$R=0$ 時失真 1（變異數），每多 1 位元失真變成 $\frac14$ [▶ 1:06:33](https://youtu.be/9Fv8PlpPUCI?t=3993)。

### 6.4 和上一講的 1 位元量化比較

[▶ 1:07:06](https://youtu.be/9Fv8PlpPUCI?t=4026) Tsachy 問 Pulkit：上次 1 位元純量量化的失真算出來了嗎？Pulkit：算了碼字，沒算失真 [▶ 1:07:40](https://youtu.be/9Fv8PlpPUCI?t=4060)。

[▶ 1:08:20](https://youtu.be/9Fv8PlpPUCI?t=4100) 每個符號單獨送 1 位元正負號，是率 1 的方案，失真是某個值；而 $D(1)=2^{-2}=\frac14$ 是率 1 時**任何方案**能達到的最佳值。但要達到它得很辛苦：要用很大的資料區塊，不是逐符號送 1 位元那麼簡單 [▶ 1:08:20](https://youtu.be/9Fv8PlpPUCI?t=4100)。

> 以下**不是逐字稿內容**，是補上 Pulkit 那個方案的失真（第 11 集已算）：正負號量化、重建 $\pm\sqrt{2/\pi}$ 的 MSE 是 $1-\frac2\pi\approx0.363$，比理論最佳的 $0.25$ 多約 45%。

---

## 7. 為什麼是 $\frac12\log\frac1D$：球體覆蓋

[▶ 1:09:02](https://youtu.be/9Fv8PlpPUCI?t=4142) 給一點直覺：大區塊要怎麼努力、能好多少。

### 7.1 典型的 $n$ 元組落在一顆球裡

[▶ 1:09:42](https://youtu.be/9Fv8PlpPUCI?t=4182) 連續資料也可以談典型性，只是不數集合的元素個數，而是談**體積** [▶ 1:10:18](https://youtu.be/9Fv8PlpPUCI?t=4218)。

【課堂討論】[▶ 1:10:56](https://youtu.be/9Fv8PlpPUCI?t=4256) $X\sim\mathcal N(0,1)$，$\mathbb{E}[X^2]$ 是多少？學生答：**1**。

[▶ 1:11:35](https://youtu.be/9Fv8PlpPUCI?t=4295) 由大數法則，以高機率

$$\frac1n\sum_{i=1}^nX_i^2\approx1\quad\Longrightarrow\quad\sqrt{\sum_{i=1}^nX_i^2}\lesssim\sqrt n.$$

（要嚴謹需要 ε 之類，講者說大家不需要。）[▶ 1:12:13](https://youtu.be/9Fv8PlpPUCI?t=4333) 把實現的 $n$ 元組看成 $\mathbb{R}^n$ 裡的一點，它幾乎一定落在**半徑約 $\sqrt n$ 的 $n$ 維球**裡。

### 7.2 一個碼字能蓋住多少

[▶ 1:12:58](https://youtu.be/9Fv8PlpPUCI?t=4378) 要達到失真 $D$，必須讓典型球裡的序列都在某個重建碼字的失真 $D$ 以內。

[▶ 1:12:58](https://youtu.be/9Fv8PlpPUCI?t=4378) 先注意：用 $m$ 位元表示，等於有一個大小 $M=2^m$ 的**碼本**（可能重建的集合）[▶ 1:14:18](https://youtu.be/9Fv8PlpPUCI?t=4458)：解碼器看到一串位元，就輸出一個重建 [▶ 1:14:53](https://youtu.be/9Fv8PlpPUCI?t=4493)。

[▶ 1:15:36](https://youtu.be/9Fv8PlpPUCI?t=4536) 一個碼字 $y^n$ 能在失真 $D$ 內蓋住的序列：每符號失真 $\le D$ ⟺ $\sum(x_i-y_i)^2\le nD$ ⟺ 在以 $y^n$ 為中心、**半徑 $\sqrt{nD}$** 的球裡 [▶ 1:16:19](https://youtu.be/9Fv8PlpPUCI?t=4579)。（取平方根才是向量的長度；乘 $n$ 是因為失真是除以 $n$ 的平均 [▶ 1:16:57](https://youtu.be/9Fv8PlpPUCI?t=4617)。）

### 7.3 體積比

[▶ 1:17:42](https://youtu.be/9Fv8PlpPUCI?t=4662) 碼本至少要多大？用體積守恆的論證：至少是大球體積除以小球體積 [▶ 1:18:39](https://youtu.be/9Fv8PlpPUCI?t=4719)。$n$ 維球的體積 $=c_n\cdot r^n$（$c_n$ 只和 $n$ 有關）：

$$M\ \ge\ \frac{c_n\left(\sqrt n\right)^n}{c_n\left(\sqrt{nD}\right)^n}=\left(\frac1D\right)^{n/2}.$$

[▶ 1:20:04](https://youtu.be/9Fv8PlpPUCI?t=4804) 所以

$$R=\frac{\log_2M}{n}\ \ge\ \frac1n\cdot\frac n2\log_2\frac1D=\frac12\log_2\frac1D.$$

這就是率失真函數 [▶ 1:20:41](https://youtu.be/9Fv8PlpPUCI?t=4841)。

### 7.4 高維時覆蓋很有效率

[▶ 1:21:16](https://youtu.be/9Fv8PlpPUCI?t=4876) 體積論證說明**至少**要這麼多。在二維畫圖會覺得：用小球蓋大球一定會有很多重疊。但 **$n$ 很大時，重疊變得微不足道**，覆蓋非常有效率，碼本大小基本上不需要超過這個比值 [▶ 1:21:53](https://youtu.be/9Fv8PlpPUCI?t=4913)。

[▶ 1:22:34](https://youtu.be/9Fv8PlpPUCI?t=4954) 碼字（小球中心）怎麼選？不必太講究：**隨機選**就行，只要從一個刻劃好的分布取樣。這正是證明「最小互資訊可以達到」的方法 [▶ 1:22:34](https://youtu.be/9Fv8PlpPUCI?t=4954)。不只高斯，這個圖像對一般來源、分布、失真準則都成立 [▶ 1:23:13](https://youtu.be/9Fv8PlpPUCI?t=4993)。

> 以下**不是逐字稿內容**，是把這個圖像和 $D(R)=2^{-2R}$ 連起來：碼本有 $2^{nR}$ 個碼字，每個蓋住半徑 $\sqrt{nD}$ 的球，要蓋滿半徑 $\sqrt n$ 的球，需 $2^{nR}\ge D^{-n/2}$，即 $D\ge2^{-2R}$。所以「每多 1 位元，失真乘 $\frac14$」就是「每多 1 位元，可用的小球數乘 $2^n$、小球半徑可以縮成一半」。

### 7.5 結尾

[▶ 1:23:51](https://youtu.be/9Fv8PlpPUCI?t=5031) Pulkit 補充：上一講 notebook 有那張圖，比較實際方法的失真和最佳的 $\frac12\log\frac{\sigma^2}D$；會上傳去年的投影片，可以看簡單方案和理論極限差多少、要多做多少工 [▶ 1:23:51](https://youtu.be/9Fv8PlpPUCI?t=5031)。Tsachy：下一講開頭會再強調重點 [▶ 1:24:31](https://youtu.be/9Fv8PlpPUCI?t=5071)。

> ⚠️ 逐字稿缺字 [▶ 1:23:51](https://youtu.be/9Fv8PlpPUCI?t=5031)：字幕「which Saki was making」應為 Tsachy。

---

## 8. 上一講小考（投影片）

【投影片補充】`slide_12_2023.pdf`（課堂沒有討論，投影片附了前兩小題的答案）：$U\sim\mathrm{Unif}[0,1]$，MSE 失真。

- **1 位元純量量化器的最佳量化**：區間 $S_1=[0,0.5]$、$S_2=(0.5,1]$，重建點 $C=\{0.25,0.75\}$。
- **平均失真**：
$$D=\int_0^{0.5}(x-0.25)^2dx+\int_{0.5}^{1}(x-0.75)^2dx=2\int_0^{0.5}(x-0.25)^2dx=\frac43(0.25)^3\approx0.0208.$$

（後兩小題比較三種 2 維向量量化器、以及純量 vs. 2 維何者較好，投影片沒附答案，本筆記不寫。）

> 以下**不是逐字稿內容**，是補上積分：$\int_0^{0.5}(x-0.25)^2dx=\left[\frac{(x-0.25)^3}3\right]_0^{0.5}=\frac{(0.25)^3-(-0.25)^3}{3}=\frac{2(0.25)^3}3$，乘 2 得 $\frac43(0.25)^3=\frac1{48}$。也就是寬 $\Delta=0.5$ 的均勻量化，MSE $=\frac{\Delta^2}{12}$。

---

## 9. 一頁速查表

### 互資訊

$$I(X;Y)=H(X)+H(Y)-H(X,Y)=H(X)-H(X\mid Y)=H(Y)-H(Y\mid X)=D\left(P_{XY}\|P_XP_Y\right)$$

- 對稱、非負；$=0$ ⟺ 獨立。**關鍵一步**：$\log\frac{P(x\mid y)}{P(x)}=\log\frac{P(x,y)}{P(x)P(y)}$。
- 熵對連續變數無意義，互資訊對任何分布都有定義。

### 有損壓縮

- 失真 $D=\mathbb{E}\left[\frac1n\sum d(X_i,Y_i)\right]$；率 $R=\frac mn$。
- Hamming $d=\mathbf 1\{x\ne y\}$；平方誤差 $d=(x-y)^2$。

### 率失真定理（iid）

$$R(D)=\min_{P_{Y\mid X}:\ \mathbb{E}d(X,Y)\le D}I(X;Y)$$

- $R(0)=H(X)$（離散、Hamming）；$R(D)$ 非遞增、**凸**（時間分享 ⇒ 凸）。

### 兩個例子

| 來源 / 失真 | $R(D)$ | 端點檢查 |
|---|---|---|
| $\mathrm{Ber}(p)$，$p\le\frac12$ / Hamming | $h_2(p)-h_2(D)$，$D\le p$；否則 0 | $D=0$：熵；$D\ge p$：全猜 0 |
| $\mathcal N(0,\sigma^2)$ / 平方誤差 | $\frac12\log\frac{\sigma^2}D$，$D\le\sigma^2$；否則 0 | $D\ge\sigma^2$：全猜 0；$D\to0$：$\infty$ |

- 高斯失真率：$D(R)=\sigma^22^{-2R}$（每 1 位元失真 ×1/4）。
- 對照：1 位元正負號量化 $1-\frac2\pi\approx0.363$ vs. 最佳 $0.25$。

### 球體覆蓋直覺

典型球半徑 $\sqrt{n\sigma^2}$，每個碼字蓋半徑 $\sqrt{nD}$ ⇒ $M\ge(\sigma^2/D)^{n/2}$ ⇒ $R\ge\frac12\log\frac{\sigma^2}D$；高維時重疊可忽略，隨機碼本就能達到。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 高斯 $R(D)$、多個高斯分量的位元分配（water-filling） | 第 13 集 |
| 率失真曲線作為實際編碼器的基準 | 第 13–16 集 |
| 率 + λ × 失真的取捨 | 第 16 集學習式壓縮直接最小化 $\log\frac1{P(\hat z)}+\lambda d$ |
| 典型性、隨機碼本 | 理論；實作上用轉換編碼逼近 |

> 以上對應是依播放清單標題推估的，做到時再更新。

---

## 附：本集一句話總結

> **互資訊 $I(X;Y)=H(X)-H(X\mid Y)=D(P_{XY}\|P_XP_Y)$ 衡量相依程度，而且對連續變數也有定義。Shannon 的率失真定理說，iid 來源要達到失真 $D$ 的最小率是 $R(D)=\min_{\mathbb{E}d\le D}I(X;Y)$：Bernoulli/Hamming 是 $h_2(p)-h_2(D)$，高斯/平方誤差是 $\frac12\log\frac{\sigma^2}D$（即 $D=\sigma^22^{-2R}$）。這條凸曲線可以用高維球體覆蓋理解：大區塊時用隨機碼本就能幾乎無重疊地蓋住典型球。**

---

*筆記依據 Tsachy Weissman「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 12 錄影逐字稿（人工字幕，1:24:50）、投影片 slide_12_2023 與 Cover & Thomas《Elements of Information Theory》2nd ed. §2.4、§10.2–10.4 整理。*
