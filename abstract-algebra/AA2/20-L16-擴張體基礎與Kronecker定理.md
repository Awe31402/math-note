---
course: Abstract Algebra II (Spring 2026)
episode: 20
lecture: L16
date: 2026-02-27
video: https://www.youtube.com/watch?v=NnwhqJ9vJw8
notes: 講義/AA2/Math422_Lecture16_FieldExtensions.pdf
---

# 第 20 集 · L16：擴張體基礎、Kronecker 定理 [▶ 影片](https://www.youtube.com/watch?v=NnwhqJ9vJw8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[19-複習-BossFight1]] ｜ [總目錄](../README.md) ｜ 下一集：[[21-L18-擴張體與分裂體]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 20 集，Lecture 16
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（56:19，自動字幕）＋ 手寫講義 `Math422_Lecture16_FieldExtensions.pdf`（9 頁），依 Dummit & Foote §13.1。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 特徵](#1-特徵)
- [2. 質子體](#2-質子體)
- [3. 擴張體與次數](#3-擴張體與次數)
- [4. 體同態不是 0 就是單射](#4-體同態不是-0-就是單射)
- [5. Kronecker 定理](#5-kronecker-定理)
- [6. K = F[x]/(p) 的基底：1, θ, …, θⁿ⁻¹](#6-k--fxp-的基底1-θ--θⁿ⁻¹)
- [7. 單擴張；x³ − 2 的三個根](#7-單擴張x³--2-的三個根)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/NnwhqJ9vJw8?t=0) 課前禱告。「今天要看的問題：把給定的體**系統地**放進一個更大的體。目標連回最根本的問題——**怎麼解多項式**？如果多項式在給定的體裡沒有解，能不能造一個**更大的體**讓它有解？這是這堂課的**核心動機**。」

---

## 1. 特徵

> **定義（特徵 characteristic）**（講義 p.1）[▶ 01:00](https://youtu.be/NnwhqJ9vJw8?t=60)　體 $F$ 的特徵是使 $p\cdot1_F = \underbrace{1_F+\cdots+1_F}_{p} = 0$ 的**最小**正整數 $p$，記 $\mathrm{ch}(F) = p$；若不存在，$\mathrm{ch}(F) = 0$。

> **命題**（講義 p.1，D&F §13.1 第一個命題）　$\mathrm{ch}(F)$ 是 0 或質數 $p$。若 $\mathrm{ch}(F) = p$，則 $p\cdot\alpha = \alpha+\cdots+\alpha = 0$ 對所有 $\alpha\in F$。

- [▶ 02:00](https://youtu.be/NnwhqJ9vJw8?t=120)「**一定是質數**：若特徵是 6，$2\cdot3 = 0$ 就有**零因子**——但體沒有零因子。」
- [▶ 03:00](https://youtu.be/NnwhqJ9vJw8?t=180)【課堂討論】「$m\cdot1_F+n\cdot1_F$ 是什麼？$(m\cdot1_F)(n\cdot1_F)$ 呢？」「$(m+n)\cdot1_F$、$mn\cdot1_F$。」

---

## 2. 質子體

[▶ 04:00](https://youtu.be/NnwhqJ9vJw8?t=240)（講義 p.2）
- $\varphi:\mathbb{Z}\to F$，$\varphi(n) = n\cdot1_F$ 是**環同態**。
- $\mathbb{Z}$ 的理想只有 $n\mathbb{Z}$ ⇒ $\ker\varphi = \{0\}$（特徵 0）或 $p\mathbb{Z}$（特徵 $p$）。
- $\bar\varphi:\mathbb{Z}/\ker\varphi\to F$ 是**單射** ⇒ $F$ 裡有 $\mathbb{Z}$ 或 $\mathbb{Z}_p$ 的副本。
- $F$ 是體 ⇒ 由 $\varphi(\mathbb{Z})$ 生成的**分式體**也在 $F$ 裡：特徵 0 是 $\mathbb{Q}$ 的副本，特徵 $p$ 是 $\mathbb{Z}_p$（本身已是體）。

> **定義（質子體 prime subfield）**（講義 p.2）[▶ 07:00](https://youtu.be/NnwhqJ9vJw8?t=420)　由 $1_F$ 生成的子體——同構於 $\mathbb{Q}$ 或 $\mathbb{F}_p$。

- 「一直把 1 加自己：**回到 0** ⇒ 有 $\mathbb{Z}_p$ 的副本；**一直走下去** ⇒ 有整數的副本，而體裡反元素都在 ⇒ 有 $\mathbb{Q}$ 的副本。」
- 記號：D&F 用 $\mathbb{F}_p$ 表示 $\mathbb{Z}/p\mathbb{Z}$。（[▶ 09:00](https://youtu.be/NnwhqJ9vJw8?t=540) 學生問 $\mathbb{F}_p$ 和 $\mathbb{Z}_p$ 是不是同一個東西；老師：「就是 $\mathbb{Z}/p\mathbb{Z}$，只是 D&F 的記號。」）

**例**（講義 p.2）[▶ 10:00](https://youtu.be/NnwhqJ9vJw8?t=600)
- **E1**：$\mathbb{Q}$ 是 $\mathbb{R}$、$\mathbb{C}$、$\mathbb{Q}$ 的質子體（「子體可以是整個體」）。
- **E3**：有理函數體 $\mathbb{R}(x) = \{f/g : g\neq0\}$ 的質子體是 $\mathbb{Q}$。
- **E2**：$\mathbb{F}_p$ 是 $\mathbb{F}_p$、$\mathbb{F}_p(t)$ 的質子體。【課堂討論】[▶ 12:00](https://youtu.be/NnwhqJ9vJw8?t=720)「考試那題 $\mathbb{Z}_2[x]/(x^2+x+1)$ 的質子體？」「$\mathbb{Z}_2$。」
- 【課堂討論】「你們知道**特徵 $p$ 的無窮體**嗎？」——$\mathbb{Z}_p(x)$，係數在 $\mathbb{Z}_p$ 的有理函數。「這是無窮的吧？……突然我**不確定**了。只要在有限體上工作，我就有點不自在。老實說，**特徵 0 讓我比較自在**。」

💬 $\mathbb{F}_p(x)$ 確實是無窮的：$1,x,x^2,\dots$ 兩兩不同。

---

## 3. 擴張體與次數

> **定義（擴張體）**（講義 p.3）[▶ 14:00](https://youtu.be/NnwhqJ9vJw8?t=840)　$K$ 是含子體 $F$ 的體，就說 $K$ 是 $F$ 的**擴張體**，記 $K/F$，或畫成**體塔**：
> $$\begin{matrix}K\\ |\\ F\end{matrix}$$
> $F$ 叫**基體**（base field）。

**觀察**[▶ 15:00](https://youtu.be/NnwhqJ9vJw8?t=900)：$F$ 的元素可以乘 $K$ 的元素，結果還在 $K$；$K$ 加法交換、結合……⇒ **$K$ 是 $F$ 上的向量空間**。

> **定義（次數）**（講義 p.3）[▶ 16:30](https://youtu.be/NnwhqJ9vJw8?t=990)　$[K:F] = \dim_FK$。有限時叫**有限擴張**。

**例**[▶ 17:30](https://youtu.be/NnwhqJ9vJw8?t=1050)
- $\mathbb{C} = \mathrm{span}_\mathbb{R}\{1,i\}$ ⇒ $[\mathbb{C}:\mathbb{R}] = 2$，有限擴張。
- $\mathbb{R}/\mathbb{Q}$：「**每個體都是它質子體的擴張**。」但 $\mathbb{R}$ 作為 $\mathbb{Q}$ 向量空間是**無窮維**——沒有有限個實數，其有理線性組合能給出所有實數。

---

## 4. 體同態不是 0 就是單射

[▶ 19:30](https://youtu.be/NnwhqJ9vJw8?t=1170)「作業裡研究過**從體出發**的環同態，結果**很無聊**。」
- 【課堂討論】「體的理想能是什麼？」「體裡非零元都是……」「**單位**。」「含單位的理想？」「整個體。」「所以體的理想只有：**全部和『沒有』**——『沒有』是 0，不是真的沒有。」
- $\varphi:F\to F'$ 體同態（「這是給你的，Emma」）：$\ker\varphi = F$ ⇒ $\varphi\equiv0$；或 $\ker\varphi = 0$ ⇒ **單射**。

> **命題**（講義 p.3）　任何**不恆為零**的體同態都是**單射**。

【口頭】[▶ 22:00](https://youtu.be/NnwhqJ9vJw8?t=1320)「第 13 章**一再一再**用到這個。只要有證據說同態把某個東西送到非零，它就**自動單射**。如果以後我忘了，你們要**糾正我**。我**一定**會忘，這是我的天性。」

---

## 5. Kronecker 定理

[▶ 22:00](https://youtu.be/NnwhqJ9vJw8?t=1320)「這是我**也許整門課最喜歡**的定理。D&F **不講歷史**，但我在別處看到它叫 Kronecker 定理，所以我這樣叫。」

> **定理 3（Kronecker）**（講義 p.4，D&F §13.1 Thm 3）[▶ 22:30](https://youtu.be/NnwhqJ9vJw8?t=1350)　$F$ 體，$p(x)\in F[x]$ **不可約**。則存在體 $K$，含 $F$ 的同構副本，且 $p(x)$ 在 $K$ 中**有根**。把 $F$ 等同於這個副本，就是說：存在 $F$ 的擴張使 $p(x)$ 有根。

**證明**[▶ 25:00](https://youtu.be/NnwhqJ9vJw8?t=1500)「我其實**已經劇透過了**——就是考試那題的那種東西。」
- 【課堂討論】「$p$ 不可約，$(p(x))$ 是什麼？」「**極大理想**。」「商掉呢？」「**體**。」
- 令 $K = F[x]/(p(x))$——是體。（「D&F 多用圓括號，我有時用角括號，都可以。」）
- **$F$ 的副本**[▶ 27:30](https://youtu.be/NnwhqJ9vJw8?t=1650)：$\pi:F[x]\to K$，$\pi(f) = f+(p)$ 是環同態。（「D&F 可能寫 $f(x)\bmod p(x)$。那沒問題，我只是**從不**在任何地方用 mod，我不喜歡。」）限制到常數多項式 $F$：$\pi|_F(1) = 1+(p)\neq0$ ⇒ **不恆為零 ⇒ 單射**（§4）⇒ $F\cong\pi(F)\subseteq K$。
- **根**[▶ 31:30](https://youtu.be/NnwhqJ9vJw8?t=1890)：令 $\theta = x+(p(x))$（「之前我用 $\alpha$，現在跟 D&F 用 $\theta$」）。「D&F 的論證**不具體**，是套環同態的定理。我覺得**寫出來**比較有幫助——別擔心，不做歸納，『**別告訴 Spano 博士**』。」
  - $\theta^k = x^k+(p)$，所以 $p(x) = a_nx^n+\cdots+a_0$ 時
$$p(\theta) = a_n\theta^n+\cdots+a_1\theta+a_0 = a_nx^n+\cdots+a_0+(p) = p(x)+(p) = (p) = 0\ \text{in }K.\ \blacksquare$$

【講義補充】講義 p.4：「如果你比較喜歡 D&F p.513 的論證，就用它。」

---

## 6. K = F[x]/(p) 的基底：1, θ, …, θⁿ⁻¹

> **定理 4**（講義 p.5，D&F Thm 4）[▶ 24:30](https://youtu.be/NnwhqJ9vJw8?t=1470)　$p(x)\in F[x]$ 不可約、$\deg p = n$，$K = F[x]/(p)$，$\theta = x+(p)$。則 $1,\theta,\dots,\theta^{n-1}$ 是 $K$ 在 $F$ 上的**基底**，$[K:F] = n$：
> $$K = \{a_0+a_1\theta+\cdots+a_{n-1}\theta^{n-1} : a_i\in F\}.$$

[▶ 35:00](https://youtu.be/NnwhqJ9vJw8?t=2100)（學生：「定理證完了嗎？」「證完了。但我想用這計算**做更多**。」）

**張成**[▶ 36:00](https://youtu.be/NnwhqJ9vJw8?t=2160)：任取 $a(x)+(p)\in K$。**除法算法**：$a = p\,b+r$，$r = 0$ 或 $\deg r<n$ ⇒
$$a(x)+(p) = r(x)+(p) = r_0+r_1\theta+\cdots+r_{n-1}\theta^{n-1}.$$
- （中間把壞掉的麥克筆**丟進垃圾桶**：「每丟一支，就少一支會再惹我生氣的筆。」學生：「你的 $b$ 看起來像降記號 $\flat$。」「試著讓它**升**一點？我自己走進去的。」）
- （老師差點寫 $a(x)+p(x) = r(x)$：「**這會讓我惹麻煩**——你們這樣寫我會扣分。如果我聰明點，就寫『$\bmod p(x)$』——**這就是他們那樣寫的原因**。你們可以用 D&F 的記號。」）
- 【Q&A】[▶ 40:30](https://youtu.be/NnwhqJ9vJw8?t=2430) 學生：「怎麼知道是到 $n-1$？$r_{n-1}$ 可能是 0？」老師：「對，我**沒說**這些係數非零——$r$ 甚至可以是零多項式。重點是任何多項式都能模 $p$ 化約到次數 $\le n-1$。」

**線性獨立**[▶ 41:30](https://youtu.be/NnwhqJ9vJw8?t=2490)：設有 $b_0,\dots,b_{n-1}\in F$ **不全為零**，$b_0+b_1\theta+\cdots+b_{n-1}\theta^{n-1} = 0$。令 $b(x) = b_0+\cdots+b_{n-1}x^{n-1}$——非零、次數 $\le n-1$。
- 「我聲稱 $b(x)\in(p(x))$……怎麼看出來的……」（老師卡了一下。）
- ⇒ $p$（次數 $n$）整除次數更低的非零 $b$，**不可能**。$\blacksquare$

💬 卡住的那一步：$b(\theta) = b(x)+(p)$，所以 $b(\theta) = 0$ in $K$ 就是說 $b(x)+(p) = (p)$，即 **$b(x)\in(p(x))$**。

- 【Q&A】[▶ 46:00](https://youtu.be/NnwhqJ9vJw8?t=2760) 學生：「『不全為零』是說全部 $b$ 都……？」老師：「是說**至少一個非零**。不是說不能有 0。好問題。」
- 【口頭】[▶ 45:30](https://youtu.be/NnwhqJ9vJw8?t=2730)「這**很棒**：用不可約多項式商出來的擴張，我們知道**次數**、能寫下**基底**，還能很自然地**計算**。」

【講義補充】**推論 5**（講義 p.6）：$K$ 中加法就是多項式加法；乘法 $a(\theta)b(\theta) = r(\theta)$，$r$ 是 $a(x)b(x)$ 除以 $p(x)$ 的**餘式**。

---

## 7. 單擴張；x³ − 2 的三個根

【課堂討論】[▶ 46:30](https://youtu.be/NnwhqJ9vJw8?t=2790)「誰能給我一個有趣的不可約多項式？」學生：「$x^2+1$。」「當然可以。」學生：「$x^2+67$。」「**打得好**。我想看個比較不熟的。」

**例 5**（講義 p.8）[▶ 47:30](https://youtu.be/NnwhqJ9vJw8?t=2850)：$p(x) = x^3-2$。【課堂討論】「不可約嗎？」學生：「**在哪裡上**？」「很好，謝謝。你們學到很多東西。」（「我出考試是**為了讓人學習**。考你已經會的東西就沒意思了。」）在 $\mathbb{Q}$ 上用 Eisenstein（$p = 2$）不可約。
- $z^3 = 2$ 在 $\mathbb{C}$ 的解：$\sqrt[3]2$、$\omega\sqrt[3]2$、$\omega^2\sqrt[3]2$，$\omega = e^{2\pi i/3} = \frac{-1+i\sqrt3}2$、$\omega^2 = e^{4\pi i/3} = \frac{-1-i\sqrt3}2$。由因式定理
$$x^3-2 = (x-\sqrt[3]2)(x-\omega\sqrt[3]2)(x-\omega^2\sqrt[3]2).$$

💬 [▶ 49:30](https://youtu.be/NnwhqJ9vJw8?t=2970) 老師說 $\omega$ 那點的角度是「$\pi/3$，$\cos(\pi/3) = -\frac12$」——角度是 **$2\pi/3$**，$\cos(2\pi/3) = -\frac12$。

> **定義**（講義 p.6）[▶ 51:00](https://youtu.be/NnwhqJ9vJw8?t=3060)　$K/F$，$\alpha,\beta,\dots\in K$。含 $F$ 和 $\alpha,\beta,\dots$ 的**最小**子體記 $F(\alpha,\beta,\dots)$，叫由它們**生成**的體。若 $K = F(\alpha)$，叫**單擴張**（simple extension）。

- 「最小」的意思：**所有**含 $F,\alpha,\beta,\dots$ 的子體的**交**（子體的交還是子體；$K$ 本身就是一個，所以非空）。「我們一直在**沒有理由**地用這記號，現在給了理由。」
- 「新元素**不一定是新的**——蠢例子：$\mathbb{R}(\pi) = \mathbb{R}$。另一方面，$\mathbb{R}(i) = \mathbb{C}$。」

**三個根給出同構的體**[▶ 53:00](https://youtu.be/NnwhqJ9vJw8?t=3180)
$$\mathbb{Q}(\sqrt[3]2)\cong\mathbb{Q}(\omega\sqrt[3]2)\cong\mathbb{Q}(\omega^2\sqrt[3]2)\cong\mathbb{Q}[x]/(x^3-2).$$
- 「第一個**明顯是實數**的子體——有理數加一個實數。後兩個**不是**實數的子體。所以它們**根本不是同一個體**，卻全都**同構**：每個都是 $\theta^3 = 2$ 的 $\mathbb{Q}(\theta)$。」
- 【口頭】[▶ 55:30](https://youtu.be/NnwhqJ9vJw8?t=3330)「這是 **§13.1 的終極教訓**——我還沒講的定理會把它抽象地講明：不可約多項式的**不同根**，加進基體都得到**同構的擴張**。**所有根都一樣**。這正是 **Galois 理論的核心**：根之間有某種潛在的**對稱**。」學生：「我們要開始 Galois 了！」

💬 講義 p.8 例 5 最後一行寫成 $\mathbb{Q}(\sqrt[3]3)$——應是 **$\sqrt[3]2$**。

【講義補充】講義 p.7–9 的定理（本集還沒講）：
- **Thm 6**（D&F p.517）：$p$ 不可約、$\alpha\in K$ 是 $p$ 的根 ⇒ $F(\alpha)\cong F[x]/(p(x))$。證明：$\varphi(a(x)) = a(\alpha)$，$p\in\ker\varphi$，$(p)$ 極大 ⇒ 像是含 $F$ 和 $\alpha$ 的體 ⇒ 就是 $F(\alpha)$。
- **Cor 7**：$F(\alpha) = \{a_0+a_1\alpha+\cdots+a_{n-1}\alpha^{n-1}\}$。
- **E4**：$\mathbb{Q}(\sqrt2)\cong\mathbb{Q}(-\sqrt2)\cong\mathbb{Q}[x]/(x^2-2)$；$a+b\sqrt2\mapsto a-b\sqrt2$ 其實是**自同構**，因為 $\mathbb{Q}(\sqrt2) = \mathbb{Q}(-\sqrt2)$。
- **Thm 8**：體同構 $\varphi:F\to F'$、$p$ 不可約、$p'$ 是係數套 $\varphi$ 得到的多項式；$\alpha$、$\beta$ 分別是根 ⇒ 存在同構 $\sigma:F(\alpha)\to F'(\beta)$，$\alpha\mapsto\beta$、$\sigma|_F = \varphi$。

---

## 8. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $\mathrm{ch}(F) = 0$ 或質數 | 合數會有零因子 |
| 質子體 $\cong\mathbb{Q}$ 或 $\mathbb{F}_p$ | $n\mapsto n\cdot1_F$，核 $0$ 或 $p\mathbb{Z}$ |
| $K/F$ ⇒ $K$ 是 $F$ 向量空間 | $[K:F] = \dim_FK$ |
| 體同態不是 0 就是單射 | 體的理想只有 $0$、$F$ |
| **Kronecker**：不可約 $p$ 在某擴張有根 | $K = F[x]/(p)$，$\theta = x+(p)$，$p(\theta) = 0$ |
| $[F[x]/(p):F] = \deg p$ | 除法算法張成；$b(\theta) = 0$ ⇒ $p\mid b$ 獨立 |
| 同一不可約多項式的根給同構的體 | $\mathbb{Q}(\omega^k\sqrt[3]2)\cong\mathbb{Q}[x]/(x^3-2)$ |

| 中文 | English |
|---|---|
| 特徵 | characteristic |
| 質子體 | prime subfield |
| 擴張體；基體 | extension field; base field |
| 體塔 | tower of fields |
| 次數；有限擴張 | degree; finite extension |
| 單擴張 | simple extension |
| 由…生成的體 | field generated by |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **Thm 6、8；代數擴張；分裂體** | [[21-L18-擴張體與分裂體]] |
| **特徵 $p$、重根** | [[22-L19-可分擴張]] |
| **根之間的對稱 → Galois 群** | [[24-L21-Galois擴張與Galois群]] |

---

## 附：本集一句話總結

> **體的特徵是 0 或質數，質子體因此是 $\mathbb{Q}$ 或 $\mathbb{F}_p$；擴張 $K/F$ 讓 $K$ 成為 $F$ 向量空間、次數 $[K:F] = \dim_FK$；體同態不是 0 就是單射；Kronecker 定理用 $K = F[x]/(p(x))$、$\theta = x+(p)$ 給不可約多項式造出一個根，而 $1,\theta,\dots,\theta^{n-1}$ 是基底、$[K:F] = \deg p$；最後 $x^3-2$ 的三個根（一實兩虛）生成的體雖然不同卻都同構——根之間的對稱就是 Galois 理論的核心。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 16 錄影逐字稿（YouTube 自動字幕，56:19）與手寫講義 `Math422_Lecture16_FieldExtensions.pdf`（依 Dummit & Foote §13.1）整理。*
