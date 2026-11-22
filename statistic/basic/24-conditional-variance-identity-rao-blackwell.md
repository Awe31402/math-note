---
course: 統計學（數理統計，數學系）
episode: 24
lecture: Lec24
date: 待補
video: https://youtu.be/Z5Re1IstFm4
notes: Hogg 8th ed. §2.3 Theorem 2.3.1(b)（p. 114）；§7.3 Rao–Blackwell 定理（Theorem 7.3.1，p. 427）
---

# 第 24 集 · Lec24：證明 $\text{Var}(Y)=E[\text{Var}(Y|X)]+\text{Var}[E(Y|X)]$；Rao–Blackwell 的想法 [▶ 影片](https://youtu.be/Z5Re1IstFm4)

← 上一集：[23](23-factorization-proof-examples-conditional-expectation.md) ｜ [總目錄](../README.md) ｜ 下一集：[25](25-rao-blackwell-theorem-completeness.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 24 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（30:23，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.3、§7.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Lemma」→「LEMA」，「variance」→「valance／valence」，「conditional mean」照錄，「充分統計量」照錄。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：(a) 與變異數公式](#1-複習a-與變異數公式)
- [2. 證明 (b)：Var(Y)＝E[Var(Y|X)]＋Var[E(Y|X)]](#2-證明-bvaryevaryxvareyx)
- [3. 改善一個不偏估計量](#3-改善一個不偏估計量)
- [4. Lemma：給定統計量取條件期望值](#4-lemma給定統計量取條件期望值)
- [5. 陷阱：結果不一定是統計量](#5-陷阱結果不一定是統計量)
- [6. U 是充分統計量時就沒問題](#6-u-是充分統計量時就沒問題)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 證明 $\text{Var}(Y)=E[\text{Var}(Y\mid X)]+\text{Var}[E(Y\mid X)]$ | Theorem 2.3.1，p. 114 |
| 給定統計量取條件期望值：仍不偏、變異數變小 | Theorem 7.3.1（Rao–Blackwell），p. 427 |
| 為什麼要給定**充分**統計量 | §7.3 |

---

## 1. 複習：(a) 與變異數公式

[▶ 00:30](https://youtu.be/Z5Re1IstFm4?t=30)

- **(a)**：$E[E(Y\mid X)]=E(Y)$。$E(Y\mid X)$ 怎麼來：先給小寫 $x$ 算條件期望值（$x$ 的函數），再把 $x$ 改大寫，變成隨機變數，就能再取期望值。
- [▶ 01:33](https://youtu.be/Z5Re1IstFm4?t=93) **變異數**：$\text{Var}(Y)=E[(Y-EY)^2]=E(Y^2)-(EY)^2$。

---

## 2. 證明 (b)：Var(Y)＝E[Var(Y|X)]＋Var[E(Y|X)]

[▶ 02:34](https://youtu.be/Z5Re1IstFm4?t=154)

> $$\text{Var}(Y)=E\left[\text{Var}(Y\mid X)\right]+\text{Var}\left[E(Y\mid X)\right].$$

- $\text{Var}(Y\mid X)$、$E(Y\mid X)$ 都是 $X$ 的函數，是隨機變數，所以前者能取期望值、後者能取變異數。
- 「條件變異數的期望值，加上條件期望值的變異數，等於 $Y$ 的變異數。」

**Step 1：條件變異數的捷徑**（[▶ 03:34](https://youtu.be/Z5Re1IstFm4?t=214)）。先給小寫 $x$。定義是 $E[(Y-E(Y\mid x))^2\mid x]$，展開平方再取條件期望值（和一般變異數一樣）：
$$\text{Var}(Y\mid x)=E(Y^2\mid x)-[E(Y\mid x)]^2.$$
「平方的條件期望值，減掉條件期望值的平方。」

**Step 2：換成大寫 $X$，兩邊取期望值**（[▶ 06:11](https://youtu.be/Z5Re1IstFm4?t=371)）
$$E[\text{Var}(Y\mid X)]=E\left[E(Y^2\mid X)\right]-E\left[(E(Y\mid X))^2\right].$$
第一項：$Y^2$ 也是隨機變數，用 (a)：$E[E(Y^2\mid X)]=E(Y^2)$。

第二項**不能**用 (a)：[▶ 08:14](https://youtu.be/Z5Re1IstFm4?t=494) 是條件期望值**先平方**再取期望值，不等於 $E(Y^2)$。照抄。
$$E[\text{Var}(Y\mid X)]=E(Y^2)-E\left[(E(Y\mid X))^2\right].\tag{1}$$

**Step 3：條件期望值的變異數**（[▶ 08:46](https://youtu.be/Z5Re1IstFm4?t=526)）。$E(Y\mid X)$ 是隨機變數，用「平方的期望值減期望值的平方」，再用 (a)：
$$\text{Var}[E(Y\mid X)]=E\left[(E(Y\mid X))^2\right]-\left(E[E(Y\mid X)]\right)^2=E\left[(E(Y\mid X))^2\right]-(EY)^2.\tag{2}$$

**Step 4：相加**（[▶ 10:16](https://youtu.be/Z5Re1IstFm4?t=616)）。(1)＋(2)，$E[(E(Y\mid X))^2]$ 一正一負消掉：
$$E[\text{Var}(Y\mid X)]+\text{Var}[E(Y\mid X)]=E(Y^2)-(EY)^2=\text{Var}(Y).\qquad\blacksquare$$

【口頭】[▶ 10:46](https://youtu.be/Z5Re1IstFm4?t=646) 有點複雜，用背的沒用。要一步一步了解什麼叫條件 pdf、條件期望值、條件變異數，否則會被符號弄亂。條件（conditional）這個觀念在統計裡很重要。

---

## 3. 改善一個不偏估計量

[▶ 11:16](https://youtu.be/Z5Re1IstFm4?t=676) 目的：找 UMVUE。沒辦法直接告訴你怎麼找，要靠定理一步一步建立。

設 $X_1,\dots,X_n$ 來自 $f(x;\theta)$，要估 $\tau(\theta)$。

[▶ 12:17](https://youtu.be/Z5Re1IstFm4?t=737) **思路**：先有一個估計量，想辦法**改進**它；改進後的比原本好，還可以再改進，越來越好，就會趨近 UMVUE。

---

## 4. Lemma：給定統計量取條件期望值

[▶ 12:47](https://youtu.be/Z5Re1IstFm4?t=767)

> **Lemma**：$\hat\tau=\hat\tau(X_1,\dots,X_n)$ 是 $\tau(\theta)$ 的不偏估計量，$U=u(X_1,\dots,X_n)$ 是任一統計量。則
> (a) $E(\hat\tau\mid U)$ 也是不偏的：$E\left[E(\hat\tau\mid U)\right]=\tau(\theta)$；
> (b) $\text{Var}\left[E(\hat\tau\mid U)\right]\le\text{Var}(\hat\tau)$。

[▶ 14:18](https://youtu.be/Z5Re1IstFm4?t=858) 意思：只要找到一個統計量，給定它取條件期望值，就得到一個**仍然不偏、變異數更小**的東西。「你是不偏，我還是不偏；我的變異數比你小，就改進了。」

**證明 (a)**（[▶ 18:32](https://youtu.be/Z5Re1IstFm4?t=1112)）：$\hat\tau$ 是隨機變數（角色是 $Y$），$U$ 是隨機變數（角色是 $X$）。用 (a)：
$$E\left[E(\hat\tau\mid U)\right]=E(\hat\tau)=\tau(\theta).$$
（最後一步是因為 $\hat\tau$ 不偏。）

**證明 (b)**（[▶ 20:34](https://youtu.be/Z5Re1IstFm4?t=1234)）：用本集證的 (b)：
$$\text{Var}(\hat\tau)=E\left[\text{Var}(\hat\tau\mid U)\right]+\text{Var}\left[E(\hat\tau\mid U)\right].$$
[▶ 22:09](https://youtu.be/Z5Re1IstFm4?t=1329) 第一項 $\ge 0$：

- 變異數沒有負的：$\text{Var}(X)=\int(x-EX)^2f(x)\,dx$，平方 $\ge 0$、pdf $\ge 0$，積分 $\ge 0$。
- 條件變異數同理 $\ge 0$；非負的東西取期望值（積分）還是 $\ge 0$。

刪掉第一項，右邊變小：$\text{Var}(\hat\tau)\ge\text{Var}[E(\hat\tau\mid U)]$。∎

---

## 5. 陷阱：結果不一定是統計量

[▶ 24:45](https://youtu.be/Z5Re1IstFm4?t=1485) Lemma 說「不偏」，但**沒說是估計量**。

[▶ 25:48](https://youtu.be/Z5Re1IstFm4?t=1548)

- $E(\hat\tau\mid U)$ 是 $U$ 的函數，所以是 $X_1,\dots,X_n$ 的函數。
- 但這個函數裡**可能有 $\theta$**（條件期望值要用條件 pdf 算，條件 pdf 可能含 $\theta$）。
- 有 $\theta$ 就不是統計量，就不能當估計量。

---

## 6. U 是充分統計量時就沒問題

[▶ 26:48](https://youtu.be/Z5Re1IstFm4?t=1608)

$U$ 是**充分統計量** ⇒ 給定 $U=u$，$X_1,\dots,X_n$ 的條件 pdf **不含 $\theta$**。

[▶ 28:20](https://youtu.be/Z5Re1IstFm4?t=1700) 所以
$$E(\hat\tau\mid U=u)=\int\!\cdots\!\int\hat\tau(x_1,\dots,x_n)\,f(x_1,\dots,x_n\mid U=u)\,d\mathbf x.$$

- $\hat\tau$ 是估計量，不含 $\theta$。
- 條件 pdf 不含 $\theta$（$U$ 充分）。
- 積出來是 $u$ 的函數、不含 $\theta$；把 $u$ 改成大寫 $U$，還是不含 $\theta$。

⇒ $E(\hat\tau\mid U)$ 是**統計量**，所以是**不偏估計量**，而且變異數比 $\hat\tau$ 小。

【口頭】[▶ 24:45](https://youtu.be/Z5Re1IstFm4?t=1485) 這就是為什麼前面要講充分統計量：充分統計量跟這個結果合起來，是一個很重要的結果（下一集的定理）。

【課本補充】這就是 **Rao–Blackwell 定理**（課本 Theorem 7.3.1，p. 427）：$Y_1$ 是 $\theta$ 的充分統計量，$Y_2$ 是 $\theta$ 的不偏估計量，則 $\varphi(Y_1)=E(Y_2\mid Y_1)$ 是 $Y_1$ 的函數、是 $\theta$ 的不偏估計量，且 $\text{Var}(\varphi(Y_1))\le\text{Var}(Y_2)$。

---

## 7. 一頁速查表

**條件變異數公式**

- $\text{Var}(Y\mid x)=E(Y^2\mid x)-[E(Y\mid x)]^2$。
- $\text{Var}(Y)=E[\text{Var}(Y\mid X)]+\text{Var}[E(Y\mid X)]$。

關鍵一步：
$E[\text{Var}(Y\mid X)]=E(Y^2)-E[(E(Y\mid X))^2]$；
$\text{Var}[E(Y\mid X)]=E[(E(Y\mid X))^2]-(EY)^2$；
相加，中間項消掉。

**改善不偏估計量**（$\hat\tau$ 不偏，$U$ 統計量）

| | 結論 | 用的工具 |
|---|---|---|
| 不偏 | $E[E(\hat\tau\mid U)]=\tau(\theta)$ | $E[E(Y\mid X)]=E(Y)$ |
| 變異數變小 | $\text{Var}[E(\hat\tau\mid U)]\le\text{Var}(\hat\tau)$ | 上面的分解，$E[\text{Var}(\cdot\mid U)]\ge 0$ |
| 是統計量？ | 只有 $U$ **充分**時保證是 | 條件 pdf 不含 $\theta$ |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Rao–Blackwell | 下一集：正式定理；UMVUE 一定是充分統計量的函數 |
| 完備性 | Lehmann–Scheffé：完備充分統計量的不偏函數就是 UMVUE |

---

## 附：本集一句話總結

> **用「平方的條件期望值減條件期望值的平方」和 $E[E(Y\mid X)]=E(Y)$ 證明 $\text{Var}(Y)=E[\text{Var}(Y\mid X)]+\text{Var}[E(Y\mid X)]$；於是給定任何統計量取條件期望值，不偏估計量仍不偏、變異數變小，但只有給定**充分**統計量時，結果才保證不含 $\theta$、是真正的估計量。**

---

*筆記依據「統計學」Lec24 錄影逐字稿（whisper large-v3-turbo，30:23）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
