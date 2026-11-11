---
course: Stanford EE364A Convex Optimization I（2023）
episode: 7
lecture: Lecture 7
date: 待補
video: https://youtu.be/P_SuSVZnrT0
notes: 《Convex Optimization》§4.7（書頁 174–188，PDF 頁 188–202）；§5.1（書頁 215–223，PDF 頁 229–237）
---

# 第 7 集 · Lecture 7：向量最佳化、Lagrange 對偶函數 [▶ 影片](https://youtu.be/P_SuSVZnrT0)

← 上一集：[06-problem-classes](06-problem-classes.md) ｜ [總目錄](README.md) ｜ 下一集：[08-duality](08-duality.md) →

> **課程**：Stanford EE364A Convex Optimization I，2023 — 第 7 集
> **講者**：Stephen Boyd
> **來源**：YouTube 錄影逐字稿（1:20:38，人工字幕 en-US）＋ Boyd & Vandenberghe《Convex Optimization》§4.7、§5.1
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 向量最佳化](#1-向量最佳化)
  - [1.1 新的語意：最佳與 Pareto 最佳](#11-新的語意最佳與-pareto-最佳)
  - [1.2 多準則最佳化](#12-多準則最佳化)
  - [1.3 例：正則化最小平方、風險–報酬](#13-例正則化最小平方風險報酬)
  - [1.4 純量化](#14-純量化)
- [2. Lagrange 對偶](#2-lagrange-對偶)
  - [2.1 Lagrangian](#21-lagrangian)
  - [2.2 看起來很爛的近似](#22-看起來很爛的近似)
  - [2.3 對偶函數與下界性質](#23-對偶函數與下界性質)
- [3. 例子](#3-例子)
  - [3.1 線性方程的最小範數解](#31-線性方程的最小範數解)
  - [3.2 標準形式 LP](#32-標準形式-lp)
  - [3.3 對偶憑證](#33-對偶憑證)
  - [3.4 等式約束的範數最小化](#34-等式約束的範數最小化)
  - [3.5 雙向分割與譜分割](#35-雙向分割與譜分割)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 向量最佳化：最佳、Pareto 最佳 | §4.7.1–4.7.3 |
| 純量化、多準則、正則化最小平方、風險–報酬 | §4.7.4–4.7.6 |
| Lagrangian、對偶函數、下界性質 | §5.1.1–5.1.3 |
| 例：最小範數、LP、範數最小化、雙向分割 | §5.1.5 |

老師說對偶「大部分人沒看過；看過的話，教的人也沒說出 D 開頭那個字」，但你可能在統計或經濟課看過它的論證。

---

## 1. 向量最佳化

### 1.1 新的語意：最佳與 Pareto 最佳

[▶ 01:11](https://youtu.be/P_SuSVZnrT0?t=71)

之前講向量**不等式**（例如矩陣變數半正定）時，最佳化問題的語意沒變：不可行就完全不接受；可行的裡面，**純量**目標最小的最好。

現在把**目標**變成向量：

$$
\begin{aligned}
\text{minimize (w.r.t. }K)\quad & f_0(x)\in\mathbb{R}^q\\
\text{subject to}\quad & f_i(x)\le0,\quad h_i(x)=0
\end{aligned}
$$

「最小化一個向量」是什麼意思？**得改語意**。關鍵又是「最小 vs 極小」。

【口頭】[▶ 02:44](https://youtu.be/P_SuSVZnrT0?t=164) 例：「幫我找一個估計器。」「目標？」「讓我的誤差共變異數矩陣小。」——「小是什麼意思？」如果有一個選擇的共變異數矩陣比其他**所有**的都小（最小元素），那就毫無歧義。

**可達目標值集合** [▶ 03:46](https://youtu.be/P_SuSVZnrT0?t=226)：
$$\mathcal{O}=\{f_0(x)\mid x\text{ 可行}\}\subseteq\mathbb{R}^q$$

純量時 $\mathcal{O}$ 是區間，語意很簡單：最左邊那點。

| 概念 | 定義 | 圖（$K=\mathbb{R}^2_+$，左下好） |
|---|---|---|
| **最佳**（optimal） | $f_0(x)$ 是 $\mathcal{O}$ 的**最小**元素 | $\mathcal{O}$ 整個在 $f_0(x^\star)$ 右上方。「很少發生，但在統計、估計有幾個有名的例子」 |
| **Pareto 最佳**（Pareto optimal） | $f_0(x)$ 是 $\mathcal{O}$ 的**極小**元素 | $\mathcal{O}$ 左下邊界上的點 |

【口頭】[▶ 05:57](https://youtu.be/P_SuSVZnrT0?t=357)
- 現在「比較好」有意義了：左下方的點**比較好**。達到 $\mathcal{O}$ 內部某點的 $x$，「技術名詞是**愚蠢的選擇**」——有一堆點毫無疑問比它好。
- Pareto 最佳點：沒有點**嚴格**比它好。兩個 Pareto 點**無法比較**，沒有更多資訊不能說哪個好。
- 別名：**非支配**（non-dominated）。內部的點是**被支配**的（dominated）。Pareto 這個詞來自經濟學，約 1890 年代。

### 1.2 多準則最佳化

[▶ 08:01](https://youtu.be/P_SuSVZnrT0?t=481)

$K=\mathbb{R}^q_+$，$f_0(x)=(F_1(x),\dots,F_q(x))$，每個 $F_i$ 叫一個**目標**；希望全部都小。

- **最佳**：一個 $x$ **同時**最小化 $F_1,\dots,F_q$——各目標之間「沒有競爭」。【口頭】[▶ 10:37](https://youtu.be/P_SuSVZnrT0?t=637)「我設計了一個電路，同時最小化面積、靜態功耗、動態功耗、最大化放大器輸出」——太棒了，但「基本上從來不會發生」。
- **Pareto 最佳** [▶ 11:07](https://youtu.be/P_SuSVZnrT0?t=667)：**沒有人能讓你難堪**——「難堪」是指「我有個 $x$ 在每一項都和你一樣好，而且至少一項比你好」。例：兩個生產計畫，12 種資源，我在全部都不比你差、而且兩項比你好 → 我支配你，你不是 Pareto 最佳（但我也不一定是）。

【口頭】[▶ 09:03](https://youtu.be/P_SuSVZnrT0?t=543)「我不知道有哪個實際問題**不是**多準則問題。」機器學習有損失和正則項要取捨；控制要命中目標，又要權衡燃料和乘坐舒適度。有人把這變成一整個領域，老師覺得很可笑：懂了之後它非常直接，下面會看到。

**取捨曲線** [▶ 12:09](https://youtu.be/P_SuSVZnrT0?t=729)：二目標時，Pareto 最佳值構成**最佳取捨曲線**（optimal trade-off curve）。
- $\mathcal{O}$ 外左下方：「很好但**不可能**」；$\mathcal{O}$ 內部：「可能但**愚蠢**」；邊界：不愚蠢的。
- 比較曲線上兩點：上面那點第一目標贏、但用第二目標**付出代價**——兩個目標之間在**交換**，有簡單的經濟解釋。

### 1.3 例：正則化最小平方、風險–報酬

**例 1：正則化最小平方** [▶ 13:45](https://youtu.be/P_SuSVZnrT0?t=825)（課本 Example 4.9）

$$\text{minimize (w.r.t. }\mathbb{R}^2_+)\quad\left(\|Ax-b\|_2^2,\ \|x\|_2^2\right)$$

語意：選一個 $x$，你會被**兩個數字**評判：(1) 追蹤誤差／訓練誤差 $\|Ax-b\|_2^2$——「請近似滿足 $Ax=b$」；(2) $x$ 不要太大。和**嶺回歸**（ridge regression）有關。

圖（原則上把每個 $x\in\mathbb{R}^n$ 的兩個數字點出來）：只有左下邊界那條曲線（含端點）值得考慮。比較曲線上兩點時會說：「你用擬合誤差交換了參數大小。」

**例 2：風險–報酬取捨** [▶ 16:19](https://youtu.be/P_SuSVZnrT0?t=979)（課本 Example 4.10）

- $x\in\mathbb{R}^n$：投資組合，$x\succeq0$、$\mathbf{1}^Tx=1$（**混合權重**：財富投入各資產的比例）。
- 【口頭】[▶ 16:49](https://youtu.be/P_SuSVZnrT0?t=1009) 大尺度如 Stanford 的捐贈基金：資產是資產類別（美國股票、歐洲股票、另類投資、創投……）。也可以讓 $x_i<0$：持有 $-5\%$ 的中期公司債 = **借**來賣掉、期末從市場買回還人家，價格跌了就賺。「對多數人這只是文化素養，做基因的就抱歉了。」
- $p$：報酬（相對價格變化）向量，例如 $(+0.02,-0.01,+0.02)$；組合報酬 $p^Tx$。$p$ 是隨機向量，平均 $\bar p$、共變異數 $\Sigma$。
- 兩個目標：**期望報酬** $\bar p^Tx$（要大）、**報酬變異數** $x^T\Sigma x$（要小，叫**風險**；開根號是標準差、**波動率**）。

$$\text{minimize (w.r.t. }\mathbb{R}^2_+)\quad\left(-\bar p^Tx,\ x^T\Sigma x\right)\quad\text{s.t.}\quad\mathbf{1}^Tx=1,\ x\succeq0$$

【口頭】[▶ 21:33](https://youtu.be/P_SuSVZnrT0?t=1293)「高平均報酬」不代表每天都漲，只代表「如果你相信統計模型（其實不太好），把那天倒帶重來 1 萬次取平均，它漲了」——後者不可能、前者是假的。這源自 1953 年 **Harry Markowitz**。

【Q&A】[▶ 23:39](https://youtu.be/P_SuSVZnrT0?t=1419) 學生問：負號會讓它不凸嗎？答：**仍是凸的**。多準則最小化要求**每個**目標凸：風險是凸二次，負報酬是仿射（凸）。

**圖**（課本 Figure 4.12）[▶ 24:39](https://youtu.be/P_SuSVZnrT0?t=1479)：
- 上：**風險–報酬取捨曲線**（傳統畫法：橫軸風險／標準差、縱軸報酬；左上好）。老師忘了這條曲線的名字。
- 下：**堆疊圖**，每條垂直線是曲線上一點的組合配置。0% 報酬時全放 $x_4$（大概是**現金**，沒風險）；「承擔更多風險」時先不再持有現金，再加入債券、大型股、小型股（「我編的，但不完全是」）。

> 以下**不是逐字稿內容**：這條曲線一般稱為**效率前緣**（efficient frontier）。（老師說想不起名字。）

### 1.4 純量化

[▶ 26:09](https://youtu.be/P_SuSVZnrT0?t=1569)

**純量化**（scalarization）：把向量目標映成一個分數，就有了全序。

取 $\lambda\succ_{K^*}0$，解

$$\text{minimize}\quad\lambda^Tf_0(x)\quad\text{s.t.}\quad f_i(x)\le0,\ h_i(x)=0$$

- 由[第 3 集 §5](03-convex-functions.md#5-用對偶錐刻畫最小與極小元素)：它的最佳解**一定是 Pareto 最佳**。
- 若 $f_0$ 是 $K$-凸，$\lambda\succeq_{K^*}0$ 時 $\lambda^Tf_0$ 是凸的純量函數，所以這是普通的凸問題。
- 幾何 [▶ 27:43](https://youtu.be/P_SuSVZnrT0?t=1663)：$\lambda^Tf_0$ 的等高線是 $\mathcal{O}$ 空間的超平面，沿 $-\lambda$ 方向盡量推，碰到的點是 Pareto 最佳。那裡的切線斜率告訴你兩個目標的**局部交換率**——$\lambda$ 可以看成**價格向量**。

【口頭】[▶ 28:49](https://youtu.be/P_SuSVZnrT0?t=1729) 這是把很直觀的事講得很花俏。大家碰到多準則問題，直接「丟幾個權重進去」，例如機器學習「損失 + λ × 正則項」，連說都不說，因為很顯然。

**多準則的解釋** [▶ 29:51](https://youtu.be/P_SuSVZnrT0?t=1791)：$K=\mathbb{R}^q_+$ 時 $K^*=\mathbb{R}^q_+$，就是最小化 $\sum_i\lambda_iF_i(x)$，$\lambda_i>0$。
- $\lambda_i$ **字面上就是目標 $i$ 的價格**：若 $F_1=12$、$\lambda_1=10$，你付 120 美元。
- **改變價格**就得到不同的 Pareto 點，沿著取捨曲線（多目標時是取捨曲面）移動。

**例：正則化最小平方的純量化** [▶ 30:52](https://youtu.be/P_SuSVZnrT0?t=1852)

$$\text{minimize}\quad\|Ax-b\|_2^2+\gamma\|x\|_2^2$$

- $\lambda$ 乘任何正數解不變，所以可以令第一個權重為 1。第一個叫**主要目標**（訓練損失），第二個叫**次要目標**。
- $\gamma$ 是**匯率**：大的 $x$ 比大的殘差讓你煩幾倍。數值意義取決於單位。
- 解：$x=(A^TA+\gamma I)^{-1}A^Tb$（課本），就是嶺回歸。

【口頭】[▶ 32:23](https://youtu.be/P_SuSVZnrT0?t=1943) 很多時候帶上物理單位思考很棒：一個目標是燃料（公斤），另一個是乘坐平順度，例如 **jerk**（急動度）的均方根。控制和機械的方言：位置的一階導數是速度、二階加速度、三階 **jerk**、四階 **snap**；高級電梯（「不是這個國家的」）的軌跡最小化 snap，讓你完全感覺不到在動；無人機軌跡也最小化 snap。還有兩個從沒用過的：**crackle、pop**。「朋友說『我在最小化 snap 的均方根』，你問『那 crackle 或 pop 呢？』，保證他會有反應。」

【Q&A】[▶ 34:26](https://youtu.be/P_SuSVZnrT0?t=2066) 學生問：為什麼要求 $\lambda\in K^*$？答：數學上，$f_0$ 是 $K$-凸時，$\lambda\succeq_{K^*}0$ 保證 $\lambda^Tf_0$ 凸；否則不一定凸，「很好但我們解不了」。$\mathbb{R}^q_+$ 的對偶就是自己，所以多準則情況就是「取一組正權重，最小化加權和，保證得到 Pareto 點；想要另一個就換權重」。

【Q&A】[▶ 35:28](https://youtu.be/P_SuSVZnrT0?t=2128) 學生問：變動 $\lambda$ 能找到所有 Pareto 點嗎？答：（凸問題）**幾乎所有**，但拿不到某些極限點。老師指著的例子是非凸的，說他不該拿它當例子。

【課本補充】§4.7.4：凸向量最佳化問題中，每個 Pareto 最佳點都是**某個非零** $\lambda\succeq_{K^*}0$ 的純量化最佳解；但用 $\lambda\succ_{K^*}0$ 可能拿不到全部（$\lambda$ 有零分量時的極限點）。

**風險–報酬的純量化** [▶ 36:28](https://youtu.be/P_SuSVZnrT0?t=2188)：

$$\text{maximize}\quad\bar p^Tx-\gamma x^T\Sigma x\quad\text{s.t.}\quad\mathbf{1}^Tx=1,\ x\succeq0$$

$\bar p^Tx-\gamma x^T\Sigma x$ 叫**風險調整報酬**（risk-adjusted return），$\gamma$ 是**風險趨避參數**：風險讓你多煩，換算到報酬的尺度。

**另一種掃描法** [▶ 37:33](https://youtu.be/P_SuSVZnrT0?t=2253)（作業會用到）：不純量化，改成**約束**：「風險不超過 10%，最大化報酬」，然後掃描風險上限，每個值解一次、記下報酬和風險、畫出來。結果一樣。

---

## 2. Lagrange 對偶

[▶ 38:33](https://youtu.be/P_SuSVZnrT0?t=2313)

【口頭】「前兩三次看到 Lagrange 乘數，我完全不知道是什麼意思。它被當成一種**行為**來教：把目標加上約束的倍數——『那些是什麼？』『Lagrange 乘數。』『然後呢？』『取偏導數設為零。』『但那是什麼意思？』『閉嘴照做。』」老師希望下週四你會懂，他自己第一次懂是在凸最佳化的脈絡裡。「它一步步很無辜地開始，過一陣子我們就會說出完全不顯然的東西。」

### 2.1 Lagrangian

[▶ 40:05](https://youtu.be/P_SuSVZnrT0?t=2405)

【口頭】Lagrange 大約 1810、1820 年代（或更早）在做這個，當時沒有不等式約束，這個名字是「榮譽性」的歸屬。

標準形式問題（**不必是凸的**——很多有趣的應用都不凸）：

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x)\le0,\quad i=1,\dots,m\\
& h_i(x)=0,\quad i=1,\dots,p
\end{aligned}
$$

定義域 $\mathcal{D}$，最佳值 $p^\star$。**Lagrangian**（$L:\mathbb{R}^n\times\mathbb{R}^m\times\mathbb{R}^p\to\mathbb{R}$）：

$$L(x,\lambda,\nu)=f_0(x)+\sum_{i=1}^m\lambda_if_i(x)+\sum_{i=1}^p\nu_ih_i(x)$$

- $\lambda_i$：第 $i$ 條不等式的 **Lagrange 乘數**；$\nu_i$：第 $i$ 條等式的乘數。合稱**對偶變數**（dual variables）。

【口頭】[▶ 41:12](https://youtu.be/P_SuSVZnrT0?t=2472) 一種說法：原問題是**計畫經濟**——約束就是規定，違反了 SEC 會來找你；Lagrangian 是**市場版本**——「想違反那條不等式？可以，$\lambda$ 是正的，**付錢**就好。」

### 2.2 看起來很爛的近似

[▶ 42:18](https://youtu.be/P_SuSVZnrT0?t=2538)

老師畫一維圖：橫軸 $f_1(x)$，縱軸 $f_0(x)$。$f_1>0$（右邊）完全不能接受；左邊都可以，越低越好。

**把約束問題寫成無約束** [▶ 42:52](https://youtu.be/P_SuSVZnrT0?t=2572)：

$$\text{minimize}\quad f_0(x)+I_-(f_1(x)),\qquad I_-(u)=\begin{cases}0&u\le0\\\infty&u>0\end{cases}$$

$I_-$ 是指示函數，「一種情緒化、躁鬱的函數，要嘛 0 要嘛 $+\infty$」。

**Lagrangian 是把 $I_-(u)$ 換成線性函數 $\lambda u$** [▶ 43:55](https://youtu.be/P_SuSVZnrT0?t=2635)：

【口頭】「如果故事的開頭是『我要用無約束最佳化來處理約束，第一步是把這個（階梯）近似成那條（直線）』，大家都會同意這是**荒謬的近似**。」

**倉庫的例子** [▶ 44:56](https://youtu.be/P_SuSVZnrT0?t=2696)：$f_1(x)$ 是你超出倉庫容量多少。
- 原問題：超過上限完全不行；低於上限——用滿或有一堆倉庫空著——**沒有差別**。
- Lagrangian（$f_0$ 單位是美元）：$\lambda$ 是**價格**。想超過上限？可以，你要付錢租額外的空間。反過來，低於上限時你會**得到補貼**——可以把沒用的倉庫空間租出去賺錢。

「這強烈暗示：Lagrange 乘數在很多情況下會是**價格**。」

### 2.3 對偶函數與下界性質

[▶ 46:58](https://youtu.be/P_SuSVZnrT0?t=2818)

**Lagrange 對偶函數**（dual function）$g:\mathbb{R}^m\times\mathbb{R}^p\to\mathbb{R}$：

$$g(\lambda,\nu)=\inf_{x\in\mathcal{D}}L(x,\lambda,\nu)=\inf_{x\in\mathcal{D}}\left(f_0(x)+\sum_i\lambda_if_i(x)+\sum_i\nu_ih_i(x)\right)$$

- 對偶變數在應用領域各有名字：很多地方叫**影子價格**（shadow prices）；能源領域叫**節點邊際電價**（locational marginal prices）[▶ 47:28](https://youtu.be/P_SuSVZnrT0?t=2848)。
- 【口頭】和**共軛函數**的經濟解釋一樣：把 $\lambda,\nu$ 看成價格，$g$ 就是**價格的函數下的最低成本**。

**性質 1：$g$ 永遠是凹的**，即使原問題不凸 [▶ 48:28](https://youtu.be/P_SuSVZnrT0?t=2908)。

【課堂討論】為什麼？學生：凸函數的最小值……老師修正：是**仿射函數的下確界**。固定 $x$，$L$ 是 $(\lambda,\nu)$ 的仿射函數（可能係數很複雜）；一族仿射函數取下確界是凹的，**沒有例外**。

**性質 2：下界性質** [▶ 49:29](https://youtu.be/P_SuSVZnrT0?t=2969)

$$\lambda\succeq0\ \Rightarrow\ g(\lambda,\nu)\le p^\star$$

證明：設 $\tilde x$ 可行。則 $h_i(\tilde x)=0$；$\lambda_i\ge0$、$f_i(\tilde x)\le0$，所以 $\sum\lambda_if_i(\tilde x)\le0$。

$$L(\tilde x,\lambda,\nu)=f_0(\tilde x)+\sum_i\lambda_if_i(\tilde x)+\sum_i\nu_ih_i(\tilde x)\le f_0(\tilde x)$$
（第一個和 $\le0$，第二個和 $=0$。）

所以 $g(\lambda,\nu)=\inf_xL(x,\lambda,\nu)\le L(\tilde x,\lambda,\nu)\le f_0(\tilde x)$。對所有可行 $\tilde x$ 取下確界得 $g\le p^\star$。

【口頭】[▶ 50:01](https://youtu.be/P_SuSVZnrT0?t=3001)「我在用極深的數學：非負數乘非正數是非正的、非正數加起來非正、一個數加上非正數會變小。」「到深的部分我會告訴你，這還不是。」

【Q&A】[▶ 51:04](https://youtu.be/P_SuSVZnrT0?t=3064) 學生問：同樣的性質也要求 $\nu$ 非負嗎？答：**不用**。只有**不等式**的乘數要非負；$\nu$ 正負都可以——「你說『如果 $\nu$ 非負也成立』，對，但其實更強：$\nu$ 完全沒限制」。

**為什麼 $\lambda$ 要 $\ge0$**（直覺）[▶ 51:35](https://youtu.be/P_SuSVZnrT0?t=3095)：$\lambda<0$ 的直線是「付你越來越多錢去違反倉庫限制，滿足限制反而開始收你錢」——「原本只是爛近似，這個是**極度愚蠢**」。

【Q&A】[▶ 53:09](https://youtu.be/P_SuSVZnrT0?t=3189) 學生問 $\nu$ 有類似的直覺嗎？答：等式約束的「真實」懲罰是 $h_1=0$ 時為 0、其他處都 $+\infty$；Lagrangian 用直線 $\nu h_1$ 近似它，斜率正負都一樣爛。

【口頭】[▶ 54:45](https://youtu.be/P_SuSVZnrT0?t=3285)「我的重點是：這樣描述時，它**聽起來是個很爛的主意**。正常人會說『老兄，那近似太糟了，這故事不會有好結局。』但顯然它會有好結局，不然我不會講給你聽。」

【Q&A】[▶ 55:47](https://youtu.be/P_SuSVZnrT0?t=3347) 學生問 $\tilde x$ 是什麼？答：**任何**原問題的可行點。若取最佳點，右邊就是 $p^\star$。

---

## 3. 例子

### 3.1 線性方程的最小範數解

[▶ 56:22](https://youtu.be/P_SuSVZnrT0?t=3382)

$$\text{minimize }x^Tx\quad\text{s.t.}\quad Ax=b$$

（有解析解，「這很蠢，只是看它怎麼運作」。）

1. Lagrangian：$L(x,\nu)=x^Tx+\nu^T(Ax-b)$，對 $x$ 是凸二次。
2. 最小化：$\nabla_xL=2x+A^T\nu=0\Rightarrow x=-\tfrac12A^T\nu$。
3. 代回：
$$g(\nu)=\tfrac14\nu^TAA^T\nu-\tfrac12\nu^TAA^T\nu-b^T\nu=-\tfrac14\nu^TAA^T\nu-b^T\nu$$
   凹（$AA^T\succeq0$ 加負號），符合預期。

**下界**：任何 $\nu$ 都給 $p^\star\ge-\tfrac14\nu^TAA^T\nu-b^T\nu$。

【課堂討論】[▶ 57:59](https://youtu.be/P_SuSVZnrT0?t=3479) 取 $\nu=0$ 得什麼下界？學生：**0**。老師：「謝謝你給我看你的問題，由對偶我可以告訴你：最佳值永遠不會是負的。」——大家會覺得你是白痴，因為目標本來就非負。

【口頭】[▶ 58:29](https://youtu.be/P_SuSVZnrT0?t=3509) 但這已經有應用：10 億個變數，你用快速啟發式算出一個解，想知道**離最佳多遠**，就找一個好的 $\nu$ 算下界：「我在 5% 以內」——「完全夠了，原問題裡本來就沒有東西準到 5% 以上。」

### 3.2 標準形式 LP

[▶ 59:31](https://youtu.be/P_SuSVZnrT0?t=3571)

$$\text{minimize }c^Tx\quad\text{s.t.}\quad Ax=b,\ x\succeq0$$

把 $x\succeq0$ 寫成 $-x\preceq0$：

$$L(x,\lambda,\nu)=c^Tx+\nu^T(Ax-b)-\lambda^Tx=-b^T\nu+\left(c+A^T\nu-\lambda\right)^Tx$$

【課堂討論】[▶ 1:00:03](https://youtu.be/P_SuSVZnrT0?t=3603) 這是 $x$ 的什麼函數？**仿射**。仿射函數的最小值？學生：$-\infty$。老師：通常是；有一個例外——學生說「限制定義域」，不是；**線性部分為零**時，最小值就是常數：
$$\inf_x\left(p^Tx+q\right)=\begin{cases}q&p=0\\-\infty&\text{否則}\end{cases}$$

所以

$$g(\lambda,\nu)=\begin{cases}-b^T\nu&A^T\nu-\lambda+c=0\\-\infty&\text{否則}\end{cases}$$

$g$ 是限制在仿射集上的線性函數，凹。

**下界**：$A^T\nu-\lambda+c=0$ 且 $\lambda\succeq0$，等價於 $A^T\nu+c\succeq0$。所以

$$A^T\nu+c\succeq0\ \Rightarrow\ p^\star\ge-b^T\nu$$

**直接證明（只做這一次）** [▶ 1:03:05](https://youtu.be/P_SuSVZnrT0?t=3785)：設 $x$ 可行（$Ax=b$、$x\succeq0$），有人給你 $\nu$ 滿足 $A^T\nu+c\succeq0$。
1. 因為 $Ax=b$：$\nu^TAx=\nu^Tb$。
2. 「極深的事實：兩個非負向量的內積非負」：$(A^T\nu+c)^Tx\ge0$，即 $\nu^TAx+c^Tx\ge0$。
3. 代入 1：$\nu^Tb+c^Tx\ge0$，即 $c^Tx\ge-b^T\nu$。

「我完全從零推出來，沒有 Lagrangian、對偶函數那些。」

### 3.3 對偶憑證

[▶ 1:06:40](https://youtu.be/P_SuSVZnrT0?t=4000)

【口頭】之後數值解 LP（和大多數你會解的凸問題）時：
- 你得到最佳的 $x$——檢查可行，目標值例如 3.7。
- **不管你要不要**，你也會得到 $\nu$（對偶變數），而且下界是**緊的**：代進對偶目標 $g$，得到的下界**剛好等於** 3.7。
- 這叫**對偶憑證**（dual certificate）。你甚至不必相信解法器：它回傳兩樣東西——一個最佳點，和一個**簡短、自足的證明，說明沒有人能做得更好**。「抽象地看，我覺得這很美。」

### 3.4 等式約束的範數最小化

[▶ 1:08:12](https://youtu.be/P_SuSVZnrT0?t=4092)

$$\text{minimize }\|x\|\quad\text{s.t.}\quad Ax=b$$

$$g(\nu)=\inf_x\left(\|x\|-\nu^TAx+b^T\nu\right)=\begin{cases}b^T\nu&\|A^T\nu\|_*\le1\\-\infty&\text{否則}\end{cases}$$

- $b^T\nu$ 和 $x$ 無關，提出來；剩下「範數減線性函數」的下確界，和**共軛函數**有關，結果只有 0 或 $-\infty$。
- $\|v\|_*=\sup_{\|u\|\le1}u^Tv$ 是**對偶範數**。

【課本補充】§5.1.5 的關鍵事實：$\inf_x(\|x\|-y^Tx)=0$ 若 $\|y\|_*\le1$，否則 $-\infty$。（$\|y\|_*\le1$ 時 $y^Tx\le\|x\|\|y\|_*\le\|x\|$，下確界在 $x=0$ 取 0；$\|y\|_*>1$ 時有 $\|u\|\le1$ 使 $y^Tu>1$，取 $x=tu$、$t\to\infty$，$\|x\|-y^Tx\le t(1-y^Tu)\to-\infty$。）

**下界**：任何滿足 $\|A^T\nu\|_*\le1$ 的 $\nu$，$p^\star\ge b^T\nu$。

【口頭】[▶ 1:09:43](https://youtu.be/P_SuSVZnrT0?t=4183) 應用：衛星**最省燃料軌跡**，把衛星從現在的位置送到該在的位置，大概用 $\ell_1$ 範數。任何滿足條件的向量 $\nu$，$b^T\nu$ 就是「至少要花多少燃料」的下界。「已經有很強的暗示：這東西非常有用。」

### 3.5 雙向分割與譜分割

[▶ 1:10:45](https://youtu.be/P_SuSVZnrT0?t=4245)

**雙向分割問題**（two-way partitioning）：

$$\text{minimize }x^TWx\quad\text{s.t.}\quad x_i^2=1,\ i=1,\dots,n$$

$W\in\mathbf{S}^n$。$x_i=+1$ 表示物件 $i$ 在第一組，$-1$ 在第二組。

**目標的意思** [▶ 1:11:17](https://youtu.be/P_SuSVZnrT0?t=4277)：
$$x^TWx=\sum_{i,j}W_{ij}x_ix_j,\qquad x_ix_j=\begin{cases}+1&i,j\text{ 同組}\\-1&\text{不同組}\end{cases}$$
所以 $x^TWx$ = 同組的 $W_{ij}$ 和 − 不同組的 $W_{ij}$ 和。把一群人分成兩隊：$W_{ij}>0$ 代表 $i$、$j$ 合不來（同組要付 $W_{ij}$，分開反而賺 $W_{ij}$）；$W_{ij}<0$ 代表很合得來。

**非凸**，兩個原因：$W$ 不一定半正定；$x_i^2=1$ 不是仿射（$x_i^2\le1$ 才凸）。

**對偶函數** [▶ 1:13:58](https://youtu.be/P_SuSVZnrT0?t=4438)：

$$L(x,\nu)=x^TWx+\sum_i\nu_i(x_i^2-1)=x^T\left(W+\mathbf{diag}(\nu)\right)x-\mathbf{1}^T\nu$$

【課堂討論】[▶ 1:14:28](https://youtu.be/P_SuSVZnrT0?t=4468)「二次型最小化的對話」：$\inf_xx^TAx$（$A$ 對稱）是什麼？
- $A$ 有負特徵值（或任何讓二次型為負的點）：沿那個方向走越遠越負（二次地），$-\infty$。
- $A\succeq0$：0（取 $x=0$，而且不可能更小）。

$$g(\nu)=\begin{cases}-\mathbf{1}^T\nu&W+\mathbf{diag}(\nu)\succeq0\\-\infty&\text{否則}\end{cases}$$

**下界**：任何使 $W+\mathbf{diag}(\nu)\succeq0$ 的 $\nu$，$p^\star\ge-\mathbf{1}^T\nu$。「代入不同的數字就能得到各種有名的界。」

【課本補充】例：取 $\nu=-\lambda_{\min}(W)\mathbf{1}$，則 $W+\mathbf{diag}(\nu)=W-\lambda_{\min}(W)I\succeq0$，得 $p^\star\ge n\lambda_{\min}(W)$。

**譜分割**（spectral partitioning）[▶ 1:16:32](https://youtu.be/P_SuSVZnrT0?t=4592)

【課堂討論】誰看過？一隻手。老師：「每個人都要知道，不懂它就沒辦法做正經的街頭格鬥應用數學，分割問題到處都是。」

- **在解什麼**：雙向分割（非凸、組合問題）的近似解。
- **步驟**：
  1. **鬆弛**：把 $x_i^2=1$（對每個 $i$）換成 $\sum_ix_i^2=n$（若前者成立，後者一定成立）：
  $$\text{minimize }x^TWx\quad\text{s.t.}\quad\|x\|_2^2=n$$
  2. 這仍不凸，但它是「大約七個我們能解的非凸問題之一」——**特徵值問題**。【課堂討論】解是什麼？學生：最小的那個。對：$W$ **最小特徵值**對應的特徵向量，縮放到 $\|x\|_2^2=n$。最佳值 $n\lambda_{\min}(W)$ 是原問題的**下界**（因為是鬆弛）。
  3. 【課堂討論】[▶ 1:18:34](https://youtu.be/P_SuSVZnrT0?t=4714) 得到的 $x$ 是浮點數，不是 $\pm1$。學生建議：**四捨五入**——取**符號** $x_i\leftarrow\mathrm{sign}(x_i)$。「完成，恭喜，這就是譜分割。」
- 老師說還有一點沒講：可以**調整 $W$ 的對角線**讓它稍微好一點。適用於巨大的問題，效果很好。
- **什麼時候會失敗**：取符號只是啟發式，得到的分割不保證最佳；只知道它和下界 $n\lambda_{\min}(W)$ 的差距。

> 以下**不是逐字稿內容**，是依課本推論的：「調整對角線」對應選不同的 $\nu$——用對偶函數找最好的 $\nu$（最大化 $-\mathbf{1}^T\nu$ s.t. $W+\mathbf{diag}(\nu)\succeq0$，是個 SDP），會得到比 $n\lambda_{\min}(W)$ 更好的下界（課本 §5.2.4、Exercise 5.39）。

【Q&A】[▶ 1:19:37](https://youtu.be/P_SuSVZnrT0?t=4777) 學生問：$W$ 必須對稱或半正定嗎？答：非對稱沒意義（二次型只看對稱部分 $(W+W^T)/2$）；**不必半正定**。只要 $W$ 對稱，鬆弛問題就能完全解：最小特徵向量縮放，正負特徵值都無所謂。

---

## 4. 一頁速查表

### 向量最佳化

| 概念 | 定義 |
|---|---|
| 可達集 | $\mathcal{O}=\{f_0(x)\mid x\text{ 可行}\}$ |
| 最佳 | $f_0(x^\star)$ 是 $\mathcal{O}$ 的最小元素（同時最小化所有目標，罕見） |
| Pareto 最佳 | 極小元素 = 非支配 = 沒人能在全部不差、至少一項更好 |
| 純量化 | $\lambda\succ_{K^*}0$，min $\lambda^Tf_0(x)$ → 必為 Pareto；$\lambda$ = 價格 |
| 正則化 LS | $\|Ax-b\|_2^2+\gamma\|x\|_2^2$，$x=(A^TA+\gamma I)^{-1}A^Tb$ |
| 風險–報酬 | $\max\bar p^Tx-\gamma x^T\Sigma x$；或約束風險、掃描 |

### Lagrange 對偶

$$L(x,\lambda,\nu)=f_0(x)+\sum\lambda_if_i(x)+\sum\nu_ih_i(x),\qquad g(\lambda,\nu)=\inf_xL(x,\lambda,\nu)$$

| 性質 | 關鍵一步 |
|---|---|
| $g$ 凹（永遠） | 仿射函數 $(\lambda,\nu)\mapsto L$ 的下確界 |
| $\lambda\succeq0\Rightarrow g(\lambda,\nu)\le p^\star$ | 可行 $\tilde x$：$\lambda_if_i(\tilde x)\le0$、$h_i(\tilde x)=0$ |
| 直覺 | 把指示函數 $I_-(u)$ 換成 $\lambda u$（價格）；$\lambda<0$ 荒謬 |

### 對偶函數例子

| 原問題 | $g$ | 下界 |
|---|---|---|
| $\min x^Tx$ s.t. $Ax=b$ | $-\tfrac14\nu^TAA^T\nu-b^T\nu$ | 任何 $\nu$ |
| $\min c^Tx$ s.t. $Ax=b$，$x\succeq0$ | $-b^T\nu$ 若 $A^T\nu-\lambda+c=0$ | $A^T\nu+c\succeq0\Rightarrow p^\star\ge-b^T\nu$ |
| $\min\|x\|$ s.t. $Ax=b$ | $b^T\nu$ 若 $\|A^T\nu\|_*\le1$ | 同左 |
| $\min x^TWx$ s.t. $x_i^2=1$ | $-\mathbf{1}^T\nu$ 若 $W+\mathbf{diag}(\nu)\succeq0$ | $\nu=-\lambda_{\min}\mathbf{1}\Rightarrow p^\star\ge n\lambda_{\min}(W)$ |

- 仿射函數 $\inf=q$ 若線性部分為零，否則 $-\infty$；二次型 $\inf=0$ 若 $\succeq0$，否則 $-\infty$。
- 對偶憑證：解法器同時回傳 $x^\star$ 和使 $g=f_0(x^\star)$ 的對偶變數。
- 譜分割：最小特徵向量 → 取符號。

---

## 5. 與後續集數的連結

> 以下**不是逐字稿內容**：依課本章節與老師預告推估，做到時再更新。

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 對偶問題、弱／強對偶、Slater 條件 | 第 8 集（課本 §5.2） |
| 對偶函數與共軛函數的關係 | 課本 §5.1.6 |
| Lagrange 乘數 = 價格、敏感度 | 課本 §5.4、§5.6 |
| KKT 條件、互補鬆弛 | 課本 §5.5 |
| 對偶憑證、停止準則 | 課本 §5.5.1、內點法 |
| 正則化最小平方、取捨曲線 | 近似與擬合（課本第 6 章） |
| 雙向分割的 SDP 界 | 課本 §5.2.4、§11.6 |

---

## 附：本集一句話總結

> **向量目標要換語意：最佳是同時最小化所有目標（罕見），Pareto 最佳是沒有人能支配你；用正權重（價格）純量化就得到 Pareto 點。Lagrangian 把硬約束換成「付錢就能違反」的線性懲罰——看起來是很爛的近似，但它給出的對偶函數永遠是凹的，而且（$\lambda\succeq0$ 時）永遠是原問題最佳值的下界；解法器回傳的對偶變數就是「沒人能做得更好」的證明。**

---

*筆記依據 Stephen Boyd「Stanford EE364A Convex Optimization I（2023）」Lecture 7 錄影逐字稿（人工字幕，1:20:38）與 Boyd & Vandenberghe《Convex Optimization》§4.7、§5.1 整理。*
