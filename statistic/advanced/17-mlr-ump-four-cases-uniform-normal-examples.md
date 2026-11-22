---
course: 高等統計學（數理統計續）
episode: 17
lecture: Lec17（第九週 2/2）
date: 待補
video: https://youtu.be/Itklwv-3Nso
notes: Hogg 8th ed. §8.2 單調概似比與 UMP（Definition 8.2.2、p. 483–484）；順序統計量最大值的 pdf（§4.4）
---

# 第 17 集 · 第九週 (2/2)：MLR 下的 UMP 拒絕域（四種情形）；例：Uniform(0,θ)、N(μ,1) [▶ 影片](https://youtu.be/Itklwv-3Nso)

← 上一集：[16](16-ump-composite-definition-monotone-likelihood-ratio.md) ｜ [總目錄](../README.md) ｜ 下一集：[18](18-likelihood-ratio-test-definition.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 17 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 55 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §8.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「monotone likelihood ratio」→「Monotone Ligratio／Motor Ton Regressio」，「UMP」→「UMB」，「背」→「Bid」，「indicator function」照錄。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：family of densities 與 MLR](#1-複習family-of-densities-與-mlr)
- [2. UMP 的檢定力函數是單調的](#2-ump-的檢定力函數是單調的)
- [3. 四種情形：用直覺判斷拒絕域方向](#3-四種情形用直覺判斷拒絕域方向)
- [4. 例一：Uniform(0,θ)，H₀:θ≤θ₀ vs H₁:θ>θ₀](#4-例一uniform0θh₀θθ₀-vs-h₁θθ₀)
- [5. 例二：N(μ,1)，H₀:μ≥0 vs H₁:μ<0](#5-例二nμ1h₀μ0-vs-h₁μ0)
- [6. 步驟整理與預告](#6-步驟整理與預告)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 單邊假設 ＋ MLR ⇒ UMP | §8.2，p. 483–484 |
| UMP 的 power function 單調、最大在 $\theta_0$ | §8.2 |
| 例：Uniform、Normal | §8.2 |

---

## 1. 複習：family of densities 與 MLR

[▶ 00:32](https://youtu.be/Itklwv-3Nso?t=32) 給一個 $\theta$ 就有一個 pdf $f(x;\theta)$；參數空間每一點都對應一個 density，全部的集合叫 **family of densities**。

**MLR**（[▶ 01:34](https://youtu.be/Itklwv-3Nso?t=94)）：$\theta'<\theta''$，$\frac{L(\theta')}{L(\theta'')}$ 是某統計量 $T$ 的 nondecreasing 或 nonincreasing 函數。

[▶ 02:35](https://youtu.be/Itklwv-3Nso?t=155) 要有 UMP，**兩個條件都要**：

1. 假設是**單邊**的：$H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$，或 $H_0:\theta\ge\theta_0$ vs $H_1:\theta<\theta_0$；
2. family of densities 有 **MLR**。

---

## 2. UMP 的檢定力函數是單調的

[▶ 04:05](https://youtu.be/Itklwv-3Nso?t=245) 理論結果（不證明）：有 MLR 時，UMP 檢定的 power function 是**單調**的。

**$H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$**（[▶ 05:07](https://youtu.be/Itklwv-3Nso?t=307)）：

- $H_0$ 區 power 都 $\le\alpha$；遞增，在 $\theta_0$ **剛好**達到 $\alpha$；
- 過了 $\theta_0$ 繼續增加，$\theta$ 越遠越接近 1。

**$H_0:\theta\ge\theta_0$ vs $H_1:\theta<\theta_0$**（[▶ 08:18](https://youtu.be/Itklwv-3Nso?t=498)）：從左邊接近 1 開始遞減，在 $\theta_0$ 剛好是 $\alpha$，再越來越小。

**用處**（[▶ 07:12](https://youtu.be/Itklwv-3Nso?t=432)）：size $=\sup_{\theta\in\Theta_0}\pi_C(\theta)$ 要剛好 $\alpha$。因為單調，最大值一定在**邊界點 $\theta_0$**，所以只要解
$$P_{\theta_0}(\mathbf X\in C)=\alpha.$$
不用每一點都去找。

---

## 3. 四種情形：用直覺判斷拒絕域方向

[▶ 08:48](https://youtu.be/Itklwv-3Nso?t=528) 兩種假設 × MLR 遞增或遞減 = 四種情形。

【口頭】[▶ 09:18](https://youtu.be/Itklwv-3Nso?t=558) 不要用**背**的，要用**直覺**（intuition）。證明很難，不證，但這個結果很重要。

**直覺**：概似比分子是比較小的 $\theta'$、分母是比較大的 $\theta''$。先判斷分子、分母分別代表 $H_0$ 還是 $H_1$；比值偏向 $H_1$ 時拒絕 $H_0$。

**A：$H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$**（[▶ 11:19](https://youtu.be/Itklwv-3Nso?t=679)）

分子（小 $\theta$）像 $H_0$，分母（大 $\theta$）像 $H_1$ ⇒ 比值**小**時拒絕 $H_0$。

| MLR | 比值小 ⇔ | UMP 拒絕域 |
|---|---|---|
| 比值是 $T$ 的**遞增**函數 | $T$ 小 | $T\le t_0$ |
| 比值是 $T$ 的**遞減**函數 | $T$ 大 | $T\ge t_0$ |

**B：$H_0:\theta\ge\theta_0$ vs $H_1:\theta<\theta_0$**（[▶ 18:30](https://youtu.be/Itklwv-3Nso?t=1110)）

分子（小 $\theta$）像 $H_1$，分母像 $H_0$ ⇒ 比值**大**時拒絕 $H_0$。

| MLR | 比值大 ⇔ | UMP 拒絕域 |
|---|---|---|
| 比值是 $T$ 的**遞增**函數 | $T$ 大 | $T\ge t_0$ |
| 比值是 $T$ 的**遞減**函數 | $T$ 小 | $T\le t_0$ |

四種情形都用 $P_{\theta_0}(\text{拒絕})=\alpha$ 決定 $t_0$。

（遞增是指 nondecreasing，可以有常數段；直覺上就當它遞增。）

---

## 4. 例一：Uniform(0,θ)，H₀:θ≤θ₀ vs H₁:θ>θ₀

[▶ 22:41](https://youtu.be/Itklwv-3Nso?t=1361) $X_1,\dots,X_n$ iid Uniform$(0,\theta)$，$\theta>0$。

**family of densities**（[▶ 23:13](https://youtu.be/Itklwv-3Nso?t=1393)）：$f(x;\theta)=\frac1\theta$，$0<x<\theta$；參數空間 $\Omega=(0,\infty)$。每個 $\theta\in\Omega$ 一個 density。

**假設**：單邊 ✓。接著檢查 MLR。

**概似函數**（[▶ 26:24](https://youtu.be/Itklwv-3Nso?t=1584)）：用指示函數，
$$L(\theta;\mathbf x)=\prod_{i=1}^n\frac1\theta I(0<x_i<\theta)=\frac{1}{\theta^n}I(0<y_n<\theta),\qquad y_n=\max_ix_i.$$

[▶ 28:28](https://youtu.be/Itklwv-3Nso?t=1708) 為什麼可以換成 $y_n$：每一個都在 $(0,\theta)$ ⇔ 最大的在 $(0,\theta)$。（所有 $x_i>0$ 是樣本空間本來就滿足的。）

**概似比**（[▶ 29:32](https://youtu.be/Itklwv-3Nso?t=1772)）：$\theta'<\theta''$，
$$\frac{L(\theta')}{L(\theta'')}=\left(\frac{\theta''}{\theta'}\right)^n\frac{I(0<y_n<\theta')}{I(0<y_n<\theta'')}=\begin{cases}\left(\frac{\theta''}{\theta'}\right)^n>0,&0<y_n<\theta',\\[2pt]0,&\theta'\le y_n<\theta''.\end{cases}$$

[▶ 32:09](https://youtu.be/Itklwv-3Nso?t=1929) 是 $y_n$ 的函數，從正的常數降到 0 ⇒ **nonincreasing in $y_n$**。有 MLR ⇒ UMP 一定存在。

**方向**（[▶ 34:42](https://youtu.be/Itklwv-3Nso?t=2082)）：情形 A（$H_0$ 小）、比值遞減 ⇒ 比值小 ⇔ $y_n$ 大：
$$C=\{y_n\ge c\}.$$

**找 $c$**（[▶ 37:15](https://youtu.be/Itklwv-3Nso?t=2235)）：需要 $Y_n$ 的 pdf（最大順序統計量）：
$$g_n(y)=n[F(y)]^{n-1}f(y),\qquad F(x)=\int_0^x\frac1\theta\,dt=\frac x\theta,$$
$$g_n(y)=n\left(\frac y\theta\right)^{n-1}\frac1\theta=\frac{ny^{n-1}}{\theta^n},\qquad 0<y<\theta.$$

[▶ 38:47](https://youtu.be/Itklwv-3Nso?t=2327) 邊界點 $\theta=\theta_0$：
$$\alpha=P_{\theta_0}(Y_n\ge c)=\int_c^{\theta_0}\frac{ny^{n-1}}{\theta_0^n}\,dy=1-\left(\frac{c}{\theta_0}\right)^n\ \Rightarrow\ c=\theta_0(1-\alpha)^{1/n}.$$

> **UMP 拒絕域**（[▶ 39:50](https://youtu.be/Itklwv-3Nso?t=2390)）：$C=\left\{y_n\ge\theta_0(1-\alpha)^{1/n}\right\}$。

【口頭】[▶ 40:21](https://youtu.be/Itklwv-3Nso?t=2421) 整個過程沒有去想定理怎麼寫——四種情形不可能用背的，每一題都要判斷一次。步驟：density → 概似函數 → 概似比是不是某統計量的單調函數 → 單邊 ＋ MLR 就有 UMP → 找邊界點。這種題目做幾遍就會了解。

---

## 5. 例二：N(μ,1)，H₀:μ≥0 vs H₁:μ<0

[▶ 41:23](https://youtu.be/Itklwv-3Nso?t=2483) $X_1,\dots,X_n$ iid $N(\mu,1)$，參數空間 $(-\infty,\infty)$。
$$H_0:\mu\ge 0\quad\text{vs}\quad H_1:\mu<0\ \ (\text{單邊}).$$

**概似比**（[▶ 43:25](https://youtu.be/Itklwv-3Nso?t=2605)）：$\mu_1<\mu_2$。（$H_0$ 是 $\mu$ 大，所以分母 $\mu_2$ 像 $H_0$、分子 $\mu_1$ 像 $H_1$。）
$$\frac{L(\mu_1)}{L(\mu_2)}=\frac{(2\pi)^{-n/2}\exp\left\{-\frac12\sum(x_i-\mu_1)^2\right\}}{(2\pi)^{-n/2}\exp\left\{-\frac12\sum(x_i-\mu_2)^2\right\}}=\exp\left\{-(\mu_2-\mu_1)\sum x_i+\frac n2(\mu_2^2-\mu_1^2)\right\}.$$

[▶ 46:28](https://youtu.be/Itklwv-3Nso?t=2788) 後面是常數。$\mu_2-\mu_1>0$，前面有負號 ⇒ $\sum x_i$ 的**遞減**函數 ⇒ 有 MLR（in $\sum x_i$）⇒ UMP 存在。

**方向**（[▶ 47:58](https://youtu.be/Itklwv-3Nso?t=2878)）：情形 B（分子像 $H_1$），比值大才拒絕；遞減 ⇒ $\sum x_i$ 小：
$$C=\left\{\sum x_i\le c\right\}.$$

**找 $c$**（[▶ 49:01](https://youtu.be/Itklwv-3Nso?t=2941)）：$\sum X_i\sim N(n\mu,n)$。邊界點 $\mu=0$：$\frac{\sum X_i}{\sqrt n}\sim N(0,1)$，
$$\alpha=P_{\mu=0}\left(\sum X_i\le c\right)=P\left(Z\le\frac{c}{\sqrt n}\right)\ \Rightarrow\ \frac{c}{\sqrt n}=-z_\alpha.$$
（標準常態對稱於 0：右尾 $\alpha$ 的點是 $z_\alpha$，左尾 $\alpha$ 的點是 $-z_\alpha$。）

> **UMP 拒絕域**（[▶ 51:03](https://youtu.be/Itklwv-3Nso?t=3063)）：
> $$C=\left\{\sum x_i\le-\sqrt n\,z_\alpha\right\}=\left\{\bar x\le-\frac{z_\alpha}{\sqrt n}\right\}.$$

---

## 6. 步驟整理與預告

[▶ 52:07](https://youtu.be/Itklwv-3Nso?t=3127)

1. 假設必須是**單邊**；不是就不用做了（一般不存在）。
2. 概似比（分子小 $\theta$、分母大 $\theta$）是不是某統計量的**單調**函數。
3. 判斷分子代表 $H_0$ 還是 $H_1$，決定 $T$ 取大還是取小。
4. 在邊界點 $\theta_0$ 解臨界值。

[▶ 53:39](https://youtu.be/Itklwv-3Nso?t=3219) UMP 講到這裡，會給題目自己練習。順序：MP（簡單對簡單）→ UMP（$H_0$ 一點、$H_1$ 集合，由定義直接找）→ UMP（兩邊都是單邊複合，靠 MLR）。

[▶ 54:11](https://youtu.be/Itklwv-3Nso?t=3251) 很多情形沒有 UMP，就用**概似比檢定**：還是用概似函數的比，但在 $H_0$ 上找概似函數最大的、分母也找最大的去比。不保證是最好的，就是一個方法。

---

## 7. 一頁速查表

**UMP 存在條件**：單邊假設 ＋ MLR。power function 單調 ⇒ size 在 $\theta_0$ 達到 ⇒ 解 $P_{\theta_0}(C)=\alpha$。

**四種情形**（比值 $=L(\theta')/L(\theta'')$，$\theta'<\theta''$）

| 假設 | 比值遞增 in $T$ | 比值遞減 in $T$ |
|---|---|---|
| $H_0:\theta\le\theta_0$ vs $\theta>\theta_0$ | $T\le t_0$ | $T\ge t_0$ |
| $H_0:\theta\ge\theta_0$ vs $\theta<\theta_0$ | $T\ge t_0$ | $T\le t_0$ |

記法（直覺）：分母是大 $\theta$；$H_1$ 在大的那邊時，比值小就拒絕；$H_1$ 在小的那邊時，比值大就拒絕。

**例**

| 分配 | 假設 | MLR | UMP 拒絕域 |
|---|---|---|---|
| Uniform$(0,\theta)$ | $\theta\le\theta_0$ vs $>$ | 遞減 in $y_n=\max x_i$ | $y_n\ge\theta_0(1-\alpha)^{1/n}$ |
| $N(\mu,1)$ | $\mu\ge 0$ vs $<$ | 遞減 in $\sum x_i$ | $\bar x\le-z_\alpha/\sqrt n$ |

關鍵：$Y_n$ 的 pdf $g_n(y)=n[F(y)]^{n-1}f(y)$；Uniform 時 $P_{\theta_0}(Y_n\ge c)=1-(c/\theta_0)^n$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 沒有 UMP 時 | 下一集：概似比檢定（likelihood ratio test） |
| 順序統計量的 pdf | 第 1–3 集 |

---

## 附：本集一句話總結

> **單邊假設加上單調概似比就保證有 UMP 檢定，而且它的檢定力函數單調、size 在邊界點 $\theta_0$ 達到；判斷分子（小 $\theta$）代表 $H_0$ 還是 $H_1$、比值隨 $T$ 遞增還遞減，就知道拒絕域是 $T\ge t_0$ 還是 $T\le t_0$——Uniform 得 $y_n\ge\theta_0(1-\alpha)^{1/n}$，$N(\mu,1)$ 的 $H_0:\mu\ge 0$ 得 $\bar x\le-z_\alpha/\sqrt n$。**

---

*筆記依據「高等統計學」Lec17 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
