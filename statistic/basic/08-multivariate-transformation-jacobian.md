---
course: 統計學（數理統計，數學系）
episode: 8
lecture: Lec08
date: 待補
video: https://youtu.be/4p_eZcGVUSE
notes: Hogg 8th ed. §1.7.2 Example（$-2\log X$）；§3.3.1 卡方 pdf；§2.2 二元變換（p. 100）；§2.7 多元變換（p. 143）
---

# 第 8 集 · Lec08：$-2\log X$ 是卡方；多個隨機變數的變換與 Jacobian [▶ 影片](https://youtu.be/4p_eZcGVUSE)

← 上一集：[07](07-iid-one-to-one-transformation-uniform.md) ｜ [總目錄](../README.md) ｜ 下一集：[09](09-transformation-example-random-sample-statistic-mgf-independence.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 8 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（29:18，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.2、§2.7、§3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Jacobian」→「Jakobin／加科病／夾架餅」，「joint」→「Join／9np」，「行列式」→「行類式」，「卡方」→「卡荒」，「all」＝「2」，「反函數」→「緩藍素／反彈數」，「映」→「印／因」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例：X～U(0,1)，Y＝−2 log X](#1-例xu01y2-log-x)
- [2. 問題：n 個隨機變數變成 m 個](#2-問題n-個隨機變數變成-m-個)
- [3. 做法：補成 n 個、一對一](#3-做法補成-n-個一對一)
- [4. 為什麼可以：連續型 joint pdf 的意義](#4-為什麼可以連續型-joint-pdf-的意義)
- [5. Jacobian 與變換公式](#5-jacobian-與變換公式)
- [6. 最常用：兩個變數的情形](#6-最常用兩個變數的情形)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本對應 |
|---|---|
| 認分配：$\frac12 e^{-y/2}$ 是 $\chi^2(2)$ | §3.3.1 |
| $n$ 個連續隨機變數 → $m$ 個：補成一對一、用 Jacobian | §2.2，p. 100；§2.7，p. 143 |

---

## 1. 例：X～U(0,1)，Y＝−2 log X

[▶ 00:00](https://youtu.be/4p_eZcGVUSE?t=0) 老師說「上一次」已經導出 $Y=-2\log X$ 的 pdf，這集一開始直接看結果、判斷是什麼分配。

⚠️ 待確認：上一集（Lec07）錄影最後說「例題下一次再講」就結束了，這集開頭已經有結果。推導過程可能在兩支影片之間沒錄到。以下推導**不是逐字稿內容**，是依上一集的一對一變換公式補的。

**推導（補）**：

- $X\sim U(0,1)$：$f_X(x)=1$，$0<x<1$。值域 $A=(0,1)$。
- $y=g(x)=-2\log x$ 在 $(0,1)$ 上遞減、一對一。$g(A)=(0,\infty)$。
- 反函數：$x=g^{-1}(y)=e^{-y/2}$；$\dfrac{dx}{dy}=-\dfrac12e^{-y/2}$。
- 公式：
$$f_Y(y)=f_X\left(e^{-y/2}\right)\left|-\frac12e^{-y/2}\right|=\frac12e^{-y/2},\qquad y>0.$$

**判斷是什麼分配**（[▶ 01:03](https://youtu.be/4p_eZcGVUSE?t=63)）：

【口頭】有時候結果是已知的分配，要認得出來；認不出來就照寫。

- 看到 $e^{-(\text{某數})y}$ → 一定跟 Gamma 或卡方有關。
- Gamma pdf：$\dfrac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}$。
  - 沒有 $x^{\alpha-1}$ 那一項 → $\alpha=1$。
  - 指數是 $-y/2$ → $\beta=2$ → 是卡方。
- 卡方 pdf（[▶ 03:12](https://youtu.be/4p_eZcGVUSE?t=192)）：$\dfrac{1}{\Gamma(r/2)2^{r/2}}x^{r/2-1}e^{-x/2}$。$\alpha=r/2=1$ ⇒ $r=2$。代入：$\Gamma(1)=1$、$2^1=2$、$x^0=1$，得 $\frac12e^{-x/2}$。✓

所以
$$Y=-2\log X\sim\chi^2(2).$$

【口頭】要記得卡方的 pdf，不然不會判斷。

---

## 2. 問題：n 個隨機變數變成 m 個

[▶ 04:13](https://youtu.be/4p_eZcGVUSE?t=253) 一對一變換其實**不常發生**。最常發生的是：

- 有 $X_1,X_2$ 兩個隨機變數（有 joint pdf $f(x_1,x_2)$，和各自的 marginal pdf）。
- 定一個 $Y=X_1X_2$（或 $X_1+X_2$、$X_1-X_2$、$X_1/X_2$……）。
- 想要 $Y$ 的 pdf。

[▶ 06:15](https://youtu.be/4p_eZcGVUSE?t=375) $X_1,X_2$ 是實數函數，相乘還是實數函數，所以 $Y$ 是隨機變數，一定有 pdf。

**一般形式**（[▶ 06:46](https://youtu.be/4p_eZcGVUSE?t=406)）：$n$ 個**連續型**隨機變數 $X_1,\dots,X_n$，變成 $m$ 個（$m<n$）：

$$Y_1=g_1(X_1,\dots,X_n),\ \dots,\ Y_m=g_m(X_1,\dots,X_n),$$

即 $(g_1,\dots,g_m):\mathbb{R}^n\to\mathbb{R}^m$。要找 $Y_1,\dots,Y_m$ 的 joint pdf。

---

## 3. 做法：補成 n 個、一對一

[▶ 08:47](https://youtu.be/4p_eZcGVUSE?t=527) $m<n$ 沒辦法直接做。要**擴充**到 $n$ 個：

1. 自己再定 $Y_{m+1}=g_{m+1}(X_1,\dots,X_n)$，…，$Y_n=g_n(X_1,\dots,X_n)$。
2. 要定得讓 $(g_1,\dots,g_n):\mathbb{R}^n\to\mathbb{R}^n$ 是**一對一**。
3. 用下面的公式求 $Y_1,\dots,Y_n$ 的 joint pdf。
4. 把多出來的 $y_{m+1},\dots,y_n$ **積掉**，剩下 $Y_1,\dots,Y_m$ 的 joint pdf。

[▶ 09:47](https://youtu.be/4p_eZcGVUSE?t=587) **例**：$Y_1=X_1X_2$ 是 $\mathbb{R}^2\to\mathbb{R}$。再定一個 $Y_2$（可以是 $X_1$、$X_1+X_2$……隨你定），但要讓 $(Y_1,Y_2):\mathbb{R}^2\to\mathbb{R}^2$ 一對一。

---

## 4. 為什麼可以：連續型 joint pdf 的意義

[▶ 12:21](https://youtu.be/4p_eZcGVUSE?t=741)

> **連續型 joint pdf**：$X_1,\dots,X_n$ 連續型，若存在 $f\ge 0$，使得對 $\mathbb{R}^n$ 的任何子集 $A$，
> $$P\left((X_1,\dots,X_n)\in A\right)=\int\!\cdots\!\int_A f(x_1,\dots,x_n)\,dx_1\cdots dx_n,$$
> 則 $f$ 就是它們的 joint pdf。

- 以前用分配函數定義（$A=(-\infty,x_1]\times\cdots$），理論上可以擴充到任何集合。
- [▶ 13:54](https://youtu.be/4p_eZcGVUSE?t=834) 兩個方向都要會用：
  - 知道 joint pdf → 落在 $A$ 的機率就積分。
  - 不知道 joint pdf → 如果「落在任何 $A$ 的機率都等於某個非負函數的積分」，那個函數**就是** joint pdf。

---

## 5. Jacobian 與變換公式

[▶ 14:55](https://youtu.be/4p_eZcGVUSE?t=895) 一對一 ⇒ 有反函數：

$$x_1=w_1(y_1,\dots,y_n),\ \dots,\ x_n=w_n(y_1,\dots,y_n).$$

> **Jacobian**（[▶ 15:58](https://youtu.be/4p_eZcGVUSE?t=958)）：
> $$J=\det\begin{pmatrix}\dfrac{\partial x_1}{\partial y_1} & \cdots & \dfrac{\partial x_1}{\partial y_n}\\ \vdots & & \vdots\\ \dfrac{\partial x_n}{\partial y_1} & \cdots & \dfrac{\partial x_n}{\partial y_n}\end{pmatrix}$$
> 第 $i$ 列是 $x_i$ 對 $y_1,\dots,y_n$ 的偏微分。$J$ 可能正也可能負。

**推導**（[▶ 17:00](https://youtu.be/4p_eZcGVUSE?t=1020)）：

**Step 1**：$(X_1,\dots,X_n)$ 落在 $A$ 的機率：
$$P(\mathbf{X}\in A)=\int_A f_{\mathbf X}(x_1,\dots,x_n)\,d\mathbf{x}.$$

**Step 2**：多重積分的變數變換（高等微積分）：
$$=\int_{g(A)}f_{\mathbf X}\left(w_1(\mathbf y),\dots,w_n(\mathbf y)\right)|J|\,d\mathbf{y}.$$
$g(A)=\{(g_1(\mathbf x),\dots,g_n(\mathbf x)):\mathbf x\in A\}$：把 $A$ 裡每個點都映過去的集合。

**Step 3**（[▶ 20:41](https://youtu.be/4p_eZcGVUSE?t=1241)）：

- 左邊 $=P(\mathbf Y\in g(A))$（$\mathbf X\in A$ 和 $\mathbf Y\in g(A)$ 是同一個事件）。
- 右邊被積函數 $\ge 0$（joint pdf $\ge 0$，$|J|\ge 0$）。
- 所以「$\mathbf Y$ 落在任何集合的機率＝這個非負函數的積分」。由 §4，它就是 $\mathbf Y$ 的 joint pdf。

> **變換公式**：
> $$f_{\mathbf Y}(y_1,\dots,y_n)=f_{\mathbf X}\left(w_1(\mathbf y),\dots,w_n(\mathbf y)\right)|J|,\qquad \mathbf y\in g(A);\ \text{其他為 }0.$$

[▶ 22:43](https://youtu.be/4p_eZcGVUSE?t=1363) 【口頭】這是高等微積分多重積分的做法，就是因為這個理論，裡面那個函數就是 joint pdf。

**Step 4**（[▶ 24:14](https://youtu.be/4p_eZcGVUSE?t=1454)）：只要 $Y_1,\dots,Y_m$，就把 $y_{m+1},\dots,y_n$ 積掉：
$$f_{Y_1,\dots,Y_m}(y_1,\dots,y_m)=\int\!\cdots\!\int f_{\mathbf Y}(y_1,\dots,y_n)\,dy_{m+1}\cdots dy_n.$$

---

## 6. 最常用：兩個變數的情形

[▶ 24:45](https://youtu.be/4p_eZcGVUSE?t=1485)

設 $X_1,X_2$ 連續，joint pdf $f(x_1,x_2)$，**space**（joint pdf 大於 0 的範圍）是 $A$。
$Y_1=g_1(X_1,X_2)$、$Y_2=g_2(X_1,X_2)$ 一對一，反函數 $x_1=w_1(y_1,y_2)$、$x_2=w_2(y_1,y_2)$。

$$J=\det\begin{pmatrix}\dfrac{\partial x_1}{\partial y_1} & \dfrac{\partial x_1}{\partial y_2}\\[2mm] \dfrac{\partial x_2}{\partial y_1} & \dfrac{\partial x_2}{\partial y_2}\end{pmatrix},$$

$$f_{Y_1,Y_2}(y_1,y_2)=f\left(w_1(y_1,y_2),w_2(y_1,y_2)\right)|J|,\qquad (y_1,y_2)\in g(A).$$

**做題步驟**（[▶ 26:49](https://youtu.be/4p_eZcGVUSE?t=1609)）：

1. **先找 joint pdf**。題目常只給 $X_1,X_2$ 各自的 pdf，沒給 joint pdf（例如獨立時就相乘）。
2. **找 space $A$**：joint pdf 在哪裡大於 0。
3. 定 $Y_1,Y_2$，**確認一對一**。
4. 找反函數、算 Jacobian。
5. **找 $g(A)$**：$(Y_1,Y_2)$ 的值域，就是 $Y$ 的 joint pdf 大於 0 的範圍。
6. 套公式；要 marginal 就積掉另一個。

[▶ 27:49](https://youtu.be/4p_eZcGVUSE?t=1669) 【口頭】**範圍為什麼重要**：例如要 $Y_1$ 的 marginal pdf，要對 $y_2$ 積分。不能每次都從 $-\infty$ 積到 $\infty$——函數可能只在某一部分大於 0，等於 0 的部分不能拿那個公式去積。範圍弄錯，積出來的 pdf 總積分就不是 1，表示積錯了。

例子下次講。

---

## 7. 一頁速查表

**認分配**：$\frac12e^{-y/2}$（$y>0$）＝$\chi^2(2)$＝$\Gamma(1,2)$。
$X\sim U(0,1)$ ⇒ $-2\log X\sim\chi^2(2)$（$x=e^{-y/2}$，$|dx/dy|=\frac12e^{-y/2}$）。

**$n\to m$ 的變換**

1. 補 $Y_{m+1},\dots,Y_n$，讓 $\mathbb{R}^n\to\mathbb{R}^n$ 一對一。
2. 反函數 $x_i=w_i(\mathbf y)$；$J=\det\left[\partial x_i/\partial y_j\right]$。
3. $f_{\mathbf Y}(\mathbf y)=f_{\mathbf X}(\mathbf w(\mathbf y))|J|$，$\mathbf y\in g(A)$。
4. 積掉多的變數。

**關鍵一步**：$P(\mathbf Y\in g(A))=P(\mathbf X\in A)=\int_A f_{\mathbf X}=\int_{g(A)}f_{\mathbf X}(\mathbf w)|J|$；任何集合的機率都等於這個非負函數的積分 ⇒ 它就是 joint pdf。

**範圍**：先找 $A$（$f_{\mathbf X}>0$），再找 $g(A)$；積 marginal 時只積大於 0 的部分。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 二元變換、Jacobian | 下一集的例題；$t$、$F$ 分配的推導 |
| 補變數成一對一 | 求 $X_1+X_2$、$X_1/X_2$ 等的分配 |

---

## 附：本集一句話總結

> **要求 $m$ 個 $Y=g(X_1,\dots,X_n)$ 的分配，先補成 $n$ 個一對一變換，用 $f_{\mathbf Y}=f_{\mathbf X}(\mathbf w(\mathbf y))|J|$ 得到 joint pdf，再把多的變數積掉；範圍 $g(A)$ 一定要找對。**

---

## ⚠️ 待確認清單

1. [▶ 00:00](https://youtu.be/4p_eZcGVUSE?t=0) $Y=-2\log X$ 的推導，老師說「上一次」做過，但 Lec07 錄影裡沒有。可能有一段沒錄到。

---

*筆記依據「統計學」Lec08 錄影逐字稿（whisper large-v3-turbo，29:18）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
