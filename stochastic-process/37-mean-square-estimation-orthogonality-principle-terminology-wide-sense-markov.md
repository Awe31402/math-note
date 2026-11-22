---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 37
lecture: Lec 13-1 Mean Square Estimation — Introduction (1/2)
date: 待補
video: https://youtu.be/NmpTxlkgOhM
notes: Papoulis & Pillai 4th ed. §13-1 Introduction（式 (13-1)–(13-6)、Theorem 13-1、Terminology、Simple Illustrations: Prediction，pp. 580–582）
---

# 第 37 集 · Lec 13-1 (1/2)：均方估計、Theorem 13-1（正交原理）、名詞（smoothing / prediction / filtering）、單點預測、wide-sense Markov of order 1 [▶ 影片](https://youtu.be/NmpTxlkgOhM)

← 上一集：[36](36-euler-lagrange-optimum-windows-lms-two-to-one-rule.md) ｜ [總目錄](README.md) ｜ 下一集：[38](38-multiple-data-derivative-prediction-interpolation-noncausal-wiener-filter.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 37 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（37:44，whisper large-v3-turbo）＋ Papoulis §13-1（pp. 580–582）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「bias／variance」→「BIAS／VARIOUS」，「two-to-one rule」→「2-2-1 rule」，「Euler–Lagrange」→「Lagrange Euler／Uler-Lagrange」，「Lagrange multiplier」→「Lagrange Multiplied」，「Wold decomposition」→「Wall Decomposition／world decomposition」，「wide-sense stationary」→「Whitesense Stationary／Wisen-Stathing」，「i.i.d.」→「ID RID」，「uncorrelated」→「Uncoated」，「precoder」→「Precoder」，「weighting」→「waiting」，「mean square error」→「mean square error／mean² error」，「實數」→「時數」，「orthogonality」→「Also-Gonality／osoconative」，「Cartesian」→「Cartesian／迪卡爾」，「criterion」→「Quitearine／quiterion」，「正交」→「證交／正教」，「hyperplane」→「hyperplane」，「smoothing」→「Smoothie」，「Markov」→「Marco／Marcovian」，「wide-sense Markov」→「Wise Sense Mark／Why sense Markov」，「等比級數」→「等比極數」，「穩態」→「穩泰」，「autocorrelation」→「autochrome／autoculting／autocorhesion／autogon／autoclin」。以下一律用正確的字。

> **本集定位**：最後一章。上一集講 MSE（在 bias 和 variance 間平衡）和 2 比 1 法則；第 13 章介紹 MSE 估計器——通訊上非常常用。不再只是估頻譜，而是估**任意隨機過程**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 問題：最佳線性估計](#1-問題最佳線性估計)
- [2. 回顧 Wold 分解](#2-回顧-wold-分解)
- [3. 最廣義的線性估計 $h(\alpha,t)$](#3-最廣義的線性估計-hαt)
- [4. Theorem 13-1](#4-theorem-13-1)
  - [4.1 推導（對函數微分）](#41-推導對函數微分)
  - [4.2 最小誤差](#42-最小誤差)
- [5. 正交原理 (orthogonality principle)](#5-正交原理-orthogonality-principle)
- [6. 名詞](#6-名詞)
- [7. 單點預測](#7-單點預測)
- [8. Wide-sense Markov of order 1](#8-wide-sense-markov-of-order-1)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 問題、Wold 回顧 | [▶ 00:00](https://youtu.be/NmpTxlkgOhM?t=0) | 式 (13-1)、(13-2)，p. 580 |
| Theorem 13-1 | [▶ 04:12](https://youtu.be/NmpTxlkgOhM?t=252) | 式 (13-3)–(13-6)，p. 581 |
| 正交原理 | [▶ 13:33](https://youtu.be/NmpTxlkgOhM?t=813) | §7-4 |
| 名詞 | [▶ 20:40](https://youtu.be/NmpTxlkgOhM?t=1240) | Terminology，p. 581 |
| 單點預測、wide-sense Markov | [▶ 24:49](https://youtu.be/NmpTxlkgOhM?t=1489) | Prediction，p. 582 |

---

## 1. 問題：最佳線性估計

[▶ 00:00](https://youtu.be/NmpTxlkgOhM?t=0) 要估計任意隨機過程 $S$，觀察到資料 $X$。這種估計／預測 (prediction) 在通訊技巧非常常用。第 12 章得到的工具（Euler–Lagrange、Lagrange 乘數）大家都會了。

- **只看線性估計**：非線性估計幾乎沒辦法用很完整的理論呈現，設計技巧比較難。
- **線性估計** (best linear estimator)：資料經過卷積（濾波器）得到估計——定理 9-2、9-4 完全可以用。

---

## 2. 回顧 Wold 分解

[▶ 02:05](https://youtu.be/NmpTxlkgOhM?t=125) 這章還會用到 Wold 分解：
- WSS 過程你當然希望 **whitening**（工程上非常常見）——轉成 i.i.d. 或白的過程，每個時間彼此獨立無關、沒有能量交互影響（uncorrelated）。
- 像把一個大集體拆到最小的、彼此獨立的單元；再組合回去，**組合不回來**。
- 組合回來的叫 regular，少的那塊是 predictable。任何 WSS 過程都可以拆成 regular + predictable。

**為什麼重要**：接收端常要做 MSE 估計或預測（predictor、precoder 等都是預測動作的延伸）。最容易的是線性預測，因為可以用濾波器（卷積）的技巧。

---

## 3. 最廣義的線性估計 $h(\alpha,t)$

[▶ 03:39](https://youtu.be/NmpTxlkgOhM?t=219) 卷積是 $\int h(t-\alpha)X(\alpha)d\alpha$。這裡不寫成卷積，而寫 $h(\alpha,t)$——把它當 **weighting**（像 data window），但目標是讓 bias² + variance 最小：

$$\hat S(t)=\int_a^bh(\alpha,t)\,X(\alpha)\,d\alpha.$$

**兩個參數**：$t$ 對應**輸出**（要估計的點），$\alpha$ 對應**輸入**（資料點）。
- 例：要估 10:10 的值，抓到 9:00 到 10:00 一小時的資料；每筆資料都重要但重要性不同，每一分鐘給不同的 weighting（$\alpha$ 從 9 點到 10 點），乘上去積分。
- 要估 10:11 時，weighting 可能不一樣——**不同的輸出時間可以用不同的 weighting**。
- 所以比卷積還廣一點，是**最廣義的線性估計**。

**MSE**：
$$P=E\left\{\left[S(t)-\hat S(t)\right]^2\right\}\qquad\text{(13-2)},$$
$S(t)$ 是那個時間點真正的值，$\hat S(t)$ 是線性預測的估計值。希望最小。從第 12 章學到現在：要對期望值得到好結果，要看**二次**。

【課本補充】p. 580：課本寫 $\hat S(t)=\hat E\{S(t)|X(\xi),a\le\xi\le b\}=\int_a^bh(\alpha)X(\alpha)d\alpha$（式 (13-1)），$h(\alpha)$ 隱含依賴 $t$。$h(\alpha)$ 有不可數個未知數（每個 $\alpha\in(a,b)$ 的值）。

---

## 4. Theorem 13-1

> **Theorem 13-1**：MSE 最小 ⇔ 資料和誤差正交：
> $$E\left\{\left[S(t)-\int_a^bh(\alpha,t)X(\alpha)d\alpha\right]X(\xi)\right\}=0,\quad a\le\xi\le b\qquad\text{(13-3)},$$
> 等價於 $h$ 滿足積分方程
> $$R_{sx}(t,\xi)=\int_a^bh(\alpha,t)\,R_{xx}(\alpha,\xi)\,d\alpha,\quad a\le\xi\le b\qquad\text{(13-4)}.$$

**記號**：下標後面的 $x$ 是**觀察的資料**（後面會用很多次，所以下標弄清楚）；$s$ 是要估計的對象。我們只看得到 $X$，所以能用的只有 $R_{xx}$：用 $R_{xx}$ 乘上線性預測的係數，要逼近 $R_{sx}$。

### 4.1 推導（對函數微分）

[▶ 08:52](https://youtu.be/NmpTxlkgOhM?t=532) 又是要找一個最好的函數（$h(\alpha,t)$ 是二維函數）。比較簡單：要 MSE 最小，展開（假設實數；不是實數就比較麻煩）：
$$P=E\{S^2\}-2E\{S\hat S\}+E\{\hat S^2\}.$$
代 $\hat S$（$X$ 的線性組合），積分和期望值互換：
$$P=R_{ss}(t,t)-2\int h(\alpha,t)R_{sx}(t,\alpha)d\alpha+\iint h(\alpha,t)h(\beta,t)R_{xx}(\alpha,\beta)\,d\alpha\,d\beta.$$
（$X$ 經過兩次濾波器，跟定理 9-2 很像；$R_{sx}$ 經過一次。）**從來沒假設 WSS**，所以自相關是兩個參數——任何隨機過程都是這個結果。

**對函數的某一個值做微分**（或用 Euler–Lagrange）[▶ 10:25](https://youtu.be/NmpTxlkgOhM?t=625)：老師把二維函數離散化想像——像一個 3×3 的表 $a_{11},a_{12},\dots,a_{33}$。整個式子對 $a_2$ 偏微分：
- 有 $a_2$ 的只有「它那一列」和「它那一行」，其他項根本不用管。
- 對 $a_2$ 偏微分，那一列得到 $a_1,a_3$，那一行也得到 $a_1,a_3$——兩條；中間是平方項，有兩倍的 $a_2$，各補一個到兩條裡。
- 所以得到兩個完整的 $a_1,a_2,a_3$，再減掉兩倍的 $R_{sx}$（一維那項）。

設為 0，消掉 2，就是 (13-4)。用 Euler–Lagrange 解一模一樣。

### 4.2 最小誤差

[▶ 12:33](https://youtu.be/NmpTxlkgOhM?t=753) 代回去：二次項用 (13-4) 換成 $+1$ 倍，減兩倍那項變成 $-1$ 倍：
$$P_{\min}=R_{ss}(t,t)-\int_a^bh(\alpha,t)R_{sx}(t,\alpha)\,d\alpha\qquad\text{(13-6)}.$$
原來的功率扣掉「最好的線性預測乘上 $R_{sx}$」。

【課本補充】p. 581 的證明：用 Riemann 和近似積分，把 $(a,b)$ 切成 $m$ 段，$\hat S\approx\sum h(\alpha_k)X(\alpha_k)\Delta\alpha$，套用離散正交原理 (7-82) 得聯立方程 (13-5)，$\Delta\alpha\to0$ 就是 (13-4)。一般 (13-4) 只能數值解；本章考慮能得到顯式解的特例，除非另外說明，都假設 WSS 且實數。

---

## 5. 正交原理 (orthogonality principle)

[▶ 13:33](https://youtu.be/NmpTxlkgOhM?t=813) 剛剛是數學的結果；現在要記**定性的概念**：做估計又做線性預測時，如果有 **inner product** 的概念，就簡單多了——**正交**。

**幾何圖像**：要估的 $S$ 在 xyz 空間，資料 $X$ 只在 xy 平面上（任何函數都可以經由內積投影到高維的直角座標）。線性預測就是要讓誤差 $\|S-\hat S\|^2$（兩向量相減的 norm 平方）最小。只能做線性組合，所以最小的一定是**垂直**——誤差 $S-\hat S$ 垂直於資料平面。線性代數特別強調的正交，對應到內積。

**為什麼成立**：MSE **本身就是內積**的概念：
$$\langle X,Y\rangle=E\{XY^*\},\qquad\|e\|^2=E\{|e|^2\}.$$
期望值完全符合內積的四個基本性質。（函數的內積是兩個函數相乘的積分；直角座標的內積是座標相乘的和；期望值也是。自己跟自己的內積是 norm 平方。）

**換準則就要換內積**：如果要 minimize 四次方、或 exponential cost，就沒有這個概念，不見得有這個結果——要重新定義內積，或者根本沒有這麼漂亮的結果。而且線性預測剛好是在函數本身上做線性組合，完全符合線性代數。

> **正交原理**：最佳線性預測的**誤差**和**資料**的內積是 0：
> $$E\{[S(t)-\hat S(t)]X(\xi)\}=0.$$

**驗證**：$\hat S=\int hX$，乘上 $X$，期望值和積分互換，剛好得到 (13-4)——不是巧合，因為它剛好是內積。

**principle vs rule**【口頭】：principle 這個字很重，被稱為 principle 表示是很基本的重要結果；2 比 1 法則只叫 rule（rule of thumb）。

**線性代數的價值**【口頭】：線性代數後來放到大一，因為裡面的東西非常非常有用；第四代行動通訊就是正交概念的延續。最佳線性預測會 span 一個超平面 (hyperplane)（不一定二維，可能三、四、五維）。**第 13 章全部繞著這件事在講。**

---

## 6. 名詞

[▶ 20:40](https://youtu.be/NmpTxlkgOhM?t=1240)

- **data interval**：觀察的時間 $(a,b)$；**data**：這區間收到、直接看到的東西。

**例**【口頭】：9 點到 10 點，自動資料收集器在新竹一直抓 PM2.5 資料。想估台北（沒有 sensor、還沒來得及放），新竹台北差不遠（100 公里就開到了），所以用新竹的資料估台北。

| 名詞 | 條件 | 例 |
|---|---|---|
| **smoothing** | $t$ 在資料區間**內** | 用新竹 9–10 點估台北 9:30（類似第 34 集的 smoothed spectrum：觀察和估計時間重疊） |
| **forward predictor** | $t>b$，且 $X=S$ | 用新竹 9–10 點預測新竹 11 點 |
| **backward predictor** | $t<a$，且 $X=S$ | 用新竹 9–10 點估新竹 8 點 |
| **filtering and prediction** | $t$ 在區間外，且 $X\ne S$ | 用新竹的資料預測台北／桃園 11 點 |

- **predictor** 有一個條件：資料和要估的是**同一個隨機過程**（看新竹預測新竹）。老師開玩笑：現在空污越來越嚴重，不用 predictor 了，眼睛看就知道了。
- 名詞每本書可能不同，這本書採這個系統；理解名詞才比較能看文獻。

---

## 7. 單點預測

[▶ 24:49](https://youtu.be/NmpTxlkgOhM?t=1489) **forward predictor**：現在 11:30 下大雨，要預測 12 點下課時還下不下雨。重要條件：**stationarity**（沒有穩態很難預測；沒有 ergodic 通常也很難）。還是 Theorem 13-1，沒有新定理，只是 $X=S$。

$$R_{ss}(t,\xi)=\int_a^bh(\alpha,t)R_{ss}(\alpha,\xi)d\alpha.$$
（下標：資料對資料的自相關乘上 weighting，得到預測對資料的自相關——資料是基礎、預測在外面。）

**單點**（$a=b$）、stationary：用 $S(t)$ 預測 $S(t+\lambda)$（例如 12 點的濕度 = 11:30 的濕度乘一個常數，$\lambda$ 是半小時）：

> $$\hat S(t+\lambda)=aS(t),\qquad a=\frac{R(\lambda)}{R(0)},\qquad P=R(0)-aR(\lambda).$$

**直觀** [▶ 27:53](https://youtu.be/NmpTxlkgOhM?t=1673)：
- 自相關**降得很慢**：關聯性很強（這個時間值很大，下個時間也很大）→ 係數要放大。
- 自相關**降得很快**：$\lambda$ 一移開就瞬間掉很小 → 最好的係數要很小。
- 係數**完全正比於** $R(\lambda)$——完全吻合直覺，而且量化了自相關的重要性。
- 誤差 $R(0)-\frac{R^2(\lambda)}{R(0)}$ 比較沒辦法詮釋。
- 單點的線性預測通常不是很好。

還可以驗證正交：資料和預測誤差完全正交。

---

## 8. Wide-sense Markov of order 1

[▶ 29:59](https://youtu.be/NmpTxlkgOhM?t=1799)

**名詞拆解**：
- **wide sense**：聯想 WSS——只看一、二階動差（三、四階對工程很麻煩，簡化）。
- **Markov**：現在基於過去做預測；現在和過去可以有 transition 的關係。
- **order 1**：用過去**一個點**就夠了，不需要過去所有的時間。用 11:30 預測 12 點已經夠，不需要 11:30 以前的資料。

**Markov 性質**：$X_n$ 給定 $X_{n-1},X_{n-2},\dots$ 的機率只跟 $X_{n-1}$ 有關——Markov 把它切斷（$X_{n-2},X_{n-3}$ 可以拿掉；**不是說無關**，而是知道前一刻就完全了解 $X_n$ 的機率）。order 2：要知道過去兩個時間的值。

例【口頭】：這個學生是不是好學生？只要給我上一次考試的結果就好，去年、大前年的考試都沒有用——可以切斷，就是 order 1。

> **Wide-sense Markov of order 1**：用最近一點的最佳線性預測（乘一個常數）就是用**整個過去**的最佳線性預測。

**什麼時候成立**：自相關的比值只跟時間差有關（分子分母同減一數，比值不變）：
$$\frac{R(\lambda+\xi)}{R(\xi)}=\frac{R(\lambda)}{R(0)}\quad\Rightarrow\quad\text{等比級數},\ R(\tau)=Ae^{-\alpha|\tau|}.$$
就像 $\frac{a_3}{a_2}=\frac{a_2}{a_1}$——公比。**指數遞減**在自然界常發生（通訊上一些波形都是指數遞減）。此時 $a=e^{-\alpha\lambda}$。

**證明（正交原理）** [▶ 35:07](https://youtu.be/NmpTxlkgOhM?t=2107)：給一筆額外的資料 $S(t-\xi)$（$\xi\ge0$），有沒有用？**完全取決於正交原理**：它和目前的預測誤差正交，就沒有用（不會讓誤差更小）。
$$E\{[S(t+\lambda)-aS(t)]S(t-\xi)\}=R(\lambda+\xi)-aR(\xi)=Ae^{-\alpha(\lambda+\xi)}-e^{-\alpha\lambda}\cdot Ae^{-\alpha\xi}=0.$$
所以 9 點以前的資料全部和預測誤差正交——給我沒有用。∎

**觀念很怪？**【口頭】給三筆、五筆資料都沒用，只看最後一筆就能做最好的線性預測。這表示線性預測還蠻不好的——要讓別的資料有用，要做**非線性預測**（不排除）。

⚠️ 待確認：老師說 Markov「在 70 年代」對這方面很有貢獻，年代待查。

【課本補充】p. 582：用 $S(t)$ 和 $S'(t)$ 估 $S(t+\lambda)$：$\hat S=a_1S+a_2S'$，$a_1=\frac{R(\lambda)}{R(0)}$、$a_2=\frac{R'(\lambda)}{R''(0)}$；$\lambda$ 小時 $\hat S(t+\lambda)\approx S(t)+\lambda S'(t)$。

---

## 9. 一頁速查表

| 項目 | 公式／重點 |
|---|---|
| 線性估計 | $\hat S(t)=\int_a^bh(\alpha,t)X(\alpha)d\alpha$ |
| MSE | $P=E\{[S(t)-\hat S(t)]^2\}$ |
| Theorem 13-1 | $R_{sx}(t,\xi)=\int_a^bh(\alpha,t)R_{xx}(\alpha,\xi)d\alpha$ |
| 最小誤差 | $P=R_{ss}(t,t)-\int hR_{sx}(t,\alpha)d\alpha$ |
| 正交原理 | $E\{[S-\hat S]X(\xi)\}=0$（MSE 是內積） |
| 單點預測 | $a=\frac{R(\lambda)}{R(0)}$，$P=R(0)-aR(\lambda)$ |
| WS Markov 1 | $R=Ae^{-\alpha\lvert\tau\rvert}$，$a=e^{-\alpha\lambda}$，過去資料無用 |

**名詞**：smoothing（$t$ 在區間內）；forward/backward predictor（$X=S$，$t>b$／$t<a$）；filtering and prediction（$X\ne S$，$t$ 在外）。

**關鍵步驟**：
- 展開 MSE → 二次型 → 對 $h$ 的每一點偏微分（3×3 表：一列一行、中間兩倍）。
- 正交原理是幾何：誤差垂直於資料張成的超平面；換準則就要換內積。
- WS Markov 驗證：$R(\lambda+\xi)-aR(\xi)=0$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 正交原理、Theorem 13-1 | 下一集：更多簡單例子、smoothing、Wiener 濾波 |
| 預測、Wold 分解 | §13-2（第 39–40 集）：prediction、Kolmogorov–Szegö |
| 可預測 ⇔ 線譜（WSS） | §13-2 證明 |

---

## 附：本集一句話總結

> **最佳線性估計 $\hat S=\int h(\alpha,t)X(\alpha)d\alpha$ 讓均方誤差最小的條件是 $R_{sx}=\int hR_{xx}$——也就是正交原理：誤差和資料正交，因為 MSE 本身就是一種內積；單點預測的係數是 $R(\lambda)/R(0)$，而指數遞減自相關的過程是 wide-sense Markov of order 1，只要最近一點就夠，過去的資料都和誤差正交、沒有用。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。
2. 老師說 Markov「在 70 年代」有貢獻：年代待查。

---

*筆記依據陳伯寧老師「隨機過程」Lec 13-1 (1/2) 錄影逐字稿（whisper large-v3-turbo，37:44）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
