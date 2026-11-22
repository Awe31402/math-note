---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 22
lecture: "Lec22 Chapter 5: Differential Entropy and Gaussian Channels: 5.1 Differential entropy"
date: 待補
video: https://youtu.be/7jzQID3fSY0
notes: Alajaji & Chen §5.1（pp. 165–172，Example 5.1–Example 5.8）
---

# 第 22 集 · Lec22 第 5 章：連續 source 的 entropy 是無限大、differential entropy [▶ 影片](https://youtu.be/7jzQID3fSY0)

← 上一集：[21](21-joint-source-channel-separation.md) ｜ [總目錄](README.md) ｜ 下一集：[23](23-differential-entropy-joint-divergence-mutual-info.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 22 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（30:49，whisper large-v3-turbo）＋ 課本 §5.1（pp. 165–172）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「capacity」聽成「可佩裏」，「continuous」聽成「continual」，「quantization」聽成「quantation／contention／框材」，「waveform」聽成「Wayform」，「Riemann integral」聽成「Reyman Integral／李曼／里曼積分」，「Lebesgue integral」聽成「the best integral」，「實變分析」聽成「十遍分析」，「criterion」聽成「quiterion」，「Rényi」聽成「Rinney」，「實數」聽成「時數」，「mean value theorem」正確，「Shannon」聽成「Shanen」，「旺季」應為「忘記」。開頭「詞曲曲 李宗盛」是幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要第 5 章](#1-為什麼要第-5-章)
- [2. Discrete、continuous、waveform source](#2-discretecontinuouswaveform-source)
- [3. 連續 source 的 entropy 是無限大](#3-連續-source-的-entropy-是無限大)
- [4. 需要一個新的量](#4-需要一個新的量)
- [5. Lemma 5.2：量化後的 entropy ≈ h(X) + n](#5-lemma-52量化後的-entropy--hx--n)
- [6. 證明](#6-證明)
- [7. Differential entropy 的定義與意義](#7-differential-entropy-的定義與意義)
- [8. 例子](#8-例子)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

連續 source 要完整傳過去需要無限多 bit——entropy 對連續 source 失效。這一集定義新的量 **differential entropy** $h(X)=-\int f\log f$，並用「均勻量化到 $n$ bit 精確度後的 entropy ≈ $h(X)+n$」來理解它。

【口頭】希望你抓到的是思考模式的精神，幾年後還記得；數學忘記沒關係。

| 主題 | 課本 |
|---|---|
| 連續 source 的 entropy 無限大 | Example 5.1（p. 166） |
| 量化後 entropy ≈ $h+n$ | Lemma 5.2、Theorem 5.3（pp. 167–169） |
| Differential entropy | Definition 5.4（p. 169） |
| 例子 | Example 5.5–5.8（pp. 169–172） |

---

## 1. 為什麼要第 5 章

[▶ 00:31](https://youtu.be/7jzQID3fSY0?t=31)

【口頭】
- 第三定律（rate-distortion）的出發點：有時 entropy rate 比 capacity 大很多，送不過去。
- 有一種情形 entropy rate **一定**比 capacity 大：**continuous source**。整個第 5 章會告訴你：任何連續 source 的 entropy 都是無限大，要沒有資料損失地完整送過去，需要無限多 bit——一定大於 capacity。所以要做 distortion（有損壓縮）。
- 另一個要考慮的是 **Gaussian channel**——最常見的傳輸管道是高斯雜訊。在它底下，怎麼利用連續輸入做有損壓縮、得到和輸出的關係。

---

## 2. Discrete、continuous、waveform source

[▶ 01:02](https://youtu.be/7jzQID3fSY0?t=62)

「continuous」有兩個意思：**時間**（index set）和**值**。
- **Discrete source**：時間離散（取樣後 1、2、3、4 單位時間送）、值也離散（只送 ±1、±3）。
- **Continuous source**（這一章）：時間還是離散，但值 $X$ 是連續的——第一個時間送 0.2、第二個送 −0.8、第三個送 0.92……任何實數都有可能。
- **Waveform source**：時間和值都連續。例：三個 codeword 是三種不同的波形，接收端用有雜訊的接收波形去猜送的是 0、1 還是 2。【口頭】比較不接近實用系統：兩個都開放連續，複雜度增加很多，得到的 gain 卻不多。

【口頭】之後會證明：**對高斯雜訊，最好的輸入是連續的、而且是高斯分布**。高斯輸入實作上不可能做，實際用 BPSK、QPSK（±1、±3）。但把輸入限制在這些離散值，capacity 只損失一點點，大約 **0.2 dB**——非常少，所以不一定要堅持連續輸入。

---

## 3. 連續 source 的 entropy 是無限大

[▶ 04:08](https://youtu.be/7jzQID3fSY0?t=248)

**Example 5.1**（p. 166）：$X$ 在 $[0,1)$ 上 uniform，pdf $f_X(x)=1$。
- 實作上會**量化（quantization）**：例如分成 256 個位階、每個用 8 bit。一般地，step size $\Delta=\frac1m$，
$$q_m(X)=\frac im\quad\text{若}\ \frac{i-1}m\le X<\frac im,\quad1\le i\le m.$$
- 量化後每個值機率 $\frac1m$，
$$H(q_m(X))=-\sum_{i=1}^m\frac1m\log_2\frac1m=\log_2m\ \text{bits}.$$
- **Processing 只會減少 entropy**：$q_m$ 是一個函數（多對一：一個範圍全部用一個值代表；原本無限多可能，量化後只剩 $m$ 個），所以 $H(X)\ge H(q_m(X))=\log_2m$。
- $m$ 可以任意大，$\log_2m\to\infty$，所以 **$H(X)=\infty$**。

結論：任何連續 source 要無損壓縮都不可能，也送不過去。

---

## 4. 需要一個新的量

[▶ 07:16](https://youtu.be/7jzQID3fSY0?t=436)

- 所有連續 source 的 entropy 都是無限大，**沒辦法比較**：高斯 source 是無限大、uniform source 也是無限大，誰的資料量比較豐富、誰比較難送？無限大和無限大不能比大小。
- 所以 entropy 這個量在這種應用情境下**失效**了（limited in its effectiveness），要找一個新的量——它是 entropy 的等效，所以這一節叫 **differential entropy**。

**沒有嚴格的操作定理**（【口頭】）[▶ 08:20](https://youtu.be/7jzQID3fSY0?t=500)：
- Shannon 第一定律的大貢獻：數學上用三大公設算出 entropy，操作上的最小壓縮率剛好等於它——兩者完全相等。
- Differential entropy 的問題：**沒有一個操作上的定理**說「某個操作在某個 criterion 下最好就是 $h(X)$」，到目前為止還沒找到。它只有概念性的解釋；叫 entropy 是因為它是延伸概念。下面的例子只能「理解」，不是那種強烈的等效結果。

---

## 5. Lemma 5.2：量化後的 entropy ≈ h(X) + n

[▶ 10:27](https://youtu.be/7jzQID3fSY0?t=627)

**Riemann 積分**（【口頭】）：古埃及尼羅河氾濫，爛泥帶來肥沃的土壤，但大家田地的界線不見了，要重新丈量面積。長方形面積是底乘以高；不規則形狀就用越來越細的小長方形去逼近，從上、從下逼近都收斂到同一個值，就是 Riemann 積分。有的函數不能 Riemann 積分，那要用實變分析的 Lebesgue 積分；工程上用最簡單的 Riemann 就好。

**Lemma 5.2**（p. 167）：$X$ 的 support 是 $[a,b)$、pdf $f_X$，$-f_X\log_2f_X$ **Riemann 可積**且 $-\int_a^bf_X\log_2f_X\,dx$ 有限。以 **$n$-bit accuracy** 均勻量化（step size $\Delta=2^{-n}$）得到 $q_n(X)$，則 $n$ 夠大時
$$H(q_n(X))\approx-\int_a^bf_X(x)\log_2f_X(x)\,dx+n,\qquad\text{即}\ \lim_{n\to\infty}\left[H(q_n(X))-n\right]=-\int_a^bf_X(x)\log_2f_X(x)\,dx.$$

- **$n$-bit accuracy**（【口頭】）：$\Delta=2^{-n}$，二進位小數點以下第 $n$ 位都精確（$10^{-n}$ 就是十進位第 $n$ 位）。例：$\Delta=2^{-4}=\frac1{16}$，$[0,1)$ 上最多 16 個位階。
- 意義：量化後的 entropy 大約是「一個新的量」加上 $n$。

---

## 6. 證明

[▶ 19:12](https://youtu.be/7jzQID3fSY0?t=1152)

（課本 pp. 167–168）

**Step 1：mean value theorem**。$\Delta=2^{-n}$，$t_i=a+i\Delta$（$i=0,\dots,j-1$），$t_j=b$，$j=\lceil(b-a)2^n\rceil$。由 mean value theorem（一階逼近），存在 $x_i\in[t_{i-1},t_i]$ 使
$$p_i:=\int_{t_{i-1}}^{t_i}f_X(x)\,dx=f_X(x_i)(t_i-t_{i-1})=\Delta\cdot f_X(x_i).$$

**Step 2：Riemann 和 $h^{(n)}(X)$**。定義
$$h^{(n)}(X):=-\sum_{i=1}^j\left[f_X(x_i)\log_2f_X(x_i)\right]2^{-n}.$$
【口頭】這跟操作無關：就是用寬 $\Delta$、高 $-f\log f$（取中間值）的長方形去逼近 $-f\log f$ 這個函數底下的面積。因為 Riemann 可積，$h^{(n)}(X)\to-\int_a^bf_X\log_2f_X\,dx$；即對任意 $\varepsilon>0$，存在 $N$ 使 $n>N$ 時兩者差 $<\varepsilon$。

**Step 3：量化後的 entropy**：
$$H(q_n(X))=-\sum_ip_i\log_2p_i=-\sum_i\left(f_X(x_i)2^{-n}\right)\log_2\left(f_X(x_i)2^{-n}\right).$$
（和 Step 2 的差別：機率 $p_i$ 裡多了一個 $\Delta=2^{-n}$。）

**Step 4：相減**：
$$H(q_n(X))-h^{(n)}(X)=-\sum_i\left[f_X(x_i)2^{-n}\right]\log_2(2^{-n})=n\sum_i\int_{t_{i-1}}^{t_i}f_X(x)\,dx=n\int_a^bf_X(x)\,dx=n.$$
【口頭】把 $2^{-n}$ 提出來，只差 $\log_22^{-n}=-n$ 那一項，負負得正，總面積是 1。

所以 $n>N$ 時
$$-\int f\log f+n-\varepsilon<H(q_n(X))=h^{(n)}(X)+n<-\int f\log f+n+\varepsilon,$$
得證。∎

【課本補充】**Theorem 5.3**（Rényi 1959，pp. 168–169）：對 support 任意的實數隨機變數，只要量化後 $-\sum p_i\log p_i$ 有限、右邊積分存在，同樣 $\lim[H(q_n(X))-n]=-\int_{S_X}f_X\log_2f_X\,dx$。【口頭】大家慢慢把條件放寬（不必 Riemann 可積、support 不必是 $[a,b)$），都有類似結果。

---

## 7. Differential entropy 的定義與意義

[▶ 15:05](https://youtu.be/7jzQID3fSY0?t=905)

**Definition 5.4（differential entropy）**（p. 169）：連續隨機變數 $X$，pdf $f_X$、support $S_X$，
$$h(X):=-\int_{S_X}f_X(x)\log_2f_X(x)\,dx=E\left[-\log_2f_X(X)\right]\quad(\text{積分存在時}).$$

**意義**（【口頭】）：
- 樣子很像 entropy（density 乘上 log 倒數再積分；離散是 summation），但它**不是來自三大公設**。
- 它是「$n$-bit 均勻量化後的 entropy 減去 $n$」。
- **可正可負**，不保證恆正，所以好像也不是在代表 information 的量。
- 一種解釋：它衡量**一個 source 適不適合／容不容易做 uniform quantization**。數位傳輸一定要送量化後的 $q_n(X)$；它的 entropy 越小越容易送（information transmission theorem：要小於 capacity 才送得過去）。基本量是 $n$，再加減一個數——那個數就是 $h(X)$。所以 **$h(X)$ 越大，量化後的 entropy rate 越高、越難送，source 越「豐富」**。
- 之後會證明：**在相同能量（variance）下，高斯最難做量化**——它最豐富，用 uniform quantization 出來的 entropy 最多。

【課本補充】課本（p. 169）的說法：$H(q_n(X))$ 是無損描述 $q_n(X)$ 的最小平均 bit 數，所以以 $n$-bit 精確度描述 $X$ 大約需要 $h(X)+n$ bit；$h(X)$ 越大，固定精確度下描述量化後的 $X$ 平均需要的 bit 越多。

---

## 8. 例子

**Example 5.5**（pp. 169–170）[▶ 25:26](https://youtu.be/7jzQID3fSY0?t=1526)：support $[0,1)$，$f_X(x)=2x$（總面積是 1）。
$$h(X)=\int_0^1-2x\log_2(2x)\,dx=\left.\frac{x^2\left(\log_2e-2\log_2(2x)\right)}2\right|_0^1=\frac1{2\ln2}-\log_22\approx-0.2787\text{ bits}.$$
- 量化：$\Pr\left[q_n(X)=\frac i{2^n}\right]=\frac{2i-1}{2^{2n}}$，
$$H(q_n(X))=-\frac1{2^{2n}}\sum_{i=1}^{2^n}(2i-1)\log_2(2i-1)+2\log_2(2^n).$$
- 課本 Table 5.1：$n$ 增加時 $H(q_n(X))\to\infty$（老師說 $n=9$ 時約 8.72），但 $H(q_n(X))-n\to-0.2787$。
- 【口頭】負的代表什麼：step size $2^{-10}$（1024 個位階）時，量化後只需要約 $10-0.28$，大概 9 點多個 bit 就夠；capacity 若是 10 bit 就送得過去。

**Example 5.7（uniform）**（p. 171）[▶ 26:58](https://youtu.be/7jzQID3fSY0?t=1618)：$X\sim U[a,b)$，density 是常數 $\frac1{b-a}$，
$$h(X)=\log_2(b-a).$$
$b-a<1$ 時是**負的**。
- 【口頭】例：螢幕亮度只到 0–0.8，數位顯示要量化到 $2^{-10}$ 的精確度時，不需要 10 bit，少一點點就好；若範圍是 0–2，就需要比 10 bit 多一點。

**Example 5.8（Gaussian）**（pp. 171–172）[▶ 28:29](https://youtu.be/7jzQID3fSY0?t=1709)：$X\sim\mathcal N(\mu,\sigma^2)$，$\sigma^2>0$（$\sigma^2=0$ 就是 deterministic，沒意義），
$$f_X(x)=\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}\quad(\text{要背}).$$
$$\begin{aligned}
h(X)&=E\left[-\log_2f_X(X)\right]=E\left[\frac12\log_2(2\pi\sigma^2)+\frac{(X-\mu)^2}{2\sigma^2}\log_2e\right]\\
&=\frac12\log_2(2\pi\sigma^2)+\frac{\sigma^2}{2\sigma^2}\log_2e=\frac12\log_2(2\pi e\sigma^2).
\end{aligned}$$
（第一項是常數乘 density 積分為 1；第二項是 second moment $\sigma^2$。）

**觀察：和 $\mu$ 無關，只跟 variance 有關。**
- 【口頭】$\mu=0$ 和 $\mu=1$ 的高斯（都從 $-\infty$ 到 $\infty$），用 $2^{-10}$ 的精確度量化，難易程度一樣——**平移不改變量化的難易程度**；uniform 在 $[0,1)$ 和 $[1,2)$ 量化後的資料量也一樣。這個解釋是對的：平移不改變 differential entropy（對所有 source 都對）。

【課本補充】**Example 5.6**（p. 170）：鐳原子衰變時間 $f_X(x)=\lambda e^{-\lambda x}$，半衰期（median）80 年 ⇒ $\lambda=0.00866$。3 位數精確度約 $\log_2999\approx10$ bit，所以描述量化後的衰變時間約需
$$h(X)+10=\log_2\frac e\lambda+10\approx18.29\text{ bits}.$$

---

## 9. 一頁速查表

**連續 source 的 entropy**：$H(q_m(X))=\log_2m$（$U[0,1)$），且 $H(X)\ge H(q_m(X))$ ⇒ $H(X)=\infty$。entropy 對連續 source 失效。

**Lemma 5.2**：$\Delta=2^{-n}$ 均勻量化，
$$\lim_{n\to\infty}\left[H(q_n(X))-n\right]=-\int f_X\log_2f_X\,dx.$$
- 關鍵：$p_i=\Delta f(x_i)$（mean value theorem）⇒ $H(q_n)-h^{(n)}=-\sum p_i\log_2\Delta=n$；$h^{(n)}$ 是 Riemann 和。

**Differential entropy**：$h(X)=-\int f\log_2f=E[-\log_2f(X)]$。
- 解釋：$n$-bit 量化後約需 $h(X)+n$ bit；$h$ 越大越難量化、越豐富。可正可負；沒有嚴格的操作定理。
- $U[a,b)$：$\log_2(b-a)$。
- $f=2x$ on $[0,1)$：$\frac1{2\ln2}-1\approx-0.2787$。
- $\mathcal N(\mu,\sigma^2)$：$\frac12\log_2(2\pi e\sigma^2)$，與 $\mu$ 無關（平移不變）。
- 指數分布：$\log_2\frac e\lambda$。

**輸入**：對高斯雜訊，最佳輸入是高斯；限制成 BPSK/QPSK 只損失約 0.2 dB（老師口述）。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Joint / conditional differential entropy、divergence、mutual information；平移、縮放的性質 | 第 23 集（§5.2） |
| 相同 variance 下高斯的 differential entropy 最大 | 第 23 集（Theorem 5.20） |
| 連續 source 的 AEP、typical set 的體積 | 第 24 集（§5.3） |
| Gaussian channel capacity $\frac12\log(1+\frac P\sigma^2)$ | 第 24 集（§5.4） |
| 連續 source 一定要有損：rate-distortion | 第 27–29 集（第 6 章） |

---

## 附：本集一句話總結

> **連續 source 要無損描述需要無限多 bit，所以 entropy 失效；但均勻量化到 $n$ bit 精確度後，entropy 大約是 $h(X)+n$——differential entropy $h(X)=-\int f\log f$ 衡量的是一個 source「多難量化」，例如高斯是 $\frac12\log(2\pi e\sigma^2)$，跟平移無關。**

---

*筆記依據陳伯寧老師「消息理論」Lec22 錄影逐字稿（whisper large-v3-turbo，30:49）與 Alajaji & Chen 課本 §5.1 整理。*
