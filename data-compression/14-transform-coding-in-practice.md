---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 14
lecture: Lecture 14
date: 2023-11-13
video: https://youtu.be/eaMrplHvxlg
notes: 投影片 L14.pdf、L14_ann.pdf；課本沒有 DCT 和音訊壓縮，本集只用到 §10.3.3 的注水結果
---

# 第 14 集 · Lecture 14：實際的轉換編碼：影像、音訊（Transform Coding in Real-Life: Image, Audio, etc.） [▶ 影片](https://youtu.be/eaMrplHvxlg)

← 上一集：[13-gaussian-rd-transform-coding](13-gaussian-rd-transform-coding.md) ｜ [總目錄](README.md) ｜ 下一集：[15-image-compression-jpeg-bpg](15-image-compression-jpeg-bpg.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 14 集
> **講者**：Pulkit Tandon（Shubham 回答一個問題時補充）
> **來源**：YouTube 錄影逐字稿（1:28:03，人工字幕 en-US；錄影在比較 MP3 前中斷）＋ 投影片 `L14.pdf`、`L14_ann.pdf`（網站上兩個檔名的標籤疑似對調，兩份都看）
> **標記說明**：
> - `【口頭】` 講者口頭補充，投影片沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 小考檢討：注水](#1-小考檢討注水)
- [2. 回顧：轉換編碼與 KLT](#2-回顧轉換編碼與-klt)
- [3. 例子：Gauss–Markov 來源的 KLT](#3-例子gaussmarkov-來源的-klt)
- [4. 轉換編碼的兩個旋鈕](#4-轉換編碼的兩個旋鈕)
- [5. 實驗：VQ vs. 轉換編碼](#5-實驗vq-vs-轉換編碼)
- [6. 為什麼實務上不用 KLT](#6-為什麼實務上不用-klt)
- [7. 實用的轉換：DCT](#7-實用的轉換dct)
- [8. DCT 的直覺：notebook 例子](#8-dct-的直覺notebook-例子)
- [9. 一個陽春的有損壓縮器：音訊](#9-一個陽春的有損壓縮器音訊)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/eaMrplHvxlg?t=5) 延續前兩講，講**實際的轉換編碼**，最後做一個很陽春的**音訊壓縮器**，動手做。

[▶ 06:27](https://youtu.be/eaMrplHvxlg?t=387) 今天：(1) 一個具體的 KLT 例子；(2) 實用的轉換 **DCT**；(3) 用目前學過的元件做一個音訊壓縮器。

---

## 1. 小考檢討：注水

[▶ 00:05](https://youtu.be/eaMrplHvxlg?t=5) 上一講的重點：**在給定失真下，變異數大的分量多給位元** [▶ 00:36](https://youtu.be/eaMrplHvxlg?t=36)。注水的精確數學（KKT）只對高斯成立，但這個直覺適用於所有實用的有損壓縮器。

小考：$\sigma_1^2=1$、$\sigma_2^2=3$，MSE [▶ 01:10](https://youtu.be/eaMrplHvxlg?t=70)。

| 題 | 答案 |
|---|---|
| $D=1.5$ 時最佳的 $D_1,D_2$ | $D_1=\sigma_1^2=1$，$D_2=2$（第 4 個選項）[▶ 01:41](https://youtu.be/eaMrplHvxlg?t=101) |
| $D=2$ 時最佳的率 | **0** [▶ 02:17](https://youtu.be/eaMrplHvxlg?t=137)：$D=\frac{\sigma_1^2+\sigma_2^2}2$，兩個分量各給到自己的變異數，都是 0 位元 |

> ⚠️ 逐字稿缺字 [▶ 01:41](https://youtu.be/eaMrplHvxlg?t=101)：講者說「D2 would be D minus D1」；本課的 $D$ 是平均失真，應為 $D_2=2D-D_1=2$，和投影片選項一致。

**哪些敘述正確** [▶ 02:50](https://youtu.be/eaMrplHvxlg?t=170)：

1. $D$ 在兩個變異數以下時，$D_1=D_2$。✓（KKT 解的結果。）
2. $D$ 在兩個變異數以下時，第一個分量的率比較低。✓ [▶ 03:28](https://youtu.be/eaMrplHvxlg?t=208)：$D_1=D_2$ 時每個分量率 $\frac12\log\frac{\sigma_i^2}D$，$\sigma_1<\sigma_2$ ⇒ $R_1<R_2$。**失真平分，但變異數大的分量仍拿到比較多位元**。
3. $D$ 在兩個變異數之間時，至少一個分量率為 0。✓

---

## 2. 回顧：轉換編碼與 KLT

[▶ 04:05](https://youtu.be/eaMrplHvxlg?t=245) 轉換編碼的兩個好處 [▶ 04:37](https://youtu.be/eaMrplHvxlg?t=277)：

1. **去相關**：之後能用簡單的量化，複雜度低。
2. **能量集中**：前幾個分量有比較多能量，變異數差很大，才能有選擇地分配位元 [▶ 05:12](https://youtu.be/eaMrplHvxlg?t=312)。

方塊圖：在原本的有損流程前加轉換 $T$，解碼後做 $T^{-1}$。

**KLT** [▶ 05:46](https://youtu.be/eaMrplHvxlg?t=346)：以特徵值為基礎的線性轉換。轉換是 $U^T$，$U$ 的各行是 $X$ 的共變異數矩陣的特徵向量 [▶ 05:46](https://youtu.be/eaMrplHvxlg?t=346)。

> **主要想法**：把資料轉到新基底，讓分量**不相關**且**變異數不同** [▶ 06:27](https://youtu.be/eaMrplHvxlg?t=387)。

---

## 3. 例子：Gauss–Markov 來源的 KLT

### 3.1 來源

[▶ 07:05](https://youtu.be/eaMrplHvxlg?t=425)

$$X_n=\rho X_{n-1}+\sqrt{1-\rho^2}\ \mathcal N(0,\sigma^2),\qquad X_0\sim\mathcal N(0,\sigma^2),$$

雜訊 iid。區塊大小 $k=2$ [▶ 07:43](https://youtu.be/eaMrplHvxlg?t=463)。這叫 **Gauss–Markov 來源**：高斯，而且 $X_n$ 只依賴前一個符號加上雜訊（Markov 性質）[▶ 08:14](https://youtu.be/eaMrplHvxlg?t=494)。

[▶ 08:14](https://youtu.be/eaMrplHvxlg?t=494) 把每兩個樣本畫成二維散佈圖：明顯相關，知道前一個就大概知道下一個 [▶ 08:50](https://youtu.be/eaMrplHvxlg?t=530)。

### 3.2 每個 $X_n$ 的分布

[▶ 09:43](https://youtu.be/eaMrplHvxlg?t=583) $X_1=\rho X_0+\sqrt{1-\rho^2}\,Z$，$Z$ 和 $X_0$ 獨立。獨立高斯相加：平均相加、變異數相加 [▶ 10:25](https://youtu.be/eaMrplHvxlg?t=625)：

$$X_1\sim\mathcal N\left(0,\ \rho^2\sigma^2+(1-\rho^2)\sigma^2\right)=\mathcal N(0,\sigma^2).$$

[▶ 11:02](https://youtu.be/eaMrplHvxlg?t=662) 這就是那個 $\sqrt{1-\rho^2}$ 的用意：讓分析簡單。依此類推，每個 $X_n\sim\mathcal N(0,\sigma^2)$，每個符號的分布都**平穩** [▶ 11:38](https://youtu.be/eaMrplHvxlg?t=698)。

### 3.3 共變異數矩陣【課堂討論】

[▶ 12:13](https://youtu.be/eaMrplHvxlg?t=733) KLT 第一步：算 $2\times2$ 共變異數矩陣（提示：過程平穩）[▶ 12:53](https://youtu.be/eaMrplHvxlg?t=773)。平均都是 0 [▶ 13:56](https://youtu.be/eaMrplHvxlg?t=836)：

- 對角項：$\mathbb{E}[X_0^2]=\mathbb{E}[X_1^2]=\sigma^2$ [▶ 14:33](https://youtu.be/eaMrplHvxlg?t=873)。
- 非對角項 [▶ 15:39](https://youtu.be/eaMrplHvxlg?t=939)：$\mathbb{E}[X_0X_1]$。學生直接答 $\rho\sigma^2$ [▶ 16:14](https://youtu.be/eaMrplHvxlg?t=974)。

$$\mathbb{E}[X_1X_0]=\mathbb{E}\left[\rho X_0^2\right]+\sqrt{1-\rho^2}\,\mathbb{E}[Z]\,\mathbb{E}[X_0]=\rho\sigma^2+0.$$

（第二項用獨立 ⇒ 期望值可以拆開，而兩者平均都是 0 [▶ 17:25](https://youtu.be/eaMrplHvxlg?t=1045)。）

$$\Sigma=\sigma^2\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}.$$

### 3.4 特徵分解

【課堂討論】[▶ 18:40](https://youtu.be/eaMrplHvxlg?t=1120) 下一步？學生答：**特徵向量分解** [▶ 18:40](https://youtu.be/eaMrplHvxlg?t=1120)。

[▶ 19:30](https://youtu.be/eaMrplHvxlg?t=1170) 講者請大家回家自己算（$2\times2$ 不難）：

| 特徵值 | 特徵向量 |
|---|---|
| $(1+\rho)\sigma^2$ | $\frac1{\sqrt2}(1,1)$ |
| $(1-\rho)\sigma^2$ | $\frac1{\sqrt2}(1,-1)$ |

> 以下**不是逐字稿內容**，是補上計算：$\det(\Sigma-\lambda I)=(\sigma^2-\lambda)^2-\rho^2\sigma^4=0$ ⇒ $\lambda=\sigma^2(1\pm\rho)$。代回：$\lambda=(1+\rho)\sigma^2$ 時 $(\Sigma-\lambda I)v=0$ 給 $v_1=v_2$；$\lambda=(1-\rho)\sigma^2$ 時給 $v_1=-v_2$。

### 3.5 轉換後的分量【課堂討論】

[▶ 20:41](https://youtu.be/eaMrplHvxlg?t=1241) $U=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$，轉換 $T=U^T$ [▶ 21:12](https://youtu.be/eaMrplHvxlg?t=1272)。學生答：轉換後是**和與差**（正規化過）[▶ 21:49](https://youtu.be/eaMrplHvxlg?t=1309)：

$$Y_1=\frac{X_1+X_2}{\sqrt2},\qquad Y_2=\frac{X_1-X_2}{\sqrt2}.$$

### 3.6 去相關了

[▶ 23:34](https://youtu.be/eaMrplHvxlg?t=1414) 轉換後的散佈圖：同樣尺度下看起來相關性小了，但光看圖不能確定 [▶ 24:13](https://youtu.be/eaMrplHvxlg?t=1453)。要算 $Y$ 的共變異數（講者留作回家練習）[▶ 24:52](https://youtu.be/eaMrplHvxlg?t=1492)：

$$\Sigma_Y=\sigma^2\begin{bmatrix}1+\rho&0\\0&1-\rho\end{bmatrix}.$$

> 以下**不是逐字稿內容**，是補上驗算：$\mathbb{E}[Y_1Y_2]=\frac12\left(\mathbb{E}X_1^2-\mathbb{E}X_2^2\right)=0$；$\mathbb{E}Y_1^2=\frac12(\sigma^2+2\rho\sigma^2+\sigma^2)=(1+\rho)\sigma^2$；$\mathbb{E}Y_2^2=(1-\rho)\sigma^2$。

[▶ 25:28](https://youtu.be/eaMrplHvxlg?t=1528) 換成各自的尺度（縱軸 −0.4 到 0.4、橫軸 −4 到 4）再看：點分布成圓形，看 $Y_1$ 猜不出 $Y_2$；而且兩個方向的尺度差很多 [▶ 26:02](https://youtu.be/eaMrplHvxlg?t=1562)。

> 這個轉換做到了兩件事：**去相關**，而且給出**變異數差很多**的兩個分量，可以照注水直覺分配位元 [▶ 26:36](https://youtu.be/eaMrplHvxlg?t=1596)。

---

## 4. 轉換編碼的兩個旋鈕

### 4.1 流程

[▶ 28:00](https://youtu.be/eaMrplHvxlg?t=1680) 來源 $x_{1,1},x_{1,2},x_{2,1},x_{2,2},\dots$（每兩個一組）[▶ 28:35](https://youtu.be/eaMrplHvxlg?t=1715)：

1. **選轉換的區塊大小**：這個例子明顯是 $2\times2$，因為我們知道相依只往回一步；實務上不知道相關性延伸多遠 [▶ 29:12](https://youtu.be/eaMrplHvxlg?t=1752)。也可以 $4\times4$、$8\times8$、$16\times16$ [▶ 29:45](https://youtu.be/eaMrplHvxlg?t=1785)。
2. 轉換後，還是要做以前的那套：量化、碼本，最後送位元流 [▶ 29:45](https://youtu.be/eaMrplHvxlg?t=1785)。做法 [▶ 30:20](https://youtu.be/eaMrplHvxlg?t=1820)：**每個轉換分量當成一條串流**，各自獨立量化（純量、向量、不同區塊大小都可以）[▶ 30:59](https://youtu.be/eaMrplHvxlg?t=1859)。

[▶ 31:36](https://youtu.be/eaMrplHvxlg?t=1896) 為什麼各自量化？這樣才能利用兩條串流變異數不同：$\mathrm{Var}(Y_1)=(1+\rho)\sigma^2$、$\mathrm{Var}(Y_2)=(1-\rho)\sigma^2$，用注水分配位元 [▶ 32:12](https://youtu.be/eaMrplHvxlg?t=1932)。

### 4.2 兩個旋鈕

[▶ 32:50](https://youtu.be/eaMrplHvxlg?t=1970) 例：平均 1 位元／樣本（投影片原本寫 2，學生指出後講者更正）[▶ 39:54](https://youtu.be/eaMrplHvxlg?t=2394)。

1. **每個分量的位元分配** [▶ 32:50](https://youtu.be/eaMrplHvxlg?t=1970)：$(1,1)$、$(2,0)$（第二條根本不送）……都合法，平均都是 1 位元／符號 [▶ 33:58](https://youtu.be/eaMrplHvxlg?t=2038)。
2. **每條串流的量化方式** [▶ 34:46](https://youtu.be/eaMrplHvxlg?t=2086)：例如分量 1 用 1 位元純量量化（碼本大小 2）；分量 2 用向量長度 2 的向量量化（碼本大小 $2^2=4$）[▶ 36:35](https://youtu.be/eaMrplHvxlg?t=2195)。這就遞迴回到量化那一講。

【口頭】[▶ 36:35](https://youtu.be/eaMrplHvxlg?t=2195) "component"、"stream"、"channel" 在實務上會混用，看上下文。

[▶ 37:08](https://youtu.be/eaMrplHvxlg?t=2228) 再加上：轉換本身和它的區塊大小也是旋鈕。實務上調率失真時**兩種都調**，產生很多不同率的壓縮串流，再挑最好的 [▶ 37:42](https://youtu.be/eaMrplHvxlg?t=2262)；例如串流服務 [▶ 38:14](https://youtu.be/eaMrplHvxlg?t=2294)。

【Q&A】[▶ 38:14](https://youtu.be/eaMrplHvxlg?t=2294) 學生問：每條串流各給 1 位元／樣本，合起來不就還是每樣本 1 位元？講者 [▶ 38:47](https://youtu.be/eaMrplHvxlg?t=2327)：轉換後兩條串流是各自壓縮的（丟掉二維結構，把所有 $Y_1$ 一起壓、所有 $Y_2$ 一起壓）。學生指出投影片寫的是 2 位元／樣本；講者：寫錯了，應該是 1 位元 [▶ 39:24](https://youtu.be/eaMrplHvxlg?t=2364)。

---

## 5. 實驗：VQ vs. 轉換編碼

[▶ 39:54](https://youtu.be/eaMrplHvxlg?t=2394) notebook（只描述）：線性轉換、向量量化器、`TransformVqEncoder`/`Decoder`：先用線性層轉換，再對每個係數（串流）分別向量量化 [▶ 41:09](https://youtu.be/eaMrplHvxlg?t=2469)。編碼器對每個係數做迴圈、各自 VQ 編碼，還要**寫下每條串流的長度**，不然串起來後不知道第二條從哪開始 [▶ 42:21](https://youtu.be/eaMrplHvxlg?t=2541)。解碼器反過來做。【口頭】[▶ 42:55](https://youtu.be/eaMrplHvxlg?t=2575) 建議把它當理解型作業：先別看程式，自己實作一次。

**結果**（全部固定 1 位元／符號，`L14.pdf` 的輸出）[▶ 43:35](https://youtu.be/eaMrplHvxlg?t=2615)：

| | $\rho=0.9$ | $\rho=0.99$ | $\rho=0.5$ |
|---|---|---|---|
| VQ，區塊 2 | 0.163 | 0.107 | 0.305 |
| VQ，區塊 4 | 0.095 | 0.020 | 0.271 |
| 轉換 + VQ，分配 $(1,1)$ | 0.276 | 0.204 | 0.374 |
| 轉換 + VQ，分配 $(0,2)$ | 0.970 | 0.890 | 0.786 |
| 轉換 + VQ，分配 $(2,0)$ | **0.122** | **0.030** | 0.343 |

（數字是 MSE 失真。）

- [▶ 44:14](https://youtu.be/eaMrplHvxlg?t=2654) VQ：區塊越大失真越低，但複雜度也越高（要在 4 維找碼本點）。
- 【課堂討論】[▶ 45:56](https://youtu.be/eaMrplHvxlg?t=2756) $\rho=0.9$ 時不同分配差這麼多，為什麼？學生答：第一個分量變異數大很多，需要更多空間；位元給錯分量，失真就很高 [▶ 46:36](https://youtu.be/eaMrplHvxlg?t=2796)。講者：**位元多給變異數大的分量**，用同樣的量化複雜度（多一步轉換）就勝過 0.163；反過來就付很大的代價；平分也不是最佳的 [▶ 47:14](https://youtu.be/eaMrplHvxlg?t=2834)。
- 【課堂討論】[▶ 47:53](https://youtu.be/eaMrplHvxlg?t=2873) $\rho$ 變大，好處會更多還是更少？舉手大約一半一半，講者：**更多** [▶ 48:34](https://youtu.be/eaMrplHvxlg?t=2914)。兩個變異數 $(1\pm\rho)\sigma^2$ 的差距變大，更能注水、更早丟掉小的分量 [▶ 49:17](https://youtu.be/eaMrplHvxlg?t=2957)。$\rho=0.99$：$(2,0)$ 只有 0.030，遠小於 VQ 區塊 2 的 0.107 [▶ 49:17](https://youtu.be/eaMrplHvxlg?t=2957)。
- [▶ 49:55](https://youtu.be/eaMrplHvxlg?t=2995) 但 VQ 區塊 4 仍然贏 $(2,0)$。**向量量化很強，只是很吃計算**；轉換編碼常讓你「用一支箭就能解決，而不必用火箭」[▶ 50:27](https://youtu.be/eaMrplHvxlg?t=3027)。
- [▶ 50:27](https://youtu.be/eaMrplHvxlg?t=3027) $\rho=0.5$：連 $(2,0)$ 都贏不了 VQ 區塊 2。講者留作思考題，提示 [▶ 51:33](https://youtu.be/eaMrplHvxlg?t=3093)：變異數是 $(1+\rho)\sigma^2$ 和 $(1-\rho)\sigma^2$，兩者獨立高斯，問題的精確解已經推過了；$\rho$ 小時，總失真可能比**兩個**變異數都小，那就不能把第一個……（應為第二個）分量完全丟掉，而要給它較少但非零的率 [▶ 52:08](https://youtu.be/eaMrplHvxlg?t=3128)。這次實驗沒找到正確的分配 [▶ 52:45](https://youtu.be/eaMrplHvxlg?t=3165)。

> 以下**不是逐字稿內容**，是照講者的提示做出這個思考題（$\sigma^2=1$，平均 1 位元／符號）：
> - **$\rho=0.5$**：變異數 1.5、0.5。試情況 1（平分失真）：$\frac12\left[\frac12\log\frac{1.5}D+\frac12\log\frac{0.5}D\right]=1$ ⇒ $D^2=\frac{0.75}{16}$ ⇒ $D\approx0.217<0.5$，確實在兩個變異數以下。所以最佳分配是 $R_1=\frac12\log\frac{1.5}{0.217}\approx1.40$、$R_2=\frac12\log\frac{0.5}{0.217}\approx0.60$，**兩個分量都要給位元**，$(2,0)$ 不是最佳的。
> - **$\rho=0.9$**：變異數 1.9、0.1。平分會得到 $D\approx0.109>0.1$，所以是情況 2：$D_2=0.1$（不送）、$\frac14\log\frac{1.9}{2D-0.1}=1$ ⇒ $D\approx0.109$。最佳分配正是 $(2,0)$，和實驗一致；理論最佳 0.109，實驗的 0.122 已很接近。

【口頭】[▶ 52:45](https://youtu.be/eaMrplHvxlg?t=3165) 建議照上一講小考的方式自己算一次。

---

## 6. 為什麼實務上不用 KLT

[▶ 52:45](https://youtu.be/eaMrplHvxlg?t=3165) 實際上**沒人用 KLT** [▶ 53:26](https://youtu.be/eaMrplHvxlg?t=3206)：

1. KLT **依賴輸入的統計**：要從樣本估分布或直接估共變異數矩陣，每來一批新資料就要重算一次，而特徵分解要花計算時間 [▶ 54:00](https://youtu.be/eaMrplHvxlg?t=3240)。**這是主要問題。**
2. 實務上不知道真的 $\Sigma$，只能估計，有誤差 [▶ 54:41](https://youtu.be/eaMrplHvxlg?t=3281)（次要）。

[▶ 54:41](https://youtu.be/eaMrplHvxlg?t=3281) 所以要的是：**一個固定的、結構化的轉換 $T$**，不隨資料改變、好算，又有好的**能量集中**性質 [▶ 55:27](https://youtu.be/eaMrplHvxlg?t=3327)。不能去相關、不能集中能量的轉換，對壓縮沒用。

---

## 7. 實用的轉換：DCT

### 7.1 由來

[▶ 56:03](https://youtu.be/eaMrplHvxlg?t=3363) **離散餘弦轉換**（Discrete Cosine Transform, DCT）：用在非常多壓縮器裡；熟 Fourier 轉換的人可以把它想成 **DFT 的兄弟**，另一種頻率轉換。

【口頭】[▶ 56:38](https://youtu.be/eaMrplHvxlg?t=3398) Kedar 找到發明者寫的文章〈How I Came Up with the Discrete Cosine Transform〉，週末讀很有趣。兩段摘錄：

- 他著迷的是：**KLT 是最佳轉換，卻沒有有效率的演算法能算它**；所以研究重點是能不能找到一個**能有效計算的 KLT 近似** [▶ 57:21](https://youtu.be/eaMrplHvxlg?t=3441)。
- 他想出了 DCT，現在到處都用 [▶ 57:21](https://youtu.be/eaMrplHvxlg?t=3441)。好笑的是，**NSF 當時沒資助他的計畫**。講者說：做研究時你相信自己的想法但沒人相信，別灰心 [▶ 57:21](https://youtu.be/eaMrplHvxlg?t=3441)。

[▶ 57:21](https://youtu.be/eaMrplHvxlg?t=3441) 每次在瀏覽器載入一張圖、打開多媒體檔，幾乎都有一個 DCT 在跑：音訊、影片、YouTube、Netflix、Spotify [▶ 58:08](https://youtu.be/eaMrplHvxlg?t=3488)。

> ⚠️ 逐字稿缺字 [▶ 56:38](https://youtu.be/eaMrplHvxlg?t=3398)：字幕把作者名字寫成「Nasser」；投影片只列文章標題，作者全名待補。

### 7.2 實用轉換的共通點

[▶ 58:43](https://youtu.be/eaMrplHvxlg?t=3523) 選擇很多：DCT、DFT、小波……（維基百科有一張 Fourier 類轉換的清單）。講者說這部分會很直覺、不嚴謹，嚴謹的要上訊號處理課 [▶ 59:17](https://youtu.be/eaMrplHvxlg?t=3557)。

[▶ 59:55](https://youtu.be/eaMrplHvxlg?t=3595)

1. 大多基於**正交（正規）基底**。
2. 利用訊號在某個基底下的**稀疏性**：DCT 利用訊號在**餘弦（頻率）基底**下的稀疏性。自然訊號做 DCT 後，很多轉換分量本來就是 0 或很小，可以丟掉 [▶ 1:00:34](https://youtu.be/eaMrplHvxlg?t=3634)。這正是能量集中。
3. 為什麼有效：**自然訊號的統計** [▶ 1:01:10](https://youtu.be/eaMrplHvxlg?t=3670)。自然影像、音訊、影片做頻率分析，**大部分能量在低頻**，高頻能量很少 [▶ 1:01:44](https://youtu.be/eaMrplHvxlg?t=3704)。（講者：這是一個不明顯的直覺跳躍：「周圍的世界是被低通濾波過的」。）DCT 在某些設定下也是 KLT 的好近似（不細講）。

### 7.3 另一個理由：人的感知

[▶ 1:02:23](https://youtu.be/eaMrplHvxlg?t=3743) 實際壓縮器怎麼丟位元、怎麼分配位元，不只看能量，還看**最終是誰在用** [▶ 1:02:57](https://youtu.be/eaMrplHvxlg?t=3777)：

- 影像、音訊最後給人看、聽。人看不到太高頻的東西，雜訊頻率很高的話低通濾波後就看不到。
- 人聽得到約 20 Hz–20 kHz（實際上很少人那麼寬）[▶ 1:03:34](https://youtu.be/eaMrplHvxlg?t=3814)。20 kHz 以上的分量就算有能量也不用存，沒有人會聽到（目前也沒在為狗壓縮音訊）。

[▶ 1:03:34](https://youtu.be/eaMrplHvxlg?t=3814) 關鍵：**MSE 不是對的度量**，某種意義上「人的誤差」才是 [▶ 1:04:12](https://youtu.be/eaMrplHvxlg?t=3852)。感恩節後有一整講專講這個（資訊理論課通常不講，但對壓縮很重要）。

> **帶走的重點：高頻分量壓多一點，通常就沒問題。** [▶ 1:04:50](https://youtu.be/eaMrplHvxlg?t=3890)

### 7.4 DCT 的性質

[▶ 1:04:50](https://youtu.be/eaMrplHvxlg?t=3890)（`L14_ann.pdf`）

- 在離散點上取餘弦函數的值 [▶ 1:05:26](https://youtu.be/eaMrplHvxlg?t=3926)。
- **線性**，而且是**正交**的。
- DFT 的變體，輸出可以想成把訊號拆成不同的獨立頻率通道。
- **實數值**：Fourier 轉換可能有虛數，DCT 不會 [▶ 1:05:58](https://youtu.be/eaMrplHvxlg?t=3958)。
- **無損轉換**（$T^{-1}$ 存在），可以直接插進流程。
- 有 DCT-I、II、III、IV 等版本，差在推導矩陣時的**邊界條件**；壓縮多用 **DCT-II** [▶ 1:06:30](https://youtu.be/eaMrplHvxlg?t=3990)。

> 以下**不是逐字稿內容**，是補上 DCT-II 的常見正交形式（課堂說公式放在 notebook 裡，請自己看）：長度 $N$ 的區塊，
> $$C_{k,n}=\alpha_k\cos\left(\frac{\pi(2n+1)k}{2N}\right),\quad k,n=0,\dots,N-1,\qquad\alpha_0=\sqrt{\tfrac1N},\ \alpha_k=\sqrt{\tfrac2N}\ (k\ge1).$$
> 第 0 列是常數 $\sqrt{1/N}$（對應 §8.1 說的「第一列是常數」），第 $k$ 列是頻率遞增的餘弦取樣；$C$ 是正交矩陣，$C^{-1}=C^T$。

---

## 8. DCT 的直覺：notebook 例子

### 8.1 轉換矩陣

[▶ 1:07:02](https://youtu.be/eaMrplHvxlg?t=4022) 區塊大小取 8，DCT 矩陣是 $8\times8$ [▶ 1:07:37](https://youtu.be/eaMrplHvxlg?t=4057)。畫成色塊圖（黃正、藍負）：

- **第 0 列是常數**：乘上向量，第一個係數就正比於所有分量的和（差不多是平均）[▶ 1:07:37](https://youtu.be/eaMrplHvxlg?t=4057)。
- 往下越來越「扭」：每一列是把某個餘弦波離散化取 8 個點，**頻率越來越高** [▶ 1:08:48](https://youtu.be/eaMrplHvxlg?t=4128)。

### 8.2 幾種訊號

[▶ 1:09:54](https://youtu.be/eaMrplHvxlg?t=4194)

1. **常數訊號** [▶ 1:09:54](https://youtu.be/eaMrplHvxlg?t=4194)：DCT 只在第 0 個係數有值（只有常數頻率）；IDCT 還原原訊號。
2. **不同頻率的正弦波** [▶ 1:10:31](https://youtu.be/eaMrplHvxlg?t=4231)：例如某個頻率的訊號，DCT 大部分高頻係數是 0，在第 2 個係數有峰值。頻率越高，非零的係數就往高的索引移 [▶ 1:11:06](https://youtu.be/eaMrplHvxlg?t=4266)。DCT 在**追蹤頻率** [▶ 1:11:46](https://youtu.be/eaMrplHvxlg?t=4306)。不是完美的 delta 函數，因為連續變離散後很多事取決於邊界和取樣點。
3. **一般訊號**（三角形）[▶ 1:11:46](https://youtu.be/eaMrplHvxlg?t=4306)：大部分是低頻，但也有一點非零的高頻（例如第 5 個係數有個小柱子）[▶ 1:12:19](https://youtu.be/eaMrplHvxlg?t=4339)。IDCT 還原原訊號。

### 8.3 丟掉小係數

[▶ 1:12:51](https://youtu.be/eaMrplHvxlg?t=4371) 有損壓縮不會保留全部 DCT。直覺：**丟掉能量很小的分量**，就不用量化那整條串流。做法：設門檻，絕對值低於門檻的係數設成 0 [▶ 1:13:27](https://youtu.be/eaMrplHvxlg?t=4407)。

| 門檻 | 結果 |
|---|---|
| 0 | 保留全部，重建完全一樣 |
| 0.25 | 只有一個小係數變 0，出現一點誤差 [▶ 1:13:27](https://youtu.be/eaMrplHvxlg?t=4407) |
| 0.5 | 所有高頻係數都是 0，8 個只留 3 個，但重建（綠）和原訊號（紅）差不多 [▶ 1:14:06](https://youtu.be/eaMrplHvxlg?t=4446) |
| 更大 | 最後只剩 DC（只傳平均），誤差爆表 [▶ 1:14:42](https://youtu.be/eaMrplHvxlg?t=4482) |

[▶ 1:14:42](https://youtu.be/eaMrplHvxlg?t=4482) 門檻 1 或 2（留 2、3 個係數）看情況可能可以接受。這就是 DCT 的用法：拆成轉換分量，丟掉一些；更常見的是不完全丟掉，而是**某些分量壓多一點、某些壓少一點** [▶ 1:15:17](https://youtu.be/eaMrplHvxlg?t=4517)。

### 8.4 為什麼不用 Fourier 轉換？【Q&A】

[▶ 1:15:54](https://youtu.be/eaMrplHvxlg?t=4554) 學生問：DCT 和 Fourier 轉換有什麼不同？

講者 [▶ 1:15:54](https://youtu.be/eaMrplHvxlg?t=4554)：可以想成姊妹轉換，差在**邊界條件**。切成區塊時，DCT 處理邊界比較好 [▶ 1:16:27](https://youtu.be/eaMrplHvxlg?t=4587)。Shubham 補充：對常數類的訊號 DCT 比較好；餘弦在 0 是平的，正弦在 0 的導數大 [▶ 1:17:02](https://youtu.be/eaMrplHvxlg?t=4622)。

講者再解釋 [▶ 1:17:02](https://youtu.be/eaMrplHvxlg?t=4622)：訊號是連續的串流，切成 8 個一組。希望逆轉換後區塊**邊界不要突然跳**：若第一個區塊最後一個值是 1、第二個區塊開頭也是一串 1，常數就該跨區塊保持常數 [▶ 1:17:42](https://youtu.be/eaMrplHvxlg?t=4662)。DCT 在丟掉係數後仍能讓常數訊號保持常數；DFT 可能造成很大的跳動。這種跳動是常見的假影，叫**區塊效應**（blocking artifacts）[▶ 1:17:42](https://youtu.be/eaMrplHvxlg?t=4662)。講者說之後會在 Ed 上貼更詳細的回答 [▶ 1:18:20](https://youtu.be/eaMrplHvxlg?t=4700)。

---

## 9. 一個陽春的有損壓縮器：音訊

### 9.1 流程

[▶ 1:18:20](https://youtu.be/eaMrplHvxlg?t=4700)

```
編碼：X ──[轉換]──> Y ──[量化]──> 碼本索引 ──[熵編碼]──> 位元流（決定率）
解碼：位元流 ──[熵解碼]──> 碼本索引 ──[反量化]──> Ŷ ──[反轉換]──> X̂
失真 = d(X, X̂)
```

[▶ 1:19:25](https://youtu.be/eaMrplHvxlg?t=4765) **唯一有損的步驟是量化**。做完這些就有一個實用的有損壓縮器；下一講的 **JPEG 本質上就是這張圖**，只是每個方塊都最佳化到極致 [▶ 1:19:25](https://youtu.be/eaMrplHvxlg?t=4765)。

[▶ 1:20:02](https://youtu.be/eaMrplHvxlg?t=4802) 設計選擇很多：轉換、量化、熵編碼都有很多選項，課堂只講了一些。

### 9.2 音訊壓縮器

[▶ 1:20:36](https://youtu.be/eaMrplHvxlg?t=4836)（Shubham 寫的 notebook）：轉換用 **DCT**、量化用**純量量化**；這裡沒做熵編碼。兩個旋鈕 [▶ 1:21:10](https://youtu.be/eaMrplHvxlg?t=4870)：

1. **頻率截止**（frequency cutoff）：留幾個 DCT 分量（就是 §8.3 的低通 DCT）。
2. **量化等級數**：每個分量量化得多細。

[▶ 1:21:43](https://youtu.be/eaMrplHvxlg?t=4903) 一段音訊的 DCT：橫軸是頻率分量（獨立的轉換通道）、縱軸是能量。自然訊號在某個頻率之後**能量突然掉下去**，這就是自然訊號的統計 [▶ 1:22:17](https://youtu.be/eaMrplHvxlg?t=4937)。

### 9.3 聽聽看

[▶ 1:22:50](https://youtu.be/eaMrplHvxlg?t=4970) 原曲（講者說做過作業 3 就知道有位講者是寶可夢迷）。

| 版本 | 聽起來 |
|---|---|
| 原始 | 原曲 |
| **低頻截止**（丟掉高頻） | 還聽得出在唱什麼，但**很悶**（dull）[▶ 1:23:23](https://youtu.be/eaMrplHvxlg?t=5003) |
| **減少量化等級**（保留所有頻率） | 樂器、高音、低音都在，但背後有**沙沙的靜電雜訊** [▶ 1:23:23](https://youtu.be/eaMrplHvxlg?t=5003)、[▶ 1:24:03](https://youtu.be/eaMrplHvxlg?t=5043) |

[▶ 1:24:03](https://youtu.be/eaMrplHvxlg?t=5043) 兩個旋鈕造成**聽感很不一樣**的失真。

### 9.4 率失真曲線與編碼表

[▶ 1:24:03](https://youtu.be/eaMrplHvxlg?t=5043) 把各種組合畫成率失真圖：橫軸率、縱軸失真；不同顏色是不同頻率截止、不同符號是不同量化等級 [▶ 1:24:38](https://youtu.be/eaMrplHvxlg?t=5078)。實務上也這樣做：串流服務會把這首歌編成很多版本，在每個率下保留失真最低的那個 [▶ 1:24:38](https://youtu.be/eaMrplHvxlg?t=5078)。

[▶ 1:24:38](https://youtu.be/eaMrplHvxlg?t=5078) 黑線是 Pareto 最佳線：

- **極低率**時，靠**多納入一些頻率**得益（顏色在變）。
- 過了某點，再多頻率沒用（能量本來就很低），改成把低頻分量量化得更精細（符號在變）[▶ 1:25:13](https://youtu.be/eaMrplHvxlg?t=5113)。

[▶ 1:25:49](https://youtu.be/eaMrplHvxlg?t=5149) 每家串流服務都有這種東西，叫**編碼表**（encoding tables）。

### 9.5 有轉換 vs. 沒轉換

[▶ 1:25:49](https://youtu.be/eaMrplHvxlg?t=5149) 沒上這門課的朋友直接量化、不做轉換：在同樣的量化能力下，失真高很多（圖上的黑點）[▶ 1:26:22](https://youtu.be/eaMrplHvxlg?t=5182)。

【課堂討論】[▶ 1:26:22](https://youtu.be/eaMrplHvxlg?t=5182) 再聽兩段：一段是轉換 + 量化（低通），一段是直接量化 [▶ 1:26:53](https://youtu.be/eaMrplHvxlg?t=5213)。聽起來差不多，因為講者故意讓兩者 **MSE 一樣**；但位元率：**直接量化 160 kbps，轉換 + 量化只要 86 kbps** [▶ 1:26:53](https://youtu.be/eaMrplHvxlg?t=5213)。

[▶ 1:27:27](https://youtu.be/eaMrplHvxlg?t=5247) 最後想和很流行的 **MP3** 比較，錄影在這裡結束。

> ⚠️ 待確認 [▶ 1:27:27](https://youtu.be/eaMrplHvxlg?t=5247)：錄影在和 MP3 比較前中斷，比較結果待補（可能在 notebook 或下一講開頭）。

---

## 10. 一頁速查表

### Gauss–Markov 例子（$k=2$）

$$\Sigma=\sigma^2\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix},\quad\lambda=(1\pm\rho)\sigma^2,\quad Y_1=\frac{X_1+X_2}{\sqrt2},\ Y_2=\frac{X_1-X_2}{\sqrt2},\quad\Sigma_Y=\mathrm{diag}\left((1+\rho)\sigma^2,(1-\rho)\sigma^2\right)$$

**關鍵一步**：$\mathbb{E}[X_0X_1]=\rho\,\mathbb{E}X_0^2=\rho\sigma^2$（雜訊項因獨立且零平均消失）。

### 轉換編碼的旋鈕

1. 轉換與區塊大小。
2. 每條串流的位元分配（照注水）與量化方式（純量／向量）。
- 實務上兩個都掃一遍，取 Pareto 前緣（編碼表）。

### 實驗教訓（1 位元／符號）

- 位元給大變異數分量：$\rho=0.9$ 時 0.122 vs. 平分 0.276 vs. 給錯 0.970。
- $\rho$ 越大好處越大；$\rho$ 小時兩個分量都該給位元（注水情況 1）。
- VQ 區塊 4 仍可能更好，但複雜度高。

### KLT vs. DCT

| | KLT | DCT |
|---|---|---|
| 依賴資料 | 是，要重算 | 否，固定 |
| 最佳性 | 對給定 $\Sigma$ 最佳 | 對自然訊號接近最佳 |
| 計算 | 特徵分解 | 有快速演算法 |

DCT：正交、實數、無損、頻率遞增的離散餘弦；壓縮用 DCT-II；比 DFT 更不會在區塊邊界跳動。

### 自然訊號

能量集中在低頻；人也聽不到、看不到很高頻 ⇒ **高頻壓多一點**。

### 陽春有損壓縮器

轉換 → 量化（唯一有損）→ 熵編碼。音訊例：低頻截止 → 悶；量化粗 → 沙沙聲；同 MSE 下轉換 86 kbps vs. 直接量化 160 kbps。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| DCT → 量化 → 熵編碼 | 第 15 集 JPEG（8×8 DCT、量化表、Huffman） |
| 區塊效應 | 第 15 集 JPEG 的假影、BPG 的去區塊濾波 |
| 學出來的非線性轉換 | 第 16 集 |
| 人的感知、MSE 不是對的度量 | 第 17 集 |
| 編碼表、串流服務選版本 | 第 18 集影片壓縮 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **Gauss–Markov 來源兩個一組做 KLT，得到「和」與「差」兩個不相關、變異數 $(1\pm\rho)\sigma^2$ 差很多的分量；位元給變異數大的那個，用很簡單的量化就能大幅降低失真，$\rho$ 越大越明顯。KLT 要隨資料重算，所以實務上用固定的 DCT：自然訊號能量集中在低頻、人也感受不到高頻，所以高頻壓多一點就好。轉換 → 量化 → 熵編碼就是一個陽春但實用的有損壓縮器，音訊例子裡同樣 MSE 下只要不做轉換時一半的位元率。**

---

## ⚠️ 待確認清單

1. [▶ 1:27:27](https://youtu.be/eaMrplHvxlg?t=5247) 錄影在和 MP3 比較前中斷，比較結果待補。
2. [▶ 56:38](https://youtu.be/eaMrplHvxlg?t=3398) DCT 發明者的全名：字幕作「Nasser」，投影片只列文章標題。

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 14 錄影逐字稿（人工字幕，1:28:03）與投影片 L14、L14_ann 整理；注水結果見 Cover & Thomas §10.3.3。*
