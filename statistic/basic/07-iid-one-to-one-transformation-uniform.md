---
course: 統計學（數理統計，數學系）
episode: 7
lecture: Lec07
date: 待補
video: https://youtu.be/dRC87g-p5cs
notes: Hogg 8th ed. §2.4 獨立（Definition 2.4.1，p. 118）；iid（p. 152）；§1.7.2 一對一變換定理（Theorem 1.7.1，p. 55）；均勻分配（p. 50）
---

# 第 7 集 · Lec07：iid；連續型一對一變換公式；均勻分配 [▶ 影片](https://youtu.be/dRC87g-p5cs)

← 上一集：[06](06-mgf-uniqueness-random-vectors-independence.md) ｜ [總目錄](../README.md) ｜ 下一集：[08](08-multivariate-transformation-jacobian.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 7 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（26:36，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.7.2、§2.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「iid」→「RID」，「joint」→「Jone／join」，「遞增／遞減」→「地增／地減」，「微積分基本定理」→「微基因基本定義」，「$g^{-1}$」→「G inverse／Gin versus／基因不是」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：獨立、同分配，合起來叫 iid](#1-複習獨立同分配合起來叫-iid)
- [2. 一對一變換公式](#2-一對一變換公式)
  - [2.1 定理](#21-定理)
  - [2.2 範圍很重要](#22-範圍很重要)
  - [2.3 證明：g 遞增](#23-證明g-遞增)
  - [2.4 證明：g 遞減](#24-證明g-遞減)
- [3. 均勻分配](#3-均勻分配)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本對應 |
|---|---|
| iid＝獨立＋同分配 | p. 152 |
| 連續型隨機變數的一對一變換公式 | Theorem 1.7.1，p. 55 |
| 均勻分配 $U(a,b)$ | p. 50 |

---

## 1. 複習：獨立、同分配，合起來叫 iid

[▶ 00:32](https://youtu.be/dRC87g-p5cs?t=32)

**獨立**（independent，縮寫 I）：$f(x,y)=f_X(x)f_Y(y)$，對所有 $(x,y)$。

[▶ 01:05](https://youtu.be/dRC87g-p5cs?t=65) **反過來用**：已知 $X,Y$ 獨立，又知道各自的 pdf（marginal pdf），joint pdf 就是兩個**乘起來**。

**同分配**（identically distributed，縮寫 i.d.，[▶ 02:07](https://youtu.be/dRC87g-p5cs?t=127)）：$f_X(x)=f_Y(x)$，對所有 $x$。

- 同一點發生的機會一模一樣。
- 注意寫法：是 $f_Y(x)$，不是 $f_Y(y)$。要在**同一點**比較。

> **iid**（independent and identically distributed，[▶ 03:10](https://youtu.be/dRC87g-p5cs?t=190)）：獨立而且同分配。

【口頭】統計會一直用這個觀念：$n$ 個 iid 隨機變數。

---

## 2. 一對一變換公式

[▶ 04:14](https://youtu.be/dRC87g-p5cs?t=254) 主題：變數變換（transformation）。

前面用分配函數法、mgf 法找 $Y=g(X)$ 的分配，都是針對**特定分配**。現在要一個**一般公式**，針對連續型、一對一的變換。

### 2.1 定理

[▶ 05:15](https://youtu.be/dRC87g-p5cs?t=315)

設定：

- $X$ 是連續型隨機變數，pdf $f_X(x)$。
- [▶ 05:45](https://youtu.be/dRC87g-p5cs?t=345) $A=X(S)$ 是 $X$ 的**值域**（$\mathbb{R}$ 只是對應域，不一定是值域）。在 $A$ 裡 $f_X>0$，$A$ 外 $f_X=0$。
- $y=g(x)$ 可微分、**一對一**。所以有反函數 $x=g^{-1}(y)$。

> **定理**（課本 Theorem 1.7.1，p. 55）：$Y=g(X)$ 的 pdf 為
> $$f_Y(y)=\begin{cases}f_X\left(g^{-1}(y)\right)\left|\dfrac{d}{dy}g^{-1}(y)\right|, & y\in g(A)\\ 0, & \text{其他}\end{cases}$$

[▶ 07:47](https://youtu.be/dRC87g-p5cs?t=467) 【口頭】公式裡沒說 $X$ 是常態、Poisson 還是什麼。只要 $X$ 連續、$g$ 一對一可微，就能直接套，不用再用分配函數法或 mgf 法。

**怎麼記**：

1. 原來 $X$ 的 pdf，把 $x$ 換成 $g^{-1}(y)$。
2. 乘上反函數對 $y$ 的導數。
3. 導數可能是負的，pdf 不能負，所以取**絕對值**。

【課本補充】課本把 $\frac{dx}{dy}=\frac{d}{dy}g^{-1}(y)$ 叫這個變換的 **Jacobian**，記作 $J$。

### 2.2 範圍很重要

[▶ 08:48](https://youtu.be/dRC87g-p5cs?t=528)

- $X$ 的 pdf 只在值域 $A$ 大於 0。
- 所以 $Y=g(X)$ 只在 $g(A)$ 大於 0；$g(A)$ 以外不會發生，pdf 是 0。

[▶ 10:19](https://youtu.be/dRC87g-p5cs?t=619) 【口頭】範圍弄錯，整個積分就不會等於 1。積分大於 1 或小於 1，表示範圍錯了（當然也可能 pdf 找錯）。

### 2.3 證明：g 遞增

[▶ 12:27](https://youtu.be/dRC87g-p5cs?t=747) 用分配函數法：$X$ 連續、$g$ 可微，所以 $Y$ 也連續，分配函數微分就是 pdf。

$$F_Y(y)=P(Y\le y)=P\left(g(X)\le y\right).$$

難點：$g(X)\le y$ 對應哪些 $x$？要看 $g$ 的形狀。[▶ 13:33](https://youtu.be/dRC87g-p5cs?t=813) 一對一（連續）函數不是遞增就是遞減。

**情形 1：$g$ 遞增**（反函數也遞增）

[▶ 14:03](https://youtu.be/dRC87g-p5cs?t=843) 看圖：$x_1<x_2$ ⇒ $g(x_1)<g(x_2)$。所以

$$g(x)\le y\iff x\le g^{-1}(y).$$

（$y$ 軸上 $\le y$ 的那一段，對應回 $x$ 軸就是 $\le g^{-1}(y)$ 的那一段。兩個事件一樣，機率一樣。）

$$F_Y(y)=P\left(X\le g^{-1}(y)\right)=\int_{-\infty}^{g^{-1}(y)}f_X(x)\,dx.$$

[▶ 16:37](https://youtu.be/dRC87g-p5cs?t=997) 微分（微積分基本定理＋連鎖律）：
$$f_Y(y)=f_X\left(g^{-1}(y)\right)\cdot\frac{d}{dy}g^{-1}(y).$$

$g^{-1}$ 遞增 ⇒ 導數 $>0$ ⇒ 等於它的絕對值。和定理一樣。

### 2.4 證明：g 遞減

[▶ 18:08](https://youtu.be/dRC87g-p5cs?t=1088)

**情形 2：$g$ 遞減**（反函數也遞減）

[▶ 19:39](https://youtu.be/dRC87g-p5cs?t=1179) 看圖：$x_1<x_2$ ⇒ $g(x_1)>g(x_2)$。越大的 $x$，$y$ 越小。所以

$$g(x)\le y\iff x\ge g^{-1}(y).$$

[▶ 21:43](https://youtu.be/dRC87g-p5cs?t=1303) 用補集合：
$$F_Y(y)=P\left(X\ge g^{-1}(y)\right)=1-P\left(X<g^{-1}(y)\right)=1-\int_{-\infty}^{g^{-1}(y)}f_X(x)\,dx.$$

【口頭】$\ge$ 的補集合是 $<$，寫不寫等號都沒關係，因為連續型單點機率是 0。

[▶ 22:43](https://youtu.be/dRC87g-p5cs?t=1363) 微分：1 的微分是 0：
$$f_Y(y)=-f_X\left(g^{-1}(y)\right)\cdot\frac{d}{dy}g^{-1}(y).$$

$g^{-1}$ 遞減 ⇒ 導數 $<0$，前面又有負號，負負得正：
$$f_Y(y)=f_X\left(g^{-1}(y)\right)\left|\frac{d}{dy}g^{-1}(y)\right|.$$

兩種情形合起來就是定理。∎

---

## 3. 均勻分配

[▶ 23:44](https://youtu.be/dRC87g-p5cs?t=1424) 例題下次講，先定義一個分配。

【口頭】uniform 中文常叫「制服」：大家穿得一模一樣。在機率裡，uniform 分配就是**每一點機會都一樣**。

> **均勻分配**（uniform distribution）：$X\sim U(a,b)$，
> $$f(x)=\begin{cases}\dfrac{1}{b-a}, & a<x<b\\ 0, & \text{其他}\end{cases}$$

- $U$ 後面的 $(a,b)$ 是範圍：在 $(a,b)$ 裡每一點機會相同，外面不可能發生。
- [▶ 25:18](https://youtu.be/dRC87g-p5cs?t=1518) 為什麼是 $\frac{1}{b-a}$？
  1. 機會相同 → pdf 是常數 $c$。
  2. 要是 pdf：$c>0$，而且 $\int_a^bc\,dx=c(b-a)=1$ ⇒ $c=\frac{1}{b-a}$。

---

## 4. 一頁速查表

**iid**：獨立（$f(x,y)=f_X(x)f_Y(y)$）＋ 同分配（$f_X(x)=f_Y(x)$）。獨立時 joint pdf＝marginal 相乘。

**一對一變換公式**（$X$ 連續，$g$ 一對一可微，$A$ 是 $X$ 的值域）

$$f_Y(y)=f_X\left(g^{-1}(y)\right)\left|\frac{dg^{-1}(y)}{dy}\right|,\quad y\in g(A).$$

關鍵一步：

| | $g(X)\le y$ 等價於 | $F_Y(y)$ | 微分後的符號 |
|---|---|---|---|
| $g$ 遞增 | $X\le g^{-1}(y)$ | $\int_{-\infty}^{g^{-1}(y)}f_X$ | 導數 $>0$ |
| $g$ 遞減 | $X\ge g^{-1}(y)$ | $1-\int_{-\infty}^{g^{-1}(y)}f_X$ | 負號 × 導數 $<0$ ＝ 正 |

**檢查**：範圍 $g(A)$ 弄錯 → 積分不等於 1。

**均勻分配**：$U(a,b)$，$f(x)=\frac{1}{b-a}$，$a<x<b$（常數，且積分＝1）。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 一對一變換公式 | 下一集的例題（從均勻分配出發） |
| iid | 隨機樣本、樣本平均的分配 |
| 均勻分配 | 變換例題、機率積分變換 |

---

## 附：本集一句話總結

> **iid 是獨立加同分配；連續型隨機變數經一對一可微變換 $Y=g(X)$ 後，$f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|$（在 $g(A)$ 上），證明分 $g$ 遞增、遞減兩種用分配函數法。**

---

*筆記依據「統計學」Lec07 錄影逐字稿（whisper large-v3-turbo，26:36）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
