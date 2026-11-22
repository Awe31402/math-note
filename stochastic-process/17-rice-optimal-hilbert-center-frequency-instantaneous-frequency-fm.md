---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 17
lecture: Lec 10-3 Random Walks and Other Applications — Modulation (2/3)
date: 待補
video: https://youtu.be/a4qBf-61V7E
notes: Papoulis & Pillai 4th ed. §10-3（Hilbert transforms、Rice's representation 式 (10-142)–(10-147)，pp. 466–467；Optimum envelope、Rice's representation theorem 式 (10-148)–(10-150)，pp. 468–469；Instantaneous frequency 式 (10-151)–(10-154)，p. 469）
---

# 第 17 集 · Lec 10-3 (2/3)：Rice 表示法的最佳解就是 Hilbert 轉換、最佳載波是頻譜重心、瞬時頻率、FM 訊號何時 WSS [▶ 影片](https://youtu.be/a4qBf-61V7E)

← 上一集：[16](16-modulation-baseband-passband-rice-representation.md) ｜ [總目錄](README.md) ｜ 下一集：[18](18-woodward-theorem-fm-spectrum-gaussian-process-definitions.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 17 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（56:41，whisper large-v3-turbo）＋ Papoulis §10-3（pp. 466–469）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Hilbert transform」→「Huber／Hilberton Form」，「Rice」→「RISE／Rise」，「穩態」→「穩泰／稳太」，「wide-sense stationary」→「wise and／Y3／Wisen stationary」，「zero mean」→「geo mean／0min」，「複數」→「負數」，「實部／虛部」→「十步／實步／虛步」，「實數」→「時數」，「時域」→「Title 面／tine domain／tidal 面」，「all-pass」→「all pass」，「phase modulation」→「face modulation」，「amplitude modulation」→「amperature modulation」，「in-phase」→「inphase」，「quasi-monochromatic」→「Criside Monochromatic」，「instantaneous frequency」→「Instantaneous Frequency」，「奇對稱」→「G 對稱」，「偶對稱」→「偶對稱」，「complex conjugate」→「compress／complete conjugate」，「相位」→「向位」，「Fourier」→「負率的」，「convolution」→「commolution／Commolution」，「Theorem 9-2」→「定理92」，「time-variant」→「Time Variant」。以下一律用正確的字。

> **接上一集**：上一集的目標是找一個 $Y$，讓 $X,Y$ 能量平衡（$R_{XX}=R_{YY}$、$R_{XY}=-R_{YX}$），整個系統鎖在穩態。Rice 用線性濾波器 $Y=h*X$ 來造，得到兩個條件：**全通** ($|H|^2=1$)，以及 $H^*=-H$。這樣的 $Y$ 不唯一（只限制了一、二階動差，三、四階完全沒限制）。這一集加上第三個條件，推出 $H$ 的形式，再用「解調回基頻後變化最小」的準則，證明**最佳的就是 Hilbert 轉換**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 第三個條件：$H(-\omega)=-H(\omega)$](#1-第三個條件h-omega-homega)
- [2. 三個條件推出 $H(\omega)=\pm j$](#2-三個條件推出-homegapm-j)
- [3. Rice 的最佳準則：基頻變化最小](#3-rice-的最佳準則基頻變化最小)
  - [3.1 給定 $Y$：最佳載波是頻譜重心](#31-給定-y最佳載波是頻譜重心)
  - [3.2 選 $Y$：讓重心越大越好 ⇒ Hilbert 轉換](#32-選-y讓重心越大越好--hilbert-轉換)
  - [3.3 結論](#33-結論)
- [4. 瞬時頻率：最佳載波的時域解釋](#4-瞬時頻率最佳載波的時域解釋)
- [5. FM 訊號何時 WSS](#5-fm-訊號何時-wss)
- [6. Theorem 9-2 的限制](#6-theorem-9-2-的限制)
- [7. FM 的數學細節：積分要存在](#7-fm-的數學細節積分要存在)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 第三個條件、$H$ 的形式 | [▶ 00:00](https://youtu.be/a4qBf-61V7E?t=0) | 無（老師的推導） |
| 最佳載波、Hilbert 最佳 | [▶ 09:20](https://youtu.be/a4qBf-61V7E?t=560) | 式 (10-148)–(10-150)，pp. 468–469 |
| 瞬時頻率 | [▶ 31:21](https://youtu.be/a4qBf-61V7E?t=1881) | 式 (10-151)–(10-154)，p. 469 |
| FM 訊號 | [▶ 42:36](https://youtu.be/a4qBf-61V7E?t=2556) | §10-3 後段 |
| Theorem 9-2 的限制 | [▶ 48:15](https://youtu.be/a4qBf-61V7E?t=2895) | 無（【口頭】） |

老師說【口頭】：數位通訊直接介紹 Hilbert 轉換，不會介紹它的思維過程；這部分很重要，一定要了解、要會。

---

## 1. 第三個條件：$H(-\omega)=-H(\omega)$

[▶ 02:05](https://youtu.be/a4qBf-61V7E?t=125) 這是**方便性**的條件：推導過程中有它，可以更快得到 $H$ 的形式。

從 $R_{XY}$ 和 $R_{YX}$ 的關係：
$$R_{XY}(-\tau)=E\left[X(t-\tau)Y^*(t)\right]=\left(E\left[Y(t)X^*(t-\tau)\right]\right)^*=R_{YX}^*(\tau).$$
（期望值可以任意對調，對調後差一個共軛。）再加上穩態條件 $R_{YX}=-R_{XY}$，以及 $X,Y$ 都是實數過程，得到 $R_{XY}$ 是**奇函數**，所以 $S_{XY}$ 也是奇函數。代入 $S_{XY}=S_{XX}H^*$（$S_{XX}$ 是偶函數）：

> **條件 3**：$H(-\omega)=-H(\omega)$。

（以下補充，**不是逐字稿內容**：也可以這樣看——$h$ 是實數濾波器所以 $H(-\omega)=H^*(\omega)$，再加上條件 2 $H^*=-H$，就得到條件 3。）

---

## 2. 三個條件推出 $H(\omega)=\pm j$

[▶ 04:38](https://youtu.be/a4qBf-61V7E?t=278) 現在有三個條件：

1. $|H(\omega)|^2=1$（全通）
2. $H^*(\omega)=-H(\omega)$
3. $H(-\omega)=-H(\omega)$

**Step 1（條件 1）**：一個複數取絕對值是它到原點的距離。$|H|=1$ 代表 $H$ 在複數平面的**單位圓**上，只有角度能變：
$$H(\omega)=e^{j\varphi(\omega)}.$$

**Step 2（條件 2）**：$e^{j\varphi}=-e^{-j\varphi}$，即 $e^{j2\varphi(\omega)}=-1$。$-1$ 的角度是 $\pi$（加 $2\pi$ 的整數倍）：
$$2\varphi(\omega)=\pi+2\pi k\ \Rightarrow\ \varphi(\omega)=\left(k(\omega)+\tfrac12\right)\pi.$$
角度加 $2\pi$ 在複數平面是同一點，所以限制 $k(\omega)\in\{0,1\}$：
$$H(\omega)=e^{j(k+\frac12)\pi}=j\,(-1)^{k(\omega)},\quad\text{也就是 }H(\omega)=\pm j.$$

**Step 3（條件 3）**：$j(-1)^{k(-\omega)}=-j(-1)^{k(\omega)}$，所以
$$k(-\omega)\ne k(\omega):\ \text{一邊是 0，對應的另一邊一定是 1}.$$

例：設計 $k(\omega)$，右邊某段是 1，左邊對應的地方一定是 0；右邊某段是 0，左邊對應一定是 1。**這樣的設計一定穩態**。但什麼樣的設計最好？

---

## 3. Rice 的最佳準則：基頻變化最小

[▶ 09:20](https://youtu.be/a4qBf-61V7E?t=560) 回顧記號：$W=A+jB$ 是基頻；$Z=X+jY=We^{j\omega_0t}$ 是射頻；$X$ 是天線真正收到的實數訊號（已知，所以 $S_{XX}$ 已知）；$Y$ 是接收端輔助產生的。

> **Rice 的準則**：希望解回基頻的訊號 $W$，它的**微分**在均方意義下最小：
> $$\min\ E\left|W'(t)\right|^2.$$

- 微分代表對時間的**波動**。從射頻解回基頻時，希望對時間不要震盪得太厲害。
- $W$ 是隨機的，所以看均方（先平方再取期望值）。
- 這樣不只 WSS，時域上的觀察也最穩定。Rice 宣稱：只有一個可能，就是 **Hilbert 轉換**。

### 3.1 給定 $Y$：最佳載波是頻譜重心

[▶ 11:51](https://youtu.be/a4qBf-61V7E?t=711)

老師說【口頭】：學過這門課，**一看到微分就想到它是一個線性濾波器**（$X\to X'$ 是一個系統），輸入輸出的關係由 Theorem 9-2、基本定理完全知道；**一看到均方，就想到要回到自相關、回到功率頻譜**。兩個串起來，任何類似的狀況都會處理，不是只會處理課本有的。

**Step 1：** 微分器 $H=j\omega$，輸出頻譜 = 輸入頻譜 × $\omega^2$：$S_{W'W'}(\omega)=\omega^2S_{WW}(\omega)$。

**Step 2：** 均方 = 自相關在 0 = 功率頻譜總積分（反轉換代 $\tau=0$，$e^{j\omega\cdot0}=1$）：
$$M=2\pi E|W'(t)|^2=\int_{-\infty}^{\infty}\omega^2S_{WW}(\omega)\,d\omega.$$

**Step 3：** $W$、$Z$ 差一個複數載波，頻譜差一個平移 $S_{WW}(\omega)=S_{ZZ}(\omega+\omega_0)$。換到 $Z$（因為 $Z$ 和已知的 $X$ 比較有直接關係）：
$$M=\int_{-\infty}^{\infty}(\omega-\omega_0)^2S_{ZZ}(\omega)\,d\omega\qquad\text{(10-148)}.$$

（接收端的 $\omega_0$ 不一定要和傳送端一樣：傳送端 1.8 GHz，可以用 1.7 GHz 解，解出來還是穩態的。現在要找最好的 $\omega_0$。）

**Step 4：給定 $S_{ZZ}$（也就是給定 $Y$），對 $\omega_0$ 最小化。** 這個形式很熟：對 $\omega_0$ 偏微分設為 0，最好的 $\omega_0$ 就是**重心** (center of gravity)：
$$\bar{\omega}_0=\frac{\int\omega\,S_{ZZ}(\omega)\,d\omega}{\int S_{ZZ}(\omega)\,d\omega}.$$

### 3.2 選 $Y$：讓重心越大越好 ⇒ Hilbert 轉換

[▶ 18:00](https://youtu.be/a4qBf-61V7E?t=1080) 但 $S_{ZZ}$ 還依賴 $Y$，要把 $M$ 轉成只跟已知的 $S_{XX}$ 有關。

**Step 5：** 代入 $\bar{\omega}_0$，展開：
$$M=\int\left(\omega^2-\bar{\omega}_0^2\right)S_{ZZ}(\omega)\,d\omega.$$
把 $\omega\to-\omega$ 再積一次一樣，所以取平均 $\frac12[S_{ZZ}(\omega)+S_{ZZ}(-\omega)]$；由上一集 Observation 4，$S_{ZZ}(\omega)+S_{ZZ}(-\omega)=4S_{XX}(\omega)$（$X$ 實數，頻譜對稱）：
$$M=2\int\left(\omega^2-\bar{\omega}_0^2\right)S_{XX}(\omega)\,d\omega\qquad\text{(10-150)}.$$
$S_{XX}$ 已知，第一項、$\int S_{XX}$ 都是常數，**只剩 $\bar{\omega}_0$ 會變**。

> **重要結論 1**：要讓解回基頻後變化最小，**載波 $\bar\omega_0$ 要盡量大**（在保持 WSS 的所有可能中）。

老師說【口頭】：傳送端 1.8 GHz 送來，也許用 1.9 GHz 解，回到基頻的變動最小、最穩。這是 Rice 的思考模式。忘了證明沒關係，要記得這個概念。

**圖像** [▶ 21:04](https://youtu.be/a4qBf-61V7E?t=1264)：以前直觀上，收到的頻譜左右對稱，就取中間當載波。但能量不平衡時（右邊重、左邊輕），要做**重心**：把 $\omega_0$ 往右挪。實作上不一定會這樣，偏一邊就會產生微分意義下的不穩。

**Step 6：算重心。** $S_{ZZ}=2S_{XX}-2jS_{XY}$（Observation 3）。$S_{XX}$ 是偶函數，乘 $\omega$ 積分為 0（左右對消）；$S_{XY}$ 是奇函數，乘 $\omega$ 後左右一樣，積一半乘 2：
$$\int\omega\,S_{ZZ}\,d\omega=-2j\int\omega\,S_{XY}\,d\omega=4\int_0^\infty\omega\left(-jS_{XY}(\omega)\right)d\omega,\qquad\int S_{ZZ}\,d\omega=4\int_0^\infty S_{XX}\,d\omega.$$

**Step 7：代入濾波器。** Theorem 9-2：$S_{XY}=S_{XX}H^*$。$H=j(-1)^k$，$H^*=-j(-1)^k$：
$$-jS_{XY}=-j\cdot S_{XX}\cdot(-j)(-1)^{k}=(-1)^{k+1}S_{XX}.$$
所以
$$\bar{\omega}_0=\frac{\int_0^\infty\omega\,(-1)^{k(\omega)+1}S_{XX}(\omega)\,d\omega}{\int_0^\infty S_{XX}(\omega)\,d\omega}.$$

**Step 8：最大化。** $\omega>0$、$S_{XX}\ge0$ 都固定，要積分最大，$(-1)^{k+1}$ 在 $\omega>0$ 最好**通通是 $+1$**（有負的就會抵消掉）：$k(\omega)=1$，$H(\omega)=-j$（$\omega>0$）。由條件 3，$\omega<0$ 時 $k=0$，$H=j$。這正是
$$H(\omega)=-j\,\text{sgn}\,\omega\quad\text{（Hilbert 轉換）}.$$ ∎

### 3.3 結論

> **定理（Rice）**：Rice 表示法 $X=A\cos\omega_0t-B\sin\omega_0t$ 在「$E|W'|^2$ 最小」的意義下最佳時，$Y=\hat{X}$（Hilbert 轉換），最佳載波是 $S_{XX}$ **右半邊的重心**：
> $$\bar{\omega}_0=\frac{\int_0^\infty\omega\,S_{XX}(\omega)\,d\omega}{\int_0^\infty S_{XX}(\omega)\,d\omega}.$$

- 非常漂亮的定理：Hilbert 轉換除了操作上的意義，還有**理論意義**。
- 最佳載波直接從已知的 $S_{XX}$ 算，不用借助 $Z$。$X$ 頻譜左右對稱，左邊不看，做右邊的**能量重心**。
- 解釋現象：如果刻意把載波放偏，解調回基頻時有比較高的機率震盪得比較嚴重。
- 圖：Hilbert 轉換把左半邊整個消掉（$1+\text{sgn}\,\omega$），$Z$ 只剩右半邊、高度拉高 4 倍；以重心為載波移回基頻，左右能量平衡，所以變異最小（均方意義）。

【課本補充】p. 469 Theorem（Rice's representation）：課本寫 $\bar\omega_0=\frac{\int\omega S_{ZZ}}{\int S_{ZZ}}=\frac{\int_0^\infty\omega B_{XY}(\omega)d\omega}{\int_0^\infty S_{XX}(\omega)d\omega}$，$B_{XY}=-jS_{XY}$，且 $|B_{XY}|\le S_{XX}$；最大化發生在 $|B_{XY}(\omega)|=S_{XX}(\omega)$，得 $-jS_{XY}=S_{XX}\text{sgn}\,\omega$、$S_{ZZ}=4S_{XX}U(\omega)$。課本 (10-144)：$X(t)=i(t)\cos\omega_0t-q(t)\sin\omega_0t$，$i$ 叫**同相分量** (inphase)、$q$ 叫**正交分量** (quadrature)，它們不只依賴 $X$，也依賴 $\omega_0$ 的選擇。

【課本補充】**帶通過程** (bandpass，p. 467)：$S_{XX}$ 在 $(\omega_1,\omega_2)$ 外為 0；頻寬遠小於中心頻率叫**窄頻**（narrowband，或 quasi-monochromatic）；$S_{XX}$ 是脈衝叫**單色** (monochromatic)，例如 $a\cos\omega_0t+b\sin\omega_0t$。課本 Fig. 10-16：$\omega_1+\omega_c\le2\omega_0$ 時，$i$、$q$ 可用乘 $2\cos\omega_0t$、$-2\sin\omega_0t$ 再經理想低通濾波器得到。

---

## 4. 瞬時頻率：最佳載波的時域解釋

[▶ 31:21](https://youtu.be/a4qBf-61V7E?t=1881) 調變有兩大類：**相位調變**（廣義，包含 FM 頻率調變和狹義的純相位 PM）和**振幅調變** (AM)。從 FM／PM 的角度看：

- 基頻 $W=A+jB=r\,e^{j\varphi}$（極座標，半徑 $r$、角度 $\varphi$）。
- 射頻 $X=\text{Re}[We^{j\omega_0t}]=A\cos\omega_0t-B\sin\omega_0t=r\cos(\omega_0t+\varphi)$。
- $A$ 叫 in-phase（同相），$B$ 在複數平面差 90°，叫 quadrature（正交）。用 $\cos$ 送 $A$、$\sin$ 送 $B$，兩者正交，加在一起完全不互相干擾。

> **瞬時頻率** (instantaneous frequency)：**頻率是相位的微分**。
> $$\omega_i(t)=\frac{d}{dt}\left[\omega_0t+\varphi(t)\right]=\omega_0+\varphi'(t)\qquad\text{(10-151)}.$$

- 用 $\varphi$ 傳資訊，當下的頻率有時比 $\omega_0$ 高、有時低，有一個分布。
- 第 12 集的引理：$\omega_i$ 的 **PDF 就是功率頻譜**。兩個概念串起來。

**名詞**：bandpass（只在一個頻帶有值）、narrowband（頻帶遠小於載波）、quasi-monochromatic（接近單頻）、monochromatic（單頻，頻譜是單一脈衝）。

> **最佳載波 = 瞬時頻率的能量加權平均**：
> $$\bar{\omega}_0=\frac{E\{r^2\omega_i\}}{E\{r^2\}}.$$
> （$r^2$ 是能量——複數平面上到原點距離的平方。）

**證明** [▶ 36:01](https://youtu.be/a4qBf-61V7E?t=2161)：

**Step 1：** $Z$ 只有右半邊（Hilbert），重心
$$\bar{\omega}_0=\frac{\int\omega S_{ZZ}\,d\omega}{\int S_{ZZ}\,d\omega}.$$
分子乘 $\frac{1}{2\pi}$ 轉到時域，並寫成 $-j\cdot(j\omega)$：$j\omega S_{ZZ}$ 就是 $Z$ 經過微分器後的互頻譜，所以分子 $\propto E\{Z'(t)Z^*(t)\}$、分母 $\propto E\{|Z|^2\}=E\{r^2\}$。（又是 Theorem 9-2：看到微分就有一個系統的能量關係。）

**Step 2：** 極座標 $Z=r\,e^{j(\omega_0t+\varphi)}$，微分（乘積法則）：
$$Z'=r'e^{j(\cdot)}+r\cdot j\omega_ie^{j(\cdot)}\ \Rightarrow\ Z'Z^*=rr'+j\,r^2\omega_i\qquad\text{(10-152)}.$$

**Step 3：** $E\{rr'\}=0$：$rr'=XX'+YY'$；$R_{XX'}$ 是 $S_{XX}$ 乘 $\pm j\omega$ 的轉換，$S_{XX}$ 偶函數乘 $\omega$ 積分為 0（同理 $Y$）。

**Step 4：** 所以 $E\{Z'Z^*\}=jE\{r^2\omega_i\}$，代入得 $\bar\omega_0=E\{r^2\omega_i\}/E\{r^2\}$。 ∎

**意義**【口頭】：最佳載波有兩種觀點——
- **頻譜觀點**：功率頻譜（右半邊）的重心；
- **時域觀點**：瞬時頻率在能量上的重心。

時域公式對任何 $t$ 都對（10 點、10 點 01 分……答案都一樣），因為系統是穩態的；不穩態時答案會隨時間變，載波就要動。

【課本補充】(10-153)：$E\{r^2\omega_i\}=\frac{1}{2\pi}\int\omega S_{ZZ}(\omega)d\omega$。課本強調瞬時頻率**不是唯一定義的**，因為對偶過程 $Y$ 不唯一；Rice 表示法 $Y=\hat X$ 時，$\omega_i=\frac{X\hat X'-X'\hat X}{r^2}$，$r^2=X^2+\hat X^2$（式 (10-154)）。

---

## 5. FM 訊號何時 WSS

[▶ 42:36](https://youtu.be/a4qBf-61V7E?t=2556) FM 訊號的資訊都在角度，半徑 $r$ 沒有資訊，直接設成 1：
$$Z(t)=e^{j\left(\omega_0t+\lambda\varphi(t)+\varphi_0\right)},\qquad\varphi(t)=\int_0^tC(\alpha)\,d\alpha,\qquad X(t)=\text{Re}\,Z(t).$$

- $C(t)$ 是資訊，用頻率送；頻率是相位的微分，所以資訊要先**積分**才放進相位。
- $\lambda$ 叫**調變指數** (modulation index)，調 $\lambda$ 可以調頻寬。
- $\varphi_0$：基礎相位，和資訊獨立。

> **結論**：若 $C(t)$ **嚴格平穩** (SSS)，$\varphi_0$ 在 $(0,2\pi)$ 均勻且和 $C$ 獨立，則 $X(t)$ 是零平均 WSS。**$C$ 只是弱平穩不夠**。

**證明**：

1. **平均**：$E[X]=\text{Re}\,E[Z]$（取實部和期望值可以對調）。$\varphi_0$ 均勻，$e^{j\varphi_0}$ 平均為 0（最簡單的零平均方法：在 0 到 $2\pi$ 均勻）。所以 $E[X]=0$。
   - $\varphi_0$ 的角色就是讓平均為 0；而零平均時才 if and only if 系統穩態（上一集）。
2. **自相關**：$X=\frac12(Z+Z^*)$，
$$E[X(t+\tau)X(t)]=\tfrac12\text{Re}\left\{E[Z(t+\tau)Z(t)]+E[Z(t+\tau)Z^*(t)]\right\}.$$
   - $E[Z(t+\tau)Z(t)]$（沒有共軛）含 $e^{j2\varphi_0}$，均勻相位使它為 0。老師說這個現象通常普遍成立，可以想想看。
   - $E[Z(t+\tau)Z^*(t)]=e^{j\omega_0\tau}E\left\{e^{j\lambda\int_t^{t+\tau}C(\alpha)d\alpha}\right\}$。
3. **為什麼要嚴格平穩** [▶ 47:15](https://youtu.be/a4qBf-61V7E?t=2835)：積分是從 $t$ 到 $t+\tau$。要不隨時間變，必須把它換成從 $0$ 到 $\tau$ 還相等——也就是 $\int_t^{t+\tau}C$ 的**整個分布**（不只一、二階動差，因為放在指數裡）不隨 $t$ 變。這需要 $C$ 嚴格平穩。 ∎

老師的提醒【口頭】：若要舉不是 WSS 的反例，最好的方法是**讓平均不穩**（例如 $\varphi_0$ 是確定的常數），不用去搞自相關。

---

## 6. Theorem 9-2 的限制

[▶ 48:15](https://youtu.be/a4qBf-61V7E?t=2895) 老師說考試可能會考這個觀念。

- 證明 Theorem 9-2 用的是**卷積**，但不是所有線性系統都能用卷積表示。微分沒有卷積形式，但可以用（脈衝響應的極限、或頻譜上 $j\omega$）。
- **取實部**也是線性系統，也沒有卷積形式。它能不能用 Theorem 9-2？**不行**。
- 證據：$Z\to X=\text{Re}\,Z$ 的自相關關係是 $R_{XX}=\frac12\text{Re}\,R_{ZZ}$（第 2 步），多了一個 $\frac12$，不是「經過兩次濾波」的形式。這種線性系統要**硬算**。
- 結論：Theorem 9-2 有個很強的限制——線性系統要能用**卷積**表示，或有功率頻譜（轉移函數）形式可表示（像微分，用極限處理）。

以下補充，**不是逐字稿內容**：取實部 $\frac12(Z+Z^*)$ 牽涉到**共軛**，對複數係數不是線性的（只是實線性），所以不能寫成卷積 $h*Z$。

**時變系統可以用** [▶ 50:54](https://youtu.be/a4qBf-61V7E?t=3054)：乘 $e^{j\omega_0t}$ 是時變線性系統，Theorem 9-2 還是可以用：證明是用 $h(\tau;t)$，第一次對 $t_2$ 做（加共軛）、第二次對 $t_1$ 做，只是結果變成 $t_1,t_2$ 的函數、不再是 WSS。老師說投影片只討論 $h_1(\tau)e^{j\omega_0t}$ 這種可拆的形式，是因為希望輸出是 WSS；但不能拆的時變系統，定理還是可以用。重點是：**輸入輸出的關係能用卷積描述，定理就能用**。$R_{ZZ}$ 和 $R_{WW}$ 差一個 $e^{j\omega_0\tau}$ 就是這樣來的。

---

## 7. FM 的數學細節：積分要存在

[▶ 54:27](https://youtu.be/a4qBf-61V7E?t=3267)

- **PM**（狹義相位調變）：資訊在 $\varphi$ 上，$\varphi$ 是資訊過程。把 $\varphi$ 的映射定義完，$X$ 只是把 $\varphi$ 放到指數上，所以 $X$ 是 well-defined 的。
- **FM**：資訊是 $C$，$X$ 是 $\varphi$ 的函數，而 $\varphi$ 是 $C$ 的**積分**。$C$ 定義在機率空間上（一個映射），所有統計性都對；但 **$C$ 可不可以積分**是個問題。有的函數不能積分；如果刻意把 $C$ 做成不能積分，$\varphi$ 就不是合法的函數。
- 嚴謹的數學上要注意：透過積分時，積分沒有定義就不能定義它。大部分時候考慮 nice 的函數，都是可積的。

---

## 8. 一頁速查表

### Rice 表示法的濾波器

| 條件 | 結果 |
|---|---|
| 1. $\lvert H\rvert^2=1$ | $H=e^{j\varphi(\omega)}$ |
| 2. $H^*=-H$ | $e^{j2\varphi}=-1$ ⇒ $H=j(-1)^{k(\omega)}=\pm j$ |
| 3. $H(-\omega)=-H(\omega)$ | $k(-\omega)\ne k(\omega)$ |

### 最佳化

- $M=2\pi E|W'|^2=\int(\omega-\omega_0)^2S_{ZZ}\,d\omega$ → 最佳 $\omega_0$ = $S_{ZZ}$ 的重心。
- $M=2\int(\omega^2-\bar\omega_0^2)S_{XX}\,d\omega$ → 重心越大越好。
- $\bar\omega_0=\frac{\int_0^\infty\omega(-1)^{k+1}S_{XX}}{\int_0^\infty S_{XX}}$ → $k=1$（$\omega>0$）→ $H=-j\,\text{sgn}\,\omega$。
- **最佳載波** $\bar\omega_0=\frac{\int_0^\infty\omega S_{XX}d\omega}{\int_0^\infty S_{XX}d\omega}=\frac{E\{r^2\omega_i\}}{E\{r^2\}}$。

### 瞬時頻率

$\omega_i=\omega_0+\varphi'(t)$；$Z'Z^*=rr'+jr^2\omega_i$，$E\{rr'\}=0$。

### FM

$Z=e^{j(\omega_0t+\lambda\int_0^tC+\varphi_0)}$：$C$ SSS、$\varphi_0\sim U(0,2\pi)$ 獨立 ⇒ $X=\text{Re}\,Z$ 零平均 WSS。關鍵：$\int_t^{t+\tau}C$ 的分布要與 $t$ 無關。

### Theorem 9-2 的適用範圍

- 可用：卷積型（含時變 $h(\tau;t)$）、有轉移函數的（微分 $j\omega$）。
- 不可直接用：取實部（$R_{XX}=\frac12\text{Re}\,R_{ZZ}$）。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| FM 訊號的頻譜 | 下一集：FM 頻譜、Woodward 定理（$\lambda$ 大時頻譜 ≈ 瞬時頻率的分布） |
| 瞬時頻率的 PDF = 功率頻譜 | 第 12 集引理的應用 |
| 載波沒有隨機相位時不 WSS | §10-4 循環平穩過程（第 19 集） |
| Theorem 9-2 的限制 | 考試觀念題 |

---

## 附：本集一句話總結

> **Rice 表示法中選 $Y=h*X$，三個條件逼出 $H=\pm j$；再要求解回基頻的訊號變化最小（$E|W'|^2$ 最小），就必須讓載波等於頻譜重心並盡量大，唯一的答案是 Hilbert 轉換，最佳載波是 $S_{XX}$ 右半邊的重心，也等於瞬時頻率的能量加權平均。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 10-3 (2/3) 錄影逐字稿（whisper large-v3-turbo，56:41）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
