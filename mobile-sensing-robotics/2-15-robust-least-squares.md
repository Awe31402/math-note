---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-15
lecture: Robust Least Squares for Graph-Based SLAM
date: 待補（2021 夏季學期）
video: https://youtu.be/z60RbiY18I8
notes: 《視覺 SLAM 十四講》第 2 版 §9.2.4（書頁 251–252，PDF 頁 274–275）；MVG 附錄 6 §A6.8（書頁 616–622，PDF 頁 634–640）
---

# 第 2-15 集 · 圖式 SLAM 的強健最小平方 [▶ 影片](https://youtu.be/z60RbiY18I8)

← 上一集：[2-14-hierarchical-pose-graphs](2-14-hierarchical-pose-graphs.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-17-visual-features-part1](2-17-visual-features-part1.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-15 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:03:11，Whisper `medium.en` 轉錄）＋《視覺 SLAM 十四講》§9.2.4 ＋ MVG §A6.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

（BRIEF 原本寫 MVG §4.7；查過 §4.7 是 RANSAC（留給 2-22），強健代價函數在附錄 6 §A6.8，已更正 BRIEF。）

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 問題：高斯假設與離群值](#1-問題高斯假設與離群值)
- [2. Max-Mixture](#2-max-mixture)
- [3. Dynamic Covariance Scaling](#3-dynamic-covariance-scaling)
- [4. 強健核（M 估計）](#4-強健核m-估計)
- [5. 加權最小平方 = 強健估計](#5-加權最小平方--強健估計)
- [6. 選哪個核？](#6-選哪個核)
- [7. 自適應核（Barron）](#7-自適應核barron)
- [8. 截斷的自適應核與 EM](#8-截斷的自適應核與-em)
- [9. 總結與建議](#9-總結與建議)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

資料關聯不完美（錯的閉合迴圈）時，一般最小平方會被少數離群值拉壞。本集講四種**強健最小平方**：**Max-Mixture**、**Dynamic Covariance Scaling（DCS）**、**強健核**（M 估計），以及**自適應核**（用 EM 估計核的形狀）。

---

## 1. 問題：高斯假設與離群值

[▶ 00:30](https://youtu.be/z60RbiY18I8?t=30)

- 最小化平方誤差和 ⇔ 估計高斯分布的平均（假設所有邊的雜訊都是高斯）。
- 對**感測雜訊**，高斯是不錯的近似；但**資料關聯錯誤**（例如把兩個地標搞混）時，更多機率質量落在分布的**尾巴**，高斯假設不成立。
- 標準最小平方的問題：假設**沒有離群值**。現實中一定有：東西會搞混、感測器不完美、分布可能多峰（高斯只有一個峰）。
- 根源：**平方**。離模型很遠的點，誤差被平方放大 → 少數離群值就能把參數拉離正解。

**現實中何時發生** [▶ 02:39](https://youtu.be/z60RbiY18I8?t=159)：

- 地方長得一樣：大樓裡很多房間很像，機器人搞混 → 錯的閉合迴圈。
- 雜亂或重複結構：林蔭道上等距種的樹，用樹幹定位時容易搞混。
- GPS 多路徑（訊號反射），無法唯一定位。

**例子** [▶ 03:35](https://youtu.be/z60RbiY18I8?t=215)：

- Edwin Olson 團隊的模擬世界：小機器人和幾個箱子，算機器人在每個位置的可能性 → 有一個突出的峰，但明顯是**多峰**分布，用單一高斯不是最好的選擇。
- Intel 實驗室資料集：走廊上兩處的掃描用 ICP 也對得很好 → 產生把兩個其實不同的地方連起來的約束。不常發生，但會發生。
- 加入 1 個離群值：還好（仔細看走廊有點彎）；5 個、10 個：地圖嚴重扭曲，無法導航；再多更糟。

**目標**：即使有離群值（感測器不完美，一般無法消除），最佳化也不受影響，建出的地圖和沒有離群值時幾乎一樣。

---

## 2. Max-Mixture

[▶ 06:17](https://youtu.be/z60RbiY18I8?t=377)

由 Pratik Agarwal 和 Edwin Olson 提出。好處：約束可以有**多個峰**。

**從高斯到高斯和** [▶ 06:37](https://youtu.be/z60RbiY18I8?t=397)：

$$
p(e_{ij}) = \eta\,\exp\!\left( -\tfrac12 e_{ij}^{\mathsf T}\Omega_{ij}e_{ij} \right)
\quad\longrightarrow\quad
p(e_{ij}) = \sum_{k=1}^{K} w_k\,\eta_k\,\exp\!\left( -\tfrac12 e_{ijk}^{\mathsf T}\Omega_{ijk}e_{ijk} \right)
$$

- $w_k$：每個高斯的權重。

**問題** [▶ 08:08](https://youtu.be/z60RbiY18I8?t=488)：取負對數時：

- 單一高斯：$-\log p = \tfrac12 e^{\mathsf T}\Omega e + \text{常數}$ → 正好是最小平方的項。
- 高斯和：$\log$ **不能移進總和裡**（只有乘積才能變成和）→ 得不到最小平方的形式。

**巧思**：粗略近似，把 $\sum$ 換成 $\max$（只管目前最重要的那個峰）→ 名字 max-mixture 的由來 [▶ 09:18](https://youtu.be/z60RbiY18I8?t=558)：

$$
p(e_{ij}) \approx \max_k\; w_k\,\eta_k\,\exp\!\left( -\tfrac12 e_{ijk}^{\mathsf T}\Omega_{ijk}e_{ijk} \right)
$$

$$
-\log p(e_{ij}) \approx \min_k \left[ \tfrac12 e_{ijk}^{\mathsf T}\Omega_{ijk}e_{ijk} - \log(w_k\eta_k) \right]
$$

- $\log$ 可以移進 $\max$ 裡 → 每一項又是二次式。
- 近似誤差：兩個峰離得遠（且變異小）時，重疊部分很小，誤差很小；峰很近時誤差較大。但講者認為真正的多峰通常離得比較遠。
- 圖示 [▶ 10:34](https://youtu.be/z60RbiY18I8?t=634)：兩個高斯的「和」和「取最大」只在重疊處不同；峰越遠差越小。

**怎麼放進最小平方** [▶ 12:33](https://youtu.be/z60RbiY18I8?t=753)：

1. 每一輪，對每個多峰約束，計算**所有 $K$ 個成分**的誤差。
2. 選負對數概似最小（最能解釋觀測）的成分。
3. 當作單一高斯，照常做最小平方。
4. **每輪重選**：圖的組態改變，可能跳到另一個成分（通常只在最佳化初期）。

- 每一輪內部和原本完全一樣（局部仍是二次式），**Jacobian 都能沿用**。

**用來剔除離群值** [▶ 15:37](https://youtu.be/z60RbiY18I8?t=937)：

- 兩個成分：閉合迴圈的高斯（窄）＋ 一個**很寬**的高斯（變異很大，表示「其他都可能」）。
- 閉合迴圈符合目前估計 → 用窄的；不符合 → 用寬的，即使差 20～50 公尺，對整體影響也很小。
- 誤差函數：近處是窄的二次、遠處是很寬的二次，形狀和 **corrupted Gaussian** 很像，只在切換處略有差異。

**其他用途** [▶ 17:07](https://youtu.be/z60RbiY18I8?t=1027)：

- 資料關聯歧義：「我在這裡、或那裡、或其他任何地方」→ 多個成分。
- **輪子打滑**：里程計約束可以是「照預期往前走」（窄高斯）或「幾乎沒動」（另一個高斯）——不只處理資料關聯，也處理平台運動學的問題。

**結果** [▶ 13:55](https://youtu.be/z60RbiY18I8?t=835)：

- Intel 資料集：紅線是離群的閉合迴圈（約 10 個、更多到 50 或 100 個），標準最小平方壞掉，max-mixture 能分辨哪些是錯的、等於把它們停用。
- 計算負擔小（圖：藍色標準、紅色 max-mixture，用 Cholesky）：多出來的只是評估各成分，和解線性系統相比可以忽略。
- 球面資料集 [▶ 18:37](https://youtu.be/z60RbiY18I8?t=1117)：標準 Gauss-Newton 1 個離群值就有局部擾動，10 個已經看不出球形，100 個完全認不出；max-mixture 都沒有明顯影響。
- 【口頭】講者認為**明確支援多峰**是 max-mixture 最有趣的性質，大部分其他強健方法做不到。也用在實際的 SLAM 系統中。

一句話：**選高斯和裡最好的那個峰，在這一輪當作單一高斯；每輪重選。**

---

## 3. Dynamic Covariance Scaling

[▶ 20:37](https://youtu.be/z60RbiY18I8?t=1237)

- 不支援多峰，但有其他好性質；其實是第 4 節強健核的特例。
- 想法：給每個約束一個**額外權重**，覺得是離群值就降權：

$$
\min_x \sum_{ij} e_{ij}^{\mathsf T}\,\bigl( s_{ij}^2\,\Omega_{ij} \bigr)\,e_{ij}
$$

- $s_{ij} = 1$ → 標準最小平方；約束離目前預期很遠 → 給小的 $s_{ij}$，避免拉壞解。
- DCS 的設法 [▶ 22:23](https://youtu.be/z60RbiY18I8?t=1343)：$s_{ij}$ 取 **1** 和一個依 $\chi^2_{ij}$（不含縮放的誤差項）和參數 $\Phi$ 而定的值兩者的**最小值**。$\Phi$ 控制降權有多激進。
  - `⚠️ 待確認`：講者只說「取 1 和這個值（含 $\chi^2$、$\Phi$）的最小值」，沒有念出式子，投影片內容看不到；確切公式待補。

**圖示** [▶ 23:06](https://youtu.be/z60RbiY18I8?t=1386)：

- 黑：平方誤差；藍：縮放函數 $s$；紅：縮放後的誤差。
- 在 $s = 1$ 的範圍內，兩者一樣（二次）；超出後紅色越來越平。
- 縮放影響線性化 → **Jacobian 也會改變**。
- 動畫：誤差增加時，一開始一樣；超出二次區後被降權；非常遠的點，影響甚至比二次區邊界的點還小。
- 解讀：二次區是預期有雜訊的範圍；之外視為離群值，越遠影響越小。但接近正解的點不要降太多，仍要把 Jacobian 往對的方向拉。

一句話：**把離目前估計很遠的約束降權。**

---

## 4. 強健核（M 估計）

[▶ 26:21](https://youtu.be/z60RbiY18I8?t=1581)

- **M 估計**（M-estimation）：最佳化領域早就有的技術，用不同的加權函數降低對離群值的敏感度。
- 有離群值時，高斯的**尾巴機率太小** → 要**抬高尾巴**。抬多少，反映預期有多少離群值、離群值怎麼分布（完全隨機或有某種結構）。
- 做法：誤差不直接平方，而是經過函數 $\rho$：

$$
p(e) \propto \exp\bigl( -\rho(e) \bigr), \qquad
x^* = \arg\min_x \sum_i \rho\bigl( e_i(x) \bigr)
$$

- $e$ 是誤差的**值**（不是誤差向量）。
- 高斯：$\rho(e) = e^2$；DCS：二次函數乘上縮放 $s$。
- （Max-mixture 的「高斯和」不能寫成這種形式，但 max-mixture 本身可以。）

**常見的核** [▶ 29:42](https://youtu.be/z60RbiY18I8?t=1782)：

| 核 | $\rho(e)$ | 說明 |
|---|---|---|
| 平方（$L_2$） | $e^2$ | 高斯 |
| $L_1$ | $\lvert e \rvert$ | 絕對值 |
| **Huber** | $\lvert e \rvert < c$：二次；否則：線性 | 很常用。小於 $c$ 視為內點用二次、大於 $c$ 視為外點用線性 |
| Cauchy | — | 也很常用 |
| Corrupted Gaussian | — | max-mixture 的形狀，至少可以近似放進來 |
| Blake-Zisserman | — | `⚠️ 逐字稿缺字`：Whisper 寫 “scissor man”，推測為 Blake-Zisserman（MVG §A6.8 列有此函數） |

- 共同點：除了 $L_1$，靠近 0 時都像二次，遠處比高斯平。有些核到遠處甚至**完全不算**：Jacobian 為零，對最佳化沒有貢獻。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Hooper”、“cushy”，應為 **Huber**、**Cauchy**。

【課本補充】MVG §A6.8（書頁 616–620，PDF 頁 634–638）：

- 量測獨立、誤差分布 $f(\delta)$ → 代價 $-\sum_i \log f(\delta_i)$（通常減掉 $\log f(0)$ 讓準確量測代價為 0）。
- 設 $2\sigma^2 = 1$：

| 代價函數 | $C(\delta)$ | 性質 |
|---|---|---|
| 平方誤差 | $\delta^2$ | 不強健：遠處離群值影響過大 |
| Blake-Zisserman | $-\log\bigl( \exp(-\delta^2) + \varepsilon \bigr)$ | 內點 $\approx \delta^2$，外點漸近 $-\log\varepsilon$；非凸 |
| Corrupted Gaussian | $-\log\bigl( \alpha e^{-\delta^2} + (1-\alpha)e^{-\delta^2/w^2}/w \bigr)$ | 內點、外點兩個高斯的混合；非凸 |
| Cauchy | $b^2\log(1 + \delta^2/b^2)$ | 來自尾巴較重的 Cauchy 分布；非凸 |
| $L_1$ | $2b\lvert\delta\rvert$ | 求**中位數**；凸 |
| Huber | $\delta^2$（$\lvert\delta\rvert < b$），$2b\lvert\delta\rvert - b^2$（其他） | 一階導數連續；$b \approx$ 離群門檻；凸 |
| Pseudo-Huber | $2b^2\bigl( \sqrt{1 + (\delta/b)^2} - 1 \bigr)$ | Huber 的光滑版（各階可導）；凸 |

- $L_1$ 求中位數的理由：$\lvert x - a_i \rvert$ 對 $x$ 的導數是 $\pm 1$，兩邊個數相等時總導數為零 → 中位數；中位數不受遠處資料影響。
- 圖 A6.5、A6.6：離群值偏一邊時，平方誤差的最小值被拉走；**非凸**的代價函數在離群值附近有局部極小（30% 成塊離群值時甚至有兩個極小）；**Huber 凸**，只有一個極小，從任何起點都會收斂到它。

【十四講補充】§9.2.4（書頁 251–252，PDF 頁 274–275）：誤配會產生誤差很大的邊，梯度也大，最佳化會優先遷就它、抹平其他正確邊的影響。原因是二範數增長太快 → 換成增長較慢、但仍**光滑**（才能求導）的函數。Huber 核：

$$
H(e) = \begin{cases} \tfrac12 e^2, & \lvert e \rvert \le \delta \\ \delta\left( \lvert e \rvert - \tfrac12\delta \right), & \text{其他} \end{cases}
$$

超過閾值後二次變一次，等於**限制了梯度的最大值**。另有 Cauchy、Tukey 核，可看 g2o、Ceres 提供哪些。

---

## 5. 加權最小平方 = 強健估計

[▶ 32:01](https://youtu.be/z60RbiY18I8?t=1921)

兩個問題：

$$
\text{加權最小平方：}\ \min_x \sum_i w_i\, e_i(x)^2, \qquad
\text{強健估計：}\ \min_x \sum_i \rho\bigl( e_i(x) \bigr)
$$

- 資訊矩陣本身就是一種權重（把它從中間拿出來當 $w$ 是等價的）。

**比較梯度**（最佳解處梯度為零）[▶ 33:00](https://youtu.be/z60RbiY18I8?t=1980)：

$$
\text{加權：}\ \frac{\partial}{\partial x}\Bigl( \tfrac12 w_i e_i^2 \Bigr) = w_i\, e_i\, \frac{\partial e_i}{\partial x}, \qquad
\text{強健：}\ \frac{\partial}{\partial x}\rho(e_i) = \rho'(e_i)\, \frac{\partial e_i}{\partial x}
$$

（權重視為在目前估計固定；係數 $\tfrac12$ 是為了和 $\rho$ 的導數對齊，講者口述只說「形式相同」。）

- $\partial e_i/\partial x$ 部分一樣，只差前面的係數。令兩者相等：

$$
\boxed{\;w_i = \frac{1}{e_i}\,\rho'(e_i)\;}
$$

- 意思：**把每個約束的權重設成這個值，就能用已經會解的加權最小平方實現強健估計**（迭代重新加權）。
- Jacobian 會多一個和核有關的項，程式要改一點；其他部分不變。
- DCS 對應某個特定的核：**Geman-McClure**。DCS 可以看成強健估計的特例。
- `⚠️ 逐字稿缺字`：Whisper 寫 “gammon mcclure”、“gem and mclure”，應為 **Geman-McClure**。

**檢查** [▶ 35:13](https://youtu.be/z60RbiY18I8?t=2113)：以下不是逐字稿內容，是依上式推論的例子。

- 平方：$\rho = \tfrac12 e^2$ → $\rho' = e$ → $w = 1$（不加權）。
- Huber（用十四講的寫法）：$\lvert e \rvert \le \delta$ 時 $w = 1$；否則 $\rho' = \delta\,\mathrm{sign}(e)$ → $w = \delta / \lvert e \rvert$，越遠權重越小。

【課本補充】MVG §A6.8（書頁 621–622）的放法略有不同：LM 實作通常內建最小化 $\lVert\Delta\rVert^2$，所以把每個誤差向量換成 $w_i\delta_i$，讓 $\lVert w_i\delta_i \rVert^2 = C(\lVert\delta_i\rVert)$，也就是 $w_i = C(\lVert\delta_i\rVert)^{1/2} / \lVert\delta_i\rVert$（式 A6.18，「衰減因子」）。平方誤差時 $w = 1$；其他代價函數在內點區幾乎不衰減，區外依不同程度衰減。

---

## 6. 選哪個核？

[▶ 37:11](https://youtu.be/z60RbiY18I8?t=2231)

- 取決於**離群值分布**。大家常常試錯：把所有核試一遍，看哪個對手上的問題好。
- DCS 在 SLAM（至少雷射 SLAM）效果不錯 → 可以猜誤差分布和 DCS 有點關係，但只是估計，取決於感測器、環境等。
- 不滿意之處：要選對核，得相當了解離群值分布，但通常不知道。

**常見的變通法** [▶ 39:07](https://youtu.be/z60RbiY18I8?t=2347)（很多穩健的視覺 SLAM、BA 系統）：

1. 先用尾巴很強（遠離二次式很極端）的核，跑 $n_1$ 輪，強力剔除離群值。
2. 再用比較弱的核跑幾輪。
3. 檢查，把超出 $\pm c$ 的離群值丟掉。
4. 剩下的用高斯或 Huber 最佳化（最後幾輪有些點可能又跑出 $\pm c$，所以不要太激進）。

- 可行，但要在中途換核、寫一堆「這麼多輪這樣、那麼多輪那樣」的 if-else，不太漂亮。

---

## 7. 自適應核（Barron）

[▶ 40:43](https://youtu.be/z60RbiY18I8?t=2443)

- Jonathan **Barron**（講者說「去年」發表）提出一個**一族**的強健核 $\rho(e, \alpha, c)$：
  - $c$：原本就隱含在核裡（從二次換成別的形式的地方），這裡明確當參數。
  - **$\alpha$**：新參數，改變 $\alpha$ 就改變損失函數的形狀。
- `⚠️ 待確認`：講者沒有念出 $\rho(e, \alpha, c)$ 的式子；確切公式待補。

| $\alpha$ | 對應的核 |
|---|---|
| 2 | $L_2$（平方） |
| 1 | pseudo-Huber（和 Huber 很像） |
| 0 | Cauchy |
| −2 | Geman-McClure（和 DCS 很像） |
| $\to -\infty$ | 極平的分布，最強的降權 |

**權重** [▶ 43:08](https://youtu.be/z60RbiY18I8?t=2588)：$\alpha = 2$ 時權重恆為 1（標準最小平方）；$\alpha$ 越小，離群值降權越強；$-\infty$ 最強。

**模擬** [▶ 44:13](https://youtu.be/z60RbiY18I8?t=2653)：人工產生不同分布的殘差（藍色直方圖）。每種固定的核都在**某一種**離群值分布上最好（例如殘差依 Cauchy 分布產生，Cauchy 核最好）。黃色的 **adaptive**（依殘差分布調 $\alpha$）總是貼合 → 轉 $\alpha$ 這個旋鈕，就能讓損失函數符合目前的離群值分布。

- 【口頭】講者推薦 Barron 原始影片，說明得很好。

**Barron 方法的限制** [▶ 45:53](https://youtu.be/z60RbiY18I8?t=2753)：在最佳化中自動調 $\alpha$ 時，$\alpha < 0$ 會離開「機率分布」的範圍（正規化積分變無限大）→ 只能在 $[0, 2]$ 自動調整。影片：四種殘差分布，Barron 無法再往負值走，講者團隊的變體可以。

---

## 8. 截斷的自適應核與 EM

[▶ 46:56](https://youtu.be/z60RbiY18I8?t=2816)

**聯合最佳化**：未知數加上 $\alpha$：

$$
\min_{x,\,\alpha} \sum_i \rho\bigl( e_i(x), \alpha \bigr)
$$

（$c$ 視為常數。）

定義離群值分布和損失：

$$
p(e \mid \alpha) = \frac{1}{Z(\alpha)}\exp\bigl( -\rho(e, \alpha) \bigr), \qquad
Z(\alpha) = \int_{-\infty}^{\infty} \exp\bigl( -\rho(e, \alpha) \bigr)\, de
$$

$$
\text{自適應損失} = -\log p(e \mid \alpha) = \rho(e, \alpha) + \log Z(\alpha)
$$

- **問題** [▶ 48:35](https://youtu.be/z60RbiY18I8?t=2915)：$\alpha < 0$ 時尾巴趨近常數或下降很慢 → $Z(\alpha) \to \infty$ → 不是機率分布。
- **技巧**：假設現實中不會有極端誤差，**限制最大離群值**：積分範圍從 $(-\infty, \infty)$ 改成 $[-\tau, \tau]$，範圍外的約束直接**不考慮**（從問題中拿掉）→ 又是機率分布了。
- 圖 [▶ 50:07](https://youtu.be/z60RbiY18I8?t=3007)：$\tau = 10$，曲線在 ±10 掉到零。
- $\log Z(\alpha)$ 是**偏移量**：核越激進，偏移越大。所有誤差都小（沒有離群值）時，平方誤差的偏移最小 → 會被選中；離群值多時，才值得付偏移的代價換激進的核。

**聯合最佳化的問題** [▶ 51:44](https://youtu.be/z60RbiY18I8?t=3104)：簡單問題沒事，複雜問題會出狀況：

1. $\alpha$ 會**主導**估計：系統偏好轉 $\alpha$ 這個旋鈕，因為比改變真正的參數「便宜」→ 不穩定。
2. 對初始猜測敏感。
3. 使用者觀點：要對 $\alpha$ 也求導，**重算 Jacobian**，原本能跑的程式要改。

**EM 做法** [▶ 53:07](https://youtu.be/z60RbiY18I8?t=3187)：

- **E 步**：固定參數 $x$，估計目前最好的 $\alpha$。
- **M 步**：固定 $\alpha$，解標準（加權）最小平方。
- 來回迭代直到收斂。
- 講者團隊發現在 SLAM、ICP、BA 中比聯合最佳化**穩健得多**。
- 好處：最小平方內部**不用改 Jacobian**（$\alpha$ 的估計移到外面）；只要實作核函數本身，權重有閉式解，直接放進去。

**例子：ICP（KITTI 高速公路）** [▶ 54:27](https://youtu.be/z60RbiY18I8?t=3267)：

- 64 線光達、360° 視野；高速公路周圍結構很少（只有平坦路面，能限制上下，但車子可以沿路面「滑動」）。
- 其他車超車：ICP 把不同時刻看到的車疊在一起，等於假設那台車沒動 → 估計錯誤。
- Huber：車子看起來停下來、甚至**倒退**（對齊到超車的車），直到那台車離開。
- 自適應核：平常 $\alpha$ 正常；車子靠近時 $\alpha$ 降到最小值 $-10$，強烈剔除離群值，超車結束後回升 → 照常前進。
- （同 2-08、2-10 的例子。）

---

## 9. 總結與建議

[▶ 59:20](https://youtu.be/z60RbiY18I8?t=3560)

| 方法 | 重點 | 何時用 |
|---|---|---|
| **Max-Mixture** | 高斯和的近似（$\sum \to \max$）；支援**多峰** | 有多峰時（講者推薦） |
| **DCS** | 依誤差降權；是強健核的特例，和 Geman-McClure 差一個常數或比例 | 想固定用一種核時的好選擇；g2o 等工具箱設一個旗標就能用 |
| **強健核** | $\rho$ 決定離群值分布的形狀；$w = \rho'(e)/e$ | 知道離群值分布時 |
| **自適應核（EM）** | 同時估計核的形狀 | 不知道離群值分布時（大部分人） |

【口頭】講者的建議 [▶ 1:01:39](https://youtu.be/z60RbiY18I8?t=3699)：

- 知道離群值分布 → 直接選對應的核。不知道（講者認為大部分人不知道）→ 推薦 **EM 式的自適應估計**。
- 今天很多系統仍用 **Huber** 當標準選擇：比標準最小平方好，但剔除能力夠不夠？例如 BA 常常**不夠**。
- 要更激進的核：Geman-McClure 或 DCS，在 SLAM 中效果不錯。
- 如果今天要建 SLAM 系統，講者會用**EM 估計的自適應核**。

參考文獻（講者列四篇）：max-mixture、dynamic covariance scaling、一般強健損失函數（Barron）、EM 版本（講者團隊）。

---

## 10. 一頁速查表

### 10.1 Max-Mixture

$$
-\log p(e) \approx \min_k\Bigl[ \tfrac12 e_k^{\mathsf T}\Omega_k e_k - \log(w_k\eta_k) \Bigr]
$$

關鍵一步：$\log\sum$ 無法拆，$\log\max = \max\log$ 可以 → 每輪選最佳成分後又是二次式。

離群值剔除：窄高斯（閉合迴圈）＋ 很寬的高斯（其他）。

### 10.2 DCS

$\min \sum e^{\mathsf T}(s^2\Omega)e$，$s = \min(1, \cdot)$ 依 $\chi^2$ 和 $\Phi$；對應 Geman-McClure。

### 10.3 強健核 ↔ 加權最小平方

$$
w_i = \frac{\rho'(e_i)}{e_i}
$$

關鍵一步：$\nabla \tfrac12 w e^2 = w e \nabla e$，$\nabla \rho(e) = \rho'(e)\nabla e$，令係數相等。

| 核 | $\rho$ | 權重 $w$（$\rho$ 取 $\tfrac12 e^2$ 尺度時） |
|---|---|---|
| 平方 | $\tfrac12 e^2$ | 1 |
| Huber | $\tfrac12 e^2$ / $\delta(\lvert e \rvert - \tfrac12\delta)$ | 1 / $\delta/\lvert e \rvert$ |
| MVG 寫法 | 代價 $C(\delta)$ | $C^{1/2}/\lvert\delta\rvert$（乘在誤差向量上） |

凸（$L_1$、Huber、pseudo-Huber）→ 單一極小；非凸（Cauchy、Geman-McClure、Blake-Zisserman）→ 剔除更強，但有局部極小。

### 10.4 自適應核

| 項 | 內容 |
|---|---|
| $\alpha$ | 2：$L_2$；1：pseudo-Huber；0：Cauchy；−2：Geman-McClure；$-\infty$：最強 |
| 損失 | $\rho(e, \alpha) + \log Z(\alpha)$ |
| 問題 | $\alpha < 0$ 時 $Z \to \infty$ |
| 截斷 | 積分只到 $[-\tau, \tau]$，範圍外的約束丟掉 |
| EM | E：固定 $x$ 估 $\alpha$；M：固定 $\alpha$ 解加權最小平方 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 離群值、錯誤的資料關聯 | 2-22 RANSAC（另一種處理離群值的方法） |
| 強健核用在 BA | 2-24 以後的相機幾何、重投影誤差 |
| 視覺特徵的配對錯誤 | 2-17、2-20 視覺特徵 |

---

## 附：本集一句話總結

> **錯的資料關聯會讓平方誤差爆掉。Max-Mixture 用 $\max$ 近似高斯和，支援多峰；DCS 依誤差降權，是 Geman-McClure 核；任何強健核都能用權重 $w = \rho'(e)/e$ 放進加權最小平方；不知道離群值分布時，用 Barron 的一族核加截斷，再以 EM 交替估計 $\alpha$ 和參數。**

---

## ⚠️ 待確認清單

1. [▶ 22:23](https://youtu.be/z60RbiY18I8?t=1343) DCS 縮放係數 $s_{ij}$ 的確切公式：講者只說是 1 和一個含 $\chi^2_{ij}$、$\Phi$ 的值取最小，沒有念出式子；BRIEF 列的來源中也沒有。待補。
2. [▶ 40:49](https://youtu.be/z60RbiY18I8?t=2449) Barron 一族強健核 $\rho(e, \alpha, c)$ 的確切公式：講者沒有念出，BRIEF 列的來源中也沒有。待補。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Robust Least Squares for Graph-Based SLAM 錄影逐字稿（Whisper `medium.en`，1:03:11）、《視覺 SLAM 十四講》§9.2.4 與 MVG §A6.8 整理。*
