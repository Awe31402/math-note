---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 27
lecture: Lec 11-3 Spectral Representation — Fourier Series and Karhunen–Loève Expansions (2/2)
date: 待補
video: https://youtu.be/_-3RZnfinHI
notes: Papoulis & Pillai 4th ed. §11-3 Karhunen–Loève Expansion（式 (11-55)–(11-63)、Example 11-9、11-10，pp. 511–513）；§11-2 補充；§10-6 smoothing 補充
---

# 第 27 集 · Lec 11-3 (2/2)：前幾集的補充（配方法、AR 的平穩性、可預測 vs 線譜、MA 就是卷積）、Karhunen–Loève 展開、Wiener 過程的特徵函數、WSS 時傅立葉轉換就是 KL 展開 [▶ 影片](https://youtu.be/_-3RZnfinHI)

← 上一集：[26](26-fourier-series-expansion-ms-periodic.md) ｜ [總目錄](README.md) ｜ 下一集：[28](28-spectral-representation-nonstationary-white-windowing-wold.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 27 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:16:33，whisper large-v3-turbo）＋ Papoulis §11-3（pp. 511–513）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Poisson sum formula」→「PPOZONE SUMFORMULA／portson sum formula」，「Lagrange multiplier」→「Lagrange Multiplier」，「配方法」→「配方法」，「Riemann integrable」→「Dryment Integrable」，「autoregressive」→「Auto-Regressive」，「Yule–Walker」→「your worker／your walker」，「Wold decomposition」→「Wall Decompetition」，「line spectrum」→「Line Spectrum／line spectral」，「Karhunen–Loève」→「Hunen Love／Cohunelab／Kahunen Love」，「orthonormal」→「Othonormal／osonormal」，「orthogonal」→「osogonal」，「inner product」→「Inner Product」，「eigenvalue／eigenvector／eigenfunction」→「Igon value／Igon Vector／Igon function／eign function」，「kernel」→「Kernel」，「Mercer's theorem」→「mercer's theorem／Mersethear」，「Markov source」→「Markov source」，「entropy rate」→「entropy rate」，「MIMO」→「MIMO」，「Wiener process」→「winer process／Winer process」，「Brownian motion」→「Bronnier Motion／brownian motion」，「null space」→「nounspace／now space」，「canonical form／echelon form」→「canonical form／usland form」，「Gram–Schmidt」→「Grensmead」，「微分方程」→「文方程／偏為分方程式」，「Real Analysis」→「識變函數分析」，「OFDM」→「OFDM」，「circular shift」→「circular shift」，「wide-sense stationary」→「wise and stationary／Y-Sign Station／Wisen stationary」，「complex conjugate」→「compress／complete conjugate」，「variance」→「variance」，「white」→「壞」。以下一律用正確的字。

> **接上一集**：上一集的 Fourier 級數：只有在均方週期時，投影係數才保證不相關。能不能找到一種投影，**任何過程**（不一定平穩）投影出的可數個係數都保證不相關？這就是 **Karhunen–Loève 展開**。開頭老師先補充前幾集的幾個問題。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 補充一：Poisson 求和公式的直覺](#1-補充一poisson-求和公式的直覺)
- [2. 補充二：平滑濾波器用配方法（不用對函數微分）](#2-補充二平滑濾波器用配方法不用對函數微分)
- [3. 補充三：AR 過程的隱含假設——WSS](#3-補充三ar-過程的隱含假設wss)
  - [3.1 「可預測」的兩種定義](#31-可預測的兩種定義)
  - [3.2 $|a|>1$ 不是 WSS 的證明](#32-a1-不是-wss-的證明)
  - [3.3 沒有輸入的系統](#33-沒有輸入的系統)
- [4. 補充四：MA 就是卷積](#4-補充四ma-就是卷積)
- [5. Karhunen–Loève 展開](#5-karhunenloève-展開)
  - [5.1 正交基與投影](#51-正交基與投影)
  - [5.2 定理：特徵函數的投影係數正交](#52-定理特徵函數的投影係數正交)
  - [5.3 特徵值是能量](#53-特徵值是能量)
  - [5.4 Mercer 定理](#54-mercer-定理)
  - [5.5 區間內均方相等](#55-區間內均方相等)
- [6. 例：Wiener 過程的 KL 展開](#6-例wiener-過程的-kl-展開)
- [7. WSS 時：傅立葉轉換就是 KL 展開](#7-wss-時傅立葉轉換就是-kl-展開)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 補充 Poisson 求和、配方法 | [▶ 00:00](https://youtu.be/_-3RZnfinHI?t=0) | 附錄 10A；§10-6 |
| 補充 AR、可預測、MA | [▶ 05:07](https://youtu.be/_-3RZnfinHI?t=307) | §11-2 |
| KL 展開 | [▶ 20:29](https://youtu.be/_-3RZnfinHI?t=1229) | 式 (11-55)–(11-62)，pp. 511–512 |
| Wiener 過程 | [▶ 39:21](https://youtu.be/_-3RZnfinHI?t=2361) | Example 11-10，pp. 512–513 |
| 傅立葉 = KL（WSS） | [▶ 62:24](https://youtu.be/_-3RZnfinHI?t=3744) | §11-4 預告 |

---

## 1. 補充一：Poisson 求和公式的直覺

[▶ 00:00](https://youtu.be/_-3RZnfinHI?t=0) 課本放在附錄，表示作者認為它是重要的**技巧**（也有重要的觀念）。老師說最好看得很熟，後面幾章的推導常用到：

> **直覺**：看到連加很多個**整數倍**的指數項，立刻聯想到**一串連續的脈衝**，兩者完全相等：
> $$\sum_ne^{jn\omega_0x}=T\sum_n\delta(x+nT),\quad\omega_0=\frac{2\pi}T.$$

不用真的背（隨時查得到），但要有直覺。通訊上非常常用，取樣就是它。

---

## 2. 補充二：平滑濾波器用配方法（不用對函數微分）

[▶ 01:33](https://youtu.be/_-3RZnfinHI?t=93) 第 21 集求最佳平滑濾波器時，對一個積分式的某個值做微分——那是取巧的做法，有些同學覺得怪。換一個方法：**配方法**（只要兩步）。

Lagrange 乘數的目標函數，把積分寫在一起（後面都是常數）：
$$J=\frac{N_0}{2}\int h^2(\tau)d\tau-\lambda_1\int h(\tau)d\tau-\lambda_2\int\tau^2h(\tau)d\tau=\frac{N_0}{2}\int\left[h(\tau)-\frac{\lambda_1+\lambda_2\tau^2}{N_0}\right]^2d\tau-(\text{常數}).$$

- 把 $h(\tau)$ 當成單一變數，做高中的配方法：$x^2-2bx=(x-b)^2-b^2$。
- 其他項都和 $h$ 無關，只有平方那一項有關，而它只會讓積分**增加**。所以 $h(\tau)\ne\frac{\lambda_1+\lambda_2\tau^2}{N_0}$ 時積分只會變大。
- 最佳解 $h(\tau)=\frac{\lambda_1+\lambda_2\tau^2}{N_0}$，和用微分的結果一樣。

老師說：配方就相當於做微分；三次以上就用高中多項式的方法找極值。如果對「對函數做微分」理解上有困難（的確要 Riemann 可積的函數才能那樣做），就用配方法。同一個證明有不同的方法，選讓自己比較理解的。

---

## 3. 補充三：AR 過程的隱含假設——WSS

[▶ 05:07](https://youtu.be/_-3RZnfinHI?t=307) AR 用過去的輸出改變現在的輸出，讓影響無限延續，現在很多 model 都用。上一集推 Yule–Walker 時，**隱含假設過程是 WSS**（才能寫成 $R[m]$ 只看時間差）。看書要看證明，因為要看它的假設。

### 3.1 「可預測」的兩種定義

[▶ 09:46](https://youtu.be/_-3RZnfinHI?t=586) 例：$b_0=0$、$a=2$：$X[t]=2X[t-1]$。

- **文字定義**：用過去的值百分之百預測未來 → 知道 $X[t-1]$ 就百分之百知道 $X[t]$（兩倍），所以**是**可預測的。
- **有些書（包括課本）的定義**：可預測 = **線譜**。線譜的根都是 $e^{j\omega_i}$，全部在**單位圓上**。$a=2$ 的根在單位圓**外**，所以**不是**線譜。

**釐清**：「可預測 ⇔ 線譜」確實可以證明（第 13 章），但**前提是 WSS**，書上沒特別強調，所以產生混淆。正確說法：
> **WSS 的可預測過程 ⇔ 線譜。**

$a=2$ 或 $a=\frac12$ 從文字意義看都是可預測的，但它們不是 WSS（不穩定），被排除在這個條件外。AR 過程的根跑掉時，可能是 non-stable、non-stationary 的過程。

### 3.2 $|a|>1$ 不是 WSS 的證明

[▶ 12:49](https://youtu.be/_-3RZnfinHI?t=769) 非平穩時 Yule–Walker 還是對的，只是自相關要寫成 $R(t,t)$、$R(t,t-1)$……不能相減。

**反證**：假設 $X[n]-aX[n-1]=b\,I[n]$ 是 WSS，則 Yule–Walker 成立：
$$R[0]-aR[1]=b^2,\qquad R[1]-aR[0]=0.$$
兩個未知數、兩個方程式，唯一解：
$$R[0]=\frac{b^2}{1-a^2},\qquad R[1]=\frac{ab^2}{1-a^2}.$$
$a=2$ 時 $R[0]=\frac{b^2}{1-4}<0$。但自相關在 0 不可能是負的（是功率）。矛盾，所以**不是 WSS**。 ∎

直觀：$a=\frac12$（$b_0=0$）時，給一個 1，下一次變 $\frac12$、再 $\frac14$……越來越小最後不見；$a=2$ 時越來越大爆掉。都不是穩態。課本不討論，因為整本書著重在 stationary process，所以 $M=0$、$b_0=0$ 的情況只考慮**根在單位圓上**。如果你真的需要一個會慢慢衰減的非平穩過程，就知道它是什麼了。

### 3.3 沒有輸入的系統

[▶ 17:53](https://youtu.be/_-3RZnfinHI?t=1073) 之前說「穩定濾波器：WSS 輸入 ⇒ WSS 輸出」。$b_0=0$ 的 AR 能用這句話嗎？**不能**：這個系統**沒有輸入**（inputless），沒有地方讓你放 WSS 的輸入。所以它可能穩態、可能不穩態，完全由係數的根的位置決定。

---

## 4. 補充四：MA 就是卷積

[▶ 18:56](https://youtu.be/_-3RZnfinHI?t=1136)

- MA $X[n]=\sum_kb_kI[n-k]$ 就是卷積，係數 $b_k$ 就是 $h[k]$。
- 任何能用卷積定義的系統：order 有限就是 MA；不有限也可以視為 MA 的延伸。
- 有限個值的平方和或絕對值和一定有限，所以一定穩定。**有限長度脈衝響應（FIR）和 MA 是同一件事。**

---

## 5. Karhunen–Loève 展開

### 5.1 正交基與投影

[▶ 20:29](https://youtu.be/_-3RZnfinHI?t=1229) Fourier 級數得到的係數 $c_n$ 是**可數個**（不再是連續函數），很棒；但只有均方週期時才不相關。有沒有一種投影，可數個係數保證不相關？

老師說 Karhunen（芬蘭人）和 Loève（猶太裔法國人，二戰時被抓進集中營、在集中營裡寫書，幸運沒被殺，後來去了美國）做了這個研究。【口頭】

> **展開形式**：
> $$\hat X(t)=\sum_{n=1}^{\infty}c_n\varphi_n(t),\quad0<t<T;\qquad c_n=\int_0^TX(t)\varphi_n^*(t)\,dt\qquad\text{(11-55), (11-57)},$$
> $\{\varphi_n\}$ 在 $(0,T)$ 上**正交歸一** (orthonormal)：
> $$\int_0^T\varphi_n(t)\varphi_m^*(t)\,dt=\delta[n-m]\qquad\text{(11-56)}.$$

- **內積** (inner product)：通訊和很多領域裡，兩個函數的內積定義為兩個函數相乘（複數加共軛）再積分。之所以有用，是因為**實作就是這樣做**：兩個訊號波相乘、積分一個範圍（例如 0 到 $T$）。內積要滿足四個基本性質，這個定義完全符合。
- 線性代數的類比：三個正交的函數 $\varphi_1,\varphi_2,\varphi_3$ 當軸，隨機過程 $X$ 是一個向量；$c_n$ 就是 $X$ 在各軸上的**投影**（內積）。用投影值乘原來的函數做線性組合，希望就是原來的函數。

**還需要一個條件**：正交歸一還不夠，$\varphi_n$ 要是隨機過程「核」(kernel) 的**特徵函數**。

### 5.2 定理：特徵函數的投影係數正交

> **KL 定理**：若 $\varphi_n$ 是積分方程的特徵函數 (eigenfunction)
> $$\int_0^TR(t_1,t_2)\varphi_n(t_2)\,dt_2=\lambda_n\varphi_n(t_1),\quad0<t_1<T\qquad\text{(11-58)},$$
> 則投影係數彼此**正交**：
> $$E\{c_nc_m^*\}=\lambda_n\delta[n-m]\qquad\text{(11-61)},$$
> 而且 $E|\hat X(t)-X(t)|^2=0$，$0<t<T$（式 (11-60)）。

**特徵向量的直觀**【口頭】：$Av=\lambda v$——系統運作 $A$ 之後一定回到某個特定的方向 $\lambda v$；再乘一次 $A$ 還是同一個方向。所以在那個方向就定住了，是一個穩態、收斂的方向。特徵函數是運作時非常重要的方向。

- **不需要 WSS**：公式裡是 $R(t,s)$（逗點），不是 $t-s$。這樣的函數通常存在，因為自相關保證非負定。
- 驗證：之前 Fourier 級數投影就是特例——WSS、均方週期時，$R(t-s)$ 的特徵函數就是 $e^{jn\omega_0t}$。

**證明**（老師說只有四行，很多老師考這個）[▶ 26:02](https://youtu.be/_-3RZnfinHI?t=1562)：
$$E\{c_nc_m^*\}=E\left\{\int_0^TX(t)\varphi_n^*(t)dt\int_0^TX^*(s)\varphi_m(s)ds\right\}=\int_0^T\left[\int_0^TR^*(s,t)\varphi_n^*(t)dt\right]\varphi_m(s)\,ds.$$
（期望值和積分互換。）括號裡就是特徵方程（取共軛）：$=\lambda_n\varphi_n^*(s)$。只用這一個性質（矩陣乘特徵函數 = 特徵值乘特徵函數）。再用正交：
$$=\lambda_n\int_0^T\varphi_n^*(s)\varphi_m(s)\,ds=\lambda_n\delta[n-m].$$ ∎

（$\lambda_n$ 是實數，共軛不影響。）

**實作上**【口頭】：理論上非常喜歡用 KL 展開，實作上通常很難——要用特徵函數合成通訊訊號，特徵函數都是很怪的波形，做不出來。但特殊情況下特徵函數的格式固定：傅立葉轉換就是一種；矩陣有循環性質時，傅立葉的根就是它的特徵函數，就可以運作。還是有人在 channel estimation 用特徵函數，做得蠻成功的。

### 5.3 特徵值是能量

[▶ 28:07](https://youtu.be/_-3RZnfinHI?t=1687)
$$\lambda_n=E|c_n|^2.$$
- 特徵值一律非負（最小是 0；是 0 就不要了）、純實數。
- 它是係數的平方——**能量**的單位：投影到某一軸上的功率。
- 應用【口頭】：MIMO 傳輸有人只用主要的幾根特徵函數（特徵值最大的那幾個），其他設為 0，通常可以抓到最大的重點。Markov source 有 transition matrix，換成特徵值、特徵向量後，**最大的特徵值決定收斂到 entropy rate 的速度**。特徵值決定很多東西。

### 5.4 Mercer 定理

[▶ 30:39](https://youtu.be/_-3RZnfinHI?t=1839)

> **Mercer 定理**：任何自相關都可以寫成特徵值、特徵函數的和：
> $$R(t,s)=\sum_n\lambda_n\varphi_n(t)\varphi_n^*(s),\qquad R(t,t)=\sum_n\lambda_n|\varphi_n(t)|^2\qquad\text{(11-59)}.$$

- 是線性代數 $A=S\Lambda S^{-1}$（$S$ 是特徵向量組成的矩陣、$\Lambda$ 是特徵值對角矩陣）的**連續版本**。由定義 $AS=S\Lambda$ 直接得到，不用證；對稱矩陣基本上可逆。
- 老師說它在某些狀況有用，沒給證明；這是課本 (11-59) 的 $t_1=t_2$ 特例，一般 $t\ne s$ 的版本是 Mercer 定理。

### 5.5 區間內均方相等

[▶ 32:12](https://youtu.be/_-3RZnfinHI?t=1932) 證明和上一集**完全一樣**：展開四項，證明四項都相等；但比 Fourier 級數**乾淨很多**（所以理論上——例如資訊理論——KL 展開用得非常多，是基本技巧）。

- 第一項：$E|\hat X|^2=\sum_n\sum_mE\{c_nc_m^*\}\varphi_n\varphi_m^*=\sum_n\lambda_n|\varphi_n(t)|^2=R(t,t)$（期望值和求和互換、係數正交、Mercer）。等於第四項。
- 第二項：$E\{\hat XX^*\}=\sum_n\varphi_n(t)E\{c_nX^*(t)\}$，係數代投影、積分和期望值互換，得特徵方程 $\lambda_n\varphi_n^*(t)$，所以 $=\sum_n\lambda_n|\varphi_n|^2=R(t,t)$。
- 第三項同理。四項相等，得證。

**外面呢？** [▶ 36:20](https://youtu.be/_-3RZnfinHI?t=2180) $t>T$ 或 $t<0$：case by case，只保證 $(0,T)$ 內準，因為投影只用了 $(0,T)$ 的資料。若外面和裡面有對應的性質（例如 WSS 且均方週期，Fourier 級數是它的特徵函數），雖然只積 $(0,T)$，但性質重複，相當於從 $-\infty$ 積到 $\infty$ 全進來了，所以所有範圍都準。

【課本補充】p. 512：反過來也對——若 $\varphi_n$ 正交歸一、$X=\sum c_n\varphi_n$ 且 $E\{c_nc_m^*\}=\sigma_n^2\delta[n-m]$，則 $\varphi_n$ 必滿足 (11-58)、$\lambda=\sigma_n^2$。KL 展開中 $X(t)$ 不必平穩；若平穩，原點可以任意選。Example 11-9：理想低通過程 $R(\tau)=\frac{\sin a\tau}{\pi\tau}$，特徵函數是**長橢球函數** (prolate-spheroidal functions)。

---

## 6. 例：Wiener 過程的 KL 展開

[▶ 39:21](https://youtu.be/_-3RZnfinHI?t=2361) 特徵向量有方法算（正規化成 canonical／echelon form，算 null space，不需要 Gram–Schmidt）；但**特徵函數的推導比較 tricky、case by case**。老師用 Wiener 過程示範。

> **Wiener 過程**：和 Poisson 過程類似，用性質定義：$W(0)=0$；$W(t_2)-W(t_1)$ 是**零平均高斯**，變異數 $\alpha(t_2-t_1)$；不重疊區間的增量**獨立**。

- 時間差越大，變異越大。用來描述小粒子（量子）的碰撞行為、**布朗運動** (Brownian motion) 非常適合。Wiener 研究了布朗運動的一些概念（愛因斯坦的重要成果也是布朗運動）。【口頭】

**Step 1：自相關**（和 Poisson 一樣拆區間，用獨立增量）。$t_{\min}<t_{\max}$：
$$E\{W(t_{\min})W(t_{\max})\}=E\{W^2(t_{\min})\}+E\{W(t_{\min})\}E\{W(t_{\max})-W(t_{\min})\}=\alpha t_{\min}+0.$$
（零平均，第二項不見；Poisson 不是零平均所以有 $\lambda^2t_1t_2$。）
$$R(t_1,t_2)=\alpha\min(t_1,t_2).$$
顯然不是 WSS。

**Step 2：特徵方程（積分方程）。**
$$\int_0^T\alpha\min(t,s)\varphi(s)\,ds=\lambda\varphi(t).$$
大一學的是**微分方程**，這是積分方程——用微分把它導成熟悉的形式。

**Step 3：拆掉 min**（看到 min／max 一定要拆掉，它對微分、積分很麻煩）：$s<t$ 時 min 是 $s$，$s>t$ 時是 $t$：
$$\alpha\int_0^ts\varphi(s)\,ds+\alpha t\int_t^T\varphi(s)\,ds=\lambda\varphi(t)\qquad(A_1).$$

**Step 4：微分一次**（積分上限是 $t$，對 $t$ 微分就是把被積函數代 $t$；第二項是乘積，微分有兩項，下限 $t$ 微分帶負號）：
$$\alpha t\varphi(t)+\alpha\int_t^T\varphi(s)\,ds-\alpha t\varphi(t)=\lambda\varphi'(t)\ \Rightarrow\ \alpha\int_t^T\varphi(s)\,ds=\lambda\varphi'(t)\qquad(A_2).$$
（第一、三項消掉。）

**Step 5：再微分一次**，積分沒了：
$$-\alpha\varphi(t)=\lambda\varphi''(t)\ \Rightarrow\ \varphi''(t)+\frac{\alpha}{\lambda}\varphi(t)=0.$$
大一微積分、電路學常用的二階微分方程。

**Step 6：初始條件要回原式找。** 微分會讓資訊消失：$f=g$ 時微分相等，但 $f=g+c$ 微分也相等。所以最後的方程式解出來不一定滿足原式，**初始條件要從原來的 $A_1$、$A_2$ 找**，通常在**邊界** $t=0$、$t=T$（四個機會）：
- $A_1$ 代 $t=0$：兩個積分都是 0（或乘 0），得 $\varphi(0)=0$。
- $A_2$ 代 $t=T$：積分是 0，得 $\varphi'(T)=0$。
（剛好找到兩個；找到更少就不夠，解完要代回原式確認。）

**Step 7：解。** 二階常係數方程 $y''+by=0$ 的解有三種：$b=0$ 是 $1,x$；$b<0$ 是指數；$b>0$ 是 $\cos,\sin$。這裡 $\lambda>0$（特徵值非負）、$\alpha>0$（是變異數，自相關在 $t$ 到 $t$），所以 $b=\frac\alpha\lambda>0$：
$$\varphi(t)=c_1\cos\sqrt{\tfrac\alpha\lambda}\,t+c_2\sin\sqrt{\tfrac\alpha\lambda}\,t.$$
（老師說這些公式網路上都查得到。他在修實變分析 (Real Analysis) 時才發現微積分裡有很多概念——Riemann 積分、Lebesgue 積分等。）

**Step 8：三個未知數、三個條件**（$c_1$、$c_2$、$\lambda$；第三個條件是**正交歸一**：$\int_0^T\varphi^2=1$）：
1. $\varphi(0)=0$ ⇒ $c_1=0$。
2. $\varphi'(T)=c_2\sqrt{\frac\alpha\lambda}\cos\sqrt{\frac\alpha\lambda}T=0$ ⇒ $\sqrt{\frac{\alpha}{\lambda}}T=\frac{(2n+1)\pi}{2}$（$\frac\pi2$ 的奇數倍）。
3. $\int_0^Tc_2^2\sin^2(\cdot)dt=c_2^2\left(\frac T2-\int\frac{\cos2(\cdot)}{2}\right)=\frac{c_2^2T}{2}=1$ ⇒ $c_2=\sqrt{\frac2T}$。（$\sin^2A=\frac{1-\cos2A}{2}$，cos 那項積一整個週期是 0。）

> **Wiener 過程的特徵函數與特徵值**：
> $$\varphi_n(t)=\sqrt{\frac2T}\sin\frac{(2n+1)\pi t}{2T},\qquad\lambda_n=\frac{4\alpha T^2}{(2n+1)^2\pi^2},\qquad n=0,1,2,\dots$$
> 無限多個。

**Step 9：驗證正交。** 兩個三角函數相乘一定要拆成單一的：$\sin A\sin B=\frac12[\cos(A-B)-\cos(A+B)]$。正規化後積分範圍是 $(0,1)$，$k_n$、$k_m$ 都是整數，只有一種情況積分是 1（delta）；兩個 delta 不會同時是 1（要 $k_n=k_m$ 且 $k_n+k_m+1=0$，沒有整數解）。
- 結果 $1$：自己和自己，完整能量 1。
- 結果 $-1$：兩個差一個負號（例如 $\frac32$ 和 $-\frac32$）——完全反向，是同一個向量。所以**只取 $2k_n+1>0$ 的**，負的就是正的那個加負號。

所以布朗運動可以拆成特徵函數和投影的組合；常把係數乘 $\sqrt{\frac T2}$ 調整，讓 $X(t)=\sum C_n'\sin(\cdot)$，比較乾淨。老師說：看完應該覺得「叫我求特徵函數，我不要做」——有些情況特徵函數很不好求，求出來搞不好就是一篇論文。

---

## 7. WSS 時：傅立葉轉換就是 KL 展開

[▶ 62:24](https://youtu.be/_-3RZnfinHI?t=3744) 有些書或論文說：**傅立葉轉換本身就是在做特徵值和特徵函數**——傅立葉的根是特徵函數，投影出來的頻譜是特徵值。什麼時候可以這樣說？

**WSS**（積分範圍 $-\infty$ 到 $\infty$）：特徵方程
$$\int_{-\infty}^{\infty}R(t-s)\varphi(s)\,ds=\lambda\varphi(t)$$
是一個**卷積**（就像 OFDM：把 $H$ 改成 circular shift 時，特徵向量就是傅立葉級數的根；這和實作有關）。頻譜上卷積變相乘：
$$S(\omega)\Phi(\omega)=\lambda\Phi(\omega)\ \Leftrightarrow\ \left[S(\omega)-\lambda\right]\Phi(\omega)=0.$$

**討論**：兩個實數相乘是 0，至少一個是 0。
- $S(\omega)\ne\lambda$ 的地方：$\Phi(\omega)$ 一定是 0。
- $S(\omega)=\lambda$ 的地方（畫頻譜，水平線 $\lambda$ 和它相交的點，例如兩點）：$\Phi$ 可以不是 0。但不能讓它也是 0（否則特徵函數沒有能量，總積分要是 1），所以**唯一的選擇是放一個脈衝**。
- 兩個交點 → 一個特徵值對應兩個特徵向量（重根），各選一個脈衝。

所以特徵函數的傅立葉轉換是**單一脈衝**，回到時域就是**單頻**：
$$\varphi_u(t)=\frac{1}{\sqrt{2\pi}}e^{jut},\qquad\lambda_u=S(u).$$

⚠️ 逐字稿缺字：[▶ 69:31](https://youtu.be/_-3RZnfinHI?t=4171) 老師當場修正投影片：原本寫 $\frac{1}{2\pi}$ 不對，應是 $\frac{1}{\sqrt{2\pi}}$（第 77 張投影片），兩個 $\frac{1}{\sqrt{2\pi}}$ 相乘積分才得到 $\delta(\omega_1-\omega_2)$：同一個特徵函數總面積 1，不同的正交。

**投影係數**：$X$ 對特徵函數的共軛做投影（共軛使正號變負號）：
$$c(u)=\frac{1}{\sqrt{2\pi}}\int X(t)e^{-jut}dt=\frac{X(u)}{\sqrt{2\pi}},\qquad X(t)=\int c(u)\varphi_u(t)\,du.$$
所以**對 WSS 過程，傅立葉轉換就是 KL 展開**——同一件事。

**嚴謹性**【口頭】：理論上有人覺得不夠嚴謹——特徵函數一般是可數個；這裡是**不可數**無限多個，也不是線性組合而是積分。但目的是讓大家看到這個觀念；而這個觀念帶出下一節。

**WSS 過程的頻域是白的** [▶ 74:10](https://youtu.be/_-3RZnfinHI?t=4450)：
- 觀察股市、河川流動等資料，如果是 WSS，有時很希望丟到頻域分析。為什麼？因為**任何 WSS 過程的傅立葉轉換 $X(\omega)$（本身也是隨機過程）都是白的**：
$$E\{X(u)X^*(v)\}=0,\quad u\ne v.$$
- 但它是**非平穩**的白（時變白，第 5 集）。
- 任何兩個頻率在隨機上都沒有關係（不相關、正交）；高斯過程更好，是獨立的。
- 結論：特徵值就是 $S(\omega)$（配上 $\frac1{\sqrt{2\pi}}$ 的係數）。

（這是下一節 §11-4 的主題。）

---

## 8. 一頁速查表

### 補充

- Poisson 求和：整數倍指數連加 = 一串脈衝。
- 平滑濾波器：配方 $J=\frac{N_0}2\int[h-\frac{\lambda_1+\lambda_2\tau^2}{N_0}]^2-c$。
- WSS 可預測 ⇔ 線譜；$|a|>1$ 的 AR 非 WSS（Yule–Walker 得 $R[0]=\frac{b^2}{1-a^2}<0$）。
- MA = 卷積 = FIR，一定穩定。

### KL 展開

| 項目 | 公式 |
|---|---|
| 展開 | $\hat X=\sum c_n\varphi_n$，$c_n=\int_0^TX\varphi_n^*$，$0<t<T$ |
| 特徵方程 | $\int_0^TR(t,s)\varphi_n(s)ds=\lambda_n\varphi_n(t)$ |
| 係數正交 | $E\{c_nc_m^*\}=\lambda_n\delta[n-m]$（不需 WSS） |
| 特徵值 | $\lambda_n=E\lvert c_n\rvert^2\ge0$（能量） |
| Mercer | $R(t,s)=\sum\lambda_n\varphi_n(t)\varphi_n^*(s)$ |

- 正交證明關鍵：期望值積分互換 → 特徵方程 → 正交歸一。

### Wiener 過程

$R=\alpha\min(t_1,t_2)$；$\varphi''+\frac\alpha\lambda\varphi=0$，$\varphi(0)=0$、$\varphi'(T)=0$；
$$\varphi_n=\sqrt{\tfrac2T}\sin\tfrac{(2n+1)\pi t}{2T},\quad\lambda_n=\tfrac{4\alpha T^2}{(2n+1)^2\pi^2}.$$
- 技巧：拆 min、微分兩次、初始條件回原式找。

### WSS：傅立葉 = KL

$\varphi_u=\frac{1}{\sqrt{2\pi}}e^{jut}$，$\lambda_u=S(u)$，$c(u)=\frac{X(u)}{\sqrt{2\pi}}$；$X(\omega)$ 是（非平穩的）白過程。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| WSS 的 $X(\omega)$ 是白的 | 下一集：§11-4 隨機過程的頻譜表示 |
| WSS 可預測 ⇔ 線譜 | §13-2（第 39–40 集）證明 |
| 特徵值、能量 | 資訊理論、MIMO |
| Wiener 過程、布朗運動 | §10-1 random walk（課程跳過） |

---

## 附：本集一句話總結

> **Karhunen–Loève 展開用自相關核的特徵函數當正交基做投影，任何過程（不必平穩）的係數都互相正交、特徵值就是投影的能量，並在區間內均方重建原過程；Wiener 過程的特徵函數是 $\sqrt{2/T}\sin\frac{(2n+1)\pi t}{2T}$；而對 WSS 過程，特徵方程是卷積，特徵函數就是單頻 $e^{jut}/\sqrt{2\pi}$——傅立葉轉換就是 KL 展開，頻域是白的。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-3 (2/2) 錄影逐字稿（whisper large-v3-turbo，1:16:33）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
