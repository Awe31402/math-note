---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 8
lecture: Lec 9-1 General Concepts — Definitions (7/7)
date: 待補
video: https://youtu.be/CsYOZMqQBEQ
notes: Papoulis & Pillai 4th ed. §9-1 Stationary Processes（式 (9-47)–(9-72)，pp. 387–392；Example 9-13、9-14 與 Corollary，pp. 390–392）
---

# 第 8 集 · Lec 9-1 (7/7)：平穩過程（SSS、WSS 等）、$a\cos\omega t+b\sin\omega t$ 何時平穩、為什麼一定是高斯、相關時間 [▶ 影片](https://youtu.be/CsYOZMqQBEQ)

← 上一集：[07](07-telegraph-signal-poisson-sum-difference-selection-uniform.md) ｜ [總目錄](README.md) ｜ 下一集：[09](09-systems-memoryless-sss-preserved-hard-limiter-arcsine.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 8 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（51:32，whisper large-v3-turbo）＋ Papoulis §9-1（pp. 387–392）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「穩態」→「穩泰／稳泰」，「wide-sense stationary」→「Wisen stationary／Y Send／wise and stationary／RAW 稳泰」，「weakly」→「weekly」，「strict sense」→「tricky sense」，「invariant to a shift of the origin」→「invariant to achieve the origin／shift of the region」，「平移」→「評儀」，「transient」→「trancient」，「Jacobian」→「Jakobian／Jacobean」，「Gaussian」→「高四／高宣」，「complex」→「Compress／負數」，「uncorrelated」→「uncorreation」，「−π」→「复π／复拍」，「weighting」→「waiting」，「除以」→「處以」，「σ」→「7」（$c$ 唸成「二分之 7」），「e 的」→「1 的」，「Poisson」→「破纵／prozone」，「iterated expectation」→「迭代的期望值」，「自我類化」＝「自我相似」（指高斯線性組合仍是高斯）。以下一律用正確的字。

> **接上一集**：上一集最後預告了平穩性。這一集是 Lec 9-1 的最後一部：定義各種平穩，然後拿通訊最常見的 $a\cos\omega t+b\sin\omega t$ 問「什麼時候嚴格平穩？什麼時候廣義平穩？」，得到一個漂亮的結論：**$a$、$b$ 獨立又要嚴格平穩，只能是高斯**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要平穩](#1-為什麼要平穩)
- [2. 嚴格平穩 SSS](#2-嚴格平穩-sss)
- [3. 聯合平穩](#3-聯合平穩)
- [4. 廣義平穩 WSS](#4-廣義平穩-wss)
- [5. 其他平穩：都是「不隨原點平移而變」](#5-其他平穩都是不隨原點平移而變)
- [6. $a\cos\omega t+b\sin\omega t$ 何時嚴格平穩](#6-acosomega-tbsinomega-t-何時嚴格平穩)
  - [6.1 定理](#61-定理)
  - [6.2 補充：Jacobian 變數變換的條件](#62-補充jacobian-變數變換的條件)
  - [6.3 證明（only if）](#63-證明only-if)
  - [6.4 證明（if）](#64-證明if)
- [7. 何時廣義平穩](#7-何時廣義平穩)
  - [7.1 $a\cos\omega t+b\sin\omega t$](#71-acosomega-tbsinomega-t)
  - [7.2 $A\cos(\omega t+\varphi)$](#72-acosomega-tvarphi)
  - [7.3 $Ae^{j(\omega t+\varphi)}$](#73-aejomega-tvarphi)
- [8. 獨立又嚴格平穩 ⇒ 高斯](#8-獨立又嚴格平穩--高斯)
  - [8.1 證明 $a$、$b$ 是高斯](#81-證明-ab-是高斯)
  - [8.2 證明 $X(t)$ 是高斯過程](#82-證明-xt-是高斯過程)
- [9. 相關時間](#9-相關時間)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| SSS、聯合平穩、WSS | [▶ 01:31](https://youtu.be/CsYOZMqQBEQ?t=91) | 式 (9-47)–(9-56)，pp. 387–388 |
| 其他平穩 | [▶ 08:56](https://youtu.be/CsYOZMqQBEQ?t=536) | p. 392 |
| $a\cos\omega t+b\sin\omega t$ 嚴格平穩 | [▶ 12:35](https://youtu.be/CsYOZMqQBEQ?t=755) | Example 9-13，式 (9-66)，p. 391 |
| 廣義平穩的條件 | [▶ 28:26](https://youtu.be/CsYOZMqQBEQ?t=1706) | 式 (9-63)、Example 9-14，pp. 390–392 |
| 獨立 + SSS ⇒ 高斯 | [▶ 35:05](https://youtu.be/CsYOZMqQBEQ?t=2105) | Corollary，p. 391 |
| 相關時間 | [▶ 49:25](https://youtu.be/CsYOZMqQBEQ?t=2965) | 式 (9-58)，p. 389 |

---

## 1. 為什麼要平穩

[▶ 00:00](https://youtu.be/CsYOZMqQBEQ?t=0)【口頭】

- 設計手機時，要傳的資訊、要對付的雜訊都是隨機過程。設計是根據它們的**統計特性**。
- 如果設計時用的統計特性，和賣給使用者後實際使用時的統計特性不一樣，這個設計就很奇怪。
- 所以要假設兩個時間的統計特性一樣——這就是**平穩** (stationary)。實際上也蠻符合狀況。

---

## 2. 嚴格平穩 SSS

[▶ 01:31](https://youtu.be/CsYOZMqQBEQ?t=91)

> **嚴格平穩** (strict-sense stationary，SSS)：隨機過程的統計性質 **invariant to a shift of the origin**（不隨原點平移而改變）。也就是 $X(t)$ 和 $X(t+c)$ 對任何 $c$ 有相同的統計。

- **原點** (origin) 是座標的基準點。例：今年 1 月開始設計，基準點設在 1 月；3 月出貨，使用者從 3 月開始當新原點。兩個原點下的統計特性一樣，手機就沒問題。數學上就是**座標平移**。
- 它跟時間無關，但又要看時間，所以說「不隨時間座標的原點平移而改變」。

**它有多嚴格？** [▶ 03:09](https://youtu.be/CsYOZMqQBEQ?t=189)

- 定義說的是**所有**統計特性，不只是有限維聯合分布，**也包含無限維的**。
- 例如第 4 集的「時間 0 到 1 之間發生過的最小值」：平移之後也要一樣。
- 要看這麼多統計特性，一定要回到機率空間。所以實作上很難驗證。
- 老師說後面某個證明會用機率空間來證嚴格的性質，你會發現有機率空間時證明比較可行。

【課本補充】Papoulis 式 (9-47)–(9-49)，p. 387：SSS 的 $n$ 階密度滿足
$$f(x_1,\dots,x_n;t_1,\dots,t_n)=f(x_1,\dots,x_n;t_1+c,\dots,t_n+c)\quad\text{對任何 }c.$$
所以一階密度與 $t$ 無關：$f(x;t)=f(x)$；二階密度只跟 $\tau=t_1-t_2$ 有關：$f(x_1,x_2;t_1,t_2)=f(x_1,x_2;\tau)$（取 $c=-t_2$）。

---

## 3. 聯合平穩

[▶ 05:16](https://youtu.be/CsYOZMqQBEQ?t=316)

> **聯合平穩** (jointly stationary)：兩個過程 $X(t)$、$Y(t)$ 的聯合統計，和 $X(t+c)$、$Y(t+c)$ 的聯合統計一樣，對任何 $c$。

- 兩個參數之間的相關性在 big data 裡很重要；過去主要看輸入和輸出的相關性。
- 所有平穩的定義都用同一句藍字：**invariant to a shift of the origin**。這是大家公認比較合理、完整的定義。
- **綠框**：複數過程 $Z(t)=X(t)+jY(t)$ 是（嚴格）平穩，若 $X(t)$、$Y(t)$ 聯合平穩。「strict sense」常被省略，單講 stationary 就是嚴格的。

---

## 4. 廣義平穩 WSS

[▶ 06:18](https://youtu.be/CsYOZMqQBEQ?t=378) 實作上不需要這麼嚴格。

> **廣義平穩** (wide-sense stationary，WSS；也叫 weakly stationary，弱平穩)：**平均函數和自相關函數** invariant to a shift of the origin。

- 只關心一階、二階動差，也就是能量的影響。

**等價條件**（綠框，由定義推出）：

> $X(t)$ 是 WSS **⇔** $E[X(t)]=\eta$（常數）**且** $R(t_1,t_2)$ 只跟 $\tau=t_1-t_2$ 有關：$R(t_1,t_2)=R(\tau)$。

推導：

- 平均不隨原點改變 → 每個時間的平均都一樣 → 常數。
- 自相關不隨原點改變 → 把每個參數都減 $t_2$（換基準點）：$R(t_1,t_2)=R(t_1-t_2,0)$，只跟時間差有關。

老師說【口頭】：大學部通訊原理用的定義可能是綠框這個（只跟時間差有關），直接當定義也對，但看不到平穩的**基本精神**——不隨時間改變。過幾年什麼都忘了，記得「穩態就是不隨時間改變」，其他都推得出來。

> **聯合 WSS** (jointly WSS)：兩個過程各自 WSS，而且互相關（老師說：平均和互相關）不隨原點平移而變，即 $R_{XY}(t_1,t_2)=R_{XY}(\tau)$。

【課本補充】Papoulis 式 (9-50)–(9-56)，p. 388：

- $E\{X(t)\}=\eta$（9-50）；$E\{X(t+\tau)X^*(t)\}=R(\tau)$（9-51）。
- $E\{|X(t)|^2\}=R(0)$：平穩過程的**平均功率與 $t$ 無關**，等於 $R(0)$。
- $C(\tau)=R(\tau)-|\eta|^2$（9-54），$r(\tau)=C(\tau)/C(0)$（9-55）。
- Example 9-11：$R(\tau)=Ae^{-\alpha|\tau|}$，則 $E\{[X(8)-X(5)]^2\}=R(0)+R(0)-2R(3)=2A-2Ae^{-3\alpha}$。
- p. 390：SSS ⇒ WSS（由 (9-48)、(9-49)）；反之一般不成立，但**常態過程例外**：常態 WSS 過程的特性函數 (9-60) 只依賴 $t_i-t_k$，不隨原點平移而變，所以是 SSS。

---

## 5. 其他平穩：都是「不隨原點平移而變」

[▶ 08:56](https://youtu.be/CsYOZMqQBEQ?t=536) 文獻上有各種平穩，基本意義都一樣。學會之後，必要時你可以定義自己的平穩。

| 名稱 | 什麼不隨原點平移而變 |
|---|---|
| **協方差平穩** (covariance stationarity) | 自協方差 $C(t_1,t_2)$。不在乎平均飄動時用 |
| **$N$ 階平穩** ($N$th-order stationarity) | 任取 $n\le N$ 個時間的樣本的聯合統計；$N+1$ 不保證 |
| **區間內平穩** (stationarity in an interval) | 平移後所有樣本時間仍在同一個區間內時，統計一樣 |
| **漸近平穩** (asymptotic stationarity) | $X(t+c)$ 在 $c\to\infty$ 時的統計（去掉暫態 transient 後） |

- **$N$ 階**：取兩個時間 $X(t_1),X(t_2)$ 叫二階（所以自相關是二階統計）；取三個叫三階。論文寫「$N$th order」就很清楚它要什麼。
- **區間內**：通訊裝置用三個月，只要保證三個月內穩態。量河川流量，春夏秋冬不一樣，不能拿春天的統計討論冬天；春天這段是平穩的，到夏天換成流量更大的統計。
- **漸近**：例如上一集的半隨機電報訊號。

【課本補充】Papoulis p. 392：

- 協方差平穩 ⇒ 中心化過程 $\tilde{X}(t)=X(t)-\eta(t)$ 是 WSS（式 (9-70)）。
- 另有**平穩增量** (stationary increments)：$Y(t)=X(t+h)-X(t)$ 對每個 $h$ 是平穩過程。Poisson 過程是例子。

---

## 6. $a\cos\omega t+b\sin\omega t$ 何時嚴格平穩

### 6.1 定理

[▶ 12:35](https://youtu.be/CsYOZMqQBEQ?t=755) 學過通訊原理就認得：這是**通訊傳輸的基本樣式**。用 $\cos$、$\sin$ 兩個載波把 $a$、$b$ 送出去。$a$、$b$ 是要送的訊息（隨機變數），$\omega$ 是常數。

> **定理**：$X(t)=a\cos\omega t+b\sin\omega t$ 是 SSS **⇔** $(a,b)$ 的聯合密度是**圓對稱** (circularly symmetric)：
> $$f(a,b)=f\left(\sqrt{a^2+b^2}\right).$$

- 圓對稱：把 PDF 畫在二維平面上（第三維是密度），它對 $z$ 軸完全對稱，怎麼旋轉都不變。
- **意義**【口頭】：要讓載波送出去的訊號嚴格平穩，$\cos$ 軸和 $\sin$ 軸的訊號在統計上要對 $z$ 軸完全對稱。反過來，只要有一點不對稱，就絕對不是嚴格平穩（因為是 if and only if）。

### 6.2 補充：Jacobian 變數變換的條件

[▶ 17:40](https://youtu.be/CsYOZMqQBEQ?t=1060) 證明要用到大一微積分的變數變換。研究所階段要注意**每個定理的條件**，證明、做研究時才不會出錯。

> **定理（變數變換）**：$X$ 的密度的支撐集 (support) 是**開集** $U$。$g:U\to V$ 一對一、**連續可微** (continuously differentiable)，則 $V$ 是開集，反函數 $T=g^{-1}$ 也連續可微。若 Jacobian
> $$J_T(\mathbf{y})=\det\begin{pmatrix}\partial T_1/\partial y_1&\partial T_1/\partial y_2\\\partial T_2/\partial y_1&\partial T_2/\partial y_2\end{pmatrix}\ne 0,$$
> 則 $Y=g(X)$ 的密度為
> $$f_Y(\mathbf{y})=f_X\left(T(\mathbf{y})\right)\left|J_T(\mathbf{y})\right|.$$

- 定義在**開集**上：閉集在證明上會出問題。
- **連續可微**：要可微，而且微分後連續。如果可微但微分不連續，用了結果會有問題。
- Jacobian **不能是 0**。
- 開集聽起來很嚴格，其實**對密度沒有限制**：密度少一點、多一點（測度 0 的集合）沒關係。

**例：極座標** [▶ 21:43](https://youtu.be/CsYOZMqQBEQ?t=1303)

$$f_X(x_1,x_2)=\frac{1}{2\pi}e^{-(x_1^2+x_2^2)/2}\quad\text{（圓對稱）}$$

換成極座標：$y_1=\sqrt{x_1^2+x_2^2}$（半徑），$y_2=\tan^{-1}(x_2/x_1)$（角度）。

1. 一對一、連續可微都沒問題。
2. 要開集、Jacobian 不為 0：老師把**兩條線拿掉**，讓半徑一定 $>0$、角度不會落在 $0$ 或 $2\pi$ 的端點，於是 support 是開集。拿掉兩條線對密度沒影響，總積分還是 1。
3. 反函數：$x_1=y_1\cos y_2$，$x_2=y_1\sin y_2$。
4. Jacobian：
$$J_T=\det\begin{pmatrix}\cos y_2&-y_1\sin y_2\\\sin y_2&y_1\cos y_2\end{pmatrix}=y_1\cos^2y_2+y_1\sin^2y_2=y_1.$$
   在 support 上 $y_1>0$，所以不為 0（因為刻意把那一點拿掉了）。
5. 所以 $f_Y(y_1,y_2)=\frac{1}{2\pi}e^{-y_1^2/2}\,y_1$。

### 6.3 證明（only if）

[▶ 14:36](https://youtu.be/CsYOZMqQBEQ?t=876) 設 $X(t)$ 是 SSS，證 $f(a,b)$ 圓對稱。這裡**沒有機率空間**，只能用原來的性質證。

**Step 1：取兩個時間的樣本。** 取 $0$ 和 $\frac{\pi}{2\omega}$：
$$X(0)=a,\qquad X\left(\tfrac{\pi}{2\omega}\right)=a\cos\tfrac{\pi}{2}+b\sin\tfrac{\pi}{2}=b.$$
老師說這是刻意的技巧，讓樣本向量剛好是 $(a,b)$。

**Step 2：平移 $t$ 之後再取同樣的兩個時間。**
$$X(t)=a\cos\omega t+b\sin\omega t,\qquad X\left(t+\tfrac{\pi}{2\omega}\right)=b\cos\omega t-a\sin\omega t.$$

**Step 3：嚴格平穩 → 兩組樣本的聯合密度一樣。** 令 $\mathbf{x}=(a,b)$，$\mathbf{y}=\left(X(t),X(t+\frac{\pi}{2\omega})\right)$，兩者密度相同。

**Step 4：$\mathbf{y}$ 是 $\mathbf{x}$ 的旋轉。**
$$\mathbf{y}=\begin{pmatrix}\cos\omega t&\sin\omega t\\-\sin\omega t&\cos\omega t\end{pmatrix}\mathbf{x}.$$
這是線性映射，一定連續可微，旋轉矩陣的行列式是 1，所以由 Jacobian 公式 $f_Y(\mathbf{y})=f_X(T(\mathbf{y}))\cdot 1$。

**Step 5：** $f_Y=f_X$（Step 3），所以 $f_X(T(\mathbf{y}))=f_X(\mathbf{y})$：**旋轉任意角度 $\omega t$ 之後，密度的值完全一樣**。所以 $f(a,b)$ 是圓對稱。 ∎

**直覺**【口頭】：這個訊號其實在 $xy$ 平面上繞 $z$ 軸一直旋轉（$\omega$ 是常數、$t$ 一直變）。因為嚴格平穩，旋轉時**完全看不出來**——形狀完全不變，你以為它沒在轉，但它其實在轉。這才叫穩態。

### 6.4 證明（if）

[▶ 25:54](https://youtu.be/CsYOZMqQBEQ?t=1554) 設 $f(a,b)$ 圓對稱，證 $X(t)$ 是 SSS。

1. 定義平移 $\tau$ 後的過程：
$$X_1(t)=X(t+\tau)=a_1\cos\omega t+b_1\sin\omega t,$$
$$a_1=a\cos\omega\tau+b\sin\omega\tau,\qquad b_1=b\cos\omega\tau-a\sin\omega\tau.$$
2. $(a_1,b_1)$ 是 $(a,b)$ 旋轉 $\omega\tau$。圓對稱的密度旋轉後看不出來，所以 $(a,b)$ 和 $(a_1,b_1)$ 的聯合密度**完全一樣**。
3. $X(t)$ 的統計完全由 $(a,b)$ 的聯合密度決定（再乘上確定的函數 $\cos\omega t$、$\sin\omega t$）；$X_1(t)$ 由 $(a_1,b_1)$ 決定，形式一樣。
4. 所以 $X(t)$ 和 $X(t+\tau)$ 統計完全相同，對每個 $\tau$。 ∎

老師說【口頭】：完全沒用機率空間，就得到一個很重要的結果。通訊原理通常只教廣義平穩，這裡教嚴格平穩，條件更嚴：要求 PDF 圓對稱。

【課本補充】Papoulis Example 9-13，式 (9-66)，p. 391，證法相同。課本先指出兩種平穩都**必須** $E\{a\}=E\{b\}=0$（式 (9-62)），因為平均 $E\{a\}\cos\omega t+E\{b\}\sin\omega t$ 要與 $t$ 無關。

---

## 7. 何時廣義平穩

[▶ 28:26](https://youtu.be/CsYOZMqQBEQ?t=1706) 嚴格平穩實作上難維持，也沒必要；一般只關心能量（二階動差）。

### 7.1 $a\cos\omega t+b\sin\omega t$

**老師的敘述**：若 $a$、$b$ **不相關、零平均**，則 $X(t)$ 是 WSS。

證明（只需驗證）：

- 零平均 → $E[X(t)]=0$，常數。
- 二階動差（實數，共軛可拿掉）照算，結果只跟 $t_1-t_2$ 有關。

**來源衝突，兩邊都寫**：Papoulis 式 (9-63)、(9-64)（p. 390）的條件多一個**等變異數**：

> $X(t)$ 是 WSS **⇔** $E\{ab\}=0$ **且** $E\{a^2\}=E\{b^2\}=\sigma^2$（在 $E\{a\}=E\{b\}=0$ 之下）。此時 $R(\tau)=\sigma^2\cos\omega\tau$。

以下**不是逐字稿內容**，是依課本 (9-65) 的計算補的：展開
$$E[X(t+\tau)X(t)]=E\{a^2\}\cos\omega(t+\tau)\cos\omega t+E\{b^2\}\sin\omega(t+\tau)\sin\omega t+E\{ab\}\sin\omega(2t+\tau).$$
若 $E\{a^2\}=E\{b^2\}=\sigma^2$、$E\{ab\}=0$，前兩項合成 $\sigma^2\cos\omega\tau$；若 $E\{a^2\}\ne E\{b^2\}$，會多出 $\frac{E\{a^2\}-E\{b^2\}}{2}\cos\omega(2t+\tau)$，跟 $t$ 有關，就不是 WSS。所以等變異數是必要的。

⚠️ 待確認：老師口頭只說「uncorrelated、zero mean」，投影片上是否也有等變異數，逐字稿無法確定。

老師留的思考題：反過來（WSS ⇒ $a,b$ 零平均、不相關）對不對？回去自己練習。（課本的答案：加上等變異數後是 if and only if。）

### 7.2 $A\cos(\omega t+\varphi)$

[▶ 30:29](https://youtu.be/CsYOZMqQBEQ?t=1829) 通訊上也會產生 $A\cos(\omega t+\varphi)$，$A$ 是常數。這是 **FM**（頻率調變，資訊載在頻率）或 **PM**（相位調變，資訊載在相位）：$\omega$、$\varphi$ 是隨機變數（例如來的流量是 Poisson）。

> 若 $\varphi$ 在 $(-\pi,\pi)$ **均勻分布**（且和 $\omega$ 獨立），則 $X(t)=A\cos(\omega t+\varphi)$ 是 WSS，平均 0，
> $$R(\tau)=\frac{A^2}{2}E\{\cos\omega\tau\}.$$

- 學到的：條件**跟 $\omega$ 的分布無關**，只要 $\varphi$ 均勻。（老師說 $\varphi$ 和 $\omega$「基本上要有一點點關係」——課本的條件是兩者**獨立**。）

**證明：**

**一階**：用**疊代期望值** (iterated expectation)。先固定 $\omega$ 為某個值，對 $\varphi$ 取期望值：
$$E[X(t)]=E\left\{E\left[A\cos(\omega t+\varphi)\mid\omega\right]\right\}=E\left\{\frac{A}{2\pi}\int_{-\pi}^{\pi}\cos(\omega t+\varphi)\,d\varphi\right\}=0.$$
（均勻相位走一整圈，平均一定是 0。）

**二階**：用積化和差 $\cos A\cos B=\frac12\cos(A+B)+\frac12\cos(A-B)$：
$$X(t_1)X(t_2)=\frac{A^2}{2}\left[\cos\left(\omega(t_1+t_2)+2\varphi\right)+\cos\omega(t_1-t_2)\right].$$
第一項含 $2\varphi$，$2\varphi$ 在長度 $4\pi$ 的區間（兩個週期）上均勻，期望值是 0。所以
$$R(t_1,t_2)=\frac{A^2}{2}E\{\cos\omega(t_1-t_2)\},$$
只跟時間差有關，不管 $\omega$ 的分布。 ∎

老師說：相位要很穩、每個相位都有。這樣的訊號不是我們希望做出來的，但這是一個條件。思考題：反過來（WSS ⇒ $\varphi$ 一定均勻）對嗎？老師說答案比較傾向否定，要舉反例。

【課本補充】Papoulis Example 9-14，式 (9-67)–(9-69)，pp. 391–392：$R(\tau)=\frac{a^2}{2}E\{\cos\omega\tau\}=\frac{a^2}{2}\text{Re}\,\Phi_\omega(\tau)$，$\Phi_\omega$ 是 $\omega$ 的特性函數。

### 7.3 $Ae^{j(\omega t+\varphi)}$

[▶ 33:33](https://youtu.be/CsYOZMqQBEQ?t=2013) 複數訊號。證明一樣，不再做（老師說再做一次有點 boring）。

> 若 $\varphi$ 在 $(-\pi,\pi)$ 均勻（且和 $\omega$ 獨立），則 $Z(t)=Ae^{j(\omega t+\varphi)}$ 是 WSS，平均 0。

- 如果 $\varphi$ 不是在 $(-\pi,\pi)$，例如只在 $\pm 20°$，可能就不是。舉個反例就知道。
- 思考題：是不是 if and only if？老師說應該不算，要舉反例。

【課本補充】Papoulis p. 392：$E\{Z(t+\tau)Z^*(t)\}=A^2E\{e^{j\omega\tau}\}=A^2\Phi_\omega(\tau)$。

**總結**【口頭】：怎麼造出嚴格或弱平穩的通訊訊號？**兩軸（$\cos$ 軸、$\sin$ 軸）要平衡**。非常平衡（PDF 圓對稱）就嚴格平穩；一階、二階平衡就弱平穩。

---

## 8. 獨立又嚴格平穩 ⇒ 高斯

[▶ 35:05](https://youtu.be/CsYOZMqQBEQ?t=2105)

注意：圓對稱**不代表**獨立。可以做出 $a$、$b$ 相依、但 PDF 圓對稱的例子。現在**多加一個條件**：

> **推論**：若 $X(t)=a\cos\omega t+b\sin\omega t$ 是 SSS，**而且 $a$、$b$ 獨立**，則 $a$、$b$ 一定是**常態**（高斯）。

- 非常漂亮的結果：只有高斯能讓 $a$、$b$ 獨立又嚴格平穩，別的分布絕對做不到。這也是高斯重要的原因之一。【口頭】

### 8.1 證明 $a$、$b$ 是高斯

已知 SSS ⇔ 圓對稱，所以只剩證高斯。老師說：證明時每個條件都要拿來用，額外的條件是**獨立**。

**Step 1：兩個條件合起來。** 獨立 → 聯合密度是乘積；圓對稱 → 只跟半徑 $r=\sqrt{a^2+b^2}$ 有關：
$$f_a(a)\,f_b(b)=g(r).$$

**Step 2：對 $a$ 偏微分。** 右邊用連鎖律，$\frac{\partial r}{\partial a}=\frac12(a^2+b^2)^{-1/2}\cdot 2a=\frac{a}{r}$：
$$f_a'(a)\,f_b(b)=g'(r)\,\frac{a}{r}.$$

**Step 3：兩邊除以 $f_a(a)f_b(b)=g(r)$**（$f_b$ 消掉）：
$$\frac{1}{a}\cdot\frac{f_a'(a)}{f_a(a)}=\frac{1}{r}\cdot\frac{g'(r)}{g(r)}.$$

**Step 4：右邊一定是常數。** 對 $b$ 做同樣的事，得 $\frac{1}{b}\frac{f_b'(b)}{f_b(b)}=\frac1r\frac{g'(r)}{g(r)}$。所以
$$\frac{1}{a}\frac{f_a'(a)}{f_a(a)}=\frac{1}{b}\frac{f_b'(b)}{f_b(b)}\quad\text{對所有 }a,b.$$
左邊只跟 $a$ 有關、右邊只跟 $b$ 有關，兩者對所有 $a,b$ 相等，所以都等於同一個常數 $c$。

（老師的論證方式：代 $a=\alpha$、$b=\beta$，再對調成 $a=\beta$、$b=\alpha$。$r=\sqrt{\alpha^2+\beta^2}$ 不變，所以右邊一樣，左邊也必須一樣；不可能不等，所以是常數。上面的寫法是把同一個想法寫完整。）

**Step 5：解微分方程。**
$$\frac{g'(r)}{g(r)}=c\,r\ \Rightarrow\ \ln g(r)=\frac{c}{2}r^2+\text{const}\ \Rightarrow\ g(r)=K\,e^{cr^2/2}.$$
同樣 $f_a(a)\propto e^{ca^2/2}$。

**Step 6：常數一定是負的。** 若 $c=0$，$g$ 是常數，積分爆到無限大；若 $c>0$，$e^{cr^2/2}$ 也爆掉。密度的總積分必須是 1（有限），所以 $c<0$，記 $c=-\frac{1}{\sigma^2}$：
$$g(r)=\frac{1}{2\pi\sigma^2}e^{-r^2/(2\sigma^2)},\qquad f_a(a)=\frac{1}{\sqrt{2\pi}\sigma}e^{-a^2/(2\sigma^2)}.$$
（常數 $\frac{1}{2\pi\sigma^2}$ 由總積分為 1 決定。）所以 $a$、$b$ 是零平均、同變異數的獨立高斯，也就是聯合高斯。

**學到的觀念**【口頭】：**一個函數的微分除以自己，再乘 $\frac1r$，如果是常數，它就是高斯**。所以要證明高斯時，可以看這個形式；它不是巧合。老師說：重要的是看完數學抓到觀念，然後把數學忘掉，這才是高手。

### 8.2 證明 $X(t)$ 是高斯過程

[▶ 44:19](https://youtu.be/CsYOZMqQBEQ?t=2659) 還沒證完！上面只證了 $(a,b)$ 聯合高斯，還沒證 $X(t)$ 是**高斯過程**。

回到 Papoulis 的定義（第 6 集）：任何有限維樣本聯合高斯。老師說這時候課本的定義就有用了；用 Haykin 或 Proakis 的定義，這裡可能比較難證。

1. 取 $k$ 個時間 $t_1,\dots,t_k$：
$$X(t_i)=a\cos\omega t_i+b\sin\omega t_i,\qquad i=1,\dots,k.$$
2. 每個 $X(t_i)$ 都是 $a$、$b$ 的**線性組合**，只是加權不同。
3. **聯合高斯的線性組合還是聯合高斯**。所以 $(X(t_1),\dots,X(t_k))$ 聯合高斯。 ∎

【課本補充】Papoulis Corollary（p. 391）：證明「由 (9-66) 和 (6-31) 得到」，一句帶過。

---

## 9. 相關時間

[▶ 49:25](https://youtu.be/CsYOZMqQBEQ?t=2965) 第 9-1 節的最後一張投影片。用**一個量**說明相關的程度。

> **相關時間** (correlation time)：對 WSS 過程，
> $$\tau_c=\frac{1}{C(0)}\int_0^{\infty}C(\tau)\,d\tau.$$

**例：a-dependent 的 WSS 過程**（$|\tau|>a$ 時 $C(\tau)=0$）：

1. $\tau_c=\frac{1}{C(0)}\int_0^{a}C(\tau)\,d\tau\le\int_0^{a}\frac{|C(\tau)|}{C(0)}\,d\tau$。
2. 協方差最大在 0：$|C(\tau)|\le C(0)$，所以被積函數 $\le 1$。
3. 所以 $\tau_c\le a$。超過 $a$ 就沒關係了，算出來的相關時間比 $a$ 小。

用途【口頭】：隨機過程那麼長，比較不同過程的相關強弱需要一個基準量。例如一個算出 1.8、一個算出 1.9，就可以比較。這只是一種定義方法，給大家參考。

【課本補充】Papoulis 式 (9-57)–(9-59)，p. 389：

- WSS 白雜訊：$C(\tau)=q\,\delta(\tau)$（9-57）。
- a-dependent 時，常數 $a$ 就叫相關時間；(9-58) 是推廣到一般過程的定義。
- 大多數規則的過程：$C(\tau)\to 0$、$R(\tau)\to|\eta|^2$（$|\tau|\to\infty$）。
- Example 9-12：$\mathbf{s}=\int_{-T}^{T}X(t)\,dt$，$\sigma_s^2=\int_{-2T}^{2T}(2T-|\tau|)C(\tau)\,d\tau$（9-59）；若 $a\ll T$，$\sigma_s^2\approx 2T\int_{-a}^{a}C(\tau)\,d\tau$，所以 a-dependent 過程可以用 $q=\int_{-a}^{a}C(\tau)\,d\tau$ 的白雜訊代替。

---

## 10. 一頁速查表

### 平穩的種類

| 名稱 | 條件 |
|---|---|
| SSS | 所有統計不隨原點平移變；$f(x;t)=f(x)$，$f(x_1,x_2;t_1,t_2)=f(x_1,x_2;\tau)$ |
| WSS | $E[X(t)]=\eta$，$R(t_1,t_2)=R(\tau)$；$E\lvert X(t)\rvert^2=R(0)$ |
| 聯合 WSS | 各自 WSS 且 $R_{XY}(t_1,t_2)=R_{XY}(\tau)$ |
| 協方差平穩 | $C(t_1,t_2)=C(\tau)$ ⇒ $X-\eta$ 是 WSS |
| $N$ 階 | $n\le N$ 階密度平移不變 |
| 區間內 | 平移後仍在區間內時不變 |
| 漸近 | $c\to\infty$ 時 $X(t+c)$ 統計趨於不依賴 $c$ |

- SSS ⇒ WSS；反之不成立，但**常態 WSS ⇒ SSS**。

### $a\cos\omega t+b\sin\omega t$

- 必要：$E\{a\}=E\{b\}=0$。
- **SSS ⇔ $f(a,b)$ 圓對稱**。關鍵：取 $t=0$、$\frac{\pi}{2\omega}$ 得 $(a,b)$；平移 $t$ 得 $(a,b)$ 旋轉 $\omega t$，Jacobian 為 1。
- **WSS ⇔ $E\{ab\}=0$、$E\{a^2\}=E\{b^2\}$**（課本）；$R(\tau)=\sigma^2\cos\omega\tau$。
- **SSS + $a,b$ 獨立 ⇒ 高斯**。關鍵：$f_a(a)f_b(b)=g(r)$ → $\frac{f_a'}{af_a}=\frac{g'}{rg}=c$ → $g=Ke^{cr^2/2}$，$c=-1/\sigma^2<0$。

### 相位隨機的訊號

- $A\cos(\omega t+\varphi)$，$\varphi\sim U(-\pi,\pi)$ 與 $\omega$ 獨立 → WSS，$R(\tau)=\frac{A^2}{2}E\{\cos\omega\tau\}$。關鍵：$\cos(\cdot+2\varphi)$ 期望值 0。
- $Ae^{j(\omega t+\varphi)}$ → WSS，$R(\tau)=A^2E\{e^{j\omega\tau}\}$。

### 其他

- Jacobian 公式：$f_Y(\mathbf{y})=f_X(T(\mathbf{y}))|J_T(\mathbf{y})|$，條件：開集、一對一、連續可微、$J\ne 0$。極座標 $J=r$。
- 相關時間 $\tau_c=\frac{1}{C(0)}\int_0^\infty C(\tau)d\tau$；a-dependent 時 $\tau_c\le a$。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| WSS、$R(\tau)$ | 下一集起：§9-2 系統的隨機輸入；§9-3 功率頻譜 $S(\omega)=\int R(\tau)e^{-j\omega\tau}d\tau$ |
| $A\cos(\omega t+\varphi)$、$a\cos\omega t+b\sin\omega t$ | §10-3 調變（第 16–18 集） |
| 漸近平穩、平穩增量 | 循環平穩過程（§10-4，第 19 集） |
| 嚴格平穩要用機率空間證 | 遍歷性（第 30–33 集） |
| 相關時間、a-dependent ≈ 白雜訊 | 遍歷性、頻譜估計的變異數 |

---

## 附：本集一句話總結

> **所有平穩都是「統計不隨原點平移而變」，差別只在看哪些統計；通訊訊號 $a\cos\omega t+b\sin\omega t$ 嚴格平穩 ⇔ $(a,b)$ 的密度圓對稱，廣義平穩 ⇔ 不相關且等變異數，而若 $a$、$b$ 還要獨立，唯一可能就是高斯。**

---

## ⚠️ 待確認清單

1. [▶ 28:57](https://youtu.be/CsYOZMqQBEQ?t=1737) $a\cos\omega t+b\sin\omega t$ 為 WSS 的條件：老師口頭只說「不相關、零平均」，課本 (9-63) 多「等變異數」（數學上必要）；投影片是否有寫，待確認。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-1 (7/7) 錄影逐字稿（whisper large-v3-turbo，51:32）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
