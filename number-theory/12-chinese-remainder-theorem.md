---
course: Number Theory（2021 秋，線上錄影）
episode: 12
lecture: Lecture 12
date: 待補（2021 秋）
video: https://youtu.be/uaqHImi8i3Y
notes: Jones & Jones §3.2–3.3（書頁 46–57，PDF 頁 61–72）：Theorem 3.7、Corollary 3.8、Lemma 3.9、p. 50–51 的解法步驟、Example 3.9–3.13、Theorem 3.10（中國剩餘定理）
---

# 第 12 集 · Lecture 12：線性同餘與中國剩餘定理（Chinese Remainder Theorem） [▶ 影片](https://youtu.be/uaqHImi8i3Y)

← 上一集：[11-modular-calculations-integer-roots](11-modular-calculations-integer-roots.md) ｜ [總目錄](README.md) ｜ 下一集：[13-fermat-little-theorem](13-fermat-little-theorem.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 12 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（42:13，**whisper 轉錄**；YouTube 字幕下載被擋）＋ Jones & Jones §3.2–3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 線性同餘的解](#1-線性同餘的解)
- [2. 化簡同餘的兩招](#2-化簡同餘的兩招)
- [3. 解線性同餘的流程](#3-解線性同餘的流程)
- [4. 中國剩餘定理](#4-中國剩餘定理)
- [5. 聯立同餘的例子](#5-聯立同餘的例子)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】本集只講**線性**同餘和聯立同餘；非線性同餘不打算講一般方法（Jones & Jones 有）[▶ 00:00](https://youtu.be/uaqHImi8i3Y?t=0)。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | $ax\equiv b\ (\mathrm{mod}\ n)$ 有解 ⇔ $d\mid b$，恰 $d$ 個解 | Theorem 3.7、Corollary 3.8 |
| 2–3 | 化簡的兩招與解題流程 | Lemma 3.9、p. 50–51 |
| 4–5 | 中國剩餘定理（構造性證明）與例子 | Theorem 3.10 |

---

## 1. 線性同餘的解

### 1.1 定理

[▶ 00:00](https://youtu.be/uaqHImi8i3Y?t=0)

**定理**：$d = \gcd(a,n)$。
- $ax\equiv b\ (\mathrm{mod}\ n)$ 有解 $\iff d\mid b$。
- 若 $d\mid b$ 且 $x_0$ 是一個解，則所有解是
$$x = x_0 + \frac{n}{d}\,t,\qquad t\in\mathbb{Z}.$$
- 在 $\mathbb{Z}_n$ 裡等價地說：$\bar a\bar x = \bar b$ 的解集是
$$\left\{\bar x_0,\ \overline{x_0+\tfrac nd},\ \overline{x_0+\tfrac{2n}d},\ \dots,\ \overline{x_0+\tfrac{(d-1)n}{d}}\right\},$$
**恰好 $d$ 個**相異同餘類。$d=1$ 時只有一個解。

### 1.2 證明

[▶ 01:29](https://youtu.be/uaqHImi8i3Y?t=89)

這是第 5 集**線性丟番圖方程**的近親。回想：$ax+by=c$ 有解 ⇔ $\gcd(a,b)\mid c$，通解 $x = x_0+\frac bdm$、$y = y_0-\frac adm$。

而
$$ax\equiv b\ (\mathrm{mod}\ n) \iff ax + jn = b \text{ 對某個整數 } j.$$
對照：$n$ 扮演 $b$ 的角色（固定），$j$ 是另一個變數，$b$ 扮演 $c$ 的角色。所以有解 ⇔ $\gcd(a,n)\mid b$，且 $x = x_0+\frac{n}{d}t$（$j$ 的公式「我用不太到，但它在那裡」）。

**為什麼只有 $d$ 個同餘類** [▶ 04:40](https://youtu.be/uaqHImi8i3Y?t=280)：$t$ 只要取 $0,1,\dots,d-1$。取 $t=d$ 得 $x_0+n\equiv x_0$，開始重複。

【口頭】「如果你的人生取決於它，可以把最後這部分寫得更嚴謹。」

> 【課本補充】Theorem 3.7 的證明（p. 47）把這點寫清楚：$x_0+\frac{nt}{d}\equiv x_0+\frac{nt'}{d}\ (\mathrm{mod}\ n)\iff n\mid\frac{n(t-t')}{d}\iff d\mid t-t'$。所以 $t$ 跑過模 $d$ 的完全剩餘系，正好得到 $d$ 個類。課本也指出：這 $d$ 個類合起來其實是**一個**模 $n/d$ 的類 $[x_0]_{n/d}$。

### 1.3 例子

**例 1**（回顧第 10 集）[▶ 05:16](https://youtu.be/uaqHImi8i3Y?t=316)：$2x\equiv4\ (\mathrm{mod}\ 6)$。$\gcd(2,6) = 2\mid4$，有解。猜 $x_0 = 2$。通解 $2+\frac62t = 2+3t$，$t = 0,1$：$x\equiv2,5\ (\mathrm{mod}\ 6)$。和第 10 集逐一代入的結果一樣。

**例 2**：$5x\equiv8\ (\mathrm{mod}\ 20)$。$\gcd(5,20) = 5\nmid8$，**無解**（$\bar5\bar x = \bar8$ 在 $\mathbb{Z}_{20}$ 也無解）。

**例 3**：$5x\equiv15\ (\mathrm{mod}\ 20)$ [▶ 07:10](https://youtu.be/uaqHImi8i3Y?t=430)。$\gcd = 5\mid15$，有 5 個解。猜 $x_0 = 3$。通解 $3+\frac{20}5t = 3+4t$：
$$x\equiv3,7,11,15,19\ (\mathrm{mod}\ 20).$$

### 1.4 推論：唯一解 ⇔ 互質

[▶ 08:24](https://youtu.be/uaqHImi8i3Y?t=504)

**推論**：$ax\equiv b\ (\mathrm{mod}\ n)$ 對每個 $b$ 都有唯一解 $\iff\gcd(a,n) = 1$。

**證明**：$d>1$ 時要嘛無解（$d\nmid b$）、要嘛 $d$ 個解。$d=1$ 時 $\bar a$ 是單位，兩邊乘 $\bar a^{-1}$ 得唯一解 $\bar x = \bar a^{-1}\bar b$。∎

**例**：$121x\equiv10\ (\mathrm{mod}\ 300)$ [▶ 09:36](https://youtu.be/uaqHImi8i3Y?t=576)
- $\gcd(121,300) = 1$，有唯一解。
- 用 Bill Cook 的網站（考試時用向量輾轉相除法）：$-119\cdot121 + 48\cdot300 = 1$，所以 $121^{-1}\equiv-119\equiv181\ (\mathrm{mod}\ 300)$。
- 兩邊乘 181：$x\equiv1810\equiv10\ (\mathrm{mod}\ 300)$。

【口頭】算完回頭看：「我早該知道的！」$121\cdot10 = 1210 = 4\cdot300+10$。「事後諸葛總是 20/20。」[▶ 12:09](https://youtu.be/uaqHImi8i3Y?t=729)

---

## 2. 化簡同餘的兩招

[▶ 12:49](https://youtu.be/uaqHImi8i3Y?t=769)

互質時有找反元素的演算法；但 $d\ge2$ 時找特解 $x_0$ 到目前只能猜。下面是把同餘換成**等價**、更好解的同餘的方法，基本上只有兩招。

**例**（講者先示範）：
- 「$1000\cdot(\cdots)$」型：$a$、$b$、模數都被 1000 整除，三個一起除以 1000，得 $x\equiv2\ (\mathrm{mod}\ 3)$。
- $17x\equiv34\ (\mathrm{mod}\ 20)$：兩邊除以 17（模數不變），得 $x\equiv2\ (\mathrm{mod}\ 20)$。

⚠️ 待確認：[▶ 13:28](https://youtu.be/uaqHImi8i3Y?t=808) 第一個例子的原式字幕沒唸出，只說「divide by a thousand, a thousand, a thousand」得 $x\equiv2\ (\mathrm{mod}\ 3)$，推測原式是 $1000x\equiv2000\ (\mathrm{mod}\ 3000)$。字幕又說「$x\equiv2$ mod 3000 solves star」，但除以 1000 後的等價同餘是 mod 3（模 3000 有 1000 個解）。

⚠️ 逐字稿缺字：第二個例子字幕說「divided 17 by 2 and 34 by 2」，應為除以 17（$17/17 = 1$、$34/17 = 2$）。

**定理** [▶ 14:09](https://youtu.be/uaqHImi8i3Y?t=849)：
1. **三個一起除**：若 $m$ 整除 $a,b,n$，令 $a' = a/m$、$b' = b/m$、$n' = n/m$，則
$$ax\equiv b\ (\mathrm{mod}\ n)\iff a'x\equiv b'\ (\mathrm{mod}\ n')$$
（同一組整數 $x$ 同時解兩者）。
2. **只除 $a,b$**：若 $\gcd(a,n) = 1$ 且 $m$ 整除 $a,b$，則
$$ax\equiv b\ (\mathrm{mod}\ n)\iff a'x\equiv b'\ (\mathrm{mod}\ n)$$
（**模數不變**；前提是 $a$ 和 $n$ 互質。例如 $17$ 和 $20$ 互質，所以上面除以 17 合法。）

**證明** [▶ 15:32](https://youtu.be/uaqHImi8i3Y?t=932)：
1. $ax\equiv b\ (\mathrm{mod}\ n)\iff ax+nj = b$。代 $a = ma'$、$n = mn'$、$b = mb'$，除以 $m\neq0$：$a'x+n'j = b'$，即 $a'x\equiv b'\ (\mathrm{mod}\ n')$。兩個方向都可以走。
2. $\gcd(m,n) = 1$：否則 $m$ 和 $n$ 的公因數也整除 $a = ma'$，和 $\gcd(a,n)=1$ 矛盾。所以 $\bar m^{-1}$ 在 $\mathbb{Z}_n$ 存在。$\bar a\bar x = \bar b$ 即 $\bar m\bar a'\bar x = \bar m\bar b'$，乘 $\bar m^{-1}$：$\bar a'\bar x = \bar b'$。∎

**差別**：第 1 招**改變模數**，第 2 招**模數不變** [▶ 18:03](https://youtu.be/uaqHImi8i3Y?t=1083)。

> 【課本補充】這是 Lemma 3.9（p. 49）。Exercise 3.6：第 2 招在 $a,n$ 不互質時可能錯。

---

## 3. 解線性同餘的流程

[▶ 18:37](https://youtu.be/uaqHImi8i3Y?t=1117)

【口頭】講者畫了一張「很可怕的流程圖」，是 Jones & Jones p. 50 的摘要（課本多做了一點）。

**在解什麼**：$ax\equiv b\ (\mathrm{mod}\ n)$ 的所有解。

**步驟**：
1. 算 $d = \gcd(a,n)$。$d\nmid b$ → 無解，停。
2. $d\mid b$ → 通解 $x_0+\frac ndt$，$t = 0,\dots,d-1$。現在只要找**一個** $x_0$。
3. 先試著**猜** $x_0$。（講者說這對他給的幾乎任何例子都行。）
4. 猜不到：用第 1 招除以 $d$，得 $a'x\equiv b'\ (\mathrm{mod}\ n')$，此時 $\gcd(a',n') = 1$。
5. 還不好解：用第 2 招除以 $m = \gcd(a',b')$，得 $a''x\equiv b''\ (\mathrm{mod}\ n')$。
6. 必要時把 $b''$ 加減模數的倍數（同餘不變），湊出和 $a''$ 有公因數的數，再回到第 5 步。
7. 目標：化成 $\pm x\equiv(\cdots)$，讀出 $x_0$，回到第 2 步。

【口頭】這不是說這是最好的方法，你可能一開始就猜到；這只是示範定理怎麼用 [▶ 21:05](https://youtu.be/uaqHImi8i3Y?t=1265)。

> 【課本補充】p. 50–51 的 Step 4 另一個做法：乘上適當常數 $c$ 讓 $ca''$ 的最小絕對值剩餘變小。Example 3.13：$4x\equiv13\ (\mathrm{mod}\ 47)$，$4\cdot12 = 48\equiv1$，乘 12 得 $x\equiv12\cdot13\equiv15$。

**例 1**：$20x\equiv30\ (\mathrm{mod}\ 45)$ [▶ 21:43](https://youtu.be/uaqHImi8i3Y?t=1303)
1. $\gcd(20,45) = 5\mid30$，有 5 個解。
2. 第 1 招除以 5：$4x\equiv6\ (\mathrm{mod}\ 9)$。
3. 第 2 招除以 $\gcd(4,6) = 2$（$\gcd(4,9)=1$）：$2x\equiv3\ (\mathrm{mod}\ 9)$。
4. **狡猾的一步**：模 9 可以加 9：$2x\equiv12\ (\mathrm{mod}\ 9)$。再除以 2：$x\equiv6\ (\mathrm{mod}\ 9)$。
5. 通解 $x = 6+\frac{45}5t = 6+9t$，$t = 0,\dots,4$：$x\equiv6,15,24,33,42\ (\mathrm{mod}\ 45)$。

**例 2**：$10x\equiv6\ (\mathrm{mod}\ 14)$ [▶ 23:30](https://youtu.be/uaqHImi8i3Y?t=1410)
1. $\gcd(10,14) = 2\mid6$。
2. 除以 2：$5x\equiv3\ (\mathrm{mod}\ 7)$。
3. $3+7 = 10$：$5x\equiv10\ (\mathrm{mod}\ 7)$；除以 5：$x\equiv2\ (\mathrm{mod}\ 7)$。
4. 通解 $2+7t$，$t = 0,1$：$x\equiv2,9\ (\mathrm{mod}\ 14)$。

（課本 Example 3.12 就是這題。）

---

## 4. 中國剩餘定理

### 4.1 背景

[▶ 24:35](https://youtu.be/uaqHImi8i3Y?t=1475)

【口頭】叫「中國」剩餘定理，是因為它出現在相當古老的中國文獻裡。這類問題出現在計算行星、恆星的聯合運動：時間有週期性（例如現在 5 點、過 300 小時是幾點？用 mod 24 算），太陽、月亮、行星各有不同的軌道週期——天文學，「更糟的是占星學」[▶ 25:19](https://youtu.be/uaqHImi8i3Y?t=1519)。

> 【課本補充】p. 52：西元 1 世紀中國數學家孫子考慮過「一個數除以 3、5、7 餘 2、3、2」這類問題。若模數不互質可能無解：$x\equiv3\ (\mathrm{mod}\ 9)$ 和 $x\equiv2\ (\mathrm{mod}\ 6)$ 互相矛盾（前者 $3\mid x$、後者 $3\nmid x$）。Theorem 3.10 的天文應用：週期互質的事件會以週期 $n = \prod n_i$ 同時發生（行星合、日月食）。

### 4.2 敘述

[▶ 25:58](https://youtu.be/uaqHImi8i3Y?t=1558)

**定理（中國剩餘定理，CRT）**：$n_1,\dots,n_k$ 是**兩兩互質**的正整數，$a_1,\dots,a_k$ 是任意整數。則聯立同餘
$$x\equiv a_1\ (\mathrm{mod}\ n_1),\quad x\equiv a_2\ (\mathrm{mod}\ n_2),\quad\dots,\quad x\equiv a_k\ (\mathrm{mod}\ n_k)$$
的解恰好是**一個**模 $N = n_1n_2\cdots n_k$ 的同餘類。

【口頭】讀到這種敘述會以為證明很可怕，其實不但不可怕，還是**構造性**的：證明直接告訴你怎麼解。講者很喜歡這個標準證明 [▶ 26:36](https://youtu.be/uaqHImi8i3Y?t=1596)。

### 4.3 證明（同時是演算法）

[▶ 27:10](https://youtu.be/uaqHImi8i3Y?t=1630)

1. 令 $N = n_1\cdots n_k$，$M_j = N/n_j$（除了 $n_j$ 以外所有模數的乘積）。
2. 觀察：
   - $M_j\equiv0\ (\mathrm{mod}\ n_i)$ 對所有 $i\neq j$（$M_j$ 含 $n_i$ 這個因數）。
   - $\gcd(M_j,n_j) = 1$（$n_j$ 和其他模數都沒有公因數）。
3. 所以 $\bar M_j^{-1}$ 在 $\mathbb{Z}_{n_j}$ 存在：取整數 $d_j$ 使
$$M_jd_j\equiv1\ (\mathrm{mod}\ n_j).$$
4. **公式**：
$$x_0 = a_1M_1d_1 + a_2M_2d_2 + \cdots + a_kM_kd_k. \tag{$*$}$$
5. **驗證**：模 $n_j$ 時，$i\neq j$ 的項都含 $M_i\equiv0$，只剩
$$x_0\equiv a_jM_jd_j\equiv a_j\cdot1 = a_j\ (\mathrm{mod}\ n_j).$$
$j$ 任意，所以 $x_0$ 同時滿足 $k$ 個同餘。
6. **唯一（模 $N$）** [▶ 29:41](https://youtu.be/uaqHImi8i3Y?t=1781)：若 $y$ 也是解，則 $y\equiv a_i\equiv x_0\ (\mathrm{mod}\ n_i)$，所以每個 $n_i\mid y-x_0$。$n_i$ 兩兩互質，所以乘積 $N\mid y-x_0$（第 5 集推論 3 反覆用），即 $y\equiv x_0\ (\mathrm{mod}\ N)$。∎

---

## 5. 聯立同餘的例子

**例 1** [▶ 31:01](https://youtu.be/uaqHImi8i3Y?t=1861)：
$$x\equiv3\ (\mathrm{mod}\ 7),\quad x\equiv10\ (\mathrm{mod}\ 19),\quad x\equiv6\ (\mathrm{mod}\ 3).$$
- $n_1,n_2,n_3 = 7,19,3$，$N = 399$。
- $M_1 = 19\cdot3 = 57$、$M_2 = 7\cdot3 = 21$、$M_3 = 7\cdot19 = 133$。
- $a_1,a_2,a_3 = 3,10,6$。
- $d_1$：$57\equiv1\ (\mathrm{mod}\ 7)$，反元素 1，$d_1 = 1$。
- $d_2$：$21\equiv2\ (\mathrm{mod}\ 19)$。向量輾轉相除：$19 = 9\cdot2+1$，$1 = 19-9\cdot2$，所以 $2^{-1}\equiv-9\equiv10$，$d_2 = 10$。（「然後我想：廢話，$2\cdot10 = 20\equiv1$。但我需要這個計算才看得出來。」）
- $d_3$：$133\equiv1\ (\mathrm{mod}\ 3)$，$d_3 = 1$。
- 公式：
$$x_0 = 3\cdot57\cdot1 + 10\cdot21\cdot10 + 6\cdot133\cdot1 = 171+2100+798 = 3069\equiv276\ (\mathrm{mod}\ 399).$$
- 檢查：$276 = 39\cdot7+3$ ✓；$276 = 14\cdot19+10$ ✓；$276\equiv0\equiv6\ (\mathrm{mod}\ 3)$ ✓。

**解**：$x\equiv276\ (\mathrm{mod}\ 399)$。

【口頭】期中考可以帶一頁筆記，講者說他一定會把中國剩餘定理寫上去，因為很容易記錯一點點 [▶ 35:13](https://youtu.be/uaqHImi8i3Y?t=2113)。

**例 2：代入法** [▶ 35:53](https://youtu.be/uaqHImi8i3Y?t=2153)
$$7x\equiv3\ (\mathrm{mod}\ 12),\qquad 10x\equiv6\ (\mathrm{mod}\ 14).$$
- 左邊不是單純的 $x$，不能直接套 CRT；講者這題也不用 CRT。
- $\gcd(7,12) = 1$，第一式有唯一解（mod 12）；$\gcd(10,14) = 2\mid6$，第二式有解。
- 先解第一式：向量輾轉相除得 $1 = 3\cdot12-5\cdot7$，$7^{-1}\equiv-5\equiv7\ (\mathrm{mod}\ 12)$。（「廢話，$7\cdot7 = 49\equiv1$，7 是自己的反元素。」）乘 7：$x\equiv49\cdot x\equiv21\equiv9\ (\mathrm{mod}\ 12)$。
- 代入第二式：$10\cdot9 = 90 = 6\cdot14+6\equiv6$ ✓。

所以 $x = 9$ 同時解兩式。**代入法**：解出一個同餘，代進另一個——解方程組的很多技巧在同餘組都有類比。

（以下**不是逐字稿內容**，是依 CRT 推論的完整答案：第一式等價於 $x\equiv9\ (\mathrm{mod}\ 12)$，第二式等價於 $x\equiv2\ (\mathrm{mod}\ 7)$；兩個模數互質，CRT 給唯一的 $x\equiv9\ (\mathrm{mod}\ 84)$。注意 $x = 21$ 雖然滿足第一式，但 $21\equiv0\ (\mathrm{mod}\ 7)$ 不滿足第二式，所以「第一式只有一個解」要理解成「模 12 只有一類」。）

**例 3：另一種做法** [▶ 38:56](https://youtu.be/uaqHImi8i3Y?t=2336)

同一組。第二式用第 1 招除以 2：$5x\equiv3\ (\mathrm{mod}\ 7)$。$5\cdot3 = 15\equiv1$，$5^{-1} = 3$，乘 3：$x\equiv9\equiv2\ (\mathrm{mod}\ 7)$。第一式乘 $7^{-1} = 7$：$x\equiv9\ (\mathrm{mod}\ 12)$。$x = 9$ 解兩者。

⚠️ 逐字稿缺字：[▶ 38:56](https://youtu.be/uaqHImi8i3Y?t=2336) whisper 把例 3 唸成「10x congruent to 6 mod 12」，從後面的計算看是 mod 14（和例 2 同一組）。

**例 4** [▶ 40:45](https://youtu.be/uaqHImi8i3Y?t=2445)

【口頭】本集暗號是「watch」。

講者給了一組三個同餘，用第 1 招各除以 2，化成和例 1 **相同的模數** 7、19、3：
$$x\equiv5\ (\mathrm{mod}\ 7),\quad x\equiv3\ (\mathrm{mod}\ 19),\quad x\equiv2\ (\mathrm{mod}\ 3).$$
可以重用例 1 的 $M_j$、$d_j$，只換 $a_j$：
$$x_0 = 5\cdot57\cdot1 + 3\cdot21\cdot10 + 2\cdot133\cdot1 = 285+630+266 = 1181\equiv383\ (\mathrm{mod}\ 399).$$
（檢查：$383 = 54\cdot7+5$、$383 = 20\cdot19+3$、$383 = 127\cdot3+2$。）

⚠️ 待確認：除以 2 之前的原始三個同餘，字幕沒唸出。

---

## 6. 一頁速查表

**線性同餘** $ax\equiv b\ (\mathrm{mod}\ n)$，$d = \gcd(a,n)$
- 有解 $\iff d\mid b$；通解 $x_0+\frac ndt$，恰 $d$ 個類（$t = 0..d-1$）。
- 關鍵：$ax\equiv b\iff ax+jn = b$，就是線性丟番圖方程。
- 唯一解 $\iff\gcd(a,n) = 1$，$x\equiv a^{-1}b$。例：$121^{-1}\equiv181\ (\mathrm{mod}\ 300)$。

**化簡兩招**
1. $m\mid a,b,n$：三個都除 → 模數變 $n/m$。
2. $\gcd(a,n) = 1$、$m\mid a,b$：只除 $a,b$ → 模數不變（$\bar m^{-1}$ 存在）。
- 再加上：$b$ 可加減 $n$ 的倍數湊整除。

**例**：$20x\equiv30\ (45)\to4x\equiv6\ (9)\to2x\equiv3\equiv12\ (9)\to x\equiv6\ (9)$ ⇒ $6,15,24,33,42\ (\mathrm{mod}\ 45)$。

**中國剩餘定理**：$n_i$ 兩兩互質 ⇒ $x\equiv a_i\ (\mathrm{mod}\ n_i)$ 的解是唯一的一類 mod $N = \prod n_i$。
- $M_j = N/n_j$，$d_j = M_j^{-1}\bmod n_j$，$x_0 = \sum a_jM_jd_j$。
- 關鍵：模 $n_j$ 時 $M_i\equiv0$（$i\neq j$），$M_jd_j\equiv1$。
- 例：$(3,10,6)$ mod $(7,19,3)$：$M = 57,21,133$，$d = 1,10,1$，$x\equiv276\ (\mathrm{mod}\ 399)$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| CRT | 第 13 集（模 $n$ 同餘 ⇔ 模每個質數冪同餘） |
| CRT 給映成 | 第 15 集（$\mathbb{Z}_r\times\mathbb{Z}_s\cong\mathbb{Z}_{rs}$、$U_{rs}\cong U_r\times U_s$；找最大階元素） |
| 線性同餘的解法 | 第 15 集（$4j\equiv8\ (\mathrm{mod}\ 10)$ 型的指數方程） |
| 反元素 | 第 16 集（RSA 解密指數） |

---

## 附：本集一句話總結

> **$ax\equiv b\ (\mathrm{mod}\ n)$ 就是線性丟番圖方程 $ax+jn=b$，所以 $\gcd(a,n)\mid b$ 才有解、且恰有 $\gcd(a,n)$ 個類；模數兩兩互質的聯立同餘由中國剩餘定理給出唯一解 $x_0=\sum a_jM_jd_j\ (\mathrm{mod}\ \prod n_j)$，證明本身就是演算法。**

---

## ⚠️ 待確認清單

1. [▶ 13:28](https://youtu.be/uaqHImi8i3Y?t=808) 「除以 1000」例子的原式沒唸出（推測 $1000x\equiv2000\ (\mathrm{mod}\ 3000)$），且講者說「$x\equiv2$ mod 3000」與化簡結果 mod 3 不一致。
2. [▶ 40:45](https://youtu.be/uaqHImi8i3Y?t=2445) 例 4 除以 2 之前的原始同餘沒唸出。
3. 本集逐字稿是 whisper（large-v3-turbo）轉錄，不是 YouTube 字幕；時間點可能和影片差 1–2 秒。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 12 錄影的 whisper 逐字稿（42:13）與 Jones & Jones《Elementary Number Theory》§3.2–3.3 整理。*
