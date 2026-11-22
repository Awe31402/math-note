---
course: 高等統計學（數理統計續）
episode: 24
lecture: Lec24（第十三週 1/2）
date: 待補
video: https://youtu.be/YkbqM9nQRLA
notes: Hogg 8th ed. §4.5 比例的大樣本檢定；§1.5–1.7 隨機變數與 pdf；§2.1、§2.3 joint／marginal／conditional pdf；§3.5 多元常態（預告）
---

# 第 24 集 · 第十三週 (1/2)：H₀:p₁=p₂ 的大樣本檢定；二維常態分配的預備：從函數到 joint pdf [▶ 影片](https://youtu.be/YkbqM9nQRLA)

← 上一集：[23](23-two-sample-means-proportion-test-summary.md) ｜ [總目錄](../README.md) ｜ 下一集：[25](25-bivariate-normal-marginal-conditional-chi-square-intro.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 24 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 23 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.5–1.7、§2.1、§2.3、§3.5、§4.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「pivotal quantity」→「PuPetal Quality」，「bivariate」→「By-Value」，「二維」→「奧維／歐尾」，「卡方檢定」→「卡房檢定」，「樣本空間」→「樣門空間」，「映到實數空間」→「印到十字／14 空間」，「機率集合函數」→「機力／激勵集合函數」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. H₀:p₁=p₂ 的大樣本檢定](#1-h₀p₁p₂-的大樣本檢定)
- [2. 為什麼需要多維](#2-為什麼需要多維)
- [3. 複習：樣本空間、機率集合函數、隨機變數、pdf](#3-複習樣本空間機率集合函數隨機變數pdf)
- [4. 反過來：有函數就有隨機變數](#4-反過來有函數就有隨機變數)
- [5. 證明二維 joint pdf 的方法](#5-證明二維-joint-pdf-的方法)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $H_0:p_1=p_2$ 的近似檢定 | §4.5 |
| 二維常態的預備 | §2.1、§2.3、§3.5 |

[▶ 07:43](https://youtu.be/YkbqM9nQRLA?t=463) 最後還有兩個主題：**二維常態分配**（bivariate normal distribution）和 **$\chi^2$ 檢定**。

---

## 1. H₀:p₁=p₂ 的大樣本檢定

[▶ 00:00](https://youtu.be/YkbqM9nQRLA?t=0) 上一集：
$$\frac{(\hat p_1-\hat p_2)-(p_1-p_2)}{\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}}\ \dot\sim\ N(0,1).$$

[▶ 00:31](https://youtu.be/YkbqM9nQRLA?t=31) 它是**樞紐量**（pivotal quantity）：隨機樣本和參數的函數。$\hat p_1,\hat p_2$、根號裡的東西都由 $X$、$Y$ 算得出來（樣本只有一個也還是隨機樣本）；參數是 $p_1-p_2$。用它可以造 $p_1-p_2$ 的信賴區間。

**檢定**（[▶ 02:03](https://youtu.be/YkbqM9nQRLA?t=123)）：$H_0:p_1=p_2$ vs $H_1:p_1\ne p_2$。$H_0$ 下 $p_1-p_2=0$：
$$Z=\frac{\hat p_1-\hat p_2}{\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}}\ \dot\sim\ N(0,1).$$

**直覺**（[▶ 03:03](https://youtu.be/YkbqM9nQRLA?t=183)）：$\hat p_1-\hat p_2\xrightarrow{P}p_1-p_2$，$H_0$ 下是 0。所以 $\hat p_1-\hat p_2$ 在 0 旁邊就相信 $H_0$；太大或太小就拒絕。

> **拒絕域**（[▶ 04:41](https://youtu.be/YkbqM9nQRLA?t=281)）：$Z\le-z_{\alpha/2}$ 或 $Z\ge z_{\alpha/2}$，即 $|Z|\ge z_{\alpha/2}$。

**size 近似 $\alpha$**（[▶ 05:11](https://youtu.be/YkbqM9nQRLA?t=311)）：$Z_0\sim N(0,1)$ 時 $P(Z_0\le-z_{\alpha/2})+P(Z_0\ge z_{\alpha/2})=\alpha$；$H_0$ 下 $Z$ 很接近 $Z_0$，所以
$$P_{H_0}(Z\le-z_{\alpha/2})+P_{H_0}(Z\ge z_{\alpha/2})\approx\frac\alpha2+\frac\alpha2=\alpha.$$
這是顯著水準 $\alpha$ 的（近似）檢定。

以下**不是逐字稿內容**，是補充：實務上也常在 $H_0$ 下用合併比例 $\hat p=\frac{X+Y}{n+m}$ 估計共同的 $p$，分母寫成 $\sqrt{\hat p(1-\hat p)\left(\frac1n+\frac1m\right)}$；課堂用的是各自的 $\hat p_1,\hat p_2$。

---

## 2. 為什麼需要多維

【口頭】[▶ 08:14](https://youtu.be/YkbqM9nQRLA?t=494)

- 讀統計通常會讀**多變量統計**（multivariate statistics）＝多維的統計。
- 一個隨機變數把樣本空間映到實數線，是一維的。
- 很多事情不是一維的：電子產品合不合格，厚度、亮度、化學性質……好多性質都要合格；去做體檢，心跳、血壓、肝指數……一檢查就好幾十項。量的是很多隨機變數。
- [▶ 09:48](https://youtu.be/YkbqM9nQRLA?t=588) 二維以上幾乎都限制在**常態分配**：別的分配不是沒有，但非常困難。

---

## 3. 複習：樣本空間、機率集合函數、隨機變數、pdf

[▶ 10:19](https://youtu.be/YkbqM9nQRLA?t=619)

- **樣本空間** $\mathcal S$。
- **事件**：$\mathcal S$ 的子集。
- **機率集合函數** $P$：定義在事件上的函數，滿足幾個條件（以前講過）。
- [▶ 11:23](https://youtu.be/YkbqM9nQRLA?t=683) **隨機變數** $X$：把 $\mathcal S$ 映到實數空間的函數。任何這種函數都叫隨機變數，可以定義無限多個。
- [▶ 12:24](https://youtu.be/YkbqM9nQRLA?t=744) **離散型**：值域 $X(\mathcal S)$ 可數（countable，可以 1、2、3 地數），$P(X\in A)=\sum_{x\in A}f(x)$。
- [▶ 13:28](https://youtu.be/YkbqM9nQRLA?t=808) **連續型**：$P(X\in A)=\int_Af(x)\,dx$。

[▶ 13:59](https://youtu.be/YkbqM9nQRLA?t=839) 本來算 $P(X\in A)$ 要把 $A$ 映回樣本空間，找 $X^{-1}(A)$（函數值落在 $A$ 的那些點）的機率。有了 pdf 就不用回到樣本空間，直接相加或積分——簡單很多。所以 **pdf 非常重要**。

---

## 4. 反過來：有函數就有隨機變數

> **定理（機率論）**（[▶ 15:00](https://youtu.be/YkbqM9nQRLA?t=900)）：若 $f\ge 0$ 且 $\int f=1$（或 $\sum f=1$），則存在樣本空間、機率集合函數和隨機變數 $X$，使 $f$ 就是 $X$ 的 pdf。

- 原本的順序：樣本空間 → 機率集合函數 → 隨機變數 → pdf。
- [▶ 15:31](https://youtu.be/YkbqM9nQRLA?t=931) 反過來：先有函數，一定有對應的隨機變數。
- 【口頭】[▶ 16:01](https://youtu.be/YkbqM9nQRLA?t=961) 學過的機率分配都是數學家找出來的，再發現現實社會很多問題很接近這些分配。

**二維**（[▶ 17:04](https://youtu.be/YkbqM9nQRLA?t=1024)）：若 $f(x,y)\ge 0$ 且 $\iint_{\mathbb R^2}f=1$，則存在隨機變數 $X,Y$ 使 $f$ 是它們的 joint pdf。

[▶ 17:35](https://youtu.be/YkbqM9nQRLA?t=1055) 所以二維不用先找樣本空間、機率集合函數、再定義兩個隨機變數映到 $\mathbb R^2$ 去找 joint pdf；先找一個函數就好。

---

## 5. 證明二維 joint pdf 的方法

[▶ 18:36](https://youtu.be/YkbqM9nQRLA?t=1116) 下次要用這個方法證明二維常態。

**設定**：$f(x,y)\ge 0$ 可以拆成
$$f(x,y)=h(x)\,g(x,y),$$
其中

1. $\int_{-\infty}^\infty h(x)\,dx=1$；
2. 對**每一個** $x$：$\int_{-\infty}^\infty g(x,y)\,dy=1$。

**結論**：

**(a) $f$ 是 joint pdf**（[▶ 20:11](https://youtu.be/YkbqM9nQRLA?t=1211)）：
$$\iint f(x,y)\,dy\,dx=\int h(x)\underbrace{\left[\int g(x,y)\,dy\right]}_{=1}dx=\int h(x)\,dx=1.$$

**(b) $h$ 是 $X$ 的 marginal pdf**（[▶ 21:12](https://youtu.be/YkbqM9nQRLA?t=1272)）：
$$f_X(x)=\int f(x,y)\,dy=h(x)\int g(x,y)\,dy=h(x).$$

**(c) $g$ 是給定 $X=x$ 時 $Y$ 的 conditional pdf**（[▶ 22:14](https://youtu.be/YkbqM9nQRLA?t=1334)）：類比條件機率 $P(B\mid A)=\frac{P(A\cap B)}{P(A)}$，
$$f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)}=\frac{h(x)g(x,y)}{h(x)}=g(x,y).$$

---

## 6. 一頁速查表

**$H_0:p_1=p_2$**：
$$Z=\frac{\hat p_1-\hat p_2}{\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}},\qquad\text{拒絕 }|Z|\ge z_{\alpha/2}\ (\text{size}\approx\alpha).$$

**有函數就有隨機變數**：$f\ge 0$、$\int f=1$ ⇒ 存在 $X$ 以 $f$ 為 pdf（二維同理）。

**拆解法**：$f(x,y)=h(x)g(x,y)$，$\int h=1$，$\int g(x,y)\,dy=1\ \forall x$ ⇒

| | 結論 |
|---|---|
| $f$ | joint pdf |
| $h(x)$ | $X$ 的 marginal pdf |
| $g(x,y)$ | $Y\mid X=x$ 的 conditional pdf |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 拆解法 | 下一集：二維常態的 joint pdf、marginal、conditional |
| 多維 | $\chi^2$ 檢定 |

---

## 附：本集一句話總結

> **$H_0:p_1=p_2$ 的近似檢定用 $\hat p_1-\hat p_2$ 除以估計標準差，絕對值超過 $z_{\alpha/2}$ 就拒絕；接著為二維常態做準備：只要非負函數積分為 1 就是某些隨機變數的 pdf，而若 $f(x,y)=h(x)g(x,y)$ 且 $h$ 和每個 $g(x,\cdot)$ 都積分為 1，則 $f$ 是 joint pdf、$h$ 是 $X$ 的 marginal、$g$ 是 $Y\mid X$ 的 conditional。**

---

*筆記依據「高等統計學」Lec24 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
