---
course: 統計學（數理統計，數學系）
episode: 13
lecture: Lec13
date: 待補
video: https://youtu.be/HF9dpQSEqPk
notes: Hogg 8th ed. §5.1 依機率收斂（Definition 5.1.1，p. 322）、弱大數法則（Theorem 5.1.1，p. 322）、一致性（Definition 5.1.2，p. 324）；§1.10 Markov 不等式（Theorem 1.10.2，p. 79）、Chebyshev 不等式（Theorem 1.10.3，p. 79）
---

# 第 13 集 · Lec13：依機率收斂、Markov 與 Chebyshev、弱大數法則、一致估計量 [▶ 影片](https://youtu.be/HF9dpQSEqPk)

← 上一集：[12](12-estimator-unbiasedness.md) ｜ [總目錄](../README.md) ｜ 下一集：[14](14-sample-variance-unbiased-consistent-method-of-moments.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 13 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:12:22，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.10、§5.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「收斂」→「縮鏈／縮練／熟練」，「機率收斂」→「肌力縮練／基力修炼」，「Markov」→「Marco」，「Chebyshev」→「chipation」，「弱大數法則」→「RAW／偌大數法則」，「consistent」照錄，「$\epsilon$」→「Epson」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 從數列收斂到隨機變數的收斂](#1-從數列收斂到隨機變數的收斂)
- [2. 依機率收斂](#2-依機率收斂)
- [3. Markov 不等式與 Chebyshev 不等式](#3-markov-不等式與-chebyshev-不等式)
- [4. 定理：(漸近) 不偏 ＋ 變異數 → 0 ⇒ 依機率收斂](#4-定理漸近-不偏--變異數--0--依機率收斂)
- [5. 弱大數法則](#5-弱大數法則)
- [6. 一致估計量](#6-一致估計量)
- [7. 樣本動差收斂到母體動差](#7-樣本動差收斂到母體動差)
- [8. 下一步：S² 是 σ² 的好估計量嗎？](#8-下一步s-是-σ-的好估計量嗎)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 依機率收斂 $X_n\xrightarrow{P}X$ | Definition 5.1.1，p. 322 |
| Markov、Chebyshev 不等式 | Theorem 1.10.2–1.10.3，p. 79 |
| 不偏（或漸近不偏）＋ var→0 ⇒ 依機率收斂 | （課本 §5.1 用 Chebyshev 證 WLLN） |
| 弱大數法則 | Theorem 5.1.1，p. 322 |
| 一致估計量 | Definition 5.1.2，p. 324 |
| 樣本 $k$ 次動差 → 母體 $k$ 次動差 | §5.1 |

[▶ 00:00](https://youtu.be/HF9dpQSEqPk?t=0) 【口頭】很多東西是從微積分延伸出來的。回頭想微積分學那些東西的意義，統計面對的問題有些和微積分一樣。

---

## 1. 從數列收斂到隨機變數的收斂

[▶ 01:01](https://youtu.be/HF9dpQSEqPk?t=61) 微積分：$a_n\to a$ 指

$$\forall\epsilon>0,\ \exists N,\ n>N\Rightarrow|a_n-a|<\epsilon.$$

- 不要求 $a_n=a$，只要求**無窮接近**：你要多接近都可以。
- 【口頭】$\epsilon$ 可以取 $(10^{14})^{-2}$（「一百兆的平方分之一」）那麼小，超過 $N$ 之後 $a_n$ 和 $a$ 的距離比它還小，就當作沒有距離。

[▶ 03:04](https://youtu.be/HF9dpQSEqPk?t=184) 現在的問題：$X_n$ 是**隨機變數**的數列，要收斂到 $X$（$X$ 可以是隨機變數或常數）。

- $X_n$ 是實數函數（$S\to\mathbb{R}$），所以這其實是**函數的數列**。
- [▶ 04:04](https://youtu.be/HF9dpQSEqPk?t=244) 和數學裡函數數列的收斂不同，因為這裡的函數**有機率**。
- 機率裡的收斂有很多種，本課只用兩種。第一種：**依機率收斂**。

---

## 2. 依機率收斂

[▶ 05:04](https://youtu.be/HF9dpQSEqPk?t=304)

> **定義（依機率收斂，convergence in probability）**（課本 Definition 5.1.1，p. 322）：
> $$\forall\epsilon>0,\qquad \lim_{n\to\infty}P\left(|X_n-X|\ge\epsilon\right)=0.$$
> 記作 $X_n\xrightarrow{P}X$。

**等價寫法**（[▶ 07:43](https://youtu.be/HF9dpQSEqPk?t=463)，取補集合）：
$$\lim_{n\to\infty}P\left(|X_n-X|<\epsilon\right)=1.$$
（寫 $>$ 還是 $\ge$ 不影響。）

**意義**（[▶ 06:07](https://youtu.be/HF9dpQSEqPk?t=367)）：

- $\{|X_n-X|\ge\epsilon\}$ 是一個**事件**：樣本空間裡，$X_n(s)$ 和 $X(s)$ 相差比 $\epsilon$ 還大的那些點 $s$。給一個 $n$ 就有一個事件。
- 這些點的機率 → 0：相差超過任意小的數的點「幾乎沒有」。
- 反過來，相差比任意小的數還小的點，機率 → 1：**幾乎是整個樣本空間**（$P(S)=1$）。
- 所以 $X_n$ 和 $X$ 最後幾乎沒有差別。這個「沒有差別」是從**事件的機率**來看的，所以叫 in probability。

【口頭】要感覺這個機率收斂到 0 的意義，從微積分的收斂去對照思考。

---

## 3. Markov 不等式與 Chebyshev 不等式

[▶ 14:27](https://youtu.be/HF9dpQSEqPk?t=867) 機率裡兩個定理（老師說機率課應學過，不會的要回去看）。

> **Markov 不等式**（課本 Theorem 1.10.2，p. 79）：$X\ge 0$，$u>0$，則
> $$P(X\ge u)\le\frac{E(X)}{u}.$$

老師沒證。【課本補充】證明（連續型）：
$$E(X)=\int_0^\infty xf(x)\,dx\ge\int_u^\infty xf(x)\,dx\ge u\int_u^\infty f(x)\,dx=uP(X\ge u).$$

> **Chebyshev 不等式**（[▶ 14:58](https://youtu.be/HF9dpQSEqPk?t=898)，課本 Theorem 1.10.3，p. 79）：$E(X)=\mu$，$\text{Var}(X)=\sigma^2$，$k>0$，則
> $$P(|X-\mu|\ge k)\le\frac{\sigma^2}{k^2}.$$

**證明**（由 Markov，[▶ 15:59](https://youtu.be/HF9dpQSEqPk?t=959)）：

1. $|X-\mu|\ge 0$、$k>0$，兩邊平方：$P(|X-\mu|\ge k)=P\left((X-\mu)^2\ge k^2\right)$。
2. $(X-\mu)^2\ge 0$，用 Markov：$\le\dfrac{E[(X-\mu)^2]}{k^2}=\dfrac{\sigma^2}{k^2}$。

**其他寫法**（[▶ 18:04](https://youtu.be/HF9dpQSEqPk?t=1084)）：

- 補集合：$P(|X-\mu|<k)\ge 1-\dfrac{\sigma^2}{k^2}$。
- 把 $k$ 換成 $k\sigma$：$P(|X-\mu|\ge k\sigma)\le\dfrac{1}{k^2}$。

---

## 4. 定理：(漸近) 不偏 ＋ 變異數 → 0 ⇒ 依機率收斂

[▶ 19:11](https://youtu.be/HF9dpQSEqPk?t=1151) 回到估計：$\hat\theta=\hat\theta(X_1,\dots,X_n)$ 是估計量（隨機變數），$\theta$ 是常數，兩者不可能相等。但至少希望 $\hat\theta\xrightarrow{P}\theta$。

[▶ 22:16](https://youtu.be/HF9dpQSEqPk?t=1336) 需要一個好驗證的條件：

> **定理**：若當 $n\to\infty$，
> 1. $E(\hat\theta)=\theta$（不偏），或 $E(\hat\theta)\to\theta$（**漸近不偏**，asymptotically unbiased）；
> 2. $\text{Var}(\hat\theta)\to 0$；
>
> 則 $\hat\theta\xrightarrow{P}\theta$。

**證明**

**Step 1：均方誤差分解**（[▶ 25:22](https://youtu.be/HF9dpQSEqPk?t=1522)）。加一個減一個 $E(\hat\theta)$：
$$E\left[(\hat\theta-\theta)^2\right]=E\left[\left(\hat\theta-E\hat\theta+E\hat\theta-\theta\right)^2\right].$$
展開成三項：

- $E\left[(\hat\theta-E\hat\theta)^2\right]=\text{Var}(\hat\theta)$（隨機變數減期望值平方再取期望值，就是變異數）。
- $(E\hat\theta-\theta)^2$：$E\hat\theta$ 已是**常數**，常數的期望值是自己。
- 交叉項：$2(E\hat\theta-\theta)\,E\left[\hat\theta-E\hat\theta\right]=2(E\hat\theta-\theta)(E\hat\theta-E\hat\theta)=0$。

$$E\left[(\hat\theta-\theta)^2\right]=\text{Var}(\hat\theta)+\left(E\hat\theta-\theta\right)^2.$$

**Step 2：Markov**（[▶ 29:27](https://youtu.be/HF9dpQSEqPk?t=1767)）。兩邊平方，用 Markov：
$$0\le P\left(|\hat\theta-\theta|\ge\epsilon\right)=P\left((\hat\theta-\theta)^2\ge\epsilon^2\right)\le\frac{E[(\hat\theta-\theta)^2]}{\epsilon^2}=\frac{\text{Var}(\hat\theta)+(E\hat\theta-\theta)^2}{\epsilon^2}.$$

**Step 3：取極限**（[▶ 30:59](https://youtu.be/HF9dpQSEqPk?t=1859)）。$\text{Var}(\hat\theta)\to 0$；$E\hat\theta-\theta\to 0$，平方也 → 0；分母 $\epsilon^2>0$ 和 $n$ 無關。右邊 → 0，左邊 $\ge 0$，夾擠 ⇒ 中間 → 0。∎

【口頭】這個定理非常重要。以後要驗證估計量有沒有依機率收斂到 $\theta$，就驗這兩個條件。

---

## 5. 弱大數法則

[▶ 33:34](https://youtu.be/HF9dpQSEqPk?t=2014) 機率裡很重要的定理：**大數法則**（law of large numbers），有弱的（weak）和強的（strong）。

【口頭】[▶ 34:04](https://youtu.be/HF9dpQSEqPk?t=2044) 清華有位教授一輩子都在做大數法則，做不完；他把第一個兒子取名叫「大數」。一個東西就可以讓你做一輩子。讀書要非常喜歡一個方向，一輩子做那個研究，會做得很有成就、很快樂。人生不能什麼都喜歡，最後要很喜歡一個東西。

**為什麼關心平均數**（[▶ 36:43](https://youtu.be/HF9dpQSEqPk?t=2203)）【口頭】：

- 產品有標準規格（粉筆太硬寫不出、太軟會斷；血壓也有標準值）。
- 每個產品的值都不一樣。如果分配的平均**剛好在標準規格**，大部分產品都在標準附近，是好的；平均偏離標準，大部分產品都不好。
- 班上微積分平均 80，大部分人都好；平均 40，大部分都考不好。

想知道：樣本平均 $\bar X$ 會不會依機率收斂到母體平均 $\mu$？如果會，$n$ 夠大時雖不知道 $\mu$，$\bar X$ 一定和它很接近。

> **弱大數法則**（weak law of large numbers，WLLN）（課本 Theorem 5.1.1，p. 322）：$X_1,\dots,X_n$ 是隨機樣本，mean $\mu$，variance $\sigma^2<\infty$（**有限**），則
> $$\bar X\xrightarrow{P}\mu.$$

（有些隨機變數的變異數是無窮大，那種不行。）

**證明**（[▶ 42:58](https://youtu.be/HF9dpQSEqPk?t=2578)，用 §4 的定理）：

1. **不偏**：$E(\bar X)=\frac1n\sum E(X_i)=\frac1n\cdot n\mu=\mu$。
2. **變異數 → 0**：常數提出來要平方；**獨立**時和的變異數＝變異數的和；**同分配**每個都是 $\sigma^2$：
$$\text{Var}(\bar X)=\frac{1}{n^2}\text{Var}\left(\sum X_i\right)=\frac{1}{n^2}\sum\text{Var}(X_i)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}\to 0.$$
（$\sigma^2$ 有限才行。）

所以 $\bar X\xrightarrow{P}\mu$。∎

---

## 6. 一致估計量

[▶ 46:35](https://youtu.be/HF9dpQSEqPk?t=2795) 【口頭】統計的觀念都是從機率來的；機率讀得好，統計就簡單，統計只是把機率的觀念換個名字。

> **定義（一致估計量，consistent estimator）**（課本 Definition 5.1.2，p. 324）：估計量 $\hat\theta$（和 $n$ 有關）若
> $$\hat\theta\xrightarrow{P}\theta,$$
> 就叫 $\theta$ 的一致估計量；說 $\hat\theta$ 有**一致性**（consistency）。

| 機率名詞 | 統計名詞 |
|---|---|
| $\hat\theta\xrightarrow{P}\theta$ | $\hat\theta$ 是 consistent（一致） |
| — | $E_\theta\hat\theta=\theta$：unbiased（不偏） |

**例：不偏但不一致**（[▶ 50:24](https://youtu.be/HF9dpQSEqPk?t=3024)）：只用 $X_1$ 估 $\mu$。

- $E(X_1)=\mu$ ⇒ 不偏。
- [▶ 51:58](https://youtu.be/HF9dpQSEqPk?t=3118) 但
$$P(|X_1-\mu|\ge\epsilon)=1-P(\mu-\epsilon<X_1<\mu+\epsilon)=1-\int_{\mu-\epsilon}^{\mu+\epsilon}f(x)\,dx.$$
$\epsilon$ 很小時，那一小段的機率 $<1$，所以這是一個 $>0$ 的**常數**，而且**和 $n$ 無關**（只用一個 $X_1$），不會 → 0。
- 所以 $X_1$ **不是**一致估計量。

[▶ 55:04](https://youtu.be/HF9dpQSEqPk?t=3304) 估 $\mu$ 通常用 $\bar X$：不偏、而且由 WLLN 是一致的。

---

## 7. 樣本動差收斂到母體動差

[▶ 56:42](https://youtu.be/HF9dpQSEqPk?t=3402)

> **母體 $k$ 次動差**（population $k$-th moment）：$E_\theta(X^k)=\int x^kf(x;\theta)\,dx$（離散用 $\sum$）。

- 期望值的下標 $\theta$：分配裡有不知道的 $\theta$。
- [▶ 59:47](https://youtu.be/HF9dpQSEqPk?t=3587) 積完 $x$ 就不見了，但 $\theta$ 還在，所以母體動差是 **$\theta$ 的函數**，永遠算不出數字。
- population（母體）：背後我們不知道的那個分配。

> **樣本 $k$ 次動差**（sample $k$-th moment，[▶ 61:21](https://youtu.be/HF9dpQSEqPk?t=3681)）：$\dfrac1n\sum_{i=1}^nX_i^k$。

觀察到樣本後一定算得出來。

> **結論**（[▶ 62:26](https://youtu.be/HF9dpQSEqPk?t=3746)）：若 $\text{Var}(X^k)<\infty$，則
> $$\frac1n\sum_{i=1}^nX_i^k\xrightarrow{P}E_\theta(X^k).$$
> 樣本 $k$ 次動差是母體 $k$ 次動差的一致估計量。

**證明**（[▶ 64:02](https://youtu.be/HF9dpQSEqPk?t=3842)）：

1. $X_1,\dots,X_n$ iid。
2. 各取 $k$ 次方：獨立的各取函數 → 還是獨立；同分配的取**同一個**函數 → 還是同分配。所以 $X_1^k,\dots,X_n^k$ iid，mean $E(X^k)$，variance $\text{Var}(X^k)$。
3. 對 $X_1^k,\dots,X_n^k$ 用 WLLN：它們的平均依機率收斂到它們的 mean。∎

[▶ 68:47](https://youtu.be/HF9dpQSEqPk?t=4127) 這個在很多狀況都會用到。

---

## 8. 下一步：S² 是 σ² 的好估計量嗎？

[▶ 69:22](https://youtu.be/HF9dpQSEqPk?t=4162) 小結：$X_1,\dots,X_n$ iid，mean $\mu$、variance $\sigma^2$（不限常態）。

- $\bar X$ 是 $\mu$ 的**不偏**估計量（$E\bar X=\mu$）。
- $\bar X$ 是 $\mu$ 的**一致**估計量（WLLN）。

估 $\mu$ 用 $\bar X$ 是不錯的。

[▶ 71:26](https://youtu.be/HF9dpQSEqPk?t=4286) 那 $\sigma^2$ 呢？候選：樣本變異數 $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$。它是 $\sigma^2$ 的不偏估計量嗎？一致估計量嗎？下次證明。

---

## 9. 一頁速查表

**依機率收斂**：$X_n\xrightarrow{P}X\iff\forall\epsilon>0,\ P(|X_n-X|\ge\epsilon)\to 0$（等價：$P(|X_n-X|<\epsilon)\to 1$）。

**不等式**

| | 敘述 | 關鍵一步 |
|---|---|---|
| Markov | $X\ge 0\Rightarrow P(X\ge u)\le\frac{E X}{u}$ | $\int_u^\infty xf\ge u\int_u^\infty f$ |
| Chebyshev | $P(\lvert X-\mu\rvert\ge k)\le\frac{\sigma^2}{k^2}$ | 兩邊平方後用 Markov |

**一致性的充分條件**：$E\hat\theta\to\theta$ 且 $\text{Var}\hat\theta\to 0$ ⇒ $\hat\theta\xrightarrow{P}\theta$。

關鍵一步：$E(\hat\theta-\theta)^2=\text{Var}(\hat\theta)+(E\hat\theta-\theta)^2$，再用 Markov。

**WLLN**：iid、$\sigma^2<\infty$ ⇒ $\bar X\xrightarrow{P}\mu$。關鍵：$E\bar X=\mu$，$\text{Var}\bar X=\sigma^2/n\to 0$。

**名詞**

| | 定義 |
|---|---|
| 不偏 | $E_\theta\hat\theta=\theta$ |
| 一致 | $\hat\theta\xrightarrow{P}\theta$ |

- $X_1$：不偏但不一致（$P(|X_1-\mu|\ge\epsilon)$ 是和 $n$ 無關的正常數）。
- $\bar X$：不偏且一致。

**動差**：$\frac1n\sum X_i^k\xrightarrow{P}E_\theta(X^k)$（$X_i^k$ 仍 iid，用 WLLN）。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $S^2$ 的不偏與一致 | 下一集 |
| 樣本動差 → 母體動差 | 動差法（method of moments） |
| 依機率收斂 | 依分配收斂、中央極限定理 |
| 均方誤差分解 | 比較估計量好壞 |

---

## 附：本集一句話總結

> **依機率收斂指 $P(|X_n-X|\ge\epsilon)\to 0$；用 Markov 不等式證明「（漸近）不偏且變異數 → 0 就依機率收斂」，由此得弱大數法則 $\bar X\xrightarrow{P}\mu$；統計把依機率收斂到 $\theta$ 的估計量叫一致估計量，樣本動差就是母體動差的一致估計量。**

---

*筆記依據「統計學」Lec13 錄影逐字稿（whisper large-v3-turbo，1:12:22）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
