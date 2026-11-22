---
course: 高等統計學（數理統計續）
episode: 19
lecture: Lec19（第十週 2/2）
date: 待補
video: https://youtu.be/Y_niPLoiQtg
notes: Hogg 8th ed. §8.3 概似比檢定；§8.3.1 常態平均數的 LRT（p. 488 起）；Gamma 與 χ² 的關係（§3.3）
---

# 第 19 集 · 第十週 (2/2)：概似比檢定例題——指數分配單邊、常態平均數雙邊（變異數已知／未知） [▶ 影片](https://youtu.be/Y_niPLoiQtg)

← 上一集：[18](18-likelihood-ratio-test-definition.md) ｜ [總目錄](../README.md) ｜ 下一集：[20](20-lrt-to-t-test-f-distribution.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 19 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 47 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §3.3、§8.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「exponential」→「Explonential」，「Gamma」→「伽瑪」，「$\chi^2$」→「卡荒／卡方」，「MLE」→「ML1／mlo1」，「general(ized) likelihood ratio」→「General Lig Ratio」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例一：指數分配，H₀:θ≤θ₀ vs H₁:θ>θ₀](#1-例一指數分配h₀θθ₀-vs-h₁θθ₀)
  - [1.1 兩個最大概似值](#11-兩個最大概似值)
  - [1.2 Λ 是 x̄ 的遞增函數](#12-λ-是-x-的遞增函數)
  - [1.3 用 Gamma→χ² 找臨界值](#13-用-gammaχ²-找臨界值)
- [2. 例二：N(θ,1)，H₀:θ=0 vs H₁:θ≠0](#2-例二nθ1h₀θ0-vs-h₁θ0)
- [3. 例三：N(θ₁,θ₂) 兩參數都未知，H₀:θ₁=0](#3-例三nθ₁θ₂-兩參數都未知h₀θ₁0)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:33](https://youtu.be/Y_niPLoiQtg?t=33) LRT：分子是 $H_0$ 上的最大概似值，分母是整個參數空間的最大（代 MLE）。$\Lambda$ 小就拒絕。問題是 $\Lambda$ 的分配很難，要判斷 $\Lambda$ 是不是某統計量的**遞增或遞減**函數。

| 例 | 假設 | 課本 |
|---|---|---|
| 指數 $\theta e^{-\theta x}$ | $\theta\le\theta_0$ vs $\theta>\theta_0$ | §8.3 |
| $N(\theta,1)$ | $\theta=0$ vs $\theta\ne 0$ | §8.3.1 |
| $N(\theta_1,\theta_2)$ | $\theta_1=0$ vs $\theta_1\ne 0$ | §8.3.1，p. 488 起 |

---

## 1. 例一：指數分配，H₀:θ≤θ₀ vs H₁:θ>θ₀

[▶ 02:06](https://youtu.be/Y_niPLoiQtg?t=126) $X_1,\dots,X_n$ iid，$f(x;\theta)=\theta e^{-\theta x}$，$x>0$，$\theta>0$（參數空間 $(0,\infty)$）。

【口頭】看到 exponential 就要知道它是一種 Gamma。這個例子其實有 UMP，應該去找 UMP；這裡是為了練習 LRT。

**概似函數**（[▶ 03:38](https://youtu.be/Y_niPLoiQtg?t=218)）：
$$L(\theta)=\prod\theta e^{-\theta x_i}=\theta^ne^{-\theta\sum x_i}.$$

### 1.1 兩個最大概似值

**分母：整個參數空間**（[▶ 04:40](https://youtu.be/Y_niPLoiQtg?t=280)）。
$$\log L=n\log\theta-\theta\sum x_i,\qquad\frac{d}{d\theta}\log L=\frac n\theta-\sum x_i=0\ \Rightarrow\ \hat\theta_{\text{MLE}}=\frac{1}{\bar x}.$$
$$\max_\Omega L=\left(\frac1{\bar x}\right)^ne^{-\frac{1}{\bar x}\cdot n\bar x}=\bar x^{-n}e^{-n}.$$

**分子：$H_0$ 上的最大**（[▶ 06:11](https://youtu.be/Y_niPLoiQtg?t=371)）。微分等於 0 只有一個解 ⇒ $L$ 只有一個極大值、沒有其他 local maximum；在 $\hat\theta$ 左邊遞增、右邊遞減。

| 情形 | $\Theta_0=(0,\theta_0]$ 上的最大 |
|---|---|
| $\theta_0<\frac1{\bar x}$（MLE 不在 $H_0$） | 在端點：$L(\theta_0)=\theta_0^ne^{-\theta_0n\bar x}$ |
| $\theta_0\ge\frac1{\bar x}$（MLE 在 $H_0$） | 在 MLE：$\bar x^{-n}e^{-n}$ |

### 1.2 Λ 是 x̄ 的遞增函數

**$\Lambda$**（[▶ 09:48](https://youtu.be/Y_niPLoiQtg?t=588)）：$\theta_0<\frac1{\bar x}\iff\bar x<\frac1{\theta_0}$，
$$\Lambda=\begin{cases}\dfrac{\theta_0^ne^{-n\theta_0\bar x}}{\bar x^{-n}e^{-n}}=(\theta_0\bar x)^ne^{-n\theta_0\bar x+n},&\bar x<\frac1{\theta_0},\\[6pt]1,&\bar x\ge\frac1{\theta_0}.\end{cases}$$

[▶ 12:24](https://youtu.be/Y_niPLoiQtg?t=744) $\Lambda$ 整個是 $\bar x$ 的函數，但它的分配太複雜。改成看它是 $\bar x$ 的遞增還是遞減函數。

**微分**（[▶ 15:26](https://youtu.be/Y_niPLoiQtg?t=926)）：$\bar x<\frac1{\theta_0}$ 那段，
$$\log\Lambda=n\log(\theta_0\bar x)-n\theta_0\bar x+n,\qquad\frac{d\log\Lambda}{d\bar x}=\frac n{\bar x}-n\theta_0=n\left(\frac1{\bar x}-\theta_0\right)>0.$$
（因為 $\bar x<\frac1{\theta_0}$ ⇔ $\theta_0<\frac1{\bar x}$。）

[▶ 16:58](https://youtu.be/Y_niPLoiQtg?t=1018) 所以 $\Lambda$ 遞增上去，到 $\bar x=\frac1{\theta_0}$ 剛好是 1，之後都是 1。

$\Lambda$ 小 ⇔ $\bar x$ 小：
$$C=\{\bar x\le c\}.$$

### 1.3 用 Gamma→χ² 找臨界值

[▶ 18:28](https://youtu.be/Y_niPLoiQtg?t=1108) $\bar X$ 的分配不好直接用。改寫 pdf：
$$\theta e^{-\theta x}=\frac{1}{\Gamma(1)(1/\theta)^1}x^{1-1}e^{-x/(1/\theta)}\ \Rightarrow\ X\sim\Gamma\left(\alpha=1,\beta=\frac1\theta\right).$$

- [▶ 19:30](https://youtu.be/Y_niPLoiQtg?t=1170) 獨立 Gamma 相加（$\beta$ 相同）還是 Gamma，$\alpha$ 相加：$\sum X_i\sim\Gamma\left(n,\frac1\theta\right)$。
- [▶ 21:35](https://youtu.be/Y_niPLoiQtg?t=1295) $X\sim\Gamma(\alpha,\beta)$ ⇒ $\frac{2X}{\beta}\sim\chi^2(2\alpha)$（機率裡講過的）。

邊界點 $\theta=\theta_0$（[▶ 22:05](https://youtu.be/Y_niPLoiQtg?t=1325)）：$\frac{2\sum X_i}{1/\theta_0}=2\theta_0\sum X_i\sim\chi^2(2n)$。
$$\alpha=P_{\theta_0}(\bar X\le c)=P_{\theta_0}\left(2\theta_0\sum X_i\le 2\theta_0nc\right)=P\left(\chi^2(2n)\le 2n\theta_0c\right).$$

令 $\chi^2_\alpha(2n)$ 為 $\chi^2(2n)$ 左尾機率 $\alpha$ 的點（老師的記法）：

> **LRT 拒絕域**（[▶ 23:42](https://youtu.be/Y_niPLoiQtg?t=1422)）：
> $$\bar x\le\frac{\chi^2_\alpha(2n)}{2n\theta_0}.$$

（size 取在邊界點 $\theta_0$：$P_\theta(\bar X\le c)$ 隨 $\theta$ 遞增，$\Theta_0$ 上最大在 $\theta_0$。以上括號這句不是逐字稿內容，是依指數分配 $\theta$ 越大 $\bar X$ 越小推論的；老師直接代 $\theta_0$。）

【口頭】這個過程有點複雜。

---

## 2. 例二：N(θ,1)，H₀:θ=0 vs H₁:θ≠0

[▶ 24:12](https://youtu.be/Y_niPLoiQtg?t=1452) $X_1,\dots,X_n$ iid $N(\theta,1)$，變異數已知，比較簡單。

【口頭】[▶ 24:44](https://youtu.be/Y_niPLoiQtg?t=1484) 看任何分配都要知道參數空間：$N(\mu,\sigma^2)$ 中 $\mu\in(-\infty,\infty)$、$\sigma^2>0$。題目通常不會講，要自己知道。

[▶ 26:18](https://youtu.be/Y_niPLoiQtg?t=1578) 為什麼簡單：$H_0$ 只有一點，分子直接代 $\theta=0$；分母代 MLE。雙邊，沒有 UMP，一定要用 LRT。

**概似函數與 MLE**（[▶ 26:50](https://youtu.be/Y_niPLoiQtg?t=1610)）：
$$L(\theta)=(2\pi)^{-n/2}e^{-\frac12\sum(x_i-\theta)^2},\qquad\frac{d}{d\theta}\log L=\sum(x_i-\theta)=0\Rightarrow\hat\theta=\bar x.$$

**$\Lambda$**（[▶ 28:23](https://youtu.be/Y_niPLoiQtg?t=1703)）：
$$\Lambda=\frac{L(0)}{L(\bar x)}=\frac{(2\pi)^{-n/2}e^{-\frac12\sum x_i^2}}{(2\pi)^{-n/2}e^{-\frac12\sum(x_i-\bar x)^2}}.$$

【口頭】[▶ 29:26](https://youtu.be/Y_niPLoiQtg?t=1766) 這個展開統計會用很多次：
$$\sum(x_i-\bar x)^2=\sum x_i^2-n\bar x^2.$$
（$-2\bar x\sum x_i=-2n\bar x^2$，加上 $n\bar x^2$，淨 $-n\bar x^2$。）

所以
$$\Lambda=e^{-\frac n2\bar x^2}.$$

**轉換**（[▶ 31:28](https://youtu.be/Y_niPLoiQtg?t=1888)）：$\Lambda\le\lambda_0$ ⇔ $-\frac n2\bar x^2\le\log\lambda_0$ ⇔ $\bar x^2\ge c_1$ ⇔ $|\bar x|\ge c_2$ ⇔ $|\sqrt n\bar x|\ge c$。

[▶ 32:32](https://youtu.be/Y_niPLoiQtg?t=1952) 乘 $\sqrt n$ 是為了方便：$H_0$ 下 $\bar X\sim N\left(0,\frac1n\right)$，$\sqrt n\bar X\sim N(0,1)$。

$$\alpha=P_{\theta=0}(|\sqrt n\bar X|\ge c)=P(|Z|\ge c)\Rightarrow c=z_{\alpha/2}.$$
（$N(0,1)$ 對稱，兩邊各 $\alpha/2$。）

> **LRT 拒絕域**（[▶ 35:06](https://youtu.be/Y_niPLoiQtg?t=2106)）：$|\sqrt n\bar x|\ge z_{\alpha/2}$。

---

## 3. 例三：N(θ₁,θ₂) 兩參數都未知，H₀:θ₁=0

[▶ 35:37](https://youtu.be/Y_niPLoiQtg?t=2137) $X_1,\dots,X_n$ iid $N(\theta_1,\theta_2)$，$\theta_1\in\mathbb R$（平均數）、$\theta_2>0$（變異數）都未知。
$$H_0:\theta_1=0\quad\text{vs}\quad H_1:\theta_1\ne 0.$$

[▶ 36:41](https://youtu.be/Y_niPLoiQtg?t=2201) 參數空間其實是 $\Omega=\{(\theta_1,\theta_2):\theta_1\in\mathbb R,\theta_2>0\}$。假設要想成
$$H_0:\theta_1=0,\ \theta_2>0\quad\text{vs}\quad H_1:\theta_1\ne 0,\ \theta_2>0.$$
$\theta_2$ 沒有限制，兩邊都 $>0$。

**概似函數**（[▶ 37:41](https://youtu.be/Y_niPLoiQtg?t=2261)）：
$$L(\theta_1,\theta_2)=(2\pi\theta_2)^{-n/2}\exp\left\{-\frac{1}{2\theta_2}\sum(x_i-\theta_1)^2\right\}.$$

**分子：$H_0$ 上的最大**（[▶ 38:12](https://youtu.be/Y_niPLoiQtg?t=2292)）：$\theta_1=0$，只對 $\theta_2$ 求最大。
$$\log L(0,\theta_2)=-\frac n2\log(2\pi\theta_2)-\frac{1}{2\theta_2}\sum x_i^2,\qquad\frac{\partial}{\partial\theta_2}=0\Rightarrow\hat\theta_2^{(0)}=\frac1n\sum x_i^2.$$
代回（$\sum x_i^2$ 消掉）：
$$\max_{\Theta_0}L=\left(\frac{2\pi}{n}\sum x_i^2\right)^{-n/2}e^{-n/2}.$$

**分母：整個參數空間的最大＝MLE**（[▶ 42:18](https://youtu.be/Y_niPLoiQtg?t=2538)）：先對 $\theta_1$ 微分，得 $\hat\theta_1=\bar x$；代入再對 $\theta_2$ 微分，得
$$\hat\theta_2=\frac1n\sum(x_i-\bar x)^2.$$
$$\max_\Omega L=\left(\frac{2\pi}{n}\sum(x_i-\bar x)^2\right)^{-n/2}e^{-n/2}.$$

**$\Lambda$**（[▶ 45:28](https://youtu.be/Y_niPLoiQtg?t=2728)）：
$$\Lambda=\left[\frac{\sum(x_i-\bar x)^2}{\sum x_i^2}\right]^{n/2}.$$

[▶ 46:29](https://youtu.be/Y_niPLoiQtg?t=2789) 取 log、除以 $\frac n2$：$\Lambda\le\lambda_0$ ⇔ $\log\frac{\sum(x_i-\bar x)^2}{\sum x_i^2}\le\lambda_1$。這個量的分配還是不知道，要再轉換——下次講。

---

## 4. 一頁速查表

**LRT 解題步驟**：

1. 概似函數 → MLE → 分母 $=L(\hat\theta)$。
2. $H_0$ 上的最大：$H_0$ 是一點就直接代；是區間要看 MLE 在不在 $H_0$ 裡（不在就在端點）。
3. $\Lambda$ 化簡，判斷它是哪個統計量的遞增／遞減函數（可用微分）。
4. 一對一轉成分配已知的統計量，用 size $=\alpha$ 找臨界值。

**例**

| 分配 | 假設 | $\Lambda$ | LRT 拒絕域 |
|---|---|---|---|
| $\theta e^{-\theta x}$ | $\theta\le\theta_0$ vs $>$ | $(\theta_0\bar x)^ne^{-n\theta_0\bar x+n}$（$\bar x<1/\theta_0$），否則 1 | $\bar x\le\frac{\chi^2_\alpha(2n)}{2n\theta_0}$ |
| $N(\theta,1)$ | $\theta=0$ vs $\ne$ | $e^{-n\bar x^2/2}$ | $\lvert\sqrt n\bar x\rvert\ge z_{\alpha/2}$ |
| $N(\theta_1,\theta_2)$ | $\theta_1=0$ vs $\ne$ | $\left[\frac{\sum(x_i-\bar x)^2}{\sum x_i^2}\right]^{n/2}$ | 下集（$t$ 檢定） |

**常用事實**：

- $X\sim\Gamma(\alpha,\beta)$ ⇒ $2X/\beta\sim\chi^2(2\alpha)$；指數 $\theta e^{-\theta x}=\Gamma(1,1/\theta)$。
- $\sum(x_i-\bar x)^2=\sum x_i^2-n\bar x^2$。
- $N(\mu,\sigma^2)$ 的 MLE：$\hat\mu=\bar x$，$\hat\sigma^2=\frac1n\sum(x_i-\bar x)^2$。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 例三的 $\Lambda$ | 下一集：轉成 $t$ 統計量 |
| Gamma→$\chi^2$ | 變異數的檢定 |

---

## 附：本集一句話總結

> **LRT 例題的套路是：分母代 MLE、分子在 $H_0$ 上求最大（區間時看 MLE 在不在裡面），化簡 $\Lambda$ 後判斷它是哪個統計量的單調函數，再轉成已知分配求臨界值——指數分配單邊得 $\bar x\le\chi^2_\alpha(2n)/(2n\theta_0)$，$N(\theta,1)$ 雙邊得 $|\sqrt n\bar x|\ge z_{\alpha/2}$，$N(\theta_1,\theta_2)$ 得 $\Lambda=[\sum(x_i-\bar x)^2/\sum x_i^2]^{n/2}$，下集續。**

---

*筆記依據「高等統計學」Lec19 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
