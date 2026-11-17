---
course: Number Theory（2021 秋，線上錄影）
episode: 10
lecture: Lecture 10
date: 待補（2021 秋）
video: https://youtu.be/743PRycdLDg
notes: Jones & Jones §3.1（書頁 37–46，PDF 頁 52–61）：Lemma 3.1–3.3、Example 3.1–3.6；線性同餘 §3.2（書頁 46–52）講者說留到後面
---

# 第 10 集 · Lecture 10：模運算（Modular Arithmetic） [▶ 影片](https://youtu.be/743PRycdLDg)

← 上一集：[09-irrationality-of-sqrt2](09-irrationality-of-sqrt2.md) ｜ [總目錄](README.md) ｜ 下一集：[11-modular-calculations-integer-roots](11-modular-calculations-integer-roots.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 10 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（35:32，自動字幕）＋ Jones & Jones §3.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 同餘的定義](#1-同餘的定義)
- [2. 同餘類與 Z_n](#2-同餘類與-z_n)
- [3. 同餘類 = 餘數相同](#3-同餘類--餘數相同)
- [4. 計算例子](#4-計算例子)
- [5. 乘法反元素、零因子、單位](#5-乘法反元素零因子單位)
- [6. 解線性同餘](#6-解線性同餘)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 段落 | 內容 | 課本 |
|---|---|---|
| 1–3 | 同餘、同餘類、$\mathbb{Z}_n$ 的加乘 | §3.1 Lemma 3.1–3.3 |
| 4 | 用 mod 算大數的餘數 | Example 3.3–3.5 |
| 5 | 單位 $\iff\gcd(x,n)=1$；用向量輾轉相除求反元素 | （課本在 §3.2、§5.1） |
| 6 | 解 $ax\equiv b\ (\mathrm{mod}\ n)$ 的初步 | §3.2 |

---

## 1. 同餘的定義

[▶ 00:01](https://youtu.be/743PRycdLDg?t=1)

**定義**：$n$ 是正整數，$x,y$ 是整數。
$$x\equiv y\ (\mathrm{mod}\ n) \iff n\mid y-x \iff x = y+nj \text{ 對某個 } j\in\mathbb{Z}.$$
讀作「$x$ 同餘 $y$ 模 $n$」（$x$ is congruent to $y$ mod $n$）。也就是 $x$ 和 $y$ 差一個 $n$ 的倍數。

**模 $n$ 同餘是 $\mathbb{Z}$ 上的等價關係**（第 1 集的定義）。

> 【課本補充】課本的定義（p. 38）是「$a,b$ 除以 $n$ 的餘數相同」，再用 Lemma 3.1 證明等價於 $n\mid a-b$——和講者的順序相反（講者在第 3 節證這個等價）。Lemma 3.2 證等價關係：反身 $n\mid a-a$；對稱 $n\mid a-b\Rightarrow n\mid b-a$；遞移 $n\mid(a-b)+(b-c) = a-c$。

**定理（同餘可以加、可以乘）** [▶ 00:35](https://youtu.be/743PRycdLDg?t=35)：若 $x\equiv x'$、$y\equiv y'\ (\mathrm{mod}\ n)$，則
$$x+y\equiv x'+y',\qquad xy\equiv x'y'\ (\mathrm{mod}\ n).$$

**證明**：$x' = x+jn$、$y' = y+kn$。
- 相加：$x'+y' = (x+y) + (j+k)n$。
- 相乘：$x'y' = xy + (xk+yj+jkn)n$。

把含 $n$ 的項放一起，就看出同餘。∎

---

## 2. 同餘類與 Z_n

[▶ 01:41](https://youtu.be/743PRycdLDg?t=101)

**定義**：$x$ 的**同餘類**（residue class / congruence class，就是等價類）
$$\bar x = [x] = x+n\mathbb{Z} = \{\,x+nj : j\in\mathbb{Z}\,\}.$$
講者兩種記號都用。

所有同餘類的集合記作 $\mathbb{Z}_n$（讀作「$\mathbb{Z}$ mod $n$」，也寫 $\mathbb{Z}/n\mathbb{Z}$）：
$$\mathbb{Z}_n = \{\bar x : x\in\mathbb{Z}\} = \{\bar0,\bar1,\dots,\overline{n-1}\}.$$

**運算**（用代表來定義）：
$$\bar x\pm\bar y = \overline{x\pm y},\qquad \bar x\,\bar y = \overline{xy}.$$
上面的定理保證這是 **well-defined**（和代表的選擇無關，第 1 集的觀念）。

**例**：
- $\mathbb{Z}_2 = \{\bar0,\bar1\}$：$\bar0 = 2\mathbb{Z}$（偶數）、$\bar1 = 1+2\mathbb{Z}$（奇數）。可以有意義地把這兩個**集合**相加相乘，這就是模 2 運算。
- $\mathbb{Z}_3 = \{\bar0,\bar1,\bar2\}$：把整數分成 3 的倍數、3 的倍數 +1、+2。
  - $\bar1+\bar2 = \bar3 = \bar0$（3 的倍數在 $\mathbb{Z}_3$ 裡都變成 0）。
  - $\bar2\cdot\bar2 = \bar4 = \bar1$。

> 【課本補充】p. 41–42：**冪次**可以定義（$[a]^k=[a^k]$），但「把指數也當成同餘類」不 well-defined：在 $\mathbb{Z}_3$，$[1]=[4]$，但 $2^1 = 2$、$2^4 = 16\equiv1$，結果不同。所以只在 $\mathbb{Z}_n$ 裡做加、減、乘、冪。

---

## 3. 同餘類 = 餘數相同

[▶ 05:09](https://youtu.be/743PRycdLDg?t=309)

**定理**：$\bar x = \bar y$（集合相等）$\iff$ $x$、$y$ 除以 $n$ 的餘數相同。

【口頭】除以 $n$ 的餘數也叫 residue，但講者盡量不用這個詞，也不定義它。

**證明**：
- (⇒) $\bar x = \bar y$，所以 $x = y+nj$。由除法演算法 $x = q_1n+r_1$、$y = q_2n+r_2$，$0\le r_1,r_2<n$。代入整理：
$$(q_1-q_2-j)\,n = r_2-r_1.$$
取絕對值：$|q_1-q_2-j|\,n = |r_2-r_1| < n$（兩個 $[0,n)$ 裡的數相距小於 $n$）。所以 $q_1-q_2-j = 0$，於是 $r_1=r_2$。
- (⇐) 餘數都是 $r$：$y - x = (q_2-q_1)n$，所以 $n\mid y-x$，$\bar x = \bar y$。∎

**推論** [▶ 08:01](https://youtu.be/743PRycdLDg?t=481)：
$$n\mid x \iff \bar x = \bar0 \iff x\equiv0\ (\mathrm{mod}\ n).$$

【口頭】注意：$x\equiv0$ 是**同餘**不是等號。想把同餘變成等式，就到 $\mathbb{Z}_n$ 裡寫 $\bar x = \bar0$ [▶ 08:35](https://youtu.be/743PRycdLDg?t=515)。

---

## 4. 計算例子

**性質**（講者證了第一條，用歸納；其餘類似）[▶ 10:47](https://youtu.be/743PRycdLDg?t=647)：
$$\bar x_1+\cdots+\bar x_k = \overline{x_1+\cdots+x_k},\quad \bar x_1\cdots\bar x_k = \overline{x_1\cdots x_k},\quad \bar x^k = \overline{x^k},\quad \overline{x+nj} = \bar x,\quad \bar n\,\bar x = \bar0.$$

**重點**：計算時，$n$ 的倍數都可以直接丟掉。

**例 1**：$3672\times254$ 能被 7 整除嗎？[▶ 09:06](https://youtu.be/743PRycdLDg?t=546)

在 $\mathbb{Z}_7$ 裡分別化簡兩個因數：
- $254 = 210+44 = 7\cdot30+7\cdot6+2$，所以 $\overline{254} = \bar2$。
- $3672$：講者拆成 $3500+172$，再把 172 拆成 $7\cdot20+22$、$22 = 7\cdot3+1$，得 $\overline{3672}=\bar1$，最後結論「餘數是 2，不被 7 整除」。

⚠️ 待確認（講者算錯）：$140+22 = 162\neq172$。正確是 $172 = 7\cdot24+4$，所以 $\overline{3672} = \bar4$（$3672 = 7\cdot524+4$），乘積 $\bar4\cdot\bar2 = \bar8 = \bar1$。**結論「不被 7 整除」仍然對，但餘數是 1 不是 2**（筆記用 Python 驗證：$3672\cdot254 \bmod 7 = 1$）。

**例 2**：$3^{20}$ 在 $\mathbb{Z}_{13}$ [▶ 11:56](https://youtu.be/743PRycdLDg?t=716)
$$3^{20} = 3^2\cdot3^{18} = 3^2\cdot(3^3)^6 = 9\cdot27^6.$$
$27 = 26+1$，$26 = 2\cdot13$，所以 $\overline{27} = \bar1$，$\overline{27}^6 = \bar1$。於是 $\overline{3^{20}} = \bar9$。

⚠️ 逐字稿缺字：講者一度說成「nineteen」，馬上改口「nine」。

【口頭】記號 [▶ 13:03](https://youtu.be/743PRycdLDg?t=783)：
- 中括號比橫線好寫，講者會兩種混用。
- 同時用兩個模數時，可以加下標，如 $[9]_{13}$。
- 熟了之後大家會把橫線、括號都省略；但本集講者盡量都寫。

**例 3**：$288\times45$ 除以 7 的餘數 [▶ 14:11](https://youtu.be/743PRycdLDg?t=851)
- $288 = 280+8 = 7\cdot40+7+1$ → $\bar1$。
- $45 = 6\cdot7+3$ → $\bar3$。
- 乘積 $\bar1\cdot\bar3 = \bar3$，餘數是 3。

> 【課本補充】Example 3.3–3.5（p. 42–43）用**最小絕對值剩餘**（least absolute residues，取 $-n/2<r\le n/2$）讓計算更省：
> - $28\times33 \bmod 35$：$28\equiv-7$、$33\equiv-2$，乘積 $\equiv14$。
> - $3^8\bmod13$：$3^2 = 9\equiv-4$，$3^4\equiv16\equiv3$，$3^8\equiv9$。
> - Example 3.6：$6\mid a(a+1)(2a+1)$ 對所有 $a$：檢查 $a\equiv0,\pm1,\pm2,3\ (\mathrm{mod}\ 6)$ 每種情況。

---

## 5. 乘法反元素、零因子、單位

### 5.1 零因子沒有反元素

[▶ 15:50](https://youtu.be/743PRycdLDg?t=950)

加法反元素沒問題：$\bar x$ 的加法反元素是 $\overline{-x}$。乘法比較麻煩。

在 $\mathbb{Z}_6$：$\bar2\cdot\bar3 = \bar6 = \bar0$，但 $\bar2\neq\bar0$、$\bar3\neq\bar0$。

**$\bar2$ 沒有反元素**（講者的旁註）[▶ 16:55](https://youtu.be/743PRycdLDg?t=1015)：若 $\bar2^{-1}$ 存在，把 $\bar2\cdot\bar3=\bar0$ 兩邊左乘 $\bar2^{-1}$：
$$\bar2^{-1}\bar2\,\bar3 = \bar2^{-1}\bar0 \ \Rightarrow\ \bar3 = \bar0,$$
荒謬。一般地，**零因子不可能有乘法反元素**。

### 5.2 定義

[▶ 18:03](https://youtu.be/743PRycdLDg?t=1083)

- $\bar x$ 的**乘法反元素**：$\bar y$ 使 $\bar x\bar y = \bar1$，記作 $\bar x^{-1}$。
- 有反元素的 $\bar x$ 叫**單位**（unit）；$\mathbb{Z}_n$ 所有單位的集合記作 $U_n$。
- 若 $\bar x\bar y = \bar0$ 而 $\bar x,\bar y\neq\bar0$，則 $\bar x,\bar y$ 叫**零因子**（zero divisor）。

$\mathbb{Z}_n$ 的元素只有三種：$\bar0$、零因子、單位。

**例**：
- $\mathbb{Z}_6 = \{\bar0,\dots,\bar5\}$ [▶ 19:11](https://youtu.be/743PRycdLDg?t=1151)：$\bar2,\bar3,\bar4$ 是零因子（$\bar3\cdot\bar4 = \overline{12} = \bar0$）；$\bar0$ 不是單位也不是零因子（依定義）；$\bar1\cdot\bar1 = \bar1$、$\bar5\cdot\bar5 = \overline{25} = \bar1$，所以 $U_6 = \{\bar1,\bar5\}$，各自是自己的反元素。
- $\mathbb{Z}_7$ [▶ 20:17](https://youtu.be/743PRycdLDg?t=1217)：$U_7 = \{\bar1,\dots,\bar6\}$，因為
$$2\cdot4 = 8\equiv1,\quad 3\cdot5 = 15\equiv1,\quad 1\cdot1 = 1,\quad 6\cdot6 = 36\equiv1\ (\mathrm{mod}\ 7).$$

【口頭】接下來講者不再唸出「bar」，因為「快把我逼瘋了」[▶ 19:44](https://youtu.be/743PRycdLDg?t=1184)。

### 5.3 單位的判準

[▶ 21:21](https://youtu.be/743PRycdLDg?t=1281)

**定理**：
$$U_n = \{\,\bar x\in\mathbb{Z}_n : \gcd(x,n) = 1\,\}.$$
而且若 $\gcd(x,n)=1$，由 Bézout 得 $ax+bn = 1$，則 $\bar x^{-1} = \bar a$。

**證明**：
- (⇒) $\bar x$ 是單位，有 $\bar y$ 使 $\overline{xy} = \bar1$，即 $xy + nj = 1$ 對某個 $j$。整數線性組合等於 1，所以 $x,n$ 互質（第 5 集推論 1）。
- (⇐) $\gcd(x,n)=1$，Bézout 給 $ax+bn = 1$。取同餘類，$n$ 的倍數消失：$\bar a\bar x = \bar1$，所以 $\bar x^{-1} = \bar a$。∎

### 5.4 例：$\mathbb{Z}_{200}$

[▶ 23:31](https://youtu.be/743PRycdLDg?t=1411)（「這種我不建議用猜的」）

求 $x=20, 23, 50$ 在 $\mathbb{Z}_{200}$ 的反元素：
- $20\mid200$、$50\mid200$，$\gcd(20,200)=20$、$\gcd(50,200)=50$，不互質 → $\overline{20}$、$\overline{50}$ 不是單位。
- 23 和 200 互質。向量輾轉相除（$a=200$、$b=23$）：

| 數 | 組合 |
|---|---|
| 200 | $a$ |
| 23 | $b$ |
| 16 | $a-8b$ |
| 7 | $b-(a-8b) = -a+9b$ |
| 2 | $(a-8b)-2(-a+9b) = 3a-26b$ |
| 1 | $(-a+9b)-3(3a-26b) = -10a+87b$ |

所以 $-10\cdot200 + 87\cdot23 = 1$（$-2000+2001$）。模 200，200 那項消失：$\overline{87}\cdot\overline{23} = \bar1$，
$$\overline{23}^{-1} = \overline{87}.$$

⚠️ 待確認：[▶ 25:42](https://youtu.be/743PRycdLDg?t=1542) 字幕說最後一列是「minus 16a plus 87b」，但 $-16\cdot200+87\cdot23\neq1$；筆記重算得 $-10a+87b$。反元素 87 不受影響（筆記用 Python 驗證 $23^{-1}\bmod200 = 87$）。

【口頭】
- 剩餘數為 0 的最後一步不用做：看到餘數 1 就知道 gcd 是 1 [▶ 25:09](https://youtu.be/743PRycdLDg?t=1509)。
- 模數小（如 7）就直接試乘；模數大（如 200）才靠向量輾轉相除法 [▶ 26:18](https://youtu.be/743PRycdLDg?t=1578)。
- 期中考一定會考向量輾轉相除法：「如果期中考沒考它，我會覺得自己當老師失敗了。」[▶ 26:50](https://youtu.be/743PRycdLDg?t=1610)

### 5.5 例：$\mathbb{Z}_{11}$ 的反元素用湊的

[▶ 27:22](https://youtu.be/743PRycdLDg?t=1642)

11 是質數，除了 $\bar0$ 每個都是單位。小模數可以用巧思湊：

| 觀察 | 結論 |
|---|---|
| $3\cdot4 = 12\equiv1$ | $3^{-1}=4$、$4^{-1}=3$ |
| $3\cdot7 = 21\equiv-1$，平方：$9\cdot49\equiv1$，而 $49\equiv5$ | $9\cdot5\equiv1$：$9^{-1}=5$、$5^{-1}=9$ |
| $10\equiv-1$，$10^2\equiv1$ | $10^{-1}=10$ |
| $6\cdot6 = 36\equiv3$，乘 $4=3^{-1}$：$6\cdot24\equiv1$，$24\equiv2$ | $6\cdot2\equiv1$：$6^{-1}=2$、$2^{-1}=6$ |
| $7\cdot7 = 49\equiv5$，乘 $9=5^{-1}$：$7\cdot63\equiv1$，$63\equiv8$ | $7^{-1}=8$ |
| $1\cdot1=1$ | $1^{-1}=1$ |

**小技巧**：找到乘積 $\equiv-1$，平方就得到乘積 $\equiv1$ [▶ 28:30](https://youtu.be/743PRycdLDg?t=1710)。

---

## 6. 解線性同餘

[▶ 31:12](https://youtu.be/743PRycdLDg?t=1872)

【口頭】你可以選擇處理「同餘問題」或「$\mathbb{Z}_n$ 裡的等式問題」。講者偏好抽象的等式。

**例 1**：$3x\equiv10\ (\mathrm{mod}\ 11)$
- 改寫：$\bar3\bar x = \overline{10}$ 在 $\mathbb{Z}_{11}$。
- 上面算過 $\bar3^{-1} = \bar4$，兩邊乘 $\bar4$：$\bar x = \overline{40} = \bar7$。
- 所以 $x\equiv7\ (\mathrm{mod}\ 11)$。（檢查：$3\cdot7 = 21\equiv10$。）

**例 2**：$2x\equiv4\ (\mathrm{mod}\ 6)$ [▶ 32:17](https://youtu.be/743PRycdLDg?t=1937)
- $\bar2$ 在 $\mathbb{Z}_6$ 沒有反元素，不能用上面的方法。
- 但 $\mathbb{Z}_6$ 只有 6 個元素，**全部代進去試**（小學時答案太多不能這樣做，這裡可以）：

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $2x$ | 0 | 2 | 4 | 0 | 2 | 4 |

- 解：$x\equiv2$ 或 $x\equiv5\ (\mathrm{mod}\ 6)$。這次有**兩個**解。

⚠️ 逐字稿缺字：[▶ 33:22](https://youtu.be/743PRycdLDg?t=2002) 講者先說「x equals two bar and x equals four bar」，馬上改口為五（$2\cdot4 = 8\equiv2$，不是 4）。

**沒有解的情形** [▶ 33:54](https://youtu.be/743PRycdLDg?t=2034)：由上表，$2x$ 只取 $0,2,4$。所以 $2x\equiv1$、$3$、$5\ (\mathrm{mod}\ 6)$ 都**無解**。

**定理**：若 $\bar a$ 是單位，則 $ax\equiv b\ (\mathrm{mod}\ n)$ 有唯一解 $x\equiv cb\ (\mathrm{mod}\ n)$，其中 $\bar c = \bar a^{-1}$。（證明就是例 1 的計算。）

【口頭】Jones & Jones pp. 46–52 對解任何線性同餘有很好的建議，後面的集數（講者說 lecture 12）會講很多 [▶ 35:00](https://youtu.be/743PRycdLDg?t=2100)。

---

## 7. 一頁速查表

**同餘**：$x\equiv y\ (\mathrm{mod}\ n)\iff n\mid y-x\iff$ 餘數相同。是等價關係。
- 可加可乘。關鍵：$x' = x+jn$、$y'=y+kn$ ⇒ $x'y' = xy+(xk+yj+jkn)n$。

**$\mathbb{Z}_n$** $= \{\bar0,\dots,\overline{n-1}\}$，$\bar x+\bar y = \overline{x+y}$、$\bar x\bar y = \overline{xy}$（well-defined）。$n$ 的倍數可以丟掉。

**計算**：先把每個因數化簡再乘。$3^{20}\equiv9\cdot(27)^6\equiv9\ (\mathrm{mod}\ 13)$；$288\cdot45\equiv1\cdot3 = 3\ (\mathrm{mod}\ 7)$。

**單位**：$U_n = \{\bar x : \gcd(x,n)=1\}$。
- 關鍵：$\bar x\bar y = \bar1\iff xy+nj = 1\iff$ 互質。
- 求反元素：Bézout $ax+bn = 1$ ⇒ $\bar x^{-1} = \bar a$。例：$23^{-1}\equiv87\ (\mathrm{mod}\ 200)$。
- 零因子 $\bar x\bar y=\bar0$（都非零）沒有反元素。

**線性同餘** $ax\equiv b\ (\mathrm{mod}\ n)$
- $\bar a$ 是單位 ⇒ 唯一解 $x\equiv a^{-1}b$。
- 否則模數小時全部代入：$2x\equiv4\ (\mathrm{mod}\ 6)$ ⇒ $x\equiv2,5$；$2x\equiv1,3,5$ 無解。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 線性同餘的一般解法 | 第 11–12 集（課本 §3.2；中國剩餘定理） |
| 用 mod 算大數 | 第 11 集（模運算計算、多項式的整數根） |
| 單位群 $U_n$、$\gcd(x,n)=1$ | 第 14–15 集（單位群、Euler 函數） |
| 反元素用 Bézout | 第 16 集（RSA 的解密指數） |
| $\mathbb{Z}_p$（$p$ 質數）每個非零元素都是單位 | 第 13 集（Fermat 小定理）；$\mathbb{Z}_p$ 是體 |

---

## 附：本集一句話總結

> **模 $n$ 同餘是等價關係，同餘類組成 $\mathbb{Z}_n$，可以加、乘（丟掉 $n$ 的倍數）；$\bar x$ 有乘法反元素恰好當 $\gcd(x,n)=1$，反元素由 Bézout $ax+bn=1$ 給出 $\bar a$——所以 $\bar a$ 是單位時 $ax\equiv b$ 有唯一解 $x\equiv a^{-1}b$。**

---

## ⚠️ 待確認清單

1. [▶ 09:39](https://youtu.be/743PRycdLDg?t=579) 例 1 講者把 $3672$ 模 7 算成 1（拆 $172 = 7\cdot20+22$ 是錯的），正確是 4，乘積餘數是 1 不是 2；結論「不被 7 整除」不變。
2. [▶ 25:42](https://youtu.be/743PRycdLDg?t=1542) $\mathbb{Z}_{200}$ 例子的 Bézout 係數字幕是「$-16a+87b$」，筆記重算為 $-10a+87b$，不知是字幕錯還是板書錯。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 10 錄影逐字稿（YouTube 自動字幕，35:32）與 Jones & Jones《Elementary Number Theory》§3.1 整理。*
