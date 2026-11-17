---
course: Number Theory（2021 秋，線上錄影）
episode: 19
lecture: Lecture 18
date: 待補（2021 秋）
video: https://youtu.be/4KLw_qaQMk8
notes: Jones & Jones 沒有複數的專節（序言說後三章假設讀者會複數）；第 15 集已用過 $\zeta_n = e^{2\pi i/n}$
---

# 第 19 集 · Lecture 18：複數與單位根（Complex Numbers and Roots of Unity） [▶ 影片](https://youtu.be/4KLw_qaQMk8)

← 上一集：[18-quadratic-reciprocity-2](18-quadratic-reciprocity-2.md) ｜ [總目錄](README.md) ｜ 下一集：[20-solution-of-the-cubic](20-solution-of-the-cubic.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 19 集（影片標題無編號，講者開場稱「lecture 18」）
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（24:15，自動字幕）；課本無對應章節
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 直角座標形式、共軛、長度](#1-直角座標形式共軛長度)
- [2. 極座標形式與虛指數](#2-極座標形式與虛指數)
- [3. 例子：化成極座標、求冪](#3-例子化成極座標求冪)
- [4. 解 z^n = w](#4-解-zn--w)
- [5. 單位根](#5-單位根)
- [6. 例子：w^4 = −1、w^3 = 27、複係數二次方程](#6-例子w4--1w3--27複係數二次方程)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】簡單複習複數，特別是**極座標形式**，以及由它馬上得到、數學系以外比較少人知道的計算。這裡的內容都可以教給高中生，某些地區傳統上也的確這樣教 [▶ 00:00](https://youtu.be/4KLw_qaQMk8?t=0)。

| 段落 | 內容 |
|---|---|
| 1 | 共軛、長度及其性質（$\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$） |
| 2–3 | $e^{i\theta} = \cos\theta+i\sin\theta$；極座標形式；de Moivre |
| 4–5 | $z^n = w$ 的 $n$ 個解；單位根 |
| 6 | $w^4=-1$、$w^3=27$ 的解與因式分解 |

> Jones & Jones 序言說最後三章假設讀者已經會複數等大學一年級數學，所以沒有複數的專節。本集沒有【課本補充】。

---

## 1. 直角座標形式、共軛、長度

[▶ 00:32](https://youtu.be/4KLw_qaQMk8?t=32)

**定義**：
- 複數 $z = x+iy$（$x,y$ 實數），這叫**直角座標形式**（Cartesian form）。
- **共軛**（complex conjugate）：$\bar z = x-iy$。（物理學家等有時寫 $z^*$。）
- **長度**（length，又叫絕對值或模，modulus）：$\lvert z\rvert = \sqrt{x^2+y^2}$，是原點到 $z$ 的距離（直角三角形兩股 $\lvert x\rvert$、$\lvert y\rvert$）。

**性質** [▶ 01:40](https://youtu.be/4KLw_qaQMk8?t=100)：
1. $\overline{z\pm w} = \bar z\pm\bar w$
2. $\overline{zw} = \bar z\,\bar w$
3. $\lvert z\rvert = \sqrt{z\bar z}$
4. $\lvert zw\rvert = \lvert z\rvert\,\lvert w\rvert$

【口頭】性質 4 很重要，是複數特別的原因之一。講者自己研究**結合代數**（associative algebras），一般結合代數（甚至交換的）不能期待「積的範數 = 範數的積」，通常只有「$\le$ 某常數 × 範數的積」，這會毀掉在代數上做微積分的分析——不過這不是本課的內容 [▶ 02:12](https://youtu.be/4KLw_qaQMk8?t=132)。

**證明**：
1. $z = x+iy$、$w = a+ib$，直接算。
2. $zw = (xa-yb) + i(xb+ya)$，共軛是 $(xa-yb) - i(xb+ya)$；而 $\bar z\bar w = (x-iy)(a-ib) = (xa-yb) - i(xb+ya)$。相同。
3. $z\bar z = (x+iy)(x-iy) = x^2+y^2$。
4. 用 2、3：
$$\lvert zw\rvert = \sqrt{zw\,\overline{zw}} = \sqrt{zw\,\bar z\,\bar w} = \sqrt{z\bar z}\,\sqrt{w\bar w} = \lvert z\rvert\,\lvert w\rvert.$$

---

## 2. 極座標形式與虛指數

### 2.1 定義

[▶ 04:25](https://youtu.be/4KLw_qaQMk8?t=265)

**定義**：對實數 $\theta$，**虛指數**（imaginary exponential）
$$e^{i\theta} = \cos\theta + i\sin\theta.$$

**極座標形式**（polar form）：$z = x+iy$，令 $r = \lvert z\rvert$、$\theta$ 是 $z$ 的方向角，則
$$z = r\cos\theta + ir\sin\theta = re^{i\theta}.$$
也就是**大小 × 方向**：$e^{i\theta}$ 是長度 1、指向 $z$ 方向的複數。

【口頭】也可以從 Maclaurin 級數「推導」出 $e^{i\theta} = \cos\theta+i\sin\theta$：指數的冪級數展開後，帶 $i$ 的項是 $\sin$、不帶的是 $\cos$。但本課直接用這個公式**定義** $e^{i\theta}$ [▶ 05:31](https://youtu.be/4KLw_qaQMk8?t=331)。

### 2.2 性質

[▶ 06:02](https://youtu.be/4KLw_qaQMk8?t=362)

1. $e^{i\theta}e^{i\beta} = e^{i(\theta+\beta)}$
2. $\left(e^{i\theta}\right)^n = e^{in\theta}$（**de Moivre 定理**）
3. $\cos\theta = \dfrac{e^{i\theta}+e^{-i\theta}}2$，$\sin\theta = \dfrac{e^{i\theta}-e^{-i\theta}}{2i}$
4. $\dfrac1{e^{i\theta}} = e^{-i\theta}$，$e^0 = 1$
5. $e^{i(\theta+2\pi k)} = e^{i\theta}$（週期 $2\pi$，因為 $\sin$、$\cos$ 週期 $2\pi$）

**證明性質 1**（講者說「相當美」）[▶ 06:34](https://youtu.be/4KLw_qaQMk8?t=394)：
$$(\cos\theta+i\sin\theta)(\cos\beta+i\sin\beta) = (\cos\theta\cos\beta - \sin\theta\sin\beta) + i(\sin\theta\cos\beta+\cos\theta\sin\beta)$$
（$-\sin\theta\sin\beta$ 來自 $i^2 = -1$）
$$= \cos(\theta+\beta) + i\sin(\theta+\beta) = e^{i(\theta+\beta)}.$$

【口頭】性質 1 用一句話同時包含了 $\cos$ 和 $\sin$ 的**和角公式**。虛指數用代數上自然的記號，擁有三角學的全部智慧。這不是微積分，完全可以教高中生，沒教是一場悲劇 [▶ 07:07](https://youtu.be/4KLw_qaQMk8?t=427)。

**證明性質 3**：$e^{i\theta} = \cos\theta+i\sin\theta$，$e^{-i\theta} = \cos\theta - i\sin\theta$（$\cos$ 是偶函數、$\sin$ 是奇函數）。相加、相減再除以 2 或 $2i$。

【口頭】用這兩個公式可以推出無數三角恆等式，不用背；講者有其他影片示範，有興趣可以問 [▶ 08:12](https://youtu.be/4KLw_qaQMk8?t=492)。

---

## 3. 例子：化成極座標、求冪

**例 1**：$z = 3+3i$ [▶ 08:44](https://youtu.be/4KLw_qaQMk8?t=524)
- $\lvert z\rvert = \sqrt{9+9} = \sqrt{18}$；兩股都是 3，角度 $45° = \pi/4$。
- $z = \sqrt{18}\,e^{i\pi/4}$。

【口頭】角度要用**弧度**；寫 $e^{i\cdot45°}$「從沒看過有人這樣寫」。不過給度數講者也不會太生氣 [▶ 09:17](https://youtu.be/4KLw_qaQMk8?t=557)。

**為什麼要極座標** [▶ 09:50](https://youtu.be/4KLw_qaQMk8?t=590)：
- $(3+3i)^{20}$：用二項式定理寫出 Pascal 三角形 20 列也可以，但極座標簡單得多：
$$z^{20} = (\sqrt{18})^{20}e^{20i\pi/4} = 18^{10}e^{5\pi i} = 18^{10}e^{4\pi i}e^{\pi i} = 18^{10}\cdot(-1) = -18^{10}.$$
（$e^{\pi i} = -1$。）
- 倒數：
$$\frac1z = \frac1{\sqrt{18}}e^{-i\pi/4} = \frac1{\sqrt{18}}\left(\frac1{\sqrt2}-\frac i{\sqrt2}\right) = \frac{1-i}{\sqrt{36}} = \frac{1-i}6.$$

**例 2**：$z = 3i$ [▶ 10:55](https://youtu.be/4KLw_qaQMk8?t=655)：在虛軸上，角度 $90° = \pi/2$。檢查 $e^{i\pi/2} = \cos\frac\pi2+i\sin\frac\pi2 = i$。所以 $3i = 3e^{i\pi/2}$。

**例 3**：$z = -\sqrt3-i$ [▶ 11:28](https://youtu.be/4KLw_qaQMk8?t=688)
- 在第三象限。銳角 $\beta$ 滿足 $\tan\beta = \frac1{\sqrt3}$，所以 $\beta = \pi/6$；標準角 $\pi+\frac\pi6 = \frac{7\pi}6$。
- $\lvert z\rvert = \sqrt{3+1} = 2$，$z = 2e^{7\pi i/6}$。
- $z^{12} = 2^{12}e^{12\cdot7\pi i/6} = 2^{12}e^{14\pi i} = 2^{12}$（$14\pi$ 是 $2\pi$ 的倍數）。

【口頭】任何複數都能化成極座標，但找**標準角**一般不容易，要分很多情況——三角學課很大一部分就在教這個 [▶ 13:09](https://youtu.be/4KLw_qaQMk8?t=789)。

**定理** [▶ 13:41](https://youtu.be/4KLw_qaQMk8?t=821)：若 $r_1e^{i\theta_1} = r_2e^{i\theta_2}$（$r_1,r_2\ge0$），則 $r_1 = r_2$，且 $\theta_1$、$\theta_2$ **同界**（coterminal，幾何上同一方向）：$\theta_1 - \theta_2 = 2\pi k$，$k\in\mathbb{Z}$。

**證明**：兩邊取長度得 $\lvert r_1\rvert = \lvert r_2\rvert$，非負所以相等。於是 $e^{i\theta_1} = e^{i\theta_2}$，$\cos$ 和 $\sin$ 都相等，所以兩角差 $2\pi$ 的整數倍。（講者說最後一步可以寫得更嚴謹，但不寫。）

---

## 4. 解 z^n = w

[▶ 14:46](https://youtu.be/4KLw_qaQMk8?t=886)

**問題**：給 $w$ 和 $n$，求所有 $z$ 使 $z^n = w$。

**做法**：都寫成極座標，$z = re^{i\theta}$（未知）、$w = se^{i\beta}$（已知）。
$$z^n = r^ne^{in\theta} = se^{i\beta}.$$
由上面的定理：
$$r^n = s,\qquad n\theta = \beta+2\pi k.$$
所以 $r = \sqrt[n]s$（實數 $n$ 次方根）、$\theta = \dfrac{\beta+2\pi k}{n}$。$k = 0,1,\dots,n-1$ 給出完整的解；再往下就重複。

**定理**：$w = \lvert w\rvert e^{i\beta}$，則 $z^n = w$ 的解集是
$$z = \sqrt[n]{\lvert w\rvert}\,\exp\!\left(i\,\frac{\beta+2\pi k}{n}\right),\qquad k = 0,1,\dots,n-1.$$
**恰好 $n$ 個解。**

---

## 5. 單位根

[▶ 16:56](https://youtu.be/4KLw_qaQMk8?t=1016)

**定義**：
- $w$ 的角 $\beta\in(-\pi,\pi]$，**主 $n$ 次方根**（principal $n$-th root）：$\sqrt[n]{\lvert w\rvert}\,e^{i\beta/n}$。
- **主 $n$ 次單位根**（principal $n$-th root of unity）：
$$\zeta_n = e^{2\pi i/n} = \cos\frac{2\pi}n + i\sin\frac{2\pi}n.$$
- $w^{1/n}$ 表示 $w$ 的**所有** $n$ 次方根（多值，不是函數）：
$$w^{1/n} = \{\,\rho,\ \zeta_n\rho,\ \zeta_n^2\rho,\ \dots,\ \zeta_n^{n-1}\rho\,\},\quad \rho = \text{主 } n \text{ 次方根}.$$
所以 $z^n = w\Rightarrow z\in w^{1/n}$。

**幾何**：找到一個根，其他的都是乘上 $\zeta_n$ 的冪——乘 $\zeta_n$ 就是**旋轉** $2\pi/n$ [▶ 18:35](https://youtu.be/4KLw_qaQMk8?t=1115)。$n$ 次單位根 $1^{1/n}$ 是單位圓上正 $n$ 邊形的頂點（講者畫了 $n = 2,\dots,6$）。

**例**：
- $1^{1/4} = \{1, i, -1, -i\}$（主 4 次單位根是 $i$）。
- 主 3 次單位根 $\zeta_3 = \dfrac{-1+i\sqrt3}2$，$\zeta_3^2 = \dfrac{-1-i\sqrt3}2$。

【口頭】很酷的事：**所有 $n$ 次單位根加起來是 0**。講者和一位學生寫過一篇研究論文，就用到這個 [▶ 19:44](https://youtu.be/4KLw_qaQMk8?t=1184)。

（以下**不是逐字稿內容**，是依等比級數補的理由：$n\ge2$ 時 $1+\zeta_n+\cdots+\zeta_n^{n-1} = \dfrac{\zeta_n^n-1}{\zeta_n-1} = 0$，因為 $\zeta_n^n = 1$、$\zeta_n\neq1$。）

---

## 6. 例子：w^4 = −1、w^3 = 27、複係數二次方程

### 6.1 $w^4 = -1$

[▶ 19:44](https://youtu.be/4KLw_qaQMk8?t=1184)

- $-1 = e^{i\pi}$，主 4 次方根是 $e^{i\pi/4}$。
- 乘上 $1^{1/4} = \{1,i,-1,-i\}$：
$$e^{i\pi/4},\ e^{3i\pi/4},\ e^{5i\pi/4},\ e^{7i\pi/4},\quad\text{即}\quad\frac{\pm1\pm i}{\sqrt2}.$$

**因式分解** [▶ 20:51](https://youtu.be/4KLw_qaQMk8?t=1251)：由因式定理（複係數多項式也成立），
$$w^4+1 = (w-e^{i\pi/4})(w-e^{3i\pi/4})(w-e^{5i\pi/4})(w-e^{7i\pi/4}).$$

**另一種做法**：平方差兩次：
$$w^4+1 = w^4 - i^2 = (w^2-i)(w^2+i) = (w-\sqrt i)(w+\sqrt i)(w-\sqrt{-i})(w+\sqrt{-i}).$$
問題是 $\sqrt i$ 是什麼——取主平方根：$\sqrt i = e^{i\pi/4}$、$\sqrt{-i} = e^{-i\pi/4}$，又回到上面的結果。

⚠️ 逐字稿缺字：[▶ 21:22](https://youtu.be/4KLw_qaQMk8?t=1282) 字幕先說「square root of i is … e to the minus pi i over 4」再改口為 $e^{i\pi/4}$。

【口頭】你大概沒辦法用高中代數直接分解 $x^4+1$，因為得看出它能拆成那樣，不太明顯。理論上任何四次式都能分解 [▶ 21:53](https://youtu.be/4KLw_qaQMk8?t=1313)。

（以下**不是逐字稿內容**，是把共軛的兩對乘起來得到的實係數分解：$(w-e^{i\pi/4})(w-e^{-i\pi/4}) = w^2-\sqrt2w+1$、$(w-e^{3i\pi/4})(w-e^{-3i\pi/4}) = w^2+\sqrt2w+1$，所以 $w^4+1 = (w^2-\sqrt2w+1)(w^2+\sqrt2w+1)$。講者說「乘開很有趣」，螢幕上可能就是這個，字幕沒唸出。）

### 6.2 $w^3 = 27$

[▶ 22:29](https://youtu.be/4KLw_qaQMk8?t=1349)

- 主立方根：$\sqrt[3]{27} = 3$（這裡就是一般微積分前的立方根）。
- $27^{1/3} = 3\cdot1^{1/3} = \{3,\ 3\zeta_3,\ 3\zeta_3^2\} = \left\{3,\ \dfrac{-3+3i\sqrt3}2,\ \dfrac{-3-3i\sqrt3}2\right\}$。
- 因式定理：
$$w^3-27 = (w-3)(w-3\zeta_3)(w-3\zeta_3^2).$$

### 6.3 複係數的二次公式

[▶ 23:01](https://youtu.be/4KLw_qaQMk8?t=1381)

回顧第 1 集用配方法推二次公式的步驟：$a,b,c$ 是**複數**時每一步照樣成立，一直到「$\pm$」那一步——$\pm$ 正是 $(\cdot)^{1/2}$（兩個平方根）給的。所以
$$z = \frac{-b\pm\left(b^2-4ac\right)^{1/2}}{2a}$$
對複係數二次方程也成立，其中 $(\cdot)^{1/2}$ 是兩個複數平方根。

講者舉了一個例子，得到形如 $z = -\tfrac12\pm\sqrt{\cdots}$ 的答案，根號裡是含 $\sqrt2$ 和 $i$ 的複數；要寫得更明確得把根號裡的數化成極座標再開方，但時間不夠了。

⚠️ 待確認：這個例子的原方程字幕沒唸清楚（只聽到「$-\frac12\pm$ the square root of $\frac12+\sqrt2-\sqrt2i$」之類），待補。

【口頭】「抱歉今天時間用完了，有問題寄信給我。」[▶ 24:06](https://youtu.be/4KLw_qaQMk8?t=1446)

---

## 7. 一頁速查表

**共軛與長度**：$\bar z = x-iy$，$\lvert z\rvert = \sqrt{x^2+y^2} = \sqrt{z\bar z}$。
- $\overline{zw} = \bar z\bar w$；$\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$（關鍵：$\sqrt{zw\bar z\bar w}$）。

**虛指數**：$e^{i\theta} = \cos\theta+i\sin\theta$；$z = re^{i\theta}$。
- $e^{i\theta}e^{i\beta} = e^{i(\theta+\beta)}$（= 兩個和角公式）。
- de Moivre：$(e^{i\theta})^n = e^{in\theta}$；週期 $2\pi$；$e^{i\pi} = -1$。
- $\cos\theta = \frac{e^{i\theta}+e^{-i\theta}}2$，$\sin\theta = \frac{e^{i\theta}-e^{-i\theta}}{2i}$。

**例**：$(3+3i)^{20} = -18^{10}$；$\frac1{3+3i} = \frac{1-i}6$；$(-\sqrt3-i)^{12} = 2^{12}$。

**$z^n = w$**：$z = \sqrt[n]{\lvert w\rvert}\,e^{i(\beta+2\pi k)/n}$，$k = 0..n-1$，恰 $n$ 個。
- 關鍵：$r^n = s$、$n\theta = \beta+2\pi k$。

**單位根**：$\zeta_n = e^{2\pi i/n}$；$w^{1/n} = \rho\cdot\{1,\zeta_n,\dots,\zeta_n^{n-1}\}$（旋轉 $2\pi/n$）；所有 $n$ 次單位根和為 0。
- $1^{1/4} = \{\pm1,\pm i\}$；$\zeta_3 = \frac{-1+i\sqrt3}2$。
- $w^4 = -1$：$\frac{\pm1\pm i}{\sqrt2}$；$w^3-27 = (w-3)(w-3\zeta_3)(w-3\zeta_3^2)$。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 立方單位根 $\zeta_3$、$z^n = w$ | 第 20 集（三次方程的解：Cardano 公式的三個根） |
| $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$、$z\bar z = x^2+y^2$ | 第 21–22 集（高斯整數的範數 $N(a+bi) = a^2+b^2$ 是乘法的） |
| 範數的乘法性在一般代數不成立 | 第 23 集（四元數仍有乘法範數） |
| 單位根、分圓多項式 | 第 24 集（Kummer 用分圓整數研究 Fermat 最後定理） |

---

## 附：本集一句話總結

> **定義 $e^{i\theta}=\cos\theta+i\sin\theta$ 後，每個複數都是「大小 × 方向」$re^{i\theta}$，乘法變成長度相乘、角度相加（一句話包含兩個和角公式），所以 $z^n=w$ 恰有 $n$ 個解：主根乘上 $n$ 次單位根 $\zeta_n^k=e^{2\pi ik/n}$，也就是單位圓上正 $n$ 邊形的旋轉。**

---

## ⚠️ 待確認清單

1. [▶ 23:01](https://youtu.be/4KLw_qaQMk8?t=1381) 複係數二次方程例子的原方程沒唸清楚，待補。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 18（Complex Numbers and Roots of Unity）錄影逐字稿（YouTube 自動字幕，24:15）整理；Jones & Jones 無對應章節。*
