---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 18
lecture: Lec 10-3 Random Walks and Other Applications — Modulation (3/3)
date: 待補
video: https://youtu.be/pInAtXl6AHA
notes: Papoulis & Pillai 4th ed. §10-3 Frequency Modulation（Theorem 10-3 式 (10-155)–(10-160)、Theorem 10-4 Woodward's theorem 式 (10-161)–(10-164)、Normal processes 式 (10-165)–(10-169)，pp. 470–472）
---

# 第 18 集 · Lec 10-3 (3/3)：Woodward 定理（FM 頻譜 ≈ 瞬時頻率的分布）、高斯過程的兩種定義、高斯例子驗證、寬頻 vs 窄頻 FM [▶ 影片](https://youtu.be/pInAtXl6AHA)

← 上一集：[17](17-rice-optimal-hilbert-center-frequency-instantaneous-frequency-fm.md) ｜ [總目錄](README.md) ｜ 下一集：[19](19-cyclostationary-processes-time-average-pam.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 18 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（42:31，whisper large-v3-turbo）＋ Papoulis §10-3（pp. 470–472）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Woodward」→「Witworth／Wilworth／Vivor／WordWord」，「lemma」→「Lama／Lamma／類碼」，「wide-sense stationary」→「white 線／wise and stationary」，「zero mean」→「geo mean」，「穩態」→「穩泰」，「distribution」→「Detribution」，「Papoulis」→「Propoulis／Propolis／popolis」，「Riemann–Lebesgue」→「Reimann-Lebesgue」，「truncation」→「tuncation」，「sinc」→「sync」，「傅立葉轉換」→「負列轉換／复列转换」，「Gaussian」→「高宣／高圈／高斯」，「Gray & Davisson」→「Gray and Davidson」，「Haykin」→「Hacking／Hackings／Hagin」，「positive definite」→「Positive Deafening」，「existence theorem」→「Existent Theory／Existing Theorem」，「Lebesgue integrable」→「Lebert Integrable」，「weighted sum」→「Waited Sum」，「necessary exclusion」→「necessary exclusion」，「narrowband／wideband」→「nailband／yband」，「approximate」→「Aprosimate／apposimate／applysmate」，「Proakis」→「Prokey」。以下一律用正確的字。

> **接上一集**：上一集證明了 FM 訊號 $X=\text{Re}\,e^{j(\omega_0t+\lambda\int_0^tC+\varphi_0)}$ 在 $C$ 嚴格平穩時是零平均 WSS。這一集問它的**功率頻譜**長什麼樣子。第 12 集的引理說：頻率的 PDF 就是功率頻譜。Woodward 定理把這個習題級的觀察推廣成定理：**$\lambda$ 夠大時，FM 頻譜 ≈ 瞬時頻率的分布**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：引理與 FM 的平穩性](#1-回顧引理與-fm-的平穩性)
- [2. Woodward 定理](#2-woodward-定理)
  - [2.1 敘述](#21-敘述)
  - [2.2 證明：用一條直線逼近相位](#22-證明用一條直線逼近相位)
  - [2.3 Riemann–Lebesgue 引理](#23-riemannlebesgue-引理)
  - [2.4 老師的評價](#24-老師的評價)
- [3. 高斯過程的兩種定義](#3-高斯過程的兩種定義)
  - [3.1 Papoulis／Gray & Davisson 的定義](#31-papoulisgray--davisson-的定義)
  - [3.2 Haykin 的定義](#32-haykin-的定義)
  - [3.3 用 Haykin 定義證：高斯過程的積分是高斯](#33-用-haykin-定義證高斯過程的積分是高斯)
  - [3.4 兩個定義誰強](#34-兩個定義誰強)
- [4. 用高斯例子驗證 Woodward 有多準](#4-用高斯例子驗證-woodward-有多準)
- [5. 寬頻 FM vs 窄頻 FM](#5-寬頻-fm-vs-窄頻-fm)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 回顧引理、FM 平穩 | [▶ 00:00](https://youtu.be/pInAtXl6AHA?t=0) | Theorem 10-3，p. 470 |
| Woodward 定理與證明 | [▶ 03:07](https://youtu.be/pInAtXl6AHA?t=187) | Theorem 10-4，式 (10-161)–(10-164)，p. 471 |
| 高斯過程的定義 | [▶ 21:24](https://youtu.be/pInAtXl6AHA?t=1284) | §9-1 p. 386；Haykin |
| 高斯例子、寬頻／窄頻 | [▶ 33:11](https://youtu.be/pInAtXl6AHA?t=1991) | 式 (10-165)–(10-169)，pp. 471–472 |

---

## 1. 回顧：引理與 FM 的平穩性

[▶ 00:00](https://youtu.be/pInAtXl6AHA?t=0)

- **引理**（第 12 集）：給一個頻譜 $S(\omega)$，要造一個訊號以它為功率頻譜，直接的做法是 $e^{j(\omega t-\varphi)}$，$\omega$ 的 PDF 就是正規化的 $S(\omega)$（$S$ 非負，正規化成面積 1 就能當 PDF）。暗示：**瞬時頻率本身的機率分布，就是將來頻譜的樣子**。
- **FM 的平穩**（上一集）：資訊 $C(t)$ 要**嚴格平穩**，因為 $\varphi(t)=\int_0^tC$ 在不同時間積分的範圍不同；還要可積。$\varphi_0$ 和 $C$ 獨立、均勻，是為了讓平均不隨時間變（零平均）。$C$ 不是嚴格平穩，$\int_t^{t+\tau}C$ 的統計性質在不同 $t$ 會不一樣，就不是 WSS，也就很難算功率頻譜。

【課本補充】Theorem 10-3（p. 470）：若 $C$ 是 SSS、$\varphi_0$ 與 $C$ 獨立且 $E\{e^{j\varphi_0}\}=E\{e^{j2\varphi_0}\}=0$，則 $X$ 是零平均 WSS，
$$R_{XX}(\tau)=\tfrac12\text{Re}\,R_{ZZ}(\tau),\qquad R_{ZZ}(\tau)=R_{WW}(\tau)e^{j\omega_0\tau},\qquad R_{WW}(\tau)=E\{W(\tau)\},\ W(t)=e^{j\lambda\varphi(t)}.$$
**相位調變**時 $\varphi$ 的統計已知，$E\{W(t)\}=\Phi_\varphi(\lambda,t)$ 是 $\varphi(t)$ 的特性函數；**頻率調變**時只知道 $C$ 的統計，要求積分的統計，一般不容易——常態情形例外。

---

## 2. Woodward 定理

### 2.1 敘述

[▶ 03:07](https://youtu.be/pInAtXl6AHA?t=187) 課本的 Theorem 10-4，Papoulis 認為它是重要的定理。

> **Woodward 定理**：若 $C(t)$ **連續**、嚴格平穩，密度 $f_C(c)$ 有界，則 **$\lambda$ 夠大時**
> $$S_{XX}(\omega)\approx\frac{\pi}{2\lambda}\left[f_C\left(\frac{\omega-\omega_0}{\lambda}\right)+f_C\left(\frac{-\omega-\omega_0}{\lambda}\right)\right]\qquad\text{(10-161)}.$$

- $C$ 嚴格平穩，所以任何時間的分布都一樣，$f_C$ 就是它的 PDF。
- $C$ 是什麼？相位 $\lambda\varphi$ 的微分（除以 $\lambda$），也就是**頻率**（扣掉 $\omega_0$）。所以：**FM 訊號的功率頻譜 ≈ 瞬時頻率的分布，左右平移到 $\pm\omega_0$**，除以 $\lambda$ 只是縮放。
- 和引理是同一件事：引理的相位是 $\omega t$，微分剛好是 $\omega$；這裡的相位是 $\lambda\int C$，不再那麼漂亮，所以只能近似。
- 條件：**$\lambda$ 要夠大**（調變指數大、頻寬夠寬）才準；**$C$ 要連續**。

### 2.2 證明：用一條直線逼近相位

[▶ 07:09](https://youtu.be/pInAtXl6AHA?t=429)

**Step 1：用直線逼近。** 為什麼要連續？因為想把相位變成「$\omega t$」的樣子。$C$ 連續，在很小的範圍 $|\tau|<\tau_0$ 內 $C(t)\approx C(0)$，相位就用一條直線逼近：
$$\varphi(\tau)=\int_0^\tau C(\alpha)\,d\alpha\approx C(0)\,\tau=\bar{\varphi}(\tau)\qquad(|\tau|<\tau_0).$$
斜率 $C_0=C(0)$ 是隨機的。

**Step 2：兩個系統。** 原來的 $Z$（取實部得 $X$），和逼近的 $\bar Z=e^{j(\omega_0t+\lambda C_0t+\varphi_0)}$（取實部得 $\bar X$）。$\bar C(t)=C_0$ 不隨時間變，也是嚴格平穩。

**Step 3：算 $\bar Z$ 的自相關**（照算，代入相乘取期望值）：
$$R_{\bar Z\bar Z}(\tau)=e^{j\omega_0\tau}E\left\{e^{j\lambda C_0\tau}\right\}=e^{j\omega_0\tau}\Phi_C(\lambda\tau),$$
$\Phi_C(u)=E\{e^{juC}\}$ 是 $C$ 的特性函數。

**Step 4：認出傅立葉轉換。** 期望值就是把 $C_0$ 代某個數 $c$ 再乘機率積分——這就是 PDF 的（反）傅立葉轉換。Woodward 令 $u=\lambda c$，把 $\frac1\lambda$ 帶出來，變成純粹的傅立葉轉換形式：
$$S_{\bar Z\bar Z}(\omega)=\int e^{j\omega_0\tau}\Phi_C(\lambda\tau)e^{-j\omega\tau}d\tau=\frac{2\pi}{\lambda}f_C\left(\frac{\omega-\omega_0}{\lambda}\right).$$
（中間多一項常數的傅立葉轉換是 $2\pi\delta$，delta 積分把 $u=\omega-\omega_0$ 帶出來。）到這裡**都是等號**，就是引理：相位是 $\omega t$ 時，頻率的 PDF 就是功率頻譜。

**Step 5：** $\bar X$ 的頻譜用 Observation 4（$4S_{XX}(\omega)=S_{ZZ}(\omega)+S_{ZZ}(-\omega)$）：兩個疊加除以 4，得到 (10-161) 的右邊。還是等號。

**Step 6：Woodward 真正做的事——比較 $Z$ 和 $\bar Z$**（從習題變成定理的地方）[▶ 13:13](https://youtu.be/pInAtXl6AHA?t=793)：

- $|\tau|<\tau_0$：直線逼近曲線，兩者很接近。
- $|\tau|>\tau_0$：直線和曲線會差很多；但自相關是期望值，**兩者都很接近 0**。為什麼？
  - $R_{\bar Z\bar Z}$ 是 $\Phi_C(\lambda\tau)$：$C$ 有密度，由 Riemann–Lebesgue 引理，特性函數在引數趨於無限大時趨於 0。$\tau>\tau_0$ 且 $\lambda$ 很大，$\lambda\tau$ 很大，所以很小。
  - 原來的 $R_{ZZ}$ 也一樣（有 $\lambda$ 在裡面，$\lambda$ 很大）。
- 所以對所有 $\tau$，$R_{ZZ}\approx R_{\bar Z\bar Z}$，傅立葉轉換也近似。 ∎

【課本補充】Papoulis 的證明（p. 471）相同：$|\tau|<\tau_0$ 時 $E\{W(\tau)\}\approx E\{e^{j\lambda\tau C(0)}\}=\Phi_C(\lambda\tau)$；$\lambda$ 夠大時 $|\tau|>\tau_0$ 的 $\Phi_C(\lambda\tau)\approx0$，所以 (10-164) 對每個 $\tau$ 都是令人滿意的近似。

### 2.3 Riemann–Lebesgue 引理

[▶ 14:45](https://youtu.be/pInAtXl6AHA?t=885)

> 若隨機變數 $X$ 有密度 $f$（$f\ge0$，$\int f=1$），則特性函數 $\Phi(s)=\int f(t)e^{jst}dt\to0$，$|s|\to\infty$。

**證明的想法**（老師黑板上畫的）：

1. **截斷** (truncation)：$f$ 總面積是 1（有限），一定找得到夠大的 $A$，令 $g=f\cdot\mathbf{1}_{[-A,A]}$，使 $\int|f-g|$ 很小（外面幾乎是 0）。
2. 兩個特性函數的差：
$$\left|\int fe^{jst}dt-\int ge^{jst}dt\right|\le\int|f-g|\,dt\quad\text{（指數取絕對值就不見了）},$$
   很小。
3. $g$ 的特性函數：若 $g$ 有界、又是 $[-A,A]$ 上的「好」函數，$\int_{-A}^{A}e^{jst}dt=\frac{2\sin As}{s}$ 是 sinc 函數，以 $\frac1s$ 降到 0。（老師用 $\le g_{\max}\int_{-A}^{A}e^{jst}dt$ 的說法帶過。）

**同一件事的訊號觀點**【口頭】：任何**有限能量**的訊號，頻譜在頻率趨於無限大時一定趨於 0。這是極限的觀念——不會在某處突然掉成 0，只是趨近。

### 2.4 老師的評價

[▶ 12:42](https://youtu.be/pInAtXl6AHA?t=762)【口頭】

- 老師**不太喜歡**這個定理：它是近似 (approximation)，不夠精確；**沒告訴你 $\lambda$ 要多大**才好。$\lambda=30$ 夠不夠大？$50$ 呢？都不知道。
- 比喻：「夠用功就可以通過這門課」完全沒有量化；如果告訴你「至少讀 30 小時一定過」，你就會真的把 30 小時空出來。
- 所以它的重要性是給一個**定性**的概念（從引理延伸來的）：FM 訊號的頻譜就是頻率的分布。
- 怎麼把一個習題（引理）推廣成可發表的定理？這就是 Woodward 做的事。

---

## 3. 高斯過程的兩種定義

[▶ 21:24](https://youtu.be/pInAtXl6AHA?t=1284) 接下來要用高斯過程驗證 Woodward 有多準，先討論高斯過程。老師在第 9 章把不同書的定義拿出來比，目的是：每本書的定義都不一樣，要有自己的判斷，知道你需要什麼條件；科學研究，尤其工程，沒有絕對的標準，以應用為主。

### 3.1 Papoulis／Gray & Davisson 的定義

> **定義 1**：隨機過程是高斯的，若任何**有限個**樣本構成高斯隨機向量（聯合高斯）。

- Gray & Davisson 的書也用這個定義，和 Papoulis 完全一樣。老師說 Davisson、Gray 都是理論研究非常出色的學者，喜歡這個嚴謹的定義。
- 由這個定義可推：**存在定理**——給任何平均函數和非負定函數，就完全定義一個高斯過程。高斯過程可以用二階統計完全描述（第 6 集）。

### 3.2 Haykin 的定義

> **定義 2**（Haykin）：$X(t)$ 是高斯過程，若對**每一個**（Lebesgue 可積的）函數 $g(t)$，
> $$Y=\int g(t)\,X(t)\,dt$$
> 都是高斯隨機變數，即 PDF 為 $\frac{1}{\sqrt{2\pi}\sigma}e^{-(y-m)^2/(2\sigma^2)}$。

兩個定義形式上完全不一樣。可能還有第三種。

### 3.3 用 Haykin 定義證：高斯過程的積分是高斯

[▶ 25:01](https://youtu.be/pInAtXl6AHA?t=1501) Haykin 需要這個定義，是因為他後面的證明用它比較方便。老師說：老師要你證某個定理，用別本書的定義證不出來時，可以換一個方便證明的定義；但你還不夠有名，自己的定義別人可能 challenge，最好找一個已經有人這樣定義的來用。

> **命題**：$C(t)$ 是高斯過程 ⇒ $\varphi(s)=\int_0^sC(\theta)\,d\theta$ 是高斯過程。

- 用 Papoulis 的定義不好證：要取三個、五個樣本，證它們聯合高斯；知道 $C$ 有這個性質，但積分之後再取樣是不是也有？有點麻煩。
- 用 Haykin 的定義很快：對任何 $g$，交換積分順序（微積分的基本概念）：
$$\int g(s)\varphi(s)\,ds=\int g(s)\int_0^sC(\theta)\,d\theta\,ds=\int C(\theta)\underbrace{\left[\int_{s\ge\theta}g(s)\,ds\right]}_{G(\theta)}d\theta.$$
  $C$ 是高斯，乘上任何函數 $G$ 再積分都是高斯，所以 $\varphi$ 是高斯。 ∎

### 3.4 兩個定義誰強

[▶ 28:36](https://youtu.be/pInAtXl6AHA?t=1716)

- **Haykin ⇒ Papoulis**：取 $g$ 為 $n$ 個 delta 函數的加權和，$\int gX=\sum a_iX(t_i)$ 就是有限個樣本的任意線性組合。任意線性組合都是高斯 ⇔ 聯合高斯。所以 Haykin 的定義**比較廣**（能推出書上的定義）。
- **Papoulis ⇒ Haykin？** 有人說反過來也對（兩者等價），但這裡有點 tricky：
  - 有限個聯合高斯的線性組合是高斯（2 個、3 個、4 個都對）。
  - 但積分是**無限多個**的線性組合（有限和取極限）。無限多個會不會收斂到不是高斯的東西？要看加權。
  - 老師的例子：i.i.d. 和除以 $\sqrt n$（再乘適當常數）趨於高斯（中央極限定理）；除以 $n$ 趨於常數（期望值，大數法則）；除以 $n^2$ 趨於 0。所以會不會退化 (degenerate)、跑到別的地方，要看加權。
- 老師的結論：比較確定的是 **Haykin 的定義比較廣**；課本真正需要的是有限樣本，就直接這樣定義。

⚠️ 待確認：老師口述大數法則／中央極限定理時還提到「除以 $n\log n$ 趨於常數 1」，逐字稿聽不清楚，未寫入。

---

## 4. 用高斯例子驗證 Woodward 有多準

[▶ 33:11](https://youtu.be/pInAtXl6AHA?t=1991) 證明的重點：$|\tau|<\tau_0$ 時 $R_{ZZ}\approx R_{\bar Z\bar Z}$；$|\tau|>\tau_0$ 時兩者都接近 0。用最簡單的高斯例子看準不準。

**設定**：由存在定理，給零平均和一個自相關，就產生一個高斯過程：
$$R_C(\tau)\approx\begin{cases}\rho,&|\tau|<\tau_0\\0,&|\tau|>\tau_0\end{cases}$$

**為什麼是 $\approx$？** [▶ 34:12](https://youtu.be/pInAtXl6AHA?t=2052) 這個函數**不是非負定**的：第 13 集的必要條件排除——自相關在原點連續則處處連續；它在原點連續，卻在 $\tau_0$ 突然斷掉。所以用近似：真正的函數是掉下來但連續（不是瞬間跳躍），就合法了。

**Step 1：$\varphi$ 的變異數。** $\varphi$ 是 $C$ 的積分（積分是線性系統，也可以用 Theorem 9-2，它是卷積的極限，轉移函數是 $\frac{1}{j\omega}$），照兩次積分算：
$$\sigma_\varphi^2(\tau)=E\{\varphi^2(\tau)\}=\int_0^\tau\!\!\int_0^\tau R_C(\alpha-\beta)\,d\alpha\,d\beta\approx\begin{cases}\rho\tau^2,&|\tau|<\tau_0\\\rho\tau_0(2\tau-\tau_0),&\tau>\tau_0\end{cases}$$

**Step 2：高斯的特性函數。** $\varphi$ 是零平均高斯（上一節），特性函數只需要二階動差：
$$R_{WW}(\tau)=E\{e^{j\lambda\varphi(\tau)}\}=e^{-\lambda^2\sigma_\varphi^2(\tau)/2}.$$

**Step 3：直線逼近的版本。** $\bar Z$ 只有一點 $C_0\sim N(0,\rho)$，所以 $R_{\bar W\bar W}(\tau)=e^{-\lambda^2\rho\tau^2/2}$，**對所有 $\tau$**。

**Step 4：比較。** $|\tau|<\tau_0$ 時兩者**完全一樣**。差別只在 $\tau>\tau_0$：
$$\left|R_{WW}-R_{\bar W\bar W}\right|\le e^{-\lambda^2\rho\tau_0(2\tau-\tau_0)/2}+e^{-\lambda^2\rho\tau^2/2}.$$
傅立葉轉換後，把絕對值放進積分（後面的 $e^{-j\omega\tau}$ 就不見了）積出來，會出現高斯 CDF 的形式，看不出準不準。

**Step 5：高斯尾機率的上下界**（Proakis 書上也有，非常有名的近似）：
$$\frac{1}{\sqrt{2\pi}x}e^{-x^2/2}\left(1-\frac1{x^2}\right)\le Q(x)\le\frac{1}{\sqrt{2\pi}x}e^{-x^2/2}.$$
只取第一項是上界，減一項是下界，再加一項又是上界……可以把高斯 CDF 畫得非常準。用它得到差的上界，**$\lambda^2$ 在指數上**：$\lambda$ 夠大，兩者的差直接掉下來。

所以在這個例子，**Woodward 近似蠻準的**——這次有量化的依據了。（$X$ 的頻譜是兩個 $Z$ 頻譜的疊加，結論一樣。）老師提醒：你也可以故意做一個例子讓它不準，因為它畢竟是近似。

（投影片上的完整積分細節逐字稿沒唸，待補。）

【課本補充】Papoulis 的版本（pp. 471–472）：$C$ 零平均常態，$\sigma_\varphi^2(\tau)=2\int_0^\tau R_C(\alpha)(\tau-\alpha)d\alpha$（式 (10-165)）。用相關時間 $\tau_c=\frac1\rho\int_0^\infty R_C$ 和兩個常數 $\tau_0<\tau_1$（$R_C\approx\rho$ 於 $|\tau|<\tau_0$，$\approx0$ 於 $|\tau|>\tau_1$）：
$$\sigma_\varphi^2(\tau)\approx\begin{cases}\rho\tau^2,&|\tau|<\tau_0\\2\rho\tau_c\tau,&\tau>\tau_1\end{cases}\qquad R_{WW}(\tau)\approx\begin{cases}e^{-\rho\lambda^2\tau^2/2}\\e^{-\rho\lambda^2\tau_c\tau}\end{cases}\qquad\text{(10-167)}.$$

---

## 5. 寬頻 FM vs 窄頻 FM

[▶ 39:16](https://youtu.be/pInAtXl6AHA?t=2356)

- **$\lambda$ 夠大**（頻寬寬）：$Z$ 和 $\bar Z$ 很接近，頻譜就是預期的頻率 PDF。$C$ 是 $\varphi$ 的微分，就是頻率（瞬時頻率 $\omega_i=\omega_0+\lambda C$）。→ **寬頻 FM** (wideband FM)：功率頻譜 = 瞬時頻率的 PDF。
- **$\lambda$ 很小**（$\tau_0$ 也小）：剛才的公式（$\tau>\tau_0$ 那一段）裡不一樣的那一項會**凸顯**出來，主導整個積分。它的傅立葉轉換會變成另一種形式，拉得很遠，和近似完全不準。→ **窄頻 FM** (narrowband FM)：不能用頻率的 PDF 來近似。

> **結論**：寬頻 FM 的功率頻譜就是瞬時頻率的 PDF；窄頻 FM 不是。

【課本補充】p. 472，式 (10-168)、(10-169)：傅立葉轉換的漸近性質——$R_{WW}$ 在小 $\tau$ 的行為決定 $S_{WW}$ 在大 $\omega$ 的行為，反之亦然。
$$e^{-\rho\lambda^2\tau^2/2}\leftrightarrow\frac1\lambda\sqrt{\frac{2\pi}{\rho}}e^{-\omega^2/2\rho\lambda^2},\qquad e^{-\rho\lambda^2\tau_c|\tau|}\leftrightarrow\frac{2\rho\tau_c\lambda^2}{\omega^2+\rho^2\tau_c^2\lambda^4}.$$
所以 $S_{WW}$ 在原點附近是 **Lorentzian**，$\omega\to\infty$ 時漸近常態。寬頻 FM（$\rho\lambda^2\tau_0^2\gg1$）時 $R_{WW}\approx0$（$|\tau|>\tau_0$），用上面的近似得 $S_{WW}(\omega)\approx\frac{2\pi}{\lambda}f_C\left(\frac\omega\lambda\right)$，和 Woodward 定理一致。

---

## 6. 一頁速查表

### Woodward 定理

$$S_{XX}(\omega)\approx\frac{\pi}{2\lambda}\left[f_C\left(\tfrac{\omega-\omega_0}{\lambda}\right)+f_C\left(\tfrac{-\omega-\omega_0}{\lambda}\right)\right]\quad(\lambda\ \text{大},\ C\ \text{連續、SSS})$$

- 關鍵一步：$\varphi(\tau)\approx C(0)\tau$（$|\tau|<\tau_0$）→ $R_{\bar Z\bar Z}=e^{j\omega_0\tau}\Phi_C(\lambda\tau)$ → 傅立葉轉換 $=\frac{2\pi}{\lambda}f_C\left(\frac{\omega-\omega_0}{\lambda}\right)$。
- $|\tau|>\tau_0$：Riemann–Lebesgue，$\Phi_C(\lambda\tau)\to0$。
- 意義：FM 頻譜 ≈ 瞬時頻率的分布（引理的推廣）；只是定性的，沒說 $\lambda$ 多大。

### Riemann–Lebesgue

有密度 ⇒ 特性函數 $\to0$；有限能量訊號的頻譜在 $\omega\to\infty$ 時 $\to0$。關鍵：截斷 + $\int_{-A}^{A}e^{jst}dt=\frac{2\sin As}{s}$。

### 高斯過程的定義

| 定義 | 內容 | 強弱 |
|---|---|---|
| Papoulis、Gray & Davisson | 有限樣本聯合高斯 | 被 Haykin 推出 |
| Haykin | $\int gX\,dt$ 對每個 $g$ 都是高斯 | 較廣；反向需無限線性組合仍高斯（tricky） |

- Haykin 定義下：高斯過程的積分是高斯（交換積分順序，$G(\theta)=\int_\theta g$）。

### 高斯 FM 例子

- $R_C\approx\rho\mathbf{1}[|\tau|<\tau_0]$（不是非負定，只能近似）；$\sigma_\varphi^2=\rho\tau^2$ 或 $\rho\tau_0(2\tau-\tau_0)$；$R_{WW}=e^{-\lambda^2\sigma_\varphi^2/2}$。
- 誤差上界的指數含 $\lambda^2$ → 寬頻時很準；窄頻時不準（Lorentzian）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 調變訊號的平穩性 | 下一集：§10-4 循環平穩過程（載波沒有隨機相位時） |
| 高斯過程的定義 | §11 頻譜表示、§13 均方估計 |
| Riemann–Lebesgue、漸近性質 | §12-2 頻譜估計 |
| 相關時間 $\tau_c$ | 遍歷性（第 30–33 集） |

---

## 附：本集一句話總結

> **Woodward 定理：調變指數 $\lambda$ 夠大時，FM 訊號的功率頻譜就是瞬時頻率（資訊 $C$）的 PDF 平移到 $\pm\omega_0$——證明靠在小範圍用直線逼近相位、在大範圍靠 Riemann–Lebesgue 讓兩者都趨於 0；高斯例子顯示誤差隨 $\lambda^2$ 指數衰減，但窄頻 FM 就不適用。**

---

## ⚠️ 待確認清單

1. [▶ 32:10](https://youtu.be/pInAtXl6AHA?t=1930) 老師口述「除以 $n\log n$ 趨於常數 1」等極限例子，逐字稿聽不清楚。
2. [▶ 37:14](https://youtu.be/pInAtXl6AHA?t=2234) 高斯例子中誤差上界的完整積分結果，投影片有、逐字稿沒唸出。
3. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 10-3 (3/3) 錄影逐字稿（whisper large-v3-turbo，42:31）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
