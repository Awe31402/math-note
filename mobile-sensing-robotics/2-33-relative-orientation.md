---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-33
lecture: Relative Orientation, Fundamental and Essential Matrix
date: 待補（2021 夏季學期）
video: https://youtu.be/gYYumFSDsvA
notes: MVG 第 9 章（書頁 239–259，PDF 頁 257–277）；《視覺 SLAM 十四講》第 2 版 §7.3（書頁 165–170，PDF 頁 188–193）
---

# 第 2-33 集 · 相對定向、基本矩陣與本質矩陣 [▶ 影片](https://youtu.be/gYYumFSDsvA)

← 上一集：[2-31-p3p-grunert](2-31-p3p-grunert.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-35-epipolar-geometry](2-35-epipolar-geometry.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-33 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（59:50，Whisper `medium.en` 轉錄）＋ MVG 第 9 章 ＋《視覺 SLAM 十四講》§7.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 相機對](#1-相機對)
- [2. 參數計數：能估計什麼](#2-參數計數能估計什麼)
  - [2.1 已校正相機：5 個](#21-已校正相機5-個)
  - [2.2 未校正相機：7 個](#22-未校正相機7-個)
- [3. 共面約束](#3-共面約束)
- [4. 基本矩陣 F](#4-基本矩陣-f)
- [5. 從投影矩陣算 F](#5-從投影矩陣算-f)
- [6. F 的兩種定義（轉置）](#6-f-的兩種定義轉置)
- [7. 本質矩陣 E](#7-本質矩陣-e)
- [8. 相對定向的參數化](#8-相對定向的參數化)
- [9. 總結](#9-總結)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

從一台相機進到**兩台相機**：不知道場景，只靠兩張影像的點對應，能估計兩台相機的哪些相對關係？引出描述相對定向的兩個矩陣：未校正相機的**基本矩陣** $F$、已校正相機的**本質矩陣** $E$。

---

## 1. 相機對

[▶ 00:10](https://youtu.be/gYYumFSDsvA?t=10)

- **雙眼相機**：兩台實體相機剛性固定、同時拍照。**立體正規情形**（stereo normal case）：兩台相機朝同一方向，只沿一個方向偏移。
- 也可以是**一台相機在環境中移動**，在兩個位置各拍一張；或兩台相機自由移動。
- 相機對 = 兩個拍照的組態，用這兩張影像估計東西（例如兩台相機拍照時的相對定向）。

---

## 2. 參數計數：能估計什麼

[▶ 02:05](https://youtu.be/gYYumFSDsvA?t=125)

**理論最大參數數**：

| | 每台相機 | 相機對 |
|---|---|---|
| 已校正（只有外參） | 6（位置 3 ＋ 朝向 3） | **12** |
| 未校正（外參＋5 內參；兩台的 $K$ 可能不同） | 11 | **22** |

**關鍵問題** [▶ 04:50](https://youtu.be/gYYumFSDsvA?t=290)：**不知道場景**也能估計相機運動嗎？P3P（3 個控制點）和 DLT 都用了場景知識；這裡只用兩張影像。

- 從單張影像很難估**尺度**：人類能估物體大小是靠學過的知識；只看影像本身不可能（可以做出讓人誤判大小的影像）。相機是**方向量測裝置**，不知道物體多遠。

### 2.1 已校正相機：5 個

[▶ 07:44](https://youtu.be/gYYumFSDsvA?t=464)

記號：單撇 $'$ = 相機 1，雙撇 $''$ = 相機 2。

- 固定相機 1 當參考座標系。相機 2 看到一個盒子（不知道大小，甚至不知道是盒子）。
- 把相機 2 沿著兩投影中心的連線**往外移**，同時把場景**放大**：同一個像素仍看到同一個點 → 產生**完全相同**的影像。
- → 無法得到相機 2 相對相機 1 的完整平移：**不知道兩台相機多遠**（尺度）。也不知道相機 1 在全域座標系的位置（全域平移、旋轉）。

| 無法估計 | 數量 |
|---|---|
| 全域平移 | 3 |
| 全域旋轉 | 3 |
| 尺度（兩相機的距離） | 1 |
| **合計** | **7**（= 一個**相似轉換**） |

$$
12 - 7 = \boxed{5}\ \text{個可估計的參數}
$$

- 可估：相機 2 相對相機 1 的**旋轉** $R$（3）＋ 連接投影中心的**基線向量** $\boldsymbol b$ 的**方向**（2）；$\boldsymbol b$ 的長度不行。
- 已校正相機給出**保角**映射。
- 用兩台已校正相機重建出的場景模型叫**攝影測量模型**（photogrammetric model）：只知道到一個相似轉換（沒有全域位置、朝向、尺度）。

**相對定向 vs 絕對定向** [▶ 14:03](https://youtu.be/gYYumFSDsvA?t=843)：

- **相對定向**：相機 2 相對相機 1（已校正：5 個參數）——本集主題，只靠影像就能估。
- **絕對定向**：把攝影測量模型放進真實世界（固定那個相似轉換的 7 個參數）——需要場景知識，例如 3 個已知 3D 點。

**要得到完整 3D 模型需要什麼** [▶ 15:04](https://youtu.be/gYYumFSDsvA?t=904)（以空拍影像中屋頂上的點為例）：

- 3 個已知 3D 點；或
- 兩台相機的完整位姿（直接三角化）；或
- 相機 1 的位置（固定 6 個自由度）＋ **基線長度**（第 7 個：尺度）；或
- 真實世界中的已知距離。

### 2.2 未校正相機：7 個

[▶ 17:12](https://youtu.be/gYYumFSDsvA?t=1032)

- 只考慮每台 11 個自由度（無非線性誤差）→ **保直線**但**不保角**的映射。
- 重建出的物體只能到一個**射影轉換**：3D 射影轉換是 $4 \times 4$ 齊次矩陣，16 − 1（比例）= **15** 個自由度。

$$
22 - 15 = \boxed{7}\ \text{個可估計的參數}
$$

- 絕對定向至少要 **5** 個控制點（$3 \times 5 = 15$）。
- （講者這段有幾處口誤：說「DLT 需要 5 個控制點」應為 6；說「7 個相對於**未**校正相機的 5 個」應為「已校正」；說「已校正相機的絕對定向要 5 個點」應為未校正。依上下文更正。）

**整理** [▶ 19:35](https://youtu.be/gYYumFSDsvA?t=1175)：

| | 每台 | 相機對 | 相對定向（只靠影像） | 絕對定向（需場景） | 最少控制點 |
|---|---|---|---|---|---|
| 已校正 | 6 | 12 | **5** | 7（相似轉換） | 3 |
| 未校正 | 11 | 22 | **7** | 15（射影轉換） | 5 |

- 【口頭】相對定向很重要：拿相機在世界中移動，不需要任何場景知識，只要找到兩張影像中相同的點（不知道它們在世界的哪裡），就能恢復相機運動（已校正 5、未校正 7 個自由度）[▶ 21:23](https://youtu.be/gYYumFSDsvA?t=1283)。

---

## 3. 共面約束

[▶ 22:07](https://youtu.be/gYYumFSDsvA?t=1327)

- 假設沒有雜訊。相機 1、相機 2 都看到點 $\boldsymbol X$ → 兩條射線**交於** $\boldsymbol X$ → 兩條射線在同一個 3D 平面上 → 連接兩投影中心的向量也在這個平面上。
- 三個向量共面 ⇔ **純量三重積**為零：

$$
\bigl[\ \overrightarrow{O'X'},\ \ \overrightarrow{O'O''},\ \ \overrightarrow{O''X''}\ \bigr] = 0
$$

（$X'$、$X''$ 指同一個 3D 點 $X$，分別從兩台相機看；三個向量不必是單位向量。）

**純量三重積**（德文 Spatprodukt）[▶ 25:08](https://youtu.be/gYYumFSDsvA?t=1508)：

$$
[\boldsymbol a, \boldsymbol b, \boldsymbol c] = (\boldsymbol a \times \boldsymbol b)\cdot\boldsymbol c
$$

- = 三個向量張成的**平行六面體體積**。
- $\boldsymbol a \times \boldsymbol b$ 垂直於 $\boldsymbol a, \boldsymbol b$；再和 $\boldsymbol c$ 內積為零 ⇔ $\boldsymbol c$ 在 $\boldsymbol a, \boldsymbol b$ 張成的平面上 ⇔ 體積為零 ⇔ 三向量共面。
- 這個約束不需要任何場景知識，只要兩台相機看到同一個點。

---

## 4. 基本矩陣 F

[▶ 26:47](https://youtu.be/gYYumFSDsvA?t=1607)

**投影**（同一個未知的 3D 點 $\mathbf X$）：

$$
\mathbf x' = K'R'\,[\,I_3 \mid -\boldsymbol X_{O'}\,]\,\mathbf X, \qquad
\mathbf x'' = K''R''\,[\,I_3 \mid -\boldsymbol X_{O''}\,]\,\mathbf X
$$

**正規化方向向量** [▶ 28:18](https://youtu.be/gYYumFSDsvA?t=1698)：$K^{-1}\mathbf x$ 是相機座標系中的方向；再乘 $R^{-1}$ 轉到共同的座標系：

$$
{}^{n}\mathbf x' = (R')^{-1}(K')^{-1}\,\mathbf x' = [\,I_3 \mid -\boldsymbol X_{O'}\,]\,\mathbf X \quad (\text{到比例}), \qquad
{}^{n}\mathbf x'' = (R'')^{-1}(K'')^{-1}\,\mathbf x''
$$

這就是 $\overrightarrow{O'X'}$、$\overrightarrow{O''X''}$。**基線**：

$$
\boldsymbol b = \overrightarrow{O'O''} = \boldsymbol X_{O''} - \boldsymbol X_{O'}
$$

**代入三重積** [▶ 31:04](https://youtu.be/gYYumFSDsvA?t=1864)：$[{}^n\mathbf x', \boldsymbol b, {}^n\mathbf x''] = {}^n\mathbf x'^{\mathsf T}(\boldsymbol b \times {}^n\mathbf x'') = 0$，把外積寫成**反對稱矩陣**：

$$
\boldsymbol b \times \boldsymbol x = S_{\boldsymbol b}\,\boldsymbol x, \qquad
S_{\boldsymbol b} = \begin{bmatrix} 0 & -b_3 & b_2 \\ b_3 & 0 & -b_1 \\ -b_2 & b_1 & 0 \end{bmatrix}
$$

- 驗證第一列：$0\cdot x_1 - b_3x_2 + b_2x_3 = b_2x_3 - b_3x_2$，正是外積的第一分量 [▶ 32:30](https://youtu.be/gYYumFSDsvA?t=1950)。
- 反對稱：對角為零，下三角是上三角的負值，$S^{\mathsf T} = -S$。好處：外積變成矩陣乘法，可以寫成一串矩陣相乘。

$$
{}^{n}\mathbf x'^{\mathsf T}\,S_{\boldsymbol b}\,{}^{n}\mathbf x'' = 0
$$

**展開** [▶ 35:04](https://youtu.be/gYYumFSDsvA?t=2104)：

$$
\mathbf x'^{\mathsf T}\,(K')^{-\mathsf T}(R')^{-\mathsf T}\,S_{\boldsymbol b}\,(R'')^{-1}(K'')^{-1}\,\mathbf x'' = 0
$$

旋轉矩陣 $R^{-\mathsf T} = R$、$R^{-1} = R^{\mathsf T}$，中間 5 個矩陣合成一個 $3 \times 3$ 矩陣：

$$
\boxed{\;F = (K')^{-\mathsf T}\,R'\,S_{\boldsymbol b}\,R''^{\mathsf T}\,(K'')^{-1}, \qquad \mathbf x'^{\mathsf T}F\,\mathbf x'' = 0\;}
$$

- $F$：**基本矩陣**（fundamental matrix），包含未校正相機相對定向的**所有**可估資訊。
- **共面約束**：同一個 3D 點的兩個像素座標必須滿足 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$——之後會反覆用到。
- 前提是點量得完美；實際上有雜訊，只會是很小的值。
- $F$ 有 **7 個自由度**（22 − 15）。

【課本補充】MVG §9.2（書頁 242–246）的其他推導：

- **幾何**：經過任一平面 $\pi$ 的點轉移 $\mathbf x' = H_\pi\mathbf x$，對極線 $\boldsymbol l' = \boldsymbol e' \times \mathbf x' = [\boldsymbol e']_\times H_\pi\mathbf x$ → $F = [\boldsymbol e']_\times H_\pi$（結果 9.1）。$[\boldsymbol e']_\times$ 秩 2、$H$ 秩 3 → **$F$ 秩 2**。
- **7 個自由度**的另一種算法：$3 \times 3$ 齊次矩陣有 8 個獨立比例，再加上 $\det F = 0$ 這個約束，少一個。
- 兩相機中心重合時 $F = 0$（純旋轉沒有基線）。

【十四講補充】§7.3.1（書頁 166–167）用歸一化座標推導：$\boldsymbol x_1 = K^{-1}\boldsymbol p_1$、$\boldsymbol x_2 = K^{-1}\boldsymbol p_2$，$\boldsymbol x_2 \simeq R\boldsymbol x_1 + \boldsymbol t$（式 7.5）；兩邊左乘 $\boldsymbol t^\wedge$（和 $\boldsymbol t$ 做外積）再左乘 $\boldsymbol x_2^{\mathsf T}$：左邊 $\boldsymbol x_2^{\mathsf T}\boldsymbol t^\wedge\boldsymbol x_2 = 0$（$\boldsymbol t^\wedge\boldsymbol x_2$ 垂直於 $\boldsymbol x_2$），所以

$$
\boldsymbol x_2^{\mathsf T}\,\boldsymbol t^\wedge R\,\boldsymbol x_1 = 0, \qquad \boldsymbol p_2^{\mathsf T}K^{-\mathsf T}\boldsymbol t^\wedge RK^{-1}\boldsymbol p_1 = 0 \qquad (7.8,\ 7.9)
$$

幾何意義：$O_1, P, O_2$ 三點共面——和講者的共面約束一樣（$\boldsymbol t^\wedge$ 就是反對稱矩陣 $S_{\boldsymbol t}$）。

---

## 5. 從投影矩陣算 F

[▶ 39:03](https://youtu.be/gYYumFSDsvA?t=2343)

已知兩台相機的投影矩陣 $P', P''$（$3 \times 4$），能直接算 $F$ 嗎？可以，做法類似 DLT 的拆解，但更簡單：

$$
P' = [\,A' \mid \boldsymbol a'\,], \qquad A' = K'R', \qquad \boldsymbol a' = -K'R'\boldsymbol X_{O'}
$$

- 投影中心：$(A')^{-1}\boldsymbol a' = -R'^{\mathsf T}K'^{-1}K'R'\boldsymbol X_{O'} = -\boldsymbol X_{O'}$ → $\boldsymbol X_{O'} = -(A')^{-1}\boldsymbol a'$；相機 2 同理。
- 基線：$\boldsymbol b = \boldsymbol X_{O''} - \boldsymbol X_{O'}$。

$$
\boxed{\;F = (A')^{-\mathsf T}\,S_{\boldsymbol b}\,(A'')^{-1}\;}
$$

（驗證：$(A')^{-\mathsf T} = (K'R')^{-\mathsf T} = K'^{-\mathsf T}R'$、$(A'')^{-1} = R''^{\mathsf T}K''^{-1}$，和第 4 節的 $F$ 相同。這個檢查是筆記補的。）

- （講者說「$P$ 是 $4 \times 3$ 矩陣」，應為 $3 \times 4$；說「足以建立本質矩陣」，這裡應為基本矩陣。）

---

## 6. F 的兩種定義（轉置）

[▶ 42:44](https://youtu.be/gYYumFSDsvA?t=2564)

- 把共面約束整個轉置：$\mathbf x''^{\mathsf T}F^{\mathsf T}\mathbf x' = 0$ → 另一種定義的基本矩陣是 $F^{\mathsf T}$。
- 多相機時：從相機 $i$ 到 $j$ 的 $F_{ij}$，另一種是 $F_{ji} = F_{ij}^{\mathsf T}$。
- 本課用 $F_{12}$（攝影測量的標準）；**Hartley & Zisserman**（3D 幾何的「聖經」，即 MVG）用相反的定義 $F_{21} = F_{12}^{\mathsf T}$。看 MVG 的式子時要記得差一個轉置。
- `⚠️ 逐字稿缺字`：Whisper 寫 “Hartley Scissor Man”，應為 **Hartley & Zisserman**。

【課本補充】MVG（書頁 245）的寫法是 $\mathbf x'^{\mathsf T}F\mathbf x = 0$，其中 $\mathbf x$ 在**第一**張、$\mathbf x'$ 在**第二**張影像——所以 $F_{\text{MVG}} = F_{\text{本課}}^{\mathsf T}$。MVG 的其他性質（用 MVG 的記號）：

| 性質 | 式子 |
|---|---|
| 對極線 | $\boldsymbol l' = F\mathbf x$（$\mathbf x$ 在第二張的對極線）；$\boldsymbol l = F^{\mathsf T}\mathbf x'$ |
| 極點 | $F\boldsymbol e = 0$（右零向量）、$F^{\mathsf T}\boldsymbol e' = 0$（左零向量） |
| 從相機算 | $P = K[I \mid 0]$、$P' = K'[R \mid \boldsymbol t]$ → $F = K'^{-\mathsf T}[\boldsymbol t]_\times RK^{-1}$ |
| 反序 | $F^{\mathsf T}$ 是相機對 $(P', P)$ 的基本矩陣 |

---

## 7. 本質矩陣 E

[▶ 44:41](https://youtu.be/gYYumFSDsvA?t=2681)

- **本質矩陣** = 已校正相機的基本矩陣。大多時候我們用已校正相機（例如張正友法，2-29）：把影像用 $K$ 修正後就是已校正相機，校正參數完全拿掉，定向問題更簡單（假設沒有那 5 個參數以外的畸變）。
- 已校正相機中，$K^{-1}\mathbf x$ 直接就是相機座標系中的方向 ${}^{k}\mathbf x$。

**推導** [▶ 47:02](https://youtu.be/gYYumFSDsvA?t=2822)：從 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$ 展開，$\mathbf x'^{\mathsf T}K'^{-\mathsf T} = {}^{k}\mathbf x'^{\mathsf T}$、$K''^{-1}\mathbf x'' = {}^{k}\mathbf x''$：

$$
\boxed{\;{}^{k}\mathbf x'^{\mathsf T}\,E\,{}^{k}\mathbf x'' = 0, \qquad E = R'\,S_{\boldsymbol b}\,R''^{\mathsf T}\;}
$$

- 只含**旋轉**和**基線**參數，校正矩陣消失 → **5 個自由度**（就是已校正相機可估的 5 個）。
- $E$ 是 $3 \times 3$（9 個元素），5 個參數 → **4 個約束**：一個來自齊次（比例），其他是對**奇異值**的約束（2-37 會用到）。

【課本補充】MVG §9.6（書頁 257–259）：

- 歸一化座標 $\hat{\mathbf x} = K^{-1}\mathbf x$；$P = [I \mid 0]$、$P' = [R \mid \boldsymbol t]$ 的基本矩陣叫本質矩陣 $E = [\boldsymbol t]_\times R$；$\hat{\mathbf x}'^{\mathsf T}E\hat{\mathbf x} = 0$；$E = K'^{\mathsf T}FK$（式 9.12）。歷史上 Longuet-Higgins 先提出 $E$，$F$ 是去掉「已校正」這個（非本質的）假設後的推廣。
- **結果 9.17**：$3 \times 3$ 矩陣是本質矩陣 ⇔ **兩個奇異值相等、第三個為零**。
- 從 $E$ 取回相機（結果 9.19）：$E = U\operatorname{diag}(1, 1, 0)V^{\mathsf T}$，$W = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$，四組解 $P' = [UWV^{\mathsf T} \mid \pm\boldsymbol u_3]$、$[UW^{\mathsf T}V^{\mathsf T} \mid \pm\boldsymbol u_3]$（$\boldsymbol u_3$ 是 $U$ 的最後一欄）。只有一組讓重建的點在兩台相機**前方**，用一個點測試就能選出（詳見 2-37）。

【十四講補充】§7.3.1–7.3.2（書頁 167–168）：$E = \boldsymbol t^\wedge R$、$F = K^{-\mathsf T}EK^{-1}$、$\boldsymbol x_2^{\mathsf T}E\boldsymbol x_1 = \boldsymbol p_2^{\mathsf T}F\boldsymbol p_1 = 0$（式 7.10）。位姿估計變成兩步：由配對點求 $E$ 或 $F$，再由 $E$ 或 $F$ 求 $R, \boldsymbol t$。SLAM 中內參通常已知，所以實務上多用形式較簡單的 $E$。$E$ 的性質：乘任意非零常數仍滿足約束（尺度等價）；奇異值必為 $[\sigma, \sigma, 0]$（內在性質）；6 − 1 = 5 個自由度。

---

## 8. 相對定向的參數化

[▶ 51:08](https://youtu.be/gYYumFSDsvA?t=3068)

怎麼參數化那 5 個自由度？都是把相機 1 放在參考座標系原點，描述相機 2：

| 參數化 | 參數 | 說明 |
|---|---|---|
| **相依影像的一般參數化**（general parameterization of dependent images） | $R$（相機 2 相對相機 1）＋ 基線 $\boldsymbol b$，**$\lVert\boldsymbol b\rVert = 1$** | 6 個參數 ＋ 1 個約束。**今天最常用** |
| **相依影像的攝影測量參數化** | $R$ ＋ $b_y, b_z$，**$b_x$ 設為常數** | 5 個參數、沒有約束。傳統：飛機往下拍、沿 $x$ 方向等速飛。$b_x = 0$（沒有沿 $x$ 的運動）時數值出問題（只能讓 $b_y, b_z \to \infty$） |
| **獨立影像的參數化** | $R_1, R_2$ ＋ 固定單位長的基線方向 | 全用旋轉表示（強調相機是方向量測裝置）；6 個旋轉參數，但兩台同時轉相同角度無法分辨 → 有一個相依 |

**一般參數化的本質矩陣** [▶ 56:22](https://youtu.be/gYYumFSDsvA?t=3382)：相機 1 是參考座標系，$R' = I$；相對定向的旋轉就是相機 2 的旋轉 $R'' = R$：

$$
E = S_{\boldsymbol b}\,R^{\mathsf T}, \qquad \boldsymbol b = (b_x, b_y, b_z)^{\mathsf T}, \quad b_x^2 + b_y^2 + b_z^2 = 1
$$

【十四講補充】§7.3.2（書頁 169–170）把 $E$ 分解回 $R, \boldsymbol t$ 時同樣只能得到單位長（或任意尺度）的 $\boldsymbol t$——對應這裡「$\lVert\boldsymbol b\rVert = 1$」。

---

## 9. 總結

[▶ 58:08](https://youtu.be/gYYumFSDsvA?t=3488)

- 影像對的參數、相對定向的描述。
- 未校正相機 → **基本矩陣** $F$，共面約束 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$。
- 已校正相機 → **本質矩陣** $E$（「已校正相機對的基本矩陣」），${}^k\mathbf x'^{\mathsf T}E\,{}^k\mathbf x'' = 0$，用相機座標系的影像座標。
- 參數化：最常用的是相依影像的一般參數化（相機 1 在原點，$R$ 表示相機 2 的朝向，單位長的基線方向）。
- 延伸閱讀：Förstner & Wrobel 的 *Photogrammetric Computer Vision* 第 12.2 節。
- `⚠️ 逐字稿缺字`：Whisper 寫 “first and robust book”，推測為 **Förstner & Wrobel** 的書（同 2-29）。

---

## 10. 一頁速查表

### 10.1 參數計數

| | 相機對 | 相對定向 | 絕對定向 | 控制點 |
|---|---|---|---|---|
| 已校正 | 12 | 5（$R$ 3 ＋ $\boldsymbol b$ 方向 2） | 7（相似） | ≥ 3 |
| 未校正 | 22 | 7 | 15（射影） | ≥ 5 |

關鍵一步：相機 2 沿基線外移、場景等比放大 → 影像完全相同 → 尺度不可知。

### 10.2 共面約束 → F

$$
[\overrightarrow{O'X'}, \boldsymbol b, \overrightarrow{O''X''}] = 0
\ \Rightarrow\
{}^n\mathbf x'^{\mathsf T}S_{\boldsymbol b}\,{}^n\mathbf x'' = 0, \quad {}^n\mathbf x = R^{\mathsf T}K^{-1}\mathbf x
$$

$$
F = K'^{-\mathsf T}R'\,S_{\boldsymbol b}\,R''^{\mathsf T}K''^{-1} = (A')^{-\mathsf T}S_{\boldsymbol b}(A'')^{-1}, \qquad \mathbf x'^{\mathsf T}F\mathbf x'' = 0
$$

| 性質 | F | E |
|---|---|---|
| 相機 | 未校正 | 已校正 |
| 式子 | $K'^{-\mathsf T}R'S_{\boldsymbol b}R''^{\mathsf T}K''^{-1}$ | $R'S_{\boldsymbol b}R''^{\mathsf T}$（一般參數化：$S_{\boldsymbol b}R^{\mathsf T}$） |
| 自由度 | 7 | 5 |
| 約束 | 秩 2（$\det F = 0$） | 奇異值 $(\sigma, \sigma, 0)$ |
| 關係 | $E = K'^{\mathsf T}FK''$ | |

### 10.3 記號提醒

本課 $F_{12}$：$\mathbf x'^{\mathsf T}F\mathbf x'' = 0$；MVG：$\mathbf x'^{\mathsf T}F\mathbf x = 0$（$\mathbf x'$ 在第二張）→ $F_{\text{MVG}} = F_{\text{本課}}^{\mathsf T}$。

$$
S_{\boldsymbol b} = \begin{bmatrix} 0 & -b_3 & b_2 \\ b_3 & 0 & -b_1 \\ -b_2 & b_1 & 0 \end{bmatrix}, \quad \boldsymbol b \times \boldsymbol x = S_{\boldsymbol b}\boldsymbol x, \quad S^{\mathsf T} = -S
$$

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 共面約束、對極平面 | 2-35 對極幾何（極點、對極線） |
| 從點對應估 $F$、$E$ | 2-37 八點演算法、從 $E$ 拆出 $R, \boldsymbol b$ |
| 相對定向 = 視覺里程計 | 2-22（五點演算法 + RANSAC） |
| 絕對定向需 3 個點 | 2-31 P3P 的類比 |

---

## 附：本集一句話總結

> **不知道場景時，兩張影像只能定出相對定向：已校正 12 − 7 = 5 個參數（旋轉＋基線方向，缺尺度），未校正 22 − 15 = 7 個。兩條射線和基線共面（純量三重積為零）給出 $\mathbf x'^{\mathsf T}F\mathbf x'' = 0$，$F = K'^{-\mathsf T}R'S_{\boldsymbol b}R''^{\mathsf T}K''^{-1}$；已校正時變成本質矩陣 $E = R'S_{\boldsymbol b}R''^{\mathsf T}$（5 自由度）。注意 MVG 的 $F$ 是本課的轉置。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Relative Orientation, Fundamental and Essential Matrix 錄影逐字稿（Whisper `medium.en`，59:50）、MVG 第 9 章與《視覺 SLAM 十四講》§7.3 整理。*
