---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 10
lecture: Lec 9-2 General Concepts — Systems with Stochastic Inputs (2/3)
date: 待補
video: https://youtu.be/aipmve63RRk
notes: Papoulis & Pillai 4th ed. §9-2（Example 9-17 Bussgang's theorem，式 (9-81)–(9-84)，p. 397；Linear Systems，式 (9-85)–(9-87)，pp. 397–398）
---

# 第 10 集 · Lec 9-2 (2/3)：Bussgang 定理、線性系統就是卷積、脈衝響應、Dirac delta 的陷阱 [▶ 影片](https://youtu.be/aipmve63RRk)

← 上一集：[09](09-systems-memoryless-sss-preserved-hard-limiter-arcsine.md) ｜ [總目錄](README.md) ｜ 下一集：[11](11-time-varying-fundamental-theorem-linear-systems.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 10 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（52:11，whisper large-v3-turbo）＋ Papoulis §9-2（pp. 397–398）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【Q&A】` 學生提問
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Bussgang」→「Baskin／Buskin」，「correlation」→「coration／Coreation／Collation」，「arcsine」→「oxide／Axine」，「hard limiter」→「Hot／Hull Limiter」，「memoryless」→「memory system／memorless」（指無記憶），「Gaussian」→「高圈／高丝」，「iterated expectation」→「期望值的迭代法」，「ρ」→「Raw／RAW」，「OFDM」→「OFDN」，「error function」→「R function」，「伏」→「幅」，「可微」→「可為」，「微分」→「為分／唯一分」，「一階可微」→「一接可為」，「affine」→「affine」，「convolution」→「commolution／combolution／CAMLUSH」，「impulse response」→「imput／input／Import response」，「discrete」→「discreet」，「time-varying」→「time-bearing」，「weighting」→「waiting」，「reflection／鏡射」→「近射」，「Dirac」→「Direct」，「replication property」（老師的用詞，即 sifting property，篩選性質），「平行線」→「平均线」，「Lebesgue measure」→「the best major」，「審論文」→「審論文」。以下一律用正確的字。

> **接上一集**：上一集講到無記憶系統和硬限幅器的反正弦定律：輸出的自相關和輸入的自相關**不是線性關係**。這一集先看 Bussgang 的觀察：換成看**輸入和輸出的互相關**，就變成**完全成正比**。然後進入線性系統，說明線性系統（可微時）就是卷積，最後討論 Dirac delta 函數使用上的陷阱。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Bussgang 定理](#1-bussgang-定理)
  - [1.1 敘述](#11-敘述)
  - [1.2 證明（老師的版本）](#12-證明老師的版本)
  - [1.3 推論與意義](#13-推論與意義)
  - [1.4 例：硬限幅器](#14-例硬限幅器)
  - [1.5 例：限幅器（clipper）](#15-例限幅器clipper)
  - [1.6 老師的常數 vs 課本的常數](#16-老師的常數-vs-課本的常數)
- [2. 線性系統](#2-線性系統)
  - [2.1 疊加原理](#21-疊加原理)
  - [2.2 可微的線性映射只有一種形式](#22-可微的線性映射只有一種形式)
  - [2.3 所以線性系統就是卷積](#23-所以線性系統就是卷積)
  - [2.4 脈衝響應、時不變](#24-脈衝響應時不變)
  - [2.5 LTI 系統保持 SSS](#25-lti-系統保持-sss)
  - [2.6 反例：微分器是線性但不是卷積](#26-反例微分器是線性但不是卷積)
- [3. Dirac delta 函數的陷阱](#3-dirac-delta-函數的陷阱)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| Bussgang 定理與證明 | [▶ 00:00](https://youtu.be/aipmve63RRk?t=0) | Example 9-17，式 (9-81)–(9-84)，p. 397 |
| 線性系統 = 卷積 | [▶ 22:09](https://youtu.be/aipmve63RRk?t=1329) | 式 (9-85)–(9-87)，pp. 397–398 |
| 脈衝響應、時不變 | [▶ 34:32](https://youtu.be/aipmve63RRk?t=2072) | p. 398 |
| 微分器、delta 函數 | [▶ 38:36](https://youtu.be/aipmve63RRk?t=2316) | 無（【口頭】） |

---

## 1. Bussgang 定理

### 1.1 敘述

[▶ 00:00](https://youtu.be/aipmve63RRk?t=0) 課本把它列成 Example 9-17，老師認為它是**定理**：結果很廣、告訴我們重要性質。他說：證明也許只有幾行，但第一個提出這個觀點、而且有用，就有它的價值。【口頭】

> **Bussgang 定理**：若輸入 $X(t)$ 是**零平均、平穩的高斯**過程，系統是**無記憶**的 $Y(t)=g(X(t))$，則輸入和輸出的**互相關**和輸入的**自相關**成正比：
> $$R_{XY}(\tau)=K\,R_{XX}(\tau).$$

- 對**任何**無記憶系統都對（包含硬限幅器）。
- 對比：硬限幅器輸出的**自相關** $R_{YY}=\frac2\pi\arcsin\frac{R_{XX}}{R_{XX}(0)}$ 和輸入的自相關不是線性關係（$\rho$ 小時才接近線性）。Bussgang 看的是另一件事——**互相關**，發現它永遠是**完全線性**、過原點的正比。

### 1.2 證明（老師的版本）

[▶ 04:07](https://youtu.be/aipmve63RRk?t=247) 老師的算法和課本有一點不一樣，最後會說明。

記 $X_1=X(t_1)$、$X_2=X(t_2)$。系統映射 $T$ 可以是隨機的。

**Step 1：無記憶。** $Y(t_2)=T(X(t_2))$：
$$R_{XY}(t_1,t_2)=E\left[X_1\,T(X_2)\right].$$

**Step 2：疊代期望值。** 先固定 $X_1=x_1$、$X_2=x_2$，對（可能隨機的）$T$ 取期望值，再對 $(X_1,X_2)$ 取期望值。定義
$$g(x_2)=E\left[T(x_2)\right]$$
（輸入是 $x_2$ 時，輸出的平均值）。於是最裡面那層積分直接拿掉：
$$R_{XY}(t_1,t_2)=E\left[X_1\,g(X_2)\right].$$

**Step 3：先對 $X_1$ 取條件期望值。** $X_1,X_2$ 聯合高斯、零平均、同變異數 $R_{XX}(0)$，相關係數 $\rho=\frac{R_{XX}(t_1-t_2)}{R_{XX}(0)}$。指數部分對 $x_1$ 配方：$x_1^2-2\rho x_1x_2+x_2^2=(x_1-\rho x_2)^2+(1-\rho^2)x_2^2$，馬上看出
$$E[X_1\mid X_2=x_2]=\rho\,x_2.$$
所以
$$E\left[X_1g(X_2)\right]=E\left[E[X_1\mid X_2]\,g(X_2)\right]=\rho\,E\left[X_2\,g(X_2)\right].$$

**Step 4：** $E[X_2g(X_2)]$ 不管是什麼，積出來是一個**常數**（平穩，跟時間無關），記成 $E[Xg(X)]$：
$$R_{XY}(\tau)=\frac{R_{XX}(\tau)}{R_{XX}(0)}\,E\left[X\,g(X)\right]=K\,R_{XX}(\tau),\qquad K=\frac{E\left[Xg(X)\right]}{R_{XX}(0)}.$$ ∎

老師說：知道目的（證明互相關和自相關差一個常數倍）之後，證明不難。

### 1.3 推論與意義

[▶ 10:16](https://youtu.be/aipmve63RRk?t=616)

- **過原點的正比**：若 $R_{XX}(\tau)=0$，則 $R_{XY}(\tau)=0$。
  - 例：輸入是**白**的高斯（$t_1\ne t_2$ 時獨立），則輸入和輸出（不同時間）的互相關一定是 0。
  - 輸入自相關是 0.1，互相關就是 $0.1K$。
- 常數 $K$ 由**系統的映射**決定：$K$ 小，正比線增加得慢；$K$ 大，輸入和輸出的關係就很強。
- 老師的提醒【口頭】：十年後忘了怎麼算沒關係，但要記得：**高斯輸入 + 無記憶系統 ⇒ 輸入輸出的互相關和輸入的自相關成正比**。高斯輸入非常常見，這對系統判斷很有幫助。

老師也提到可以用上一集的抽象符號例子算 $g(1)$、$g(-1)$（講義 p. 73），反正一定算得出來。（逐字稿唸的數字聽不清楚，待補。）

### 1.4 例：硬限幅器

[▶ 12:51](https://youtu.be/aipmve63RRk?t=771) $g(x)=\text{sgn}\,x$（$x>0$ 為 1，$x<0$ 為 $-1$）。

$$E\left[Xg(X)\right]=E\left[X\,\text{sgn}X\right]=E|X|.$$

零平均高斯 $|X|$ 的期望值（常見結果）：$E|X|=\sqrt{\frac{2}{\pi}R_{XX}(0)}$。所以
$$K=\frac{1}{R_{XX}(0)}\sqrt{\frac{2R_{XX}(0)}{\pi}}=\sqrt{\frac{2}{\pi R_{XX}(0)}},\qquad R_{XY}(\tau)=R_{XX}(\tau)\sqrt{\frac{2}{\pi R_{XX}(0)}}.$$

直觀：常數由「輸入」和「平均輸出」相乘的期望值決定，所以跟輸入、輸出都有關，結果合理。

【課本補充】Papoulis 式 (9-83)，p. 397，結果相同。

### 1.5 例：限幅器（clipper）

[▶ 15:57](https://youtu.be/aipmve63RRk?t=957) 通訊上常見，也叫 **clipper**：輸入在 $\pm c$ 之間就保留，太大切成 $c$，太小切成 $-c$。例如 OFDM 系統可能有這種東西，把訊號限制在某個大小內，不要破壞系統。

$$g(x)=\begin{cases}x,&|x|<c\\c,&x>c\\-c,&x<-c\end{cases}$$

它是無記憶的，所以互相關和輸入自相關成正比。算 $K$ 要對高斯積分，結果是 error function 的形式（細節在講義上，上課不講）。

**意義**【口頭】：切的位置 $c$ 影響常數 $K$（正比線的斜率）。要切在 $\pm 2.5$、$\pm 2$ 還是 $\pm 1.5$ V，可以用 $K$ 討論它對相關的影響。

【課本補充】Papoulis 式 (9-84)：$K=\int_{-c}^{c}f(x)\,dx=2G\left(\frac{c}{\sqrt{R_{XX}(0)}}\right)-1$，$G$ 是標準常態 CDF。

### 1.6 老師的常數 vs 課本的常數

[▶ 17:59](https://youtu.be/aipmve63RRk?t=1079)

| | 老師 | Papoulis (9-81) |
|---|---|---|
| $K$ | $\dfrac{E\left[Xg(X)\right]}{R_{XX}(0)}$ | $E\left[g'(X)\right]$ |
| 條件 | 不用可微 | $g$ 要可微 |

- 兩者**相等**，條件是 $g(x)e^{-x^2/(2R_{XX}(0))}\to 0$（$|x|\to\infty$，不會爆掉）。用微積分的基本公式（分部積分）就能證。
- $g$ 不可微時只能用老師的；可微時用課本的（先微分再取期望值）比較快。

以下**不是逐字稿內容**，是依分部積分補的關鍵一步：令 $\sigma^2=R_{XX}(0)$，高斯密度滿足 $f'(x)=-\frac{x}{\sigma^2}f(x)$，所以
$$E[Xg(X)]=\int xg(x)f(x)\,dx=-\sigma^2\int g(x)f'(x)\,dx=-\sigma^2\left[gf\right]_{-\infty}^{\infty}+\sigma^2\int g'(x)f(x)\,dx=\sigma^2E[g'(X)].$$
邊界項為 0 正是上面的條件。

**驗證兩個例子：**

- **硬限幅器**：工程上寫 $g'(x)=2\delta(x)$，所以 $E[g'(X)]=2f(0)=\frac{2}{\sqrt{2\pi R_{XX}(0)}}=\sqrt{\frac{2}{\pi R_{XX}(0)}}$，和 1.4 一樣。
- **限幅器**：$g'(x)=1$（$|x|<c$），$0$（$|x|>c$），所以 $E[g'(X)]=P(|X|<c)$。老師說課本這裡的常數**有點算錯**，照這個 $g'$ 算才對，算出來和他的常數相等。

⚠️ 待確認：以下**不是逐字稿內容**，是依上面的式子推的——$P(|X|<c)=2G\left(c/\sqrt{R_{XX}(0)}\right)-1$，和第 4 版式 (9-84) 一致；用老師的 $K$ 直接積分也得到同一個值。所以第 4 版這裡看起來是對的，老師說的錯誤可能指別的版本或別的式子。

---

## 2. 線性系統

[▶ 22:09](https://youtu.be/aipmve63RRk?t=1329) 為什麼線性重要？上一集說過：**線性（且無記憶）時，輸入 WSS 保證輸出 WSS**。前面講的都是無記憶系統，現在加一個更強的條件：線性。

### 2.1 疊加原理

> **線性系統**：輸入 $A$ 得 $B$、輸入 $C$ 得 $D$，則輸入 $A+C$ 一定得 $B+D$——**疊加原理** (superposition principle)。文字敘述：輸入的**線性組合**（例如 $0.8A+0.2C$）得到的輸出，是原來輸出的**同樣的線性組合**（$0.8B+0.2D$）。

- 線性系統一定過原點。
- 係數（加權）可以是**隨機變數**，還是線性系統。

【課本補充】Papoulis 式 (9-86)：$L[a_1x_1(t)+a_2x_2(t)]=a_1L[x_1(t)]+a_2L[x_2(t)]$；係數可以是隨機變數，因為系統是確定的、只作用在 $t$ 上。

### 2.2 可微的線性映射只有一種形式

[▶ 26:17](https://youtu.be/aipmve63RRk?t=1577) 線性系統和**卷積** (convolution) 幾乎等價，但**不完全**——有的線性系統不能用卷積表示。【Q&A】有同學問到這件事（例如微分器），老師先提關鍵條件：**一階可微** (first-order differentiable)。

> **引理**：若 $f:\mathbb{R}^n\to\mathbb{R}$ **線性**（$f(\mathbf{x}+\mathbf{u})=f(\mathbf{x})+f(\mathbf{u})$）**且可微**，則
> $$f(\mathbf{x})=\sum_{i=1}^{n}\frac{\partial f}{\partial x_i}(\mathbf{0})\,x_i.$$
> 沒有例外。例：$f(x,y,z)$ 線性又可微，只能是 $ax+by+cz$。

**證明：**

**Step 1：微分的定義。** 可微，所以左右導數相等；取一邊就好：
$$\frac{\partial f}{\partial x_i}(\mathbf{x})=\lim_{\Delta\to 0}\frac{f(\mathbf{x}+\Delta\mathbf{e}_i)-f(\mathbf{x})}{\Delta}.$$

**Step 2：用線性拆開。** $f(\mathbf{x}+\Delta\mathbf{e}_i)=f(\mathbf{x})+f(\Delta\mathbf{e}_i)$，$f(\mathbf{x})$ 消掉：
$$\frac{\partial f}{\partial x_i}(\mathbf{x})=\lim_{\Delta\to 0}\frac{f(\Delta\mathbf{e}_i)}{\Delta}.$$

**Step 3：** 右邊跟 $\mathbf{x}$ 在哪裡**完全無關**（只代 $0,\dots,0,\Delta,0,\dots$），而且因為可微一定存在。所以每個偏導數都是**常數** $a_i$，$f$ 對每個 $x_i$ 都是一次的（affine）：
$$f(\mathbf{x})=\sum_i a_ix_i+c.$$
（常數 $c$ 對 $x_i$ 的微分是 0，不影響上面的論證。）

**Step 4：線性一定過原點。** $f(\mathbf{0})=f(\mathbf{0}+\mathbf{0})=f(\mathbf{0})+f(\mathbf{0})$，即 $c=c+c$，所以 $c=0$。

而 $a_i=\frac{\partial f}{\partial x_i}(\mathbf{0})$。 ∎

### 2.3 所以線性系統就是卷積

[▶ 31:29](https://youtu.be/aipmve63RRk?t=1889) 把引理用在系統上：輸出 $Y(t)$ 是輸入 $X(t),X(t-1),X(t-2),\dots$ 的函數。系統線性、映射可微，則
$$Y(t)=\sum_{n}h(n;t)\,X(t-n),\qquad h(n;t)=\frac{\partial T_t}{\partial x(t-n)}(\mathbf{0}).$$

這就是**卷積**。新的理解【口頭】：

- **卷積的係數就是系統映射 $T$ 的微分**（對每個維度）。過去學線性系統直接介紹卷積，現在多一層意義。
- 記號 $h(n;t)$ 裡的「$;t$」：允許**時變** (time-varying)。映射隨時間變，微分當然也變。線性系統可以時變，也不一定要無記憶。
- 映射 $T$ 是隨機的，微分 $h$ 就是隨機的。
- 連續時間就是連續的卷積積分。
- 一般假設 $h$ 和 $X$ 獨立（工程上合理）；相依也允許，線性不要求獨立。

### 2.4 脈衝響應、時不變

[▶ 34:32](https://youtu.be/aipmve63RRk?t=2072) 有了這些微分係數，輸出就可以用卷積算出來：
$$Y(t)=\int h(\tau;t)\,X(t-\tau)\,d\tau.$$

**為什麼叫 convolution？** $X(t-\tau)$ 看 $t=0$ 時就是 $X(-\tau)$，是 $X(\tau)$ 對 $y$ 軸做 180° 翻轉（左右鏡射）。convolve 有「捲、轉」的意思。

> **脈衝響應** (impulse response)：輸入送一個脈衝 $\delta$，輸出觀察到的「反應」(response) 就是 $h$。

理由：delta 乘任何函數再積分，就得到那個函數值（取 $\tau=t-s$ 代入）。所以想知道係數，就輸入一個脈衝去**量測**。

> **時不變** (time-invariant)：映射不隨時間改變 → 微分不隨時間改變 → $h$ 沒有「$;t$」：
> $$Y(t)=\int_{-\infty}^{\infty}h(\tau)\,X(t-\tau)\,d\tau.$$
> **線性時不變** (LTI) 系統就是卷積。

【課本補充】Papoulis p. 398：時不變 = 對 $X(t+c)$ 的響應是 $Y(t+c)$；書中所有線性系統都假設時不變。$Y(t)=X(t)*h(t)=\int X(t-\alpha)h(\alpha)\,d\alpha$（式 (9-87)），$h(t)=L[\delta(t)]$。另外：常態過程經過線性系統仍是常態（把積分近似成和，就是常態隨機變數的線性組合）。

### 2.5 LTI 系統保持 SSS

[▶ 38:05](https://youtu.be/aipmve63RRk?t=2285)

> **引理**：若系統是 LTI，輸入 SSS ⇒ 輸出 SSS。

老師說這不需要再證，因為已經證過無記憶系統的情形，「包含了線性時不變」。

⚠️ 待確認：以下**不是逐字稿內容**，是依課本 p. 398 補的——一般的 LTI 系統（卷積）是**有記憶**的，不屬於上一集證明的無記憶系統，所以不能直接套用。課本的理由是**時不變性**：$Y(t+c)=L[X(t+c)]$ 對每個 $c$ 成立；$X(t)$ 和 $X(t+c)$ 統計相同，經過同一個系統 $L$ 得到的 $Y(t)$ 和 $Y(t+c)$ 統計也相同。老師的意思可能是「同樣的證明想法（同一個映射、不隨時間變）」適用。

### 2.6 反例：微分器是線性但不是卷積

[▶ 38:36](https://youtu.be/aipmve63RRk?t=2316) 卷積有限制，不代表所有線性系統。只要舉一個映射 $T$ **不可微**的例子。

**微分器**：$Y(t)=X'(t)$。

- **是線性**：兩個函數微分的和 = 和的微分。
- **不能寫成卷積**：沒有脈衝響應。送一個 $\delta$ 進去，輸出應該是 $\delta'$，但 **delta 的微分沒有定義**（目前沒有辦法定義；脈衝微分還是脈衝也說不通）。

---

## 3. Dirac delta 函數的陷阱

[▶ 40:08](https://youtu.be/aipmve63RRk?t=2408) 既然脈衝響應要用 delta，就討論為什麼 delta 不能微分。

**定義**：Dirac 在做物理思考時引進的理論工具。
- $\delta(t)$ 在 $t=0$ 是無限大，$t\ne 0$ 是 0。（例：$\delta(x-3)$ 在 3 有一個脈衝，圖上畫「高度 1」，其實高度是無限大，只是指標。）
- 總積分是 1。

這些都是**定義**，不是公設。（公設是大家都承認的，例如「兩條平行線不相交」。）有人不喜歡這種函數；見仁見智，能證明在你的領域有用就好。【口頭】

> **唯一能用的性質**（老師叫 replication property，複製性質；一般叫 sifting property）：
> $$\int_{-\infty}^{\infty}g(t)\,\delta(t-\tau)\,dt=g(\tau),$$
> **只在 $g$ 於 $\tau$ 連續時成立**。在不連續點，結果**沒有定義** (undefined)。

**怪事一：$\delta(t)$ 和 $2\delta(t)$** [▶ 43:11](https://youtu.be/aipmve63RRk?t=2591)

- 逐點看：$t=0$ 時左邊無限大、右邊 2 × 無限大；$t\ne 0$ 時都是 0。如果認為「無限大 = 無限大」，兩個函數處處相等。
- 但用複製性質（$g\equiv 1$、$g\equiv 2$ 都連續）：$\int\delta(t)\,dt=1$，$\int 2\delta(t)\,dt=2$，積分不一樣。
- 高等微積分說：兩個函數除了測度為 0 的點以外都相等，積分一定相等。delta 違反了這件事。

**問題出在「無限大 = 無限大」**【口頭】：

- 老師認為數學上無限大不是數值，不能說無限大等於無限大，否則常得到錯誤結論。
- 例：證明裡有 $x+a=y+a$，消掉 $a$ 得 $x=y$；結果 $x=3$、$y=2$。因為 $a$ 剛好是無限大，$x+\infty=y+\infty$ 不代表 $x=y$。
- 審論文時看到整個推導都很合理、結論卻是錯的，常常就是某個變數跑到無限大（例如除以 0），又把無限大當成相等。推導時要避免任何量衝到無限大。

**結論**：delta 函數**透過積分才有意義**（老師說這是他個人的觀點），將來的用途一定是和某個函數積分。所以**不能再對它微分**，也就沒有微分器的脈衝響應。它在工程上非常有用，因為卷積本身是積分，脈衝響應要用 delta，帶進去運算很方便。

**怪事二：delta 的積分** [▶ 48:55](https://youtu.be/aipmve63RRk?t=2935)

$$\int_{-\infty}^{x}2\delta(\tau)\,d\tau=\int_{-\infty}^{\infty}2\delta(\tau)\,\mathbf{1}[\tau<x]\,d\tau.$$

- 指示函數 $2\cdot\mathbf{1}[\tau<x]$ 在 $\tau<x$ 是 2、$\tau\ge x$ 是 0，在 $\tau=x$ 有一個不連續點。
- 用複製性質代 $\tau=0$：$x>0$ 時是 2，$x<0$ 時是 0。這就是硬限幅器 $\text{sgn}\,x$ 加 1（拉高成 2 和 0），的確對。
- **但 $x=0$ 那一點不對**：不連續點不能下任何結論，要說 undefined 或 indeterminate 才嚴謹。
- 所以不要把不連續點和 delta 的積分直接給一個值。例如「函數微分的積分 = 自己加常數」這種看似合理的推論，碰到 delta 會產生問題。

---

## 4. 一頁速查表

### Bussgang 定理（零平均平穩高斯輸入、無記憶系統 $g$）

$$R_{XY}(\tau)=K\,R_{XX}(\tau),\qquad K=\frac{E[Xg(X)]}{R_{XX}(0)}=E[g'(X)]$$

- 關鍵一步：$E[X_1\mid X_2]=\rho X_2$ → $E[X_1g(X_2)]=\rho\,E[X_2g(X_2)]$。
- 兩種 $K$ 相等：分部積分，$f'(x)=-\frac{x}{\sigma^2}f(x)$，要求 $g(x)e^{-x^2/2\sigma^2}\to 0$。
- 硬限幅器：$K=\sqrt{\frac{2}{\pi R_{XX}(0)}}$（$E|X|=\sqrt{2R_{XX}(0)/\pi}$）。
- 限幅器 $\pm c$：$K=P(|X|<c)=2G\left(c/\sqrt{R_{XX}(0)}\right)-1$。
- $R_{XX}(\tau)=0\Rightarrow R_{XY}(\tau)=0$。

### 線性系統

- 疊加原理；係數可隨機；過原點。
- **可微線性映射** $f(\mathbf{x})=\sum_i\frac{\partial f}{\partial x_i}(\mathbf{0})x_i$。關鍵：$\partial_if(\mathbf{x})=\lim f(\Delta\mathbf{e}_i)/\Delta$ 與 $\mathbf{x}$ 無關；$f(\mathbf{0})=2f(\mathbf{0})\Rightarrow c=0$。
- 卷積係數 = 映射的微分：$Y(t)=\sum_nh(n;t)X(t-n)$；LTI：$Y(t)=\int h(\tau)X(t-\tau)d\tau$，$h=L[\delta]$。
- LTI：SSS 進 → SSS 出（時不變）；常態進 → 常態出。
- 微分器線性但非卷積（$\delta'$ 無定義）。

### Dirac delta

- 唯一性質：$\int g(t)\delta(t-\tau)dt=g(\tau)$，**只在 $g$ 連續點**。
- $\delta$ 與 $2\delta$ 逐點「相等」但積分不同 → 不要寫「$\infty=\infty$」。
- 只透過積分有意義；不能微分。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| LTI 系統、卷積 | 下一集：線性系統輸出的平均、互相關、自相關（Fundamental theorem，式 (9-88)–(9-93)） |
| 互相關 $R_{XY}$ | $R_{XY}=R_{XX}*h^*(-\tau)$、$R_{YY}=R_{XY}*h(\tau)$ |
| 脈衝響應、delta | §9-3 功率頻譜：$S_{YY}=S_{XX}\lvert H\rvert^2$ |
| 微分器 | 課本附錄 9A：均方微分 |

---

## 附：本集一句話總結

> **高斯輸入經過任何無記憶系統，輸入輸出的互相關都和輸入自相關成正比（Bussgang，$K=E[Xg(X)]/R_{XX}(0)$）；線性系統只要可微就一定是卷積，卷積係數就是系統映射的微分，但微分器這種不可微的線性系統沒有脈衝響應，因為 delta 函數只透過積分才有意義。**

---

## ⚠️ 待確認清單

1. [▶ 20:37](https://youtu.be/aipmve63RRk?t=1237) 老師說課本限幅器的常數 (9-84)「有點算錯」；依計算第 4 版 (9-84) 與老師的常數一致，老師指的錯誤待確認。
2. [▶ 38:05](https://youtu.be/aipmve63RRk?t=2285) 老師說「LTI 保持 SSS」因為已證過無記憶系統的情形；一般 LTI 系統有記憶，課本用時不變性證明。老師的原意待確認。
3. [▶ 11:49](https://youtu.be/aipmve63RRk?t=709) 用上一集抽象符號例子算 $g(1)$、$g(-1)$ 的數值，逐字稿聽不清楚。
4. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-2 (2/3) 錄影逐字稿（whisper large-v3-turbo，52:11）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
