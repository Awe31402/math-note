---
course: Abstract Algebra I (Fall 2016)
episode: 5
lecture: L4
date: 2016-09-05
video: https://www.youtube.com/watch?v=PHqmS3JUpf4
notes: AlgebraInotes_2018.pdf §1.1 Prequel 1（p.9–15）
---

# 第 5 集 · L4：除法算則、整除、gcd、輾轉相除法與 Bézout 等式 [▶ 影片](https://www.youtube.com/watch?v=PHqmS3JUpf4&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[04-L3-中心-中心化子-二面體群]] ｜ [總目錄](../README.md) ｜ 下一集：[[06-習題課-Gallian第2-3章]] →

## 本集概要

- **除法算則**（非零除數版）：$a = qb + r$，$0\le r<|b|$，$q,r$ 唯一。
- **整除**的定義與基本性質；$a\mid b$ 且 $b\mid a \iff a=\pm b$。
- **最大公因數** gcd；關鍵引理 $a = qb+r \Rightarrow \gcd(a,b) = \gcd(b,r)$。
- **輾轉相除法 (Euclidean algorithm)**：最後一個非零餘數就是 gcd；倒推回去得到**擴展輾轉相除法**，寫出 $\gcd(a,b) = ka + lb$，也就是 **Bézout 等式**。
- 應用：用 Bézout 等式**有系統地求模反元素**，為下一講的模運算打底。

> 📘 講義對應：2018 講義 §1.1 Prequel 1「integers」（p.8–15）。老師口頭說的編號（如「1.4.3」「Lemma 1.4.13」）是 2016 版講義，2018 版分別是 Thm 1.1.3、Lemma 1.1.13。

---

## 筆記

### 1. 除法算則 [▶ 00:00](https://youtu.be/PHqmS3JUpf4?t=0)

> **定理（非零除數的除法算則 nonzero division algorithm）**　設 $a,b\in\mathbb{Z}$，$b\neq 0$。則存在**唯一**的商 $q\in\mathbb{Z}$ 與餘數 $r\in\mathbb{Z}$，使得
> $$a = qb + r,\qquad 0\le r<|b|.$$

**證明思路**（課堂只講大意，細節在講義）[▶ 01:32](https://youtu.be/PHqmS3JUpf4?t=92)：
- 先處理 $b>0$：看集合 $\{a - nb \mid n\in\mathbb{Z},\ a-nb\ge 0\}$。它是非空的非負整數集，由**良序原理 (well-ordering principle)** 有最小元素，這個最小元素就是餘數 $r$。
- 再把 $b<0$ 的情況化成 $b>0$。

這個結果會引導後面所有的思考。

> **Gallian 10th ed., p.2**（Theorem 0.1 Division Algorithm）: *"Let a and b be integers with b > 0. Then there exist unique integers q and r with the property that a = bq + r, where 0 ≤ r < b."*

### 2. 整除與質數 [▶ 02:32](https://youtu.be/PHqmS3JUpf4?t=152)

> **定義（整除 divides）**　設 $a,b\in\mathbb{Z}$。若存在 $c\in\mathbb{Z}$ 使得 $a = bc$，則說 **$b$ 整除 $a$**，記作 $b\mid a$。此時也說 $b$ 是 $a$ 的**因數 (factor / divisor)**。

注意 $b\mid a$ 是一個**敘述**（真或假），**不是運算** [▶ 03:33](https://youtu.be/PHqmS3JUpf4?t=213)。

> **定義（質數 prime）** [▶ 04:03](https://youtu.be/PHqmS3JUpf4?t=243)　若 $p\in\mathbb{N}$ 滿足「$n\mid p \Rightarrow n = p$ 或 $n=1$」，則 $p$ 是**質數**。

> 💬 照字面讀，$p=1$ 也符合這個條件；一般的定義會另外要求 $p>1$。課堂和講義都沒有特別處理這點。

> **命題** [▶ 04:34](https://youtu.be/PHqmS3JUpf4?t=274)　設 $a,b,c,d,m\in\mathbb{Z}$。
> 1. $a\mid b$ 且 $b\mid c \Rightarrow a\mid c$（遞移性）
> 2. $a\mid b$ 且 $c\mid d \Rightarrow ac\mid bd$
> 3. 若 $m\neq 0$，則 $ma\mid mb \iff a\mid b$
> 4. 若 $d\mid a$ 且 $a\neq 0$，則 $|d|\le|a|$

**證明 (1)** [▶ 06:37](https://youtu.be/PHqmS3JUpf4?t=397)　存在 $k,l\in\mathbb{Z}$ 使 $b = ka$、$c = lb$。代入得 $c = l(ka) = (lk)a$，而 $lk\in\mathbb{Z}$，所以 $a\mid c$。$\blacksquare$

**(4) 的直覺** [▶ 18:13](https://youtu.be/PHqmS3JUpf4?t=1093)：若 $a = bc$ 且 $a\neq0$，則整數 $c\neq 0$，$|c|\ge 1$，所以 $|a| = |b||c|\ge|b|$。

> **定理** [▶ 09:16](https://youtu.be/PHqmS3JUpf4?t=556)　設 $a_1,\dots,a_k,c\in\mathbb{Z}$。
> 1. 若 $c\mid a_i$ 對 $i=1,\dots,k$ 都成立，則 $c\mid (u_1a_1 + \cdots + u_ka_k)$，對任意 $u_1,\dots,u_k\in\mathbb{Z}$。
>    **白話**：$c$ 整除每個 $a_i$，就整除它們的任何**整係數線性組合**。
> 2. $a\mid b$ 且 $b\mid a \iff a = \pm b$。

(1) 的證明和上面的命題 (1) 幾乎一樣，略過。

**證明 (2)** [▶ 11:24](https://youtu.be/PHqmS3JUpf4?t=684)　（$\Rightarrow$）存在 $k,l$ 使 $b = ka$、$a = lb$，代入得 $a = lka$。
- **若 $a\neq 0$**：兩邊除以 $a$ 得 $1 = lk$。因為 $l,k$ 是整數，只能 $l=k=1$ 或 $l=k=-1$，所以 $a = \pm b$ [▶ 12:33](https://youtu.be/PHqmS3JUpf4?t=753)。
- **若 $a = 0$**：由 $a\mid b$ 得 $b = 0\cdot j = 0$，所以 $a = b = 0$，仍然 $a=\pm b$ [▶ 13:35](https://youtu.be/PHqmS3JUpf4?t=815)。

（$\Leftarrow$）若 $a = \pm b$，則 $b=\pm a$，兩者互為 $\pm1$ 倍，所以互相整除 [▶ 15:10](https://youtu.be/PHqmS3JUpf4?t=910)。$\blacksquare$

**最常用的特例** [▶ 16:10](https://youtu.be/PHqmS3JUpf4?t=970)：

> **推論**　若 $c\mid x$ 且 $c\mid y$，則 $c\mid (ax+by)$，對所有 $a,b\in\mathbb{Z}$。

### 3. 最大公因數 [▶ 16:42](https://youtu.be/PHqmS3JUpf4?t=1002)

> **定義**　若 $d\mid a$ 且 $d\mid b$，稱 $d$ 為 $a,b$ 的**公因數 (common divisor)**。若 $a,b$ 不全為 $0$，它們最大的公因數稱為**最大公因數 (greatest common divisor)**，記作 $\gcd(a,b)$。

這個定義合理，因為由命題 (4)，公因數的絕對值不會超過 $\max\{|a|,|b|\}$ [▶ 18:13](https://youtu.be/PHqmS3JUpf4?t=1093)。

**小時候的方法：質因數分解** [▶ 19:13](https://youtu.be/PHqmS3JUpf4?t=1153)
$$\gcd(105,90) = \gcd(3\cdot5\cdot7,\ 2\cdot3\cdot3\cdot5) = 3\cdot 5 = 15.$$
問題是**大數的質因數分解很困難**，這也正是 RSA 加密的基礎 [▶ 20:13](https://youtu.be/PHqmS3JUpf4?t=1213)。所以需要更好的方法。

### 4. 輾轉相除法 [▶ 21:14](https://youtu.be/PHqmS3JUpf4?t=1274)

因為 $\gcd(a,b) = \gcd(\pm a,\pm b)$，只需要處理 $a,b\in\mathbb{N}$ 的情況 [▶ 21:45](https://youtu.be/PHqmS3JUpf4?t=1305)。

**演算法**
1. 對 $a,b$ 用除法算則：$a = q_1 b + r_1$，$0\le r_1<b$。若 $r_1 = 0$，則 $b\mid a$，$\gcd(a,b) = b$ [▶ 22:47](https://youtu.be/PHqmS3JUpf4?t=1367)。
2. 否則對 $b, r_1$ 再做一次：$b = q_2 r_1 + r_2$，$0\le r_2<r_1$。此時 $r_1$ 扮演上一步 $b$ 的角色，$b$ 扮演 $a$ 的角色 [▶ 23:17](https://youtu.be/PHqmS3JUpf4?t=1397)。
3. 繼續：$r_1 = q_3 r_2 + r_3$，……直到餘數為 $0$。

**為什麼最後一個非零餘數就是 gcd？** 課堂上老師推到一半發現漏講了一個關鍵引理 [▶ 28:59](https://youtu.be/PHqmS3JUpf4?t=1739)：

> **引理（講義 Lemma 1.1.13）**　設 $a,b,q,r\in\mathbb{Z}$。若 $a = qb + r$，則
> $$\gcd(a,b) = \gcd(b,r).$$

**證明** [▶ 30:00](https://youtu.be/PHqmS3JUpf4?t=1800)　關鍵是把式子改寫成 $r = a - qb$。
- 若 $d$ 同時整除 $a,b$，由推論，$d$ 整除 $a - qb = r$。
- 若 $d$ 同時整除 $b,r$，由推論，$d$ 整除 $qb + r = a$。

所以 $\{a,b\}$ 與 $\{b,r\}$ 的公因數完全相同，最大公因數自然相等。$\blacksquare$

**套用到演算法** [▶ 31:01](https://youtu.be/PHqmS3JUpf4?t=1861)：
$$\gcd(a,b) = \gcd(b,r_1) = \gcd(r_1,r_2) = \cdots = \gcd(r_{n-1}, r_n) = r_n,$$
其中 $r_n$ 是最後一個非零餘數（因為 $r_{n-1} = q_{n+1}r_n$，所以 $r_n\mid r_{n-1}$）。

**為什麼一定會停？** [▶ 33:04](https://youtu.be/PHqmS3JUpf4?t=1984)：餘數**嚴格遞減**，$b > r_1 > r_2 > \cdots \ge 0$，所以最多 $b$ 步就會出現 $0$。

> **定理（輾轉相除法 Euclidean algorithm）**　設 $a,b\in\mathbb{N}$，$a>b$。依上述方式重複做除法，最後一個非零餘數就是 $\gcd(a,b)$。

### 5. 例：$\gcd(100,44)$ 與倒推 [▶ 33:34](https://youtu.be/PHqmS3JUpf4?t=2014)

$$\begin{aligned}
100 &= 44\cdot 2 + 12\\
44 &= 12\cdot 3 + 8\\
12 &= 8\cdot 1 + 4\\
8 &= 4\cdot 2 + 0
\end{aligned}$$

最後一個非零餘數是 $4$，所以 $\gcd(100,44) = 4$ [▶ 35:37](https://youtu.be/PHqmS3JUpf4?t=2137)。這完全沒有用到質因數分解。

**擴展輾轉相除法 (extended Euclidean algorithm)** [▶ 36:08](https://youtu.be/PHqmS3JUpf4?t=2168)：要把 $4$ 寫成 $100$ 和 $44$ 的整係數線性組合 $4 = k\cdot 100 + l\cdot 44$。做法是**從倒數第二式往回代**：
$$\begin{aligned}
4 &= 12 - 8\\
  &= 12 - (44 - 3\cdot 12) = 4\cdot 12 - 44\\
  &= 4(100 - 2\cdot 44) - 44 = 4\cdot 100 - 9\cdot 44.
\end{aligned}$$

驗算：$400 - 396 = 4$ ✓

> 💬 老師一開始試圖從上往下代入，越寫越亂，後來學生提示「從 $4 = 12 - 8$ 開始往回代」才順利完成 [▶ 39:42](https://youtu.be/PHqmS3JUpf4?t=2382)–41:43。上面是正確的倒推順序。

**老師的建議** [▶ 41:43](https://youtu.be/PHqmS3JUpf4?t=2503)：看別人做不會真正理解，自己動手算幾次就會了。「大概做到第三題你就會覺得無聊。」這個方法對任何數字都一樣，沒有特殊技巧。

### 6. 例：$\gcd(240,11)$ [▶ 43:18](https://youtu.be/PHqmS3JUpf4?t=2598)

$$\begin{aligned}
240 &= 11\cdot 21 + 9\\
11 &= 9\cdot 1 + 2\\
9 &= 2\cdot 4 + 1\\
2 &= 1\cdot 2
\end{aligned}$$

所以 $\gcd(240,11) = 1$，兩數**互質**（這不意外）[▶ 43:48](https://youtu.be/PHqmS3JUpf4?t=2628)。更有趣的是找出 $1 = k\cdot 240 + l\cdot 11$ [▶ 44:48](https://youtu.be/PHqmS3JUpf4?t=2688)：

$$\begin{aligned}
1 &= 9 - 4\cdot 2\\
  &= 9 - 4(11 - 9) = 5\cdot 9 - 4\cdot 11\\
  &= 5(240 - 21\cdot 11) - 4\cdot 11 = 5\cdot 240 - 109\cdot 11.
\end{aligned}$$

驗算：$1200 - 1199 = 1$ ✓

> 💬 老師中途一度把 $5\cdot 21$ 算錯，得到 $-59$，隨即更正為 $105$，所以係數是 $-109$ [▶ 47:52](https://youtu.be/PHqmS3JUpf4?t=2872)。整理時合併同類項也很有幫助，例如把 $9 + 4\cdot 9$ 合成 $5\cdot 9$ [▶ 46:20](https://youtu.be/PHqmS3JUpf4?t=2780)。

### 7. Bézout 等式與模反元素 [▶ 48:52](https://youtu.be/PHqmS3JUpf4?t=2932)

> **定理（Bézout 等式 Bézout's identity）**　若 $a,b\in\mathbb{Z}$ 不全為 $0$，則存在 $x,y\in\mathbb{Z}$ 使得
> $$ax + by = \gcd(a,b).$$

擴展輾轉相除法就是**構造** $x,y$ 的系統方法。

> **Gallian 10th ed., p.3**（Theorem 0.2 GCD Is a Linear Combination）: *"For any nonzero integers a and b, there exist integers s and t such that gcd(a, b) = as + bt. Moreover, gcd(a, b) is the smallest positive integer of the form as + bt."*
>
> Gallian 多了「gcd 是這種形式中最小的正整數」這個刻畫，證明方法也不同（用良序原理，不用輾轉相除）。

**應用：求模反元素** [▶ 49:53](https://youtu.be/PHqmS3JUpf4?t=2993)　從 $5\cdot 240 - 109\cdot 11 = 1$ 可以直接讀出：
- **模 $240$**：$-109\cdot 11\equiv 1$，所以 $11^{-1} \equiv -109 \equiv 131 \pmod{240}$。
- **模 $11$**：$5\cdot 240 \equiv 1$，所以 $240^{-1}\equiv 5$（也可以說 $5^{-1}\equiv 240\equiv 9$）$\pmod{11}$。
- **模 $109$**：$5\cdot 240 \equiv 1$，所以 $5^{-1} \equiv 240 \equiv 22 \pmod{109}$ [▶ 51:25](https://youtu.be/PHqmS3JUpf4?t=3085)。

原理：取某個模數，讓等式中的一項變成 $0$，剩下的就是「兩數乘積 $\equiv 1$」，也就是互為模反元素。

> 💬 字幕中老師念的模數和反元素對應有些混亂；上面三行是依等式逐一驗算過的版本（例如 $11\cdot 131 = 1441 = 6\cdot 240 + 1$，$5\cdot 22 = 110 = 109 + 1$）。

**老師的提醒** [▶ 51:55](https://youtu.be/PHqmS3JUpf4?t=3115)：小模數時直接猜就好。例如求 $3$ 在模 $6$ 下的反元素，跑擴展輾轉相除法是浪費時間。（$\gcd(3,6) = 3 \neq 1$，所以 $3$ 根本沒有模 6 的反元素。）

**下次預告** [▶ 49:53](https://youtu.be/PHqmS3JUpf4?t=2993)：把模運算建立在嚴謹的基礎上；順利的話會講到如何求模係數矩陣的反矩陣。

**附帶**：老師提到 L3 結尾的 $D_3$ 計算漏了一個 $f$，結論不完全正確；講義裡的例子是對的 [▶ 50:55](https://youtu.be/PHqmS3JUpf4?t=3055)。（見 [[04-L3-中心-中心化子-二面體群]] 第 9 節，筆記已採用講義版本。）

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 除法算則 | division algorithm | [00:00](https://youtu.be/PHqmS3JUpf4?t=0) |
| 商；餘數 | quotient; remainder | [01:01](https://youtu.be/PHqmS3JUpf4?t=61) |
| 良序原理 | well-ordering principle | [02:02](https://youtu.be/PHqmS3JUpf4?t=122) |
| 整除；因數 | divides; factor / divisor | [02:32](https://youtu.be/PHqmS3JUpf4?t=152) |
| 質數 | prime | [04:03](https://youtu.be/PHqmS3JUpf4?t=243) |
| 整係數線性組合 | integer linear combination | [10:17](https://youtu.be/PHqmS3JUpf4?t=617) |
| 公因數 | common divisor | [16:42](https://youtu.be/PHqmS3JUpf4?t=1002) |
| 最大公因數 | greatest common divisor (gcd) | [17:12](https://youtu.be/PHqmS3JUpf4?t=1032) |
| 質因數分解 | prime factorization | [19:13](https://youtu.be/PHqmS3JUpf4?t=1153) |
| 輾轉相除法 | Euclidean algorithm | [21:14](https://youtu.be/PHqmS3JUpf4?t=1274) |
| 擴展輾轉相除法 | extended Euclidean algorithm | [36:08](https://youtu.be/PHqmS3JUpf4?t=2168) |
| 互質 | relatively prime | [43:48](https://youtu.be/PHqmS3JUpf4?t=2628) |
| Bézout 等式 | Bézout's identity | [48:52](https://youtu.be/PHqmS3JUpf4?t=2932) |

## ⚠️ 待確認清單

（本集無）
