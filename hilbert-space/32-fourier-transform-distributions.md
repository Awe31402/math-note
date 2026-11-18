---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 32
lecture: Lecture 32
date: 2023-04-21
video: https://youtu.be/rmz3GsOaE-Y （part 1）、https://youtu.be/pQr5xMlUnmI （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.12（書頁 271–273，PDF 頁 290–292）、§6.1–6.2（書頁 287–299，PDF 頁 306–318）
---

# 第 32 集 · 用 Fourier 變換解微分方程、分佈理論概覽 [▶ 影片](https://youtu.be/rmz3GsOaE-Y)

← 上一集：[31-greens-function-fourier-transform](31-greens-function-fourier-transform.md) ｜ [總目錄](README.md) ｜ 下一集：[33-classical-quantum-mechanics](33-classical-quantum-mechanics.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 32 集
> **講者**：James Cook（⚠️ 待確認，見第 01 集）
> **來源**：YouTube 自動字幕逐字稿（part 1 約 59:40；part 2 約 36:20）＋ Debnath & Mikusiński §5.12、§6.1–6.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 常係數 ODE 的 Fourier 解法](#1-常係數-ode-的-fourier-解法)
- [2. 單位脈衝與 Green 函數](#2-單位脈衝與-green-函數)
- [3. 例：RL 電路（留數定理）](#3-例rl-電路留數定理)
- [4. 第 6 章開場：為什麼需要分佈](#4-第-6-章開場為什麼需要分佈)
- [5. 弱形式：乘上 φ、分部積分](#5-弱形式乘上-φ分部積分)
- [6. 測試函數](#6-測試函數)
- [7. 測試函數的收斂](#7-測試函數的收斂)
- [8. 分佈的定義；正則與奇異分佈](#8-分佈的定義正則與奇異分佈)
- [9. 例：Heaviside 函數、Dirac δ](#9-例heaviside-函數dirac-δ)
- [10. 分佈的導數](#10-分佈的導數)
- [11. 【口頭】階梯函數的導數是 δ](#11-口頭階梯函數的導數是-δ)
- [12. 第 6 章其餘部分（只翻過）](#12-第-6-章其餘部分只翻過)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者的目標：讓大家「對分佈（distribution）是什麼、怎麼運作有點感覺」。開始前先補一個 Fourier 變換的計算（§5.12），因為它接著上次的內容。[▶ 00:33](https://youtu.be/rmz3GsOaE-Y?t=33)

| 主題 | 課本位置 |
|---|---|
| Fourier 變換解 ODE、admittance、Green 函數 | §5.12 開頭，(5.96)–(5.102)，pp. 271–272 |
| RL 電路 | Example 5.12.1，pp. 272–273 |
| 弱形式、測試函數 | §6.2 (6.1)–(6.7)、Definition 6.2.1 – Theorem 6.2.3，pp. 288–290 |
| 收斂、分佈、正則／奇異 | Definition 6.2.4 – Definition 6.2.8，pp. 290–292 |
| Heaviside、δ、分佈導數 | Example 6.2.9 – Example 6.2.14，pp. 292–294 |

---

## 1. 常係數 ODE 的 Fourier 解法

[▶ 01:05](https://youtu.be/rmz3GsOaE-Y?t=65)

**問題**：$n$ 階常係數線性 ODE
$$Ly(t)=f(t),\qquad L=a_nD^n+a_{n-1}D^{n-1}+\cdots+a_1D+a_0,\quad D=\frac{d}{dt}.$$

**第 1 步：兩邊做 Fourier 變換。** 上一集的 $\mathcal F\{y^{(k)}\}=(i\omega)^k\hat y$ 把每個 $D$ 換成 $i\omega$：[▶ 02:17](https://youtu.be/rmz3GsOaE-Y?t=137)
$$\left(a_n(i\omega)^n+a_{n-1}(i\omega)^{n-1}+\cdots+a_1(i\omega)+a_0\right)\hat y(\omega)=\hat f(\omega).$$

令多項式 $\hat p(z)=a_nz^n+\cdots+a_1z+a_0$，這就是
$$\hat p(i\omega)\,\hat y(\omega)=\hat f(\omega).$$

**第 2 步：代數地解出 $\hat y$。** 微分方程變成了除法：
$$\hat y(\omega)=\frac{\hat f(\omega)}{\hat p(i\omega)}=\hat f(\omega)\,\hat g(\omega),\qquad \hat g(\omega)=\frac1{\hat p(i\omega)}.$$

【口頭】講者吐槽作者「凡是 $\omega$ 的函數都戴帽子」，連 $\hat p$ 都戴。[▶ 03:30](https://youtu.be/rmz3GsOaE-Y?t=210)

**第 3 步：反變換。** 由摺積定理（$\mathcal F(f*g)=\hat f\hat g$）：[▶ 04:34](https://youtu.be/rmz3GsOaE-Y?t=274)
$$y(t)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(\xi)\,g(t-\xi)\,d\xi,\qquad g=\mathcal F^{-1}\{\hat g\}.$$

---

## 2. 單位脈衝與 Green 函數

[▶ 05:41](https://youtu.be/rmz3GsOaE-Y?t=341)

講者說：這個形式讓人想起 Green 函數。看右邊是 Dirac δ 的方程
$$LG(t)=\delta(t).$$

**δ 的 Fourier 變換**：【口頭】「Dirac δ 是個美妙的東西：它把積分變成取值。」[▶ 07:00](https://youtu.be/rmz3GsOaE-Y?t=420)
$$\hat\delta(\omega)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-i\omega t}\delta(t)\,dt=\frac1{\sqrt{2\pi}}e^{-i\omega\cdot0}=\frac1{\sqrt{2\pi}} .$$

所以變換後 $\hat p(i\omega)\hat G(\omega)=\frac1{\sqrt{2\pi}}$，即
$$\hat G(\omega)=\frac1{\sqrt{2\pi}}\hat g(\omega),\qquad G(t)=\frac1{\sqrt{2\pi}}g(t).$$

把 $\frac1{\sqrt{2\pi}}$ 吸進 $G$，解就寫成[▶ 09:23](https://youtu.be/rmz3GsOaE-Y?t=563)
$$y(t)=\int_{-\infty}^{\infty}f(\xi)\,G(t-\xi)\,d\xi .\tag{5.102}$$

**結論**：Green 函數就是「強迫項是單位脈衝」時方程的解。

【課本補充】物理用語：$f$ 叫輸入（input），$y$ 叫輸出（output）。$\hat g(\omega)=\left(\hat p(i\omega)\right)^{-1}$（即 $\sqrt{2\pi}G$ 的 Fourier 變換）叫 **admittance**。求響應的步驟：輸入做 Fourier 變換 → 乘 admittance → 反變換。（講者唸到這裡時說「他還沒給它名字」，其實課本在下一段就給了。）

**【口頭】為什麼叫「單位脈衝」？**[▶ 10:34](https://youtu.be/rmz3GsOaE-Y?t=634) 名字來自物理。牛頓第二定律寫成 $\frac{dp}{dt}=F_{\text{net}}$，積分得
$$\Delta p=\int_{t_1}^{t_2}F_{\text{net}}\,dt ,$$
力–時間圖下的面積叫**衝量**（impulse，常記 $J$）。若力是 $t_3$ 時刻的 δ，則積分在 $t_3\in[t_1,t_2]$ 時是 1，否則是 0：一個瞬間、面積為 1 的衝擊——所以叫「單位」脈衝。

---

## 3. 例：RL 電路（留數定理）

[▶ 12:48](https://youtu.be/rmz3GsOaE-Y?t=768)

**Example 5.12.1**：電流 $I(t)$ 滿足
$$L\frac{dI}{dt}+RI=E,\qquad E(t)=E_0e^{-|t|}.$$
$L$ 是電感、$R$ 是電阻、$E$ 是外加「電動勢」。這就是 RL 電路的 Kirchhoff 電壓定律。

【口頭】講者說「electromotive force」這個名字很討厭：它其實是電壓（單位電荷的位能），不是力。[▶ 14:02](https://youtu.be/rmz3GsOaE-Y?t=842)

**第 1 步：變換。** 用 $\mathcal F\{I'\}=i\omega\hat I$，以及上次算的 $\mathcal F\{e^{-|t|}\}=\sqrt{\frac2\pi}\frac1{1+\omega^2}$（$\alpha=1$）：[▶ 16:02](https://youtu.be/rmz3GsOaE-Y?t=962)
$$(i\omega L+R)\,\hat I(\omega)=\sqrt{\frac2\pi}\,\frac{E_0}{1+\omega^2}
\quad\Longrightarrow\quad
\hat I(\omega)=\sqrt{\frac2\pi}\,\frac{E_0}{(i\omega L+R)(1+\omega^2)} .$$

【口頭】「好的電機工程師會直接查反變換表，什麼都不算；我們要守規矩自己算。」[▶ 18:29](https://youtu.be/rmz3GsOaE-Y?t=1109)

**第 2 步：反變換。** 乘上 $\frac1{\sqrt{2\pi}}$：$\frac1{\sqrt{2\pi}}\sqrt{\frac2\pi}=\frac1\pi$。[▶ 19:23](https://youtu.be/rmz3GsOaE-Y?t=1163)
$$I(t)=\frac{E_0}{\pi}\int_{-\infty}^{\infty}\frac{e^{i\omega t}}{(i\omega L+R)(1+\omega^2)}\,d\omega .$$

**第 3 步：看成複變函數，找極點。**[▶ 20:31](https://youtu.be/rmz3GsOaE-Y?t=1231)
$$F(z)=\frac{e^{izt}}{(izL+R)(1+z^2)}=\frac{e^{izt}}{iL\left(z-\frac{iR}{L}\right)(z-i)(z+i)} .$$
極點在 $z=i$、$z=-i$、$z=\frac{iR}{L}$。其中 $i$ 和 $\frac{iR}{L}$ 在上半平面。

**第 4 步：$t>0$，用上半圓圍道。**[▶ 22:29](https://youtu.be/rmz3GsOaE-Y?t=1349) 半徑夠大時兩個上半平面極點都被圍住；分母是三次、分子 $|e^{izt}|\le1$，所以外圈半圓上的積分趨於 0（講者說用 ML 不等式「相當明顯」）。由留數定理：
$$I(t)=\frac{E_0}{\pi}\cdot2\pi i\left[\operatorname{Res}_{z=i}F+\operatorname{Res}_{z=iR/L}F\right].$$

**第 5 步：算留數。**（課堂上講者邊算邊修正，下面是課本 p. 273 的整理。）[▶ 24:14](https://youtu.be/rmz3GsOaE-Y?t=1454)

- 在 $z=i$：$i\cdot i\cdot L+R=R-L$，$z+i=2i$，所以
$$\operatorname{Res}_{z=i}F=\frac{e^{-t}}{2i(R-L)} .$$
- 在 $z=\frac{iR}{L}$：要先把 $izL+R$ 寫成 $iL\left(z-\frac{iR}L\right)$（講者特別提醒這一步）；$1+z^2=1-\frac{R^2}{L^2}$，$e^{izt}=e^{-Rt/L}$，所以
$$\operatorname{Res}_{z=iR/L}F=\frac{e^{-Rt/L}}{iL\left(1-R^2/L^2\right)} .$$

**第 6 步：合起來。**
$$I(t)=2iE_0\left[\frac{e^{-t}}{2i(R-L)}+\frac{e^{-Rt/L}}{iL(1-R^2/L^2)}\right]
=E_0\left(\frac{e^{-t}}{R-L}-\frac{2L\,e^{-Rt/L}}{R^2-L^2}\right),\qquad t>0 .$$
（最後一步用 $L\left(1-\frac{R^2}{L^2}\right)=\frac{L^2-R^2}{L}$，即上下同乘 $L$。這裡假設 $R\ne L$。）[▶ 27:36](https://youtu.be/rmz3GsOaE-Y?t=1656)

**為什麼要 $t>0$？**[▶ 28:54](https://youtu.be/rmz3GsOaE-Y?t=1734) 在上半平面 $z=iy$（$y>0$），$e^{izt}=e^{-yt}$。$t>0$ 時有界；$t<0$ 時它會爆掉，上半圓圍道不能用。

**$t<0$**：改用下半圓圍道，只圍到 $z=-i$（順時針，多一個負號）：[▶ 29:28](https://youtu.be/rmz3GsOaE-Y?t=1768)
$$I(t)=-\frac{E_0}{\pi}\cdot2\pi i\operatorname{Res}_{z=-i}F=\frac{E_0\,e^{t}}{L+R},\qquad t<0 .$$
【口頭】講者說可以看出為什麼：另外兩個極點根本不在下半平面的圍道裡。

**$t=0$**：電流連續，所以 $I(0)=\lim_{t\to0^-}I(t)=\frac{E_0}{R+L}$。[▶ 30:49](https://youtu.be/rmz3GsOaE-Y?t=1849) 講者說從 $t>0$ 那邊取極限應該也得到同樣的值，「雖然不是一眼就看得出來」。

以下**不是逐字稿內容**，是依上面的 $t>0$ 公式推論的：令 $t\to0^+$，
$$E_0\left(\frac1{R-L}-\frac{2L}{R^2-L^2}\right)=E_0\,\frac{(R+L)-2L}{(R-L)(R+L)}=E_0\,\frac{R-L}{(R-L)(R+L)}=\frac{E_0}{R+L} ,$$
兩邊確實一致。

【口頭】課本還有十幾、二十個用 Fourier 變換解微分方程的例子，講者沒時間做。他說如果能常教進階微分方程，才會熟到不用看書就能教。[▶ 31:21](https://youtu.be/rmz3GsOaE-Y?t=1881)

---

## 4. 第 6 章開場：為什麼需要分佈

[▶ 33:00](https://youtu.be/rmz3GsOaE-Y?t=1980)

講者唸了第 6 章開頭的兩段引文：

- **Poincaré**：「無論人的想像多麼豐富，自然還要豐富一千倍。……沒有這些物理理論，我們就不會認識偏微分方程。」講者的解讀：物理逼我們去看那些光為了數學本身大概不會去看的 PDE。
- **Dieudonné**：1930–1940 年間，數學家開始系統研究線性 PDE 的「弱解」（weak solution）；Laurent Schwartz 在 1945 年看出 Sobolev 引入（他自己又獨立重新發現）的「分佈」概念，可以給出 Fourier 變換的令人滿意的推廣。

【口頭】講者說「分佈是 Fourier 變換的推廣」這句話他自己還沒完全懂，但覺得很有意思。分佈理論由 Sobolev（1936）和 Schwartz（1940–50 年代）發展，所以也叫 **Schwartz 分佈**。[▶ 35:13](https://youtu.be/rmz3GsOaE-Y?t=2113)

---

## 5. 弱形式：乘上 φ、分部積分

[▶ 35:46](https://youtu.be/rmz3GsOaE-Y?t=2146)

**設定**：$N$ 個變數、$m$ 階、常係數的偏微分算子
$$L=\sum_{|\alpha|\le m}a_\alpha D^\alpha,\qquad D^\alpha=\frac{\partial^{|\alpha|}}{\partial x_1^{\alpha_1}\cdots\partial x_N^{\alpha_N}} .$$
這裡 $\alpha=(\alpha_1,\dots,\alpha_N)$ 是**多重指標**（multi-index），$|\alpha|=\alpha_1+\cdots+\alpha_N$。方程是
$$Lu=\sum_{|\alpha|\le m}a_\alpha D^\alpha u=f .\tag{6.2}$$

課本說：這個方程只有在 $u$ 的那些導數都存在時才有意義，這對解是很嚴的限制，而且常常根本沒有這樣的解。[▶ 37:31](https://youtu.be/rmz3GsOaE-Y?t=2251)

**第 1 步：乘上 $\varphi$。** 取 $\varphi$ 無窮可微，且在某個有界集合之外為 0。（講者一開始口誤說成「在有界集合外不為 0」，馬上更正。）[▶ 38:06](https://youtu.be/rmz3GsOaE-Y?t=2286)

**第 2 步：在 $\mathbb R^N$ 上積分。**
$$\int_{\mathbb R^N}\left(\sum_{|\alpha|\le m}a_\alpha D^\alpha u(x)\right)\varphi(x)\,dx=\int_{\mathbb R^N}f(x)\varphi(x)\,dx .$$

【口頭】講者說他早上剛在微積分二教 Fourier 級數：在展開式兩邊乘上 $\sin$ 再積分。這裡的手法很像。[▶ 39:17](https://youtu.be/rmz3GsOaE-Y?t=2357)

**第 3 步：分部積分。** 因為 $\varphi$ 在有界集合外為 0，邊界項全部消失。每把一個導數從 $u$ 搬到 $\varphi$ 就多一個負號，$D^\alpha$ 搬過去就是 $(-1)^{|\alpha|}$：[▶ 40:30](https://youtu.be/rmz3GsOaE-Y?t=2430)
$$\int_{\mathbb R^N}u(x)\left(\sum_{|\alpha|\le m}(-1)^{|\alpha|}a_\alpha D^\alpha\varphi(x)\right)dx=\int_{\mathbb R^N}f(x)\varphi(x)\,dx .$$
（講者提醒這用到多變數的分部積分，「本身就會引出一些問題」。）

**第 4 步：記 $L^*$。**
$$L^*=\sum_{|\alpha|\le m}(-1)^{|\alpha|}a_\alpha D^\alpha,\qquad \int_{\mathbb R^N}u\,(L^*\varphi)\,dx=\int_{\mathbb R^N}f\varphi\,dx .\tag{6.7}$$

**重點**：[▶ 43:58](https://youtu.be/rmz3GsOaE-Y?t=2638)
- (6.2) 的解一定是 (6.7) 的解。
- 但 $u$ 可以滿足 (6.7) 而**不可微**。所以 (6.7) 的解集合比較大。
- 這是「廣義函數」理論的基本想法。

**用積分來比較函數**：[▶ 44:34](https://youtu.be/rmz3GsOaE-Y?t=2674) 設 $f,g$ 在 $\mathbb R^N$ 上連續。若對每個「光滑、在有界集合外為 0」的 $\varphi$ 都有
$$\int f\varphi=\int g\varphi ,$$
則 $f(x)=g(x)$ 對每個 $x$ 成立。【口頭】講者說課本把這句寫「反過來」（先寫結論再寫條件），像 ε–δ 的寫法。不是逐點比較數值，而是拿光滑函數去「測試」$f$ 和 $g$，所以這些 $\varphi$ 叫**測試函數**。

以下**不是逐字稿內容**，是依連續性推論的：證明想法——令 $h=f-g$，若 $h(x_0)\ne0$（例如 $\operatorname{Re}h(x_0)>0$），由連續性 $\operatorname{Re}h>0$ 在 $x_0$ 附近一個小球上成立；取一個只在這個小球內為正的測試函數 $\varphi\ge0$（例如第 6 節的鐘形函數平移縮放），就得到 $\operatorname{Re}\int h\varphi>0$，矛盾。

---

## 6. 測試函數

[▶ 47:05](https://youtu.be/rmz3GsOaE-Y?t=2825)

**Definition 6.2.1**：**測試函數**（test function）是 $\mathbb R^N$ 上無窮可微、在某個有界集合外為 0 的函數。全體記為 $\mathcal D(\mathbb R^N)$ 或 $\mathcal D$。「無窮可微」常說成「光滑」（smooth）。

【口頭】講者想了一下為什麼課本說「有界」而不說「緊支撐」：「緊緻需要閉且有界，他沒說閉。」

以下**不是逐字稿內容**，是依支撐集的定義推論的：兩者其實等價。支撐集通常定義成 $\{x:\varphi(x)\ne0\}$ 的**閉包**，它一定是閉集；若 $\varphi$ 在有界集 $B$ 外為 0，支撐集就包含在 $\overline B$ 裡，也有界，所以是緊緻的。

**Example 6.2.2（鐘形函數）**：$N=1$ 時，[▶ 49:45](https://youtu.be/rmz3GsOaE-Y?t=2985)
$$\varphi(x)=\begin{cases}\exp\left(\dfrac1{x^2-1}\right),&|x|<1\\[4pt]0,&|x|\ge1\end{cases}$$

講者在黑板上分析指數裡的 $\frac1{x^2-1}$。先拆部分分式：[▶ 50:56](https://youtu.be/rmz3GsOaE-Y?t=3056)
$$\frac1{x^2-1}=\frac12\left(\frac1{x-1}-\frac1{x+1}\right).$$
- $x=0$ 時 $\frac1{x^2-1}=-1$。
- $x\to1^-$ 或 $x\to-1^+$ 時 $x^2-1\to0^-$，所以 $\frac1{x^2-1}\to-\infty$。
- 因此 $\varphi(x)=e^{1/(x^2-1)}\to0$：在 $\pm1$ 平滑地接到 0。[▶ 53:44](https://youtu.be/rmz3GsOaE-Y?t=3224)

【課堂討論】講者畫圖時，一位學生提到把兩端接起來像環面；最後大家去看課本 p. 290 的 Figure 6.1。[▶ 55:27](https://youtu.be/rmz3GsOaE-Y?t=3327)

【口頭】（part 2 開頭）講者說這個例子的「秘方」是 $\pm1$ 是**本性奇點**（essential singularity）：$e^{1/(x-1)}$ 展開是 $1+\frac1{x-1}+\frac1{2(x-1)^2}+\cdots$ 無窮多項負冪次。所以測試函數**不是解析函數**——這很重要，因為解析函數若在一段區間上為 0 就處處為 0，無法有緊支撐。[▶ part 2 01:04](https://youtu.be/pQr5xMlUnmI?t=64)

**從一個造出很多個**：[▶ 56:03](https://youtu.be/rmz3GsOaE-Y?t=3363)
- $\varphi(ax+b)$（$a\ne0$）
- $f(x)\varphi(x)$（$f$ 任意光滑函數）
- $\varphi^{(k)}(x)$

**多變數**：
$$\varphi(x)=\begin{cases}\exp\left(\dfrac1{x_1^2+\cdots+x_N^2-1}\right),&x_1^2+\cdots+x_N^2<1\\[4pt]0,&\text{其他}\end{cases}$$
【口頭】二維就是把一維的圖繞軸轉一圈。三維不好畫，可以想成給空間上色：原點附近一團彩色的球，外面全透明。講者說這也是建構流形理論時會玩的把戲。[▶ 57:18](https://youtu.be/rmz3GsOaE-Y?t=3438)

**Theorem 6.2.3**：$\mathcal D$ 是向量空間；若 $\varphi,\psi\in\mathcal D$，則[▶ 59:39](https://youtu.be/rmz3GsOaE-Y?t=3579)
- (a) $f\varphi\in\mathcal D$（$f$ 光滑）；
- (b) $\varphi\circ A\in\mathcal D$（$A$ 是 $\mathbb R^N$ 到 $\mathbb R^N$ 的仿射變換）；
- (c) $\varphi*\psi\in\mathcal D$。

（課本：證明留作習題。）

---

## 7. 測試函數的收斂

[▶ part 2 03:13](https://youtu.be/pQr5xMlUnmI?t=193)

**Definition 6.2.4**：$\varphi_n\xrightarrow{\mathcal D}\varphi$ 的意思是同時有
- (a) 所有 $\varphi_n$ 都在**同一個**有界集合 $S$ 之外為 0；
- (b) 對每個多重指標 $\alpha$，$D^\alpha\varphi_n\to D^\alpha\varphi$ 在 $\mathbb R^N$ 上一致收斂。

**Theorem 6.2.6**：若 $\varphi_n\xrightarrow{\mathcal D}\varphi$、$\psi_n\xrightarrow{\mathcal D}\psi$，則[▶ part 2 04:39](https://youtu.be/pQr5xMlUnmI?t=279)
- (a) $a\varphi_n+b\psi_n\xrightarrow{\mathcal D}a\varphi+b\psi$；
- (b) $f\varphi_n\xrightarrow{\mathcal D}f\varphi$（$f$ 光滑）；
- (c) $\varphi_n\circ A\xrightarrow{\mathcal D}\varphi\circ A$（$A$ 仿射）；
- (d) $D^\alpha\varphi_n\xrightarrow{\mathcal D}D^\alpha\varphi$。

【課本補充】Example 6.2.5 的一個反例很值得記：$\varphi_n(x)=b_n\varphi(a_nx)$（$a_n,b_n\to0^+$）的每階導數都一致收斂到 0，但支撐集越來越大、沒有共同的有界集合，所以**不在** $\mathcal D$ 中收斂。條件 (a) 不是多餘的。

---

## 8. 分佈的定義；正則與奇異分佈

[▶ part 2 05:46](https://youtu.be/pQr5xMlUnmI?t=346)

【口頭】「這就是第 6 章的核心。」

**Definition 6.2.7**：$\mathbb R^N$ 上的**分佈**（distribution）$F$ 是 $\mathcal D(\mathbb R^N)$ 上的**連續線性泛函**：
- 線性：$F(a\varphi+b\psi)=aF(\varphi)+bF(\psi)$；
- 連續：$\varphi_n\xrightarrow{\mathcal D}\varphi$ 時 $F(\varphi_n)\to F(\varphi)$。

全體分佈記為 $\mathcal D'(\mathbb R^N)$ 或 $\mathcal D'$。【Q&A】學生問那一撇是不是某種運算；講者說不是，只是名字。[▶ part 2 10:42](https://youtu.be/pQr5xMlUnmI?t=642)

**記號**：從這裡開始不寫 $F(\varphi)$，而寫
$$\langle F,\varphi\rangle .$$
【口頭】課本說這**不是**內積，也不會混淆；但講者說這是刻意的——它和內積有相似之處，想想內積在 Fourier 分析和廣義 Fourier 係數裡扮演的角色。[▶ part 2 07:40](https://youtu.be/pQr5xMlUnmI?t=460)

**函數怎麼變成分佈**：嚴格說函數不是分佈（定義域不是 $\mathcal D$）。但每個**局部可積**函數 $f$ 都對應一個分佈 $F$：[▶ part 2 08:49](https://youtu.be/pQr5xMlUnmI?t=529)
$$\langle F,\varphi\rangle=\int_{\mathbb R^N}f\varphi .$$
【口頭】這合理：測試函數只在有界集合上不為 0，局部可積函數乘上它還是可積的。

**Definition 6.2.8**：若存在局部可積的 $f$ 使 $\langle F,\varphi\rangle=\int f\varphi$ 對所有 $\varphi\in\mathcal D$ 成立，$F$ 叫**正則分佈**（regular distribution）；否則叫**奇異分佈**（singular distribution）。

---

## 9. 例：Heaviside 函數、Dirac δ

### Heaviside

[▶ part 2 11:17](https://youtu.be/pQr5xMlUnmI?t=677)

**Example 6.2.9**：$\Omega\subset\mathbb R^N$ 開集（或只要可測）。
$$\langle F,\varphi\rangle=\int_\Omega\varphi=\int_{\mathbb R^N}\chi_\Omega\,\varphi$$
是正則分佈（$\chi_\Omega$ 是 $\Omega$ 的特徵函數）。線性來自積分的線性。

取 $\Omega=(0,\infty)\times\cdots\times(0,\infty)$，就得到 **Heaviside 函數**。[▶ part 2 13:03](https://youtu.be/pQr5xMlUnmI?t=783)

【口頭】講者自己會把「被積的那個函數」叫 Heaviside 函數。用單位階梯函數
$$u(t)=\begin{cases}0,&t<0\\1,&t\ge0\end{cases}$$
寫成 $\langle F,\varphi\rangle=\int u(x_1)u(x_2)\cdots u(x_N)\,\varphi(x)\,dx$。它在所有座標都為正時是 1：平面上第一象限為 1、其他三個象限為 0；三維時第一卦限為 1、其他七個為 0。[▶ part 2 14:44](https://youtu.be/pQr5xMlUnmI?t=884)

### Dirac δ

[▶ part 2 15:50](https://youtu.be/pQr5xMlUnmI?t=950)

**Example 6.2.10**：
$$\langle\delta,\varphi\rangle=\varphi(0).$$
- 線性：明顯。
- 連續：$\varphi_n\xrightarrow{\mathcal D}\varphi$ ⟹ $\varphi_n\to\varphi$ 一致收斂 ⟹ $\varphi_n(0)\to\varphi(0)$。[▶ part 2 18:28](https://youtu.be/pQr5xMlUnmI?t=1108)

**δ 是奇異分佈**：【口頭】要證明不存在函數 $f$ 使 $\varphi(0)=\int f\varphi$ 對所有 $\varphi$ 成立。講者說「顯然荒謬」：δ 的值只看 $\varphi$ 在 0 的值，不可能用一個固定的函數去積分得到所有這些值；「也許可以寫得更嚴謹」。[▶ part 2 19:37](https://youtu.be/pQr5xMlUnmI?t=1177)

以下**不是逐字稿內容**，是依控制收斂定理推論的嚴謹版本：假設有局部可積 $f$ 使 $\int f\varphi=\varphi(0)$。取鐘形函數 $\varphi$（$\varphi(0)=e^{-1}$），令 $\varphi_n(x)=\varphi(nx)$。則 $\varphi_n(0)=e^{-1}$ 對所有 $n$ 成立；但 $\varphi_n$ 的支撐在 $|x|<1/n$ 內、$|f\varphi_n|\le e^{-1}|f|\,\chi_{\{|x|<1\}}$（可積），且 $x\ne0$ 時 $\varphi_n(x)\to0$，所以由控制收斂 $\int f\varphi_n\to0\ne e^{-1}$，矛盾。

【Q&A】一位學生說開始看出這和流形上的微積分有關，問哪本書做「流形上的嚴謹分析」。講者說他知道嚴謹的實分析和泛函分析的書，流形版的想到一本，作者名字幕作「Warner／Werner」（講者自己也不確定），說之後 email 給學生。[▶ part 2 16:40](https://youtu.be/pQr5xMlUnmI?t=1000)

**Example 6.2.11**：對多重指標 $\alpha$，$\langle F,\varphi\rangle=D^\alpha\varphi(0)$ 也是分佈，證明和 δ 類似。

---

## 10. 分佈的導數

[▶ part 2 21:38](https://youtu.be/pQr5xMlUnmI?t=1298)

**原則**：對分佈定義新運算時，要和正則分佈上的古典定義一致。

課本的做法：若某運算 $A$ 對函數有
$$\int (Af)\varphi=\int f\,(A^*\varphi)$$
而 $A^*$ 是把 $\mathcal D$ 映到 $\mathcal D$ 的連續運算，就**定義** $\langle AF,\varphi\rangle=\langle F,A^*\varphi\rangle$。

【口頭】講者說課本「有點滑頭」：沒說 $A^*$ 是伴隨算子，但記號上就是那個樣子。[▶ part 2 23:24](https://youtu.be/pQr5xMlUnmI?t=1404)

**導數的情形**：分部積分（$\varphi$ 有緊支撐，邊界項為 0）給出
$$\int\frac{\partial f}{\partial x_k}\varphi=-\int f\frac{\partial\varphi}{\partial x_k} .$$

**Definition 6.2.12**：[▶ part 2 24:00](https://youtu.be/pQr5xMlUnmI?t=1440)
$$\left\langle\frac{\partial F}{\partial x_k},\varphi\right\rangle=-\left\langle F,\frac{\partial\varphi}{\partial x_k}\right\rangle ,\qquad
\left\langle D^\alpha F,\varphi\right\rangle=(-1)^{|\alpha|}\left\langle F,D^\alpha\varphi\right\rangle .$$

【口頭】負號的理由是「好幾件事串在一起」：模仿伴隨算子、就是分部積分公式、而且讓正則分佈和底下的函數一致。[▶ part 2 25:08](https://youtu.be/pQr5xMlUnmI?t=1508)

**Theorem 6.2.13**：$F$ 是分佈 ⟹ $D^\alpha F$ 對任何多重指標 $\alpha$ 都是分佈。講者說證明不難、沒做。

【課本補充】證明要點：線性直接驗算；連續性來自 Theorem 6.2.6(d)——$\varphi_n\xrightarrow{\mathcal D}\varphi$ ⟹ $D^\alpha\varphi_n\xrightarrow{\mathcal D}D^\alpha\varphi$ ⟹ $\langle F,D^\alpha\varphi_n\rangle\to\langle F,D^\alpha\varphi\rangle$。

---

## 11. 【口頭】階梯函數的導數是 δ

[▶ part 2 25:42](https://youtu.be/pQr5xMlUnmI?t=1542)

講者講了大學時的故事：同一學期修實分析和電磁學。

- 實分析課上，他因為「證明開頭已經說 $c$ 是實數，後面沒再說一次」而被扣分——「嚴謹到煩人」。
- 電磁學課上，教授用 $\Theta(t)=0$（$t<0$）、$1$（$t\ge0$）（字幕作「$\ge1$」，依上下文應為 $\ge0$），問：「階梯函數的導數是什麼？」[▶ part 2 27:23](https://youtu.be/pQr5xMlUnmI?t=1643)
- 他心想：「不連續，哪來的導數？」結果教授笑大家連這都不知道：
$$\frac{d}{dt}\Theta(t)=\delta(t).$$

【口頭】「一旦看到就忘不掉」：函數在一瞬間跳升一個單位。可以用一列光滑的 $f_n\to\Theta$ 來想，$f_n'$ 在跳的地方變成越來越高、越來越窄的尖峰，其他地方是 0。[▶ part 2 29:57](https://youtu.be/pQr5xMlUnmI?t=1797)

**課本的嚴格證明（Example 6.2.14，p. 294）**：[▶ part 2 31:18](https://youtu.be/pQr5xMlUnmI?t=1878)
$$\left\langle\frac{d}{dx}H,\varphi\right\rangle=-\left\langle H,\varphi'\right\rangle=-\int_0^\infty\varphi'(x)\,dx=-\left(\lim_{x\to\infty}\varphi(x)-\varphi(0)\right)=\varphi(0)=\langle\delta,\varphi\rangle .$$
（$\varphi$ 在有界集合外為 0，所以 $\lim_{x\to\infty}\varphi(x)=0$。）因此 $H'=\delta$。

---

## 12. 第 6 章其餘部分（只翻過）

[▶ part 2 31:51](https://youtu.be/pQr5xMlUnmI?t=1911)

講者快速翻過，沒有上黑板：
- 分佈的弱收斂；p. 296 用函數列逼近 δ。【課本補充】Example 6.2.18：$f_n(x)=\dfrac{n}{\pi(1+n^2x^2)}$ 在分佈意義下收斂到 δ。
- Theorem 6.2.19：$F_n\to F$ ⟹ $D^\alpha F_n\to D^\alpha F$（可以逐項微分）。
- 反導數（Theorem 6.2.21：每個分佈都有反導數）；Theorem 6.2.22：$F'=0$ ⟹ $F$ 是常數。
- p. 298 起：把一切改到開集 $\Omega\subset\mathbb R^N$ 上。p. 299 的 Leibniz 公式（多重導數的乘積法則）：【口頭】「人生某個時候你該試著證明它；我只證過一維的。」[▶ part 2 32:57](https://youtu.be/pQr5xMlUnmI?t=1977)
- §6.3 Sobolev 空間：「很美，希望你研究所會修。」
- 後面用分佈重看 Green 函數：p. 306 基本解（fundamental solution）、p. 307 Green 函數的嚴格定義、pp. 309–311 多變數的 Lagrange 公式（講者說一維版本在 Haberman 的書裡看過）。
- 本章最後有一個同時用 Fourier 和 Laplace 變換解（講者記得是）波動方程的例子，沒時間做。

講者出了幾題這部分的作業，說做作業會讓內容「凝固」一點。[▶ part 2 35:44](https://youtu.be/pQr5xMlUnmI?t=2144)

**預告**：下次講量子力學。

---

## 13. 一頁速查表

| 項目 | 公式／內容 | 關鍵一步 |
|---|---|---|
| ODE → 代數 | $\hat p(i\omega)\hat y=\hat f$ | $D\mapsto i\omega$ |
| 解 | $\hat y=\hat f\hat g$，$\hat g=1/\hat p(i\omega)$ | admittance |
| 反變換 | $y=\frac1{\sqrt{2\pi}}\int f(\xi)g(t-\xi)d\xi=\int f(\xi)G(t-\xi)d\xi$ | 摺積定理 |
| δ 的變換 | $\hat\delta=\frac1{\sqrt{2\pi}}$ | 積分變取值 |
| Green 函數 | $LG=\delta$ 的解，$G=g/\sqrt{2\pi}$ | 單位脈衝的響應 |
| RL 電路 $t>0$ | $I=E_0\left(\frac{e^{-t}}{R-L}-\frac{2Le^{-Rt/L}}{R^2-L^2}\right)$ | 上半平面極點 $i$、$iR/L$ |
| RL 電路 $t<0$ | $I=\frac{E_0e^t}{L+R}$ | 下半平面極點 $-i$ |
| 弱形式 | $\int uL^*\varphi=\int f\varphi$，$L^*=\sum(-1)^{|\alpha|}a_\alpha D^\alpha$ | 分部積分，邊界項為 0 |
| 測試函數 | $C^\infty$、在有界集外為 0；記 $\mathcal D$ | |
| 鐘形函數 | $e^{1/(x^2-1)}$（$|x|<1$），0 其他 | $x\to\pm1$ 時指數 $\to-\infty$；非解析 |
| $\mathcal D$ 收斂 | 共同有界支撐＋每階導數一致收斂 | |
| 分佈 | $\mathcal D$ 上連續線性泛函，記 $\langle F,\varphi\rangle$ | |
| 正則分佈 | $\langle F,\varphi\rangle=\int f\varphi$，$f$ 局部可積 | |
| Dirac δ | $\langle\delta,\varphi\rangle=\varphi(0)$；奇異 | 縮放 $\varphi(nx)$＋控制收斂 |
| 分佈導數 | $\langle D^\alpha F,\varphi\rangle=(-1)^{|\alpha|}\langle F,D^\alpha\varphi\rangle$ | 模仿分部積分 |
| $H'=\delta$ | $-\int_0^\infty\varphi'=\varphi(0)$ | |

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Dirac δ、$\langle\cdot,\cdot\rangle$ 記號 | 第 33–34 集：量子力學（bra–ket 記號、位置本徵態） |
| Fourier 變換、Gauss 函數 | 第 33–34 集：位置與動量、測不準原理 |
| 弱形式（第 19 集的弱收斂、Sobolev 空間） | 本課到此為止；§6.3、§6.5 留給研究所 |

---

## 附：本集一句話總結

> **Fourier 變換把常係數 ODE 變成除法，反變換時 Green 函數就是「對單位脈衝 δ 的響應」；而為了讓 δ 這種「不是函數的函數」有嚴格意義，第 6 章改用光滑、有界支撐的測試函數去「測試」——分佈就是測試函數上的連續線性泛函，導數靠分部積分搬到 $\varphi$ 上定義，於是不連續的階梯函數也能微分：$H'=\delta$。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-04-21 錄影逐字稿（YouTube 自動字幕，part 1 約 59:40、part 2 約 36:20）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.12、§6.1–6.2 整理。*
