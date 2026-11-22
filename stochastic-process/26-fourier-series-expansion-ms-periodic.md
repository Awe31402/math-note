---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 26
lecture: Lec 11-3 Spectral Representation — Fourier Series and Karhunen–Loève Expansions (1/2)
date: 待補
video: https://youtu.be/Jfq9RG-xsZg
notes: Papoulis & Pillai 4th ed. §11-3 Fourier Series（式 (11-50)–(11-54)、Theorem 11-1，pp. 509–510）；附錄 10A Poisson 求和公式
---

# 第 26 集 · Lec 11-3 (1/2)：隨機過程的 Fourier 級數展開——一個區間內均方相等、為什麼不含端點、均方週期時係數不相關 [▶ 影片](https://youtu.be/Jfq9RG-xsZg)

← 上一集：[25](25-ar-ma-arma-yule-walker-line-spectrum.md) ｜ [總目錄](README.md) ｜ 下一集：[27](27-karhunen-loeve-expansion-wiener-process-fourier-eigenfunctions.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 26 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（25:20，whisper large-v3-turbo）＋ Papoulis §11-3（pp. 509–510）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Fourier series」→「Fullier Series」，「approximation」→「approsimation」，「wide-sense stationary」→「Wisen Station／y線stationary／wise and stationary」，「mean square」→「mean square」，「complex conjugate」→「complete count／complete conjugate」，「Karhunen–Loève」→「Kahunen Love」，「Poisson sum formula」→「Person Sum Formula／poison sum formula／prozone sum formula／Portone Sumfirm」，「indicator function」→「indicator function」，「replication property」→「replication property」，「indeterminate」→「indeterminate」，「MS periodic」→「mx periodic／ms periodic」，「uncorrelated」→「uncoerated／uncorelated」，「zero mean」→「zero mean」，「技術（係數）」→「技術／技數」，「實數」→「時數」，「X hat」→「X-Head／x hat」。以下一律用正確的字。

> **接上一集**：上一集介紹線譜：一堆頻率乘上係數 $c_n$ 組合起來（可預測過程）。§11-3 是延伸：如果頻率是**某個基本頻率的整數倍**，用投影得到係數，組合出來的會不會是原過程的好近似？答案：**在你關心的區間內，均方意義下完全相等**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 動機：從線譜到 Fourier 級數](#1-動機從線譜到-fourier-級數)
- [2. 定理：區間內均方相等](#2-定理區間內均方相等)
- [3. 證明：四項都相等](#3-證明四項都相等)
  - [3.1 第一項 $E|\hat X|^2$](#31-第一項-ehat-x2)
  - [3.2 第二、三項](#32-第二三項)
- [4. 為什麼不包含端點](#4-為什麼不包含端點)
- [5. 均方週期：處處相等](#5-均方週期處處相等)
- [6. Theorem 11-1：均方週期時係數不相關](#6-theorem-11-1均方週期時係數不相關)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 動機、定理 | [▶ 00:00](https://youtu.be/Jfq9RG-xsZg?t=0) | 式 (11-51)、(11-54)，p. 510 |
| 證明 | [▶ 03:39](https://youtu.be/Jfq9RG-xsZg?t=219) | Prob. 11-12；附錄 10A |
| 端點 | [▶ 17:26](https://youtu.be/Jfq9RG-xsZg?t=1046) | 無（【口頭】） |
| 均方週期、Theorem 11-1 | [▶ 14:25](https://youtu.be/Jfq9RG-xsZg?t=865) | Theorem 11-1，式 (11-52)、(11-53)，p. 510 |

---

## 1. 動機：從線譜到 Fourier 級數

[▶ 00:00](https://youtu.be/Jfq9RG-xsZg?t=0)

- 上一集的線譜：頻率 $\omega_1,\omega_2,\omega_3$（例如三個）乘係數組合，是可預測過程，三階就能實作。
- 這裡頻率是 **$n\omega_0$**——基本頻率的**整數倍**（1 倍、2 倍、3 倍……），$\omega_0=\frac{2\pi}{T}$。
- 用**投影**得到係數：$c_n=\frac1T\int_0^TX(t)e^{-jn\omega_0t}dt$——這就是 **Fourier 級數**（標題的由來）。

> **Fourier 級數展開**：給 WSS 過程 $X(t)$，取一個區間 $(0,T)$，令
> $$\hat X(t)=\sum_{n=-\infty}^{\infty}c_ne^{jn\omega_0t},\qquad c_n=\frac1T\int_0^TX(t)e^{-jn\omega_0t}dt,\qquad\omega_0=\frac{2\pi}{T}\qquad\text{(11-51)}.$$

**問題**：這個新的隨機過程形式比較簡單（離散的係數），它會不會是 $X(t)$ 的好近似？

---

## 2. 定理：區間內均方相等

[▶ 01:33](https://youtu.be/Jfq9RG-xsZg?t=93)

> **定理**：$X(t)$ 是 WSS（不一定週期），則
> $$E\left|\hat X(t)-X(t)\right|^2=0,\qquad0<t<T\qquad\text{(11-54)}.$$

**圖像**【口頭】：$X(t)$ 是隨機的，外面是什麼不知道（外面也是隨機的）。我只關心一段時間，例如今天一整天 24 小時。連續的過程，我想用**離散**的方式表示：在頻譜上取一堆整數倍的頻率，用投影得到的係數做線性組合，得到 $\hat X(t)$。

- 在**這一段時間**內，$\hat X$ 和 $X$ **完全相等**（均方意義）——對這段期間的隨機過程完全了解。
- **外面**：只投影這一段，外面通常**不相等**。

【課本補充】p. 510：WSS 但不週期時，係數 $c_n$ **不正交**（$n$ 大時近似正交）。下一部分要說明任何過程（平穩或不平穩）都能展開成係數正交的級數（KL 展開）。

---

## 3. 證明：四項都相等

[▶ 03:39](https://youtu.be/Jfq9RG-xsZg?t=219) 老師說這個證明和後面另一個證明（KL 展開）數學上一樣，所以仔細講。

展開（複數，自己乘自己的共軛）：
$$E|\hat X-X|^2=E\{\hat X\hat X^*\}-E\{\hat XX^*\}-E\{X\hat X^*\}+E\{XX^*\}.$$

**觀念**：每一項算出來**都相等**（都等於 $R(0)$），加兩次減兩次就是 0。原因是投影很完整——$\hat X$ 和 $X$ 當輸入輸出看的話，互相關和自相關都相等。後面的 KL 展開、各種投影都是類似的概念。

### 3.1 第一項 $E|\hat X|^2$

[▶ 05:41](https://youtu.be/Jfq9RG-xsZg?t=341)

**Step 1：代入。**
$$E\{\hat X(t)\hat X^*(t)\}=\sum_n\sum_m\frac{1}{T^2}\int_0^T\!\!\int_0^TR(u-v)e^{-jn\omega_0u}e^{jm\omega_0v}\,du\,dv\cdot e^{jn\omega_0t}e^{-jm\omega_0t}.$$
（期望值和積分互換。）

**Step 2：求和與積分對調**（老師說：通訊上、機率上最常做的就是一直對調積分和求和，讓它容易算）。先求和：
$$\sum_ne^{jn\omega_0(t-u)}=T\sum_n\delta(t-u+nT).$$
這是 **Poisson 求和公式**（附錄 10A）：一堆指數旋轉的和 = 一堆 delta 的和。老師說它很有用，運算上要記得。

**Step 3：再對調**，讓 delta 和積分對消。**但要小心積分範圍是有限的**：
- 積分範圍是整條數線時，delta 一定會碰到，直接對消。
- 現在只積 $(0,T)$：脈衝出現在範圍**內**，積分是 1；在範圍**外**，積分是 0。
- 所以用**指示函數** (indicator function)：
$$\int_0^T\delta(t-u+nT)f(u)\,du=f(t+nT)\,\mathbf{1}\left[0<t+nT<T\right].$$
  對 $v$ 同理，得 $\mathbf{1}[0<t-mT<T]$（符號依變數設定）。

**Step 4：指示函數和求和對消。** $\mathbf{1}[0<t+nT<T]$ 等價於 $-\frac tT<n<1-\frac tT$：一個**寬度為 1** 的區間（上界減下界 = 1），裡面**只有一個整數**。
- 例：下界 0.8、上界 1.8，裡面只有 $n=1$。
- 這裡 $0<t<T$（沒有等號），所以 $\frac tT\in(0,1)$，$-\frac tT\in(-1,0)$，**唯一的整數是 $n=0$**；$m$ 也一樣是 0。
- 求和根本沒用，只剩一項：
$$E\{\hat X\hat X^*\}=R(0)=E\{XX^*\}.$$
第一項 = 第四項。

老師說：中間用了幾乎所有之前的技巧——delta 函數、Poisson 求和公式。

### 3.2 第二、三項

[▶ 12:23](https://youtu.be/Jfq9RG-xsZg?t=743) 一樣照做，只有一個求和、一個積分，寫起來簡單：
$$E\{\hat X(t)X^*(t)\}=\sum_n\frac1T\int_0^TR(u-t)e^{-jn\omega_0u}du\,e^{jn\omega_0t}.$$
對調、Poisson 求和公式、指示函數，只剩一個整數 $m'$：因為 $0<t<T$，$m'=0$，所以 $=R(0)$。老師說寫 $m'$ 是因為後面會證更廣義的東西，那時整數不一定是 0。第三項同理（得到的整數和第二項差一個負號）。

第四項就是 $R(0)$。四項相等，兩加兩減 = 0。 ∎

---

## 4. 為什麼不包含端點

[▶ 17:26](https://youtu.be/Jfq9RG-xsZg?t=1046) 定理寫 $0<t<T$，**沒有等號**。為什麼？中間用到「delta 和積分對消」：
$$\int_0^T\delta(t)\,dt=\int_{-\infty}^{\infty}\mathbf{1}[0<t<T]\,\delta(t)\,dt.$$
delta 只有一個性質可用：**複製性質**——把函數 $g$ 在脈衝那一點的值帶出來，**但那一點必須是 $g$ 的連續點**。指示函數在 0 和 $T$ 是**不連續**的（有跳躍），脈衝剛好出現在積分範圍的邊界，所以**不能對消，結果是 indeterminate**。有的文章會忽略這一點；老師說這是吹毛求疵，但要講數學嚴謹性就必須這樣。

---

## 5. 均方週期：處處相等

[▶ 14:25](https://youtu.be/Jfq9RG-xsZg?t=865)

> 若 $X(t)$ **均方週期**、週期剛好是 $T$（$E|X(t+T)-X(t)|^2=0$），則只要投影**一個週期**，$\hat X(t)=X(t)$ 對**所有** $t\in\mathbb{R}$ 都成立（均方意義）。

- 證明技巧完全一樣，展開四項、四項相等；只是指示函數留下的整數 $m'$、$m''$ 不一定是 0（$t$ 不在 $(0,T)$ 內時），要一個週期一個週期討論。
- 用到：**均方週期 ⇔ 自相關也是週期的**（週期相同）——所以整數不同也沒關係，四項還是相等。
- 結論：在一次、二次（均方）的性質上，兩個過程完全吻合。

---

## 6. Theorem 11-1：均方週期時係數不相關

[▶ 21:29](https://youtu.be/Jfq9RG-xsZg?t=1289) 更好的結果（我們最喜歡的）：

> **Theorem 11-1**：$X(t)$ 是 WSS、均方週期（週期 $T$），則 $\hat X(t)=X(t)$（均方），而且係數**零平均、互不相關**（除了 $n=0$）：
> $$E\{c_n\}=\begin{cases}\eta_X,&n=0\\0,&n\ne0\end{cases}\qquad E\{c_nc_m^*\}=\begin{cases}\gamma_n,&n=m\\0,&n\ne m\end{cases}\qquad\text{(11-53)},$$
> $\gamma_n=\frac1T\int_0^TR(\tau)e^{-jn\omega_0\tau}d\tau$ 是 $R(\tau)$ 的 Fourier 係數。

- 我們一直希望係數不相關：兩個係數之間沒有能量的相互影響。
- 如果 $X$ 不是週期的，只投影一段，雖然能完全代表原過程，但係數可能相依、可能很強的相關。**只有均方週期時，投影出來的係數保證不相關、零平均**。

**零平均的奇怪之處**【口頭】：$X$ 沒有說零平均，但投影出來的係數是零平均——平均**只丟給 $n=0$ 那一個係數**。

**證明（平均）**：WSS，平均是常數 $\mu_X$，提出來：
$$E\{c_n\}=\frac{\mu_X}{T}\int_0^Te^{-jn\omega_0t}dt=\mu_X\,\delta[n].$$
積分剛好是一個週期（和 $\omega_0$ 切齊），$n\ne0$ 時是 0、$n=0$ 時是 1。

**證明（不相關）**：投影後，積分和期望值對調；WSS，只跟時間差有關；變數變換，自相關放在某一個積分，另一個積分剛好是 delta：
$$E\{c_nc_m^*\}=\frac1{T^2}\int_0^T\!\!\int_0^TR(t-s)e^{-jn\omega_0t}e^{jm\omega_0s}\,dt\,ds=\gamma_n\delta[n-m].$$
（用 $R$ 的週期性，內層積分得 $\gamma_ne^{-jn\omega_0s}$，外層 $\frac1T\int_0^Te^{-j(n-m)\omega_0s}ds=\delta[n-m]$。）

【課本補充】p. 510 的證明：$E\{c_nX^*(\alpha)\}=\frac1T\int_0^TR(t-\alpha)e^{-jn\omega_0t}dt=\gamma_ne^{-jn\omega_0\alpha}$，再得 $E\{c_nc_m^*\}=\gamma_n\delta[n-m]$；並由 $E|\hat X|^2=\sum\gamma_n=R(0)=E|X|^2$、$E\{\hat XX^*\}=\sum\gamma_n$ 得 (11-52)。式 (11-50)：WSS 均方週期 ⇔ $R(\tau)$ 週期 $T$，$R(\tau)=\sum\gamma_ne^{jn\omega_0\tau}$。

---

## 7. 一頁速查表

### Fourier 級數展開

$$\hat X(t)=\sum_nc_ne^{jn\omega_0t},\quad c_n=\frac1T\int_0^TX(t)e^{-jn\omega_0t}dt,\quad\omega_0=\frac{2\pi}T$$

| 情況 | 均方相等的範圍 | 係數 |
|---|---|---|
| WSS（不週期） | $0<t<T$（不含端點） | 不正交（$n$ 大時近似正交） |
| WSS 且均方週期 $T$ | 所有 $t$ | $n\ne0$ 零平均、不相關；$E\lvert c_n\rvert^2=\gamma_n$；$E c_0=\eta$ |

### 證明的關鍵

- 四項 $E\hat X\hat X^*$、$E\hat XX^*$、$EX\hat X^*$、$EXX^*$ 都等於 $R(0)$。
- Poisson 求和公式：$\sum_ne^{jn\omega_0x}=T\sum_n\delta(x+nT)$。
- 有限區間：$\int_0^T\delta(\cdot)$ 要用指示函數；寬度 1 的區間只有一個整數。
- 端點：指示函數不連續，複製性質不能用 → indeterminate。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 投影、四項相等的證明 | 下一集：Karhunen–Loève 展開（係數正交的展開） |
| 均方週期 ⇔ $R$ 週期 | 第 13–14 集回顧 |
| 不相關的係數 | §11-4 頻譜表示（第 28–29 集） |

---

## 附：本集一句話總結

> **把 WSS 過程在區間 $(0,T)$ 上投影到整數倍頻率 $e^{jn\omega_0t}$ 得到 Fourier 係數，組合回去在 $(0,T)$ 內（不含端點）均方意義下和原過程完全相等——證明靠 Poisson 求和公式讓四項都等於 $R(0)$；若過程均方週期 $T$，則處處相等，而且係數零平均、互不相關。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-3 (1/2) 錄影逐字稿（whisper large-v3-turbo，25:20）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
