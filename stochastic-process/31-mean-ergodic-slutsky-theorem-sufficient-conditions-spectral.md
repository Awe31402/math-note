---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 31
lecture: Lec 12-1 Spectrum Estimation — Ergodicity (1/3)
date: 待補
video: https://youtu.be/onZdVKEBZpg
notes: Papoulis & Pillai 4th ed. §12-1 Mean-Ergodic Processes（式 (12-1)–(12-18)、Theorem 12-1、12-2、Example 12-1、12-6、12-7，pp. 523–530）
---

# 第 31 集 · Lec 12-1 (1/3)：均值遍歷 (mean-ergodic)、時間平均的變異數、Slutsky 定理、充分條件、離散版本、頻譜詮釋 [▶ 影片](https://youtu.be/onZdVKEBZpg)

← 上一集：[30](30-ergodicity-shift-invariant-event-history.md) ｜ [總目錄](README.md) ｜ 下一集：[32](32-ergodicity-motivation-measurement-correction.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 31 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（40:26，whisper large-v3-turbo）＋ Papoulis §12-1（pp. 523–530）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「mean-ergodic」→「Mean Ergatic／meanerguided／minergatic／mean or guarded／miner got it／米尔·嘎丁」，「Papoulis」→「populis／Popolis」，「Riemann integrable」→「Ryman Integral／Reyman-Integrable」，「Chebyshev」→「Chabyshev」，「autocovariance」→「Auto Covariance／autocovarian／autocovalent」，「wide-sense stationary」→「Y-Send Station／Wisen Station」，「lemma」→「Lamma／lama」，「Slutsky」→「Sylasky／Slasky／Selasky／Slaski」，「Cauchy–Schwarz inequality」→「Colch-Swast Inequality／Culture Swatch Iniquity」，「趨近於 0」→「曲菌磷／趨均於0／區區無限大」，「ε」→「absence／Epson」，「sufficient condition」→「sufficiency condition」，「sinc」→「sync」，「Poisson sum formula」→「poison sum formula」，「indicator function」→「indicator function」，「駐波」→「鑄波」，「regular process」→「regular random process」，「predictable」→「predictable」。以下一律用正確的字。

> **接上一集**：上一集講了 ergodic 的原始定義和混淆。這集課本**換一個新名詞**——mean-ergodic——直接用結果來定義。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Papoulis 的新名詞：mean-ergodic](#1-papoulis-的新名詞mean-ergodic)
- [2. Example 12-1：常數隨機變數](#2-example-12-1常數隨機變數)
- [3. 時間平均的變異數（引理）](#3-時間平均的變異數引理)
- [4. Slutsky 定理：拿掉三角波](#4-slutsky-定理拿掉三角波)
  - [4.1 必要性（Cauchy–Schwarz）](#41-必要性cauchyschwarz)
  - [4.2 充分性（三角波變成積分）](#42-充分性三角波變成積分)
- [5. 充分條件](#5-充分條件)
- [6. 離散版本與例子](#6-離散版本與例子)
- [7. 頻譜詮釋](#7-頻譜詮釋)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| mean-ergodic 定義、Example 12-1 | [▶ 00:00](https://youtu.be/onZdVKEBZpg?t=0) | 式 (12-1)，pp. 523–524 |
| 變異數引理 | [▶ 07:09](https://youtu.be/onZdVKEBZpg?t=429) | 式 (12-4)、(12-5)，pp. 524–525 |
| Slutsky 定理 | [▶ 13:16](https://youtu.be/onZdVKEBZpg?t=796) | Theorem 12-1，pp. 526–527 |
| 充分條件 | [▶ 24:29](https://youtu.be/onZdVKEBZpg?t=1469) | 式 (12-9)、(12-10)，p. 527 |
| 離散 | [▶ 29:37](https://youtu.be/onZdVKEBZpg?t=1777) | Theorem 12-2、Example 12-6，p. 528 |
| 頻譜詮釋 | [▶ 34:44](https://youtu.be/onZdVKEBZpg?t=2084) | 式 (12-15)–(12-18)、Example 12-7，pp. 529–530 |

---

## 1. Papoulis 的新名詞：mean-ergodic

[▶ 00:00](https://youtu.be/onZdVKEBZpg?t=0) 課本定義遍歷性時不從原始觀點看，而是**換一個名詞**：不定義 ergodic process，定義 **mean-ergodic process**——「我創一個新名詞，你不要跟過去的東西混淆」。老師說 Papoulis 夠大牌，這樣定義 OK，而且很聰明。

**時間平均**：
$$\eta_T=\frac1{2T}\int_{-T}^{T}X(t)\,dt\qquad\text{(12-1)}.$$
$\eta_T$ 是隨機變數（可能是 3、4、2，各有機率）。

> **mean-ergodic**：$T\to\infty$ 時 $\eta_T$ 趨近一個**常數**（那個常數叫 mean）。課本：$\sigma_T^2=\mathrm{Var}\,\eta_T\to0$，則 $\eta_T\to\eta$（均方意義）。
> **用結果來定義**；不要求 stationary、也不要求 WSS。

**有什麼用**【口頭】：我們想估計期望值。但不可能在同一個時間丟一萬次骰子——只能這個時間丟一次、下個時間丟一次。一秒丟一次，一天就 86400 次，用八萬多次平均。**實作上能做的只有時間平均**（每個時間只能量一次，不能同時有一萬台機器量）。

- 真正的平均是在**同一個時間**、把所有狀態（機率空間上的不同結果）都量過——實際上做不到。
- 時間平均是不是我們要的期望值？ergodic 就是要回答這個問題。

**Riemann 可積**【口頭】：$\eta_T$ 用長條正方形塞面積算積分，所以過程要 Riemann 可積才有意義；有些隨機過程不是。

---

## 2. Example 12-1：常數隨機變數

[▶ 04:36](https://youtu.be/onZdVKEBZpg?t=276)

> **Example 12-1**：$X(t)=c$，$c$ 是隨機變數（$c=3$ 就所有時間都是 3；$c=4$ 就都是 4；各有機率）。

- **是 stationary**：不隨時間改變。
- **不是 mean-ergodic**：平均出來一定是 $c$，是隨機變數，$c-\eta$ 不管 $\eta$ 怎麼取都不是 0。（老師更正自己：不是「量起來有時大有時小」——一旦觀察到就不會變了，但量之前不知道是多少。）
- **也不是原始定義的 ergodic**：原始定義的 ergodic 一定收斂到常數。只要不是 mean-ergodic，就不是 ergodic。
- stationary 保證時間平均收斂，但只保證收斂到**隨機變數**——這裡收斂到 $c$。

老師說：前一集花時間打基礎是有道理的，在這裡會更理解。

---

## 3. 時間平均的變異數（引理）

[▶ 07:09](https://youtu.be/onZdVKEBZpg?t=429) 現在討論 Chebyshev 那類問題：時間平均 $\eta_T$ 的變異數是多少？

**一般情況**（不假設平穩）：
$$\sigma_T^2=\frac1{4T^2}\int_{-T}^{T}\!\!\int_{-T}^{T}\left[R(t,s)-\eta(t)\eta^*(s)\right]dt\,ds.$$
（變異數 = 二階動差 − 平均平方。寫 $R(t,s)$ 就是因為沒假設平穩——mean-ergodic 本身和平穩無關。）

**WSS 時**（我們關心的通常是 WSS，只看二階）：平均是常數、自相關只跟時間差有關。老師說推導不難，但**結果很重要**，所以停一下：

**Step 1：變數變換** $u=t-s$。$t\in(-T,T)$ ⇒ $u\in(-T-s,\,T-s)$。

**Step 2：換積分順序**（$du\,ds\to ds\,du$）。積分區域是一個**平行四邊形**：$u$ 從 $-2T$ 到 $2T$。
- 下半 $u\in(-2T,0)$：$s$ 從 $-T-u$ 到 $T$。
- 上半 $u\in(0,2T)$：$s$ 從 $-T$ 到 $T-u$。
- 兩塊合起來，$s$ 的長度都是 $2T-|u|$（直角三角形面積那種形狀，$u$ 越接近 0 越大）。

**Step 3：** $\int_{-2T}^{2T}\left(1-\frac{|u|}{2T}\right)\frac{du}{2T}=1$，所以平均可以放進積分合併，得自共變異 $C(u)=R(u)-|\eta|^2$：

> **引理**：WSS 時
> $$\sigma_T^2=\frac1{2T}\int_{-2T}^{2T}C(u)\left(1-\frac{|u|}{2T}\right)du\qquad\text{(12-4)}.$$
> WSS 過程是 mean-ergodic **⇔** $\sigma_T^2\to0$：
> $$\frac1{2T}\int_{-2T}^{2T}C(u)\left(1-\frac{|u|}{2T}\right)du\xrightarrow[T\to\infty]{}0\qquad\text{(12-5)}.$$

**意思**：量流量、股市資料要做平均——平均會不會趨近常數？是不是量越多越準？要看**自共變異和一個三角波**（$-2T$ 到 $2T$，高度 1）相乘的積分平均，window 越大時是否趨近 0。

【課本補充】p. 525：$\sigma_T$ 也能決定信賴區間——由 Chebyshev 不等式，$\eta$ 在 $\eta_T\pm10\sigma_T$ 內的機率大於 0.99。Example 12-3：$C(\tau)=qe^{-c|\tau|}$，$\sigma_T^2=\frac{q}{cT}\left(1-\frac{1-e^{-2cT}}{2cT}\right)\to0$。Example 12-4：$X=\eta+\nu$，$\nu$ 白雜訊 $q\delta(\tau)$，$\sigma_T^2=\frac q{2T}$。式 (12-6)：$C(\tau)\to0$ 時 $\sigma_T^2\approx\frac{\tau_c}{T}C(0)$，$\tau_c$ 是相關時間。

---

## 4. Slutsky 定理：拿掉三角波

[▶ 13:16](https://youtu.be/onZdVKEBZpg?t=796) 前面的引理很直觀，像習題。但乘三角波有點麻煩。Slutsky（老師說是俄國人）發現**可以拿掉**：

> **Theorem 12-1（Slutsky）**：WSS 過程 $X(t)$ 是 mean-ergodic **⇔**
> $$\frac1T\int_0^TC(\tau)\,d\tau\xrightarrow[T\to\infty]{}0\qquad\text{(12-7)}.$$
> 只要看**自共變異總面積的平均**。

**直觀**【口頭】：如果自共變異永遠是正的，總面積是正的，這就不會成立。什麼時候成立？**有正有負，剛好對消**——自共變異比較像震盪的狀態。就像全班平均 60 分，代表有人高於、有人低於；全部都高於 60 分，平均不會是 60。要舉反例很簡單。

所以能不能量、量得準不準，完全看自共變異的性質。

**證明**：用上面的引理。要證兩個方向：沒有三角波的平均趨近 0 ⇔ 有三角波的趨近 0。

### 4.1 必要性（Cauchy–Schwarz）

[▶ 16:22](https://youtu.be/onZdVKEBZpg?t=982)

**Cauchy–Schwarz 不等式**：$\mathrm{Cov}^2[\eta_T,X(0)]\le\mathrm{Var}\,\eta_T\cdot\mathrm{Var}\,X(0)=\sigma_T^2C(0)$。

左邊：$\eta_T$ 和 $X(0)$ 的共變異，代 $\eta_T$ 的定義，期望值和積分互換：
$$\mathrm{Cov}[\eta_T,X(0)]=\frac1{2T}\int_{-T}^{T}C(t)\,dt.$$
這剛好是要的量。若 mean-ergodic（$\sigma_T\to0$），上界趨近 0，它也趨近 0。∎

### 4.2 充分性（三角波變成積分）

[▶ 18:24](https://youtu.be/onZdVKEBZpg?t=1104) 倒回來比較麻煩。

**Step 1**：(12-7) 趨近 0 ⇒ 給 $\varepsilon>0$，存在很大的 $T_0$，window 比它大時平均一定很小：
$$\frac1t\int_0^tC(\tau)\,d\tau<\varepsilon\quad\Leftrightarrow\quad\int_0^tC(\tau)\,d\tau<t\varepsilon,\quad t>T_0$$
（最多線性遞增）。

**Step 2**：變異數（用 $C$ 對稱，寫成單邊）：
$$\sigma_T^2=\frac1{T}\int_0^{2T}C(\tau)\left(1-\frac{\tau}{2T}\right)d\tau=\frac1{2T^2}\int_0^{2T}C(\tau)(2T-\tau)\,d\tau.$$

**Step 3：關鍵技巧——把三角波變成積分** [▶ 19:56](https://youtu.be/onZdVKEBZpg?t=1196)：
$$2T-\tau=\int_\tau^{2T}dt.$$
變成雙重積分，**對調積分順序**（橫的變直的）：
$$\int_0^{2T}C(\tau)(2T-\tau)\,d\tau=\int_0^{2T}\left[\int_0^{t}C(\tau)\,d\tau\right]dt.$$
三角波不見了，裡面就是沒有三角波的積分。老師說：這個技巧沒有觀念，是數學分析的技巧，他好幾篇論文的推導都用到；看人家推導看起來簡單、看完沒感覺，但抓到重點，自己分析時就會想到能不能用上去。技巧是累積的學習。

**Step 4：切成兩段** $(0,2T_0)$ 和 $(2T_0,2T)$：
- 前段：WSS 的自共變異最大值在原點，$|C(\tau)|\le C(0)$（大學部通訊系統導論證過：$E|X(t+\tau)-X(t)|^2\ge0$ 展開四項，兩項 $\tau$、兩項 0），所以內層積分 $\le tC(0)$，是常數的積分。
- 後段：內層積分 $<t\varepsilon$（線性），積出來是 $t^2$ 的多項式。
$$\sigma_T^2<\frac{2T_0}{T}C(0)+\frac{\varepsilon}{2T^2}\int_{2T_0}^{2T}t\,dt\ \xrightarrow[T\to\infty]{}\ 0+\varepsilon.$$
（課本 p. 527 的係數寫法不同，得到 $2\varepsilon$；常數倍不影響結論。）

**Step 5**：$\varepsilon$ 可以任意小，左邊和 $\varepsilon$ 無關 ⇒ $\sigma_T^2\to0$。∎

**結論**：驗證過程是否 mean-ergodic，只要看自共變異在 window 越大時面積平均會不會是 0。很多時候碰到的不會是 0，那就不能量（預期量到常數是不行的）。

---

## 5. 充分條件

[▶ 24:29](https://youtu.be/onZdVKEBZpg?t=1469) if and only if 的條件等於是定義；有時希望用比較**容易檢測**的條件（充分條件的意義就在這裡）。

> **充分條件**：
> (a) $\int_0^\infty|C(\tau)|\,d\tau<\infty$（總面積有限）⇒ mean-ergodic（式 (12-9)）；
> (b) $C(\tau)\to0$（$\tau\to\pm\infty$）⇒ mean-ergodic（式 (12-10)）。

⚠️ 逐字稿缺字：老師說投影片要修正——(b) 要寫**絕對值** $|\tau|\to\infty$，兩端（$+\infty$ 和 $-\infty$）都要是 0。

**自共變異的詮釋**【口頭】：兩個不同時間相互的能量影響——這個時間的值，對隔 $\tau$ 的時間影響衰減多少。$\tau\to\infty$ 時影響慢慢消失，你就可以量。反例：有人受傷十年還記得——「那一年跟我借一支鉛筆沒還，十年後還記得要報仇」，這樣就不是 ergodic，這個人沒辦法量。

**(a) ⇒ (b)**：總面積有限，無限遠處一定是 0（否則無限遠還有高度、底又無限長，會爆掉）。所以只要證 (b)，(a) 也就對了；而且 (b) 比較好驗證。

**證明 (b)**：存在 $T_0$，$\tau>T_0$ 時 $|C(\tau)|<\varepsilon$（極限定義的延伸）。切 $T_0$ 以內和以外：
$$\frac1T\int_0^TC(\tau)d\tau=\frac1T\int_0^{T_0}C\,d\tau+\frac1T\int_{T_0}^{T}C\,d\tau<\frac{T_0}{T}C(0)+\frac{T-T_0}{T}\varepsilon\ \to\ \varepsilon.$$
（裡面用 $C(0)$ 最大，外面是很小的常數。）$\varepsilon$ 任意小，由 Slutsky 定理得證。∎

【課本補充】p. 527 Example 12-5：$X(t)=a\cos\omega t+b\sin\omega t+c$，$a,b$ 不相關、零平均、同變異數，$C(\tau)=\sigma^2\cos\omega\tau$，$\frac1T\int_0^TC=\frac{\sigma^2}{\omega T}\sin\omega T\to0$，是 mean-ergodic——正是「有正有負、震盪對消」的例子。註：$\eta_T$ 不偏但不是最好的，用加權平均 $\int w(t)X(t)dt$ 可以得到更小的變異數。

---

## 6. 離散版本與例子

[▶ 29:37](https://youtu.be/onZdVKEBZpg?t=1777) 有時只能量離散點，沒辦法連續量測：
$$\eta_M=\frac1N\sum_{n=-M}^{M}X[n],\quad N=2M+1\qquad\text{(12-11)}$$
（用 $\frac1{2M+1}$ 準確一點，用 $\frac1{2M}$ 也 OK）。趨近常數就定義為 mean-ergodic。

$$\sigma_M^2=\frac1N\sum_{m=-2M}^{2M}C[m]\left(1-\frac{|m|}{N}\right)\qquad\text{(12-12)}$$
（老師說是習題，請同學自己算。）

> **Theorem 12-2（Slutsky，離散）**：$X[n]$ 是 mean-ergodic ⇔ $\frac1M\sum_{m=0}^{M}C[m]\to0$（式 (12-13)）。

證明方法完全一樣（找 $T_0$、Cauchy–Schwarz）。Slutsky 把三角形的「濾波器」拿掉，這個技巧在不同領域的證明都有看到。充分條件也一樣：$C[m]\to0$ 就是 mean-ergodic。大 $M$ 時 $\sigma_M^2\approx\frac1M\sum_{m=0}^{M}C[m]$（式 (12-14)）。

**Example 12-6** [▶ 31:39](https://youtu.be/onZdVKEBZpg?t=1899)：
- **(a) 白雜訊**（零平均，$C[m]=P\delta[m]$）：$m\ge1$ 都是 0 ⇒ 一定是 mean-ergodic。估計的變異數只有 $u=0$ 留下：$\sigma_M^2=\frac PN$。
- **(b) $C[m]=Pa^{|m|}$**（濾波器做出來的過程，$|a|<1$；$|a|>1$ 就爆掉）：指數遞減、非常快 ⇒ 一看就知道是 mean-ergodic，不用計算。$\sigma_M^2\approx\frac{P(1+a)}{N(1-a)}$。

**觀察**【口頭】：
- 大部分正常碰到的自共變異（扣掉平均後），$\tau\to\infty$ 都是 0，通常指數遞減、衰減還蠻快——大部分過程是 mean-ergodic。
- 估計的變異數大部分是 **$\frac1T$ 的衰減**（和 window 成反比）。
- 可以故意造一個衰減很慢的自共變異，變異數就衰減很慢——要量很準，window 要非常非常大。

【課本補充】p. 528：(b) 若改用白雜訊的 $N_1$ 項平均，變異數 $\frac P{N_1}$ 等於 $\sigma_M^2$ 時 $N_1=N\frac{1-a}{1+a}$。p. 529 Sampling：連續過程數值估計時，用 $N$ 個取樣的平均 $\eta_N$，變異數 $\frac1{N^2}\sum\sum C(t_n-t_k)$。

---

## 7. 頻譜詮釋

[▶ 34:44](https://youtu.be/onZdVKEBZpg?t=2084) 前面都在時域看自共變異；Slutsky 的貢獻是只要看面積就好，原始是要乘上三角形的波形（像過濾器）。

**三角波 $1-\frac{|u|}{2T}$ 的傅立葉轉換是 $\mathrm{sinc}^2$**（老師說同學要有這個敏感度）。所以：

> **頻譜版**：令共變異頻譜 $S^c(\omega)=S(\omega)-2\pi\eta^2\delta(\omega)$（扣掉平均），
> $$\sigma_T^2=\frac1{2\pi}\int_{-\infty}^{\infty}S^c(\omega)\frac{\sin^2T\omega}{T^2\omega^2}\,d\omega\qquad\text{(12-16)}.$$
> 是共變異頻譜和 $\mathrm{sinc}^2$ 相乘的積分；$T$ 越大，sinc 越窄、越集中在原點（都是正的，因為平方）。

**推導**：積分範圍放到 $-\infty$ 到 $\infty$（加指示函數限制非零範圍）；自共變異轉到頻譜多一個積分，三角波轉成 $\mathrm{sinc}^2$；三個積分對調，出現 Poisson 求和公式的**積分版**（指數函數積分 = delta）；delta 和一個積分對消。老師說要記的不是公式，是概念：時域乘三角波 = 頻域乘 $\mathrm{sinc}^2$ 積分；而 Slutsky 告訴我們三角波可以拿掉。

**有脈衝就不是 mean-ergodic** [▶ 37:45](https://youtu.be/onZdVKEBZpg?t=2265)：WSS 過程 = regular + predictable（Wold）。有 predictable 部分就有駐波、**共變異頻譜在原點有脈衝**（卡在原點）。
- 頻譜非負，sinc² 也非負，積分是正的。
- 脈衝 $2\pi k_0\delta(\omega)$ 代進去要代 $\omega=0$，得一個正數 $k_0$。
- 正數加正數，不管 $T$ 多大都不會趨近 0（呼應 Slutsky：平均要是 0 一定有正有負，全是正的不行）⇒ **一定不是 mean-ergodic**。

【課本補充】p. 529：若 $X$ 是 regular，$S^c$ 在原點沒有脈衝，$T$ 大時 $S^c(\omega)\approx S^c(0)$，$\sigma_T^2\approx\frac{S^c(0)}{2T}\to0$（式 (12-17)）；若 $S^c=S_1^c+2\pi k_0\delta(\omega)$，$\sigma_T^2\approx\frac{S_1(0)}{2T}+k_0\to k_0$（式 (12-18)）。p. 530 Example 12-7：$Y=aX$（Example 11-12）有 $2\pi\sigma_a^2\eta_x^2\delta(\omega)$，不是 mean-ergodic。mean-ergodic 的等價條件：(1) $\sigma_T\to0$；(2) Wold 分解的常數項 $c_0=0$；(3) 積分頻譜 $F^c(\omega)$ 在原點連續；(4) $Z(\omega)$ 在原點連續。

**為什麼第 12 章全部討論 regular process**【口頭】：predictable 部分出現時，實際量測很討厭——變異數不會趨近 0。regular 過程的共變異頻譜一定沒有脈衝，不會出現這個現象（但是不是 mean-ergodic 還要再看）；有脈衝就一定不是。所以整個東西前後串在一起，不是獨立的觀念——這也是為什麼要定義 regular process。

---

## 8. 一頁速查表

| 項目 | 公式／條件 |
|---|---|
| 時間平均 | $\eta_T=\frac1{2T}\int_{-T}^TX(t)dt$ |
| mean-ergodic | $\eta_T\to$ 常數（用結果定義；不需平穩） |
| 變異數（WSS） | $\sigma_T^2=\frac1{2T}\int_{-2T}^{2T}C(u)\left(1-\frac{\lvert u\rvert}{2T}\right)du$ |
| Slutsky | mean-ergodic ⇔ $\frac1T\int_0^TC(\tau)d\tau\to0$ |
| 充分條件 | $\int_0^\infty\lvert C\rvert<\infty$ ⇒ $C(\tau)\to0$ ⇒ mean-ergodic |
| 離散 | $\frac1M\sum_0^MC[m]\to0$ |
| 頻譜 | $\sigma_T^2=\frac1{2\pi}\int S^c(\omega)\frac{\sin^2T\omega}{T^2\omega^2}d\omega$；$S^c$ 原點有脈衝 ⇒ 不是 |

**關鍵步驟**：
- 引理：$u=t-s$，平行四邊形換順序，長度 $2T-\lvert u\rvert$。
- Slutsky 必要：$\mathrm{Cov}^2[\eta_T,X(0)]\le\sigma_T^2C(0)$。
- Slutsky 充分：$2T-\tau=\int_\tau^{2T}dt$，對調順序拿掉三角波，切 $2T_0$，用 $\lvert C\rvert\le C(0)$。
- 例：白雜訊 $\sigma_M^2=\frac PN$；$Pa^{\lvert m\rvert}$ 得 $\frac{P(1+a)}{N(1-a)}$；大多 $\frac1T$ 衰減。
- Example 12-1：$X=c$ 平穩但不 mean-ergodic。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| mean-ergodic、Slutsky | 下一集：covariance-ergodic（變異數、自相關的估計） |
| regular 過程、無脈衝 | 第 34–36 集頻譜估計 |
| $\frac1T$ 衰減、加權平均 | 頻譜估計的 window |

---

## 附：本集一句話總結

> **Papoulis 用結果定義 mean-ergodic（時間平均趨近常數）；WSS 時時間平均的變異數是自共變異乘三角波的積分平均，Slutsky 定理說三角波可以拿掉——只要自共變異面積平均趨近 0（有正有負對消，或 $C(\tau)\to0$）就能用時間平均估計期望值；頻譜上，共變異頻譜在原點有脈衝（Wold 的 predictable 部分）就一定不是 mean-ergodic。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 12-1 (1/3) 錄影逐字稿（whisper large-v3-turbo，40:26）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
