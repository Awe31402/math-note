---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 32
lecture: Lecture 11 (Part 2) – Two-view and multi-view stereo
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/N_iECTqZtQQ
notes: 校正部分可對照 MVG §11.12（書頁 302–308，PDF 頁 320–326）；匹配代價 MVG 沒有，只依逐字稿
---

# 第 32 集 · Lecture 11 (Part 2)：校正 homography 的推導、匹配代價（NCC、SSD、SAD、互資訊） [▶ 影片](https://youtu.be/N_iECTqZtQQ)

← 上一集：[31-stereo-part1](31-stereo-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[33-stereo-part3](33-stereo-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 32 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（25:44，Whisper `medium.en` 轉錄）
> **標記說明**：
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 校正 homography 的推導](#1-校正-homography-的推導)
  - [1.1 設定](#11-設定)
  - [1.2 兩個極點](#12-兩個極點)
  - [1.3 左圖的 H：一個旋轉](#13-左圖的-h一個旋轉)
  - [1.4 右圖的 H'](#14-右圖的-h)
  - [1.5 實際套用：反向映射](#15-實際套用反向映射)
- [2. 沿掃描線找對應](#2-沿掃描線找對應)
- [3. 匹配代價](#3-匹配代價)
  - [3.1 NCC](#31-ncc)
  - [3.2 SSD](#32-ssd)
  - [3.3 正規化 SSD = 1 − NCC](#33-正規化-ssd--1--ncc)
  - [3.4 SAD](#34-sad)
  - [3.5 互資訊](#35-互資訊)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

1. 接上一集：具體構造把極點送到 $(1,0,0)^\mathsf{T}$ 的 $H$、$H'$。
2. 校正後沿掃描線比對 patch，介紹四種**匹配代價（matching cost）**。

---

## 1. 校正 homography 的推導

### 1.1 設定

[▶ 00:00](https://youtu.be/N_iECTqZtQQ?t=0)

- 3D 點 $\mathbf{P}$ 投到左、右圖的 $\mathbf{p}$、$\mathbf{p}'$。
- 光心 $\mathbf{o}$、$\mathbf{o}'$（MVG 記作 $\tilde{\mathbf{C}}$、$\tilde{\mathbf{C}}'$，非齊次 $3\times1$）。
- 相機矩陣：左相機放在標準座標系，右相機相對它轉 $R$、移 $\mathbf{t}$：
$$
M=K\left[I\mid\mathbf{0}\right],\qquad M'=K'\left[R\mid\mathbf{t}\right]
$$

### 1.2 兩個極點

[▶ 01:19](https://youtu.be/N_iECTqZtQQ?t=79)

**左圖極點** = 右相機光心投到左圖。右光心在左相機座標下是 $\mathbf{o}'=-R^\mathsf{T}\mathbf{t}$：

$$
\mathbf{e}=M\begin{pmatrix}\mathbf{o}'\\1\end{pmatrix}=K\left[I\mid\mathbf{0}\right]\begin{pmatrix}\mathbf{o}'\\1\end{pmatrix}=K\mathbf{o}'
$$

- 「相機正規化」的極點（拿掉 $K$）：$\hat{\mathbf{e}}=\mathbf{o}'$。

**右圖極點** = 左光心（原點）投到右圖：

$$
\mathbf{e}'=M'\begin{pmatrix}\mathbf{0}\\1\end{pmatrix}=K'\left[R\mid\mathbf{t}\right]\begin{pmatrix}\mathbf{0}\\1\end{pmatrix}=K'\mathbf{t}
$$

- 正規化：$\hat{\mathbf{e}}'=\mathbf{t}$。

⚠️ 逐字稿缺字 [▶ 03:14](https://youtu.be/N_iECTqZtQQ?t=194)：Whisper 把左光心也寫成「o'」，依上下文是 $\mathbf{o}$（原點）。

### 1.3 左圖的 H：一個旋轉

[▶ 03:53](https://youtu.be/N_iECTqZtQQ?t=233)

要找 $H$ 使 $H\hat{\mathbf{e}}\propto(1,0,0)^\mathsf{T}$。

- $(1,0,0)$：$x$ 分量非零、$y$ 分量 0 → 兩個極點在同一條掃描線方向上，極線對齊。
- **用旋轉矩陣當 $H$**：第 8 集講過，homography 存在於「場景是平面」或「相機純旋轉」兩種情況。純旋轉 → 可以選 $H$ 是正交矩陣（旋轉）：
$$
H=\begin{pmatrix}\mathbf{r}_1^\mathsf{T}\\\mathbf{r}_2^\mathsf{T}\\\mathbf{r}_3^\mathsf{T}\end{pmatrix}
$$

**三列怎麼選** [▶ 05:05](https://youtu.be/N_iECTqZtQQ?t=305)：

1. **第一列**：極點方向的單位向量
$$
\mathbf{r}_1=\frac{\mathbf{o}'}{\|\mathbf{o}'\|}
$$
   → $H\mathbf{o}'$ 的第一個分量是 $\mathbf{r}_1^\mathsf{T}\mathbf{o}'=\|\mathbf{o}'\|$。
2. **第二列**：任一個和 $\mathbf{r}_1$ 正交的單位向量（旋轉矩陣任兩列正交）。
3. **第三列**：和前兩列都正交 → 外積
$$
\mathbf{r}_3=\mathbf{r}_1\times\mathbf{r}_2
$$

**為什麼這樣就把極點送到 $(1,0,0)$**：$\mathbf{r}_2$、$\mathbf{r}_3$ 都和 $\mathbf{r}_1$（也就是 $\mathbf{o}'$ 的方向）正交，所以

$$
H\mathbf{o}'=\begin{pmatrix}\mathbf{r}_1^\mathsf{T}\mathbf{o}'\\\mathbf{r}_2^\mathsf{T}\mathbf{o}'\\\mathbf{r}_3^\mathsf{T}\mathbf{o}'\end{pmatrix}=\begin{pmatrix}\|\mathbf{o}'\|\\0\\0\end{pmatrix}\propto\begin{pmatrix}1\\0\\0\end{pmatrix}
$$

（齊次座標差一個倍數 $\|\mathbf{o}'\|$ 沒關係；逐字稿說「等於 1」是指正規化之後。）

⚠️ 待確認 [▶ 05:44](https://youtu.be/N_iECTqZtQQ?t=344)：講者說 $\mathbf{r}_2$ 有「一個好選擇」，指著投影片上的式子，但沒唸出來。

> 以下**不是逐字稿內容**，是一個能滿足條件的選法（常見於 stereo 校正的教材）：若 $\mathbf{o}'=(o_x,o_y,o_z)^\mathsf{T}$，取
> $$
> \mathbf{r}_2=\frac{1}{\sqrt{o_x^2+o_y^2}}\begin{pmatrix}-o_y\\o_x\\0\end{pmatrix}
> $$
> 驗算：$\mathbf{r}_1^\mathsf{T}\mathbf{r}_2\propto-o_xo_y+o_yo_x+0=0$。它沒有 $z$ 分量，等於讓新的 $y$ 軸留在原影像平面內，扭曲較小。投影片實際的式子待查。

### 1.4 右圖的 H'

[▶ 07:21](https://youtu.be/N_iECTqZtQQ?t=441)

$$
H'=HR^\mathsf{T}
$$

講者留作練習：驗證 $H\hat{\mathbf{e}}\propto(1,0,0)^\mathsf{T}$ 且 $H'\hat{\mathbf{e}}'\propto(1,0,0)^\mathsf{T}$。

> 以下**不是逐字稿內容**，是這個練習的驗算：
> $$
> H'\hat{\mathbf{e}}'=HR^\mathsf{T}\mathbf{t}=H\left(-\mathbf{o}'\right)=-\begin{pmatrix}\|\mathbf{o}'\|\\0\\0\end{pmatrix}\propto\begin{pmatrix}1\\0\\0\end{pmatrix}
> $$
> 用到 $\mathbf{o}'=-R^\mathsf{T}\mathbf{t}$，所以 $R^\mathsf{T}\mathbf{t}=-\mathbf{o}'$。
>
> 直覺：$R^\mathsf{T}$ 先把右相機轉回和左相機同一個方向，再套用和左圖一樣的 $H$——兩台相機最後朝向完全一樣，只差沿新 $x$ 軸的平移，就是上一集的平行情況。

> 以下**不是逐字稿內容**，是補充：$H$、$H'$ 作用在**正規化座標**（$K^{-1}\mathbf{x}$）上。直接作用在像素上時要寫成 $K_{\text{new}}HK^{-1}$、$K_{\text{new}}H'K'^{-1}$，其中 $K_{\text{new}}$ 是兩張校正影像共用的內參。

### 1.5 實際套用：反向映射

[▶ 08:36](https://youtu.be/N_iECTqZtQQ?t=516)

- 直覺做法：對原圖每個像素算 $H\mathbf{x}$，放到校正影像 → 校正影像會有**洞**（第 8 集講過）。
- **實際做法**：對**校正影像**的每個像素，用 $H^{-1}$ 找到原圖的對應位置，讀那裡的 RGB 值填回來（像查表）。這樣就沒有洞。
- 右圖同樣用 $H'^{-1}$。

【課本補充】MVG §11.12：MVG 用另一種方法——先讓 $H'$ 在影像中心附近接近剛體變換，再找一個「匹配」的 $H$ 讓兩張圖對應點的水平差距（視差）的平方和最小。課堂用的是已知 $R,\mathbf{t}$ 的校準 stereo，所以可以直接用旋轉構造。

---

## 2. 沿掃描線找對應

[▶ 10:28](https://youtu.be/N_iECTqZtQQ?t=628)

校正後，任一對影像都變成平行的一對，極線在同一列。

對參考影像每個像素：

1. 取它周圍的 patch。
2. 在另一張圖的**同一列**上滑動視窗，每個位置算一個**匹配代價**。
3. 代價**最低**（外觀最相似）的位置就是對應點 $x'$。
4. 視差 $d=x-x'$。

---

## 3. 匹配代價

[▶ 12:44](https://youtu.be/N_iECTqZtQQ?t=764)

也叫**光度一致性（photo-consistency）**代價。四種：NCC、SSD、SAD、互資訊。

**記號**：參考 patch 和候選 patch（例如 $3\times3$ 視窗 $\Omega$）各拉成向量 $\mathbf{f}$、$\mathbf{g}$；$\bar f$、$\bar g$ 是平均灰階；$\sigma_f$、$\sigma_g$ 是標準差：

$$
\sigma_f=\sqrt{\frac{1}{|\Omega|}\sum_{\mathbf{x}\in\Omega}\left(f(\mathbf{x})-\bar f\right)^2}
$$

### 3.1 NCC

[▶ 13:04](https://youtu.be/N_iECTqZtQQ?t=784)

**零均值正規化互相關（zero-mean normalized cross-correlation，ZNCC，常簡稱 NCC）**：

$$
\mathrm{NCC}(\mathbf{f},\mathbf{g})=\frac{1}{|\Omega|}\sum_{\mathbf{x}\in\Omega}\frac{\left(f(\mathbf{x})-\bar f\right)\left(g(\mathbf{x})-\bar g\right)}{\sigma_f\,\sigma_g}\in[-1,1]
$$

（公式依講者對各符號的說明寫出；投影片原式沒唸。）

- **越大越像**。
- 除以兩個 patch 的標準差 → 對**增益和偏移（gain and bias）**不變 → 對光照變化不敏感。

**失敗情況** [▶ 16:26](https://youtu.be/N_iECTqZtQQ?t=986)：

- **缺乏紋理**：沿掃描線是一片均勻表面 → 代價曲線幾乎是平的，找不出明顯的最佳視差。
- **重複紋理**：會有好幾個差不多好的位置。

> 以下**不是逐字稿內容**，是補充：均勻表面還有一個數值問題——$\sigma_f$ 或 $\sigma_g$ 接近 0，NCC 的分母趨近 0，值不穩定。

### 3.2 SSD

[▶ 17:43](https://youtu.be/N_iECTqZtQQ?t=1063)

**平方差和（sum of squared differences）**：

$$
\mathrm{SSD}(\mathbf{f},\mathbf{g})=\|\mathbf{f}-\mathbf{g}\|^2
$$

- **越小越像**。
- 沒有上界（NCC 被限制在 $[-1,1]$）。可以用指數函數映射到 $(0,1]$：
$$
\exp\left(-\frac{\|\mathbf{f}-\mathbf{g}\|^2}{\sigma^2}\right)
$$
  類似高斯；$\sigma$ 是超參數。（分母寫 $\sigma^2$ 或 $2\sigma^2$ 只差一個常數，逐字稿沒唸出投影片的確切形式。）

**缺點** [▶ 19:28](https://youtu.be/N_iECTqZtQQ?t=1168)：對**離群值**（outlier）**非常敏感**。

- 代價隨差距**平方**成長。一個像素錯得很離譜，就會讓整個代價變得非常大，壓過其他像素。

### 3.3 正規化 SSD = 1 − NCC

[▶ 20:34](https://youtu.be/N_iECTqZtQQ?t=1234)

**正規化 SSD（NSSD）**：每個 patch 先減平均、除以標準差，再算 SSD：

$$
\mathrm{NSSD}(\mathbf{f},\mathbf{g})=\frac{1}{2|\Omega|}\sum_{\mathbf{x}\in\Omega}\left(\frac{f(\mathbf{x})-\bar f}{\sigma_f}-\frac{g(\mathbf{x})-\bar g}{\sigma_g}\right)^2
$$

- 平移到平均、按標準差縮小 → 差距有界，不會因為某些值很大就爆掉。

**和 NCC 的關係** [▶ 21:44](https://youtu.be/N_iECTqZtQQ?t=1304)：講者說代進去就得到 $1-\mathrm{NCC}$。

> 以下**不是逐字稿內容**，是推導（依上面的正規化寫法；投影片的常數可能不同）：令 $\tilde f=(f-\bar f)/\sigma_f$、$\tilde g=(g-\bar g)/\sigma_g$。由 $\sigma_f$ 的定義，$\sum_\Omega\tilde f^2=|\Omega|$，同理 $\sum_\Omega\tilde g^2=|\Omega|$；又 $\sum_\Omega\tilde f\tilde g=|\Omega|\cdot\mathrm{NCC}$。所以
> $$
> \sum_\Omega\left(\tilde f-\tilde g\right)^2=\sum\tilde f^2-2\sum\tilde f\tilde g+\sum\tilde g^2=2|\Omega|\left(1-\mathrm{NCC}\right)
> $$
> 除以 $2|\Omega|$ 得 $\mathrm{NSSD}=1-\mathrm{NCC}\in[0,2]$。

- 本質上就是 NCC **反過來**：NCC 越大越像，NSSD 越小越像。

### 3.4 SAD

[▶ 22:46](https://youtu.be/N_iECTqZtQQ?t=1366)

**絕對差和（sum of absolute differences）**：用 L1 範數取代 L2：

$$
\mathrm{SAD}(\mathbf{f},\mathbf{g})=\|\mathbf{f}-\mathbf{g}\|_1=\sum_{\mathbf{x}\in\Omega}\left|f(\mathbf{x})-g(\mathbf{x})\right|
$$

- **比 SSD 對離群值更強健**：L2 是二次曲線，差距大時懲罰暴增；L1 是 V 形，差距大時懲罰只線性成長。

### 3.5 互資訊

[▶ 24:29](https://youtu.be/N_iECTqZtQQ?t=1469)

來自資訊理論，衡量兩個隨機變數 $X$、$Y$ **有多相依**：

$$
I(X;Y)=\sum_{x}\sum_{y}p(x,y)\log\frac{p(x,y)}{p(x)\,p(y)}
$$

- $p(x,y)$：聯合機率；$p(x)$、$p(y)$：邊際機率。
- 匹配代價取**負的互資訊** $-I$：互資訊大（相依、相像）→ 代價小；代價大 → 兩個 patch 很不像。

（本集在 25:44 講到一半結束，下一集繼續。）

> 以下**不是逐字稿內容**，是補充：用在影像上時，$X$、$Y$ 是兩個 patch 對應像素的灰階，$p(x,y)$ 由聯合灰階直方圖估計。互資訊只看「灰階之間有沒有固定關係」，不要求灰階相等，所以連非線性的亮度變化也能處理。

---

## 4. 一頁速查表

### 校正

| 項目 | 公式 | 關鍵一步 |
|---|---|---|
| 相機 | $M=K[I\mid\mathbf{0}]$、$M'=K'[R\mid\mathbf{t}]$ | — |
| 極點 | $\mathbf{e}=K\mathbf{o}'$、$\mathbf{e}'=K'\mathbf{t}$；正規化 $\hat{\mathbf{e}}=\mathbf{o}'=-R^\mathsf{T}\mathbf{t}$、$\hat{\mathbf{e}}'=\mathbf{t}$ | 對方的光心投影過來 |
| $H$ | 旋轉，$\mathbf{r}_1=\mathbf{o}'/\|\mathbf{o}'\|$、$\mathbf{r}_2\perp\mathbf{r}_1$、$\mathbf{r}_3=\mathbf{r}_1\times\mathbf{r}_2$ | $\mathbf{r}_{2,3}\perp\mathbf{o}'$ → $H\mathbf{o}'\propto(1,0,0)^\mathsf{T}$ |
| $H'$ | $HR^\mathsf{T}$ | $R^\mathsf{T}\mathbf{t}=-\mathbf{o}'$ |
| 重新取樣 | 校正影像每像素用 $H^{-1}$ 回原圖讀值 | 避免洞 |

### 匹配代價

| 代價 | 公式 | 越 ○ 越像 | 特性 |
|---|---|---|---|
| NCC | $\frac{1}{|\Omega|}\sum\frac{(f-\bar f)(g-\bar g)}{\sigma_f\sigma_g}\in[-1,1]$ | 大 | 對增益、偏移不變；怕無紋理、重複紋理 |
| SSD | $\|\mathbf{f}-\mathbf{g}\|^2$（可映成 $e^{-\|\cdot\|^2/\sigma^2}$） | 小 | 無上界；怕離群值 |
| NSSD | $=1-\mathrm{NCC}$ | 小 | 先標準化再 SSD |
| SAD | $\|\mathbf{f}-\mathbf{g}\|_1$ | 小 | 比 SSD 強健 |
| 互資訊 | $-\sum p(x,y)\log\frac{p(x,y)}{p(x)p(y)}$ | 小 | 衡量相依程度 |

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 互資訊 | 第 33 集（講完互資訊；SGM 常用它當匹配代價） |
| 只靠局部 patch 會在無紋理處失敗 | 第 33 集（掃描線最佳化、SGM 加平滑項） |
| 匹配代價 | 第 34 集（平面掃描的光度一致性） |

---

## 附：本集一句話總結

> **校準過的 stereo 可以直接構造校正 homography：左圖的 $H$ 是一個旋轉，第一列取極點方向 $\mathbf{o}'/\|\mathbf{o}'\|$、其餘兩列和它正交，於是極點被送到 $(1,0,0)$；右圖用 $H'=HR^\mathsf{T}$，套用時以 $H^{-1}$ 反向取樣避免洞；校正後沿掃描線比對 patch，代價可以用 NCC（對光照不變、怕無紋理）、SSD（怕離群值）、NSSD（$=1-\mathrm{NCC}$）、SAD（較強健）或負的互資訊。**

---

## ⚠️ 待確認清單

1. [▶ 05:44](https://youtu.be/N_iECTqZtQQ?t=344) 投影片上 $\mathbf{r}_2$ 的確切式子：講者沒唸出來，筆記用的是一個常見的選法 $(-o_y,o_x,0)^\mathsf{T}/\sqrt{o_x^2+o_y^2}$。

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 11 (Part 2) 錄影逐字稿（Whisper `medium.en`，25:44）整理；校正部分對照 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §11.12。*
