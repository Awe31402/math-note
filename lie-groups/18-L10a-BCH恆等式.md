---
course: Matrix Lie Groups (Spring 2016)
episode: 18
lecture: L10a
date: 2016-04-11（part 1）
video: https://www.youtube.com/watch?v=cPIt_ajpSlU
notes: Hall 第 1 版 §3.1 Thm. 3.1–3.2（p.64–67）、§3.2 Thm. 3.3、Cor. 3.4（p.67–70）
---

# 第 18 集 · L10a：Heisenberg 情況的 BCH、BCH 積分形式、Cor. 3.4 [▶ 影片](https://www.youtube.com/watch?v=cPIt_ajpSlU&list=PLBY4G2o7DhF3FS2CaX62eiQWGP9_xdLYs)

← 上一集：[[17-L9b-二階BCH]] ｜ [總目錄](README.md) ｜ 下一集：[[19-L10b-指數映射的導數]] →

> **課程**：Matrix Lie Groups（Liberty University，Spring 2016）— 第 18 集，April 11 part 1
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ Hall《Lie Groups, Lie Algebras, and Representations》第 1 版 §3.1（p.63–67）、§3.2（p.67–70）
> **標記說明**：`【口頭】` 老師口頭補充、課本沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【課本補充】` 課本有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Thm. 3.1：括號和 X、Y 都交換時的 BCH](#1-thm-31括號和-xy-都交換時的-bch)
  - [1.1 敘述；Heisenberg 李代數](#11-敘述heisenberg-李代數)
  - [1.2 證明策略：引入參數 t，比較 ODE](#12-證明策略引入參數-t比較-ode)
  - [1.3 計算 A'(t)](#13-計算-at)
- [2. Thm. 3.2：Heisenberg 群上的李代數同態都能升成群同態](#2-thm-32heisenberg-群上的李代數同態都能升成群同態)
- [3. BCH 的積分形式（Thm. 3.3）](#3-bch-的積分形式thm-33)
- [4. Cor. 3.4：φ 穿過 BCH](#4-cor-34φ-穿過-bch)
- [5. 預告：指數映射的導數](#5-預告指數映射的導數)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】[▶ 00:02](https://youtu.be/cPIt_ajpSlU?t=2) 「書前面有很多很有趣的計算，我們應該能跟上不少。」[▶ 34:53](https://youtu.be/cPIt_ajpSlU?t=2093)「一開始讀以為只是技術性的東西，但這些證明裡有很多計算**本身就很有趣**，有值得你們看的計算技巧。」

| 主題 | Hall |
|---|---|
| $[X,Y]$ 和 $X, Y$ 交換時，$e^Xe^Y = e^{X+Y+\frac12[X,Y]}$ | Thm. 3.1（p.64–66） |
| Heisenberg 群的同態 | Thm. 3.2（p.66–67） |
| BCH 積分形式 | Thm. 3.3（p.68） |
| 李代數同態穿過 BCH | Cor. 3.4（p.69） |

## 1. Thm. 3.1：括號和 X、Y 都交換時的 BCH

### 1.1 敘述；Heisenberg 李代數

[▶ 00:45](https://youtu.be/cPIt_ajpSlU?t=45)

> **Theorem 3.1（Hall p.64）**　$X, Y$ 是 $n\times n$ 複數矩陣，且
> $$[X, [X, Y]] = [Y, [X, Y]] = 0.$$
> 則
> $$e^Xe^Y = e^{X + Y + \frac12[X, Y]}.$$

[▶ 01:27](https://youtu.be/cPIt_ajpSlU?t=87) **Heisenberg 群**的李代數滿足這個條件：$3\times 3$ **嚴格上三角**矩陣。兩個相乘只剩右上角 $(1, 3)$ 位置；那種矩陣再和任何嚴格上三角矩陣乘都是 0。

[▶ 02:42](https://youtu.be/cPIt_ajpSlU?t=162) 這是 BCH 級數「在 $[X, Y]$ 那項就停下」的特例。上次只證到二階、沒證高階項都是巢狀交換子；這個在特殊情況下是**完整**結果，「是實打實的進步」。

### 1.2 證明策略：引入參數 t，比較 ODE

[▶ 03:14](https://youtu.be/cPIt_ajpSlU?t=194) 證更一般的

$$
e^{tX}e^{tY} = e^{tX + tY + \frac{t^2}{2}[X, Y]},
$$

$t = 1$ 就是定理。

【口頭】[▶ 03:49](https://youtu.be/cPIt_ajpSlU?t=229) 「如果問我這最像進階微積分的什麼，大概是**引入參數算積分**那招。」我們要的等式在 $t = 1$；引入參數就能用**微積分**。

[▶ 04:35](https://youtu.be/cPIt_ajpSlU?t=275) $[X, Y]$ 和 $tX + tY$ 交換，交換的矩陣指數律成立，所以右邊 $= e^{tX + tY}e^{\frac{t^2}{2}[X,Y]}$。移項（反元素就是加負號）得等價的式子：

$$
\underbrace{e^{tX}e^{tY}e^{-\frac{t^2}{2}[X, Y]}}_{A(t)} = \underbrace{e^{t(X + Y)}}_{B(t)}. \tag{3.4}
$$

[▶ 07:09](https://youtu.be/cPIt_ajpSlU?t=429) $B$ 滿足

$$
B'(t) = B(t)(X + Y),\qquad B(0) = I.
$$

[▶ 07:51](https://youtu.be/cPIt_ajpSlU?t=471) 如果 $A$ 滿足**同一個** ODE 和初值，由 ODE 的**存在唯一定理**，$A = B$。

【口頭】[▶ 08:29](https://youtu.be/cPIt_ajpSlU?t=509) 老師重讀了 Stillwell 的 BCH 證明。Stillwell 批評：這類書的其他證明都靠 ODE 存在唯一定理，「而這在 BCH 裡很奇怪」。

### 1.3 計算 A'(t)

[▶ 09:06](https://youtu.be/cPIt_ajpSlU?t=546) 三個因子的乘積法則（$(fgh)' = f'gh + fg'h + fgh'$）：

$$
A'(t) = e^{tX}Xe^{tY}e^{-\frac{t^2}{2}[X,Y]} + e^{tX}e^{tY}Ye^{-\frac{t^2}{2}[X,Y]} + e^{tX}e^{tY}e^{-\frac{t^2}{2}[X,Y]}\left(-t[X, Y]\right). \tag{3.5}
$$

**第二項**　[▶ 10:24](https://youtu.be/cPIt_ajpSlU?t=624) $Y$ 和 $[X, Y]$ 交換，所以和 $e^{-\frac{t^2}{2}[X,Y]}$ 交換：第二項 $= A(t)\,Y$。

**第一項**　[▶ 12:27](https://youtu.be/cPIt_ajpSlU?t=747) $X$ **不一定**和 $e^{tY}$ 交換。Hall 的巧招：

$$
Xe^{tY} = e^{tY}\left(e^{-tY}Xe^{tY}\right) = e^{tY}\operatorname{Ad}_{e^{-tY}}(X) = e^{tY}e^{-t\operatorname{ad}_Y}(X).
$$

[▶ 13:43](https://youtu.be/cPIt_ajpSlU?t=823) 「這是共軛，也就是大伴隨。我們證過大小伴隨的關係 $\operatorname{Ad}_{e^Z} = e^{\operatorname{ad}_Z}$。」[▶ 14:17](https://youtu.be/cPIt_ajpSlU?t=857) 「這正是**該寫成小伴隨**的地方：小伴隨就是在做巢狀交換子。」

[▶ 15:37](https://youtu.be/cPIt_ajpSlU?t=937) 展開級數：

$$
e^{-t\operatorname{ad}_Y}(X) = X - t[Y, X] + \frac{t^2}{2}[Y, [Y, X]] - \cdots
$$

[▶ 16:28](https://youtu.be/cPIt_ajpSlU?t=988) $[Y, [Y, X]] = -[Y, [X, Y]] = 0$，**級數截斷**：

$$
e^{-t\operatorname{ad}_Y}(X) = X - t[Y, X] = X + t[X, Y].
$$

[▶ 17:46](https://youtu.be/cPIt_ajpSlU?t=1066) 所以第一項 $= e^{tX}e^{tY}(X + t[X, Y])e^{-\frac{t^2}{2}[X,Y]} = A(t)(X + t[X, Y])$（$X + t[X,Y]$ 和 $[X,Y]$ 交換，可以挪過去）。

**合起來**　[▶ 19:58](https://youtu.be/cPIt_ajpSlU?t=1198)

$$
A'(t) = A(t)(X + t[X, Y]) + A(t)Y - A(t)\,t[X, Y] = A(t)(X + Y).
$$

[▶ 20:35](https://youtu.be/cPIt_ajpSlU?t=1235) 綠色的兩項 $\pm t[X, Y]$「一定得抵消」——它們確實抵消。$A(0) = I = B(0)$，所以 $A = B$。代 $t = 1$。∎

【口頭】[▶ 20:35](https://youtu.be/cPIt_ajpSlU?t=1235) 「要找哪個 ODE，寫下 $B$ 的瞬間就很明顯。困難是 $A$ 那邊；這裡看到大伴隨和小伴隨怎麼**合作**，把巢狀交換子恆等式實際用上。」

## 2. Thm. 3.2：Heisenberg 群上的李代數同態都能升成群同態

[▶ 21:42](https://youtu.be/cPIt_ajpSlU?t=1302)

> **Theorem 3.2（Hall p.66）**　$H$ 是 Heisenberg 群、$\mathfrak h$ 是它的李代數；$G$ 是矩陣李群。若 $\phi:\mathfrak h\to\mathfrak g$ 是李代數同態，則存在唯一的李群同態 $\Phi: H\to G$，使 $\Phi(e^X) = e^{\phi(X)}$。

[▶ 22:18](https://youtu.be/cPIt_ajpSlU?t=1338) 證明思路：Heisenberg 群的指數映射是**雙射**（Hall 習題 2.26），所以可以直接**定義**

$$
\Phi(A) = e^{\phi(\log A)}.
$$

[▶ 22:53](https://youtu.be/cPIt_ajpSlU?t=1373) 因為 Heisenberg 李代數滿足「括號和兩邊交換」，可以用 Thm. 3.1 證同態性質。

> 【課本補充】Hall p.66–67：
> - $\phi$ 是李代數同態，所以 $[\phi(X), [\phi(X), \phi(Y)]] = \phi([X, [X, Y]]) = 0$，$\phi(X), \phi(Y)$ 也滿足 Thm. 3.1 的條件。
> - $A = e^X$、$B = e^Y$：$AB = e^{X + Y + \frac12[X,Y]}$，所以
> $$\Phi(AB) = e^{\phi(X) + \phi(Y) + \frac12[\phi(X), \phi(Y)]} = e^{\phi(X)}e^{\phi(Y)} = \Phi(A)\Phi(B).$$
> - 連續性：$\log$、$\exp$、$\phi$ 都連續。唯一性：指數映射是雙射。

【Q&A】[▶ 22:53](https://youtu.be/cPIt_ajpSlU?t=1373) 學生問 Heisenberg 群的定義。老師：第 2 章講過——$3\times 3$ 實矩陣、**嚴格上三角加上對角線全是 1**：

$$
H = \left\{\begin{pmatrix}1 & a & b\\ 0 & 1 & c\\ 0 & 0 & 1\end{pmatrix}\right\},\qquad
\mathfrak h = \left\{\begin{pmatrix}0 & x & y\\ 0 & 0 & z\\ 0 & 0 & 0\end{pmatrix}\right\}.
$$

【口頭】[▶ 23:25](https://youtu.be/cPIt_ajpSlU?t=1405) 老師一開始說「它其實不是矩陣李群」，「好笑但不好笑」——⚠️ 它**是**矩陣李群；Hall 提到的「不是矩陣李群」的例子是 Heisenberg 群的某個**商群**（Hall §C.3）。（推論，不是逐字稿內容。）

[▶ 24:31](https://youtu.be/cPIt_ajpSlU?t=1471) 【口頭】想造「交換子不為零、但交換子的交換子為零」這類例子，**嚴格上三角矩陣**就是去處：每乘一次，非零元素就往右上角推一格。$4\times 4$ 的話，要三層括號才變 0，依此類推。

## 3. BCH 的積分形式（Thm. 3.3）

[▶ 25:06](https://youtu.be/cPIt_ajpSlU?t=1506) 一般的 BCH，「論證很滑溜」。先定義

$$
g(z) = \frac{\log z}{1 - \frac1z}.
$$

[▶ 25:40](https://youtu.be/cPIt_ajpSlU?t=1540) 在圓盤 $\{|z - 1| < 1\}$ 上解析（可以選主支的對數）。[▶ 26:18](https://youtu.be/cPIt_ajpSlU?t=1578) 所以存在係數 $a_m$：

$$
g(z) = \sum_{m=0}^\infty a_m(z - 1)^m.
$$

「它們是什麼不重要，存在就好。」

[▶ 26:51](https://youtu.be/cPIt_ajpSlU?t=1611) 對算子 $A$，$\|A - I\| < 1$ 時定義 $g(A) = \sum a_m(A - I)^m$。

[▶ 27:29](https://youtu.be/cPIt_ajpSlU?t=1649)

> **Theorem 3.3（BCH 積分形式，Hall p.68）**　對所有夠小的 $n\times n$ 複數矩陣 $X, Y$：
> $$\log\left(e^Xe^Y\right) = X + \int_0^1 g\left(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}\right)(Y)\,dt. \tag{3.6}$$

[▶ 28:03](https://youtu.be/cPIt_ajpSlU?t=1683) 只對**夠小的**矩陣成立，不是全域結果。BCH 級數對不夠小的矩陣**發散**。

【口頭】[▶ 29:26](https://youtu.be/cPIt_ajpSlU?t=1766) 「第一反應：這跟我知道的 BCH 一點都不像。」

[▶ 30:01](https://youtu.be/cPIt_ajpSlU?t=1801) 為什麼 $g(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y})$ 有意義：$e^{\operatorname{ad}_X}$ 是線性算子。$X, Y$ 小時，[▶ 30:35](https://youtu.be/cPIt_ajpSlU?t=1835) 每多一個 $\operatorname{ad}$ 就多乘一個 $X$ 或 $Y$ 的因子，所以 $e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}$ **很接近恆等算子**，$\|\cdot - I\| < 1$，$g$ 的級數收斂。

【課堂討論】[▶ 31:43](https://youtu.be/cPIt_ajpSlU?t=1903) 如果 $X, Y$ 交換呢？左邊是 $X + Y$。[▶ 32:21](https://youtu.be/cPIt_ajpSlU?t=1941) 右邊：$\operatorname{ad}_X(Y) = 0$ 等等，$e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}$ 作用在 $Y$ 上就是恆等，$g$ 只剩 $a_0 = g(1) = 1$，積分 $\int_0^1 Y\,dt = Y$。右邊也是 $X + Y$。✓（Hall 習題 5。）

> 推論（不是逐字稿內容）：$g(1) = \lim_{z\to 1}\frac{\log z}{1 - 1/z} = \lim_{z\to 1}\frac{z\log z}{z - 1} = 1$（L'Hôpital）。

[▶ 33:06](https://youtu.be/cPIt_ajpSlU?t=1986) Hall 原話：式 (3.6)「**確實很醜**。但我們在乎的不是細節，而是它把 $\log(e^Xe^Y)$ 用李代數的量 $\operatorname{ad}_X$、$\operatorname{ad}_Y$ 表示出來。」Hall 提到 Jacobson（1962）§V.5 有直接證明：$\log(e^Xe^Y)$ 展開的每一項都能寫成交換子。「我們不走那條路。」

> 【課本補充】Hall p.68：為什麼不直接把兩個指數和對數都展開、乘開？前幾項確實能得到一樣的答案，但**怎麼知道每一項都能寫成交換子？** 二階項一定是 $X^2, Y^2, XY, YX$ 的組合，要能寫成交換子，它必須正好是 $c(XY - YX)$——二階乘開能看到，但高階完全不清楚（Hall 習題 6）。

## 4. Cor. 3.4：φ 穿過 BCH

[▶ 34:53](https://youtu.be/cPIt_ajpSlU?t=2093)

> **Corollary 3.4（Hall p.69）**　$G$ 是矩陣李群，$\phi:\mathfrak g\to\mathfrak{gl}(n; \mathbb{C})$ 是李代數同態。則對所有夠小的 $X, Y\in\mathfrak g$，$\log(e^Xe^Y)\in\mathfrak g$，且
> $$\phi\left(\log(e^Xe^Y)\right) = \log\left(e^{\phi(X)}e^{\phi(Y)}\right). \tag{3.7}$$

【Q&A】[▶ 37:37](https://youtu.be/cPIt_ajpSlU?t=2257) 學生：這和上次的式子不是一樣嗎？老師：上次是 (3.3)，是**解釋**為什麼 BCH 和「從李代數同態造群同態」有關；現在是嚴格的推論。

**$\log(e^Xe^Y)\in\mathfrak g$**　[▶ 38:51](https://youtu.be/cPIt_ajpSlU?t=2331) $X, Y\in\mathfrak g$，則 $\operatorname{ad}_X, \operatorname{ad}_Y$ 把 $\mathfrak g$ 映到 $\mathfrak g$（$\mathfrak g$ 對括號封閉），所以 $g(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y})(Y)\in\mathfrak g$，積分（$\mathfrak g$ 是閉子空間）也在 $\mathfrak g$。

**$\phi$ 穿過 $\operatorname{ad}$**　[▶ 43:32](https://youtu.be/cPIt_ajpSlU?t=2612) 李代數同態：$\phi([Y, X]) = [\phi(Y), \phi(X)]$，也就是

$$
\phi\left(\operatorname{ad}_Y(X)\right) = \operatorname{ad}_{\phi(Y)}\left(\phi(X)\right).
$$

[▶ 44:10](https://youtu.be/cPIt_ajpSlU?t=2650) 重複 $m$ 次：$\phi\left((\operatorname{ad}_Y)^m X\right) = (\operatorname{ad}_{\phi(Y)})^m\phi(X)$。

[▶ 45:31](https://youtu.be/cPIt_ajpSlU?t=2731) 對指數級數逐項用（「先不管分析上的細節」）：

$$
\phi\left(e^{t\operatorname{ad}_Y}X\right) = \sum_m\frac{t^m}{m!}\phi\left((\operatorname{ad}_Y)^mX\right) = \sum_m\frac{t^m}{m!}(\operatorname{ad}_{\phi(Y)})^m\phi(X) = e^{t\operatorname{ad}_{\phi(Y)}}\phi(X).
$$

[▶ 47:49](https://youtu.be/cPIt_ajpSlU?t=2869) Hall：「同理」

$$
\phi\left(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}(Y)\right) = e^{\operatorname{ad}_{\phi(X)}}e^{t\operatorname{ad}_{\phi(Y)}}\phi(Y).
$$

【課堂討論】[▶ 48:30](https://youtu.be/cPIt_ajpSlU?t=2910) 老師問這兩個伴隨算子交換嗎？學生：不交換，那是**算子合成**。[▶ 49:50](https://youtu.be/cPIt_ajpSlU?t=2990) 學生解釋「同理」：把同一招用兩次：先把 $\phi$ 穿過 $e^{t\operatorname{ad}_Y}$，再穿過 $e^{\operatorname{ad}_X}$。

[▶ 51:29](https://youtu.be/cPIt_ajpSlU?t=3089)–[▶ 57:16](https://youtu.be/cPIt_ajpSlU?t=3436) 把 $\phi$ 套到 (3.6) 兩邊：
1. $\phi$ 線性，穿過積分。
2. [▶ 53:27](https://youtu.be/cPIt_ajpSlU?t=3207) $g$ 只是算子的冪級數（「把 $g$ 想成一種奇怪的指數」），$\phi$ 一樣穿過 $g(\cdot) = \sum a_m(\cdot - I)^m$。
3. 得到 $\phi(X) + \int_0^1 g\left(e^{\operatorname{ad}_{\phi(X)}}e^{t\operatorname{ad}_{\phi(Y)}}\right)(\phi(Y))\,dt$。
4. [▶ 57:16](https://youtu.be/cPIt_ajpSlU?t=3436) 這正是 (3.6) 把 $X, Y$ 換成 $\phi(X), \phi(Y)$，所以等於 $\log(e^{\phi(X)}e^{\phi(Y)})$。∎

【口頭】[▶ 52:50](https://youtu.be/cPIt_ajpSlU?t=3170) 澄清：這裡**假設** BCH（Thm. 3.3）已知，它在後面的小節（§3.4）才證。

## 5. 預告：指數映射的導數

[▶ 58:51](https://youtu.be/cPIt_ajpSlU?t=3531) §3.3「全是很有趣的計算想法」。若 $X, Y$ 交換，$e^{X + tY} = e^Xe^{tY}$，$\frac{d}{dt}e^{X+tY} = e^XY$。[▶ 59:28](https://youtu.be/cPIt_ajpSlU?t=3568) 不交換時呢？影片在這裡斷掉，接 part 2。

## 6. 一頁速查表

| 敘述 | 關鍵一步 |
|---|---|
| $[X,[X,Y]] = [Y,[X,Y]] = 0\Rightarrow e^Xe^Y = e^{X+Y+\frac12[X,Y]}$ | $A(t)$、$B(t)$ 滿足同一個 ODE |
| $Xe^{tY} = e^{tY}e^{-t\operatorname{ad}_Y}(X)$ | $\operatorname{Ad}_{e^{-tY}} = e^{-t\operatorname{ad}_Y}$ |
| $e^{-t\operatorname{ad}_Y}(X) = X + t[X, Y]$ | 級數因 $[Y,[Y,X]] = 0$ 截斷 |
| Heisenberg 李代數：$3\times 3$ 嚴格上三角 | 兩次括號就是 0 |
| Heisenberg：李代數同態 ⟹ 群同態 | $\exp$ 是雙射，$\Phi = \exp\circ\phi\circ\log$ |
| $g(z) = \frac{\log z}{1 - 1/z} = \sum a_m(z-1)^m$，$g(1) = 1$ | 在 $\lvert z - 1\rvert < 1$ 解析 |
| BCH：$\log(e^Xe^Y) = X + \int_0^1 g(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y})(Y)\,dt$ | 只用 $\operatorname{ad}_X, \operatorname{ad}_Y$ |
| $\phi(\log(e^Xe^Y)) = \log(e^{\phi(X)}e^{\phi(Y)})$ | $\phi\circ\operatorname{ad}_Y = \operatorname{ad}_{\phi(Y)}\circ\phi$，穿過冪級數和積分 |

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\frac{d}{dt}e^{X+tY}$ | 下一集：指數映射的導數（Hall §3.3） |
| BCH 積分形式的證明 | Hall §3.4（April 18） |
| BCH 的級數係數 | April 18：BCH 的計算 |
| Cor. 3.4 | 單連通群上李代數同態升成群同態（April 25） |

---

## 附：本集一句話總結

> **當 $[X, Y]$ 和 $X, Y$ 都交換時，引入參數 $t$、比較兩邊滿足的 ODE，再用 $\operatorname{Ad}_{e^{-tY}} = e^{-t\operatorname{ad}_Y}$ 讓巢狀交換子截斷，就證出 $e^Xe^Y = e^{X+Y+\frac12[X,Y]}$；一般情況則有 BCH 的積分形式，它把 $\log(e^Xe^Y)$ 完全用 $\operatorname{ad}_X, \operatorname{ad}_Y$ 寫出來，所以李代數同態能整個「穿過」它。**
