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

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 39 集，Lecture 33
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ 手寫講義 `Math422_Lecture33_RCF_Jordan.pdf`（8 頁），依 Dummit & Foote §12.2–12.3。前 40 分鐘黑板，後面投影。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：這堂課錄影斷成兩段，後段（紐結的 $\mathbb{Z}$-模）在 [[38-紐結群計算]]。

---

## 目錄

- [0. 開場：兩個方向看同一件事](#0-開場兩個方向看同一件事)
- [1. 不變因子 → 初等因子](#1-不變因子--初等因子)
- [2. 例：ℚ 上的不變因子與初等因子](#2-例ℚ-上的不變因子與初等因子)
- [3. 循環子空間 ⇒ 伴隨矩陣](#3-循環子空間--伴隨矩陣)
- [4. 有理標準形](#4-有理標準形)
- [5. k-鏈 ⇒ Jordan 塊；冪零矩陣 N_k](#5-k-鏈--jordan-塊冪零矩陣-n_k)
- [6. 一個 22×22 的有理標準形](#6-一個-2222-的有理標準形)
- [7. 例：特徵多項式 (x−1)²(x+1)；Jordan 形](#7-例特徵多項式-x1²x1jordan-形)
- [8. 例：x⁴ + 1 在 ℚ、ℝ、ℂ 上](#8-例x⁴--1-在-ℚℝℂ-上)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 開場：兩個方向看同一件事

[▶ 00:00](https://youtu.be/FeCKnYjPLjA?t=0)（學生：「$f'$ 的 **Laplace 變換**。」「$f'$ 的 Laplace 變換**跟這無關**。開始吧。」）課前禱告：「幫助我們多懂一點**有理標準形**和 **Jordan 形**。」

[▶ 00:30](https://youtu.be/FeCKnYjPLjA?t=30)「Lecture 33，大致是 **PID 上模的例子**。主要聚焦：描述 $F$ 上 $n\times n$ 矩陣 $A$ 給的 $F[x]$-模。」（講義 p.1）$f(x)v = f(A)v$；上次的 Smith 形對 $xI-A$ 做 $F[x]$ 上的列＋行運算，得到**唯一**的不變因子 $a_1(x)\mid a_2(x)\mid\cdots\mid a_m(x)$。

【口頭】[▶ 03:00](https://youtu.be/FeCKnYjPLjA?t=180)「兩種看法：一是**我們已經會線代**，用線代理解抽象代數；另一是證明 PID 上有限生成模的一般分類定理，那其實就**證明了**線代裡我**從沒證過**的結果——例如 **Jordan 基底的存在**，在適當的詮釋下由 §12.1 Thm 6 推出。」
- **$m_A(x) = a_m(x)$**（最後一個不變因子）；**$\mathrm{char}_A(x) = a_1(x)\cdots a_m(x)$**——「整除條件**限制很大**」。
- 【講義補充】講義 p.1：Math 321 學過 $m_A$ 和 $\mathrm{char}_A$ 有相同的根，且 $\mathrm{char}_A(A) = 0$（**Cayley–Hamilton**）；$\mathrm{char}_A$ 也是初等因子的乘積。

---

## 1. 不變因子 → 初等因子

[▶ 04:30](https://youtu.be/FeCKnYjPLjA?t=270)「不變因子**不必是質的**——不能是單位、要非零，但不必是質元。不過我們在 PID 上，PID 自動是 UFD，所以不變因子有**質數冪分解**。」那些**質數冪**就是**初等因子**。

【講義補充】講義 p.4 的系統寫法：$a_m(x) = p_1^{r_1^m}\cdots p_s^{r_s^m}$，$a_{m-1} = p_1^{r_1^{m-1}}\cdots$……，$a_1 = p_1^{r_1^1}\cdots$，其中 $r_j^m\ge r_j^{m-1}\ge\cdots\ge r_j^1\ge0$。初等因子就是那些 $r_j^k\neq0$ 的 $p_j^{r_j^k}$。（老師在課上說：「這是一個**陰險而有點可怕**的嘗試，用醜的雙下標列舉——**我不推薦**。」）

---

## 2. 例：ℚ 上的不變因子與初等因子

**例 1**（老師現場編、不在講義）[▶ 06:00](https://youtu.be/FeCKnYjPLjA?t=360)「注意例子的**顏色**。」在 $\mathbb{Q}$ 上：
$$a_3 = (x^3-2)^3(x^2+1),\quad a_2 = (x^3-2)^2(x^2+1),\quad a_1 = x^3-2.$$

【Q&A】[▶ 08:00](https://youtu.be/FeCKnYjPLjA?t=480) 學生：「為什麼 $a_2$ 沒有 $(x^3-2)^3$？等等，我以為它是**唯一**的。」老師：「給一組不變因子，有理標準形是唯一的。但**給定 $a_m$**，往下**降**的方式有很多種——例如另一組：$a_2 = (x^3-2)^3(x^2+1)$、$a_1 = (x^3-2)^3(x^2+1)$……」
- 學生：「你想讓它們有**相同的特徵多項式**。」「好，可以。$(x^3-2)$ 共 6 個、$(x^2+1)$ 共 2 個……**最大的可以等於次大的**，這是允許的。」兩組的乘積相同 ⇒ **特徵多項式相同、但是不同的情形**。
- 學生：「那昨天我問的『唯一嗎』？」「我可能對你**以為**你在問的問題肯定地回答了，也可能我當時沒懂答錯了。」學生：「對特定的**矩陣**，它唯一嗎？」「**是**——給定矩陣，Smith 形唯一。**對給定的基體**；換脈絡就可能變。」

**初等因子**[▶ 12:30](https://youtu.be/FeCKnYjPLjA?t=750)：
- 第一組：$x^3-2;\ (x^3-2)^2,\ x^2+1;\ (x^3-2)^3,\ x^2+1$。（學生：「你忘了**立方**。」「謝謝。」）
- 第二組：$(x^3-2)^3,\ x^2+1,\ (x^3-2)^3,\ x^2+1$。
- 「初等因子的乘積還是特徵多項式，而且它們**是不變因子的因式分解**。」

（講義 p.2、p.4）基本定理兩種形式：
$$F^n\cong\frac{F[x]}{(a_1)}\oplus\cdots\oplus\frac{F[x]}{(a_m)}\qquad(\text{Thm 5}),\qquad F^n\cong\frac{F[x]}{(d_1)}\oplus\cdots\oplus\frac{F[x]}{(d_s)}\qquad(\text{Thm 6}).$$
「我要說明：**Thm 5 給出有理標準形**，**Thm 6**（在適當脈絡下）**給出 Jordan 形**。本質上要懂怎麼替每個小塊**造基底**。」

---

## 3. 循環子空間 ⇒ 伴隨矩陣

（「**Lemma** 押韻的是什麼？」「**Dilemma**。」「Emma。」「誰是 Emma？」「**我的名字**。」）

> **定理**（講義 p.2）[▶ 17:30](https://youtu.be/FeCKnYjPLjA?t=1050)　$\langle\!\langle v\rangle\!\rangle = \mathrm{span}_F\{v,Av,\dots,A^{n-1}v\}$，$a(x) = x^n+c_{n-1}x^{n-1}+\cdots+c_1x+c_0$，$a(A)v = 0$。則 $\beta = \{v,Av,\dots,A^{n-1}v\}$ 是 $\langle\!\langle v\rangle\!\rangle$ 的基底，$L_A$ 在 $\beta$ 下的矩陣是**伴隨矩陣**
> $$C_{a(x)} = \begin{pmatrix}0&0&\cdots&0&-c_0\\1&0&\cdots&0&-c_1\\0&1&\cdots&0&-c_2\\\vdots&&\ddots&&\vdots\\0&0&\cdots&1&-c_{n-1}\end{pmatrix}.$$

- 【口頭】[▶ 19:30](https://youtu.be/FeCKnYjPLjA?t=1170)「這樣的多項式**一定存在**（$v\neq0$）：一直乘 $A$，最後一定線性相關——否則 $F^n$ 裡就有**無窮**個線性獨立向量，那很難做到。Math 321 用 $T$ 證過。」
- 【口頭】「（負號放這裡）——我**修好了**，這是 D&F 的寫法。」（老師把 $\langle\!\langle\ \rangle\!\rangle$ 叫「langle langle wrangle wrangle」，學生：「你**自己剛定義**的記號。」）

**證明**[▶ 23:30](https://youtu.be/FeCKnYjPLjA?t=1410)：第 $j$ 個基底向量是 $A^{j-1}v$，$A(A^{j-1}v) = A^jv$ = 第 $j+1$ 個 ⇒ 座標 $e_{j+1}$（次對角線的 1）。最後一個 $A(A^{n-1}v) = A^nv = -c_0v-c_1Av-\cdots-c_{n-1}A^{n-1}v$（因為 $a(A)v = 0$）⇒ 最後一欄 $-c_0,\dots,-c_{n-1}$。
- 【口頭】[▶ 25:30](https://youtu.be/FeCKnYjPLjA?t=1530)「D&F 有方法：用 Smith 形時**追蹤生成元**來造 $v$。我**沒耐心**教——小例子可以**臨時**直接算出有理標準形，不需要反推 Smith 形。」

---

## 4. 有理標準形

> **定理**（講義 p.3）[▶ 27:30](https://youtu.be/FeCKnYjPLjA?t=1650)　對每個不變因子 $a_j$ 取循環子空間的基底 $\beta_j$，令 $\beta = \beta_1\cup\cdots\cup\beta_m$，則
> $$[L_A]_{\beta,\beta} = C_{a_1(x)}\oplus C_{a_2(x)}\oplus\cdots\oplus C_{a_m(x)}$$
> ——$A$ 的**有理標準形**。

- （學生：「那應該是 $m$。」「對，$m$ 是不變因子的個數。」）
- **唯一**：不變因子唯一 ⇒ 伴隨矩陣唯一。$C_A = \beta^{-1}A\beta$ ⇒ **$A$ 相似於它的有理標準形**。
- 【口頭】[▶ 30:00](https://youtu.be/FeCKnYjPLjA?t=1800)「要檢查兩個矩陣**相似**嗎？算它們的有理標準形；一樣就相似，不一樣就不相似（相似是等價關係）。有理標準形的好處：**不依賴**基體裡有沒有多項式的根。」

【講義補充】講義 p.3 一段被劃掉的話：「oops！我假設了 $a_i$ 不可約」——有理標準形用的就是不變因子本身，不需要它們不可約。講義 p.3 Remark：§12.2 描述了在算 Smith 形時順便造出 $\beta$ 的方法，「我大概不會做到複雜到值得那樣算的題目」。

---

## 5. k-鏈 ⇒ Jordan 塊；冪零矩陣 N_k

[▶ 31:00](https://youtu.be/FeCKnYjPLjA?t=1860)（講義 p.4–5）現在假設初等因子 $d_j(x) = (x-\lambda_j)^{n_j}$——特徵多項式在 $F$ 上**分裂**（乘積是一次因式、可重複），也就是所有特徵值都在 $F$ 裡。

> **定理**（講義 p.5）[▶ 32:00](https://youtu.be/FeCKnYjPLjA?t=1920)　$v_1,\dots,v_k$ 滿足
> $$(A-\lambda I)v_1 = 0,\qquad(A-\lambda I)v_j = v_{j-1}\ (j = 2,\dots,k),$$
> 即 $\beta = \{v_1,\dots,v_k\}$ 是 $A$ 的特徵值 $\lambda$ 的 **$k$-鏈**。則 $L_A$ 限制在 $\mathrm{span}(\beta)$ 上的矩陣是 $k\times k$ **Jordan 塊**
> $$J_k(\lambda) = \lambda I_k+N_k.$$

（「為什麼是 $k$？」學生：「**學我的名字**。」「她說我有好幾堂沒點名了。」）

> **定義**（講義 p.5）[▶ 36:00](https://youtu.be/FeCKnYjPLjA?t=2160)　$N_k = [0\mid e_1\mid e_2\mid\cdots\mid e_{k-1}]$。

**計算**：$Av_1 = \lambda v_1$、$Av_2 = \lambda v_2+v_1$、……、$Av_k = \lambda v_k+v_{k-1}$ ⇒ 座標 $\lambda e_1$、$\lambda e_2+e_1$、……、$\lambda e_k+e_{k-1}$ ⇒ $\lambda I_k+[0\mid e_1\mid\cdots\mid e_{k-1}]$。

**$N_k$ 冪零**[▶ 38:30](https://youtu.be/FeCKnYjPLjA?t=2310)：用逐欄規則
$$N_k^2 = [0\mid Ne_1\mid Ne_2\mid\cdots\mid Ne_{k-1}] = [0\mid0\mid e_1\mid\cdots\mid e_{k-2}],$$
每乘一次 0 就往右推一格（可以歸納），$N_k^{k-1} = E_{1,k}$ 非零、$N_k^k = 0$——「**$k$ 階冪零矩陣**，這是**我喜歡的那個**。」

【講義補充】（講義 p.6）
- 把所有 $n_j$-鏈接起來：$[L_A]_{\beta,\beta} = J_{n_1}(\lambda_1)\oplus\cdots\oplus J_{n_s}(\lambda_s) = J_A$——**Jordan 形**。
- $[\beta]^{-1}A[\beta] = J_A$ ⇒ $\det A = \lambda_1^{n_1}\cdots\lambda_s^{n_s}$、$\mathrm{tr}A = n_1\lambda_1+\cdots+n_s\lambda_s$。
- $\dot x = Ax$ 的通解 $x = e^{tA}c$，$e^{tA} = [\beta]e^{tJ_A}[\beta]^{-1}$，而 $e^{tJ_A}$ **很好算**。

【口頭】[▶ 53:30](https://youtu.be/FeCKnYjPLjA?t=3210)「Jordan 形**沒有**整除條件撐住唯一性——**可以重排塊**。但有超酷的公式：行列式是特徵值之積、跡是特徵值之和（**計重數**）。還有**任何常係數一階微分方程**都能用矩陣指數解：矩陣指數相似變換到 Jordan 形的矩陣指數，那有**神奇的**好公式。」

---

## 6. 一個 22×22 的有理標準形

[▶ 42:00](https://youtu.be/FeCKnYjPLjA?t=2520)「在進入投影之前，試著寫下 §2 例子的有理標準形和 Jordan 形——講義沒有。……可能要花一陣子，我該**當作業**。」學生：「真的要出成作業？」「**一定會**。今天會貼更多題目——我昨天花了**好幾個小時**出題。」學生：「作業不管幾題都是 100 分。」「你們**都對**，但題目會變多。」

學生用電腦幫忙展開[▶ 43:30](https://youtu.be/FeCKnYjPLjA?t=2610)：
$$a_3 = (x^3-2)^3(x^2+1) = x^{11}+x^9-6x^8-6x^6+12x^5+12x^3-8x^2-8,$$
$$a_2 = (x^3-2)^2(x^2+1) = x^8+x^6-4x^5-4x^3+4x^2+4,\qquad a_1 = x^3-2.$$
有理標準形 $C_{a_1}\oplus C_{a_2}\oplus C_{a_3}$：$3\times3$、$8\times8$、$11\times11$ 三塊（總共 22 = 特徵多項式的次數 $3\cdot6+2\cdot2$）。$C_{a_1}$：次對角 1、最後一欄 $(2,0,0)$。（老師在黑板上填 8×8 和 11×11 的最後一欄，數錯好幾次：「**數數好難**。」學生念、老師寫。「你**好勇敢**。」）

【課堂討論】[▶ 50:00](https://youtu.be/FeCKnYjPLjA?t=3000)「Jordan 形呢？」「**陷阱題**：**沒有** Jordan 形——在有理數上**不分裂**。」

---

## 7. 例：特徵多項式 (x−1)²(x+1)；Jordan 形

**例**（講義 p.1、p.3）[▶ 50:30](https://youtu.be/FeCKnYjPLjA?t=3030)（「我寫講義時想到的**比較簡單**的例子」）：$\mathrm{char}_A = (x-1)^2(x+1)$。最小多項式只有兩種可能：
- **(I)** $m_A = (x-1)(x+1)$——**分裂、無重根** ⇒ 可對角化。不變因子 $a_1 = x-1$、$a_2 = x^2-1$；初等因子 $x-1,x-1,x+1$。
$$\text{RCF} = [1]\oplus C_{x^2-1} = [1]\oplus\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad\text{Jordan} = \mathrm{diag}(1,-1,1).$$
- **(II)** $m_A = (x-1)^2(x+1) = \mathrm{char}_A$——只有**一個**不變因子。初等因子 $(x-1)^2$、$x+1$ ⇒ Jordan 形 $J_2(1)\oplus J_1(-1)$；有理標準形是 $C_{(x-1)^2(x+1)} = C_{x^3-x^2-x+1}$。

💬 講義 p.3 的 E2 把特徵多項式寫成 $(x-1)^2(x-1)$，左半邊又用 $(x-1)^3$ 的伴隨矩陣 $C_{x^3-3x^2+3x-1}$ 和 $J_2(1)\oplus J_1(1)$，右半邊卻用 $(x-1)(x+1)$——兩個特徵多項式**混在一起**了。上面依 p.1 的 E1（$\mathrm{char} = (x-1)^2(x+1)$）整理。

---

## 8. 例：x⁴ + 1 在 ℚ、ℝ、ℂ 上

**E3**（講義 p.7–8）[▶ 54:30](https://youtu.be/FeCKnYjPLjA?t=3270)「我問了個**不愉快**的問題：$\mathrm{char}_A = x^4+1$，在 $\mathbb{Q}$、$\mathbb{R}$、$\mathbb{C}$ 上的有理標準形？這讓我理解了**現在 AI 處理這問題的某些怪癖**——**小心**，AI 有時是錯的，或至少**資訊不足**。」

- **$\mathbb{Q}$**：$x^4+1$ 在 $\mathbb{Q}$ 上不可約 ⇒ 唯一的不變因子是它自己 ⇒
$$A\sim C_{x^4+1} = \begin{pmatrix}0&0&0&-1\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}.$$
  **沒有** Jordan 形——不分裂。
- **$\mathbb{R}$**：$x^4+1 = (x^2+\sqrt2x+1)(x^2-\sqrt2x+1)$，沒有實根（「沒有實數的 4 次方是 $-1$」）。[▶ 56:00](https://youtu.be/FeCKnYjPLjA?t=3360)「Gemini 或 ChatGPT 其中一個**浪費我的時間**：說有理標準形是 $C_{x^2+\sqrt2x+1}\oplus C_{x^2-\sqrt2x+1}$。我想——我們說過有理標準形**唯一**，但那個你可以把兩塊**對調**——那就**不唯一**了？我查了 D&F、查了另一本書，**都沒有**。是 Gemini 在浪費我的時間。這樣做**可以**（矩陣確實相似於它），但那**不是**有理標準形。在 $\mathbb{R}$ 上有理標準形**仍然**是那個 $4\times4$ 伴隨矩陣。」（講義 p.7 把那個直和**劃掉**：「我們可以這樣做，但那不是有理標準形。」）「我留著劃掉的版本，因為知道**不用聽 chat 的**有幫助。」
- **$\mathbb{C}$**[▶ 57:00](https://youtu.be/FeCKnYjPLjA?t=3420)：代數封閉，$\omega = e^{i\pi/4}$，$\omega^4 = e^{i\pi} = -1$：
$$x^4+1 = (x-\omega)(x-\omega^3)(x-\omega^5)(x-\omega^7).$$
  初等因子 $x-\omega,\ x-\omega^3,\ x-\omega^5,\ x-\omega^7$ ⇒ **Jordan 形**
$$A\sim J_1(\omega)\oplus J_1(\omega^3)\oplus J_1(\omega^5)\oplus J_1(\omega^7) = \mathrm{diag}(\omega,\omega^3,\omega^5,\omega^7).$$
  老師（和講義 p.8）說「在這個脈絡下有理標準形和 Jordan 形**相同**」，並說會出一題作業探討兩者何時相同。

💬 依老師自己在 $\mathbb{R}$ 那段的邏輯，$\mathbb{C}$ 上**不變因子仍只有一個** $x^4+1$（不變因子由 $xI-A$ 的 Smith 形決定，擴大體不會改變），所以 $\mathbb{C}$ 上的有理標準形**仍是** $C_{x^4+1}$；對角矩陣 $\mathrm{diag}(\omega,\omega^3,\omega^5,\omega^7)$ 是 **Jordan 形**（初等因子形式），兩者相似但**不是同一個矩陣**。有理標準形和 Jordan 形真正一致的情形，例如 $A = \lambda I$（不變因子全是 $x-\lambda$）。

[▶ 59:00](https://youtu.be/FeCKnYjPLjA?t=3540)（學生：「是你要**饒舌**嗎？」「我覺得 Avery 也該在場**受苦**。」「如果我錄下來，他們可以**關掉**逃走。」「那就不一樣了。」）→ 後段在 [[38-紐結群計算]]。

---

## 9. 一頁速查表

| 概念 | 內容 |
|---|---|
| $m_A$；$\mathrm{char}_A$ | $a_m$；$\prod a_i = \prod d_j$ |
| 初等因子 | 不變因子的質數冪因式 |
| 伴隨矩陣 $C_{a(x)}$ | 循環基底 $v,Av,\dots,A^{n-1}v$；最後一欄 $-c_i$ |
| **有理標準形** | $C_{a_1}\oplus\cdots\oplus C_{a_m}$，唯一，不需特徵值 |
| $k$-鏈 | $(A-\lambda)v_1 = 0$、$(A-\lambda)v_j = v_{j-1}$ |
| **Jordan 塊** | $J_k(\lambda) = \lambda I_k+N_k$，$N_k = [0\mid e_1\mid\cdots\mid e_{k-1}]$ |
| $N_k$ | $N_k^{k-1} = E_{1,k}$，$N_k^k = 0$ |
| Jordan 形 | $\bigoplus J_{n_j}(\lambda_j)$，需要分裂；塊可重排 |
| $\det$、$\mathrm{tr}$ | 特徵值之積、之和（計重數） |
| $x^4+1$ | $\mathbb{Q},\mathbb{R}$：RCF $= C_{x^4+1}$，無 Jordan；$\mathbb{C}$：Jordan $= \mathrm{diag}(\omega,\omega^3,\omega^5,\omega^7)$ |

| 中文 | English |
|---|---|
| 有理標準形 | rational canonical form (RCF) |
| 伴隨矩陣 | companion matrix |
| 循環子空間 | cyclic subspace |
| $k$-鏈 | $k$-chain |
| Jordan 塊；Jordan 形 | Jordan block; Jordan form |
| 冪零矩陣 | nilpotent matrix |
| 矩陣指數 | matrix exponential |
| 相似 | similar |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **同一堂課的後段：紐結** | [[38-紐結群計算]] |
| **實結合代數、正則表示** | [[40-L34-實結合代數的正則表示]] |
| **矩陣指數、$\mathcal{A}$-微積分** | [[41-A可微性與A微積分-下]]、[[42-A可微性與A微積分-上]] |
| **Boss Fight 3 複習** | [[43-複習-BossFight3-下]]、[[44-複習-BossFight3-上]] |

---

## 附：本集一句話總結

> **$F[x]$-模 $F^n$ 的不變因子 $a_1\mid\cdots\mid a_m$ 由 Smith 形唯一決定（$a_m$ 是最小多項式、乘積是特徵多項式），拆成質數冪就是初等因子；每個循環子空間 $\mathrm{span}\{v,Av,\dots\}$ 在那組基底下是伴隨矩陣，所以 $A$ 相似於唯一的有理標準形 $\bigoplus C_{a_i}$（不需要特徵值，可以判斷相似）；當特徵值都在 $F$ 裡，每個 $k$-鏈給一個 Jordan 塊 $\lambda I+N_k$，拼成 Jordan 形；例子包括 $\mathbb{Q}$ 上一個 22×22 的有理標準形、$(x-1)^2(x+1)$ 的兩種情形，以及 $x^4+1$ 在 $\mathbb{Q}$、$\mathbb{R}$、$\mathbb{C}$ 上的對比——順便提醒 AI 會把有理標準形講錯。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 33 錄影逐字稿前段（YouTube 自動字幕，59:51）與手寫講義 `Math422_Lecture33_RCF_Jordan.pdf`（依 Dummit & Foote §12.2–12.3）整理。*
