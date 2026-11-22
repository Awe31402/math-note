---
course: 統計學（數理統計，數學系）
episode: 23
lecture: Lec23
date: 待補
video: https://youtu.be/RwdNY6YhvTk
notes: Hogg 8th ed. Theorem 7.2.1 因子分解定理（p. 422）；§7.7 多參數的充分統計量（Example 7.7.1，p. 447）；§2.3 條件期望值、條件變異數（Theorem 2.3.1，p. 114）
---

# 第 23 集 · Lec23：因子分解定理（⇐）；Poisson 與常態的充分統計量；條件期望值與變異數 [▶ 影片](https://youtu.be/RwdNY6YhvTk)

← 上一集：[22](22-uniform-max-sufficient-factorization-theorem.md) ｜ [總目錄](../README.md) ｜ 下一集：[24](24-conditional-variance-identity-rao-blackwell.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 23 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:10:46，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §2.3、§7.2、§7.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「充分統計量」→「沖溫／充溫統計量」，「反函數」→「法蘭素」，「Jacobian」→「Jakobin／傑克平」，「Poisson」→「普華松／伏松」，「conditional expectation／variance」→「conditional acceptation／valence」，「joint」→「Join／9np」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 因子分解定理：證明（⇐）](#1-因子分解定理證明)
- [2. 例 1：Poisson](#2-例-1poisson)
- [3. 例 2：常態（兩個參數）](#3-例-2常態兩個參數)
- [4. 回顧：為什麼要充分統計量](#4-回顧為什麼要充分統計量)
- [5. 條件期望值](#5-條件期望值)
- [6. 條件變異數](#6-條件變異數)
- [7. 定理：E[E(Y|X)]＝E(Y)；Var(Y)＝E[Var(Y|X)]＋Var[E(Y|X)]](#7-定理eeyxeyvaryevaryxvareyx)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 因子分解定理（⇐ 方向） | Theorem 7.2.1，p. 422 |
| Poisson 的 $\sum X_i$、$\bar X$；常態的 $(\bar X,S^2)$ | §7.2、Example 7.7.1，p. 447 |
| 條件期望值、條件變異數 | §2.3，Theorem 2.3.1，p. 114 |

---

## 1. 因子分解定理：證明（⇐）

[▶ 00:30](https://youtu.be/RwdNY6YhvTk?t=30) 複習：$U$ 充分 ⇔ $f(\mathbf x;\theta)=k_1(u(\mathbf x);\theta)k_2(\mathbf x)$，$k_2$ 不含 $\theta$。上次證了 ⇒，今天證 ⇐（假設連續型）。

**假設**：joint pdf 能拆成 $k_1(u(\mathbf x);\theta)k_2(\mathbf x)$。**要證**：給定 $U=y_1$，樣本的條件 pdf 不含 $\theta$。

**Step 1：補變數做一對一變換**（[▶ 06:10](https://youtu.be/RwdNY6YhvTk?t=370)）

- 令 $Y_1=u(X_1,\dots,X_n)$（就是 $U$）。只有一個，要再造 $n-1$ 個：$Y_2=u_2(\mathbf X),\dots,Y_n=u_n(\mathbf X)$，讓 $(Y_1,\dots,Y_n)$ 和 $(X_1,\dots,X_n)$ **一對一**。
- 反函數：$x_i=w_i(y_1,\dots,y_n)$。
- Jacobian $J=\det[\partial x_i/\partial y_j]$。

[▶ 09:15](https://youtu.be/RwdNY6YhvTk?t=555) **$J$ 不含 $\theta$**：$Y_i$ 都是統計量（不含 $\theta$），反函數也不含，微分後還是不含。

**Step 2：$Y$ 的 joint pdf**（[▶ 10:16](https://youtu.be/RwdNY6YhvTk?t=616)）。變換公式，再代入假設的分解（$u(\mathbf x)$ 就是 $y_1$）：
$$f_{\mathbf Y}(y_1,\dots,y_n)=f(\mathbf w;\theta)|J|=k_1(y_1;\theta)\,k_2(w_1,\dots,w_n)\,|J|.$$

**Step 3：$U=Y_1$ 的 marginal pdf**（[▶ 13:24](https://youtu.be/RwdNY6YhvTk?t=804)）。把 $y_2,\dots,y_n$ 積掉；$k_1$ 只和 $y_1$ 有關，提出來：
$$f_U(y_1;\theta)=k_1(y_1;\theta)\underbrace{\int\!\cdots\!\int k_2(w_1,\dots,w_n)|J|\,dy_2\cdots dy_n}_{\text{只和 }y_1\text{ 有關，不含 }\theta}.$$
（$k_2$、$|J|$ 都不含 $\theta$，積掉 $y_2,\dots,y_n$ 後只剩 $y_1$。）

**Step 4：條件 pdf**（[▶ 14:57](https://youtu.be/RwdNY6YhvTk?t=897)）。給定 $U=y_1$，分子是樣本 joint pdf，分母是 $U$ 的 pdf：
$$f(\mathbf x\mid U=y_1)=\frac{k_1(y_1;\theta)k_2(\mathbf x)}{k_1(y_1;\theta)\int\cdots\int k_2|J|\,dy_2\cdots dy_n}=\frac{k_2(\mathbf x)}{\int\cdots\int k_2|J|\,dy_2\cdots dy_n}.$$
$k_1$ 消掉，剩下的都不含 $\theta$ ⇒ $U$ 充分。∎

[▶ 21:40](https://youtu.be/RwdNY6YhvTk?t=1300) 【口頭】觀念清楚就知道怎麼做。以後驗證充分統計量，**只要把 joint pdf 拆**。$k_2$ 找不到也沒關係，當作 1（1 也是 $\mathbf x$ 的函數）。

---

## 2. 例 1：Poisson

[▶ 22:47](https://youtu.be/RwdNY6YhvTk?t=1367) $X_1,\dots,X_n$ iid Poisson$(\lambda)$。

**joint pdf**（[▶ 23:18](https://youtu.be/RwdNY6YhvTk?t=1398)）：
$$f(\mathbf x;\lambda)=\prod_{i=1}^n\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}=\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}.$$

**拆法 1**（[▶ 25:22](https://youtu.be/RwdNY6YhvTk?t=1522)）：
$$f=\underbrace{\lambda^{\sum x_i}e^{-n\lambda}}_{k_1(\sum x_i;\lambda)}\cdot\underbrace{\frac{1}{\prod x_i!}}_{k_2(\mathbf x)}\ \Rightarrow\ \sum X_i\text{ 是 }\lambda\text{ 的充分統計量}.$$

[▶ 26:55](https://youtu.be/RwdNY6YhvTk?t=1615) 比用定義簡單多了：用定義要先找 $\sum X_i$ 的分配，再算條件 pdf。

**拆法 2**（[▶ 27:26](https://youtu.be/RwdNY6YhvTk?t=1646)）：$\sum x_i=n\bar x$，
$$f=\lambda^{n\bar x}e^{-n\lambda}\cdot\frac{1}{\prod x_i!}\ \Rightarrow\ \bar X\text{ 也是充分統計量}.$$

**拆法 3**（[▶ 29:42](https://youtu.be/RwdNY6YhvTk?t=1782)）：Poisson 的值非負，$\bar x\ge 0$，所以 $\bar x=(\bar x^2)^{1/2}$：
$$f=\lambda^{n(\bar x^2)^{1/2}}e^{-n\lambda}\cdot\frac{1}{\prod x_i!}\ \Rightarrow\ \bar X^2\text{ 也是充分統計量}.$$

[▶ 30:47](https://youtu.be/RwdNY6YhvTk?t=1847) 充分統計量可以有很多個，只要拆得出來就是。

---

## 3. 例 2：常態（兩個參數）

[▶ 31:24](https://youtu.be/RwdNY6YhvTk?t=1884) $X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$，$\mu,\sigma^2$ 都未知。希望拆成**兩個**統計量。

**joint pdf**（[▶ 32:55](https://youtu.be/RwdNY6YhvTk?t=1975)）：
$$f(\mathbf x;\mu,\sigma^2)=(2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp\left[-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2\right].$$

**笨拆法**（[▶ 34:33](https://youtu.be/RwdNY6YhvTk?t=2073)）：整個當 $k_1(x_1,\dots,x_n;\mu,\sigma^2)$，$k_2=1$ ⇒ 樣本本身是充分的（Lec21 證過）。但它是 $n$ 維，不好。

**好拆法**（[▶ 36:44](https://youtu.be/RwdNY6YhvTk?t=2204)）：只能動指數裡的 $\sum(x_i-\mu)^2$。加減 $\bar x$：
$$\sum(x_i-\mu)^2=\sum(x_i-\bar x)^2+n(\bar x-\mu)^2+2(\bar x-\mu)\underbrace{\sum(x_i-\bar x)}_{0}=(n-1)s^2+n(\bar x-\mu)^2.$$
（$s^2=\frac{1}{n-1}\sum(x_i-\bar x)^2$。）

代回（[▶ 38:56](https://youtu.be/RwdNY6YhvTk?t=2336)）：
$$f=\underbrace{(2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp\left[-\frac{(n-1)s^2+n(\bar x-\mu)^2}{2\sigma^2}\right]}_{k_1(\bar x,s^2;\mu,\sigma^2)}\cdot\underbrace{1}_{k_2}.$$

- $k_1$ 裡的統計量只有 $\bar x$、$s^2$；$n$ 是樣本數、$\mu,\sigma^2$ 是參數。
- $(2\pi)^{-n/2}$ 放 $k_1$ 或 $k_2$ 都可以。

⇒ $(\bar X,S^2)$ 是 $(\mu,\sigma^2)$ 的充分統計量，**二維**（比樣本的 $n$ 維小很多）。

---

## 4. 回顧：為什麼要充分統計量

[▶ 41:41](https://youtu.be/RwdNY6YhvTk?t=2501)

- 統計問題：樣本來自 $f(x;\theta)$，$\theta$ 未知，想了解 $\theta$。
- 統計推論三個方向：點估計（目前在講）＋兩個還沒講的。
- [▶ 43:47](https://youtu.be/RwdNY6YhvTk?t=2627) 找估計量的方法：動差法、MLE，都不保證最好。「最好」＝UMVUE。
- [▶ 44:17](https://youtu.be/RwdNY6YhvTk?t=2657) Cramér–Rao：不偏估計量的變異數 $\ge$ 下界，達到就是 UMVUE。但常常不知道哪個估計量達得到，無法驗證。
- [▶ 45:18](https://youtu.be/RwdNY6YhvTk?t=2718) 需要更一般的方法 → **充分統計量**在找 UMVUE 的過程扮演很重要的角色。先要一些理論：條件期望值。

---

## 5. 條件期望值

[▶ 45:48](https://youtu.be/RwdNY6YhvTk?t=2748) 複習：

- marginal：$f_X(x)=\int f(x,y)\,dy$，$f_Y(y)=\int f(x,y)\,dx$。
- conditional：$f(y\mid x)=\frac{f(x,y)}{f_X(x)}$，所以 $f(x,y)=f(y\mid x)f_X(x)=f(x\mid y)f_Y(y)$。
- 期望值 $E(Y)=\int yf_Y(y)\,dy$；變異數 $\text{Var}(Y)=E[(Y-EY)^2]=E(Y^2)-(EY)^2$。

> **條件期望值**（conditional expectation，[▶ 49:53](https://youtu.be/RwdNY6YhvTk?t=2993)）：已知 $X=x$，$Y$ 的期望值
> $$E(Y\mid X=x)=\int_{-\infty}^{\infty}y\,f(y\mid x)\,dy.$$

【口頭】[▶ 50:26](https://youtu.be/RwdNY6YhvTk?t=3026) 例：題目有時簡單有時難，兩個同學一起考，一個高另一個通常也高。已知甲考 $x$ 分，乙的平均（期望值）是多少？

- $y$ 改小寫，乘的是**條件 pdf** $f(y\mid x)$（因為 $X=x$ 已經發生）。
- [▶ 51:59](https://youtu.be/RwdNY6YhvTk?t=3119) 積掉 $y$ 後，結果是 $x$ 的函數；$x$ 是給定的，所以它是**常數**，不是隨機變數。

**$E(Y\mid X)$**（[▶ 52:29](https://youtu.be/RwdNY6YhvTk?t=3149)）：先算 $E(Y\mid X=x)$（$x$ 的函數），再把小寫 $x$ 換成大寫 $X$。

- 它是 $X$ 的函數，所以是**隨機變數**。
- 【口頭】這不容易了解，要慢慢想清楚這個過程。

---

## 6. 條件變異數

[▶ 55:07](https://youtu.be/RwdNY6YhvTk?t=3307)

> **條件變異數**（conditional variance）：
> $$\text{Var}(Y\mid X=x)=E\left[\left(Y-E(Y\mid x)\right)^2\,\middle|\,X=x\right]=\int\left(y-E(Y\mid x)\right)^2f(y\mid x)\,dy.$$

- 隨機變數減掉**條件**期望值、平方、再取**條件**期望值。
- $E(Y\mid x)$ 裡的 $Y$ 不能改小寫，因為已經取過期望值、是常數。
- [▶ 57:41](https://youtu.be/RwdNY6YhvTk?t=3461) 同樣有捷徑：$\text{Var}(Y\mid x)=E(Y^2\mid x)-[E(Y\mid x)]^2$。

**$\text{Var}(Y\mid X)$**（[▶ 58:42](https://youtu.be/RwdNY6YhvTk?t=3522)）：先算 $\text{Var}(Y\mid X=x)$，再把 $x$ 換成 $X$。$Y$ 已經積掉，只剩 $X$ 的函數，是隨機變數。

---

## 7. 定理：E[E(Y|X)]＝E(Y)；Var(Y)＝E[Var(Y|X)]＋Var[E(Y|X)]

[▶ 59:42](https://youtu.be/RwdNY6YhvTk?t=3582) 【口頭】要從條件 pdf 一步一步看下來，花點時間理解。這些定理在統計裡很重要。

> **定理**（課本 Theorem 2.3.1，p. 114）：
> (a) $E\left[E(Y\mid X)\right]=E(Y)$。「條件期望值的期望值等於期望值。」
> (b) $\text{Var}(Y)=E\left[\text{Var}(Y\mid X)\right]+\text{Var}\left[E(Y\mid X)\right]$。

[▶ 62:48](https://youtu.be/RwdNY6YhvTk?t=3768) **(b) 的意義**：兩項都 $\ge 0$，所以
$$\text{Var}\left[E(Y\mid X)\right]\le\text{Var}(Y).$$
【口頭】最後要用的就是這個：條件期望值的變異數一定比原本的變異數小。

**證明 (a)**（[▶ 65:05](https://youtu.be/RwdNY6YhvTk?t=3905)）

1. **規則**：$X$ 的函數 $g(X)$ 取期望值＝$\int g(x)f_X(x)\,dx$。
2. $E(Y\mid X)$ 是 $X$ 的函數，所以
$$E[E(Y\mid X)]=\int E(Y\mid x)f_X(x)\,dx=\int\left[\int yf(y\mid x)\,dy\right]f_X(x)\,dx.$$
3. [▶ 68:09](https://youtu.be/RwdNY6YhvTk?t=4089) $f(y\mid x)f_X(x)=f(x,y)$（joint pdf）：
$$=\iint y\,f(x,y)\,dy\,dx.$$
4. 交換積分順序，先積 $x$：$\int f(x,y)\,dx=f_Y(y)$：
$$=\int y\left[\int f(x,y)\,dx\right]dy=\int yf_Y(y)\,dy=E(Y).\qquad\blacksquare$$

(b) 老師這集沒證。

[▶ 70:13](https://youtu.be/RwdNY6YhvTk?t=4213) 【口頭】整個過程要自己練習，一步一步都清楚就了解了。

---

## 8. 一頁速查表

**因子分解定理（⇐）證明關鍵**：補 $Y_2,\dots,Y_n$ 一對一 → $f_{\mathbf Y}=k_1(y_1;\theta)k_2(\mathbf w)|J|$ → $f_U=k_1\cdot(\text{不含 }\theta)$ → 條件 pdf 中 $k_1$ 消掉。

**例子**

| 分配 | 拆法 | 充分統計量 |
|---|---|---|
| Poisson$(\lambda)$ | $\lambda^{\sum x_i}e^{-n\lambda}\cdot\frac{1}{\prod x_i!}$ | $\sum X_i$（也可以 $\bar X$、$\bar X^2$） |
| $N(\mu,\sigma^2)$ | $\sum(x_i-\mu)^2=(n-1)s^2+n(\bar x-\mu)^2$ | $(\bar X,S^2)$ |

充分統計量不唯一，維度越小越好。

**條件期望值、變異數**

- $E(Y\mid X=x)=\int yf(y\mid x)\,dy$（常數）；換成 $X$ 得 $E(Y\mid X)$（隨機變數）。
- $\text{Var}(Y\mid x)=E[(Y-E(Y\mid x))^2\mid x]=E(Y^2\mid x)-[E(Y\mid x)]^2$。

**定理**

- $E[E(Y\mid X)]=E(Y)$。關鍵：$f(y\mid x)f_X(x)=f(x,y)$，交換積分順序。
- $\text{Var}(Y)=E[\text{Var}(Y\mid X)]+\text{Var}[E(Y\mid X)]$ ⇒ $\text{Var}[E(Y\mid X)]\le\text{Var}(Y)$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| (b) 的證明 | 下一集 |
| $\text{Var}[E(Y\mid X)]\le\text{Var}(Y)$ | Rao–Blackwell：給定充分統計量取條件期望值，變異數變小 |
| 充分統計量 | 找 UMVUE |

---

## 附：本集一句話總結

> **因子分解定理的 ⇐ 方向用一對一變換證明：$k_1$ 在條件 pdf 中被消掉；用它很快得到 Poisson 的 $\sum X_i$、常態的 $(\bar X,S^2)$ 是充分統計量；接著定義條件期望值、條件變異數，並證明 $E[E(Y\mid X)]=E(Y)$、$\text{Var}(Y)=E[\text{Var}(Y\mid X)]+\text{Var}[E(Y\mid X)]$。**

---

*筆記依據「統計學」Lec23 錄影逐字稿（whisper large-v3-turbo，1:10:46）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
