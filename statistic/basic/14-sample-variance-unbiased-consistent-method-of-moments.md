---
course: 統計學（數理統計，數學系）
episode: 14
lecture: Lec14
date: 待補
video: https://youtu.be/X9gS4syIVxc
notes: Hogg 8th ed. §4.1 $S^2$ 不偏（p. 227 附近）；§5.1 $S^2$ 一致（Example，p. 324 附近）、Theorem 5.1.2–5.1.4 依機率收斂的運算（p. 322–323）；動差法（索引 p. 165）
---

# 第 14 集 · Lec14：$S^2$ 是 $\sigma^2$ 的不偏且一致估計量；動差法預告 [▶ 影片](https://youtu.be/X9gS4syIVxc)

← 上一集：[13](13-convergence-in-probability-wlln-consistency.md) ｜ [總目錄](../README.md) ｜ 下一集：[15](15-method-of-moments-likelihood-mle.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 14 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（34:58，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.1、§5.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「iid」→「RID」，「variance」→「valence」，「收斂」→「縮練／縮鏈」，「動差法 method of moments」→「mess or moment／動插法」，「弱大數法則」→「偌大數法則」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：X̄ 是 μ 的好估計量](#1-複習x̄-是-μ-的好估計量)
- [2. 工具：E(X²)＝μ²＋σ²](#2-工具exμσ)
- [3. S² 是 σ² 的不偏估計量](#3-s-是-σ-的不偏估計量)
- [4. 為什麼除以 n−1？](#4-為什麼除以-n1)
- [5. S² 是 σ² 的一致估計量](#5-s-是-σ-的一致估計量)
- [6. 小結與考試範圍](#6-小結與考試範圍)
- [7. 補充：連續函數保持依機率收斂](#7-補充連續函數保持依機率收斂)
- [8. 預告：動差法](#8-預告動差法)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/X9gS4syIVxc?t=0) 統計推論＝估計＋檢定；估計＝點估計＋區間估計。從現在起大部分在講點估計的理論。

設定（[▶ 01:01](https://youtu.be/X9gS4syIVxc?t=61)）：$X_1,\dots,X_n$ 是隨機樣本，來自**某個**分配，mean $\mu$、variance $\sigma^2$。分配是什麼（常態、卡方、Poisson、二項……）**不需要知道**。

| 參數 | 估計量 | 不偏 | 一致 |
|---|---|---|---|
| $\mu$ | $\bar X$ | ✓（上次） | ✓（WLLN，上次） |
| $\sigma^2$ | $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ | **本集** | **本集** |

---

## 1. 複習：X̄ 是 μ 的好估計量

[▶ 02:32](https://youtu.be/X9gS4syIVxc?t=152)

- $\mu$：**母體平均數**（population mean）；$\bar X$：**樣本平均數**（sample mean）。用樣本平均數估母體平均數。
- **不偏**（[▶ 04:35](https://youtu.be/X9gS4syIVxc?t=275)）：$\bar X$ 的分配中心在 $\mu$，觀察值大部分在 $\mu$ 附近，但通常不等於 $\mu$。
- **一致**（[▶ 05:06](https://youtu.be/X9gS4syIVxc?t=306)）：$P(|\bar X-\mu|<\epsilon)\to 1$。$\epsilon$ 很小時，$n$ 夠大，$\bar X$ 和 $\mu$ 幾乎沒差別——不會相等，但可以**無窮接近**。

---

## 2. 工具：E(X²)＝μ²＋σ²

[▶ 06:40](https://youtu.be/X9gS4syIVxc?t=400)

> 任何隨機變數 $X$（mean $\mu$、variance $\sigma^2$）：
> $$E(X^2)=\mu^2+\sigma^2.$$
> 「平方的期望值＝平均數的平方＋變異數。」

**證明**：
$$\sigma^2=E[(X-\mu)^2]=E(X^2)-2\mu E(X)+\mu^2=E(X^2)-\mu^2.$$
（$-2\mu$ 是常數可提出；$\mu^2$ 是常數，期望值是自己。）移項即得。

這就是 Lec04 的 $\sigma^2=E(X^2)-\mu^2$ 換個方向用。

---

## 3. S² 是 σ² 的不偏估計量

[▶ 09:44](https://youtu.be/X9gS4syIVxc?t=584)

> **定理**：$E(S^2)=\sigma^2$。

**Step 1：展開**（[▶ 10:15](https://youtu.be/X9gS4syIVxc?t=615)）
$$\sum(X_i-\bar X)^2=\sum X_i^2-2\bar X\sum X_i+n\bar X^2.$$
因為 $\sum X_i=n\bar X$：
$$=\sum X_i^2-2n\bar X^2+n\bar X^2=\sum X_i^2-n\bar X^2.$$

**Step 2：取期望值**（[▶ 11:45](https://youtu.be/X9gS4syIVxc?t=705)）。和的期望值＝期望值的和；常數提出：
$$E(S^2)=\frac{1}{n-1}\left[\sum E(X_i^2)-nE(\bar X^2)\right].$$

**Step 3：用 §2 的工具兩次**（[▶ 12:15](https://youtu.be/X9gS4syIVxc?t=735)）：

- $X_i$：mean $\mu$、variance $\sigma^2$（iid）⇒ $E(X_i^2)=\mu^2+\sigma^2$。
- [▶ 14:18](https://youtu.be/X9gS4syIVxc?t=858) $\bar X$：mean $\mu$、variance $\frac{\sigma^2}{n}$ ⇒ $E(\bar X^2)=\mu^2+\frac{\sigma^2}{n}$。

  （$\text{Var}(\bar X)=\frac{1}{n^2}\sum\text{Var}(X_i)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}$，用了獨立。）

**Step 4：代入**（[▶ 16:22](https://youtu.be/X9gS4syIVxc?t=982)）：
$$E(S^2)=\frac{1}{n-1}\left[n(\mu^2+\sigma^2)-n\left(\mu^2+\frac{\sigma^2}{n}\right)\right]=\frac{1}{n-1}\left[n\sigma^2-\sigma^2\right]=\sigma^2.\qquad\blacksquare$$

【口頭】[▶ 15:52](https://youtu.be/X9gS4syIVxc?t=952) 技巧就只有「平方的期望值＝平均的平方＋變異數」，分別用在 $X_i$ 和 $\bar X$ 上。

---

## 4. 為什麼除以 n−1？

[▶ 17:22](https://youtu.be/X9gS4syIVxc?t=1042)

另一個候選：$\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2$。

- 直覺上 $n$ 個加起來應該除以 $n$ 才是平均。
- 但它**不偏**：由 §3，$E(\hat\sigma^2)=\frac{n-1}{n}\sigma^2\ne\sigma^2$。
- **除以 $n-1$，期望值才剛好等於 $\sigma^2$**，這是最重要的原因。

【口頭】[▶ 18:22](https://youtu.be/X9gS4syIVxc?t=1102) 你們以後到科學園區的電子公司上班，不只做統計的人，工程師、經理（電子、資工畢業的）也常碰到這個，因為統計對電子生產非常重要。他們常懷疑為什麼除以 $n-1$。跟他說「因為不偏」，他不知道什麼叫不偏——不偏其實不容易懂。

**不偏的意思再講一次**（[▶ 19:52](https://youtu.be/X9gS4syIVxc?t=1192)）：$S^2$ 是隨機變數，有分配，分配中心在 $\sigma^2$。觀察到的 $S^2$ 不會剛好等於 $\sigma^2$，但大部分落在 $\sigma^2$ 附近。

---

## 5. S² 是 σ² 的一致估計量

[▶ 20:22](https://youtu.be/X9gS4syIVxc?t=1222)

> **定理**：$S^2\xrightarrow{P}\sigma^2$。

**Step 1：改寫**（[▶ 21:23](https://youtu.be/X9gS4syIVxc?t=1283)）。由 §3 Step 1：
$$S^2=\frac{1}{n-1}\left[\sum X_i^2-n\bar X^2\right]=\frac{n}{n-1}\cdot\frac1n\sum_{i=1}^nX_i^2-\frac{n}{n-1}\bar X^2.$$

**Step 2：各部分的極限**

- $\frac{n}{n-1}\to 1$（[▶ 23:31](https://youtu.be/X9gS4syIVxc?t=1411)）。
- [▶ 24:01](https://youtu.be/X9gS4syIVxc?t=1441) $\frac1n\sum X_i^2$：$X_1,\dots,X_n$ iid ⇒ $X_1^2,\dots,X_n^2$ 也 iid（獨立的各取函數仍獨立；同分配取同一函數仍同分配），mean $E(X^2)$。由 **WLLN**（假設 $\text{Var}(X^2)<\infty$）：
$$\frac1n\sum X_i^2\xrightarrow{P}E(X^2)=\mu^2+\sigma^2.$$
- [▶ 26:33](https://youtu.be/X9gS4syIVxc?t=1593) $\bar X\xrightarrow{P}\mu$（WLLN），所以 $\bar X^2\xrightarrow{P}\mu^2$（見 §7）。

**Step 3：合起來**（[▶ 27:03](https://youtu.be/X9gS4syIVxc?t=1623)）：
$$S^2\xrightarrow{P}1\cdot(\mu^2+\sigma^2)-1\cdot\mu^2=\sigma^2.\qquad\blacksquare$$

【課本補充】Step 3 用到「依機率收斂的和、積、常數倍還是依機率收斂」（課本 Theorem 5.1.2–5.1.3，p. 322–323）。老師直接用，沒講。

⚠️ 逐字稿缺字：[▶ 27:03](https://youtu.be/X9gS4syIVxc?t=1623) 老師板書寫錯一處，口頭更正為「$\mu^2$ 加上 $\sigma^2$」。

---

## 6. 小結與考試範圍

[▶ 27:34](https://youtu.be/X9gS4syIVxc?t=1654)

隨機樣本 mean $\mu$、variance $\sigma^2$：

| 要估 | 用 | 理由 |
|---|---|---|
| $\mu$ | $\bar X$ | 不偏、一致 |
| $\sigma^2$ | $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ | 不偏、一致 |

- **不偏**：$n$ 有限時不會等於，但分配中心在參數，大部分在它附近。
- **一致**：$n$ 夠大時幾乎等於參數，可能還不相等，但非常接近。

[▶ 29:39](https://youtu.be/X9gS4syIVxc?t=1779) 【口頭】**考試考到這裡**。後面的內容留到期末考。

---

## 7. 補充：連續函數保持依機率收斂

[▶ 30:20](https://youtu.be/X9gS4syIVxc?t=1820) 【口頭】一致性有些地方沒講清楚，下學期（高等統計學）會講得比較清楚。

例：$\bar X\xrightarrow{P}\mu$（WLLN）沒問題；但 $\bar X^2\xrightarrow{P}\mu^2$ 呢？

[▶ 30:56](https://youtu.be/X9gS4syIVxc?t=1856) 會的。有個定理：只要 $g$ 是**連續函數**，$\bar X\xrightarrow{P}\mu$ 就推出 $g(\bar X)\xrightarrow{P}g(\mu)$。有些統計書有證明，以後會講。

【課本補充】課本 Theorem 5.1.4（p. 323）：$X_n\xrightarrow{P}a$ 且 $g$ 在 $a$ 連續 ⇒ $g(X_n)\xrightarrow{P}g(a)$。

---

## 8. 預告：動差法

[▶ 31:28](https://youtu.be/X9gS4syIVxc?t=1888) 要估 $\theta$，需要一個方法告訴你怎麼找估計量。要介紹兩種。

**第一種：動差法**（method of moments，[▶ 31:58](https://youtu.be/X9gS4syIVxc?t=1918)）

- 母體 $k$ 次動差 $E_\theta(X^k)$：是 $\theta$ 的函數，算不出來。
- 樣本 $k$ 次動差 $\frac1n\sum X_i^k$：算得出來，而且依機率收斂到母體動差（上次證的）。$n$ 夠大時兩者幾乎沒差別。
- [▶ 33:02](https://youtu.be/X9gS4syIVxc?t=1982) 所以**令兩者相等**：
$$E_\theta(X^k)=\frac1n\sum_{i=1}^nX_i^k.$$
這是一個以 $\theta$ 為未知數的方程式。解出 $\theta$，就叫**動差法估計量**。
- 「用樣本動差估母體動差。」

下次詳講。

---

## 9. 一頁速查表

**工具**：$E(X^2)=\mu^2+\sigma^2$。

**恆等式**：$\sum(X_i-\bar X)^2=\sum X_i^2-n\bar X^2$。

**$S^2$ 不偏**：
$$E(S^2)=\frac{1}{n-1}\left[n(\mu^2+\sigma^2)-n\left(\mu^2+\frac{\sigma^2}{n}\right)\right]=\sigma^2.$$
關鍵：$E(X_i^2)=\mu^2+\sigma^2$，$E(\bar X^2)=\mu^2+\sigma^2/n$。

除以 $n$ 的版本：$E\left[\frac1n\sum(X_i-\bar X)^2\right]=\frac{n-1}{n}\sigma^2$（偏）。

**$S^2$ 一致**：
$$S^2=\frac{n}{n-1}\cdot\underbrace{\frac1n\sum X_i^2}_{\xrightarrow{P}\mu^2+\sigma^2}-\frac{n}{n-1}\underbrace{\bar X^2}_{\xrightarrow{P}\mu^2}\xrightarrow{P}\sigma^2.$$
關鍵：$X_i^2$ iid 用 WLLN；連續函數保持依機率收斂。

**動差法**：令 $E_\theta(X^k)=\frac1n\sum X_i^k$，解 $\theta$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 動差法 | 下一集 |
| 連續函數保持收斂 | 下學期高等統計學 |
| $\bar X$、$S^2$ 的性質 | 信賴區間、檢定 |

---

## 附：本集一句話總結

> **用「$E(X^2)=\mu^2+\sigma^2$」證明 $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ 的期望值剛好是 $\sigma^2$（所以除以 $n-1$），再用弱大數法則證明 $S^2\xrightarrow{P}\sigma^2$；估 $\mu$ 用 $\bar X$、估 $\sigma^2$ 用 $S^2$，兩者都不偏且一致。**

---

*筆記依據「統計學」Lec14 錄影逐字稿（whisper large-v3-turbo，34:58）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
