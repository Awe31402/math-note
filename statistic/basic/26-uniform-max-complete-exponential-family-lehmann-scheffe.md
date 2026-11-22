---
course: 統計學（數理統計，數學系）
episode: 26
lecture: Lec26
date: 待補
video: https://youtu.be/Nbgl9OOb1Cg
notes: Hogg 8th ed. Example 7.4.2 均勻分配的 $Y_n$ 完備（p. 433）；§7.5 指數族（Definition 7.5.1 regular exponential class，p. 435；Theorem 7.5.2，p. 437）；Theorem 7.4.1 Lehmann–Scheffé（p. 432）
---

# 第 26 集 · Lec26：$U(0,\theta)$ 的 $Y_n$ 是完備充分統計量；指數族；Lehmann–Scheffé 定理（敘述） [▶ 影片](https://youtu.be/Nbgl9OOb1Cg)

← 上一集：[25](25-rao-blackwell-theorem-completeness.md) ｜ [總目錄](../README.md) ｜ 下一集：[27](27-lehmann-scheffe-proof-umvue-examples.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 26 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（34:43，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §7.4、§7.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「充分統計量」→「充溫統計量」，「exponential family」照錄（中文「指數族」），「Lehmann–Scheffé」→「Lehmane-Safe」，「微積分基本定理」→「維基因基本定義」，「unique」照錄。[▶ 18:33](https://youtu.be/Nbgl9OOb1Cg?t=1113)–[▶ 26:03](https://youtu.be/Nbgl9OOb1Cg?t=1563) 約 7.5 分鐘沒有講課內容（whisper 只輸出「感谢观看」等幻聽字），應是休息時間。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. U(0, θ)：Yₙ 是充分的（用因子分解）](#1-u0-θyₙ-是充分的用因子分解)
- [2. U(0, θ)：Yₙ 是完備的](#2-u0-θyₙ-是完備的)
- [3. 指數族](#3-指數族)
- [4. 定理：指數族的完備充分統計量](#4-定理指數族的完備充分統計量)
- [5. 唯一的意思](#5-唯一的意思)
- [6. Lehmann–Scheffé 定理](#6-lehmannscheffé-定理)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:30](https://youtu.be/Nbgl9OOb1Cg?t=30) 目標：找 UMVUE。先找一個**又充分又完備**的統計量（sufficient and complete statistic）。

- 證充分：用定義（條件 pdf 不含 $\theta$），或用**因子分解定理**（比較簡單）。
- 證完備：目前只有定義。

| 主題 | 課本 |
|---|---|
| $U(0,\theta)$ 的 $Y_n$：充分（因子分解）、完備（定義） | Example 7.4.2，p. 433 |
| 指數族：直接讀出完備充分統計量 | §7.5，p. 435–437 |
| Lehmann–Scheffé：完備充分統計量的不偏函數就是 UMVUE | Theorem 7.4.1，p. 432 |

---

## 1. U(0, θ)：Yₙ 是充分的（用因子分解）

[▶ 01:32](https://youtu.be/Nbgl9OOb1Cg?t=92) $X_1,\dots,X_n$ iid $U(0,\theta)$，$f(x;\theta)=\frac1\theta$，$0<x<\theta$；$\theta>0$（參數空間 $(0,\infty)$）。

上次用定義證過 $Y_n=\max X_i$ 充分，這次用因子分解定理（[▶ 02:32](https://youtu.be/Nbgl9OOb1Cg?t=152)）：

$$f(\mathbf x;\theta)=\prod_{i=1}^n\frac1\theta I(0<x_i<\theta)=\frac{1}{\theta^n}\prod_{i=1}^nI(0<x_i<\theta).$$

[▶ 04:32](https://youtu.be/Nbgl9OOb1Cg?t=272) 指示函數的乘積是 0 或 1，全部是 1 才是 1 ⇔ 每個 $x_i\in(0,\theta)$ ⇔ 最大的 $y_n\in(0,\theta)$。

$$f(\mathbf x;\theta)=\underbrace{\frac{1}{\theta^n}I(0<y_n<\theta)}_{k_1(y_n;\theta)}\cdot\underbrace{1}_{k_2(\mathbf x)}.$$

⇒ $Y_n$ 充分。

---

## 2. U(0, θ)：Yₙ 是完備的

[▶ 07:05](https://youtu.be/Nbgl9OOb1Cg?t=425) 已知充分，希望它也完備。用定義：任意 $h$，設 $E_\theta[h(Y_n)]=0$，$\forall\theta>0$；要證 $P_\theta(h(Y_n)=0)=1$。

**$Y_n$ 的 pdf**（[▶ 08:39](https://youtu.be/Nbgl9OOb1Cg?t=519)）：$F(x)=\frac x\theta$，
$$f_{Y_n}(y)=n\left(\frac y\theta\right)^{n-1}\frac1\theta=\frac{ny^{n-1}}{\theta^n},\quad 0<y<\theta.$$

**Step 1**（[▶ 10:43](https://youtu.be/Nbgl9OOb1Cg?t=643)）：
$$0=E_\theta[h(Y_n)]=\int_0^\theta h(y)\frac{ny^{n-1}}{\theta^n}\,dy=\frac{n}{\theta^n}\int_0^\theta h(y)y^{n-1}\,dy.$$

【口頭】[▶ 11:14](https://youtu.be/Nbgl9OOb1Cg?t=674) 範圍是 0 到 $\theta$（每個 $X_i$ 都在裡面，最大的也在裡面）。千萬不要寫成 $-\infty$ 到 $\infty$，那樣就證不出來。

**Step 2**（[▶ 11:44](https://youtu.be/Nbgl9OOb1Cg?t=704)）：$\theta>0$ ⇒ $\frac{n}{\theta^n}>0$，所以
$$0=\int_0^\theta h(y)y^{n-1}\,dy,\qquad\forall\theta>0.$$

**Step 3：兩邊對 $\theta$ 微分**（[▶ 12:45](https://youtu.be/Nbgl9OOb1Cg?t=765)）。左邊 0 的微分是 0；右邊用微積分基本定理（把上限 $\theta$ 代進去）：
$$0=h(\theta)\theta^{n-1},\qquad\forall\theta>0.$$

**Step 4**（[▶ 13:47](https://youtu.be/Nbgl9OOb1Cg?t=827)）：$\theta^{n-1}>0$ ⇒ $h(\theta)=0$，$\forall\theta>0$。換個名字：$h(y)=0$，$\forall y>0$；當然 $0<y<\theta$ 時也是 0。

**Step 5**（[▶ 14:47](https://youtu.be/Nbgl9OOb1Cg?t=887)）：$h(Y_n)=0$ 這件事和 $Y_n\in(0,\theta)$ 一樣，所以
$$P_\theta(h(Y_n)=0)=P_\theta(0<Y_n<\theta)=\int_0^\theta f_{Y_n}(y)\,dy=1.$$
（pdf 對整個範圍積分是 1，不用真的積。）對所有 $\theta$ 成立 ⇒ $Y_n$ **完備**。∎

【口頭】[▶ 16:52](https://youtu.be/Nbgl9OOb1Cg?t=1012) 目前只給兩個例子。每個問題都要一個方法去證，不容易，所以希望有一個像因子分解定理一樣的定理，很容易找到完備（順便充分）的統計量。

（另外老師提到：一小時講不完，下週一可能還要上一點點，再上演習課。）

---

## 3. 指數族

[▶ 26:34](https://youtu.be/Nbgl9OOb1Cg?t=1594)

- 每次個別證充分、證完備，非常麻煩；尤其完備，不同分配技巧都不一樣（剛剛兩例就兩種技巧）。
- 有一種形式的分配，很容易找到完備充分統計量。**統計學過的分配大部分都是這種**。叫**指數族**（exponential family）。

> **定義（指數族）**（[▶ 28:06](https://youtu.be/Nbgl9OOb1Cg?t=1686)）：$X$ 的 pdf 若能寫成
> $$f(x;\theta)=\exp\left[a(x)b(\theta)+c(\theta)+d(x)\right],\qquad l<x<q,$$
> 而且 $l,q$ 是**不依賴 $\theta$** 的常數（可以是 $\pm\infty$），就說它屬於指數族。

- 不一定一開始就長這樣，**能轉換成**這個形式就算。
- [▶ 29:08](https://youtu.be/Nbgl9OOb1Cg?t=1748) 最重要的是「$x$ 的函數 × $\theta$ 的函數」那一項 $a(x)b(\theta)$。$c(\theta)$、$d(x)$ 沒有就當 0。
- **範圍不能依賴 $\theta$**。

[▶ 29:38](https://youtu.be/Nbgl9OOb1Cg?t=1778) **反例**：$U(0,\theta)$ 的 pdf $\frac1\theta$，$0<x<\theta$，範圍和 $\theta$ 有關 ⇒ **不屬於**指數族。

【口頭】轉換不難，做幾個例子就會。

【課本補充】課本 Definition 7.5.1（p. 435）叫 **regular exponential class**，寫成 $\exp[p(\theta)K(x)+H(x)+q(\theta)]$，除了 support 不依賴 $\theta$，還要求 $p(\theta)$ 是非平凡的連續函數、$K(x)$ 不恆為 0 等正則條件。

---

## 4. 定理：指數族的完備充分統計量

[▶ 30:08](https://youtu.be/Nbgl9OOb1Cg?t=1808)

> **定理**（課本 Theorem 7.5.2，p. 437）：$X_1,\dots,X_n$ 是隨機樣本，來自指數族
> $$f(x;\theta)=\exp\left[a(x)b(\theta)+c(\theta)+d(x)\right],$$
> 則
> $$\sum_{i=1}^na(X_i)$$
> 是**完備充分統計量**。

- 做法：把 pdf 化成這個形式，$x$ 乘 $\theta$ 那一項的「$x$ 函數」$a(x)$，把 $x$ 換成 $X_i$ 加起來，就是答案。
- 【口頭】太容易了。這個定理很難，本課沒辦法證，但會告訴你怎麼判斷。

---

## 5. 唯一的意思

[▶ 31:38](https://youtu.be/Nbgl9OOb1Cg?t=1898) 要證下一個定理會用到**唯一**（unique）。

> 兩個隨機變數 $X,Y$「一樣」，若 $P(X=Y)=1$。

所以「唯一」是指：滿足條件的隨機變數，任兩個相等的機率是 1，當成只有一個。

---

## 6. Lehmann–Scheffé 定理

[▶ 32:09](https://youtu.be/Nbgl9OOb1Cg?t=1929) Lehmann 和 Scheffé 兩個人證的。

> **Lehmann–Scheffé 定理**（課本 Theorem 7.4.1，p. 432）：$U$ 是**完備充分統計量**。若 $\hat\tau=T(U)$ 是 $U$ 的函數，且是 $\tau(\theta)$ 的不偏估計量（$E_\theta[T(U)]=\tau(\theta)$），則
> 1. 這樣的函數是**唯一的**（$U$ 的不偏函數只有一個）；
> 2. $T(U)$ 就是 $\tau(\theta)$ 的 **UMVUE**。

[▶ 33:40](https://youtu.be/Nbgl9OOb1Cg?t=2020) 【口頭】這個定理非常好：只要找得到完備充分統計量，它的函數只要不偏，就是 UMVUE；而且這樣的函數只有一個。

證明下次講。

---

## 7. 一頁速查表

**$U(0,\theta)$ 的 $Y_n=\max X_i$**

- 充分：$f(\mathbf x;\theta)=\theta^{-n}I(0<y_n<\theta)\cdot 1$。
- 完備：$0=\int_0^\theta h(y)y^{n-1}dy$ $\forall\theta$ → 對 $\theta$ 微分得 $h(\theta)\theta^{n-1}=0$ → $h\equiv 0$。
- 範圍是 $(0,\theta)$，不能寫 $(-\infty,\infty)$。

**指數族**：$f(x;\theta)=\exp[a(x)b(\theta)+c(\theta)+d(x)]$，範圍不依賴 $\theta$。
⇒ $\sum a(X_i)$ 是完備充分統計量。
（$U(0,\theta)$ 範圍依賴 $\theta$，不是指數族。）

**唯一**：$P(X=Y)=1$ 就當作一樣。

**Lehmann–Scheffé**：$U$ 完備充分，$T(U)$ 不偏 ⇒ $T(U)$ 是唯一的 UMVUE。

找 UMVUE 的流程：
1. 找完備充分統計量 $U$（指數族直接讀 $\sum a(X_i)$）。
2. 找 $U$ 的函數讓它不偏。
3. 那就是 UMVUE。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Lehmann–Scheffé 的證明 | 下一集 |
| 指數族 | 下一集：常見分配化成指數族、求 UMVUE |
| $U(0,\theta)$ 的 $Y_n$ 完備充分 | UMVUE 是 $\frac{n+1}{n}Y_n$ |

---

## 附：本集一句話總結

> **$U(0,\theta)$ 的 $Y_n$ 用因子分解證充分、用「積分恆為 0 再對 $\theta$ 微分」證完備；屬於指數族 $\exp[a(x)b(\theta)+c(\theta)+d(x)]$（範圍不含 $\theta$）的分配，$\sum a(X_i)$ 直接就是完備充分統計量；Lehmann–Scheffé 定理說：完備充分統計量的不偏函數唯一，而且就是 UMVUE。**

---

*筆記依據「統計學」Lec26 錄影逐字稿（whisper large-v3-turbo，34:43）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
