---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 28
lecture: Lec28 6.3 Rate–distortion theorem：AEP for distortion typical set、Shannon's lossy source coding theorem
date: 待補
video: https://youtu.be/is6v9Jbcc4E
notes: Alajaji & Chen §6.2 末–§6.3（pp. 225–237，Lemma 6.13–Observation 6.22）
---

# 第 28 集 · Lec28 §6.3：Rate–distortion theorem（Shannon 第三定律）[▶ 影片](https://youtu.be/is6v9Jbcc4E)

← 上一集：[27](27-lossy-compression-motivation-distortion.md) ｜ [總目錄](README.md) ｜ 下一集：[29](29-rate-distortion-calculation.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 28 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:30:05，whisper large-v3-turbo）＋ 課本 §6.2–6.3（pp. 225–237）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「i.i.d.」聽成「RID」，「distortion」聽成「dittortion／detortion／Detortion」，「rate–distortion」聽成「Ray Distortion／rate torsion」，「typical set」聽成「Typical say／tip pro say／Typical仕様」，「asymptotic equipartition」聽成「Asymthetic Equal Partition」，「convex」聽成「Comeback／comebacks」，「monotonicity」聽成「monotality」，「stationary ergodic」聽成「Station Ergotic／Stationary Ergotic」，「大數法則」聽成「大樹法則／大術法則」，「fundamental inequality」聽成「fundamental equality／Fundamental Inquality」，「indicator function」聽成「indicator function（斷字）」，「Shannon」聽成「Shanon／Shanen／宣人／學能」，「codeword」聽成「Codework／co-work／扣握」，「codebook」聽成「co-book」，「epsilon」聽成「absent」，「three-delta」正確。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：為什麼 R(D) 是 min I(Z;Ẑ)](#1-複習為什麼-rd-是-min-izẑ)
- [2. Time sharing：R(D) 是 convex](#2-time-sharingrd-是-convex)
- [3. Distortion typical set：多了第四個條件](#3-distortion-typical-set多了第四個條件)
- [4. 三個條件其實是一個：information density](#4-三個條件其實是一個information-density)
- [5. 自己造一個不等式：Lemma 6.19](#5-自己造一個不等式lemma-619)
- [6. Theorem 6.20 的敘述](#6-theorem-620-的敘述)
- [7. Achievability：random coding](#7-achievabilityrandom-coding)
- [8. R⁽ᴵ⁾(D) 的性質與 D_max](#8-rᴵd-的性質與-d_max)
- [9. Converse](#9-converse)
- [10. 總結與 stationary ergodic 的推廣](#10-總結與-stationary-ergodic-的推廣)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】今天把第一部分做一個總結，之後進第二部分（近年的重要觀念延伸）。

本集證明 **Shannon 的 rate–distortion theorem**（第三定律）：操作上的 $R(D)$ 等於純數學的 $R^{(I)}(D)=\min I(Z;\hat Z)$。沿途講 time-sharing（$R(D)$ convex）、**distortion typical set**（多一個條件）、老師對 typical set 的另一個定義（**information density**）、證明用的不等式 $(1-xy)^n\le1-x+e^{-yn}$ 是怎麼「造」出來的。

| 主題 | 課本 |
|---|---|
| Time-sharing、$R(D)$ 的定義與性質 | Lemma 6.13、Definition 6.14、Observation 6.15（pp. 225–227） |
| Distortion typical set、AEP | Definition 6.16、Theorem 6.17–6.18（pp. 227–229） |
| 不等式 | Lemma 6.19（p. 229） |
| Rate–distortion theorem（memoryless） | Theorem 6.20（pp. 229–234） |
| Stationary ergodic | Theorem 6.21、Observation 6.22（pp. 235–237） |

---

## 1. 複習：為什麼 R(D) 是 min I(Z;Ẑ)

[▶ 00:30](https://youtu.be/is6v9Jbcc4E?t=30)

- Source $Z_1,Z_2,\dots$ i.i.d.（每次觀察獨立、同分布），entropy rate 就是 $H(Z)$。資料量太大、capacity 太小，要壓成 $\hat Z_1,\hat Z_2,\dots$（每 $n$ 個壓一次）；壓縮後的平均資訊量比原來小，由 lossless source coding theorem，一定有資料損失 ⇒ 有 distortion。
- Distortion 越小 rate 越大，是 trade-off。
- 精神：**additive** distortion，整體是個別的和；除以 $n$ 就有大數法則。

**Venn 圖的出發點**：$\hat Z$ 是壓縮的結果，它的資訊量包含在 $Z$ 裡面——沒有「$\hat Z$ 知道、$Z$ 不知道」的那一塊（傳輸時有兩圈交錯，壓縮時沒有）。所以
$$H(\hat Z^n)=I(Z^n;\hat Z^n),$$
rate 就是 $\frac1nI(Z^n;\hat Z^n)$。Shannon 的公式：
$$R(D)=\min_{P_{\hat Z|Z}:\ E[\rho(Z,\hat Z)]\le D}I(Z;\hat Z).$$
- 和原題目一樣：讓壓縮後的資訊量越小越好，但 distortion 不能超過 $D$。
- $I$ 是「輸入分布」和「條件分布」的函數；輸入 $P_Z$ 固定，能改的是**壓縮方法** $P_{\hat Z|Z}$——可以是統計式的（看到 1，擲骰子 70% 變 1、30% 變 2）。

**操作量 vs. 數學量**【口頭】：$R(D)$ 是**操作的量**（真的去壓一張畫面，得到 rate 和 distortion）；$R^{(I)}(D)$ 是**純數學的量**（給機率就算得出來）。最後證明兩者相等——又回到 Shannon 最早的想法：先用純數學定義一個量，證明它就是操作上的量。好處和 entropy 一樣：你的方法接近這條曲線，就知道不用再改善了。

---

## 2. Time sharing：R(D) 是 convex

[▶ 08:41](https://youtu.be/is6v9Jbcc4E?t=521)

**Lemma 6.13（time-sharing principle）**（p. 225）：additive distortion 下，rate–distortion region 是 convex。
- 【口頭】有方法達到 $(R_1,D_1)$（例如壓到 30%）、另一個達到 $(R_2,D_2)$（壓到 40%），兩點的連線都做得到：30% 的時間用方法 1、70% 用方法 2。
- 要 **minimize** rate，實際曲線一定比連線更好 ⇒ $R(D)$ 是 **convex**。（對照：capacity 是 maximize，所以是 concave。）
- 【口頭】工程上碰到很多操作函數，都可以用 time-sharing 去 argue 它是 concave 還是 convex（看是 max 還是 min）。

**為什麼要有理數**【口頭】：長度 $n$ 再大也是整數。取 $\lambda=\frac r{r+s}$（$r,s$ 正整數），總長度 $(r+s)n$，前 $rn$ 個用 $h_1$、後 $sn$ 個用 $h_2$——例如 $\lambda=0.3$、長度 1000，前 300 個用方法 1、後 700 個用方法 2。$\lambda$ 是無理數（例如 $\frac{\sqrt2}2=0.71\dots$）就不知道怎麼分，用有理數去逼近。Rate 和 distortion 都是個別的加權和，就證完了。

**Definition 6.14**：$R(D)=\min\{R:(R,D)\in\mathcal R\}$。
**Observation 6.15**：$R(D)$ 非遞增（要求越寬鬆，rate 可以越低）、convex；$R(0)$ 對應 lossless，就是 entropy（第一定律已證）。

---

## 3. Distortion typical set：多了第四個條件

[▶ 17:27](https://youtu.be/is6v9Jbcc4E?t=1047)

循著 Shannon 的脈絡：只壓縮**會發生**的對象（例如全部是 0 的序列機率很低，壓得好不好都不影響）⇒ 找 typical set。

**Definition 6.16（distortion δ-typical set）**（p. 227）：$(z^n,\hat z^n)$ 依 $P_{Z,\hat Z}$ i.i.d.，bounded additive distortion，
$$\begin{aligned}
D_n(\delta):=\Big\{(z^n,\hat z^n):\ &\left|-\tfrac1n\log_2P_{Z^n}(z^n)-H(Z)\right|<\delta,\\
&\left|-\tfrac1n\log_2P_{\hat Z^n}(\hat z^n)-H(\hat Z)\right|<\delta,\\
&\left|-\tfrac1n\log_2P_{Z^n\hat Z^n}(z^n,\hat z^n)-H(Z,\hat Z)\right|<\delta,\\
&\left|\tfrac1n\rho_n(z^n,\hat z^n)-E[\rho(Z,\hat Z)]\right|<\delta\Big\}.
\end{aligned}$$
前三個和 channel coding 的 jointly typical set 一樣，**第四個是新的**：平均 distortion 要接近期望值。$\frac1n\rho_n=\frac1n\sum\rho(z_i,\hat z_i)$ 是很多量的平均 ⇒ 大數法則保證收斂。

**為什麼要 bounded**【口頭】[▶ 22:05](https://youtu.be/is6v9Jbcc4E?t=1325)：若某個 $\rho(z,\hat z)=\infty$（例如 1 用 4 代表感覺無限大），平均裡有一項無限大，平均就是無限大、不會收斂。但真正需要的是**收斂**：只要衝到很大的機率不大、在機率上還收斂到期望值就行。例如 squared error $(z-\hat z)^2$ 沒有上界，但仍可以用。所以重點不是 i.i.d.，而是**大數法則**——這是做 data analytics 的重要概念。

【口頭】順帶：社會科學的民調，每家媒體的支持度不一樣（20%、30%），如果系統只是 stationary，每個都「對」；non-stationary 更糟。我們需要的是每個人量都收斂到同一個期望值。

**Theorem 6.18（AEP for distortion measure）**（p. 228）：
1. $n$ 夠大時 $P_{Z^n\hat Z^n}(D_n^c(\delta))<\delta$；
2. 對所有 $(z^n,\hat z^n)\in D_n(\delta)$：
$$P_{\hat Z^n}(\hat z^n)\ge P_{\hat Z^n|Z^n}(\hat z^n|z^n)\,2^{-n[I(Z;\hat Z)+3\delta]}.\qquad(6.3.1)$$

---

## 4. 三個條件其實是一個：information density

[▶ 25:08](https://youtu.be/is6v9Jbcc4E?t=1508)

【口頭】所有書的 typical set 都這樣定義；老師提供另一個定義（其他書不會這樣講），和第二部分有關。

把 (6.3.1) 移項、取 $\log_2$、除以 $n$：
$$\frac1n\log_2\frac{P_{\hat Z^n|Z^n}(\hat z^n|z^n)}{P_{\hat Z^n}(\hat z^n)}\le I(Z;\hat Z)+3\delta.$$
（另一邊 $\ge I-3\delta$ 也成立，只是證明用不到。）所以可以**直接**定義
$$\left|\frac1n\log_2\frac{P_{Z^n\hat Z^n}(z^n,\hat z^n)}{P_{Z^n}(z^n)P_{\hat Z^n}(\hat z^n)}-I(Z;\hat Z)\right|\le3\delta$$
為 typical set——後面的證明全部對。

**為什麼原本要三個條件**：
$$\log\frac{P_{Z\hat Z}}{P_ZP_{\hat Z}}=\log P_{Z\hat Z}-\log P_Z-\log P_{\hat Z},$$
第三個條件（joint）、第一個（輸入 $Z$）、第二個（輸出 $\hat Z$）各管一項，合起來就是 $I=H(Z)+H(\hat Z)-H(Z,\hat Z)$。Shannon 最早只用三大公設定義 entropy，所以分開寫；**真正需要的只有一個條件**——channel capacity 的證明也一樣（把 $Z,\hat Z$ 換成 $X,Y$）。i.i.d. 時這個量是個別項的和，除以 $n$，由大數法則收斂到 $I$。

**AEP 的精神：兩邊都要**：在集合裡每個元素的這個量幾乎一樣大（都 $\approx I$），「票票等值」，不能丟掉任何一個；若裡面有人多有人少，就還可以忽略一些。所以證明只用右半邊，但觀念上兩邊都需要。

**Information density**【口頭】[▶ 33:53](https://youtu.be/is6v9Jbcc4E?t=2033)：
$$\frac1n\log_2\frac{P_{Z^n\hat Z^n}(z^n,\hat z^n)}{P_{Z^n}(z^n)P_{\hat Z^n}(\hat z^n)}$$
在 90 年代之後有專有名詞叫 **information density**。若沒有大數法則（只有 stationary，甚至 non-stationary、time-varying），它**不會收斂**到期望值，而是一個隨機變數、有一個分布（第一次量 0.2、第二次 0.3……）。這個分布才是最該分析的量：知道它，就知道這個體系怎麼壓縮、怎麼傳輸、極限在哪裡——這是**第二部分**的重點。Non-stationary source 的 $\frac1n\log P(X^n)$ 不再是平均（不能拆成很多量的和），但只要知道它的機率分布就夠了。

---

## 5. 自己造一個不等式：Lemma 6.19

[▶ 37:56](https://youtu.be/is6v9Jbcc4E?t=2276)

**Lemma 6.19**（p. 229）：$0\le x,y\le1$、$n>0$，
$$(1-xy)^n\le1-x+e^{-yn},$$
等號 iff $(x,y)=(1,0)$。

【口頭】**怎麼創造你需要的不等式**——一定有目的：
- 像 fundamental inequality 一樣，要把麻煩的東西（log、$n$ 次方）拿掉，右邊變成**線性**（不會要 $x^2$，那對我們沒用），而且 $x$ 前面沒有係數——因為 $x$ 將來是機率，$1-x$ 減起來才會出現「機率和 = 1」的結果。
- 但 $(1-xy)^n\le1-x$ 是**錯的**：$1-x$ 是斜率 −1 的直線（$x=0$ 時 1、$x=1$ 時 0）；$(1-xy)^n$ 是凹進去的曲線，中間在直線下面，兩端會翹起來。檢查：$x=0$ 時 $1\le1$ 對；$x=1$ 時 $(1-y)^n\le0$ 錯。
- 修正：把直線往外移一點點，補上 $x=1$ 時的差距 $(1-y)^n$：$(1-xy)^n\le1-x+(1-y)^n$。
- 再用 fundamental inequality $1-y\le e^{-y}$（兩邊取 log 就是它），$(1-y)^n\le e^{-ny}$。修正量 $e^{-ny}$ 夠小：$y>0$、$n$ 很大就不見了。
- 嚴格證明用微積分（課本取 $g_y(t)=(1-yt)^n$ 的二次微分）。

---

## 6. Theorem 6.20 的敘述

[▶ 43:09](https://youtu.be/is6v9Jbcc4E?t=2589)

**Theorem 6.20（Shannon's rate–distortion theorem for memoryless sources）**（p. 229）：DMS，additive 且 **bounded**（$\rho_{\max}:=\max\rho(z,\hat z)<\infty$）的 distortion，
$$R(D)=\min_{P_{\hat Z|Z}:\ E[\rho(Z,\hat Z)]\le D}I(Z;\hat Z).$$
- 右邊叫 **(Shannon's) information rate–distortion function** $R^{(I)}(D)$，純數學（給 $P_Z$ 就算得出來，不知道怎麼設計）；左邊叫 operational rate–distortion function。
- **Min 一定存在**：$I$ 對條件分布 $P_{\hat Z|Z}$ 是 **convex**（對 $P_Z$ 是 concave）——好像上帝很巧妙的安排；convex function 取最小很棒。
- 【口頭】1948 年就有這個量，大概到 1990 年之後才找到真正達到極限的方法。

**證明策略**【口頭】：直接證 $x=y$ 在 information theory 很難，所以證 $x\le y+\varepsilon$ 和 $x\ge y-\varepsilon$。加 $\varepsilon$ 的目的：有 $\varepsilon$ 才能定義 $\delta$，有 $\delta$ 才能定義 typical set（typical set 不嚴格、是大約的、asymptotic 的）。$\varepsilon$ 任意小都對，就得到等號。

---

## 7. Achievability：random coding

[▶ 47:48](https://youtu.be/is6v9Jbcc4E?t=2868)

**要證**：$R(D+\varepsilon)\le R^{(I)}(D)+4\varepsilon$——存在一個方法，distortion 多一點點、rate 也多一點點。

**設定**：
- 令 $P_{\tilde Z|Z}$ 是達到 $R^{(I)}(D)$ 的條件分布（數學上存在），$E[\rho(Z,\tilde Z)]\le D$。由它算出輸出端分布 $P_{\tilde Z}$。
- 選 $M_n$ 使 $\frac1n\log_2M_n$ 在 $R^{(I)}(D)$ 附近，比它大一點（課本取的常數：$\frac\gamma2$、$4\varepsilon$；【口頭】這些數字不重要，4 只是因為後面會有 4 項小量相加）。
- $\delta$ 再取小一點——看到 $\delta$ 就知道是要做 typical set。

**Random coding argument**【口頭】：Shannon 發明的「辯證法」——不知道怎麼設計，就隨機選。
- 例：$n=3$，$Z^n$ 有 8 種可能；$M_n=4$，只選 4 個代表值（壓到 2 bit；原本 3 bit），例如 000、001、100、011——用 $P_{\tilde Z}$ **獨立地**挑 $M_n$ 個 codeword $c_1,\dots,c_{M_n}$（可以重複，重複就是很爛的碼）。
- 【口頭】$n$ 夠大時，隨便挑的大部分設計都還不錯——期望值好（全班平均 90 分，大部分同學都考得不錯）。但要打得夠亂、散得夠開。

**編碼規則**：令 $T(\mathcal C_n)$ = 和某個 codeword distortion-typical 的 $z^n$ 的集合（有「強連結」的）。
- $z^n$ 若和某個 codeword $c$ 是 typical pair，就壓成 $c$（例如 000 壓到 000）；
- 和兩個以上 typical：隨便挑一個（可以隨機，例如各 $\frac12$）；
- 和誰都不 typical：亂壓，反正機率很低，不影響效能。

**算「沒被涵蓋」的機率的期望值**（對所有 codebook 平均）：
- 【口頭】Summation 對調：$\sum_{\mathcal C}P(\mathcal C)\sum_{z^n\notin T(\mathcal C)}P(z^n)=\sum_{z^n}P(z^n)\sum_{\mathcal C:\,z^n\notin T(\mathcal C)}P(\mathcal C)$——就像 $\sum_x\sum_{y\ge x}=\sum_y\sum_{x\le y}$，條件一樣、順序對調。
- 對固定的 $z^n$，裡面是「挑的 $M_n$ 個 codeword **都不**和 $z^n$ typical」的機率。每個獨立挑，所以是 $M_n$ 次方：例如 8 個裡有 2 個和它 typical，每次只能從另外 6 個挑，機率 $\left(\frac68\right)^4$ 這種形式。
- 用 indicator $K(z^n,\hat z^n)$（typical 為 1，否則 0）：
$$\Pr[\text{每個都不 typical}]=\left(1-\sum_{\hat z^n}P_{\tilde Z^n}(\hat z^n)K(z^n,\hat z^n)\right)^{M_n}.$$
- **用 (6.3.1)** 把獨立的 $P_{\tilde Z^n}$ 換成 dependent 的條件機率（差一個常數 $2^{-n(I+3\delta)}$）：
$$\le\left(1-2^{-n(I(Z;\tilde Z)+3\delta)}\sum_{\hat z^n}P_{\tilde Z^n|Z^n}(\hat z^n|z^n)K(z^n,\hat z^n)\right)^{M_n}.$$
- **用 Lemma 6.19**，$x=\sum P_{\tilde Z^n|Z^n}K$（一個機率）、$y=2^{-n(I+3\delta)}$：
$$\le1-\sum_{\hat z^n}P_{\tilde Z^n|Z^n}(\hat z^n|z^n)K(z^n,\hat z^n)+\exp\left(-M_n2^{-n(I(Z;\tilde Z)+3\delta)}\right).$$
- 指數項：$M_n\approx2^{n(R^{(I)}+\text{一點})}$ 比 $2^{n(I+3\delta)}$ 大（$\delta$ 取得夠小），所以 $M_n2^{-n(I+3\delta)}\to\infty$，$e^{-(\cdot)}\to0$。
- 對 $z^n$ 平均，前兩項變成 $1-P_{Z^n\tilde Z^n}(D_n(\delta))=P(D_n^c)<\delta$。
- 所以期望值 $<2\delta$ ⇒ **一定存在**一個 codebook，沒被涵蓋的機率 $<2\delta$。【口頭】那個挑法要經過好幾十年才發現；Shannon 用 random coding argument 證明存在性。

**Distortion**：對這個存在的 $h_n$，
- 在 $T$ 裡：第四個條件保證 $\frac1n\rho_n\le E[\rho(Z,\tilde Z)]+\delta\le D+\delta$；
- 在 $T$ 外：最多 $\rho_{\max}$，機率 $<2\delta$；
- 所以 $E\left[\frac1n\rho_n\right]\le D+\delta+2\delta\rho_{\max}\le D+\varepsilon$（$\delta$ 取得比 $\varepsilon$ 小）。
- 【口頭】這就是為什麼要多一個 $\delta$：$E[\rho]\le D$ 是我們故意挑的分布，加 $\delta$ 之後仍 $\le D+\varepsilon$，符合條件。

---

## 8. R⁽ᴵ⁾(D) 的性質與 D_max

[▶ 70:19](https://youtu.be/is6v9Jbcc4E?t=4219)

**$R^{(I)}(D)$ 是 convex**（用數學證，不是操作）：
- 【口頭】前面用 time-sharing 證的是**操作量** $R(D)$ convex；$R^{(I)}$ 是純數學的量，還沒證（最後兩者相等，所以它一定要 convex）。
- 取達到 $(D_1,R^{(I)}(D_1))$、$(D_2,R^{(I)}(D_2))$ 的條件分布 $P_1$、$P_2$，令 $P_\lambda=\lambda P_1+(1-\lambda)P_2$，distortion 是 $\lambda D_1+(1-\lambda)D_2$。
$$R^{(I)}(\lambda D_1+(1-\lambda)D_2)\le I(P_Z,P_\lambda)\le\lambda I(P_Z,P_1)+(1-\lambda)I(P_Z,P_2)=\lambda R^{(I)}(D_1)+(1-\lambda)R^{(I)}(D_2).$$
  第一步：min 比任何一個都小；第二步：$I$ 對條件分布 convex。
- 數學上也是非遞增（限制越鬆，min 越小）；convex + 單調 ⇒ 連續。

**什麼時候 $R^{(I)}(D)=0$**（$D\ge D_{\max}$）：
- 【口頭】什麼都不用送：輸出端自己隨機亂產生，和輸入**獨立**，$P_{Z\hat Z}=P_ZP_{\hat Z}$，$I=0$。若這樣的 distortion 還滿足要求，rate 就是 0。你送一個畫面，我隨便產生另一個畫面，distortion 還符合要求，根本不用送。
- 在所有獨立的情形中找最好的 $P_{\hat Z}$：
$$D_{\max}:=\min_{P_{\hat Z}}\sum_{\hat z}P_{\hat Z}(\hat z)\sum_zP_Z(z)\rho(z,\hat z)=\min_{\hat z}E[\rho(Z,\hat z)].$$
  把機率全部放在讓 $E[\rho(Z,\hat z)]$ 最小的那個 $\hat z$（例如四個值 0.3、0.2、0.1……，就全部放在最小的那個）。
- 所以有意義的情形是 $D<D_{\max}$。

---

## 9. Converse

[▶ 79:29](https://youtu.be/is6v9Jbcc4E?t=4769)

**要證**：對所有設計，$R(D+\varepsilon)\ge R^{(I)}(D+\varepsilon)$——rate 若比數學量小，distortion 就一定比較大。（$R^{(I)}=0$ 時不用證，rate 本來就 $\ge0$。）

對任何 $(n,M_n,D+\varepsilon)$ 碼 $h_n$，$\hat Z^n=h_n(Z^n)$：
$$\begin{aligned}
\log_2M_n&\ge H(\hat Z^n)&&(\text{只有 }M_n\text{ 種可能；uniform 才等號})\\
&=H(\hat Z^n)-H(\hat Z^n|Z^n)=I(Z^n;\hat Z^n)&&(h_n\text{ 是函數，}H(\hat Z^n|Z^n)=0)\\
&=H(Z^n)-H(Z^n|\hat Z^n)\\
&=\sum_iH(Z_i)-\sum_iH(Z_i|Z^{i-1},\hat Z^n)&&(\text{i.i.d.；chain rule})\\
&\ge\sum_i\left[H(Z_i)-H(Z_i|\hat Z_i)\right]=\sum_iI(Z_i;\hat Z_i)&&(\text{條件少，entropy 不會變小})\\
&\ge\sum_iR^{(I)}(D_i)&&(D_i:=E[\rho(Z_i,\hat Z_i)]\text{；}R^{(I)}\text{ 是 min})\\
&\ge nR^{(I)}\left(\tfrac1n\textstyle\sum_iD_i\right)&&(R^{(I)}\text{ convex，Jensen})\\
&\ge nR^{(I)}(D+\varepsilon)&&(\tfrac1n\textstyle\sum D_i\le D+\varepsilon\text{，}R^{(I)}\text{ 非遞增}).
\end{aligned}$$

【口頭】
- **好的壓縮，壓完之後很像 uniform**；不是 uniform 就還可以再壓（所以第一步通常不是等號）。
- 第二步就是那張 Venn 圖：原本要看的是壓縮後的 entropy，但轉成壓縮前後的 **mutual information** 比較好做。補上 $H(\hat Z^n|Z^n)=0$，加 0 減 0 不變。
- 對照資料傳輸：$I(X;Y)=h(Y)-h(Z)$，雜訊 $h(Z)$ 固定，要讓輸出越豐富越好；這裡反過來，$H(Z^n)$ 固定（資料量太大一定要壓），扣掉的 $H(Z^n|\hat Z^n)$ 是「看到輸出仍不了解輸入」的部分——在 distortion 限制下，要讓它扣得越多越好。
- 整個證明沒有牽涉到任何方法，所以對所有方法都對（universal）。
- 嚴格遞減的用法：若 $R^{(I)}(D_1)>R^{(I)}(D_2)$ 則 $D_1<D_2$——rate 比數學量小，distortion 就一定比較大。

---

## 10. 總結與 stationary ergodic 的推廣

[▶ 86:39](https://youtu.be/is6v9Jbcc4E?t=5199)

- 操作上可達的有損壓縮量，可以用數學量 mutual information 得到。
- **Bounded 的條件可以放寬**：squared error 沒有上界，但真正需要的是「固定輸出 $\hat z$，$E[\rho(Z,\hat z)]$ 有限」，所以 squared error 還能用——高斯 source 可以算（下一集）。
- 第一部分的整理：source coding theorem（entropy typical set）、channel coding theorem（capacity）、rate–distortion theorem——都靠 **typical set** 和 **random coding argument**（不會設計，就算隨機挑的期望值）。

**Theorem 6.21（stationary ergodic source）**（p. 235）：$R(D)=\lim_{n\to\infty}R_n^{(I)}(D)$，
$$R_n^{(I)}(D):=\min_{P_{\hat Z^n|Z^n}:\ \frac1nE[\rho_n(Z^n,\hat Z^n)]\le D}\frac1nI(Z^n;\hat Z^n).$$
大數法則對、typical set 也對，所以很容易延伸；差別只是要看 $n$ 個對 $n$ 個的 mutual information 和 distortion。

【口頭】90 年代的延伸（下一部分）：沒有大數法則就沒有 typical set；這時重點是 information density 的**分布**。Typical set 會有結構性的變化：裡面的元素不再等重，有的多有的少（non-stationary 的情形），機率高的要多關注一點。

---

## 11. 一頁速查表

**Rate–distortion theorem（Thm 6.20）**：bounded additive distortion 的 DMS，
$$R(D)=R^{(I)}(D)=\min_{P_{\hat Z|Z}:\,E\rho(Z,\hat Z)\le D}I(Z;\hat Z).$$
- 直覺：$\hat Z=h(Z)$ ⇒ $H(\hat Z)=I(Z;\hat Z)$。
- $R(D)$ convex（time-sharing）；$R^{(I)}$ convex（$I$ 對 $P_{\hat Z|Z}$ convex）、非遞增；$D\ge D_{\max}=\min_{\hat z}E\rho(Z,\hat z)$ 時 $=0$。

**Distortion typical set**：三個 entropy 條件 + $\left|\frac1n\rho_n-E\rho\right|<\delta$。三個 entropy 條件可合成一個：$\left|\frac1n\log\frac{P(z^n,\hat z^n)}{P(z^n)P(\hat z^n)}-I\right|\le3\delta$（information density）。
- AEP：$P(D_n^c)<\delta$；$P_{\hat Z^n}(\hat z^n)\ge P_{\hat Z^n|Z^n}(\hat z^n|z^n)2^{-n(I+3\delta)}$。

**Lemma 6.19**：$(1-xy)^n\le1-x+e^{-yn}$（直線 $1-x$ 往外移，補 $(1-y)^n\le e^{-ny}$）。

**Achievability**：用 $P_{\tilde Z}$ 隨機挑 $M_n\approx2^{n(R^{(I)}+\cdot)}$ 個 codeword；$E[\Pr(\text{沒被涵蓋})]\le P(D_n^c)+\exp(-M_n2^{-n(I+3\delta)})<2\delta$；distortion $\le D+\delta+2\delta\rho_{\max}$。

**Converse**：$\log M_n\ge H(\hat Z^n)=I(Z^n;\hat Z^n)\ge\sum I(Z_i;\hat Z_i)\ge\sum R^{(I)}(D_i)\ge nR^{(I)}(\frac1n\sum D_i)$。

**Stationary ergodic（Thm 6.21）**：$R(D)=\lim\frac1n\min I(Z^n;\hat Z^n)$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 計算 $R(D)$：二元 source（Hamming）、高斯 source（squared error） | 第 29 集（§6.4） |
| $rR(D)<C$：有損的 joint source–channel coding | 第 30 集（§6.5） |
| Information density 的分布、沒有大數法則時的壓縮 | 第 32–34 集（第二部分） |

---

## 附：本集一句話總結

> **因為壓縮結果是原資料的函數，rate 就是 $I(Z;\hat Z)$，所以 Shannon 第三定律說最小 rate $R(D)=\min_{E\rho\le D}I(Z;\hat Z)$：可達性靠隨機挑 codeword、多一個「平均 distortion 接近期望值」的 typical 條件、以及為此量身打造的不等式 $(1-xy)^n\le1-x+e^{-yn}$；反向靠 Venn 圖把 entropy 換成 mutual information，再用 convexity 收尾。**

---

*筆記依據陳伯寧老師「消息理論」Lec28 錄影逐字稿（whisper large-v3-turbo，1:30:05）與 Alajaji & Chen 課本 §6.2–6.3 整理。*
