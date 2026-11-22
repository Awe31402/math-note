---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 24
lecture: Lec 11-2 Spectral Representation — Finite-Order Systems and State Variables (2/3)
date: 待補
video: https://youtu.be/2_VK7-qh-Q0
notes: Papoulis & Pillai 4th ed. §11-2 Discrete-Time Systems、Finite-order processes（式 (11-31)–(11-38)，pp. 506–507）；§11-1 regular process 回顧
---

# 第 24 集 · Lec 11-2 (2/3)：回顧 regular process、部分分式、離散有限階過程的脈衝響應與自相關（課本少了一項） [▶ 影片](https://youtu.be/2_VK7-qh-Q0)

← 上一集：[23](23-state-variables-finite-order-processes-continuous.md) ｜ [總目錄](README.md) ｜ 下一集：[25](25-ar-ma-arma-yule-walker-line-spectrum.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 24 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（42:49，whisper large-v3-turbo）＋ Papoulis §11-2（pp. 506–507）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「probability space」→「propriet space」，「實數」→「時數」，「impulse response」→「input response」，「pole」→「poor／por／paw」，「Papoulis」→「popolis」，「partial fraction」→「partial fraction／partual fraction／partial friction」，「discrete」→「discreet」，「wide-sense stationary」→「Widesense／wisen stationary」，「predictable」→「predictable」，「inverse Laplace transform」→「inverse laplace transform」，「Hurwitz polynomial」→「Hervis Polynomial」，「unit circle」→「單位元／unicircle」，「minimum phase」→「minimum phase」，「causal」→「causal」，「complex conjugate」→「Complete Conjugate／Cumpler-Country」，「Kronecker delta」→「direct or connect delta function」，「inverse Fourier series」→「inverse fully series」，「time domain」→「tine domain／title 面」，「frequency domain」→「frequent domain」，「通分」→「通分」，「高中」→「高中」。以下一律用正確的字。

> **接上一集**：上一集講了連續時間的狀態變數系統和有限階過程。這一集先回顧 regular process 和第 11 章的脈絡，再完成**離散時間有限階過程**：用部分分式拆解，脈衝響應就是根的 $n$ 次方；頻譜拆成兩份相加時，老師指出**課本少了一項**常數。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：regular process、stable、causal](#1-回顧regular-processstablecausal)
- [2. 第 11 章的脈絡與預告（分解定理）](#2-第-11-章的脈絡與預告分解定理)
- [3. 部分分式](#3-部分分式)
- [4. 回顧：連續時間「相乘變相加」的拆解](#4-回顧連續時間相乘變相加的拆解)
- [5. 線性代數小事：$C\mathbf{u}=0$ 對任意 $\mathbf{u}$ ⇒ $C=0$](#5-線性代數小事cmathbfu0-對任意-mathbfu--c0)
- [6. 離散有限階過程](#6-離散有限階過程)
  - [6.1 定義](#61-定義)
  - [6.2 $m\le n$：常數項是一個在原點的根](#62-mle-n常數項是一個在原點的根)
  - [6.3 脈衝響應：根的 $n$ 次方](#63-脈衝響應根的-n-次方)
  - [6.4 頻譜拆成相加：課本少了一項](#64-頻譜拆成相加課本少了一項)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 回顧 regular、stable、causal | [▶ 00:00](https://youtu.be/2_VK7-qh-Q0?t=0) | §11-1 |
| 第 11 章脈絡、分解定理預告 | [▶ 05:14](https://youtu.be/2_VK7-qh-Q0?t=314) | §11-4（之後） |
| 部分分式、相乘變相加 | [▶ 07:21](https://youtu.be/2_VK7-qh-Q0?t=441) | 式 (11-28) |
| 離散有限階過程 | [▶ 19:42](https://youtu.be/2_VK7-qh-Q0?t=1182) | 式 (11-34)–(11-37)，p. 507 |

---

## 1. 回顧：regular process、stable、causal

[▶ 00:00](https://youtu.be/2_VK7-qh-Q0?t=0)

- 廣義來說，任何從機率空間到實數的 well-defined 映射都是隨機過程。
- 第 11 章專注一個特別的 class：**regular process**——一般用**線性濾波器**可以觀察到的輸出。輸入是白雜訊；濾波器要合理：**穩定**而且**因果**（實作一定做 stable、causal 的濾波器）。

| | 定性描述 | 數學描述 |
|---|---|---|
| **Causal** | 沒有輸入就沒有輸出 | 脈衝響應 $h(\tau)=0$（$\tau<0$），若且唯若（前提是有脈衝響應） |
| **Stable** | 輸入有界 → 輸出有界；不會輸入有限能量、輸出無限能量 | 寫成 $\frac{N(s)}{D(s)}$ 時，pole 在 $s$ 平面左半邊 |

**只看有限的 pole**【口頭】：嚴謹一點應加「finite」。Papoulis 的例子和習題看的都是有限的 pole。例如微分器 $j\omega$，$\omega\to\infty$ 時衝到無限大，有人詮釋成「pole 在無限大」；但實作上不會讓頻率無限大，也做不到，所以忽略。這樣 regular process 的定義稍微廣一點，不看無限大那種比較 tricky 的情況。（每個作者的想法可能不一樣。）

---

## 2. 第 11 章的脈絡與預告（分解定理）

[▶ 05:14](https://youtu.be/2_VK7-qh-Q0?t=314)

- 廣義的 regular process 很難分析。作者的理念：**比較好分析的都是多項式**（$N(s)/D(s)$、離散的 $N(z)/D(z)$）。
- 為什麼中間插了 §11-2（狀態變數）？因為：**用線性狀態方式定義的系統，算出的轉移函數最後都是多項式除以多項式**——通常就是這樣實作的。最後的廣義式子都能轉成狀態的形式。

**預告：這一章最後最重要的結果**（老師說會仔細講證明）[▶ 08:22](https://youtu.be/2_VK7-qh-Q0?t=502)：

> **分解**：任何 WSS 過程都可以拆成兩個隨機過程的和：
> $$X=\text{regular process}+\text{predictable process}.$$

- **predictable**（可預測的）：完全可預測——給過去（例如過去三天）的值，明天會出現什麼值你百分之百可以預測，**沒有預測誤差**。它也是隨機的：沒給過去的值時，當然是隨機的。（可以說它是 irregular process。）
- **regular**：來自白雜訊，有過去的值預測未來，**還是會有誤差**。
- 意義：做任何 WSS 過程的分析時，都可以用這個拆解做調整——第一部分是線性濾波器產生的 regular process，第二部分是完全可預測的過程。

---

## 3. 部分分式

[▶ 07:21](https://youtu.be/2_VK7-qh-Q0?t=441) 處理多項式時常把它拆成一次式：**部分分式** (partial fraction)。例：
$$\frac{\cdots}{(z-1)(z-2)}=\frac{A}{z-1}+\frac{B}{z-2}.$$
只要通分、左右兩邊比較係數，就得到 $A$、$B$。高中以前就應該會，老師請大家手寫練習二次、三次式的拆解——**只要是二次式，就拆到一次式**，方便運算。

---

## 4. 回顧：連續時間「相乘變相加」的拆解

[▶ 10:56](https://youtu.be/2_VK7-qh-Q0?t=656) 每個數學背後都有想法。

- 線性濾波器：輸出頻譜 = 輸入經過濾波器兩次，所以 $S(s)=L(s)L(-s)$（相乘）。
- 目標：**拆成兩份相加**，而且兩份互相對稱。

**為什麼不是隨便拆？** 偶函數拆成兩份對稱相加，有非常多種方法（不唯一）：最直觀的是右半邊一塊、左半邊是它的鏡像；也可以左右各取一點對調再加。這裡的拆解有特色：

1. **pole 和原來一樣**（$s_1,s_2,\dots$ 沒變）。
2. **上標 $+$ 有意義**：反 Laplace 轉換後，時域只有 $\tau>0$ 有值。因為 $s_i$ 選在左半平面。（頻域左右兩邊都可能有值，但時域只有正的部分；概念上像因果，但它不是濾波器，所以不叫 causal。）
3. 唯一差別是**分子的係數**：原來 $\gamma_i$，變成 $\alpha_i=\gamma_iL(-s_i)$——把左半平面的根加負號（例如 $-2,-3$ 變 $2,3$）代進原來的函數，乘上原係數。

（老師說這個拆解在頻域只拆一半，不是我們真正要的；要的是在時域拆一半、左右剛好對稱。）

**用例子對應**【口頭】：
- $L=\frac1{s+\alpha}$：$\gamma=1$；代對稱點 $+\alpha$：$L(\alpha)=\frac1{2\alpha}$，所以 $\alpha_1=\frac1{2\alpha}$。
- $L=\frac{1}{(s+1)(s+2)}=\frac1{s+1}-\frac1{s+2}$：根 $-1,-2$；代 $+1$：$L(1)=\frac1{2\cdot3}=\frac16$；代 $+2$：$L(2)=\frac{1}{3\cdot4}=\frac1{12}$，原係數 $-1$，所以 $-\frac1{12}$。

老師說：介紹狀態變數系統的目的，是讓大家知道用線性的狀態定義，出來都是多項式除以多項式；狀態的改變是線性的（下一個時間的狀態 = 之前狀態的線性組合，$A$ 是矩陣）。如果是非線性的狀態改變，就沒有這樣的線性結果。

---

## 5. 線性代數小事：$C\mathbf{u}=0$ 對任意 $\mathbf{u}$ ⇒ $C=0$

[▶ 20:45](https://youtu.be/2_VK7-qh-Q0?t=1245) 上一集從 $(z\Phi-A)\mathbf{u}=I\mathbf{u}$（$\mathbf{u}$ 任意）推出 $z\Phi-A=I$。為什麼對？

> 若 $A\mathbf{u}=B\mathbf{u}$ 對任意 $\mathbf{u}$，則 $A=B$。等價：若 $C\mathbf{u}=\mathbf{0}$ 對任意 $\mathbf{u}$，則 $C$ 是零矩陣。

**證明（一句話）**：若 $C$ 有任何非零元素，絕對可以選一個 $\mathbf{u}$ 讓 $C\mathbf{u}\ne\mathbf{0}$。例：$C=\begin{pmatrix}1&0\\0&0\end{pmatrix}$，取 $\mathbf{u}=(1,0)^T$，$C\mathbf{u}=(1,0)^T\ne\mathbf{0}$。矛盾。 ∎

---

## 6. 離散有限階過程

### 6.1 定義

[▶ 19:42](https://youtu.be/2_VK7-qh-Q0?t=1182) 實作上有狀態變數的線性系統，最廣義的形式：分子是 $z^{-1}$ 的 $M$ 次多項式、分母是 $N$ 次多項式。習慣用 $z^{-1}$ 而不是 $z$：$z^{-1}$ 代表**過去**，從過去做線性組合到未來。

> **離散有限階過程**：
> $$L(z)=\frac{N(z)}{D(z)}=\frac{b_0+b_1z^{-1}+\cdots+b_Mz^{-M}}{1+a_1z^{-1}+\cdots+a_Nz^{-N}},\qquad S(z)=L(z)L(1/z)\qquad\text{(11-34), (11-36)},$$
> 多項式的根都在**單位圓內**（濾波器才穩定）。

老師說：將來到業界設計系統，$z$ 域多項式的根一定要在單位圓內，因為要穩定。

**它一定是 regular 嗎？** [▶ 23:21](https://youtu.be/2_VK7-qh-Q0?t=1401) 這裡只說根在單位圓內，沒說一定 regular。regular 要求 $L$ 和 $1/L$ 都因果穩定（最小相位）：
- 對過程本身，只看 **pole**（決定穩不穩定）。
- 因為還要看倒數，所以 **zero** 的位置也很重要（倒數時 zero 變 pole）。

### 6.2 $m\le n$：常數項是一個在原點的根

[▶ 25:25](https://youtu.be/2_VK7-qh-Q0?t=1525) 先假設分子次數 $M\le N$（$M>N$ 之後的章節討論）。課本沒討論**等號**，老師補上：根可以是 0。

- 分子分母次數相同時，可以先除出一個**常數**。例：$\frac{1+2z^{-1}+3z^{-2}}{1+2z^{-1}+4z^{-2}}=1+\frac{-z^{-2}}{1+2z^{-1}+4z^{-2}}$。
- 這個常數可以寫成 $\frac{\gamma_1}{1-0\cdot z^{-1}}$——**相當於一個根在原點** $z_1=0$。
- 常數係數就是 $\frac{b_N}{a_N}$（最高次項係數相除）。
- 根在原點只會有一個；除完之後分子次數一定小於分母，其他根 $z_2,z_3,\dots\ne0$——符合課本後面的推導。

所以把等號放進來，形式沒有改變，沒有例外。

### 6.3 脈衝響應：根的 $n$ 次方

[▶ 30:04](https://youtu.be/2_VK7-qh-Q0?t=1804) 部分分式拆成一次式的和（假設根是單根）：
$$L(z)=\sum_i\frac{\gamma_i}{1-z_iz^{-1}}.$$

為什麼要拆？因為算時域脈衝響應就容易了：
$$\frac{1}{1-a}=1+a+a^2+a^3+\cdots\quad(|a|<1),\qquad\frac{\gamma_i}{1-z_iz^{-1}}=\gamma_i\left(1+z_iz^{-1}+z_i^2z^{-2}+\cdots\right).$$
$z^{-k}$ 就是延遲 $k$ 格，所以
$$\boxed{l[n]=\sum_i\gamma_iz_i^nU[n]}.$$

- 脈衝響應就是**根的 $n$ 次方**乘係數。例：根 $\frac12$ → 那一項是 $\left(\frac12\right)^n$。
- **為什麼要根在單位圓內**：$\left(\frac12\right)^n$ 的連加是等比級數，才會**收斂**，系統才穩定。
- $z_1=0$ 那一項：常數的反轉換是 Kronecker delta（$n=0$ 是 1，其他是 0），一個脈衝。

**直觀**【口頭】：看到一個多項式系統（例如 5 階，5 個根），熟練的設計者看**根的位置**就猜得到脈衝響應收斂多快：就是 5 項相加，每項是根的 $n$ 次方。根越接近原點衰減越快：$0.9^n$ 衰減慢，$0.1^n$ 衰減很快。所以根的位置很重要；設計者調整 pole 的位置，就知道速度，也知道這個隨機過程自相關的衰減有多快。

### 6.4 頻譜拆成相加：課本少了一項

[▶ 35:09](https://youtu.be/2_VK7-qh-Q0?t=2109)

$$S(z)=L(z)L(z^{-1}).$$
（$z=e^{j\omega}$，所以 $z$ 的共軛剛好是 $e^{-j\omega}=z^{-1}$。）

兩個都拆成部分分式相乘，再拆成相加。**課本在這一步少了一項**（最後結果是對的，過程有問題）：

**驗證（通分）**：
$$\frac{1}{1-z_iz^{-1}}\cdot\frac{1}{1-z_kz}=\frac{A}{1-z_iz^{-1}}+\frac{B}{1-z_kz}+\text{(常數)}.$$
把右邊兩個一次式通分，分母乘開是 $1-z_kz-z_iz^{-1}+z_iz_k$；兩個相乘時 $z$ 和 $z^{-1}$ 會消掉，多出 $z_iz_k$ 這個常數，所以**還需要補一個常數項**才能完全對上。（連續時間的 $\frac{1}{s+\alpha}\cdot\frac{1}{-s+\alpha}$ 通分時 $s$ 和 $-s$ 剛好消掉、沒有常數，所以不用補。）

整理後（以下式子**不是逐字稿原文**，是依老師說明、由 $R[m]=\sum\alpha_iz_i^{|m|}$ 反推補完整的）：
$$S(z)=\underbrace{\sum_i\frac{\alpha_i}{1-z_iz^{-1}}}_{S^+(z)}+\underbrace{\sum_i\frac{\alpha_i}{1-z_iz}}_{S^+(1/z)}-\sum_i\alpha_i,\qquad\alpha_i=\gamma_i\,L(1/z_i).$$

- 兩塊幾乎完全對稱，分子一樣。
- **係數**：和連續時間一樣的想法——連續是把根代到另一半平面（$s_i\to-s_i$）；離散是把單位圓內的根**取倒數**代到單位圓外（$z_i\to1/z_i$），重新算係數。
- 上標 $+$：反轉換只在正的部分有值，因為根就是原來的根，都在單位圓內。

**時域**：每一份是 $\alpha_iz_i^m$，所以
$$R[m]=\sum_i\alpha_iz_i^{|m|}\qquad\text{(11-37)}.$$

**少的那一項影響什麼** [▶ 40:16](https://youtu.be/2_VK7-qh-Q0?t=2416)：常數的反轉換是一個脈衝，**只影響原點** $m=0$。
- 兩份對稱相加：$\sum\alpha_iz_i^m$（$m\ge0$）和 $\sum\alpha_iz_i^{-m}$（$m\le0$），在 $m=0$ 都有 $R^+[0]$，**重複算了一次**。
- 補上 $-\sum\alpha_i$ 剛好減掉一次，把左右兩端密合接在一起。
- 連續時間不需要這一項（類比的，單點不影響）；離散時 $m$ 是整數 $0,1,2,\dots$，要嚴謹地補上。

【課本補充】p. 507：課本 (11-37) 寫 $S(z)=\sum_i\frac{\alpha_i}{1-z_iz^{-1}}+\sum_i\frac{\alpha_i}{1-z_iz}$，$R[m]=\sum_i\alpha_iz_i^{|m|}$，$\alpha_i=\gamma_iL(1/z_i)$。也可以用卷積定理 $R[m]=l[m]*l[-m]=\sum_{k\ge0}l[|m|+k]l[k]$（式 (11-35)）求。$X[n]$ 滿足遞迴 $X[n]+a_1X[n-1]+\cdots+a_NX[n-N]=b_0I[n]+\cdots+b_MI[n-M]$（式 (11-38)）。

老師的總結【口頭】：類比和數位都講完了。目標是設計 regular process；只能討論多項式——regular process 不一定是多項式，但多項式比較好做系統化分析。就像只做線性系統：線性好控制；非線性可能性質更好，但很難系統化設計。

---

## 7. 一頁速查表

### 定義回顧

- regular = 白雜訊經最小相位（$L$、$1/L$ 都因果穩定）濾波器；只看有限的 pole。
- 預告：WSS = regular + predictable。

### 離散有限階過程

| 項目 | 公式 |
|---|---|
| 濾波器 | $L(z)=\frac{b_0+\cdots+b_Mz^{-M}}{1+a_1z^{-1}+\cdots+a_Nz^{-N}}$，根在單位圓內 |
| 部分分式 | $L=\sum\frac{\gamma_i}{1-z_iz^{-1}}$（$M=N$ 時有 $z_1=0$ 的常數項 $\frac{b_N}{a_N}$） |
| 脈衝響應 | $l[n]=\sum\gamma_iz_i^nU[n]$（用 $\frac1{1-a}=\sum a^k$） |
| 頻譜拆解 | $S=S^+(z)+S^+(1/z)-\sum\alpha_i$，$\alpha_i=\gamma_iL(1/z_i)$ |
| 自相關 | $R[m]=\sum\alpha_iz_i^{\lvert m\rvert}$ |

- 課本少了 $-\sum\alpha_i$：只影響 $m=0$（兩份重複算了 $R^+[0]$）。
- 根越接近原點，衰減越快。

### 連續 vs 離散

| | 連續 | 離散 |
|---|---|---|
| 對稱點 | $s_i\to-s_i$ | $z_i\to1/z_i$ |
| 係數 | $\alpha_i=\gamma_iL(-s_i)$ | $\alpha_i=\gamma_iL(1/z_i)$ |
| 自相關 | $\sum\alpha_ie^{s_i\lvert\tau\rvert}$ | $\sum\alpha_iz_i^{\lvert m\rvert}$ |
| 補常數 | 不需要 | 需要 $-\sum\alpha_i$ |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 離散有限階過程 | 下一集：AR、MA、ARMA，Yule–Walker 方程 |
| regular + predictable 分解 | §11-4（第 28–29 集）Wold 分解 |
| 根的位置決定衰減 | §12-2 參數化頻譜估計 |

---

## 附：本集一句話總結

> **離散有限階過程的濾波器拆成部分分式 $\sum\frac{\gamma_i}{1-z_iz^{-1}}$，脈衝響應就是根的 $n$ 次方 $\sum\gamma_iz_i^n$（根在單位圓內才收斂）；頻譜拆成兩份對稱相加時要補一個常數 $-\sum\alpha_i$（課本漏了，只影響原點），自相關是 $\sum\alpha_iz_i^{|m|}$，係數 $\alpha_i=\gamma_iL(1/z_i)$。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-2 (2/3) 錄影逐字稿（whisper large-v3-turbo，42:49）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
