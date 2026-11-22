---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 21
lecture: Lec 10-6 Deterministic Signals in Noise & Appendix 10A The Poisson Sum Formula
date: 待補
video: https://youtu.be/EhYHzU_7oaI
notes: Papoulis & Pillai 4th ed. §10-6 Deterministic Signals in Noise（matched filter 式 (10-217)–(10-224)、tapped delay line 式 (10-225)–(10-227)、smoothing 式 (10-228)–(10-241)，pp. 483–487）；Appendix 10A Poisson Sum Formula（式 (10A-1)、(10A-2)，p. 495 附近）
---

# 第 21 集 · Lec 10-6 + 附錄 10A：雜訊中的確定訊號——有色雜訊的 matched filter、tapped delay line（Lagrange 乘數）、平滑濾波器與 bias–variance、Poisson 求和公式 [▶ 影片](https://youtu.be/EhYHzU_7oaI)

← 上一集：[20](20-bandlimited-processes-sampling-theorem-past-samples-random-sampling.md) ｜ [總目錄](README.md) ｜ 下一集：[22](22-factorization-innovations-minimum-phase-regular-process.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 21 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:08:22，whisper large-v3-turbo）＋ Papoulis §10-6（pp. 483–487）、附錄 10A
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「matched filter」→「Match Filter」，「signal-to-noise ratio」→「signal to noise／Signal to Knowledge／signal to down／signal potential ratio」，「Cauchy–Schwarz」→「Colchus-Watt／超區 swath／Colchie Swatch」，「causal」→「cozal／codal」，「tapped delay line」→「Tap Delay Line／type delay line」，「convolution」→「commolution／combolution」，「suboptimal」→「suboptimal」，「Lagrange multiplier」→「Lagrange Multiplied／Motiplyer／modiplier」，「quadratic form」→「quadractic form」，「smoothing」→「smoothie／Smoothing」，「bias」→「BIOS」，「zero mean」→「G-O mean」，「Taylor」→「胎額／胎的／Tiler」，「polynomial」→「polynomial」，「approximate」→「Aproximate／apposimate／Approsimate」，「Papoulis」→「Popolis／propolis」，「parabolic window」→「parabolic window」，「Poisson sum formula」→「prozone sum formula／Prozoned Sum Formula／寡重 someformular」，「aliasing」→「alien 型／A 連性」，「extended Fourier transform」→「extended friction／fully transform」，「unstable」→「unstable」，「wide-sense stationary」→「Y-Sense Stationary」，「white」→「white／坏」。以下一律用正確的字。

> **接上一集**：上一集講帶限過程與取樣。§10-6 回到通訊傳輸的問題：**在雜訊中傳送／估計一個確定的訊號**。兩個問題：(1) 偵測——設計濾波器讓輸出的訊雜比最大（matched filter）；(2) 估計——設計平滑濾波器估計原本的輸入（smoothing），出現 bias 和 variance 的取捨。最後補充附錄 10A 的 Poisson 求和公式。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Matched filter：有色雜訊](#1-matched-filter有色雜訊)
  - [1.1 問題](#11-問題)
  - [1.2 解：Cauchy–Schwarz](#12-解cauchyschwarz)
  - [1.3 白雜訊：傳統的 matched filter](#13-白雜訊傳統的-matched-filter)
- [2. Matched filter 實作上做不到：非因果](#2-matched-filter-實作上做不到非因果)
- [3. Tapped delay line：在可實作的架構下最好](#3-tapped-delay-line在可實作的架構下最好)
  - [3.1 兩階段技巧：分子固定、分母最小](#31-兩階段技巧分子固定分母最小)
  - [3.2 Lagrange 乘數法](#32-lagrange-乘數法)
  - [3.3 解](#33-解)
- [4. 平滑：估計原本的輸入](#4-平滑估計原本的輸入)
  - [4.1 問題與直觀](#41-問題與直觀)
  - [4.2 Bias 與 variance](#42-bias-與-variance)
  - [4.3 假設：對稱、面積 1、Taylor 展開](#43-假設對稱面積-1taylor-展開)
  - [4.4 兩個 Lagrange 乘數：最佳濾波器是拋物線](#44-兩個-lagrange-乘數最佳濾波器是拋物線)
  - [4.5 Near optimal：誤差 $\frac{9N_0}{16T}$](#45-near-optimal誤差-frac9n_016t)
  - [4.6 全正的視窗（moving average、parabolic）的問題](#46-全正的視窗moving-averageparabolic的問題)
- [5. 附錄 10A：Poisson 求和公式](#5-附錄-10apoisson-求和公式)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 有色雜訊的 matched filter | [▶ 00:00](https://youtu.be/EhYHzU_7oaI?t=0) | 式 (10-217)–(10-224)，pp. 483–485 |
| 非因果、tapped delay line | [▶ 07:16](https://youtu.be/EhYHzU_7oaI?t=436) | 式 (10-225)–(10-227)，p. 485 |
| Lagrange 乘數 | [▶ 14:24](https://youtu.be/EhYHzU_7oaI?t=864) | Prob. 10-26 |
| 平滑估計 | [▶ 28:22](https://youtu.be/EhYHzU_7oaI?t=1702) | 式 (10-228)–(10-241)，pp. 485–487 |
| Poisson 求和公式 | [▶ 62:50](https://youtu.be/EhYHzU_7oaI?t=3770) | 附錄 10A |

---

## 1. Matched filter：有色雜訊

### 1.1 問題

[▶ 00:32](https://youtu.be/EhYHzU_7oaI?t=32) 大學部教過，答案大家都知道是 matched filter；因為重要再講一次，但加一點難度：**雜訊不是白的，是有色的** (colored noise)——有的頻率雜訊多、有的少。

- 送 $f(t)$（確定訊號），加上雜訊 $V(t)$（零平均 WSS，功率頻譜 $S_{VV}(\omega)$），收到 $X(t)=f(t)+V(t)$。
- 通過要設計的線性濾波器 $h$，在 $t_0$ 取樣得 $Y(t_0)$。
- **線性**：送 $f$ 得 $Y_f$、送 $V$ 得 $Y_V$，送 $f+V$ 得 $Y_f+Y_V$。所以輸出是「訊號 + 一個加上去的隨機項」。這是用線性濾波器的原因之一：操作上容易；有非線性區的話，雜訊的現象沒辦法預測。【口頭】

$$Y_f(t_0)=\frac1{2\pi}\int F(\omega)H(\omega)e^{j\omega t_0}d\omega,\qquad E\{Y_V^2\}=\frac1{2\pi}\int S_{VV}(\omega)|H(\omega)|^2d\omega.$$

目標：讓**輸出訊雜比**最大
$$\rho^2=\frac{|Y_f(t_0)|^2}{E\{Y_V^2(t_0)\}}.$$

### 1.2 解：Cauchy–Schwarz

[▶ 03:37](https://youtu.be/EhYHzU_7oaI?t=217)

**Step 1：湊項。** 被積函數乘、除 $\sqrt{S_{VV}}$（老師說數位通訊考過這題），目的是湊出能和分母對消的項：
$$|2\pi Y_f(t_0)|^2=\left|\int\frac{F(\omega)}{\sqrt{S_{VV}}}\cdot\sqrt{S_{VV}}H(\omega)e^{j\omega t_0}d\omega\right|^2.$$

**Step 2：Cauchy–Schwarz：**
$$\le\int\frac{|F(\omega)|^2}{S_{VV}(\omega)}d\omega\cdot\int S_{VV}(\omega)|H(\omega)|^2d\omega.$$
第二個積分剛好和分母對消：
$$\rho^2\le\frac1{2\pi}\int\frac{|F(\omega)|^2}{S_{VV}(\omega)}d\omega\qquad\text{(10-223)}.$$

**Step 3：等號**：Cauchy–Schwarz 的兩項成正比（$k$ 是常數）：
$$\sqrt{S_{VV}}H(\omega)=k\frac{F^*(\omega)e^{-j\omega t_0}}{\sqrt{S_{VV}}}\ \Rightarrow\ \boxed{H(\omega)=k\frac{F^*(\omega)}{S_{VV}(\omega)}e^{-j\omega t_0}}\qquad\text{(10-224)}.$$

**意義**【口頭】：
- 多了一個維度：上界和雜訊能量的**倒數**有關。
- 這裡的 match 要 match **兩件事**：原來訊號的格式 $F$，還有**雜訊的功率頻譜**。
- 概念上剛好補償 $S_{VV}$：**雜訊大的頻率最好不要送訊號，雜訊小的頻率多送一點**。
- 給定雜訊頻譜、給定 $f$ 的波形，設計 $H$。這個形式在數位通訊好像沒介紹，通訊系統裡只是用另一種方式呈現。

### 1.3 白雜訊：傳統的 matched filter

[▶ 06:46](https://youtu.be/EhYHzU_7oaI?t=406) 白雜訊 $S_{VV}=\sigma_0^2$（各頻率一樣），不用 match 它：
$$H(\omega)=kF^*(\omega)e^{-j\omega t_0},\qquad h(t)=kf(t_0-t)\qquad\text{(10-222)}.$$
濾波器就是輸入波形**翻轉再平移**——輸入長這樣，matched filter 就長那樣（轉過來）。

【課本補充】(10-221)：此時 $\rho_{\max}^2=E_f/\sigma_0^2$，$E_f=\frac1{2\pi}\int|F|^2$ 是訊號能量。

---

## 2. Matched filter 實作上做不到：非因果

[▶ 07:48](https://youtu.be/EhYHzU_7oaI?t=468)

> **因果濾波器** (causal filter)：有輸入才有輸出（cause and effect），輸入是 0、輸出一定是 0。線性濾波器是因果的 ⇔ $h(\tau)=0$（$\tau<0$）（可以證明）。

**卷積的直觀** [▶ 09:48](https://youtu.be/EhYHzU_7oaI?t=588)：$h_1$ 不為 0 的區域有這麼大，$h_2$ 不為 0 的區域有那麼大；$h_1*h_2$ 不為 0 的區域**只會擴大**（左右各擴大一個 $h_2$ 的寬度），不會縮小。數學上一定可以證明。

- 最佳濾波器在時域是 $f$ 的翻轉和 $S_{VV}^{-1}$ 的反轉換做**卷積**，所以不為 0 的區域會擴大。
- $f$ 本來就從時間 0 開始傳（因果的），翻轉再卷積後，最佳的 $h$ 會延伸到負時間 → **非因果** (non-causal) 濾波器，基本上做不出來。

**所以**：在一個**實作上可能的架構**下，找讓輸出訊雜比最大的參數。從 matched filter 的角度看，這是 **suboptimal**（次佳）——達不到理論上那麼漂亮的結果。

老師說【口頭】：論文裡寫「我的輸出是 matched filter output」，你就知道那很可能做不到；但理論上它是 **benchmark**（最完美情況下的結果）。所以實作的設計最好不叫 optimal filter，可以叫 **best** filter——在某個架構條件下最好的。

---

## 3. Tapped delay line：在可實作的架構下最好

[▶ 08:48](https://youtu.be/EhYHzU_7oaI?t=528) **Tapped delay line**（抽頭延遲線）：一條線上一連串延遲 $D$（clock 同步），每一級拉出來乘一個係數，全部加起來。設計數位濾波器都用這個架構，實作上很方便。（和上一集的二項式形式一模一樣，只是 $m$ 維。）

$$H(\omega)=a_0+a_1e^{-j\omega T}+\cdots+a_me^{-jm\omega T}\qquad\text{(10-225)}.$$
$$Y_f(t_0)=\sum_{i=0}^{m}a_if(t_0-iT),\qquad Y_V(t)=\sum_ia_iV(t-iT).$$

訊雜比
$$\rho^2=\frac{\left(\sum_ia_if(t_0-iT)\right)^2}{\sum_i\sum_ka_ia_kR_{VV}((k-i)T)}.$$

### 3.1 兩階段技巧：分子固定、分母最小

[▶ 14:24](https://youtu.be/EhYHzU_7oaI?t=864) 要最大化 $\frac{f(x)}{g(x)}$，分子分母同時處理比較麻煩。技巧：**先把分子設為常數 $c$，在這個條件下最小化分母**（等同最大化分母的倒數）；再調整 $c$，在每個 $c$ 下都得到最好的，看哪個 $c$ 最好。兩階段做法。

這裡：令 $Y_f(t_0)=\sum a_if(t_0-iT)=c$，找 $a_0,\dots,a_m$ 讓分母（雜訊功率）最小。

### 3.2 Lagrange 乘數法

[▶ 16:58](https://youtu.be/EhYHzU_7oaI?t=1018) 問題變成：最小化 $g(\mathbf{x})$，但 $\mathbf{x}$ 有條件 $f(\mathbf{x})=c$。

- 直接取 $g'=0$ 得到的 $\mathbf{x}$ 可能不符合條件。要引進一個自由度。
- **Lagrange 乘數** (Lagrange multiplier)：加一項 $\lambda(f(\mathbf{x})-c)$。因為 $f(\mathbf{x})=c$，這一項是 0，乘任何數還是 0，**不影響極值**。
- 微分 $g'+\lambda f'=0$，多了 $\lambda$ 可以調整；最後調 $\lambda$ 讓 $f(\mathbf{x})=c$ 成立。
- 為什麼常寫成 multiplier**s** technique（加 s）？因為條件可能有好幾個：$f(\mathbf{x})=c$、$h(\mathbf{x})=d$，就需要兩個乘數 $\lambda_1,\lambda_2$。

老師說【口頭】：通訊常要做最大化／最小化，所以這個技巧非常常用；學資訊理論 (information theory) 時，capacity、entropy 的最大化、傳送 rate 最大，全部都用 Lagrange 乘數。他不把它叫數學技巧，而是**一個很有用的想法**；了解背後的想法，才知道在什麼場合有用。

### 3.3 解

[▶ 19:33](https://youtu.be/EhYHzU_7oaI?t=1173) 目標函數（WSS 雜訊）：
$$\sum_i\sum_ka_ia_kR_{VV}((n-i)T)\cdots-2\lambda\left(\sum_ia_if(t_0-iT)-c\right).$$
（乘 2 只是計算方便，之後會和 $\frac12$ 消掉；一般乘數沒有係數。）

**Step 1：對 $a_n$ 偏微分。** 二次式 $\sum\sum a_ia_k(\cdot)$ 寫成矩陣：$a_1a_1,a_1a_2,a_1a_3;a_2a_1,a_2a_2,\dots$。對 $a_2$ 微分，只剩一行和一列，各給一份；實數自相關左右對稱，兩份相同，合成 2 倍和 2 消掉：
$$\sum_{i=0}^{m}a_iR_{VV}((n-i)T)=\lambda f(t_0-nT),\qquad n=0,1,\dots,m.$$

**Step 2：** 這是 $\mathbf{a}$ 的**多元一次聯立方程式**：$R\mathbf{a}=\lambda\mathbf{f}$。係數矩陣來自雜訊自相關的樣本，假設行列式不為 0（很高機率），
$$\mathbf{a}=\lambda R^{-1}\mathbf{f}.$$

老師的實作提醒【口頭】：這是最直觀的解；但濾波器 40 階以上時，用 MATLAB 直接求反矩陣，解出來會是 **unstable** 的濾波器，係數會跑掉——電腦的精度有限。可以用其他方法解，不一定要用反矩陣。

**Step 3：解 $\lambda$。** 用條件 $\mathbf{a}^T\mathbf{f}=c$：$\lambda\,\mathbf{f}^TR^{-1}\mathbf{f}=c$，所以 $\lambda=\frac{c}{\mathbf{f}^TR^{-1}\mathbf{f}}$。（有兩個等號條件就有兩個乘數、兩個方程式解兩個參數。）

**Step 4：選 $c$。** 代回訊雜比：分子 $c^2$，分母 $\mathbf{a}^TR\mathbf{a}=\lambda^2\mathbf{f}^TR^{-1}\mathbf{f}=\frac{c^2}{\mathbf{f}^TR^{-1}\mathbf{f}}$，$c$ 消掉：
$$\rho^2=\mathbf{f}^TR^{-1}\mathbf{f}.$$
**和 $c$ 無關**——這個例子剛好是特例，$c$ 取多少都一樣，可以成比例地設計。

**合理性**：$R$ 是合法的自相關矩陣，一定非負定，它的反矩陣也是；二次式 (quadratic form) $\mathbf{f}^TR^{-1}\mathbf{f}\ge0$。訊雜比不可能是負的，全部都 match。

【課本補充】(10-227)：課本的結果寫成 $\sum_ia_iR(nT-iT)=kf(t_0-nT)$，$k$ 是任意常數，和上面一致（課本把推導放在習題 Prob. 10-26）。

---

## 4. 平滑：估計原本的輸入

### 4.1 問題與直觀

[▶ 28:22](https://youtu.be/EhYHzU_7oaI?t=1702) 另一個觀點。老師說這和現在的 learning／training 有關：training sequence 可能都有雜訊；網路上很多假資訊（真正訊息加上雜訊），怎麼用大量資訊比對、過濾出真正的資訊？是一模一樣的 modeling。【口頭】

**smoothing**（平滑）：例如序列 2, 6, 33, 1 在某處有很大的跳躍；每三個做平均（$(2+6+33)/3\approx13.7$、$(6+33+1)/3\approx13.3$），跳躍就沒那麼大。濾波器係數都是正的時，就相當於一種平滑。

**不同的問題**：前面是在輸出端的訊雜比；現在要用濾波器**估計原來的輸入** $f(t_0)$（所以叫 filter input）：
$$Y(t)=\int X(t-\tau)h(\tau)\,d\tau,\qquad X=f+V,\qquad\text{目標：}Y(t_0)\approx f(t_0).$$

**為什麼平均有幫助**【口頭】：某個值加雜訊 1、加雜訊 2、加雜訊 3，三個平均：$\frac{3\theta}{3}=\theta$ 不變；雜訊 $\frac{n_1+n_2+n_3}{3}$ 的變異數會降。所以用很多其他地方的值做平均，讓雜訊漸漸消失，而原來的數值（如果穩定）不會改變。

**雜訊假設**：零平均**白雜訊**，可以時變：$R_{VV}(t_1,t_2)=q(t_1)\delta(t_1-t_2)$（對推導沒影響）。

### 4.2 Bias 與 variance

[▶ 33:29](https://youtu.be/EhYHzU_7oaI?t=2009) 誤差
$$e=E\left\{[Y(t_0)-f(t_0)]^2\right\}=E\left\{[Y_f(t_0)+Y_V(t_0)-f(t_0)]^2\right\}.$$
$Y_V$ 零平均，交叉項取期望值為 0（$(a+b)^2$ 的 $2ab$ 消掉）：
$$e=\underbrace{\left[Y_f(t_0)-f(t_0)\right]^2}_{b^2}+\underbrace{E\{Y_V^2(t_0)\}}_{\sigma^2}.$$

- $b=\int f(t_0-\tau)h(\tau)d\tau-f(t_0)$ 叫 **bias**（偏差）：**完全沒有雜訊**時還是有的偏差。老師的比喻：「什麼資訊都給你了，你還是有個基本的偏見，就是不願意承認。」
- $\sigma^2=\int q(t_0-\tau)h^2(\tau)d\tau$（Theorem 9-2，雜訊經過兩次濾波；假設實數，沒有共軛）叫 **variance**（變異）：在 bias 左右的變異，由雜訊造成。
- Detection／estimation 會告訴你：兩者是**取捨** (trade-off)。一個好方法到這個階段，再改善只能改其中一個：改善 variance，bias 可能變大，反之亦然。整體誤差是兩者的和。

### 4.3 假設：對稱、面積 1、Taylor 展開

[▶ 36:36](https://youtu.be/EhYHzU_7oaI?t=2196) 這裡的技巧和 detection／estimation 教的不一樣：我們可以**設計濾波器**，所以可以假設它符合某些條件——一方面方便求解，一方面實作上也合理。

**假設 1（濾波器形式）**：
$$h(-\tau)=h(\tau),\qquad\int_{-T}^{T}h(\tau)\,d\tau=1,\qquad h=0\ (|\tau|>T)\qquad\text{(10-231)}.$$
對中點左右對稱、總面積 1、有限寬度。（這是非因果的，為了推導方便；實作上就做成 $(0,2T)$、對中間對稱的因果濾波器。）

**假設 2**：雜訊不時變，$q(t)=q$（白雜訊強度，老師寫 $\frac{N_0}{2}$）。

**假設 3（Taylor 展開）**：要估計的 $f$ 可微，在 $t_0$ 展開到二階，三階以上忽略：
$$f(t_0-\tau)\approx f(t_0)-\tau f'(t_0)+\frac{\tau^2}{2}f''(t_0).$$
課本寫成近似（$\approx$）。老師說：這在設計數位濾波器時很常用——把要估計的東西變成**多項式**；濾波器本身也是多項式，兩者就容易 match。

**代入 bias**：
$$b=f(t_0)\left[\int h-1\right]-f'(t_0)\int\tau h(\tau)d\tau+\frac{f''(t_0)}{2}\int\tau^2h(\tau)d\tau.$$
- 第一項：面積 1 → 0。（老師舉例：影像處理、line coding 時濾波器係數 $(-1,2,-1)$ 總和是 0 就不對，$(-1,3,-1)$ 總和是 1 比較好。）
- 第二項：對稱，$\tau h(\tau)$ 對中點積分 → 0。
- 只剩第三項：
$$b\approx\frac{f''(t_0)}{2}M,\quad M=\int_{-T}^{T}\tau^2h(\tau)d\tau;\qquad\sigma^2\approx q\int_{-T}^{T}h^2(\tau)d\tau\qquad\text{(10-233)}.$$

（不一定要用 Taylor 展開，用別的方式把 $f$ 變成多項式也可以；Taylor 只是方便，用微分得到係數。）

### 4.4 兩個 Lagrange 乘數：最佳濾波器是拋物線

[▶ 40:41](https://youtu.be/EhYHzU_7oaI?t=2441) 要最小化 $e=\frac{M^2f''^2}{4}+q\int h^2$。同樣的技巧：把 bias 設為常數，$M=\int\tau^2h=C$，去最小化 variance。**兩個等號條件 → 兩個乘數**：
$$\int h=1,\qquad\int\tau^2h=C.$$
$$J=q\int h^2(\tau)d\tau-\lambda_1\left(\int h-1\right)-\lambda_2\left(\int\tau^2h-C\right).$$
對每一點 $h(\tau)$ 微分（老師說：積分好像不能直接對它微分，用直觀的延伸——就像二次式矩陣只剩一行一列）：
$$2q\,h(\tau)-\lambda_1-\lambda_2\tau^2=0\ \Rightarrow\ h(\tau)=\frac{\lambda_1+\lambda_2\tau^2}{2q}.$$

**最佳濾波器是 $\tau$ 的二次式（拋物線）**，$\lambda_1,\lambda_2$ 由兩個條件（二元一次聯立方程式）解出（多項式積分很容易，$\int\tau^2=\frac{\tau^3}{3}$……）。

老師要強調的直觀【口頭】：**要估計的東西是多項式，濾波器去 match 它，最好的濾波器也是多項式**。所以**多項式逼近** (polynomial approximation) 是很有用的概念：他看過論文把不規則的圖形用六階多項式逼近，再設計濾波器去對付它，最好的也是多項式。數值分析裡有各種多項式逼近（Lagrange form 等），各有利弊。

**和課本的差別**：課本標題叫 smoothing，要求 $h(t)>0$（全正）。老師的設計**不保證全正**：拋物線頂點在 $\tau=0$，可能**邊緣是負的**。意義：要估中間這個值，把最邊緣的地方稍微扣掉一點，免得估得太大、超過太多。要全正的話（課本），需要額外條件：頂點大於 0、邊界也大於 0，$C$ 要在這個條件底下找。

### 4.5 Near optimal：誤差 $\frac{9N_0}{16T}$

[▶ 48:59](https://youtu.be/EhYHzU_7oaI?t=2939) 正規化：$\bar C=C/T^2$、$v=\tau/T$，積分範圍變 $(-1,1)$。誤差是 $\bar C$ 的二次式（拋物線），取頂點得最小值，代回去式子很醜，含一個參數
$$a\propto\frac{[f''(t_0)]^2T^5}{N_0}$$
（和要估計訊號的二次微分、雜訊 $N_0$、視窗 $T$ 都有關）。$a$ 很大時，忽略帶 $a$ 的項，就得到乾淨的結果。

**Near optimal 濾波器**（老師的，課本沒有）：把 $a$ 拿掉、讓濾波器係數是常數，不隨 $f''$、$N_0$ 調整。

以下的係數**不是逐字稿內容**，是依「面積 1、二階無偏（$\int\tau^2h=0$）、最小化 $\int h^2$」推導補上的（老師口述的係數聽不清楚；推得的誤差和老師說的 $\frac{9N_0}{16T}$ 一致）：

令 $h=\alpha+\beta\tau^2$。$\int_{-T}^{T}h=2\alpha T+\frac{2\beta T^3}{3}=1$，$\int\tau^2h=\frac{2\alpha T^3}{3}+\frac{2\beta T^5}{5}=0$，解得 $\alpha=\frac{9}{8T}$、$\beta=-\frac{15}{8T^3}$：
$$h(\tau)=\frac{3}{8T}\left(3-\frac{5\tau^2}{T^2}\right),\quad|\tau|\le T.$$
- 邊緣（$|\tau|>\sqrt{3/5}\,T$）是**負的**。
- $\int h^2=\frac{9}{8T}$，所以 variance $=\frac{N_0}{2}\cdot\frac{9}{8T}=\frac{9N_0}{16T}$；bias（到二階）是 0。

> **Near optimal 的誤差**：$e=\dfrac{9N_0}{16T}$，和視窗大小 $T$ **成反比**，是不偏估計 (unbiased)；$T\to\infty$ 時誤差 $\to0$。

**解讀**【口頭】：$T$ 是視窗大小——做 machine learning 時要看多寬的資料（左右看）來預測這一點。用 1 萬筆和 2 萬筆資料估計，照理 2 萬筆的誤差要更低。這裡誤差和 $\frac1T$ 成正比：2 萬筆降到一半、3 萬筆降到三分之一。合理。

### 4.6 全正的視窗（moving average、parabolic）的問題

[▶ 51:00](https://youtu.be/EhYHzU_7oaI?t=3060)

**課本的濾波器一定是正的**（weighted average）。問題：**視窗越大，估計誤差不一定越小**——好不容易收集 10 萬筆資料，反而比用 1 萬筆估得更差。

**Moving average**：$h(\tau)=\frac{1}{2T}$（$|\tau|\le T$），完全信任每個值、而且一樣信任。代公式：
$$e=b^2+\sigma^2\approx\frac{T^4}{36}[f''(t_0)]^2+\frac{q}{2T}.$$
有 $T^4$ 和 $\frac1T$ 兩項，對 $T$ 微分等於 0，有一個**最好的視窗** $T_m$；比它大，多拿的資料沒有用（大家都一樣信任）。

**Parabolic window**（Papoulis 自己提出，有些 estimation 書也教）：在全正的條件下最好的濾波器，二次拋物線。誤差也是 $T^4$ 加 $\frac1T$ 的樣子，一樣有最好的視窗。

**比較四個濾波器**（視窗都拉到 $(-1,1)$）：

| 濾波器 | 形狀 | 誤差 |
|---|---|---|
| Optimal（老師） | 拋物線，有正有負 | 含 $a$ |
| Near optimal（老師） | $\frac38(3-5v^2)$，常數係數 | $\frac{9N_0}{16T}$，$T\to\infty$ 時 $\to0$ |
| Moving average | $\frac12$ | 有最佳 $T_m$，不隨 $T$ 增大而減小 |
| Parabolic（Papoulis） | $\frac34(1-v^2)$ | 有最佳 $T_m$；比 moving average 只改善一點點 |

老師說 parabolic 只比 moving average 改善一點點（他算的係數約從 0.266 到 0.251），而 moving average 實作很簡單；但兩者都是常數最小值，不能隨 $T$ 增大而減小。

**結論**【口頭】：全正的視窗（不管 moving average 或 parabolic），把視窗越放越大、看的資料越來越多時，估計不一定越準，因為全部都設成正的權重。如果願意**有正有負**——離要估計的點近的給正權重（相信它）、遠的給一些負權重（超過了把它扣回來）——結果就比較像直觀預期：資料越多誤差越小，無限多時誤差趨於 0。老師說：要做適當的取捨，不能信任每個人，世界很險惡。

【課本補充】pp. 486–487：
- 正規化 $w(t)=Th(Tt)$，$M_w=\int_{-1}^1t^2w$、$E_w=\int_{-1}^1w^2$，$e=\frac14T^4M_w^2[f'']^2+\frac{E_w}{T}q$（式 (10-237)），最小在 $T_m=\left(\frac{E_wq}{M_w^2[f'']^2}\right)^{1/5}$（10-238）。
- **two-to-one rule**：$T=T_m$ 時，估計誤差的標準差等於 bias 的兩倍，$\sigma=2b$（10-239）。
- Moving average：$M_w=\frac13$、$E_w=\frac12$，$T_m=\sqrt[5]{\frac{9q}{2[f'']^2}}$，$e=5b^2=\frac{5q}{8T_m}$（10-240）。
- Parabolic window：$w(t)=0.75(1-t^2)$，$E_w=\frac35$、$M_w=\frac15$（10-241），是在 $w>0$、$E_w$ 固定下讓 $M_w$ 最小的形狀；最佳濾波器 $h(t)=\frac{1}{T_m}w(t/T_m)$，因為 $T_m$ 依 $t$ 而變，是時變的。

---

## 5. 附錄 10A：Poisson 求和公式

[▶ 62:50](https://youtu.be/EhYHzU_7oaI?t=3770) 常用的工具，補充在這裡。

> **Poisson 求和公式** (Poisson sum formula)：若 $F(u)=\int f(x)e^{-jux}dx$，則對任何 $c$，
> $$\sum_{n=-\infty}^{\infty}f(x+nc)=\frac1c\sum_{n=-\infty}^{\infty}F(nu_0)e^{jnu_0x},\qquad u_0=\frac{2\pi}{c}\qquad\text{(10A-1)}.$$

- 左邊：把 $f$ **重複、疊加**（$n=0,1,2,-1,\dots$）——通訊上就是 **aliasing** 的概念。
- 右邊：$F(nu_0)$ 是以 $u_0$ 為單位對 $F$ **取樣**，用這些整數點做內插，就完美回復 aliasing 之後的結果。
- 所以**取樣定理其實是 Poisson 求和公式的變形**；這是**確定的**（不是隨機的）相等，數學上完美的公式。
- 通訊上用的就是它：離散時間自相關經過傅立葉級數得到離散頻譜，它是原來連續頻譜的 aliasing 疊加（第 15 集）。取 $c=2\pi$ 就得到通訊上給的公式；取樣週期不是整數時，把 $2\pi$ 換成別的 $c$ 就好。
- 老師說：很多理論原來在數學端已經有結果，工程端拿來用。證明留給大家自己看。

**關於 extended Fourier transform 的提醒** [▶ 63:20](https://youtu.be/EhYHzU_7oaI?t=3800)：Poisson 求和公式要 $f$、$F$ 是嚴謹的傅立葉轉換對。老師以前說過 extended Fourier transform（為了讓 1 和 delta 成為轉換對，用極限處理）的定義不嚴謹；作業第 1 題 (c) 用一個例子讓大家驗證：這種定義是 case by case 的，不是像「重力加速度 9.8」那樣在任何地方都成立的 rule，有些情況會不成立。

【課本補充】證明（附錄 10A）：
1. $\sum_n\delta(x+nc)=\frac1c\sum_ne^{jnu_0x}$（10A-2）：左邊是週期 $c$ 的函數，傅立葉級數係數是 $\frac1c\int_{-c/2}^{c/2}\delta(x)e^{-jnu_0x}dx=\frac1c$。
2. 兩邊和 $f$ 卷積：$\delta(x+nc)*f(x)=f(x+nc)$；$e^{jnu_0x}*f(x)=e^{jnu_0x}F(nu_0)$。得 (10A-1)。

---

## 6. 一頁速查表

### Matched filter

| 雜訊 | 最佳 $H(\omega)$ | 最大訊雜比 |
|---|---|---|
| 有色 $S_{VV}$ | $k\frac{F^*(\omega)}{S_{VV}(\omega)}e^{-j\omega t_0}$ | $\rho^2=\frac1{2\pi}\int\frac{\lvert F\rvert^2}{S_{VV}}d\omega$ |
| 白 $\sigma_0^2$ | $kF^*(\omega)e^{-j\omega t_0}$，$h=kf(t_0-t)$ | $E_f/\sigma_0^2$ |

- 關鍵：乘除 $\sqrt{S_{VV}}$ 後 Cauchy–Schwarz；雜訊大的頻率少送。
- 卷積只擴大支撐集 → 最佳解非因果 → 實作用 tapped delay line（suboptimal、best）。

### Tapped delay line

- $H=\sum_{i=0}^ma_ie^{-ji\omega T}$；分子固定 $=c$、最小化雜訊功率；Lagrange：$\sum_ia_iR_{VV}((n-i)T)=\lambda f(t_0-nT)$。
- $\mathbf{a}=\lambda R^{-1}\mathbf{f}$，$\rho^2=\mathbf{f}^TR^{-1}\mathbf{f}$（與 $c$ 無關）。

### Lagrange 乘數

最小化 $g(\mathbf{x})$ s.t. $f_k(\mathbf{x})=c_k$：$\nabla g+\sum_k\lambda_k\nabla f_k=0$，再用條件解 $\lambda_k$。

### 平滑

- $e=b^2+\sigma^2$；$b\approx\frac{f''}{2}\int\tau^2h$，$\sigma^2\approx q\int h^2$（$h$ 對稱、面積 1）。
- 兩個乘數 → $h(\tau)=\frac{\lambda_1+\lambda_2\tau^2}{2q}$（拋物線）。
- Near optimal：$h=\frac{3}{8T}(3-\frac{5\tau^2}{T^2})$，$e=\frac{9N_0}{16T}$，無偏、$\to0$。
- 全正視窗（moving average $\frac1{2T}$、parabolic $\frac{3}{4T}(1-\frac{\tau^2}{T^2})$）：有最佳 $T_m$，資料多不一定好；two-to-one rule $\sigma=2b$。

### Poisson 求和公式

$\sum_nf(x+nc)=\frac1c\sum_nF(nu_0)e^{jnu_0x}$，$u_0=\frac{2\pi}c$；取樣定理、aliasing 的根源。關鍵：$\sum\delta(x+nc)=\frac1c\sum e^{jnu_0x}$ 再卷積 $f$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 因果性、非因果的最佳解 | 下一集：§11-1 分解與創新（因果、最小相位濾波器） |
| $R\mathbf{a}=\lambda\mathbf{f}$（Toeplitz 方程式） | §13-2 預測（Yule–Walker、Wiener 濾波器） |
| bias–variance 取捨 | §12-2 頻譜估計 |
| Lagrange 乘數 | §12-4 最大熵、資訊理論 |

---

## 附：本集一句話總結

> **雜訊中的確定訊號：要讓輸出訊雜比最大，最佳濾波器 $H=kF^*e^{-j\omega t_0}/S_{VV}$ 同時 match 訊號和雜訊頻譜，但它是非因果的，實作用 tapped delay line 配合 Lagrange 乘數得到 $\mathbf{a}\propto R^{-1}\mathbf{f}$；要估計原本的輸入則是 bias 與 variance 的取捨，最佳平滑濾波器是有正有負的拋物線，誤差 $\frac{9N_0}{16T}$ 隨資料增加趨於 0，而全正的視窗（moving average、parabolic）反而有最佳視窗、資料多不一定好。**

---

## ⚠️ 待確認清單

1. [▶ 52:02](https://youtu.be/EhYHzU_7oaI?t=3122) 老師最佳／near optimal 濾波器的係數口述聽不清楚；筆記的 $\frac{3}{8T}(3-\frac{5\tau^2}{T^2})$ 是依條件推導，誤差 $\frac{9N_0}{16T}$ 與老師一致。
2. [▶ 58:11](https://youtu.be/EhYHzU_7oaI?t=3491) 老師比較 moving average 與 parabolic 時說的係數 0.266、0.251 是什麼量，逐字稿沒說清楚。
3. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 10-6 & 附錄 10A 錄影逐字稿（whisper large-v3-turbo，1:08:22）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
