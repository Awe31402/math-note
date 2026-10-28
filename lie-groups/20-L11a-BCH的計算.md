---
course: Matrix Lie Groups (Spring 2016)
episode: 20
lecture: L11a
date: 2016-04-18（part 1）
video: https://www.youtube.com/watch?v=zAEudNoxelM
notes: Hall 第 1 版 Thm. 3.5（p.70）、§3.4 BCH 的證明（p.73–74）、§3.5 級數形式（p.74–76）
---

# 第 20 集 · L11a：BCH 積分形式的證明、用 g(z) 算級數 [▶ 影片](https://www.youtube.com/watch?v=zAEudNoxelM&list=PLBY4G2o7DhF3FS2CaX62eiQWGP9_xdLYs)

← 上一集：[[19-L10b-指數映射的導數]] ｜ [總目錄](README.md) ｜ 下一集：[[21-L11b-BCH三階項]] →

> **課程**：Matrix Lie Groups（Liberty University，Spring 2016）— 第 20 集，April 18 part 1
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ Hall《Lie Groups, Lie Algebras, and Representations》第 1 版 §3.3–3.5（p.70–76）
> **標記說明**：`【口頭】` 老師口頭補充、課本沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【課本補充】` 課本有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習 Thm. 3.5](#1-複習-thm-35)
- [2. BCH 積分形式的證明（Hall §3.4）](#2-bch-積分形式的證明hall-34)
  - [2.1 引入參數](#21-引入參數)
  - [2.2 用 Thm. 3.5](#22-用-thm-35)
  - [2.3 用 Ad 和 ad 的關係](#23-用-ad-和-ad-的關係)
  - [2.4 認出 g，積分](#24-認出-g積分)
- [3. g(z) 的級數](#3-gz-的級數)
- [4. 展開 e^{ad_X}e^{t ad_Y} − I](#4-展開-eadxet-ady--i)
- [5. 一階和二階：X + Y + ½[X, Y]](#5-一階和二階x--y--½x-y)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:03](https://youtu.be/zAEudNoxelM?t=3) 【口頭】禱告：「求祢讓我們成功算出再下一階。」「$\frac1{12}$ 那項今天一定拿得到。問題是能不能更進一步，還是我們會說『喔，這就是為什麼大家不算到那裡』。」

## 1. 複習 Thm. 3.5

[▶ 00:41](https://youtu.be/zAEudNoxelM?t=41) 不證，直接用（上一集）：

$$
\frac{d}{dt}e^{X+tY}|_{t=0} = e^X\left\{\frac{I - e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}(Y)\right\},\qquad
\frac{d}{dt}e^{X(t)} = e^{X(t)}\left\{\frac{I - e^{-\operatorname{ad}_{X(t)}}}{\operatorname{ad}_{X(t)}}\left(\frac{dX}{dt}\right)\right\}.
$$

[▶ 02:08](https://youtu.be/zAEudNoxelM?t=128) 括號裡的冪級數：

$$
\frac{1 - e^{-z}}{z} = \sum_{n=0}^\infty\frac{(-1)^nz^n}{(n+1)!} = 1 - \frac{z}{2!} + \frac{z^2}{3!} - \frac{z^3}{4!} + \cdots
$$

⚠️ 逐字稿缺字：[▶ 02:47](https://youtu.be/zAEudNoxelM?t=167) 老師寫了幾次才寫對（漏了 $(-1)^n$、指數的位置）。上式依 Hall p.70。

【口頭】[▶ 06:32](https://youtu.be/zAEudNoxelM?t=392) Thm. 3.5 的證明兩頁，用的是「除以 $m$、取 $m$ 次方、$m\to\infty$」那個狡猾的技巧（Lie 乘積公式也用過）。

## 2. BCH 積分形式的證明（Hall §3.4）

[▶ 07:06](https://youtu.be/zAEudNoxelM?t=426) 「走過證明，會幫我們看懂後面的計算，值得。」

### 2.1 引入參數

[▶ 07:50](https://youtu.be/zAEudNoxelM?t=470) $X, Y$ 固定、夠小。對 $0\le t\le 1$ 定義

$$
Z(t) = \log\left(e^Xe^{tY}\right),\qquad\text{所以}\quad e^{Z(t)} = e^Xe^{tY}.
$$

### 2.2 用 Thm. 3.5

[▶ 09:03](https://youtu.be/zAEudNoxelM?t=543)

$$
e^{-Z(t)}\frac{d}{dt}e^{Z(t)} = \left(e^Xe^{tY}\right)^{-1}e^Xe^{tY}Y = Y.
$$

[▶ 10:29](https://youtu.be/zAEudNoxelM?t=629) 微分時 $e^X$ 是常數，$e^{tY}$ 的導數是 $e^{tY}Y$；前面是反元素，抵消。

[▶ 11:41](https://youtu.be/zAEudNoxelM?t=701) 另一方面，由 (3.10)，左邊也等於

$$
\frac{I - e^{-\operatorname{ad}_{Z(t)}}}{\operatorname{ad}_{Z(t)}}\left(\frac{dZ}{dt}\right).
$$

所以

$$
\frac{I - e^{-\operatorname{ad}_{Z(t)}}}{\operatorname{ad}_{Z(t)}}\left(\frac{dZ}{dt}\right) = Y.
$$

【Q&A】[▶ 12:22](https://youtu.be/zAEudNoxelM?t=742) 學生：可以把 $e^Xe^{tY}$ 寫成 $e^{X + tY}$ 再套 Thm. 3.5 嗎？老師：不行，一般不能那樣合併。用的是 (3.10)，$X(t)$ 換成 $Z(t)$。學生又提醒：左邊還有 $e^{-Z}$，兩邊的 $e^{\pm Z}$ 抵消。

[▶ 14:10](https://youtu.be/zAEudNoxelM?t=850) $X, Y$ 夠小 ⟹ $Z(t)$ 也小 ⟹ 那個算子接近恆等、**可逆**。解出

$$
\frac{dZ}{dt} = \left\{\frac{I - e^{-\operatorname{ad}_{Z(t)}}}{\operatorname{ad}_{Z(t)}}\right\}^{-1}(Y).
$$

【口頭】[▶ 14:42](https://youtu.be/zAEudNoxelM?t=882) 「很好，但這怎麼會有幫助？還不知道。我只知道過去幾週講的主角**全都上場了**。」

### 2.3 用 Ad 和 ad 的關係

[▶ 15:14](https://youtu.be/zAEudNoxelM?t=914) 把 $e^{Z(t)} = e^Xe^{tY}$ 餵給大 $\operatorname{Ad}$（它是群同態）：

$$
\operatorname{Ad}_{e^{Z(t)}} = \operatorname{Ad}_{e^X}\operatorname{Ad}_{e^{tY}}.
$$

[▶ 16:43](https://youtu.be/zAEudNoxelM?t=1003) 用 $\operatorname{Ad}_{e^W} = e^{\operatorname{ad}_W}$：

$$
e^{\operatorname{ad}_{Z(t)}} = e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y},\qquad\text{所以}\quad\operatorname{ad}_{Z(t)} = \log\left(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}\right).
$$

### 2.4 認出 g，積分

[▶ 19:06](https://youtu.be/zAEudNoxelM?t=1146) 代回去（令 $A = e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}$，則 $e^{-\operatorname{ad}_Z} = A^{-1}$、$\operatorname{ad}_Z = \log A$）：

$$
\frac{dZ}{dt} = \left\{\frac{I - A^{-1}}{\log A}\right\}^{-1}(Y).
$$

【課堂討論】[▶ 19:56](https://youtu.be/zAEudNoxelM?t=1196)–[▶ 28:36](https://youtu.be/zAEudNoxelM?t=1716) Hall 寫 $g(z) = \left\{\frac{1 - z^{-1}}{\log z}\right\}^{-1}$。全班以為 $\{\cdot\}^{-1}$ 是**反函數**，花了很久想驗證「$g$ 的反函數是這個」，試著展開 $\log z$ 做長除法，一直對不上。

[▶ 28:02](https://youtu.be/zAEudNoxelM?t=1682) 老師恍然大悟：「好丟臉。」這裡的 $\{\cdot\}^{-1}$ 是**倒數**，而且這個 $g$ 就是第 18 集定義的那個：

$$
g(z) = \frac{\log z}{1 - z^{-1}} = \frac{z\log z}{z - 1}.
$$

[▶ 28:36](https://youtu.be/zAEudNoxelM?t=1716) 「你們被我錯誤的標記帶偏了，以為我在連結別的東西。」「我們沒看懂反而是好事——要是看懂了才更慘。」

[▶ 31:14](https://youtu.be/zAEudNoxelM?t=1874) 所以

$$
\frac{dZ}{dt} = g\left(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}\right)(Y).
$$

[▶ 31:46](https://youtu.be/zAEudNoxelM?t=1906) 【口頭】這有一個**形式**上的步驟：在複數上取倒數沒問題，但換成算子的冪級數，怎麼知道算子的版本也互為倒數？這要用級數小心證明，Hall 說「不難證」。

[▶ 32:18](https://youtu.be/zAEudNoxelM?t=1938) 從 0 積到 1：

$$
Z(1) - Z(0) = \int_0^1g\left(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}\right)(Y)\,dt.
$$

[▶ 33:32](https://youtu.be/zAEudNoxelM?t=2012) $Z(1) = \log(e^Xe^Y)$，$Z(0) = \log e^X = X$。這就是 BCH 的積分形式 (3.6)。∎

【口頭】[▶ 34:20](https://youtu.be/zAEudNoxelM?t=2060) 這是「引入參數求積分」那招的**大人版**：想要 $\log(e^Xe^Y)$ 的恆等式，就引入參數 $e^Xe^{tY}$，微分，用一堆狡猾的東西。

[▶ 35:24](https://youtu.be/zAEudNoxelM?t=2124) 【口頭】證明是很多機器的組合：「除以 $m$ 取 $m$ 次方」得到指數的導數、大伴隨的同態性質、大小伴隨的關係。Stillwell 的 Eichler 證明不靠這些（三頁純代數），「但我喜歡這本書的方式，它讓你開始想伴隨映射這些東西，它們在李群和李代數裡會有自己的生命。」

## 3. g(z) 的級數

[▶ 36:31](https://youtu.be/zAEudNoxelM?t=2191)

$$
g(z) = \frac{z\log z}{z - 1} = \frac{(z - 1) + 1}{z - 1}\cdot\log z.
$$

[▶ 37:07](https://youtu.be/zAEudNoxelM?t=2227) 展開 $\log z$（學生提醒公式；第 11 集推過）：

$$
\log z = \sum_{m=1}^\infty\frac{(-1)^{m+1}}{m}(z - 1)^m = (z - 1) - \frac{(z-1)^2}{2} + \frac{(z-1)^3}{3} - \cdots
$$

[▶ 39:23](https://youtu.be/zAEudNoxelM?t=2363) 除以 $z - 1$，換指標 $j = m - 1$：

$$
\frac{\log z}{z - 1} = \sum_{j=0}^\infty\frac{(-1)^j}{j + 1}(z - 1)^j.
$$

[▶ 41:07](https://youtu.be/zAEudNoxelM?t=2467) 乘上 $1 + (z - 1)$，把 $j = 0$ 的項拿出來，[▶ 41:45](https://youtu.be/zAEudNoxelM?t=2505) 合併同次項並通分（學生建議）：

$$
\frac{(-1)^j}{j+1} + \frac{(-1)^{j-1}}{j} = (-1)^{j+1}\left(\frac1j - \frac1{j+1}\right) = \frac{(-1)^{j+1}}{j(j+1)}.
$$

[▶ 42:25](https://youtu.be/zAEudNoxelM?t=2545)

$$
\boxed{\ g(z) = 1 + \sum_{j=1}^\infty\frac{(-1)^{j+1}}{j(j+1)}(z - 1)^j = 1 + \frac12(z-1) - \frac16(z-1)^2 + \frac1{12}(z-1)^3 - \cdots\ }
$$

【口頭】「就像把一個部分分式的題目反過來做——像伸縮級數，但反伸縮。」

> 【課本補充】Hall p.75 給的閉式完全相同：$g(z) = 1 + \sum_{m\ge 1}\frac{(-1)^{m+1}}{m(m+1)}(z-1)^m$。

## 4. 展開 e^{ad_X}e^{t ad_Y} − I

[▶ 43:48](https://youtu.be/zAEudNoxelM?t=2628) 【口頭】「我要試著算到**三階**，書上只算到二階。用 BCH 公式推出 BCH 關係。」

[▶ 47:00](https://youtu.be/zAEudNoxelM?t=2820) 【Q&A】學生：為什麼要減 $I$？老師：$g$ 是以 $z = 1$ 為中心展開的，要代入 $z = e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}$，所以需要 $z - 1$ 也就是 $e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y} - I$。[▶ 48:41](https://youtu.be/zAEudNoxelM?t=2921) 好消息是 $I$ 抵消。

[▶ 45:02](https://youtu.be/zAEudNoxelM?t=2702)

$$
e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y} - I = \left(I + \operatorname{ad}_X + \tfrac12\operatorname{ad}_X^2 + \tfrac16\operatorname{ad}_X^3 + \cdots\right)\left(I + t\operatorname{ad}_Y + \tfrac{t^2}{2}\operatorname{ad}_Y^2 + \cdots\right) - I.
$$

[▶ 49:20](https://youtu.be/zAEudNoxelM?t=2960)–[▶ 52:47](https://youtu.be/zAEudNoxelM?t=3167) 按次數整理（學生幫忙）：

$$
\begin{aligned}
&\text{一階：}\ \operatorname{ad}_X + t\operatorname{ad}_Y\\
&\text{二階：}\ \tfrac12\operatorname{ad}_X^2 + t\operatorname{ad}_X\operatorname{ad}_Y + \tfrac{t^2}{2}\operatorname{ad}_Y^2\\
&\text{三階：}\ \tfrac16\operatorname{ad}_X^3 + \tfrac t2\operatorname{ad}_X^2\operatorname{ad}_Y + \tfrac{t^2}{2}\operatorname{ad}_X\operatorname{ad}_Y^2 + \tfrac{t^3}{6}\operatorname{ad}_Y^3
\end{aligned}
$$

[▶ 50:35](https://youtu.be/zAEudNoxelM?t=3035) 【口頭】偷懶的方法：最後要**作用在 $Y$ 上**，而 $\operatorname{ad}_Y(Y) = [Y, Y] = 0$。所以**任何最右邊是 $\operatorname{ad}_Y$ 的項都是 0**。[▶ 52:02](https://youtu.be/zAEudNoxelM?t=3122)「但我不能太早丟掉它們——要等代進 $g$ 的級數之後才能丟，太早丟會搞混。」

> 【課本補充】Hall p.75 的關鍵觀察：$e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y} - I$ **沒有零階項**，所以 $(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y} - I)^m$ 只貢獻 $m$ 階以上的項。要算到 $k$ 階，$g$ 只需要展開到 $(z-1)^k$。

## 5. 一階和二階：X + Y + ½[X, Y]

[▶ 54:21](https://youtu.be/zAEudNoxelM?t=3261) 代入 $g(z) = 1 + \frac12(z - 1) - \frac16(z-1)^2 + \cdots$，作用在 $Y$ 上，按「巢狀交換子的層數」分組。

- **零個交換子**：$g$ 的常數 $1$ 給 $I(Y) = Y$。
- **一個交換子**：[▶ 54:56](https://youtu.be/zAEudNoxelM?t=3296) 只有 $\frac12(z - 1)$ 的一階部分：
$$
\tfrac12(\operatorname{ad}_X + t\operatorname{ad}_Y)(Y) = \tfrac12[X, Y] + \tfrac t2[Y, Y] = \tfrac12[X, Y].
$$

【口頭】[▶ 55:28](https://youtu.be/zAEudNoxelM?t=3328) 為什麼能分層：$z - 1$ 沒有常數項，所以 $(z-1)^2$ 只有兩層以上的巢狀交換子，依此類推。[▶ 56:32](https://youtu.be/zAEudNoxelM?t=3392)「一旦習慣這種想法，這比上次那堆級數**快太多**了。」

【課堂討論】[▶ 57:43](https://youtu.be/zAEudNoxelM?t=3463) 學生問「$\frac16$ 哪來的」——老師：那是錯的，那項沒有 $t$，應該是 $\frac12\operatorname{ad}_X^2$。

所以到一層交換子：

$$
\log(e^Xe^Y) = X + \int_0^1\left(Y + \tfrac12[X, Y] + \cdots\right)dt = X + Y + \tfrac12[X, Y] + \cdots
$$

[▶ 58:23](https://youtu.be/zAEudNoxelM?t=3503) 二層交換子要看 $\frac12(z-1)$ 的二階部分和 $-\frac16(z-1)^2$。[▶ 58:58](https://youtu.be/zAEudNoxelM?t=3538) $(z - 1)^2$ 到二階：$(\operatorname{ad}_X + t\operatorname{ad}_Y)^2$，其中最右邊是 $\operatorname{ad}_Y$ 的「對我們已經死了」。影片在三階計算中途斷掉，接 part 2。

## 6. 一頁速查表

| 敘述 | 關鍵一步 |
|---|---|
| $Z(t) = \log(e^Xe^{tY})$，$e^{-Z}\frac{d}{dt}e^Z = Y$ | 直接微分 $e^Xe^{tY}$ |
| $\frac{I - e^{-\operatorname{ad}_Z}}{\operatorname{ad}_Z}(Z') = Y$ | Thm. 3.5 的 (3.10) |
| $e^{\operatorname{ad}_{Z(t)}} = e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}$ | $\operatorname{Ad}$ 是同態 ＋ $\operatorname{Ad}_{e^W} = e^{\operatorname{ad}_W}$ |
| $Z'(t) = g(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y})(Y)$，$g(z) = \frac{z\log z}{z-1}$ | $\{\frac{1 - z^{-1}}{\log z}\}^{-1}$ 是**倒數**不是反函數 |
| $g(z) = 1 + \sum_{j\ge1}\frac{(-1)^{j+1}}{j(j+1)}(z-1)^j$ | 展開 $\log z$、合併、通分 |
| $e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y} - I$ 沒有零階項 | $(z-1)^m$ 只貢獻 $m$ 階以上 |
| 最右邊是 $\operatorname{ad}_Y$ 的項作用在 $Y$ 上為 0 | $[Y, Y] = 0$ |
| $\log(e^Xe^Y) = X + Y + \frac12[X,Y] + \cdots$ | $\frac12(\operatorname{ad}_X)(Y)$，積分 |

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 三階項 $\frac1{12}[X,[X,Y]] - \frac1{12}[Y,[X,Y]]$ | 下一集 |
| BCH ＋ 單連通 | 李代數同態升成群同態、萬有覆蓋（April 25） |

---

## 附：本集一句話總結

> **BCH 積分形式的證明把所有主角串起來：引入參數 $Z(t) = \log(e^Xe^{tY})$、用指數映射的導數、用 $\operatorname{Ad}$ 的同態性質和 $\operatorname{Ad}_{e^W} = e^{\operatorname{ad}_W}$，最後認出 $g(z) = \frac{z\log z}{z-1}$；把 $g$ 展開、利用 $\operatorname{ad}_Y(Y) = 0$ 逐層算，就能快速得到 $X + Y + \frac12[X, Y] + \cdots$。**
