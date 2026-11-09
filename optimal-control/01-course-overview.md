---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 1
lecture: Lecture 1
date: 待補（週一）
video: https://youtu.be/Au2stLALZew
notes: 《Principles of Robot Autonomy》第 2 章開頭、§2.1（書頁 55–60，PDF 頁 57–62）
---

# 第 1 集 · Lecture 1：課程介紹（Course Overview） [▶ 影片](https://youtu.be/Au2stLALZew)

← 上一集：無 ｜ [總目錄](README.md) ｜ 下一集：[02-optimization-theory](02-optimization-theory.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 1 集
> **講者**：Marco Pavone（Stanford 航太系教授，也在 NVIDIA 帶自主系統研究）
> **來源**：YouTube 錄影逐字稿（1:13:23，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§2.1
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 課程行政](#1-課程行政)
- [2. 什麼是控制](#2-什麼是控制)
  - [2.1 回饋控制的方塊圖](#21-回饋控制的方塊圖)
  - [2.2 古典控制想要什麼](#22-古典控制想要什麼)
  - [2.3 古典控制少了什麼：最佳、規劃、學習](#23-古典控制少了什麼最佳規劃學習)
- [3. 課程地圖](#3-課程地圖)
- [4. 最佳控制問題的三個成分](#4-最佳控制問題的三個成分)
  - [4.1 數學模型：常微分方程](#41-數學模型常微分方程)
  - [4.2 例子：雙積分器](#42-例子雙積分器)
  - [4.3 約束](#43-約束)
  - [4.4 性能指標](#44-性能指標)
  - [4.5 最佳控制問題的完整敘述](#45-最佳控制問題的完整敘述)
- [5. 控制界和電腦科學界的用語對照](#5-控制界和電腦科學界的用語對照)
- [6. 開迴路 vs 閉迴路](#6-開迴路-vs-閉迴路)
- [7. 離散時間版本](#7-離散時間版本)
- [8. 擾動怎麼建模](#8-擾動怎麼建模)
- [9. 預告：先學古典最佳化](#9-預告先學古典最佳化)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 課程行政 | — |
| 控制是什麼、古典控制少了什麼 | 課本沒有 |
| 課程地圖（開迴路、閉迴路、MPC、學習） | 課本沒有 |
| 最佳控制問題的三個成分與完整敘述 | §2.1 |
| 開迴路 vs 閉迴路 | 第 2 章開頭（書頁 60） |
| 局部／全域最小值 | 課本沒有（課本 §2.2.1 直接從必要條件開始） |

---

## 1. 課程行政

[▶ 00:36](https://youtu.be/Au2stLALZew?t=36)

- **4 份作業**（理論＋Python 程式），每份 20%，共 80%。約每兩週一份，週五交。
- **期末考** 20%，6 月 8 日 3:30–6:30。
- 在 Ed 論壇有意義地回答同學問題，最多加 5%。
- 6 天免費遲交額度，每份作業最多用 2 天。
- 必要教材：投影片、上課、作業。網站另有 course notes 和參考書（非必要）。
- 前四週週五有 recitation（習題／工具課），介紹本課會用的工具。

> ⚠️ 逐字稿缺字 [▶ 02:41](https://youtu.be/Au2stLALZew?t=161)：字幕寫「such as, for example, **jags** or regression models」。「jags」依上下文可能是 **JAX**（Python 數值計算套件），待確認。

**先備知識** [▶ 03:13](https://youtu.be/Au2stLALZew?t=193)：多變數微積分、常微分方程（懂是什麼就好，不用會解很難的）、**線性代數要很熟**。最佳化、機器學習、控制有學過更好，但課程是自足的（self-contained）。

有 **Homework 0**（不計分）讓你自我檢測。老師說不要用 ChatGPT 做，它當成自我測驗才有意義。

**課程風格** [▶ 05:15](https://youtu.be/Au2stLALZew?t=315)：**廣度優先於深度**。目標是給你最佳控制和學習型控制主要方法的全貌和分類（taxonomy）。想深入某個方法要自己讀。課程一般被認為蠻難，因為主題很雜（微積分、統計……都會用到）。

【Q&A】[▶ 06:47](https://youtu.be/Au2stLALZew?t=407) 作業什麼時候發？答：週五交，大約每兩週一份，平均分布在整個學期。

---

## 2. 什麼是控制

### 2.1 回饋控制的方塊圖

[▶ 07:18](https://youtu.be/Au2stLALZew?t=438) 控制：你有一個**系統**（system，可以是實體的，例如無人機；也可以是金融系統），想**作用**在它上面，讓它產生想要的反應。

標準方塊圖的元素：

| 元素 | 意思 | 開車的例子 | 室溫的例子 |
|---|---|---|---|
| 系統（plant） | 被控制的東西 | 車 | 房子 |
| 感測器（sensor） | 量系統的狀態 | 相機、速度計 | 溫度計 |
| 參考（reference） | 高層目標 | 換車道、保持某速度 | 恆溫器設定 |
| 控制器（controller） | 由量測＋參考算出控制 | — | — |
| 控制（control action） | 送進系統的指令 | 方向盤角度、油門 | 瓦斯流量 |
| 輸出（output） | 系統的反應 | 加速度 | 室溫 |

關鍵是**一直重複**：算控制 → 看系統反應 → 量測 → 重算控制。這就是**閉迴路控制**（closed-loop control）。

【口頭】[▶ 09:24](https://youtu.be/Au2stLALZew?t=564) 人從出生就在做閉迴路控制：眼睛是感測器，「走到那扇門」是參考，關節是致動器。

**模型可以很務實** [▶ 10:25](https://youtu.be/Au2stLALZew?t=625)

【口頭】控制洗澡水溫：計算流體力學的人會建熱力學模型。控制的人比較務實——「旋鈕往右變熱、往左變冷」就是你的模型。模型可以很簡化，也可以**從資料學**出來。

### 2.2 古典控制想要什麼

[▶ 11:27](https://youtu.be/Au2stLALZew?t=687) 現實的麻煩：

- **擾動**（disturbance）：飛機遇到陣風，被推離標稱（nominal）軌跡。
- **量測雜訊**（measurement noise）：感測器不完美。

古典控制（頻域方法、PID 控制）想達成的目標 [▶ 12:00](https://youtu.be/Au2stLALZew?t=720)：

1. **穩定**（stability）：系統不會失控，輸出保持有界（bounded）。穩定有好幾種定義（內部、外部），這裡用直覺意思。
2. **追蹤**（tracking）：輸出盡量貼近參考訊號。
3. **抑制擾動**（disturbance rejection）：陣風不要把軌跡推太遠。
4. **強健**（robust）[▶ 13:01](https://youtu.be/Au2stLALZew?t=781)：模型不準時（模型**永遠**不準），或系統隨時間改變時（例如溫度改變，致動器反應也變），控制器仍然表現良好。

古典控制（例如 Stanford ENGR 105）對這些都有工具。

> ⚠️ 逐字稿缺字 [▶ 12:30](https://youtu.be/Au2stLALZew?t=750)：字幕寫「the **hum** temperature」，應為 **home** temperature（室溫）。

### 2.3 古典控制少了什麼：最佳、規劃、學習

[▶ 14:04](https://youtu.be/Au2stLALZew?t=844)

1. **性能（最佳）**：達到穩定的方法很多，哪一個**最好**？例如最省控制力氣的。
2. **規劃**（planning）：方塊圖假設有人給你參考訊號。控制室溫時很明顯，但控制飛機路徑時，**那條路徑從哪裡來**？
3. **學習**（learning）[▶ 14:35](https://youtu.be/Au2stLALZew?t=875)：上面都假設模型已知。如果不知道，或系統運作中會變，怎麼辦？

這三點就是本課的核心 [▶ 15:06](https://youtu.be/Au2stLALZew?t=906)：

- **Optimal**（最佳）→ 性能目標。
- **Learning-based**（學習型）→ 從資料學模型、根據資料調整控制器。
- 而且要把參考訊號（規劃）也納入控制分析。

**歷史** [▶ 16:07](https://youtu.be/Au2stLALZew?t=967)

【口頭】最佳控制約有 50 年歷史，起源於冷戰時期最佳化彈道飛彈軌跡。兩個先驅各自獨立發展，理論方法不同但有很多共通點：

| | 美國 | 蘇聯 |
|---|---|---|
| 先驅 | **Richard Bellman**（Bellman 方程就是他） | **Pontryagin**（失明的數學家） |
| 之後在本課 | 動態規劃（DP） | 間接法（Pontryagin 最小原理） |

---

## 3. 課程地圖

[▶ 16:38](https://youtu.be/Au2stLALZew?t=998) 這張圖老師說會「陪我們一整學期」。

```
                        最佳控制（模型已知）
          ┌─────────────────────┬─────────────────────┐
     開迴路最佳控制          MPC（橋樑）            閉迴路最佳控制
     ├─ 間接法                                    ├─ 動態規劃（DP）
     └─ 直接法                                    └─ HJB／HJI（可達性）
     （約 3 週）            （約 2–3 堂）           （約 2 週）

                     資料驅動最佳控制（模型未知）
          ├─ 模仿學習（imitation learning）
          └─ 強化學習（reinforcement learning）
               ├─ 基於模型（model-based）
               └─ 無模型（model-free）
```

**開迴路**（open-loop）[▶ 17:09](https://youtu.be/Au2stLALZew?t=1029)：先算好一整串控制動作，然後**照做，不再看世界**。

【口頭】「我要走到那扇門。我規劃好路線，閉上眼睛，祈禱好運。」如果有同學站起來，我就撞上去了。

**閉迴路**（closed-loop）：規劃，但一直量測、重新最佳化。

| | 開迴路 | 閉迴路 |
|---|---|---|
| 計算 | **非常有效率** | 比較貴（要考慮各種突發狀況） |
| 擾動 | 脆弱（brittle） | 天生能處理 |
| 本課方法 | 間接法、直接法 | 動態規劃、HJB／HJI |

[▶ 18:14](https://youtu.be/Au2stLALZew?t=1094) 為什麼先學開迴路？雖然比較弱，但計算很快；有些應用開迴路就夠用。

[▶ 19:16](https://youtu.be/Au2stLALZew?t=1156) 閉迴路有兩支：

- **動態規劃**（dynamic programming，DP）。
- **Hamilton–Jacobi–Bellman（HJB）、Hamilton–Jacobi–Isaacs（HJI）方程**：DP 的連續時間版本。它們給出**可達性**（reachability）的方法，用來在控制器外面加**安全護欄**（safety guardrail）。

**MPC：兩者兼得** [▶ 19:47](https://youtu.be/Au2stLALZew?t=1187)

**模型預測控制**（model predictive control，MPC）。老師說它是 PID 之後**用得最廣的控制方法**。

做法：解一個開迴路問題 → 只執行控制序列的**前一小段** → 量測 → 重新解開迴路問題 → ……每一刻解的都是開迴路問題，但因為一直重新量測，整體是閉迴路。

**學習的部分** [▶ 20:47](https://youtu.be/Au2stLALZew?t=1247)：後半學期**不再假設**知道模型。

- **模仿學習**（imitation learning）[▶ 21:49](https://youtu.be/Au2stLALZew?t=1309)：拿到最佳策略的示範，去模仿它。
- **強化學習**（reinforcement learning，RL）：不模仿老師，自己**試誤**（trial and error）學。分 model-based 和 model-free。

【口頭】[▶ 22:21](https://youtu.be/Au2stLALZew?t=1341) 這些方法**不是互相競爭**，常常混用。例子：

- 自駕車：先用模仿學習得到不錯的駕駛策略（bootstrap），再用 RL 改進。
- 推理模型：先監督式微調（supervised fine-tuning），再用各種 RL 改進。

【口頭】[▶ 23:53](https://youtu.be/Au2stLALZew?t=1433) 現代機器人系統這些方法全都用，「儘管大家炒作視覺語言模型能解決一切」。

**課程目標** [▶ 24:23](https://youtu.be/Au2stLALZew?t=1463)：

1. 學主要方法的**理論和實作**（所以作業有理論題也有 Python）。
2. 給一個**統一框架**，把古典最佳控制、DP、RL 串起來，讓你知道什麼時候用什麼工具。

【口頭】「不要太愛上某一個工具。」很多人愛上某種模仿學習，就拿它去解世界上每個問題——機器人和最佳控制不是這樣運作的。

---

## 4. 最佳控制問題的三個成分

[▶ 26:58](https://youtu.be/Au2stLALZew?t=1618) 上面地圖裡**所有方法解的都是同一個問題**。這個問題有三個成分：

1. 被控系統的**數學模型**。
2. **約束**（constraints）：古典回饋控制通常不明確處理，但最佳控制要納入。例如自駕車不能撞別的車。
3. **性能指標**（performance criterion）。

（課本 §2.1 的三個成分跟這裡一樣。）

### 4.1 數學模型：常微分方程

[▶ 27:59](https://youtu.be/Au2stLALZew?t=1679) 本課的模型是一組**常微分方程**（ordinary differential equation，ODE）：

$$
\begin{aligned}
\dot x_1(t) &= f_1\left(x_1(t),\dots,x_n(t),\ u_1(t),\dots,u_m(t),\ t\right) \\
&\ \ \vdots \\
\dot x_n(t) &= f_n\left(x_1(t),\dots,x_n(t),\ u_1(t),\dots,u_m(t),\ t\right)
\end{aligned}
$$

- $x_1,\dots,x_n$：**狀態**（state）。和控制一起，就能預測系統未來會怎樣。
- $u_1,\dots,u_m$：**控制輸入**（control input），例如油門和方向盤。
- $f_1,\dots,f_n$：告訴你狀態怎麼隨現在的狀態和控制演變。
- 點 $\dot x$ = 對時間微分；兩點 $\ddot x$ = 二次微分。

寫成向量：$\dot{\mathbf{x}}(t)=\mathbf{f}\left(\mathbf{x}(t),\mathbf{u}(t),t\right)$。

**為什麼 ODE =「預測未來的機制」** [▶ 29:38](https://youtu.be/Au2stLALZew?t=1778)

一維情況 $\dot x(t)=f(x(t),u(t),t)$。導數用差分近似（$\Delta t$ 很小，例如 0.1 秒）：

$$\dot x(t)\approx\frac{x(t+\Delta t)-x(t)}{\Delta t}$$

代進去：

$$\frac{x(t+\Delta t)-x(t)}{\Delta t}\approx f(x(t),u(t),t)\ \Rightarrow\ x(t+\Delta t)\approx x(t)+\Delta t\cdot f(x(t),u(t),t)$$

所以知道現在的 $x$、$u$ 和 $f$，就知道 $\Delta t$ 之後的狀態。

【口頭】[▶ 31:51](https://youtu.be/Au2stLALZew?t=1911) 「數學家看到 ODE 看到的是美麗的數學物件；我看到的是預測未來的機制。」

**本課不假設線性** [▶ 32:21](https://youtu.be/Au2stLALZew?t=1941)：$f$ 可以是任何函數。這已經離開了標準控制課常做的線性假設。

**$f$ 可以顯式依賴時間** [▶ 32:54](https://youtu.be/Au2stLALZew?t=1974)：同樣的狀態和控制，在不同時間可能反應不同。例如白天和晚上系統反應不一樣。

**用語** [▶ 33:59](https://youtu.be/Au2stLALZew?t=2039)：

- **控制歷史**（control history）：一段時間內的控制輸入值。
- **軌跡**（trajectory）：$[t_0,t_f]$ 內的狀態值。
- $t_0$：初始時間；$t_f$：終端時間（final time）。

### 4.2 例子：雙積分器

[▶ 33:59](https://youtu.be/Au2stLALZew?t=2039) 一台推車在水平面上動。$s$ 是推車中心離原點的位移。我們控制加速度（質量設為 1）：

$$\ddot s(t)=u(t)$$

這是**二階** ODE。但本課要的是**一階** ODE 系統。

**技巧：加狀態** [▶ 35:32](https://youtu.be/Au2stLALZew?t=2132)。新增狀態 $v$（速度）：

$$
\begin{aligned}
\dot s(t) &= v(t) &&\text{（位移的導數 = 速度）}\\
\dot v(t) &= u(t) &&\text{（速度的導數 = 加速度 = 輸入）}
\end{aligned}
$$

高階 ODE **一定**能用這招變成一階 ODE 系統，而且是一對一的。所以用本課方法前，先把系統化成一階形式。

**矩陣形式** [▶ 37:36](https://youtu.be/Au2stLALZew?t=2256)：這個系統是線性的，可寫成 $\dot{\mathbf{x}}=A\mathbf{x}+B\mathbf{u}$，$A$ 叫**狀態矩陣**（state matrix），$B$ 叫**輸入矩陣**（input matrix）。

> 以下**不是逐字稿內容**，是依上面兩條方程寫出的矩陣（老師說「not important now」沒有唸出來）：
> $$\mathbf{x}=\begin{pmatrix}s\\v\end{pmatrix},\qquad A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}0\\1\end{pmatrix}$$

### 4.3 約束

[▶ 38:08](https://youtu.be/Au2stLALZew?t=2288) 常見的約束：

| 種類 | 例子 |
|---|---|
| **初始條件** | 知道從哪裡出發：$x(t_0)=x_0$ |
| **終端條件**（有時有、有時沒有） | 太空船要降落在火星某個隕石坑：$x(t_f)=x_f$ |
| **狀態約束** | 避開壞區域：上下界；或「待在圓外面」（圓 = 一個人，機器人不能碰到他） |
| **控制約束** | 推力有上下界 |

> ⚠️ 逐字稿缺字 [▶ 38:39](https://youtu.be/Au2stLALZew?t=2319)：字幕寫「a **trust** level that is above a certain quantity」，應為 **thrust**（推力）。

【口頭】[▶ 39:10](https://youtu.be/Au2stLALZew?t=2350) 老師來 Stanford 前在 NASA JPL 工作，火星精準降落正是他當時研究的問題。

【口頭】[▶ 39:40](https://youtu.be/Au2stLALZew?t=2380) 約束可以寫得很自由，但寫得太複雜，後面的數學方法會變難。

**可容許**（admissible）[▶ 40:10](https://youtu.be/Au2stLALZew?t=2410)：

- 控制歷史在所有時間都滿足控制約束 → **可容許控制**（admissible control）。
- 狀態軌跡在所有時間都滿足狀態約束 → **可容許軌跡**（admissible trajectory）。

【課本補充】課本 Definition 2.1.1 寫成：$x(t)\in\mathcal{X}$ 且 $u(t)\in\mathcal{U}$，$\forall t\in[t_0,t_f]$。課本註解：這讓數值方法可以只考慮可容許的序列。

### 4.4 性能指標

[▶ 40:40](https://youtu.be/Au2stLALZew?t=2440) 本課只用這種形式：

$$J=h\left(x(t_f),t_f\right)+\int_{t_0}^{t_f} g\left(x(t),u(t),t\right)\,dt$$

【口頭】這不是最一般的形式，但在「夠一般」和「算得出來」之間取得平衡。最佳控制一直有這個張力：問題描述越精緻越好，但精緻到解不出來就沒用了。

**終端成本**（terminal cost）$h$ [▶ 42:19](https://youtu.be/Au2stLALZew?t=2539)：在 $t_f$ 停在 $x(t_f)$，你有多不開心。

例：想在 $t_f$ 到達 $x_f$：

$$h\left(x(t_f),t_f\right)=\left\|x(t_f)-x_f\right\|^2$$

剛好到達 → 0；偏離越多 → 成本越大。

> ⚠️ 逐字稿缺字 [▶ 42:54](https://youtu.be/Au2stLALZew?t=2574)：字幕寫「x tf minus **f**」，應為 $x_f$（期望終點）。

**運行成本**（running cost）$g$ [▶ 43:58](https://youtu.be/Au2stLALZew?t=2638)：

- $g(x,u,t)$ 是**每單位時間**付的成本（老師也叫 stage-wise cost）。
- 積分 = 從 $t_0$ 到 $t_f$ 加總 → 沿軌跡的**累積成本**。
- 典型例子 [▶ 45:30](https://youtu.be/Au2stLALZew?t=2730)：$g=u(t)^2$，代表控制力氣（能量）；積分起來是總共花的燃料。

【口頭】[▶ 45:30](https://youtu.be/Au2stLALZew?t=2730) 學過 DP 的話，這跟 DP 的成本沒兩樣：積分變成加總，成本就是各階段成本的和。因為解的是同一個問題。

> ⚠️ 逐字稿缺字 [▶ 46:00](https://youtu.be/Au2stLALZew?t=2760)：字幕寫「this becomes a **submission**」，應為 **summation**（加總）。

【Q&A】[▶ 46:00](https://youtu.be/Au2stLALZew?t=2760) 學生問運行成本是不是可以放追蹤誤差。答：可以。例如
$$g=\left\|x(t)-x_{\text{ref}}(t)\right\|^2,\qquad h=t_f^2$$
前者讓實際軌跡貼近參考軌跡，後者懲罰花太久時間。

**$t_f$ 固定或自由** [▶ 47:02](https://youtu.be/Au2stLALZew?t=2822)：

- $t_0$ 通常給定。
- $t_f$ 可以**給定**（例如 10 秒內完成），也可以**自由**（越快越好，同時誤差要小）。自由時要在成本裡放跟時間有關的項，才能表達「最小化時間」。

【課本補充】課本：$t_f$ 可以是有限固定、有限自由、或無限。無限時通常忽略終端成本（設 $h=0$）。

【Q&A】[▶ 51:45](https://youtu.be/Au2stLALZew?t=3105) 學生問：為什麼要把終端項和積分項分開寫？答：對，有時同一個成本兩邊都能表達，看方便。

**目標函數的取捨** 【Q&A】[▶ 25:27](https://youtu.be/Au2stLALZew?t=1527) 學生問最佳是用哪個指標定義？答：**設計者決定**。可以考慮不要失控、控制力氣、時間。但「越快」通常和「越省」衝突——要快就得花更多燃料——所以要做取捨。

**為什麼成本要是「加總」形式** [▶ 50:13](https://youtu.be/Au2stLALZew?t=3013)

【口頭】積分本質上是加總。加總讓你能**把問題切成小塊**。在離散時間這會導出**最佳性原理**（principle of optimality，連續時間也有對應），大幅減少要搜尋的解。如果成本不是加法結構，這些結構全部失效，計算會變得極難。之後講 DP 時會更清楚。

### 4.5 最佳控制問題的完整敘述

[▶ 47:33](https://youtu.be/Au2stLALZew?t=2853)

> **最佳控制問題**：找一個可容許控制 $u^*$，使系統 $\dot x=f(x,u,t)$ 走出可容許軌跡 $x^*$，並且 $(u^*,x^*)$ 讓
> $$J=h\left(x(t_f),t_f\right)+\int_{t_0}^{t_f}g\left(x(t),u(t),t\right)dt$$
> 最小。

- 選定 $u$ 後，$x$ 由 ODE **唯一決定**。但成本同時依賴 $x$ 和 $u$。**決策變數是 $u(t)$。**

【課本補充】課本式 (2.3) 寫成最佳化問題的樣子：
$$
\begin{aligned}
\underset{u(t)}{\text{minimize}}\quad & J \\
\text{subject to}\quad & \dot x(t)=f(x(t),u(t),t),\quad x(t_0)=x_0,\quad x(t_f)=x_f,\quad x(t)\in\mathcal{X},\quad u(t)\in\mathcal{U}
\end{aligned}
$$
課本把 $J$ 叫 **cost functional**（成本泛函）：**泛函**（functional）把「函數」對應到實數，可以想成「函數的函數」。

**難在哪：無限維** [▶ 48:38](https://youtu.be/Au2stLALZew?t=2918)

- 一般最佳化：有限個決策變數。例如 $\min x_1^2+x_2^2$，只要選兩個數。
- 這裡：$u(t)$ 是時間的函數。要選 $u(t_0)$、$u(t_0+\varepsilon)$、$u(t_0+2\varepsilon)$……$\varepsilon$ 任意小 → **無限多個**變數。
- 所以叫**無限維最佳化問題**（infinite-dimensional optimization problem）。
- 好消息：很多工具可以從有限維最佳化回收來用。接下來幾堂會講這些橋樑。

**其他注意事項** [▶ 52:15](https://youtu.be/Au2stLALZew?t=3135)：

- 這個敘述找的是**全域**最小，但有時只能接受局部最小。
- 解**不一定存在**；存在也**不一定唯一**。
- 最大化問題都能改成最小化：$\max F\iff\min(-F)$。

---

## 5. 控制界和電腦科學界的用語對照

[▶ 53:18](https://youtu.be/Au2stLALZew?t=3198)

| | 控制界 | 電腦科學界 |
|---|---|---|
| 性能指標 | 成本（cost）$J$，**最小化** | 獎勵（reward）$r$，**最大化** |
| 狀態 | $x$ | $s$ |
| 控制 | $u$ | $a$（action，動作） |

【口頭】「至於為什麼一個社群愛最大化、另一個愛最小化，心理學上的考量留給你們。」

本課前三分之二用控制界記號，最後三分之一（RL）換成電腦科學記號，比較接近論文。

---

## 6. 開迴路 vs 閉迴路

[▶ 54:52](https://youtu.be/Au2stLALZew?t=3292) 老師說這個差別看起來細微，但**非常重要**，連資深研究者都會搞混。

| | 開迴路 | 閉迴路 |
|---|---|---|
| 控制是誰的函數 | **時間**和**初始狀態**：$u^*=e\left(x(t_0),t\right)$ | **目前狀態**（和時間）：$u^*=\pi\left(x(t),t\right)$ |
| 走到門的例子 | 先算好每一步，閉眼照走 | 眼睛張開，每一刻依當下狀態決定 |
| 有人站起來 | 撞上去 | 繞過去 |

[▶ 56:59](https://youtu.be/Au2stLALZew?t=3419) 閉迴路是在更大的類別裡最佳化（開迴路是它的子集）：不只告訴你「一切照計畫時」怎麼做，也告訴你「出狀況時」怎麼做。代價是要一直量測狀態。

$\pi$ 叫**策略**（policy）：把狀態對應到最佳控制動作的函數。

【Q&A】[▶ 57:32](https://youtu.be/Au2stLALZew?t=3452) 學生問記號。答：$\pi$ 是閉迴路策略的標準記號。開迴路的 $e$ 是老師為了「囉嗦清楚」自己取的；一般人直接寫 $u^*(t)$，對初始狀態的依賴不寫出來。

【課本補充】課本第 2 章開頭把開迴路寫成 $u^*(t)=\ell\left(x(t_0),t\right)$（式 2.4），用的字母是 $\ell$，不是 $e$。

【Q&A】[▶ 60:41](https://youtu.be/Au2stLALZew?t=3641) 學生問：閉迴路也依賴初始狀態啊，差別在哪？
答：閉迴路**還**依賴所有**未來**的狀態，告訴你在世界的任何狀態下怎麼做最好。（狀態也可以包含你和周圍所有人的相對位置。）開迴路固定初始條件、算出控制序列後，就盲目執行，不管發生什麼。

【口頭】[▶ 61:44](https://youtu.be/Au2stLALZew?t=3704) 聽起來很瘋狂，但像太空船飛往月球，開迴路可能就夠了。而且實務上通常用**滾動時域**（receding horizon）執行：執行前 10%，張開眼看看，重算一個新的開迴路序列。這就通往 MPC——整體是閉迴路，但每一刻只解開迴路問題，計算上比較划算。

【課本補充】課本也說：只考慮開迴路策略在軌跡最佳化裡很自然，因為它計算快；強健性可以靠閉迴路追蹤，或像 MPC 那樣滾動重新最佳化來補。

---

## 7. 離散時間版本

[▶ 59:08](https://youtu.be/Au2stLALZew?t=3548) 把上面全部離散化，得到幾乎一樣的問題：

$$
\begin{aligned}
\text{動態：}\quad & x_{k+1}=f(x_k,u_k,k) \\
\text{成本：}\quad & J=h(x_N)+\sum_{k=0}^{N-1}g(x_k,u_k,k) \\
\text{約束：}\quad & u_k\in\mathcal{U}
\end{aligned}
$$

> 以下**不是逐字稿內容**：成本式子的具體寫法（終端時刻記為 $N$）是依「積分換成加總」寫出的，投影片原式字幕沒有唸。

開迴路／閉迴路的概念完全一樣。推廣到隨機情況就是**馬可夫決策過程**（Markov decision process，MDP），後面會講。前期先專注在確定性（deterministic）問題。

---

## 8. 擾動怎麼建模

【Q&A】[▶ 62:49](https://youtu.be/Au2stLALZew?t=3769) 學生問擾動怎麼放進模型。答：幾種方式：

1. **明確放進動態**：$f$ 多一個擾動變數 $w$，再給擾動一個模型：
   - **隨機**（stochastic）：照某個機率分布隨機產生。→ 之後的 MDP。
   - **確定性最壞情況**（worst case）：假設大自然在某個範圍內**故意**最大程度干擾你，類似賽局。→ 之後的**微分賽局**（differential games）。
2. **不明確建模**：設計時忽略擾動，但讓軌跡離約束邊界留夠多**緩衝**，小擾動就不會撞到東西。

【口頭】[▶ 64:52](https://youtu.be/Au2stLALZew?t=3892) 預告幾週後要解的經典問題：

- **殺人司機問題**（homicidal chauffeur）：你是行人，要從起點走到終點；有一台車想撞你。車比你快，但行人可以**原地轉任意方向**，車不能橫移。問題：從哪些初始條件出發，可以保證不被撞到終點？
- **湖中女士**（lady in the lake）：一位女士要游到岸邊柵欄，有怪物在岸上追她。

---

## 9. 預告：先學古典最佳化

[▶ 66:27](https://youtu.be/Au2stLALZew?t=3987) 最佳控制說到底是一個**最佳化問題**，只是很難（維度很高甚至無限維）。所以接下來幾堂先退一步，看**古典最佳化**（有限個變數）有哪些工具：必要最佳性條件、計算方法。之後再把直覺搬到最佳控制。

**無約束非線性規劃**（unconstrained nonlinear programming）[▶ 67:31](https://youtu.be/Au2stLALZew?t=4051)：

$$\min_{x\in\mathbb{R}^n} f(x)$$

$x=(x_1,\dots,x_n)$ 是 $n$ 個要選的數字。通常假設 $f$ 連續可微，有時二次連續可微。

**局部最小 vs 全域最小** [▶ 69:02](https://youtu.be/Au2stLALZew?t=4142)

> **局部最小值**：存在 $\varepsilon>0$，使得所有 $\|x-x^*\|<\varepsilon$ 的 $x$ 都有 $f(x)\ge f(x^*)$。
>
> **全域最小值**：所有 $x$ 都有 $f(x)\ge f(x^*)$。

圖：$x^*$ 周圍半徑 $\varepsilon$ 的小球裡，函數值都不比 $f(x^*)$ 小。但小球外面可能有更小的點 → $x^*$ 只是局部最小，不是全域最小。

> ⚠️ 逐字稿缺字 [▶ 70:06](https://youtu.be/Au2stLALZew?t=4206)：字幕寫「the value of the function f is **lower** than f of x star」，依接下來的說明（$f(x)\ge f(x^*)$）應為「**higher**（不低於）」。

**下次預告** [▶ 71:09](https://youtu.be/Au2stLALZew?t=4269)：必要最佳性條件。如果 $x^*$ 是局部最小，那麼 $\nabla f(x^*)=0$。用途是當過濾器：找出所有滿足條件的點（希望不多），一個一個算函數值，最小的就是最小值。之後這個概念會搬到最佳控制，條件會更複雜，但想法一樣。然後加入約束 $h(x)\le$ 某個數，更接近最佳控制的形式。

---

## 10. 一頁速查表

### 最佳控制問題

$$
\begin{aligned}
\underset{u(\cdot)}{\min}\quad & J=h\left(x(t_f),t_f\right)+\int_{t_0}^{t_f}g\left(x(t),u(t),t\right)dt \\
\text{s.t.}\quad & \dot x(t)=f\left(x(t),u(t),t\right),\quad x(t_0)=x_0 \\
& x(t)\in\mathcal{X},\quad u(t)\in\mathcal{U}\quad(\text{可容許}),\quad \text{可能還有 }x(t_f)=x_f
\end{aligned}
$$

| 項目 | 重點 |
|---|---|
| 三成分 | 模型（ODE）、約束、性能指標 |
| ODE 的意思 | $x(t+\Delta t)\approx x(t)+\Delta t\,f(x,u,t)$：預測未來 |
| 高階 → 一階 | 加狀態：$\ddot s=u\ \Rightarrow\ \dot s=v,\ \dot v=u$ |
| 終端成本 $h$ | 結束時多不開心，例 $\|x(t_f)-x_f\|^2$ |
| 運行成本 $g$ | 每單位時間的成本，例 $u^2$（能量）、$\|x-x_{\text{ref}}\|^2$（追蹤） |
| 為什麼要加法結構 | 能切成小塊 → 最佳性原理 → DP |
| 難處 | 無限維；解可能不存在、不唯一 |
| $\max F$ | $=\min(-F)$ |

### 開迴路 vs 閉迴路

| | 開迴路 | 閉迴路 |
|---|---|---|
| 形式 | $u^*(t)=e(x(t_0),t)$（課本記 $\ell$） | $u^*=\pi(x(t),t)$（策略） |
| 優點 | 計算快 | 能處理擾動 |
| 缺點 | 脆弱 | 計算貴 |
| 折衷 | MPC：每刻解開迴路，只執行前一段，再量測重解 | |

### 用語

控制 $(x,u,J\ \min)$ ⟷ 電腦科學 $(s,a,r\ \max)$

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 局部／全域最小、必要條件預告 | 第 2 集最佳化理論 |
| 無限維最佳化 | 第 3 集變分法（泛函的最小化） |
| Pontryagin | 第 4 集間接法（Pontryagin 最小原理） |
| 開迴路：間接法、直接法 | 第 4、5、6 集 |
| 閉迴路：DP、Bellman | 第 7、9 集 |
| HJB／HJI、可達性、殺人司機 | 第 10 集可達性分析 |
| MPC、滾動時域 | 第 11、12 集 |
| 模仿學習、RL、記號 $s,a,r$ | 第 13–19 集 |

---

## 附：本集一句話總結

> **本課所有方法——間接法、直接法、DP、MPC、模仿學習、RL——都在解同一個問題：在 ODE 動態和約束下，選一個控制函數 $u(t)$ 讓「終端成本＋累積運行成本」最小。差別只在開迴路或閉迴路、模型已知或要從資料學。**

---

## ⚠️ 待確認清單

1. 上課日期：只知道是週一，確切日期待補。
2. [▶ 02:41](https://youtu.be/Au2stLALZew?t=161) Recitation 要教的工具，字幕寫「jags」，推測是 JAX，待確認。
3. [▶ 59:08](https://youtu.be/Au2stLALZew?t=3548) 離散時間成本的具體式子（終端時刻記號）是推論的，待對照投影片。

---

*筆記依據 Marco Pavone「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 1 錄影逐字稿（人工字幕，1:13:23）與《Principles of Robot Autonomy》§2.1 整理。*
