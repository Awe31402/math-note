---
course: 高等統計學（數理統計續）
episode: 1
lecture: Lec01（第一週 1/2）
date: 待補
video: https://youtu.be/6aRiVM2JAPU
notes: Hogg 8th ed. §2.7 多元變換（非一對一，p. 146 附近）；§4.4 順序統計量（Theorem 4.4.1，p. 254）
---

# 第 1 集 · 第一週 (1/2)：非一對一變換；順序統計量的 joint pdf [▶ 影片](https://youtu.be/6aRiVM2JAPU)

← 上一集：（無；接續[統計學 Lec27](../basic/27-lehmann-scheffe-proof-umvue-examples.md)） ｜ [總目錄](../README.md) ｜ 下一集：[02](02-order-statistics-marginal-pdf-min-max-jth.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 1 集
> **講者**：待補（和上學期「統計學」同一位老師）
> **來源**：YouTube 錄影逐字稿（54:40，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.7、§4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Jacobian」→「Jakobin／夾口餅／甲骨餅」，「反函數」→「法蘭素／法難數／緩緩數」，「joint」→「join／九文」，「iid」→「RID」，「機率」→「激勵／基率」。[▶ 38:42](https://youtu.be/6aRiVM2JAPU?t=2322)–[▶ 40:42](https://youtu.be/6aRiVM2JAPU?t=2442) 約 2 分鐘沒有講課內容（whisper 幻聽字），應是錄影中斷或休息。以下一律用正確的字。

---

## 目錄

- [0. 這門課要做什麼](#0-這門課要做什麼)
- [1. 複習：一對一變換公式](#1-複習一對一變換公式)
- [2. 順序統計量不是一對一](#2-順序統計量不是一對一)
- [3. 非一對一變換：切成幾塊](#3-非一對一變換切成幾塊)
- [4. 定理：順序統計量的 joint pdf](#4-定理順序統計量的-joint-pdf)
- [5. 證明（n＝3）](#5-證明n3)
- [6. 預告：marginal pdf 的公式](#6-預告marginal-pdf-的公式)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這門課要做什麼

[▶ 00:00](https://youtu.be/6aRiVM2JAPU?t=0) 這門課叫高等統計學，但其實和上學期的東西是**延續**的。

[▶ 00:35](https://youtu.be/6aRiVM2JAPU?t=35) 在講兩個重要主題之前，先介紹統計裡一個很重要的東西：**順序統計量的分配**。老師猜大家以前學機率時大多沒學過，所以重新介紹。

- 上學期只導過**最小**和**最大**順序統計量的 pdf（比較好導）。
- [▶ 01:06](https://youtu.be/6aRiVM2JAPU?t=66) 但有時要用中間某一個、或某兩個（例如第 3 和第 8 個的 joint pdf），所以要學一般的方法。

| 主題 | 課本 |
|---|---|
| 一對一變換（複習） | §2.7 |
| 非一對一變換：切塊、相加 | §2.7（p. 146 附近） |
| 順序統計量的 joint pdf $n!\prod f(y_i)$ | Theorem 4.4.1，p. 254 |

---

## 1. 複習：一對一變換公式

[▶ 02:09](https://youtu.be/6aRiVM2JAPU?t=129) $X_1,\dots,X_k$ 連續型，joint pdf $f(x_1,\dots,x_k)$。

- 如果是隨機樣本，joint pdf＝個別 pdf 相乘（每個都一樣）。現在不管是不是隨機樣本。

[▶ 03:42](https://youtu.be/6aRiVM2JAPU?t=222) 定義 $k$ 個新變數：$Y_i=h_i(X_1,\dots,X_k)$，$i=1,\dots,k$。$k$ 個變成 $k$ 個，而且**一對一**。

- 一對一 ⇒ 有反函數：$x_i=w_i(y_1,\dots,y_k)$。
- [▶ 06:47](https://youtu.be/6aRiVM2JAPU?t=407) Jacobian：$J=\det\left[\dfrac{\partial x_i}{\partial y_j}\right]$（$k\times k$ 矩陣的行列式）。

$$f_{\mathbf Y}(y_1,\dots,y_k)=f\left(w_1(\mathbf y),\dots,w_k(\mathbf y)\right)|J|.$$

[▶ 08:21](https://youtu.be/6aRiVM2JAPU?t=501) 還要找 $(Y_1,\dots,Y_k)$ 落在什麼範圍。

---

## 2. 順序統計量不是一對一

[▶ 08:51](https://youtu.be/6aRiVM2JAPU?t=531) 想找順序統計量的 joint pdf，但它**不是一對一**。

**例**（$n=2$）：$Y_1=\min(X_1,X_2)$，$Y_2=\max(X_1,X_2)$。

- [▶ 09:51](https://youtu.be/6aRiVM2JAPU?t=591) 畫 $(x_1,x_2)$ 平面和直線 $x_1=x_2$。右下 $x_1>x_2$，左上 $x_1<x_2$。
- 點 $(x_1,x_2)=(y_1,y_2)$（$y_1<y_2$）映到 $(\min,\max)=(y_1,y_2)$。
- 點 $(x_1,x_2)=(y_2,y_1)$ 也映到 $(y_1,y_2)$。
- [▶ 11:26](https://youtu.be/6aRiVM2JAPU?t=686) **兩點映成同一點** ⇒ 不是一對一。

---

## 3. 非一對一變換：切成幾塊

[▶ 12:58](https://youtu.be/6aRiVM2JAPU?t=778)

**想法**（$n=2$）：用直線 $x_1=x_2$ 把平面切成 $A_1$（$x_1<x_2$）和 $A_2$（$x_1>x_2$）。在**每一塊**上，變換都是一對一的。

> **非一對一變換**（[▶ 14:34](https://youtu.be/6aRiVM2JAPU?t=874)）：把 $(X_1,\dots,X_k)$ 的 space $A$ 切成（partition）$A_1,\dots,A_m$，使得在每一塊 $A_j$ 上，$(y_1,\dots,y_k)=h(\mathbf x)$ 都是一對一，映到同一個 $B$。第 $j$ 塊有自己的反函數 $w_{1j},\dots,w_{kj}$ 和 Jacobian $J_j$。則
> $$f_{\mathbf Y}(\mathbf y)=\sum_{j=1}^mf\left(w_{1j}(\mathbf y),\dots,w_{kj}(\mathbf y)\right)|J_j|,\qquad\mathbf y\in B.$$

- 每一塊個別轉換出來的東西**不是** pdf；**加起來**才是 pdf。
- 切幾塊（$m$）看問題而定。

【口頭】[▶ 18:09](https://youtu.be/6aRiVM2JAPU?t=1089) Hogg and Craig 那本書的習題就有這種不是一對一、要你做轉換的題目。

---

## 4. 定理：順序統計量的 joint pdf

[▶ 18:39](https://youtu.be/6aRiVM2JAPU?t=1119) $X_1,\dots,X_n$ 是隨機樣本（iid），來自**連續**分配，pdf $f(x)$，$a<x<b$。

順序統計量：$Y_1<Y_2<\cdots<Y_n$，$Y_1$ 最小、$Y_n$ 最大；$Y_j$ 叫第 $j$ 個順序統計量。

[▶ 23:50](https://youtu.be/6aRiVM2JAPU?t=1430) $n$ 維空間要切成**幾塊**？$n=2$ 切 2 塊（$2!$），$n=3$ 切 6 塊（$3!$），一般是 **$n!$** 塊。而且每塊轉換出來的函數都一樣。

> **定理**（課本 Theorem 4.4.1，p. 254）：
> $$f_{Y_1,\dots,Y_n}(y_1,\dots,y_n)=\begin{cases}n!\,f(y_1)f(y_2)\cdots f(y_n), & a<y_1<y_2<\cdots<y_n<b\\ 0, & \text{其他}\end{cases}$$

- [▶ 26:24](https://youtu.be/6aRiVM2JAPU?t=1584) $f(y_1)\cdots f(y_n)$ 就是原本 joint pdf $f(x_1)\cdots f(x_n)$ 把 $x$ 換成 $y$。
- [▶ 27:25](https://youtu.be/6aRiVM2JAPU?t=1645) 範圍：$Y_1$ 最小所以 $<Y_2<\cdots<Y_n$；原本都在 $(a,b)$。
- 等號寫不寫都沒關係：連續型，排序後還是連續型，等號那些點沒有機率。

---

## 5. 證明（n＝3）

[▶ 28:27](https://youtu.be/6aRiVM2JAPU?t=1707) 只證 $n=3$（比較容易；$n=4,5$ 也能證，只是比較麻煩）。

**Step 1：原本的 joint pdf**（[▶ 28:57](https://youtu.be/6aRiVM2JAPU?t=1737)）。iid ⇒
$$f(x_1,x_2,x_3)=f(x_1)f(x_2)f(x_3),\qquad A=\{a<x_i<b,\ i=1,2,3\}.$$

【口頭】[▶ 30:31](https://youtu.be/6aRiVM2JAPU?t=1831) 隨機樣本是獨立的，$X_1$ 落在哪裡和 $X_2$ 無關；但順序統計量不是，$Y_1$ 不可能比 $Y_2$ 大，它們一定有關係。

**Step 2：切成 $3!=6$ 塊**（[▶ 31:02](https://youtu.be/6aRiVM2JAPU?t=1862)）。$x_1,x_2,x_3$ 的大小順序有 6 種排法：

| 塊 | 條件 | 反函數 $(x_1,x_2,x_3)=$ | $J$ |
|---|---|---|---|
| $A_1$ | $x_1<x_2<x_3$ | $(y_1,y_2,y_3)$ | $1$ |
| $A_2$ | $x_2<x_1<x_3$ | $(y_2,y_1,y_3)$ | $-1$ |
| $A_3$ | $x_1<x_3<x_2$ | $(y_1,y_3,y_2)$ | $-1$ |
| $A_4$ | $x_2<x_3<x_1$ | $(y_3,y_1,y_2)$ | $1$ |
| $A_5$ | $x_3<x_1<x_2$ | $(y_2,y_3,y_1)$ | $1$ |
| $A_6$ | $x_3<x_2<x_1$ | $(y_3,y_2,y_1)$ | $-1$ |

- [▶ 32:06](https://youtu.be/6aRiVM2JAPU?t=1926) 例 $A_1$：$x_1$ 最小 ⇒ 映到 $y_1$；$x_2$ 第二 ⇒ $y_2$；$x_3$ 最大 ⇒ $y_3$。反過來給定 $(y_1,y_2,y_3)$，$x_1=y_1$……。
- [▶ 32:37](https://youtu.be/6aRiVM2JAPU?t=1957) 例 $A_2$：$x_2$ 最小 ⇒ $x_2=y_1$；$x_1$ 第二 ⇒ $x_1=y_2$；$x_3=y_3$。
- 每一塊都映到 $B=\{a<y_1<y_2<y_3<b\}$，而且一對一。

**Step 3：Jacobian**（[▶ 35:45](https://youtu.be/6aRiVM2JAPU?t=2145)）。每塊的反函數只是把 $y$ 重新排列，所以 Jacobian 矩陣是**排列矩陣**（每列每行恰一個 1），行列式是 $\pm 1$。

- $A_1$：單位矩陣，$J_1=1$。
- [▶ 36:47](https://youtu.be/6aRiVM2JAPU?t=2207) $A_2$：$x_1=y_2,x_2=y_1,x_3=y_3$，矩陣 $\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}$，$J_2=-1$。
- $A_3$：$x_1=y_1,x_2=y_3,x_3=y_2$，$J_3=-1$。

**Step 4：相加**（[▶ 41:44](https://youtu.be/6aRiVM2JAPU?t=2504)）
$$f_{\mathbf Y}(\mathbf y)=\sum_{j=1}^6f(w_{1j})f(w_{2j})f(w_{3j})|J_j|.$$

- [▶ 44:54](https://youtu.be/6aRiVM2JAPU?t=2694) 每一項都是 $f(y_1),f(y_2),f(y_3)$ 換順序相乘，乘起來一樣：$f(y_1)f(y_2)f(y_3)$。
- 每個 $|J_j|=1$。
- 共 6 項。

$$f_{\mathbf Y}(y_1,y_2,y_3)=3!\,f(y_1)f(y_2)f(y_3),\qquad a<y_1<y_2<y_3<b.\qquad\blacksquare$$

[▶ 45:57](https://youtu.be/6aRiVM2JAPU?t=2757) 一般 $n$：切 $n!$ 塊，每塊的函數都是 $\prod f(y_i)$，$|J|$ 都是 1，加起來得 $n!\prod f(y_i)$。

---

## 6. 預告：marginal pdf 的公式

[▶ 47:33](https://youtu.be/6aRiVM2JAPU?t=2853) 有了 joint pdf，想要：$Y_1$、$Y_n$、$Y_j$ 的 pdf；$Y_i,Y_j$ 的 joint pdf。

**要用的積分**（[▶ 48:03](https://youtu.be/6aRiVM2JAPU?t=2883)）：$F$ 是 $X$ 的分配函數（連續型 $F'=f$），$F(a)=0$、$F(b)=1$：
$$\int_y^bf(t)\,dt=1-F(y),\qquad\int_a^yf(t)\,dt=F(y).$$

**第 $j$ 個的 pdf 怎麼記**（[▶ 50:07](https://youtu.be/6aRiVM2JAPU?t=3007)）：從 joint pdf 把其他的積掉。

- $y_j$ **下面**有 $j-1$ 個要積，都從 $a$ 開始積 → 每個得 $F(y_j)$ → $[F(y_j)]^{j-1}$，分母出現 $(j-1)!$。
- $y_j$ **上面**有 $n-j$ 個要積，都積到 $b$ → 每個得 $1-F(y_j)$ → $[1-F(y_j)]^{n-j}$，分母出現 $(n-j)!$。
- $f(y_j)$ 不積，留著。

$$f_{Y_j}(y)=\frac{n!}{(j-1)!\,(n-j)!}[F(y)]^{j-1}[1-F(y)]^{n-j}f(y),\quad a<y<b.$$

特例（[▶ 52:39](https://youtu.be/6aRiVM2JAPU?t=3159)）：

- $j=1$：$f_{Y_1}(y)=n[1-F(y)]^{n-1}f(y)$（上學期導過）。
- $j=n$：$f_{Y_n}(y)=n[F(y)]^{n-1}f(y)$。

證明下次講。【口頭】公式很好記，因為你就是這樣積分才得到的。

---

## 7. 一頁速查表

**非一對一變換**：把 space 切成 $A_1,\dots,A_m$，每塊一對一，
$$f_{\mathbf Y}(\mathbf y)=\sum_{j=1}^mf(\mathbf w_j(\mathbf y))|J_j|.$$

**順序統計量 joint pdf**：
$$f_{Y_1,\dots,Y_n}(\mathbf y)=n!\prod_{i=1}^nf(y_i),\quad a<y_1<\cdots<y_n<b.$$
關鍵：切 $n!$ 塊（所有排列），每塊反函數是排列、$|J|=1$、函數值都是 $\prod f(y_i)$。

**積分**：$\int_a^yf=F(y)$，$\int_y^bf=1-F(y)$。

**第 $j$ 個**（下次證）：
$$f_{Y_j}(y)=\frac{n!}{(j-1)!(n-j)!}F(y)^{j-1}[1-F(y)]^{n-j}f(y).$$

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 第 $j$ 個、任兩個順序統計量的 pdf | 下一集證明 |
| 順序統計量 | 樣本中位數、全距、分位數的分配；無母數方法 |

---

## 附：本集一句話總結

> **順序統計量不是一對一變換，做法是把樣本空間依大小順序切成 $n!$ 塊，每塊一對一、Jacobian 絕對值是 1、函數值都是 $\prod f(y_i)$，加起來得 joint pdf $n!\,f(y_1)\cdots f(y_n)$（$y_1<\cdots<y_n$）。**

---

*筆記依據「高等統計學」Lec01 錄影逐字稿（whisper large-v3-turbo，54:40）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
