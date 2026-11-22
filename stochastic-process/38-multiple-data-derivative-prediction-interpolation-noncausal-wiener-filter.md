---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 38
lecture: Lec 13-1 Mean Square Estimation — Introduction (2/2)
date: 待補
video: https://youtu.be/dj6_7NXQJCM
notes: Papoulis & Pillai 4th ed. §13-1 Simple Illustrations（Prediction、Filtering、Interpolation 式 (13-7)–(13-11)、Smoothing 式 (13-12)–(13-16)，pp. 582–585）
---

# 第 38 集 · Lec 13-1 (2/2)：多筆資料的線性預測、用 $S$ 和 $S'$ 預測、平穩時係數不隨時間變、內插 (interpolation) 與 sinc、算 MSE 的快速方法、非因果 Wiener 濾波器 [▶ 影片](https://youtu.be/dj6_7NXQJCM)

← 上一集：[37](37-mean-square-estimation-orthogonality-principle-terminology-wide-sense-markov.md) ｜ [總目錄](README.md) ｜ 下一集：[39](39-prediction-infinite-past-error-filter-regular-r-step-analog.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 38 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（29:47，whisper large-v3-turbo）＋ Papoulis §13-1（pp. 582–585）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「orthogonality principle」→「Autogonality Principle／Authoconality／all-so-goal nality」，「正交」→「證交」，「wide-sense Markov」→「Widesense Markov」，「weighting」→「waiting」，「autocorrelation」→「autocorrigion／autochrome／autocarrant／AutoColient／autoclumphant」，「wide-sense stationary」→「Y線stationary／Wisen stationary」，「interpolation」→「interpellation」，「Nyquist rate」→「dequase rate／Niquist／Niquis」，「sinc」→「sync」，「band-limited」→「Band Limited／Banelimited」，「mean square error」→「min squared error／Min2Error」，「norm」→「none」，「Wiener filter」→「Winer Filter」，「noncausal」→「Nun Causal」，「聯立方程式」→「連例方程式」，「權重」→「微挺」。以下一律用正確的字。

> **本集定位**：第 13 章從實用角度很重要——不管做什麼領域，大部分都會碰到 MSE 估計器；頻譜估計反而比較侷限在特定應用。線性預測非常常用。觀念上永遠記得**正交原理**：資料跟誤差一定要完全正交（線性代數的幾何觀念）。

---

## 目錄

- [1. 回顧：wide-sense Markov of order 1](#1-回顧wide-sense-markov-of-order-1)
- [2. 多筆資料的線性估計](#2-多筆資料的線性估計)
- [3. 例：用 $S$ 和 $S'$ 預測（走勢）](#3-例用-s-和-s-預測走勢)
- [4. Filtering under stationarity](#4-filtering-under-stationarity)
- [5. 內插 (interpolation)](#5-內插-interpolation)
  - [5.1 正交原理](#51-正交原理)
  - [5.2 算 MSE 的快速方法](#52-算-mse-的快速方法)
  - [5.3 頻帶受限：sinc 內插](#53-頻帶受限sinc-內插)
- [6. Smoothing：非因果 Wiener 濾波器](#6-smoothing非因果-wiener-濾波器)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 1. 回顧：wide-sense Markov of order 1

[▶ 01:04](https://youtu.be/dj6_7NXQJCM?t=64)
- **wide sense**：沒辦法看所有統計現象，一般看一、二階，比較鬆散、廣義。
- **Markov**：從某個時間點以前的資料都不需要參考；order 1 只要看一點。
- **怎麼證**：正交原理——把之前的資料跟現在的誤差相乘取期望值是 0，代表那筆資料沒用。

---

## 2. 多筆資料的線性估計

[▶ 02:06](https://youtu.be/dj6_7NXQJCM?t=126) 推廣：要估 $S$，有 $K$ 種資料 $X_1,\dots,X_K$（更常發生：例如估股市走向，有好幾筆不同來源的資料），每種都收集一段時間：
$$\hat S(t)=\sum_{i=1}^{K}\int h_i(\alpha,t)X_i(\alpha)\,d\alpha.$$
weighting 兩個參數：$t$ 是要預測的時間（10 點、10:30、10:40 的走向，weighting 可能不同）；$\alpha$ 是跟哪筆資料相乘。

**正交原理**：資料乘誤差 = 0，解出來就是答案。證明非常單純——這是線性預測設計的好處。

**不用計算也看得出來** [▶ 04:09](https://youtu.be/dj6_7NXQJCM?t=249)：
$$R_{sx_l}(t,\xi)=\sum_i\int h_i(\alpha,t)R_{x_ix_l}(\alpha,\xi)\,d\alpha.$$
- **右邊**：資料兩兩之間的自相關，做 weighting、加總。
- **左邊**：要預測的對象跟資料之間的自相關。
公式不用記，概念要抓到。

---

## 3. 例：用 $S$ 和 $S'$ 預測（走勢）

[▶ 04:39](https://youtu.be/dj6_7NXQJCM?t=279) 只收到一筆資料，但可以用**微分**——從另一個角度看好像是非線性預測，但還是線性 weighting。

$$\hat S(t+\lambda)=a_1S(t)+a_2S'(t).$$
**直觀**【口頭】：用現在的溫度和溫度的變化預測一小時後（$\lambda=1$ 小時），比只用現在溫度準一點——同一個溫度，可能是上升到的、也可能是下降到的。股市一樣：現在 8100 點，是上升到達還是下降到達？這個資訊也有幫助。微分就是**走勢**。商學院和很多現象的預測常用資料和資料的微分預測走勢，很實用。

**正交原理**：誤差和 $S(t)$、$S'(t)$ 都正交——兩筆資料，二元一次聯立方程。

**自相關的轉換**（綠框）[▶ 07:48](https://youtu.be/dj6_7NXQJCM?t=468)：WSS 時，把微分器當成線性濾波器（輸入 $S$、輸出 $S'$），用定理 9-2：
- 輸入對輸出的自相關 = 輸入自相關經過濾波器**一次**（對第二個參數微分）。
- 輸出對輸出 = 經過**兩次**（再對 $t_1$ 微分；因為後面是 $-t_2$，有負號）。
$$R_{ss'}(\tau)=-R'(\tau),\qquad R_{s's'}(\tau)=-R''(\tau).$$

**解**：資料時間是 $a$，要預測的時間是 $a+\lambda$。WSS ⇒ 解出來的係數跟**絕對時間無關**（10 點預測和 11 點預測用的 weighting 完全一樣）。

**簡化**：WSS 的自相關最大值永遠在原點（重要定理），是頂點，所以通常 $R'(0)=0$。代入，交叉項殺掉：
$$a_1=\frac{R(\lambda)}{R(0)},\qquad a_2=\frac{R'(\lambda)}{R''(0)}.$$

**合理**：
- 要預測的時間和資料時間的相關性 $R(\lambda)$ 大，就信任資料，weighting 大；10 點到 11 點相關性很小，weighting 就小。
- 微分的相關性大就信任微分，小就不信任。
- 走勢往上就預測下個時間往上，往下就往下——量完全成正比。老師說他有一陣子在買股票，這時這觀念就很重要。

【課本補充】p. 582：$P=R(0)-a_1R(\lambda)+a_2R'(\lambda)$；$\lambda$ 小時 $a_1\approx1$、$a_2\approx\lambda$，$\hat S(t+\lambda)\approx S(t)+\lambda S'(t)$。

---

## 4. Filtering under stationarity

[▶ 13:20](https://youtu.be/dj6_7NXQJCM?t=800) 濾波器：有輸入有輸出（系統觀）。輸入 $X$、輸出 $\hat S$，用濾波器的想像看線性預測（濾波器剛好也是線性）。（⚠️ 逐字稿缺字：老師口誤說「到第 11 章」，指的是第 13 章的這一節。）

$S$、$X$ **jointly stationary** 時，預測係數是常數，完全跟要預測的點 $t$ 無關：
$$\hat S(t)=aX(t),\qquad a=\frac{R_{sx}(0)}{R_{xx}(0)},\qquad P=R_{ss}(0)-aR_{sx}(0).$$
系統穩態時預測係數不隨時間改變；不穩時要隨時間改變。很直觀的數學結果。

---

## 5. 內插 (interpolation)

[▶ 14:52](https://youtu.be/dj6_7NXQJCM?t=892) 有很多離散的點，要產生中間的點、把中間連起來。通訊上很有用：傳送端送的就是取樣後的點（不太可能送連續的）。Nyquist rate 告訴你：取樣率超過頻寬兩倍，用 sinc 做內插可以完全精準、沒有誤差地產生原訊號。

**這節要講**：內插事實上就是**線性預測**，可以得到一模一樣的結果——不管用什麼角度看，結果一樣。

### 5.1 正交原理

[▶ 16:25](https://youtu.be/dj6_7NXQJCM?t=985) 取樣點 $t+kT$，要估 $t+\lambda$（$0<\lambda<T$）的值，用 $2N+1$ 個點（⚠️ 逐字稿缺字：老師先說 $2N$，更正為 $2N+1$）：
$$\hat S(t+\lambda)=\sum_{k=-N}^{N}a_kS(t+kT)\qquad\text{(13-7)}.$$
**正交原理**（老師說「一定會考一題」）：誤差和每筆資料正交：
$$E\left\{\left[S(t+\lambda)-\sum_ka_kS(t+kT)\right]S(t+nT)\right\}=0\ \Rightarrow\ \sum_{k=-N}^{N}a_kR(kT-nT)=R(\lambda-nT),\quad|n|\le N\qquad\text{(13-8)}.$$

### 5.2 算 MSE 的快速方法

[▶ 18:26](https://youtu.be/dj6_7NXQJCM?t=1106) 考試、平常運算除了正交原理，常要算 MSE。照定義是誤差乘誤差（的共軛）——norm 平方。但一般不這樣算：

> **快速方法**：$P=E\{e\cdot S\}$——誤差乘上**要預測的對象**。

**理由**：$e=S-\hat S$，所以 $E\{e\cdot e\}=E\{eS\}-E\{e\hat S\}$；$\hat S$ 是資料的線性組合，和誤差正交，第二項是 0。用幾何想像也完全正確。很多書和論文直接這樣算。
$$P=E\{e_N(t)S(t+\lambda)\}=R(0)-\sum_ka_kR(\lambda-kT)\qquad\text{(13-10)}.$$
一乘進去取期望值，馬上得到 MSE 和自相關的關係，非常直觀。

> 正交原理講兩件事：(1) 誤差乘資料 = 0；(2) 誤差乘預測對象 = MSE。

### 5.3 頻帶受限：sinc 內插

[▶ 20:59](https://youtu.be/dj6_7NXQJCM?t=1259) 驗證和 Nyquist（老師說 1930 年左右；⚠️ 待確認年份）、Shannon 取樣定理一樣。係數有兩個參數：預測時間 $\lambda$、資料 $k$。

$S$ **頻帶受限**、功率頻譜在頻帶內是平的，$T=\frac\pi\sigma$：自相關是 sinc，$R(kT-nT)$ 在 $k=n$ 時是 1（歸一化）、$k\ne n$ 時是 0。求和只剩一項 $a_n$（$N\to\infty$）：
$$a_n=\frac{\sin\sigma(\lambda-nT)}{\sigma(\lambda-nT)}.$$
就是 sinc 內插。

**提醒**【口頭】：這裡假設功率頻譜是平的。不是平的，自相關就不是 sinc，**sinc 內插從 MSE 角度就不是最好的**。Nyquist 他們提議用 sinc 做內插只是一個方法；頻譜不平時要用別的函數。

【課本補充】p. 583–584：內插誤差可看成誤差濾波器 $E_N(\omega)=e^{j\omega\lambda}-\sum a_ke^{jkT\omega}$ 的輸出，$P=\frac1{2\pi}\int S(\omega)|E_N(\omega)|^2d\omega$（式 (13-11)）——等於用三角多項式（截斷的 Fourier 級數）逼近 $e^{j\omega\lambda}$ 的加權均方誤差。另有 quadrature：用 $N+1$ 個取樣估 $\int_0^bS(t)dt$。

---

## 6. Smoothing：非因果 Wiener 濾波器

[▶ 23:34](https://youtu.be/dj6_7NXQJCM?t=1414) Smoothing 是濾波器的名詞（第 12 章也出現過：data window 和 spectral window——老師說「這個也會考」；spectral window 在頻譜上直接做卷積，讓頻譜比較順）。

**設定**：資料**無限多**（從 $-\infty$ 觀察到 $\infty$，不太合理），資料是要估的對象加雜訊（加性系統在通訊上很常見）：
$$X(t)=S(t)+\nu(t),\qquad\hat S(t)=\int_{-\infty}^{\infty}h(\alpha)X(t-\alpha)\,d\alpha\qquad\text{(13-12)}.$$

**正交原理**：之前資料是 $a$ 到 $b$ 有限的；現在 $-\infty$ 到 $\infty$，得到**卷積**形式：
$$R_{sx}(\tau)=\int h(\alpha)R_{xx}(\tau-\alpha)\,d\alpha\qquad\text{(13-13)}.$$
時域卷積 ⇒ 頻域相乘：

> **非因果 Wiener 濾波器**：
> $$H(\omega)=\frac{S_{sx}(\omega)}{S_{xx}(\omega)}\qquad\text{(13-14)}.$$
> 分子：預測對象跟資料之間的功率頻譜；分母：資料跟資料的功率頻譜。

**為什麼叫 noncausal**：不合理——要預測一個對象，你不可能有未來的資料（什麼都有）。理論上告訴你可以用卷積和傅立葉轉換的關係來做；但後面會講這個其實不太能用。

**訊號和雜訊正交**（$\nu$ 零平均、和 $S$ 獨立）：$S_{sx}=S_{ss}$、$S_{xx}=S_{ss}+S_{\nu\nu}$：
$$H(\omega)=\frac{S_{ss}(\omega)}{S_{ss}(\omega)+S_{\nu\nu}(\omega)},\qquad P=\frac1{2\pi}\int\frac{S_{ss}(\omega)S_{\nu\nu}(\omega)}{S_{ss}(\omega)+S_{\nu\nu}(\omega)}d\omega\qquad\text{(13-16)}.$$
（算 MSE 又用快速方法：誤差乘預測對象的期望值；再轉到頻譜。）

**重要觀念** [▶ 27:11](https://youtu.be/dj6_7NXQJCM?t=1631)：**雜訊的頻譜和訊號的頻譜沒有重疊**，則 $H=1$（訊號頻帶）、$H=0$（雜訊頻帶），$P=0$——可以完全沒有誤差地回復。
- 通訊上最常用：你的頻率跟我不一樣，基本上不受干擾。
- 例【口頭】：兩個樂器發出的頻率不一樣，耳朵馬上分得出來；指揮很厲害，十幾樣樂器頻率不同，一聽就知道哪個樂器發什麼聲音。兩個樂器頻譜完全重疊時就很難區隔。

**§13-1 總結**：線性預測、正交原理、怎麼算 MSE——三個最重要的基礎概念，做任何系統都可能用到。要做非線性預測要自己想怎麼推廣；有時看起來非線性（用微分、用 $X^2$），其實可以變形成線性預測的樣子。

---

## 7. 一頁速查表

| 問題 | 結果 |
|---|---|
| 多筆資料 | $R_{sx_l}=\sum_i\int h_iR_{x_ix_l}$ |
| 用 $S,S'$ 預測 | $a_1=\frac{R(\lambda)}{R(0)}$，$a_2=\frac{R'(\lambda)}{R''(0)}$（$R'(0)=0$） |
| Filtering | $a=\frac{R_{sx}(0)}{R_{xx}(0)}$，不隨時間變 |
| 內插 | $\sum_ka_kR(kT-nT)=R(\lambda-nT)$ |
| MSE 快速算法 | $P=E\{eS\}$ |
| 頻帶受限 | $a_n=\mathrm{sinc}$；頻譜不平時 sinc 非最佳 |
| 非因果 Wiener | $H=\frac{S_{sx}}{S_{xx}}=\frac{S_{ss}}{S_{ss}+S_{\nu\nu}}$；不重疊 ⇒ $P=0$ |

**關鍵步驟**：
- 微分器當濾波器：$R_{ss'}=-R'$、$R_{s's'}=-R''$。
- $E\{e\hat S\}=0$ ⇒ $E\{e^2\}=E\{eS\}$。
- 無限資料 ⇒ 卷積 ⇒ 頻域相除。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 非因果 Wiener 不能用 | 第 39–40 集：因果的預測、Wiener–Hopf |
| 預測、Wold | §13-2 Prediction |

---

## 附：本集一句話總結

> **線性估計的一切都從正交原理來：多筆資料（包括用微分當「走勢」資料）就是解自相關的聯立方程，平穩時係數不隨時間變；內插就是線性預測，頻帶受限且頻譜平時最佳係數正好是 sinc；MSE 可以用「誤差乘預測對象」快速算；有無限資料時得到非因果 Wiener 濾波器 $S_{ss}/(S_{ss}+S_{\nu\nu})$，訊號雜訊頻譜不重疊就能零誤差。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。
2. 老師說 Nyquist「1930 年」的工作：年份待查。

---

*筆記依據陳伯寧老師「隨機過程」Lec 13-1 (2/2) 錄影逐字稿（whisper large-v3-turbo，29:47）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
