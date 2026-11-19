---
course: Number Theory（2021 秋，線上錄影）
episode: 30
lecture: 2021-10-20 第 2 部
date: 2021-10-20
video: https://youtu.be/Ihh0LA4rpwg
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.2 Example 4.2.18（p. 133）、§4.3 Lecture 23（p. 134–136）：Definition 4.3.1、Example 4.3.2–4.3.3、Theorem 4.3.6–4.3.7（陳述）
---

# 第 30 集 · 質理想與極大理想登場（Prime and Maximal Ideals Introduced） [▶ 影片](https://youtu.be/Ihh0LA4rpwg)

← 上一集：[29-ideals-factor-rings](29-ideals-factor-rings.md) ｜ [總目錄](README.md) ｜ 下一集：[31-prime-maximal-ideal-theorems-1](31-prime-maximal-ideal-theorems-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 30 集（2021-10-20 第 2 部，接第 29 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（17:13，自動字幕）＋ 講者講義 §4.2–4.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. R[x]/⟨x² + 1⟩ 就是複數](#1-rxx--1-就是複數)
- [2. 質理想與極大理想的定義](#2-質理想與極大理想的定義)
- [3. pZ 是質理想](#3-pz-是質理想)
- [4. Z₃₆ 的理想格子圖](#4-z-的理想格子圖)
- [5. 預告兩個大定理](#5-預告兩個大定理)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

收尾第 29 集的 $\mathbb{R}[x]/\langle x^2+1\rangle$，然後定義**質理想**和**極大理想**，用 $\mathbb{Z}_{36}$ 的圖看出它們跟「商環是不是體」的關係。

| 主題 | 時間 | 講義 |
|---|---|---|
| $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$ | 00:01 | Ex 4.2.18 |
| 定義 | 05:08 | Def 4.3.1 |
| $p\mathbb{Z}$ | 07:26 | Ex 4.3.2 |
| $\mathbb{Z}_{36}$ | 09:32 | Ex 4.3.3 |
| 兩個定理（預告） | 14:50 | Thm 4.3.6–4.3.7 |

---

## 1. R[x]/⟨x² + 1⟩ 就是複數

[▶ 00:01](https://youtu.be/Ihh0LA4rpwg?t=1)

接第 29 集：在商環裡 $x^2 = -1$。（講者把理想 $\langle x^2+1\rangle$ 簡寫成 $A$，「寫括號寫累了」。）

**任何陪集都能化成 $a+bx+A$**：例如 10 次多項式
$$a_{10}x^{10}+\cdots+a_1x+a_0+A = \left[a_{10}(-1)^5+a_8(-1)^4+\cdots+a_0\right] + x\left[a_9(-1)^4+a_7(-1)^3+\cdots+a_1\right]+A.$$
偶次項變成常數，奇次項變成 $x$ 的係數。（講者：「我幹嘛寫出來，白痴。」）重點：$x^2 = -1$，所有高次方都能壓到常數項和一次項。

**乘法** [▶ 02:34](https://youtu.be/Ihh0LA4rpwg?t=154)：
$$(a+bx+A)(c+dx+A) = ac+(ad+bc)x+bd\,x^2+A = (ac-bd)+(ad+bc)x+A.$$

把 $x$ 換成 $i$：$(a+bi)(c+di) = (ac-bd)+(ad+bc)i$——**正是複數乘法** [▶ 04:08](https://youtu.be/Ihh0LA4rpwg?t=248)。

> **結論**：複數的一個模型是 $\mathbb{R}[x]/\langle x^2+1\rangle$——實係數多項式模掉 $x^2+1$ 生成的理想。

【口頭】「我覺得這是構造複數最優雅、最美的方法之一。但有代價：2×2 矩陣（第 1–2 集）對高中生容易接受得多。」

（講義說這是 Cauchy 在 1847 年給的構造，見第 29 集。）

---

## 2. 質理想與極大理想的定義

[▶ 05:08](https://youtu.be/Ihh0LA4rpwg?t=308)

> **定義**（講義 Definition 4.3.1）：$R$ 是可交換環，$A$ 是 $R$ 的**真**理想。
> 1. **質理想**（prime ideal）：$a,b\in R$、$ab\in A$ ⇒ $a\in A$ 或 $b\in A$。
> 2. **極大理想**（maximal ideal）：若理想 $B$ 滿足 $A\subseteq B\subseteq R$，則 $B = A$ 或 $B = R$。

（講者特別提醒「**真**理想——小心！」）

白話：

- **質理想**：像質數一樣——乘積掉進來，就有一個因數掉進來。
- **極大理想**：夾在 $A$ 和整個環之間，**沒有別的理想**。

> 【講義補充】Definition 4.3.1 後面（p. 134）：「質」這個名字自然連到我們在 $\mathbb{Z}$ 裡的質數：Euclid 引理說質數 $p\mid ab$ ⇒ $p\mid a$ 或 $p\mid b$。講義說還有另一種定義質理想的方式，讓「理想的包含」和「整數的整除」的對應更清楚，見他 Math 307 講義的 Lecture 22。

---

## 3. pZ 是質理想

[▶ 07:26](https://youtu.be/Ihh0LA4rpwg?t=446)

【課堂討論】講者問：質數生成的理想會是質理想嗎？「我打賭是。」

**證明**（講義 Example 4.3.2）：$p$ 是質數。設 $a,b\in\mathbb{Z}$、$ab\in p\mathbb{Z}$。

1. $ab = pk$，所以 $p\mid ab$。
2. 由 **Euclid 引理**（第 5 集）[▶ 08:28](https://youtu.be/Ihh0LA4rpwg?t=508)：$p\mid a$ 或 $p\mid b$。
3. $a = pn$ 或 $b = pm$，也就是 $a\in p\mathbb{Z}$ 或 $b\in p\mathbb{Z}$。∎

所以**質數生成的主理想是質理想**。

> 以下**不是逐字稿內容**，是補一個對照：合數 $n = st$（$1<s,t<n$）時，$st\in n\mathbb{Z}$ 但 $s,t\notin n\mathbb{Z}$，所以 $n\mathbb{Z}$ **不是**質理想。例如 $2\cdot 3\in 6\mathbb{Z}$ 但 $2,3\notin 6\mathbb{Z}$。

---

## 4. Z₃₆ 的理想格子圖

[▶ 09:32](https://youtu.be/Ihh0LA4rpwg?t=572)

講者：要理解極大理想，畫**格子圖**（lattice diagram）很有用。【口頭】「這是我教抽象代數時犯的錯：我不夠強調這些圖。真正的代數學家用這些圖比我多得多。」

$\mathbb{Z}_{36}$（也就是 $\mathbb{Z}/36\mathbb{Z}$）的理想，由上（大）到下（小）：

```
             Z₃₆
           /     \
        ⟨2⟩       ⟨3⟩
       /    \    /    \
     ⟨4⟩     ⟨6⟩      ⟨9⟩
        \   /    \   /
        ⟨12⟩     ⟨18⟩
           \     /
            ⟨0⟩
```

（圖是依講者口述「$\langle2\rangle$、$\langle3\rangle$ 在下面、再下面是 $\langle4\rangle$……兩個合起來得到這些……最下面是 0」整理的；講義 p. 134 有這張圖。線表示包含關係。）

**理想的大小** [▶ 11:39](https://youtu.be/Ihh0LA4rpwg?t=699)：

- $\langle 2\rangle$ 有 **18** 個元素，「基本上就是偶數」。
- $\langle 3\rangle$ 有 **12** 個：$0,3,6,9,12,15,18,21,24,27,30,33$。

**$\langle2\rangle$ 和 $\langle3\rangle$ 是極大理想** [▶ 12:11](https://youtu.be/Ihh0LA4rpwg?t=731)：它們和整個環之間**沒有別的理想**。

**看商環** [▶ 12:45](https://youtu.be/Ihh0LA4rpwg?t=765)：

| 理想 $A$ | 元素數 | $\mathbb{Z}_{36}/A$ 有幾個陪集 | $\mathbb{Z}_{36}/A\cong$ | 是體？ |
|---|---|---|---|---|
| $\langle 2\rangle$ | 18 | $36/18 = 2$ | $\mathbb{Z}_2$ | ✅ |
| $\langle 3\rangle$ | 12 | $36/12 = 3$ | $\mathbb{Z}_3$ | ✅ |
| $\langle 4\rangle$ | 9 | $36/9 = 4$ | $\mathbb{Z}_4$ | ❌ |

- 講者：陪集把 $\mathbb{Z}_{36}$ 切成**一樣大**的塊，所以 12 個元素的理想給 3 個陪集，18 個的給 2 個。
- $\langle 2\rangle$、$\langle 3\rangle$ 是極大理想，商環**是體**。
- $\langle 4\rangle$ 不是極大理想（$\langle4\rangle\subsetneq\langle2\rangle\subsetneq\mathbb{Z}_{36}$），商環 $\cong\mathbb{Z}_4$ **不是體**。

講者 [▶ 13:17](https://youtu.be/Ihh0LA4rpwg?t=797)：「這說明一個定理：**環模極大理想是體**。」

> 【講義補充】Example 4.3.3（p. 134）也看了**理想裡面的理想**：$\langle 12\rangle$ 和 $\langle 18\rangle$ 是 $\langle 6\rangle$ 裡的極大理想。例如
> $$\langle6\rangle = \{0,6,12,18,24,30\},\quad\langle 12\rangle = \{0,12,24\},\quad\langle6\rangle/\langle12\rangle = \{\langle12\rangle,\ 6+\langle12\rangle\}\cong\mathbb{Z}_2.$$
> （嚴格說 $\langle 6\rangle$ 沒有乘法單位元素——它是 rng——所以這只是類比。這一句**不是講義內容**。）

---

## 5. 預告兩個大定理

[▶ 14:50](https://youtu.be/Ihh0LA4rpwg?t=890)

【課堂討論】學生問：是若且唯若嗎？還有：$\mathbb{C}$ 是體，那能證 $\langle x^2+1\rangle$ 是 $\mathbb{R}[x]$ 的極大理想嗎？講者：好問題。講義下一個例子（Example 4.3.4）就**直接證明** $\langle x^2+1\rangle$ 在 $\mathbb{R}[x]$ 裡是極大的，再給一個 $\mathbb{Z}_2[x]$ 裡的反例。然後是兩個定理：

> **定理**（講義 Theorem 4.3.6）：$R$ 是有單位元素的可交換環，$A$ 是理想。
> $$R/A\ \text{是整環}\iff A\ \text{是質理想}.$$

> **定理**（講義 Theorem 4.3.7）：$R$ 是有單位元素的可交換環，$A$ 是理想。
> $$R/A\ \text{是體}\iff A\ \text{是極大理想}.$$

（講者順便說：商環也叫**商環**（quotient ring），factor ring 和 quotient ring 是同義詞。）

**兩個方向都有用** [▶ 15:50](https://youtu.be/Ihh0LA4rpwg?t=950)：

- 如果早知道 $\mathbb{C}$ 是體，那 $\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$ 是體，**由定理 4.3.7 就知道** $\langle x^2+1\rangle$ 是極大理想，不用 Example 4.3.4 的直接計算。
- 「有時證明某個東西是體，比證明理想是極大的容易得多。」反之亦然。

講者說這是他（講義）Lecture 22–23 的兩個大定理。

**進度** [▶ 16:20](https://youtu.be/Ihh0LA4rpwg?t=980)：講者想「稍微超前」，因為之後有一天要講兩件事、中間還有一份講義要插，「希望下次講完 23，進到 24」。

【口頭】講者問學生覺得帶回家考（take-home test）怎樣。學生：「還沒看。」「不好玩。」

---

## 6. 一頁速查表

**$\mathbb{R}[x]/\langle x^2+1\rangle\cong\mathbb{C}$**：每個陪集有代表元 $a+bx$；$x^2 = -1$；乘法 $(a+bx)(c+dx) = (ac-bd)+(ad+bc)x$。

**質理想**（真理想）：$ab\in A$ ⇒ $a\in A$ 或 $b\in A$。

**極大理想**（真理想）：$A\subseteq B\subseteq R$ ⇒ $B=A$ 或 $B=R$。

**例子**

- $p\mathbb{Z}$（$p$ 質數）是質理想。**關鍵一步**：Euclid 引理。
- $n\mathbb{Z}$（$n$ 合數）不是質理想：$st\in n\mathbb{Z}$、$s,t\notin n\mathbb{Z}$。
- $\mathbb{Z}_{36}$：極大理想 $\langle2\rangle,\langle3\rangle$；商環 $\mathbb{Z}_2,\mathbb{Z}_3$ 是體。$\langle4\rangle$ 不是極大，商環 $\mathbb{Z}_4$ 不是體。

**兩個大定理**（$R$ 有 1 的可交換環）：

| $A$ | $R/A$ |
|---|---|
| 質理想 | 整環 |
| 極大理想 | 體 |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 定理 4.3.6–4.3.7 的證明；$\langle x^2+1\rangle$ 極大的直接證明 | 第 31–32 集 |
| 極大 ⇒ 質；質但不極大的例子（$\langle x\rangle\subseteq\mathbb{Z}[x]$） | 第 31–32 集 |
| 環同態、同構（$\mathbb{Z}_{36}/\langle2\rangle\cong\mathbb{Z}_2$ 的嚴格說法） | 第 31–32 集 |
| $F[x]/\langle p(x)\rangle$ 是體 ⇔ $p$ 不可約 | 第 36–37、40–43 集 |

---

## 附：本集一句話總結

> **把 $\mathbb{R}[x]$ 裡的 $x^2+1$ 壓成零，得到的商環就是複數。質理想是「乘積在裡面，就有一個因數在裡面」，極大理想是「上面只剩整個環」；從 $\mathbb{Z}_{36}$ 的格子圖看出：模極大理想得到體（$\mathbb{Z}_2$、$\mathbb{Z}_3$），模非極大理想不是（$\mathbb{Z}_4$）——下集證明這是一般定理。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-20 第 2 部錄影逐字稿（YouTube 自動字幕，17:13）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.2–4.3 整理。*
