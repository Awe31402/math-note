---
course: 統計學（數理統計，數學系）
episode: 19
lecture: Lec19
date: 待補
video: https://youtu.be/oRcceUnloBk
notes: Hogg 8th ed. §6.2 Rao–Cramér 下界（Theorem 6.2.1，p. 365；Corollary 6.2.1，p. 366）；正則條件 Assumptions 6.1.1（p. 356）、6.2.1（p. 362）；Fisher 資訊（p. 363）；有效估計量 Definition 6.2.1（p. 366）
---

# 第 19 集 · Lec19：$\tau(\theta)$ 的 UMVUE；Cramér–Rao 下界與證明 [▶ 影片](https://youtu.be/oRcceUnloBk)

← 上一集：[18](18-invariance-examples-umvue.md) ｜ [總目錄](../README.md) ｜ 下一集：[20](20-cramer-rao-examples-conditional-pdf.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 19 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（56:23，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §6.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Cramér–Rao lower bound」→「Clamoura-Loban／Climate Raw Raw／Colomero low-bomb」，「下界」→「下陷」，「regularity conditions」→「regulatory conditions」，「Cauchy–Schwarz」照錄，「density function」照錄，「variance」→「valance／valence」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. τ(θ) 的 UMVUE](#1-τθ-的-umvue)
- [2. 怎麼找 UMVUE：兩種方法](#2-怎麼找-umvue兩種方法)
- [3. 正則條件](#3-正則條件)
- [4. Cramér–Rao 下界](#4-cramérrao-下界)
  - [4.1 定理](#41-定理)
  - [4.2 為什麼有用：達到下界就是 UMVUE](#42-為什麼有用達到下界就是-umvue)
- [5. 證明](#5-證明)
  - [5.1 引理：score 的期望值是 0](#51-引理score-的期望值是-0)
  - [5.2 對不偏條件微分](#52-對不偏條件微分)
  - [5.3 把 joint pdf 的微分寫成 score](#53-把-joint-pdf-的微分寫成-score)
  - [5.4 Cauchy–Schwarz](#54-cauchyschwarz)
  - [5.5 算分母](#55-算分母)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $\tau(\theta)$ 的不偏估計量、UMVUE | §7.1 |
| 正則條件 | Assumptions 6.1.1、6.2.1 |
| Cramér–Rao 下界（課本叫 Rao–Cramér） | Theorem 6.2.1，p. 365 |
| 達到下界 ⇒ UMVUE | Definition 6.2.1（有效估計量） |

---

## 1. τ(θ) 的 UMVUE

[▶ 00:33](https://youtu.be/oRcceUnloBk?t=33) 有時候要估的不是 $\theta$，而是 $\theta$ 的函數 $\tau(\theta)$（例如 $\theta^2$、$3\theta$）。定義類似：

> **不偏**：$E_\theta\left[\hat\tau(\theta)\right]=\tau(\theta)$，對所有 $\theta$。
>
> **UMVUE**：不偏估計量 $\hat\tau$ 若對**任何** $\tau(\theta)$ 的不偏估計量 $\hat\tau^*$，
> $$\text{Var}_\theta(\hat\tau)\le\text{Var}_\theta(\hat\tau^*),\qquad\text{對所有 }\theta,$$
> 就叫 $\tau(\theta)$ 的 UMVUE。

[▶ 03:38](https://youtu.be/oRcceUnloBk?t=218) 每個字的意思：

- 固定一個 $\theta$：變異數在所有不偏估計量裡最小 → MVUE。
- 前面加 U（uniformly）：**不管哪個 $\theta$ 是對的**，都最小。

[▶ 05:11](https://youtu.be/oRcceUnloBk?t=311) 【口頭】要比較的是**所有**不偏估計量，不是兩個在比；而且不知道 $\theta$ 是多少，所以**所有 $\theta$** 都要比。就像五門課的第一名都是同一個人。這個觀念比一般的「最小」更強。

---

## 2. 怎麼找 UMVUE：兩種方法

[▶ 06:44](https://youtu.be/oRcceUnloBk?t=404) 書上大多講兩種：

1. 比較理論的方法（牽涉很多理論），**學期最後**整個在講那個。
2. 比較簡單的方法：**Cramér–Rao 下界**（Cramér–Rao lower bound）。

[▶ 07:15](https://youtu.be/oRcceUnloBk?t=435) 【口頭】兩人各自發現這個定理，所以用兩人的姓合起來命名。老師說 Cramér「應該是西班牙人」，Rao 是印度人。

---

## 3. 正則條件

[▶ 08:17](https://youtu.be/oRcceUnloBk?t=497) 定理要成立，分配要滿足一些條件，叫**正則條件**（regularity conditions）。

【口頭】[▶ 08:48](https://youtu.be/oRcceUnloBk?t=528) 有四個。**不用背**，考試絕對不會叫你背；但要知道有這些條件，盡量看懂。

1. **參數空間是區間**（[▶ 09:51](https://youtu.be/oRcceUnloBk?t=591)）：$(a,\infty)$、$(a,b)$、$(-\infty,b)$、$(-\infty,\infty)$ 之類，不能是一點一點的；$a,b$ 和參數無關。
2. **support 和 $\theta$ 無關**（[▶ 10:21](https://youtu.be/oRcceUnloBk?t=621)）：$\{x: f(x;\theta)=0\}$ 這個集合不隨 $\theta$ 變。
3. **pdf 的微分和積分可以交換**（[▶ 10:54](https://youtu.be/oRcceUnloBk?t=654)）：
$$\int\frac{\partial}{\partial\theta}f(x;\theta)\,dx=\frac{\partial}{\partial\theta}\int f(x;\theta)\,dx=\frac{\partial}{\partial\theta}1=0.$$
   【口頭】以後證明時看到「pdf 對 $\theta$ 微分再對 $x$ 積分」，就知道是 0。
4. **估計量乘 joint pdf 的微分也可以交換**（[▶ 12:27](https://youtu.be/oRcceUnloBk?t=747)）：對 $\tau(\theta)$ 的不偏估計量 $T(X_1,\dots,X_n)$，
$$\int\!\cdots\!\int T(\mathbf x)\frac{\partial}{\partial\theta}f(\mathbf x;\theta)\,d\mathbf x=\frac{\partial}{\partial\theta}\int\!\cdots\!\int T(\mathbf x)f(\mathbf x;\theta)\,d\mathbf x.$$

⚠️ 逐字稿缺字：[▶ 13:31](https://youtu.be/oRcceUnloBk?t=811) 老師說板書第 4 條「少寫了一個 $T(x_1,\dots,x_n)$」，已補上。

【課本補充】注意 $U(0,\theta)$ 不滿足條件 2（support 是 $[0,\theta]$，隨 $\theta$ 變），所以不能用 Cramér–Rao。

---

## 4. Cramér–Rao 下界

### 4.1 定理

[▶ 15:12](https://youtu.be/oRcceUnloBk?t=912)

> **定理（Cramér–Rao 下界）**（課本 Theorem 6.2.1、Corollary 6.2.1，p. 365–366）：正則條件成立，$X_1,\dots,X_n$ iid $f(x;\theta)$，$\hat\tau$ 是 $\tau(\theta)$ 的**任何**不偏估計量，則
> $$\text{Var}_\theta(\hat\tau)\ \ge\ \frac{[\tau'(\theta)]^2}{nE_\theta\left[\left(\frac{\partial}{\partial\theta}\log f(X;\theta)\right)^2\right]}=\frac{[\tau'(\theta)]^2}{-nE_\theta\left[\frac{\partial^2}{\partial\theta^2}\log f(X;\theta)\right]}.$$
> 右邊叫 **Cramér–Rao 下界**（lower bound）。

**怎麼讀分母**（[▶ 19:54](https://youtu.be/oRcceUnloBk?t=1194)）：

- pdf 裡的 $x$ 改成大寫 $X$（才是隨機變數）。
- 取 log、對 $\theta$ 微分、平方、再對 $X$ 取期望值，乘 $n$（$n$ 個樣本）。
- 或：取 log、對 $\theta$ 微分**兩次**、取期望值、加負號、乘 $n$。

**分子**：$\tau(\theta)$ 的微分的平方。估的就是 $\theta$ 時，$\tau(\theta)=\theta$，分子是 $1$。

[▶ 42:58](https://youtu.be/oRcceUnloBk?t=2578) 老師比較喜歡**第二種**（微分兩次）：一次微分再平方常常有很多項，取期望值要積分比較麻煩；微分兩次常常比較簡單。

【課本補充】課本把 $I(\theta)=E\left[\left(\frac{\partial}{\partial\theta}\log f(X;\theta)\right)^2\right]=-E\left[\frac{\partial^2}{\partial\theta^2}\log f(X;\theta)\right]$ 叫 **Fisher 資訊**（Fisher information，p. 363），下界寫成 $\frac{[\tau'(\theta)]^2}{nI(\theta)}$。兩種寫法相等的證明在課本 p. 363（老師沒證）。

### 4.2 為什麼有用：達到下界就是 UMVUE

[▶ 17:20](https://youtu.be/oRcceUnloBk?t=1040)

- 定理沒有說誰是 UMVUE，只說：**所有不偏估計量的變異數都 $\ge$ 下界**。
- 所以：如果找到一個不偏估計量，**變異數剛好等於下界**，它就是 UMVUE——沒有人能比它小。

【口頭】[▶ 17:51](https://youtu.be/oRcceUnloBk?t=1071) 比喻：全班沒有人超過 90 分（90 是上界）。如果有人剛好 90 分，他一定是那一科第一名。

[▶ 54:33](https://youtu.be/oRcceUnloBk?t=3273) 「達到下界」（achieve the bound）：不偏估計量的變異數＝Cramér–Rao 下界 ⇒ 它是 UMVUE。

【課本補充】課本 Definition 6.2.1（p. 366）把達到下界的不偏估計量叫**有效估計量**（efficient estimator）。

---

## 5. 證明

[▶ 22:58](https://youtu.be/oRcceUnloBk?t=1378) 假設連續型（離散型把積分改成加總，同樣成立）。

### 5.1 引理：score 的期望值是 0

[▶ 23:30](https://youtu.be/oRcceUnloBk?t=1410)

> $$E_\theta\left[\frac{\partial}{\partial\theta}\log f(X;\theta)\right]=0.$$

**證明**：$X$ 的函數取期望值，改小寫乘 pdf 積分。$\log$ 的微分＝分母放 $f$、乘 $f$ 的微分，和 pdf 消掉：
$$\int\frac{\frac{\partial}{\partial\theta}f(x;\theta)}{f(x;\theta)}f(x;\theta)\,dx=\int\frac{\partial}{\partial\theta}f(x;\theta)\,dx=0\quad(\text{條件 3}).$$

### 5.2 對不偏條件微分

[▶ 26:34](https://youtu.be/oRcceUnloBk?t=1594) 記 $\hat\tau=T(X_1,\dots,X_n)$，$f(\mathbf x;\theta)=\prod f(x_i;\theta)$（獨立相乘、同分配同一個 $f$）。不偏：
$$\tau(\theta)=E_\theta[T]=\int\!\cdots\!\int T(\mathbf x)f(\mathbf x;\theta)\,d\mathbf x.$$

**兩邊對 $\theta$ 微分**，並**多減一項 0**（[▶ 30:07](https://youtu.be/oRcceUnloBk?t=1807)）：
$$\tau'(\theta)=\frac{\partial}{\partial\theta}\int T(\mathbf x)f(\mathbf x;\theta)\,d\mathbf x-\tau(\theta)\frac{\partial}{\partial\theta}\int f(\mathbf x;\theta)\,d\mathbf x.$$
第二項是 0：joint pdf 積分是 1，1 的微分是 0。

【口頭】為什麼要多減這一項？沒有它就證不出來。這是他們厲害的地方，這個技巧要記。

[▶ 31:40](https://youtu.be/oRcceUnloBk?t=1900) 微分搬進積分（條件 3、4）。$T(\mathbf x)$ 和 $\tau(\theta)$ 對 $\mathbf x$ 積分時當常數，只有 joint pdf 被微分；兩項後面的東西一樣，合併：
$$\tau'(\theta)=\int\!\cdots\!\int\left[T(\mathbf x)-\tau(\theta)\right]\frac{\partial}{\partial\theta}f(\mathbf x;\theta)\,d\mathbf x.$$

### 5.3 把 joint pdf 的微分寫成 score

[▶ 33:44](https://youtu.be/oRcceUnloBk?t=2024) joint pdf 是 $n$ 個相乘，用乘積法則（微第一個乘其他、加微第二個乘其他……）：
$$\frac{\partial}{\partial\theta}\prod_{i=1}^nf(x_i;\theta)=\sum_{j=1}^n\left[\frac{\partial}{\partial\theta}f(x_j;\theta)\right]\prod_{i\ne j}f(x_i;\theta).$$

[▶ 37:23](https://youtu.be/oRcceUnloBk?t=2243) 技巧：$\frac{\partial}{\partial\theta}f(x_j;\theta)=\left[\frac{\partial}{\partial\theta}\log f(x_j;\theta)\right]f(x_j;\theta)$。多出來的 $f(x_j;\theta)$ 剛好補上 $\prod_{i\ne j}$ 缺的那一項：
$$\frac{\partial}{\partial\theta}f(\mathbf x;\theta)=\left[\sum_{j=1}^n\frac{\partial}{\partial\theta}\log f(x_j;\theta)\right]f(\mathbf x;\theta).$$

[▶ 40:28](https://youtu.be/oRcceUnloBk?t=2428) 代回。**關鍵觀念**（[▶ 41:00](https://youtu.be/oRcceUnloBk?t=2460)）：「$\mathbf x$ 的函數 × joint pdf 再積分」＝那個函數的期望值。所以
$$\tau'(\theta)=E_\theta\left[\left(T-\tau(\theta)\right)\cdot\sum_{j=1}^n\frac{\partial}{\partial\theta}\log f(X_j;\theta)\right].$$

### 5.4 Cauchy–Schwarz

[▶ 44:08](https://youtu.be/oRcceUnloBk?t=2648)

> **Cauchy–Schwarz 不等式**：$[E(XY)]^2\le E(X^2)E(Y^2)$。

【口頭】[▶ 45:45](https://youtu.be/oRcceUnloBk?t=2745) 證明回去機率課本看。這個不等式在數學很多地方都有（級數、積分），統計上是這個形式，證明技巧類似。

令 $X=T-\tau(\theta)$、$Y=\sum_j\frac{\partial}{\partial\theta}\log f(X_j;\theta)$，兩邊平方（[▶ 47:19](https://youtu.be/oRcceUnloBk?t=2839)）：
$$[\tau'(\theta)]^2\le E\left[(T-\tau(\theta))^2\right]\cdot E\left[\left(\sum_j\frac{\partial}{\partial\theta}\log f(X_j;\theta)\right)^2\right].$$

$T$ 不偏、期望值是 $\tau(\theta)$，所以 $E[(T-\tau(\theta))^2]=\text{Var}(T)$。除過去：
$$\text{Var}(T)\ge\frac{[\tau'(\theta)]^2}{E\left[\left(\sum_j\frac{\partial}{\partial\theta}\log f(X_j;\theta)\right)^2\right]}.$$

### 5.5 算分母

[▶ 49:52](https://youtu.be/oRcceUnloBk?t=2992) 令 $S_j=\frac{\partial}{\partial\theta}\log f(X_j;\theta)$。和的平方＝平方和＋兩兩相乘：
$$E\left[\left(\sum_jS_j\right)^2\right]=\sum_jE(S_j^2)+\sum_{i\ne j}E(S_iS_j).$$

- [▶ 50:54](https://youtu.be/oRcceUnloBk?t=3054) $S_i$ 是 $X_i$ 的函數、$S_j$ 是 $X_j$ 的函數，獨立 ⇒ $E(S_iS_j)=E(S_i)E(S_j)=0\cdot 0=0$（§5.1 引理）。
- [▶ 52:27](https://youtu.be/oRcceUnloBk?t=3147) 同分配 ⇒ 每個 $E(S_j^2)$ 一樣，共 $n$ 個。

$$E\left[\left(\sum_jS_j\right)^2\right]=nE\left[\left(\frac{\partial}{\partial\theta}\log f(X;\theta)\right)^2\right].$$

代回得定理。∎

【口頭】[▶ 53:30](https://youtu.be/oRcceUnloBk?t=3210) 這大概是這門課最長的證明，不容易，但要讀統計就要會證。了解整個證明過程，會懂得比較多。

---

## 6. 一頁速查表

**UMVUE（估 $\tau(\theta)$）**：不偏，且 $\text{Var}_\theta(\hat\tau)\le\text{Var}_\theta(\hat\tau^*)$，$\forall$ 不偏 $\hat\tau^*$，$\forall\theta$。

**Cramér–Rao 下界**（正則條件下）：
$$\text{Var}_\theta(\hat\tau)\ge\frac{[\tau'(\theta)]^2}{nE\left[\left(\partial_\theta\log f(X;\theta)\right)^2\right]}=\frac{[\tau'(\theta)]^2}{-nE\left[\partial_\theta^2\log f(X;\theta)\right]}.$$
估 $\theta$ 本身時分子是 1。

**用法**：不偏估計量的變異數＝下界 ⇒ UMVUE。

**正則條件重點**：參數空間是區間；support 不依賴 $\theta$；微分積分可交換。$U(0,\theta)$ 不適用。

**證明關鍵步驟**

1. $E[\partial_\theta\log f(X;\theta)]=0$（$\int\partial_\theta f=0$）。
2. $\tau'(\theta)=\int(T-\tau)\partial_\theta f(\mathbf x;\theta)$（多減 $\tau\cdot\partial_\theta\int f=0$）。
3. $\partial_\theta f(\mathbf x;\theta)=\left[\sum_j\partial_\theta\log f(x_j;\theta)\right]f(\mathbf x;\theta)$。
4. Cauchy–Schwarz：$[E(XY)]^2\le E(X^2)E(Y^2)$。
5. 交叉項期望值為 0（獨立＋第 1 步）⇒ 分母是 $n$ 倍。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Cramér–Rao 下界 | 下一集：用它驗證 UMVUE 的例子 |
| 另一種找 UMVUE 的方法 | 學期最後：充分統計量、完備性 |
| Fisher 資訊 | 下學期：MLE 的漸近常態性 |

---

## 附：本集一句話總結

> **在正則條件下，$\tau(\theta)$ 的任何不偏估計量的變異數都 $\ge\frac{[\tau'(\theta)]^2}{nE[(\partial_\theta\log f)^2]}$（Cramér–Rao 下界）；證明靠「多減一個 0」「joint pdf 的微分寫成 score 之和」與 Cauchy–Schwarz；找到變異數等於下界的不偏估計量，它就是 UMVUE。**

---

## ⚠️ 待確認清單

1. [▶ 07:15](https://youtu.be/oRcceUnloBk?t=435) 老師說 Cramér「應該是西班牙人」。課本沒有寫兩人的國籍，無法用課本查證。

---

*筆記依據「統計學」Lec19 錄影逐字稿（whisper large-v3-turbo，56:23）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
