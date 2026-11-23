---
course: Mobile Sensing and Robotics 1（Uni Bonn, Winter 2021/22）
episode: 1-07
lecture: Motion Models
date: 待補（2021/22 冬季學期）
video: https://youtu.be/IVTV7vJgIkU
notes: 《Probabilistic Robotics》早期草稿版 第 5 章 §5.2–5.4（書頁 92–114，PDF 頁 104–126）
---

# 第 1-07 集 · 機率運動模型（Motion Models） [▶ 影片](https://youtu.be/IVTV7vJgIkU)

← 上一集：[1-06-robot-locomotion](1-06-robot-locomotion.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[1-08-observation-models](1-08-observation-models.md) →

> **課程**：Mobile Sensing and Robotics 1，Uni Bonn，2021/22 冬季學期 — 第 1-07 集
> **講者**：Nived Chebrolu（依影片標題）
> **來源**：YouTube 錄影逐字稿（41:12，Whisper `medium.en` 轉錄）＋《Probabilistic Robotics》早期草稿版第 5 章
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 運動為什麼不確定](#1-運動為什麼不確定)
- [2. 運動模型在貝氏濾波裡的位置](#2-運動模型在貝氏濾波裡的位置)
- [3. 兩種模型：里程計 vs. 速度](#3-兩種模型里程計-vs-速度)
- [4. 輪式機器人的誤差來源](#4-輪式機器人的誤差來源)
- [5. 里程計模型](#5-里程計模型)
  - [5.1 旋轉—平移—旋轉](#51-旋轉平移旋轉)
  - [5.2 雜訊模型](#52-雜訊模型)
  - [5.3 常態分布與三角分布](#53-常態分布與三角分布)
  - [5.4 算機率：給定終點求 p](#54-算機率給定終點求-p)
  - [5.5 抽樣：給定起點產生終點](#55-抽樣給定起點產生終點)
- [6. 速度模型](#6-速度模型)
- [7. 總結](#7-總結)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集（1-06）假設機器人完全照指令走。這集加上**不確定性**：建立機率運動模型 $p(x_t \mid x_{t-1}, u_t)$，也就是貝氏濾波**預測步**裡的那一項。講兩種模型：**里程計模型**（詳細）和**速度模型**（簡略）。

| 主題 | 課本（草稿版） |
|---|---|
| 運動模型的定義、香蕉形分布 | §5.2.2（書頁 93–95） |
| 速度模型 | §5.3（書頁 95–107） |
| 里程計模型 | §5.4（書頁 107–114） |
| 抽樣常態／三角分布 | 表 5.2、表 5.4（書頁 97–98） |

---

## 1. 運動為什麼不確定

[▶ 00:05](https://youtu.be/IVTV7vJgIkU?t=5)

- 輪子在地上打滑。
- 給了速度指令，但機器人不會**瞬間**達到那個速度。
- 叫它走 1 公尺，實際可能走 95 公分或 1.05 公尺。

**例子** [▶ 02:37](https://youtu.be/IVTV7vJgIkU?t=157)：機器人在迷宮裡繞一圈。一條線是真正走的路，另一條是機器人「以為」自己走的路（里程計的估計）。里程計一直**偏右**，誤差一路累積（**漂移**，drift）。

【口頭】偏右的可能原因：重量分配不平均，或某個輪胎打氣比較多。結果是隨時間累積的系統性漂移。

---

## 2. 運動模型在貝氏濾波裡的位置

[▶ 03:50](https://youtu.be/IVTV7vJgIkU?t=230)

要算的是

$$
p(x_t \mid x_{t-1},\, u_t)
$$

「從 $x_{t-1}$ 出發、執行指令 $u_t$，最後在 $x_t$ 的機率」。這叫**運動模型**（motion model）。它是一個**後驗**機率，因為是在給定條件下 $x_t$ 的機率 [▶ 07:52](https://youtu.be/IVTV7vJgIkU?t=472)。

【口頭】例子：叫機器人從原點走 1 公尺，可以問「最後在 1.1 公尺的機率」「在 0.99 公尺的機率」……。最高的機率應該在 1 公尺附近。

**在貝氏濾波裡** [▶ 05:23](https://youtu.be/IVTV7vJgIkU?t=323)（1-03 第 4 節）：

$$
\overline{bel}(x_t) = \int p(x_t \mid x_{t-1},\, u_t)\; bel(x_{t-1})\; dx_{t-1}
$$

- 對所有可能的上一刻位置 $x_{t-1}$，乘上「從那裡到 $x_t$ 的機率」，加起來 → **預測步**。
- 之後用觀測 $z_t$（GPS、雷射……）修正 → 下一集 1-08。
- 一般來說：**運動增加不確定性，觀測減少不確定性** [▶ 07:29](https://youtu.be/IVTV7vJgIkU?t=449)。

**$u_t$ 是什麼** [▶ 08:13](https://youtu.be/IVTV7vJgIkU?t=493)：

| 平台 | $u_t$ |
|---|---|
| 差速驅動 | 左右輪速度 |
| Ackermann | 線速度、角速度、轉向角 |
| 四軸飛行器 | 各螺旋槳的指令 |
| 人形機器人 | 各關節的指令 |

本集只講**輪式**機器人，用兩個比較抽象的模型，不綁定特定驅動方式。

---

## 3. 兩種模型：里程計 vs. 速度

[▶ 09:07](https://youtu.be/IVTV7vJgIkU?t=547)

| | 里程計模型（odometry-based） | 速度模型（velocity-based） |
|---|---|---|
| 資料來源 | 馬達軸上的**編碼器**量到的實際轉動 | 給機器人的**速度指令** |
| 性質 | 一種回饋：事後量到實際怎麼動 | 只是「往前看」：照物理公式推算 |
| 別名 | — | 講者說有時也叫**航位推算**（dead reckoning） |
| 準確度 | 通常**較高** | 通常較低 |
| 什麼時候用 | 有編碼器時，實務上多半用這個 | 沒有編碼器、只有指令時 |

【口頭】嚴格說，里程計是**量測**；但本課把它當成**控制指令**來處理，因為它量的是「怎麼移動」[▶ 09:55](https://youtu.be/IVTV7vJgIkU?t=595)。

### 輪子編碼器

[▶ 10:38](https://youtu.be/IVTV7vJgIkU?t=638)

- 一個有黑白相間條紋的圓盤，裝在馬達軸上，跟著馬達轉。
- 電路偵測「從白條換到黑條」的時刻，產生一個脈衝。
- 數脈衝就知道馬達轉了多少；輪子直接接在馬達上，就能換算平台移動了多少。

為什麼里程計比較準 [▶ 12:06](https://youtu.be/IVTV7vJgIkU?t=726)：它記錄的是指令**執行後**實際的轉動；速度模型只是**希望**指令有被執行，不知道中間發生了什麼。

【課本補充】課本 §5.4（書頁 107）補充：兩者都有漂移和打滑的問題，但速度模型還多了「實際的馬達控制器和（粗糙的）數學模型不一致」這個誤差。另外，里程計只能**事後**拿到，對濾波沒問題，但不能拿來做精確的規劃和控制。

【課本補充】課本 §5.4.1（書頁 108）說明為什麼把里程計當控制：如果把它當量測，貝氏濾波的狀態就必須包含實際速度，狀態維度會變大。為了讓狀態空間小，通常直接把里程計當成控制訊號。

---

## 4. 輪式機器人的誤差來源

[▶ 12:46](https://youtu.be/IVTV7vJgIkU?t=766)

理想情況：兩個輪子直徑完全一樣、地面平坦、平順滾動 → 完全照 1-06 的差速或 Ackermann 公式走。

實際上：

| 誤差來源 | 結果 |
|---|---|
| 壓過電線、石頭，產生顛簸 | 某個輪子少算或多算幾圈 → 以為走的距離和實際不同 |
| 兩輪直徑不同（打氣不一樣；載重不平均，一邊壓力較大） | 運動公式不知道這件事 → 估計和實際偏離 |
| 地毯、滑的地面 | 輪子沒有純滾動 → 輪子轉數和實際移動對不上 |

---

## 5. 里程計模型

### 5.1 旋轉—平移—旋轉

[▶ 15:04](https://youtu.be/IVTV7vJgIkU?t=904)

- 里程計報告：時間 $t-1$ 在 $\bar{x}_{t-1} = (\bar{x}, \bar{y}, \bar\theta)$，時間 $t$ 在 $\bar{x}_t = (\bar{x}', \bar{y}', \bar\theta')$。（頭上的橫線表示這是里程計自己座標系裡的讀數。）
- 把兩個位姿之間的移動拆成三步：
  1. **原地旋轉** $\delta_{\text{rot1}}$（轉向目標點）
  2. **直線平移** $\delta_{\text{trans}}$
  3. **原地旋轉** $\delta_{\text{rot2}}$（轉到最後的朝向）
- 這只是**抽象化**：差速機器人實際可能沿圓弧走，但分析時把指令拆成「轉—走—轉」。

**從兩個位姿算出三個參數** [▶ 16:09](https://youtu.be/IVTV7vJgIkU?t=969)：

$$
\delta_{\text{trans}} = \sqrt{(\bar{x}' - \bar{x})^2 + (\bar{y}' - \bar{y})^2}
$$

$$
\delta_{\text{rot1}} = \operatorname{atan2}(\bar{y}' - \bar{y},\; \bar{x}' - \bar{x}) - \bar\theta
$$

$$
\delta_{\text{rot2}} = \bar\theta' - \bar\theta - \delta_{\text{rot1}}
$$

- $\delta_{\text{trans}}$：兩點的距離。
- $\delta_{\text{rot1}}$：從起點指向終點的方向角，減掉原本的朝向。
- $\delta_{\text{rot2}}$：總共要轉的角度 $\bar\theta' - \bar\theta$，扣掉已經轉的 $\delta_{\text{rot1}}$。

（$\operatorname{atan2}(y, x)$ 是四象限的反正切，回傳 $(-\pi, \pi]$ 的角度。）

【課本補充】課本 §5.4.1（書頁 109）：每一對位姿都對應**唯一**的 $(\delta_{\text{rot1}}, \delta_{\text{trans}}, \delta_{\text{rot2}})$，而且這三個數足以重建相對運動，所以它們是相對運動的**充分統計量**（sufficient statistic）。里程計的座標系和真實世界座標系之間的轉換未知（知道的話定位問題就解決了），但**相對**移動是真實相對移動的好估計。

### 5.2 雜訊模型

[▶ 17:27](https://youtu.be/IVTV7vJgIkU?t=1047)

**兩種想法**：

1. 直接假設終點附近是一個大高斯。
2. **對三個參數各自加雜訊**。← 實務上比較符合真實的雜訊。

講者用第二種 [▶ 18:16](https://youtu.be/IVTV7vJgIkU?t=1096)：

$$
\hat\delta_{\text{rot1}} = \delta_{\text{rot1}} + \varepsilon_{\alpha_1 |\delta_{\text{rot1}}| + \alpha_2 \delta_{\text{trans}}}
$$

$$
\hat\delta_{\text{trans}} = \delta_{\text{trans}} + \varepsilon_{\alpha_3 \delta_{\text{trans}} + \alpha_4 (|\delta_{\text{rot1}}| + |\delta_{\text{rot2}}|)}
$$

$$
\hat\delta_{\text{rot2}} = \delta_{\text{rot2}} + \varepsilon_{\alpha_1 |\delta_{\text{rot2}}| + \alpha_2 \delta_{\text{trans}}}
$$

- $\varepsilon_b$：平均為 0、參數為 $b$ 的雜訊。講者稱 $b$ 為「標準差」；課本草稿版稱為「變異數」。
- 雜訊大小**和移動量成正比**：

| 係數 | 意思 |
|---|---|
| $\alpha_1$ | 旋轉量 → 旋轉誤差（轉 60° 比轉 30° 誤差大） |
| $\alpha_2$ | 平移量 → 旋轉誤差（走得遠，角度也容易偏） |
| $\alpha_3$ | 平移量 → 平移誤差 |
| $\alpha_4$ | 旋轉量 → 平移誤差 |

- 兩個旋轉用同一組 $\alpha_1, \alpha_2$。
- 這四個 $\alpha$ 是**機器人特有**的參數。

（絕對值記號是筆記加的：角度可以是負的，但雜訊大小要用量的大小。講者口述「轉多少」，沒有提到正負號。）

**重要**：三個參數的雜訊都是高斯，但**終點位置的分布不是高斯** [▶ 18:37](https://youtu.be/IVTV7vJgIkU?t=1117)，因為從 $(\delta_{\text{rot1}}, \delta_{\text{trans}}, \delta_{\text{rot2}})$ 到 $(x', y', \theta')$ 的公式是**非線性**的（有 $\cos$、$\sin$）。高斯經過非線性函數就不再是高斯。

### 5.3 常態分布與三角分布

[▶ 21:07](https://youtu.be/IVTV7vJgIkU?t=1267)

$\varepsilon$ 通常用常態分布，但任何能描述雜訊的分布都可以。

**為什麼考慮三角分布** [▶ 21:29](https://youtu.be/IVTV7vJgIkU?t=1289)：

- 常態分布在無限遠處還有一點點機率。
- 【口頭】對機器人來說，「突然出現在無限遠」等於被**綁架**（kidnapped）。
- 如果確定系統不會這樣，可以用三角分布：誤差**有界**，永遠不會超出範圍。

**密度函數**（$a$ = 查詢點離平均值多遠，$b$ = 標準差）[▶ 23:10](https://youtu.be/IVTV7vJgIkU?t=1390)：

常態：

$$
\mathrm{prob}(a, b) = \frac{1}{\sqrt{2\pi b^2}} \exp\!\left( -\frac{1}{2}\frac{a^2}{b^2} \right)
$$

三角：

$$
\mathrm{prob}(a, b) = \max\!\left( 0,\; \frac{\sqrt{6}\, b - |a|}{6 b^2} \right)
$$

（公式在投影片上，逐字稿沒有唸出來。以下**不是逐字稿內容**：三角分布的式子是依課本表 5.2 的結構、並用「標準差 $b$」重新整理的。檢查：底寬 $2\sqrt6 b$、峰高 $\frac{1}{\sqrt6 b}$，面積 $= \frac12 \cdot 2\sqrt6 b \cdot \frac{1}{\sqrt6 b} = 1$；變異數 $= \frac{(\sqrt6 b)^2}{6} = b^2$。課本草稿版排版不清，寫作「$\frac{\sqrt{6b} - |a|}{6b}$」，且把 $b$ 稱為變異數。）

【口頭】例子 [▶ 23:49](https://youtu.be/IVTV7vJgIkU?t=1429)：叫機器人轉 30°，問「實際轉了 45° 的機率」→ $a = 45° - 30° = 15°$；$b$ 是這個動作通常的誤差，要從機器人本身的行為估計。

### 5.4 算機率：給定終點求 p

[▶ 24:21](https://youtu.be/IVTV7vJgIkU?t=1461)

**問題**：已知里程計讀數 $u_t = (\bar{x}_{t-1}, \bar{x}_t)$，假設機器人從 $x_{t-1} = (x, y, \theta)$ 到了 $x_t = (x', y', \theta')$，這個假設的機率是多少？

```
Algorithm motion_model_odometry(x_t, u_t, x_{t-1}):
  // 1. 里程計讀數 → 三個參數（量到的）
  δ_rot1  = atan2(ȳ' - ȳ, x̄' - x̄) - θ̄
  δ_trans = sqrt((x̄' - x̄)² + (ȳ' - ȳ)²)
  δ_rot2  = θ̄' - θ̄ - δ_rot1
  // 2. 假設的起終點 → 三個參數（假設的）
  δ̂_rot1  = atan2(y' - y, x' - x) - θ
  δ̂_trans = sqrt((x' - x)² + (y' - y)²)
  δ̂_rot2  = θ' - θ - δ̂_rot1
  // 3. 每個參數的差，在雜訊分布下的機率
  p1 = prob(δ_rot1  - δ̂_rot1,  α1|δ̂_rot1| + α2 δ̂_trans)
  p2 = prob(δ_trans - δ̂_trans, α3 δ̂_trans + α4(|δ̂_rot1| + |δ̂_rot2|))
  p3 = prob(δ_rot2  - δ̂_rot2,  α1|δ̂_rot2| + α2 δ̂_trans)
  // 4. 假設三者獨立 → 相乘
  return p1 · p2 · p3
```

（形式依課本表 5.5，書頁 108；講者口述的步驟相同。）

- 三個動作的誤差**互相獨立**，所以機率相乘 [▶ 26:01](https://youtu.be/IVTV7vJgIkU?t=1561)。
- 要畫出整個分布，就對**每個可能的終點**跑一次這個演算法 [▶ 26:24](https://youtu.be/IVTV7vJgIkU?t=1584)。

【課本補充】課本書頁 110 提醒一個常見錯誤：所有**角度差**都必須落在 $[-\pi, \pi]$，例如 $\delta_{\text{rot2}} - \hat\delta_{\text{rot2}}$ 要截到這個範圍。忘了這件事，程式偶爾會發散。

### 結果：香蕉形分布

[▶ 26:34](https://youtu.be/IVTV7vJgIkU?t=1594)

- 從 $x$ 出發、執行 $u$，越黑的地方越可能是終點。
- 形狀像**香蕉**：因為這台機器人的**旋轉誤差比平移誤差大**，沿角度方向的變異大於沿前進方向。
- 如果各誤差一樣大，會比較接近圓形。
- 路徑不同，形狀也不同（誤差隨時間傳遞）。
- 做法 [▶ 27:52](https://youtu.be/IVTV7vJgIkU?t=1672)：在終點附近畫網格，每格跑一次演算法。圖是 2D 的，實際是 3D（$x, y, \theta$）。
- 這叫**直方圖表示**（histogram representation）：把世界離散化，每格一個機率。

### 5.5 抽樣：給定起點產生終點

[▶ 28:32](https://youtu.be/IVTV7vJgIkU?t=1712)

另一種表示：**樣本表示**（sample-based representation）。

- 機率密度高的地方，樣本多。
- 之後幾集（粒子濾波，1-14）會看到：樣本表示比直方圖好用。
- 要做這件事，先要會從分布**抽樣**。

**從常態分布抽樣** [▶ 29:25](https://youtu.be/IVTV7vJgIkU?t=1765)：取 12 個均勻分布的隨機數，加起來，除以 2：

$$
\mathrm{sample}(b) = \frac{1}{2} \sum_{i=1}^{12} \mathrm{rand}(-b,\, b)
$$

講者畫了一百萬個樣本的直方圖，看起來就是常態分布。

**為什麼是 12 個、除以 2**（以下**不是逐字稿內容**，是依機率計算推論的）：$\mathrm{rand}(-b, b)$ 的變異數是 $\frac{(2b)^2}{12} = \frac{b^2}{3}$。12 個獨立相加，變異數 $= 12 \cdot \frac{b^2}{3} = 4b^2$。除以 2，變異數 $= \frac{4b^2}{4} = b^2$，標準差剛好是 $b$。由中央極限定理，很多個獨立變數相加會接近常態。

【課本補充】課本草稿版表 5.4（書頁 98）寫作 $\frac{b}{6}\sum_{i=1}^{12}\mathrm{rand}(-1, 1)$，標準差是 $\frac{b}{6} \cdot 2 = \frac{b}{3}$，和「變異數 $b$」或「標準差 $b$」都對不上，應是草稿的筆誤。課本也指出這個近似的值永遠落在有限範圍內（不是真的常態）。

**從三角分布抽樣** [▶ 30:04](https://youtu.be/IVTV7vJgIkU?t=1804)：公式在投影片上，講者說「不看證明」，逐字稿沒有唸出公式。1000 個樣本時近似還有誤差；一百萬個樣本就很接近三角形。

以下**不是逐字稿內容**，是依機率計算推論的：兩個獨立的 $\mathrm{rand}(-b, b)$ **相加**是 $[-2b, 2b]$ 上的三角分布，變異數 $\frac{2b^2}{3}$；乘上 $\frac{\sqrt6}{2}$ 讓變異數變成 $b^2$：

$$
\mathrm{sample\_tri}(b) = \frac{\sqrt{6}}{2}\bigl( \mathrm{rand}(-b, b) + \mathrm{rand}(-b, b) \bigr)
$$

（課本草稿版表 5.4 寫的是 $b \cdot \mathrm{rand}(-1,1) \cdot \mathrm{rand}(-1,1)$，兩個均勻變數**相乘**不是三角分布，應是筆誤。）

**抽樣版的運動模型** [▶ 30:38](https://youtu.be/IVTV7vJgIkU?t=1838)：像**模擬**一樣。

- 例如 100 個樣本當作 100 個可能的 $x_{t-1}$。
- 對每個樣本：照指令移動，並依雜訊模型加上隨機雜訊 → 得到一個新位姿。
- 新的 100 個位姿就近似運動模型的分布。

```
Algorithm sample_motion_model_odometry(u_t, x_{t-1}):
  δ_rot1  = atan2(ȳ' - ȳ, x̄' - x̄) - θ̄
  δ_trans = sqrt((x̄' - x̄)² + (ȳ' - ȳ)²)
  δ_rot2  = θ̄' - θ̄ - δ_rot1
  δ̂_rot1  = δ_rot1  + sample(α1|δ_rot1| + α2 δ_trans)
  δ̂_trans = δ_trans + sample(α3 δ_trans + α4(|δ_rot1| + |δ_rot2|))
  δ̂_rot2  = δ_rot2  + sample(α1|δ_rot2| + α2 δ_trans)
  x' = x + δ̂_trans · cos(θ + δ̂_rot1)
  y' = y + δ̂_trans · sin(θ + δ̂_rot1)
  θ' = θ + δ̂_rot1 + δ̂_rot2
  return (x', y', θ')
```

（形式依課本表 5.6，書頁 110；講者口述的步驟相同 [▶ 31:19](https://youtu.be/IVTV7vJgIkU?t=1879)。課本用減號 $\delta - \mathrm{sample}(\cdot)$，因為雜訊平均為 0、對稱，加或減結果一樣。）

**位置更新的由來**：先轉 $\hat\delta_{\text{rot1}}$，朝向變成 $\theta + \hat\delta_{\text{rot1}}$；沿這個方向走 $\hat\delta_{\text{trans}}$，所以 $x$ 增加 $\hat\delta_{\text{trans}}\cos(\theta + \hat\delta_{\text{rot1}})$、$y$ 增加 $\hat\delta_{\text{trans}}\sin(\theta + \hat\delta_{\text{rot1}})$；最後再轉 $\hat\delta_{\text{rot2}}$，總朝向變化是兩次旋轉之和。

**結果** [▶ 32:58](https://youtu.be/IVTV7vJgIkU?t=1978)：樣本的形狀和直方圖版很像。三種參數：

- 角度誤差大 → 香蕉形。
- 前進方向誤差大 → 沿前進方向拉長。
- 角度誤差遠大於平移誤差 → 很彎的香蕉。

**連續執行多個指令** [▶ 33:55](https://youtu.be/IVTV7vJgIkU?t=2035)：起點確定，每執行一個指令，樣本就散開一點；執行約 10 個指令後，分布已經非常分散。也可以用直方圖做同樣的事。

### 兩種方法對照

| | 直方圖／算密度 | 抽樣 |
|---|---|---|
| 輸入 | $x_{t-1}$、$u_t$、**假設的** $x_t$ | $x_{t-1}$、$u_t$ |
| 輸出 | 機率 $p(x_t \mid x_{t-1}, u_t)$ | 一個隨機的 $x_t$ |
| 做法 | 反推：終點 → 參數 → 誤差機率 | 正向模擬：加雜訊 → 移動 |
| 用在 | 直方圖濾波、EKF 類 | 粒子濾波 |

【課本補充】課本 §5.3.2（書頁 99）：很多時候**抽樣比算密度容易**。抽樣只需要正向模擬物理模型；算某個假設位姿的機率，需要反推誤差參數，也就是要算物理模型的反函數。粒子濾波只需要抽樣，這是它好實作的原因之一。

---

## 6. 速度模型

[▶ 35:16](https://youtu.be/IVTV7vJgIkU?t=2116)

- 指令是**線速度** $v$ 和**角速度** $\omega$。給定 $v, \omega$，機器人沿圓弧走。
- 雜訊加在 $v$ 和 $\omega$ 上，大小和兩者的量值有關，各有係數：

$$
\hat{v} = v + \varepsilon_{\alpha_1 |v| + \alpha_2 |\omega|}, \qquad
\hat\omega = \omega + \varepsilon_{\alpha_3 |v| + \alpha_4 |\omega|}
$$

### 缺一個維度

[▶ 36:14](https://youtu.be/IVTV7vJgIkU?t=2174)

- 狀態有 **3** 維（$x, y, \theta$），控制只有 **2** 維（$v, \omega$）。
- 給定 $v, \omega$ 就對應一條圓弧。終點的**朝向**被圓弧決定了，無法表示「到了圓弧上同一個點、但朝向不同」的誤差。
- 解法：加一個額外的誤差項 $\gamma$，加在最後的朝向上 [▶ 37:03](https://youtu.be/IVTV7vJgIkU?t=2223)：

$$
\hat\gamma = \varepsilon_{\alpha_5 |v| + \alpha_6 |\omega|}
$$

### 更新公式

[▶ 37:17](https://youtu.be/IVTV7vJgIkU?t=2237)

講者說「不推導，這就是更新式」：

$$
\begin{aligned}
x' &= x - \frac{\hat v}{\hat\omega}\sin\theta + \frac{\hat v}{\hat\omega}\sin(\theta + \hat\omega\,\Delta t) \\
y' &= y + \frac{\hat v}{\hat\omega}\cos\theta - \frac{\hat v}{\hat\omega}\cos(\theta + \hat\omega\,\Delta t) \\
\theta' &= \theta + \hat\omega\,\Delta t + \hat\gamma\,\Delta t
\end{aligned}
$$

（公式依課本表 5.3 與式 (5.9)，書頁 98、101。）

**推導**（講者沒推；依課本 §5.3.3 和 1-06 的 ICC 整理）：

1. 沿圓弧走，半徑 $r = \hat v / \hat\omega$（由 $v = \omega r$）。
2. 圓心（就是 1-06 的 ICC，把 $R$ 換成 $r$）：$x_c = x - r\sin\theta$，$y_c = y + r\cos\theta$。
3. 經過 $\Delta t$，朝向轉了 $\hat\omega\,\Delta t$，新朝向 $\theta + \hat\omega\,\Delta t$。
4. 新位置在圓上、相對圓心的方向和新朝向垂直：$x' = x_c + r\sin(\theta + \hat\omega\Delta t)$，$y' = y_c - r\cos(\theta + \hat\omega\Delta t)$。
5. 代入 $x_c, y_c$ 就得到上式。
6. 最後朝向再加上 $\hat\gamma\,\Delta t$。

（$\hat\omega = 0$ 時是直線，$r \to \infty$，公式要另外處理。）

**結果** [▶ 38:17](https://youtu.be/IVTV7vJgIkU?t=2297)：看起來和里程計模型很像。有些機器人沒有編碼器，只能用速度模型。一般來說速度模型**比較不準**：只是下了指令，不知道實際發生什麼。

【課本補充】課本 §5.4.1（書頁 111）：兩次更新之間的時間越短，兩種模型越相似。室內機器人通常每 0.1 秒更新一次，這時差別不大。可用時，里程計模型比較好，特別是速度值不是量到的、而是丟給 PID 控制器去設定馬達電流時。

---

## 7. 總結

[▶ 38:59](https://youtu.be/IVTV7vJgIkU?t=2339)

- 兩種模型：**里程計模型**（有編碼器）和**速度模型**（只有指令）。
- 兩種計算方式：對空間中每一點**查詢**機率（直方圖），或**抽樣**模擬。
- 執行多個指令後，誤差累積成漂移。
- 所有計算都假設固定的時間間隔 $\Delta t$，在這段時間內指令不變。【口頭】如果更新夠快（例如每秒 100 次），就幾乎等於連續積分 [▶ 40:24](https://youtu.be/IVTV7vJgIkU?t=2424)。
- 延伸閱讀：《Probabilistic Robotics》第 5 章（速度模型的推導在那裡）。

---

## 8. 一頁速查表

### 8.1 里程計模型

| 項 | 公式 | 關鍵一步 |
|---|---|---|
| 平移 | $\delta_{\text{trans}} = \sqrt{(\bar x' - \bar x)^2 + (\bar y' - \bar y)^2}$ | 兩點距離 |
| 第一次旋轉 | $\delta_{\text{rot1}} = \operatorname{atan2}(\bar y' - \bar y, \bar x' - \bar x) - \bar\theta$ | 轉向終點 |
| 第二次旋轉 | $\delta_{\text{rot2}} = \bar\theta' - \bar\theta - \delta_{\text{rot1}}$ | 總轉角扣掉第一次 |
| 雜訊 | $\varepsilon_{\alpha_1|\delta_{\text{rot}}| + \alpha_2\delta_{\text{trans}}}$（旋轉）、$\varepsilon_{\alpha_3\delta_{\text{trans}} + \alpha_4(|\delta_{\text{rot1}}| + |\delta_{\text{rot2}}|)}$（平移） | 誤差和移動量成正比 |
| 正向更新 | $x' = x + \hat\delta_{\text{trans}}\cos(\theta + \hat\delta_{\text{rot1}})$，$y' = y + \hat\delta_{\text{trans}}\sin(\theta + \hat\delta_{\text{rot1}})$，$\theta' = \theta + \hat\delta_{\text{rot1}} + \hat\delta_{\text{rot2}}$ | 轉—走—轉 |
| 機率 | $p = p_1\, p_2\, p_3$ | 三個誤差獨立 |

### 8.2 速度模型

| 項 | 公式 |
|---|---|
| 雜訊 | $\hat v = v + \varepsilon_{\alpha_1|v| + \alpha_2|\omega|}$，$\hat\omega = \omega + \varepsilon_{\alpha_3|v| + \alpha_4|\omega|}$，$\hat\gamma = \varepsilon_{\alpha_5|v| + \alpha_6|\omega|}$ |
| 更新 | $x' = x - \frac{\hat v}{\hat\omega}\sin\theta + \frac{\hat v}{\hat\omega}\sin(\theta + \hat\omega\Delta t)$ |
| | $y' = y + \frac{\hat v}{\hat\omega}\cos\theta - \frac{\hat v}{\hat\omega}\cos(\theta + \hat\omega\Delta t)$ |
| | $\theta' = \theta + \hat\omega\Delta t + \hat\gamma\Delta t$ |
| 為什麼要 $\gamma$ | 狀態 3 維、控制 2 維，缺終點朝向的誤差 |

### 8.3 分布與抽樣（$b$ = 標準差）

| | 密度 | 抽樣 |
|---|---|---|
| 常態 | $\frac{1}{\sqrt{2\pi}b}e^{-a^2/(2b^2)}$ | $\frac12\sum_{i=1}^{12}\mathrm{rand}(-b, b)$（變異數 $12 \cdot \frac{b^2}{3} / 4 = b^2$） |
| 三角 | $\max\!\left(0, \frac{\sqrt6 b - |a|}{6b^2}\right)$ | $\frac{\sqrt6}{2}(\mathrm{rand}(-b,b) + \mathrm{rand}(-b,b))$（推論） |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $p(x_t \mid x_{t-1}, u_t)$ = 預測步 | 1-08 觀測模型（另一半：修正步） |
| 高斯經非線性 → 非高斯 | 1-10 EKF（線性化來近似） |
| 里程計模型 | 1-12 EKF 定位、1-14 MCL |
| 抽樣版運動模型 | 1-14 粒子濾波（每個粒子用它往前推） |
| 漂移累積 | 1-21 定位總覽、MSR2 2-03 SLAM |

---

## 附：本集一句話總結

> **把一段移動拆成「轉—走—轉」，三個參數各自加上和移動量成正比的雜訊，就得到里程計運動模型；終點分布是香蕉形，可以逐點算機率，也可以直接抽樣模擬。**

---

*筆記依據 Nived Chebrolu「Mobile Sensing and Robotics 1」Motion Models 錄影逐字稿（Whisper `medium.en`，41:12）與《Probabilistic Robotics》早期草稿版第 5 章整理。*
