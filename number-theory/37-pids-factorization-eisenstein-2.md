---
course: Number Theory（2021 秋，線上錄影）
episode: 37
lecture: 2021-11-03 第 2 部
date: 2021-11-03
video: https://youtu.be/RO9oZWQILrY
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.6 Lecture 26（p. 152–153）：Theorem 4.6.20 證明、Theorem 4.6.21、Corollary 4.6.22–4.6.23、Example 4.6.24–4.6.25
---

# 第 37 集 · Φ_p 不可約、⟨p(x)⟩ 極大 ⇔ p(x) 不可約（PIDs, Factorization, Eisenstein, Part 2） [▶ 影片](https://youtu.be/RO9oZWQILrY)

← 上一集：[36-pids-factorization-eisenstein-1](36-pids-factorization-eisenstein-1.md) ｜ [總目錄](README.md) ｜ 下一集：[38-pids-euclidean-domains-ufds-1](38-pids-euclidean-domains-ufds-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 37 集（2021-11-03 第 2 部，接第 36 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（17:40，whisper 轉錄）＋ 講者講義 §4.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Φ_p 不可約（收尾）：平移技巧](#1-φ_p-不可約收尾平移技巧)
- [2. ⟨p(x)⟩ 是極大理想 ⇔ p(x) 不可約](#2-px-是極大理想--px-不可約)
  - [2.1 (⇒) 極大 ⇒ 不可約](#21--極大--不可約)
  - [2.2 (⇐) 不可約 ⇒ 極大（講義）](#22--不可約--極大講義)
- [3. 推論：F[x]/⟨p(x)⟩ 是體；不可約多項式像質數](#3-推論fxpx-是體不可約多項式像質數)
- [4. 例子：8 個元素的體、9 個元素的體](#4-例子8-個元素的體9-個元素的體)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

收尾第 36 集分圓多項式的證明，然後把**極大理想**（第 30–31 集）和**多項式分解**（第 36 集）連起來。講者：「這很令人興奮。」

（這部只講到定理 4.6.21 的前半，後半和推論講者說「下次前 10 分鐘」講完；下面依講義補上，標【講義補充】。）

---

## 1. Φ_p 不可約（收尾）：平移技巧

[▶ 00:00](https://youtu.be/RO9oZWQILrY?t=0)

接第 36 集：$f(x) = \Phi_p(x+1) = \dfrac{(x+1)^p-1}{x}$。

**二項式定理**：$(x+1)^p$ 的係數是 $\binom p0,\binom p1,\binom p2,\dots,\binom pp$。（講者一度用 $p=3$ 舉例：$\binom31,\binom32,\binom33,\binom30$，「我是白痴」。）

1 抵消後除以 $x$：
$$f(x) = x^{p-1}+p\,x^{p-2}+\cdots+p.$$

- 中間的係數 $\binom pk$（$1\le k\le p-1$）：「研究二項式係數的公式，它們都有因數 $p$。」
- $p$ 不整除首項係數 1。
- （常數項 $p$ 不被 $p^2$ 整除。）

由 **Eisenstein**，$\Phi_p(x+1)$ 在 $\mathbb{Q}$ 上不可約 [▶ 01:02](https://youtu.be/RO9oZWQILrY?t=62)。

**回到 $\Phi_p$** [▶ 01:32](https://youtu.be/RO9oZWQILrY?t=92)：假設 $\Phi_p(x) = g(x)h(x)$ 可約，則
$$\Phi_p(x+1) = g(x+1)\,h(x+1)$$
也可約，跟上面矛盾。所以 **$\Phi_p$ 不可約**。∎

講者：這是**平移技巧**（shifting trick）——把多項式平移，平移後的不可約，原本的也不可約。「很狡猾，但對這個有用。」

【Q&A】[▶ 02:33](https://youtu.be/RO9oZWQILrY?t=153) 學生問：是因為在 $\mathbb{Q}$ 上才行嗎？講者：不，「我想剛才的論證跟體無關，甚至在整環上可能都行」。

> 以下**不是逐字稿內容**，是補兩個講者帶過的地方：
> - **為什麼 $p\mid\binom pk$**：$\binom pk = \dfrac{p!}{k!(p-k)!}$，分子有因數 $p$；$1\le k\le p-1$ 時分母 $k!(p-k)!$ 的因數都小於 $p$，不含 $p$（$p$ 是質數）。所以 $p$ 留在分子裡。
> - **平移不改變次數**：$g(x+1)$ 跟 $g(x)$ 次數一樣，所以非平凡分解平移後還是非平凡的。這只用到 $x\mapsto x+1$ 是多項式環的自同構（反函數是 $x\mapsto x-1$），所以講者說「跟體無關」是對的。

---

## 2. ⟨p(x)⟩ 是極大理想 ⇔ p(x) 不可約

[▶ 03:04](https://youtu.be/RO9oZWQILrY?t=184)

> **定理**（講義 Theorem 4.6.21）：$F$ 是體，$p(x)\in F[x]$。則
> $$\langle p(x)\rangle\ \text{是 }F[x]\text{ 的極大理想}\iff p(x)\ \text{在 }F\text{ 上不可約}.$$

講者：「我們把之前的**極大理想**和現在的**多項式分解**連起來了。」

### 2.1 (⇒) 極大 ⇒ 不可約

[▶ 04:04](https://youtu.be/RO9oZWQILrY?t=244)

設 $\langle p\rangle$ 是極大理想。

1. **$p\neq 0$**，而且 **$p$ 不是常數** [▶ 05:05](https://youtu.be/RO9oZWQILrY?t=305)：極大理想的定義要求它不是整個環。若 $p = c$ 是非零常數，$\langle c\rangle$ 就是全部（常數倍可以湊出所有多項式）。
2. 設 $p = gh$ 是 $F$ 上的一個分解 [▶ 06:08](https://youtu.be/RO9oZWQILrY?t=368)。
3. **$\langle p\rangle\subseteq\langle g\rangle$**：若 $j\in\langle p\rangle$，$j = pk = g(hk)$，所以 $j\in\langle g\rangle$ [▶ 07:39](https://youtu.be/RO9oZWQILrY?t=459)。
4. 所以 $\langle p\rangle\subseteq\langle g\rangle\subseteq F[x]$。由**極大性**，$\langle g\rangle = \langle p\rangle$ 或 $\langle g\rangle = F[x]$ [▶ 08:12](https://youtu.be/RO9oZWQILrY?t=492)。

**情況一：$\langle g\rangle = \langle p\rangle$** [▶ 08:42](https://youtu.be/RO9oZWQILrY?t=522)：$g\in\langle p\rangle$，所以 $g = pq$。看次數 [▶ 13:58](https://youtu.be/RO9oZWQILrY?t=838)：

- $p = gh$ ⇒ $\deg p\ge\deg g$。
- $g = pq$ ⇒ $\deg g\ge\deg p$。

所以 $\deg g = \deg p$，於是 $\deg h = 0$，**$h$ 是非零常數——單位**。

**情況二：$\langle g\rangle = F[x]$** [▶ 15:39](https://youtu.be/RO9oZWQILrY?t=939)：$1\in\langle g\rangle$，存在 $a(x)$ 使 $a(x)g(x) = 1$，所以 **$g$ 是單位**（非零常數）。

兩種情況都有一個因式是單位，所以**每個分解都是平凡的**，$p$ 不可約。∎

【口頭】講者一開始假設分解是「非平凡的」想推出矛盾 [▶ 11:25](https://youtu.be/RO9oZWQILrY?t=685)，後來說「我寫的沒錯，只是沒切中要點」，改成不假設非平凡、直接說明每個分解都有單位（講義的寫法）。他也抱怨一直寫 $(x)$：「寫 $p,g,h$ 就簡單多了，$(x)$ 對論證沒有任何幫助，但我卡住了。」

講者 [▶ 16:43](https://youtu.be/RO9oZWQILrY?t=1003)：「後半證明下次再講，比較短。」他說**這個定理是好考題**，「我把它講得比實際難」。

### 2.2 (⇐) 不可約 ⇒ 極大（講義）

> 【講義補充】Theorem 4.6.21 (⇐) 的證明（p. 152）：設 $p$ 不可約，理想 $I$ 滿足 $\langle p\rangle\subseteq I\subseteq F[x]$。
> 1. **$F[x]$ 是 PID**（第 36 集），所以 $I = \langle g\rangle$。
> 2. $p\in\langle p\rangle\subseteq\langle g\rangle$，所以 $p = kg$。
> 3. $p$ 不可約，所以 $k$ 或 $g$ 是單位（次數 0）。
>    - $\deg k = 0$：$p$ 和 $g$ 差一個非零常數，$\langle p\rangle = \langle g\rangle = I$。
>    - $\deg g = 0$：$g$ 是單位，$I = \langle g\rangle = F[x]$。
> 4. 所以 $\langle p\rangle$ 是極大理想。∎
>
> **關鍵**：這個方向用到 **$F[x]$ 是 PID**——中間的理想一定是主理想，才能用不可約性。

---

## 3. 推論：F[x]/⟨p(x)⟩ 是體；不可約多項式像質數

> 【講義補充】
>
> **Corollary 4.6.22**（p. 152）：$F$ 是體，$p(x)$ 在 $F$ 上不可約，則
> $$F[x]/\langle p(x)\rangle\ \text{是體}.$$
> 證明：Theorem 4.6.21 ⇒ $\langle p\rangle$ 極大 ⇒ 由第 31 集 Theorem 4.3.7，商環是體。講義說「不可約多項式可以用來**造出新的體**」。
>
> **Corollary 4.6.23**（p. 153）：$F$ 是體，$p(x)$ 不可約。若 $p\mid ab$，則 $p\mid a$ 或 $p\mid b$。
> 證明：$\langle p\rangle$ 極大 ⇒ 質理想（第 31 集）。$ab\in\langle p\rangle$ ⇒ $a\in\langle p\rangle$ 或 $b\in\langle p\rangle$。
> 講義說：**這是證明 $\mathbb{Z}[x]$ 是唯一分解整環的關鍵，唯一性就來自這個定理。**（對照第 5 集整數的「$p\mid ab\Rightarrow p\mid a$ 或 $p\mid b$」、第 19 集高斯質數的 Lemma 6.5。）

---

## 4. 例子：8 個元素的體、9 個元素的體

> 【講義補充】
>
> **Example 4.6.24**（p. 153）：$x^3+x+1\in\mathbb{Z}_2[x]$。在 $x=0,1$ 的值都是 1（不是 0），3 次沒有根，所以**不可約**（第 36 集 Theorem 4.6.6）。所以
> $$\mathbb{Z}_2[x]/\langle x^3+x+1\rangle\ \text{是一個有 8 個元素的體}.$$
> 元素是 $a+bx+cx^2$（$a,b,c\in\mathbb{Z}_2$，$2^3 = 8$ 個），乘法照常、但用規則 $x^3 = -x-1 = x+1$。例如：
> $$x\cdot x^2 = x^3 = x+1,\qquad x^2\cdot x^2 = x\cdot x^3 = x(x+1) = x^2+x,$$
> $$(x+1)(x^2+x) = x^3+x^2+x^2+x = x^3+x = (x+1)+x = 1.$$
> 所以 $x+1$ 和 $x^2+x$ 互為反元素。Gallian p. 302–303 有更多計算。
>
> 講義說：寫出陪集就不好玩了，實務上只寫代表元——就像 $\mathbb{C} = \mathbb{R}[x]/\langle x^2+1\rangle$ 的元素 $a+bx+\langle x^2+1\rangle$，我們平常只寫 $a+bi$、$i^2=-1$。
>
> **Example 4.6.25**（p. 153）：$x^2+1\in\mathbb{Z}_3[x]$ 不可約（第 36 集算過沒有根），所以
> $$\mathbb{Z}_3[x]/\langle x^2+1\rangle = \{a+bx+\langle x^2+1\rangle : a,b\in\mathbb{Z}_3\}$$
> 是 9 個元素的體。$(a+bx)(c+dx) = (ac-bd)+(ad+bc)x$，所以它同構於第 28 集的 **$\mathbb{Z}_3[i]$**。

---

## 5. 一頁速查表

**$\Phi_p$ 不可約**：$\Phi_p(x+1) = x^{p-1}+px^{p-2}+\cdots+p$ 滿足 Eisenstein（$p$）；平移技巧：$\Phi_p = gh$ ⇒ $\Phi_p(x+1) = g(x+1)h(x+1)$。**關鍵一步**：$p\mid\binom pk$（$1\le k\le p-1$）。

**$\langle p(x)\rangle$ 極大 ⇔ $p(x)$ 不可約**（$F$ 是體）

| 方向 | 關鍵一步 |
|---|---|
| (⇒) | $p = gh$ ⇒ $\langle p\rangle\subseteq\langle g\rangle$ ⇒ $\langle g\rangle = \langle p\rangle$（次數相等，$h$ 是常數）或 $\langle g\rangle = F[x]$（$g$ 是單位） |
| (⇐) | $F[x]$ 是 PID ⇒ 中間的理想 $=\langle g\rangle$ ⇒ $p = kg$ ⇒ $k$ 或 $g$ 是單位 |

**推論**

- $p$ 不可約 ⇒ $F[x]/\langle p\rangle$ 是體。
- $p$ 不可約、$p\mid ab$ ⇒ $p\mid a$ 或 $p\mid b$（⇒ 唯一分解）。

**例子**

| 體 | 元素數 | 規則 |
|---|---|---|
| $\mathbb{Z}_2[x]/\langle x^3+x+1\rangle$ | 8 | $x^3 = x+1$ |
| $\mathbb{Z}_3[x]/\langle x^2+1\rangle\cong\mathbb{Z}_3[i]$ | 9 | $x^2 = -1$ |
| $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$ | ∞ | $x^2 = -1$ |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\mathbb{Z}[x]$ 是唯一分解整環；不可約 vs 質 | 第 38–39 集 |
| Euclid 整環 ⇒ PID ⇒ UFD | 第 38–39 集 |
| $F[x]/\langle p(x)\rangle$ 是包含 $p$ 的根的擴張體（Kronecker 定理） | 第 40–41 集 |
| 最小多項式、單擴張 $F(\alpha)\cong F[x]/\langle p\rangle$ | 第 42–43 集 |
| 有限體（$p^n$ 個元素） | 第 40–45 集 |

---

## 附：本集一句話總結

> **把 $\Phi_p$ 平移成 $\Phi_p(x+1)$ 就能用 Eisenstein 證它不可約。在體上的多項式環裡，「$\langle p(x)\rangle$ 是極大理想」恰好就是「$p(x)$ 不可約」——所以模掉一個不可約多項式就得到一個新的體，例如 8 個元素的 $\mathbb{Z}_2[x]/\langle x^3+x+1\rangle$；而不可約多項式也像質數一樣：整除乘積就整除其中一個。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-03 第 2 部錄影逐字稿（whisper 轉錄，17:40）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.6 整理。*
