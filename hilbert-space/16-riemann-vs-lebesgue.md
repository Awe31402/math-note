---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 16
lecture: Lecture 16
date: 2023-02-22
video: https://youtu.be/e9KkfTG7FP4
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.10–2.11（書頁 64–71，PDF 頁 83–90）
---

# 第 16 集 · Riemann 積分 vs Lebesgue 積分、可測集 [▶ 影片](https://youtu.be/e9KkfTG7FP4)

← 上一集：[15-locally-integrable-functions](15-locally-integrable-functions.md) ｜ [總目錄](README.md) ｜ 下一集：[17-lebesgue-rn-convolution](17-lebesgue-rn-convolution.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 16 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（59:50，whisper 轉錄，時間點可能差 1–2 秒）＋ Debnath & Mikusiński §2.10–2.11
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Riemann 可積 ⟹ Lebesgue 可積](#1-riemann-可積--lebesgue-可積)
- [2. 積分函數是連續的](#2-積分函數是連續的)
- [3. 微積分基本定理、變數代換（課堂跳過）](#3-微積分基本定理變數代換課堂跳過)
- [4. 可測集與 Lebesgue 測度](#4-可測集與-lebesgue-測度)
- [5. 零集的覆蓋刻畫](#5-零集的覆蓋刻畫)
- [6. 可數可加性](#6-可數可加性)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Riemann 可積 ⟹ Lebesgue 可積，積分相等 | Theorem 2.10.1，pp. 64–65 |
| $F(x)=\int_c^xf$ 連續 | Theorem 2.10.2，p. 65 |
| 微積分基本定理、變數代換（跳過） | Theorem 2.10.3–2.10.4，pp. 65–67 |
| 可測集、Lebesgue 測度 | Definition 2.11.1–2.11.2，p. 68 |
| 零集 ⟺ 可被總長任意小的區間覆蓋 | Theorem 2.11.3，pp. 68–69 |
| 可數可加性 | Theorem 2.11.4，pp. 69–70 |

**講者的擔心**[▶ 00:00](https://youtu.be/e9KkfTG7FP4?t=0)：這本書沒有給 Riemann 積分的定義，卻要證 Lebesgue 積分跟 Riemann 積分一樣——「你沒定義 Riemann 積分，怎麼知道？」他猜課本假設讀者在正式的實分析課學過。學生說他們的實分析課沒講到積分。

講者也抱怨【口頭】：清潔人員用水擦白板，留下看不見的條紋，要用白板清潔劑（裡面有蠟）才對。[▶ 01:31](https://youtu.be/e9KkfTG7FP4?t=91)

---

## 1. Riemann 可積 ⟹ Lebesgue 可積

[▶ 02:11](https://youtu.be/e9KkfTG7FP4?t=131) 課本 Theorem 2.10.1。

**定理**：Riemann 可積函數是 Lebesgue 可積的，而且兩個積分相等。

**設定**：$f$ Riemann 可積，在 $[a,b)$ 外為 0，$|f|<M$。講者說：Riemann 積分本來就只處理有界函數，所以這不失一般性。他說很多人教微積分只對連續函數講 Riemann 積分，可以推廣到有限多個不連續點：把連續的小段的積分加起來。[▶ 04:08](https://youtu.be/e9KkfTG7FP4?t=248)

**Step 1：等分。**[▶ 05:02](https://youtu.be/e9KkfTG7FP4?t=302) 把 $[a,b)$ 分成 $n$ 等份，每份長 $\Delta x=\frac{b-a}{n}$（課本叫 $c$，講者堅持用 $\Delta x$）：

$$I_k=[a+(k-1)\Delta x,\ a+k\Delta x),\qquad k=1,\dots,n.$$

（講者給 $I_k$ 取了個綽號「Pac-Man$_k$」。）

**Step 2：下、上階梯函數。**[▶ 06:31](https://youtu.be/e9KkfTG7FP4?t=391)

$$g_n(x)=\inf_{t\in I_k}f(t),\qquad h_n(x)=\sup_{t\in I_k}f(t)\qquad(x\in I_k),$$

區間外都是 0。講者發現課本的下標寫得混亂（式子裡有 $n$ 也有 $k$），猜是筆誤，「你要把 $n$ 換成 $k$，或把那個 $k$ 換成 $n$，隨你」。$g_n$、$h_n$ 在每個 $I_k$ 上是常數，所以**是階梯函數**。[▶ 20:06](https://youtu.be/e9KkfTG7FP4?t=1206)

**Step 3：$g_n$ 非遞減？**【課堂討論】[▶ 11:05](https://youtu.be/e9KkfTG7FP4?t=665) 課本說 $(g_n)$ 是有界、非遞減的函數列。講者問為什麼非遞減。他先注意到相鄰的 $I_k$ 互不相交但「互相碰著」，而且用的是下確界不是最小值，接著給了一個關於相鄰區間的論證，說「這其實很微妙，我很驚訝自己想通了」（他說今天凌晨兩點半就起來寫微積分講義）。

> 以下**不是逐字稿內容**，是依數學推論的：課堂上的論證（比較同一個分割裡相鄰兩段的下確界）其實不是理由。真正的理由應該是**加細**：如果新分割的每一段都包含在舊分割的某一段裡，新的下確界取在較小的集合上，所以 $\ge$ 舊的下確界。可是「分成 $n$ 等份」和「分成 $n+1$ 等份」**不是**彼此的加細（例如 $n=2$ 的分點 $\frac12$ 不是 $n=3$ 的分點），所以 $g_n\le g_{n+1}$ 一般**不成立**。例如 $[0,1)$ 上 $f=\chi_{[1/2,1)}$：$g_2=\chi_{[1/2,1)}$，但 $g_3=\chi_{[2/3,1)}$，在 $[\frac12,\frac23)$ 上 $g_3=0<1=g_2$。
>
> **修正**：改用 $2^m$ 等份（每次對半切），分割一個比一個細，$g_{2^m}$ 就真的非遞減、$h_{2^m}$ 非遞增。下面的論證照樣成立。

**Step 4：取極限。**[▶ 18:07](https://youtu.be/e9KkfTG7FP4?t=1087) 每個 $x$ 上 $(g_n(x))$ 是有界單調實數列，所以收斂。【課堂討論】學生先提單調收斂定理，講者想了一下，學生改說是「有界單調數列收斂定理」，講者：「謝謝，我這週微積分 II 才剛教過。」定義 $g(x)=\lim g_n(x)$。

$|g_n|\le M\chi_{[a,b)}$（可積），由 **Lebesgue 控制收斂定理**，$g$ 可積且 $\int g=\lim\int g_n$。同理 $h=\lim h_n$ 可積，$\int h=\lim\int h_n$（$h_n$ 非遞增，論證一樣）。[▶ 20:49](https://youtu.be/e9KkfTG7FP4?t=1249)

**Step 5：用 Riemann 可積。**[▶ 23:35](https://youtu.be/e9KkfTG7FP4?t=1415) 因為 $f$ Riemann 可積，

$$\lim_n\int g_n=\lim_n\int h_n.$$

$\int g_n$ 是**下和**，$\int h_n$ 是**上和**。講者：Riemann 可積的一種刻畫就是下和與上和收斂到同一個值。

【課堂討論】學生提到 **Darboux 積分**。講者：Darboux 是對**任意**分割做的，我們這裡從一開始就用等寬分割。他比較微積分課本【口頭】：Howard Anton 的《Calculus》不用 $n\to\infty$，而是讓 $\Delta x\to0$ 跑遍所有分割，寬度不必相等，「其實相當高級」；Stewart 用等寬分割，他印象中幾乎不談上下和。他自己教學生時說：「左端點、右端點、中點規則都收斂到同一個值，那就是面積」——只要函數 Riemann 可積就對。[▶ 25:36](https://youtu.be/e9KkfTG7FP4?t=1536)

**Step 6：結論。**[▶ 27:36](https://youtu.be/e9KkfTG7FP4?t=1656)

$$\int|h-g|=\int(h-g)=\lim_n\int(h_n-g_n)=0. \tag{2.15}$$

所以 $g=h$ a.e.。又 $g\le f\le h$，所以 $g=f=h$ a.e.。因此 $f$ Lebesgue 可積，而且 Riemann 積分和 Lebesgue 積分都等於 $\lim\int g_n$。∎

講者：要完全滿意，需要手上有 Riemann 積分完整嚴格的定義；不管用哪種講法，只要夠仔細，其中一部分一定是「上下和要吻合」。[▶ 29:12](https://youtu.be/e9KkfTG7FP4?t=1752)

---

## 2. 積分函數是連續的

[▶ 30:36](https://youtu.be/e9KkfTG7FP4?t=1836) 課本 Theorem 2.10.2。

**定理**：$f$ 在區間 $(a,b)$（有界或無界）上 Lebesgue 可積，$a\le c\le b$。則

$$F(x)=\int_c^xf$$

在 $(a,b)$ 上連續，而且 $F(a)=\lim_{x\to a^+}F(x)$、$F(b)=\lim_{x\to b^-}F(x)$ 存在且有限。

講者：Lebesgue 可積函數可以極度不連續，但**積分把它抹平**，得到的面積函數一定連續。課本允許 $a,b$ 是 $\pm\infty$。[▶ 32:12](https://youtu.be/e9KkfTG7FP4?t=1932)

**證明（右連續）**[▶ 33:31](https://youtu.be/e9KkfTG7FP4?t=2011)：

1. 取 $a\le x<b$，以及遞減數列 $x<x_{n+1}<x_n<b$，$x_n\to x$。
2. 令 $g_n=\chi_{(x,x_n)}$。$n\to\infty$ 時區間縮成空集（$x$ 本身不在開區間裡），所以 $fg_n\to0$ 在每一點。[▶ 36:56](https://youtu.be/e9KkfTG7FP4?t=2216)
3. $|fg_n|\le|f|$：$g_n$ 只是 0 或 1。
4. $F(x_n)-F(x)=\int_x^{x_n}f$。

   【課堂討論】[▶ 39:16](https://youtu.be/e9KkfTG7FP4?t=2356) 講者問：我們證過 $\int_c^{x_n}f-\int_c^xf=\int_x^{x_n}f$ 嗎？他不記得，猜是作業。他畫數線檢查 $c$ 在不同位置的情況：$c$ 在 $x$ 和 $x_n$ 之間時直接相加；$c$ 在右邊時用 $\int_c^{x}=-\int_{x}^c$ 的約定，相減後剩 $\int_x^{x_n}$。結論：「不管 $c$ 在哪都對。」講者提到這就是他第一堂課說的「用 Riemann 定義很難證、Lebesgue 下一行就好」的那條性質。
5. 所以 $F(x_n)-F(x)=\int fg_n\to0$，由**控制收斂定理**。[▶ 45:00](https://youtu.be/e9KkfTG7FP4?t=2700)

$F$ 在 $x$ 右連續，也在 $a$ 有右極限。左連續同理（用 $\chi_{(x_n,x)}$，$x_n\uparrow x$）。左右都連續 ⟹ 連續。∎

講者：「這是收斂定理的直接結果……什麼都是 Lebesgue 控制收斂定理，對吧？」[▶ 47:40](https://youtu.be/e9KkfTG7FP4?t=2860)

---

## 3. 微積分基本定理、變數代換（課堂跳過）

[▶ 48:17](https://youtu.be/e9KkfTG7FP4?t=2897) 講者說他要跳過 §2.10 剩下的部分（Lebesgue 積分的微積分基本定理與變數代換），如果週末前有時間再回來。

【課本補充】

**Theorem 2.10.3（微積分基本定理）**：$f$ 在 $(a,b)$ 上可積，$F(x)=\int_c^xf$。若 $f$ 在 $x_0$ **連續**，則 $F$ 在 $x_0$ 可微且 $F'(x_0)=f(x_0)$。

證明要點：$h>0$ 時 $\frac{F(x_0+h)-F(x_0)}{h}=\frac1h\int_{x_0}^{x_0+h}f$。連續 ⟹ 對 $\varepsilon$ 有 $\delta$，在 $(x_0,x_0+\delta)$ 上 $f(x_0)-\varepsilon<f<f(x_0)+\varepsilon$；積分再除以 $h$，差商就夾在 $f(x_0)\pm\varepsilon$ 之間。$h<0$ 同理。

**Theorem 2.10.4（變數代換）**：$g$ 在 $(a,b)$ 上非遞減、可微，$g'$ 在 $(a,b)$ 上可積；$f$ 在 $(g(a),g(b))$ 上可積。則 $f(g(t))g'(t)$ 在 $(a,b)$ 上可積，而且

$$\int_{g(a)}^{g(b)}f(t)\,dt=\int_a^bf(g(t))\,g'(t)\,dt.$$

---

## 4. 可測集與 Lebesgue 測度

[▶ 49:38](https://youtu.be/e9KkfTG7FP4?t=2978) 課本 §2.11。

【課本補充】這本書的積分不需要測度；但有了積分，測度可以很容易地定義。Lebesgue 測度是把「區間長度」推廣到一大類集合。不是所有集合都可測，而且不可測集的存在證明**不是建構性的**：只能證明它存在，造不出來（參考 Friedman 1982）。

**可測集（measurable set）**：$S$ 的特徵函數 $\chi_S$ **局部可積**。

**Lebesgue 測度**：$S$ 可測。若 $\chi_S$ 可積，$\mu(S)=\int\chi_S$；若不可積，$\mu(S)=\infty$。

**例子**【課堂討論】[▶ 56:27](https://youtu.be/e9KkfTG7FP4?t=3387)：講者問開區間 $(a,b)$ 的測度。學生答 $b-a$（$\chi_{(a,b)}$ 的積分）。講者：「把它去神秘化，測度基本上就是集合的**長度**。」測度 0 就是長度 0。

**零集** = 測度為 0 的集合。

---

## 5. 零集的覆蓋刻畫

[▶ 52:11](https://youtu.be/e9KkfTG7FP4?t=3131) 課本 Theorem 2.11.3。講者說證明一頁長，只敘述。

**定理**：$S\subseteq\mathbb{R}$ 是零集 ⟺ 對每個 $\varepsilon>0$，存在半開區間 $[a_1,b_1),[a_2,b_2),\dots$ 使

$$S\subseteq\bigcup_{n=1}^\infty[a_n,b_n)\quad\text{而且}\quad\sum_{n=1}^\infty(b_n-a_n)<\varepsilon. \tag{2.21}$$

講者：意思是能用總長任意小的一串區間把 $S$ 蓋住。

> 以下**不是逐字稿內容**，是用這個定理看「可數集是零集」：$S=\{s_1,s_2,\dots\}$，用 $[s_n,s_n+\varepsilon/2^{n+1})$ 蓋住 $s_n$，總長 $\varepsilon/2<\varepsilon$。所以 $\mathbb{Q}$ 是零集，$\chi_{\mathbb{Q}}=0$ a.e.，$\int\chi_{\mathbb{Q}}=0$——這就是第 11 集那個「Riemann 處理不了」的函數，Lebesgue 積分給它 0。（第 11 集 Example 2.2.5 在 $\mathbb{Q}$ 裡做的正是這個覆蓋。）

---

## 6. 可數可加性

[▶ 54:46](https://youtu.be/e9KkfTG7FP4?t=3286) 課本 Theorem 2.11.4。

**定理（$\sigma$-可加性）**：$S_1,S_2,\dots$ 是互不相交的可測集，則 $S=\bigcup_nS_n$ 可測，而且

$$\mu(S)=\sum_{n=1}^\infty\mu(S_n). \tag{2.24}$$

講者：級數可以發散（等於 $\infty$）。[▶ 55:56](https://youtu.be/e9KkfTG7FP4?t=3356)

**例子**【課堂討論】[▶ 57:06](https://youtu.be/e9KkfTG7FP4?t=3426)：

$$[1,\infty)=\bigcup_{n=1}^\infty[n,n+1).$$

（講者先寫成從 0 開始，學生糾正成從 1。）每塊測度 1，所以

$$\mu([1,\infty))=\sum_{n=1}^\infty1=\infty.$$

講者【口頭】：測度是數學裡少數「把 $\infty$ 當成擴充數系的一員、有意義地使用」的例子；好的分析書在 sup、inf 上也會用 $\pm\infty$ 把概念完整推廣。

【課本補充】課本 §2.11 還有**可測函數**（存在階梯函數列幾乎處處收斂到它）及其性質；例如 $\frac1x$（$x>0$）、0（$x\le0$）可測但不局部可積；若 $f$ 可測且 $|f|$ 可積，則 $f$ 可積。本集沒講。

**下一堂**：講者打算講完可測集，並概述第 2 章剩下的幾節。[▶ 59:28](https://youtu.be/e9KkfTG7FP4?t=3568)

---

## 7. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| Riemann ⟹ Lebesgue | 積分相等 | 下、上階梯函數 $g_n\le f\le h_n$；控制收斂；上下和極限相等 ⟹ $g=f=h$ a.e. |
| 小修正 | 用 $2^m$ 等份 | 等分 $n$ 份不是彼此加細，$g_n$ 不一定遞增 |
| 積分函數連續 | $F(x)=\int_c^xf$ 連續、端點極限存在 | $F(x_n)-F(x)=\int f\chi_{(x,x_n)}\to0$（控制收斂） |
| FTC | $f$ 在 $x_0$ 連續 ⟹ $F'(x_0)=f(x_0)$ | 差商夾在 $f(x_0)\pm\varepsilon$ |
| 變數代換 | $\int_{g(a)}^{g(b)}f=\int_a^bf(g(t))g'(t)dt$ | $g$ 非遞減、可微 |
| 可測集 | $\chi_S$ 局部可積 | |
| 測度 | $\mu(S)=\int\chi_S$ 或 $\infty$ | $\mu((a,b))=b-a$ |
| 零集 | ⟺ 可被總長 $<\varepsilon$ 的區間蓋住 | 可數集是零集；$\int\chi_\mathbb{Q}=0$ |
| $\sigma$-可加 | 不相交 ⟹ $\mu(\bigcup S_n)=\sum\mu(S_n)$ | $[1,\infty)$ 測度 $\infty$ |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Lebesgue 積分包含 Riemann 積分 | 之後所有具體計算都能用微積分的方法 |
| 積分讓函數變光滑 | 第 17 集：摺積讓函數變光滑 |
| 可測集上的積分 $\int_\Omega f=\int f\chi_\Omega$、$L^1(\Omega)$ | 第 17 集起：$\mathbb{R}^N$ 上的積分；第 18 集：$L^2(\Omega)$ |
| 測度 | 第 33–34 集：量子力學的機率詮釋 |

---

## 附：本集一句話總結

> **Riemann 可積函數夾在上下階梯函數之間，用控制收斂定理取極限、再用「上下和吻合」，就得到它也是 Lebesgue 可積、積分相同；Lebesgue 積分讓積分函數自動連續；而有了積分，測度就是特徵函數的積分——長度的推廣，零集就是能被總長任意小的區間蓋住的集合。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-22 錄影逐字稿（whisper large-v3-turbo 轉錄，59:50）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.10–2.11 整理。*
