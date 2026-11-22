---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 39
lecture: Lec 13-2 Mean Square Estimation — Prediction (1/2)
date: 待補
video: https://youtu.be/0gioCnJF6iE
notes: Papoulis & Pillai 4th ed. §13-2 Prediction（Infinite Past 式 (13-19)–(13-26)、Theorem 13-2、Regular Processes 式 (13-27)–(13-35)、r-step predictor 式 (13-36)–(13-38)、Analog Processes 式 (13-39)–(13-47)，pp. 587–594）
---

# 第 39 集 · Lec 13-2 (1/2)：用整個過去預測、Wiener–Hopf 方程、誤差濾波器與誤差是白的、Theorem 13-2（零點在單位圓內）、regular 過程的預測、Kolmogorov–Szegő 公式、WS Markov of order $N$、$r$ 步預測、類比預測、為什麼不能用傅立葉轉換解 Wiener–Hopf [▶ 影片](https://youtu.be/0gioCnJF6iE)

← 上一集：[38](38-multiple-data-derivative-prediction-interpolation-noncausal-wiener-filter.md) ｜ [總目錄](README.md) ｜ 下一集：[40](40-predictable-process-fir-predictor-lattice-levinson.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 39 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:03:21，whisper large-v3-turbo）＋ Papoulis §13-2（pp. 587–594）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「r-step away」→「R Step Away」，「orthogonality principle」→「autogonality principle／Orthogonal Principle」，「Wiener–Hopf equation」→「Weiner-Hoff Equation／Winert equation／Winor-Holt」，「z-transform」→「G存form／寄存缝／计存form」，「error filter」→「Aerror filter／Area Process」，「Wold decomposition」→「Vault Decomposition／Vold decomposition」，「Gram–Schmidt procedure」→「Gran Smith Procedure」，「線性代數」→「线性怠数」，「i.i.d.」→「ID」，「單位圓」→「單位元／單位員」，「zero」→「Zero」，「proof by contradiction」→「Prove by Contradiction」，「regular」→「regular」，「rational spectrum」→「Rational Spectrum」，「Kolmogorov–Szegő」→「Komogorov 跟 Zegel／Comargrove-Zegel」，「wide-sense Markov」→「Wiseins Markov／Widesense Markov」，「AR process」→「AR process／ARプロジェクト」，「Poisson」→「Prozoned」，「正交」→「證交」，「white」→「坏／白色」，「complex conjugate」→「complete conjugate」，「dummy variable」→「Dummy Variable」。以下一律用正確的字。

> **本集定位**：另一個角度——**預測**。各種壓縮技術（影像傳輸）都有預測：如果能準確預測未來的影像就不用送了，接收端做同樣的預測就能把影像還原得很好。這裡直接講離散（前面講的是連續）。

---

## 目錄

- [0. 三種預測](#0-三種預測)
- [1. 用整個過去預測：Wiener–Hopf](#1-用整個過去預測wienerhopf)
- [2. 誤差濾波器與誤差是白的](#2-誤差濾波器與誤差是白的)
- [3. Theorem 13-2：誤差濾波器的零點在單位圓內](#3-theorem-13-2誤差濾波器的零點在單位圓內)
- [4. 為什麼不能直接用 z 轉換解](#4-為什麼不能直接用-z-轉換解)
- [5. Regular 過程的預測](#5-regular-過程的預測)
  - [5.1 用 innovations 預測](#51-用-innovations-預測)
  - [5.2 預測濾波器 $H=1-\frac{l[0]}{L}$](#52-預測濾波器-h1-fracl0l)
  - [5.3 例 13-3：有理頻譜](#53-例-13-3有理頻譜)
- [6. Kolmogorov–Szegő 公式](#6-kolmogorovszegő-公式)
- [7. Wide-sense Markov of order $N$](#7-wide-sense-markov-of-order-n)
- [8. $r$ 步預測](#8-r-步預測)
- [9. 類比預測](#9-類比預測)
- [10. 用 $e^{j\omega t}$ 的觀點看：為什麼傅立葉轉換不能解 Wiener–Hopf](#10-用-ejomega-t-的觀點看為什麼傅立葉轉換不能解-wienerhopf)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 三種預測

[▶ 00:31](https://youtu.be/0gioCnJF6iE?t=31)
- **entire past**：用所有的過去預測下一個時間點。
- **r-step away**：用 $r$ 個時間以前的資料預測現在（最近進來的資料可能還沒整理好、不能用）。
- **finite past**：用過去 $N$ 個點預測。

感覺上都一樣（計算都一樣），但到數位端做法會不同。

---

## 1. 用整個過去預測：Wiener–Hopf

[▶ 01:01](https://youtu.be/0gioCnJF6iE?t=61)
$$\hat S[n]=\sum_{k=1}^{\infty}h[k]S[n-k]\qquad\text{(13-19)}.$$
係數一般有兩個參數（要預測的時間 $n$、weighting 的 $k$）。**正交原理**：誤差跟所有資料正交，就能解係數。若預測對象是**穩態**的，係數不隨時間改變（非常重要的觀念）：
$$R[m]-\sum_{k=1}^{\infty}h[k]R[m-k]=0,\quad m\ge1\qquad\text{(13-22)}.$$
叫 **Wiener–Hopf 方程**（數位形式）。不想記名字就說「用正交原理」——資料跟預測誤差完全正交，不用背。

**預測濾波器**：
$$H(z)=h[1]z^{-1}+h[2]z^{-2}+\cdots\qquad\text{(13-20)}.$$
為什麼沒有 $z^0$？預測用的是之前的資料，從 $z^{-1}$ 開始。老師說這很重要：$r$ 步預測就要從 $z^{-r}$ 開始，$z^{-(r-1)}$ 以前不能有係數——牽涉到濾波器 z 轉換的樣子。

---

## 2. 誤差濾波器與誤差是白的

[▶ 03:03](https://youtu.be/0gioCnJF6iE?t=183)

> **誤差濾波器** (error filter)：$e[n]=S[n]-\hat S[n]$ 是 $S$ 經過
> $$E(z)=1-H(z)=1-\sum_{n\ge1}h[n]z^{-n}\qquad\text{(13-23)}.$$
> **常數項一定是 1**。

例：$0.8-2z^{-1}$ 不可能是誤差濾波器（常數項不是 1），除非要把預測對象乘 0.8。看起來簡單，但是很基本的重要概念，隨時要想到。

> **線性預測完剩下的一定是白的**：$E\{e[n]e[n-m]\}=P\delta[m]$（式 (13-24)）。

線性預測用的是二階動差（自相關），所有二階的關係全部用完了，剩下的就拆到完全沒有關係（除非要三階、四階，那是另一個問題）。Wold 分解時算過一次。

**證明**（三行）：
1. 預測誤差跟資料正交（第一個永遠用正交原理）。
2. 之前的預測誤差 $e[n-m]$ 是之前資料的線性組合。
3. 所以之前的預測誤差跟現在的誤差正交。∎

**Gram–Schmidt 的類比**【口頭】：一維一維拉出來，跟維度有關的全部用完，剩下的一定跟之前的正交，除非再增加維度。反過來：**預測不夠好，誤差一定不夠白**。

**資料壓縮的類比**【口頭】：資訊理論裡，最好的壓縮器壓完出來是 i.i.d.（白的），可以證明；不是最好的，壓出來絕對不白——表示還可以再壓。很多自然現象都這樣，可以舉一反三。

---

## 3. Theorem 13-2：誤差濾波器的零點在單位圓內

[▶ 07:08](https://youtu.be/0gioCnJF6iE?t=428) 課本列為 theorem，表示作者認為重要（Theorem 13-1 是正交原理）。

> **Theorem 13-2**：最佳（整個過去）預測的誤差濾波器，若 $E(z_i)=0$，則 $|z_i|\le1$（式 (13-26)）。
> 零點都在單位圓內（在外面濾波器就不 stable）。

老師說一定要會證明：它牽涉兩個層面——發現別人的濾波器不夠好時，怎麼改善？把零點從外面**移進來**。

**寫成零點乘積**：
$$E(z)=1-h_1z^{-1}-h_2z^{-2}-\cdots=\prod_i\left(1-z_iz^{-1}\right).$$
（$N$ 次多項式有 $N$ 個根，可能是複數；乘回來就還原。）

**反證**：假設是最佳線性預測，但某個 $|z_i|>1$。把這個因子換掉：
$$E_0(z)=E(z)\frac{1-z^{-1}/z_i^*}{1-z_iz^{-1}}.$$
- 為什麼是 $\frac1{z_i^*}$ 不是 $\frac1{z_i}$：$z_i=|z_i|e^{j\theta_i}$，取倒數再共軛，**角度一樣**——就是在同一個角度把點往裡面移（操作上像用滑鼠拖）。不要被數學迷惑。
- **看絕對值平方**：看到線性濾波器的絕對值平方要聯想——輸出功率頻譜 = 輸入功率頻譜 × $|H|^2$。預測誤差 $P$ 是能量，所以要看濾波器的絕對值平方：
$$P=\frac1{2\pi}\int|E(e^{j\omega})|^2S(\omega)\,d\omega\qquad\text{(13-25)}.$$
  （老師說：誤差是能量、資料壓縮的 entropy 也是能量概念——很多事情都在講能量、講二次。）
- 令 $z=e^{j\omega}$，分子分母除以 $e^{j\theta_i}$，$\omega'=\omega-\theta_i$，展開成 cos、sin，實部平方加虛部平方——分子分母對消，只差一項：
$$|E_0(e^{j\omega})|=\frac{1}{|z_i|}|E(e^{j\omega})|<|E(e^{j\omega})|.$$
（細節留給同學算，不難。）
- 誤差能量變小——違反「這是最好的線性預測」。∎

**$E_0$ 還要是合法的誤差濾波器**：乘上這個因子後常數項還是 1，而且 causal。（若某項常數是 0.8，搞不好絕對值平方更小，但那不是線性預測的誤差濾波器。）

**只適用整個過去**：$E_0$ 不見得是合法的 **r-step** 誤差濾波器——乘出來 $z^{-1}$ 的係數不見得是 0（2 步預測 $z^{-1}$ 項要是 0、3 步預測 $z^{-1},z^{-2}$ 都要是 0）。所以沒有「$r$ 步預測的根一定在單位圓內」這個定理——沒辦法用同樣方法證；後面會看到 FIR 做其他線性預測時，根還會跑到外面。

**結論**：最好的預測濾波器是穩定的；系統做預測發現不穩定，表示可能不是最好的。

---

## 4. 為什麼不能直接用 z 轉換解

[▶ 17:58](https://youtu.be/0gioCnJF6iE?t=1078) Wiener–Hopf 在時域看起來是**卷積**，同學會馬上想做 z 轉換變相乘——**不行**。

**關鍵**：(13-22) 只在 **$m\ge1$** 成立（用的資料沒有用未來）。z 轉換是 $k$ 從 $-\infty$ 到 $\infty$；兩邊不是對每個 $m$ 都相等，就不能做。若對所有整數 $m$ 都有正交（像非因果 Wiener 濾波器可以用未來），就可以。所以公式給了，係數卻沒有系統化的方法解。§10 會用例子讓大家有感覺。

但**特定情況**很好解——regular。

---

## 5. Regular 過程的預測

### 5.1 用 innovations 預測

[▶ 20:01](https://youtu.be/0gioCnJF6iE?t=1201) **Regular**：在一、二階統計上，可以用白過程 $I$ 經過 causal（$k$ 從 0 開始）、stable 的濾波器 $L$ 產生：
$$S[n]=\sum_{k=0}^{\infty}l[k]I[n-k]\qquad\text{(13-27)}.$$
老師說：實際上碰到的過程大部分是 regular。

**想法**：$S$ 是用白的積木（基礎元件、螺絲）組出來的；用過去的資料做線性組合預測，相當於用這些基礎方塊預測——同樣一件事，都是線性的。

**正交原理**：預測誤差跟拿來預測的 $I$ 正交。好處：$I$ 是白的，$E\{I[n]I[m]\}$ 不是 1 就是 0。
- $R_{si}[m]=E\{S[n]I[n-m]\}=\sum l[k]\delta[m-k]=l[m]$（式 (13-30)）。
- 所以係數 $h_i[m]=R_{si}[m]=l[m]$。

> **結論**：
> $$\hat S[n]=\sum_{k=1}^{\infty}l[k]I[n-k]\qquad\text{(13-31)}.$$
> 用來組合 $S[n]$ 的係數完全一樣，**只是把現在這個方塊拿掉**（$k$ 從 1 開始）。
> 誤差 $e[n]=l[0]I[n]$，$P=l^2[0]$（式 (13-32)）。

### 5.2 預測濾波器 $H=1-\frac{l[0]}{L}$

[▶ 24:42](https://youtu.be/0gioCnJF6iE?t=1482) 我們要的是從 $S$ 進、$\hat S$ 出的濾波器 $H(z)$。**這個方塊圖非常重要**：
- $I$ 經過 $L(z)-l[0]$（扣掉常數項）得到 $\hat S$。
- 真正的輸入是 $S$：前面接 $\frac{1}{L(z)}$，$S\to I$。
- 串起來：

> $$H(z)=\frac{1}{L(z)}\left(L(z)-l[0]\right)=1-\frac{l[0]}{L(z)}\qquad\text{(13-33)},\qquad l[0]=\lim_{z\to\infty}L(z).$$
> （$z\to\infty$ 時 $z^{-1},z^{-2}$ 都是 0，剩常數項。）

**永遠記得**：碰到 regular 過程，有一個**中心點 $I$**，用來組成所有人。從 $I$ 出發往左往右走都可以（例如另一個過程是 $I$ 經過 $L'(z)$ 也沒關係）。考試可能用 $X$ 預測 $S$，但架構完全一樣。

**比喻**【口頭】：每個人最小的單位是細胞、DNA；全部拆到 DNA 再組合，可以變成另一個東西。這是拆解再重組的架構。也顯示 Wold 分解很重要：WSS 過程不見得能用 $I$ 組出來——只差一個東西，predictable 部分。

### 5.3 例 13-3：有理頻譜

[▶ 30:23](https://youtu.be/0gioCnJF6iE?t=1823) 一般的 regular 很難產生 $L$；**有理頻譜**（多項式除多項式）就很方便：取根，單位圓內的留下、外面的丟掉，就是 $L(z)$（第 22 集）。

例：$S(\omega)=\frac{5-4\cos\omega}{10-6\cos\omega}$，$L(z)=\frac{2z-1}{3z-1}$，$l[0]=\frac23$：
$$H(z)=1-\frac23\cdot\frac{3z-1}{2z-1}=\frac{-z^{-1}}{6\left(1-\frac12z^{-1}\right)}.$$
這不是 $\sum h[k]z^{-k}$ 的樣子，可以展開：$-\frac16z^{-1}\left(1+\frac12z^{-1}+\frac14z^{-2}+\cdots\right)$。但實作上常用遞迴（IIR）實現比較容易：
$$\hat S[n]-\frac12\hat S[n-1]=-\frac16S[n-1].$$

---

## 6. Kolmogorov–Szegő 公式

[▶ 32:26](https://youtu.be/0gioCnJF6iE?t=1946) 附錄有，沒給證明。誤差是 $l^2[0]$，而
$$\ln l^2[0]=\frac1{2\pi}\int_{-\pi}^{\pi}\ln|L(e^{j\omega})|^2d\omega.$$
$S(\omega)=|L(e^{j\omega})|^2$，取指數：

> **Kolmogorov–Szegő MS 誤差公式**：
> $$P=\exp\left\{\frac1{2\pi}\int_{-\pi}^{\pi}\ln S(\omega)\,d\omega\right\}\qquad\text{(13-34)}.$$

- 給功率頻譜（不管是不是有理的，只要能這樣寫），就告訴你**最好的線性預測誤差**。
- 當參考值：你的線性預測 MSE 等於這個值就是最好；比它大可能不是最好。

---

## 7. Wide-sense Markov of order $N$

[▶ 33:56](https://youtu.be/0gioCnJF6iE?t=2036) Order 1：自相關是等比級數（指數遞減），只要一點就夠——昨天的資料就夠，前天、大前天的不能增加預測準確度。Order $N$：遞減沒那麼快，要過去 $N$ 個點。

**AR 過程**：$S$ 是 AR（$L(z)=\frac{b_0}{1+a_1z^{-1}+\cdots+a_Nz^{-N}}$），直接用剛剛的觀念：
$$H(z)=-a_1z^{-1}-\cdots-a_Nz^{-N},\qquad P=b_0^2\qquad\text{(13-35)}.$$
**任何 AR 過程，預測只要過去 $N$ 個值**——這種過程叫 wide-sense Markov of order $N$。AR 過程還有一個重要性：很容易預測。

---

## 8. $r$ 步預測

[▶ 36:02](https://youtu.be/0gioCnJF6iE?t=2162) 只有 $S[n-r],S[n-r-1],\dots$（中間有一段距離）。實作上用最近的資料預測比較合理（不會用一年前的預測今天，除非這一年的資料全被銷毀）。介紹它主要是呼應 regularity：

> $$\hat S_r[n]=\sum_{k=r}^{\infty}l[k]I[n-k]\qquad\text{(13-36)},\qquad P_r=\sum_{k=0}^{r-1}l^2[k]\qquad\text{(13-38)}.$$
> 把 $r$ 個時間之前的方塊用同樣的係數組合；$0$ 到 $r-1$ 項都不見了，誤差是它們的平方和。
> $$H_r(z)=1-\frac{1}{L(z)}\sum_{k=0}^{r-1}l[k]z^{-k}\qquad\text{(13-37)}.$$

證明步驟完全一樣（$I$ 是白的，用正交原理）。老師說：這一章的證明不難，把該寫的式子寫出來答案就有了。前提是要知道 $L(z)$——有理頻譜時很好算。

**例 13-4**：$R[m]=a^{|m|}$（$0<a<1$）——指數遞減，影響過一天三分之一、再一天九分之一……一看就覺得很好預測，是 WS Markov of order 1。
$$S(z)=\frac{b^2}{(1-az^{-1})(1-az)},\quad b^2=1-a^2,\quad L(z)=\frac{b}{1-az^{-1}}.$$
代入，分母變分子乘起來只剩一項：
$$\hat S_r[n]=a^rS[n-r],\qquad P_r=1-a^{2r}.$$
$r$ 步預測只要 $n-r$ 那一點、係數 $a^r$，其他都不要——完全呼應 WS Markov order 1；它也是 AR(1)。

---

## 9. 類比預測

[▶ 42:18](https://youtu.be/0gioCnJF6iE?t=2538) 用 $t$ 以前所有的值預測 $\lambda$ 時間以後：
$$\hat S(t+\lambda)=\int_0^\infty h(\alpha)S(t-\alpha)\,d\alpha\qquad\text{(13-39)}.$$
正交原理得積分方程（Wiener–Hopf 積分形式）：
$$R(\tau+\lambda)=\int_0^\infty h(\alpha)R(\tau-\alpha)\,d\alpha,\quad\tau\ge0\qquad\text{(13-40)}.$$
不好解；**regular**（$S$ 是白的 $I$ 經過 $L$）就容易：$R_{ii}$ 是脈衝，得 $g=R_{si}=l$：

> $$\hat S(t+\lambda)=\int_\lambda^\infty l(\alpha)I(t+\lambda-\alpha)\,d\alpha,\qquad P=\int_0^\lambda l^2(\alpha)\,d\alpha.$$
> 要預測一小時後，就把 $l(\tau)$ 的前一小時扣掉（causal，從 0 開始）；扣掉那塊就是誤差（$I$ 是白的，能量是 $l^2$ 的面積）。
> $$H(s)=\frac{H_i(s)}{L(s)},\qquad h_i(t)=l(t+\lambda)U(t)\qquad\text{(13-45), (13-46)}.$$
> （$\tau=0$ 時用的是 $l(\lambda)$——用的是 $\lambda$ 以後的值。）

一般考數位的（比較好算、應用比較大），觀念完全一樣。

**例 13-5**：$R(\tau)=2\alpha e^{-\alpha|\tau|}$——等比級數，指數遞減。實際碰得到：電話話務、電話流量若是 Poisson 就是指數遞減（現在的網路一般不是）。
$$S(s)=\frac{1}{\alpha^2-s^2},\quad L(s)=\frac{1}{\alpha+s}\ (\text{取左半平面}),\quad l(t)=e^{-\alpha t}U(t),$$
$$H(s)=e^{-\alpha\lambda},\qquad\hat S(t+\lambda)=e^{-\alpha\lambda}S(t).$$
$H$ 是常數（只跟 $\alpha$、$\lambda$ 有關），$h(\tau)$ 是 delta——用 10 點的值乘一個常數預測 11 點，不需要 9 點、9:30、9:50 的資料。因為它是 WS Markov of order 1（自相關指數遞減）。老師說：常看到的現象幾乎都是這樣，雖然不一定嚴格。

---

## 10. 用 $e^{j\omega t}$ 的觀點看：為什麼傅立葉轉換不能解 Wiener–Hopf

[▶ 48:00](https://youtu.be/0gioCnJF6iE?t=2880)

**觀念**：最佳線性預測**只跟自相關有關**（和用來估計的資料的自相關）。所以任兩個過程有一模一樣的自相關（二階相等，三、四階不知道），最佳線性預測一定完全一樣。

【Q&A】[▶ 49:00](https://youtu.be/0gioCnJF6iE?t=2940) 剛剛有同學問：用 $X$ 和 $X^2$ 做（仍是線性）預測可以嗎？老師：可以，但要解兩個係數，需要資料和資料的自相關——$X^2$ 和自己要四階。給了四階就能估得好一點；只有二階，第二個係數算不出來。

**換一個過程**：定理 9-X（老師說第 9 章的投影片）：給一個功率頻譜 $A(\omega)$，存在一個「通訊訊號樣子」的過程有這個頻譜：
$$Z(t)=e^{j\omega t},\quad\omega\text{ 是隨機變數，密度}\propto A(\omega)\ \Rightarrow\ R_{zz}(\tau)=E\{e^{j\omega\tau}\}\leftrightarrow A(\omega).$$
所以要預測 $S$，乾脆不用 $S$，改預測**有同樣自相關**的 $Z$——答案會完全一樣，而且 $Z$ 的形式完全知道。老師說有人用這種觀點做最好的線性預測，他覺得非常有趣。

$$\hat Z(t+\lambda)=e^{j\omega t}H(\omega)\quad(H\text{ 是要解的濾波器，}\omega\text{ 代隨機變數}).$$

**正交原理**（$Z$ 是複數，要加共軛）：
$$E\{[Z(t+\lambda)-\hat Z(t+\lambda)]Z^*(t-\tau)\}=0,\quad\tau\ge0.$$
指數相乘就是指數相減，$t$ 消掉：
$$E\{e^{j\omega(\lambda+\tau)}\}=E\{e^{j\omega\tau}H(\omega)\}\ \Leftrightarrow\ \int e^{j\omega\tau}e^{j\omega\lambda}A(\omega)d\omega=\int e^{j\omega\tau}H(\omega)A(\omega)d\omega.$$

**看起來**：用傅立葉轉換唯一性，$A(\omega)e^{j\omega\lambda}=A(\omega)H(\omega)$——**答案是錯的**。

**紅字**：這個等式**只在 $\tau\ge0$ 成立**，$\tau<0$ 完全不成立，所以不能用傅立葉轉換的唯一性（它要對所有參數都成立）。這就是為什麼傅立葉轉換不能解 Wiener–Hopf——雖然是卷積關係。

**用例 13-5 驗證** [▶ 59:47](https://youtu.be/0gioCnJF6iE?t=3587)：$S_{zz}=\frac{4\alpha^2}{\alpha^2+\omega^2}$，已知最好的濾波器 $H=e^{-\alpha\lambda}$。代進去，左邊得 $2\alpha e^{-\alpha|\tau+\lambda|}$，右邊得 $2\alpha e^{-\alpha(|\tau|+\lambda)}$。要相等就是
$$|\tau+\lambda|=|\tau|+\lambda.$$
畫圖：$|\tau+\lambda|$ 在 $-\lambda$ 折上去；$|\tau|+\lambda$ 在 0 折上去、提升 $\lambda$。兩函數**只在 $\tau\ge0$ 相等**，$\tau<0$ 完全不等——剛好完全符合要求。若用傅立葉轉換直接說兩邊相等就錯了；只能硬解。非因果系統（所有 $\tau$ 都成立）才能用。

---

## 11. 一頁速查表

| 項目 | 公式 |
|---|---|
| Wiener–Hopf（離散） | $R[m]=\sum_{k\ge1}h[k]R[m-k]$，$m\ge1$ |
| 誤差濾波器 | $E(z)=1-H(z)$，常數項 1；誤差白：$R_{ee}=P\delta[m]$ |
| Theorem 13-2 | $E$ 的零點 $\lvert z_i\rvert\le1$（只限整個過去） |
| Regular 預測 | $\hat S=\sum_{k\ge1}l[k]I[n-k]$，$P=l^2[0]$，$H=1-\frac{l[0]}{L}$ |
| Kolmogorov–Szegő | $P=\exp\{\frac1{2\pi}\int\ln S\}$ |
| AR / WS Markov $N$ | $H=-a_1z^{-1}-\cdots-a_Nz^{-N}$，$P=b_0^2$ |
| $r$ 步 | $H_r=1-\frac1L\sum_{k<r}l[k]z^{-k}$，$P_r=\sum_{k<r}l^2[k]$ |
| 類比 | $h_i(t)=l(t+\lambda)U(t)$，$H=\frac{H_i}{L}$，$P=\int_0^\lambda l^2$ |

**關鍵步驟**：
- 誤差白：過去的誤差是過去資料的組合，和現在誤差正交。
- 零點外移改善：乘 $\frac{1-z^{-1}/z_i^*}{1-z_iz^{-1}}$，$\lvert E_0\rvert=\frac{1}{\lvert z_i\rvert}\lvert E\rvert$。
- Regular：$R_{si}[m]=l[m]$，從中心點 $I$ 出發。
- 例：$R=a^{\lvert m\rvert}$ ⇒ $\hat S_r=a^rS[n-r]$；$R=2\alpha e^{-\alpha\lvert\tau\rvert}$ ⇒ $H=e^{-\alpha\lambda}$。
- 傅立葉轉換不能解：等式只對 $\tau\ge0$ 成立（$\lvert\tau+\lambda\rvert=\lvert\tau\rvert+\lambda$ 只在 $\tau\ge0$）。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 有限過去、FIR、根跑到外面 | 下一集：finite past、Levinson、lattice |
| Wold、predictable ⇔ 線譜 | 下一集 |

---

## 附：本集一句話總結

> **用整個過去預測要解只在 $m\ge1$ 成立的 Wiener–Hopf 方程，所以不能直接用 z／傅立葉轉換；最佳預測的誤差一定是白的、誤差濾波器常數項為 1 且零點都在單位圓內；若過程是 regular（白的 $I$ 過 $L$），從中心點 $I$ 出發把現在那個方塊拿掉就是最佳預測，$H=1-l[0]/L$、誤差 $l^2[0]$（Kolmogorov–Szegő 給出 $\exp\frac1{2\pi}\int\ln S$）；$r$ 步、類比預測同理，指數遞減的自相關只要最近一點。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 13-2 (1/2) 錄影逐字稿（whisper large-v3-turbo，1:03:21）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
