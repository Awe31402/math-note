---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 13
lecture: Lecture 13
date: 待補（第 7 週週一）
video: https://youtu.be/RtJSHiqOdgQ
notes: 課本沒有對應章節（系統辨識、適應控制、MRAC 都不在《Principles of Robot Autonomy》裡）
---

# 第 13 集 · Lecture 13：學習型控制入門（Intro to Learning） [▶ 影片](https://youtu.be/RtJSHiqOdgQ)

← 上一集：[12-feasibility-of-mpc](12-feasibility-of-mpc.md) ｜ [總目錄](README.md) ｜ 下一集：[14-intro-to-il-and-rl](14-intro-to-il-and-rl.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 13 集
> **講者**：待確認（本集沒有自我介紹；口頭習慣「if you wish」「kind of」與第 3–6 集的 Daniele Gammelli 相同，推測是他）
> **來源**：YouTube 錄影逐字稿（1:20:05，上傳者提供的人工字幕）；課本無對應章節，本集只靠逐字稿
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【Q&A】` 學生提問與回答
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 面對不確定性的三種做法](#1-面對不確定性的三種做法)
- [2. 學習型控制的地圖](#2-學習型控制的地圖)
  - [2.1 學什麼：直接 vs 間接](#21-學什麼直接-vs-間接)
  - [2.2 怎麼學：0 回合、1 回合、多回合](#22-怎麼學0-回合1-回合多回合)
- [3. 系統辨識](#3-系統辨識)
  - [3.1 最小平方法](#31-最小平方法)
  - [3.2 用在線性動態](#32-用在線性動態)
  - [3.3 估計量的性質：無偏與共變異數](#33-估計量的性質無偏與共變異數)
  - [3.4 實務問題：模型準不等於控制好](#34-實務問題模型準不等於控制好)
- [4. 適應控制](#4-適應控制)
- [5. 複習：Lyapunov 全域穩定](#5-複習lyapunov-全域穩定)
  - [5.1 例子：質量－彈簧－阻尼](#51-例子質量彈簧阻尼)
- [6. 模型參考適應控制（MRAC）](#6-模型參考適應控制mrac)
  - [6.1 四個成分](#61-四個成分)
  - [6.2 質量已知時](#62-質量已知時)
  - [6.3 質量未知：加上適應律](#63-質量未知加上適應律)
  - [6.4 Lyapunov 分析](#64-lyapunov-分析)
- [7. 演算法整理](#7-演算法整理)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/RtJSHiqOdgQ?t=5) **課程第二部分開始。**

回顧第一部分（課程地圖的下半部）：

| 方法 | 優點 | 缺點 |
|---|---|---|
| 開迴路（間接法、直接法） | 快、可靠 | 只對給定的初始條件 |
| 閉迴路（DP、HJB、HJI） | 給出任何狀態下的行為規則，較強 | 計算昂貴 |
| MPC | 反覆解開迴路問題，得到閉迴路的表現 | — |

[▶ 01:36](https://youtu.be/RtJSHiqOdgQ?t=96) 這些方法都假設**知道動態**（解析式或微分方程）。第二部分**放寬這個假設**：事先**不知道**模型的動態——**學習型**的設定。

今天：

- 學習型控制的大致地圖。
- 課程地圖左上角：比較**古典**的學習方式——**系統辨識**和**適應控制**。
- 兩種適應控制：**MRAC**（模型參考適應控制）和 **MIAC**（模型辨識適應控制）。

> ⚠️ 逐字稿缺字 [▶ 02:06](https://youtu.be/RtJSHiqOdgQ?t=126)：字幕寫「MAIC」，依「Model Identification Adaptive Control」應為 **MIAC**。

> 本集課本沒有對應內容，全部依逐字稿整理。

---

## 1. 面對不確定性的三種做法

[▶ 02:38](https://youtu.be/RtJSHiqOdgQ?t=158) 熟悉的設定：控制器 → 系統 → 感測器量輸出 → 跟**參考**比較 → 控制器。問題：系統有**不確定性**或**未建模的效應**怎麼辦？

| 做法 | 想法 | 例子／評價 |
|---|---|---|
| **1. 靠回饋** [▶ 03:41](https://youtu.be/RtJSHiqOdgQ?t=221) | 很多時候不確定性影響很小，回饋控制就足以補償 | 無人機有小小的未建模風；用 PID 追蹤參考軌跡就夠了 |
| **2. 強健控制** [▶ 04:42](https://youtu.be/RtJSHiqOdgQ?t=282) | 像第 10 集的極小極大：假設擾動是對手，對**最壞情況**強健 | 很好，但行為可能**太防禦、太保守**（「殺人司機」那個「蠻殘忍的例子」） |
| **3. 資料驅動** [▶ 06:16](https://youtu.be/RtJSHiqOdgQ?t=376) | 收集系統行為和狀態轉移的例子，**從資料學**近似模型 | 無人機存下以前飛行的紀錄，用來學動態——**本集和之後幾週的重點** |

【口頭】這是好的心智模型：有不確定性時，也許回饋就夠；也許要很保守、考慮最壞情況；也許要用資料驅動。

---

## 2. 學習型控制的地圖

### 2.1 學什麼：直接 vs 間接

[▶ 07:52](https://youtu.be/RtJSHiqOdgQ?t=472)

| 類型 | 用量測做什麼 |
|---|---|
| **直接**（direct） | 直接改進**控制器** |
| **間接**（indirect） | 先學一個近似的**動態模型**，再用模型改進控制器（中間目標：**系統辨識**） |

| 本課的方法 | 類型 |
|---|---|
| 直接適應控制（MRAC） | 直接 |
| 間接適應控制（MIAC）、系統辨識 | 間接 |
| 模仿學習、無模型 RL | 直接（之後幾週） |
| 基於模型的 RL | 間接（之後幾週） |

### 2.2 怎麼學：0 回合、1 回合、多回合

[▶ 09:25](https://youtu.be/RtJSHiqOdgQ?t=565)

| 情境 | 意思 | 例子 |
|---|---|---|
| **0 回合**（zero episodes）＝系統辨識 | 事先收集好資料集（某個策略控制系統的軌跡），**完全離線**地估計參數或模型，再改進控制器 | 用以前的飛行紀錄 |
| **1 回合**（one episode）＝線上適應 [▶ 09:55](https://youtu.be/RtJSHiqOdgQ?t=595) | 一邊控制系統一邊學習、適應 | 四旋翼載著**未知質量** $m$ 的貨物；沒辦法從以前的飛行估 $m$，要在飛行中**線上**估計並適應 |
| **多回合**（multiple episodes）＝經典 RL [▶ 11:02](https://youtu.be/RtJSHiqOdgQ?t=662) | 有可以**無限重置**的環境；學習發生在回合**之間** | 下西洋棋：每局開始重置，一局下完更新策略，再下一局 |

【口頭】[▶ 12:32](https://youtu.be/RtJSHiqOdgQ?t=752) 界線不是那麼嚴格。例如線上 RL 通常假設可重置的環境（多回合），但**離線 RL** 屬於 0 回合。不要太死板地看。

【Q&A】[▶ 13:03](https://youtu.be/RtJSHiqOdgQ?t=783) 學生問 1 回合和多回合的差別？答：兩者都跟環境互動。多回合的差別是有**回合的結構**，可以跨回合學習。用西洋棋比喻：多回合 = 下無限多局，每局之間改進；1 回合 = 在**一局之內**學會下棋。

【Q&A】[▶ 14:04](https://youtu.be/RtJSHiqOdgQ?t=844) 學生問：多回合是不是能探索到一次跑不到的狀態？答：對，在同一個環境裡用不同方式行動，可以探索狀態空間的不同部分。

【Q&A】[▶ 14:37](https://youtu.be/RtJSHiqOdgQ?t=877) 學生問：把一次駕駛紀錄切成多段時間序列，算多回合嗎？答：比較像 **0 回合**——你有一個軌跡資料集，切成小段建立「預測下一個狀態」（前向動態）的問題。因為你不是那個收集資料的 agent。多回合情境下，**你的策略決定你得到的經驗**。0 回合時，你大概不會讓一個從零開始的神經網路開車（一定會撞）；但西洋棋可以一開始很爛、慢慢變好。

---

## 3. 系統辨識

[▶ 16:09](https://youtu.be/RtJSHiqOdgQ?t=969) 很多問題**不用線上學**：收集以前的實驗或行為資料集 → 建立**資料驅動的動態模型** → 用它**取代**你對動態的知識，再套用任何控制工具（前半學期學的）。

傳統工具：**線性迴歸**。

### 3.1 最小平方法

[▶ 17:43](https://youtu.be/RtJSHiqOdgQ?t=1063) **模型**：

$$y=\theta^\top z+\varepsilon$$

- $y$：輸出；$z$：輸入；$\theta$：要學的參數；$\varepsilon$：過程本身的雜訊。

**資料集**：$\mathcal D=\{(z_i,y_i)\}_{i=1}^N$。

**最小平方損失** [▶ 18:45](https://youtu.be/RtJSHiqOdgQ?t=1125)：

$$\hat\theta=\arg\min_\theta\sum_{i=1}^N\left(y_i-\theta^\top z_i\right)^2=\arg\min_\theta\left\|y-Z\theta\right\|_2^2$$

$Z$ 是把輸入向量堆疊起來的矩陣（每列一個 $z_i^\top$）。

**解** [▶ 19:48](https://youtu.be/RtJSHiqOdgQ?t=1188)：凸函數 → 令梯度 = 0（必要且充分）：

$$
\begin{aligned}
\nabla_\theta\left(y^\top y-2\theta^\top Z^\top y+\theta^\top Z^\top Z\theta\right)&=-2Z^\top y+2Z^\top Z\theta=0 \\
\Rightarrow\quad \hat\theta&=\left(Z^\top Z\right)^{-1}Z^\top y
\end{aligned}
$$

### 3.2 用在線性動態

[▶ 22:14](https://youtu.be/RtJSHiqOdgQ?t=1334) 假設系統：

$$x_{t+1}=Ax_t+Bu_t+\varepsilon_t=\begin{pmatrix}A&B\end{pmatrix}\begin{pmatrix}x_t\\u_t\end{pmatrix}+\varepsilon_t$$

對應上一節的記號：

| 最小平方 | 系統辨識 |
|---|---|
| $y$ | $x_{t+1}$ |
| $z$ | $(x_t,u_t)$ |
| $\theta$ | $(A,B)$ |

**資料** [▶ 23:55](https://youtu.be/RtJSHiqOdgQ?t=1435)：收集系統的軌跡（狀態和控制隨時間的序列），切成 $\left((x_t,u_t),\ x_{t+1}\right)$ 的配對。

這就是「從資料學近似動態模型」的意思：把系統演化的例子改寫成迴歸問題，從「目前狀態 + 控制」映射到「下一個狀態」。

**實務註記** [▶ 25:33](https://youtu.be/RtJSHiqOdgQ?t=1533)：

- 資料很多時 $Z$ 很大，求 $(Z^\top Z)^{-1}$ 很貴。有**遞迴**形式（recursive least squares）避免反覆求大矩陣的逆——資料一直流進來時很有用。
- 這裡是離散時間，連續時間也有對應版本。

**理論結果** [▶ 26:38](https://youtu.be/RtJSHiqOdgQ?t=1598)：

- 如果雜訊 $\varepsilon_t$ **零均值、互不相關、變異數相同且有限**，這個估計量是**最佳線性無偏估計量**（best linear unbiased estimator，BLUE）。
- 如果雜訊是**高斯**的，它也是**最大概似估計量**（maximum likelihood estimator，MLE）。

> 以下**不是逐字稿內容**：第一點就是統計學的 **Gauss–Markov 定理**，講者沒說出名字。

### 3.3 估計量的性質：無偏與共變異數

[▶ 27:09](https://youtu.be/RtJSHiqOdgQ?t=1629) 問：$\hat\theta$ 什麼時候會收斂到真值 $\theta$？

講者畫圖：橫軸是收集的資料量，縱軸是估計 $\hat\theta$，真值 $\theta^*$ 是一條水平線。估計過程本身是**隨機變數**（因為 $\hat\theta$ 依賴有雜訊的 $y$）。想知道：

1. 平均來說是否以真值為中心？
2. 資料越多，它的變動會怎樣？

**把 $\hat\theta$ 寫開** [▶ 28:48](https://youtu.be/RtJSHiqOdgQ?t=1728)：代入 $y=Z\theta+\varepsilon$：

$$\hat\theta=\left(Z^\top Z\right)^{-1}Z^\top\left(Z\theta+\varepsilon\right)=\theta+\left(Z^\top Z\right)^{-1}Z^\top\varepsilon$$

**均值** [▶ 29:57](https://youtu.be/RtJSHiqOdgQ?t=1797)：唯一的隨機量是 $\varepsilon$，其他都能移出期望；$\mathbb E[\varepsilon]=0$：

$$\mathbb E[\hat\theta]=\theta$$

**無偏**：平均來說會收斂到真值。

**共變異數** [▶ 30:58](https://youtu.be/RtJSHiqOdgQ?t=1858)：用 $\mathrm{Cov}(Mx)=M\,\mathrm{Cov}(x)M^\top$（$M=(Z^\top Z)^{-1}Z^\top$），以及 $\mathrm{Cov}(\varepsilon)=\sigma^2I$（不相關、同變異數 → 只有對角線、都是 $\sigma^2$）：

$$\mathrm{Cov}(\hat\theta)=\left(Z^\top Z\right)^{-1}Z^\top\left(\sigma^2I\right)Z\left(Z^\top Z\right)^{-1}=\sigma^2\left(Z^\top Z\right)^{-1}=\sigma^2\left(\sum_{t=1}^N\begin{pmatrix}x_t\\u_t\end{pmatrix}\begin{pmatrix}x_t\\u_t\end{pmatrix}^\top\right)^{-1}$$

**希望共變異數 → 0** [▶ 33:35](https://youtu.be/RtJSHiqOdgQ?t=2015)：逆矩陣在分母，所以要那個總和隨 $N$ **趨近無限大**。

- 系統一直運作、而且運作得**不平凡**（例如不是一直停在 0），總和就會趨近無限大，共變異數趨近 0。
- 這叫**持續激勵**（persistent excitation）：要一直用**有意義的方式**刺激系統。

【Q&A】[▶ 34:36](https://youtu.be/RtJSHiqOdgQ?t=2076) 學生問：有沒有直覺說明 $Z^\top Z$ 什麼時候可逆？答：這裡簡化了。完整推導有一些正則條件會說明何時可逆，講者可以提供參考。這裡只是快速帶到結果：用線性模型估線性系統，這個估計量無偏，在一些正則條件下共變異數收斂到 0。

### 3.4 實務問題：模型準不等於控制好

[▶ 36:13](https://youtu.be/RtJSHiqOdgQ?t=2173)

1. **資料預算**：需要多少資料？怎麼量化參數估計「夠好」？
2. **真正在乎的是控制表現** [▶ 36:44](https://youtu.be/RtJSHiqOdgQ?t=2204)，不是模型準確度。

   講者畫了極端例子：控制律依參數 $\theta$ 的**符號**跳變（$\theta<0$ 用一種控制，$\theta>0$ 用另一種）。真值 $\theta^*$ 在正的那邊。兩個估計：
   - $\hat\theta_1$：離真值比較遠，但在**對的一側**。
   - $\hat\theta_2$：離真值比較近，但在**錯的一側**。

   從統計（距離）來看 $\hat\theta_2$ 比較好；從控制來看 $\hat\theta_1$ 才對。

   【口頭】這是系統辨識的主要缺點之一：引入了「模型估計」這個中間目標，它**不一定**跟控制表現一致。
3. **怎麼收集資料** [▶ 38:56](https://youtu.be/RtJSHiqOdgQ?t=2336)：邊收集邊學？收集時有**安全**考量？只有部分知識時操作系統，可能要越保守越好。
4. **模型家族夠不夠表達** [▶ 39:27](https://youtu.be/RtJSHiqOdgQ?t=2367)：這裡真實系統是線性、我們也估線性，剛好吻合。但實際上不知道系統怎麼運作——有「資料量 vs 模型表達力」的取捨。

---

## 4. 適應控制

[▶ 40:28](https://youtu.be/RtJSHiqOdgQ?t=2428) 系統辨識是 **0 回合**；**適應控制**（adaptive control）是 **1 回合**：一邊即時操作系統，一邊**線上適應**改進控制。

| | 做法 | 類型 |
|---|---|---|
| **MRAC**（model reference adaptive control，模型參考適應控制） | 直接調整控制器 | 直接 |
| **MIAC**（model identification adaptive control，模型辨識適應控制） | 先估模型（名字裡有 identification），再用它改進控制 | 間接 |

**適應控制的經典設定** [▶ 41:28](https://youtu.be/RtJSHiqOdgQ?t=2488)：文獻很傳統，通常**不是**「最佳」適應控制——不是最佳化某個表現指標或成本，而是證明**耦合系統的穩定性**：

$$\text{控制器}\ +\ \text{適應機制}\ +\ \text{系統動態}$$

你要自己設計控制器和適應機制（怎麼根據經驗調參數），然後分析整個閉迴路耦合系統是否穩定。

---

## 5. 複習：Lyapunov 全域穩定

[▶ 42:33](https://youtu.be/RtJSHiqOdgQ?t=2553) 本課分析穩定性的工具。

自主系統 $\dot x=f(x)$（受策略控制的系統也能寫成自主系統：$\dot x=f(x,\pi(x))$）。$x^*$ 是平衡點：$f(x^*)=0$。

> **Lyapunov 全域穩定定理** [▶ 43:34](https://youtu.be/RtJSHiqOdgQ?t=2614)
>
> 如果存在函數 $V$ 使得
> 1. $V(x)>0$，$\forall x\ne x^*$；$V(x^*)=0$
> 2. $\dot V(x)<0$，$\forall x\ne x^*$
> 3. **徑向無界**（radially unbounded）：$\|x\|\to\infty\Rightarrow V(x)\to\infty$
>
> 那麼 $x^*$ 是**全域漸近穩定**的。

- 上週只講了局部版本；第 3 條是為了**全域**而加強的條件。
- 圖像 [▶ 45:11](https://youtu.be/RtJSHiqOdgQ?t=2711)：二維狀態 $(x_1,x_2)$ 上一個碗形的 $V$；照系統動態走，能量耗散，到達平衡點。除了平衡點都是正的；離越遠越大。
- 好處：不用積分動態、不用對每個初始條件求解，只要找到滿足條件的函數。

### 5.1 例子：質量－彈簧－阻尼

[▶ 46:45](https://youtu.be/RtJSHiqOdgQ?t=2805) 先在**沒有控制**的系統上示範 Lyapunov 分析。

質量 $m$、彈簧 $k$、阻尼 $d$（外力 $F=0$），要證明穩定到位置 0、速度 0：

$$m\ddot x=-d\dot x-kx$$

**候選 Lyapunov 函數 = 系統能量**（位能 + 動能）[▶ 47:55](https://youtu.be/RtJSHiqOdgQ?t=2875)：

$$E(x,\dot x)=\frac12kx^2+\frac12m\dot x^2$$

> ⚠️ 逐字稿缺字 [▶ 47:55](https://youtu.be/RtJSHiqOdgQ?t=2875)：字幕寫「1/2 k x **dot**」，位能項應為 $\frac12kx^2$。

- 條件 1、3：一眼看出——$E>0$ 除非 $x=\dot x=0$；$x$ 變大 $E$ 也變大。
- 條件 2 [▶ 49:30](https://youtu.be/RtJSHiqOdgQ?t=2970)：

$$\dot E=kx\dot x+m\dot x\ddot x=kx\dot x+\dot x\left(-d\dot x-kx\right)=-d\dot x^2$$

講者說這「除了平衡點外都是負的」，滿足條件 2。

> 以下**不是逐字稿內容**，是補充說明：嚴格來說 $\dot E=-d\dot x^2$ 在 $\dot x=0$、$x\ne 0$ 的點也是 0，所以只是**半負定**（$\le 0$），不嚴格滿足條件 2。要完成證明通常用 **LaSalle 不變原理**：在 $\dot E=0$ 的集合（$\dot x=0$）上，唯一能一直待著的軌跡是 $x=0$（否則彈簧力會讓 $\ddot x\ne 0$），所以仍然收斂到原點。

---

## 6. 模型參考適應控制（MRAC）

### 6.1 四個成分

[▶ 51:07](https://youtu.be/RtJSHiqOdgQ?t=3067)

1. **受控體**（plant）：含**未知參數**的系統。
2. **參考模型**（reference model）：簡潔地指定系統**想要的輸出**。另一種指定表現的方式——不用目標函數，而是看**跟參考訊號的距離**。
3. **回饋控制律**：含**可調參數**。
4. **適應機制**：怎麼調那些參數（要我們自己設計）。

### 6.2 質量已知時

[▶ 52:47](https://youtu.be/RtJSHiqOdgQ?t=3167) 先在「一切已知」的情況分析，再加入未知參數和適應機制重做一次。

**系統**：雙積分器
$$m\ddot x=u$$

**參考模型** [▶ 54:20](https://youtu.be/RtJSHiqOdgQ?t=3260)：引入虛擬變數 $x_m$（m = model），代表「理想的」受控質量反應。給定位置指令 $r(t)$：

$$\ddot x_m+k_d\dot x_m+k_px_m=k\,r(t)$$

$k$ 們是設計者選的增益。

> ⚠️ 待確認 [▶ 55:26](https://youtu.be/RtJSHiqOdgQ?t=3326)：右邊字幕寫「kr of t」，是 $k_r\,r(t)$ 還是 $k_p\,r(t)$ 待對照投影片。

**追蹤誤差**：$\tilde x=x-x_m$。

**控制律**（質量已知）[▶ 56:33](https://youtu.be/RtJSHiqOdgQ?t=3393)：

$$u=m\left(\ddot x_m-2\lambda\dot{\tilde x}-\lambda^2\tilde x\right),\qquad\lambda>0$$

【口頭】[▶ 57:04](https://youtu.be/RtJSHiqOdgQ?t=3424) 這些東西哪來的？實際設計時要自己想出參考訊號、控制律。這裡假設有人給我們，只示範之後的穩定性分析。實務上是反覆嘗試：試某個參考模型 → 證不出穩定 → 再改。

**閉迴路** [▶ 59:10](https://youtu.be/RtJSHiqOdgQ?t=3550)：代入 $m\ddot x=u$：

$$m\ddot x=m\left(\ddot x_m-2\lambda\dot{\tilde x}-\lambda^2\tilde x\right)\ \Rightarrow\ m\left(\ddot{\tilde x}+2\lambda\dot{\tilde x}+\lambda^2\tilde x\right)=0$$

（$\ddot x-\ddot x_m=\ddot{\tilde x}$；$m$ 可以消掉。）

解這個 ODE [▶ 60:20](https://youtu.be/RtJSHiqOdgQ?t=3620)：

$$\tilde x(t)=\left(c_0+c_1t\right)e^{-\lambda t}$$

$\lambda>0$ → $t\to\infty$ 時 $\tilde x\to 0$。

【課堂討論】[▶ 61:26](https://youtu.be/RtJSHiqOdgQ?t=3686) 講者問這代表什麼？學生：追蹤誤差趨近 0。講者：對，$\tilde x$ 就是追蹤誤差。

### 6.3 質量未知：加上適應律

[▶ 61:57](https://youtu.be/RtJSHiqOdgQ?t=3717) 更實際的情況：$m$ **未知**，只有估計 $\hat m$。

**記號** [▶ 63:04](https://youtu.be/RtJSHiqOdgQ?t=3784)：

$$s=\dot{\tilde x}+\lambda\tilde x,\qquad \nu=\ddot x_m-2\lambda\dot{\tilde x}-\lambda^2\tilde x,\qquad \tilde m=\hat m-m$$

> ⚠️ 逐字稿缺字 [▶ 63:04](https://youtu.be/RtJSHiqOdgQ?t=3784)：字幕把 $\nu$ 的第一項唸成「x double dot」，依上一節控制律應為 $\ddot x_m$。

**控制律**：$u=\hat m\,\nu$（把 $m$ 換成估計 $\hat m$）。

**閉迴路** [▶ 64:05](https://youtu.be/RtJSHiqOdgQ?t=3845)：

$$m\ddot x=\hat m\nu=\tilde m\nu+m\nu\ \Rightarrow\ m\left(\ddot x-\nu\right)=\tilde m\nu$$

而 $\ddot x-\nu=\ddot{\tilde x}+2\lambda\dot{\tilde x}+\lambda^2\tilde x=\dot s+\lambda s$，所以

$$m\left(\dot s+\lambda s\right)=\tilde m\,\nu$$

**適應律** [▶ 66:59](https://youtu.be/RtJSHiqOdgQ?t=4019)：

$$\dot{\hat m}=-\gamma\,\nu\,s,\qquad\gamma>0\ \text{（適應增益）}$$

### 6.4 Lyapunov 分析

[▶ 67:38](https://youtu.be/RtJSHiqOdgQ?t=4058) **候選 Lyapunov 函數**：

$$V=\frac12\left(ms^2+\frac1\gamma\tilde m^2\right)$$

條件 1、3 容易，留給大家 [▶ 68:44](https://youtu.be/RtJSHiqOdgQ?t=4124)。條件 2：

1. $m$ 是常數 → $\dot{\tilde m}=\dot{\hat m}$ [▶ 69:16](https://youtu.be/RtJSHiqOdgQ?t=4156)。
2. 微分：
$$\dot V=ms\dot s+\frac1\gamma\tilde m\dot{\hat m}=ms\dot s-\frac1\gamma\tilde m\gamma\nu s=s\left(m\dot s-\tilde m\nu\right)$$
3. 由閉迴路，$m\dot s=\tilde m\nu-m\lambda s$，所以 $m\dot s-\tilde m\nu=-m\lambda s$：

$$\boxed{\dot V=-\lambda m\,s^2}$$

**結論** [▶ 72:04](https://youtu.be/RtJSHiqOdgQ?t=4324)：$s\to 0$。

**$s\to 0$ 代表追蹤誤差 $\to 0$** [▶ 72:34](https://youtu.be/RtJSHiqOdgQ?t=4354)：

- $s=\dot{\tilde x}+\lambda\tilde x\to 0$ → $\dot{\tilde x}\to-\lambda\tilde x$。
- 在 $(\tilde x,\dot{\tilde x})$ 平面上，系統收斂到直線 $\dot{\tilde x}=-\lambda\tilde x$。
- 在這條線上：$\tilde x<0$ 時 $\dot{\tilde x}>0$（往上長）；$\tilde x>0$ 時 $\dot{\tilde x}<0$（往下降）→ 沿著線走到 0。
- 所以 $\tilde x=x-x_m\to 0$：**追蹤誤差收斂到 0**。

> 以下**不是逐字稿內容**，是補充說明：
> - $\dot V=-\lambda ms^2$ 只跟 $s$ 有關，在 $s=0$、$\tilde m\ne 0$ 時也是 0，所以 $\dot V$ 只是**半負定**。嚴格結論是 $V$ 有界（所以 $s$、$\tilde m$ 有界），再用 **Barbalat 引理**得到 $s\to 0$。
> - 這個分析**不保證** $\hat m\to m$（參數不一定收斂到真值）；要參數收斂，通常還需要類似第 3.3 節的**持續激勵**條件。追蹤誤差收斂不需要參數準確——呼應 3.4「模型準不等於控制好」。

【Q&A】[▶ 74:46](https://youtu.be/RtJSHiqOdgQ?t=4486) 學生問 Lyapunov 定理怎麼用在這裡。答：候選函數是 $s$（和 $\tilde m$）的函數；明確驗證了條件 2，其他兩條一眼可見。滿足三條 → 系統全域漸近收斂到 $s=0$；再由上面的分析，$s\to 0$ ⟹ 追蹤誤差 $\to 0$。是 Lyapunov 定理的「一對一」應用。

【Q&A】[▶ 76:21](https://youtu.be/RtJSHiqOdgQ?t=4581) 學生問：已知和未知質量兩種情況都只證明收斂，沒有算出 $\gamma$ 或 $\lambda$？答：對。適應控制的經典做法：設計一個耦合系統（系統、控制器、可調參數的適應機制），然後證明它穩定。適應機制依賴我們引入的增益，實務上要**調**。

【口頭】[▶ 77:23](https://youtu.be/RtJSHiqOdgQ?t=4643) 講者承認這個分析感覺很繁複：引入很多函數、控制律、參考，都不清楚從哪來。實際上這非常依案例而定，對本課不太有意義。真的要對某個系統做適應控制，你要自己推出參考、控制律、適應律、候選 Lyapunov 函數。本課只示範「有了這些成分之後」的穩定性分析。

【Q&A】[▶ 78:59](https://youtu.be/RtJSHiqOdgQ?t=4739) 學生問：分析完全取決於那個 Lyapunov 函數，它怎麼來的？答：「這就是我們完全快轉的地方。」如果你對一個有趣的系統推出了 Lyapunov 函數並證明穩定，「你就寫一篇論文，很開心。」非常依案例而定。下一頁投影片有參考書（往前推導的方向）。

> 參考書名字幕沒唸，待補。

**下次**：收尾 MRAC（以及 MIAC），週三見。

---

## 7. 演算法整理

### 系統辨識（線性、最小平方）

**在解什麼**：動態未知但可假設為 $x_{t+1}=Ax_t+Bu_t+\varepsilon_t$；手上有離線軌跡資料（0 回合）。

```
1. 從軌跡切出 N 筆 ((x_t, u_t), x_{t+1})
2. Z ← 每列 (x_tᵀ, u_tᵀ)；Y ← 每列 x_{t+1}ᵀ
3. [A B]ᵀ = (ZᵀZ)⁻¹ ZᵀY（資料串流時用遞迴最小平方）
4. 把估出的 (Â, B̂) 當成真模型，套用前半學期的控制方法（LQR、MPC……）
```

**什麼時候會失敗**：沒有持續激勵（例如系統一直停在 0）→ $Z^\top Z$ 不可逆、共變異數不收斂；真實系統不是線性的 → 模型家族不夠表達；估得準不代表控制好（例如估錯符號）；收集資料時可能不安全。

### MRAC（直接適應控制，雙積分器例子）

**在解什麼**：$m\ddot x=u$，$m$ 未知；要追蹤參考模型 $x_m(t)$（1 回合，線上）。

```
設計：參考模型 ẍ_m + k_d ẋ_m + k_p x_m = k r(t)；增益 λ > 0、γ > 0
每個時刻：
1. x̃ = x − x_m；s = dx̃/dt + λ x̃；ν = ẍ_m − 2λ dx̃/dt − λ² x̃
2. 控制 u = m̂ ν
3. 更新估計 dm̂/dt = −γ ν s
```

**什麼時候會失敗**：參考模型、控制律、Lyapunov 函數都要針對系統自己推（非常依案例）；$\gamma$、$\lambda$ 要調；只保證追蹤誤差收斂，不保證 $\hat m$ 收斂到真值。

---

## 8. 一頁速查表

### 學習型控制地圖

| 維度 | 選項 |
|---|---|
| 學什麼 | 直接（改控制器） / 間接（先學模型） |
| 怎麼學 | 0 回合（離線資料，系統辨識） / 1 回合（線上適應） / 多回合（可重置環境，RL） |
| 面對不確定性 | 回饋 / 強健（最壞情況） / 資料驅動 |

### 最小平方

| 項目 | 式子 |
|---|---|
| 模型 | $y=\theta^\top z+\varepsilon$ |
| 解 | $\hat\theta=(Z^\top Z)^{-1}Z^\top y$（梯度 $-2Z^\top y+2Z^\top Z\theta=0$） |
| 系統辨識 | $y=x_{t+1}$，$z=(x_t,u_t)$，$\theta=(A,B)$ |
| 無偏 | $\hat\theta=\theta+(Z^\top Z)^{-1}Z^\top\varepsilon$ → $\mathbb E[\hat\theta]=\theta$ |
| 共變異數 | $\sigma^2(Z^\top Z)^{-1}=\sigma^2\left(\sum z_tz_t^\top\right)^{-1}$ → 持續激勵時 $\to 0$ |
| 性質 | BLUE（零均值、不相關、同變異數）；高斯時 = MLE |

### Lyapunov（全域）

$V>0$（除平衡點）、$\dot V<0$（除平衡點）、徑向無界 ⟹ 全域漸近穩定。
質量－彈簧－阻尼：$E=\frac12kx^2+\frac12m\dot x^2$，$\dot E=-d\dot x^2$。

### MRAC

| 項目 | 式子 |
|---|---|
| 系統 | $m\ddot x=u$ |
| 誤差 | $\tilde x=x-x_m$，$s=\dot{\tilde x}+\lambda\tilde x$ |
| 控制 | $u=\hat m\nu$，$\nu=\ddot x_m-2\lambda\dot{\tilde x}-\lambda^2\tilde x$ |
| 閉迴路 | $m(\dot s+\lambda s)=\tilde m\nu$ |
| 適應律 | $\dot{\hat m}=-\gamma\nu s$ |
| Lyapunov | $V=\frac12(ms^2+\tilde m^2/\gamma)$，$\dot V=-\lambda ms^2$ |
| 結論 | $s\to 0$ ⟹ $\tilde x\to 0$（沿 $\dot{\tilde x}=-\lambda\tilde x$） |
| 已知 $m$ 時 | $\tilde x=(c_0+c_1t)e^{-\lambda t}\to 0$ |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| MRAC 收尾、MIAC | 第 14 集開頭（講者預告） |
| 模仿學習 | 第 14–15 集 |
| 多回合、RL | 第 14、16–18 集 |
| 間接法（先學模型）、系統辨識 | 第 19 集基於模型的 RL |
| 持續激勵 ↔ 探索 | RL 的探索問題（待確認） |
| 「模型準 ≠ 控制好」 | 第 19 集（目標不一致問題，待確認） |

---

## 附：本集一句話總結

> **第二部分不再假設知道動態。學習型控制可以直接改控制器或先學模型，資料可以來自離線資料集（系統辨識）、線上單次操作（適應控制）或可重置的多回合互動（RL）。系統辨識用最小平方 $\hat\theta=(Z^\top Z)^{-1}Z^\top y$ 估 $(A,B)$，在持續激勵下無偏且共變異數趨近 0，但模型準不等於控制好；MRAC 則用參考模型、含估計參數的控制律和適應律 $\dot{\hat m}=-\gamma\nu s$，靠 Lyapunov 函數 $\frac12(ms^2+\tilde m^2/\gamma)$ 證明追蹤誤差收斂。**

---

## ⚠️ 待確認清單

1. 上課日期待補（第 7 週週一）。
2. 講者身分：本集沒有自我介紹，推測是 Daniele Gammelli。
3. [▶ 55:26](https://youtu.be/RtJSHiqOdgQ?t=3326) 參考模型右邊的增益是 $k_r$ 還是 $k_p$。
4. [▶ 78:59](https://youtu.be/RtJSHiqOdgQ?t=4739) 講者推薦的適應控制參考書名待補。

---

*筆記依據「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 13 錄影逐字稿（人工字幕，1:20:05）整理；本集課本無對應章節。*
