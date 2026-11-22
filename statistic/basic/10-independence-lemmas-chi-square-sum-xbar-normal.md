---
course: 統計學（數理統計，數學系）
episode: 10
lecture: Lec10
date: 待補
video: https://youtu.be/e4fTfQreXO4
notes: Hogg 8th ed. Theorem 2.4.4 $E[u(X_1)v(X_2)]=E[u(X_1)]E[v(X_2)]$（p. 122）；Corollary 3.3.1 獨立卡方之和（p. 180）；Theorem 3.4.1 $Z^2\sim\chi^2(1)$（p. 192）；Theorem 3.6.1 常態樣本的 $\bar X$、$S^2$（p. 214）；Theorem 3.4.2 獨立常態的線性組合（p. 193）
---

# 第 10 集 · Lec10：幾個預備結果；獨立卡方相加；$Z^2\sim\chi^2(1)$；$\bar X$ 是常態 [▶ 影片](https://youtu.be/e4fTfQreXO4)

← 上一集：[09](09-transformation-example-random-sample-statistic-mgf-independence.md) ｜ [總目錄](../README.md) ｜ 下一集：[11](11-xbar-s2-independence-chi-square-statistical-inference.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 10 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（40:41，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.4、§3.3、§3.4、§3.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「卡方」→「卡彎」，「joint」→「Join」，「variance」→「valence」，「$\sqrt\pi=\Gamma(1/2)$」→「根號π是等於就啥伽馬二分之一」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. (A) 兩組隨機變數獨立；獨立變數的函數還是獨立](#1-a-兩組隨機變數獨立獨立變數的函數還是獨立)
- [2. (B) 獨立 ⇒ 相乘的期望值＝期望值相乘](#2-b-獨立--相乘的期望值期望值相乘)
- [3. (C) 從 joint mgf 取出一個的 mgf](#3-c-從-joint-mgf-取出一個的-mgf)
- [4. (D) 獨立卡方相加還是卡方](#4-d-獨立卡方相加還是卡方)
- [5. (E) 標準化；(F) 對稱函數的積分](#5-e-標準化f-對稱函數的積分)
- [6. (G) 標準常態平方是 χ²(1)](#6-g-標準常態平方是-χ1)
- [7. 主定理：常態樣本的 X̄ 與 S²](#7-主定理常態樣本的-x̄-與-s)
- [8. 證明 (a)：X̄～N(μ, σ²/n)](#8-證明-ax̄nμ-σn)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/e4fTfQreXO4?t=0) 準備講一個「統計上非常重要的定理」。先介紹幾個小結果 (A)–(G)，它們不大，但常常用到。

| 編號 | 結果 | 課本 |
|---|---|---|
| (A) | 獨立變數各取函數，還是獨立 | — |
| (B) | 獨立 ⇒ $E[g(X)h(Y)]=E[g(X)]E[h(Y)]$ | Theorem 2.4.4，p. 122 |
| (C) | $M_{X,Y}(0,t)=M_Y(t)$ | — |
| (D) | 獨立 $\chi^2(r_1)+\chi^2(r_2)=\chi^2(r_1+r_2)$ | Corollary 3.3.1，p. 180 |
| (E) | $\frac{X-\mu}{\sigma}\sim N(0,1)$ | 已證 |
| (F) | 偶函數 $\int_{-a}^a=2\int_0^a$ | — |
| (G) | $Z\sim N(0,1)\Rightarrow Z^2\sim\chi^2(1)$ | Theorem 3.4.1，p. 192 |
| 主定理 | 常態樣本：$\bar X\sim N(\mu,\sigma^2/n)$；$\bar X\perp S^2$；$\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$ | Theorem 3.6.1，p. 214 |

---

## 1. (A) 兩組隨機變數獨立；獨立變數的函數還是獨立

[▶ 00:32](https://youtu.be/e4fTfQreXO4?t=32)

> **定義**：$(X_1,\dots,X_n)$ 和 $(Y_1,\dots,Y_m)$ 兩組獨立，意思是
> $$f(x_1,\dots,x_n,y_1,\dots,y_m)=f_{\mathbf X}(x_1,\dots,x_n)\,f_{\mathbf Y}(y_1,\dots,y_m).$$

- 和兩個隨機變數獨立一樣：合起來的 joint pdf（$n+m$ 個）＝兩組各自的 joint pdf 相乘。
- [▶ 02:07](https://youtu.be/e4fTfQreXO4?t=127) **組內**有沒有獨立都沒關係。只說兩組之間獨立。

**重要觀念**（[▶ 03:09](https://youtu.be/e4fTfQreXO4?t=189)）：獨立的隨機變數，各自取函數，結果還是獨立。

例：$X_1,X_2,X_3,X_4$ 獨立。

- 各取一個函數：$3X_1$、$2X_2$、$e^{X_3}$、$\sin X_4$ 還是獨立。
- 分成兩組各取函數：$X_1+X_2$ 和 $X_3-X_4$（或 $X_3X_4$）還是獨立。

[▶ 04:44](https://youtu.be/e4fTfQreXO4?t=284) 老師說這個「沒辦法證明，就當作是對的」。

【課本補充】這其實可以證明（課本 §2.4、§2.6 有相關討論，例如用 mgf 可分解或 cdf 可分解來證）。本課不證。

---

## 2. (B) 獨立 ⇒ 相乘的期望值＝期望值相乘

[▶ 05:14](https://youtu.be/e4fTfQreXO4?t=314) 這個會**非常常用**。

> **定理**（課本 Theorem 2.4.4，p. 122）：$X,Y$ 獨立，則
> $$E[g(X)h(Y)]=E[g(X)]\,E[h(Y)].$$

可以先各自取期望值再相乘，比較容易。

**證明**（[▶ 06:48](https://youtu.be/e4fTfQreXO4?t=408)）：

1. 照定義，兩個隨機變數的函數取期望值：大寫改小寫，乘 joint pdf，雙重積分：
$$E[g(X)h(Y)]=\iint g(x)h(y)f(x,y)\,dx\,dy.$$
2. 獨立 ⇒ $f(x,y)=f_X(x)f_Y(y)$。
3. 被積函數分成「只有 $x$」×「只有 $y$」，雙重積分拆成兩個積分相乘：
$$=\int g(x)f_X(x)\,dx\cdot\int h(y)f_Y(y)\,dy=E[g(X)]E[h(Y)].$$

（離散型把積分換成相加。）

---

## 3. (C) 從 joint mgf 取出一個的 mgf

[▶ 09:56](https://youtu.be/e4fTfQreXO4?t=596)

> $$M_{X,Y}(0,t)=M_Y(t).$$

把 $X$ 對應的 $t$ 定成 0，就只剩 $Y$ 的 mgf。

**證明**：$M_{X,Y}(t_1,t)=E\left(e^{t_1X+tY}\right)$。令 $t_1=0$：$E\left(e^{tY}\right)=M_Y(t)$。

**用途**（[▶ 13:07](https://youtu.be/e4fTfQreXO4?t=787)）：好幾個隨機變數的 joint mgf 找出來了，想要其中幾個的 mgf，就把其他的 $t$ 都定成 0。

---

## 4. (D) 獨立卡方相加還是卡方

[▶ 14:02](https://youtu.be/e4fTfQreXO4?t=842)

> $X\sim\chi^2(r_1)$、$Y\sim\chi^2(r_2)$、$X,Y$ 獨立 ⇒ $X+Y\sim\chi^2(r_1+r_2)$。

自由度相加。

[▶ 14:32](https://youtu.be/e4fTfQreXO4?t=872) 【口頭】碰到相加的，證明都用 **mgf**，比較簡單，不要用變數變換。

**證明**：

$$M_{X+Y}(t)=E\left(e^{t(X+Y)}\right)=E\left(e^{tX}e^{tY}\right).$$

$e^{tX}$ 是 $X$ 的函數、$e^{tY}$ 是 $Y$ 的函數，$X,Y$ 獨立，由 (B)：

$$=E\left(e^{tX}\right)E\left(e^{tY}\right)=M_X(t)M_Y(t)=(1-2t)^{-r_1/2}(1-2t)^{-r_2/2}=(1-2t)^{-(r_1+r_2)/2},\quad t<\tfrac12.$$

只有卡方有這種 mgf，由唯一性 $X+Y\sim\chi^2(r_1+r_2)$。∎

【課本補充】課本 Corollary 3.3.1（p. 180）推廣到 $n$ 個：獨立 $X_i\sim\chi^2(r_i)$ ⇒ $\sum X_i\sim\chi^2\left(\sum r_i\right)$。證法相同。

---

## 5. (E) 標準化；(F) 對稱函數的積分

**(E)**（[▶ 20:17](https://youtu.be/e4fTfQreXO4?t=1217)）：$X\sim N(\mu,\sigma^2)$ ⇒ $\frac{X-\mu}{\sigma}\sim N(0,1)$。已證過（Lec05、Lec06），一定要知道。

**(F)**（[▶ 20:47](https://youtu.be/e4fTfQreXO4?t=1247)）：若 $f(-x)=f(x)$（對 0 對稱，偶函數），則
$$\int_{-a}^{a}f(x)\,dx=2\int_0^af(x)\,dx.$$
兩邊面積一樣，積一半再乘 2。

---

## 6. (G) 標準常態平方是 χ²(1)

[▶ 21:17](https://youtu.be/e4fTfQreXO4?t=1277)

> $Z\sim N(0,1)$ ⇒ $Y=Z^2\sim\chi^2(1)$。

可以用分配函數法，也可以用 mgf 法（老師說實習課可能用別的方法）。這裡用**分配函數法**。

**Step 1：分配函數**（[▶ 22:19](https://youtu.be/e4fTfQreXO4?t=1339)）。$Y=Z^2\ge 0$，所以只看 $y>0$：
$$F_Y(y)=P(Z^2\le y)=P\left(-\sqrt y\le Z\le\sqrt y\right).$$

**Step 2：寫成積分**（[▶ 23:51](https://youtu.be/e4fTfQreXO4?t=1431)）。隨機變數落在一個範圍的機率＝pdf 對那個範圍積分：
$$F_Y(y)=\int_{-\sqrt y}^{\sqrt y}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz.$$

**Step 3：用 (F)**（[▶ 24:22](https://youtu.be/e4fTfQreXO4?t=1462)）。被積函數只和 $z^2$ 有關，$f(-z)=f(z)$：
$$F_Y(y)=2\int_0^{\sqrt y}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz.$$
積不出來沒關係，要的是微分。

**Step 4：微分**（[▶ 25:29](https://youtu.be/e4fTfQreXO4?t=1529)）。上限 $\sqrt y$，代進被積函數，再乘 $\frac{d}{dy}\sqrt y=\frac12y^{-1/2}$：
$$f_Y(y)=2\cdot\frac{1}{\sqrt{2\pi}}e^{-y/2}\cdot\frac12y^{-1/2}=\frac{1}{\sqrt{2\pi}}y^{-1/2}e^{-y/2},\quad y>0.$$

**Step 5：認出卡方**（[▶ 27:05](https://youtu.be/e4fTfQreXO4?t=1625)）。關鍵：$\sqrt\pi=\Gamma(1/2)$，$\sqrt2=2^{1/2}$，$y^{-1/2}=y^{1/2-1}$：
$$f_Y(y)=\frac{1}{\Gamma(1/2)2^{1/2}}y^{1/2-1}e^{-y/2}.$$
對照 $\chi^2(r)$ 的 pdf $\frac{1}{\Gamma(r/2)2^{r/2}}y^{r/2-1}e^{-y/2}$，$r=1$。∎

【口頭】你要能看出 $\frac{1}{\sqrt{2\pi}}$ 裡藏著 $\Gamma(1/2)$。

---

## 7. 主定理：常態樣本的 X̄ 與 S²

[▶ 29:13](https://youtu.be/e4fTfQreXO4?t=1753) 統計裡非常重要的定理，最重要的是 (b)、(c)。

> **定理**（課本 Theorem 3.6.1，p. 214）：$X_1,\dots,X_n$ 是來自 $N(\mu,\sigma^2)$ 的隨機樣本。令
> $$\bar X=\frac1n\sum_{i=1}^nX_i\ (\text{樣本平均數}),\qquad S^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2\ (\text{樣本變異數}).$$
> 則
> (a) $\bar X\sim N\left(\mu,\dfrac{\sigma^2}{n}\right)$；
> (b) $\bar X$ 和 $S^2$ **獨立**；
> (c) $\dfrac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$。

**為什麼 (b) 難得**（[▶ 30:52](https://youtu.be/e4fTfQreXO4?t=1852)）：

- $\bar X$ 和 $S^2$ 都是**同一組** $X_1,\dots,X_n$ 的函數。
- 由 (A)，獨立的變數「各自」取函數會獨立。但對**同一組**取兩個函數，一般**不會**獨立：
$$g(X,Y)\text{ 和 }h(X,Y)\text{ 一般不獨立}.$$
- 所以 $\bar X\perp S^2$ 是很少見的結果。

(c) 現在比較難理解。下次證 (b)、(c)，今天先證 (a)。

---

## 8. 證明 (a)：X̄～N(μ, σ²/n)

[▶ 33:31](https://youtu.be/e4fTfQreXO4?t=2011) 找 $\bar X$ 的 mgf。

**Step 1**：
$$M_{\bar X}(t)=E\left(e^{t\bar X}\right)=E\left(e^{\frac tn(X_1+\cdots+X_n)}\right)=E\left(e^{\frac tnX_1}e^{\frac tnX_2}\cdots e^{\frac tnX_n}\right).$$
指數裡的相加拆成相乘。

**Step 2**（[▶ 35:06](https://youtu.be/e4fTfQreXO4?t=2106)）：每個因子是一個 $X_i$ 的函數 $g_i(X_i)$。隨機樣本 ⇒ 獨立，由 (B)（推廣到 $n$ 個）：
$$=E\left(e^{\frac tnX_1}\right)E\left(e^{\frac tnX_2}\cdots\right)\cdots=\prod_{i=1}^nM_{X_i}\left(\frac tn\right).$$

**Step 3**（[▶ 36:39](https://youtu.be/e4fTfQreXO4?t=2199)）：同分配 ⇒ 每個 $M_{X_i}$ 都是 $N(\mu,\sigma^2)$ 的 mgf，在 $t/n$ 那一點：
$$M_{X_i}\left(\frac tn\right)=\exp\left(\mu\frac tn+\frac{\sigma^2}{2}\frac{t^2}{n^2}\right).$$

**Step 4**（[▶ 37:53](https://youtu.be/e4fTfQreXO4?t=2273)）：$n$ 個相乘 → 指數相加，乘 $n$：
$$M_{\bar X}(t)=\exp\left(n\mu\frac tn+n\frac{\sigma^2t^2}{2n^2}\right)=\exp\left(\mu t+\frac12\cdot\frac{\sigma^2}{n}t^2\right).$$

【口頭】為什麼要把 $t$ 都挪到後面？因為要找的是 $\bar X$ 在 $t$ 那一點的 mgf，要整理成 $e^{(\cdot)t+\frac12(\cdot)t^2}$ 的樣子，才能讀出 mean 和 variance。

**Step 5**：這是 $N\left(\mu,\frac{\sigma^2}{n}\right)$ 的 mgf：$t$ 前面是 mean $\mu$，$\frac12t^2$ 前面是 variance $\frac{\sigma^2}{n}$。由唯一性得證。∎

[▶ 40:00](https://youtu.be/e4fTfQreXO4?t=2400) 【口頭】這種證明一定要會。相關的狀況很多，自己導一遍，會一種就全部會。

【課本補充】更一般地（Theorem 3.4.2，p. 193）：獨立 $X_i\sim N(\mu_i,\sigma_i^2)$ ⇒ $\sum a_iX_i\sim N\left(\sum a_i\mu_i,\ \sum a_i^2\sigma_i^2\right)$。

---

## 9. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| 獨立 ⇒ $E[g(X)h(Y)]=E[g(X)]E[h(Y)]$ | joint pdf 拆成相乘，雙重積分拆開 |
| $M_{X,Y}(0,t)=M_Y(t)$ | $t_1=0$ 代入 $E(e^{t_1X+tY})$ |
| 獨立 $\chi^2(r_1)+\chi^2(r_2)=\chi^2(r_1+r_2)$ | $M_{X+Y}=M_XM_Y=(1-2t)^{-(r_1+r_2)/2}$ |
| $Z^2\sim\chi^2(1)$ | $F_Y(y)=2\int_0^{\sqrt y}\phi$；微分乘 $\frac12y^{-1/2}$；$\sqrt\pi=\Gamma(\frac12)$ |
| $\bar X\sim N(\mu,\sigma^2/n)$ | $M_{\bar X}(t)=[M_X(t/n)]^n$ |

**獨立相加的 mgf**：$X_1,\dots,X_n$ 獨立 ⇒ $M_{\sum X_i}(t)=\prod M_{X_i}(t)$。

**主定理**（常態隨機樣本）：

1. $\bar X\sim N(\mu,\sigma^2/n)$
2. $\bar X\perp S^2$（同一組樣本的兩個函數卻獨立，很難得）
3. $(n-1)S^2/\sigma^2\sim\chi^2(n-1)$

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 主定理 (b)、(c) | 下一集證明 |
| $Z^2\sim\chi^2(1)$、卡方相加 | 證明 (c)；$t$ 分配、$F$ 分配 |
| $\bar X\sim N(\mu,\sigma^2/n)$ | 信賴區間、檢定 |

---

## 附：本集一句話總結

> **獨立變數各取函數仍獨立、相乘的期望值可拆開；用 mgf 證明獨立卡方相加自由度相加、用分配函數法證明 $Z^2\sim\chi^2(1)$；接著提出常態樣本的主定理，並用 mgf 證明 $\bar X\sim N(\mu,\sigma^2/n)$。**

---

*筆記依據「統計學」Lec10 錄影逐字稿（whisper large-v3-turbo，40:41）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
