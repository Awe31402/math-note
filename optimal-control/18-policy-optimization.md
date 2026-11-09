---
course: Stanford AA203 Optimal and Learning-Based Control（2026 春）
episode: 18
lecture: Lecture 18
date: 待補（第 10 週週一）
video: https://youtu.be/a1g9U_5zO54
notes: 《Principles of Robot Autonomy》§18.5.2（書頁 478–483，PDF 頁 480–485）：策略梯度、REINFORCE、actor-critic
---

# 第 18 集 · Lecture 18：策略最佳化（RL Policy Optimization） [▶ 影片](https://youtu.be/a1g9U_5zO54)

← 上一集：[17-value-based-rl](17-value-based-rl.md) ｜ [總目錄](README.md) ｜ 下一集：[19-model-based-rl](19-model-based-rl.md) →

> **課程**：Stanford AA203 Optimal and Learning-Based Control，2026 春 — 第 18 集
> **講者**：待確認（本集沒有自我介紹；推測同為 Daniele Gammelli）
> **來源**：YouTube 錄影逐字稿（1:20:18，上傳者提供的人工字幕）＋《Principles of Robot Autonomy》§18.5.2
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
- [1. 把 RL 寫成對 θ 的最佳化](#1-把-rl-寫成對-θ-的最佳化)
- [2. 推導策略梯度](#2-推導策略梯度)
  - [2.1 對數導數技巧](#21-對數導數技巧)
  - [2.2 未知的動態消失了](#22-未知的動態消失了)
  - [2.3 用樣本估計](#23-用樣本估計)
- [3. REINFORCE](#3-reinforce)
- [4. 直覺：加權的最大概似](#4-直覺加權的最大概似)
- [5. 策略梯度的高變異數](#5-策略梯度的高變異數)
  - [5.1 為什麼會高變異](#51-為什麼會高變異)
  - [5.2 技巧一：因果性（剩餘獎勵）](#52-技巧一因果性剩餘獎勵)
  - [5.3 技巧二：基準線](#53-技巧二基準線)
- [6. 同策略、優缺點](#6-同策略優缺點)
- [7. Actor-critic](#7-actor-critic)
  - [7.1 用評論家估剩餘獎勵](#71-用評論家估剩餘獎勵)
  - [7.2 加上基準線 → 優勢函數](#72-加上基準線--優勢函數)
  - [7.3 A2C](#73-a2c)
  - [7.4 怎麼擬合評論家](#74-怎麼擬合評論家)
- [8. 例子：AlphaGo](#8-例子alphago)
- [9. 演算法整理](#9-演算法整理)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:06](https://youtu.be/a1g9U_5zO54?t=6) 學期最後一週。過去幾週：MC、TD、基於值的方法。今天：無模型 RL 的**第二大家族**——**策略最佳化**。

| | 基於值 | 策略最佳化 |
|---|---|---|
| 策略 | **隱含**：由值函數定義（$\arg\max Q$） | **明確**：參數化策略 $\pi_\theta$ |
| 做什麼 | 對值函數做不動點迭代 | 調參數 $\theta$，**直接最大化** RL 目標 |

今天：

1. 定義**策略梯度** → 第一個演算法 **REINFORCE**。
2. 策略梯度估計量的**變異數**。
3. **Actor-critic** 方法（非常流行）。
4. 近期的演算法和應用（AlphaGo）。

| 主題 | 課本 |
|---|---|
| 策略梯度推導、REINFORCE | §18.5.2 |
| 剩餘獎勵、基準線 | §18.5.2 |
| Actor-critic、優勢函數 | §18.5.2 |
| AlphaGo 論文導讀 | 課本沒有 |

---

## 1. 把 RL 寫成對 θ 的最佳化

[▶ 02:09](https://youtu.be/a1g9U_5zO54?t=129) 回顧軌跡分布（三個隨機來源：初始狀態、策略、轉移）：

$$p_\theta(\tau)=p(x_1)\prod_{t=1}^{T}\pi_\theta(u_t\mid x_t)\,p(x_{t+1}\mid x_t,u_t)$$

（$p(x_1)$ 可以想成 gym 環境的 `.reset()`。）

**RL 目標** [▶ 04:12](https://youtu.be/a1g9U_5zO54?t=252)：策略參數化為 $\pi_\theta$，初始分布和轉移不直接依賴 $\theta$，但策略會影響軌跡的演化：

$$\theta^*=\arg\max_\theta J(\theta),\qquad J(\theta)=\mathbb E_{\tau\sim p_\theta(\tau)}\left[\sum_tr(x_t,u_t)\right]$$

（為了記號簡單，假設**不折扣**；有折扣也一樣成立。）

**怎麼解** [▶ 05:44](https://youtu.be/a1g9U_5zO54?t=344)：基於值的方法是間接地解同一個問題（對 Q 和 V 做不動點迭代，理論保證收斂到最佳）。現在要**明確地**解這個最佳化問題——**梯度上升**：估出 $\nabla_\theta J$，在參數空間沿梯度方向走。「在 RL 目標上爬山。」

**第一個問題** [▶ 07:16](https://youtu.be/a1g9U_5zO54?t=436)：目標本身就不簡單——期望是對軌跡分布取的，而我們**不知道轉移動態**（這正是重點）。

解法：照前幾週的老招——**取樣**。讓策略跑 $N$ 次，取經驗平均：

$$J(\theta)\approx\frac1N\sum_{i=1}^N\sum_tr(x_{i,t},u_{i,t})$$

---

## 2. 推導策略梯度

[▶ 09:22](https://youtu.be/a1g9U_5zO54?t=562) 記 $r(\tau)=\sum_{t=1}^Tr(x_t,u_t)$（一條軌跡的獎勵總和）。由期望的定義：

$$J(\theta)=\mathbb E_{\tau\sim p_\theta}[r(\tau)]=\int p_\theta(\tau)\,r(\tau)\,d\tau$$

$$\nabla_\theta J(\theta)=\int\nabla_\theta p_\theta(\tau)\,r(\tau)\,d\tau$$

**問題** [▶ 10:58](https://youtu.be/a1g9U_5zO54?t=658)：這樣寫不能用——梯度透過 $p_\theta(\tau)$ 依賴**未知的動態**和初始分布。接下來兩頁就是把它「揉」成可以計算的形式。

### 2.1 對數導數技巧

[▶ 11:29](https://youtu.be/a1g9U_5zO54?t=689) 恆等式：

$$p_\theta(\tau)\nabla_\theta\log p_\theta(\tau)=p_\theta(\tau)\frac{\nabla_\theta p_\theta(\tau)}{p_\theta(\tau)}=\nabla_\theta p_\theta(\tau)$$

（$\log$ 的導數 = 函數的導數 ÷ 函數本身，兩個 $p$ 抵銷。）

代進去 [▶ 12:32](https://youtu.be/a1g9U_5zO54?t=752)：

$$\nabla_\theta J(\theta)=\int p_\theta(\tau)\nabla_\theta\log p_\theta(\tau)\,r(\tau)\,d\tau=\mathbb E_{\tau\sim p_\theta}\left[\nabla_\theta\log p_\theta(\tau)\,r(\tau)\right]$$

【口頭】[▶ 13:03](https://youtu.be/a1g9U_5zO54?t=783) 還不能用（還有 $\nabla\log p_\theta(\tau)$），但方向對了：只要是「對軌跡分布的期望」，就能用跟環境互動取樣來近似。

### 2.2 未知的動態消失了

[▶ 13:34](https://youtu.be/a1g9U_5zO54?t=814) 對軌跡分布取 log，乘積變成和：

$$\log p_\theta(\tau)=\log p(x_1)+\sum_{t=1}^T\left[\log\pi_\theta(u_t\mid x_t)+\log p(x_{t+1}\mid x_t,u_t)\right]$$

對 $\theta$ 微分 [▶ 15:11](https://youtu.be/a1g9U_5zO54?t=911)：第一項和第三項**不依賴 $\theta$**，梯度是 0！只剩策略那一項——而策略是**我們自己定義的**，可以算：

$$\boxed{\nabla_\theta J(\theta)=\mathbb E_{\tau\sim p_\theta}\left[\left(\sum_{t=1}^T\nabla_\theta\log\pi_\theta(u_t\mid x_t)\right)\left(\sum_{t=1}^Tr(x_t,u_t)\right)\right]}$$

**例** [▶ 15:44](https://youtu.be/a1g9U_5zO54?t=944)：一維連續動作，策略是高斯 $\pi_\theta(u_t\mid x_t)=\mathcal N(\mu_\theta,\sigma_\theta^2)$，$\theta$ 代表均值和變異數 → $\log\pi_\theta$ 完全可以算。

期望裡面每一樣都**已知**：獎勵總和（觀察到的）和 $\log\pi$ 的梯度（自己定義的）。

### 2.3 用樣本估計

[▶ 17:20](https://youtu.be/a1g9U_5zO54?t=1040) 同一招：跑 $N$ 條軌跡，取經驗平均：

$$\nabla_\theta J(\theta)\approx\frac1N\sum_{i=1}^N\left(\sum_{t=1}^T\nabla_\theta\log\pi_\theta(u_{i,t}\mid x_{i,t})\right)\left(\sum_{t=1}^Tr(x_{i,t},u_{i,t})\right)$$

---

## 3. REINFORCE

[▶ 18:21](https://youtu.be/a1g9U_5zO54?t=1101) 上面的推導直接給出第一個策略最佳化演算法 **REINFORCE**：

```
重複：
    1. 讓 π_θ 跟環境互動，抽 N 條軌跡 {τ_i}
    2. ∇_θ J ≈ (1/N) Σ_i (Σ_t ∇_θ log π_θ(u_{i,t}|x_{i,t})) (Σ_t r(x_{i,t},u_{i,t}))
    3. θ ← θ + α ∇_θ J
```

**放進 RL 骨架** [▶ 19:22](https://youtu.be/a1g9U_5zO54?t=1162)：

| 步驟 | REINFORCE |
|---|---|
| 1. 產生樣本 | 跑策略 |
| 2. 估回報 | **蒙地卡羅**：跑完回合，加總所有獎勵 |
| 3. 改進策略 | 參數空間的梯度步 |

這只是內迴圈的一步；外面還有一層迴圈：策略改進後收集新經驗、重新估梯度……

> ⚠️ 逐字稿缺字：字幕把 REINFORCE 寫成「reinforced」。

---

## 4. 直覺：加權的最大概似

[▶ 20:55](https://youtu.be/a1g9U_5zO54?t=1255) $\log\pi$ 是策略給動作的對數機率（連續或離散都適用：離散時策略是有限動作上的類別分布）。

**跟行為複製比較** [▶ 22:03](https://youtu.be/a1g9U_5zO54?t=1323)：

| | 梯度 |
|---|---|
| 最大概似（行為複製） | $\frac1N\sum_i\sum_t\nabla_\theta\log\pi_\theta(u_{i,t}\mid x_{i,t})$ |
| 策略梯度 | $\frac1N\sum_i\left(\sum_t\nabla_\theta\log\pi_\theta(u_{i,t}\mid x_{i,t})\right)\,r(\tau_i)$ |

策略梯度 = **以軌跡獎勵加權的**最大概似梯度。

- 行為複製：沿梯度走 = 提高資料集中**所有**動作的機率。
- 策略梯度：依**表現**提高動作機率——獎勵高的軌跡裡的動作被提高得更多。

**重點** [▶ 24:37](https://youtu.be/a1g9U_5zO54?t=1477)：沿策略梯度走，就是改參數讓**高獎勵的軌跡更可能**、低獎勵的更不可能。講者畫圖：軌跡的線寬代表策略給它的機率質量；希望好軌跡變粗、壞軌跡變細。策略梯度正是把「試誤學習」形式化：試各種策略，透過參數更新讓有效的更可能、無效的更不可能。

【Q&A】[▶ 25:39](https://youtu.be/a1g9U_5zO54?t=1539) 學生問：模仿學習用不了這個，是因為沒有明確的獎勵嗎？答：某種程度是。你也可以自己建一個獎勵去加權行為複製的損失——行為複製那堂最後講的「用監督式學習做 RL」就是這樣（用獎勵過濾示範等）。

【口頭】[▶ 26:42](https://youtu.be/a1g9U_5zO54?t=1602) 這大概是本堂**最基本**的想法。

---

## 5. 策略梯度的高變異數

[▶ 27:13](https://youtu.be/a1g9U_5zO54?t=1633) 直覺上很合理，但有明顯限制：這個梯度估計量的**變異數極高** → 學習訊號極不穩定。

### 5.1 為什麼會高變異

[▶ 28:17](https://youtu.be/a1g9U_5zO54?t=1697) 講者畫圖：橫軸是軌跡空間，一個高斯代表策略誘導的軌跡分布。

1. 跑出三條軌跡，回報兩正一負。策略梯度會讓正的那些更可能、負的那條更不可能——正如預期。
2. 把三個回報**都加上同一個正常數**（相對差距不變，只是絕對值不同）[▶ 29:21](https://youtu.be/a1g9U_5zO54?t=1761)。
3. 現在三個都是正的：策略梯度雖然還是比較偏好好的那些，但**仍然會試著涵蓋**原本負的那條 → 結果更分散。

【口頭】極端的例子，但重點是：用**樣本**估真正的梯度，依抽到的樣本不同，梯度可以差很多——這就是高變異數。

**後果** [▶ 30:55](https://youtu.be/a1g9U_5zO54?t=1855)：表現更差、收斂更慢、訓練曲線更不穩定。策略最佳化的研究很大一部分就是在找**降低變異數**的方法；不同演算法很大程度是策略梯度的不同實作。

【Q&A】[▶ 31:27](https://youtu.be/a1g9U_5zO54?t=1887) 學生問：獎勵可以離散或連續（例如到目標得 5 分 vs 依離目標遠近連續給分），連續的獎勵會降低變異數嗎？答：一般來說，獎勵越**密集**（dense），越有利於把學習傳遍整個演算法——不只是變異數，也有利於**功勞分配**（讓學習在整條軌跡上更細緻）。直覺正確。

### 5.2 技巧一：因果性（剩餘獎勵）

[▶ 32:59](https://youtu.be/a1g9U_5zO54?t=1979) 與其說是策略，不如說是個簡單技巧。

- 現在的式子：時刻 $t'$ 的 $\log\pi$ 被**整條軌跡**的獎勵總和加權——包括 $t'$ **之前**的獎勵。
- 違反直覺：時刻 $t'$ 的動作**不可能影響**之前的獎勵。這就是**因果性**（causality）。

**改成只加總之後的獎勵** [▶ 34:02](https://youtu.be/a1g9U_5zO54?t=2042)：

$$\nabla_\theta J(\theta)\approx\frac1N\sum_{i=1}^N\sum_{t=1}^T\nabla_\theta\log\pi_\theta(u_{i,t}\mid x_{i,t})\underbrace{\left(\sum_{t'=t}^Tr(x_{i,t'},u_{i,t'})\right)}_{\text{剩餘獎勵（reward-to-go）}}$$

**為什麼降低變異數** [▶ 34:36](https://youtu.be/a1g9U_5zO54?t=2076)：

- 拿掉了動作根本影響不到的項。
- 加總的獎勵項變**少**了；每個獎勵都依賴整條軌跡上的隨機元素（反覆從策略和轉移取樣），所以項越少、變異數越低。

【口頭】簡單，但確實可量測地改善。

### 5.3 技巧二：基準線

[▶ 35:44](https://youtu.be/a1g9U_5zO54?t=2144) 對策略最佳化非常重要。

- 策略梯度只有在回報**置中**時才會「做對的事」（5.1 的反例：相對差距一樣，但回報沒置中，梯度就做了不想要的事）。
- 想要：比**平均好**的行為機率提高，比平均差的降低。
- **基準線**（baseline）$b$：從回報中**減掉**的量：

$$\nabla_\theta J(\theta)\approx\frac1N\sum_{i=1}^N\nabla_\theta\log p_\theta(\tau_i)\left[r(\tau_i)-b\right]$$

**健全性檢查：還是無偏嗎？** [▶ 37:51](https://youtu.be/a1g9U_5zO54?t=2271) 推導保證無限樣本時策略梯度的期望是對的；減掉 $b$ 會改變期望嗎？——**不會**：

$$
\begin{aligned}
\mathbb E_{\tau\sim p_\theta}\left[\nabla_\theta\log p_\theta(\tau)\,b\right]&=\int p_\theta(\tau)\nabla_\theta\log p_\theta(\tau)\,b\,d\tau \\
&=\int\nabla_\theta p_\theta(\tau)\,b\,d\tau\qquad\text{（同一個恆等式，反方向用）} \\
&=b\,\nabla_\theta\int p_\theta(\tau)\,d\tau=b\,\nabla_\theta 1=0
\end{aligned}
$$

（$p_\theta$ 是合法的機率密度，積分 = 1。）

所以加了基準線，估計量**仍然無偏**——「免費」降低變異數。

**常用的選擇** [▶ 41:01](https://youtu.be/a1g9U_5zO54?t=2461)：**平均回報**

$$b=\frac1N\sum_{i=1}^Nr(\tau_i)$$

**效果** [▶ 42:02](https://youtu.be/a1g9U_5zO54?t=2522)：訓練曲線範例：就算很簡單的環境，同一個演算法只改策略梯度的式子，訓練就快很多；有些情況甚至是「收斂到好解」和「不收斂」的差別。

---

## 6. 同策略、優缺點

【課堂討論】[▶ 43:03](https://youtu.be/a1g9U_5zO54?t=2583) 講者問：這是同策略還是離策略？學生：同策略，因為是用目前策略的展開更新。講者：對。梯度的估計依賴**目前策略** $\pi_\theta$ 的展開；一更新策略，就要收集新經驗重估梯度。（有離策略的延伸，但照今天的推導是同策略。）

**優缺點** [▶ 45:40](https://youtu.be/a1g9U_5zO54?t=2740)：

| 優點 | 缺點 |
|---|---|
| **天然處理連續動作**：只要定義適當的 $\pi_\theta(u\mid x)$（例如高斯）；離散（類別分布）也一樣。基於值的方法 $\arg\max_uQ$ 在連續動作時本身就是最佳化問題 | **同策略** → **樣本效率極低**：可能要跟環境互動非常多次才收斂（相比之下 Q-learning 可以離策略） |
| **直接最佳化我們在乎的目標**（折扣獎勵和），就是在目標上做梯度上升。基於值的方法引入中間目標（Bellman 不動點），中途停下來不清楚進度如何 | 高變異數（第 5 節） |

【Q&A】[▶ 48:14](https://youtu.be/a1g9U_5zO54?t=2894) 學生問：Q-learning「中途停」是什麼意思？答：兩者都是迭代演算法——這裡是梯度上升，Q-learning 是不動點迭代（反覆強制 Bellman 最佳方程）。都可能在收斂前停下。策略最佳化在最大化一個目標，進度很清楚；Q-learning 在收斂前不太清楚怎麼評估進度。

---

## 7. Actor-critic

[▶ 50:20](https://youtu.be/a1g9U_5zO54?t=3020) 大量建立在策略梯度上，但結合**策略梯度**和**基於值**兩邊的優點。

### 7.1 用評論家估剩餘獎勵

[▶ 50:53](https://youtu.be/a1g9U_5zO54?t=3053) 剩餘獎勵 $\sum_{t'=t}^Tr_{t'}$ 正是高變異數的來源：它只是「期望剩餘獎勵」的**有限樣本**估計，是有雜訊的估計（反覆從各種雜訊來源取樣——就算做同樣的動作序列，展開也可能不同）。

**Actor-critic 的想法** [▶ 52:30](https://youtu.be/a1g9U_5zO54?t=3150)：與其用取樣估剩餘獎勵，不如**擬合一個參數化函數**去估**真正的期望**。

| 角色 | 是什麼 |
|---|---|
| **演員**（actor） | 策略 $\pi_\theta$ |
| **評論家**（critic） | 更準地估期望剩餘獎勵——也就是**值函數**（前幾週學的函數近似） |

把剩餘獎勵換成評論家的估計 [▶ 54:39](https://youtu.be/a1g9U_5zO54?t=3279)：

$$\nabla_\theta J(\theta)\approx\frac1N\sum_i\sum_t\nabla_\theta\log\pi_\theta(u_{i,t}\mid x_{i,t})\,\hat Q_\phi(x_{i,t},u_{i,t})$$

假設評論家擬合得好，就能降低策略梯度的變異數。

### 7.2 加上基準線 → 優勢函數

[▶ 55:20](https://youtu.be/a1g9U_5zO54?t=3320) 再結合基準線：要把 $\hat Q$ 置中，選**依狀態**的基準線——在策略下 $Q$ 的期望：

$$b(x_t)=\mathbb E_{u_t\sim\pi_\theta(\cdot\mid x_t)}\left[Q(x_t,u_t)\right]=V(x_t)$$

**$Q$ 的期望就是 $V$** [▶ 57:23](https://youtu.be/a1g9U_5zO54?t=3443)：

- $Q^\pi(x_t,u_t)$：在 $x_t$ **做了 $u_t$**、之後照 $\pi$ 的期望獎勵。
- $V^\pi(x_t)$：只給狀態；不知道這一步選哪個動作 → 對策略選動作的分布**平均**。
- 從 $t+1$ 起兩者都照 $\pi$ 取樣；差別只在這一步：$Q$ 多了一個資訊——**承諾**了某個動作。

【Q&A】[▶ 59:38](https://youtu.be/a1g9U_5zO54?t=3578) 學生確認：所以是對未來所有可能的動作平均？答：直覺很像。差別只在一步的推理：$t+1$ 之後兩者都對策略可能做的事取平均；$t$ 到 $t+1$ 那一步，$Q$ 指定了現在的動作，$V$ 則依策略的分布平均。

**優勢函數**（advantage function）[▶ 61:15](https://youtu.be/a1g9U_5zO54?t=3675)：

$$A^\pi(x_t,u_t)=Q^\pi(x_t,u_t)-V^\pi(x_t)$$

$$\nabla_\theta J(\theta)\approx\frac1N\sum_i\sum_t\nabla_\theta\log\pi_\theta(u_{i,t}\mid x_{i,t})\,\hat A(x_{i,t},u_{i,t})$$

意思：動作 $u_t$ 比在 $x_t$ 的**平均動作**好多少。沿這個梯度走 → 比平均好的動作機率提高、比平均差的降低。這個量太重要了，所以有自己的名字。

【Q&A】[▶ 62:47](https://youtu.be/a1g9U_5zO54?t=3767) 學生問：評論家跟演員無關，換一個演員評論家還能用？答：功能上它們是兩個參數化函數。但評論家的參數 $\phi$ 是用環境經驗擬合的，而經驗由策略決定——擬合的是**這個策略**（演員）的值函數，所以**不獨立**。

【Q&A】[▶ 63:51](https://youtu.be/a1g9U_5zO54?t=3831) 學生問「平均動作」是什麼樣子？答：策略是動作上的分布：連續時是高斯，離散時（例如四個方向）是類別分布。「平均動作」就是對這個分布取期望——這是**隨機策略**。

【Q&A】[▶ 64:53](https://youtu.be/a1g9U_5zO54?t=3893) 學生問：能用預訓練的評論家，不用從零開始嗎？答：理論上**不行**：值函數是針對某個特定策略的，這裡要的是正在學的那個策略的值函數。實務上只要它對梯度更新有用、方向一致，預訓練的評論家可能有幫助。

### 7.3 A2C

[▶ 66:26](https://youtu.be/a1g9U_5zO54?t=3986) **三者並排**：

| | 擬合 | 改進策略 |
|---|---|---|
| Fitted Q-learning | 擬合 $Q_\phi$（MC 或 TD 目標的迴歸） | 隱含：$\arg\max Q$ |
| REINFORCE | — | 策略梯度（MC 回報） |
| **Actor-critic** | 擬合 $V$、$Q$ 或 $A$（跟 fitted Q 一樣的迴歸） | **策略梯度**（用評論家） |

把不同家族的元件拼起來。

**估哪個量？** [▶ 69:03](https://youtu.be/a1g9U_5zO54?t=4143) 沒有對錯，看演算法。考量之一：問題複雜度——$V$ 只吃狀態，比較容易；$Q$ 或 $A$ 要學「狀態 + 控制」的映射。

**A2C**（advantage actor-critic）[▶ 70:05](https://youtu.be/a1g9U_5zO54?t=4205)，大概是最流行的 actor-critic 實作：

- 想用優勢 $A=Q-V$，但不想擬合 $Q$ 和 $V$ **兩個**網路。
- 技巧：$Q(x_t,u_t)\approx r(x_t,u_t)+V(x_{t+1})$，所以
$$\hat A(x_t,u_t)\approx r(x_t,u_t)+\gamma\hat V_\phi(x_{t+1})-\hat V_\phi(x_t)$$
**只要擬合 $V$**。

```
重複：
    1. 跑策略 π_θ，收集 (x_t, u_t, r_t, x_{t+1})
    2. 擬合 V_φ（MC 或 TD 目標）
    3. Â_t = r_t + γ V_φ(x_{t+1}) − V_φ(x_t)
    4. ∇_θ J ≈ Σ_t ∇_θ log π_θ(u_t|x_t) Â_t
    5. θ ← θ + α ∇_θ J
```

> ⚠️ 逐字稿缺字 [▶ 70:05](https://youtu.be/a1g9U_5zO54?t=4205)：字幕把 A2C 寫成「a to z」。

【課本補充】課本 Algorithm 18.7 是 A2C 的完整虛擬碼：演員和評論家各用一個學習率 $\alpha_\theta$、$\alpha_\phi$；評論家用 TD 目標 $y_t=r_t+\gamma V_\phi(x_{t+1})$ 更新 $\phi\leftarrow\phi-\alpha_\phi\nabla_\phi(y_t-V_\phi(x_t))^2$，優勢 $A_t=y_t-V_\phi(x_t)$。

> 以下**不是逐字稿內容**：$\hat A$ 正好就是第 16 集的 **TD 誤差** $\delta_t$。講者寫的近似式沒有 $\gamma$（本堂假設不折扣），上式加回了 $\gamma$。

### 7.4 怎麼擬合評論家

[▶ 72:19](https://youtu.be/a1g9U_5zO54?t=4339) 跟基於值方法的函數近似完全一樣：

| 方式 | 資料集 | 迴歸 |
|---|---|---|
| MC | $\{(x_{i,t},\ y_{i,t}=\sum_{t'\ge t}r_{i,t'})\}$ | $\min_\phi\sum\left\|V_\phi(x_{i,t})-y_{i,t}\right\|^2$ |
| TD | $\{(x_{i,t},\ y_{i,t}=r_{i,t}+\gamma V_\phi(x_{i,t+1}))\}$ | 同上 |

【課本補充】課本 §18.5.2 涵蓋策略梯度、REINFORCE 和 actor-critic。

---

## 8. 例子：AlphaGo

[▶ 73:28](https://youtu.be/a1g9U_5zO54?t=4408) 講者說是 RL 最大的成功之一（約 2014–2016），推薦讀論文——用今天的內容大概能看懂整篇。

- 目標：用 RL 學會下**圍棋**（維度極高的棋盤遊戲）。
- **策略網路** + **價值網路** → 用的是 **actor-critic** 方法 [▶ 74:31](https://youtu.be/a1g9U_5zO54?t=4471)：
  - 策略網路：棋盤狀態 → 下一手的分布（有限個動作）。
  - 價值網路：棋盤狀態 → 一個純量（狀態值函數）。
- **自我對弈**（self-play）[▶ 75:38](https://youtu.be/a1g9U_5zO54?t=4538)：策略跟自己或自己的舊版本在模擬環境對戰；重播對局，算策略梯度更新：

$$\Delta\theta=\frac{\alpha}{m}\sum_{i=1}^m\sum_t\nabla_\theta\log p_\theta\left(a_t^i\mid s_t^i\right)\left(z_t^i-v\left(s_t^i\right)\right)$$

  - $z$：觀察到的回報（輸贏）；$v(s)$：價值函數當**基準線**，用來**降低變異數**——論文說的就是「REINFORCE with baseline」。

【Q&A】[▶ 76:46](https://youtu.be/a1g9U_5zO54?t=4606) 學生問：獎勵訊號只在回合結束時給？答：是。

**沒講的部分** [▶ 77:18](https://youtu.be/a1g9U_5zO54?t=4638)：主要貢獻之一是**搜尋**：不是直接從類別分布抽動作，而是用那個分布引導明確的搜尋——**蒙地卡羅樹搜尋**（Monte Carlo tree search，MCTS）。但 RL 那一側的高層直覺就是今天講的。

【Q&A】[▶ 77:48](https://youtu.be/a1g9U_5zO54?t=4668) 學生問：有保證找到的策略是最好的嗎？還是只是人類打不贏？答：深度 RL **沒有任何理論**能給證明或收斂保證。他們擊敗了世界冠軍，就宣稱這是夠好的結果。

【Q&A】[▶ 78:18](https://youtu.be/a1g9U_5zO54?t=4698) 學生問：為什麼保留人類的版本？答：當時先用**行為複製**（專家示範資料集）起步，再用 RL 微調。後續的工作證明行為複製那部分反而**有害**最終表現，改成完全靠自我對弈學。

> 「後續的工作」一般指 AlphaGo Zero（2017），講者沒說名字。

【Q&A】[▶ 78:51](https://youtu.be/a1g9U_5zO54?t=4731) 學生問：每 500 次迭代更新一次對手（用目前最好的參數），怎麼避免收斂到只對某個對手有效的策略？答：要再確認論文。直覺是你希望對手的水準也越來越高；因為一直更新對手、有學習迴圈，你總會被激勵去找比舊版本更好的策略，某種意義上就是在爬山。可能他們還做了更精緻的處理。

**下次**：收尾，並開始講基於模型的 RL。

---

## 9. 演算法整理

### REINFORCE（含剩餘獎勵和基準線）

**在解什麼**：無模型 RL，直接最佳化參數化策略；連續或離散動作皆可。

```
初始化 π_θ
重複：
    跑 π_θ 抽 N 條軌跡
    對每個 i, t：G_{i,t} = Σ_{t'≥t} r_{i,t'}（剩餘獎勵）
    b = 平均回報
    ∇J ≈ (1/N) Σ_i Σ_t ∇_θ log π_θ(u_{i,t}|x_{i,t}) (G_{i,t} − b)
    θ ← θ + α ∇J
```

**什麼時候會失敗**：變異數高 → 不穩定、慢，甚至不收斂（不加基準線時尤其）；同策略 → 每次更新都要重新收集資料，樣本效率極低；需要回合結束（MC 回報）；獎勵稀疏時功勞分配難。

### A2C（advantage actor-critic）

**在解什麼**：同上，但用評論家降低變異數。

```
初始化演員 π_θ、評論家 V_φ
重複：
    跑 π_θ 收集轉移 (x_t,u_t,r_t,x_{t+1})
    擬合 V_φ：迴歸到 MC 回報或 TD 目標 r_t + γ V_φ(x_{t+1})
    Â_t = r_t + γ V_φ(x_{t+1}) − V_φ(x_t)
    θ ← θ + α Σ_t ∇_θ log π_θ(u_t|x_t) Â_t
```

**什麼時候會失敗**：評論家估不準 → 優勢有偏、梯度方向錯；評論家是針對目前策略的，策略變了要跟著更新；仍是同策略（樣本效率低）；深度 RL 沒有收斂保證。

---

## 10. 一頁速查表

### 策略梯度推導

| 步驟 | 式子 |
|---|---|
| 目標 | $J(\theta)=\mathbb E_{\tau\sim p_\theta}[r(\tau)]=\int p_\theta(\tau)r(\tau)d\tau$ |
| 對數導數技巧 | $p_\theta\nabla\log p_\theta=\nabla p_\theta$ → $\nabla J=\mathbb E[\nabla\log p_\theta(\tau)\,r(\tau)]$ |
| 動態消失 | $\nabla\log p_\theta(\tau)=\sum_t\nabla\log\pi_\theta(u_t\mid x_t)$（初始分布、轉移不含 $\theta$） |
| 結果 | $\nabla J=\mathbb E\left[\left(\sum_t\nabla\log\pi_\theta(u_t\mid x_t)\right)\left(\sum_tr_t\right)\right]$ |
| 估計 | 跑 $N$ 條軌跡取平均 |

### 直覺

策略梯度 = 以 $r(\tau)$ 加權的最大概似梯度 → 好軌跡更可能、壞軌跡更不可能。

### 降變異數

| 技巧 | 改法 | 為什麼無偏／有效 |
|---|---|---|
| 因果性 | $r(\tau)\to\sum_{t'\ge t}r_{t'}$（剩餘獎勵） | 動作影響不到過去；加總項變少 |
| 基準線 | $r\to r-b$，例 $b=$ 平均回報 | $\mathbb E[\nabla\log p_\theta\,b]=b\nabla\int p_\theta=0$ |
| 評論家 | 剩餘獎勵 → $\hat Q_\phi$ | 用擬合的期望取代單一樣本 |
| 優勢 | $\hat A=Q-V\approx r+\gamma V(x')-V(x)$ | 依狀態的基準線 $V=\mathbb E_{u\sim\pi}Q$ |

### 比較

| | 基於值（Q-learning） | 策略梯度 | Actor-critic |
|---|---|---|---|
| 策略 | 隱含 $\arg\max Q$ | 明確 $\pi_\theta$ | 明確 $\pi_\theta$ |
| 連續動作 | 難 | 容易 | 容易 |
| 目標 | 中間目標（Bellman） | 直接最佳化 $J$ | 直接最佳化 $J$ |
| 策略 | 離策略 | 同策略 | 同策略（基本形式） |
| 變異數 | — | 高 | 較低 |

### AlphaGo

策略網路 + 價值網路（actor-critic）；自我對弈；REINFORCE with baseline：$\nabla\log p_\theta(a\mid s)(z-v(s))$；加上 MCTS。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 同策略 → 樣本效率低 | 第 19 集基於模型 RL（用學到的模型提高樣本效率） |
| 骨架第 2 步「擬合模型」 | 第 19 集 |
| 策略梯度＋學到的模型 | 第 19 集（待確認） |
| 第 7–8 集的 MPC、iLQR | 第 19 集：用學到的動態做規劃（待確認） |

---

## 附：本集一句話總結

> **策略最佳化把策略寫成 $\pi_\theta$，直接對 RL 目標做梯度上升；對數導數技巧讓未知的動態從梯度中消失，得到 $\nabla J=\mathbb E\left[\sum_t\nabla\log\pi_\theta(u_t\mid x_t)\cdot\text{回報}\right]$——就是以獎勵加權的最大概似，取樣估計即 REINFORCE。它直接處理連續動作，但同策略、變異數高；用因果性（剩餘獎勵）、無偏的基準線、再用學到的評論家估 $Q$ 或優勢 $A=Q-V\approx r+\gamma V(x')-V(x)$，就得到 actor-critic（A2C），AlphaGo 正是以價值網路為基準線的這類方法。**

---

## ⚠️ 待確認清單

1. 上課日期待補（第 10 週週一）。
2. 講者身分：本集沒有自我介紹，推測是 Daniele Gammelli。

---

*筆記依據「Stanford AA203 Optimal and Learning-Based Control（2026 春）」Lecture 18 錄影逐字稿（人工字幕，1:20:18）與《Principles of Robot Autonomy》§18.5.2 整理。*
