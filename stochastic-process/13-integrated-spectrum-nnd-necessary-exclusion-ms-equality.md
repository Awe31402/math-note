---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 13
lecture: Lec 9-3 General Concepts — The Power Spectrum (2/3)
date: 待補
video: https://youtu.be/b5m94_2EjK0
notes: Papoulis & Pillai 4th ed. §9-3（Integrated spectrum 式 (9-167)、(9-168)，p. 417；Properties of correlations、Pólya's criterion、Theorem 9-5、Continuity、Example 9-30，式 (9-173)–(9-177)，pp. 418–419；MS continuity and periodicity、cross-correlation bound，式 (9-178)–(9-181)，pp. 419–420）；§9-1 MS equality 式 (9-1)，p. 375；MS periodicity、Theorem 9-1，式 (9-71)–(9-73)，pp. 392–393
---

# 第 13 集 · Lec 9-3 (2/3)：積分頻譜與 Riemann–Stieltjes 積分、非負定 ⇔ 非負頻譜、自相關的必要條件排除法、互頻譜的界、均方相等與均方週期 [▶ 影片](https://youtu.be/b5m94_2EjK0)

← 上一集：[12](12-power-spectrum-doppler-transfer-function-hilbert-wiener-khinchin.md) ｜ [總目錄](README.md) ｜ 下一集：[14](14-ms-periodicity-continuity-differentiability-integrability.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 13 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（48:57，whisper large-v3-turbo）＋ Papoulis §9-3（pp. 417–420）、§9-1（pp. 375、392–393）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Riemann–Stieltjes」→「Weyman-Steel-T's／Reimann Astilty」，「Riemann」→「Reiman／Ryman／李曼」，「Lebesgue」→「The Basque」，「Billingsley」→「Billions里」，「Probability and Measure」→「Probability and Major」，「實變（分析）」→「十變／十遍分析」，「nonnegative definite」→「non-negi definite／non-negative definition／deafening」，「Wiener–Khinchin」→「Weiner-Kinchen」，「傅立葉轉換」→「複裂轉換／复理准分／fluoration form」，「autocorrelation」→「autochromic／autoclinic／autocolline／autoclonal function」，「necessary exclusion」→「necessary exclusion／Occlusion／inclusion」，「Pólya」→「Polya」，「Cauchy–Schwarz inequality」→「Culti-Swagic Equality／Culture Swartz／Colchus-Watt／Colch-Swagin」，「實部／虛部」→「實步／虛步」，「complex conjugate」→「complete conjugate」，「mean square」→「mean square」，「interpolation」→「interpretation」，「量度」→「良度」，「wide-sense stationary」→「wise and stationary／Wisen Station」，「probability space」→「Provice-based／Private Space／Probability-based」。以下一律用正確的字。

> **接上一集**：上一集定義了功率頻譜，證明它非負（Wiener–Khinchin），並說明任何非負可積函數都是某個訊號的頻譜。這一集把幾件事串起來：**非負定 ⇔ 非負頻譜**；然後學怎麼判斷一個函數「不可能是自相關」（必要條件排除法），最後為下一章釐清「隨機過程相等、週期」是什麼意思。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 積分頻譜與 Riemann–Stieltjes 積分](#1-積分頻譜與-riemannstieltjes-積分)
- [2. 非負定 ⇔ 非負頻譜](#2-非負定--非負頻譜)
- [3. 判斷一個函數是不是自相關](#3-判斷一個函數是不是自相關)
  - [3.1 必要條件排除法](#31-必要條件排除法)
  - [3.2 充分條件：Pólya 判準](#32-充分條件pólya-判準)
  - [3.3 必要條件一：有一點等於 $R(0)$ ⇒ 週期](#33-必要條件一有一點等於-r0--週期)
  - [3.4 必要條件二：原點連續 ⇒ 處處連續](#34-必要條件二原點連續--處處連續)
  - [3.5 例：截斷拋物線不是自相關](#35-例截斷拋物線不是自相關)
- [4. 互頻譜的界](#4-互頻譜的界)
- [5. 隨機過程「相等」是什麼意思：均方相等](#5-隨機過程相等是什麼意思均方相等)
  - [5.1 均方相等](#51-均方相等)
  - [5.2 每個時間各自成立 vs 所有時間同時成立](#52-每個時間各自成立-vs-所有時間同時成立)
- [6. 均方週期](#6-均方週期)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 積分頻譜、Riemann–Stieltjes | [▶ 00:00](https://youtu.be/b5m94_2EjK0?t=0) | 式 (9-167)、(9-168)，p. 417 |
| 非負定 ⇔ 非負頻譜 | [▶ 09:49](https://youtu.be/b5m94_2EjK0?t=589) | 式 (9-173)，p. 418 |
| 必要條件排除、Pólya | [▶ 13:58](https://youtu.be/b5m94_2EjK0?t=838) | Theorem 9-5、Example 9-30，pp. 418–419 |
| 互頻譜的界 | [▶ 29:56](https://youtu.be/b5m94_2EjK0?t=1796) | 式 (9-180)、(9-181)，pp. 419–420 |
| 均方相等、均方週期 | [▶ 35:07](https://youtu.be/b5m94_2EjK0?t=2107) | 式 (9-1)、(9-71)–(9-73)、(9-179) |

---

## 1. 積分頻譜與 Riemann–Stieltjes 積分

[▶ 00:00](https://youtu.be/b5m94_2EjK0?t=0) 不是每本書都有，老師講它的物理意義和什麼時候方便。

> **積分頻譜** (integrated spectrum)：功率頻譜的積分
> $$F(\omega)=\int_{-\infty}^{\omega}S(\alpha)\,d\alpha.$$

**類比 PDF 和 CDF**【口頭】：

- 小寫 $f(x)$ 是 PDF，從 $-\infty$ 積到 $u$ 就是大寫的 CDF $F(u)$。
- 老師喜歡先算 CDF（上一集都卜勒的例子就是由 CDF 求 $\omega$ 的密度）。PDF 看得到一些概念，但 **CDF 比較完備**。
- 回到 Billingsley《Probability and Measure》定理 14.1（第 3 集）：給 CDF 就 well-defined，不需要機率空間。
- **積分之後就沒有 delta 函數**。處理密度時有時要引進 delta，使用要很小心；delta 用積分就消除了。看一個函數的積分函數，就完全沒有 delta 的問題。

【課本補充】$S\ge 0$ ⇒ $F(\omega)$ 非遞減。若 $S$ 含 $\beta_i\delta(\omega-\omega_i)$，$F$ 在 $\omega_i$ 有跳躍 $\beta_i$。積分協方差頻譜 $F^c$：$F(\omega)=F^c(\omega)+2\pi\eta^2U(\omega)$。

用積分頻譜，自相關寫成 **Riemann–Stieltjes 積分**：
$$R(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{j\omega\tau}\,dF(\omega)\qquad\text{(9-168)}.$$

**怎麼理解這個記號** [▶ 03:07](https://youtu.be/b5m94_2EjK0?t=187)【口頭】：比較嚴謹的數學很常用，很多同學看了覺得怪。

- **Riemann 積分** $\int f(x)\,dx$：切長條圖，第 $i$ 個長方形高 $f(i\Delta)$、底 $\Delta$；$\Delta\to 0$ 逼近面積。$dx$ 來自 $\Delta x$。
- **Riemann–Stieltjes 積分** $\int f(x)\,dg(x)$：還是用長方形逼近，**高**還是 $f$ 決定，但**底**改成 $g$ 的差：第一個長方形底是 $g(\Delta)-g(0)$，第二個是 $g(2\Delta)-g(\Delta)$……
  $$\int f(x)\,dg(x)=\lim_{\Delta\to0}\sum_if(i\Delta)\left[g(i\Delta)-g((i-1)\Delta)\right].$$
  用非線性的方式逼近。
- 若 $g$ 可微，就和 $\int f(x)g'(x)\,dx$ **一模一樣**。所以 $F$ 可微時 (9-168) 就是原來的反轉換。
- 主要用途：推廣到 $g$ **微分不存在**的情況，只要有差值就能算。
- 老師說他教高等機率論時會出題：給 $f(x)$、$g(x)$，請算 $\int f\,dg$——切長方形，底用 $g$ 的差算，再逼近就好。
- 看到這個記號就想：**很細的長方形逼近，底是那個函數的差**。

老師的教學觀【口頭】：他在美國修了很多數學系的課，數學系老師有時急著證定理，忽略解釋基本的出發點。這門課有些推導省略，花時間解釋觀念可能更持久；以後看嚴謹證明也許還是會卡住，但至少不會完全茫然。

**積分協方差頻譜** (integrated covariance spectrum)：協方差頻譜的積分，同樣用 Riemann–Stieltjes 的方式，避開 delta 函數。

---

## 2. 非負定 ⇔ 非負頻譜

[▶ 09:49](https://youtu.be/b5m94_2EjK0?t=589) 課本叫 PD，老師說應該叫 NND（非負定），一般書是這樣認知的。

把已經證明的結果整理起來（WSS 情形）：

1. **$R(\tau)$ 是自相關 ⇒ $S(\omega)\ge0$**：Wiener–Khinchin（上一集）。不是非負的函數不可能是功率頻譜。
2. **$S(\omega)\ge0$（可積）⇒ 存在過程以它為頻譜**：上一集的引理，造 $Ae^{j(\omega t-\varphi)}$，頻率 $\omega$ 的 PDF 正比於 $S$。PDF 不可能是負的，也說明了頻譜不會是負的。
3. **$R(t_1,t_2)$ 是自相關 ⇔ $R$ 非負定**（第 4 集，不管是否 WSS）。

合起來：

> **定理**：（WSS）$R(\tau)$ 是自相關 ⇔ $R(\tau)$ 非負定 ⇔ 它的傅立葉轉換 $S(\omega)\ge 0$。

- 數學上這是一個很重要的定理：**非負定函數經過傅立葉轉換一定非負，而且是 if and only if**（課本稱為 Bochner 的結果，引用 Bochner《Lectures on Fourier Integrals》）。
- 好處：過去要在時域判斷非負定（很難），現在**做傅立葉轉換看是不是 $\ge0$** 就好，比較簡單。前提是 WSS。

【課本補充】Papoulis p. 418，式 (9-173)：$\sum_{i,j}a_ia_j^*R(\tau_i-\tau_j)\ge0$；「可以證明反過來也對」。

---

## 3. 判斷一個函數是不是自相關

[▶ 13:58](https://youtu.be/b5m94_2EjK0?t=838) 老師說很多老師喜歡考：畫一個（或四五個）波形，請你判斷哪個不是自相關。好幾屆研究所考試都考過。

### 3.1 必要條件排除法

例：畫一個在原點是**最小值**的函數。它一定不是自相關，因為自相關的**最大值一定在原點**（$|R(\tau)|\le R(0)$）。

> **必要條件排除** (necessary exclusion)：「若 $P$ 則 $Q$」⇔「若非 $Q$ 則非 $P$」。若「是自相關 ⇒ 某性質」，那麼「沒有那個性質 ⇒ 不是自相關」。

老師說這在邏輯上常用，例如做演算法加速：把不可能的情況直接排除，速度就快了。他的學生做通訊時也常做這種事，只是不知道它叫 necessary exclusion；用這種方式包裝陳述，會很漂亮。【口頭】

【課本補充】(9-174)：$|R(\tau)|\le\frac{1}{2\pi}\int S(\omega)d\omega=R(0)$（因為 $S\ge0$）。

### 3.2 充分條件：Pólya 判準

[▶ 16:05](https://youtu.be/b5m94_2EjK0?t=965)

> **Pólya 充分判準** (Pólya's sufficient criterion)：若 $R(\tau)$ 在 $\tau>0$ 是 concave（老師與課本的用詞），而且 $\tau\to\infty$ 時趨於有限的極限，則 $R(\tau)$ 非負定（是自相關）。

- **充分**條件：條件成立就保證是，但不包含所有可能。很容易造出不滿足這個條件、卻非負定的函數。條件很強。

【課本補充】Papoulis p. 418 的例子：$w(\tau)=e^{-\alpha|\tau|^c}$，$0<c<1$ 時 $w\to0$ 且 $w''(\tau)>0$（$\tau>0$），所以由 Pólya 判準是 p.d.；而 $1\le c\le 2$ 時也是 p.d.，雖然不滿足這個判準。

⚠️ 待確認：課本例子用的是 $w''>0$，也就是**凸**（convex，向上彎）。標準的 Pólya 判準也是「$\tau>0$ 時**凸**、遞減到有限極限」。老師和課本文字都寫 concave，可能是用詞（凹向上）不同，讀的時候以 $w''\ge 0$ 為準。

### 3.3 必要條件一：有一點等於 $R(0)$ ⇒ 週期

[▶ 17:07](https://youtu.be/b5m94_2EjK0?t=1027)

> **Theorem 9-5**：若 $R(\tau_1)=R(0)$，某個 $\tau_1\ne0$，則 $R(\tau)$ 是週期 $\tau_1$ 的週期函數：$R(\tau+\tau_1)=R(\tau)$，對所有 $\tau$。

**用法**：畫一個函數，在 $\tau_1$ 的值和原點一樣，但後面沒有再出現 → 一定不是自相關。只要有一點和原點一樣，後面就不用再畫了，全部重複。

**證明**：老師說後面二十幾頁所有的證明全部都是 **Cauchy–Schwarz 不等式**：要證自相關的性質就是看二階動差，而二階動差有一個很好的不等式
$$\left|E[ZW^*]\right|^2\le E|Z|^2\,E|W|^2.$$

**Step 1：** 巧妙地取差距 $\tau_1$ 的兩個時間：$Z=X(t+\tau+\tau_1)-X(t+\tau)$，$W=X(t)$：
$$\left|E\left\{\left[X(t+\tau+\tau_1)-X(t+\tau)\right]X^*(t)\right\}\right|^2\le E\left|X(t+\tau+\tau_1)-X(t+\tau)\right|^2\,E|X(t)|^2.$$

**Step 2：** 左邊全部可以寫成自相關：$\left|R(\tau+\tau_1)-R(\tau)\right|^2$。

**Step 3：** 右邊展開平方，三項：
$$E\left|X(s+\tau_1)-X(s)\right|^2=R(0)-R(\tau_1)-R(-\tau_1)+R(0)=2R(0)-2\,\text{Re}\,R(\tau_1).$$
（$R(-\tau_1)=R^*(\tau_1)$，加起來是兩倍實部。）所以
$$\left|R(\tau+\tau_1)-R(\tau)\right|^2\le 2\left[R(0)-\text{Re}\,R(\tau_1)\right]R(0).$$

**Step 4：小技巧。** 一般 $R(\tau)$ 可能是複數，但 **$R(0)=E|X(t)|^2$ 一定是純實數**（自己乘自己的共軛）。$R(\tau_1)=R(0)$，所以 $R(\tau_1)$ 也是純實數、沒有虛部，共軛就是自己。右邊 $=2[R(0)-R(0)]R(0)=0$。

**Step 5：** 左邊是平方 $\le0$，所以 $R(\tau+\tau_1)=R(\tau)$，對所有 $\tau$。 ∎

【課本補充】Theorem 9-5，式 (9-175)–(9-177)，p. 418。Corollary（p. 419）：若 $R(\tau_1)=R(\tau_2)=R(0)$，且 $\tau_1/\tau_2$ 是無理數（不可公度），則 $R(\tau)$ 是常數（同時有兩個不可公度的週期，只能是常數）。

### 3.4 必要條件二：原點連續 ⇒ 處處連續

[▶ 22:53](https://youtu.be/b5m94_2EjK0?t=1373)

> 若自相關 $R(\tau)$ 在**原點連續**，則它**處處連續**。

**用法**：一個函數在原點附近連續，卻在某個地方有跳躍 (jump) → 不可能是自相關。原點附近的性質很重要。

**證明**：一樣立刻想到 Cauchy–Schwarz，得到和 3.3 **一模一樣**的式子：
$$\left|R(\tau+\tau_1)-R(\tau)\right|^2\le 2\left[R(0)-\text{Re}\,R(\tau_1)\right]R(0).$$
$\tau_1\to0$：原點連續，所以 $R(\tau_1)\to R(0)$，右邊 $\to0$。所以對任何 $\tau$，$R(\tau+\tau_1)\to R(\tau)$：處處連續。 ∎

反過來說：自相關如果在任何地方有跳躍，在原點也不可能連續——原點會單獨有一根脈衝。

### 3.5 例：截斷拋物線不是自相關

[▶ 26:23](https://youtu.be/b5m94_2EjK0?t=1583)

$$w(\tau)=\begin{cases}a^2-\tau^2,&|\tau|<a\\0,&|\tau|>a\end{cases}$$

**直接用上面兩個條件判斷不出來**：它處處連續（3.4 是必要條件，不是充分）；也沒有任何一點的值和原點一樣（3.3 用不上）。

**技巧**【口頭】：任何函數經過一個**合法的線性濾波器**，如果原來是自相關，輸出也一定要是自相關（Theorem 9-2，經過兩次濾波）。所以：輸出不是 ⇒ 原來也不是。

**用微分器（合法的濾波器）：** 若 $w$ 是 $X(t)$ 的自相關，則 $X'(t)$ 的自相關是（第 11 集，WSS 時）
$$R_{X'X'}(\tau)=-w''(\tau).$$
寫成 $w(t_1-t_2)=a^2-(t_1-t_2)^2$：對 $t_2$ 偏微分得 $2(t_1-t_2)$，再對 $t_1$ 偏微分得 2：
$$-w''(\tau)=\begin{cases}2,&|\tau|<a\\0,&|\tau|>a\end{cases}$$

它在 $\tau=0$ **連續**，在 $\tau=a$ **不連續**，違反 3.4。所以 $-w''$ 不是自相關，$w$ 也不是。

⚠️ 逐字稿缺字：[▶ 28:56](https://youtu.be/b5m94_2EjK0?t=1736) 字幕說「在 $\tau$ 等於 2 的地方是不連續的」，應是 $\tau=a$（$-w''$ 的值是 2）。

老師說：還有很多技巧，例如經過合法的濾波器（微分兩次）再看波形；課本有很多範例可以練習。

【課本補充】Example 9-30，p. 419，論證相同。

---

## 4. 互頻譜的界

[▶ 29:56](https://youtu.be/b5m94_2EjK0?t=1796)

**為什麼功率頻譜是「功率」**【口頭】：源頭是我們把**二階動差當作能量**。傅立葉轉換只是一個工具，把高速變化和低速變化的頻率分開：影像動態變化大，高頻就多；聲音做傅立葉轉換，就知道是高頻還是低頻。所以自相關的傅立葉轉換，就是把能量依頻率切開。互頻譜就是各個頻率上，輸入和輸出之間的能量關係。

> **互頻譜的界**：對任何 $a<b$，
> $$\left|\int_a^bS_{XY}(\omega)\,d\omega\right|^2\le\int_a^bS_{XX}(\omega)\,d\omega\int_a^bS_{YY}(\omega)\,d\omega\qquad\text{(9-181)}.$$

- 不用積到無限大，任何一塊都對。例如只看一個 200 kHz 寬的頻段：輸入和輸出之間的相互影響，不會超過兩者（在那一段的功率）的乘積。

**證明**（老師說：不看證明先猜，一定是經過濾波器）：

1. 設計理想濾波器 $H_1(\omega)=H_2(\omega)=1$（$a<\omega<b$），其他為 0。$X$ 通過得 $Z$，$Y$ 通過得 $W$。
2. Cauchy–Schwarz：$|R_{ZW}(0)|^2=\left|E[Z(t)W^*(t)]\right|^2\le E|Z|^2E|W|^2=R_{ZZ}(0)R_{WW}(0)$。
3. 輸出功率 = 輸入頻譜乘 $|H|^2$ 再積分（Theorem 9-4），時間差 0 時反轉換的 $e^{j\omega\tau}$ 不見：
$$R_{ZZ}(0)=\frac{1}{2\pi}\int_a^bS_{XX}\,d\omega,\qquad R_{WW}(0)=\frac{1}{2\pi}\int_a^bS_{YY}\,d\omega,\qquad R_{ZW}(0)=\frac{1}{2\pi}\int_a^bS_{XY}\,d\omega.$$
   （$R_{ZW}$：$S_{ZW}=H_1S_{XY}H_2^*$，$H$ 在 $(a,b)$ 都是 1。）
4. 代入第 2 步，$\frac{1}{2\pi}$ 抵消，得證。 ∎

**等號**：Cauchy–Schwarz 等號成立時，兩個訊號（在能量上）成正比。

【課本補充】(9-180)：$R_{XY}^2(\tau)\le R_{XX}(0)R_{YY}(0)$，由 Cauchy–Schwarz 直接得到。

---

## 5. 隨機過程「相等」是什麼意思：均方相等

[▶ 35:07](https://youtu.be/b5m94_2EjK0?t=2107) 課本正文沒完全提（在附錄和 §9-1 開頭），老師覺得要知道觀念。

### 5.1 均方相等

數字 3 等於 3 沒問題。但隨機變數 $X$ 不是等於 3，它可能是 1、2、3，各有機率。說 $X=Y$ 是什麼意思？

> **均方相等** (equality in the mean-square sense)：
> $$E\left|X-Y\right|^2=0.$$
> 對隨機過程：$E|X(t)-Y(t)|^2=0$ 對每個 $t$。記號有時在等號上加一個 m 或別的標記，大部分時候省略，直接寫 $X(t)=Y(t)$。

- 直觀：兩個東西「隨機相等」，就是它們相減的隨機性是 0。
- 可以證明 $E|X-Y|^2=0$ ⇔ $P(X=Y)=1$：觀察到 $X=3$，$Y$ 就是 3；$X=2$，$Y$ 就是 2；不相等的機率是 0。
- 為什麼要講？下一章會講「取樣後再內插 (interpolation) 的隨機過程等於原來的過程」，這個「等於」要定義清楚。

### 5.2 每個時間各自成立 vs 所有時間同時成立

[▶ 38:16](https://youtu.be/b5m94_2EjK0?t=2296) 回到機率空間：隨機過程就是定義映射（第一題習題就是請你自己定義映射）。

- 對每個時間 $t$，令
$$A_t=\{\zeta: X(t,\zeta)=Y(t,\zeta)\}$$
  （兩個映射映出來的實數一樣的那些 $\zeta$）。均方相等 ⇔ $P(A_t)=1$，**對每個 $t$**。
- 再令 $A_\infty=\bigcap_tA_t$：**所有時間同時**相等的 $\zeta$。
- 課本要講的是：均方相等**只需要每個時間各自** $P(A_t)=1$，不需要 $P(A_\infty)=1$ 那麼強。一個時間一個時間看，每個時間的映射可以不一樣，不用綜合看。

**集合的觀念** [▶ 41:51](https://youtu.be/b5m94_2EjK0?t=2511)：

- $P(A_1)=P(A_2)=1$ ⇒ $P(A_1\cap A_2)=1$。證明：
$$1\ge P(A_1\cup A_2)=P(A_1)+P(A_2)-P(A_1\cap A_2)=2-P(A_1\cap A_2)\ \Rightarrow\ P(A_1\cap A_2)\ge1.$$
  這個公式成立靠第三個公設（可加性）；拿掉可加性就算不了。
- 交集**可數**個（$A_1,A_2,A_3,\dots$）：還是 1，因為有可數可加性。
- 交集**不可數**個（例如 $t\in\mathbb{R}$ 的所有 $A_t$）：**不知道**。不可數交集作為集合可以定義，但公設沒有定義不可數個集合交集的量度，所以不會算。數學上沒定義的東西，答案就是不知道。老師的比喻：沒告訴你「兩條平行線不相交」這個公設，你就不知道。【口頭】

**例**：$S=\mathbb{R}$，$A_t$ 是 $S$ 拿掉一點（$\zeta=t$ 那一點），每個 $P(A_t)=1$；但每一點都被拿掉過，$A_\infty=\varnothing$，$P(A_\infty)=0$。這個例子剛好算得出來，但一般不一定能量。

【課本補充】Papoulis p. 375（式 (9-1)）：MS 相等時 $P(A_t)=1$，但不能推出 $P(A_\infty)=1$；因為 $A_\infty$ 是 $t$ 跑遍整條實數軸時所有 $A_t$ 的交集，$P(A_\infty)$ 甚至可能是 0。

---

## 6. 均方週期

[▶ 45:54](https://youtu.be/b5m94_2EjK0?t=2754) 下一章會講隨機過程的相等和**週期**。$X(t)$ 是隨機的，每個時間只知道機率（例如 $\pm1$ 各半），怎麼說它是週期的？要講清楚。

> **均方週期** (MS periodic)：週期 $T$，若
> $$E\left|X(t+T)-X(t)\right|^2=0,\quad\text{對每個 }t.$$
> 一般省略 mean square，說「a random process is periodic」通常就是這個意思。所有東西以**能量**為出發點。

**怎麼驗證**：這是二階動差，所以一定跟自相關有關。

> **（WSS）** $X(t)$ 均方週期 ⇔ $R(\tau)$ 是週期函數。

老師的總結【口頭】：**隨機過程在均方意義下的性質，完全顯現在它的自相關上**，因為兩者都是能量上的思維。

【課本補充】
- WSS（p. 419，式 (9-179)）：$E|X(t+\tau_1)-X(t)|^2=2[R(0)-R(\tau_1)]$，所以 MS 週期 ⇔ $R(\tau_1)=R(0)$ ⇔（Theorem 9-5）$R$ 是週期函數。類似地，MS 連續 ⇔ $R(\tau)$ 處處連續（式 (9-178)）。
- 一般（不一定 WSS），**Theorem 9-1**（p. 393）：$X(t)$ MS 週期 ⇔ $R(t_1,t_2)$ **雙週期**：$R(t_1+mT,t_2+nT)=R(t_1,t_2)$，對所有整數 $m,n$。證明也用 Cauchy–Schwarz：$E^2\{X(t_1)[X(t_2+T)-X(t_2)]\}\le E\{X^2(t_1)\}E\{[X(t_2+T)-X(t_2)]^2\}$。
- p. 392–393：MS 週期時，對特定 $t$，$X(t+T)=X(t)$ 機率 1；但「對所有 $t$ 都 $X(t+T,\zeta)=X(t,\zeta)$」的 $\zeta$ 集合不一定機率 1（同 5.2）。MS 週期過程的平均是週期的。

---

## 7. 一頁速查表

### 積分頻譜

- $F(\omega)=\int_{-\infty}^\omega S$，非遞減；$R(\tau)=\frac1{2\pi}\int e^{j\omega\tau}dF(\omega)$。
- Riemann–Stieltjes：$\int f\,dg=\lim\sum f(x_i)[g(x_i)-g(x_{i-1})]$；$g$ 可微時 $=\int fg'\,dx$。用途：避開 delta。

### 自相關的判定（WSS）

| 類型 | 條件 |
|---|---|
| 充要 | $R$ 非負定 ⇔ $S(\omega)\ge0$ |
| 充分（Pólya） | $\tau>0$ 凸（$w''\ge0$）、趨於有限極限 |
| 必要 | $\lvert R(\tau)\rvert\le R(0)$ |
| 必要（Thm 9-5） | $R(\tau_1)=R(0)$ ⇒ 週期 $\tau_1$ |
| 必要 | 原點連續 ⇒ 處處連續 |
| 技巧 | 經過合法濾波器（如微分：$-R''$）後仍須是自相關 |

- 關鍵不等式（Cauchy–Schwarz）：$\lvert R(\tau+\tau_1)-R(\tau)\rvert^2\le2[R(0)-\text{Re}\,R(\tau_1)]R(0)$。
- 截斷拋物線 $a^2-\tau^2$：$-w''$ 在 0 連續、在 $a$ 跳 → 不是自相關。

### 互頻譜的界

$\left|\int_a^bS_{XY}\right|^2\le\int_a^bS_{XX}\int_a^bS_{YY}$。關鍵：理想帶通 + Cauchy–Schwarz。$R_{XY}^2(\tau)\le R_{XX}(0)R_{YY}(0)$。

### 均方意義

- 均方相等：$E|X-Y|^2=0$ ⇔ $P(X=Y)=1$；只要求每個 $t$ 各自成立。
- 可數個機率 1 的事件交集仍機率 1；不可數交集沒有定義。
- 均方週期：$E|X(t+T)-X(t)|^2=0$ ⇔（WSS）$R$ 週期；一般 ⇔ $R(t_1,t_2)$ 雙週期。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 均方相等 | §10-5 取樣定理：取樣再內插 = 原過程（均方意義） |
| 均方週期 | §10-4 循環平穩過程；§11-3 Fourier 級數展開 |
| Riemann–Stieltjes、積分頻譜 | §11-4 頻譜表示（Fourier–Stieltjes 表示） |
| 自相關判定 | 習題、考試 |
| 下一集 | §9-3 (3/3)：離散時間前的剩餘部分 |

---

## 附：本集一句話總結

> **WSS 時「是自相關 ⇔ 非負定 ⇔ 頻譜非負」；要排除一個函數不是自相關，就用必要條件（最大在原點、有一點等於 $R(0)$ 就必須週期、原點連續就必須處處連續、經過合法濾波器後仍須合法），證明全靠 Cauchy–Schwarz；而隨機過程的「相等」「週期」都是均方意義，完全由自相關決定。**

---

## ⚠️ 待確認清單

1. [▶ 16:36](https://youtu.be/b5m94_2EjK0?t=996) Pólya 判準：老師和課本都說 concave，但課本例子 $w''>0$（凸），標準敘述也是凸；用詞待確認。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-3 (2/3) 錄影逐字稿（whisper large-v3-turbo，48:57）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
