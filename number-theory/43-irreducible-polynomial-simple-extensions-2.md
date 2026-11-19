---
course: Number Theory（2021 秋，線上錄影）
episode: 43
lecture: 2021-11-15 第 2 部
date: 2021-11-15
video: https://youtu.be/Yj0aLQVsROk
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.9 Lecture 29（p. 169–170）：Theorem 4.9.26 證明、Corollary 4.9.27、Example 4.9.28
---

# 第 43 集 · 基底定理的證明、Q(2^{3/2}) = Q(√2)（Irreducible Polynomial and Simple Extensions, Part 2） [▶ 影片](https://youtu.be/Yj0aLQVsROk)

← 上一集：[42-irreducible-polynomial-simple-extensions-1](42-irreducible-polynomial-simple-extensions-1.md) ｜ [總目錄](README.md) ｜ 下一集：[44-algebraic-extensions-degree-1](44-algebraic-extensions-degree-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 43 集（2021-11-15 第 2 部，接第 42 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（23:44，whisper 轉錄）＋ 講者講義 §4.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 生成：歸納法（「小精靈開心」）](#1-生成歸納法小精靈開心)
- [2. 唯一：移到同一邊](#2-唯一移到同一邊)
- [3. 推論：dim F(α) = deg(α, F)](#3-推論dim-fα--degα-f)
- [4. 例子：Q(⁵√2) 的基底](#4-例子q2-的基底)
- [5. Q(√2, √3) ≠ Q(√6)](#5-q2-3--q6)
- [6. Q(2^{3/2}) = Q(√2)](#6-q232--q2)
- [7. 方括號和圓括號](#7-方括號和圓括號)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

收尾第 42 集的 Theorem 4.9.26：單擴張 $F(\alpha)$（$\deg(\alpha,F) = n$）的每個元素都能**唯一地**寫成 $b_0+b_1\alpha+\cdots+b_{n-1}\alpha^{n-1}$。然後回頭處理上次留下的兩個例子。

回顧第 42 集的 $(\star)$：$\mathrm{irr}(\alpha,F) = x^n+a_{n-1}x^{n-1}+\cdots+a_0$，所以
$$\alpha^n = -\sum_{k=0}^{n-1}a_k\alpha^k.\qquad(\star)$$
「**小精靈**」（Pac-Man）= $\mathrm{span}_F\{1,\alpha,\dots,\alpha^{n-1}\}$，也就是 $1,\alpha,\dots,\alpha^{n-1}$ 的 $F$ 係數線性組合。

---

## 1. 生成：歸納法（「小精靈開心」）

[▶ 00:00](https://youtu.be/Yj0aLQVsROk?t=0)

講者先照黑板上的方式（對 $\beta$ 的最高次 $m$ 歸納，設 $b_m\neq0$）做基本情況 $m = n$：
$$\beta = b_0+\cdots+b_{n-1}\alpha^{n-1}+b_n\alpha^n = \sum_{k=0}^{n-1}(b_k-b_na_k)\alpha^k$$
（用 $(\star)$；講者「掉了一個負號——在這，找回來了」）。「小精靈開心。」

然後 [▶ 02:42](https://youtu.be/Yj0aLQVsROk?t=162) 他說講義走的路比較好：改成對 $m$ 歸納證明
$$\textbf{主張：}\ \alpha^m\in\mathrm{span}_F\{1,\alpha,\dots,\alpha^{n-1}\}\quad(m\ge n).$$
「我好像在那個方向有心理障礙，我們換個方向走。」（$n$ 固定，是 $\alpha$ 的次數；$m$ 是變數。）

**基本情況** $m = n$：就是 $(\star)$。

**歸納步驟** [▶ 06:13](https://youtu.be/Yj0aLQVsROk?t=373)：設 $\alpha^m = \sum_{k=0}^{n-1}c_k\alpha^k$。則
$$\alpha^{m+1} = \alpha\cdot\alpha^m = c_0\alpha+c_1\alpha^2+\cdots+c_{n-2}\alpha^{n-1}+c_{n-1}\alpha^n.$$
只有最後一項是「麻煩製造者」。用 $(\star)$ 換掉 $\alpha^n$，合併同類項 [▶ 09:13](https://youtu.be/Yj0aLQVsROk?t=553)：
$$\alpha^{m+1} = -c_{n-1}a_0+(c_0-c_{n-1}a_1)\alpha+\cdots+(c_{n-2}-c_{n-1}a_{n-1})\alpha^{n-1}.$$
在小精靈裡。∎（生成）

所以 $\beta = b_0+\cdots+b_m\alpha^m$ 的每個高次方都能換成小精靈裡的東西，$\beta$ 也在小精靈裡。

---

## 2. 唯一：移到同一邊

[▶ 11:05](https://youtu.be/Yj0aLQVsROk?t=665)

設
$$b_0+b_1\alpha+\cdots+b_{n-1}\alpha^{n-1} = \bar b_0+\bar b_1\alpha+\cdots+\bar b_{n-1}\alpha^{n-1}.$$

【課堂討論】講者問怎麼辦？移到同一邊：
$$g(x) = (b_0-\bar b_0)+(b_1-\bar b_1)x+\cdots+(b_{n-1}-\bar b_{n-1})x^{n-1}.$$

- $g(\alpha) = 0$。
- $\deg g\le n-1$，但 $p = \mathrm{irr}(\alpha,F)$ 是以 $\alpha$ 為根的**次數最小**的多項式，次數是 $n$ [▶ 12:44](https://youtu.be/Yj0aLQVsROk?t=764)。
- 所以 $g$ 必須是**零多項式**：所有係數都是 0，$b_k = \bar b_k$。∎（唯一）

講者 [▶ 13:14](https://youtu.be/Yj0aLQVsROk?t=794)：「**這是講義剩下所有東西的基礎**——我們可以只用添加元素的次方，替擴張體造出基底。」

---

## 3. 推論：dim F(α) = deg(α, F)

> 【講義補充】
>
> **Corollary 4.9.27**（p. 170）：$E = F(\alpha)$，$\alpha$ 在 $F$ 上代數，$\deg(\alpha,F) = n\ge1$。則 $\{1,\alpha,\dots,\alpha^{n-1}\}$ 是 $F(\alpha)$ 作為 $F$ 上向量空間的基底，
> $$\dim_F F(\alpha) = \deg(\alpha,F).$$
> （講義：線性獨立等價於「可以比較係數」，所以直接從上面的證明得到。）
>
> **Example 4.9.28**：$\mathbb{C} = \mathbb{R}(i)$，$\mathrm{irr}(i,\mathbb{R}) = x^2+1$，$\mathbb{C}$ 是 $\mathbb{R}$ 上 2 維向量空間，基底 $\{1,i\}$。

---

## 4. 例子：Q(⁵√2) 的基底

[▶ 13:56](https://youtu.be/Yj0aLQVsROk?t=836)（「把我們的例子的基底寫下來，然後我就不再超時了。時光飛逝，玩得開心嘛。」）

$\alpha = \sqrt[5]2$，$\deg(\alpha,\mathbb{Q}) = 5$（第 42 集，Eisenstein）。所以 $\mathbb{Q}(\sqrt[5]2)$ 是單擴張，
$$\mathbb{Q}(\sqrt[5]2) = \mathrm{span}_{\mathbb{Q}}\{1,\alpha,\alpha^2,\alpha^3,\alpha^4\},$$
元素是
$$a_0+a_1\sqrt[5]2+a_2\left(\sqrt[5]2\right)^2+a_3\left(\sqrt[5]2\right)^3+a_4\left(\sqrt[5]2\right)^4,\qquad a_i\in\mathbb{Q}.$$

---

## 5. Q(√2, √3) ≠ Q(√6)

[▶ 15:29](https://youtu.be/Yj0aLQVsROk?t=929)

回到第 42 集的問題「$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt6)$？」，講者：「**這是錯的。**」

【課堂討論】講者問：那該放什麼？學生：「為了得到 $\sqrt6$？」講者：不是——能不能找到**單一個**元素，用它做單擴張就得到全部？「這是我們下次希望弄清楚的事之一。」

> 以下**不是逐字稿內容**，是補一個答案（第 42 集筆記也有）：$\gamma = \sqrt2+\sqrt3$ 就行。$\gamma^3 = 11\sqrt2+9\sqrt3$，所以 $\sqrt2 = \frac{\gamma^3-9\gamma}2$、$\sqrt3 = \frac{11\gamma-\gamma^3}2$ 都在 $\mathbb{Q}(\gamma)$ 裡，$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3)$。

---

## 6. Q(2^{3/2}) = Q(√2)

[▶ 16:31](https://youtu.be/Yj0aLQVsROk?t=991)

上次的 $2^{3/2}$：$2^{3/2} = 2^{2/2}\cdot2^{1/2} = 2\sqrt2$。所以 $\mathbb{Q}(2^{3/2}) = \mathbb{Q}(2\sqrt2)$，講者說「不難證明」它就是 $\mathbb{Q}(\sqrt2)$。

**$x^2-8$ 不可約** [▶ 17:38](https://youtu.be/Yj0aLQVsROk?t=1058)：講者：「不是用 Eisenstein（$4\mid 8$）。也許模 3？」

- 模 3：$\bar f(x) = x^2-8\equiv x^2+1$（「加 9」）。
- $\bar f(0) = 1$、$\bar f(1) = 2$、$\bar f(2) = 5\equiv2$。二次、**沒有根** ⇒ 在 $\mathbb{Z}_3$ 上不可約。
- 次數沒降，所以由**模 $p$ 判別法**（第 36 集），$x^2-8$ 在 $\mathbb{Q}$ 上不可約。

講者 [▶ 18:55](https://youtu.be/Yj0aLQVsROk?t=1135)：「判別不可約我們有兩個主要工具：**Eisenstein 和這個把戲**。次數高於 3 時比較麻煩。」

所以 $\mathrm{irr}(2^{3/2},\mathbb{Q}) = x^2-8$，**2 次擴張**，基底 $\{1,\alpha\}$。

**兩邊互相包含** [▶ 19:25](https://youtu.be/Yj0aLQVsROk?t=1165)：

- $a+b\cdot2^{3/2} = a+2b\sqrt2\in\mathbb{Q}(\sqrt2)$，所以 $\mathbb{Q}(2^{3/2})\subseteq\mathbb{Q}(\sqrt2)$。
- $a+b\sqrt2 = a+\frac b2\cdot2\sqrt2 = a+\frac b2\cdot2^{3/2}\in\mathbb{Q}(2^{3/2})$，所以 $\mathbb{Q}(\sqrt2)\subseteq\mathbb{Q}(2^{3/2})$。
- 所以**相等**。

**一般的定理** [▶ 21:14](https://youtu.be/Yj0aLQVsROk?t=1274)：
$$F(\alpha) = F(c\alpha),\qquad c\in F,\ c\neq0.$$
關鍵是 2 在 $\mathbb{Q}$ 裡，所以能除以它。講者：「這會是很好的作業題，但作業都寫好了，你們安全了。最壞可能放期末考，但我大概會忘，那是感恩節後的事。」

> 以下**不是逐字稿內容**，是補這個定理的一行證明：$c\alpha\in F(\alpha)$，所以 $F(c\alpha)\subseteq F(\alpha)$；$\alpha = c^{-1}(c\alpha)\in F(c\alpha)$，所以 $F(\alpha)\subseteq F(c\alpha)$。（用「最小的體」的定義。）

---

## 7. 方括號和圓括號

[▶ 21:45](https://youtu.be/Yj0aLQVsROk?t=1305)

【Q&A】學生問：之前說方括號和圓括號記號不同，現在用哪個？講者：

- **方括號 = 環**：例如 $\mathbb{Q}[\pi]$，包含 $\mathbb{Q}$ 和 $\pi$ 的最小的**環**，「那是有意的，因為它不是體」。
- **圓括號 = 體**：體的擴張。
- 「有時候兩者相等」（像 $\mathbb{Q}[\sqrt2] = \mathbb{Q}(\sqrt2)$，第 40 集）。

**課程安排** [▶ 22:49](https://youtu.be/Yj0aLQVsROk?t=1369)：下次把這些收尾，剩下的是「Conrad 的一段」（第 46–47 集），然後是第 3 次考試和期末考。學生說很高興考試在感恩節後，因為其他課都擠在這週考。

---

## 8. 一頁速查表

**基底定理**：$\deg(\alpha,F) = n$ ⇒ $\{1,\alpha,\dots,\alpha^{n-1}\}$ 是 $F(\alpha)$ 在 $F$ 上的基底，$\dim_FF(\alpha) = \deg(\alpha,F)$。

| 部分 | 關鍵一步 |
|---|---|
| 生成 | 歸納：$\alpha^{m+1} = \alpha\cdot\sum c_k\alpha^k$，最後一項 $c_{n-1}\alpha^n$ 用 $\alpha^n = -\sum a_k\alpha^k$ 換掉 |
| 唯一 | 兩組係數相減得 $g$，$g(\alpha) = 0$、$\deg g<n$ ⇒ $g = 0$ |

**例子**

| 體 | 基底 | 維度 |
|---|---|---|
| $\mathbb{R}(i) = \mathbb{C}$ | $1,i$ | 2 |
| $\mathbb{Q}(\sqrt[5]2)$ | $1,\sqrt[5]2,\dots,(\sqrt[5]2)^4$ | 5 |
| $\mathbb{Q}(2^{3/2}) = \mathbb{Q}(\sqrt2)$ | $1,2^{3/2}$（或 $1,\sqrt2$） | 2 |

**$F(c\alpha) = F(\alpha)$**（$0\neq c\in F$）。

**判別不可約兩大工具**：Eisenstein；模 $p$（$x^2-8$ 模 3 是 $x^2+1$，沒有根）。

**記號**：$F[\alpha]$ 是環，$F(\alpha)$ 是體；$\alpha$ 代數時相等，$\alpha$ 超越時不相等（$\mathbb{Q}[\pi]\neq\mathbb{Q}(\pi)$）。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $[E:F]$ = 維度；有限擴張 ⇒ 代數擴張 | 第 44 集 |
| 塔定理 $[K:F] = [K:E][E:F]$；$\deg(\beta,F)\mid\deg(\alpha,F)$ | 第 44–45 集 |
| 找單一個元素生成 $\mathbb{Q}(\sqrt2,\sqrt3)$（本原元素） | 第 45 集 |
| Conrad 的講義：理想修正唯一分解 | 第 46–47 集 |

---

## 附：本集一句話總結

> **單擴張 $F(\alpha)$ 的每個元素都能唯一寫成 $1,\alpha,\dots,\alpha^{n-1}$ 的組合：用 $\mathrm{irr}(\alpha,F)$ 把 $\alpha^n$ 換成低次方就能歸納出「生成」，兩種寫法相減得到次數太低的根就推出「唯一」。所以 $F(\alpha)$ 的維度就是 $\alpha$ 的次數；例如 $2^{3/2} = 2\sqrt2$ 的不可約多項式是 $x^2-8$（模 3 判別），而且 $\mathbb{Q}(2^{3/2}) = \mathbb{Q}(\sqrt2)$。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-15 第 2 部錄影逐字稿（whisper 轉錄，23:44）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.9 整理。*
