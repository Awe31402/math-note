---
course: 統計學（數理統計，數學系）
episode: 6
lecture: Lec06
date: 待補
video: https://youtu.be/WKIKv_BhN2g
notes: Hogg 8th ed. §1.7.2 分配函數法；§1.9 Theorem 1.9.2 mgf 唯一性（p. 71）；§2.1 隨機向量（Definition 2.1.1，p. 85）、§2.1.1 邊際分配（p. 89）、§2.6 多個隨機變數（Definition 2.6.1，p. 134）；§1.4.1 事件獨立（Definition 1.4.2，p. 29）；§2.4 隨機變數獨立（Definition 2.4.1，p. 118）；同分配（p. 40）、iid（p. 152）
---

# 第 6 集 · Lec06：Gamma→卡方；mgf 唯一性；隨機向量、獨立、同分配 [▶ 影片](https://youtu.be/WKIKv_BhN2g)

← 上一集：[05](05-gamma-mgf-cdf-technique.md) ｜ [總目錄](../README.md) ｜ 下一集：[07](07-iid-one-to-one-transformation-uniform.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 6 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:11:13，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.4、§1.7、§1.9、§2.1、§2.4、§2.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「卡方」→「卡荒／卡皇／烤荒」，「Poisson」→「普阿松／土阿松」，「joint」→「join／9n」，「marginal」照錄，「機率」→「激勵／積慮」，「樣本空間」→「樣門／藥門空間」，「實數」→「時數／十四」，「method」→「MESO」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例：Gamma 變換成卡方（分配函數法）](#1-例gamma-變換成卡方分配函數法)
- [2. mgf 唯一性定理](#2-mgf-唯一性定理)
- [3. mgf 法](#3-mgf-法)
  - [3.1 標準化常態變數（mgf 法）](#31-標準化常態變數mgf-法)
  - [3.2 Gamma 變換成卡方（mgf 法）](#32-gamma-變換成卡方mgf-法)
- [4. 為什麼要很多個隨機變數](#4-為什麼要很多個隨機變數)
- [5. 隨機向量、聯合 pdf、邊際 pdf](#5-隨機向量聯合-pdf邊際-pdf)
- [6. 事件的獨立](#6-事件的獨立)
- [7. 連續型：單點機率是 0](#7-連續型單點機率是-0)
- [8. 隨機變數的獨立](#8-隨機變數的獨立)
- [9. 同分配](#9-同分配)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本對應 |
|---|---|
| $X\sim\Gamma(\alpha,\beta)$ ⇒ $\frac{2X}{\beta}\sim\chi^2(2\alpha)$（兩種證法） | §1.7.2、§3.3 |
| mgf 和分配一對一 | Theorem 1.9.2，p. 71 |
| mgf 法 | §1.9 |
| 隨機向量、聯合 pdf、邊際 pdf | §2.1，p. 85；§2.6，p. 134 |
| 事件獨立、隨機變數獨立 | Definition 1.4.2，p. 29；Definition 2.4.1，p. 118 |
| 同分配（identically distributed） | p. 40、p. 152 |

[▶ 01:02](https://youtu.be/WKIKv_BhN2g?t=62) 【口頭】求 $Y=g(X)$ 的分配有很多方法。每種方法對某些問題比較簡單、對某些比較難，要做過才知道哪種問題用哪種方法。

---

## 1. 例：Gamma 變換成卡方（分配函數法）

[▶ 01:32](https://youtu.be/WKIKv_BhN2g?t=92)

> **命題**：$X\sim\Gamma(\alpha,\beta)$，則 $Y=\dfrac{2X}{\beta}\sim\chi^2(r)$，$r=2\alpha$。

複習：$f_X(x)=\dfrac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}$，$x>0$；$x\le 0$ 是 0。「你一定要記得，不記得就沒辦法了。」

**證明（分配函數法）**（[▶ 03:37](https://youtu.be/WKIKv_BhN2g?t=217)）

**Step 1：$Y$ 的分配函數換成 $X$ 的事件。** $\alpha,\beta>0$，所以乘除不改不等號方向：
$$F_Y(y)=P(Y\le y)=P\left(\frac{2X}{\beta}\le y\right)=P\left(X\le\frac{\beta y}{2}\right).$$

**Step 2：寫成積分。** [▶ 05:42](https://youtu.be/WKIKv_BhN2g?t=342) 為什麼從 0 積？因為 $X$ 只在 $(0,\infty)$ 有正的 pdf。
$$F_Y(y)=\int_0^{\beta y/2}\frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}\,dx.$$
不用真的積出來，學過微積分就能微分。

**Step 3：微分。** 上限是 $y$ 的函數 $h(y)=\beta y/2$，所以「把 $x$ 換成 $\beta y/2$」再乘 $h'(y)=\beta/2$：
$$f_Y(y)=\frac{1}{\Gamma(\alpha)\beta^\alpha}\left(\frac{\beta y}{2}\right)^{\alpha-1}e^{-y/2}\cdot\frac{\beta}{2}.$$

**Step 4：化簡**（[▶ 08:20](https://youtu.be/WKIKv_BhN2g?t=500)）：$\beta^{\alpha-1}\cdot\beta=\beta^\alpha$，和分母 $\beta^\alpha$ 消掉；$2^{-(\alpha-1)}\cdot 2^{-1}=2^{-\alpha}$：
$$f_Y(y)=\frac{1}{\Gamma(\alpha)2^\alpha}y^{\alpha-1}e^{-y/2}.$$

**Step 5：範圍與認分配。** $x>0$、$\beta>0$ ⇒ $y>0$。令 $\alpha=r/2$：
$$f_Y(y)=\frac{1}{\Gamma(r/2)2^{r/2}}y^{r/2-1}e^{-y/2},\quad y>0,$$
這是 $\chi^2(r)$ 的 pdf。∎

[▶ 10:24](https://youtu.be/WKIKv_BhN2g?t=624) 分配函數法的最後一步：從 pdf 的長相**判斷是什麼分配**。

---

## 2. mgf 唯一性定理

[▶ 11:28](https://youtu.be/WKIKv_BhN2g?t=688) 很重要的定理。

> **定理**：若 mgf 在 0 附近某區間存在，則 **mgf 和分配一對一對應**。
> 換句話說：兩個隨機變數的 mgf 在 0 附近相同 ⇔ 它們的分配相同。

【課本補充】課本 Theorem 1.9.2（p. 71）：$M_X(t)=M_Y(t)$ 對某個 $(-h,h)$ 內所有 $t$ 成立 ⇔ $F_X(z)=F_Y(z)$ 對所有 $z$ 成立。課本說證明超出本書範圍。老師也沒證。

[▶ 14:00](https://youtu.be/WKIKv_BhN2g?t=840) 意思：

- 一個分配只有一個 mgf；
- 一個 mgf 也只對應一個分配，不會有別的分配有同樣的 mgf。
- 所以**看到 mgf 就知道是什麼分配**。前面已經導出各分配的 mgf，查表就行。

**例**（[▶ 15:02](https://youtu.be/WKIKv_BhN2g?t=902)）：

- $f(x)=\dfrac{3^xe^{-3}}{x!}$，$x=0,1,2,\dots$ → 這是 Poisson$(3)$ → mgf $=e^{3(e^t-1)}$。
- 反過來，$M_X(t)=e^{100(e^t-1)}$ → 只有 Poisson 有這種 mgf → $X\sim\text{Poisson}(100)$。

[▶ 18:43](https://youtu.be/WKIKv_BhN2g?t=1123) 【口頭】比喻：班上 50 人編號 1 到 50，叫號碼就知道是誰，看到人就知道幾號，這是一對一。如果整排同學都叫 1 號，叫一個號碼好多人站起來，就不是一對一。

---

## 3. mgf 法

**做法**：要找 $Y=g(X)$ 的分配 → 照定義算 $M_Y(t)=E(e^{tY})$，用 $X$ 的 mgf 表示 → 認出是哪個分配的 mgf → 由唯一性，$Y$ 就是那個分配。

**常用技巧**：$X$ 的 mgf 是 $M_X(t)=E(e^{tX})$，這裡的 $t$ 可以換成任何實數。所以
$$E\left(e^{(\text{某實數})\cdot X}\right)=M_X(\text{某實數}).$$

### 3.1 標準化常態變數（mgf 法）

[▶ 19:43](https://youtu.be/WKIKv_BhN2g?t=1183) 再證一次 $X\sim N(\mu,\sigma^2)$ ⇒ $Z=\frac{X-\mu}{\sigma}\sim N(0,1)$。

目標：$N(0,1)$ 的 mgf 是 $e^{t^2/2}$（$\mu=0$、$\sigma^2=1$ 代入 $e^{\mu t+\sigma^2t^2/2}$）。

**Step 1：照定義**（[▶ 22:47](https://youtu.be/WKIKv_BhN2g?t=1367)）
$$M_Z(t)=E\left(e^{tZ}\right)=E\left(e^{t(X-\mu)/\sigma}\right)=E\left(e^{-\mu t/\sigma}\cdot e^{(t/\sigma)X}\right).$$

**Step 2：常數提出來**（[▶ 24:31](https://youtu.be/WKIKv_BhN2g?t=1471)）：$e^{-\mu t/\sigma}$ 是常數，$E(aW)=aE(W)$：
$$M_Z(t)=e^{-\mu t/\sigma}\,E\left(e^{(t/\sigma)X}\right).$$

**Step 3：認出 $X$ 的 mgf**（[▶ 25:33](https://youtu.be/WKIKv_BhN2g?t=1533)）：$E\left(e^{(t/\sigma)X}\right)=M_X(t/\sigma)$。$t/\sigma$ 還是實數，所以把 $M_X(t)=e^{\mu t+\sigma^2t^2/2}$ 的 $t$ 全換成 $t/\sigma$：
$$M_X\left(\frac t\sigma\right)=\exp\left(\mu\frac{t}{\sigma}+\frac{\sigma^2}{2}\frac{t^2}{\sigma^2}\right).$$

**Step 4：合併**（[▶ 29:36](https://youtu.be/WKIKv_BhN2g?t=1776)）：$-\mu t/\sigma$ 和 $+\mu t/\sigma$ 消掉；$\sigma^2$ 消掉：
$$M_Z(t)=e^{t^2/2},\qquad t\in\mathbb{R}.$$

**Step 5**：這是 $N(0,1)$ 的 mgf，由唯一性 $Z\sim N(0,1)$。∎

### 3.2 Gamma 變換成卡方（mgf 法）

[▶ 32:48](https://youtu.be/WKIKv_BhN2g?t=1968)

已知：$\Gamma(\alpha,\beta)$ 的 mgf 是 $(1-\beta t)^{-\alpha}$，$t<1/\beta$；$\chi^2(r)$ 的 mgf 是 $(1-2t)^{-r/2}$，$t<1/2$。

**Step 1**（[▶ 34:52](https://youtu.be/WKIKv_BhN2g?t=2092)）：
$$M_Y(t)=E\left(e^{tY}\right)=E\left(e^{(2t/\beta)X}\right)=M_X\left(\frac{2t}{\beta}\right).$$

**Step 2**（[▶ 36:58](https://youtu.be/WKIKv_BhN2g?t=2218)）：把 $t$ 換成 $2t/\beta$：
$$M_Y(t)=\left(1-\beta\cdot\frac{2t}{\beta}\right)^{-\alpha}=(1-2t)^{-\alpha}=(1-2t)^{-r/2}.$$
條件 $\frac{2t}{\beta}<\frac{1}{\beta}$，即 $t<\frac12$。

**Step 3**：這是 $\chi^2(r)$ 的 mgf（$r=2\alpha$），所以 $Y\sim\chi^2(r)$。∎

[▶ 38:00](https://youtu.be/WKIKv_BhN2g?t=2280) 【口頭】這種證明一定要會，常常會用到。

---

## 4. 為什麼要很多個隨機變數

[▶ 38:30](https://youtu.be/WKIKv_BhN2g?t=2310) 隨機變數是**可以被觀察的**：做一次實驗得到樣本點 $s$，隨機變數就發生一個值 $x=X(s)$。

[▶ 40:04](https://youtu.be/WKIKv_BhN2g?t=2404) 做統計通常不會只觀察一個 $X$。【口頭】例子：

- **選舉民調**：明年初選總統、立委。全台兩千多萬人，民調機構只找一千多到兩千人。每個受訪者都是一個隨機變數：還沒抽之前不知道是誰（從電話簿隨便抽）；抽出來問了，就有**觀察值**，不再是隨機的。
- **品質管制**（品管）：工廠每幾分鐘抽 3 到 5 個產品，看它們的平均。
- 不可能問遍兩千三百萬人，所以用統計。

> **統計的目的**：用少數樣本，了解背後的整體。

---

## 5. 隨機向量、聯合 pdf、邊際 pdf

[▶ 43:11](https://youtu.be/WKIKv_BhN2g?t=2591)

> **定義（隨機向量，random vector）**：$\mathbf{X}=(X_1,\dots,X_n)$，每個 $X_i$ 都是隨機變數。它是 $S\to\mathbb{R}^n$ 的函數：$s\mapsto(X_1(s),\dots,X_n(s))$。

只考慮全部離散或全部連續；一部分離散一部分連續的不考慮。

**聯合 pdf**（joint pdf，[▶ 44:13](https://youtu.be/WKIKv_BhN2g?t=2653)）：

- **離散**：$f(x_1,\dots,x_n)=P(X_1=x_1,\dots,X_n=x_n)$。
  - 照定義本來要去樣本空間找「$X_1(s)=x_1,\dots,X_n(s)=x_n$」的點再算 $P$；有了 joint pdf 就直接代。
- **連續**（[▶ 46:21](https://youtu.be/WKIKv_BhN2g?t=2781)）：先有**聯合分配函數**（joint distribution function）
  $$F(x_1,\dots,x_n)=P(X_1\le x_1,\dots,X_n\le x_n).$$
  若存在函數 $f$ 使
  $$F(x_1,\dots,x_n)=\int_{-\infty}^{x_n}\cdots\int_{-\infty}^{x_1}f(t_1,\dots,t_n)\,dt_1\cdots dt_n,$$
  $f$ 就叫 joint pdf。

[▶ 47:22](https://youtu.be/WKIKv_BhN2g?t=2842) 【口頭】這部分了解就好，不用背，不會考叫你寫這個定義。要知道的觀念：一個隨機變數有 pdf；好幾個一起有 joint pdf，代表**同時發生**的機會。

**邊際 pdf**（marginal pdf，[▶ 48:24](https://youtu.be/WKIKv_BhN2g?t=2904)）：每個 $X_i$ 自己的 pdf。「marginal」就是「個別」的意思。

**由 joint 求 marginal**（以兩個為例，[▶ 49:25](https://youtu.be/WKIKv_BhN2g?t=2965)）：把不要的變數「加掉」或「積掉」：
$$f_{X_1}(x_1)=\sum_{x_2}f(x_1,x_2)\quad\text{或}\quad\int_{-\infty}^{\infty}f(x_1,x_2)\,dx_2.$$
$f_{X_2}$ 同理，把 $x_1$ 加掉／積掉。

【口頭】這些是機率的內容，不太會考這種題目，但後面要用。接下來要探討隨機變數**之間的關係**，這是統計很重要的觀念。

[▶ 50:28](https://youtu.be/WKIKv_BhN2g?t=3028) 【口頭】分配一樣，值也通常不一樣：兩個微積分程度一樣的同學考同一份題目，成績不會一樣，今天考明天考也不一樣。連續型的話，相等的機率是 0。

---

## 6. 事件的獨立

[▶ 51:31](https://youtu.be/WKIKv_BhN2g?t=3091) 兩個事件「沒關係」，機率的名詞叫**獨立**（independent）。

> **定義**（課本 Definition 1.4.2，p. 29）：事件 $A,B\subset S$ 獨立，若
> $$P(A\cap B)=P(A)P(B).$$
> 「同時發生的機率＝個別機率相乘。」

【課堂討論】[▶ 52:35](https://youtu.be/WKIKv_BhN2g?t=3155) 老師問：$A\cap B=\varnothing$ 時，$A,B$ 獨立嗎？學生猜「沒關係就獨立」。

老師的答案：**通常不獨立**。因為 $A$ 發生了，$B$ 就一定不會發生；知道一個就知道另一個。表面上分開、沒關係，其實有關係。

（驗算，不是逐字稿內容，依定義推的：$P(A\cap B)=0$，所以獨立 ⇔ $P(A)P(B)=0$ ⇔ 至少一個機率是 0。兩個都有正機率時一定不獨立。）

[▶ 55:12](https://youtu.be/WKIKv_BhN2g?t=3312) 怪例子：$\varnothing$ 和 $\varnothing$ 獨立。$P(\varnothing\cap\varnothing)=0=0\cdot 0$。「一個東西跟它自己是獨立的。」

[▶ 55:43](https://youtu.be/WKIKv_BhN2g?t=3343) 【口頭】這門課一直在定義新名詞，後面的名詞都和前面有關。統計是一點一點觀念累積起來的；前面不懂，後面會很難懂。

---

## 7. 連續型：單點機率是 0

[▶ 56:45](https://youtu.be/WKIKv_BhN2g?t=3405) 兩個隨機變數 $X,Y$ 有 joint pdf $f(x,y)$，可以想成「$X=x$、$Y=y$ 同時發生的機會」。但連續型不能說它是機率。

【課堂討論】[▶ 57:45](https://youtu.be/WKIKv_BhN2g?t=3465) $X$ 連續，$P(X=x)=?$ 學生答 0。

**理由**：$P(X=x)=P(X\in\{x\})=\int_x^xf(t)\,dt=0$。機率是 pdf 下面的面積，一點只是一條線，沒有面積。

[▶ 59:19](https://youtu.be/WKIKv_BhN2g?t=3559) **機率 0 不表示不會發生**：每一點機率都是 0，但做實驗一定有結果，那個結果原本的機率就是 0。

【口頭】買彩券中獎機率幾乎是 0，但總有人中。中獎的人說是祖宗保佑、去拜神，「那麼多人在拜，為什麼只有一個人中？中的人也不一定有拜。」每個人機會都幾乎是 0，但總有一個會發生。

---

## 8. 隨機變數的獨立

[▶ 61:55](https://youtu.be/WKIKv_BhN2g?t=3715) $X,Y$ 有 joint pdf $f(x,y)$，各自有 marginal pdf $f_X(x)$、$f_Y(y)$。

> **定義（隨機變數獨立）**（課本 Definition 2.4.1，p. 118）：
> $$f(x,y)=f_X(x)f_Y(y),\qquad\text{對所有 }(x,y).$$

**為什麼這樣定義**（[▶ 62:57](https://youtu.be/WKIKv_BhN2g?t=3777)，以離散為例）：

- 左邊 $=P(X=x,Y=y)$，右邊 $=P(X=x)P(Y=y)$。
- 令 $A=\{X=x\}$、$B=\{Y=y\}$，這就是「$P(A\cap B)=P(A)P(B)$」，事件 $A,B$ 獨立。
- 不知道會發生哪個 $(x,y)$，所以要求 $\mathbb{R}^2$ 裡**每一個** $(x,y)$ 都成立。

[▶ 64:58](https://youtu.be/WKIKv_BhN2g?t=3898) 【口頭】所以兩個隨機變數獨立是**非常嚴格**的條件。

---

## 9. 同分配

[▶ 66:02](https://youtu.be/WKIKv_BhN2g?t=3962) 第二個名詞：**同分配**（identically distributed）。

**先想：兩個函數什麼時候相等？**（[▶ 66:37](https://youtu.be/WKIKv_BhN2g?t=3997)）

- $x^2$ 和 $x^3$：都是 $x$ 的函數，但不相等。
- $\cos x$ 和 $\sin x$：都叫三角函數，但不相等。
- $f(x)=x^2$ 和 $g(y)=y^2$：**相等**。因為相等是指「給同一個點，函數值一樣」：$f(x)=g(x)$ 對所有 $x$。變數名字不重要，型態一樣就相等。

> **定義（同分配）**（[▶ 68:12](https://youtu.be/WKIKv_BhN2g?t=4092)）：$X,Y$ 的 marginal pdf 是同一個函數，
> $$f_X(x)=f_Y(x),\qquad\text{對所有 }x.$$

- 兩個 pdf 的圖完全重疊：同一點發生的機會一樣。
- 縮寫 **i.d.**（identically distributed）。
- [▶ 70:16](https://youtu.be/WKIKv_BhN2g?t=4216) 同分配**不表示**兩個會發生同樣的值。

【課本補充】課本把它叫 **equal in distribution**（p. 40），並強調 $X$、$Y$ 同分配但可能根本不相等。獨立且同分配縮寫 **iid**（p. 152）。

---

## 10. 一頁速查表

**mgf 唯一性**：mgf 在 0 附近相同 ⇔ 分配相同。看到 mgf 就認得分配。

**mgf 法的關鍵技巧**：$E\left(e^{cX}\right)=M_X(c)$，把 $M_X$ 裡的 $t$ 換成 $c$。

| 結論 | mgf 法關鍵一步 |
|---|---|
| $\frac{X-\mu}{\sigma}\sim N(0,1)$ | $M_Z(t)=e^{-\mu t/\sigma}M_X(t/\sigma)=e^{t^2/2}$ |
| $X\sim\Gamma(\alpha,\beta)\Rightarrow\frac{2X}{\beta}\sim\chi^2(2\alpha)$ | $M_Y(t)=M_X(2t/\beta)=(1-2t)^{-\alpha}$ |

**分配函數法關鍵一步**（Gamma→卡方）：$F_Y(y)=\int_0^{\beta y/2}f_X$，微分乘 $\beta/2$，$\beta$ 全消。

**隨機向量**

- joint pdf：離散 $P(X_1=x_1,\dots)$；連續是 joint cdf 的被積函數。
- marginal：把其他變數加掉／積掉，$f_{X_1}(x_1)=\int f(x_1,x_2)\,dx_2$。

**獨立**

| | 定義 |
|---|---|
| 事件 | $P(A\cap B)=P(A)P(B)$ |
| 隨機變數 | $f(x,y)=f_X(x)f_Y(y)$，對所有 $(x,y)$ |

- 互斥（$A\cap B=\varnothing$）且機率都正 ⇒ **不**獨立。
- $\varnothing$ 和 $\varnothing$ 獨立。

**同分配**：$f_X=f_Y$（同一個函數）。不表示 $X=Y$。

**連續型**：$P(X=x)=0$，但機率 0 不表示不會發生。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| mgf 唯一性、mgf 法 | 證明獨立隨機變數之和的分配 |
| 獨立、同分配 | iid 隨機樣本、樣本平均 |
| joint / marginal pdf | 多變數變換、統計量的分配 |

---

## 附：本集一句話總結

> **mgf 和分配一對一，所以算出 $Y$ 的 mgf 就能認出 $Y$ 的分配（例如 $\frac{X-\mu}{\sigma}\sim N(0,1)$、$\frac{2X}{\beta}\sim\chi^2(2\alpha)$）；接著為多個隨機變數定義聯合 pdf、邊際 pdf、獨立（joint＝marginal 相乘）和同分配（marginal pdf 是同一個函數）。**

---

*筆記依據「統計學」Lec06 錄影逐字稿（whisper large-v3-turbo，1:11:13）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
