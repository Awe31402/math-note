---
course: Mobile Sensing and Robotics 2（Uni Bonn, Summer 2021）
episode: 2-24
lecture: Camera Parameters – Extrinsics and Intrinsics
date: 待補（2021 夏季學期）
video: https://youtu.be/uHApDqH-8UE
notes: MVG 第 6 章 §6.1（書頁 153–158，PDF 頁 171–176）；《視覺 SLAM 十四講》第 2 版 §5.1（書頁 97–102，PDF 頁 120–125）
---

# 第 2-24 集 · 相機參數：外參與內參 [▶ 影片](https://youtu.be/uHApDqH-8UE)

← 上一集：[2-22-ransac](2-22-ransac.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[2-27-dlt](2-27-dlt.md) →

> **課程**：Mobile Sensing and Robotics 2，Uni Bonn，2021 夏季學期 — 第 2-24 集
> **講者**：Cyrill Stachniss
> **來源**：YouTube 錄影逐字稿（1:15:25，Whisper `medium.en` 轉錄）＋ MVG §6.1 ＋《視覺 SLAM 十四講》§5.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `【十四講補充】` 十四講有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 四個座標系](#1-四個座標系)
- [2. 外參與內參](#2-外參與內參)
- [3. 外參：剛體轉換](#3-外參剛體轉換)
- [4. 理想透視投影](#4-理想透視投影)
- [5. 校正矩陣與共線方程](#5-校正矩陣與共線方程)
- [6. 影像平面到感測器：仿射轉換](#6-影像平面到感測器仿射轉換)
- [7. DLT 與 11 個參數](#7-dlt-與-11-個參數)
- [8. 非線性誤差](#8-非線性誤差)
- [9. 反向映射：像素到 3D 射線](#9-反向映射像素到-3d-射線)
- [10. 相機的分類](#10-相機的分類)
- [11. 總結](#11-總結)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

描述 3D 世界點怎麼映射到 2D 像素：

$$
{}^{s}\mathbf{x} = P\,\mathbf{X}
$$

- $\mathbf{X}$：3D 點的齊次座標（4 維）；${}^{s}\mathbf{x}$：像素的齊次座標（3 維）；$P$：$3 \times 4$ 投影矩陣。
- 目標：了解 $P$ 裡有什麼、各參數描述什麼物理性質。只要牽涉相機幾何（估計相機在哪、或 3D 點在哪），這個式子遲早會出現。

---

## 1. 四個座標系

[▶ 02:30](https://youtu.be/uHApDqH-8UE?t=150)

| 符號 | 座標系 | 說明 |
|---|---|---|
| $S_o$ | 世界／物體 | 外部給定的座標系（沒有左上標時就是這個） |
| $S_k$ | 相機 | 原點在**投影中心** |
| $S_c$ | 影像平面 | 和相機座標系只差沿 $z$ 方向一個常數 |
| $S_s$ | 感測器 | 晶片上像素 (0, 0) 的位置，通常在角落 |

- 記號：左上標 = 點在哪個座標系表示；轉換矩陣左上標是「到」、右下標是「從」。串接時相鄰的字母要相同，不同就是寫錯了：

$$
{}^{s}\mathbf{x} = {}^{s}H_{c}\ {}^{c}P_{k}\ {}^{k}H_{o}\ \mathbf{X}
$$

**幾何** [▶ 05:26](https://youtu.be/uHApDqH-8UE?t=326)：

- 相機座標系原點 = 投影中心；影像平面離投影中心的距離 = **相機常數** $c$。
- 相機座標系和影像平面的 $x$、$y$ 軸相同，只沿 $z$ 平移 $c$：影像平面原點在相機座標系中是 $(0, 0, c)$（通常是負的位移）。
- 影像平面的 (0, 0) 通常在光軸上；感測器的 (0, 0) 不同。最後要的是感測器座標，因為那才是影像回傳的像素。

---

## 2. 外參與內參

[▶ 07:46](https://youtu.be/uHApDqH-8UE?t=466)

| 步驟 | 從 → 到 | 維度 | 性質 |
|---|---|---|---|
| 1 | 物體 → 相機 | 3D → 3D | 剛體轉換，**外參** |
| 2 | 相機 → 影像平面 | 3D → 2D | 理想投影，**失去深度**（單張影像缺深度資訊的原因） |
| 3 | 影像平面 → 感測器 | 2D → 2D | 仿射轉換（線性模型到此為止） |
| 4 | 感測器內 | 2D → 2D | **非線性**誤差補償（例如透鏡畸變） |

- 非線性誤差實際上發生在光線經過透鏡、投影到影像平面時，但習慣在最後感測器座標系加一個轉換來補償。
- **外參**（extrinsics）：相機外面的事：相機在哪、怎麼轉。相機移動就改變。
- **內參**（intrinsics）：相機裡面的事：例如感測器裝在投影中心後面的哪裡。步驟 2～4 都算內參。
- 校正好的相機，拿著走來走去，內參不變、外參一直變 → 分開很合理；校正後，狀態估計大多只需要處理外參。

---

## 3. 外參：剛體轉換

[▶ 11:29](https://youtu.be/uHApDqH-8UE?t=689)

- 相機只能平移和旋轉（不能扭曲或縮放世界）→ **剛體轉換**：3 個平移＋3 個旋轉（例如偏航、俯仰、滾轉）= **6 個外參**。可逆。
- 記號：點 $\boldsymbol{X}_P = (X_P, Y_P, Z_P)^{\mathsf T}$；投影中心 $\boldsymbol{X}_O$（有些書寫 $\boldsymbol{Z}$ 或 $\boldsymbol{Z}_O$）。投影中心 = 針孔模型中所有光線通過的那一點。
- 字體慣例：斜體 = 歐氏座標；正體 = 齊次座標。

**歐氏座標** [▶ 14:23](https://youtu.be/uHApDqH-8UE?t=863)：先減掉相機位置，再旋轉：

$$
{}^{k}\boldsymbol{X}_P = R\,(\boldsymbol{X}_P - \boldsymbol{X}_O)
$$

**齊次座標**：

$$
{}^{k}\mathbf{X}_P =
\begin{bmatrix} R & \mathbf{0} \\ \mathbf{0}^{\mathsf T} & 1 \end{bmatrix}
\begin{bmatrix} I_3 & -\boldsymbol{X}_O \\ \mathbf{0}^{\mathsf T} & 1 \end{bmatrix}
\begin{bmatrix} \boldsymbol{X}_P \\ 1 \end{bmatrix}
= \begin{bmatrix} R & -R\boldsymbol{X}_O \\ \mathbf{0}^{\mathsf T} & 1 \end{bmatrix} \mathbf{X}_P
= {}^{k}H\,\mathbf{X}_P
$$

【課本補充】MVG §6.1 式 (6.6)：$\tilde X_{\text{cam}} = R(\tilde X - \tilde C)$，齊次形式 $\begin{bmatrix} R & -R\tilde C \\ 0 & 1 \end{bmatrix}$——同一件事，MVG 把投影中心記為 $\tilde C$。也可以不寫出相機中心，寫成 $X_{\text{cam}} = RX + t$，$t = -R\tilde C$（式 6.8）。

---

## 4. 理想透視投影

[▶ 17:32](https://youtu.be/uHApDqH-8UE?t=1052)

- 3D → 2D，**不可逆**（失去深度這一個自由度）。之後的影像平面 → 感測器、感測器內的轉換都可逆。
- 內參三步驟：(1) 理想透視投影到影像平面；(2) 映到感測器座標（晶片的像素 (0, 0) 通常在角落）；(3) 感測器內的非線性補償。

**理想投影的假設** [▶ 20:15](https://youtu.be/uHApDqH-8UE?t=1215)：

- 透鏡無畸變（現實不是）。
- 所有光線都是直線、通過投影中心（完美針孔；現實的針孔不是無限小）。這一點定義相機座標系原點。
- 焦點和主點都在光軸上；光軸垂直穿過主點。
- 投影中心到影像平面的距離處處相同 = 相機常數 $c$。

**影像平面放前面** [▶ 21:56](https://youtu.be/uHApDqH-8UE?t=1316)：

- 物理模型：影像平面在投影中心**後面**，影像上下顛倒，$z$ 軸朝後，$c > 0$。
- 電腦視覺常用：把影像平面轉 180° 放到**前面**，影像正立；不符合物理，但好視覺化。兩者等價。這時 $c$ 是**負的**。本課用這個模型。

**截線定理**（相似三角形）[▶ 24:02](https://youtu.be/uHApDqH-8UE?t=1442)：

$$
{}^{c}x_P = c\,\frac{{}^{k}X_P}{{}^{k}Z_P}, \qquad
{}^{c}y_P = c\,\frac{{}^{k}Y_P}{{}^{k}Z_P}, \qquad
{}^{c}z_P = c
$$

**齊次形式** [▶ 26:18](https://youtu.be/uHApDqH-8UE?t=1578)：

$$
{}^{c}\mathbf{x}_P = \begin{bmatrix} c & 0 & 0 & 0 \\ 0 & c & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}
\begin{bmatrix} {}^{k}X_P \\ {}^{k}Y_P \\ {}^{k}Z_P \\ 1 \end{bmatrix}
= {}^{c}P_k\ {}^{k}\mathbf{X}_P
$$

**驗證** [▶ 27:41](https://youtu.be/uHApDqH-8UE?t=1661)：相乘得 $(c\,{}^kX_P,\ c\,{}^kY_P,\ {}^kZ_P)$；齊次轉歐氏要除以最後一個分量 ${}^kZ_P$ → $(c\,X/Z,\ c\,Y/Z)$，正好是截線定理的結果。

【十四講補充】§5.1.1（書頁 97–99）：相機座標 $O\text{-}x\text{-}y\text{-}z$，$z$ 朝前、$x$ 朝右、$y$ 朝下。真實成像 $\tfrac{Z}{f} = -\tfrac{X}{X'} = -\tfrac{Y}{Y'}$（負號 = 倒像，式 5.1）；把成像平面對稱放到前面，去掉負號：$X' = f\tfrac{X}{Z}$、$Y' = f\tfrac{Y}{Z}$（式 5.3）。大多數相機輸出的影像已被軟體翻正，所以這樣處理沒有壞處。

---

## 5. 校正矩陣與共線方程

[▶ 30:31](https://youtu.be/uHApDqH-8UE?t=1831)

外參和投影都是齊次矩陣 → 直接相乘，得到從世界到影像平面的投影矩陣。

- 把所有**內參**放進一個 $3 \times 3$ 的**校正矩陣**（calibration matrix）$K$。
- **理想相機**：

$$
K = \begin{bmatrix} c & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

- 記號 $[A \mid b]$：左邊 $3 \times 3$ 矩陣、右邊一欄 3 維向量，合成 $3 \times 4$。整個映射寫成一行：

$$
\mathbf{x} = K\,R\,[\,I_3 \mid -\boldsymbol{X}_O\,]\,\mathbf{X}
$$

$K$ = 內參；$R$ 和 $\boldsymbol{X}_O$ = 外參；$[\cdot \mid \cdot]$ 也表達了 3D → 2D 的投影。

**共線方程**（collinearity equations）[▶ 34:16](https://youtu.be/uHApDqH-8UE?t=2056)：把所有運算展開、正規化，寫回歐氏座標。講者只展示投影片、沒有念出式子；以下不是逐字稿內容，是依 $K = \operatorname{diag}(c, c, 1)$ 和上式展開的（$\boldsymbol r_i^{\mathsf T}$ 是 $R$ 的第 $i$ 列）：

$$
x = c\,\frac{\boldsymbol r_1^{\mathsf T}(\boldsymbol X - \boldsymbol X_O)}{\boldsymbol r_3^{\mathsf T}(\boldsymbol X - \boldsymbol X_O)}, \qquad
y = c\,\frac{\boldsymbol r_2^{\mathsf T}(\boldsymbol X - \boldsymbol X_O)}{\boldsymbol r_3^{\mathsf T}(\boldsymbol X - \boldsymbol X_O)}
$$

- 【口頭】歐氏座標寫起來醜得多；用齊次座標好寫，也比較不會出錯 [▶ 34:46](https://youtu.be/uHApDqH-8UE?t=2086)。

---

## 6. 影像平面到感測器：仿射轉換

[▶ 35:10](https://youtu.be/uHApDqH-8UE?t=2110)

三件事：

| 參數 | 意義 |
|---|---|
| **主點** $(x_H, y_H)$ | 光軸穿過影像平面的點（影像平面座標 (0, 0)）對應到晶片上哪個像素；只是平面內的平移 |
| **尺度差** $m$ | 晶片的 $x$、$y$ 方向尺度可能不同（取決於晶片和線路設計）；$x$ 尺度定為 1，$y$ 為 $1 + m$。理想是 0，實際略大或略小 |
| **剪切** $s$ | 傳統上補償剪切；類比底片才有，今天數位相機通常 $\approx 0$ |

$$
{}^{s}H_{c} = \begin{bmatrix} 1 & s & x_H \\ 0 & 1 + m & y_H \\ 0 & 0 & 1 \end{bmatrix}
$$

- 多了 4 個參數：尺度差、剪切、主點 $x$、主點 $y$。

**新的校正矩陣** [▶ 39:00](https://youtu.be/uHApDqH-8UE?t=2340)：$K = {}^{s}H_{c}\,\operatorname{diag}(c, c, 1)$：

$$
\boxed{\;K = \begin{bmatrix} c & c\,s & x_H \\ 0 & c\,(1 + m) & y_H \\ 0 & 0 & 1 \end{bmatrix}\;}
$$

（矩陣乘出來的形式是筆記補算；講者口述「相機常數 $c$ 填進這三個位置，$s$ 通常還是 0」。）

- **5 個內參**：相機常數 $c$、剪切 $s$、尺度差 $m$、主點 $x_H$、$y_H$。這是傳統上不含非線性誤差的五個參數，對應**仿射**轉換。
- 有些書寫兩個相機常數（或焦距）$c_x$、$c_y$：$c_x = c$、$c_y = c + cm$，直接對應。

【課本補充】MVG §6.1 式 (6.9)、(6.10)（書頁 157）：

$$
K = \begin{bmatrix} \alpha_x & s & x_0 \\ 0 & \alpha_y & y_0 \\ 0 & 0 & 1 \end{bmatrix}
$$

- $\alpha_x = f m_x$、$\alpha_y = f m_y$：以像素為單位的焦距（$m_x, m_y$ 是每單位長度的像素數，非正方形像素時不同）；$(x_0, y_0)$ 是像素單位的主點。$s$ 是 skew，一般相機為 0。
- 和講者記號的對應：$\alpha_x \leftrightarrow c$、$\alpha_y \leftrightarrow c(1 + m)$、$s_{\text{MVG}} \leftrightarrow c\,s$、$(x_0, y_0) \leftrightarrow (x_H, y_H)$。

【十四講補充】§5.1.1（書頁 98–99）：像素座標系 $o\text{-}u\text{-}v$，原點在左上角，$u$ 朝右、$v$ 朝下。和成像平面差一個縮放（$u$ 軸 $\alpha$ 倍、$v$ 軸 $\beta$ 倍）和原點平移 $[c_x, c_y]$；令 $f_x = \alpha f$、$f_y = \beta f$（單位像素）：

$$
Z\begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = KP \qquad (5.7)
$$

（沒有剪切。）內參通常出廠後固定；需要自己確定時叫**標定**（例如張正友的單目棋盤格標定法，見 2-29）。

---

## 7. DLT 與 11 個參數

[▶ 40:28](https://youtu.be/uHApDqH-8UE?t=2428)

- 這個轉換（6 個外參 ＋ 5 個內參）叫 **DLT**（direct linear transform，直接線性轉換）。
- 【口頭】注意 DLT 在攝影測量裡有**兩個意思**：(1) 描述這個轉換本身；(2) 估計這 11 個參數的方法（2-27）[▶ 40:45](https://youtu.be/uHApDqH-8UE?t=2445)。
- 這是**仿射相機**的模型：世界到感測器 = 仿射轉換 ＋ 投影；不含非線性透鏡誤差。

$$
\mathbf{x} = P\,\mathbf{X}, \qquad P = K\,R\,[\,I_3 \mid -\boldsymbol{X}_O\,]
$$

| 部分 | 參數數 |
|---|---|
| $K$ | 5 |
| $R$ | 3 |
| $\boldsymbol{X}_O$ | 3 |
| 合計 | **11** |

歐氏形式（$p_{11}, \dots, p_{34}$ 是 $P$ 的 12 個元素）：

$$
x = \frac{p_{11}X + p_{12}Y + p_{13}Z + p_{14}}{p_{31}X + p_{32}Y + p_{33}Z + p_{34}}, \qquad
y = \frac{p_{21}X + p_{22}Y + p_{23}Z + p_{24}}{p_{31}X + p_{32}Y + p_{33}Z + p_{34}}
$$

（式子依「$\mathbf x = P\mathbf X$ 除以第三分量」寫出；講者只說「這是歐氏參數的結果式」。）

**12 個元素、11 個參數？** [▶ 42:41](https://youtu.be/uHApDqH-8UE?t=2561)：$P$ 是**齊次**矩陣，只定義到一個比例因子：乘上任何非零純量都是同一個轉換 → 少一個自由度。

【課本補充】MVG §6.1（書頁 157）：$K$ 為 (6.10) 形式的 $P = KR[I \mid -\tilde C]$ 叫**有限射影相機**，11 個自由度，等於 $3 \times 4$ 齊次矩陣的自由度。左邊 $3 \times 3$ 子矩陣 $M = KR$ 非奇異；反過來，任何左 $3 \times 3$ 非奇異的 $3 \times 4$ 矩陣都能用 **RQ 分解** $M = KR$（$K$ 上三角、$R$ 旋轉）拆成這個形式，$P = M[I \mid M^{-1}p_4]$。自由度的層次：基本針孔 $P = KR[I \mid -\tilde C]$ 有 9 個（$K$ 只有 $f, p_x, p_y$）；CCD（非正方形像素）10 個；加 skew 11 個。MVG 表 6.1：相機中心是 $P$ 的右零空間（$PC = 0$），有限相機 $C = (-M^{-1}p_4, 1)^{\mathsf T}$。

---

## 8. 非線性誤差

[▶ 43:53](https://youtu.be/uHApDqH-8UE?t=2633)

- 非線性誤差其實發生在整條 $k \to s$ 的路上；但約定：投影和仿射保持線性，非線性部分全部放在感測器座標系內的一個映射補償。
- 原因：**透鏡畸變**（例如廣角鏡頭的**桶形畸變**：直線看起來像桶子）、感測器不平、製造不完美……
- 【口頭】講者說透鏡品質過去 40、50 年甚至變差了（以前的鏡頭品質更高），所以補償非線性誤差更重要 [▶ 45:22](https://youtu.be/uHApDqH-8UE?t=2722)。

**位置相依的位移** [▶ 45:48](https://youtu.be/uHApDqH-8UE?t=2748)：

$$
{}^{a}\boldsymbol{x} = {}^{s}\boldsymbol{x} + \Delta\boldsymbol{x}({}^{s}\boldsymbol{x}, \boldsymbol{q})
$$

- 每個像素依它在影像中的位置，各自移一點（$\boldsymbol q$ 是非線性參數）。例：桶形畸變把直線往外彎 → 補償時把點往內移。
- 理論上每個位置都不同；通常假設平滑變化，或用參數形式表示。
- 例：普通網路攝影機拍的鍵盤，實際是直線的邊在影像中是彎的（不保直線）；校正內參（含非線性）後可以把影像修正成直線（邊緣的內容被往內移）。

**齊次形式**：

$$
{}^{a}H_{s} = \begin{bmatrix} 1 & 0 & \Delta x(\boldsymbol x, \boldsymbol q) \\ 0 & 1 & \Delta y(\boldsymbol x, \boldsymbol q) \\ 0 & 0 & 1 \end{bmatrix}, \qquad
{}^{a}K = {}^{a}H_{s}\,K = \begin{bmatrix} c & c\,s & x_H + \Delta x \\ 0 & c\,(1 + m) & y_H + \Delta y \\ 0 & 0 & 1 \end{bmatrix}
$$

只有主點那一欄多了位置相依的位移。

**怎麼建模 $\Delta x, \Delta y$** [▶ 50:16](https://youtu.be/uHApDqH-8UE?t=3016)：

| 類型 | 做法 | 優缺點 |
|---|---|---|
| **物理模型** | 用數學描述各種物理效應，取物理模型的參數 | 有助了解問題在哪；但原因很多、難以描述、參數難取得 → 越來越少用 |
| **現象模型** | 假設一個模型，擬合參數讓影像最好 | 好做、今天很流行；但不會告訴你問題出在哪 |

**桶形畸變模型** [▶ 51:49](https://youtu.be/uHApDqH-8UE?t=3109)：

$$
x' = x\,(1 + q_1 r^2 + q_2 r^4), \qquad
y' = y\,(1 + q_1 r^2 + q_2 r^4)
$$

（講者口述「從原座標開始，加上依 $r$ 的二次項和四次項，係數 $q_1, q_2$」；寫成乘積形式是依口述整理。）

- $r$：主點到像素的距離。在主點 $r = 0$，沒有位移；越往外位移越大。
- 只有 $q_1, q_2$ 兩個參數。圖：中心沒有畸變，越往外越強；反過來移動像素就能去畸變。
- 也可以用其他畸變模型；模型越複雜越難：有些參數彼此補償或加強同一個效應，估計不容易。

**實務：兩步** [▶ 54:14](https://youtu.be/uHApDqH-8UE?t=3254)：

1. 線性：$\mathbf{x} = P\mathbf{X}$ 得到感測器座標（忽略非線性）——對所有像素相同。
2. 非線性：逐點修正像素位置——每個像素不同。

【十四講補充】§5.1.2（書頁 100–102）：在**歸一化平面**上的點 $(x, y)$、$r^2 = x^2 + y^2$：

- 徑向畸變（透鏡形狀造成；桶形、枕形）：$x_{\text{d}} = x(1 + k_1 r^2 + k_2 r^4 + k_3 r^6)$，$y$ 同（式 5.10）——和講者的模型同形，多一項 $r^6$。
- 切向畸變（組裝時透鏡和成像面不嚴格平行）：$x_{\text{d}} = x + 2p_1 xy + p_2(r^2 + 2x^2)$，$y_{\text{d}} = y + p_1(r^2 + 2y^2) + 2p_2 xy$（式 5.11）。
- 合起來 5 個係數，再 $u = f_x x_{\text{d}} + c_x$、$v = f_y y_{\text{d}} + c_y$（式 5.13）；實際可只用 $k_1, p_1, p_2$。
- 去畸變有兩種：先把整張影像去畸變（視覺 SLAM 較常見），或從畸變點按方程反推。

---

## 9. 反向映射：像素到 3D 射線

[▶ 55:42](https://youtu.be/uHApDqH-8UE?t=3342)

- 做 3D 重建時，要從像素推回 3D 點。但投影失去資訊，非線性部分也麻煩 → **無法完全反推**，只能限制點在 3D 中的位置（結合多張影像才能得到點）。
- 兩步：(1) 從修正後座標回到感測器座標；(2) 從感測器座標回到 3D。

**步驟 1：反推非線性** [▶ 57:46](https://youtu.be/uHApDqH-8UE?t=3466)：

- 問題：$\Delta\boldsymbol x$ 依賴**感測器座標** ${}^s\boldsymbol x$，但手上只有修正後的 ${}^a\boldsymbol x$ → 不能直接反轉，要**迭代**：
  1. 初始猜測：用 ${}^a\boldsymbol x$ 本身代入位移函數（假設畸變不太怪）。
  2. 反轉矩陣，得到 ${}^s\boldsymbol x$ 的第一個估計。
  3. 把新估計代回位移函數（${}^a\boldsymbol x$ 保持不變），得到第二個估計……
  4. 通常很快收斂。

$$
{}^{s}\boldsymbol x^{(k+1)} = {}^{a}\boldsymbol x - \Delta\boldsymbol x\bigl( {}^{s}\boldsymbol x^{(k)}, \boldsymbol q \bigr), \qquad {}^{s}\boldsymbol x^{(0)} = {}^{a}\boldsymbol x
$$

（迭代式依口述「用目前估計算位移、反轉、重複」整理。）

- 座標通常相對**主點**表示（畸變發生在影像平面），可能要先換算。

**步驟 2：反推線性投影** [▶ 1:01:19](https://youtu.be/uHApDqH-8UE?t=3679)：

$$
\lambda\,\mathbf{x} = P\,\mathbf{X} = KR\,[\,I_3 \mid -\boldsymbol X_O\,]\begin{bmatrix} \boldsymbol X \\ 1 \end{bmatrix} = KR\,\boldsymbol X - KR\,\boldsymbol X_O
$$

（$\lambda$ 來自齊次座標的比例。）移項、左乘 $(KR)^{-1}$：

$$
\boxed{\;\boldsymbol X = \boldsymbol X_O + \lambda\,(KR)^{-1}\,\mathbf{x}\;}
$$

**解讀** [▶ 1:03:48](https://youtu.be/uHApDqH-8UE?t=3828)：

- $(KR)^{-1}\mathbf{x}$：從投影中心 $\boldsymbol X_O$ 指向 3D 點的**射線方向**。
- $\lambda$：沿射線多遠——**無法解出**。這正是 3D 投影到 2D 時失去的那一個自由度。
- 所以從像素只能知道點在哪條射線上，不知道多遠。
- 【口頭】這非常重要：校正矩陣和相機旋轉相乘、求反、乘上像素座標 → 從相機原點到 3D 點的射線方向。3D 重建會一直用到 [▶ 1:06:30](https://youtu.be/uHApDqH-8UE?t=3990)。

【課本補充】MVG §8.5（結果 8.15，書頁 208）：在相機的歐氏座標系中，影像點 $x$ 對應的射線方向是 $d = K^{-1}x$（一般不是單位向量），$K$ 就是 $x$ 和射線方向之間的（仿射）轉換。

【十四講補充】§5.1.1（書頁 100）：$(RP_w + t) = [X, Y, Z]^{\mathsf T} \to [X/Z, Y/Z, 1]^{\mathsf T}$ 是 $z = 1$ 的**歸一化平面**上的點；歸一化座標左乘 $K$ 就是像素座標。相機座標乘以任何非零常數，歸一化座標都一樣 → **深度在投影中丟失**，所以單目無法得到像素的深度。實作要檢查 $Z > 0$（負的 $Z$ 也能得到歸一化平面上的點，但相機拍不到後方的景物）。

---

## 10. 相機的分類

[▶ 1:07:29](https://youtu.be/uHApDqH-8UE?t=4049)

| 相機 | 允許的參數 | $K$ | 自由度 |
|---|---|---|---|
| **正規化相機**（normalized） | 只有平移 $X, Y, Z$；$R = I$、$c = 1$、無主點、無尺度差、無剪切、無非線性 | $I$ | 3 |
| **單位相機**（unit） | ＋ 旋轉（看不同方向），內參不變 | $I$ | 6 |
| **理想相機**（ideal） | ＋ 相機常數 $c$（$\neq 1$）；理想透視投影 | $\operatorname{diag}(c, c, 1)$ | 7 |
| **歐氏相機**（Euclidean） | ＋ 主點 $x_H, y_H$（影像平面內只有平移）；無尺度差、無剪切 | $\begin{bmatrix} c & 0 & x_H \\ 0 & c & y_H \\ 0 & 0 & 1 \end{bmatrix}$ | 9 |
| **仿射相機**（affine）＝ DLT | ＋ $m, s$；**保直線**、無非線性 | 第 6 節的 $K$ | 11 |
| **一般相機** | ＋ 非線性 $q_1, q_2, \dots$ | ${}^aK$ | 11 ＋ 非線性參數數 |

（正規化相機的自由度，講者沒有明說，依「只允許平移」推得 3；其他自由度是講者說的。）

- 世界中的直線在影像中仍是直線 ⇔ 沒有非線性誤差；直線變彎就表示有非線性誤差 [▶ 1:10:18](https://youtu.be/uHApDqH-8UE?t=4218)。

**其他術語** [▶ 1:11:35](https://youtu.be/uHApDqH-8UE?t=4295)：

- **已校正相機**（calibrated）：知道 $K$。**未校正相機**：不知道（剛買回來直接拍）。估計出 $K$ 後，把影像中的點乘上校正資訊 → 已校正。
- **量測相機**（metric camera）：專為量測設計、內參盡量不變的相機；今天不太用這個詞。
- 估計內參的過程 = **相機校正**（camera calibration），之後會講（2-29）。

---

## 11. 總結

[▶ 1:12:53](https://youtu.be/uHApDqH-8UE?t=4373)

- 描述從世界座標系到**晶片**座標系的映射：哪個 3D 點對應哪個像素。
- **外參**：相機在世界中的位置和朝向（相機外面的事）。**內參**：相機座標系到感測器座標系（相機裡面的事），可能含非線性誤差；本集的 5 個內參不含非線性。
- **DLT**：11 自由度的 $\mathbf x = P\mathbf X$。
- 非線性誤差（桶形畸變）；反向映射：像素只能定出一條射線，不知道多遠。
- 整條鏈：剛體轉換（外參）→ 中心投影（相機 → 影像平面）→ 仿射轉換（影像平面 → 感測器）→ 非線性補償。
- `⚠️ 逐字稿缺字`：Whisper 寫 “spiral distortion”，從上下文應為 **barrel distortion**（桶形畸變）。

---

## 12. 一頁速查表

### 12.1 映射鏈

$$
{}^{a}\mathbf{x} = {}^{a}H_{s}(\mathbf x)\ \underbrace{K\,R\,[\,I_3 \mid -\boldsymbol X_O\,]}_{P\ (\text{DLT, 11 參數})}\ \mathbf{X}
$$

| 步驟 | 矩陣 | 參數 |
|---|---|---|
| 世界 → 相機 | $\begin{bmatrix} R & -R\boldsymbol X_O \\ 0 & 1 \end{bmatrix}$ | 6（外參） |
| 相機 → 影像平面 | $\begin{bmatrix} c & 0 & 0 & 0 \\ 0 & c & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$ | 1（$c$） |
| 影像平面 → 感測器 | $\begin{bmatrix} 1 & s & x_H \\ 0 & 1+m & y_H \\ 0 & 0 & 1 \end{bmatrix}$ | 4 |
| 非線性 | $\begin{bmatrix} 1 & 0 & \Delta x \\ 0 & 1 & \Delta y \\ 0 & 0 & 1 \end{bmatrix}$ | $q_1, q_2, \dots$ |

### 12.2 校正矩陣

$$
K = \begin{bmatrix} c & cs & x_H \\ 0 & c(1+m) & y_H \\ 0 & 0 & 1 \end{bmatrix}
\quad\leftrightarrow\quad
K_{\text{MVG}} = \begin{bmatrix} \alpha_x & s & x_0 \\ 0 & \alpha_y & y_0 \\ 0 & 0 & 1 \end{bmatrix}
$$

### 12.3 關鍵式

| 項 | 式子 | 關鍵一步 |
|---|---|---|
| 理想投影 | $x = cX/Z$，$y = cY/Z$ | 相似三角形；齊次除以 $Z$ |
| 12 元素 11 參數 | — | 齊次矩陣只定到比例 |
| 桶形畸變 | $x' = x(1 + q_1r^2 + q_2r^4)$ | $r$ = 到主點的距離 |
| 反推非線性 | ${}^s\boldsymbol x^{(k+1)} = {}^a\boldsymbol x - \Delta\boldsymbol x({}^s\boldsymbol x^{(k)})$ | 從 ${}^a\boldsymbol x$ 起迭代 |
| 像素 → 射線 | $\boldsymbol X = \boldsymbol X_O + \lambda (KR)^{-1}\mathbf x$ | $\lambda$（深度）無法解出 |

### 12.4 相機分類

正規化（3）→ 單位（6）→ 理想（7）→ 歐氏（9）→ 仿射／DLT（11）→ 一般（11 ＋ 非線性）。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| DLT 的第二個意思：估計 11 個參數 | 2-27 DLT |
| 相機校正、內參估計 | 2-29 張正友法 |
| 已知內參求外參 | 2-29（P3P 的前提）、2-31 P3P |
| 像素 → 射線方向 $(KR)^{-1}\mathbf x$ | 2-31（射線夾角）、2-33～2-37（對極幾何） |

---

## 附：本集一句話總結

> **3D 點到像素：$\mathbf x = KR[I \mid -\boldsymbol X_O]\mathbf X$。外參 6 個（$R$、$\boldsymbol X_O$），內參 5 個（相機常數 $c$、剪切 $s$、尺度差 $m$、主點 $x_H, y_H$），合計 11 個 = DLT／仿射相機；再加位置相依的非線性修正（例如桶形畸變 $1 + q_1r^2 + q_2r^4$）。反向只能得到射線 $\boldsymbol X_O + \lambda(KR)^{-1}\mathbf x$，深度 $\lambda$ 已在投影中丟失。**

---

*筆記依據 Cyrill Stachniss「Mobile Sensing and Robotics 2」Camera Parameters 錄影逐字稿（Whisper `medium.en`，1:15:25）、MVG §6.1 與《視覺 SLAM 十四講》§5.1 整理。*
