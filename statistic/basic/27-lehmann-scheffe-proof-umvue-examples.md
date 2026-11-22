---
course: 統計學（數理統計，數學系）
episode: 27
lecture: Lec27
date: 待補
video: https://youtu.be/wqCd8dqj0Uw
notes: Hogg 8th ed. Theorem 7.4.1 Lehmann–Scheffé（p. 432）；Example 7.4.2 $U(0,\theta)$ 的 UMVUE（p. 433）；§7.5 指數族（Theorem 7.5.2，p. 437）
---

# 第 27 集 · Lec27：Lehmann–Scheffé 定理的證明；UMVUE 例題（均勻、Bernoulli、常態） [▶ 影片](https://youtu.be/wqCd8dqj0Uw)

← 上一集：[26](26-uniform-max-complete-exponential-family-lehmann-scheffe.md) ｜ [總目錄](../README.md) ｜ 下一集：（本課最後一集；下學期見[高等統計學](../advanced/)）

> **課程**：統計學（數學系的「數理統計」）— 第 27 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（37:16，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §7.4、§7.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Rao–Blackwell」→「羅伯拉威爾／Robbio」，「Lehmann–Scheffé」→「Lehman's Affair／Lehmann-Safe」，「充分」→「充溫／冲温」，「順序統計量」→「瞬息統計量」，「Bernoulli」→「本能力」，「Poisson」→「普阿森」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：充分、完備、指數族](#1-回顧充分完備指數族)
- [2. Lehmann–Scheffé 定理](#2-lehmannscheffé-定理)
- [3. 證明 (1)：唯一](#3-證明-1唯一)
- [4. 證明 (2)：是 UMVUE](#4-證明-2是-umvue)
- [5. 實際怎麼找 UMVUE](#5-實際怎麼找-umvue)
- [6. 例 1：U(0, θ)](#6-例-1u0-θ)
- [7. 例 2：Bernoulli](#7-例-2bernoulli)
- [8. 例 3：常態（σ²＝1）](#8-例-3常態σ1)
- [9. 結語](#9-結語)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續的連結](#11-與後續的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Lehmann–Scheffé 定理的證明 | Theorem 7.4.1，p. 432 |
| 找 UMVUE 的兩種做法 | §7.4 |
| 例：$U(0,\theta)$、Bernoulli、$N(\mu,1)$ | Example 7.4.2；§7.5 |

---

## 1. 回顧：充分、完備、指數族

[▶ 00:30](https://youtu.be/wqCd8dqj0Uw?t=30)

- **充分統計量**：擁有和樣本一樣多的 $\theta$ 資訊。很多，要維度小的。
- **完備**：再加一個條件。
- [▶ 02:02](https://youtu.be/wqCd8dqj0Uw?t=122) 本來各有找法；分配屬於**指數族**時，很容易找到完備充分統計量。
- 好處：用它來估 $\tau(\theta)$。

**完備的定義**（[▶ 03:36](https://youtu.be/wqCd8dqj0Uw?t=216)，要記得）：
$$E_\theta[h(U)]=0\ \forall\theta\ \Rightarrow\ P_\theta(h(U)=0)=1\ \forall\theta.$$
「任何函數只要期望值恆為 0，它本來就是 0。」所以完備沒那麼容易找。

---

## 2. Lehmann–Scheffé 定理

[▶ 02:33](https://youtu.be/wqCd8dqj0Uw?t=153)

> **Lehmann–Scheffé 定理**（課本 Theorem 7.4.1，p. 432）：$U$ 是完備充分統計量，$\hat\tau=T(U)$ 是 $\tau(\theta)$ 的不偏估計量，則
> 1. $U$ 的函數中，不偏的**只有一個**（unique）；
> 2. 這一個就是 $\tau(\theta)$ 的 **UMVUE**。

---

## 3. 證明 (1)：唯一

[▶ 05:07](https://youtu.be/wqCd8dqj0Uw?t=307) 假設還有另一個 $U$ 的函數 $\hat\tau^*=T^*(U)$ 也不偏，證明兩個一樣。

**Step 1**：$T(U)-T^*(U)$ 也是 $U$ 的函數（兩個 $U$ 的函數相減）。

**Step 2**（[▶ 06:38](https://youtu.be/wqCd8dqj0Uw?t=398)）：兩個都不偏，
$$E_\theta[T(U)-T^*(U)]=\tau(\theta)-\tau(\theta)=0,\qquad\forall\theta.$$

**Step 3**（[▶ 07:10](https://youtu.be/wqCd8dqj0Uw?t=430)）：$U$ 完備，$h(U)=T(U)-T^*(U)$ 的期望值恆為 0 ⇒
$$P_\theta\left(T(U)-T^*(U)=0\right)=1\ \Rightarrow\ P_\theta\left(T(U)=T^*(U)\right)=1.$$

相等的機率是 1，就是相等（上一集「唯一」的意思）。所以 $U$ 的不偏函數只有一個。∎

---

## 4. 證明 (2)：是 UMVUE

[▶ 09:10](https://youtu.be/wqCd8dqj0Uw?t=550) 要證：**任何**不偏估計量的變異數都 $\ge\text{Var}(\hat\tau)$。

設 $T$ 是 $\tau(\theta)$ 的**任一**不偏估計量。

**Step 1：用 Rao–Blackwell**（[▶ 10:10](https://youtu.be/wqCd8dqj0Uw?t=610)）。考慮 $E(T\mid U)$：

- $U$ 充分 ⇒ $E(T\mid U)$ 是**統計量**。
- $E[E(T\mid U)]=E(T)=\tau(\theta)$ ⇒ **不偏**。
- 所以 $E(T\mid U)$ 是不偏估計量。

**Step 2：它是 $U$ 的函數**（[▶ 11:42](https://youtu.be/wqCd8dqj0Uw?t=702)）。給定 $U$ 取期望值，$T$ 被積掉，剩下 $U$。所以 $E(T\mid U)$ 是 $U$ 的不偏函數。由 (1) 唯一性：
$$E(T\mid U)=\hat\tau.$$

**Step 3：變異數**（[▶ 13:13](https://youtu.be/wqCd8dqj0Uw?t=793)）。Rao–Blackwell 還說條件期望值的變異數比較小：
$$\text{Var}(\hat\tau)=\text{Var}[E(T\mid U)]\le\text{Var}(T).$$

$T$ 是任意不偏估計量 ⇒ $\hat\tau$ 的變異數比所有不偏估計量都小 ⇒ $\hat\tau$ 是 **UMVUE**。∎

【口頭】[▶ 15:49](https://youtu.be/wqCd8dqj0Uw?t=949) 這個定理不容易，記結論就好；但要讀統計就要會證。整個懂的話，前面很多觀念都懂了：Rao–Blackwell、充分統計量、完備……這些非常漂亮的觀念整個結合起來，就是這個定理。Lehmann 和 Scheffé 是兩位很重要的統計學家。

---

## 5. 實際怎麼找 UMVUE

[▶ 16:51](https://youtu.be/wqCd8dqj0Uw?t=1011) 已有完備充分統計量 $U$，兩種做法：

**做法 1**：隨便找一個不偏估計量 $T$，算 $E(T\mid U)$，它就是 UMVUE（§4 Step 2）。

- [▶ 17:53](https://youtu.be/wqCd8dqj0Uw?t=1073) 缺點：常常**導不出來**（條件期望值很難算）。某些特殊問題要靠這種方式。

**做法 2**（大部分用這個，比較簡單）：直接算 $E(U)$。

- 若 $E(U)=c\cdot\tau(\theta)$，則 $U/c$ 是 $U$ 的函數、而且 $E(U/c)=\tau(\theta)$ 不偏 ⇒ 就是 UMVUE。
- [▶ 18:54](https://youtu.be/wqCd8dqj0Uw?t=1134) 若差一個常數，就加回來；是倍數就除回去。

【口頭】[▶ 19:24](https://youtu.be/wqCd8dqj0Uw?t=1164) 這種題目要做很多才清楚，但一定要把觀念弄懂。點估計最重要的理論就是這一套：充分、完備、Rao–Blackwell、Cramér–Rao、Lehmann–Scheffé，很多定理連貫在一起，目的就是找 UMVUE。

---

## 6. 例 1：U(0, θ)

[▶ 19:54](https://youtu.be/wqCd8dqj0Uw?t=1194) $X_1,\dots,X_n$ iid $U(0,\theta)$，找 $\theta$ 的 UMVUE。

**完備充分統計量**（[▶ 20:24](https://youtu.be/wqCd8dqj0Uw?t=1224)）：$Y_n=\max X_i$（前兩集證過）。這個分配範圍和 $\theta$ 有關，**不能**用指數族定理。

**$Y_n$ 的 pdf**（[▶ 21:25](https://youtu.be/wqCd8dqj0Uw?t=1285)）：$f_{Y_n}(y)=\dfrac{ny^{n-1}}{\theta^n}$，$0<y<\theta$。

**期望值**（[▶ 22:58](https://youtu.be/wqCd8dqj0Uw?t=1378)）：積分範圍一定是 0 到 $\theta$，
$$E(Y_n)=\int_0^\theta y\cdot\frac{ny^{n-1}}{\theta^n}\,dy=\frac{n}{\theta^n}\cdot\frac{\theta^{n+1}}{n+1}=\frac{n}{n+1}\theta.$$

**UMVUE**（[▶ 24:31](https://youtu.be/wqCd8dqj0Uw?t=1471)）：除掉常數，
$$\hat\theta=\frac{n+1}{n}Y_n.$$
它是 $Y_n$（完備充分）的函數、而且不偏 ⇒ UMVUE。

【口頭】[▶ 25:37](https://youtu.be/wqCd8dqj0Uw?t=1537) 這個定理讓問題變得非常簡單。這題**不能**用 Cramér–Rao 下界：它的 $x$ 範圍有 $\theta$，不滿足正則條件。一定要用這個方法。

⚠️ 逐字稿缺字：[▶ 26:08](https://youtu.be/wqCd8dqj0Uw?t=1568) 字幕寫「Rawbrewal 定理……還要微分……X 範圍不能有 Sita」，依內容（要微分、範圍不能依賴 $\theta$ 是正則條件）應指 **Cramér–Rao 下界**，不是 Rao–Blackwell。

---

## 7. 例 2：Bernoulli

[▶ 26:38](https://youtu.be/wqCd8dqj0Uw?t=1598) $X_1,\dots,X_n$ iid Bernoulli$(p)$，找 $p$ 的 UMVUE。

【口頭】[▶ 26:38](https://youtu.be/wqCd8dqj0Uw?t=1598) 題目如果叫你用 Cramér–Rao 下界，就要找下界、驗證某估計量不偏且變異數等於它；沒指定方法就任何方法都行。這裡用完備充分統計量。

**化成指數族**（[▶ 28:09](https://youtu.be/wqCd8dqj0Uw?t=1689)）：
$$f(x;p)=p^x(1-p)^{1-x}=(1-p)\left(\frac{p}{1-p}\right)^x=\exp\left[x\log\frac{p}{1-p}+\log(1-p)\right],\quad x=0,1.$$

對照 $\exp[a(x)b(\theta)+c(\theta)+d(x)]$（[▶ 29:42](https://youtu.be/wqCd8dqj0Uw?t=1782)）：$a(x)=x$，$b(p)=\log\frac{p}{1-p}$，$c(p)=\log(1-p)$，$d(x)=0$；範圍 $\{0,1\}$ 和 $p$ 無關。

⇒ $\sum X_i$ 是完備充分統計量。

**期望值**（[▶ 30:42](https://youtu.be/wqCd8dqj0Uw?t=1842)）：$E\left(\sum X_i\right)=np$。除以 $n$：
$$\hat p=\frac1n\sum X_i=\bar X\quad\text{是 }p\text{ 的 UMVUE}.$$

【口頭】[▶ 32:15](https://youtu.be/wqCd8dqj0Uw?t=1935) 現在做起來很簡單，是因為我們花了很多時間把定理一步一步建立起來。每個過程都要懂，只會用很容易忘。

---

## 8. 例 3：常態（σ²＝1）

[▶ 32:46](https://youtu.be/wqCd8dqj0Uw?t=1966) $X_1,\dots,X_n$ iid $N(\mu,1)$（變異數已知是 1），找 $\mu$ 的 UMVUE。

**化成指數族**（[▶ 33:17](https://youtu.be/wqCd8dqj0Uw?t=1997)）：
$$f(x;\mu)=\frac{1}{\sqrt{2\pi}}e^{-(x-\mu)^2/2}=\exp\left[x\mu-\frac{x^2}{2}-\frac{\mu^2}{2}-\log\sqrt{2\pi}\right].$$
（展開 $(x-\mu)^2=x^2-2x\mu+\mu^2$，$\frac{1}{\sqrt{2\pi}}$ 取 log 搬到指數上。）

[▶ 34:51](https://youtu.be/wqCd8dqj0Uw?t=2091) $a(x)=x$、$b(\mu)=\mu$，$-\frac{x^2}{2}$ 是 $d(x)$，其他是 $c(\mu)$；範圍 $\mathbb{R}$ 和 $\mu$ 無關。

⇒ $\sum X_i$ 是完備充分統計量。

**期望值**（[▶ 35:22](https://youtu.be/wqCd8dqj0Uw?t=2122)）：$E(\sum X_i)=n\mu$。除以 $n$：
$$\hat\mu=\bar X\quad\text{是 }\mu\text{ 的 UMVUE}.$$

[▶ 36:23](https://youtu.be/wqCd8dqj0Uw?t=2183) 還有一題 Poisson，留給同學自己做，不會再問實習課助教。（方法一樣。）

---

## 9. 結語

[▶ 36:23](https://youtu.be/wqCd8dqj0Uw?t=2183) 【口頭】如果整個都會了，這就是這一套理論。以後想讀和統計有關的，要花時間把前面這些理論全部搞清楚。

---

## 10. 一頁速查表

**Lehmann–Scheffé**：$U$ 完備充分，$T(U)$ 不偏 ⇒ $T(U)$ 唯一且是 UMVUE。

| 部分 | 關鍵一步 |
|---|---|
| 唯一 | $E[T(U)-T^*(U)]\equiv 0$ + 完備 ⇒ $P(T=T^*)=1$ |
| UMVUE | 任意不偏 $T$：$E(T\mid U)$ 是 $U$ 的不偏函數 ⇒ $=\hat\tau$；Rao–Blackwell ⇒ $\text{Var}(\hat\tau)\le\text{Var}(T)$ |

**找 UMVUE**

1. 找完備充分統計量 $U$（指數族：$\sum a(X_i)$；均勻：$Y_n$）。
2. 算 $E(U)$，調整常數讓它不偏。

| 分配 | 完備充分統計量 | $E(U)$ | UMVUE |
|---|---|---|---|
| $U(0,\theta)$ | $Y_n$ | $\frac{n}{n+1}\theta$ | $\frac{n+1}{n}Y_n$ |
| Bernoulli$(p)$ | $\sum X_i$ | $np$ | $\bar X$ |
| $N(\mu,1)$ | $\sum X_i$ | $n\mu$ | $\bar X$ |

**指數族寫法**：
- Bernoulli：$\exp\left[x\log\frac{p}{1-p}+\log(1-p)\right]$。
- $N(\mu,1)$：$\exp\left[x\mu-\frac{x^2}{2}-\frac{\mu^2}{2}-\log\sqrt{2\pi}\right]$。

**$U(0,\theta)$ 不能用 Cramér–Rao、不能用指數族**（範圍依賴 $\theta$）。

---

## 11. 與後續的連結

| 本集觀念 | 下學期（高等統計學）會用到 |
|---|---|
| UMVUE、充分完備 | 更多分配、多參數情形 |
| 統計推論的另外兩條路 | 區間估計、假設檢定（Lec11 預告過） |
| 依機率收斂 | 依分配收斂、中央極限定理 |

---

## 附：本集一句話總結

> **Lehmann–Scheffé：完備充分統計量 $U$ 的不偏函數只有一個（靠完備性），而且任何不偏估計量經 Rao–Blackwell 給定 $U$ 後都變成它、變異數只會更小，所以它就是 UMVUE；實際操作就是找完備充分統計量、算期望值、調常數，例如 $U(0,\theta)$ 的 $\frac{n+1}{n}Y_n$、Bernoulli 與 $N(\mu,1)$ 的 $\bar X$。**

---

*筆記依據「統計學」Lec27 錄影逐字稿（whisper large-v3-turbo，37:16）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
