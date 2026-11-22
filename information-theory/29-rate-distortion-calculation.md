---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 29
lecture: Lec29 6.4 Calculation of the rate–distortion function：6.4.1 binary source、6.4.2 Gaussian source、Shannon lower bound
date: 待補
video: https://youtu.be/m9TOxLAMCRU
notes: Alajaji & Chen §6.4（pp. 237–247，Theorem 6.23–Observation 6.31）
---

# 第 29 集 · Lec29 §6.4：計算 rate–distortion function（二元 source、高斯 source）[▶ 影片](https://youtu.be/m9TOxLAMCRU)

← 上一集：[28](28-rate-distortion-theorem.md) ｜ [總目錄](README.md) ｜ 下一集：[30](30-lossy-joint-source-channel-coding.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 29 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（18:57，whisper large-v3-turbo）＋ 課本 §6.4（pp. 237–247）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：開頭「作詞文章」是亂碼；「rate–distortion function」聽成「Registration Function／Raditation function／Ratortion function」，「Hamming」聽成「Hemming」，「bit error」聽成「Bit Array」，「distortion」聽成「Detortion／dittortion」，「Gaussian」聽成「高 c」，「Shannon」聽成「Shanen」，「non-Gaussianness」聽成「nongaussian／non-gaussianist」，「LDPC code」聽成「LDP code」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 二元 source + Hamming distortion](#1-二元-source--hamming-distortion)
- [2. 證明：下界 + 硬解達到](#2-證明下界--硬解達到)
- [3. 高斯 source 最難壓縮](#3-高斯-source-最難壓縮)
- [4. 證明：用 dummy 雜訊構造](#4-證明用-dummy-雜訊構造)
- [5. Shannon lower bound 與 non-Gaussianness](#5-shannon-lower-bound-與-non-gaussianness)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

進第二部分之前，算兩個最重要的 rate–distortion function（不需要知道方法，數學上就能算，因為 $R(D)=R^{(I)}(D)$）：
1. **二元 source + Hamming distortion**：$R(D)=h_b(p)-h_b(D)$——$D$ 就是 **bit error rate**，下一集拿來看 Turbo／LDPC code 做到什麼程度。
2. **高斯 source + squared error**：$R(D)=\frac12\log_2\frac{\sigma^2}D$，而且**高斯最難壓縮**（同 variance 的 source 中 $R(D)$ 最大）。

最後講 **Shannon lower bound**，並和第 26 集的 entropy power、non-Gaussianness 連起來。

| 主題 | 課本 |
|---|---|
| 二元 DMS、Hamming | §6.4.1 Theorem 6.23（pp. 238–240） |
| 一般 DMS 的結果 | Theorem 6.24、Observation 6.25（pp. 240–241） |
| 高斯 source 最大化 $R(D)$ | §6.4.2 Theorem 6.26（pp. 241–242） |
| Shannon lower bound | Theorem 6.27（pp. 242–243） |
| 有記憶的高斯 source；Laplacian／absolute error | Observation 6.28、§6.4.3（pp. 243–247） |

---

## 1. 二元 source + Hamming distortion

[▶ 00:00](https://youtu.be/m9TOxLAMCRU?t=0)

**Theorem 6.23**（p. 238）：二元 DMS，$P_Z(0)=p$、$P_Z(1)=1-p$，Hamming distortion：
$$R(D)=\begin{cases}h_b(p)-h_b(D),&0\le D<\min\{p,1-p\};\\0,&D\ge\min\{p,1-p\}.\end{cases}$$
$h_b$ 是 binary entropy function。

【口頭】
- $h_b(p)$ 是原來的資訊量；$D=0$（完全沒有資料損失）最多只能壓到這麼多。允許一點 distortion，就可以**扣掉** $h_b(D)$。
- 扣到 $D=p$（設 $p<\frac12$）時 rate 為 0：根本不用壓縮，接收端隨便產生（例如全 0），distortion 就已經 $\le p$。
- **Hamming distortion 就是錯誤率**：送全 0、收到 0010100000，distortion 是 2（一樣的地方沒有 distortion，不一樣就是 1）。送 10 萬次錯 8 次，平均 distortion 就是 bit error rate。所以 $D$ 就是 **bit error rate**（例如系統要求 $10^{-5}$）——這個公式下一集用來詮釋 Turbo code、LDPC code 的效能。

---

## 2. 證明：下界 + 硬解達到

[▶ 03:02](https://youtu.be/m9TOxLAMCRU?t=182)

設 $p\le\frac12$、$0\le D<p$。

**下界**：對任何滿足 $E[\rho(Z,\hat Z)]\le D$ 的 $P_{\hat Z|Z}$（即 $\Pr\{Z\oplus\hat Z=1\}\le D$），
$$\begin{aligned}
I(Z;\hat Z)&=H(Z)-H(Z|\hat Z)\\
&=h_b(p)-H(Z\oplus\hat Z|\hat Z)\\
&\ge h_b(p)-H(Z\oplus\hat Z)&&(\text{條件拿掉，entropy 只會增加})\\
&\ge h_b(p)-h_b(D)&&(h_b\text{ 在 }[0,\tfrac12]\text{ 遞增，}\Pr\{Z\oplus\hat Z=1\}\le D).
\end{aligned}$$

【口頭】
- 資料傳輸時看的是接收端 $H(Y)-H(Y|X)$；**資料壓縮時傳送端（source）是常數**，所以寫成 $H(Z)-H(Z|\hat Z)$：$H(Z)$ 固定，看能扣掉多少。
- 為什麼 $H(Z|\hat Z)=H(Z\oplus\hat Z|\hat Z)$：給定 $\hat Z$ 時，$Z\mapsto Z\oplus\hat Z$ 只是重新標名字（例如給定 $\hat Z=1$ 時，原本 0、1 的機率 $\frac14,\frac34$ 變成 1、0 的機率），機率沒有改變，entropy 不變。

**達到下界**：$R^{(I)}$ 是最小值，只要找到一個 $P_{\hat Z|Z}$ 讓等號成立。
- 要 $H(Z|\hat Z)=h_b(D)$：令「反向」通道 $P_{Z|\hat Z}(0|0)=P_{Z|\hat Z}(1|1)=1-D$（$Z=\hat Z\oplus N$，$N$ 是 Bernoulli($D$)，和 $\hat Z$ 獨立）。
- 【口頭】就是**解方程式硬解**：有解，lower bound 就達得到；細節課本列得很詳細。課本解出
$$P_{\hat Z|Z}(0|0)=\frac{1-D}{1-2D}\left(1-\frac Dp\right),\qquad P_{\hat Z|Z}(1|1)=\frac{1-D}{1-2D}\left(1-\frac D{1-p}\right).$$

> 以下**不是逐字稿內容**，是依課本的構造推論的等價寫法：反向通道是 crossover $D$ 的 BSC，$\hat Z$ 的分布要滿足 $P_{\hat Z}(0)(1-D)+P_{\hat Z}(1)D=p$，即 $P_{\hat Z}(0)=\frac{p-D}{1-2D}$；$D<p\le\frac12$ 時它落在 $[0,1]$，所以解存在。

**$D\ge p$**：讓 $\hat Z$ 和 $Z$ 獨立，找最好的獨立分布——永遠輸出比較常見的符號（$p\le\frac12$ 時 $\hat Z\equiv1$），distortion $=\Pr(Z=0)=p=\min\{p,1-p\}\le D$，$I=0$。

【課本補充】Theorem 6.24（p. 240）：一般 DMS 在 Hamming distortion 下，$R(D)\ge H(Z)-D\log_2(|\mathcal Z|-1)-h_b(D)$，在 $D$ 夠小時等號成立；二元時就化成 Theorem 6.23。

---

## 3. 高斯 source 最難壓縮

[▶ 06:06](https://youtu.be/m9TOxLAMCRU?t=366)

**Squared error distortion**（也是 additive）：個別相減的平方和——聲音或畫面的能量差。

**Theorem 6.26（Gaussian sources maximize the rate–distortion function）**（p. 241）：squared error 下，任何連續無記憶 source（support $\mathbb R$、mean 0、variance $\sigma^2$、differential entropy 有限）
$$R(D)\le\begin{cases}\frac12\log_2\frac{\sigma^2}D,&0<D\le\sigma^2;\\0,&D>\sigma^2,\end{cases}$$
**等號在 source 是高斯**時成立。

【口頭】
- 相同 variance（相同能量）下，**高斯最難壓縮**：例如別的 source 每個符號要 0.2 bit（100 次 20 bit），高斯要 0.3 bit（30 bit），才達到一樣的 distortion。因為高斯最豐富——和「高斯有最大的 differential entropy」是同一件事。
- $D$ 越小，$\frac{\sigma^2}D$ 越大，rate 增加得非常快（log 的行為、很 sharp）：要求越高，rate 越高。
- **$D=0$ 時 rate 無限大**：連續 source 要精確恢復，沒辦法壓縮。但只要給一點點 $D$（例如 0.1），rate 就是有限的。
- **單位**：$D$ 來自 squared error 的期望值，單位是**能量**；$\frac{\sigma^2}D$ 是同單位相除，取 log 才是 rate。

---

## 4. 證明：用 dummy 雜訊構造

[▶ 09:44](https://youtu.be/m9TOxLAMCRU?t=584)

**上界**（任何 source）：$R(D)=R^{(I)}(D)$ 是最小的 mutual information，所以**任取**一個滿足限制的 $f_{\hat Z|Z}$ 都是上界：$R(D)\le I(f_Z,f_{\hat Z|Z})$。

**構造**（$0<D\le\sigma^2$）：令 $a=1-\frac D{\sigma^2}$，取和 $Z$ 獨立的 dummy 高斯 $W\sim\mathcal N(0,aD)$，定義
$$\hat Z=aZ+W.$$
- 【口頭】這是**純數學**的構造，和怎麼壓縮無關：把壓縮看成「輸入 $Z$ 乘一個常數、加一個獨立雜訊得到輸出」的 additive channel。放 $a$ 是為了**調 distortion**。
- Distortion：$\hat Z-Z=(a-1)Z+W$，$Z$、$W$ 獨立，所以
$$E[(Z-\hat Z)^2]=(1-a)^2\sigma^2+aD=\frac{D^2}{\sigma^2}+D-\frac{D^2}{\sigma^2}=D.\ \checkmark$$
- $\mathrm{Var}(\hat Z)=a^2\sigma^2+aD=a(a\sigma^2+D)=a\sigma^2=\sigma^2-D$。

**計算**：
$$\begin{aligned}
R(D)\le I(Z;\hat Z)&=h(\hat Z)-h(\hat Z|Z)=h(\hat Z)-h(W+aZ|Z)\\
&=h(\hat Z)-h(W|Z)&&(\text{平移不變})\\
&=h(\hat Z)-h(W)&&(W\text{、}Z\text{ 獨立})\\
&=h(\hat Z)-\tfrac12\log_2(2\pi e\,aD)\\
&\le\tfrac12\log_2\left(2\pi e(\sigma^2-D)\right)-\tfrac12\log_2(2\pi e\,aD)&&(\text{同 variance 高斯 }h\text{ 最大})\\
&=\tfrac12\log_2\frac{\sigma^2-D}{(1-D/\sigma^2)D}=\tfrac12\log_2\frac{\sigma^2}D.
\end{aligned}$$
- 【口頭】要 rate 越小，減掉的 $h(W)$ 要越大 ⇒ $W$ 選**高斯**（最豐富的 differential entropy）。
- **等號**：$\hat Z$ 是高斯。$Z$ 是高斯、$W$ 是高斯 ⇒ $\hat Z=aZ+W$ 是高斯。（高斯 source 的下界／達到性，課本另外證明。）

**$D>\sigma^2$**：讓 $\hat Z\equiv0$（和 $Z$ 獨立），$E[(Z-\hat Z)^2]=\sigma^2<D$，$I=0$。【口頭】distortion 要求比能量還寬鬆，接收端隨機亂產生就滿足，根本不用送。

---

## 5. Shannon lower bound 與 non-Gaussianness

[▶ 14:54](https://youtu.be/m9TOxLAMCRU?t=894)

**Theorem 6.27（Shannon lower bound，squared error）**（p. 242）：
$$R(D)\ge h(Z)-\frac12\log_2(2\pi eD).$$
- 上界 $\frac12\log_2\frac{\sigma^2}D$、下界 $h(Z)-\frac12\log_2(2\pi eD)$；**$Z$ 是高斯時兩者相等**（$h(Z)=\frac12\log_2(2\pi e\sigma^2)$）。

**和 entropy power、non-Gaussianness 連起來**【口頭】（第 26 集）：
- 加性雜訊 $I=h(Y)-h(Z)$，真正影響傳輸量的是 $h(Z)$，不是實體能量 $E[Z^2]$。Entropy 是傳輸量（rate），所以 **entropy power** $\frac1{2\pi e}2^{2h(Z)}$ 是「影響傳輸量的等效能量」。兩個獨立雜訊相加，實體能量相加，但 entropy power 會增加更多（EPI）。
- **Non-Gaussianness**：同 variance 高斯的 differential entropy 減掉實際的 $h(Z)$（等於 $D(Z\|Z_G)$），單位是 rate。
- 放到壓縮：上下界的差
$$\frac12\log_2\frac{\sigma^2}D-\left(h(Z)-\frac12\log_2(2\pi eD)\right)=\frac12\log_2(2\pi e\sigma^2)-h(Z)=D(Z\|Z_G).$$
  所以 $R_G(D)-D(Z\|Z_G)\le R(D)\le R_G(D)$：**越不像高斯越好壓**，最多可以少掉一個 non-Gaussianness。
- 【口頭】這些是 Verdú 他們用來直觀詮釋「碰到的雜訊或 source 不像高斯」時會有什麼現象。

> 以下**不是逐字稿內容**，是依 Theorem 6.26–6.27 與第 26 集的 $D(Z\|Z_G)=\frac12\log_2(2\pi e\sigma^2)-h(Z)$ 推論的上式。

【課本補充】
- Observation 6.28：有記憶的 stationary Gauss–Markov source（variance 1、$K_X(\tau)=a^{|\tau|}$），$D\le\frac{1-a}{1+a}$ 時 $R(D)=\frac12\log_2\frac{1-a^2}D$。
- §6.4.3：absolute error distortion 下，Laplacian source 扮演高斯的角色（Theorem 6.29 最大化 $R(D)$），也有對應的 Shannon lower bound（Theorem 6.30）。

---

## 6. 一頁速查表

**二元 source + Hamming（Thm 6.23）**：$R(D)=h_b(p)-h_b(D)$（$D<\min\{p,1-p\}$），否則 0。$D$ = bit error rate。
- 下界：$I=h_b(p)-H(Z\oplus\hat Z|\hat Z)\ge h_b(p)-H(Z\oplus\hat Z)\ge h_b(p)-h_b(D)$。
- 達到：反向 BSC($D$)，$P_{\hat Z}(0)=\frac{p-D}{1-2D}$。

**高斯 + squared error（Thm 6.26）**：任何 variance $\sigma^2$ 的 source $R(D)\le\frac12\log_2\frac{\sigma^2}D$（$D\le\sigma^2$），高斯時等號——**高斯最難壓縮**。
- 構造：$\hat Z=aZ+W$，$a=1-\frac D{\sigma^2}$，$W\sim\mathcal N(0,aD)$；$E(Z-\hat Z)^2=D$，$\mathrm{Var}\hat Z=\sigma^2-D$；$I=h(\hat Z)-h(W)\le\frac12\log_2\frac{\sigma^2-D}{aD}=\frac12\log_2\frac{\sigma^2}D$。
- $D\to0$：rate $\to\infty$（連續 source 不能無損壓縮）；$D>\sigma^2$：rate 0。

**Shannon lower bound（Thm 6.27）**：$R(D)\ge h(Z)-\frac12\log_2(2\pi eD)$；上下界差 $=D(Z\|Z_G)$（non-Gaussianness）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $rR(D)<C$ 的有損 joint source–channel coding | 第 30 集（§6.5） |
| $h_b(p)-h_b(D)$ 和 BSC／AWGN capacity 合起來 → Shannon limit（BER vs $E_b/N_0$） | 第 31 集（§6.6） |
| 高斯 source 經 AWGN：$\frac12\log\frac{\sigma^2}D\le\frac12\log(1+\text{SNR})$ | 第 31 集 |

---

## 附：本集一句話總結

> **二元 source 在 Hamming（錯誤率）distortion 下 $R(D)=h_b(p)-h_b(D)$，靠「條件拿掉 entropy 變大」得下界、解方程式得達到；同 variance 的連續 source 在 squared error 下 $R(D)\le\frac12\log_2(\sigma^2/D)$，高斯時等號——高斯最難壓縮，越不像高斯越好壓，差距就是 non-Gaussianness。**

---

*筆記依據陳伯寧老師「消息理論」Lec29 錄影逐字稿（whisper large-v3-turbo，18:57）與 Alajaji & Chen 課本 §6.4 整理。*
