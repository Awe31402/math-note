---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 26
lecture: Lec26 5.6 Capacity of correlated parallel Gaussian channels, 5.7 Non-Gaussian discrete-time memoryless channels, 5.8 Band-limited white Gaussian channel
date: 待補
video: https://youtu.be/YtTH7ZdUcKI
notes: Alajaji & Chen §5.6–5.8（pp. 201–210，Theorem 5.38–Observation 5.46）
---

# 第 26 集 · Lec26 §5.6–5.8：相關的平行高斯通道、MIMO、entropy power、band-limited AWGN [▶ 影片](https://youtu.be/YtTH7ZdUcKI)

← 上一集：[25](25-parallel-gaussian-channels-water-filling.md) ｜ [總目錄](README.md) ｜ 下一集：[27](27-lossy-compression-motivation-distortion.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 26 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（45:15，whisper large-v3-turbo）＋ 課本 §5.6–5.8（pp. 201–210）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「高斯」聽成「高學／高薰／高宣／高思／高師」，「線性代數」聽成「先進代數／信心代數」，「colored noise」聽成「color noise／cutor／Cutter」，「eigen system」聽成「I跟System／iGensystem／Igonsystem」，「uncorrelated」聽成「uncollected／Uncreated」，「diagonalize」聽成「逮個輪化」，「Hadamard inequality」聽成「Hadama inequality」，「複數」聽成「負數」、「實數」聽成「時數」、「實部／虛部」聽成「十步／虛步」，「基頻」聽成「機頻」，「non-Gaussianness」聽成「non-gaussianist」，「autocorrelation」聽成「auto-correction」，「傅立葉」聽成「負利的／Fluidium」，「Nyquist、Kotelnikov」聽成「Nightquist Hotel Kennikov」，「sampling theorem」聽成「Sampling Theory／SimpleInseam」，「sinc」聽成「Sync」，「$N_0$」聽成「ending」，「ergodic」聽成「ergatic」，「大數法則」聽成「大術法則」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 開場：機率是長期表現](#1-開場機率是長期表現)
- [2. 相關的雜訊：轉到 eigenvector 上倒水](#2-相關的雜訊轉到-eigenvector-上倒水)
- [3. Theorem 5.38 的證明](#3-theorem-538-的證明)
- [4. MIMO 與複數系統的 capacity](#4-mimo-與複數系統的-capacity)
- [5. Non-Gaussian 雜訊：entropy power](#5-non-gaussian-雜訊entropy-power)
- [6. Entropy power inequality 與 non-Gaussianness](#6-entropy-power-inequality-與-non-gaussianness)
- [7. Band-limited white Gaussian channel](#7-band-limited-white-gaussian-channel)
- [8. 例子：電話線、ADSL；colored noise](#8-例子電話線adslcolored-noise)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

第五章收尾：
1. 雜訊**相關**（colored）的平行高斯通道：轉到雜訊 covariance matrix 的 **eigenvector** 軸上，用 **eigenvalue** 當底倒水。
2. **MIMO**：複數系統的公式沒有 $\frac12$；capacity 隨 $\min(M,N)$ 線性成長。
3. **非高斯雜訊**：用 **entropy power** 夾出 capacity 的上下界；entropy power inequality；non-Gaussianness $D(Z\|Z_G)$。
4. **連續時間、頻寬 $W$** 的 AWGN：$C=W\log_2\left(1+\frac P{N_0W}\right)$ bits/s。

| 主題 | 課本 |
|---|---|
| 相關平行高斯通道 | §5.6 Theorem 5.38（pp. 201–203） |
| MIMO、OFDM | Observation 5.39–5.40（pp. 203–206） |
| Entropy power、上下界、EPI、non-Gaussianness | §5.7 Definition 5.41–Observation 5.43（pp. 206–207） |
| Band-limited AWGN、例子 | §5.8 (5.8.3)、Example 5.44–5.45、Observation 5.46（pp. 207–210） |

---

## 1. 開場：機率是長期表現

[▶ 00:00](https://youtu.be/YtTH7ZdUcKI?t=0)

【口頭】現在什麼都講量化、講數字，但很多數字對個人沒有意義：
- 天氣預報說明天下雨機率 70%——和 65% 對你有什麼差別？要不要帶傘？機率講的是**長期表現**，不是一次。報 70% 不下雨，它也沒報錯（剛好發生那 30%）。
- 投顧說賺錢機率 92%——你賠了就是賠了；而且你一輩子可能只投資兩次。
- **一次傳輸沒有機率，一次投資沒有機率**，你就是要真的做判斷。

接下來的定理也一樣：是**長期傳輸**下能達到 capacity 的公式。

---

## 2. 相關的雜訊：轉到 eigenvector 上倒水

[▶ 02:00](https://youtu.be/YtTH7ZdUcKI?t=120)

**設定**：四支天線，四個雜訊有**相關性**（天線很難讓雜訊獨立，除非拉得很開）。【口頭】上一集說 water-filling 在實作上不對，是因為「高斯輸入」這個假設；但**分析模式是對的**。這裡先假設高斯輸入達得到，學這個分析模式。

【口頭】**線性代數不是白學的**：大二學 eigenvalue、eigenvector 常常不知道要幹嘛，在通訊上它非常有意義。
- 雜訊不再是白色，而是有顏色的 **colored noise**，看它的 **covariance matrix** $K_Z$。
- **Eigenvalue 是能量**（單位就是能量）。
- **Eigenvector 是系統運作的獨立軸**：輸入要運作在雜訊的 eigenvector 上。
- 雜訊是 colored，輸入也要是 **colored 的高斯**，而且「顏色」和雜訊一樣（相同的 eigen system）——要長得像你。
- 在 eigenvector 軸上倒水：$P_i=\theta-\lambda_i$。注意 $P_1$ **不是**第一支天線的能量，而是第一個 eigenvector 軸上的能量；要轉回來才知道每支天線用多少。

**Theorem 5.38（correlated parallel Gaussian channels 的 capacity）**（p. 203）：雜訊 covariance matrix $K_Z$ 正定，總功率 $P$，
$$C(P)=\sum_{i=1}^k\frac12\log_2\left(1+\frac{P_i}{\lambda_i}\right),\qquad P_i=\max\{0,\theta-\lambda_i\},\qquad\sum_iP_i=P,$$
$\lambda_i$ 是 $K_Z$ 的第 $i$ 個 eigenvalue。由 mean 0 的高斯輸入達到，其 covariance $K_X$ 和 $K_Z$ **有相同的 eigenvectors**，第 $i$ 個 eigenvalue 是 $P_i$。

【口頭】
- 工程直覺：碰到有相關性的問題，**先轉到它的 eigen system 上思考**，通常會得到對的解。
- 非高斯輸入（BPSK、QPSK）時一樣轉到 eigenvector 軸上，只是改成 mercury/water-filling 或 two-phase water-filling。
- 複雜度：64 支天線就是 64×64 的矩陣，手機很難算。若只有 3×3 的運算能力，就找 eigenvalue 最大（訊號最強）的三根軸，其他設為 0，只針對這三根解，結果還不錯。

---

## 3. Theorem 5.38 的證明

[▶ 07:06](https://youtu.be/YtTH7ZdUcKI?t=426)

**限制改寫成矩陣**：每軸能量總和 $\le P$ 就是 $\mathrm{tr}(K_X)\le P$（$K_X$ 是輸入的 covariance matrix）。

**第一步**：加性通道，輸入和雜訊獨立，
$$I(X^k;Y^k)=h(Y^k)-h(Z^k),\qquad K_Y=K_X+K_Z$$
（獨立相加 covariance 就相加，不必是高斯）。$h(Z^k)$ 量出來、不能動，只能讓輸出越豐富越好——高斯最大：
$$h(Y^k)\le\frac12\log_2\left[(2\pi e)^k\det(K_X+K_Z)\right],$$
等號在 $Y^k$ 高斯，也就是 $X^k$ 是高斯。

**第二步：怎麼分配（量化）**。要 maximize $\det(K_X+K_Z)$，$\mathrm{tr}(K_X)\le P$。
- 把 $K_Z$ 對角化：$K_Z=A\Lambda A^T$，$A$ 的 column 是 eigenvectors（$AA^T=I$），$\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_k)$。
- $\det(K_X+K_Z)=\det(AA^TK_XAA^T+A\Lambda A^T)=\det(A)\det(A^TK_XA+\Lambda)\det(A^T)=\det(A^TK_XA+\Lambda)$。
- 令 $V=A^TK_XA$。變成對付 **uncorrelated** 的雜訊 $\Lambda$——上一集的結果可以用了。
- **Trace 的限制不變**：$\mathrm{tr}(V)=\mathrm{tr}(A^TK_XA)=\mathrm{tr}(K_XAA^T)=\mathrm{tr}(K_X)\le P$（trace 裡矩陣可以輪換）。
- **Hadamard inequality**：正定矩陣的 determinant $\le$ 對角線相乘，所以
$$\det(V+\Lambda)\le\prod_i(V_{ii}+\lambda_i),$$
  等號在 $V$ 是 diagonal——也就是 $K_X=AVA^T$ **和 $K_Z$ 有相同的 eigenvectors**。
- 剩下就是 $\sum V_{ii}=P$ 下 maximize $\sum\frac12\log(1+\frac{V_{ii}}{\lambda_i})$，就是 water-filling，$V_{ii}=P_i=\max\{0,\theta-\lambda_i\}$。∎

【口頭】
- 矩陣運算要熟；將來走向量子通訊，非常著重這種矩陣轉換。
- 做工程理論，不能只玩數學：要建立 guideline、能解釋工程現象；解釋不了就只剩數學遊戲，那就要找出為什麼不合。

---

## 4. MIMO 與複數系統的 capacity

[▶ 13:47](https://youtu.be/YtTH7ZdUcKI?t=827)

**多天線模型**（Observation 5.39，p. 203）：$\underline Y_i=H_i\underline X_i+\underline Z_i$，$H$ 是 $N\times M$ 矩陣（$M$ 支傳送、$N$ 支接收天線），一般是**複數**。

**為什麼是複數**【口頭】：基頻傳送有兩軸，例如 QPSK 送 $\pm1\pm i$ 四點——用複數表示二維向量。

**複數系統沒有 $\frac12$**：
- 實數：$C(P)=\frac12\log_2\left(1+\frac P{\sigma^2}\right)$。
- 複數：$C(P)=\log_2\left(1+\frac P{\sigma^2}\right)$。
- 直觀：一個複數是兩維實數，每次送兩軸，帶兩倍的量。
- 數學來源：高斯 pdf 不一樣（課本 footnote 13）。實數 $\left(\frac1{\sqrt{2\pi\sigma^2}}\right)^N\exp\left(-\frac1{2\sigma^2}\sum z_i^2\right)$；複數 $\left(\frac1{\pi\sigma^2}\right)^N\exp\left(-\frac1{\sigma^2}\sum|z_i|^2\right)$，2 不見了，differential entropy 就沒有 $\frac12$。
- **兩者等效**的例子：二維實數 $(z_1,z_2)$、每維 variance $\sigma^2$；換成一維複數 $z=z_1+iz_2$，$|z|^2=z_1^2+z_2^2$，複數的 variance 是 $E|z|^2=2\sigma^2$。把 $2\sigma^2$ 代進複數公式，兩邊完全一樣。
- 【口頭】看到公式有 $\frac12$，就知道它在玩實數體系；沒有 $\frac12$，就是複數體系（等效基頻）。寫錯了你馬上可以指正。

**兩種情形**（課本 (5.6.2)、(5.6.3)，$K_Z=I_N$）：
- **DSI**（接收端完全知道 $H$，傳送端只知道分布）：先取期望值再 max（輸入只能固定一個）：
$$C_{DSI}(P)=\max_{K_X:\,\mathrm{tr}(K_X)\le P}E_H\left[\log_2\det\left(HK_XH^\dagger+I_N\right)\right].$$
- **FSI**（兩端都知道 $H$）：先 max 再取期望值，結果是 water-filling：輸入乘上 $H$ 要和雜訊的 eigenvector 對齊，在 eigenvector 方向分配能量，高度是 eigenvalue。$C_{DSI}\le C_{FSI}$。

**Capacity 和 $\min(M,N)$ 成正比**【口頭】[▶ 20:07](https://youtu.be/YtTH7ZdUcKI?t=1207)：
- 雖然達不到，但它是很多人實作時用的 guideline：兩支天線 2 倍、三支 3 倍、四支 4 倍。
- 取**少的那邊**：1 傳 3 收，$\min=1$，從 capacity 來看沒用；3 傳 1 收也沒用；3 傳 2 收是 2 倍。
- 要把 100 Mbps 增加 10 倍，傳送端和接收端天線都要超過 10 根才有用。
- 【課本補充】課本說：接收端完全知道 Rayleigh fading 係數時，高 SNR 下 MIMO capacity 隨 $\min(M,N)$ 線性成長；MIMO 已是 Wi-Fi（IEEE 802.11）、4G WiMax、LTE 的必要元件。另有 Observation 5.40（OFDM）課堂沒講。

---

## 5. Non-Gaussian 雜訊：entropy power

[▶ 21:40](https://youtu.be/YtTH7ZdUcKI?t=1300)

【口頭】雜訊像高斯是理論假設；量測也很接近，但「接近」不代表真的一樣。雜訊不是高斯時 capacity 理論上更高（上一集），做不做得到是另一回事。

加性雜訊：$I(X;Y)=h(Y)-h(Z)$——真正影響傳輸量的是雜訊的 **differential entropy**，不是 variance。高斯時 $h(Z)=\frac12\log_2(2\pi e\sigma^2)$，非高斯沒有公式。

**Definition 5.41（entropy power）**（p. 206）：
$$Z_e:=\frac1{2\pi e}2^{2h(Z)}.$$
- 它是「和 $Z$ 有**相同 differential entropy** 的高斯」的 variance：$\frac12\log_2(2\pi eZ_e)=h(Z)$。
- 【口頭】單位是 power，但來自 entropy 的概念；不是真正的雜訊能量，而是**直接影響傳輸量的等效雜訊能量**。例如告訴你 $Z_e=2.1$，傳輸量就是 $h(Y)-\frac12\log_2(2\pi e\cdot2.1)$，直接代就好。和 differential entropy 一對一對應，但有很多直觀用途。
- $Z$ 是高斯時 $Z_e=\mathrm{Var}(Z)$。

**Lemma 5.42（上下界）**（p. 206）：加性雜訊、variance $\sigma^2$、power $P$，
$$\frac12\log_2\frac{P+\sigma^2}{Z_e}\ \ge\ C(P)\ \ge\ \frac12\log_2\frac{P+\sigma^2}{\sigma^2}.$$
- 下界：Theorem 5.33（最爛就是碰到高斯）。
- 上界：$I=h(Y)-h(Z)\le\frac12\log_2[2\pi e(P+\sigma^2)]-\frac12\log_2(2\pi eZ_e)$。
- 【口頭】上界是 overestimate：雜訊不是高斯時 $Y$ 不太可能是高斯。但趨勢是對的。例：上界算出 2.8，就不可能每次傳 3、4、5 個 bit。
- 【口頭】$Z_e$、$\sigma^2$ 都是量出來的；$C(P)$ 夾在兩條 log 曲線中間——**用能量換傳輸量大概是 log 的關係**：能量 2 倍變 4 倍，換到的是 log 2 到 log 4。

【口頭】如果傳送、接收端都不知道 $A$（或切成「training 估 $A$ + 給定 $A$ 接收」兩段），整段平均的 capacity 是不知道的；BPSK、QPSK 時更難，連高斯輸入都不知道，這是後續研究。

---

## 6. Entropy power inequality 與 non-Gaussianness

[▶ 27:21](https://youtu.be/YtTH7ZdUcKI?t=1641)

**高斯**：獨立的 $Z_1$、$Z_2$ 相加，variance 相加；寫成 $2^{2h(Z_1+Z_2)}=2^{2h(Z_1)}+2^{2h(Z_2)}$。（【口頭】這個 2 表示是實數系統；複數系統沒有。）

**Entropy power inequality（EPI）**（(5.7.2)–(5.7.3)，p. 207）：獨立、非高斯時
$$2^{2h(Z_1+Z_2)}\ge2^{2h(Z_1)}+2^{2h(Z_2)}\iff Z_e(Z_1+Z_2)\ge Z_e(Z_1)+Z_e(Z_2).$$
- 【口頭】常見情形：$Y_1=X_1+Z_1$、$Y_2=X_2+Z_2$，接收端把兩個加在一起，就碰到兩個雜訊相加。兩個不像高斯的雜訊加起來，entropy power 會**比個別的和還多**——因為 $h$ 是被減掉的，損失更多。所以「像不像高斯」很重要。
- 證明課本引 [83, §17.8]（Cover & Thomas）。

**Observation 5.43（non-Gaussianness）**（p. 207）：
$$\frac12\log_2\frac{P+\sigma^2}{Z_e}=\frac12\log_2\frac{P+\sigma^2}{\sigma^2}+D(Z\|Z_G),$$
$Z_G\sim\mathcal N(0,\sigma^2)$。所以
$$C_G(P)+D(Z\|Z_G)\ \ge\ C(P)\ \ge\ C_G(P).$$
- $D(Z\|Z_G)$ 叫 **non-Gaussianness**：雜訊像不像高斯，用 divergence 量，對系統有量化意義。
- 【口頭】證明：兩邊相減，上面的 $P+\sigma^2$ 消掉，剩下的就是 divergence 的公式。這是 Verdú 他們提出的（Princeton 的學者，water-filling 的後續研究也是他們）。

> 以下**不是逐字稿內容**，是依 divergence 定義推論的一步：$D(Z\|Z_G)=-h(Z)-\int f_Z\log_2f_{Z_G}=-h(Z)+\frac12\log_2(2\pi e\sigma^2)$（因為 $\log f_{Z_G}$ 只有二次項，$E[Z^2]=\sigma^2$），而 $\frac12\log_2\frac{\sigma^2}{Z_e}=\frac12\log_2(2\pi e\sigma^2)-h(Z)$，兩者相等。

---

## 7. Band-limited white Gaussian channel

[▶ 30:25](https://youtu.be/YtTH7ZdUcKI?t=1825)

【口頭】更實際的系統是連續的：送的是**波形** $X(t)$，雜訊也是波形，通道和輸入做 convolution（頻域相乘）。先講線性、簡化的情況。

**模型**（§5.8，p. 207）：$Y(t)=(X(t)+Z(t))*h(t)$。
- $h$ 是**理想低通**：$H(f)=1$（$|f|\le W$），否則 0——這是自然界的，不能改。
- $Z(t)$：白色高斯，PSD $=\frac{N_0}2$（正負頻率都一樣）。【口頭】PSD 是 autocorrelation function 的傅立葉轉換。
- Power constraint（長期平均）：$\lim\frac1T\int E[X(t)^2]dt\le P$。
- $X(t)$ 也設成 band-limited：在 $|f|>W$ 放能量沒用，會被濾掉（通道只過 1 MHz，送 2 MHz 沒用）。

**化簡**：convolution 是線性，可分配：$Y=X*h+Z*h$；$X$ 本來就在 $[-W,W]$ 內，$X*h=X$。所以等效於
$$Y(t)=X(t)+\tilde Z(t),\qquad\tilde Z=Z*h\ (\text{filtered noise}),$$
PSD 是 $\frac{N_0}2$（$|f|\le W$），外面 0。【口頭】線性系統的好處：輸出 PSD = 輸入 PSD × $|H(f)|^2$，能量可以預估；非線性就沒有這個關係。

**Sampling theorem**【口頭】：band-limited 的訊號每 $\frac1{2W}$ 秒取樣一次，可以用 interpolation **完全重建**波形（Nyquist、Kotelnikov、Shannon 的貢獻；有的書說 sampling theorem 是 Shannon 在 information theory 之外很大的貢獻）。數位通訊常用的 Rake receiver，推導也假設 band-limited。
- 注意「沒有資料損失」指波形可以完全重建，**不是** Shannon 的 information 量（連續波形的 information 量是無限大）。

**雜訊樣本不相關**：$\tilde Z$ 的 autocorrelation 是 PSD 的反傅立葉轉換
$$K_{\tilde Z}(\tau)=N_0W\,\mathrm{sinc}(2W\tau),\qquad\mathrm{sinc}(x)=\frac{\sin\pi x}{\pi x}.$$
每 $\frac1{2W}$ 取樣：不同時間的樣本 $\mathrm{sinc}$ 剛好是 0 ⇒ **uncorrelated**（高斯 ⇒ 獨立）；同一時間是 $N_0W$（總面積）。所以變成**白色**的離散時間 AWGN，不用 water-filling（colored 才要）。

**Capacity**：每個樣本的 signal power 是 $E[X_n^2]=P$，noise power 是 $N_0W$，所以每次 channel use：
$$C=\frac12\log_2\left(1+\frac P{N_0W}\right)\ \text{bits / channel use}.$$
（【口頭】有 $\frac12$——實數系統。）每秒 $2W$ 個 sample（每次 channel use 是 $\frac1{2W}$ 秒），單位換成 bits/second：
$$\boxed{C(P)=W\log_2\left(1+\frac P{N_0W}\right)\ \text{bits/second}}\qquad(5.8.3)$$
$\frac P{N_0W}$ 是 SNR。最佳輸入：用 water-filling 看，雜訊 PSD 在 $[-W,W]$ 是平的 $\frac{N_0}2$，倒水量 $P$，所以每個頻率用一樣的能量，PSD $=\frac P{2W}$（寬 $2W$ × 高 $\frac P{2W}=P$）。

【課本補充】課本強調這個推導是 heuristic：沒有嚴格證明原通道和離散版本等效，也沒有對原通道證 coding theorem。

【口頭】我們的公式都建立在大數法則上。工程（自然界）的現象很容易有大數法則——該下雨就下雨、該地震就地震；社會科學（選票）就難說是 stationary、ergodic，每次預測都不準很合理，因為人會亂講、會臨時改變。

---

## 8. 例子：電話線、ADSL；colored noise

[▶ 41:37](https://youtu.be/YtTH7ZdUcKI?t=2497)

**Example 5.44（電話線）**：頻寬 $W=4$ kHz、SNR 40 dB。
- 【口頭】40 dB 很厲害：傳送能量是雜訊的 $10^{40/10}=10^4$（1 萬）倍。無線能做到 20 dB 就很難了；有線短距離可能達到 40 dB。
- $C=4000\log_2(1+10000)=53151.4$ bits/s。

> ⚠️ 逐字稿缺字／口誤：[▶ 42:40](https://youtu.be/YtTH7ZdUcKI?t=2560) 老師說「就是 51K 而已」，後面又說「傳到 104 是兩倍」（以 52K 算）。課本 Example 5.44 算出 53151.4 bits/s ≈ 53 kbps。

- 傳輸速度在 53 kbps 以下，一定存在方法（長期平均）做得到；超過錯誤率就很高。例如 rate 是兩倍，weak converse 說錯誤率至少 $1-\frac CR=\frac12$；實際上是 strong converse，更糟。

**ADSL**【口頭】：有線傳輸可以到幾百 Mbps，是因為 $W$ 大。ADSL（Asymmetric Digital Subscriber Line，非對稱：上傳和下載不一樣）的上傳頻寬約 1 MHz 以上；代進公式約 15 Mbps（下載頻寬更大）。實際 ADSL 上傳大約 1 Mbps、下載大約 10 Mbps 左右，還沒達到；而且 15 Mbps 的代價是 40 dB。

> ⚠️ 待確認：[▶ 43:11](https://youtu.be/YtTH7ZdUcKI?t=2591) ADSL 的頻寬與速率數字（「1Mbps 以上」「9MHz、10MHz」「1.2 Mbps 變成 15 Mbps」）逐字稿很亂，單位 Hz／bps 混用，無法確定老師的原意；課本沒有這個例子。

【課本補充】Example 5.45：$W\to\infty$ 時 $C\to\frac P{N_0\ln2}$ bits/s（有限值）。

**Colored Gaussian noise**（Observation 5.46，p. 209）[▶ 44:12](https://youtu.be/YtTH7ZdUcKI?t=2652)：雜訊 PSD 不平時，在頻域上**倒水**——雜訊 PSD 當底、水量 $P$，就知道哪個頻率用多一點能量、哪個少一點。（【口頭】用 BPSK、QPSK 時倒水就不對了，可能要偏向 equal SNR；但若假設 water-filling 對，最佳傳輸 PSD 完全由倒水決定。）這是第五章的結果。

---

## 9. 一頁速查表

**相關平行高斯（Thm 5.38）**：$C=\sum\frac12\log_2(1+\frac{P_i}{\lambda_i})$，$P_i=\max\{0,\theta-\lambda_i\}$，$\lambda_i$ 是 $K_Z$ 的 eigenvalue。
- 關鍵一步：$K_Z=A\Lambda A^T$，$\det(K_X+K_Z)=\det(V+\Lambda)$，$V=A^TK_XA$，$\mathrm{tr}V=\mathrm{tr}K_X$；Hadamard：$\det(V+\Lambda)\le\prod(V_{ii}+\lambda_i)$，等號 $V$ diagonal ⇒ $K_X$ 和 $K_Z$ 同 eigenvectors。

**MIMO**：$\underline Y=H\underline X+\underline Z$（複數）。
- 複數 AWGN：$C=\log_2(1+\frac P{\sigma^2})$（沒有 $\frac12$；複數高斯 pdf 是 $\frac1{\pi\sigma^2}e^{-|z|^2/\sigma^2}$）。
- $C_{DSI}=\max_{\mathrm{tr}K_X\le P}E_H\log_2\det(HK_XH^\dagger+I)\le C_{FSI}$；capacity $\propto\min(M,N)$。

**Entropy power**：$Z_e=\frac1{2\pi e}2^{2h(Z)}$（同 $h$ 的高斯的 variance）。
- $\frac12\log_2\frac{P+\sigma^2}{Z_e}\ge C(P)\ge\frac12\log_2\frac{P+\sigma^2}{\sigma^2}$；即 $C_G+D(Z\|Z_G)\ge C\ge C_G$。
- EPI：$Z_e(Z_1+Z_2)\ge Z_e(Z_1)+Z_e(Z_2)$，高斯時等號。

**Band-limited AWGN**：理想低通 $W$、PSD $\frac{N_0}2$。
- 取樣每 $\frac1{2W}$ 秒；雜訊 autocorrelation $N_0W\,\mathrm{sinc}(2W\tau)$ ⇒ 樣本獨立。
- $C=W\log_2(1+\frac P{N_0W})$ bits/s；電話線 4 kHz、40 dB ⇒ 53.15 kbps。
- Colored noise ⇒ 在頻域倒水。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 進入第六章：有損壓縮、distortion | 第 27 集（§6.1–6.2） |
| Reverse water-filling（平行高斯 source 的 rate-distortion） | 第 29 集（§6.4） |
| $W\log_2(1+\frac P{N_0W})$ 推出 Shannon limit（$E_b/N_0\ge\ln2$） | 第 31 集（§6.6） |

---

## 附：本集一句話總結

> **雜訊相關時，把一切轉到雜訊 covariance 的 eigenvector 上，用 eigenvalue 當底倒水；MIMO 的 capacity 隨天線數的較小者線性成長（複數系統沒有 1/2）；非高斯雜訊的 capacity 夾在 $C_G$ 和 $C_G+D(Z\|Z_G)$ 之間；而頻寬 $W$ 的 AWGN 波形通道，透過取樣變成離散通道，得到 $W\log_2(1+P/N_0W)$ bits/s。**

---

## ⚠️ 待確認清單

1. [▶ 43:11](https://youtu.be/YtTH7ZdUcKI?t=2591) ADSL 的頻寬與速率數字逐字稿很亂（Hz、bps 混用），老師原意無法確定；課本沒有這個例子。

---

*筆記依據陳伯寧老師「消息理論」Lec26 錄影逐字稿（whisper large-v3-turbo，45:15）與 Alajaji & Chen 課本 §5.6–5.8 整理。*
