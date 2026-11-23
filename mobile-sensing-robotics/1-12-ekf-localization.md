---
course: Mobile Sensing and Robotics 1（Uni Bonn, Winter 2021/22）
episode: 1-12
lecture: EKF Localization
date: 待補（2021/22 冬季學期）
video: https://youtu.be/PiCC-SxWlH8
notes: 《Probabilistic Robotics》早期草稿版 §7.5（書頁 166–174，PDF 頁 178–186）
---

# 第 1-12 集 · EKF 定位（EKF Localization） [▶ 影片](https://youtu.be/PiCC-SxWlH8)

← 上一集：[1-10-kalman-filter-ekf](1-10-kalman-filter-ekf.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[1-14-particle-filter-mcl](1-14-particle-filter-mcl.md) →

> **課程**：Mobile Sensing and Robotics 1，Uni Bonn，2021/22 冬季學期 — 第 1-12 集
> **講者**：Nived Chebrolu（依影片標題）
> **來源**：YouTube 錄影逐字稿（36:21，Whisper `medium.en` 轉錄）＋《Probabilistic Robotics》早期草稿版 §7.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 動機：北海上的船](#1-動機北海上的船)
- [2. 複習：KF 的假設與 EKF](#2-複習kf-的假設與-ekf)
- [3. 問題設定](#3-問題設定)
- [4. 運動模型：里程計](#4-運動模型里程計)
  - [4.1 對狀態的 Jacobian $G_t$](#41-對狀態的-jacobian-g_t)
  - [4.2 對控制的 Jacobian $V_t$](#42-對控制的-jacobian-v_t)
- [5. 觀測模型：距離—方位](#5-觀測模型距離方位)
  - [5.1 觀測的 Jacobian $H_t$](#51-觀測的-jacobian-h_t)
- [6. 完整的 EKF 定位演算法](#6-完整的-ekf-定位演算法)
- [7. 圖解一次迭代](#7-圖解一次迭代)
  - [7.1 預測](#71-預測)
  - [7.2 期望觀測與新息](#72-期望觀測與新息)
  - [7.3 修正](#73-修正)
- [8. 模擬例子](#8-模擬例子)
- [9. 總結](#9-總結)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

把 1-10 的 EKF 用在具體問題：**2D 機器人定位**。狀態是 $(x, y, \theta)$，地圖是一串已知位置的地標。要做的就是把 1-07 的**里程計運動模型**和 1-08 的**距離—方位觀測模型**代進 EKF，並**算出所有 Jacobian**。

| 主題 | 課本（草稿版） |
|---|---|
| EKF 定位的概念、一維例子 | §7.5、§7.5.1（書頁 166–168） |
| EKF 定位演算法 | §7.5.2 表 7.2（書頁 168–170） |
| 推導 | §7.5.3（書頁 170–174） |

課本版本和講者版本的差別：

| | 講者 | 課本草稿版表 7.2 |
|---|---|---|
| 運動模型 | **里程計模型**（轉—走—轉） | 速度模型 $(v, \omega)$ |
| 運動雜訊 | 在控制空間給，用 $V_t$ 映射到狀態空間 | 直接給狀態空間的 $R_t$ |
| 觀測 | 距離＋方位 | 距離＋方位＋簽名 |

---

## 1. 動機：北海上的船

[▶ 00:29](https://youtu.be/PiCC-SxWlH8?t=29)

- 德國北海岸，你在一艘船上（紅點）。知道目前位置、速度和海上的風。
- **航位推算**：一小時後會到黑點。這是**運動**給的估計（也可以用機器人上的編碼器）。
- 岸上有**燈塔**（地標），手上有燈塔地圖 → 根據看到的燈塔推出另一個位置估計（藍色）。這是**量測**給的估計。
- 兩個估計各有不確定性。Kalman 濾波用這些不確定性把兩者**融合**成第三個估計。
- 圖上 KF 的估計大約在兩者中間 → 可以推斷兩個估計的確定程度差不多。不確定性不同時，結果會偏向比較確定的那一個 [▶ 02:29](https://youtu.be/PiCC-SxWlH8?t=149)。

---

## 2. 複習：KF 的假設與 EKF

[▶ 03:09](https://youtu.be/PiCC-SxWlH8?t=189)

**KF 的假設**：

1. 要追蹤的狀態是**高斯**分布（1D 或多維）。
2. 運動模型和觀測模型都是**線性**的，雜訊是高斯：

$$
x_t = A_t x_{t-1} + B_t u_t + \varepsilon_t, \qquad z_t = C_t x_t + \delta_t
$$

在這些條件下，KF 的解是**最佳**的。

**實際上不是線性** [▶ 04:51](https://youtu.be/PiCC-SxWlH8?t=291)：Ackermann、差速驅動的公式（1-06）都是非線性的；偵測環境特徵、相機看特徵的觀測模型也是非線性的。換成任意非線性函數 $g$、$h$ 後，KF 的解就不再是最佳的。

**EKF 的做法**：在線性化點做一階泰勒展開。

- 運動：在 $\mu_{t-1}$（上一步最好的估計）線性化，Jacobian $G_t = \partial g / \partial x$。對行動機器人，狀態變數是位姿 $(x, y, \theta)$。
- 觀測：在 $\bar\mu_t$（運動後的預測狀態）線性化，Jacobian $H_t$。

線性化之後就能回到 KF 的框架（1-10 第 12 節的演算法）。

**Kalman 增益的直覺** [▶ 09:25](https://youtu.be/PiCC-SxWlH8?t=565)：$K_t$ 和運動後的不確定性 $\bar\Sigma_t$ **成正比**，和觀測雜訊 $Q_t$（經 $H_t$）**成反比**。所以它在運動雜訊和量測雜訊之間做加權。$K_t$ 乘上**新息**（innovation）$z_t - h(\bar\mu_t)$：實際量測減掉「如果我在 $\bar\mu_t$，應該量到什麼」。

---

## 3. 問題設定

[▶ 11:29](https://youtu.be/PiCC-SxWlH8?t=689)

| 項目 | 設定 |
|---|---|
| 狀態 | $x_t = (x, y, \theta)^{\mathsf T}$，2D 位姿 |
| 地圖 | 一串**地標**（獨特的特徵：船例子裡的燈塔、影像裡的顯著特徵），位置已知 |
| 運動 | 里程計模型 $u_t = (\delta_{\text{rot1}}, \delta_{\text{trans}}, \delta_{\text{rot2}})^{\mathsf T}$ |
| 觀測 | 每個看到的地標給一個距離和方位 |
| 對應 | 假設知道每個觀測是哪個地標（課本稱「已知對應」） |

【課本補充】課本 §7.5（書頁 166）說，「地標可以唯一辨識」不一定是壞假設：例如巴黎的艾菲爾鐵塔，很少和別的地標搞混，而且全巴黎都看得到。

---

## 4. 運動模型：里程計

[▶ 12:22](https://youtu.be/PiCC-SxWlH8?t=742)

和 1-07 一樣，兩個位姿之間的移動拆成「轉 $\delta_{\text{rot1}}$ — 走 $\delta_{\text{trans}}$ — 轉 $\delta_{\text{rot2}}$」：

$$
\begin{bmatrix} x' \\ y' \\ \theta' \end{bmatrix}
= g(u_t, x_{t-1}) =
\begin{bmatrix}
x + \delta_{\text{trans}} \cos(\theta + \delta_{\text{rot1}}) \\
y + \delta_{\text{trans}} \sin(\theta + \delta_{\text{rot1}}) \\
\theta + \delta_{\text{rot1}} + \delta_{\text{rot2}}
\end{bmatrix}
+ \mathcal{N}(0, R_t)
$$

- 幾何來源 [▶ 13:31](https://youtu.be/PiCC-SxWlH8?t=811)：先轉 $\delta_{\text{rot1}}$，朝向變成 $\theta + \delta_{\text{rot1}}$；沿這個方向走 $\delta_{\text{trans}}$；最後再轉 $\delta_{\text{rot2}}$。
- $R_t$：運動雜訊的共變異數，文獻常叫**過程雜訊**（process noise）。
- 這個模型**對狀態是非線性**（有 $\cos$、$\sin$ of $\theta$），**對控制也是非線性** [▶ 14:38](https://youtu.be/PiCC-SxWlH8?t=878)：$\delta_{\text{trans}}$ 和 $\delta_{\text{rot1}}$ 相乘，而且 $\delta_{\text{rot1}}$ 在 $\cos$ 裡面。
- 所以要對**狀態**和**控制**各算一個 Jacobian。

### 4.1 對狀態的 Jacobian $G_t$

[▶ 15:34](https://youtu.be/PiCC-SxWlH8?t=934)

$g$ 有 3 個分量，狀態有 3 個變數 → $G_t$ 是 $3 \times 3$。第 1 欄是對 $x$ 的偏導，第 2 欄對 $y$，第 3 欄對 $\theta$。

講者示範第 1 列（$g_1 = x + \delta_{\text{trans}}\cos(\theta + \delta_{\text{rot1}})$）[▶ 16:39](https://youtu.be/PiCC-SxWlH8?t=999)：

- 對 $x$：只有 $x$ 這一項含 $x$ → $1$。
- 對 $y$：完全沒有 $y$ → $0$。
- 對 $\theta$：$\frac{\partial}{\partial\theta}\cos(\theta + \delta_{\text{rot1}}) = -\sin(\theta + \delta_{\text{rot1}})$ → $-\delta_{\text{trans}}\sin(\theta + \delta_{\text{rot1}})$。

第 2 列（$g_2 = y + \delta_{\text{trans}}\sin(\theta + \delta_{\text{rot1}})$）：$0$、$1$、$\delta_{\text{trans}}\cos(\theta + \delta_{\text{rot1}})$。
第 3 列（$g_3 = \theta + \delta_{\text{rot1}} + \delta_{\text{rot2}}$）：$0$、$0$、$1$。

$$
G_t = \frac{\partial g}{\partial x_{t-1}} =
\begin{bmatrix}
1 & 0 & -\delta_{\text{trans}} \sin(\theta + \delta_{\text{rot1}}) \\
0 & 1 & \delta_{\text{trans}} \cos(\theta + \delta_{\text{rot1}}) \\
0 & 0 & 1
\end{bmatrix}
$$

在 $\theta = \mu_{t-1,\theta}$ 求值。

（第 2、3 列是筆記依同樣方法補算的；講者說「每一列重複同樣的步驟再疊起來」，矩陣在投影片上。）

### 4.2 對控制的 Jacobian $V_t$

[▶ 17:38](https://youtu.be/PiCC-SxWlH8?t=1058)

控制 $u = (\delta_{\text{rot1}}, \delta_{\text{trans}}, \delta_{\text{rot2}})$ 是 3 維 → $V_t$ 也是 $3 \times 3$。第 1 欄對 $\delta_{\text{rot1}}$，第 2 欄對 $\delta_{\text{trans}}$，第 3 欄對 $\delta_{\text{rot2}}$。

逐項：

- $g_1$：對 $\delta_{\text{rot1}}$ → $-\delta_{\text{trans}}\sin(\theta + \delta_{\text{rot1}})$；對 $\delta_{\text{trans}}$ → $\cos(\theta + \delta_{\text{rot1}})$；對 $\delta_{\text{rot2}}$ → $0$。
- $g_2$：對 $\delta_{\text{rot1}}$ → $\delta_{\text{trans}}\cos(\theta + \delta_{\text{rot1}})$；對 $\delta_{\text{trans}}$ → $\sin(\theta + \delta_{\text{rot1}})$；對 $\delta_{\text{rot2}}$ → $0$。
- $g_3$：對 $\delta_{\text{rot1}}$ → $1$；對 $\delta_{\text{trans}}$ → $0$；對 $\delta_{\text{rot2}}$ → $1$。

$$
V_t = \frac{\partial g}{\partial u_t} =
\begin{bmatrix}
-\delta_{\text{trans}} \sin(\theta + \delta_{\text{rot1}}) & \cos(\theta + \delta_{\text{rot1}}) & 0 \\
\delta_{\text{trans}} \cos(\theta + \delta_{\text{rot1}}) & \sin(\theta + \delta_{\text{rot1}}) & 0 \\
1 & 0 & 1
\end{bmatrix}
$$

（矩陣是筆記依講者說的方法逐項算出的；投影片上的版本逐字稿看不到。）

`⚠️ 逐字稿缺字`：[▶ 17:49](https://youtu.be/PiCC-SxWlH8?t=1069) 講者說控制是「delta rotation one, delta translation and a delta translation two」，第三個應為 **delta rotation two**（口誤）。

**為什麼需要 $V_t$**：運動雜訊是在**控制空間**描述的（轉多少、走多少的誤差，見 1-07），但 EKF 的共變異數在**狀態空間** $(x, y, \theta)$。$V_t$ 把控制空間的雜訊映射到狀態空間（第 6 節）。

---

## 5. 觀測模型：距離—方位

[▶ 19:04](https://youtu.be/PiCC-SxWlH8?t=1144)

- 感測器對每個看到的特徵給**距離**（到燈塔多遠）和**方位**（燈塔在哪個角度）。
- 環境裡有很多特徵，用下標 $i$ 區分。一次看到 5 個特徵，就有 5 組量測。
- 定位問題：**地圖已知**，第 $i$ 個觀測對應地圖上第 $j$ 個地標，位置 $(m_{j,x}, m_{j,y})$。

$$
z_t^i = \begin{bmatrix} r_t^i \\ \phi_t^i \end{bmatrix}
= h(x_t, j, m) + \mathcal{N}(0, Q_t)
= \begin{bmatrix}
\sqrt{(m_{j,x} - x)^2 + (m_{j,y} - y)^2} \\
\operatorname{atan2}(m_{j,y} - y,\; m_{j,x} - x) - \theta
\end{bmatrix}
+ \mathcal{N}(0, Q_t)
$$

- 距離：機器人 $(x, y)$ 到地標的畢氏距離，就是**期望距離**。真的感測器還有雜訊 $Q_t$。
- 方位：連接機器人和地標的線的反正切，減掉機器人的朝向 $\theta$（量的是相對於機器人前方的角度，見 1-08 第 7.1 節）。
- 兩個都是非線性（平方根、反正切）→ 在 $\bar\mu_t$ 線性化。

（講者在 [▶ 21:14](https://youtu.be/PiCC-SxWlH8?t=1274) 口頭描述方位時沒提 $-\theta$；這裡依 1-08 和課本式 (7.9) 寫出。）

### 5.1 觀測的 Jacobian $H_t$

[▶ 21:52](https://youtu.be/PiCC-SxWlH8?t=1312)

講者說代數比較長，投影片上只給結果。$h$ 有 2 個分量、狀態有 3 個變數 → $H_t$ 是 $2 \times 3$。

以下推導**不是逐字稿內容**，是筆記依微分規則補上的。記

$$
\delta_x = m_{j,x} - \bar\mu_{t,x}, \qquad \delta_y = m_{j,y} - \bar\mu_{t,y}, \qquad q = \delta_x^2 + \delta_y^2
$$

注意 $\frac{\partial \delta_x}{\partial x} = -1$、$\frac{\partial \delta_y}{\partial y} = -1$。

**距離** $r = \sqrt{q}$：

$$
\frac{\partial r}{\partial x} = \frac{1}{2\sqrt q} \cdot 2\delta_x \cdot (-1) = -\frac{\delta_x}{\sqrt q}, \qquad
\frac{\partial r}{\partial y} = -\frac{\delta_y}{\sqrt q}, \qquad
\frac{\partial r}{\partial \theta} = 0
$$

**方位** $\phi = \operatorname{atan2}(\delta_y, \delta_x) - \theta$。用 $\frac{\partial}{\partial \delta_x}\operatorname{atan2}(\delta_y, \delta_x) = -\frac{\delta_y}{q}$、$\frac{\partial}{\partial \delta_y}\operatorname{atan2}(\delta_y, \delta_x) = \frac{\delta_x}{q}$：

$$
\frac{\partial \phi}{\partial x} = -\frac{\delta_y}{q} \cdot (-1) = \frac{\delta_y}{q}, \qquad
\frac{\partial \phi}{\partial y} = \frac{\delta_x}{q} \cdot (-1) = -\frac{\delta_x}{q}, \qquad
\frac{\partial \phi}{\partial \theta} = -1
$$

$$
H_t^i = \frac{\partial h}{\partial x_t}\bigg|_{\bar\mu_t} =
\begin{bmatrix}
-\dfrac{\delta_x}{\sqrt q} & -\dfrac{\delta_y}{\sqrt q} & 0 \\[2mm]
\dfrac{\delta_y}{q} & -\dfrac{\delta_x}{q} & -1
\end{bmatrix}
= \frac{1}{q}
\begin{bmatrix}
-\sqrt q\, \delta_x & -\sqrt q\, \delta_y & 0 \\
\delta_y & -\delta_x & -q
\end{bmatrix}
$$

（$\operatorname{atan2}$ 的偏導和 $\arctan(\delta_y/\delta_x)$ 相同：$\frac{d}{d\delta_x}\arctan\frac{\delta_y}{\delta_x} = \frac{1}{1 + \delta_y^2/\delta_x^2} \cdot \left(-\frac{\delta_y}{\delta_x^2}\right) = -\frac{\delta_y}{q}$。）

【課本補充】課本草稿版表 7.2 第 11 行（書頁 169）的 $H_t^i$ 排版有誤：第一列寫成 $(\sqrt q\, \delta_x, -\sqrt q\, \delta_y, 0)$、第二列寫成 $(\delta_y, \delta_x, -1)$，正負號和 $q$ 都對不上上面的逐項微分。以上面的推導為準。課本版本還多一列簽名 $s$，那一列全是 0（簽名不依賴位姿，所以對 EKF 更新沒有影響）。

---

## 6. 完整的 EKF 定位演算法

[▶ 23:15](https://youtu.be/PiCC-SxWlH8?t=1395)

講者：「看起來很多式子，其實只是代換。」

```
Algorithm EKF_localization(μ_{t-1}, Σ_{t-1}, u_t, z_t, m):
  θ = μ_{t-1,θ}
  // ---- 預測 ----
  G_t = [[1, 0, -δ_trans sin(θ+δ_rot1)],
         [0, 1,  δ_trans cos(θ+δ_rot1)],
         [0, 0,  1]]
  V_t = [[-δ_trans sin(θ+δ_rot1), cos(θ+δ_rot1), 0],
         [ δ_trans cos(θ+δ_rot1), sin(θ+δ_rot1), 0],
         [ 1,                     0,             1]]
  M_t = 控制空間的雜訊共變異數（見下）
  μ̄_t = μ_{t-1} + [δ_trans cos(θ+δ_rot1), δ_trans sin(θ+δ_rot1), δ_rot1+δ_rot2]ᵀ
  Σ̄_t = G_t Σ_{t-1} G_tᵀ + V_t M_t V_tᵀ
  // ---- 修正：對每個看到的地標 ----
  for all observed features z_t^i = (r, φ)ᵀ do
    j  = 這個觀測對應的地標
    δ  = (m_{j,x} - μ̄_{t,x}, m_{j,y} - μ̄_{t,y})ᵀ
    q  = δᵀδ
    ẑ  = (√q, atan2(δ_y, δ_x) - μ̄_{t,θ})ᵀ
    H  = (1/q) [[-√q δ_x, -√q δ_y, 0],
                [ δ_y,    -δ_x,   -q]]
    K  = Σ̄_t Hᵀ (H Σ̄_t Hᵀ + Q_t)⁻¹
    μ̄_t = μ̄_t + K (z_t^i - ẑ)
    Σ̄_t = (I - K H) Σ̄_t
  endfor
  return μ_t = μ̄_t, Σ_t = Σ̄_t
```

**預測步** [▶ 24:06](https://youtu.be/PiCC-SxWlH8?t=1446)：

- 平均值：上一步平均值加上非線性運動模型 $g$。
- 共變異數兩項：
  - $G_t \Sigma_{t-1} G_t^{\mathsf T}$：上一步的不確定性經運動模型傳播。
  - $V_t M_t V_t^{\mathsf T}$：**這次運動新加的不確定性**。$M_t$ 是控制空間的雜訊（執行 $\delta_{\text{rot1}}$、$\delta_{\text{trans}}$、$\delta_{\text{rot2}}$ 時實際的誤差），$V_t$ 把它映射到狀態空間 [▶ 25:26](https://youtu.be/PiCC-SxWlH8?t=1526)。
- 這相當於 1-10 的 $R_t = V_t M_t V_t^{\mathsf T}$。

**$M_t$ 怎麼給**：講者沒寫出 $M_t$ 的式子。以下**不是逐字稿內容**，是依 1-07 的里程計雜訊模型推論的：三個參數的雜訊互相獨立，標準差分別是 $\alpha_1|\delta_{\text{rot1}}| + \alpha_2\delta_{\text{trans}}$ 等（1-07 第 5.2 節），所以

$$
M_t = \operatorname{diag}\!\Bigl( (\alpha_1|\delta_{\text{rot1}}| + \alpha_2\delta_{\text{trans}})^2,\;
(\alpha_3\delta_{\text{trans}} + \alpha_4(|\delta_{\text{rot1}}| + |\delta_{\text{rot2}}|))^2,\;
(\alpha_1|\delta_{\text{rot2}}| + \alpha_2\delta_{\text{trans}})^2 \Bigr)
$$

【課本補充】課本 §7.5.3（書頁 172）也提到：運動雜訊的大小取決於運動量，所以 $R_t$ 是控制和 $\mu_{t-1}$ 的函數；課本把設計它留作習題。

**修正步** [▶ 27:37](https://youtu.be/PiCC-SxWlH8?t=1657)：

- 可以同時看到很多特徵，對**每一個**都做一次修正。看到 10 個新特徵就做 10 次更新。
- 每個特徵：用預測位置和地圖上的地標位置算出**期望觀測** $\hat z$，再算新息、增益、更新。

（上面的虛擬碼把每個特徵一個接一個地更新，每次用前一次更新後的 $\bar\mu_t, \bar\Sigma_t$。講者只說「對每個量測做更新」，沒有指定細節。課本草稿版表 7.2 則是先對所有特徵算增益，再一起加總：$\mu_t = \bar\mu_t + \sum_i K_t^i(z_t^i - \hat z_t^i)$。）

---

## 7. 圖解一次迭代

### 7.1 預測

[▶ 25:59](https://youtu.be/PiCC-SxWlH8?t=1559)

- 在 $t-1$：機器人在某位置，朝向用一條線表示，不確定性是淺灰色橢圓。
- 執行 $u_t$，到新位置。
- 新的不確定性來自兩處：
  1. 原本就不確定在哪 → 下一步也不確定（$G_t \Sigma_{t-1} G_t^{\mathsf T}$）。
  2. 控制本身的不確定性（$V_t M_t V_t^{\mathsf T}$）。
- 兩者相加 → 更大的深灰色橢圓 $\bar\Sigma_t$。

### 7.2 期望觀測與新息

[▶ 28:40](https://youtu.be/PiCC-SxWlH8?t=1720)

- 在 $(x, y)$ 空間：圖上畫出估計的位置（帶不確定性）和**真實位置**（只是為了說明，實際上不知道，這正是要估計的）。兩者有誤差。
- 實際量測 $z_t$ 取決於**真實位置**；期望量測 $\hat z_t$ 取決於**估計位置**。因為估計錯了，兩者不同。
- 在**量測空間**看 [▶ 29:43](https://youtu.be/PiCC-SxWlH8?t=1783)：橫軸距離、縱軸方位。
  - 你認為特徵在 $\hat z_t$，帶有不確定性（因為你本來就不確定自己在哪，這個不確定性帶進了「特徵在哪」）。
  - 感測器實際給 $z_t$。
  - 兩者的差就是**新息**向量。

### 7.3 修正

[▶ 31:07](https://youtu.be/PiCC-SxWlH8?t=1867)

- 算 Kalman 增益，用新息更新平均值和共變異數。
- 運動後的估計 $\bar\mu_t$：比較不確定，離真實位置比較遠。
- 修正後：位置**更接近真實位置**，而且**更確定**（橢圓變小）。
- 這就是 EKF 在這個應用上的一次迭代；機器人一直移動，就一直重複。

【課本補充】課本 §7.5.1（書頁 167–168）用一維走廊三扇門的例子（1-03 的例子）說明 EKF 定位：為了配合單峰高斯，假設 (1) 知道看到的是哪一扇門，(2) 初始位置大致已知。修正後的變異數比原本的 belief 和觀測密度都小，因為「結合兩個獨立估計，應該比各自單獨更確定」。

---

## 8. 模擬例子

[▶ 32:35](https://youtu.be/PiCC-SxWlH8?t=1955)

- 模擬環境裡有幾個特徵（想成燈塔）。機器人實際沿一條**方形**路徑走。
- 只用運動（航位推算）：粉紅色軌跡，過一段時間就**漂走**了。因為沒有任何地圖資訊可以修正。
- EKF：藍色軌跡。每 5 步偵測一次地標（紅色特徵周圍的綠色表示偵測到），每次偵測就做修正。
- 運動時共變異數**變大**（藍色橢圓變大）；一觀測到特徵，共變異數又**縮小**。
- 最後藍色軌跡幾乎和真實軌跡完全重疊。

---

## 9. 總結

[▶ 34:31](https://youtu.be/PiCC-SxWlH8?t=2071)

- 這集是 EKF 在 2D 定位的應用。
- 需要 EKF 而不是 KF，因為運動模型和觀測模型都是非線性的。大部分機器人、真實世界的應用都需要這個延伸版本。
- 線性化是一種近似。但如果離真實解夠近、雜訊不太大，估計就很好：「不是最佳，但很接近最佳」。
- 延伸閱讀：《Probabilistic Robotics》第 3 章、第 7 章；一篇關於操作高斯密度的論文（推導 KF 時會用到裡面的步驟；1-10 也推薦過）。

---

## 10. 一頁速查表

### 10.1 模型

| 項 | 公式 |
|---|---|
| 運動 $g$ | $(x + \delta_{\text{trans}}\cos(\theta + \delta_{\text{rot1}}),\; y + \delta_{\text{trans}}\sin(\theta + \delta_{\text{rot1}}),\; \theta + \delta_{\text{rot1}} + \delta_{\text{rot2}})$ |
| 觀測 $h$ | $(\sqrt q,\; \operatorname{atan2}(\delta_y, \delta_x) - \theta)$，$\delta = m_j - (x, y)$，$q = \delta^{\mathsf T}\delta$ |

### 10.2 Jacobian（$c = \cos(\theta + \delta_{\text{rot1}})$，$s = \sin(\theta + \delta_{\text{rot1}})$）

| Jacobian | 矩陣 | 關鍵一步 |
|---|---|---|
| $G_t = \partial g/\partial x$ | $\begin{bmatrix} 1 & 0 & -\delta_{\text{trans}} s \\ 0 & 1 & \delta_{\text{trans}} c \\ 0 & 0 & 1 \end{bmatrix}$ | $\partial_\theta \cos = -\sin$ |
| $V_t = \partial g/\partial u$ | $\begin{bmatrix} -\delta_{\text{trans}} s & c & 0 \\ \delta_{\text{trans}} c & s & 0 \\ 1 & 0 & 1 \end{bmatrix}$ | 欄序：$\delta_{\text{rot1}}, \delta_{\text{trans}}, \delta_{\text{rot2}}$ |
| $H_t = \partial h/\partial x$ | $\frac{1}{q}\begin{bmatrix} -\sqrt q\,\delta_x & -\sqrt q\,\delta_y & 0 \\ \delta_y & -\delta_x & -q \end{bmatrix}$ | $\partial\delta_x/\partial x = -1$；$\partial_{\delta_x}\operatorname{atan2} = -\delta_y/q$ |

### 10.3 更新

| 步驟 | 公式 |
|---|---|
| 預測平均 | $\bar\mu_t = g(u_t, \mu_{t-1})$ |
| 預測共變異數 | $\bar\Sigma_t = G_t\Sigma_{t-1}G_t^{\mathsf T} + V_t M_t V_t^{\mathsf T}$ |
| 每個地標 | $K = \bar\Sigma H^{\mathsf T}(H\bar\Sigma H^{\mathsf T} + Q_t)^{-1}$，$\bar\mu \leftarrow \bar\mu + K(z^i - \hat z^i)$，$\bar\Sigma \leftarrow (I - KH)\bar\Sigma$ |

### 10.4 實作注意（推論）

- 方位的新息 $\phi - \hat\phi$ 要正規化到 $[-\pi, \pi]$（同 1-07 課本提醒的角度差問題）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| EKF 只能單峰、需初始位置大致已知 | 1-14 粒子濾波／MCL（可以全域定位） |
| 已知對應的假設 | 1-21 定位總覽（資料關聯問題） |
| 地標當作狀態的一部分一起估計 | EKF SLAM（MSR2 2-03 SLAM 入門提到） |
| $V_t M_t V_t^{\mathsf T}$：把雜訊從一個空間映射到另一個 | MSR2：2-11 Graph SLAM（資訊矩陣、Jacobian） |

---

## 附：本集一句話總結

> **EKF 定位 = EKF ＋ 里程計運動模型 ＋ 距離方位觀測模型。關鍵是三個 Jacobian：$G_t$（對狀態）、$V_t$（對控制，把控制雜訊 $M_t$ 映射成 $V_t M_t V_t^{\mathsf T}$）、$H_t$（觀測對狀態）；運動讓橢圓變大，看到地標讓它變小。**

---

*筆記依據 Nived Chebrolu「Mobile Sensing and Robotics 1」EKF Localization 錄影逐字稿（Whisper `medium.en`，36:21）與《Probabilistic Robotics》早期草稿版 §7.5 整理。*
