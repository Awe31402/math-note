---
course: Number Theory（2021 秋，線上錄影）
episode: 42
lecture: 2021-11-15 第 1 部
date: 2021-11-15
video: https://youtu.be/kNYaxKcq8YY
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.9 Lecture 29（p. 167–169）：Theorem 4.9.18、Example 4.9.19、Theorem 4.9.20、Definition 4.9.21、Example 4.9.22–4.9.24、Definition 4.9.25、Theorem 4.9.26（開頭）
---

# 第 42 集 · 超越元、最小多項式、單擴張（Irreducible Polynomial and Simple Extensions, Part 1） [▶ 影片](https://youtu.be/kNYaxKcq8YY)

← 上一集：[41-extension-fields-2](41-extension-fields-2.md) ｜ [總目錄](README.md) ｜ 下一集：[43-irreducible-polynomial-simple-extensions-2](43-irreducible-polynomial-simple-extensions-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 42 集（2021-11-15 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；開頭 2 分多鐘是課前閒聊；結尾被切斷）＋ 講者講義 §4.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 超越 ⇔ 求值同態是單射](#1-超越--求值同態是單射)
- [2. Q[x] ≅ Q[π]](#2-qx--qπ)
- [3. 最小多項式存在、不可約、唯一](#3-最小多項式存在不可約唯一)
- [4. 定義：irr(α, F) 和 deg(α, F)](#4-定義irrα-f-和-degα-f)
- [5. 例子](#5-例子)
- [6. 單擴張 F(α)](#6-單擴張-fα)
- [7. F(α) 的基底是 1, α, …, αⁿ⁻¹（開頭）](#7-fα-的基底是-1-α--αⁿ⁻¹開頭)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:01](https://youtu.be/kNYaxKcq8YY?t=1)

課前講者和學生閒聊 YouTube 的審查（他說他盡量不剪片，但怕課堂上順口講的話讓頻道多年後被封，而且審查的會是機器人）。[▶ 02:23](https://youtu.be/kNYaxKcq8YY?t=143)「回到數學。」

今天：超越元的刻畫、**最小多項式**（講義叫「$\alpha$ 的不可約多項式」）、**單擴張**。講者：「你們很多作業就是根據這個定義。」

---

## 1. 超越 ⇔ 求值同態是單射

[▶ 02:23](https://youtu.be/kNYaxKcq8YY?t=143)

> **定理**（講義 Theorem 4.9.18）：$E$ 是 $F$ 的擴張體，$\alpha\in E$。則 $\alpha$ 在 $F$ 上超越 ⇔ 求值同態 $\varphi_\alpha:F[x]\to E$ 給出 $F[x]$ 跟 $E$ 的一個**子整環**的同構。特別是：$\alpha$ 超越 ⇔ $\varphi_\alpha$ 是單射。

（講者：「我不說**子體**，因為它可能不是子體。」）

**回顧** [▶ 04:22](https://youtu.be/kNYaxKcq8YY?t=262)：$\alpha$ 在 $F$ 上代數 ⇔ 存在非零 $p(x)\in F[x]$，$\varphi_\alpha(p) = p(\alpha) = 0$。否則超越。例：$\pi$ 在 $\mathbb{R}$ 上代數（$x-\pi$），在 $\mathbb{Q}$ 上超越。「我們預設以有理數當背景，但在這門課我們盡量講清楚基體。」

**證明**：

**(⇒)** [▶ 07:24](https://youtu.be/kNYaxKcq8YY?t=444)：$\ker\varphi_\alpha = \{f\in F[x] : f(\alpha) = 0\}$。$\alpha$ 超越，所以裡面**只有零多項式**——有非零的就代表 $\alpha$ 是代數的。$\ker\varphi_\alpha = \{0\}$。群論定理：核是單位元 ⇒ 一對一。

**(⇐)** [▶ 09:31](https://youtu.be/kNYaxKcq8YY?t=571)：設 $\varphi_\alpha$ 一對一。$\varphi_\alpha(0) = 0$（零多項式代 $\alpha$ 還是 0）。若 $f(\alpha) = 0$，則 $\varphi_\alpha(f) = \varphi_\alpha(0)$，一對一 ⇒ $f = 0$。所以**只有零多項式**以 $\alpha$ 為根，$\alpha$ 不是代數的。（講者：「我講得不夠快到重點。」）

**同構的部分** [▶ 13:35](https://youtu.be/kNYaxKcq8YY?t=815)（「我忘了同構那部分，我很糟」）：**第一同構定理**，
$$F[x]/\ker\varphi_\alpha\cong\varphi_\alpha(F[x]).$$
超越時核是 $\{0\}$，$F[x]/\{0\}\cong F[x]$，所以
$$F[x]\cong\varphi_\alpha(F[x]) = \{f(\alpha) : f\in F[x]\}.$$

講者 [▶ 12:22](https://youtu.be/kNYaxKcq8YY?t=742)：講這個證明主要是**再提醒一次多項式和求值同態的互動**——「這是重頭戲」。

---

## 2. Q[x] ≅ Q[π]

[▶ 15:14](https://youtu.be/kNYaxKcq8YY?t=914)（講義 Example 4.9.19）

$\pi$ 在 $\mathbb{Q}$ 上超越，所以
$$\mathbb{Q}[x]\cong\mathbb{Q}[\pi],\qquad a_0+a_1x+\cdots+a_nx^n\mapsto a_0+a_1\pi+\cdots+a_n\pi^n.$$
「這個同構很蠢」——就是在 $\pi$ 求值。

**它是體嗎？** [▶ 16:58](https://youtu.be/kNYaxKcq8YY?t=1018) 這是環同構，不能一邊是體一邊不是。$\mathbb{Q}[x]$ **不是體**（單位只有非零常數），例如 $2+x$ 的反元素不在 $\mathbb{Q}[x]$ 裡。所以 $\mathbb{Q}[\pi]$ 也不是體。

$\frac1{2+x}$ 在**有理式** $\mathbb{Q}(x)$ 裡（講者說該叫有理式不叫有理函數，「我想區分函數和式子」）。有理式成一個體，非零元素的反元素就是倒數。

**超越元的意義** [▶ 18:36](https://youtu.be/kNYaxKcq8YY?t=1116)：超越元就像**不定元**，可以寫它的多項式。$\pi$ 的各次方在 $\mathbb{Q}$ 上**線性獨立**。

⚠️ 字幕這裡講者說「若不線性獨立，就代表 $\pi$ 是有理數」，但線性相依其實代表 $\pi$ 是**代數數**（不只是有理數）。以下**不是逐字稿內容**，是依定義推論的：$\pi$ 的次方線性相依 ⇔ 有非零的 $c_0+c_1\pi+\cdots+c_n\pi^n = 0$ ⇔ $\pi$ 在 $\mathbb{Q}$ 上代數。講者接著說「我沒證明的巨大主張是 $\pi$ 不是有理數，那很難證」，應指 $\pi$ 的超越性。屬口誤，不列進待確認清單。

> 【講義補充】Example 4.9.19（p. 168）：$\mathbb{Q}(\pi)$（含 $\mathbb{Q}$ 和 $\pi$ 的最小體）**不等於** $\varphi_\pi(\mathbb{Q}[x]) = \mathbb{Q}[\pi]$。$\mathbb{Q}(\pi)$ 是 $\mathbb{Q}[\pi]$ 的**分式體**，可以想成以 $\pi$ 為變數的有理函數。一般地，$F[x]$ 包含在分式體 $F(x)$ 裡。

---

## 3. 最小多項式存在、不可約、唯一

[▶ 19:36](https://youtu.be/kNYaxKcq8YY?t=1176)

講者：Theorem 4.9.20「其實又是體論基本定理，只是換了衣服」。

> **定理**（講義 Theorem 4.9.20）：$E$ 是 $F$ 的擴張體，$\alpha\in E$ 在 $F$ 上代數。則
> 1. 存在不可約的 $p(x)\in F[x]$ 使 $p(\alpha) = 0$；
> 2. $p(x)$ 在差一個 $F$ 的非零常數倍之外唯一，是以 $\alpha$ 為根的**次數最小**的多項式；
> 3. 若 $f(\alpha) = 0$、$f\neq0$，則 $p(x)\mid f(x)$。

講者 [▶ 20:42](https://youtu.be/kNYaxKcq8YY?t=1242)：跟 Kronecker 定理（第 40 集）不太一樣——那個說存在擴張體使 $p$ 有根；這個是**已經有**擴張體和代數元 $\alpha$，找出殺掉它的不可約多項式。

**證明**：

1. 一開始講者想用 UFD 把 $f$ 分解成不可約因式 [▶ 23:54](https://youtu.be/kNYaxKcq8YY?t=1434)，然後說：「這是個壞選擇，這個兔子洞會帶我們跑很遠。讓我在它浪費更多時間前擦掉。順帶一提，我有備課。」
2. **改用 PID** [▶ 24:50](https://youtu.be/kNYaxKcq8YY?t=1490)：$F[x]$ 是 PID（例如：次數當範數是 Euclid 整環 ⇒ PID）。$\ker\varphi_\alpha$ 是理想，所以 $\ker\varphi_\alpha = \langle p(x)\rangle$。
3. 生成元就是核裡**次數最小**的非零多項式（第 36 集 Theorem 4.5.18）[▶ 26:28](https://youtu.be/kNYaxKcq8YY?t=1588)。講者重講了原因：理想裡多項式的次數是整數子集，良序原理取最小；別的東西若生成它，次數會比最小的還小。（「真希望我記得最近三講教了什麼。」）
4. **整除** [▶ 31:50](https://youtu.be/kNYaxKcq8YY?t=1910)：$f(\alpha) = 0$ ⇒ $f\in\ker\varphi_\alpha = \langle p\rangle$ ⇒ $f = pg$，$p\mid f$。
5. **不可約** [▶ 30:44](https://youtu.be/kNYaxKcq8YY?t=1844)：若 $p = gh$，$g,h$ 都不是常數，則 $p(\alpha) = g(\alpha)h(\alpha) = 0$，$g(\alpha) = 0$ 或 $h(\alpha) = 0$——次數比 $p$ 小的多項式以 $\alpha$ 為根，矛盾。
6. **唯一** [▶ 32:32](https://youtu.be/kNYaxKcq8YY?t=1952)：若 $\langle p\rangle = \langle\bar p\rangle$，PID（整環）裡同一個主理想的兩個生成元**相伴**（第 39 集）。$F[x]$ 的單位是非零常數，所以 $p = c\bar p$。∎

（講者：「我想寫 $p'$，但那會想到導數，改寫 $\bar p$。」）

---

## 4. 定義：irr(α, F) 和 deg(α, F)

[▶ 34:04](https://youtu.be/kNYaxKcq8YY?t=2044)

講者：「這些鋪陳都是為了確保接下來的定義是合理的。」

> **定義**（講義 Definition 4.9.21）：$E$ 是 $F$ 的擴張體，$\alpha\in E$ 在 $F$ 上代數。以 $\alpha$ 為根、**次數最小的唯一首一多項式** $p(x)\in F[x]$ 叫做 **$\alpha$ 在 $F$ 上的不可約多項式**，記作
> $$\mathrm{irr}(\alpha,F) = p(x),\qquad\deg(\alpha,F) = \deg\big(\mathrm{irr}(\alpha,F)\big)\ (\alpha\text{ 在 }F\text{ 上的次數}).$$

**首一**（monic）【課堂討論】[▶ 37:03](https://youtu.be/kNYaxKcq8YY?t=2223)：學生答「最高項是 1 或 0」，講者：「接近了」——**首項係數是 1**。例：$x^3+2x-7$ 是首一的，$2x^3+1$ 不是。

（「首一」把「差一個常數倍」的不唯一性消掉，所以是**唯一**的。很多書叫它**最小多項式**。）

---

## 5. 例子

[▶ 38:06](https://youtu.be/kNYaxKcq8YY?t=2286)

| 例 | $\alpha$ | $F$ | $\mathrm{irr}(\alpha,F)$ | $\deg$ | 理由 |
|---|---|---|---|---|---|
| 5 | $i$ | $\mathbb{R}$ | $x^2+1$ | 2 | 沒有一次的實多項式以 $i$ 為根 |
| 6 | $\sqrt2$ | $\mathbb{Q}$ | $x^2-2$ | 2 | Eisenstein（$p=2$） |
| 7 | $\pi$ | $\mathbb{R}$ | $x-\pi$ | 1 | |
| 8 | $c\in F$ | $F$ | $x-c$ | 1 | |
| 9 | $\sqrt[5]2$ | $\mathbb{Q}$ | $x^5-2$ | 5 | Eisenstein（$p=2$） |

**$\sqrt2$** [▶ 40:43](https://youtu.be/kNYaxKcq8YY?t=2443)：講者說用 Eisenstein 是「殺雞用牛刀」：$2\mid -2$（和 0），$2\nmid 1$，**而且 $4\nmid -2$**——「我上次沒強調，常數項也要 $p^2$ 不整除」。更直接：一次式以 $\sqrt2$ 為根就代表 $\pm\sqrt2$ 是有理數，荒謬。

**$c\in F$** [▶ 42:14](https://youtu.be/kNYaxKcq8YY?t=2534)：「很蠢但對。」限制在於寫下的必須是 $F$ 上的多項式。例 5 不能寫 $x-i$，因為 $i$ 不是實數。有趣的情況通常是 $c\notin F$。

**$\sqrt[5]2$** [▶ 43:18](https://youtu.be/kNYaxKcq8YY?t=2598)：$x^5-2$ 由 Eisenstein（$p=2$）不可約。六次方根、七次方根……都一樣。

**$2^{3/2}$？** [▶ 44:21](https://youtu.be/kNYaxKcq8YY?t=2661)：講者想到 $\alpha = 2^{3/2}$，平方得 $\alpha^2 = 8$，說 $x^2-8$「大概是」它的不可約多項式，但「我不確定那是真的」，請學生提醒他回頭看。

講者在第 43 集回頭處理：用模 3 判別法證 $x^2-8$ 不可約（模 3 是 $x^2+1$，沒有根），所以 $\mathrm{irr}(2^{3/2},\mathbb{Q}) = x^2-8$，而且 $\mathbb{Q}(2^{3/2}) = \mathbb{Q}(\sqrt2)$。

> 以下**不是逐字稿內容**，是另一個看法：$2^{3/2} = 2\sqrt2$ 是 $x^2-8$ 的根。$x^2-8$ 是 2 次，有根 ⇔ 可約（第 36 集），而它的根 $\pm2\sqrt2$ 都不是有理數，所以在 $\mathbb{Q}$ 上不可約。因此 $\mathrm{irr}(2^{3/2},\mathbb{Q}) = x^2-8$，$\deg = 2$。（Eisenstein 在這裡不能直接用：$p=2$ 時 $4\mid 8$。）

---

## 6. 單擴張 F(α)

[▶ 46:45](https://youtu.be/kNYaxKcq8YY?t=2805)

> **定義**（講義 Definition 4.9.25）：若存在 $\alpha\in E$ 使 $E = F(\alpha)$，就說 $E$ 是 $F$ 的**單擴張**（simple extension）。
> - $F(\alpha)$：包含 $F$ 和 $\alpha$ 的最小的體；
> - $F(\alpha,\beta)$、$F(\alpha_1,\dots,\alpha_n)$：包含 $F$ 和這些元素的最小的體。

（講者說通常想要 $\alpha\notin F$，但講義沒寫這條。）

**單擴張只用一個元素**：$F(\alpha,\beta)$ 要是單擴張，必須存在 $\gamma$ 使 $F(\alpha,\beta) = F(\gamma)$。

**例：$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt6)$？** [▶ 48:47](https://youtu.be/kNYaxKcq8YY?t=2927) 講者：「我相信是，但可能錯。」試了一下：$\sqrt6 = \sqrt2\sqrt3$，但從 $\sqrt6$ 拿回 $\sqrt2$、$\sqrt3$ 沒算出來（「可惡」）。「與其燒課堂時間，我把它留成問題，你們可以證明或否證。」

講者在第 43 集說：「**這是錯的。**」

> 以下**不是逐字稿內容**，是依第 44 集的次數公式補理由：$\mathbb{Q}(\sqrt6)$ 在 $\mathbb{Q}$ 上是 2 維（$\mathrm{irr} = x^2-6$），而 $\mathbb{Q}(\sqrt2,\sqrt3)$ 是 4 維（基底 $1,\sqrt2,\sqrt3,\sqrt6$）。但 $\mathbb{Q}(\sqrt2,\sqrt3)$ **還是單擴張**：$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3)$。令 $\gamma = \sqrt2+\sqrt3$，$\gamma^2 = 5+2\sqrt6$，$\gamma^3 = 11\sqrt2+9\sqrt3$，所以 $\sqrt2 = \frac{\gamma^3-9\gamma}2$、$\sqrt3 = \frac{11\gamma-\gamma^3}2$ 都在 $\mathbb{Q}(\gamma)$ 裡。（第 45 集的本原元素定理說特徵 0 時這總是做得到。）

> 【講義補充】講義（p. 169）：$F(\alpha)$ 也可以定義成所有包含 $F$ 和 $\alpha$ 的體的交集。「$F(\alpha)$ 叫 $F$ 添加 $\alpha$。希望你原諒我之前沒正式定義就用了這些詞，遲到總比不到好。」

---

## 7. F(α) 的基底是 1, α, …, αⁿ⁻¹（開頭）

[▶ 51:12](https://youtu.be/kNYaxKcq8YY?t=3072)

> **定理**（講義 Theorem 4.9.26）：$E = F(\alpha)$ 是單擴張，$\alpha$ 在 $F$ 上代數，$\deg(\alpha,F) = n\ge1$。則每個 $\beta\in E$ 都能**唯一地**寫成
> $$\beta = b_0+b_1\alpha+b_2\alpha^2+\cdots+b_{n-1}\alpha^{n-1},\qquad b_i\in F.$$

**這定理真正在說什麼** [▶ 52:55](https://youtu.be/kNYaxKcq8YY?t=3175)：$\{1,\alpha,\dots,\alpha^{n-1}\}$ 是 $F(\alpha)$ 作為 $F$ 上向量空間的**基底**。

- 「每個 $\beta$ 都能寫成」= 生成集（spanning set）。
- 「係數唯一」= 線性獨立（線性獨立的一種刻畫：對基底的座標唯一）。

**證明開頭** [▶ 54:34](https://youtu.be/kNYaxKcq8YY?t=3274)：

1. 設 $\mathrm{irr}(\alpha,F) = p(x) = x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$（首一）。$p(\alpha) = 0$，所以
   $$\alpha^n = -a_{n-1}\alpha^{n-1}-\cdots-a_1\alpha-a_0 = -\sum_{k=0}^{n-1}a_k\alpha^k.\qquad(\star)$$
2. 包含 $\alpha$ 和 $F$ 的最小體是 $E = F[x]/\langle p\rangle$，$\alpha = x+\langle p\rangle$（前面討論過）[▶ 56:08](https://youtu.be/kNYaxKcq8YY?t=3368)。
3. 任意元素 $\beta = b_0+b_1\alpha+\cdots+b_m\alpha^m$（代表元是 $m$ 次多項式，再用 $x^j+\langle p\rangle = \alpha^j$）。
4. 要證能再化簡：若 $m<n$ 就做完了。講者把「是 $1,\alpha,\dots,\alpha^{n-1}$ 的線性組合」這件事取名「**小精靈**（Pac-Man）」[▶ 58:55](https://youtu.be/kNYaxKcq8YY?t=3535)，打算對 $m\ge n$ 歸納。（影片在這裡被切斷，接第 43 集。）

---

## 8. 一頁速查表

**超越 ⇔ $\varphi_\alpha$ 單射**：核 = 以 $\alpha$ 為根的多項式；超越 ⇔ 核 = $\{0\}$。此時 $F[x]\cong F[\alpha]$（第一同構定理）。例：$\mathbb{Q}[x]\cong\mathbb{Q}[\pi]$，不是體；$\mathbb{Q}(\pi)$ 是它的分式體。

**最小多項式**（$\alpha$ 代數）

| 性質 | 關鍵一步 |
|---|---|
| 存在 | $F[x]$ 是 PID：$\ker\varphi_\alpha = \langle p\rangle$，$p$ = 核裡次數最小的 |
| 整除 | $f(\alpha) = 0$ ⇒ $f\in\langle p\rangle$ ⇒ $p\mid f$ |
| 不可約 | $p = gh$ ⇒ $g(\alpha) = 0$ 或 $h(\alpha) = 0$，次數更小，矛盾 |
| 唯一（差常數倍） | 同一個主理想的生成元相伴；單位 = 非零常數 |

$\mathrm{irr}(\alpha,F)$ = **首一**（首項係數 1）的那個；$\deg(\alpha,F) = \deg\mathrm{irr}(\alpha,F)$。

| $\alpha$ | $F$ | $\mathrm{irr}$ | $\deg$ |
|---|---|---|---|
| $i$ | $\mathbb{R}$ | $x^2+1$ | 2 |
| $\sqrt2$ | $\mathbb{Q}$ | $x^2-2$ | 2 |
| $\sqrt[5]2$ | $\mathbb{Q}$ | $x^5-2$ | 5 |
| $c\in F$ | $F$ | $x-c$ | 1 |

**單擴張** $E = F(\alpha)$。**基底定理**：$\deg(\alpha,F) = n$ ⇒ $F(\alpha)$ 的元素唯一地寫成 $b_0+\cdots+b_{n-1}\alpha^{n-1}$，即 $\{1,\alpha,\dots,\alpha^{n-1}\}$ 是基底。**關鍵一步**：$(\star)$ $\alpha^n = -\sum a_k\alpha^k$ 把高次方降下來。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 基底定理的證明（歸納 + 唯一性）；$\dim F(\alpha) = \deg(\alpha,F)$ | 第 43 集 |
| $\mathbb{Q}(\sqrt2,\sqrt3)$ 和 $\mathbb{Q}(\sqrt6)$ | 第 43–45 集 |
| 有限擴張 ⇒ 代數擴張；$[K:F] = [K:E][E:F]$ | 第 44–45 集 |
| 本原元素定理 | 第 45 集 |

---

## 附：本集一句話總結

> **$\alpha$ 是超越的，恰好是「求值映射 $f\mapsto f(\alpha)$ 是一對一」，這時 $F[\alpha]$ 就像多項式環（例如 $\mathbb{Q}[\pi]$）。$\alpha$ 是代數的話，因為 $F[x]$ 是 PID，以 $\alpha$ 為根的多項式恰好是某個 $p(x)$ 的倍數——這個 $p$ 不可約、次數最小、取首一就唯一，記作 $\mathrm{irr}(\alpha,F)$。單擴張 $F(\alpha)$ 的元素都能唯一寫成 $1,\alpha,\dots,\alpha^{n-1}$ 的組合，也就是說它們是基底。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-15 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.9 整理。*
