---
course: 統計學（數理統計，數學系）
episode: 18
lecture: Lec18
date: 待補
video: https://youtu.be/nEzeFNHewSY
notes: Hogg 8th ed. Theorem 6.1.2 MLE 不變性（p. 358）；§7.1 估計量的品質、MVUE（Definition 7.1.1，p. 413）
---

# 第 18 集 · Lec18：不變性定理的例子；什麼是「最好的」估計量：UMVUE [▶ 影片](https://youtu.be/nEzeFNHewSY)

← 上一集：[17](17-mle-examples-uniform-binomial-normal-invariance.md) ｜ [總目錄](../README.md) ｜ 下一集：[19](19-umvue-cramer-rao-lower-bound.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 18 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（33:55，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §6.1、§7.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 來源說法不一致，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「$\tau(\theta)$」→「tall／tow of theta」，「二項」→「偶像」，「method of moments」→「Metal Moment／Mesomoment」，「variance」→「valence」，「UMVUE」照錄。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 不變性定理：複習與例子](#1-不變性定理複習與例子)
- [2. 回顧：動差法 vs MLE](#2-回顧動差法-vs-mle)
- [3. 估計量的期望值和變異數都跟 θ 有關](#3-估計量的期望值和變異數都跟-θ-有關)
- [4. 「第一名」的兩種意思](#4-第一名的兩種意思)
- [5. 在一個 θ₀ 變異數最小](#5-在一個-θ₀-變異數最小)
- [6. UMVUE](#6-umvue)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 不變性定理的例子：$p^2$、$\sqrt p$、$e^p$、$\sigma$ | Theorem 6.1.2，p. 358 |
| 找「最好的」估計量：UMVUE 的定義 | §7.1，Definition 7.1.1，p. 413 |

---

## 1. 不變性定理：複習與例子

[▶ 00:00](https://youtu.be/nEzeFNHewSY?t=0) 若 $\hat\theta$ 是 $\theta$ 的 MLE、$\tau$ 一對一，則 $\widehat{\tau(\theta)}=\tau(\hat\theta)$。

[▶ 01:31](https://youtu.be/nEzeFNHewSY?t=91) 本來要找 $\tau(\theta)$ 的 MLE：把概似函數裡的 $\theta$ 寫成 $\tau^{-1}(\tau(\theta))$，**對 $\tau(\theta)$ 微分**（不是對 $\theta$）令它等於 0。定理說不用那麼麻煩：直接把 $\theta$ 換成 $\hat\theta$。

**例：二項**（[▶ 03:33](https://youtu.be/nEzeFNHewSY?t=213)），$Y\sim b(n,p)$，$\hat p=Y/n$。

- 參數空間：$p$ 是成功機率，$0<p<1$。
- 在 $(0,1)$ 上，下面這些都是一對一：

| $\tau(p)$ | 一對一？ | MLE |
|---|---|---|
| $p^2$ | ✓（$p>0$，開根號回去） | $(Y/n)^2$ |
| $\sqrt p$ | ✓ | $\sqrt{Y/n}$ |
| $e^p$ | ✓ | $e^{Y/n}$ |
| $p(1-p)$ | ✗ | 老師說：直接代 $\frac Yn(1-\frac Yn)$ 可以拿來估計，但**不是** MLE |

⚠️ 待確認：[▶ 05:36](https://youtu.be/nEzeFNHewSY?t=336) 老師說 $p(1-p)$ 不是一對一，所以 $\hat p(1-\hat p)$ 不是 MLE。課本 Theorem 6.1.2（p. 358）的不變性**不要求一對一**：對任何函數 $g$，$g(\hat\theta)$ 都是 $g(\theta)$ 的 MLE（用誘導概似函數定義）。兩者對 MLE 的定義不同，照課本的定義 $\hat p(1-\hat p)$ 是 MLE。

**例：常態**（[▶ 06:06](https://youtu.be/nEzeFNHewSY?t=366)），$\hat\mu=\bar X$，$\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2$。

- 常想估的是 $\sigma$，不是 $\sigma^2$。
- $\sigma>0$，所以 $(\mu,\sigma^2)\mapsto(\mu,\sigma)$ 是一對一。
- MLE：$\hat\mu=\bar X$，$\hat\sigma=\sqrt{\hat\sigma^2}=\sqrt{\frac1n\sum(X_i-\bar X)^2}$。
- [▶ 07:40](https://youtu.be/nEzeFNHewSY?t=460) 本來要對 $\mu$ 和 $\sigma$（不是 $\sigma^2$）偏微分令 0 解聯立，解出來會一樣。一對一函數那麼多，不可能每個都微分，直接套就好。

---

## 2. 回顧：動差法 vs MLE

[▶ 08:42](https://youtu.be/nEzeFNHewSY?t=522)

| | 動差法 | MLE |
|---|---|---|
| 想法 | 母體動差＝樣本動差，解聯立 | 讓概似函數最大 |
| 用到分配？ | **沒有**（只用動差） | **有**（概似函數＝joint pdf） |
| 理論 | 比較弱 | 通常比較好 |

[▶ 11:20](https://youtu.be/nEzeFNHewSY?t=680) 【口頭】但兩者都只是「找估計量的方法」，**不保證**找到的是最好的。

[▶ 11:51](https://youtu.be/nEzeFNHewSY?t=711) 接下來要找**最好的**估計量。先要說清楚什麼叫「最好」。

- 不偏、一致都是好的觀念，但不偏估計量、一致估計量都**很多**。怎麼從很多裡面挑最好的？

---

## 3. 估計量的期望值和變異數都跟 θ 有關

[▶ 12:53](https://youtu.be/nEzeFNHewSY?t=773) 設 $X_1,\dots,X_n$ 來自 $f(x;\theta)$，$\theta\in\Omega$；$\hat\theta=\hat\theta(X_1,\dots,X_n)$ 是估計量（不含參數的統計量）。

**期望值**（[▶ 14:23](https://youtu.be/nEzeFNHewSY?t=863)）：
$$E_\theta(\hat\theta)=\int\!\cdots\!\int\hat\theta(x_1,\dots,x_n)f(x_1,\dots,x_n;\theta)\,dx_1\cdots dx_n.$$
joint pdf 裡有 $\theta$，所以結果是 $\theta$ 的函數。下標 $\theta$：「當 $\theta$ 是真正的值」。

- 不偏 ⇔ $E_\theta(\hat\theta)=\theta$。
- [▶ 16:26](https://youtu.be/nEzeFNHewSY?t=986) 畫圖：若 $\theta_1$ 是對的，$\hat\theta$ 的 pdf 以 $\theta_1$ 為中心；若 $\theta_2$ 是對的，就以 $\theta_2$ 為中心……不知道哪個對，分配就跟著移。

**變異數**（[▶ 18:29](https://youtu.be/nEzeFNHewSY?t=1109)）：設 $\hat\theta$ 不偏，
$$\text{Var}_\theta(\hat\theta)=E_\theta\left[(\hat\theta-\theta)^2\right]=\int\!\cdots\!\int\left(\hat\theta(\mathbf x)-\theta\right)^2f(\mathbf x;\theta)\,d\mathbf x,$$
也是 $\theta$ 的函數。

【口頭】一定要記得變異數的定義：隨機變數減掉它的期望值、平方、再取期望值。

---

## 4. 「第一名」的兩種意思

[▶ 21:31](https://youtu.be/nEzeFNHewSY?t=1291) 【口頭】UMVUE 這個觀念要花一段時間慢慢感受。

- **鋼琴比賽第一名**（[▶ 22:02](https://youtu.be/nEzeFNHewSY?t=1322)）：20 人表演，打成績，最高的就是第一，沒爭議。
- **班上第一名**（[▶ 22:33](https://youtu.be/nEzeFNHewSY?t=1353)）：每人修的課不同，成績乘學分、加起來、除以總學分，算**平均**，平均最高的是第一。大家都接受。
- **另一種第一名**（[▶ 23:35](https://youtu.be/nEzeFNHewSY?t=1415)）：全班 50 人都修同樣 5 門課（微積分、代數、高微……），每門課各有一個第一名。有沒有可能這 5 門的第一名**是同一個人**？通常沒有。如果有，這個人叫 **uniform 的第一名**：不是平均第一，而是**每一門都第一**。這種第一常常不存在。

---

## 5. 在一個 θ₀ 變異數最小

[▶ 25:11](https://youtu.be/nEzeFNHewSY?t=1511) 先把 $\theta$ 固定成 $\theta_0$。

> 若 $\hat\theta$ 不偏，且對**任何**不偏估計量 $\hat\theta^*$，
> $$\text{Var}_{\theta_0}(\hat\theta)\le\text{Var}_{\theta_0}(\hat\theta^*),$$
> 就說 $\hat\theta$ 在 $\theta_0$ 是 **minimum variance**（變異數最小）。

- [▶ 26:44](https://youtu.be/nEzeFNHewSY?t=1604) 跟誰比？跟**所有不偏估計量**比。（就像「應數系三年級第一名」，要說清楚是跟全班比。）
- 「minimum variance」：變異數最小；「unbiased estimator」：在不偏估計量裡面。
- [▶ 29:20](https://youtu.be/nEzeFNHewSY?t=1760) 如果知道 $\theta_0$ 是對的，當然選它。問題是**不知道** $\theta_0$ 是不是對的；換一個 $\theta_1$，最小的可能是另一個估計量。

---

## 6. UMVUE

[▶ 29:51](https://youtu.be/nEzeFNHewSY?t=1791)

> **定義（UMVUE，uniformly minimum variance unbiased estimator）**：不偏估計量 $\hat\theta$ 若對**任何**不偏估計量 $\hat\theta^*$ 都有
> $$\text{Var}_\theta(\hat\theta)\le\text{Var}_\theta(\hat\theta^*),\qquad\textbf{對所有 }\theta\in\Omega,$$
> 就叫 $\theta$ 的 UMVUE（一致最小變異不偏估計量）。

**每個字的意思**（[▶ 32:25](https://youtu.be/nEzeFNHewSY?t=1945)）：

| 字 | 意思 |
|---|---|
| U（uniformly） | **不管哪個 $\theta$ 是對的**都最小（「對所有 $\theta$」那句話） |
| MV（minimum variance） | 變異數最小 |
| UE（unbiased estimator） | 跟**所有不偏估計量**比 |

- 就是「每一門課都第一名」的那種第一。
- [▶ 31:55](https://youtu.be/nEzeFNHewSY?t=1915) 每個固定的 $\theta$，變異數最小的通常存在（變異數 $\ge 0$）；但「每個 $\theta$ 的最小都是同一個估計量」就不一定存在。
- 在估計問題裡，很多情形 UMVUE 是存在的。之後要學怎麼找。

【課本補充】課本 Definition 7.1.1（p. 413）把它叫 **MVUE**（minimum variance unbiased estimator），定義裡就要求對所有 $\theta\in\Omega$ 成立，相當於老師的 UMVUE。

---

## 7. 一頁速查表

**不變性定理的用法**：$\tau$ 一對一 ⇒ $\widehat{\tau(\theta)}=\tau(\hat\theta)$。

| 例 | MLE |
|---|---|
| $b(n,p)$：$p^2$、$\sqrt p$、$e^p$ | $(Y/n)^2$、$\sqrt{Y/n}$、$e^{Y/n}$ |
| $N(\mu,\sigma^2)$：$\sigma$ | $\sqrt{\frac1n\sum(X_i-\bar X)^2}$ |

**估計量的 mean、variance 都是 $\theta$ 的函數**（因為 joint pdf 含 $\theta$）。

**UMVUE**：不偏，且
$$\text{Var}_\theta(\hat\theta)\le\text{Var}_\theta(\hat\theta^*)\quad\forall\text{ 不偏 }\hat\theta^*,\ \forall\theta\in\Omega.$$
U＝每個 $\theta$ 都最小（每門課都第一）；MV＝變異數最小；UE＝在不偏估計量裡比。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| UMVUE | 下一集起：怎麼找 UMVUE（Cramér–Rao 下界、充分統計量） |
| 動差法 vs MLE | 比較估計量效率 |

---

## 附：本集一句話總結

> **一對一變換下 MLE 直接代入（$p^2$、$\sqrt p$、$\sigma$）；動差法與 MLE 只是找估計量的方法，不保證最好；「最好」定義為 UMVUE：在所有不偏估計量裡，不管哪個 $\theta$ 是對的，它的變異數都最小。**

---

## ⚠️ 待確認清單

1. [▶ 05:36](https://youtu.be/nEzeFNHewSY?t=336) 老師說 $p(1-p)$ 非一對一，所以 $\hat p(1-\hat p)$ 不是 MLE；課本 Theorem 6.1.2 的不變性對任何函數都成立。差別在 MLE 的定義（是否用誘導概似函數）。

---

*筆記依據「統計學」Lec18 錄影逐字稿（whisper large-v3-turbo，33:55）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
