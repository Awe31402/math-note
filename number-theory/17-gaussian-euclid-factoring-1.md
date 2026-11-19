---
course: Number Theory（2021 秋，線上錄影）
episode: 17
lecture: 2021-10-04 第 1 部
date: 2021-10-04
video: https://youtu.be/Gd9xAj5FrjA
notes: 講者照 Keith Conrad〈The Gaussian Integers〉§4–6（定理編號照它）；Jones & Jones《Elementary Number Theory》§10.2 相伴元、不可約元素（書頁 198，PDF 頁 213）
---

# 第 17 集 · 高斯整數的 Euclid 演算法、分解、合數與質數（上）（Euclidean Algorithm, Factoring Gaussian Integers, Composite vs. Prime, Part 1） [▶ 影片](https://youtu.be/Gd9xAj5FrjA)

← 上一集：[16-gaussian-integers-division-algorithm-2](16-gaussian-integers-division-algorithm-2.md) ｜ [總目錄](README.md) ｜ 下一集：[18-gaussian-euclid-factoring-2](18-gaussian-euclid-factoring-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 17 集（2021-10-04 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，whisper 轉錄；結尾被切斷）＋ Jones & Jones《Elementary Number Theory》§10.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. gcd 與互質的定義](#1-gcd-與互質的定義)
- [2. Euclid 演算法](#2-euclid-演算法)
- [3. 例子：32 + 9i 和 4 + 11i](#3-例子32--9i-和-4--11i)
  - [3.1 往下除](#31-往下除)
  - [3.2 向量版：Bézout 係數](#32-向量版bézout-係數)
- [4. 例子：4 + 5i 和 4 − 5i 互質](#4-例子4--5i-和-4--5i-互質)
- [5. gcd 只唯一到差一個單位](#5-gcd-只唯一到差一個單位)
- [6. Bézout 定理](#6-bézout-定理)
- [7. 互質的推論](#7-互質的推論)
- [8. gcd 的四種等價說法](#8-gcd-的四種等價說法)
- [9. 唯一分解的準備：平凡因數與合數](#9-唯一分解的準備平凡因數與合數)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

繼續 Conrad 的講義：§4 Euclid 演算法、§5 Bézout 定理、§6 唯一分解。講者說到目前為止的東西，大多能在**別的數系**裡模仿；但有些數系**沒有除法演算法**，也就**沒有唯一分解**——而唯一分解是之後用高斯整數解有趣問題的關鍵。

| 主題 | 時間 | Conrad 編號 |
|---|---|---|
| gcd、互質 | 00:00 | 定義 |
| Euclid 演算法 | 02:33 | Theorem 4.3 |
| 例子 | 09:20 | Example 4.4 |
| 向量版 | 16:13 | — |
| 互質的例子 | 23:26 | Example 4.5 |
| gcd 差單位 | 29:32 | Corollary 4.7 |
| Bézout | 33:38 | Theorem 5.1、Corollary 5.2 |
| 互質推論 | 40:29 | Corollary 5.7–5.9 |
| 平凡因數、合數 | 50:11 | Lemma 6.1、Definition 6.2 |

---

## 1. gcd 與互質的定義

[▶ 00:00](https://youtu.be/Gd9xAj5FrjA?t=0)

> **定義**：$\alpha,\beta\in\mathbb{Z}[i]$ 非零。$\alpha$ 和 $\beta$ 的**一個**最大公因數（a greatest common divisor）是**範數最大**的公因數。

講者特別改口：要說「**一個**」gcd，不是「**這個**」gcd（理由見第 5 節）。

> **定義** [▶ 01:08](https://youtu.be/Gd9xAj5FrjA?t=68)：若 $\alpha,\beta$ 的公因數**只有單位**，就說它們**互質**（relatively prime）。

**講者的困惑** [▶ 00:38](https://youtu.be/Gd9xAj5FrjA?t=38)：講者一直覺得「應該是**最小**範數吧？」理由是 Euclid 演算法裡餘數的範數一直變小，最後的非零餘數範數最小。他說「這只從半小時前開始困擾我，還沒時間好好查，Conrad 是對的機率非常高」，下課再查。

> 以下**不是逐字稿內容**，是解開講者的困惑：**Conrad 的「最大」是對的。** 兩個「最」比較的對象不同：
> - 在**餘數**之間，最後一個非零餘數 $\rho_k$ 的範數**最小**（$N(\beta)>N(\rho_1)>\cdots>N(\rho_k)$）。
> - 在**公因數**之間，$\rho_k$ 的範數**最大**：任何公因數 $\delta'$ 都整除 $\rho_k$（第 2 節），所以 $N(\delta')\mid N(\rho_k)$，$N(\delta')\le N(\rho_k)$。
>
> 整數裡也一樣：$\gcd(100,44)=4$ 是最後一個非零餘數（餘數裡最小），也是公因數裡最大的。講者在 [▶ 14:57](https://youtu.be/Gd9xAj5FrjA?t=897) 也說「我想它確實是範數最大的公因數，是我想錯了」。

---

## 2. Euclid 演算法

[▶ 02:33](https://youtu.be/Gd9xAj5FrjA?t=153)

> **定理**（Conrad 4.3）：$\alpha,\beta\in\mathbb{Z}[i]$ 非零。**反覆用除法定理**：每一步的除數和餘數變成下一步的被除數和除數，直到餘數為 0。**最後一個非零餘數**就是 $\alpha,\beta$ 的一個 gcd。

$$\begin{aligned}
\alpha &= \beta\gamma_1+\rho_1, & N(\rho_1)&<N(\beta)\\
\beta &= \rho_1\gamma_2+\rho_2, & N(\rho_2)&<N(\rho_1)\\
\rho_1 &= \rho_2\gamma_3+\rho_3, & N(\rho_3)&<N(\rho_2)\\
&\ \ \vdots\\
\rho_{k-1} &= \rho_k\gamma_{k+1}+0.
\end{aligned}$$

**會停** [▶ 04:33](https://youtu.be/Gd9xAj5FrjA?t=273)：範數是非負整數，而且嚴格遞減
$$N(\beta)>N(\rho_1)>N(\rho_2)>\cdots>N(\rho_k)>N(\rho_{k+1})=0,$$
所以有限步一定停。（講者寫最後一行的下標時卡了一下，「我在說什麼」，最後理清楚。）

**為什麼最後的非零餘數是公因數、而且是 gcd** [▶ 07:47](https://youtu.be/Gd9xAj5FrjA?t=467)：

- 每一式都能解出餘數：$\rho_1 = \alpha-\beta\gamma_1$，$\rho_2 = \beta-\rho_1\gamma_2$……所以 **$\alpha,\beta$ 的任何公因數都整除每個餘數**，特別是整除 $\rho_k$。
- 反過來，從最後一式往上看，$\rho_k$ 整除 $\rho_{k-1}$，再整除 $\rho_{k-2}$……一路整除 $\beta$ 和 $\alpha$。所以 $\rho_k$ 是公因數。
- 講者：「跟整數完全同一個故事。」

---

## 3. 例子：32 + 9i 和 4 + 11i

### 3.1 往下除

[▶ 09:20](https://youtu.be/Gd9xAj5FrjA?t=560)（Conrad Example 4.4）

$\alpha = 32+9i$、$\beta = 4+11i$。

**怎麼找第一個商** [▶ 09:51](https://youtu.be/Gd9xAj5FrjA?t=591)：講者示範用 **Wolfram Alpha**，直接輸入 `(32+9i)/(4+11i)`，要小數近似：
$$\frac{32+9i}{4+11i} = \frac{227}{137}-\frac{316}{137}\,i\approx 1.65-2.31\,i.$$
（講者一開始唸成「$+2.31i$」，查了 Conrad 才發現是負的。）取最近的高斯整數：$\gamma_1 = 2-2i$。

【口頭】「當然可以手算，但如果你跟我一樣，大概有 10% 機率算錯，然後很煩。」Conrad 的講義直接寫 $2-2i$ 不解釋，「解釋這些細節的話，這份講義就不是講義而是一本書了，而且不會是本有趣的書」。

**全部的步驟** [▶ 12:54](https://youtu.be/Gd9xAj5FrjA?t=774)：

| 步驟 | 等式 | 餘數的範數 |
|---|---|---|
| 1 | $32+9i = (4+11i)(2-2i) + (2-5i)$ | $N(2-5i) = 29$ |
| 2 | $4+11i = (2-5i)(-2+i) + (3-i)$ | $N(3-i) = 10$ |
| 3 | $2-5i = (3-i)(1-i) + (-i)$ | $N(-i) = 1$ |
| 4 | $3-i = (-i)(1+3i) + 0$ | — |

（驗算第 1 步：$(4+11i)(2-2i) = 8-8i+22i+22 = 30+14i$，$32+9i-(30+14i) = 2-5i$。）

**最後一個非零餘數是 $-i$**，一個**單位**。所以 **$32+9i$ 和 $4+11i$ 互質**。

講者 [▶ 13:54](https://youtu.be/Gd9xAj5FrjA?t=834)：如果只是要 gcd，**一碰到單位就可以停**——單位整除一切，下一步餘數一定是 0。

### 3.2 向量版：Bézout 係數

[▶ 16:13](https://youtu.be/Gd9xAj5FrjA?t=973)

講者說這個 Conrad 沒有，是他自己加的，用來說明 **Bézout 在這裡照樣成立**。

| 數對 | 用 $\alpha,\beta$ 表示 |
|---|---|
| $(32+9i,\ 4+11i)$ | $(\alpha,\ \beta)$ |
| $(4+11i,\ 2-5i)$ | $(\beta,\ \alpha-(2-2i)\beta)$ |
| $(2-5i,\ 3-i)$ | $(\ \cdots,\ (2-i)\alpha+(6i-1)\beta)$ |
| $(3-i,\ -i)$ | $(\ \cdots,\ 3i\,\alpha-(7+5i)\beta)$ |

- 第 2 行：$2-5i = \alpha-(2-2i)\beta$。
- 第 3 行：$3-i = \beta-(-2+i)\left[\alpha-(2-2i)\beta\right]$，化簡成 $(2-i)\alpha+(6i-1)\beta$。（講者說「不容易看出來」。）
- 第 4 行：$-i = \left[\alpha-(2-2i)\beta\right]-(1-i)\left[(2-i)\alpha+(6i-1)\beta\right]$，化簡成 $3i\,\alpha-(7+5i)\beta$。（講者把左邊那一欄叫「小精靈」，「我不在乎它是什麼」。）

**結果** [▶ 21:23](https://youtu.be/Gd9xAj5FrjA?t=1283)：
$$-i = 3i\,\alpha-(7+5i)\,\beta.$$
（驗算：$3i(32+9i) = -27+96i$，$(7+5i)(4+11i) = -27+97i$，相減得 $-i$。）

**兩邊乘 $i$** [▶ 21:53](https://youtu.be/Gd9xAj5FrjA?t=1313)：$i\cdot(-i) = 1$，
$$1 = -3\,\alpha+(5-7i)\,\beta.$$
所以 $\gcd = -i$ 也可以說 $\gcd = 1$。

【口頭】「這是我第二次試。第一次在兩個地方犯了蠢錯，整個垮掉。這種計算要非常小心，所以我鼓勵你們用 Wolfram Alpha 或任何對你有用的工具。」

---

## 4. 例子：4 + 5i 和 4 − 5i 互質

[▶ 23:26](https://youtu.be/Gd9xAj5FrjA?t=1406)（Conrad Example 4.5）

（第 15 集：這兩個範數都是 41，但不差一個單位。）

**往下除**：

1. $4+5i = (4-5i)\cdot i + (-1+i)$。
   驗算：$(4-5i)i = 5+4i$，加 $-1+i$ 得 $4+5i$。✓ 餘數範數 $N(-1+i) = 2$，遠小於 $\frac12\cdot 41$。
2. $4-5i = (-1+i)(-4) + (-i)$。
   驗算：$(-1+i)(-4) = 4-4i$，加 $-i$ 得 $4-5i$。✓

碰到單位 $-i$，停。**gcd 是單位，所以互質。**

⚠️ 逐字稿缺字：第 2 步字幕寫「minus 1 minus i times minus 4 minus i」，乘出來不對。上面依 $\dfrac{4-5i}{-1+i} = -4.5+0.5i$ 取商 $-4$ 重算。

**Bézout：倒推** [▶ 27:28](https://youtu.be/Gd9xAj5FrjA?t=1648)

【課堂討論】講者問：能不能直接看出 $1 = \square\,(4+5i)+\square\,(4-5i)$？學生覺得很難。講者：「要你們直接看出來大概太過分了。分解複數比分解實數難一點吧？」

講者改用 Conrad 強調的**倒推法**（back substitution）：

- 由第 2 步：$-i = (4-5i) + 4(-1+i)$。
- 由第 1 步：$-1+i = (4+5i) - i(4-5i)$。代入：
  $$-i = (4-5i) + 4(4+5i) - 4i(4-5i) = (1-4i)(4-5i) + 4(4+5i).$$
- 兩邊乘 $i$：
  $$1 = (4+i)(4-5i) + 4i\,(4+5i).$$

（驗算：$(4+i)(4-5i) = 21-16i$，$4i(4+5i) = -20+16i$，相加得 $1$。✓）

⚠️ 逐字稿缺字：字幕裡講者寫的係數是 $(1+i)$ 和 $(i-1)$，代進去不等於 $-i$ 和 $1$。上面是重算的結果。

---

## 5. gcd 只唯一到差一個單位

[▶ 29:32](https://youtu.be/Gd9xAj5FrjA?t=1772)

> **推論**（Conrad 4.7）：$\alpha,\beta$ 非零，$\delta$ 是 Euclid 演算法給出的 gcd。則 $\alpha,\beta$ 的**任何** gcd 都是 $\delta$ 乘一個單位。

**證明** [▶ 30:37](https://youtu.be/Gd9xAj5FrjA?t=1837)：設 $\delta'$ 是另一個 gcd。

1. 由 Euclid 演算法的證明，公因數 $\delta'$ 整除 $\delta$：$\delta = \delta'\gamma$。
2. 取範數：$N(\delta) = N(\delta')N(\gamma)$。
3. $\delta'$ 也是 gcd（範數最大），所以 $N(\delta')\ge N(\delta)$；而 $\delta$ 也是公因數，所以 $N(\delta)\le N(\delta')$——兩者都是最大，所以 $N(\delta) = N(\delta')$。
4. 於是 $N(\gamma) = 1$，$\gamma$ 是單位。∎

講者 [▶ 22:24](https://youtu.be/Gd9xAj5FrjA?t=1344)：所以說「**一個** gcd」。不像正整數有唯一的 gcd，這裡 gcd 只定義到差一個單位，「但這不是問題」。例如 3.2 的 $-i$ 和 $1$ 都是 gcd。

（講者說第 3 步時一度講成「整數只能小於等於自己乘另一個整數」，最後歸結到 $N(\gamma)=1$。）

---

## 6. Bézout 定理

[▶ 33:38](https://youtu.be/Gd9xAj5FrjA?t=2018)

> **Bézout 定理**（Conrad 5.1）：$\alpha,\beta\in\mathbb{Z}[i]$ 非零，$\delta$ 是一個 gcd。則存在 $x,y\in\mathbb{Z}[i]$ 使
> $$\delta = \alpha x+\beta y.$$

（講者口誤說「$x,y$ 是整數」，應是高斯整數。）

**證明**：倒推——從最後一個非零餘數往上，一式一式代換（就是第 4 節的做法）。實務上也可以用向量版 Euclid 演算法（第 3.2 節：$x = 3i$、$y = -7-5i$）。

> **推論**（Conrad 5.2）[▶ 36:45](https://youtu.be/Gd9xAj5FrjA?t=2205)：$\alpha,\beta$ 互質 $\iff$ 存在 $x,y\in\mathbb{Z}[i]$ 使 $\alpha x+\beta y = 1$。

- **(⇒)** 由 Bézout 寫出某個 gcd 的組合。gcd 是單位，若不是 1，就乘上 $i$、$-i$ 或 $-1$ 把它變成 1，整條式子一起乘。
- **(⇐)** [▶ 38:17](https://youtu.be/Gd9xAj5FrjA?t=2297)（講者說「這方向我比較不清楚」，然後照 Conrad 講）：若 $\alpha x+\beta y=1$，任何公因數 $d$ 都整除 $1$。**整除單位的東西本身是單位**（上次用範數證過：$N(d)\mid N(1)=1$）。所以公因數只有單位，互質。

【口頭】[▶ 39:28](https://youtu.be/Gd9xAj5FrjA?t=2368) Conrad Example 5.3 用倒推得到跟 3.2 一樣的結果。講者說作業寫「用向量版」，但用倒推也可以，「我比較喜歡向量版，不知道哪個比較好」。Conrad 5.4–5.6 也是 Bézout 的計算例子。

---

## 7. 互質的推論

[▶ 40:29](https://youtu.be/Gd9xAj5FrjA?t=2429)

> **推論**（Conrad 5.7）：若 $\alpha\mid\beta\gamma$，且 $\alpha,\beta$ 互質，則 $\alpha\mid\gamma$。

【課堂討論】講者問結論是什麼。學生：$\alpha$ 跟 $\beta$ 互質，所以 $\alpha$ 不整除 $\beta$，那就得整除另一個。

講者說他特別講這個證明，因為**下一個推論是作業**，而且要讓大家看到：**可以直接把整數的證明搬過來，把整數換成高斯整數，論證一模一樣**。

**證明** [▶ 43:02](https://youtu.be/Gd9xAj5FrjA?t=2582)（Conrad 用 $(\alpha,\beta)=1$ 表示 gcd 是 1）：

1. $\alpha\mid\beta\gamma$ ⇒ $\beta\gamma = \alpha\kappa$（某個 $\kappa\in\mathbb{Z}[i]$）。
2. 互質 ⇒ $1 = \alpha x+\beta y$（推論 5.2）。
3. 兩邊乘 $\gamma$：
   $$\gamma = \gamma\alpha x+\gamma\beta y = \gamma\alpha x+\alpha\kappa y = \alpha\,(\gamma x+\kappa y).$$
4. 所以 $\alpha\mid\gamma$。∎

「這**完全**就是我們在整數裡的證明。」（第 5 集 Lemma 2.1(b)。）

**另外兩個**（講者不證，留給學生；5.8 是作業）：

> **推論**（Conrad 5.8）[▶ 45:39](https://youtu.be/Gd9xAj5FrjA?t=2739)：若 $\alpha\mid\gamma$、$\beta\mid\gamma$，且 $\alpha,\beta$ 互質，則 $\alpha\beta\mid\gamma$。

> **推論**（Conrad 5.9）[▶ 46:11](https://youtu.be/Gd9xAj5FrjA?t=2771)：$\alpha,\beta,\gamma$ 非零。$\alpha,\gamma$ 互質且 $\beta,\gamma$ 互質 $\iff$ $\alpha\beta$ 和 $\gamma$ 互質。

【口頭】講者注意到有學生打自己巴掌保持清醒抄筆記，「真是硬派」。

---

## 8. gcd 的四種等價說法

[▶ 47:41](https://youtu.be/Gd9xAj5FrjA?t=2861)

Conrad 指出，非零整數 $a,b$ 的 gcd 有好幾種等價描述，高斯整數各有對應版本：

| 整數 $a,b$ | 高斯整數 $\alpha,\beta$ |
|---|---|
| 最大的公因數 | 範數最大的公因數（定義） |
| 被所有公因數整除的正公因數 | 被所有公因數整除的公因數 |
| $ax+by$（$x,y\in\mathbb{Z}$）的最小正值 | $\alpha x+\beta y$ 的範數最小的非零值 |
| 整除所有 $ax+by$ 的那個正的 $ax+by$ | 整除所有 $\alpha x+\beta y$ 的那個 $\alpha x+\beta y$ |

Conrad 把證明等價留給讀者。講者：「我覺得很有趣。」

---

## 9. 唯一分解的準備：平凡因數與合數

[▶ 50:11](https://youtu.be/Gd9xAj5FrjA?t=3011)

> **引理**（Conrad 6.1）：$\alpha\neq 0$。$\alpha$ 的因數中，範數為 $1$ 或 $N(\alpha)$ 的，只有**單位**和 **$\alpha$ 乘單位**。

**證明** [▶ 51:21](https://youtu.be/Gd9xAj5FrjA?t=3081)：設 $\beta\mid\alpha$。

- $N(\beta) = 1$：$\beta$ 是單位（第 15 集）。
- $N(\beta) = N(\alpha)$：寫 $\alpha = \beta\gamma$（Conrad 叫 $\gamma$「互補因數」）。取範數 $N(\alpha) = N(\beta)N(\gamma)$，消掉 $N(\alpha)=N(\beta)$，得 $N(\gamma)=1$，$\gamma$ 是單位。所以 $\alpha = \pm\beta$ 或 $\pm i\beta$，$\beta$ 是 $\alpha$ 乘單位。∎

**警告** [▶ 53:22](https://youtu.be/Gd9xAj5FrjA?t=3202)：這**不是**說「範數等於 $N(\alpha)$ 的高斯整數只有 $\pm\alpha,\pm i\alpha$」。例如
$$N(1+8i) = 65 = N(4+7i),$$
但它們不差一個單位。關鍵是引理說的是 **$\alpha$ 的因數**——$1+8i$ 並不整除 $4+7i$。

**整數的類比** [▶ 54:53](https://youtu.be/Gd9xAj5FrjA?t=3293)：

- $15 = 3\cdot 5 = (-3)(-5)$：這兩個是「有意思的」分解。
- $15 = 1\cdot 15 = (-1)(-15)$：「無趣的」分解，任何數都能這樣寫，我們不算它。
- $7 = 7\cdot 1 = (-7)(-1)$：其中一個因數是單位，**不能**說這證明 7 是合數。

（講者一開始舉 12，發現「選錯了」，改成 15。）

> **定義**（Conrad 6.2，講義第 12 頁）[▶ 57:31](https://youtu.be/Gd9xAj5FrjA?t=3451)：$\alpha\in\mathbb{Z}[i]$，$N(\alpha)>1$（也就是 $\alpha$ 不是單位）。若 $\alpha$ 有**非平凡因數**，就叫 $\alpha$ **合數**（composite）。
>
> **平凡因數**（trivial factor）：$\pm1,\ \pm i,\ \pm\alpha,\ \pm i\alpha$。

**等價說法** [▶ 59:03](https://youtu.be/Gd9xAj5FrjA?t=3543)：寫 $\alpha = \beta\gamma$，「$1<N(\beta)<N(\alpha)$」等價於「$N(\beta)>1$ 且 $N(\gamma)>1$」。講者：「這是我想它的關鍵方式。」（影片在這裡被切斷，接第 18 集。）

> 以下**不是逐字稿內容**，是補上為什麼等價：$N(\alpha) = N(\beta)N(\gamma)$。$N(\beta)<N(\alpha)$ ⇔ $N(\gamma)>1$；$N(\beta)>1$ 就是 $N(\beta)>1$。所以兩個條件一樣。

> 【課本補充】§10.2（p. 198）用的詞：
> - **相伴元**（associates）：$a = ub$，$u$ 是單位。這是等價關係（單位在乘法下成群）。Conrad 說的「差一個單位」就是相伴。
> - **不可約元素**（irreducible）：不是 $0$ 也不是單位，而且因數只有單位和自己的相伴元。否則叫**可約**（reducible）。在 $\mathbb{Z}$ 裡，$a$ 的相伴元是 $\pm a$，不可約元素就是 $\pm p$（$p$ 質數）。
> - Conrad 的「合數」就是課本的「可約」；不是合數（也不是單位）的就是不可約。

---

## 10. 一頁速查表

**gcd**：範數**最大**的公因數；只唯一到差一個單位。**互質**：公因數只有單位。

**Euclid 演算法**：反覆除法定理，最後一個非零餘數是 gcd；碰到單位就可停（⇒ 互質）。

- **關鍵一步**：公因數整除每個餘數；最後的餘數往上整除每一行。
- 找商：算 $\alpha/\beta$ 的小數，取最近的高斯整數（可用 Wolfram Alpha）。

**例子**

| $\alpha,\beta$ | 過程 | gcd | Bézout |
|---|---|---|---|
| $32+9i,\ 4+11i$ | 商 $2-2i,\,-2+i,\,1-i$；餘數 $2-5i,\,3-i,\,-i$ | $-i\sim1$ | $1 = -3\alpha+(5-7i)\beta$ |
| $4+5i,\ 4-5i$ | $4+5i = (4-5i)i+(-1+i)$；$4-5i = (-1+i)(-4)-i$ | $-i\sim1$ | $1 = 4i(4+5i)+(4+i)(4-5i)$ |

**Bézout**：$\delta = \alpha x+\beta y$。互質 ⇔ $\alpha x+\beta y=1$ 有解。

**互質推論**：$\alpha\mid\beta\gamma$、$(\alpha,\beta)=1$ ⇒ $\alpha\mid\gamma$。**關鍵一步**：$\gamma = \alpha(\gamma x+\kappa y)$（跟整數同一個證明）。

**平凡因數**：$\pm1,\pm i,\pm\alpha,\pm i\alpha$。**合數**：有非平凡因數 ⇔ $\alpha=\beta\gamma$ 且 $N(\beta),N(\gamma)>1$。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 合數 vs 高斯質數、唯一分解 | 第 18–19 集 |
| 互質推論 ⇒ 「高斯質數整除乘積就整除其一」 | 第 18–19 集 |
| 分解 $p = a^2+b^2$ | 第 19–21 集 |
| 唯一分解失敗的數系 | 第 22 集 |
| 相伴、不可約、質元素的一般定義 | 第 36–39 集 |

---

## 附：本集一句話總結

> **高斯整數的 Euclid 演算法跟整數一樣：反覆做除法，最後一個非零餘數就是 gcd（只唯一到差一個單位），碰到單位就表示互質。倒推或向量版能寫出 Bézout 組合，所以整數裡「$\alpha\mid\beta\gamma$ 且 $\alpha,\beta$ 互質 ⇒ $\alpha\mid\gamma$」的證明原封不動搬過來。最後定義平凡因數和合數，為唯一分解做準備。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-04 第 1 部錄影逐字稿（whisper 轉錄，59:51）與 Jones & Jones《Elementary Number Theory》§10.2 整理；講者的主要參考是 Keith Conrad〈The Gaussian Integers〉。*
