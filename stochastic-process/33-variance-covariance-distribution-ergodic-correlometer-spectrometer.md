---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 33
lecture: Lec 12-1 Spectrum Estimation — Ergodicity (3/3)
date: 待補
video: https://youtu.be/i4aInSNzAnY
notes: Papoulis & Pillai 4th ed. §12-1（式 (12-15)–(12-35)、Example 12-8、Covariance-Ergodic、Nonlinear Estimators、Correlometers and Spectrometers、Distribution-Ergodic，pp. 529–537）
---

# 第 33 集 · Lec 12-1 (3/3)：mean-ergodic 的頻譜與濾波器觀點、variance-ergodic（四階、高斯配對公式）、未知平均、covariance-ergodic、Bussgang 量測、distribution-ergodic、相關計與頻譜計 [▶ 影片](https://youtu.be/i4aInSNzAnY)

← 上一集：[32](32-ergodicity-motivation-measurement-correction.md) ｜ [總目錄](README.md) ｜ 下一集：[34](34-periodogram-bias-variance-data-window-smoothed-spectrum.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 33 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（58:52，whisper large-v3-turbo）＋ Papoulis §12-1（pp. 529–537）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：開頭「在耕見 某個程中素是由這幾個程度。 小白雜誌」為無意義的雜訊字幕；「ergodicity」→「Ergoticity／ergaticity」，「variance-ergodic」→「variouserganic／varianterganic」，「covariance-ergodic」→「covarian ergaticity」，「distribution-ergodic」→「distribution or guarded」，「sinc」→「sync」，「covariance spectrum」→「covariant spectrum」，「predictable／regular」→「predictable／regular」，「Wold decomposition」→「wold decomposition」，「strict-sense stationary」→「Stricky Sense Stationary／SS」，「fourth moment」→「forced moment」，「穩態」→「穩泰」，「jointly Gaussian」→「JoinGauss」，「Gaussian Processes for Machine Learning」→「Gaussian Random Process in Machine Learning」，「bias／biased／unbiased」→「bias」，「Bussgang」→「Baskin／Buskin」，「cross-covariance」→「Close Covariance」，「hard limiter」→「Hart Limiter／Heart Limiter」，「memoryless system」→「Memory System」，「CDF」→「CDF」，「correlometer」→「correlometer」，「Fabry–Pérot interferometer」→「某一個 F 跟 P 這兩個……Interferometer」，「Michelson」→（未說名字），「central limit theorem」→「central limit theorem」，「Chebyshev」→「Tabyshev／Chavyshev」，「Kolmogorov」→「Komagorov」，「實數」→「時數」，「名垂青史」→「名垂侵蚀」，「高斯」→「高丝／高湿」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Mean-ergodic 的頻譜觀點](#1-mean-ergodic-的頻譜觀點)
- [2. 時間平均 = 一個線性濾波器](#2-時間平均--一個線性濾波器)
- [3. Variance-ergodic](#3-variance-ergodic)
  - [3.1 為什麼要 SSS：量 $k$ 階要 $2k$ 階穩定](#31-為什麼要-sss量-k-階要-2k-階穩定)
  - [3.2 高斯的配對公式](#32-高斯的配對公式)
  - [3.3 已知平均 vs 未知平均](#33-已知平均-vs-未知平均)
- [4. Covariance-ergodic](#4-covariance-ergodic)
- [5. 什麼時候都量得準（高斯）](#5-什麼時候都量得準高斯)
- [6. 再一次：真正要的是大數法則](#6-再一次真正要的是大數法則)
- [7. 互共變異](#7-互共變異)
- [8. 用 Bussgang 定理量自共變異](#8-用-bussgang-定理量自共變異)
- [9. Distribution-ergodic](#9-distribution-ergodic)
- [10. 相關計與頻譜計](#10-相關計與頻譜計)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 頻譜觀點、濾波器觀點 | [▶ 00:00](https://youtu.be/i4aInSNzAnY?t=0) | 式 (12-15)、(12-16)，p. 529 |
| Variance-ergodic | [▶ 09:43](https://youtu.be/i4aInSNzAnY?t=583) | 式 (12-19)–(12-24)，pp. 531–532 |
| Covariance-ergodic | [▶ 25:12](https://youtu.be/i4aInSNzAnY?t=1512) | 式 (12-25)–(12-28)，p. 532 |
| 大數法則 | [▶ 32:53](https://youtu.be/i4aInSNzAnY?t=1973) | 無（【口頭】） |
| Bussgang | [▶ 39:33](https://youtu.be/i4aInSNzAnY?t=2373) | 式 (12-32)、(12-33)，p. 534 |
| Distribution-ergodic | [▶ 42:37](https://youtu.be/i4aInSNzAnY?t=2557) | 式 (12-34)、(12-35)，pp. 536–537 |
| 相關計、頻譜計 | [▶ 49:12](https://youtu.be/i4aInSNzAnY?t=2952) | pp. 534–536 |

---

## 1. Mean-ergodic 的頻譜觀點

[▶ 00:00](https://youtu.be/i4aInSNzAnY?t=0) 從功率頻譜看：

$$\sigma_T^2=\frac1{2\pi}\int S^c(\omega)\frac{\sin^2T\omega}{T^2\omega^2}d\omega\qquad\text{(12-16)}.$$

**定性理解**【口頭】：量測一定只量一段時間（一天、一年、二十年），不可能無限長，所以一定是一個 **window**；window 轉到頻域是 sinc，又是能量，所以是 $\mathrm{sinc}^2$。

- 用的是**共變異頻譜** $S^c$（上標 c）：要把期望值扣掉，看的是**變異**。要估期望值，只要看變異——變異很小就會接近要量的期望值。所以用 autocovariance，不用 autocorrelation。（例：上集 AM 期望值 2，不是 3 就是 1。）
- 這個變異數趨近 0 是 if and only if 的條件。

**有脈衝就不可量** [▶ 02:04](https://youtu.be/i4aInSNzAnY?t=124)：扣掉期望值後共變異頻譜有脈衝——就是 predictable 部分（Wold 分解：WSS = regular + predictable，predictable 的頻譜都是脈衝；我們做得出來的都是 regular）。delta 積分就是把它的位置代進 sinc，只要不是剛好在 sinc 的零點，就有一個**完全不會衰減**的值。

**大數據的提醒**【口頭】：資料量非常大，有沒有用？**不是 ergodic，大沒有用**——平均是不對的。而且這種過程每個人量出來會不一樣（不是量不量得準的問題）。你和同事認真量同一個現象得到不同結論——例如地球有沒有暖化，為什麼某些人量出來和我們不一樣——就表示是 non-ergodic process，見仁見智（如果是真的認真量，不是自己亂想）。

---

## 2. 時間平均 = 一個線性濾波器

[▶ 04:37](https://youtu.be/i4aInSNzAnY?t=277) $\eta_T$ 是精確的量測——連續積分、沒有取樣、$-T$ 到 $T$ 所有值都進來，再除以 $2T$。另一個觀點：

- $-T$ 到 $T$ 的積分像一個 **window**，window 本身是一個濾波器——**moving average**（time-average window）。實作上例如每 30 ms 切一段量一次。
- 輸入是要量的對象 $X$，輸出是量測結果 ⇒ **線性非時變、穩定**的濾波器（脈衝響應總面積有限）。
- $\eta_T$ 就是送進去之後，在某個時間看那一點的結果；window 大小 $2T$。

（量測不見得真的用濾波器做，但相當於把河川流量、地球暖化溫度送進一個線性濾波器。）這是一個 generalization。

**好處**：用第 9 章的觀念——輸出的變異數（輸出的自共變異在 0）就是**輸入的自共變異經過兩次濾波器**。後面的數學不重要（大一微積分，積分換順序 $ds\,dv\to dv\,ds$，把自共變異獨立出來，就看到它跟三角波做積分），要的是這個想法。課本式 (12-2)、(12-3)：$\eta_T=w(0)$，$w(t)=\frac1{2T}\int_{t-T}^{t+T}X(\alpha)d\alpha$。

**回顧** [▶ 08:10](https://youtu.be/i4aInSNzAnY?t=490)：ergodic 在 1950、60 年代來自遍歷集合——封閉系統裡對時間的循環操作（大寫 $T$ 隱含 Time）。在封閉系統裡一直跳、跳不出來，就會量到所有現象，時間平均就變期望值。但封閉的物理系統很難達到，總會跟外界交流。80、90 年代的書常用結果定義 ergodic——不能說完全對錯。書是人寫的，不同切入點得到不同結果，要多看幾本比較。Papoulis 聰明，創了新名詞 mean-ergodic。

---

## 3. Variance-ergodic

[▶ 10:13](https://youtu.be/i4aInSNzAnY?t=613) 另一個新名詞——**variance-ergodic**。老師說不用看定義，從觀念就推得到：**我要量變異數，量不量得準？**

- 只能在不同時間各量一個值，用不同時間的平方的平均，能不能量到變異數？
- 變異數 = 值平方的期望值 − 平均平方。所以把量到的平方做平均，50 個同學量、每人平均都一樣，就是 variance-ergodic。問題跟前面是一樣的。

### 3.1 為什麼要 SSS：量 $k$ 階要 $2k$ 階穩定

[▶ 11:16](https://youtu.be/i4aInSNzAnY?t=676) 課本這裡要求 **SSS**（strict-sense stationary，所有動差都穩態），前面沒特別強調。舉一反三：

- Slutsky：一階（平均）要量得準，要有**二階**的性質（自共變異）。
- 所以二階（變異數）要量得準，要有**四階**的性質：$E\{X^2(t+\tau)X^2(t)\}$ 要收斂。
- 四階要穩態才能推導；不要求 SSS 的話，至少要四階穩態。
- 三階要量得準，要**六階**收斂。例如要量腦波的三階動差，腦波的六階統計特性至少要收斂。

老師說：這樣的數學討論有價值，它建立了量測的基礎理論；以後碰到問題就知道緣由和解釋。

**已知平均（設 $\eta=0$）**：
$$V_T=\frac1{2T}\int_{-T}^{T}X^2(t)\,dt\qquad\text{(12-20)},$$
不偏；用 Slutsky 定理於 $X^2(t)$，variance-ergodic ⇔
$$\frac1T\int_0^T E\{X^2(t+\tau)X^2(t)\}\,d\tau\to C^2(0)\qquad\text{(12-22)}.$$

### 3.2 高斯的配對公式

[▶ 13:18](https://youtu.be/i4aInSNzAnY?t=798) 很多隨機過程的四階沒有 closed form，所以課本例子都是**高斯**——高斯的一、二、三、四階都有公式。

【口頭】老師最近看到一本書《Gaussian Processes for Machine Learning》專門討論高斯：machine learning 是 model-based，最好的 model 就是高斯，可以做很多假設。

> **高斯配對公式**（零平均、jointly Gaussian 的 $X,Y,U,V$）：
> $$E\{XYUV\}=E\{XY\}E\{UV\}+E\{XU\}E\{YV\}+E\{XV\}E\{YU\}.$$
> 兩兩配對加起來（4 取 2 的所有配對），**降階**。六個就是每次取兩個、所有配對窮舉（exhaustive）。四階、六階、八階都馬上降到二階。

**用在 $X^2$**：$X=Y$、$U=V$：
$$E\{X^2U^2\}=E\{X^2\}E\{U^2\}+2E^2\{XU\}.$$
三項裡有兩項一樣，所以是兩倍。代進去：
$$C_{x^2x^2}(\tau)=E\{X^2(t+\tau)X^2(t)\}-E^2\{X^2\}=2C^2(\tau)\qquad\text{(12-23)}.$$
（下一張投影片有細節：$+2$ 那項留下，$C^2(0)$ 那項消掉。）**高斯特有**：二次對二次的自共變異 = 兩倍一次對一次自共變異的平方。

> **高斯過程 variance-ergodic ⇔**
> $$\frac1T\int_0^TC^2(\tau)\,d\tau\to0\qquad\text{(12-24)}.$$

加平方說不定會變大、更難。老師說這個概念對一般過程也可以用（大部分過程都有一點高斯的影子）：二次要量得準，自共變異平方的積分平均要收斂到 0。

【課本補充】p. 531：由 $\left|\frac1T\int_0^TC\right|^2\le\frac1T\int_0^TC^2$，高斯過程 variance-ergodic ⇒ mean-ergodic，反過來不對。頻譜詮釋：mean-ergodic ⇔ $S^c$ 在**原點**沒有脈衝；variance-ergodic ⇔ $S^c$ **任何地方**都沒有脈衝。Example 12-8：$X=a\cos\omega t+b\sin\omega t+\eta$（高斯、平穩）是 mean-ergodic，但 $|X-\eta|^2$ 含隨機常數 $\frac{a^2+b^2}{2}$，不是 variance-ergodic。

### 3.3 已知平均 vs 未知平均

[▶ 19:32](https://youtu.be/i4aInSNzAnY?t=1172) 上面用的是 $\mu_X$——表示百分之百確定期望值，只量二次變異。這通常比較難：不了解過程，一階、二階都不知道，卻要量二階。

**未知平均**（非常實際，雜訊連期望值是不是 0 都不知道）：先量一階、把平均量準，再把量到的 $X$ 減掉量出來的平均、平方、積分平均：
$$\hat V_T=\frac1{2T}\int_{-T}^{T}\left[X(t)-\eta_T\right]^2dt.$$
實際操作上常常至少要量兩個：一階、二階。

**偏差 (bias)** [▶ 21:36](https://youtu.be/i4aInSNzAnY?t=1296)：detection/estimation 學過，bias 就是偏見——即使量得很準，期望值上還是有偏差。
- 用真的 $\eta$：**不偏** (unbiased)。
- 用 $\eta_T$：**有偏** (biased)。

**但估計變異數比較小** [▶ 22:37](https://youtu.be/i4aInSNzAnY?t=1357)：例：真平均是 0，只量四次：$0.1,0.9,-0.1,0.9$。量測平均 $\frac{1.8}{4}\approx0.45$。
- 以量測平均當中心算變異數——用自己的資料算出來的平均——一定比較小。
- 以真正的 0 當中心算，一定比較大。

所以有些應用（in many cases）即使知道平均是 0，**刻意不用**，而用 biased 的 $\eta_T$ 當中心，因為估計變異數明顯比較小（數學上可以嚴謹證明）。

【課本補充】p. 532：$T$ 大時 bias 可忽略，$\hat V_T$ 的變異數可近似為已知平均時 $V_T$ 的變異數；很多情況 $E\{(\hat V_T-V)^2\}$ 在中等 $T$ 時比 $E\{(V_T-V)^2\}$ 小。

---

## 4. Covariance-ergodic

[▶ 25:12](https://youtu.be/i4aInSNzAnY?t=1512) 老師說：課本一直重複一模一樣的觀念，同學都很清楚接下來要做什麼了。

**要量共變異**：例如相距 $\lambda=0.1$ 秒，通訊訊號的延續影響是多少？每隔一秒量一次，每次量**隔 0.1 秒的兩個值**，相乘再平均：
$$C_T(\lambda)=\frac1{2T}\int_{-T}^{T}Z(t)\,dt,\quad Z(t)=X(t+\lambda)X(t)\qquad\text{(12-25)}.$$

為什麼要 SSS：量二階要驗證四階性質，四階要穩態。為什麼只舉高斯：其他過程沒有好的性質可以算。老師說高斯實在很厲害，挑了一個對的好對象，名字永遠出現在每本課本、名垂青史。

**用配對公式**（零平均高斯 SSS）[▶ 27:15](https://youtu.be/i4aInSNzAnY?t=1635)：

⚠️ 逐字稿缺字：老師說原講義寫錯（copy 來 copy 去 copy 錯了），正確是 $E\{Z(t+\tau)Z(t)\}=E\{X(t+\tau+\lambda)X(t+\tau)X(t+\lambda)X(t)\}$。四個高斯，1 配 2、3 配 4；1 配 3、2 配 4；1 配 4、2 配 3：
$$=C^2(\lambda)+C^2(\tau)+C(\tau+\lambda)C(\tau-\lambda).$$
減掉 $E^2\{Z\}=C^2(\lambda)$：

> $$C_{zz}(\tau)=C(\lambda+\tau)C(\lambda-\tau)+C^2(\tau)\qquad\text{(12-27)}.$$
> covariance-ergodic ⇔ $\frac1T\int_0^TC_{zz}(\tau)d\tau\to0$（式 (12-26)）。

（老師說過程有問題但答案是對的。）$\lambda$ 是要量的間隔，$\tau$ 是自共變異本身的參數。

【課本補充】p. 532：$\mathrm{Var}\,C_T(\lambda)\approx\frac1T\int_0^{2T}[C(\lambda+\tau)C(\lambda-\tau)+C^2(\tau)]d\tau$（式 (12-28)）。

---

## 5. 什麼時候都量得準（高斯）

[▶ 32:23](https://youtu.be/i4aInSNzAnY?t=1943)

> **結論**：高斯過程的自共變異在 $\tau\to\infty$ 時趨近 0，則**平均、變異數、自共變異都量得準**，而且每個人量出來都一樣。

（由 (12-27)：$C(\tau)\to0$ ⇒ $C_{zz}(\tau)\to0$。）別的過程通常也對，但證明沒那麼直接，需要一些條件。

⚠️ 逐字稿缺字 [▶ 38:00](https://youtu.be/i4aInSNzAnY?t=2280)：老師說投影片要更正——應是 $\tau\to\infty$ 時 $C(\tau)\to0$；更精確是**絕對值** $|\tau|\to\infty$（正、負無限大都要是 0）。很多書也有這種不小心的謬誤，觀念清楚就知道。

---

## 6. 再一次：真正要的是大數法則

[▶ 32:53](https://youtu.be/i4aInSNzAnY?t=1973) 有些老師上這門課會刻意避免 ergodic，因為它後來好像沒那麼強烈的重要性。原因：

- 真正要的是**量測之後量得準**。ergodic 保證量得準，但量得準**不一定**是 ergodic（照原始定義）——存在量得準但不是 ergodic 的過程。
- Slutsky 定理說 mean-ergodic ⇔ 自共變異面積平均趨近 0；但回到最原始的要求，ergodic 不是 if and only if。
- 那個要求叫**大數法則**：一個群體平均有一個現象，大家平均量出來都一樣。不一定要完全封閉，也有大數法則的行為。
- 近期的機率書討論的是：在什麼條件下有大數法則的結果。大數法則不是單一定理——Kolmogorov 有他的條件、Chebyshev 有他的條件。ergodic 只是其中一個條件。
- 老師寫資訊理論講義時沒有刻意用 ergodicity 的定義，強調的是大數法則的現象。

**$t$ 和 $T_0$** [▶ 36:29](https://youtu.be/i4aInSNzAnY?t=2189)：左邊（量測）有兩個參數——起始點 $t$ 和 window $T_0$；右邊只有 $T_0$。$t$ 不見了，前提是 WSS：系統穩態時，**從哪一點開始量不重要**——從春天量到冬天，跟從夏天量到明年春天，結果一樣，才叫穩態；不穩態時結果不一樣。

> **兩個條件都要的原因**：
> - 不同時間量、量出來都一樣 → **stationary**。
> - 每個人量的都一樣 → **ergodic**（要的其實是大數法則的結果）。

---

## 7. 互共變異

[▶ 38:31](https://youtu.be/i4aInSNzAnY?t=2311) 例如要量河川流量跟風力、跟溫度有沒有關係——量兩個不同量測值之間的**互共變異** (cross-covariance)。用一模一樣的方式：二次變四次，舉例一定舉高斯。

【課本補充】p. 533：$\hat C_{xy}(\tau)=\frac1{2T}\int_{-T}^TX(t+\tau)Y(t)dt$（式 (12-29)）不偏，變異數用 (12-4) 把 $C$ 換成 $C_{xy}$；若 $C_{xx},C_{yy},C_{xy}$ 在 $\tau\to\infty$ 都趨近 0，則 cross-covariance-ergodic（Prob. 12-9）。

老師說：ergodic 的概念講得夠多了，三個例子應該足夠理解背後的道理；思考性的東西很深，就像量子物理學家、霍金、愛因斯坦講的東西沒什麼人聽得懂，但真正搞清楚一次，接下去就 OK 了，只是觀念上的轉換。

---

## 8. 用 Bussgang 定理量自共變異

[▶ 39:33](https://youtu.be/i4aInSNzAnY?t=2373) **Bussgang 定理**（第 10 集）：高斯在大自然太常發生（中央極限定理）。高斯過程經過**無記憶系統**，輸入輸出的**互共變異和輸入的自共變異完全成正比**。

為什麼再拿出來：要量自共變異，可以改量互共變異——知道一個就知道另一個（差一個已知常數）。實作系統很多時候是設計成量互共變異。

**例：hard limiter** $Y=\mathrm{sgn}\,X$（大於 0 輸出 1、小於 0 輸出 −1）。不是線性系統，但 Bussgang 對任何無記憶系統成立，而無記憶系統很好實作：
$$C_{xy}(\tau)=KC_{xx}(\tau),\quad K=\sqrt{\frac{2}{\pi C_{xx}(0)}}\qquad\text{(12-32)},$$
$$\hat C_{xx}(\tau)=\frac1K\hat C_{xy}(\tau)=\frac1{2KT}\int_{-T}^{T}X(t+\tau)\,\mathrm{sgn}\,X(t)\,dt\qquad\text{(12-33)}.$$
就是 $X$ 跟自己的 hard limiter（$\pm1$）相乘再積分——這是 Bussgang 定理的量測應用。

【課本補充】p. 533 arcsine law：$C_{yy}(\tau)=\frac2\pi\arcsin\frac{C_{xx}(\tau)}{C_{xx}(0)}$（式 (12-30)）。$\hat C_{yy}(\tau)=\frac{T_\tau^+}{T}-1$（$T_\tau^+$ 是 $X(t+\tau)X(t)>0$ 的總時間，被積函數只是 $\pm1$），得 $\hat C_{xx}(\tau)=\hat C_{xx}(0)\sin\left[\frac\pi2\hat C_{yy}(\tau)\right]$（差一個因子）。

---

## 9. Distribution-ergodic

[▶ 42:37](https://youtu.be/i4aInSNzAnY?t=2557) 比較複雜，一般比較少做（一般只量一階、二階）。如果要量統計現象的**分布**：首先要穩態——**SSS 一定要**。

**量 CDF**：用 Bussgang 那樣的想法，把 $X$ 當輸入透過一個 mapping，切在 $x$：
$$Y(t)=\mathbf 1[X(t)\le x],\qquad E\{Y(t)\}=P\{X(t)\le x\}=F(x).$$
（⚠️ 逐字稿缺字：老師口誤說「比 $x$ 小加 1、比 $x$ 大減 1」，後面更正為指示函數：比 $x$ 小給 1、比 $x$ 大給 0、不累積。）

**為什麼量 CDF 比 PDF 好**【口頭】[▶ 43:37](https://youtu.be/i4aInSNzAnY?t=2617)：
- **CDF**（累積分布函數）：量四點 $0.1,0.9,2.3,4.4$，每點機率 $\frac14$，累積畫：到 0.1 升到 $\frac14$、0.9 升到 $\frac12$、2.3 升到 $\frac34$、4.4 升到 1。不需要太多點就能得到蠻精準的曲線——做一個 Gaussian random process generator，大概一百到幾百點（每點 1%）畫出來就蠻接近原始高斯。
- **PDF**：要畫長條圖，每 0.1 切一塊，數落在每塊的點數（300、400、312……）除以總數得高度。每個區間至少要一百點以上才畫得準；區間 0.1 時一萬點大概畫不出高斯的樣子。
- 所以一般直接畫 CDF。

**估計**：例如在 3.0 以下發生過三次、以上一次，估計 $\frac34$——把指示函數加起來平均：
$$F_T(x)=\frac1{2T}\int_{-T}^{T}Y(t)\,dt=\frac{\tau_1+\cdots+\tau_n}{2T}\qquad\text{(12-34)}$$
（$\tau_i$ 是 $X(t)<x$ 的時間區間長度）。

**又回到 mean-ergodic**：量 $Y$ 的平均準不準。$C_{yy}$ = 兩個 $Y$ 相乘的期望值減個別期望值相乘，是**分布**的相減：$R_y(\tau)=P\{X(t+\tau)\le x,X(t)\le x\}=F(x,x;\tau)$（二階分布）。

> **distribution-ergodic ⇔**
> $$\frac1T\int_0^TF(x,x;\tau)\,d\tau\to F^2(x)\qquad\text{(12-35)}.$$

【課本補充】p. 537：充分條件：$\tau\to\infty$ 時 $F(x,x;\tau)\to F^2(x)$——$X(t)$ 和 $X(t+\tau)$ 在 $\tau$ 大時獨立就成立。密度：$f(x)\Delta x\approx\frac1{2T}\sum\Delta\tau_i$，是單一樣本落在 $x$ 到 $x+\Delta x$ 之間的時間百分比，可以用來設計類比估計器。

---

## 10. 相關計與頻譜計

[▶ 49:12](https://youtu.be/i4aInSNzAnY?t=2952) 老師說接下來比較沒有概念、比較簡單。

**相關計** (correlometer)：量自相關的實體裝置。照觀念：兩個相乘（要四階的觀念）、積分一個 window = 經過**低通濾波器**（相當於積分器）。兩種結構（課本 Fig. 12-3）：

| 結構 | 元件 | 輸出 |
|---|---|---|
| (a) | delay、**乘法器**、LPF | $R(\lambda)$ |
| (b) | delay、**加法器**、**平方器**、LPF | $2[R(0)+R(\lambda)]$ |

- (a) 需要**廣義乘法器**（兩個任意值相乘都要給結果），複雜度高、很難。
- (b) 加法器比乘法器容易；平方器可能用查表，表也不會太大。換一下結構思維，可以讓裝置售價或製作複雜度降低。
- (b) 得到要量的自相關加一個常數：$E\{[X(t-\lambda)+X(t)]^2\}=2[R(0)+R(\lambda)]$。在 $\lambda=0$ 得到 4 倍的 $R(0)$，扣掉就好了。

**光學實現（Michelson 干涉儀，Fig. 12-5）**[▶ 51:44](https://youtu.be/i4aInSNzAnY?t=3104)：利用**光程**做 delay——光速一樣，走比較長的路徑就比較晚到。同一個光源 $X(t)$（隨過程的值改變光的特性），一個 copy 折射、一個穿透，走路徑 1 和 2；移動鏡子距離 $d$，$\lambda=\frac{2d}c$；$t_0=\frac lc$ 是路徑 1 的到達時間。用平方器（detector）加 LPF，得 $2A^2[R(0)+R(\lambda)]$。不需要難做的廣義乘法器。

**頻譜計** (spectrometer，Fig. 12-4) [▶ 53:16](https://youtu.be/i4aInSNzAnY?t=3196)：直接量功率頻譜（自相關的傅立葉轉換）。
- 設計一個非常窄的帶通濾波器 $B(\omega)$（中心 $\omega_0$、單位能量）。
- 線性濾波器：輸出頻譜 = 輸入頻譜 × $|B(\omega)|^2$。只讓某個特定頻率通過，量到的就是 $S(\omega_0)$。
- 平方器 + LPF：量 $E\{y^2(t)\}$——相當於前面結構把 $\lambda$ 設 0（光程完全一樣），直接平方。
$$E\{y^2(t)\}=\frac1{2\pi}\int S(\omega)|B(\omega)|^2d\omega\approx S(\omega_0).$$
- 這種裝置通常非常貴。

**Fabry–Pérot 干涉儀（Fig. 12-6）**：兩片高反射平板 $P_1,P_2$，距離 $d$ 可調：
$$B(\omega)=\frac{1}{1-r^2e^{-j2\omega d/c}},\quad r\approx1.$$
- 老師說有點像 AR model（$r<1$ 可以展開），可以實作。
- 它不是單一脈衝，而是**週期性**的很多個脈衝，中心 $\omega_n=\frac{\pi nc}{d}$（⚠️ 課本印 $\omega_n=\frac{\pi nd}{c}$，由 $e^{-j2\omega d/c}=1$ 推應為 $\frac{\pi nc}{d}$，待確認）。理想上只想要一個脈衝，但很難；調整讓間隔比要量的頻譜還寬，要量的部分中間就只有一個脈衝。
- 複數平面圖：分母 $1-r^2e^{-j2\omega d/c}$——1 是實數，減去旋轉 $-\frac{2\omega d}{c}$、長度 $r^2$ 的向量；量的是這個向量長度的倒數 $|B(\omega)|$。$r=0.9$ 就很接近脈衝，$0.6$ 不像。

**最後提醒**：量不量得準，還要看隨機過程的特性。不是 ergodic 就不用量，量出來一直不一樣。

---

## 11. 一頁速查表

| 量什麼 | 條件（高斯、零平均） | 關鍵 |
|---|---|---|
| 平均 | $\frac1T\int_0^TC\to0$ | Slutsky；$S^c$ 原點無脈衝 |
| 變異數（已知平均） | $\frac1T\int_0^TC^2\to0$ | $C_{x^2x^2}=2C^2$；$S^c$ 無脈衝 |
| 自共變異 $C(\lambda)$ | $\frac1T\int_0^T[C(\lambda+\tau)C(\lambda-\tau)+C^2(\tau)]\to0$ | 配對公式 |
| 分布 $F(x)$ | $\frac1T\int_0^TF(x,x;\tau)d\tau\to F^2(x)$ | $Y=\mathbf 1[X\le x]$ |
| 全部 | $C(\tau)\to0$（$\lvert\tau\rvert\to\infty$） | — |

- 量 $k$ 階要 $2k$ 階穩定（SSS）。
- 高斯配對：$E\{XYUV\}=E\{XY\}E\{UV\}+E\{XU\}E\{YV\}+E\{XV\}E\{YU\}$。
- 未知平均：用 $\eta_T$ 當中心——有偏，但估計變異數較小。
- 時間平均 = moving-average 濾波器；輸出變異數 = 輸入自共變異過兩次濾波器。
- Bussgang：$\hat C_{xx}=\frac1K\cdot\frac1{2T}\int X(t+\tau)\mathrm{sgn}X(t)dt$，$K=\sqrt{2/(\pi C(0))}$。
- 相關計 (b)：加法器 + 平方器，得 $2[R(0)+R(\lambda)]$；頻譜計：窄帶通 + 平方 + LPF 得 $S(\omega_0)$。
- stationary：從哪裡開始量都一樣；ergodic（大數法則）：誰量都一樣。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 量自相關、頻譜計 | 下一集起：§12-2 頻譜估計（periodogram） |
| window、sinc² | 頻譜估計的 window、偏差與變異數 |
| 大數法則 | 資訊理論 |

---

## 附：本集一句話總結

> **用時間平均量平均要自共變異條件、量變異數要四階條件、量自共變異也要四階（高斯靠配對公式降階：$C_{x^2x^2}=2C^2$），所以高斯過程只要 $C(\tau)\to0$ 平均、變異數、自共變異都量得準；不知道平均時用量測平均當中心雖有偏但變異數較小；實作上可用 Bussgang（hard limiter）、加法器加平方器的相關計、窄帶通的頻譜計來量——而工程上真正要的是大數法則。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。
2. Fabry–Pérot 的頻帶中心：課本 p. 536 印 $\omega_n=\frac{\pi nd}{c}$，依 $B(\omega)$ 的分母推應為 $\frac{\pi nc}{d}$，老師沒講。

---

*筆記依據陳伯寧老師「隨機過程」Lec 12-1 (3/3) 錄影逐字稿（whisper large-v3-turbo，58:52）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
