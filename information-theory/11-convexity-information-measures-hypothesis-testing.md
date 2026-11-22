---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 11
lecture: Lec11 2.7 Convexity/concavity of information measures, 2.8 Fundamentals of hypothesis testing
date: 待補
video: https://youtu.be/Zc6oi3LwKtg
notes: Alajaji & Chen §2.6 末（Lemma 2.44、Corollary 2.45）、§2.7（Lemma 2.46）、§2.8（Lemma 2.48–2.49，pp. 40–45）、§2.9（Definition 2.50–2.51）
---

# 第 11 集 · Lec11 §2.7–2.8：資訊量的凸性、Neyman–Pearson、Chernoff–Stein lemma [▶ 影片](https://youtu.be/Zc6oi3LwKtg)

← 上一集：[10](10-divergence-variational-distance.md) ｜ [總目錄](README.md) ｜ 下一集：[12](12-lossless-data-compression-principles-aep.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 11 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（44:51，whisper large-v3-turbo）＋ 課本 §2.7–2.9（pp. 36–46）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「量度」聽成「良度」，「convex set」聽成「comvac set／comeback set」，「concave」聽成「concade／con-K」，「convex」聽成「combex／comebacks」，「lossy」聽成「Lawsey」，「Venn 圖」聽成「文式圖」，「Kullback–Leibler」聽成「Coolback Library／Liber」，「null hypothesis」聽成「now hypothesis」，「Bayesian」聽成「Basian」，「Neyman–Pearson」聽成「Newman-Pearson／Newman PSNA」，「false alarm」聽成「Force Alarm」，「likelihood ratio」聽成「likely ratio／Likethood Ratio」，「Chernoff」聽成「Chernel／churnoff／churn of」，「criterion」聽成「quiterion」，「Rényi」聽成「Rhenie／Rinear」，「Shannon」聽成「Shanan」，「ε」聽成「Epson」，「clustering point」聽成「classing point」，「擒賊先擒王」聽成「勤賊先勤王」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Entropy 是 concave](#1-entropy-是-concave)
- [2. Mutual information：對輸入 concave、對通道 convex](#2-mutual-information對輸入-concave對通道-convex)
- [3. Shannon 的小故事](#3-shannon-的小故事)
- [4. Divergence 是 convex](#4-divergence-是-convex)
- [5. Hypothesis testing 的設定](#5-hypothesis-testing-的設定)
- [6. Bayesian vs Neyman–Pearson](#6-bayesian-vs-neymanpearson)
- [7. Neyman–Pearson lemma](#7-neymanpearson-lemma)
- [8. Chernoff–Stein lemma](#8-chernoffstein-lemma)
- [9. 證明：forward part（divergence typical set）](#9-證明forward-partdivergence-typical-set)
- [10. 證明：converse part（交集的論證）](#10-證明converse-part交集的論證)
- [11. 第 2 章總結：其他 information measures](#11-第-2-章總結其他-information-measures)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

1. **§2.7**：entropy、mutual information、divergence 對分布的 convex／concave 性質——之後要對它們取極值，而它們剛好都有好的凸性，Shannon 的三大定律都用到。
2. **§2.8**：hypothesis testing。Neyman–Pearson lemma 說 likelihood ratio test 最好；**Chernoff–Stein lemma**（老師稱「Shannon 三大定律之外的第四個定律」）說 type II 錯誤率以 $2^{-nD}$ 衰減，確認 divergence 的操作意義。

| 主題 | 課本 |
|---|---|
| 獨立 side information、divergence 可加 | Lemma 2.44、Corollary 2.45（p. 36） |
| 凸性 | §2.7 Lemma 2.46（pp. 37–40） |
| Hypothesis testing、Neyman–Pearson | §2.8、Lemma 2.48（pp. 40–43） |
| Chernoff–Stein | Lemma 2.49（pp. 43–45） |
| Rényi 資訊量 | §2.9 Definition 2.50–2.51（pp. 45–46） |

---

## 1. Entropy 是 concave

[▶ 00:00](https://youtu.be/Zc6oi3LwKtg?t=0)

- 三元分布 $(p_0,p_1,p_2)$：$p_i\ge0$、總和 1。這個集合在三維空間是 **convex set**（任兩點的線性組合仍在集合裡）。
- 在這個 convex set 上，$H$ 是 $(p,q,r)$ 的函數，而且是 **concave**。

**Lemma 2.46 (1)**（p. 37）：
$$H\left(\lambda P_X+(1-\lambda)P_{X'}\right)\ge\lambda H(P_X)+(1-\lambda)H(P_{X'}),\quad\lambda\in[0,1].$$
（兩個分布做 weighted sum 還是分布；先混合再算 entropy ≥ 先算再混合。）

【課本補充】證明（log-sum，p. 37）：左減右等於
$$\lambda\sum_xP_X(x)\log_2\frac{P_X(x)}{\lambda P_X(x)+(1-\lambda)P_{X'}(x)}+(1-\lambda)\sum_xP_{X'}(x)\log_2\frac{P_{X'}(x)}{\lambda P_X(x)+(1-\lambda)P_{X'}(x)},$$
兩項都是 divergence（各自用 log-sum）$\ge0$，等號 iff $P_X=P_{X'}$。

【口頭】好像是巧合：我們常要讓 entropy 衝到最大，concave 函數有極大值、微分就找得到；要找最小也容易——concave 的最小值一定在邊界。

---

## 2. Mutual information：對輸入 concave、對通道 convex

[▶ 01:32](https://youtu.be/Zc6oi3LwKtg?t=92)

刻意把 MI 寫成**兩個分布的函數**（用逗號表示是一般的兩輸入函數，而不是分號的「傳送端 vs 接收端」）：
$$I(P_X,P_{Y|X}):=\sum_x\sum_yP_X(x)P_{Y|X}(y|x)\log_2\frac{P_{Y|X}(y|x)}{\sum_aP_X(a)P_{Y|X}(y|a)}.$$
$P_X$ 和 $P_{Y|X}$ 各自落在一個 convex set（維度看可能值的個數）。

**Lemma 2.46 (2)**（p. 37）：
- 固定 $P_{Y|X}$，$I$ 是 $P_X$ 的 **concave** 函數；
- 固定 $P_X$，$I$ 是 $P_{Y|X}$ 的 **convex** 函數。

**為什麼剛好有用**（【口頭】）：
- **第二定律（channel coding）**：$P_{Y|X}$ 是自然界量出來的雜訊（送 0 不見得收到 0），不能改；$P_X$ 是你能操作的（送 0、1、2、±1 的比例）。要改 $P_X$ 讓 MI 最大——就是最好的傳輸量 capacity。因為對 $P_X$ concave，**極大值一定存在、微分就找得到、KKT 都成立**。
- **第三定律（lossy data compression，rate-distortion）** [▶ 05:09](https://youtu.be/Zc6oi3LwKtg?t=309)：
  - 要壓縮 $X$，但 $H(X)$ 太大（例如 2 bit），硬碟／flash 只有 1 bit，只能有損失（distortion）地壓成 $\hat X$。
  - Venn 圖：$\hat X$ 是從 $X$ 壓下來的（是 $X$ 的函數），所以 $\hat X$ 的圈整個在 $X$ 的圈裡；兩圈的交集是 $I(X;\hat X)=H(\hat X)$。【口頭】一般的書沒畫這個圖。
  - 這時 $P_X$ 固定（要壓縮的對象，可能是 Markov），能改的是 $P_{\hat X|X}$（壓縮方法）。要找 $P_{\hat X|X}$ 讓 $I(X;\hat X)$ **最小**（在 distortion 限制下）。因為對第二個參數 convex，**極小值一定存在、可以做**。
- 等號何時成立：比值和 $X$ 無關時，在端點上。老師要大家記：**對第一個 concave、對第二個 convex**；第一個的 maximization 是第二定律，第二個的 minimization 是第三定律。

---

## 3. Shannon 的小故事

[▶ 08:44](https://youtu.be/Zc6oi3LwKtg?t=524)

【口頭】
- Shannon 有與生俱來的直覺，碩士、博士論文都是經典，題目還都不一樣。
- 21 歲 MIT 碩士論文：第一個提出用**布林代數**設計邏輯電路，被譽為當代最有價值的碩士論文。
- 三年後 MIT 博士論文：*An Algebra for Theoretical Genetics*（遺傳學）。
- 1948 年的經典論文其實在念博士時就做出來了：23 歲拜訪 von Neumann，原本叫 uncertainty，von Neumann 建議叫 entropy；慢慢想清楚，到 32 歲才發表，大約累積了 9 年。

【課本補充】課本 p. 2 註 2 也提到 Shannon 的碩士論文把開關電路和布林代數連起來、博士論文是 population genetics 的代數架構。

---

## 4. Divergence 是 convex

[▶ 10:15](https://youtu.be/Zc6oi3LwKtg?t=615)

**Lemma 2.46 (3)**（p. 37）：$D(P_X\|P_{\hat X})$ 對第一個參數 convex、對第二個參數 convex，而且對**這一對** convex：
$$D\left(\lambda P_X+(1-\lambda)Q_X\,\middle\|\,\lambda P_{\hat X}+(1-\lambda)Q_{\hat X}\right)\le\lambda D(P_X\|P_{\hat X})+(1-\lambda)D(Q_X\|Q_{\hat X}).$$

【口頭】divergence 的貢獻不在 Shannon，是 Kullback 和 Leibler 1951 年提出的。它是 relative entropy——真正分布是 $P_X$、你以為是 $P_{\hat X}$ 時壓縮付出的代價。要 minimize 這個代價時，因為 convex，一定有解、微分就求得到。

【課本補充】（上一集最後的兩個結果，p. 36）
- **Lemma 2.44**：$X$ 和 $Z$ 獨立、$\hat X$ 和 $\hat Z$ 獨立，則 $D(P_{X|Z}\|P_{\hat X|\hat Z}|P_Z)=D(P_X\|P_{\hat X})$——獨立的 side information 不改變 divergence。
- **Corollary 2.45**：同樣條件下 $D(P_{X,Z}\|P_{\hat X,\hat Z})=D(P_X\|P_{\hat X})+D(P_Z\|P_{\hat Z})$（可加性）。

---

## 5. Hypothesis testing 的設定

[▶ 11:16](https://youtu.be/Zc6oi3LwKtg?t=676)

【口頭】現在開始講**操作**，跟機率理論無關。Chernoff 1952 年處理的是 hypothesis testing：
- 例：銅板公不公平（正反各 1/2，還是不是）？產品算不算成功、要不要賣？
- 根據一串觀察 $X_1,\dots,X_n$ 做決定。

**設定**（課本 pp. 40–41）：
- $H_0$：**null hypothesis**，$X^n\sim P_{X^n}$（編號從 0 開始）；
- $H_1$：**alternative hypothesis**，$X^n\sim P_{\hat X^n}$（只有兩個，所以第二個叫 alternative）。
- **Decision mapping** $\phi(x^n)\in\{0,1\}$：把觀察空間切成兩塊（partition）：
  - **Acceptance region for $H_0$**：$\{x^n:\phi(x^n)=0\}$（"I accept the null hypothesis"）；
  - Acceptance region for $H_1$：$\{x^n:\phi(x^n)=1\}$。
- 兩種錯誤：
$$\text{Type I：}\alpha_n=P_{X^n}\{x^n:\phi(x^n)=1\},\qquad\text{Type II：}\beta_n=P_{\hat X^n}\{x^n:\phi(x^n)=0\}.$$
（Type I：真的是 $P_X$，卻猜 $H_1$；Type II：真的是 $P_{\hat X}$，卻猜 $H_0$。）

【口頭】通訊的接收端做的就是 hypothesis testing。老師再次說：三門數學／觀念性強的課是 Random Process、Detection & Estimation、Information Theory；最後這門真的學通，有助於邏輯推理研究題目。

---

## 6. Bayesian vs Neyman–Pearson

[▶ 14:26](https://youtu.be/Zc6oi3LwKtg?t=866)

兩派的差別在 criterion：
1. **Bayesian**：兩個錯誤都重視，最小化加權和 $\min_\phi\left[\pi_0\alpha_n(\phi)+\pi_1\beta_n(\phi)\right]$（$\pi_0,\pi_1$ 是先驗機率）。
2. **Neyman–Pearson**（Chernoff 做的是這個）：一個錯誤有上限，最小化另一個：
$$\min_{\phi:\ \alpha_n(\phi)\le\varepsilon}\beta_n(\phi).$$

【口頭】例：空襲警報。
- 沒有敵機卻拉警報（**false alarm**）：大家亂跑一下，跑完回來就好，可以容忍——限制它小於某比例（例如 0.01）。
- 有敵機卻沒拉警報：大家不躲，炸彈一下就完了——要最小化這個。

【課本補充】課本 p. 42：$\phi$ 可以是 deterministic rule，也可以是 randomization rule（例如對某些 $\tilde x^n$，以機率 0.2 猜 0、0.8 猜 1）。

---

## 7. Neyman–Pearson lemma

[▶ 15:57](https://youtu.be/Zc6oi3LwKtg?t=957)

**Lemma 2.48**（p. 42）：用 likelihood ratio 定義 $H_0$ 的 acceptance region
$$\mathcal A_n(\tau):=\left\{x^n:\ \frac{P_{X^n}(x^n)}{P_{\hat X^n}(x^n)}>\tau\right\},\qquad\alpha_n^*:=P_{X^n}\left(\mathcal A_n^c(\tau)\right),\quad\beta_n^*:=P_{\hat X^n}\left(\mathcal A_n(\tau)\right).$$
任何其他 acceptance region 的 $\alpha_n,\beta_n$ 滿足
$$\alpha_n\le\alpha_n^*\ \Rightarrow\ \beta_n\ge\beta_n^*.$$
即**不可能同時改善兩種錯誤**。

- 數學上合理：$x^n$ 在 $P_X$ 下的機率比在 $P_{\hat X}$ 下大很多（超過 $\tau$ 倍），就該猜 $H_0$。
- **里程碑的意義**（【口頭】）：**likelihood ratio test 是最好的**——工程上只要做 likelihood ratio test 就夠了。而且它 operationally feasible：代進函數（查表）、一個比較器比大於小於 $\tau$，實作最喜歡這種形式。

**證明**（課本 p. 42）[▶ 18:29](https://youtu.be/Zc6oi3LwKtg?t=1109)：$B$ 是任意 $H_0$ 的 acceptance region。
$$\alpha_n+\tau\beta_n=\sum_{x^n\in B^c}P_{X^n}(x^n)+\tau\sum_{x^n\in B}P_{\hat X^n}(x^n)=\tau+\sum_{x^n\in B^c}\left[P_{X^n}(x^n)-\tau P_{\hat X^n}(x^n)\right].$$
（第二個 sum 寫成 $\tau(1-\sum_{B^c}P_{\hat X^n})$。）要讓它最小，$B^c$ 要恰好收進所有讓方括號為負的 $x^n$，也就是 $P_{X^n}<\tau P_{\hat X^n}$ 的點——即 $B=\mathcal A_n(\tau)$。所以
$$\alpha_n+\tau\beta_n\ge\alpha_n^*+\tau\beta_n^*,$$
若 $\alpha_n\le\alpha_n^*$ 就必須 $\beta_n\ge\beta_n^*$。

【口頭】這種證明之後 Chernoff 和 Shannon 都用，很 universal。

---

## 8. Chernoff–Stein lemma

[▶ 20:33](https://youtu.be/Zc6oi3LwKtg?t=1233)

**Lemma 2.49（Chernoff–Stein lemma）**（p. 43）：觀察 $X^n$ 是 **i.i.d.**，來自 $P_X$（$H_0$）或 $P_{\hat X}$（$H_1$）。最好的 type II 錯誤
$$\beta_n^*(\varepsilon):=\min_{\alpha_n\le\varepsilon}\beta_n$$
滿足
$$\lim_{n\to\infty}-\frac1n\log_2\beta_n^*(\varepsilon)=D(P_X\|P_{\hat X}),\quad\text{對任意 }\varepsilon\in(0,1).$$
即 $\beta_n^*\approx2^{-nD(P_X\|P_{\hat X})}$。

- 要 i.i.d. 是因為需要大數法則（time average 收斂）。例：銅板可能是「正 1/4、反 3/4」或「正 3/4、反 1/4」，不知道是哪一個。
- **確認了 divergence 的操作意義**：它完全決定了 hypothesis testing 的行為。divergence 越大，錯誤率下降越快，用越少的觀察就達到同樣的錯誤率。【口頭】例：$D=2$ ⇒ $\beta\approx2^{-2n}$；$D=3$ ⇒ $\approx2^{-3n}$。要錯誤率小於某值，$D=3$ 需要的觀察數遠少於 $D=2$，因為是指數遞減。

**和 $\varepsilon$ 無關（strong converse）** [▶ 23:09](https://youtu.be/Zc6oi3LwKtg?t=1389)（【口頭】）：
- 對**任意** $\varepsilon$：type I 錯誤限制 0.01 或放寬到 0.1，收斂速度都還是 $D$。
- 差別藏在次要項：其實 $\beta_n^*$ 前面還有一項和 $\sqrt n$ 有關的因子，$\varepsilon$ 透過高斯 CDF（Q function）的反函數出現在 $\sqrt n$ 那項。$n$ 很大時 $n$ 那項 dominant（$n=10000$ 時 $\sqrt n=100$），取 $\frac1n\log$ 再取極限後 $\sqrt n$ 項就消失了。
- 這種「跟 $\varepsilon$ 無關」的強烈結果叫 **strong converse**，Shannon 三大定律也都有（第 12、18 集）。

> ⚠️ 待確認：[▶ 23:39](https://youtu.be/Zc6oi3LwKtg?t=1419) 老師口述的二階修正項（「$\Phi^{-1}(\varepsilon)$ 乘 $\sqrt n$」之類）課本沒有，逐字稿也聽不清完整形式；只能確定它是 $O(\sqrt n)$ 的項，取 $\frac1n\log$ 後消失。

---

## 9. 證明：forward part（divergence typical set）

[▶ 25:09](https://youtu.be/Zc6oi3LwKtg?t=1509)

【口頭】這個證明本來不像 Shannon 的其他證明，老師故意改寫成和 Shannon 一樣的邏輯：**大數法則**。i.i.d. ⇒ 一定存在一個機率很大、size 很小的集合。

**Forward part**：存在一個 acceptance region 使
$$\liminf_{n\to\infty}-\frac1n\log_2\beta_n\ge D(P_X\|P_{\hat X}).$$

**Step 1：divergence typical set** [▶ 26:10](https://youtu.be/Zc6oi3LwKtg?t=1570)：對任意 $\delta>0$，
$$\mathcal A_n(\delta):=\left\{x^n:\ \left|\frac1n\log_2\frac{P_{X^n}(x^n)}{P_{\hat X^n}(x^n)}-D(P_X\|P_{\hat X})\right|<\delta\right\}.$$
- 因為 i.i.d.，
$$\frac1n\log_2\frac{P_{X^n}(x^n)}{P_{\hat X^n}(x^n)}=\frac1n\sum_{i=1}^n\log_2\frac{P_X(x_i)}{P_{\hat X}(x_i)}=\frac1n\sum_{i=1}^nY_i,$$
其中 $Y_i=\log_2\frac{P_X(X_i)}{P_{\hat X}(X_i)}$ 是 $X_i$ 的函數，所以 $Y_i$ 也 i.i.d.，而且 $E_{P_X}[Y_i]=D(P_X\|P_{\hat X})$。
- 由**弱大數法則**，在 $P_X$ 下 $\frac1n\sum Y_i\to D$ in probability，所以 $P_{X^n}(\mathcal A_n(\delta))\to1$。（先取機率再取極限——消息理論只需要 convergence in probability。）
- 這就是 **typical set**（沿用 Shannon 的名詞）：大家都共同看到、很容易看到的典型 outcome；機率趨近 1，但元素不多。【口頭】財富集中在 5% 的人身上，抽稅抽那 5% 就好；操作只要針對裡面，外面不用管。引入 $\delta$ 是為了證明方便，$\delta$ 可以任意小。任何讓這個集合機率趨近 1 的統計條件都行，i.i.d. 只是其中一種。

**關鍵性質** [▶ 31:12](https://youtu.be/Zc6oi3LwKtg?t=1872)：在 $\mathcal A_n(\delta)$ 裡，乘以 $n$、取 2 的次方再移項：
$$P_{X^n}(x^n)\,2^{-n(D+\delta)}<P_{\hat X^n}(x^n)<P_{X^n}(x^n)\,2^{-n(D-\delta)}.$$
$D$ 通常是正的（例如 2 或 3）、$\delta$ 很小（$10^{-2}$、$10^{-3}$），所以在這個集合裡 **$P_{\hat X^n}$ 約是 $P_{X^n}$ 乘上一個很小的數 $2^{-nD}$**：$P_X$ 的機率都在裡面，$P_{\hat X}$ 的機率幾乎都在外面。

**Step 2：取 $\mathcal A_n(\delta)$ 當 $H_0$ 的 acceptance region。**
- **Type I**：$\alpha_n=P_{X^n}(\mathcal A_n^c(\delta))\to0$（大數法則），所以 $n$ sufficiently large 時 $\alpha_n<\varepsilon$。【口頭】sufficiently large $n$——information theory 最常用的敘述：block length 夠長、觀察夠多時一定成立。
- **Type II** [▶ 34:46](https://youtu.be/Zc6oi3LwKtg?t=2086)：
$$\beta_n=P_{\hat X^n}(\mathcal A_n(\delta))=\sum_{x^n\in\mathcal A_n(\delta)}P_{\hat X^n}(x^n)\le\sum_{x^n\in\mathcal A_n(\delta)}P_{X^n}(x^n)\,2^{-n(D-\delta)}=2^{-n(D-\delta)}(1-\alpha_n).$$
  - 【口頭】這個區域就是 log-likelihood ratio test 決定的區域——follow Neyman–Pearson。
- 取 $-\frac1n\log_2$：
$$-\frac1n\log_2\beta_n\ge D-\delta-\frac1n\log_2(1-\alpha_n).$$
  $\alpha_n\to0$，最後一項 $\to0$。因為不知道極限存不存在，取 liminf（最小的群集點）：$\liminf-\frac1n\log_2\beta_n\ge D-\delta$。$\delta$ 任意小（第 4 集的等價敘述），得證。

【口頭】用很簡單的 likelihood ratio 切割就得到很好的結果；forward part 只要證存在一個方法。

---

## 10. 證明：converse part（交集的論證）

[▶ 37:50](https://youtu.be/Zc6oi3LwKtg?t=2270)

**Converse**：**任何** acceptance region $\mathcal B_n$，只要 $\alpha_n=P_{X^n}(\mathcal B_n^c)\le\varepsilon$，都有
$$\limsup_{n\to\infty}-\frac1n\log_2\beta_n\le D(P_X\|P_{\hat X}).$$
（有了 liminf ≥ D 和 limsup ≤ D，兩者相等，極限存在且等於 $D$。）

**核心想法**（【口頭】）：typical set（likelihood ratio 切割）已經抓到最好的重點。你的切割 $\mathcal B_n$ 要做得好，**一定要和 $\mathcal A_n(\delta)$ 有足夠分量的交集**。就像抽稅要抽得好，最有錢的那 5% 一定要抽到大部分——擒賊先擒王。

**計算** [▶ 39:51](https://youtu.be/Zc6oi3LwKtg?t=2391)：
$$\beta_n=P_{\hat X^n}(\mathcal B_n)\ge P_{\hat X^n}(\mathcal B_n\cap\mathcal A_n(\delta))=\sum_{x^n\in\mathcal B_n\cap\mathcal A_n(\delta)}P_{\hat X^n}(x^n)\ge2^{-n(D+\delta)}\sum_{x^n\in\mathcal B_n\cap\mathcal A_n(\delta)}P_{X^n}(x^n).$$
（交集在 $\mathcal A_n(\delta)$ 裡，所以滿足 typical set 的性質 $P_{\hat X^n}>P_{X^n}2^{-n(D+\delta)}$。）

再用一個很鬆但夠用的不等式 $P(A\cap B)\ge1-P(A^c)-P(B^c)$：
$$P_{X^n}(\mathcal B_n\cap\mathcal A_n(\delta))\ge1-P_{X^n}(\mathcal B_n^c)-P_{X^n}(\mathcal A_n^c(\delta))\ge1-\varepsilon-P_{X^n}(\mathcal A_n^c(\delta)),$$
而 $P_{X^n}(\mathcal A_n^c(\delta))\to0$。所以
$$-\frac1n\log_2\beta_n\le D+\delta-\frac1n\log_2\left(1-\varepsilon-P_{X^n}(\mathcal A_n^c(\delta))\right)\to D+\delta.$$
（$1-\varepsilon>0$，所以 log 項是有限的，除以 $n$ 後趨近 0。）取 limsup，$\delta$ 任意小，得證。∎

【口頭】考試不會要你背整個證明（那有點殘忍），但會抽出重要步驟考概念：**typical set、交集**。

---

## 11. 第 2 章總結：其他 information measures

[▶ 43:32](https://youtu.be/Zc6oi3LwKtg?t=2612)

【口頭】
- entropy 的定義歷史上有十幾種，但要有**操作意義**作為支撐才算數。
- Rényi entropy 在 70 年代找到操作意義：有 cost function 時的最小 cost（第 2 集）。
- Rényi divergence（兩個分布分別取 $\alpha$、$1-\alpha$ 次方相乘再加總取 log）目前還沒有確定的操作意義。這些量都有 log，跟 information 量有關。

【課本補充】§2.9（pp. 45–46）：
- **Rényi entropy**（$\alpha>0$，$\alpha\ne1$）：$H_\alpha(X)=\frac1{1-\alpha}\log\sum_xP_X(x)^\alpha$。
- **Rényi divergence**（$0<\alpha<1$）：$D_\alpha(X\|\hat X)=\frac1{\alpha-1}\log\sum_xP_X^\alpha(x)P_{\hat X}^{1-\alpha}(x)$。
- Lemma 2.52：$\alpha\to1$ 時分別回到 Shannon entropy 和 divergence。

---

## 12. 一頁速查表

**凸性（Lemma 2.46）**
- $H(P_X)$ 對 $P_X$ concave（log-sum：左減右 = 兩個 divergence 的加權和）。
- $I(P_X,P_{Y|X})$：對 $P_X$ concave（→ capacity 的 max 可做）；對 $P_{Y|X}$ convex（→ rate-distortion 的 min 可做）。
- $D(P\|Q)$ 對 $(P,Q)$ 聯合 convex。
- 獨立 side information 不改變 $D$；獨立時 $D$ 可加。

**Hypothesis testing**
- $\alpha_n=P_{X^n}(\phi=1)$（type I）、$\beta_n=P_{\hat X^n}(\phi=0)$（type II）。
- Bayesian：$\min\pi_0\alpha_n+\pi_1\beta_n$；Neyman–Pearson：$\min_{\alpha_n\le\varepsilon}\beta_n$。

**Neyman–Pearson lemma**：$\mathcal A_n(\tau)=\{P_{X^n}/P_{\hat X^n}>\tau\}$ 最好；$\alpha_n\le\alpha_n^*\Rightarrow\beta_n\ge\beta_n^*$。
- 關鍵：$\alpha_n+\tau\beta_n=\tau+\sum_{B^c}(P_{X^n}-\tau P_{\hat X^n})$，$B^c$ 收進所有負項時最小。

**Chernoff–Stein**：i.i.d. ⇒ $\lim-\frac1n\log_2\beta_n^*(\varepsilon)=D(P_X\|P_{\hat X})$，$\forall\varepsilon\in(0,1)$（strong converse）。
- Typical set $\mathcal A_n(\delta)=\{|\frac1n\log\frac{P_{X^n}}{P_{\hat X^n}}-D|<\delta\}$：$P_{X^n}(\mathcal A_n)\to1$（WLLN）；其中 $P_{\hat X^n}\approx P_{X^n}2^{-nD}$。
- Forward：$\beta_n\le2^{-n(D-\delta)}$。
- Converse：$\beta_n\ge P_{\hat X^n}(\mathcal B_n\cap\mathcal A_n)\ge2^{-n(D+\delta)}(1-\varepsilon-o(1))$。

**Rényi**：$H_\alpha=\frac1{1-\alpha}\log\sum p^\alpha$；$D_\alpha=\frac1{\alpha-1}\log\sum p^\alpha q^{1-\alpha}$；$\alpha\to1$ 回到 Shannon。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Typical set（大機率、小 size） | 第 12 集（AEP、source coding theorem） |
| Strong converse | 第 12 集（source coding）、第 18 集（channel coding） |
| $I$ 對 $P_X$ concave ⇒ capacity | 第 16–19 集（第 4 章） |
| $I$ 對 $P_{\hat X|X}$ convex ⇒ rate-distortion | 第 27–29 集（第 6 章） |
| Rényi entropy 的操作意義 | 第 15 集附近（§3.3.2） |
| Divergence rate（有記憶的觀察） | 第 12 集（第 3 章） |

---

## 附：本集一句話總結

> **資訊量的凸性剛好對：$I$ 對輸入分布 concave（capacity 可求）、對通道 convex（rate-distortion 可求）；而 Chernoff–Stein lemma 用 typical set 證明 hypothesis testing 的最佳錯誤率是 $2^{-nD}$——divergence 就是兩個分布「被分辨」的速度。**

---

## ⚠️ 待確認清單

1. [▶ 23:39](https://youtu.be/Zc6oi3LwKtg?t=1419) Chernoff–Stein 的二階修正項（和 $\varepsilon$、$\sqrt n$、Q function 反函數有關）的確切形式，課本沒有，逐字稿聽不清。

---

*筆記依據陳伯寧老師「消息理論」Lec11 錄影逐字稿（whisper large-v3-turbo，44:51）與 Alajaji & Chen 課本 §2.6–2.9 整理。*
