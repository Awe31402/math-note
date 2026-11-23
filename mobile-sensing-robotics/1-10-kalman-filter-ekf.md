---
course: Mobile Sensing and Robotics 1（Uni Bonn, Winter 2021/22）
episode: 1-10
lecture: Kalman Filter & EKF
date: 待補（2021/22 冬季學期）
video: https://youtu.be/E-6paM_Iwfc
notes: 《Probabilistic Robotics》早期草稿版 第 3 章 §3.1–3.3（書頁 33–54，PDF 頁 45–66）
---

# 第 1-10 集 · Kalman 濾波與擴展 Kalman 濾波（Kalman Filter & EKF） [▶ 影片](https://youtu.be/E-6paM_Iwfc)

← 上一集：[1-08-observation-models](1-08-observation-models.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[1-12-ekf-localization](1-12-ekf-localization.md) →

> **課程**：Mobile Sensing and Robotics 1，Uni Bonn，2021/22 冬季學期 — 第 1-10 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:13:36，Whisper `medium.en` 轉錄）＋《Probabilistic Robotics》早期草稿版第 3 章
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Kalman 濾波是什麼](#1-kalman-濾波是什麼)
- [2. 直覺例子：船與燈塔](#2-直覺例子船與燈塔)
- [3. 和貝氏濾波的關係](#3-和貝氏濾波的關係)
- [4. 工具箱：高斯的性質](#4-工具箱高斯的性質)
- [5. 線性高斯模型](#5-線性高斯模型)
  - [5.1 運動模型](#51-運動模型)
  - [5.2 觀測模型](#52-觀測模型)
  - [5.3 矩陣 A、B、C 和雜訊 R、Q](#53-矩陣-abc-和雜訊-rq)
- [6. 為什麼一直都是高斯](#6-為什麼一直都是高斯)
- [7. Kalman 濾波演算法](#7-kalman-濾波演算法)
- [8. 一維例子](#8-一維例子)
- [9. 非線性的問題](#9-非線性的問題)
- [10. 線性化：泰勒展開與 Jacobian](#10-線性化泰勒展開與-jacobian)
- [11. 線性化誤差取決於什麼](#11-線性化誤差取決於什麼)
- [12. 擴展 Kalman 濾波（EKF）演算法](#12-擴展-kalman-濾波ekf演算法)
- [13. 兩個極端：完美感測器與無用感測器](#13-兩個極端完美感測器與無用感測器)
- [14. 例子：EKF 定位](#14-例子ekf-定位)
- [15. 總結](#15-總結)
- [16. 一頁速查表](#16-一頁速查表)
- [17. 與後續集數的連結](#17-與後續集數的連結)

---

## 0. 這堂課要做什麼

貝氏濾波的第一個具體實作：**Kalman 濾波**（KF，全部高斯＋線性模型），以及處理非線性的**擴展 Kalman 濾波**（extended Kalman filter, EKF）。講者說會用直覺的方式講，**不做完整推導**。

| 主題 | 課本（草稿版） |
|---|---|
| 高斯濾波器、moments 表示 | §3.1（書頁 33–34） |
| 線性高斯系統、KF 演算法 | §3.2.1–3.2.3（書頁 34–39） |
| KF 的完整推導 | §3.2.4（書頁 39–48，本集跳過） |
| EKF：泰勒展開、演算法、實務 | §3.3（書頁 48–54） |
| 資訊濾波器 | §3.4（本集沒講） |

`⚠️ 逐字稿缺字`：整集 “base filter” → **Bayes filter**。

---

## 1. Kalman 濾波是什麼

[▶ 00:31](https://youtu.be/E-6paM_Iwfc?t=31)

- 一種遞迴貝氏濾波，特別之處：
  1. **所有**機率分布都是**高斯**；
  2. 所有模型都是**線性**的。
- 在「高斯＋線性」的情況下，它是**最佳**濾波器（統計上最佳，不可能做得更好）。
- 在這種情況下，它和**最小平方法**（least squares）給出**相同的結果**，只是算法不同：KF 是遞迴的，最小平方是批次的。
- 流程和貝氏濾波一樣：**預測**（用控制）→ **修正**（用觀測）→ 預測 → 修正……

---

## 2. 直覺例子：船與燈塔

[▶ 02:21](https://youtu.be/E-6paM_Iwfc?t=141)

1. 你在船上沿海岸航行，大概知道自己在哪（黑色圓圈）。
2. 你保持某個方向開一段時間 → 估計自己到了新位置（黑色叉叉）。這是**預測**。
3. 你看到岸邊有一座**燈塔** → 根據觀測，你應該在一條虛線上（綠色）。一座燈塔不夠決定完整位姿，但能給一部分資訊；多座燈塔就能告訴你更多。
4. 結合預測和觀測 → 紅色的新估計。這是**修正**。

**重點** [▶ 04:38](https://youtu.be/E-6paM_Iwfc?t=278)：Kalman 濾波算的是預測和觀測的**加權平均**，權重取決於你對兩者各有多確定。比較確定的那個，影響比較大。

---

## 3. 和貝氏濾波的關係

[▶ 05:14](https://youtu.be/E-6paM_Iwfc?t=314)

| 步驟 | 貝氏濾波 | 數學上是 |
|---|---|---|
| 預測 | $\overline{bel}(x_t) = \int p(x_t \mid u_t, x_{t-1})\, bel(x_{t-1})\, dx_{t-1}$ | 兩個分布的**卷積**（convolution） |
| 修正 | $bel(x_t) = \eta\, p(z_t \mid x_t)\, \overline{bel}(x_t)$ | 兩個分布**相乘** |

Kalman 濾波完全照這兩步走，只是假設一切都是高斯、模型都是線性。【口頭】在這種情況下，「不需要再找別的狀態估計方法」，頂多用等價的最小平方法 [▶ 07:03](https://youtu.be/E-6paM_Iwfc?t=423)。

---

## 4. 工具箱：高斯的性質

[▶ 08:07](https://youtu.be/E-6paM_Iwfc?t=487)

推導 KF 可以從機率的角度，也可以從線性代數的角度。最關鍵的兩個運算是**邊際化**和**條件化**。

設 $x_a$、$x_b$ 的聯合分布是高斯：

$$
p(x_a, x_b) = \mathcal{N}
$$

那麼：

| 運算 | 結果 |
|---|---|
| 邊際 $p(x_a) = \int p(x_a, x_b)\, dx_b$ | 高斯 |
| 邊際 $p(x_b)$ | 高斯 |
| 條件 $p(x_a \mid x_b)$ | 高斯 |
| 條件 $p(x_b \mid x_a)$ | 高斯 |

- 邊際的參數很好算；條件稍微複雜，通常會用到 **Schur 補**（Schur complement）[▶ 10:16](https://youtu.be/E-6paM_Iwfc?t=616)。講者沒有寫出式子。
- `⚠️ 逐字稿缺字`：Whisper 寫 “show complement”，應為 **Schur complement**。

**線性變換保持高斯** [▶ 10:35](https://youtu.be/E-6paM_Iwfc?t=635)：把高斯丟進線性函數 $y = Ax + b$，結果還是高斯。這很重要：目前的 belief 是高斯，和高斯模型（運動、觀測）結合後也必須是高斯，下一步才能繼續用。運動會增加不確定性，但只要是線性加高斯雜訊，就還是高斯。

---

## 5. 線性高斯模型

[▶ 11:47](https://youtu.be/E-6paM_Iwfc?t=707)

### 5.1 運動模型

$$
x_t = A_t\, x_{t-1} + B_t\, u_t + \varepsilon_t
$$

寫成機率分布 [▶ 17:35](https://youtu.be/E-6paM_Iwfc?t=1055)：平均值是 $A_t x_{t-1} + B_t u_t$，共變異數是 $R_t$：

$$
p(x_t \mid u_t, x_{t-1}) = \det(2\pi R_t)^{-\frac12} \exp\!\left( -\frac12 (x_t - A_t x_{t-1} - B_t u_t)^{\mathsf T} R_t^{-1} (x_t - A_t x_{t-1} - B_t u_t) \right)
$$

講者解讀指數：「離平均值多遠」，乘上共變異數的反矩陣（運動的不確定性）。

### 5.2 觀測模型

$$
z_t = C_t\, x_t + \delta_t
$$

- $C_t x_t$ 是**預測觀測**（predicted observation）：如果在狀態 $x_t$，應該看到什麼。

$$
p(z_t \mid x_t) = \det(2\pi Q_t)^{-\frac12} \exp\!\left( -\frac12 (z_t - C_t x_t)^{\mathsf T} Q_t^{-1} (z_t - C_t x_t) \right)
$$

指數裡是「實際觀測和預測觀測的差」，用觀測的不確定性 $Q_t$ 加權 [▶ 20:23](https://youtu.be/E-6paM_Iwfc?t=1223)。

### 5.3 矩陣 A、B、C 和雜訊 R、Q

[▶ 13:19](https://youtu.be/E-6paM_Iwfc?t=799)

| 記號 | 大小 | 意思 |
|---|---|---|
| $A_t$ | $n \times n$ | 不施加控制、沒有雜訊時，狀態怎麼從 $t-1$ 演變到 $t$（$n$ = 狀態維度） |
| $B_t$ | $n \times l$ | 控制 $u_t$ 怎麼改變狀態（$l$ = 控制維度）；是加上去的一項 |
| $C_t$ | $k \times n$ | 把狀態映射到觀測空間（$k$ = 觀測維度） |
| $R_t$ | $n \times n$ | **運動**雜訊 $\varepsilon_t$ 的共變異數（零平均高斯） |
| $Q_t$ | $k \times k$ | **觀測**雜訊 $\delta_t$ 的共變異數（零平均高斯） |

【口頭】$A_t$ 的例子：

- 最簡單：$A_t = I$（單位矩陣），不動就不變。
- 車子不踩油門還有慣性速度 → 位置一直在變，這可以寫進 $A_t$。
- 無人機遇到風（外在因素，不是你控制的）→ 風造成的漂移也可以寫進 $A_t$。

【口頭】**$R$ 和 $Q$ 的命名要小心** [▶ 17:04](https://youtu.be/E-6paM_Iwfc?t=1024)：本課照《Probabilistic Robotics》：$R$ = 運動雜訊，$Q$ = 觀測雜訊。但這個社群以外的很多文獻**剛好相反**。對照其他資料時要確認。

（講者在 [▶ 17:12](https://youtu.be/E-6paM_Iwfc?t=1032) 口誤說成「$Q_t$ 是控制的雜訊」，依前後文和課本，$Q_t$ 是**觀測**雜訊。）

【課本補充】課本 §3.2.1（書頁 34–36）把 KF 需要的條件整理成三條（再加上貝氏濾波的馬可夫假設）：(1) 狀態轉移是線性加高斯雜訊；(2) 觀測是線性加高斯雜訊；(3) 初始 belief $bel(x_0)$ 是高斯。這三條就保證每一刻的後驗都是高斯。

---

## 6. 為什麼一直都是高斯

[▶ 22:15](https://youtu.be/E-6paM_Iwfc?t=1335)

要證明：如果 $bel(x_{t-1})$ 是高斯，那 $bel(x_t)$ 也是高斯。這像**數學歸納法**：初始 belief 是高斯；每一步都保持高斯 → 永遠是高斯。

**修正步** [▶ 22:27](https://youtu.be/E-6paM_Iwfc?t=1347)：$bel(x_t) = \eta\, p(z_t \mid x_t)\, \overline{bel}(x_t)$。

- $p(z_t \mid x_t)$ 是高斯（5.2 節）。
- **兩個高斯相乘還是高斯**。
- 所以只要 $\overline{bel}(x_t)$ 是高斯，$bel(x_t)$ 就是高斯。

**預測步** [▶ 23:48](https://youtu.be/E-6paM_Iwfc?t=1428)：$\overline{bel}(x_t) = \int p(x_t \mid u_t, x_{t-1})\, bel(x_{t-1})\, dx_{t-1}$。

- 兩個高斯，但中間有積分。這是**卷積**，**兩個高斯的卷積還是高斯**。

**證明概要** [▶ 26:10](https://youtu.be/E-6paM_Iwfc?t=1570)：

1. 代入兩個高斯（常數都丟進 $\eta$）：

$$
\overline{bel}(x_t) = \eta \int \exp\!\left( -\tfrac12 (x_t - A_t x_{t-1} - B_t u_t)^{\mathsf T} R_t^{-1} (\cdots) \right) \exp\!\left( -\tfrac12 (x_{t-1} - \mu_{t-1})^{\mathsf T} \Sigma_{t-1}^{-1} (\cdots) \right) dx_{t-1}
$$

2. 兩個指數相乘 = 指數裡相加，寫成 $\exp(-L_t)$。
3. 把 $L_t$ 拆成兩部分：$L_t = L_t(x_{t-1}, x_t) + L_t(x_t)$，第二部分**只含** $x_t$。
4. 只含 $x_t$ 的部分可以提到積分外面：

$$
\overline{bel}(x_t) = \eta\, \exp\!\bigl(-L_t(x_t)\bigr) \int \exp\!\bigl(-L_t(x_{t-1}, x_t)\bigr)\, dx_{t-1}
$$

5. 積分裡是一個對 $x_{t-1}$ 的高斯，積分 = 對 $x_{t-1}$ **邊際化**，結果還是高斯（講者說的；課本 §3.2.4 指出這個積分其實是常數，和 $x_t$ 無關）。
6. 高斯 × 高斯 = 高斯。

詳細步驟見課本 §3.2.4（講者說 3.2 節）。

**結論** [▶ 29:13](https://youtu.be/E-6paM_Iwfc?t=1753)：只要活在「線性＋高斯」的世界，從頭到尾都不會離開高斯。這很重要：一旦離開，下一步的輸入就不是高斯，整個方法就壞了。

**所以只要存兩樣東西** [▶ 31:11](https://youtu.be/E-6paM_Iwfc?t=1871)：高斯由**平均值** $\mu$ 和**共變異數** $\Sigma$ 完全決定。演算法就是把 $(\mu_{t-1}, \Sigma_{t-1})$ 變成 $(\mu_t, \Sigma_t)$。

**推導 KF 需要的工具** [▶ 32:43](https://youtu.be/E-6paM_Iwfc?t=1963)：兩個高斯相乘還是高斯；線性變換保持高斯；高斯的邊際和條件還是高斯，以及它們的平均值和共變異數怎麼算；兩個高斯的卷積；**矩陣反轉引理**（matrix inversion lemma）。講者沒有做推導。

---

## 7. Kalman 濾波演算法

[▶ 33:52](https://youtu.be/E-6paM_Iwfc?t=2032)

```
Algorithm Kalman_filter(μ_{t-1}, Σ_{t-1}, u_t, z_t):
  // 預測
  μ̄_t = A_t μ_{t-1} + B_t u_t
  Σ̄_t = A_t Σ_{t-1} A_tᵀ + R_t
  // 修正
  K_t = Σ̄_t C_tᵀ (C_t Σ̄_t C_tᵀ + Q_t)⁻¹
  μ_t = μ̄_t + K_t (z_t - C_t μ̄_t)
  Σ_t = (I - K_t C_t) Σ̄_t
  return μ_t, Σ_t
```

（形式依課本表 3.1，書頁 36；講者逐行說明。）

**預測步**（兩行）[▶ 34:41](https://youtu.be/E-6paM_Iwfc?t=2081)：

- 平均值：照線性模型推一步。
- 共變異數：$A_t \Sigma_{t-1} A_t^{\mathsf T}$ 是**一階誤差傳播**（高斯經過線性函數，不確定性怎麼變），再加上運動本身的雜訊 $R_t$。

**修正步**（三行）[▶ 35:53](https://youtu.be/E-6paM_Iwfc?t=2153)：

- $K_t$：**Kalman 增益**（Kalman gain）。決定「比較相信觀測，還是比較相信預測」。它是一個比值，牽涉觀測的不確定性 $Q_t$ 和映射矩陣 $C_t$。
- $z_t - C_t \bar\mu_t$：實際觀測減掉預測觀測，叫**新息**（innovation）。這個詞是筆記補的；講者只說「實際觀測和預測觀測的差」，就是觀測模型指數裡那一項。
- $K_t$ 把這個差**從觀測空間映射回狀態空間**，告訴我們預測的平均值要修多少。
- 共變異數也要更新：多了一個觀測 = 多了資訊，不確定性通常**減少**。

輸出 $(\mu_t, \Sigma_t)$，下一步和 $u_{t+1}, z_{t+1}$ 一起再丟回去。

【課本補充】課本 §3.2.2（書頁 37）：KF 計算很有效率。主要成本是 $k \times k$ 矩陣的反矩陣（$k$ = 觀測維度），約 $O(k^{2.8})$；加上共變異數更新約 $O(n^2)$（$n$ = 狀態維度）。

---

## 8. 一維例子

[▶ 39:03](https://youtu.be/E-6paM_Iwfc?t=2343)

- 紅色高斯 = **預測**；綠色高斯 = **量測**。
- 結合結果 = 藍色。藍色**比較靠近綠色**，因為綠色的變異數比較小（比較相信量測）。
- 藍色的變異數**比紅色和綠色都小**：結合兩個資訊，變得更確定。
- 下一步：從藍色出發，往正 $x$ 方向預測 → 移動了，而且變寬。新的量測這次比較不準 → 結合後的黃色落在兩者中間。

**一般規律** [▶ 40:44](https://youtu.be/E-6paM_Iwfc?t=2444)：

- **預測步增加**不確定性（原本的不確定性＋控制的誤差），除非運動完美。
- **量測步減少**不確定性，除非量測完全沒資訊。
- 結果是兩個估計的**加權平均**，權重由各自的不確定性決定。

以下**不是逐字稿內容**，是依課本表 3.1 令所有量為純量、$C_t = 1$ 推出的一維公式，讓上面的圖可以算：

預測後是 $\mathcal{N}(\bar\mu, \bar\sigma^2)$，量測是 $z$、雜訊變異數 $\sigma_z^2$：

$$
K = \frac{\bar\sigma^2}{\bar\sigma^2 + \sigma_z^2}, \qquad
\mu = \bar\mu + K(z - \bar\mu) = \frac{\sigma_z^2\, \bar\mu + \bar\sigma^2\, z}{\bar\sigma^2 + \sigma_z^2}
$$

$$
\sigma^2 = (1 - K)\,\bar\sigma^2 = \frac{\bar\sigma^2\, \sigma_z^2}{\bar\sigma^2 + \sigma_z^2}
$$

- $\mu$ 是 $\bar\mu$ 和 $z$ 的加權平均，**權重和對方的變異數成正比**：量測越準（$\sigma_z^2$ 越小），$z$ 的權重越大。
- $\frac{1}{\sigma^2} = \frac{1}{\bar\sigma^2} + \frac{1}{\sigma_z^2}$，所以 $\sigma^2$ 比 $\bar\sigma^2$ 和 $\sigma_z^2$ **都小**。

（驗算第二式：$\bar\mu + \frac{\bar\sigma^2}{\bar\sigma^2 + \sigma_z^2}(z - \bar\mu) = \frac{(\bar\sigma^2 + \sigma_z^2)\bar\mu + \bar\sigma^2 z - \bar\sigma^2 \bar\mu}{\bar\sigma^2 + \sigma_z^2} = \frac{\sigma_z^2 \bar\mu + \bar\sigma^2 z}{\bar\sigma^2 + \sigma_z^2}$。）

---

## 9. 非線性的問題

[▶ 43:30](https://youtu.be/E-6paM_Iwfc?t=2610)

KF 的兩個假設（全部高斯、全部線性）都很強：

- 高斯：很多感測器的雜訊接近高斯，**大致可以接受**。
- 線性：**幾乎永遠不成立**。描述車子在 2D（更別說 3D）的運動會有角度，就有 $\sin$、$\cos$，不是線性的。

所以模型改成一般的函數：

$$
x_t = g(u_t, x_{t-1}) + \varepsilon_t, \qquad z_t = h(x_t) + \delta_t
$$

**為什麼是問題** [▶ 45:47](https://youtu.be/E-6paM_Iwfc?t=2747)（圖解）：

- 下方是輸入的高斯，右邊是函數，左邊是輸出。每一點往上碰到函數、再轉到另一軸，就是它被映射到的位置。
- 線性函數：輸出還是高斯。
- 非線性函數：輸出（黑色曲線）**明顯不是高斯**。
- 硬用一個高斯去近似黑色曲線（藍色），差很遠。
- 一旦離開高斯世界，KF 就不能用了。

---

## 10. 線性化：泰勒展開與 Jacobian

[▶ 49:03](https://youtu.be/E-6paM_Iwfc?t=2943)

最簡單的辦法：承認函數是非線性的，但在某一點附近**局部線性化**：在**線性化點**算一階導數，畫一條切線，把函數當成這條直線。這就是**一階泰勒展開**（Taylor expansion）。

**預測步** [▶ 49:45](https://youtu.be/E-6paM_Iwfc?t=2985)：線性化點選上一刻的平均值 $\mu_{t-1}$：

$$
g(u_t, x_{t-1}) \approx g(u_t, \mu_{t-1}) + \underbrace{\frac{\partial g(u_t, \mu_{t-1})}{\partial x_{t-1}}}_{=:\, G_t} (x_{t-1} - \mu_{t-1})
$$

**修正步** [▶ 50:59](https://youtu.be/E-6paM_Iwfc?t=3059)：線性化點選**預測後**的平均值 $\bar\mu_t$（修正前最好的估計）：

$$
h(x_t) \approx h(\bar\mu_t) + \underbrace{\frac{\partial h(\bar\mu_t)}{\partial x_t}}_{=:\, H_t} (x_t - \bar\mu_t)
$$

結構：常數（函數在線性化點的值）＋斜率 ×（離線性化點多遠）。這是線性函數。

### Jacobian

[▶ 52:02](https://youtu.be/E-6paM_Iwfc?t=3122)

多維時，一階導數不是一個數，而是一個矩陣，叫 **Jacobian**（一般不是方陣）。函數 $g$ 有 $m$ 個輸出分量、變數 $x$ 有 $n$ 維：

$$
G = \frac{\partial g}{\partial x} =
\begin{bmatrix}
\dfrac{\partial g_1}{\partial x_1} & \cdots & \dfrac{\partial g_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial g_m}{\partial x_1} & \cdots & \dfrac{\partial g_m}{\partial x_n}
\end{bmatrix}
$$

（逐字稿裡講者說「第 1 個函數分量對第 1 個變數、對第 2 個變數……」，排列方式依標準寫法整理。）

- 2D 時，線性化就是在那一點貼一個**切平面**，在平面上移動。
- 離線性化點**近**時近似很好，**遠**時誤差變大 [▶ 53:31](https://youtu.be/E-6paM_Iwfc?t=3211)。
- Jacobian 就是一般梯度／一階導數在多維時的推廣。

### 線性化後的效果

[▶ 54:15](https://youtu.be/E-6paM_Iwfc?t=3255)：

- 在平均值處用紅色切線近似藍色的非線性函數。
- 高斯經過紅色切線 → 輸出是**高斯**（紅色）。
- 但它沒辦法反映藍色函數的非線性：真正的輸出是黑色曲線；把黑色曲線用平均值和變異數近似是藍色高斯；紅色和藍色之間還有差距。
- 講者：這離完美很遠，不是「最好的」近似，但是**最簡單、最標準**的做法。有更好的近似方法。

---

## 11. 線性化誤差取決於什麼

[▶ 56:02](https://youtu.be/E-6paM_Iwfc?t=3362)

兩個因素：

1. **函數有多非線性**：紅色切線和藍色函數差多遠。差很少 → 誤差小。
2. **輸入的不確定性有多大**：
   - 不確定性大 → 很多機率質量落在離線性化點很遠的地方 → 那裡切線誤差大 → 輸出誤差大。
   - 不確定性小（高斯很尖）→ 誤差小。連黑色曲線都比較像高斯，紅色和藍色也比較接近。

**結論** [▶ 58:13](https://youtu.be/E-6paM_Iwfc?t=3493)：**不確定性越小、模型越接近線性，EKF 表現越好。**

【課本補充】課本 §3.3.4（書頁 54）因此建議：用 EKF 時，**讓狀態估計的不確定性保持小**很重要。

---

## 12. 擴展 Kalman 濾波（EKF）演算法

[▶ 59:46](https://youtu.be/E-6paM_Iwfc?t=3586)

線性化後，運動模型的高斯平均值從 $A_t x_{t-1} + B_t u_t$ 換成 $g(u_t, \mu_{t-1}) + G_t(x_{t-1} - \mu_{t-1})$；觀測模型的 $C_t x_t$ 換成 $h(\bar\mu_t) + H_t(x_t - \bar\mu_t)$。代進 KF，改動很少：

```
Algorithm Extended_Kalman_filter(μ_{t-1}, Σ_{t-1}, u_t, z_t):
  μ̄_t = g(u_t, μ_{t-1})
  Σ̄_t = G_t Σ_{t-1} G_tᵀ + R_t
  K_t = Σ̄_t H_tᵀ (H_t Σ̄_t H_tᵀ + Q_t)⁻¹
  μ_t = μ̄_t + K_t (z_t - h(μ̄_t))
  Σ_t = (I - K_t H_t) Σ̄_t
  return μ_t, Σ_t
```

（形式依課本表 3.3，書頁 51。）

| | KF | EKF |
|---|---|---|
| 預測平均值 | $A_t \mu_{t-1} + B_t u_t$ | $g(u_t, \mu_{t-1})$（**直接用非線性函數**） |
| 預測觀測 | $C_t \bar\mu_t$ | $h(\bar\mu_t)$（**直接用非線性函數**） |
| 共變異數、增益裡的矩陣 | $A_t$、$C_t$ | Jacobian $G_t$、$H_t$ |

- 為什麼平均值可以直接用非線性函數 [▶ 1:00:38](https://youtu.be/E-6paM_Iwfc?t=3638)：只是把**一個點**送進函數，不需要線性化。
- 「extended」= 把 KF **擴展**到非線性模型。

【課本補充】EKF 的 belief 只是**近似**，不像 KF 是精確的（課本 §3.3，書頁 49）。

---

## 13. 兩個極端：完美感測器與無用感測器

[▶ 1:01:44](https://youtu.be/E-6paM_Iwfc?t=3704)

### 完美感測器：$Q_t = 0$

[▶ 1:02:19](https://youtu.be/E-6paM_Iwfc?t=3739)

1. $Q_t = 0$ 時：

$$
K_t = \bar\Sigma_t H_t^{\mathsf T} (H_t \bar\Sigma_t H_t^{\mathsf T})^{-1}
$$

2. 乘積的反矩陣 = 反矩陣反序相乘（假設 $H_t$ 是可逆方陣）：

$$
(H_t \bar\Sigma_t H_t^{\mathsf T})^{-1} = (H_t^{\mathsf T})^{-1}\, \bar\Sigma_t^{-1}\, H_t^{-1}
$$

3. 代入，$H_t^{\mathsf T}(H_t^{\mathsf T})^{-1} = I$、$\bar\Sigma_t \bar\Sigma_t^{-1} = I$：

$$
K_t = \bar\Sigma_t H_t^{\mathsf T} (H_t^{\mathsf T})^{-1} \bar\Sigma_t^{-1} H_t^{-1} = H_t^{-1}
$$

4. 代入平均值更新 [▶ 1:03:49](https://youtu.be/E-6paM_Iwfc?t=3829)（講者用線性化的 $h(\bar\mu_t) \approx H_t \bar\mu_t$ 來看）：

$$
\mu_t = \bar\mu_t + H_t^{-1}(z_t - H_t \bar\mu_t) = \bar\mu_t + H_t^{-1} z_t - \bar\mu_t = H_t^{-1} z_t
$$

意思：把觀測**直接映射回狀態空間**，預測完全被抵消。完美、沒有雜訊的感測器，當然只相信它。

（以下**不是逐字稿內容**，是依矩陣反轉的條件推論的：第 2 步要求 $H_t$ 是可逆方陣，也就是觀測維度等於狀態維度、而且觀測能完全決定狀態。觀測維度比狀態少時，$H_t^{-1}$ 不存在，這個推導不成立；這時完美感測器只會完全決定「看得到的那部分」狀態。）

### 無用感測器：$Q_t \to \infty$

[▶ 1:05:36](https://youtu.be/E-6paM_Iwfc?t=3936)

1. 對角線上是無限大的共變異數 = 完全沒資訊。
2. $H_t \bar\Sigma_t H_t^{\mathsf T} + Q_t$：有限 + 無限 = 無限。
3. 反矩陣 → 0（除以無限大）。
4. 所以 $K_t \to 0$（零矩陣）。
5. $\mu_t = \bar\mu_t + 0 = \bar\mu_t$：**只相信預測**。

| 感測器 | $Q_t$ | $K_t$ | $\mu_t$ |
|---|---|---|---|
| 完美 | $0$ | $H_t^{-1}$（$H_t$ 可逆時） | $H_t^{-1} z_t$（只信觀測） |
| 無用 | $\infty$ | $0$ | $\bar\mu_t$（只信預測） |

---

## 14. 例子：EKF 定位

[▶ 1:07:41](https://youtu.be/E-6paM_Iwfc?t=4061)

詳細在 1-12 集，這裡只是預告。

- 灰線是實際路徑；環境中有 6 個地標。
- 初始 belief → 依運動預測到某處（但實際走的是另一條）→ 觀測到地標 → 修正。觀測有雜訊，修正後的位置可能還有偏差。
- 繼續走、繼續觀測，每次觀測都把估計拉近真實位置。
- 每一步都能看到預測的不確定性和觀測的不確定性如何結合：本質上是**預測和觀測的加權和**。
- 影片 [▶ 1:09:43](https://youtu.be/E-6paM_Iwfc?t=4183)：只靠運動指令會漂移（粉紅色軌跡）；EKF 的估計（藍線）能很好地追蹤實際的圓形路徑。

---

## 15. 總結

[▶ 1:10:35](https://youtu.be/E-6paM_Iwfc?t=4235)

- **KF** = 高斯＋線性情況下的貝氏濾波。
- **EKF** = 處理非線性的一種方法：用泰勒展開做**局部線性化**。
- 這不是唯一的方法，只是最直接、最常見的。更好的近似例如**無跡 Kalman 濾波**（unscented Kalman filter, UKF），不只用一個線性化點。
- EKF 是標準工具，效果好，**除非**：
  1. 不確定性**非常大**：例如初始 belief 接近均勻分布或是多峰 → 線性化誤差很大。
  2. 非線性模型**不能**用線性函數好好近似。
- 只要模型不要離線性太遠、不確定性能被限制住（例如用高品質感測器），KF/EKF 就是遞迴狀態估計的標準工具。

**延伸閱讀** [▶ 1:12:19](https://youtu.be/E-6paM_Iwfc?t=4339)：

- 《Probabilistic Robotics》第 3 章、第 7 章。
- 想親手推導 KF：講者推薦一篇用操作高斯分布推導 KF 的文章，五、六頁，網路上找得到。作者 Whisper 寫作 “Schoen and Lindstrom”（`⚠️ 待確認`：作者姓名拼法與篇名，逐字稿無法確定）。

【課本補充】課本 §3.3.4（書頁 53–54）另外提到：
- EKF 每次更新的時間約 $O(k^{2.8} + n^2)$；粒子濾波等方法可能要指數時間。
- 高斯是單峰的，可以想成「一個猜測＋一個不確定性橢圓」。要同時追蹤多個假設時，常見的延伸是用**高斯混合**表示後驗，叫**多假設（擴展）Kalman 濾波**（MHEKF）。
- 除了泰勒展開，另外兩種線性化常常更好：**無跡 Kalman 濾波**（在選定的幾個點探測函數，依結果算線性近似）和 **moments matching**（讓線性化保留後驗真正的平均值和共變異數；EKF 做不到這點）。

---

## 16. 一頁速查表

### 16.1 KF

| 步驟 | 公式 | 關鍵 |
|---|---|---|
| 模型 | $x_t = A_t x_{t-1} + B_t u_t + \varepsilon_t$，$\varepsilon_t \sim \mathcal N(0, R_t)$ | 線性＋高斯 |
| | $z_t = C_t x_t + \delta_t$，$\delta_t \sim \mathcal N(0, Q_t)$ | |
| 預測 | $\bar\mu_t = A_t\mu_{t-1} + B_t u_t$ | |
| | $\bar\Sigma_t = A_t \Sigma_{t-1} A_t^{\mathsf T} + R_t$ | 線性誤差傳播＋運動雜訊 |
| 增益 | $K_t = \bar\Sigma_t C_t^{\mathsf T}(C_t \bar\Sigma_t C_t^{\mathsf T} + Q_t)^{-1}$ | 信預測還是信觀測 |
| 修正 | $\mu_t = \bar\mu_t + K_t(z_t - C_t\bar\mu_t)$ | 新息經 $K_t$ 映射回狀態 |
| | $\Sigma_t = (I - K_t C_t)\bar\Sigma_t$ | 不確定性減少 |

### 16.2 EKF

| 改動 | 公式 |
|---|---|
| 模型 | $x_t = g(u_t, x_{t-1}) + \varepsilon_t$，$z_t = h(x_t) + \delta_t$ |
| Jacobian | $G_t = \left.\frac{\partial g}{\partial x_{t-1}}\right|_{u_t, \mu_{t-1}}$，$H_t = \left.\frac{\partial h}{\partial x_t}\right|_{\bar\mu_t}$ |
| 平均值 | $\bar\mu_t = g(u_t, \mu_{t-1})$，修正用 $z_t - h(\bar\mu_t)$ |
| 其餘 | 把 $A_t \to G_t$、$C_t \to H_t$ |

### 16.3 一維（推論）

$$
K = \frac{\bar\sigma^2}{\bar\sigma^2 + \sigma_z^2}, \quad
\mu = \frac{\sigma_z^2\bar\mu + \bar\sigma^2 z}{\bar\sigma^2 + \sigma_z^2}, \quad
\frac{1}{\sigma^2} = \frac{1}{\bar\sigma^2} + \frac{1}{\sigma_z^2}
$$

### 16.4 高斯工具箱

| 性質 | 結果 |
|---|---|
| 邊際、條件 | 還是高斯（條件要用 Schur 補） |
| 線性變換 | 還是高斯 |
| 相乘 | 還是高斯（修正步） |
| 卷積 | 還是高斯（預測步） |
| 非線性變換 | **不是**高斯 → 要線性化 |

### 16.5 EKF 什麼時候會失敗

| 情況 | 原因 |
|---|---|
| 不確定性很大（接近均勻、多峰） | 機率質量遠離線性化點，切線誤差大 |
| 函數高度非線性 | 切線本身就是爛近似 |
| 需要多個假設 | 高斯是單峰的 |

---

## 17. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| EKF 演算法、Jacobian $G_t$、$H_t$ | 1-12 EKF 定位（具體算出里程計模型和地標觀測模型的 Jacobian） |
| EKF 不能處理多峰、大不確定性 | 1-14 粒子濾波（能表示任意分布） |
| KF 和最小平方等價 | MSR2：2-05 最小平方、2-11 Graph SLAM |
| 線性化、Jacobian | MSR2：2-10 非線性最小平方（Gauss-Newton） |
| $R$/$Q$ 命名在不同文獻相反 | 讀 MPC（1-16、1-17）等控制文獻時注意 |

---

## 附：本集一句話總結

> **Kalman 濾波：在「全高斯＋全線性」下，貝氏濾波的預測和修正都保持高斯，只要更新平均值和共變異數，結果是預測和觀測依不確定性的加權平均。EKF：非線性時，在平均值處用 Jacobian 做一階泰勒展開，其餘照抄 KF；不確定性越小、模型越接近線性，效果越好。**

---

## ⚠️ 待確認清單

1. [▶ 1:12:36](https://youtu.be/E-6paM_Iwfc?t=4356) 講者推薦的 KF 推導文章，作者 Whisper 寫作 “Schoen and Lindstrom”，正確姓名拼法與篇名待確認。

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 1」Kalman Filter & EKF 錄影逐字稿（Whisper `medium.en`，1:13:36）與《Probabilistic Robotics》早期草稿版第 3 章整理。*
