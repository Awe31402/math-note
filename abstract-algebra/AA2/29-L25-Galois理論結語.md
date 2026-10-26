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

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 29 集，Lecture 25
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:47，自動字幕）＋ 手寫講義 `Math422_Lecture25_GaloisConclusions.pdf`（6 頁），依 Dummit & Foote §14.7。前半投影講義，後半黑板照 D&F 唸。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 回到五次方程](#0-回到五次方程)
- [1. 循環擴張；單根式擴張](#1-循環擴張單根式擴張)
- [2. F 含 n 次單位根 ⇒ F(ⁿ√a)/F 循環（Prop 36）](#2-f-含-n-次單位根--fⁿaf-循環prop-36)
- [3. Lagrange 預解式；循環 ⇒ 根式（Prop 37）](#3-lagrange-預解式循環--根式prop-37)
- [4. 群的指數；Kummer 理論](#4-群的指數kummer-理論)
- [5. 根式擴張；Gauss 的正 17 邊形](#5-根式擴張gauss-的正-17-邊形)
- [6. 可根式解 ⟺ Galois 群可解（Thm 39）](#6-可根式解--galois-群可解thm-39)
- [7. 一般五次方程不可根式解](#7-一般五次方程不可根式解)
- [8. 微分 Galois 理論](#8-微分-galois-理論)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 回到五次方程

[▶ 00:00](https://youtu.be/Yc2ngBwDZVk?t=0) 課前禱告：「我們研究**可解性**和 Galois 擴張。」「我想**快速推過**這講的開頭，好**停留**在最後那個計算——我覺得那是**最有趣**的部分，而它不在投影片上。」

（講義 p.1）[▶ 00:30](https://youtu.be/Yc2ngBwDZVk?t=30)「Lecture 25：**根式擴張與可解性**。這回到**整件事的起源**：想用係數的**簡單公式**解五次多項式方程，像**二次公式**那樣。這最終**驅使 Galois** 發現群論論證。現在我們試著**重走他的腳步**。」
- 「整個討論的基礎：我們**會解** $x^n = a$——找 $\sqrt[n]a$，再乘上 $n$ 次單位根的冪，填滿解集。就這樣。之前看過它們的自同構群——**特別好**，其實是**循環**的。」

---

## 1. 循環擴張；單根式擴張

> **定義**（講義 p.1）[▶ 01:30](https://youtu.be/Yc2ngBwDZVk?t=90)　$K/F$ 是 Galois 且 Galois 群**循環**，叫**循環擴張**（cyclic extension）。

**單根式擴張**：在 $F$ 加入某個 $a\in F$ 的 $n$ 次根。$x^n-a$ 的解有 $\sqrt[n]a$（任一個特定解）和 $\sqrt[n]a\,\zeta_n^k$；所以 **$F$ 含 $n$ 次單位根**時，$F(\sqrt[n]a)$ 表現「**很好**」——它是分裂體、Galois。

**例 1**（講義 p.1）[▶ 02:30](https://youtu.be/Yc2ngBwDZVk?t=150)：$x^2-p$（$p$ 質數）。$\zeta_2 = e^{\pi i} = -1$——「哪些體含 2 次單位根？**答案是：都含**。」
- 【口頭】「特徵 2 可能有什麼壞掉——我不想特徵 2。如果有什麼壞話要說特徵 2，**不會是我說的**。我只說：**遠離特徵 2**，那是個**壞地方**，要找**比我聰明得多**的人。」
- $\mathbb{Q}(\sqrt p)$ 是分裂體，$\mathrm{Gal} = \{1,\sigma\}$，$\sigma(a+b\sqrt p) = a-b\sqrt p$（「某種**假複數共軛**」）⇒ 2 階循環。

**例 2**（講義 p.1）[▶ 04:00](https://youtu.be/Yc2ngBwDZVk?t=240)：$\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}$ **不行**（自同構只有恆等）。但取 $F = \mathbb{Q}(i\sqrt3)$——它含 $\zeta_3 = \frac{-1+i\sqrt3}2$ ⇒ $F(\sqrt[3]2)$ 分裂 $x^3-2$，而且
$$\mathrm{Gal}(\mathbb{Q}(i\sqrt3,\sqrt[3]2)/\mathbb{Q}(i\sqrt3))\cong\mathbb{Z}_3.$$
「這就是 $x^3-2$ 在 $\mathbb{Q}$ 上的 Galois 群 $S_3$ 裡，$\sigma$ 生成的那個 3 階循環子群。」「**單根式擴張有循環 Galois 群**。」

---

## 2. F 含 n 次單位根 ⇒ F(ⁿ√a)/F 循環（Prop 36）

> **命題 36**（講義 p.2）[▶ 06:00](https://youtu.be/Yc2ngBwDZVk?t=360)　$F$ 的特徵不整除 $n$，且 $F$ 含 $n$ 次單位根。則對 $a\in F$，$F(\sqrt[n]a)/F$ 是**循環**擴張，次數**整除 $n$**。

**證明**：
- $K = F(\sqrt[n]a)$ 含 $x^n-a$ 的所有根（$F$ 已有單位根）⇒ 分裂體 ⇒ **Galois**。
- $\sigma\in\mathrm{Gal}(K/F)$ 置換 $x^n-a$ 的根 ⇒ 存在 $n$ 次單位根 $\zeta_\sigma$ 使 $\sigma(\sqrt[n]a) = \zeta_\sigma\sqrt[n]a$。
- 映射 $\psi:\sigma\mapsto\zeta_\sigma$，從 Galois 群到 $\mu_n\subseteq F$。**同態**[▶ 08:00](https://youtu.be/Yc2ngBwDZVk?t=480)：
$$\sigma\tau(\sqrt[n]a) = \sigma(\zeta_\tau\sqrt[n]a) = \zeta_\tau\sigma(\sqrt[n]a) = \zeta_\tau\zeta_\sigma\sqrt[n]a\ ⇒\ \zeta_{\sigma\tau} = \zeta_\sigma\zeta_\tau.$$
  （$\zeta_\tau\in F$ 被 $\sigma$ 固定，所以**拉出來**。）
- **核** = 固定 $\sqrt[n]a$ 的自同構 = 只有恆等 ⇒ 單射 ⇒ Galois 群同構於 $\mu_n$ 的子群。
- 【課堂討論】[▶ 09:30](https://youtu.be/Yc2ngBwDZVk?t=570)「由什麼定理，群的階整除……？」「**Lagrange**。」⇒ $|\mathrm{Gal}|$ 整除 $n$。$\mu_n$ 循環，**循環群的子群是循環的** ⇒ 「**遊戲結束，夥計（man）**——我是說，女士們。」（學生：「你想**政治正確**。」「你**不夠男人**來配我。」「確實不夠。」）$\blacksquare$

---

## 3. Lagrange 預解式；循環 ⇒ 根式（Prop 37）

> **定義**（講義 p.3）[▶ 10:00](https://youtu.be/Yc2ngBwDZVk?t=600)　$K/F$ 循環、$n$ 次，$\mathrm{ch}F\nmid n$、$\mu_n\subseteq F$，$\sigma$ 生成 $\mathrm{Gal}(K/F)$。對 $\alpha\in K$、$\zeta\in\mu_n$，**Lagrange 預解式**：
> $$(\alpha,\zeta) = \alpha+\zeta\sigma(\alpha)+\zeta^2\sigma^2(\alpha)+\cdots+\zeta^{n-1}\sigma^{n-1}(\alpha).$$

「這像某種……多項式？**到底是什麼**？我不知道，反正叫 Lagrange 預解式。D&F 介紹它，你會想『這是什麼？』但它**有用途**。」

**計算**[▶ 11:00](https://youtu.be/Yc2ngBwDZVk?t=660)（$\zeta\in F$ 被 $\sigma$ 固定；$\sigma^n = 1$；$\zeta^n = 1$ ⇒ $\zeta^{n-1} = \zeta^{-1}$）：
$$\sigma(\alpha,\zeta) = \sigma\alpha+\zeta\sigma^2\alpha+\cdots+\zeta^{n-2}\sigma^{n-1}\alpha+\zeta^{-1}\alpha = \zeta^{-1}(\alpha,\zeta).$$
「**最後的成了第一**。」
- ⇒ $\sigma\left((\alpha,\zeta)^n\right) = \zeta^{-n}(\alpha,\zeta)^n = (\alpha,\zeta)^n$ ⇒ **$(\alpha,\zeta)^n\in F$**。（老師先說「預解式在 $F$ 裡」，自己改正：「是它的 **$n$ 次方**在 $F$ 裡。」）
- 【講義補充】用自同構 $1,\sigma,\dots,\sigma^{n-1}$ 的**線性獨立**（「特徵標那套，我之前帶過，這裡沒法講細節。**Sorry**——用 Tucker Carlson 說 sorry 的語氣」）可取 $\alpha$ 使 $(\alpha,\zeta)\neq0$（$\zeta$ 取本原根）。則 $\sigma^j(\alpha,\zeta) = \zeta^{-j}(\alpha,\zeta)$，$j<n$ 時**不固定** ⇒ $(\alpha,\zeta)$ 不在任何真子體 ⇒ $K = F((\alpha,\zeta))$，而 $(\alpha,\zeta)^n = a\in F$ ⇒ $K = F(\sqrt[n]a)$。

> **命題 37**（講義 p.4）[▶ 16:00](https://youtu.be/Yc2ngBwDZVk?t=960)　$\mathrm{ch}F\nmid n$、$\mu_n\subseteq F$ 時，任何 $n$ 次循環擴張都是 $F(\sqrt[n]a)$（某個 $a\in F$）的形式。

- 【口頭】[▶ 15:00](https://youtu.be/Yc2ngBwDZVk?t=900)「Lagrange 預解式是**計算 $n$ 次根**的方法。如果你覺得這很厲害——我也是。我想 **Lagrange 花了幾十年**發明它，這是讓人們相信五次方程**不能解**的機器的一部分。」（學生：「幾十年比 Galois 的一生還長。」「他活到 21 還是 20？」）
- 「所以兩個方向都對：單根式擴張 ⇒ 循環；循環 ⇒ 用 Lagrange 預解式造出 $n$ 次根 ⇒ 單根式擴張。」

---

## 4. 群的指數；Kummer 理論

> **定義**（講義 p.4）[▶ 17:00](https://youtu.be/Yc2ngBwDZVk?t=1020)　若 $g^n = 1$ 對所有 $g\in G$，說 $G$ 的**指數**是 $n$。

【口頭】「你們在 421 講過群的指數嗎？我是很久以前教數論時**發現**它的。」
- **RSA 故事**[▶ 17:30](https://youtu.be/Yc2ngBwDZVk?t=1050)：「講 RSA 加密，給學生一個指數讓他們加密訊息，我離開 10 分鐘，回來問加密後的訊息——他們給我的**就是原訊息**。『你們有照演算法做嗎？』『有，它就**什麼都沒做**。』」原來那個群（模某數的單位群，不是循環群，而是循環群的直積）的指數比我給的數小，而且剛好讓 $g^{151} = g^{50}g^{50}g^{50}g = g$。「我以為群的**階**夠大就安全——但指數可以比階小。」
- **例**[▶ 19:30](https://youtu.be/Yc2ngBwDZVk?t=1170)：$U(\mathbb{Z}_{11}\times\mathbb{Z}_7)\cong\mathbb{Z}_{10}\times\mathbb{Z}_6$，60 個元素，但指數是 **30**（$\mathrm{lcm}(10,6)$）。（「你們不知道？**可惡**，我很確定是這樣。」）
- 【口頭】「群的階**一定**是一個指數（421 證過 $g^{|G|} = e$），但那**不是有趣的**部分。D&F 這節**沒說『最小』**，所以我不確定它要求最小——我想是最小的。」（學生 Shane 追問：「我**故意避開**這個問題，Shane。謝謝。」）

【講義補充】（講義 p.4，D&F p.626）$K = F(\sqrt[n]{a_1},\dots,\sqrt[n]{a_k})$ 是 Abel 擴張、Galois 群指數 $n$。令 $(F^\times)^n = \{a^n\}$，$F^\times/(F^\times)^n$ 是指數 $n$ 的 Abel 群。**宣稱**：$\mathrm{Gal}(K/F)$ 同構於 $F^\times/(F^\times)^n$ 中由 $a_1,\dots,a_k$ 生成的子群；兩個這種擴張相等 $\iff$ 對應子群相等。所以 $F^\times/(F^\times)^n$ 的有限生成子群**分類**了指數 $n$ 的 Abel 擴張。這和前面的命題合稱 **Kummer 理論**——「翻過去看，**很嚇人**，超出我的專長。」

---

## 5. 根式擴張；Gauss 的正 17 邊形

[▶ 24:00](https://youtu.be/Yc2ngBwDZVk?t=1440)「現在專注在**特徵 0**。」

> **定義**（講義 p.5）
> 1. 在 $F$ 上代數的 $\alpha$ **可用根式表示**（可根式解出），若 $\alpha\in K$，而 $K$ 由一連串**單根式擴張**得到：
> $$F = K_0\subset K_1\subset\cdots\subset K_s = K,\qquad K_{i+1} = K_i(\sqrt[n_i]{a_i}),\ a_i\in K_i.$$
> 這種 $K$ 叫 $F$ 的**根式擴張**（root extension）。
> 2. 多項式 $f(x)\in F[x]$ 的所有根都能用根式解出，就說 $f$ **可用根式解**（solved by radicals）。

- 「每一步都是根式擴張——每次加入上一步某東西的 $n_i$ 次根。你也可以用 Lagrange 預解式造它們——我不會做，那東西**太野獸了**。」
- [▶ 25:30](https://youtu.be/Yc2ngBwDZVk?t=1530)「**Lagrange 解不了**、**Abel 證明不可能**、**Galois 也證明不可能**的問題，正是 $f$ 能不能用根式解。能的話，根就有用**係數的算術公式**表達的式子。」

**例 3：正 17 邊形**（講義 p.5，D&F §14.5）[▶ 26:30](https://youtu.be/Yc2ngBwDZVk?t=1590)
$$K_1 = \mathbb{Q}(\sqrt{17}),\ K_2 = K_1\left(\sqrt{2(17-\sqrt{17})}\right),\ K_3 = K_2\left(\sqrt{2(17+\sqrt{17})}\right),\ K_4 = K_3(\sqrt{a_3}),$$
$a_3 = 17+3\sqrt{17}-\sqrt{2(17-\sqrt{17})}-2\sqrt{2(17+\sqrt{17})}$——「這個**怪物**」。
- 【課堂討論】「你們幾歲？」「……」「**Gauss** 做這個時 **19 歲**（1796）。」學生：「然後他死了？」「不不，那是 Galois。Gauss 活到**高壽**，是個**脾氣暴躁**的老頭——一般共識是這樣。」
- 次數 2、4、8、16 的子體——「記得那個講了 3 分鐘的定理：尺規作圖對應 **$2^k$ 次**擴張。」這早於 Galois 二三十年——「所以你看得出 Galois 為什麼做那些事：**這些東西在水裡**，大家都在玩這種遊戲。這是個**很古老**、一直沒解決的歐氏幾何問題，Gauss 解了。」

> **引理 38**（講義 p.6）[▶ 28:30](https://youtu.be/Yc2ngBwDZVk?t=1710)　$\alpha$ 在某個根式擴張 $K$ 裡 ⇒ $\alpha$ 在某個**在 $F$ 上 Galois**、且每一步 $K_{i+1}/K_i$ 都**循環**的根式擴張裡。

（老師不證。）【講義補充】證明（講義 p.6，D&F p.628）：取 $K$ 的 **Galois 閉包** $L$；每個 $\sigma(K)$ 也是根式擴張，根式擴張的合成還是根式擴張 ⇒ $L$（所有 $\sigma(K)$ 的合成）是根式擴張且 Galois。再把需要的 $n_i$ 次單位根都加進基體得 $F'$，鏈 $F\subseteq F'\subset F'K_1\subset\cdots\subset F'K$ 每步都循環。

---

## 6. 可根式解 ⟺ Galois 群可解（Thm 39）

[▶ 30:00](https://youtu.be/Yc2ngBwDZVk?t=1800)（改黑板。學生：「太亮了。」）

> **定義（可解群）**[▶ 30:30](https://youtu.be/Yc2ngBwDZVk?t=1830)　有限群 $G$ **可解**：存在子群鏈
> $$1 = G_s\le G_{s-1}\le\cdots\le G_1\le G_0 = G,$$
> 使每個 $G_i/G_{i+1}$ 是**循環**群。

- 【課堂討論】「商要什麼條件？」學生：「循環。」「對——**你們證過**的那題。我出那題就是要讓你們在今天之前**至少知道**可解的定義。」（「那提醒我**要改你們的作業**了。」學生：「Violet 太好心了。」「也許讓 **Shane 改**。」）
- **事實**：可解群的**子群**可解；$H\trianglelefteq G$ 時，$G/H$ 和 $H$ 都可解 ⇒ $G$ 可解（作業題）。「其實是**當且僅當**，但另一方向**太技術**，我替你們拿掉了。」

💬 定義裡還要求每個 $G_{i+1}$ 是 $G_i$ 的**正規**子群（$G_{i+1}\trianglelefteq G_i$），否則商 $G_i/G_{i+1}$ 不是群。

> **定理 39（Galois）**[▶ 33:30](https://youtu.be/Yc2ngBwDZVk?t=2010)　（特徵 0）多項式 $f(x)$ **可用根式解** $\iff$ 它的 **Galois 群可解**。

「D&F 說『現在證明 Galois 關於**用根式解多項式根**與**多項式 Galois 群**的根本連結』。我們在特徵 0；證明也適用很多其他情形，**我不在乎**。抱歉，我該更在乎別的特徵——但我**死忠特徵 0**。」學生：「**保持真實**。」「我喜歡保持真實——或至少**有理**。其實我也不反對複數。」

- 【口頭】[▶ 34:30](https://youtu.be/Yc2ngBwDZVk?t=2070)「模糊地你已經能體會為什麼：根式擴張給出循環 Galois 群；一步步擴張，每一步相對上一步都是循環的——**拼起來應該行得通**。但那不是證明。而『$f$ 可用根式解』**正是**我們開學時問的問題：能不能用基體的根號寫出根的公式？」

**證明概要**[▶ 35:30](https://youtu.be/Yc2ngBwDZVk?t=2130)（照 D&F 唸）
- **(⇒)** $f$ 可根式解 ⇒ 每個根在引理 38 那樣的擴張裡；合成 $L$ 還是同類（Prop 21）。$G_i$ 對應子體 $K_i$，$\mathrm{Gal}(K_{i+1}/K_i) = G_i/G_{i+1}$ 循環 ⇒ $G = \mathrm{Gal}(L/F)$ 可解。$L$ 含 $f$ 的分裂體 ⇒ $f$ 的 Galois 群是 $G$ 的**商群** ⇒ 可解。
  - 「抱歉，這證明跟前兩個命題**真正交織**，我腦子裡**放不下全部**。」
- **(⇐)** $f$ 的 Galois 群 $G$ 可解，$K$ 是分裂體。由 Galois 對應，子群鏈 $1 = G_s\le\cdots\le G_0 = G$ 給出子體鏈
$$F = K_0\subset K_1\subset\cdots\subset K_s = K,$$
  （包含反轉）每步 $K_{i+1}/K_i$ 是 $n_i$ 次**循環**擴張。「還不能說是根式擴張——需要 $n$ 次單位根**在裡面**，否則就壞了。下一步是**把單位根合成進去**，之後每一步就是根式擴張（Prop 37）。以我給的細節程度，這大概跟我寫下來一樣好。」

---

## 7. 一般五次方程不可根式解

> **推論 40**[▶ 48:00](https://youtu.be/Yc2ngBwDZVk?t=2880)　一般的 $n$ 次方程 $f(x) = 0$，**$n\ge5$ 時不能用根式解**。

- 【課堂討論】[▶ 48:30](https://youtu.be/Yc2ngBwDZVk?t=2910)「上次證了什麼？」「一般多項式的 Galois 群是**對稱群** $S_n$。」（[[28-L24-多項式的Galois群]]）
- **$S_n$ 在 $n\ge5$ 不可解**[▶ 49:30](https://youtu.be/Yc2ngBwDZVk?t=2970)：「這在**第 4 章**——中級群論，我在這門課沒逼你們那麼緊。原諒我，**總得留點東西給研究所**。」
  - **定理 24**：$A_n$ 是**單群**（$n\ge5$）。【課堂討論】「單群是什麼意思？」學生：「只有平凡的正規子群。」「對——**沒有有趣的商群**，只有 $\{e\}$ 和 $A_n$。關於群本身，商群給不了任何資訊。但**可解群正是靠商群**帶有群的非平凡資訊——**相反**的東西。」
  - [▶ 52:30](https://youtu.be/Yc2ngBwDZVk?t=3150)「$S_n$ 的正規子群？我記得的定理：指標是整除群階的**最小質數**時子群正規。$|S_n|$ 最小的質因數是 2 ⇒ 你**唯一的希望**是指標 2 的子群——只有一個，**交錯群** $A_n$（偶置換）。但 $A_n$ 在 $n\ge5$ **也是單群**。」
  - 「回第 4 章可以找到剩下的故事——**不完全平凡**，但沒比我現在講的遠多少。$S_5$ 不可解，$n = 6,7,\dots$ **也不會變好**。」

💬 老師「唯一的希望是指標 2」的推理不嚴格——那個定理只說指標是最小質數時**必定**正規，並沒說其他指標的子群不可能正規（例如 $S_4$ 的 $V_4$ 指標 6 卻正規）。正確的事實是：$n\ge5$ 時 $S_n$ 的正規子群只有 $1$、$A_n$、$S_n$。所以任何合成鏈都要經過 $A_n/1 = A_n$，它是**非 Abel 單群**、不是循環群 ⇒ $S_n$ 不可解。

**明確的例子**[▶ 55:00](https://youtu.be/Yc2ngBwDZVk?t=3300)：
$$f(x) = x^5-6x+3\in\mathbb{Q}[x].$$
可以論證它的 Galois 群含一個 **5-循環**和一個**對換** ⇒ 同構於 $S_5$ ⇒ **不能用根式解**。「這是一個**明確**的五次多項式，不能用根式解。」

【講義補充】（D&F 的論證）Eisenstein（$p = 3$）⇒ 不可約 ⇒ 5 整除 $|G|$ ⇒ 由 Cauchy 定理有 5-循環；它恰有 3 個實根（導數 $5x^4-6$ 兩個實臨界點，變號三次），所以**複數共軛**交換兩個虛根、固定三個實根 ⇒ 是一個對換。$S_5$ 由一個 5-循環和一個對換生成。

- [▶ 56:00](https://youtu.be/Yc2ngBwDZVk?t=3360)「這之後 D&F 回去用 Galois 群**推導 Cardano 公式**，還有二次公式、四次……」學生：「我們花在 **Cardano** 上的時間已經夠了。」「我們這學期在 Cardano 上**已經花夠了**——沒必要**重新揭開那道傷口**。」學生：「我會說**太多了**。」「**太多了**，是。」

---

## 8. 微分 Galois 理論

[▶ 57:00](https://youtu.be/Yc2ngBwDZVk?t=3420)「這差不多就是多項式 Galois 理論的**結尾**。但 Galois 理論是**更一般**的想法：解**某種東西**——例如**微分方程**——都有對應的 Galois 理論。」
- 「你們問過：一個積分能不能用**初等函數**解出來？」學生：「$e^{x^2}$。」「對，$\int e^{x^2}dx$ 不能用初等函數表示。那『初等函數』是什麼意思？它扮演的角色**類似根式擴張**：在基本的體裡加入初等函數，能不能解這個微分方程？這就是**微分 Galois 理論**玩的遊戲，有**微分 Galois 群**，是一整套東西。」
- 「我弟弟帶過一個大學部的**特別主題**小組（大概四個人，每週見一次），他有份四頁的 PDF 講得**很精簡**——我**找不到**了。比這個**更技術**，因為還牽涉**微積分**。」
- 【口頭】[▶ 59:30](https://youtu.be/Yc2ngBwDZVk?t=3570)「我只想告訴你們：**看自同構**、看某種**保持結構的群**——這不只是這裡的事，而是一個在抽象數學裡**持續延伸**、超過我們所到之處的主題。」

---

## 9. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| 循環擴張 | Galois 且 Galois 群循環 |
| **Prop 36**：$\mu_n\subseteq F$ ⇒ $F(\sqrt[n]a)/F$ 循環、次數整除 $n$ | $\sigma\mapsto\zeta_\sigma$ 是單射同態到 $\mu_n$ |
| Lagrange 預解式 $(\alpha,\zeta) = \sum\zeta^i\sigma^i\alpha$ | $\sigma(\alpha,\zeta) = \zeta^{-1}(\alpha,\zeta)$ ⇒ $(\alpha,\zeta)^n\in F$ |
| **Prop 37**：循環 ⇒ $F(\sqrt[n]a)$ | 預解式造出 $n$ 次根 |
| 群的指數 | $\mathbb{Z}_{10}\times\mathbb{Z}_6$ 指數 30 |
| Kummer 理論 | $F^\times/(F^\times)^n$ 的子群分類指數 $n$ 的 Abel 擴張 |
| 根式擴張 | $K_{i+1} = K_i(\sqrt[n_i]{a_i})$ |
| 正 17 邊形 | 2、4、8、16 次的平方根鏈（Gauss 19 歲） |
| **Thm 39**：可根式解 ⟺ Galois 群可解 | 根式鏈 ↔ 子群鏈（商循環） |
| **Cor 40**：一般 $n\ge5$ 次不可根式解 | Galois 群 $S_n$，$A_n$ 單群 |
| $x^5-6x+3$ 不可根式解 | 5-循環 + 對換 ⇒ $S_5$ |

| 中文 | English |
|---|---|
| 循環擴張 | cyclic extension |
| 單根式擴張；根式擴張 | simple radical extension; root extension |
| 可用根式解 | solvable by radicals |
| Lagrange 預解式 | Lagrange resolvent |
| 群的指數 | exponent of a group |
| Kummer 理論 | Kummer theory |
| 可解群 | solvable group |
| 單群；交錯群 | simple group; alternating group |
| Galois 閉包 | Galois closure |
| 微分 Galois 理論 | differential Galois theory |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **Galois 理論結束，進入模論** | [[30-L26-模]] |
| **開學時的 Cardano、對稱函數** | [[01-L1-群論起源與等距變換]] |
| **可解群（中級群論）** | [[04-L3-同構定理與中階群論概覽]] |

---

## 附：本集一句話總結

> **基體含 $n$ 次單位根時，加入一個 $n$ 次根得到循環擴張（Galois 群嵌入 $\mu_n$）；反過來，Lagrange 預解式 $(\alpha,\zeta)$ 的 $n$ 次方落在基體，於是每個循環擴張都是單根式擴張；把根式擴張定義成一連串單根式擴張（Gauss 19 歲用四層平方根造出正 17 邊形），就得到 Galois 的定理：特徵 0 下多項式可用根式解 ⟺ 它的 Galois 群可解；而一般 $n$ 次多項式的 Galois 群是 $S_n$，$n\ge5$ 時 $A_n$ 是非 Abel 單群、$S_n$ 不可解，所以一般五次以上方程沒有根式公式——$x^5-6x+3$ 就是明確的例子。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 25 錄影逐字稿（YouTube 自動字幕，59:47）與手寫講義 `Math422_Lecture25_GaloisConclusions.pdf`（依 Dummit & Foote §14.7）整理。*
