---
course: Number Theory（2021 秋，線上錄影）
episode: 47
lecture: 2021-12-01 第 2 部
date: 2021-12-01
video: https://youtu.be/b8ygAt9n4nY
notes: 講者講義沒有涵蓋；本集接第 46 集講 Keith Conrad「Factoring in quadratic fields」，定理編號照講者口述，該 PDF 不在本筆記的來源清單裡
---

# 第 47 集 · 理想的乘法與唯一分解（How Ideals Fix Numbers, Part 2） [▶ 影片](https://youtu.be/b8ygAt9n4nY)

← 上一集：[46-ideals-fix-numbers-1](46-ideals-fix-numbers-1.md) ｜ [總目錄](README.md) ｜ 下一集：（本課最後一集）

> **課程**：Number Theory（線上課，2021 秋）— 第 47 集（2021-12-01 第 2 部，接第 46 集；全課最後一部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（16:41，whisper 轉錄）。講者照 Keith Conrad 的 PDF 講；那份 PDF 不在本筆記的來源裡，所以定理只寫講者在課堂上說的內容。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 理想的乘法](#1-理想的乘法)
- [2. 理想的整除 = 反過來的包含](#2-理想的整除--反過來的包含)
- [3. 乘法的性質、共軛理想](#3-乘法的性質共軛理想)
- [4. 修好 15 的兩種分解](#4-修好-15-的兩種分解)
- [5. 大定理：理想的唯一分解](#5-大定理理想的唯一分解)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 回顧：整門課走到哪裡](#7-回顧整門課走到哪裡)

---

## 0. 這堂課要做什麼

接第 46 集：定義理想的乘法和整除，然後用理想把 $15 = 3\cdot5 = (1+\sqrt{-14})(1-\sqrt{-14})$ 的「兩種分解」統一起來。這是**整門課的最後一部影片**。

（記號：$\mathcal{O}_K$ 是二次體 $K$ 的整數；這裡主要是 $K = \mathbb{Q}(\sqrt{-14})$，$\mathcal{O}_K = \mathbb{Z}[\sqrt{-14}]$，第 46 集。）

---

## 1. 理想的乘法

[▶ 00:00](https://youtu.be/b8ygAt9n4nY?t=0)

接第 46 集的定義 $\mathfrak{a}\mathfrak{b} = \{\sum x_jy_j : x_j\in\mathfrak{a},\ y_j\in\mathfrak{b}\}$。若 $\mathfrak{a} = (\alpha_1,\dots,\alpha_m)$、$\mathfrak{b} = (\beta_1,\dots,\beta_n)$，則
$$\mathfrak{a}\mathfrak{b} = (\alpha_1\beta_1,\ \alpha_1\beta_2,\ \dots,\ \alpha_m\beta_n).$$
**乘兩個理想，就把生成元兩兩相乘**，全部列出來。

**主理想更簡單** [▶ 00:30](https://youtu.be/b8ygAt9n4nY?t=30)：主理想由一個元素生成。若 $\mathfrak{a} = (\alpha)$、$\mathfrak{b} = (\beta)$，則
$$(\alpha)(\beta) = (\alpha\beta).$$

---

## 2. 理想的整除 = 反過來的包含

[▶ 01:01](https://youtu.be/b8ygAt9n4nY?t=61)

**定義**【課堂討論】：$\mathfrak{a}\mid\mathfrak{b}$ 指存在理想 $\mathfrak{c}$ 使 $\mathfrak{b} = \mathfrak{a}\mathfrak{c}$。（講者：「我有沒有寫反？寫出來才知道。」）

> **定理**（Conrad Theorem 4.27 的一部分，依講者口述）[▶ 02:03](https://youtu.be/b8ygAt9n4nY?t=123)：
> $$\mathfrak{a}\mid\mathfrak{b}\iff\mathfrak{a}\supseteq\mathfrak{b}.$$

**整除就是包含**——而且方向是「除數比較大」。

**例**（講者：「這不是我們現在在的地方，但運作方式一樣，比較簡單」）[▶ 03:42](https://youtu.be/b8ygAt9n4nY?t=222)：在 $\mathbb{Z}$ 裡
$$20\mathbb{Z}\cdot10\mathbb{Z} = 200\mathbb{Z},\qquad\text{即 }(20)(10) = (200).$$

- 所以理想 $(10)$ **整除** $(200)$。
- 包含：$10\mathbb{Z}\supseteq200\mathbb{Z}$——200 的倍數都是 10 的倍數。

【課堂討論】[▶ 04:13](https://youtu.be/b8ygAt9n4nY?t=253) 學生一開始被「它們都是整數的集合」搞混，又在包含的方向上來回。講者：「10 的倍數**包含**全部 200 的倍數。」口訣：**整除者包含被整除者**（to contain is to divide）。

---

## 3. 乘法的性質、共軛理想

**乘法的性質** [▶ 05:51](https://youtu.be/b8ygAt9n4nY?t=351)：

- $\mathfrak{a}\mathfrak{b} = (0)$ ⇒ $\mathfrak{a} = (0)$ 或 $\mathfrak{b} = (0)$。（「很酷」——像整環沒有零因子。）
- **可交換**、**可結合**。

**共軛理想** [▶ 06:21](https://youtu.be/b8ygAt9n4nY?t=381)：
$$\bar{\mathfrak{a}} = \{\bar\alpha : \alpha\in\mathfrak{a}\}.$$
性質跟數的共軛一樣：$\overline{\mathfrak{a}\mathfrak{b}} = \bar{\mathfrak{a}}\,\bar{\mathfrak{b}}$、$\bar{\bar{\mathfrak{a}}} = \mathfrak{a}$。

**理想的共軛比數的有趣** [▶ 07:24](https://youtu.be/b8ygAt9n4nY?t=444)：有些理想**自共軛**卻不只是 $\mathbb{Z}$ 的東西。例：
$$\overline{(2,\sqrt{-14})} = (2,-\sqrt{-14}) = (2,\sqrt{-14}).$$
（講者：「可以證，我不做。」）這個理想自共軛，但裡面有 $\sqrt{-14}$ 的部分，不只是「實部」。

（相等的理由：$-\sqrt{-14} = (-1)\cdot\sqrt{-14}$，兩邊的生成元互相在對方裡面，第 46 集「只要檢查生成元」。這句**不是逐字稿內容**。）

**把數和理想連起來的關鍵** [▶ 08:24](https://youtu.be/b8ygAt9n4nY?t=504)：$\alpha,\beta\in\mathcal{O}_K$，
$$(\alpha)\mid(\beta)\iff\alpha\mid\beta.$$
所以主理想的整除跟元素的整除一模一樣——**數可以看成特殊的理想**。

---

## 4. 修好 15 的兩種分解

[▶ 09:23](https://youtu.be/b8ygAt9n4nY?t=563)

回到開頭的例子：$15 = 3\cdot5 = (1+\sqrt{-14})(1-\sqrt{-14})$。令
$$P = (3,\ 1+\sqrt{-14}),\qquad Q = (5,\ 1+\sqrt{-14}).$$
可以算出 [▶ 10:12](https://youtu.be/b8ygAt9n4nY?t=612)：
$$(3) = P\bar P,\qquad(5) = Q\bar Q,\qquad PQ = (1+\sqrt{-14}),\qquad\bar P\bar Q = (1-\sqrt{-14}).$$

**在理想的層次** [▶ 11:18](https://youtu.be/b8ygAt9n4nY?t=678)：
$$(3)(5) = P\bar P\cdot Q\bar Q = (PQ)(\bar P\bar Q) = (1+\sqrt{-14})(1-\sqrt{-14})$$
（理想的乘法可交換，可以重排）。

$P$、$Q$（和 $\bar P$、$\bar Q$）是**質理想**。講者 [▶ 12:30](https://youtu.be/b8ygAt9n4nY?t=750)：「我沒怎麼講怎麼理解理想的質性，但就跟我們理解數的質性一樣——質理想就是基本上不能再分解的那種。」

所以理想 $(15)$ **沒有兩種不同的質分解**——它的質因數分解就是 $P\bar PQ\bar Q$。「在數的層次我們看到的，只是**把這些質因子用不同方式配對**。」

$$\underbrace{(P\bar P)}_{(3)}\underbrace{(Q\bar Q)}_{(5)} = \underbrace{(PQ)}_{(1+\sqrt{-14})}\underbrace{(\bar P\bar Q)}_{(1-\sqrt{-14})}$$

> 以下**不是逐字稿內容**，是驗算兩個等式（用第 46 集「乘理想 = 生成元兩兩相乘」）：
> - $PQ = \left(15,\ 3(1+\sqrt{-14}),\ 5(1+\sqrt{-14}),\ (1+\sqrt{-14})^2\right)$。四個生成元都是 $1+\sqrt{-14}$ 的倍數（$15 = (1+\sqrt{-14})(1-\sqrt{-14})$），所以 $PQ\subseteq(1+\sqrt{-14})$；又 $2\cdot5(1+\sqrt{-14})-3\cdot3(1+\sqrt{-14}) = 1+\sqrt{-14}$，所以 $1+\sqrt{-14}\in PQ$。相等。
> - $P\bar P = \left(9,\ 3(1-\sqrt{-14}),\ 3(1+\sqrt{-14}),\ 15\right)$。每個生成元都是 3 的倍數，所以 $\subseteq(3)$；又 $15-9 = 6$、$9-6 = 3$，所以 $3\in P\bar P$。相等。（$Q\bar Q = (5)$ 同理：$Q\bar Q = (25,\ 5(1\pm\sqrt{-14}),\ 15)$，$25-15 = 10$、$15-10 = 5$。）

---

## 5. 大定理：理想的唯一分解

[▶ 13:19](https://youtu.be/b8ygAt9n4nY?t=799)

講者「說但不寫」，順帶提到途中的定理：

- **理想的和就是最大公因數**：取線性組合（相加）就是 gcd。（對照第 39 集：互極大是互質的理想版本。）
- **範數是 $\mathbb{Z}$ 的質數的理想是質理想。**
- 非零質理想 = 極大理想 = 真理想，而且每次分解它，其中一個因子是單位理想 $(1)$。

> **定理**（Conrad Theorem 7.10，p. 18，依講者口述）[▶ 14:23](https://youtu.be/b8ygAt9n4nY?t=863)：$\mathcal{O}_K$ 裡每個非零、非單位（不是 $(1)$）的理想，都能寫成**質理想的乘積**，而且在因子順序之外**唯一**：若 $\mathfrak{a} = P_1\cdots P_r = Q_1\cdots Q_s$（都是質理想），則兩邊的質理想相同，只是重排。

講者：「就像整數的質因數分解，理想也一樣。**我們確實找回了質因數分解**——在理想的層次。」

> **定理**（Conrad Theorem 7.12，依講者口述）[▶ 15:25](https://youtu.be/b8ygAt9n4nY?t=925)：$\mathcal{O}_K$ 的元素有唯一分解 ⇔ $\mathcal{O}_K$ 的每個理想都是主理想。

講者：這退一步問「元素層次的唯一分解**在哪裡**失敗？」答案：恰好在 $\mathcal{O}_K$ **不是 PID** 的時候——例如 $\mathbb{Z}[\sqrt{-5}]$，「我想那是我們第一次看到唯一分解失敗的地方」。（課程裡 $\mathbb{Z}[\sqrt{-3}]$ 在第 22 集、講義的 $\mathbb{Z}[\sqrt{-5}]$ 在第 39 集。）

> 以下**不是逐字稿內容**，是把這兩個定理接回第 39 集：第 39 集證過 PID ⇒ UFD；Theorem 7.12 說在 $\mathcal{O}_K$ 裡反方向也對。所以在 $\mathbb{Z}[\sqrt{-14}]$ 裡，$P = (3,1+\sqrt{-14})$ 一定**不是主理想**——否則 $P = (\pi)$，$\pi\mid3$ 且 $3 = \pi\bar\pi$ 會跟「3 不可約」矛盾（$\pi$ 和 $\bar\pi$ 都不是單位，因為理想的範數是 3）。元素層次的分解失敗，正是因為這些質理想沒有一個「數」可以代表。

【口頭】[▶ 15:55](https://youtu.be/b8ygAt9n4nY?t=955) 「我還沒開始真正講這份 PDF，還有很多。如果你想學更多——如果你是有志的**代數數論**學者，你應該仔細研讀 Keith Conrad 寫的每一樣東西。」

「總之，這學期很好玩。謝謝大家。」

---

## 6. 一頁速查表

**理想乘法**：$(\alpha_1,\dots,\alpha_m)(\beta_1,\dots,\beta_n) = (\alpha_i\beta_j\text{ 全部})$；$(\alpha)(\beta) = (\alpha\beta)$。

**整除 = 包含**：$\mathfrak{a}\mid\mathfrak{b}\iff\mathfrak{a}\supseteq\mathfrak{b}$。例：$(10)\mid(200)$，$10\mathbb{Z}\supseteq200\mathbb{Z}$。$(\alpha)\mid(\beta)\iff\alpha\mid\beta$。

**性質**：$\mathfrak{a}\mathfrak{b} = 0$ ⇒ 其一為 0；可交換、可結合；$\overline{\mathfrak{a}\mathfrak{b}} = \bar{\mathfrak{a}}\bar{\mathfrak{b}}$。自共軛例：$(2,\sqrt{-14})$。

**修好 15**（$\mathbb{Z}[\sqrt{-14}]$）：$P = (3,1+\sqrt{-14})$、$Q = (5,1+\sqrt{-14})$ 是質理想，
$$(3) = P\bar P,\quad(5) = Q\bar Q,\quad(1\pm\sqrt{-14}) = PQ,\ \bar P\bar Q,\quad(15) = P\bar PQ\bar Q.$$
**關鍵一步**：$10(1+\sqrt{-14})-9(1+\sqrt{-14}) = 1+\sqrt{-14}$，所以 $1+\sqrt{-14}\in PQ$。

**大定理**：$\mathcal{O}_K$ 的非零非單位理想唯一分解成質理想（Theorem 7.10）；元素唯一分解 ⇔ PID（Theorem 7.12）。理想的和 = gcd。

---

## 7. 回顧：整門課走到哪裡

> 以下**不是逐字稿內容**，是把全課串起來的導覽：
>
> | 階段 | 集數 | 主線 |
> |---|---|---|
> | 整數的算術 | 1–14 | Euclid、Bézout、質因數分解、同餘、群、RSA |
> | 唯一分解的威力 | 15–24 | 高斯整數、Eisenstein 整數、四元數；$\mathbb{Z}[\sqrt{-3}]$ 失敗；費馬最後定理的歷史 |
> | 二次互反律 | 25–26 | |
> | 環與理想 | 27–35 | 環、理想、商環、質／極大理想、同態、分式體、多項式環 |
> | 分解的抽象理論 | 36–39 | PID、不可約 vs 質、Euclid ⇒ PID ⇒ UFD |
> | 擴張體 | 40–45 | Kronecker、最小多項式、$[K:F]$、本原元素 |
> | 理想修好唯一分解 | 46–47 | $\mathcal{O}_K$、理想的唯一分解 |

---

## 附：本集一句話總結

> **理想可以相乘（生成元兩兩相乘），而且「整除」就是「包含」。在 $\mathbb{Z}[\sqrt{-14}]$ 裡，$15$ 的兩種分解只是同一組質理想 $P,\bar P,Q,\bar Q$ 的兩種配對：$(3)(5) = (P\bar P)(Q\bar Q) = (PQ)(\bar P\bar Q) = (1+\sqrt{-14})(1-\sqrt{-14})$。二次體的整數裡，每個理想都唯一分解成質理想——唯一分解在理想的層次被找回來了；元素層次失敗，恰好是因為環不是 PID。**

---

*筆記依據 James S. Cook「Number Theory」2021-12-01 第 2 部錄影逐字稿（whisper 轉錄，16:41）整理；課堂內容出自 Keith Conrad「Factoring in quadratic fields」，該 PDF 未列入本筆記來源，定理編號照講者口述。*
