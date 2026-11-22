---
course: 高等統計學（數理統計續）
episode: 25
lecture: Lec25（第十三週 2/2）
date: 待補
video: https://youtu.be/kI2Se2OrXls
notes: Hogg 8th ed. §3.5.1 二維常態分配（p. 198）；§2.3 條件分配；§4.7 卡方檢定（p. 283）
---

# 第 25 集 · 第十三週 (2/2)：二維常態分配——joint pdf、邊際、條件分配；卡方適合度檢定的想法 [▶ 影片](https://youtu.be/kI2Se2OrXls)

← 上一集：[24](24-p1-p2-test-bivariate-normal-preliminaries.md) ｜ [總目錄](../README.md) ｜ 下一集：[26](26-pearson-chi-square-test-mendel-example.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 25 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 61 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.3、§3.5.1、§4.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「bivariate」→「by varic／By-Value」，「二維」→「歐維／奧尾」，「$\rho$」→「Low／Raw／羅」，「covariance」→「Covalence」，「斗笠」→「躲立／斗粒」，「chi-square」→「Cite／Kai Square」，「goodness of fit」照錄，「partition」照錄。[▶ 00:00](https://youtu.be/kI2Se2OrXls?t=0) 開頭重複的「字幕提供」是幻聽，忽略。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要隨機向量、為什麼是常態](#1-為什麼要隨機向量為什麼是常態)
- [2. 二維常態的 pdf](#2-二維常態的-pdf)
- [3. 證明它是 joint pdf：配方](#3-證明它是-joint-pdf配方)
- [4. 邊際分配](#4-邊際分配)
- [5. 條件分配](#5-條件分配)
- [6. 卡方適合度檢定的想法](#6-卡方適合度檢定的想法)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 二維常態 pdf、證明積分為 1 | §3.5.1，p. 198 |
| 邊際：$X\sim N(\mu_1,\sigma_1^2)$、$Y\sim N(\mu_2,\sigma_2^2)$ | §3.5.1 |
| 條件：$Y\mid X=x$ 的平均數與變異數 | §3.5.1、§2.3 |
| 卡方適合度檢定 | §4.7，p. 283 |

---

## 1. 為什麼要隨機向量、為什麼是常態

【口頭】[▶ 00:33](https://youtu.be/kI2Se2OrXls?t=33)

- 電子公司檢驗產品，不會只看厚度，還有亮度等很多特徵，都要好才是好。
- [▶ 01:03](https://youtu.be/kI2Se2OrXls?t=63) 以後當父母，你不會只希望小孩書讀得好，也希望運動、音樂都不錯。
- 同時看好幾個隨機變數，合起來叫**隨機向量**；它的 pdf 叫 **joint pdf**。
- [▶ 02:04](https://youtu.be/kI2Se2OrXls?t=124) 為什麼講常態：一維時，平均數的信賴區間、檢定、兩平均數、兩變異數，通通是常態才有辦法做；別的分配就要靠大樣本。工學院、管理學院、時間序列、生物統計，用的幾乎都是常態。

---

## 2. 二維常態的 pdf

[▶ 03:06](https://youtu.be/kI2Se2OrXls?t=186) 先給一個函數：

$$f(x,y)=\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\exp\left\{-\frac{1}{2(1-\rho^2)}\left[\left(\frac{x-\mu_1}{\sigma_1}\right)^2-2\rho\frac{(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\left(\frac{y-\mu_2}{\sigma_2}\right)^2\right]\right\},$$
$(x,y)\in\mathbb R^2$，$\sigma_1,\sigma_2>0$，$-1<\rho<1$。

【口頭】看起來非常複雜，**絕對不要背**。常常看到、熟悉了，自然就記下來。

**跟一維比較**（[▶ 06:12](https://youtu.be/kI2Se2OrXls?t=372)）：一維 $N(\mu,\sigma^2)$ 的 pdf 是 $\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$。

- 兩個隨機變數，兩個 $\sqrt{2\pi}$ ⇒ $2\pi$；兩個 $\sigma$。
- 多了 $\sqrt{1-\rho^2}$ 和交叉項：描述兩者的**相關**。

**$\rho$ 是相關係數**（[▶ 06:43](https://youtu.be/kI2Se2OrXls?t=403)）：
$$\rho=\frac{\text{Cov}(X,Y)}{\sigma_1\sigma_2}=\frac{E[(X-\mu_1)(Y-\mu_2)]}{\sigma_1\sigma_2}.$$
[▶ 07:44](https://youtu.be/kI2Se2OrXls?t=464) $X,Y$ 獨立 ⇒ $E[(X-\mu_1)(Y-\mu_2)]=E(X-\mu_1)E(Y-\mu_2)=0$ ⇒ $\rho=0$；這時 $\sqrt{1-\rho^2}=1$、交叉項消失。

**形狀**（[▶ 09:48](https://youtu.be/kI2Se2OrXls?t=588)）：【口頭】像農民上山工作戴的**斗笠**：一軸 $x$、一軸 $y$，高度是 pdf，三維空間的東西。

可以證明：$\mu_1,\mu_2$ 是 $X,Y$ 的平均數；$\sigma_1^2,\sigma_2^2$ 是變異數；$\rho\in(-1,1)$ 是相關係數。

---

## 3. 證明它是 joint pdf：配方

[▶ 11:19](https://youtu.be/kI2Se2OrXls?t=679) 要證 $f\ge 0$、$\iint f=1$。

**$f\ge 0$**：$\sigma_1,\sigma_2>0$；$\rho^2<1$ ⇒ $\sqrt{1-\rho^2}>0$；指數函數 $>0$。

**$\iint f=1$**（[▶ 11:49](https://youtu.be/kI2Se2OrXls?t=709)）：用上一集的拆解法，拆成 $h(x)g(x,y)$。技巧相當高。

令 $a=\frac{y-\mu_2}{\sigma_2}$，$b=\rho\frac{x-\mu_1}{\sigma_1}$（[▶ 13:19](https://youtu.be/kI2Se2OrXls?t=799)）。中括號是 $a^2-2ab+\left(\frac{x-\mu_1}{\sigma_1}\right)^2$，配成 $(a-b)^2$，多出的 $b^2$ 減回去：
$$[\cdots]=(a-b)^2+(1-\rho^2)\left(\frac{x-\mu_1}{\sigma_1}\right)^2.$$

[▶ 15:19](https://youtu.be/kI2Se2OrXls?t=919) $(a-b)^2$ 的分母提出 $\sigma_2$：
$$(a-b)^2=\frac{1}{\sigma_2^2}\left[y-\left(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1)\right)\right]^2.$$

代回指數（[▶ 18:28](https://youtu.be/kI2Se2OrXls?t=1108)）：$(1-\rho^2)$ 在第二項消掉，
$$f(x,y)=\underbrace{\frac{1}{\sqrt{2\pi}\sigma_1}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}}}_{h(x)}\cdot\underbrace{\frac{1}{\sqrt{2\pi}\sigma_2\sqrt{1-\rho^2}}\exp\left\{-\frac{\left[y-\left(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1)\right)\right]^2}{2\sigma_2^2(1-\rho^2)}\right\}}_{g(x,y)}.$$

- $h(x)$：$N(\mu_1,\sigma_1^2)$ 的 pdf ⇒ $\int h=1$。
- [▶ 22:08](https://youtu.be/kI2Se2OrXls?t=1328) $g(x,\cdot)$：對每個 $x$，是 $N\left(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1),\ \sigma_2^2(1-\rho^2)\right)$ 的 pdf ⇒ $\int g\,dy=1$。

[▶ 23:11](https://youtu.be/kI2Se2OrXls?t=1391) 先積 $y$ 得 1，再積 $x$ 得 1 ⇒ $\iint f=1$。原本非常複雜的積分，拆開後變成兩個常態 pdf 相乘。

> **定義**（[▶ 25:50](https://youtu.be/kI2Se2OrXls?t=1550)）：$(X,Y)$ 的 joint pdf 是上式時，稱 $(X,Y)$ 具有**二維常態分配**（bivariate normal distribution）。

[▶ 26:52](https://youtu.be/kI2Se2OrXls?t=1612) 由上一集的定理，背後一定有樣本空間、機率集合函數、兩個隨機變數映到 $\mathbb R^2$。有了 joint pdf，算 $P((X,Y)\in A)$ 就對 $A$ 積分；算 $E[u(X,Y)]=\iint u(x,y)f(x,y)\,dx\,dy$，什麼都可以做。

---

## 4. 邊際分配

[▶ 30:28](https://youtu.be/kI2Se2OrXls?t=1828) 兩個合起來是二維常態，個別是什麼分配？用 joint pdf 對另一個變數積分。

**$X$ 的邊際**（[▶ 31:30](https://youtu.be/kI2Se2OrXls?t=1890)）：用 $f=h(x)g(x,y)$，對 $y$ 積分，$g$ 積成 1：
$$f_X(x)=\frac{1}{\sqrt{2\pi}\sigma_1}e^{-\frac{(x-\mu_1)^2}{2\sigma_1^2}}\ \Rightarrow\ X\sim N(\mu_1,\sigma_1^2).$$

**$Y$ 的邊際**（[▶ 35:06](https://youtu.be/kI2Se2OrXls?t=2106)）：同樣的技巧，改把 $x$ 那一項當 $a$ 配方，寫成
$$f(x,y)=\frac{1}{\sqrt{2\pi}\sigma_2}e^{-\frac{(y-\mu_2)^2}{2\sigma_2^2}}\cdot\frac{1}{\sqrt{2\pi}\sigma_1\sqrt{1-\rho^2}}\exp\left\{-\frac{\left[x-\left(\mu_1+\rho\frac{\sigma_1}{\sigma_2}(y-\mu_2)\right)\right]^2}{2\sigma_1^2(1-\rho^2)}\right\},$$
先對 $x$ 積分 ⇒ $Y\sim N(\mu_2,\sigma_2^2)$。

---

## 5. 條件分配

[▶ 37:37](https://youtu.be/kI2Se2OrXls?t=2257) 二維、三維以上時**條件分配**很重要。

**直覺**（[▶ 38:08](https://youtu.be/kI2Se2OrXls?t=2288)）：$P(B\mid A)=\frac{P(A\cap B)}{P(A)}$。$A$ 已經發生，$A$ 以外不會發生，把 $A$ 重新當成樣本空間；$B$ 要發生只能在交集裡。

[▶ 39:41](https://youtu.be/kI2Se2OrXls?t=2381) $X$ 已經發生在 $x$：把斗笠沿著 $X=x$ 那條線切下去，得到一條曲線，那就是條件 pdf。
$$f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)}.$$
條件 pdf 還是 pdf：給定 $x$，對 $y$ 從 $-\infty$ 積到 $\infty$ 是 1。

**計算**（[▶ 42:13](https://youtu.be/kI2Se2OrXls?t=2533)）：分子用 $h(x)g(x,y)$ 那個形式（第一項就是分母）：
$$f_{Y\mid X}(y\mid x)=g(x,y).$$

> **結果**（[▶ 45:56](https://youtu.be/kI2Se2OrXls?t=2756)）：
> $$Y\mid X=x\ \sim\ N\left(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1),\ \sigma_2^2(1-\rho^2)\right).$$
> $$E(Y\mid X=x)=\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1),\qquad\text{Var}(Y\mid X=x)=\sigma_2^2(1-\rho^2).$$

（$x$ 是給定的常數，所以平均數裡雖然有 $x$，仍是常數。）

**迴歸**（[▶ 47:28](https://youtu.be/kI2Se2OrXls?t=2848)）：統計最主要的延伸是**迴歸**（regression），專門討論固定 $X$ 看 $Y$。

【口頭】[▶ 47:59](https://youtu.be/kI2Se2OrXls?t=2879) 通貨膨脹什麼都貴，政府想把利率提高：利率高，存銀行的利息多，大家把錢放銀行，社會上消費的錢變少，價格就降低。現在利率 1%、2%，一百萬一年領一兩萬，沒人想存，都去買股票、做生意。政府要想：利率提高多少，物價能降低多少——這就是給定一個東西看另一個。迴歸關心的是 $Y$，但不會只有一個 $X$。

---

## 6. 卡方適合度檢定的想法

[▶ 49:32](https://youtu.be/kI2Se2OrXls?t=2972) 最後一個主題：**$\chi^2$ 檢定**（chi-square test），比較適當的名字是**適合度檢定**（goodness-of-fit test）。

**動機**（[▶ 50:03](https://youtu.be/kI2Se2OrXls?t=3003)）：

- 統計推論有點估計、區間估計、檢定。【口頭】我們不喜歡點估計：$\hat\theta$ 是隨機變數、$\theta$ 是常數，相等的機率通常是 0；除非樣本數無窮，否則點估計意義不大，即使它是 UMVUE。
- [▶ 51:36](https://youtu.be/kI2Se2OrXls?t=3096) 信賴區間、檢定可以**保證**：區間涵蓋 $\theta$ 的機率 95%、99%；$H_0$ 對卻拒絕的機率很小。
- [▶ 52:06](https://youtu.be/kI2Se2OrXls?t=3126) 但大多數方法都**假設**樣本來自某個分配，通常是常態。怎麼知道真的是常態？要檢定：
$$H_0:X\text{ 來自常態}\quad\text{vs}\quad H_1:X\text{ 不是來自常態}.$$
接受 $H_0$ 就相信樣本真的來自常態。

【口頭】[▶ 54:12](https://youtu.be/kI2Se2OrXls?t=3252) 正式名稱是 **Pearson 卡方檢定**。這是**老** Pearson 發展的；Neyman–Pearson 的 Pearson 是他的兒子，跟 Neyman 創造了另一套假設檢定理論。

**一般化**（[▶ 55:12](https://youtu.be/kI2Se2OrXls?t=3312)）：$H_0:X\sim F_0$ vs $H_1:X\not\sim F_0$。抽隨機樣本 $X_1,\dots,X_n$。

**做法**（[▶ 56:49](https://youtu.be/kI2Se2OrXls?t=3409)）：

1. 把 $X$ 的空間切成 $A_1,\dots,A_k$：一個 **partition**（互相排斥、聯集是整個空間）。
2. [▶ 58:21](https://youtu.be/kI2Se2OrXls?t=3501) $H_0$ 下每塊的機率：$p_j=P_{H_0}(X\in A_j)=\int_{A_j}f_0(x)\,dx$。
3. [▶ 58:51](https://youtu.be/kI2Se2OrXls?t=3531) **理論個數**：$n$ 個樣本，落在 $A_j$ 的個數理論上是 $np_j$。
4. [▶ 59:53](https://youtu.be/kI2Se2OrXls?t=3593) **實際個數**：$N_j$＝真正落在 $A_j$ 的個數。
5. 每一塊的 $N_j$ 和 $np_j$ 都很接近 ⇒ 相信 $H_0$；有很多塊不接近 ⇒ 不相信 $H_0$。

下一集把它變成檢定統計量。

---

## 7. 一頁速查表

**二維常態**：
$$f(x,y)=\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\exp\left\{-\frac{1}{2(1-\rho^2)}\left[z_1^2-2\rho z_1z_2+z_2^2\right]\right\},\quad z_1=\frac{x-\mu_1}{\sigma_1},\ z_2=\frac{y-\mu_2}{\sigma_2}.$$

**關鍵一步（配方）**：$z_1^2-2\rho z_1z_2+z_2^2=(z_2-\rho z_1)^2+(1-\rho^2)z_1^2$ ⇒ $f=h(x)\,g(x,y)$。

| | 分配 |
|---|---|
| $X$ | $N(\mu_1,\sigma_1^2)$ |
| $Y$ | $N(\mu_2,\sigma_2^2)$ |
| $Y\mid X=x$ | $N\left(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1),\ \sigma_2^2(1-\rho^2)\right)$ |
| $X\mid Y=y$ | $N\left(\mu_1+\rho\frac{\sigma_1}{\sigma_2}(y-\mu_2),\ \sigma_1^2(1-\rho^2)\right)$ |

$\rho=\frac{\text{Cov}(X,Y)}{\sigma_1\sigma_2}$；獨立 ⇒ $\rho=0$。

**卡方適合度**：partition $A_1,\dots,A_k$；$p_j=P_{H_0}(A_j)$；比較實際個數 $N_j$ 和理論個數 $np_j$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $N_j$ vs $np_j$ | 下一集：Pearson 卡方統計量 $\sum\frac{(N_j-np_j)^2}{np_j}$ |
| 條件平均 | 迴歸分析（課程之外） |

---

## 附：本集一句話總結

> **二維常態的 joint pdf 雖然複雜，但把指數裡的二次式配方成 $(z_2-\rho z_1)^2+(1-\rho^2)z_1^2$，就拆成「$X\sim N(\mu_1,\sigma_1^2)$ 的 pdf」乘上「$Y\mid X=x\sim N(\mu_2+\rho\frac{\sigma_2}{\sigma_1}(x-\mu_1),\sigma_2^2(1-\rho^2))$ 的 pdf」，一次得到積分為 1、邊際與條件分配；接著介紹卡方適合度檢定：把空間切塊，比較每塊的實際個數和 $H_0$ 下的理論個數。**

---

*筆記依據「高等統計學」Lec25 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
