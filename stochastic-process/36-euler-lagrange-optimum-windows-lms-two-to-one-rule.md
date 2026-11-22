---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 36
lecture: Lec 12-2 Spectrum Estimation — Spectrum Estimation (3/3)
date: 待補
video: https://youtu.be/el_HQoB6ox4
notes: Papoulis & Pillai 4th ed. §12-2 Optimum Windows（式 (12-62)–(12-73)，pp. 545–548）；§10-6 smoothing（式 (10-73)–(10-75)）
---

# 第 36 集 · Lec 12-2 (3/3)：泛函與 Euler–Lagrange 方程、最小 bias 的 data window（截斷 cosine）、最小 bias 的 spectral window（Papoulis window）、LMS spectral window 與 2 比 1 法則 [▶ 影片](https://youtu.be/el_HQoB6ox4)

← 上一集：[35](35-smoothed-spectrum-variance-window-tradeoff-bartlett-tukey-papoulis.md) ｜ [總目錄](README.md) ｜ 下一集：[37](37-mean-square-estimation-orthogonality-principle-terminology-wide-sense-markov.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 36 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（51:57，whisper large-v3-turbo）＋ Papoulis §12-2（pp. 545–548）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「泛函」→「範函」，「functional analysis」→「Functional Analysis」，「truncated cosine」→「troncated cosine」，「Papoulis」→「popolis／Propolis」，「Taylor expansion with remainder」→「態勒展開式／cater expansion with remainder」，「Lagrange multiplier」→「Lagrange Motiplyer」，「Parseval's theorem」→「Persifor's Theorem／partible theorem」，「Euler–Lagrange」→「Uder-Lagrange／Lagrange Euler／Uler-Lagrange」，「微分方程」→「五元方程／二次平衡方式／二次的偏微分方程式」，「實數」→「時數」，「bias」→「BIOS」，「least mean square」→「lead mean square／less mean square／List mean Square／LISMINE SQUARE」，「two-to-one rule」→「2,2,1,入我／2-2-1 rule／221 rule／2-1-rule」，「rule of thumb」→「rule of thumb」，「Turbo code」→「Turbo-Coding」，「LDPC code」→「LDP-Code」，「Gaussian approximation」→「高選 apprasimation」，「moving average」→「moving average」，「mean value theorem」→「mean value theorem」，「white」→「壞的」，「non-stationary white」→「non-stationary white」，「sinc」→「Sync」，「Gaussian」→「高資／高選」。以下一律用正確的字。

> **接上一集**：上一集看到 bias 和 variance 的取捨，也看到 Papoulis 的 window 最好。這集用**泛函**的工具——Euler–Lagrange 方程——推出最佳 window，最後講 LMS 估計和 2 比 1 法則。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 最小 bias 的 data window：把問題寫出來](#1-最小-bias-的-data-window把問題寫出來)
  - [1.1 二次近似（Taylor）](#11-二次近似taylor)
  - [1.2 對照第 21 集](#12-對照第-21-集)
  - [1.3 轉到時域](#13-轉到時域)
- [2. Euler–Lagrange 方程](#2-eulerlagrange-方程)
  - [2.1 用它重做第 21 集](#21-用它重做第-21-集)
- [3. 解最佳 data window：截斷 cosine](#3-解最佳-data-window截斷-cosine)
- [4. 最小 bias 的 spectral window：Papoulis window](#4-最小-bias-的-spectral-windowpapoulis-window)
- [5. LMS spectral window](#5-lms-spectral-window)
  - [5.1 MSE = bias² + variance](#51-mse--bias²--variance)
  - [5.2 模型：要估的對象加白雜訊](#52-模型要估的對象加白雜訊)
  - [5.3 例：moving average window 與 2 比 1 法則](#53-例moving-average-window-與-2-比-1-法則)
  - [5.4 最佳 window 跟 $\omega$ 有關](#54-最佳-window-跟-omega-有關)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 最小 bias data window 的問題 | [▶ 00:00](https://youtu.be/el_HQoB6ox4?t=0) | 式 (12-62)–(12-64)，p. 545 |
| Euler–Lagrange | [▶ 10:14](https://youtu.be/el_HQoB6ox4?t=614) | 無（課本只說「可以證明」） |
| 截斷 cosine | [▶ 16:55](https://youtu.be/el_HQoB6ox4?t=1015) | 式 (12-65)，p. 545 |
| Papoulis spectral window | [▶ 23:20](https://youtu.be/el_HQoB6ox4?t=1400) | 式 (12-66)–(12-69)，p. 546 |
| LMS、2 比 1 法則 | [▶ 27:57](https://youtu.be/el_HQoB6ox4?t=1677) | 式 (12-70)–(12-73)，pp. 546–548 |

---

## 1. 最小 bias 的 data window：把問題寫出來

[▶ 00:00](https://youtu.be/el_HQoB6ox4?t=0) 開始講**泛函** (functional analysis)。為什麼有用：設計 window 有很多情況，不是只有第 11 章之前直接用多項式做最好設計那種。

什麼都不給，很難設計最好的 window——什麼是「最好」？data window 要 minimize bias。data window 的效果：$C(\omega)$ 取絕對值平方後和頻譜做卷積。要證明：在某個條件下，最好的是 **truncated cosine data window**（從 $-T$ 到 $T$ 切掉的 cosine；老師說它其實就是 Papoulis window 的一種，⚠️ 見 §4 的說明）。

### 1.1 二次近似（Taylor）

[▶ 01:32](https://youtu.be/el_HQoB6ox4?t=92) 假設要估的對象可以用**二次式**近似（多項式；也可以三次、四次、五次，先從二次開始）：
- 一次太粗糙（用直線估）；用拋物線逼近，有個轉折，稍微好一點；一般做到二次就很準了。
- 最好的拋物線做法之一是 **Taylor 展開**到二次（with remainder，大一微積分下學期；三次項要夠小才準）。
- 精密工業要非常準時，有人做到六次，波形已經逼近得非常準。

$$S(\omega-\alpha)\approx S(\omega)-\alpha S'(\omega)+\frac{\alpha^2}{2}S''(\omega).$$

**加條件**：
1. window 在頻譜上**左右對稱**（所以才調成 $-T$ 到 $T$）：對稱波形乘 $\alpha$ 兩邊一積是 0，**一次項不見了**。
2. **總面積是 1**（最好逼近 delta）：第一項就留下 $S(\omega)$。

所以 bias：
$$B_c(\omega)=\frac1{2\pi}\int S(\omega-\alpha)\frac{C^2(\alpha)}{2T}d\alpha-S(\omega)\approx\frac{S''(\omega)}{4\pi}\cdot\frac{1}{2T}\int\alpha^2C^2(\alpha)\,d\alpha\qquad\text{(12-63)}.$$
（老師說這不是 Papoulis 做的，大家都這樣做。）bias 拆成兩個因子：只跟 $S$ 有關的 $S''(\omega)$，和只跟 $C$ 有關的二階動差。所以只要 **minimize 二階動差**：
$$M_2=\frac{1}{2\pi}\int\omega^2C^2(\omega)\,d\omega=\int_{-T}^{T}|c'(t)|^2dt\qquad\text{(12-64)}.$$
（定理 9-2 的概念：經過 $(j\omega)^2$ 的濾波器——$j\omega$ 是**微分器**——所以時域是微分的絕對值平方的積分。）

### 1.2 對照第 21 集

[▶ 05:07](https://youtu.be/el_HQoB6ox4?t=307) 這種題目做過類似的：第 10 章（第 21 集，式 (10-73)–(10-75)）設計 detection（平滑）濾波器：
- 條件：濾波器總面積 1、對稱、$\int\tau^2h(\tau)d\tau$ 是常數；
- minimize $\frac{N_0}{2}\int h^2$；用 Lagrange 乘數、微分是 0。

這裡一樣：
- 條件一：$\frac1{4\pi T}\int C^2(\omega)d\omega=1$；
- 條件二：data window 對稱；
- minimize $M_2$。

都是泛函要做的事：**找一個函數**，有一些等號條件，minimize 某個量。

### 1.3 轉到時域

[▶ 07:10](https://youtu.be/el_HQoB6ox4?t=430) 直接做有點困難，轉到時域設計：
- **條件一**：用 **Parseval 定理**（時域絕對值平方的積分 = 頻譜絕對值平方的積分），頻譜總積分 1 ⇔ 時域 $\int_{-T}^{T}c^2(t)dt=2T$（依此處的歸一化）。
- **條件二**：頻譜對稱——假設 $c(t)$ 是**實數**。實數的傅立葉轉換是共軛對稱；取了絕對值，只要時域是實數，頻譜對稱自動成立。
- **目標**：minimize $\int|c'(t)|^2dt$。

變成泛函問題。泛函問題很難（是很難的定理），但我們是工程師，要用的是結果。

---

## 2. Euler–Lagrange 方程

[▶ 10:14](https://youtu.be/el_HQoB6ox4?t=614) **加條件**：
- $c(t)$ **非負**——為什麼？它是純實數，希望把**絕對值拿掉**（有正有負有時候討厭，這樣比較簡單）。
- **邊界條件**：$c(\pm T)=0$。通常不希望設計一個在邊界跳起來的濾波器（很難設計），希望在 $-T$ 和 $T$ 都是 0。

**Lagrange 乘數** (multiplier) 法：把要 minimize 的量減掉 $\lambda$ 乘條件（$\lambda$ 叫 multiplier；Lagrange 發明的）。$\int c^2=2T$ 是常數，所以那項乘不乘結果一樣。整理成
$$\int_{-T}^{T}L\,dt,\qquad L(t,c,c')=c'^2(t)-\lambda c^2(t).$$
$L$ 是 $t$ 的函數，也是**函數 $c(t)$ 的函數**、也是 $c'(t)$ 的函數——函數的函數（$c$ 改變，整個 $L$ 就改變）。

> **Euler–Lagrange 方程**：要 optimize $\int L(x,f,f',\dots,f^{(k)})\,dx$，極值一定在
> $$\frac{\partial L}{\partial f}-\frac{d}{dx}\frac{\partial L}{\partial f'}+\frac{d^2}{dx^2}\frac{\partial L}{\partial f''}-\cdots=0$$
> 的地方（到 $k$ 次），再代邊界條件就做完了。

**直觀**：微積分教過 minimize $f(x)$，極值在 $f'(x)=0$。這裡一樣，只是對**函數** $f$ 做（偏）微分：對 $f$ 偏微分，減去「對 $f'$ 偏微分後再對 $x$ 微分」，加上「對 $f''$ 偏微分後對 $x$ 微分兩次」……

老師說：這是蠻難、蠻重要的定理，不容易證，直接用結果就好；修到數學所的泛函課應該會看到。如果把**函數也當作變數**來看，問題就解決了。

### 2.1 用它重做第 21 集

[▶ 13:51](https://youtu.be/el_HQoB6ox4?t=831)
$$L=\frac{N_0}{2}h^2(\tau)-\lambda_1h(\tau)-\lambda_2\tau^2h(\tau).$$
$L$ 跟 $\tau$、$h$ 有關，沒有 $h'$、$h''$，只要做第一項：
$$\frac{\partial L}{\partial h}=N_0h(\tau)-\lambda_1-\lambda_2\tau^2=0\ \Rightarrow\ h(\tau)=\frac{\lambda_1+\lambda_2\tau^2}{N_0}.$$
最好的設計就是多項式——直接用 Euler–Lagrange，非常快。

---

## 3. 解最佳 data window：截斷 cosine

[▶ 15:54](https://youtu.be/el_HQoB6ox4?t=954)（綠色是補充，課本不見得有細節。）

**Step 1：Euler–Lagrange。** $L=c'^2-\lambda c^2$：
- 對 $c$ 偏微分（$c'$ 當常數）：$-2\lambda c(t)$。
- 對 $c'$ 偏微分：$2c'(t)$；再對 $t$ 微分：$2c''(t)$。
$$-2\lambda c(t)-2c''(t)=0\ \Rightarrow\ c''(t)+\lambda c(t)=0.$$
又回到微分方程（大二學的）——第 27 集解 Wiener 過程特徵函數時解過一模一樣的式子。

**Step 2：解的形式。** 二階常係數方程的解是兩個函數的組合，看 $\lambda$ 的正負（負：指數；0：比較簡單）。這裡 $\lambda>0$，令 $\lambda=k^2$：
$$c(t)=c_1\cos kt+c_2\sin kt.$$

**Step 3：邊界條件** $c(\pm T)=0$：
$$c_1\cos kT+c_2\sin kT=0,\qquad c_1\cos kT-c_2\sin kT=0$$
（$t=-T$ 時 sin 的負號拉出來）。$a+b=a-b=0$ ⇒ $a=b=0$：
$$c_1\cos kT=0,\qquad c_2\sin kT=0.$$

**Step 4：四種情況。** 兩個相乘是 0，至少一個是 0：
- $c_1=c_2=0$：零函數，不要玩了，排除。
- $\cos kT=\sin kT=0$：不可能同時是 0（自己畫圖）。所以 $c_1,c_2$ 至少一個是 0。
- 要 $c(t)\ge0$：sin 一端往正、一端往負，不行 ⇒ **$c_2=0$**。

$$c(t)=c_1\cos kt.$$
要在 $(-T,T)$ 都是正的且端點為 0，剛好取半個週期：$k=\frac{\pi}{2T}$。

**Step 5：歸一化** $\int_{-T}^{T}c^2dt=2T$ ⇒ $c_1=\sqrt2$。

> **最佳（最小 bias）data window**：截斷 cosine
> $$c(t)=\sqrt2\cos\frac{\pi t}{2T},\quad|t|<T;\qquad C(\omega)\propto\frac{\cos T\omega}{\pi^2-4T^2\omega^2}.$$

【課本補充】p. 545：課本歸一化為 $\frac1{2\pi}\int C^2=1$（即 $\int c^2=1$），寫成 $c(t)=\frac1{\sqrt T}\cos\frac{\pi}{2T}t$，$C(\omega)=4\pi\sqrt T\frac{\cos T\omega}{\pi^2-4T^2\omega^2}$（式 (12-65)）。所得 $M_2=1$；不用 data window 時 $c=1$、$M_2=2$——最佳 data window 讓 **bias 減少 50%**。

**老師的總結** [▶ 21:14](https://youtu.be/el_HQoB6ox4?t=1274)：要解一個函數或濾波器，有一些條件，要 minimize 或 maximize 一個（在積分裡、有微分、二次、三次的）量——經過濾波器就會產生微分積分這些項——最標準的解法就是 **Euler–Lagrange 方程**。前提是假設要估的頻譜是多項式（二次）。有這麼好的工具，可以再推廣（例如讓 $c(t)$ 可以有正有負）。

老師順便說：通訊很喜歡用 raised cosine 濾波器，在某些方面是有道理的。

---

## 4. 最小 bias 的 spectral window：Papoulis window

[▶ 23:20](https://youtu.be/el_HQoB6ox4?t=1400) spectral window 主要是降 variance，但現在先找 bias 最小的。沒有 data window 時，bias 是頻譜和 spectral window 做卷積減 $S$。

**舉一反三**：一開始就給過公式——spectral window 和 data window 在頻譜上角色幾乎一樣，都是卷積；唯一差別是 data window 取絕對值平方，spectral window 沒有。所以最好的 spectral window 應該就是把絕對值、平方拿掉——觀念上很像。

**驗證**：一樣假設頻譜可用二次多項式逼近（係數不一定要是微分，反正是二次式）；window 左右對稱 ⇒ 一次項是 0：
$$B(\omega)\approx\frac{m_2}{2}S''(\omega),\qquad m_2=\frac1{2\pi}\int\omega^2W(\omega)\,d\omega\qquad\text{(12-66)}.$$
所以在總面積 1 的前提下，**minimize $m_2$**——顯示 $m_2$ 很重要：看 spectral window 時，**寬度 $m_2$ 決定 bias 的大小**。

條件：總積分 1、左右對稱、$W\ge0$（已經恆正）。和前面一樣，令 $W(\omega)=C^2(\omega)$（$2T$ 換成 $M$）：

> **最小 bias 的 spectral window（Papoulis window）**：
> $$w(t)=\frac1\pi\left|\sin\frac{\pi}{M}t\right|+\left(1-\frac{|t|}{M}\right)\cos\frac{\pi}{M}t,\quad|t|\le M\qquad\text{(12-68)},$$
> $$W(\omega)=8M\pi^2\frac{\cos^2(M\omega/2)}{(\pi^2-M^2\omega^2)^2}\qquad\text{(12-69)}.$$
> $w(t)=c(t)*c(-t)$。

課本用參數 $M$；把 $M$ 換成 $2T$ 就是老師的式子（cos 平方除以 $(\pi^2-4T^2\omega^2)^2$）。這是 Papoulis 發表的結果（Table 12-1 最後一個：高解析度時 bias 最小）。【口頭】如果被分配到 filter design 部門，很可能要面對繼續設計最好的 window。

⚠️ 老師在 §1 說「truncated cosine data window 其實是 Papoulis window」：課本裡 Papoulis window 指的是**spectral/lag window** (12-68)（它是截斷 cosine 和自己的卷積）；截斷 cosine 本身是最佳 **data** window (12-65)。兩者有關但不是同一個。

---

## 5. LMS spectral window

### 5.1 MSE = bias² + variance

[▶ 27:57](https://youtu.be/el_HQoB6ox4?t=1677) 沒辦法同時讓 bias 和 variance 變小，就做平衡——兩個相加最小：
$$e=B^2(\omega)+\mathrm{Var}\,S_w(\omega)\qquad\text{(12-70)}.$$
叫 **least mean square (LMS)**。

**為什麼叫 mean square**：
- $E(X-\bar X)^2$ 叫 variance。
- $E(X-\theta)^2$（$\theta$ 是要估的對象、$X$ 是拿來估的）不見得是 variance——叫 **mean square error**。
- unbiased 時兩者相等；biased 時不相等。
- $E(X-\theta)^2=(EX-\theta)^2+E(X-EX)^2$ = bias² + variance（展開後一項剛好消掉，都是等號）。

（上一集的 estimation variance 其實就是這個 MSE。）

### 5.2 模型：要估的對象加白雜訊

[▶ 30:34](https://youtu.be/el_HQoB6ox4?t=1834) 也可以用前面的 Euler–Lagrange 技巧，但這裡介紹另一種方式。

**Detection/estimation 最常見的模型**：觀察 $Y=\theta+N$——要估的對象加一個雜訊（相加模型），也是工程上最常碰到的。【口頭】老師最近審一篇論文也用這個模型：估計不太準，就把它當作「估計的對象 + 等效雜訊」——常用技巧。

**例：Turbo code 的高斯近似**【口頭】[▶ 34:11](https://youtu.be/el_HQoB6ox4?t=2051)：Turbo code（或 LDPC code）一發明就發現效能特別好——recursive、iterative，像兩個 turbo 來回修正。很難分析，數學上幾乎沒辦法 model，有人說它接近高斯行為（期望值加高斯），做了 Gaussian approximation 分析、得到一些結果；後來有人用實驗證明其實不像高斯，之前的結果都沒什麼用（但他們已經發表了）。所以用高斯近似是對是錯，要看應用對象。

**頻譜估計的情況**（沒有 data window、沒有 spectral window）：
$$S_T(\omega)=S(\omega)+\nu(\omega).$$
- 加一個常數只是**平移**，不改變 variance（大二機率）：$\mathrm{Var}S_T=\mathrm{Var}\nu$。
- **$\nu$ 零平均**（$T$ 大時 $S_T$ 不偏）。
- **$\nu$ 是白的**：用 Theorem 12-4 的強假設（高斯時成立；要估的 $X(t)$ 很不像高斯就不一定對）：
$$\mathrm{Cov}[S_T(u),S_T(v)]=\frac{1}{4T^2}\left[S_{YY}^2(u,-v)+S_{YY}^2(u,v)\right].$$
  - $T$ 大 ⇒ $\frac1T$ 很小 ⇒ $|u+v|\gg\frac1T$ 幾乎都成立 ⇒ $S_{YY}(u,v)\approx0$。
  - 故意留 $S_{YY}(u,-v)$：$u+v$ 大不代表 $u-v$ 大。它是 sinc 的積分（式 (12-47)）；$T$ 大時 sinc 很窄，積分有效範圍內 $S$ 近乎常數，提出來（老師說推理不嚴謹，但不見得是錯）。sinc 的積分剛好是 sinc（等號）：
$$\mathrm{Cov}\approx\frac{\sin^2T(u-v)}{T^2(u-v)^2}S^2(u)\to\frac{\pi}{T}S^2(u)\delta(u-v)\qquad\text{(12-57)}.$$
  - 觀念又出來了：**variance 就是功率頻譜的平方**，完全正比——有人做出來不是平方，就知道他的定義和一般人不一樣。

> 所以 $\nu(\omega)$ 是**非平穩白雜訊**，自相關 $\frac\pi TS^2(u)\delta(u-v)$。（非平穩白的另一個 domain 是 WSS——傅立葉轉換的兩個 domain，非常重要的規則。）

**sinc 的積分是 sinc 的證明**（下一頁細節）[▶ 40:54](https://youtu.be/el_HQoB6ox4?t=2454)：永遠記得——**sinc 在另一個 domain 是方波**（$-T$ 到 $T$ 都是 1），方波很好積；sinc² 是三角波。跑到另一個 domain 處理非常容易；然後積分互換（$dt_1dt_2df\to df\,dt_1dt_2$），出現 delta 消掉一個積分，又回到 sinc。老師說：這沒有觀念，純粹數學技巧；sinc 是通訊特別容易碰到的函數。

### 5.3 例：moving average window 與 2 比 1 法則

[▶ 32:04](https://youtu.be/el_HQoB6ox4?t=1924) **先講結果——2 比 1 法則 (two-to-one rule)**：

> 最好的 LMS 設計，**估計的標準差通常是 bias 的兩倍**。

- rule of thumb，不是定理（不一定完全正確）。以前做統計的「兩倍 sigma」概念。
- 看到別人做出 4 比 1、5 比 1，直覺是：是不是做得不好、還能改善？或者有額外條件讓它違反直覺、反而更好——要去探究。

**例**（artificial）[▶ 42:59](https://youtu.be/el_HQoB6ox4?t=2579)：
1. spectral window 是**方波**（moving average），寬度 $2\Delta$、高度 $\frac1{2\Delta}$（面積 1）——Daniell 早年用的。
2. 頻譜用**二次拋物線**近似（最常用）。
3. 用上面的模型：$\nu$ 零平均、白（非平穩白），variance 是 $\frac\pi TS^2$。

$$S_\Delta(\omega)=\frac1{2\Delta}\int_{-\Delta}^{\Delta}S_T(\omega-\alpha)\,d\alpha\qquad\text{(12-71)}.$$

**Bias**：代 $S_T=S+\nu$，$S(\omega-\alpha)\approx S-\alpha S'+\frac{\alpha^2}2S''$（Taylor，反正變成多項式）：第一項（面積 1）得 $S(\omega)$；第二項（對稱）是 0；剩平方項：
$$\text{bias}=\frac{1}{2\Delta}\int_{-\Delta}^{\Delta}\frac{\alpha^2}{2}S''\,d\alpha=S''(\omega)\frac{\Delta^2}{6}.$$

**Variance**：平移不改變 variance，只剩雜訊項；白的 ⇒ delta 和一個積分消掉，剩頻譜平方；用均值定理 (mean value theorem) 近似：
$$\mathrm{Var}\,S_\Delta(\omega)=\frac{1}{4\Delta^2}\int_{-\Delta}^{\Delta}\frac{\pi S^2(\omega)}{T}d\alpha=\frac{\pi S^2(\omega)}{2\Delta T}.$$

**MSE**：
$$e=\frac{\Delta^4}{36}\left[S''(\omega)\right]^2+\frac{\pi S^2(\omega)}{2\Delta T}\qquad\text{(12-72)}.$$
是 $\Delta$ 的多項式（加 $\frac1\Delta$）——對 $\Delta$ 微分等於 0 就能解出最好的 $\Delta$（結果有點不好看，但一定解得出來）：
$$\frac{\Delta^3}{9}[S'']^2=\frac{\pi S^2}{2\Delta^2T}\ \Rightarrow\ \Delta^*=\left(\frac{9\pi}{2T}\right)^{0.2}\left(\frac{S(\omega)}{S''(\omega)}\right)^{0.4}.$$
代回去：
$$\frac{\text{bias}}{\sqrt{\mathrm{Var}}}=\frac12.$$

**2 比 1 法則的用法** [▶ 49:13](https://youtu.be/el_HQoB6ox4?t=2953)：大部分情況下最好的設計都是 2 比 1。找不到最好的設計也沒關係，把 variance 和 bias 調到 2 比 1，結果大概不會太差（大家都是調 2 比 1）。若是 4 比 1，表示 variance 太大，要調小一點、讓 bias 大一點，慢慢調到 2 比 1。

**理解推導的價值**【口頭】：知道人家怎麼得到結論，就知道什麼時候不成立、什麼時候比較可能成立、什麼時候是例外。例如：高斯是很重要的假設——河川流量、股市交易很不像高斯，結果就不見得對；或者系統沒辦法 model 成「估計對象 + 雜訊」，結論也不對。

### 5.4 最佳 window 跟 $\omega$ 有關

[▶ 49:43](https://youtu.be/el_HQoB6ox4?t=2983) 推導裡有一個「不合理」的地方：最佳 $\Delta^*$ 是 **$\omega$ 的函數**。
- 設計一個濾波器估功率頻譜，但不同頻率點（量 1.8 GHz、量 1.9 GHz）最好的 window 不一樣大、調 2 比 1 的地方不一樣。
- 例：5G 不知道要用 70 GHz 還是 30 GHz，兩者最好的 window 大小 $\Delta^*$ 不同——跟當時的頻譜特性有關。
- 量測上麻煩：過程中要不停調 window 大小。

**最佳 spectral window 的形狀**（沒給細節）：同樣假設二次、相加雜訊模型、非平穩白，有人做出最好的結果——老師說是「三角波」。

⚠️ 兩邊說法不同：課本 p. 548 說最小化 MSE 的 window 是**截斷拋物線** (truncated parabola)，由 Priestley 提出：
$$S_w(\omega)=\frac{3}{4\Delta}\int_{-\Delta}^{\Delta}S_T(\omega-y)\left(1-\frac{y^2}{\Delta^2}\right)dy,\qquad\Delta=\left(\frac{15\pi}{T}\right)^{0.2}\left(\frac{S(\omega)}{S''(\omega)}\right)^{0.4}\qquad\text{(12-73)}.$$
老師說的「三角波」可能是口誤或字幕錯，待確認。課本也指出它跟頻率有關、大小是未知 $S$ 和 $S''$ 的函數，所以要先估 $S$ 和 $S''$，再決定下一步的 $\Delta$。

---

## 6. 一頁速查表

### 泛函工具

**Euler–Lagrange**：optimize $\int L(x,f,f',\dots)dx$ ⇒ $\frac{\partial L}{\partial f}-\frac{d}{dx}\frac{\partial L}{\partial f'}+\frac{d^2}{dx^2}\frac{\partial L}{\partial f''}-\cdots=0$。

### 最佳 window

| 目標 | 要 minimize | 結果 |
|---|---|---|
| bias（data window） | $M_2=\int\lvert c'\rvert^2$，s.t. $\int c^2$ 固定 | 截斷 cosine $c\propto\cos\frac{\pi t}{2T}$；bias 減 50% |
| bias（spectral window） | $m_2=\frac1{2\pi}\int\omega^2W$，s.t. 面積 1 | Papoulis window，$W=C^2$（$2T\to M$） |
| MSE（spectral window） | $B^2+\mathrm{Var}$ | 截斷拋物線（Priestley）；$\Delta$ 依 $\omega$ |

**關鍵步驟**：
- 二次近似 + 對稱 ⇒ bias $\approx\frac{S''}{2}\times$（二階動差）。
- $L=c'^2-\lambda c^2$ ⇒ $c''+\lambda c=0$ ⇒ $c_1\cos kt+c_2\sin kt$；$c(\pm T)=0$、$c\ge0$ ⇒ $c_2=0$、$k=\frac\pi{2T}$。
- 第 21 集重做：$\partial L/\partial h=N_0h-\lambda_1-\lambda_2\tau^2=0$。

### LMS 與 2 比 1

- $S_T=S+\nu$，$\nu$ 非平穩白：$\frac\pi TS^2(u)\delta(u-v)$。
- Moving average $2\Delta$：bias $=\frac{\Delta^2}6S''$，Var $=\frac{\pi S^2}{2\Delta T}$。
- 最佳：$\Delta^*\propto T^{-0.2}(S/S'')^{0.4}$；**標準差 = 2 × bias**。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| MSE、相加雜訊模型 | 下一集起：第 13 章 Mean Square Estimation |
| 正交原理、Wiener 濾波 | §13-1、13-2 |
| Euler–Lagrange | 最佳濾波器設計 |

---

## 附：本集一句話總結

> **把要估的頻譜做二次 Taylor 近似、window 取對稱且面積 1，最小化 bias 就變成最小化 window 的二階動差——用泛函的 Euler–Lagrange 方程解出最佳 data window 是截斷 cosine（bias 減半），最佳 spectral window 是它平方後的 Papoulis window；若要最小化 bias² + variance，把 periodogram 看成「真頻譜 + 非平穩白雜訊」，最佳設計會讓標準差約等於 bias 的兩倍（2 比 1 法則），而最佳 window 大小還跟頻率有關。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。
2. LMS 最佳 spectral window 的形狀：老師說「三角波」，課本說截斷拋物線（Priestley）。

---

*筆記依據陳伯寧老師「隨機過程」Lec 12-2 (3/3) 錄影逐字稿（whisper large-v3-turbo，51:57）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
