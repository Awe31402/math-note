---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 4
lecture: Lecture 4
date: 2023-01-23
video: https://youtu.be/ZdtLhKZcMeo （part 1）、https://youtu.be/4VEu9zSwcPs （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3，Definition 1.3.17–Example 1.3.32（書頁 14–18，PDF 頁 33–37）
---

# 第 4 集 · 開集、閉集、序列閉、緊緻：緊緻 ⟹ 閉且有界 [▶ 影片](https://youtu.be/ZdtLhKZcMeo)

← 上一集：[03-equivalent-norms](03-equivalent-norms.md) ｜ [總目錄](README.md) ｜ 下一集：[05-riesz-lemma-unit-ball](05-riesz-lemma-unit-ball.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 4 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 自動字幕 ＋ part 2 14:38 whisper 轉錄，時間點可能差 1–2 秒）＋ Debnath & Mikusiński §1.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 開集與閉集](#1-開集與閉集)
- [2. 例子](#2-例子)
- [3. 開集、閉集的運算](#3-開集閉集的運算)
- [4. 定理：閉 ⟺ 序列閉](#4-定理閉--序列閉)
- [5. 閉包與稠密](#5-閉包與稠密)
- [6. 緊緻與有界](#6-緊緻與有界)
- [7. 定理：緊緻 ⟹ 閉且有界](#7-定理緊緻--閉且有界)
- [8. 反例：C([0,1]) 的閉單位球不緊緻](#8-反例c01-的閉單位球不緊緻)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 開集、閉集 | Definition 1.3.17，p. 14 |
| 開球是開的、$C(\Omega)$ 中的開集與閉集 | Example 1.3.18–1.3.19，p. 15 |
| 聯集、交集 | Theorem 1.3.20，pp. 15–16 |
| 閉 ⟺ 序列閉 | Theorem 1.3.21，p. 16 |
| 閉包、稠密、Weierstrass 逼近定理 | Definition 1.3.22–Theorem 1.3.27，pp. 16–17 |
| 緊緻、有界 | Definition 1.3.28–1.3.30，p. 17 |
| 緊緻 ⟹ 閉且有界 | Theorem 1.3.31，pp. 17–18 |
| $C([0,1])$ 閉單位球不緊緻 | Example 1.3.32，p. 18 |

上一集：從範數定義了距離、開球、閉球、球面，證了有限維空間所有範數等價。[▶ 00:07](https://youtu.be/ZdtLhKZcMeo?t=7)

---

## 1. 開集與閉集

[▶ 00:42](https://youtu.be/ZdtLhKZcMeo?t=42) 課本 Definition 1.3.17。

**開集（open set）**：賦範空間 $E$ 的子集 $S$ 是開的，如果對每個 $x\in S$，存在 $\varepsilon>0$ 使

$$B(x,\varepsilon)=\{y\in E:\|y-x\|<\varepsilon\}\subseteq S.$$

白話：集合裡每一點周圍都能放一個小開球，整個在集合裡。

**閉集（closed set）**：補集 $E\setminus S$ 是開集。講者說他習慣寫 $E-S$。

【課本補充】等價的範數定義同樣的開集（雖然球的形狀不同）；閉集、稠密、緊緻等用開集定義的概念也一樣。

**度量不一定來自範數**【Q&A】[▶ 02:37](https://youtu.be/ZdtLhKZcMeo?t=157) 學生問這跟拓樸課的度量一樣嗎？講者：拓樸課的度量更一般；有些度量能由範數誘導，但不是全部。例如任意集合上的**離散度量**：兩點相同時距離 0，不同時距離 1。它誘導的是**離散拓樸**。

---

## 2. 例子

[▶ 03:44](https://youtu.be/ZdtLhKZcMeo?t=224)

**Example 1.3.18**（講者只敘述）：開球是開集；閉球和球面是閉集。

**Example 1.3.19**[▶ 04:27](https://youtu.be/ZdtLhKZcMeo?t=267)：$\Omega\subseteq\mathbb{R}^N$ 閉且有界，$C(\Omega)$ 用最大值範數。$f\in C(\Omega)$ 且 $f(x)>0$ 對所有 $x$。

| 開集 | 閉集 |
|---|---|
| $\{g:g(x)<f(x)\ \forall x\}$ | $\{g:g(x)\le f(x)\ \forall x\}$ |
| $\{g:g(x)>f(x)\ \forall x\}$ | $\{g:g(x)\ge f(x)\ \forall x\}$ |
| $\{g:|g(x)|<f(x)\ \forall x\}$ | $\{g:|g(x)|\le f(x)\ \forall x\}$ |
| $\{g:|g(x)|>f(x)\ \forall x\}$ | $\{g:|g(x)|\ge f(x)\ \forall x\}$ |
| | $\{g:g(x_0)=\lambda\}$（$x_0$ 固定，$\lambda\in\mathbb{C}$） |

講者的提醒【口頭】[▶ 05:38](https://youtu.be/ZdtLhKZcMeo?t=338)：寫不等式 $g(x)<f(x)$ 時 $g$ 必須是**實值**的（複數不能比大小）；有絕對值的那幾個才可以是複值。課本在同一個例子裡混用了兩種。

**直覺**【口頭】[▶ 08:28](https://youtu.be/ZdtLhKZcMeo?t=508)：用**等式**定義的集合通常是閉的，用**嚴格不等式**定義的通常是開的。但這個建議「有點危險」——例如 $\le$ 定義的也是閉的。

> 以下**不是逐字稿內容**，是一個開集的驗證示範：$U=\{g:g(x)<f(x)\ \forall x\}$。取 $g\in U$。$f-g$ 在緊緻集 $\Omega$ 上連續且處處 $>0$，所以有最小值 $\delta>0$。若 $\|h-g\|<\delta$，則 $h(x)<g(x)+\delta\le f(x)$，$h\in U$。所以 $B(g,\delta)\subseteq U$。（這裡要用 $\Omega$ 緊緻保證最小值取得到。）

---

## 3. 開集、閉集的運算

[▶ 08:28](https://youtu.be/ZdtLhKZcMeo?t=508) 課本 Theorem 1.3.20（證明是習題）。

- (a) 任意多個開集的聯集是開集。
- (b) **有限**多個開集的交集是開集。
- (c) **有限**多個閉集的聯集是閉集。
- (d) 任意多個閉集的交集是閉集。
- (e) 空集和整個空間既開又閉。

講者一開始寫錯，後來改正。[▶ 11:39](https://youtu.be/ZdtLhKZcMeo?t=699) 他順便「爆雷」拓樸課【口頭】：(a)(b)(e) 就是**拓樸**的標準定義；也可以用閉集當基本概念定義拓樸，那時是 (c)(d)(e)。用開集還是閉集當主角，決定了「任意」落在聯集還是交集上。

---

## 4. 定理：閉 ⟺ 序列閉

[▶ 13:24](https://youtu.be/ZdtLhKZcMeo?t=804) 課本 Theorem 1.3.21。講者說：從抽象的開球，回到「具體得多的分析」。

**定理**：$S\subseteq E$ 是閉集 ⟺ $S$ 中每個在 $E$ 中收斂的數列，極限都在 $S$ 裡：

$$x_1,x_2,\ldots\in S,\ x_n\to x\ \Longrightarrow\ x\in S.$$

白話：閉集就是「關得住極限」的集合。

### (⟹)

[▶ 14:37](https://youtu.be/ZdtLhKZcMeo?t=877)

設 $S$ 閉，$x_n\in S$，$x_n\to x$。反證：假設 $x\notin S$，即 $x\in E\setminus S$。

1. $E\setminus S$ 是開集，所以有 $\varepsilon>0$ 使 $B(x,\varepsilon)\subseteq E\setminus S$。
2. $\|x-x_n\|\to0$，所以 $n$ 夠大時 $\|x-x_n\|<\varepsilon$，即 $x_n\in B(x,\varepsilon)\subseteq E\setminus S$。
3. 但 $x_n\in S$，矛盾。所以 $x\in S$。

講者說畫圖有幫助：數列在 $S$ 裡收斂到外面的點 $x$，$x$ 周圍有一個在 $S$ 外的球，數列遲早要進那個球——直觀上矛盾。他一開始在紙上看不出來，後來想通：矛盾就是「$x_n$ 跑進了 $E\setminus S$」。[▶ 18:13](https://youtu.be/ZdtLhKZcMeo?t=1093)

### (⟸)

[▶ 20:04](https://youtu.be/ZdtLhKZcMeo?t=1204)

講者先想直接證（證補集是開的），取 $z\in E\setminus S$ 後就卡住了。所以照課本用反證。

設「極限都在 $S$ 裡」。假設 $S$ 不閉，即 $E\setminus S$ 不開。

1. 有一點 $x\in E\setminus S$，它周圍**每個**球 $B(x,\varepsilon)$ 都**不**整個在 $E\setminus S$ 裡，也就是每個球都含有 $S$ 的點。
2. 取 $\varepsilon=\frac1n$：每個 $n$ 選 $x_n\in S\cap B(x,\frac1n)$。
3. $\|x_n-x\|<\frac1n\to0$，所以 $x_n\to x$。
4. 由假設 $x\in S$，但 $x\in E\setminus S$，矛盾。∎

講者的觀察【口頭】[▶ 24:17](https://youtu.be/ZdtLhKZcMeo?t=1457)：這種建構式論證幾乎都取 $\varepsilon=\frac1n$，「我一再看到這個」。

講者說：這很重要，這就是用數列檢查一個集合是不是閉的。這種方法在一般拓樸空間不能用；這裡（賦範空間，甚至度量空間）能用，而且證明其實只用到「球」，沒用到範數的其他性質。[▶ 27:44](https://youtu.be/ZdtLhKZcMeo?t=1664)

【課本補充】課本說這個定理可以用來證 Example 1.3.19 的那些集合是閉的。

---

## 5. 閉包與稠密

[▶ 28:16](https://youtu.be/ZdtLhKZcMeo?t=1696) 課本 Definition 1.3.22–Theorem 1.3.27。

**閉包（closure）**：$\operatorname{cl}S$ = 所有包含 $S$ 的閉集的交集。由 Theorem 1.3.20(d)，它是閉集；它是包含 $S$ 的**最小**閉集。

**Theorem 1.3.23**（習題）：

$$\operatorname{cl}S=\{x\in E:\ \text{存在 } x_1,x_2,\ldots\in S \text{ 使 } x_n\to x\}.$$

講者說：「所有包含 $S$ 的閉集的交集」很難想像，但「$S$ 中數列所有可能的極限」就不那麼嚇人。他也說「這些習題證明真的幫我省了很多時間」。[▶ 30:17](https://youtu.be/ZdtLhKZcMeo?t=1817)

**Example 1.3.24（Weierstrass 逼近定理）**[▶ 30:54](https://youtu.be/ZdtLhKZcMeo?t=1854)：$[a,b]$ 上每個連續函數都能被多項式**一致**逼近：存在多項式 $p_n$ 使 $\|p_n-f\|=\max_{[a,b]}|p_n(t)-f(t)|\to0$。用今天的語言：

$$\operatorname{cl}P([a,b])=C([a,b]).$$

講者說這個定理技術性高、很有意思，可能是在應該證它的課裡沒被證的那種。

**稠密（dense）**：$S$ 在 $E$ 中稠密，如果 $\operatorname{cl}S=E$。

**例子**：

- 多項式在 $C([a,b])$ 中稠密（Example 1.3.26）。
- 只有有限多個非零項的複數列，在 $\ell^p$（$p\ge1$）中稠密（Example 1.3.26）。講者說可以把它們想成某種「多項式」，但他沒展開。[▶ 35:18](https://youtu.be/ZdtLhKZcMeo?t=2118)
- 【口頭】$\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密[▶ 37:19](https://youtu.be/ZdtLhKZcMeo?t=2239)：每個實數 $c$ 都是有理數列的極限。$c$ 是有理數就用常數數列；否則取小數展開的截斷 $c_n$（取前 $n$ 位），$c_n\to c$。講者說有人會覺得用小數展開當證明很濫用，「但就是這樣」。

> 以下**不是逐字稿內容**，是有限數列在 $\ell^p$ 稠密的一行理由：$z\in\ell^p$，令 $z^{(N)}=(z_1,\dots,z_N,0,0,\dots)$。則 $\|z-z^{(N)}\|_p^p=\sum_{n>N}|z_n|^p\to0$（收斂級數的尾巴）。

**Theorem 1.3.27**（習題）[▶ 39:40](https://youtu.be/ZdtLhKZcMeo?t=2380)：下面等價：

- (a) $S$ 在 $E$ 中稠密；
- (b) 對每個 $x\in E$，有 $x_n\in S$ 使 $x_n\to x$；
- (c) $E$ 的每個非空開集都含有 $S$ 的元素。

---

## 6. 緊緻與有界

[▶ 41:27](https://youtu.be/ZdtLhKZcMeo?t=2487) 課本 Definition 1.3.28–1.3.30。

**緊緻（compact）**：$S$ 是緊緻的，如果 $S$ 中每個數列都有收斂子數列，而且**極限在 $S$ 裡**。

講者說：這其實叫**序列緊緻（sequential compactness）**。拓樸的定義是「每個開覆蓋都有有限子覆蓋」；這本書用序列的版本。

**Example 1.3.29**：在 $\mathbb{R}^N$ 或 $\mathbb{C}^N$ 中，緊緻 ⟺ 閉且有界。講者說這比較像提醒，不是例子；這是 $\mathbb{R}^N$ 特有的。課本說對任何有限維賦範空間都成立，無限維就複雜了。

**有界（bounded）**[▶ 43:24](https://youtu.be/ZdtLhKZcMeo?t=2604)：$S\subseteq B(0,r)$ 對某個 $r>0$。講者說他平常不要求球心在原點，但邏輯上一樣：能用某個球包住，就能用夠大的、以原點為心的球包住。

**一個刻畫**[▶ 44:35](https://youtu.be/ZdtLhKZcMeo?t=2675)：課本說「容易證明」

$$S\text{ 有界}\iff\text{對任意 } x_n\in S \text{ 和任意純量 } \lambda_n\to0,\ \lambda_nx_n\to0.$$

【課堂討論】講者想證 (⟸)，試了 $\lambda_n=\frac1n$，沒成功。他說：這些書常常丟一句「顯然」，讓讀者覺得應該一眼看出來，但他覺得需要想一下。[▶ 48:32](https://youtu.be/ZdtLhKZcMeo?t=2912)

> 以下**不是逐字稿內容**，是補上的證明：
> - (⟹) $S\subseteq B(0,r)$，則 $\|\lambda_nx_n\|\le|\lambda_n|\,r\to0$。
> - (⟸) 反證：$S$ 無界，則對每個 $n$ 有 $x_n\in S$ 使 $\|x_n\|\ge n^2$。取 $\lambda_n=\frac1n\to0$，則 $\|\lambda_nx_n\|\ge n\not\to0$。（講者試的 $\lambda_n=\frac1n$ 是對的，關鍵是 $x_n$ 要選得比 $n$ 增長得更快。）

---

## 7. 定理：緊緻 ⟹ 閉且有界

[▶ 49:38](https://youtu.be/ZdtLhKZcMeo?t=2978) 課本 Theorem 1.3.31。講者強調：這個定理**不假設有限維**。

**定理**：賦範空間中，緊緻集是閉且有界的。

### 閉

[▶ 50:29](https://youtu.be/ZdtLhKZcMeo?t=3029)

$S$ 緊緻，$x_n\in S$，$x_n\to x$。要證 $x\in S$（序列閉，見第 4 節）。

1. 由緊緻，$(x_n)$ 有子數列 $x_{p_n}\to y\in S$。
2. 收斂數列的每個子數列都收斂到同一個極限，所以 $x_{p_n}\to x$。
3. 極限唯一，$x=y\in S$。∎

講者承認第 2 步有個缺口，但「希望實分析已經講清楚了」：收斂數列的子數列收斂到同一個極限。他說這個事實主要的用途是證明數列**不收斂**：找到兩個極限不同的子數列就行。「如果我們盡責，微積分 II 都該教這個」，但入門書不強調。[▶ 52:25](https://youtu.be/ZdtLhKZcMeo?t=3145)

**子數列的定義**[▶ 53:28](https://youtu.be/ZdtLhKZcMeo?t=3208)：存在嚴格遞增的函數 $p:\mathbb{N}\to\mathbb{N}$，子數列是 $x_{p(n)}=x_{p_n}$。例如只取偶數項。必須「往外走」，不能回頭取樣。

> 以下**不是逐字稿內容**，是第 2 步的證明：$p$ 嚴格遞增 ⟹ $p_n\ge n$（歸納）。給 $\varepsilon$，有 $N$ 使 $n\ge N$ 時 $\|x_n-x\|<\varepsilon$；則 $n\ge N$ 時 $p_n\ge N$，$\|x_{p_n}-x\|<\varepsilon$。

### 有界

[▶ 54:35](https://youtu.be/ZdtLhKZcMeo?t=3275)

反證：$S$ 無界，則有 $x_n\in S$ 使 $\|x_n\|\ge n$ 對所有 $n$。課本說「顯然」$(x_n)$ 沒有收斂子數列，所以 $S$ 不緊緻。

> 以下**不是逐字稿內容**，是「顯然」的理由：任何子數列 $x_{p_n}$ 滿足 $\|x_{p_n}\|\ge p_n\ge n\to\infty$，無界；而收斂數列有界（第 3 集），所以子數列不收斂。

講者說這兩個證明對他來說比課本說「顯然」的那個（有界的刻畫）還容易，「也許只是因為這兩個我看得出來」。[▶ 56:12](https://youtu.be/ZdtLhKZcMeo?t=3372)

---

## 8. 反例：C([0,1]) 的閉單位球不緊緻

[▶ 56:42](https://youtu.be/ZdtLhKZcMeo?t=3402) 課本 Example 1.3.32。

**主張**：$C([0,1])$（最大值範數）的閉單位球 $\overline B(0,1)$ 閉且有界，但**不緊緻**。課本的理由：$x_n(t)=t^n$ 都在 $\overline B(0,1)$ 裡，而「顯然」沒有子數列在 $C([0,1])$ 中收斂。

講者說：「我承認我不懂這個例子。」問題就在「顯然」那裡。

**課堂上確認的部分**：

- **有界**：$\overline B(0,1)\subseteq B(0,2)$，顯然有界。[▶ 59:06](https://youtu.be/ZdtLhKZcMeo?t=3546)
- **閉**：它是閉包（閉球），閉包是閉的（作業題）。
- **$x_n$ 連續**：$t,t^2,t^3,\dots$ 都是連續函數。講者畫了 $n=1,2,3$ 的圖。[▶ part 2 00:00](https://youtu.be/4VEu9zSwcPs?t=0)
- **$x_n\in\overline B(0,1)$**【課堂討論】[▶ part 2 04:32](https://youtu.be/4VEu9zSwcPs?t=272)：講者一度以為 $x_n(1)=1$ 會讓它不在球裡，學生提醒閉球是 $\le1$——「那個橫槓很重要」。

**卡住的地方**[▶ part 2 06:04](https://youtu.be/4VEu9zSwcPs?t=364)：學生指出逐點極限：$t<1$ 時 $t^n\to0$，$t=1$ 時 $t^n=1$。所以 $x_n$ **逐點**收斂到一個**不連續**的函數（$[0,1)$ 上是 0，$t=1$ 是 1）。講者說：但我們用的不是逐點收斂，是一致範數下的收斂；如果極限 $x^*$ 存在，它必須在 $C([0,1])$ 裡、是連續函數，而 $\max_t|t^n-x^*(t)|\to0$。他想不出 $x^*$ 是什麼，就停在這裡，說會在下堂課前想清楚。

【Q&A】[▶ part 2 12:21](https://youtu.be/4VEu9zSwcPs?t=741) 學生說：如果取 $x^*=0$（零函數），$\max_t|t^n-0|=1$ 永遠不趨近 0；所以不會一致收斂到 0。講者同意，並聯想到上次的結論：沒有範數能描述逐點收斂。

> 以下**不是逐字稿內容**，是補上課本「顯然」的兩種理由：
>
> **理由 1（逐點極限）**：假設子數列 $x_{p_n}\to x^*$ 在一致範數下收斂。一致收斂推出逐點收斂（每點 $|x_{p_n}(t)-x^*(t)|\le\|x_{p_n}-x^*\|$）。所以 $x^*(t)=\lim t^{p_n}$，即 $x^*=0$ 在 $[0,1)$、$x^*(1)=1$。這個函數不連續，不在 $C([0,1])$ 裡，矛盾。所以這正是學生找到的那個逐點極限造成的矛盾：極限「應該」是它，但它不在空間裡。
>
> **理由 2（不是 Cauchy）**：設 $n\ge2m$。在 $[0,1]$ 上 $t^n\le t^{2m}$，所以
> $$\|x_m-x_n\|=\max_t(t^m-t^n)\ge\max_t(t^m-t^{2m})=\max_{s\in[0,1]}(s-s^2)=\tfrac14\quad(s=t^m).$$
> 任何子數列裡，對每個 $p_m$ 都能找到 $p_n\ge2p_m$，兩項距離 $\ge\frac14$，所以子數列不是 Cauchy，不收斂。

**講者的總結**[▶ part 2 09:44](https://youtu.be/4VEu9zSwcPs?t=584)：這是無限維空間中「閉且有界但不緊緻」的標準例子。緊緻 ⟹ 閉且有界在所有賦範空間都成立；反方向在無限維一般不成立。下一集講 **Riesz 引理**和 Theorem 1.3.34：賦範空間有限維 ⟺ 閉單位球緊緻。證明會用到上一集證範數等價的同一套技術。

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 開集 | 每點有 $B(x,\varepsilon)\subseteq S$ | |
| 閉集 | 補集是開集 | |
| 運算 | 任意聯集開、有限交集開；有限聯集閉、任意交集閉 | 拓樸的公理 |
| 閉 ⟺ 序列閉 | $x_n\in S$, $x_n\to x\Rightarrow x\in S$ | ⟹ $x$ 外的球吞掉數列；⟸ 取 $x_n\in S\cap B(x,\frac1n)$ |
| 閉包 | $\operatorname{cl}S$ = 含 $S$ 的閉集之交 = $S$ 中數列極限的集合 | |
| 稠密 | $\operatorname{cl}S=E$ | 多項式在 $C([a,b])$（Weierstrass）；有限數列在 $\ell^p$；$\mathbb{Q}$ 在 $\mathbb{R}$ |
| 緊緻 | 每個數列有收斂子數列、極限在 $S$ | 序列緊緻 |
| 有界 | $S\subseteq B(0,r)$ ⟺ $\lambda_n\to0\Rightarrow\lambda_nx_n\to0$ | ⟸ 選 $\|x_n\|\ge n^2$、$\lambda_n=\frac1n$ |
| 緊緻 ⟹ 閉 | | 子數列極限 = 原數列極限 |
| 緊緻 ⟹ 有界 | | $\|x_n\|\ge n$ 的數列無收斂子數列 |
| 反例 | $C([0,1])$ 的 $\overline B(0,1)$，$x_n=t^n$ | 逐點極限不連續；或 $\|x_n-x_{2n}\|=\frac14$ |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 閉 ⟺ 序列閉 | 第 5 集（Riesz 引理中 $d>0$）、第 6 集（閉子空間是 Banach） |
| 有限維 ⟺ 單位球緊緻 | 第 5 集（Riesz 引理） |
| 閉包、稠密 | 第 6 集（完備化：$\Phi(E)$ 稠密）、第 8 集（稠密子空間上延拓）、第 23 集（可分 Hilbert 空間） |
| 子數列的極限 | 第 6 集（Cauchy + 收斂子數列 ⟹ 收斂） |

---

## 附：本集一句話總結

> **閉集就是「關得住極限」的集合，閉包就是「所有極限」；在賦範空間裡，緊緻一定閉且有界，但反過來只在有限維成立——$C([0,1])$ 中的 $t^n$ 全在閉單位球裡，逐點極限卻是不連續函數，所以沒有任何子數列能在一致範數下收斂。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-01-23 錄影逐字稿（part 1 YouTube 自動字幕 59:51；part 2 whisper large-v3-turbo 轉錄 14:38）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §1.3 整理。*
