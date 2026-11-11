---
course: Stanford EE364A Convex Optimization I（2023）
episode: 8
lecture: Lecture 8
date: 待補
video: https://youtu.be/wsRznzNgTS0
notes: 《Convex Optimization》§5.1.6–5.7（書頁 221–253，PDF 頁 235–267）
---

# 第 8 集 · Lecture 8：對偶問題、強對偶、KKT、敏感度分析 [▶ 影片](https://youtu.be/wsRznzNgTS0)

← 上一集：[07-vector-optimization-duality](07-vector-optimization-duality.md) ｜ [總目錄](README.md) ｜ 下一集：[09-duality-2-approximation](09-duality-2-approximation.md) →

> **課程**：Stanford EE364A Convex Optimization I，2023 — 第 8 集
> **講者**：Stephen Boyd
> **來源**：YouTube 錄影逐字稿（1:20:46，人工字幕 en-US）＋ Boyd & Vandenberghe《Convex Optimization》§5.1.6–5.7
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：分割問題的下界與貪婪法](#1-複習分割問題的下界與貪婪法)
- [2. 對偶函數與共軛函數](#2-對偶函數與共軛函數)
- [3. 對偶問題](#3-對偶問題)
- [4. 弱對偶與強對偶](#4-弱對偶與強對偶)
- [5. 例：LP 與 QP 的對偶](#5-例lp-與-qp-的對偶)
- [6. 非凸但強對偶成立的問題](#6-非凸但強對偶成立的問題)
- [7. 幾何解釋](#7-幾何解釋)
- [8. 互補鬆弛](#8-互補鬆弛)
- [9. KKT 條件](#9-kkt-條件)
- [10. 例：注水](#10-例注水)
- [11. 擾動與敏感度分析](#11-擾動與敏感度分析)
- [12. 預告：重新表述與對偶](#12-預告重新表述與對偶)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 對偶函數與共軛、最大熵 | §5.1.6 |
| 對偶問題、LP／QP 的對偶 | §5.2.1、§5.2.4 |
| 弱對偶、強對偶、Slater 條件 | §5.2.2–5.2.3 |
| 非凸問題的強對偶（兩個二次式） | §5.2.4、附錄 B |
| 幾何解釋 | §5.3 |
| 互補鬆弛、KKT、注水 | §5.5.2–5.5.3 |
| 力學解釋 | §5.5.4 |
| 擾動與敏感度 | §5.6 |
| 重新表述（開頭） | §5.7 |

---

## 1. 複習：分割問題的下界與貪婪法

[▶ 00:04](https://youtu.be/wsRznzNgTS0?t=4)

對**任何**問題（凸不凸都行）形成 Lagrangian、對偶函數，得到一個**以 $(\lambda,\nu)$ 為參數的下界**。隨便丟 $\lambda,\nu$ 常得到 $-\infty$——「那是通用下界，毫無資訊」；但有些情況得到很不顯然的界。

雙向分割（[第 7 集 §3.5](07-vector-optimization-duality.md#35-雙向分割與譜分割)）：$W+\mathbf{diag}(\nu)\succeq0$ ⇒ $p^\star\ge-\mathbf{1}^T\nu$。精確解這個問題極難，但【口頭】[▶ 03:11](https://youtu.be/wsRznzNgTS0?t=191)「你幾乎永遠不需要精確解」：問他 $W$ 從哪來，通常是編的，「符號大概是對的」。

**街頭格鬥：貪婪局部搜尋** [▶ 03:45](https://youtu.be/wsRznzNgTS0?t=225)

- **在解什麼**：雙向分割的近似解。
- **步驟**：
  1. 隨機初始化 $x\in\{\pm1\}^n$。
  2. 依序檢查 $i=1,2,3,\dots$：翻轉 $x_i$ 的符號，目標下降就接受。
  3. 一直循環到沒有任何單一翻轉能改善（稱 **1-opt**）。
  4. 再多寫四行：考慮**成對**同時翻轉，循環到沒有任何一對能改善（**2-opt**）。
- **什麼時候會失敗**：k-opt 只代表在這個離散集合上**局部最佳**，不是最佳。

【口頭】[▶ 05:51](https://youtu.be/wsRznzNgTS0?t=351) 這類方法常常很好用，放進大系統沒人在乎。但有人問「離最佳多遠？」時，對偶下界就派上用場：「我的啟發式 50 毫秒得到 3.2，我證明沒人能做得比 2.7 好。」那就表示不需要有人去改進你的分割器，該把力氣放在別處。

---

## 2. 對偶函數與共軛函數

[▶ 06:53](https://youtu.be/wsRznzNgTS0?t=413)

問題（不必凸）：
$$\text{minimize }f_0(x)\quad\text{s.t.}\quad Ax\preceq b,\ Cx=d$$

$$
\begin{aligned}
g(\lambda,\nu)&=\inf_x\left(f_0(x)+\lambda^T(Ax-b)+\nu^T(Cx-d)\right)\\
&=-b^T\lambda-d^T\nu+\inf_x\left(f_0(x)+(A^T\lambda+C^T\nu)^Tx\right)\\
&=-b^T\lambda-d^T\nu-f_0^*\left(-A^T\lambda-C^T\nu\right)
\end{aligned}
$$

不含 $x$ 的項提出 inf；剩下「函數加線性函數」的下確界——差幾個符號就是**共軛函數**（共軛是「最大化線性減函數」）。「共軛就這樣直接從對偶函數裡跑出來。」

**例：最大熵** [▶ 08:26](https://youtu.be/wsRznzNgTS0?t=506)

$$\text{minimize }f_0(x)=\sum_{i=1}^nx_i\log x_i\quad\text{s.t.}\quad Ax\preceq b,\ \mathbf{1}^Tx=1$$

- $x$ 是 $n$ 個項目上的機率分布（定義域保證 $x\succ0$）。約束指定某些函數的期望值：「二階動差是這個、$x$ 滿足某條件的機率是 0.2、三階動差在這兩個數之間」。
- 這就是**找滿足這些期望值要求的最大熵分布**，「這是很真實的問題」。
- 不用自己算：Google「負熵的共軛」得 $f_0^*(y)=\sum_ie^{y_i-1}$。於是最大熵問題的對偶是一個**涉及指數**的凸問題。

【口頭】[▶ 10:05](https://youtu.be/wsRznzNgTS0?t=605) 統計的人應該有感：這是**最大熵**和**指數族**（exponential families）的連結；那些領域到處都是對偶和共軛。

【課本補充】§5.1.6 Example 5.5：令 $a_i$ 為 $A$ 的第 $i$ 行，
$$g(\lambda,\nu)=-b^T\lambda-\nu-\sum_{i=1}^ne^{-a_i^T\lambda-\nu-1}$$

---

## 3. 對偶問題

[▶ 11:06](https://youtu.be/wsRznzNgTS0?t=666)

「$\lambda,\nu$ 是參數，不同的給不同下界——你顯然會有**找最好下界**的衝動，無法控制的衝動。」

**Lagrange 對偶問題**：

$$\text{maximize}\quad g(\lambda,\nu)\quad\text{subject to}\quad\lambda\succeq0$$

- 用 Lagrange 對偶找原問題最佳值的**最大下界**。
- **永遠是凸問題**（最大化凹函數、凸約束），**即使原問題不凸**。
- 最佳值記 $d^\star$。滿足 $\lambda\succeq0$、$g>-\infty$ 的 $(\lambda,\nu)$ 叫**對偶可行**；最佳的叫**對偶最佳**。
- 常把 $g>-\infty$ 的隱含約束寫明。例：標準形式 LP（$\min c^Tx$ s.t. $Ax=b$、$x\succeq0$）的對偶寫成
$$\text{maximize }-b^T\nu\quad\text{s.t.}\quad A^T\nu+c\succeq0$$
  老師說這做了幾個「無辜的轉換」，嚴格的對偶是最大化一個「不滿足某條件就是 $-\infty$」的函數。這兩個 LP 互為**對偶 LP**；「對偶」這個名字暗示做兩次會回到原本，就像共軛——在某些情況下確實如此。

---

## 4. 弱對偶與強對偶

[▶ 13:18](https://youtu.be/wsRznzNgTS0?t=798)

| | 式子 | 何時成立 |
|---|---|---|
| **弱對偶** | $d^\star\le p^\star$ | **永遠**，凸不凸都成立，沒有例外 |
| **強對偶** | $d^\star=p^\star$ | 一般不成立；**凸問題通常成立** |

- $p^\star-d^\star$ 叫**對偶間隙**（duality gap）。
- $d^\star=+\infty$ ⇒ $p^\star=+\infty$：這是原問題**不可行**的證明。
- 【口頭】[▶ 13:51](https://youtu.be/wsRznzNgTS0?t=831) 弱對偶「聽起來很玄」，其實只靠「非負數乘積非負、非負數相加非負」。
- 弱對偶的用途：困難問題（例如分割）的對偶是 SDP，可以解，得到一個非平凡的下界。

【口頭】[▶ 14:55](https://youtu.be/wsRznzNgTS0?t=895)「在所有**實際的**凸問題裡，強對偶都成立。有沒有凸問題會失敗？有。但如果你遇到一個，要回頭問自己——你不會遇到；比較可能的是某個討厭的同事問『你怎麼知道強對偶成立？』，叫他走開就好。如果真的遇到這種病態，代表你在做錯的事。」

**約束規範**（constraint qualification）[▶ 15:56](https://youtu.be/wsRznzNgTS0?t=956)：保證強對偶的額外條件。「有整本書、整門課只講這個，第 150 頁左右會有一張圖寫著 Slater、這個人、那個人的名字，誰推出誰。」老師受過純數學訓練「可以這樣說數學，這不傷害任何人，但我不認為正常人需要擔心」。

**Slater 條件**（「大鐵鎚」）[▶ 18:01](https://youtu.be/wsRznzNgTS0?t=1081)：凸問题若存在一點使不等式**嚴格**成立，

$$\exists x\in\mathbf{relint}\,\mathcal{D}:\quad f_i(x)<0,\ i=1,\dots,m,\quad Ax=b$$

則強對偶成立（而且 $d^\star>-\infty$ 時對偶最佳值可達到）。
- **線性不等式不需要嚴格滿足**（較強的版本）。
- 很多問題不滿足 Slater 卻照樣強對偶。

**分割問題的實務** [▶ 16:27](https://youtu.be/wsRznzNgTS0?t=987)

【口頭】你寫了三行貪婪分割、通過單元測試、放進大系統，「你是英雄」。某天有人問「離全域最佳多遠？」你解那個對偶 SDP 得到一個數，和貪婪法比——「當然會相當接近」。有人問你怎麼做分割，你說「四行貪婪法」或「譜分割加四行貪婪法」；討厭的人問「那是非凸的，離全域最佳多遠？」，正確答案大概是「誰在乎，請走開，我有正事要做」——但你也可以說「剛好我解過對偶問題，通常最多差 5%–10%」。

---

## 5. 例：LP 與 QP 的對偶

**不等式形式 LP** [▶ 19:04](https://youtu.be/wsRznzNgTS0?t=1144)

$$\text{minimize }c^Tx\quad\text{s.t.}\quad Ax\preceq b$$

$$g(\lambda)=\inf_x\left((c+A^T\lambda)^Tx-b^T\lambda\right)=\begin{cases}-b^T\lambda&A^T\lambda+c=0\\-\infty&\text{否則}\end{cases}$$

對偶（把隱含約束寫明）：

$$\text{maximize }-b^T\lambda\quad\text{s.t.}\quad A^T\lambda+c=0,\ \lambda\succeq0$$

- 任何對偶可行的 $\lambda$，$-b^T\lambda$ 是原 LP 最佳值的下界。
- 線性不等式免除 Slater 的嚴格要求，所以 LP **永遠強對偶**，除了極病態的情況：$p^\star=+\infty$ 且 $d^\star=-\infty$（兩者都不可行），「要特別造，很小很蠢，但你至少知道會發生」。
- 解出來會有對偶可行的 $\lambda$ 使 $-b^T\lambda$ 等於原目標值——**最佳性憑證**。【口頭】[▶ 21:42](https://youtu.be/wsRznzNgTS0?t=1302) 大多數方法解 LP 時**不管你要不要**都會給你 $\lambda$：回傳 $x$，同時回傳一個完全獨立、可檢查的證明，說明沒有可行點目標更小。「在數值計算裡這非常罕見，但所有解法器都這樣做。」它們回傳**原始最佳**（primal optimal）和**對偶最佳**（dual optimal）。

**QP**（$P\in\mathbf{S}^n_{++}$）[▶ 22:43](https://youtu.be/wsRznzNgTS0?t=1363)

$$\text{minimize }x^TPx\quad\text{s.t.}\quad Ax\preceq b$$

【課本補充】§5.2.4：$L=x^TPx+\lambda^T(Ax-b)$，對 $x$ 最小化得 $x=-\tfrac12P^{-1}A^T\lambda$，

$$g(\lambda)=-\tfrac14\lambda^TAP^{-1}A^T\lambda-b^T\lambda$$

對偶：$\text{maximize }-\tfrac14\lambda^TAP^{-1}A^T\lambda-b^T\lambda$ s.t. $\lambda\succeq0$。

- 任何對偶可行點的目標值是原問題的下界；任何原始可行點的目標值是對偶問題的上界。
- 線性不等式 → 無例外，$p^\star=d^\star$。

【口頭】[▶ 23:44](https://youtu.be/wsRznzNgTS0?t=1424)「這是個驚人的終點。」故事一開始很不可信：把 0/$\infty$ 的指示函數用一條直線近似——「我不知道誰能說那是近似」。結果是：**把直線調對，就得到原問題的最佳值**——至少對凸問題，「它沒有一開始看起來那麼蠢」。

---

## 6. 非凸但強對偶成立的問題

[▶ 25:16](https://youtu.be/wsRznzNgTS0?t=1516)

有些非凸問題已知強對偶成立。有名的：**在單位球上最小化非凸二次式**——「不容易證，但成立」。

【課本補充】§5.2.4 Example 5.7 與附錄 B：
$$\text{minimize }x^TAx+2b^Tx\quad\text{s.t.}\quad x^Tx\le1$$
（$A\in\mathbf{S}^n$，不必半正定）強對偶成立。更一般地：**只有一個二次不等式約束的二次規劃**（目標和約束都可以是非凸二次）只要 Slater 條件成立，強對偶就成立（S-引理）。

**推論：任何只有兩個二次式的最佳化問題都能可處理地解** [▶ 25:46](https://youtu.be/wsRznzNgTS0?t=1546)。你已知幾個：特徵值、奇異值問題。「最大化 $x^TAx$ s.t. $x^Tx=1$——那是特徵值問題，你知道那是全域解。『你的問題是凸的嗎？』『其實不是。』」

**「能解的都是因為凸」** [▶ 26:48](https://youtu.be/wsRznzNgTS0?t=1608)

【口頭】有人主張最佳化裡**任何**你能解的問題都是因為凸。很強也很怪，但部分是真的。例：圖上最短路徑可以證明它的鬆弛是緊的（零對偶間隙）。老師覺得這很蠢，因為對你沒幫助：「我該用 CVXPY 的 LP 解法器找最短路徑嗎？不，用最短路徑演算法，例如 Dijkstra。」特徵值問題能解也可以說成「它的對偶 (A) 是凸的、(B) 強對偶成立」。「是個延伸，但技術上是真的。我想不出任何應用數學領域裡能全域求解、背後卻沒有凸性潛伏的問題。」

【口頭】[▶ 28:20](https://youtu.be/wsRznzNgTS0?t=1700)「兩個二次式」這件事很少人知道，**大約每 10 年就在 10 個不同領域被重新發現一次**：「此刻就有人在寫一篇 25 頁、記號很爛的論文，以為發現了深刻的東西。」甚至有一篇論文專門寫它被重複發現的歷史。還有更怪的：複數域上 6 個變數的四次式也有零對偶間隙，原因來自代數幾何——「我建議你連我剛說的都忘掉」。

---

## 7. 幾何解釋

[▶ 29:24](https://youtu.be/wsRznzNgTS0?t=1764)

問題：$\min f_0(x)$ s.t. $f_1(x)\le0$（**非凸**也行）。$x$ 可以是 100 維，但看二維的集合

$$\mathcal{G}=\{(f_1(x),f_0(x))\mid x\in\mathcal{D}\}$$

（課本 Figure 5.3）

- 橫軸 $u=f_1$：**右邊完全不能接受**（不可行），只看左半邊。
- 縱軸 $t=f_0$：越低越好。
- $p^\star$ = $\mathcal{G}$ 在左半平面的**最低點**的高度，「位能最低的那點」。

**對偶函數的幾何** [▶ 31:31](https://youtu.be/wsRznzNgTS0?t=1891)：Lagrangian 只依賴這兩個數：$L=t+\lambda u$。固定 $\lambda$，等高線是斜率 $-\lambda$ 的直線 $\lambda u+t=$ 常數。往左下推到剛好碰到 $\mathcal{G}$，這條**支撐線和縱軸的交點就是 $g(\lambda)$**。

$$g(\lambda)=\inf\{\lambda u+t\mid(u,t)\in\mathcal{G}\}$$

- 圖上看得到 $g(\lambda)\le p^\star$。
- 轉動斜率：$\lambda$ 很大時（線很陡）交點低；轉到同時碰到兩點時交點最高 = $d^\star$；再轉又往下。「我用眼睛描出 $g$ 的形狀：上升、到頂、下降——是凹的，我們早就知道。」
- **間隙** $p^\star-d^\star$ 在圖上看得見 [▶ 34:09](https://youtu.be/wsRznzNgTS0?t=2049)：它來自 $\mathcal{G}$ 的**凹陷**（非凸部分）。若 $\mathcal{G}$ 凸，就沒有間隙。

**凸問題的版本** [▶ 35:11](https://youtu.be/wsRznzNgTS0?t=2111)：改用

$$\mathcal{A}=\{(u,t)\mid\exists x\in\mathcal{D}:\ f_1(x)\le u,\ f_0(x)\le t\}$$

（$\mathcal{G}$ 往右上延伸）。凸問題的 $\mathcal{A}$ 是凸集。$p^\star$ 是 $\mathcal{A}$ 和縱軸交點的最低處；支撐線轉到在 $(0,p^\star)$ **相切**的斜率時，$g(\lambda)=p^\star$——這就是**支撐超平面定理**讓強對偶成立的原因。

**預告敏感度** [▶ 37:44](https://youtu.be/wsRznzNgTS0?t=2264)

【口頭】你去談判：「50 毫瓦的功率預算我做不到，時脈跑不起來，給我 55。」這把約束從 $f_1\le0$ 放寬成 $f_1\le$ 某個正數，在圖上往右移。目標**只會下降**，而且下降量可以用 **Lagrange 乘數**（那條切線的斜率）很好地近似。所以有人叫它**影子價格**：要放寬或收緊約束，你願意付出多少目標。

【口頭】[▶ 39:19](https://youtu.be/wsRznzNgTS0?t=2359) 用這張圖也能造出「凸但有正對偶間隙」的病態問題，「但我不做，因為你不該做」。

---

## 8. 互補鬆弛

[▶ 39:49](https://youtu.be/wsRznzNgTS0?t=2389)

設強對偶成立，$x^\star$ 原始最佳、$(\lambda^\star,\nu^\star)$ 對偶最佳（合稱**原始–對偶最佳**）。

$$
\begin{aligned}
f_0(x^\star)=g(\lambda^\star,\nu^\star)&=\inf_x\left(f_0(x)+\sum_i\lambda_i^\star f_i(x)+\sum_i\nu_i^\star h_i(x)\right)\\
&\le f_0(x^\star)+\sum_i\lambda_i^\star f_i(x^\star)+\sum_i\nu_i^\star h_i(x^\star)\\
&\le f_0(x^\star)
\end{aligned}
$$

- 第一個 $\le$：下確界不超過在 $x=x^\star$ 的值。
- 第二個 $\le$：$h_i(x^\star)=0$；$\lambda_i^\star\ge0$、$f_i(x^\star)\le0$。

頭尾相同，所以**兩個不等式都是等式**。由第二個等式：$\sum_i\lambda_i^\star f_i(x^\star)=0$。

【課堂討論】[▶ 41:52](https://youtu.be/wsRznzNgTS0?t=2512) 一串**每項都 $\le0$** 的數加起來是 0，能得出什麼？——**每一項都是 0**。

$$\lambda_i^\star f_i(x^\star)=0,\quad i=1,\dots,m$$

這叫**互補鬆弛**（complementary slackness）：

$$\lambda_i^\star>0\Rightarrow f_i(x^\star)=0,\qquad f_i(x^\star)<0\Rightarrow\lambda_i^\star=0$$

- $f_i(x)=0$：約束**緊**（tight）；$f_i(x)<0$：約束**鬆**（slack）。
- **約束鬆，乘數一定是 0**；乘數非零，約束一定緊。

【課本補充】第一個等式也給出：$x^\star$ 最小化 $L(x,\lambda^\star,\nu^\star)$。

**力學類比** [▶ 42:54](https://youtu.be/wsRznzNgTS0?t=2574)（課本 §5.5.4）

【口頭】「鬆」「緊」本來就是力學的比喻，而且完全對得上：最小化某個機械系統的位能，受約束（例：碰到牆面、兩點之間有纜線）。
- 「鬆」= 沒碰到牆、纜線沒有張力；「緊」= 碰到了、纜線繃緊（taut）。
- **$\lambda$ 字面上就是接觸力或纜線張力，單位是牛頓**。纜線鬆 → 沒有張力 → $\lambda=0$。

【Q&A】[▶ 44:29](https://youtu.be/wsRznzNgTS0?t=2669) 學生問：怎麼知道 $\lambda^\star$、$f_i^\star$ 是有限的？對偶問題不會跑到無窮大嗎？答：這裡假設**原始最佳和對偶最佳都存在**（而且強對偶）。你說的是不可行或對偶無界的情況，那時沒有這些結論，之後會講。

---

## 9. KKT 條件

[▶ 44:59](https://youtu.be/wsRznzNgTS0?t=2699)

**名字的故事** [▶ 45:32](https://youtu.be/wsRznzNgTS0?t=2732)

【口頭】Lagrange 等人在 19 世紀初提出等式約束下最小化的條件（只做一兩條約束），所以名字掛他。推廣到不等式，「如果你問 19 世紀中後期的數學家，他們一定做得出來」，但不知為何直到約 **1951 年** Princeton 的 Kuhn 和 Tucker 才提出，叫 **Kuhn–Tucker 條件**，1960–65 年的論文都這樣叫。約十年後發現 **Karush 1938 年的碩士論文**（未發表）裡什麼都有了，於是大家做了對的事，改叫 **Karush–Kuhn–Tucker**。

「真正的教訓是：**永遠不要假裝你是第一個做出某件事的人**——首先，幾乎可以確定 Gauss 知道。」老師有朋友會提醒他「那不是 Cauchy–Schwarz 不等式，是 500 年前的某某不等式」；「你也不該和說這種話的人混在一起」。「每次我查證這類指控，都證明是假的——包括我自己的。」

> ⚠️ 逐字稿缺字 [▶ 47:08](https://youtu.be/wsRznzNgTS0?t=2828)：字幕寫「it's the **Bhattacharya** inequality, which is 500 years earlier」，人名可能聽錯，無法確認。

**KKT 條件**（$f_i,h_i$ 可微）[▶ 47:40](https://youtu.be/wsRznzNgTS0?t=2860)：

| 條件 | 式子 | 意思 |
|---|---|---|
| 1. 原始可行 | $f_i(x)\le0$，$h_i(x)=0$ | 不可行就不是候選 |
| 2. 對偶可行 | $\lambda\succeq0$ | 負的 $\lambda$ = 被付錢去違反約束，沒道理 |
| 3. 互補鬆弛 | $\lambda_if_i(x)=0$ | 乘數為正 $\iff$ 約束緊 |
| 4. 穩定性 | $\nabla f_0(x)+\sum_i\lambda_i\nabla f_i(x)+\sum_i\nu_i\nabla h_i(x)=0$ | Lagrangian 對 $x$ 的梯度為零 |

- 推廣了「無約束凸問題：$\nabla f_0=0$ 是充要條件」[▶ 49:41](https://youtu.be/wsRznzNgTS0?t=2981)。
- 滿足 KKT 的 $(x,\lambda,\nu)$ 叫 **KKT 點**。

**任何問題（不必凸）**：若強對偶成立且 $x^\star,(\lambda^\star,\nu^\star)$ 最佳，則它們滿足 KKT（上一節 + $x^\star$ 最小化 $L$ ⇒ 梯度為零）。非凸時 KKT 點「**也許**是最佳」——就像非凸函數梯度為零的點叫駐點，「正確且合法的答案是：我不知道，也許」。

**凸問題：KKT ⇒ 最佳** [▶ 50:44](https://youtu.be/wsRznzNgTS0?t=3044)：設 $\tilde x,\tilde\lambda,\tilde\nu$ 滿足 KKT。
1. $\tilde\lambda\succeq0$，所以 $L(x,\tilde\lambda,\tilde\nu)=f_0+\sum\tilde\lambda_if_i+\sum\tilde\nu_ih_i$ 是 $x$ 的凸函數（凸 + 非負倍的凸 + 仿射）——**$\lambda$ 非負在這裡很重要**。
2. 凸函數梯度為零 ⇒ $\tilde x$ 最小化 $L$：$g(\tilde\lambda,\tilde\nu)=L(\tilde x,\tilde\lambda,\tilde\nu)$。
3. 互補鬆弛 + $h_i(\tilde x)=0$：$L(\tilde x,\tilde\lambda,\tilde\nu)=f_0(\tilde x)$。
4. 所以 $g(\tilde\lambda,\tilde\nu)=f_0(\tilde x)$：原始目標 = 對偶目標，**零間隙**，$\tilde x$ 原始最佳、$(\tilde\lambda,\tilde\nu)$ 對偶最佳。

【課本補充】若 Slater 成立，則 $x$ 最佳 $\iff$ 存在 $(\lambda,\nu)$ 使 KKT 成立（充要）。

【口頭】[▶ 52:16](https://youtu.be/wsRznzNgTS0?t=3136) 最好的記法：KKT 推廣了兩件事——凸函數「梯度為零」、以及 1830 年代的 Lagrange 乘數。微積分課上無腦學的「形成 Lagrangian、對 $x$ 偏微分設為零、對乘數偏微分設為零」，KKT 把它推廣到不等式。

---

## 10. 例：注水

[▶ 53:17](https://youtu.be/wsRznzNgTS0?t=3197)（課本 Example 5.2）

【口頭】背景：無線裝置要傳到另一個終端，把頻帶分成 512 個通道，每個通道有自己的訊雜比（因為別人也在傳）。問：用哪些通道、各用多少功率，使總位元率最大？$\log(\alpha_i+x_i)$ 乘上一些常數就是通道 $i$ 每秒能傳的位元數（$x_i$ 是功率，$\alpha_i$ 和雜訊有關）。

【課堂討論】[▶ 54:19](https://youtu.be/wsRznzNgTS0?t=3259) 誰修過資訊理論或通訊？「就這些，好。」

$$
\begin{aligned}
\text{minimize}\quad & -\sum_{i=1}^n\log(\alpha_i+x_i)\\
\text{subject to}\quad & x\succeq0,\quad\mathbf{1}^Tx=1
\end{aligned}
$$

這是「極少數可以拿出 19 世紀紙筆直接解 KKT」的問題之一。

【課本補充】KKT 的推導：
1. KKT：$x\succeq0$，$\mathbf{1}^Tx=1$，$\lambda\succeq0$，$\lambda_ix_i=0$，$-\dfrac{1}{\alpha_i+x_i}-\lambda_i+\nu=0$。
2. 由穩定性 $\lambda_i=\nu-\dfrac{1}{\alpha_i+x_i}\ge0$。
3. 若 $\nu<1/\alpha_i$：$x_i=0$ 會使 $\lambda_i<0$，所以 $x_i>0$，由互補鬆弛 $\lambda_i=0$，得 $x_i=1/\nu-\alpha_i$。
4. 若 $\nu\ge1/\alpha_i$：$x_i>0$ 會使 $\lambda_i=\nu-\frac{1}{\alpha_i+x_i}>0$，違反互補鬆弛，所以 $x_i=0$。
5. 合起來：
$$x_i=\max\left\{0,\ \frac1\nu-\alpha_i\right\},\qquad\nu\text{ 由 }\sum_i\max\left\{0,\frac1\nu-\alpha_i\right\}=1\text{ 決定}$$
（左邊對 $1/\nu$ 遞增，所以 $\nu$ 唯一。）

**解釋：注水**（water-filling）[▶ 55:52](https://youtu.be/wsRznzNgTS0?t=3352)：把 $\alpha_i$ 畫成第 $i$ 塊的地板高度，往上灌水到水位 $1/\nu$，總水量為 1。每塊的水深就是 $x_i$。
- $\alpha_i$ 大（雜訊大）：只放一點功率；太爛的通道：**不放功率**。
- 最乾淨的通道：放最多功率。

【口頭】[▶ 54:49](https://youtu.be/wsRznzNgTS0?t=3289) 1970 年代左右有人推出這個，很興奮；但「現在有點蠢」：就算有解析公式，數值方法算得一樣快；而且加其他約束照樣快。

【課堂討論】[▶ 56:23](https://youtu.be/wsRznzNgTS0?t=3383) 修過通訊的同學在那門課看過注水嗎？看過。「他們知道那是凸問題嗎？」「應該知道。」「好，有進步。在哪？」「Caltech。」「那他們會知道。」

---

## 11. 擾動與敏感度分析

[▶ 56:56](https://youtu.be/wsRznzNgTS0?t=3416)

「對偶非常酷、非常實用的應用。」

**擾動問題**：

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x)\le u_i,\quad i=1,\dots,m\\
& h_i(x)=v_i,\quad i=1,\dots,p
\end{aligned}
$$

最佳值 $p^\star(u,v)$；$p^\star(0,0)=p^\star$。

| | 意思 |
|---|---|
| $u_i>0$ | **放寬**（relax）約束 $i$：更多 $x$ 滿足。「50 毫瓦做不到，給我 55」 |
| $u_i<0$ | **收緊**（restrict）。經理去跟另一部分的設計者說「能借我 5 毫瓦嗎？」「我想可以，但會比較差。」「我們會在發獎金時記得。」 |
| $v_i\ne0$ | 等式約束的擾動，見下 |

**等式擾動的例子：電網** [▶ 58:31](https://youtu.be/wsRznzNgTS0?t=3511)：最佳化整個加州電網的潮流，等式約束是**功率守恆**：某變電站從 115 kV 線路流入的功率 = 從 15 kV 配電線流出的功率。擾動 $v_i\ne0$ 的意思是：「開一台卡車到那個變電站，接條電線，抽走（或注入）1 百萬瓦。」

【課堂討論】[▶ 1:00:35](https://youtu.be/wsRznzNgTS0?t=3635) $u_i$ 增加，最佳值怎樣？學生：下降。老師：會下降或不變——若那條約束**本來就鬆**，就不變：「你給我 55 毫瓦？我現在只用 48，連你的 50 都不需要，拿 2 回去吧。」（「別這樣說，但你可以。」）$u_i$ 減少（收緊）：上升；若約束鬆也可能不變；若緊，**一定付出代價**，甚至變成**不可行**（$p^\star=+\infty$，「最強烈的上升」）。

**單一約束時**：直接重解很多次畫曲線——例如功率上限從 10 到 80 毫瓦，每個值重新合成電路，得到「目標對分配到的功率的最佳取捨曲線」。但對偶給你**免費的局部資訊**。

**全域不等式**（由弱對偶）[▶ 1:03:43](https://youtu.be/wsRznzNgTS0?t=3823)：設原（未擾動）問題強對偶成立，$\lambda^\star,\nu^\star$ 對偶最佳，則對所有 $u,v$：

$$p^\star(u,v)\ge p^\star(0,0)-\lambda^{\star T}u-\nu^{\star T}v$$

- 這是**全域的，不是局部、不是近似**。
- 幾何：右邊是 $p^\star(u)$ 曲線在 $u=0$ 的切平面，曲線（凸問題時是凸的）在它上方。

【課本補充】證明：對任何在擾動問題中可行的 $x$，
$$p^\star(0,0)=g(\lambda^\star,\nu^\star)\le f_0(x)+\sum_i\lambda_i^\star f_i(x)+\sum_i\nu_i^\star h_i(x)\le f_0(x)+\lambda^{\star T}u+\nu^{\star T}v$$
（$\lambda_i^\star\ge0$、$f_i(x)\le u_i$、$h_i(x)=v_i$。）對所有可行 $x$ 取下確界即得。

**不對稱的解讀**（「要仔細聽英文措辭」）[▶ 1:05:17](https://youtu.be/wsRznzNgTS0?t=3917)

| 情況 | 結論 |
|---|---|
| $\lambda_i^\star$ **大**，**收緊**約束 $i$（$u_i<0$） | $p^\star$ **保證**上升，至少 $-\lambda_i^\star u_i$；可能更多，甚至到 $+\infty$ |
| $\lambda_i^\star$ **大**，**放寬**約束 $i$（$u_i>0$） | 「我**預測**會下降很多」——但**不保證**，實際下降可能比預測少 |
| $\lambda_i^\star$ **小**，放寬 | $p^\star$ 不會下降太多 |
| $\lambda_i^\star$ **小**，收緊 | $p^\star$ 可能上升很多（不能下結論） |

【口頭】放寬時的正確說法：「第一，**謝謝你給我額外資源**（一定要先說）。」「好好用。」「會的。」「目標會怎樣？」「好問題，好消息是 $\lambda^\star$ 是正的，我預測會下降不少。」「什麼叫預測？我剛給你資源耶！」「好，我預測**大概**會，但不能保證，實際下降可能比預測少。」老師畫一個「悲慘的例子」[▶ 1:07:21](https://youtu.be/wsRznzNgTS0?t=4041)：$p^\star(u)$ 在 0 處斜率很陡（乘數很大），但往右馬上變平——「你不知道，其實你剛好卡在一個極限，額外資源幫不了你。」

**哪些約束「更緊」** [▶ 1:08:24](https://youtu.be/wsRznzNgTS0?t=4104)

【口頭】電路設計有 50 條約束（相位裕度、功率、面積、擺幅、三階失真……），設計完通常只有 10–15 條是緊的。布林式的「緊」是：預算 50 用了 50。

【課堂討論】要知道「哪些比其他更緊」怎麼辦？——**看 Lagrange 乘數**。兩條都用滿預算，一條乘數很小、一條很大：前者「緊，但沒那麼緊」。就像機械系統：「它頂在牆上，但接觸力不大」；「纜線繃緊了，但只有 5 牛頓張力」。

**力學** [▶ 1:10:24](https://youtu.be/wsRznzNgTS0?t=4224)：最小化機械構型的總能量，約束如「兩點不能超過一公尺（有纜線）」「$x_1$ 不能低於地板」。乘數是最佳能量對擾動約束（例如把地板往下移）的偏導數，**物理單位就是牛頓**。

【口頭】[▶ 1:11:25](https://youtu.be/wsRznzNgTS0?t=4285) 老師很久以前替電路設計師做過一個工具：50 條約束，一欄預算、一欄設計值；乘數大就塗紅色、中等橘色、小的黃色、鬆的不塗色。設計師說：「太棒了！這是新東西！大家什麼時候知道的？」——「提示一下：這叫 Lagrange 乘數，他 1840 年就過世了。」

**局部敏感度** [▶ 1:12:26](https://youtu.be/wsRznzNgTS0?t=4346)：若 $p^\star(u,v)$ 在 $(0,0)$ 可微（老師說「常常**不**可微」）：

$$\lambda_i^\star=-\frac{\partial p^\star(0,0)}{\partial u_i},\qquad\nu_i^\star=-\frac{\partial p^\star(0,0)}{\partial v_i}$$

收緊約束成本上升，所以加負號。

**應用：節點邊際電價** [▶ 1:12:58](https://youtu.be/wsRznzNgTS0?t=4378)：電網每個節點的功率平衡等式約束，解完會得到一個乘數 = 「在那個節點抽走或注入能量，總系統成本（3,000 台發電機的營運成本，美元）的變化率」。能源業叫**節點邊際電價**（locational marginal prices）。你可以去查德州或加州某節點某小時（或某 15 分鐘）的電價，例如「每百萬瓦時 83 美元」——「就是這個」。

**應用：資料中心資源分配** [▶ 1:15:04](https://youtu.be/wsRznzNgTS0?t=4504)：350 種工作類別，分配 I/O 頻寬、核心數……乘數就是**資源的價格**。所以很多領域叫對偶變數**價格**或**影子價格**。「機械系大概不會這樣叫：『我願意付更多。』——『老兄，那是水泥地。』」

---

## 12. 預告：重新表述與對偶

[▶ 1:16:37](https://youtu.be/wsRznzNgTS0?t=4597)

【口頭】**CVXPY 做的事就只有這個**：從你的問題建立一個等價問題，再一個、再一個……42 步之後得到解法器能處理的問題，丟給解法器，再全部拉回來——每個歸約方法都附帶一個**回復方法**（「若解了歸約後的問題，怎麼解原問題」）。懂編譯器的人會認出這是**重寫系統**：產生新的、可證明語意等價的原始碼（例如兩個操作互不相干時才重新排序）。

**問題** [▶ 1:18:40](https://youtu.be/wsRznzNgTS0?t=4720)：
- $P$ 和 $\tilde P$ 等價（例如消去／加入等式約束、加鬆弛變數）。
- $D$ 是 $P$ 的 Lagrange 對偶，$\tilde D$ 是 $\tilde P$ 的對偶。
- $P$–$\tilde P$ 有關（等價），$P$–$D$、$\tilde P$–$\tilde D$ 有關（對偶）。那 $D$ 和 $\tilde D$ 呢？（強對偶下最佳值都相同。）

【口頭】把這張圖給數學系的人看，「他們的運動皮質會開始抽動，想畫上那條線、讓它變成**交換圖**（commutative diagram）……他們會去找粉筆」。下次繼續。

---

## 13. 一頁速查表

### 對偶問題

$$\text{maximize }g(\lambda,\nu)\quad\text{s.t.}\quad\lambda\succeq0\qquad(\text{永遠凸})$$

| 原問題 | 對偶 |
|---|---|
| $\min c^Tx$ s.t. $Ax=b$，$x\succeq0$ | $\max-b^T\nu$ s.t. $A^T\nu+c\succeq0$ |
| $\min c^Tx$ s.t. $Ax\preceq b$ | $\max-b^T\lambda$ s.t. $A^T\lambda+c=0$，$\lambda\succeq0$ |
| $\min x^TPx$ s.t. $Ax\preceq b$ | $\max-\tfrac14\lambda^TAP^{-1}A^T\lambda-b^T\lambda$ s.t. $\lambda\succeq0$ |
| $\min f_0(x)$ s.t. $Ax\preceq b$，$Cx=d$ | $g=-b^T\lambda-d^T\nu-f_0^*(-A^T\lambda-C^T\nu)$ |
| 最大熵 | $g=-b^T\lambda-\nu-\sum e^{-a_i^T\lambda-\nu-1}$ |

### 對偶性

| 名稱 | 內容 |
|---|---|
| 弱對偶 | $d^\star\le p^\star$，永遠成立 |
| 強對偶 | $d^\star=p^\star$；凸 + Slater（存在嚴格可行點，線性不等式免除）⇒ 成立 |
| 非凸例外 | 兩個二次式（S-引理）、特徵值問題 |
| 幾何 | $\mathcal{G}=\{(f_1,f_0)\}$；支撐線截距 = $g(\lambda)$；間隙來自 $\mathcal{G}$ 的凹陷 |

### KKT（可微）

1. $f_i\le0$，$h_i=0$　2. $\lambda\succeq0$　3. $\lambda_if_i=0$　4. $\nabla f_0+\sum\lambda_i\nabla f_i+\sum\nu_i\nabla h_i=0$

- 強對偶 + 最佳 ⇒ KKT（任何問題）。
- 凸 + KKT ⇒ 最佳（關鍵：$\lambda\succeq0$ 讓 $L$ 凸）。
- 互補鬆弛的證明：$f_0(x^\star)=g\le L(x^\star,\lambda^\star,\nu^\star)\le f_0(x^\star)$，每項 $\lambda_i^\star f_i(x^\star)\le0$ 且和為 0。

### 注水

$x_i=\max\{0,1/\nu-\alpha_i\}$，$\sum x_i=1$。

### 敏感度

| | 式子 |
|---|---|
| 全域 | $p^\star(u,v)\ge p^\star(0,0)-\lambda^{\star T}u-\nu^{\star T}v$ |
| 局部 | $\lambda_i^\star=-\partial p^\star/\partial u_i$，$\nu_i^\star=-\partial p^\star/\partial v_i$ |
| 解讀 | 大 $\lambda_i^\star$ 收緊 → **保證**大幅上升；放寬 → **預測**下降（不保證） |
| 名字 | 影子價格、節點邊際電價、接觸力／張力（牛頓） |

---

## 14. 與後續集數的連結

> 以下**不是逐字稿內容**：依課本章節與老師預告推估，做到時再更新。

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 重新表述後的對偶（$D$ vs $\tilde D$） | 第 9 集（課本 §5.7） |
| 擇一定理、無套利 | 課本 §5.8 |
| 對偶憑證、停止準則 | 內點法（課本第 11 章） |
| KKT | Newton 法、等式約束最小化（課本第 10 章） |
| 敏感度、影子價格 | 實務建模、作業 |
| 最大熵 ↔ 指數族 | 統計估計（課本第 7 章） |
| 分割的 SDP 下界 | 課本 §11.6 |

---

## 附：本集一句話總結

> **找最好的對偶下界就是對偶問題，它永遠是凸的；弱對偶永遠成立，凸問題在 Slater 這類條件下強對偶成立。強對偶給出互補鬆弛（鬆的約束乘數為零）和 KKT 條件，對凸問題 KKT 就是最佳性條件。最實用的是：最佳乘數告訴你放寬或收緊每條約束時最佳值怎麼變——它們是影子價格、電價、接觸力。**

---

## ⚠️ 待確認清單

1. 上課日期待補。
2. [▶ 47:08](https://youtu.be/wsRznzNgTS0?t=2828) 字幕「Bhattacharya inequality, 500 years earlier」人名可能聽錯。

---

*筆記依據 Stephen Boyd「Stanford EE364A Convex Optimization I（2023）」Lecture 8 錄影逐字稿（人工字幕，1:20:46）與 Boyd & Vandenberghe《Convex Optimization》§5.1.6–5.7 整理。*
