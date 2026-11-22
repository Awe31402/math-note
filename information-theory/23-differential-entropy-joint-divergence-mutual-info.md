---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 23
lecture: Lec23 5.1 Differential entropy, 5.2 Joint, cond. diff. entropy, divergence, mutual info
date: 待補
video: https://youtu.be/4nbJ00jcO3Q
notes: Alajaji & Chen §5.1–5.2（pp. 165–183，Example 5.8、Definition 5.9–Observation 5.21）
---

# 第 23 集 · Lec23 §5.2：joint／conditional differential entropy、divergence、mutual information，高斯最大 [▶ 影片](https://youtu.be/4nbJ00jcO3Q)

← 上一集：[22](22-differential-entropy-1.md) ｜ [總目錄](README.md) ｜ 下一集：[24](24-continuous-aep-gaussian-channel-capacity.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 23 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:07:51，whisper large-v3-turbo）＋ 課本 §5.1–5.2（pp. 165–183）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「rate-distortion」聽成「Ray Distortion／Rate Dittortion」，「quantization」聽成「quantation／框台」，「continuous」聽成「continual」，「Bayes rule」聽成「Bayesian Rule／倍式法則」（應為貝氏法則），「Neyman–Pearson」聽成「Neumann-Pearson」，「Chernoff–Stein」聽成「churn of Stein」，「volume」聽成「Volent／Volume」，「公設」聽成「公社」，「Jacobian」聽成「Jacobean」，「原點」聽成「遠點」，「eigenvalue／eigenvector」正確，「Hadamard inequality」聽成「Hadema Inequality」，「Laplacian」聽成「Laproxian」，「Poisson」聽成「Prozant」，「fuzzy logic」聽成「Fargy Logic」，「accuracy」正確，「實數」聽成「時數」。開頭「文化的層次……」是 whisper 幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 脈絡回顧：為什麼要 rate-distortion](#1-脈絡回顧為什麼要-rate-distortion)
- [2. Differential entropy 的意義：調整量](#2-differential-entropy-的意義調整量)
- [3. 高斯的 differential entropy：關鍵在第二步](#3-高斯的-differential-entropy關鍵在第二步)
- [4. Joint 與 conditional differential entropy](#4-joint-與-conditional-differential-entropy)
- [5. Divergence 與 mutual information：n 會消掉](#5-divergence-與-mutual-informationn-會消掉)
- [6. 性質（Lemma 5.14）](#6-性質lemma-514)
- [7. 平移不變與加性雜訊](#7-平移不變與加性雜訊)
- [8. 縮放、線性與非線性變換](#8-縮放線性與非線性變換)
- [9. 多變數高斯的 differential entropy](#9-多變數高斯的-differential-entropy)
- [10. 高斯有最大的 differential entropy](#10-高斯有最大的-differential-entropy)
- [11. 其他限制下的最大：uniform、exponential、Laplacian](#11-其他限制下的最大uniformexponentiallaplacian)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

把 entropy 家族的量都推廣到連續情形，並解釋**為什麼 divergence 和 mutual information 能直接推廣、differential entropy 卻沒有操作定理**（量化的 $n$ 會消掉）。整理 differential entropy 的性質（平移不變、縮放），證明**同樣 covariance 下高斯的 differential entropy 最大**——所以高斯雜訊最難對付。

| 主題 | 課本 |
|---|---|
| Joint／conditional differential entropy、divergence、MI | Definition 5.9–5.12、Observation 5.13（pp. 172–174） |
| 性質 1–11 | Lemma 5.14、Observation 5.15（pp. 174–177） |
| 多變數高斯、Hadamard | Definition 5.16、Theorem 5.18、Corollary 5.19（pp. 177–180） |
| 高斯最大、其他限制 | Theorem 5.20、Observation 5.21（pp. 180–183） |

---

## 1. 脈絡回顧：為什麼要 rate-distortion

[▶ 00:00](https://youtu.be/4nbJ00jcO3Q?t=0)

- 第一定律（壓縮極限 entropy）、第二定律（capacity）、整合定律（information transmission：$m\cdot H<n\cdot C$ 才送得過去）都講完了，現在準備第三定律 **rate-distortion theorem**。
- 但 source 大部分是**連續**的。量化（uniform quantization，step size $2^{-n}$，$n$-bit accuracy）後的 entropy 約 $n$ 加上 differential entropy；$n\to\infty$ 時趨近無限大，而 processing 只會讓 entropy 變小，所以連續 source 的 entropy rate 都是無限大——大於任何有限的 capacity，沒有工程方法送得過去。
- 所以要 **lossy data compression**：例如影像原本是連續的，量化成 256 個位階就有 finite entropy，再慢慢送（今天送明天到也沒關係），調 $m$、$n$ 讓它送得過去。

---

## 2. Differential entropy 的意義：調整量

[▶ 05:42](https://youtu.be/4nbJ00jcO3Q?t=342)

【口頭】
- Differential entropy（也有人叫 continuous entropy）沒有像 source coding、channel coding 那樣明確的等號定理，只有概念上的逼近：它是「連續 source 量化後的 entropy」和「量化精確度 $n$」之間的**調整量（差距）**。
- 越大代表越不容易用量化完整表示。
- 例：兩個 source，$h=8$ 和 $h=-2$。$n=10$（$2^{-10}$）時，第一個量化後要約 18 bit，第二個只要約 8 bit——有的 source 量化完還是非常難傳。
- **高斯最難壓縮**：在相同能量的 source 中，它的 differential entropy 最大——它非常**豐富（rich）**，內含的 information 最多。

---

## 3. 高斯的 differential entropy：關鍵在第二步

[▶ 08:46](https://youtu.be/4nbJ00jcO3Q?t=526)

（Example 5.8，p. 171）$X\sim\mathcal N(\mu,\sigma^2)$。用 $\log_2$ 是因為要和量化精確度 $n$（bit）同單位相加。
$$\begin{aligned}
h(X)&=-\int f_X(x)\log_2f_X(x)\,dx\\
&=\int f_X(x)\left[\frac12\log_2(2\pi\sigma^2)+\frac{(x-\mu)^2}{2\sigma^2}\log_2e\right]dx\qquad(\ast)\\
&=\frac12\log_2(2\pi\sigma^2)+\frac{\sigma^2}{2\sigma^2}\log_2e=\frac12\log_2(2\pi e\sigma^2).
\end{aligned}$$

**第二步 $(\ast)$ 非常重要**（【口頭】）[▶ 10:50](https://youtu.be/4nbJ00jcO3Q?t=650)：
- 第一項是常數，乘上**任何** pdf 積分都是那個常數；
- 第二項只用到 $(x-\mu)^2$ 的期望值——**second moment（variance）**，跟 pdf 的形式無關。
- 所以如果把 $f_X$ 換成**任何**同 variance 的分布 $f_Y$，這個積分 $\int f_Y(-\log_2f_X)$ 的值都一樣。這就是之後證明「高斯最大」的關鍵。
- 【口頭】最難對付的敵人是策略很多的敵人：高斯雜訊最豐富，很難猜它會怎麼干擾你；單純的雜訊只有一種干擾策略，就好對付。

**舉一反三** [▶ 13:56](https://youtu.be/4nbJ00jcO3Q?t=836)：pdf 若是 $e^{-\lambda|x-\mu|}$ 的形式，取 log 後只剩一次 moment——那它就會在「first absolute moment 相同」的 source 中最大；若是三次方，就在 third absolute moment 相同中最大。
- 為什麼專注高斯：通訊看的是**能量 = variance**。光學看的能量是 **first absolute moment**，所以光學常用 exponential（或 Laplacian）輸入，不用高斯——因為在他們的能量限制下那個最豐富。

【口頭】和 $\mu$ 無關：黃色和白色兩個高斯只差平移，量化的難易程度完全一樣。

---

## 4. Joint 與 conditional differential entropy

[▶ 16:30](https://youtu.be/4nbJ00jcO3Q?t=990)

**Definition 5.9（joint differential entropy）**（p. 172）：
$$h(X^n)=-\int f_{X^n}(x^n)\log_2f_{X^n}(x^n)\,dx^n.$$

**Definition 5.10（conditional differential entropy）**（p. 172）：
$$h(Y|X)=-\int\!\!\int f_{X,Y}(x,y)\log_2f_{Y|X}(y|x)\,dx\,dy.$$
（對聯合分布積分，log 裡用條件 pdf——條件 pdf 的期望值。）

【口頭】
- 傳送端 $X$、接收端 $Y$ 都連續，entropy 都無限大，所以討論 joint differential entropy。它不是三大公設衍生的；能不能用它在連續通道上做「共有的量就是傳輸極限」？之後會問。
- **Chain rule** 還是成立：$f_{X,Y}=f_Xf_{Y|X}$（Bayes 法則，19 世紀建立的機率基本法則，連續、離散都對），所以 $h(X,Y)=h(X)+h(Y|X)$。
- 口頭解釋：對 $X$、$Y$ 都量化，要調整的總量 $h(X,Y)$ 可以分開算——先量化 $X$ 的調整量，再量化給定 $X$ 後剩下的 $Y$ 的調整量。

---

## 5. Divergence 與 mutual information：n 會消掉

[▶ 19:36](https://youtu.be/4nbJ00jcO3Q?t=1176)

**Definition 5.11（divergence）**（p. 173）：
$$D(X\|Y)=\int f_X(x)\log_2\frac{f_X(x)}{f_Y(x)}\,dx.$$
**Definition 5.12（mutual information）**（p. 173）：
$$I(X;Y)=\int\!\!\int f_{X,Y}(x,y)\log_2\frac{f_{X,Y}(x,y)}{f_X(x)f_Y(y)}\,dx\,dy=h(X)-h(X|Y)=h(Y)-h(Y|X).$$

**為什麼它們能直接推廣**（【口頭】）：
- **Divergence**：Chernoff–Stein lemma 說 type II 錯誤的指數就是 divergence（離散時用 divergence typical set 證）。連續時沒辦法「數個數」，要改用**體積（volume）**：存在一個體積很小、機率很大的集合。Chernoff 定理對連續的 $X$、$\hat X$ 也成立（老師沒給證明）。
  - 理由：divergence 又叫 **relative entropy**——是**差值**：$\int f_X\log f_X-\int f_X\log f_Y$。把兩個都量化到 $n$ bit（processing 只會讓鑑別度變差），量化後的 divergence 是「($n$ + 調整量)」減「($n$ + 調整量)」——**$n$ 和 $n$ 消掉**，只剩調整量的差。所以量化越來越細時，量化後的 divergence 就趨近連續版的定義，物理意義完全一樣。
  - Entropy 不行，因為它沒有相減，$n$ 消不掉。
- **Mutual information**：Shannon 原本就是用 $H(X)-H(X|Y)$（兩個圈扣掉共有的）定義共識。換成小寫 $h$：傳送端量化成 $n$ bit（例如 6 bit）、接收端量化成 $m$ bit（例如 8 bit），
$$I=\left[n+h(X)\right]+\left[m+h(Y)\right]-\left[n+m+h(X,Y)\right]=h(X)+h(Y)-h(X,Y),$$
  $n$、$m$ 都消掉。所以**channel coding theorem 可以推廣到連續通道**：capacity 還是輸入和輸出最大的 mutual information，只是用 density 定義。

【課本補充】Observation 5.13（pp. 173–174）：量化成 $q_n(X)$、$q_m(Y)$ 時，$I(q_n(X);q_m(Y))\to I(X;Y)$，$D(q_n(X)\|q_n(Y))\to D(X\|Y)$。

【口頭】現在很多 data analytics、big data 要做資料分析、抓資訊量：為什麼這時候選這個量、那時候選那個量，要理解背後的道理。

---

## 6. 性質（Lemma 5.14）

[▶ 31:52](https://youtu.be/4nbJ00jcO3Q?t=1912)

（pp. 174–176）
1. **Divergence 非負**：$D(X\|Y)\ge0$，等號 iff 兩個 pdf（幾乎處處）相同。
2. **Mutual information 非負**：$I(X;Y)\ge0$，等號 iff 獨立。【口頭】傳輸量不可能是負的；完全不能溝通就是 0。
3. **Conditioning 不增加 differential entropy**：$h(X|Y)\le h(X)$，等號 iff 獨立。【口頭】differential entropy 不是三大公設來的，但也有這個性質：有額外的訊息 $Y$，量化 $X$ 應該比較容易達到好的精確度——調整量比較小（例如 $10+2$ 變 $10+1.5$）。證明用 Bayes 法則。
4. **Chain rule for differential entropy**：$h(X^n)=\sum_ih(X_i|X^{i-1})$。（先量化第一個，給定第一個再量化第二個……）
5. **Chain rule for mutual information**。
6. **DPI**：$X\to Y\to Z$ ⇒ $I(X;Y)\ge I(X;Z)$。（離得越遠、處理越多，訊息越少。）
7. **Independence bound**：$h(X^n)\le\sum_ih(X_i)$，等號 iff 獨立。（分開量化、不考慮相關性，一定要花比較多 bit。）
8–11 是 differential entropy **特有**的性質（下兩節）。

---

## 7. 平移不變與加性雜訊

[▶ 35:26](https://youtu.be/4nbJ00jcO3Q?t=2126)

**Property 8（平移不變，translation invariance）**：
$$h(X+c)=h(X),\qquad h(X+Y|Y)=h(X|Y);$$
多變數也一樣。

【口頭】電視調整的電壓是 0–0.8 V，要量化成 256 個位階；加一個 offset 變成 1–1.8 V，量化會比較容易嗎？不會，範圍還是那麼大。

**為什麼這個性質非常重要**（【口頭】）[▶ 37:31](https://youtu.be/4nbJ00jcO3Q?t=2251)：一個數學的量可以討論很多性質，但有些對操作真正有用。實際碰到的雜訊大多是**加性雜訊（additive noise）**——相加就是對 $X$ 做平移。$Y=X+N$，$N$ 和 $X$ 獨立：
$$h(Y|X)=h(X+N|X)=h(N|X)=h(N),$$
所以
$$I(X;Y)=h(Y)-h(Y|X)=h(Y)-h(N).$$
- 第二項 $h(N)$ 你不能改善（雜訊是量出來的），它是被**扣掉**的。所以**雜訊的 differential entropy 越大，能傳的越少**。
- 最大的是高斯（還沒證）——所以從通訊角度最不喜歡高斯；光學上最不喜歡 Laplacian。兩個原因：這種雜訊 differential entropy 最大，而且我們對付的剛好是相加雜訊。

---

## 8. 縮放、線性與非線性變換

[▶ 41:37](https://youtu.be/4nbJ00jcO3Q?t=2497)

**Property 9（縮放）**：$a\ne0$，
$$h(aX)=h(X)+\log_2|a|.$$
【口頭】0–0.8 V 放大成 0–1.6 V，要達到同樣的量化精確度（例如 $10^{-1}$ 的刻度）比較難，位階要更多。放大 2 倍，要多切一半（0–0.8、0.8–1.6），多 1 bit——$\log_22=1$；放大 4 倍多 2 bit。數學非常對：scaling 會改變 differential entropy，因為它是量化精確度的調整量。

**Property 10（線性變換）**：$Y=AX$，$A$ 可逆，
$$h(Y)=h(X)+\log_2|\det(A)|.$$
【口頭】二維以上的放大可能不等倍率（$x$ 軸 2 倍、$y$ 軸 3 倍、變形、加上旋轉），看的是 determinant。

**Property 11（非線性變換）**：$Y=(g_1(X_1),\dots,g_n(X_n))$，$g_i$ 可微，
$$h(Y)=h(X)+\int f_{X^n}(x^n)\log_2|\det(J)|\,dx^n,$$
$J$ 是 Jacobian 矩陣。
- 【口頭】例：語音、影像常做非線性放大——聲音小的放大多、大的放大少（人的感官不是線性的）。證明就是用定義，把 $y$ 換回 $x$ 時積分要乘 Jacobian（像大一微積分從直角坐標換到極坐標）。
- 實作上會平移、旋轉、放大、縮小；在連續通道下要知道什麼操作會怎麼改變它。

【課本補充】Observation 5.15（p. 176）：由 Property 9，$h$ 可以任意大或任意小（縮放就好），不像離散 entropy 有 $0\le H\le\log|\mathcal X|$ 的界。

---

## 9. 多變數高斯的 differential entropy

[▶ 51:21](https://youtu.be/4nbJ00jcO3Q?t=3081)

【口頭】高斯重要，因為應用上真的會碰到：有線傳輸量到的幾乎都是高斯；遠距離（例如微波）的背景雜訊也是加性高斯。

【口頭】花很久解釋 differential entropy 的概念，老師覺得這比要證明的數學重要。例：要讓一支筆在桌上平衡，可以硬幹（往左倒就往右拉），調得夠快就平衡，但很費力；懂了槓桿、力矩，就能省很多力氣。現在很多 big data、AI 的研究是結果論（試七八種結構，training 出來就對），不知道為什麼——需要有人朝理解的方向去想。這就是為什麼國外通訊研究所把消息理論當必修基礎。

**Theorem 5.18**（p. 178）：$X\sim\mathcal N_n(\mu,K_X)$（$K_X$ 正定），
$$h(X)=\frac12\log_2\left[(2\pi e)^n\det(K_X)\right].$$
$n=1$ 時回到 $\frac12\log_2(2\pi e\sigma^2)$。

**證明**（課本 pp. 178–179）：
- 平移不變，假設 mean 為 0。
- $K_X$ 正定（對稱），可以**對角化**：存在 orthogonal 矩陣 $A$（$A^T=A^{-1}$，$|\det A|=1$）使 $K_Y=AK_XA^T=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$，$Y=AX$。
- 高斯的線性變換還是高斯；$K_Y$ 對角 ⇒ $Y_i$ uncorrelated ⇒（高斯）獨立。
- $h(Y)=\sum_ih(Y_i)=\sum_i\frac12\log_2(2\pi e\lambda_i)=\frac12\log_2\left[(2\pi e)^n\prod\lambda_i\right]=\frac12\log_2\left[(2\pi e)^n\det K_Y\right]$。
- $\det K_Y=\det A\det K_X\det A^T=\det K_X$；Property 10 加 $|\det A|=1$ 得 $h(X)=h(Y)$。∎

【口頭】只跟 covariance 的 determinant 有關，而 determinant 是 **eigenvalue 的乘積**。老師大二學 eigenvalue、eigenvector 時不知道在幹嘛，後來發現很重要：通訊上常抓大的 eigenvalue（影響 differential entropy 的主要量）。例：學生的博士論文做 64 根天線的傳輸，$64\times64$ 的 channel gain 矩陣太大，就做 eigen-decomposition、對角化，取大的、丟掉小的，性質就很好——方向是對的，因為它完全影響 mutual information。

---

## 10. 高斯有最大的 differential entropy

[▶ 55:53](https://youtu.be/4nbJ00jcO3Q?t=3353)

**Corollary 5.19（Hadamard 不等式）**（p. 180）：正定矩陣 $K$，
$$\det(K)\le\prod_{i=1}^nK_{i,i},$$
等號 iff $K$ 是對角矩陣。
【課本補充】證明：取 $X\sim\mathcal N_n(0,K)$，$\frac12\log_2[(2\pi e)^n\det K]=h(X)\le\sum_ih(X_i)=\frac12\log_2[(2\pi e)^n\prod K_{i,i}]$（independence bound）。

**Theorem 5.20（最大 differential entropy）**（p. 180）：$X$ 的 support 是 $\mathbb R^n$、mean $\mu$、covariance $K_X$、$h$ 有限，則
$$h(X)\le\frac12\log_2\left[(2\pi e)^n\det(K_X)\right],$$
等號 iff $X$ 是高斯。

【口頭】所有能量（variance）相同的連續 source 中，**高斯的 differential entropy 最大**——也就是當雜訊時 channel capacity 最小、最難對付。很倒楣，我們真的碰到的大多就是高斯。

**證明（$n=1$）**（照口訣：相減、用 divergence $\ge0$）[▶ 58:29](https://youtu.be/4nbJ00jcO3Q?t=3509)：令 $g$ 是和 $X$ 同 mean、同 variance 的高斯 pdf。
$$0\le D(f_X\|g)=\int f_X\log_2\frac{f_X}g=-h(X)-\int f_X(x)\log_2g(x)\,dx.$$
而由第 3 節的關鍵觀察，$-\int f_X\log_2g$ 只用到 $X$ 的 second moment，所以等於 $-\int g\log_2g=h(\text{Gaussian})=\frac12\log_2(2\pi e\sigma^2)$。於是 $h(X)\le\frac12\log_2(2\pi e\sigma^2)$，等號 iff $D=0$ iff $X$ 是高斯。
- 【口頭】高斯為什麼這麼豐富：它有特別的形式（exponential），取 log 後只剩能量那一項。只要有指數形式的都不好壓縮。

**多變數**（課本 pp. 181–182）：用 whitening：$Z=AX$，$A$ orthogonal 讓 $K_Z$ 對角。$X$ 不一定是高斯，所以
$$h(X)=h(Z)\le\sum_ih(Z_i)\le\sum_i\frac12\log_2(2\pi e\,\mathrm{Var}(Z_i))=\frac12\log_2\left[(2\pi e)^n\det K_Z\right]=\frac12\log_2\left[(2\pi e)^n\det K_X\right].$$
（independence bound，再對每個 $Z_i$ 用一維結果。）

---

## 11. 其他限制下的最大：uniform、exponential、Laplacian

[▶ 62:03](https://youtu.be/4nbJ00jcO3Q?t=3723)

**問題**：雜訊若不是高斯——例如 $Y=X+N$，$N$ 只在 $[-1,1]$ 之間——最難對付的雜訊是什麼？因為 $I=h(Y)-h(N)$，最怕 $h(N)$ 大。

**Observation 5.21**（p. 182）：
1. support 是 $(a,b)$ 的所有分布中，**uniform** 的 differential entropy 最大。
   - 【口頭】合理：每個值機會都一樣，你對它最無知，最難量化得精確。若雜訊靠近 ±1 的機率高、0 的機率低，反而比較好對付，因為有預期。高斯不在這裡，因為它的 support 是整個實數。
2. support 是 $[0,\infty)$、mean 為 $\mu$ 的分布中，**exponential**（參數 $\lambda=\frac1\mu$）最大。
   - 【口頭】什麼時候雜訊一定是正的？**光學傳輸**——雜訊不可能是負的，量到的也不是高斯。光學的能量是 first moment（老師問過光學學者）。最怕的雜訊就是 exponential。巧的是，在大數法則下常觀察到的也是 exponential：例如銀行顧客彼此獨立地來，一段時間來的個數是 Poisson，相鄰兩個之間的時間是 exponential。
3. support 是 $\mathbb R$、mean $\mu$、$E|X-\mu|=\lambda$ 的分布中，**Laplacian**
$$f_X(x)=\frac1{2\lambda}e^{-|x-\mu|/\lambda}$$
   最大。【口頭】所以光學的論文常在討論 Laplacian——剛好是他們最怕的雜訊，而他們量到的也都是它。這些都是大數法則在不同情形下收斂出來的分布。

【口頭】怎麼看出來：算 differential entropy 時，一取 log 和指數消掉、再取期望值，就只剩那個 moment，跟分布的樣子無關——所以最怕的是這種形式。很多書有各種變形的題目，看懂了都很簡單。準備考試：考 10 題可以背、100 題也許可以背，1000 題選 10 題就不行了——要**歸納、理解背後的道理**。

【課本補充】Observation 5.22（p. 183）：stationary 零均值高斯過程的 differential entropy rate、divergence rate 和它們的 Rényi 版本都存在，而且有解析式。

---

## 12. 一頁速查表

**定義**：$h(X^n)=-\int f\log f$；$h(Y|X)=-\iint f_{XY}\log f_{Y|X}$；$D(X\|Y)=\int f_X\log\frac{f_X}{f_Y}$；$I(X;Y)=\iint f_{XY}\log\frac{f_{XY}}{f_Xf_Y}=h(X)-h(X|Y)$。

**為什麼 $D$、$I$ 能推廣、$h$ 沒有操作定理**：量化後 $H\approx n+h$；$D$、$I$ 是差值，$n$ 消掉；$h$ 沒有相減，$n$ 消不掉。

**性質**
- $D\ge0$、$I\ge0$、$h(X|Y)\le h(X)$、chain rule、DPI、$h(X^n)\le\sum h(X_i)$（同離散）。
- 平移：$h(X+c)=h(X)$，$h(X+Y|Y)=h(X|Y)$。
- 縮放：$h(aX)=h(X)+\log_2|a|$；線性：$h(AX)=h(X)+\log_2|\det A|$；非線性：加 $E[\log_2|\det J|]$。
- 加性雜訊 $Y=X+N$（獨立）：$I(X;Y)=h(Y)-h(N)$——雜訊的 $h$ 越大越糟。

**高斯**
- $h(\mathcal N(\mu,\sigma^2))=\frac12\log_2(2\pi e\sigma^2)$；$h(\mathcal N_n(\mu,K))=\frac12\log_2[(2\pi e)^n\det K]$（對角化 + 獨立）。
- 關鍵：$\int f\cdot(-\log g_{\text{Gauss}})$ 只依賴 second moment。
- Hadamard：$\det K\le\prod K_{ii}$。
- **最大**：同 covariance 下 $h(X)\le\frac12\log_2[(2\pi e)^n\det K_X]$，等號 iff 高斯（證：$0\le D(f\|g)=-h(X)+h(g)$）。

**其他限制下的最大**：support $(a,b)$ → uniform；support $[0,\infty)$、固定 mean → exponential；support $\mathbb R$、固定 $E|X-\mu|$ → Laplacian。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 連續 source 的 AEP、typical set 的體積 | 第 24 集（§5.3） |
| $I=h(Y)-h(N)$ + 高斯最大 ⇒ Gaussian channel capacity、高斯輸入最佳 | 第 24 集（§5.4） |
| 高斯雜訊讓 capacity 最小（Theorem 5.33） | 第 24 集 |
| 多變數高斯、對角化、eigenvalue | 第 25–26 集（parallel Gaussian channels、water-filling） |
| 高斯 source 的 rate-distortion | 第 29 集（§6.4） |

---

## 附：本集一句話總結

> **把 entropy 家族推廣到連續時，divergence 和 mutual information 是「差值」，量化的 $n$ 會消掉所以意義完全保留；differential entropy 則是量化的調整量——它平移不變、縮放會加 $\log|a|$，而在同樣能量下高斯最大，因為 $I=h(Y)-h(N)$，高斯雜訊正是最難對付的雜訊。**

---

*筆記依據陳伯寧老師「消息理論」Lec23 錄影逐字稿（whisper large-v3-turbo，1:07:51）與 Alajaji & Chen 課本 §5.1–5.2 整理。*
