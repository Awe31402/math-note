---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 11
lecture: Lec 9-2 General Concepts — Systems with Stochastic Inputs (3/3)
date: 待補
video: https://youtu.be/4Ad4Qd_OOms
notes: Papoulis & Pillai 4th ed. §9-2（Fundamental theorem 式 (9-88)–(9-91)、Theorem 9-2 式 (9-92)–(9-95)、Corollary 式 (9-97)、(9-98)，pp. 398–401；Differentiators、Poisson impulses、Differential equations、General moments，式 (9-101)–(9-121)，pp. 402–405）
---

# 第 11 集 · Lec 9-2 (3/3)：時變系統、線性系統的基本定理（平均、互相關、自相關）、微分器、微分方程、三階動差 [▶ 影片](https://youtu.be/4Ad4Qd_OOms)

← 上一集：[10](10-bussgang-linear-systems-convolution-delta.md) ｜ [總目錄](README.md) ｜ 下一集：[12](12-power-spectrum-doppler-transfer-function-hilbert-wiener-khinchin.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 11 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（23:40，whisper large-v3-turbo）＋ Papoulis §9-2（pp. 398–405）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「都卜勒」＝「杜卜勒」（Doppler），「impulse response」→「imput response」，「convolution」→「commolution／comulation」，「convolve」→「combob／convalve」，「調變」→「條變」，「線性」→「線心」，「複數」→「負數」，「weighting」→「waiting」，「SSS」→「SS」，「wide-sense stationary」→「y-sand／wise and stationary」，「complex conjugate」→「compress／complete conjugate」，「Bussgang」→「Baskin」，「Gaussian」→「高丝」，「Riemann integral」→「Reinman Integral」，「時域」→「Title 面」，「頻域」→「斗面」，「Poisson」→「poison／prozone」，「autocorrelation」→「autochrome／autogreen／autocoration function」，「實數」→「時數」，「excitation」→「excitation」。以下一律用正確的字。

> **接上一集**：上一集證明了可微的線性系統就是卷積，係數 $h$ 是系統映射的微分。這一集先看一個時變系統的例子（類似都卜勒效應），然後是 §9-2 最重要的定理：**線性系統輸出的平均、互相關、自相關怎麼由輸入算出來**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 時變系統的例子：類似都卜勒效應](#1-時變系統的例子類似都卜勒效應)
- [2. 記號：為什麼寫 $h(\tau;t)$](#2-記號為什麼寫-htaut)
- [3. 基本定理（Fundamental Theorem + Theorem 9-2）](#3-基本定理fundamental-theorem--theorem-9-2)
  - [3.1 敘述](#31-敘述)
  - [3.2 證明](#32-證明)
  - [3.3 推論：協方差也一樣](#33-推論協方差也一樣)
  - [3.4 不能寫成卷積的線性系統也成立](#34-不能寫成卷積的線性系統也成立)
- [4. 例：微分器](#4-例微分器)
- [5. 例：Poisson 過程經過微分器](#5-例poisson-過程經過微分器)
- [6. 例：微分方程](#6-例微分方程)
- [7. 推廣：三階動差](#7-推廣三階動差)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 時變系統例子、記號 | [▶ 00:00](https://youtu.be/4Ad4Qd_OOms?t=0) | 無（【口頭】） |
| 基本定理 | [▶ 06:11](https://youtu.be/4Ad4Qd_OOms?t=371) | 式 (9-88)–(9-98)，pp. 398–401 |
| 微分器、Poisson 脈衝 | [▶ 16:05](https://youtu.be/4Ad4Qd_OOms?t=965) | 式 (9-101)–(9-110)，pp. 402–404 |
| 微分方程 | [▶ 19:08](https://youtu.be/4Ad4Qd_OOms?t=1148) | 式 (9-111)–(9-118)，pp. 404–405 |
| 三階動差 | [▶ 21:40](https://youtu.be/4Ad4Qd_OOms?t=1300) | 式 (9-119)–(9-121)，p. 405 |

---

## 1. 時變系統的例子：類似都卜勒效應

[▶ 00:00](https://youtu.be/4Ad4Qd_OOms?t=0) 最有名的時變系統是**都卜勒效應** (Doppler effect)：隨時間改變，頻率就會偏移。

**例**：脈衝響應
$$h(\tau;t)=\delta(\tau)\,e^{j\omega_0t}.$$

- $\delta(\tau)$：完全通過（$\tau$ 是卷積的變數）。
- $e^{j\omega_0t}$：隨時間有相位偏移。

輸出（卷積，左邊寫脈衝響應、右邊寫輸入）：
$$Y(t)=\int h(\tau;t)\,X(t-\tau)\,d\tau=\int\delta(\tau)\,e^{j\omega_0t}X(t-\tau)\,d\tau.$$

用 delta 的複製性質（假設 $X$ 連續；不連續點要說 undefined）：代 $\tau=0$，$e^{j\omega_0t}$ 和 $\tau$ 無關直接帶出來：
$$Y(t)=X(t)\,e^{j\omega_0t}.$$

- 就是把輸入乘上**複數載波**，相當於**調變**（從低頻調到高頻），直觀上頻率會偏。
- **線性**：可以驗證符合疊加原理。
- **時變**：把輸入晚 $s$ 送進去，$X(t-s)$ 的輸出是 $X(t-s)e^{j\omega_0t}$，不是 $Y(t-s)=X(t-s)e^{j\omega_0(t-s)}$——相位旋轉的角度不一樣。

---

## 2. 記號：為什麼寫 $h(\tau;t)$

[▶ 02:33](https://youtu.be/4Ad4Qd_OOms?t=153)【口頭】

- 有的書寫 $h(\tau,t)$（逗點）。逗點通常隱含兩個變數**對等**，像 $f(x,y)$。
- 老師用**冒號** $h(\tau;t)$：兩個變數**角色不對等**——對 $\tau$ 積分（卷積），$t$ 代表隨時間的變化。老師說這個記號也不是標準的，沒辦法做更進一步的推廣，但比較合理。
- 時不變時拿掉 $;t$：$Y(t)=\int h(\tau)X(t-\tau)\,d\tau$，也寫成 $h(t)*X(t)$。
- 時不變時數學上可以互換成 $\int X(\tau)h(t-\tau)\,d\tau$，但**觀念上最好不要互換**：
  - $h$ 的角色是**加權** (weighting)，被卷積的是輸入。
  - $h$ 是系統映射 $T$ 的微分（上一集證明的）。
  - 不要把輸入當加權去卷積 $h$。用這個角度，推廣到時變系統比較容易理解。

---

## 3. 基本定理（Fundamental Theorem + Theorem 9-2）

[▶ 06:11](https://youtu.be/4Ad4Qd_OOms?t=371) 課本分成兩個定理（Fundamental theorem 和 Theorem 9-2），老師合在一起看，叫 **Fundamental Theorem**——非常基本而重要。

**動機**：無記憶系統時，輸入 SSS ⇒ 輸出 SSS；但輸入 WSS 時輸出不一定 WSS（平方就是反例）。**要線性**才保持 WSS。這就是為什麼任何領域設計系統都喜歡線性：要維持弱穩態。所以要知道線性系統輸入、輸出之間一階、二階的關係。

### 3.1 敘述

> **基本定理**：對線性系統 $Y(t)=\int h(\tau;t)X(t-\tau)\,d\tau$（$h$ 可以是隨機的，和 $X$ 獨立，或至少不相關）：
>
> 1. **平均**（經過一次濾波）：
> $$\eta_Y(t)=\int E\left[h(\tau;t)\right]\eta_X(t-\tau)\,d\tau.$$
> 2. **互相關**（對 $t_2$ 卷積一次，要共軛）：
> $$R_{XY}(t_1,t_2)=\int E\left[h^*(\tau_2;t_2)\right]R_{XX}(t_1,t_2-\tau_2)\,d\tau_2.$$
> 3. **自相關**（再對 $t_1$ 卷積一次；共兩次）：
> $$R_{YY}(t_1,t_2)=\iint E\left[h(\tau_1;t_1)h^*(\tau_2;t_2)\right]R_{XX}(t_1-\tau_1,t_2-\tau_2)\,d\tau_1d\tau_2.$$

直觀【口頭】：

- 一階：線性，所以就是卷積一次。
- 二階：是二次的，所以輸出要經過**兩次**卷積：先對第二個參數 $t_2$ 卷積（要**共軛**），再對第一個參數 $t_1$ 卷積。
- $h$ 可能是隨機的：系統可能有 **fading**（衰落），隨時間、隨狀況變化，有機率。所以卷積後對 $h$ 取期望值。
- 中間那一步是輸入和輸出的**互相關**：只經過一次卷積。（呼應 Bussgang 定理：高斯 + 無記憶時，互相關和輸入自相關成正比。）
- 因為是 $X$ 對 $Y$（不是 $Y$ 對 $X$），$Y$ 在後面、要共軛，所以對 $t_2$ 卷積。

【課本補充】Papoulis（確定的 LTI 系統）：
- Fundamental theorem（式 (9-88)、(9-89)）：$E\{L[X(t)]\}=L[E\{X(t)\}]$，即 $\eta_Y(t)=L[\eta_X(t)]=\eta_X(t)*h(t)$。
- Theorem 9-2（式 (9-92)–(9-95)）：$R_{XY}(t_1,t_2)=L_2[R_{XX}(t_1,t_2)]$，$R_{YY}(t_1,t_2)=L_1[R_{XY}(t_1,t_2)]$。$L_2$ 表示系統作用在 $t_2$ 上（$t_1$ 當參數），$L_1$ 作用在 $t_1$ 上：
$$R_{XY}(t_1,t_2)=\int R_{XX}(t_1,t_2-\alpha)h(\alpha)\,d\alpha,\qquad R_{YY}(t_1,t_2)=\int R_{XY}(t_1-\alpha,t_2)h(\alpha)\,d\alpha.$$
- 複數情形（式 (9-98)）：$R_{XY}=R_{XX}*h^*(t_2)$，$R_{YY}=R_{XY}*h(t_1)$。
- 課本 Fig. 9-8b：把 $R_{XX}(t_1,t_2)$ 當輸入、系統作用在 $t_2$，輸出是 $R_{XY}$；再把 $R_{XY}$ 當輸入、作用在 $t_1$，輸出是 $R_{YY}$。課本說觀念上先求 $R_{XY}$ 比較好。

### 3.2 證明

[▶ 10:19](https://youtu.be/4Ad4Qd_OOms?t=619) 假設 Riemann 積分，期望值和積分可以互換。

**平均：**
$$\eta_Y(t)=E\left[\int h(\tau;t)X(t-\tau)\,d\tau\right]=\int E\left[h(\tau;t)X(t-\tau)\right]d\tau=\int E[h(\tau;t)]\,\eta_X(t-\tau)\,d\tau.$$
最後一步：通常假設輸入和通道**獨立**（至少不相關），相乘的期望值 = 期望值相乘。

注意：這裡**還沒有**假設輸入平穩，任何輸入都對，是最廣義的關係。

**互相關：**
$$R_{XY}(t_1,t_2)=E\left[X(t_1)Y^*(t_2)\right]=E\left[X(t_1)\int h^*(\tau_2;t_2)X^*(t_2-\tau_2)\,d\tau_2\right]$$
$$=\int E\left[h^*(\tau_2;t_2)\right]E\left[X(t_1)X^*(t_2-\tau_2)\right]d\tau_2=\int E\left[h^*(\tau_2;t_2)\right]R_{XX}(t_1,t_2-\tau_2)\,d\tau_2.$$

**自相關：** 把 $Y(t_1)$、$Y^*(t_2)$ 都寫成卷積，$Y^*$ 帶出 $h^*(\tau_2;t_2)$：
$$R_{YY}(t_1,t_2)=E\left[\int h(\tau_1;t_1)X(t_1-\tau_1)d\tau_1\int h^*(\tau_2;t_2)X^*(t_2-\tau_2)d\tau_2\right]$$
$$=\iint E\left[h(\tau_1;t_1)h^*(\tau_2;t_2)\right]R_{XX}(t_1-\tau_1,t_2-\tau_2)\,d\tau_1d\tau_2.$$ ∎

老師說：證明不難，但要把它變成**直覺**。這個定理不好記，$t_1$、$t_2$ 很容易搞錯；一般喜歡記它在**頻譜上**的版本（之後會講）。理由【口頭】：給你一個輸入、一個加權，請你心算卷積的樣子，很難，老師自己也做不出來；但在頻譜上卷積變成**相乘**，給兩個函數想像相乘的樣子就容易多了。不過要從時域出發。

### 3.3 推論：協方差也一樣

[▶ 14:27](https://youtu.be/4Ad4Qd_OOms?t=867) 扣掉期望值的自協方差、互協方差，有**一模一樣**的性質。

【課本補充】Papoulis Corollary（式 (9-97)）：中心化過程 $\tilde{Y}(t)=Y(t)-\eta_Y(t)=L[\tilde{X}(t)]$（式 (9-91)），所以
$$C_{XY}(t_1,t_2)=C_{XX}(t_1,t_2)*h(t_2),\qquad C_{YY}(t_1,t_2)=C_{XY}(t_1,t_2)*h(t_1).$$

### 3.4 不能寫成卷積的線性系統也成立

[▶ 15:00](https://youtu.be/4Ad4Qd_OOms?t=900)

- 證明用了卷積，但有些線性系統（例如微分器）不能寫成卷積。
- **定理對任何線性系統都對**，只是證明要多做些功夫：輸出的自相關 = 輸入的自相關經過**兩次**濾波；輸出的平均 = 輸入的平均經過**一次**濾波。
- 觀念：例如微分，先把極限拉出來，裡面還是承認 delta 函數的脈衝響應，但不對 delta 取微分；先證定理，最後再討論極限。證明比較 tricky。

【課本補充】課本的證明本來就不用卷積：(9-85) 乘以 $X(t_1)$ 得 $X(t_1)Y(t)=L_t[X(t_1)X(t)]$，取期望值用 (9-88) 得 $E\{X(t_1)Y(t)\}=L_t[R_{XX}(t_1,t)]$，令 $t=t_2$ 即 (9-92)。所以對任何線性算子都成立。

---

## 4. 例：微分器

[▶ 16:05](https://youtu.be/4Ad4Qd_OOms?t=965) $Y(t)=X'(t)$，線性系統。「經過濾波」就是「做微分」：

$$\eta_Y(t)=\eta_X'(t),\qquad R_{XY}(t_1,t_2)=\frac{\partial R_{XX}(t_1,t_2)}{\partial t_2},\qquad R_{YY}(t_1,t_2)=\frac{\partial R_{XY}(t_1,t_2)}{\partial t_1}=\frac{\partial^2R_{XX}(t_1,t_2)}{\partial t_1\partial t_2}.$$

- $X$ 對 $Y$：$Y$ 經過一次濾波，所以對 $t_2$ 微分。
- $Y$ 對 $Y$：經過兩次微分，分別對 $t_1$、$t_2$。
- 協方差也一樣。老師說知道這件事，做微分就變得很直觀。

【課本補充】Papoulis 式 (9-101)–(9-106)，pp. 402–403。若 $X$ 是 WSS：$E\{X'(t)\}=0$，且 $\tau=t_1-t_2$ 時 $\frac{\partial R_{XX}(t_1-t_2)}{\partial t_2}=-R_{XX}'(\tau)$，$\frac{\partial^2R_{XX}(t_1-t_2)}{\partial t_1\partial t_2}=-R_{XX}''(\tau)$，所以
$$R_{XX'}(\tau)=-R_{XX}'(\tau),\qquad R_{X'X'}(\tau)=-R_{XX}''(\tau).$$

---

## 5. 例：Poisson 過程經過微分器

[▶ 17:37](https://youtu.be/4Ad4Qd_OOms?t=1057)

- 輸入 $X(t)$ 是 Poisson 過程：階梯函數，每來一個顧客（arrival）或封包就累積 1。
- 經過微分器，得到原來的 **Poisson 點**：一串脈衝 $Z(t)=\sum_i\delta(t-t_i)$。
- 用基本定理很好算（直接算恐怕比較複雜）：
  - 平均：輸入平均 $\lambda t$，微分一次 → 常數 $\lambda$。
  - 自相關：輸入自相關微分兩次。

老師說「微分兩次事實上又是一個常數」，請大家自己一定要練習。

【課本補充】Papoulis「Poisson impulses」（式 (9-107)–(9-110)，pp. 403–404）的完整結果：輸入 $R_{XX}(t_1,t_2)=\lambda^2t_1t_2+\lambda\min(t_1,t_2)$（第 6 集）。
1. 對 $t_2$ 微分：$R_{XZ}(t_1,t_2)=\lambda^2t_1+\lambda U(t_1-t_2)$（$U$ 是單位階梯函數）。
2. 這個函數在 $t_1=t_2$ 不連續，對 $t_1$ 微分會出現脈衝 $\lambda\delta(t_1-t_2)$：
$$R_{ZZ}(t_1,t_2)=\lambda^2+\lambda\,\delta(t_1-t_2).$$
所以 $Z(t)$ 是平穩的，平均 $\lambda$，自相關 $R_{ZZ}(\tau)=\lambda^2+\lambda\delta(\tau)$——除了常數 $\lambda^2$，還有一個脈衝。

---

## 6. 例：微分方程

[▶ 19:08](https://youtu.be/4Ad4Qd_OOms?t=1148) 比較不常見的推廣。前面是「輸出 = 輸入的微分」；現在倒過來：輸入 $X(t)$ 是**激勵** (excitation)，輸出滿足一個微分方程

$$a_nY^{(n)}(t)+\cdots+a_1Y'(t)+a_0Y(t)=X(t).$$

這是線性系統（可以證明），所以基本定理可以用。

- **平均**：經過一次濾波，把平均代進整個方程式：
$$a_n\eta_Y^{(n)}(t)+\cdots+a_0\eta_Y(t)=\eta_X(t).$$
  解它需要**初始條件**，一般都是 0：出發點 $t=0$ 時值是 0、各階微分也是 0（因為都沒有變化）。有了初始條件就能用微積分解出來。
- **自相關**：基本定理要用**兩次**——第一次對 $t_2$，第二次對 $t_1$；初始條件一樣都是 0。

老師說【口頭】：這個定理很簡單但很重要，幫助快速了解系統輸入、輸出之間的能量關係（一階、二階概念上就是能量的相互影響）。學工程最希望的是產生**工程直覺**：看到一個系統，心中大概知道輸入是這個、輸出會是什麼樣子。

【課本補充】Papoulis 式 (9-111)–(9-118)，pp. 404–405：
$$a_n\frac{\partial^nR_{XY}(t_1,t_2)}{\partial t_2^n}+\cdots+a_0R_{XY}(t_1,t_2)=R_{XX}(t_1,t_2),\quad R_{XY}(t_1,0)=\cdots=\frac{\partial^{n-1}R_{XY}(t_1,0)}{\partial t_2^{n-1}}=0;$$
$$a_n\frac{\partial^nR_{YY}(t_1,t_2)}{\partial t_1^n}+\cdots+a_0R_{YY}(t_1,t_2)=R_{XY}(t_1,t_2),\quad R_{YY}(0,t_2)=\cdots=0.$$

---

## 7. 推廣：三階動差

[▶ 21:40](https://youtu.be/4Ad4Qd_OOms?t=1300) §9-2 的最後一個定理，只是簡單的數學推廣。有些特定應用需要**三階動差**（例如看相位），就想知道輸入和輸出三階動差的關係。為了敘述簡單，假設 $h$ 是實數（複數也容易推廣）。

三階動差：$R_{XXX}(t_1,t_2,t_3)=E[X(t_1)X(t_2)X(t_3)]$。每把一個 $X$ 換成 $Y$，就對那個時間做一次卷積：

$$R_{XXY}(t_1,t_2,t_3)=\int R_{XXX}(t_1,t_2,t_3-\gamma)h(\gamma)\,d\gamma\quad\text{（對 }t_3\text{）}$$
$$R_{XYY}(t_1,t_2,t_3)=\int R_{XXY}(t_1,t_2-\beta,t_3)h(\beta)\,d\beta\quad\text{（對 }t_2\text{）}$$
$$R_{YYY}(t_1,t_2,t_3)=\int R_{XYY}(t_1-\alpha,t_2,t_3)h(\alpha)\,d\alpha\quad\text{（對 }t_1\text{）}$$

$R_{YYY}$ 就是經過**三次**濾波。這是線性系統的好處。舉一反三：好多個濾波器、四階、五階、六階都一樣。

【課本補充】Papoulis 式 (9-119)–(9-121)，p. 405。課本提醒：要算特定 $t_1,t_2,t_3$ 的 $R_{YYY}$，必須知道**所有** $t_1,t_2,t_3$ 的 $R_{XXX}$。

---

## 8. 一頁速查表

### 時變系統例子

$h(\tau;t)=\delta(\tau)e^{j\omega_0t}$ ⇒ $Y(t)=X(t)e^{j\omega_0t}$：線性、時變（調變／都卜勒）。

### 線性系統基本定理

| 量 | 公式 | 次數 |
|---|---|---|
| 平均 | $\eta_Y(t)=\int E[h(\tau;t)]\,\eta_X(t-\tau)\,d\tau$ | 一次 |
| 互相關 | $R_{XY}(t_1,t_2)=\int E[h^*(\tau;t_2)]\,R_{XX}(t_1,t_2-\tau)\,d\tau$ | 對 $t_2$ 一次（共軛） |
| 自相關 | $R_{YY}(t_1,t_2)=\int R_{XY}(t_1-\tau,t_2)\,h(\tau)\,d\tau$（確定 $h$） | 再對 $t_1$ 一次 |

- 關鍵一步：$E[X(t_1)Y^*(t_2)]=\int E[h^*]E[X(t_1)X^*(t_2-\tau)]d\tau$（$h$ 與 $X$ 獨立、期望值與積分互換）。
- 協方差同樣成立（中心化過程經過同一系統）。
- 對任何線性算子都成立：$R_{XY}=L_2[R_{XX}]$，$R_{YY}=L_1[R_{XY}]$。

### 例子

- **微分器**：$R_{XY}=\partial_{t_2}R_{XX}$，$R_{YY}=\partial_{t_1}\partial_{t_2}R_{XX}$；WSS 時 $R_{XX'}=-R_{XX}'$，$R_{X'X'}=-R_{XX}''$。
- **Poisson 脈衝**：$\eta_Z=\lambda$，$R_{ZZ}(\tau)=\lambda^2+\lambda\delta(\tau)$。
- **微分方程**：平均、互相關、自相關各自滿足同一個微分方程（分別對 $t$、$t_2$、$t_1$），初始條件全 0。
- **三階動差**：每把一個 $X$ 換成 $Y$，就對那個時間卷積一次。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 基本定理的頻譜版本 | 下一集起：§9-3 功率頻譜，$S_{XY}=S_{XX}H^*$，$S_{YY}=S_{XX}\lvert H\rvert^2$ |
| WSS 輸入 → WSS 輸出（線性） | §9-3：$R_{YY}(\tau)=R_{XX}(\tau)*h(\tau)*h^*(-\tau)$ |
| 調變 $X(t)e^{j\omega_0t}$ | §10-3 調變（第 16–18 集） |
| 白雜訊輸入（課本 Theorem 9-3） | §9-3、§11 |
| 三階動差 | 課本 §10-7 bispectra（課程沒排） |

---

## 附：本集一句話總結

> **線性系統的輸出：平均是輸入平均經過一次濾波，互相關是輸入自相關對 $t_2$ 經過一次（共軛的）濾波，自相關再對 $t_1$ 經過一次——共兩次；這對任何線性系統都成立，也是「線性系統保持廣義平穩」的根據。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-2 (3/3) 錄影逐字稿（whisper large-v3-turbo，23:40）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
