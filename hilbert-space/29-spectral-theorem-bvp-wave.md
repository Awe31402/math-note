---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 29
lecture: Lecture 29
date: 2023-04-07
video: https://youtu.be/LeMR2v-XTAg （part 1）、https://youtu.be/-2xo6P3p9Xo （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.10（書頁 196–201，PDF 頁 215–220）；邊界值問題與波動方程是講者自己的講法（課本 §5.9 的特例）
---

# 第 29 集 · 譜定理概述、邊界值問題、波動方程 [▶ 影片](https://youtu.be/LeMR2v-XTAg)

← 上一集：[28-eigenvectors-finite-dim-review](28-eigenvectors-finite-dim-review.md) ｜ [總目錄](README.md) ｜ 下一集：[30-separation-of-variables-sturm-liouville](30-separation-of-variables-sturm-liouville.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 29 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 52:03，自動字幕）＋ Debnath & Mikusiński §4.10
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Hilbert–Schmidt 定理](#1-hilbertschmidt-定理)
- [2. 有限維類比：零空間 = 列空間的正交補](#2-有限維類比零空間--列空間的正交補)
- [3. 緊緻自伴算子的譜定理](#3-緊緻自伴算子的譜定理)
- [4. 投影分解與算子的函數](#4-投影分解與算子的函數)
- [5. 邊界值問題 vs 初值問題](#5-邊界值問題-vs-初值問題)
- [6. 例 1：X(0) = X(L) = 0](#6-例-1x0--xl--0)
- [7. 例 2：X′(0) = X′(L) = 0](#7-例-2x0--xl--0)
- [8. 例 3：X′(0) = 0、X(L) = 0](#8-例-3x0--0xl--0)
- [9. 波動方程與分離變數](#9-波動方程與分離變數)
- [10. 為什麼這導向分析](#10-為什麼這導向分析)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者的計畫：用大約 20 分鐘談本徵值與譜分解，「也許試著證明定理，保留放棄的權利」；剩下時間解一個微分方程。[▶ 00:35](https://youtu.be/LeMR2v-XTAg?t=35)

| 主題 | 來源 |
|---|---|
| Hilbert–Schmidt 定理 | Theorem 4.10.1，pp. 196–198 |
| 緊緻自伴算子的譜定理 | Corollary 4.10.2–4.10.3，pp. 198–199 |
| 算子的函數；可交換算子 | Definition 4.10.4、Theorem 4.10.8，pp. 199–201 |
| 邊界值問題、波動方程 | 講者的講法 |

---

## 1. Hilbert–Schmidt 定理

[▶ 01:12](https://youtu.be/LeMR2v-XTAg?t=72) 課本 Theorem 4.10.1。

課本的前言：有限維 Hilbert 空間（例如 $\mathbb{C}^n$）中，自伴算子的本徵向量構成 $H$ 的正交基底（線代已知）。下面推廣到無限維。

講者【口頭】：我們在一個奇怪的處境，沒有給緊緻算子適當的定義，也沒深入，但他想讓學生感受它能做到什麼，「某種意義上是部分綜覽模式」。

**定理（Hilbert–Schmidt）**：$A$ 是無限維 Hilbert 空間 $H$ 上的**緊緻自伴**算子。則存在對應**非零**本徵值 $(\lambda_n)$ 的正規正交本徵向量系統 $(u_n)$，使每個 $x\in H$ 都能唯一寫成

$$x=\sum_{n=1}^\infty\alpha_nu_n+v,\qquad\alpha_n\in\mathbb{C},\ v\in\mathcal N(A). \tag{4.39}$$

講者決定**走一遍證明的步驟**（不完全證）[▶ 05:01](https://youtu.be/LeMR2v-XTAg?t=301)：

1. 由 Theorem 4.9.16 和 Corollary 4.9.17，有本徵值 $\lambda_1$ 使 $|\lambda_1|=\sup_{\|x\|\le1}|\langle Ax,x\rangle|$。取正規化本徵向量 $u_1$。
2. $Q_1=\{u_1\}^\perp$，閉子空間。對 $x\in Q_1$：
   $$\langle Ax,u_1\rangle=\langle x,Au_1\rangle=\lambda_1\langle x,u_1\rangle=0$$
   （自伴；$\lambda_1$ 是實數）。所以 $A$ 把 $Q_1$ 映進 $Q_1$。
3. 把 $A$ 限制在 $Q_1$ 上——還是緊緻自伴——再用一次 Theorem 4.9.16：有 $\lambda_2$ 使 $|\lambda_2|=\sup\{|\langle Ax,x\rangle|:x\in Q_1,\|x\|\le1\}$，取 $u_2$。講者說條件「$x\in Q_1$」可以疊在 sup 下面，也可以寫成集合，看記號品味。[▶ 09:33](https://youtu.be/LeMR2v-XTAg?t=573)
4. $Q_2=\{x\in Q_1:x\perp u_2\}$，重複。得 $\lambda_1,\lambda_2,\dots$、$u_1,u_2,\dots$、$Q_n=\{x\in Q_{n-1}:x\perp u_n\}$。
5. **有限情形**[▶ 14:06](https://youtu.be/LeMR2v-XTAg?t=846)：可能在某個 $k$ 時 $\langle Ax,x\rangle=0$ 對所有 $x\in Q_k$。那麼 $x=\alpha_1u_1+\cdots+\alpha_ku_k+v$，$Av=0$，而且 $Ax=\lambda_1\alpha_1u_1+\cdots+\lambda_k\alpha_ku_k$。講者在這步有點卡（學生幫忙），說「到這之前一切都很直接」。
6. **無限情形**[▶ 19:51](https://youtu.be/LeMR2v-XTAg?t=1191)：令 $S$ 是 $u_1,u_2,\dots$ 張成的閉子空間，用正交分解定理（3.6.6）把 $x$ 拆成 $S$ 中的部分和 $S^\perp$ 中的部分 $v$。課本再用半頁證明 $S^\perp$ 中的元素都在零空間裡。講者讓學生自己讀那半頁。

【課本補充】第 6 步的關鍵：$v\in S^\perp\subseteq Q_n$ 對所有 $n$，所以
$$|\langle Av,v\rangle|\le\|v\|^2|\lambda_{n+1}|\to0$$
（Theorem 4.9.19：$\lambda_n\to0$）。所以 $A$ 在 $S^\perp$ 上的二次型是 0，由 Theorem 4.4.14 範數是 0，$Av=0$。

---

## 2. 有限維類比：零空間 = 列空間的正交補

【口頭】[▶ 20:58](https://youtu.be/LeMR2v-XTAg?t=1258)

講者想說證明在推廣有限維的什麼：線性變換的「基本子空間」。

$T:V\to V$，**核** $\ker T=\{x:Tx=0\}$，**像** $\operatorname{im}T$。$T$ 的矩陣 $A$（「先壓下談基底的慾望」）：$\operatorname{Null}(A)=\{x\in\mathbb{R}^n:Ax=0\}$。

**例**[▶ 24:42](https://youtu.be/LeMR2v-XTAg?t=1482)：向量 $s_1,\dots,s_k$ 排成矩陣 $S=[s_1|\cdots|s_k]$。$\operatorname{span}\{s_i\}=\operatorname{Col}(S)$。它的正交補：

$$x\perp s_i\ \forall i\iff s_i^Tx=0\ \forall i\iff S^Tx=0.$$

所以

$$\operatorname{Col}(S)^\perp=\operatorname{Null}(S^T).$$

講者：他覺得證明的後半就是這件事的無限維類比：把本徵向量張成的閉子空間取正交補，再論證它落在算子的零空間裡。「這是一種感覺，不是嚴格的說法，也許我錯了。」[▶ 28:24](https://youtu.be/LeMR2v-XTAg?t=1704)

---

## 3. 緊緻自伴算子的譜定理

[▶ 29:02](https://youtu.be/LeMR2v-XTAg?t=1742) 課本 Corollary 4.10.2。

**推論（緊緻自伴算子的譜定理）**：$A$ 是無限維 Hilbert 空間 $H$ 上的緊緻自伴算子。則 $H$ 有一個由 $A$ 的本徵向量組成的**完備正規正交系統** $\{v_1,v_2,\dots\}$，而且對每個 $x\in H$，

$$Ax=\sum_{n=1}^\infty\lambda_n\langle x,v_n\rangle v_n, \tag{4.41}$$

$\lambda_n$ 是 $v_n$ 的本徵值。

【課堂討論】[▶ 30:00](https://youtu.be/LeMR2v-XTAg?t=1800) 講者問這跟上一個定理差在哪。學生：把 $A$ 作用在 (4.39) 上，$Av=0$ 就消失了。講者：「我是笨蛋……你只要拿前一個定理乘上 $A$。」

另一個差別[▶ 32:34](https://youtu.be/LeMR2v-XTAg?t=1954)：要得到**完備**的系統，要把 $u_1,u_2,\dots$ 補上 $\mathcal N(A)$ 的一組正規正交基底。零空間裡的向量也是本徵向量（本徵值 0）。$A$ 限制在零空間上仍是 Hilbert 空間上的自伴算子，所以那組基底存在；併起來就得到整個空間的正規正交系統。

---

## 4. 投影分解與算子的函數

### 投影分解

[▶ 34:53](https://youtu.be/LeMR2v-XTAg?t=2093) 課本 Corollary 4.10.3。

$A$ 緊緻自伴，則

$$A=\sum_{n=1}^\infty\lambda_nP_n, \tag{4.42}$$

$P_n$ 是投影到**有限維**子空間的投影。

【課堂討論】[▶ 36:20](https://youtu.be/LeMR2v-XTAg?t=2180) 講者一度很驚訝：這好像說零空間是有限維的？後來想通：式子裡其實還有「$+0\cdot P_0$」（投影到零空間），只是不出現；$\lambda_n$ 是所有**非零**本徵值，它們的本徵空間才是有限維（Theorem 4.9.18）。「這式子對 0 本徵空間什麼也沒說。」

課本：這只是譜定理的另一個版本，但很重要，因為它能自然推廣到更一般的算子，也導出算子的冪和函數的優雅表示。

### 算子的冪與函數

[▶ 39:40](https://youtu.be/LeMR2v-XTAg?t=2380)

投影是**冪等的**：$P_n^2=P_n$（「影子的影子還是影子」）。所以

$$A^2=\sum_n\lambda_nAP_n=\sum_n\lambda_n^2P_n,\qquad A^k=\sum_n\lambda_n^kP_n. \tag{4.43}$$

講者卡在「為什麼 $AP_nx=\lambda_nP_nx$」以及交叉項 $P_mP_n$（$m\ne n$）為什麼是 0，用有限維檢查[▶ 44:54](https://youtu.be/LeMR2v-XTAg?t=2694)：$A=\lambda_1P_1+\lambda_2P_2$，$P_j=u_ju_j^T$，

$$A^2=\lambda_1^2P_1^2+\lambda_1\lambda_2P_1P_2+\lambda_2\lambda_1P_2P_1+\lambda_2^2P_2^2.$$

$P_1P_2=u_1(u_1^Tu_2)u_2^T=0$（正交），$P_j^2=P_j$，所以 $A^2=\lambda_1^2P_1+\lambda_2^2P_2$。講者說他卡住是因為我們跳過了投影那節（§4.7）。

**多項式**[▶ 47:52](https://youtu.be/LeMR2v-XTAg?t=2872)：$p(t)=a_1t+\cdots+a_kt^k$，

$$p(A)=\sum_np(\lambda_n)P_n.$$

（講者一開始寫成 $\lambda_n$ 乘 $p$，學生糾正成 $p(\lambda_n)$。）

【課本補充】常數項必須是 0，否則 $p(\lambda_n)\not\to0$；有常數項時另外加 $a_0I$，但那時 $p(A)$ 不再緊緻。

**Definition 4.10.4（算子的函數）**：$f$ 實值，$f(\lambda)\to0$（$\lambda\to0$）、$f(0)=0$。定義

$$f(A)=\sum_{n=1}^\infty f(\lambda_n)P_n. \tag{4.44}$$

講者：下一頁就用 Maclaurin 級數定義例如 $\sin A=\sum(\sin\lambda_n)P_n$。課本例：$\lambda_n\ge0$ 時 $A^\alpha=\sum\lambda_n^\alpha P_n$，$\alpha=\frac12$ 就是正算子的平方根。

**Theorem 4.10.8**[▶ 50:04](https://youtu.be/LeMR2v-XTAg?t=3004)：兩個**可交換**的緊緻自伴算子 $A,B$，有一組由**共同**本徵向量組成的正規正交系統。講者：這對量子力學很重要。

**§4.11 無界算子**[▶ 50:36](https://youtu.be/LeMR2v-XTAg?t=3036)：講者說他沒什麼要說的；之後要看的例子大概會涉及無界算子，主要例子是**微分算子**（p. 207 Example 4.11.13，$A=i\frac{d}{dt}$）。「學期是有限的，總得有東西讓步。」

講者【口頭】[▶ 52:26](https://youtu.be/LeMR2v-XTAg?t=3146)：他越來越欣賞這本書，再投入幾百小時能學到很多；羨慕學生能做作業。也許將來學校開數學碩士，他就能正式教這門課。

---

## 5. 邊界值問題 vs 初值問題

[▶ 54:21](https://youtu.be/LeMR2v-XTAg?t=3261) 講者：「我一直在等這個微分方程。」他說自己是「憑心教」，沒帶筆記。

- **初值問題**：所有資料都給在**同一個**自變數值上。有很好的存在定理（第 9 集）。
- **邊界值問題（boundary value problem, BVP）**：資料給在**兩個不同**的自變數值（時間或位置）上。解集合的結構很不一樣。

講者先試 $y''+y=0$、$y(0)=0$、$y(L)=0$，解 $y=c_1\cos x+c_2\sin x$。學生問複數解：$e^{ix}$ 的實部是 cos、虛部是 sin，我們找實解。$y(0)=c_1=0$；$y(L)=c_2\sin L=0$，所以 $c_2=0$（什麼都沒有）或 $L=n\pi$。講者發現這不是他想要的形式，「我們重來，要更貪心」：在方程裡放一個參數。[▶ part 2 00:50](https://youtu.be/-2xo6P3p9Xo?t=50)

---

## 6. 例 1：X(0) = X(L) = 0

[▶ part 2 01:28](https://youtu.be/-2xo6P3p9Xo?t=88)

$$X''+KX=0,\qquad X(0)=X(L)=0,\qquad L>0.$$

講者說：要分情況討論 $K$ 的正負，正的寫成某數的平方、負的寫成負的某數的平方，「不這麼做就會埋在根號的 sin、cos 裡」。[▶ part 2 08:43](https://youtu.be/-2xo6P3p9Xo?t=523)

**$K>0$**：$K=k^2$，$X=c_1\cos kx+c_2\sin kx$。$X(0)=c_1=0$；$X(L)=c_2\sin kL=0$。$c_2=0$ 太無聊，所以 $kL=n\pi$（$n\in\mathbb{N}$；$n=0$ 又是零解，負的 $n$ 只給出負號）：

$$k=\frac{n\pi}L,\qquad K=\frac{n^2\pi^2}{L^2},\qquad X_n(x)=\sin\frac{n\pi x}{L}.$$

**$K=0$**[▶ part 2 07:35](https://youtu.be/-2xo6P3p9Xo?t=455)：$X''=0$，$X=ax+b$。$X(0)=b=0$、$X(L)=aL=0$，所以 $X=0$。

**$K<0$**：$K=-\beta^2$（$\beta>0$），$X''-\beta^2X=0$。

$$X=c_1\cosh\beta x+c_2\sinh\beta x.$$

講者：特徵根 $\pm\beta$ 給 $e^{\pm\beta x}$，但對邊界值問題那很糟；用 cosh、sinh 好得多，因為 $\cosh0=1$、$\sinh0=0$。[▶ part 2 09:18](https://youtu.be/-2xo6P3p9Xo?t=558)

$X(0)=c_1=0$；$X(L)=c_2\sinh\beta L=0$。【課堂討論】$c_2=0$ 無聊；$\sinh\beta L=0$ 只有 $\beta L=0$，但 $\beta>0$、$L>0$。理由：$(\sinh x)'=\cosh x\ge1$，sinh 嚴格遞增，只有一個零點（也可以說反雙曲正弦對所有輸入有定義，$\beta L=\sinh^{-1}0=0$）。所以只有零解。

**結論**[▶ part 2 12:49](https://youtu.be/-2xo6P3p9Xo?t=769)：非零解只有

$$X_n=\sin\frac{n\pi x}L,\qquad K=\frac{n^2\pi^2}{L^2}\ (n=1,2,\dots).$$

這些叫**本徵解**（eigen solutions）。講者【口頭】：第 5、6 章用的「本徵值」跟我們之前的用法不完全一樣，「有點像代數數論裡的『範數』——類似的想法，但不是同一個定義」。

**這有多奇怪**【口頭】[▶ part 2 03:12](https://youtu.be/-2xo6P3p9Xo?t=192)：微分方程課裡，寫下方程、給任何初值，就有唯一解，一路延伸下去。這裡反過來：先給邊界值，才發現只有**特定的**方程（$K=n^2\pi^2/L^2$）有非零解；對給定的 $L$，絕大多數 $K$ 都失敗。

---

## 7. 例 2：X′(0) = X′(L) = 0

[▶ part 2 15:39](https://youtu.be/-2xo6P3p9Xo?t=939)

同一個方程，邊界條件改成導數為 0。

- **$K=0$**：$X=ax+b$，$X'=a=0$，$b$ 沒有限制。所以 **$X_0=1$ 是解**。講者：「這次 $K=0$ 給了我們東西。」
- **$K=-\beta^2<0$**：$X'=c_1\beta\sinh\beta x+c_2\beta\cosh\beta x$（學生提醒鏈鎖律的 $\beta$）。$X'(0)=c_2\beta=0$ ⟹ $c_2=0$；$X'(L)=c_1\beta\sinh\beta L=0$ ⟹ $c_1=0$。沒有解。
- **$K=\beta^2>0$**：$X'=-c_1\beta\sin\beta x+c_2\beta\cos\beta x$。$X'(0)=c_2\beta=0$ ⟹ $c_2=0$；$X'(L)=-c_1\beta\sin\beta L=0$ ⟹ $\beta L=n\pi$。

$$X_n=\cos\frac{n\pi x}L,\qquad K=\frac{n^2\pi^2}{L^2}\ (n=0,1,2,\dots).$$

講者【口頭】[▶ part 2 21:45](https://youtu.be/-2xo6P3p9Xo?t=1305)：他有寫好這一切的筆記，會分享。Nagle–Saff–Snider 只對具體例子做，從不給出「一般故事」；他教了好幾年，發現一直在做同樣的事，「我應該寫成定理」。

---

## 8. 例 3：X′(0) = 0、X(L) = 0

[▶ part 2 22:58](https://youtu.be/-2xo6P3p9Xo?t=1378)

- **$K=-\beta^2<0$**：$X(0)$…… 講者一開始把兩個條件都代到 $X'$ 裡，得到跟例 2 一樣的答案，覺得不對，發現「我應該代進 $X$ 而不是 $X'$」。[▶ part 2 28:22](https://youtu.be/-2xo6P3p9Xo?t=1702) 正確做：$X'(0)=c_2\beta=0$；$X(L)=c_1\cosh\beta L=0$，$\cosh\ge1$，所以 $c_1=0$。沒有解。
- **$K=\beta^2>0$**：$X'(0)=c_2\beta=0$ ⟹ $c_2=0$；$X(L)=c_1\cos\beta L=0$ ⟹ $\beta L=\pm\frac\pi2,\pm\frac{3\pi}2,\dots$。

【課堂討論】更優雅的寫法？學生答：$(2n+1)\frac\pi2$。

$$\beta=\frac{(2n+1)\pi}{2L},\qquad K=\frac{(2n+1)^2\pi^2}{4L^2},\qquad X_n=\cos\frac{(2n+1)\pi x}{2L}\quad(n=0,1,2,\dots).$$

**寓意**[▶ part 2 30:17](https://youtu.be/-2xo6P3p9Xo?t=1817)：每個邊界值問題都附帶一組**無限多個**、由自然數編號的解，而且它們在某個自然的函數空間內積（$\int_0^L$）下**正交**。

---

## 9. 波動方程與分離變數

[▶ part 2 31:25](https://youtu.be/-2xo6P3p9Xo?t=1885) 講者：「讓我們看看 Fourier 和他那類人是怎麼發現需要研究分析的。」

**問題**（速度取 1）：

$$u_{xx}=u_{tt},\qquad 0<x<L.$$

- **邊界條件**：弦兩端固定，$u(0,t)=u(L,t)=0$。
- **初始條件**：初始形狀 $u(x,0)=f(x)$；因為是波動方程，還要初始速度 $u_t(x,0)=g(x)$。

### 分離變數

[▶ part 2 32:29](https://youtu.be/-2xo6P3p9Xo?t=1949)

天才的想法：猜 $u(x,t)=X(x)T(t)$。則 $u_{xx}=X''T$、$u_{tt}=XT''$，代入除以 $XT$：

$$\frac{X''}{X}=\frac{T''}{T}.$$

左邊只跟 $x$ 有關，右邊只跟 $t$ 有關，唯一的可能是兩邊都等於常數，講者「為了自己的方便」叫它 $-K$：

$$X''+KX=0,\qquad T''+KT=0.$$

**邊界條件傳到 $X$**[▶ part 2 36:52](https://youtu.be/-2xo6P3p9Xo?t=2212)：$u(0,t)=X(0)T(t)=0$ 對所有 $t$；$T$ 不是零函數，所以 $X(0)=0$；同理 $X(L)=0$。這正是**例 1**：

$$X_n=\sin\frac{n\pi x}L,\qquad K=\frac{n^2\pi^2}{L^2}.$$

**時間部分**：$T''+\frac{n^2\pi^2}{L^2}T=0$：

$$T_n(t)=a_n\cos\frac{n\pi t}{L}+b_n\sin\frac{n\pi t}L.$$

講者：如果原方程有速度 $v\ne0$，它會進到 $T$ 那邊調整 $K$，修正「時間除以長度」這種量綱上怪怪的地方。

**疊加**[▶ part 2 39:50](https://youtu.be/-2xo6P3p9Xo?t=2390)：

$$u(x,t)=\sum_{n=1}^\infty\left(a_n\cos\frac{n\pi t}L+b_n\sin\frac{n\pi t}L\right)\sin\frac{n\pi x}L.$$

對**任何** $a_n,b_n$，這都滿足方程和邊界條件——一個 sin、cos 的無窮級數。

### 用初始條件定係數

[▶ part 2 41:03](https://youtu.be/-2xo6P3p9Xo?t=2463)

**例**：$f(x)=\sin\frac{\pi x}L$。$t=0$：

$$u(x,0)=\sum_na_n\sin\frac{n\pi x}L=\sin\frac{\pi x}L.$$

sin 函數構成（$L^2$ 中的）正交系統，可以**比較係數**：$a_1=1$，$a_n=0$（$n\ge2$）。$b_n$ 還是自由的。

**初始速度**[▶ part 2 43:40](https://youtu.be/-2xo6P3p9Xo?t=2620)：對 $t$ 微分再代 $t=0$：

$$u_t(x,0)=\sum_nb_n\frac{n\pi}L\sin\frac{n\pi x}L.$$

例：$g(x)=\sin\frac{\pi x}L$（講者說「希望這在物理上合理……我有時即興編題會惹麻煩，有人正式投訴過」）。比較係數：$\frac{\pi}{L}b_1=1$，$b_1=\frac L\pi$，其餘為 0。

**解**[▶ part 2 46:48](https://youtu.be/-2xo6P3p9Xo?t=2808)：

$$u(x,t)=\left(\cos\frac{\pi t}L+\frac L\pi\sin\frac{\pi t}L\right)\sin\frac{\pi x}L.$$

講者：真正的關鍵是 sin、cos 函數系的**正交性**。

### 一般的初始條件

[▶ part 2 47:56](https://youtu.be/-2xo6P3p9Xo?t=2876)

【課堂討論】講者問：如果初始位置和速度不是單純的 sin、cos 呢？學生答：只要是合理的函數，就能用 sin、cos 逼近。講者：對，求它的 **Fourier 展開**（通常是無窮級數），對應選 $a_n,b_n$。要同時給初始位置和初始速度才能定出 $a_n$ 和 $b_n$。

> 以下**不是逐字稿內容**，是依第 21–22 集補上係數公式：$\left\{\sqrt{\frac2L}\sin\frac{n\pi x}L\right\}$ 是 $L^2([0,L])$ 的完備正規正交系統（第 22 集 Example 3.4.18 換尺度），所以
> $$a_n=\frac2L\int_0^Lf(x)\sin\frac{n\pi x}Ldx,\qquad b_n=\frac{2}{n\pi}\int_0^Lg(x)\sin\frac{n\pi x}Ldx.$$

---

## 10. 為什麼這導向分析

【口頭】[▶ part 2 49:10](https://youtu.be/-2xo6P3p9Xo?t=2950)

- 這就是為什麼要懂「用 sin、cos 的和造出函數」。
- 但 sin、cos 無窮和的分析很棘手：一個收斂的 cos 級數，逐項微分可能得到發散的級數——連逐項微分這麼簡單的事都會壞掉。
- sin、cos 收斂到其他函數，隱含了「**幾乎處處**」的想法：兩個只在零集上不同的函數有相同的 Fourier 展開；在跳躍不連續點，Fourier 展開傾向取**跳躍的平均值**。
- 「一旦開始做這種數學，就會引出分析的問題——你會**發現**分析。」這可以追溯到 Fourier。

**熱方程**[▶ part 2 50:18](https://youtu.be/-2xo6P3p9Xo?t=3018)：講者說 Fourier 是對熱方程做的，熱方程更簡單：

$$u_{xx}=ku_t,\qquad\text{一般地}\quad\nabla^2u=k\frac{\partial u}{\partial t}$$

（$\nabla^2$ 是 Laplacian）。描述熱的流動。方法一樣：猜乘積解，代入，然後求初始溫度分佈的 Fourier 展開。之後的課可能會做一個。

**下一步**[▶ part 2 50:52](https://youtu.be/-2xo6P3p9Xo?t=3052)：第 5 章的 **Sturm–Liouville** 問題就是在推廣這些：邊界條件變成未知函數和導數的任意線性組合。講者想先讓學生看過具體的，再看一般的。

講者最後說：「我很驚訝還沒接到電話。」（他兒子的棒球賽可能因雨取消。）

---

## 11. 一頁速查表

| 項目 | 內容 | 關鍵 |
|---|---|---|
| Hilbert–Schmidt | 緊緻自伴：$x=\sum\alpha_nu_n+v$，$v\in\mathcal N(A)$ | 逐次取最大 $|\langle Ax,x\rangle|$；$A$ 保持 $\{u_1\}^\perp$ |
| 有限維類比 | $\operatorname{Col}(S)^\perp=\operatorname{Null}(S^T)$ | |
| 譜定理 | 完備正規正交本徵向量系統；$Ax=\sum\lambda_n\langle x,v_n\rangle v_n$ | 補上 $\mathcal N(A)$ 的基底 |
| 投影分解 | $A=\sum\lambda_nP_n$（非零本徵值、有限維投影） | $P_n^2=P_n$，$P_mP_n=0$ |
| 函數 | $A^k=\sum\lambda_n^kP_n$，$f(A)=\sum f(\lambda_n)P_n$ | $f(0)=0$ |
| 可交換 | 有共同本徵向量 | 量子力學 |
| BVP 例 1 | $X(0)=X(L)=0$：$\sin\frac{n\pi x}L$，$K=\frac{n^2\pi^2}{L^2}$ | $K\le0$ 只有零解（sinh 嚴格遞增） |
| BVP 例 2 | $X'(0)=X'(L)=0$：$\cos\frac{n\pi x}L$（含 $n=0$ 的常數） | |
| BVP 例 3 | $X'(0)=0$、$X(L)=0$：$\cos\frac{(2n+1)\pi x}{2L}$ | $\cos\beta L=0$ |
| 技巧 | $K>0$ 寫 $\beta^2$、$K<0$ 寫 $-\beta^2$；負時用 cosh、sinh | |
| 波動方程 | $u_{xx}=u_{tt}$，固定端點 | $X''/X=T''/T=-K$ |
| 解 | $u=\sum(a_n\cos\frac{n\pi t}L+b_n\sin\frac{n\pi t}L)\sin\frac{n\pi x}L$ | 初始位置定 $a_n$，初始速度定 $b_n$ |

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 邊界值問題的本徵解 | 第 30 集：更多分離變數例子、Sturm–Liouville（§5.9） |
| Fourier 展開求係數 | 第 30 集：$p=2$ 級數求和（Parseval） |
| 微分算子的「反」 | 第 31 集：Green 函數（§5.10） |
| 熱方程 | 第 30–31 集；Fourier 變換（§5.11） |
| 可交換算子有共同本徵向量 | 第 33–34 集：量子力學 |

---

## 附：本集一句話總結

> **緊緻自伴算子可以像有限維對稱矩陣一樣被「對角化」：有完備的正規正交本徵向量系統，算子就是「本徵值乘投影」的和，任何函數都能這樣作用在算子上；而這套理論的原型就是邊界值問題——$X''+KX=0$ 加上兩端條件，只有 $K=n^2\pi^2/L^2$ 之類的本徵值才有非零解，本徵函數 sin、cos 互相正交，波動方程的解就是它們的級數，係數由初始條件的 Fourier 展開決定。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-04-07 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 52:03）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.10 整理；邊界值問題與波動方程依講者口述。*
