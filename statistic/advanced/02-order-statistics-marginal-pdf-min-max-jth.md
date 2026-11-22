---
course: 高等統計學（數理統計續）
episode: 2
lecture: Lec02（第一週 2/2）
date: 待補
video: https://youtu.be/yzWQA6rQBqk
notes: Hogg 8th ed. §4.4 順序統計量（Theorem 4.4.1，p. 254；第 $k$ 個順序統計量的 pdf，式 (4.4.2)，p. 255）
---

# 第 2 集 · 第一週 (2/2)：從 joint pdf 積出最小、最大、第 j 個順序統計量的 pdf [▶ 影片](https://youtu.be/yzWQA6rQBqk)

← 上一集：[01](01-non-one-to-one-transformation-order-statistics-joint-pdf.md) ｜ [總目錄](../README.md) ｜ 下一集：[03](03-two-order-statistics-joint-pdf-t-distribution.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 2 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（37:02，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「joint」→「join／糾紋／揪文」，「iid」→「RID」，「機率」→「激勵」，「Hogg & Craig」→「Hawk & Craig」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：joint pdf](#1-複習joint-pdf)
- [2. 兩個積分事實](#2-兩個積分事實)
- [3. 最小 Y₁ 的 pdf：從最大的開始積](#3-最小-y₁-的-pdf從最大的開始積)
- [4. 最大 Yₙ 的 pdf：從最小的開始積](#4-最大-yₙ-的-pdf從最小的開始積)
- [5. 第 j 個 Yⱼ 的 pdf：兩邊一起積](#5-第-j-個-yⱼ-的-pdf兩邊一起積)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/yzWQA6rQBqk?t=0) 上學期用比較簡單的方式導過最小、最大的分配。現在用一般的方式：從 joint pdf 積分，這樣中間某一個、某兩個都能求。

| 主題 | 課本 |
|---|---|
| $f_{Y_1}$、$f_{Y_n}$（用 joint pdf 積分重新導） | §4.4 |
| 第 $j$ 個順序統計量 $f_{Y_j}$ | 式 (4.4.2)，p. 255 |

---

## 1. 複習：joint pdf

[▶ 01:02](https://youtu.be/yzWQA6rQBqk?t=62) $X_1,\dots,X_n$ iid，pdf $f(x)$，$a<x<b$。順序統計量 $Y_1<\cdots<Y_n$：

$$f_{Y_1,\dots,Y_n}(y_1,\dots,y_n)=n!\,f(y_1)f(y_2)\cdots f(y_n),\quad a<y_1<y_2<\cdots<y_n<b.$$

[▶ 02:38](https://youtu.be/yzWQA6rQBqk?t=158) 範圍：最小的還是比 $a$ 大、最大的還是比 $b$ 小（原本都在 $(a,b)$）。

要其中某一個的 pdf：把**其他的全部積掉**。

---

## 2. 兩個積分事實

$F$ 是 $X$ 的分配函數（連續型，$F'=f$），$F(a)=0$、$F(b)=1$。

1. $\displaystyle\int_c^bf(t)\,dt=1-F(c)$（[▶ 07:49](https://youtu.be/yzWQA6rQBqk?t=469)：積到 $b$ 就得「1 減分配函數」）。
2. $\displaystyle\int_a^cf(t)\,dt=F(c)$（[▶ 18:41](https://youtu.be/yzWQA6rQBqk?t=1121)：$a$ 以下沒有機率，$F(a)=0$）。

再加兩個反導函數（連鎖律）：

3. $\dfrac{d}{dy}\dfrac{[1-F(y)]^{k}}{k}=-[1-F(y)]^{k-1}f(y)$，所以 $\displaystyle\int_c^b[1-F(y)]^{k-1}f(y)\,dy=\frac{[1-F(c)]^{k}}{k}$。
4. $\dfrac{d}{dy}\dfrac{[F(y)]^{k}}{k}=[F(y)]^{k-1}f(y)$，所以 $\displaystyle\int_a^c[F(y)]^{k-1}f(y)\,dy=\frac{[F(c)]^{k}}{k}$。

---

## 3. 最小 Y₁ 的 pdf：從最大的開始積

[▶ 03:41](https://youtu.be/yzWQA6rQBqk?t=221) 要 $Y_1$，就積掉 $y_2,\dots,y_n$。

**積分順序很重要**（[▶ 04:11](https://youtu.be/yzWQA6rQBqk?t=251)）：

- 從 $y_2$ 開始積（$y_1$ 到 $y_3$）很麻煩。
- 比較簡單：**從最大的 $y_n$ 開始積**。$y_n$ 從 $y_{n-1}$ 積到 $b$；積完 $y_n$ 不見，再積 $y_{n-1}$（從 $y_{n-2}$ 到 $b$）……一路積到 $y_2$（從 $y_1$ 到 $b$）。

$$f_{Y_1}(y_1)=n!\,f(y_1)\int_{y_1}^b\!\!\int_{y_2}^b\!\!\cdots\int_{y_{n-1}}^bf(y_2)\cdots f(y_n)\,dy_n\cdots dy_3\,dy_2.$$

**Step 1：積 $y_n$**（[▶ 06:46](https://youtu.be/yzWQA6rQBqk?t=406)）。其他當常數：
$$\int_{y_{n-1}}^bf(y_n)\,dy_n=1-F(y_{n-1})=\frac{[1-F(y_{n-1})]^1}{1!}.$$
（老師在分母補一個 $1!$，好看出規律。）

**Step 2：積 $y_{n-1}$**（[▶ 08:51](https://youtu.be/yzWQA6rQBqk?t=531)）。用事實 3：
$$\int_{y_{n-2}}^b\frac{[1-F(y_{n-1})]^1}{1!}f(y_{n-1})\,dy_{n-1}=\frac{[1-F(y_{n-2})]^2}{2!}.$$
（$b$ 代進去是 $1-F(b)=0$；下限代進去，負號抵掉。）

**Step 3：規律**（[▶ 11:56](https://youtu.be/yzWQA6rQBqk?t=716)）：積 1 個 → $\frac{[1-F]^1}{1!}$；積 2 個 → $\frac{[1-F]^2}{2!}$；積 3 個 → $\frac{[1-F]^3}{3!}$……

[▶ 12:29](https://youtu.be/yzWQA6rQBqk?t=749) 積到只剩 $y_2$ 還沒積時，已經積了 $n-2$ 個：$\dfrac{[1-F(y_2)]^{n-2}}{(n-2)!}$。

**Step 4：積 $y_2$**（[▶ 13:34](https://youtu.be/yzWQA6rQBqk?t=814)）：
$$\int_{y_1}^b\frac{[1-F(y_2)]^{n-2}}{(n-2)!}f(y_2)\,dy_2=\frac{[1-F(y_1)]^{n-1}}{(n-1)!}.$$

**結果**（[▶ 14:04](https://youtu.be/yzWQA6rQBqk?t=844)）：$\frac{n!}{(n-1)!}=n$，
$$f_{Y_1}(y)=n[1-F(y)]^{n-1}f(y),\quad a<y<b.$$

和上學期證的一模一樣，只是方法不同。【口頭】學這個的好處：會一兩個之後，其他的答案自己就知道了。

---

## 4. 最大 Yₙ 的 pdf：從最小的開始積

[▶ 15:37](https://youtu.be/yzWQA6rQBqk?t=937) 要 $Y_n$，積掉 $y_1,\dots,y_{n-1}$。

**積分順序**（[▶ 16:39](https://youtu.be/yzWQA6rQBqk?t=999)）：從 $y_{n-1}$ 開始（$y_{n-2}$ 到 $y_n$）比較麻煩；比較簡單的是**從最小的 $y_1$ 開始**，$y_1$ 從 $a$ 積到 $y_2$；再積 $y_2$（$a$ 到 $y_3$）……最後 $y_{n-1}$（$a$ 到 $y_n$）。

$$f_{Y_n}(y_n)=n!\,f(y_n)\int_a^{y_n}\!\!\cdots\int_a^{y_3}\!\!\int_a^{y_2}f(y_1)\cdots f(y_{n-1})\,dy_1\,dy_2\cdots dy_{n-1}.$$

**Step 1：積 $y_1$**（[▶ 18:11](https://youtu.be/yzWQA6rQBqk?t=1091)）：$\int_a^{y_2}f(y_1)\,dy_1=F(y_2)=\frac{[F(y_2)]^1}{1!}$。

**Step 2：積 $y_2$**（[▶ 20:47](https://youtu.be/yzWQA6rQBqk?t=1247)）。用事實 4：$\int_a^{y_3}F(y_2)f(y_2)\,dy_2=\frac{[F(y_3)]^2}{2!}$。

**Step 3：規律**：積 $k$ 個 → $\dfrac{[F(y_{k+1})]^k}{k!}$。

**Step 4**（[▶ 23:26](https://youtu.be/yzWQA6rQBqk?t=1406)）：積到剩 $y_{n-1}$ 時，已積 $n-2$ 個：$\frac{[F(y_{n-1})]^{n-2}}{(n-2)!}$。再積 $y_{n-1}$（從 $a$ 到 $y_n$）：$\frac{[F(y_n)]^{n-1}}{(n-1)!}$。

**結果**（[▶ 26:04](https://youtu.be/yzWQA6rQBqk?t=1564)）：
$$f_{Y_n}(y)=n[F(y)]^{n-1}f(y),\quad a<y<b.$$

---

## 5. 第 j 個 Yⱼ 的 pdf：兩邊一起積

[▶ 26:37](https://youtu.be/yzWQA6rQBqk?t=1597) 【口頭】剩下的不證了，但告訴你怎麼證，自己推導看看。Hogg & Craig 那本書好像都有證，方法跟老師的一模一樣。

[▶ 27:38](https://youtu.be/yzWQA6rQBqk?t=1658) 要 $Y_j$：把**前面**的（$y_1,\dots,y_{j-1}$）和**後面**的（$y_{j+1},\dots,y_n$）都積掉。

**積分順序**（[▶ 29:11](https://youtu.be/yzWQA6rQBqk?t=1751)）：

- 前面：從 $y_1$ 開始（$a$ 到 $y_2$）、$y_2$（$a$ 到 $y_3$）……最後 $y_{j-1}$（$a$ 到 $y_j$）。
- 後面：從 $y_n$ 開始（$y_{n-1}$ 到 $b$）、$y_{n-1}$（$y_{n-2}$ 到 $b$）……最後 $y_{j+1}$（$y_j$ 到 $b$）。

**結果怎麼讀**（[▶ 31:12](https://youtu.be/yzWQA6rQBqk?t=1872)）：

| 部分 | 來源 |
|---|---|
| $n!$ | joint pdf 本來就有 |
| $f(y_j)$ | 沒被積掉，留著 |
| $\dfrac{[F(y_j)]^{j-1}}{(j-1)!}$ | 前面積了 $j-1$ 個，都從 $a$ 開始 → 得分配函數 |
| $\dfrac{[1-F(y_j)]^{n-j}}{(n-j)!}$ | 後面積了 $n-j$ 個，都積到 $b$ → 得 1 減分配函數 |

> **第 $j$ 個順序統計量的 pdf**（[▶ 34:52](https://youtu.be/yzWQA6rQBqk?t=2092)，課本式 (4.4.2)，p. 255）：
> $$f_{Y_j}(y)=\frac{n!}{(j-1)!\,(n-j)!}[F(y)]^{j-1}[1-F(y)]^{n-j}f(y),\qquad a<y<b.$$

（$j=1$、$j=n$ 就是 §3、§4 的結果。）

---

## 6. 一頁速查表

**積分技巧**

- 要「上面」的被積掉 → 從最大的開始，每個積到 $b$ → $\dfrac{[1-F]^k}{k!}$。
- 要「下面」的被積掉 → 從最小的開始，每個從 $a$ 積 → $\dfrac{[F]^k}{k!}$。

**公式**

| | pdf |
|---|---|
| $Y_1$（最小） | $n[1-F(y)]^{n-1}f(y)$ |
| $Y_n$（最大） | $n[F(y)]^{n-1}f(y)$ |
| $Y_j$（第 $j$ 個） | $\dfrac{n!}{(j-1)!(n-j)!}F(y)^{j-1}[1-F(y)]^{n-j}f(y)$ |

**記法**：下面有 $j-1$ 個 → $F^{j-1}/(j-1)!$；上面有 $n-j$ 個 → $(1-F)^{n-j}/(n-j)!$；自己 → $f$；前面乘 $n!$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 任兩個順序統計量的 joint pdf | 下一集（同樣的積法） |
| $f_{Y_j}$ | 樣本中位數、分位數；無母數信賴區間 |

---

## 附：本集一句話總結

> **從順序統計量的 joint pdf $n!\prod f(y_i)$ 出發，要最小的就從最大的開始一路積到 $b$（得 $[1-F]^{k}/k!$），要最大的就從最小的開始一路從 $a$ 積（得 $F^{k}/k!$），兩邊一起積就得第 $j$ 個的 pdf $\frac{n!}{(j-1)!(n-j)!}F^{j-1}(1-F)^{n-j}f$。**

---

*筆記依據「高等統計學」Lec02 錄影逐字稿（whisper large-v3-turbo，37:02）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
