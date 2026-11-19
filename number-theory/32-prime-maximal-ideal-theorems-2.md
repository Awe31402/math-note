---
course: Number Theory（2021 秋，線上錄影）
episode: 32
lecture: 2021-10-25 第 2 部
date: 2021-10-25
video: https://youtu.be/MpcuKv4yme8
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.4 Lecture 24（p. 138–139）：Theorem 4.4.6–4.4.8、Example 4.4.9
---

# 第 32 集 · 核、第一同構定理（Prime and Maximal Ideal Theorems, Ring Isomorphism, Part 2） [▶ 影片](https://youtu.be/MpcuKv4yme8)

← 上一集：[31-prime-maximal-ideal-theorems-1](31-prime-maximal-ideal-theorems-1.md) ｜ [總目錄](README.md) ｜ 下一集：[33-prime-subfields-field-of-fractions-1](33-prime-subfields-field-of-fractions-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 32 集（2021-10-25 第 2 部，接第 31 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（14:22，自動字幕）＋ 講者講義 §4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 核是理想（證明）](#1-核是理想證明)
- [2. 環的第一同構定理](#2-環的第一同構定理)
- [3. 每個理想都是某個同態的核](#3-每個理想都是某個同態的核)
- [4. 例子：Z[x]/⟨x⟩ ≅ Z](#4-例子zx--z)
- [5. 預告：質子體與分式體](#5-預告質子體與分式體)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

接第 31 集：證明核是理想，講**環的第一同構定理**，用它重新看 $\mathbb{Z}[x]/\langle x\rangle$。

| 主題 | 時間 | 講義 |
|---|---|---|
| 核是理想 | 00:06 | Thm 4.4.6 |
| 第一同構定理 | 02:21 | Thm 4.4.7 |
| 理想是核 | 06:55 | Thm 4.4.8 |
| $\mathbb{Z}[x]/\langle x\rangle\cong\mathbb{Z}$ | 08:07 | Ex 4.4.9 |
| 預告 | 12:58 | — |

---

## 1. 核是理想（證明）

[▶ 00:06](https://youtu.be/MpcuKv4yme8?t=6)

> **定理**（講義 Theorem 4.4.6）：$\varphi:R\to S$ 是環同態，則 $\ker\varphi = \{r\in R : \varphi(r) = 0\}$ 是 $R$ 的理想。

設 $a,b\in\ker\varphi$、$r\in R$。用理想判別法（第 29 集）：

1. **減法** [▶ 00:39](https://youtu.be/MpcuKv4yme8?t=39)：
   $$\varphi(a-b) = \varphi(a)-\varphi(b) = 0-0 = 0.$$
   【課堂討論】講者提醒：不能說 $a,b$ 是零，我們知道的是 $\varphi(a) = \varphi(b) = 0$。$\varphi(a-b) = \varphi(a)-\varphi(b)$ 講者說「我沒證過，但你可以證」。所以 $a-b\in\ker\varphi$。
2. **超級封閉** [▶ 01:19](https://youtu.be/MpcuKv4yme8?t=79)：
   $$\varphi(ar) = \varphi(a)\varphi(r) = 0\cdot\varphi(r) = 0,\qquad\varphi(ra) = \varphi(r)\cdot 0 = 0.$$
   所以 $ar,ra\in\ker\varphi$。
3. $\ker\varphi\subseteq R$ 顯然。所以 $\ker\varphi$ 是理想。∎

（講者：說「核是理想」就好，不用說「子理想」，理想本來就是子物件。）

> 以下**不是逐字稿內容**，是補上「你可以證」的那一步：$\varphi(0) = \varphi(0+0) = \varphi(0)+\varphi(0)$，消去得 $\varphi(0) = 0$；再由 $\varphi(b)+\varphi(-b) = \varphi(0) = 0$ 得 $\varphi(-b) = -\varphi(b)$。所以 $\varphi(a-b) = \varphi(a)+\varphi(-b) = \varphi(a)-\varphi(b)$。這就是群同態保持反元素。

---

## 2. 環的第一同構定理

[▶ 02:21](https://youtu.be/MpcuKv4yme8?t=141)

講者：「單看這個定理也許不起眼，但跟下一個定理配在一起，在**構造上**非常有力。」

> **第一同構定理**（講義 Theorem 4.4.7）：$\varphi:R\to S$ 是環同態，則
> $$R/\ker\varphi\ \to\ \varphi(R),\qquad r+\ker\varphi\ \mapsto\ \varphi(r)$$
> 是環同構。也就是
> $$R/\ker\varphi\cong\varphi(R).$$

【課堂討論】講者問：群論裡講過第一同構定理嗎？學生：有。講者：這就是環的版本，「基本上是用環裡面的**加法群**的第一同構定理，乘法的部分就照你希望的那樣順順跟上」。

講義把證明留作練習，講者講思路 [▶ 04:33](https://youtu.be/MpcuKv4yme8?t=273)。記 $K = \ker\varphi$，映射 $\psi(r+K) = \varphi(r)$。

- **單射** [▶ 05:07](https://youtu.be/MpcuKv4yme8?t=307)：若 $\psi(r_1+K) = \psi(r_2+K)$，即 $\varphi(r_1) = \varphi(r_2)$，則 $\varphi(r_1-r_2) = 0$，$r_1-r_2\in K$，所以 $r_1+K = r_2+K$。「輸出相等推出輸入相等。」
- **映成**：「幾乎是自動的」——$\varphi(R)$ 裡任何東西都是某個 $\varphi(r)$，而 $r+K$ 被送到它。
- **保持加法和乘法**：「相當直接」。

> 以下**不是逐字稿內容**，是補兩個講者帶過的地方：
> - **well-defined**：$r_1+K = r_2+K$ ⇒ $r_1-r_2\in K$ ⇒ $\varphi(r_1) = \varphi(r_2)$。（就是單射那條推論反過來。）
> - **保持運算**：$\psi((r+K)(s+K)) = \psi(rs+K) = \varphi(rs) = \varphi(r)\varphi(s)$；加法和 $1+K\mapsto\varphi(1) = 1$ 一樣。

---

## 3. 每個理想都是某個同態的核

[▶ 06:55](https://youtu.be/MpcuKv4yme8?t=415)

> **定理**（講義 Theorem 4.4.8）：環 $R$ 的每個理想都是某個環同態的核。具體地說，理想 $A$ 是
> $$\psi:R\to R/A,\qquad\psi(r) = r+A$$
> 的核。

講者說證明不難，讓大家自己讀。

> 【講義補充】Theorem 4.4.8 的證明（p. 138）：$A$ 是理想，所以商環 $R/A$ well-defined。$\pi(r) = r+A$ 滿足
> $$\pi(r+s) = (r+A)+(s+A),\qquad\pi(rs) = (r+A)(s+A).$$
> $\pi(r) = A$（$R/A$ 的零）⇔ $r\in A$，所以 $\ker\pi = A$。講義說這是 Gallian p. 274 Theorem 15.4。

（合起來：**理想 = 環同態的核**，兩個概念是同一件事。這一句**不是逐字稿內容**。）

---

## 4. 例子：Z[x]/⟨x⟩ ≅ Z

[▶ 08:07](https://youtu.be/MpcuKv4yme8?t=487)（講義 Example 4.4.9）

取求值映射（第 31 集）
$$\varphi:\mathbb{Z}[x]\to\mathbb{Z},\qquad\varphi(f(x)) = f(0).$$

**映成** [▶ 08:38](https://youtu.be/MpcuKv4yme8?t=518)：任取 $a\in\mathbb{Z}$，$\varphi(x+a) = 0+a = a$。

【口頭】「其實直接寫 $\varphi(a) = a$ 就好——在常數多項式上求值，就得回那個常數。$3$ 在 $\pi$ 的值是 $3$，這讓微積分學生很不安，但是真的。我放個 $x$ 是讓你們覺得我們有做事。」

**核** [▶ 10:24](https://youtu.be/MpcuKv4yme8?t=624)：
$$\ker\varphi = \{f\in\mathbb{Z}[x] : f(0) = 0\}.$$

【課堂討論】講者問：代數裡學過什麼？**因式定理**（factor theorem）：多項式在 0 的值是 0，表示 **$x$ 是它的因式**。所以
$$\ker\varphi = \langle x\rangle.$$

**套第一同構定理** [▶ 11:26](https://youtu.be/MpcuKv4yme8?t=686)：
$$\mathbb{Z}[x]/\langle x\rangle\cong\varphi(\mathbb{Z}[x]) = \mathbb{Z}.$$

**直覺** [▶ 11:58](https://youtu.be/MpcuKv4yme8?t=718)：商環 $\mathbb{Z}[x]/\langle x\rangle$ 裡，**$x$ 扮演零**，$x$ 的倍數都是零：
$$a+bx+cx^2+\cdots+c_nx^n+\langle x\rangle = a+\langle x\rangle.$$
只剩常數項 $a$ 活下來。講者：「這只是 $a$ 的一個很蠢的記號。同構就是把 $x$ 丟掉。」

> 【講義補充】Example 4.4.9（p. 139）接著用第 31 集的兩個大定理：$\mathbb{Z}$ 是整環，所以 $\langle x\rangle$ 是**質理想**（Thm 4.3.6）；$\mathbb{Z}$ 不是體，所以 $\langle x\rangle$ **不是極大理想**（Thm 4.3.7）。這跟第 31 集用 $\langle x\rangle\subsetneq\langle2,x\rangle$ 直接證的結論一樣，但完全不用找中間的理想。

---

## 5. 預告：質子體與分式體

[▶ 12:58](https://youtu.be/MpcuKv4yme8?t=778)

講者說下次（從講義 Theorem 4.4.10 開始）「非常令人興奮」：

- **質子體**（prime subfield）：一個體裡面「最小的」體——被所有子體包含的那個子體。它只能是 **$\mathbb{Q}$** 或 **$\mathbb{Z}_p$**（$p$ 質數）。
- **分式體**（field of fractions）的論證：用嚴格的數學**明確地構造出有理數**。講者：「我覺得這是這部分課程的高潮之一。」而且這個構造不只造出 $\mathbb{Q}$，對其他整環一樣能造出「分式體」。

---

## 6. 一頁速查表

**核是理想**：$\varphi(a-b) = \varphi(a)-\varphi(b) = 0$；$\varphi(ar) = \varphi(a)\varphi(r) = 0$。

**第一同構定理**：$R/\ker\varphi\cong\varphi(R)$，$r+\ker\varphi\mapsto\varphi(r)$。

- 單射的**關鍵一步**：$\varphi(r_1) = \varphi(r_2)$ ⇒ $r_1-r_2\in\ker\varphi$。
- 本質是加法群的第一同構定理，乘法跟著走。

**理想 = 核**：理想 $A$ 是自然映射 $R\to R/A$ 的核。

**例子**：$\varphi:\mathbb{Z}[x]\to\mathbb{Z}$，$f\mapsto f(0)$。映成、$\ker\varphi = \langle x\rangle$（因式定理）⇒ $\mathbb{Z}[x]/\langle x\rangle\cong\mathbb{Z}$ ⇒ $\langle x\rangle$ 質、不極大。

**用法**：想知道 $R/A$ 長什麼樣，找一個映成的同態 $R\to S$，核剛好是 $A$，就得 $R/A\cong S$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $n\mapsto n\cdot1$ 的核 ⇒ $\mathbb{Z}_n$ 或 $\mathbb{Z}$ 在環裡；質子體 | 第 33 集 |
| 分式體的構造 | 第 33–34 集 |
| 因式定理的嚴格證明 | 第 35 集 |
| $F[x]/\langle p(x)\rangle$ 用同構定理認出擴張體 | 第 40–43 集 |

---

## 附：本集一句話總結

> **環同態的核一定是理想，每個理想也都是某個同態（自然映射）的核；第一同構定理說 $R/\ker\varphi\cong\varphi(R)$。用求值映射 $f\mapsto f(0)$，馬上得到 $\mathbb{Z}[x]/\langle x\rangle\cong\mathbb{Z}$——把 $x$ 壓成零，只剩常數項。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-25 第 2 部錄影逐字稿（YouTube 自動字幕，14:22）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.4 整理。*
