---
course: Number Theory（2021 秋，線上錄影）
episode: 12
lecture: 2021-09-18 第 2 部
date: 2021-09-18
video: https://youtu.be/VFnFvZFWkSY
notes: Jones & Jones《Elementary Number Theory》附錄 B 直積（書頁 244，PDF 頁 259）；§3.3 Theorem 3.10 中國剩餘定理（書頁 52–53，PDF 頁 67–68）；講者講義主要取自 Gallian《Contemporary Abstract Algebra》
---

# 第 12 集 · U(n) 的結構與循環群的故事（Structure of U(n) and Story of Cyclic Groups） [▶ 影片](https://youtu.be/VFnFvZFWkSY)

← 上一集：[11-cyclic-groups-short-course-2](11-cyclic-groups-short-course-2.md) ｜ [總目錄](README.md) ｜ 下一集：[13-rsa-quadratic-diophantine-pell-1](13-rsa-quadratic-diophantine-pell-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 12 集（2021-09-18 第 2 部，接第 11 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（55:27，自動字幕）＋ Jones & Jones《Elementary Number Theory》附錄 B、§3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 群的直積](#1-群的直積)
- [2. 直積裡元素的階 = lcm](#2-直積裡元素的階--lcm)
- [3. 計數例子](#3-計數例子)
  - [3.1 Z₆ × Z₂ 的 6 階元素](#31-z--z-的-6-階元素)
  - [3.2 Z₁₀₀ × Z₂₅ 的 10 階元素與子群](#32-z--z-的-10-階元素與子群)
- [4. G × H 什麼時候是循環群](#4-g--h-什麼時候是循環群)
- [5. 有限交換群的分類](#5-有限交換群的分類)
- [6. U_st ≅ U_s × U_t 與 φ 的乘性](#6-u_st--u_s--u_t-與-φ-的乘性)
- [7. 中國剩餘定理](#7-中國剩餘定理)
  - [7.1 定理與構造式證明](#71-定理與構造式證明)
  - [7.2 例子：兩個同餘式](#72-例子兩個同餘式)
  - [7.3 例子：三個同餘式](#73-例子三個同餘式)
- [8. U_n 的結構](#8-u_n-的結構)
- [9. Fermat 小定理與 Euler 定理](#9-fermat-小定理與-euler-定理)
- [10. 作業導覽](#10-作業導覽)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

接第 11 集的講義（第 16 頁起），把「$U_n$ 長什麼樣」講完。路線：

直積 → 直積裡元素的階 → 什麼時候直積是循環群 → $U_{st}\cong U_s\times U_t$（要用中國剩餘定理）→ $U_n$ 的完整結構 → Fermat 小定理、Euler 定理。

| 主題 | 時間 | 課本 |
|---|---|---|
| 直積、元素的階 | 00:02 | 附錄 B |
| 計數例子 | 05:11 | — |
| 直積是循環群的條件 | 11:50 | 附錄 B |
| 有限交換群分類 | 18:05 | — |
| $U_{st}\cong U_s\times U_t$ | 20:38 | — |
| 中國剩餘定理 | 27:18 | §3.3 Theorem 3.10 |
| $U_n$ 的結構 | 38:04 | — |
| Fermat 小定理、Euler 定理 | 44:19 | — |
| 作業導覽 | 48:29 | — |

---

## 1. 群的直積

[▶ 00:02](https://youtu.be/VFnFvZFWkSY?t=2)

> **定義**：群 $G,H$ 的**直積**（direct product）$G\times H$ 就是笛卡兒積 $\{(g,h)\}$，運算**每個分量照各自的群算**：
> $$(g_1,h_1)(g_2,h_2) = (g_1g_2,\ h_1h_2).$$

- 兩個都是加法群就寫成加法；也可以一個加法、一個乘法。
- **單位元素**是 $(e_G, e_H)$，「單位元素組成的向量」。

---

## 2. 直積裡元素的階 = lcm

[▶ 00:32](https://youtu.be/VFnFvZFWkSY?t=32)

> **定理**：若 $|x|$、$|y|$ 有限，$(x,y)\in G\times H$，則
> $$|(x,y)| = \mathrm{lcm}(|x|,|y|).$$

講者：「很酷、超好用，能解一大堆問題。」

**證明** [▶ 01:03](https://youtu.be/VFnFvZFWkSY?t=63)：設 $|x|=m$、$|y|=n$，$s=\mathrm{lcm}(m,n)$，$s = km = ln$。

1. **先看次方怎麼算** [▶ 02:04](https://youtu.be/VFnFvZFWkSY?t=124)：$(x,y)^2 = (x,y)(x,y) = (x^2,y^2)$；同理（可用歸納法）$(x,y)^s = (x^s,y^s)$。
2. **$s$ 次方回到單位元素**：
   $$(x,y)^s = (x^{km},\,y^{ln}) = \left((x^m)^k,\,(y^n)^l\right) = (e_G^k,\,e_H^l) = (e_G,e_H).$$
   所以 $|(x,y)|\le s$。
3. **不會更小** [▶ 03:39](https://youtu.be/VFnFvZFWkSY?t=219)：若 $(x,y)^j = (e,e)$、$j<s$，則 $x^j=e$、$y^j=e$。由第 11 集推論 C，$m\mid j$、$n\mid j$。所以 $j$ 是 $m,n$ 的公倍數，卻比最小公倍數小，「這太瘋狂了」。∎

**例子** [▶ 04:40](https://youtu.be/VFnFvZFWkSY?t=280)：$\mathbb{Z}_{10}\times\mathbb{Z}_5$ 裡的 $(3,2)$。

- $\gcd(3,10)=1$，所以 $3$ 是 $\mathbb{Z}_{10}$ 的生成元，$|3|=10$。
- $\gcd(2,5)=1$，所以 $|2|=5$。
- $|(3,2)| = \mathrm{lcm}(10,5) = 10$。

驗算：$10\cdot(3,2) = (30,20) = (0,0)$，而且更小的倍數都不行。

---

## 3. 計數例子

### 3.1 Z₆ × Z₂ 的 6 階元素

[▶ 05:41](https://youtu.be/VFnFvZFWkSY?t=341)

要 $\mathrm{lcm}(|x|,|y|)=6$。$|x|$ 只能是 $6$ 的因數 $1,2,3,6$，$|y|$ 只能是 $1,2$。能湊出 lcm $=6$ 的有三種：

| 情況 | $|x|$ | $|y|$ | $x$ 的選法 | $y$ 的選法 | 元素 |
|---|---|---|---|---|---|
| 1 | 6 | 1 | $\varphi(6)=2$ | 1 | $(1,0),(5,0)$ |
| 2 | 6 | 2 | 2 | 1 | $(1,1),(5,1)$ |
| 3 | 3 | 2 | $\varphi(3)=2$ | 1 | $(2,1),(4,1)$ |

共 **6 個** 6 階元素。

- 【口頭】[▶ 06:44](https://youtu.be/VFnFvZFWkSY?t=404) 講者 2015 年的講義**漏了情況 2**，以為只有 4 個。「我出了名的不會數這種分情況的。如果覺得哪裡錯了——看到什麼就說什麼。」
- 6 個 $= 3\times\varphi(6)$，符合第 11 集推論 1.79。
- 而且這說明 **$\mathbb{Z}_6\times\mathbb{Z}_2$ 不是循環群**：12 階循環群只會有 $\varphi(6)=2$ 個 6 階元素。

### 3.2 Z₁₀₀ × Z₂₅ 的 10 階元素與子群

[▶ 08:16](https://youtu.be/VFnFvZFWkSY?t=496)

（講者說這是作業題，也是 Gallian 書上的例子。）

$|x|$ 整除 100、$|y|$ 整除 25。要 $\mathrm{lcm}=10$：

| 情況 | $|x|$ | $|y|$ | 個數 |
|---|---|---|---|
| 1 | 10 | 1 | $\varphi(10)\cdot 1 = 4$ |
| 2 | 10 | 2 | ❌ $\mathbb{Z}_{25}$ 沒有 2 階元素（$2\nmid 25$） |
| 3 | 10 | 5 | $\varphi(10)\varphi(5) = 4\cdot 4 = 16$ |
| 4 | 2 | 5 | $\varphi(2)\varphi(5) = 1\cdot 4 = 4$ |

共 $4+16+4 = 24$ 個 10 階元素。

⚠️ 逐字稿缺字：字幕裡講者把情況 2 說成「$|y|=2$ 有一個」算 4 個、情況 4 說成「不可能」，跟他自己前面說的「$\mathbb{Z}_{25}$ 沒有 2 階元素」矛盾，看起來是把情況 2 和 4 講反了。上表是照 lcm 重新整理的，總數 24 跟講者一樣。

**10 階子群有幾個** [▶ 10:49](https://youtu.be/VFnFvZFWkSY?t=649)：每個 10 階循環子群有 $\varphi(10)=4$ 個生成元（就是它的 4 個 10 階元素），而不同的子群不共用生成元。所以
$$\frac{24}{4} = 6\ \text{個 10 階循環子群}.$$

【口頭】Gallian 把這比喻成「**數羊腳來數羊**」：羊圈裡有 100 條腿，就有 25 隻羊（「排除不幸的基因突變」）。講者教抽象代數時有個動物學主修的學生，他想出別的版本：什麼數有 8 個生成元？那就像數蜘蛛。

---

## 4. G × H 什麼時候是循環群

[▶ 11:50](https://youtu.be/VFnFvZFWkSY?t=710)

> **定理**（講者講義 2.7.10）：$G,H$ 是有限循環群。則
> $$G\times H\ \text{是循環群}\iff\gcd(|G|,|H|)=1.$$

**證明 (⇐)**：$|G|=m$、$|H|=n$ 互質，所以 $\mathrm{lcm}(m,n)=mn$。設 $G=\langle a\rangle$、$H=\langle b\rangle$。由第 2 節，
$$|(a,b)| = \mathrm{lcm}(m,n) = mn = |G\times H|.$$
$(a,b)$ 生成的子群跟整個群一樣大，所以就是整個群。

**證明 (⇒)** [▶ 12:51](https://youtu.be/VFnFvZFWkSY?t=771)：設 $G\times H = \langle(x,y)\rangle$，$d=\gcd(m,n)$。$x^m = e$、$y^n = e$（任何元素的「群的階」次方都是 $e$）。則
$$(x,y)^{mn/d} = \left((x^m)^{n/d},\,(y^n)^{m/d}\right) = (e,e).$$
所以 $mn = |(x,y)|\le mn/d$，推出 $d=1$。∎

> **推論** [▶ 14:23](https://youtu.be/VFnFvZFWkSY?t=863)：$\mathbb{Z}_{mn}\cong\mathbb{Z}_m\times\mathbb{Z}_n\iff\gcd(m,n)=1$。
> **證明**：互質時 $\mathbb{Z}_m\times\mathbb{Z}_n$ 是 $mn$ 階循環群，而同階循環群只有一個（第 11 集），所以同構於 $\mathbb{Z}_{mn}$。

**推廣到很多個** [▶ 14:55](https://youtu.be/VFnFvZFWkSY?t=895)：

- $|(g_1,\dots,g_k)| = \mathrm{lcm}(|g_1|,\dots,|g_k|)$。
- 例：$\mathbb{Z}_3\times\mathbb{Z}_{10}\times\mathbb{Z}_{11}$ 裡的 $(2,3,4)$。$2,3,4$ 分別是各自的生成元，階是 $3,10,11$，所以
  $$|(2,3,4)| = \mathrm{lcm}(3,10,11) = 330.$$
  講者：「要把它加自己 330 次才會回到 0。用這小小的計算就知道，很酷。」
- 若 $n_1,\dots,n_k$ **兩兩互質**：$\mathbb{Z}_{n_1n_2\cdots n_k}\cong\mathbb{Z}_{n_1}\times\cdots\times\mathbb{Z}_{n_k}$。
- 例：$\mathbb{Z}_3\times\mathbb{Z}_{10}\times\mathbb{Z}_{11}\cong\mathbb{Z}_{330}$；$\mathbb{Z}_2\times\mathbb{Z}_3\times\mathbb{Z}_7\times\mathbb{Z}_{11}\cong\mathbb{Z}_{462}$。

【口頭】看到一個直積，「陪審團還沒判」它是不是循環群，要再研究能不能縮成一個 $\mathbb{Z}_n$。

> 【課本補充】附錄 B（p. 244）：若 $m,n$ 互質則 $C_m\times C_n\cong C_{mn}$，理由就是 $(c_1,c_2)$ 的階是 $mn$。

---

## 5. 有限交換群的分類

[▶ 18:05](https://youtu.be/VFnFvZFWkSY?t=1085)

> **有限交換群基本定理**：每個有限交換群都是**質數冪階循環群**的直積。而且直積的項數、各循環群的階，都由群唯一決定。

【口頭】「這是很大的結果」，自然的證明在**模**（module）理論裡，是「抽象代數二」的內容，本課不證。講者說有興趣可以找他做獨立研究。

**例子：100 階交換群有幾種？** [▶ 19:06](https://youtu.be/VFnFvZFWkSY?t=1146)

$100 = 2^2\cdot 5^2$。每個質數冪各自拆：$2^2$ 可以是 $\mathbb{Z}_4$ 或 $\mathbb{Z}_2\times\mathbb{Z}_2$；$5^2$ 可以是 $\mathbb{Z}_{25}$ 或 $\mathbb{Z}_5\times\mathbb{Z}_5$。所以共 $2\times 2 = 4$ 種：

| 分解 | 備註 |
|---|---|
| $\mathbb{Z}_4\times\mathbb{Z}_{25}$ | $\cong\mathbb{Z}_{100}$，循環群 |
| $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_{25}$ | $\cong\mathbb{Z}_2\times\mathbb{Z}_{50}$，不是循環群 |
| $\mathbb{Z}_4\times\mathbb{Z}_5\times\mathbb{Z}_5$ | |
| $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_5\times\mathbb{Z}_5$ | |

四個彼此不同構（各階元素的個數不一樣）。在同構意義下，100 階交換群**只有這四種**。

---

## 6. U_st ≅ U_s × U_t 與 φ 的乘性

[▶ 20:38](https://youtu.be/VFnFvZFWkSY?t=1238)

> **定理**：若 $\gcd(s,t)=1$，則
> $$U_{st}\cong U_s\times U_t.$$
>
> **推論（φ 的乘性）**：若 $\gcd(s,t)=1$，則
> $$\varphi(st) = \varphi(s)\,\varphi(t).$$

講者：「這對計算**超級重要**。」這叫 Euler 函數的**乘性**（multiplicative property）。

**證明**（「直接但有點技術」）[▶ 22:42](https://youtu.be/VFnFvZFWkSY?t=1362)：定義
$$\psi\left([x]_{st}\right) = \left([x]_s,\ [x]_t\right).$$
（這裡同時有模 $st$、模 $s$、模 $t$。）

1. **單一值（well-defined）**[▶ 23:13](https://youtu.be/VFnFvZFWkSY?t=1393)：若 $[y]_{st}=[x]_{st}$，$y = x+jst$。則 $[y]_s = [x+(jt)s]_s = [x]_s$，同理 $[y]_t=[x]_t$。所以結果不依代表元而定。
2. **真的落在 $U_s\times U_t$** [▶ 24:14](https://youtu.be/VFnFvZFWkSY?t=1454)：講者說「這很細，例子裡通常不談，但這裡要緊」。若 $[x]_{st}$ 有反元素 $[y]_{st}$，則 $xy-1 = nst$，所以 $xy\equiv 1$ 模 $s$ 也模 $t$。$[x]_s$、$[x]_t$ 都是單位。
3. **同態** [▶ 25:15](https://youtu.be/VFnFvZFWkSY?t=1515)：
   $$\psi([x][y]) = \psi([xy]) = ([xy]_s,[xy]_t) = ([x]_s,[x]_t)([y]_s,[y]_t) = \psi([x])\psi([y]).$$
4. **一對一** [▶ 26:16](https://youtu.be/VFnFvZFWkSY?t=1576)：兩邊都是有限集合，證一對一就夠。同態一對一 ⇔ **核**（kernel，被送到單位元素的元素）只有單位元素。
   $$\ker\psi = \{\,[x]_{st} : x\equiv 1\ (\mathrm{mod}\ s),\ x\equiv 1\ (\mathrm{mod}\ t)\,\}.$$
   要同時解兩個同餘式。由**中國剩餘定理**，唯一解是 $x\equiv 1\ (\mathrm{mod}\ st)$。所以核只有 $[1]$，$\psi$ 一對一。
5. 講者說「兩邊都有限，證一對一或映成之一就夠」，所以 $\psi$ 是同構。∎

> 以下**不是逐字稿內容**，是補一個講者帶過的地方：第 5 步要「一對一 ⇒ 映成」，需要先知道兩邊**一樣大**，而那正是我們想證的 $\varphi(st)=\varphi(s)\varphi(t)$。不繞圈的做法是直接證**映成**：給 $([a]_s,[b]_t)\in U_s\times U_t$，由中國剩餘定理有 $x$ 同時滿足 $x\equiv a\ (\mathrm{mod}\ s)$、$x\equiv b\ (\mathrm{mod}\ t)$；這個 $x$ 跟 $s$、$t$ 都互質，所以跟 $st$ 互質，$[x]_{st}\in U_{st}$ 而且 $\psi([x]_{st}) = ([a]_s,[b]_t)$。一對一加映成就是雙射。

**推廣**：$n_1,\dots,n_k$ 兩兩互質時 $U_{n_1\cdots n_k}\cong U_{n_1}\times\cdots\times U_{n_k}$，$\varphi(n_1\cdots n_k)=\varphi(n_1)\cdots\varphi(n_k)$。證明一樣，關鍵還是用中國剩餘定理證核是平凡的。

---

## 7. 中國剩餘定理

### 7.1 定理與構造式證明

[▶ 27:18](https://youtu.be/VFnFvZFWkSY?t=1638)

講者說作業有題要用到，而且「證明是**構造式**的，並不複雜」。

> **中國剩餘定理**（Chinese Remainder Theorem）：$m_1,\dots,m_r$ 兩兩互質，$M = m_1m_2\cdots m_r$。則同餘方程組
> $$x\equiv a_1\ (\mathrm{mod}\ m_1),\quad x\equiv a_2\ (\mathrm{mod}\ m_2),\quad\dots,\quad x\equiv a_r\ (\mathrm{mod}\ m_r)$$
> 有解，而且解在模 $M$ 下**唯一**。

**證明（構造解）** [▶ 28:52](https://youtu.be/VFnFvZFWkSY?t=1732)

**Step 1**：對每個 $k$，令
$$M_k = \frac{M}{m_k} = m_1\cdots\widehat{m_k}\cdots m_r.$$
（帽子 $\widehat{\ }$ 表示「拿掉這一項」，講者說「這是你不想戴的帽子」。）

**Step 2**：$\gcd(M_k,m_k)=1$，因為 $M_k$ 是把 $m_k$ 拿掉後其他 $m_j$ 的乘積，每個 $m_j$ 都跟 $m_k$ 互質。

**Step 3**：由 Bézout，有 $y_k,b_k$ 使 $y_kM_k + b_km_k = 1$。所以
$$y_kM_k\equiv 1\ (\mathrm{mod}\ m_k).$$
也就是說，**$y_k$ 是 $M_k$ 模 $m_k$ 的反元素**。

**Step 4**：令
$$x = a_1M_1y_1 + a_2M_2y_2 + \cdots + a_rM_ry_r.$$

**驗證** [▶ 30:54](https://youtu.be/VFnFvZFWkSY?t=1854)：看模 $m_i$。

- $j\neq i$ 時，$M_j$ 含有因數 $m_i$，所以 $M_j\equiv 0\ (\mathrm{mod}\ m_i)$。
- 所以只剩第 $i$ 項：$x\equiv a_iM_iy_i\equiv a_i\cdot 1 = a_i\ (\mathrm{mod}\ m_i)$。

**唯一性** [▶ 31:25](https://youtu.be/VFnFvZFWkSY?t=1885)：若 $y$ 也是解，則 $y\equiv a_i\equiv x\ (\mathrm{mod}\ m_i)$，每個 $m_i\mid y-x$。$m_i$ 兩兩互質，所以乘積 $M\mid y-x$，$y\equiv x\ (\mathrm{mod}\ M)$。∎

> 【課本補充】§3.3 Theorem 3.10（p. 53）陳述相同（課本說解「組成模 $n$ 的單一個同餘類」），證明也一樣：$c_i = n/n_i$，$d_i$ 是 $c_i$ 模 $n_i$ 的反元素，$x_0 = a_1c_1d_1+\cdots+a_kc_kd_k$。
>
> 課本的背景（p. 52–53）：
> - 西元 1 世紀中國數學家**孫子**的問題：「一個數除以 3、5、7 分別餘 2、3、2」。（以下**不是逐字稿內容**：用上面的公式，$M=105$，$M_1=35,M_2=21,M_3=15$，反元素 $y_1=2,y_2=1,y_3=1$，$x = 2\cdot35\cdot2+3\cdot21\cdot1+2\cdot15\cdot1 = 233\equiv 23\ (\mathrm{mod}\ 105)$。）
> - **模數不互質可能無解**：$x\equiv 3\ (\mathrm{mod}\ 9)$、$x\equiv 2\ (\mathrm{mod}\ 6)$。第一式說 $3\mid x$，第二式說 $3\nmid x$，矛盾。
> - 應用：週期互質的週期性事件（行星會合、日月食）會以週期 $n$ 同時發生，課本說預測這些可能是這個定理最初的動機。

### 7.2 例子：兩個同餘式

[▶ 32:26](https://youtu.be/VFnFvZFWkSY?t=1946)

$$x\equiv 2\ (\mathrm{mod}\ 3),\qquad x\equiv 7\ (\mathrm{mod}\ 11).$$

| | $k=1$ | $k=2$ |
|---|---|---|
| $a_k$ | 2 | 7 |
| $m_k$ | 3 | 11 |
| $M_k = 33/m_k$ | 11 | 3 |
| $y_k = M_k^{-1}\bmod m_k$ | $11^{-1}\equiv 2\ (\mathrm{mod}\ 3)$，因 $2\cdot 11 = 22\equiv 1$ | $3^{-1}\equiv 4\ (\mathrm{mod}\ 11)$，因 $3\cdot 4 = 12\equiv 1$ |

$$x = 2\cdot 11\cdot 2 + 7\cdot 3\cdot 4 = 44+84 = 128\equiv 128-3\cdot 33 = 29\ (\mathrm{mod}\ 33).$$

**驗算**：$29 = 27+2\equiv 2\ (\mathrm{mod}\ 3)$ ✓；$29 = 22+7\equiv 7\ (\mathrm{mod}\ 11)$ ✓。

### 7.3 例子：三個同餘式

[▶ 33:56](https://youtu.be/VFnFvZFWkSY?t=2036)

$$x\equiv 3\ (\mathrm{mod}\ 3),\qquad x\equiv 7\ (\mathrm{mod}\ 8),\qquad x\equiv 10\ (\mathrm{mod}\ 11).$$

（$x\equiv 3\ (\mathrm{mod}\ 3)$ 其實就是 $x\equiv 0$，講者照原樣寫。）

$M = 3\cdot 8\cdot 11 = 264$。

| | $k=1$ | $k=2$ | $k=3$ |
|---|---|---|---|
| $a_k$ | 3 | 7 | 10 |
| $m_k$ | 3 | 8 | 11 |
| $M_k$ | 88 | 33 | 24 |
| $M_k\bmod m_k$ | $88\equiv 1$ | $33\equiv 1$ | $24\equiv 2$ |
| $y_k$ | 1 | 1 | $2^{-1}\equiv 6$（$2\cdot 6=12\equiv1$） |
| $a_kM_ky_k$ | 264 | 231 | 1440 |

講者說求反元素可以用 Euclid 演算法，但這裡數字小，直接看出來。$88\equiv 1$、$33\equiv 1$「有點尷尬」，$24$ 的反元素「終於有點意思」。

- 第一項 $264\equiv 0\ (\mathrm{mod}\ 264)$，直接丟掉。
- $231+1440 = 1671$。
- **化簡** [▶ 36:33](https://youtu.be/VFnFvZFWkSY?t=2193)：$1671/264\approx 6.32$，所以減 $6\cdot 264 = 1584$：$1671-1584 = 87$。

$$x\equiv 87\ (\mathrm{mod}\ 264).$$

【口頭】「答案留在 1671 mod 264 也可以，但那很俗氣。」

**驗算**：$87 = 29\cdot 3\equiv 0\equiv 3\ (\mathrm{mod}\ 3)$ ✓；$87 = 80+7\equiv 7\ (\mathrm{mod}\ 8)$ ✓；$87 = 77+10\equiv 10\ (\mathrm{mod}\ 11)$ ✓。

---

## 8. U_n 的結構

[▶ 38:04](https://youtu.be/VFnFvZFWkSY?t=2284)

把第 6 節和質數冪的結構合起來，就能完全描述 $U_n$。

**質數冪的 $U$**（講者講義第 29 頁的定理，講者說他「有點跳太快」，直接引用）：

> **定理**：
> - $p$ 是**奇質數**：$U_{p^n}\cong\mathbb{Z}_{p^n-p^{n-1}}$，是**循環群**。
> - $p=2$：$U_2$ 是平凡群；$U_4\cong\mathbb{Z}_2$；$n\ge 3$ 時 $U_{2^n}\cong\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}$，**不是**循環群。

⚠️ 逐字稿缺字：字幕把 $2^n$ 的情況說成「z2 cross z to the 2n minus 1」「z cross z n minus 2」，講者自己也猶豫（「$U_8$ 是 $\mathbb{Z}_2\times\mathbb{Z}_4$？不對，等一下」），最後確定 $U_8\cong\mathbb{Z}_2\times\mathbb{Z}_2$（**Klein 四元群**）。上面寫的 $\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}$ 跟 $U_8$ 吻合（$n=3$ 時是 $\mathbb{Z}_2\times\mathbb{Z}_2$），階也對（$2\cdot 2^{n-2} = 2^{n-1} = \varphi(2^n)$）。

（這就是第 9 集講者說「$p=2$ 不一樣」的原因。）

**一般的 $n$** [▶ 43:16](https://youtu.be/VFnFvZFWkSY?t=2596)：由算術基本定理 $n = p_1^{k_1}\cdots p_s^{k_s}$，各質數冪兩兩互質，所以
$$U_n\cong U_{p_1^{k_1}}\times\cdots\times U_{p_s^{k_s}},$$
每一項再用上面的定理換成 $\mathbb{Z}_k$。

**例子**

| $n$ | 分解 | $U_n\cong$ |
|---|---|---|
| $200 = 8\cdot 25$ | $U_8\times U_{25}$ | $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_{20}$ |
| $405 = 5\cdot 3^4$ | $U_5\times U_{81}$ | $\mathbb{Z}_4\times\mathbb{Z}_{54}$（$81-27=54$） |
| $195 = 5\cdot 3\cdot 13$ | $U_5\times U_3\times U_{13}$ | $\mathbb{Z}_4\times\mathbb{Z}_2\times\mathbb{Z}_{12}$ |

**$U_{200}$ 裡元素的最大階** [▶ 39:40](https://youtu.be/VFnFvZFWkSY?t=2380)：$(a,b,c)\in\mathbb{Z}_{20}\times\mathbb{Z}_2\times\mathbb{Z}_2$ 的階是 $\mathrm{lcm}(|a|,|b|,|c|)$，最多 $\mathrm{lcm}(20,2,2) = 20$。同構保持元素的階，所以**模 200 的單位，階最多是 20**。

【口頭】「如果你問我 $U_{405}$ 裡有幾個 10 階元素，天哪我不知道；但換成 $\mathbb{Z}_4\times\mathbb{Z}_{54}$ 我就算得出來。」

**作業的用法** [▶ 41:43](https://youtu.be/VFnFvZFWkSY?t=2503)：作業要證 $\mathrm{Aut}(\mathbb{Z}_n)\cong U_n$。證完後，問 $\mathbb{Z}_n$ 有幾個某階的自同構，就變成問 $U_n$ 有幾個某階元素，而 $U_n$ 可以拆成循環群的直積來算。「有點狡猾，但這就是作戰計畫。」

---

## 9. Fermat 小定理與 Euler 定理

[▶ 44:19](https://youtu.be/VFnFvZFWkSY?t=2659)

> **Fermat 小定理**（Fermat's little theorem）：若 $p$ 是質數、$a\not\equiv 0\ (\mathrm{mod}\ p)$，則
> $$a^{p-1}\equiv 1\ (\mathrm{mod}\ p).$$

**證明（用群論）** [▶ 44:49](https://youtu.be/VFnFvZFWkSY?t=2689)

1. $p$ 是質數，所以 $|U_p| = p-1$，而 $a\in U_p$。
2. $\langle a\rangle\le U_p$，由 Lagrange，$|a|$ 整除 $p-1$。寫 $p-1 = n\,|a|$。
3. $$a^{p-1} = a^{n|a|} = \left(a^{|a|}\right)^n = 1^n = 1.$$ ∎

**例子** [▶ 46:24](https://youtu.be/VFnFvZFWkSY?t=2784)：$p=17$、$a=10$。$10\not\equiv 0$，所以
$$10^{16}\equiv 1\ (\mathrm{mod}\ 17).$$
【口頭】「代數字進去，Fermat 小定理就不那麼『小』了吧？$10^{16}$ 這麼大，不用計算就知道它模 17 是 1。」會用在 RSA。

> 以下**不是逐字稿內容**，是驗算：$10^2 = 100\equiv 15\equiv -2$，$10^4\equiv 4$，$10^8\equiv 16\equiv -1$，$10^{16}\equiv 1\ (\mathrm{mod}\ 17)$。✓

> **Euler 定理** [▶ 47:29](https://youtu.be/VFnFvZFWkSY?t=2849)：若 $x\in U_n$，則
> $$x^{\varphi(n)}\equiv 1\ (\mathrm{mod}\ n).$$

講者：這只是說「**群的元素取群的階次方，會回到單位元素**」，是前面定理的直接推論（$|x|$ 整除 $|U_n| = \varphi(n)$）。Fermat 小定理是 $n=p$ 的特例。

（講者說「這其實不在 Stillwell……」，話沒講完。）

---

## 10. 作業導覽

[▶ 48:29](https://youtu.be/VFnFvZFWkSY?t=2909)

講者瀏覽兩份作業（他叫 Mission 2、Mission 3），只說方向，不給答案：

- **Mission 2**：第 13–17 題是模運算（「回到我還健康時的那堂課」）；證 $\sqrt[3]{5}$ 無理（「跟課堂上做的類似」）；$6^{13}$ 除以 4 的餘數（「想模 4 的運算」）；Euclid 演算法；用 **Fermat 小定理求反元素**（另一個選擇是 Euclid／Bézout）；第 23 題對照 Euler 定理和 Euclid 演算法。
- **Mission 3**：解 $\mathbb{Z}_n$ 裡的方程（照 Stillwell p. 34 的演算法，講者還沒在課堂講，會寫解答）；第 28 題是中國剩餘定理；第 29 題證多項式沒有整數根——只要代 $\mathbb{Z}_4$ 的 $0,1,2,3$ 都不是 0（第 8 集的想法）；把 $U_{33}$、$U_{40}$、$U_{12}$ 寫成 $\mathbb{Z}_n$ 的直積；$\mathbb{Z}_{100}\times\mathbb{Z}_{25}$ 的 10 階元素和子群（本集 3.2）；108 階交換群有幾種；證 $\mathrm{Aut}(\mathbb{Z}_n)\cong U_n$；$\mathbb{Z}_{68}$ 有幾個 4 階自同構；仿射密碼 $f(x) = mx+b$（字母 $a=0$ 到 $z=25$），由「cat 加密成某字」找出 $m,b$ 再解密。
- RSA 的題（37–40）之後補。

下週一講 RSA，「期待當面見」。

---

## 11. 一頁速查表

**直積**：$(g_1,h_1)(g_2,h_2)=(g_1g_2,h_1h_2)$；$|(x,y)|=\mathrm{lcm}(|x|,|y|)$。

- **關鍵一步**：$(x,y)^j=(e,e)\iff|x|\mid j$ 且 $|y|\mid j$。

**計數**（分情況：哪些 $|x|,|y|$ 的 lcm 是目標，每種有 $\varphi(|x|)\varphi(|y|)$ 個）：

- $\mathbb{Z}_6\times\mathbb{Z}_2$：6 個 6 階元素。
- $\mathbb{Z}_{100}\times\mathbb{Z}_{25}$：24 個 10 階元素，$24/\varphi(10)=6$ 個 10 階子群。

**循環性**：$G\times H$（有限循環）循環 $\iff\gcd(|G|,|H|)=1$。$\mathbb{Z}_{mn}\cong\mathbb{Z}_m\times\mathbb{Z}_n\iff\gcd(m,n)=1$。

**有限交換群** = 質數冪階循環群的直積（唯一）。100 階有 4 種。

**$U_{st}\cong U_s\times U_t$**（$\gcd(s,t)=1$），$[x]_{st}\mapsto([x]_s,[x]_t)$。⇒ $\varphi(st)=\varphi(s)\varphi(t)$。

**中國剩餘定理**：$m_i$ 兩兩互質 ⇒ 模 $M=\prod m_i$ 唯一解
$$x = \sum a_kM_ky_k,\qquad M_k = M/m_k,\quad y_k\equiv M_k^{-1}\ (\mathrm{mod}\ m_k).$$

- **關鍵一步**：$j\neq i$ 時 $M_j\equiv0\ (\mathrm{mod}\ m_i)$。
- 例：$x\equiv2\ (3)$、$x\equiv7\ (11)$ ⇒ $x\equiv29\ (33)$；$x\equiv0\ (3)$、$7\ (8)$、$10\ (11)$ ⇒ $x\equiv87\ (264)$。

**$U_n$ 的結構**

- $p$ 奇質數：$U_{p^n}\cong\mathbb{Z}_{p^n-p^{n-1}}$（循環）。
- $U_2=1$，$U_4\cong\mathbb{Z}_2$，$U_{2^n}\cong\mathbb{Z}_2\times\mathbb{Z}_{2^{n-2}}$（$n\ge3$）。
- 例：$U_{200}\cong\mathbb{Z}_2^2\times\mathbb{Z}_{20}$（最大階 20）；$U_{405}\cong\mathbb{Z}_4\times\mathbb{Z}_{54}$；$U_{195}\cong\mathbb{Z}_4\times\mathbb{Z}_2\times\mathbb{Z}_{12}$。

**Fermat 小定理**：$p\nmid a$ ⇒ $a^{p-1}\equiv1\ (\mathrm{mod}\ p)$。**Euler 定理**：$\gcd(x,n)=1$ ⇒ $x^{\varphi(n)}\equiv1\ (\mathrm{mod}\ n)$。**關鍵一步**：$|x|$ 整除 $|U_n|$（Lagrange）。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Euler 定理、Fermat 小定理 | 第 13–14 集（RSA） |
| $\varphi(pq)=(p-1)(q-1)$ | 第 13–14 集（RSA 金鑰） |
| 中國剩餘定理 | 作業、第 13 集起 |
| $U_p$ 是循環群（原根） | 第 25–26 集（二次互反律） |
| 高斯整數裡的中國剩餘定理類比 | 第 17–21 集 |
| $\mathbb{Z}_m\times\mathbb{Z}_n\cong\mathbb{Z}_{mn}$ 的環版本 | 第 29–32 集（商環、同構定理） |

---

## 附：本集一句話總結

> **直積裡元素的階是各分量階的 lcm，所以 $\mathbb{Z}_m\times\mathbb{Z}_n$ 是循環群恰好在 $m,n$ 互質時。用中國剩餘定理證出 $U_{st}\cong U_s\times U_t$，於是 $\varphi$ 有乘性，$U_n$ 可以完全拆成 $\mathbb{Z}_k$ 的直積；Fermat 小定理和 Euler 定理都只是「元素的群階次方等於 1」。**

---

*筆記依據 James S. Cook「Number Theory」2021-09-18 第 2 部錄影逐字稿（YouTube 自動字幕，55:27）與 Jones & Jones《Elementary Number Theory》附錄 B、§3.3 整理。*
