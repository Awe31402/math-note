---
course: 統計學（數理統計，數學系）
episode: 16
lecture: Lec16
date: 待補
video: https://youtu.be/TSqYmclIn7Y
notes: Hogg 8th ed. §6.1 MLE；§4.4 順序統計量（p. 253，Theorem 4.4.1 joint pdf；本集只講最大、最小）
---

# 第 16 集 · Lec16：MLE 的兩種情形；順序統計量（最大、最小的 pdf） [▶ 影片](https://youtu.be/TSqYmclIn7Y)

← 上一集：[15](15-method-of-moments-likelihood-mle.md) ｜ [總目錄](../README.md) ｜ 下一集：[17](17-mle-examples-uniform-binomial-normal-invariance.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 16 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（31:18，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.4、§6.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「likelihood function」→「LIGRIE FUNCTION／Lugly Function」，「order statistic」照錄（中文「順序統計量」聽成「瞬息統計量」），「遞增／遞減」→「地增／地減」，「monotone」照錄。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 找 MLE 的兩種情形](#1-找-mle-的兩種情形)
- [2. 順序統計量](#2-順序統計量)
- [3. 獨立事件同時發生的機率](#3-獨立事件同時發生的機率)
- [4. 定理：最大、最小順序統計量的 pdf](#4-定理最大最小順序統計量的-pdf)
- [5. 證明：最大 Yₙ](#5-證明最大-yₙ)
- [6. 證明：最小 Y₁](#6-證明最小-y₁)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 找 MLE：可微有內部最大值 vs 單調（最大值在端點） | §6.1 |
| 順序統計量 $Y_1<\cdots<Y_n$ | §4.4，p. 253 |
| $Y_n=\max$、$Y_1=\min$ 的 pdf | §4.4 |

---

## 1. 找 MLE 的兩種情形

[▶ 00:00](https://youtu.be/TSqYmclIn7Y?t=0) 複習：概似函數 $L(\theta;x_1,\dots,x_n)$ 就是 joint pdf，只是看成 $\theta$ 的函數。每給一組 $x_1,\dots,x_n$，就有一個 $\theta$ 讓它最大；把 $x_i$ 換大寫就是 MLE。

[▶ 01:33](https://youtu.be/TSqYmclIn7Y?t=93) 怎麼找最大值？一般兩種情形：

**情形 1：有內部最高點**（曲線先升後降）

- 最高點就是 $\hat\theta$。
- 取 $\log L$（最高點位置不變），**微分令它等於 0**，解出 $\hat\theta$。

**情形 2：$L$ 是單調的**（monotone，[▶ 02:34](https://youtu.be/TSqYmclIn7Y?t=154)）

- $\theta$ 有範圍（有端點）。
- $L$ 遞增 → 最大值在**右端點**；$L$ 遞減 → 最大值在**左端點**。
- 這時微分等於 0 解不出來，MLE 是某個端點。

例子下次講。這種情形常會用到**順序統計量**，所以先介紹它。

---

## 2. 順序統計量

[▶ 03:35](https://youtu.be/TSqYmclIn7Y?t=215)

- 統計量：隨機樣本的函數、不含參數。統計量是隨機變數，有分配，要找它的分配。
- [▶ 04:05](https://youtu.be/TSqYmclIn7Y?t=245) 本集的公式**只對連續分配成立**。

設 $X_1,\dots,X_n$ 是隨機樣本，來自**連續**分配，pdf $f(x;\theta)$。

> **定義（順序統計量，order statistics）**（[▶ 05:08](https://youtu.be/TSqYmclIn7Y?t=308)）：把 $X_1,\dots,X_n$ **由小排到大**，記作
> $$Y_1<Y_2<\cdots<Y_n.$$
> $Y_1$ 最小，$Y_2$ 第二小，……，$Y_n$ 最大。

- $Y_1=\min(X_1,\dots,X_n)$：最小的順序統計量。
- $Y_n=\max(X_1,\dots,X_n)$：最大的順序統計量。

[▶ 06:11](https://youtu.be/TSqYmclIn7Y?t=371) **例**：觀察到 7 個點，$X_6$ 最小、$X_2$ 第二小、$X_7$ 第三小……那 $Y_1=X_6$、$Y_2=X_2$、$Y_3=X_7$、……。

- 下一次抽，誰最小不一定。
- 隨機樣本同分配（pdf 都一樣），所以**每個 $X_i$ 成為最小、第二小、……、最大的機會都一樣**。

目前最有興趣的是 $Y_1$ 和 $Y_n$ 的分配。

---

## 3. 獨立事件同時發生的機率

[▶ 08:43](https://youtu.be/TSqYmclIn7Y?t=523) $X_1,\dots,X_n$ 獨立，$A_1,\dots,A_n$ 是集合：

$$P(X_1\in A_1,\dots,X_n\in A_n)=\prod_{i=1}^nP(X_i\in A_i).$$

**證明**：

1. 左邊＝joint pdf 在 $A_1\times\cdots\times A_n$ 上積分。
2. [▶ 09:44](https://youtu.be/TSqYmclIn7Y?t=584) 獨立 ⇒ joint pdf＝$\prod f(x_i;\theta)$（同分配，都寫同一個 $f$）。
3. 被積函數可分離，$n$ 重積分拆成 $n$ 個積分相乘：
$$\int_{A_1}f(x_1;\theta)\,dx_1\cdots\int_{A_n}f(x_n;\theta)\,dx_n=P(X_1\in A_1)\cdots P(X_n\in A_n).$$

---

## 4. 定理：最大、最小順序統計量的 pdf

[▶ 11:47](https://youtu.be/TSqYmclIn7Y?t=707)

令 $F(x;\theta)=P(X\le x)$ 是 $X$ 的**分配函數**（cdf），$f(x;\theta)$ 是 pdf。

> **定理**：$X_1,\dots,X_n$ 是來自連續分配的隨機樣本，則
> $$f_{Y_n}(y)=n\left[F(y;\theta)\right]^{n-1}f(y;\theta),$$
> $$f_{Y_1}(y)=n\left[1-F(y;\theta)\right]^{n-1}f(y;\theta).$$

[▶ 13:51](https://youtu.be/TSqYmclIn7Y?t=831) 【口頭】現在叫你背你不會背。但證明過一次就會背了。

---

## 5. 證明：最大 Yₙ

[▶ 14:25](https://youtu.be/TSqYmclIn7Y?t=865) 這是一個變數轉換，有很多證法。用最簡單的：**分配函數法**。$X_i$ 連續 ⇒ $Y_n$ 連續 ⇒ 分配函數微分就是 pdf。

**Step 1：事件相等**（[▶ 15:58](https://youtu.be/TSqYmclIn7Y?t=958)）

$$\{\max(X_1,\dots,X_n)\le y\}=\{X_1\le y,\ X_2\le y,\ \dots,\ X_n\le y\}.$$

- 最大的都 $\le y$ ⇒ 每個都 $\le y$。
- 每個都 $\le y$ ⇒ 最大的也 $\le y$。

[▶ 17:32](https://youtu.be/TSqYmclIn7Y?t=1052) 兩個事件（樣本點的集合）一模一樣，機率相同。

**Step 2：用獨立**（[▶ 18:36](https://youtu.be/TSqYmclIn7Y?t=1116)）

$$F_{Y_n}(y)=P(Y_n\le y)=P(X_1\le y)P(X_2\le y)\cdots P(X_n\le y).$$

**Step 3：用同分配**（[▶ 19:38](https://youtu.be/TSqYmclIn7Y?t=1178)）。每個 $P(X_i\le y)=\int_{-\infty}^yf(x;\theta)\,dx=F(y;\theta)$，一共 $n$ 個：

$$F_{Y_n}(y)=\left[F(y;\theta)\right]^n.$$

（符號：$F_{Y_n}$ 是 $Y_n$ 的分配函數；$F$ 是 $X$ 的分配函數。）

**Step 4：微分**（[▶ 21:41](https://youtu.be/TSqYmclIn7Y?t=1301)）。連鎖律；$X$ 連續 ⇒ $F'=f$：

$$f_{Y_n}(y)=n\left[F(y;\theta)\right]^{n-1}F'(y;\theta)=n\left[F(y;\theta)\right]^{n-1}f(y;\theta).\qquad\blacksquare$$

---

## 6. 證明：最小 Y₁

[▶ 23:45](https://youtu.be/TSqYmclIn7Y?t=1425)

**Step 1：最小的不能直接拆**（[▶ 24:45](https://youtu.be/TSqYmclIn7Y?t=1485)）。$\min\le y$ **不**等於「每個都 $\le y$」。改用補集合：

$$F_{Y_1}(y)=P(\min\le y)=1-P(\min>y).$$

**Step 2：事件相等**（[▶ 25:15](https://youtu.be/TSqYmclIn7Y?t=1515)）

$$\{\min(X_1,\dots,X_n)>y\}=\{X_1>y,\ \dots,\ X_n>y\}.$$

- 最小的都比 $y$ 大 ⇒ 每個都比 $y$ 大。
- 每個都比 $y$ 大 ⇒ 最小的也比 $y$ 大。

（連續型，$>$ 還是 $\ge$ 沒差。）

**Step 3：獨立、同分配**（[▶ 27:20](https://youtu.be/TSqYmclIn7Y?t=1640)）

$$P(\min>y)=\prod_{i=1}^nP(X_i>y)=\prod_{i=1}^n\left[1-P(X_i\le y)\right]=\left[1-F(y;\theta)\right]^n.$$

所以
$$F_{Y_1}(y)=1-\left[1-F(y;\theta)\right]^n.$$

**Step 4：微分**（[▶ 29:20](https://youtu.be/TSqYmclIn7Y?t=1760)）：

$$f_{Y_1}(y)=-n\left[1-F(y;\theta)\right]^{n-1}\cdot\left(-f(y;\theta)\right)=n\left[1-F(y;\theta)\right]^{n-1}f(y;\theta).\qquad\blacksquare$$

（負負得正。）

[▶ 30:20](https://youtu.be/TSqYmclIn7Y?t=1820) **差別**：$Y_1$ 用 $1-F$，$Y_n$ 用 $F$；後面都乘 $f$，裡面都放 $y$。

【口頭】這兩個公式一定要記得，但要自己證一遍才記得。抄起來背會背錯。

---

## 7. 一頁速查表

**找 MLE**

| $L(\theta)$ 的形狀 | 做法 |
|---|---|
| 有內部最高點 | 解 $\frac{d}{d\theta}\log L=0$ |
| 單調 | 最大值在 $\theta$ 範圍的端點 |

**獨立**：$P(X_1\in A_1,\dots,X_n\in A_n)=\prod P(X_i\in A_i)$。

**順序統計量**（連續、iid，$F$ 是 cdf、$f$ 是 pdf）

| | cdf | pdf | 關鍵一步 |
|---|---|---|---|
| $Y_n=\max$ | $F(y)^n$ | $nF(y)^{n-1}f(y)$ | $\max\le y\iff$ 每個 $\le y$ |
| $Y_1=\min$ | $1-[1-F(y)]^n$ | $n[1-F(y)]^{n-1}f(y)$ | $\min>y\iff$ 每個 $>y$ |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| MLE 情形 2（端點） | 下一集：均勻分配 $U(0,\theta)$ 的 MLE 是 $Y_n$ |
| $Y_n$、$Y_1$ 的 pdf | 求 MLE 的期望值、判斷不偏 |
| 一般順序統計量 | 課本 §4.4：第 $k$ 個順序統計量、joint pdf |

---

## 附：本集一句話總結

> **MLE 若有內部最高點就解 $\frac{d}{d\theta}\log L=0$，若 $L$ 單調就取端點；把樣本由小排到大得順序統計量，利用「max ≤ y ⇔ 每個 ≤ y」「min > y ⇔ 每個 > y」加上獨立同分配，得 $f_{Y_n}=nF^{n-1}f$、$f_{Y_1}=n(1-F)^{n-1}f$。**

---

*筆記依據「統計學」Lec16 錄影逐字稿（whisper large-v3-turbo，31:18）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
