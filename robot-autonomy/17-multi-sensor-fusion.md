---
course: Stanford AA274A Principles of Robotic Autonomy（2019 秋）
episode: 17
lecture: Lecture 17
date: 待補（講者說「下一堂在週四」）
video: https://youtu.be/j0LGkdKtKaY
notes: 《Principles of Robot Autonomy》第 15 章 §15.1–15.3（書頁 391–403，PDF 頁 393–405）
---

# 第 17 集 · Lecture 17：多感測器感知與資料融合（Multi-Sensor Perception & Data Fusion） [▶ 影片](https://youtu.be/j0LGkdKtKaY)

← 上一集：[16-ekf-slam](16-ekf-slam.md) ｜ [總目錄](README.md) ｜ 下一集：[18-modern-computer-vision](18-modern-computer-vision.md) →

> **課程**：Stanford AA274A Principles of Robotic Autonomy I，2019 秋 — 第 17 集
> **講者**：客座講者，來自奧地利格拉茲（Graz）的大學（自我介紹提到故鄉和 Arnold Schwarzenegger 同城）。姓名逐字稿沒有，⚠️ 待確認（推測是 TU Graz 的 Daniel Watzenig）。
> **來源**：YouTube 錄影逐字稿（1:16:23，Whisper `medium.en` 轉錄）＋《Principles of Robot Autonomy》第 15 章
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯，依課本或常識修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單
>
> **記號注意**：講者和 Pavone 一樣，用 $R_t$ 表示**過程雜訊**、$Q_t$ 表示**量測雜訊**；課本第 15 章相反（$Q_t$ 過程、$R_t$ 量測）。本筆記照講者。
>
> **常見聽錯**（⚠️ 逐字稿缺字，統一修正）：「Miladyne」→ Velodyne；「mobile eye」→ Mobileye；「Universal / inversion measurement unit」→ **慣性量測單元**（Inertial Measurement Unit, IMU）；「lighter」→ lidar；「diffusion level」→ the fusion level；「Magner, Denser」→ Magna、Denso；「G-square」→ chi-square；「pre-widening」→ pre-whitening；「estrogen one」→ estimate；「search sensor」→ third sensor。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要融合](#1-為什麼要融合)
- [2. 融合的四種分類法](#2-融合的四種分類法)
- [3. 貝氏觀點](#3-貝氏觀點)
- [4. 最簡單的例子：融合兩個高斯量測](#4-最簡單的例子融合兩個高斯量測)
  - [4.1 問題設定](#41-問題設定)
  - [4.2 推導：配方](#42-推導配方)
  - [4.3 結論：融合後比最好的感測器還準](#43-結論融合後比最好的感測器還準)
  - [4.4 和算術平均、中位數、並聯電阻的比較](#44-和算術平均中位數並聯電阻的比較)
- [5. 卡爾曼濾波器回顧](#5-卡爾曼濾波器回顧)
  - [5.1 三個假設](#51-三個假設)
  - [5.2 只能處理單一假設](#52-只能處理單一假設)
  - [5.3 跑濾波器之前：配準與時間同步](#53-跑濾波器之前配準與時間同步)
  - [5.4 預測與修正](#54-預測與修正)
- [6. 進階例子：用 KF 融合光達、GPS、IMU 估計位置](#6-進階例子用-kf-融合光達gpsimu-估計位置)
  - [6.1 為什麼不能只靠 IMU](#61-為什麼不能只靠-imu)
  - [6.2 模型](#62-模型)
  - [6.3 初值與雜訊共變異數怎麼設](#63-初值與雜訊共變異數怎麼設)
  - [6.4 情況一：光達＋IMU](#64-情況一光達imu)
  - [6.5 情況二：再加 GPS](#65-情況二再加-gps)
- [7. 偏差、有色雜訊、故障偵測](#7-偏差有色雜訊故障偵測)
- [8. 總結](#8-總結)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 01:38](https://youtu.be/j0LGkdKtKaY?t=98)

客座講者負責三堂：這堂講**資料融合**（data fusion）的觀念，之後兩堂是 Autoware（開源自駕軟體）的介紹和實作（週四、週五）。內容：

1. 為什麼需要多感測器融合；融合有哪幾種分類法。
2. 用貝氏觀點、從兩個高斯量測的融合推出「融合後變異數變小」。
3. 用卡爾曼濾波器做位置估計的融合，以及實務上的坑（配準、同步、雜訊共變異數、偏差）。

| 課堂主題 | 課本對應 |
|---|---|
| 融合的分類法 | §15.1（書頁 393–394） |
| 貝氏融合、兩個高斯的融合 | §15.2、例 15.2.1（書頁 394–395） |
| KF 多感測器融合（光達／GNSS／IMU） | §15.2.1、例 15.2.2（書頁 395–397） |
| 偏差擴增狀態、未知相關性 | §15.2.1–15.2.2（書頁 397–398） |
| 配準、時間同步等工程問題 | §15.3（書頁 399–403） |

【口頭】[▶ 02:10](https://youtu.be/j0LGkdKtKaY?t=130) 講者推薦兩本書：Fredrik Gustafsson《Statistical Sensor Fusion》（較進階，涵蓋時間同步、空間定位等實車問題）；Dan Simon《Optimal State Estimation》（從貝氏理論講到 KF、EKF、UKF、粒子濾波、$H_\infty$ 濾波）。

---

## 1. 為什麼要融合

[▶ 03:08](https://youtu.be/j0LGkdKtKaY?t=188)

【口頭】影片：講者實驗室在奧地利實車的資料——Mobileye 攝影機、Continental 長距離雷達、16 線 Velodyne 光達。

融合在車上有兩種用途：

1. **感知**（perception）：用攝影機、雷達、光達找出周圍物體。
2. **位姿估計**（pose estimation）：用 GPS、IMU、光達估計自己在哪——「要先精確知道自己在哪，才准開車」。

**核心理由** [▶ 04:28](https://youtu.be/j0LGkdKtKaY?t=268)：每個量測都有不確定性，融合的目標是**降低不確定性**。

- 雷達：在**距離方向**很準，但橫向（角度）不準 → 不確定性是一個橫向拉長的形狀。
- 攝影機：剛好相反，角度準、距離不準。
- 兩者融合 → 落在兩個形狀的**交集**，不確定性變小。

【口頭】例子：長距離雷達＋攝影機融合。物體進入兩個感測器都看得到的區域時，KF 估計的共變異數明顯縮小；只有一個感測器看得到（車的左右兩側）時，變異數又變大。

【口頭】[▶ 06:07](https://youtu.be/j0LGkdKtKaY?t=367) 延伸視野：在基礎設施上裝固定感測器。BMW 在 101 號公路上裝了攝影機和雷達，研究切入、匯流情境。車上的長距離雷達、光達約看 250–300 公尺；加上基礎設施的感測器，可到 700–800 公尺，接近一英里。

**只用一個感測器的缺點** [▶ 07:30](https://youtu.be/j0LGkdKtKaY?t=450)：範圍有限、視野有限、距離估計精度有問題、有**誤報**（false positive）和**漏報**（false negative）。誤報的例子：什麼都沒有，系統卻煞車——因為感測器看到某種假象。

**多感測器的好處**：分類更好、偵測更準、狀態估計更好、更穩健、**可用性**更高（一個感測器壞了還有 B 計畫、C 計畫），甚至「看到轉角後面」。

---

## 2. 融合的四種分類法

[▶ 09:25](https://youtu.be/j0LGkdKtKaY?t=565)

### (1) 資料相關（data-related）

[▶ 09:53](https://youtu.be/j0LGkdKtKaY?t=593)

真實資料的問題：**不完美**（imperfect，雜訊、偏差、解析度有限）、資料之間有**相關性**、**不一致**（inconsistency：互相衝突、離群值、順序錯亂）、不同感測器之間的**差異**（disparity）。

- 例如不同感測器的時間戳要對好，避免用到錯的資料。
- 【口頭】量測不是「到前車 35 公尺」就結束了，還要問：這筆資料多可信？不確定性、模糊性（vagueness）、歧義（ambiguity）、不完整（incompleteness）。

### (2) 融合層級（fusion level）

[▶ 11:46](https://youtu.be/j0LGkdKtKaY?t=706)

| 層級 | 融合什麼 | 課本用語 |
|---|---|---|
| 訊號層 | 原始資料（raw data） | 早期融合（early fusion） |
| 特徵層 | 前處理後的特徵 | 中期融合（mid fusion） |
| 決策／物件層 | 已判斷好的物件清單（object list）：這是車、卡車、腳踏車 | 晚期融合（late fusion） |

**哪個最好？** [▶ 12:25](https://youtu.be/j0LGkdKtKaY?t=745)

- 資訊理論的角度：越低層越好，原始資料包含全部資訊。
- 實務角度：汽車產業有車廠（OEM）和一階供應商（Tier 1）。車廠希望融合模組可以換供應商（Magna、Denso、Continental、Bosch），所以在**高層**有明確介面比較好換。

### (3) 融合類別（fusion class）

[▶ 13:03](https://youtu.be/j0LGkdKtKaY?t=783)

- **競爭式**（competitive）：兩個感測器量同一件事（冗餘）。目的是**失效仍可運作**（fail-operational）：一個壞了另一個接手，或多數決。
- **互補式**（complementary）：例如光達和雷達一起估距離，各自補對方看不到的部分。
- **合作式**（cooperative）：單一感測器做不到、需要第二個來源才能得到資訊，例如立體視覺的三角測量。

【課本補充】§15.1 的合作式例子：單眼視覺只有搭配慣性感測才能得到真實尺度。

### (4) 架構（architectural）

[▶ 14:11](https://youtu.be/j0LGkdKtKaY?t=851)

偏硬體實作：**集中式**（centralized）、**分散式**（decentralized）、**分布式**（distributed）。分散／分布式用不同的控制單元（或至少不同核心），可以做到**失效靜默**（fail-silent）。各有優缺點，但從失效仍可運作、符合功能安全標準 **ISO 26262** 的角度，分布式架構較合理。

【課本補充】§15.1：集中式統計效率最高，但吃頻寬、有單點故障；分散式每個子系統跑本地估計器、傳摘要（例如帶共變異數的軌跡），但會有交叉相關的問題；分布式由同儕在通訊網路上交換信念並求共識，適合 V2X 和多機器人。

---

## 3. 貝氏觀點

[▶ 15:12](https://youtu.be/j0LGkdKtKaY?t=912)

用貝氏定律的好處：能直覺地把**先驗**（prior）和**量測**結合，全部用機率密度函數處理——每個東西都當作隨機變數。

【口頭】講者的看法：一旦去算**最大後驗**（MAP）或**最大概似**估計，就變成一個最佳化問題（一階導數為零、二階導數判斷極大極小），「已經離開貝氏的框架」。只要一直把所有東西當隨機變數處理，就留在框架裡。好處是拿到完整的**後驗分布**後可以算任何統計量：眾數、條件平均、邊際分布、信心程度——比直接跑 Gauss–Newton 型最佳化得到更多資訊。

卡爾曼濾波器及其變形都屬於這個貝氏框架。

【課本補充】§15.2 的通式：若各感測器的量測在給定狀態下條件獨立，

$$
p\left( x_t \mid Z_t \right) \propto p(x_t)\prod_{i=1}^{m} p\left( z_t^{(i)} \mid x_t \right)
$$

不獨立時，要嘛建出聯合概似（含交叉共變異數），要嘛用保守的融合法。

---

## 4. 最簡單的例子：融合兩個高斯量測

### 4.1 問題設定

[▶ 17:25](https://youtu.be/j0LGkdKtKaY?t=1045)

- 兩個感測器，要量到 $n$ 個物體的距離；先取 $n = 1$。
- 兩個感測器**視野相同**。
- 感測器 1 比較好（比較貴、精度高），感測器 2 比較便宜或比較舊：$\sigma_1 < \sigma_2$。
- 兩個量測都是一維高斯：

$$
d_1(x) = \frac{1}{\sqrt{2\pi}\,\sigma_1}\exp\left( -\frac{(x - \mu_1)^2}{2\sigma_1^2} \right),\qquad
d_2(x) = \frac{1}{\sqrt{2\pi}\,\sigma_2}\exp\left( -\frac{(x - \mu_2)^2}{2\sigma_2^2} \right)
$$

**問題** [▶ 20:14](https://youtu.be/j0LGkdKtKaY?t=1214)：融合後的變異數是接近 $\sigma_1^2$？還是比 $\sigma_1^2$ 更小？

### 4.2 推導：配方

[▶ 20:42](https://youtu.be/j0LGkdKtKaY?t=1242)

融合 = 把兩個分布相乘：

$$
d_1(x)\,d_2(x) = \frac{1}{2\pi\sigma_1\sigma_2}\exp\left( -\frac12 E(x) \right),\qquad
E(x) = \frac{(x - \mu_1)^2}{\sigma_1^2} + \frac{(x - \mu_2)^2}{\sigma_2^2}
$$

前面的係數和 $x$ 無關。只看指數 $E(x)$（講者說是「基本的數學」，只給提示；以下把每一步寫完整）：

**步驟 1：展開並通分。**

$$
E(x) = \frac{\sigma_2^2 (x - \mu_1)^2 + \sigma_1^2 (x - \mu_2)^2}{\sigma_1^2\sigma_2^2}
= \frac{(\sigma_1^2 + \sigma_2^2)\,x^2 - 2\left( \sigma_2^2\mu_1 + \sigma_1^2\mu_2 \right)x + \left( \sigma_2^2\mu_1^2 + \sigma_1^2\mu_2^2 \right)}{\sigma_1^2\sigma_2^2}
$$

**步驟 2：分子分母同除以 $\sigma_1^2 + \sigma_2^2$**（講者說的「技巧」，沒有加新資訊）：

$$
E(x) = \frac{x^2 - 2\mu x + \dfrac{\sigma_2^2\mu_1^2 + \sigma_1^2\mu_2^2}{\sigma_1^2 + \sigma_2^2}}{\sigma^2},
\qquad
\mu := \frac{\sigma_2^2\mu_1 + \sigma_1^2\mu_2}{\sigma_1^2 + \sigma_2^2},\quad
\sigma^2 := \frac{\sigma_1^2\sigma_2^2}{\sigma_1^2 + \sigma_2^2}
$$

**步驟 3：加一項再減一項，湊成完全平方**（$x^2 - 2\mu x$ 缺 $\mu^2$）：

$$
E(x) = \frac{(x - \mu)^2}{\sigma^2} + \underbrace{\frac{1}{\sigma^2}\left( \frac{\sigma_2^2\mu_1^2 + \sigma_1^2\mu_2^2}{\sigma_1^2 + \sigma_2^2} - \mu^2 \right)}_{s\ (\text{和 } x \text{ 無關})}
$$

**步驟 4：把和 $x$ 無關的部分全收進常數 $C$。**

$$
d_1(x)\,d_2(x) = C\exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
$$

這就是一個平均 $\mu$、變異數 $\sigma^2$ 的高斯（差一個常數倍）。

補充：把 $s$ 算出來：$s = \dfrac{(\mu_1 - \mu_2)^2}{\sigma_1^2 + \sigma_2^2}$。它衡量兩個量測有多不一致——這也就是兩個量測差值的馬氏距離（第 16 集）。（這行**不是逐字稿內容**，是依上面的式子直接代數化簡得到的。）

### 4.3 結論：融合後比最好的感測器還準

[▶ 25:45](https://youtu.be/j0LGkdKtKaY?t=1545)

$$
\mu = \frac{\sigma_2^2}{\sigma_1^2 + \sigma_2^2}\,\mu_1 + \frac{\sigma_1^2}{\sigma_1^2 + \sigma_2^2}\,\mu_2,
\qquad
\frac{1}{\sigma^2} = \frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2}
$$

- **平均**：按變異數加權——比較準的感測器（$\sigma_1$ 小）權重比較大。
- **變異數**：$\sigma^2 < \min\left( \sigma_1^2, \sigma_2^2 \right)$。

圖上：藍色（感測器 1）窄、紅色（感測器 2）寬，融合後的黃色**比藍色還窄**。也就是說，**就算加進一個比較差的感測器，整體不確定性仍然下降**。

**為什麼 $\sigma^2 < \sigma_1^2$**：$\sigma^2 = \sigma_1^2 \cdot \dfrac{\sigma_2^2}{\sigma_1^2 + \sigma_2^2}$，而後面那個分數小於 1。

### 4.4 和算術平均、中位數、並聯電阻的比較

[▶ 27:30](https://youtu.be/j0LGkdKtKaY?t=1650)

**算術平均是最簡單的融合**：量到牆的距離兩次，取 $(d_1 + d_2)/2$；量室溫 10 次取平均。它其實也在融合 $d_1$ 和 $d_2$，只是**權重一樣**、沒用到變異數，「不太聰明」。

- 問題：爛資料和好資料權重一樣 → 對**離群值**不穩健。
- 【口頭】[▶ 29:34](https://youtu.be/j0LGkdKtKaY?t=1774) 最簡單的**穩健估計**（robust estimation）是改用**中位數**（median），它能處理離群值。

**最重要的結論**：融合時各感測器的權重由**變異數**決定，所以變異數要認真對待。

**並聯電阻類比** [▶ 30:27](https://youtu.be/j0LGkdKtKaY?t=1827)：兩個電阻 $R_1$、$R_2$ 並聯，

$$
\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}\quad\Longrightarrow\quad R = \frac{R_1 R_2}{R_1 + R_2}
$$

和融合後的變異數形式完全一樣。大家都知道並聯總電阻**小於最小的那個電阻**（例：$R_1 = 1\,\mathrm{k\Omega}$、$R_2 = 2\,\mathrm{k\Omega}$ → $R < 1\,\mathrm{k\Omega}$）；變異數也一樣，融合後小於最好的感測器。

【課本補充】§15.2.1 的**資訊形式**（information form）把這件事推廣到多維：定義資訊矩陣 $Y = \Sigma^{-1}$，每個獨立量測貢獻 $\Delta Y^{(i)} = C^{(i)\top}(Q^{(i)})^{-1}C^{(i)}$，融合就是**相加**。這正是「變異數的倒數相加」的矩陣版本。

---

## 5. 卡爾曼濾波器回顧

[▶ 33:00](https://youtu.be/j0LGkdKtKaY?t=1980)

KF 非常適合做融合。

### 5.1 三個假設

1. **線性動態** [▶ 33:27](https://youtu.be/j0LGkdKtKaY?t=2007)：
   $x_t = A_t x_{t-1} + B_t u_t + \varepsilon_t$，$\varepsilon_t$ 獨立同分布、零平均高斯、共變異數 $R_t$（可隨時間變）。
   線性系統的高斯輸入仍是高斯輸出，所以 $p(x_t \mid u_t, x_{t-1})$ 是高斯；非線性才會出問題。
2. **線性量測模型** [▶ 35:14](https://youtu.be/j0LGkdKtKaY?t=2114)：
   $z_t = C_t x_t + \delta_t$，$\delta_t$ 零平均高斯、共變異數 $Q_t$。
   $C_t$ 就是**感測器模型**——光達模型、雷達模型、攝影機模型都放這裡。
3. **初始信念是高斯** [▶ 37:27](https://youtu.be/j0LGkdKtKaY?t=2247)。（講者說「零平均」；一般來說平均可以是任意 $\mu_0$。）

三個假設保證後驗信念 $bel(x_t) = \mathcal N(\mu_t, \Sigma_t)$。

【口頭】[▶ 36:13](https://youtu.be/j0LGkdKtKaY?t=2173) Kalman 的原始想法是**新息序列**（innovation sequence）：量測和模型預測的差。每一刻要決定「比較相信量測還是比較相信模型」。所以找一個好的感測器模型 $C$ 是要花腦力的：模型差，KF 就沒什麼意義；量測差也一樣。

【口頭】[▶ 38:22](https://youtu.be/j0LGkdKtKaY?t=2302) 現實很少線性，第一步通常是線性化；但非常非線性時，線性化會「搞得一團亂」——所以才有 UKF、粒子濾波器，或用 Markov chain Monte Carlo 直接從後驗抽樣。

### 5.2 只能處理單一假設

[▶ 39:09](https://youtu.be/j0LGkdKtKaY?t=2349)

KF 只能處理**單峰**分布（單一假設）。一個物體沒問題；兩個物體要兩個 KF；$n$ 個物體要 $n$ 個 KF。分布有好幾個峰時，每個峰都要一個模式追蹤；或改用粒子濾波、MCMC。

實車周圍有很多動態物體（例如兩個行人加一台車），**資料關聯**（data association）問題——哪個量測屬於哪個物體——就變得很關鍵。

### 5.3 跑濾波器之前：配準與時間同步

[▶ 40:29](https://youtu.be/j0LGkdKtKaY?t=2429)

拿到感測器資料就直接跑 KF 是太天真了。之前要先處理：

- **配準問題**（registration）／空間對齊：光達、雷達、攝影機裝在車上不同位置，座標系不同。
- **時間對齊**（temporal alignment）：每個感測器的訊號處理流程不同、各有自己的時鐘，容易把不同時刻的資料融在一起。車上有沒有全域時間？基礎設施傳來的外部資料怎麼對時？
- **偏差**（bias），見第 7 節。

【口頭】在 Python 裡跑濾波器時這些都不明顯；但在有**硬即時**（hard real-time）需求的真實硬體上馬上會遇到。光是時空對齊和資料關聯「就可以講一堂課，甚至半門課」。

【課本補充】§15.3.1：小的外參誤差可線性化成 $z \approx h(\bar T x) + J_T\eta + \delta$。兩種處理：把外參當作「已知但不確定」，量測共變異數加上 $J_T\Sigma_T J_T^\top$；或把外參放進狀態、給它慢速隨機漫步，讓濾波器線上學。

### 5.4 預測與修正

[▶ 43:05](https://youtu.be/j0LGkdKtKaY?t=2585)

輸入：上一步的信念 $(\mu_{t-1}, \Sigma_{t-1})$、控制 $u_t$、量測 $z_t$。

1. **預測**（傳播密度，不用量測）：
   $\bar\mu_t = A_t\mu_{t-1} + B_t u_t$，$\bar\Sigma_t = A_t\Sigma_{t-1}A_t^\top + R_t$。
2. **修正**：
   $K_t = \bar\Sigma_t C_t^\top\left( C_t\bar\Sigma_t C_t^\top + Q_t \right)^{-1}$，
   $\mu_t = \bar\mu_t + K_t\left( z_t - C_t\bar\mu_t \right)$，
   $\Sigma_t = (I - K_t C_t)\bar\Sigma_t$。

【口頭】卡爾曼增益縮放新息：（純量直覺）增益接近 1 → 相信量測；接近 0 → 相信模型。每一步都重新算增益，重新評估量測好不好。

【課堂討論】[▶ 46:31](https://youtu.be/j0LGkdKtKaY?t=2791) 講者問：大家都實作過 KF 了嗎？（學生示意有）講者：「很好。」

---

## 6. 進階例子：用 KF 融合光達、GPS、IMU 估計位置

[▶ 46:35](https://youtu.be/j0LGkdKtKaY?t=2795)

【口頭】週五的 Autoware 實作也會用不同來源做融合。

### 6.1 為什麼不能只靠 IMU

[▶ 47:26](https://youtu.be/j0LGkdKtKaY?t=2846)

- IMU 量加速度，積分一次得速度、兩次得位置。
- 兩次積分會讓偏差隨時間累積。【口頭】講者說他們實測過：只靠 IMU 大概撐 10–20 秒，之後就「不知道跑到哪去了」。
- GPS 有時很差或沒訊號。
- 位姿估計是**安全關鍵**的，沒有一定精度就不該自動駕駛 → 需要 GPS、光達、IMU 的冗餘系統。

### 6.2 模型

[▶ 48:48](https://youtu.be/j0LGkdKtKaY?t=2928)

狀態：位置、速度、加速度 $x_t = (p_t, v_t, a_t)^\top$。取樣時間 $T_s$：

$$
\begin{bmatrix} p_{t+1} \\ v_{t+1} \\ a_{t+1} \end{bmatrix}
= \underbrace{\begin{bmatrix} 1 & T_s & \tfrac12 T_s^2 \\ 0 & 1 & T_s \\ 0 & 0 & 1 \end{bmatrix}}_{A}
\begin{bmatrix} p_t \\ v_t \\ a_t \end{bmatrix} + \varepsilon_t,
\qquad \varepsilon_t \sim \mathcal N(0, R_t)
$$

【口頭】講者稱它為「單軌模型」（single track model），說它對**縱向**動態夠用；做**橫向**控制就要考慮輪胎模型和更完整的動態。

> 以下**不是逐字稿內容**，是依式子本身推論的：上面這個 $A$ 其實是一維的**等加速度運動學模型**（課本例 15.2.2 也這麼稱呼），沒有用到單軌（自行車）模型的轉向與側滑。講者應是指「在縱向上用簡化的單軌模型」。

### 6.3 初值與雜訊共變異數怎麼設

**初始狀態** [▶ 51:45](https://youtu.be/j0LGkdKtKaY?t=3105)：沒有通用規則。

- 有歷史估計（上一次的狀態）就用它。
- KF 收斂很快的話，直接設 0 通常可以；但有時不收斂，就要想辦法給更接近答案的起點（例如用 GPS 資料初始化）。

**初始共變異數 $\Sigma_0$、$R$、$Q$** [▶ 52:45](https://youtu.be/j0LGkdKtKaY?t=3165)：常被當成調參。

- 小的值代表信心高：過程雜訊 $R$ 小 → 相信模型；量測雜訊 $Q$ 小 → 相信量測。
- 【口頭】警告：很多應用把量測共變異數設得很大、過程共變異數設得很小，等於**偏袒模型**——只相信單軌模型、不相信量測。
- 【口頭】**不要只把它們當調參**。過程雜訊藏在系統動態裡量不到；但**量測雜訊可以量**：有真實硬體時，對感測器多次取樣，算出真實的量測共變異數 $Q_t$，用真的分布。調太多 $Q$、$R$「會失去物理意義」。

### 6.4 情況一：光達＋IMU

[▶ 50:30](https://youtu.be/j0LGkdKtKaY?t=3030)

- 光達量位置（精度低）；IMU 量加速度。
- 量測模型：
$$
\begin{bmatrix} z_{\text{lidar}} \\ z_{\text{imu}} \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}
\begin{bmatrix} p_t \\ v_t \\ a_t \end{bmatrix} + \delta_t,
\qquad Q_t = \operatorname{diag}\left( \sigma_{\text{lidar}}^2,\ \sigma_{\text{imu}}^2 \right)
$$
- 用合成資料（真值加零平均高斯雜訊）。【口頭】MATLAB 和 Python 程式碼會由首席助教 Boris 分享（第 18 集證實他是 lead CA）。

**結果** [▶ 56:42](https://youtu.be/j0LGkdKtKaY?t=3402)：

- **位置**：估計的變異數比光達小（符合第 4 節），但估計還是不太好；只靠光達估位置不夠。
- **速度**：估計相當好，但在靜止段有偏移（offset）。【口頭】KF 處理動態比處理靜止好。
- **加速度**：IMU 量測（綠）雜訊很大；KF 估計（紅）仍有點雜。
- 講者：「老實說，我們對這結果不滿意。」

【Q&A】[▶ 60:02](https://youtu.be/j0LGkdKtKaY?t=3602) 學生問：為什麼速度估計看不到雜訊？
講者：沒有感測器直接量速度。光達量位置（從點雲）、IMU 量加速度，速度純粹是透過模型推出來的估計；而模型假設速度方向的雜訊不大，所以看起來很平滑。

### 6.5 情況二：再加 GPS

[▶ 60:57](https://youtu.be/j0LGkdKtKaY?t=3657)

- GPS 是**最好**的感測器（不確定性最小），光達仍是最差的。
- 對 KF 來說加一個感測器很簡單：**狀態方程不變**（還是估位置、速度、加速度），只有量測方程多一列：

$$
\begin{bmatrix} z_{\text{lidar}} \\ z_{\text{gps}} \\ z_{\text{imu}} \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} x_t + \delta_t,
\qquad Q_t = \operatorname{diag}\left( \sigma_{\text{lidar}}^2,\ \sigma_{\text{gps}}^2,\ \sigma_{\text{imu}}^2 \right)
$$

【口頭】[▶ 62:56](https://youtu.be/j0LGkdKtKaY?t=3776) 實務上用**差分 GPS**（differential GPS, D-GPS），精度可到約 5 公分；一般車上的 GPS 沒這麼好。

**結果** [▶ 63:51](https://youtu.be/j0LGkdKtKaY?t=3831)：估計（紅）和真值很接近，看起來幾乎和 GPS 一樣。

**那為什麼還要 KF？**

1. GPS 失效時還有後援。
2. 放大看：紅線（估計）的變異數**比黃線（GPS）還小**——正如第 4 節證明的，融合後的變異數一定小於最好感測器的變異數。

---

## 7. 偏差、有色雜訊、故障偵測

[▶ 66:41](https://youtu.be/j0LGkdKtKaY?t=4001)

【課堂討論】講者問：KF 能處理**偏差**（bias）嗎？例如 IMU 有偏差，KF 能把它算出來嗎？（學生回答聽不清楚）講者：不行，這是個問題。

**誤差的兩類** [▶ 67:24](https://youtu.be/j0LGkdKtKaY?t=4044)：

- **隨機誤差**：和變異數有關，KF 能處理。
- **系統誤差**：可重現，每次正負號都一樣，通常要校正。偏差若是常數比較好校；隨時間甚至每一步都在變就比較難。

**另一個問題：有色雜訊**（colored noise）[▶ 68:22](https://youtu.be/j0LGkdKtKaY?t=4102)：課堂上總假設線性系統＋高斯白雜訊，但實際的分布常有**厚尾**（fat tails）。可以多次取樣做直方圖擬合，看它比較像高斯、$\chi^2$ 還是 Student-$t$。

**大招：擴增狀態** [▶ 69:29](https://youtu.be/j0LGkdKtKaY?t=4169)

> 「在狀態估計的世界裡，處理不了的東西，就把它跟其他參數一起估計。」

- 狀態向量多加一列：IMU 的偏差 $b$，一起估計。
- 偏差隨時間變化的估計值，還能用來做**狀態監測**（condition monitoring）：知道感測器正在劣化。
- 有色的過程雜訊、量測雜訊也一樣：把雜訊參數（平均、變異數，或其他分布的參數）放進狀態一起估。

【課本補充】§15.2.1 的寫法：加性偏差 $b_t = b_{t-1} + w_t$（隨機漫步），擴增狀態 $x' = (x, b)$，量測 $z_t = Cx_t + b_t + \delta_t$ 對 $x'$ 是線性的，量測矩陣為 $\begin{bmatrix} C & I \end{bmatrix}$。這讓濾波器線上學偏差，不會把偏差誤當成狀態誤差。

**預白化** [▶ 70:40](https://youtu.be/j0LGkdKtKaY?t=4240)：另一招是**預白化**（pre-whitening），也叫**成形濾波器**（shaping filter）：有色雜訊進去、白雜訊出來。

**故障偵測** [▶ 71:04](https://youtu.be/j0LGkdKtKaY?t=4264)：

- 自駕車除了估計周圍物體、做路徑規劃，還要能**偵測自己系統的錯誤**、監控整體表現。
- KF 在這方面很好用：監看**新息序列**（量測和感測器模型預測的差），設一個門檻，就能發現感測器故障或完全不能用了；致動器也一樣。
- 【口頭】現在很多研究轉向這部分。

【課本補充】§15.2.1：**正規化新息平方**（Normalized Innovation Squared, NIS）$\tilde z_t^\top S_t^{-1}\tilde z_t$ 在模型正確時服從 $\chi^2$ 分布，可用來閘控離群值、偵測故障、監控一致性——和第 16 集的馬氏距離是同一個量。

---

## 8. 總結

[▶ 72:55](https://youtu.be/j0LGkdKtKaY?t=4375)

1. 多感測器融合的好處。
2. 四種分類法：資料、層級（原始資料 vs 物件清單）、類別（互補、合作、競爭）、架構。
3. 融合兩個高斯 → 融合後變異數**小於最好的感測器**（可證明）。
4. 進階例子：KF 融合不同來源。
5. 共變異數不只是調參：過程雜訊量不到，但量測雜訊在實驗室或路上可以量出來，就用真的值。

【口頭】融合的好處不只是降低變異數：感測器會故障、會給錯資料，也不是隨時都可用——想想隧道和壞天氣。「加州天氣好，但奧地利有阿爾卑斯山、很多隧道，天氣一年到頭在變。」工程師要記得系統不只在矽谷跑，而是會被部署到全世界。

---

## 9. 一頁速查表

### 兩個高斯的融合

$$
\mu = \frac{\sigma_2^2\mu_1 + \sigma_1^2\mu_2}{\sigma_1^2 + \sigma_2^2},\qquad
\frac{1}{\sigma^2} = \frac{1}{\sigma_1^2} + \frac{1}{\sigma_2^2}\ \ \Longrightarrow\ \ \sigma^2 < \min(\sigma_1^2, \sigma_2^2)
$$

- **關鍵一步**：兩個指數相加 $\frac{(x-\mu_1)^2}{\sigma_1^2} + \frac{(x-\mu_2)^2}{\sigma_2^2}$，分子分母同除 $\sigma_1^2 + \sigma_2^2$ 後配方成 $\frac{(x-\mu)^2}{\sigma^2} + s$，$s$ 與 $x$ 無關。
- 類比：並聯電阻 $R = R_1R_2/(R_1 + R_2) < \min(R_1, R_2)$。
- 算術平均 = 等權重融合，不穩健；中位數是最簡單的穩健估計。

### 卡爾曼濾波器（講者記號：$R$ 過程、$Q$ 量測）

$$
\bar\mu_t = A\mu_{t-1} + Bu_t,\quad \bar\Sigma_t = A\Sigma_{t-1}A^\top + R_t;\qquad
K_t = \bar\Sigma_t C^\top\left( C\bar\Sigma_t C^\top + Q_t \right)^{-1},\quad
\mu_t = \bar\mu_t + K_t(z_t - C\bar\mu_t),\quad \Sigma_t = (I - K_tC)\bar\Sigma_t
$$

- 多感測器：把量測**堆疊**，$C$ 每個感測器一列（或一塊），$Q_t$ 是對角塊。加感測器只改 $C$、$Q$，不改狀態方程。
- 只能處理單峰；$n$ 個物體要 $n$ 個 KF ＋資料關聯。

### 位置融合例子

$$
A = \begin{bmatrix} 1 & T_s & \tfrac12T_s^2 \\ 0 & 1 & T_s \\ 0 & 0 & 1 \end{bmatrix},\qquad
C_{\text{lidar+gps+imu}} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

### 實務清單

- 跑 KF 前：空間配準、時間同步、偏差。
- $Q$（量測雜訊）用實測，不要亂調；$R$ 小 = 偏袒模型。
- 偏差、有色雜訊 → **擴增狀態**一起估；或預白化。
- 新息超過門檻 → 感測器／致動器故障。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 感知用的攝影機、光達資料 | 第 18 集現代電腦視覺（深度學習） |
| 擴增狀態（偏差） | 對照第 16 集 EKF SLAM 擴增地標 |
| 融合層級（物件清單）、多物體追蹤 | 期末專題、Autoware 實作 |
| 系統監控、故障時切換模式 | 第 19 集狀態機 |
| 粒子濾波（多峰） | 第 21 集粒子濾波 SLAM |

---

## 附：本集一句話總結

> **融合就是把多個感測器的機率分布相乘：兩個高斯相乘後的平均按變異數加權、變異數像並聯電阻一樣比最好的那個還小；卡爾曼濾波器把這件事做成遞迴，加一個感測器只要在量測矩陣多一列。實務上更難的是跑濾波器之前的時空對齊、量測雜訊要實測而非亂調，以及「處理不了的偏差和雜訊，就放進狀態一起估」。**

---

## ⚠️ 待確認清單

1. 上課日期待補（講者說「下一堂在週四」）。
2. 講者姓名逐字稿沒有；只知道來自奧地利格拉茲的大學，推測是 Daniel Watzenig（TU Graz），未確認。
3. [▶ 00:54](https://youtu.be/j0LGkdKtKaY?t=54) 介紹講者的人（字幕「Sabor」）名字可能聽錯。（分享程式碼的「Boris」已由第 18 集確認是首席助教。）

---

*筆記依據客座講者（推斷：TU Graz）「Stanford AA274A Principles of Robotic Autonomy（2019 秋）」Lecture 17 錄影逐字稿（Whisper `medium.en`，1:16:23）與《Principles of Robot Autonomy》第 15 章整理。*
