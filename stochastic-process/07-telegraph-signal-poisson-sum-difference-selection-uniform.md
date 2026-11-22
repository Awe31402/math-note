---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 7
lecture: Lec 9-1 General Concepts — Definitions (6/7)
date: 待補
video: https://youtu.be/8VOxDURP6TI
notes: Papoulis & Pillai 4th ed. §9-1（Example 9-6 telegraph signal，式 (9-18)–(9-19)，pp. 379–380；More on Poisson processes，式 (9-20)–(9-28)，pp. 380–383）
---

# 第 7 集 · Lec 9-1 (6/7)：電報訊號、Poisson 的和與差、隨機篩選、Poisson 點是均勻分布排序 [▶ 影片](https://youtu.be/8VOxDURP6TI)

← 上一集：[06](06-independent-increment-normal-riemann-lebesgue-poisson.md) ｜ [總目錄](README.md) ｜ 下一集：[08](08-stationarity-sss-wss-circular-symmetry-gaussian.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 7 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（43:23，whisper large-v3-turbo）＋ Papoulis §9-1（pp. 379–383）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Poisson」→「Posome／保重／頗重／Proson／Polizone／波縱」，「奇數」→「激數／基數／G數」，「階乘」→「階層」，「e 的」→「1 的」（例如 $e^{-\lambda t}$ 唸成「1 的負 λt」），「1/2」→「1分之1」，「factorial」→「victorial」，「transient」→「trension」，「asymptotically」→「asymptatically／asynthetically」，「Bessel function」→「Basal Function」，「偏微分方程」→「偏微微分方程式」，「total probability」→「高杯先入我／背先入我」，「binomial」→「摆弄没有」，「標記」→「助记」，「因式」→「音式」，「話務」→「化物／畫物」，「封包」→「風暴／風包」，「穩態」→「穩泰」，「Pólya contagion」→「polyocontagion」，「autocorrelation」→「Auto-Carrison／autocritic」。以下一律用正確的字。

> **接上一集**：上一集算了 Poisson 過程的平均和自相關，並學到解題套路：**先用性質 2（不重疊區間獨立）拆開，再用性質 1（Poisson 分布）算**。這一集用同樣的套路再算幾個 Poisson 相關的例子，最後得到 Poisson 最重要的直觀：**Poisson 點就是均勻分布的點排序後的結果**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 要有操作型的思考](#1-要有操作型的思考)
- [2. 半隨機電報訊號](#2-半隨機電報訊號)
  - [2.1 定義](#21-定義)
  - [2.2 平均](#22-平均)
  - [2.3 自相關](#23-自相關)
  - [2.4 解讀](#24-解讀)
  - [2.5 全隨機電報訊號](#25-全隨機電報訊號)
- [3. Poisson 過程的和：還是 Poisson](#3-poisson-過程的和還是-poisson)
- [4. Poisson 過程的差：不是 Poisson](#4-poisson-過程的差不是-poisson)
- [5. 隨機篩選：還是 Poisson](#5-隨機篩選還是-poisson)
- [6. Poisson 和 binomial](#6-poisson-和-binomial)
- [7. Poisson 點 = 均勻分布排序](#7-poisson-點--均勻分布排序)
- [8. 預告：平穩性](#8-預告平穩性)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 半隨機／全隨機電報訊號 | [▶ 01:01](https://youtu.be/8VOxDURP6TI?t=61) | Example 9-6，式 (9-18)、(9-19)，pp. 379–380 |
| Poisson 的和、差 | [▶ 14:53](https://youtu.be/8VOxDURP6TI?t=893) | 式 (9-20)–(9-23)，pp. 380–381 |
| 隨機篩選 | [▶ 22:29](https://youtu.be/8VOxDURP6TI?t=1349) | 式 (9-24)、(9-25)，p. 381 |
| Poisson 和 binomial、均勻 | [▶ 28:46](https://youtu.be/8VOxDURP6TI?t=1726) | 式 (9-26)–(9-28)，pp. 382–383 |
| 平穩性（預告） | [▶ 41:43](https://youtu.be/8VOxDURP6TI?t=2503) | p. 387 |

---

## 1. 要有操作型的思考

[▶ 00:00](https://youtu.be/8VOxDURP6TI?t=0)【口頭】

- 書上很多範例，要去想每個範例的**操作意義**。將來量測時都會去算兩個過程的自相關。
- 例：老師參加一個口試，學生量 12 個地方的腦波，算自相關，看這邊和那邊的腦波有沒有關係。如果發現的確像 Poisson 過程，就很厲害。實際不會那麼單純，但透過觀察到的現象，可以**反推原來的隨機過程是怎麼組成的**。
- 不是算完就結束，要想結果和原來的結構之間的關聯。

---

## 2. 半隨機電報訊號

### 2.1 定義

[▶ 01:31](https://youtu.be/8VOxDURP6TI?t=91) 打電報：要嘛 1、要嘛 0（或 $\pm 1$），「答答答答」。每打一下當成一個隨機點，用 Poisson 過程來 model。

> **半隨機電報訊號** (semirandom telegraph signal)：用 Poisson 點 $t_i$（參數 $\lambda$ 為常數）定義
> $$X(t)=\begin{cases}+1,&(0,t)\ \text{內有偶數個點}\\-1,&(0,t)\ \text{內有奇數個點}\end{cases}$$

圖形：每遇到一個 Poisson 點就翻轉一次，在 $+1$、$-1$ 之間跳。

### 2.2 平均

[▶ 02:35](https://youtu.be/8VOxDURP6TI?t=155) 先猜：$+1$、$-1$ 應該會對消，平均很接近 0，但不會完全是 0。

記 $p(k)=P\{n(0,t)=k\}=e^{-\lambda t}\frac{(\lambda t)^k}{k!}$。

$$P\{X(t)=1\}=p(0)+p(2)+p(4)+\cdots=e^{-\lambda t}\left[1+\frac{(\lambda t)^2}{2!}+\frac{(\lambda t)^4}{4!}+\cdots\right]=e^{-\lambda t}\cosh\lambda t$$
$$P\{X(t)=-1\}=p(1)+p(3)+\cdots=e^{-\lambda t}\left[\lambda t+\frac{(\lambda t)^3}{3!}+\cdots\right]=e^{-\lambda t}\sinh\lambda t$$

**記法**【口頭】：$\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$，把減號全換成加號就是 $\cosh x$；$\sin x$ 同理換成 $\sinh x$。
$$\cosh x=\frac{e^{x}+e^{-x}}{2},\qquad\sinh x=\frac{e^{x}-e^{-x}}{2}.$$

所以
$$E[X(t)]=1\cdot e^{-\lambda t}\cosh\lambda t+(-1)\cdot e^{-\lambda t}\sinh\lambda t=e^{-\lambda t}\left(\cosh\lambda t-\sinh\lambda t\right)=e^{-\lambda t}\cdot e^{-\lambda t}=e^{-2\lambda t}.$$

（最後一步：$\cosh x-\sinh x=e^{-x}$。）

### 2.3 自相關

[▶ 05:10](https://youtu.be/8VOxDURP6TI?t=310) 一定先用**性質 2**拆。這裡就看出 **independent 比 uncorrelated 有用**：要用的是機率相乘，不只是相關為 0。

設 $t_1>t_2$，$\tau=t_1-t_2$。$X(t_1)X(t_2)$ 只有四種情況：

$$R(t_1,t_2)=P(\text{偶},\text{偶})\cdot(+1)+P(\text{奇},\text{奇})\cdot(+1)+P(\text{偶},\text{奇})\cdot(-1)+P(\text{奇},\text{偶})\cdot(-1),$$

（第一個「偶／奇」指 $(0,t_2)$ 的點數，第二個指 $(0,t_1)$ 的點數。）

**Step 1：拆成不重疊區間。** $(0,t_1)=(0,t_2)\cup(t_2,t_1)$。0 到 $t_2$ 有 6 個、0 到 $t_1$ 有 8 個，則 $t_2$ 到 $t_1$ 有 2 個。所以：

- 偶、偶 ⇔ $(0,t_2)$ 偶 且 $(t_2,t_1)$ 偶。
- 奇、奇 ⇔ $(0,t_2)$ 奇 且 $(t_2,t_1)$ 偶（奇數加偶數才是奇數）。
- 偶、奇 ⇔ $(0,t_2)$ 偶 且 $(t_2,t_1)$ 奇。
- 奇、偶 ⇔ $(0,t_2)$ 奇 且 $(t_2,t_1)$ 奇。

**Step 2：兩段不重疊 → 獨立（性質 2）**，交集的機率 = 個別機率相乘。記 $E_2,O_2$ 為 $(0,t_2)$ 偶／奇，$E_\tau,O_\tau$ 為 $(t_2,t_1)$ 偶／奇：
$$R=P(E_2)P(E_\tau)+P(O_2)P(E_\tau)-P(E_2)P(O_\tau)-P(O_2)P(O_\tau).$$

**Step 3：因式分解**（四項變成「兩項相加」乘「兩項相減」）：
$$R=\underbrace{\left[P(E_2)+P(O_2)\right]}_{=1}\left[P(E_\tau)-P(O_\tau)\right].$$
第一個括號是 1，因為 $(0,t_2)$ 的點數不是奇數就是偶數。

**Step 4：用性質 1。** $(t_2,t_1)$ 長度 $\tau$，同 2.2 的計算：
$$R=e^{-\lambda\tau}\cosh\lambda\tau-e^{-\lambda\tau}\sinh\lambda\tau=e^{-2\lambda\tau}.$$

**Step 5：$t_1<t_2$** 照算一遍，變成 $t_2-t_1$。總結：
$$\boxed{R(t_1,t_2)=e^{-2\lambda|t_1-t_2|}}$$

老師說【口頭】：不用背怎麼算，因為變化很多；**永遠記得想辦法用第二個性質拆解**，大部分問題就能解決。

【課本補充】Papoulis 式 (9-18)、(9-19)，pp. 379–380。課本的算法略不同：先算條件機率 $P\{X(t_1)=1\mid X(t_2)=1\}=e^{-\lambda\tau}\cosh\lambda\tau$，再乘 $P\{X(t_2)=1\}$ 得四個聯合機率，然後「省略細節」得到 (9-19)。

### 2.4 解讀

[▶ 10:15](https://youtu.be/8VOxDURP6TI?t=615)

- 平均 $e^{-2\lambda t}$：很小，趨近 0。
- 自相關：兩個時間**相距越遠，越趨近 0**。今天跟明天、後天、大後天，相關越來越弱。
- 和上一集的 Poisson 計數過程（相關不衰減）**完全不同**，反而和一般通訊訊號比較像。

為什麼？只是稍微改了映射的定義，性質就完全不同【口頭】：

- 電報訊號**不是累積量**，它是有界的 (bounded)，只在 $\pm 1$ 之間。
- 又有獨立增量。
- 不是累積量 + 獨立增量 → 關係應該越來越弱。所以結果很合理：今天打的電報跟後天的幾乎沒關係。

### 2.5 全隨機電報訊號

[▶ 11:48](https://youtu.be/8VOxDURP6TI?t=708)

- 為什麼叫 **semi**（半）random？因為 $X(0)=1$ **保證是 1**，一端被固定住了，沒有完全隨機。
- **全隨機** (full random)：起點也隨機。令
$$Y(t)=a\,X(t),$$
  $a$ 取 $+1$、$-1$ 機率各半，且和 $X(t)$ 獨立。這叫**隨機電報訊號** (random telegraph signal)。全隨機的分析通常比較容易。

性質（由 $E[a]=0$、$E[a^2]=1$、$a$ 和 $X$ 獨立）：
$$E[Y(t)]=E[a]\,E[X(t)]=0,\qquad R_{YY}(t_1,t_2)=E[a^2]\,E[X(t_1)X(t_2)]=e^{-2\lambda|t_1-t_2|}.$$

- 平均**完全是 0**：任何時間都是一半機率 $+1$、一半 $-1$，非常對稱，沒有**暫態** (transient)。
- 自相關**完全一樣**，只改變了平均。
- 半隨機有暫態：$P\{X(t)=1\}=e^{-\lambda t}\cosh\lambda t=\frac12\left(1+e^{-2\lambda t}\right)$，和 1/2 差一個隨時間越來越小的調整。漸近地 (asymptotically)，兩者統計一樣。

為什麼調整會越來越小？【口頭】因為**離被鎖住的那一點越來越遠**。一個隨機過程如果某一點被鎖住，離它很近時一定被它限制，離得遠才比較隨機；如果某個時間又被鎖定，就要重新開始。量測時：如果結果是全隨機的，表示連起點都是隨機的；如果是半隨機，表示某部分被鎖住了，但漸近上還是趨近 0。

【課本補充】Papoulis p. 380：「當 $t\to\infty$，$X(t)$ 和 $Y(t)$ 的統計漸近相等。」

---

## 3. Poisson 過程的和：還是 Poisson

[▶ 14:53](https://youtu.be/8VOxDURP6TI?t=893)

工程（尤其網路）上最常問：交換機、路由器 (router) 有好多流量進來，每個都是 Poisson，加起來是什麼？

> 若 $X_1(t)$、$X_2(t)$ 是**獨立**的 Poisson 過程，參數 $\lambda_1t$、$\lambda_2t$，則 $Z(t)=X_1(t)+X_2(t)$ 是 Poisson 過程，參數 $(\lambda_1+\lambda_2)t$。

- 就像高斯加高斯是高斯，**Poisson 加 Poisson 還是 Poisson**，以前非常喜歡用。
- 要證明，**兩個性質都要證**：任何區間的點數是 Poisson；不重疊區間獨立。

【課本補充】Papoulis p. 380 說這「easily follows」，引用 (6-86)。

---

## 4. Poisson 過程的差：不是 Poisson

[▶ 15:54](https://youtu.be/8VOxDURP6TI?t=954)

直觀上一定不是：Poisson 是**計數**，值是 $0,1,2,\dots$。兩個相減，8 減 12 是 $-4$，Poisson 沒有 $-4$。但分布還是可以算（有時要比較兩個 Poisson 流量的差異）。

$$Y(t)=X_1(t)-X_2(t),\qquad X_1,X_2\ \text{獨立，參數}\ \lambda_1t,\ \lambda_2t.$$

**Step 1：全機率。** 差 $n$ 個：一個是 $n+k$，另一個是 $k$。
$$P\{Y(t)=n\}=\sum_k P\{X_1(t)=n+k\}\,P\{X_2(t)=k\}.$$
因為 $X_1,X_2\ge 0$，$k\ge 0$ 且 $n+k\ge 0$，所以 $k$ 從 $\max(0,-n)$ 加到 $\infty$。乘積是因為獨立。

**Step 2：代入 Poisson。**
$$P\{Y(t)=n\}=\sum_{k\ge\max(0,-n)}e^{-\lambda_1t}\frac{(\lambda_1t)^{n+k}}{(n+k)!}\,e^{-\lambda_2t}\frac{(\lambda_2t)^{k}}{k!}.$$

**Step 3：讓求和從 0 開始。** 令 $\tilde{k}=k-\max(0,-n)$，$\tilde{k}=0,1,2,\dots$。

**Step 4：整理。** 把和 $k$ 無關的 $e^{-\lambda_1t}e^{-\lambda_2t}$、$(\lambda_1/\lambda_2)^{n/2}$ 拉出去。不論 $n$ 正負，分母都可以寫成 $(\tilde{k}+|n|)!\,\tilde{k}!$（例：$n<0$ 時 $\max(0,-n)=-n=|n|$）。所以結果**只跟 $|n|$ 有關**（除了 $(\lambda_1/\lambda_2)^{n/2}$ 這個調整）：差的分布有一種對稱的樣子。

**Step 5：認出 Bessel 函數。**
$$\boxed{P\{Y(t)=n\}=e^{-(\lambda_1+\lambda_2)t}\left(\frac{\lambda_1}{\lambda_2}\right)^{n/2}I_{|n|}\left(2\sqrt{\lambda_1\lambda_2}\,t\right),\qquad n=0,\pm1,\pm2,\dots}$$
其中 $I_n(x)=\sum_{k=0}^{\infty}\frac{(x/2)^{n+2k}}{k!(n+k)!}$ 是 $n$ 階**修正 Bessel 函數** (modified Bessel function)。

老師說【口頭】：Bessel 函數在通訊上常出現（數位通訊算錯誤率時也會），不是巧合：它是某種二階微分方程的解。網路分析中，如果流量是 Poisson，要算差距的分布，可以用這個結果。計算回去自己練習，他比較喜歡講觀念。

【課本補充】Papoulis 式 (9-20)–(9-23)，pp. 380–381；並有 $E[Y(t)]=(\lambda_1-\lambda_2)t$，$\text{Var}[Y(t)]=(\lambda_1+\lambda_2)t$（式 (9-23)）。

---

## 5. 隨機篩選：還是 Poisson

[▶ 22:29](https://youtu.be/8VOxDURP6TI?t=1349)

**例**：銀行櫃台，顧客到達的時間是 Poisson（顧客彼此不協調，Poisson model 通常很準）。把男顧客、女顧客分成兩組，**每一組還是 Poisson**。網路上：把具有某個特色的封包標記 (tag／mark) 出來，還是 Poisson。

> **隨機篩選** (random selection of Poisson points)：$X(t)$ 是參數 $\lambda t$ 的 Poisson 過程，每個點**獨立地**以機率 $p$ 被標記。$Y(t)$ = $(0,t)$ 內被標記的點數，$Z(t)$ = 沒被標記的點數。則
> $$Y(t)\sim P(\lambda pt),\qquad Z(t)\sim P(\lambda qt),\qquad q=1-p,$$
> 而且兩者是獨立的 Poisson 過程。

**證明性質 1（只證 $Y$；$Z$ 同理）** [▶ 25:35](https://youtu.be/8VOxDURP6TI?t=1535)：

**Step 1：全機率。** $Y(t)=k$ ⇔ 有 $X(t)=n$ 個點、其中恰好 $k$ 個被標記，$n=k,k+1,\dots$。
$$P\{Y(t)=k\}=\sum_{n=k}^{\infty}P\{k\ \text{個被標記}\mid X(t)=n\}\,P\{X(t)=n\}.$$

**Step 2：** 標記是獨立的，$n$ 個裡標 $k$ 個是 binomial；$X(t)$ 是 Poisson：
$$=\sum_{n=k}^{\infty}\binom{n}{k}p^kq^{n-k}\,e^{-\lambda t}\frac{(\lambda t)^n}{n!}.$$
到這一步問題已經解決，剩下是整理。

**Step 3：整理。** $\binom{n}{k}\frac{1}{n!}=\frac{1}{k!(n-k)!}$，把和 $n$ 無關的拉出去，令 $r=n-k$：
$$=e^{-\lambda t}\frac{(\lambda pt)^k}{k!}\sum_{r=0}^{\infty}\frac{(\lambda qt)^r}{r!}=e^{-\lambda t}\frac{(\lambda pt)^k}{k!}e^{\lambda qt}=e^{-\lambda pt}\frac{(\lambda pt)^k}{k!}.$$
（求和是指數函數的泰勒展開；$1-q=p$。）

**還沒證完！** 老師強調【口頭】：以前同學常以為這樣就證完了。要證 Poisson **兩個性質都要**：還要證 $Y$ 在不重疊區間的點數獨立（機率相乘）。這留給大家想。

**直觀**【口頭】：

- Poisson 可以**無限切割**，切得很細也沒關係；加起來也沒關係。都是 Poisson。就像高斯：切割是高斯，相加是高斯。（老師問：高斯減高斯是不是高斯？——是，所以高斯的問題通常更好解決。）
- Poisson 和高斯是兩個很重要的分布，都是某種**極限分布**，很多東西的和會發生。老師記得有人證明：網路上一個流量經過無限多次 shaping，最後一定趨向 Poisson（有條件）。所以大型網路常觀察到 Poisson。

【課本補充】Papoulis 式 (9-24)、(9-25)，p. 381。例：顧客到達是 Poisson($\lambda t$)，是男性的機率 $p$，則男顧客是 Poisson($\lambda pt$)，女顧客是獨立的 Poisson($\lambda qt$)。

---

## 6. Poisson 和 binomial

[▶ 28:46](https://youtu.be/8VOxDURP6TI?t=1726) 上面的證明裡出現了 binomial。這不是巧合，它引出 Poisson 最重要的性質。

> 對 $t_1<t_2$：
> $$P\{X(t_1)=k\mid X(t_2)=n\}=\binom{n}{k}\left(\frac{t_1}{t_2}\right)^k\left(1-\frac{t_1}{t_2}\right)^{n-k},\qquad k=0,1,\dots,n.$$
> 也就是給定 $(0,t_2)$ 有 $n$ 個點，$(0,t_1)$ 裡的點數是 $B\left(n,\frac{t_1}{t_2}\right)$。

例：銀行早上 9 點到下午 3 點，今天服務了 8 個顧客，早上來 3 個、下午來 5 個的機率是多少？剛好是 binomial。

⚠️ 逐字稿缺字：[▶ 31:22](https://youtu.be/8VOxDURP6TI?t=1882) 字幕說「剛好是 5 取 3 的 binomial」，依公式應是「8 取 3」（$n=8$、$k=3$）。

**證明：**

**Step 1：條件機率的定義** $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$：
$$P\{X(t_1)=k\mid X(t_2)=n\}=\frac{P\{X(t_1)=k,\ X(t_2)=n\}}{P\{X(t_2)=n\}}.$$

**Step 2：先想性質 2，拆成不重疊區間。** 0 到 $t_1$ 來 $k$ 個、0 到 $t_2$ 來 $n$ 個 ⇔ 0 到 $t_1$ 來 $k$ 個、$t_1$ 到 $t_2$ 來 $n-k$ 個：
$$=\frac{P\{X(t_1)=k\}\,P\{n(t_1,t_2)=n-k\}}{P\{X(t_2)=n\}}.$$
（分子拆成相乘是因為獨立增量。）

**Step 3：最後才代性質 1（Poisson）。**
$$=\frac{e^{-\lambda t_1}\frac{(\lambda t_1)^k}{k!}\cdot e^{-\lambda(t_2-t_1)}\frac{[\lambda(t_2-t_1)]^{n-k}}{(n-k)!}}{e^{-\lambda t_2}\frac{(\lambda t_2)^n}{n!}}.$$

**Step 4：整理。** 指數部分 $e^{-\lambda t_1}e^{-\lambda(t_2-t_1)}=e^{-\lambda t_2}$ 和分母抵消，$\lambda^n$ 也抵消：
$$=\frac{n!}{k!(n-k)!}\cdot\frac{t_1^k(t_2-t_1)^{n-k}}{t_2^n}=\binom{n}{k}\left(\frac{t_1}{t_2}\right)^k\left(1-\frac{t_1}{t_2}\right)^{n-k}.$$ ∎

**討論** [▶ 33:28](https://youtu.be/8VOxDURP6TI?t=2008)：

- binomial 的 $p=\frac{t_1}{t_2}$，就是**時間長度的比例**。
- 9 點到 3 點共 6 小時，早上 9 點到 12 點共 3 小時，$p=\frac36=\frac12$：給定一天來 8 個，早上和下午**各切一半**，最可能是早上 4 個、下午 4 個。
- 如果看第一個小時，就切 $\frac16$，剩下 $\frac56$。非常均勻 (uniform)。
- 所以 Poisson 雖然用兩個性質定義，Poisson 點好像有**均勻**的含義在裡面。

老師說【口頭】：數學算法過一兩年就忘了，但觀念可能留很久，變成你的直觀。

【課本補充】Papoulis 式 (9-26)，p. 382。

---

## 7. Poisson 點 = 均勻分布排序

[▶ 35:00](https://youtu.be/8VOxDURP6TI?t=2100)

**極端情況：一整天只來一個人。** 賣牛肉麵，今天生意很差只來一個人，想預測他什麼時候來，只在那時開門。【口頭】

給定 $X(T)=1$，那唯一的 Poisson 點 $\mathbf{t}_1$ 在 $(0,t)$ 內的機率：用第 6 節的公式，$n=1$、$k=1$、$t_2=T$：
$$P\{\mathbf{t}_1\le t\mid X(T)=1\}=P\{X(t)=1\mid X(T)=1\}=\binom11\left(\frac{t}{T}\right)^1\left(1-\frac{t}{T}\right)^0=\frac{t}{T}.$$

這正是 $(0,T)$ 上**均勻分布**的 CDF。所以：任何一個顧客、一個封包、一輛要上高速公路的車，在你看的區間裡都是**均勻的**。

**一般情況：給定一天來 $n$ 個人** [▶ 37:05](https://youtu.be/8VOxDURP6TI?t=2225)

> **Poisson 點的工程直觀**：給定 $(0,T)$ 內有 $n$ 個 Poisson 點 $\mathbf{t}_1<\dots<\mathbf{t}_n$，它們的分布等於：
> 1. 在 $(0,T)$ 上**獨立地**產生 $n$ 個**均勻分布**的點 $s_1,\dots,s_n$（i.i.d. uniform）；
> 2. 把它們**由小到大排序** (sorting)。
>
> 排序後的結果叫 **order statistic**（順序統計量）。

例：9 點到 3 點（6 小時），$n=8$。用程式產生 8 個均勻時間：第一個 10:10、第二個 14:03、第三個又倒回 13:05……**沒有順序**（第三個不一定比第二個大）。最後一個 9:42。把 8 個時間排序，就是 Poisson 點。

⚠️ 逐字稿缺字：[▶ 37:05](https://youtu.be/8VOxDURP6TI?t=2225) 老師說投影片「這邊有寫錯，這邊都是 N 才對」，應是 $t_1,\dots,t_n$。

意義【口頭】：

- 所以**只要所有顧客彼此不協調**，每個人在區間內自由選一個時間、任何時間機率一樣，就會產生 Poisson。你可能 1:30 去、他 10 點去、另一個 11 點去，彼此無關。
- Poisson 封包流量就是：大家都沒關係，以整個區間為基礎，我可能比你早或晚，排序後就是 Poisson 點中的某個順序。
- **怎麼模擬 Poisson 流量**：要 1 萬個封包，就用電腦現成的均勻亂數（RND）產生 1 萬個獨立的均勻點，排序後依序送進去，就是 Poisson。根本不用管 Poisson 的機率公式。

【課本補充】Papoulis 式 (9-27)、(9-28)，pp. 382–383：
- (9-27)：給定長度 $T$ 的區間只有一個點，它落在子區間 $(t,t+\Delta)$ 的機率是 $\Delta/T$。
- (9-28)：給定 $X(T)=n$，$\mathbf{t}_1,\dots,\mathbf{t}_n$ 的聯合條件分布，比對 (4-102) 就是 $n$ 個獨立、在 $(0,T)$ 均勻分布的點排序後的分布。課本結論：Poisson 過程在無限區間 $(0,\infty)$ 上隨機撒點的方式，就像均勻隨機變數在有限區間撒點一樣。

---

## 8. 預告：平穩性

[▶ 41:43](https://youtu.be/8VOxDURP6TI?t=2503) 前面講了自相關、互相關，以及建立在有限維聯合分布上的獨立。現在回頭介紹重要的 general property：**平穩** (stationarity)。

- 平穩是隨機過程裡非常重要的假設，實作上有用。
- 例：設計手機時，你最好假設雜訊是**穩態**的。否則設計測試時對付的雜訊，和使用者實際用時的雜訊，機率上不一樣，就很怪。
- 當然也有非平穩的情況，例如上一集的疾病擴散（Pólya contagion process）。

（平穩的定義在下一集。）

---

## 9. 一頁速查表

### 電報訊號（參數 $\lambda$）

| | 半隨機 $X(t)$ | 全隨機 $Y(t)=aX(t)$ |
|---|---|---|
| $P\{=1\}$ | $e^{-\lambda t}\cosh\lambda t$ | $1/2$ |
| 平均 | $e^{-2\lambda t}$ | 0 |
| 自相關 | $e^{-2\lambda\lvert t_1-t_2\rvert}$ | $e^{-2\lambda\lvert t_1-t_2\rvert}$ |

- 關鍵一步：$R=\left[P(E_2)+P(O_2)\right]\left[P(E_\tau)-P(O_\tau)\right]=1\cdot e^{-\lambda\tau}(\cosh\lambda\tau-\sinh\lambda\tau)$。
- $\cosh x-\sinh x=e^{-x}$。

### Poisson 的運算

| 運算 | 結果 | 關鍵 |
|---|---|---|
| 和（獨立） | Poisson$((\lambda_1+\lambda_2)t)$ | 兩性質都要驗 |
| 差（獨立） | $e^{-(\lambda_1+\lambda_2)t}(\lambda_1/\lambda_2)^{n/2}I_{\lvert n\rvert}(2\sqrt{\lambda_1\lambda_2}t)$ | 不是 Poisson（會取負值） |
| 隨機篩選（機率 $p$） | Poisson$(\lambda pt)$、Poisson$(\lambda qt)$，互相獨立 | $\sum_n\binom nk p^kq^{n-k}e^{-\lambda t}\frac{(\lambda t)^n}{n!}$，令 $r=n-k$ 得指數級數 |
| 條件 | $X(t_1)\mid X(t_2)=n\sim B(n,t_1/t_2)$ | 拆 $(0,t_1)$、$(t_1,t_2)$ 獨立 |

### Poisson 點的直觀

- 給定 $(0,T)$ 有 $n$ 個點 = $n$ 個 i.i.d. $U(0,T)$ 排序（order statistic）。
- $n=1$：$P\{\mathbf{t}_1\le t\mid X(T)=1\}=t/T$。
- 模擬：產生均勻亂數 → 排序。

### 解題套路

1. 先用性質 2：拆成不重疊區間，用獨立把機率相乘。
2. 最後用性質 1：代 Poisson 公式。
3. 證明是 Poisson：兩個性質都要證。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 平穩性 | 下一集：SSS、WSS 定義 |
| 電報訊號 $R=e^{-2\lambda\lvert\tau\rvert}$ | 它是 WSS 的典型例子；之後算功率頻譜（§9-3） |
| 全隨機 vs 半隨機（暫態） | 漸近平穩 (asymptotically stationary) |
| Poisson 點 | shot noise（§10-2，課程跳過）；調變、取樣的例子 |
| Bessel 函數 | 數位通訊的錯誤率 |

---

## 附：本集一句話總結

> **電報訊號只是把 Poisson 計數換成 $\pm 1$，相關就從「不衰減」變成 $e^{-2\lambda|\tau|}$；Poisson 加起來、隨機篩選都還是 Poisson，相減不是；而 Poisson 最重要的直觀是——給定區間內有 $n$ 個點，它們就是 $n$ 個獨立均勻點排序後的結果。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-1 (6/7) 錄影逐字稿（whisper large-v3-turbo，43:23）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
