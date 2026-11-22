---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 23
lecture: Lec 11-2 Spectral Representation — Finite-Order Systems and State Variables (1/3)
date: 待補
video: https://youtu.be/su9sXeQNtjI
notes: Papoulis & Pillai 4th ed. §11-2 Finite-Order Systems and State Variables（式 (11-10)–(11-33)，pp. 502–507；Example 11-5、11-6）；§9-3 Vector spectra 式 (9-169)–(9-171)，p. 417
---

# 第 23 集 · Lec 11-2 (1/3)：狀態變數系統、矩陣指數、高維 Theorem 9-4、有限階過程的自相關由極點決定 [▶ 影片](https://youtu.be/su9sXeQNtjI)

← 上一集：[22](22-factorization-innovations-minimum-phase-regular-process.md) ｜ [總目錄](README.md) ｜ 下一集：[24](24-discrete-finite-order-processes-partial-fraction.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 23 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（47:31，whisper large-v3-turbo）＋ Papoulis §11-2（pp. 502–507）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【Q&A】` 學生提問
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「state variable」→「state variable／StateVariable」，「Laplace transform」→「Lapartian Form」，「Taylor」→「胎肉／Tiler」，「eigenvalue／eigenvector／eigenmatrix」→「eigenvalue／eigenvector／eigenmetric」，「impulse response」→「imput／Input／Import Response」，「Hermitian transpose」→「hermission transpose」，「dagger」→「匕首」，「complex conjugate」→「complet control gate／ComplicatedCountry」，「filter bank」→「Filter Bank」，「MIMO」→「MIMO」，「Hurwitz polynomial」→「Hervis／Heart with／Hervitz Polynomial」，「left half plane」→「Left have plan」，「pole」→「Pore／paw／por」，「convolution」→「combolution」，「causal」→「causal」，「discrete」→「discreet」，「whitening」→「whightening」，「Paley–Wiener」→「(前集)」，「偏微分方程」（指常微分方程）→「偏微方程式」。以下一律用正確的字。

> **接上一集**：上一集講頻譜分解與最小相位。§11-2 討論**有限階系統** (finite-order systems)：系統內部有**狀態變數** (state variable)，像一個有限狀態機。重點是：有限階過程的自相關、功率頻譜**完全由極點的位置決定**，所以控制和濾波器設計的人那麼重視極點、零點放在哪裡。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 開頭：回答上一集的兩個問題](#1-開頭回答上一集的兩個問題)
- [2. 狀態變數系統](#2-狀態變數系統)
- [3. 轉移矩陣：$\Phi(s)=(sI-A)^{-1}$](#3-轉移矩陣phisis-a-1)
- [4. 矩陣函數：$e^{At}$ 是什麼意思](#4-矩陣函數eat-是什麼意思)
- [5. 整個系統的脈衝響應與高維 Theorem 9-4](#5-整個系統的脈衝響應與高維-theorem-9-4)
- [6. 微分方程就是有狀態的系統](#6-微分方程就是有狀態的系統)
- [7. 有限階過程](#7-有限階過程)
  - [7.1 定義：Hurwitz 多項式](#71-定義hurwitz-多項式)
  - [7.2 脈衝響應由極點決定](#72-脈衝響應由極點決定)
  - [7.3 頻譜拆成相加：$S=S^+(s)+S^+(-s)$](#73-頻譜拆成相加ss-ss-s)
  - [7.4 例子](#74-例子)
  - [7.5 另一個算法：$R=l*l(-\tau)$](#75-另一個算法rll-tau)
- [8. 離散時間版本（開頭）](#8-離散時間版本開頭)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 回答上一集的問題 | [▶ 08:13](https://youtu.be/su9sXeQNtjI?t=493) | — |
| 狀態變數、轉移矩陣 | [▶ 00:00](https://youtu.be/su9sXeQNtjI?t=0) | 式 (11-10)–(11-18)，pp. 503–504 |
| 矩陣函數 | [▶ 06:07](https://youtu.be/su9sXeQNtjI?t=367) | 無（線性代數） |
| 整體系統、高維 Theorem 9-4 | [▶ 15:26](https://youtu.be/su9sXeQNtjI?t=926) | 式 (11-19)–(11-21)、(9-170)、(9-171) |
| 微分方程 | [▶ 19:36](https://youtu.be/su9sXeQNtjI?t=1176) | 式 (11-22)–(11-24)，pp. 504–505 |
| 有限階過程 | [▶ 24:37](https://youtu.be/su9sXeQNtjI?t=1477) | 式 (11-25)–(11-30)、Example 11-5、11-6，pp. 505–506 |
| 離散時間 | [▶ 42:05](https://youtu.be/su9sXeQNtjI?t=2525) | 式 (11-31)–(11-33)，pp. 506–507 |

---

## 1. 開頭：回答上一集的兩個問題

【Q&A】[▶ 08:13](https://youtu.be/su9sXeQNtjI?t=493) 好幾位同學問上一集的兩個推導步驟：

**(1) Paley–Wiener 證明裡為什麼變兩倍？** 小於 1 的部分是負的，大於等於 1 的部分是正的：
$$\int|\log S|=-\int_{S<1}\log S+\int_{S\ge1}\log S.$$
把第一項補成整個區域：$-\int_{S<1}\log S=-\int\log S+\int_{S\ge1}\log S$，所以大於等於 1 的部分出現兩次，係數 2。老師說應該滿直觀的，只是當時直接寫了兩倍。（這個定理重要，因為是 if and only if：$S$ 和 $\log S$ 都可積 ⇔ regular。）

**(2) 轉移矩陣那一步怎麼來的？** 見第 3 節（老師在這裡把推導重講了一次）。

---

## 2. 狀態變數系統

[▶ 00:00](https://youtu.be/su9sXeQNtjI?t=0) 系統內部有一個**狀態** (state)，線性的，像 finite state machine。輸入、輸出都可以是高維的。

例：輸出 $Y$ 是狀態變數 $Z$ 和輸入 $X$ 的線性組合。$Z$ 不是我們要的輸出，也不是看到的輸入，是系統**內部**的狀態；在不同狀態下，輸入輸出的關係不一樣。

**最常用的定義方式是用微分**：微分代表變化——微分是正的，狀態從 0 變 1 變 2 越來越大；是負的，往小的方向走。狀態的微分是「前一刻狀態」和「輸入」的線性組合：

> **狀態變數系統**（線性、時不變、實數、因果）：
> $$\frac{dZ(t)}{dt}=AZ(t)+BX(t)\qquad\text{(11-10a)}$$
> $$Y(t)=CZ(t)+DX(t)\qquad\text{(11-10b)}$$
> 維度：$X$ 是 $m\times1$、$Y$ 是 $r\times1$、$Z$ 是 $n\times1$；$A$ 是 $n\times n$、$B$ 是 $n\times m$、$C$ 是 $r\times n$、$D$ 是 $r\times m$。

- **階數** (order)：狀態變數的維度 $n$——狀態變化越多，系統越複雜。
- 最重要的優點：整個是**線性**系統，很好分析。

【課本補充】p. 502：系統在 $t=t_0$ 的「狀態」，就是一組有限個參數，決定了過去的輸入（$t<t_0$）對未來輸出（$t>t_0$）的影響；$Z(t_0)=0$ 叫零狀態 (zero state)。狀態向量不唯一。

---

## 3. 轉移矩陣：$\Phi(s)=(sI-A)^{-1}$

[▶ 03:03](https://youtu.be/su9sXeQNtjI?t=183) 先看內部子系統：輸入 $U(t)=BX(t)$，輸出 $Z(t)$：$\frac{dZ}{dt}-AZ=U$。假設它的脈衝響應是 $\Phi$（$n\times n$，叫**轉移矩陣** transition matrix）。

不在時域分析，**轉到 Laplace 轉換**：$Z(s)=\Phi(s)U(s)$。

**高維時順序不能對調**【口頭】：老師把每個維度都寫出來（$n\times n$ 後面要接 $n\times1$，$n\times1$ 不能接在前面）。一維時可以任意對調，高維時順序很重要。

**推導**：
1. Laplace：微分就是 $s$（$j\omega$ 換成 $s$；積分是 $\frac1s$，電路學也用）：
$$sZ(s)=AZ(s)+U(s).$$
2. 代入 $Z=\Phi U$：$s\Phi U=A\Phi U+IU$。
3. 移項：$(sI-A)\Phi U=IU$。
4. $U$ 可以是**任意值**（$(1,0)$、$(0,1)$、$(2,0)$、$(1,-1)$……任意組合），線性，所以兩邊的矩陣要相等：$(sI-A)\Phi=I$。
5. 假設反矩陣存在：
$$\Phi(s)=(sI-A)^{-1}\qquad\text{(11-17)}.$$

**回到時域**：一維時 $\frac{1}{s-a}\leftrightarrow e^{at}U(t)$（上一集做過，例如 $\frac{1}{\alpha+j\omega}\leftrightarrow e^{-\alpha t}U(t)$）；高維也對：
$$\Phi(t)=e^{At},\quad t>0\qquad\text{(11-18)}.$$
$t>0$ 才有值，因為是**因果**的——不是亂寫的。

【課本補充】(11-16)：$\frac{d\Phi}{dt}-A\Phi=\delta(t)I_n$。$\varphi_{ji}(t)$ 是第 $i$ 個輸入是 $\delta$、其他為 0 時，第 $j$ 個狀態變數的值。每個元素是指數的和 $\sum_kp_{ji,k}(t)e^{s_kt}$，$s_k$ 是 $A$ 的特徵值，$p$ 是次數等於重數的多項式。

---

## 4. 矩陣函數：$e^{At}$ 是什麼意思

[▶ 06:38](https://youtu.be/su9sXeQNtjI?t=398) 老師說大一線性代數應該教過，有些同學可能忘了，給個定義。

**原始定義：Taylor 展開。** 矩陣自己乘自己（整數次方）都是 well-defined 的，所以 Taylor 展開可以定義：
$$e^{At}=\sum_{k=0}^{\infty}\frac{(At)^k}{k!}.$$
這個定義**不管**矩陣有沒有特徵值、特徵向量、反矩陣都可以用，只是計算麻煩。（矩陣一定要是**方**的：$2\times2$、$3\times3$，不能是 $2\times1$。）

**可對角化時**：若特徵向量組成的矩陣 $S$ 可逆（$A=S\Lambda S^{-1}$），任何函數 $f$ 代矩陣就是把特徵值代進 $f$、左右乘 $S$、$S^{-1}$：
$$f(A)=S\begin{pmatrix}f(\lambda_1)&&\\&f(\lambda_2)&\\&&\ddots\end{pmatrix}S^{-1}.$$
例：$e^{At}=S\,\text{diag}(e^{\lambda_1t},e^{\lambda_2t},\dots)S^{-1}$；$\log A$ 也可以這樣定義。
- 若特徵向量不夠（例如某個 $3\times3$ 矩陣只有一個特徵向量），就不能這樣算，回到 Taylor 展開（例如 $\log$ 在 1 附近的 Taylor 展開，裡面只要矩陣的整數次方）。

---

## 5. 整個系統的脈衝響應與高維 Theorem 9-4

[▶ 15:26](https://youtu.be/su9sXeQNtjI?t=926) 回到 $Y$ 和 $X$ 的關係。線性關係（映射可微）一定可以用卷積表示；注意順序都不能對調（輸入 $m$ 維、輸出 $r$ 維、狀態 $n$ 維，三個可以完全不同）。

$$Y=C\cdot\Phi*(BX)+DX\ \Rightarrow\ H(t)=Ce^{At}B+\delta(t)D,\qquad H(s)=C(sI-A)^{-1}B+D\qquad\text{(11-19)}.$$
（$X$ 只能放在最後面，前面就是脈衝響應。）

**高維的 Theorem 9-4**（課本沒這樣整理）[▶ 17:32](https://youtu.be/su9sXeQNtjI?t=1052)：

> $$S_{XY}(\omega)=S_{XX}(\omega)H^\dagger(\omega),\qquad S_{YY}(\omega)=H(\omega)S_{XX}(\omega)H^\dagger(\omega).$$

- $\dagger$（dagger，匕首符號）：**Hermitian transpose**——轉置加共軛。$H$ 是 $r\times m$，$H^\dagger$ 是 $m\times r$，維度才對：$S_{XY}$ 是 $m\times r$ = $(m\times m)(m\times r)$。
- 一維時隨便寫；**高維時順序是 $H\,S\,H^\dagger$**，$S$ 夾在中間。
- 用途：例如 MIMO 的線性 filter bank，有兩個輸入、三個輸出，要看輸入和輸出的頻譜關係。
- $s$ 域：$j\omega$ 換成 $s$，共軛的地方多一個負號。

【課本補充】Papoulis 式 (9-169)–(9-171)，p. 417：$S_{XY}(\omega)=S_{XX}(\omega)\bar H^\dagger(\omega)$，$S_{YY}(\omega)=\bar H(\omega)S_{XY}(\omega)$，$S_{YY}=\bar HS_{XX}\bar H^\dagger$——(9-149) 推廣到多端系統。

**例**：$m=r=n$，$B=C=I$、$D=0$。則 $\frac{dZ}{dt}=AZ+X$、$Y=Z$，也就是 $\frac{dY}{dt}-AY=X$，$H(s)=(sI-A)^{-1}$（式 (11-20)）。

> 任何輸入輸出有**微分關係**的系統，都可以想像成透過一個**狀態**在控制。以後會看到很多系統的輸入輸出是微分定義的，尤其在離散時間。

【課本補充】(11-21)：$S_{XY}(s)=S_{XX}(s)(-sI-A)^{-1}$，$S_{YY}(s)=(sI-A')^{-1}S_{XY}(s)$。

---

## 6. 微分方程就是有狀態的系統

[▶ 21:07](https://youtu.be/su9sXeQNtjI?t=1267) 常見的系統：

$$y^{(n)}(t)+a_1y^{(n-1)}(t)+\cdots+a_ny(t)=x(t)\qquad\text{(11-22)}.$$

直接解當然可以；線性系統的觀點是想像它有一個**狀態**：
$$\mathbf{z}=\left(y,\ y',\ y'',\dots,y^{(n-1)}\right)^T.$$
狀態的微分 $\mathbf{z}'=(y',y'',\dots,y^{(n)})$ 只是把 $\mathbf{z}$ **平移**一格，最後一項由方程式決定：
$$A=\begin{pmatrix}0&1&\cdots&0\\0&0&\ddots&\vdots\\\vdots&&&1\\-a_n&-a_{n-1}&\cdots&-a_1\end{pmatrix},\quad B=\begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix},\quad C=(1,0,\dots,0),\quad D=0.$$

**為什麼這樣描述有好處**【口頭】：最重要的是矩陣 $A$ 的**特徵值**。轉移矩陣是 $e^{At}=S\,\text{diag}(e^{\lambda_it})S^{-1}$；特徵值是負的、而且收斂很快，系統就很快趨於 0。**系統的收斂速度由 $A$（它的特徵值）控制**。

整體轉移函數（直接用 Laplace 轉換也解得出來）：
$$H(s)=\frac{1}{s^n+a_1s^{n-1}+\cdots+a_n}.$$

【課本補充】(11-23)、(11-24)：兩邊乘 $x(t-\tau)$、$y(t+\tau)$，得 $R_{yx}^{(n)}+a_1R_{yx}^{(n-1)}+\cdots+a_nR_{yx}=R_{xx}$，$R_{yy}^{(n)}+\cdots+a_nR_{yy}=R_{xy}$——(9-146) 的特例。

---

## 7. 有限階過程

### 7.1 定義：Hurwitz 多項式

[▶ 24:37](https://youtu.be/su9sXeQNtjI?t=1477) 常見的有限階系統，轉移函數都是**多項式除以多項式**（就是 §11-1 分析的東西）。

> **有限階過程** (finite-order process)：innovation filter $L(s)$ 是 $s$ 的有理函數：
> $$S(s)=L(s)L(-s),\qquad L(s)=\frac{b_0s^m+b_1s^{m-1}+\cdots+b_m}{s^n+a_1s^{n-1}+\cdots+a_n}=\frac{N(s)}{D(s)}\qquad\text{(11-25)},$$
> $N(s)$、$D(s)$ 是 **Hurwitz 多項式**：根都在**左半平面**。

為什麼要 Hurwitz？我們要 regular process、要最小相位、要穩定——同一件事。

【課本補充】(11-26)：$X(t)$ 滿足 $x^{(n)}+a_1x^{(n-1)}+\cdots+a_nx=b_0i^{(m)}+\cdots+b_mi$。

### 7.2 脈衝響應由極點決定

[▶ 26:11](https://youtu.be/su9sXeQNtjI?t=1571) 要看這種過程的自相關，一定和**根**有關。設 $m<n$，根（極點）$s_i$ 是單根。為什麼只看分母的根？極點決定濾波器穩不穩定；零點也要在左半平面，是因為還希望倒數也穩定（現在還沒看倒數）。

多項式分之多項式**一定可以拆成部分分式**（高中常做；例如 $\frac{s+8}{s^2+3s+4}=\frac{A}{s-a}+\frac{B}{s-b}$）：
$$L(s)=\sum_{i=1}^{n}\frac{\gamma_i}{s-s_i}\ \Rightarrow\ l(t)=\sum_i\gamma_ie^{s_it}U(t).$$
（$\frac{1}{s-s_i}\leftrightarrow e^{s_it}U(t)$：上一集的兩個例子就是在講這件事——係數保留，只在 $t>0$ 有值。）

老師說：所以有限階（多項式定義的）過程很容易分析：**知道根的位置，就知道它的性質**。

### 7.3 頻譜拆成相加：$S=S^+(s)+S^+(-s)$

[▶ 29:16](https://youtu.be/su9sXeQNtjI?t=1756)

**Step 1：** $S(s)=L(s)L(-s)$，兩個都拆成部分分式：$L(s)=\sum_i\frac{\gamma_i}{s-s_i}$（根在左半平面，Hurwitz），$L(-s)$ 的根就把右半平面的根補回來。

**Step 2：** 乘起來，分母二次、分子一次；**碰到二次就再拆成一次**（分母一次、分子零次最好處理）。整理後定義
$$\alpha_k=\gamma_k\,L(-s_k).$$
- $\alpha_k$ 是常數：$\gamma_k$ 乘上濾波器在**對稱點** $-s_k$ 的值。
- 會不會是極點、衝到無限大？不會。例：極點 $-2,-3$，$L(-s)$ 代的是 $2,3$（右半平面），不是極點，analytic，不是無限大、不是 0、不是不定值。

**Step 3：** 得到
$$S(s)=\sum_{i}\frac{\alpha_i}{s-s_i}+\sum_i\frac{\alpha_i}{-s-s_i}=S^+(s)+S^+(-s)\qquad\text{(11-28)}.$$

> **觀念**：regular 的有限階過程，功率頻譜除了可以**因式分解成相乘** $|L|^2$，還可以**拆成同一個函數的相加** $S^+(s)+S^+(-s)$——反映它是偶函數。上標「+」的意思是：它對應時域 $\tau>0$ 的部分（因果部分）。

**Step 4：回到時域。** $S^+$ 是一次式倒數的和，根還在原來的地方，係數變成 $\alpha_i$：
$$R^+(\tau)=\sum_i\alpha_ie^{s_i\tau}U(\tau)\quad(s_i\ \text{在左半平面，所以收斂}).$$
$S=S^+(s)+S^+(-s)$，所以 $R(\tau)=R^+(\tau)+R^+(-\tau)$，代 $\tau$ 和 $-\tau$ 結果一樣：
$$\boxed{R(\tau)=\sum_{i=1}^{n}\alpha_ie^{s_i|\tau|}}\qquad\text{(11-29)}.$$

> **結論**：regular 有限階過程的自相關**可以拆成兩項的和、左右對稱**；指數由**極點**決定，係數由「對稱點的濾波器值」決定。所以控制領域特別重視根的位置：它決定自相關的樣子，設計的人就調根的位置。

【課本補充】課本的另一個說法：$X(t-\tau)$ 只依賴 $I$ 的過去，所以和 (11-26) 右邊在 $\tau>0$ 時正交，得 $R^{(n)}+a_1R^{(n-1)}+\cdots+a_nR=0$（$\tau>0$，式 (11-27)），所以 $R(\tau)=\sum\alpha_ie^{s_i\tau}$（$\tau>0$），係數可由初值定理決定。

### 7.4 例子

**Example 11-5** [▶ 37:30](https://youtu.be/su9sXeQNtjI?t=2250)：$L(s)=\frac{1}{s+\alpha}$，極點 $-\alpha$（左半平面）。
$$S(s)=\frac{1}{(s+\alpha)(-s+\alpha)}=\frac{1/2\alpha}{s+\alpha}+\frac{1/2\alpha}{-s+\alpha},\qquad R(\tau)=\frac{1}{2\alpha}e^{-\alpha|\tau|}.$$
- $S^+$ 對應 $\frac1{2\alpha}e^{-\alpha\tau}$（$\tau>0$）：只有一半、因果的，「+」有意義。
- 真正的自相關左右完全對稱，就把 $\tau$ 加絕對值。
- 係數 $\alpha_1=\gamma_1L(\alpha)=1\cdot\frac{1}{2\alpha}$。

**Example 11-6** [▶ 38:30](https://youtu.be/su9sXeQNtjI?t=2310)：常見的微分系統
$$x''(t)+3x'(t)+2x(t)=i(t),\qquad R_{ii}=\delta(\tau).$$
$$L(s)=\frac{1}{s^2+3s+2}=\frac{1}{s+1}-\frac{1}{s+2}\quad(\text{極點 }-1,-2;\ \gamma_1=1,\ \gamma_2=-1).$$
$$\alpha_1=\gamma_1L(1)=\frac{1}{2\cdot3}=\frac16,\qquad\alpha_2=\gamma_2L(2)=-\frac{1}{3\cdot4}=-\frac1{12},$$
$$R(\tau)=\frac16e^{-|\tau|}-\frac1{12}e^{-2|\tau|}.$$

老師說【口頭】：看到它在 $s$ 平面的根（$-1$、$-2$），就很清楚它的行為——**極點決定收斂速度**。將來看別人設計的濾波器，把極點畫出來，就比較有感覺它代表的物理意義：做出來收斂快慢、統計性質都很清楚。真正要記得的是**極點、零點的位置和統計行為的關係**，不是這些數學。

【課本補充】課本對 Example 11-6 的算法：由 (11-27) $R''+3R'+2R=0$，$R=c_1e^{-\tau}+c_2e^{-2\tau}$（$\tau>0$）；用 $S(s)=\frac{s/12+1/4}{s^2+3s+2}+\frac{-s/12+1/4}{s^2-3s+2}$ 和初值定理求 $R(0)=\lim sS^+(s)=\frac1{12}=c_1+c_2$、$R'(0^+)=0=-c_1-2c_2$，得同樣結果。

### 7.5 另一個算法：$R=l*l(-\tau)$

[▶ 40:32](https://youtu.be/su9sXeQNtjI?t=2432) 有同學問：能不能直接算，不要透過這麼複雜的分析？當然可以：
$$R(\tau)=E\left[\int l(u)I(t+\tau-u)du\int l(v)I(t-v)dv\right]=\iint l(u)l(v)\delta(\tau-u+v)\,du\,dv=\int_0^\infty l(|\tau|+\alpha)l(\alpha)\,d\alpha.$$
白雜訊的 delta 讓兩個積分消掉一個，就是濾波器自己和自己的卷積；代 $-\tau$ 和 $\tau$ 一樣。有些課本習題用這個方法證。

【課本補充】(11-30)：$R(\tau)=l(\tau)*l(-\tau)=\int_0^\infty l(|\tau|+\alpha)l(\alpha)d\alpha$。

---

## 8. 離散時間版本（開頭）

[▶ 42:05](https://youtu.be/su9sXeQNtjI?t=2525) 了解連續時間，離散的就完全是複製。差別：$s$ 域換成 $z$ 域；根要在**單位圓內部**（不是左半平面）；沒有微分——**下一個時間的狀態由前一個時間的狀態決定**。

> $$Z[k+1]=AZ[k]+BX[k],\qquad Y[k]=CZ[k]+DX[k]\qquad\text{(11-31)}.$$
> 系統穩定 ⇔ $A$ 的特徵值都在單位圓內。

推導完全一樣：$z\Phi(z)U(z)=A\Phi(z)U(z)+U(z)$，$U$ 任意 ⇒ $\Phi(z)=(zI-A)^{-1}$，時域 $A^k$（因果，$k\ge0$）；整體
$$H(z)=C(zI-A)^{-1}B+D,\qquad H[k]=C\Phi[k]B+\delta[k]D\qquad\text{(11-32), (11-33)}.$$

老師說：之後會多討論離散時間——大部分時候面對的都是離散過程（數位通訊、數位時代）；類比還是很重要，但會設計類比的人比較少。

**離散有限階過程很好實作** [▶ 45:44](https://youtu.be/su9sXeQNtjI?t=2744)：例如 $L(z)=\frac{b_0}{1+a_1z^{-1}+\cdots+a_Nz^{-N}}$，實作公式就是把 $X[n],X[n-1],X[n-2],\dots$ 乘係數加起來等於 innovation 的輸入，只要加延遲就好。離散的問題比較少（上一集的 whitening filter 離散都沒問題；連續的微分器、積分器才有爭議）。多項式的根要在單位圓內，濾波器才是穩定的。

（AR、MA 等離散有限階過程的細節在下一集。）

---

## 9. 一頁速查表

### 狀態變數系統

| | 連續 | 離散 |
|---|---|---|
| 狀態方程 | $Z'=AZ+BX$ | $Z[k+1]=AZ[k]+BX[k]$ |
| 輸出 | $Y=CZ+DX$ | $Y[k]=CZ[k]+DX[k]$ |
| 轉移矩陣 | $\Phi(s)=(sI-A)^{-1}$，$\Phi(t)=e^{At}U(t)$ | $\Phi(z)=(zI-A)^{-1}$，$A^k$ |
| 系統函數 | $H(s)=C(sI-A)^{-1}B+D$ | $H(z)=C(zI-A)^{-1}B+D$ |
| 穩定 | $A$ 特徵值在左半平面 | 在單位圓內 |

- 關鍵：$(sI-A)\Phi U=IU$，$U$ 任意 ⇒ $(sI-A)\Phi=I$。
- $f(A)=S\,\text{diag}(f(\lambda_i))S^{-1}$（可對角化）；否則用 Taylor 展開。
- 高維 Theorem 9-4：$S_{XY}=S_{XX}H^\dagger$，$S_{YY}=HS_{XX}H^\dagger$（順序不能換）。
- $n$ 階微分方程 ⇔ 狀態 $(y,y',\dots,y^{(n-1)})$，$A$ 是伴隨矩陣，$H=\frac{1}{s^n+a_1s^{n-1}+\cdots+a_n}$。

### 有限階過程（$L=N/D$，Hurwitz）

- $L=\sum\frac{\gamma_i}{s-s_i}$，$l(t)=\sum\gamma_ie^{s_it}U(t)$。
- $S=S^+(s)+S^+(-s)$，$S^+=\sum\frac{\alpha_i}{s-s_i}$，$\alpha_i=\gamma_iL(-s_i)$。
- $R(\tau)=\sum\alpha_ie^{s_i|\tau|}$；也 $=l(\tau)*l(-\tau)$。
- 例：$\frac1{s+\alpha}\to\frac1{2\alpha}e^{-\alpha|\tau|}$；$x''+3x'+2x=i\to\frac16e^{-|\tau|}-\frac1{12}e^{-2|\tau|}$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 離散有限階過程 | 下一集：AR、MA、ARMA，Yule–Walker 方程 |
| $R=\sum\alpha_ie^{s_i\lvert\tau\rvert}$ | §12-2 參數化頻譜估計 |
| 狀態變數 | §13-4 Kalman 濾波器（課程沒排） |
| 極點決定收斂 | 濾波器設計 |

---

## 附：本集一句話總結

> **有狀態的線性系統 $Z'=AZ+BX$、$Y=CZ+DX$ 的系統函數是 $C(sI-A)^{-1}B+D$，任何微分方程都能看成這種系統；有限階過程的頻譜可以拆成 $S^+(s)+S^+(-s)$，自相關 $R(\tau)=\sum\alpha_ie^{s_i|\tau|}$ 完全由極點 $s_i$ 和對稱點的濾波器值 $\alpha_i=\gamma_iL(-s_i)$ 決定——所以設計系統的人才那麼在乎極點放在哪裡。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 11-2 (1/3) 錄影逐字稿（whisper large-v3-turbo，47:31）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
