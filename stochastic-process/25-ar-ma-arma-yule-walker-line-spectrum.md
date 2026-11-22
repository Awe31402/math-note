---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 25
lecture: Lec 11-2 Spectral Representation — Finite-Order Systems and State Variables (3/3)
date: 待補
video: https://youtu.be/0NWCoO9FGSk
notes: Papoulis & Pillai 4th ed. §11-2 Autoregressive processes、Line spectra、Moving average processes（式 (11-39)–(11-46)，pp. 507–508；Example 11-7）
---

# 第 25 集 · Lec 11-2 (3/3)：AR 過程與 Yule–Walker 方程、AR(1)、$|a|>1$ 不穩定、可預測過程（線譜）、MA、ARMA [▶ 影片](https://youtu.be/0NWCoO9FGSk)

← 上一集：[24](24-discrete-finite-order-processes-partial-fraction.md) ｜ [總目錄](README.md) ｜ 下一集：[26](26-fourier-series-expansion-ms-periodic.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 25 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（51:03，whisper large-v3-turbo）＋ Papoulis §11-2（pp. 507–508）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「autoregressive」→「Auto Regressive」（老師把 regressive 解釋成「退化」），「moving average」→「Moving Average」，「AR」→「Air／AR」，「uncorrelated」→「uncollated／uncollected」，「Yule–Walker」→「Your Walker」，「unit circle」→「單位員／單位元」，「wide-sense stationary」→「Y10／wise and／Wisen／weizen stationary」，「LTI」→「LTI」，「predictable」→「predictable」，「Wold decomposition」→「wall decomposition」，「line spectrum」→「Line Spectrum」，「Karhunen–Loève」→「Cohounen Love」，「Poisson sum formula」→「Poisson 3 Formula」，「impulse response」→「input／imput response」，「convolution」→「convolution」，「weighted average」→「weighted average」，「complex conjugate」→「complex conjugate」，「Fourier series」→「Fourier series」，「激勵（excitation）」→「excitation／sitation」，「Theorem 9-2」→「定理92」。以下一律用正確的字。

> **接上一集**：上一集完成了離散有限階過程的一般形式。這一集介紹三種很常見的特例——論文裡常看到的名詞：**AR**（autoregressive）、**MA**（moving average）、**ARMA**；以及 AR 的一個特例：分子為 0 的**可預測過程**（線譜）。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. AR 過程](#1-ar-過程)
  - [1.1 定義與名稱由來](#11-定義與名稱由來)
  - [1.2 影響無限延續](#12-影響無限延續)
- [2. 關鍵性質：不相關變數的線性組合仍不相關](#2-關鍵性質不相關變數的線性組合仍不相關)
- [3. Yule–Walker 方程](#3-yulewalker-方程)
- [4. 例：AR(1)](#4-例ar1)
- [5. $|a|>1$：不穩定、非平穩](#5-a1不穩定非平穩)
- [6. 分子為 0：可預測過程與線譜](#6-分子為-0可預測過程與線譜)
- [7. MA 過程](#7-ma-過程)
- [8. ARMA 過程](#8-arma-過程)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| AR 定義、名稱 | [▶ 00:00](https://youtu.be/0NWCoO9FGSk?t=0) | 式 (11-39)、(11-40)，p. 507 |
| Yule–Walker | [▶ 13:31](https://youtu.be/0NWCoO9FGSk?t=811) | 式 (11-41)，p. 508 |
| AR(1)、$\lvert a\rvert>1$ | [▶ 20:08](https://youtu.be/0NWCoO9FGSk?t=1208) | Example 11-7，p. 508 |
| 可預測過程、線譜 | [▶ 28:22](https://youtu.be/0NWCoO9FGSk?t=1702) | 式 (11-42)–(11-44)，p. 508 |
| MA、ARMA | [▶ 43:21](https://youtu.be/0NWCoO9FGSk?t=2601) | 式 (11-45)、(11-46)，p. 508 |

---

## 1. AR 過程

### 1.1 定義與名稱由來

[▶ 00:32](https://youtu.be/0NWCoO9FGSk?t=32)

> **AR 過程**（自迴歸，autoregressive）：innovation filter **只有分母是多項式，分子是常數**：
> $$L(z)=\frac{b_0}{1+a_1z^{-1}+\cdots+a_Nz^{-N}}\qquad\text{(11-39)}.$$

**注意**【口頭】：一般 AR 的定義**沒有要求根在單位圓內**（regular process 要求）。後面會討論根在外面會產生什麼。

**系統模型**：輸出 $X$、輸入 $I$，$\frac{X(z)}{I(z)}=L(z)$，交叉相乘（$z^{-1}$ 是一格延遲）：
$$X[n]+a_1X[n-1]+\cdots+a_NX[n-N]=b_0I[n]\qquad\text{(11-40)}.$$
輸入只乘 $b_0$；輸出和過去的輸出一起決定。

**為什麼叫 autoregressive**（老師的解釋：auto = 自我，regressive = 慢慢退化）[▶ 02:33](https://youtu.be/0NWCoO9FGSk?t=153)：
- 在 $t=0$ 送進一個脈衝，之後就停了（$I[1]=I[2]=\cdots=0$）。
- 但輸出會**一直循環**：例如 $X[2]-aX[1]=I[2]=0$，所以 $X[2]=aX[1]$，$X[3]=aX[2]$……自己灌給自己。
- $|a|<1$ 時慢慢衰減下來；係數是 1 就不會衰減，一直送下去（不合理）。
- 只激勵一次 (one excitation)，後面一直有輸出——**自我退化的循環**。

**用途**【口頭】：做估計、系統討論時常看到這種模型。它代表輸出的影響會**慢慢衰減、延續下去**——現在的輸出不會下一刻就沒影響了，很適合 model 影響會延續的系統，所以資料分析常用 AR model。

### 1.2 影響無限延續

[▶ 05:09](https://youtu.be/0NWCoO9FGSk?t=309) 現在的輸出由**過去 $N$ 個輸出**和**現在的輸入**完全決定。但每個過去的輸出又是更早輸入的函數，所以：

例：$X[t]-X[t-1]=I[t]$。寫 $X[t-1]-X[t-2]=I[t-1]$、……一直寫下去加起來，中間全部消掉：
$$X[t]=I[t]+I[t-1]+I[t-2]+\cdots.$$

- 現在的輸出 = **過去所有輸入**的線性組合，**無限多個**。
- 利用輸出的**回饋** (feedback)，讓所有過去輸入的影響都保留——曾經發生過的都拿來用。所以雖然叫 finite order，實際上是 **infinite order** 的影響。
- 應用：所有輸入的影響都要留下來、只是慢慢衰減（從小時候一歲、兩歲、三歲……所有東西的影響都在），就可以用 AR model。

---

## 2. 關鍵性質：不相關變數的線性組合仍不相關

[▶ 08:20](https://youtu.be/0NWCoO9FGSk?t=500)

- 兩組隨機變數 $\{X_i\}$、$\{Y_j\}$，任兩個（跨組）都不相關。用左邊的**函數**和右邊的**函數**產生兩個新的隨機變數，一般**不會**還是不相關。
- 如果是**獨立**：獨立隨機變數的函數還是獨立（獨立比較強，也比較好用）。
- **例外**：若函數是**線性組合**，$f=\sum c_iX_i$、$g=\sum d_jY_j$，則 $f$、$g$ 還是不相關（因為 $E[fg^*]=\sum\sum c_id_j^*E[X_iY_j^*]$，每一項都是 0）。這是喜歡線性系統的原因。

**應用**：輸入 $I$ 是白的。white 只是二階性質（功率頻譜是常數），也就是**不相關**。（可以假設 i.i.d.，那函數還是獨立；但這裡希望不要那麼強的性質。）所以 $I$ 的某一群和另一群做線性組合，彼此還是不相關。老師說：線性組合講二次的性質非常好，一切都在線性組合裡面。

**推論**：$X[t-m]$（$m>0$）是 $I[t-m],I[t-m-1],\dots$ 的線性組合，和現在的輸入 $I[t]$ 不相關；$I$ 零平均，所以
$$R_{XI}[-m]=E\{X[t-m]I[t]\}=0,\quad m>0.$$

---

## 3. Yule–Walker 方程

[▶ 13:31](https://youtu.be/0NWCoO9FGSk?t=811) 可以用第 9 章的觀念：輸入 $I$、輸出 $X$ 的線性系統，互相關經過一次濾波、自相關經過兩次（Theorem 9-2）。這裡直接用 (11-40) 推。

**Step 1：乘 $I[t]$ 取期望值。** 左邊 $X[t-1]I[t],X[t-2]I[t],\dots$ 的期望值都是 0（上一節），只剩 $X[t]I[t]$；WSS（輸入 WSS、線性濾波器 → 輸出 WSS，只看時間差 0）：
$$R_{XI}[0]=b_0E\{I^2\}=b_0.$$
（輸入是單位功率白雜訊。）

**Step 2：乘 $X[t-m]$ 取期望值。**
- $m=0$：$R[0]+a_1R[1]+\cdots+a_NR[N]=b_0R_{IX}[0]=b_0^2$。
- $m\ge1$：右邊 $E\{I[t]X[t-m]\}=0$。

老師說：這就是 Theorem 9-2 的事——$R_{XI}$ 當輸入經過一次濾波得到 $R_{XX}$，只是現在輸入輸出的記號換了。

> **Yule–Walker 方程**：
> $$\begin{aligned}R[0]+a_1R[1]+\cdots+a_NR[N]&=b_0^2\\R[1]+a_1R[0]+\cdots+a_NR[N-1]&=0\\&\ \ \vdots\\R[N]+a_1R[N-1]+\cdots+a_NR[0]&=0\end{aligned}\qquad\text{(11-41a)}$$
> $$R[m]+a_1R[m-1]+\cdots+a_NR[m-N]=0,\quad m>N\qquad\text{(11-41b)}.$$

**兩個用途**【口頭】：
1. **給定自相關，設計濾波器**：已知 $R[0],\dots,R[N]$（$N\times N$ 的矩陣有了），解出 $a_1,\dots,a_N$ 和 $b_0$，就能產生想要的 AR 過程。
2. **給定濾波器，求自相關**：已知 $a$、$b$，解 $R[0],\dots,R[N]$；$R[N+1],R[N+2],\dots$ 方程式沒有了，用 (11-41b) **遞迴** (recursive) 算下去（需要初值）。

【課本補充】p. 508：Yule–Walker 方程在 §12-3 用來由前 $N+1$ 個 $R[m]$ 決定 $N+1$ 個參數 $a_k$、$b_0$。

---

## 4. 例：AR(1)

[▶ 20:08](https://youtu.be/0NWCoO9FGSk?t=1208) 最簡單的 AR：
$$X[n]-aX[n-1]=b\,I[n],\qquad L(z)=\frac{b}{1-az^{-1}}.$$
（AR 不要求 $|a|<1$。）

**根最重要**：$1-az^{-1}=0$，根 $z_1=a$。$|a|<1$ 時在單位圓內，系統穩定，保證 WSS。

用上一集的公式：$\gamma_1=b$；$\alpha_1=\gamma_1L(1/z_1)$——根在單位圓內，就代單位圓外的對應點 $\frac1a$：
$$\alpha_1=b\cdot\frac{b}{1-a\cdot a}=\frac{b^2}{1-a^2},\qquad R[m]=\frac{b^2}{1-a^2}a^{|m|}.$$

老師說：那樣的拆解給很直觀的結果——給根、給係數，馬上知道時域自相關就是以**根的 $|m|$ 次方**衰減。

【課本補充】Example 11-7：課本寫 $X[n]-aX[n-1]=\nu[n]$、$R_{\nu\nu}[m]=b\,\delta[m]$（$b$ 是雜訊功率），所以 $R[0]-aR[1]=b$、$R[m]=\alpha a^{|m|}$、$\alpha=\frac{b}{1-a^2}$。和上面差在 $b$ 的意義（係數 vs. 功率）。

---

## 5. $|a|>1$：不穩定、非平穩

[▶ 22:43](https://youtu.be/0NWCoO9FGSk?t=1363) 有人真的在用不是 regular 的 AR 過程，所以討論 $|a|>1$。

- $\frac{1}{1-az^{-1}}=1+az^{-1}+a^2z^{-2}+\cdots$ 只在 $|az^{-1}|<1$ 時成立。$|a|>1$ 時**不收斂**：設計數位濾波器時模擬過，兩邊不相等、會亂跳、完全偏離想要的值。這時式子是 undefined／indeterminate。
- 所以 $|a|>1$ 時 AR 過程是**非平穩** (non-stationary) 的。

**和定理的衝突？** 通訊書上的性質：**穩定的 LTI 濾波器**，WSS 輸入保證 WSS 輸出。這裡輸入 WSS、輸出卻非平穩——問題在哪？濾波器還是線性、還是時不變；**唯一的問題是不穩定**，違反了定理的前提。

**直觀**（例 $a=2$）【口頭】：$X[t]-2X[t-1]=I[t]$，能量越來越大、會累積（像 $2^1,2^2,2^3,\dots$），不像一般 WSS 的自相關在原點最大、慢慢衰減，反而越來越大，最後會爆掉。所以一般用的時候希望 $|a|<1$。

---

## 6. 分子為 0：可預測過程與線譜

[▶ 28:22](https://youtu.be/0NWCoO9FGSk?t=1702) 之前討論 $M\le N$（包含等號，多一個根在 0）。還沒討論：$M>N$，和一個很特別的情況（課本放在後面，老師拿到前面講）：$M=0$ **而且 $b_0=0$**。

- 是 AR，但分子是 0。照理轉移函數整個是 0；但**不能把它視為 0**，它有分母——「分母分之 0」。
- 系統由 (11-40) 定義，右邊是 0：
$$X[n]+a_1X[n-1]+\cdots+a_NX[n-N]=0\qquad\text{(11-42)}.$$
  **沒有輸入**，完全在輸出端自我循環。

> **可預測過程** (predictable process)：給過去 $N$ 個值，下一個值百分之百確定。

例：一階 $X[t]+a_1X[t-1]=0$，給 $X[t-1]$，$X[t]$ 完全知道。二階：給 $X[t-1]=0.2$、$X[t-2]=0.1$，$X[t]=-(a_1\cdot0.2+a_2\cdot0.1)$。雖然整個是隨機的（三個都是隨機變數），但一定符合這個式子，所以百分之百可預測。

這就是上一集預告的**分解**（老師稱為 Wold decomposition）：任何 WSS 過程 = regular（不可預測）+ predictable（可預測，irregular）。

**線譜** (line spectrum) [▶ 32:04](https://youtu.be/0NWCoO9FGSk?t=1924)：可預測過程的功率頻譜**只有脈衝**（一根一根的線）：
$$S(\omega)=2\pi\sum_i\sigma_i^2\,\delta(\omega-\omega_i),\quad|\omega|<\pi.$$
（$2\pi$ 只是方便的係數。）

**為什麼**：解 (11-42) 得 $X[n]=\sum_ic_iz_i^n$，$D(z_i)=0$。
- 要**平穩**，$z_i$ 只能是 $e^{j\omega_i}$——**在單位圓上**（不在裡面、不在外面）。$\omega_i$ 就是那個角度（複數平面的旋轉角）。
- 係數 $c_i$ 要**零平均、互不相關**（第 15 集），$\sigma_i^2=E|c_i|^2$。
- 自相關 $R[m]=\sum_i\sigma_i^2e^{j\omega_i|m|}$（式 (11-44)），傅立葉轉換就是那些脈衝。

老師說：這和後面的 Fourier 級數投影、**Karhunen–Loève 展開**有關，那裡會看到它的影子。（有人不把它算 AR，認為 AR 應該 $b_0\ne0$；老師用自己的名詞叫它 **AR process with line spectrum**。）

**怎麼找分母係數** [▶ 35:07](https://youtu.be/0NWCoO9FGSk?t=2107)：$b_0=0$，原本的 Yule–Walker 不 work；直接用**根**解。設有 $N$ 根脈衝（$N$ 個頻率），$z_i=e^{j\omega_i}$：
$$\begin{pmatrix}1&z_1^{-1}&\cdots&z_1^{-N}\\1&z_2^{-1}&\cdots&z_2^{-N}\\\vdots&&&\vdots\\1&z_N^{-1}&\cdots&z_N^{-N}\end{pmatrix}\begin{pmatrix}1\\a_1\\\vdots\\a_N\end{pmatrix}=\mathbf{0}.$$

**驗證**：$X[t]=\sum_ic_ie^{j\omega_it}$，$X[t-k]=\sum_ic_ie^{j\omega_it}z_i^{-k}$（拆出 $e^{-j\omega_ik}=z_i^{-k}$）。所以
$$X[t]+\sum_ka_kX[t-k]=\sum_ic_ie^{j\omega_it}\underbrace{\left(1+\sum_ka_kz_i^{-k}\right)}_{=0}=0.$$
- 分母至少要 $N$ 階：$N$ 個脈衝就要 $N$ 個係數。
- 例：$N=2$：$1+a_1z_1^{-1}+a_2z_1^{-2}=0$、$1+a_1z_2^{-1}+a_2z_2^{-2}=0$，解出 $a_1,a_2$。
- **標準式**（不用解）：分母就是根的乘積
$$D(z)=\prod_{i=1}^{N}\left(1-z_iz^{-1}\right).$$
  四個頻率 → 四個根 → 四階多項式，完全串在一起。

**Poisson 求和公式的補充** [▶ 41:14](https://youtu.be/0NWCoO9FGSk?t=2474)：直接算功率頻譜時用到 Poisson 求和公式：$\sum_me^{j(\omega_i-\omega)m}=2\pi\sum_k\delta(\omega-\omega_i+2\pi k)$——頻譜上做旋轉一直連加，等於在頻譜上一串週期 $2\pi$ 的脈衝連加。老師說投影片寫得比較快，少了對 $k$ 的求和；只剩 $i=1..N$ 的一個求和，是因為離散時間只看 $(-\pi,\pi)$ 一個週期，加 $2\pi$ 的已經在外面了。

---

## 7. MA 過程

[▶ 43:21](https://youtu.be/0NWCoO9FGSk?t=2601)

> **MA 過程**（移動平均，moving average）：innovation filter 是多項式（**沒有分母**）：
> $$X[n]=b_0I[n]+b_1I[n-1]+\cdots+b_MI[n-M],\qquad L(z)=b_0+b_1z^{-1}+\cdots+b_Mz^{-M}\qquad\text{(11-45), (11-46)}.$$

- 沒有分母，就沒有分母的 pole → **一定穩定**，WSS 輸入保證 WSS 輸出。這是 MA 的優點之一。
- 輸出 = 過去和現在輸入的線性組合，係數 $b_0,\dots,b_M$。
- 名稱：一個大小 $M+1$ 的**視窗**，隨時間一直移動 (moving)，每到下個時間往左移一格，做**加權平均** (weighted average)，所以叫 moving average。
- **它就是卷積**：$\sum_kh[k]I[n-k]$，脈衝響應就是 $h[k]=b_k$——有限長度（FIR filter）。所以脈衝響應一定存在、一定穩定。
- **缺點／特性**：只侷限在視窗裡，很久以前的輸入對現在完全沒影響——**記憶長度有限** (finite memory order)。是優點還是缺點，看應用：如果希望排除很久以前的東西，就選 MA model。

在 $M>N$ 的討論裡，MA 是 $N=0$ 的特例，也沒完全涵蓋 $M>N$ 的所有情況。

**自相關**：輸出的自相關 = 輸入的自相關經過濾波器兩次（一次共軛、一次本身，所以是「加」的卷積）；輸入是白的（delta）：
$$R[m]=\sum_kb_{k+m}b_k^*.$$
（$R[m]=0$，$|m|>M$。）功率頻譜就是 $|L(e^{j\omega})|^2$。

---

## 8. ARMA 過程

[▶ 49:35](https://youtu.be/0NWCoO9FGSk?t=2975)

> **ARMA**：MA（分子 $N(z)$）和 AR（分母 $\frac1{D(z)}$）**串接**：
> $$L(z)=\frac{N(z)}{D(z)}.$$

- 串接兩個濾波器，頻譜上直接相乘，**順序不重要**。
- 就是上一集的一般有理形式，所以分析已經做過了。
- 可以衡量怎麼調配兩者，組合 AR 和 MA 的優點。很常用。

老師說：這樣就介紹了三種很重要的隨機過程。

---

## 9. 一頁速查表

### 三種過程

| | 濾波器 | 時域 | 特性 |
|---|---|---|---|
| AR | $\frac{b_0}{1+a_1z^{-1}+\cdots+a_Nz^{-N}}$ | $X[n]+\sum a_kX[n-k]=b_0I[n]$ | 回饋、影響無限延續；根不一定在單位圓內 |
| MA | $b_0+b_1z^{-1}+\cdots+b_Mz^{-M}$ | $X[n]=\sum b_kI[n-k]$ | FIR、一定穩定、記憶有限 |
| ARMA | $\frac{N(z)}{D(z)}$ | 兩者串接 | 一般有理形式 |

### Yule–Walker（AR）

$$R[m]+a_1R[m-1]+\cdots+a_NR[m-N]=\begin{cases}b_0^2,&m=0\\0,&m\ge1\end{cases}$$
- 關鍵：$X[t-m]$ 是過去輸入的線性組合，和 $I[t]$ 不相關（不相關變數的線性組合仍不相關）。

### AR(1)

$X[n]-aX[n-1]=bI[n]$：$R[m]=\frac{b^2}{1-a^2}a^{|m|}$（$|a|<1$）；$|a|>1$ 不穩定、非平穩、能量爆掉。

### 可預測過程（線譜）

- $X[n]+\sum a_kX[n-k]=0$（$b_0=0$），給過去 $N$ 個值完全決定下一個。
- 根在**單位圓上** $z_i=e^{j\omega_i}$；$X[n]=\sum c_ie^{j\omega_in}$，$c_i$ 零平均不相關。
- $S=2\pi\sum\sigma_i^2\delta(\omega-\omega_i)$，$R[m]=\sum\sigma_i^2e^{j\omega_i|m|}$，$D(z)=\prod(1-e^{j\omega_i}z^{-1})$。

### MA

$R[m]=\sum_kb_{k+m}b_k^*$，$|m|>M$ 時為 0。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 線譜、$\sum c_ie^{j\omega_in}$ | 下一集：§11-3 Fourier 級數與 Karhunen–Loève 展開 |
| 可預測 + regular 分解 | §11-4 頻譜表示（第 28–29 集） |
| Yule–Walker | §12-2、12-3 參數化頻譜估計；§13-2 預測、Levinson 演算法 |
| AR／MA 模型 | 資料分析、頻譜估計 |

---

## 附：本集一句話總結

> **AR 過程靠輸出回饋讓過去所有輸入的影響慢慢衰減延續，它的自相關滿足 Yule–Walker 方程（$|a|<1$ 才穩定，AR(1) 的 $R[m]=\frac{b^2}{1-a^2}a^{|m|}$）；分子為 0 的 AR 是可預測過程，根在單位圓上、頻譜是一根根的線；MA 是有限長度的卷積、一定穩定但記憶有限；ARMA 是兩者串接。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-2 (3/3) 錄影逐字稿（whisper large-v3-turbo，51:03）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
