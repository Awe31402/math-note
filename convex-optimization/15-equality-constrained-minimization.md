---
course: Stanford EE364A Convex Optimization I（2023）
episode: 15
lecture: Lecture 15
date: 待補
video: https://youtu.be/zVO4ccvrwrI
notes: 《Convex Optimization》§9.6–9.7（書頁 496–513，PDF 頁 510–527）；第 10 章（書頁 521–558，PDF 頁 535–572）；§11.1（書頁 561–562，PDF 頁 575–576）
---

# 第 15 集 · Lecture 15：等式約束最小化、不可行起點 Newton 法 [▶ 影片](https://youtu.be/zVO4ccvrwrI)

← 上一集：[14-newton-method](14-newton-method.md) ｜ [總目錄](README.md) ｜ 下一集：[16-interior-point-methods](16-interior-point-methods.md) →

> **課程**：Stanford EE364A Convex Optimization I，2023 — 第 15 集
> **講者**：Stephen Boyd
> **來源**：YouTube 錄影逐字稿（1:17:08，人工字幕 en-US）＋ Boyd & Vandenberghe《Convex Optimization》§9.6–9.7、第 10 章、§11.1
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：自和諧](#1-複習自和諧)
- [2. 利用 Hessian 結構](#2-利用-hessian-結構)
- [3. 等式約束最小化](#3-等式約束最小化)
  - [3.1 最佳性條件與 KKT 矩陣](#31-最佳性條件與-kkt-矩陣)
  - [3.2 消去等式約束](#32-消去等式約束)
- [4. 有等式約束的 Newton 法](#4-有等式約束的-newton-法)
- [5. 不可行起點 Newton 法](#5-不可行起點-newton-法)
- [6. 解 KKT 系統](#6-解-kkt-系統)
- [7. 例：解析中心的三種方法](#7-例解析中心的三種方法)
- [8. 例：網路流最佳化](#8-例網路流最佳化)
- [9. 例：矩陣變數](#9-例矩陣變數)
- [10. 預告：不等式約束與對數障礙](#10-預告不等式約束與對數障礙)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 自和諧（複習）、利用 Hessian 結構 | §9.6、§9.7.2 |
| 等式約束問題、KKT 矩陣、消去 | §10.1 |
| 有等式約束的 Newton 法 | §10.2 |
| 不可行起點 Newton 法 | §10.3 |
| 解 KKT 系統、例子 | §10.4 |
| 不等式約束問題（開頭） | §11.1 |

---

## 1. 複習：自和諧

[▶ 00:05](https://youtu.be/zVO4ccvrwrI?t=5)

- 目的：做一個像 Newton 法本身一樣**仿射不變**的收斂分析，修正「實作比數學分析更精緻」的尷尬。
- 分析取決於**三階導數多大**（Hessian 移動時變多快）。最直覺的 $|f'''|$ 不仿射不變；要仿射不變，就**必然**得到 $|f'''|\le2(f'')^{3/2}$（2 可以換別的數）。
- 很多我們用的函數自和諧（不是全部）。重做分析後：「**我沒辦法嘲笑它**」——假設裡沒有不可知的東西，只有「自和諧」；度量用 $\lambda$（仿射不變的梯度大小）。「如果你寫了這麼漂亮的演算法，最後的收斂判斷卻用梯度範數，恭喜，它現在微弱地依賴座標變換了。」
- 還有 $p^\star$ 的尷尬，但把 $p^\star$ 換成**任何下界**仍得到上界（下週內點法會處理）。
- 【口頭】[▶ 05:16](https://youtu.be/zVO4ccvrwrI?t=316) 老師和同事的粗略分析得到 375；更仔細的分析（Nesterov–Nemirovski）大概 11；實際斜率大概 2 左右。
- 用途：主要用來**證明內點法收斂**。有人觀察到用自和諧函數的表述實務上比較好，但沒人會強烈主張；一個方法在大量測試問題上表現好，即使不是自和諧也沒人在乎。

---

## 2. 利用 Hessian 結構

[▶ 07:19](https://youtu.be/zVO4ccvrwrI?t=439)（課本 §9.7.2）

「你在最小化光滑函數？」「我在解一串二次最小化問題。」「然後呢？」「二次最小化就是**線性代數**。」所以所有關於帶狀、稀疏的知識都直接插進來。

【口頭】常見錯誤：把 $H$ 形成成**稠密**矩陣——就算裡面一堆 0，數值方法也不一定會利用。要在腦中建立地圖：**哪些應用會產生有結構的 Hessian**。

**可分 + 仿射合成** [▶ 08:50](https://youtu.be/zVO4ccvrwrI?t=530)：

$$f(x)=\sum_{i=1}^n\psi_i(x_i)+\psi_0(Ax+b),\qquad A\in\mathbb{R}^{p\times n}\ (p\ll n)$$

$$H=D+A^TH_0A$$

- 可分函數的 Hessian 是**對角** $D$（幾乎是充要：Hessian 對角 ⟺ 交叉偏導為 0）。
- 所以 $H$ 是**對角加低秩**——「你的線性代數結構中樞應該在閃燈」。
- 天真做法：形成 $n\times n$ 再 Cholesky，每個 Newton 步 $O(n^3)$。
- 利用結構：先 Cholesky 分解 $H_0$（$p^3$），引入新變數 $w=H_0A\Delta x$ 寫成擴大的系統，再消去 $\Delta x$，主導成本是形成一個矩陣，約 $2p^2n$。$p=n/100$ 時省 10,000 倍。

【Q&A】[▶ 14:09](https://youtu.be/zVO4ccvrwrI?t=849) 學生問：引入 $w$ 的動機？答：就是**反消去**（上上集），在利用對角加低秩的結構。

**帶狀 Hessian** [▶ 12:01](https://youtu.be/zVO4ccvrwrI?t=721)

【課堂討論】Hessian 帶狀用文字講是什麼意思？把 $\partial^2f/\partial x_i\partial x_j\ne0$ 叫做 $i,j$ 之間的**交互作用**：帶狀 = 交互作用是**局部的**，$|i-j|$ 小於半帶寬才有。控制、訊號處理整個領域都是。Newton 步的成本？**對 $n$ 線性**。

【課堂討論】[▶ 13:04](https://youtu.be/zVO4ccvrwrI?t=784) 用 Newton 法解一個幾千步、狀態 10 維、5 個輸入的最佳控制問題要多久？直接寫出來可能一兩秒；**懂的話不到一毫秒**。「這是一切的關鍵，你就是得知道。」

---

## 3. 等式約束最小化

[▶ 14:39](https://youtu.be/zVO4ccvrwrI?t=879)（課本第 10 章）

「這是做作業需要的內容，你一定得仔細讀課本，只有幾頁。」

$$\text{minimize }f(x)\quad\text{s.t.}\quad Ax=b$$

$f$ 凸、二次連續可微，$A\in\mathbb{R}^{p\times n}$ 列滿秩。

### 3.1 最佳性條件與 KKT 矩陣

$x^\star$ 最佳 $\iff$ 存在 $\nu^\star$ 使

$$\nabla f(x^\star)+A^T\nu^\star=0,\qquad Ax^\star=b$$

（梯度在 $\mathcal{R}(A^T)$ 裡且原始可行；$f$ 凸時充要，「沒有任何附加條件」。）

**等式約束凸二次最小化** [▶ 15:41](https://youtu.be/zVO4ccvrwrI?t=941)：$f(x)=\tfrac12x^TPx+q^Tx+r$，$P\succeq0$。梯度是仿射的，KKT 條件變成**線性方程組**：

$$\begin{pmatrix}P&A^T\\A&0\end{pmatrix}\begin{pmatrix}x^\star\\\nu^\star\end{pmatrix}=\begin{pmatrix}-q\\b\end{pmatrix}$$

左邊叫 **KKT 矩陣**，「出現在我能想到的每個領域：力學、電機……」

- **不是正定的**（是「準半定」quasi-semidefinite）。
- **非奇異 $\iff\mathcal{N}(P)\cap\mathcal{N}(A)=\{0\}$**：若有共同向量同時滿足 $Ax=0$、$Px=0$，就奇異 [▶ 17:12](https://youtu.be/zVO4ccvrwrI?t=1032)。
- 解法之一：**LDLᵀ 分解**（「符號不一樣的 Cholesky」）。

【課本補充】§10.1.1 的其他等價條件：$Ax=0,\ x\ne0\Rightarrow x^TPx>0$；或 $P+A^TA\succ0$。

### 3.2 消去等式約束

[▶ 18:12](https://youtu.be/zVO4ccvrwrI?t=1092)

第 2 週講過：$\{x\mid Ax=b\}=\{Fz+\hat x\mid z\in\mathbb{R}^{n-p}\}$（$\hat x$ 是特解，$\mathcal{R}(F)=\mathcal{N}(A)$，例如對 $A^T$ 做 QR）。得到無約束問題

$$\text{minimize }\tilde f(z)=f(Fz+\hat x)$$

用 Newton 法解；從 $z^\star$ 可以重建 $x^\star$，甚至 $\nu^\star$。

**例：資源分配** [▶ 20:14](https://youtu.be/zVO4ccvrwrI?t=1214)

$$\text{minimize }\sum_{i=1}^nf_i(x_i)\quad\text{s.t.}\quad x_1+\cdots+x_n=b$$

$x_i$ 是分給代理人 $i$ 的資源，$b$ 是總預算，$f_i$ 是代理人 $i$ 的成本。消去 $x_n=b-x_1-\cdots-x_{n-1}$：

$$\text{minimize }\sum_{i=1}^{n-1}f_i(x_i)+f_n\left(b-\sum_{i=1}^{n-1}x_i\right),\qquad F=\begin{pmatrix}I\\-\mathbf{1}^T\end{pmatrix}$$

【課堂討論】[▶ 21:51](https://youtu.be/zVO4ccvrwrI?t=1311) 這個函數的 Hessian？學生：箭頭。老師：很接近但不是——它是**稠密**的。前一項的 Hessian？**對角**。後一項？**秩 1**（$\mathbf{1}\mathbf{1}^T$ 乘一個數）。所以是**對角加秩 1** → **線性時間**。「他們會說『我用 SGD，因為太大了，我有一百萬個變數』——『太可惜了，我手機就能做』。每天都有人不懂這些、說『我試了 NumPy，太慢』。」

【Q&A】[▶ 23:26](https://youtu.be/zVO4ccvrwrI?t=1406) 學生問 $F$ 在哪？答：化簡後的式子就是 $f(Fz+\hat x)$ 寫成自然的形式；$F$ 是 $I$ 疊在 $-\mathbf{1}^T$ 上（$n\times(n-1)$）。

---

## 4. 有等式約束的 Newton 法

[▶ 23:56](https://youtu.be/zVO4ccvrwrI?t=1436)（課本 §10.2）

**Newton 步**：解

$$\begin{pmatrix}\nabla^2f(x)&A^T\\A&0\end{pmatrix}\begin{pmatrix}\Delta x_{\text{nt}}\\w\end{pmatrix}=\begin{pmatrix}-\nabla f(x)\\0\end{pmatrix}$$

**解釋**：
1. **最小化二階近似** [▶ 24:26](https://youtu.be/zVO4ccvrwrI?t=1466)：把 $f$ 做二階 Taylor 展開（常數 + 線性 + 凸二次），在 $A(x+v)=b$ 下最小化——那就是上面的 KKT 系統。
2. **線性化最佳性條件** [▶ 25:00](https://youtu.be/zVO4ccvrwrI?t=1500)：$A(x+\Delta x)=b$ 本來就線性；$\nabla f(x+\Delta x)+A^Tw=0$ 用一階展開 $\nabla f(x)+\nabla^2f(x)\Delta x$ 近似。若 $f$ 真的是二次，走這一步就到最佳解。

**Newton 遞減量** [▶ 26:02](https://youtu.be/zVO4ccvrwrI?t=1562)：$\lambda(x)=\left(\Delta x_{\text{nt}}^T\nabla^2f(x)\Delta x_{\text{nt}}\right)^{1/2}$，Newton 步在 Hessian 度量下的長度。$\tfrac12\lambda^2$ 是走 Newton 步時（若 $f$ 二次就是精確的）**預測的下降量**，實務上是離最佳多遠的很好近似。

**演算法**（可行下降法）[▶ 26:34](https://youtu.be/zVO4ccvrwrI?t=1594)：
- **在解什麼**：等式約束、光滑凸最小化，從**可行**點出發。
- **步驟**：給 $x\in\mathbf{dom}\,f$ 且 $Ax=b$；重複：算 $\Delta x_{\text{nt}}$、$\lambda^2$；若 $\lambda^2/2\le\epsilon$ 停；回溯線搜尋；$x:=x+t\Delta x_{\text{nt}}$。
- 和無約束 Newton 法**一模一樣**，差別只在解的是 KKT 系統。迭代點一直可行、目標一直下降、仿射不變。
- **什麼時候會失敗**：需要一個**可行**的起點（同時 $Ax=b$ 且在定義域內），一般可能要解一個 LP 才找得到。

**不需要新的分析** [▶ 28:05](https://youtu.be/zVO4ccvrwrI?t=1685)：把 Newton 法用在消去後的問題，和直接用這個方法**完全相同**（原始迭代、對偶迭代、$\lambda$ 都一樣），所以收斂證明直接搬過來。

**消去 vs 不消去** [▶ 29:08](https://youtu.be/zVO4ccvrwrI?t=1748)：1000 個變數、100 條約束。消去後解 900 個變數；解 KKT 系統是 1100 個。「$1100^3$ 比 $900^3$ 大。」——「對。但我們會發現**幾乎總是解比較大的系統比較好**。」無結構時當然寧願解小的；**有結構時這一般完全錯誤**，而且不直覺。

---

## 5. 不可行起點 Newton 法

[▶ 30:39](https://youtu.be/zVO4ccvrwrI?t=1839)（課本 §10.3）

和作業直接相關。起點 $x\in\mathbf{dom}\,f$ 但**不必滿足** $Ax=b$。Newton 步：

$$\begin{pmatrix}\nabla^2f(x)&A^T\\A&0\end{pmatrix}\begin{pmatrix}\Delta x\\w\end{pmatrix}=-\begin{pmatrix}\nabla f(x)\\Ax-b\end{pmatrix}$$

- 【口頭】「這大概是 90%–95% 的人實際在用的；你一直在解的問題，ECOS 之類的解法器就在替你做這個。」
- **走一步 $t=1$ 之後就可行**，之後一直可行，基本上等於可行起點的 Newton 法（除了線搜尋和停止準則）。

【Q&A】[▶ 32:14](https://youtu.be/zVO4ccvrwrI?t=1934) 學生問：那實務上是不是先走一步 $t=1$ 再切換回原本的方法？答：不行——**你不一定能走 $t=1$**，例如它可能跑出 $f$ 的定義域。

**原始–對偶解釋**：令 $z=(x,\nu)$（**原始–對偶變數**：上半是原始、下半是對偶），殘差

$$r(x,\nu)=\begin{pmatrix}\nabla f(x)+A^T\nu\\Ax-b\end{pmatrix}$$

線搜尋看的是 $\|r\|_2$，不是函數值。

**演算法**（課本 §10.3.2）[▶ 33:45](https://youtu.be/zVO4ccvrwrI?t=2025)：
- **步驟**：給 $x\in\mathbf{dom}\,f$、$\nu$、$\alpha\in(0,\tfrac12)$、$\beta\in(0,1)$；重複：
  1. 算原始、對偶 Newton 步 $\Delta x_{\text{nt}}$、$\Delta\nu_{\text{nt}}$（$\Delta\nu_{\text{nt}}=w-\nu$）。
  2. 回溯：$t:=1$；當 $\|r(x+t\Delta x,\nu+t\Delta\nu)\|_2>(1-\alpha t)\|r(x,\nu)\|_2$ 時 $t:=\beta t$。
  3. 更新 $x,\nu$。
  4. 直到 $Ax=b$ 且 $\|r(x,\nu)\|_2\le\epsilon$。
- $\beta$ 典型 $\tfrac12$、$\tfrac14$、0.1，「沒差」。
- **為什麼回溯一定會結束** [▶ 37:29](https://youtu.be/zVO4ccvrwrI?t=2249)：$\|r\|_2$ 沿 Newton 方向的方向導數恰為 $-\|r\|_2$（斜率 $-1$ 的比例），打折成 $\alpha$ 倍後，$t$ 夠小一定在下方。

【課堂討論】[▶ 34:21](https://youtu.be/zVO4ccvrwrI?t=2061) $f=-\sum\log x_i$，給一個在定義域內的點？學生：**1**（全 1 向量）。「其實任何正數都行，我也不能說什麼。」

**定義域的陷阱（作業重點）** [▶ 35:26](https://youtu.be/zVO4ccvrwrI?t=2126)

【口頭】定義域是 $\mathbb{R}^n_{++}$ 時，**不要**直接算 $x+t\Delta x$ 再算梯度和 Hessian。如果某分量變成負的或 0，梯度 $-1/x$、Hessian $1/x^2$ **照樣算得出數字**，「但之後不會有任何好事發生，你的演算法不會動」。正確做法：先檢查 $x+t\Delta x>0$，**不是正的就別評估**，直接 $t:=\beta t$，直到在定義域內才評估殘差。

【口頭】[▶ 38:30](https://youtu.be/zVO4ccvrwrI?t=2310) 助教提到他們自己的實作可能就犯了這個錯，老師：「每個人一生都該寫一次對定義域太隨便、結果很慘的 Newton 程式——這是很好的人生經驗。」

---

## 6. 解 KKT 系統

[▶ 39:04](https://youtu.be/zVO4ccvrwrI?t=2344)（課本 §10.4.1）

$$\begin{pmatrix}H&A^T\\A&0\end{pmatrix}\begin{pmatrix}v\\w\end{pmatrix}=-\begin{pmatrix}g\\h\end{pmatrix}$$

| 方法 | 何時用 |
|---|---|
| **LDLᵀ 分解**（稀疏套件） | 一般；$H$、$A$ 稀疏時會利用比你知道的還多的結構（控制、訊號處理……） |
| **消去**（區塊消去 $H$） | $H$ 對角（目標可分、靠等式耦合）、帶狀時 |

**消去 $H$** [▶ 40:37](https://youtu.be/zVO4ccvrwrI?t=2437)：

$$\left(AH^{-1}A^T\right)w=h-AH^{-1}g,\qquad Hv=-(g+A^Tw)$$

形成 $AH^{-1}A^T$、分解、求解；$H$ 對角時 $H^{-1}$「根本不用擔心」。

【口頭】[▶ 40:05](https://youtu.be/zVO4ccvrwrI?t=2405) 例：無人機巡航**必須回到起點**的最佳控制。聽到最佳控制就想到帶狀系統；「回到起點」耦合了開頭和結尾的狀態，是一條**破壞帶狀**的等式約束——但也能極快處理，「根本不是問題」。

---

## 7. 例：解析中心的三種方法

[▶ 41:43](https://youtu.be/zVO4ccvrwrI?t=2503)（課本 §10.4.2，「和你作業要解的極為接近」）

$$\text{minimize}\quad-\sum_{i=1}^n\log x_i\quad\text{s.t.}\quad Ax=b\qquad(A\in\mathbb{R}^{100\times500})$$

目標嚴格凸，所以可以從對偶的解重建原始的解。

| 方法 | 初始化要求 | 結果 |
|---|---|---|
| 1. 可行起點 Newton 法 | $x\succ0$ **且** $Ax=b$ | 約 14 步 |
| 2. 對偶上的 Newton 法：$\max-b^T\nu+\sum\log(A^T\nu)_i+n$ | $A^T\nu\succ0$ | 約 9 步 |
| 3. 不可行起點 Newton 法 | 只要 $x\succ0$（例如全 1） | 約 22 步 |

**初始化** [▶ 43:13](https://youtu.be/zVO4ccvrwrI?t=2593)：
- 方法 1：一般的 $A,b$ 要找 $x\succ0$、$Ax=b$，**一般得解 LP**——「通則：不該有比解問題本身還複雜的子程序」。但有時很容易：
  - 【課堂討論】$\sum x_i=b$（對數效用的資源分配，例如分配 I/O 頻寬給一群行程），初始分配？學生：**$b/n$**。對：均勻分配，「在程式裡加註解『以均勻分配初始化』，完成」。
- 方法 2：要找 $A^T\nu\succ0$，同樣看情況。
- 方法 3：只要在定義域裡，**最簡單**。

**「對偶比較快」的錯誤說法** [▶ 45:49](https://youtu.be/zVO4ccvrwrI?t=2749)

【口頭】有人會說：「我解**對偶**資源分配問題，聽起來很高級——這是**價格發現**法，因為對偶變數就是邊際效用。而且我只有 100 個變數，Newton 那邊有 500 個，我應該快 $5^3$ 倍；而且我 9 步，你 14 步。」「我聽過人們互相這樣說、放在投影片上。全都錯得離譜、蠢得不好笑。」

**真相：用聰明的線性代數，三者每步成本相同** [▶ 48:52](https://youtu.be/zVO4ccvrwrI?t=2932)：

| 方法 | 每步要解的系統 |
|---|---|
| 可行 Newton（區塊消去） | $A\,\mathbf{diag}(x)^2A^Tw=b$ |
| 對偶 Newton | $A\,\mathbf{diag}(A^T\nu)^{-2}A^T\Delta\nu=-b+A\,\mathbf{diag}(A^T\nu)^{-1}\mathbf{1}$ |
| 不可行 Newton（區塊消去） | $A\,\mathbf{diag}(x)^2A^Tw=2Ax-b$ |

全都是 $100\times100$ 的「$A\times$ 正對角 $\times A^T$」系統，只有右手邊不同（不可行版多了殘差 $b-Ax$）。

「如果用天真的線性代數（形成完整 KKT 矩陣再解），它們差很多；用聰明的，複雜度完全一樣。這對對偶一般也成立：有人說『我用 Newton 法解對偶』——用聰明的線性代數就沒差。解對偶確實有理由，但更進階，例如要**分散式**方法時。」

---

## 8. 例：網路流最佳化

[▶ 51:22](https://youtu.be/zVO4ccvrwrI?t=3082)（課本 §10.4.3）

$$\text{minimize}\quad\sum_{i=1}^n\phi_i(x_i)\quad\text{s.t.}\quad Ax=b$$

- 有向圖，$x_i$ 是邊 $i$ 上的流量。**可以為負**（「電機的人知道」）：相對於**參考方向**反向流動。
- $\tilde A$ 是**節點–邊關聯矩陣**：每一行（一條邊）恰有一個 $+1$、一個 $-1$——**極稀疏**。
- $\tilde Ax=0$：每個節點**流量守恆**；這樣的 $x$ 叫**環流**（circulation），例如沿一圈各 1。
- $b$：每個節點注入（或抽出）的量。
- 名字：**單一商品流**（single commodity flow）。例：電路的電荷；忽略傳輸損失的電網（注入是發電機、抽出是負載）；銀行系統的資金流；藥物在人體各隔室間的移動。

【課堂討論】[▶ 55:30](https://youtu.be/zVO4ccvrwrI?t=3330) 怎麼知道 $\tilde A$ 不是滿秩？學生：所有列加起來是 0。對：$\mathbf{1}^T\tilde A=0$。所以刪掉一列（電機方言：把一個節點設為**接地**），得到滿秩的 $A$。

【課堂討論】[▶ 56:34](https://youtu.be/zVO4ccvrwrI?t=3394) 誰在別處看過？生物的**通量平衡**（flux balance）、線性規劃課。

**看到這個問題你該想到** [▶ 57:38](https://youtu.be/zVO4ccvrwrI?t=3458)：
1. 目標**可分** → Hessian $H$ **對角**。
2. $A$ 是關聯矩陣，每行兩個非零 → **稀疏**。
3. 消去 $H$：要解 $AH^{-1}A^Tw=\cdots$。$AH^{-1}A^T$ 是 **Laplacian**（電路裡就是**電導矩陣**）：對角正、非對角非正、（未刪列時）每列和為 0。
4. **稀疏模式一眼可知** [▶ 1:00:41](https://youtu.be/zVO4ccvrwrI?t=3641)：節點 $i,j$ 有邊相連，$(i,j)$ 元素才非零。一百萬個節點、一千萬條邊、每個節點度數 2–50 → 每列 10–50 個非零，稀疏。

【口頭】加州電網大約 3,100 台發電機、6,000 條輸電線，「就算你笨笨地用稠密方法也沒問題」；但美國西部電網就大了（五萬、十萬）。有人說「我有一百萬個節點、一千萬條邊，你要用梯度法？」「不，老兄，我們全力上 Newton。」「你連 Hessian 都形成不了。」「對，我不形成 Hessian，我解 KKT 系統、利用結構，就能很快。」「大多數人不知道這個。」解 Laplacian 方程組在理論電腦科學是一整個子產業，「老實說大多完全沒用，有不是那些的好方法」。

---

## 9. 例：矩陣變數

[▶ 1:02:12](https://youtu.be/zVO4ccvrwrI?t=3732)（課本 §10.4.4）

$$\text{minimize}\quad\log\det X^{-1}\quad\text{s.t.}\quad\mathrm{tr}(A_iX)=b_i,\ i=1,\dots,p\qquad(X\in\mathbf{S}^n)$$

**天真做法** [▶ 1:02:46](https://youtu.be/zVO4ccvrwrI?t=3766)：把 $X$ 的 $n(n+1)/2$ 個獨立元素攤成向量，Hessian 是 $\frac{n(n+1)}2\times\frac{n(n+1)}2$——約 $n^4$ 個元素，每步 $O(n^6)$。$n=200$ 就卡住。

【口頭】這出現在機率、隨機過程、控制。「你不會想寫出逆矩陣行列式的 Hessian——其實可以寫成抽象線性算子，不難。」

**正確做法：寫最佳性條件再線性化** [▶ 1:04:49](https://youtu.be/zVO4ccvrwrI?t=3889)：
- 梯度：$\nabla\log\det X^{-1}=-X^{-1}$。
- $-X^{-1}$ 的一階變化：$X^{-1}\Delta XX^{-1}$（「純量 $-1/x$ 的導數是 $1/x^2$，矩陣只是怎麼說 $1/x^2$」）。
- Newton 方程：
$$X^{-1}\Delta XX^{-1}+\sum_{j=1}^pw_jA_j=X^{-1},\qquad\mathrm{tr}(A_i\Delta X)=0$$
- **手動區塊消去** [▶ 1:06:22](https://youtu.be/zVO4ccvrwrI?t=3982)：第一式左右乘 $X$ 得 $\Delta X=X-\sum_jw_jXA_jX$，代入第二式：
$$\sum_{j=1}^p\mathrm{tr}(A_iXA_jX)\,w_j=b_i,\quad i=1,\dots,p$$
  稠密正定的 $p\times p$ 系統。
- 成本約 $pn^3+p^2n^2+p^3$，對 $n$ 是**二次方**等級（相對變數個數 $\sim n^2$），比天真的 $n^6$ 好太多——「等於從 $n^3$ 變成 $n$」。

【口頭】「你不知道，但每次你解 SDP，解法器裡發生的就是這個。」

**作業提醒** [▶ 1:08:23](https://youtu.be/zVO4ccvrwrI?t=4103)：「花點時間做，但如果除錯了兩三個小時，你該有理智離開鍵盤，把手舉起來讓大家看到，然後走開。」最後大概 15 行。要看的就是那個**加速往下**的誤差曲線。

---

## 10. 預告：不等式約束與對數障礙

[▶ 1:09:55](https://youtu.be/zVO4ccvrwrI?t=4195)（課本 §11.1）

**階層** [▶ 1:09:55](https://youtu.be/zVO4ccvrwrI?t=4195)：
1. 線性代數 = 有效地**在線性等式下最小化凸二次**。
2. 光滑函數加等式約束：「我把它近似成二次，22 步」，每步是 1。
3. 下一層：**不等式約束**，化成一串光滑、等式約束的最小化。

**問題**：

$$\text{minimize }f_0(x)\quad\text{s.t.}\quad f_i(x)\le0,\ i=1,\dots,m,\quad Ax=b$$

- $f_i$ 凸、二次連續可微。CVXPY 之類會先把問題編譯成這種形式：例如「最小化 $\|Ax-b\|_\infty$ s.t. $x\succeq0$」目標不光滑，轉成 LP 後所有 $f_i$ 都是仿射（「非常光滑」）。
- 假設**嚴格可行** → 強對偶成立、對偶最佳存在。
- 例：LP、QP、QCQP、GP（$f_i$ 是仿射函數的 log-sum-exp）、**線性不等式約束下的熵最大化**。
  - 【口頭】[▶ 1:12:31](https://youtu.be/zVO4ccvrwrI?t=4351) $x$ 是有限集合上的機率分布；機率向量的線性約束就是**某個函數的期望值**——「落在這個集合的機率在 0.1 到 0.2 之間」——找滿足這些的最大熵分布。
- SDP、SOCP 最好當成廣義不等式問題處理，之後再講。

**對數障礙的故事** [▶ 1:14:01](https://youtu.be/zVO4ccvrwrI?t=4441)：

約束的語意是指示函數：$f_i(x)\le0$ 收費 0，$>0$ 收費 $+\infty$——所以叫**硬約束**。
- 對偶的故事從「用一條直線近似它」開始——「正常人會說那不是好近似」——結果因為斜率調對，凸問題時其實是**無限好**的近似。
- 這次的故事更好：「我想用 Newton 法，但這個函數不連續、不可微。」【課堂討論】直接對它用 Newton 法效果如何？「不好——根本不會動。」「那我做一個光滑的：一個往上衝到無窮的**障礙函數**，就能用 Newton 法。」下次繼續。

---

## 11. 一頁速查表

### Hessian 結構

| 函數形式 | Hessian | 每步成本 |
|---|---|---|
| $\sum\psi_i(x_i)$ | 對角 | $O(n)$ |
| $\sum\psi_i(x_i)+\psi_0(Ax+b)$ | $D+A^TH_0A$（對角加低秩） | $\approx2p^2n$ |
| 局部交互作用 | 帶狀 | $O(n)$ |
| 資源分配消去後 | 對角 + 秩 1 | $O(n)$ |

### 等式約束 Newton

$$\begin{pmatrix}\nabla^2f&A^T\\A&0\end{pmatrix}\begin{pmatrix}\Delta x\\w\end{pmatrix}=-\begin{pmatrix}\nabla f\\Ax-b\end{pmatrix}$$

| 版本 | 右手邊第二塊 | 起點 | 線搜尋 |
|---|---|---|---|
| 可行 | $0$ | $Ax=b$、$x\in\mathbf{dom}$ | $f$ 回溯 |
| 不可行 | $Ax-b$ | 只要 $x\in\mathbf{dom}$ | $\|r\|_2\le(1-\alpha t)\|r\|_2$；**先檢查定義域** |

- KKT 矩陣非奇異 $\iff\mathcal{N}(H)\cap\mathcal{N}(A)=\{0\}$。
- $\lambda=(\Delta x^T\nabla^2f\Delta x)^{1/2}$；消去後跑 Newton 和直接跑完全相同。
- 走 $t=1$ 一次後就可行。

### 解 KKT

- LDLᵀ（稀疏）；或消去 $H$：$(AH^{-1}A^T)w=h-AH^{-1}g$。
- 解析中心：可行、對偶、不可行三法每步都是 $A\,\mathbf{diag}\,A^T$ 系統。
- 網路流：$AH^{-1}A^T$ 是 Laplacian，稀疏模式 = 圖。
- 矩陣變數：$\sum_j\mathrm{tr}(A_iXA_jX)w_j=b_i$，$O(pn^3)$ 取代 $O(n^6)$。

---

## 12. 與後續集數的連結

> 以下**不是逐字稿內容**：依課本章節推估，做到時再更新。

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 對數障礙、中心路徑、障礙法 | 第 16 集（課本 §11.2–11.3） |
| 不可行起點 Newton | 障礙法的中心化步驟、Phase I |
| 原始–對偶殘差 | 原始–對偶內點法（課本 §11.7） |
| 自和諧 | 障礙法的複雜度分析（課本 §11.5） |
| 自己寫 Newton 解法器 | Homework 7–8 |

---

## 附：本集一句話總結

> **等式約束的 Newton 法就是解一個 KKT 系統，和消去約束後跑 Newton 法完全相同；不可行起點版只要起點在定義域內，用殘差範數做線搜尋，走一步全長就可行——但一定要先檢查定義域再評估。真正決定速度的是線性代數：可分目標給對角 Hessian、關聯矩陣給 Laplacian、對角加低秩給線性時間，聰明地解，「原始 vs 對偶 vs 不可行」每步成本完全一樣。**

---

*筆記依據 Stephen Boyd「Stanford EE364A Convex Optimization I（2023）」Lecture 15 錄影逐字稿（人工字幕，1:17:08）與 Boyd & Vandenberghe《Convex Optimization》§9.6–9.7、第 10 章、§11.1 整理。*
