---
course: Stanford AA274A Principles of Robotic Autonomy（2019 秋）
episode: 1
lecture: Lecture 1
date: 待補（2019 秋季第一堂）
video: https://youtu.be/Lgt5ONBtFI0
notes: 《Principles of Robot Autonomy》前言（書頁 1–5，PDF 頁 3–7）、§1.2–1.3（書頁 30–45，PDF 頁 32–47）
---

# 第 1 集 · Lecture 1：課程介紹與移動機器人運動學（Overview, Mobile Robot Kinematics） [▶ 影片](https://youtu.be/Lgt5ONBtFI0)

← 上一集：無 ｜ [總目錄](README.md) ｜ 下一集：[02-ros](02-ros.md) →

> **課程**：Stanford AA274A Principles of Robotic Autonomy I，2019 秋 — 第 1 集
> **講者**：Marco Pavone（推斷：講者沒報名字，但說自己來自義大利、到 Stanford 前在 NASA JPL 當機器人學家，並帶 Autonomous Systems Lab）
> **來源**：YouTube 錄影逐字稿（1:15:15，Whisper `medium.en` 轉錄）＋《Principles of Robot Autonomy》前言、§1.2–1.3
> **標記說明**：
> - `【口頭】` 老師口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 老師問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 自動化 vs. 自主](#1-自動化-vs-自主)
- [2. See–Think–Act 循環](#2-seethinkact-循環)
- [3. 課程行政](#3-課程行政)
- [4. 為什麼需要運動模型](#4-為什麼需要運動模型)
- [5. 廣義座標與組態空間](#5-廣義座標與組態空間)
- [6. 完整約束（holonomic constraints）](#6-完整約束holonomic-constraints)
- [7. 運動學約束與 Pfaffian 形式](#7-運動學約束與-pfaffian-形式)
- [8. 非完整約束（nonholonomic constraints）](#8-非完整約束nonholonomic-constraints)
- [9. 例子：在平面上滾動的輪子](#9-例子在平面上滾動的輪子)
  - [9.1 推出「不打滑」約束](#91-推出不打滑約束)
  - [9.2 為什麼它是非完整約束](#92-為什麼它是非完整約束)
- [10. 輪子的種類](#10-輪子的種類)
- [11. 從約束推出運動學模型](#11-從約束推出運動學模型)
  - [11.1 一般步驟](#111-一般步驟)
  - [11.2 Unicycle 模型](#112-unicycle-模型)
- [12. 差速驅動機器人](#12-差速驅動機器人)
  - [12.1 為什麼跟 unicycle 一樣](#121-為什麼跟-unicycle-一樣)
  - [12.2 左右輪轉速 ↔ $v$、$\omega$](#122-左右輪轉速--v-omega)
- [13. 簡單車模型及其變形](#13-簡單車模型及其變形)
- [14. 從運動學模型到動力學模型](#14-從運動學模型到動力學模型)
- [15. 一頁速查表](#15-一頁速查表)
- [16. 與後續集數的連結](#16-與後續集數的連結)

---

## 0. 這堂課要做什麼

前 20 分鐘是課程介紹，後 55 分鐘開始第一個技術主題：**移動機器人的運動學模型**。

| 主題 | 課本 |
|---|---|
| 自動化 vs. 自主、See–Think–Act | 前言 |
| 廣義座標、完整／非完整約束、Pfaffian 形式 | §1.2.1–1.2.4 |
| Unicycle、差速驅動、簡單車模型 | §1.3.1–1.3.3 |
| 加積分器的動態延伸 | §1.3（Example 1.3.1） |

課本 §1.1（狀態空間模型）、§1.2.5（動力學、Lagrange 法）、§1.4（數值模擬）本集沒講。

---

## 1. 自動化 vs. 自主

[▶ 01:44](https://youtu.be/Lgt5ONBtFI0?t=104)

- **自動化（automation）**：機器人可能遇到的**每一種情況，在設計時就能預先想到**。所有動作都由工程師事先寫好，機器人不會碰到意外。例子：工廠裡組裝汽車的機械手臂（老師放的是 Fiat 500 的組裝線）。
- **自主（autonomy）**：機器人要處理**設計時想不到的情況**，所以它必須自己會「推理」。例子：自駕車要緊急閃避一個突然衝上馬路的小孩。

> ⚠️ 逐字稿缺字 [▶ 02:54](https://youtu.be/Lgt5ONBtFI0?t=174)：Whisper 寫「avoid a key that is suddenly crossing the road… because the key is changing a duck」，依上下文應是「a **kid** … **chasing** a duck」（小孩在追鴨子）。

`【口頭】` 老師舉的應用：自駕車、送貨無人機（Amazon）、飛行汽車（Airbus 原型）、小型送貨車、手術機器人。手術機器人現在幾乎都是醫生遙控（teleoperation）；下一步是讓機器人在少量監督下自己做。老師自己也做太空機器人。

【課本補充】前言另外區分了「自主」和「人工智慧（AI）」：自主的重點是**主動做決策**；AI 是一大類工具，提供自主需要的計算方法。

---

## 2. See–Think–Act 循環

[▶ 05:02](https://youtu.be/Lgt5ONBtFI0?t=302)

要讓機器人自己做決定，就要設計它的**自主堆疊（autonomy stack）**——一整套軟體模組。架構有很多種，本課用最常見的 **See–Think–Act 循環**，包含四個能力：

1. **感知（perception）**：用感測器（相機、雷射、雷達……）讀環境，從讀數萃取資訊。「影像裡有人嗎？有球嗎？有樹嗎？」
2. **定位與建圖（localization and map building）**：根據感知資訊，算出機器人在地圖上的位置。地圖可能已知，也可能未知——未知時要**同時定位與建圖**（SLAM, Simultaneous Localization and Mapping）。
3. **決策（decision making）**：知道自己在哪後，決定下一步做什麼。例：自駕車要不要換車道、要不要超車。通常要考慮環境和周圍其他人（例如人開的車）的不確定性。
4. **軌跡最佳化與控制（trajectory optimization and control）**：把高階決定翻成一條要跟的軌跡，再送出控制指令去跟它。

機器人動了 → 環境改變 → 再從頭感知，形成循環。

課程的**四大模組**就照這四個能力排：

| 模組 | 內容 |
|---|---|
| 1 | 運動規劃與控制（motion planning and control） |
| 2 | 機器人感知（robotic perception） |
| 3 | 定位與 SLAM |
| 4 | 決策：狀態機（state machines），稍微碰一點強化學習 |

> ⚠️ 逐字稿缺字 [▶ 07:40](https://youtu.be/Lgt5ONBtFI0?t=460)：Whisper 寫「localization in slum」，應是「localization and **SLAM**」。

【課本補充】課本的圖（前言 Figure 2）把它畫成三段：See（感測、感知）→ Think（濾波、定位建圖、決策）→ Act（軌跡生成、運動規劃、致動器控制）。課本也提到它和 OODA 循環（observe–orient–decide–act）同一個想法。

---

## 3. 課程行政

[▶ 07:26](https://youtu.be/Lgt5ONBtFI0?t=446)

`【口頭】` 重點整理：

- **很跨領域**：好處是你會懂整個自主堆疊；老師說很多人只懂其中一塊，這會妨礙你當機器人學家。壞處是數學和程式都會被「拉伸」。
- **要碰硬體**：期末要把自己一路寫的軟體裝到真機器人上，「debug 到天荒地老」是機器人學家的日常，「挫折是機器人學家的 DNA」。
- **先修**：程式、微積分與線性代數、機率與統計。助教不會教特徵值或基本 Python。會發一份不計分的自我檢測小考。
- **評分**：期中考兩次（10 月、11 月）各 15%、期末專題、作業（4 份 problem set）40%、每週 section 出席，另有 Piazza 好問題／好回答最多 5% 加分。
  > ⚠️ 待確認 [▶ 11:04](https://youtu.be/Lgt5ONBtFI0?t=664)：Whisper 寫專題「50%」、section「50%」，加起來超過 100%，應是聽錯；確切比例待補。
- **期末專題**：用一台差速驅動小車（上面有雷射、相機、強力處理器，感測器配置像自駕車），所有模組都在車上跑。去年的題目：在模擬城市裡自己開車，要偵測交通號誌 → 放進地圖 → 認出是停車標誌還是速限標誌 → 照著做，最後比賽。
- 5 位助教；用老師的 Autonomous Systems Lab 和 Stanford 汽車研究中心（CARS）的設備。
  > ⚠️ 逐字稿缺字 [▶ 13:18](https://youtu.be/Lgt5ONBtFI0?t=798)：Whisper 寫「Autonomous Assistance Lab」「CODERAC」，依上下文應是 Autonomous **Systems** Lab、**CARS**（Center for Automotive Research at Stanford）。
- 第 3 模組要先補機率和濾波理論，再用卡爾曼濾波（Kalman filtering）和粒子濾波（particle filtering）做定位與建圖。
  > ⚠️ 逐字稿缺字 [▶ 14:19](https://youtu.be/Lgt5ONBtFI0?t=859)：Whisper 寫「camera filtering」，應是「**Kalman** filtering」。

**Q&A**（[▶ 14:43](https://youtu.be/Lgt5ONBtFI0?t=883)）

- `【Q&A】` 會擴大名額嗎？→ 不會。只有 30 台機器人，4 人一組，沒辦法再多。
- `【Q&A】` 今年第一次拆成 A、B 兩門，怎麼銜接？→ 這是兩部曲的第一部。冬季的 AA274B（進階版）也有四個模組：(1) 學習式控制與感知（本課幾乎不用學習方法，都是古典方法）；(2) 自主系統的驗證與確認，以及 See–Think–Act 以外的架構；(3) 和人互動的模型與演算法（意圖建模等）；(4) 移動操作（mobile manipulation）。作業一樣是在本學期的堆疊上繼續加功能。
  > ⚠️ 待確認 [▶ 15:21](https://youtu.be/Lgt5ONBtFI0?t=921)：B 課的共同授課者，Whisper 寫「Professor Dorso-Sevic and Jeanette Balck」，人名聽不清，待確認。
- `【口頭】` 週五有一門 1 學分的機器人研討會，推薦去聽。本課有 3 學分和 4 學分兩種，4 學分多一份期末的論文評論。
- `【Q&A】` 跟去年單一學期的 274 一樣嗎？→ 相似但不等於。以前內容塞太滿；今年把機器學習的部分移到 B 課，多加了週五一堂課講更深入的細節，還新增「多感測器融合」一週和幾堂「自駕車開源軟體」。
- `【Q&A】` 選 CS237A 或 EE260A 的人也要上週五的課嗎？→ 要。只有選 AA174A（大學部版）的人不用。
- `【Q&A】` 期中考在課堂上考嗎？→ 是，時間不行可以另約。
- `【Q&A】` 為什麼不同系的候補名單人數不一樣？→ 老師也不清楚註冊組怎麼運作，但應該最後是合成一份候補名單。

---

## 4. 為什麼需要運動模型

[▶ 20:39](https://youtu.be/Lgt5ONBtFI0?t=1239)

第一模組是控制與規劃，而**做控制與規劃要先有模型**。本課主要看**移動系統**（自駕車、無人機……）；手術機器人那種底座固定的不算。

模型最重要的是寫出「運動必須遵守的**約束**」。老師的例子：

> 開車時你知道車**不能橫著移動**；但只要沒有障礙物，把前進、後退幾個動作接起來，**你哪裡都去得了**。

我們要的模型，就是要能做這種推理：每一瞬間能怎麼動有限制，但整體能到哪裡沒有限制。這正是後面「非完整約束」的意思。

---

## 5. 廣義座標與組態空間

[▶ 22:16](https://youtu.be/Lgt5ONBtFI0?t=1336)

- **廣義座標（generalized coordinates）** $\xi$：能完整描述機器人姿態（pose）的**最少**一組座標。
- **組態空間（configuration space）**：所有可能的 $\xi$ 組成的空間。

**例：直立滾動的輪子**（想成一枚硬幣立著在桌上滾）。輪子所在的平面叫**矢狀面（sagittal plane）**，它垂直於地面。

$$
\xi = \left[ x,\ y,\ \theta \right]^\top
$$

- $(x, y)$：輪子中心（或接觸點）的位置。
- $\theta$：輪子相對某個參考軸的朝向（heading）。

所以組態空間是三維的。`【口頭】` 真的輪子會倒，這裡假設理想世界，輪子永遠保持直立。

**運動（motion）／軌跡（trajectory）**：組態隨時間變化的函數 $t \mapsto \xi(t) \in \mathbb{R}^n$。unicycle 的 $n = 3$。

【課本補充】§1.2.1：同一個組態可以有不同的廣義座標選法，例如輪子位置也能改用極座標表示。課本另外強調，組態 $q$ 通常只是完整「狀態」的一部分，狀態常常還包含速度 $\dot q$。

---

## 6. 完整約束（holonomic constraints）

[▶ 24:01](https://youtu.be/Lgt5ONBtFI0?t=1441)

**定義**：只牽涉到組態變數、**不牽涉到它們的導數**的約束：

$$
h_i(\xi) = 0, \qquad i = 1, \dots, k
$$

**效果**：把機器人能到的組態，限制在函數 $h_i$ 的**等值集（level set）** 上。有 $k$ 個獨立的完整約束，可到達的空間就從 $n$ 維降成 $n-k$ 維。

**從哪來**：通常來自**機械連接**，例如機械手臂的關節。

**例：兩節用旋轉關節（revolute joint）接起來的手臂**（[▶ 25:22](https://youtu.be/Lgt5ONBtFI0?t=1522)）

- 每一節都是平面上的剛體，各要 3 個變數：第 1 節 $(x_1, y_1, \theta_1)$，第 2 節 $(x_2, y_2, \theta_2)$。$(x_i,y_i)$ 取在兩節相接的那個點。合起來名義上 6 維。
- 旋轉關節讓兩節在接點黏在一起：

$$
h_1:\ x_1 - x_2 = 0, \qquad h_2:\ y_1 - y_2 = 0
$$

- `【課堂討論】` 老師問：那需要幾個變數才能描述整個系統？學生答「4」。老師：對，就是 $6 - 2 = 4$（原本的變數數減掉完整約束數）。一種選法是 $(x_1, y_1, \theta_1)$ 加上**兩節的相對角度**（也就是關節角）。
- `【口頭】` 對有旋轉、滑動（prismatic）關節的手臂，關節角就是常用的精簡座標。

【課本補充】§1.2.2 的單擺例子：用 $(x, y)$ 描述擺錘，桿長固定給出完整約束 $x^2 + y^2 - L^2 = 0$；改用角度 $\theta$ 就只要 1 個變數，約束自動滿足。

---

## 7. 運動學約束與 Pfaffian 形式

[▶ 27:50](https://youtu.be/Lgt5ONBtFI0?t=1670)

**運動學約束（kinematic constraints）**：同時牽涉到廣義座標 $\xi$ 和**廣義速度** $\dot\xi$（點表示對時間微分）的約束。它限制的是系統**每一瞬間能怎麼動**，也就是限制速度向量。例：車子不能橫著移動。

**Pfaffian 形式**：對 $\dot\xi$ 是**線性**的約束（對 $\xi$ 可以是非線性）：

$$
a_i^\top(\xi)\,\dot\xi = 0, \qquad i = 1, \dots, k
$$

**完整約束 ⇒ Pfaffian 約束**（[▶ 29:15](https://youtu.be/Lgt5ONBtFI0?t=1755)）。對 $h_i(\xi) = 0$ 兩邊對時間微分，右邊是 0 的導數還是 0；左邊用連鎖律：

$$
\frac{d}{dt} h_i(\xi(t)) = \frac{\partial h_i}{\partial \xi}\,\dot\xi = 0
$$

所以取 $a_i^\top(\xi) = \dfrac{\partial h_i}{\partial \xi}$，就得到 Pfaffian 形式。

**反過來呢？**（[▶ 30:02](https://youtu.be/Lgt5ONBtFI0?t=1802)）給一個 Pfaffian 約束 $a^\top(\xi)\dot\xi = 0$，是否一定找得到函數 $h$ 使 $\dfrac{d}{dt}h(\xi) = a^\top(\xi)\dot\xi$？

- `【課堂討論】` 學生問「$h$ 也要等於 0 嗎？」→ 老師：是，完整約束就是 $h = 0$，所以它的時間導數才是 0。另一位學生說「好像總能積分回去，除非函數很怪」。→ 老師：這就是**可積性問題（integrability problem）**，比那複雜，但**簡短答案是：不一定**。

`【口頭】` 老師說會用例子說明為什麼物理上可能不可積（見第 9 節）。

---

## 8. 非完整約束（nonholonomic constraints）

[▶ 32:03](https://youtu.be/Lgt5ONBtFI0?t=1923)

**定義**：**無法積分成完整約束**的運動學約束，叫非完整約束。

看一個 Pfaffian 約束 $a^\top(\xi)\dot\xi = 0$ 的兩種情況：

| | 情況 1：可積（完整） | 情況 2：不可積（非完整） |
|---|---|---|
| 條件 | 存在 $h$ 使 $h(\xi) = 0$ 且 $\frac{d}{dt}h = a^\top\dot\xi$ | 找不到這樣的 $h$ |
| 限制什麼 | **能到哪裡**：只能待在 $h$ 的某個等值集上 | **每一瞬間能往哪動**：不是每個速度都允許 |
| 可到達空間 | 降成 $n-1$ 維 | **不受限**，可能到得了任何組態 |
| 例子 | $\xi = (x_1, x_2)$，$x_1 + x_2 = 0$ → 只能在一條直線上動，不是整個平面 | 車子：橫向速度不允許，但接幾個動作就能到平面上任何點 |

一句話：**完整約束限制「能到哪」，非完整約束限制「怎麼走」。**

【課本補充】§1.2.3 的說法：非完整約束把 $\dot\xi$ 限制在一個 $(n-k)$ 維子空間（$A^\top(\xi)$ 的零空間），但不降低組態空間本身的維度。

---

## 9. 例子：在平面上滾動的輪子

[▶ 35:32](https://youtu.be/Lgt5ONBtFI0?t=2132)

設定：一個輪子在 $xy$ 平面上滾，輪子平面（矢狀面）垂直於地面，像硬幣立著滾。$\xi = (x, y, \theta)$。

假設**純滾動、不打滑（rolling without slipping）**：接觸點的速度**在垂直於矢狀面的方向上分量為 0**。白話：輪子**不能往側邊滑**。

### 9.1 推出「不打滑」約束

`【課堂討論】` 這一段是老師邊問邊推。

**Step 1：朝向的單位向量。** 令 $e_v$ 是輪子朝向（也就是接觸點速度方向）的單位向量。$\theta$ 是它和 $x$ 軸的夾角，長度為 1，所以

$$
e_v = \left[ \cos\theta,\ \sin\theta \right]^\top
$$

（學生答出 $\cos\theta$、$\sin\theta$。）

> `【Q&A】` [▶ 37:50](https://youtu.be/Lgt5ONBtFI0?t=2270)：學生問了一個關於 $\theta$ 的問題（Whisper 沒錄到問題本身）。老師回答：$\theta$ 是**硬幣的朝向**；這個向量躺在地面上，硬幣永遠垂直地面，$\theta$ 是硬幣面和參考軸的夾角。

**Step 2：側向的單位向量。** 令 $e_v^\perp$ 是和 $e_v$ 垂直、指向側邊的單位向量。它和 $x$ 軸的夾角是 $\frac{\pi}{2} - \theta$，而且在 $x$ 軸下方，所以

$$
e_v^\perp = \left[ \cos\left( \tfrac{\pi}{2} - \theta \right),\ -\sin\left( \tfrac{\pi}{2} - \theta \right) \right]^\top = \left[ \sin\theta,\ -\cos\theta \right]^\top
$$

**檢查垂直**：$e_v \cdot e_v^\perp = \cos\theta\sin\theta - \sin\theta\cos\theta = 0$。✓

**Step 3：寫成約束。** 速度向量 $v = (\dot x, \dot y)$ 在側向沒有分量，也就是 $v \perp e_v^\perp$：

$$
\left[ \dot x,\ \dot y \right] \cdot e_v^\perp = \dot x \sin\theta - \dot y \cos\theta = 0
$$

**Step 4：寫成對整個 $\dot\xi$ 的標準 Pfaffian 形式。** 補一個 0 給 $\dot\theta$：

$$
a^\top(\xi)\,\dot\xi = \left[ \sin\theta,\ -\cos\theta,\ 0 \right] \begin{bmatrix} \dot x \\ \dot y \\ \dot\theta \end{bmatrix} = 0
$$

> `【Q&A】` [▶ 44:33](https://youtu.be/Lgt5ONBtFI0?t=2673)：學生問怎麼從 $\dot x\sin\theta - \dot y\cos\theta = 0$ 變成「向量乘 $\dot\xi$」。老師：$\dot\xi = (\dot x, \dot y, \dot\theta)$，第三個分量放 0，乘 $\dot\theta$ 就消掉了，結果一樣。這樣寫是因為 Pfaffian 約束的標準寫法是對**全部**組態變數，不只對 $x, y$。

它是 Pfaffian：對 $\dot\xi$ 線性；對 $\xi$ 非線性（透過 $\sin$、$\cos$）。

### 9.2 為什麼它是非完整約束

[▶ 42:11](https://youtu.be/Lgt5ONBtFI0?t=2531)

這個約束只說「不能側滑」，**不會讓你失去可到達性**。老師用**三段式走法**說明，任給起點 $(x_0, y_0, \theta_0)$ 和終點 $(x_f, y_f, \theta_f)$：

1. 原地旋轉，轉到朝向終點的方向。
2. 直線開到終點位置。
3. 原地旋轉，把朝向對齊 $\theta_f$。

每一段都沒有側滑，所以都滿足約束。因此**任何組態都到得了**。

為什麼這就證明「不可積」：以下**不是逐字稿內容**，是依第 8 節的對照表補上的一步。假設約束可積，存在 $h$ 使 $h(\xi) = 0$；那麼所有可行的運動都被困在 $h$ 的某個等值集裡，這是三維空間裡的二維曲面，有些組態到不了。可是三段式走法說明每個組態都到得了，矛盾。所以找不到這樣的 $h$，約束是非完整的。

> `【Q&A】` [▶ 43:12](https://youtu.be/Lgt5ONBtFI0?t=2592)：學生問：這裡對 $\dot\theta$（原地轉的速度）沒有任何限制嗎？→ 老師：這裡沒有。其他系統可能有。後面會把模型改得更實際——角速度無上限的模型沒有用，沒有機器人做得到。這裡只是先把非完整約束的觀念講清楚。

**重點**（[▶ 43:45](https://youtu.be/Lgt5ONBtFI0?t=2625)）：

| 系統 | 主要受哪種約束 |
|---|---|
| 機械手臂（manipulator） | 完整約束（關節） |
| 輪式系統（wheeled system） | 非完整約束（輪子不能側滑） |

【課本補充】§1.2.3 用同一個例子，另外指出：$a^\top(\xi)$ 的零空間由 $[\cos\theta, \sin\theta, 0]^\top$（滾動方向）和 $[0, 0, 1]^\top$（原地旋轉）張成。這正是第 11 節要用的。

---

## 10. 輪子的種類

[▶ 44:07](https://youtu.be/Lgt5ONBtFI0?t=2647)

`【口頭】` 課本沒有這一段。

| 種類 | 描述 | 例子 |
|---|---|---|
| **固定標準輪**（fixed standard wheel） | 只能繞穿過輪心、垂直矢狀面的軸轉（就是正常滾）；**不能**繞垂直軸轉向 | 購物車的後輪 |
| **可轉向標準輪**（steerable standard wheel） | 同上，但**可以**繞垂直軸轉向；垂直軸穿過輪心和接觸點 | 汽車前輪 |
| **腳輪**（caster wheel） | 輪心和它接到車身的點**有偏移**，所以垂直轉軸**不穿過輪心**。好處：會自動對齊側向運動 | 購物車的前輪 |

`【口頭】` 購物車：後輪給穩定性，前輪（腳輪）給機動性。你一轉彎，前輪馬上自己對齊。

- **主動（active）**：有致動器（actuator，例如馬達）可以控制它。
- **被動（passive）**：像購物車前輪，自己順著運動方向對齊。

還有瑞典輪（Swedish wheel）、全向輪（omnidirectional wheel）等，本課不管。

---

## 11. 從約束推出運動學模型

### 11.1 一般步驟

[▶ 48:17](https://youtu.be/Lgt5ONBtFI0?t=2897)

輪式系統通常每個輪子給一個「不側滑」約束；$k$ 個輪子就有 $k$ 個約束。把它們**疊成矩陣**：

$$
a_1^\top(\xi)\dot\xi = 0,\ \dots,\ a_k^\top(\xi)\dot\xi = 0
\quad\Longleftrightarrow\quad
A^\top(\xi)\,\dot\xi = 0,
\qquad
A^\top(\xi) = \begin{bmatrix} a_1^\top(\xi) \\ \vdots \\ a_k^\top(\xi) \end{bmatrix} \in \mathbb{R}^{k \times n}
$$

> `【Q&A】` [▶ 49:07](https://youtu.be/Lgt5ONBtFI0?t=2947)：運動學約束一定能寫成 Pfaffian 形式嗎？→ 不一定。但輪子的約束通常是 Pfaffian，本課主要看輪式系統，所以會看到的都是 Pfaffian。

> `【Q&A】` [▶ 50:14](https://youtu.be/Lgt5ONBtFI0?t=3014)：$A^\top$ 是什麼？→ 就是把每個 Pfaffian 約束的列向量 $a_i^\top$ 一列一列疊起來的矩陣，讓一堆約束變成一個矩陣式子。
> ⚠️ 逐字稿缺字 [▶ 50:34](https://youtu.be/Lgt5ONBtFI0?t=3034)：老師舉 unicycle 的 $a_1$，Whisper 寫「minus cosine of theta 0」，掉了前面的 $\sin\theta$；依第 9 節應是 $a_1^\top = [\sin\theta, -\cos\theta, 0]$。

**關鍵觀察**：$A^\top(\xi)\dot\xi = 0$ 的意思是，在組態 $\xi$ 下，**允許的速度 $\dot\xi$ 必須在 $A^\top(\xi)$ 的零空間（null space，又叫核 kernel）裡**。

`【課堂討論】` [▶ 51:25](https://youtu.be/Lgt5ONBtFI0?t=3085)：組態空間 3 維、只有 1 個約束（$A^\top$ 只有 1 列），零空間幾維？學生答 2。（秩–零度定理：$3 - 1 = 2$。）

零空間有一組基底 $g_1(\xi), \dots, g_{n-k}(\xi)$，所以任何允許的速度都能寫成它們的線性組合：

$$
\dot\xi = \sum_{j=1}^{n-k} g_j(\xi)\,u_j = G(\xi)\,u
$$

係數 $u_j$ 就解釋成**控制輸入**。這是一個非線性微分方程，就是機器人的**運動學模型（kinematic model）**。

**演算法：從約束推出運動學模型**

- **在解什麼**：已知機器人的運動學約束，要一個「輸入 → 速度」的模型，而且保證任何輸入都不違反約束。
- **步驟**：
  1. 寫出每個約束的 Pfaffian 形式 $a_i^\top(\xi)\dot\xi = 0$。
  2. 疊成約束矩陣 $A^\top(\xi)$。
  3. 求 $A^\top(\xi)$ 的零空間，挑一組基底 $g_1, \dots, g_{n-k}$（基底可自由選，挑物理意義好的）。
  4. 模型就是 $\dot\xi = \sum_j g_j(\xi) u_j$。
- **為什麼保證滿足約束**【課本補充，§1.2.4】：代回去，$A^\top G u = \sum_j (A^\top g_j) u_j = \sum_j 0 \cdot u_j = 0$，因為每個 $g_j$ 都在零空間裡。
- **什麼時候會失敗**：
  - 約束不是 Pfaffian 形式時，這套線性代數做不下去（第 49:07 的 Q&A）。
  - 有些約束是**重複**的（例如差速驅動的兩個後輪，見 12.1）。不先合併的話，$A^\top$ 的列不獨立，零空間維度要用秩算，不能直接用 $n - k$。
  - 得到的模型只管「速度方向」，不管速度能多大、要多少力——輸入沒上下限時不實際（見 11.2、第 14 節）。

`【口頭】` 本課其實只會用到一個運動學模型；講這套框架是讓你知道這些模型從哪來。以後要控制飛機、車子、拖車，可以去查現成的模型表（老師之後給參考書），不用自己推。

### 11.2 Unicycle 模型

[▶ 53:31](https://youtu.be/Lgt5ONBtFI0?t=3211)

從第 9 節的純滾動約束出發，只有一個約束：

$$
A^\top(\xi) = a^\top(\xi) = \left[ \sin\theta,\ -\cos\theta,\ 0 \right]
$$

組態空間 3 維 → 零空間 2 維 → 要 2 個基底向量。一組方便的選法：

$$
g_1 = \begin{bmatrix} \cos\theta \\ \sin\theta \\ 0 \end{bmatrix}, \qquad
g_2 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
$$

**檢查在零空間裡**：

- $a^\top g_1 = \sin\theta\cos\theta - \cos\theta\sin\theta + 0 = 0$ ✓
- $a^\top g_2 = 0 + 0 + 0 = 0$ ✓
- 兩者明顯線性獨立 ✓

所以得到著名的 **unicycle 模型**：

$$
\begin{bmatrix} \dot x \\ \dot y \\ \dot\theta \end{bmatrix}
= \begin{bmatrix} \cos\theta \\ \sin\theta \\ 0 \end{bmatrix} v
+ \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \omega
$$

兩個輸入有物理意義：

- $v$：接觸點的速度大小（往前開多快）。
- $\omega = \dot\theta$：角速度（轉多快）。

`【口頭】` 這就是本學期用來控制那台機器人的模型，原因見第 12 節。

**加上界限**（[▶ 56:04](https://youtu.be/Lgt5ONBtFI0?t=3364)）：實際上要加最大速度、最大角速度：

$$
|v| \le v_{\max}, \qquad |\omega| \le \omega_{\max}
$$

---

## 12. 差速驅動機器人

[▶ 57:06](https://youtu.be/Lgt5ONBtFI0?t=3426)

Unicycle 是理想模型（硬幣會倒）。幸好有一種很實用的機器人，運動學**等同** unicycle：**差速驅動機器人（differential drive robot）**，也就是本學期要用的那台。

結構：

- 後面兩個**固定輪**，各自有馬達 → **主動輪**。
- 前面一個**腳輪** → **被動輪**，自己對齊。
- 兩個後輪可以**分別**控制，例如一個往前、一個往後。

`【課堂討論】` 老師問：一個輪子往前、一個往後會怎樣？學生答：會原地轉。這就是「差速」的意思。

### 12.1 為什麼跟 unicycle 一樣

[▶ 58:34](https://youtu.be/Lgt5ONBtFI0?t=3514)

- 每個後輪各給一個「不側滑」約束，形式和第 9 節一樣。
- `【課堂討論】` 兩個後輪用一根軸連在一起，「左輪不能側滑」是否就代表「右輪不能側滑」？學生答：是。所以兩個約束**重複**，合併成一個。
- 前面的腳輪可以自由對齊側向運動，**沒有**側滑約束。

⇒ 只剩一個約束，和 unicycle 一模一樣，所以運動學相同。

【課本補充】§1.3.2 的驗算：設 $(x,y)$ 是後軸中點、車寬 $L$，兩輪中心

$$
p_l = \begin{bmatrix} x - \frac{L}{2}\sin\theta \\ y + \frac{L}{2}\cos\theta \end{bmatrix}, \qquad
p_r = \begin{bmatrix} x + \frac{L}{2}\sin\theta \\ y - \frac{L}{2}\cos\theta \end{bmatrix}
$$

微分得 $\dot p_l = \left[ \dot x - \frac{L}{2}\dot\theta\cos\theta,\ \dot y - \frac{L}{2}\dot\theta\sin\theta \right]^\top$，代入 $\dot p_l \cdot e_v^\perp$：

$$
\left( \dot x - \tfrac{L}{2}\dot\theta\cos\theta \right)\sin\theta - \left( \dot y - \tfrac{L}{2}\dot\theta\sin\theta \right)\cos\theta = \dot x\sin\theta - \dot y\cos\theta
$$

（含 $\dot\theta$ 的兩項互相消掉。）右輪同理。兩個約束都化成同一條 $\dot x\sin\theta - \dot y\cos\theta = 0$。

**差別在輸入**：unicycle 直接控制 $v$ 和 $\omega$；差速驅動只能控制**兩個輪子的轉速** $\omega_L$、$\omega_R$。所以要找兩者的換算，換算好就能「用 unicycle 模型規劃，再換成左右輪轉速去執行」。

> `【Q&A】` [▶ 61:01](https://youtu.be/Lgt5ONBtFI0?t=3661)：換算一樣，但最大速度的限制不一樣吧？unicycle 可以把最大角速度調很高，差速驅動卻不行。→ 老師：完全正確。運動學一樣是因為約束一樣；但左右輪轉速的界限，會換算成不同形狀的 $v$、$\omega$ 界限。不同的界限會給出不同的子模型（見第 13 節）。

### 12.2 左右輪轉速 ↔ $v$、$\omega$

[▶ 61:53](https://youtu.be/Lgt5ONBtFI0?t=3713)

**瞬時旋轉中心（ICR, instantaneous center of rotation，又叫 instantaneous curvature center）**：車子沿彎路走時，每一瞬間都在繞某一點轉，這一點在兩後輪中心的連線（延長線）上。白話：如果保持當下的速度向量不變，車子會繞這一點畫圓。

記號：

| 符號 | 意思 |
|---|---|
| $\omega$ | 繞 ICR 的角速度（剛體，各點相同） |
| $v$ | 後軸中點的速度 |
| $R$ | 後軸中點到 ICR 的距離（曲率半徑） |
| $L$ | 車寬（兩後輪間距） |
| $v_L, v_R$ | 左、右輪的線速度 |
| $r$ | 輪子半徑 |
| $\omega_L, \omega_R$ | 左、右輪的轉速 |

**Step 1**：繞 ICR 轉，速度 = 角速度 × 半徑。左輪離 ICR $R - \frac{L}{2}$，右輪 $R + \frac{L}{2}$（ICR 在左側時）：

$$
v = \omega R, \qquad
v_L = \omega\left( R - \tfrac{L}{2} \right), \qquad
v_R = \omega\left( R + \tfrac{L}{2} \right)
$$

**Step 2（求 $\omega$）**：右減左，$R$ 消掉：

$$
v_R - v_L = \omega L \quad\Longrightarrow\quad \omega = \frac{v_R - v_L}{L}
$$

> ⚠️ 逐字稿缺字 [▶ 65:02](https://youtu.be/Lgt5ONBtFI0?t=3902)：Whisper 寫「the angular speed is equal to the differential speed over **2**」。但上一行老師剛推出 $v_R - v_L = \omega L$，所以應是「over **L**」（L 和 2 唸起來像）。課本 §1.3.2 也是除以 $L$。

`【課堂討論】` 直覺檢查：$v_R = v_L$ 時角速度是多少？→ 0，合理，車子走直線。若 $v_L = 0$、$v_R \ne 0$，就有角速度，車子**繞左輪**轉。

**Step 3（求 $v$）**：左加右：

$$
v_L + v_R = 2\omega R = 2v \quad\Longrightarrow\quad v = \frac{v_L + v_R}{2}
$$

中點速度就是左右輪速度的平均。

**Step 4（輪速 ↔ 轉速）**：不打滑時，輪子線速度 = 轉速 × 半徑：

$$
v_L = r\,\omega_L, \qquad v_R = r\,\omega_R
$$

> `【Q&A】` [▶ 68:15](https://youtu.be/Lgt5ONBtFI0?t=4095)：學生指出投影片上的式子漏了輪半徑 $r$。老師：對，不然單位對不上，抱歉。

**合起來**（和課本式 1.27 一致）：

$$
v = \frac{r}{2}\left( \omega_R + \omega_L \right), \qquad
\omega = \frac{r}{L}\left( \omega_R - \omega_L \right)
$$

這是一對一的換算，反過來也能解：$\omega_R = \dfrac{1}{r}\left( v + \dfrac{L}{2}\omega \right)$，$\omega_L = \dfrac{1}{r}\left( v - \dfrac{L}{2}\omega \right)$（由上兩式相加減得到）。

**結論**（[▶ 68:41](https://youtu.be/Lgt5ONBtFI0?t=4121)）：差速驅動機器人可以看成一台 unicycle，$v$、$\omega$ 取在**後軸中點**。規劃軌跡時用 unicycle 模型，再用上面的換算求左右輪轉速。下週會講怎麼算軌跡。

---

## 13. 簡單車模型及其變形

[▶ 69:13](https://youtu.be/Lgt5ONBtFI0?t=4153)

> `【Q&A】` 學生問：這個模型會不會有奇異點（singularity），例如腳輪轉到和運動方向垂直的時候？→ 老師：這跟約束怎麼定義有關，並引出下面這個比較複雜的模型，它就可能有奇異點。

**簡單車模型（simple car model）**：後面兩個固定輪（同前），前面改成兩個**可轉向輪**。

- 組態空間變 **4 維**：後軸中點 $(x, y)$、車頭朝向 $\theta$、轉向角 $\phi$（前輪和車身縱軸的夾角）。
- 約束有 **2 個，而且不重複**：後輪不側滑、前輪不側滑。
- 4 個變數、2 個獨立約束 → 零空間 2 維 → **2 個控制輸入**：速度 $v$、轉向角 $\phi$。

老師沒在課堂推這個模型的式子。【課本補充】§1.3.3 給出（課本叫 bicycle/simple car model，把左右兩輪合成一個）：

$$
\dot x = v\cos\theta, \qquad
\dot y = v\sin\theta, \qquad
\dot\theta = \frac{v}{L}\tan\phi
$$

這裡 $L$ 是**軸距**（前後軸距離），不是第 12 節的車寬。狀態 $(x, y, \theta)$，輸入 $(v, \phi)$。

> `【Q&A】` [▶ 71:06](https://youtu.be/Lgt5ONBtFI0?t=4266)：這就是自行車模型（bicycle model）嗎？→ 是。

**依輸入界限分出的子模型**（[▶ 71:16](https://youtu.be/Lgt5ONBtFI0?t=4276)）：

| 模型 | 速度 $v$ | 轉向角 $\phi$ |
|---|---|---|
| 簡單車（simple car） | $|v| \le v_{\max}$ | $|\phi| \le \phi_{\max} < \frac{\pi}{2}$ |
| Reeds–Shepp 車 | 只能取最大前進或最大後退速度：$v \in \{ -v_{\max}, v_{\max} \}$ | 同上 |
| Dubins 車 | 只能取最大前進速度：$v = v_{\max}$ | 同上 |

- $\phi < \frac{\pi}{2}$ 是為了**避開奇異點**：$\phi = \frac{\pi}{2}$ 時 $\tan\phi$ 發散。
- Reeds–Shepp 常用在運動規劃；Dubins 本課也會用。

> ⚠️ 逐字稿缺字 [▶ 71:50](https://youtu.be/Lgt5ONBtFI0?t=4310)：Whisper 寫「Ritz ship car」，應是「**Reeds–Shepp** car」。表中各模型的具體不等式依口述和慣例寫出，投影片原式沒唸，待確認。

**參考書**（[▶ 72:08](https://youtu.be/Lgt5ONBtFI0?t=4328)）：老師推薦兩本：一本講怎麼推這些模型、包括奇異點（投影片上的書名沒唸出來）；另一本是 Steve LaValle 的 *Planning Algorithms*（老師稱 *Motion Planning*），列了很多機器人用的運動學模型。

---

## 14. 從運動學模型到動力學模型

[▶ 72:27](https://youtu.be/Lgt5ONBtFI0?t=4347)

> `【Q&A】` 學生問：為什麼轉向角不算在（模型的）組態變數裡？→ 老師用最後一張投影片回答（就是這一節）：運動學模型只是一個子系統，轉向角可以再加回狀態裡。

**警告**：運動學狀態空間模型，永遠只該看成**更完整的動力學模型裡的一個子系統**。（呼應學生問題：為什麼模型裡沒有 $\ddot x$、加速度？）

兩種常見做法：

1. **黑盒分工**：規劃軌跡時用運動學模型，因為比較好最佳化。再假設有一個底層模組，把想要的運動學量（速度 $v$、角速度 $\omega$）翻成真正處理動力學（加速度、角加速度）的控制訊號。這最常見。
2. **把模型做準一點**：在輸入前面**加積分器**。
   - Unicycle：把 $v$ 變成狀態變數，新增 $\dot v = a$，新的輸入是加速度 $a$。（第一份作業就會做這個。）
   - 簡單車：把轉向角 $\zeta$ 變成狀態變數，新增 $\dot\zeta = u_\zeta$，新的輸入是轉向速率（slew rate）。

【課本補充】Example 1.3.1 寫出 unicycle 的動態延伸：狀態 $(x, y, \theta, v)$、輸入 $(\omega, a)$：

$$
\dot x = v\cos\theta, \qquad \dot y = v\sin\theta, \qquad \dot\theta = \omega, \qquad \dot v = a
$$

**取捨**（[▶ 74:06](https://youtu.be/Lgt5ONBtFI0?t=4446)）：

- 模型要**夠像**真實動力學，規劃出來的軌跡才做得到。
- 模型又**不能太複雜**，因為軌跡最佳化很吃計算（下週會看到），模型太複雜就算太久。
- 怎麼平衡「某種程度上是門藝術」。本課會針對輪式系統，特別是差速驅動機器人，示範怎麼平衡。

**下一步**：下一堂介紹 ROS（機器人作業系統）；週五是一家自駕卡車公司的 CEO 來講把自主系統放到真實世界的挑戰；下週講軌跡最佳化、軌跡追蹤與控制。

---

## 15. 一頁速查表

### 約束分類

| | 形式 | 限制 | 來源 |
|---|---|---|---|
| 完整 | $h_i(\xi) = 0$ | 能到哪（降成 $n-k$ 維） | 關節、機械連接 |
| 運動學（Pfaffian） | $a_i^\top(\xi)\dot\xi = 0$ | 每一瞬間能往哪動 | 輪子不側滑 |
| 非完整 | Pfaffian 但積不回 $h(\xi) = 0$ | 只限制怎麼走，不限制能到哪 | 輪子不側滑 |

- **完整 ⇒ Pfaffian**：$\frac{d}{dt}h_i(\xi) = \frac{\partial h_i}{\partial\xi}\dot\xi = 0$，取 $a_i^\top = \frac{\partial h_i}{\partial\xi}$。
- **Pfaffian ⇏ 完整**：反例是滾動輪子；用三段式走法證明哪都到得了，所以不可能被困在等值集上。

### 滾動不打滑

- $e_v = [\cos\theta, \sin\theta]^\top$，$e_v^\perp = [\sin\theta, -\cos\theta]^\top$（關鍵：側向速度 $(\dot x, \dot y)\cdot e_v^\perp = 0$）。
- 約束：$\dot x\sin\theta - \dot y\cos\theta = 0$，即 $[\sin\theta, -\cos\theta, 0]\,\dot\xi = 0$。

### 從約束到模型

$A^\top(\xi)\dot\xi = 0$ ⇒ $\dot\xi \in \ker A^\top(\xi)$ ⇒ $\dot\xi = \sum_j g_j(\xi)u_j$，$g_j$ 是零空間的基底（關鍵：$A^\top g_j = 0$ 保證任何 $u$ 都滿足約束）。

### 模型總表

| 模型 | 式子 | 狀態／輸入 |
|---|---|---|
| Unicycle | $\dot x = v\cos\theta,\ \dot y = v\sin\theta,\ \dot\theta = \omega$ | $(x,y,\theta)$ / $(v,\omega)$ |
| 差速驅動 | 同 unicycle，加換算 $v = \frac{r}{2}(\omega_R + \omega_L)$，$\omega = \frac{r}{L}(\omega_R - \omega_L)$ | $(x,y,\theta)$ / $(\omega_R, \omega_L)$ |
| 簡單車 | $\dot x = v\cos\theta,\ \dot y = v\sin\theta,\ \dot\theta = \frac{v}{L}\tan\phi$（$L$ = 軸距） | $(x,y,\theta)$ / $(v,\phi)$ |
| Reeds–Shepp | 簡單車，$v \in \{\pm v_{\max}\}$ | |
| Dubins | 簡單車，$v = v_{\max}$ | |
| 動態延伸 unicycle | unicycle 加 $\dot v = a$ | $(x,y,\theta,v)$ / $(\omega, a)$ |

**差速驅動換算的關鍵一步**：繞 ICR 轉，$v_L = \omega(R - \frac{L}{2})$、$v_R = \omega(R + \frac{L}{2})$；相減得 $\omega = \frac{v_R - v_L}{L}$，相加得 $v = \frac{v_L + v_R}{2}$；再用 $v_{L,R} = r\,\omega_{L,R}$。

---

## 16. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| ROS（預告） | 第 2 集 |
| Unicycle／差速驅動模型 | 第 3 集軌跡最佳化、第 4 集軌跡追蹤（用它規劃與控制機器人） |
| 動態延伸（加積分器）、模型準確度 vs. 計算量 | 第 3–5 集軌跡最佳化 |
| Dubins、Reeds–Shepp 車、非完整約束 | 第 6–7 集運動規劃 |
| See–Think–Act 四大模組 | 整門課的架構：感知第 8–12、18 集；定位與 SLAM 第 13–17、21 集；決策第 19–20 集 |

---

## 附：本集一句話總結

> **輪子不能側滑是一個「非完整約束」：它限制每一瞬間能往哪動，卻不限制最後能到哪。把這些約束疊成矩陣、取零空間的基底，就得到 unicycle 模型；差速驅動機器人的運動學和它完全一樣，只要把左右輪轉速換算成 $v$、$\omega$。**

---

## ⚠️ 待確認清單

1. 上課日期：只知道是 2019 秋季第一堂，確切日期待補。
2. 講者是 Marco Pavone：依「來自義大利、前 NASA JPL、帶 Autonomous Systems Lab」推斷，影片中沒報名字。
3. [▶ 11:04](https://youtu.be/Lgt5ONBtFI0?t=664) 評分比例：Whisper 給的期末專題、section 比例加起來超過 100%，確切數字待補。
4. [▶ 15:21](https://youtu.be/Lgt5ONBtFI0?t=921) AA274B 的共同授課者姓名，Whisper 聽成「Dorso-Sevic」「Jeanette Balck」，待確認。
5. [▶ 71:16](https://youtu.be/Lgt5ONBtFI0?t=4276) 簡單車／Reeds–Shepp／Dubins 的界限不等式：投影片原式沒唸出來，表格依口述重建。
6. [▶ 72:08](https://youtu.be/Lgt5ONBtFI0?t=4328) 老師推薦的第一本參考書（講運動學模型與奇異點）書名沒唸出來。

---

*筆記依據 Marco Pavone（推斷）「Stanford AA274A Principles of Robotic Autonomy（2019 秋）」Lecture 1 錄影逐字稿（Whisper `medium.en`，1:15:15）與《Principles of Robot Autonomy》前言、§1.2–1.3 整理。*
