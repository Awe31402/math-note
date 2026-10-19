---
course: Abstract Algebra II (Spring 2026)
episode: 39
lecture: L33
date: 2026-04-24
video: https://www.youtube.com/watch?v=FeCKnYjPLjA
notes: 講義/AA2/Math422_Lecture33_RCF_Jordan.pdf
---

# 第 39 集 · L33：有理標準形與 Jordan 形；不變因子與初等因子 [▶ 影片](https://www.youtube.com/watch?v=FeCKnYjPLjA&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[38-紐結群計算]] ｜ [總目錄](../README.md) ｜ 下一集：[[40-L34-實結合代數的正則表示]] →

## 本集概要

D&F §12.2–12.3，PID 上模的例子：
- $n\times n$ 矩陣 $A$ 給出 $F^n$ 的 $F[x]$-模；Smith 標準形給不變因子；$m_A$ = 最後一個不變因子，$p_A$ = 不變因子的乘積。
- 用一組 $\mathbb{Q}$ 上的不變因子當例子，列出對應的初等因子（不變因子在給定矩陣下唯一，但給定特徵多項式不唯一）。
- **引理**：循環子空間 $\langle\langle v\rangle\rangle$ 的基底 $v,Av,\dots,A^{n-1}v$ 下，矩陣是**伴隨矩陣**。⇒ **有理標準形**；$A$ 相似於它（判斷相似的工具）。
- **$k$-鏈**與 **Jordan 塊** $J_k(\lambda) = \lambda I_k+N_k$；$N_k$ 冪零。⇒ **Jordan 形**（特徵值都在體裡時）。
- 例：22×22 的有理標準形；$x^4+1$ 在 $\mathbb{Q},\mathbb{R},\mathbb{C}$ 上；AI 會給錯答案。

> 📘 講義對應：Math422 Lecture 33「Rational Canonical Form & Jordan Form」；D&F §12.2–12.3（Thm 6 的詮釋）。

---

## 筆記

### 1. 設定 [▶ 01:00](https://youtu.be/FeCKnYjPLjA?t=60)

（開場學生在聊 $f'$ 的 Laplace 變換——「無關，開始吧」。）

$A\in F^{n\times n}$，$F^n$ 成為 $F[x]$-模：$f(x)\cdot v = f(A)v$。對 $xI-A$ 做 $F[x]$ 上的列、行運算（Smith 標準形）得到不變因子 $a_1(x)\mid\cdots\mid a_m(x)$ [▶ 01:30](https://youtu.be/FeCKnYjPLjA?t=90)。
- 兩種看法：用已知的線性代數理解抽象代數；或反過來，用分類定理**證明**線性代數中老師沒證過的事（例如 Jordan 基底的存在——Thm 6 適當詮釋後就給出）[▶ 03:00](https://youtu.be/FeCKnYjPLjA?t=180)。
- $m_A(x) = a_m(x)$；$p_A(x) = a_1(x)\cdots a_m(x)$。
- 不變因子不必是質元，但 $F[x]$ 是 UFD，可分解成質數冪 $d_1(x),\dots,d_s(x)$——**初等因子**。

### 2. 例：不變因子與初等因子 [▶ 06:30](https://youtu.be/FeCKnYjPLjA?t=390)

（「注意這個例子的顏色。」）在 $\mathbb{Q}$ 上：
$$a_1 = x^3-2,\quad a_2 = (x^3-2)^2(x^2+1),\quad a_3 = (x^3-2)^3(x^2+1).$$
- 另一組可能：$a_2' = x^3-2$、$a_3' = (x^3-2)^3(x^2+1)$——學生問「這不是應該唯一嗎？」（上次問過）[▶ 08:00](https://youtu.be/FeCKnYjPLjA?t=480)。
- 說清楚：**給定一個矩陣**（和基礎體），Smith 標準形與不變因子唯一；但**給定特徵多項式**，可能的不變因子組不唯一。（老師承認上次可能誤解了學生的問題。）最大的兩個不變因子也可以相等 [▶ 10:30](https://youtu.be/FeCKnYjPLjA?t=630)。
- **初等因子**（第一組）[▶ 12:30](https://youtu.be/FeCKnYjPLjA?t=750)：$x^3-2$；$(x^3-2)^2$、$x^2+1$；$(x^3-2)^3$、$x^2+1$。它們是各個不變因子的質數冪分解；乘積仍是特徵多項式。（老師一度漏了立方，學生抓到。）

**兩種分解** [▶ 15:00](https://youtu.be/FeCKnYjPLjA?t=900)
- Thm 5：$F^n\cong F[x]/(a_1)\oplus\cdots\oplus F[x]/(a_m)$ → **有理標準形**。
- Thm 6：$F^n\cong F[x]/(d_1)\oplus\cdots\oplus F[x]/(d_s)$ → 適當條件下的 **Jordan 形**。
- 關鍵：替每一塊造一組基底。

### 3. 伴隨矩陣引理 [▶ 17:00](https://youtu.be/FeCKnYjPLjA?t=1020)

（「lemma 和什麼押韻？」——「dilemma」「Emma」。）

> **引理 1**：設 $a(x) = x^n+c_{n-1}x^{n-1}+\cdots+c_1x+c_0$，$a(A)v = 0$（$v$ 在 $a(A)$ 的零空間裡），$\langle\langle v\rangle\rangle = \mathrm{span}\{v,Av,\dots,A^{n-1}v\}$。則 $\beta = \{v,Av,\dots,A^{n-1}v\}$ 是 $\langle\langle v\rangle\rangle$ 的基底，且 $L_A$ 在 $\beta$ 下的矩陣是**伴隨矩陣**
> $$C_{a(x)} = \begin{pmatrix}0&&&-c_0\\1&0&&-c_1\\&\ddots&\ddots&\vdots\\&&1&-c_{n-1}\end{pmatrix}.$$

- 這樣的多項式一定存在：$v,Av,A^2v,\dots$ 終究會線性相關，否則 $F^n$ 裡有無窮多個線性獨立向量（Math 321 用 $T$ 證過）[▶ 19:30](https://youtu.be/FeCKnYjPLjA?t=1170)。
- 老師把負號放在最後一欄（跟 D&F）。
- **證明** [▶ 23:00](https://youtu.be/FeCKnYjPLjA?t=1380)：$A\cdot A^jv = A^{j+1}v$，所以第 $j$ 欄是 $e_{j+1}$；最後 $A\cdot A^{n-1}v = A^nv = -c_0v-c_1Av-\cdots-c_{n-1}A^{n-1}v$，座標就是最後一欄。
- D&F 有從 Smith 標準形追蹤生成元、構造 $v$ 的方法，「我沒耐心教」；小例子直接算即可。

> **引理 2 / 有理標準形**：可以構造 $\beta_1,\dots,\beta_m$（每塊如引理 1），$\beta = \beta_1\cup\cdots\cup\beta_m$，則
> $$[A]_\beta = C_{a_1(x)}\oplus C_{a_2(x)}\oplus\cdots\oplus C_{a_m(x)}$$
> 叫 $A$ 的**有理標準形**（rational canonical form），記 $C_A$。它唯一（因為不變因子唯一）[▶ 28:30](https://youtu.be/FeCKnYjPLjA?t=1710)。

- $C_A = \beta^{-1}A\beta$：**$A$ 相似於它的有理標準形**。所以兩個矩陣相似 ⇔ 有理標準形相同（相似是等價關係）[▶ 30:00](https://youtu.be/FeCKnYjPLjA?t=1800)。
- 優點：**不需要**特徵多項式在 $F$ 上有根。

### 4. Jordan 形 [▶ 31:00](https://youtu.be/FeCKnYjPLjA?t=1860)

假設初等因子都形如 $(x-\lambda_j)^{n_j}$——特徵多項式在 $F$ 上**分裂**（乘成一次因式，可重複），即所有特徵值都在 $F$ 裡。

> **定理**：$v_1,\dots,v_k$ 滿足 $(A-\lambda I)v_1 = 0$、$(A-\lambda I)v_j = v_{j-1}$（$j = 2,\dots,k$）——一條特徵值 $\lambda$ 的 **$k$-鏈**（$k$-chain）。則 $L_A$ 在 $\beta = \{v_1,\dots,v_k\}$ 的生成空間上的矩陣是 **Jordan 塊**
> $$J_k(\lambda) = \begin{pmatrix}\lambda&1&&\\&\lambda&\ddots&\\&&\ddots&1\\&&&\lambda\end{pmatrix} = \lambda I_k+N_k.$$

- （學生：「為什麼用 $k$？」——「$k$ 很酷。」學生 K：「記住我的名字。」）
- 證明：$Av_1 = \lambda v_1$、$Av_j = \lambda v_j+v_{j-1}$，座標分別是 $\lambda e_1$、$\lambda e_j+e_{j-1}$ [▶ 36:30](https://youtu.be/FeCKnYjPLjA?t=2190)。
- $N_k = [0\,|\,e_1\,|\,e_2\,|\cdots|\,e_{k-1}]$。用欄乘法：$N_k^2 = [0\,|\,0\,|\,e_1\,|\cdots|\,e_{k-2}]$——零一直往右推（可歸納證明），$N_k^{k-1} = E_{1k}\ne0$、$N_k^k = 0$：$k$ 階**冪零矩陣**（「我喜歡的那個」）[▶ 38:30](https://youtu.be/FeCKnYjPLjA?t=2310)。

- **Jordan 形** = 每條鏈一個 Jordan 塊的直和；特徵值都在體裡時 $A$ 相似於它。但塊的**順序可以換**，不像有理標準形有整除條件鎖住順序 [▶ 53:30](https://youtu.be/FeCKnYjPLjA?t=3210)。
- 漂亮公式：$\det A$ = 特徵值乘積、$\mathrm{tr}A$ = 特徵值和（計重數）。**矩陣指數**透過相似變換到 Jordan 形就有公式——所以常係數一階線性微分方程組都能解 [▶ 54:30](https://youtu.be/FeCKnYjPLjA?t=3270)。

> 💬 學生：「我第二次考試大半沒寫，分數反而比較高。」老師：作業還有更多題，這週五貼出，一週後交；「作業不管多少題都是 100 分。」[▶ 42:30](https://youtu.be/FeCKnYjPLjA?t=2550)

### 5. 計算例子 [▶ 43:00](https://youtu.be/FeCKnYjPLjA?t=2580)

**§2 例子的有理標準形**：學生用電腦展開
$$a_3 = (x^3-2)^3(x^2+1) = x^{11}+x^9-6x^8-6x^6+12x^5+12x^3-8x^2-8,$$
$$a_2 = (x^3-2)^2(x^2+1) = x^8+x^6-4x^5-4x^3+4x^2+4.$$
- $A\sim C_{x^3-2}\oplus C_{a_2}\oplus C_{a_3}$：$3\times3$、$8\times8$、$11\times11$ 的伴隨矩陣，共 $22\times22$。老師在黑板上寫最後一欄時數不清位置（「數數好難」），學生唸係數幫忙 [▶ 45:30](https://youtu.be/FeCKnYjPLjA?t=2730)。
- Jordan 形呢？「陷阱題——沒有，因為在 $\mathbb{Q}$ 上不分裂。」

**簡單例子**（講義 E2，p.3）[▶ 50:30](https://youtu.be/FeCKnYjPLjA?t=3030)：講義寫「$\mathrm{char}_A(x) = (x-1)^2(x-1)$」，分兩種情況：
- **最小多項式沒有重根**：$m_A = (x-1)(x+1) = x^2-1 = a_2$，$a_1 = x-1$。有理標準形 $C_{x-1}\oplus C_{x^2-1} = (1)\oplus\begin{pmatrix}0&1\\1&0\end{pmatrix}$；初等因子 $x-1,\ x+1,\ x-1$；Jordan 形 $\mathrm{diag}(1,-1,1)$——可對角化。
- **最小多項式 = 特徵多項式**：只有一個不變因子 $a_1 = (x-1)^3 = x^3-3x^2+3x-1$，有理標準形 $C_{x^3-3x^2+3x-1} = \begin{pmatrix}0&0&1\\1&0&-3\\0&1&3\end{pmatrix}$。講義寫初等因子 $(x-1)^2,\ x-1$ 並給出 Jordan 形 $J_2(1)\oplus J_1(1)$。
- 講義還有一段用雙重下標列出不變因子中的質數冪（p.4；「我不推薦這種寫法」）[▶ 52:30](https://youtu.be/FeCKnYjPLjA?t=3150)。

> 💬 補充（非課堂內容）：講義這個例子的特徵多項式似乎有筆誤——第一種情況要 $\mathrm{char}_A = (x-1)^2(x+1)$；第二種情況若只有一個不變因子 $(x-1)^3$，初等因子應是 $(x-1)^3$、Jordan 形 $J_3(1)$；而 $J_2(1)\oplus J_1(1)$ 對應的是不變因子 $x-1,\ (x-1)^2$。

**$x^4+1$ 在三個體上** [▶ 55:00](https://youtu.be/FeCKnYjPLjA?t=3300)
- **$\mathbb{Q}$**：$x^4+1$ 不可約，唯一的不變因子就是它；有理標準形 = 一個 $4\times4$ 伴隨矩陣。沒有 Jordan 形（沒有有理根）。
- **$\mathbb{R}$**：沒有實根（沒有實數的四次方是 $-1$），分解成兩個不可約二次式。AI（ChatGPT 或 Gemini）說有理標準形是兩個 $2\times2$ 伴隨矩陣的直和——**錯**：那樣順序可以交換，就不唯一了。矩陣確實相似於它，但有理標準形仍是**同一個** $4\times4$ 伴隨矩陣（D&F 和老師另一本書都這樣）。「AI 有時會錯，或至少資訊不足。」[▶ 56:00](https://youtu.be/FeCKnYjPLjA?t=3360)
- **$\mathbb{C}$**：代數封閉，$x^4+1 = (x-\omega)(x-\omega^3)(x-\omega^5)(x-\omega^7)$，$\omega = e^{i\pi/4}$（$\omega^4 = e^{i\pi} = -1$）。仍只有一個不變因子；初等因子四個一次式，Jordan 形 $= \mathrm{diag}(\omega,\omega^3,\omega^5,\omega^7)$。

> 💬 老師說在 $\mathbb{C}$ 上「有理標準形和 Jordan 形相同」。補充（非課堂內容）：依本講的定義（不變因子伴隨矩陣的直和），$\mathbb{C}$ 上的有理標準形仍是 $x^4+1$ 的 $4\times4$ 伴隨矩陣（不變因子不隨擴大基礎體而改變），不是對角矩陣；用**初等因子**的伴隨矩陣組成的那種形式才會是對角的。老師說會出一題作業探討兩者何時相同。

（最後學生要求老師表演饒舌；「Avery 不在，要大家一起受苦才行」。）

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 伴隨矩陣 | companion matrix | §3 |
| 循環子空間 | cyclic subspace | §3 |
| 有理標準形 | rational canonical form | §3 |
| 相似 | similar | §3 |
| 分裂（多項式） | split | §4 |
| $k$-鏈 | $k$-chain | §4 |
| Jordan 塊 | Jordan block | §4 |
| 冪零矩陣 | nilpotent matrix | §4 |
| Jordan 形 | Jordan form | §4 |
| 矩陣指數 | matrix exponential | §4 |

## ⚠️ 待確認清單

（本集無）
