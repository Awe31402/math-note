---
course: 統計學（數理統計，數學系）
episode: 11
lecture: Lec11
date: 待補
video: https://youtu.be/HwoubxzTZbw
notes: Hogg 8th ed. Theorem 3.6.1 (b)(c)（p. 214）；§4.1 點估計（p. 225）；§4.2 信賴區間（p. 238）；§4.5 假設檢定（p. 267）
---

# 第 11 集 · Lec11：證明 $\bar X\perp S^2$ 與 $(n-1)S^2/\sigma^2\sim\chi^2(n-1)$；統計推論的兩條路 [▶ 影片](https://youtu.be/HwoubxzTZbw)

← 上一集：[10](10-independence-lemmas-chi-square-sum-xbar-normal.md) ｜ [總目錄](../README.md) ｜ 下一集：[12](12-estimator-unbiasedness.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 11 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:04:39，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §3.6、§4.1、§4.2、§4.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「卡方」→「卡荒」，「iid」→「RID」，「$\theta$」→「seta／zeta／sitta」，「$\hat\theta$」→「Sitta Head」，「joint」→「Join」，「implies」→「implied」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 證明 (b)：X̄ 與 S² 獨立](#1-證明-bx̄-與-s-獨立)
  - [1.1 策略：證 X̄ 和 (X₁−X̄,…,Xₙ−X̄) 獨立](#11-策略證-x̄-和-x₁x̄xₙx̄-獨立)
  - [1.2 算 joint mgf](#12-算-joint-mgf)
  - [1.3 拆成兩個 mgf 相乘](#13-拆成兩個-mgf-相乘)
- [2. 熱身：Σ(Xᵢ−μ)²/σ² ～ χ²(n)](#2-熱身σxᵢμσ--χn)
- [3. 證明 (c)：(n−1)S²/σ² ～ χ²(n−1)](#3-證明-cn1sσ--χn1)
- [4. 「估一個參數，自由度減一」](#4-估一個參數自由度減一)
- [5. 進入統計：為什麼需要統計推論](#5-進入統計為什麼需要統計推論)
- [6. 統計推論的兩條路](#6-統計推論的兩條路)
  - [6.1 點估計](#61-點估計)
  - [6.2 區間估計](#62-區間估計)
  - [6.3 假設檢定](#63-假設檢定)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

接上一集的主定理（$X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$）：

| | 結論 | 狀態 |
|---|---|---|
| (a) | $\bar X\sim N(\mu,\sigma^2/n)$ | 上一集證過 |
| (b) | $\bar X\perp S^2$ | **本集** |
| (c) | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$ | **本集** |

然後正式進入統計：點估計、區間估計、假設檢定。

---

## 1. 證明 (b)：X̄ 與 S² 獨立

### 1.1 策略：證 X̄ 和 (X₁−X̄,…,Xₙ−X̄) 獨立

[▶ 00:31](https://youtu.be/HwoubxzTZbw?t=31) 複習：獨立的 $X,Y$ 各取函數會獨立；但對**同一組**取兩個函數一般**不**獨立。$\bar X$、$S^2$ 都是 $X_1,\dots,X_n$ 的函數卻獨立，是特例。

**工具**（[▶ 02:35](https://youtu.be/HwoubxzTZbw?t=155)）：兩組隨機變數獨立 ⇔ joint mgf＝各組 mgf 相乘。

**策略**（[▶ 03:05](https://youtu.be/HwoubxzTZbw?t=185)）：證明

$$\bar X\quad\text{和}\quad(X_1-\bar X,\ X_2-\bar X,\ \dots,\ X_n-\bar X)$$

這兩組獨立。因為

$$S^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2$$

只是第二組的函數（各自平方、加起來、除以 $n-1$）。第二組裡雖然有 $\bar X$，但 $S^2$ 是「第二組」的函數，和第一組獨立，所以 $\bar X\perp S^2$。

### 1.2 算 joint mgf

[▶ 05:37](https://youtu.be/HwoubxzTZbw?t=337) 一共 $n+1$ 個隨機變數，配 $n+1$ 個 $t$：$\bar X$ 配 $t$，$X_i-\bar X$ 配 $t_i$。

$$M(t,t_1,\dots,t_n)=E\left[\exp\left(t\bar X+\sum_{i=1}^nt_i(X_i-\bar X)\right)\right].$$

**整理指數**（[▶ 08:38](https://youtu.be/HwoubxzTZbw?t=518)）。令 $\bar t=\frac1n\sum t_i$：

$$t\bar X+\sum t_iX_i-\left(\sum t_i\right)\bar X=\sum_{i=1}^n\frac tnX_i+\sum_{i=1}^nt_iX_i-\sum_{i=1}^n\bar tX_i=\sum_{i=1}^n\left[\frac{n(t_i-\bar t)+t}{n}\right]X_i.$$

（用了 $\sum t_i\cdot\bar X=n\bar t\cdot\frac1n\sum X_i=\sum\bar tX_i$。）

**拆開**（[▶ 11:10](https://youtu.be/HwoubxzTZbw?t=670)）。令 $c_i=\frac{n(t_i-\bar t)+t}{n}$，指數裡的和變成乘積：

$$M=E\left[\prod_{i=1}^ne^{c_iX_i}\right].$$

每個因子只是 $X_i$ 的函數。$X_1,\dots,X_n$ 獨立 ⇒ 相乘的期望值＝期望值相乘：

$$M=\prod_{i=1}^nE\left(e^{c_iX_i}\right)=\prod_{i=1}^nM_{X_i}(c_i).$$

**代常態 mgf**（[▶ 13:19](https://youtu.be/HwoubxzTZbw?t=799)）：$M_{X_i}(c)=\exp\left(\mu c+\frac{\sigma^2}{2}c^2\right)$，相乘變指數相加：

$$M=\exp\left(\mu\sum c_i+\frac{\sigma^2}{2}\sum c_i^2\right).$$

### 1.3 拆成兩個 mgf 相乘

[▶ 14:50](https://youtu.be/HwoubxzTZbw?t=890) 先記一個常用事實（[▶ 16:25](https://youtu.be/HwoubxzTZbw?t=985)）：

$$\sum_{i=1}^n(x_i-\bar x)=0.$$

【口頭】每人成績減全班平均加起來一定是 0：比平均大的和比平均小的抵消。證明：$\sum x_i-n\bar x=\sum x_i-\sum x_i=0$。

所以 $\sum(t_i-\bar t)=0$。算兩個和：

- $\sum c_i=\sum(t_i-\bar t)+t=t$。
- $\sum c_i^2=\sum\left[(t_i-\bar t)+\frac tn\right]^2=\sum(t_i-\bar t)^2+\frac{2t}{n}\sum(t_i-\bar t)+n\frac{t^2}{n^2}=\sum(t_i-\bar t)^2+\frac{t^2}{n}$。

代回：

$$M=\underbrace{\exp\left(\mu t+\frac12\cdot\frac{\sigma^2}{n}t^2\right)}_{\text{只有 }t}\cdot\underbrace{\exp\left(\frac{\sigma^2}{2}\sum_{i=1}^n(t_i-\bar t)^2\right)}_{\text{只有 }t_1,\dots,t_n}.$$

[▶ 18:02](https://youtu.be/HwoubxzTZbw?t=1082) 認出兩個因子：

1. **第一個**：$\bar X\sim N(\mu,\sigma^2/n)$（定理 (a)），它的 mgf 就是 $e^{\mu t+\frac12\frac{\sigma^2}{n}t^2}$。所以第一個＝$M_{\bar X}(t)$。
2. **第二個**（[▶ 19:05](https://youtu.be/HwoubxzTZbw?t=1145)）：要 $(X_1-\bar X,\dots,X_n-\bar X)$ 的 joint mgf，就把 $\bar X$ 對應的 $t$ 定成 0（上一集的 (C)）。$t=0$ 時第一個因子是 1，剩下第二個因子。所以第二個＝$M_{X_1-\bar X,\dots,X_n-\bar X}(t_1,\dots,t_n)$。

$$M(t,t_1,\dots,t_n)=M_{\bar X}(t)\cdot M_{X_1-\bar X,\dots,X_n-\bar X}(t_1,\dots,t_n).$$

joint mgf＝兩組 mgf 相乘 ⇒ 兩組獨立 ⇒ $\bar X\perp S^2$。∎

[▶ 22:42](https://youtu.be/HwoubxzTZbw?t=1362) 【口頭】每本數理統計的書都會證這個定理，方法各不相同；老師覺得這種最簡單。

---

## 2. 熱身：Σ(Xᵢ−μ)²/σ² ～ χ²(n)

[▶ 23:44](https://youtu.be/HwoubxzTZbw?t=1424)

1. $X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$。
2. 各取**同一個**函數 $g(x)=\frac{x-\mu}{\sigma}$：
   - 獨立的各取函數 → 還是獨立（I）。
   - [▶ 25:50](https://youtu.be/HwoubxzTZbw?t=1550) 同分配的取**同一個**函數 → 還是同分配（i.d.）：$P(g(X)\le c)=P(g(Y)\le c)$。
   - 每個都是 $N(0,1)$（標準化）。所以 $\frac{X_i-\mu}{\sigma}$ iid $N(0,1)$。
3. [▶ 27:52](https://youtu.be/HwoubxzTZbw?t=1672) 再各取平方：還是 iid，每個是 $\chi^2(1)$（$Z^2\sim\chi^2(1)$）。
4. [▶ 29:24](https://youtu.be/HwoubxzTZbw?t=1764) 獨立卡方相加，自由度相加：

$$\sum_{i=1}^n\left(\frac{X_i-\mu}{\sigma}\right)^2=\frac{\sum_{i=1}^n(X_i-\mu)^2}{\sigma^2}\sim\chi^2(n).$$

---

## 3. 證明 (c)：(n−1)S²/σ² ～ χ²(n−1)

[▶ 30:25](https://youtu.be/HwoubxzTZbw?t=1825) 目標：$\frac{(n-1)S^2}{\sigma^2}=\frac{\sum(X_i-\bar X)^2}{\sigma^2}$ 的 mgf 是 $(1-2t)^{-(n-1)/2}$。

**Step 1：加一個減一個 $\bar X$**（[▶ 34:33](https://youtu.be/HwoubxzTZbw?t=2073)）：
$$\sum(X_i-\mu)^2=\sum\left[(X_i-\bar X)+(\bar X-\mu)\right]^2=\sum(X_i-\bar X)^2+n(\bar X-\mu)^2+2(\bar X-\mu)\underbrace{\sum(X_i-\bar X)}_{=0}.$$
所以
$$\frac{\sum(X_i-\mu)^2}{\sigma^2}=\frac{(n-1)S^2}{\sigma^2}+\frac{(\bar X-\mu)^2}{\sigma^2/n}.$$

**Step 2：取 mgf**（[▶ 36:34](https://youtu.be/HwoubxzTZbw?t=2194)）。左邊是 $\chi^2(n)$：
$$(1-2t)^{-n/2}=E\left[\exp\left(t\frac{(n-1)S^2}{\sigma^2}\right)\exp\left(t\frac{(\bar X-\mu)^2}{\sigma^2/n}\right)\right].$$

**Step 3：用 (b)**（[▶ 37:05](https://youtu.be/HwoubxzTZbw?t=2225)）。第一個因子只是 $S^2$ 的函數（其他都是常數），第二個只是 $\bar X$ 的函數。$\bar X\perp S^2$ ⇒ 拆開：
$$(1-2t)^{-n/2}=M_{(n-1)S^2/\sigma^2}(t)\cdot M_{(\bar X-\mu)^2/(\sigma^2/n)}(t).$$

**Step 4：第二個是 $\chi^2(1)$**（[▶ 39:48](https://youtu.be/HwoubxzTZbw?t=2388)）。$\bar X\sim N(\mu,\sigma^2/n)$，標準化 $\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$，平方是 $\chi^2(1)$：
$$M_{(\bar X-\mu)^2/(\sigma^2/n)}(t)=(1-2t)^{-1/2}.$$

**Step 5：除過去**：
$$M_{(n-1)S^2/\sigma^2}(t)=\frac{(1-2t)^{-n/2}}{(1-2t)^{-1/2}}=(1-2t)^{-(n-1)/2},\quad t<\tfrac12.$$
這是 $\chi^2(n-1)$ 的 mgf。∎

[▶ 40:51](https://youtu.be/HwoubxzTZbw?t=2451) 【口頭】證明有一點技巧，導一遍就會。唯一要用的是 $\sum(X_i-\mu)^2/\sigma^2\sim\chi^2(n)$。

---

## 4. 「估一個參數，自由度減一」

[▶ 41:54](https://youtu.be/HwoubxzTZbw?t=2514)

**不能這樣看**（[▶ 43:29](https://youtu.be/HwoubxzTZbw?t=2609)）：
$$\frac{(n-1)S^2}{\sigma^2}=\sum\left(\frac{X_i-\bar X}{\sigma}\right)^2\quad\text{✗ 不能說是 } n\text{ 個 }\chi^2(1)\text{ 相加}.$$
因為 $\frac{X_i-\bar X}{\sigma}$ 不是 $N(0,1)$，而且彼此**不獨立**。所以才要花那麼多功夫證明。

**怎麼記**（[▶ 44:31](https://youtu.be/HwoubxzTZbw?t=2671)）：

| | 分配 |
|---|---|
| $\dfrac{\sum(X_i-\mu)^2}{\sigma^2}$ | $\chi^2(n)$ |
| $\dfrac{\sum(X_i-\bar X)^2}{\sigma^2}$（$\mu$ 換成 $\bar X$） | $\chi^2(n-1)$ |

【口頭】唯一差別是把不知道的 $\mu$ 換成估計值 $\bar X$。統計常常這樣：一個隨機變數本來是 $\chi^2(n)$，裡面有參數不知道，你估計一個，分配還是卡方，但**估一個就減一個**自由度。以後會看到很多。

[▶ 45:31](https://youtu.be/HwoubxzTZbw?t=2731) 機率的部分講到這裡。前面等於都在複習機率。

---

## 5. 進入統計：為什麼需要統計推論

[▶ 46:05](https://youtu.be/HwoubxzTZbw?t=2765)

- 機率和統計都繞著**隨機變數**。它不只是變數（值不固定），還是**隨機**的：發生多少不知道，但照一定的模式發生，那個模式就是 **pdf**。
- [▶ 47:51](https://youtu.be/HwoubxzTZbw?t=2871) **知道 pdf 就知道一切**：
  - $\mu=\int xf(x)\,dx$
  - $\sigma^2=\int(x-\mu)^2f(x)\,dx$
  - $P(a<X<b)=\int_a^bf(x)\,dx$
- [▶ 49:23](https://youtu.be/HwoubxzTZbw?t=2963) 需要統計，是因為**不完全知道** $f$。

[▶ 49:54](https://youtu.be/HwoubxzTZbw?t=2994) 很多書不叫 *Mathematical Statistics*，叫 *Statistical Inference*。**推論**像猜測，但是**有道理的猜測**。

【口頭】[▶ 50:25](https://youtu.be/HwoubxzTZbw?t=3025) 大家都在做推論：

- 看醫生肚子痛，醫生猜是胃還是十二指腸，沒有百分之百把握。老師說自己身上某處痛了兩年，醫生都說是壓力大；後來另一位醫生才診斷出是疝氣，去開了刀。也有人被說有癌症，開刀後發現沒有，白挨一刀。醫生也會推論錯。
- 早上起來猜會不會下雨，憑經驗，可能對可能錯。
- 我們的推論是用**統計方法**做的。

**統計推論的問題**（[▶ 53:31](https://youtu.be/HwoubxzTZbw?t=3211)）：

- pdf 寫成 $f(x;\theta)$：函數 $f$ 知道，$\theta$ 不知道（常態的 $\mu,\sigma^2$、Poisson 的 $\lambda$、二項的 $p$）。
- 統計要做的事：**推論 $\theta$**。
- [▶ 54:31](https://youtu.be/HwoubxzTZbw?t=3271) 不能憑空推論，一定要有**隨機樣本** $X_1,\dots,X_n$（都從 $f(x;\theta)$ 來）。觀察值裡有 $\theta$ 的資訊。

---

## 6. 統計推論的兩條路

[▶ 55:33](https://youtu.be/HwoubxzTZbw?t=3333) 兩個方向：**估計**（estimation）和**假設檢定**（hypothesis testing）。

### 6.1 點估計

[▶ 56:05](https://youtu.be/HwoubxzTZbw?t=3365)

> **點估計**（point estimation）：用樣本的函數 $\hat\theta=\hat\theta(X_1,\dots,X_n)$ 來估 $\theta$。$\theta$ 上面戴帽子，讀「theta hat」。

有很多漂亮的理論，後面會講。

**缺點**（[▶ 57:08](https://youtu.be/HwoubxzTZbw?t=3428)）：$\hat\theta$ 幾乎不可能**剛好等於** $\theta$。

例：用 $\bar X$ 估常態的 $\mu$。

- $\bar X\sim N(\mu,\sigma^2/n)$。$n$ 越大，variance 越小，越往 $\mu$ 集中；$n\to\infty$ 時才會等於 $\mu$。但不可能抽無窮多次，做統計就是因為只能抽少量。
- [▶ 58:42](https://youtu.be/HwoubxzTZbw?t=3522) $n$ 固定時，$\bar X$ 是連續型：$P(\bar X=\mu)=\int_\mu^\mu f_{\bar X}=0$。

[▶ 60:46](https://youtu.be/HwoubxzTZbw?t=3646) 【口頭】$\theta$ 是常數；$\hat\theta$ 是隨機變數，有分配、每點都可能出現。隨機變數怎麼可能剛好等於一個常數？相等的機率是 0。

### 6.2 區間估計

[▶ 59:43](https://youtu.be/HwoubxzTZbw?t=3583)

> **區間估計**（interval estimation）：找兩個統計量 $T_1=T_1(X_1,\dots,X_n)$、$T_2=T_2(X_1,\dots,X_n)$，使
> $$P(T_1<\theta<T_2)=1-\alpha.$$
> $1-\alpha$ 通常取 $0.9$、$0.95$、$0.99$。$(T_1,T_2)$ 叫**信賴區間**（confidence interval）。

- 雖然不知道 $\theta$ 等於多少，但知道它落在哪個範圍的機率很大。
- [▶ 61:47](https://youtu.be/HwoubxzTZbw?t=3707) **希望區間短、涵蓋機率大**。【口頭】期末考後你問會不會及格。我說「你的成績在 30 到 80 之間，機率 0.95」，你沒感覺；我說「在 72 到 75 之間，機率 0.8」，雖然機率小一點，你卻很有信心。

### 6.3 假設檢定

[▶ 62:49](https://youtu.be/HwoubxzTZbw?t=3769)

- 【口頭】統計最重要的其實是**假設檢定**，統計的發展就是從假設檢定開始的。
- 很多時候不想知道 $\theta$ 等於多少，而是想知道**它有沒有超過某個值**。
- [▶ 63:22](https://youtu.be/HwoubxzTZbw?t=3802) 【口頭】感冒看醫生拿藥。醫生說「治好的機率 0.3 以上」，你可能不吃，回家喝開水就好；說「0.7 以上」，你就有信心回家吃。你在乎的是有沒有超過某個值，不在乎它到底是多少。

後面會講。下課。

---

## 7. 一頁速查表

**常態樣本主定理**（$X_i$ iid $N(\mu,\sigma^2)$）

| | 結論 | 證明關鍵一步 |
|---|---|---|
| (a) | $\bar X\sim N(\mu,\sigma^2/n)$ | $M_{\bar X}(t)=[M_X(t/n)]^n$ |
| (b) | $\bar X\perp S^2$ | joint mgf of $(\bar X;X_1-\bar X,\dots)$ $=e^{\mu t+\frac{\sigma^2}{2n}t^2}\cdot e^{\frac{\sigma^2}{2}\sum(t_i-\bar t)^2}$ |
| (c) | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$ | $\chi^2(n)=\frac{(n-1)S^2}{\sigma^2}+\chi^2(1)$，獨立 ⇒ mgf 相除 |

**常用恆等式**

- $\sum(x_i-\bar x)=0$
- $\sum(x_i-\mu)^2=\sum(x_i-\bar x)^2+n(\bar x-\mu)^2$

**卡方**

- $\sum\frac{(X_i-\mu)^2}{\sigma^2}\sim\chi^2(n)$（$n$ 個獨立 $\chi^2(1)$）
- $\sum\frac{(X_i-\bar X)^2}{\sigma^2}\sim\chi^2(n-1)$（$\mu$ 換成 $\bar X$：估一個減一個自由度）

**統計推論**

| 方法 | 做什麼 | 注意 |
|---|---|---|
| 點估計 | $\hat\theta(X_1,\dots,X_n)$ | 連續時 $P(\hat\theta=\theta)=0$ |
| 區間估計 | $P(T_1<\theta<T_2)=1-\alpha$ | 區間要短、機率要大 |
| 假設檢定 | $\theta$ 有沒有超過某值 | 統計最重要的部分 |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| (b)、(c) | $t$ 分配、常態母體的信賴區間與檢定 |
| 點估計 | 下一集起：估計量的好壞（不偏、一致……） |
| 區間估計、假設檢定 | 課本第 4 章後半、第 8 章 |

---

## 附：本集一句話總結

> **用 joint mgf 拆成兩個因子證明 $\bar X$ 和 $(X_i-\bar X)$ 獨立，所以 $\bar X\perp S^2$；再用 $\chi^2(n)=\frac{(n-1)S^2}{\sigma^2}+\chi^2(1)$ 和獨立性得 $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$；接著進入統計：因為 $\theta$ 不知道，所以要用隨機樣本做點估計、區間估計或假設檢定。**

---

*筆記依據「統計學」Lec11 錄影逐字稿（whisper large-v3-turbo，1:04:39）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
