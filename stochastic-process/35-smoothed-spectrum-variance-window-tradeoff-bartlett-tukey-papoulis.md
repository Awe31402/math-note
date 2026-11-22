---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 35
lecture: Lec 12-2 Spectrum Estimation — Spectrum Estimation (2/3)
date: 待補
video: https://youtu.be/M6k9i-Zsa9M
notes: Papoulis & Pillai 4th ed. §12-2 Smoothed Spectrum（式 (12-51)–(12-61)、Theorem 12-5、Table 12-1、Window selection，pp. 541–545）
---

# 第 35 集 · Lec 12-2 (2/3)：第 12 章的全貌、smoothed spectrum 的 bias 與 variance、白雜訊例子（Bartlett window）、$\mathrm{Var}\approx\frac{E_w}{2T}S^2$、窄與寬的取捨、常見 window [▶ 影片](https://youtu.be/M6k9i-Zsa9M)

← 上一集：[34](34-periodogram-bias-variance-data-window-smoothed-spectrum.md) ｜ [總目錄](README.md) ｜ 下一集：[36](36-euler-lagrange-optimum-windows-lms-two-to-one-rule.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 35 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（37:47，whisper large-v3-turbo）＋ Papoulis §12-2（pp. 541–545）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「ergodic」→「ergatic／Ergotic」，「pointwise ergodic theorem」→「Point Ergotic Theorem」，「大數法則」→「大樹法則」，「bias」→「BIOS」，「weighting」→「Waiting」，「data window」→「data window」，「spectral window」→「bactral window／vector window」，「convolution」→「commolution／comolution／comvolution」，「lag window」→「Leg Window」，「criterion」→「Quiterion／quiteria」，「white」→「坏的」，「guideline」→「guidline」，「Bartlett」→「Bullet」，「Tukey」→「Tewkey／Tuki」，「raised cosine」→「raise cosine」，「Papoulis」→「Propolis／popolis」，「functional（泛函）」→「Functional」，「distant values」→「distance value」，「estimation」→「Extimation／attimation」，「trade-off」→「tradeoff」，「complex Gaussian」→「負數高斯／Comprehensive Mean Gaussian」，「complex conjugate」→「Complete Controgate」，「sinc」→「Sync／sink」，「機率」→「基率」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 第 12 章的全貌](#1-第-12-章的全貌)
- [2. 兩種 window 的整體公式](#2-兩種-window-的整體公式)
- [3. Bias：spectral window 要窄、外面要是 0](#3-biasspectral-window-要窄外面要是-0)
- [4. Variance：白雜訊的例子](#4-variance白雜訊的例子)
  - [4.1 一個參數的 window 族](#41-一個參數的-window-族)
  - [4.2 四階條件：複數高斯](#42-四階條件複數高斯)
  - [4.3 結果：$\mathrm{Var}\approx\frac{E_w}{2T}S^2$](#43-結果mathrmvarapproxfracew2ts2)
- [5. 取捨：$M$ 大 bias 小、$M$ 小 variance 小](#5-取捨m-大-bias-小m-小-variance-小)
- [6. 常見的 window](#6-常見的-window)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 全貌回顧 | [▶ 00:00](https://youtu.be/M6k9i-Zsa9M?t=0) | — |
| 兩種 window、bias | [▶ 08:12](https://youtu.be/M6k9i-Zsa9M?t=492) | 式 (12-52)、(12-53)，p. 541 |
| 白雜訊、variance | [▶ 15:19](https://youtu.be/M6k9i-Zsa9M?t=919) | Theorem 12-5，式 (12-56)，p. 542 |
| 取捨 | [▶ 28:33](https://youtu.be/M6k9i-Zsa9M?t=1713) | 式 (12-58)、(12-59)，p. 543 |
| 常見 window | [▶ 32:11](https://youtu.be/M6k9i-Zsa9M?t=1931) | Table 12-1、式 (12-60)，pp. 543–544 |

---

## 1. 第 12 章的全貌

[▶ 00:00](https://youtu.be/M6k9i-Zsa9M?t=0) 老師說：除了細節，要了解第 12 章到底想學什麼。

**整章就是一件很單純的事**：
- 只能觀察有限時間（normalize 成 $-T$ 到 $T$），做有限區間的傅立葉轉換（得到的頻譜是 $-\infty$ 到 $\infty$）。
- 取絕對值平方、除以 $2T$（normalize 觀察的 window）——$S_T(\omega)$——當作真正的功率頻譜。
- 這個估計會準或不準，所以要探討它的 **mean** 和 **variance**。

**§12-1 為什麼講 ergodic**：告訴你什麼時候可以做估計。有些過程再怎麼增加 window、觀察越多資料，都不會讓估計更準。
- 原始定義：封閉系統、從時間不變的操作定義；結果是 $\frac{X_1+\cdots+X_n}{n}$ 趨近常數（ergodic 過程的 ergodic 事件機率非 0 即 1 ⇒ pointwise ergodic theorem）。
- 但這只是**充分條件**，不是 if and only if。這個結果在統計上叫**大數法則**——群體越大、觀察越多，平均趨近常數。很多大數法則定理各自找不同條件，ergodic 是其中一個。
- 有些書把這個結果拿來定義 ergodic，就混淆了（好像不符合大數法則的就不是 ergodic）。Papoulis 比較聰明，換名詞：mean-ergodic、variance-ergodic、distribution-ergodic，和原來的定義區隔。

**§12-2**：估計準不準。期望值不見得等於要估的值——detection/estimation 裡的 unbiased vs biased estimator。這是 biased estimator，希望 bias 越小越好：
- **data window** $c(t)$：最簡單的方法，觀察值乘 weighting（信任的乘大、不信任的乘小）。data（直接拿到的原始資料）上的 window。對調 bias 還蠻有用、比較直接；對 estimation variance 沒那麼大的直接幫助。
- **spectral window** $W(\omega)$：直接在頻譜上調，不是相乘而是**卷積**。對 variance 的調整效果比較好，對 bias 比較不明顯。（不是一定：兩者都可以調 bias 和 variance，看效果。）
- 轉回時域叫 **lag window** $w(\tau)$：lag = delay（間隔 10 秒、20 秒之後看到的值），直接作用在自相關上。

今天要講怎麼設計最好的 data window 和 spectral window。跟前面設計最好的濾波器（第 21 集）很像，但準則 (criterion) 不同、結果就不同。前面結果漂亮是因為剛好都是多項式（把要估的東西假設成一階、二階、三階多項式，標準的設計方式）。

---

## 2. 兩種 window 的整體公式

[▶ 08:42](https://youtu.be/M6k9i-Zsa9M?t=522) 把 data window 和 spectral window 整合在一起：
$$E\{S_w(\omega;c)\}\approx\frac1{2\pi}\cdot\frac{1}{4\pi T}\,S(\omega)*C^2(\omega)*W(\omega).$$

- 大寫 $W$：作用在頻譜上。
- 大寫 $C$：data window $c(t)$ 的傅立葉轉換。因為是在**時域、之前**做的，作用到頻譜上要取**絕對值平方**。
- 兩者效果其實差異沒那麼大，角色不同而已；data window 的限制是只在 $-T$ 到 $T$ 有值。
- $T$ 是另一個參數：量測 window 的區間大小。

老師說：這是到 (12-56) 為止的總結；有這個概念，看哪本書都只是角色轉換，講的是同一件事。

**data window 的傳統條件** [▶ 10:44](https://youtu.be/M6k9i-Zsa9M?t=644)：
$$\frac{1}{4\pi T}C^2(\omega)\to\delta(\omega)\quad(T\to\infty).$$
不管怎麼設計，都希望有這個性質（數學上能處理的重要理由：會轉成 delta）。這樣 $T\to\infty$ 時：
$$E\{S_w(\omega)\}\approx\frac1{2\pi}S(\omega)*W(\omega)\qquad\text{(12-53)}.$$
就是 spectral window 和功率頻譜做卷積。

【課本補充】p. 541：lag window 條件 $w(0)=1=\frac1{2\pi}\int W(\omega)d\omega$、$W(-\omega)=W(\omega)$、$W(\omega)\ge0$（式 (12-52)）；(12-53) 假設 $W$ 在任何長度 $\frac1T$ 的區間近乎常數。

---

## 3. Bias：spectral window 要窄、外面要是 0

[▶ 12:15](https://youtu.be/M6k9i-Zsa9M?t=735) 希望至少漸近不偏（$T\to\infty$ 時趨近要估的東西），而且要有大數法則的行為。$W$ 要長什麼樣子？

**卷積的直觀**【口頭】：卷積會把原來的東西**變寬**。原來的頻譜是一根脈衝，卷積後就有寬度；寬度 $B$ 的東西和寬度 $A$ 的卷積，左右各拉開 $A$。拉開之後值也會被調整。所以：
- **越窄越好**：原點附近很短的 duration，才能讓那一點的值還蠻準。
- **外面最好都是 0**：外面不是 0，卷積會把所有值納進來相乘相加，把別的地方的值跟這邊混在一起，影響這點的估計準確度。

同學會說「那就用脈衝就好了」——跟 data window 很像，實際上也沒錯。但還要考慮 variance。

---

## 4. Variance：白雜訊的例子

[▶ 14:18](https://youtu.be/M6k9i-Zsa9M?t=858) 計算後，variance 是兩個經過 data window 的估計值（$\frac{|\cdot|^2}{2T}$）的共變異，再經過**兩次** spectral window（window 是線性的）。效果很難從數學公式討論，所以用簡化的例子——最好的例子當然是高斯。

**人為的例子** (artificial example)：要估的功率頻譜是**白的**：$R(\tau)=\frac{N_0}2\delta(\tau)$，$S(\omega)=\frac{N_0}{2}$（平的）。
- 回顧 Theorem 12-4（證明不太嚴謹，但有重要的 guideline）：估計的 variance 約等於要估值的平方。
- 這就是估**雜訊能量**：通訊接收端實作上有時必須估 $\frac{N_0}2$。
- 先不用 data window，只看 spectral window 的效果。

### 4.1 一個參數的 window 族

[▶ 16:51](https://youtu.be/M6k9i-Zsa9M?t=1011) spectral window 的設計太多樣化，沒辦法全部設計。**簡化**：固定一個基本型 $W_0$，只剩**一個參數** $M$：
$$W(\omega)=M\,W_0(M\omega)\quad\leftrightarrow\quad w(\tau)=w_0\left(\frac{\tau}{M}\right)\qquad\text{(12-58)}.$$
- 老師說這是標準的研究做法：任何通訊系統的參數都好多（10 個、20 個），要學會怎麼簡化。
- 基本型用 $\mathrm{sinc}^2$ 當 spectral window（Bartlett window）；乘 2 就縮成一半、乘 3 縮成三分之一。
- 頻譜上拉寬 ⇔ 時域壓縮，反之亦然。

⚠️ 逐字稿缺字：老師說「lag window 是方波，負 1 到 1，標準的三角波」——口語混在一起。Bartlett 的 lag window 是**三角波** $w_0(t)=1-|t|$（$|t|\le1$），spectral window 是 $\frac{4\sin^2(\omega/2)}{\omega^2}$（Table 12-1）。

**乘 $M$ 的原因** [▶ 29:34](https://youtu.be/M6k9i-Zsa9M?t=1774)：**固定面積**。令 $\omega'=M\omega$：
$$\int MW_0(M\omega)\,d\omega=\int W_0(\omega')\,d\omega'.$$
調寬度但總面積不變（總要維持一個定量）。

**預告結論**：bias 要窄（越窄越好），但 variance 會發現**越寬越好**——tradeoff。所有估計 (estimation) 都是這樣：bias 變好 variance 就變差，反之亦然。

### 4.2 四階條件：複數高斯

[▶ 19:23](https://youtu.be/M6k9i-Zsa9M?t=1163) §12-1 建立的基礎：
- 估 mean，看二階（自共變異）。
- 估 variance，看四階。
- 估三階要看六階——要 double 一下。
- 這裡要估的是二階的性質（自相關／頻譜），所以要四階的性質確認。

一般隨機變數的四階沒辦法算，所以**假設**四個相乘可以兩兩配對降次——直觀就是**高斯**。

**複數高斯**（獨立、零平均、二維）：
$$E\{c_nc_m^*\}=\sigma^2\delta[n-m],\qquad E\{c_nc_m\}=0.$$
不加共軛的期望值剛好是 0，加了絕對值就是正的。**降階**：四個取期望值就是兩兩配對——1 配 2、1 配 3、1 配 4，相加；唯一差別是有共軛，所以**有一組相乘是 0**（兩個都沒共軛或都有共軛的那組），只剩兩項。細節留給同學看。

### 4.3 結果：$\mathrm{Var}\approx\frac{E_w}{2T}S^2$

[▶ 22:27](https://youtu.be/M6k9i-Zsa9M?t=1347) 不看 data window。共變異 = 兩兩相乘再減個別期望值相乘；由假設，四階 = 兩個自共變異乘積的和，扣掉一個只剩一個。自相關是脈衝（雜訊），所以剛好得到 $\mathrm{sinc}^2$。

真正的 variance = 共變異經過兩次 spectral window（兩個 sinc）。過程：積分順序對調（$dy\,dz\to dz\,dy$——「所有的運算整本書都是這樣子，碰到積分一定是順序對調，因為通常會有新的、比較好算的結果」）；$T\to\infty$ 時 $\mathrm{sinc}^2$ 接近 delta（總積分 1、中間衝到無限大）。

> **Theorem 12-5**：$|\omega|\gg\frac1T$ 時
> $$\mathrm{Var}\,S_w(\omega)\approx\frac{E_w}{2T}S^2(\omega),\qquad E_w=\frac1{2\pi}\int_{-\infty}^{\infty}W^2(\omega)\,d\omega\qquad\text{(12-56)}.$$

**讀藍色的字**：
- Theorem 12-4 是有道理的：variance 真的**正比於功率頻譜的平方**（高斯時）；我們要估的大部分是高斯形式（machine learning 也有專門估高斯的書）。
- $\frac1{2T}$：variance 跟量測 window 大小有關。
- $E_w$：spectral window **平方**的積分。為什麼是平方？因為 variance 要經過 window **兩次**（定理 9-2、9-4 的直觀）——算出來是一次，觀念上就不對。
- 所以 **$E_w$ 越小越好**——spectral window 對調 variance 很直接，就是由這個式子來的。
- 這個例子：$S=\frac{N_0}2$ 是常數；Bartlett window 的 $E_w=\frac23M$。

【課本補充】p. 542 的證明：$\mathrm{Cov}[S_T(u),S_T(v)]\approx\frac{\sin^2T(u-v)}{T^2(u-v)^2}S^2(u)$（式 (12-55)），$|u-v|\gg\frac1T$ 可忽略，所以近似成面積 $\frac\pi TS^2(u)$ 的脈衝：$\mathrm{Cov}=\frac\pi TS^2(u)\delta(u-v)$（式 (12-57)），代入 $S_w=\frac1{2\pi}S_T*W$ 得 (12-56)。

---

## 5. 取捨：$M$ 大 bias 小、$M$ 小 variance 小

[▶ 28:33](https://youtu.be/M6k9i-Zsa9M?t=1713) bias 要窄、外面是 0；variance 要 $E_w$ 小。看起來沒衝突——設計一個很窄的脈衝、讓平方總面積也很小，有可能嗎？老師說：這個脈絡很邏輯、很清楚，做研究要這樣思考。

- **bias 小** → $M$ 要**大**（$M$ 乘在 $\omega$ 上，越大脈衝縮得越窄）。
- **variance 小** → $E_w$ 小。但面積固定、寬度縮小，平方之後就多一個 $M$：
$$E_w=M\,E_{w0}\quad(E_{w0}\text{ 是基本型的標準值，不變}).$$
所以 $M$ 要**小**。

> **衝突**：一個要 $M$ 大、一個要 $M$ 小。bias 和 variance 很難同時調好——只能衡量：要 bias 小、variance 小，還是兩者的 weighted sum 小。

**General 的 guideline** [▶ 36:20](https://youtu.be/M6k9i-Zsa9M?t=2180)：不只 Bartlett，用任何基本波形拉寬壓窄設計，都只有一個參數 $M$，**$M$ 和 variance 成正比**。要讓 variance 降兩倍，$M$ 變一半就對了。

**當評審的例子**【口頭】：以後去業界做 estimation，或去評審公司其他部門的計畫——如果有人說「把 window 降一半，variance 降四倍」，你就知道這違反直覺（任何 window 結果都一樣是正比），表示他哪裡搞錯了。當評審常常就是用這種基本觀念，抓到工程上可能的問題。「所以還是要學 Random Process。」

【課本補充】p. 543：可靠度 $\frac{\mathrm{Var}S_w}{S^2}\approx\frac{E_w}{2T}=\alpha$（式 (12-59)）。大部分 window 的 $E_w$ 在 $0.5M$ 到 $0.8M$；若可接受 $\alpha=0.2$，須 $M\le\frac T2$。沒有先驗資訊時：從 $M=\frac T2$ 開始，若估計在 $\frac1M$ 量級的區間近乎常數，表示 $M$ 太大，逐步減小（減 $M$ 不太影響 bias，但 variance 變小）；最佳平衡時，估計的標準差應等於 bias 的兩倍。若 $M=\frac T2$ 時還不平滑，表示 $T$ 不夠大。（不確定性原理：bias 要 $W$ 短，與 $M$ 小衝突。）

---

## 6. 常見的 window

[▶ 32:11](https://youtu.be/M6k9i-Zsa9M?t=1931) 歷史上有很多 window，通常用發明者的名字命名。

| Window | lag window $w_0(t)$（$\lvert t\rvert\le1$） | spectral $W_0(\omega)$ | $m_2$ | $E_w$ |
|---|---|---|---|---|
| Bartlett | $1-\lvert t\rvert$（三角波） | $\frac{4\sin^2(\omega/2)}{\omega^2}$ | $\infty$ | $\frac23$ |
| Tukey | $\frac12(1+\cos\pi t)$（raised cosine） | $\frac{\pi^2\sin\omega}{\omega(\pi^2-\omega^2)}$ | $\frac{\pi^2}{2}$ | $\frac34$ |
| Parzen | 三角波的卷積 | $\frac34\left(\frac{\sin(\omega/4)}{\omega/4}\right)^4$ | 12 | 0.539 |
| Papoulis | $\frac1\pi\lvert\sin\pi t\rvert+(1-\lvert t\rvert)\cos\pi t$ | $8\pi^2\frac{\cos^2(\omega/2)}{(\pi^2-\omega^2)^2}$ | $\pi^2$ | 0.587 |

（表格依課本 Table 12-1；老師只提 Bartlett、Tukey、Papoulis。）

- Papoulis 做了 combine：有 cosine、有三角波，做標準的 compromise。**Turn out Papoulis 最好**——但說最好要先有準則，Papoulis 有定義（下一集）。
- 他用的技巧叫 **functional（泛函）**：有同學對「積分之後做微分」沒辦法接受，其實泛函常常在做這件事。泛函這門課通常修過實變之後才修，比較深；後面會舉例。

**$m_2$**（課本式 (12-60)）：
$$m_2=\frac1{2\pi}\int\omega^2W(\omega)\,d\omega=\frac{1}{M^2}\cdot\frac1{2\pi}\int\omega^2W_0(\omega)\,d\omega.$$
- 像波形**寬度**的量（二階動差）。
- **希望 spectral window 外面降得非常快**：spectral window 用卷積影響（把頻譜送進一個濾波器，數位濾波器很直接）——不希望**遠方的頻譜值** (distant values) 影響要算的這點；要估的是這一小塊，卷積太寬就把遠方的值納進來。怎麼量降得快不快？就是 $m_2$。
- **Bartlett 的 $m_2=\infty$**：以 $\omega^2$ 的速度降，降得不夠快，所以不太好。Tukey $\frac{\pi^2}2$ 有點小；Papoulis 剛好在中間，$\pi^2$。
- $m_2$ 也希望小；$E_w=ME_{w0}$。

【課本補充】p. 544 選 window 形狀的考量：(1) $W(\omega)$ 要非負、面積 $2\pi$（保證估計非負、一致）；(2) bias 小 → $W$ 的 duration 小，用 $m_2$ 衡量；(3) $W(\omega)$ 隨 $\omega$ 增加要快速趨近 0（旁瓣小），減少遠方峰值的影響——由 $w(t)$ 的連續性決定：要 $W\sim A/\omega^n$，$w$ 在端點 $\pm M$ 的 $n-1$ 階以下導數都要是 0（式 (12-61)）；(4) $E_w$ 要小（降低 variance）。大部分 window 是經驗選的；高解析度（$T$ 大）時，表中最後一個（Papoulis）讓 bias 最小。

---

## 7. 一頁速查表

| 項目 | 公式／重點 |
|---|---|
| 全貌 | $S_T=\frac1{2T}\lvert X_T\rvert^2$ 估 $S$；看 mean 與 variance |
| 整體 | $E S_w\approx\frac1{2\pi}\frac1{4\pi T}S*C^2*W$ |
| Bias（$T$ 大） | $E S_w\approx\frac1{2\pi}S*W$：$W$ 要窄、外面為 0 |
| Variance | $\mathrm{Var}S_w\approx\frac{E_w}{2T}S^2$，$E_w=\frac1{2\pi}\int W^2$ |
| Window 族 | $W=MW_0(M\omega)$（面積固定），$E_w=ME_{w0}$ |
| 取捨 | $M$ 大 → bias 小；$M$ 小 → variance 小；variance ∝ $M$ |
| $m_2$ | $\frac1{2\pi}\int\omega^2W$：寬度／衰減；Bartlett $=\infty$ |

**關鍵步驟**：
- 四階條件：複數高斯 $E\{c_nc_m\}=0$，配對時一組為 0。
- 白雜訊 $S=\frac{N_0}2$：共變異得 $\mathrm{sinc}^2$，經過兩次 $W$，$\mathrm{sinc}^2\to\delta$。
- $E_w$ 是平方的積分，因為 variance 經過 window 兩次。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 最佳 window、泛函技巧 | 下一集：minimum bias data/spectral window、LMS spectral window |
| bias–variance 取捨 | 第 13 章 MS 估計 |

---

## 附：本集一句話總結

> **第 12 章就是用有限資料的 $\frac1{2T}|X_T(\omega)|^2$ 估功率頻譜並分析它的 mean 與 variance；平滑後 bias 由 $S*W$ 決定（$W$ 要窄、外面為 0），variance 約 $\frac{E_w}{2T}S^2$（$E_w$ 是 $W^2$ 的面積）；用 $W=MW_0(M\omega)$ 一個參數調整時，$M$ 大 bias 小但 $E_w=ME_{w0}$ 變大——bias 與 variance 只能取捨，而 variance 永遠正比於 $M$。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 12-2 (2/3) 錄影逐字稿（whisper large-v3-turbo，37:47）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
