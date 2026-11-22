---
course: 統計學（數理統計，數學系）
episode: 4
lecture: Lec04
date: 待補
video: https://youtu.be/lGsT2Zm0KGk
notes: Hogg 8th ed. §1.9 動差生成函數（Definition 1.9.3，p. 70；Theorem 1.9.1 $\sigma^2=E(X^2)-\mu^2$，p. 69；$M^{(m)}(0)=E(X^m)$，p. 72）；§3.1 Bernoulli、binomial 的 mgf；§3.2 Poisson 的 mgf；§3.4 常態的 mgf
---

# 第 4 集 · Lec04：動差生成函數；Bernoulli、二項、Poisson、常態的 mean 與 variance [▶ 影片](https://youtu.be/lGsT2Zm0KGk)

← 上一集：[03](03-chi-square-expectation-mean-variance.md) ｜ [總目錄](../README.md) ｜ 下一集：[05](05-gamma-mgf-cdf-technique.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 4 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:24:36，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.9、§3.1、§3.2、§3.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「動差」→「洞差／動插」，「期望值 expectation」→「exaptation／exploitation」，「variance」→「valence／balance」，「mean」→「命／mine」，「級數」→「急速／極速」，「收斂」→「縮斂／縮練」，「二項」→「偶像／奧向」，「微分」→「違分／微溫／微婚」，「$e$」常被聽成「1」或「E」（例如「1的t乘x四方」＝$e^{tx}$）。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：期望值要加（積）哪一塊](#1-複習期望值要加積哪一塊)
- [2. 動差生成函數](#2-動差生成函數)
  - [2.1 動差](#21-動差)
  - [2.2 定義](#22-定義)
  - [2.3 定理：微分 k 次、令 t＝0 得 k 次動差](#23-定理微分-k-次令-t0-得-k-次動差)
  - [2.4 用 mgf 算 mean 和 variance](#24-用-mgf-算-mean-和-variance)
- [3. Bernoulli 分配](#3-bernoulli-分配)
- [4. 二項分配](#4-二項分配)
- [5. Poisson 分配](#5-poisson-分配)
- [6. 常態分配](#6-常態分配)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

定義**動差生成函數**（moment generating function，mgf），證明它為什麼能「生成動差」，然後一個一個分配導出 mgf、mean、variance。

| 分配 | mgf $M(t)$ | mean | variance |
|---|---|---|---|
| Bernoulli$(p)$ | $1-p+pe^t$ | $p$ | $p(1-p)$ |
| $b(n,p)$ | $(1-p+pe^t)^n$ | $np$ | $np(1-p)$ |
| Poisson$(\lambda)$ | $e^{\lambda(e^t-1)}$ | $\lambda$ | $\lambda$ |
| $N(\mu,\sigma^2)$ | $e^{\mu t+\sigma^2t^2/2}$ | $\mu$ | $\sigma^2$ |

---

## 1. 複習：期望值要加（積）哪一塊

[▶ 00:30](https://youtu.be/lGsT2Zm0KGk?t=30)

- $X$ 是隨機變數、$g$ 是實數函數，則 $g(X)$ 還是隨機變數（$S\xrightarrow{X}\mathbb{R}\xrightarrow{g}\mathbb{R}$）。
- 期望值：大寫 $X$ 改小寫，乘以 pdf（權重），離散相加、連續積分。

[▶ 02:40](https://youtu.be/lGsT2Zm0KGk?t=160) **加哪些 $x$？** 加**值域**（range）$X(S)$ 裡的點。

- $X:S\to\mathbb{R}$ 的 $\mathbb{R}$ 是**對應域**（codomain），不一定是值域。值域是 $X(S)$，被映到的那一塊。
- 值域以外的點不會發生，pdf 是 0。所以寫 $\int_{-\infty}^\infty$ 也可以，實際上只要積值域。

$$E[g(X)]=\sum_{x\in X(S)}g(x)f(x)\quad\text{或}\quad\int_{X(S)}g(x)f(x)\,dx.$$

[▶ 06:34](https://youtu.be/lGsT2Zm0KGk?t=394) 【口頭】從數學角度看統計，數學其實很簡單。但如果沒有慢慢了解每個定義在幹什麼，最後會「每個都會、通通不會」，因為不知道統計在做什麼。每個定義都要真正去了解。

---

## 2. 動差生成函數

### 2.1 動差

[▶ 08:07](https://youtu.be/lGsT2Zm0KGk?t=487)

> **定義（$k$ 次動差，$k$-th moment）**：$E(X^k)$。

$X^k$ 是 $X$ 的實數函數，所以是隨機變數，可以取期望值。

### 2.2 定義

[▶ 10:11](https://youtu.be/lGsT2Zm0KGk?t=611)

> **定義（動差生成函數，mgf）**：
> $$M_X(t)=E\left(e^{tX}\right).$$

- 它是 $t$ 的函數：給一個實數 $t$，得到一個值。
- 對固定的 $t$，$e^{tx}$ 是 $x$ 的實數函數，所以可以取期望值。
- [▶ 12:15](https://youtu.be/lGsT2Zm0KGk?t=735) 不一定每個 $t$ 都存在（加總或積分可能發散）。我們關心存在的那些 $t$。本課會碰到的，至少在某一塊都存在。

【課本補充】Definition 1.9.3（p. 70）要求：存在 $h>0$，使 $E(e^{tX})$ 在 $-h<t<h$ 都存在，才說 mgf 存在。也就是要在 0 附近的一個開區間存在。

[▶ 13:16](https://youtu.be/lGsT2Zm0KGk?t=796) **數學上的性質**：如果 mgf 在 $0$ 附近某個區間 $(-\delta,\delta)$ 都存在，那麼「先取期望值（加總／積分）再對 $t$ 微分」＝「先微分再取期望值」：

$$\frac{d^k}{dt^k}E\left(e^{tX}\right)=E\left(\frac{d^k}{dt^k}e^{tX}\right).$$

老師沒證明，直接用（「數學上告訴我們這件事情」）。

### 2.3 定理：微分 k 次、令 t＝0 得 k 次動差

[▶ 15:54](https://youtu.be/lGsT2Zm0KGk?t=954)

> **定理**：若 mgf 在 0 附近存在，則
> $$M_X^{(k)}(0)=E(X^k).$$

這就是名字的由來：它能**生成動差**。

[▶ 16:56](https://youtu.be/lGsT2Zm0KGk?t=1016) **為什麼不直接算？** 直接算 $E(X^k)=\int x^kf(x)\,dx$ 常常很麻煩。mgf 導過一次就能背起來，之後只要微分，微分比較簡單。

**證明**（[▶ 18:29](https://youtu.be/lGsT2Zm0KGk?t=1109)，假設連續型）：

$$M(t)=\int_{-\infty}^{\infty}e^{tx}f(x)\,dx.$$

（值域外 $f=0$，所以寫成 $-\infty$ 到 $\infty$ 沒關係。）

**Step 1：微分一次。** 微分搬進積分。$f(x)$ 和 $t$ 無關，當常數；$\frac{d}{dt}e^{tx}=xe^{tx}$：
$$M'(t)=\int_{-\infty}^{\infty}\frac{\partial}{\partial t}e^{tx}f(x)\,dx=\int_{-\infty}^{\infty}xe^{tx}f(x)\,dx.$$

**Step 2：再微分一次。** $x$ 和 $t$ 無關，提出來；再多一個 $x$：
$$M''(t)=\int_{-\infty}^{\infty}x^2e^{tx}f(x)\,dx.$$

**Step 3：一般地**，每微分一次多一個 $x$。若 $M^{(k-1)}(t)=\int x^{k-1}e^{tx}f(x)\,dx$，再微分一次：
$$M^{(k)}(t)=\int_{-\infty}^{\infty}x^ke^{tx}f(x)\,dx.$$

**Step 4：令 $t=0$**，$e^{0}=1$：
$$M^{(k)}(0)=\int_{-\infty}^{\infty}x^kf(x)\,dx=E(X^k).\qquad\blacksquare$$

### 2.4 用 mgf 算 mean 和 variance

[▶ 26:58](https://youtu.be/lGsT2Zm0KGk?t=1618)

**mean**：$\mu=E(X)=M'(0)$。

**variance**（[▶ 28:00](https://youtu.be/lGsT2Zm0KGk?t=1680)）：先證明

> $$\sigma^2=E(X^2)-\mu^2=E(X^2)-[E(X)]^2.$$
> 「平方的期望值減掉期望值的平方。」

**證明**：

1. 展開：$(X-\mu)^2=X^2-2\mu X+\mu^2$。
2. [▶ 29:34](https://youtu.be/lGsT2Zm0KGk?t=1774) **關鍵觀念**：$\mu=E(X)$ 是積分（或加總）完的結果，是**常數**，不再是隨機變數。
3. 和的期望值＝期望值的和；常數可以提出來；常數的期望值是自己：
$$E[(X-\mu)^2]=E(X^2)-2\mu E(X)+\mu^2=E(X^2)-2\mu^2+\mu^2=E(X^2)-\mu^2.$$

所以

$$\sigma^2=M''(0)-[M'(0)]^2.$$

【課本補充】這個公式是課本 Theorem 1.9.1（p. 69）。

---

## 3. Bernoulli 分配

[▶ 34:13](https://youtu.be/lGsT2Zm0KGk?t=2053)

pdf：$f(x)=p^x(1-p)^{1-x}$，$x=0,1$；其他是 0。值域 $\{0,1\}$，離散 → 相加。

**mgf**：
$$M(t)=\sum_{x=0}^{1}e^{tx}p^x(1-p)^{1-x}=\underbrace{1\cdot 1\cdot(1-p)}_{x=0}+\underbrace{e^t\cdot p\cdot 1}_{x=1}=1-p+pe^t.$$

[▶ 37:18](https://youtu.be/lGsT2Zm0KGk?t=2238) 只有兩項相加，一定收斂，所以**對所有 $t\in\mathbb{R}$ 存在**，0 附近當然存在。

**mean**（[▶ 38:56](https://youtu.be/lGsT2Zm0KGk?t=2336)）：$M'(t)=pe^t$（$1-p$ 是常數，微分是 0），$\mu=M'(0)=p$。

**variance**：$M''(t)=pe^t$，$E(X^2)=M''(0)=p$。
$$\sigma^2=p-p^2=p(1-p).$$
$0\le p\le 1$，所以不會是負的。

---

## 4. 二項分配

[▶ 41:32](https://youtu.be/lGsT2Zm0KGk?t=2492)

$X\sim b(n,p)$：$n$ 次 Bernoulli 的成功次數。pdf：$f(x)=\binom{n}{x}p^x(1-p)^{n-x}$，$x=0,1,\dots,n$。

【口頭】看到 binomial 就要能寫出 pdf，寫不出來很多東西就沒辦法繼續學。

**mgf**（[▶ 43:38](https://youtu.be/lGsT2Zm0KGk?t=2618)）：

**Step 1**：照定義，離散相加：
$$M(t)=\sum_{x=0}^{n}e^{tx}\binom{n}{x}p^x(1-p)^{n-x}.$$

**Step 2**：技巧：$e^{tx}=(e^t)^x$，和 $p^x$ 合併：
$$M(t)=\sum_{x=0}^{n}\binom{n}{x}\left(pe^t\right)^x(1-p)^{n-x}.$$

**Step 3**：[▶ 45:42](https://youtu.be/lGsT2Zm0KGk?t=2742) 對照高中的**二項展開式**（binomial expansion），對所有實數 $a,b$：
$$(a+b)^n=\sum_{k=0}^{n}\binom{n}{k}b^ka^{n-k}.$$
取 $k=x$、$b=pe^t$、$a=1-p$：
$$M(t)=\left(1-p+pe^t\right)^n,\qquad t\in\mathbb{R}.$$

[▶ 48:17](https://youtu.be/lGsT2Zm0KGk?t=2897) 和 Bernoulli 比較：Bernoulli 是 $(1-p+pe^t)^1$（做 1 次），binomial 是 $n$ 次方（做 $n$ 次）。

**mean**（[▶ 49:20](https://youtu.be/lGsT2Zm0KGk?t=2960)）：連鎖律：
$$M'(t)=n\left(1-p+pe^t\right)^{n-1}\cdot pe^t.$$
$t=0$：括號裡 $1-p+p=1$，所以 $\mu=M'(0)=np$。

**variance**（[▶ 51:28](https://youtu.be/lGsT2Zm0KGk?t=3088)）：乘積法則，兩個 $t$ 的函數相乘：
$$M''(t)=n(n-1)\left(1-p+pe^t\right)^{n-2}p^2e^{2t}+n\left(1-p+pe^t\right)^{n-1}pe^t.$$
$t=0$：$E(X^2)=M''(0)=n(n-1)p^2+np$。
$$\sigma^2=n(n-1)p^2+np-(np)^2=-np^2+np=np(1-p).$$

[▶ 54:34](https://youtu.be/lGsT2Zm0KGk?t=3274) 【口頭】這些一定要**自己導一遍**。不是死背，導幾遍熟了自然記得。好幾個分配，死背會弄錯。

---

## 5. Poisson 分配

[▶ 55:47](https://youtu.be/lGsT2Zm0KGk?t=3347)

$X\sim\text{Poisson}(\lambda)$：$f(x)=\dfrac{\lambda^xe^{-\lambda}}{x!}$，$x=0,1,2,\dots$。

【口頭】想成「做無窮多次 Bernoulli 實驗，成功幾次」，所以值域是所有非負整數。可數 → 離散 → 相加。

**mgf**（[▶ 56:50](https://youtu.be/lGsT2Zm0KGk?t=3410)）：

**Step 1**：
$$M(t)=\sum_{x=0}^{\infty}e^{tx}\frac{\lambda^xe^{-\lambda}}{x!}.$$

**Step 2**：和 $x$ 無關的 $e^{-\lambda}$ 提出來；$e^{tx}\lambda^x=(\lambda e^t)^x$：
$$M(t)=e^{-\lambda}\sum_{x=0}^{\infty}\frac{(\lambda e^t)^x}{x!}.$$

**Step 3**：[▶ 58:26](https://youtu.be/lGsT2Zm0KGk?t=3506) 微積分的級數（series）：對所有 $a\in\mathbb{R}$，
$$\sum_{k=0}^{\infty}\frac{a^k}{k!}=e^a\quad(\text{收斂}).$$
取 $a=\lambda e^t$：
$$M(t)=e^{-\lambda}e^{\lambda e^t}=e^{\lambda(e^t-1)},\qquad t\in\mathbb{R}.$$

**mean**（[▶ 61:18](https://youtu.be/lGsT2Zm0KGk?t=3678)）：指數函數微分＝自己 × 指數部分的微分：
$$M'(t)=e^{\lambda(e^t-1)}\cdot\lambda e^t,\qquad \mu=M'(0)=e^0\cdot\lambda=\lambda.$$

**variance**（[▶ 62:50](https://youtu.be/lGsT2Zm0KGk?t=3770)）：乘積法則：
$$M''(t)=e^{\lambda(e^t-1)}\lambda^2e^{2t}+e^{\lambda(e^t-1)}\lambda e^t.$$
$E(X^2)=M''(0)=\lambda^2+\lambda$。
$$\sigma^2=\lambda^2+\lambda-\lambda^2=\lambda.$$

[▶ 64:57](https://youtu.be/lGsT2Zm0KGk?t=3897) 【口頭】Poisson 的 mean 和 variance **相等**，都是 $\lambda$。老師說這是他在統計和機率裡看過唯一 mean 等於 variance 的隨機變數。

---

## 6. 常態分配

[▶ 65:32](https://youtu.be/lGsT2Zm0KGk?t=3932) **先複習一個一直要用的結果**：任何 pdf 對 $-\infty$ 到 $\infty$ 積分都是 1。

- 值域外 pdf 是 0，所以 $\int_{-\infty}^\infty f=\int_{X(S)}f$。
- $\int_{-\infty}^\infty f=P(X\in\mathbb{R})$；把 $\mathbb{R}$ 映回去是整個 $S$；$P(S)=1$。

所以：只要被積函數長成
$$\frac{1}{\sqrt{2\pi}\,\sigma}\exp\left[-\frac{(x-m)^2}{2\sigma^2}\right]$$
（$m$ 任意實數、$\sigma>0$，**分母的 $\sigma$ 和指數裡的 $\sigma^2$ 要對應**），它就是常態 pdf，$\int_{-\infty}^{\infty}=1$。

**mgf**（[▶ 70:18](https://youtu.be/lGsT2Zm0KGk?t=4218)）：

**Step 1**：照定義，連續、值域是 $\mathbb{R}$：
$$M(t)=\int_{-\infty}^{\infty}e^{tx}\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]dx.$$

**Step 2**：[▶ 71:50](https://youtu.be/lGsT2Zm0KGk?t=4310) 把兩個指數合併，提出 $-\frac{1}{2\sigma^2}$：
$$tx-\frac{(x-\mu)^2}{2\sigma^2}=-\frac{1}{2\sigma^2}\left[x^2-2\mu x+\mu^2-2\sigma^2tx\right]=-\frac{1}{2\sigma^2}\left[x^2-2(\mu+\sigma^2t)x+\mu^2\right].$$

**Step 3**：[▶ 72:55](https://youtu.be/lGsT2Zm0KGk?t=4375) 配方。令 $m=\mu+\sigma^2t$：
$$x^2-2mx+\mu^2=(x-m)^2-m^2+\mu^2.$$
所以
$$tx-\frac{(x-\mu)^2}{2\sigma^2}=-\frac{(x-m)^2}{2\sigma^2}+\frac{m^2-\mu^2}{2\sigma^2}.$$

【口頭】為什麼要湊成這樣？因為常態 pdf 一定是「$-\dfrac{(x-\text{某數})^2}{2\sigma^2}$」的形式。

**Step 4**：[▶ 74:56](https://youtu.be/lGsT2Zm0KGk?t=4496) 和 $x$ 無關的提出積分：
$$M(t)=\exp\left[\frac{m^2-\mu^2}{2\sigma^2}\right]\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(x-m)^2}{2\sigma^2}\right]dx.$$
積分裡是 $N(m,\sigma^2)$ 的 pdf（$m=\mu+\sigma^2t$ 是新的 mean），積分＝1。

**Step 5**：[▶ 78:03](https://youtu.be/lGsT2Zm0KGk?t=4683) 展開 $m^2=\mu^2+2\mu\sigma^2t+\sigma^4t^2$：
$$\frac{m^2-\mu^2}{2\sigma^2}=\frac{2\mu\sigma^2t+\sigma^4t^2}{2\sigma^2}=\mu t+\frac{\sigma^2t^2}{2}.$$

$$\boxed{M(t)=\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right),\qquad t\in\mathbb{R}}$$

[▶ 79:05](https://youtu.be/lGsT2Zm0KGk?t=4745) 存在性：對任何實數 $t$，$m=\mu+\sigma^2t$ 是實數，Step 4 的積分都是 1，所以對所有 $t$ 存在。這個要記下來。

【口頭】[▶ 76:29](https://youtu.be/lGsT2Zm0KGk?t=4589) 應用：研究所考 $\int_{-\infty}^{\infty}e^{-x^2/2}dx$，你找不到反導函數。但 $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ 是 $N(0,1)$ 的 pdf，積分是 1，所以答案是 $\sqrt{2\pi}$。

**mean**（[▶ 80:13](https://youtu.be/lGsT2Zm0KGk?t=4813)）：
$$M'(t)=\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right)(\mu+\sigma^2t),\qquad E(X)=M'(0)=\mu.$$

所以常態分配裡的 $\mu$ **就是它的 mean**。（老師提醒：這裡先別寫「$\mu=$」，因為 $\mu$ 已經是常態的參數名，寫 $E(X)$。）

**variance**（[▶ 81:47](https://youtu.be/lGsT2Zm0KGk?t=4907)）：乘積法則：
$$M''(t)=\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right)(\mu+\sigma^2t)^2+\sigma^2\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right).$$
$E(X^2)=M''(0)=\mu^2+\sigma^2$。
$$\text{Var}(X)=\mu^2+\sigma^2-\mu^2=\sigma^2.$$

所以 $N(\mu,\sigma^2)$ 的 $\sigma^2$ **就是它的 variance**。

[▶ 83:49](https://youtu.be/lGsT2Zm0KGk?t=5029) 【口頭】整個導下來不難，要自己導一遍，這樣才記得 mgf、mean、variance。

---

## 7. 一頁速查表

**mgf 的定義與核心定理**

$$M(t)=E(e^{tX}),\qquad M^{(k)}(0)=E(X^k).$$

關鍵一步：0 附近存在 ⇒ 微分可以搬進積分；每微分一次 $e^{tx}$ 多吐出一個 $x$；$t=0$ 時 $e^0=1$。

**mean、variance**

$$\mu=M'(0),\qquad \sigma^2=M''(0)-[M'(0)]^2.$$

關鍵一步：$\sigma^2=E[(X-\mu)^2]=E(X^2)-2\mu E(X)+\mu^2=E(X^2)-\mu^2$（$\mu$ 是常數）。

**四個分配**

| 分配 | mgf | 導 mgf 的關鍵一步 | mean | var |
|---|---|---|---|---|
| Bernoulli$(p)$ | $1-p+pe^t$ | 兩項直接加 | $p$ | $p(1-p)$ |
| $b(n,p)$ | $(1-p+pe^t)^n$ | $e^{tx}p^x=(pe^t)^x$，二項展開式 | $np$ | $np(1-p)$ |
| Poisson$(\lambda)$ | $e^{\lambda(e^t-1)}$ | $\sum\frac{a^k}{k!}=e^a$，$a=\lambda e^t$ | $\lambda$ | $\lambda$ |
| $N(\mu,\sigma^2)$ | $e^{\mu t+\sigma^2t^2/2}$ | 配方成 $N(\mu+\sigma^2t,\sigma^2)$ 的 pdf，積分＝1 | $\mu$ | $\sigma^2$ |

四個的 mgf 都對所有 $t\in\mathbb{R}$ 存在。

**常用積分**：$\int_{-\infty}^{\infty}e^{-x^2/2}dx=\sqrt{2\pi}$（$N(0,1)$ pdf 積分＝1）。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| mgf | 下一集：Gamma、卡方的 mgf；之後用 mgf 判斷分配、證明極限定理 |
| $\sigma^2=E(X^2)-\mu^2$ | 幾乎每一次算 variance |
| 「pdf 積分＝1」的配方技巧 | Gamma 的 mgf 也用同一招 |

---

## 附：本集一句話總結

> **mgf $M(t)=E(e^{tX})$ 微分 $k$ 次、令 $t=0$ 就得 $E(X^k)$；用它一口氣導出 Bernoulli、二項、Poisson、常態的 mean 和 variance，其中常態的參數 $\mu,\sigma^2$ 正好就是 mean 和 variance。**

---

*筆記依據「統計學」Lec04 錄影逐字稿（whisper large-v3-turbo，1:24:36）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
