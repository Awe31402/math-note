---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 12
lecture: Lec 9-3 General Concepts — The Power Spectrum (1/3)
date: 待補
video: https://youtu.be/FQ9njBn5TLE
notes: Papoulis & Pillai 4th ed. §9-3（定義 式 (9-133)–(9-138)，pp. 408–409；任意正函數都是功率頻譜 式 (9-139)–(9-141)、Example 9-24 Doppler effect 式 (9-142)，pp. 410–411；Theorem 9-4 式 (9-146)–(9-152)，pp. 412–413；Example 9-28 Hilbert transforms、analytic signal，式 (9-158)–(9-162)，pp. 415–416；Wiener–Khinchin theorem 式 (9-163)–(9-165)，p. 416）
---

# 第 12 集 · Lec 9-3 (1/3)：功率頻譜、用頻率分布造訊號（都卜勒效應）、轉移函數、Hilbert 轉換、Wiener–Khinchin 定理 [▶ 影片](https://youtu.be/FQ9njBn5TLE)

← 上一集：[11](11-time-varying-fundamental-theorem-linear-systems.md) ｜ [總目錄](README.md) ｜ 下一集：[13](13-integrated-spectrum-nnd-necessary-exclusion-ms-equality.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 12 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（1:03:34，whisper large-v3-turbo）＋ Papoulis §9-3（pp. 408–416）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「傅立葉轉換」→「負列轉換／複裂轉換／复理的转换／Fullet Transform」，「時域」→「title 面／tine domain／Tile domain」，「實數」→「時數」，「實部／虛部」→「實步／虛步」，「一階可微」→「一接可為／可圍」，「wide-sense stationary」→「Y線 stationary／Wisen stationary」，「Poisson」→「poison」，「autocorrelation」→「autochaline／autochrome／autocornion function」，「lemma」→「Lema／Lamma／lama」，「Doppler」→「都布勒／都博勒／杜卜勒／多普勒」，「調變」→「條變」，「相位」→「向位」，「projected velocity」→「Protected Velocity」，「distribution」→「DETTRIBUTION」，「weighting」→「waiting」，「Hilbert」→「Huber／Hugh-Hilbert」，「quadrature」→「quadrature」，「all-pass」→「all parts」，「magnitude response」→「magnetive response」，「Wiener–Khinchin」→「Wiener-Kinchentheir」，「characteristic function」→「Characterize Function」，「nonnegative」→「non-negative／negative」（最後一句「的確是 negative」應為 nonnegative），「extended Fourier transform」→「Extended Fluidium／Fluoration／friction form」。以下一律用正確的字。

> **接上一集**：上一集的基本定理是在**時域**做卷積，很難產生直覺。這一節（§9-3）到**頻譜**上看：卷積變相乘，這是直覺培養最重要的地方。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 功率頻譜的定義](#1-功率頻譜的定義)
  - [1.1 定義與兩種傅立葉記號](#11-定義與兩種傅立葉記號)
  - [1.2 功率頻譜一定是實數](#12-功率頻譜一定是實數)
  - [1.3 互功率頻譜](#13-互功率頻譜)
- [2. 例：電報訊號的頻譜，與「平滑 ↔ 衰減」](#2-例電報訊號的頻譜與平滑--衰減)
- [3. 協方差頻譜](#3-協方差頻譜)
- [4. 引理：任何非負可積函數都是某個訊號的功率頻譜](#4-引理任何非負可積函數都是某個訊號的功率頻譜)
- [5. 應用：都卜勒效應](#5-應用都卜勒效應)
- [6. 線性系統的頻譜版本（Theorem 9-4）](#6-線性系統的頻譜版本theorem-9-4)
- [7. 轉移函數與 extended Fourier transform](#7-轉移函數與-extended-fourier-transform)
- [8. Hilbert 轉換與解析訊號](#8-hilbert-轉換與解析訊號)
- [9. Wiener–Khinchin 定理：功率頻譜非負](#9-wienerkhinchin-定理功率頻譜非負)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 功率頻譜、互頻譜 | [▶ 00:30](https://youtu.be/FQ9njBn5TLE?t=30) | 式 (9-133)–(9-137)，p. 408 |
| 電報訊號例子、協方差頻譜 | [▶ 06:41](https://youtu.be/FQ9njBn5TLE?t=401) | Example 9-22、式 (9-138)，p. 409 |
| 引理、都卜勒效應 | [▶ 12:22](https://youtu.be/FQ9njBn5TLE?t=742) | 式 (9-139)–(9-142)，pp. 410–411 |
| Theorem 9-4 | [▶ 31:16](https://youtu.be/FQ9njBn5TLE?t=1876) | 式 (9-146)–(9-149)，p. 412 |
| 轉移函數、extended FT | [▶ 39:29](https://youtu.be/FQ9njBn5TLE?t=2369) | 無（【口頭】） |
| Hilbert 轉換 | [▶ 48:10](https://youtu.be/FQ9njBn5TLE?t=2890) | Example 9-28，pp. 415–416 |
| Wiener–Khinchin | [▶ 57:25](https://youtu.be/FQ9njBn5TLE?t=3445) | 式 (9-163)–(9-165)，p. 416 |

---

## 1. 功率頻譜的定義

### 1.1 定義與兩種傅立葉記號

[▶ 00:30](https://youtu.be/FQ9njBn5TLE?t=30)

> **功率頻譜** (power spectrum)，更精確叫**功率頻譜密度** (power spectral density，PSD)：WSS 過程的自相關函數的傅立葉轉換
> $$S_{XX}(\omega)=\int_{-\infty}^{\infty}R_{XX}(\tau)\,e^{-j\omega\tau}\,d\tau,\qquad R_{XX}(\tau)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S_{XX}(\omega)\,e^{j\omega\tau}\,d\omega.$$

- **密度**：它的積分給你訊號的**功率**。它把整個訊號的功率分散到各個頻率上：1 kHz 有多少、1.1 kHz 有多少、1.2 kHz 有多少，全部列出來。
- 有了它就能選擇讓某些頻率通過、濾掉其他頻率——這就是**濾波器**的基本概念：針對頻率來濾。
- 隱含假設 **WSS**：自相關只跟 $\tau$ 有關。

**記號**【口頭】：老師教數位通訊時喜歡用 $e^{-j2\pi f\tau}$，$f$ 的單位就是頻率，反轉換**沒有常數**，比較對稱。但很多書（包括課本）用 $\omega=2\pi f$，反轉換要多一個 $\frac{1}{2\pi}$。這門課跟課本用 $\omega$，記得反轉換要加 $\frac{1}{2\pi}$。

### 1.2 功率頻譜一定是實數

[▶ 02:35](https://youtu.be/FQ9njBn5TLE?t=155)

由期望值的定義：
$$R_{XX}(-\tau)=E\left[X(t-\tau)X^*(t)\right]=\left(E\left[X(t)X^*(t-\tau)\right]\right)^*=R_{XX}^*(\tau).$$

- 一個時域函數滿足 $R(-\tau)=R^*(\tau)$（**共軛對稱**）⇔ 它的頻譜是**純實數**（if and only if）。
- 符合期望：它代表每個頻率的**能量**。能量是實數（老師說虛數能量「好像暗黑界的能量從某個地方冒出來」）。之後還會證明它**非負**（第 9 節）：能量要嘛 0、要嘛有。【口頭】

**實數過程**：$R(\tau)$ 純實數且**偶函數**（左右對稱）⇒ 頻譜也純實數、左右對稱，只要算一半：
$$S(\omega)=2\int_0^{\infty}R(\tau)\cos\omega\tau\,d\tau,\qquad R(\tau)=\frac{1}{\pi}\int_0^{\infty}S(\omega)\cos\omega\tau\,d\omega.$$
- 前面乘 2 是因為另一半完全一樣；反轉換 $\frac{2}{2\pi}=\frac1\pi$。
- 只取 $\cos$：$e^{-j\omega\tau}=\cos\omega\tau-j\sin\omega\tau$，對稱時 $\sin$（虛部）兩邊的積分抵消。實數世界只要做 **cosine transform**。

【課本補充】式 (9-133)–(9-135)，p. 408。

### 1.3 互功率頻譜

[▶ 06:11](https://youtu.be/FQ9njBn5TLE?t=371)

> **互功率頻譜** (cross-power spectrum)：$S_{XY}(\omega)=\int R_{XY}(\tau)e^{-j\omega\tau}d\tau$，$R_{XY}(\tau)=E[X(t+\tau)Y^*(t)]$。

- 用來看輸入和輸出的頻譜關係。
- 上一集基本定理的 $R_{XX}$ 有 $t_1,t_2$；這裡只有 $\tau=t_1-t_2$，因為假設**聯合 WSS**。

【課本補充】$S_{XY}$ 一般是複數（即使 $X$、$Y$ 是實數）；$S_{XY}(\omega)=S_{YX}^*(\omega)$（式 (9-137)）。

---

## 2. 例：電報訊號的頻譜，與「平滑 ↔ 衰減」

[▶ 06:41](https://youtu.be/FQ9njBn5TLE?t=401) 電報訊號（Poisson 點做 $\pm1$ 對應）的自相關 $R(\tau)=e^{-2\lambda|\tau|}$。

**先預期**：$R$ 對 $\tau=0$ 對稱、純實數 → 頻譜應該對 $\omega=0$ 對稱、純實數。算出來：
$$S(\omega)=\int_{-\infty}^{\infty}e^{-2\lambda|\tau|}e^{-j\omega\tau}d\tau=2\int_0^\infty e^{-2\lambda\tau}\cos\omega\tau\,d\tau=\frac{4\lambda}{4\lambda^2+\omega^2}.$$
的確對 $\omega=0$ 對稱。

（老師說的是半隨機電報訊號；它的平均 $e^{-2\lambda t}$ 隨時間變，嚴格說不是 WSS。課本 Example 9-22 用的是**隨機**電報訊號，自相關相同，是 WSS。）

**平滑 ↔ 衰減** [▶ 07:45](https://youtu.be/FQ9njBn5TLE?t=465)【口頭】：

- $R(\tau)=e^{-2\lambda|\tau|}$ 在 $\tau=0$ **不可微**（有尖角）。所以 $\int\omega\,S(\omega)\,d\omega$ 會衝到無限大：頻譜在 $\omega\to\infty$ 衰減得不夠快（這裡 $S\sim 4\lambda/\omega^2$）。
- 傅立葉轉換的對稱性：**時域的某一點，反映到頻譜的無限遠處（尾巴，tail）**；**頻譜的某一點，反映到時域的無限遠處**。
  - $\tau=0$ 的平滑度 ↔ $\omega\to\infty$ 的衰減。
  - $\omega=0$ 的平滑度 ↔ $\tau\to\infty$ 的衰減。這裡 $S$ 在 $\omega=0$ 非常可微，所以 $\int R(\tau)\,\tau\,d\tau$ 一定有限。
- 時域一階可微、二階不可微 → 頻譜乘 $\omega^2$ 就爆掉（衰減慢）。
- **設計直覺**：政府只給你 10 MHz 的頻段，你希望能量集中在裡面、外面衰減很快，例如像 $\frac{1}{\omega^6}$。那 $R(\tau)$ 在原點要夠多階可微；原點的可微階數不夠，頻譜百分之百達不到那個衰減速度。老師說機率的書上有比較完整的證明。

---

## 3. 協方差頻譜

[▶ 10:18](https://youtu.be/FQ9njBn5TLE?t=618)

> **協方差頻譜** (covariance spectrum)：自協方差 $C(\tau)$ 的傅立葉轉換 $S^c(\omega)$。

- 有些書甚至把它定義成功率頻譜（第 5 集 Gray & Davisson），老師覺得有點怪，所以強調叫 covariance spectrum 比較清楚。
- WSS 時平均 $\eta$ 是常數，$R(\tau)=C(\tau)+|\eta|^2$。常數的傅立葉轉換是脈衝：$\mathcal{F}\{1\}=2\pi\delta(\omega)$（用 $\omega$ 記號，反轉換有 $\frac1{2\pi}$，所以多一個 $2\pi$）：
$$S(\omega)=S^c(\omega)+2\pi|\eta|^2\delta(\omega).$$
- 會算功率頻譜，協方差頻譜就是扣掉一個脈衝。

【課本補充】式 (9-138)，p. 409。Example 9-23：Poisson 脈衝 $R_Z(\tau)=\lambda^2+\lambda\delta(\tau)$（上一集），所以 $S_Z(\omega)=\lambda+2\pi\lambda^2\delta(\omega)$，$S_Z^c(\omega)=\lambda$。

---

## 4. 引理：任何非負可積函數都是某個訊號的功率頻譜

[▶ 12:22](https://youtu.be/FQ9njBn5TLE?t=742) 一般書上沒特別介紹，但老師覺得很好用。他稱為 **lemma**（不夠大到叫定理；有些論文會叫 **observation**，一個很敏銳的觀察）。

> **引理**：給任何**非負**、**可積**的函數 $S(\omega)$，一定能造出一個 WSS 訊號，功率頻譜就是 $S(\omega)$。做法：
> $$X(t)=a\,e^{j(\omega t-\varphi)},$$
> - $a$ 是常數，$a^2=\frac{1}{2\pi}\int S(\omega)\,d\omega$（就是總功率 $R(0)$）；
> - $\omega$ 是隨機變數，**密度** $f_\omega(\omega)=\frac{S(\omega)}{2\pi a^2}$（也就是用你的功率頻譜當密度，正規化成總面積 1）；
> - $\varphi$ 在 $(-\pi,\pi)$ 均勻，和 $\omega$ 獨立。

- **可積**：總面積代表功率，我們看的訊號功率不會是無限大，所以是有限能量的訊號。
- **$a=0$ 的情形**（為了證明完整）：$a^2$ 是 $S$ 的積分；$S$ 非負又積分為 0，就是處處為 0。這時 $\omega$ 是什麼都沒關係，$X\equiv 0$，頻譜就是 0。
- **驗證**：算自相關。由第 8 集，$R_X(\tau)=a^2E\{e^{j\omega\tau}\}=a^2\int f_\omega(\omega)e^{j\omega\tau}d\omega$，所以由傅立葉轉換的唯一性，$S_X(\omega)=2\pi a^2f_\omega(\omega)=S(\omega)$。

**實數對稱版**：若 $S$ 還是**偶函數**，就不用產生有實部有虛部的訊號：
$$Y(t)=a\cos(\omega t+\varphi),\qquad f_\omega(\omega)=\frac{S(\omega)}{\pi a^2}\quad\left(\text{即 }a^2=\tfrac{1}{\pi}\textstyle\int S(\omega)\,d\omega\right).$$

**$\varphi$ 的角色** [▶ 19:00](https://youtu.be/FQ9njBn5TLE?t=1140)：只是為了造成 **WSS**——讓平均是常數（0）。如果不需要這個條件，$\varphi$ 可以拿掉。

**意義**【口頭】：

- 這不是唯一的做法，但剛好符合通訊的概念：通訊幾乎都產生 $Ae^{j(\omega t-\varphi)}$。$\omega$ 隨機就是 FM（數位通訊的 FSK），$\varphi$ 隨機就是 PM。
- **功率頻譜就是頻率 $\omega$ 的 PDF**（乘上常數）。兩者息息相關。
- 例：要在某個 10 MHz 範圍產生某個形狀的功率頻譜，就做一個載波，讓它的頻率分布長成那個形狀。

【課本補充】式 (9-139)–(9-141)，p. 410。課本 $\varphi$ 取在 $(0,2\pi)$ 均勻（和 $(-\pi,\pi)$ 等價）。

---

## 5. 應用：都卜勒效應

[▶ 20:00](https://youtu.be/FQ9njBn5TLE?t=1200) 都卜勒效應就是因為移動、距離變化造成的**頻率偏移**。頻率有一個分布，由上面的引理，**這個分布的形狀就是功率頻譜**。不用再算了。

**設定**：接收端固定，發射端以速度 $v$ 移動，運動方向和「發射端到接收端的直線」夾角 $\theta$。取**投影速度** (projected velocity) $v_x=v\cos\theta$。發射單頻訊號 $e^{j\omega_0t}$（harmonic oscillator），收到
$$s(t)=a\,e^{j\omega_0(t-r/c)},\qquad r=r_0+v_xt,\quad c=\text{光速（傳播速度）}.$$

展開：
$$s(t)=a\,e^{j(\omega t-\varphi)},\qquad\omega=\omega_0\left(1-\frac{v\cos\theta}{c}\right),\quad\varphi=\frac{r_0\omega_0}{c}.$$

**是不是 WSS？** 不是：$\varphi$ 是常數不是均勻分布，所以平均隨時間變。但自相關 $R(\tau)=a^2E\{e^{j\omega\tau}\}$ 只跟 $\tau$ 有關。如果不在乎平均這個條件，還是可以把功率頻譜定義成自相關的傅立葉轉換：
$$S(\omega)=2\pi a^2f_\omega(\omega).$$

**由 $v$ 的分布求 $\omega$ 的分布** [▶ 25:10](https://youtu.be/FQ9njBn5TLE?t=1510)：老師習慣**從 CDF 著手**，不從 PDF，這樣絕對不會錯。（以下以 $\cos\theta=1$、$v$ 即投影速度。）

$$F_\omega(w)=P\left\{\omega_0\left(1-\frac{v}{c}\right)\le w\right\}=P\left\{v\ge c\left(1-\frac{w}{\omega_0}\right)\right\}=1-F_v\left(c\left(1-\frac{w}{\omega_0}\right)\right).$$
微分：
$$f_\omega(w)=\frac{c}{\omega_0}f_v\left(c\left(1-\frac{w}{\omega_0}\right)\right),\qquad S(\omega)=\frac{2\pi a^2c}{\omega_0}f_v\left[\left(1-\frac{\omega}{\omega_0}\right)c\right].$$

**解讀**【口頭】：

- 頻率在變化時，功率頻譜就做完全一樣的變化。看到功率頻譜這樣變化、訊號又是通訊的樣子，就可以大膽想像頻率確實有類似的變化。
- 例：政府給你 200 kHz，你量到左右偏 10 kHz，就表示震盪頻率有 10 kHz 的變化。現在知道更多：**那個變化的機率，就是功率頻譜的形狀**。

**三個情況**：

1. **速度均勻分布**：例如時速 100 到 120 公里之間任何速度都可能。$v$ 均勻 → $\omega$ 在兩個常數之間均勻 → 頻譜是一塊**平的寬度**，高度是兩端差的倒數（乘常數）。隨機運動會**展寬** (broaden) 頻譜。
2. **定速**：例如定速 110 公里。$\omega$ 是常數，PDF 是脈衝 → 頻譜也是一個脈衝 $2\pi a^2\delta\left(\omega-\omega_0(1-v/c)\right)$，只是偏移了。靠近、遠離頻率都會偏，但偏移量是常數。確定的運動只造成頻譜**平移** (shift)。
3. **$\cos\theta=0$**：移動方向和波的方向垂直，沒有都卜勒效應，不管速度隨機或固定，都是不偏移的脈衝。

【課本補充】Example 9-24，式 (9-142)，pp. 410–411，Fig. 9-12（發射頻譜是 $\omega_0$ 的脈衝，接收頻譜被展寬）。課本另一例：發射端是溫度 $T$ 的氣體中的粒子，$v_x$ 是零平均、變異數 $kT/m$ 的常態，則
$$S(\omega)=\frac{2\pi a^2c}{\omega_0\sqrt{2\pi kT/m}}\exp\left\{-\frac{mc^2}{2kT}\left(1-\frac{\omega}{\omega_0}\right)^2\right\}.$$

---

## 6. 線性系統的頻譜版本（Theorem 9-4）

[▶ 31:16](https://youtu.be/FQ9njBn5TLE?t=1876) 卷積在腦中很難心算，但兩個頻譜相乘，腦中總有個雛形。要把上一集的基本定理改成 WSS 版本：令 $t_1=t+\tau$、$t_2=t$，只看差。

**為什麼出現 $h^*(-\tau)$？** [▶ 32:46](https://youtu.be/FQ9njBn5TLE?t=1966)

- 互相關先對 $t_2$ 卷積：$R_{XX}(t_1,t_2-u)$，只看差就是 $R_{XX}(\tau+u)$，變成「加」。
- 但卷積習慣把 $h$ 當**加權**、訊號寫成「減」。令 $u'=-u$，就寫成 $R_{XX}(\tau-u')$，加權變成 $h^*(-u')$。
- 所以第一次卷積的加權是 $h^*(-\tau)$。很多書都這樣寫，現在知道為什麼，不是公式背下來的。

> **Theorem 9-4**（LTI 系統，輸入 WSS）：
> $$R_{XY}(\tau)=R_{XX}(\tau)*h^*(-\tau),\qquad R_{YY}(\tau)=R_{XY}(\tau)*h(\tau),$$
> $$S_{XY}(\omega)=S_{XX}(\omega)H^*(\omega),\qquad S_{YY}(\omega)=S_{XY}(\omega)H(\omega)=S_{XX}(\omega)\left|H(\omega)\right|^2.$$

- 時域卷積一次 = 頻譜相乘一次；$h^*(-\tau)$ 的傅立葉轉換是 $H^*(\omega)$。
- 老師的版本還允許 $h$ 隨機（取期望值）和時變。

**頻率偏移（調變）** [▶ 35:54](https://youtu.be/FQ9njBn5TLE?t=2154)：老師的版本有一個 $e^{j\omega_0t}$ 的時變因子（像上一集的例子），輸出頻譜會**往右平移 $\omega_0$**——都卜勒效應（或調變）就出來了。

以下**不是逐字稿內容**，是依上一集的例子推的（投影片公式逐字稿沒唸全）：若 $h(\tau;t)=h(\tau)e^{j\omega_0t}$，則 $Y(t)=e^{j\omega_0t}\left(h*X\right)(t)$，所以
$$R_{YY}(\tau)=e^{j\omega_0\tau}R_{Y_0Y_0}(\tau),\qquad S_{YY}(\omega)=S_{XX}(\omega-\omega_0)\left|H(\omega-\omega_0)\right|^2,$$
其中 $Y_0=h*X$。

**口訣**（golden rule）【口頭】：**時域做相位旋轉 = 頻譜做平移**；反過來，頻譜做相位旋轉 = 時域做平移。頻譜有平移，時域一定有相位旋轉。調變和都卜勒效應是同一件事：都卜勒是自然界幫你做的調變。

【課本補充】Papoulis Theorem 9-4，式 (9-146)、(9-147)，p. 412。證明：(9-145) 取共軛乘以 $X(t+\tau)$、取期望值，$E\{X(t+\tau)X^*(t-\alpha)\}=R_{XX}(\tau+\alpha)$，得 $R_{XY}(\tau)=\int R_{XX}(\tau+\alpha)h^*(\alpha)d\alpha=\int R_{XX}(\tau-\beta)h^*(-\beta)d\beta$。推論 (9-148)–(9-150)：$R_{YY}=R_{XX}*\rho$，$\rho(\tau)=h(\tau)*h^*(-\tau)\leftrightarrow|H(\omega)|^2$。白雜訊輸入 $S_{XX}=q$：$S_{YY}=q|H|^2$（式 (9-151)）。

---

## 7. 轉移函數與 extended Fourier transform

[▶ 39:29](https://youtu.be/FQ9njBn5TLE?t=2369)

> **轉移函數** (transfer function)：脈衝響應 $h(\tau)$ 的傅立葉轉換 $H(\omega)$。頻譜上
> $$Y(\omega)=H(\omega)\,X(\omega).$$

- 輸入的每個頻率乘上不同的**加權** $H(\omega)$，不用卷積，直接相乘。
- 直覺：輸入頻譜一個形狀、濾波器一個形狀（例如帶通的方塊），點對點相乘：濾波器是 0 的地方全部消掉，只留下通過的那一塊。形狀不用算就大概知道。
- 名詞：$h(\tau)$ 叫 impulse response；$H(\omega)$ 叫 transfer function；$|H(\omega)|$ 叫 magnitude response。各種名詞其實指同一件事的不同面向。

**只要是這個形式就一定是線性**：送 $X_1$ 得 $Y_1$、送 $X_2$ 得 $Y_2$，則送 $aX_1+bX_2$ 得 $H(aX_1+bX_2)=aY_1+bY_2$。

**比卷積更廣** [▶ 43:04](https://youtu.be/FQ9njBn5TLE?t=2584)：微分器沒有脈衝響應（第 10 集），但在頻譜上可以說它有轉移函數 $H(\omega)=j\omega$。$j\omega$ 的絕對值積分不是有限的，嚴格說沒有傅立葉反轉換；但觀念上可以這樣用。若 $H(\omega)$ 的反轉換存在，時域卷積 ⇔ 頻譜相乘（if and only if）。

**傅立葉轉換存在的條件** [▶ 44:04](https://youtu.be/FQ9njBn5TLE?t=2644)（嚴謹的版本）：

1. 絕對可積：$\int|g(t)|\,dt<\infty$。
2. 在任何有限區間內，局部極大值、局部極小值、不連續點都是**有限個**。

反例：$g(t)=1$（$t$ 不是有理數）、$0$（其他）——不連續點有無限多個，沒辦法討論它的傅立葉轉換。

> **extended Fourier transform**（延伸的傅立葉轉換）：$g$ 的傅立葉轉換不存在時，找一串「好的」函數 $g_n\to g$，它們的傅立葉轉換 $G_n(\omega)$ 存在，定義
> $$G(\omega)=\lim_{n\to\infty}G_n(\omega).$$

- 不是 well-defined 的方法，是**方便法門**，但在很多地方有用。
- 最常用：乘上指數 $e^{-|t|/n}$ 把爆掉的函數壓下來。例：$1$ 沒有傅立葉轉換（總面積不有限），但 $\mathcal{F}\{e^{-|t|/n}\}=\frac{2/n}{1/n^2+\omega^2}\to 2\pi\delta(\omega)$，所以說 $\mathcal{F}\{1\}=2\pi\delta(\omega)$。
- 漏洞：極限從不同方向逼近可能不一樣，extended FT 可能有好幾個。工程上問題不大，因為大家都用同樣的指數方式逼近。
- 微分器 $j\omega$ 以 $|\omega|$ 線性增加，乘上指數就壓下來了。

---

## 8. Hilbert 轉換與解析訊號

[▶ 48:10](https://youtu.be/FQ9njBn5TLE?t=2890) 時域和頻域都不符合傅立葉轉換的要求，要用 extended FT。因為很有用、Hilbert 有貢獻，取名 **Hilbert transform**（不只是某個特定的轉移函數）。

> **Hilbert 轉換**（quadrature filter，正交濾波器）：
> $$H(\omega)=-j\,\text{sgn}\,\omega=\begin{cases}-j,&\omega>0\\j,&\omega<0\end{cases}$$

- $\omega>0$ 乘 $-j$：旋轉 $-\frac\pi2$（轉到虛軸下方）；$\omega<0$ 乘 $j$：旋轉 $+\frac\pi2$。都是 90°，方向相反。
- $\text{sgn}$（sign function）：$\omega>0$ 為 1、$\omega<0$ 為 $-1$。$\omega=0$ 有的書定義為 0，有的不定義；單一點對積分沒影響，工程上不太在乎。
- **quadrature** = 四分之一：旋轉 $\pm\frac\pi2$，剛好是一圈的四分之一。
- $|H(\omega)|=1$：每個頻率都乘 1，能量不變，叫 **all-pass filter**（全通濾波器）。只做相位旋轉。
- 但它**不是單純的時域平移**：正頻率和負頻率旋轉方向不一樣。（若正負頻率旋轉一樣，就只是另一個域的平移。）

**脈衝響應**（用 extended FT，乘 $e^{-|\omega|/n}$ 壓下來，分 $\omega>0$、$\omega<0$ 積分避開 sgn；老師說基本積分細節跳過，以下補上）：
$$h_n(t)=\frac{1}{2\pi}\left[-j\int_0^\infty e^{(-1/n+jt)\omega}d\omega+j\int_{-\infty}^0e^{(1/n+jt)\omega}d\omega\right]=\frac{1}{2\pi}\left[\frac{-j}{1/n-jt}+\frac{j}{1/n+jt}\right]=\frac{1}{\pi}\cdot\frac{t}{t^2+1/n^2}.$$
$n\to\infty$：$t\ne0$ 時 $\to\frac{1}{\pi t}$，$t=0$ 時是 0。所以
$$h(t)=\frac{1}{\pi t}.$$
$\frac1{\pi t}$ 也不可積，沒有正常的傅立葉轉換，兩邊都是 extended FT 的結果。

記號：$X$ 經過 Hilbert 轉換的輸出記為 $\hat{X}$：
$$\hat{X}(t)=X(t)*\frac{1}{\pi t}=\frac1\pi\int_{-\infty}^{\infty}\frac{X(\alpha)}{t-\alpha}\,d\alpha\qquad\text{(9-159)}.$$

**用途：只看一半的頻譜** [▶ 54:20](https://youtu.be/FQ9njBn5TLE?t=3260)。訊號分析常常只要看一半的頻譜（數學上很方便）。

> **解析訊號** (analytic signal)：$Z(t)=X(t)+j\hat{X}(t)$。

頻譜上（線性系統，$\hat X(\omega)=H(\omega)X(\omega)$）：
$$Z(\omega)=X(\omega)+j\left(-j\,\text{sgn}\,\omega\right)X(\omega)=\left(1+\text{sgn}\,\omega\right)X(\omega)=\begin{cases}2X(\omega),&\omega>0\\X(\omega),&\omega=0\\0,&\omega<0\end{cases}$$

- $j\cdot(-j)=1$，負號消掉。$\omega<0$ 時 $\text{sgn}=-1$，$1+(-1)=0$，負頻率**完全消掉**；正頻率保留。數學上非常乾淨漂亮。
- $\omega=0$ 的值只是為了完備性，工程上沒什麼需求。
- 所以 Hilbert 轉換真正的用途：要只看一半頻譜時，把 $\hat X$ 乘 $j$ 加上去，負頻率就消掉了。

【課本補充】Example 9-28，式 (9-158)–(9-162)，pp. 415–416：$\cos\omega t$ 經過正交濾波器變 $\sin\omega t$，$\sin\omega t$ 變 $-\cos\omega t$。$S_{X\hat X}(\omega)=jS_{XX}(\omega)\text{sgn}\,\omega$，$S_{\hat X\hat X}=S_{XX}$；解析訊號是系統 $2U(\omega)$ 的輸出，$S_{ZZ}(\omega)=4S_{XX}(\omega)U(\omega)$。

---

## 9. Wiener–Khinchin 定理：功率頻譜非負

[▶ 57:25](https://youtu.be/FQ9njBn5TLE?t=3445) 定理以人名為名，代表它的確重要。已知 $S(\omega)$ 是實數，現在證它**非負**。

> **Wiener–Khinchin 定理**：$S(\omega)\ge 0$，對每個 $\omega$。

**需要的性質**（紅字，課本沒特別說明）【口頭】：一般合理的函數（不含 delta）積分之後，**不連續點會不見**：從 $-\infty$ 積到 $x$，$x$ 一直往右移，經過跳躍點時積分值是連續變化的。傅立葉轉換是一種積分，所以（非 extended 的）傅立葉轉換是**連續**的，事實上**均勻連續** (uniformly continuous)。機率書上證的是：特性函數 $\Phi(t)=E\{e^{jtX}\}=\int f(x)e^{jtx}dx$ 永遠連續——它就是傅立葉轉換。

**證明（反證法）：**

1. 假設 $S(\omega)$ 在某點是負的，例如 $-0.3$。
2. $S$ 連續 → 那點附近存在一個**區間** $(\omega_1,\omega_2)$，$S$ 在整個區間都是負的。（這一步需要連續性。）
3. 設計一個合法的理想帶通濾波器：$H(\omega)=1$（$\omega_1<\omega<\omega_2$），其他為 0。
4. 由 Theorem 9-4（沒有頻率偏移）：$S_{YY}(\omega)=S_{XX}(\omega)|H(\omega)|^2$。
5. 輸出功率：
$$E|Y(t)|^2=R_{YY}(0)=\frac{1}{2\pi}\int S_{YY}(\omega)\,d\omega=\frac{1}{2\pi}\int_{\omega_1}^{\omega_2}S_{XX}(\omega)\,d\omega<0.$$
   （$R_{YY}(0)$ 就是反轉換代 $\tau=0$，$e^{j\omega\cdot0}=1$。）
6. 但 $|Y(t)|^2\ge 0$，期望值不可能是負的。矛盾。 ∎

所以合理的功率頻譜**是實數、而且非負**。

【課本補充】Papoulis 式 (9-163)–(9-166)，p. 416。課本的證法一樣，寫成 $0\le E\{y^2(t)\}=\frac{1}{2\pi}\int_{\omega_1}^{\omega_2}S(\omega)d\omega$ 對任何區間成立，所以 $S\ge 0$。課本補充：結合第 4 節的引理，**一個函數是功率頻譜 ⇔ 它非負**（可積）。取窄帶 $\omega_{1,2}=\omega_0\pm\delta$，$E\{y^2\}\approx\frac{\delta}{\pi}S(\omega_0)$：這說明平均功率在頻率軸上的**局部化**。

---

## 10. 一頁速查表

### 定義

| 名稱 | 公式 |
|---|---|
| 功率頻譜 | $S(\omega)=\int R(\tau)e^{-j\omega\tau}d\tau$，$R(\tau)=\frac1{2\pi}\int S(\omega)e^{j\omega\tau}d\omega$ |
| 實數過程 | $S(\omega)=2\int_0^\infty R(\tau)\cos\omega\tau\,d\tau$ |
| 互頻譜 | $S_{XY}=\mathcal{F}\{R_{XY}\}$，$S_{XY}=S_{YX}^*$ |
| 協方差頻譜 | $S=S^c+2\pi\lvert\eta\rvert^2\delta(\omega)$ |

- $R(-\tau)=R^*(\tau)$ ⇔ $S$ 實數。
- 例：$R=e^{-2\lambda|\tau|}$ ⇒ $S=\frac{4\lambda}{4\lambda^2+\omega^2}$。
- $\tau=0$ 平滑度 ↔ $\omega\to\infty$ 衰減；$\omega=0$ 平滑度 ↔ $\tau\to\infty$ 衰減。

### 引理（頻率分布 = 功率頻譜）

$X=ae^{j(\omega t-\varphi)}$，$f_\omega=\frac{S}{2\pi a^2}$，$a^2=\frac1{2\pi}\int S$，$\varphi\sim U(-\pi,\pi)$ ⇒ $S_X=S$。關鍵：$R_X(\tau)=a^2E\{e^{j\omega\tau}\}$。

### 都卜勒

$\omega=\omega_0(1-v\cos\theta/c)$，$S(\omega)=2\pi a^2f_\omega(\omega)=\frac{2\pi a^2c}{\omega_0}f_v\left[(1-\frac{\omega}{\omega_0})c\right]$。隨機速度 → 展寬；定速 → 平移；垂直 → 不變。

### 線性系統（Theorem 9-4）

$$S_{XY}=S_{XX}H^*,\quad S_{YY}=S_{XX}\lvert H\rvert^2;\qquad R_{XY}=R_{XX}*h^*(-\tau)$$

- 時域相位旋轉 ⇔ 頻域平移。

### Hilbert 與解析訊號

- $H(\omega)=-j\,\text{sgn}\,\omega$，$h(t)=\frac1{\pi t}$（extended FT，乘 $e^{-|\omega|/n}$）。
- $Z=X+j\hat X$ ⇒ $Z(\omega)=(1+\text{sgn}\,\omega)X(\omega)$，負頻率消掉。

### Wiener–Khinchin

$S(\omega)\ge0$。關鍵：$S$ 連續 → 負值必在一個區間 → 帶通濾波後 $E|Y|^2=\frac1{2\pi}\int_{\omega_1}^{\omega_2}S<0$，矛盾。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $S_{YY}=S_{XX}\lvert H\rvert^2$ | 下一集：更多頻譜例子；§11-1 分解 $S=\lvert H\rvert^2$ |
| 引理（頻率分布造頻譜） | §10-3 調變（第 16–18 集） |
| Hilbert 轉換、解析訊號 | §10-3 單邊帶調變、帶通過程 |
| 協方差頻譜 | §12 頻譜估計 |
| 平滑 ↔ 衰減 | 頻譜估計的視窗 |

---

## 附：本集一句話總結

> **功率頻譜是自相關的傅立葉轉換，一定是實數、非負（Wiener–Khinchin）；任何非負可積函數都能當某個訊號的頻譜——只要讓載波頻率的 PDF 長成那個形狀，所以都卜勒效應下頻率的分布就是接收頻譜；線性系統在頻譜上就是乘上 $|H(\omega)|^2$。**

---

## ⚠️ 待確認清單

1. [▶ 35:54](https://youtu.be/FQ9njBn5TLE?t=2154) 老師版 Theorem 9-4 含隨機 $h$ 與 $e^{j\omega_0t}$ 頻率偏移的完整公式，逐字稿沒唸全；筆記中的平移公式是推論的。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-3 (1/3) 錄影逐字稿（whisper large-v3-turbo，1:03:34）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
