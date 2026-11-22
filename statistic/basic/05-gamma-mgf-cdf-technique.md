---
course: 統計學（數理統計，數學系）
episode: 5
lecture: Lec05
date: 待補
video: https://youtu.be/JUV6MVs7JFM
notes: Hogg 8th ed. §3.3 Γ 分配的 mgf、mean、variance（p. 175）；§3.3.1 卡方分配的 mgf、mean、variance（p. 178–179）；§1.7.2 連續型的變數變換（分配函數法，p. 53）；§3.4 標準化 $Z=(X-\mu)/\sigma$（p. 186–187）
---

# 第 5 集 · Lec05：Gamma 與卡方的 mgf；分配函數法 [▶ 影片](https://youtu.be/JUV6MVs7JFM)

← 上一集：[04](04-mgf-bernoulli-binomial-poisson-normal.md) ｜ [總目錄](../README.md) ｜ 下一集：[06](06-mgf-uniqueness-random-vectors-independence.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 5 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（30:29，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.7.2、§3.3、§3.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「$\alpha$」→「阿化／阿華」，「卡方」→「卡荒／卡王／卡灣」，「variance」→「valence」，「mean」→「mine／命」，「$e$」→「1」（例如「1的負β分之x」＝$e^{-x/\beta}$），「β等於all／or」＝$\beta=2$。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Gamma 分配的 mgf](#1-gamma-分配的-mgf)
- [2. Gamma 的 mean 和 variance](#2-gamma-的-mean-和-variance)
- [3. 卡方分配的 mgf、mean、variance](#3-卡方分配的-mgfmeanvariance)
- [4. 新問題：Y＝g(X) 的分配](#4-新問題yg-x-的分配)
- [5. 分配函數法](#5-分配函數法)
- [6. 例：標準化常態變數](#6-例標準化常態變數)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本對應 |
|---|---|
| Gamma 的 mgf、mean、variance | §3.3，p. 175 |
| 卡方的 mgf、mean、variance | §3.3.1，p. 178–179 |
| 求 $Y=g(X)$ 的 pdf：分配函數法 | §1.7.2，p. 53 |
| $X\sim N(\mu,\sigma^2)$ ⇒ $\frac{X-\mu}{\sigma}\sim N(0,1)$ | §3.4，p. 187 |

---

## 1. Gamma 分配的 mgf

[▶ 00:30](https://youtu.be/JUV6MVs7JFM?t=30) 複習：

$$X\sim\Gamma(\alpha,\beta):\quad f(x)=\begin{cases}\dfrac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}, & x>0\\ 0, & \text{其他}\end{cases}$$

- pdf 定義在整個 $\mathbb{R}$。常常只寫 $x>0$ 那段，其他是 0 要自己知道。
- [▶ 02:01](https://youtu.be/JUV6MVs7JFM?t=121) $\alpha,\beta$ 叫**參數**（parameter），只要是正實數就好。

[▶ 02:33](https://youtu.be/JUV6MVs7JFM?t=153) **重點**：看到長這樣的函數就知道它是 pdf。所以對任何 $\alpha>0,\beta>0$：

$$\int_0^\infty\frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}\,dx=1.\tag{★}$$

**mgf**（[▶ 03:35](https://youtu.be/JUV6MVs7JFM?t=215)）：

**Step 1**：照定義（只積 pdf 大於 0 的 $(0,\infty)$）：
$$M(t)=E(e^{tX})=\int_0^\infty e^{tx}\frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}\,dx.$$

【口頭】[▶ 04:06](https://youtu.be/JUV6MVs7JFM?t=246) 隨機變數一律寫大寫；$t$ 是實數常數；取期望值時 $X$ 改小寫。

**Step 2**：[▶ 05:10](https://youtu.be/JUV6MVs7JFM?t=310) 兩個指數合併，並把 $x$ 以外的東西放到分母（因為 Gamma pdf 的指數是 $-x/(\text{某數})$）：
$$tx-\frac{x}{\beta}=-\frac{x(1-\beta t)}{\beta}=-\frac{x}{\beta/(1-\beta t)}.$$
令新的 $\beta^*=\dfrac{\beta}{1-\beta t}$。

**Step 3**：[▶ 06:15](https://youtu.be/JUV6MVs7JFM?t=375) 湊成 $\Gamma(\alpha,\beta^*)$ 的 pdf。pdf 裡 $\beta$ 的位置要一致：指數是 $\beta^*$，前面就要是 $(\beta^*)^\alpha$。原本前面只有 $\beta^\alpha$，所以補乘再除回來：
$$\frac{1}{\beta^\alpha}=\frac{1}{(\beta^*)^\alpha}\cdot\left(\frac{\beta^*}{\beta}\right)^\alpha=\frac{1}{(\beta^*)^\alpha}(1-\beta t)^{-\alpha}.$$
所以
$$M(t)=(1-\beta t)^{-\alpha}\int_0^\infty\frac{1}{\Gamma(\alpha)(\beta^*)^\alpha}x^{\alpha-1}e^{-x/\beta^*}\,dx.$$

**Step 4**：[▶ 07:46](https://youtu.be/JUV6MVs7JFM?t=466) 要用 (★)，需要 $\beta^*>0$：
$$\frac{\beta}{1-\beta t}>0\iff 1-\beta t>0\iff t<\frac1\beta.$$
這時積分是 1：

$$\boxed{M(t)=(1-\beta t)^{-\alpha},\qquad t<\frac{1}{\beta}}$$

[▶ 08:17](https://youtu.be/JUV6MVs7JFM?t=497) $(-\infty,1/\beta)$ 包含 0 附近的區間，所以可以用「微分令 $t=0$」的定理。【口頭】pdf 和 mgf 都要會背。

---

## 2. Gamma 的 mean 和 variance

[▶ 09:22](https://youtu.be/JUV6MVs7JFM?t=562)

**一次微分**：$-\alpha$ 拿下來，次方減 1，再乘裡面的微分 $-\beta$，負負得正：
$$M'(t)=\alpha\beta(1-\beta t)^{-\alpha-1},\qquad \mu=M'(0)=\alpha\beta.$$

**二次微分**（[▶ 10:24](https://youtu.be/JUV6MVs7JFM?t=624)）：$-(\alpha+1)$ 拿下來，再乘 $-\beta$：
$$M''(t)=\alpha(\alpha+1)\beta^2(1-\beta t)^{-\alpha-2},\qquad E(X^2)=M''(0)=\alpha(\alpha+1)\beta^2.$$

**variance**：
$$\sigma^2=\alpha(\alpha+1)\beta^2-(\alpha\beta)^2=\alpha^2\beta^2+\alpha\beta^2-\alpha^2\beta^2=\alpha\beta^2.$$

[▶ 11:24](https://youtu.be/JUV6MVs7JFM?t=684) 【口頭】證一兩次就記得。把所有分配的 pdf、mgf、mean、variance 抄起來用背的，一定會弄錯（不知道是 $-1$ 還是 $-2$）。分配就這幾個，mgf 用途很多，會常常用。

---

## 3. 卡方分配的 mgf、mean、variance

[▶ 12:27](https://youtu.be/JUV6MVs7JFM?t=747) 卡方是 Gamma 取 $\beta=2$、$\alpha=r/2$。直接代入，不用再導：

| | Gamma$(\alpha,\beta)$ | $\chi^2(r)$（$\alpha=r/2$，$\beta=2$） |
|---|---|---|
| mgf | $(1-\beta t)^{-\alpha}$，$t<1/\beta$ | $(1-2t)^{-r/2}$，$t<1/2$ |
| mean | $\alpha\beta$ | $\frac r2\cdot 2=r$ |
| variance | $\alpha\beta^2$ | $\frac r2\cdot 4=2r$ |

[▶ 13:32](https://youtu.be/JUV6MVs7JFM?t=812) 記法：**自由度就是卡方的平均數；自由度的兩倍就是變異數。**

---

## 4. 新問題：Y＝g(X) 的分配

[▶ 14:03](https://youtu.be/JUV6MVs7JFM?t=843) 新主題（還是機率的部分）。

- $X$ 是隨機變數，$g$ 是實數函數，$Y=g(X)$ 也是隨機變數（上一次講過）。上一次講它的期望值；這次要找它的**分配**。
- [▶ 15:04](https://youtu.be/JUV6MVs7JFM?t=904) 複習：離散型 $f(x)=P(X=x)$；連續型 $F(x)=\int_{-\infty}^xf(t)\,dt$。我們考慮的隨機變數一定有 pdf。
- [▶ 16:37](https://youtu.be/JUV6MVs7JFM?t=997) $Y$ 也是隨機變數，所以也有 pdf。**問題：$Y$ 的 pdf 是什麼？**

方法有很多。這次講**分配函數法**（the cdf technique）。

---

## 5. 分配函數法

[▶ 17:38](https://youtu.be/JUV6MVs7JFM?t=1058)

**原理**：$X$ 連續型，

$$F(x)=\int_{-\infty}^{x}f(t)\,dt.$$

兩邊對 $x$ 微分。由**微積分基本定理**（積分上限的導數＝把上限代進被積函數）：

$$F'(x)=f(x).$$

> **連續型：分配函數的導數就是 pdf。**

所以，就算不知道 pdf，只要找得到分配函數，微分就是 pdf。

**做法**（[▶ 19:11](https://youtu.be/JUV6MVs7JFM?t=1151)）：要找 $Y=g(X)$ 的 pdf：

1. 寫出 $Y$ 的分配函數，並用 $Y=g(X)$ 換成 $X$ 的事件：
$$G(y)=P(Y\le y)=P\left(g(X)\le y\right).$$
2. 用 $X$ 的已知 pdf 算出這個機率。
3. 微分：$g_Y(y)=G'(y)$。

---

## 6. 例：標準化常態變數

[▶ 20:42](https://youtu.be/JUV6MVs7JFM?t=1242)

> **定理**：$X\sim N(\mu,\sigma^2)$（$\mu$ 是 mean，$\sigma^2$ 是 variance），則
> $$Z=\frac{X-\mu}{\sigma}\sim N(0,1).$$

「常態變數減掉平均數、除以標準差，是標準常態。」

**證明**（分配函數法）：

**Step 1：$Z$ 的分配函數換成 $X$ 的事件**（[▶ 22:13](https://youtu.be/JUV6MVs7JFM?t=1333)）
$$F_Z(z)=P(Z\le z)=P\left(\frac{X-\mu}{\sigma}\le z\right)=P(X\le\mu+\sigma z).$$
（$\sigma>0$，乘過去不等號不變。）

**Step 2：用 $X$ 的 pdf 寫成積分**（[▶ 23:49](https://youtu.be/JUV6MVs7JFM?t=1429)）
$$F_Z(z)=\int_{-\infty}^{\mu+\sigma z}\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]dx.$$
這個積分算不出封閉式，但**可以微分**，這就夠了。

**Step 3：微分**（[▶ 26:56](https://youtu.be/JUV6MVs7JFM?t=1616)）。用微積分基本定理加連鎖律：
$$\frac{d}{dz}\int_{-\infty}^{h(z)}f(t)\,dt=f\left(h(z)\right)h'(z).$$
這裡 $h(z)=\mu+\sigma z$，$h'(z)=\sigma$。把被積函數裡的 $x$ 換成 $\mu+\sigma z$：
$$f_Z(z)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(\mu+\sigma z-\mu)^2}{2\sigma^2}\right]\cdot\sigma.$$

**Step 4：化簡**（[▶ 27:59](https://youtu.be/JUV6MVs7JFM?t=1679)）：$\sigma$ 消掉；$\mu$ 消掉；$(\sigma z)^2=\sigma^2z^2$，和分母的 $\sigma^2$ 消掉：
$$f_Z(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2},\qquad z\in\mathbb{R}.$$

**Step 5：認出分配**（[▶ 28:29](https://youtu.be/JUV6MVs7JFM?t=1709)）：對照 $N(\mu,\sigma^2)$ 的 pdf，這是 mean $0$、variance $1$ 的常態，即 $N(0,1)$。∎

[▶ 29:30](https://youtu.be/JUV6MVs7JFM?t=1770) 這是一種方法，還有別的方法，下次講。

---

## 7. 一頁速查表

**Gamma 與卡方**

| | mgf | 關鍵一步 | mean | var |
|---|---|---|---|---|
| $\Gamma(\alpha,\beta)$ | $(1-\beta t)^{-\alpha}$，$t<1/\beta$ | 指數合併成 $-x/\beta^*$，$\beta^*=\frac{\beta}{1-\beta t}$，湊成 Gamma pdf | $\alpha\beta$ | $\alpha\beta^2$ |
| $\chi^2(r)$ | $(1-2t)^{-r/2}$，$t<1/2$ | 代 $\alpha=r/2,\beta=2$ | $r$ | $2r$ |

**分配函數法**（連續型）

1. $G(y)=P(g(X)\le y)$，換成 $X$ 的事件。
2. 用 $X$ 的 pdf 寫成積分。
3. $g_Y(y)=G'(y)$。

關鍵：$F'=f$（微積分基本定理）；$\dfrac{d}{dz}\int_{-\infty}^{h(z)}f=f(h(z))h'(z)$。

**標準化**：$X\sim N(\mu,\sigma^2)$ ⇒ $\dfrac{X-\mu}{\sigma}\sim N(0,1)$。

關鍵一步：$P\left(\frac{X-\mu}{\sigma}\le z\right)=P(X\le\mu+\sigma z)$，微分後乘上 $h'(z)=\sigma$ 剛好消掉分母的 $\sigma$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 分配函數法 | 下一集起：其他求 $g(X)$ 分配的方法（變數變換、mgf 法） |
| $Z=(X-\mu)/\sigma\sim N(0,1)$ | 查常態表、信賴區間、檢定 |
| 卡方 mean $r$、var $2r$ | 抽樣分配 |

---

## 附：本集一句話總結

> **Gamma 的 mgf 是 $(1-\beta t)^{-\alpha}$（mean $\alpha\beta$、var $\alpha\beta^2$），卡方是它的特例（mean $r$、var $2r$）；求 $Y=g(X)$ 的 pdf，可以先求 $Y$ 的分配函數再微分，例如證明常態標準化後是 $N(0,1)$。**

---

*筆記依據「統計學」Lec05 錄影逐字稿（whisper large-v3-turbo，30:29）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
