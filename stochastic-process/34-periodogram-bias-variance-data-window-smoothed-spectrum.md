---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 34
lecture: Lec 12-2 Spectrum Estimation — Spectrum Estimation (1/3)
date: 待補
video: https://youtu.be/tUYxbzvys2g
notes: Papoulis & Pillai 4th ed. §12-2（式 (12-36)–(12-53)、Theorem 12-3、12-4、Data window、Smoothed Spectrum，pp. 537–541）
---

# 第 34 集 · Lec 12-2 (1/3)：periodogram、漸近不偏、Theorem 12-4 變異數 ≈ $S^2(\omega)$、高斯假設的驗證、estimation variance vs variance of the estimate、data window 與 smoothed spectrum [▶ 影片](https://youtu.be/tUYxbzvys2g)

← 上一集：[33](33-variance-covariance-distribution-ergodic-correlometer-spectrometer.md) ｜ [總目錄](README.md) ｜ 下一集：[35](35-smoothed-spectrum-variance-window-tradeoff-bartlett-tukey-papoulis.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 34 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（57:01，whisper large-v3-turbo）＋ Papoulis §12-2（pp. 537–541）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「periodogram」→「periodogram／periodigran」，「truncation」→「tuncation／Trancation」，「asymptotically unbiased」→「Asymptotically Unbiased」，「wide-sense stationary」→「Wisen Stationary／YC station」，「autocorrelation」→「autoclin／autocomming／autochrome／autoculting」，「sinc」→「Sync／sink／性函數」，「approximation」→「approsimation／apprasimation／Atlasmation」，「Dirac delta」→「direct delta」，「Proakis」→「Proxy's」，「rule of thumb」→「rule of thumb／Rue of Thumb」，「Papoulis」→「Propolis／popality」，「data window」→「Data window」，「weighting」→「waiting」，「modified periodogram」→「Modified Periodogram」，「bias」→「BIOS」，「variance of the estimate」→「variance of the estimation／Variance of the Estimate」，「smoothed spectrum」→「Smooth Spectrum」，「lag window」→「Leg window」，「spectral window」→「spectral window」，「real」→「時數」，「魚與熊掌不可兼得」→「鱼与熊掌不可得奸」。以下一律用正確的字。

> **接上一集**：上一集最後講到真的要量功率頻譜（頻譜計）。這集正式進入**頻譜估計**：只有有限長度的資料時，估出來準不準？

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 問題：只能量一個 window](#1-問題只能量一個-window)
- [2. Periodogram](#2-periodogram)
- [3. Theorem 12-4 的結論與直觀](#3-theorem-12-4-的結論與直觀)
- [4. 證明一：漸近不偏](#4-證明一漸近不偏)
  - [4.1 截斷後的二維頻譜是實數](#41-截斷後的二維頻譜是實數)
  - [4.2 sinc 截斷近似](#42-sinc-截斷近似)
  - [4.3 sinc² 當 delta](#43-sinc²-當-delta)
- [5. 證明二：變異數](#5-證明二變異數)
- [6. 補充：高斯時假設成立](#6-補充高斯時假設成立)
- [7. Estimation variance vs variance of the estimate](#7-estimation-variance-vs-variance-of-the-estimate)
- [8. Data window：調 bias](#8-data-window調-bias)
- [9. Smoothed spectrum：調 variance](#9-smoothed-spectrum調-variance)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| Periodogram、Theorem 12-4 結論 | [▶ 00:00](https://youtu.be/tUYxbzvys2g?t=0) | 式 (12-36)–(12-39)、(12-46) |
| 漸近不偏的證明 | [▶ 09:43](https://youtu.be/tUYxbzvys2g?t=583) | 式 (12-42)、(12-43)，p. 539 |
| 變異數 | [▶ 28:44](https://youtu.be/tUYxbzvys2g?t=1724) | Theorem 12-4，p. 540 |
| Data window | [▶ 31:17](https://youtu.be/tUYxbzvys2g?t=1877) | 式 (12-44)、(12-45)，p. 540 |
| 高斯假設 | [▶ 35:21](https://youtu.be/tUYxbzvys2g?t=2121) | 式 (11-74) |
| Estimation variance | [▶ 41:32](https://youtu.be/tUYxbzvys2g?t=2492) | 無（【口頭】） |
| Smoothed spectrum | [▶ 48:11](https://youtu.be/tUYxbzvys2g?t=2891) | 式 (12-51)，p. 541 |

---

## 1. 問題：只能量一個 window

[▶ 00:00](https://youtu.be/tUYxbzvys2g?t=0) 老師大四時，對面實驗室有很貴的 HP 頻譜分析裝置，可以掃描頻譜畫出來（老師做影像處理，不需要）。頻譜估計確實有裝置在做，而且非常貴。【口頭】

- 不可能量 $-\infty$ 到 $\infty$，一定量一個 window。上一集討論 $T\to\infty$ 量得準不準；現在 **$T$ 不能趨近無限大**——即使大數據也是有限個值。
- 例：給你一年、二十年的數值，請你告訴我地球有沒有暖化（雖然地球已經幾十億歲了）。
- 截斷後的資料：
$$X_T(t)=X(t)p_T(t),\qquad p_T(t)=\begin{cases}1,&|t|<T\\0,&|t|>T\end{cases}\qquad\text{(12-36)}.$$
- 回到根本：設計了 HP 這麼貴的裝置，量出來不準，理論上有什麼誤差？

假設 $X$ 是實數（複數也都對）、WSS。

---

## 2. Periodogram

[▶ 02:02](https://youtu.be/tUYxbzvys2g?t=122) **名字**【口頭】：period 是一個時期——講一句話加個句點 (period) 就結束了。所以 periodogram 的意思是「量到一個時間就結束了，只有這麼多數值」。

> **Periodogram**：
> $$S_T(\omega)=\frac1{2T}\left|\int_{-T}^{T}X(t)e^{-j\omega t}dt\right|^2=\frac1{2T}|X_T(\omega)|^2\qquad\text{(12-39)}.$$
> 量一段時間（$-T$ 到 $T$，把 0 放中間比較平衡），做傅立葉轉換（例如光學傅立葉轉換裝置），取絕對值平方，除以 $2T$。

- 它是**隨機變數**：每次量都不一樣（可能要量十次、一百次、一萬次來平均）。
- 為什麼取絕對值平方：WSS 的功率頻譜一定是**實數、非負**（證過），功率不會是負的。量出來若有正有負就很怪。periodogram 也是實數、非負——和功率完全一致。老師說數位通訊課有用數學證明它和功率頻譜有關。

⚠️ 逐字稿缺字：老師說投影片打錯，應是粗體 $\mathbf x$（隨機過程），不是 $x_b$。

【課本補充】pp. 538–539：估計 $R(\tau)$ 用
$$R_T(\tau)=\frac1{2T}\int_{-T+|\tau|/2}^{T-|\tau|/2}X\left(t+\frac\tau2\right)X\left(t-\frac\tau2\right)dt\qquad\text{(12-38)}$$
（有偏、但變異數比不偏版本小）。**Theorem 12-3**：$S_T(\omega)=\int_{-2T}^{2T}R_T(\tau)e^{-j\omega\tau}d\tau$（式 (12-40)；因為 $R_T=\frac1{2T}X_T(\tau)*X_T(-\tau)$）。早年用類比技術時 periodogram 結果可靠；數位處理精度提高後，算出的頻譜反而很雜亂——因為 (12-40) 用到所有 $|\tau|$ 到 $2T$ 的 $R_T$，大 $\tau$ 時 $R_T$ 變異數大，$S_T(\omega)$ 趨近平均 $S(\omega)$ 的白雜訊過程。

---

## 3. Theorem 12-4 的結論與直觀

[▶ 05:04](https://youtu.be/tUYxbzvys2g?t=304) 令 $Y=X_T$（換個記號），$S_T=\frac{|Y|^2}{2T}$。

> **(1) 漸近不偏** (asymptotically unbiased)：
> $$E\{S_T(\omega)\}\xrightarrow[T\to\infty]{}S(\omega).$$
> **(2) Theorem 12-4（頻譜變異數）**：$T$ 大時
> $$\mathrm{Var}\,S_T(\omega)\approx\begin{cases}2S^2(0),&\omega=0\\S^2(\omega),&|\omega|\gg\frac1T\end{cases}\qquad\text{(12-46)}.$$
> 條件（假設）：$\mathrm{Cov}\{|Y(u)|^2,|Y(v)|^2\}=S_{YY}^2(u,v)+S_{YY}^2(u,-v)$（$S_{YY}$ 是 $Y$ 的二維頻譜）。

**直觀**【口頭】[▶ 06:35](https://youtu.be/tUYxbzvys2g?t=395)：
- 變異數 = 每次量會跑掉的範圍；越小越準。
- 例：監控北韓發射飛彈的訊號，一點一點量功率頻譜畫圖。**每一點量錯的變異數不一樣大**，剛好是那點功率頻譜的**平方**：值 0.1 → 變異數 0.01；值 8 → 64；值 20 → 400。
- **要量的東西值越大，越不容易量準**；值小量得比較準。符合一般的經驗（rule of thumb）。
- 前提 $|\omega|\gg\frac1T$；$T$ 通常很大，所以一般都 OK。$\omega=0$ 時多乘兩倍。
- 條件很強：**高斯**時百分之百成立，其他過程通常不成立；但一般說量的對象大部分有高斯行為，所以這個直覺是對的。

老師說：不是只把敘述念完、看證明看完就結束。這個證明很 tricky（因為是近似），要理解 Papoulis 為什麼覺得它重要——它隱含給你的直覺。

---

## 4. 證明一：漸近不偏

> ⚠️ 老師的證明和課本不同：課本 p. 539 直接用 $E\{S_T\}=\int(1-\frac{|\tau|}{2T})R(\tau)e^{-j\omega\tau}d\tau$ 和三角波 ↔ $\mathrm{sinc}^2$ 得 (12-42)；老師用二維傅立葉轉換和 sinc 截斷近似（以下）。

**Step 0** [▶ 09:43](https://youtu.be/tUYxbzvys2g?t=583)：截斷 = 輸入經過 window，輸出自相關 = 輸入自相關乘兩次截斷 window：
$$R_{YY}(t_1,t_2)=R(t_1-t_2)\,p_T(t_1)\,p_T(t_2).$$

**Step 1：二維傅立葉轉換**（不知道是不是只跟某個參數有關，所以做最廣義的）：
$$S_{YY}(u_1,u_2)=\iint R(t_1-t_2)p_T(t_1)p_T(t_2)e^{-j(u_1t_1+u_2t_2)}dt_1dt_2.$$
**Step 2**：要看頻譜，把 $R$ 寫成 $S$ 的反轉換。
**Step 3**：**積分順序對調**——先對 $dt_1,dt_2$ 積，再對 $df$ 積。方波 $p_T$ 的傅立葉轉換是 sinc：
$$S_{YY}(u_1,u_2)=\frac1{2\pi}\int S(f)\frac{2\sin T(u_1-f)}{u_1-f}\cdot\frac{2\sin T(u_2+f)}{u_2+f}\,df.$$

**「定理一」**【口頭】：所有隨機過程的證明都一定有一個步驟叫積分對調——好像沒有例外。老師講了 MIT 一個演講者的笑話：他畫了 source encoder → channel encoder → channel → channel decoder → source decoder，說「定理：所有通訊課本的圖一都是這個圖。證明：全對。」大家鼓掌，他叫它 figure-one theorem。

### 4.1 截斷後的二維頻譜是實數

[▶ 13:20](https://youtu.be/tUYxbzvys2g?t=800) 紅字重點：
- 一般過程（不一定 WSS）只能做 $R(t_1,t_2)$ 的二維轉換——**不保證是實數**，沒有任何特殊性質。
- 但輸入是 **WSS** 時，上式裡 $\frac1{2\pi}$、兩個 sinc、$S(f)$ 都是實數 ⇒ $S_{YY}(u_1,u_2)$ **一定是純實數**（不管用什麼 window）。後面會用到。
- 名詞：二維的不叫 power spectrum（不帶功率意味），應該叫二維的廣義傅立葉轉換。

### 4.2 sinc 截斷近似

[▶ 16:25](https://youtu.be/tUYxbzvys2g?t=985) 很 tricky 的地方：sinc 越來越小（高度衰減），在特殊點是 0。把外面直接當 0：正、負各只取 $k$ 個波折（$k$ 很大，外面都很小，積分好像沒什麼損失）。轉成 $f$ 的條件：兩個 window（指示函數）
- 藍色：$u_1-\frac{k\pi}{T}<f<u_1+\frac{k\pi}{T}$；
- 紅色：$-u_2-\frac{k\pi}{T}<f<-u_2+\frac{k\pi}{T}$。

**兩個 window 完全沒重疊**（例如一個積 3 到 6、一個積 20 到 29），相乘永遠是 0，積分就是 0。條件（藍的最大值 ≤ 紅的最小值，或反過來）整理成
$$u_1+u_2\le-\frac{2\pi k}{T}\quad\text{或}\quad u_1+u_2\ge\frac{2\pi k}{T}.$$
$k$ 很大 ⇒ **$|u_1+u_2|\gg\frac1T$ 時 $S_{YY}(u_1,u_2)\approx0$**。

老師說：這只是定性說法，沒告訴我差多少；科學講的是量化 (quantitative)，他比較希望講清楚一點。

### 4.3 sinc² 當 delta

[▶ 22:38](https://youtu.be/tUYxbzvys2g?t=1358) 代 $u_1=\omega$、$u_2=-\omega$：兩個 sinc 完全一樣，變成平方（這是**等號**，不是近似）：
$$S_{YY}(\omega,-\omega)=2T\int S(f)\frac{\sin^2T(\omega-f)}{\pi T(\omega-f)^2}\,df.$$
- $\mathrm{sinc}^2$ 總積分是 1（Proakis 的數位通訊課本用很多次）。
- $T\to\infty$ 時在 0 衝到無限大、其他點都趨近 0、總面積永遠是 1 ⇒ **當作 delta**。

**綠框：為什麼可以當 delta**：任何函數 $f_n(t)$ 總積分 1、$n\to\infty$ 時在原點衝到無限大、其他地方都是 0，就用 delta 取代（有人用三角波、有人用方波，都對）。不是只有 sinc² 可以用。這又是一個近似，準不準也沒講。

**用第 11 章的結果**：$E\{S_T(\omega)\}=\frac1{2T}E\{|Y(\omega)|^2\}=\frac1{2T}S_{YY}(\omega,-\omega)$——第 11 章（第 28 集）：一個 domain 的自相關是另一個 domain 的功率頻譜（差一個負號，$\omega$ 和 $-\omega$）。那時要講的重點是「WSS 在另一個 domain 是白的」，現在順道用。$2T$ 對消：
$$E\{S_T(\omega)\}\approx S(\omega),\quad T\to\infty.$$ ∎

用了很不精準的證明（$k$ 和 delta），有點 technical，但數學上算 OK。

【課本補充】p. 539：精確式 $E\{S_T(\omega)\}=\int\frac{\sin^2T(\omega-y)}{\pi T(\omega-y)^2}S(y)dy$（式 (12-42)）——periodogram 的平均是 $S(\omega)$ 的**平滑版本**；平滑核只在寬度約 $\frac1T$ 的區間有值，所以 $S$ 連續處 $T$ 大時 $\approx S(\omega)$（式 (12-43)）。

---

## 5. 證明二：變異數

[▶ 28:44](https://youtu.be/tUYxbzvys2g?t=1724) 用**假設**（不用證明）：
$$\mathrm{Cov}\{|Y(u)|^2,|Y(v)|^2\}=S_{YY}^2(u,v)+S_{YY}^2(u,-v).$$
代 $u=v=\omega$：
$$\mathrm{Var}\,S_T(\omega)=\frac1{4T^2}\left[S_{YY}^2(\omega,\omega)+S_{YY}^2(\omega,-\omega)\right].$$
- $|\omega|\gg\frac1T$：$S_{YY}(\omega,\omega)$ 的 $u_1+u_2=2\omega\gg\frac1T$，由 §4.2 是 0；$S_{YY}(\omega,-\omega)\approx2TS(\omega)$ ⇒ $\mathrm{Var}\approx S^2(\omega)$。
- $\omega=0$：兩項一樣 ⇒ $2S^2(0)$。∎

**隱含意義**：估計的變異數 = 要估的值的平方。要估的值越大，越不容易估準，很吻合實際量測的現象。

**Comment** [▶ 31:17](https://youtu.be/tUYxbzvys2g?t=1877)：$S_T$ 漸近不偏，但實際上 $T$ 是固定的（量一天、一週、一年），**bias 還是有**。接下來要講有限 $T$ 下怎麼調整 bias。

【課本補充】p. 540 Note：對特定 $\tau$，$R_T(\tau)\to R(\tau)$；但 $S_T(\omega)$ 不趨近 $S(\omega)$，因為 $R_T\to R$ 對 $\tau$ 不是均勻收斂。p. 541 Note：若有 $N$ 個獨立樣本（或把一個長樣本切成 $N$ 段近乎獨立的），各自算 periodogram 再平均：$\mathrm{Var}\,\bar S_T\approx\frac1NS^2(\omega)$（式 (12-50)），$N$ 大時變異數小，但 bias 可能明顯。

---

## 6. 補充：高斯時假設成立

[▶ 35:21](https://youtu.be/tUYxbzvys2g?t=2121) 定理講完要討論：定理裡的假設合不合理、能不能成立？Theorem 12-4 的強假設，**高斯時成立**。（⚠️ 逐字稿缺字：老師這裡口誤說「定理 11-3」，指的是 Theorem 12-4。）

**證明**（用高斯降階：兩兩配對，所有組合湊出來）：傅立葉轉換有實部虛部，$Y(u)=A_u+jB_u$、$Y(v)=A_v+jB_v$，都是高斯。
- $|Y(u)|^2=A_u^2+B_u^2$；$|Y(u)|^2|Y(v)|^2$ 乘出來四項，期望值的乘積也四項。
- 例：$E\{A_u^2A_v^2\}$ 是四個高斯相乘，配對有三種（1 配 2、1 配 3、1 配 4），降階：$E\{A_u^2\}E\{A_v^2\}+2E^2\{A_uA_v\}$。
- 令 $c=E\{A_uA_v\}$、$d=E\{B_uB_v\}$、$e=E\{A_uB_v\}$、$f=E\{B_uA_v\}$，整理得 $\mathrm{Cov}=2(c^2+d^2+e^2+f^2)$。

**用第 11 章**：
$$S_{YY}(u,-v)=E\{Y(u)Y^*(v)\}=(c+d)+j(f-e),\qquad S_{YY}(u,v)=E\{Y(u)Y(v)\}=(c-d)+j(e+f).$$
**關鍵**：§4.1 證過 WSS 時 $S_{YY}(u_1,u_2)$ **一定是純實數**，所以虛部是 0：$e=f=0$。兩式相加 $2c$、相減 $2d$，平方和的關係剛好給出
$$S_{YY}^2(u,v)+S_{YY}^2(u,-v)=2(c^2+d^2)=\mathrm{Cov}\{|Y(u)|^2,|Y(v)|^2\}.$$ ∎

所以假設沒那麼不合理；要違反它，要造一個分布很不像高斯的過程。複數時證出來的結果略有不同。（課本對應式 (11-74)。）

老師說：這些東西寫下來不容易，課本很多沒寫，他用口頭讓大家更深入了解；做研究也一樣——要有根本、要有討論、要有假設、每個假設也要討論。

---

## 7. Estimation variance vs variance of the estimate

[▶ 41:32](https://youtu.be/tUYxbzvys2g?t=2492) 課本有兩個不同的名詞，講的不一樣的事情。令估計量 (estimate) $\hat\theta$（例如 $S_T(\omega)$），真值 $\theta$（真正的 $S(\omega)$）：

| 名詞 | 定義 | 意思 |
|---|---|---|
| variance of the estimate | $\mathrm{Var}\,\hat\theta=E(\hat\theta-E\hat\theta)^2$ | 估計量本身直接取變異數（離量測平均的距離） |
| estimation variance | $E(\hat\theta-\theta)^2$ | 估計誤差的變異數（離真值的距離） |

**誰大**：展開
$$E(\hat\theta-\theta)^2=\mathrm{Var}\,\hat\theta+\left(E\hat\theta-\theta\right)^2\ \ge\ \mathrm{Var}\,\hat\theta.$$
（第一項展開四項，第二項是兩項相減，對消後剛好湊出一個平方項。）**estimation variance 一定 ≥ variance of the estimate**——這是證明，不是「通常」。例：真平均 0，量 $0.1,-0.1,0.9,0.9$，量測平均 0.45。

**讀論文要小心**【口頭】：有些論文給很小的變異數，其實給的是 variance of the estimate。要正確詮釋人家呈現的是哪一個。

**下界**（老師沒給證明）[▶ 45:05](https://youtu.be/tUYxbzvys2g?t=2705)：由 Theorem 12-4，variance of the estimate $\approx S^2$，所以 estimation variance $\gtrsim S^2$——**通常不可能變成 0**，大約是要量的值的平方，不會比它好。除非東西一點都不隨機，總是會有誤差。

---

## 8. Data window：調 bias

[▶ 31:47](https://youtu.be/tUYxbzvys2g?t=1907) 調 bias 的方法：加 window。兩種加法：

- **data window**：加在**時域**。好記：量到的資料 (data) 都是時域的；頻譜（傅立葉轉換）是我們的想像。
- **spectral window**：加在頻域（§9）。

> **Modified periodogram**：
> $$S_c(\omega)=\frac1{2T}\left|\int_{-T}^{T}c(t)X(t)e^{-j\omega t}dt\right|^2\qquad\text{(12-44)}.$$
> $c(t)$ 是 data window（加 weighting：信任的地方權重大，不信任的小）。記號上用分號 $S_T(\omega;c)$：$\omega$ 是真正要對準的參數點，$c$ 是一個 functional，不對等。

- 類比第 21 集：要偵測的對象是多項式，最好的濾波器也是對應的多項式。這裡也是加 weighting——要量準的點附近設大、外面設小，很直觀。通常 bias 會小很多。
- 推導和前面一模一樣（積分對調，把 $p_T$ 換成 $c$）：
$$E\{S_c(\omega)\}=\frac1{4\pi T}S(\omega)*C^2(\omega)\qquad\text{(12-45)}.$$
- 第 21 集（第 11 章的平滑濾波器）假設多項式，可以用配方法；這裡比較難，要用一個非常有名的定理（後面講），學了一定有用。

**提醒** [▶ 47:09](https://youtu.be/tUYxbzvys2g?t=2829)：data window **通常對降低變異數幫助不大**（rule of thumb）。對 bias 有幫助很直觀（把 $0.1,-0.1,0.9,0.9$ 的權重調一調，有機會降低 bias），對變異數不那麼直觀。

【課本補充】p. 541：用 data window 得到的頻譜變異數基本上和 $S_T(\omega)$ 一樣——data window 不能降低估計的變異數；要改善，必須把 $R_T(\tau)$ 換成 $w(\tau)R_T(\tau)$，或平滑 periodogram。

---

## 9. Smoothed spectrum：調 variance

[▶ 48:41](https://youtu.be/tUYxbzvys2g?t=2921) **直接在頻域調頻譜形狀**，對調整變異數比較有效（rule of thumb）。時域叫 moving average，頻域叫 smooth。

> **Smoothed spectrum**：
> $$S_w(\omega)=\frac1{2\pi}\int S_T(\omega-y)W(y)\,dy=\int_{-2T}^{2T}w(\tau)R_T(\tau)e^{-j\omega\tau}d\tau\qquad\text{(12-51)}.$$
> periodogram（或 modified periodogram）和 $W$ 做**卷積**。
> - $W(\omega)$：**spectral window**（調 variance）。
> - $w(\tau)$：**lag window**。

**bias 和 variance 很難同時改善**（at the price of slightly larger bias）：variance 調好了 bias 就提高，反之亦然——魚與熊掌不可兼得，只能取捨。所以一般兩個都用，適度調整（後面會講最好的在哪裡）。

**lag window 和 data window 不一樣** [▶ 50:43](https://youtu.be/tUYxbzvys2g?t=3043)：頻域卷積 ⇒ 時域相乘，但**不是乘在原來的資料上**：
- 資料 $0.2,0.3,0.9,0.8$（例如空氣流速）→ data window 直接作用在資料上（乘 1、1、0.5、0.5）。
- 把 4 點資料做 4 點傅立葉轉換，得到量測資料的頻譜（例如 $2.0,4.8,3.3,3.3$）→ $W$ 對**頻譜的量測資料**做 smoothing（卷積）。
- 時域對應的是乘在 **$\tau$** 上——自相關的 $\tau$（前後相距的時間差）。**lag = delay**：今天的事件延遲到明天還在發酵的效果。所以 $w(\tau)$ 叫 lag window。$S_T$ 的反轉換是 $R_T(\tau)$，乘在 lag 上，不是乘在絕對時間 $t$ 上。

| window | 作用在 | 主要調 |
|---|---|---|
| data window $c(t)$ | 時域資料 | bias |
| spectral window $W(\omega)$ / lag window $w(\tau)$ | 頻域卷積 / 自相關的 lag | variance |

**兩個都用** [▶ 55:19](https://youtu.be/tUYxbzvys2g?t=3319)：data window 的效果是頻譜和 $C^2$（data window 傅立葉轉換的平方）卷積；再跟 spectral window 卷積一次：
$$E\{S_w(\omega;c)\}\approx\frac{1}{2\pi}\cdot\frac{1}{4\pi T}S(\omega)*C^2(\omega)*W(\omega).$$
同學會問：做一個不就結果一樣？後面會看到有點不一樣——data window 有絕對值平方進來，spectral window 只有一次；操作的位置不同，跟實作（放在哪裡比較容易做）有關。

---

## 10. 一頁速查表

| 項目 | 公式 |
|---|---|
| Periodogram | $S_T(\omega)=\frac1{2T}\lvert X_T(\omega)\rvert^2$ |
| 平均（精確） | $E S_T=\int\frac{\sin^2T(\omega-y)}{\pi T(\omega-y)^2}S(y)dy\to S(\omega)$ |
| 變異數 | $\approx S^2(\omega)$（$\lvert\omega\rvert\gg1/T$），$2S^2(0)$（$\omega=0$） |
| 假設（高斯成立） | $\mathrm{Cov}\{\lvert Y(u)\rvert^2,\lvert Y(v)\rvert^2\}=S_{YY}^2(u,v)+S_{YY}^2(u,-v)$ |
| Modified periodogram | $S_c=\frac1{2T}\lvert\int cXe^{-j\omega t}\rvert^2$，$E S_c=\frac1{4\pi T}S*C^2$ |
| Smoothed | $S_w=\frac1{2\pi}S_T*W=\int wR_Te^{-j\omega\tau}d\tau$ |
| 兩種變異 | $E(\hat\theta-\theta)^2=\mathrm{Var}\hat\theta+\text{bias}^2\ge\mathrm{Var}\hat\theta$ |

**關鍵步驟**：
- 二維轉換 → 積分對調 → 兩個 sinc；WSS ⇒ $S_{YY}(u_1,u_2)$ 實數。
- sinc 只取 $k$ 個波折 ⇒ $\lvert u_1+u_2\rvert\gg\frac1T$ 時 $S_{YY}\approx0$。
- $u_1=\omega,u_2=-\omega$ ⇒ sinc²，總面積 1 ⇒ delta。
- 高斯驗證：配對降階 + $S_{YY}$ 實數 ⇒ $e=f=0$。
- 直覺：值越大越難量準（變異數 ∝ 值²）；data window 調 bias、spectral/lag window 調 variance，兩者取捨。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Smoothed spectrum 的 bias、variance | 下一集：Theorem 12-5、window 的選擇 |
| 「非常有名的定理」（最佳 window） | 第 35–36 集 |
| 頻譜估計 | 第 13 章 MS 估計 |

---

## 附：本集一句話總結

> **只量有限長度時，periodogram $\frac1{2T}|X_T(\omega)|^2$ 漸近不偏（平均是 $S$ 被 sinc² 平滑的版本），但變異數約等於 $S^2(\omega)$——值越大越難量準（高斯時假設完全成立）；estimation variance 一定不小於 variance of the estimate；時域的 data window 主要調 bias、頻域的 spectral window（時域上是作用在 lag 上的 lag window）主要調 variance，兩者只能取捨。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 12-2 (1/3) 錄影逐字稿（whisper large-v3-turbo，57:01）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
