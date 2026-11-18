---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 30
lecture: Lecture 30
date: 2023-04-14
video: https://youtu.be/1nelD2AP68E （part 1）、https://youtu.be/hgw7iXusEaI （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.9（書頁 247–253，PDF 頁 266–272）；開頭是講者自己的 Nagle–Saff–Snider 習題解答
---

# 第 30 集 · Basel 問題、分離變數的例子、Sturm–Liouville 理論 [▶ 影片](https://youtu.be/1nelD2AP68E)

← 上一集：[29-spectral-theorem-bvp-wave](29-spectral-theorem-bvp-wave.md) ｜ [總目錄](README.md) ｜ 下一集：[31-greens-function-fourier-transform](31-greens-function-fourier-transform.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 30 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 whisper 轉錄，時間點可能差 1–2 秒；part 2 28:54 自動字幕）＋ Debnath & Mikusiński §5.9 ＋ 講者投影的解答與參考書（只依口述）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Fourier 級數與 Basel 問題](#1-fourier-級數與-basel-問題)
- [2. Laplace 方程的分離變數](#2-laplace-方程的分離變數)
- [3. 波動方程、d'Alembert 解](#3-波動方程dalembert-解)
- [4. Sturm–Liouville 系統的定義](#4-sturmliouville-系統的定義)
- [5. 例子與週期 Sturm–Liouville 系統](#5-例子與週期-sturmliouville-系統)
- [6. 算子 L 與 Lagrange 恆等式](#6-算子-l-與-lagrange-恆等式)
- [7. Abel 公式](#7-abel-公式)
- [8. 本徵函數除常數倍外唯一](#8-本徵函數除常數倍外唯一)
- [9. L 是自伴的；本徵值是實數](#9-l-是自伴的本徵值是實數)
- [10. 加權正交](#10-加權正交)
- [11. 參考書的總結](#11-參考書的總結)
- [12. 預告：Green 函數](#12-預告green-函數)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者先做一點「展示說明」：投影他以前寫的 Nagle–Saff–Snider PDE 那章的解答（下課後會分享連結），然後回到課本 §5.9。「不必全部抄下來。」[▶ 06:12](https://youtu.be/1nelD2AP68E?t=372)

| 主題 | 來源 |
|---|---|
| Fourier 級數、$\sum\frac1{n^2}=\frac{\pi^2}6$ | 講者的解答 |
| Laplace 方程、波動方程、d'Alembert | 講者的解答 |
| Sturm–Liouville 系統 | Definition 5.9.1–5.9.2、Example 5.9.3–5.9.4，pp. 247–249 |
| Lagrange 恆等式、Abel 公式、唯一性 | Theorem 5.9.5–5.9.7，pp. 250–251 |
| 自伴、實本徵值、加權正交 | Theorem 5.9.8–5.9.10，pp. 251–253 |
| Green 函數預告 | 講者的筆記 |

---

## 1. Fourier 級數與 Basel 問題

[▶ 00:36](https://youtu.be/1nelD2AP68E?t=36)

講者展示：$x$ 的 Fourier 級數——對 cos 和 sin 在 $[-\pi,\pi]$ 上積分，得到一個 sin 的無窮和；也有分段連續函數的 Fourier 展開。

**歷史**【口頭】[▶ 01:09](https://youtu.be/1nelD2AP68E?t=69)：講者前一天讀 Fourier 的歷史。Fourier 認為任何函數都能展開成三角級數，但想法起初被 **Lagrange**（大約 1800 年前後的「大師」）否定；Lagrange 在世時 Fourier 很難發表某些東西，因為 Lagrange 用不同的方法做三角級數。有趣的是 Fourier 說「任何連續函數」，但 Fourier 展開從一開始就允許不連續的函數。講者：這些詞（例如「連續」）今天有精確的技術意義，當年的人用法未必一樣，「就像聽 1950 年和 1980 年的人談『保守價值』」。

### $x^2$ 的 Fourier 級數與 $\sum1/n^2$

[▶ 02:16](https://youtu.be/1nelD2AP68E?t=136)

講者展示（在 $[-1,1]$ 上）：

$$x^2=\frac13+\sum_{n=1}^\infty\frac{4(-1)^n}{n^2\pi^2}\cos(n\pi x).$$

【課堂討論】代 $x=1$。講者：$x=1$ 正好在適用範圍的邊緣，「希望它行得通……級數最有趣的結果常發生在定義域的邊上」。這裡的等號其實是「幾乎處處」。

$\cos(n\pi)=(-1)^n$，乘上 $(-1)^n$ 變成 1：

$$1=\frac13+\sum_{n=1}^\infty\frac{4}{n^2\pi^2}\ \Longrightarrow\ \frac23=\frac{4}{\pi^2}\sum\frac1{n^2}\ \Longrightarrow\ \sum_{n=1}^\infty\frac1{n^2}=\frac23\cdot\frac{\pi^2}4=\frac{\pi^2}6.$$

講者：「這就是為什麼 $p=2$ 級數的和是 $\pi^2/6$。」Euler 早就知道；三角級數比 Fourier 早，但 Fourier 第一個真正推廣它們的應用，以及應用的普遍性。

> 以下**不是逐字稿內容**，是補一句為什麼在 $x=1$ 可以代：$x^2$ 的週期延拓在 $x=\pm1$ 處連續（兩邊的值都是 1），而且分段光滑，所以 Fourier 級數在那裡逐點收斂到 1。若是有跳躍，級數會收斂到跳躍的平均值（第 29 集講者提過）。

講者也指出投影片上的 Legendre 多項式跟一位學生的作業有點相關。

---

## 2. Laplace 方程的分離變數

[▶ 06:43](https://youtu.be/1nelD2AP68E?t=403)

**Laplace 方程**：$\nabla^2u=0$。一維 $u''=0$，二維 $u_{xx}+u_{yy}=0$，$n$ 維 $\sum\partial^2u/\partial x_i^2=0$。

講者【口頭】：人們也在流形上研究 Laplacian：流形上需要什麼結構 Laplacian 才是良定義的算子？他的學生 Min 研究過流形上哪裡能寫下 Dirac 算子。「微分算子跟空間的配對，是數學物理、現代數學研究的活躍領域。」[▶ 07:15](https://youtu.be/1nelD2AP68E?t=435)

- 用**極座標**分離變數，會得到變係數問題，其實是 **Cauchy–Euler** 方程。
- **Gauss 定律**取散度得 **Poisson 方程**（跟 Laplacian 有關）：先解 Laplace 方程，再加一個處理非齊次項的部分——像「齊次解加特解」。

### 例：矩形上的 Laplace 方程

[▶ 08:48](https://youtu.be/1nelD2AP68E?t=528)

$u_{xx}+u_{yy}=0$，$0<x<\pi$、$0<y<1$；$x=0,\pi$ 處導數為 0；下邊給一個函數、上邊是 0（可以想成電壓）。

分離變數後，只有一種情況給非零解（上一集的例 2）：$x$ 方向是 $\cos nx$，$K=n^2$；$y$ 方程變成 $Y''-n^2Y=0$，解是 cosh、sinh。總解是 cos 乘 cosh／sinh 的乘積的級數。講者：「我把它當作空白樣板」，再選係數去配邊界條件。（講者說叫「初始條件」不太對，這裡是 $x,y$，應該叫邊界條件。）

講者說那份解答是他「找到定理之前」寫的，每次都把所有情況重做一遍。答案最後用 cosh、sinh 的恆等式化簡，只是為了跟書後答案對上；「有趣的數學在這裡就結束了」。[▶ 11:59](https://youtu.be/1nelD2AP68E?t=719)

**第二個例子**[▶ 12:30](https://youtu.be/1nelD2AP68E?t=750)：端點值為 0，邊界函數是任意的 $f(x)$。同樣的套路：只有一種情況有貢獻，本徵值 $-n^2$，$y$ 方向 cosh、sinh。把 $f$ 寫成 Fourier 級數，讓解的係數跟 $f$ 的 Fourier 係數對上；係數要算積分。「這是非常強大的方法。」講者說這是他以前的想法，「不是錯，只是不是最好的想法」。

**Fourier 與熱流**【口頭】[▶ 13:36](https://youtu.be/1nelD2AP68E?t=816)：Fourier 研究熱流、解熱方程 $\nabla^2u=\partial u/\partial t$。他把物體切成小立方體，研究能量從立方體一面流到另一面，由此**推導出** Laplacian。兩端值為 0、導數為 0 這些邊界條件，Fourier 都看過。

**圓盤上**[▶ 15:13](https://youtu.be/1nelD2AP68E?t=913)：用極座標，加上週期邊界條件，會碰到 Cauchy–Euler 問題——這是求鼓面波動、圓盤熱流要用的數學。講者說這超出課程範圍。

講者回憶【口頭】[▶ 16:19](https://youtu.be/1nelD2AP68E?t=979)：大學修到這門課時很有成就感，解一題寫了三頁，「而且不是證明，只是計算」。現在懂得用定理，半頁就能做完。

---

## 3. 波動方程、d'Alembert 解

[▶ 16:50](https://youtu.be/1nelD2AP68E?t=1010)

**波動方程**：同樣的方法，分離變數得到一對相關的微分方程。講者：「我在為 Sturm–Liouville 鋪路，因為這些全都是 Sturm–Liouville 問題。」得到「本徵解」，取無窮級數，選係數配合條件；如果初始條件是 $x-x^2$ 這種，就得真的算 Fourier 積分。

**d'Alembert 解**[▶ 18:25](https://youtu.be/1nelD2AP68E?t=1105)：定義在 $(-\infty,\infty)$ 上時，把解寫成**向右走的波加向左走的波**之和。代入初始條件解出各部分。講者：「d'Alembert 解很漂亮」；這也能用另一種方法推，更漂亮的是用 **Fourier 變換**，他希望這學期能講到。

> 以下**不是逐字稿內容**，是補上 d'Alembert 解的形式（速度 1）：$u(x,t)=F(x+t)+G(x-t)$；給 $u(x,0)=f$、$u_t(x,0)=g$ 時，$u=\frac12\left[f(x+t)+f(x-t)\right]+\frac12\int_{x-t}^{x+t}g(s)ds$。

**微分方程課該教什麼**【口頭】[▶ 19:29](https://youtu.be/1nelD2AP68E?t=1169)：講者說這是學校微分方程課（某位老師）不會教的部分。如果他教微分方程，最後三堂一定講熱方程、波動方程、Laplace 方程和 Fourier 級數基礎，因為對工程很重要。「老師有個習慣，在一階方程上花太多時間；我覺得那對學生沒幫助，也不有趣。」

---

## 4. Sturm–Liouville 系統的定義

[▶ 20:37](https://youtu.be/1nelD2AP68E?t=1237) 課本 §5.9。

講者提到：第 5 章前面有些部分他很早就講過（壓縮映射、存在唯一性，第 8–9 集）；他本來想回來做得更好，「結果那就是全部了，抱歉」。更深的存在唯一性定理、甚至反函數定理，都是用壓縮映射證的。

**Definition 5.9.1（正則 Sturm–Liouville 系統）**：

$$\frac{d}{dx}\left(p(x)\frac{du}{dx}\right)+\big(q(x)+\lambda\omega(x)\big)u=0,\qquad a\le x\le b, \tag{5.66}$$

邊界條件

$$a_1u(a)+a_2u'(a)=0,\qquad b_1u(b)+b_2u'(b)=0, \tag{5.67}$$

其中 $p,q,\omega$ 是 $[a,b]$ 上連續的實值函數，$p$ 和 $\omega$ 在 $[a,b]$ 上**為正**，$p'$ 存在且連續，$a_1,a_2,b_1,b_2$ 是給定實數，$a_1^2+a_2^2>0$、$b_1^2+b_2^2>0$。

講者：「system」這裡用得比較合理：「能用 set 就別用 system。這不是集合，是一堆東西放在一起。」[▶ 22:30](https://youtu.be/1nelD2AP68E?t=1350)

**$a_1^2+a_2^2>0$ 是什麼意思**【口頭】[▶ 25:19](https://youtu.be/1nelD2AP68E?t=1519)：「這裡有東西可學」：說一組常數不全為 0，花俏的寫法就是平方和為正。意思只是 $a_1,a_2$ 不能都是 0，否則邊界條件是「$0=0$」的蠢方程。

**Definition 5.9.2（奇異 Sturm–Liouville 系統）**[▶ 26:27](https://youtu.be/1nelD2AP68E?t=1587)：其他條件都一樣，但 $p$ 只在開區間 $(a,b)$ 上為正，可能在一個或兩個端點為 0。邊界條件換成：

- (a) $u$ 在 $(a,b)$ 上有界；
- (b) 若 $p$ 在某端點不為 0，就在那端點滿足 (5.67) 形式的條件。

講者說他不太確定 (b) 的確切意思，「別太擔心，他會給例子」。

---

## 5. 例子與週期 Sturm–Liouville 系統

**Example 5.9.3**[▶ 28:49](https://youtu.be/1nelD2AP68E?t=1729)（上一集做過）：$u''+\lambda u=0$，$0\le x\le\pi$，$u(0)=u(\pi)=0$。

$$\lambda_n=n^2,\qquad u_n(x)=\sin nx\quad(n=1,2,\dots).$$

課本說：這裡 $\lambda_n\to\infty$，跟緊緻自伴算子本徵值趨近 0 不同（§5.10 解釋）。

**週期 Sturm–Liouville 系統**[▶ 30:23](https://youtu.be/1nelD2AP68E?t=1823)：同樣的方程，但

$$p(a)=p(b),\qquad u(a)=u(b),\qquad u'(a)=u'(b).$$

講者：之前投影片上極座標、繞一圈的 Laplace 方程就是週期 Sturm–Liouville 問題，而且可能是奇異的——典型的奇異方程是 **Cauchy–Euler**，0 是正則奇點（有限階的極點，可以處理）。深入下去就是 **Frobenius 方法**，「更深的魔法，每個應用數學的學生都該深入學」，是下一層的微分方程，他在入門課教過，「很難」。

**Example 5.9.4**[▶ 32:35](https://youtu.be/1nelD2AP68E?t=1955)：$u''+\lambda u=0$，$-\pi<x<\pi$，$u(\pi)=u(-\pi)$、$u'(\pi)=u'(-\pi)$。

$$\lambda=0,1,4,\dots,n^2,\dots;\qquad\text{本徵函數 }1,\cos x,\sin x,\cos2x,\sin2x,\dots$$

【課本補充】每個 $\lambda_n=n^2$（$n\ge1$）有**兩個**線性獨立的本徵函數 $\cos nx$、$\sin nx$；$\lambda=0$ 的本徵函數是常數 1。（所以下面「本徵函數唯一」的定理只對**正則**系統，週期系統不成立。）

---

## 6. 算子 L 與 Lagrange 恆等式

[▶ 34:10](https://youtu.be/1nelD2AP68E?t=2050)

令

$$Lu=\frac{d}{dx}\left(p\frac{du}{dx}\right)+qu.$$

方程變成 $Lu=-\lambda\omega u$。

講者【口頭】[▶ 34:42](https://youtu.be/1nelD2AP68E?t=2082)：這就是為什麼叫 $\lambda$「本徵值」讓他有點不舒服：精神上有點像，但有權函數 $\omega$；即使 $\omega=1$，他平常的慣例也該是 $+$ 而不是 $-$。「類比是對的，但如果把對應搞得太死板會把你逼瘋，不值得。」

**定義域** $\mathcal D(L)$：$[a,b]$ 上的複值函數 $u$，使 $u''\in L^2([a,b])$ 且滿足邊界條件。$L:\mathcal D(L)\to L^2([a,b])$。奇異系統把邊界條件換成「有界」加上另一端的條件。

**Theorem 5.9.5（Lagrange 恆等式）**[▶ 36:49](https://youtu.be/1nelD2AP68E?t=2209)：對 $u,v\in\mathcal D(L)$，

$$uLv-vLu=\frac{d}{dx}\left[p\left(u\frac{dv}{dx}-v\frac{du}{dx}\right)\right]. \tag{5.68}$$

講者：「這純粹是計算，我不做。」

【課本補充】$uLv-vLu=u(pv')'+quv-v(pu')'-quv=u(pv')'-v(pu')'$，而 $\left[p(uv'-vu')\right]'=u'pv'+u(pv')'-v'pu'-v(pu')'$，中間兩項相消，一樣。

---

## 7. Abel 公式

[▶ 37:58](https://youtu.be/1nelD2AP68E?t=2278) 課本 Theorem 5.9.6。

**定理**：若 $u,v$ 是 $Lu+\lambda\omega u=0$ 在 $[a,b]$ 上的兩個解，則

$$p(x)W(x;u,v)=\text{常數},\qquad W=\det\begin{pmatrix}u&u'\\v&v'\end{pmatrix}=uv'-u'v$$

（**Wronskian**，Josef Hoëné de Wronski，1778–1853）。

講者說「今天該算點東西」，跟著課本推[▶ 39:46](https://youtu.be/1nelD2AP68E?t=2386)：

1. 寫出兩個方程：$(pu')'+(q+\lambda\omega)u=0$、$(pv')'+(q+\lambda\omega)v=0$。
2. 第一式乘 $v$、第二式乘 $u$，相減：$(q+\lambda\omega)uv$ 那項消掉，
   $$u(pv')'-v(pu')'=0.$$
   講者：「這幾乎就是 Lagrange 恆等式。」
3. 從 $a$ 積到 $x$。講者：要用分部積分（乘積法則）：$u(pv')'=(upv')'-pv'u'$，$v(pu')'=(vpu')'-pu'v'$。相減時 $pu'v'$ 兩項消掉，剩下全導數：
   $$\Big[p(uv'-vu')\Big]_a^x=0.$$
   「這是分部積分（乘積法則）在積分裡移動導數的魔法。」[▶ 45:24](https://youtu.be/1nelD2AP68E?t=2724)
4. 所以 $p(x)\big(u(x)v'(x)-u'(x)v(x)\big)-p(a)\big(u(a)v'(a)-u'(a)v(a)\big)=0$，即 $p(x)W(x)=p(a)W(a)$，常數。

講者一度困惑課本寫「$=$ 常數」而他算出 0；後來看懂：那表示 $p(x)W(x)$ 等於 $p(a)W(a)$，是常數。[▶ 48:11](https://youtu.be/1nelD2AP68E?t=2891)

---

## 8. 本徵函數除常數倍外唯一

[▶ 48:48](https://youtu.be/1nelD2AP68E?t=2928) 課本 Theorem 5.9.7。

**定理**：正則 Sturm–Liouville 系統的本徵函數除了常數倍以外是唯一的。

**證明**：$u,v$ 是同一個 $\lambda$ 的本徵函數，都滿足 Abel 公式的前提：$p(x)W(x;u,v)=$ 常數。

1. $p>0$，所以若 $W$ 在 $[a,b]$ 某一點為 0，就處處為 0（常數為 0）。
2. 邊界條件：$a_1u(a)+a_2u'(a)=0$、$a_1v(a)+a_2v'(a)=0$。寫成矩陣[▶ 52:22](https://youtu.be/1nelD2AP68E?t=3142)：
   $$\begin{pmatrix}u(a)&u'(a)\\v(a)&v'(a)\end{pmatrix}\begin{pmatrix}a_1\\a_2\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$
   齊次方程有零解；但 $(a_1,a_2)$ 是給定的、不全為 0（$a_1^2+a_2^2>0$），是**非零解**。所以係數矩陣奇異，行列式 $W(a)=0$。（學生指出講者一開始寫的矩陣是轉置，講者：「你說得對，行列式一樣。」）[▶ 53:37](https://youtu.be/1nelD2AP68E?t=3217)
3. 所以 $W\equiv0$，因此 $u,v$ 線性相依：$u=cv$。∎

**一個微妙的地方**【口頭】[▶ 55:28](https://youtu.be/1nelD2AP68E?t=3328)：「Wronskian 恆為 0 ⟹ 線性相依」只對**微分方程的解**成立。講者舉反例：$x^2$ 和 $x|x|$，它們的 Wronskian 在整個實數線上恆為 0，但線性獨立。這兩個不是同一個二階線性方程的解，所以那個定理不適用。「課本在這裡依賴了一些微分方程的理論，這裡有微妙之處。」

講者也說：Abel 公式對 $n$ 階線性方程都成立（他的筆記有），他習慣的形式是用積分寫的。而**一維** Sturm–Liouville 問題的本徵函數唯一；二維、三維就不是。

---

## 9. L 是自伴的；本徵值是實數

### Theorem 5.9.8：$L$ 自伴

[▶ 57:22](https://youtu.be/1nelD2AP68E?t=3442)

**定理**：對 $u,v\in\mathcal D(L)$，$\langle Lu,v\rangle=\langle u,Lv\rangle$（$L^2([a,b])$ 內積）。也就是 **$L$ 是自伴算子**。

**證明**：邊界條件的常數都是實數，所以 $v\in\mathcal D(L)$ ⟹ $\bar v\in\mathcal D(L)$；$p,q$ 實值，所以 $L\bar v=\overline{Lv}$。講者：「某種意義上 $L$ 是實算子。」

$$\langle Lu,v\rangle-\langle u,Lv\rangle=\int_a^b(\bar vLu-uL\bar v)dx=\Big[p(u'\bar v-u\bar v')\Big]_a^b. \tag{5.70}$$

【課堂討論】[▶ 59:41](https://youtu.be/1nelD2AP68E?t=3581) 第一行是內積定義；第二行學生說是 Lagrange 恆等式，講者：「完全對」，它把差換成一個全導數，積分就只剩端點值。[▶ part 2 00:01](https://youtu.be/hgw7iXusEaI?t=1)

最後要證端點項為 0：若 $p(a)=0$ 直接成立；若 $p(a)>0$，$u,\bar v$ 都滿足 $a$ 處的邊界條件，跟上一節一樣的矩陣論證給出 $u(a)\bar v'(a)-\bar v(a)u'(a)=0$。$b$ 端同理。講者讓學生看 p. 252。

### Theorem 5.9.9：本徵值是實數

[▶ part 2 02:20](https://youtu.be/hgw7iXusEaI?t=140)

講者：「我們剛證了它是自伴的，所以本徵值是實數——但課本還是給了證明，因為那個計算很有趣。」他說幾年前教一群想多學微分方程的學生時第一次看到這個。

$Lu=-\lambda\omega u$，$u\ne0$：

$$0=\langle Lu,u\rangle-\langle u,Lu\rangle=\langle-\lambda\omega u,u\rangle-\langle u,-\lambda\omega u\rangle=(\bar\lambda-\lambda)\int_a^b\omega(x)|u(x)|^2dx.$$

講者說 $\omega$ 不是常數，不能直接提出內積外，所以寫成積分；兩個內積都化成 $\int\omega|u|^2$ 乘上 $\lambda$ 或 $\bar\lambda$。[▶ part 2 05:54](https://youtu.be/hgw7iXusEaI?t=354)

$\omega>0$、$u\ne0$，積分為正，所以 $\lambda=\bar\lambda$。∎

【課本補充】這個定理只說本徵值是實數，不保證存在；§5.10 會證正則系統有**無限多個**本徵值。

---

## 10. 加權正交

[▶ part 2 06:27](https://youtu.be/hgw7iXusEaI?t=387) 課本 Theorem 5.9.10。

**定理**：Sturm–Liouville 系統中不同本徵值的本徵函數，對**帶權函數 $\omega$** 的內積正交：

$$Lu=-\lambda_1\omega u,\ Lv=-\lambda_2\omega v,\ \lambda_1\ne\lambda_2\ \Longrightarrow\ \langle u,v\rangle_\omega=\int_a^b\omega(x)u(x)\overline{v(x)}dx=0.$$

講者說證明有點長但直接，沒時間做。

【課本補充】證明：$u_1Lu_2-u_2Lu_1=(\lambda_1-\lambda_2)\omega u_1u_2$；積分，左邊由 Lagrange 恆等式只剩端點項（邊界條件使它為 0），所以 $(\lambda_1-\lambda_2)\int\omega u_1u_2=0$。

**有趣的地方**【口頭】[▶ part 2 08:11](https://youtu.be/hgw7iXusEaI?t=491)：這裡出現**另一種幾何**，反映了 $\omega$——$\omega$ 是 Sturm–Liouville 問題的特徵。「你在定義跟給定微分方程配對的正交性。」權函數不同，什麼叫正交就不同。我們看過的例子權函數多半是 1（sin、cos），所以分不出普通 $L^2$ 內積和「Sturm–Liouville 內積」。「微分方程本身就帶著一個新的幾何世界，你得在裡面理解它的解怎麼行為、怎麼互動。」（這就是第 19 集的加權 $L^2$。）

**為什麼要學這些**【口頭】[▶ part 2 09:17](https://youtu.be/hgw7iXusEaI?t=557)：你可能問：為什麼要學正交、自伴這些？部分答案是：它們幫你理解我們看過的那一整串 PDE 的**共同模式**——解集合的結構彼此相似，因為底下都是同一套 Sturm–Liouville 理論。不是每個問題都是 Sturm–Liouville 型的，「但 Sturm–Liouville 撒的網非常寬」。

---

## 11. 參考書的總結

[▶ part 2 11:39](https://youtu.be/hgw7iXusEaI?t=699) 講者投影他以前教那群學生時用的一本書（較低階的 PDE 書），推薦大家買，「第三版大約 10 美元，很值得」。⚠️ 待確認：講者沒說書名。

書裡的重點（講者念）：

- 三種邊界條件（兩端為 0、導數為 0、週期）的結果整理表——就是講者做過的三個例子；以及配合初始條件的係數積分公式。
- 物理例子：非均勻棒的熱流、非均勻弦的振動、圓對稱的熱流。邊界上函數為 0 是**固定溫度**；導數為 0 是**絕熱**；對振動弦，導數為 0 是**自由端**。
- 書中權函數叫 $\sigma$ 而不是 $\omega$。
- **Sturm–Liouville 定理**（書中的總結）[▶ part 2 15:32](https://youtu.be/hgw7iXusEaI?t=932)：
  1. 本徵值是實數；
  2. 有**無限多個**本徵值，可以排成 $\lambda_1<\lambda_2<\cdots$，有最小的、沒有最大的；
  3. 本徵函數除常數倍外唯一；
  4. 第 $n$ 個本徵函數恰好有 $n-1$ 個零點（講者：「這個我們書上沒看到」）；
  5. 本徵函數構成完備集：任何分段光滑函數都能用本徵函數的廣義 Fourier 級數表示（幾乎處處），在跳躍不連續點收斂到跳躍的平均值；
  6. 不同本徵值的本徵函數對權函數正交；
  7. 本徵值和本徵函數由 **Rayleigh 商**（一個積分）相關。講者：他大學的 PDE 老師好像花了七堂課推它。
- 書中對 Fourier 級數的收斂、發散有具體的論證；也有自伴算子、Lagrange 恆等式（微分形式）、**Green 公式**（積分形式）；Gram–Schmidt 要用權函數做。
- **多維**[▶ part 2 19:10](https://youtu.be/hgw7iXusEaI?t=1150)：二維的 Lagrange 恆等式跟 Green 定理有關；二階導數換成 Laplacian，得到 **Helmholtz 方程** $\nabla^2\varphi+\lambda\varphi=0$。對應定理：本徵值實、無限多、有最小沒有最大，但一個本徵值可以有**多個**本徵函數；仍有完備集和廣義 Fourier 級數；Rayleigh 商裡的積分變成面積分和線積分。

講者：「這部分回答了『我們一開始為什麼要學這些』：它幫我們更深地理解怎麼解微分方程。」[▶ part 2 21:34](https://youtu.be/hgw7iXusEaI?t=1294)

---

## 12. 預告：Green 函數

【口頭】[▶ part 2 22:07](https://youtu.be/hgw7iXusEaI?t=1327) 講者投影他的筆記（會分享）。

**想法**：非齊次問題 $Ly=f$。微分方程課說解 = 齊次解 + 特解。希望有個反算子 $y=L^{-1}f$；但不是真正的反，因為解不唯一（差一個齊次解），最多只能找到一個「代表」。這是做得到的。

**一階**[▶ part 2 22:39](https://youtu.be/hgw7iXusEaI?t=1359)：$y'+py=q$，用積分因子法得公式。把 $p$ 看成給定、$q$ 看成變數，解是 $q$ 對某個函數 $K$ 的積分，$K$ 是積分的差的指數——這就是 **Green 函數**：Green 函數的積分給出微分算子的反算子。

**二階**[▶ part 2 23:46](https://youtu.be/hgw7iXusEaI?t=1426)：用**參數變異法**，$y_1,y_2$ 是齊次解，改寫一下得到：解 = 外力對 Green 函數的積分。所以可以用參數變異法推出 Green 函數的形式。

**Laplace 變換**[▶ part 2 25:33](https://youtu.be/hgw7iXusEaI?t=1533)：取 Laplace 變換、在頻率域解出 $Y$、取反變換：解是 $f$ 跟 $h$ 的摺積，$h$ 是**傳遞函數**（transfer function，工程用語）的反變換。這也是一個 Green 函數：$n$ 階常係數問題的 Green 函數就是傳遞函數的反變換，在 $t-u$ 處取值。他的筆記還推導了摺積公式、算了幾個具體例子。

**一般情況**[▶ part 2 24:55](https://youtu.be/hgw7iXusEaI?t=1495)：對任意微分方程怎麼找這個反算子（Green 函數）？這牽涉到**分佈（distributions）**，也牽涉到變換。講者說下次（週三）會講分佈（第 6 章：分佈是函數的推廣），雖然他很想先講 Fourier 變換；要真正理解分佈，也需要 Fourier 變換。

---

## 13. 一頁速查表

| 項目 | 內容 | 關鍵 |
|---|---|---|
| Basel | $\sum\frac1{n^2}=\frac{\pi^2}6$ | $x^2=\frac13+\sum\frac{4(-1)^n}{n^2\pi^2}\cos n\pi x$ 代 $x=1$ |
| Laplace 方程 | 矩形：cos × cosh/sinh 級數 | 分離變數；邊界條件配係數 |
| d'Alembert | $u=F(x+t)+G(x-t)$ | 左右行波 |
| 正則 S–L | $(pu')'+(q+\lambda\omega)u=0$，$a_1u+a_2u'=0$ 等 | $p,\omega>0$，$a_1^2+a_2^2>0$ |
| 奇異 S–L | $p$ 在端點可為 0；條件改成有界 | |
| 週期 S–L | $u(a)=u(b)$、$u'(a)=u'(b)$ | 例：$1,\cos nx,\sin nx$ |
| Lagrange | $uLv-vLu=\left[p(uv'-vu')\right]'$ | |
| Abel | $p(x)W(x)=$ 常數 | 相乘相減、分部積分 |
| 唯一 | 正則 S–L 本徵函數唯一（差常數） | 邊界條件 ⟹ $W(a)=0$ ⟹ $W\equiv0$ |
| 注意 | $W\equiv0$ ⟹ 相依只對解成立 | $x^2$ 與 $x|x|$ |
| 自伴 | $\langle Lu,v\rangle=\langle u,Lv\rangle$ | 端點項由邊界條件消掉 |
| 實本徵值 | $(\bar\lambda-\lambda)\int\omega|u|^2=0$ | $\omega>0$ |
| 加權正交 | $\int_a^b\omega u_1\bar u_2=0$（$\lambda_1\ne\lambda_2$） | 微分方程帶來自己的幾何 |
| Green 函數 | $y=\int G(x,s)f(s)ds$ | 積分因子／參數變異／傳遞函數的反變換 |

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Green 函數、反微分算子 | 第 31 集（§5.10） |
| 本徵值 $\lambda_n\to\infty$ vs 緊緻算子 $\lambda_n\to0$ | 第 31 集：Green 算子是緊緻的，本徵值是 $1/\lambda_n$（Theorem 5.10.4） |
| Fourier 變換 | 第 31–32 集（§5.11） |
| 分佈 | 第 32 集（第 6 章） |
| Hermite、Legendre 方程是 S–L | 第 33–34 集：量子力學 |

---

## 附：本集一句話總結

> **分離變數把 Laplace、波動、熱方程化成一個個邊界值問題，而這些全是 Sturm–Liouville 系統 $(pu')'+(q+\lambda\omega)u=0$ 的特例：Lagrange 恆等式讓它的算子自伴，所以本徵值是實數、本徵函數在「以 $\omega$ 加權」的內積下正交——微分方程自帶一套幾何；而 Fourier 級數這種工具，甚至能順手算出 $\sum1/n^2=\pi^2/6$。**

---

## ⚠️ 待確認清單

1. [▶ part 2 11:39](https://youtu.be/hgw7iXusEaI?t=699) 講者投影的那本較低階 PDE 參考書（「第三版約 10 美元」、權函數記為 $\sigma$、有 Rayleigh 商與 Helmholtz 方程的章節），講者沒有說出書名。

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-04-14 錄影逐字稿（part 1 whisper large-v3-turbo 轉錄 59:51；part 2 YouTube 自動字幕 28:54）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §5.9 整理；開頭的例題依講者投影的解答之口述。*
