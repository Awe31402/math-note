---
course: 統計學（數理統計，數學系）
episode: 3
lecture: Lec03
date: 待補
video: https://youtu.be/Wibh6QhdPGI
notes: Hogg 8th ed. §3.3 Γ 分配（p. 173–174）、§3.3.1 卡方分配（p. 178）；§1.8 期望值（Definition 1.8.1、Theorem 1.8.1–1.8.2，p. 60–63）；§1.9 平均數與變異數（Definition 1.9.1–1.9.2，p. 68）
---

# 第 3 集 · Lec03：卡方分配、期望值、平均數與變異數 [▶ 影片](https://youtu.be/Wibh6QhdPGI)

← 上一集：[02](02-bernoulli-binomial-normal-poisson-gamma.md) ｜ [總目錄](../README.md) ｜ 下一集：[04](04-mgf-bernoulli-binomial-poisson-normal.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 3 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（35:38，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.8–1.9、§3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「機率」→「激勵／基地／肌力」，「樣本空間」→「樣門空間／藥門空間」，「實數」→「時速／十數」，「卡方」→「卡幅／卡彎／卡荒」，「期望值 expectation」→「exploitation／exaptation」，「變異數 variance」→「Valence／violence」，「mean」→「mine／密碼」，「服從」→「浮蟲／符從」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：離散型與連續型](#1-複習離散型與連續型)
- [2. Gamma 分配再看一次](#2-gamma-分配再看一次)
- [3. 卡方分配](#3-卡方分配)
- [4. 這學期會用到的分配就這幾個](#4-這學期會用到的分配就這幾個)
- [5. 期望值](#5-期望值)
  - [5.1 從班上平均成績說起](#51-從班上平均成績說起)
  - [5.2 隨機變數的函數還是隨機變數](#52-隨機變數的函數還是隨機變數)
  - [5.3 期望值的定義](#53-期望值的定義)
  - [5.4 兩個常用性質](#54-兩個常用性質)
- [6. 平均數 mean](#6-平均數-mean)
- [7. 變異數 variance](#7-變異數-variance)
- [8. 預告：動差生成函數](#8-預告動差生成函數)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本對應 |
|---|---|
| 複習：離散型、連續型隨機變數 | §1.6–1.7 |
| Gamma 分配、卡方分配 | §3.3，p. 173；§3.3.1，p. 178 |
| 期望值 $E[g(X)]$ | §1.8，p. 60 |
| 平均數 $\mu$、變異數 $\sigma^2$ | §1.9，p. 68 |

---

## 1. 複習：離散型與連續型

[▶ 00:31](https://youtu.be/Wibh6QhdPGI?t=31) 機率的架構：

1. 隨機實驗 → 樣本空間 $S$；$S$ 的子集是事件。
2. 機率集合函數 $P$，定義在 $S$ 的子集上。
3. 隨機變數 $X: S\to\mathbb{R}$。

[▶ 01:31](https://youtu.be/Wibh6QhdPGI?t=91) 本課只考慮兩種隨機變數：

| 種類 | 條件 | pdf |
|---|---|---|
| 離散型 | 值域 $X(S)$ 可數（countable） | $f(x)=P(X=x)$ |
| 連續型 | 存在 $f\ge 0$ 使 $F(x)=P(X\le x)=\int_{-\infty}^{x}f(t)\,dt$ | 那個 $f$ |

[▶ 02:36](https://youtu.be/Wibh6QhdPGI?t=156) 【口頭】$P(X\le x)$ 一定算得出來：把 $(-\infty,x]$ 映回樣本空間，那裡有 $P$。連續型就是「這個機率剛好等於某個非負函數的積分」。

[▶ 04:09](https://youtu.be/Wibh6QhdPGI?t=249) 目前只討論這兩種，所以**每個隨機變數都有 pdf**。連續型的 pdf 通常直接給。

---

## 2. Gamma 分配再看一次

[▶ 04:43](https://youtu.be/Wibh6QhdPGI?t=283)

$$X\sim\Gamma(\alpha,\beta):\quad f(x)=\frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta},\quad x>0.$$

- 值域是 $(0,\infty)$；$x\le 0$ 不會發生。
- $\alpha>0$、$\beta>0$，通常不知道。$\alpha,\beta$ 不同，分配就不同，所以記號要寫出 $\alpha,\beta$。

[▶ 06:46](https://youtu.be/Wibh6QhdPGI?t=406) 因為是 pdf，對值域積分一定是 1：

$$\int_0^\infty\frac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}\,dx=1.$$

（理由同上一集：等於 $P(S)=1$。）看到長這樣的積分，答案就是 1。

---

## 3. 卡方分配

[▶ 07:17](https://youtu.be/Wibh6QhdPGI?t=437) Gamma 分配有很多種 $\alpha,\beta$。其中一種特別重要，另外取名字：

> **卡方分配**（chi-square distribution）：Gamma 分配取 $\beta=2$、$\alpha=r/2$（即 $r=2\alpha$）。
> $$X\sim\chi^2(r):\quad f(x)=\frac{1}{\Gamma(r/2)\,2^{r/2}}x^{r/2-1}e^{-x/2},\quad x>0.$$

- $\chi$ 是希臘字母，讀 chi，不是 x。
- [▶ 09:19](https://youtu.be/Wibh6QhdPGI?t=559) 剩下的未知數 $r$ 叫**自由度**（degrees of freedom）。很多分配都有一個叫「自由度」的參數，只是名字。
- 【口頭】只要記得 Gamma 的 pdf，代 $\alpha=r/2$、$\beta=2$ 就會寫卡方的 pdf。
- 即 $\chi^2(r)=\Gamma(r/2,\,2)$。

⚠️ 逐字稿缺字：[▶ 07:49](https://youtu.be/Wibh6QhdPGI?t=469) 字幕是「β剛好等於all」「R等兩倍的A化」，應為「$\beta=2$」「$r=2\alpha$」（「all／O」是「二」，「A化」是「$\alpha$」），依課本 §3.3.1（p. 178）修正。

---

## 4. 這學期會用到的分配就這幾個

[▶ 10:51](https://youtu.be/Wibh6QhdPGI?t=651) 【口頭】

- 這學期，還有下學期的「高統」（高等統計學），講到的統計分配**幾乎都離不開**前面這幾個：Bernoulli、binomial、Poisson、normal、Gamma、卡方。
- Gamma 還有一個更簡單的特例叫**指數分配**（exponential distribution）。
- 很多統計理論的例子都用這幾個分配，所以要記住，「才幾個分配嘛」。

【課本補充】指數分配是 Gamma 取 $\alpha=1$：$f(x)=\frac{1}{\beta}e^{-x/\beta}$，$x>0$（§3.3，p. 175 附近）。本集只提名字。

---

## 5. 期望值

### 5.1 從班上平均成績說起

[▶ 11:54](https://youtu.be/Wibh6QhdPGI?t=714) 開始講比較「統計」的觀念：**期望值**（expectation）。期望值就是**平均**。

例：班上 50 人，成績 $x_1,\dots,x_{50}$。平均成績

$$\frac{1}{50}\sum_{i=1}^{50}x_i=\sum_{i=1}^{50}x_i\cdot\frac{1}{50}.$$

[▶ 12:54](https://youtu.be/Wibh6QhdPGI?t=774) 把「隨便抽一個同學看成績」當成隨機變數 $X$。每個同學被抽到的機率是 $1/50$，這個 $1/50$ 就是 pdf $f(x_i)$。所以

> 平均＝每個值 × 它的機率，全部加起來。

[▶ 13:56](https://youtu.be/Wibh6QhdPGI?t=836) 算班上平均時每個人一樣重要（權重都是 $1/50$）。但一般隨機變數**每一點的重要性不同**：pdf 高的地方容易出現，比較重要。所以要做**加權平均**，權重就是 pdf。

### 5.2 隨機變數的函數還是隨機變數

[▶ 15:30](https://youtu.be/Wibh6QhdPGI?t=930)

> **事實**：$X$ 是隨機變數，$g:\mathbb{R}\to\mathbb{R}$ 是實數函數，則合成函數（composite function）$g(X)$ 也是隨機變數。

**理由**：$g(X)$ 對每個樣本點 $s$ 的值是 $g(X(s))$。$X(s)$ 是實數，$g$ 把實數送到實數，所以 $g(X(s))\in\mathbb{R}$。所以 $g(X)$ 是 $S\to\mathbb{R}$ 的函數，就是隨機變數。

$$S\ \xrightarrow{\ X\ }\ \mathbb{R}\ \xrightarrow{\ g\ }\ \mathbb{R}$$

例：$e^X+2$、$\sin X$ 都是隨機變數。

### 5.3 期望值的定義

[▶ 18:37](https://youtu.be/Wibh6QhdPGI?t=1117)

> **定義（期望值）**：
> $$E[g(X)]=\begin{cases}\displaystyle\sum_x g(x)f(x), & X\text{ 離散}\\[2mm] \displaystyle\int_{-\infty}^{\infty}g(x)f(x)\,dx, & X\text{ 連續}\end{cases}$$

- 大寫 $X$ 改成小寫 $x$：代表「發生 $x$ 這一點」。
- $f(x)$ 是 $x$ 這一點的權重（weight）。重要的乘大權重，不重要的乘小權重。

【課本補充】課本 Definition 1.8.1（p. 60）定義的是 $E(X)$，並要求絕對收斂：$\int|x|f(x)\,dx<\infty$（離散型 $\sum|x|f(x)<\infty$）才說期望值存在。$E[g(X)]$ 用上面公式算是課本 Theorem 1.8.1（p. 63）。

### 5.4 兩個常用性質

[▶ 20:10](https://youtu.be/Wibh6QhdPGI?t=1210)

**性質 1：$E(c)=c$**（$c$ 是常數）

常數 $c$ 看成常數函數 $g(x)=c$（不管 $x$ 是多少都是 $c$）。以連續型為例：

$$E(c)=\int_{-\infty}^{\infty}c\,f(x)\,dx=c\int_{-\infty}^{\infty}f(x)\,dx=c\cdot 1=c.$$

關鍵：pdf 積分等於 1。

**性質 2：$E(aX+b)=aE(X)+b$**（[▶ 22:13](https://youtu.be/Wibh6QhdPGI?t=1333)）

$$E(aX+b)=\int_{-\infty}^{\infty}(ax+b)f(x)\,dx=a\int_{-\infty}^{\infty}xf(x)\,dx+b\int_{-\infty}^{\infty}f(x)\,dx=aE(X)+b.$$

- 拆開的條件：兩個積分都收斂，「和的積分＝積分的和」才成立。
- ⚠️ 逐字稿缺字：[▶ 23:15](https://youtu.be/Wibh6QhdPGI?t=1395) 這段 whisper 輸出一串重複的「x」和亂碼，是轉錄錯誤。推導依前後文與課本 Theorem 1.8.2（p. 63）補齊。

---

## 6. 平均數 mean

[▶ 23:48](https://youtu.be/Wibh6QhdPGI?t=1428) 期望值裡有兩個特別重要、天天用的。第一個：

> **定義（平均數，mean）**：$\mu=E(X)$。
> $$\mu=\begin{cases}\displaystyle\sum_x x f(x), & \text{離散}\\[2mm] \displaystyle\int_{-\infty}^{\infty}x f(x)\,dx, & \text{連續}\end{cases}$$

也就是 $g(x)=x$ 的期望值。

[▶ 26:23](https://youtu.be/Wibh6QhdPGI?t=1583) **意義**：分配的**中心點**。例：某同學成績剛好等於班平均，他的名次大概在中間。

---

## 7. 變異數 variance

[▶ 26:54](https://youtu.be/Wibh6QhdPGI?t=1614) 平均一樣，分散程度可以不一樣。

[▶ 27:24](https://youtu.be/Wibh6QhdPGI?t=1644) 畫兩個中心相同的 pdf：一個中間高、兩邊很快掉下來；一個比較矮、比較寬。因為兩個積分都是 1，中間高的那個，外面一定很快變小。

- 中間高的：**分散程度小**。也會跑到遠處，但機會很小。
- 矮寬的：遠處發生的機會相對大很多。

[▶ 28:55](https://youtu.be/Wibh6QhdPGI?t=1735) 【口頭】例：兩班微積分平均都是 60。一班成績都在 50 幾到 60 幾，很集中；另一班有 90 幾也有接近 0 分。平均一樣，分散程度差很多。

> **定義（變異數，variance）**（[▶ 29:25](https://youtu.be/Wibh6QhdPGI?t=1765)）：
> $$\sigma^2=\text{Var}(X)=E\left[(X-\mu)^2\right]=\int_{-\infty}^{\infty}(x-\mu)^2 f(x)\,dx\quad(\text{連續}).$$
> 離散型把積分換成 $\sum_x$。

- $\sigma$ 就是常態分配裡那個 $\sigma$。
- [▶ 30:27](https://youtu.be/Wibh6QhdPGI?t=1827) 注意：$E(X)$ 裡的 $X$ **不改成小寫**，因為取完期望值已經是常數 $\mu$。只有 $g(X)=(X-\mu)^2$ 裡的 $X$ 改成小寫。

[▶ 31:29](https://youtu.be/Wibh6QhdPGI?t=1889) **為什麼取平方？** $x-\mu$ 有正有負。我們只在乎「差多少」，不在乎誰大。平均 60 時，65 分和 55 分都差 5 分。取平方讓正負一樣看待。

[▶ 33:04](https://youtu.be/Wibh6QhdPGI?t=1984) 變異數大 → 分配矮寬；變異數小 → 很集中在中間。

**每個分配我們都想知道它的 mean 和 variance**，因為都很重要。

【課本補充】課本 §1.9（p. 68）還有一個好用的公式：$\sigma^2=E(X^2)-\mu^2$。推導：展開 $(X-\mu)^2=X^2-2\mu X+\mu^2$，用性質 2：$E(X^2)-2\mu E(X)+\mu^2=E(X^2)-\mu^2$。本集沒講。

---

## 8. 預告：動差生成函數

[▶ 33:36](https://youtu.be/Wibh6QhdPGI?t=2016) 【口頭】

- mean 和 variance 其實都能直接用定義積分（或加總）算出來，機率課應該學過，但比較麻煩。
- 我們要用一個比較快的工具：**動差生成函數**（moment generating function，mgf）。下一次講。

---

## 9. 一頁速查表

**卡方＝特殊的 Gamma**

$$\chi^2(r)=\Gamma\left(\tfrac{r}{2},\,2\right):\quad f(x)=\frac{1}{\Gamma(r/2)2^{r/2}}x^{r/2-1}e^{-x/2},\ x>0.$$

$r$：自由度。

**期望值**

$$E[g(X)]=\sum_x g(x)f(x)\quad\text{或}\quad\int g(x)f(x)\,dx.$$

- $g(X)$ 是隨機變數：$S\xrightarrow{X}\mathbb{R}\xrightarrow{g}\mathbb{R}$。
- $E(c)=c$（關鍵：$\int f=1$）。
- $E(aX+b)=aE(X)+b$（關鍵：拆積分，再用 $\int f=1$）。

**平均數、變異數**

| | 定義 | 意義 |
|---|---|---|
| $\mu$ | $E(X)$ | 中心點 |
| $\sigma^2$ | $E[(X-\mu)^2]$ | 分散程度（平方是為了不分正負） |

捷徑（課本）：$\sigma^2=E(X^2)-\mu^2$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| mean、variance | 下一集用動差生成函數算各分配的 mean、variance |
| 卡方分配 | 抽樣分配、檢定 |
| 期望值的線性 | 之後幾乎每一集 |

---

## 附：本集一句話總結

> **卡方是 $\beta=2$、$\alpha=r/2$ 的 Gamma；期望值是「以 pdf 為權重的加權平均」，其中 $\mu=E(X)$ 描述中心、$\sigma^2=E[(X-\mu)^2]$ 描述分散程度。**

---

*筆記依據「統計學」Lec03 錄影逐字稿（whisper large-v3-turbo，35:38）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
