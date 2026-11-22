---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 28
lecture: Lec 11-4 Spectral Representation — Spectral Representation of Random Processes (1/2)
date: 待補
video: https://youtu.be/HJAyotjQU4M
notes: Papoulis & Pillai 4th ed. §11-4（式 (11-65)–(11-93)、Theorem 11-2、Example 11-11、Wold's decomposition，pp. 513–518）
---

# 第 28 集 · Lec 11-4 (1/2)：隨機過程的頻譜表示——WSS ⇔ 頻域白、實數過程的實部虛部、windowing、Fourier–Stieltjes 表示、Wold 分解 [▶ 影片](https://youtu.be/HJAyotjQU4M)

← 上一集：[27](27-karhunen-loeve-expansion-wiener-process-fourier-eigenfunctions.md) ｜ [總目錄](README.md) ｜ 下一集：[29](29-wold-decomposition-intuition-example-discrete-bispectrum.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 28 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（55:08，whisper large-v3-turbo）＋ Papoulis §11-4（pp. 513–518）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「frequency domain」→「fliquid domain／Fringer Domain／free domain」，「time domain」→「Title面／tide domain／tine domain／tidal面」，「lemma」→「lama／lay」，「autocorrelation」→「AutoQuality／Auto-Collision／autocry／Auto-Coin／autoclion／autochrome」，「wide-sense stationary」→「Wise and Stated／Y線Stationary／weizen statement／whisen stationary」，「nonstationary white」→「non-stationary white／non-stationary y」，「white」→「坏的／壞」，「uncorrelated scattering」→「Uncollated Scattering」，「fading channel」→「Fading Channel」，「實部／虛部」→「實步／虛步」，「純實數」→「純時數」，「windowing」→「windowing」，「weighting」→「waiting」，「convolution」→「compulsion／combolution」，「Fourier–Stieltjes representation」→「Fullier Cot Representation／StuT」，「orthogonal increment」→「orthogonal increment」，「Poisson process」→「Proson Process／prozone process」，「Brownian motion」→「Bronnier Motion」，「Wold decomposition」→「Vold／world decomposition」，「regular process」→「regular process」，「predictable」→「predict／prey」，「linear predictor」→「linear predictor」，「orthogonal principle」→「Orthogonal Principle」，「inner product」→「inner product」，「Wiener–Hopf equation」→「Weiner-Hope equation／Wine and Hope equation」，「causal」→「causal」，「whitening filter」→「whitening filter」，「倒數」→「導數」，「正交」→「證交」，「線性組合」→「性性組合」。以下一律用正確的字。

> **接上一集**：上一集看到 WSS 過程的傅立葉轉換就是 KL 展開，頻域是白的。這集正式講：**時域 WSS ⇔ 頻域（非平穩）白**，再加上 windowing、Fourier–Stieltjes 表示和 Wold 分解。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 引理：兩個 domain 的自相關和頻譜對調](#1-引理兩個-domain-的自相關和頻譜對調)
- [2. Theorem 11-2：非平穩白 ⇔ 頻域 WSS](#2-theorem-11-2非平穩白--頻域-wss)
- [3. 實數 WSS：頻域實部、虛部能量平衡且正交](#3-實數-wss頻域實部虛部能量平衡且正交)
- [4. Windowing](#4-windowing)
- [5. Fourier–Stieltjes 表示：正交增量](#5-fourierstieltjes-表示正交增量)
- [6. Wold 分解](#6-wold-分解)
  - [6.1 定理](#61-定理)
  - [6.2 關鍵一步：最佳線性預測的誤差是白的](#62-關鍵一步最佳線性預測的誤差是白的)
  - [6.3 拆解：$X_r$ 和 $X_p$](#63-拆解x_r-和-x_p)
  - [6.4 證明 $X_p$ 可預測](#64-證明-x_p-可預測)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 引理、Theorem 11-2 | [▶ 00:00](https://youtu.be/HJAyotjQU4M?t=0) | 式 (11-65)–(11-69)，(11-76)，pp. 513–515 |
| 實數 WSS | [▶ 07:10](https://youtu.be/HJAyotjQU4M?t=430) | 式 (11-78)、(11-79)，p. 515 |
| Windowing | [▶ 11:50](https://youtu.be/HJAyotjQU4M?t=710) | 式 (11-80)–(11-83)、Example 11-11，pp. 515–516 |
| Fourier–Stieltjes | [▶ 20:02](https://youtu.be/HJAyotjQU4M?t=1202) | 式 (11-84)–(11-88)，pp. 516–517 |
| Wold 分解 | [▶ 24:37](https://youtu.be/HJAyotjQU4M?t=1477) | 式 (11-89)–(11-93)，pp. 517–518；§13-2 |

---

## 1. 引理：兩個 domain 的自相關和頻譜對調

[▶ 00:00](https://youtu.be/HJAyotjQU4M?t=0) 大部分同學分析 WSS 過程都在時域拼命做。這節轉到**頻域**做分析，老師覺得這個觀念很有用。

**頻譜表示**：直接把隨機過程轉到頻域，頻域本身也是隨機過程：
$$X(\omega)=\int_{-\infty}^{\infty}X(t)e^{-j\omega t}dt\qquad\text{(11-65)},\qquad X(t)=\frac1{2\pi}\int X(\omega)e^{j\omega t}d\omega\qquad\text{(11-66)}$$
（均方意義的極限）。

> **引理**：$X(t)$ 是**任意**隨機過程（$R(t_1,t_2)$ 兩個參數，不一定 WSS）。令二維傅立葉轉換
> $$\Gamma(u,v)=\iint R(t_1,t_2)e^{-j(ut_1+vt_2)}dt_1dt_2\qquad\text{(11-67)},$$
> 則
> $$E\{X(u)X^*(v)\}=\Gamma(u,-v)\qquad\text{(11-68)}.$$

**意思**：**小寫 $x$ 的（二維）功率頻譜就是大寫 $X$ 的自相關**，反之亦然——兩個 domain 剛好對調，只差一個負號。

**證明**：$E\{X(u)X^*(v)\}=\iint E\{X(t_1)X^*(t_2)\}e^{-jut_1}e^{+jvt_2}dt_1dt_2$。負號是因為共軛讓 $e^{-jvt_2}$ 變 $e^{+jvt_2}$。老師說不用背，數學很簡單，要理解的是「對調」。

---

## 2. Theorem 11-2：非平穩白 ⇔ 頻域 WSS

[▶ 02:35](https://youtu.be/HJAyotjQU4M?t=155) 課本寫成 example（老師說其實是重要定理）。

**非平穩白** (nonstationary white)：$R(t_1,t_2)=q(t_1)\delta(t_1-t_2)$。
- $t_1\ne t_2$ 都是 0：任兩個不同時間沒有能量的交互影響。
- 但自己對自己的能量 $q(t)$ 不一樣（早上、下午、晚上不同）。

**例子**【口頭】：fading channel 有很多路徑（直射、打天花板再下來、打地板再下來），到達時間都不一樣。為了簡化分析和實作，假設 **uncorrelated scattering**：不同路徑、不同 delay 的訊號不相關（零平均就是正交）；但每條路徑衰減不同，能量不一樣。這就是非平穩白。

> **Theorem 11-2**：若 $R(t_1,t_2)=q(t_1)\delta(t_1-t_2)$，則
> $$E\{X(\omega+\alpha)X^*(\alpha)\}=Q(\omega)=\int q(t)e^{-j\omega t}dt\qquad\text{(11-69)}.$$
> 即**非平穩白的傅立葉轉換是 WSS**。

**證明**：二維傅立葉轉換，delta 和一個積分消掉：
$$\Gamma(u,v)=\iint q(t_1)\delta(t_1-t_2)e^{-j(ut_1+vt_2)}dt_1dt_2=\int q(t_2)e^{-j(u+v)t_2}dt_2=Q(u+v).$$
用引理：$E\{X(u)X^*(v)\}=\Gamma(u,-v)=Q(u-v)$——只跟**頻率差**有關，所以頻域是 WSS。∎

**反過來**（WSS ⇒ 頻域非平穩白）[▶ 06:09](https://youtu.be/HJAyotjQU4M?t=369)：$R(t_1,t_2)=R(t_1-t_2)$ 時
$$\Gamma(u,v)=2\pi S(u)\delta(u+v)\qquad\text{(11-75)},\qquad E\{X(u)X^*(v)\}=2\pi S(u)\delta(u-v)\qquad\text{(11-76)}.$$
（負號讓 $u+v$ 變 $u-v$。）所以變成 if and only if。

> **這節要學的兩個文字觀念**：
> 1. **白的東西，另一個 domain 是 WSS。**
> 2. **WSS 的東西，另一個 domain 是白的。**

為什麼喜歡到另一個 domain 分析？白的東西很容易分析——任兩個不同時間（頻率）沒有能量交互影響。老師說過去同學可能都沒想到，這對數據分析很有幫助。

【課本補充】p. 515：反過來也對（Prob. 11-12）：$X(t)$ 是 WSS ⇔ $E\{X(\omega)\}=0$（$\omega\ne0$）且 $E\{X(u)X^*(v)\}=Q(u)\delta(u-v)$（式 (11-77)）。p. 514：$X$ 是實數時 $E\{X(u)X(v)\}=\Gamma(u,v)$、$X(-\omega)=X^*(\omega)$；實數高斯過程時 $\mathrm{Cov}\{|X(u)|^2,|X(v)|^2\}=\Gamma^2(u,-v)+\Gamma^2(u,v)$（Theorem 11-3）。

---

## 3. 實數 WSS：頻域實部、虛部能量平衡且正交

[▶ 07:10](https://youtu.be/HJAyotjQU4M?t=430) 多加一個條件（以前考過）：$X(t)$ 是 WSS **而且純實數**。會額外得到什麼？

**Step 1**：頻域是非平穩白，所以看 $\omega$ 和 $-\omega$ 兩個頻率：$\omega\ne-\omega$（$\omega\ne0$），所以
$$E\{X(\omega)X^*(-\omega)\}=0.$$
【口頭】通訊上正、負頻率分不開——實作上做不出 $-1.8$ GHz（負頻率是美麗的想像），但數學上它們的相關一定是 0。

**Step 2**：時域純實數 ⇒ 頻域**共軛對稱**：$X(-\omega)=X^*(\omega)$。代入：
$$E\{X(\omega)X^*(-\omega)\}=E\{X^2(\omega)\}=0.$$

**Step 3**：拆實部、虛部 $X(\omega)=A(\omega)+jB(\omega)$：
$$E\{X^2(\omega)\}=E\{A^2\}-E\{B^2\}+2jE\{AB\}=0.$$
實部、虛部都要是 0：

> **結論**：實數 WSS 過程的傅立葉轉換不只是白的，而且
> $$E\{A^2(\omega)\}=E\{B^2(\omega)\},\qquad E\{A(\omega)B(\omega)\}=0\qquad\text{(11-79b)}.$$
> 實部虛部**能量平衡**、**完全正交**。

所以實部、虛部還可以拆開分析，互不影響。

**數據分析的提醒**【口頭】：現在很多人做 big data。老師當口試委員時，很多人把河川、天氣資料直接當穩態做 autocorrelation——比較有深的認識的話，看結果會覺得資料本身不是穩態。做一個傅立葉轉換就知道，它不像穩態（頻域不白）。

【課本補充】p. 515：實數時 $X(t)=\frac1\pi\int_0^\infty A(\omega)\cos\omega t\,d\omega-\frac1\pi\int_0^\infty B(\omega)\sin\omega t\,d\omega$（式 (11-78)），且 $u\ne v$ 時 $E\{A(u)A(v)\}=E\{A(u)B(v)\}=E\{B(u)B(v)\}=0$（式 (11-79a)）。反過來也對（Prob. 11-13）。

---

## 4. Windowing

[▶ 11:50](https://youtu.be/HJAyotjQU4M?t=710) 實際上不可能從 $-\infty$ 看到 $\infty$，一定是透過一個 window 看（觀察一年、觀察一個人一個月）。課本沒著墨太多，只講關係。

**數學模型**：$Y(t)=w(t)X(t)$ 是一個**時變線性濾波器**（脈衝響應 $w(t)\delta(\tau)$：$\delta$ 是卷積不改變，$w(t)$ 改變時間 domain）。例：$w(t)=p_T(t)$，$|t|<T$ 乘 1、外面乘 0（Example 11-11）。

**自相關**（用 Theorem 9-2）：
$$R_{YY}(t_1,t_2)=w(t_1)w^*(t_2)R(t_1-t_2).$$

- **非常直觀**：對資料做 window，就相當於對自相關做 window——$t_1$ 乘一次、$t_2$ 乘一次。二維自相關**直接截掉**外面那塊。
- window 前、後的自相關對你都沒影響，因為直接切掉了。
- 也可以有 **weighting**：比較相信最近的數字（一個月前乘 1、一年前乘 0.1），自相關乘上一模一樣的 weighting。

**頻譜**：時域相乘 → 頻域**卷積**，不直觀：
$$\Gamma_{YY}(u,v)=\frac1{2\pi}\int W(u-\beta)W^*(-v-\beta)S(\beta)\,d\beta\qquad\text{(11-80)},$$
$$E\{|Y(\omega)|^2\}=\frac1{2\pi}\int|W(\omega-\beta)|^2S(\beta)\,d\beta\qquad\text{(11-82)}.$$

**Example 11-11**：$X_T(\omega)=\int_{-T}^TX(t)e^{-j\omega t}dt$，$W(\omega)=\frac{2\sin T\omega}{\omega}$：
$$E\{|X_T(\omega)|^2\}=S(\omega)*\frac{2\sin^2T\omega}{\pi\omega^2}\qquad\text{(11-83)}.$$
老師說：這時在頻譜上分析好像沒好處（是卷積，而且是切掉的 sinc，比較複雜）；在時域分析 window 比較容易。

---

## 5. Fourier–Stieltjes 表示：正交增量

[▶ 20:02](https://youtu.be/HJAyotjQU4M?t=1202) 資料分析有很多層：時域（河流流量 $X(t)$）→ 覺得是 WSS，到頻域（白的）→ 頻域也不好分析時，**再積分**。就像分析分布時，PDF 不好分析就用 CDF。

$$Z(\omega)=\int_0^\omega X(\alpha)\,d\alpha\qquad\text{(11-84)},\qquad dZ(\omega)=X(\omega)d\omega,\qquad X(t)=\frac1{2\pi}\int e^{j\omega t}dZ(\omega)\qquad\text{(11-87)}.$$
（課本註：Cramér 提出。積分是線性濾波器。）

> **性質**：$X$ 是 WSS ⇒ $Z(\omega)$ 有**正交增量** (orthogonal increment)：$\omega_1<\omega_2<\omega_3<\omega_4$ 時
> $$E\{[Z(\omega_2)-Z(\omega_1)][Z^*(\omega_4)-Z^*(\omega_3)]\}=0\qquad\text{(11-85a)},\qquad E|Z(\omega_2)-Z(\omega_1)|^2=2\pi\int_{\omega_1}^{\omega_2}S(\omega)d\omega\qquad\text{(11-85b)}.$$

**證明**：增量寫成 $X$ 的積分，積分和期望值互換，得頻域自相關 $2\pi S(\alpha)\delta(\alpha-\beta)$；delta 和積分對消要注意範圍：$\alpha$ 在 $(\omega_1,\omega_2)$、要等於落在 $(\omega_3,\omega_4)$ 的 $\beta$——兩區間不重疊，所以是 0。∎

就像 Poisson 過程、Wiener 過程：不重疊區間沒關係。所以**布朗運動、Poisson 過程可能是某個白過程的積分**；要回到白的，就微分。這些性質彼此有關聯。

---

## 6. Wold 分解

### 6.1 定理

[▶ 24:37](https://youtu.be/HJAyotjQU4M?t=1477) 老師說這是這一章非常重要的定理。

> **Wold 分解**：任何 WSS 過程都可以拆成
> $$X=X_r+X_p\qquad\text{(11-89)},$$
> $X_r$ 是 **regular** 過程、$X_p$ 是 **predictable** 過程，而且兩者**正交**：$E\{X_r(t+\tau)X_p^*(t)\}=0$（式 (11-91)）。

- **regular**：可以寫成**白色輸入經過 causal 且 stable 的濾波器**：$X_r(t)=\int_0^\infty l(\tau)I(t-\tau)d\tau$（離散：$\sum_{k\ge0}l_kI[n-k]$）。
- **predictable**（文字定義）：用過去百分之百預測未來，誤差是 0。
- 拆解**不一定唯一**，只要找到一組。
- 兩者都要是 WSS（例如 $a=2$、$a=\frac12$ 那種非平穩的可預測過程加起來不會是 WSS，老師請同學自己想怎麼證）。

**為什麼重要（和第 13 章 estimation 的關聯）**【口頭】：
- predictable 部分**不需要做 estimation**（定義就是能百分之百預測）。
- 只要針對 regular 部分做預測——用形成它的濾波器係數就得到最好的估計濾波器。
- 所以 WSS 過程很好預測：拆成兩塊，一塊完全可預測，另一塊用形成的係數預測。書上沒這樣串，老師把它串起來。

**用詞提醒**：第 13 章的定理是「a process is predictable iff its spectrum consists of lines」。這有點怪：$a=\frac12$、$a=2$ 的 AR（$X[t]=aX[t-1]$）也可以用過去預測未來，但不是線譜、也不是 WSS。所以要自己加上：**WSS 過程**是可預測的 ⇔ 頻譜是線（根在單位圓上）。看上下文或證明（第 13 章的證明確實用到 WSS）就會清楚。

離散版本也一樣成立；老師用**離散版本**證明（比較好想像）。這是這一章最長的證明（四頁），和 estimation 很有關。

> ⚠️ 課堂證明和課本不同：課本 pp. 517–518 用 Fourier–Stieltjes 的 $Z(\omega)$ 拆成連續部分 $Z_r$ 和階梯部分 $Z_p$ 來證明；老師用的是**線性預測**的證明（以下）。

### 6.2 關鍵一步：最佳線性預測的誤差是白的

[▶ 30:16](https://youtu.be/HJAyotjQU4M?t=1816) 用過去的線性組合預測現在（linear predictor；預測也可以非線性，但實作大多線性）：
$$\hat X[n]=\sum_{k=1}^{\infty}a_kX[n-k],\qquad E[n]=X[n]-\hat X[n].$$
取均方意義最佳的 $a_k$。

**正交原理** (orthogonality principle)【口頭】：線性代數——用過去在另一個平面上的線性組合去近似，最近的點就是**垂直**（正交）的那個點。垂直是幾何概念，這裡是**借用**：資料之間的內積定義為
$$\langle X,Y\rangle=E\{XY^*\},$$
符合內積的四個基本性質，所以線性代數的推導全部可用。最佳估計的誤差和所有資料正交：
$$E\{E[n]X^*[n-k]\}=0,\quad k\ge1.$$
（由此解 $a_k$ 的方程叫 **Wiener–Hopf 方程**，不是這裡的重點。）

> **Wold 看到的最重要性質**：WSS 過程做最佳線性預測，**剩下沒預測到的誤差 $E[n]$ 是白的**。

**證明**：要證 $E\{E[n]E^*[n+\tau]\}=0$（$\tau<0$，例如 $\tau=-2$）。$E[n-2]=X[n-2]-\sum a_kX[n-2-k]$ 只跟 $X[n-2],X[n-3],\dots$ 有關——對時間 $n$ 來說全是**過去的資料**。$E[n]$ 和過去的資料都正交，所以兩項都是 0。∎

老師說這一步是整個證明的 key step，到這裡大概就做完了。

### 6.3 拆解：$X_r$ 和 $X_p$

[▶ 38:04](https://youtu.be/HJAyotjQU4M?t=2284) 現在**用誤差 $E$ 當資料**對 $X$ 做最佳線性估計：
$$X_r[n]=\sum_{k=0}^{\infty}w_kE[n-k],\qquad X_p[n]=X[n]-X_r[n].$$

- 奇怪的地方：$E$ 是白的，$E[n-1],E[n-2],\dots$ 彼此無關；但 $X[n]$ 和 $E[n]$ 還是有關的。
- $X_r$：白色輸入經過 causal 濾波器 $W$（之後可證 stable）→ **regular**（下標 r）。
- $X_p$：用 $E$ 估計 $X$ 剩下的部分，由正交原理和所有 $E[n-k]$（$k\ge0$）正交；$X_r$ 是這些 $E$ 的線性組合 → **$X_r\perp X_p$**。
- 拆成兩塊、統計上完全正交：一塊不能完全預測、可由濾波器產生；另一塊可以完全預測。剩下最 tricky 的是證明 $X_p$ 是 predictable。

### 6.4 證明 $X_p$ 可預測

[▶ 41:07](https://youtu.be/HJAyotjQU4M?t=2467)

**定義兩個濾波器**：
- $A(z)=1-\sum_{k\ge1}a_kz^{-k}$（$a_k$ 是用 $X$ 的過去預測 $X$ 的最佳係數；$k=0$ 項是 1）。
- $W(z)=\sum_{k\ge0}w_kz^{-k}$（用 $E$ 估計 $X$ 的最佳係數）。

**定義** $Y$：$X_p$ 經過 $A$ 的輸出：
$$Y[n]=X_p[n]-\sum_{k\ge1}a_kX_p[n-k].$$
如果 $X_p$ 是 predictable，就是 $X_p[n]=\sum a_kX_p[n-k]$。所以**只要證明 $Y\equiv0$**。

**怎麼證 $Y=0$**：內積的性質——**自己和自己正交的只有零向量**：$E|Y|^2=0$ ⇒ $Y=0$（就像 $\int|f|^2=0$ ⇒ $f=0$）。

**觀察（方塊圖）**：
1. $X$ 經過 $A$ 輸出 $E$（定義：$E=X-\sum a_kX[n-k]$）。
2. $X_p$ 經過 $A$ 輸出 $Y$（定義）。
3. 線性：$X-X_p=X_r$ 經過 $A$ 輸出 $E-Y$。
4. $E$ 經過 $W$ 輸出 $X_r$（定義）。
5. 串起來：$E\to W\to A\to E-Y$；再用 $E$ 減掉它就得 $Y$。整個黑盒子：
$$Y=\left[1-A(z)W(z)\right]E.$$

**$Y$ 的兩個身份**：
- $A$、$W$ 都 causal（$k$ 從 0 或 1 開始），$1-AW$ 也 causal ⇒ **$Y$ 是 $E[n],E[n-1],\dots$ 的線性組合**。
- $Y$ 是 $X_p$ 經過 $A$ ⇒ **$Y$ 是 $X_p[n],X_p[n-1],\dots$ 的線性組合**。

**正交原理**：$X_p$ 是用 $E$ 估計剩下的部分，和所有 $E[n-k]$（$k\ge0$）正交。所以
$$E|Y|^2=E\{Y\cdot Y^*\}=0$$
（一邊寫成 $X_p$ 的組合、一邊寫成 $E$ 的組合）。⇒ $Y=0$ ⇒ $X_p$ predictable。∎

**注意**：
- $X_p$ 的預測係數**不能亂取**：一定是 $X$ 最佳線性預測的係數 $a_1,a_2,\dots$：$X_p[n]=a_1X_p[n-1]+a_2X_p[n-2]+\cdots$。下一個範例的拆解並沒有照這個做法，但不違反定理——定理只說找得到一組，沒說唯一；要證唯一要另外花功夫。
- **暗示** [▶ 54:06](https://youtu.be/HJAyotjQU4M?t=3246)：如果 $X$ 沒有 predictable 部分，$Y=(1-AW)E=0$ 對白的 $E$ 成立 ⇒ 濾波器是 0 ⇒ $A(z)W(z)=1$，$A$ 是 $W$ 的倒數。老師說 $W$ 這個名字好像隱含 **white**——$A$ 就是 whitening filter。兩者的關係第 13 章會看到端倪。

以下**不是逐字稿內容**，是依課本 p. 518 推論的：老師說的「下面那個範例」應是 Example 11-12（$Y=aX$、$E\{a\}=0$，$X$ regular 且和 $a$ 獨立 ⇒ $Y_p=\eta_xa$、$Y_r=a[X-\eta_x]$），下一集講。

---

## 7. 一頁速查表

### 頻譜表示

| 時域 $X(t)$ | 頻域 $X(\omega)$ |
|---|---|
| 任意：$R(t_1,t_2)$，$\Gamma(u,v)$ | $E\{X(u)X^*(v)\}=\Gamma(u,-v)$（對調、差負號） |
| 非平穩白 $q(t_1)\delta(t_1-t_2)$ | WSS：$E\{X(\omega+\alpha)X^*(\alpha)\}=Q(\omega)$ |
| WSS $R(\tau)$ | 非平穩白：$2\pi S(u)\delta(u-v)$ |
| 實數 WSS | 另加 $E A^2=E B^2$、$E\{AB\}=0$ |

- 關鍵一步：$\Gamma$ 的定義裡 delta 消掉一個積分；共軛讓 $v\to-v$。
- 實數：$X(-\omega)=X^*(\omega)$ ⇒ $E\{X^2(\omega)\}=E\{X(\omega)X^*(-\omega)\}=0$。

### Windowing

$Y=wX$：$R_{YY}=w(t_1)w^*(t_2)R(t_1-t_2)$（直接截掉）；$E\lvert Y(\omega)\rvert^2=\frac1{2\pi}\int\lvert W(\omega-\beta)\rvert^2S(\beta)d\beta$（卷積）。

### Fourier–Stieltjes

$Z(\omega)=\int_0^\omega X(\alpha)d\alpha$，$dZ=Xd\omega$；WSS ⇒ 正交增量，$E\lvert dZ\rvert^2=2\pi S\,d\omega$。

### Wold 分解

$X=X_r+X_p$，$X_r\perp X_p$。證明（離散）：
1. 最佳線性預測誤差 $E$ 是白的（正交原理）。
2. $X_r=\sum_{k\ge0}w_kE[n-k]$（regular），$X_p=X-X_r$。
3. $Y=A*X_p=(1-AW)E$：同時是 $E$ 過去和 $X_p$ 過去的組合，$X_p\perp E$ ⇒ $E\lvert Y\rvert^2=0$ ⇒ $X_p$ 可預測。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Wold 分解、Example 11-12 | 下一集 |
| 正交原理、Wiener–Hopf | §13-1、13-2（第 37–40 集） |
| WSS 可預測 ⇔ 線譜 | §13-2 |
| 頻域白 | 第 12 章頻譜估計（第 34–36 集） |

---

## 附：本集一句話總結

> **時域 WSS 的傅立葉轉換是頻域的非平穩白，非平穩白的傅立葉轉換是 WSS（實數時實部虛部還能量平衡且正交）；window 在時域直接截掉自相關、在頻域是卷積；頻譜積分得到正交增量的 $Z(\omega)$；Wold 分解把任何 WSS 過程拆成正交的 regular（白雜訊過 causal 濾波器）與 predictable 兩部分，關鍵是最佳線性預測的誤差是白的。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-4 (1/2) 錄影逐字稿（whisper large-v3-turbo，55:08）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
