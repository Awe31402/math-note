---
course: 高等統計學（數理統計續）
episode: 3
lecture: Lec03（第二週）
date: 待補
video: https://youtu.be/8U-EVNSSrGY
notes: Hogg 8th ed. §4.4 兩個順序統計量的 joint pdf（式 (4.4.3)，p. 256）；§3.6 $t$ 分配（p. 210–211）
---

# 第 3 集 · 第二週：兩個順序統計量的 joint pdf；$t$ 分配的推導 [▶ 影片](https://youtu.be/8U-EVNSSrGY)

← 上一集：[02](02-order-statistics-marginal-pdf-min-max-jth.md) ｜ [總目錄](../README.md) ｜ 下一集：[04](04-standard-normal-table-confidence-interval-pivotal-quantity.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 3 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（29:49，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §3.6、§4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「joint」→「JM／Jone」，「Jacobian」→「Jakobin／蝶蝶」，「反函數」→「法蘭素」，「卡方」→「卡荒」，「信賴區間」→「信賴期間」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 兩個順序統計量的 joint pdf](#1-兩個順序統計量的-joint-pdf)
- [2. 為什麼要 t 分配](#2-為什麼要-t-分配)
- [3. t 分配的定義](#3-t-分配的定義)
- [4. 推導 t 分配的 pdf](#4-推導-t-分配的-pdf)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $Y_j,Y_k$ 的 joint pdf | 式 (4.4.3)，p. 256 |
| $t$ 分配：$T=\frac{Z}{\sqrt{V/r}}$ 的 pdf | §3.6，p. 210–211 |

---

## 1. 兩個順序統計量的 joint pdf

[▶ 00:37](https://youtu.be/8U-EVNSSrGY?t=37) 有時候想要其中兩個（也可能三、四個）。【口頭】只舉兩個的例子，告訴你積分規則和結果，積分過程回去自己練。要用**理解**的：知道規則就知道答案為什麼長這樣。

設 $j<k$，要 $Y_j,Y_k$ 的 joint pdf。從 $n!\prod f(y_i)$ 出發，$y_j,y_k$ 不積，其他都積掉。

**分三段積**（[▶ 02:41](https://youtu.be/8U-EVNSSrGY?t=161)）：

| 段 | 變數 | 積分順序 | 最後一步 | 得到 |
|---|---|---|---|---|
| 後面 | $y_{k+1},\dots,y_n$（$n-k$ 個） | 從 $y_n$ 開始，每個積到 $b$ | $y_{k+1}$：$y_k$ 到 $b$ | $\dfrac{[1-F(y_k)]^{n-k}}{(n-k)!}$ |
| 中間 | $y_{j+1},\dots,y_{k-1}$（$k-j-1$ 個） | 從 $y_{k-1}$ 開始（也可以從 $y_{j+1}$，一樣麻煩） | $y_{j+1}$：$y_j$ 到 $y_k$ | $\dfrac{[F(y_k)-F(y_j)]^{k-j-1}}{(k-j-1)!}$ |
| 前面 | $y_1,\dots,y_{j-1}$（$j-1$ 個） | 從 $y_1$ 開始，每個從 $a$ 積 | $y_{j-1}$：$a$ 到 $y_j$ | $\dfrac{[F(y_j)]^{j-1}}{(j-1)!}$ |

- [▶ 06:50](https://youtu.be/8U-EVNSSrGY?t=410) 前面：$\int_a^{y_j}f=F(y_j)-F(a)=F(y_j)$。
- [▶ 07:51](https://youtu.be/8U-EVNSSrGY?t=471) 中間：$\int_{y_j}^{y_k}f=F(y_k)-F(y_j)$。
- [▶ 08:52](https://youtu.be/8U-EVNSSrGY?t=532) 後面：$\int_{y_k}^bf=1-F(y_k)$。
- $f(y_j)$、$f(y_k)$ 不積，留著。

> **結果**（[▶ 09:56](https://youtu.be/8U-EVNSSrGY?t=596)，課本式 (4.4.3)）：$a<y_j<y_k<b$，
> $$f_{Y_j,Y_k}(y_j,y_k)=\frac{n!}{(j-1)!\,(k-j-1)!\,(n-k)!}[F(y_j)]^{j-1}[F(y_k)-F(y_j)]^{k-j-1}[1-F(y_k)]^{n-k}f(y_j)f(y_k).$$

【口頭】[▶ 11:28](https://youtu.be/8U-EVNSSrGY?t=688) 懂了就可以自己寫三個、四個、五個的。Hogg & Craig 那本書有比較詳細的內容。有時候用得到、有時候用不到，但這是機率裡很重要的一部分，應該要會。

---

## 2. 為什麼要 t 分配

[▶ 11:28](https://youtu.be/8U-EVNSSrGY?t=688) 後面的主要主題是**信賴區間**和**假設檢定**。

【口頭】統計和別的領域不同：講任何東西都要說「我有多少信心」，一定要有機率。這些方法一定要用到一個新分配：**$t$ 分配**。

[▶ 12:29](https://youtu.be/8U-EVNSSrGY?t=749) $t$ 分配不是本來就有的，是我們**創造**出來的。

---

## 3. t 分配的定義

[▶ 12:29](https://youtu.be/8U-EVNSSrGY?t=749)

> **定義（$t$ 分配）**：$Z\sim N(0,1)$，$V\sim\chi^2(r)$，$Z$ 和 $V$ **獨立**。令
> $$T=\frac{Z}{\sqrt{V/r}}.$$
> $T$ 的分配叫 **$t$ 分配**，自由度（degrees of freedom）$r$，記作 $T\sim t(r)$。

- 【口頭】好記法：「標準常態」除以「根號（卡方除以它的自由度）」，兩者要獨立。
- [▶ 14:29](https://youtu.be/8U-EVNSSrGY?t=869) 實數函數的函數還是實數函數，所以 $T$ 是隨機變數，有分配。
- [▶ 15:30](https://youtu.be/8U-EVNSSrGY?t=930) 分子永遠是標準常態；分母卡方的自由度不同，$T$ 的分配就不同，所以 $t$ 分配也有自由度 $r$。

---

## 4. 推導 t 分配的 pdf

[▶ 16:31](https://youtu.be/8U-EVNSSrGY?t=991) 兩個變數變一個，要再定一個，讓它一對一。

**Step 1：$(Z,V)$ 的 joint pdf**（[▶ 17:34](https://youtu.be/8U-EVNSSrGY?t=1054)）。獨立 ⇒ 相乘。

複習 Gamma 和卡方的 pdf（[▶ 18:37](https://youtu.be/8U-EVNSSrGY?t=1117)，「一定要記得」）：
$$\Gamma(\alpha,\beta):\ \frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta};\qquad\chi^2(r)=\Gamma\left(\tfrac r2,2\right):\ \frac{1}{\Gamma(r/2)2^{r/2}}v^{r/2-1}e^{-v/2}.$$

$$f_{Z,V}(z,v)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\cdot\frac{1}{\Gamma(r/2)2^{r/2}}v^{r/2-1}e^{-v/2},\qquad -\infty<z<\infty,\ v>0.$$

【口頭】[▶ 20:10](https://youtu.be/8U-EVNSSrGY?t=1210) 變數變換一定要把範圍搞清楚，範圍寫錯，最後的 pdf 積起來就不是 1。

**Step 2：變換與範圍**（[▶ 20:40](https://youtu.be/8U-EVNSSrGY?t=1240)）
$$t=\frac{z}{\sqrt{v/r}},\qquad u=v.$$

- $z\in\mathbb{R}$、$\sqrt{v/r}>0$ ⇒ $t\in\mathbb{R}$。
- $u=v>0$。
- $B=\{(t,u): -\infty<t<\infty,\ u>0\}$。

**Step 3：一對一、反函數**（[▶ 22:12](https://youtu.be/8U-EVNSSrGY?t=1332)）。給定 $(t,u)$ 解：$v=u$，$z=t\sqrt{u/r}=\dfrac{t\sqrt u}{\sqrt r}$。唯一解 ⇒ 一對一。

**Step 4：Jacobian**（[▶ 23:13](https://youtu.be/8U-EVNSSrGY?t=1393)）
$$J=\det\begin{pmatrix}\dfrac{\partial z}{\partial t} & \dfrac{\partial z}{\partial u}\\[2mm] \dfrac{\partial v}{\partial t} & \dfrac{\partial v}{\partial u}\end{pmatrix}=\det\begin{pmatrix}\dfrac{\sqrt u}{\sqrt r} & \dfrac{t}{2\sqrt{ru}}\\[2mm] 0 & 1\end{pmatrix}=\frac{\sqrt u}{\sqrt r}>0.$$

**Step 5：$(T,U)$ 的 joint pdf**（[▶ 24:50](https://youtu.be/8U-EVNSSrGY?t=1490)）。把 $z=t\sqrt{u/r}$、$v=u$ 代入，乘 $|J|$：
$$f_{T,U}(t,u)=\frac{1}{\sqrt{2\pi}\,\Gamma(r/2)\,2^{r/2}}\,u^{r/2-1}e^{-u/2}\,e^{-t^2u/(2r)}\cdot\frac{\sqrt u}{\sqrt r}.$$
整理 $u$ 的部分：
$$f_{T,U}(t,u)=\frac{1}{\sqrt{2\pi r}\,\Gamma(r/2)\,2^{r/2}}\,u^{\frac{r+1}{2}-1}\exp\left[-\frac u2\left(1+\frac{t^2}{r}\right)\right].$$

**Step 6：積掉 $u$，湊成 Gamma pdf**（[▶ 26:24](https://youtu.be/8U-EVNSSrGY?t=1584)）

【口頭】看到 $e^{-(\cdot)u}$ 和 $u^{(\cdot)-1}$ 就要判斷：這是 Gamma 分配。把 $u$ 以外的東西放到分母當 $\beta$：

$$\alpha=\frac{r+1}{2},\qquad\beta=\frac{2}{1+t^2/r}.$$

乘上再除以 $\Gamma(\alpha)\beta^\alpha$，積分裡就是 $\Gamma(\alpha,\beta)$ 的 pdf，積分＝1：
$$\int_0^\infty u^{\alpha-1}e^{-u/\beta}\,du=\Gamma(\alpha)\beta^\alpha.$$

**結果**（[▶ 28:27](https://youtu.be/8U-EVNSSrGY?t=1707)）：
$$f_T(t)=\frac{\Gamma\left(\frac{r+1}{2}\right)}{\sqrt{\pi r}\,\Gamma\left(\frac r2\right)}\left(1+\frac{t^2}{r}\right)^{-(r+1)/2},\qquad -\infty<t<\infty.$$

（整理：$\frac{\Gamma(\alpha)\beta^\alpha}{\sqrt{2\pi r}\Gamma(r/2)2^{r/2}}$，$\beta^\alpha=2^{(r+1)/2}(1+t^2/r)^{-(r+1)/2}$，$\frac{2^{(r+1)/2}}{\sqrt 2\cdot 2^{r/2}}=1$。這段整理不是逐字稿內容，是依課本 p. 211 補的。）

【口頭】[▶ 28:27](https://youtu.be/8U-EVNSSrGY?t=1707) 這個 pdf **不要背**，太麻煩。但希望會自己導；想讀統計，這種變數變換技巧一定要會，才知道怎麼找新的分配。考試不會考導這個。

---

## 5. 一頁速查表

**兩個順序統計量**（$j<k$）：
$$f_{Y_j,Y_k}=\frac{n!}{(j-1)!(k-j-1)!(n-k)!}F(y_j)^{j-1}[F(y_k)-F(y_j)]^{k-j-1}[1-F(y_k)]^{n-k}f(y_j)f(y_k).$$
記法：下面 $j-1$ 個 → $F(y_j)$；中間 $k-j-1$ 個 → $F(y_k)-F(y_j)$；上面 $n-k$ 個 → $1-F(y_k)$。

**$t$ 分配**：$Z\sim N(0,1)$、$V\sim\chi^2(r)$ 獨立，$T=\dfrac{Z}{\sqrt{V/r}}\sim t(r)$。

推導關鍵：
1. 補 $U=V$；反函數 $z=t\sqrt{u/r}$，$v=u$；$J=\sqrt{u/r}$。
2. joint pdf 對 $u$ 是 $\Gamma\left(\frac{r+1}{2},\frac{2}{1+t^2/r}\right)$ 的核，積分＝$\Gamma(\alpha)\beta^\alpha$。

$$f_T(t)=\frac{\Gamma\left(\frac{r+1}{2}\right)}{\sqrt{\pi r}\,\Gamma\left(\frac r2\right)}\left(1+\frac{t^2}{r}\right)^{-\frac{r+1}{2}}.$$

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $t$ 分配 | 常態母體 $\sigma^2$ 未知時 $\mu$ 的信賴區間、$t$ 檢定 |
| $\frac{\bar X-\mu}{S/\sqrt n}\sim t(n-1)$ | 用上學期的 $\bar X\perp S^2$、$\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$ |
| 順序統計量 | 無母數方法 |

---

## 附：本集一句話總結

> **兩個順序統計量的 joint pdf 分三段積（下面得 $F(y_j)$、中間得 $F(y_k)-F(y_j)$、上面得 $1-F(y_k)$）；$t$ 分配定義為獨立的「標準常態 ÷ $\sqrt{\text{卡方}/r}$」，用補一個變數、Jacobian、把 $u$ 湊成 Gamma pdf 積掉，就得到它的 pdf。**

---

*筆記依據「高等統計學」Lec03 錄影逐字稿（whisper large-v3-turbo，29:49）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
