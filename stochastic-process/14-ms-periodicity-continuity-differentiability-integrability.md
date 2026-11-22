---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 14
lecture: Lec 9-3 General Concepts — The Power Spectrum (3/3)
date: 待補
video: https://youtu.be/ido3-Ns4dDo
notes: Papoulis & Pillai 4th ed. §9-1 Theorem 9-1（式 (9-71)–(9-73)，pp. 392–393）；§9-3 MS continuity and periodicity（式 (9-178)、(9-179)，p. 419）；Appendix 9A Continuity, Differentiation, Integration（Theorem 9A-1–9A-3，式 (9A-1)–(9A-9)，pp. 426–428）
---

# 第 14 集 · Lec 9-3 (3/3)：均方意義下的週期、連續、可微、可積——全部都是自相關的性質 [▶ 影片](https://youtu.be/ido3-Ns4dDo)

← 上一集：[13](13-integrated-spectrum-nnd-necessary-exclusion-ms-equality.md) ｜ [總目錄](README.md) ｜ 下一集：[15](15-discrete-time-processes-sampling-schur-paley-wiener.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 14 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（21:27，whisper large-v3-turbo）＋ Papoulis §9-1、§9-3、附錄 9A（pp. 392–393、419、426–428）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Cauchy–Schwarz inequality」→「Cultry Swatch／Culture Swords」，「若且唯若」→「若且微弱」，「wide-sense stationary」→「ysense／y sense／wise and stationary／Wisen Station」，「doubly periodic」→「w periodic」，「一維／二維」→「一圍／二圍」，「實部／虛部」→「十步／虛步」，「投影片」→「後影片」，「Poisson」→「poison／頗重」，「計數」→「技術」，「probability space」→「proprietate space」，「Brownian motion」→「Bronnier Motion」，「Poisson」→「波索」，「偏微分」→「偏尾分」，「Riemann integral」→「Reiman Integral／里曼積分／理慢可激」，「interpolation」→「interpretation」。以下一律用正確的字。

> **接上一集**：上一集最後定義了均方相等和均方週期。這一集把 Lec 9-3 收尾：均方意義下的**週期、連續、可微、可積**，全部都等價於**自相關**的對應性質。這是第 9 章的尾聲。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Mean square 是什麼](#1-mean-square-是什麼)
- [2. 均方週期 ⇔ 自相關雙週期（Theorem 9-1）](#2-均方週期--自相關雙週期theorem-9-1)
- [3. 均方連續 ⇔ 自相關連續](#3-均方連續--自相關連續)
  - [3.1 例：Poisson 過程是均方連續的](#31-例poisson-過程是均方連續的)
- [4. WSS 時的簡化](#4-wss-時的簡化)
- [5. 均方可微](#5-均方可微)
- [6. 均方可積](#6-均方可積)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| mean square 的意義 | [▶ 00:00](https://youtu.be/ido3-Ns4dDo?t=0) | — |
| 均方週期（Theorem 9-1） | [▶ 03:02](https://youtu.be/ido3-Ns4dDo?t=182) | 式 (9-71)–(9-73)，pp. 392–393 |
| 均方連續、Poisson 例子 | [▶ 07:10](https://youtu.be/ido3-Ns4dDo?t=430) | Theorem 9A-1，p. 427 |
| WSS 簡化 | [▶ 11:52](https://youtu.be/ido3-Ns4dDo?t=712) | 式 (9-178)、(9-179)，p. 419 |
| 均方可微、可積 | [▶ 15:58](https://youtu.be/ido3-Ns4dDo?t=958) | Theorem 9A-2、9A-3，pp. 427–428 |

---

## 1. Mean square 是什麼

[▶ 00:00](https://youtu.be/ido3-Ns4dDo?t=0)

- **mean square**（均方）：先取**平方**（square），再取**期望值**（mean）。英文慣例：先做的寫在後面。例：mean square error = 先把誤差平方、再取期望值。
- 反過來 **square mean** 是先取期望值、再平方。
- 隨機變數是變數，說 $X=Y$ 一定要講在什麼意義下。也可以用「先取絕對值再取期望值」等其他意義，但數學上大部分用 **mean square**。
- 下一章取樣定理：取樣後經過內插，跟原來的過程「相等」——就是均方意義。

**老師要傳達的核心觀念**【口頭】：均方意義的定義雖然是用隨機過程 $X$ 本身寫的，但實際檢驗時，**先平方再取期望值剛好就是自相關**。所以隨機過程的相等、可微分、週期性……**指的完全都是自相關的性質**。

---

## 2. 均方週期 ⇔ 自相關雙週期（Theorem 9-1）

[▶ 03:02](https://youtu.be/ido3-Ns4dDo?t=182) 回到 Theorem 9-1——課本第 9 章的**第一個**定理。第 9 章講到尾聲又回到它：開宗明義告訴你相等、週期、微分是什麼概念。

> **定義（均方週期，MS periodic）**：$E\left|X(t+T)-X(t)\right|^2=0$，對所有 $t$。
>
> **Theorem 9-1**：$X(t)$ 均方週期（週期 $T$）**⇔** 自相關**雙週期** (doubly periodic)：
> $$R(t_1+mT,\ t_2+nT)=R(t_1,t_2),\quad\text{對所有整數 }m,n.$$

- 沒有 WSS 的條件，所以自相關是**二維**的 $R(t_1,t_2)$，每一維都要週期 $T$。

**證明**：均方意義下能用的工具就是 Cauchy–Schwarz。

**⇒（forward part，順著念）**：取 $Z=X(t_1)$、$W=X(t_2+T)-X(t_2)$：
$$\left|E\left\{X(t_1)\left[X(t_2+T)-X(t_2)\right]^*\right\}\right|^2\le E|X(t_1)|^2\cdot E\left|X(t_2+T)-X(t_2)\right|^2.$$
右邊第二個因子由均方週期的定義是 0。左邊就是 $|R(t_1,t_2+T)-R(t_1,t_2)|^2$，所以 $R(t_1,t_2+T)=R(t_1,t_2)$。重複使用（兩個變數都做）得到雙週期。

**⇐（converse，把句子倒過來念）**：雙週期對任何整數 $m,n$ 都對，所以代 1。把均方展開，本身就是自相關：
$$E|X(t+T)-X(t)|^2=R(t+T,t+T)-R(t+T,t)-R(t,t+T)+R(t,t).$$
由雙週期，$R(t+T,t+T)=R(t,t)$，$R(t+T,t)=R(t,t)$，$R(t,t+T)=R(t,t)$，全部相等，所以 $=0$。 ∎

老師說：數學不深，但課本認為很重要，他也認為觀念上很重要。有了這個觀念，後面可以舉一反三。

---

## 3. 均方連續 ⇔ 自相關連續

[▶ 07:10](https://youtu.be/ido3-Ns4dDo?t=430) 這不在課本正文，在附錄 9A。

> **定義（均方連續，MS continuous）**：對任何 $t$，從左或從右逼近都連續：
> $$E\left|X(t+\varepsilon)-X(t)\right|^2\to0,\quad\varepsilon\to0.$$
>
> **Theorem 9A-1**：若自相關 $R(t_1,t_2)$ 連續，則 $X(t)$ 均方連續。

**證明**：展開
$$E|X(t+\varepsilon)-X(t)|^2=R(t+\varepsilon,t+\varepsilon)-R(t+\varepsilon,t)-R(t,t+\varepsilon)+R(t,t).$$
$R$ 連續，$\varepsilon\to0$ 時四項都趨於 $R(t,t)$，相消為 0。 ∎（老師說：要嘛展開、要嘛用 Cauchy–Schwarz，這樣的工具就夠了。）

【課本補充】Corollary（9A-2）：均方連續 ⇒ 平均連續，因為 $E\{[X(t+\varepsilon)-X(t)]^2\}\ge E^2\{X(t+\varepsilon)-X(t)\}$；所以 $\lim E\{X(t+\varepsilon)\}=E\{\lim X(t+\varepsilon)\}$（9A-3）。

### 3.1 例：Poisson 過程是均方連續的

[▶ 08:45](https://youtu.be/ido3-Ns4dDo?t=525) Poisson 過程：$t_1,t_2,t_3,\dots$ 是隨機點，計數 0 到 $t$ 之間來了幾個顧客、幾通電話、幾個封包。它是均方連續的嗎？

看圖會覺得不是——它一直在跳。但：

以下的計算**不是逐字稿內容**，是依第 6 集的自相關 $R(t_1,t_2)=\lambda^2t_1t_2+\lambda\min(t_1,t_2)$ 補的：
$$E|X(t+\varepsilon)-X(t)|^2=\underbrace{\lambda^2(t+\varepsilon)^2+\lambda(t+\varepsilon)}_{R(t+\varepsilon,t+\varepsilon)}-2\underbrace{\left[\lambda^2t(t+\varepsilon)+\lambda t\right]}_{R(t+\varepsilon,t)}+\underbrace{\lambda^2t^2+\lambda t}_{R(t,t)}=\lambda^2\varepsilon^2+\lambda\varepsilon\to0.$$
（$\varepsilon>0$；$R$ 處處連續，所以是均方連續。）

**重要的觀念區隔**【口頭】：

- 回到機率空間：隨機過程不是隨機的，是**函數映射**。
- **隨機過程均方連續，不代表它原來的映射（每一條樣本路徑）連續**。
- 因為均方只要求**期望值**是 0，不是每一點都是 0。（類比：$\pm1$ 各半，期望值是 0，但它從來不是 0。）
- Poisson 過程：**均方連續**，但**每一條映射都不連續**，一直有跳躍。
- 所以你可以定義一個映射不連續、但隨機過程（均方）連續的例子。這要跟過去學確定函數 (deterministic function) 的觀念區隔開來，不小心就會犯邏輯上的小錯誤。統計上的東西跟實際的東西還是有一點距離。

【課本補充】Papoulis p. 427 Note：(9A-1) 對區間 $I$ 內每個 $t$ 成立，只推出在某個**特定**點上幾乎所有樣本連續，不推出樣本在 $I$ 內每一點都連續。Poisson 過程和 Wiener 過程都是均方連續；但 Poisson 的樣本在 $t_i$ 不連續，而 Wiener 過程幾乎所有樣本都連續。

---

## 4. WSS 時的簡化

[▶ 11:52](https://youtu.be/ido3-Ns4dDo?t=712) 前面都沒加條件，所以自相關是二維 $R(t_1,t_2)$。加上 **WSS**，自相關只是時間差的函數，均方的 if and only if 條件可以簡化成**一維**。（老師說投影片上這裡從二維變一維，自己看可能看不出要表達什麼。）

**均方連續**（WSS）：
$$E|X(t+\varepsilon)-X(t)|^2=2\left[R(0)-\text{Re}\,R(\varepsilon)\right].$$

為什麼只有**實部**？展開 $E|A-B|^2=E|A|^2-E[AB^*]-E[BA^*]+E|B|^2$。中間兩項互為共軛，相加是實數 $2\,\text{Re}\,E[AB^*]$；WSS 時 $E[AB^*]=R(\varepsilon)$。所以**只要看自相關的實部**，虛部完全不重要。這是 WSS 帶來的特有現象。

> （WSS）$X(t)$ 均方連續 ⇔ $\text{Re}\,R(\tau)$ 在 $\tau=0$ 連續（再由第 13 集，⇔ $R(\tau)$ 處處連續）。

**均方週期**（WSS）：
$$E|X(t+T)-X(t)|^2=2\left[R(0)-\text{Re}\,R(T)\right].$$

> （WSS）$X(t)$ 均方週期 ⇔ $R(T)=R(0)$。

- **只要看兩點**：$0$ 和一個週期 $T$。這兩點相等就是均方週期，不用看別的點。（由第 13 集 Theorem 9-5，$R(T)=R(0)$ 又推出 $R$ 是週期 $T$ 的函數。）這是 WSS 給的好結果。

【課本補充】式 (9-178)、(9-179)，p. 419。

---

## 5. 均方可微

[▶ 15:58](https://youtu.be/ido3-Ns4dDo?t=958) 例：以後可能碰到**布朗運動** (Brownian motion)，它和 Poisson 一樣是用條件定義的。它可不可微？分析時我們還是會對它微分，所以要講清楚是什麼意義下的微分。

> **均方可微** (MS differentiable)：把「還沒完成的微分」（差商）和「已經完成的微分」（微分器的輸出 $X'(t)$，本身是一個隨機過程）相減，平方取期望值趨於 0：
> $$E\left|\frac{X(t+\varepsilon)-X(t)}{\varepsilon}-X'(t)\right|^2\to0,\quad\varepsilon\to0.$$

> **Theorem 9A-2**：若 $\dfrac{\partial^2R(t_1,t_2)}{\partial t_1\partial t_2}$ 存在，則 $X(t)$ 均方可微。

**證明的想法**：一樣把平方展開，結果完全由自相關決定。展開後有 $X'X'$ 的項（第三項），這裡需要額外用到一個東西——**基本定理和 Theorem 9-2**（第 11 集）：

- 心中要有這張圖：$R_{XX}(t_1,t_2)$ → 對 $t_2$ 濾波 → $R_{XY}$ → 對 $t_1$ 濾波 → $R_{YY}$。輸出的自相關就是輸入的自相關經過**兩次**濾波（$t_2$ 先、$t_1$ 後）。
- 微分器是線性濾波器，所以
$$R_{XX'}(t_1,t_2)=\frac{\partial R_{XX}(t_1,t_2)}{\partial t_2},\qquad R_{X'X'}(t_1,t_2)=\frac{\partial^2R_{XX}(t_1,t_2)}{\partial t_1\partial t_2}.$$
- 把展開式裡的 $R_{X'X'}$、$R_{XX'}$ 都換成 $R_{XX}$ 的偏微分，整理後就相消。

老師說這裡給的是觀念，不是 step by step 的完整證明；有興趣可以自己證。

【課本補充】Papoulis Theorem 9A-2（p. 427）的證法用 **Cauchy 判準** (Cauchy criterion)，避開未知的 $X'(t)$：只要證
$$E\left\{\left[\frac{X(t+\varepsilon_1)-X(t)}{\varepsilon_1}-\frac{X(t+\varepsilon_2)-X(t)}{\varepsilon_2}\right]^2\right\}\to0,\quad\varepsilon_1,\varepsilon_2\to0.$$
關鍵一步：$E\{[X(t+\varepsilon_1)-X(t)][X(t+\varepsilon_2)-X(t)]\}=R(t+\varepsilon_1,t+\varepsilon_2)-R(t+\varepsilon_1,t)-R(t,t+\varepsilon_2)+R(t,t)$，除以 $\varepsilon_1\varepsilon_2$ 趨於 $\frac{\partial^2R(t,t)}{\partial t\,\partial t}$；展開平方得 $\partial^2R-2\partial^2R+\partial^2R=0$。Corollary：$E\{X'(t)\}=\frac{d}{dt}E\{X(t)\}$。課本 Note：Poisson 過程的自相關在 $t_i$ 不連續，所以 $X'(t)$ 在那些點不存在；但像確定訊號一樣，可以引進隨機脈衝，把 $X'(t)$ 解讀成 Poisson 脈衝（第 11 集）。

**意義**【口頭】：有了這個觀念，就知道怎麼定義自己需要的性質。將來做研究處理隨機過程時，最重要的性質就是自相關。

---

## 6. 均方可積

[▶ 20:06](https://youtu.be/ido3-Ns4dDo?t=1206)

> **均方可積** (MS integrable)：Riemann 和在均方意義下收斂
> $$\int_a^bX(t)\,dt=\lim_{\Delta t_i\to0}\sum_iX(t_i)\,\Delta t_i.$$
> **Theorem 9A-3**：若 $\displaystyle\int_a^b\!\!\int_a^b|R(t_1,t_2)|\,dt_1dt_2<\infty$，則 $X(t)$ 均方可積。

- 這是什麼積分？**Riemann 積分**——畫長方形、切長條。一般都假設分析的對象是 Riemann 可積的，比較方便處理。
- 積分器是**線性**的（$A$ 是 $B$ 的積分、$C$ 是 $D$ 的積分，則 $A+C$ 是 $B+D$ 的積分），所以基本定理和 Theorem 9-2 照樣可以用。**只要是線性濾波器就可以用；非線性就不行。**

【課本補充】證明同樣用 Cauchy 判準：展開 $E\left\{\sum_iX(t_i)\Delta t_i\sum_kX(t_k)\Delta t_k\right\}=\sum_{i,k}R(t_i,t_k)\Delta t_i\Delta t_k$，趨於 $R$ 的二重積分。Corollary（9A-9）：
$$E\left\{\left|\int_a^bX(t)\,dt\right|^2\right\}=\int_a^b\!\!\int_a^bR(t_1,t_2)\,dt_1dt_2,$$
和第 6 集 Example 9-3 的 (9-11) 一致。

---

## 7. 一頁速查表

### 均方意義的性質 = 自相關的性質

| 性質 | 定義 | 等價（或充分）條件 |
|---|---|---|
| 均方週期 | $E\lvert X(t+T)-X(t)\rvert^2=0$ | ⇔ $R(t_1,t_2)$ 雙週期；WSS：⇔ $R(T)=R(0)$ |
| 均方連續 | $E\lvert X(t+\varepsilon)-X(t)\rvert^2\to0$ | ⇐ $R(t_1,t_2)$ 連續；WSS：⇔ $\text{Re}\,R(\tau)$ 在 0 連續 |
| 均方可微 | $E\lvert\frac{X(t+\varepsilon)-X(t)}{\varepsilon}-X'(t)\rvert^2\to0$ | ⇐ $\partial^2R/\partial t_1\partial t_2$ 存在 |
| 均方可積 | Riemann 和均方收斂 | ⇐ $\iint\lvert R\rvert<\infty$ |

- 關鍵展開：$E\lvert X(s)-X(t)\rvert^2=R(s,s)-R(s,t)-R(t,s)+R(t,t)$；WSS：$=2[R(0)-\text{Re}\,R(s-t)]$。
- 均方週期 ⇒（Cauchy–Schwarz）$\lvert R(t_1,t_2+T)-R(t_1,t_2)\rvert^2\le R(t_1,t_1)\cdot0$。
- 微分器、積分器是線性濾波器：$R_{XX'}=\partial_{t_2}R$，$R_{X'X'}=\partial_{t_1}\partial_{t_2}R$；$E\lvert\int X\rvert^2=\iint R$。

### 觀念

- 均方連續 ≠ 樣本路徑連續。Poisson：$E|X(t+\varepsilon)-X(t)|^2=\lambda\varepsilon+\lambda^2\varepsilon^2\to0$，但每條路徑都在跳。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 均方相等、均方連續 | §10-5 取樣定理（第 20 集）：取樣後內插 = 原過程（均方） |
| 均方週期 | §10-4 循環平穩（第 19 集）；§11-3 Fourier 級數（第 26–27 集） |
| 均方可積、$E\lvert\int X\rvert^2=\iint R$ | §12-1 遍歷性：時間平均的變異數（第 30–33 集） |
| 下一集 | §9-4 離散時間過程（第 15 集） |

---

## 附：本集一句話總結

> **隨機過程在均方意義下的週期、連續、可微、可積，全部可以由自相關判斷（週期 ⇔ $R$ 雙週期；WSS 時只看 $R(T)=R(0)$；連續看 $R$ 連續；可微看 $\partial^2R/\partial t_1\partial t_2$；可積看 $\iint|R|$），但要記得：均方連續不代表每條樣本路徑連續，Poisson 過程就是例子。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-3 (3/3) 錄影逐字稿（whisper large-v3-turbo，21:27）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
