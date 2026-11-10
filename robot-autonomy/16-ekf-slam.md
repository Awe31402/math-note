---
course: Stanford AA274A Principles of Robotic Autonomy（2019 秋）
episode: 16
lecture: Lecture 16
date: 待補（推斷為週三：老師說「週五出差」）
video: https://youtu.be/fkug1jGSgzU
notes: 《Principles of Robot Autonomy》§13.5.2–13.6（書頁 337–340，PDF 頁 339–342）、§14.4–14.5（書頁 357–369，PDF 頁 359–371）
---

# 第 16 集 · Lecture 16：對應變數估計、Monte Carlo 定位與 EKF SLAM [▶ 影片](https://youtu.be/fkug1jGSgzU)

← 上一集：[15-ekf-localization](15-ekf-localization.md) ｜ [總目錄](README.md) ｜ 下一集：[17-multi-sensor-fusion](17-multi-sensor-fusion.md) →

> **課程**：Stanford AA274A Principles of Robotic Autonomy I，2019 秋 — 第 16 集
> **講者**：Marco Pavone（推斷：展示「自己的研究」——小行星上跳躍式探測器的 SLAM，並說週五出差）
> **來源**：YouTube 錄影逐字稿（1:18:58，Whisper `medium.en` 轉錄）＋《Principles of Robot Autonomy》第 13、14 章
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯，依課本修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單
>
> **記號注意**：同第 14、15 集，老師用 $R_t$ 表示**過程（運動）雜訊**、$Q_t$ 表示**量測雜訊**；課本第 13、14 章剛好相反（$Q_t$ 過程、$R_t$ 量測）。本筆記照老師的記號。
>
> **常見聽錯**（⚠️ 逐字稿缺字，以下統一修正，不再逐一標）：「melanobis / Malanovitz」→ **Mahalanobis**；「EK epsilon / ZLAM / EKD epsilon」→ **EKF SLAM / SLAM**；「lemma j」→ landmark j；「multi-apothesis」→ multi-hypothesis；「lighter sensor」→ lidar；「future-based map」→ feature-based map；「sampling with a placement」→ with replacement；「try rejection / trial rejection」→ outlier rejection。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 對應變數從哪裡來：最大概似估計](#1-對應變數從哪裡來最大概似估計)
  - [1.1 想法與代價](#11-想法與代價)
  - [1.2 一次一個量測的近似](#12-一次一個量測的近似)
  - [1.3 用全機率定理算出量測的分布](#13-用全機率定理算出量測的分布)
  - [1.4 EKF 定位（未知對應）演算法](#14-ekf-定位未知對應演算法)
- [2. 馬氏距離（Mahalanobis distance）](#2-馬氏距離mahalanobis-distance)
- [3. Monte Carlo 定位（MCL）](#3-monte-carlo-定位mcl)
- [4. SLAM 問題](#4-slam-問題)
  - [4.1 定義：線上 SLAM 與完整 SLAM](#41-定義線上-slam-與完整-slam)
  - [4.2 為什麼 SLAM 難](#42-為什麼-slam-難)
  - [4.3 路徑誤差和地圖誤差是相關的](#43-路徑誤差和地圖誤差是相關的)
- [5. EKF SLAM（已知對應）](#5-ekf-slam已知對應)
  - [5.1 擴增狀態向量](#51-擴增狀態向量)
  - [5.2 狀態轉移模型](#52-狀態轉移模型)
  - [5.3 量測模型與稀疏 Jacobian](#53-量測模型與稀疏-jacobian)
  - [5.4 初始化](#54-初始化)
  - [5.5 演算法](#55-演算法)
  - [5.6 例子：迴圈閉合讓所有不確定性一起縮小](#56-例子迴圈閉合讓所有不確定性一起縮小)
- [6. EKF SLAM（未知對應）預告](#6-ekf-slam未知對應預告)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集做 EKF 定位時有一個不實際的假設：**對應變數（correspondence variable）是已知的**——有個神諭告訴我們每個量測來自哪個地標。這堂課把這個假設拿掉，再把「地圖已知」這個假設也拿掉。

1. 用**最大概似估計**（maximum likelihood estimation, MLE）估對應變數；另一個等價的看法是**馬氏距離**。
2. （研究所 AA274A 學生才要負責）把粒子濾波器套到定位上：**Monte Carlo 定位**。
3. 地圖也不知道 → **同時定位與建圖**（Simultaneous Localization and Mapping, SLAM），並用 EKF 解：**EKF SLAM**。

| 課堂主題 | 課本對應 |
|---|---|
| 未知對應的 EKF 定位 | §13.5.2（書頁 337–339） |
| Monte Carlo 定位 | §13.6、演算法 13.4（書頁 339–340） |
| SLAM 的數學基礎 | §14.4（書頁 357–362） |
| EKF SLAM（已知／未知對應） | §14.5、§14.5.1、§14.5.2（書頁 362–369） |

【口頭】老師指定的閱讀是 *Probabilistic Robotics*（Thrun、Burgard、Fox）第 8 章和第 10 章 [▶ 42:57](https://youtu.be/fkug1jGSgzU?t=2577)。（⚠️ 逐字稿缺字：字幕「Sebastian Stern, Barger than Dieter Fox」→ Sebastian Thrun、Wolfram Burgard、Dieter Fox。）

---

## 1. 對應變數從哪裡來：最大概似估計

### 1.1 想法與代價

[▶ 01:06](https://youtu.be/fkug1jGSgzU?t=66)

回顧記號：$c_t^i = j$ 表示「時間 $t$ 的第 $i$ 個量測 $z_t^i$ 來自地圖中第 $j$ 個地標」。

現實中沒人告訴我們 $c_t^i$，要自己估。最基本的做法：

1. 先找出**最能解釋資料**的對應值（最大概似）。
2. 然後**當作它是對的**，照已知對應的 EKF 定位往下做。

$$
\hat c_t = \arg\max_{c_t}\ p\left( z_t \mid c_{1:t},\ m,\ z_{1:t-1},\ u_{1:t} \right)
$$

其中 $m$ 是（已知的）地圖，$u_{1:t}$ 是控制歷史，$z_{1:t-1}$ 是量測歷史，$c_{1:t-1}$ 在之前的步驟已經決定好了，要選的只有 $c_t$。

**代價**：一旦選錯就**整個認了**，錯誤會一路帶到後面的時間步。所以這個方法好算，但比較**脆弱**（brittle）。補救方式：

- 加**離群值剔除**（outlier rejection）機制。
- 同時追蹤很多地標，少數幾個配錯也不致命。

【Q&A】[▶ 03:45](https://youtu.be/fkug1jGSgzU?t=225) 學生問：有沒有演算法是保留 $c_{1:t}$ 的機率分布、而不是只取一個值？
老師：這是最基本的版本。更進階的是**多假設**（multi-hypothesis）演算法：同時保留很多個定位假設，每個對應一條對應變數的歷史，再按機率混合。學生追問：這個版本只要配錯一個 $c$ 就會一直錯下去？老師：對，就是剛剛說的；但地標很多時，配錯一個影響有限，也可以再加剔除機制。

### 1.2 一次一個量測的近似

[▶ 05:43](https://youtu.be/fkug1jGSgzU?t=343)

困難：$z_t$ 其實是一整個向量（例如光達一次回傳一片點雲），每個分量 $z_t^i$ 都要配到某個地標。所有配法的數量**隨量測數指數成長**，直接算聯合的最大概似太貴。

常用近似：**每個量測分開做**最大概似。

$$
\hat c_t^i = \arg\max_{c_t^i}\ p\left( z_t^i \mid c_{1:t},\ m,\ z_{1:t-1},\ u_{1:t} \right)
$$

【口頭】老師的例子 [▶ 07:45](https://youtu.be/fkug1jGSgzU?t=465)：「這個量測若來自地標 1，觀察到它的機率是 0.3；若來自地標 2，是 0.5。」→ 配給地標 2。

### 1.3 用全機率定理算出量測的分布

[▶ 08:39](https://youtu.be/fkug1jGSgzU?t=519)

剩下的問題是把上面那個機率寫成解析形式。對狀態 $x_t$ 用**全機率定理**（law of total probability）：

$$
p\left( z_t^i \mid c_{1:t}, m, z_{1:t-1}, u_{1:t} \right)
= \int \underbrace{p\left( z_t^i \mid x_t, c_t^i, m \right)}_{\text{量測模型}}\ \underbrace{p\left( x_t \mid c_{1:t-1}, m, z_{1:t-1}, u_{1:t} \right)}_{\overline{bel}(x_t)\ \text{預測信念}}\ dx_t
$$

- 第一項是量測模型：高斯，平均 $h(x_t, j, m)$，共變異數 $Q_t$。
- 第二項是預測信念：在 EKF 裡永遠當作高斯 $\mathcal N(\bar\mu_t, \bar\Sigma_t)$。
- 兩個高斯相乘再積分還是高斯。（老師略過約一頁的代數推導，說「繁瑣但不複雜」。）線性化 $h$ 之後結果是：

$$
p\left( z_t^i \mid c_t^i = j, \dots \right) \approx \mathcal N\left( z_t^i;\ \hat z_t^j,\ S_t^j \right),\qquad
\hat z_t^j = h(\bar\mu_t, j, m),\qquad
S_t^j = H_t^j\,\bar\Sigma_t\,(H_t^j)^\top + Q_t
$$

**直覺** [▶ 11:25](https://youtu.be/fkug1jGSgzU?t=685)：量測的不確定性來自兩件事——

1. 我們不確定自己在哪 → 所以也不確定地標「應該」出現在哪（$H\bar\Sigma H^\top$）。
2. 量測本身有雜訊（$Q_t$）。

總變異數就是兩者相加。平均值是「如果狀態剛好等於最可能值 $\bar\mu_t$，我會量到什麼」。這兩個量（$\hat z$、$S$）本來在 EKF 定位裡就要算。

**怎麼選** [▶ 12:22](https://youtu.be/fkug1jGSgzU?t=742)：對每個可能的 $j$ 畫一個高斯（橫軸是量測值）。把實際量到的 $z_t^i$ 代進每個高斯，看哪個的機率密度最高，就選那個 $j$。

【課堂討論】老師畫了地標 1、2 兩個高斯，問該選哪個；學生答「2」，因為在 2 的高斯下，觀察到的量測值的密度比較高。

【Q&A】[▶ 14:17](https://youtu.be/fkug1jGSgzU?t=857) 學生問：這樣選出來的對應不一定是一對一（bijection），會不會兩個量測配到同一個地標？
老師：這不一定是錯的。例如一個很寬的障礙物，光達的兩道回波很可能都打在同一個物體上。

### 1.4 EKF 定位（未知對應）演算法

[▶ 15:04](https://youtu.be/fkug1jGSgzU?t=904)

**在解什麼**：跟上一集一樣用 EKF 追蹤姿態，但每個量測來自哪個地標要自己猜。

**步驟**：

1. **預測**（跟已知對應完全一樣——預測不用量測，所以對應變數不參與）：
   $\bar\mu_t = g(u_t, \mu_{t-1})$，$\bar\Sigma_t = G_t\Sigma_{t-1}G_t^\top + R_t$。
2. 對每個量測 $z_t^i$：
   1. 對**每個**地標 $k$，假設「$z_t^i$ 來自 $k$」，算預期量測 $\hat z_t^k = h(\bar\mu_t, k, m)$ 與不確定性 $S_t^k = H_t^k\bar\Sigma_t(H_t^k)^\top + Q_t$。
   2. 選讓資料最可能的 $j = \arg\max_k \mathcal N(z_t^i; \hat z_t^k, S_t^k)$（等價於選馬氏距離最小的，見第 2 節）。
   3. **認定**這個對應，照常更新：$K = \bar\Sigma_t (H_t^j)^\top (S_t^j)^{-1}$，$\bar\mu_t \leftarrow \bar\mu_t + K(z_t^i - \hat z_t^j)$，$\bar\Sigma_t \leftarrow (I - KH_t^j)\bar\Sigma_t$。
3. $\mu_t = \bar\mu_t$，$\Sigma_t = \bar\Sigma_t$。

跟已知對應的版本比，**唯一的差別是步驟 2.1–2.2**。

**什麼時候會失敗**：對應選錯就一路錯下去（沒有反悔機制）；地標長得很像、或不確定性大到好幾個高斯重疊時最容易選錯。

【口頭】[▶ 20:08](https://youtu.be/fkug1jGSgzU?t=1208) 例子：我看到一個回波，它是那張桌子還是那個講台？若配給桌子算出的機率比配給講台高，就配給桌子。

【口頭】[▶ 21:07](https://youtu.be/fkug1jGSgzU?t=1267) 整理成三個積木：(1) 用預測步驟往前推估計；(2) 用量測修正；(3) 為了能用量測修正，要先把量測配到地標。

【口頭】[▶ 21:42](https://youtu.be/fkug1jGSgzU?t=1302) 地標不一定要是點。作業會用**線**（更精確說是線段）當地標，一條線用 $(r, \alpha)$ 兩個參數表示，這就是量測。

---

## 2. 馬氏距離（Mahalanobis distance）

[▶ 22:19](https://youtu.be/fkug1jGSgzU?t=1339)

另一種配對方式：把量測配給**馬氏距離最小**的地標。

**概念**：有一個隨機變數，平均是 $\mu$，不確定性是一個橢圓。想問「某個值離期望值多遠」時，不該用歐氏距離，而該問「**離平均幾個 $\sigma$**」。

- 若某個方向很不確定（橢圓長軸）、另一個方向很確定（短軸），那麼長軸端點和短軸端點雖然歐氏距離不同，統計上都是「1 個 $\sigma$ 遠」，距離相同。
- 反過來，同樣歐氏距離的兩個觀測，落在不確定方向的那個比較「可能」，落在確定方向的那個比較「遠」。

**怎麼算** [▶ 25:35](https://youtu.be/fkug1jGSgzU?t=1535)：先算差，再用共變異數的反矩陣縮放：

$$
d_t^{ik} = \left( z_t^i - \hat z_t^k \right)^\top \left( S_t^k \right)^{-1} \left( z_t^i - \hat z_t^k \right)
$$

某軸很不確定 → $\sigma$ 大 → 除以大數得到小距離 → 統計上其實很近。老師自己說這個解釋「數學上很粗暴，但很實用」。

**用來配對**：對每個可能的對應 $k$ 算 $\hat z_t^k$、$S_t^k$，再算實際量測到每個預期量測的馬氏距離，選最小的。

【Q&A】[▶ 25:09](https://youtu.be/fkug1jGSgzU?t=1509) 學生問：橢圓上的點都是一樣的「確定程度」嗎？老師：對，都是離平均 1 個 $\sigma$。學生補充「大概 63% 機率落在裡面」，老師回「對」。

> 以下**不是逐字稿內容**，是依高斯分布的性質推論的：1 維高斯落在 $\pm 1\sigma$ 內的機率約 68%；但 **2 維**高斯落在 1-$\sigma$ 橢圓內的機率是 $1 - e^{-1/2} \approx 39\%$（因為 $d$ 服從自由度 2 的 $\chi^2$ 分布）。課堂上說的「63%」兩者都不是，應當作口語的大概說法。

【Q&A】[▶ 28:11](https://youtu.be/fkug1jGSgzU?t=1691) 學生問：馬氏距離是不是也算一種最大概似？
老師：非常相關，哲學一樣——都是選「最能解釋觀測」的對應。只是這裡「最能解釋」的意思是：實際觀測和「若 $i$ 對應 $j$ 時預期的觀測」之間的距離最小，而距離是用 $\sigma$ 量的。

【課本補充】課本 §13.5.2 指出兩者其實**等價**：高斯密度
$\mathcal N(z; \hat z, S) \propto |S|^{-1/2}\exp\left( -\tfrac12 d \right)$，
若忽略 $|S|$ 在不同 $k$ 之間的差異，最大化密度就等於最小化 $d$。課本還提到**驗證閘**（validation gate）：最小的 $d$ 仍超過門檻，就把量測當成「沒配到」（索引 $N+1$），不拿來更新。

【口頭】[▶ 29:07](https://youtu.be/fkug1jGSgzU?t=1747) 處理脆弱性的進階方法（超出本課範圍）：多假設追蹤濾波器，信念用**高斯混合**表示，每個高斯追蹤一串不同的配對決定；也可以不用 EKF，改用其他參數式濾波器。⚠️ 待確認：字幕說「such as EKF」，依上下文應是別的濾波器（推測是 UKF，unscented Kalman filter）。

---

## 3. Monte Carlo 定位（MCL）

[▶ 29:54](https://youtu.be/fkug1jGSgzU?t=1794)

【口頭】這一節只有研究所版（AA274A）要負責，大學部版（CS/AA174）不用。

前面都是**參數式**（parametric）方法：用高斯近似信念。另一條路是**非參數式**：用一群**粒子**（particle）表示信念，每個粒子是狀態的一個具體取值。把第 13 集的粒子濾波器套到定位上，就叫 **Monte Carlo 定位**（Monte Carlo Localization, MCL）。

好消息：EKF 套到定位很麻煩，粒子濾波器套到定位**非常簡單**——把狀態轉移模型和量測模型換成機器人的版本（並帶入地圖 $m$）就好。

**在解什麼**：已知地圖下估計姿態，信念可以是任意形狀（多峰也行）。

**步驟**（輸入：上一步的 $M$ 個粒子（通常約 1000 個）、$u_t$、$z_t$、$m$）：

1. 對每個粒子 $k$：
   1. **預測**：從 $p(x_t \mid x_{t-1}^{[k]}, u_t, m)$ 抽一個新粒子 $\bar x_t^{[k]}$。
   2. **權重**：$w_t^{[k]} = p(z_t \mid \bar x_t^{[k]}, m)$——若狀態真的是這個粒子，現在這個量測有多可能。
2. **重抽樣**（resampling）：抽 $M$ 次、**放回抽樣**（with replacement），每次抽到粒子 $k$ 的機率正比於 $w_t^{[k]}$。
3. 回傳新的粒子集合。

【口頭】[▶ 33:46](https://youtu.be/fkug1jGSgzU?t=2026) 因為是放回抽樣，可能一直抽到同一個粒子。例子：三個粒子分別代表「我面向這邊／那邊／另一邊」，量到的是一張桌子，只有一個粒子和它相容（機率 1），另兩個機率 0 → 新集合仍有三個粒子，但全是同一個重複三次。

【口頭】[▶ 34:55](https://youtu.be/fkug1jGSgzU?t=2095) 作業 4 第 3 題要實作 MCL「加一個小改良」：上面每次抽樣彼此**獨立**，運氣差時會一直抽到同一個粒子，可能讓濾波器發散；有更好的重抽樣方法。

> 以下**不是逐字稿內容**，是依粒子濾波器的標準做法推論的：這個改良很可能是**低變異重抽樣**（low-variance / systematic resampling）——只抽一個隨機數，然後用等間距的指標掃過累積權重，讓抽樣結果更貼近權重比例。⚠️ 待確認：逐字稿只說「用某個隨機過程做更好的重抽樣」，沒講名字。

【Q&A】[▶ 35:43](https://youtu.be/fkug1jGSgzU?t=2143) 學生問：地圖怎麼放進量測模型和狀態轉移模型？
老師：跟 EKF 完全一樣，上一集講過。例如狀態轉移：往前推的分布原本不知道有障礙物，把「不考慮地圖的轉移模型」乘上一個「這個狀態和地圖相不相容」的項，就把撞牆的狀態壓掉。

**優點**：概念上好實作、穩健，能處理**全域定位**、**位置追蹤**、**綁架機器人問題**，也能透過離群值剔除處理動態環境。

**缺點／注意** [▶ 37:00](https://youtu.be/fkug1jGSgzU?t=2220)：

- 演算法裡有 for 迴圈，粒子很多時若實作不小心會非常慢——要即時跑，實作很重要（作業會遇到）。
- 可以用更進階的重抽樣增加穩健性。
- **粒子匱乏**（particle starvation）[▶ 38:29](https://youtu.be/fkug1jGSgzU?t=2309)：某一輪運氣差，只剩一個粒子被複製 1000 次，粒子不夠表示信念。實務做法：偶爾在環境各處**隨機撒一些粒子**，對應「機器人可能被綁架」的想法，讓每個地方都保有一點殘餘機率。

**例子** [▶ 37:47](https://youtu.be/fkug1jGSgzU?t=2267)：機器人移動並得到視線（line-of-sight）量測。一開始粒子撒滿整個環境；依過去量測，有兩群粒子都相容；進到房間看見一張「另一處沒有」的桌子後，錯的那群在重抽樣時消失，最後粒子都集中在正確姿態附近。

【Q&A】[▶ 39:12](https://youtu.be/fkug1jGSgzU?t=2352) 學生問：環境對稱（例如上下兩間一模一樣的房間）怎麼辦？
老師：只靠量測確實無法分辨，所以信念**就該有兩個峰**，同時追蹤，直到有能分辨的量測。這正是粒子濾波器的強項；EKF 做不到——它只有一個大高斯，平均落在兩個峰中間，**保證是錯的位置**。所以 EKF 只適合位置追蹤，或初始估計已經不錯的情況；完全不知道在哪時要用非參數方法（或高斯混合之類的參數方法）。

【Q&A】[▶ 40:47](https://youtu.be/fkug1jGSgzU?t=2447) 學生問：是不是 EKF 適合稀疏環境、MCL 適合地標密集的環境？
老師：可分辨的地標越多，**所有**濾波器都越好。EKF 定位特別適合特徵式地圖（feature-based map），粒子濾波器適用範圍更廣，但「地標好分辨」對誰都有利，兩者在這點上沒差。

【Q&A】[▶ 41:37](https://youtu.be/fkug1jGSgzU?t=2497) 學生問：圖中藍線是什麼？老師：量測，假設視線感測器每 10 度一道射線。學生追問有些射線穿牆了？老師：模擬的瑕疵。

---

## 4. SLAM 問題

### 4.1 定義：線上 SLAM 與完整 SLAM

[▶ 42:02](https://youtu.be/fkug1jGSgzU?t=2522)

定位假設地圖已知。如果地圖也不知道 → **SLAM**：只給量測歷史 $z_{1:t}$ 和控制歷史 $u_{1:t}$，同時估計機器人的姿態（或路徑）**和**地圖。

關鍵改變 [▶ 45:07](https://youtu.be/fkug1jGSgzU?t=2707)：地圖 $m$ 從「條件變數」搬到「要估計的變數」。

$$
\text{定位：}\ p\left( x_t \mid z_{1:t}, u_{1:t}, m \right)
\qquad\longrightarrow\qquad
\text{SLAM：}\ p\left( x_t, m \mid z_{1:t}, u_{1:t} \right)
$$

【口頭】[▶ 43:25](https://youtu.be/fkug1jGSgzU?t=2605) 老師展示自己的研究：一個在小行星上**跳躍移動**的探測器，邊落地邊建小行星的地圖（在 JPL 的小行星模型上測試）。難處：光照要嘛極亮要嘛極暗；跳躍運動不連續；尺度變化大。但仍可即時、可靠地追蹤軌跡——「這是加強版的 SLAM」。

兩種版本 [▶ 45:41](https://youtu.be/fkug1jGSgzU?t=2741)：

| | 估計什麼 | 機率式 |
|---|---|---|
| **線上 SLAM**（online SLAM） | 目前姿態＋地圖 | $p\left( x_t, m \mid z_{1:t}, u_{1:t} \right)$ |
| **完整 SLAM**（full SLAM） | 整條路徑＋地圖 | $p\left( x_{1:t}, m \mid z_{1:t}, u_{1:t} \right)$ |

- 線上 SLAM 通常導出**遞迴**演算法（例如 EKF SLAM），計算上很可行。
- 理論上有整條過去路徑的估計更強。
- 兩種都還分「對應已知」和「對應未知」；實際上通常不知道，要自己解。

### 4.2 為什麼 SLAM 難

[▶ 46:36](https://youtu.be/fkug1jGSgzU?t=2796)

1. **連續＋組合混在一起**：地標位置、機器人姿態是連續量（航向在 $0$ 到 $2\pi$ 之間任意值）；量測對地標的對應是整數變數，是組合問題。這是一個混合（hybrid）問題。
2. **維度暴增** [▶ 47:23](https://youtu.be/fkug1jGSgzU?t=2843)：

【課堂討論】老師問：獨輪車模型 $x_t = (x, y, \theta)$，定位時信念是幾個變數的分布？學生答「3」（老師：「不是陷阱題」）。SLAM 時常常追蹤上千個地標，信念變成上千、上萬個變數的分布。

【口頭】[▶ 48:48](https://youtu.be/fkug1jGSgzU?t=2928) 圖模型（graphical model）：濾波只有狀態、控制、量測；定位多了一個已知的地圖節點；SLAM 的地圖節點影響量測（也透過「不能穿牆」影響狀態轉移），但看不到，要估計。線上 SLAM 估目前姿態和地圖，完整 SLAM 估整條路徑和地圖。

### 4.3 路徑誤差和地圖誤差是相關的

[▶ 49:59](https://youtu.be/fkug1jGSgzU?t=2999)

這是 SLAM 的挑戰，也是機會。

- 一開始我們定義全域座標系＝機器人的局部座標系，所以初始姿態**沒有不確定性**（地圖不知道，座標原點放哪都行，但之後要保持一致）。此時看到的地標，不確定性只來自量測雜訊。
- 開始移動後，自己在哪越來越不確定，看到的地標在哪也跟著不確定。
- 這兩種不確定性**是相關的**：如果知道自己在這裡，地標大概就在那裡；知道自己在別處，地標就在別處。

→ 地圖知道得越多，越能限制姿態；姿態知道得越多，越能限制地圖。

- **挑戰**：要正確推理，就得處理這個相關性。
- **機會**：一旦能減少「我在哪」的不確定性，地圖的不確定性也**馬上**跟著減少（見 5.6）。

---

## 5. EKF SLAM（已知對應）

[▶ 51:53](https://youtu.be/fkug1jGSgzU?t=3113)

跟定位一樣，把 SLAM 包裝成濾波問題：參數式（如高斯）或非參數式（粒子）。這堂課講 EKF 版本，兩個假設：

1. 運動雜訊和量測雜訊都是高斯（EKF 的假設）。
2. 地圖是**特徵式**（feature-based），例如點地標。

【口頭】「只要懂濾波的基礎，EKF SLAM 在概念上並不複雜；要讓它真的能用才複雜。」

### 5.1 擴增狀態向量

[▶ 53:31](https://youtu.be/fkug1jGSgzU?t=3211)

**關鍵技巧**：把地標座標塞進狀態，形成**擴增狀態向量**（augmented state vector）：

$$
y_t = \begin{bmatrix} x_t \\ m \end{bmatrix}
= \left( x,\ y,\ \theta,\ m_{1,x},\ m_{1,y},\ \dots,\ m_{N,x},\ m_{N,y} \right)^\top
\in \mathbb R^{3 + 2N}
$$

- 獨輪車姿態 3 維（別的機器人可能更多），每個點地標 2 維（$x$、$y$ 座標）。（⚠️ 逐字稿缺字：字幕「three plus one」→ $3 + 2N$。）
- 對應已知 ⟹ 隱含知道**有幾個**地標（不知道在哪，但知道幾個）。
- 若不知道地標數（未知對應的情況），$y_t$ 會**隨時間變長**。

目標：算線上 SLAM 的後驗 $p\left( y_t \mid z_{1:t}, u_{1:t} \right)$。

【口頭】[▶ 55:43](https://youtu.be/fkug1jGSgzU?t=3343) 投影片有筆誤：條件裡不該再有 $m$，因為 $m$ 已經在 $y_t$ 裡了。

然後就是**對擴增向量跑 EKF 定位**。需要：狀態轉移模型、量測模型、初始化。

### 5.2 狀態轉移模型

[▶ 56:09](https://youtu.be/fkug1jGSgzU?t=3369)

假設**環境是靜態的**：不知道地標在哪，但知道它們不會動。

$$
y_t = \begin{bmatrix} g\left( u_t, x_{t-1} \right) \\ m \end{bmatrix} + \varepsilon_t,
\qquad
\varepsilon_t \sim \mathcal N\left( 0,\ \begin{bmatrix} R_t^{x} & 0 \\ 0 & 0_{2N \times 2N} \end{bmatrix} \right)
$$

- 前 3 個分量：機器人的運動方程，有雜訊。
- 後 $2N$ 個分量：$m_t = m_{t-1}$，**沒有**雜訊——共變異數只有左上 $3 \times 3$ 區塊非零。

$g$ 一般是非線性的，照 EKF 慣例在 $\mu_{t-1}$ 附近線性化，Jacobian 記作 $G_t$。它的結構是：

$$
G_t = \begin{bmatrix} G_t^{x} & 0 \\ 0 & I_{2N} \end{bmatrix}
$$

（以下這個分塊形式**不是逐字稿內容**，是依「地標不動」直接推出的：地標那塊的轉移是恆等映射，所以 Jacobian 是單位矩陣。）

### 5.3 量測模型與稀疏 Jacobian

[▶ 59:18](https://youtu.be/fkug1jGSgzU?t=3558)

跟上一集一樣用**距離－方位**（range-bearing）感測器。若量測 $i$ 來自地標 $j$：

$$
z_t^i = \begin{bmatrix} r_t^i \\ \phi_t^i \end{bmatrix}
= \begin{bmatrix} \sqrt{\left( m_{j,x} - x \right)^2 + \left( m_{j,y} - y \right)^2} \\ \operatorname{atan2}\left( m_{j,y} - y,\ m_{j,x} - x \right) - \theta \end{bmatrix} + \delta_t,
\qquad \delta_t \sim \mathcal N(0, Q_t)
$$

距離是機器人到地標的歐氏距離；方位是「地標的絕對方向角」減去機器人航向 $\theta$。

**稀疏 Jacobian** [▶ 60:54](https://youtu.be/fkug1jGSgzU?t=3654)：

【課堂討論】老師問：$y_t$ 有 $3 + 2N$ 個變數，但量測模型實際依賴幾個變數？學生答：5 個——$x, y, \theta, m_{j,x}, m_{j,y}$。

所以對 $y_t$ 求偏導時，$3 + 2N$ 個分量裡只有 5 個非零。叫 MATLAB 之類的去對每個變數求導很蠢。做法：

1. 只對這 5 個變數求導，得到 $2 \times 5$ 的**低維 Jacobian** $h_t^{j}$（下面寫法依課本與 Thrun 的標準形式）：
$$
\delta = \begin{bmatrix} \delta_x \\ \delta_y \end{bmatrix} = \begin{bmatrix} \bar\mu_{j,x} - \bar\mu_{t,x} \\ \bar\mu_{j,y} - \bar\mu_{t,y} \end{bmatrix},\quad q = \delta^\top\delta,
\qquad
h_t^{j} = \frac{1}{q}\begin{bmatrix} -\sqrt q\,\delta_x & -\sqrt q\,\delta_y & 0 & \sqrt q\,\delta_x & \sqrt q\,\delta_y \\ \delta_y & -\delta_x & -q & -\delta_y & \delta_x \end{bmatrix}
$$
2. 用一個 $5 \times (3 + 2N)$ 的**投影矩陣**（projection matrix）$F_{x,j}$ 放回完整維度：$H_t^j = h_t^j\,F_{x,j}$。
$$
F_{x,j} = \begin{bmatrix} I_3 & 0 & \cdots & 0 & 0 & 0 & \cdots & 0 \\ 0 & 0 & \cdots & 0 & I_2 & 0 & \cdots & 0 \end{bmatrix}
$$
   - 上面一列：$I_3$ 放在前 3 欄（姿態的導數 → 完整 Jacobian 的左上區塊）。
   - 下面一列：$I_2$ 放在第 $j$ 個地標的兩欄（地標區塊裡的第 $2j-1$、$2j$ 欄，也就是完整向量的第 $2j+2$、$2j+3$ 欄），其餘都是 0。

【口頭】老師強調這只是**記帳**（bookkeeping）、避免無謂計算的技巧；本質仍是在最可能的擴增狀態附近把量測模型線性化。

### 5.4 初始化

[▶ 63:49](https://youtu.be/fkug1jGSgzU?t=3829)

一開始既不知道地圖也不知道自己在哪。SLAM 的自然做法：**把初始姿態當成座標原點**，之後建的地圖都相對於這個座標系，並追蹤機器人局部座標系和它之間的轉換。

$$
\mu_0 = \left( 0, 0, 0, 0, \dots, 0 \right)^\top,
\qquad
\Sigma_0 = \begin{bmatrix} 0_{3\times 3} & 0 \\ 0 & \infty \cdot I_{2N} \end{bmatrix}
$$

- 姿態：定義我們就在原點，所以不確定性是 0。
- 地標：不知道在哪，平均隨便設 0，不確定性設為**無限大**。

**第一次看到某個地標時** [▶ 65:40](https://youtu.be/fkug1jGSgzU?t=3940)：用機器人的最可能位置 $(\bar\mu_{t,x}, \bar\mu_{t,y})$、航向 $\bar\mu_{t,\theta}$，加上量到的 $(r_t^i, \phi_t^i)$ 反推：

$$
\begin{bmatrix} \bar\mu_{j,x} \\ \bar\mu_{j,y} \end{bmatrix}
= \begin{bmatrix} \bar\mu_{t,x} \\ \bar\mu_{t,y} \end{bmatrix}
+ r_t^i \begin{bmatrix} \cos\left( \phi_t^i + \bar\mu_{t,\theta} \right) \\ \sin\left( \phi_t^i + \bar\mu_{t,\theta} \right) \end{bmatrix}
$$

意思：地標在以我為圓心、半徑 $r_t^i$ 的圓上，方位角決定在圓上的哪一點。這是近似——它假設真實狀態就等於期望值，一般不成立。

### 5.5 演算法

[▶ 67:28](https://youtu.be/fkug1jGSgzU?t=4048)

**在解什麼**：給上一步擴增狀態的信念 $(\mu_{t-1}, \Sigma_{t-1})$、控制 $u_t$、量測 $z_t$、對應 $c_t$，算新的信念。

**步驟**：

1. **預測**（跟 EKF 定位一樣，只是地標分量的動態是恆等）：
   $\bar\mu_t = \begin{bmatrix} g(u_t, \mu_{t-1}^x) \\ \mu_{t-1}^m \end{bmatrix}$，
   $\bar\Sigma_t = G_t\Sigma_{t-1}G_t^\top + R_t$（不確定性 = 「我覺得我在哪」的不確定性 + 運動不確定性）。
2. 對每個量測 $z_t^i$，令 $j = c_t^i$：
   1. 若地標 $j$ **從沒看過**，用 5.4 的公式初始化 $\bar\mu_j$。
   2. 算預期量測 $\hat z_t^i = h(\bar\mu_t, j)$ 和 $H_t^i = h_t^i F_{x,j}$。
   3. $S = H_t^i\bar\Sigma_t (H_t^i)^\top + Q_t$，$K_t^i = \bar\Sigma_t (H_t^i)^\top S^{-1}$。
   4. $\bar\mu_t \leftarrow \bar\mu_t + K_t^i\left( z_t^i - \hat z_t^i \right)$，$\bar\Sigma_t \leftarrow \left( I - K_t^i H_t^i \right)\bar\Sigma_t$。
3. $\mu_t = \bar\mu_t$，$\Sigma_t = \bar\Sigma_t$。

**跟 EKF 定位的主要差別** [▶ 70:06](https://youtu.be/fkug1jGSgzU?t=4206)：$\bar\mu$ 是 $3 + 2N$ 維；卡爾曼增益 $K$ 是一個**滿的**向量（矩陣），所以**一個地標的量測會修正所有地標的位置估計**。（⚠️ 逐字稿缺字：字幕「the Kalman filter is a full vector」，依上下文是 Kalman gain。）

**什麼時候會失敗**：初始化地標時假設狀態等於期望值（不準）；線性化誤差；共變異數是 $(3+2N)^2$ 的滿矩陣，地標多時計算量隨 $N$ 平方成長【課本補充：§14.5 指出每步更新是 $O(N^2)$】；對應一旦錯（未知對應時）會汙染地圖。

【Q&A】[▶ 70:27](https://youtu.be/fkug1jGSgzU?t=4227) 學生問：「若地標 $j$ 沒看過」這個判斷，是不是就是「所有機率都很低、沒有一個配得上」？
老師：現在是對應已知的情況，沒有機率可言——那個函數直接告訴你看過沒。這不實際；後面（未知對應）就會用機率來判斷，你說的正是那個想法。

### 5.6 例子：迴圈閉合讓所有不確定性一起縮小

[▶ 71:13](https://youtu.be/fkug1jGSgzU?t=4273)

1. 起點：局部座標系＝全域座標系，姿態沒有不確定性。看到第一個地標，它只有量測雜訊造成的不確定性。
2. 開始移動：姿態不確定性因運動雜訊變大。
3. 看到第二個地標：它的不確定性比較大——量測雜訊之外，還加上「我在哪」的不確定性。
4. 繼續走：越來越不確定自己在哪，新看到的地標也越來越不確定。
5. **又看到最一開始那個地標**：馬上能把自己限制在不確定性橢圓裡的某個特定位置 → 姿態不確定性**一下子縮小**。

【口頭】直覺：一開始看到這張椅子，走一圈沒看到它，越來越不確定自己在哪；突然又看到它，知道自己離它 1 公尺——這就限制了**整條過去路徑**的估計：不可能上一步還在 50 公尺外。

（以下名詞**不是逐字稿內容**：這個「回到看過的地方」的事件，一般稱為**迴圈閉合**（loop closure），課本 §14.2.4 有討論。）

【Q&A】[▶ 73:21](https://youtu.be/fkug1jGSgzU?t=4401) 學生問：能認出這是同一個地標，是因為對應已知？老師：對。

**為什麼所有地標也一起變準** [▶ 73:30](https://youtu.be/fkug1jGSgzU?t=4410)：某個地標原本的分布很長，因為「如果我在這，它就在這；如果我在那，它就在那」。現在知道自己大概在哪了，地標的分布也就集中到對應的位置。這是 EKF SLAM 的「魔法」：一個能限制位置的量測，會傳播到所有地標的估計。

【課堂討論】老師問：$\Sigma$ 有幾維？學生答 $3 + 2N$。所以 $\Sigma$ 是 $(3+2N)\times(3+2N)$，而且是**滿矩陣**——非對角元素不為零，表示變數之間有相關。正是這些相關性，讓一個不確定性縮小時，其他的同時縮小。

---

## 6. EKF SLAM（未知對應）預告

[▶ 75:21](https://youtu.be/fkug1jGSgzU?t=4521)

【口頭】老師說這部分講得比較趕，下週會再花 10 分鐘複習。

要多加一步：估對應變數，用馬氏距離。

**步驟**（對每個量測 $z_t^i$）：

1. 先**假設**它來自一個新地標（索引 $N_t + 1$），用 5.4 的公式算出這個新地標的位置。
2. 對所有地標 $k = 1, \dots, N_t + 1$（包括剛假設的新地標），算 $\hat z_t^k$、$S_t^k$，以及馬氏距離
   $\pi_k = \left( z_t^i - \hat z_t^k \right)^\top \left( S_t^k \right)^{-1} \left( z_t^i - \hat z_t^k \right)$。
3. 把新地標的 $\pi_{N_t+1}$ **設成** $\alpha$（設計參數）。
4. $j = \arg\min_k \pi_k$。如果 $j = N_t + 1$，就真的新增這個地標（$N_t \leftarrow N_t + 1$）。
5. 有了對應之後，其他都一樣。

換句話說：**到所有已知地標的馬氏距離都超過 $\alpha$ 時，就建一個新地標**。

【課本補充】§14.5.2 把「超過 $\alpha$」形式化為 **$\chi^2$ 閘**（$\chi^2$ gating）：若模型正確，$d$ 維量測的馬氏距離服從自由度 $d$ 的 $\chi^2$ 分布，所以 $\alpha$ 可取 $\chi^2_d$ 的某個分位數（例如 95%）。

**往後要怎麼加強**（超出本課） [▶ 77:24](https://youtu.be/fkug1jGSgzU?t=4644)：

- 未知對應時常產生**虛假地標**（spurious landmark）：以為是新的、其實不是 → 需要離群值剔除機制。
- 電腦視覺端：挑**真正有辨識度**的地標。特徵偵測（feature detection）非常重要，這也是之前花時間講它的原因（第 11–12 集）。

【口頭】[▶ 78:12](https://youtu.be/fkug1jGSgzU?t=4692) 下週：感測器融合，以及怎麼用開源自駕軟體（Autoware）；會先花 10 分鐘複習未知對應的 EKF SLAM。粒子式 SLAM 另找時間補課（下週或下下週），作業不考。到這裡，作業 4 需要的東西都有了。（⚠️ 逐字稿缺字：字幕「auto-ware」→ Autoware。）

---

## 7. 一頁速查表

### 對應變數的最大概似（逐個量測）

$$
\hat c_t^i = \arg\max_j\ \mathcal N\left( z_t^i;\ \hat z_t^j,\ S_t^j \right),\qquad
\hat z_t^j = h(\bar\mu_t, j, m),\quad S_t^j = H_t^j\bar\Sigma_t(H_t^j)^\top + Q_t
$$

- **關鍵一步**：對 $x_t$ 用全機率定理 $p(z^i \mid \cdot) = \int p(z^i \mid x_t, j)\,\overline{bel}(x_t)\,dx_t$；兩個高斯（線性化後）相乘積分仍是高斯，變異數相加。
- 量測不確定性 = 狀態不確定性（經 $H$ 投影）＋ 量測雜訊。

### 馬氏距離

$$
d = \left( z - \hat z \right)^\top S^{-1} \left( z - \hat z \right)
$$

- 「離平均幾個 $\sigma$」；不確定的方向被打折。
- **關鍵一步**：$\log\mathcal N(z; \hat z, S) = -\tfrac12 d - \tfrac12\log|S| + \text{常數}$，忽略 $|S|$ 的差異時，最大概似 ⟺ 最小馬氏距離。

### Monte Carlo 定位

每個粒子：$\bar x^{[k]} \sim p(x_t \mid x_{t-1}^{[k]}, u_t, m)$，$w^{[k]} = p(z_t \mid \bar x^{[k]}, m)$ → 依 $w$ 放回重抽 $M$ 次。

- 能表示多峰信念（對稱環境、全域定位、綁架）；小心粒子匱乏 → 偶爾隨機撒粒子。

### EKF SLAM

$$
y_t = \begin{bmatrix} x_t \\ m \end{bmatrix} \in \mathbb R^{3+2N},\qquad
y_t = \begin{bmatrix} g(u_t, x_{t-1}) \\ m \end{bmatrix} + \varepsilon_t,\quad \operatorname{Cov}(\varepsilon_t) = \begin{bmatrix} R_t^x & 0 \\ 0 & 0 \end{bmatrix}
$$

$$
H_t^j = h_t^j\,F_{x,j}\ \ (2\times 5 \text{ 低維 Jacobian} \times 5\times(3+2N) \text{ 投影}),\qquad
\mu_0 = 0,\ \ \Sigma_0 = \operatorname{diag}\left( 0_{3}, \infty\cdot I_{2N} \right)
$$

$$
\text{新地標：}\ \bar\mu_j = \bar\mu_{t,xy} + r\left( \cos(\phi + \bar\mu_{t,\theta}),\ \sin(\phi + \bar\mu_{t,\theta}) \right)
$$

- **關鍵一步**：$\Sigma$ 是滿矩陣（姿態和地標相關）→ 卡爾曼增益是滿的 → 一個量測修正所有地標；迴圈閉合時所有不確定性一起縮小。
- 未知對應：新地標的分數設為 $\alpha$，選馬氏距離最小者；全部都 $> \alpha$ 就新增地標。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 未知對應的 EKF SLAM（複習） | 第 17 集開頭 |
| 感測器融合、Autoware | 第 17 集 |
| 粒子式 SLAM（FastSLAM）、MCL 延伸 | 第 21 集（補課） |
| 特徵偵測的重要性 | 第 18 集現代電腦視覺 |
| 不確定性下的決策（信念當狀態） | 第 20 集 |

---

## 附：本集一句話總結

> **對應變數未知時，把每個量測配給「讓它最可能出現」的地標（等價於馬氏距離最小者）然後認定它；把粒子濾波器的模型換成機器人的版本就得到 Monte Carlo 定位，能處理多峰信念；地圖也未知時，把地標座標塞進狀態向量、讓它們的動態是「不動」，對這個擴增向量跑 EKF 就是 EKF SLAM——因為姿態和地標的共變異數是滿的，一次重新看到舊地標就能讓整張地圖一起變準。**

---

## ⚠️ 待確認清單

1. 上課日期待補（推斷為週三）。
2. [▶ 29:44](https://youtu.be/fkug1jGSgzU?t=1784) 字幕「You can also use other parametric filters for localization such as EKF」——依上下文應指 EKF 以外的參數式濾波器（推測 UKF），未確認。
3. [▶ 35:06](https://youtu.be/fkug1jGSgzU?t=2106) 作業 4 第 3 題的「重抽樣改良」名稱逐字稿沒講，筆記推論為低變異重抽樣。

---

*筆記依據 Marco Pavone（推斷）「Stanford AA274A Principles of Robotic Autonomy（2019 秋）」Lecture 16 錄影逐字稿（Whisper `medium.en`，1:18:58）與《Principles of Robot Autonomy》§13.5.2–13.6、§14.4–14.5 整理。*
