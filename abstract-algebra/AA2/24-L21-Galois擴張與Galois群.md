---
course: Abstract Algebra II (Spring 2026)
episode: 24
lecture: L21
date: 2026-03-11
video: https://www.youtube.com/watch?v=wtedDsycOZ8
notes: 講義/AA2/Math422_Lecture21_GaloisBeginnings.pdf
---

# 第 24 集 · L21：Galois 擴張與 Galois 群的基本定義 [▶ 影片](https://www.youtube.com/watch?v=wtedDsycOZ8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[23-L20-分圓體與Galois理論開始]] ｜ [總目錄](../README.md) ｜ 下一集：[[25-L22-Galois理論基本定理]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 24 集，Lecture 21
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:26，自動字幕）＋ 手寫講義 `Math422_Lecture21_GaloisBeginnings.pdf`（7 頁），依 Dummit & Foote §14.1。黑板為主。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. Galois 理論在做什麼](#0-galois-理論在做什麼)
- [1. 自同構；固定 F 的自同構群 Aut(K/F)](#1-自同構固定-f-的自同構群-autkf)
- [2. 自同構把根送到根（Prop 2）](#2-自同構把根送到根prop-2)
- [3. 例：ℚ(√2) 與 ℚ(∛2)](#3-例ℚ2-與-ℚ2)
- [4. 固定體 Kᴴ](#4-固定體-kᴴ)
- [5. 包含關係反轉（Prop 4）](#5-包含關係反轉prop-4)
- [6. |Aut(E/F)| ≤ [E:F]；Galois 擴張的定義](#6-autef--efgalois-擴張的定義)
- [7. 例：ℚ(√2, √3) 的 Galois 群是 Klein 四元群](#7-例ℚ2-3-的-galois-群是-klein-四元群)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. Galois 理論在做什麼

[▶ 00:00](https://youtu.be/wtedDsycOZ8?t=0) 課前禱告：「幫助我們看見**你的** Galois 理論。」

【講義補充】講義 p.1：Évariste Galois（1811–1832）開創的理論，研究 $f(x) = 0$ 的解如何在某個擴張 $K/F$ 中得到——「簡單說，**秘密鎖在分裂體的代數結構裡**。要好幾堂課才能拆開細節。」

---

## 1. 自同構；固定 F 的自同構群 Aut(K/F)

> **定義**（講義 p.1–2）[▶ 00:30](https://youtu.be/wtedDsycOZ8?t=30)
> 1. 體 $K$ 到自己的同構叫**自同構**，記 $\sigma\in\mathrm{Aut}(K)$；寫 $\sigma\alpha$ 代替 $\sigma(\alpha)$。
> 2. $\sigma\alpha = \alpha$ 時說 $\sigma$ **固定** $\alpha$；$\sigma$ 固定 $F$ 的所有元素時說 $\sigma$ **固定 $F$**。
> 3. $\mathrm{Aut}(K/F)$：$K$ 中**固定 $F$** 的自同構全體——「$K$ 的 **$F$-固定自同構**」。

【講義補充】講義 p.1：任何自同構都固定 1，而 1 生成質子體 ⇒ **自同構固定質子體**。所以 $\mathrm{Aut}(\mathbb{Q}) = \{1\}$、$\mathrm{Aut}(\mathbb{F}_p) = \{1\}$。

> **命題 1**（講義 p.2）[▶ 02:30](https://youtu.be/wtedDsycOZ8?t=150)　$\mathrm{Aut}(K)$ 對合成是群，$\mathrm{Aut}(K/F)$ 是它的子群。

- $\mathrm{Aut}(K)$：同構的合成、反函數還是同構；含恆等 ⇒ 是 $K$ 上所有雙射的子群。
- **$\mathrm{Aut}(K/F)$**[▶ 03:30](https://youtu.be/wtedDsycOZ8?t=210)：$\sigma,\tau$ 固定 $F$，$x\in F$：
$$\sigma\tau x = \sigma x = x;\qquad x = \sigma^{-1}\sigma x = \sigma^{-1}x.$$
  所以對乘法、反元素封閉；含恆等 $1$（$1x = x$）⇒ 非空 ⇒ 子群。
- 【Q&A】學生：「要證非空嗎？」「要，**我會講到**。」
- 「你們開心嗎？你們開心我就開心。——**那不是真的**。那**絕對是謊話**。」學生：「反過來倒是真的。」「我相信的是一種……**對抗式教學法**。」

---

## 2. 自同構把根送到根（Prop 2）

> **命題 2**（講義 p.2）[▶ 06:30](https://youtu.be/wtedDsycOZ8?t=390)　$K/F$，$\alpha\in K$ 在 $F$ 上代數。則對任何 $\sigma\in\mathrm{Aut}(K/F)$，$\sigma\alpha$ 是 $\alpha$ 在 $F$ 上**最小多項式的根**。也就是說：**$\mathrm{Aut}(K/F)$ 置換不可約多項式的根**。等價地：$F$ 上任何以 $\alpha$ 為根的多項式也以 $\sigma\alpha$ 為根。

【口頭】[▶ 08:00](https://youtu.be/wtedDsycOZ8?t=480)「我覺得 **Galois 理論真正從這個命題開始**。」

**證明**：$\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_1\alpha+a_0 = 0$，$a_j\in F$。$\sigma$ 固定 $F$ ⇒ $\sigma a_j = a_j$。
- 「**自己算算看**，別只抄我寫的。對方程式取 $\sigma$。」
- 【課堂討論】[▶ 10:30](https://youtu.be/wtedDsycOZ8?t=630)「環自同構把 0 送到哪？」「0。」
- 加法性、乘法性：$\sigma(a_j\alpha^j) = \sigma(a_j)\sigma(\alpha)^j = a_j(\sigma\alpha)^j$ ⇒
$$(\sigma\alpha)^n+a_{n-1}(\sigma\alpha)^{n-1}+\cdots+a_1\sigma\alpha+a_0 = 0.$$
- 所以 $f(\alpha) = 0$ ⇒ $f(\sigma\alpha) = 0$。$\blacksquare$

【講義補充】講義 p.3：$K = F(\alpha)$ 或 $F(\alpha,\beta)$ 時，$\mathrm{Aut}(K/F)$ 的結構本質上由**生成元怎麼送到其他生成元**決定——那些會是某個共同多項式的根。每個 $\sigma$ 都固定 $F$，所以 $\sigma$ 的特別之處都落在 $F$ 以外的元素上。

（[▶ 13:00](https://youtu.be/wtedDsycOZ8?t=780) 學生在畫塗鴉：「那是**很好的藝術**。」「比你的 capstone 好？」「好多了。」「我女兒今天也在我手臂上畫。你們跟我女兒**很像**。」）

---

## 3. 例：ℚ(√2) 與 ℚ(∛2)

**例 1**（講義 p.4）[▶ 13:30](https://youtu.be/wtedDsycOZ8?t=810)：$K = \mathbb{Q}(\sqrt2)$。
- 【口頭】「如果 $K$ 擴張它的質子體 $\mathbb{Q}$，**任何**自同構都自動固定 $\mathbb{Q}$（把 1 送到 1，推下去就是）⇒ $\mathrm{Aut}(K/\mathbb{Q}) = \mathrm{Aut}(K)$。」
- 自同構**完全由 $\sqrt2$ 的命運決定**：$\pm\sqrt2$ 是 $x^2-2$ 的根，$\sqrt2$ 只能送到 $\sqrt2$ 或 $-\sqrt2$：
$$1(a+b\sqrt2) = a+b\sqrt2,\qquad\sigma(a+b\sqrt2) = a-b\sqrt2.$$
- 「有點像複數共軛，但不是。」$\sigma\sigma = 1$ ⇒ $\mathrm{Aut}(\mathbb{Q}(\sqrt2)) = \{1,\sigma\}\cong\mathbb{Z}_2$。

**例 2**（講義 p.4）[▶ 17:30](https://youtu.be/wtedDsycOZ8?t=1050)：$K = \mathbb{Q}(\sqrt[3]2)$，3 次（$x^3-2$ Eisenstein 不可約），元素 $a+b\sqrt[3]2+c(\sqrt[3]2)^2$。
- $\tau$ 必須把 $\sqrt[3]2$ 送到 $x^3-2$ 的根：$\sqrt[3]2$、$\zeta_3\sqrt[3]2$、$\zeta_3^2\sqrt[3]2$。「後兩個**就像那匹馬一樣不是真的**。」（3 年前新聞：飛機上有位女士大喊「那匹馬不是真的！」被趕下飛機。學生：「是 Violet 的媽媽嗎？」「這是**很到位的呼應**，打得好。」）
- 後兩個不是實數，而 $\mathbb{Q}(\sqrt[3]2)\subset\mathbb{R}$ ⇒ 它們**不在 $K$ 裡** ⇒ $\tau\sqrt[3]2 = \sqrt[3]2$ ⇒ $\tau = 1$。
$$\mathrm{Aut}(\mathbb{Q}(\sqrt[3]2)) = \{1\}.$$

---

## 4. 固定體 Kᴴ

[▶ 21:30](https://youtu.be/wtedDsycOZ8?t=1290)（講義 p.5）$K/F$ 有限 ⇒ $\mathrm{Aut}(K/F)$ 是有限群。「每個擴張 $K/F$ 可以配一個群 $\mathrm{Aut}(K/F)$。**反方向**也行：每個自同構子群可以配一個子體——**固定子體**。」
- 【口頭】[▶ 22:30](https://youtu.be/wtedDsycOZ8?t=1350)「我要用一個 D&F（至少現在）**沒有**的記號。我以前想過這材料，發現書的講法**缺了一個記號**，而那記號有助於**把想法掛上去**。」

> **命題 3**（講義 p.5）[▶ 23:00](https://youtu.be/wtedDsycOZ8?t=1380)　$H\le\mathrm{Aut}(K)$。則 $K$ 中被 $H$ **所有**元素固定的元素構成 $K$ 的子體
> $$K^H = \{x\in K : \sigma x = x\ \forall\sigma\in H\},$$
> 叫 $H$ 的**固定體**（fixed field）。

【Q&A】[▶ 24:30](https://youtu.be/wtedDsycOZ8?t=1470) 學生：「這感覺比較像**定義**。」老師：「宣稱的是那裡**有個體**，所以要證它是體。我是在命題裡做了定義——**被你抓到了**。」

**證明（填空）**[▶ 25:00](https://youtu.be/wtedDsycOZ8?t=1500)：$h\in H$，$a,b\in K^H$ ⇒ $h(a) = $＿、$h(b) = $＿ ⇒ $h(a\pm b) = $＿ ⇒ $a\pm b\in$＿；$h(ab) = h(a)h(b) = $＿、$h(a^{-1}) = h(a)^{-1} = $＿ ⇒ $ab,a^{-1}\in$＿。
- 【課堂討論】[▶ 27:30](https://youtu.be/wtedDsycOZ8?t=1650)「像填字遊戲（Mad Libs）。」「但**更簡單、更有趣**。」學生依序填：$a$、$b$、$a\pm b$、$K^H$、$ab$、$a^{-1}$、$K^H$。（學生填了一個形容詞：「**軟軟的**。」）
- 【課堂討論】[▶ 29:00](https://youtu.be/wtedDsycOZ8?t=1740)「我假設 $H$ 是**子群**——證明哪裡用到了？」「這是**陷阱題**：**沒用到**。對任意自同構子集都成立。」（講義 p.5 的 Remark：$S\subseteq\mathrm{Aut}(K)$ 任意子集，$K^S$ 也是子體。）

---

## 5. 包含關係反轉（Prop 4）

[▶ 29:30](https://youtu.be/wtedDsycOZ8?t=1770)「這有點**意外**，也是 Galois 理論有點難的部分原因。這樣運作有點**彆扭**，但事實就是如此。」

> **命題 4**（講義 p.6）　群 ↔ 體 的對應是**包含關係反轉**的：
> 1. $F_1\subseteq F_2\subseteq K$ ⇒ $\mathrm{Aut}(K/F_2)\le\mathrm{Aut}(K/F_1)$。
> 2. $H_1\le H_2\le\mathrm{Aut}(K)$ ⇒ $K^{H_2}\subseteq K^{H_1}$。

- 【課堂討論】[▶ 31:00](https://youtu.be/wtedDsycOZ8?t=1860) 老師填空時學生說「先 $F_2$ 再 $F_1$」：「你怎麼知道？」「因為一個包含另一個。」學生問用子集還是子群符號：「群用 $\le$（子群），體用 $\subseteq$。也可以都寫 $\subseteq$——**也對，但沒那麼有趣**。」（學生：「代數一兩個都用角括號。」「我是照 D&F 的記號。」）

**證明**[▶ 33:00](https://youtu.be/wtedDsycOZ8?t=1980)
1. $\sigma\in\mathrm{Aut}(K/F_2)$，$x\in F_1\subseteq F_2$ ⇒ $\sigma x = x$ ⇒ $\sigma\in\mathrm{Aut}(K/F_1)$。學生：「只要證包含——它們**已經是群**了。」「對，今天前面已經證過。」
2. [▶ 35:30](https://youtu.be/wtedDsycOZ8?t=2130) $a\in K^{H_2}$，$\tau\in H_1\subseteq H_2$ ⇒ $\tau a = a$ ⇒ $a\in K^{H_1}$。$\blacksquare$

（[▶ 37:30](https://youtu.be/wtedDsycOZ8?t=2250)「你們總坐在我**沒寫**的那邊。看 Daniel——他在看身後找**影子 Daniel**。」「我會很享受 **Sprano 博士教 Jacob 代數一**。」）

---

## 6. |Aut(E/F)| ≤ [E:F]；Galois 擴張的定義

> **命題 5**（講義 p.7）[▶ 38:30](https://youtu.be/wtedDsycOZ8?t=2310)　$E$ 是 $f(x)\in F[x]$ 在 $F$ 上的分裂體 ⇒
> $$|\mathrm{Aut}(E/F)|\le[E:F],$$
> **$f$ 可分時取等號**。

- 「證明也許下次，**不是今天**。在 D&F §14.1 p.561–562——**不是什麼嚴守的秘密**。」
- 「其實對**任何**有限擴張都能證 $|\mathrm{Aut}(K/F)|\le[K:F]$——分裂體的假設不必要，但分裂體**特別有趣**。」

> **定義**（講義 p.7）[▶ 40:30](https://youtu.be/wtedDsycOZ8?t=2430)　$K/F$ 有限。若 $|\mathrm{Aut}(K/F)| = [K:F]$，說 $K$ 在 $F$ 上是 **Galois** 的，$K/F$ 是 **Galois 擴張**；此時 $\mathrm{Aut}(K/F)$ 叫 **Galois 群**，記 $\mathrm{Gal}(K/F)$。

> **定義**[▶ 42:00](https://youtu.be/wtedDsycOZ8?t=2520)　$f(x)$ 在 $F$ 上可分，**$f$ 的 Galois 群**是它的分裂體的 Galois 群。

> **推論 6**（講義 p.7）[▶ 43:00](https://youtu.be/wtedDsycOZ8?t=2580)　$K$ 是 $F$ 上**可分**多項式 $f$ 的分裂體 ⇒ $K/F$ 是 Galois。

- 「這定義**只因為**推論 6 才合理。推論 6 粗略地說：**分裂體是 Galois 的**。要我正式講嗎？」學生：「要。」（學生的電池剩 **67%**——「我准了。」）

【課堂討論】[▶ 45:00](https://youtu.be/wtedDsycOZ8?t=2700)「例 1、例 2 哪個是 Galois？」
- **例 1** $\mathbb{Q}(\sqrt2)$：是可分多項式 $x^2-2$ 的分裂體 ⇒ Galois。也看得出 $[\mathbb{Q}(\sqrt2):\mathbb{Q}] = 2 = |\mathrm{Aut}|$——「自同構和維度**一樣多**」。
- **例 2** $\mathbb{Q}(\sqrt[3]2)$：$[\,:\mathbb{Q}] = 3\neq1 = |\mathrm{Aut}|$ ⇒ **不是** Galois。

---

## 7. 例：ℚ(√2, √3) 的 Galois 群是 Klein 四元群

[▶ 47:30](https://youtu.be/wtedDsycOZ8?t=2850)（「我已經到例 3 了？」「沒有，你今天**一直在證東西**。」）$K = \mathbb{Q}(\sqrt2,\sqrt3)$。
- 【課堂討論】「它是什麼的分裂體？」「$(x^2-2)(x^2-3)$。」$\pm\sqrt2,\pm\sqrt3$ 都在裡面——明顯。「次數花了點功夫——**4**。」⇒ 推論 6：Galois，「我看到**四個**自同構，來找它們。」
- 基底 $1,\sqrt2,\sqrt3,\sqrt6$（「$\sqrt2\sqrt3$ 寫成 $\sqrt6$ 比較不怪」）。任意元素
$$\tau(a+b\sqrt2+c\sqrt3+d\sqrt6) = a+b\,\tau\sqrt2+c\,\tau\sqrt3+d\,\tau\sqrt2\,\tau\sqrt3.$$
  ⇒ **$\tau$ 完全由 $\tau\sqrt2$、$\tau\sqrt3$ 決定**。
- [▶ 52:30](https://youtu.be/wtedDsycOZ8?t=3150)「**不能**把 $\sqrt2$ 送到 $\sqrt3$：$\sqrt2$ 是 $x^2-2$ 的根，若能，$\sqrt3$ 就得是 $x^2-2$ 的根——不是。」⇒ $\sqrt2\mapsto\pm\sqrt2$、$\sqrt3\mapsto\pm\sqrt3$，**四種口味**：

| | $\sqrt2\mapsto$ | $\sqrt3\mapsto$ |
|---|---|---|
| $1$ | $\sqrt2$ | $\sqrt3$ |
| $\tau$ | $\sqrt2$ | $-\sqrt3$ |
| $\sigma$ | $-\sqrt2$ | $\sqrt3$ |
| $\sigma\tau$ | $-\sqrt2$ | $-\sqrt3$ |

（D&F 的命名；老師在黑板上依固定體推回：$\sigma$ 固定 $\sqrt3$、$\tau$ 固定 $\sqrt2$。）
- $\sigma^2 = \tau^2 = 1$、$\sigma\tau = \tau\sigma$ ⇒
$$\mathrm{Gal}(K/\mathbb{Q}) = \mathrm{Gal}((x^2-2)(x^2-3)/\mathbb{Q}) = \{1,\sigma,\tau,\sigma\tau\}.$$
- 學生：「這是 **V 群**。」「什麼群？」「V 群。」「**Klein 四元群**，對。他叫它 V 群（Vierergruppe）——Gallian 裡的？」（學生打出 Aut 時被自動改成 Otto：「她男朋友姓 Otto。」）

【口頭】[▶ 56:30](https://youtu.be/wtedDsycOZ8?t=3390)「這次**所有可能**的自同構都出現了。**不一定**這樣：生成元要送到生成元，但能不能做到又跟其他結構**一致**，不一定。更複雜的例子會看到。」
- 「$\mathbb{Q}(\sqrt[3]2)$ 要修好，就加入三次單位根——得到 $x^3-2$ 的分裂體，Galois 群我想是 6 階，**$S_3$**，如果我記得對。那有點複雜，也許下次。」

**固定體**[▶ 57:30](https://youtu.be/wtedDsycOZ8?t=3450)【課堂討論】「$H_1 = \{1,\sigma\}$ 固定哪個子體？看一下就能答。」學生：「$\mathbb{Q}(\sqrt3)$。」
$$K^{\{1,\sigma\}} = \mathbb{Q}(\sqrt3),\qquad K^{\{1,\tau\}} = \mathbb{Q}(\sqrt2),\qquad K^{\{1,\sigma\tau\}} = \mathbb{Q}(\sqrt6).$$
- 【口頭】[▶ 59:00](https://youtu.be/wtedDsycOZ8?t=3540)「今天的**包含反轉**命題表示：**體塔**和 Galois 群的**子群格**之間有某種有趣的對應。這是我們該看的——也許下次。**那裡開始有點難**。但這就是**核心**。」

---

## 8. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $\mathrm{Aut}(K/F)\le\mathrm{Aut}(K)$ | $\sigma\tau x = x$、$\sigma^{-1}x = x$ |
| 自同構固定質子體 | $\sigma(1) = 1$ |
| **Prop 2**：$\sigma\alpha$ 是 $m_{\alpha,F}$ 的根 | 對 $f(\alpha) = 0$ 取 $\sigma$，係數不動 |
| $\mathrm{Aut}(\mathbb{Q}(\sqrt2)) = \{1,\sigma\}\cong\mathbb{Z}_2$ | $\sqrt2\mapsto\pm\sqrt2$ |
| $\mathrm{Aut}(\mathbb{Q}(\sqrt[3]2)) = \{1\}$ | 另兩根不是實數 |
| $K^H$ 是子體（$H$ 可以只是子集） | 對 $\pm,\times,{}^{-1}$ 封閉 |
| **包含反轉** | $F_1\subseteq F_2$ ⇒ $\mathrm{Aut}(K/F_2)\le\mathrm{Aut}(K/F_1)$；$H_1\le H_2$ ⇒ $K^{H_2}\subseteq K^{H_1}$ |
| $|\mathrm{Aut}(E/F)|\le[E:F]$，可分時相等 | D&F p.561 |
| Galois ⟺ $|\mathrm{Aut}(K/F)| = [K:F]$ | 可分多項式的分裂體是 Galois |
| $\mathrm{Gal}(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q})\cong V_4$ | 固定體 $\mathbb{Q}(\sqrt3)$、$\mathbb{Q}(\sqrt2)$、$\mathbb{Q}(\sqrt6)$ |

| 中文 | English |
|---|---|
| 自同構 | automorphism |
| 固定 | fix |
| $F$-固定自同構群 | $\mathrm{Aut}(K/F)$ |
| 固定體 | fixed field $K^H$ |
| 包含反轉 | inclusion reversing |
| Galois 擴張；Galois 群 | Galois extension; Galois group $\mathrm{Gal}(K/F)$ |
| Klein 四元群 | Klein four-group $V_4$ |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **子群格 ↔ 子體格（基本定理）** | [[25-L22-Galois理論基本定理]] |
| **Prop 5 的證明、$x^3-2$ 的 $S_3$** | [[25-L22-Galois理論基本定理]]、[[27-L23-Galois理論例子-上]] |
| **多項式的 Galois 群** | [[28-L24-多項式的Galois群]] |

---

## 附：本集一句話總結

> **固定基體 $F$ 的自同構構成群 $\mathrm{Aut}(K/F)$，而且它們把每個元素送到同一個最小多項式的另一個根——Galois 理論從這裡開始；反過來，任一組自同構的固定元素構成固定體 $K^H$，而群 ↔ 體的對應是包含關係反轉的；分裂體滿足 $|\mathrm{Aut}(E/F)|\le[E:F]$，相等時叫 Galois 擴張（可分多項式的分裂體都是），例如 $\mathbb{Q}(\sqrt2)$ 是、$\mathbb{Q}(\sqrt[3]2)$ 不是，而 $\mathbb{Q}(\sqrt2,\sqrt3)$ 的 Galois 群是 Klein 四元群，三個 2 階子群正好固定 $\mathbb{Q}(\sqrt3)$、$\mathbb{Q}(\sqrt2)$、$\mathbb{Q}(\sqrt6)$。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 21 錄影逐字稿（YouTube 自動字幕，59:26）與手寫講義 `Math422_Lecture21_GaloisBeginnings.pdf`（依 Dummit & Foote §14.1）整理。*
