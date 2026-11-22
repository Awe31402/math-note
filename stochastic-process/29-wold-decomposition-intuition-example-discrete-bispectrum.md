---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 29
lecture: Lec 11-4 Spectral Representation — Spectral Representation of Random Processes (2/2)
date: 待補
video: https://youtu.be/Nc2B7DowucE
notes: Papoulis & Pillai 4th ed. §10-7（雙頻譜與系統辨識，pp. 489–492）；§11-4（Wold's decomposition 式 (11-93)–(11-95)、Example 11-12、Discrete-time processes 式 (11-96)–(11-98)、Bispectra 式 (11-99)–(11-102)，pp. 518–521）
---

# 第 29 集 · Lec 11-4 (2/2)：Wold 分解的直觀（拆到最小再組回去）、$X_p$ 和所有誤差正交、Example 11-12、離散頻譜表示、雙頻譜 (bispectrum) 與系統相位 [▶ 影片](https://youtu.be/Nc2B7DowucE)

← 上一集：[28](28-spectral-representation-nonstationary-white-windowing-wold.md) ｜ [總目錄](README.md) ｜ 下一集：[30](30-ergodicity-shift-invariant-event-history.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 29 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（39:55，whisper large-v3-turbo）＋ Papoulis §11-4（pp. 518–521）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「Wold decomposition」→「Wall Decompetition／Valdecompetition／Boldy Composition／wo」，「wide-sense stationary」→「Widescent Stationery／Whitesense Stationary」，「正交」→「證交／正焦」，「standing wave（駐波）」→「鑄波」，「Lebesgue」→「the best」，「absolutely continuous／singular」→「absolutely continuous／singular」，「stationary ergodic」→「station ergotic」，「i.i.d.」→「RID／id」，「orthogonality principle」→「Orthogonal Principle」，「causal／stable」→「Causal／Stable」，「regular」→「regural」，「factorization」→「factorization」，「minimum phase」→「minimum phase」，「autocorrelation」→「Auto Corrigine／autocritic」，「DC stuck」→「DC stock」，「bispectrum」→「by spectrum／bySpectrum」，「third-order moment」→「third moment／third order moment」，「strict-sense stationary」→「strict and stationary／strictly sense station」，「magnitude response」→「magnitude response」，「conjugate symmetry」→「conjugate symmetry」，「time domain／frequency domain」→「Tile Domain／tide domain／tine domain／Frequent Domain／Frigged Domain」，「uncorrelated scattering」→「uncorrelated scattering」，「nanosecond」→「nanosecond／nosecond」，「單位圓」→「單位元／單位員／單位園」。以下一律用正確的字。

> **接上一集**：上一集用線性預測證明了 Wold 分解。這集老師先回頭討論**這個證明在做什麼、為什麼重要**，再講課本的範例、離散版本和雙頻譜。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Wold 分解的直觀：拆到最小再組回去](#1-wold-分解的直觀拆到最小再組回去)
- [2. $X_p$ 是什麼：駐波](#2-x_p-是什麼駐波)
- [3. 更強的結論：$X_p$ 和所有誤差正交](#3-更強的結論x_p-和所有誤差正交)
- [4. 證明的兩個缺口](#4-證明的兩個缺口)
- [5. 頻譜：把脈衝抽出來](#5-頻譜把脈衝抽出來)
- [6. Example 11-12](#6-example-11-12)
- [7. 離散時間過程的頻譜表示](#7-離散時間過程的頻譜表示)
- [8. 雙頻譜 (bispectrum)](#8-雙頻譜-bispectrum)
  - [8.1 定義](#81-定義)
  - [8.2 為什麼要三階：系統相位](#82-為什麼要三階系統相位)
  - [8.3 用白雜訊量測相位](#83-用白雜訊量測相位)
  - [8.4 SSS 過程的雙頻譜在頻域](#84-sss-過程的雙頻譜在頻域)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| Wold 分解的討論 | [▶ 00:00](https://youtu.be/Nc2B7DowucE?t=0) | pp. 517–518 |
| Example 11-12 | [▶ 18:15](https://youtu.be/Nc2B7DowucE?t=1095) | p. 518 |
| 離散頻譜表示 | [▶ 21:23](https://youtu.be/Nc2B7DowucE?t=1283) | 式 (11-96)–(11-98)，p. 519 |
| 雙頻譜 | [▶ 26:01](https://youtu.be/Nc2B7DowucE?t=1561) | 式 (11-99)–(11-102)，pp. 519–521 |

---

## 1. Wold 分解的直觀：拆到最小再組回去

[▶ 00:00](https://youtu.be/Nc2B7DowucE?t=0) 老師說這算這一章最重要的定理之一，回頭花點時間討論。

**濾波器 $A(z)$**：輸入 WSS 過程 $X$，輸出誤差 $E$。
- $E[t]$：用 $X[t-1],X[t-2],\dots$ 對 $X[t]$ 做最佳線性預測，**剩下沒辦法預測的部分**。
- $E[t+1]$：用 $X[t],X[t-1],\dots$ 預測 $X[t+1]$ 剩下的部分。

**拆玩具的比喻**【口頭】：小時候看到玩具都想把它拆掉，拆到最小的螺絲元件；物理化學也想把東西拆到最小單位——原子、分子。
- **第一步（$A$）= 拆解**：拆到最小的部分就是 $E$。所有的 $E$ 彼此正交（「獨立」的感覺），是白的——能量上完全沒有影響、不能再拆的最小單元。
- **第二步（$W$）= 組回去**：拆完要證實拆對了，就要組回去。$W$ 想用 $E$ 組回原來的 $X$。
- **結果組不回來**：少一個東西，跟原來不相等。這就是 $X_p$——沒辦法用 $E$ 合成的**額外部分**。

**歷史上很多重要定理都在做拆解**【口頭】：
- Lebesgue：任何分布可以拆成三塊——absolutely continuous、（連續的）singular、離散的。
- 任何 stationary 過程可以拆成 stationary ergodic 過程的線性組合。
- 拆解定理都很重要，因為對分析非常有用。

**怎麼用**：以後分析一個對象，先拆解——能不能拆到最小最小的基本單元（像 i.i.d.）？拆完再合成回來，合不回來就表示裡面有你沒拆到的東西。老師說：數學家沒什麼特別，就是多思考；這樣你可以創造自己的定理（姓陳就叫 Chen Theorem，姓林就叫 Lin Theorem）。

---

## 2. $X_p$ 是什麼：駐波

[▶ 05:09](https://youtu.be/Nc2B7DowucE?t=309) 回顧最簡單的 AR 範例 $\frac{b}{1-az^{-1}}$，$b=0$（沒有輸入）：

| $a$ | 行為 |
|---|---|
| $a=1$ | $X[t]=X[t-1]$，值停在那裡不動 |
| $a=e^{j\omega_i}$（單位圓上） | $X[t]=e^{j\omega_i}X[t-1]$：能量沒損失，只是旋轉（例如每步轉 30°，轉 12 次回原狀）——像**駐波**，永遠存在、一直共振重複 |
| $\lvert a\rvert>1$（例如 2） | 一直乘 2，爆掉（overflow），不穩 |
| $\lvert a\rvert<1$（例如 $\frac12$） | 指數遞減，一下子消失 |

只有**根在單位圓上**的狀態會留下來。$X_p$ 就是所有這種駐波（一倍、兩倍、三倍……）——能量一直停在那裡，**躲在裡面、沒辦法合成**。老師說用這個方式理解就不用背了。

---

## 3. 更強的結論：$X_p$ 和所有誤差正交

[▶ 08:47](https://youtu.be/Nc2B7DowucE?t=527) 上一集只用到 $X_p[t]$ 和 $E[t],E[t-1],\dots$（現在和過去）正交。其實可以寫得更強：

> $$E\{X_p[t]E^*[t+k]\}=0\quad\text{對所有整數 }k.$$
> 剩下的部分和用來合成的最小單元**完全正交**——過去、現在、未來都是。

**證明**：
$$X_p[t]=X[t]-X_r[t]=X[t]-\sum_{k\ge0}w_kE[t-k],\qquad E[t-k]=X[t-k]-\sum_{n\ge1}a_nX[t-k-n].$$
所以 $X_p[t]$ 是 $X[t],X[t-1],X[t-2],\dots$（現在加所有過去的觀察）的線性組合。

$E[t+1]$ 是用 $X[t],X[t-1],\dots$ 預測 $X[t+1]$ 剩下的部分 ⇒ 和這整塊正交（線性預測的結果）。$X_p[t]$ 是這塊的線性組合 ⇒ $E[t+1]\perp X_p[t]$。$E[t+2],E[t+3],\dots$ 同理。∎

老師說：這個拆解相當漂亮，是經典的結果；重要的是真的理解它背後的思維，將來才能借鏡。

---

## 4. 證明的兩個缺口

[▶ 14:10](https://youtu.be/Nc2B7DowucE?t=850) 這個證明的本體其實在第 13 章，老師拿到第 11 章先講，因為剛學完 regular 和 predictable 過程，比較整體。

1. **正交原理** (orthogonality principle) 直接拿來用、沒證明（線性預測剩下的部分和資料正交）。第 13 章說明。
2. **Stable**：結論寫 $X_r$ 是白雜訊經過 causal（stable）濾波器，stable 是**加括號**的——有用意。
   - causal 沒問題：$k$ 從 0 開始，脈衝響應在過去是 0。
   - stable 沒證（至少要絕對值和有限）。第 13 章稍微提到：如果過程的**功率有限**，線性預測的係數不會爆掉，所以 $W$ 也 stable。
   - 所以 Wold 定理的敘述可能也要加：過程不是任意的，要能量有限。但一般不會特別講，因為大家不關心能量無限大的過程。

---

## 5. 頻譜：把脈衝抽出來

[▶ 16:43](https://youtu.be/Nc2B7DowucE?t=1003)
- $X_r$：拆到最細的螺絲再組回來的東西——用線性組合可以合成，也是實作做得出來的。
- $X_p$：合成不出來、剩下的部分。

兩者完全正交，所以功率頻譜直接疊加：
$$S(\omega)=S_r(\omega)+S_p(\omega)\qquad\text{(11-94)}.$$
- $S_p$ 是**線譜**（很多脈衝）。Wold 分解在頻譜上做的事就是：**把脈衝提出來**。
- 實作上做不出單一脈衝的東西，很合理；但理論上有，也可能線路裡剛好形成駐波迴路就會產生。
- $S_r$ 可以做 factorization（開根號），濾波器是 minimum phase（第 22 集）。

【課本補充】p. 518：$S_p(\omega)=2\pi k_0\delta(\omega)+2\pi\sum_ik_i\delta(\omega-\omega_i)$（式 (11-95)），原點的脈衝是 $2\pi(k_0+\eta^2)\delta(\omega)$。$X_p(t)=c_0+\sum_ic_ie^{j\omega_it}$，$E\{c_ic_j^*\}=k_i\delta[i-j]$（式 (11-90)、(11-93)）。

---

## 6. Example 11-12

[▶ 18:15](https://youtu.be/Nc2B7DowucE?t=1095)

> **Example 11-12**：$Y(t)=aX(t)$，$a$ 是隨機變數、$E\{a\}=0$；$X$ 是 regular（可以拆成 i.i.d. 的組合），$X$ 和 $a$ 獨立。求 $Y$ 的 Wold 分解。

**為什麼前面講頻譜**：從頻譜看比較直觀——predictable 部分是線譜。

**Step 1：自相關和頻譜。**
$$E\{Y(t)\}=0,\qquad R_{YY}(\tau)=E\{a^2\}R_{XX}(\tau)=\sigma_a^2R_{XX}(\tau).$$
沒有假設 $X$ 零平均，所以 $S_{XX}=S^c_{XX}+2\pi\eta_X^2\delta(\omega)$（原點有 DC 脈衝）：
$$S_{YY}(\omega)=\sigma_a^2S^c_{XX}(\omega)+2\pi\sigma_a^2\eta_X^2\delta(\omega).$$

**Step 2：把脈衝抽出來。** 脈衝是駐波，能量卡在那裡（DC stuck）；沒有脈衝的部分就是可以開根號的 regular 過程。【口頭】delta 是人為定義的函數，delta 開根號沒有定義，所以本來就沒有對它開根號這件事，要先抽出來。

$$Y_p(t)=\eta_Xa,\qquad Y_r(t)=a\left[X(t)-\eta_X\right].$$

**驗證**：
- $Y_p$ 確實 predictable：$a$ 只丟一次（例如丟骰子丟出 3 點就永遠是 3 點），不隨時間改變；過去告訴我是 3 點，下個時間還是 3 點，百分之百預測。
- 頻譜也對、兩者也真的正交。

（上一集提到：這個拆解並沒有照證明裡的做法取係數，但不違反定理，因為定理沒說唯一。）

---

## 7. 離散時間過程的頻譜表示

[▶ 21:23](https://youtu.be/Nc2B7DowucE?t=1283)

$$X(\omega)=\sum_nX[n]e^{-jn\omega}\qquad\text{(11-96)},\qquad X[n]=\frac1{2\pi}\int_{-\pi}^{\pi}X(\omega)e^{jn\omega}d\omega\qquad\text{(11-97)}.$$
離散的頻譜一定是週期 $2\pi$ 的。不一定 WSS 時做二維轉換 $\Gamma(u_1,u_2)$；同樣有**時域自相關 ⇔ 頻域功率頻譜**、**時域功率頻譜 ⇔ 頻域自相關**，差一個負號（因為共軛）。老師說證明很簡單，不用背，要用再查。

> **WSS ⇒ DFT 是非平穩白**：
> $$E\{X(u)X^*(v)\}=2\pi S(u)\delta(u-v),\quad-\pi<u,v<\pi\qquad\text{(11-98)}.$$

**為什麼有用**【口頭】：現在做 data analytics、machine learning、big data，一般至少要假設分析的對象是穩態的；但時域穩不穩態不見得看得出來。所以乾脆把資料送到頻譜上——若穩態，頻域是非平穩白：$u\ne v$ 時能量干擾完全是 0，不同頻率的值可能不一樣。

**例**（數位通訊的 fading channel）：uncorrelated scattering——打一個電波收到三個（delay 10、12、14 ns），強度不同。不同路徑能量上不相關 → $\delta(\tau_1-\tau_2)$，但值有強有弱 → **非平穩白**。轉到另一個 domain 就是 WSS（if and only if）。

【課本補充】p. 519 證明：用 $\sum_ne^{-jn\omega}=2\pi\delta(\omega)$（$|\omega|<\pi$），
$$E\{X(u)X^*(v)\}=\sum_n\sum_mR[m]e^{-j[(m+n)u-nv]}=\sum_ne^{-jn(u-v)}\sum_mR[m]e^{-jmu}.$$

---

## 8. 雙頻譜 (bispectrum)

[▶ 26:01](https://youtu.be/Nc2B7DowucE?t=1561) 老師在一些碩士口試場合看過有老師做三階動差分析，所以要告訴大家什麼時候三階分析是必要的、有幫助的。

### 8.1 定義

**三階動差**：看三個時間彼此的關係：
$$R(u,v)=E\{X(t+u)X(t+v)X^*(t)\}.$$
- 只有最後一個加共軛。為什麼不是最後兩個？那是同一件事——整個取共軛就變成兩個有、一個沒有，只是反向。但不能都不取。
- **要求跟 $t$ 無關**：參數只有 $u$、$v$（前兩個和最後一個的時間差）。若隨時間改變，就對時間平均（time-average bispectrum）。

**雙頻譜** = 二維傅立葉轉換（兩個參數，所以叫 bi-spectrum）：
$$S(u,v)=\iint R(\mu,\nu)e^{-j(u\mu+v\nu)}d\mu\,d\nu.$$

**什麼時候三階動差不隨時間改變**：WSS 只保證一、二階。可以延伸定義「一、二、三階都不隨時間改變」的過程，但應用不廣，沒人特別定義。**SSS** 保證（所有階都不變，但是很強的假設）。

### 8.2 為什麼要三階：系統相位

[▶ 29:08](https://youtu.be/Nc2B7DowucE?t=1748) 例【口頭】：腦波測試，相位非常重要。我們只看得到輸入、輸出，要知道中間的黑盒子（電波、聲波進入身體出來，分析肝、胃、腦的狀態）。

- **只測二階**：只知道 $|H(\omega)|^2$（magnitude response），**不知道相位**。
- 有些應用系統的相位非常重要（牽涉到 delay 等細節）。

> **線性系統的雙頻譜**：
> $$S_{YY}(\omega_1,\omega_2)=S_{XX}(\omega_1,\omega_2)\,H(\omega_1)H(\omega_2)H^*(\omega_1+\omega_2).$$
> 不只跟 $|H|$ 有關——**三階可以量到系統的相位**。二階、三階都知道了，就不需要測到四階。

**推導**（老師說很簡單，步驟上課講過好幾次）：照定義寫輸出的三階動差，是三個卷積；積分和期望值一直對調（先做期望值）；五個積分，做變數變換 $u',v'$；$\tau_3$ 的積分會得到 $\omega_1+\omega_2$；一個一個積出來。

出處：課本 §10-7 Bispectra and System Identification，式 (10-251)（課程跳過第 10 章大部分，這裡拿來用）。

### 8.3 用白雜訊量測相位

[▶ 32:09](https://youtu.be/Nc2B7DowucE?t=1929) 老師說這個範例比較重要。

**輸入**：SSS 的白過程，三階的「白」：$R(u,v)=Q\delta(u)\delta(v)$，雙頻譜是二維平面上高度 $Q$ 的常數（所有頻率都有，所以叫白）。一般做系統測試就是這樣：丟一個雜訊進你的肚子，後面用 sensor 看穿過身體後電波變成什麼樣子（uniform，面面俱到看所有可能性）。

**輸出**：
$$S_{YY}(\omega_1,\omega_2)=Q\,H(\omega_1)H(\omega_2)H^*(\omega_1+\omega_2).$$

**看角度**：$|H|$ 二階已經知道，想知道每個頻率轉了幾度（高頻轉比較多還是低頻？可能代表不同的病變）。寫 $H(\omega)=|H(\omega)|e^{j\varphi(\omega)}$，乘法變成角度相加、共軛變成相減：
$$\theta(\omega_1,\omega_2)=\varphi(\omega_1)+\varphi(\omega_2)-\varphi(\omega_1+\omega_2),$$
$\theta$ 是量到的輸出雙頻譜的角度。

**解 $\varphi$：先微分。** 對 $\omega_2$ 偏微分，再代 $\omega_2=0$：
- $\varphi(\omega_1)$ 那項不見了。
- $\varphi(\omega_2)$ 那項變成 $\varphi'(0)$。
- $\varphi(\omega_1+\omega_2)$ 對 $\omega_2$ 偏微分就是原函數微分，代 $\omega_2=0$ 得 $\varphi'(\omega_1)$。
$$\frac{\partial\theta}{\partial\omega_2}(\omega_1,0)=\varphi'(0)-\varphi'(\omega_1)\ \Rightarrow\ \varphi'(\omega_1)=\varphi'(0)-\frac{\partial\theta}{\partial\omega_2}(\omega_1,0).$$
**再積分回來**（$0$ 到 $\omega$）：
$$\varphi(\omega)=\varphi(0)+\varphi'(0)\,\omega-\int_0^{\omega}\frac{\partial\theta}{\partial\omega_2}(\omega_1,0)\,d\omega_1.$$
不用量很多地方，只要量**原點附近**的偏微分。這是一般常用的量測系統相位變化的方式。

**實數系統** [▶ 37:49](https://youtu.be/Nc2B7DowucE?t=2269)：$h(\tau)$ 是實數 ⇒ 頻譜共軛對稱 ⇒ $\varphi(0)=0$（原點沒有旋轉），這項可以拿掉。但原點的微分 $\varphi'(0)$ 不見得是 0，那個值不能省略。

> ⚠️ 兩邊說法不同：老師說 $\varphi'(0)$ 不能省略；課本 §10-7（式 (10-257)–(10-259)，pp. 490–491）說相位**只能決定到差一個線性項**——若 $\varphi(\omega)$ 滿足 (10-257)，$\varphi(\omega)+c\omega$ 也滿足（線性項在 $\theta$ 裡互相抵消），所以可以**假設** $\varphi'(0)=0$，得 $\varphi(\omega)=-\int_0^\omega\theta_v(u,0)\,du$。兩者不矛盾：$\varphi'(0)$ 從雙頻譜量不到（對應純延遲），課本選擇設為 0。

【課本補充】§10-7：振幅也能從雙頻譜求：$B(u,v)=QA(u)A(v)A(u+v)$，代 $v=0$ 得 $QA^2(\omega)=B(\omega,0)/A(0)$（式 (10-258)），只能決定到差一個常數倍。數值上用 $\varphi(n\Delta)\approx-\sum_{k=1}^{n}\theta(k\Delta,\Delta)$（式 (10-260)）。若系統是 minimum phase，二階就能決定相位（第 22 集）。

### 8.4 SSS 過程的雙頻譜在頻域

[▶ 38:21](https://youtu.be/Nc2B7DowucE?t=2301) 類比「WSS ⇒ 頻域非平穩白」：

> **Theorem 11-4**：$X$ 是實數 SSS，則
> $$E\{X(u)X(v)X^*(w)\}=2\pi S(u,v)\,\delta(u+v-w)\qquad\text{(11-99)}.$$

- 三維傅立葉轉換只在平面 $u+v=w$ 上才有值（「非平穩白」的三階版本），每個值不一樣。
- 證明：最基本的傅立葉轉換，令 $t_1=t_3+\mu$、$t_2=t_3+\nu$，最後一個積分 $\int e^{-j(u+v-w)t_3}dt_3=2\pi\delta(u+v-w)$。

【課本補充】pp. 520–521：Theorem 11-5：$Z(\omega)$ 的增量的三階動差 $=2\pi\iint_RS(u,v)\,du\,dv$，$R$ 是三個區域 $\omega_1<u<\omega_2$、$\omega_3<v<\omega_4$、$\omega_5<u+v<\omega_6$ 的交集（式 (11-101)）；推論 $E\{dZ(u_0)dZ(v_0)dZ^*(w_0)\}=2\pi S(u_0,v_0)du\,dv$（$w_0=u_0+v_0$，否則 0），可以用來以 $Z(\omega)$ 定義 SSS 過程的雙頻譜（式 (11-102)）。

老師說這個主題只是介紹觀念，讓大家知道有這樣的東西，好像沒有特別需要考。

---

## 9. 一頁速查表

### Wold 分解（回顧＋補充）

- $A$：拆解，$X\to E$（最小單元、白）；$W$：組合，$E\to X_r$；組不回來的是 $X_p$（駐波，根在單位圓上）。
- $X_p[t]$ 是 $X[t],X[t-1],\dots$ 的組合 ⇒ 和**所有** $E[t+k]$ 正交。
- 缺口：正交原理（第 13 章）、$W$ stable（功率有限時）。
- $S=S_r+S_p$，$S_p$ 是線譜（把脈衝抽出來）。
- Example 11-12：$Y=aX$ ⇒ $Y_p=\eta_Xa$，$Y_r=a(X-\eta_X)$。

### 離散

WSS ⇒ $E\{X(u)X^*(v)\}=2\pi S(u)\delta(u-v)$，$\lvert u\rvert,\lvert v\rvert<\pi$。

### 雙頻譜

| 項目 | 公式 |
|---|---|
| 三階動差 | $R(u,v)=E\{X(t+u)X(t+v)X^*(t)\}$ |
| 線性系統 | $S_{YY}=S_{XX}H(\omega_1)H(\omega_2)H^*(\omega_1+\omega_2)$ |
| 相位 | $\theta=\varphi(\omega_1)+\varphi(\omega_2)-\varphi(\omega_1+\omega_2)$ |
| 解相位 | $\varphi(\omega)=\varphi(0)+\varphi'(0)\omega-\int_0^\omega\partial_{\omega_2}\theta(\omega_1,0)d\omega_1$ |
| SSS 頻域 | $E\{X(u)X(v)X^*(w)\}=2\pi S(u,v)\delta(u+v-w)$ |

- 關鍵一步：對 $\omega_2$ 偏微分再代 0，讓 $\varphi(\omega_1)$ 消失、$\varphi(\omega_1+\omega_2)$ 變 $\varphi'(\omega_1)$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 正交原理、Wold 的證明本體 | §13-1、13-2（第 37–40 集） |
| WSS 頻域白、DFT | 第 12 章頻譜估計（第 34–36 集） |
| 拆解成 ergodic 的線性組合 | 第 30 集：ergodicity |

---

## 附：本集一句話總結

> **Wold 分解就是先用最佳線性預測把 WSS 過程拆成最小的白色誤差，再用它組回去——組得回來的是 regular 部分，組不回來的是根在單位圓上的駐波（predictable、線譜），而且它和所有過去現在未來的誤差都正交；三階的雙頻譜 $H(\omega_1)H(\omega_2)H^*(\omega_1+\omega_2)$ 能量到二階量不到的系統相位。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-4 (2/2) 錄影逐字稿（whisper large-v3-turbo，39:55）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
