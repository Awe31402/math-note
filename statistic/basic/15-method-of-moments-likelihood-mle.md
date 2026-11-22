---
course: 統計學（數理統計，數學系）
episode: 15
lecture: Lec15
date: 待補
video: https://youtu.be/y-hqbYapRnM
notes: Hogg 8th ed. 動差法（索引 p. 165）；§4.1 概似函數與 MLE（p. 225–228）；§6.1 最大概似估計（p. 355）
---

# 第 15 集 · Lec15：動差法；概似函數與最大概似估計量 [▶ 影片](https://youtu.be/y-hqbYapRnM)

← 上一集：[14](14-sample-variance-unbiased-consistent-method-of-moments.md) ｜ [總目錄](../README.md) ｜ 下一集：[16](16-mle-two-cases-order-statistics.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 15 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:13:01，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.1、§6.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「method of moments」→「Metal of Moment／Messive Moment／Meso-Moment」，「likelihood」→「Lightly Who／Lugly-foo／Ligree」，「univariate／bivariate」→「Univalent／bivallet」，「概似函數」→「蓋式函數」，「遞增」→「地增」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 動差法](#1-動差法)
  - [1.1 為什麼用樣本動差估母體動差](#11-為什麼用樣本動差估母體動差)
  - [1.2 做法：幾個參數就用幾個動差](#12-做法幾個參數就用幾個動差)
- [2. 例 1：Bernoulli](#2-例-1bernoulli)
- [3. 例 2：Poisson](#3-例-2poisson)
- [4. 例 3：常態（兩個參數）](#4-例-3常態兩個參數)
- [5. 最大概似估計量](#5-最大概似估計量)
  - [5.1 joint pdf 的兩種看法](#51-joint-pdf-的兩種看法)
  - [5.2 概似函數](#52-概似函數)
  - [5.3 為什麼選概似最大的 θ](#53-為什麼選概似最大的-θ)
  - [5.4 定義 MLE](#54-定義-mle)
- [6. 取 log 不改變最大值的位置](#6-取-log-不改變最大值的位置)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/y-hqbYapRnM?t=0) 設定：隨機樣本 $X_1,\dots,X_n$ 來自 $f(x;\theta)$，$f$ 知道、$\theta$ 不知道。用樣本估 $\theta$。介紹兩種找估計量的方法：

| 方法 | 想法 |
|---|---|
| 動差法（method of moments） | 令樣本動差＝母體動差，解 $\theta$ |
| 最大概似估計（maximum likelihood） | 選讓「已發生的資料機率最大」的 $\theta$ |

---

## 1. 動差法

### 1.1 為什麼用樣本動差估母體動差

[▶ 01:33](https://youtu.be/y-hqbYapRnM?t=93) 【口頭】要先想：為什麼用動差？

- **母體 $k$ 次動差** $E_\theta(X^k)=\int x^kf(x;\theta)\,dx$：積完 $x$ 不見了，剩下 $\theta$ 的函數。
- **樣本 $k$ 次動差** $\frac1n\sum X_i^k$。

[▶ 03:34](https://youtu.be/y-hqbYapRnM?t=214) 樣本動差有兩個好性質：

1. **不偏**：$E\left(\frac1n\sum X_i^k\right)=E(X^k)$。所以 $n$ 有限時，它的分配以母體動差為中心，觀察值大部分在母體動差附近。
2. **一致**：$\frac1n\sum X_i^k\xrightarrow{P}E(X^k)$。$n$ 夠大（30、50）就很接近。

所以用樣本動差估母體動差是有道理的。

### 1.2 做法：幾個參數就用幾個動差

[▶ 05:39](https://youtu.be/y-hqbYapRnM?t=339)

> **動差法**：$\theta=(\theta_1,\dots,\theta_k)$ 有 $k$ 個參數，解聯立方程式
> $$\frac1n\sum_{i=1}^nX_i^j=E_\theta(X^j),\qquad j=1,\dots,k.$$
> 解出的 $\hat\theta_1,\dots,\hat\theta_k$ 叫**動差法估計量**。

| 參數維度 | 方程式 |
|---|---|
| 1（univariate） | $\bar X=E_\theta(X)$ |
| 2（bivariate） | $\bar X=E_\theta(X)$，$\frac1n\sum X_i^2=E_\theta(X^2)$ |
| $k$ | 第 1 到第 $k$ 次動差都令相等 |

[▶ 08:12](https://youtu.be/y-hqbYapRnM?t=492) 兩邊本來不會相等，「令相等」是把它當方程式來解。一維時解出來一定是 $\bar X$ 的函數。

【口頭】大部分問題都很簡單，重要的是**觀念**，觀念不容易懂。

---

## 2. 例 1：Bernoulli

[▶ 11:20](https://youtu.be/y-hqbYapRnM?t=680) $X_1,\dots,X_n$ iid Bernoulli$(p)$。

【口頭】每個分配都要知道這些（不知道就不會做）：

| | Bernoulli$(p)$ |
|---|---|
| pdf | $p^x(1-p)^{1-x}$，$x=0,1$ |
| mean | $p$ |
| variance | $p(1-p)$ |
| mgf | $1-p+pe^t$，$t\in\mathbb{R}$ |

不記得 mean 的話，要自己用 pdf 積分（加總），或 mgf 微分一次令 $t=0$。

**動差法**（[▶ 12:52](https://youtu.be/y-hqbYapRnM?t=772)）：一個參數，$\bar X=E_p(X)=p$ ⇒
$$\hat p=\bar X.$$

**性質**（[▶ 14:53](https://youtu.be/y-hqbYapRnM?t=893)）：

- 不偏：$E(\hat p)=\frac1n\sum E(X_i)=p$。
- 一致：WLLN，$\bar X\xrightarrow{P}E(X)=p$。

（注意符號：$\xrightarrow{P}$ 上面的 $P$ 是「依機率」，和參數 $p$ 不是同一個意思。）

---

## 3. 例 2：Poisson

[▶ 17:31](https://youtu.be/y-hqbYapRnM?t=1051) $X_1,\dots,X_n$ iid Poisson$(\lambda)$。

| | Poisson$(\lambda)$ |
|---|---|
| pdf | $\frac{\lambda^xe^{-\lambda}}{x!}$，$x=0,1,2,\dots$ |
| mean | $\lambda$ |
| variance | $\lambda$ |
| mgf | $e^{\lambda(e^t-1)}$ |

**動差法**（[▶ 19:36](https://youtu.be/y-hqbYapRnM?t=1176)）：$\bar X=E(X)=\lambda$ ⇒ $\hat\lambda=\bar X$。

- 不偏：$E(\bar X)=\lambda$。
- 一致：WLLN，$\bar X\xrightarrow{P}\lambda$。

---

## 4. 例 3：常態（兩個參數）

[▶ 22:17](https://youtu.be/y-hqbYapRnM?t=1337) $X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$。參數 $(\mu,\sigma^2)$，二維。$\mu$ 就是 mean，$\sigma^2$ 就是 variance。

**聯立方程式**（[▶ 23:48](https://youtu.be/y-hqbYapRnM?t=1428)）：

$$\begin{cases}\bar X=E(X)=\mu\\[1mm] \dfrac1n\sum X_i^2=E(X^2)=\mu^2+\sigma^2\end{cases}$$

（$E(X^2)=\mu^2+\sigma^2$：平均的平方加變異數。）

**解**（[▶ 25:26](https://youtu.be/y-hqbYapRnM?t=1526)）：

- 第一式：$\hat\mu=\bar X$。
- 第二式把 $\mu$ 換成 $\bar X$：$\hat\sigma^2=\frac1n\sum X_i^2-\bar X^2$。

**化簡**（[▶ 25:56](https://youtu.be/y-hqbYapRnM?t=1556)）：$\frac1n\sum(X_i-\bar X)^2=\frac1n\left[\sum X_i^2-2\bar X\cdot n\bar X+n\bar X^2\right]=\frac1n\sum X_i^2-\bar X^2$，所以

$$\hat\sigma^2=\frac1n\sum_{i=1}^n(X_i-\bar X)^2.$$

注意是**除以 $n$**，不是 $n-1$。

**性質**

- $\hat\mu=\bar X$：不偏、一致（[▶ 28:09](https://youtu.be/y-hqbYapRnM?t=1689)）。
- $\hat\sigma^2$ **不偏？**（[▶ 29:10](https://youtu.be/y-hqbYapRnM?t=1750)）
$$E(\hat\sigma^2)=\frac{n-1}{n}E\left[\frac{1}{n-1}\sum(X_i-\bar X)^2\right]=\frac{n-1}{n}E(S^2)=\frac{n-1}{n}\sigma^2\ne\sigma^2.$$
  **不是**不偏。
- $\hat\sigma^2$ **一致？**（[▶ 30:43](https://youtu.be/y-hqbYapRnM?t=1843)）$\hat\sigma^2=\frac1n\sum X_i^2-\bar X^2$。$X_i^2$ iid，WLLN ⇒ $\frac1n\sum X_i^2\xrightarrow{P}E(X^2)=\mu^2+\sigma^2$；$\bar X^2\xrightarrow{P}\mu^2$。所以 $\hat\sigma^2\xrightarrow{P}\sigma^2$，**是**一致的。

---

## 5. 最大概似估計量

[▶ 33:22](https://youtu.be/y-hqbYapRnM?t=2002) 第二種方法：**maximum likelihood estimator（MLE，最大概似估計量）**，讓 likelihood 達到最大的估計量。

【口頭】[▶ 35:28](https://youtu.be/y-hqbYapRnM?t=2128) 統計一步一步建立新觀念；同一個東西在機率和統計可能有不同名字、不同意義，每個都要慢慢想。統計好好讀就不難；只背一背去考試，即使及格也完全不懂。統計基本上是「懂或不懂」（0 或 1），不像一般數學可以懂 60%。

### 5.1 joint pdf 的兩種看法

[▶ 37:03](https://youtu.be/y-hqbYapRnM?t=2223) 隨機樣本：獨立 ⇒ joint pdf＝個別 pdf 相乘；同分配 ⇒ 每個都是 $f(\cdot;\theta)$：

$$f(x_1,\dots,x_n;\theta)=\prod_{i=1}^nf(x_i;\theta).$$

[▶ 39:36](https://youtu.be/y-hqbYapRnM?t=2376) **看法 1：當作 joint pdf**——它是 $x_1,\dots,x_n$ 的函數（$\theta$ 是某個不知道的常數）。所以對 $x_1,\dots,x_n$ 積分（或加總）一定是 1，不管 $\theta$ 是多少。

$\theta$ 在**參數空間** $\Omega$ 裡（老師寫成大寫 $\Theta$）。

### 5.2 概似函數

[▶ 42:14](https://youtu.be/y-hqbYapRnM?t=2534)

> **看法 2：概似函數**（likelihood function）：把 $x_1,\dots,x_n$ 當作**固定**的，同一個式子看成 $\theta$ 的函數：
> $$L(\theta;x_1,\dots,x_n)=\prod_{i=1}^nf(x_i;\theta),\qquad\theta\in\Omega.$$

- 為什麼 $x_i$ 是固定的？因為隨機樣本會被**觀察**出來，觀察出來就只是數值。
- [▶ 45:23](https://youtu.be/y-hqbYapRnM?t=2723) 給一個 $\theta$ 就有一個函數值，叫在那個 $\theta$ 的 **likelihood（概似）**。$L(\theta_1;\mathbf x)$ 是 $\theta=\theta_1$ 時的 likelihood。
- 【口頭】同一個東西、不同態度。看到一隻貓，是自己家的就想抱起來，是隔壁的腳就想踢過去：角色不同。

### 5.3 為什麼選概似最大的 θ

[▶ 47:30](https://youtu.be/y-hqbYapRnM?t=2850) $x_1,\dots,x_n$ 已經發生了，但不知道哪個 $\theta$ 是對的，要選哪個？標準是什麼？

【口頭】例子：

- [▶ 48:02](https://youtu.be/y-hqbYapRnM?t=2882) 有人開賓士、穿西裝打領帶。你猜他有錢還是沒錢？有些窮人也會抵押房子借錢買車耍帥，但很少。開賓士的人比較多是有錢人，所以猜有錢。
- [▶ 49:37](https://youtu.be/y-hqbYapRnM?t=2977) 有人剛從田裡出來、戴斗笠、滿身泥巴走進銀行。有些農戶有幾千萬的田地，銀行經理會跑出來迎接，但那是少數。所以猜比較沒錢。
- [▶ 56:21](https://youtu.be/y-hqbYapRnM?t=3381) 一個新竹市的同學考上交大數學系，是光武中學還是新竹中學畢業？光武也有人考上交大，但新竹中學考上的機會大多了，所以猜新竹中學。

統計就是：答案（$\theta$）在背後，沒人知道。你選**犯錯機率比較小**的那個猜法——不表示不會錯，但錯的機率小。

[▶ 52:15](https://youtu.be/y-hqbYapRnM?t=3135) **把 likelihood 想成機率**：$L(\theta;x_1,\dots,x_n)$ 其實還是 joint pdf，可以想成「當 $\theta$ 是對的時候，發生 $X_1=x_1,\dots,X_n=x_n$ 的機率」。

$x_1,\dots,x_n$ 已經發生了。若
$$L(\theta_1;\mathbf x)>L(\theta_2;\mathbf x),$$
就覺得 $\theta_1$ 比 $\theta_2$ **可靠**（reliable）。如果 $\theta_2$ 是對的，發生這組資料的機率那麼小，可是它發生了，你怎麼會相信 $\theta_2$？

[▶ 57:53](https://youtu.be/y-hqbYapRnM?t=3473) 【口頭】統計一直在做選擇，就像人生。選讓你比較不會犯錯的方式。

### 5.4 定義 MLE

[▶ 58:23](https://youtu.be/y-hqbYapRnM?t=3503)

> **定義（MLE）**：給定 $x_1,\dots,x_n$，令 $\hat\theta(x_1,\dots,x_n)\in\Omega$ 使概似函數最大：
> $$L\left(\hat\theta;x_1,\dots,x_n\right)=\max_{\theta\in\Omega}L(\theta;x_1,\dots,x_n).$$
> 把小寫換成大寫，$\hat\theta(X_1,\dots,X_n)$ 叫 $\theta$ 的**最大概似估計量**（MLE）。

- [▶ 59:23](https://youtu.be/y-hqbYapRnM?t=3563) 不同的 $x_1,\dots,x_n$，最大值的位置不同，所以 $\hat\theta$ 一定是 $x_1,\dots,x_n$ 的函數。
- [▶ 60:25](https://youtu.be/y-hqbYapRnM?t=3625) 先在小寫（固定）下找最大，找到函數後換成大寫，才是隨機樣本的函數，才叫估計量。
- 代入觀察值的 $\hat\theta(x_1,\dots,x_n)$ 叫**最大概似估計值**（maximum likelihood estimate）。
- [▶ 63:59](https://youtu.be/y-hqbYapRnM?t=3839) 老師說概似函數通常有界，所以最大值存在。

【課本補充】最大值不一定存在、也不一定唯一；課本 §6.1 在正則條件（regularity conditions）下討論 MLE 的存在與性質。

---

## 6. 取 log 不改變最大值的位置

[▶ 64:32](https://youtu.be/y-hqbYapRnM?t=3872) 怎麼找 MLE？$L$ 是 $\theta$ 的函數，求最大值可以用微分（但不是每種情況都行，下次講兩種情形）。

[▶ 65:06](https://youtu.be/y-hqbYapRnM?t=3906) $\log$（自然對數）：$\frac{d}{dx}\log x=\frac1x>0$（$x>0$），所以 $\log$ 是**遞增**函數。因此

$$L(\theta_1;\mathbf x)\ge L(\theta_2;\mathbf x)\iff\log L(\theta_1;\mathbf x)\ge\log L(\theta_2;\mathbf x).$$

（⇒：遞增函數保持大小；⇐：$\log a\ge\log b$ 只可能 $a\ge b$。）

[▶ 68:23](https://youtu.be/y-hqbYapRnM?t=4103) 所以：

> $\hat\theta$ 讓 $L$ 最大 ⇔ $\hat\theta$ 讓 $\log L$ 最大。

[▶ 71:00](https://youtu.be/y-hqbYapRnM?t=4260) **好處**：我們要的是「哪一點」最大，不是最大值是多少。統計裡的 pdf 大多有**指數函數**，乘積取 log 變成相加、指數變成相乘，再微分比較好解，答案一樣。

以後找 MLE：把 joint pdf 取 log，再微分令它等於 0。

---

## 7. 一頁速查表

**動差法**：$k$ 個參數 → 令 $\frac1n\sum X_i^j=E_\theta(X^j)$，$j=1,\dots,k$，解聯立。
理由：樣本動差是母體動差的不偏且一致估計量。

| 分配 | 動差法估計量 | 不偏 | 一致 |
|---|---|---|---|
| Bernoulli$(p)$ | $\hat p=\bar X$ | ✓ | ✓ |
| Poisson$(\lambda)$ | $\hat\lambda=\bar X$ | ✓ | ✓ |
| $N(\mu,\sigma^2)$ | $\hat\mu=\bar X$ | ✓ | ✓ |
| | $\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2$ | ✗（$\frac{n-1}{n}\sigma^2$） | ✓ |

**概似函數**：$L(\theta;\mathbf x)=\prod f(x_i;\theta)$，$\mathbf x$ 固定、看成 $\theta$ 的函數。
（同一式子當 joint pdf 時是 $\mathbf x$ 的函數，積分＝1。）

**MLE**：$\hat\theta=\arg\max_{\theta\in\Omega}L(\theta;\mathbf x)$，再把 $x_i$ 換成 $X_i$。
直覺：已發生的資料，選讓它發生機率最大的 $\theta$（犯錯機率最小）。

**技巧**：$\log$ 遞增 ⇒ $\arg\max L=\arg\max\log L$。解 $\frac{\partial}{\partial\theta}\log L=0$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\log L$ 微分＝0 | 下一集：各分配的 MLE；不能微分的情形 |
| MLE | 課本第 6 章：MLE 的性質、檢定 |
| 動差法 vs MLE | 比較兩種估計量 |

---

## 附：本集一句話總結

> **動差法：幾個參數就令幾個樣本動差等於母體動差，解出參數（常態的 $\hat\sigma^2$ 會除以 $n$，有偏但一致）；最大概似法：把 joint pdf 看成 $\theta$ 的概似函數，選讓已發生資料機率最大的 $\theta$，取 log 不改變最大值位置。**

---

*筆記依據「統計學」Lec15 錄影逐字稿（whisper large-v3-turbo，1:13:01）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
