---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 15
lecture: Lecture 15
date: 2023-02-20
video: https://youtu.be/CzzPs5_UoBI （part 1）、https://youtu.be/uLBDUPXgstU （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.8 Theorem 2.8.3–2.8.5、§2.9（書頁 60–64，PDF 頁 79–83）
---

# 第 15 集 · 收斂定理回顧、局部可積函數 [▶ 影片](https://youtu.be/CzzPs5_UoBI)

← 上一集：[14-convergence-ae-vs-norm](14-convergence-ae-vs-norm.md) ｜ [總目錄](README.md) ｜ 下一集：[16-riemann-vs-lebesgue](16-riemann-vs-lebesgue.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 15 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 4:07，自動字幕）＋ Debnath & Mikusiński §2.8–2.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 三個收斂定理](#1-三個收斂定理)
- [2. 區間上的積分](#2-區間上的積分)
- [3. 可積 ⟹ 每個區間上可積](#3-可積--每個區間上可積)
- [4. 局部可積函數](#4-局部可積函數)
- [5. 局部可積 × 局部有界 = 局部可積](#5-局部可積--局部有界--局部可積)
- [6. 被可積函數控制的局部可積函數是可積的](#6-被可積函數控制的局部可積函數是可積的)
- [7. 記號約定與 L¹([a,b])](#7-記號約定與-l¹ab)
- [8. 預告：§2.10–2.12](#8-預告2102-12)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 單調收斂定理、控制收斂定理、Fatou 引理（敘述） | Theorem 2.8.3–2.8.5，pp. 60–62 |
| 區間上的積分 | Definition 2.9.1、Theorem 2.9.2，p. 62 |
| 局部可積 | Definition 2.9.3，p. 62 |
| 局部可積的乘積 | Theorem 2.9.4，p. 63 |
| 被 $L^1$ 函數控制 ⟹ 可積 | Theorem 2.9.5，p. 63 |
| $L^1([a,b])$ | p. 63 |

---

## 1. 三個收斂定理

[▶ 00:04](https://youtu.be/CzzPs5_UoBI?t=4) 講者把它們寫在黑板上方（小字），因為之後的證明常用，特別是單調收斂定理。他說今天只敘述、看一看，「讓它們進入我們的系統」。

### 單調收斂定理（Theorem 2.8.3，Beppo Levi）

$(f_n)$ 是可積函數列，幾乎處處單調，而且 $\left|\int f_n\right|\le M$ 對所有 $n$。則存在可積函數 $f$ 使

$$f_n\to f\ \text{i.n.（範數）}\quad\text{且}\quad f_n\to f\ \text{a.e.},\qquad\left|\int f\right|\le M.$$

講者提醒：「按範數」很容易漏看。

### Lebesgue 控制收斂定理（Theorem 2.8.4）

[▶ 02:44](https://youtu.be/CzzPs5_UoBI?t=164)

$(f_n)$ 是可積函數列，$f_n\to f$ a.e.，而且存在**可積**函數 $h$ 使 $|f_n|\le h$ 對所有 $n$。則 $f$ 可積，而且 $f_n\to f$ i.n.（因此 $\int f_n\to\int f$）。

### Fatou 引理（Theorem 2.8.5）

[▶ 04:05](https://youtu.be/CzzPs5_UoBI?t=245)

$(f_n)$ 是**非負**可積函數列，$\int f_n\le M$ 對所有 $n$。若 $f_n\to f$ a.e.，則 $f$ 可積，而且 $\int f\le M$。

講者念全名 Pierre Joseph Louis Fatou（1878–1929），開玩笑說自己只有三個名字，覺得很遜。證明用單調收斂定理，兩段，他急著進下一節所以跳過。

### 單調收斂 vs Fatou

[▶ 06:01](https://youtu.be/CzzPs5_UoBI?t=361)

| | 單調收斂 | Fatou |
|---|---|---|
| 假設 | **單調** a.e. + 積分有界 | **非負** + 積分有界 + a.e. 收斂到 $f$ |
| 結論 | **存在**極限 $f$，i.n. 且 a.e. 收斂 | 已知的極限 $f$ **可積**，$\int f\le M$ |

講者：Fatou 完全沒提單調；它的積分條件沒加絕對值，但函數非負，加不加一樣，不會有相消。而且 Fatou 是「如果 a.e. 收斂到 $f$，那麼……」，所以兩者是「真正不同的動物」。

【課本補充】Fatou 的證明概要：令 $\varphi_{n,k}=\min\{f_n,\dots,f_{n+k}\}$。固定 $n$，對 $k$ 遞減，由單調收斂定理收斂到 $\varphi_n=\inf\{f_n,f_{n+1},\dots\}$；$\varphi_n\le f_n$，所以 $\int\varphi_n\le M$；$(\varphi_n)$ 遞增，再用一次單調收斂定理收斂到可積的 $g$，$\int g\le M$；而 $\varphi_n\to f$ a.e.，所以 $f=g$ a.e.。

---

## 2. 區間上的積分

[▶ 08:15](https://youtu.be/CzzPs5_UoBI?t=495) 課本 §2.9 Definition 2.9.1。

$\int f$ 是對**整條實數線**的積分。應用上常要在有界區間上積分：

$$\int_a^bf=\int f\chi_{[a,b]},$$

$\chi_{[a,b]}$ 是 $[a,b]$ 的特徵函數，$f\chi_{[a,b]}$ 是逐點乘積。

講者【口頭】[▶ 09:35](https://youtu.be/CzzPs5_UoBI?t=575)：課本終於用了特徵函數的記號，「寫書時大概一直抗拒，到這節實在需要了才放進來」。

【Q&A】[▶ 10:17](https://youtu.be/CzzPs5_UoBI?t=617) 學生問：$\chi_{[a,b]}$ 是閉區間，不是階梯函數吧？講者：照我們的定義不是；用半開區間是這本書形式上的選擇，不是必要的。課本下一段就說：用閉區間沒有特別意義，用開區間或半開區間定義完全等價；證明時用 $\chi_{[a,b)}$ 比較方便。

> 以下**不是逐字稿內容**，是補一句理由：$\chi_{[a,b]}$ 和 $\chi_{[a,b)}$ 只差一個點 $\{b\}$，單點是零集，所以兩者幾乎處處相等，積分一樣。

---

## 3. 可積 ⟹ 每個區間上可積

[▶ 12:02](https://youtu.be/CzzPs5_UoBI?t=722) 課本 Theorem 2.9.2。

**定理**：若 $f\in L^1(\mathbb{R})$，則 $\int_a^bf$ 對每個區間 $[a,b]$ 存在。

**證明**：$f\simeq f_1+f_2+\cdots$。令

$$g_n(x)=\begin{cases}f_n(x), & x\in[a,b]\\0, & \text{其他}\end{cases}$$

課本說「容易檢查」$f\chi_{[a,b]}\simeq g_1+g_2+\cdots$。

【課堂討論】[▶ 14:57](https://youtu.be/CzzPs5_UoBI?t=897) 講者說他「需要帶點心，這時間精神很差」。他和學生一起檢查：

- 學生指出 $g_n=f_n\chi_{[a,b]}$。
- **條件 (a)**：$|g_n|\le|f_n|$，所以 $\sum\int|g_n|\le\sum\int|f_n|<\infty$。
- **條件 (b)**[▶ 18:35](https://youtu.be/CzzPs5_UoBI?t=1115)：分兩種情況。
  - $x\notin[a,b]$：$f\chi_{[a,b]}(x)=f(x)\cdot0=0$，而所有 $g_n(x)=0$，相符。
  - $x\in[a,b]$：$f\chi_{[a,b]}(x)=f(x)=\sum f_n(x)=\sum g_n(x)$（在絕對收斂的點），相符。

**反過來不成立**[▶ 21:01](https://youtu.be/CzzPs5_UoBI?t=1261)：常數函數 $f=1$，$\int_a^b1=b-a$ 對每個有限區間都存在，但 $1\notin L^1(\mathbb{R})$——在整條實數線上積分會爆掉。講者說他差點講成「保守向量場」，物理還在腦袋裡。

### 為什麼 1 不可積？

【課堂討論】[▶ 25:13](https://youtu.be/CzzPs5_UoBI?t=1513) 講者問：怎麼直接從定義證明 1 不是 Lebesgue 可積？學生說它違反條件 (a)。講者說：可以用階梯函數表示 1（每個整數區間一塊），但要證的是**不存在**滿足 (a)(b) 的表示，這比較難。學生提到用 p. 41 的定義看權重乘長度會超過；講者想到用「第 $n$ 項檢驗」之類論證級數處處發散。最後講者說：「我們在追一隻無趣的兔子」，往下走。[▶ 33:08](https://youtu.be/CzzPs5_UoBI?t=1988)

> 以下**不是逐字稿內容**，是一個簡短的證明：假設 $1\in L^1(\mathbb{R})$。對每個 $n$，$\chi_{[-n,n)}\le1$，由積分的單調性（Theorem 2.3.4），$2n=\int\chi_{[-n,n)}\le\int1$。這對所有 $n$ 成立，但 $\int1$ 是有限的實數，矛盾。

---

## 4. 局部可積函數

[▶ 23:21](https://youtu.be/CzzPs5_UoBI?t=1401) 課本 Definition 2.9.3。

**定義**：$f$ 定義在 $\mathbb{R}$ 上，若 $\int_a^bf$ 對每個 $-\infty<a<b<\infty$ 都存在，叫**局部可積（locally integrable）**。

- 常數函數 1 是局部可積的，但不可積。
- Theorem 2.9.2 換句話說：**可積 ⟹ 局部可積**；反過來不對。[▶ 33:41](https://youtu.be/CzzPs5_UoBI?t=2021)

講者【口頭】[▶ 24:38](https://youtu.be/CzzPs5_UoBI?t=1478)：Lebesgue 積分在某種意義上是把 Riemann 的 $\int_{-\infty}^\infty$ 形式化，所以函數如果不趨近 0，就沒戲了。

【課本補充】

- 只要檢查 $\int_{-n}^nf$ 對每個 $n\in\mathbb{N}$ 存在就夠了（習題）。
- 局部可積函數構成向量空間，$L^1(\mathbb{R})$ 是它的子空間。
- 局部可積函數的絕對值是局部可積的。
- 但局部可積函數的**乘積**不一定局部可積（習題 39）。講者說習題 39 大概是「$\frac{1}{\sqrt{x}}$ 乘 $\frac1{\sqrt x}$ 得 $\frac1x$」那類例子，兩個因子用同一個「秘密壞醬汁」造成發散。[▶ 35:14](https://youtu.be/CzzPs5_UoBI?t=2114)

> 以下**不是逐字稿內容**，是那類例子的驗證：令 $f(x)=|x|^{-1/2}$（$x\ne0$）、$f(0)=0$。$\int_{-1}^1|x|^{-1/2}dx=4$，所以 $f$ 局部可積；但 $f^2=\frac1{|x|}$，$\int_{-1}^1\frac{dx}{|x|}=\infty$，所以 $f\cdot f$ 不局部可積。

---

## 5. 局部可積 × 局部有界 = 局部可積

[▶ 34:12](https://youtu.be/CzzPs5_UoBI?t=2052) 課本 Theorem 2.9.4。

**定理**：$f,g$ 局部可積，$g$ 在每個 $[a,b]$ 上**有界**。則 $fg$ 局部可積。

**證明**[▶ 36:23](https://youtu.be/CzzPs5_UoBI?t=2183)：固定 $a<b$。令 $F=f\chi_{[a,b)}$、$G=g\chi_{[a,b)}$。講者解釋：「$\int_a^bf$ 存在」就是說 $F$ 是 Lebesgue 可積。

1. $F\simeq f_1+f_2+\cdots$，$f_n$ 是支撐在 $[a,b)$ 內的階梯函數。
2. 要證 $FG\simeq f_1g+f_2g+\cdots$。（講者指出 $FG=fg\chi_{[a,b)}$，因為 $\chi\cdot\chi=\chi$：$1\cdot1=1$，$0\cdot0=0$。[▶ 46:35](https://youtu.be/CzzPs5_UoBI?t=2795)）
3. **條件 (a)**：在 $[a,b)$ 上 $|g|<M$，所以 $|f_ng|<M|f_n|$，
   $$\sum\int|f_ng|<M\sum\int|f_n|<\infty.$$
   講者說：常數乘收斂級數還是收斂。
4. **條件 (b)**[▶ 43:43](https://youtu.be/CzzPs5_UoBI?t=2623)：若 $\sum|g(x)f_n(x)|<\infty$，因為 $g$ 不依賴 $n$，$\sum|g(x)f_n(x)|=|g(x)|\sum|f_n(x)|$。所以要嘛 $g(x)=0$，要嘛 $\sum|f_n(x)|<\infty$。兩種情況都有 $F(x)G(x)=\sum f_n(x)g(x)$。∎

講者：有趣的是只需要 $g$ 有界，不需要 $f$ 有界。

**「有界」要有絕對值**【Q&A】[▶ 50:25](https://youtu.be/CzzPs5_UoBI?t=3025) 學生指出：課本寫「$g<M$」，但第 3 步要的是 $|g|<M$，只有上界推不出來（$g$ 可能是很大的負數）。講者先想從 $g<M$ 推出 $|g|<M$，試了一下發現推不出來，同意學生：應該寫 $|g|<M$。「說一個東西有界，本來就該上下都有界。」

---

## 6. 被可積函數控制的局部可積函數是可積的

[▶ 48:29](https://youtu.be/CzzPs5_UoBI?t=2909) 課本 Theorem 2.9.5。

**定理**：$f$ 局部可積，而且 $|f|\le g$ 對某個 $g\in L^1(\mathbb{R})$。則 $f\in L^1(\mathbb{R})$。

**證明**[▶ 53:56](https://youtu.be/CzzPs5_UoBI?t=3236)：

1. 令 $f_n=f\chi_{[-n,n]}$。局部可積 ⟹ $\int_{-n}^nf$ 存在，所以 $f_n$ 可積。
2. $f_n\to f$ **處處**（每個 $x$，$n>|x|$ 後 $f_n(x)=f(x)$），當然 a.e.。
3. $|f_n|\le|f|\le g$，$g$ 可積。
4. 由 **Lebesgue 控制收斂定理**，$f$ 可積。∎

講者說：只用到控制收斂定理的「$f$ 可積」那一半，沒用「按範數收斂」那一半。局部可積和可積不等價，但兩者之間有一些交互作用。[▶ 57:44](https://youtu.be/CzzPs5_UoBI?t=3464)

---

## 7. 記號約定與 L¹([a,b])

[▶ 58:17](https://youtu.be/CzzPs5_UoBI?t=3497)

**約定**：

$$\int_a^bf=-\int_b^af\quad(b<a),\qquad\int_a^af=0.$$

**$L^1([a,b])$**[▶ 58:51](https://youtu.be/CzzPs5_UoBI?t=3531)：$L^1(\mathbb{R})$ 中所有在 $[a,b]$ 外為 0 的函數（支撐包含在 $[a,b]$ 內），是向量空間。作為 $L^1(\mathbb{R})$ 的子空間，把幾乎處處相等的函數視為同一個，它是賦範空間，範數

$$\|f\|=\int_a^b|f|.$$

【課堂討論】講者問範數是什麼，學生答：定積分。講者說：「它不真的是賦範空間，但幾乎是」，理由跟之前一樣（零函數）。[▶ part 2 00:00](https://youtu.be/uLBDUPXgstU?t=0)

【課本補充】$L^1([a,b])$ 的完備性容易由 $L^1(\mathbb{R})$ 的完備性推出。其他集合也可以代替區間，§2.11 討論。

---

## 8. 預告：§2.10–2.12

【口頭】[▶ part 2 01:05](https://youtu.be/uLBDUPXgstU?t=65)

- **§2.10**（「我們一直在等的」）：每個 Riemann 可積函數都 Lebesgue 可積；積分函數 $F(x)=\int_c^xf$ 連續；$F$ 是被積函數的反導數（Theorem 2.10.3）；變數代換定理。等於證了微積分基本定理。
- **§2.11**：$\mathbb{R}$ 上的 Lebesgue 測度、可測集。
- **§2.12**：複值函數的積分。講者說這節「很蠢」，可能不教：自變數還是實數，基本上就是做兩個實積分。

講者希望這週講完第 2 章，急著進 Hilbert 空間那章。作業：別等他指定，先開始做；他公布題單後，學生可以說「我做了某某題，能不能加上」。

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵 |
|---|---|---|
| 單調收斂 | a.e. 單調 + $|\int f_n|\le M$ ⟹ $\exists f$，i.n. 且 a.e. | 伸縮級數 |
| 控制收斂 | $f_n\to f$ a.e. + $|f_n|\le h\in L^1$ ⟹ $f\in L^1$，i.n. | 交換極限與積分 |
| Fatou | $f_n\ge0$、$\int f_n\le M$、$f_n\to f$ a.e. ⟹ $f\in L^1$，$\int f\le M$ | $\inf\{f_n,f_{n+1},\dots\}$ + 兩次單調收斂 |
| 區間積分 | $\int_a^bf=\int f\chi_{[a,b]}$ | 開、閉、半開都一樣 |
| 可積 ⟹ 局部可積 | Thm 2.9.2 | $g_n=f_n\chi_{[a,b]}$ |
| 反例 | $1$ 局部可積但不可積 | $2n=\int\chi_{[-n,n)}\le\int1$ |
| 乘積 | $f,g$ 局部可積、$|g|$ 局部有界 ⟹ $fg$ 局部可積 | $\sum\int|f_ng|<M\sum\int|f_n|$；要 $|g|<M$ |
| 乘積反例 | $|x|^{-1/2}\cdot|x|^{-1/2}=|x|^{-1}$ | 習題 39 |
| 被控制 | $f$ 局部可積、$|f|\le g\in L^1$ ⟹ $f\in L^1$ | $f\chi_{[-n,n]}$ + 控制收斂 |
| $L^1([a,b])$ | 支撐在 $[a,b]$ 內，$\|f\|=\int_a^b|f|$ | 完備 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Riemann vs Lebesgue、微積分基本定理 | 第 16 集（§2.10–2.11） |
| 控制收斂定理 | 第 16–17 集；第 31 集：Fourier 變換 |
| 局部可積函數 | 第 32 集：廣義函數（分佈）——局部可積函數定義正則分佈 |
| $L^1([a,b])$ | 第 18 集起：$L^2([a,b])$ 是 Hilbert 空間 |

---

## 附：本集一句話總結

> **單調收斂、控制收斂、Fatou 三個定理是用「容易檢查的幾乎處處收斂」換取「可積與範數收斂」的工具；而局部可積（每個有限區間上可積）比可積弱，像常數 1 就是局部可積卻不可積——但只要被一個可積函數控制，局部可積就升級成可積。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-20 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 4:07）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.8–2.9 整理。*
