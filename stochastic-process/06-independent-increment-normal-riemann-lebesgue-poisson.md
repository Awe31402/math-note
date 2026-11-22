---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 6
lecture: Lec 9-1 General Concepts — Definitions (5/7)
date: 待補
video: https://youtu.be/pFK4f8YmmiU
notes: Papoulis & Pillai 4th ed. §9-1（Example 9-3，p. 377；Example 9-5 Poisson process，式 (9-13)–(9-17)，pp. 378–379；independent increments、normal processes，式 (9-46)，pp. 385–386；point and renewal processes，p. 387）
---

# 第 6 集 · Lec 9-1 (5/7)：獨立增量、常態過程、Riemann vs Lebesgue 積分、點過程、Poisson 過程的自相關 [▶ 影片](https://youtu.be/pFK4f8YmmiU)

← 上一集：[05](05-covariance-orthogonal-uncorrelated-white-noise.md) ｜ [總目錄](README.md) ｜ 下一集：[07](07-telegraph-signal-poisson-sum-difference-selection-uniform.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 6 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（46:42，whisper large-v3-turbo）＋ Papoulis §9-1（pp. 377–379、385–387）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Poisson」→「PoZone／Prozone／Portone／頗重／provision／ポイゾン」，「Brownian motion」→「Brownia motion」，「Lebesgue」→「the best／Lebeck」，「Riemann」→「里曼／禮曼／理慢／理賣／Rhyment」，「supremum／infimum」→「supremant／infinite」，「話務」→「化物／畫物」，「封包」→「風包」，「無理數」→「五理數」，「閉區間」→「B區間／壁區間」，「Borel set」→「boreal set」，「實數」→「時數」，「拆成」→「猜成」，「乘進去」→「沉進去」，「die away」→「大要位／呆耀味」，「霧霾」→「霧蠻」，「家族的」→「家種的」，「實變分析」→「十遍分析」，「數學系」→「數學技」，「傅立葉轉換」→「負利的轉換」，「Noah／Nile effect」→「Noir effect」。以下一律用正確的字。

> **接上一集**：上一集講了獨立、正交、不相關、a-dependent、白過程。這一集繼續加兩個限制（獨立增量、常態），插入一段積分的觀念（為什麼課本說「Riemann 積分」），最後介紹點過程和 Poisson 過程，算它的自相關並解讀物理意義。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 獨立增量、不相關增量](#1-獨立增量不相關增量)
- [2. 常態（高斯）過程](#2-常態高斯過程)
  - [2.1 定義](#21-定義)
  - [2.2 存在定理](#22-存在定理)
- [3. 為什麼課本強調「Riemann 積分」](#3-為什麼課本強調riemann-積分)
  - [3.1 Riemann 積分：用長方形逼近](#31-riemann-積分用長方形逼近)
  - [3.2 Riemann 積分失效的例子](#32-riemann-積分失效的例子)
  - [3.3 Lebesgue 積分：simple function](#33-lebesgue-積分simple-function)
  - [3.4 真正的目的：期望值和積分可以交換](#34-真正的目的期望值和積分可以交換)
- [4. 點過程、更新過程、計數過程](#4-點過程更新過程計數過程)
- [5. Poisson 過程](#5-poisson-過程)
  - [5.1 定義：兩個性質](#51-定義兩個性質)
  - [5.2 平均](#52-平均)
  - [5.3 自相關：先用性質 2 拆開](#53-自相關先用性質-2-拆開)
  - [5.4 解讀：為什麼相關不會衰減](#54-解讀為什麼相關不會衰減)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 獨立增量 | [▶ 00:00](https://youtu.be/pFK4f8YmmiU?t=0) | pp. 385–386 |
| 常態過程、存在定理 | [▶ 02:33](https://youtu.be/pFK4f8YmmiU?t=153) | 式 (9-46)，p. 386 |
| Riemann vs Lebesgue | [▶ 07:41](https://youtu.be/pFK4f8YmmiU?t=461) | Example 9-3，p. 377 |
| 點過程、更新過程 | [▶ 24:04](https://youtu.be/pFK4f8YmmiU?t=1444) | p. 387 |
| Poisson 過程 | [▶ 27:11](https://youtu.be/pFK4f8YmmiU?t=1631) | Example 9-5，式 (9-13)–(9-17)，pp. 378–379 |

---

## 1. 獨立增量、不相關增量

[▶ 00:00](https://youtu.be/pFK4f8YmmiU?t=0) 網路應用、量子科學都會用到。

**例：布朗運動** (Brownian motion)。最早是植物學家布朗看到花粉粒被分子撞來撞去；愛因斯坦等人做了理論。這一段時間的位移和另一段時間的位移，因為都是亂撞，彼此獨立。【口頭】

> **獨立增量** (independent increments)：對任何 $t_1<t_2<t_3<t_4$，增量 $X(t_2)-X(t_1)$ 和 $X(t_4)-X(t_3)$ **獨立**。

- $X(t_2)-X(t_1)$ 就是 $t_1$ 到 $t_2$ 的位移。例：10:00–10:10 的位移和 11:00–11:10 的位移完全無關。
- 之後會用它定義 **Poisson 過程**。Poisson 在通訊上很有用：描述話務量，早期交換機都針對 Poisson 設計（單位時間來幾通電話）。

> **不相關增量** (uncorrelated increments)：同樣的句型，把「獨立」換成「不相關」。

為什麼要這個？工程上有時希望假設**不要那麼強**，應用就比較廣。既然只看一階、二階（能量的影響），不需要那麼強的獨立增量。

【課本補充】Papoulis pp. 385–386：Poisson 過程是獨立增量過程；白雜訊的積分（上一集 Example 9-9）是不相關增量過程。

老師順便說【口頭】：「process」常省略 random 或 stochastic，直接叫 process。對我們來說它本來就不隨機，只是一個映射。

---

## 2. 常態（高斯）過程

### 2.1 定義

[▶ 02:33](https://youtu.be/pFK4f8YmmiU?t=153)

> **常態過程** (normal process)：對任何 $n$、任何 $t_1,\dots,t_n$，隨機變數 $X(t_1),\dots,X(t_n)$ 是**聯合常態** (jointly normal) 的。

- 關鍵字又是 **finite**：任何定義都只講有限維。無限維很難定義，除非給機率空間。
- 聯合常態：例如三維，就可以寫出它的高斯 PDF。$n$ 維的形式是（逐字稿對公式唸得不清楚，依標準形式重建）
$$f(\mathbf{x})=\frac{1}{(2\pi)^{n/2}\left|\Sigma\right|^{1/2}}\exp\left(-\frac12(\mathbf{x}-\boldsymbol{\mu})^{T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu})\right),$$
  $\boldsymbol{\mu}=(\eta(t_1),\dots,\eta(t_n))$，$\Sigma_{ik}=C(t_i,t_k)$，$|\Sigma|$ 是行列式 (determinant)。

**為什麼叫 normal？**【口頭】老師說網路上有文章專門討論高斯為什麼變成 normal，是漸進的過程：慢慢有文獻說它是「常見的」。熱運動、大數法則（老師口語；應指中央極限定理那類現象）形成的分布大多是常態，非常常見，所以叫 normal——平常、很常見、像一個基準。

**每本書的定義不一樣**：老師說上學期教的 Haykin 那本書，高斯過程的定義就不是這樣（⚠️ 逐字稿聽成「Herkin」）。但 normal 的各種定義通常是**等價的**，只是敘述不同。Papoulis 這樣定義，是為了方便證明下面的存在定理。

【課本補充】Papoulis p. 386：常態過程的統計完全由平均 $\eta(t)$ 和自協方差 $C(t_1,t_2)$ 決定。一階密度是 $N\left(\eta(t);\sqrt{C(t,t)}\right)$；二階密度是聯合常態，相關係數 $r(t_1,t_2)$。

### 2.2 存在定理

[▶ 05:37](https://youtu.be/pFK4f8YmmiU?t=337)

> **存在定理** (existence theorem)：給任意函數 $\eta(t)$ 和任意**非負定**函數 $C(t_1,t_2)$，**一定存在**一個常態過程，它的平均是 $\eta(t)$、自協方差是 $C(t_1,t_2)$。

- 這就是「自協方差 ⇔ 非負定」的反方向（if and only if 的另一半），用高斯就可以證。
- **證明的技巧**：特性函數 (characteristic function) 和分布一對一對應，因為兩者是傅立葉轉換的關係。所以只要寫出 $n$ 階特性函數：
$$\Phi(\omega_1,\dots,\omega_n)=\exp\left\{j\sum_i\eta(t_i)\omega_i-\frac12\sum_{i,k}C(t_i,t_k)\,\omega_i\omega_k\right\}\qquad\text{(9-46)}$$
- 看到 $\sum_i$、$\sum_{i,k}$ 就知道是有限維。證明完全配合定義。

【課本補充】Papoulis p. 386 的證明一句話：把給定的 $\eta$、$C$ 代進 (9-46)，它的反轉換是密度，因為 $C$ 是 p.d.（非負定保證 $\Sigma$ 是合法的協方差矩陣）。

---

## 3. 為什麼課本強調「Riemann 積分」

[▶ 07:41](https://youtu.be/pFK4f8YmmiU?t=461) Papoulis 在 Example 9-3 和之後的例子都特別寫「Riemann 積分」。老師說：這本書範例多，但有些地方沒寫清楚就直接用了；研究所要把觀念弄清楚。

【課本補充】Example 9-3（p. 377）：$\mathbf{s}=\int_a^b\mathbf{x}(t)\,dt$。把它解釋成 Riemann 積分，由期望值的線性得
$$\eta_s=E\{\mathbf{s}\}=\int_a^b\eta(t)\,dt\quad\text{(9-10)},\qquad E\{\mathbf{s}^2\}=\int_a^b\!\!\int_a^b R(t_1,t_2)\,dt_1dt_2\quad\text{(9-11)}.$$

### 3.1 Riemann 積分：用長方形逼近

[▶ 08:42](https://youtu.be/pFK4f8YmmiU?t=522)

老師的故事【口頭】：古埃及人很會算面積，因為尼羅河每年氾濫，把農田蓋滿爛泥巴（不用施肥，很好種），但分不清哪塊地是誰的，要重新算面積：你兩公頃、我 3.2 公頃。

**觀念**：長方形面積好算（底 × 高）。

1. 把 $[a,b]$ 切成 $x_0<x_1<x_2<\dots<x_n$，每段一個長方形。這種一階一階的函數叫 **step function**（階梯函數），底一定是**連續的區間**。
2. **白色**的長方形都在函數**底下**：面積和 $\le$ 真正面積。所有切法取**上確界** (supremum)。
3. **紅色**的長方形都**蓋住**函數：面積和 $\ge$ 真正面積。所有切法取**下確界** (infimum)。
4. 兩者**相等**，就是 Riemann 積分：
$$\sup_{\text{下方階梯}}\sum_k m_k(x_k-x_{k-1})=\inf_{\text{上方階梯}}\sum_k M_k(x_k-x_{k-1})=\int_a^b f(x)\,dx.$$

老師的插曲【口頭】：後來亞斯文高壩蓋好，尼羅河不氾濫，埃及人不用再算面積（數學就變差了），也沒有肥沃的土壤，要施肥了。另外網路上有「**Noah effect**（諾亞效應）／Nile effect（尼羅河效應）」：要嘛都不來，要嘛一起來——封包要嘛都不送、要送全部一起送，高速公路要嘛沒人、要嘛全部塞住；就像要嘛不下雨，要下就連下七天七夜。統計上會討論這種現象。

### 3.2 Riemann 積分失效的例子

[▶ 14:50](https://youtu.be/pFK4f8YmmiU?t=890)

$$f(x)=\begin{cases}1,&x\ \text{是有理數}\\0,&x\ \text{是無理數}\end{cases}\qquad x\in[a,b]$$

- Riemann 積分的長方形永遠是**有限個**（切 100 份、200 份……），無限是用極限做的。
- 任何小區間裡都**同時**有有理數和無理數（處處稠密）。
- 下方的長方形：區間裡有無理數，高度只能是 0，總和 0。
- 上方的長方形：區間裡有有理數，高度至少是 1，總和 $b-a$。
- 不管切多細，**一個是 0、一個是 $b-a$，永遠合不起來**。Riemann 積分失效。

### 3.3 Lebesgue 積分：simple function

[▶ 16:23](https://youtu.be/pFK4f8YmmiU?t=983) 換一個**基本單位**（老師比喻：量子力學找基本量 quantum，所有東西都是它的整數倍）。

> **simple function**（簡單函數）：把定義域切成**有限個**集合 $U_1,\dots,U_k$，每個集合上函數是**一個常數** $c_i$。它的積分是
> $$\sum_{i=1}^{k}c_i\,\lambda(U_i),$$
> $\lambda(U_i)$ 是 $U_i$ 的 Lebesgue 測度（「寬度總和」）。

- 和 step function 的差別：**底不需要連續**，只要是 Borel 集。例：$\{2,3.1,5.6\}$ 這三個點都映到 1，就可以算成同一塊。
- 底是 Borel 集，所以能用 Lebesgue 測度量「長度」（區間長 = 右端 − 左端）。

**解決剛才的函數** [▶ 19:26](https://youtu.be/pFK4f8YmmiU?t=1166)：

1. 把實數切成兩塊：有理數集合 $\mathbb{Q}$（映到 1）和無理數集合（映到 0）。
2. 一個有理數 $q$ 本身就是一個閉區間 $[q,q]$，長度 $q-q=0$。
3. 有理數是可數個這種點的聯集，由可數可加性，$\lambda(\mathbb{Q}\cap[a,b])=0$。
4. 積分 $=1\cdot 0+0\cdot(b-a)=0$。上面壓下來是 0，下面頂上去也是 0，問題解決。

### 3.4 真正的目的：期望值和積分可以交換

[▶ 20:59](https://youtu.be/pFK4f8YmmiU?t=1259) 課本只是要算 $E[\mathbf{s}]$ 和 $E[\mathbf{s}^2]$，為什麼要提 Riemann？

- $E[\mathbf{s}]$ 的原始定義是**先積分、再取期望值**：$E\left[\int_a^b X(t)\,dt\right]$。
- 但我們運算時會**交換**成先取期望值、再積分：$\int_a^b E[X(t)]\,dt$。
- 數學上任何交換都要問：**能不能換？** 這就是嚴謹。
- Lebesgue 討論的常是很怪的函數（有理數、無理數對應到不同值，劇烈跳躍），積分和期望值互換可能出問題、有反例。
- Papoulis 說「以下積分都是 Riemann」，等於限定是 nice 的函數，交換就沒問題。工程上也很少碰到那些怪函數。

老師說【口頭】：數位通訊課每次都直接把期望值和積分對調，很自然；但嚴格說不一定能這樣做。他在美國修實變分析時，數學系老師很重視定理和證明；他覺得之後還要想：這個定理在工程上有沒有意義、怎麼調整。Papoulis 是數學系的老師，文字描述其實很嚴謹。

---

## 4. 點過程、更新過程、計數過程

[▶ 24:04](https://youtu.be/pFK4f8YmmiU?t=1444) 網路、話務 (traffic) 上很常見。

> - **點過程** (point process)：時間軸上的一組隨機點 $t_1,t_2,t_3,\dots$。
> - **更新過程** (renewal process)：相鄰兩點的差 $z_1=t_1,\ z_2=t_2-t_1,\ \dots,\ z_n=t_n-t_{n-1}$。renew = 重新開始。
> - **計數過程** (counting process)：$X(t)$ = 時間 $(0,t)$ 內有幾個點。

**例：燈泡壽命** [▶ 25:38](https://youtu.be/pFK4f8YmmiU?t=1538)：

- 燈泡什麼時候壞不知道。壞掉的時間 $t_1,t_2,t_3,\dots$ 是點過程。
- 壞了就換新的 (renew the light bulb)，兩次壞掉的間隔 $z_i$ 就是第 $i$ 顆燈泡的壽命，這是更新過程。
- 計數過程：例如 100 年內壞了幾顆。

老師的笑話【口頭】：現在的燈泡好像內建計時器，時間到就壞。他朋友買某家滑鼠保證一年，結果一年後全部同時壞掉——「這家公司的 renewal process 做得真好」。

【課本補充】Papoulis p. 387（Fig. 9-4）：三個概念一一對應——點過程 $t_i$；在每個 $t_i$ 跳一階的離散狀態過程 $X(t)$；更新過程 $z_i$，且 $t_n=z_1+\dots+z_n$。

---

## 5. Poisson 過程

### 5.1 定義：兩個性質

[▶ 27:11](https://youtu.be/pFK4f8YmmiU?t=1631) 做網路的一定會碰到。它的定義**完全來自需求或觀察**，沒提任何機率空間，只用結果的性質定義。考試、習題能用的性質**只有這兩個**。

> **Poisson 過程**：$X(t)=n(0,t)$ = 區間 $(0,t)$ 內的 **Poisson 點**個數，其中：
> 1. **（Poisson 分布）** 區間 $(t_1,t_2)$ 內的點數 $n(t_1,t_2)$ 是 Poisson 隨機變數：
> $$P\{n(t_1,t_2)=k\}=e^{-\Lambda}\frac{\Lambda^k}{k!},\qquad\Lambda=\int_{t_1}^{t_2}\lambda(t)\,dt.$$
>    $\lambda$ 為常數時 $\Lambda=\lambda(t_2-t_1)$。
> 2. **（獨立增量）** 若 $(t_1,t_2)$ 和 $(t_3,t_4)$ **不重疊** (non-overlapping)，則 $n(t_1,t_2)$ 和 $n(t_3,t_4)$ **獨立**。

- 早期電話話務是 Poisson：大家打電話不互相協調、彼此獨立，而且長話短說（通話時間呈指數衰減）。老師開玩笑說現在大家講電話都很久，就不是 Poisson 了。【口頭】
- **要證明某個過程是 Poisson，兩個條件都要證**。通常大家只證第 1 個、忘了第 2 個；證獨立通常比較難。
- 圖：$X(t)$ 從 0 開始，每來一個點（一通電話、一個封包）就累加 1，是一條往上的階梯。

老師說【口頭】：以前做網路的 shaper、switch、router，看到 Poisson 輸入很開心；後來實際量測發現 **Ethernet traffic 根本不是 Poisson**，用 Poisson 假設設計的都不好，因為網路流量大多是 Noah effect：大家不約而同一起上網、看同一張照片、同一則新聞，然後塞車。這是現在做 server 的挑戰。

【課本補充】Papoulis Example 9-5（p. 378）：性質 $P_1$、$P_2$，式 (9-13)；非均勻情形見 (9-16)、(9-17)。

### 5.2 平均

[▶ 32:53](https://youtu.be/pFK4f8YmmiU?t=1973) Poisson 隨機變數只要給一個參數，就是它的期望值。所以（把 $t_1$ 換成 0、$t_2$ 換成 $t$）：
$$\eta(t)=E[X(t)]=E[n(0,t)]=\int_0^t\lambda(\alpha)\,d\alpha.$$
$\lambda$ 為常數時 $\eta(t)=\lambda t$。

（這裡都假設 Riemann 積分，所以積分和期望值可以互換。）

### 5.3 自相關：先用性質 2 拆開

[▶ 33:54](https://youtu.be/pFK4f8YmmiU?t=2034) 記 $\Lambda(t)=\int_0^t\lambda(\alpha)\,d\alpha$。先假設 $t_1<t_2$。

**Step 1：寫定義。**
$$R(t_1,t_2)=E[X(t_1)X(t_2)]=E\left[n(0,t_1)\,n(0,t_2)\right].$$

**Step 2：用性質 2，把 $(0,t_2)$ 拆成不重疊的兩段。** 這是關鍵：0 到 $t_1$ 來 3 通、$t_1$ 到 $t_2$ 來 5 通，整段就是 8 通。
$$n(0,t_2)=n(0,t_1)+n(t_1,t_2).$$

**Step 3：乘進去。**
$$R(t_1,t_2)=E\left[n^2(0,t_1)\right]+E\left[n(0,t_1)\,n(t_1,t_2)\right].$$

**Step 4：$(0,t_1)$ 和 $(t_1,t_2)$ 不重疊 → 獨立（性質 2）**，第二項拆成兩個期望值相乘：
$$R(t_1,t_2)=E\left[n^2(0,t_1)\right]+E\left[n(0,t_1)\right]E\left[n(t_1,t_2)\right].$$

**Step 5：用性質 1（Poisson 的動差）。** Poisson 參數 $\Lambda$ 的平均是 $\Lambda$、變異數也是 $\Lambda$，所以二階動差 $=\Lambda+\Lambda^2$。
$$R(t_1,t_2)=\Lambda(t_1)+\Lambda^2(t_1)+\Lambda(t_1)\left[\Lambda(t_2)-\Lambda(t_1)\right]=\Lambda(t_1)+\Lambda(t_1)\Lambda(t_2).$$
（$n(t_1,t_2)$ 的參數是 $\int_{t_1}^{t_2}\lambda=\Lambda(t_2)-\Lambda(t_1)$。）

**Step 6：$t_1>t_2$**：同樣做法，把 $(0,t_1)$ 拆成 $(0,t_2)$ 和 $(t_2,t_1)$。結果只差第一項變成 $\Lambda(t_2)$。所以第一項永遠取**小的**：
$$\boxed{R(t_1,t_2)=\Lambda\left(\min(t_1,t_2)\right)+\Lambda(t_1)\Lambda(t_2)}$$

老師說【口頭】：Poisson 過程只有兩個性質，任何性質都只能用這兩個推。解題套路：**先用性質 2 想辦法拆成不重疊的區間，再用性質 1 算 Poisson**。考試大概都考這種。因為性質 2 是「獨立」而不只是「不相關」，性質 1 又給了 Poisson 的所有動差，所以三階動差也算得出來，比二階多一點東西。

**$\lambda$ 是常數時**：$\Lambda(t)=\lambda t$，
$$R(t_1,t_2)=\lambda\min(t_1,t_2)+\lambda^2t_1t_2.$$

【課本補充】Papoulis 式 (9-14)：$R(t_1,t_2)=\lambda t_2+\lambda^2t_1t_2$（$t_1\ge t_2$），$\lambda t_1+\lambda^2t_1t_2$（$t_1\le t_2$）；非均勻情形 (9-17)：$R(t_1,t_2)=\int_0^{t_1}\lambda(t)\,dt\left[1+\int_0^{t_2}\lambda(t)\,dt\right]$（$t_1\le t_2$），和上面一致。

### 5.4 解讀：為什麼相關不會衰減

[▶ 40:10](https://youtu.be/pFK4f8YmmiU?t=2410) 老師說：很多論文證完定理就結束；他希望學生要**討論結果**。【口頭】

**看到什麼**：二階動差是能量。$R(t_1,t_2)$ 隨時間**線性增加**，而且很快。

**自相關的操作意義** (operational meaning)：給一個量化指標，表示**單點和另一個單點**之間的關係（$t_2$ 當現在，$t_1$ 就是過去；$t_1$ 當現在，$t_2$ 就是未來）。現在 big data 幾乎都用它算資料之間的關係。

**看自協方差**（$\lambda$ 常數）：
$$C(t_1,t_2)=R(t_1,t_2)-\eta(t_1)\eta(t_2)=\lambda\min(t_1,t_2)+\lambda^2t_1t_2-\lambda t_1\cdot\lambda t_2=\lambda\min(t_1,t_2).$$

- 一般直覺（例如 Proakis 書裡的通訊訊號）：同一個過程的兩點，時間拉得越遠，相關應該越弱。
- 但這裡固定 $t_1$、把 $t_2$ 一直拉遠（今天跟明天、後天、大後天），$C=\lambda t_1$ 是**常數**，**不會衰減** (does not die away)，一直維持一個準位。

**為什麼？** 回到過程本身：它算的是**累積量**。

- 0 到 $t_1$ 來了 8 個人，0 到 $t_2$ 來了 12 個人。這 12 個人裡有 8 個就是 0 到 $t_1$ 來的。
- 所以 $X(t_2)$ 和 $X(t_1)$ 一定有很強的關係，而且這個關係**不會衰減**：到後天，這 8 個人還在裡面。
- 累積量通常都有這個現象。

**$R$ 為什麼還會線性增加？** 多出的 $\lambda^2t_1t_2$ 就是 $\eta(t_1)\eta(t_2)$，來自**一階（DC）**：這個過程有一個很強、隨時間增加的 DC，自相關才會拉得越遠反而越大。

老師的應用提醒【口頭】：以後做 big data，如果量到兩個參數之間有很強、不衰減的相關，就要想到：原始的量裡可能有一個分量一直在（像累積量、像 DC）。例如量河川和旁邊工廠排放物的相關越來越大，或像北京霧霾每年增加，要去詮釋背後是什麼原因。

---

## 6. 一頁速查表

### 限制

- **獨立增量**：不重疊區間的增量獨立。**不相關增量**：換成不相關。
- **常態過程**：任何有限個樣本聯合常態；由 $\eta(t)$、$C(t_1,t_2)$ 完全決定。
- **存在定理**：任何 $\eta$ 和非負定 $C$ → 存在常態過程；證明用 (9-46) 特性函數 $\exp\{j\sum\eta_i\omega_i-\frac12\sum C_{ik}\omega_i\omega_k\}$。

### 積分

- Riemann：上、下階梯函數的 inf／sup 相等。
- 反例：有理數指示函數，下和 0、上和 $b-a$。
- Lebesgue：simple function，底是 Borel 集；$\lambda(\mathbb{Q})=0$ → 積分 0。
- 課本說「Riemann 積分」是為了 $E\left[\int X\,dt\right]=\int E[X]\,dt$ 可以交換。

### 點過程

- 點 $t_i$；更新 $z_i=t_i-t_{i-1}$；計數 $X(t)=n(0,t)$；$t_n=z_1+\dots+z_n$。

### Poisson 過程

| 量 | 結果 |
|---|---|
| 定義 | ① $n(t_1,t_2)\sim\text{Poisson}\left(\int_{t_1}^{t_2}\lambda\right)$ ② 不重疊區間獨立 |
| 平均 | $\eta(t)=\Lambda(t)=\int_0^t\lambda$；常數時 $\lambda t$ |
| 自相關 | $R=\Lambda(\min(t_1,t_2))+\Lambda(t_1)\Lambda(t_2)$；常數時 $\lambda\min(t_1,t_2)+\lambda^2t_1t_2$ |
| 自協方差 | $C=\lambda\min(t_1,t_2)$ |

- 關鍵一步：$n(0,t_2)=n(0,t_1)+n(t_1,t_2)$，兩段獨立；Poisson 二階動差 $\Lambda+\Lambda^2$。
- 解讀：累積量 → 相關不衰減；$\lambda^2t_1t_2$ 來自 DC。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Poisson 過程的兩個性質 | 下一集：電報訊號 (telegraph signal)、更多 Poisson 例子 |
| 平穩（課本 p. 387 緊接著） | 下一集起：SSS、WSS |
| 期望值與積分交換 | §9-2 系統輸出的平均與自相關（第 9–11 集） |
| 常態過程 | 常態過程通過線性系統仍是常態 |
| 布朗運動、獨立增量 | Random walk（§10-1，課程跳過）、Wiener process |

---

## 附：本集一句話總結

> **Poisson 過程只靠兩個性質（點數是 Poisson、不重疊區間獨立）定義；算任何統計量的套路都是「先拆成不重疊區間，再用 Poisson 動差」，算出的自協方差 $\lambda\min(t_1,t_2)$ 不會隨時間拉遠而衰減，因為它是累積量。**

---

## ⚠️ 待確認清單

1. [▶ 04:37](https://youtu.be/pFK4f8YmmiU?t=277) 「上學期教的 Herkin 那本」推測是 Haykin 的書，書名待確認。
2. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-1 (5/7) 錄影逐字稿（whisper large-v3-turbo，46:42）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
