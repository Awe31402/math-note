---
course: Number Theory（2021 秋，線上錄影）
episode: 36
lecture: 2021-11-03 第 1 部
date: 2021-11-03
video: https://youtu.be/M9GwrboiER0
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.5（p. 147）：Definition 4.5.16、Theorem 4.5.17–4.5.18、Example 4.5.19；§4.6 Lecture 26（p. 148–152）：Definition 4.6.1、Example 4.6.2–4.6.7、Theorem 4.6.13、Example 4.6.14、4.6.16、Theorem 4.6.18（Eisenstein）、Example 4.6.19、Theorem 4.6.20
---

# 第 36 集 · 主理想整環、多項式的分解、Eisenstein 判別法（上）（PIDs, Factorization, Eisenstein, Part 1） [▶ 影片](https://youtu.be/M9GwrboiER0)

← 上一集：[35-polynomial-rings-factor-theorem](35-polynomial-rings-factor-theorem.md) ｜ [總目錄](README.md) ｜ 下一集：[37-pids-factorization-eisenstein-2](37-pids-factorization-eisenstein-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 36 集（2021-11-03 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕；結尾被切斷）＋ 講者講義 §4.5–4.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 主理想整環（PID）](#1-主理想整環pid)
- [2. 體上的多項式環是 PID](#2-體上的多項式環是-pid)
- [3. 用它再證一次 R[x]/⟨x² + 1⟩ ≅ C](#3-用它再證一次-rxx--1--c)
- [4. 不可約多項式](#4-不可約多項式)
- [5. 例子：不可約要看在哪個環上](#5-例子不可約要看在哪個環上)
- [6. 2 次、3 次：可約 ⇔ 有根](#6-2-次3-次可約--有根)
- [7. 模 p 判別法](#7-模-p-判別法)
- [8. Eisenstein 判別法](#8-eisenstein-判別法)
- [9. 分圓多項式 Φ_p（開頭）](#9-分圓多項式-φ_p開頭)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:01](https://youtu.be/M9GwrboiER0?t=1)

講者先說講義 Example 4.5.15（p. 147）用 $n$ 次單位根分解多項式，「滿妙的」，可能出成作業，請大家自己讀；「但我得進入 PID 了」。

| 主題 | 時間 | 講義 |
|---|---|---|
| PID 定義 | 00:01 | Def 4.5.16 |
| $F[x]$ 是 PID | 01:22 | Thm 4.5.17–4.5.18 |
| $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$ | 14:01 | Ex 4.5.19 |
| 不可約 | 20:28 | Def 4.6.1 |
| 例子 | 23:54 | Ex 4.6.2–4.6.5 |
| 2、3 次 | 32:22 | Thm 4.6.6、Ex 4.6.7 |
| 模 $p$ 判別法 | 39:44 | Thm 4.6.13、Ex 4.6.14、4.6.16 |
| Eisenstein | 48:59 | Thm 4.6.18、Ex 4.6.19 |
| 分圓多項式 | 55:26 | Thm 4.6.20 |

> 【講義補充】Example 4.5.15（p. 147）：$\omega = e^{2\pi i/n}$ 是**本原 $n$ 次單位根**，$\omega^n = 1$ 而 $\omega^k\neq1$（$1\le k<n$），所以 $1,\omega,\dots,\omega^{n-1}$ 都是 $x^n = 1$ 的解：
> $$x^n-1 = (x-1)(x-\omega)(x-\omega^2)\cdots(x-\omega^{n-1}).$$
> 例：$x^4-1 = (x^2+1)(x^2-1) = (x+i)(x-i)(x-1)(x+1)$，$\omega_4 = i$。

---

## 1. 主理想整環（PID）

[▶ 00:01](https://youtu.be/M9GwrboiER0?t=1)

> **定義**（講義 Definition 4.5.16）：**主理想整環**（principal ideal domain，PID）是**每個理想都是主理想**的整環——每個理想都長成 $\langle a\rangle = \{ra : r\in R\}$。

（第 29 集講者問過：多個生成元的理想能不能寫成主理想？PID 就是「永遠能」的環。）

---

## 2. 體上的多項式環是 PID

[▶ 01:22](https://youtu.be/M9GwrboiER0?t=82)

> **定理**（講義 Theorem 4.5.17）：若 $F$ 是體，則 $F[x]$ 是 PID。

講者：「這種證明是**好考題**，不完全簡單，但很適合考。」

**證明**：

1. **$F[x]$ 是整環** [▶ 01:59](https://youtu.be/M9GwrboiER0?t=119)：$F$ 是整環，第 35 集證過整環上的多項式環是整環（首項係數相乘不為 0）。
2. 設 $I$ 是 $F[x]$ 的理想。若 $I = \{0\}$，$I = \langle 0\rangle$ 是主理想 [▶ 03:05](https://youtu.be/M9GwrboiER0?t=185)。
3. 若 $I\neq\{0\}$：$I$ 裡非零多項式的次數組成 $\mathbb{N}\cup\{0\}$ 的非空子集合（零多項式沒有次數，丟掉）。由**良序原理**，取次數最小的 $g(x)\in I$ [▶ 04:09](https://youtu.be/M9GwrboiER0?t=249)。
4. **$I\subseteq\langle g\rangle$**：任取 $f\in I$。**除法演算法**（第 35 集，要體）：$f = gq+r$，$r = 0$ 或 $\deg r<\deg g$。
5. $r = f-gq$ [▶ 06:23](https://youtu.be/M9GwrboiER0?t=383)：$f\in I$、$gq\in I$（超級封閉），所以 $r\in I$。
6. 若 $r\neq0$，它是 $I$ 裡次數比 $g$ 小的元素，跟 $g$ 次數最小矛盾 [▶ 06:53](https://youtu.be/M9GwrboiER0?t=413)。所以 $r = 0$，$f = gq\in\langle g\rangle$。
7. **$\langle g\rangle\subseteq I$** [▶ 08:25](https://youtu.be/M9GwrboiER0?t=505)：【課堂討論】講者問為什麼。答：$g\in I$，$I$ 是理想，$g$ 的多項式倍數都在 $I$ 裡（超級封閉）。
8. 所以 $I = \langle g\rangle$。每個理想都是主理想。∎

（講者特別說：$g$ 是「**一個**」次數最小的元素，不是「**唯一**的」，可能有好幾個。）

> **定理**（講義 Theorem 4.5.18）[▶ 12:33](https://youtu.be/M9GwrboiER0?t=753)：$F$ 是體，$I\neq\{0\}$ 是 $F[x]$ 的理想，$g\in F[x]$。則
> $$I = \langle g(x)\rangle\iff g\text{ 是 }I\text{ 裡次數最小的非零多項式}.$$

講者說這其實是上面證明的推論：**非零理想由它次數最小的元素生成**。

**不是體呢？** [▶ 10:10](https://youtu.be/M9GwrboiER0?t=610) 例如 $\mathbb{Z}_6[x]$：PID 的定義第一條就是整環，「這是行不通的起點」。講者也想了一下：不是整環也能談理想嗎？可以——第 29 集我們模過 $\mathbb{Z}_6$ 的偶數，商環的構造不要求原本的環是整環。「$\mathbb{Z}_6[x]$ 的理想長什麼樣？我其實不知道，得想想。只是拋出一個問題。」

---

## 3. 用它再證一次 R[x]/⟨x² + 1⟩ ≅ C

[▶ 14:01](https://youtu.be/M9GwrboiER0?t=841)（講義 Example 4.5.19，「非常好的應用」）

$$\varphi:\mathbb{R}[x]\to\mathbb{C},\qquad\varphi(f(x)) = f(i).$$
這是環同態（求值映射）。

1. **$x^2+1\in\ker\varphi$** [▶ 15:06](https://youtu.be/M9GwrboiER0?t=906)：$\varphi(x^2+1) = i^2+1 = 0$。
2. **它是核裡次數最小的嗎？** 若一次式 $ax+b$ 在核裡，$\varphi(ax+b) = ai+b = 0$。複數為 0 ⇔ 實部、虛部都是 0，所以 $a = b = 0$ [▶ 16:41](https://youtu.be/M9GwrboiER0?t=1001)。**核裡沒有一次式**。

   （講者叫錯名字時說「趴下做 20 下伏地挺身——抱歉，這對沒來的人很突兀」。）
3. 由 Theorem 4.5.18：$\ker\varphi = \langle x^2+1\rangle$。
4. **映成** [▶ 17:46](https://youtu.be/M9GwrboiER0?t=1066)：任取 $b+ai\in\mathbb{C}$，$\varphi(ax+b) = ai+b$。
5. **第一同構定理**：
   $$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}.$$

講者 [▶ 19:58](https://youtu.be/M9GwrboiER0?t=1198)：「我寫了很多，但真的研究它的邏輯，幾秒鐘就能在腦中總結。很直接的證明，跟這裡很多證明一樣，**最終都靠除法演算法**。」

（這是第三次證明這件事：第 29–30 集直接算、第 31 集用極大理想、這次用第一同構定理。）

---

## 4. 不可約多項式

[▶ 20:28](https://youtu.be/M9GwrboiER0?t=1228)

講者：「這就是我舊的 Lecture 25 的結尾，現在是 Lecture 26，**全部在講因式分解**。你們很早就知道因式分解——FOIL。我們要升一級。」

> **定義**（講義 Definition 4.6.1）：$D$ 是整環。$f(x)\in D[x]$ 不是 0 也不是單位。若每當 $f = gh$（$g,h\in D[x]$），$g$ 或 $h$ 就是 $D[x]$ 的**單位**，就說 $f$ 在 $D$ 上**不可約**（irreducible over $D$）。不是 0、不是單位、也不是不可約的，叫**可約**（reducible）。

（講者：「這是我最後一次寫出 irreducible，以後都寫 irred。」）

講者 [▶ 23:23](https://youtu.be/M9GwrboiER0?t=1403)：這跟以前學的差不遠吧？以前可能說「質多項式」——「我們之後會區分這兩個詞，注意」。（第 38–39 集：不可約 vs 質。）

> 【講義補充】講義（p. 148）開玩笑：「換句話說，如果一個多項式不是不不可約的，它就是可約的。」

---

## 5. 例子：不可約要看在哪個環上

[▶ 24:24](https://youtu.be/M9GwrboiER0?t=1464)

**$x^2+1$**（Ex 4.6.2）：

- 在 $\mathbb{R}$ 上不可約。
- 在 $\mathbb{C}$ 上可約：$x^2+1 = (x+i)(x-i)$。

講者：「不可約要看**你從哪裡拿多項式**、允許什麼當因式。只研究實多項式的分解，就**禁止**用 $\pm i$。」

**體上的多項式環的單位** [▶ 25:57](https://youtu.be/M9GwrboiER0?t=1557)：$f(x)g(x) = 1$ 只能是 $a_0b_0 = 1$、其他係數都是 0。所以**單位就是非零常數**。

- 所以要說 $x+i$ 不可約，先要知道它**不是單位**：它不是常數，所以不是。
- 「**認清你的敵人**」：體上的多項式，非常數就不是單位。

> 【講義補充】講義 Example 4.6.3（p. 148）：$2x+4 = 2(x+2)$ 在 $\mathbb{Z}$ 上**可約**，因為 $2$ 在 $\mathbb{Z}$ 裡**不是單位**；在 $\mathbb{Q}$ 或 $\mathbb{R}$ 上**不可約**，因為 $2$ 是單位。「重點是脈絡很重要。」

**$x^2-7$**（Ex 4.6.4）[▶ 27:28](https://youtu.be/M9GwrboiER0?t=1648)：

- $x^2-7 = (x-\sqrt7)(x+\sqrt7)$，所以在 $\mathbb{R}$（和 $\mathbb{C}$）上可約。
- 在 $\mathbb{Q}$ 上**不可約**：只用有理係數沒辦法這樣分解，$\sqrt7$ 是無理數（第 5 集）。

**$x^2+1$ 在 $\mathbb{Z}_3$ 和 $\mathbb{Z}_5$**（Ex 4.6.5）[▶ 29:05](https://youtu.be/M9GwrboiER0?t=1745)：

- $\mathbb{Z}_3$：$f(0) = 1$、$f(1) = 2$、$f(2) = 5\equiv 2$。**沒有一次因式**，所以不可約（下一節的定理）。
- $\mathbb{Z}_5$：$f(2) = 5\equiv 0$，所以 $x-2$ 是因式。

**講者的巧招** [▶ 31:14](https://youtu.be/M9GwrboiER0?t=1874)：「有時候走點旁門比較好。」模 5 可以減 5：
$$x^2+1 = x^2-4 = (x-2)(x+2)\quad\text{在 }\mathbb{Z}_5[x].$$
平方差。乘開 $-2x$ 和 $+2x$ 抵消。**可約**。

> 【講義補充】Example 4.6.5（p. 148）用的是「無聊但有系統」的方法：設 $x^2+1 = (x-2)(x+a) = x^2+(a-2)x-2a$，比較係數得 $a-2 = 0$、$-2a = 1$，$a = 2$ 同時滿足（$-4\equiv1\ (\mathrm{mod}\ 5)$）。
>
> 以下**不是逐字稿內容**：這跟第 20 集對得上——$x^2\equiv-1$ 模 5 有解（$5\equiv1\ (\mathrm{mod}\ 4)$），模 3 無解（$3\equiv3\ (\mathrm{mod}\ 4)$）。

---

## 6. 2 次、3 次：可約 ⇔ 有根

[▶ 32:22](https://youtu.be/M9GwrboiER0?t=1942)

講者：「**很重要，不要過度延伸這個定理**。很容易過度延伸，我自己就被搞糊塗過。」

> **定理**（講義 Theorem 4.6.6）：$F$ 是體，$f\in F[x]$，$\deg f = 2$ 或 $3$。則
> $$f\ \text{在 }F\text{ 上可約}\iff f\ \text{在 }F\text{ 裡有根}.$$

**證明** [▶ 35:31](https://youtu.be/M9GwrboiER0?t=2131)：

- 可約 = 分解成兩個非單位（非常數）的乘積。2 次只能「1 次 × 1 次」；3 次只能「1 次 × 2 次」。**都有一次因式**。
- 由**因式定理**（第 35 集），$x-a$ 是因式 ⇔ $f(a) = 0$。

**警世故事：4 次就不行**（Ex 4.6.7）[▶ 36:39](https://youtu.be/M9GwrboiER0?t=2199)：
$$f(x) = x^4+14x^2+49 = (x^2+7)^2\in\mathbb{R}[x].$$

- 沒有實根：$x^2+7>0$。
- 但**可約**：$x^2+7$ 不是單位。
- （$x^2+7$ 本身在 $\mathbb{R}$ 上不可約：2 次、沒有實根。）

講者：「到 4 次就可能分成 2 次 × 2 次，不能再靠一次因式透過因式定理得到根。」

---

## 7. 模 p 判別法

[▶ 39:44](https://youtu.be/M9GwrboiER0?t=2384)

講者說要跳過講義 p. 149–151 的**本原多項式**（primitive polynomial）理論——用來研究整係數多項式的不可約性，「我現在對它沒那麼有興趣，講了會讓我趕著講想慢慢講的東西」，請大家自己讀。他「偷那節的主要定理，不證明」：

> **定理**（講義 Theorem 4.6.13）[▶ 41:16](https://youtu.be/M9GwrboiER0?t=2476)：$p$ 是質數，$f(x)\in\mathbb{Z}[x]$，$\deg f\ge1$。$\bar f(x)\in\mathbb{Z}_p[x]$ 是把 $f$ 的係數模 $p$ 得到的多項式。若
> - $\bar f$ 在 $\mathbb{Z}_p$ 上不可約，而且
> - $\deg\bar f = \deg f$，
>
> 則 $f$ 在 $\mathbb{Q}$ 上不可約。

（講者說作業早就有類似的設定：把整係數多項式換成 $\mathbb{Z}_n$ 係數。）

**例子**（Ex 4.6.14）[▶ 44:04](https://youtu.be/M9GwrboiER0?t=2644)：$f(x) = 29x^3+5x^2+2x+1$。

1. 模 2：$\bar f(x) = x^3+x^2+1$。
2. 3 次，用第 6 節：只要檢查有沒有根。$\bar f(0) = 1$，$\bar f(1) = 1+1+1 = 1$。**沒有根**，所以 $\bar f$ 在 $\mathbb{Z}_2$ 上不可約。
3. $\deg\bar f = \deg f = 3$。
4. 所以 **$f$ 在 $\mathbb{Q}$ 上不可約**。

講者：「這非常好，因為直接證它在有理數上不可約，不是你想試的事。」

【課堂討論】[▶ 46:09](https://youtu.be/M9GwrboiER0?t=2769) 講者問：你猜這套把戲是誰的？學生猜 Euler、Euclid、Lagrange、Gauss。講者：「**Gauss**。至少 Gauss 發現了它，別人大概也發現過。」

**警世故事**（Ex 4.6.16）[▶ 46:42](https://youtu.be/M9GwrboiER0?t=2802)：$f(x) = x^4+1$。

- 對**每個**質數 $p$，$\bar f$ 在 $\mathbb{Z}_p[x]$ 裡都**可約**。
- 但 $f$ 在 $\mathbb{Q}$ 上**不可約**。

講者：這個判別法「有用的時候有用」；對所有質數都失敗，**不能**推出可約。「指派這題給抽象代數學生的話，願他們安息。我覺得這可能是我出過最難的抽象代數題，就是很血腥。但是好練習，做完真的學到很多。」

> 【講義補充】講義（p. 150–151）：
> - **Example 4.6.15**：$21x^3-3x^2+2x+8$ 模 2 是 $x^2(x+1)$（可約，沒結論）；改用模 5：$x^3+2x^2+2x+3$ 在 $0,1,2,3,4$ 的值是 $3,3,3,-1,2$，都不是 0，所以模 5 不可約，原多項式在 $\mathbb{Q}$ 上不可約。**換個質數可能就成功。**
> - Theorem 4.6.13 只能**肯定**在 $\mathbb{Q}$ 上不可約，**不能否定**。
> - **Example 4.6.17**：有理係數的多項式乘上分母的公倍數，就變成整係數，可以用這些工具。講義用模 2 檢查了 4 次多項式 $x^4+x+1$：沒有一次因式，2 次因式只可能是 $x^2+x+1$，比較係數得到矛盾，所以不可約。
> - 本原多項式的主要定理（Theorem 4.6.11，Gallian 叫 **Gauss 引理**）：**整係數多項式若在 $\mathbb{Q}$ 上可約，則在 $\mathbb{Z}$ 上也可約**。例：$6x^2+19x-7 = 6(x+\frac72)(x-\frac13) = (2x+7)(3x-1)$。講義說「Gauss 引理這名字跟 Gauss 的工作比起來不太有描述性」。

---

## 8. Eisenstein 判別法

[▶ 48:59](https://youtu.be/M9GwrboiER0?t=2939)

講者說這個也不證，但會用。

> **Eisenstein 判別法**（講義 Theorem 4.6.18）：$f(x) = a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0\in\mathbb{Z}[x]$。若存在質數 $p$ 使
> - $p\nmid a_n$（不整除首項係數），
> - $p\mid a_j$ 對 $j = n-1,\dots,0$（整除其他所有係數），
> - $p^2\nmid a_0$（$p^2$ 不整除常數項），
>
> 則 $f$ 在 $\mathbb{Q}$ 上不可約。

**注意**：講者在課堂上陳述時**漏了第三個條件** $p^2\nmid a_0$，他在第 39 集自己更正了（「我想我抄的時候漏了，那是很重要的條件」）。講義 Theorem 4.6.18（p. 151）有這一條，沒有它定理是錯的（例如 $x^2-4$：$p=2$ 滿足前兩條，但 $x^2-4 = (x-2)(x+2)$）。

【口頭】[▶ 50:33](https://youtu.be/M9GwrboiER0?t=3033) 這是「最基本的版本」。講者的哥哥正在抱怨不知道該在什麼一般性下陳述這個定理，因為它有更抽象的版本；「如果他寫了東西，我會轉給你們」。證明有很多種，「有些簡單，有些之後才簡單」。

**這是 GRE 數學科目考的好武器** [▶ 51:34](https://youtu.be/M9GwrboiER0?t=3094)：問「這個多項式不可約嗎？」就拿出它。要用它得**選一個質數**，「但通常看到多項式，該選的質數就會瞪著你」。

**例子**（Ex 4.6.19）[▶ 52:04](https://youtu.be/M9GwrboiER0?t=3124)：
$$f(x) = 13x^7+2x^6+4x^3+18x+2.$$

【課堂討論】要找 $p$：$p\nmid 13$，但 $p\mid 2,4,18,2$。學生：**$p = 2$**。（$2^2 = 4\nmid 2$。）所以由 Eisenstein，**$f$ 在 $\mathbb{Q}$ 上不可約**。「沒那麼糟吧？」

> 【講義補充】Example 4.6.19（p. 151）補充：係數為 0 的項也要被 $p$ 整除——沒問題，$p\mid0$ 永遠成立（$0 = p\cdot0$）。講義說 Eisenstein 的證明延到後面，因為「Gallian p. 321 Example 4 的論證比 p. 300 的反證法有趣得多」。

【口頭】[▶ 53:09](https://youtu.be/M9GwrboiER0?t=3189) 講者最喜歡的 YouTube 留言之一：他在抽象代數二講 **Galois 理論**——「大學抽象代數課的皇冠寶石，如果你到得了的話；很多學校覺得對大學生來說是徒勞」——那天有高中生來旁聽，所以他講了很多關於二次方程的「低階」東西。結果有人留言說他「很居高臨下，這些是抽象代數二的學生，不該當高中生講」。「可是那裡真的有個高中生。」

---

## 9. 分圓多項式 Φ_p（開頭）

[▶ 55:26](https://youtu.be/M9GwrboiER0?t=3326)

令 $S = 1+x+\cdots+x^{p-1}$。則 $xS = x+x^2+\cdots+x^p$，
$$xS-S = x^p-1.$$
（講者說講義這裡有個打字錯誤，結果應該是 $x^p-1$。）所以
$$(x-1)(1+x+\cdots+x^{p-1}) = x^p-1,\qquad 1+x+\cdots+x^{p-1} = \frac{x^p-1}{x-1}.$$

這個多項式叫**第 $p$ 個分圓多項式**（$p$-th cyclotomic polynomial）：
$$\Phi_p(x) = 1+x+\cdots+x^{p-1}.$$

> **定理**（講義 Theorem 4.6.20）：$p$ 是質數，則 $\Phi_p(x)$ 在 $\mathbb{Q}$ 上不可約。

**證明的巧招** [▶ 57:31](https://youtu.be/M9GwrboiER0?t=3451)：令 $f(x) = \Phi_p(x+1)$。由上面的公式，
$$f(x) = \frac{(x+1)^p-1}{(x+1)-1} = \frac1x\left[x^p+px^{p-1}+\binom p2x^{p-2}+\cdots+px+1-1\right]$$
（用**二項式定理**）。影片在這裡被切斷，接第 37 集。

> 【講義補充】Theorem 4.6.20 的證明（p. 152）：整理得
> $$f(x) = x^{p-1}+px^{p-2}+\cdots+p.$$
> 除了首項，每個係數 $\binom pk$（$1\le k\le p-1$）都被 $p$ 整除，常數項是 $p$、不被 $p^2$ 整除，所以由 **Eisenstein（$p$）**，$f$ 在 $\mathbb{Q}$ 上不可約。若 $\Phi_p = gh$ 可約，則 $f(x) = \Phi_p(x+1) = g(x+1)h(x+1)$ 也可約，矛盾。所以 $\Phi_p$ 不可約。
>
> （「分圓」：$\Phi_p$ 的根是 $p$ 次單位根 $\zeta,\zeta^2,\dots,\zeta^{p-1}$，把圓切成 $p$ 等份，見第 23 集。這一句**不是講義內容**。）

---

## 10. 一頁速查表

**PID**：每個理想都是主理想的整環。

**$F[x]$（$F$ 體）是 PID**。**關鍵一步**：取 $I$ 裡次數最小的 $g$；$f = gq+r$，$r = f-gq\in I$ 次數更小 ⇒ $r=0$。非零理想 $=\langle$ 次數最小的元素 $\rangle$。

**$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$**：$\varphi(f) = f(i)$ 映成；核沒有一次式 ⇒ $\ker\varphi = \langle x^2+1\rangle$。

**不可約**（整環 $D$ 上）：非零、非單位，任何分解都有一個因式是單位。體上多項式的單位 = 非零常數。

| 多項式 | 在哪裡不可約 | 在哪裡可約 |
|---|---|---|
| $x^2+1$ | $\mathbb{R},\mathbb{Q},\mathbb{Z}_3$ | $\mathbb{C}$、$\mathbb{Z}_5$（$=(x-2)(x+2)$） |
| $x^2-7$ | $\mathbb{Q}$ | $\mathbb{R}$ |
| $2x+4$ | $\mathbb{Q},\mathbb{R}$ | $\mathbb{Z}$（$2$ 不是單位） |
| $(x^2+7)^2$ | — | $\mathbb{R}$（但沒有實根） |

**判別工具**

| 工具 | 內容 |
|---|---|
| 2、3 次 | 可約 ⇔ 有根（4 次起不行） |
| 模 $p$ | $\bar f$ 在 $\mathbb{Z}_p$ 不可約且次數不降 ⇒ $f$ 在 $\mathbb{Q}$ 不可約（只能肯定，不能否定；$x^4+1$） |
| Eisenstein | $p\nmid a_n$、$p\mid a_j$（$j<n$）、$p^2\nmid a_0$ ⇒ 在 $\mathbb{Q}$ 不可約 |
| Gauss 引理 | 整係數在 $\mathbb{Q}$ 可約 ⇒ 在 $\mathbb{Z}$ 可約 |

**分圓多項式** $\Phi_p = 1+x+\cdots+x^{p-1} = \frac{x^p-1}{x-1}$ 在 $\mathbb{Q}$ 不可約。**關鍵一步**：$\Phi_p(x+1)$ 用 Eisenstein（$p$）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\Phi_p$ 證明收尾；$\langle p(x)\rangle$ 極大 ⇔ $p$ 不可約；$F[x]/\langle p\rangle$ 是體 | 第 37 集 |
| 不可約 vs 質；Euclid 整環、UFD | 第 38–39 集 |
| 不可約多項式 ⇒ 擴張體 | 第 40–43 集 |
| Galois 理論（講者提到的皇冠寶石） | 本課沒講 |

---

## 附：本集一句話總結

> **體上的多項式環是主理想整環：每個理想都由它次數最小的元素生成（靠除法演算法），由此第三次證明 $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$。多項式可不可約要看在哪個環上；判別工具有「2、3 次看有沒有根」「模 $p$ 不可約就在 $\mathbb{Q}$ 不可約」和 Eisenstein 判別法，後者證明了分圓多項式 $\Phi_p$ 不可約。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-03 第 1 部錄影逐字稿（YouTube 自動字幕，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.5–4.6 整理。*
