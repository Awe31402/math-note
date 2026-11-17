---
course: Number Theory（2021 秋，線上錄影）
episode: 14
lecture: Lecture 14
date: 待補（2021 秋）
video: https://youtu.be/ouAlEMkHuyI
notes: Jones & Jones §5.1–5.2（書頁 83–88，PDF 頁 98–103）：Lemma 5.1、Theorem 5.2、Theorem 5.3（Euler）、Lemma 5.4
---

# 第 14 集 · Lecture 14：單位群與 Euler 函數（Group of Units and Euler's Function） [▶ 影片](https://youtu.be/ouAlEMkHuyI)

← 上一集：[13-fermat-little-theorem](13-fermat-little-theorem.md) ｜ [總目錄](README.md) ｜ 下一集：[15-euler-theorem-unit-group-structure](15-euler-theorem-unit-group-structure.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 14 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（14:41，自動字幕）＋ Jones & Jones §5.1–5.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. U_n 是群](#1-u_n-是群)
- [2. Euler 函數](#2-euler-函數)
- [3. φ(p^k) 的公式](#3-φp^k-的公式)
- [4. Euler 定理](#4-euler-定理)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】這集很短；技術部分其實之前（第 10、13 集）已經講過，這裡快速再跑一次 [▶ 00:00](https://youtu.be/ouAlEMkHuyI?t=0)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | $U_n$ 對乘法形成群 | Lemma 5.1、Theorem 5.2 |
| 2–3 | $\phi(n) = \lvert U_n\rvert$；$\phi(p^k) = p^k-p^{k-1}$ | §5.2 定義、Lemma 5.4 |
| 4 | Euler 定理 $a^{\phi(n)}\equiv1$ | Theorem 5.3 |

---

## 1. U_n 是群

[▶ 00:00](https://youtu.be/ouAlEMkHuyI?t=0)

回顧：$\mathbb{Z}_n$ 的乘法用代表定義，$\bar1$ 是乘法單位，乘法交換、結合（因為整數乘法結合，傳到 $\mathbb{Z}_n$）。

$$U_n = \{\,[x]\in\mathbb{Z}_n : \gcd(x,n) = 1\,\}.$$

**定理**：$U_n$ 對乘法形成**群**（封閉、結合、有單位元素、有反元素）。

**證明** [▶ 01:06](https://youtu.be/ouAlEMkHuyI?t=66)：
- **單位元素**：$\gcd(1,n)=1$，所以 $[1]\in U_n$。
- **反元素**：$[x]\in U_n$ ⇒ $\gcd(x,n) = 1$ ⇒ Bézout 給 $ax+bn = 1$ ⇒ $[a][x] = [1]$。這條等式也說明 $\gcd(a,n) = 1$，所以 $[a]\in U_n$，且 $[x]^{-1} = [a]$。
- **封閉**：$[x],[y]\in U_n$。由 Bézout：
$$a_1x+a_2n = 1,\qquad b_1y+b_2n = 1.$$
兩式相乘：
$$a_1b_1\,xy + (\text{含 } n \text{ 的項}) = 1.$$
所以 $xy$ 和 $n$ 的某個整數線性組合等於 1，$\gcd(xy,n) = 1$，$[xy]\in U_n$。
- **結合**：從 $\mathbb{Z}$ 繼承。∎

**附註**：$U_n$ 恰好是 $\mathbb{Z}_n$ 中有乘法反元素的同餘類（第 10 集）。叫「單位群」（group of units）是因為它在數學技術意義上真的是一個群。

> 【課本補充】Theorem 5.2（p. 85）證封閉更直接：$[a][u] = [1]$、$[b][v] = [1]$ ⇒ $[ab][uv] = [au][bv] = [1]$。Exercise 5.2：$U_n$ 是交換群。

---

## 2. Euler 函數

[▶ 03:19](https://youtu.be/ouAlEMkHuyI?t=199)

**定義**：**Euler $\phi$ 函數**（Euler's phi function，讀作「fee」）
$$\phi(n) = \lvert U_n\rvert = \#\{\,1\le a\le n : \gcd(a,n) = 1\,\}.$$

**例**：

| $n$ | $U_n$ | $\phi(n)$ |
|---|---|---|
| 2 | $\{1\}$ | 1 |
| 3 | $\{1,2\}$ | 2 |
| 4 | $\{1,3\}$ | 2 |
| 5 | $\{1,2,3,4\}$ | 4 |
| 6 | $\{1,5\}$ | 2 |
| 7 | $\{1,\dots,6\}$ | 6 |
| 8 | $\{1,3,5,7\}$ | 4 |
| 9 | $\{1,2,4,5,7,8\}$ | 6 |
| 10 | $\{1,3,7,9\}$ | 4 |
| 20 | $\{1,3,7,9,11,13,17,19\}$ | 8 |
| 72 | 去掉 2 和 3 的倍數 | 24 |

【口頭】
- 數值忽上忽下像雲霄飛車，看不太出公式。下一集會給公式，但講者從不主張直接套公式，公式只是幫你思考怎麼算的指引 [▶ 04:58](https://youtu.be/ouAlEMkHuyI?t=298)。
- $0$（即 $\bar n$）永遠不在 $U_n$ 裡。

⚠️ 逐字稿缺字：[▶ 06:02](https://youtu.be/ouAlEMkHuyI?t=362) 字幕說 72「is 3 squared times 3 squared times 2 cubed」，應為 $72 = 9\cdot8 = 3^2\cdot2^3$。

---

## 3. φ(p^k) 的公式

[▶ 07:07](https://youtu.be/ouAlEMkHuyI?t=427)

**例**：
- $25 = 5^2$：除了 5 的倍數全部互質。1 到 25 有 $25/5 = 5$ 個 5 的倍數，所以 $\phi(25) = 25-5 = 20$。
- $27 = 3^3$：少的是 $3,6,9,\dots,27$，共 $27/3 = 9$ 個，所以 $\phi(27) = 27-9 = 18$。

**規律** [▶ 08:14](https://youtu.be/ouAlEMkHuyI?t=494)：
$$\phi(p) = p-1,\quad \phi(p^2) = p^2-p,\quad \phi(p^3) = p^3-p^2,\quad\dots,\quad \phi(p^k) = p^k - p^{k-1}.$$

**理由**：1 到 $p^k$ 共 $p^k$ 個數；和 $p^k$ 不互質 ⇔ 被 $p$ 整除；$p$ 的倍數有 $p^k/p = p^{k-1}$ 個。減掉就是答案。

**例** [▶ 09:19](https://youtu.be/ouAlEMkHuyI?t=559)：
- $\phi(25) = 5^2-5 = 20$；$\phi(27) = 3^3-3^2 = 18$。
- $625 = 5^4$：$\phi(625) = 5^4-5^3 = 625-125 = 500$。模 625 有 500 個可逆的數。

【口頭】大模數時當然不會真的列出整個單位群，所以這個公式很重要 [▶ 09:54](https://youtu.be/ouAlEMkHuyI?t=594)。

> 【課本補充】Lemma 5.4（p. 87）：$\phi(p^e) = p^e-p^{e-1} = p^{e-1}(p-1) = p^e\left(1-\tfrac1p\right)$。機率解釋：隨機取一個數，被 $p$ 整除的機率是 $1/p$，所以和 $p^e$ 互質的比例是 $1-1/p$。

---

## 4. Euler 定理

### 4.1 敘述與證明

[▶ 10:28](https://youtu.be/ouAlEMkHuyI?t=628)

上一集用過群論定理：有限群 $G$ 的階是 $n$，則每個 $x\in G$ 都有 $x^n = e$。套到 $U_n$：

**定理（Euler，1760）**：若 $\gcd(a,n) = 1$，則
$$a^{\phi(n)}\equiv1\ (\mathrm{mod}\ n).$$

**證明**：$\lvert U_n\rvert = \phi(n)$。$\gcd(a,n)=1$ ⇒ $[a]\in U_n$。群元素的「群的階」次方是單位元素：$[a]^{\phi(n)} = [1]$。這個 $\mathbb{Z}_n$ 裡的等式就是同餘 $a^{\phi(n)}\equiv1\ (\mathrm{mod}\ n)$。∎

（$n=p$ 質數時 $\phi(p) = p-1$，就是 Fermat 小定理。）

> 【課本補充】Theorem 5.3（p. 86）也給了 Fermat 小定理「證法一」的推廣：取**簡化剩餘系**（reduced set of residues）$R = \{r_1,\dots,r_{\phi(n)}\}$（每個單位類取一個代表）；$\gcd(a,n)=1$ 時 $aR$ 也是簡化剩餘系，乘積比較得 $a^{\phi(n)}r_1\cdots r_{\phi(n)}\equiv r_1\cdots r_{\phi(n)}$，約掉單位 $r_i$。Example 5.3：$U_{12} = \{\pm1,\pm5\}$，$\phi(12)=4$，$5^4 = 625\equiv1\ (\mathrm{mod}\ 12)$。

### 4.2 例子

**例 1** [▶ 11:37](https://youtu.be/ouAlEMkHuyI?t=697)：$\phi(625) = 500$，而 $121 = 11^2$ 和 625 互質，所以
$$121^{500}\equiv1\ (\mathrm{mod}\ 625).$$
【口頭】直接算會很痛苦。

**例 2** [▶ 12:11](https://youtu.be/ouAlEMkHuyI?t=731)：$\phi(20) = 8$、$\gcd(3,20) = 1$，所以 $3^8\equiv1\ (\mathrm{mod}\ 20)$。

於是 $3\cdot3^7\equiv1$，即 $3^7$ 是 3 在 $\mathbb{Z}_{20}$ 的反元素。算：
$$3^7 = 9\cdot9\cdot27 = 81\cdot27\equiv1\cdot7 = 7\ (\mathrm{mod}\ 20).$$
確實 $3\cdot7 = 21\equiv1$。

### 4.3 推論：反元素公式

[▶ 13:19](https://youtu.be/ouAlEMkHuyI?t=799)

**推論**：若 $[a]\in U_n$，則
$$[a]^{-1} = [a]^{\phi(n)-1}.$$

【口頭】有公式不代表好用。實際找反元素時，用猜的或用**向量輾轉相除法**比算 $a^{\phi(n)-1}$ 有效率得多。不過這公式有它的用途——下一集之後的 **RSA 加密**會看到 [▶ 13:53](https://youtu.be/ouAlEMkHuyI?t=833)。

---

## 5. 一頁速查表

**$U_n = \{[x] : \gcd(x,n)=1\}$ 是群**。
- 反元素：$ax+bn=1$ ⇒ $[x]^{-1}=[a]$。
- 封閉：$(a_1x+a_2n)(b_1y+b_2n) = 1$ ⇒ $a_1b_1xy+(\cdots)n = 1$ ⇒ $\gcd(xy,n)=1$。

**Euler 函數** $\phi(n) = \lvert U_n\rvert$。
- $\phi(2..10) = 1,2,2,4,2,6,4,6,4$；$\phi(20)=8$；$\phi(72)=24$。
- $\phi(p^k) = p^k-p^{k-1}$。關鍵：1 到 $p^k$ 中 $p$ 的倍數有 $p^{k-1}$ 個。
- $\phi(25)=20$、$\phi(27)=18$、$\phi(625)=500$。

**Euler 定理**：$\gcd(a,n)=1$ ⇒ $a^{\phi(n)}\equiv1\ (\mathrm{mod}\ n)$。
- 關鍵：$[a]\in U_n$，群裡 $x^{\lvert G\rvert}=e$。
- $121^{500}\equiv1\ (\mathrm{mod}\ 625)$；$3^8\equiv1\ (\mathrm{mod}\ 20)$。
- 推論：$[a]^{-1} = [a]^{\phi(n)-1}$（實務上用向量輾轉相除較快）。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\phi(p^k)$ | 第 15 集（$\phi$ 的乘法性、一般公式） |
| $U_n$ 的群結構 | 第 15 集（單位群的結構、原根） |
| Euler 定理、$a^{\phi(n)-1}$ | 第 16 集（RSA 加密） |
| $U_p$ | 第 17–18 集（二次剩餘） |

---

## 附：本集一句話總結

> **和 $n$ 互質的同餘類組成乘法群 $U_n$（反元素由 Bézout 給出），它的大小是 Euler 函數 $\phi(n)$，其中 $\phi(p^k)=p^k-p^{k-1}$；因為群元素的「群階」次方是單位元素，得到 Euler 定理 $a^{\phi(n)}\equiv1\ (\mathrm{mod}\ n)$，Fermat 小定理是 $n=p$ 的特例。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 14 錄影逐字稿（YouTube 自動字幕，14:41）與 Jones & Jones《Elementary Number Theory》§5.1–5.2 整理。*
