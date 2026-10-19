---
course: Abstract Algebra II (Spring 2026)
episode: 23
lecture: L20
date: 2026-03-09
video: https://www.youtube.com/watch?v=Ye9Sf63TTmc
notes: 講義/AA2/Math422_Lecture20_CyclotomicExtensions.pdf
---

# 第 23 集 · L20：分圓體、Galois 理論開始 [▶ 影片](https://www.youtube.com/watch?v=Ye9Sf63TTmc&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[22-L19-可分擴張]] ｜ [總目錄](../README.md) ｜ 下一集：[[24-L21-Galois擴張與Galois群]] →

## 本集概要

D&F §13.6：
- $x^n-1$ 的根是 $n$ 次單位根 $\zeta_n^k$，**沒有重根**；$\mu_n$ 是群；$\mathbb{Q}(\zeta_n)$ 是 $x^n-1$ 的分裂體——**分圓體**。
- 目標：$[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$。$n = p$ 質數時已證（$\Phi_p$ 不可約）。
- **分圓多項式** $\Phi_n$：根是**本原** $n$ 次單位根。逐一算 $\Phi_1$ 到 $\Phi_{12}$；$x^n-1 = \prod_{d\mid n}\Phi_d(x)$；$n = \sum_{d\mid n}\varphi(d)$。
- $\Phi_n\in\mathbb{Z}[x]$、不可約（不證）。$\mathbb{Q}(\zeta_8)$、$\mathbb{Q}(\zeta_3) = \mathbb{Q}(i\sqrt3)$；$x^p-2$ 分裂體次數 $p(p-1)$。
- 開始 Galois 理論：Galois（1811–1832）死於決鬥；最後放了一支 Galois 生平的歌。

> 📘 講義對應：Math422 Lecture 20「Cyclotomic Extensions」；D&F §13.6（Lemma 40、Thm 41）。

---

## 筆記

### 1. $x^n-1$ 的分解 [▶ 01:00](https://youtu.be/Ye9Sf63TTmc?t=60)

（開場：學生說「加分」；老師擦掉另一堂課的三角函數。）

- $e^{i\theta} = 1\iff\theta\in2\pi\mathbb{Z}$。$(e^{i\theta})^n = 1\iff\theta = 2\pi k/n$。所以 $\zeta_n^k$（$\zeta_n = e^{2\pi i/n}$，**本原 $n$ 次單位根**）都是 $x^n-1$ 的根 [▶ 02:00](https://youtu.be/Ye9Sf63TTmc?t=120)。
- 至多 $n$ 個根。**沒有重根**：$f' = nx^{n-1}$ 只在 0 為零（特徵 0，我們把 $x^n-1$ 看成有理多項式），而 $f(0) = -1\ne0$ [▶ 05:00](https://youtu.be/Ye9Sf63TTmc?t=300)。（學生開玩笑把導數唸錯：「早上剛考過積分，太快了。」）
- 所以 $1,\zeta_n,\dots,\zeta_n^{n-1}$ 相異（複分析記號 $1^{1/n}$；D&F 記 $\mu_n$），
$$x^n-1 = (x-1)(x-\zeta_n)(x-\zeta_n^2)\cdots(x-\zeta_n^{n-1}).$$
- $\mathbb{Q}(\zeta_n)$ 是 $x^n-1$ 的分裂體——第 $n$ 個**分圓體**（cyclotomic field）。只要加 $\zeta_n$：體對乘法封閉，次方自動都在 [▶ 09:00](https://youtu.be/Ye9Sf63TTmc?t=540)。

**$\mu_n$ 是群** [▶ 09:30](https://youtu.be/Ye9Sf63TTmc?t=570)：$\alpha^n = \beta^n = 1\Rightarrow(\alpha\beta)^n = 1$；$\alpha^{-1} = \alpha^{n-1}$，$(\alpha^{n-1})^n = (\alpha^n)^{n-1} = 1$。（老師算反元素卡了一下，「指數律」。）

**小 $n$ 的值** [▶ 14:30](https://youtu.be/Ye9Sf63TTmc?t=870)：$\zeta_1 = 1$、$\zeta_2 = -1$、$\zeta_3 = \frac{-1+i\sqrt3}2$、$\zeta_4 = i$、
$$\zeta_5 = \frac{\sqrt5-1}4+i\,\frac{\sqrt{10+2\sqrt5}}4,$$
$\zeta_6 = \frac{1+i\sqrt3}2$、$\zeta_8 = \frac{\sqrt2+i\sqrt2}2$。（「別叫我證 $\zeta_5$。」$\zeta_7$ 涉及 6 次多項式，很醜所以沒寫。）

### 2. 目標：$[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$ [▶ 16:30](https://youtu.be/Ye9Sf63TTmc?t=990)

- $n = 1,2$ 很蠢（加 1 或 $-1$ 就是 $\mathbb{Q}$）；$n\ge3$ 才有趣。
- $x^n-1 = (x-1)(x^{n-1}+\cdots+x+1)$。**$n = p$ 質數**：$\Phi_p = x^{p-1}+\cdots+1$ 已證不可約（Eisenstein + 平移），是 $\zeta_p$ 的最小多項式，次數 $p-1 = \varphi(p)$。完成 [▶ 18:30](https://youtu.be/Ye9Sf63TTmc?t=1110)。
- 問題在 $n$ 是合數時。（老師改用投影：他花了幾小時把 D&F 沒寫的分解細節寫出來。）

### 3. 分圓多項式 [▶ 24:00](https://youtu.be/Ye9Sf63TTmc?t=1440)

> **定義**：第 $n$ 個**分圓多項式** $\Phi_n(x)$ 是以**本原** $n$ 次單位根為根的多項式：$\Phi_n(x) = \prod(x-\zeta)$，$\zeta$ 取遍本原 $n$ 次單位根（$\zeta_n^k$，$k\in U(n)$）。

- **注意**：$n$ 是合數時 $\Phi_n$ **不再是** $x^{n-1}+\cdots+x+1$。「我以前就因為閱讀理解沒讀懂，搞得很亂。」

**逐一計算** [▶ 25:00](https://youtu.be/Ye9Sf63TTmc?t=1500)
| $n$ | $x^n-1$ 的分解 | $\Phi_n$ |
|---|---|---|
| 1 | $x-1$ | $x-1$ |
| 2 | $(x-1)(x+1)$ | $x+1$ |
| 3 | $(x-1)(x^2+x+1)$ | $x^2+x+1$（根 $\omega,\omega^2$） |
| 4 | $(x-1)(x+1)(x^2+1)$ | $x^2+1$（根 $\pm i$；$U(4) = \{1,3\}$，$i^3 = -i$） |
| 5 | $(x-1)\Phi_5$ | $x^4+x^3+x^2+x+1$ |
| 6 | $(x-1)(x^2+x+1)(x+1)(x^2-x+1)$ | $x^2-x+1$ |
| 8 | $(x^4-1)(x^4+1)$ | $x^4+1$（根 $\zeta_8^{1,3,5,7}$） |
| 12 | $(x^6-1)(x^6+1) = \cdots$ | $x^4-x^2+1$（$U(12) = \{1,5,7,11\}$） |

- 觀察：$x^2-1 = \Phi_1\Phi_2$、$x^4-1 = \Phi_1\Phi_2\Phi_4$——1、2、4 正是 4 的因數。「哇。」（學生的「wow」聽起來很酸。）
- $\Phi_{12}$ 的直接推導：把本原 12 次單位根配成共軛對，乘開時出現 $\cos\frac{5\pi}6$、$\cos\frac\pi6$，化簡不難 [▶ 32:00](https://youtu.be/Ye9Sf63TTmc?t=1920)。另一法：$x^{12}-1$ 除以前面所有因數的 $\Phi_d$——老師試過，乘出 20 項很煩，再用 Wolfram Alpha 驗證長除法。（「代數的 stoner 笑話——在你們出生前的那種。」）

> **一般公式**：$$x^n-1 = \prod_{d\mid n}\Phi_d(x),$$ $d$ 取遍 $n$ 的所有正因數（含 1 和 $n$）[▶ 40:30](https://youtu.be/Ye9Sf63TTmc?t=2430)。

- 學生 Shane 抓到投影片寫錯：原本寫「$n = d_1d_2\cdots d_k$」，但 $1\cdot2\cdot4\ne4$——應該是「$d_1,\dots,d_k$ 是 $n$ 的**所有相異因數**」，不是乘積 [▶ 36:00](https://youtu.be/Ye9Sf63TTmc?t=2160)。
- 證明想法：$d\mid n$ ⇒ $\mu_d\le\mu_n$（$\alpha^d = 1\Rightarrow\alpha^n = (\alpha^d)^m = 1$）；每個 $n$ 次單位根的階 $d$ 整除 $n$，它是本原 $d$ 次單位根。把 $\prod_{\zeta\in\mu_n}(x-\zeta)$ 依階分組 [▶ 39:00](https://youtu.be/Ye9Sf63TTmc?t=2340)。
- 比較次數（$\deg\Phi_d = \varphi(d)$）：
$$n = \sum_{d\mid n}\varphi(d).$$
  例 $n = 12$：$\varphi(1)+\varphi(2)+\varphi(3)+\varphi(4)+\varphi(6)+\varphi(12) = 1+1+2+2+2+4 = 12$ [▶ 42:30](https://youtu.be/Ye9Sf63TTmc?t=2550)。

> **引理**（D&F Lemma 40）：$\Phi_n(x)$ 是 $\mathbb{Z}[x]$ 中次數 $\varphi(n)$ 的首一多項式。

> **定理**（D&F Thm 41）：$\Phi_n(x)$ 在 $\mathbb{Q}$ 上不可約。所以 $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$。

- 證明用到 Frobenius 自同態，不講（「我比較想把時間花在例子上」）。可以直接假設 $\Phi_n$ 不可約，除非題目就是要你證某個特定的 $\Phi_n$ 不可約 [▶ 44:00](https://youtu.be/Ye9Sf63TTmc?t=2640)。

### 4. 例子 [▶ 44:30](https://youtu.be/Ye9Sf63TTmc?t=2670)

- **$\mathbb{Q}(\zeta_8)$**，次數 4：$\zeta_8+\zeta_8^7 = \sqrt2$，所以 $\sqrt2$ 在裡面；再除以 $\sqrt2$ 可看出 $i$ 也在。$\mathbb{Q}(i)$、$\mathbb{Q}(\sqrt2)$ 都是子體，兩者「獨立」，合起來 4 次。
- **$\mathbb{Q}(\zeta_3) = \mathbb{Q}(i\sqrt3)$** [▶ 46:30](https://youtu.be/Ye9Sf63TTmc?t=2790)：$2\zeta_3+1 = i\sqrt3$，所以 $\mathbb{Q}(i\sqrt3)\subseteq\mathbb{Q}(\zeta_3)$；兩者都 2 次，子空間維數相同就相等。
- **$x^p-2$ 的分裂體** [▶ 47:30](https://youtu.be/Ye9Sf63TTmc?t=2850)：$\alpha = \sqrt[p]2$，$\alpha\zeta$（$\zeta\in\mu_p$）是全部 $p$ 個根，所以分裂體是 $\mathbb{Q}(\sqrt[p]2,\zeta_p)$。
  - 兩個子體次數 $p$ 和 $p-1$ 都整除總次數，且互質 ⇒ 總次數至少 $p(p-1)$；又至多 $p(p-1)$。所以 $= p(p-1)$ [▶ 50:00](https://youtu.be/Ye9Sf63TTmc?t=3000)。
  - 推論：$x^p-2$ 在 $\mathbb{Q}(\zeta_p)$ 上**仍然不可約**；$\Phi_p$ 在 $\mathbb{Q}(\sqrt[p]2)$ 上也仍不可約。一般地，擴大基礎體會危及不可約性（$x^2+1$ 在 $\mathbb{C}$ 上就可約了），但這兩個子體「獨立」，所以沒事——而且是從體論免費得到的 [▶ 52:00](https://youtu.be/Ye9Sf63TTmc?t=3120)。

> 💬 老師口誤說「$\mathbb{Q}(\sqrt[p]2)$ 是 2 次擴張」，應是 $p$ 次。

### 5. Galois 理論開始（只剩 4 分鐘）[▶ 54:30](https://youtu.be/Ye9Sf63TTmc?t=3270)

- **Galois**（1811–1832）。學生：「我 21 歲了。」——「別想了，很令人沮喪。不過活到 22 就比他好。」
- 體到自己的同構叫**自同構**（automorphism）；記號從 $\sigma(\alpha)$ 改成 $\sigma\alpha$。
- Galois 怎麼死的？**決鬥**——大概是為了政治或女人（學生：「希望是女人。」）。
- 最後播了一支講 Galois 生平的歌（父親自殺、考試失利、為了一個女孩去決鬥）[▶ 56:30](https://youtu.be/Ye9Sf63TTmc?t=3390)。

> 💬 學生把「男生笨、女生壞」的笑話怪到 Spano 老師頭上（「他的工作就是推廣（generalize）」）[▶ 22:00](https://youtu.be/Ye9Sf63TTmc?t=1320)。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| $n$ 次單位根 | $n$-th roots of unity | §1 |
| 本原單位根 | primitive root of unity | §1 |
| 分圓體 | cyclotomic field | §1 |
| 分圓多項式 | cyclotomic polynomial | §3 |
| 自同構 | automorphism | §5 |

## ⚠️ 待確認清單

（本集無）
