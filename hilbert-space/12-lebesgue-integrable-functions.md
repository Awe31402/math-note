---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 12
lecture: Lecture 12
date: 2023-02-10
video: https://youtu.be/b7EvaW-mjrA （part 1）、https://youtu.be/MP169hGYA7E （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.3（書頁 45–48，PDF 頁 64–67）
---

# 第 12 集 · Lebesgue 可積函數：積分與表示無關、L¹(ℝ) [▶ 影片](https://youtu.be/b7EvaW-mjrA)

← 上一集：[11-lebesgue-step-functions](11-lebesgue-step-functions.md) ｜ [總目錄](README.md) ｜ 下一集：[13-absolute-value-series](13-absolute-value-series.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 12 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 33:26 ＋ part 2 20:10，自動字幕）＋ Debnath & Mikusiński §2.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習定義](#1-複習定義)
- [2. Lemma 2.3.2：非負函數的積分非負](#2-lemma-232非負函數的積分非負)
- [3. Corollary 2.3.3：積分與表示無關](#3-corollary-233積分與表示無關)
- [4. L¹(ℝ) 是向量空間，積分是線性泛函](#4-l¹ℝ-是向量空間積分是線性泛函)
- [5. 級數在哪裡發散？零集的第一次出現](#5-級數在哪裡發散零集的第一次出現)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $f\simeq\sum f_n$、$f\ge0$ ⟹ $\sum\int f_n\ge0$ | Lemma 2.3.2，pp. 45–46 |
| 積分不依賴表示 | Corollary 2.3.3，p. 46 |
| $L^1(\mathbb{R})$ 是向量空間、積分線性且單調 | Theorem 2.3.4，p. 47 |
| 級數發散的點構成「零集」 | p. 47 |

---

## 1. 複習定義

[▶ 00:03](https://youtu.be/b7EvaW-mjrA?t=3)

$f$ **Lebesgue 可積**，記作 $f\simeq f_1+f_2+\cdots$，意思是有階梯函數 $f_n$ 使

- (a) $\sum_{n=1}^\infty\int|f_n|<\infty$；
- (b) $f(x)=\sum_{n=1}^\infty f_n(x)$ 對每個 $\sum|f_n(x)|<\infty$ 的 $x$。

積分定義為 $\int f=\sum_{n=1}^\infty\int f_n$，而階梯函數的積分就是矩形面積之和。

**問題**：$f$ 可能有很多種表示。不同表示給出的 $\sum\int f_n$ 一樣嗎？如果不一樣，「$\int f$」就沒有意義。

---

## 2. Lemma 2.3.2：非負函數的積分非負

[▶ 01:44](https://youtu.be/b7EvaW-mjrA?t=104)

**引理**：若 $f\simeq f_1+f_2+\cdots$ 且 $f\ge0$（對所有 $x$），則

$$\int f_1+\int f_2+\cdots\ge0.$$

講者照課本的證明走。

**Step 1：選 $n_0$。**[▶ 02:16](https://youtu.be/b7EvaW-mjrA?t=136) 給 $\varepsilon>0$，選 $n_0$ 使

$$\sum_{n=n_0+1}^\infty\int|f_n|<\varepsilon. \tag{2.11}$$

講者解釋為什麼可以：條件 (a) 說級數 $\sum\int|f_n|$ 收斂，所以尾巴能任意小；否則就跟收斂矛盾。

**Step 2：輔助數列。**[▶ 04:00](https://youtu.be/b7EvaW-mjrA?t=240)

$$g_n=f_1+\cdots+f_{n_0}+|f_{n_0+1}|+\cdots+|f_{n_0+n}|.$$

**$g_n$ 非遞減**【課堂討論】[▶ 06:28](https://youtu.be/b7EvaW-mjrA?t=388)：講者一開始想不通，後來說「我真笨」：$g_{n+1}=g_n+|f_{n_0+n+1}|\ge g_n$。$n$ 只影響最後一項，加上去的是非負的；可能相等（那一項是 0），所以是「非遞減」不是「遞增」。

**極限 $\ge0$**[▶ 10:30](https://youtu.be/b7EvaW-mjrA?t=630)：因為 $|f_k|\ge f_k$，

$$g_n(x)\ge\sum_{k=1}^{n_0+n}f_k(x),$$

讓 $n\to\infty$，右邊趨近 $f(x)\ge0$。所以 $\lim g_n(x)\ge0$。講者說：「我開始覺得在這個引理上花太多時間了，因為它其實很明顯。」

> 以下**不是逐字稿內容**，是補上課堂沒處理的情況：上面的論證只在 $\sum|f_n(x)|<\infty$ 的點成立（那裡才知道 $\sum f_k(x)=f(x)$）。在 $\sum|f_n(x)|=\infty$ 的點，$g_n(x)$ 的前 $n_0$ 項固定，後面加的是一個發散的非負級數，所以 $g_n(x)\to+\infty\ge0$。兩種情況都 $\ge0$。

**Step 3：用 Corollary 2.2.7。**[▶ 12:09](https://youtu.be/b7EvaW-mjrA?t=729) $(g_n)$ 是非遞減的階梯函數列，逐點極限 $\ge0$，由上一集的 Corollary 2.2.7，

$$\lim_n\int g_n\ge0.$$

**Step 4：估計。**[▶ 13:16](https://youtu.be/b7EvaW-mjrA?t=796)

$$\begin{aligned}0&\le\int f_1+\cdots+\int f_{n_0}+\sum_{n=n_0+1}^\infty\int|f_n|\\&\le\int f_1+\cdots+\int f_{n_0}+\sum_{n=n_0+1}^\infty\left(\int f_n+\int|f_n|\right)+\sum_{n=n_0+1}^\infty\int|f_n|\\&=\sum_{n=1}^\infty\int f_n+2\sum_{n=n_0+1}^\infty\int|f_n|\\&\le\sum_{n=1}^\infty\int f_n+2\varepsilon.\end{aligned}$$

- 第一行就是 $\lim\int g_n$。
- 第二行：課本加了 $\sum\left(\int f_n+\int|f_n|\right)$。講者說「這有點可疑」，他的解釋是逐點想：$f_n$ 為正時 $f_n+|f_n|=2|f_n|$，為負時相消成 0，所以加的東西 $\ge0$。[▶ 16:22](https://youtu.be/b7EvaW-mjrA?t=982)
- 第三行：前 $n_0$ 項加上 $\sum_{n>n_0}\int f_n$ 正好是 $\sum_{n=1}^\infty\int f_n$，剩下兩份 $\sum_{n>n_0}\int|f_n|$。
- 第四行用 (2.11)。

> 以下**不是逐字稿內容**，是第二行的另一種說法：由 Theorem 2.2.2(d)，$\left|\int f_n\right|\le\int|f_n|$，所以 $\int f_n+\int|f_n|\ge0$。

**Step 5：結論。**[▶ 19:39](https://youtu.be/b7EvaW-mjrA?t=1179) $0\le\sum\int f_n+2\varepsilon$ 對每個 $\varepsilon>0$ 成立，所以 $\sum\int f_n\ge0$。

【課堂討論】講者舉具體數字：如果 $\sum\int f_n=-0.5$，取 $\varepsilon=0.1$，就得到 $0\le-0.5+0.2=-0.3$，荒謬。∎[▶ 20:53](https://youtu.be/b7EvaW-mjrA?t=1253)

---

## 3. Corollary 2.3.3：積分與表示無關

[▶ 21:36](https://youtu.be/b7EvaW-mjrA?t=1296)

**推論**：若 $f\simeq\sum f_n$ 而且 $f\simeq\sum g_n$，則

$$\sum_{n=1}^\infty\int f_n=\sum_{n=1}^\infty\int g_n.$$

講者：這說明一個函數用兩串不同的階梯函數表示，生出的 Lebesgue 積分一樣；所以積分的定義**不依賴表示**。

**證明**[▶ 23:24](https://youtu.be/b7EvaW-mjrA?t=1404)：

1. 交錯排列兩串：$0\simeq f_1-g_1+f_2-g_2+\cdots$。講者解釋：$f-f$ 是零函數，兩串各自收斂到 $f$，相減收斂到 0。
2. 零函數 $\ge0$，用 Lemma 2.3.2：
   $$\int f_1-\int g_1+\int f_2-\int g_2+\cdots\ge0.$$
3. 兩個級數都絕對收斂，可以重排成 $\sum\int f_n-\sum\int g_n\ge0$。講者說：更小心的話可以先做有限和再重排取極限，課本直接用級數。[▶ 25:29](https://youtu.be/b7EvaW-mjrA?t=1529)
4. 記 $F=\sum\int f_n$、$G=\sum\int g_n$，得 $F\ge G$。論證對 $f,g$ 對稱，所以 $G\ge F$。故 $F=G$。∎

> 以下**不是逐字稿內容**，是補一個細節：第 1 步要驗證 $0\simeq f_1-g_1+f_2-g_2+\cdots$ 符合定義。(a)：$\sum\left(\int|f_n|+\int|g_n|\right)<\infty$。(b)：若 $\sum(|f_n(x)|+|g_n(x)|)<\infty$，則兩個級數在 $x$ 都絕對收斂，和分別是 $f(x)$，所以交錯級數的和是 $f(x)-f(x)=0$。

**後果**【課本補充】[▶ 27:32](https://youtu.be/b7EvaW-mjrA?t=1652)：

- 階梯函數 $f$ 是 Lebesgue 可積的：$f\simeq f+0+0+\cdots$，而且兩種定義的積分相等，所以可以用同一個符號 $\int$。
- 每個 Riemann 可積函數都 Lebesgue 可積，兩個積分相等（§2.10 證明）。
- 所有 Lebesgue 可積函數構成的空間記作 $L^1(\mathbb{R})$。之後本書說「可積」就是 Lebesgue 可積；講 Riemann 時會明說。

---

## 4. L¹(ℝ) 是向量空間，積分是線性泛函

[▶ 28:41](https://youtu.be/b7EvaW-mjrA?t=1721) 課本 Theorem 2.3.4。

**定理**：$L^1(\mathbb{R})$ 是向量空間，$\int$ 是 $L^1(\mathbb{R})$ 上的線性泛函。而且若 $f,g\in L^1(\mathbb{R})$、$f\le g$，則 $\int f\le\int g$。

**加法**[▶ 31:43](https://youtu.be/b7EvaW-mjrA?t=1903)：$f\simeq\sum f_n$、$g\simeq\sum g_n$。講者提議用 $(f_n+g_n)$ 當 $f+g$ 的表示，並檢查條件 (a)：

$$\sum_{n=1}^N\int|f_n+g_n|\le\sum_{n=1}^N\int|f_n|+\sum_{n=1}^N\int|g_n|,$$

$N\to\infty$ 時右邊兩個都有限，所以左邊有限。[▶ part 2 01:50](https://youtu.be/MP169hGYA7E?t=110) 積分：

$$\int(f+g)=\sum\int(f_n+g_n)=\sum\left(\int f_n+\int g_n\right)=\int f+\int g,$$

用了階梯函數積分的線性和「兩個收斂級數的和」（微積分 II）。

> 以下**不是逐字稿內容**，是依課本指出課堂版本的一個缺口：用 $(f_n+g_n)$ 時，條件 (b) 不一定成立。在某點 $x$，$\sum|f_n(x)+g_n(x)|$ 可能收斂，但 $\sum|f_n(x)|$ 和 $\sum|g_n(x)|$ 各自發散（大的正負項互相抵消），那裡我們不知道 $\sum(f_n+g_n)(x)$ 是不是 $f(x)+g(x)$。課本改用**交錯排列**
> $$f+g\simeq f_1+g_1+f_2+g_2+\cdots,$$
> 這時 $\sum(|f_n(x)|+|g_n(x)|)<\infty$ 推出兩個級數都絕對收斂，(b) 就成立；積分也一樣是 $\sum\int f_n+\sum\int g_n$。

**純量乘法**[▶ part 2 03:02](https://youtu.be/MP169hGYA7E?t=182)：$\lambda f\simeq\lambda f_1+\lambda f_2+\cdots$，$\int\lambda f=\lambda\int f$。零函數可積，負函數也可積。講者說：「這感覺像作業題，我停一下。」

**單調**[▶ part 2 07:47](https://youtu.be/MP169hGYA7E?t=467)：$f\le g$ ⟹ $g-f\ge0$ ⟹ $\int(g-f)\ge0$（Lemma 2.3.2）⟹ $\int g-\int f\ge0$（線性：$-f=(-1)f$，$-1$ 可以提出積分）。∎

---

## 5. 級數在哪裡發散？零集的第一次出現

[▶ part 2 09:01](https://youtu.be/MP169hGYA7E?t=541) 課本 p. 47。

講者重寫條件 (a)(b)。課本的觀察：

- 條件 (a) 完全沒提到 $f$。
- 條件 (b) 只要求在**絕對收斂的點** $f=\sum f_n$。那些點有多少？

**一個令人擔心的情況**[▶ part 2 12:40](https://youtu.be/MP169hGYA7E?t=760)：假如能找到滿足 (a) 的階梯函數 $f_n$，使 $\sum|f_n(x)|$ 在某個開區間 $(a,b)$ 的**每一點**都發散。把它們在 $(a,b)$ 外改成 0，那麼對**任何**在 $(a,b)$ 外為 0 的函數 $f$，都有 $f\simeq f_1+f_2+\cdots$（$(a,b)$ 外兩邊都是 0；$(a,b)$ 內條件 (b) 不用檢查）。講者說：這會非常惱人——那些 $f$ 的積分全都一樣，不管 $f$ 在 $(a,b)$ 裡長什麼樣。

**課本的回答**：既然已經證了積分與表示無關，這樣的數列**不可能存在**；級數不可能在非空開區間的每一點都發散。

**更強的結果**[▶ part 2 15:37](https://youtu.be/MP169hGYA7E?t=937)：若 $f\simeq f_1+f_2+\cdots$，令

$$Z=\left\{x\in\mathbb{R}:\sum_{n=1}^\infty|f_n(x)|=\infty\right\},\qquad g=\chi_Z.$$

則 $\int g=0$。

【課本補充】理由：$f+g\simeq f_1+f_2+\cdots$ 也成立（$g$ 只在 $Z$ 上不為 0，而 $Z$ 上條件 (b) 不用檢查）。所以 $\int(f+g)=\sum\int f_n=\int f$，由線性 $\int g=0$。

**零集**：$\int\chi_Z=0$，所以 $Z$ 在某種意義上是「很小」的集合，叫**零集（null set）**。於是：級數 $\sum f_n(x)$ 收斂到 $f(x)$ 對**零集以外**的所有 $x$ 成立。這種收斂叫**幾乎處處收斂（convergence almost everywhere）**，§2.7 討論。講者說這是第一次碰到「幾乎處處」，而且這裡還沒證明，別想從字裡行間看出來。[▶ part 2 17:38](https://youtu.be/MP169hGYA7E?t=1058)

**講者的題外話**【口頭】[▶ part 2 18:16](https://youtu.be/MP169hGYA7E?t=1096)：數學裡有時一方有看似鐵證的證明，另一方有看似可信的反例，只是有點模糊——研究前線的爭論就在這裡發生，「那裡你會看到政治」；他有個學生就遇過這種情況。

**還沒有例子**[▶ part 2 19:25](https://youtu.be/MP169hGYA7E?t=1165)：課本 p. 48 說，目前只有定義，要用「展開成階梯函數級數」來證一個函數可積很彆扭，「就像用 Riemann 和算 $\int_0^1e^xdx$」。讀者要有耐心，等理論再發展一點，就能輕鬆造出非平凡的例子。學生說他沒耐心，講者說「很遺憾，但我懂」。

---

## 6. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| Lemma 2.3.2 | $f\simeq\sum f_n$、$f\ge0$ ⟹ $\sum\int f_n\ge0$ | $g_n=f_1+\cdots+f_{n_0}+|f_{n_0+1}|+\cdots+|f_{n_0+n}|$ 非遞減、極限 $\ge0$；Cor 2.2.7；尾巴 $<\varepsilon$ |
| Cor 2.3.3 | 兩種表示 ⟹ $\sum\int f_n=\sum\int g_n$ | $0\simeq f_1-g_1+f_2-g_2+\cdots$；Lemma 2.3.2 兩個方向 |
| 階梯函數 | $f\simeq f+0+0+\cdots$ | 兩種積分一致 |
| $L^1(\mathbb{R})$ | Lebesgue 可積函數的空間 | Riemann 可積 ⊂ $L^1$（§2.10） |
| Thm 2.3.4 | $L^1$ 向量空間、$\int$ 線性、單調 | $f+g\simeq f_1+g_1+f_2+g_2+\cdots$（交錯） |
| 零集 | $Z=\{\sum|f_n|=\infty\}$，$\int\chi_Z=0$ | $f+\chi_Z\simeq\sum f_n$ |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 可積函數的絕對值 | 第 13 集：$|f|\in L^1$（Theorem 2.4.1） |
| 用可積函數代替階梯函數展開 | 第 13 集：Theorem 2.5.3（$L^1$ 的完備性雛形） |
| 零集、幾乎處處 | 第 14 集（§2.7） |
| Riemann ⊂ Lebesgue | 第 16 集（§2.10） |

---

## 附：本集一句話總結

> **用「非負函數的積分非負」這個引理（底下靠的是上一集單調階梯函數列的定理），可以證明同一個函數的任兩種階梯函數表示給出同一個積分，所以 Lebesgue 積分定義合理，$L^1(\mathbb{R})$ 是向量空間、積分是線性單調的泛函；而表示的級數發散的地方，必然是積分為 0 的「零集」。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-10 錄影逐字稿（YouTube 自動字幕，part 1 33:26 ＋ part 2 20:10）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.3 整理。*
