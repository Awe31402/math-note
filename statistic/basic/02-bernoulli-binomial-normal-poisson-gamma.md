---
course: 統計學（數理統計，數學系）
episode: 2
lecture: Lec02
date: 待補
video: https://youtu.be/-RmY1CgTK4I
notes: Hogg 8th ed. §3.1 Bernoulli、binomial（p. 155–156）；§1.7 連續型隨機變數（Definition 1.7.1，p. 49）；§3.4 常態分配（p. 186）；§3.2 Poisson（p. 167）、§5.2 Poisson 近似二項（p. 337）；§3.3 Γ 函數與 Γ 分配（p. 173–174）
---

# 第 2 集 · Lec02：Bernoulli、二項、常態、Poisson、Gamma 分配 [▶ 影片](https://youtu.be/-RmY1CgTK4I)

← 上一集：[01](01-random-experiment-random-variable-df.md) ｜ [總目錄](../README.md) ｜ 下一集：[03](03-chi-square-expectation-mean-variance.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 2 集
> **講者**：待補（從課堂舉例看是**交大**的課，見 §5）
> **來源**：YouTube 錄影逐字稿（1:12:19，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §1.7、§3.1–3.4、§5.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 學生插話、老師回應
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「機率」常被聽成「激勵／基粒／肌粒」，「樣本空間」→「樣門空間」，「實數」→「時數／十四」，「服從」→「符蟲／浮蟲」，「二項」→「偶像／all向／奧向」，「Bernoulli」→「Bennuni／本努力／本輪理」，「Poisson」→「普阿松／普華松」，「常態分配」→「常代分貝」，「反曲點」→「緩區點」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Bernoulli 分配](#1-bernoulli-分配)
- [2. 二項分配](#2-二項分配)
- [3. 連續型隨機變數與常態分配](#3-連續型隨機變數與常態分配)
  - [3.1 連續型的定義](#31-連續型的定義)
  - [3.2 常態分配的 pdf 與圖形](#32-常態分配的-pdf-與圖形)
  - [3.3 有了 pdf 就直接積分](#33-有了-pdf-就直接積分)
  - [3.4 pdf 積分＝1 的妙用](#34-pdf-積分1-的妙用)
- [4. Poisson 分配：二項分配的極限](#4-poisson-分配二項分配的極限)
- [5. Poisson 分配的應用](#5-poisson-分配的應用)
- [6. Gamma 函數與 Gamma 分配](#6-gamma-函數與-gamma-分配)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

接著上一集的 Bernoulli 實驗，把幾個常用分配一個一個建立起來。

| 主題 | 課本對應 |
|---|---|
| Bernoulli 分配：從樣本空間導出 pmf | §3.1，p. 155 |
| 二項分配：$n$ 次獨立 Bernoulli 的成功次數 | §3.1，p. 156 |
| 連續型隨機變數、常態分配 | §1.7，p. 49；§3.4，p. 186 |
| Poisson 分配＝二項分配 $n\to\infty$ 的極限 | §3.2，p. 167；§5.2，p. 337 |
| Gamma 函數、Gamma 分配 | §3.3，p. 173 |

**一個用詞差異**：老師對離散和連續都叫「機率密度函數」（probability density function，pdf），記作 $f(x)$。【課本補充】課本把離散的叫 **pmf**（probability mass function，機率質量函數），連續的才叫 pdf。

---

## 1. Bernoulli 分配

[▶ 00:35](https://youtu.be/-RmY1CgTK4I?t=35) 複習上一集：

- 樣本空間 $S=\{s,f\}$（成功、失敗）。
- 機率集合函數：$P(\{s\})=p$，$P(\{f\})=1-p$，$P(\varnothing)=0$，$P(S)=1$。
- 隨機變數：$X(s)=1$，$X(f)=0$。

[▶ 02:39](https://youtu.be/-RmY1CgTK4I?t=159) 討論隨機變數，最重要的是它的**分配**（distribution）。分配可以指 pdf，也可以指分配函數。現在先找 pdf。

[▶ 03:43](https://youtu.be/-RmY1CgTK4I?t=223) $X$ 的值域只有 $\{0,1\}$，是**可數**的，所以 $X$ 是**離散型隨機變數**（discrete random variable）。離散型的 pdf 定義為

$$f(x)=P(X=x).$$

**一點一點算**（都用上一集的「映回去」）：

| $x$ | $X^{-1}(\{x\})$ | $f(x)$ |
|---|---|---|
| $1$ | $\{s\}$（只有 $s$ 被送到 1） | $P(\{s\})=p$ |
| $0$ | $\{f\}$ | $P(\{f\})=1-p$ |
| 其他 $x$ | $\varnothing$（沒有點被送到 $x$） | $P(\varnothing)=0$ |

[▶ 07:07](https://youtu.be/-RmY1CgTK4I?t=427) 注意：pdf 的定義域是**整個 $\mathbb{R}$**，所以「其他點」也要算，答案是 0。

[▶ 08:40](https://youtu.be/-RmY1CgTK4I?t=520) 整理成一個式子（**要背**）：

$$f(x)=\begin{cases}p^x(1-p)^{1-x}, & x=0,1\\ 0, & \text{其他}\end{cases}$$

驗算：$x=1$ → $p^1(1-p)^0=p$；$x=0$ → $p^0(1-p)^1=1-p$。

[▶ 11:15](https://youtu.be/-RmY1CgTK4I?t=675) 做一次 Bernoulli 實驗得到的這個 $X$ 叫 **Bernoulli 隨機變數**，它的分配叫 **Bernoulli 分配**。記號：

$$X\sim \text{Bernoulli}(p).$$

「$\sim$」讀作「服從」。$p$ 是成功機率，通常不知道。

---

## 2. 二項分配

[▶ 12:18](https://youtu.be/-RmY1CgTK4I?t=738) 擴充：把 Bernoulli 實驗**獨立地**（independent）做 $n$ 次。

**隨機變數**：$Y$＝$n$ 次中**成功的次數**（number of successes）。

⚠️ 老師一開始寫成 $X$，[▶ 16:57](https://youtu.be/-RmY1CgTK4I?t=1017) 改成 $Y$，因為後面都用 $Y$。

**Step 1：樣本空間**（[▶ 13:51](https://youtu.be/-RmY1CgTK4I?t=831)）

每個結果是一個長度 $n$ 的序列：

$$S=\{(x_1,x_2,\dots,x_n):\ x_i\in\{s,f\},\ i=1,\dots,n\}.$$

$x_i$ 是第 $i$ 次的結果。每個位置 2 種，所以 $S$ 有 $2^n$ 個點。

例：$(s,f,s,f,f,\dots,f)$ 對應 $Y=2$。但 $(s,s,f,\dots,f)$、$(f,\dots,f,s,s)$ 也都是 $Y=2$。

**Step 2：值域**（[▶ 17:57](https://youtu.be/-RmY1CgTK4I?t=1077)）

$Y\in\{0,1,2,\dots,n\}$。不會是 1.2 次。可數 → 離散型。

**Step 3：pdf**（[▶ 19:28](https://youtu.be/-RmY1CgTK4I?t=1168)）

$f(y)=P(Y=y)$。把 $\{y\}$ 映回 $S$：找出所有「剛好 $y$ 次成功」的序列。

1. **有幾個？** 想成 $n$ 個位置，挑 $y$ 個放 $s$，其餘放 $f$。$s$ 和 $s$ 互換一樣，所以是組合：$\binom{n}{y}$ 個。
2. **它們互斥**（disjoint）：發生其中一個序列，就不會發生另一個。所以總機率＝個別機率相加（公理 3）。
3. **每一個的機率**（[▶ 24:03](https://youtu.be/-RmY1CgTK4I?t=1443)）：各次獨立 → 機率相乘。$y$ 次成功各給 $p$，$n-y$ 次失敗各給 $1-p$：
$$p^y(1-p)^{n-y}.$$
每個序列都一樣。
4. **加起來**：

$$f(y)=\begin{cases}\binom{n}{y}p^y(1-p)^{n-y}, & y=0,1,\dots,n\\ 0, & \text{其他}\end{cases}$$

（[▶ 27:47](https://youtu.be/-RmY1CgTK4I?t=1667) 錄影中斷約 40 秒。）

[▶ 28:28](https://youtu.be/-RmY1CgTK4I?t=1708) 這叫**二項分配**（binomial distribution）。記號：

$$Y\sim b(n,p).$$

[▶ 28:58](https://youtu.be/-RmY1CgTK4I?t=1738) 【口頭】為什麼說「服從」？因為隨機變數落在每一點的機會，都**照那個分配來**。pdf 在某點高，那點就容易出現；低，就不容易出現。

[▶ 30:32](https://youtu.be/-RmY1CgTK4I?t=1832) 要記得：

| 做幾次 Bernoulli | 成功次數的分配 |
|---|---|
| 1 次 | Bernoulli$(p)$ |
| $n$ 次（獨立） | $b(n,p)$ |

---

## 3. 連續型隨機變數與常態分配

### 3.1 連續型的定義

[▶ 31:02](https://youtu.be/-RmY1CgTK4I?t=1862) 分配還有很多連續型的，而且連續型其實比較重要。連續型通常**直接給 pdf**。

> **定義（連續型隨機變數，老師的版本）**：如果 $X$ 的分配函數可以寫成某個非負函數 $f\ge 0$ 的積分
> $$F(x)=P(X\le x)=\int_{-\infty}^{x}f(t)\,dt,$$
> 就叫 $X$ 是連續型隨機變數，$f$ 叫它的 pdf。

【課本補充】課本 Definition 1.7.1（p. 49）的定義不同：**分配函數 $F$ 在每一點都連續**，就叫連續型。能寫成上面那種積分的，課本叫「絕對連續」（absolutely continuous），並說大部分連續型都是這種。老師的定義相當於課本的絕對連續。

### 3.2 常態分配的 pdf 與圖形

[▶ 33:06](https://youtu.be/-RmY1CgTK4I?t=1986)

> **常態分配**（normal distribution）：$X$ 的 pdf 是
> $$f(x)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right],\qquad x\in\mathbb{R}.$$
> $\mu$ 是某個實數（可能不知道），$\sigma>0$。記作 $X\sim N(\mu,\sigma^2)$。

- 值域是整個 $\mathbb{R}$（映成，onto）。
- [▶ 35:42](https://youtu.be/-RmY1CgTK4I?t=2142) $f\ge 0$：$\sqrt{2\pi}>0$、$\sigma>0$、指數函數 $>0$。
- $\mu$、$\sigma^2$ 代表什麼，之後再講。

**圖形**（[▶ 36:44](https://youtu.be/-RmY1CgTK4I?t=2204)）：鐘形。

- 中心在 $x=\mu$：代進去指數是 $e^0=1$，是最高點，所以 $f''(\mu)<0$。
- $x=\mu\pm\sigma$ 是**反曲點**（point of inflection）：$f''(\mu-\sigma)=f''(\mu+\sigma)=0$。
- $|x-\mu|>\sigma$ 凹向上；$|x-\mu|<\sigma$ 凹向下。

【課本補充】驗算反曲點（不是逐字稿內容，是依微積分推導的）：令 $z=(x-\mu)/\sigma$，$f\propto e^{-z^2/2}$。對 $x$ 微兩次：
$$f'(x)=-\frac{x-\mu}{\sigma^2}f(x),\qquad f''(x)=\left[\frac{(x-\mu)^2}{\sigma^4}-\frac{1}{\sigma^2}\right]f(x).$$
$f''=0 \iff (x-\mu)^2=\sigma^2 \iff x=\mu\pm\sigma$。

[▶ 38:52](https://youtu.be/-RmY1CgTK4I?t=2332) 【口頭】「這個 pdf 一定要背下來。期中考之後還不會背，就不用上課了。」因為天天會用。

[▶ 39:53](https://youtu.be/-RmY1CgTK4I?t=2393) $\mu=0$、$\sigma=1$ 時叫**標準常態分配**（standard normal distribution），$N(0,1)$。

### 3.3 有了 pdf 就直接積分

[▶ 40:23](https://youtu.be/-RmY1CgTK4I?t=2423)

$$P(X\in A)=\int_A f(x)\,dx.$$

[▶ 40:53](https://youtu.be/-RmY1CgTK4I?t=2453) 【口頭】照定義，本來要把 $A$ 映回樣本空間 $S$，用 $P$ 去算，很麻煩。有了 pdf 就**不用回去了**，直接積分。就算找不到反導函數，也能用數值方法算。

### 3.4 pdf 積分＝1 的妙用

[▶ 42:58](https://youtu.be/-RmY1CgTK4I?t=2578) **性質**：連續型的 pdf 滿足

$$\int_{-\infty}^{\infty}f(x)\,dx=1.$$

**證明**：左邊＝$P(X\in\mathbb{R})$。映回去：$X^{-1}(\mathbb{R})=S$（每個樣本點都被送到某個實數）。所以＝$P(S)=1$。

[▶ 45:03](https://youtu.be/-RmY1CgTK4I?t=2703) 【口頭】應用：研究所考
$$\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}\,\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]dx$$
你找不到反導函數，但答案就是 1，因為它是常態 pdf。

【課堂討論】[▶ 45:34](https://youtu.be/-RmY1CgTK4I?t=2734) 老師把積分下限寫成 0，學生指出應是 $-\infty$。老師更正：中心在 $\mu$ 不在 0，所以 0 到 $\infty$ 的積分不是 $1/2$。

---

## 4. Poisson 分配：二項分配的極限

[▶ 46:40](https://youtu.be/-RmY1CgTK4I?t=2800)

> **定理**：$X\sim b(n,p)$。令 $\lambda=np$ **固定**，讓 $n\to\infty$，則對每個 $x=0,1,2,\dots$
> $$\binom{n}{x}p^x(1-p)^{n-x}\ \longrightarrow\ \frac{\lambda^x e^{-\lambda}}{x!}.$$

**證明**（[▶ 48:45](https://youtu.be/-RmY1CgTK4I?t=2925)）：

**Step 1：代 $p=\lambda/n$。**
$$\binom{n}{x}p^x(1-p)^{n-x}=\frac{n!}{x!\,(n-x)!}\left(\frac{\lambda}{n}\right)^x\left(1-\frac{\lambda}{n}\right)^{n-x}.$$

**Step 2：把和 $n$ 無關的提出來**（$x!$、$\lambda^x$），並約分 $\dfrac{n!}{(n-x)!}=n(n-1)\cdots(n-x+1)$：
$$=\frac{\lambda^x}{x!}\cdot\frac{n(n-1)\cdots(n-(x-1))}{n^x}\cdot\left(1-\frac{\lambda}{n}\right)^{n}\cdot\left(1-\frac{\lambda}{n}\right)^{-x}.$$

**Step 3：分子有 $x$ 項，分母有 $x$ 個 $n$，一項配一個 $n$：**
$$\frac{n(n-1)\cdots(n-x+1)}{n^x}=1\cdot\left(1-\frac1n\right)\left(1-\frac2n\right)\cdots\left(1-\frac{x-1}{n}\right).$$

**Step 4：取極限 $n\to\infty$**（$x$ 固定）：

- 每個 $1-\frac{k}{n}\to 1$；有限個相乘 → $1$（極限存在時，乘積的極限＝極限的乘積）。
- $\left(1+\frac{-\lambda}{n}\right)^n\to e^{-\lambda}$（微積分：$\left(1+\frac{a}{n}\right)^n\to e^a$）。
- $\left(1-\frac{\lambda}{n}\right)^{-x}\to 1^{-x}=1$（$x$ 是固定的有限次方）。

所以極限是 $\dfrac{\lambda^x}{x!}e^{-\lambda}$。∎

[▶ 55:07](https://youtu.be/-RmY1CgTK4I?t=3307) 極限這個 pdf 叫 **Poisson 分配**。

【課堂討論】[▶ 55:43](https://youtu.be/-RmY1CgTK4I?t=3343) 學生問 $\left(1-\frac{\lambda}{n}\right)^{-x}$ 那項怎麼處理、$n\to\infty$ 時 $p$ 怎樣。老師回答：$\lambda=np$ 要**固定**，所以 $n\to\infty$ 時 $p$ 必須越來越小。這是一個**近似**，理論上不是很漂亮。

[▶ 56:45](https://youtu.be/-RmY1CgTK4I?t=3405) 【口頭】實用意義：$n$ 很大、$p$ 夠小、$np$ 不大（老師說應用上大約 $np\le 5$ 或 $3$）時，用 Poisson 算的機率和二項算的非常接近。$np$ 很大就不準。

> **Poisson 分配**（[▶ 58:17](https://youtu.be/-RmY1CgTK4I?t=3497)，**要背**）：
> $$f(x)=\begin{cases}\dfrac{\lambda^x e^{-\lambda}}{x!}, & x=0,1,2,\dots\\ 0, & \text{其他}\end{cases}$$
> 記作 $X\sim\text{Poisson}(\lambda)$。$\lambda$ 通常不知道。

【課本補充】課本 §3.2（p. 167）用 $m$ 或 $\lambda$ 當參數；§5.2（p. 337）用分配函數的收斂（convergence in distribution）正式證明這個近似。

[▶ 62:50](https://youtu.be/-RmY1CgTK4I?t=3770) 【口頭】要有的概念：

| 做幾次 Bernoulli | 成功次數的分配 |
|---|---|
| $n$ 次（$n$ 固定） | $b(n,p)$ |
| 「無窮多次」（$n\to\infty$，$np=\lambda$ 固定） | Poisson$(\lambda)$ |

「不是只背公式，要有這樣的概念。」

---

## 5. Poisson 分配的應用

[▶ 58:47](https://youtu.be/-RmY1CgTK4I?t=3527) 【口頭】

- **電話總機**：以前打長途電話（新竹打高雄）要經過電信局總機小姐轉接。二十年前打到交大也要先打總機（老師提到交大總機號碼 03-5712121），再轉宿舍。學校要知道今天大概多少人打進來，才知道要配幾個總機。
  - 全台灣每個人都**可能**打來，也可能不打 → 每人是一次 Bernoulli 實驗。
  - 人數很多（老師說五百萬），每人打來機率很小 → 打進來的人數近似 Poisson。
  - 「微積分討論數列收斂，$n=30$ 就很接近極限了，五百萬當然夠大。」
- **醫院**：新竹市每個人可能來看病也可能不來。排 20 個醫生只來 3 個病人虧大；排 2 個醫生病人太多也虧大。來看病人數近似 Poisson。
- 這類分配早期多是美國 **Bell 實驗室**（當時最大的電話公司）研究出來的。

---

## 6. Gamma 函數與 Gamma 分配

[▶ 63:20](https://youtu.be/-RmY1CgTK4I?t=3800)

> **Gamma 函數**（gamma function）：對 $\alpha>0$，
> $$\Gamma(\alpha)=\int_0^{\infty}x^{\alpha-1}e^{-x}\,dx.$$

**性質**（[▶ 66:01](https://youtu.be/-RmY1CgTK4I?t=3961)）：

1. $\Gamma(\alpha)=(\alpha-1)\Gamma(\alpha-1)$，$\alpha>1$。

   **推導**（分部積分，老師只說「用分部積分」，以下步驟是依此推的）：取 $u=x^{\alpha-1}$，$dv=e^{-x}dx$，$v=-e^{-x}$：
   $$\Gamma(\alpha)=\left[-x^{\alpha-1}e^{-x}\right]_0^{\infty}+(\alpha-1)\int_0^\infty x^{\alpha-2}e^{-x}dx=0+(\alpha-1)\Gamma(\alpha-1).$$
   （$\alpha>1$ 時邊界項在 0 和 $\infty$ 都是 0。）

2. $\Gamma(1)=\int_0^\infty e^{-x}dx=1$。

3. $n$ 是正整數：反覆用性質 1，
   $$\Gamma(n)=(n-1)(n-2)\cdots 2\cdot 1\cdot\Gamma(1)=(n-1)!.$$

4. [▶ 68:17](https://youtu.be/-RmY1CgTK4I?t=4097) $\Gamma\left(\frac12\right)=\sqrt{\pi}$。老師說需要數學證明，沒證；工程數學通常會證。

[▶ 68:49](https://youtu.be/-RmY1CgTK4I?t=4129) Gamma 函數的主要用途：定義 **Gamma 分配**。

> **Gamma 分配**（[▶ 70:09](https://youtu.be/-RmY1CgTK4I?t=4209)）：$\alpha>0$，$\beta>0$，
> $$f(x)=\begin{cases}\dfrac{1}{\Gamma(\alpha)\beta^{\alpha}}x^{\alpha-1}e^{-x/\beta}, & x>0\\ 0, & x\le 0\end{cases}$$
> 記作 $X\sim\Gamma(\alpha,\beta)$。

⚠️ 逐字稿缺字：[▶ 69:20](https://youtu.be/-RmY1CgTK4I?t=4160) 這段 whisper 輸出一長串重複的「α」，是轉錄錯誤（幻聽），內容依 [▶ 70:09](https://youtu.be/-RmY1CgTK4I?t=4209) 的口述和課本 §3.3（p. 174）的公式重建。

**圖形**（[▶ 71:10](https://youtu.be/-RmY1CgTK4I?t=4270)）：$x<0$ 是 0；$x>0$ 很快上升，再慢慢下降，尾巴拖到無窮。

詳細性質下次講。下課。

---

## 7. 一頁速查表

| 分配 | pdf（pmf） | 值域 | 來源 |
|---|---|---|---|
| Bernoulli$(p)$ | $p^x(1-p)^{1-x}$ | $x=0,1$ | 做 1 次 Bernoulli 的成功次數 |
| $b(n,p)$ | $\binom{n}{x}p^x(1-p)^{n-x}$ | $x=0,\dots,n$ | 獨立做 $n$ 次的成功次數 |
| Poisson$(\lambda)$ | $\dfrac{\lambda^x e^{-\lambda}}{x!}$ | $x=0,1,2,\dots$ | $b(n,p)$，$np=\lambda$，$n\to\infty$ |
| $N(\mu,\sigma^2)$ | $\dfrac{1}{\sqrt{2\pi}\sigma}e^{-(x-\mu)^2/(2\sigma^2)}$ | $\mathbb{R}$ | 直接給定 |
| $\Gamma(\alpha,\beta)$ | $\dfrac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}$ | $x>0$ | 直接給定 |

**二項 pdf 的關鍵一步**：「剛好 $y$ 次成功」的序列有 $\binom{n}{y}$ 個、彼此互斥、每個機率 $p^y(1-p)^{n-y}$（獨立相乘）。

**Poisson 極限的關鍵一步**：
$$\frac{n(n-1)\cdots(n-x+1)}{n^x}\to 1,\quad \left(1-\frac{\lambda}{n}\right)^n\to e^{-\lambda},\quad \left(1-\frac{\lambda}{n}\right)^{-x}\to 1.$$

**pdf 積分＝1**：$\int_{\mathbb{R}}f=P(X^{-1}(\mathbb{R}))=P(S)=1$。可以拿來算「找不到反導函數」的積分。

**常態圖形**：最高點 $x=\mu$；反曲點 $x=\mu\pm\sigma$（$f''=[(x-\mu)^2/\sigma^4-1/\sigma^2]f$）。

**Gamma 函數**：
- $\Gamma(\alpha)=(\alpha-1)\Gamma(\alpha-1)$（分部積分）
- $\Gamma(1)=1$，$\Gamma(n)=(n-1)!$
- $\Gamma(1/2)=\sqrt\pi$

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Gamma 分配 | 下一集繼續講它的性質、特例 |
| 常態分配 $\mu$、$\sigma^2$ 的意義 | 期望值、變異數 |
| Poisson 近似二項 | 分配收斂（課本第 5 章） |

---

## 附：本集一句話總結

> **從樣本空間一步步導出 Bernoulli 和二項分配；二項分配在 $n\to\infty$、$np=\lambda$ 固定時變成 Poisson；連續型分配（常態、Gamma）直接給 pdf，有了 pdf 就直接積分算機率，不用再回到樣本空間。**

---

## ⚠️ 待確認清單

1. 講者姓名、上課學期：逐字稿沒提到（只知道是交大）。

---

*筆記依據「統計學」Lec02 錄影逐字稿（whisper large-v3-turbo，1:12:19）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
