---
course: 統計學（數理統計，數學系）
episode: 17
lecture: Lec17
date: 待補
video: https://youtu.be/HKHnWDIGxPs
notes: Hogg 8th ed. Example 4.1.4 均勻 $U(0,\theta)$ 的 MLE（p. 230）；Example 4.1.2 二項（p. 228）；Example 4.1.3 常態（p. 228）；Theorem 6.1.2 MLE 的不變性（p. 358）
---

# 第 17 集 · Lec17：MLE 例題（均勻、二項、常態）與不變性定理 [▶ 影片](https://youtu.be/HKHnWDIGxPs)

← 上一集：[16](16-mle-two-cases-order-statistics.md) ｜ [總目錄](../README.md) ｜ 下一集：[18](18-invariance-examples-umvue.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 17 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:05:04，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.1、§6.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「likelihood」→「Lugly／Ligrid／likely-foo」，「indicator function」照錄，「$\tau$」→「tau／tow」，「二項」→「偶像」，「卡方」照錄，「asymptotically unbiased」→「近視不偏」（＝近似不偏）。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例 1：U(0, θ) 的 MLE](#1-例-1u0-θ-的-mle)
  - [1.1 寫出概似函數（用指示函數）](#11-寫出概似函數用指示函數)
  - [1.2 畫圖找最大值](#12-畫圖找最大值)
  - [1.3 不偏？一致？](#13-不偏一致)
- [2. 例 2：二項分配的 MLE](#2-例-2二項分配的-mle)
- [3. 例 3：常態分配的 MLE](#3-例-3常態分配的-mle)
- [4. MLE 的不變性定理](#4-mle-的不變性定理)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

三個和 MLE 有關的例題，每題都問：MLE 是什麼？不偏嗎？一致嗎？最後講**不變性定理**。

| 例 | 分配 | MLE | 不偏 | 一致 |
|---|---|---|---|---|
| 1 | $U(0,\theta)$ | $Y_n=\max X_i$ | ✗（漸近不偏） | ✓ |
| 2 | $b(n,p)$ | $Y/n$ | ✓ | ✓ |
| 3 | $N(\mu,\sigma^2)$ | $\bar X$；$\frac1n\sum(X_i-\bar X)^2$ | ✓；✗（漸近不偏） | ✓；✓ |

[▶ 01:02](https://youtu.be/HKHnWDIGxPs?t=62) 【口頭】均勻分配在統計裡很特殊：不管用哪種統計方法，處理均勻分配都和其他分配不同，所以常拿來當例子。要熟悉，但觀念要清楚。

[▶ 02:04](https://youtu.be/HKHnWDIGxPs?t=124) 要判斷 MLE 是否不偏、一致，**一定要找出 MLE 的分配**，會用到以前學的很多理論。

---

## 1. 例 1：U(0, θ) 的 MLE

### 1.1 寫出概似函數（用指示函數）

[▶ 03:06](https://youtu.be/HKHnWDIGxPs?t=186) 要找 MLE，先要有概似函數；要有概似函數，先要有 pdf。

$$f(x;\theta)=\begin{cases}\frac1\theta, & 0\le x\le\theta\\ 0, & \text{其他}\end{cases}$$

[▶ 05:08](https://youtu.be/HKHnWDIGxPs?t=308) 為了好處理，用**指示函數**（indicator function）寫：

$$f(x;\theta)=\frac1\theta\,I(0\le x\le\theta),\qquad I(\cdot)=\begin{cases}1, & \text{條件成立}\\ 0, & \text{不成立}\end{cases}$$

**概似函數**（[▶ 06:46](https://youtu.be/HKHnWDIGxPs?t=406)）：獨立 ⇒ 相乘；同分配 ⇒ 都是同一個 $f$：

$$L(\theta)=\prod_{i=1}^n\frac1\theta I(0\le x_i\le\theta)=\frac{1}{\theta^n}\prod_{i=1}^nI(0\le x_i\le\theta).$$

**化簡指示函數的乘積**（[▶ 08:19](https://youtu.be/HKHnWDIGxPs?t=499)）：

- 每個指示函數是 0 或 1。$n$ 個相乘，**每個都是 1** 才是 1，有一個 0 就是 0。
- 所以乘積＝1 ⇔ 每個 $x_i$ 都在 $[0,\theta]$。
- [▶ 09:50](https://youtu.be/HKHnWDIGxPs?t=590) 令 $y_n=\max(x_1,\dots,x_n)$。「每個都 $\le\theta$」⇔「最大的 $\le\theta$」。

$$L(\theta)=\frac{1}{\theta^n}I(0\le y_n\le\theta).$$

[▶ 13:26](https://youtu.be/HKHnWDIGxPs?t=806) **要看成 $\theta$ 的函數**：$y_n\le\theta$ 就是 $\theta\ge y_n$（$\theta$ 可以到 $\infty$）：

$$L(\theta)=\begin{cases}\dfrac{1}{\theta^n}, & y_n\le\theta<\infty\\ 0, & \theta<y_n\end{cases}$$

### 1.2 畫圖找最大值

[▶ 14:59](https://youtu.be/HKHnWDIGxPs?t=899)

- $\theta<y_n$：$L=0$。
- $\theta=y_n$：$L=\frac{1}{y_n^n}$，最高。
- $\theta>y_n$：$\theta^n$ 越來越大，$L$ **遞減**。

所以 $\theta=y_n$ 時最大。換成大寫：

$$\hat\theta_{\text{MLE}}=Y_n=\max(X_1,\dots,X_n).$$

[▶ 17:02](https://youtu.be/HKHnWDIGxPs?t=1022) 這題**不能**用「取 log 微分＝0」：最大值在 $\theta=y_n$，那點左邊不連續、不可微。不是每題都能取 log 微分。碰到均勻分配就照這種方式做：寫成指示函數、畫圖。

### 1.3 不偏？一致？

[▶ 17:33](https://youtu.be/HKHnWDIGxPs?t=1053) 要找 $Y_n$ 的分配。用上一集公式（$U(0,\theta)$ 是連續分配）：

$$f_{Y_n}(y)=n[F(y)]^{n-1}f(y).$$

**$X$ 的分配函數**（[▶ 20:37](https://youtu.be/HKHnWDIGxPs?t=1237)）：pdf 只在 $[0,\theta]$，所以從 0 積：
$$F(x)=\int_0^x\frac1\theta\,dt=\frac x\theta,\quad 0\le x\le\theta.$$

**$Y_n$ 的 pdf**（[▶ 22:07](https://youtu.be/HKHnWDIGxPs?t=1327)）：
$$f_{Y_n}(y)=n\left(\frac y\theta\right)^{n-1}\frac1\theta=\frac{ny^{n-1}}{\theta^n},\quad 0\le y\le\theta.$$
（每個 $X_i\in[0,\theta]$，最大的也在 $[0,\theta]$。）

**期望值**（[▶ 23:41](https://youtu.be/HKHnWDIGxPs?t=1421)）：
$$E(Y_n)=\int_0^\theta y\cdot\frac{ny^{n-1}}{\theta^n}\,dy=\frac{n}{\theta^n}\cdot\frac{\theta^{n+1}}{n+1}=\frac{n}{n+1}\theta\ne\theta.$$
**不是不偏**。但 $\frac{n}{n+1}\to 1$，所以 $E(Y_n)\to\theta$：**漸近不偏**。

**一致**（[▶ 25:11](https://youtu.be/HKHnWDIGxPs?t=1511)）：用 Lec13 定理（漸近不偏＋var → 0 ⇒ 依機率收斂）。

$$E(Y_n^2)=\int_0^\theta y^2\frac{ny^{n-1}}{\theta^n}\,dy=\frac{n}{n+2}\theta^2.$$
$$\text{Var}(Y_n)=\frac{n}{n+2}\theta^2-\left(\frac{n}{n+1}\right)^2\theta^2\to\theta^2-\theta^2=0.$$

所以 $Y_n\xrightarrow{P}\theta$，是 $\theta$ 的**一致**估計量。

[▶ 28:14](https://youtu.be/HKHnWDIGxPs?t=1694) 【口頭】這題的證明過程要很熟悉，以後不同的統計處理常常會用到這個例子。

---

## 2. 例 2：二項分配的 MLE

[▶ 28:44](https://youtu.be/HKHnWDIGxPs?t=1724) $Y\sim b(n,p)$。

【口頭】把它想成只有**一個**樣本（one sample）。所以概似函數就是它的 pdf：

$$L(p)=\binom{n}{y}p^y(1-p)^{n-y}.$$

**取 log**（[▶ 30:17](https://youtu.be/HKHnWDIGxPs?t=1817)）：原本三個東西相乘，微分要用好幾次乘積法則；取 log 變相加：
$$\log L(p)=\log\binom ny+y\log p+(n-y)\log(1-p).$$

**微分令 0**（[▶ 31:17](https://youtu.be/HKHnWDIGxPs?t=1877)）：$\log\binom ny$ 是常數，微分 0；$\log(1-p)$ 的微分要多乘 $-1$：
$$\frac{d}{dp}\log L=\frac yp-\frac{n-y}{1-p}=0.$$
$$y(1-p)=p(n-y)\ \Rightarrow\ y-yp=np-py\ \Rightarrow\ y=np.$$

$$\hat p=\frac Yn.$$

**不偏**（[▶ 33:20](https://youtu.be/HKHnWDIGxPs?t=2000)）：$E(\hat p)=\frac1nE(Y)=\frac{np}{n}=p$。✓

**一致**（[▶ 34:29](https://youtu.be/HKHnWDIGxPs?t=2069)）：常數提出變異數要平方：
$$\text{Var}(\hat p)=\frac{1}{n^2}\text{Var}(Y)=\frac{np(1-p)}{n^2}=\frac{p(1-p)}{n}\to 0.$$
不偏＋var → 0 ⇒ $\hat p\xrightarrow{P}p$。✓

---

## 3. 例 3：常態分配的 MLE

[▶ 35:35](https://youtu.be/HKHnWDIGxPs?t=2135) $X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$，兩個參數 $\mu,\sigma^2$ 都未知。

**概似函數**（[▶ 36:41](https://youtu.be/HKHnWDIGxPs?t=2201)）：
$$L(\mu,\sigma^2)=\prod_{i=1}^n\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x_i-\mu)^2}{2\sigma^2}}=(2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp\left[-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2\right].$$

【口頭】[▶ 38:16](https://youtu.be/HKHnWDIGxPs?t=2296) 要寫成 $\sigma^2$ 的形式（$\sigma=(\sigma^2)^{1/2}$），因為要估的是 $\sigma^2$，不是 $\sigma$。

**取 log**（[▶ 39:49](https://youtu.be/HKHnWDIGxPs?t=2389)）：
$$\log L=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac{1}{2\sigma^2}\sum(x_i-\mu)^2.$$

兩個參數 → 兩個方程式（對 $\mu$、對 $\sigma^2$ 偏微分令 0）。

**對 $\mu$**（[▶ 40:21](https://youtu.be/HKHnWDIGxPs?t=2421)）：前兩項和 $\mu$ 無關；和的微分＝微分的和：
$$\frac{\partial}{\partial\mu}\log L=\frac{1}{\sigma^2}\sum(x_i-\mu)=0\ \Rightarrow\ \sum x_i=n\mu\ \Rightarrow\ \hat\mu=\bar X.$$

**對 $\sigma^2$**（[▶ 42:24](https://youtu.be/HKHnWDIGxPs?t=2544)）：第一個方程式已解出 $\mu$，代入 $\hat\mu$。

【口頭】[▶ 42:54](https://youtu.be/HKHnWDIGxPs?t=2574) 對誰微分要想清楚。對 $x$ 微 $x^2$ 是 $2x$；但對 $x^2$ 微 $x^2$，是把 $x^2$ 當成一個變數，答案是 1。這裡把 $\sigma^2$ 當成一個變數。

$$\frac{\partial}{\partial\sigma^2}\log L=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}\sum(x_i-\bar x)^2=0\ \Rightarrow\ \hat\sigma^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2.$$

**$\hat\mu$ 的性質**（[▶ 45:30](https://youtu.be/HKHnWDIGxPs?t=2730)）：$E(\bar X)=\mu$（不偏）；$\text{Var}(\bar X)=\frac{\sigma^2}{n}\to 0$ ⇒ 一致。

**$\hat\sigma^2$ 不偏？**（[▶ 47:06](https://youtu.be/HKHnWDIGxPs?t=2826)）
$$E(\hat\sigma^2)=\frac{n-1}{n}E\left[\frac{1}{n-1}\sum(X_i-\bar X)^2\right]=\frac{n-1}{n}\sigma^2.$$
不是不偏，但 $\to\sigma^2$：**漸近不偏**（asymptotically unbiased）。

**$\hat\sigma^2$ 的變異數 → 0？**（[▶ 50:23](https://youtu.be/HKHnWDIGxPs?t=3023)）不能直接看，要用技巧：常態樣本有
$$\frac{\sum(X_i-\bar X)^2}{\sigma^2}\sim\chi^2(n-1)\quad(\text{Lec11 證過}).$$
所以
$$\text{Var}(\hat\sigma^2)=\text{Var}\left(\frac{\sigma^2}{n}\cdot\frac{\sum(X_i-\bar X)^2}{\sigma^2}\right)=\frac{\sigma^4}{n^2}\cdot 2(n-1)\to 0.$$
（卡方的變異數＝兩倍自由度。）

漸近不偏＋var → 0 ⇒ $\hat\sigma^2\xrightarrow{P}\sigma^2$，**一致**。

---

## 4. MLE 的不變性定理

[▶ 53:05](https://youtu.be/HKHnWDIGxPs?t=3185) **問題**：已有 $\hat p=Y/n$。如果想要的是 $\sqrt p$、$e^p$、三角函數……的 MLE 呢？

- [▶ 54:37](https://youtu.be/HKHnWDIGxPs?t=3277) 笨方法：把 pdf 裡的 $p$ 改寫成 $(\sqrt p)^2$，對 $\sqrt p$ 微分。但每換一個函數都要重做一次。
- 有沒有辦法直接代進去？

**$\tau(\theta)$ 的參數空間**（[▶ 56:07](https://youtu.be/HKHnWDIGxPs?t=3367)）：
$$T=\{\tau:\ \exists\theta\in\Omega,\ \tau(\theta)=\tau\}=\tau(\Omega),$$
就是 $\tau$ 這個函數的值域。

> **不變性定理**（invariance，[▶ 58:07](https://youtu.be/HKHnWDIGxPs?t=3487)）：若 $\hat\theta$ 是 $\theta$ 的 MLE，且 $\tau$ 是**一對一**函數，則 $\tau(\hat\theta)$ 是 $\tau(\theta)$ 的 MLE。

**證明**（[▶ 58:38](https://youtu.be/HKHnWDIGxPs?t=3518)）：

1. **$\tau(\theta)$ 的概似函數**。$\tau$ 一對一 ⇒ 有反函數，$\theta=\tau^{-1}(\tau(\theta))$：
$$L(\theta;\mathbf x)=L\left(\tau^{-1}(\tau(\theta));\mathbf x\right).$$
把合成函數 $L\circ\tau^{-1}$ 叫做 $L^*$，則 $L^*(\tau;\mathbf x)$ 就是以 $\tau$ 為參數的概似函數，$\tau\in T$。

2. **證 $\tau(\hat\theta)$ 讓 $L^*$ 最大**（[▶ 62:11](https://youtu.be/HKHnWDIGxPs?t=3731)）。對任何 $\tau=\tau(\theta)\in T$：
$$L^*\left(\tau(\hat\theta)\right)=L\left(\tau^{-1}(\tau(\hat\theta))\right)=L(\hat\theta)\ \ge\ L(\theta)=L\left(\tau^{-1}(\tau(\theta))\right)=L^*(\tau).$$
中間的 $\ge$ 是因為 $\hat\theta$ 是 $\theta$ 的 MLE。

3. 所以 $\tau(\hat\theta)$ 是 $L^*$ 在 $T$ 上的最大點，就是 $\tau(\theta)$ 的 MLE。∎

[▶ 64:11](https://youtu.be/HKHnWDIGxPs?t=3851) 有了一個 MLE，就能找很多 MLE。例子下次講。

【課本補充】課本 Theorem 6.1.2（p. 358）的不變性**不要求一對一**：對任何函數 $g$，$g(\hat\theta)$ 都是 $\eta=g(\theta)$ 的 MLE（用「誘導概似函數」定義 $\eta$ 的 MLE）。老師的版本是一對一的特例，證明較簡單。

---

## 5. 一頁速查表

**$U(0,\theta)$**

- $L(\theta)=\theta^{-n}I(\theta\ge y_n)$；$\theta>y_n$ 遞減 ⇒ $\hat\theta=Y_n$。（不能微分。）
- $f_{Y_n}(y)=\frac{ny^{n-1}}{\theta^n}$，$0\le y\le\theta$。
- $E(Y_n)=\frac{n}{n+1}\theta$（漸近不偏），$E(Y_n^2)=\frac{n}{n+2}\theta^2$，$\text{Var}\to 0$ ⇒ 一致。

**$b(n,p)$**：$\frac{d}{dp}\log L=\frac yp-\frac{n-y}{1-p}=0$ ⇒ $\hat p=Y/n$；不偏、$\text{Var}=\frac{p(1-p)}{n}\to 0$。

**$N(\mu,\sigma^2)$**

- $\hat\mu=\bar X$（不偏、一致）。
- $\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2$：$E=\frac{n-1}{n}\sigma^2$（漸近不偏）；$\text{Var}=\frac{2(n-1)\sigma^4}{n^2}\to 0$（用 $\frac{\sum(X_i-\bar X)^2}{\sigma^2}\sim\chi^2(n-1)$）⇒ 一致。
- 技巧：對 $\sigma^2$ 微分時把 $\sigma^2$ 當一個變數。

**不變性**：$\hat\theta$ 是 MLE、$\tau$ 一對一 ⇒ $\tau(\hat\theta)$ 是 $\tau(\theta)$ 的 MLE。
關鍵：$L^*(\tau)=L(\tau^{-1}(\tau))$，$L^*(\tau(\hat\theta))=L(\hat\theta)\ge L(\theta)=L^*(\tau(\theta))$。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 不變性定理 | 下一集的例子（$\sqrt p$ 等） |
| $U(0,\theta)$ 的 $Y_n$ | 充分統計量、區間估計的例子 |
| MLE 的漸近性質 | 課本第 6 章 |

---

## 附：本集一句話總結

> **均勻 $U(0,\theta)$ 的概似函數在 $\theta\ge\max x_i$ 時遞減，所以 MLE 是 $Y_n$（漸近不偏、一致）；二項的 MLE 是 $Y/n$（不偏、一致）；常態的 MLE 是 $\bar X$ 和 $\frac1n\sum(X_i-\bar X)^2$（後者漸近不偏、一致）；若 $\tau$ 一對一，$\tau(\hat\theta)$ 就是 $\tau(\theta)$ 的 MLE。**

---

*筆記依據「統計學」Lec17 錄影逐字稿（whisper large-v3-turbo，1:05:04）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
