---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 30
lecture: Lec30 Chapter 6：6.5 Lossy joint source–channel coding theorem、6.6 Shannon limit of communication systems（1/2）
date: 待補
video: https://youtu.be/dVBICTIzUBs
notes: Alajaji & Chen §6.5–6.6（pp. 248–257，Theorem 6.33–Example 6.39）
---

# 第 30 集 · Lec30 §6.5–6.6：有損的 joint source–channel coding theorem 與 Shannon limit（上）[▶ 影片](https://youtu.be/dVBICTIzUBs)

← 上一集：[29](29-rate-distortion-calculation.md) ｜ [總目錄](README.md) ｜ 下一集：[31](31-shannon-limit-communication-systems.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 30 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（25:54，whisper large-v3-turbo）＋ 課本 §6.5–6.6（pp. 248–257）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「lossy」聽成「Law C／Lawsey」，「Hamming」聽成「Hemming」，「BER」聽成「bit array／r b e r」，「stationary ergodic」聽成「station ergotic」，「hard decision」聽成「Hard Decision／哈底細菌／hard decadent」，「signal-to-noise ratio」聽成「signal to knowledge／node／total ratio」，「rate-1/3、rate-1/2」聽成「3e／三一、2E／21 code」，「trellis coded modulation」聽成「trace coding modulation」，「Forney」聽成「佛尼」，「LDPC」聽成「LDB Code」，「MacKay」聽成「McKay」，「Shannon」聽成「Shanon／Shanen」，「大數法則」聽成「大樹法則」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：lossless 的 separation principle](#1-複習lossless-的-separation-principle)
- [2. Theorem 6.33：有損的 joint source–channel coding](#2-theorem-633有損的-joint-sourcechannel-coding)
- [3. 單位：換成 bits per second](#3-單位換成-bits-per-second)
- [4. Shannon limit 的定義](#4-shannon-limit-的定義)
- [5. 例一：二元 source 經 BSC（hard decision）](#5-例一二元-source-經-bschard-decision)
- [6. 例二：高斯 source 經 AWGN](#6-例二高斯-source-經-awgn)
- [7. 例三：二元 source 經 BPSK-AWGN（soft decision）](#7-例三二元-source-經-bpsk-awgnsoft-decision)
- [8. 五十年的路：從 9.6 dB 到 Shannon limit](#8-五十年的路從-96-db-到-shannon-limit)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

第六章、也是整個傳統消息理論的最後一個項目：**有損的 joint source–channel coding theorem**（lossy information transmission theorem）——條件是 $\frac mn R(D)<C$。用它定義 **Shannon limit**：給定 rate，系統能達到的**最小 distortion**（Hamming 時就是最小 bit error rate），算出 BSC 和 BPSK-AWGN 下的 Shannon limit 表，並看 Turbo code、LDPC code 怎麼一步步逼近它。

| 主題 | 課本 |
|---|---|
| 有損 joint source–channel coding theorem | §6.5 Definition 6.32、Theorem 6.33（pp. 248–249） |
| Signaling rate 的形式 | Observation 6.34（p. 249） |
| Shannon limit 定義 | §6.6 (6.6.1)（pp. 249–250） |
| BSC／hard decision | Example 6.35、Table 6.1（pp. 250–252） |
| 高斯 source 經 AWGN | Example 6.37（pp. 253–254） |
| BPSK-AWGN soft decision | Example 6.39、Fig. 6.4、Table 6.2（pp. 255–257） |

---

## 1. 複習：lossless 的 separation principle

[▶ 00:00](https://youtu.be/dVBICTIzUBs?t=0)

第 21 集的 **information transmission theorem**：source 每 $m$ 個處理一次、channel 每 $n$ 個送一次，
- $mH<nC$：送得過去，而且 **lossless**；
- 反過來：一定送不過去。

【口頭】為什麼叫 **separation principle**：左邊只和 source 的分布有關，右邊只和雜訊的分布有關，兩個量**獨立計算**。

---

## 2. Theorem 6.33：有損的 joint source–channel coding

[▶ 01:02](https://youtu.be/dVBICTIzUBs?t=62)

【口頭】送不過去沒關係，允許 **lossy**——把傳輸也當成一種壓縮。中間怎麼傳、方法是什麼都不知道，只要求接收端的估計 $\hat Z^m$ 和 source $Z^m$ 之間
$$\frac1mE\left[\rho_m(Z^m,\hat Z^m)\right]\le D.$$
- $\rho$ 是 **Hamming** 時，$D$ 就是 **bit error rate**（通訊上的 $10^{-5}$）——這是 **detection**（送 0101，猜 0101）。
- $\rho$ 是 **squared error** 時，要讓 $\sum(Z_i-\hat Z_i)^2$ 小——這是 **estimation**。
- distortion 一樣要是 **additive**、**bounded**（大數法則）。

**Theorem 6.33（lossy joint source–channel coding theorem）**（p. 248）：stationary ergodic source（有限字母、bounded additive distortion、rate–distortion function $R(D)$），DMC（capacity $C$），兩者同單位：
- **Forward**：對任何 $D>0$，若 $\limsup_{m\to\infty}\frac m{n_m}R(D)<C$，則 $m$ 夠大時存在 $m$-to-$n_m$ 的有損 source–channel code 滿足 distortion $D$。
- **Converse**：任何滿足 distortion $D$ 的碼都有 $\frac m{n_m}R(D)\le C$。

【口頭】
- Source 推廣到 stationary ergodic——要的還是大數法則。
- $R(D)$ 只看 source 分布（$\hat Z$ 是數學上自己產生的，不是真正接收端的），$C$ 只看雜訊——**仍然是 separation**。什麼時候不能 separation，以後會講。
- 和 lossless 比：把 $mH$ 換成 $mR(D)$。而且是 **if and only if**。
- 例：binary uniform source（壓縮好的 0101，各 $\frac12$）＋Hamming：$R(D)=1-h_b(D)$；BSC：$C=1-h_b(\varepsilon)$。$\varepsilon$ 是量出來的，BER 要求給定，有時做得到、有時做不到。
- 這是極限的概念：$\frac mn$ 是 1000/1000、一萬/一萬、一千萬/一千萬……$m,n\to\infty$（需要 typical set）。直觀上就是 $m$ 倍的 $R(D)$ 要小於 $n$ 倍的 $C$。

【課本補充】證明用 channel coding theorem 和 rate–distortion theorem，和第 21 集 lossless 版本類似，課本留作習題。

---

## 3. 單位：換成 bits per second

[▶ 07:06](https://youtu.be/dVBICTIzUBs?t=426)

- $R(D)$ 的單位：每個 **source 符號** $Z$ 用幾個 bit；$C$ 的單位：每次 **channel 使用** $X$ 帶幾個 bit。單位不同，所以要乘上個數：例如 500 個 source、每個 3 bit，共 1500 bit；2000 次 channel 使用能帶多少 bit。
- **時間要對齊**：$m$ 個 source 符號要用 $n$ 次 channel 送完，$mT_s=nT_c$（$T_s$：每個 source 符號的時間；$T_c$：每次 channel 使用的時間），所以 $\frac mn=\frac{T_c}{T_s}$。

**Observation 6.34**（p. 249）：$\frac{T_c}{T_s}R(D)<C$ 做得到；反過來任何碼都有 $\frac{T_c}{T_s}R(D)\le C$。

兩邊除以 $T_c$：$\frac{R(D)}{T_s}<\frac C{T_c}$——**source 每秒產生的 bit 數** < **channel 每秒能帶的 bit 數**，單位一樣才能比。【口頭】例如傳送端每 0.1 ms 送一次、source 每 0.2 ms 來一次。Source 每秒來 3 bit、channel 每秒只能帶 2 bit，一定送不過去——這是證明出來的：左邊是達到這個 distortion 的**最小**傳送量，右邊是 channel 的**最大**傳送速度。

**做不到怎麼辦**【口頭】：例如 $R(D)$ 算出 2.1 bps、channel 只有 2.0 bps，就把 $D$ 放寬：$10^{-5}$ 變 $10^{-4}$，$R(D)$ 也許變 1.9 bps < 2.0，就存在方法送過去——那方法在哪裡不知道，可能要經過二、三十年才找到。

---

## 4. Shannon limit 的定義

[▶ 11:47](https://youtu.be/dVBICTIzUBs?t=707)

令 $R_{sc}:=\frac mn$（source 符號／channel 使用）。能做到就要
$$R_{sc}\cdot R(D)\le C\iff R(D)\le\frac C{R_{sc}}.\qquad(6.6.1)$$
**Shannon limit** $D_{SL}$：讓 (6.6.1) 取等號的**最小** $D$——所有 rate $R_{sc}$ 的碼能達到的 distortion 的下界。Hamming 時就是最小錯誤率。

【口頭】我們更喜歡從錯誤率的角度看：$10^{-5}$ 做不做得到？畫圖：$R(D)$ 是一條曲線（binary 時 $h_b(p)-h_b(D)$），channel 固定 ⇒ $C$ 固定，要求的 rate 固定 ⇒ 水平線 $\frac C{R_{sc}}$，交點就是能達到的 distortion，再小就做不到。

【課本補充】Shannon limit 一般不一定達得到；文獻上類似的量叫 OPTA（optimal performance theoretically achievable）、LMTR。

---

## 5. 例一：二元 source 經 BSC（hard decision）

[▶ 13:21](https://youtu.be/dVBICTIzUBs?t=801)

**Example 6.35**（p. 250）：binary uniform DMS、Hamming（$E\rho=P_b$，bit error probability），BSC crossover $\varepsilon<\frac12$。
$$R(D)=1-h_b(D),\quad C=1-h_b(\varepsilon)\ \Rightarrow\ D_{SL}=h_b^{-1}\left(1-\frac{1-h_b(\varepsilon)}{R_{sc}}\right).\qquad(6.6.2)$$
- $h_b^{-1}$ 是 $h_b$ 在 $[0,\frac12]$ 上的反函數（$h_b$ 在整個 $[0,1]$ 上沒有反函數）。
- 【口頭】反過來看：給錯誤率要求（例如 $10^{-4}$），能容忍的最大雜訊 $\varepsilon$ 是多少——雜訊比它小就一定送得過去，比它大就送不過去。

**換成 AWGN + BPSK + hard decision**（(6.6.5)–(6.6.7)）：
- 【口頭】實際的通道是高斯雜訊。把 1、0 轉成 ±1 送（BPSK），接收端用 0 當門檻決定 1 或 0（hard decision）：送 +1 可能得 +1 或 −1、送 −1 也一樣；雜訊 zero mean、全對稱 ⇒ 自動形成 **BSC**。
- $\varepsilon=Q\left(\sqrt{\frac{2P}{N_0}}\right)$，$Q(x)=\frac1{\sqrt{2\pi}}\int_x^\infty e^{-t^2/2}dt$（數位通訊學過的 $Q(\sqrt{2\,\text{SNR}})$）。
- 用 **每個 source（information）bit 的 SNR** $\gamma_b:=\frac{E_b}{N_0}$：每次 channel 使用的能量 $P=R_{sc}E_b$，所以 $\varepsilon=Q\left(\sqrt{2R_{sc}\gamma_b}\right)$，
$$R_{sc}\left(1-h_b(D_{SL})\right)=1-h_b\left(Q\left(\sqrt{2R_{sc}\gamma_b}\right)\right).\qquad(6.6.7)$$

**Table 6.1**（hard decision 的 Shannon limit，$\gamma_b$ 單位 dB）：

| $R_{sc}$ | $D_{SL}=0$ | $10^{-5}$ | $10^{-4}$ | $10^{-3}$ | $10^{-2}$ |
|---|---|---|---|---|---|
| 1/3 | 1.212 | 1.210 | 1.202 | 1.150 | 0.077 |
| 1/2 | 1.775 | 1.772 | 1.763 | 1.703 | 1.258 |
| 2/3 | 2.516 | 2.513 | 2.503 | 2.423 | 1.882 |
| 4/5 | 3.369 | 3.367 | 3.354 | 3.250 | 2.547 |

（課本表格最後一欄印成 $10^{-3}$，依數值和老師口述「$10^{-2}$……0.07」應為 $10^{-2}$。）

【口頭】解讀：
- Rate 1/3（送 3 個 channel bit 帶 1 個 information bit），要求 $10^{-5}$，SNR 不能比 **1.2 dB** 差。量出來 0.9 dB，就**絕對做不到**。
- 1.2 dB 是 guideline：你的方法在 3 dB 做到 $10^{-5}$，就離 Shannon limit 還有 $3-1.2=1.8$ dB，可以比較誰差得比較遠、還有多少改善空間。
- 完全不要錯誤（$D=0$）也可以：SNR 大於 1.212 dB 就行（3 dB 是兩倍，1.2 dB 大概一點多倍）。
- 願意錯誤率高（$10^{-2}$），大概 0 dB（0.077）就可以——雜訊能量和傳送能量差不多相等也做得到。
- Rate 變快（1/2），要求更高。
- 應用：火星拍一張照片傳回 NASA，若 SNR 比表上的差，又要這個速度，Shannon 告訴你不可能 ⇒ 要**降速**（1/6、1/10、1/12……），找到一個要求低於量到的 SNR（例如 0.9 dB）、錯誤率又可接受的 rate，才比較有機會。
- Hard decision 不是我們的目標，等一下講 soft decision。

【課本補充】$R_{sc}=1$ 時 $D_{SL}=\varepsilon$，而**不編碼**（直接送 $X_i=Z_i$、輸出當重建 $\hat Z_i=Y_i$）就達到 $P_b=\varepsilon$——uncoded 是最佳的，而且沒有延遲、沒有複雜度。$R_{sc}\ne1$ 或 source 非 uniform 時就不是了。

---

## 6. 例二：高斯 source 經 AWGN

[▶ 20:01](https://youtu.be/dVBICTIzUBs?t=1201)

**Example 6.37**（p. 253）：高斯 source（variance $\sigma^2$）、squared error，AWGN（power $P$、noise variance $\sigma_N^2$）。
$$\frac12\log_2\frac{\sigma^2}{D_{SL}}=\frac1{2R_{sc}}\log_2\left(1+\frac P{\sigma_N^2}\right)\ \Rightarrow\ D_{SL}=\frac{\sigma^2}{\left(1+\frac P{\sigma_N^2}\right)^{1/R_{sc}}}.\qquad(6.6.10)$$
- 【口頭】這裡 $\sigma^2$ 是 **source** 本身的 variance，不是雜訊。
- 這個例子照理是達得到的：source 是連續的、channel 輸入可以是高斯（capacity 公式要求高斯輸入）。【口頭】代公式就好，不是重點。

---

## 7. 例三：二元 source 經 BPSK-AWGN（soft decision）

[▶ 21:03](https://youtu.be/dVBICTIzUBs?t=1263)

【口頭】這才是對的：binary uniform source、Hamming（$D$ = 錯誤率），AWGN，但不做 hard decision（**soft decision**，輸出不量化）。注意上一個 AWGN 的 $\frac12\log(1+\text{SNR})$ 要求高斯輸入——我們送 binary，做不到。現在限制輸入只能送 ±1（每一軸 ±1，實際系統就是這樣）。

**Capacity**：±1 只是平移，row、column 都是 permutation ⇒ symmetric channel ⇒ 達到 capacity 的輸入是 ±1 各 $\frac12$。代進去（Example 6.39，p. 255）：
$$C(P)=\frac P{\sigma_N^2}\log_2e-\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-y^2/2}\log_2\cosh\left(\frac P{\sigma_N^2}+y\sqrt{\frac P{\sigma_N^2}}\right)dy,$$
$\sigma_N^2=\frac{N_0}2$、$P=R_{sc}E_b$、$\gamma_b=\frac{E_b}{N_0}$。Shannon limit：
$$h_b(D_{SL})=1-2\gamma_b\log_2e+\frac1{R_{sc}\sqrt{2\pi}}\int_{-\infty}^\infty e^{-y^2/2}\log_2\cosh\left(2R_{sc}\gamma_b+y\sqrt{2R_{sc}\gamma_b}\right)dy.\qquad(6.6.14)$$
- 【口頭】為什麼除以 $R_{sc}$：兩邊都要是 bits per second。積分沒有 closed form，但寫到這個式子就可以用數值方法**畫圖**——非常重要的圖（Fig. 6.4）。

**Table 6.2**（soft decision 的 Shannon limit，dB）：

| $R_{sc}$ | $D_{SL}=0$ | $10^{-5}$ | $10^{-4}$ | $10^{-3}$ | $10^{-2}$ |
|---|---|---|---|---|---|
| 1/3 | −0.496 | −0.496 | −0.504 | −0.559 | −0.960 |
| 1/2 | 0.186 | 0.186 | 0.177 | 0.111 | −0.357 |
| 2/3 | 1.060 | 1.057 | 1.047 | 0.963 | 0.382 |
| 4/5 | 2.040 | 2.038 | 2.023 | 1.909 | 1.152 |

【口頭】現在通訊基本上設計 rate 1/2 的碼：要達到 $10^{-5}$，SNR 至少 **0.19 dB**（0.186）——這就是一直努力的目標。Rate 1/3（放慢一點）約 **−0.49 dB**。圖上往下剛好是一條很陡的直線。

---

## 8. 五十年的路：從 9.6 dB 到 Shannon limit

[▶ 23:39](https://youtu.be/dVBICTIzUBs?t=1419)

【口頭】達到 $10^{-5}$ 需要的 SNR：
- **不編碼的 BPSK**：約 9.6 dB——離 Shannon limit 9 dB 以上。
- **Convolutional code**：約 6 dB 左右。
- **Trellis coded modulation**：約 4 dB。
- **Concatenated code**（Forney，外太空通訊用）：約 2 dB，還是蠻遠。
- **Turbo code（1993）**：在一個 conference 發表，沒有理論，只有模擬。碼很長：長度 65536、rate 1/3，老師說總長度大約 18 萬（之前很少人用這麼長的碼）。（以下**不是逐字稿內容**，是算術檢查：$65536\times3=196{,}608$，約 20 萬；另外課本說達到 0.9 dB 的是 **rate-1/2** 的 turbo code，和老師口述的 rate 1/3 不同，兩邊並列。）模擬結果：$10^{-5}$ 只要 **0.9 dB**；rate 1/2 的 Shannon limit 是 0.19 dB，差約 **0.7 dB**——第一次進到離 Shannon limit 1 dB 以內，是很大的突破。
- **LDPC code（1998）**：MacKay 他們，現在通訊在用的。離 Shannon limit 只有 0.0 幾 dB。經過 50 年的研究，終於在 AWGN 上達到 Shannon capacity。

> ⚠️ 逐字稿缺字：[▶ 24:10](https://youtu.be/dVBICTIzUBs?t=1450) Turbo code 發表的 conference 聽成「WOM」。課本參考文獻 [44] 是 Berrou, Glavieux, Thitimajshima 發表在 **IEEE International Conference on Communications（ICC）** 的論文。課本說 rate-1/2 turbo code 在 $\gamma_b=0.9$ dB 達到 $10^{-5}$，離 Shannon limit 0.186 dB 只有 **0.714 dB**。

【課本補充】LDPC code 最早由 Gallager 提出（課本 [133] 1962、[134] 1963），MacKay 與 Neal 的「Near Shannon limit performance of LDPC codes」（[251]）是 1997 年。老師說的「1998 年 MacKay 他們把 LDPC 發明了」，指的是 LDPC 被重新發現並證明接近 Shannon limit 的那一段。

---

## 9. 一頁速查表

**Lossy JSCC（Thm 6.33）**：stationary ergodic source + DMC，
- $\limsup\frac mnR(D)<C$ ⇒ 可以做到 distortion $D$；任何做到 $D$ 的碼都有 $\frac mnR(D)\le C$。
- 仍是 separation：$R(D)$ 只看 source、$C$ 只看雜訊。Lossless 版本是 $D=0$、$R(0)=H$。
- 時間對齊：$\frac mn=\frac{T_c}{T_s}$ ⇒ $\frac{R(D)}{T_s}<\frac C{T_c}$（bits/s 對 bits/s）。

**Shannon limit**：$R(D_{SL})=\frac C{R_{sc}}$ 的最小 $D$。

**二元 uniform source**：$R(D)=1-h_b(D)$。
- BSC：$D_{SL}=h_b^{-1}\left(1-\frac{1-h_b(\varepsilon)}{R_{sc}}\right)$；hard-decision BPSK：$\varepsilon=Q(\sqrt{2R_{sc}\gamma_b})$。
- Soft decision：$C$ 用 BPSK 輸入的積分式（無 closed form）。
- 數字：rate 1/2、$10^{-5}$：hard 1.772 dB、soft **0.186 dB**；rate 1/3：hard 1.210 dB、soft **−0.496 dB**。

**高斯 source 經 AWGN**：$D_{SL}=\sigma^2\big/\left(1+\frac P{\sigma_N^2}\right)^{1/R_{sc}}$。

**歷史**（rate 1/2、$10^{-5}$）：uncoded 9.6 dB → convolutional ~6 → TCM ~4 → concatenated ~2 → Turbo 0.9 dB（差 0.714 dB）→ LDPC 差 0.0 幾 dB。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Shannon limit 的其他例子（fading channel 等） | 第 31 集（§6.6 下半） |
| Separation 什麼時候不成立；沒有大數法則時的極限 | 第 32–35 集（第二部分） |

---

## 附：本集一句話總結

> **允許失真時，能傳得過去的充要條件是「source 每秒需要的最少 bit 數 $R(D)/T_s$」小於「channel 每秒最多能帶的 bit 數 $C/T_c$」；把它取等號解出的最小失真就是 Shannon limit——rate 1/2 的二元系統在 soft-decision AWGN 上要 $10^{-5}$ 至少要 0.186 dB，而人類花了 50 年，從 9.6 dB 一路靠 Turbo、LDPC 碼逼近到它。**

---

*筆記依據陳伯寧老師「消息理論」Lec30 錄影逐字稿（whisper large-v3-turbo，25:54）與 Alajaji & Chen 課本 §6.5–6.6 整理。*
