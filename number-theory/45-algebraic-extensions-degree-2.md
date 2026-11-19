---
course: Number Theory（2021 秋，線上錄影）
episode: 45
lecture: 2021-11-17 第 2 部
date: 2021-11-17
video: https://youtu.be/y7Pv0GBJor0
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.10 Lecture 30（p. 172）：Example 4.10.7–4.10.8、Theorem 4.10.9、Theorem 4.10.10（本原元素定理）
---

# 第 45 集 · Q(√2, ∛2) = Q(⁶√2)、本原元素定理（Algebraic Extensions and Degree, Part 2） [▶ 影片](https://youtu.be/y7Pv0GBJor0)

← 上一集：[44-algebraic-extensions-degree-1](44-algebraic-extensions-degree-1.md) ｜ [總目錄](README.md) ｜ 下一集：[46-ideals-fix-numbers-1](46-ideals-fix-numbers-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 45 集（2021-11-17 第 2 部，接第 44 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（20:08，whisper 轉錄）＋ 講者講義 §4.10
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. x³ − 2 在 Q(√2) 上不可約（收尾）](#1-x--2-在-q2-上不可約收尾)
- [2. Q(√2)(∛2)：6 維，其實是 Q(⁶√2)](#2-q2∛26-維其實是-q2)
- [3. 有限擴張 ⇔ 有限生成的代數擴張](#3-有限擴張--有限生成的代數擴張)
- [4. 本原元素定理（Steinitz）](#4-本原元素定理steinitz)
- [5. Q(√2, √3) = Q(√2 + √3)](#5-q2-3--q2--3)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

收尾第 44 集的例子，再看兩個「多個元素的擴張其實是單擴張」的例子，最後是**本原元素定理**。這是講者講義的最後一部分；感恩節後換 Conrad 的講義（第 46–47 集）。

---

## 1. x³ − 2 在 Q(√2) 上不可約（收尾）

[▶ 00:00](https://youtu.be/y7Pv0GBJor0?t=0)

接第 44 集：假設 $\beta\in\mathbb{Q}(\sqrt2)$ 是 $x^3-2$ 的根。塔 $\mathbb{Q}\subseteq\mathbb{Q}(\beta)\subseteq\mathbb{Q}(\sqrt2)$：
$$\underbrace{[\mathbb{Q}(\sqrt2):\mathbb{Q}]}_{2} = \underbrace{[\mathbb{Q}(\sqrt2):\mathbb{Q}(\beta)]}_{n\ge1}\cdot\underbrace{[\mathbb{Q}(\beta):\mathbb{Q}]}_{3}.$$

【課堂討論】講者：「你們告訴我這裡怎麼了？」$2 = 3n$ 不可能（$3\nmid2$）。所以那個「**假設**」是錯的：

**結論** [▶ 01:01](https://youtu.be/y7Pv0GBJor0?t=61)：$x^3-2$ 在 $\mathbb{Q}(\sqrt2)$ 裡**沒有根**。

它是三次式、沒有根，由第 36 集的定理（2、3 次：可約 ⇔ 有根），**$x^3-2$ 在 $\mathbb{Q}(\sqrt2)$ 上不可約**。

講者 [▶ 01:32](https://youtu.be/y7Pv0GBJor0?t=92)：我們判別不可約的工具（Eisenstein、模 $p$）大多是**在 $\mathbb{Q}$ 上**，這裡證的是**在擴張體上**不可約。「這是個狡猾的新把戲，這門課不會多探討；但如果你去學 **Galois 理論**，這是一再使用的基本計算。」

---

## 2. Q(√2)(∛2)：6 維，其實是 Q(⁶√2)

[▶ 02:55](https://youtu.be/y7Pv0GBJor0?t=175)（講義 Example 4.10.8，課堂叫例 5）

考慮 $\mathbb{Q}(\sqrt2)$ 再添加 $\sqrt[3]2$。

**$\sqrt[3]2$ 在 $\mathbb{Q}(\sqrt2)$ 上的次數**：由第 1 節，
$$\mathrm{irr}\left(\sqrt[3]2,\ \mathbb{Q}(\sqrt2)\right) = x^3-2.$$
（順帶：$\mathrm{irr}(\sqrt[3]2,\mathbb{Q})$ 也是 $x^3-2$，「但前一句對接下來比較重要」。）

所以令 $\alpha = \sqrt[3]2$（「先叫它 $\alpha$，去神祕化一下」），元素是
$$a+b\alpha+c\alpha^2,\qquad a,b,c\in\mathbb{Q}(\sqrt2).$$

**全部展開** [▶ 04:52](https://youtu.be/y7Pv0GBJor0?t=292)：$a = a_1+a_2\sqrt2$、$b = b_1+b_2\sqrt2$、$c = c_1+c_2\sqrt2$（$a_i,b_i,c_i\in\mathbb{Q}$）：
$$a_1+a_2\,2^{1/2}+b_1\,2^{1/3}+b_2\,2^{5/6}+c_1\,2^{2/3}+c_2\,2^{7/6}.$$
（$\frac12+\frac13 = \frac56$；講者一開始忘了 $\alpha^2$ 的平方，「我漏了平方」，改成 $\frac23+\frac12 = \frac76$。）

所以這是 $\mathbb{Q}$ 上的 **6 維**擴張，基底
$$1,\ 2^{1/2},\ 2^{1/3},\ 2^{5/6},\ 2^{2/3},\ 2^{7/6}.$$
（塔定理：$[\mathbb{Q}(\sqrt2)(\sqrt[3]2):\mathbb{Q}] = 3\cdot2 = 6$。）

**「垂手可得的果實，我為什麼摘不到？」** [▶ 07:27](https://youtu.be/y7Pv0GBJor0?t=447) 全部換成六分之幾：$\frac12 = \frac36$、$\frac13 = \frac26$、$\frac23 = \frac46$、$\frac76 = 1+\frac16$（$2^{7/6} = 2\cdot2^{1/6}$）。所以全都是 $2^{1/6}$ 的次方：
$$\mathbb{Q}(\sqrt2)(\sqrt[3]2) = \mathbb{Q}(\sqrt[6]2).$$

- $x^6-2$ 由 Eisenstein（$p = 2$）在 $\mathbb{Q}$ 上不可約，所以 $[\mathbb{Q}(\sqrt[6]2):\mathbb{Q}] = 6$，跟上面一致。
- 記號：$\mathbb{Q}(\sqrt2,\sqrt[3]2)$ = 含 $\mathbb{Q}$、$\sqrt2$、$\sqrt[3]2$ 的最小體 = $\mathbb{Q}(\sqrt2)(\sqrt[3]2)$（「很容易證」）。

講者 [▶ 09:01](https://youtu.be/y7Pv0GBJor0?t=541)：所以它其實是 $\mathbb{Q}$ 上的**單擴張**。「一開始看不出來它是單一元素的擴張。算完才發現：啊哈，添加 $\sqrt[6]2$ 一個元素就自動得到全部。」

> 以下**不是逐字稿內容**，是補「為什麼 $\sqrt2,\sqrt[3]2\in\mathbb{Q}(\sqrt[6]2)$」：$\sqrt2 = (\sqrt[6]2)^3$、$\sqrt[3]2 = (\sqrt[6]2)^2$；反過來 $\sqrt[6]2 = 2^{1/6} = 2^{1/2}\cdot2^{-1/3} = \dfrac{\sqrt2}{\sqrt[3]2}$。所以兩邊互相包含。

---

## 3. 有限擴張 ⇔ 有限生成的代數擴張

[▶ 09:42](https://youtu.be/y7Pv0GBJor0?t=582)

> **定理**（講義 Theorem 4.10.9）：$E$ 是 $F$ 的代數擴張。則存在有限多個 $\alpha_1,\dots,\alpha_n\in E$ 使 $E = F(\alpha_1,\dots,\alpha_n)$ ⇔ $E$ 是 $F$ 的有限擴張。

講者：「我沒有證明，可以看 **Fraleigh** 的書 p. 286，我辦公室某處有一本，有興趣可以借。」

---

## 4. 本原元素定理（Steinitz）

[▶ 11:19](https://youtu.be/y7Pv0GBJor0?t=679)

> **本原元素定理**（講義 Theorem 4.10.10，Steinitz 1910）：$F$ 是**特徵 0** 的體，$a,b$ 在 $F$ 上代數，則存在 $c\in F(a,b)$ 使
> $$F(a,b) = F(c).$$

也就是：特徵 0 時，兩個元素的擴張原則上都能改寫成一個元素的擴張——**單擴張**。$c$ 叫**本原元素**（primitive element）。

> 【講義補充】講義（p. 172）：證明見 Gallian p. 367。特徵 $p$ 時沒有這麼簡單，只有上面較複雜的 Theorem 4.10.9。

---

## 5. Q(√2, √3) = Q(√2 + √3)

[▶ 12:20](https://youtu.be/y7Pv0GBJor0?t=740)（課堂例 6，上次的問題）

Steinitz 說 $\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\text{某個東西})$。「如果我們找出那個東西，就能下課了。你們猜是什麼？」

【課堂討論】學生：上次問過，做不出來。講者：「做不出來是因為我把它們**相乘**（$\sqrt6$）。那不是正確的路。**改成相加。**」

令 $\gamma = \sqrt2+\sqrt3\in\mathbb{Q}(\sqrt2,\sqrt3)$。

**倒數** [▶ 13:26](https://youtu.be/y7Pv0GBJor0?t=806)：分母有理化，
$$\frac1\gamma = \frac1{\sqrt3+\sqrt2}\cdot\frac{\sqrt3-\sqrt2}{\sqrt3-\sqrt2} = \frac{\sqrt3-\sqrt2}{3-2} = \sqrt3-\sqrt2.$$

**加減** [▶ 14:34](https://youtu.be/y7Pv0GBJor0?t=874)：
$$\gamma+\frac1\gamma = 2\sqrt3,\qquad\gamma-\frac1\gamma = 2\sqrt2.$$
所以
$$\sqrt3 = \frac12\left(\gamma+\frac1\gamma\right),\qquad\sqrt2 = \frac12\left(\gamma-\frac1\gamma\right).$$

**$\mathbb{Q}(\sqrt2,\sqrt3)\subseteq\mathbb{Q}(\gamma)$** [▶ 15:34](https://youtu.be/y7Pv0GBJor0?t=934)：體裡有 $\frac1\gamma$，加起來還在體裡，$\frac12\in\mathbb{Q}$ 也可以乘。所以 $\sqrt2,\sqrt3\in\mathbb{Q}(\gamma)$，用它們造的東西都在 $\mathbb{Q}(\gamma)$ 裡。

**$\mathbb{Q}(\gamma)\subseteq\mathbb{Q}(\sqrt2,\sqrt3)$** [▶ 17:25](https://youtu.be/y7Pv0GBJor0?t=1045)：「很明顯」——$\gamma\in\mathbb{Q}(\sqrt2,\sqrt3)$。（講者說完整論證要講 $\gamma$ 次方的 $\mathbb{Q}$ 組合，「我把它講得比需要的複雜」。）

所以
$$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3).$$
「添加 $\sqrt2$ 與 $\sqrt3$ 的和，用體運算就能拿回 $\sqrt3$ 和 $\sqrt2$。」

**這是 $\sqrt2,\sqrt3$ 特有的嗎？** [▶ 18:33](https://youtu.be/y7Pv0GBJor0?t=1113) 講者：「我不這麼想。我想特徵 0 的體上 $F(\alpha,\beta)$ 很可能就是 $F(\alpha+\beta)$……我沒把握。我想可以模仿這些計算，但我很久沒讀那個證明了，Gallian 裡有。」「我們上次很接近了，只是該加不該乘。」

> 以下**不是逐字稿內容**，是補講者沒把握的那句：$F(\alpha,\beta) = F(\alpha+\beta)$ **不是永遠成立**，例如 $\beta = -\alpha$ 時 $\alpha+\beta = 0$，$F(0) = F$。本原元素定理的標準證明（Gallian p. 367 的方向）是：除了有限多個例外的 $t\in F$，$c = \alpha+t\beta$ 都是本原元素；特徵 0 的體有無限多個元素，所以一定找得到。$\sqrt2+\sqrt3$ 就是 $t = 1$ 剛好可以的情形。

【口頭】[▶ 19:38](https://youtu.be/y7Pv0GBJor0?t=1178)「我又超時了，照例。抱歉。」關於 **mission 5** 的質理想和極大理想那題：**在有限的情況，質理想和極大理想是一樣的**，所有極大理想就是所有質理想。「感恩節後見。」

> 以下**不是逐字稿內容**，是補一句理由：有單位元的有限交換環 $R$ 裡，$P$ 是質理想 ⇒ $R/P$ 是**有限整環** ⇒ 是體（第 28 集：有限整環是體）⇒ $P$ 是極大理想。

---

## 6. 一頁速查表

**在擴張體上判別不可約**：$x^3-2$ 在 $\mathbb{Q}(\sqrt2)$ 裡有根 ⇒ $2 = n\cdot3$，矛盾 ⇒ 沒有根 ⇒（三次）不可約。

**$\mathbb{Q}(\sqrt2,\sqrt[3]2) = \mathbb{Q}(\sqrt[6]2)$**：次數 $3\cdot2 = 6$，基底 $2^{k/6}$（$k = 0,\dots,5$）。**關鍵一步**：指數 $\frac12,\frac13,\frac56,\frac23,\frac76$ 都是 $\frac16$ 的倍數。

**有限擴張 ⇔ 有限生成的代數擴張**（Fraleigh p. 286）。

**本原元素定理**（Steinitz 1910）：特徵 0，$F(a,b) = F(c)$。

**$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3)$**。**關鍵一步**：$\frac1\gamma = \sqrt3-\sqrt2$，$\sqrt3 = \frac12(\gamma+\frac1\gamma)$、$\sqrt2 = \frac12(\gamma-\frac1\gamma)$。（$\mathbb{Q}(\sqrt6)$ 只有 2 維，不夠。）

**有限交換環**：質理想 = 極大理想。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 唯一分解失敗 ⇒ 改用理想（Conrad） | 第 46–47 集 |
| 分裂體、Galois 理論、尺規作圖 | 本課沒講 |

---

## 附：本集一句話總結

> **用塔定理可以在擴張體上證不可約：$x^3-2$ 的根是 3 次的，塞不進 2 次的 $\mathbb{Q}(\sqrt2)$。看起來要加好幾個元素的擴張常常只要一個：$\mathbb{Q}(\sqrt2,\sqrt[3]2) = \mathbb{Q}(\sqrt[6]2)$，$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3)$（要相加、不是相乘）；Steinitz 的本原元素定理說特徵 0 時這永遠做得到。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-17 第 2 部錄影逐字稿（whisper 轉錄，20:08）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.10 整理。*
