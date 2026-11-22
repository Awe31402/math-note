---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 15
lecture: Lec 9-4 General Concepts — Discrete-Time Processes
date: 待補
video: https://youtu.be/6AsL_jKhs98
notes: Papoulis & Pillai 4th ed. §9-4 Discrete-Time Processes（式 (9-182)–(9-215)，pp. 420–426；Schur 的結果 式 (9-195)–(9-202)、Paley–Wiener criterion 式 (9-203)、(9-204)、Example 9-32、9-34、Sampling 式 (9-215)）
---

# 第 15 集 · Lec 9-4：離散時間過程——取樣後頻譜週期疊加、Schur 引理（Toeplitz 非負定 ⇔ 頻譜非負）、Paley–Wiener 判準、$\sum c_ie^{j\omega_in}$ 何時 WSS [▶ 影片](https://youtu.be/6AsL_jKhs98)

← 上一集：[14](14-ms-periodicity-continuity-differentiability-integrability.md) ｜ [總目錄](README.md) ｜ 下一集：[16](16-modulation-baseband-passband-rice-representation.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 15 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:01:35，whisper large-v3-turbo）＋ Papoulis §9-4（pp. 420–426）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【Q&A】` 學生提問
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「傅立葉轉換」→「Fullet／Fourier／覆列轉換」，「autocorrelation」→「autocarration／autoclin／autochrome／autograin／autocritic function」，「wide-sense stationary」→「y-sign／wise and／Wisen stationary」，「aliasing」→「Alien性」，「Schur」→「Sher」，「Hermitian Toeplitz」→「Hermitian topolis」，「Paley–Wiener」→「Perry Weiner／Pettie Weiner／Haley Wiener／Pelly Winer」，「positive definite」→「passive definite／Positive Devonin」，「dominated convergence theorem」→「dominic convergence theory」，「monotone convergence theorem」→「Molotone Convergence Theory」，「Poisson integral formula」→「捧重的 formula／Poisson Integral Formula」，「Cauchy–Schwarz」→「cultry-swart」，「實變分析」→「十遍分析」，「almost everywhere」→「almost everywhere」，「inner product」→「Enerpoda」，「uncorrelated」→「uncollected／uncollated」，「穩態」→「穩泰／穩碳」，「multipath fading」→「multipaste fading」，「Rayleigh distribution」→「radial distribution」，「Riemann」→「Rhyman」，「Z-transform」→「計存縫／Z選分」，「1/z」→「計分之一／Z分之1」，「discrete」→「discreet」，「complex conjugate」→「complete conjugate」。以下一律用正確的字。

> **接上一集**：§9-1 到 §9-3 都是連續時間。§9-4 把所有性質轉到**離散時間**。大部分性質照搬；這一集專講不一樣的地方：取樣造成頻譜週期疊加、離散版的「非負定 ⇔ 頻譜非負」（Schur）、更強的正定條件（Paley–Wiener），以及多頻率疊加的訊號何時平穩。這是第 9 章的最後一集。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 記號：方括號 = 離散時間](#1-記號方括號--離散時間)
- [2. 離散時間傅立葉轉換與 z 轉換](#2-離散時間傅立葉轉換與-z-轉換)
- [3. 取樣：頻譜變成週期疊加（aliasing）](#3-取樣頻譜變成週期疊加aliasing)
- [4. 基本定理與 Theorem 9-2 的離散版](#4-基本定理與-theorem-9-2-的離散版)
- [5. Schur 引理：Toeplitz 矩陣非負定 ⇔ 頻譜非負](#5-schur-引理toeplitz-矩陣非負定--頻譜非負)
  - [5.1 敘述](#51-敘述)
  - [5.2 ⇒：頻譜非負 ⇒ 非負定](#52-頻譜非負--非負定)
  - [5.3 ⇐：非負定 ⇒ 頻譜非負（Poisson 積分）](#53-非負定--頻譜非負poisson-積分)
- [6. Paley–Wiener 判準：什麼時候是正定](#6-paleywiener-判準什麼時候是正定)
- [7. $X[n]=\sum c_ie^{j\omega_in}$ 何時 WSS](#7-xnsum-c_iejomega_in-何時-wss)
- [8. Theorem 9-4 的離散版與 z 轉換例子](#8-theorem-9-4-的離散版與-z-轉換例子)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 記號、DTFT、z 轉換 | [▶ 00:00](https://youtu.be/6AsL_jKhs98?t=0) | 式 (9-182)、(9-191)–(9-194)，pp. 420–421 |
| 取樣與 aliasing | [▶ 04:38](https://youtu.be/6AsL_jKhs98?t=278) | 式 (9-215)，p. 426 |
| 離散版基本定理 | [▶ 09:46](https://youtu.be/6AsL_jKhs98?t=586) | 式 (9-186)–(9-190)，p. 421 |
| Schur 引理 | [▶ 10:48](https://youtu.be/6AsL_jKhs98?t=648) | 式 (9-195)–(9-202)，pp. 422–423 |
| Paley–Wiener | [▶ 31:18](https://youtu.be/6AsL_jKhs98?t=1878) | 式 (9-203)、(9-204)，p. 423 |
| 多頻率訊號何時 WSS | [▶ 45:17](https://youtu.be/6AsL_jKhs98?t=2717) | Example 9-32，p. 424 |
| 離散版 Theorem 9-4、z 轉換例子 | [▶ 55:29](https://youtu.be/6AsL_jKhs98?t=3329) | 式 (9-210)、(9-211)、Example 9-34，pp. 424–425 |

---

## 1. 記號：方括號 = 離散時間

[▶ 00:00](https://youtu.be/6AsL_jKhs98?t=0) 老師個人喜歡、做論文也用的記號（設計 digital filter 時也都用方括號）【口頭】：

- **方括號** $X[n]$：離散時間 (discrete in time)，只看整數時間點。
- **圓括號** $X(t)$：連續時間。
- 離散過程就是原來的連續過程只取整數點：$X[n]=X(n)$。這是一個慣例 (convention)，老師希望大家也用，會讓自己非常清楚。

自相關照原來的定義（一看到方括號就知道參數是整數）：
$$R[m_1,m_2]=E\left\{X[m_1]X^*[m_2]\right\};\qquad\text{WSS 時 }R[\tau]=E\left\{X[m+\tau]X^*[m]\right\},\ \tau\text{ 是整數}.$$

方括號的自相關就是圓括號自相關的取樣：$R[\tau]=R(\tau)$（在整數點相等），所以性質完全一樣。

【課本補充】式 (9-182)–(9-184)，p. 420：$C[n_1,n_2]=R[n_1,n_2]-\eta[n_1]\eta^*[n_2]$。離散**嚴格白雜訊**：$X[n_i]$ 互相獨立；**白雜訊**：不相關，$R[n_1,n_2]=q[n_1]\delta[n_1-n_2]$，$\delta[n]$ 是 Kronecker delta（$n=0$ 為 1，否則 0）。WSS 白雜訊就是變異數 $q$ 的 i.i.d. 序列。

---

## 2. 離散時間傅立葉轉換與 z 轉換

[▶ 02:35](https://youtu.be/6AsL_jKhs98?t=155) 只有整數點有值，所以只能做**離散時間傅立葉轉換** (DTFT)：

> **功率頻譜**（離散）：
> $$S\left(e^{j\omega}\right)=\sum_{m=-\infty}^{\infty}R[m]\,e^{-jm\omega},\qquad R[m]=\frac{1}{2\pi}\int_{-\pi}^{\pi}S\left(e^{j\omega}\right)e^{jm\omega}\,d\omega.$$

- 記號上把 $e^{j\omega}$ 獨立出來，用一個新記號 $z$ 代表：$z$ 就是一個 dummy variable，$z=e^{j\omega}$，於是得到 **z 轉換** $S(z)=\sum_mR[m]z^{-m}$。解線路時非常方便。
- 從公式看出它是**週期**的，週期 $2\pi$：設計 digital filter 時只畫 $-\pi$ 到 $\pi$，外面都一模一樣。
- 反轉換只積一個週期（$0$ 到 $2\pi$ 或 $-\pi$ 到 $\pi$），不可能積到無限大。
- 用 $\omega$ 記號，反轉換要記得 $\frac{1}{2\pi}$。（老師又說一次他比較喜歡 $2\pi f$，兩邊都沒有常數。）

【課本補充】式 (9-191)–(9-194)，p. 421。實數過程 $R[-m]=R[m]$：$S(e^{j\omega})=R[0]+2\sum_{m=1}^\infty R[m]\cos m\omega$，是 $\cos\omega$ 的函數。

---

## 3. 取樣：頻譜變成週期疊加（aliasing）

[▶ 04:38](https://youtu.be/6AsL_jKhs98?t=278) 通訊原理最重要的基本概念：**取樣後頻譜變成週期性的**。研究所考試也常考這個基本題。

> **定理**：$X[n]=X_a(n)$（取樣間隔 1）。則
> $$S\left(e^{j\omega}\right)=\sum_{k=-\infty}^{\infty}S_a(\omega+2\pi k),$$
> $S_a$ 是連續過程 $X_a(t)$ 的功率頻譜：原頻譜每隔 $2\pi$ **平移疊加**。

**證明**（老師說這是「事後諸葛」的證明：已經知道答案是週期性的，再反推的簡易證明；做研究時最早一版的證明通常最複雜，後來才越整理越精簡）：

**Step 1：** 離散自相關是連續自相關的取樣，連續的用反轉換表示：
$$R[\tau]=R_a(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S_a(\omega)e^{j\omega\tau}\,d\omega.$$

**Step 2：技巧——每 $2\pi$ 積一次。** $k=0$ 積 $(-\pi,\pi)$，$k=1$ 積 $(\pi,3\pi)$，$k=2$ 積 $(3\pi,5\pi)$……所有 $k$ 走一遍就是 $(-\infty,\infty)$：
$$R[\tau]=\sum_k\frac{1}{2\pi}\int_{-\pi+2\pi k}^{\pi+2\pi k}S_a(\omega)e^{j\omega\tau}\,d\omega.$$

**Step 3：變數變換** $\omega'=\omega-2\pi k\in(-\pi,\pi)$。$\tau$ 是整數，$e^{j2\pi k\tau}=1$，拿掉：
$$R[\tau]=\sum_k\frac{1}{2\pi}\int_{-\pi}^{\pi}S_a(\omega'+2\pi k)e^{j\omega'\tau}\,d\omega'.$$

**Step 4：** 積分和求和互換（假設都是 nice 的 Riemann 可積函數）：
$$R[\tau]=\frac{1}{2\pi}\int_{-\pi}^{\pi}\left[\sum_kS_a(\omega'+2\pi k)\right]e^{j\omega'\tau}\,d\omega'.$$

**Step 5：傅立葉轉換的唯一性。** 和第 2 節的反轉換公式比對，傅立葉轉換一對一，所以中括號就是 $S(e^{j\omega})$。 ∎

**圖像**【口頭】：原來的 $S_a(\omega)$（非負）往左右每 $2\pi$ 複製、疊加。二維傅立葉轉換（影像處理）也一樣是週期疊加。

**aliasing（混疊）**：用聲音處理軟體重新取樣 (resampling) 時，$\pm\pi$ 附近的頻率**失真特別嚴重**，因為相鄰的複製品疊到這裡來。現在是數位時代，一定會有 aliasing。（老師說聲音現在一般取樣「41 kHz」——常見的 CD 取樣率是 44.1 kHz。）

【課本補充】式 (9-215)，p. 426，一般取樣間隔 $T$：$X[n]=X_a(nT)$，
$$S\left(e^{j\omega}\right)=\sum_mR_a(mT)e^{-jm\omega}=\frac1T\sum_{n=-\infty}^{\infty}S_a\left(\frac{\omega+2\pi n}{T}\right),$$
這是 Poisson 求和公式（附錄 10A）的結果。Example 9-35：$M$ 個複指數 $\sum c_ie^{j\omega_it}$ 取樣後，在 $(-\pi,\pi)$ 內是 $M$ 條譜線 $2\pi\sum\sigma_i^2\delta(\omega-\beta_i)$，$\beta_i=T\omega_i-2\pi n_i$。

---

## 4. 基本定理與 Theorem 9-2 的離散版

[▶ 09:46](https://youtu.be/6AsL_jKhs98?t=586) 公式完全一樣、同一件事情：要知道離散時間輸入輸出的自相關關係，**把輸入的自相關當作輸入送進濾波器**（兩次）。

【課本補充】式 (9-186)–(9-190)，p. 421：
$$Y[n]=\sum_kX[n-k]h[k],\quad\eta_Y[n]=\eta_X[n]*h[n],$$
$$R_{XY}[n_1,n_2]=\sum_kR_{XX}[n_1,n_2-k]h^*[k],\qquad R_{YY}[n_1,n_2]=\sum_rR_{XY}[n_1-r,n_2]h[r].$$
WSS 時 $R_{XY}[m]=R_{XX}[m]*h^*[-m]$，$R_{YY}[m]=R_{XY}[m]*h[m]$，$\eta_Y=\eta_XH(1)$。

---

## 5. Schur 引理：Toeplitz 矩陣非負定 ⇔ 頻譜非負

### 5.1 敘述

[▶ 10:48](https://youtu.be/6AsL_jKhs98?t=648) 連續時間時（第 13 集）有：非負傅立葉轉換 ⇔ 非負定（$\sum a_ia_j^*R(\tau_i-\tau_j)\ge0$）。離散版長得很像，其實是同一件事（只是取樣）。

> **Schur 引理**：設 $R[m]$ **可和** (summable)：$\sum_m|R[m]|<\infty$，且 $R[-m]=R^*[m]$。令 $r_k=R[k]$，**Hermitian Toeplitz 矩陣**
> $$T_n=\begin{pmatrix}r_0&r_1&\cdots&r_n\\r_1^*&r_0&\cdots&r_{n-1}\\\vdots&&\ddots&\vdots\\r_n^*&r_{n-1}^*&\cdots&r_0\end{pmatrix}.$$
> 則
> $$S\left(e^{j\omega}\right)\ge0\iff T_n\ \text{非負定，對每個 }n=0,1,2,\dots$$

- **可和**這個條件課本敘述時沒特別強調，但其實需要。我們考慮的訊號能量不會是無限大；自相關不可和，代表能量可能無限大，一般碰不到。【口頭】
- $R[-m]=R^*[m]$：自相關一定符合（$X$ 和 $X^*$ 相乘的期望值，倒過來就是 $-\tau$）。
- **非負定矩陣**（大一線性代數）：對任何向量 $\mathbf{a}$，$\mathbf{a}^\dagger T_n\mathbf{a}\ge0$（左邊取共軛轉置）。若只有 $\mathbf{a}=\mathbf{0}$ 時才等於 0，就叫**正定** (positive definite)。
- 矩陣有好多維度，所以**每個 $n$** 都要非負定。

**forward 和 converse**【口頭】：順著敘述講（先講上面、再講下面）叫 forward；倒過來叫 converse。老師看過有些書搞反，反正兩個方向都要證。

### 5.2 ⇒：頻譜非負 ⇒ 非負定

**Step 1：** 展開矩陣乘法：
$$\mathbf{a}^\dagger T_n\mathbf{a}=\sum_{i=0}^{n}\sum_{m=0}^{n}a_i^*a_m\,r_{i-m}.$$

**Step 2：** 引進功率頻譜（唯一的方式）：$r_{i-m}=\frac{1}{2\pi}\int_{-\pi}^{\pi}S(e^{j\omega})e^{j(i-m)\omega}d\omega$。

**Step 3：** 積分和求和互換（老師說下一步一定做這件事，習慣了就很快）：
$$=\frac{1}{2\pi}\int_{-\pi}^{\pi}S\left(e^{j\omega}\right)\left|\sum_{m=0}^{n}a_me^{-jm\omega}\right|^2d\omega.$$
雙重求和就是一個絕對值平方。

**Step 4：** $S\ge0$、絕對值平方 $\ge0$，乘起來 $\ge0$，積分還是 $\ge0$。 ∎

老師說這和第三題習題的答案很像，回去一定要自己做。

### 5.3 ⇐：非負定 ⇒ 頻譜非負（Poisson 積分）

[▶ 17:01](https://youtu.be/6AsL_jKhs98?t=1021) 老師說這可能是第 9 章最複雜的證明；也是「事後諸葛」、整理消化過的證明，看不出原作者怎麼想到的。

**Step 1：選一個很巧的 $\mathbf{a}$。** 老師說沒看過證明根本想不出來，考試五分鐘內他自己也想不出來；應該是試過很多方法，需要好幾年的經驗。對 $0<\rho<1$、任意 $\omega_0$：
$$a_m=\sqrt{1-\rho^2}\,\rho^m\,e^{jm\omega_0}.$$

**Step 2：** $T_n$ 非負定，對**任何** $\mathbf{a}$ 都成立，所以對這個特選的 $\mathbf{a}$ 也成立。由 5.2 的 Step 3：
$$0\le\mathbf{a}^\dagger T_n\mathbf{a}=\frac{1}{2\pi}\int_{-\pi}^{\pi}(1-\rho^2)\left|\sum_{m=0}^{n}\rho^me^{jm(\omega_0-\omega)}\right|^2S\left(e^{j\omega}\right)d\omega.$$
（老師提醒：一個 $\mathbf{a}$ 讓矩陣 $\ge0$ 不代表別的 $\mathbf{a}$ 也對；但這裡前提是非負定，所以選哪個都對，我們就選一個符合未來證明需要的。）

**Step 3：等比級數。** 公比 $\rho e^{j(\omega_0-\omega)}$：
$$\sum_{m=0}^{n}\rho^me^{jm(\omega_0-\omega)}=\frac{1-\left(\rho e^{j(\omega_0-\omega)}\right)^{n+1}}{1-\rho e^{j(\omega_0-\omega)}}.$$

**Step 4：困難——$S$ 在積分裡面。** 積分 $\ge0$ 不代表被積函數 $\ge0$。所以要把積分拿掉。先取 $n\to\infty$ 簡化，但**極限和積分一般不能互換**。

實變分析裡能互換的兩個定理：
- **單調收斂定理** (monotone convergence theorem)：$f_n$ 單調遞增（或遞減）時，先積分再取極限 = 先取極限再積分。
- **控制收斂定理** (dominated convergence theorem，用得比較廣)：若 $|f_n|\le g$ 對所有 $n$，$g$ 跟 $n$ 無關而且可積（積分有限），則極限和積分可以互換。

這裡用控制收斂：
- 等比級數部分：$\left|\sum_m\rho^me^{jm(\cdot)}\right|\le\sum_m\rho^m\le\frac{1}{1-\rho}$，有限（$\rho$ 是選定的常數）。
- 頻譜部分：$|S(e^{j\omega})|\le\sum_m|R[m]|$——**這裡需要可和條件**，總能量有限，極限和積分才可以互換。自相關衝到無限大、總能量無限大的情形不在這裡討論，它的功率頻譜也不見得非負。

**Step 5：取極限。** $\rho<1$，公比的 $n+1$ 次方消失：
$$0\le\frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{1-\rho^2}{1-2\rho\cos(\omega-\omega_0)+\rho^2}\,S\left(e^{j\omega}\right)d\omega.$$
（$\left|1-\rho e^{j\theta}\right|^2=1-2\rho\cos\theta+\rho^2$。）

**Step 6：Poisson 積分公式** (Poisson integral formula)：為什麼選那個 $\mathbf{a}$？就是要湊這個公式。它的重點是**把積分裡的函數帶出來**（有點像 delta 的複製性質）：
$$\lim_{\rho\to r^-}\frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{r^2-\rho^2}{r^2-2r\rho\cos(\omega-\omega_0)+\rho^2}\,f(\omega)\,d\omega=f(\omega_0)$$
（$f$ 週期、在 $\omega_0$ 連續）。取 $r=1$、$\rho\to1$：Step 5 的左邊趨於 $S(e^{j\omega_0})$。

**Step 7：** 對所有 $0<\rho<1$ 都 $\ge0$，取極限仍 $\ge0$。$S$ 連續（$R$ 可和），所以
$$S\left(e^{j\omega_0}\right)\ge0,\quad\text{對每個 }\omega_0.$$ ∎

老師說【口頭】：這樣介紹之後，至少能抓到重點：**要把積分裡的函數帶出來時，就想到 Poisson 積分公式**，多了一個工具。數學公式會忘記（他自己一段時間不看也忘），但這種理念比較持久。

⚠️ 待確認：老師口述 Poisson 積分公式時說「對任何 $0<\rho<r$ 會等於原來的函數」；嚴格說 $\rho<r$ 時積分是 $f$ 的調和延拓，$\rho\to r$ 的**極限**才是 $f(\omega_0)$（課本也寫「its interior ray limit as $\rho\to1-0$ equals $S(\omega_0)$」）。

【課本補充】式 (9-195)–(9-202)，pp. 422–423。課本結論寫成 $S(\omega_0)\ge0$ **almost everywhere**（不另假設連續時）。

---

## 6. Paley–Wiener 判準：什麼時候是正定

[▶ 31:18](https://youtu.be/6AsL_jKhs98?t=1878)

- 課本對**函數**的 positive definite 和 non-negative definite 有點混淆（第 4 集），但對**矩陣**分得很清楚：$\mathbf{a}^\dagger T_n\mathbf{a}\ge0$，而且等於 0 **若且唯若** $\mathbf{a}=\mathbf{0}$，叫正定。
- 頻譜非負已經證完了。那「正定」會給我們額外的東西嗎？這是 Paley–Wiener 他們的研究想法。

> **Paley–Wiener 判準** (Paley–Wiener criterion)：若
> $$\frac{1}{2\pi}\int_{-\pi}^{\pi}\ln S\left(e^{j\omega}\right)d\omega>-\infty,$$
> 則每個 $T_k$（$k=0,1,2,\dots$）都是**正定**的。

**操作意義** (operational meaning)【口頭】：

- 若 $S$ 在某個**小區間**上等於 0，$\ln0=-\infty$，積分就是 $-\infty$，判準不成立。
- 所以判準要說的是：**功率頻譜不會有一整段連續區間是 0**，大部分地方都是正的。
- 但可以有**單點**是 0：那些點不影響積分。也就是 $S>0$ except 積分為 0 的一些點。
- 這裡有點 tricky：把 $\ln0$ 直接定義為 $-\infty$（$\ln$ 本來要大於 0 才能代）；老師說過把無限大當數字要很小心，但這裡確實是這個想法。
- 結論：**正定的自相關，代表功率頻譜幾乎處處是正的**。

**證明（反證法）** [▶ 36:26](https://youtu.be/6AsL_jKhs98?t=2186)：

1. 假設某個 $T_k$ 不是正定（只是非負定）：存在**非零**向量 $\mathbf{a}$，$\mathbf{a}^\dagger T_k\mathbf{a}=0$。
2. 由 5.2：$\frac{1}{2\pi}\int S(e^{j\omega})\left|\sum_ma_me^{-jm\omega}\right|^2d\omega=0$。
3. 被積函數 $\ge0$（$S\ge0$，Schur），積分為 0，所以被積函數 **almost everywhere** 為 0。
   - almost everywhere（幾乎處處）：不成立的地方，總積分（測度）是 0。若 $f\ge0$ 且 $\int f=0$，則 $f\ne0$ 的地方總面積是 0。
4. 三角多項式 $\sum_ma_me^{-jm\omega}$ **不是**幾乎處處為 0，因為**整數倍頻率互相正交**：
$$\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{jn\omega}e^{-jm\omega}d\omega=\begin{cases}1,&n=m\\0,&n\ne m\end{cases}$$
   （4G 行動通訊的基本概念：頻率是同一個基本頻率的整數倍就正交，例如 3 kHz 的 3 倍和 5 倍。）所以
$$\frac{1}{2\pi}\int_{-\pi}^{\pi}\left|\sum_ma_me^{-jm\omega}\right|^2d\omega=\sum_m|a_m|^2>0,$$
   自己跟自己的內積是 1，交叉項全部消掉。例：$(a_1e^{j\omega}+a_2e^{j2\omega})$ 和 $(b_1e^{j\omega}+b_2e^{j2\omega})$ 的內積是 $a_1b_1^*+a_2b_2^*$。
5. 所以 $S(e^{j\omega})=0$ almost everywhere（老師講義上用 $\varepsilon$ 切兩塊的方式把這一步論證完整，他說那比較像純數學硬幹出來的，不花太多時間）。
6. 於是 $\int\ln S=-\infty$，和假設矛盾。 ∎

【課本補充】式 (9-203)、(9-204)，p. 423。課本接著說：可積條件加上 Paley–Wiener 判準，讓功率頻譜可以**分解** (factorization)：存在唯一的最小相位 (minimum-phase) 函數 $H(z)=\sum_{k\ge0}h_kz^{-k}$，使 $S(\omega)=|H(e^{-j\omega})|^2$ a.e.（式 (9-205)–(9-208)）——這是 §11-1 的主題。

---

## 7. $X[n]=\sum c_ie^{j\omega_in}$ 何時 WSS

[▶ 45:17](https://youtu.be/6AsL_jKhs98?t=2717) 通訊上離散訊號常是這個形式：要傳的數位訊號 $c_1,c_2,c_3,\dots$ 用不同頻率送。整數倍頻率就正交，不整數倍就不見得。我們一直希望做出來的過程是 WSS（不穩的訊號後續處理有額外風險）。

> **定理**：設 $\omega_i$ **互不相同**，而且都**不是 DC**（$\omega_i\ne0$）。則
> $$X[n]=\sum_ic_ie^{j\omega_in}\ \text{是 WSS}\iff c_i\ \text{零平均、互不相關}.$$

- 括號裡的條件課本沒提，但很合理：兩個訊號用同一個頻率送就疊在一起，接收端絕對解不開。
- 意義：用載波合成離散通訊訊號，每個分量都要**不相關、零平均**；少一個，做出來的訊號就不穩。

**⇐**：直接驗證平均和自相關（以前做過類似的）。

**⇒**（比較 tricky，但證明一頁就完）：

**Step 1：平均是常數。** WSS ⇒ 平均是常數 $\eta$：
$$E\{X[n]\}=\sum_iE\{c_i\}e^{j\omega_in}=\eta,\quad\text{對所有 }n.$$
思考：不同頻率乘上常數加起來，會是一個不隨時間變的常數嗎？把它寫成
$$\sum_iE\{c_i\}e^{j\omega_in}-\eta\cdot e^{j0\cdot n}=0,\quad n=0,1,2,\dots$$
在多個時間取樣，就是一個**多元一次聯立方程式**，係數矩陣是 $e^{j\omega_in}$（Vandermonde 型），頻率都不一樣時**行列式不為 0**，只有唯一解：全部是 0。所以 $E\{c_i\}=0$（而且 $\eta=0$）。

- 為什麼要排除 DC？如果有一個 $\omega_i=0$，它和常數 $\eta$ 那一項是同一個頻率，疊在一起，就只能推出 $E\{c_i\}=\eta$，不一定是零平均。實作上學到：**不可以在 DC（$\omega=0$）送東西**。

**Step 2：不相關。** 算自相關：
$$E\left\{X[n+\tau]X^*[n]\right\}=\sum_{i,k}E\{c_ic_k^*\}e^{j\omega_i\tau}\,e^{j(\omega_i-\omega_k)n}.$$
WSS ⇒ 只跟 $\tau$ 有關、跟 $n$ 無關。固定 $\tau$，$n$ 一直變，結果不能變。又是一個聯立方程式（對 $n$），頻率是 $\omega_i-\omega_k$：
- 若所有 $\omega_i-\omega_k$（$i\ne k$）都不同且非 0，係數 $E\{c_ic_k^*\}e^{j\omega_i\tau}$ 都要是 0，所以 $E\{c_ic_k^*\}=0$，即不相關（零平均時，不相關 = 相乘的期望值為 0）。
- 若有些差值相同，只能推出它們疊加的係數和為 0。沒關係，還有 $\tau$：不同 $\tau$ 帶出不同的 $e^{j\omega_i\tau}$ 和 $e^{j\omega_{i'}\tau}$（原始頻率都不同），再解一次聯立方程式，個別係數還是要是 0。 ∎

老師的總結【口頭】：數位通訊常用一個訊號去不同頻率疊加，要穩態，唯一的可能就是 **uncorrelated、zero mean**，否則就不穩，if and only if。

【課本補充】Example 9-32，式 (9-209)，p. 424：此時 $R[m]=\sum_i\sigma_i^2e^{j\beta_i m}$，$S(\omega)=2\pi\sum_i\sigma_i^2\delta(\omega-\beta_i)$（$|\omega|<\pi$），$\sigma_i^2=E\{|c_i|^2\}$，$\omega_i=2\pi k_i+\beta_i$，$|\beta_i|<\pi$。（離散時間頻率要以 $2\pi$ 為模互不相同。）

---

## 8. Theorem 9-4 的離散版與 z 轉換例子

[▶ 55:29](https://youtu.be/6AsL_jKhs98?t=3329)

> **離散 Theorem 9-4**（輸入 WSS）：
> $$S_{XY}\left(e^{j\omega}\right)=S_{XX}\left(e^{j\omega}\right)E\left[H^*\left(e^{j\omega}\right)\right],\qquad S_{YY}\left(e^{j\omega}\right)=S_{XX}\left(e^{j\omega}\right)E\left[\left|H\left(e^{j\omega}\right)\right|^2\right].$$

【Q&A】[▶ 55:59](https://youtu.be/6AsL_jKhs98?t=3359) 有同學問：為什麼老師的版本有期望值、課本沒有？老師答：課本的系統是確定的 (deterministic)，不需要期望值。如果系統是隨機的——例如 **multipath fading channel**，$h$ 很可能是 Rayleigh 分布——就先做卷積，再對 $h$ 取期望值。功率頻譜本身已經是確定的函數，但經過隨機的 $h$ 出來還是隨機的，所以要對 $h$ 取期望值讓它不再隨機。

- 好處：相乘有直觀的結果。$|H|$ 在 2 kHz 是 3，那個頻率就被放大（功率放大 $|H|^2$ 倍）；在 4 kHz 是 0.2，那個頻率就被壓縮。
- 寫法：$H(e^{j\omega})$ 或用 $z=e^{j\omega}$ 寫成 $H(z)$，都是同一件事。
- 為什麼只看 WSS？因為這本書的功率頻譜是**一維**自相關的傅立葉轉換（只有 $\tau$）。需要的話可以自己推到二維。

**實數濾波器**：$h[n]$ 是實數時，$H^*(e^{j\omega})=H(e^{-j\omega})$，在 $z$ 域就是 $H(1/z)$：
$$S_{YY}(z)=S_{XX}(z)\,H(z)\,H(1/z).$$
設計 digital filter 時常用這個版本，因為時域 $h$ 通常是實數。$1/z$ 就是把 $e^{j\omega}$ 換成 $e^{-j\omega}$，即原來的共軛。

**例**（實數、但係數隨機的系統）[▶ 59:33](https://youtu.be/6AsL_jKhs98?t=3573)：
$$Y[n]-a\,Y[n-1]=X[n],$$
$a$ 是有密度的隨機變數（下一章會看到類似的東西）。

- 為什麼用 z 轉換不用傅立葉轉換？算轉移函數比較快。
- $Y[n-1]\to z^{-1}Y(z)$（$z^{-1}$ 就是延遲一格）。線性，所以 $(1-az^{-1})Y(z)=X(z)$：
$$H(z)=\frac{1}{1-az^{-1}}.$$
- 代入：
$$S_{YY}(z)=S_{XX}(z)\,E\left[\frac{1}{(1-az^{-1})(1-az)}\right].$$

【課本補充】Example 9-34（p. 425，$a$ 為常數）：若 $S_{XX}(z)=q$（白雜訊），$S_{YY}(z)=\frac{q}{(1-az^{-1})(1-az)}$，$R_{YY}[m]=\frac{q}{a^{-1}-a}a^{|m|}$。Example 9-33：一階差分 $Y[n]=X[n]-X[n-1]$，$H(z)=1-z^{-1}$，$S_{YY}(e^{j\omega})=2q(1-\cos\omega)$。課本也用離散版 (9-212) 和理想帶通濾波器證明 $S_{XX}(e^{j\omega})\ge0$（和第 12 集同樣的論證）。

老師說：這就是第 9 章要上的內容。

---

## 9. 一頁速查表

### 離散時間基本

- $R[m]=R_a(m)$；$S(e^{j\omega})=\sum R[m]e^{-jm\omega}$，週期 $2\pi$；$R[m]=\frac1{2\pi}\int_{-\pi}^{\pi}S\,e^{jm\omega}d\omega$。
- 取樣：$S(e^{j\omega})=\sum_kS_a(\omega+2\pi k)$（間隔 $T$：$\frac1T\sum S_a(\frac{\omega+2\pi n}{T})$）。關鍵：每 $2\pi$ 積一次、$e^{j2\pi k\tau}=1$、傅立葉唯一性。

### Schur 與 Paley–Wiener

| 條件 | 結論 |
|---|---|
| $S(e^{j\omega})\ge0$ | $\Leftrightarrow$ 所有 $T_n\ge0$（需 $R$ 可和） |
| $\frac1{2\pi}\int\ln S>-\infty$ | ⇒ 所有 $T_k>0$（正定） |

- ⇒ 關鍵：$\mathbf{a}^\dagger T_n\mathbf{a}=\frac1{2\pi}\int S\,|\sum a_me^{-jm\omega}|^2d\omega$。
- ⇐ 關鍵：$a_m=\sqrt{1-\rho^2}\rho^me^{jm\omega_0}$ → 控制收斂 → Poisson 核 $\frac{1-\rho^2}{1-2\rho\cos(\omega-\omega_0)+\rho^2}$ → $\rho\to1$ 得 $S(\omega_0)$。
- Paley–Wiener 意義：頻譜不能有一整段區間為 0。
- 整數倍頻率正交：$\frac1{2\pi}\int e^{j(n-m)\omega}d\omega=\delta[n-m]$。

### 多頻率訊號

$\sum c_ie^{j\omega_in}$（$\omega_i$ 互異、非 DC）WSS ⇔ $c_i$ 零平均、不相關。關鍵：Vandermonde 聯立方程式只有零解。

### 離散線性系統

- $S_{YY}(e^{j\omega})=S_{XX}(e^{j\omega})E|H(e^{j\omega})|^2$；實數 $h$：$S_{YY}(z)=S_{XX}(z)H(z)H(1/z)$。
- $Y[n]-aY[n-1]=X[n]$：$H(z)=\frac1{1-az^{-1}}$；白雜訊、$a$ 常數：$R_{YY}[m]=\frac{q\,a^{|m|}}{1-a^2}$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 取樣、aliasing、Poisson 求和公式 | §10-5 取樣定理（第 20 集）、附錄 10A（第 21 集） |
| 多頻率疊加、不相關零平均 | §10-3 調變（第 16–18 集） |
| Paley–Wiener、頻譜分解 | §11-1 分解與創新（第 22 集） |
| $Y[n]-aY[n-1]=X[n]$、z 轉換 | §11-2 有限階系統（第 23–25 集） |
| Toeplitz 矩陣 | §12-2 頻譜估計、§13-2 預測（Yule–Walker、Levinson） |

---

## 附：本集一句話總結

> **離散時間過程的頻譜是連續頻譜每隔 $2\pi$ 的週期疊加（取樣造成 aliasing）；自相關合法 ⇔ 所有 Hermitian Toeplitz 矩陣非負定 ⇔ 頻譜非負（Schur，用 Poisson 積分把頻譜「帶出來」），若再滿足 Paley–Wiener 判準（頻譜沒有整段為 0）就是正定；而多頻率疊加的訊號要平穩，係數必須零平均、互不相關。**

---

## ⚠️ 待確認清單

1. [▶ 28:47](https://youtu.be/6AsL_jKhs98?t=1727) Poisson 積分公式：老師說「對任何 $0<\rho<r$ 等於原函數」，嚴格說是 $\rho\to r$ 的極限；待確認是否口誤。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-4 錄影逐字稿（whisper large-v3-turbo，1:01:35）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
