---
course: Abstract Algebra II (Spring 2026)
episode: 29
lecture: L25
date: 2026-03-30
video: https://www.youtube.com/watch?v=Yc2ngBwDZVk
notes: 講義/AA2/Math422_Lecture25_GaloisConclusions.pdf
---

# 第 29 集 · L25：Galois 理論結語——根式可解性 [▶ 影片](https://www.youtube.com/watch?v=Yc2ngBwDZVk&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[28-L24-多項式的Galois群]] ｜ [總目錄](../README.md) ｜ 下一集：[[30-L26-模]] →

## 本集概要

D&F §14.7，回到學期初的起源故事——五次方程：
- **循環擴張**；含 $n$ 次單位根時 $F(\sqrt[n]a)/F$ 是循環的（Prop. 36）。
- **Lagrange 預解式**：反過來，循環擴張都是 $F(\sqrt[n]a)$ 的形式。群的**指數**；Kummer 理論（只提）。
- **根式可解**、**根式擴張**；Gauss 19 歲作出正 17 邊形。
- **定理 39**：$f$ 可用根式解 $\iff$ Galois 群**可解**。
- **推論 40**：$n\ge5$ 的一般方程不能用根式解（$S_n$ 不可解，因 $A_n$ 是單群）。例：$x^5-6x+3$。
- 微分 Galois 理論（$\int e^{x^2}dx$）。

> 📘 講義對應：Math422 Lecture 25「Galois Conclusions」；D&F §14.5（Prop. 29 附近，17 邊形）、§14.7（Prop. 36–37、Lemma 38、Thm 39、Cor. 40；p.626）、§4.6（$A_n$ 單）、§17.3（Kummer 理論）。

---

## 筆記

### 1. 循環擴張 [▶ 00:30](https://youtu.be/Yc2ngBwDZVk?t=30)

（老師想快點講完前半，把時間留給最後的計算——後來因為投影只寫了前面而作罷。）

- 基礎：$x^n = a$ 會解——$\sqrt[n]a$ 乘上各個 $n$ 次單位根。它們的自同構群很好，是**循環的** [▶ 01:00](https://youtu.be/Yc2ngBwDZVk?t=60)。

> **定義**：$K/F$ 是**循環擴張**（cyclic extension），若它是 Galois 的且 Galois 群循環。

- 若 $F$ 含 $n$ 次單位根，$F(\sqrt[n]a)$ 是 $x^n-a$ 的分裂體，Galois。否則不一定。
  - $x^2-p$：二次單位根只有 $-1 = e^{\pi i}$，任何體都有（特徵 2 會出問題——「我不想特徵 2，那是個壞地方，找比我聰明的人」）。$\mathbb{Q}(\sqrt p)$ 是循環的，群 $\{1,\sigma\}$ [▶ 03:00](https://youtu.be/Yc2ngBwDZVk?t=180)。
  - $\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}$ 不是 Galois。但 $\mathbb{Q}(i\sqrt3)(\sqrt[3]2)/\mathbb{Q}(i\sqrt3)$ 是：基礎體已含 $\zeta_3 = \frac{-1+i\sqrt3}2$。群 $\cong\mathbb{Z}_3$——就是 $x^3-2$ 的 Galois 群 $S_3$ 中由 $\sigma$ 生成的那個子群 [▶ 04:30](https://youtu.be/Yc2ngBwDZVk?t=270)。

> **命題 36**：$\operatorname{char}F\nmid n$，$F$ 含 $n$ 次單位根。則 $F(\sqrt[n]a)/F$ 是循環擴張，次數整除 $n$。

**證明** [▶ 06:00](https://youtu.be/Yc2ngBwDZVk?t=360)：$K = F(\sqrt[n]a)$ 含 $x^n-a$ 所有的根，是分裂體，Galois。$\sigma\in G$ 置換根，所以 $\sigma(\sqrt[n]a) = \zeta_\sigma\sqrt[n]a$（某個 $\zeta_\sigma\in\mu_n$）。
- $\psi(\sigma) = \zeta_\sigma$，$G\to\mu_n$。同態：$\sigma\tau(\sqrt[n]a) = \sigma(\zeta_\tau\sqrt[n]a) = \zeta_\tau\zeta_\sigma\sqrt[n]a$（$\zeta_\tau\in F$ 被 $\sigma$ 固定）。
- 核只有恆等 ⇒ 單射，$G$ 同構於 $\mu_n$ 的子群。由 Lagrange $|G|\mid n$；循環群的子群是循環的 [▶ 09:30](https://youtu.be/Yc2ngBwDZVk?t=570)。「game over man——呃，ladies。」（學生：「我不夠男人？」）

### 2. Lagrange 預解式 [▶ 10:00](https://youtu.be/Yc2ngBwDZVk?t=600)

$K/F$ 循環、次數 $n$、$\operatorname{char}F\nmid n$、$\mu_n\subseteq F$，$\sigma$ 生成 $G$。對 $\alpha\in K$、$\zeta\in\mu_n$ 定義 **Lagrange 預解式**
$$(\alpha,\zeta) = \alpha+\zeta\sigma(\alpha)+\zeta^2\sigma^2(\alpha)+\cdots+\zeta^{n-1}\sigma^{n-1}(\alpha).$$
- 「這到底是什麼？大概像多項式吧。」作用 $\sigma$：$\zeta$ 被固定，$\sigma^n = 1$，$\zeta^{n} = 1$ 所以 $\zeta^{n-1} = \zeta^{-1}$，得
$$\sigma(\alpha,\zeta) = \zeta^{-1}(\alpha,\zeta) \quad\Rightarrow\quad\sigma\big((\alpha,\zeta)^n\big) = (\alpha,\zeta)^n.$$
  所以 $(\alpha,\zeta)^n\in F$（老師先說成預解式本身在 $F$，再改正）[▶ 13:00](https://youtu.be/Yc2ngBwDZVk?t=780)。
- 用自同構的線性獨立（特徵標那段，之前略過）可選 $\alpha$ 使預解式非零；$\sigma^j$（$j<n$）不固定它，所以它不在任何真子體裡，$K = F((\alpha,\zeta))$——預解式就是在 $F$ 上構造 $n$ 次方根的方法 [▶ 15:00](https://youtu.be/Yc2ngBwDZVk?t=900)。
- 「Lagrange 花了十年、甚至幾十年發明這東西。」（學生：「比 Galois 一生還長。」）（「我想讓你們聽到我用 Tucker Carlson 的語氣說 sorry。」）

> **命題 37**：上述條件下，循環擴張都形如 $F(\sqrt[n]a)$。

**群的指數**（exponent）[▶ 17:00](https://youtu.be/Yc2ngBwDZVk?t=1020)：使所有 $g^m = e$ 的正整數 $m$。群的階一定是指數，但可能有更小的。
- 老師的 RSA 故事：教數論時給學生一個加密指數，結果學生加密後得到原訊息——因為那個指數剛好是群指數的倍數加 1，群又不是循環的 [▶ 17:30](https://youtu.be/Yc2ngBwDZVk?t=1050)。
- 例：$U(\mathbb{Z}_{11}\times\mathbb{Z}_7)\cong\mathbb{Z}_{10}\times\mathbb{Z}_6$，60 個元素，指數 30（$\operatorname{lcm}(10,6)$）。D&F 沒說「最小」，老師也刻意避開這點（學生 Shane 偏要問）[▶ 20:30](https://youtu.be/Yc2ngBwDZVk?t=1230)。
- 連續加入 $n$ 次方根得到的擴張，Galois 群的指數是 $n$（D&F p.626）。**Kummer 理論**（§17.3）用 $F^\times/(F^\times)^n$ 的子群分類這類交換擴張——「看起來很嚇人，超出我的專長」[▶ 23:00](https://youtu.be/Yc2ngBwDZVk?t=1380)。

### 3. 根式可解 [▶ 23:30](https://youtu.be/Yc2ngBwDZVk?t=1410)

以下只看特徵 0。

> **定義**：$\alpha$（在 $F$ 上代數）**可用根式表示**（solved for in terms of radicals），若 $\alpha\in K$，且
> $$F = K_0\subseteq K_1\subseteq\cdots\subseteq K_s = K,\qquad K_{i+1} = K_i(\sqrt[n_i]{a_i}),\ a_i\in K_i,$$
> 每一步都是單根式擴張。這樣的 $K$ 叫 **根擴張**（root extension）。$f(x)$ **可用根式解**，若它的所有根都可用根式表示 [▶ 25:00](https://youtu.be/Yc2ngBwDZVk?t=1500)。

- 這就是 Lagrange 解不出來、Abel 證明不可能、Galois 說明何時可能的問題：能否用係數的算術運算和開根號寫出根的公式。

**例：正 17 邊形**（D&F §14.5）[▶ 26:30](https://youtu.be/Yc2ngBwDZVk?t=1590)：$\mathbb{Q}\subset\mathbb{Q}(\sqrt{17})\subset\mathbb{Q}(\sqrt{17-\sqrt{17}})\subset\cdots$，一連串加入平方根，次數 2、4、8、16，得到 $\zeta_{17}$。
- **Gauss 19 歲**做出來的。（學生：「然後他就死了？」——「不，那是 Galois。Gauss 活到很老，是個暴躁老頭。」）比 Galois 早二三十年，所以這類遊戲在當時「就在空氣裡」。尺規作圖對應 $2^k$ 次擴張。

> **引理 38**（不證）：若 $\alpha$ 在某個根擴張中，則 $\alpha$ 在某個對 $F$ 是 Galois 的根擴張中，且每一步 $K_{i+1}/K_i$ 是循環的。

### 4. 主定理 [▶ 30:30](https://youtu.be/Yc2ngBwDZVk?t=1830)

> **定義**：有限群 $G$ **可解**，若有子群鏈 $1 = G_s\le G_{s-1}\le\cdots\le G_0 = G$，$G_{i+1}\lhd G_i$，且每個 $G_i/G_{i+1}$ 是循環群。

- 作業證過：可解群的子群、商群可解；$H\lhd G$ 且 $H$、$G/H$ 可解 ⇒ $G$ 可解（其實是 iff，另一方向太技術被拿掉了）[▶ 32:00](https://youtu.be/Yc2ngBwDZVk?t=1920)。（「我得改你們的作業了」；學生說了句 Clash Royale 的「嘿哈」。）

> **定理 39**（Galois）：$f(x)$ 可用根式解 $\iff$ 它的 Galois 群可解。

- 「我非常死忠於特徵 0。」——學生：「保持實在（keep it real）。」——「或至少保持有理。」
- 直覺：根式擴張的每一步給出循環的 Galois 群；一步步疊起來就是可解群的定義。
- **（⇒）** [▶ 35:30](https://youtu.be/Yc2ngBwDZVk?t=2130)：每個根在引理 38 那種擴張裡；這些擴張的合成 $L$ 仍是同一類（Prop. 21）。對應的子群 $G_i$ 給出 $\mathrm{Gal}(K_{i+1}/K_i) = G_i/G_{i+1}$ 循環，所以 $\mathrm{Gal}(L/F)$ 可解。$L$ 包含 $f$ 的分裂體，所以 $f$ 的 Galois 群是可解群的商，可解。（老師承認這部分講得零碎——它和前兩個命題緊密交纏。）
- **（⇐）** [▶ 42:30](https://youtu.be/Yc2ngBwDZVk?t=2550)：$K$ 是分裂體，$G = \mathrm{Gal}(K/F)$ 可解。用 Galois 對應把子群鏈變成體鏈 $F = K_0\subseteq K_1\subseteq\cdots\subseteq K_s = K$（包含反轉），每步循環、次數 $n_i$。但還不是根式擴張——需要基礎體有 $n_i$ 次單位根；所以先把單位根加進去，再用 Prop. 37，每一步就成了根式擴張 [▶ 47:00](https://youtu.be/Yc2ngBwDZVk?t=2820)。

> **推論 40**：$n\ge5$ 時，一般 $n$ 次方程不能用根式解 [▶ 48:00](https://youtu.be/Yc2ngBwDZVk?t=2880)。

- 上次證明一般多項式的 Galois 群是 $S_n$。而 $n\ge5$ 時 $S_n$ **不可解**：D&F §4.6 Thm 24——**$A_n$ 是單群**（$n\ge5$）[▶ 50:00](https://youtu.be/Yc2ngBwDZVk?t=3000)。
- 單群沒有有意義的商群（只有平凡群和自己）；可解群卻是靠商群攜帶資訊——性質正好相反 [▶ 51:30](https://youtu.be/Yc2ngBwDZVk?t=3090)。
- $S_n$ 的非平凡正規子群只有 $A_n$（指數 2，偶置換），而 $A_n$ 又是單的，鏈走不下去。「其餘的故事在第 4 章，得留一些給研究所。」

> 💬 補充（非課堂內容）：老師用「指數為最小質因數的子群必正規」的定理來找正規子群，那只是充分條件，不能排除其他正規子群；「$n\ge5$ 時 $S_n$ 的正規子群只有 $1,A_n,S_n$」需要用 $A_n$ 單的性質另外證明。

**例** [▶ 55:00](https://youtu.be/Yc2ngBwDZVk?t=3300)：$f(x) = x^5-6x+3\in\mathbb{Q}[x]$。可以證明它的 Galois 群含一個 5-循環和一個對換，所以是 $S_5$，**不能用根式解**——一個具體的五次方程。
- D&F 接著用 Galois 群推導二次、三次（Cardano）、四次公式——「Cardano 我們已經花太多時間了，不要再揭開那道傷口。」學生：「我覺得遠遠太多了。」

### 5. 微分 Galois 理論 [▶ 57:00](https://youtu.be/Yc2ngBwDZVk?t=3420)

- Galois 理論的想法更一般：解方程（例如**微分方程**）也有 Galois 理論——**微分 Galois 理論**。
- 例：$\int e^{x^2}dx$ 不能用**初等函數**表示。「初等函數」扮演根式擴張的角色：在基礎體上加入初等函數，能不能解出這個方程？也有微分 Galois 群。
- 老師的弟弟帶過四個大學生的專題，有一份四頁的精簡 PDF（老師找不到了）。重點：看「保持結構的自同構群」這個主題在抽象數學裡一再出現。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 循環擴張 | cyclic extension | §1 |
| Lagrange 預解式 | Lagrange resolvent | §2 |
| 群的指數 | exponent of a group | §2 |
| Kummer 理論 | Kummer theory | §2 |
| 根式可解 | solvable by radicals | §3 |
| 根擴張 | root extension | §3 |
| 可解群 | solvable group | §4 |
| 交錯群 | alternating group | §4 |
| 微分 Galois 理論 | differential Galois theory | §5 |
| 初等函數 | elementary functions | §5 |

## ⚠️ 待確認清單

（本集無）
