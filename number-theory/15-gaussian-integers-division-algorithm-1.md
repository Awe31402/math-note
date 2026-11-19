---
course: Number Theory（2021 秋，線上錄影）
episode: 15
lecture: 2021-09-29 第 1 部
date: 2021-09-29
video: https://youtu.be/GUXX7Q4qpJI
notes: 講者照 Keith Conrad 的講義〈The Gaussian Integers〉（定理編號照它）；Jones & Jones《Elementary Number Theory》§10.2（書頁 196–198，PDF 頁 211–213）：Z[i]、整環、Euclid 整環、Example 10.7、Exercise 10.4、除法的幾何證明
---

# 第 15 集 · 高斯整數：範數、單位、整除、除法定理（上）（Gaussian Integers up through Division Algorithm, Part 1） [▶ 影片](https://youtu.be/GUXX7Q4qpJI)

← 上一集：[14-rsa-quadratic-diophantine-pell-2](14-rsa-quadratic-diophantine-pell-2.md) ｜ [總目錄](README.md) ｜ 下一集：[16-gaussian-integers-division-algorithm-2](16-gaussian-integers-division-algorithm-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 15 集（2021-09-29 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，whisper 轉錄；結尾被切斷）＋ Jones & Jones《Elementary Number Theory》§10.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 高斯整數與範數](#1-高斯整數與範數)
- [2. 範數有乘性](#2-範數有乘性)
- [3. 單位只有 ±1、±i](#3-單位只有-1i)
- [4. 整除](#4-整除)
  - [4.1 定義與例子](#41-定義與例子)
  - [4.2 被普通整數整除](#42-被普通整數整除)
  - [4.3 β | α ⇒ N(β) | N(α)](#43-β--α--nβ--nα)
  - [4.4 範數是偶數 ⇔ 是 1 + i 的倍數](#44-範數是偶數--是-1--i-的倍數)
  - [4.5 用範數快速排除](#45-用範數快速排除)
- [5. 範數相同不代表差一個單位](#5-範數相同不代表差一個單位)
- [6. 除法定理](#6-除法定理)
  - [6.1 陳述](#61-陳述)
  - [6.2 例子：(27 − 23i) ÷ (8 + i)](#62-例子27--23i--8--i)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

開始講**高斯整數**（Gaussian integers）。

**用什麼教材** [▶ 00:36](https://youtu.be/GUXX7Q4qpJI?t=36)：【口頭】課本（Stillwell）第 6 章「還可以」，但 **Keith Conrad 的講義〈The Gaussian Integers〉「寫得太好了」**，證明比第 6 章某些部分清楚，所以照它講。講義放在課程網站，Conrad 的網站上也能免費下載（「Google 找得到，在他網站裡翻可能找不到，他放太多東西了」）。下面的定理編號（1.2、1.4、2.3……）是 Conrad 講義的編號。

【口頭】進度落後：原本排兩天，但有一天沒上（講者說可能要補錄一支影片）。

**為什麼學高斯整數** [▶ 01:12](https://youtu.be/GUXX7Q4qpJI?t=72)：

1. 它們會揭露**普通整數質數**的很多有趣性質。
2. 能推出之前的畢氏三元數組公式（第 1–2 集）。
3. 本身就很有意思。

講者說今天會看到：**整數的整除理論在高斯整數裡幾乎一一對應**。

| 主題 | 時間 | Conrad 編號 |
|---|---|---|
| 定義、範數 | 01:51 | 定義 |
| 範數乘性 | 05:58 | Theorem 1.2 |
| 單位 | 08:46 | Corollary 1.4 |
| 整除 | 14:28 | §2、Example 2.1–2.2 |
| 被整數整除 | 21:38 | Theorem 2.3 |
| 範數整除 | 25:39 | Theorem 2.4 |
| 偶數範數 | 28:31 | Corollary 2.5 |
| 範數相同 ≠ 差單位 | 42:41 | — |
| 除法定理 | 46:52 | Theorem 3.1 |

---

## 1. 高斯整數與範數

[▶ 01:51](https://youtu.be/GUXX7Q4qpJI?t=111)

> **定義**：**高斯整數**
> $$\mathbb{Z}[i] = \{\,a+bi : a,b\in\mathbb{Z}\,\}.$$
> （讀作「$\mathbb{Z}$ 添加 $i$」，$\mathbb{Z}$ adjoin $i$。）

它是 $\mathbb{C}$ 的子集合，所以可以直接用複數的運算。

> **定義**：$\alpha = a+bi\in\mathbb{Z}[i]$ 的**範數**（norm）
> $$N(\alpha) = \alpha\bar\alpha = (a+bi)(a-bi) = a^2+b^2.$$
> 其中 $\bar\alpha = a-bi$ 是**共軛複數**（complex conjugate）。

展開 [▶ 03:51](https://youtu.be/GUXX7Q4qpJI?t=231)：$(a+bi)(a-bi) = a^2 - abi + abi - b^2i^2 = a^2+b^2$（因為 $-i^2 = 1$）。

**例子**：$N(3) = 9$；$N(1+i) = 1^2+1^2 = 2$。

【口頭】講者第一次教數論時很不喜歡這叫「範數」：線性代數的範數跟它不一樣，這個「一點都不線性，相當非線性」。

**範數的好處** [▶ 04:57](https://youtu.be/GUXX7Q4qpJI?t=297)：

- $N(\alpha)$ 是**整數**（而且 $\ge 0$，只有 $\alpha=0$ 時是 $0$）。
- 講者：數論學家替抽象系統定義範數時，就想要它是整數值，這樣才能用那個代數結構研究整數。

【課堂討論】[▶ 07:42](https://youtu.be/GUXX7Q4qpJI?t=462) 範數就是 $a+bi$ 當作複數時**到原點距離的平方**。講者問：在整數裡，什麼扮演範數的角色？學生答：**絕對值**。

---

## 2. 範數有乘性

[▶ 05:58](https://youtu.be/GUXX7Q4qpJI?t=358)

> **定理**（Conrad 1.2）：$N(\alpha\beta) = N(\alpha)\,N(\beta)$。

講者說「就像 Euler φ 函數一樣是乘性的」，而且他用自己的證法（靠複數運算），不是 Conrad 的。

**證明** [▶ 06:30](https://youtu.be/GUXX7Q4qpJI?t=390)：

$$N(\alpha\beta) = (\alpha\beta)\overline{(\alpha\beta)} = \alpha\beta\,\bar\alpha\,\bar\beta = (\alpha\bar\alpha)(\beta\bar\beta) = N(\alpha)N(\beta).$$

- 第二個等號：**乘積的共軛 = 共軛的乘積**（共軛的基本性質）。
- 第三個等號：複數乘法可交換，重新排列。∎

---

## 3. 單位只有 ±1、±i

[▶ 08:46](https://youtu.be/GUXX7Q4qpJI?t=526)

> **推論**（Conrad 1.4）：$\mathbb{Z}[i]$ 裡**可逆**（有乘法反元素）的元素只有 $\pm 1,\ \pm i$。

**這四個可逆**：$1\cdot 1 = 1$，$(-1)(-1) = 1$，$i\cdot(-i) = 1$。所以 $1^{-1} = 1$、$(-1)^{-1} = -1$、$i^{-1} = -i$、$(-i)^{-1} = i$。

**只有這四個** [▶ 09:47](https://youtu.be/GUXX7Q4qpJI?t=587)：設 $\alpha = a+bi$ 有反元素 $\beta$，$\alpha\beta = 1$。

1. 取範數，用乘性 [▶ 10:56](https://youtu.be/GUXX7Q4qpJI?t=656)：
   $$N(\alpha)N(\beta) = N(1) = 1.$$
2. $N(\alpha),N(\beta)$ 是整數，兩個整數乘起來是 1，只能是 $1\cdot 1$ 或 $(-1)(-1)$。範數 $\ge 0$，所以 **$N(\alpha) = 1$**。
3. $a^2+b^2 = 1$，$a,b$ 是整數。$|a|$ 或 $|b|\ge 2$ 都不行，所以一個是 $0$、另一個是 $\pm 1$。
4. $\alpha\in\{\pm1,\pm i\}$。∎

【Q&A】[▶ 10:25](https://youtu.be/GUXX7Q4qpJI?t=625) 有學生說「1 的反元素就是 1」。講者：這是新的數系，不能先假設——「有理數裡也可以 $2\cdot\frac12 = 1$」。所以要用範數證。

**為什麼重要** [▶ 13:23](https://youtu.be/GUXX7Q4qpJI?t=803)：可逆元素也叫**單位**（unit）。研究高斯整數的分解時，**分解只能唯一到差一個單位**——就像整數裡 $6 = 2\cdot 3 = (-2)(-3)$。

【口頭】預告：之後的**代數整數**也有範數，解「範數 = 1」時，有一個例子會變成 **Pell 方程**，那就有**無限多個單位**。本課看的典型例子單位有限。（第 14 集的 Pell 方程。）

> 【課本補充】§10.2 Exercise 10.4（p. 197）：$u\in\mathbb{Z}[i]$ 是單位 ⇔ $N(u)=1$ ⇔ $u=\pm1$ 或 $\pm i$。

---

## 4. 整除

### 4.1 定義與例子

[▶ 14:28](https://youtu.be/GUXX7Q4qpJI?t=868)

> **定義**：$\alpha,\beta\in\mathbb{Z}[i]$。若存在 $\gamma\in\mathbb{Z}[i]$ 使 $\alpha = \beta\gamma$，就說 **$\beta$ 整除 $\alpha$**，寫 $\beta\mid\alpha$。

跟整數的定義一樣：$\alpha$ 是 $\beta$ 的**高斯整數**倍。

**例子**（Conrad 2.1）[▶ 16:15](https://youtu.be/GUXX7Q4qpJI?t=975)：
$$14-3i = (4+5i)(1-2i).$$
所以 $4+5i\mid 14-3i$。

（驗算：$(4+5i)(1-2i) = 4-8i+5i-10i^2 = 14-3i$。）

**例子**（Conrad 2.2）[▶ 16:46](https://youtu.be/GUXX7Q4qpJI?t=1006)：$4+5i$ 整除 $14+3i$ 嗎？

**方法**：直接除，看商是不是高斯整數。$\beta\neq 0$ 時，$\beta\mid\alpha\iff\alpha/\beta\in\mathbb{Z}[i]$。

**分母有理化**：上下同乘分母的共軛 [▶ 18:57](https://youtu.be/GUXX7Q4qpJI?t=1137)。

$$\frac{14+3i}{4+5i} = \frac{(14+3i)(4-5i)}{(4+5i)(4-5i)} = \frac{56-70i+12i-15i^2}{41} = \frac{71-58i}{41}.$$

- 分母就是 $N(4+5i) = 16+25 = 41$。講者：「我做這種計算時根本不想乘法，**分母永遠是範數**。」
- $\dfrac{71}{41}$、$\dfrac{58}{41}$ 不是整數，所以 **$4+5i\nmid 14+3i$**。

【口頭】[▶ 21:05](https://youtu.be/GUXX7Q4qpJI?t=1265) 有意思的是：$N(14+3i) = N(14-3i) = 205$。**範數相同，結果卻不同**——已經是個警告。

### 4.2 被普通整數整除

[▶ 21:38](https://youtu.be/GUXX7Q4qpJI?t=1298)

> **定理**（Conrad 2.3）：$\alpha = a+bi\in\mathbb{Z}[i]$，$c\in\mathbb{Z}$。則
> $$c\mid\alpha\ \text{（在 }\mathbb{Z}[i]\text{）}\iff c\mid a\ \text{且}\ c\mid b\ \text{（在 }\mathbb{Z}\text{）}.$$

【課堂討論】學生：「就是把常數提出來嘛。」講者：「對，來證。」

**(⇒)** [▶ 22:44](https://youtu.be/GUXX7Q4qpJI?t=1364) $c\mid a+bi$ ⇒ 存在 $m+ni$ 使 $a+bi = c(m+ni) = cm+cni$。兩個複數相等 ⇔ 實部、虛部都相等，所以 $a = cm$、$b = cn$，$c\mid a$ 且 $c\mid b$。

**(⇐)** [▶ 23:58](https://youtu.be/GUXX7Q4qpJI?t=1438) $a = mc$、$b = nc$ ⇒ $a+bi = c(m+ni)$ ⇒ $c\mid a+bi$。∎

**取 $b=0$** [▶ 25:09](https://youtu.be/GUXX7Q4qpJI?t=1509)：對普通整數 $a,c$，$c\mid a$ 在 $\mathbb{Z}[i]$ 裡成立 ⇔ 在 $\mathbb{Z}$ 裡成立。**整數之間的整除，搬到 $\mathbb{Z}[i]$ 不會改變。**

### 4.3 β | α ⇒ N(β) | N(α)

[▶ 25:39](https://youtu.be/GUXX7Q4qpJI?t=1539)

> **定理**（Conrad 2.4）：若 $\beta\mid\alpha$（在 $\mathbb{Z}[i]$），則 $N(\beta)\mid N(\alpha)$（在 $\mathbb{Z}$）。

**證明**：$\alpha = \beta\gamma$ ⇒ $N(\alpha) = N(\beta)N(\gamma)$。這些都是整數，所以 $N(\alpha)$ 是 $N(\beta)$ 的倍數。∎

### 4.4 範數是偶數 ⇔ 是 1 + i 的倍數

[▶ 28:31](https://youtu.be/GUXX7Q4qpJI?t=1711)

> **推論**（Conrad 2.5）：高斯整數 $\gamma$ 的範數是偶數 $\iff$ $\gamma$ 是 $1+i$ 的倍數。

講者：「某種意義上滿令人驚訝的推論。」

**(⇐)** [▶ 29:02](https://youtu.be/GUXX7Q4qpJI?t=1742) $\gamma = \alpha(1+i)$ ⇒ $N(\gamma) = N(\alpha)\cdot N(1+i) = 2N(\alpha)$，偶數。

**(⇒)** [▶ 30:07](https://youtu.be/GUXX7Q4qpJI?t=1807) 設 $\gamma = a+bi$，$N(\gamma) = a^2+b^2$ 是偶數。

1. **模 2 分情況** [▶ 31:26](https://youtu.be/GUXX7Q4qpJI?t=1886)：$a^2+b^2\equiv 0\ (\mathrm{mod}\ 2)$。$(a,b)\equiv(1,1)$ 或 $(0,0)$ 可以；$(1,0)$、$(0,1)$ 不行。所以 **$a,b$ 同為偶數或同為奇數**。
2. **想寫成** $a+bi = (1+i)(u+vi)$ [▶ 32:27](https://youtu.be/GUXX7Q4qpJI?t=1947)。展開右邊：
   $$(1+i)(u+vi) = (u-v)+(u+v)i.$$
3. 所以要解 $a = u-v$、$b = u+v$（「這是直接的線性代數」）。兩式相加、相減：
   $$u = \frac{a+b}{2},\qquad v = \frac{b-a}{2}.$$
4. **這是整數嗎？** [▶ 34:28](https://youtu.be/GUXX7Q4qpJI?t=2068) $a,b$ 同奇偶，所以 $a+b$ 和 $b-a$ 都是偶數，$u,v$ 是整數。✓ ∎

**例子**（Conrad 2.6）[▶ 34:59](https://youtu.be/GUXX7Q4qpJI?t=2099)：

- $N(1+3i) = 10$，偶數。$a=1$、$b=3$：$u = 2$、$v = 1$，所以
  $$1+3i = (1+i)(2+i).$$
  講者：「這個證明不只說它是倍數，還告訴你**怎麼**寫成倍數，滿好的。」
- $N(1-i) = 2$。$a=1$、$b=-1$：$u = 0$、$v = -1$，所以 $1-i = (1+i)(-i)$。講者一開始算成 $i$，發現「漏了一個負號」，改成 $-i$。「其實不用公式，提出一個 $-i$ 就看得出來。」

### 4.5 用範數快速排除

[▶ 38:04](https://youtu.be/GUXX7Q4qpJI?t=2284)

定理 2.4 是判斷**不整除**的快方法：檢查範數整不整除。

**例子**：$3+7i\mid 10+3i$ 嗎？

【課堂討論】學生算範數：$N(3+7i) = 9+49 = 58$，$N(10+3i) = 100+9 = 109$。$58\nmid 109$，所以 **$3+7i\nmid 10+3i$**。

**逆命題不成立** [▶ 40:10](https://youtu.be/GUXX7Q4qpJI?t=2410)：範數整除，不代表本身整除。

例：$\alpha = 14+3i$、$\beta = 4+5i$。$N(\alpha) = 205 = 41\cdot 5$，$N(\beta) = 41$，所以 $N(\beta)\mid N(\alpha)$。但 4.1 已經算過 $4+5i\nmid 14+3i$。（講者：「謝謝 Conrad，不用我另外編例子。」）

**Conrad 的總結** [▶ 42:11](https://youtu.be/GUXX7Q4qpJI?t=2531)：

- **萬無一失的方法**：分母有理化，看商是不是高斯整數。
- **範數整除**是必要條件：失敗就一定不整除；成功不保證整除。

---

## 5. 範數相同不代表差一個單位

[▶ 42:41](https://youtu.be/GUXX7Q4qpJI?t=2561)

**整數裡**：$|m| = |n|$ ⇒ $m = \pm n$。$\pm$ 就是 $\mathbb{Z}$ 的單位，所以「絕對值相同 ⇒ 差一個單位」。

**高斯整數裡這不成立** [▶ 43:43](https://youtu.be/GUXX7Q4qpJI?t=2623)：$N(\alpha) = N(\beta)$ **不能**推出 $\alpha = u\beta$（$u$ 是單位）。

**例子**：$4+5i$ 和 $4-5i$，範數都是 $41$。把 $4-5i$ 乘上四個單位：

| 單位 $u$ | $u(4-5i)$ |
|---|---|
| $1$ | $4-5i$ |
| $-1$ | $-4+5i$ |
| $i$ | $5+4i$ |
| $-i$ | $-5-4i$ |

**$4+5i$ 不在裡面**。所以兩者範數相同，卻不是差一個單位。

【口頭】「連這個都說不了，範數有什麼用？我們等著看。」

【Q&A】[▶ 45:49](https://youtu.be/GUXX7Q4qpJI?t=2749) 學生問：可以說它們離原點一樣遠、把 $a,b$ 當向量分量嗎？講者：可以，它們作為複數到原點的距離一樣。

---

## 6. 除法定理

### 6.1 陳述

[▶ 46:52](https://youtu.be/GUXX7Q4qpJI?t=2812)

> **除法定理**（Conrad 3.1）：$\alpha,\beta\in\mathbb{Z}[i]$，$\beta\neq 0$。則存在 $\gamma,\rho\in\mathbb{Z}[i]$ 使
> $$\alpha = \beta\gamma+\rho,\qquad N(\rho)<N(\beta).$$
> 事實上可以選 $\rho$ 使 $N(\rho)\le\tfrac12 N(\beta)$。

講者說先不證，先做例子理解（證明在第 16 集）。

- $\beta$ 是除數，$\gamma$ 是**商**，$\rho$ 是**餘數**。
- 兩邊除以 $\beta$ [▶ 50:34](https://youtu.be/GUXX7Q4qpJI?t=3034)：$\dfrac\alpha\beta = \gamma+\dfrac\rho\beta$。所以叫「除法定理」。

### 6.2 例子：(27 − 23i) ÷ (8 + i)

[▶ 48:55](https://youtu.be/GUXX7Q4qpJI?t=2935)

$\alpha = 27-23i$、$\beta = 8+i$，$N(\beta) = 65$。目標：$N(\rho)\le\tfrac12\cdot 65 = 32.5$，範數是整數，所以 $N(\rho)\le 32$。

**Step 1：算 $\alpha/\beta$** [▶ 51:34](https://youtu.be/GUXX7Q4qpJI?t=3094)
$$\frac{27-23i}{8+i} = \frac{(27-23i)(8-i)}{65} = \frac{193-211i}{65}\approx 2.969 - 3.246\,i.$$

（講者：「用小數很有幫助。」）

**Step 2：錯誤的選法——取 floor** [▶ 52:36](https://youtu.be/GUXX7Q4qpJI?t=3156)

整數的除法演算法用 floor（第 3 集）。照做：$\gamma = 2-4i$。則
$$\beta\gamma = (8+i)(2-4i) = 20-30i,\qquad\rho = \alpha-\beta\gamma = 7+7i,\qquad N(\rho) = 98.$$
$98>65$，**不行**。

**Step 3：正確的選法——取最接近的整數** [▶ 55:54](https://youtu.be/GUXX7Q4qpJI?t=3354)

$2.969$ 最接近 $3$，$-3.246$ 最接近 $-3$。取 $\gamma = 3-3i$：
$$\beta\gamma = (8+i)(3-3i) = 24-24i+3i-3i^2 = 27-21i,$$
$$\rho = \alpha-\beta\gamma = (27-23i)-(27-21i) = -2i,\qquad N(\rho) = 4.$$
$4\le 32.5$。✓

所以
$$27-23i = (8+i)(3-3i) + (-2i).$$

（講者一開始把 $\beta\gamma$ 當成 $\rho$，「這看起來很糟——喔，那是 $\beta\gamma$，還要用 $\alpha$ 減它」。）

**整數的類比** [▶ 58:28](https://youtu.be/GUXX7Q4qpJI?t=3508)：
$$34 = 9\cdot 4 - 2 = 9\cdot 3+7.$$
如果不堅持餘數是正的，整數也可以選絕對值更小的餘數（$-2$ 比 $7$ 小）。整數裡我們用「只看正整數」這個**權宜的化簡**避開了範數的討論；**高斯整數沒有這種化簡可用**，所以餘數、商都**不唯一**，可能有好幾種選法。（影片在這裡被切斷，接第 16 集。）

> 【課本補充】§10.2（p. 196–198）：
> - $\mathbb{Z}[i]$ 對加減乘封閉，是一個**環**，但不是體（不是每個非零元素都是單位）。它也是**整環**（$rs=0\Rightarrow r=0$ 或 $s=0$），因為 $\mathbb{C}$ 是。
> - **Euclid 整環**（Euclidean domain）：整環 $R$ 配一個函數 $d(a)\ge 0$，滿足 (1) $d(ab)\ge d(b)$，等號 ⇔ $a$ 是單位；(2) 對 $b\neq 0$，存在 $q,r$ 使 $a = qb+r$，$r=0$ 或 $d(r)<d(b)$。$\mathbb{Z}$ 配 $d(r)=|r|$ 是 Euclid 整環（Example 10.5）。
> - **Example 10.7**：$\mathbb{Z}[i]$ 配 $d(z) = z\bar z = x^2+y^2$（就是範數）是 Euclid 整環。
> - 課本給的是**幾何證明**（p. 198）：$b$ 的所有倍數 $qb$ 形成一個正方形格子（把整數格子轉 $\arg(b)$ 角、放大 $|b|$ 倍），每個正方形邊長 $|b|$。任何複數 $a$ 到最近的格點距離最多是半條對角線 $|b|/\sqrt2$。所以 $r = a-qb$ 滿足 $|r|\le|b|/\sqrt2$，
>   $$d(r) = |r|^2\le\frac{|b|^2}{2}<|b|^2 = d(b).$$
>   這正是 Conrad 定理裡的 $N(\rho)\le\tfrac12N(\beta)$。

---

## 7. 一頁速查表

**$\mathbb{Z}[i] = \{a+bi : a,b\in\mathbb{Z}\}$**；範數 $N(a+bi) = a^2+b^2 = \alpha\bar\alpha$。

- 乘性：$N(\alpha\beta) = N(\alpha)N(\beta)$。**關鍵一步**：$\overline{\alpha\beta} = \bar\alpha\bar\beta$。
- 單位：只有 $\pm1,\pm i$。**關鍵一步**：$\alpha\beta=1$ ⇒ $N(\alpha)N(\beta)=1$ ⇒ $N(\alpha)=1$ ⇒ $a^2+b^2=1$。

**整除** $\beta\mid\alpha$ ⇔ $\alpha=\beta\gamma$ ⇔ $\alpha/\beta\in\mathbb{Z}[i]$（分母有理化，分母是 $N(\beta)$）。

| 定理 | 內容 |
|---|---|
| 2.3 | $c\in\mathbb{Z}$：$c\mid a+bi$ ⇔ $c\mid a$ 且 $c\mid b$ |
| 2.4 | $\beta\mid\alpha$ ⇒ $N(\beta)\mid N(\alpha)$（逆不成立） |
| 2.5 | $N(\gamma)$ 偶 ⇔ $(1+i)\mid\gamma$；$a+bi = (1+i)\left(\frac{a+b}2+\frac{b-a}2 i\right)$ |

**例子**

- $14-3i = (4+5i)(1-2i)$；$4+5i\nmid 14+3i$（商 $\frac{71-58i}{41}$）。
- $1+3i = (1+i)(2+i)$；$1-i = (1+i)(-i)$。
- $N(3+7i)=58\nmid109=N(10+3i)$ ⇒ 不整除。
- $N(4+5i)=N(4-5i)=41$，但不差單位。

**除法定理**：$\beta\neq0$ ⇒ $\alpha = \beta\gamma+\rho$，$N(\rho)\le\frac12N(\beta)$。

- **做法**：算 $\alpha/\beta$ 的實部、虛部，各取**最接近的整數**當 $\gamma$，$\rho = \alpha-\beta\gamma$。（不要用 floor。）
- 例：$27-23i = (8+i)(3-3i)-2i$，$N(\rho)=4$。
- 商和餘數**不唯一**。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 除法定理的證明 | 第 16 集 |
| Euclid 演算法、gcd、Bézout（高斯整數版） | 第 17–18 集 |
| 唯一分解、高斯質數 | 第 17–19 集 |
| $1+i$ 的特殊地位（$2 = -i(1+i)^2$） | 第 17–19 集 |
| 範數 = 1 ⇔ 單位；Pell 方程與無限多單位 | 第 22 集（代數整數） |
| Euclid 整環的一般理論 | 第 38–39 集 |

---

## 附：本集一句話總結

> **高斯整數 $a+bi$ 有乘性的範數 $a^2+b^2$，靠它證明單位只有 $\pm1,\pm i$、用「範數整除」快速排除整除關係（但反過來不行）。除法定理說可以用 $\beta$ 除 $\alpha$、得到範數不到 $N(\beta)$ 一半的餘數——商要取最接近的高斯整數，而且不唯一。**

---

*筆記依據 James S. Cook「Number Theory」2021-09-29 第 1 部錄影逐字稿（whisper 轉錄，59:51）與 Jones & Jones《Elementary Number Theory》§10.2 整理；講者的主要參考是 Keith Conrad〈The Gaussian Integers〉。*
