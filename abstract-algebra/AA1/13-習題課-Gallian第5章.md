---
course: Abstract Algebra I (Fall 2016)
episode: 13
lecture: 習題課
date: 2016-09-15
video: https://www.youtube.com/watch?v=tn6acqjJ368
notes: 無直接對應（Gallian 第 5 章；預告講義 Thm 1.3.11、1.3.23）
---

# 第 13 集 · 習題課：Gallian 第 5 章 [▶ 影片](https://www.youtube.com/watch?v=tn6acqjJ368&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[12-L8-置換與循環記號]] ｜ [總目錄](../README.md) ｜ 下一集：[[14-L9-偶置換與奇置換]] →

## 本集概要

- **Ruffini 定理**（預告）：互斥循環乘積的階 = 各循環長度的**最小公倍數**。$k$-循環的階是 $k$。
- 一個教訓：循環裡**不能有重複的數**，例如 $(1232)$ 根本不是合法的置換。
- **把循環拆成 2-循環（換位）**：$(a_1a_2\cdots a_k) = (a_1a_k)(a_1a_{k-1})\cdots(a_1a_2)$。
- **循環的反元素**就是倒著寫：$(a_1a_2\cdots a_k)^{-1} = (a_k\cdots a_2a_1)$；乘積的反元素用襪子鞋子規則。
- 回答同學問題：循環群基本定理證明中「為什麼 $r = 0$」。
- 預告：偶置換、奇置換、交錯群 $A_n$。

---

## 筆記

### 1. Ruffini 定理（預告）[▶ 00:00](https://youtu.be/tn6acqjJ368?t=0)

> **定理（Ruffini；Gallian Thm 5.3；講義 Thm 1.3.23）**　若 $\sigma = \gamma_1\gamma_2\cdots\gamma_k$ 是**互斥**循環的乘積，則
> $$|\sigma| = \operatorname{lcm}(\gamma_1\text{ 的長度},\dots,\gamma_k\text{ 的長度}).$$

**$k$-循環的階是 $k$** [▶ 01:30](https://youtu.be/tn6acqjJ368?t=90)
- $(12)(12) = (1)$，所以 2-循環的階是 2。
- $(abc)^2 = (acb)$，$(abc)^3 = (acb)(abc) = (1)$，所以 3-循環的階是 3 [▶ 03:00](https://youtu.be/tn6acqjJ368?t=180)。
- 這裡默默用到：$a,b,c$ **互不相同** [▶ 03:30](https://youtu.be/tn6acqjJ368?t=210)。

### 2. 教訓：循環裡不能有重複的數 [▶ 04:00](https://youtu.be/tn6acqjJ368?t=240)

老師想用 $(1232)$ 示範「長度 4 但階不是 4」，算了一陣子出現矛盾，最後發現 [▶ 11:30](https://youtu.be/tn6acqjJ368?t=690)：
- $(1232)$ 說 $2\to3$，又說 $2\to1$，**2 被送到兩個地方**，連函數都不是 [▶ 17:00](https://youtu.be/tn6acqjJ368?t=1020)。
- 同樣，$(11)$ 不是真正的 2-循環。

**規則**：一個循環 $(a_1a_2\cdots a_k)$ 裡的 $a_i$ 必須**互不相同**。之後的定理都默認這點 [▶ 26:00](https://youtu.be/tn6acqjJ368?t=1560)。

> 💬 但在**乘積**裡，同一個數可以出現在不同循環，例如 $(123) = (13)(12)$ [▶ 13:30](https://youtu.be/tn6acqjJ368?t=810)。

**怎麼讀乘積** [▶ 05:30](https://youtu.be/tn6acqjJ368?t=330)：$\alpha\beta$ 表示 $\alpha(\beta(x))$，所以把 $x$ 先丟進右邊的循環，結果再丟進左邊的。只要對 $x = 1,\dots,n$ 每個數都查一次就好 [▶ 07:00](https://youtu.be/tn6acqjJ368?t=420)。

### 3. 拆成換位 [▶ 13:30](https://youtu.be/tn6acqjJ368?t=810)

**標準技巧**
$$(123) = (13)(12),\qquad (12345) = (15)(14)(13)(12).$$
一般地：
$$(a_1a_2\cdots a_k) = (a_1a_k)(a_1a_{k-1})\cdots(a_1a_3)(a_1a_2).$$

**驗證 $(12345)$**（由右往左）[▶ 14:30](https://youtu.be/tn6acqjJ368?t=870)
- $1$：$(12)$ 送到 $2$，其餘不動 2。$1\to2$ ✓
- $2$：$(12)$ 送到 $1$，$(13)$ 送到 $3$，其餘不動 3。$2\to3$ ✓
- 依此類推。

2-循環也叫**換位 (transposition)**。

**Ruffini 只適用於互斥循環** [▶ 15:00](https://youtu.be/tn6acqjJ368?t=900)：$(15)(14)(13)(12)$ 四個都是 2-循環，$\operatorname{lcm}(2,2,2,2) = 2$，但 $(12345)$ 的階是 5。因為它們**不互斥**。

> 💬 學生問重複數字的 lcm 怎麼算：例如 $\operatorname{lcm}(7,49,7) = 49$，看質因數分解 [▶ 15:30](https://youtu.be/tn6acqjJ368?t=930)。

**用法** [▶ 16:00](https://youtu.be/tn6acqjJ368?t=960)
- 已經是互斥循環：例如 $(123)(79)(8\,10\,11)$，階 $= \operatorname{lcm}(3,2,3) = 6$。（數字大時要加逗號。）
- 不是互斥循環：先化成互斥循環。例如 $(1234)(341) = (1423)$，階為 4 [▶ 17:30](https://youtu.be/tn6acqjJ368?t=1050)。

### 4. 作業提示 [▶ 18:30](https://youtu.be/tn6acqjJ368?t=1110)

週一要交的作業很多是在算置換的階，基本上就是 Ruffini 定理。
- 完成 $S_3$ 的 Cayley 表。
- 對每個置換：寫成互斥循環、求反元素、求階、寫成換位乘積、判斷奇偶 [▶ 19:30](https://youtu.be/tn6acqjJ368?t=1170)。
- Gallian #10：有限集合到自己的函數，一對一 $\iff$ 映成。老師說這其實是 Math 200（證明入門）的題，要大家複習一對一和映成 [▶ 20:00](https://youtu.be/tn6acqjJ368?t=1200)。
- Gallian #40：證明 $n\ge3$ 時 $S_n$ 不是交換群（第 10 版 Ch.5 #51）。提示：用 $1,2,3$ 的循環找不交換的例子；$S_3$ 自然地包含在 $S_4$、$S_5$……裡 [▶ 30:30](https://youtu.be/tn6acqjJ368?t=1830)。
- Gallian #35：$A_6$ 中有幾個 5 階元素？

### 5. 同學問題：循環群基本定理中為什麼 $r = 0$ [▶ 21:00](https://youtu.be/tn6acqjJ368?t=1260)

（講義 p.47，循環群基本定理 (1) 的證明第三段。見 [[10-L7-循環群-下]] §5。）

- $t$ 是 $\Lambda = \{m\in\mathbb{N}\mid a^m\in H\}$ 的最小元素。
- 除法算則：$k = qt + r$，$0\le r<t$。
- $a^t\in H \Rightarrow a^{-qt} = (a^{-t})^q\in H$；又 $a^k\in H$。所以 $a^r = a^{-qt}a^k\in H$ [▶ 23:00](https://youtu.be/tn6acqjJ368?t=1380)。
- 若 $0<r<t$，則 $r\in\Lambda$，比最小元素 $t$ 還小，矛盾。所以 $r = 0$ [▶ 24:00](https://youtu.be/tn6acqjJ368?t=1440)。

**關鍵**：「最小」是在指數的集合 $\Lambda\subseteq\mathbb{N}$ 裡比，不是比群元素 [▶ 25:00](https://youtu.be/tn6acqjJ368?t=1500)。

### 6. 循環的反元素 [▶ 25:30](https://youtu.be/tn6acqjJ368?t=1530)

- $(ab)^{-1} = (ab)$，因為 $(ab)(ab) = (1)$。
- $(abc)^{-1} = (acb)$：驗證 $(acb)(abc) = (1)$ [▶ 27:00](https://youtu.be/tn6acqjJ368?t=1620)。
- $(acb) = (cba)$，就是**倒過來寫** [▶ 29:00](https://youtu.be/tn6acqjJ368?t=1740)。

> **猜想 → 定理（講義 Lemma 1.3.22；Gallian Ch.5 習題）**
> $$(a_1a_2\cdots a_k)^{-1} = (a_k\cdots a_2a_1).$$

**驗證** [▶ 32:00](https://youtu.be/tn6acqjJ368?t=1920)：在 $(a_k\cdots a_1)(a_1\cdots a_k)$ 中，$a_1\to a_2\to a_1$，$a_2\to a_3\to a_2$，……，$a_k\to a_1\to a_k$。嚴格證明要用歸納法，老師給的是「工程師式證明」。

**乘積的反元素** [▶ 33:00](https://youtu.be/tn6acqjJ368?t=1980)：用**襪子鞋子**規則 $(\alpha\beta)^{-1} = \beta^{-1}\alpha^{-1}$，再把每個循環倒著寫。不管 $\alpha,\beta$ 是否互斥都適用。

例：$\sigma = (1234)(4765)$。則
$$\sigma^{-1} = (4765)^{-1}(1234)^{-1} = (5674)(4321).$$
化成互斥循環（由右往左）：$\sigma = (1234765)$，是 7-循環。

> 💬 板書起初寫 $(1234)(765)$，老師接著說「若這裡有個 4 也不會差多少」，之後的計算 $4\to7$、$5\to4$ 是以 $\beta = (4765)$ 算的，結果是 7-循環。

**再配上一個互斥循環** [▶ 35:00](https://youtu.be/tn6acqjJ368?t=2100)：$\gamma = (1234765)(8\,9\,10)$，由 Ruffini，$|\gamma| = \operatorname{lcm}(7,3) = 21$。

### 7. 預告：偶置換、奇置換、交錯群 [▶ 35:30](https://youtu.be/tn6acqjJ368?t=2130)

- 下一講主要證明：**每個置換都能寫成換位的乘積**。關鍵就是 §3 的那個恆等式 [▶ 36:00](https://youtu.be/tn6acqjJ368?t=2160)。
- **偶置換**：能寫成偶數個換位；**奇置換**：奇數個。
  - $(123) = (13)(12)$ 是偶的。
  - $(1234) = (14)(13)(12)$ 是奇的 [▶ 37:00](https://youtu.be/tn6acqjJ368?t=2220)。
  - 偶 × 奇 = 奇；偶 × 偶 = 偶；奇 × 奇 = 偶。
- **交錯群 (alternating group)** $A_n$：$S_n$ 中所有偶置換組成的子群 [▶ 38:00](https://youtu.be/tn6acqjJ368?t=2280)。Gallian 說 $|A_n| = n!/2$，所以 $|A_4| = 12$ [▶ 40:00](https://youtu.be/tn6acqjJ368?t=2400)。

> 💬 老師在課堂上試著列 $A_4$ 的元素，中途把 $S_4$、$S_6$ 搞混，說要再想想這題怎麼給建議 [▶ 41:00](https://youtu.be/tn6acqjJ368?t=2460)。
>
> 補充（非課堂內容）：$A_6$ 中 5 階元素的循環型一定是一個 5-循環（$\operatorname{lcm}$ 要等於 5），而 5-循環 $= 4$ 個換位，是偶置換，全部都在 $A_6$ 裡。$S_6$ 中 5-循環共有 $\binom{6}{5}\cdot 4! = 144$ 個，所以答案是 **144**。

**結尾** [▶ 42:00](https://youtu.be/tn6acqjJ368?t=2520)：老師開玩笑說全班都沒人來問問題，一定是學得非常好。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 最小公倍數 | least common multiple (lcm) | [01:00](https://youtu.be/tn6acqjJ368?t=60) |
| 換位 | transposition | [14:30](https://youtu.be/tn6acqjJ368?t=870) |
| 偶置換；奇置換 | even permutation; odd permutation | [36:30](https://youtu.be/tn6acqjJ368?t=2190) |
| 交錯群 | alternating group | [38:00](https://youtu.be/tn6acqjJ368?t=2280) |
| 子群圖 | subgroup diagram | [41:30](https://youtu.be/tn6acqjJ368?t=2490) |

## ⚠️ 待確認清單

1. [▶ 33:00](https://youtu.be/tn6acqjJ368?t=1980)–35:00 板書上 $\beta$ 究竟是 $(765)$ 還是 $(4765)$（筆記依計算結果採用 $(4765)$）。
