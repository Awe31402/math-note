---
course: Abstract Algebra II (Spring 2026)
episode: 37
lecture: L32
date: 2026-04-22
video: https://www.youtube.com/watch?v=pmeDdms6LH8
notes: 講義/AA2/Math422_Lecture32_ClassificationModulesPIDsTheorems.pdf、SmithNormalFormANDRationalCannonicalForm_4_29_18.pdf
---

# 第 37 集 · L32：Smith 標準形與 PID 上模的分類 [▶ 影片](https://www.youtube.com/watch?v=pmeDdms6LH8&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[36-L31-PID上有限生成模基本定理]] ｜ [總目錄](../README.md) ｜ 下一集：[[38-紐結群計算]] →

## 本集概要

D&F §12.1–12.2：
- 複習不變因子形式（Thm 5）、初等因子形式（Thm 6）；**準素分解定理**（Thm 7，不需有限生成）。
- $V$ 作為 $F[x]$-模（由 $T$ 或矩陣 $A$ 誘導）是純撓的；**特徵多項式**、**最小多項式**；最大不變因子 = 最小多項式。
- 例：Jordan 形矩陣的不變因子（老師現場猜錯，後來修正）。
- **Smith 標準形**：對 $xI-A$ 做多項式係數的**列與行**運算，化成對角 $\mathrm{diag}(1,\dots,1,a_1,\dots,a_m)$，$a_1\mid\cdots\mid a_m$。多個例子（老師網站上的講義）。
- **伴隨矩陣**；**有理標準形** = 不變因子伴隨矩陣的直和；初等因子 ↔ Jordan 塊；準素分量 ↔ 廣義特徵空間。

> 📘 講義對應：Math422 Lecture 32「Classification of Modules over PIDs — Theorems」；老師網站上的「Smith Normal Form and Rational Canonical Form」（2018-04-29）；D&F §12.1（Thm 5–7）、§12.2。

---

## 筆記

### 1. 複習與準素分解 [▶ 01:00](https://youtu.be/pmeDdms6LH8?t=60)

（開場學生在聊「綠旗」和「不准擁有煎烤盤」；「你還沒禱告——萬一這堂課很糟怎麼辦？」）

- **不變因子形式**：$M\cong R^r\oplus R/(a_1)\oplus\cdots\oplus R/(a_m)$，$a_1\mid\cdots\mid a_m$ 非單位；$r$ 是**自由秩**。
- **初等因子形式**：$M\cong R^r\oplus R/(p_1^{\alpha_1})\oplus\cdots\oplus R/(p_t^{\alpha_t})$，$p_i$ 是質元，**可以重複**。

> **定理 7**（**準素分解**，primary decomposition）：$R$ 是 PID，$M$ 是非零撓 $R$-模，零化子 $a = up_1^{\alpha_1}\cdots p_n^{\alpha_n}$（$p_i$ 相異質元）。令
> $$N_i = \{x\in M\mid p_i^{\alpha_i}x = 0\}.$$
> 則 $N_i$ 是零化子為 $p_i^{\alpha_i}$ 的子模，也就是被 $p_i$ 的某個冪零化的元素全體，且 $M = N_1\oplus\cdots\oplus N_n$。若 $M$ 有限生成，每個 $N_i$ 是有限個循環模的直和，零化子都整除 $p_i^{\alpha_i}$。$N_i$ 叫 $M$ 的 **$p_i$-準素分量**。

- 這個定理**不**假設 $M$ 有限生成 [▶ 10:00](https://youtu.be/pmeDdms6LH8?t=600)。可以想成把 Thm 6 中同一個質數的項放在一起。
- （學生在拉筋、扳關節，Violet 很受不了。）

### 2. $F[x]$-模的情形 [▶ 11:30](https://youtu.be/pmeDdms6LH8?t=690)

「怎麼實際找出分解？意義是什麼？」——這就是 **Smith 標準形**的用處。D&F 只對 $F[x]$-模講，但它對 $\mathbb{Z}$-模（交換群的關係矩陣）也有意義，下次講。

- $T:V\to V$（$\dim V = n$），$f(x)\cdot v = f(T)v$；或矩陣 $A$：$f(x)\cdot v = f(A)v$。上次證明 $V$ 是**純撓**的：$V\cong F[x]/(a_1(x))\oplus\cdots\oplus F[x]/(a_m(x))$ [▶ 13:30](https://youtu.be/pmeDdms6LH8?t=810)。

> **定義**：**特徵多項式** $p_T(x) = \det(xI-T)$；**最小多項式** $m_T(x)$ = 使 $m_T(T) = 0$ 的最低次首一多項式。

Math 321 的結果 [▶ 18:30](https://youtu.be/pmeDdms6LH8?t=1110)：
1. **Cayley–Hamilton**：$p_T(T) = 0$。
2. $m_T\mid p_T$，兩者有相同的根。

> **定理**：$a_m(x) = m_T(x)$——最大的不變因子就是最小多項式（也是模的零化子）。而且所有不變因子的乘積是特徵多項式 [▶ 20:30](https://youtu.be/pmeDdms6LH8?t=1230)。

**例**（Jordan 形）[▶ 21:30](https://youtu.be/pmeDdms6LH8?t=1290)：$A = J_2(3)\oplus J_1(3)\oplus J_2(2)\oplus J_2(2)\oplus J_1(2)\oplus J_1(2)$（老師現場編的）。
- $p_A = (x-3)^3(x-2)^6$；$m_A = (x-3)^2(x-2)^2$——每個特徵值取最大 Jordan 塊的大小。
- 若所有塊都是 $1\times1$，最小多項式**沒有重根**：**可對角化 ⇔ 最小多項式是相異一次因式的乘積** [▶ 23:30](https://youtu.be/pmeDdms6LH8?t=1410)。
- 不變因子？老師先猜只有三個（$a_1 = (x-2)^2$、$a_2 = (x-3)(x-2)^2$、$a_3 = m_A$），學生追問「這唯一嗎？」「不變因子必須相異嗎？」——老師沒說必須相異。看完後面的例子後老師改口：應該有**四個** [▶ 41:30](https://youtu.be/pmeDdms6LH8?t=2490)：
$$a_1 = x-2,\quad a_2 = x-2,\quad a_3 = (x-3)(x-2)^2,\quad a_4 = (x-3)^2(x-2)^2.$$
  （乘積 $(x-3)^3(x-2)^6 = p_A$，且 $a_1\mid a_2\mid a_3\mid a_4$。）
- **初等因子**：每個 Jordan 塊一個——$(x-3)^2,\ (x-3),\ (x-2)^2,\ (x-2)^2,\ (x-2),\ (x-2)$ [▶ 51:30](https://youtu.be/pmeDdms6LH8?t=3090)。

### 3. Smith 標準形 [▶ 29:00](https://youtu.be/pmeDdms6LH8?t=1740)

老師網站上有「Smith 標準形的簡單計算」講義，一大堆例子。（網站的安全憑證還在修。）

**做法**：從多項式矩陣 $xI-A$ 出發，允許：
- **列運算**，係數可以是數**或多項式**；
- **行運算**（也可以！）——大致對應重新標記基底，下次用交換群的關係矩陣說明。

目標：對角形 $\mathrm{diag}(1,\dots,1,a_1(x),\dots,a_m(x))$，**$a_1\mid a_2\mid\cdots\mid a_m$**（首一）。非單位的對角元就是不變因子。

**例 1**（3×3）[▶ 31:30](https://youtu.be/pmeDdms6LH8?t=1890)：
- 列交換把常數項換到左上；$R_2+2R_1$；**$R_3-(x-2)R_1$**——「這是新招」。
- 有了左上的 1，用行運算把第一列清掉：$C_2-C_1$、$C_3-(x-5)C_1$。
- $R_3+R_2$ 讓 $x$ 抵消；$C_3-2C_2$「像 Taylor Swift 的歌，消滅了 X」；行交換、除以 $-9$ 得到 1……
- 結果 $\mathrm{diag}(1,1,x(x-3)(x-6))$：最小多項式 $x(x-3)(x-6)$ 沒有重根 ⇒ **可對角化**，特徵值 0、3、6 [▶ 35:00](https://youtu.be/pmeDdms6LH8?t=2100)。
- 驗算：跡是 9，特徵值和 $0+3+6 = 9$（學生起鬨說「10」）。
- D&F 有演算法能沿著行運算追回特徵基底，「我強烈建議不要學，太可怕了」。（學生：「寫成程式有加分嗎？」——「你會得到成為全人口 0.003% 的滿足感。」）

**更多例子** [▶ 36:30](https://youtu.be/pmeDdms6LH8?t=2190)
- 對角矩陣 $\mathrm{diag}(2,3)$：Smith 形給出最小多項式 $(x-2)(x-3)$。
- $2\times2$ Jordan 塊：$\mathrm{diag}(1,(x-\lambda)^2)$。
- 沒有實特徵值的矩陣（$x^2+1$ 的**伴隨矩陣**）：$\mathrm{diag}(1,x^2+1)$。只有一個非單位因子時，最小多項式 = 特徵多項式。
- $\mathrm{diag}(2,2,3,3)$：中途得到 $\mathrm{diag}(1,1,x-2,x-3)$——**不是** Smith 形，因為 $x-2\nmid x-3$；繼續做得 $\mathrm{diag}(1,1,(x-2)(x-3),(x-2)(x-3))$。不變因子可以相等——所以上面例子應該是四個 [▶ 40:00](https://youtu.be/pmeDdms6LH8?t=2400)。
- 4×4 實 Jordan 塊（特徵值 $2\pm3i$，重複）：得到 $((x-2)^2+9)^2$。
- 兩個實 3×3 Jordan 塊；有 $J_2(3)$ 加上特徵值 4、5 的例子：最小多項式必須含 $(x-4)$、$(x-5)$，但不需要平方（沒有 2×2 塊）[▶ 45:30](https://youtu.be/pmeDdms6LH8?t=2730)。
- 考試三可能考：「算這個矩陣的 Smith 標準形」；若說不用寫步驟，寫結果就好。「你都修了四門理論代數，該學會：**可對角化 ⇔ 最小多項式分解成相異一次因式**。」[▶ 37:30](https://youtu.be/pmeDdms6LH8?t=2250)

### 4. 有理標準形 [▶ 46:30](https://youtu.be/pmeDdms6LH8?t=2790)

- **循環子空間** $\langle\langle v\rangle\rangle = \mathrm{span}\{v,Tv,T^2v,\dots\}$（不是 D&F 的記號）。$T$ 限制在上面，用這組基底的矩陣是一個**伴隨矩陣**。

> **定義**：首一 $p(x) = x^k+b_{k-1}x^{k-1}+\cdots+b_0$ 的**伴隨矩陣**（companion matrix）$C(p)$：次對角線全是 1，最後一欄是 $-b_0,\dots,-b_{k-1}$。它的特徵多項式就是 $p(x)$（Math 321 的作業——學生堅稱沒做過）。

- 例：$C(x^2+1) = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$；$x^2-2$、$x^3-2$ 類似 [▶ 48:30](https://youtu.be/pmeDdms6LH8?t=2910)。
- 正負號的慣例（放在哪裡）各書不同；老師比較喜歡讓多項式係數保持正號、把負號放在矩陣裡。

**三種分解，同一個例子** [▶ 52:30](https://youtu.be/pmeDdms6LH8?t=3150)
- **有理標準形**：不變因子伴隨矩陣的直和
$$C(x-2)\oplus C(x-2)\oplus C\big((x-3)(x-2)^2\big)\oplus C\big(m_A\big).$$
  「有理標準形」在不同書意義略不同，這是一種結構。它的好處：**即使沒有特徵值也有意義**；而且不變因子唯一，所以它唯一。
- **Jordan 形** ↔ **初等因子**：只在特徵值都在體裡時才有定義（$\mathbb{R}$ 上用**實 Jordan 形**——複化後再回來，旋轉伸縮塊）。Jordan 塊的順序不唯一。
- **準素分解** ↔ **廣義特徵空間**：這例子有特徵值 3 和 2 的兩個廣義特徵空間，對應 $F[x]$ 中的質元 $x-3$、$x-2$ [▶ 56:30](https://youtu.be/pmeDdms6LH8?t=3390)。

> 💬 老師抱怨代數學家不喜歡實 Jordan 形：「我問過代數學家，答案是『那很醜，你自己推就好』。不，我想要查得到——這才是重點。」[▶ 55:30](https://youtu.be/pmeDdms6LH8?t=3330)

> 💬 結尾：「你們有 AI 了，我不用教了，乾脆收攤。」然後問大家伊朗的戰爭結束了沒——「同時是也不是」。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 自由秩 | free rank | §1 |
| 準素分解 | primary decomposition | §1 |
| $p$-準素分量 | $p$-primary component | §1 |
| 特徵多項式 | characteristic polynomial | §2 |
| 最小多項式 | minimal polynomial | §2 |
| Cayley–Hamilton 定理 | Cayley–Hamilton theorem | §2 |
| Smith 標準形 | Smith normal form | §3 |
| 伴隨矩陣 | companion matrix | §4 |
| 循環子空間 | cyclic subspace | §4 |
| 實 Jordan 形 | real Jordan form | §4 |
| 廣義特徵空間 | generalized eigenspace | §4 |

## ⚠️ 待確認清單

（本集無）
