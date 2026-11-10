---
course: Stanford AA274A Principles of Robotic Autonomy（2019 秋）
episode: 14
lecture: Lecture 14
date: 待補（週四）
video: https://youtu.be/pSBhRF6j-Zc
notes: 《Principles of Robot Autonomy》第 12 章開頭、§12.1–12.3（書頁 299–316，PDF 頁 301–318）
---

# 第 14 集 · Lecture 14：參數式濾波——卡爾曼濾波與 EKF（Parametric Filtering） [▶ 影片](https://youtu.be/pSBhRF6j-Zc)

← 上一集：[13-localization-filters](13-localization-filters.md) ｜ [總目錄](README.md) ｜ 下一集：[15-ekf-localization](15-ekf-localization.md) →

> **課程**：Stanford AA274A Principles of Robotic Autonomy I，2019 秋 — 第 14 集
> **講者**：Marco Pavone（推斷：提到自己做衛星姿態判定的卡爾曼濾波經驗）
> **來源**：YouTube 錄影逐字稿（1:17:44，Whisper `medium.en` 轉錄）＋《Principles of Robot Autonomy》第 12 章
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 待確認` 查不清楚，列在最後的清單
>
> **記號注意**：老師（照 *Probabilistic Robotics*）用 $R_t$ 表示**過程雜訊**共變異數、$Q_t$ 表示**量測雜訊**共變異數；課本第 12 章剛好相反（$Q_t$ 過程、$R_t$ 量測）。本筆記照老師的記號。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習 Bayes 濾波器的直覺](#1-複習-bayes-濾波器的直覺)
- [2. 讓 Bayes 濾波器可計算：參數式 vs. 非參數式](#2-讓-bayes-濾波器可計算參數式-vs-非參數式)
- [3. 高斯分布及其代價](#3-高斯分布及其代價)
- [4. 高斯的三個性質](#4-高斯的三個性質)
- [5. 線性高斯系統](#5-線性高斯系統)
- [6. 卡爾曼濾波器](#6-卡爾曼濾波器)
  - [6.1 演算法](#61-演算法)
  - [6.2 卡爾曼增益的直覺](#62-卡爾曼增益的直覺)
  - [6.3 推導](#63-推導)
- [7. 非線性系統與擴展卡爾曼濾波器（EKF）](#7-非線性系統與擴展卡爾曼濾波器ekf)
  - [7.1 線性化](#71-線性化)
  - [7.2 EKF 演算法](#72-ekf-演算法)
  - [7.3 EKF 什麼時候會失敗](#73-ekf-什麼時候會失敗)
- [8. 無跡卡爾曼濾波器（UKF）](#8-無跡卡爾曼濾波器ukf)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/pSBhRF6j-Zc?t=0)

繼續定位：在（目前假設已知的）地圖中決定自己的姿態。下週處理地圖未知、要同時估計的情況。

上一堂講了一般形式的 Bayes 濾波器；今天講**怎麼讓它可以計算**，特別是**參數式濾波器**：卡爾曼濾波器、擴展卡爾曼濾波器（EKF）。實作是作業 4。

| 主題 | 課本 |
|---|---|
| 參數式 vs. 非參數式 | 第 12 章開頭 |
| 高斯分布與三個性質 | §12.1 |
| 卡爾曼濾波器與推導 | §12.2 |
| EKF | §12.3.1 |
| UKF | §12.3.2（本集只提概念） |
| 直方圖濾波、粒子濾波 | §12.4（週五研究所課，不在本集） |

---

## 1. 複習 Bayes 濾波器的直覺

[▶ 01:05](https://youtu.be/pSBhRF6j-Zc?t=65)

`【口頭】` 接下來的東西都是 Bayes 濾波器的延伸，基礎不清楚後面就全都不清楚，所以再講一次直覺。

- **預測**：$\overline{\operatorname{bel}}(x_t) = \int p(x_t \mid u_t, x_{t-1})\operatorname{bel}(x_{t-1})\,dx_{t-1}$——看所有可能抵達 $x_t$ 的方式，各自用「在那個 $x_{t-1}$ 的機率」和「從那裡用 $u_t$ 到 $x_t$ 的機率」加權，再加總（互斥事件）。
- **修正**：$\operatorname{bel}(x_t) = \eta\,p(z_t \mid x_t)\overline{\operatorname{bel}}(x_t)$——相容性檢查。例：量測前在某處的機率 0.8，但收到的量測和「在那裡」完全不相容，就把機率大幅調低；很相容就調高。

- `【Q&A】` [▶ 05:30](https://youtu.be/pSBhRF6j-Zc?t=330)（問 $p(z_t \mid x_t) = 0$ 時的意義）→ 如果假設在 $x_t$ 而量測和它不相容，這資訊其實很有用：確定不在 $x_t$。延伸：**主動估計（active estimation）**——算控制時不只為了完成任務，也盡量**消除**位置或地圖的歧義，刻意安排運動和量測來降低濾波器的不確定性。例：在森林迷路時，往能看到信標或燈塔的地方走；被動的話就只是一直朝目標走，不確定性會變大。

**離散版**（[▶ 07:28](https://youtu.be/pSBhRF6j-Zc?t=448)）：狀態只取有限 $M$ 個值時，結構一樣，積分換成加總，直覺更清楚：$\bar p_{k,t} = \sum_i p(x_t = k \mid u_t, x_{t-1} = i)\,p_{i,t-1}$。`【口頭】` 對 Bayes 濾波器有疑問，就看離散版，自己手算幾個例子。

**為什麼一般形式難用**（[▶ 08:59](https://youtu.be/pSBhRF6j-Zc?t=539)）：

1. 「對每個 $x_t$」——連續空間不可能列舉所有狀態。
2. 就算能，也要算**多維積分**（狀態有位置、朝向、速度……），一般算不出來。

---

## 2. 讓 Bayes 濾波器可計算：參數式 vs. 非參數式

[▶ 10:47](https://youtu.be/pSBhRF6j-Zc?t=647)

兩種方法，都巧妙利用**結構**和／或**近似**：

| | 參數式（parametric） | 非參數式（non-parametric） |
|---|---|---|
| 做法 | 強迫信念屬於某個參數化的分布族，例如**高斯** | 不加特定結構，而是近似，例如用 **Monte Carlo 取樣**：用精心選的一組**粒子**近似密度函數，把粒子往前推 |
| 傳播的東西 | 只傳參數：高斯就是**平均和變異數** | 一堆粒子 |
| 例子 | 卡爾曼濾波器、EKF | 直方圖濾波器、粒子濾波器 |
| 本課 | 今天 | 週五（研究所） |

- `【課堂討論】` [▶ 11:41](https://youtu.be/pSBhRF6j-Zc?t=701) 高斯分布由幾個參數決定？→ 平均和標準差（多維：平均向量和共變異數矩陣）。所以不用往前傳整個密度函數，只傳這兩個量——巨大的簡化。

---

## 3. 高斯分布及其代價

[▶ 14:10](https://youtu.be/pSBhRF6j-Zc?t=850)

**一維高斯**：

$$
p(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left( -\frac12\frac{(x - \mu)^2}{\sigma^2} \right), \qquad X \sim \mathcal{N}(\mu, \sigma^2)
$$

$\mu$ 是期望值，$\sigma^2$ 是變異數。鐘形；$\sigma$ 越大越胖。**支撐集無限**：從 $-\infty$ 到 $+\infty$ 每個值的機率密度都非零（離平均很遠時極小但非零）。常用：落在 $\pm 1\sigma$ 的機率約 68%、$\pm 2\sigma$ 約 95%。

**多維高斯**（[▶ 20:12](https://youtu.be/pSBhRF6j-Zc?t=1212)）：狀態是多維的，所以需要多維版本。變異數換成**共變異數矩陣** $\Sigma$，平均換成**平均向量** $\mu$：

$$
p(x) = \frac{1}{\sqrt{\det(2\pi\Sigma)}}\exp\left( -\frac12(x - \mu)^\top\Sigma^{-1}(x - \mu) \right)
$$

二維時像一個鐘形的山，等高線是**橢圓**。

**用高斯當信念的代價**（[▶ 16:47](https://youtu.be/pSBhRF6j-Zc?t=1007)）：

1. **單峰**：只追蹤**一個假設**（一個峰）。真實信念常是多峰的（被丟到 Stanford 校園：這間教室機率高、另一間像的也高、花園很低）。用一個高斯近似雙峰分布，會把質量放在兩峰之間——很差的近似。
   - 那為什麼還用？(a) 實作非常快；(b) 若用夠好的初始估計啟動濾波器，真實分布通常會保持單峰，用單峰近似是合理的。
2. **無限支撐集**：會給「你在離地球幾光年外」一點點機率。荒謬，但機率小到不影響實際表現。

`【口頭】` 一定要清楚自己的近似帶來什麼後果；否則實作出來結果不合理時，不知道是程式有 bug 還是數學上本來就不行。

---

## 4. 高斯的三個性質

[▶ 21:24](https://youtu.be/pSBhRF6j-Zc?t=1284)

高斯完全由兩個參數決定（$\mu$ 和 $\Sigma$），計算上便宜得多。三個會一直用到的性質：

**性質 1：線性變換仍是高斯。** 若 $X \sim \mathcal{N}(\mu, \Sigma)$，$Y = AX + B$，則

$$
Y \sim \mathcal{N}\left( A\mu + B,\ A\Sigma A^\top \right)
$$

老師在黑板上推一維情況（[▶ 22:51](https://youtu.be/pSBhRF6j-Zc?t=1371)）：

- 期望值：$E[Y] = E[aX + b] = a\mu + b$（期望值是線性的）。
- 變異數：

  $$
  \operatorname{Var}(Y) = E\left[ (Y - E[Y])^2 \right] = E\left[ (aX + b - a\mu - b)^2 \right] = E\left[ a^2(X - \mu)^2 \right] = a^2 E\left[ (X - \mu)^2 \right] = a^2\sigma^2
  $$

  （$b$ 消掉；常數 $a^2$ 提到期望值外面。）一維時 $A\Sigma A^\top$ 就是 $a^2\sigma^2$。
- 證明 $Y$ 確實是高斯不難，這裡不證。

**性質 2：獨立高斯相加仍是高斯。** $X_1 \sim \mathcal{N}(\mu_1, \Sigma_1)$、$X_2 \sim \mathcal{N}(\mu_2, \Sigma_2)$ 獨立，則

$$
X_1 + X_2 \sim \mathcal{N}\left( \mu_1 + \mu_2,\ \Sigma_1 + \Sigma_2 \right)
$$

期望值相加是顯然的（和的期望值永遠是期望值的和）；有意思的是**共變異數也相加**（機率課證過，這裡當事實）。

- `【Q&A】` [▶ 26:29](https://youtu.be/pSBhRF6j-Zc?t=1589)（學生指出投影片少寫了某個條件，從上下文看應是「獨立」）→ 老師：對，很糟的錯誤，謝謝。

**性質 3：兩個高斯 PDF 相乘仍是（未正規化的）高斯 PDF。** 指數相乘還是指數，配方就得到高斯。

【課本補充】§12.1 給出相乘的結果：

$$
\Sigma = \left( \Sigma_1^{-1} + \Sigma_2^{-1} \right)^{-1}, \qquad \mu = \Sigma\left( \Sigma_1^{-1}\mu_1 + \Sigma_2^{-1}\mu_2 \right)
$$

`【口頭】` 這堂和上一堂、明天的內容取自 *Probabilistic Robotics*（Thrun、Burgard、Fox），講濾波和定位的好書。

---

## 5. 線性高斯系統

[▶ 27:48](https://youtu.be/pSBhRF6j-Zc?t=1668)

先看一個用高斯**不是近似、而是精確**的特殊設定，之後再推廣到非線性（那時高斯才是近似）。

**假設 1：線性狀態轉移。**

$$
x_t = A_t\,x_{t-1} + B_t\,u_t + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0, R_t)
$$

- $A_t$、$B_t$ 可以隨時間變，但**不依賴 $x$**：時變線性模型加隨機雜訊。
- $\varepsilon_t$：**過程擾動（process disturbance）**，反映致動器、模型、或致動器和環境互動的不確定性——下了某個控制，實際到達的狀態不一定是模型預測的。
- `【Q&A】` [▶ 29:43](https://youtu.be/pSBhRF6j-Zc?t=1783) 也假設 $R_t$ 隨時間變？→ 一般寫法允許。例：機器人先在水泥地、再到沙地，在沙上空轉時下一步的不確定性大得多。實際上大多當成不隨時間變。

**對應的轉移機率**（[▶ 30:34](https://youtu.be/pSBhRF6j-Zc?t=1834)）：給定 $x_{t-1}$ 和 $u_t$，$A_tx_{t-1} + B_tu_t$ 是常數，$x_t$ 只是 $\varepsilon_t$ 的線性變換（乘 1 再加常數）。由性質 1：

$$
p(x_t \mid u_t, x_{t-1}) = \mathcal{N}\left( x_t;\ A_tx_{t-1} + B_tu_t,\ R_t \right)
$$

**假設 2：線性量測。**

$$
z_t = C_t\,x_t + \delta_t, \qquad \delta_t \sim \mathcal{N}(0, Q_t)
\quad\Longrightarrow\quad
p(z_t \mid x_t) = \mathcal{N}\left( z_t;\ C_tx_t,\ Q_t \right)
$$

**假設 3：初始信念是高斯。** $\operatorname{bel}(x_0) = \mathcal{N}(\mu_0, \Sigma_0)$。

**重點**（[▶ 36:22](https://youtu.be/pSBhRF6j-Zc?t=2182)）：這三個假設保證**每個時刻**的信念都是高斯——不是近似。所以實作 Bayes 濾波器只要更新信念高斯的平均向量和共變異數矩陣。（要證明，見 6.3。）

`【口頭】` 另一個沒明說但關鍵的假設：過程雜訊和感測雜訊不只是高斯，還和狀態**獨立**；否則推導中某些步驟不成立。

---

## 6. 卡爾曼濾波器

### 6.1 演算法

[▶ 37:46](https://youtu.be/pSBhRF6j-Zc?t=2266)

在上述設定下實作 Bayes 濾波器，就是**卡爾曼濾波器（Kalman filter）**——最有影響力的濾波器，特別是在機器人學。1950 年代由 Rudolf Kalman 提出。

`【口頭】` 有趣的是：最初的論文被一本頂尖控制期刊**退稿**。當時有爭論：用狀態表示做控制到底好不好？主流是頻率域表示。最後發表在一本不太有名的期刊（*Journal of Basic Engineering*，「我甚至不知道它還在不在」），後來成為濾波的首選演算法。「論文被退好幾次別擔心，你和偉人同行。」

**卡爾曼濾波器**

- **在解什麼**：線性動態、線性量測、高斯雜訊、高斯初始信念下，精確地遞迴計算信念 $\mathcal{N}(\mu_t, \Sigma_t)$。
- **步驟**（輸入 $\mu_{t-1}, \Sigma_{t-1}, u_t, z_t$）：
  1. **預測**（考慮控制）：

     $$
     \bar\mu_t = A_t\mu_{t-1} + B_tu_t, \qquad \bar\Sigma_t = A_t\Sigma_{t-1}A_t^\top + R_t
     $$

  2. **卡爾曼增益**：

     $$
     K_t = \bar\Sigma_tC_t^\top\left( C_t\bar\Sigma_tC_t^\top + Q_t \right)^{-1}
     $$

  3. **修正**（考慮量測）：

     $$
     \mu_t = \bar\mu_t + K_t\left( z_t - C_t\bar\mu_t \right), \qquad \Sigma_t = \left( I - K_tC_t \right)\bar\Sigma_t
     $$

  輸出 $\mu_t, \Sigma_t$。
- **什麼時候會失敗**：
  - 動態或量測**非線性** → 嚴格說不能用（要用 EKF、UKF）。
  - 雜訊不是高斯、或和狀態相關 → 不再最佳／不再精確。
  - 真實信念**多峰**（例如全域定位、對稱環境）→ 單一高斯表示不了。
  - $R_t$、$Q_t$ 設錯 → 太相信模型或太相信感測器，估計偏掉甚至發散。

**修正步驟的解讀**（[▶ 41:48](https://youtu.be/pSBhRF6j-Zc?t=2508)）：由量測模型 $z_t = C_tx_t + \delta_t$，$\delta_t$ 平均為 0，所以

- $C_t\bar\mu_t$ = 根據目前（預測信念）對狀態的了解，**預期**會收到的量測。
- $z_t$ = **實際**收到的量測。
- $z_t - C_t\bar\mu_t$ = 兩者之差（課本叫 **innovation**，新息）。

新的平均 = 預測平均 + 增益 × 這個差。

### 6.2 卡爾曼增益的直覺

[▶ 42:56](https://youtu.be/pSBhRF6j-Zc?t=2576)

卡爾曼增益是**所有魔法發生的地方**：它權衡「多相信模型」和「多相信量測」。

- $K_t = 0$：完全丟掉量測資訊，只相信模型。
- $K_t$ 很大：丟掉模型資訊，主要依賴量測。

`【課堂討論】` 想成一維（矩陣反矩陣變成除法）：

- **$Q_t$ 很大**（感測器雜訊很大、回傳垃圾）→ 除以很大的數 → $K_t$ 很小 → 修正時基本上忽略量測。合理：感測器很爛，就靠模型。
- **$\bar\Sigma_t$ 很小**（預測信念已經很確定）→ $K_t$ 也很小：已經很確定狀態在哪，就別用有雜訊的感測器去改它。

【課本補充】§12.2.1：感測雜訊大 → $K_t$ 小、依賴預測；模型不確定性大但感測器準 → $K_t$ 大、估計被拉向量測。課本也給出數值上更穩定的 **Joseph 形式**：$\Sigma_t = (I - K_tC_t)\bar\Sigma_t(I - K_tC_t)^\top + K_tQ_tK_t^\top$（換成老師的記號）。

`【口頭】` 可以證明卡爾曼濾波器在「最小化估計的均方誤差」意義下是**最佳**的濾波器（本課不證）。

**Q&A**

- `【Q&A】` [▶ 45:51](https://youtu.be/pSBhRF6j-Zc?t=2751) 卡爾曼增益從哪來？→ 等一下推導。
- `【Q&A】` [▶ 46:10](https://youtu.be/pSBhRF6j-Zc?t=2770) $C_t$ 是把量測投影到狀態空間嗎？→ 反過來：$C_t$ 把**狀態**轉成**量測**（再加雜訊）。$C_t$ 一般不必是方陣、維度不必和 $x_t$ 一樣；原則上可以是單位矩陣，但很少見。例：量測是到某物體的**距離**，狀態是 $x, y$ 和朝向——從狀態到量測是降維。之後用光達（作業機器人上用的感測器）做定位時會更具體。

### 6.3 推導

[▶ 48:23](https://youtu.be/pSBhRF6j-Zc?t=2903)

做法：把三個假設代進已嚴格推導過的 Bayes 濾波器。用**歸納法**：假設 $t-1$ 時信念是高斯 $\mathcal{N}(\mu_{t-1}, \Sigma_{t-1})$，證明 $t$ 時也是，且參數照上面的式子更新。

**預測步驟**（[▶ 49:30](https://youtu.be/pSBhRF6j-Zc?t=2970)）：

- 正式做法：$\overline{\operatorname{bel}}(x_t) = \int p(x_t \mid u_t, x_{t-1})\operatorname{bel}(x_{t-1})\,dx_{t-1}$，兩個都是高斯；用性質 3 相乘再配方——「兩頁很無聊的代數」，不太有啟發性（`【口頭】` 「我懶得做；不信的話去讀那幾節」）。
- **更直接的路**（[▶ 51:57](https://youtu.be/pSBhRF6j-Zc?t=3117)）：$x_t = A_tx_{t-1} + (B_tu_t + \varepsilon_t)$ 是**兩個獨立隨機變數的和**：
  - $A_tx_{t-1}$：高斯的線性變換 → $\mathcal{N}(A_t\mu_{t-1},\ A_t\Sigma_{t-1}A_t^\top)$（性質 1）。
  - $B_tu_t + \varepsilon_t$：常數加高斯 → $\mathcal{N}(B_tu_t + 0,\ R_t)$（常數不影響共變異數）。
  - 相加（性質 2）：平均相加、共變異數相加：

  $$
  \bar\mu_t = A_t\mu_{t-1} + B_tu_t, \qquad \bar\Sigma_t = A_t\Sigma_{t-1}A_t^\top + R_t
  $$

  正是卡爾曼濾波器的前兩條式子。這一步需要「過程雜訊和狀態獨立」的假設。

**修正步驟**（[▶ 55:08](https://youtu.be/pSBhRF6j-Zc?t=3308)）：$\operatorname{bel}(x_t) = \eta\,p(z_t \mid x_t)\overline{\operatorname{bel}}(x_t)$，其中 $\overline{\operatorname{bel}}(x_t) = \mathcal{N}(\bar\mu_t, \bar\Sigma_t)$（剛證明的）、$p(z_t \mid x_t) = \mathcal{N}(C_tx_t, Q_t)$（假設 2）。由性質 3，相乘是高斯；配方再做「另外兩頁很無聊的代數」，就得到 $\mu_t, \Sigma_t$ 的式子。老師說這一步沒有一兩行的捷徑，當作事實。

【課本補充】§12.2.2 給出這一步的骨架：

1. 修正後的信念 $\propto \exp(-\frac12 J_t)$，其中

   $$
   J_t = (z_t - C_tx_t)^\top Q_t^{-1}(z_t - C_tx_t) + (x_t - \bar\mu_t)^\top\bar\Sigma_t^{-1}(x_t - \bar\mu_t)
   $$

2. 平均是 $J_t$ 對 $x_t$ 的一階導數為 0 的點；共變異數是二階導數的反矩陣：

   $$
   \Sigma_t^{-1} = C_t^\top Q_t^{-1}C_t + \bar\Sigma_t^{-1}, \qquad \mu_t = \bar\mu_t + \Sigma_tC_t^\top Q_t^{-1}(z_t - C_t\bar\mu_t)
   $$

3. 用**矩陣反轉引理**：$(C_t^\top Q_t^{-1}C_t + \bar\Sigma_t^{-1})^{-1} = \bar\Sigma_t - \bar\Sigma_tC_t^\top(C_t\bar\Sigma_tC_t^\top + Q_t)^{-1}C_t\bar\Sigma_t$，定義 $K_t = \bar\Sigma_tC_t^\top(C_t\bar\Sigma_tC_t^\top + Q_t)^{-1}$，就得到 $\Sigma_t = (I - K_tC_t)\bar\Sigma_t$、$\mu_t = \bar\mu_t + K_t(z_t - C_t\bar\mu_t)$。

（課本記號 $Q, R$ 對調，這裡已換成老師的記號。）

**其他推導**（[▶ 57:16](https://youtu.be/pSBhRF6j-Zc?t=3436)）：直接操作高斯隨機變數（最難、不有趣）；或 Kalman 原始論文的**最佳估計理論**：設均方誤差為成本，用投影理論找最佳估計器——很優雅、步驟很少，但和 Bayes 濾波的框架比較無關。`【口頭】` 推薦讀原始論文；卡爾曼濾波器是機器人學家最有用的工具之一，理解越深越好。

---

## 7. 非線性系統與擴展卡爾曼濾波器（EKF）

### 7.1 線性化

[▶ 58:43](https://youtu.be/pSBhRF6j-Zc?t=3523)

卡爾曼濾波器的推導假設線性；那時信念是高斯是**事實**。圖像上：高斯通過線性變換還是高斯，平均 $a\mu + b$、變異數 $a^2\sigma^2$（性質 1）。

**問題**：多數機器人模型**非線性**（例如 unicycle 有 $\cos\theta$、$\sin\theta$）。高斯通過非線性變換，出來的一般**不是高斯**（例如出現兩個峰）。嚴格說就不能用卡爾曼濾波器。

**做法**：引入近似——**假裝它是高斯**，看能不能推出一個實務上夠好的濾波器。怎麼近似？**線性化**：幾乎所有函數在局部看起來都像一條直線。用線性函數近似非線性變換，再讓高斯通過這個線性近似——出來的是高斯，是真實信念的某種近似。

**線性化**（一階泰勒展開）：在線性化點 $\bar x$ 附近，

$$
f(x) \approx f(\bar x) + f'(\bar x)\,(x - \bar x)
$$

**在哪一點線性化？**（[▶ 63:30](https://youtu.be/pSBhRF6j-Zc?t=3810)）要讓近似在**機率質量最集中**的區域最好，所以自然選**隨機變數的平均**。

**狀態轉移**：$x_t = g(u_t, x_{t-1}) + \varepsilon_t$，在 $\mu_{t-1}$ 展開：

$$
g(u_t, x_{t-1}) \approx g(u_t, \mu_{t-1}) + G_t\,(x_{t-1} - \mu_{t-1}), \qquad G_t = \left. \frac{\partial g}{\partial x_{t-1}} \right|_{u_t, \mu_{t-1}}
$$

$G_t$ 是 **Jacobian**。若 $x_{t-1}$ 是（或近似成）高斯，$\varepsilon_t$ 也是高斯，那 $x_t$ 也是高斯——回到和之前一樣的設定：模型本來不是線性的，但近似讓它**看起來**是線性的。

**量測**：$z_t = h(x_t) + \delta_t$，在**預測平均** $\bar\mu_t$ 展開：

$$
h(x_t) \approx h(\bar\mu_t) + H_t\,(x_t - \bar\mu_t), \qquad H_t = \left. \frac{\partial h}{\partial x_t} \right|_{\bar\mu_t}
$$

> ⚠️ 待確認 [▶ 66:20](https://youtu.be/pSBhRF6j-Zc?t=3980)：老師口頭說量測模型「也對 $x_{t-1}$ 分布的平均線性化」；但後面寫的式子是在 $\bar\mu_t$ 展開，課本 §12.3.1 也是在預測平均 $\bar\mu_t$ 展開。依式子和課本寫。

### 7.2 EKF 演算法

[▶ 66:28](https://youtu.be/pSBhRF6j-Zc?t=3988)

線性化之後，狀態轉移和量測都是線性的，卡爾曼濾波器的式子就都能用。`【課堂討論】` 哪個矩陣取代 $A_t$？→ $G_t$（看誰乘上 $x$）。哪個取代 $C_t$？→ $H_t$。「就是模式比對。」

**擴展卡爾曼濾波器（EKF）**

- **在解什麼**：非線性動態 $g$、非線性量測 $h$、高斯雜訊下，近似地遞迴計算高斯信念。
- **步驟**：
  1. 預測：

     $$
     \bar\mu_t = g(u_t, \mu_{t-1}), \qquad \bar\Sigma_t = G_t\Sigma_{t-1}G_t^\top + R_t
     $$

  2. 增益：

     $$
     K_t = \bar\Sigma_tH_t^\top\left( H_t\bar\Sigma_tH_t^\top + Q_t \right)^{-1}
     $$

  3. 修正：

     $$
     \mu_t = \bar\mu_t + K_t\left( z_t - h(\bar\mu_t) \right), \qquad \Sigma_t = \left( I - K_tH_t \right)\bar\Sigma_t
     $$

  注意：平均用**非線性函數本身**傳播（$g(u_t, \mu_{t-1})$、$h(\bar\mu_t)$），共變異數用 **Jacobian** 傳播。
- **實作**：拿非線性模型 → 線性化 → 把 Jacobian 代進卡爾曼濾波器的式子。
- **什麼時候會失敗**：見 7.3。

**關鍵差別**：現在是**近似**，不再有保證一定成功。實務上只要待在**操作點附近**就很好用。

### 7.3 EKF 什麼時候會失敗

[▶ 69:47](https://youtu.be/pSBhRF6j-Zc?t=4187)

把高斯推過非線性的運動方程：精確做會得到一個「很可怕、算不出來」的東西；線性化會得到一個（紅色）高斯，若和「用平均與標準差去配真實分布的最佳高斯」（藍色）很接近，EKF 就運作良好。

**兩種失敗方式**：

1. **分布很胖**（不確定性大）：線性化在線性化點附近很好，但大量機率質量落在離它很遠的地方，誤差就很大。例：同樣的非線性函數、同樣的線性化，但輸入分布尾巴更重 → EKF 的結果和最佳高斯差很多，**平均都差很遠**。反之，變異數很小時，大部分質量都在線性化點附近，結果不只和最佳高斯、甚至和真實分布都很吻合。
2. **函數非線性很強**：就算靠近線性化點，線性化也不準。

**EKF 不 work 時，檢查這四件事**（[▶ 72:52](https://youtu.be/pSBhRF6j-Zc?t=4372)）：

1. 程式有 **bug**（最可能）。
2. 函數**極度非線性** → 考慮換一種濾波器。
3. **不確定性太大** → 也許該買更好的感測器。
4. **$R_t$、$Q_t$ 設錯**（很常見）。誰告訴你在沙地上的過程擾動是多少？可以做很多量測來校正，但常常有點像藝術，幾乎變成**調整參數**。

`【口頭】` 卡爾曼濾波器最煩的是：它不是慢慢變好，而是「不 work、不 work……然後突然 work」。老師做衛星**姿態判定**的卡爾曼濾波器時，花了好幾天除錯才讓它動起來。「機器人學充滿挫折。」

- `【Q&A】` [▶ 74:32](https://youtu.be/pSBhRF6j-Zc?t=4472)（問能否在線上監測 EKF 是否失效）→ 可以，但部署後能給什麼保證很難說，信念的不確定性取決於很多你控制不了的事（例如行人做出古怪舉動）。可以加監測器：「此刻處在非線性區域，EKF 追不上定位了，改做別的」，但不容易。EKF 在機器人學被大量研究，有很多變形。

【課本補充】§12.3.1 也說：EKF 在非線性很強、或線性化點離真實狀態很遠時可能表現差或**發散**；它仍是單峰高斯，不能表示多重假設；成功部署靠好的初始化、仔細調整雜訊共變異數、以及在關心區域只有輕微非線性的模型。

---

## 8. 無跡卡爾曼濾波器（UKF）

[▶ 75:31](https://youtu.be/pSBhRF6j-Zc?t=4531)

非線性下近似卡爾曼濾波器的另一種熱門方法：**無跡卡爾曼濾波器（unscented Kalman filter, UKF）**，可以看成 EKF 的**對偶**：

| | EKF | UKF |
|---|---|---|
| 近似什麼 | **線性化變換**，讓高斯精確通過 | **近似輸入的高斯**（用一組粒子），讓粒子精確通過非線性變換 |
| 做法 | Jacobian | 取 **sigma 點**（通常相對共變異數對稱分布）→ 每個點通過非線性函數 → 用一個高斯去最佳擬合輸出的點（統計迴歸） |

UKF 通常**更穩健**，特別是不確定性很大時（輸入分布很胖，UKF 的輸出也比 EKF 更像最佳高斯），只是實作比較複雜。本課不講細節。

> 逐字稿中老師有幾處把 UKF 說成「EKF」（例如「What you do in the EKF is actually to approximate the Gaussian... through particles」），依上下文是 UKF。

【課本補充】§12.3.2：$n$ 維時取 $2n+1$ 個 sigma 點 $\mathcal{X}^{(0)} = \mu$、$\mathcal{X}^{(i)} = \mu \pm c_i$（$c_i$ 是 $(n+\lambda)\Sigma$ 的矩陣平方根的行），配上權重。對高斯先驗，無跡轉換的平均和共變異數至少準到**二階**，而 EKF 只到一階，而且**不用算 Jacobian**。代價是每步要評估 $2n+1$ 次模型。

**下一步**：週五（研究所）講非參數式濾波器（直方圖濾波、粒子濾波）；下週二把學到的套用到**定位**問題。

---

## 9. 一頁速查表

### 高斯三性質

| 性質 | 結果 | 用在 |
|---|---|---|
| 線性變換 | $AX + B \sim \mathcal{N}(A\mu + B,\ A\Sigma A^\top)$ | 預測 |
| 獨立相加 | $X_1 + X_2 \sim \mathcal{N}(\mu_1 + \mu_2,\ \Sigma_1 + \Sigma_2)$ | 預測（加過程雜訊） |
| PDF 相乘 | 仍是高斯：$\Sigma = (\Sigma_1^{-1} + \Sigma_2^{-1})^{-1}$ | 修正 |

一維變異數推導關鍵：$E[(aX + b - a\mu - b)^2] = a^2E[(X - \mu)^2]$。

### 卡爾曼濾波器（$R_t$ 過程、$Q_t$ 量測）

$$
\begin{aligned}
\bar\mu_t &= A_t\mu_{t-1} + B_tu_t, & \bar\Sigma_t &= A_t\Sigma_{t-1}A_t^\top + R_t \\
K_t &= \bar\Sigma_tC_t^\top(C_t\bar\Sigma_tC_t^\top + Q_t)^{-1} \\
\mu_t &= \bar\mu_t + K_t(z_t - C_t\bar\mu_t), & \Sigma_t &= (I - K_tC_t)\bar\Sigma_t
\end{aligned}
$$

- 條件：線性轉移、線性量測、高斯初始、雜訊和狀態獨立 → 信念**精確**是高斯。
- $Q_t$ 大 → $K_t$ 小（不信感測器）；$\bar\Sigma_t$ 小 → $K_t$ 小（已很確定）。
- 預測推導關鍵：$x_t$ = 兩個獨立高斯（$A_tx_{t-1}$ 和 $B_tu_t + \varepsilon_t$）之和。

### EKF

- $G_t = \partial g/\partial x$ 在 $\mu_{t-1}$；$H_t = \partial h/\partial x$ 在 $\bar\mu_t$。
- $A_t \to G_t$、$C_t \to H_t$；平均用 $g$、$h$ 本身傳播。
- 失敗：不確定性大、非線性強、bug、雜訊參數錯。

### UKF

- EKF 的對偶：近似分布（sigma 點）而不是近似函數；二階準確、不用 Jacobian、較穩健。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| EKF 套到 unicycle ＋ 光達量測 | 第 15 集 EKF 定位、作業 4 |
| 地圖未知時把地標放進狀態 | 第 16 集 EKF SLAM |
| 多感測器量測一起進修正步驟 | 第 17 集多感測器融合 |
| 非參數式濾波（粒子） | 第 21 集粒子濾波 SLAM |
| 線性化（Jacobian） | 第 4 集非精確線性化追蹤 |

---

## 附：本集一句話總結

> **把信念限制成高斯，Bayes 濾波器就只需要更新平均和共變異數：線性高斯系統下這是精確的卡爾曼濾波器，用卡爾曼增益權衡相信模型還是相信量測；非線性系統就在平均附近用 Jacobian 線性化，得到 EKF——不確定性小、非線性輕微時很好用，否則改用 UKF 等方法。**

---

## ⚠️ 待確認清單

1. 上課日期待補（只知道是週四）。
2. [▶ 66:20](https://youtu.be/pSBhRF6j-Zc?t=3980) 量測模型線性化點：老師口述說 $x_{t-1}$ 的平均，式子和課本都是 $\bar\mu_t$，依式子寫。
3. [▶ 26:29](https://youtu.be/pSBhRF6j-Zc?t=1589) 學生指出的投影片錯誤是什麼沒錄到，從上下文推斷是「獨立」條件。

---

*筆記依據 Marco Pavone（推斷）「Stanford AA274A Principles of Robotic Autonomy（2019 秋）」Lecture 14 錄影逐字稿（Whisper `medium.en`，1:17:44）與《Principles of Robot Autonomy》第 12 章整理。*
