---
course: 統計學（數理統計，數學系）
episode: 20
lecture: Lec20
date: 待補
video: https://youtu.be/e_tMD_rSHKg
notes: Hogg 8th ed. §6.2 Rao–Cramér 下界的例子（Poisson、Bernoulli）；§1.4 條件機率（Definition 1.4.1，p. 24）；§2.3 條件分配（p. 109）；§7.2 充分統計量（預告，p. 419）
---

# 第 20 集 · Lec20：用 Cramér–Rao 下界證明 UMVUE（Poisson、Bernoulli）；條件機率與條件 pdf [▶ 影片](https://youtu.be/e_tMD_rSHKg)

← 上一集：[19](19-umvue-cramer-rao-lower-bound.md) ｜ [總目錄](../README.md) ｜ 下一集：[21](21-sufficient-statistic-definition-examples.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 20 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（40:22，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.4、§2.3、§6.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Cramér–Rao lower bound」→「Climinal Rolobank／Kolimoroban」，「Poisson」→「普華松／博阿松」，「Bernoulli」→「本能力／Bernoni」，「sufficient statistic」照錄（中文「充分統計量」），「joint」→「join／糾溫」，「互斥」→「互次」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 做法：用 Cramér–Rao 下界驗證 UMVUE](#1-做法用-cramérrao-下界驗證-umvue)
- [2. 例 1：Poisson](#2-例-1poisson)
- [3. 例 2：Bernoulli](#3-例-2bernoulli)
- [4. 讀統計的建議](#4-讀統計的建議)
- [5. Cramér–Rao 的限制；預告充分統計量](#5-cramérrao-的限制預告充分統計量)
- [6. 條件機率](#6-條件機率)
- [7. 條件 pdf](#7-條件-pdf)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Poisson、Bernoulli：MLE 達到 Cramér–Rao 下界 ⇒ UMVUE | §6.2 |
| 為什麼還需要另一套方法（充分統計量） | §7.2 |
| 條件機率、條件 pdf | §1.4，p. 24；§2.3，p. 109 |

[▶ 00:32](https://youtu.be/e_tMD_rSHKg?t=32) 【口頭】講過的分配（Poisson、Bernoulli、二項、均勻、常態、Gamma、卡方），題目只會說「來自什麼分配」，**不會給 pdf**。你要自己知道它的 pdf、mean、variance、mgf。不熟的分配題目才會給 pdf。

---

## 1. 做法：用 Cramér–Rao 下界驗證 UMVUE

[▶ 02:04](https://youtu.be/e_tMD_rSHKg?t=124)

1. 找一個估計量（例如 MLE）。
2. **確認不偏**。不偏才有資格比。
3. 算它的變異數。
4. 算 Cramér–Rao 下界（估 $\theta$ 本身時分子是 1）：
$$\text{CRLB}=\frac{1}{-nE\left[\frac{\partial^2}{\partial\theta^2}\log f(X;\theta)\right]}.$$
5. 變異數＝下界 ⇒ UMVUE。

[▶ 04:07](https://youtu.be/e_tMD_rSHKg?t=247) 【口頭】不是不偏的就不用理它，不可能是 UMVUE。就像隔壁班的同學成績再好，也不可能是我們班第一名。

---

## 2. 例 1：Poisson

[▶ 01:33](https://youtu.be/e_tMD_rSHKg?t=93) $X_1,\dots,X_n$ iid Poisson$(\lambda)$。證明 MLE $\hat\lambda=\bar X$ 是 UMVUE。

**不偏**（[▶ 03:36](https://youtu.be/e_tMD_rSHKg?t=216)）：$E(\bar X)=\frac1n\sum E(X_i)=\frac{n\lambda}{n}=\lambda$。✓

**變異數**（[▶ 04:37](https://youtu.be/e_tMD_rSHKg?t=277)）：獨立 ⇒ 和的變異數＝變異數的和；Poisson 的 variance＝mean＝$\lambda$：
$$\text{Var}(\bar X)=\frac{1}{n^2}\sum\text{Var}(X_i)=\frac{n\lambda}{n^2}=\frac\lambda n.$$

**Cramér–Rao 下界**（[▶ 05:41](https://youtu.be/e_tMD_rSHKg?t=341)）：

1. pdf（這裡 $x$ 小寫，當作 pdf）：$f(x;\lambda)=\dfrac{\lambda^xe^{-\lambda}}{x!}$。
2. 取 log：$\log f=-\log x!+x\log\lambda-\lambda$。
3. 微分一次（$\log x!$ 和 $\lambda$ 無關）：$\dfrac{\partial}{\partial\lambda}\log f=\dfrac x\lambda-1$。
4. 微分兩次：$\dfrac{\partial^2}{\partial\lambda^2}\log f=-\dfrac{x}{\lambda^2}$。
5. [▶ 09:53](https://youtu.be/e_tMD_rSHKg?t=593) 把 $x$ 改大寫取期望值：$E\left[-\dfrac{X}{\lambda^2}\right]=-\dfrac{\lambda}{\lambda^2}=-\dfrac1\lambda$。

【口頭】[▶ 09:22](https://youtu.be/e_tMD_rSHKg?t=562) 這就看出為什麼用「微分兩次」的公式：一次微分 $\frac x\lambda-1$ 要平方再取期望值，展開比較麻煩；微分兩次只剩 $-\frac{x}{\lambda^2}$，期望值很好算。

$$\text{CRLB}=\frac{1}{-n\cdot\left(-\frac1\lambda\right)}=\frac\lambda n.$$

**結論**（[▶ 11:54](https://youtu.be/e_tMD_rSHKg?t=714)）：$\bar X$ 不偏，且 $\text{Var}(\bar X)=\frac\lambda n=$ CRLB ⇒ $\bar X$ 是 $\lambda$ 的 **UMVUE**。

【口頭】[▶ 12:55](https://youtu.be/e_tMD_rSHKg?t=775) 不同題目解法都一樣，差別在 density function。不熟的分配，MLE 要自己找、期望值和變異數可能要自己積分導，會比較複雜。要把學過的東西整合起來應用；想學好就要自己做書上的習題。

---

## 3. 例 2：Bernoulli

[▶ 14:26](https://youtu.be/e_tMD_rSHKg?t=866) $X_1,\dots,X_n$ iid Bernoulli$(p)$，找 $p$ 的 UMVUE。

**Cramér–Rao 下界**（[▶ 14:57](https://youtu.be/e_tMD_rSHKg?t=897)）：

1. $f(x;p)=p^x(1-p)^{1-x}$。
2. $\log f=x\log p+(1-x)\log(1-p)$。
3. $\dfrac{\partial}{\partial p}\log f=\dfrac xp-\dfrac{1-x}{1-p}$。
   【口頭】[▶ 16:28](https://youtu.be/e_tMD_rSHKg?t=988) 用「平方的期望值」公式要把兩項相減平方，變四項，很麻煩。
4. $\dfrac{\partial^2}{\partial p^2}\log f=-\dfrac{x}{p^2}-\dfrac{1-x}{(1-p)^2}$。
5. 取期望值，$E(X)=p$：
$$E\left[-\frac{X}{p^2}-\frac{1-X}{(1-p)^2}\right]=-\frac{p}{p^2}-\frac{1-p}{(1-p)^2}=-\frac1p-\frac{1}{1-p}=-\frac{1}{p(1-p)}.$$

⚠️ 逐字稿缺字：[▶ 19:02](https://youtu.be/e_tMD_rSHKg?t=1142)–[▶ 20:33](https://youtu.be/e_tMD_rSHKg?t=1233) 老師板書時兩度寫錯符號、約分，口頭更正後得到 $-\frac{1}{p(1-p)}$（$\frac1p+\frac{1}{1-p}=\frac{1}{p(1-p)}$）。

$$\text{CRLB}=\frac{1}{-n\cdot\left(-\frac{1}{p(1-p)}\right)}=\frac{p(1-p)}{n}.$$

**用 MLE $\hat p=\bar X$**（[▶ 21:42](https://youtu.be/e_tMD_rSHKg?t=1302)）：

- 不偏：$E(\bar X)=\frac{np}{n}=p$。✓
- 變異數：$\text{Var}(\bar X)=\frac{1}{n^2}\cdot np(1-p)=\frac{p(1-p)}{n}$。（Bernoulli variance 是 $p(1-p)$，不記得就用 mgf 導。）
- 等於 CRLB ⇒ $\bar X$ 是 $p$ 的 **UMVUE**。

---

## 4. 讀統計的建議

[▶ 25:18](https://youtu.be/e_tMD_rSHKg?t=1518) 【口頭】

- 剛才的都是很簡單的題目（分配熟悉、pdf/mean/variance/mgf 都導過）。題目設計有很多型態；給你沒看過的分配，就要自己導 MLE、期望值、變異數。
- [▶ 26:20](https://youtu.be/e_tMD_rSHKg?t=1580) 很多研究所都考統計（資工、管理、統計所）。真要準備，找一本書——例如 Hogg and Craig，很好的一本——從頭到尾慢慢看，習題一題一題做、例題一題一題看。
- [▶ 26:50](https://youtu.be/e_tMD_rSHKg?t=1610) 很多人讀統計考試都會，最後完全不懂，因為觀念沒弄懂，只是把證明背下來。統計的數學簡單，最重要的是背後的觀念。
- [▶ 27:53](https://youtu.be/e_tMD_rSHKg?t=1673) 統計的來歷：早期和賭博有關；早期主要解決歐洲、美國的**農業**問題。現在用在基因分析、**生物統計**。在美國讀生物統計很好找工作，薪水比數學高很多，因為和生命有關，人家願意花錢。
- 有興趣就花功夫，不要讀半吊子；沒興趣及格就好。

---

## 5. Cramér–Rao 的限制；預告充分統計量

[▶ 28:53](https://youtu.be/e_tMD_rSHKg?t=1733) 接下來另一套找 UMVUE 的方法，核心是**充分統計量**（sufficient statistic）。

**為什麼需要另一套**（[▶ 29:55](https://youtu.be/e_tMD_rSHKg?t=1795)）：

- CRLB 算得出來，但**不告訴你**哪個估計量不偏且變異數等於它。前兩例剛好 MLE 就是。
- 如果 MLE 有偏，或不偏但變異數 > CRLB，**不表示沒有 UMVUE**。可能有一個 UMVUE，變異數比 CRLB 大，但仍是所有不偏估計量裡最小的。
- 這時動差法、MLE 都試過了也沒用，CRLB 就無能為力。
- 所以需要更一般的方法：充分統計量。它和**條件**（conditional）的觀念有關。

---

## 6. 條件機率

[▶ 31:27](https://youtu.be/e_tMD_rSHKg?t=1887)

$A,B$ 是事件（樣本空間的子集）。

- 「given $B$」：$B$ 已經發生了，也就是實驗結果落在 $B$ 裡。但不知道有沒有落在 $A$ 裡。
- 問：$B$ 已發生，$A$ 發生的機率有多大？這叫**條件機率**（conditional probability）。

> **定義**（課本 Definition 1.4.1，p. 24）：$P(B)>0$，
> $$P(A\mid B)=\frac{P(A\cap B)}{P(B)}.$$

[▶ 33:34](https://youtu.be/e_tMD_rSHKg?t=2014) $B$ 固定，$P(\cdot\mid B)$ 是 $A$ 的函數（$A$ 是 $S$ 的任何子集）。

> **事實**：$P(\cdot\mid B)$ 也是**機率集合函數**，滿足三公理：
> 1. $P(A\mid B)\ge 0$：分子是機率，$\ge 0$。
> 2. $P(S\mid B)=\frac{P(S\cap B)}{P(B)}=\frac{P(B)}{P(B)}=1$。
> 3. $A_1,A_2,\dots$ 兩兩互斥 ⇒ $P\left(\bigcup A_i\mid B\right)=\sum P(A_i\mid B)$。

（第 3 條老師只列出沒證。【課本補充】證明：$A_i\cap B$ 也兩兩互斥，$P\left(\left(\bigcup A_i\right)\cap B\right)=P\left(\bigcup(A_i\cap B)\right)=\sum P(A_i\cap B)$，再除以 $P(B)$。）

---

## 7. 條件 pdf

[▶ 36:41](https://youtu.be/e_tMD_rSHKg?t=2201) 介紹條件機率，是為了定義**條件 pdf**。

$X,Y$ 有 joint pdf $f(x,y)$；marginal pdf：$f_X(x)=\int f(x,y)\,dy$，$f_Y(y)=\int f(x,y)\,dx$。

> **定義（條件 pdf，conditional pdf）**（[▶ 37:44](https://youtu.be/e_tMD_rSHKg?t=2264)，課本 §2.3，p. 109）：
> $$f(y\mid x)=\frac{f(x,y)}{f_X(x)},\qquad f_X(x)>0.$$
> 已知 $X=x$ 發生了，$Y$ 的 pdf。

和條件機率一樣：分母是「已發生的」（$X$ 的 pdf），分子是「同時發生」（joint pdf）。$x$ 固定，所以是 $y$ 的函數。

**條件 pdf 還是 pdf**（[▶ 38:44](https://youtu.be/e_tMD_rSHKg?t=2324)）：

1. $f(y\mid x)\ge 0$。
2. 對每個固定的 $x$：
$$\int_{-\infty}^{\infty}f(y\mid x)\,dy=\frac{1}{f_X(x)}\int f(x,y)\,dy=\frac{f_X(x)}{f_X(x)}=1.$$

（離散型把積分換成加總。）

下次介紹充分統計量。

---

## 8. 一頁速查表

**用 CRLB 證 UMVUE**：不偏 → 算 Var → 算 $\text{CRLB}=\dfrac{1}{-nE[\partial^2_\theta\log f(X;\theta)]}$ → 相等就是 UMVUE。

| 分配 | $\partial_\theta^2\log f$ | $E[\cdot]$ | CRLB | $\text{Var}(\bar X)$ | UMVUE |
|---|---|---|---|---|---|
| Poisson$(\lambda)$ | $-\frac{x}{\lambda^2}$ | $-\frac1\lambda$ | $\frac\lambda n$ | $\frac\lambda n$ | $\bar X$ |
| Bernoulli$(p)$ | $-\frac{x}{p^2}-\frac{1-x}{(1-p)^2}$ | $-\frac{1}{p(1-p)}$ | $\frac{p(1-p)}{n}$ | $\frac{p(1-p)}{n}$ | $\bar X$ |

**CRLB 的限制**：沒有估計量達到下界，不表示沒有 UMVUE → 需要充分統計量。

**條件機率**：$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$，仍是機率集合函數。

**條件 pdf**：$f(y\mid x)=\frac{f(x,y)}{f_X(x)}$，非負、對 $y$ 積分＝1。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 條件 pdf | 下一集：充分統計量的定義（給定統計量，樣本的條件分配不含 $\theta$） |
| CRLB 的限制 | Rao–Blackwell、Lehmann–Scheffé（另一套找 UMVUE 的方法） |

---

## 附：本集一句話總結

> **Poisson 和 Bernoulli 的 MLE $\bar X$ 都不偏，變異數剛好等於 Cramér–Rao 下界，所以是 UMVUE；但若沒有估計量達到下界，CRLB 就無法判斷，因此需要以「條件 pdf $f(y\mid x)=f(x,y)/f_X(x)$」為基礎的充分統計量方法。**

---

*筆記依據「統計學」Lec20 錄影逐字稿（whisper large-v3-turbo，40:22）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
