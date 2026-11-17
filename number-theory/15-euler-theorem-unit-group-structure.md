---
course: Number Theory（2021 秋，線上錄影）
episode: 15
lecture: Lecture 15
date: 待補（2021 秋）
video: https://youtu.be/3oq1C2sOXdU
notes: Jones & Jones §5.2 Theorem 5.6（書頁 88，PDF 頁 103）；第 6 章 The Group of Units（書頁 97–118，PDF 頁 112–133），尤其 §6.2 原根、§6.6 應用（pp. 110–113）、§6.7 $U_n$ 的結構、§6.8 universal exponent
---

# 第 15 集 · Lecture 15：Euler 函數與單位群的結構 [▶ 影片](https://youtu.be/3oq1C2sOXdU)

← 上一集：[14-group-of-units-euler-function](14-group-of-units-euler-function.md) ｜ [總目錄](README.md) ｜ 下一集：[16-rsa-encryption](16-rsa-encryption.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 15 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（43:12，自動字幕）＋ Jones & Jones §5.2、第 6 章
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 同構](#1-同構)
- [2. 循環群](#2-循環群)
- [3. 直積](#3-直積)
- [4. φ 的乘法性](#4-φ-的乘法性)
- [5. 直積中元素的階、循環群的子群](#5-直積中元素的階循環群的子群)
- [6. U_n 的結構定理](#6-u_n-的結構定理)
- [7. 群指數](#7-群指數)
- [8. 用生成元解非線性同餘](#8-用生成元解非線性同餘)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者的開場預告 [▶ 00:00](https://youtu.be/3oq1C2sOXdU?t=0)：
1. 把 $U_n$ 寫成（同構意義下）循環群的直積；
2. 由此找出**群指數**——之後 RSA 會用到；
3. $U_n$ 是循環群時，用代換解某些非線性同餘；
4. 更多計算 $\phi$ 的公式。

【口頭】需要一些群論。講者盡量不花時間證群論的東西，只提醒定義、偶爾證一點，所以這集會有一些群論細節的缺口 [▶ 00:31](https://youtu.be/3oq1C2sOXdU?t=31)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1–3 | 同構、循環群、直積；$\mathbb{Z}_r\times\mathbb{Z}_s\cong\mathbb{Z}_{rs}$ | 附錄 B |
| 4 | $U_{rs}\cong U_r\times U_s$；$\phi(rs)=\phi(r)\phi(s)$ | Theorem 5.6 |
| 6 | $U_{p^n}$ 循環（$p$ 奇）；$U_{2^n}\cong\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}$ | §6.3–6.7 |
| 7–8 | 群指數；用生成元解 $x^4\equiv c\ (\mathrm{mod}\ 11)$ | §6.6、§6.8 |

---

## 1. 同構

[▶ 01:03](https://youtu.be/3oq1C2sOXdU?t=63)

**定義**：群 $(G,*)$ 和 $(H,\star)$ **同構**（isomorphic），寫 $G\cong H$，如果有雙射 $\psi:G\to H$ **保持運算**：
$$\psi(a*b) = \psi(a)\star\psi(b).$$
（一個可能是加法群、另一個是乘法群，加法就變成乘法。）

**例：$\mathbb{Z}_n\cong$ $n$ 次單位根** [▶ 01:38](https://youtu.be/3oq1C2sOXdU?t=98)

令 $\omega = e^{2\pi i/n}$（**本原 $n$ 次單位根**，primitive / principal $n$-th root of unity；也寫 $\omega_n$ 或 $\zeta_n$），$\omega^n = 1$。
$$H = \{1,\omega,\omega^2,\dots,\omega^{n-1}\}\ (\text{乘法}),\qquad \psi([j]) = \omega^j.$$
- **Well-defined**：若 $[j] = [j']$，則 $j' = j+nk$，$\omega^{j'} = \omega^j(\omega^n)^k = \omega^j$。所以不管代表怎麼選，結果一樣。
- **雙射**：有反函數（$\omega^j\mapsto[j]$）。
- **保持運算**：$\psi([j]+[k]) = \omega^{j+k} = \omega^j\omega^k = \psi([j])\psi([k])$。指數裡的加法變成乘法。

**具體**：$\mathbb{Z}_4\cong\{1,i,-1,-i\}$（$e^{\pi i/2} = i$）。

【口頭】之後的複數那集會再談；講者認為所有老師都該多懂複數運算，「我知道，一般的算術就夠頭痛了，為什麼還要複雜的（complex）算術」[▶ 04:53](https://youtu.be/3oq1C2sOXdU?t=293)。

---

## 2. 循環群

[▶ 05:28](https://youtu.be/3oq1C2sOXdU?t=328)

**定義**：$n$ 階群 $G$ 叫**循環群**（cyclic，生成元為 $g$），如果
$$G = \{e, g, g^2, \dots, g^{n-1}\},\quad\text{寫 } G = \langle g\rangle.$$
加法群就是 $\{0, g, 2g, \dots, (n-1)g\}$。

【口頭】有人唸「sick-lick」，有人唸「sigh-click」——「後者是錯的，開玩笑的。」

**例**：
- $\mathbb{Z}_n$ 是循環的：1 一直加就得到全部。
- $U_{10} = \{1,3,7,9\}$ [▶ 06:01](https://youtu.be/3oq1C2sOXdU?t=361)：
  - $3^2 = 9$、$3^3 = 27\equiv7$、$3^4 = 81\equiv1$：3 的冪得到全部。
  - $7^2 = 49\equiv9$、$7^3\equiv63\equiv3$、$7^4\equiv1$：7 也是生成元。
  - 9 不行：$9^2\equiv1$，只生成 $\{1,9\}$，9 的階是 2。

  所以 $U_{10}$ 是循環群，生成元 3 和 7。4 階群要有 4 階的元素才能生成；沒有和群一樣大的階的元素，就不是循環群。

**定理**：同階的循環群都同構 [▶ 07:09](https://youtu.be/3oq1C2sOXdU?t=429)。$G = \langle x\rangle$、$H=\langle y\rangle$ 都是 $n$ 階，令 $\psi(x^m) = y^m$，可證是同構（細節略）。

**例**：$\mathbb{Z}_4$ 和 $U_{10}$ 都是 4 階循環群，所以 $U_{10}\cong\mathbb{Z}_4$——同一個群，只是記號不同。

【口頭】同構保持很多性質，例如**元素的階**。$U_{10}$ 有兩個 4 階元素、一個 2 階元素和單位元素，所以 $\mathbb{Z}_4$ 也是 [▶ 08:15](https://youtu.be/3oq1C2sOXdU?t=495)。

---

## 3. 直積

[▶ 09:24](https://youtu.be/3oq1C2sOXdU?t=564)

**定義**：群 $G_1,\dots,G_k$ 的**直積**（direct product）$G_1\times\cdots\times G_k$ 是笛卡兒積，運算**逐分量**：
$$(g_1,\dots,g_k)(h_1,\dots,h_k) = (g_1h_1,\dots,g_kh_k).$$
（加法群就逐分量相加。也可以混合，但本課只用全乘法或全加法。）

**例**：$\mathbb{Z}_2\times\mathbb{Z}_3$ [▶ 10:29](https://youtu.be/3oq1C2sOXdU?t=629)

（講者錄到一半，太太的手機有郵件、兒子把他的手機拿去玩遊戲。）

6 個元素。把 $(1,1)$ 一直加：
$$(0,0),\ (1,1),\ (0,2),\ (1,0),\ (0,1),\ (1,2),$$
正好是全部。所以 $\mathbb{Z}_2\times\mathbb{Z}_3$ 是 6 階循環群，$\cong\mathbb{Z}_6$。

**定理**：若 $\gcd(r,s)=1$，則 $\mathbb{Z}_r\times\mathbb{Z}_s\cong\mathbb{Z}_{rs}$ [▶ 12:12](https://youtu.be/3oq1C2sOXdU?t=732)。

**證明**：$\psi([x]_{rs}) = ([x]_r, [x]_s)$。
- Well-defined（講者說明了）。
- **映成**：任取 $([a]_r,[b]_s)$，要找 $x$ 使 $x\equiv a\ (\mathrm{mod}\ r)$、$x\equiv b\ (\mathrm{mod}\ s)$——這正是**中國剩餘定理**（模數互質，有唯一解 mod $rs$）。
- 兩邊都有 $rs$ 個元素，映成就自動一對一，所以是雙射。
- 保持加法。∎

【口頭】這是講中國剩餘定理的原因之一：它不只用來解聯立同餘，也是這個同構的關鍵 [▶ 12:44](https://youtu.be/3oq1C2sOXdU?t=764)。

---

## 4. φ 的乘法性

### 4.1 $U_{rs}\cong U_r\times U_s$

[▶ 14:22](https://youtu.be/3oq1C2sOXdU?t=862)

**定理**：若 $\gcd(r,s) = 1$，則 $U_{rs}\cong U_r\times U_s$。（互質不能少。）

**證明**：同一個公式 $\psi([x]_{rs}) = ([x]_r,[x]_s)$，這次保持乘法。
1. **落在 $U_r\times U_s$**：若 $\gcd(x,rs) = 1$，Bézout 給 $ax+brs = 1$。把它看成 $ax + (bs)r = 1$ 和 $ax + (br)s = 1$，所以 $\gcd(x,r) = \gcd(x,s) = 1$。
2. **保持乘法**：$\psi([x][y]) = ([xy]_r,[xy]_s) = ([x]_r[y]_r,[x]_s[y]_s) = \psi([x])\psi([y])$。
3. **一對一** [▶ 17:05](https://youtu.be/3oq1C2sOXdU?t=1025)：若 $\psi([x]) = \psi([y])$，則 $y-x = jr$ 且 $y-x = ks$。$r\mid ks$ 而 $\gcd(r,s)=1$，所以 $r\mid k$，$k = rl$，$y-x = srl$，即 $x\equiv y\ (\mathrm{mod}\ rs)$。
4. **映成**：中國剩餘定理（解出的 $x$ 自動和 $rs$ 互質）。∎

【口頭】講者說 $U_{rs}$ 和 $U_r\times U_s$ 元素個數相同「不是馬上明顯的」，所以這裡分開證一對一和映成。（寫到「中國剩餘定理」時他開玩笑說「這可能有爭議」。）

### 4.2 $\phi$ 是乘法函數

[▶ 18:43](https://youtu.be/3oq1C2sOXdU?t=1123)

**定理（$\phi$ 的乘法性）**：若 $\gcd(r,s)=1$，則
$$\phi(rs) = \phi(r)\,\phi(s).$$

**證明**：同構是雙射，保持元素個數：$\lvert U_{rs}\rvert = \lvert U_r\times U_s\rvert = \lvert U_r\rvert\cdot\lvert U_s\rvert$。∎

> 【課本補充】Theorem 5.6（p. 88）用排列證明：把 $1,\dots,mn$ 排成 $n$ 列 $m$ 行（第 $c$ 行是 $c, m+c, \dots, (n-1)m+c$）。同一行模 $m$ 同餘，所以恰有 $\phi(m)$ 行和 $m$ 互質；每一行是模 $n$ 的完全剩餘系（Lemma 5.5），各有 $\phi(n)$ 個和 $n$ 互質。合計 $\phi(m)\phi(n)$。互質不能少：$\phi(2)^2\neq\phi(4)$。

**例** [▶ 19:48](https://youtu.be/3oq1C2sOXdU?t=1188)：
- $\phi(24) = \phi(3)\phi(8) = 2\cdot4 = 8$。
- $\phi(20) = \phi(4)\phi(5) = 2\cdot4 = 8$。
- $\phi(72) = \phi(8)\phi(9) = 4\cdot6 = 24$。
- $\phi(3000) = \phi(3)\phi(2^3)\phi(5^3) = 2\cdot(8-4)\cdot(125-25) = 2\cdot4\cdot100 = 800$。

（3000 以下和 3000 互質的數有 800 個；大於 3000 的話當然無限多。）

**一般公式** [▶ 22:35](https://youtu.be/3oq1C2sOXdU?t=1355)：$n = p_1^{k_1}\cdots p_s^{k_s}$（相異質數），反覆用乘法性：
$$\phi(n) = \phi(p_1^{k_1})\cdots\phi(p_s^{k_s}) = \prod_{i}\left(p_i^{k_i}-p_i^{k_i-1}\right).$$

【口頭】講者發現掃描的講義這裡漏寫了下標，要週五再重掃；這時他的樂高卡片斷了——「所以暗號是 broken」[▶ 23:08](https://youtu.be/3oq1C2sOXdU?t=1388)。

**問題**：$U_{3000}$ 有 800 個元素，它是循環群嗎？有沒有 800 階的元素？接下來幾頁就在找回答這問題的工具 [▶ 22:02](https://youtu.be/3oq1C2sOXdU?t=1322)。

---

## 5. 直積中元素的階、循環群的子群

**直積中元素的階** [▶ 23:40](https://youtu.be/3oq1C2sOXdU?t=1420)：
$$\mathrm{ord}(g_1,\dots,g_k) = \mathrm{lcm}\big(\mathrm{ord}(g_1),\dots,\mathrm{ord}(g_k)\big).$$

**例**：$(3,2)\in U_5\times U_7$。
- 模 5：$3^4 = 81\equiv1$，最小，所以 3 的階是 4。
- 模 7：$2^3 = 8\equiv1$，所以 2 的階是 3。
- $(3,2)$ 的階 $= \mathrm{lcm}(4,3) = 12$：$(3,2)^j = (3^j,2^j)$ 在 $j=12$ 第一次變成 $(1,1)$。

**循環群的事實**（群論，講者不證，「要好幾個小時才能證好」）[▶ 25:50](https://youtu.be/3oq1C2sOXdU?t=1550)：
- $n$ 階循環群有 $\phi(n)$ 個生成元。
- 對每個 $d\mid n$，有一個 $d$ 階子群，它是循環的，有 $\phi(d)$ 個生成元（所以恰有 $\phi(d)$ 個 $d$ 階元素）。
- $\displaystyle\sum_{d\mid n}\phi(d) = n$。

**推論**：若 $n$ 階群有**超過** $\phi(d)$ 個 $d$ 階元素（$d\mid n$），它就不是循環群。

**例** [▶ 26:55](https://youtu.be/3oq1C2sOXdU?t=1615)：
- $\mathbb{Z}_{30}$：30 的因數 $1,2,3,5,6,10,15,30$，$\phi$ 值 $1,1,2,4,2,4,8,8$，加起來 30。✓
- $U_8 = \{1,3,5,7\}$ **不是循環群**：$3^2 = 9\equiv1$、$5^2 = 25\equiv1$、$7^2 = 49\equiv1$，有三個 2 階元素，但 $\phi(2) = 1$，循環群最多一個 2 階元素。

【口頭】所以回答「$U_{3000}$ 是循環群嗎」的線索：找到超過一個 2 階元素，就結束了——不是循環群 [▶ 28:03](https://youtu.be/3oq1C2sOXdU?t=1683)。

---

## 6. U_n 的結構定理

[▶ 28:03](https://youtu.be/3oq1C2sOXdU?t=1683)

**定理**（講者只敘述）：
- $p$ 質數：$U_p\cong\mathbb{Z}_{p-1}$（循環）。
- $p$ 奇質數：$U_{p^n}\cong\mathbb{Z}_{p^n-p^{n-1}}$（循環）。
- $U_2\cong\{0\}$（平凡群）；$n\ge2$ 時
$$U_{2^n}\cong\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}\quad(\text{不是循環群，} n\ge3).$$

兩種情況元素個數都對：$\lvert\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}\rvert = 2\cdot2^{n-2} = 2^{n-1} = 2^n-2^{n-1}$。結構不同（循環 vs. 不循環），計數一樣 [▶ 28:40](https://youtu.be/3oq1C2sOXdU?t=1720)。

（$n=2$ 時 $\mathbb{Z}_2\times\mathbb{Z}_1\cong\mathbb{Z}_2\cong U_4$，還是循環的；上面「不是循環群」只在 $n\ge3$。這是筆記依公式補的。）

**例** [▶ 29:51](https://youtu.be/3oq1C2sOXdU?t=1791)：
- $U_{16} = U_{2^4}\cong\mathbb{Z}_2\times\mathbb{Z}_4$，8 個元素（$\phi(16)=8$）。
- $U_{80}\cong U_5\times U_{16}\cong\mathbb{Z}_4\times\mathbb{Z}_2\times\mathbb{Z}_4$，$4\cdot2\cdot4 = 32$ 個元素。
- $U_{42}\cong U_2\times U_3\times U_7\cong\{0\}\times\mathbb{Z}_2\times\mathbb{Z}_6\cong\mathbb{Z}_2\times\mathbb{Z}_6$（和平凡群的直積可以丟掉），$\phi(42) = 12$。

這三個都**不是循環群**：$U_{16}$ 沒有 8 階元素、$U_{80}$ 沒有 32 階元素、$U_{42}$ 沒有 12 階元素。

【口頭】作業問「是不是循環群」時，最簡單的答法是找兩個 2 階元素 [▶ 31:29](https://youtu.be/3oq1C2sOXdU?t=1889)。

> 【課本補充】第 6 章的完整內容：§6.2 **原根**（primitive root，$U_n$ 的生成元）；§6.3–6.4 證 $U_{p^e}$（$p$ 奇）循環、$U_{2^e}$ 的結構；§6.5 原根存在 $\iff n = 1,2,4,p^e,2p^e$（$p$ 奇質數）；§6.7 $U_n$ 的代數結構；§6.8 universal exponent（即下面的群指數）。這些證明本集都沒講。

---

## 7. 群指數

[▶ 32:01](https://youtu.be/3oq1C2sOXdU?t=1921)

**定義**：群 $G$ 的**群指數**（group exponent）$e$ 是使 $x^e = 1$ 對**所有** $x\in G$ 成立的最小正整數。

- 因為 $x^{\lvert G\rvert} = 1$，$e\le\lvert G\rvert$；事實上 $e\mid\lvert G\rvert$。
- $G$ 循環時 $e = \lvert G\rvert$；不循環時比較有趣。
- 同構保持元素的階，所以可以在同構的群裡算。

**例 1**：$U_{35}\cong U_5\times U_7\cong\mathbb{Z}_4\times\mathbb{Z}_6$ [▶ 33:07](https://youtu.be/3oq1C2sOXdU?t=1987)
- $(x,y)$ 的階是 $\mathrm{lcm}(\mathrm{ord}\,x,\mathrm{ord}\,y)$，最大是 $\mathrm{lcm}(4,6) = 12$。Jones & Jones 說得很清楚：取 4 和 6 的最小公倍數。
- 每個元素加 12 次都回到 0：$12(x,y) = (3\cdot4x, 2\cdot6y) = (0,0)$。所以群指數是 12。
- **找出 12 階元素**：$(2,3)\in U_5\times U_7$，2 在 $U_5$ 的階是 4、3 在 $U_7$ 的階是 6（講者用計算機算）。用中國剩餘定理解 $x\equiv2\ (\mathrm{mod}\ 5)$、$x\equiv3\ (\mathrm{mod}\ 7)$，得 $x\equiv17\ (\mathrm{mod}\ 35)$。17 在 $U_{35}$ 的階是 12。

⚠️ 逐字稿缺字：[▶ 35:25](https://youtu.be/3oq1C2sOXdU?t=2125) 字幕先說「x congruent to 13 mod 35」再說「that number 17 has order 12」。$13\equiv3\ (\mathrm{mod}\ 5)$ 不符；$17\equiv2\ (\mathrm{mod}\ 5)$、$17\equiv3\ (\mathrm{mod}\ 7)$ 才對，所以是 17。

**例 2**：$U_{33}\cong U_3\times U_{11}\cong\mathbb{Z}_2\times\mathbb{Z}_{10}$ [▶ 35:58](https://youtu.be/3oq1C2sOXdU?t=2158)
- 群指數 $= \mathrm{lcm}(2,10) = 10$。
- 找 10 階元素：2 在 $U_3$ 的階是 2，3 在 $U_{11}$ 的階是 5（$3^5 = 243\equiv1$），$(2,3)$ 的階 $\mathrm{lcm}(2,5)=10$。解 $x\equiv2\ (\mathrm{mod}\ 3)$、$x\equiv3\ (\mathrm{mod}\ 11)$：$x\equiv14\ (\mathrm{mod}\ 33)$。
- $\lvert U_{33}\rvert = 20$，但最大的階是 10，所以 $U_{33}$ **不是循環群**。

【口頭】群指數在 RSA 加密會很有用 [▶ 37:39](https://youtu.be/3oq1C2sOXdU?t=2259)。

---

## 8. 用生成元解非線性同餘

[▶ 38:11](https://youtu.be/3oq1C2sOXdU?t=2291)

**想法**：若 $U_n$ 是循環群、生成元 $g$，則每個單位都是 $g^j$。把未知數代換成 $x = g^j$，**指數只要模 $\phi(n)$ 相等**，非線性同餘就變成線性同餘。

$U_{11}$ 是 10 階循環群，2 是生成元。2 的冪模 11：

| $j$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $2^j\bmod11$ | 2 | 4 | 8 | 5 | 10 | 9 | 7 | 3 | 6 | 1 |

**例 1**：$x^4\equiv18\ (\mathrm{mod}\ 11)$
- $18\equiv7$ 是單位，所以 $x$ 也必須是單位，$x = 2^j$。
- $7 = 2^7$。方程變成 $2^{4j} = 2^7$，即
$$4j\equiv7\ (\mathrm{mod}\ 10).$$
- $\gcd(4,10) = 2\nmid7$，**無解**。

**例 2**：$x^4\equiv3\ (\mathrm{mod}\ 11)$ [▶ 40:24](https://youtu.be/3oq1C2sOXdU?t=2424)
- $3 = 2^8$，得 $4j\equiv8\ (\mathrm{mod}\ 10)$。
- $\gcd(4,10) = 2\mid8$，有兩個解：猜 $j=2$，另一個是 $2+10/2 = 7$。
- $x = 2^2 = 4$、$x = 2^7\equiv7$。

**解**：$x\equiv4$ 或 $x\equiv7\ (\mathrm{mod}\ 11)$。（檢查：$4^4 = 256 = 253+3$；$7^4 = 2401 = 2398+3$。）

【口頭】
- 這技巧很強：本來沒有方法處理四次同餘（除了全部代入檢查），現在只要解模 $\phi(n)$ 的線性同餘 [▶ 41:29](https://youtu.be/3oq1C2sOXdU?t=2489)。
- Jones & Jones pp. 110–113 把這推廣到更複雜的模數（$U_n$ 是直積、或偶數模數用 5 的冪的技巧）；作業大概只考本集的程度，「太深入細節了」[▶ 42:03](https://youtu.be/3oq1C2sOXdU?t=2523)。

---

## 9. 一頁速查表

**同構、循環群**
- $\psi:G\to H$ 雙射且 $\psi(ab)=\psi(a)\psi(b)$。$\mathbb{Z}_n\cong\{\omega^j\}$（$\omega = e^{2\pi i/n}$）。
- 同階循環群同構；$U_{10} = \langle3\rangle\cong\mathbb{Z}_4$。

**直積**：逐分量運算；$\mathrm{ord}(g_1,\dots,g_k) = \mathrm{lcm}(\mathrm{ord}\,g_i)$。

**互質時**（關鍵：中國剩餘定理給映成）
- $\mathbb{Z}_r\times\mathbb{Z}_s\cong\mathbb{Z}_{rs}$；$U_{rs}\cong U_r\times U_s$。
- $\phi(rs) = \phi(r)\phi(s)$；$\phi\left(\prod p_i^{k_i}\right) = \prod(p_i^{k_i}-p_i^{k_i-1})$。$\phi(3000) = 800$。

**循環群**：$n$ 階有 $\phi(n)$ 個生成元；每個 $d\mid n$ 恰有 $\phi(d)$ 個 $d$ 階元素；$\sum_{d\mid n}\phi(d) = n$。
- 超過一個 2 階元素 ⇒ 不循環（$U_8$）。

**$U_n$ 的結構**
- $U_{p^n}\cong\mathbb{Z}_{p^n-p^{n-1}}$（$p$ 奇）；$U_{2^n}\cong\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}$（$n\ge2$）。
- $U_{80}\cong\mathbb{Z}_4\times\mathbb{Z}_2\times\mathbb{Z}_4$；$U_{42}\cong\mathbb{Z}_2\times\mathbb{Z}_6$。

**群指數** $e$：最小的 $e$ 使所有 $x^e=1$。$U_{35}$：$\mathrm{lcm}(4,6) = 12$（元素 17）；$U_{33}$：$\mathrm{lcm}(2,10) = 10$（元素 14）。

**非線性同餘**：$U_n = \langle g\rangle$ ⇒ 令 $x = g^j$，$x^k\equiv g^m$ ⇔ $kj\equiv m\ (\mathrm{mod}\ \phi(n))$。
- $x^4\equiv7\ (\mathrm{mod}\ 11)$：$4j\equiv7\ (\mathrm{mod}\ 10)$ 無解。
- $x^4\equiv3\ (\mathrm{mod}\ 11)$：$4j\equiv8$ ⇒ $j = 2,7$ ⇒ $x\equiv4,7$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 群指數、$\phi(pq)=(p-1)(q-1)$ | 第 16 集（RSA 加密、解密指數） |
| $U_p$ 循環、生成元 | 第 17–18 集（二次剩餘：$a$ 是平方剩餘 ⇔ 指數 $j$ 是偶數） |
| $n$ 次單位根 $\omega = e^{2\pi i/n}$ | 第 19 集（複數與單位根） |
| 直積、同構的語言 | 第 22–23 集（高斯整數、四元數） |

---

## 附：本集一句話總結

> **中國剩餘定理給出同構 $U_{rs}\cong U_r\times U_s$（$r,s$ 互質），所以 $\phi$ 是乘法函數；$U_{p^n}$（$p$ 奇）是循環群而 $U_{2^n}\cong\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}$，由此算出群指數（各分量階數的 lcm），而在循環的 $U_n$ 裡令 $x=g^j$，就把 $x^k\equiv c$ 化成模 $\phi(n)$ 的線性同餘。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 15 錄影逐字稿（YouTube 自動字幕，43:12）與 Jones & Jones《Elementary Number Theory》§5.2、第 6 章整理。*
