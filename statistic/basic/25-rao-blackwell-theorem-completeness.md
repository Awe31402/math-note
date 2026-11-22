---
course: 統計學（數理統計，數學系）
episode: 25
lecture: Lec25
date: 待補
video: https://youtu.be/LVkm7XMBwsE
notes: Hogg 8th ed. §7.3 Rao–Blackwell 定理（Theorem 7.3.1，p. 427）；§7.4 完備性（Definition 7.4.1，p. 431；Example 7.4.1，p. 432）
---

# 第 25 集 · Lec25：Rao–Blackwell 定理；完備統計量（Bernoulli 例） [▶ 影片](https://youtu.be/LVkm7XMBwsE)

← 上一集：[24](24-conditional-variance-identity-rao-blackwell.md) ｜ [總目錄](../README.md) ｜ 下一集：[26](26-uniform-max-complete-exponential-family-lehmann-scheffe.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 25 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（47:09，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §7.3、§7.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Rao–Blackwell」→「Robbio／Raw-Blackwell」，「充分統計量」→「充溫／聪温統計量」，「Cramér–Rao lower bound」→「Colomarolobomb」，「complete」→「完備」，「Bernoulli」→「Banuni／本能力」，「二項」→「偶向」，「互斥」→「互次」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要「充分」：條件期望值是否含 θ](#1-為什麼要充分條件期望值是否含-θ)
- [2. Rao–Blackwell 定理](#2-raoblackwell-定理)
- [3. 一直改善下去？](#3-一直改善下去)
- [4. 函數為 0 ⇒ 期望值為 0，反過來呢？](#4-函數為-0--期望值為-0反過來呢)
- [5. 完備統計量的定義](#5-完備統計量的定義)
- [6. 怎麼證完備、怎麼證不完備](#6-怎麼證完備怎麼證不完備)
- [7. 例 1：Bernoulli 的 ΣXᵢ 是完備的](#7-例-1bernoulli-的-σxᵢ-是完備的)
- [8. 例 2：X₁−X₂ 不是完備的](#8-例-2x₁x₂-不是完備的)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Rao–Blackwell 定理 | Theorem 7.3.1，p. 427 |
| 完備統計量（complete statistic） | Definition 7.4.1，p. 431 |
| Bernoulli：$\sum X_i$ 完備；$X_1-X_2$ 不完備 | §7.4 |

---

## 1. 為什麼要「充分」：條件期望值是否含 θ

[▶ 01:03](https://youtu.be/LVkm7XMBwsE?t=63) $U$ 是統計量。給定 $U=u$ 時，樣本的條件 pdf $f(\mathbf x\mid U=u;\theta)$：

| $U$ | 條件 pdf 是…的函數 |
|---|---|
| 充分 | 只有 $x_1,\dots,x_n$ |
| 不充分 | $x_1,\dots,x_n$ **和 $\theta$** |

[▶ 05:46](https://youtu.be/LVkm7XMBwsE?t=346) 要估 $\tau(\theta)$，$\hat\tau(X_1,\dots,X_n)$ 是估計量。條件期望值：
$$E(\hat\tau\mid U=u)=\int\!\cdots\!\int\hat\tau(\mathbf x)\,f(\mathbf x\mid U=u;\theta)\,d\mathbf x.$$

- [▶ 07:49](https://youtu.be/LVkm7XMBwsE?t=469) 積掉 $\mathbf x$ 後剩下 $u$，一定是 $u$ 的函數。問題是有沒有 $\theta$。
- **$U$ 不充分**：條件 pdf 含 $\theta$ ⇒ 結果是 $u$ 和 $\theta$ 的函數。換成大寫 $U$ 後，雖然還是 $X_1,\dots,X_n$ 的函數（因為 $U$ 是），但含 $\theta$，**不是統計量**，不能當估計量。上次說它「不偏」，但不是估計量。
- **$U$ 充分**：條件 pdf 不含 $\theta$ ⇒ 結果只是 $u$ 的函數 ⇒ 換成 $U$ 後是**統計量**，可以當估計量。

---

## 2. Rao–Blackwell 定理

[▶ 12:26](https://youtu.be/LVkm7XMBwsE?t=746)

> **Rao–Blackwell 定理**（課本 Theorem 7.3.1，p. 427）：$\hat\tau$ 是 $\tau(\theta)$ 的不偏估計量，$U$ 是**充分**統計量，則
> 1. $E(\hat\tau\mid U)$ 是**統計量**；
> 2. 它是 $\tau(\theta)$ 的**不偏估計量**；
> 3. $\text{Var}\left[E(\hat\tau\mid U)\right]\le\text{Var}(\hat\tau)$。

**為什麼**：

1. 統計量：§1，$U$ 充分 ⇒ 條件 pdf 不含 $\theta$。
2. 不偏：上一集，$E[E(\hat\tau\mid U)]=E(\hat\tau)=\tau(\theta)$。統計量＋不偏 ⇒ 不偏**估計量**。
3. 變異數變小：上一集。

[▶ 14:58](https://youtu.be/LVkm7XMBwsE?t=898) 意思：任何一個不偏估計量都能**改善**。只要找到一個充分統計量，給定它取條件期望值，得到的仍是不偏估計量，而且變異數更小。

---

## 3. 一直改善下去？

[▶ 15:59](https://youtu.be/LVkm7XMBwsE?t=959) 有一個不偏估計量 $\hat\tau$，還有很多充分統計量 $U_1,U_2,U_3,\dots$：

$$\hat\tau\ \to\ E(\hat\tau\mid U_1)\ \to\ E\left[E(\hat\tau\mid U_1)\mid U_2\right]\ \to\ \cdots$$

- 每一步都是不偏估計量，變異數一直變小（[▶ 17:02](https://youtu.be/LVkm7XMBwsE?t=1022)）。
- [▶ 18:35](https://youtu.be/LVkm7XMBwsE?t=1115) 問題：變異數會不會收斂到 Cramér–Rao 下界？收斂到就是 UMVUE。
- [▶ 19:06](https://youtu.be/LVkm7XMBwsE?t=1146) 可以，但要條件：**不用找一堆 $U$**。只要找到一種充分統計量，再滿足一個條件，做**一步**就已經最好。這個條件叫**完備**（complete）。

---

## 4. 函數為 0 ⇒ 期望值為 0，反過來呢？

[▶ 19:36](https://youtu.be/LVkm7XMBwsE?t=1176) 複習期望值：離散 $E(X)=\sum xf(x)$，連續 $E(X)=\int xf(x)\,dx$。

$U$ 是統計量，$h(U)$ 是 $U$ 的函數。

**情形 1**（[▶ 20:38](https://youtu.be/LVkm7XMBwsE?t=1238)）：$h(U)\equiv 0$。常數的期望值是常數 ⇒ $E[h(U)]=0$，不管 $\theta$。

**情形 2**（[▶ 21:38](https://youtu.be/LVkm7XMBwsE?t=1298)）：$h(U)$ 不一定恆為 0，但 $P_\theta(h(U)=0)=1$（其他值沒有機率）。令 $H=h(U)$：

- $H$ 只在 0 有機率，所以是離散的：$f_H(0)=1$，其他點 $f_H=0$。
- $E(H)=0\cdot 1+\sum_{h\ne 0}h\cdot 0=0$。

所以：
$$h(U)=0\text{ 或 }P_\theta(h(U)=0)=1\ \Rightarrow\ E_\theta[h(U)]=0.$$

**反過來**（[▶ 24:14](https://youtu.be/LVkm7XMBwsE?t=1454)）：如果 $E_\theta[h(U)]\equiv 0$（對所有 $\theta$），能不能推出 $P_\theta(h(U)=0)=1$？**不一定**。

---

## 5. 完備統計量的定義

[▶ 25:18](https://youtu.be/LVkm7XMBwsE?t=1518)

> **定義（完備統計量，complete statistic）**（課本 Definition 7.4.1，p. 431）：統計量 $U$ 若對 $U$ 的**任何**函數 $h$，
> $$E_\theta[h(U)]=0\quad\forall\theta\in\Omega\ \Longrightarrow\ P_\theta(h(U)=0)=1\quad\forall\theta\in\Omega,$$
> 就叫完備統計量。

- 白話：任何一個函數，只要期望值對所有 $\theta$ 都是 0，這個函數本來就是 0（機率 1）。
- 不是所有統計量都滿足。

【口頭】[▶ 27:19](https://youtu.be/LVkm7XMBwsE?t=1639) 這觀念有點抽象，但在統計上很重要。我們需要的不只是充分統計量，而是**完備充分統計量**，它有很多好處。

---

## 6. 怎麼證完備、怎麼證不完備

[▶ 27:54](https://youtu.be/LVkm7XMBwsE?t=1674)

| 要證 | 要做的事 | 難度 |
|---|---|---|
| **完備** | 對**任意**函數 $h$：設 $E_\theta[h(U)]\equiv 0$，推出 $P_\theta(h(U)=0)\equiv 1$ | 比較難 |
| **不完備** | 找**一個**函數 $h$：$E_\theta[h(U)]\equiv 0$，但對**某些** $\theta$，$P_\theta(h(U)=0)<1$ | 比較簡單 |

【口頭】[▶ 28:56](https://youtu.be/LVkm7XMBwsE?t=1736) 就像微積分：證明函數連續要證定義域裡每一點都連續，比較難；證明不連續只要找到一點不連續就好。

---

## 7. 例 1：Bernoulli 的 ΣXᵢ 是完備的

[▶ 29:56](https://youtu.be/LVkm7XMBwsE?t=1796) $X_1,\dots,X_n$ iid Bernoulli$(p)$，$Y=\sum X_i\sim b(n,p)$。已知 $Y$ 是充分統計量，現在證它**完備**。參數空間 $0<p<1$。

**Step 1：假設**（[▶ 31:31](https://youtu.be/LVkm7XMBwsE?t=1891)）。任意函數 $h$，設
$$0=E_p[h(Y)]=\sum_{y=0}^nh(y)\binom ny p^y(1-p)^{n-y},\qquad\forall p\in(0,1).$$

**Step 2：提出 $(1-p)^n$**（[▶ 35:07](https://youtu.be/LVkm7XMBwsE?t=2107)）。$(1-p)^{n-y}=(1-p)^n(1-p)^{-y}$：
$$0=(1-p)^n\sum_{y=0}^nh(y)\binom ny\left(\frac{p}{1-p}\right)^y.$$
$0<p<1$ ⇒ $(1-p)^n>0$，所以等價於
$$0=\sum_{y=0}^nh(y)\binom ny\left(\frac{p}{1-p}\right)^y.$$

**Step 3：換參數**（[▶ 36:08](https://youtu.be/LVkm7XMBwsE?t=2168)）。令 $\theta=\frac{p}{1-p}$。$p\to 0$ 時 $\theta\to 0$；$p\to 1$ 時 $\theta\to\infty$。所以 $\theta\in(0,\infty)$：
$$0=\sum_{y=0}^n\left[h(y)\binom ny\right]\theta^y,\qquad\forall\theta\in(0,\infty).$$

**Step 4：多項式恆為 0 ⇒ 係數全為 0**（[▶ 37:10](https://youtu.be/LVkm7XMBwsE?t=2230)）

- 右邊是 $\theta$ 的 $n$ 次多項式，係數是 $h(y)\binom ny$。
- 令它等於 0 是一個方程式，只會有**有限**個解。
- 但這裡要對 $(0,\infty)$ 裡**不可數**多個 $\theta$ 都成立 ⇒ 只能是所有係數都是 0：
$$h(y)\binom ny=0,\qquad y=0,1,\dots,n.$$
- $\binom ny>0$ ⇒ $h(y)=0$，$y=0,1,\dots,n$。

**Step 5：機率是 1**（[▶ 39:46](https://youtu.be/LVkm7XMBwsE?t=2386)）
$$1\ge P_p(h(Y)=0)\ge P_p(Y\in\{0,1,\dots,n\})=\sum_{y=0}^n\binom ny p^y(1-p)^{n-y}=1.$$
（$h$ 在 $0,\dots,n$ 上都是 0；$Y$ 只會落在 $0,\dots,n$。）夾在兩個 1 中間 ⇒ $P_p(h(Y)=0)=1$，對所有 $p$。

所以 $Y=\sum X_i$ 是**完備**的。∎

[▶ 41:18](https://youtu.be/LVkm7XMBwsE?t=2478) 【口頭】這個例子用這種方法，不同例子證法都不一樣，所以證完備其實蠻困難的。

---

## 8. 例 2：X₁−X₂ 不是完備的

[▶ 41:48](https://youtu.be/LVkm7XMBwsE?t=2508) 同樣 $X_i$ iid Bernoulli$(p)$。$Z=X_1-X_2$ 也是統計量（只用到 $X_1,X_2$，裡面沒有參數）。證它**不**完備。

**找一個函數**（[▶ 43:20](https://youtu.be/LVkm7XMBwsE?t=2600)）：$h(Z)=Z$ 自己。

**期望值恆為 0**：$E_p(Z)=E(X_1)-E(X_2)=p-p=0$，對所有 $p$。

**但機率不是 1**（[▶ 44:21](https://youtu.be/LVkm7XMBwsE?t=2661)）：$X_i\in\{0,1\}$，$X_1-X_2=0$ ⇔ 兩個都 0 或兩個都 1（互斥），再用獨立：
$$P_p(Z=0)=P(X_1=0)P(X_2=0)+P(X_1=1)P(X_2=1)=(1-p)^2+p^2.$$
$0<p<1$ 時 $(1-p)^2+p^2<1$。

（驗算，不是逐字稿內容：$(1-p)^2+p^2=1-2p(1-p)<1$，因為 $p(1-p)>0$。）

找到一個函數期望值恆為 0、但等於 0 的機率 $<1$ ⇒ $Z$ **不是**完備的。（其實只要找到某些 $p$ 讓它 $<1$ 就夠，這裡所有 $p$ 都 $<1$。）

---

## 9. 一頁速查表

**Rao–Blackwell**：$\hat\tau$ 不偏、$U$ 充分 ⇒ $E(\hat\tau\mid U)$ 是不偏**估計量**，且 $\text{Var}[E(\hat\tau\mid U)]\le\text{Var}(\hat\tau)$。

關鍵：$U$ 充分 ⇒ 條件 pdf 不含 $\theta$ ⇒ 條件期望值不含 $\theta$ ⇒ 是統計量。

**完備**：
$$E_\theta[h(U)]\equiv 0\ \Rightarrow\ P_\theta(h(U)=0)\equiv 1,\quad\text{對任意 }h.$$
（反方向永遠成立。）

| 例（Bernoulli） | 完備？ | 關鍵一步 |
|---|---|---|
| $Y=\sum X_i$ | ✓ | $\sum h(y)\binom ny\theta^y\equiv 0$ 對 $\theta\in(0,\infty)$ ⇒ 係數全 0 |
| $Z=X_1-X_2$ | ✗ | $E(Z)=0$ 但 $P(Z=0)=(1-p)^2+p^2<1$ |

**證明策略**：完備要對所有 $h$；不完備找一個反例。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 完備充分統計量 | 下一集：Lehmann–Scheffé 定理，一步得到 UMVUE |
| Rao–Blackwell | 從任何不偏估計量出發改善 |
| 完備性的例子 | 更多分配（Poisson、常態等） |

---

## 附：本集一句話總結

> **只有給定充分統計量時，條件期望值才不含 $\theta$，所以 Rao–Blackwell 說：不偏估計量給定充分統計量取條件期望值，仍是不偏估計量且變異數更小；若這個充分統計量還是「完備」的（期望值恆為 0 的函數必恆為 0），一步就能得到最好的估計量；Bernoulli 的 $\sum X_i$ 完備，$X_1-X_2$ 不完備。**

---

*筆記依據「統計學」Lec25 錄影逐字稿（whisper large-v3-turbo，47:09）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
