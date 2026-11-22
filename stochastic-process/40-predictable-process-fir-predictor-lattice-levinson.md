---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 40
lecture: Lec 13-2 Mean Square Estimation — Prediction (2/2)
date: 待補
video: https://youtu.be/R0OdhkjjYJM
notes: Papoulis & Pillai 4th ed. §13-2（Predictable processes 式 (13-49)–(13-53)、FIR predictors 式 (13-62)–(13-66)、lattice、Levinson，pp. 595–600）；§12-3 lattice
---

# 第 40 集 · Lec 13-2 (2/2)：可預測過程的頻譜是線譜、FIR 預測器（Yule–Walker、行列式公式）、不可擴充 vs 可擴充實作、lattice（butterfly）結構、前向與後向預測、Levinson 演算法、$P_N=(1-K_N^2)P_{N-1}$ [▶ 影片](https://youtu.be/R0OdhkjjYJM)

← 上一集：[39](39-prediction-infinite-past-error-filter-regular-r-step-analog.md) ｜ [總目錄](README.md) ｜ （最後一集）

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 40 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（54:46，whisper large-v3-turbo）＋ Papoulis §13-2（pp. 595–600）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「error filter」→「error filter／Aerror Process」，「wide-sense stationary」→「wise and stationary／ysense station」，「穩態」→「穩泰」，「time-average power spectrum」→「Time Average Power Spectrum」，「駐波」→「助波」，「FIR」→「FIR」，「Kalman」→「Common Predictor／Common Innovation／common filter」，「OP amp」→「OP-amplify」，「adaptive」→「adaptive」，「orthogonality principle」→「Orthogonality Principle」，「聯立方程式」→「连利方程式」，「determinant」→「determinant」，「adjoint」→「adjoint」，「線性代數」→「信心代數」，「scalable」→「scalar／scalable」，「butterfly」→「butterfly／Botterfly」，「forward／backward prediction」→「forward／backward prediction」，「歸納法」→「歸納法」，「Wiener–Hopf」→「Weiner-Hoff」，「Levinson」→「Levinson」，「recursive」→「recursive」，「Kolmogorov–Szegő」→「Komagrov-Zegel」，「線性預測」→「信心預測／星星預測」，「real」→「時數」，「complex conjugate」→「compress conjugate」，「鏡射」→「進射／鏡射」。以下一律用正確的字。

> **本集定位**：課程最後一集。講完可預測過程，再講兩個**實作**主題：FIR 預測器（主角）和 Kalman innovations（只提概念）。

---

## 目錄

- [1. 可預測過程：頻譜一定是一堆脈衝](#1-可預測過程頻譜一定是一堆脈衝)
- [2. FIR 預測器的動機](#2-fir-預測器的動機)
- [3. Yule–Walker 方程與行列式公式](#3-yulewalker-方程與行列式公式)
- [4. 直接實作：不可擴充](#4-直接實作不可擴充)
- [5. Lattice（butterfly）結構](#5-latticebutterfly結構)
  - [5.1 一級 butterfly](#51-一級-butterfly)
  - [5.2 物理意義：前向與後向預測](#52-物理意義前向與後向預測)
  - [5.3 兩個誤差濾波器的關係](#53-兩個誤差濾波器的關係)
- [6. 解 $K_N$：Levinson 演算法](#6-解-k_nlevinson-演算法)
- [7. $P_N=(1-K_N^2)P_{N-1}$](#7-p_n1-k_n2p_n-1)
- [8. 結論](#8-結論)
- [9. Kalman innovations（概念）](#9-kalman-innovations概念)
- [10. 一頁速查表](#10-一頁速查表)

---

## 1. 可預測過程：頻譜一定是一堆脈衝

[▶ 00:00](https://youtu.be/R0OdhkjjYJM?t=0) **可預測** (predictable)：完全可預測，MSE 是 0：$S[n]=\sum_{k\ge1}h[k]S[n-k]$（式 (13-49)）。這樣的過程確實存在。

**誤差能量的另一個角度**（請圈起來）：誤差乘預測對象的期望值是 $P$；而誤差是 $S$ 經過誤差濾波器 $E(z)=1-H(z)$ 的**輸出**，所以 $P$ 是輸出能量 = 輸出功率頻譜的總積分 = 輸入頻譜 × $|E|^2$：
$$P=\frac1{2\pi}\int_{-\pi}^{\pi}|E(e^{j\omega})|^2S(\omega)\,d\omega=0\qquad\text{(13-50)}.$$

**成立條件**【口頭】：這是**穩態系統**的結果——輸入 WSS、系統線性非時變、輸出也 WSS。非穩態也許可以推廣到 time-average power spectrum，但加了極限（window、$\frac1{2T}\int_{-T}^T$），有些運算要 take care，很多結果不見得容易成立。要清楚結果成立的條件。

**推理**：兩個**非負**函數相乘的積分是 0（$f,g\ge0$，$\int fg=0$），相乘一定處處是 0（除了某些特殊的脈衝點）。$|E|^2\ge0$；WSS 的功率頻譜證過 $\ge0$。所以：
- $S(\omega)>0$ 的地方，$E(e^{j\omega})$ 一定是 0。
- $E(z)$ 是多項式 $\prod(1-z_iz^{-1})$，只有有限個零點 ⇒ $S(\omega)$ 只能在那些點非零 ⇒ **一堆脈衝**：
$$S(\omega)=2\pi\sum_{i=1}^{m}\alpha_i\delta(\omega-\omega_i),\qquad S[n]=\sum_ic_ie^{j\omega_in}\qquad\text{(13-51), (13-52)}.$$

**為什麼在單位圓上：駐波**【口頭】[▶ 06:09](https://youtu.be/R0OdhkjjYJM?t=369)：期中考考過根是 $\frac12$ 的 AR——會越來越小、消失（non-stable），不會存在。根在單位圓上就不會消失：能量穩定，像**駐波**；例如根在 $e^{j\pi/2}$，每個時間轉一下，四次就回來，一直循環、不變大也不變小、卡在那裡。

（老師提醒：可預測過程不見得要穩態；但若是穩態，根一定在單位圓上。）

【課本補充】p. 596：反過來也對：$S[n]$ 是 $m$ 個指數的和，則可預測，預測濾波器 $1-D(z)$，$D(z)=\prod_i(1-e^{j\omega_i}z^{-1})$（式 (13-53)）。p. 596–598：Wold 分解的建構式證明（Theorem 13-3）——就是第 28 集老師講的那個證明。

---

## 2. FIR 預測器的動機

[▶ 08:10](https://youtu.be/R0OdhkjjYJM?t=490) 最後兩個主題都講實作。

**FIR 預測器**：永遠用**固定的過去 $N$ 個值**預測——預測 $S[n+1]$ 時把最舊的值丟掉。
- 為什麼：這樣才能**用硬體實作**。硬體的 order 是固定的（電子學、電路學：用幾個 OP amp 就是幾級）。不固定也不一定做不出來（例如 adaptive），但這裡的出發點跟實作比較有關聯。

**對比：Kalman innovations**：從 $S_0$ 出發，用 $S_0$ 預測 $S_1$；有了 $S_1$ 就一起預測 $S_2$……預測 $S_{10}$ 時用 $S_1$ 到 $S_9$ 全部——window 不固定，把過去所有知道的資料都拿來用。考慮比較周詳，但實作上比較複雜，除非自相關有比較好的性質。

---

## 3. Yule–Walker 方程與行列式公式

[▶ 12:45](https://youtu.be/R0OdhkjjYJM?t=765)
$$\hat S_N[n]=\sum_{k=1}^{N}a_k^NS[n-k]\qquad\text{(13-62)}.$$
（上標 $N$ 是 order。）**正交原理**（第一步一定要會）：$N$ 個方程，$N$ 元一次聯立方程，寫成矩陣：
$$R[m]-\sum_{k=1}^{N}a_k^NR[m-k]=0,\quad1\le m\le N\qquad\text{(13-65)}.$$
預測誤差（實數，不加共軛）：誤差乘預測對象取期望值：
$$P_N=R[0]-\sum_{k=1}^{N}a_k^NR[k].$$

**整合成一個大方程**：要同時解 $P_N$ 和 $a_1,\dots,a_N$。$(N+1)\times(N+1)$ 的自相關矩陣 $D_{N+1}$ 乘 $(1,-a_1,\dots,-a_N)^T$ 等於 $(P_N,0,\dots,0)^T$（第一列是 $P_N$ 的式子，其他列是正交原理的 0）。用 $D\cdot\mathrm{adj}(D)=\det(D)\,I$（線性代數），得

> $$P_N=\frac{\Delta_{N+1}}{\Delta_N}\qquad\text{(13-66)},$$
> $\Delta_N$ 是 $N\times N$ 自相關矩陣的行列式。

⚠️ 逐字稿缺字：老師說投影片要更正為 determinant；口頭說「$P_N$ 等於 $D_N$ 乘上 $D_{N+1}$」是口誤，依課本 (13-66) 是相除。

**用途**：做線性預測要決定用幾階（2、3、4、5，一般可能到 6）——看誤差夠不夠小，而誤差完全由自相關決定。分母不能是 0；若 $\Delta_{N+1}=0$，就是 predictable（係數百分之百準確）。

---

## 4. 直接實作：不可擴充

[▶ 17:55](https://youtu.be/R0OdhkjjYJM?t=1075) 解出係數就得到誤差過程 $e[n]=S[n]-\hat S[n]$，所以 $\hat S[n]=S[n]-e[n]$。實作：$N$ 階濾波器，每一級一個 delay、一個乘法器乘係數，全部加起來得誤差（通常送誤差）；要還原預測就和原資料加減（老師說「這要會畫，可能會考系統圖」）。

**問題：scalable 嗎？** [▶ 18:57](https://youtu.be/R0OdhkjjYJM?t=1137) 覺得 $P_N$ 不夠小，想用 $N+1$ 階——要不要整個重新設計？
- **scalable**：原來的架構都能用，只要在上面加一個小東西（像積木），不用拆掉重建。真正的設計要調 (tune) 很久，係數是用電容電感逼近出來的、還要補償。
- 這個結構**不可擴充**：多一階，所有係數都不一樣，整個要重新調。

**例**：$R[0]=1$、$R[\pm1]=\rho$、其他是 0。
- $N=1$：$a_1=\rho$。
- $N=2$：$\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\begin{pmatrix}a_1\\a_2\end{pmatrix}=\begin{pmatrix}\rho\\0\end{pmatrix}$ ⇒ $a_1=\frac{\rho}{1-\rho^2}$、$a_2=\frac{-\rho^2}{1-\rho^2}$（以下**不是逐字稿內容**，是依 Yule–Walker 推出來的數值）。
最好的 $a_1$ 變了，要重新設計。

⚠️ 逐字稿缺字：老師說看到 $\rho^m$ 會以為是 WS Markov of order 1 但其實不是（只有 $m=0,\pm1$ 有值）——這點對；但他接著說「所以它不是 WSS」應是口誤：這個自相關只跟時間差有關，是 WSS（MA(1)），只是不是 WS Markov。

---

## 5. Lattice（butterfly）結構

[▶ 22:03](https://youtu.be/R0OdhkjjYJM?t=1323) 希望增加一階時原來架構都不動、只加一級。學 DSP 的知道 FFT 的基本單元是 **butterfly**，非常有用。

### 5.1 一級 butterfly

[▶ 22:34](https://youtu.be/R0OdhkjjYJM?t=1354) 輸入 $A$（$S[n]$），輸出 $B_1$、$C_1$；中間交叉，一條差一個 delay，係數 $K_1$：
$$\hat e_1[n]=S[n]-K_1S[n-1],\qquad\check e_1[n]=-K_1S[n]+S[n-1].$$
（考試看著架構寫，問題不大。）一直往上堆 butterfly 就能堆出要的東西——regular structure，硬體設計非常喜歡。

**兩個重點**：
1. 解出的 $K_1,K_2,\dots$ 要等效於前面的 $a$。
2. **$K$ 不可以隨 $N$ 改變**——$a_k^N$ 會隨 $N$ 變（例子已示範），但 $K_1$ 調好擺著就能用；加一階時 $K_1,K_2$ 不用動，只加 $K_3$。這才是重點。

### 5.2 物理意義：前向與後向預測

[▶ 26:41](https://youtu.be/R0OdhkjjYJM?t=1601) 例 $N=3$：
- $\hat e$：用 $S_3,S_2,S_1$ 預測 $S_4$ 的誤差——**forward prediction**。
- $\check e$：用**未來**的 $S_1,S_2,S_3$ 預測 $S_0$ 的誤差——**backward prediction**。

**為什麼要預測過去（我們不要的）？** 重點：**兩者的最佳係數一樣**。
- 觸發的觀察：系統是**穩態**的——現在跟未來的統計關係，跟現在跟過去的完全一樣。10 點預測 11 點，跟用 11 點預測 10 點是同一件事；相關性完全對稱。
- 證明：正交原理。WSS 的自相關只跟時間差有關，正的負的是同一件事。

**研究的觸發**【口頭】[▶ 30:17](https://youtu.be/R0OdhkjjYJM?t=1817)：butterfly 會額外產生一條「完全沒用」的資料——我們要 forward、不要 backward，但用另一條來輔助，讓設計 scalable。這條輔助一定要跟原來那條**配對**、像鏡子一樣完全一樣，才能讓係數跟 $N$ 無關。

【課本補充】p. 599：$\check S_N[n]=\sum_{k=1}^Na_k^NS[n+k]$；後向誤差 $\check e_N[n]=S[n-N]-\check S_N[n-N]$ 是 $S$ 經過 $\check E_N(z)=z^{-N}\hat E_N(1/z)$。

### 5.3 兩個誤差濾波器的關係

[▶ 31:24](https://youtu.be/R0OdhkjjYJM?t=1884)
$$\hat E_1(z)=1-K_1z^{-1},\qquad\check E_1(z)=-K_1+z^{-1}=z^{-1}\hat E_1(1/z).$$
串兩級（老師請同學會畫）：
$$\hat E_N(z)=\hat E_{N-1}(z)-K_Nz^{-1}\check E_{N-1}(z),\qquad\check E_N(z)=z^{-1}\check E_{N-1}(z)-K_N\hat E_{N-1}(z).$$

> **Lemma 1**：$\check E_N(z)=z^{-N}\hat E_N(1/z)$。

**證明**（歸納法）：$N=1$ 成立；假設 $N$ 成立，代上面的遞迴式證 $N+1$。因為是 recursive，一定對。

**零點**：$\hat E_N$ 的根可以證明在單位圓內（拆成 $\prod(1-z_iz^{-1})$，有根在外面就拉進來得到更小的誤差，同第 39 集）。$\check E_N$ 沒有這個性質——係數倒過來、常數項位置不同，不能用同樣技巧；可以舉例看到它的根會跑出去。所以不能說「線性預測一定在裡面」，只有某些特定形式。

---

## 6. 解 $K_N$：Levinson 演算法

[▶ 36:04](https://youtu.be/R0OdhkjjYJM?t=2164) 最重要的問題：係數不能跟 $N$ 有關。（老師強調三次：這一頁一定要會算，通常會請同學算。）

**比較係數**：用結構的遞迴 $\hat E_N=\hat E_{N-1}-K_Nz^{-1}\check E_{N-1}$，代入 $\hat E_N(z)=1-\sum a_k^Nz^{-k}$、$\check E_{N-1}=z^{-(N-1)}\hat E_{N-1}(1/z)$，同次方係數相等：
$$a_N^N=K_N,\qquad a_k^N=a_k^{N-1}-K_Na_{N-k}^{N-1}.$$
配對配得好時，$K$ 跟 $N$ 無關。

**但這樣還要先解 $a$** [▶ 39:09](https://youtu.be/R0OdhkjjYJM?t=2349)：新結構實作上只需要 $K_1,K_2,K_3$，**完全不需要 $a$**。先解 $a$ 再轉成 $K$ 很怪。希望**直接從自相關解 $K$**（it remains to solve $K_N$ directly based on the autocorrelation）。

**回到 Wiener–Hopf**，抓最後一條（$m=N$，乘出來是 0），把有 $K$ 的放一起：
$$K_N=\frac{R[N]-\sum_{k=1}^{N-1}a_k^{N-1}R[N-k]}{P_{N-1}}.$$
還脫離不了 $a$，但沒關係——寫成**遞迴演算法**：

> **Levinson 演算法**：
> - $K_1=a_1^1=\frac{R[1]}{R[0]}$，$P_1=(1-K_1^2)R[0]$。
> - 對 $N=2,3,\dots$：$K_N=\frac{1}{P_{N-1}}\left(R[N]-\sum_{k=1}^{N-1}a_k^{N-1}R[N-k]\right)$；$a_k^N=a_k^{N-1}-K_Na_{N-k}^{N-1}$，$a_N^N=K_N$；$P_N=(1-K_N^2)P_{N-1}$。

一層一層用遞迴的 $a$ 帶回來解 $K$。老師說：Levinson 的目標是用自相關直接解 $K$，沒有完全成功——目前的結果是這樣。

---

## 7. $P_N=(1-K_N^2)P_{N-1}$

[▶ 43:45](https://youtu.be/R0OdhkjjYJM?t=2625) **為什麼重要**：知道 $K$ 馬上知道誤差降多少：$P_1$ 加一級乘 $1-K_1^2$、再加一級乘 $1-K_2^2$……例：$K=0.5$ 降成 $\frac34$；$K=0.3$ 乘 $0.91$。若 $K$ 都一樣，就是**指數遞減**（等比級數）——多加一級掉一個比例。

**推導**（老師說投影片寫得不清楚，「這個都不要看」，改用更直觀的）：
$$\hat e_N[n]=\hat e_{N-1}[n]-K_N\check e_{N-1}[n-1].$$
兩邊乘預測對象 $S[n]$ 取期望值——**誤差乘預測對象 = 誤差能量**：
- 左邊：$P_N$（不用算）。
- 第一項：$P_{N-1}$（不用算）。
- 只要算最後一項：$E\{\check e_{N-1}[n-1]S[n]\}$。它是後向預測的誤差；穩態下，用三個值往前預測和往後預測的誤差應該完全相等（不相等就很怪）。算一下、比較係數得 $K_NP_{N-1}$。

$$P_N=P_{N-1}-K_N^2P_{N-1}=(1-K_N^2)P_{N-1}.$$

課本還有別的結構，這只是其中一個範例。

---

## 8. 結論

[▶ 50:29](https://youtu.be/R0OdhkjjYJM?t=3029)
1. 用越多資料、又是最好的線性預測，誤差應該越來越小 ⇒ **$|K_N|<1$**。$|K|$ 越接近 1，改善越大。
2. 根在單位圓內（沒證明）：在單位圓上多一個根沒什麼幫助；每一級都有改善，誤差濾波器應在單位圓內。
3. **到某一級之後沒改善？** 例如 WS Markov of order $N$，某一級之後就不用再加。

   ⚠️ 老師這裡說法前後不一：先說「那時算出來 $K_n$ 會是 1」（並說誤差到 0、根在單位圓上），後面又說「到某一級以後都一樣時 $K_i$ 通通都是 0」。以下**不是逐字稿內容**，是依 $P_N=(1-K_N^2)P_{N-1}$ 推論的：**誤差不再下降** ⇒ $K_N=0$（WS Markov of order $N$ 時 $K_{N+1}=K_{N+2}=\cdots=0$）；**誤差降到 0**（predictable）⇒ $|K_N|=1$，根在單位圓上。

4. 一直增加級數，誤差越來越小，極限是 **Kolmogorov–Szegő**：$P_\infty=l^2[0]=\exp\frac1{2\pi}\int\ln S$（⚠️ 逐字稿缺字：老師說投影片忘了打平方，是 $l^2[0]$）。

---

## 9. Kalman innovations（概念）

[▶ 53:04](https://youtu.be/R0OdhkjjYJM?t=3184) 剩三張投影片只講概念：把**過去所有資料**都拿來用（不是過去 $N$ 筆），所以係數和前面不一樣。課本有一節專門介紹，實用上在特殊應用有用途。基本觀念一樣：
- 係數怎麼解：**正交原理**——記得這件事，後面就容易看懂。
- 得到的結果是 **whitening**。
- 比較麻煩的是係數沒辦法系統化。

---

## 10. 一頁速查表

| 項目 | 公式／重點 |
|---|---|
| 可預測 | $P=\frac1{2\pi}\int\lvert E\rvert^2S=0$ ⇒ $S$ 是線譜，根在單位圓上（駐波） |
| FIR（Yule–Walker） | $R[m]=\sum_{k=1}^Na_k^NR[m-k]$，$1\le m\le N$ |
| 誤差 | $P_N=R[0]-\sum a_k^NR[k]=\frac{\Delta_{N+1}}{\Delta_N}$ |
| Lattice | $\hat E_N=\hat E_{N-1}-K_Nz^{-1}\check E_{N-1}$，$\check E_N=z^{-1}\check E_{N-1}-K_N\hat E_{N-1}$ |
| 前後向 | $\check E_N(z)=z^{-N}\hat E_N(1/z)$（穩態 ⇒ 係數相同） |
| Levinson | $K_N=\frac{R[N]-\sum a_k^{N-1}R[N-k]}{P_{N-1}}$，$a_k^N=a_k^{N-1}-K_Na_{N-k}^{N-1}$ |
| 誤差遞減 | $P_N=(1-K_N^2)P_{N-1}$，$\lvert K_N\rvert<1$ |

**關鍵步驟**：
- 可預測：兩個非負函數乘積積分為 0 ⇒ 處處為 0 ⇒ 頻譜只在 $E$ 的有限零點非零。
- scalable：$a_k^N$ 隨 $N$ 變，$K_N$ 不變；靠前向／後向鏡射配對。
- $P_N$ 遞迴：等式兩邊乘 $S[n]$，用「誤差 × 預測對象 = 誤差能量」。

---

## 附：本集一句話總結

> **穩態的可預測過程誤差為 0，逼得頻譜只能是誤差濾波器零點上的脈衝（單位圓上的駐波）；實作上用固定 $N$ 階的 FIR 預測器，直接實作每加一階都要重調，但用 butterfly 的 lattice 結構把前向預測和鏡射的後向預測配對，反射係數 $K_N$ 就不隨階數改變，可用 Levinson 遞迴從自相關算出，且每加一級誤差乘上 $1-K_N^2$。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。
2. 「到某一級之後沒改善時 $K$ 是 1 還是 0」：老師前後說法不同（見 §8）。

---

*筆記依據陳伯寧老師「隨機過程」Lec 13-2 (2/2) 錄影逐字稿（whisper large-v3-turbo）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
