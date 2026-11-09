---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 17
lecture: Lecture 17
date: 待補（第 9 週週三；週一放假）
video: https://youtu.be/zanXSI7zSws
notes: 《Principles of Robot Autonomy》§18.4–18.5.1（書頁 473–478，PDF 頁 475–480）：同策略／離策略、Q-learning、函數近似、Fitted Q-learning；SARSA、DQN 課本沒有
---

# 第 17 集 · Lecture 17：基於值的強化學習（RL Value-Based Methods） [▶ 影片](https://youtu.be/zanXSI7zSws)

← 上一集：[16-fundamentals-of-rl](16-fundamentals-of-rl.md) ｜ [總目錄](README.md) ｜ 下一集：[18-policy-optimization](18-policy-optimization.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 17 集
> **講者**：待確認（本集沒有自我介紹；推測同為 Daniele Gammelli）
> **來源**：YouTube 錄影逐字稿（1:17:40，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§18.4–18.5.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：預測 vs 控制](#1-回顧預測-vs-控制)
- [2. SARSA：把 MC 換成 TD](#2-sarsa把-mc-換成-td)
  - [2.1 更新式](#21-更新式)
  - [2.2 例子：有風的格子世界](#22-例子有風的格子世界)
- [3. 同策略 vs 離策略](#3-同策略-vs-離策略)
- [4. Q-learning](#4-q-learning)
  - [4.1 從離策略推出 Q-learning](#41-從離策略推出-q-learning)
  - [4.2 例子：懸崖行走](#42-例子懸崖行走)
- [5. 值函數近似](#5-值函數近似)
  - [5.1 為什麼要近似](#51-為什麼要近似)
  - [5.2 三種架構](#52-三種架構)
  - [5.3 用 MC／TD 目標做迴歸](#53-用-mctd-目標做迴歸)
  - [5.4 Fitted Q-iteration](#54-fitted-q-iteration)
- [6. 深度 Q 網路（DQN）](#6-深度-q-網路dqn)
  - [6.1 架構](#61-架構)
  - [6.2 兩個穩定技巧：經驗回放、固定目標](#62-兩個穩定技巧經驗回放固定目標)
- [7. 演算法整理](#7-演算法整理)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/zanXSI7zSws?t=5) 從今天到學期末，看具體的演算法類別。今天：**基於值**的方法（屬於無模型 RL）。

【口頭】參考：Sutton & Barto 教科書，以及 **David Silver** 的課（今天有些投影片受它啟發）。

今天：

1. 兩個很流行的基於值的演算法：**SARSA** 和 **Q-learning**。
2. 用它們深入**同策略**（on-policy）和**離策略**（off-policy）的差別。
3. **值函數近似**：擴展到高維狀態和動作空間。
4. 深度 RL 方法和應用（DQN）。

| 主題 | 課本 |
|---|---|
| 同策略 vs 離策略 | §18.4 |
| SARSA | 課本沒有 |
| Q-learning | §18.5.1、Algorithm 18.5 |
| 值函數近似、Fitted Q-learning | §18.5.1 |
| DQN、經驗回放、目標網路 | 課本沒有 |

---

## 1. 回顧：預測 vs 控制

[▶ 01:08](https://youtu.be/zanXSI7zSws?t=68)

| | 預測（prediction） | 控制（control） |
|---|---|---|
| 目標 | 給定策略，估它的值 | 學最佳化表現的策略（真正在乎的） |

- 精確方法（策略迭代、值迭代）需要完美知道動態 $p(x_{t+1}\mid x_t,u_t)$。
- MC 和 TD 從互動學。
- 備份圖：DP 不取樣（有動態）；MC、TD 取樣；TD、DP 自舉；MC 不自舉。
- 這些對 $V$ 成立，對 $Q$ 也一樣。

【Q&A】[▶ 05:46](https://youtu.be/zanXSI7zSws?t=346) 學生問：MC 一定要走到終端狀態嗎？能不能走五步就重新評估？答：MC 一定要到終端狀態，這正是它的限制之一。

**控制**：**廣義策略迭代**——交替策略評估和策略改進。上次的 v0 演算法 **MC 控制**：評估 = MC 估 $Q$，改進 = ε-貪婪。

---

## 2. SARSA：把 MC 換成 TD

[▶ 08:58](https://youtu.be/zanXSI7zSws?t=538) TD 相對 MC 的好處：

- **變異數較低**：只取樣一次；MC 要一路取樣到回合結束，累積更多隨機性。
- **可線上更新**：沿著展開一步步更新。
- 不需要回合結束，能處理**不完整序列**。

所以自然的想法：在 MC 控制裡，把「MC 估 $Q$」換成「**TD 估 $Q$**」→ 這就是 **SARSA**。

### 2.1 更新式

[▶ 11:37](https://youtu.be/zanXSI7zSws?t=697) $Q$ 的 TD 備份需要：目前的 $(x_t,u_t)$、得到的獎勵 $r_t$、下一個狀態 $x_{t+1}$、下一個控制 $u_{t+1}$：

$$\boxed{Q(x_t,u_t)\leftarrow Q(x_t,u_t)+\alpha\left[r_t+\gamma Q(x_{t+1},u_{t+1})-Q(x_t,u_t)\right]}$$

**名字** [▶ 12:39](https://youtu.be/zanXSI7zSws?t=759)：RL 文獻用 $S$（state）、$A$（action）。這五個東西 $(S_t,A_t,R_t,S_{t+1},A_{t+1})$ 拼起來就是 **SARSA**。

【口頭】從我們做的到「史上最有名的演算法之一」只差一小步。

**虛擬碼** [▶ 14:10](https://youtu.be/zanXSI7zSws?t=850)：

```
初始化 Q（例如全 0）
重複（每個回合）：
    初始化 x
    用 ε-貪婪（相對於 Q）選 u
    重複（每一步）：
        執行 u，觀察 r、x'
        用 ε-貪婪（相對於 Q）選 u'
        Q(x,u) ← Q(x,u) + α [ r + γ Q(x',u') − Q(x,u) ]
        x ← x'；u ← u'
```

ε-貪婪：機率 $\varepsilon$ 隨機動作；機率 $1-\varepsilon$ 選 $\arg\max_uQ(x,u)$。

【Q&A】[▶ 16:23](https://youtu.be/zanXSI7zSws?t=983) 學生確認：這是 TD 版的 $Q$ 更新？答：對，只往前看一步。

### 2.2 例子：有風的格子世界

[▶ 16:58](https://youtu.be/zanXSI7zSws?t=1018)

- 從起點格到目標格，動作是四個方向。
- 有虛擬的**風從下往上吹**：每一欄下方標的數字是把 agent **往上推幾格**（例如第三欄 0，第四欄 1……）。
- 目標：最短時間到目標 → 每一步獎勵 $-1$。超參數：$\varepsilon$（ε-貪婪）、$\alpha$（步長）、$\gamma=1$。

> 這是 Sutton & Barto 的 Windy Gridworld（Example 6.5），講者沒說出處。

【課堂討論】[▶ 18:34](https://youtu.be/zanXSI7zSws?t=1114) 講者問最佳策略長怎樣？

- 學生 1：先走到底部再往右。講者：好直覺，但這裡不對——誰看得出為什麼？
- 學生 2：不能同一格又往右又往上；從底部走，風會把你推過頭，到達時已經錯過 G。講者：對！在底部時每走一步都被往上推，某些欄還推兩格，到不了。實際的最佳做法是**先把自己推到天花板**，再往回走到目標。

**訓練曲線** [▶ 19:37](https://youtu.be/zanXSI7zSws?t=1177)：橫軸 = 跟環境互動的時間步數；縱軸 = 成功回合數。

- 一開始 Q 隨機 → 成功 0 次。
- 某個時候靠隨機探索碰巧到了目標 → TD 備份開始把「好」**往回傳**到起點。
- 之後表現越來越好。SARSA 確實收斂到最佳策略。

**MC 在這裡也行嗎？** 【課堂討論】[▶ 21:15](https://youtu.be/zanXSI7zSws?t=1275)：

- 學生：不行，因為只有到達目標才終止，會花很多時間亂逛。講者：直覺對。MC 需要回合終止，而這裡**只有到目標才終止**；運氣好隨機走到了，但一般**不保證**。
- **反例** [▶ 22:15](https://youtu.be/zanXSI7zSws?t=1335)：學習過程中暫時收斂到一個**繞圈**的策略。MC：永遠不會更新 Q，卡在迴圈裡。TD：每一步都線上更新，繞圈一直累積負獎勵，某個時候這個行為會比其他做法差，就跳出來了。

---

## 3. 同策略 vs 離策略

[▶ 24:01](https://youtu.be/zanXSI7zSws?t=1441)

| | 意思 |
|---|---|
| **同策略**（on-policy） | 評估／改進的，就是**目前在環境中做決定的那個策略** |
| **離策略**（off-policy） | 評估／改進的策略，可以**不同於**產生資料的那個策略 |

【課堂討論】SARSA 屬於哪一類？[▶ 25:11](https://youtu.be/zanXSI7zSws?t=1511) 學生說「也是你的策略，因為你在改它」。講者：確實在改，但改的是**正在環境中使用的那個**——ε-貪婪策略本身。所以 **SARSA 是同策略**。策略會隨時間變，但改進的就是拿來互動的那一個。

**離策略的正式說法** [▶ 26:14](https://youtu.be/zanXSI7zSws?t=1574)：

- **目標策略**（target policy）$\pi$：想評估（算值函數）的策略。
- **行為策略**（behavior policy）$\mu$：實際跟環境互動、產生資料的策略。
- 更新式用的資料是照 $\mu$ 收集的。

**為什麼重要** [▶ 26:45](https://youtu.be/zanXSI7zSws?t=1605)：

1. **不能無限互動**（例如機器人）：有時只能看人類或其他 agent 做事來學。能從別的策略產生的觀測學習，很有用。
2. **重用舊資料** [▶ 27:55](https://youtu.be/zanXSI7zSws?t=1675)：GPI 中策略一直在進步，資料是由一連串不同版本的策略產生的。到目前為止只用最新的互動、把舊資料丟掉——很浪費。
3. **解耦探索和利用** [▶ 28:57](https://youtu.be/zanXSI7zSws?t=1737)（離策略方法最為人知的理由）：可以學**最佳**策略（通常是確定性的、利用型的），同時用另一個比較**隨機**的探索策略收集資料。

【課本補充】課本 §18.4：同策略方法通常更簡單、更可靠；離策略方法能從任意行為策略產生的資料學（包括人類示範、傳統非學習型控制器的資料），但學習可能較不穩定、收斂較慢。

---

## 4. Q-learning

### 4.1 從離策略推出 Q-learning

[▶ 29:29](https://youtu.be/zanXSI7zSws?t=1769) 從 SARSA 改成離策略：

- SARSA 用行為策略 $\mu$ 產生 $(x_t,u_t,r_t,x_{t+1})$，**也用 $\mu$** 產生 $u_{t+1}$。
- 改成：$u_{t+1}'$ 從**目標策略** $\pi$ 產生，往**這個替代動作**的值更新 [▶ 30:31](https://youtu.be/zanXSI7zSws?t=1831)：

$$Q(x_t,u_t)\leftarrow Q(x_t,u_t)+\alpha\left[r_t+\gamma Q(x_{t+1},u_{t+1}')-Q(x_t,u_t)\right],\qquad u_{t+1}'\sim\pi$$

**Q-learning 的選擇** [▶ 31:37](https://youtu.be/zanXSI7zSws?t=1897)：

| 策略 | 選擇 |
|---|---|
| 目標策略 $\pi$（想學的） | 相對於 $Q$ 的**貪婪**策略：$\pi(x)=\arg\max_uQ(x,u)$ |
| 行為策略 $\mu$（拿來互動的） | **ε-貪婪**策略 |

**TD 目標變成** [▶ 32:41](https://youtu.be/zanXSI7zSws?t=1961)：

$$r_t+\gamma Q\left(x_{t+1},\arg\max_{u'}Q(x_{t+1},u')\right)=r_t+\gamma\max_{u'}Q(x_{t+1},u')$$

$$\boxed{Q(x_t,u_t)\leftarrow Q(x_t,u_t)+\alpha\left[r_t+\gamma\max_{u'}Q(x_{t+1},u')-Q(x_t,u_t)\right]}$$

**虛擬碼** [▶ 34:50](https://youtu.be/zanXSI7zSws?t=2090)：

```
初始化 Q
重複：
    在 x，用 ε-貪婪（行為策略）選 u
    執行 u，觀察 r、x'
    Q(x,u) ← Q(x,u) + α [ r + γ max_u' Q(x',u') − Q(x,u) ]
    x ← x'
```

【Q&A】[▶ 35:20](https://youtu.be/zanXSI7zSws?t=2120) 學生確認：行為策略只產生前四個元素？答：對。用 ε-貪婪在環境中產生前四個，然後**假想**自己會採取（貪婪的）那個替代動作。

【Q&A】[▶ 35:50](https://youtu.be/zanXSI7zSws?t=2150) 學生問這個新的部分是什麼？答：定義了兩個策略：行為策略跟環境互動；目標策略是真正想學的。$u'_{t+1}$ 從目標策略抽。Q-learning 裡目標策略是貪婪（argmax），行為策略是 ε-貪婪。

**理論** [▶ 37:24](https://youtu.be/zanXSI7zSws?t=2244)：在一些正則假設下，Q-learning **收斂到最佳動作值函數** $Q^*$，因此學到最佳策略。

【課本補充】課本 §18.5.1、Algorithm 18.5 是 Q-learning，並說它是離策略、估計的是 $Q^*$（不管行為策略是什麼）。

### 4.2 例子：懸崖行走

[▶ 38:28](https://youtu.be/zanXSI7zSws?t=2308)

- 從起點到終點，沒有風，但中間有一段**懸崖**（失敗區）。
- 每一步 $-1$；掉下懸崖 $-100$，並被送回起點。
- 兩種演算法都用**固定的** ε-貪婪。

> 這是 Sutton & Barto 的 Cliff Walking（Example 6.6），講者沒說出處。

**結果** [▶ 38:59](https://youtu.be/zanXSI7zSws?t=2339)：

| | 收斂到的路徑（貪婪執行時） | 訓練時每回合獎勵總和 |
|---|---|---|
| **SARSA**（藍） | 比較**安全**的路：靠上方、離懸崖遠 | **較高** |
| **Q-learning**（紅） | **最佳**（最短）路：貼著懸崖邊走 | **較低** |

**為什麼** [▶ 39:32](https://youtu.be/zanXSI7zSws?t=2372)：

- SARSA 是**同策略** → 學到的是**它自己的探索策略的最佳版本**：最佳的 ε-貪婪策略。
- Q-learning 是**離策略** → 把行為和學習目標分開 → 收斂到**最佳策略** $\pi^*$。
- 訓練時兩者都**ε-貪婪地行動**：Q-learning 貼著懸崖走，偶爾的隨機動作就會掉下去 → 訓練分數較低。SARSA 把 ε-貪婪的不確定性考慮進去，選了比較安全、離懸崖較遠的路。

【Q&A】[▶ 41:07](https://youtu.be/zanXSI7zSws?t=2467) 學生問：SARSA 一般都會收斂到比較安全的策略嗎？答：這是這組超參數下的情況。可以讓 $\varepsilon$ 依某個排程**衰減**，SARSA 也會收斂到最佳策略。SARSA 也有理論：在特定的 $\varepsilon$ 衰減方式和步長條件下收斂到最佳策略。

【Q&A】[▶ 42:09](https://youtu.be/zanXSI7zSws?t=2529) 學生問：Q-learning 路比較短，為什麼獎勵比較低？兩條路都沒穿過懸崖啊？答：路徑圖是**訓練完、貪婪地**依 Q 行動時的樣子。訓練時不是貪婪，而是 ε-貪婪；Q-learning 離懸崖近，有 $\varepsilon$ 比例的時間會掉下去、拿到 $-100$。曲線量的是**ε-貪婪地執行**兩個 Q 函數的表現。

【Q&A】[▶ 44:21](https://youtu.be/zanXSI7zSws?t=2661) 學生確認：所以訓練時 Q-learning 分數低，但它收斂到的策略本身獎勵比較高？答：對，這點非常重要。

【Q&A】[▶ 44:55](https://youtu.be/zanXSI7zSws?t=2695) 學生問有沒有做 $\varepsilon$ 衰減？答：沒有，固定超參數。有衰減的話 SARSA 也會收斂到最佳策略。

---

## 5. 值函數近似

### 5.1 為什麼要近似

[▶ 45:57](https://youtu.be/zanXSI7zSws?t=2757) 到目前都是小型玩具世界。但 RL 的著名成功（例如 **AlphaGo**）狀態空間超大：圍棋約有 $10^{170}$ 種盤面，「比宇宙的原子還多」。而且遊戲算比較簡單的，真實世界維度更高。

**表格表示的問題** [▶ 47:32](https://youtu.be/zanXSI7zSws?t=2852)：

1. **記憶體**：$10^{170}$ 個狀態，光是存就不可能。
2. **學習上的維度詛咒**：要更新查表的某個項目，就得**造訪**它。

**解法** [▶ 48:35](https://youtu.be/zanXSI7zSws?t=2915)：用參數化函數近似值函數：

$$V_\theta(x)\approx V^\pi(x),\qquad Q_\theta(x,u)\approx Q^\pi(x,u)$$

**好處** [▶ 49:11](https://youtu.be/zanXSI7zSws?t=2951)：

1. **壓縮**記憶體：只存參數 $\theta$。
2. **泛化**：希望能跨狀態泛化。例：格子世界裡，要估目標旁邊那格的值，表格法必須造訪它；有好的表示時，知道目標的事也能幫你估附近的值。

### 5.2 三種架構

[▶ 50:45](https://youtu.be/zanXSI7zSws?t=3045)（把函數近似器當成黑盒，參數 $\theta$）：

| 架構 | 輸入 | 輸出 |
|---|---|---|
| 1 | 狀態 $x$ | $V_\theta(x)$ |
| 2 | 狀態 $x$ 和控制 $u$ | 一個值 $Q_\theta(x,u)$ |
| 3 | 狀態 $x$ | **每個控制一個輸出**：$\left(Q_\theta(x,u_1),\dots,Q_\theta(x,u_n)\right)$ |

**架構 3 為什麼有用？** 【課堂討論】[▶ 52:19](https://youtu.be/zanXSI7zSws?t=3139)

- 學生 1 提到連續動作。講者：連續動作空間要做這個需要離散化，不建議；但有點對。
- 學生 2 提到多個 Q 函數。講者：大概不是。
- 學生 3：只要探一個狀態，就能對所有輸出的 Q 取 argmax？講者：對！
- 解釋 [▶ 54:22](https://youtu.be/zanXSI7zSws?t=3262)：貪婪策略是 $\arg\max_uQ$。有函數近似後這變成最佳化問題（以前只是查表）。架構 2 要呼叫 $n$ 次（$n$ 個動作）；架構 3 **呼叫一次**就拿到所有動作的值，又變回在有限元素裡查找。

**黑盒裡面** [▶ 55:23](https://youtu.be/zanXSI7zSws?t=3323)：可以很簡單（線性模型），也可以很複雜（很深的神經網路），「創意為王」，高層理解不變。

### 5.3 用 MC／TD 目標做迴歸

[▶ 56:24](https://youtu.be/zanXSI7zSws?t=3384) 要學參數 $\theta$，最小化估計值和真值的誤差（迴歸觀點）：

$$J(\theta)=\mathbb E_\pi\left[\left(V^\pi(x)-V_\theta(x)\right)^2\right]$$

**梯度下降** [▶ 57:28](https://youtu.be/zanXSI7zSws?t=3448)：

$$\Delta\theta=-\frac12\alpha\nabla_\theta J(\theta)=\alpha\,\mathbb E_\pi\left[\left(V^\pi(x)-V_\theta(x)\right)\nabla_\theta V_\theta(x)\right]$$

隨機梯度下降（用一個樣本）：

$$\Delta\theta=\alpha\left(V^\pi(x)-V_\theta(x)\right)\nabla_\theta V_\theta(x)$$

> 以上的推導細節講者說「不太有啟發性」、建議自己推；式子是依標準形式寫出的。

**雞生蛋問題** [▶ 58:31](https://youtu.be/zanXSI7zSws?t=3511)：要最小化跟**真值** $V^\pi$ 的誤差，但沒有真值。→ 用 MC 或 TD 的目標**代替**：

| | 迴歸目標 | 更新 |
|---|---|---|
| MC | 回報 $G_t$ | $\Delta\theta=\alpha\left(G_t-V_\theta(x_t)\right)\nabla_\theta V_\theta(x_t)$ |
| TD(0) | TD 目標 $r_t+\gamma V_\theta(x_{t+1})$ | $\Delta\theta=\alpha\left(r_t+\gamma V_\theta(x_{t+1})-V_\theta(x_t)\right)\nabla_\theta V_\theta(x_t)$ |

**對照** [▶ 60:07](https://youtu.be/zanXSI7zSws?t=3607)：

- 表格法：用 $G_t$ 或 TD 目標**更新查表中的單一項目**。
- 函數近似：用同樣的量**定義迴歸問題的輸入輸出配對**，據此更新參數 $\theta$。

【Q&A】[▶ 61:16](https://youtu.be/zanXSI7zSws?t=3676) 學生問（字幕不清，大意是「目標本身會隨著學習改變」）。答：很好的直覺——目標的品質隨時間演化。這正指向讓**深度 RL** 真正能用的關鍵工程突破之一：**穩定學習**。之後兩頁會講。

### 5.4 Fitted Q-iteration

[▶ 62:23](https://youtu.be/zanXSI7zSws?t=3743) 對 $Q$ 一樣：最小化 $Q_\theta$ 和真 $Q$ 的誤差；真 $Q$ 看不到，用 MC 或 TD 定義目標。用 TD 目標時，文獻叫 **fitted Q-iteration**（擬合 Q 迭代）。

**放進 GPI** [▶ 63:27](https://youtu.be/zanXSI7zSws?t=3807)：

- 評估：跟環境互動、收集資料，擬合最能估計 TD 目標的 $Q_\theta$。
- 改進：用更新後的 $Q_\theta$ 定義 ε-貪婪策略。

**放進 RL 骨架** [▶ 64:33](https://youtu.be/zanXSI7zSws?t=3873)：

```
1. 產生樣本：跑策略，收集 (x_t, u_t, r_t, x_{t+1})
2. 估回報：y_t = r_t + γ max_u' Q_θ(x_{t+1}, u')；擬合 Q_θ ≈ y
3. 改進策略：π(x) = argmax_u Q_θ(x,u)（加上 ε-貪婪探索）
```

【口頭】[▶ 64:01](https://youtu.be/zanXSI7zSws?t=3841) 希望透過反覆看類似版本的演算法，你開始看出：不同的 RL 演算法都是圍繞 MC 和 TD 的不同實例，交換或混合各種元素。

【課本補充】課本 §18.5.1 也介紹 Fitted Q-Learning：用 Q-learning 的 TD 目標更新函數近似器的參數；並說如果近似器能成功泛化，就不用造訪每個狀態-動作對。課本總結：基於值的方法建立在一小組核心概念上，主要差別在用什麼更新目標、什麼函數近似器、什麼行為策略。

---

## 6. 深度 Q 網路（DQN）

### 6.1 架構

[▶ 65:38](https://youtu.be/zanXSI7zSws?t=3938) 把今天的想法用**深度神經網路**實作。

**深度 Q 網路**（Deep Q-Networks，DQN），講者說大約 2014 年的突破性結果：

- 目標：學會最佳地玩 **Atari** 系列的各種遊戲。
- 有趣的地方：用深度神經網路（當時是**卷積神經網路**）**直接從影像**學控制——深度學習和 RL 結合的開端。
- 架構 [▶ 66:43](https://youtu.be/zanXSI7zSws?t=4003)：原始影像 → 多層 CNN → **每個可能動作一個 Q 值輸出**。影像是狀態 $x$ 的代理（觀測）。這就是第 5.2 節的**架構 3**。

> 原始 DQN 論文一般記為 Mnih 等（2013 年 arXiv、2015 年 Nature），講者說「約 2014」。

### 6.2 兩個穩定技巧：經驗回放、固定目標

[▶ 68:22](https://youtu.be/zanXSI7zSws?t=4102) 對成功極其重要的兩個技巧，解決兩個問題：

| 問題 | 說明 |
|---|---|
| **1. 樣本高度相關** [▶ 68:55](https://youtu.be/zanXSI7zSws?t=4135) | 函數近似時內迴圈是 Q 的迴歸。agent 主動和環境互動，同一段展開中相鄰的樣本**高度相關** → 對迴歸／監督式學習很糟（統計學習理論假設 i.i.d.） |
| **2. 目標會動** [▶ 69:57](https://youtu.be/zanXSI7zSws?t=4197) | 迴歸的目標 $r+\gamma\max Q_\theta$ 本身依賴 $\theta$；更新 $\theta$ 時目標也跟著變 → 不穩定 |

**DQN 學習迴圈** [▶ 70:31](https://youtu.be/zanXSI7zSws?t=4231)：

1. 在 $x_t$ 依 ε-貪婪選 $u_t$（一開始可能是隨機初始化的網路）。
2. 把轉移 $(x_t,u_t,r_t,x_{t+1})$ 存進**回放記憶體** $\mathcal D$。

**技巧 1：經驗回放**（experience replay）[▶ 71:03](https://youtu.be/zanXSI7zSws?t=4263)

- 「其實很簡單」：既然問題是轉移彼此高度相關，就把它們存進**緩衝區**，訓練時**從緩衝區隨機抽**，而不是只用最近的轉移。
- 緩衝區越大，抽出來的轉移越**去相關**。
- 圖解 [▶ 71:33](https://youtu.be/zanXSI7zSws?t=4293)：一條展開依序給出 $(x_t,u_t,r_t,x_{t+1})$、$(x_{t+1},u_{t+1},r_{t+1},x_{t+2})$……如果依序線上使用，彼此高度相關；存進一個大的轉移資料集再抽樣，就去相關了。
- （也就是離策略學習：重用舊策略產生的資料。）

**技巧 2：固定 Q 目標**（fixed Q-targets）／**目標網路** [▶ 73:08](https://youtu.be/zanXSI7zSws?t=4388)

- 用同一個值函數網路的**兩份**參數：$Q_\theta$ 和 $Q_\phi$。
- $\theta$：一直在更新的那份。$\phi$：$\theta$ 的**延遲版本**，用來算目標：
$$y_t=r_t+\gamma\max_{u'}Q_\phi(x_{t+1},u')$$
- 時間軸 [▶ 74:13](https://youtu.be/zanXSI7zSws?t=4453)：
  1. 兩份初始化成一樣。
  2. 一段時間內更新 $\theta$，**$\phi$ 固定**。$\phi$ 一開始可能很爛，但它在時間上**一致**，目標就穩定了。
  3. 以固定頻率把 $\phi$ 更新成最新的 $\theta$。
  4. 重複：現在朝稍微好一點的目標網路更新 $\theta$……
- **改進版** [▶ 75:44](https://youtu.be/zanXSI7zSws?t=4544)：上面那種硬複製可能讓 $\phi$ **跳太大**。現在最流行的是 **Polyak 平均**：$\phi$ 是過去 $\theta$ 的**移動平均**，不是一步一步硬跳。

> 以下**不是逐字稿內容**：Polyak 平均通常寫成 $\phi\leftarrow\tau\theta+(1-\tau)\phi$，$\tau$ 很小（例如 0.005）。

【口頭】[▶ 76:52](https://youtu.be/zanXSI7zSws?t=4612) 這兩個貢獻基本上是讓深度 RL 在實務上能用的關鍵。

**下週**：策略最佳化（也是無模型）；最後一堂：基於模型的 RL。

---

## 7. 演算法整理

### SARSA（同策略 TD 控制）

**在解什麼**：表格 MDP，不知道動態，學最佳（ε-貪婪）策略。

```
初始化 Q；x ← 起點；u ← ε-greedy(Q, x)
每一步：
    執行 u → r, x'
    u' ← ε-greedy(Q, x')
    Q(x,u) ← Q(x,u) + α [ r + γ Q(x',u') − Q(x,u) ]
    x ← x'；u ← u'
```

**什麼時候會失敗**：$\varepsilon$ 固定 → 收斂到「最佳的 ε-貪婪策略」而不是最佳策略（懸崖例子）；狀態太多存不下。

### Q-learning（離策略 TD 控制）

```
初始化 Q；x ← 起點
每一步：
    u ← ε-greedy(Q, x)        （行為策略）
    執行 u → r, x'
    Q(x,u) ← Q(x,u) + α [ r + γ max_u' Q(x',u') − Q(x,u) ]   （目標策略：貪婪）
    x ← x'
```

**什麼時候會失敗**：訓練時用 ε-貪婪執行，可能比 SARSA 更常踩到危險（懸崖）；狀態太多存不下。

### DQN

**在解什麼**：大狀態空間（例如影像），離散動作。

```
初始化 Q_θ，目標網路 φ ← θ，回放緩衝 D
每一步：
    u ← ε-greedy(Q_θ, x)；執行 → r, x'；存 (x,u,r,x') 進 D
    從 D 隨機抽一批 (x_i,u_i,r_i,x_i')
    y_i ← r_i + γ max_u' Q_φ(x_i', u')（終止時 y_i ← r_i）
    θ ← θ − α ∇_θ Σ_i (y_i − Q_θ(x_i,u_i))²
    每 C 步 φ ← θ（或每步 φ ← τθ + (1−τ)φ）
```

**什麼時候會失敗**：沒有經驗回放 → 樣本相關、不穩定；沒有目標網路 → 目標一直動、發散；連續動作空間時 $\max_{u'}$ 不好算（架構 3 需要離散動作）。

---

## 8. 一頁速查表

### 更新式

| 演算法 | TD 目標 | 類型 |
|---|---|---|
| SARSA | $r_t+\gamma Q(x_{t+1},u_{t+1})$，$u_{t+1}\sim\varepsilon$-貪婪 | 同策略 |
| Q-learning | $r_t+\gamma\max_{u'}Q(x_{t+1},u')$ | 離策略 |
| 函數近似（TD） | $\Delta\theta=\alpha\left(r+\gamma V_\theta(x')-V_\theta(x)\right)\nabla_\theta V_\theta(x)$ | — |
| 函數近似（MC） | $\Delta\theta=\alpha\left(G_t-V_\theta(x)\right)\nabla_\theta V_\theta(x)$ | — |
| DQN | $r+\gamma\max_{u'}Q_\phi(x',u')$（目標網路） | 離策略 |

### 同策略 vs 離策略

| | 同策略 | 離策略 |
|---|---|---|
| 學的策略 | 拿來互動的那個 | 可以不同（目標 $\pi$ vs 行為 $\mu$） |
| 例 | SARSA | Q-learning、DQN |
| 好處 | 簡單、穩定 | 重用舊資料、從他人資料學、解耦探索與利用 |

### 懸崖行走

SARSA → 安全路線（最佳 ε-貪婪策略），訓練分數高；Q-learning → 最佳路線（貼懸崖），訓練時偶爾掉下去、分數低。

### 函數近似

- 為什麼：記憶體、泛化。
- 架構：$V(x)$／$Q(x,u)$／$x\mapsto$ 所有動作的 $Q$（一次呼叫就能 argmax）。
- 迴歸目標：MC 的 $G_t$ 或 TD 目標。

### DQN 兩技巧

| 技巧 | 解決 |
|---|---|
| 經驗回放 | 樣本相關（從大緩衝區隨機抽） |
| 目標網路（硬複製或 Polyak 平均） | 目標會動 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 連續動作時 $\max Q$ 難算 | 第 18 集策略最佳化（直接參數化策略） |
| 值函數近似 + 策略 | 第 18 集 actor-critic |
| 離策略、回放緩衝 | 第 18 集（同策略 vs 離策略的策略梯度，待確認） |
| 學動態模型取代環境互動 | 第 19 集基於模型 RL |

---

## 附：本集一句話總結

> **把 MC 控制裡的 MC 換成 TD 就得到 SARSA（用 $Q(x',u')$ 自舉，同策略，學到最佳的 ε-貪婪策略）；讓目標策略變成貪婪、行為策略保持 ε-貪婪，TD 目標變成 $r+\gamma\max_{u'}Q(x',u')$，就是離策略的 Q-learning（學到真正的最佳策略，懸崖例子說明兩者差別）。狀態空間太大時用參數化的 $Q_\theta$，把 MC 或 TD 目標當迴歸標籤（fitted Q-iteration）；DQN 再加上經驗回放（去相關）和目標網路（穩定移動的目標），讓深度 RL 真正能用。**

---

## ⚠️ 待確認清單

1. 上課日期待補。
2. 講者身分：本集沒有自我介紹，推測是 Daniele Gammelli。
3. [▶ 61:16](https://youtu.be/zanXSI7zSws?t=3676) 學生問題字幕聽不清，筆記依講者回答推測問題內容。

---

*筆記依據「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 17 錄影逐字稿（人工字幕，1:17:40）與《Principles of Robot Autonomy》§18.4–18.5.1 整理。*
