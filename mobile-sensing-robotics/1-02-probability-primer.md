---
course: Mobile Sensing and Robotics 1（Uni Bonn, Winter 2021/22）
episode: 1-02
lecture: Probability Primer
date: 待補（2021/22 冬季學期）
video: https://youtu.be/JS5ndD8ans4
notes: 《Probabilistic Robotics》早期草稿版 §2.2（書頁 10–15，PDF 頁 22–27）
---

# 第 1-02 集 · 機率入門（Probability Primer for Probabilistic Robotics） [▶ 影片](https://youtu.be/JS5ndD8ans4)

← 上一集：[1-01-course-intro](1-01-course-intro.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[1-03-bayes-filter](1-03-bayes-filter.md) →

> **課程**：Mobile Sensing and Robotics 1，Uni Bonn，2021/22 冬季學期 — 第 1-02 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（42:34，Whisper `medium.en` 轉錄）＋《Probabilistic Robotics》早期草稿版 §2.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼機器人需要機率](#1-為什麼機器人需要機率)
- [2. 機率的公理](#2-機率的公理)
- [3. 離散與連續隨機變數](#3-離散與連續隨機變數)
- [4. 聯合機率、獨立、條件機率](#4-聯合機率獨立條件機率)
- [5. 全機率定理與邊際化](#5-全機率定理與邊際化)
- [6. 兩個計數的例子](#6-兩個計數的例子)
- [7. 貝氏定理](#7-貝氏定理)
- [8. 條件獨立](#8-條件獨立)
- [9. 怎麼表示一個機率分布](#9-怎麼表示一個機率分布)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

課程第一個技術單元。講者說這「不是理論課」，只花約半小時複習之後一直會用到的機率規則，下一集（1-03）就用這些規則推出**貝氏濾波**（Bayes filter）。

| 主題 | 課本 |
|---|---|
| 為什麼要用機率 | 第 1 章 §1.1–1.2 |
| 公理、隨機變數、聯合／條件機率、全機率、貝氏定理、條件獨立 | §2.2（書頁 10–15） |
| 高斯分布 | §2.2 式 (2.3)(2.4) |
| 混合高斯 | 無（本集口頭＋投影片） |

`⚠️ 逐字稿缺字`：Whisper 多次把 “Bayes filter” 寫成 “base filter” / “based filter”（如 [▶ 00:21](https://youtu.be/JS5ndD8ans4?t=21)、[▶ 00:46](https://youtu.be/JS5ndD8ans4?t=46)），下文一律改為 Bayes filter。

---

## 1. 為什麼機器人需要機率

### 1.1 機器人學裡的幾類問題

[▶ 01:37](https://youtu.be/JS5ndD8ans4?t=97)

| 問題 | 意思 |
|---|---|
| 狀態估計（state estimation） | 一般性的「推估系統現在的狀態」 |
| 建圖（mapping） | 世界長什麼樣子？ |
| 定位（localization） | 我在世界的哪裡？ |
| SLAM（simultaneous localization and mapping，同時定位與建圖） | 上面兩個一起解；本課後段與 MSR2 才深入 |
| 運動規劃（motion planning） | 要執行什麼動作才能到達／接近目標 |
| 控制（control） | 把高階的運動真正執行出來 |

### 1.2 「我在哪」和「世界長怎樣」是綁在一起的

[▶ 02:35](https://youtu.be/JS5ndD8ans4?t=155)

- 機器人學的狀態估計多半是**幾何**：障礙物在哪、地標（landmark）在哪、平台在哪。
- 有些東西會動（車子本身），有些大致不動（樹、車道線、交通號誌）。
- 【口頭】路牌的例子 [▶ 03:23](https://youtu.be/JS5ndD8ans4?t=203)：
  - 你看到前方 20 公尺有一面路牌。要知道**路牌在哪**，得先知道**你在哪**。
  - 反過來，你不知道自己在哪，但手上有地圖，看到一面很有特色的路牌 → 就能推出自己在哪。
  - 所以定位和建圖互相依賴；兩個一起解就是 SLAM。
- 例子 [▶ 04:02](https://youtu.be/JS5ndD8ans4?t=242)：車上裝 3D 光達（LiDAR，用雷射測距的感測器），一邊估計車的位姿（pose，位置＋朝向）、一邊把距離量測疊起來，就得到環境的 3D 點雲。
  - `⚠️ 逐字稿缺字`：Whisper 寫 “3d lighter scanner”，應為 **3D lidar scanner**。

### 1.3 為什麼要用機率

[▶ 04:50](https://youtu.be/JS5ndD8ans4?t=290)

關鍵理由：**世界是有雜訊的**。

- 觀測不會完美 → 觀測有不確定性。
- 動作不會完全照指令執行 → 運動有不確定性。
- 沒有完美的感測器，也沒有完美聽話的平台。

所以最好的做法是：把不確定性**明確地**放進模型，在狀態估計、甚至動作選擇時都考慮進去。

`⚠️ 逐字稿缺字`：[▶ 05:25](https://youtu.be/JS5ndD8ans4?t=325) Whisper 寫 “so the bad thing is to take that uncertainty into account”，依上下文應為 “the **best** thing”。

【口頭】定位的例子 [▶ 05:49](https://youtu.be/JS5ndD8ans4?t=349)：

- 傳統做法：「機器人**就在** $x$ 這個位置。」只要差 5 mm 就是錯的；如果規劃時只留 3 mm 安全距離擦過障礙物，可能就撞了。
- 機率做法：「機器人**大概在這一帶**，在某個區域內的機率是多少。」
- 知道自己有多不確定，就能加大安全距離，或選擇讓碰撞機率趨近零的動作。

【口頭】[▶ 07:53](https://youtu.be/JS5ndD8ans4?t=473) 講者估計這門課約 **90%** 的技術都建立在機率論上。代價是數學模型比較複雜，好處是比較穩健（robust）。

---

## 2. 機率的公理

[▶ 08:03](https://youtu.be/JS5ndD8ans4?t=483)

機率論只建立在少數幾條**公理**（axiom，不證自明的定義）上，其他一切都從它們推出來。

記號：$P(A)$ = 命題（proposition）$A$ 為真的機率。

講者列出四條：

$$
\begin{aligned}
&\text{(1)}\quad 0 \le P(A) \le 1 \\
&\text{(2)}\quad P(\text{true}) = 1 \\
&\text{(3)}\quad P(\text{false}) = 0 \\
&\text{(4)}\quad P(A \lor B) = P(A) + P(B) - P(A \land B)
\end{aligned}
$$

- $P = 1$：一定成立；$P = 0$：一定不成立；$P = 0.5$：一半的情況成立。
- 第 (4) 條的直覺 [▶ 10:17](https://youtu.be/JS5ndD8ans4?t=617)：畫兩個重疊的圓，藍色是 $A$、黃色是 $B$。$A$ 的面積加 $B$ 的面積時，中間重疊那塊（$A \land B$）被算了兩次，所以要扣掉一次。

### 2.1 例子：從公理推出 $P(\lnot A) = 1 - P(A)$

[▶ 11:04](https://youtu.be/JS5ndD8ans4?t=664)

在公理 (4) 裡把 $B$ 換成 $\lnot A$（「$A$ 不成立」）：

$$
P(A \lor \lnot A) = P(A) + P(\lnot A) - P(A \land \lnot A)
$$

- $A \land \lnot A$：$A$ 同時為真又為假，不可能發生 → $P(\text{false})$。
- $A \lor \lnot A$：$A$ 不是真就是假，一定成立 → $P(\text{true})$。

代進去：

$$
P(\text{true}) = P(A) + P(\lnot A) - P(\text{false})
$$

用公理 (2)(3)：

$$
1 = P(A) + P(\lnot A) - 0
$$

移項：

$$
P(\lnot A) = 1 - P(A) \qquad \blacksquare
$$

講者的重點：每一條規則都能這樣從公理一步步推出來；但全部從頭推太花時間，所以接下來只「快轉」介紹會用到的規則。

---

## 3. 離散與連續隨機變數

### 3.1 離散隨機變數

[▶ 14:12](https://youtu.be/JS5ndD8ans4?t=852)

- **隨機變數**（random variable）$X$：可以取不同值的變數。
- 離散（discrete）：取值是可數的，$X \in \{x_1, x_2, \dots, x_n\}$。
- $P(X = x_i)$：$X$ 取值 $x_i$ 的機率。**簡寫**為 $P(x_i)$ 或 $P(x)$。講者說 99.9% 的時候都用簡寫。
- 函數 $P$ 叫**機率質量函數**（probability mass function, pmf）。
- 性質：每個值介於 0 和 1 之間，而且

$$
\sum_{i} P(X = x_i) = 1
$$

因為 $n$ 個結果中一定有一個會發生。

### 3.2 連續隨機變數

[▶ 16:06](https://youtu.be/JS5ndD8ans4?t=966)

- $X$ 可以取連續的值。仍寫 $p(X = x)$，簡寫 $p(x)$，但這時 $p$ 是**機率密度函數**（probability density function, pdf）。
- **pdf 的值可以大於 1**。它不是機率本身。
- 要得到機率，必須**積分**：

$$
P(a \le X \le b) = \int_a^b p(x)\, dx
$$

- 整個空間的積分等於 1：

$$
\int p(x)\, dx = 1
$$

- 最常見的 pdf 是常態分布，但 $p(x)$ 可以是任何形式，只要積分是 1。

[▶ 17:38](https://youtu.be/JS5ndD8ans4?t=1058) 離散和連續的對應：

| | 離散 | 連續 |
|---|---|---|
| 全部加起來 | $\sum_x P(x) = 1$ | $\int p(x)\,dx = 1$ |
| 只算一個子集 | 對子集求和 = 落在子集的機率 | 對子集積分 = 落在子集的機率 |

---

## 4. 聯合機率、獨立、條件機率

[▶ 18:28](https://youtu.be/JS5ndD8ans4?t=1108)

### 4.1 聯合機率（joint probability）

$$
P(x, y) = P(X = x \text{ and } Y = y)
$$

### 4.2 獨立（independence）

$X$ 和 $Y$ **獨立**的定義是

$$
P(x, y) = P(x)\, P(y)
$$

意思：不管 $Y$ 是什麼，$X$ 的分布都不變。

### 4.3 條件機率（conditional probability）

[▶ 19:51](https://youtu.be/JS5ndD8ans4?t=1191)

- $P(x \mid y)$ 讀作「給定 $y$ 時 $x$ 的機率」（$x$ given $y$）。
- 它是**只對 $x$ 的分布**，前提是已經知道 $Y$ 取什麼值。
- `⚠️ 逐字稿缺字`：[▶ 19:59](https://youtu.be/JS5ndD8ans4?t=1199) Whisper 寫 “this horizontal bias reads as given”。符號 $\mid$ 是直線，依上下文應為「這條**直線**（bar）讀作 given」。

定義：

$$
P(x, y) = P(x \mid y)\, P(y)
$$

等價地（$P(y) > 0$）：

$$
P(x \mid y) = \frac{P(x, y)}{P(y)}
$$

由於 $P(x, y) = P(y, x)$，$x$、$y$ 角色可以對調。

### 4.4 用條件機率表示獨立

若 $X$、$Y$ 獨立：

$$
P(x \mid y) = \frac{P(x)\,P(y)}{P(y)} = P(x)
$$

知道 $y$ 對 $x$ 沒有任何幫助。

【口頭】[▶ 21:30](https://youtu.be/JS5ndD8ans4?t=1290) 「聯合機率和條件機率會一直出現，一定要真正搞懂 *given* 是什麼意思。」

---

## 5. 全機率定理與邊際化

### 5.1 全機率定理（law of total probability）

[▶ 21:41](https://youtu.be/JS5ndD8ans4?t=1301)

$$
P(x) = \sum_y P(x \mid y)\, P(y) \qquad\text{（離散）}
$$

$$
p(x) = \int p(x \mid y)\, p(y)\, dy \qquad\text{（連續）}
$$

直覺：假設 $y \in \{1, 2, 3\}$。

1. 先假設 $y = 1$：算「$y = 1$ 的機率」×「在 $y = 1$ 時 $x$ 的機率」。
2. 對 $y = 2$、$y = 3$ 做一樣的事。
3. 全部加起來，$y$ 就被「消掉」，只剩 $x$。

推導（講者沒寫出這一步，這裡補上）：由條件機率定義 $P(x \mid y) P(y) = P(x, y)$，所以右邊 $= \sum_y P(x, y)$，也就是下面的邊際化。

### 5.2 邊際化（marginalization）

[▶ 22:58](https://youtu.be/JS5ndD8ans4?t=1378)

$$
P(x) = \sum_y P(x, y) \qquad\qquad p(x) = \int p(x, y)\, dy
$$

- 手上有聯合分布（每一組 $(x, y)$ 的機率都知道），想要只關於 $x$ 的分布 → 把所有 $y$ 的值加起來（或積分）。
- 說法：把 $Y$「邊際化掉」（marginalize out）。

---

## 6. 兩個計數的例子

### 6.1 網格上的點

[▶ 24:01](https://youtu.be/JS5ndD8ans4?t=1441)

- 一個 $9 \times 2$ 的網格：$x \in \{1, \dots, 9\}$，$y \in \{1, 2\}$，共 18 種結果。
- 每個格子裡的藍點 = 那個結果發生的次數。例如 $(x = 1, y = 1)$ 發生了 3 次。
- **聯合分布**：格子裡的點數 ÷ 總點數。
- **邊際化掉 $x$**：把同一列（同一個 $y$）的 9 格合成一格，數點 → 得到 $P(y)$。
- **邊際化掉 $y$**：把同一行（同一個 $x$）的 2 格合成一格 → 得到 $P(x)$。
- **條件分布 $P(x \mid y = 1)$**：已知 $y = 1$，另一列完全不看；只用 $y = 1$ 那一列的 9 格做直方圖，再除以這一列的總點數。

（每一格的實際點數在投影片上，逐字稿只唸出少數幾個，無法完整重建。）

### 6.2 男性與吸菸

[▶ 26:54](https://youtu.be/JS5ndD8ans4?t=1614)

兩個二元變數：$M$（男性／非男性）、$S$（吸菸／不吸菸）。共 120 人：

| | 男性 $M$ | 女性 $\lnot M$ | 合計 |
|---|---|---|---|
| 吸菸 $S$ | 20 | 20 | 40 |
| 不吸菸 $\lnot S$ | 35 | 45 | 80 |
| 合計 | 55 | 65 | 120 |

**聯合機率**（隨機閉眼抽一個人）[▶ 28:18](https://youtu.be/JS5ndD8ans4?t=1698)：

$$
P(M, S) = \frac{20}{120}, \qquad P(M, \lnot S) = \frac{35}{120}
$$

**邊際機率** [▶ 29:27](https://youtu.be/JS5ndD8ans4?t=1767)：

$$
P(M) = \frac{20}{120} + \frac{35}{120} = \frac{55}{120}, \qquad
P(\lnot M) = \frac{65}{120}, \qquad
P(S) = \frac{40}{120}
$$

**條件機率** [▶ 30:21](https://youtu.be/JS5ndD8ans4?t=1821)：已知這個人吸菸，他是男性的機率？

- 已知吸菸 → 不吸菸那一列完全不用看，只看第一列（40 人）。
- 其中男性 20 人：

$$
P(M \mid S) = \frac{20}{40} = 0.5
$$

- 用定義驗算：

$$
P(M \mid S) = \frac{P(M, S)}{P(S)} = \frac{20/120}{40/120} = \frac{20}{40} = 0.5
$$

- 常見錯誤：分母寫成 120。講者強調「given 吸菸」就只剩 40 人。

---

## 7. 貝氏定理

[▶ 32:07](https://youtu.be/JS5ndD8ans4?t=1927)

### 7.1 推導

只用條件機率的定義，寫兩次：

$$
P(x, y) = P(x \mid y)\, P(y)
$$

$$
P(x, y) = P(y, x) = P(y \mid x)\, P(x)
$$

兩式左邊相同，所以右邊相等：

$$
P(x \mid y)\, P(y) = P(y \mid x)\, P(x)
$$

兩邊除以 $P(y)$（需要 $P(y) > 0$）：

$$
\boxed{\,P(x \mid y) = \frac{P(y \mid x)\, P(x)}{P(y)}\,}
$$

### 7.2 名稱

[▶ 33:58](https://youtu.be/JS5ndD8ans4?t=2038)

$$
\underbrace{P(x \mid y)}_{\text{posterior 後驗}} = \frac{\overbrace{P(y \mid x)}^{\text{likelihood 似然}}\ \overbrace{P(x)}^{\text{prior 先驗}}}{\underbrace{P(y)}_{\text{evidence 證據}}}
$$

（講者口頭說了 likelihood、prior、evidence；「posterior」這個詞出自課本 §2.2。）

### 7.3 用途

- 想知道 $x$ given $y$，但手上只有反方向的 $y$ given $x$ → 用貝氏定理把兩者**對調**。
- 機器人裡的典型情況：想從感測資料 $y$ 推狀態 $x$。「在狀態 $x$ 時會量到什麼」（$P(y \mid x)$）比較好建模。
- 貝氏濾波（Bayes filter）之所以叫這個名字，就是因為推導的關鍵一步用到貝氏定理。

【課本補充】課本 §2.2（書頁 13，PDF 頁 25）把 $P(y \mid x)$ 叫做**生成模型**（generative model），因為它描述「狀態 $X$ 如何產生感測量測 $Y$」。

### 7.4 帶背景知識的貝氏定理

[▶ 34:12](https://youtu.be/JS5ndD8ans4?t=2052)

在每個機率上都多加一個條件 $z$（背景知識，background knowledge），等式照樣成立：

$$
P(x \mid y, z) = \frac{P(y \mid x, z)\, P(x \mid z)}{P(y \mid z)}
$$

`⚠️ 逐字稿缺字`：Whisper 寫 “Bayes rule with background order”，應為 **background knowledge**。

【口頭】[▶ 34:53](https://youtu.be/JS5ndD8ans4?t=2093) 「貝氏定理一定要背起來，不知道貝氏定理沒有任何藉口。」

【課本補充】正規化常數（課本 §2.2 式 (2.15)，書頁 13）：分母 $P(y)$ 不含 $x$，對所有 $x$ 都是同一個數，所以常寫成

$$
P(x \mid y) = \eta\, P(y \mid x)\, P(x), \qquad \eta = P(y)^{-1}
$$

離散時的算法：先對每個 $x$ 算 $P(y \mid x) P(x)$，再把結果除以它們的總和，讓總和為 1。這樣就不用另外算 $P(y)$。這個 $\eta$ 在 1-03 集貝氏濾波會用到。

---

## 8. 條件獨立

[▶ 35:04](https://youtu.be/JS5ndD8ans4?t=2104)

**定義**：給定 $z$ 時，$x$ 和 $y$ **條件獨立**（conditionally independent），如果

$$
P(x, y \mid z) = P(x \mid z)\, P(y \mid z)
$$

**等價說法** [▶ 36:04](https://youtu.be/JS5ndD8ans4?t=2164)：

$$
P(x \mid z) = P(x \mid z, y), \qquad P(y \mid z) = P(y \mid z, x)
$$

意思：已經知道 $z$ 時，再多知道 $y$ 對推 $x$ 沒有幫助（反之亦然）。

（講者一開始口誤說成「$P(x \mid y)$ 等於 $P(x \mid y, z)$」，隨即改口為上式。）

等價的推導（講者沒寫，這裡補上）：由條件機率的定義（帶背景知識 $z$），

$$
P(x, y \mid z) = P(x \mid y, z)\, P(y \mid z)
$$

和定義式 $P(x, y \mid z) = P(x \mid z) P(y \mid z)$ 比較，兩邊除以 $P(y \mid z) > 0$，得 $P(x \mid y, z) = P(x \mid z)$。

**重要**：條件獨立**不代表**獨立 [▶ 36:48](https://youtu.be/JS5ndD8ans4?t=2208)。

$$
P(x, y \mid z) = P(x \mid z)\, P(y \mid z) \;\not\Rightarrow\; P(x, y) = P(x)\, P(y)
$$

- 為了區分，一般的獨立也叫**邊際獨立**（marginal independence）。
- 有了 $z$ 才成立；沒有 $z$ 時可能成立也可能不成立，但不能推得。

【課本補充】課本 §2.2 式 (2.27)（書頁 15，PDF 頁 27）也指出反方向一樣不成立：獨立也**不代表**條件獨立，

$$
P(x, y) = P(x)\, P(y) \;\not\Rightarrow\; P(x, y \mid z) = P(x \mid z)\, P(y \mid z)
$$

只有特殊情況下兩者才同時成立。

---

## 9. 怎麼表示一個機率分布

### 9.1 離散：直方圖

[▶ 37:20](https://youtu.be/JS5ndD8ans4?t=2240)

離散分布用**直方圖**（histogram）存最簡單，就是第 6 節那樣數次數。

### 9.2 連續：高斯分布

[▶ 37:50](https://youtu.be/JS5ndD8ans4?t=2270)

連續的世界通常要用**參數化函數**（parametric function）描述分布。最常用的是**常態分布**（normal distribution），又叫**高斯分布**（Gaussian distribution）。

**一維**：參數是平均值 $\mu$（mean）和標準差 $\sigma$（standard deviation）。

$$
p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left( -\frac{1}{2}\, \frac{(x - \mu)^2}{\sigma^2} \right)
$$

- $\mu$：峰值的位置。
- $\sigma$：寬度。$\sigma$ 越小 → 越窄、峰越高 → 不確定性越小。
- 指數裡：$x$ 離 $\mu$ 多遠，平方，除以 $\sigma^2$，乘 $-\tfrac12$。前面的常數讓積分等於 1。
- 高斯分布永遠是**單峰**（unimodal）的。

**多維**：$\mathbf{x}$ 是向量，參數是平均向量 $\boldsymbol{\mu}$ 和共變異數矩陣 $\Sigma$（covariance matrix）。

$$
p(\mathbf{x}) = \det(2\pi\Sigma)^{-\frac{1}{2}} \exp\!\left( -\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})^{\mathsf T} \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)
$$

（多維公式依課本 §2.2 式 (2.4)；講者只說「和一維很像，改用向量和矩陣」，公式在投影片上。）

- 二維可以畫成鐘形曲面。
- 三維以上很難畫，通常畫**等機率面**（iso-surface）：曲面上每一點的機率密度相同。越往橢圓（橢球）裡面機率越高，越往外越低。

**一維是多維的特例**：令 $\Sigma = \sigma^2$（$1 \times 1$），則 $\det(2\pi\Sigma)^{-1/2} = (2\pi\sigma^2)^{-1/2}$，$(\mathbf{x}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu}) = (x-\mu)^2/\sigma^2$，兩式相同。

### 9.3 混合高斯（Gaussian mixture）

[▶ 39:55](https://youtu.be/JS5ndD8ans4?t=2395)

要表示**多個峰**（multi-modal）時，把 $K$ 個高斯加權相加：

$$
p(x) = \sum_{k=1}^{K} w_k\, \mathcal{N}(x;\, \mu_k, \sigma_k^2), \qquad w_k \ge 0,\quad \sum_{k=1}^{K} w_k = 1
$$

- 權重和為 1，保證積分還是 1，仍是機率分布。
- 投影片例子：三個一維高斯合成一條有多個峰的紅色曲線；也可以用三個二維高斯。
- （權重記號 $w_k$ 是筆記寫法；講者只說「要正規化讓總和為 1」。）

【口頭】缺點 [▶ 41:03](https://youtu.be/JS5ndD8ans4?t=2463)：在某些狀態估計或最小平方問題裡，「和」很難處理。例如取對數似然（log likelihood）時，$\log$ 進不去求和裡面，比單峰高斯複雜很多。所以它不一定是好解法，但通常是表示多峰分布**最簡單**的方法。

---

## 10. 一頁速查表

### 10.1 公理與基本規則

| 規則 | 公式 | 關鍵一步 |
|---|---|---|
| 公理 | $0 \le P(A) \le 1$，$P(\text{true}) = 1$，$P(\text{false}) = 0$ | — |
| 加法公理 | $P(A \lor B) = P(A) + P(B) - P(A \land B)$ | 重疊部分被算兩次 |
| 補集 | $P(\lnot A) = 1 - P(A)$ | 令 $B = \lnot A$，$A \lor \lnot A = \text{true}$，$A \land \lnot A = \text{false}$ |
| 正規化 | $\sum_x P(x) = 1$，$\int p(x)\,dx = 1$ | 一定有一個結果發生 |
| 區間機率 | $P(a \le X \le b) = \int_a^b p(x)\,dx$ | pdf 值本身可 > 1 |

### 10.2 聯合、條件、獨立

| 規則 | 公式 | 關鍵一步 |
|---|---|---|
| 條件機率 | $P(x, y) = P(x \mid y) P(y)$ | 定義 |
| 獨立 | $P(x, y) = P(x) P(y)$ ⇔ $P(x \mid y) = P(x)$ | 代入條件機率定義 |
| 全機率 | $P(x) = \sum_y P(x \mid y) P(y)$ | $P(x \mid y)P(y) = P(x, y)$ |
| 邊際化 | $P(x) = \sum_y P(x, y)$ | 把 $y$ 加總掉 |
| 貝氏定理 | $P(x \mid y) = \dfrac{P(y \mid x) P(x)}{P(y)}$ | $P(x \mid y)P(y) = P(x,y) = P(y \mid x)P(x)$ |
| 正規化寫法【課本】 | $P(x \mid y) = \eta\, P(y \mid x) P(x)$ | 分母不含 $x$ |
| 帶背景知識 | $P(x \mid y, z) = \dfrac{P(y \mid x, z) P(x \mid z)}{P(y \mid z)}$ | 每項加條件 $z$ |
| 條件獨立 | $P(x, y \mid z) = P(x \mid z) P(y \mid z)$ ⇔ $P(x \mid z) = P(x \mid y, z)$ | 和 $P(x,y \mid z) = P(x \mid y,z)P(y \mid z)$ 比較 |
| ⚠️ | 條件獨立 ⇏ 獨立；獨立 ⇏ 條件獨立 | — |

### 10.3 分布

| 名稱 | 公式 |
|---|---|
| 一維高斯 | $\mathcal{N}(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$ |
| 多維高斯 | $\det(2\pi\Sigma)^{-1/2} \exp\!\left(-\frac12 (\mathbf{x}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$ |
| 混合高斯 | $\sum_k w_k \mathcal{N}(x; \mu_k, \sigma_k^2)$，$\sum_k w_k = 1$ |

課本 §2.2 還有期望值（expectation）、共變異數（covariance）、熵（entropy），本集沒講。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 貝氏定理、正規化常數 $\eta$ | 1-03 貝氏濾波的「修正」步驟 |
| 全機率定理 | 1-03 貝氏濾波的「預測」步驟 |
| 條件獨立（馬可夫假設） | 1-03 推導貝氏濾波時用來刪掉條件 |
| 二元變數、貝氏定理 | 1-05 佔用網格地圖（每格被佔住的機率） |
| 高斯分布 | 1-07 運動模型、1-08 觀測模型、1-10 Kalman 濾波 |
| 多峰分布 | 1-14 粒子濾波（用樣本表示任意分布） |
| 高斯 ↔ 最小平方 | MSR2：2-05 最小平方 |

---

## 附：本集一句話總結

> **世界有雜訊，所以機器人要用機率表示「大概在哪」。整門課只靠幾條規則：條件機率、全機率、邊際化、貝氏定理、條件獨立，再加上高斯分布。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 1」Probability Primer 錄影逐字稿（Whisper `medium.en`，42:34）與《Probabilistic Robotics》早期草稿版 §2.2 整理。*
