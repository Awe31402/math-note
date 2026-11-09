---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 8
lecture: Lecture 8
date: 待補（第 4 週週三）
video: https://youtu.be/1YdgSwEtf_s
notes: 《Principles of Robot Autonomy》§3.2.1 延伸、§3.2.2、§3.3.2、§3.3.3（書頁 101–110，PDF 頁 103–112）
---

# 第 8 集 · Lecture 8：LQR 類演算法（LQR-Style Algorithms） [▶ 影片](https://youtu.be/1YdgSwEtf_s)

← 上一集：[07-dynamic-programming](07-dynamic-programming.md) ｜ [總目錄](README.md) ｜ 下一集：[09-stochastic-dynamic-programming](09-stochastic-dynamic-programming.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 8 集
> **講者**：Marco Pavone（本集沒有自我介紹；上一集說「接下來三堂由我上」）
> **來源**：YouTube 錄影逐字稿（1:14:05，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§3.2–3.3
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. LQR 為什麼重要（vs PID）](#1-lqr-為什麼重要vs-pid)
- [2. 推廣 LQR：交叉項、一次項、仿射動態](#2-推廣-lqr交叉項一次項仿射動態)
- [3. 用 LQR 追蹤軌跡：線性系統](#3-用-lqr-追蹤軌跡線性系統)
  - [3.1 偏差變數](#31-偏差變數)
  - [3.2 前饋＋回饋：兩步驟設計](#32-前饋回饋兩步驟設計)
- [4. 用 LQR 追蹤軌跡：非線性系統](#4-用-lqr-追蹤軌跡非線性系統)
- [5. 疊代 LQR（iLQR）：用 LQR 做軌跡最佳化](#5-疊代-lqrilqr用-lqr-做軌跡最佳化)
  - [5.1 想法：變形而不是拉回](#51-想法變形而不是拉回)
  - [5.2 後向傳遞與前向傳遞](#52-後向傳遞與前向傳遞)
  - [5.3 iLQR vs SCP](#53-ilqr-vs-scp)
  - [5.4 實作注意事項](#54-實作注意事項)
- [6. 微分動態規劃（DDP）](#6-微分動態規劃ddp)
- [7. 演算法整理](#7-演算法整理)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:06](https://youtu.be/1YdgSwEtf_s?t=6) 上次：閉迴路、動態規劃、LQR。今天不講新概念，整堂講**怎麼在各種情境用 LQR**。

【口頭】[▶ 01:08](https://youtu.be/1YdgSwEtf_s?t=68) 作業 2：一題比較 DP 和暴力法的計算量；一題要你**從零實作 LQR**——「我知道你可以叫 AI 代理寫，但這輩子至少自己寫一次。」

接下來：下週一隨機 DP（加隨機擾動）；下週三連續時間閉迴路（HJB 方程）；之後 MPC。

| 主題 | 課本 |
|---|---|
| LQR 推廣（交叉項、仿射） | §3.2.1 後半 |
| 線性軌跡追蹤 | §3.2.2 |
| 非線性軌跡追蹤（線性化） | §3.3.2 |
| iLQR、DDP | §3.3.3 |

【口頭】[▶ 08:01](https://youtu.be/1YdgSwEtf_s?t=481) 有些式子很繁瑣（代數不難），課堂不全部列出，都在講義裡。

---

## 1. LQR 為什麼重要（vs PID）

[▶ 03:17](https://youtu.be/1YdgSwEtf_s?t=197) 老師主張：**PID 之後，LQR 是用得最廣的控制演算法**。

上次的 LQR 是要把狀態帶到**原點**（所以叫 regulator）。但機器人通常要的是**跟著某條軌跡**。LQR 能不能做？能——今天看線性和非線性的軌跡追蹤。

【Q&A】[▶ 04:20](https://youtu.be/1YdgSwEtf_s?t=260) 學生問：為什麼選 LQR 不選 PID？答：

- PID 沒有**目標函數**的概念。只能間接調整系統反應（ENGR 105/205 花很多時間在相位裕度、增益裕度、極點位置和上升時間的關係）。
- LQR 讓你**明確**指定目標，而且很有彈性：能做穩定化、軌跡追蹤，甚至用來**算軌跡**。

【Q&A】[▶ 05:23](https://youtu.be/1YdgSwEtf_s?t=323) 學生追問。答：兩者**互補**，不是對立。典型的決策架構（分層）：

| 層級 | 工具 | 考慮多少物理細節 |
|---|---|---|
| 最上層：設定目標 | 決策方法、資料驅動、LLM、VLM | 很少 |
| 中間：軌跡 | LQR 衍生、SCP、其他直接法 | 中等 |
| 最底層：致動器訊號（油門、方向盤、閥門） | PID | 最多 |

【口頭】[▶ 06:59](https://youtu.be/1YdgSwEtf_s?t=419) 例子：你決定「走到那扇門」時，不會去想手臂每個關節怎麼動；規劃路線時會考慮自己是個動態系統、身邊要留空間，但還是不想關節；越往下才越細。

---

## 2. 推廣 LQR：交叉項、一次項、仿射動態

[▶ 08:31](https://youtu.be/1YdgSwEtf_s?t=511) 回顧：LQR 沒有狀態、控制約束；動態線性 $x_{k+1}=A_kx_k+B_ku_k$。**$A_k$、$B_k$ 可以隨時間變**（下標 $k$）——之後會知道這很有用。

**推廣一：交叉項** [▶ 09:32](https://youtu.be/1YdgSwEtf_s?t=572)

$$g_k=\frac12\begin{pmatrix}x_k\\u_k\end{pmatrix}^\top\begin{pmatrix}Q_k&H_k^\top\\H_k&R_k\end{pmatrix}\begin{pmatrix}x_k\\u_k\end{pmatrix}=\frac12\left(x_k^\top Q_kx_k+u_k^\top R_ku_k\right)+u_k^\top H_kx_k$$

為什麼要交叉項 $u^\top Hx$？

- 有時懲罰控制力氣的程度跟狀態有關。
- 更機械的理由：用 LQR 做追蹤時要**線性化**，交叉項會自己跑出來。

推導完全一樣（邊界二次 → 梯度 = 0 → 解 $u$ → 代回仍二次）：最佳控制還是**線性回饋**，成本還是**二次**；只是 $L$、$P$ 的更新式稍微變了。

**推廣二：一次項、常數項、仿射動態** [▶ 12:14](https://youtu.be/1YdgSwEtf_s?t=734)

$$
\begin{aligned}
g_k&=\frac12\begin{pmatrix}x_k\\u_k\end{pmatrix}^\top\begin{pmatrix}Q_k&H_k^\top\\H_k&R_k\end{pmatrix}\begin{pmatrix}x_k\\u_k\end{pmatrix}+q_k^\top x_k+r_k^\top u_k+c_k \\
x_{k+1}&=A_kx_k+B_ku_k+d_k
\end{aligned}
$$

- 動態多了常數項 $d_k$ → 叫**仿射**（affine）。可以想成已知會在時刻 $k$ 發生的擾動（例如陣風）。
- 一樣的推導（從二次＋一次＋常數的終端成本出發）得到：

$$u_k^*=L_kx_k+l_k,\qquad J_k^*(x)=\frac12x^\top P_kx+p_k^\top x+\text{常數}$$

- $L_kx_k$：**線性回饋**（上一集叫 $F_k$，老師說抱歉記號混用）。
- $l_k$：**前饋**（feedforward）常數項。後面會看到它的直覺意義。
- $P_k$、$p_k$、常數、$L_k$、$l_k$ 都由類似 Riccati 的遞迴算出（細節在講義）。

> 以下 $g_k$ 的矩陣寫法是依老師說明（「quadratic + cross terms + linear terms + constant」）寫出的；投影片原式字幕沒唸，矩陣的確切排列待確認。

【Q&A】[▶ 13:46](https://youtu.be/1YdgSwEtf_s?t=826) 學生問：今天的式子跟上次不一樣？上次終端是 $H$？答：差別只是加了交叉項；終端矩陣叫 $Q_N$ 或 $H$ 只是記號。這些 $Q$、$R$、$H$ 都是**設計者自己選**的矩陣，不是同一個東西。

**LQR 調參** [▶ 15:19](https://youtu.be/1YdgSwEtf_s?t=919)

【口頭】LQR 一旦設定好，之後全是程序化的；你的工作是**設定**——選 $R$、$Q$、$Q_N$……這叫 **LQR 調參**（LQR tuning），一點都不簡單。老師說他調某個系統的 LQR 追蹤器花了**兩三個月**，才調出想要的橫向和縱向反應：要安全，也要讓使用者覺得舒服。有點藝術成分，也會用模擬輔助。

> ⚠️ 逐字稿缺字 [▶ 15:51](https://youtu.be/1YdgSwEtf_s?t=951)：字幕寫「tracking algorithm for the [INAUDIBLE]」，老師調參的系統名稱聽不清，待補。

【課本補充】課本 §3.2.1 把仿射版本寫成 $u_t=-K_tx_t-k_t$（式 3.30），並說這個「仿射－二次」形式在把 LQR 推到非線性系統時扮演核心角色，因為線性化和二次近似會自然產生這些項。

---

## 3. 用 LQR 追蹤軌跡：線性系統

### 3.1 偏差變數

[▶ 18:56](https://youtu.be/1YdgSwEtf_s?t=1136) 給定**參考軌跡** $\bar x_0,\bar x_1,\dots,\bar x_N$ 和 $\bar u_0,\dots,\bar u_{N-1}$（兩者透過動態連在一起）。

**從哪來？** [▶ 20:03](https://youtu.be/1YdgSwEtf_s?t=1203) 例如上週的直接法（像 SCP）算出的開迴路軌跡。

**問題**：現實有模型誤差和擾動——可能不是從 $\bar x_0$ 出發，或被擾動推開。要找控制讓實際軌跡**盡量貼近**參考軌跡（同時控制也貼近 $\bar u$）。這叫**軌跡追蹤**（trajectory tracking）。

**先看線性情況** [▶ 22:40](https://youtu.be/1YdgSwEtf_s?t=1360)（不太實用，但建立直覺）：

$$x_{k+1}=A_kx_k+B_ku_k$$

參考軌跡必須是**可行**的 [▶ 23:14](https://youtu.be/1YdgSwEtf_s?t=1394)：$\bar x_{k+1}=A_k\bar x_k+B_k\bar u_k$。

**兩式相減** [▶ 23:45](https://youtu.be/1YdgSwEtf_s?t=1425)，定義**偏差變數**（deviation variables）$\delta x_k=x_k-\bar x_k$、$\delta u_k=u_k-\bar u_k$：

$$\delta x_{k+1}=A_k\,\delta x_k+B_k\,\delta u_k$$

**關鍵觀察** [▶ 24:17](https://youtu.be/1YdgSwEtf_s?t=1457)：追蹤問題變成**對偏差變數的 LQR 調節問題**——目標是把 $\delta x$ 帶到 0。$\delta x\to 0$ 就代表 $x_k\to\bar x_k$。

**輔助 LQR 問題** [▶ 25:52](https://youtu.be/1YdgSwEtf_s?t=1552)：

$$\min_{\delta u}\ \frac12\delta x_N^\top Q_N\delta x_N+\frac12\sum_{k=0}^{N-1}\left(\delta x_k^\top Q\,\delta x_k+\delta u_k^\top R\,\delta u_k\right)$$

$Q$、$R$、$Q_N$ 是設計參數。Riccati 遞迴給出 $\delta u_k^*=L_k\,\delta x_k$。

**注意**（常見混淆）[▶ 25:22](https://youtu.be/1YdgSwEtf_s?t=1522)：真正送進系統的**不是** $\delta u$，要轉回來：

$$u_k=\bar u_k+\delta u_k$$

### 3.2 前饋＋回饋：兩步驟設計

[▶ 27:58](https://youtu.be/1YdgSwEtf_s?t=1678) 追蹤控制器的結構：

$$u_k=\underbrace{\bar u_k}_{\text{前饋（開迴路）}}+\underbrace{L_k\left(x_k-\bar x_k\right)}_{\text{回饋（閉迴路）}}$$

- **合理性檢查**：如果剛好在參考軌跡上（$x_k=\bar x_k$），回饋項是 0，就用標稱控制。
- 偏離時，回饋項依偏離程度（透過 $L_k$）把你推回參考軌跡。

**兩步驟設計**（two-step design）[▶ 29:01](https://youtu.be/1YdgSwEtf_s?t=1741)，控制和機器人很常用：

1. 用**開迴路**技巧算標稱軌跡（上週）。
2. 用**閉迴路**技巧設計控制器，在局部把你推回軌跡（這週）。

兼顧開迴路的**計算效率**和閉迴路的**強健性**。

**為什麼不直接全域解閉迴路？** [▶ 30:04](https://youtu.be/1YdgSwEtf_s?t=1804)

- 非常耗時。
- 而且可能**沒用**：機器人的環境是動態的。例如有同學站起來，約束集合就變了（多一個碰撞約束），要定期重新規劃。既然在離得很遠之前就會重算，為所有狀態解全域策略是浪費。

【Q&A】[▶ 31:06](https://youtu.be/1YdgSwEtf_s?t=1866) 學生問 $L$ 是正的嗎？會變嗎？答：下標 $k$ 表示它**隨階段變**（時變）。給定階段，它是常數增益矩陣，**不是**狀態的函數。

【Q&A】[▶ 31:36](https://youtu.be/1YdgSwEtf_s?t=1896) 學生問：$u_k$ 是已知的嗎？答：不是。$\delta u_k=u_k-\bar u_k$ 只是變數代換：$\bar u$ 已知、$u_k$ 未知。先解 $\delta u$，再得到 $u_k$。

【課本補充】課本 §3.2.2 也把這叫「兩步驟設計範式的清楚實例」：前饋 $\bar u(t)$ 來自標稱軌跡，回饋 $-K(t)(x(t)-\bar x(t))$ 補償偏差。

---

## 4. 用 LQR 追蹤軌跡：非線性系統

[▶ 32:40](https://youtu.be/1YdgSwEtf_s?t=1960) 更有意思的情況：

$$x_{k+1}=f(x_k,u_k),\qquad \bar x_{k+1}=f(\bar x_k,\bar u_k)\ \text{（參考軌跡可行）}$$

**相減** [▶ 34:20](https://youtu.be/1YdgSwEtf_s?t=2060)：$x_{k+1}-\bar x_{k+1}=f(x_k,u_k)-f(\bar x_k,\bar u_k)$。

**技巧：泰勒展開** [▶ 34:54](https://youtu.be/1YdgSwEtf_s?t=2094)，在 $(\bar x_k,\bar u_k)$ 附近：

$$f(x_k,u_k)\approx f(\bar x_k,\bar u_k)+\underbrace{\frac{\partial f}{\partial x}\Big|_{(\bar x_k,\bar u_k)}}_{A_k}(x_k-\bar x_k)+\underbrace{\frac{\partial f}{\partial u}\Big|_{(\bar x_k,\bar u_k)}}_{B_k}(u_k-\bar u_k)$$

代進去 [▶ 36:15](https://youtu.be/1YdgSwEtf_s?t=2175)，$f(\bar x_k,\bar u_k)$ 抵銷：

$$\delta x_{k+1}\approx A_k\,\delta x_k+B_k\,\delta u_k$$

又回到線性情況！照 3.1 做：輔助 LQR → $\delta u_k^*$ → $u_k=\bar u_k+\delta u_k$。

**$A_k$、$B_k$ 是時變的** [▶ 38:54](https://youtu.be/1YdgSwEtf_s?t=2334)：Jacobian 在**不同時刻的標稱點**計算，所以隨 $k$ 變。還好 LQR 本來就能處理線性時變動態。

【Q&A】[▶ 36:46](https://youtu.be/1YdgSwEtf_s?t=2206) 學生問：線性化只在附近才準？答：對。追蹤問題本來就是要**待在**標稱軌跡附近，通常起點也很接近，所以線性化通常夠好。但確實有偏太多、線性化失效、演算法變得不穩定的危險。實務上效果很好。

【Q&A】[▶ 39:24](https://youtu.be/1YdgSwEtf_s?t=2364) 學生問：能不能預先算好 Jacobian？答：環境靜態就可以。但機器人在動態環境中常常要重算開迴路軌跡，那就不能全部預算。

【Q&A】[▶ 39:55](https://youtu.be/1YdgSwEtf_s?t=2395) 學生問：只有狀態軌跡、沒有控制軌跡怎麼辦？答：這個方法需要狀態**和**控制的參考。有些演算法直接給成對的 $(\bar x,\bar u)$；否則要從狀態軌跡透過動態**反推**控制，例如用**微分平坦**（differential flatness）技巧。

【口頭】[▶ 40:58](https://youtu.be/1YdgSwEtf_s?t=2458) 再次注意結構：前饋 $\bar u$ + LQR 線性回饋 = 繞著標稱軌跡的**閉迴路外殼**。有人推你一下，控制器把你推回去。

---

## 5. 疊代 LQR（iLQR）：用 LQR 做軌跡最佳化

### 5.1 想法：變形而不是拉回

[▶ 42:06](https://youtu.be/1YdgSwEtf_s?t=2526) 回到一般非線性最佳控制問題：

$$\min\ h(x_N)+\sum_{k=0}^{N-1}c(x_k,u_k)\quad\text{s.t.}\quad x_{k+1}=f(x_k,u_k)$$

**能不能用 LQR（閉迴路工具）算最佳的開迴路軌跡？** 聽起來很怪，但可以。

[▶ 43:09](https://youtu.be/1YdgSwEtf_s?t=2589) 給一條**可行**的標稱軌跡（任何可行的都行，不要求最佳），成本 $c_1$。

- **追蹤**：找控制把你**拉回**標稱軌跡（$\delta x\to 0$）。
- **iLQR**：找控制把標稱軌跡**變形**成更好的軌跡——每個路徑點移動 $\delta x_1,\delta x_2,\dots$，讓新軌跡成本 $c_2<c_1$。

【Q&A】[▶ 44:42](https://youtu.be/1YdgSwEtf_s?t=2682) 學生問標稱軌跡哪來？已經是最佳的嗎？答：不是最佳，只是可行、有成本 $c_1$。我們想找另一條可行但成本更低的。這是一個**新的**算標稱軌跡的方法；算好後可以再用 LQR 追蹤它。「我們換檔了：現在不是追蹤，是**軌跡最佳化**。」

**做法** [▶ 46:48](https://youtu.be/1YdgSwEtf_s?t=2808)：

1. **動態**：一樣線性化 → $\delta x_{k+1}=A_k\delta x_k+B_k\delta u_k$。
2. **成本**：不是設計「把 $\delta x$ 帶到 0」的成本，而是把**真正的成本**在標稱點附近做**二階**泰勒展開 [▶ 49:33](https://youtu.be/1YdgSwEtf_s?t=2973)：

$$
\begin{aligned}
c(\bar x_k+\delta x_k,\bar u_k+\delta u_k)\approx\ & c(\bar x_k,\bar u_k)+c_x^\top\delta x_k+c_u^\top\delta u_k \\
&+\frac12\delta x_k^\top c_{xx}\,\delta x_k+\frac12\delta u_k^\top c_{uu}\,\delta u_k+\delta u_k^\top c_{ux}\,\delta x_k
\end{aligned}
$$

下標 $x$ = 對 $x$ 的導數，$xx$ = 二階，$xu$ = 交叉導數，都在 $(\bar x_k,\bar u_k)$ 計算。

這正是第 2 節的「推廣 LQR」形式（有一次項和交叉項），可以用 Riccati 遞迴快速解出 $\delta u$。

【Q&A】[▶ 51:35](https://youtu.be/1YdgSwEtf_s?t=3095) 學生問：LQR 不是會把偏差帶到 0 嗎？這裡為什麼刻意讓它不是 0？答：這不是標準 LQR，是**有一次項和常數項**的推廣版。如果只有二次項，最小值當然在 $\delta x=0$；有了一次項，$\delta x=0$ 就**不一定**是最小值。

**另一個差別** [▶ 52:35](https://youtu.be/1YdgSwEtf_s?t=3155)：追蹤時 $Q$、$R$ 是設計者選的；這裡它們是從**近似算出來**的。所以要擔心條件好壞——例如希望 $Q$ 正定，可能要**正則化**（regularize）。

### 5.2 後向傳遞與前向傳遞

[▶ 54:38](https://youtu.be/1YdgSwEtf_s?t=3278) 解出 $\delta u_k$ 後，得到新控制 $\bar u_k+\delta u_k$。從初始條件把動態往前推，得到新軌跡——成本通常更低——當作下一輪的標稱軌跡。所以叫**疊代 LQR**（iterative LQR，iLQR）。

**兩步** [▶ 56:44](https://youtu.be/1YdgSwEtf_s?t=3404)：

| 步驟 | 做什麼 |
|---|---|
| **後向傳遞**（backward pass） | 在標稱軌跡附近：動態線性化、成本二次化 → Riccati 遞迴 → 最佳 $\delta u$ 的控制律 |
| **前向傳遞**（forward pass） | 用 $u_k=\bar u_k+\delta u_k$，從 $x_0$ 往前推出新的狀態序列 |

**常見錯誤** [▶ 57:15](https://youtu.be/1YdgSwEtf_s?t=3435)：前向傳遞要用**真正的非線性動態** $x_{k+1}=f(x_k,u_k)$，**不是**線性近似。既然知道動態、往前推很容易，沒理由用近似。

**停止條件** [▶ 57:46](https://youtu.be/1YdgSwEtf_s?t=3466)：幾輪後成本下降不明顯，或軌跡變化不明顯，或達到最大迭代次數。

【Q&A】[▶ 56:10](https://youtu.be/1YdgSwEtf_s?t=3370) 學生問：這像梯度下降，每一步會多接近？答：不完全一樣，因為對動態做了近似（見 5.4）。

【課本補充】課本 §3.3.3 的前向傳遞寫成 $u_t=\bar u_t-k_t-K_t(x_t-\bar x_t)$（式 3.48）：把**回饋**也放進前向傳遞（用實際推出的 $x_t$），而不只是加上開迴路的 $\delta u$。

### 5.3 iLQR vs SCP

[▶ 58:17](https://youtu.be/1YdgSwEtf_s?t=3497) 兩者很像：都線性化動態、近似成本、反覆求解。差別：

| | iLQR | SCP |
|---|---|---|
| 每輪怎麼解 | Riccati 方程（幾乎解析） | 凸最佳化解法器 |
| 實作 | **簡單**：Riccati + 導數 | 較複雜：要解法器、信任域…… |
| 成本近似 | 二次 | 任何凸近似 |
| 約束 | **不能處理**（加約束後 Riccati 結果全部不成立） | 能處理狀態和控制約束（只要凸） |

【口頭】[▶ 59:50](https://youtu.be/1YdgSwEtf_s?t=3590) 歷史上 iLQR 很紅，因為超好實作。現在嵌入式凸最佳化解法器很強，就算要反覆解也不錯，所以 SCP 也變成熱門的直接最佳化演算法。

【Q&A】[▶ 60:22](https://youtu.be/1YdgSwEtf_s?t=3622) 學生問：所以只有離控制、狀態界很遠時才能用 iLQR？答：對，要小心處理約束。可以把約束變成**成本中的懲罰項**，但要小心；不能把它們當成真正的約束處理。

### 5.4 實作注意事項

[▶ 61:24](https://youtu.be/1YdgSwEtf_s?t=3684)

1. **待在線性化點附近**：否則近似失效，新軌跡成本甚至可能**更高**。
2. **前向傳遞時調小**：做一點**線搜尋**（line search）調整前饋項，讓新軌跡不要離上一輪太遠。
3. **停止條件**要設計。
4. **局部方法**：不保證最佳，**好的初始化很關鍵**。

   【口頭】[▶ 62:26](https://youtu.be/1YdgSwEtf_s?t=3746) 現在很強的初始化方式：用看過「無數個最佳控制問題」的**神經網路**預測，當暖啟動（warm start）。兼得資料驅動的通用性和形式化最佳控制的保證。
5. **成本矩陣可能不正定**：線性化／二次化後要正則化，例如加上常數乘單位矩陣，平移特徵值。

【口頭】[▶ 62:56](https://youtu.be/1YdgSwEtf_s?t=3776) 實作上的技巧大全：**Yuval Tassa 的博士論文 §2.2.3**。

【課本補充】課本 §3.3.3 的實務考量相同：局部最佳、二階項正則化（$H_{xx}+\mu I$、$H_{uu}+\mu I$，$\mu>0$）、停止條件、前向傳遞穩健性。

---

## 6. 微分動態規劃（DDP）

[▶ 63:28](https://youtu.be/1YdgSwEtf_s?t=3808) iLQR 想法的更強版本。

| | 先近似什麼 | 再做什麼 |
|---|---|---|
| iLQR | 近似**問題**（動態線性化、成本二次化） | **精確**跑 DP（Riccati） |
| DDP | 直接近似 **DP 方程**（Bellman 方程右邊） | 解近似後的方程 |

**推導** [▶ 64:29](https://youtu.be/1YdgSwEtf_s?t=3869)：Bellman 方程

$$J_k^*(x_k)=\min_{u_k}\left[c(x_k,u_k)+J_{k+1}^*\left(f(x_k,u_k)\right)\right]$$

寫成偏差變數 [▶ 65:34](https://youtu.be/1YdgSwEtf_s?t=3934)（$x_k=\bar x_k+\delta x_k$、$u_k=\bar u_k+\delta u_k$）：

$$J_k^*(\bar x_k+\delta x_k)=\min_{\delta u_k}\underbrace{\left[c(\bar x_k+\delta x_k,\bar u_k+\delta u_k)+J_{k+1}^*\left(f(\bar x_k+\delta x_k,\bar u_k+\delta u_k)\right)\right]}_{Q_k(\bar x_k+\delta x_k,\ \bar u_k+\delta u_k)}$$

（$\bar u$ 是常數，所以對 $\bar u+\delta u$ 最小化等於對 $\delta u$ 最小化。）

- 右邊叫 **Q 函數**（Q-function）[▶ 66:27](https://youtu.be/1YdgSwEtf_s?t=3987)。之後講資料驅動控制時會扮演關鍵角色。
- DP 是往回做的，$J_{k+1}^*$ 已經算好；$f$ 已知 → $Q_k$ 是**已知**函數，可以微分。

**把 Q 函數二階展開** [▶ 67:27](https://youtu.be/1YdgSwEtf_s?t=4047)：

$$Q_k\approx Q_k(\bar x_k,\bar u_k)+Q_{x,k}^\top\delta x+Q_{u,k}^\top\delta u+\frac12\delta x^\top Q_{xx,k}\delta x+\frac12\delta u^\top Q_{uu,k}\delta u+\delta u^\top Q_{ux,k}\delta x$$

變成 $\delta u$ 的**二次函數**（$\delta x$ 在遞迴中是固定的）。

**對 $\delta u$ 微分 = 0** [▶ 69:32](https://youtu.be/1YdgSwEtf_s?t=4172)：

$$Q_{u,k}+Q_{uu,k}\,\delta u+Q_{ux,k}\,\delta x=0\ \Rightarrow\ \delta u_k^*=-Q_{uu,k}^{-1}\left(Q_{u,k}+Q_{ux,k}\,\delta x_k\right)$$

代回去 [▶ 71:10](https://youtu.be/1YdgSwEtf_s?t=4270)，剩餘成本也是二次的 → 再退一步。

> 以下**不是逐字稿內容**：$\delta u^*$ 的閉式是由上面的一階條件直接解出的；老師說「then we solve for the optimal delta u」但沒唸出式子。它同樣是「前饋 $-Q_{uu}^{-1}Q_u$ + 線性回饋 $-Q_{uu}^{-1}Q_{ux}\delta x$」的形式。

**跟 iLQR 的差別** [▶ 71:40](https://youtu.be/1YdgSwEtf_s?t=4300)：把 $Q$ 函數的導數全部寫出來，會出現**動態的二階導數**。所以 DDP 是**二階**演算法；iLQR 只用動態的一階導數。DDP 更精緻，但直覺類似。

**總結** [▶ 72:41](https://youtu.be/1YdgSwEtf_s?t=4361)：

- LQR 用在**追蹤**（很重要，一定要熟）。
- 用 LQR 推出**直接法**：iLQR 軌跡最佳化。
- DDP：直接近似 Bellman 方程右邊。結果類似：控制 = 前饋 + 線性回饋，只是增益不同。
- 「一定要熟 iLQR 和用 LQR 做非線性追蹤。」

---

## 7. 演算法整理

### LQR 軌跡追蹤（非線性）

**在解什麼**：已有可行參考軌跡 $(\bar x,\bar u)$（例如 SCP 算的），要在擾動、模型誤差下貼著它走。

**步驟**：

```
離線：
1. 沿參考軌跡算 Jacobian：A_k = ∂f/∂x、B_k = ∂f/∂u（在 (x̄_k, ū_k)）
2. 選 Q、R、Q_N（LQR 調參）
3. 對 δx_{k+1} = A_k δx_k + B_k δu_k 跑 Riccati 遞迴 → L_k
線上（每一步）：
4. 量測 x_k
5. u_k = ū_k + L_k (x_k − x̄_k)
```

**什麼時候會失敗**：偏離太多 → 線性化失效、行為不穩定；只有狀態參考、沒有控制參考時要先反推 $\bar u$；環境變了要重算參考軌跡和增益；$Q$、$R$ 調不好 → 反應不理想（調參可能要幾個月）。

### iLQR

**在解什麼**：無約束非線性軌跡最佳化 $\min h(x_N)+\sum c(x_k,u_k)$。

**步驟**：

```
1. 初始化可行標稱軌跡 (x̄, ū)（好的初始化很關鍵，可用神經網路暖啟動）
2. 重複：
   後向傳遞：
     a. 沿 (x̄, ū) 線性化動態 → A_k, B_k
     b. 二階展開成本 → c_x, c_u, c_xx, c_uu, c_ux（必要時加 μI 正則化）
     c. 推廣 LQR 的 Riccati 遞迴 → δu_k = L_k δx_k + l_k
   前向傳遞：
     d. 從 x₀ 用「真正的」f 往前推：u_k = ū_k + δu_k（可做線搜尋縮小步伐）
     e. 新軌跡成為標稱軌跡
   f. 成本或軌跡變化很小 → 停
```

**什麼時候會失敗**：不能處理約束（只能用懲罰）；局部最佳，初始化差就卡住；步伐太大 → 近似失效、成本上升；二階項不正定 → Riccati 病態。

### DDP

**在解什麼**：同 iLQR。

**差別**：後向傳遞時把 Bellman 方程右邊的 Q 函數二階展開（包含動態的**二階**導數），$\delta u^*=-Q_{uu}^{-1}(Q_u+Q_{ux}\delta x)$。更精確、每步更貴。

---

## 8. 一頁速查表

### 推廣 LQR

| 項目 | 結果 |
|---|---|
| 交叉項 $u^\top Hx$ | 仍是 $u=Lx$，$J=\frac12x^\top Px$（$L,P$ 更新式變） |
| ＋一次項、常數、仿射動態 $+d_k$ | $u=L_kx+l_k$（回饋 + 前饋），$J=\frac12x^\top Px+p^\top x+$常數 |

### 追蹤

$$\delta x=x-\bar x,\quad \delta u=u-\bar u,\quad \delta x_{k+1}\approx A_k\delta x_k+B_k\delta u_k$$

$$u_k=\bar u_k+L_k(x_k-\bar x_k)\qquad\text{（前饋 + 回饋，兩步驟設計）}$$

- 線性系統：相減直接得到；非線性：泰勒展開，$A_k,B_k$ 是沿軌跡的 Jacobian（時變）。

### iLQR vs 追蹤

| | 追蹤 | iLQR |
|---|---|---|
| 目的 | 把 $\delta x$ 拉回 0 | 把軌跡變形成更低成本 |
| 成本 | 設計者選 $Q,R$ | 真正成本的二階展開（含一次項） |
| 輸出 | 回饋控制器 | 新的（局部最佳）軌跡 + 增益 |

### iLQR vs SCP vs DDP

| | iLQR | SCP | DDP |
|---|---|---|---|
| 子問題 | LQR（Riccati） | 凸問題 | Q 函數二次近似 |
| 約束 | ✗ | ✓（凸） | ✗ |
| 動態導數 | 一階 | 一階 | **二階** |
| 實作 | 最簡單 | 要解法器、信任域 | 較複雜 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| DP 加隨機擾動 | 第 9 集隨機 DP |
| 連續時間閉迴路 | 第 10 集 HJB、可達性 |
| 開迴路規劃 + 閉迴路追蹤、定期重新規劃 | 第 11–12 集 MPC |
| **Q 函數** | 第 16–17 集 RL（Q-learning、值函數方法） |
| 神經網路暖啟動、資料驅動 | 第 13–19 集學習型控制 |

---

## 附：本集一句話總結

> **LQR 是一把萬用鑰匙：寫成偏差變數 $\delta x=x-\bar x$ 後，軌跡追蹤（線性或線性化後的非線性）就變成 LQR 調節問題，控制 = 標稱前饋 $\bar u$ + 線性回饋 $L_k\delta x$；把同樣的機器拿去「變形」而不是「拉回」軌跡（成本做二階展開、前向傳遞用真正的動態），就得到軌跡最佳化演算法 iLQR；直接二次近似 Bellman 方程右邊的 Q 函數，則是 DDP。**

---

## ⚠️ 待確認清單

1. 上課日期待補（第 4 週週三）。
2. [▶ 12:14](https://youtu.be/1YdgSwEtf_s?t=734) 推廣 LQR 成本的矩陣排列是依口述寫出的，待對照投影片。
3. [▶ 15:51](https://youtu.be/1YdgSwEtf_s?t=951) 老師花兩三個月調 LQR 追蹤器的系統名稱聽不清，待補。

---

*筆記依據 Marco Pavone「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 8 錄影逐字稿（人工字幕，1:14:05）與《Principles of Robot Autonomy》§3.2–3.3 整理。*
