---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 19
lecture: Lec 10-4 Random Walks and Other Applications — Cyclostationary Processes
date: 待補
video: https://youtu.be/NtbS5Ll4DlY
notes: Papoulis & Pillai 4th ed. §10-4 Cyclostationary Processes（式 (10-171)–(10-186)，pp. 473–476；Theorem 10-5、10-6、10-7、Example 10-4）
---

# 第 19 集 · Lec 10-4：循環平穩過程、隨機平移變成平穩、時間平均自相關、數位脈衝串（PAM）的頻譜 [▶ 影片](https://youtu.be/NtbS5Ll4DlY)

← 上一集：[18](18-woodward-theorem-fm-spectrum-gaussian-process-definitions.md) ｜ [總目錄](README.md) ｜ 下一集：[20](20-bandlimited-processes-sampling-theorem-past-samples-random-sampling.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 19 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（33:14，whisper large-v3-turbo）＋ Papoulis §10-4（pp. 473–476）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「cyclostationary」→「Cyclostationary／cyclo-station／cycle station」，「wide-sense stationary」→「Y-Sense／Y3／Wisen／Y-SAN／wighting stationary」，「穩態」→「穩泰」，「probability space」→「provis space」，「time average」→「time average」，「autocorrelation」→「auto-corrision／autogranium／autocornifer／autoclin function」，「convolution」→「comvolution」，「replication property」→「replication property」，「discrete」→「discreet」，「傅立葉轉換」→「伏列轉換」，「impulse response」→「Import Response」，「dominated convergence theorem」→「dominated conversion theorem」，「實變分析」→「十遍分析」，「sinc」→「sync」，「Theorem 9-2」→「定理92」，「fading」→「fading」。以下一律用正確的字。

> **接上一集**：§10-3 講調變。§10-4 介紹一個新的統計特性：**循環平穩** (cyclostationary)。老師說：數位通訊一定要學這個——數位通訊的訊號基本上都是循環平穩的，不太可能是 WSS。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 定義](#1-定義)
- [2. 隨機平移一個週期：循環平穩 → 平穩](#2-隨機平移一個週期循環平穩--平穩)
  - [2.1 SSCS → SSS（用機率空間證）](#21-sscs--sss用機率空間證)
  - [2.2 WSCS → WSS](#22-wscs--wss)
- [3. 時間平均自相關](#3-時間平均自相關)
- [4. 例：數位脈衝串](#4-例數位脈衝串)
  - [4.1 驗證循環平穩](#41-驗證循環平穩)
  - [4.2 時間平均自相關（delta 相乘要小心）](#42-時間平均自相關delta-相乘要小心)
  - [4.3 時間平均功率頻譜](#43-時間平均功率頻譜)
- [5. 時間平均版的 Theorem 9-2：四個條件](#5-時間平均版的-theorem-9-2四個條件)
- [6. 例：脈衝串經過方波濾波器（PAM）](#6-例脈衝串經過方波濾波器pam)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 定義 | [▶ 00:00](https://youtu.be/NtbS5Ll4DlY?t=0) | 式 (10-171)、(10-172)，p. 473 |
| 隨機平移 → 平穩 | [▶ 01:03](https://youtu.be/NtbS5Ll4DlY?t=63) | Theorem 10-5、10-6，pp. 473–474 |
| 時間平均自相關 | [▶ 05:35](https://youtu.be/NtbS5Ll4DlY?t=335) | 式 (10-177) |
| 脈衝串例子 | [▶ 11:16](https://youtu.be/NtbS5Ll4DlY?t=676) | 式 (10-181)–(10-185)，pp. 474–475 |
| 時間平均版 Theorem 9-2 | [▶ 19:00](https://youtu.be/NtbS5Ll4DlY?t=1140) | 無（老師的推廣） |
| PAM 例子 | [▶ 30:13](https://youtu.be/NtbS5Ll4DlY?t=1813) | Theorem 10-7、Example 10-4，pp. 474–476 |

---

## 1. 定義

[▶ 00:00](https://youtu.be/NtbS5Ll4DlY?t=0) cyclo = 週期性的。

> **嚴格循環平穩** (strict-sense cyclostationary，SSCS)，週期 $T$：統計性質在原點平移 $T$ 的**整數倍**時不變：
> $$F(x_1,\dots,x_n;t_1+mT,\dots,t_n+mT)=F(x_1,\dots,x_n;t_1,\dots,t_n),\quad\text{對每個整數 }m.$$
>
> **廣義循環平穩** (wide-sense cyclostationary，WSCS)：平均和自相關是週期 $T$ 的：
> $$\eta(t+mT)=\eta(t),\qquad R(t_1+mT,t_2+mT)=R(t_1,t_2).$$

- 這裡是 $t_1,t_2$，不是 $t+\tau,t$：它不只跟時間差有關。
- SSCS ⇒ WSCS。

【課本補充】式 (10-171)、(10-172)，p. 473。

---

## 2. 隨機平移一個週期：循環平穩 → 平穩

[▶ 01:03](https://youtu.be/NtbS5Ll4DlY?t=63) 第一個重要定理：**怎麼把循環平穩轉成平穩**？看一整個週期，把一整個週期做平均。

> **定理**：$X(t)$ 循環平穩，週期 $T$。$\theta$ 在 $(0,T)$ **均勻**、和 $X$ 獨立。令**平移過程** (shifted process)
> $$\bar{X}(t)=X(t-\theta).$$
> 則
> - $X$ 是 SSCS ⇒ $\bar X$ 是 **SSS**（Theorem 10-5）；
> - $X$ 是 WSCS ⇒ $\bar X$ 是 **WSS**（Theorem 10-6）。

分布的關係：把一個週期積分、做平均——就是**時間平均** (time average)：
$$\bar F(x_1,\dots,x_n;t_1,\dots,t_n)=\frac1T\int_0^TF(x_1,\dots,x_n;t_1-\alpha,\dots,t_n-\alpha)\,d\alpha\qquad\text{(10-174)}.$$

### 2.1 SSCS → SSS（用機率空間證）

[▶ 02:33](https://youtu.be/NtbS5Ll4DlY?t=153) 為什麼回到機率空間證？因為要證的是比較強的**嚴格平穩**，沒辦法只證一、二階動差。

要證：$\bar X$ 平移 $c$ 之後，機率和 $c$ 無關。令事件 $A=\{\bar X(t_1+c)\le x_1,\dots,\bar X(t_n+c)\le x_n\}$。

**Step 1：** 對 $\theta$ 取條件（全機率），$\theta$ 均勻，密度 $\frac1T$：
$$P(A)=\frac1T\int_0^TP(A\mid\theta)\,d\theta.$$

**Step 2：** $\theta$ 和 $X$ 獨立，條件可以拿掉，換成 $X$ 的分布：
$$P(A\mid\theta)=F(x_1,\dots,x_n;t_1+c-\theta,\dots,t_n+c-\theta).$$

**Step 3：** 令 $\alpha=\theta-c$，積分範圍變成 $(-c,T-c)$，**還是一個週期**。

**Step 4：** $X$ 是循環平穩，$F$ 對時間是週期 $T$ 的，**積任何一個週期都一樣**，換回 $(0,T)$：
$$P(A)=\frac1T\int_0^TF(x_1,\dots;t_1-\alpha,\dots)\,d\alpha.$$
和 $c$ 無關，所以 $\bar X$ 是 SSS。 ∎

### 2.2 WSCS → WSS

[▶ 04:04](https://youtu.be/NtbS5Ll4DlY?t=244) 證法比較簡單、形式一樣，只要證平均和自相關。用疊代期望值：先固定 $\theta$ 對 $X$ 取期望值（$\theta$ 和 $X$ 獨立，條件拿掉）：
$$E[\bar X(t)]=\frac1T\int_0^T\eta(t-\theta)\,d\theta=\frac1T\int_0^T\eta(t)\,dt=\bar\eta\qquad\text{(10-176)},$$
$$E[\bar X(t+\tau)\bar X^*(t)]=\frac1T\int_0^TR(t+\tau-\theta,t-\theta)\,d\theta=\frac1T\int_0^TR(t+\tau,t)\,dt=\bar R(\tau)\qquad\text{(10-177)}.$$
（$\eta$ 週期、$R(t+\tau,t)$ 對 $t$ 週期，積一個週期都一樣。）只跟 $\tau$ 有關。 ∎

看起來和基本定理一致：$\bar X$ 是 $X$ 的平均，平均值也是平均。

**老師留的問題**（沒給答案，請大家回去想）[▶ 04:35](https://youtu.be/NtbS5Ll4DlY?t=275)：輸入 $X$、輸出 $Y(t)=X(t-\theta)$，$\theta$ 均勻且和 $X$ 獨立——這是不是一個卷積關係？如果是，就可以直接用 Theorem 9-2 證，根本不用硬算。

---

## 3. 時間平均自相關

[▶ 05:35](https://youtu.be/NtbS5Ll4DlY?t=335) $\bar R(\tau)$ 叫 $X$ 的**時間平均自相關** (time-average autocorrelation)。在數位通訊非常重要。

**為什麼需要**【口頭】：

- 一般隨機過程很可能不是平穩的，甚至不是循環平穩。$R(t_1,t_2)$ 不能整合成一個 $\tau$ 的函數：10 點和 11 點的關係（例如是 3），跟下午 1 點和 2 點的關係（例如是 6）不一樣。
- 設計系統時真正關心的還是**時間差**：現在打一個訊號，它的能量影響會不會延續？例如第 10 個 nanosecond 打的訊號，對第 11 個 nanosecond 有什麼殘餘影響；第 1 到第 2 個 nanosecond 之間又如何。有時影響大、有時小。
- 做法：間隔都是 $\tau$（例如 1 ns），在不同時間（1 點、2 點、3 點……）把大大小小的影響**加起來做平均**，就是延遲 $\tau$ 的平均影響。設計系統就以這個為依據。
- 老師的比喻：打一個飛彈嚇嚇別人，這個「嚇」延續多久？有的國家打一下人家根本不理你，有的一打影響力就很大。我們關心的是每做一件事情，影響力延續的週期。

> **一般的時間平均自相關**：
> $$\bar R(\tau)=\lim_{\Omega\to\infty}\frac{1}{2\Omega}\int_{-\Omega}^{\Omega}R(t+\tau,t)\,dt\quad\text{（極限要存在）}.$$

- **循環平穩**：積一個週期（或 $k$ 個週期）平均就夠了，得到 (10-177)。
- **WSS**：$R(t+\tau,t)=R(\tau)$ 是常數，常數的平均還是自己（3 加 3 加 3 除以 3 還是 3）。所以時間平均自相關是 WSS 的延伸。
- 記號：$X(t-\theta)$ 代表時間平均；頭上一橫 $\bar{\ }$ 代表對時間做平均。早上傳送、下午傳送、晚上傳送，絕對時間不管了，平均掉了；設計的系統要一整天都能用，平均來講 OK。

---

## 4. 例：數位脈衝串

[▶ 11:16](https://youtu.be/NtbS5Ll4DlY?t=676)

$$Z(t)=\sum_{n=-\infty}^{\infty}C_n\,\delta(t-nT),$$
$C_n$ 是**離散時間嚴格平穩**序列，自相關 $R_C[m]=E\{C_{n+m}C_n\}$。

數位通訊的樣子：每隔一段時間 $T$ 送一個（$C_1,C_2,C_3,\dots$），定期一直送。所以數位通訊的訊號大部分都是循環平穩的。

### 4.1 驗證循環平穩

很基本的題目，證兩個性質：

- **平均**：$E[Z(t)]=E[C]\sum_n\delta(t-nT)$。$C$ 嚴格平穩，平均是常數；脈衝每隔一個週期一根，高度都一樣，所以平均是週期 $T$ 的。
- **自相關**：
$$R_Z(t_1,t_2)=\sum_n\sum_rR_C[n-r]\,\delta(t_1-nT)\,\delta(t_2-rT).$$
  平移 $T$ 的整數倍不變，所以是週期的。

### 4.2 時間平均自相關（delta 相乘要小心）

[▶ 13:21](https://youtu.be/NtbS5Ll4DlY?t=801) 真正的目標是算時間平均自相關，積一個週期做平均，一定要會算。

改寫：令 $m=n-r$，
$$R_Z(t+\tau,t)=\sum_mR_C[m]\sum_r\delta\left(t+\tau-(m+r)T\right)\delta(t-rT)\qquad\text{(10-183)}.$$

**注意**【口頭】：兩個 delta 相乘是 **undefined**（delta 是人工定義的特別函數，裡面有無限大；「無限大乘無限大等於什麼」很怪）。delta 只有**對積分**才有意義（複製性質把函數帶出來）。

**Step 1：** 求和與積分互換，對一個週期積分：
$$\bar R_Z(\tau)=\frac1T\sum_mR_C[m]\sum_r\int_0^T\delta\left(t+\tau-(m+r)T\right)\delta(t-rT)\,dt.$$

**Step 2：** 令 $s=t-rT$。每個 $r$ 積一個長度 $T$ 的區間，$(-T,0)$、$(0,T)$、$(T,2T)$……所有 $r$ 合起來，對 $r$ 的求和和積分合成一個 $(-\infty,\infty)$ 的積分：
$$\sum_r\int_0^T\cdots\,dt=\int_{-\infty}^{\infty}\delta(s+\tau-mT)\,\delta(s)\,ds.$$

**Step 3：用複製性質要檢查連續性。** 把 $g(s)=\delta(s+\tau-mT)$ 當作被帶出來的函數，它只在 $s=mT-\tau$ 有脈衝，其他地方都是 0。複製性質要在 $s=0$ 帶出 $g(0)$，需要 $g$ 在 $s=0$ **連續**：
- $\tau\ne kT$（不是 $T$ 的整數倍）：$mT-\tau\ne0$，$g$ 在 0 附近都是 0，連續，可以用，結果是 0。
- $\tau=kT$ 但 $m\ne k$：$mT-\tau=(m-k)T\ne0$，也連續，可以用，結果是 0。
- **只有 $\tau=kT$ 且 $m=k$ 時**，$g$ 的脈衝剛好在 0，**不連續，undefined**。只有這一點會出問題。

承認這一點用 delta 表示，得
$$\bar R_Z(\tau)=\frac1T\sum_mR_C[m]\,\delta(\tau-mT)\qquad\text{(10-184)}.$$

**老師對課本的意見** [▶ 16:27](https://youtu.be/NtbS5Ll4DlY?t=987)：課本直接用了恆等式
$$\int_0^T\delta[t+\tau-(m+r)T]\,\delta(t-rT)\,dt=\delta(\tau-mT),$$
老師說這是**不對**的：兩個 delta 相乘只積 $0$ 到 $T$，不能把 delta 拿出來，要積 $-\infty$ 到 $\infty$ 才對，否則會導致錯誤的結論。也有人這樣處理：$\delta(t-a)\delta(t-b)$ 要 $t=a$ 且 $t=b$，乾脆寫成 $\delta(a-b)\delta(t-b)$，前者是常數拉出來，後者積分是 1。delta 本來就是人工造的函數，如果你覺得這樣對、對你有用，當然也可以用。

### 4.3 時間平均功率頻譜

[▶ 17:27](https://youtu.be/NtbS5Ll4DlY?t=1047) 數位通訊真正關心的是**時間平均功率頻譜**：時間平均自相關的傅立葉轉換。只有一個參數 $\tau$（延遲），絕對時間平均掉了，對不同頻率也把能量做平均。

代入，delta 和積分對消（求和積分互換後，$e^{-j\omega\tau}$ 是連續函數，代 $\tau=mT$）：
$$\bar S_Z(\omega)=\frac1T\sum_mR_C[m]e^{-jmT\omega}=\frac1T\,S_C\left(e^{j\omega T}\right)\qquad\text{(10-185)}.$$
這是離散的傅立葉轉換，頻譜是**週期性**的（週期 $\frac{2\pi}{T}$）——可以預期：時域是離散的，頻譜一定週期。

---

## 5. 時間平均版的 Theorem 9-2：四個條件

[▶ 19:00](https://youtu.be/NtbS5Ll4DlY?t=1140) 回到基本定理和 Theorem 9-2：若系統線性、可以用卷積定義，那麼輸入和輸出的**時間平均**功率頻譜有
$$\bar S_Y(\omega)=E\left|H(\omega)\right|^2\bar S_X(\omega).$$

- 這對**任何**過程都對：WSS、循環平穩、非循環平穩都可以。
- 但這裡用的是**平均**，原本的 $R_{XX}(t_1,t_2)$ 在不同時間延續的能量影響不一樣。什麼樣的系統才能用？老師說這是他一直強調的：定理好用、直觀，但要知道**什麼時候可以用**。

**四個條件**（數學不用背，記物理意義；精確式子在投影片上，逐字稿沒有完整唸出）：

1. **系統能量有限**：脈衝響應絕對值的總積分在均方意義下有限。系統可以是隨機的（例如 fading channel，有時大有時小），但 fading 的能量要有限，不能衝到無限大。實際系統也都是有限的。
2. **輸入能量有限**：輸入的平均函數和自相關（二維，$t_1,t_2$）積分後要被一個常數界住。不可以送一個能量爆到無限大的輸入，否則不保證輸出和輸入符合定理的關係。
3. 和 4. **時間平均的視窗可以任意平移**：$\frac{1}{2\Omega}\int_{-\Omega-\tau}^{\Omega-\tau}\eta(t)\,dt$ 和 $\frac{1}{2\Omega}\int_{-\Omega}^{\Omega}\eta(t)\,dt$ 在極限上一樣；自相關也一樣。也就是：把平均的視窗往右移、往左移，一直往外擴張得到的極限平均都一樣，不隨時間改變。

**直觀**【口頭】：觀察一個現象（例如股市變化）做長時間平均，從 1 月到 3 月的平均和從 3 月到 6 月的平均，視窗一直擴張後答案要一樣，才有這個穩定的時間平均結果。總結：**輸入能量要穩定、不爆到無限大；系統要穩定、沒有無限大；輸入在時間平均視窗的選取上沒有限制（從哪一天開始記錄都 OK）。** 缺一不可，都可以舉反例（舉起來比較殘忍）。

**證明的關鍵**（和原本卷積的證明一樣，多了極限）[▶ 25:40](https://youtu.be/NtbS5Ll4DlY?t=1540)：

1. 輸出的時間平均 = 取一個視窗的平均；輸出 = 輸入卷積系統，取期望值；期望值和積分對調。到這裡都沒問題。
2. **最大的不同：積分和極限要互換**。極限和極限互換、積分和積分互換（Lebesgue 積分）都沒問題，但**積分和極限互換需要條件**：用**控制收斂定理**，需要第 2 個條件——找一個函數 $g$，被積的東西都比它小，而且 $g$ 本身積分有限。這個 $g$ 就在裡面。
3. 互換後就是原來時間平均的定義；第 3、4 個條件保證視窗哪裡取都可以。

老師說【口頭】：做工程應用時記得這件事——系統都要有限；有任何瞬間脈衝的系統或輸入，就要注意系統會出問題。實變分析裡有一整個月在講積分極限互換這件事，很重要。

**big data 的提醒**【口頭】：收集一堆資料做分析、取平均時，要驗證整個系統的資料穩不穩：對每個視窗取平均，看是不是很接近（視窗要夠大）。不相等的話就不能用這個定理，甚至不能下任何結論。例如「這件事和那件事相關」不一定對——也許春天相關、秋天無關；四季有變化，或者是每十年一個 cycle 的自然現象。

---

## 6. 例：脈衝串經過方波濾波器（PAM）

[▶ 30:13](https://youtu.be/NtbS5Ll4DlY?t=1813) 把剛才的脈衝串 $Z(t)=\sum C_n\delta(t-nT)$ 送進一個濾波器，脈衝響應是方波：
$$h(t)=\begin{cases}1,&0\le t<T\\0,&\text{其他}\end{cases}$$
輸出 $X=Z*h=\sum_nC_nh(t-nT)$。

- 不知道示意系統穩不穩，但濾波器有脈衝響應（卷積定義），最直觀就想用 Theorem 9-2、9-4 描述輸入輸出的時間平均關係。
- **驗證四個條件**：
  - 系統：$\int|h|=T$ 有限；$h$ 是確定的，取期望值有取跟沒取一樣。✓
  - 輸入：已驗證是循環平穩，取一個週期的視窗沒問題；能量穩定。✓
- 所以可以用：
  - 自相關：輸入的時間平均經過兩次濾波（第一次共軛）：$\bar R_X(\tau)=\bar R_Z(\tau)*h^*(-\tau)*h(\tau)$。$h$ 高度是 1，剩下就是微積分。
  - 功率頻譜更快：輸入的時間平均頻譜乘 $|H|^2$，而方波的 $H$ 是 sinc 函數：
$$\bar S_X(\omega)=\frac1T\,S_C\left(e^{j\omega T}\right)\left|H(\omega)\right|^2,\qquad|H(\omega)|^2=\frac{4\sin^2(\omega T/2)}{\omega^2}.$$

這一張講的就是：循環平穩推廣到時間平均自相關。

【課本補充】Papoulis **PAM（脈衝振幅調變，pulse-amplitude modulation）**（pp. 474–476）：
- (10-178)：$X(t)=\sum_nC_nh(t-nT)$，$h$ 是給定函數、$C_n$ 是平穩序列。
- Theorem 10-7：平移過程的功率頻譜 $\bar S_X(\omega)=\frac1TS_C(e^{j\omega})|H(\omega)|^2$（式 (10-180)；課本的 $S_C(e^{j\omega})$ 以 $\omega T$ 為頻率變數）。課本的證法：把脈衝串寫成階梯過程 $W(t)=\sum C_nU(t-nT)$ 的微分 $Z=W'$，用 (9-103) 得 (10-183)。
- Corollary（10-186）：$C_n$ 是白雜訊 $S_C=q$ 時，$\bar S_X=\frac qT|H(\omega)|^2$，$\bar R_X=\frac qTh(\tau)*h(-\tau)$。
- Example 10-4（**二元傳輸** binary transmission）：$h$ 是方波、$C_n=\pm1$ 等機率白雜訊，$\bar S_X(\omega)=\frac{4\sin^2(\omega T/2)}{T\omega^2}$，$\bar R_X(\tau)$ 是三角形。$X$ 是 SSCS，平移過程 $X(t-\theta)$ 是平穩的。

---

## 7. 一頁速查表

### 定義

- SSCS：$F(\cdot;t_i+mT)=F(\cdot;t_i)$；WSCS：$\eta(t+mT)=\eta(t)$，$R(t_1+mT,t_2+mT)=R(t_1,t_2)$。

### 隨機平移 $\bar X(t)=X(t-\theta)$，$\theta\sim U(0,T)$ 獨立

| $X$ | $\bar X$ | 結果 |
|---|---|---|
| SSCS | SSS | $\bar F=\frac1T\int_0^TF(\cdot;t_i-\alpha)d\alpha$ |
| WSCS | WSS | $\bar\eta=\frac1T\int_0^T\eta$，$\bar R(\tau)=\frac1T\int_0^TR(t+\tau,t)dt$ |

- 關鍵：全機率對 $\theta$ 積分，換變數後仍是一個週期，週期函數積任何一個週期都一樣。

### 時間平均

- $\bar R(\tau)=\lim\frac1{2\Omega}\int_{-\Omega}^{\Omega}R(t+\tau,t)dt$；循環平穩積一週期；WSS 時就是 $R(\tau)$。
- 時間平均版 Theorem 9-2：$\bar S_Y=E|H|^2\bar S_X$，條件：系統能量有限、輸入能量有限、時間平均視窗可任意平移（極限存在且相同）。證明關鍵：控制收斂定理。

### 脈衝串與 PAM

- $Z=\sum C_n\delta(t-nT)$：$\bar R_Z(\tau)=\frac1T\sum_mR_C[m]\delta(\tau-mT)$，$\bar S_Z=\frac1TS_C(e^{j\omega T})$。
- 算的時候：兩個 delta 相乘只能放在 $(-\infty,\infty)$ 的積分裡用複製性質；$\tau=mT$ 那一點不連續、undefined。
- PAM：$\bar S_X=\frac1TS_C(e^{j\omega T})|H(\omega)|^2$；方波 $|H|^2=\frac{4\sin^2(\omega T/2)}{\omega^2}$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 離散 → 頻譜週期 | 下一集：§10-5 帶限過程與取樣定理 |
| 時間平均 | §12-1 遍歷性：時間平均 = 統計平均？（第 30–33 集） |
| 控制收斂定理 | §12 遍歷性的證明 |
| PAM 頻譜 | 數位通訊的頻譜設計 |

---

## 附：本集一句話總結

> **數位通訊訊號是循環平穩的（統計每隔週期 $T$ 重複）；把原點隨機平移一個均勻的 $\theta\in(0,T)$，就變成平穩，自相關變成一個週期內的時間平均 $\bar R(\tau)$；對一般非平穩過程也可以定義時間平均自相關與頻譜，只要系統和輸入能量有限、時間平均的視窗可任意平移，線性系統仍滿足 $\bar S_Y=|H|^2\bar S_X$，例如 PAM 的頻譜就是 $\frac1TS_C(e^{j\omega T})|H(\omega)|^2$。**

---

## ⚠️ 待確認清單

1. [▶ 20:31](https://youtu.be/NtbS5Ll4DlY?t=1231) 時間平均版 Theorem 9-2 的四個條件精確式子，投影片有、逐字稿只唸了意義；筆記依口述整理。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 10-4 錄影逐字稿（whisper large-v3-turbo，33:14）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
