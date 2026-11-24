---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 16
lecture: Lecture 16
date: 2023-11-27
video: https://youtu.be/H7dvh35xNuE
notes: 投影片 slide_16_2023.pdf；課本沒有學習式壓縮
---

# 第 16 集 · Lecture 16：學習式影像壓縮（Learnt Image Compression） [▶ 影片](https://youtu.be/H7dvh35xNuE)

← 上一集：[15-image-compression-jpeg-bpg](15-image-compression-jpeg-bpg.md) ｜ [總目錄](README.md) ｜ 下一集：[17-humans-and-compression](17-humans-and-compression.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 16 集
> **講者**：Pulkit Tandon
> **來源**：YouTube 錄影逐字稿（1:21:18，人工字幕 en-US）＋ 投影片 `slide_16_2023.pdf`。課本沒有這部分。
> **標記說明**：
> - `【口頭】` 講者口頭補充，投影片沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧與小考](#1-回顧與小考)
- [2. 傳統壓縮器還有很大空間](#2-傳統壓縮器還有很大空間)
- [3. 兩個動機：非線性轉換、端到端學習](#3-兩個動機非線性轉換端到端學習)
- [4. 機器學習 101](#4-機器學習-101)
- [5. 自編碼器](#5-自編碼器)
- [6. 學習式影像壓縮的架構與損失函數](#6-學習式影像壓縮的架構與損失函數)
- [7. 兩個不可微分的地方與繞法](#7-兩個不可微分的地方與繞法)
- [8. 直覺：率項和失真項在拔河](#8-直覺率項和失真項在拔河)
- [9. Notebook 示範：MNIST 壓縮器](#9-notebook-示範mnist-壓縮器)
- [10. 好處](#10-好處)
- [11. 現況與問題](#11-現況與問題)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/H7dvh35xNuE?t=5) 接下來幾講比較進階，**不會出作業**，但請盡量吸收、多參與討論。今天：怎麼用**機器學習**做影像壓縮，超越傳統的影像壓縮器 [▶ 02:28](https://youtu.be/H7dvh35xNuE?t=148)。

---

## 1. 回顧與小考

### 1.1 回顧

[▶ 00:05](https://youtu.be/H7dvh35xNuE?t=5) 影像是 $H\times W\times C$ 的像素陣列，每個值常是 1 位元組（有時 10 或 12 位元）。[▶ 00:46](https://youtu.be/H7dvh35xNuE?t=46) 1.1 MB 的原圖：JPEG 40×（27 KB）看不出差別；80×（14 KB）明顯假影；137×（8 KB）認不出來 [▶ 01:18](https://youtu.be/H7dvh35xNuE?t=78)。BPG 用**可變區塊大小**和**預測編碼**，同樣 8 KB 好很多 [▶ 01:53](https://youtu.be/H7dvh35xNuE?t=113)。但 BPG 仍有很多手工調整的參數 [▶ 02:28](https://youtu.be/H7dvh35xNuE?t=148)。

### 1.2 小考

[▶ 02:28](https://youtu.be/H7dvh35xNuE?t=148) 第 1 題（$370\times370$ 影像，加上 alpha 通道）：

| 題 | 答案（`slide_16_2023.pdf`） |
|---|---|
| RGB + alpha 各 8 位元 | $370\times370\times(24+8)$ 位元 $=547.6$ KB |
| 顏色 1 位元 + alpha 8 位元 | $370\times370\times9$ 位元 $\approx154.0$ KB |
| 顏色 1 位元 + alpha 1 位元 | $370\times370\times2$ 位元 $\approx34.2$ KB |

**為什麼 PNG 比「顏色 1 位元 + alpha 1 位元」還小？** [▶ 03:05](https://youtu.be/H7dvh35xNuE?t=185) 課堂沒教 PNG，題目是要大家猜。講者：很多答案都對；基本上 **PNG 的熵編碼比 JPEG 好得多** [▶ 03:39](https://youtu.be/H7dvh35xNuE?t=219)。JPEG 只是行程編碼 + Huffman；PNG 用 **LZ77** 系的無損編碼器，這張影像非常均勻，能找到很多匹配（和作業 3 寶可夢那題同樣的直覺）[▶ 04:14](https://youtu.be/H7dvh35xNuE?t=254)。

第 2 題（自製的「JPEE274G」壓縮器）[▶ 04:14](https://youtu.be/H7dvh35xNuE?t=254)：

- **加大區塊什麼時候最有用？** 同一張影像用**更高解析度**表示時：像素更多、相鄰像素更相關，大區塊更能抓到區塊內的相關性 [▶ 04:49](https://youtu.be/H7dvh35xNuE?t=289)、[▶ 05:22](https://youtu.be/H7dvh35xNuE?t=322)。
- **用前面的區塊預測什麼時候最有用？** 區塊很**同質**時（例如一隻噴火龍的圖，很多區塊顏色一樣，幾乎是複製貼上），而不是一張很雜的寶可夢合照 [▶ 05:56](https://youtu.be/H7dvh35xNuE?t=356)、[▶ 06:30](https://youtu.be/H7dvh35xNuE?t=390)。

這正是 BPG 改進 JPEG 的兩個想法。

第 3 題：預測編碼的演算法，一題解碼、一題找錯誤，很直接 [▶ 07:07](https://youtu.be/H7dvh35xNuE?t=427)。

---

## 2. 傳統壓縮器還有很大空間

[▶ 07:43](https://youtu.be/H7dvh35xNuE?t=463) BPG 在 8 KB 比 JPEG 好很多，但仔細看還有假影：鼻子有方塊感、有振鈴 [▶ 08:16](https://youtu.be/H7dvh35xNuE?t=496)。**ML 影像壓縮器**同樣 8 KB，來回切換差別很明顯（看女孩的眼睛）[▶ 08:16](https://youtu.be/H7dvh35xNuE?t=496)。和 JPEG 比更是天差地遠 [▶ 08:49](https://youtu.be/H7dvh35xNuE?t=529)。

[▶ 09:21](https://youtu.be/H7dvh35xNuE?t=561) JPEG 的流程：RGB → 顏色處理（去相關）→ 轉換 → 量化 → 無損編碼 → JPEG 檔。怎麼再改進？

---

## 3. 兩個動機：非線性轉換、端到端學習

### 3.1 超越線性轉換

[▶ 09:54](https://youtu.be/H7dvh35xNuE?t=594) JPEG、JPEG2000、BPG 都用 DCT、DWT（離散小波轉換）、DFT 的變體，**全都是線性映射**（矩陣乘法）。也許允許**非線性轉換編碼**會更好，課堂完全沒講過 [▶ 09:54](https://youtu.be/H7dvh35xNuE?t=594)。

[▶ 10:28](https://youtu.be/H7dvh35xNuE?t=628) 二維向量量化的圖：紫點是碼向量、區域是決策邊界；來源密度是**香蕉形**（黃色高、藍色低）。

- 只准用**線性**邊界：這大概是最好的了 [▶ 11:01](https://youtu.be/H7dvh35xNuE?t=661)。
- 允許**非線性**邊界：可以剛好蓋住香蕉形，只需要傳很少幾個碼向量 [▶ 11:01](https://youtu.be/H7dvh35xNuE?t=661)。

真實來源的分布沒人說它一定能被線性去相關；也許某個非線性轉換能去相關 [▶ 11:41](https://youtu.be/H7dvh35xNuE?t=701)。

【投影片補充】香蕉圖出自 Ballé et al.,〈Nonlinear transform coding〉, IEEE J. Sel. Topics Signal Process. 15(2), 2020。

### 3.2 端到端學習

[▶ 11:41](https://youtu.be/H7dvh35xNuE?t=701) JPEG 有大量**手工決定的經驗法則**：量化矩陣（雖然是根據能量和很多心理視覺實驗，但沒人說它對你的影像、你的資料集最好）[▶ 12:18](https://youtu.be/H7dvh35xNuE?t=738)；8×8 區塊大小（為什麼不更大？）；不同率之間怎麼換量化矩陣，也是手調的 [▶ 12:52](https://youtu.be/H7dvh35xNuE?t=772)。很多聰明人花很多年調每個旋鈕，但很難，而且不知道是不是最佳的。

> 能不能用**端到端**（end-to-end）的方式決定這些：直接根據最終的率和失真，反推壓縮演算法和權重？[▶ 13:30](https://youtu.be/H7dvh35xNuE?t=810) 這就是機器學習的前提。

**學習式壓縮** = 用機器學習，靠 (1) 非線性轉換、(2) 端到端訓練，超越傳統壓縮器 [▶ 13:30](https://youtu.be/H7dvh35xNuE?t=810)。

### 3.3 這個領域

[▶ 14:05](https://youtu.be/H7dvh35xNuE?t=845) 早期論文：Toderici（CVPR 2015）、Theis（ICLR 2017）；之後非常多。很熱門的領域。

[▶ 14:39](https://youtu.be/H7dvh35xNuE?t=879) **CLIC**（Challenge on Learned Image Compression），在 Data Compression Conference 舉辦，大概第四或第五屆了，很多業界和學界參加，比誰的影像、影片壓縮器最好。今天只講基本想法 [▶ 14:39](https://youtu.be/H7dvh35xNuE?t=879)。

【投影片補充】`slide_16_2023.pdf` 列了一長串論文：[Toderici, CVPR15]、[Theis, ICLR17]、[Agustsson, NIPS17]、[Ballé, ICLR17]、[Rippel, ICML17]、[Ballé, ICLR18]、[Mentzer, CVPR18]、[Ballé, ICLR19]……以及影片的 [DVC, Lu et al. 2019] 等。

---

## 4. 機器學習 101

[▶ 15:21](https://youtu.be/H7dvh35xNuE?t=921) 給沒學過 ML 的人的五分鐘簡介（學過的可以跳過）。

### 4.1 三個元件

[▶ 15:56](https://youtu.be/H7dvh35xNuE?t=956)

1. **資料** $(x,y)$：例如 $x$ 是影像，$y$ 是「有沒有狗」的標籤 [▶ 16:34](https://youtu.be/H7dvh35xNuE?t=994)。
2. **可參數化、可微分的非線性模型** $\hat y=f_\theta(x)$ [▶ 17:05](https://youtu.be/H7dvh35xNuE?t=1025)：$\theta$ 是參數（像注水裡參數化率失真曲線的 $\theta$）。輸出 $\hat y$ 是模型認為的標籤 [▶ 17:40](https://youtu.be/H7dvh35xNuE?t=1060)。
3. **損失函數** $\mathcal L(y,\hat y)$ [▶ 18:15](https://youtu.be/H7dvh35xNuE?t=1095)：預測對不對。

### 4.2 訓練

[▶ 18:48](https://youtu.be/H7dvh35xNuE?t=1128) 用**反向傳播**（backpropagation）、梯度來學 $\theta$，叫**訓練**或**學習** [▶ 19:22](https://youtu.be/H7dvh35xNuE?t=1162)：

$$\min_\theta\ \mathcal L\left(y,f_\theta(x)\right),\qquad\theta\leftarrow\theta-\eta\,\nabla_\theta\mathcal L.$$

[▶ 19:57](https://youtu.be/H7dvh35xNuE?t=1197) 現代 ML 裡這通常是**非凸**最佳化，很難精確解；就用**梯度下降**，每一步沿梯度更新 $\theta$，重複下去 [▶ 20:34](https://youtu.be/H7dvh35xNuE?t=1234)。

### 4.3 兩個重點

[▶ 22:36](https://youtu.be/H7dvh35xNuE?t=1356)

1. **只要損失函數可微分，幾乎任何目標都能最佳化** [▶ 23:10](https://youtu.be/H7dvh35xNuE?t=1390)。$f$ 若有很多層，每層都要可微（鏈鎖律）[▶ 23:41](https://youtu.be/H7dvh35xNuE?t=1421)。

   > **對我們的意義：ML 和離散分布處不來** [▶ 23:41](https://youtu.be/H7dvh35xNuE?t=1421)。無損壓縮全是離散分布，不能直接塞進標準 ML 模型，必須處理熵編碼器的離散性。

2. **可以堆疊非線性層** [▶ 24:18](https://youtu.be/H7dvh35xNuE?t=1458)：線性層再怎麼疊還是一個矩陣（$ABC$ 仍是一個矩陣），沒有增加表達力；非線性層疊起來就不是 [▶ 24:54](https://youtu.be/H7dvh35xNuE?t=1494)。所以深度神經網路越疊越深、需要越多資料 [▶ 25:27](https://youtu.be/H7dvh35xNuE?t=1527)。

---

## 5. 自編碼器

[▶ 26:01](https://youtu.be/H7dvh35xNuE?t=1561) **自編碼器**（autoencoder）：

```
x ──[編碼器 φ]──> z（瓶頸，低維）──[解碼器 θ]──> x'
損失 = d(x, x')
```

- 不需要標籤，目標是**還原出和輸入一樣的東西** [▶ 26:34](https://youtu.be/H7dvh35xNuE?t=1594)。
- 編碼器把維度降到小小的**瓶頸** $z$（**潛在變數**，latent variables），解碼器再從 $z$ 解回來 [▶ 27:45](https://youtu.be/H7dvh35xNuE?t=1665)。

【課堂討論】[▶ 27:45](https://youtu.be/H7dvh35xNuE?t=1665) 這個架構讓你想到什麼？提示：看 $z$ 這個字。學生答：**很像壓縮問題** [▶ 28:22](https://youtu.be/H7dvh35xNuE?t=1702)。

[▶ 28:22](https://youtu.be/H7dvh35xNuE?t=1702) 網路被迫學一對編碼器／解碼器，讓低維瓶頸能重建出和輸入很像的影像。JPEG 也是：影像 → 盡量少的位元 → 解回很像的影像 [▶ 29:00](https://youtu.be/H7dvh35xNuE?t=1740)。自編碼器有幾十種基本變體、每種又有上百種變體 [▶ 29:00](https://youtu.be/H7dvh35xNuE?t=1740)。

---

## 6. 學習式影像壓縮的架構與損失函數

### 6.1 問題

[▶ 29:40](https://youtu.be/H7dvh35xNuE?t=1780) 目標影像 $I$ → 編碼成位元流 → 解碼成 $\hat I$ [▶ 30:14](https://youtu.be/H7dvh35xNuE?t=1814)：

$$\min\ d(I,\hat I)\quad\text{s.t.}\quad L(\text{bits})\le B.$$

### 6.2 傳統編碼器的三步

[▶ 30:14](https://youtu.be/H7dvh35xNuE?t=1814)（把 DCT 係數叫 $z$，對應潛在變數）

1. **DCT**：$z=\mathrm{DCT}(I)$，去相關。
2. **量化**：$\hat z=Q(z)$，這裡引入損失 [▶ 30:50](https://youtu.be/H7dvh35xNuE?t=1850)。
3. **算術編碼**：碼長 $L(\text{bits})\approx\log_2\frac1{P(\hat z)}$ [▶ 31:23](https://youtu.be/H7dvh35xNuE?t=1883)。

解碼：位元 → 離散的 $\hat z$ → IDCT → $\hat I$。DCT 和 IDCT 完全可逆，損失只在量化 [▶ 31:56](https://youtu.be/H7dvh35xNuE?t=1916)。

### 6.3 換成學出來的非線性轉換

[▶ 31:56](https://youtu.be/H7dvh35xNuE?t=1916) 把 DCT/IDCT 換成**深度前饋網路**（不管什麼架構，今天不談 ML 細節）[▶ 32:29](https://youtu.be/H7dvh35xNuE?t=1949)。希望它仍有能量集中的效果 [▶ 33:06](https://youtu.be/H7dvh35xNuE?t=1986)。

**損失函數** [▶ 33:06](https://youtu.be/H7dvh35xNuE?t=1986)：用 Lagrange 形式（$\lambda>0$ 用來取捨）[▶ 33:39](https://youtu.be/H7dvh35xNuE?t=2019)：

$$\mathcal L=\underbrace{L(\text{bits})}_{\text{率}}+\lambda\,\underbrace{d(I,\hat I)}_{\text{失真}}\approx\log_2\frac1{P(\hat z)}+\lambda\,d(I,\hat I).$$

[▶ 34:15](https://youtu.be/H7dvh35xNuE?t=2055) 所以 pipeline 需要一個**機率模型** $P(\hat z)$，才能訓練。

---

## 7. 兩個不可微分的地方與繞法

### 7.1 問題在哪【課堂討論】

[▶ 34:51](https://youtu.be/H7dvh35xNuE?t=2091) 直接對這個損失反向傳播，能端到端學嗎？訓練要什麼？**目標函數要可微分** [▶ 35:28](https://youtu.be/H7dvh35xNuE?t=2128)。

- 學生答：要先量化才能得到機率分布，**量化不可微分** [▶ 36:04](https://youtu.be/H7dvh35xNuE?t=2164)。
- 講者：還有一個：**$\log\frac1{P(\hat z)}$ 也要能求梯度**，但 $\hat z$ 是離散的，$P(\hat z)$ 其實是一張**表** [▶ 36:39](https://youtu.be/H7dvh35xNuE?t=2199)、[▶ 37:14](https://youtu.be/H7dvh35xNuE?t=2234)。

### 7.2 繞法一：量化 = 加均勻雜訊 + 直通估計

[▶ 37:14](https://youtu.be/H7dvh35xNuE?t=2234) 量化先當成簡單的**取整**（純量量化）。訓練時：

- **前向**：把量化當成**加上獨立的均勻雜訊** $U(-0.5,0.5)$（2.3 → 2、3.7 → 4，誤差都在 ±0.5 以內）[▶ 37:57](https://youtu.be/H7dvh35xNuE?t=2277)：$\tilde z=z+u$。
- **反向**：**直通估計器**（straight-through estimator）：當量化層不存在，$\frac{d\hat z}{dz}=1$ [▶ 38:30](https://youtu.be/H7dvh35xNuE?t=2310)。

[▶ 38:30](https://youtu.be/H7dvh35xNuE?t=2310) 這是**假設**，沒有證明，但實驗上效果極好。處理任何離散步驟的**第一招**：當成連續變數加雜訊，梯度直接穿過 [▶ 39:06](https://youtu.be/H7dvh35xNuE?t=2346)。

### 7.3 繞法二：用 CDF 參數化機率模型

[▶ 39:06](https://youtu.be/H7dvh35xNuE?t=2346) 更大的問題：$P(\hat z)$ 是張表，怎麼對它微分？[▶ 39:40](https://youtu.be/H7dvh35xNuE?t=2380) 業界的巧妙繞法（也是假設）：**用一個密度函數參數化** $P(\hat z)$。例如假設是標準高斯 [▶ 40:14](https://youtu.be/H7dvh35xNuE?t=2414)：

$$P(\hat z)=\Phi(\hat z+0.5)-\Phi(\hat z-0.5),$$

$\Phi$ 是 $\mathcal N(0,1)$ 的 **CDF**。$\hat z$ 是取整來的，$\pm0.5$ 之間只有它這個整數 [▶ 40:47](https://youtu.be/H7dvh35xNuE?t=2447)。現在可以微分了，因為 CDF 可微 [▶ 41:29](https://youtu.be/H7dvh35xNuE?t=2489)：

$$\frac{dP(\hat z)}{d\hat z}=\phi(\hat z+0.5)-\phi(\hat z-0.5),$$

$\phi$ 是 PDF。[▶ 41:29](https://youtu.be/H7dvh35xNuE?t=2489) 圖：實線是高斯 PDF，點是 $\Phi(\hat z+0.5)-\Phi(\hat z-0.5)$，大致模仿高斯形狀。也就是**強迫**離散的 $\hat z$ 看起來像高斯分布 [▶ 42:07](https://youtu.be/H7dvh35xNuE?t=2527)。

【Q&A】[▶ 42:39](https://youtu.be/H7dvh35xNuE?t=2559) 學生問：可以這樣做，是因為反正要學，乾脆學成高斯？講者：很好的問題。**$P$ 選什麼都可以**，因為訓練時損失裡有 $\log\frac1{P(\hat z)}$ [▶ 43:16](https://youtu.be/H7dvh35xNuE?t=2596)：

- 實際產生的 $\hat z$ 分布和模型分布一樣時，$\log\frac1P$ 的期望最小（回想 KL 散度：用錯分布壓縮要多付 $D(p\|q)$）[▶ 43:51](https://youtu.be/H7dvh35xNuE?t=2631)。
- 所以最小化損失時，編碼器、解碼器的參數會自己調整，**讓輸出的 $\hat z$ 去模仿你選的分布** [▶ 44:24](https://youtu.be/H7dvh35xNuE?t=2664)。

[▶ 44:24](https://youtu.be/H7dvh35xNuE?t=2664) 為什麼選高斯？好處理。[▶ 45:00](https://youtu.be/H7dvh35xNuE?t=2700) 而且這裡不只假設高斯，還假設 $\mathcal N(0,1)$：每個離散符號 iid、平均 0、變異數 1。明顯能改進：讓平均和變異數可調、每個潛在變數各有自己的 [▶ 45:33](https://youtu.be/H7dvh35xNuE?t=2733)。

[▶ 45:33](https://youtu.be/H7dvh35xNuE?t=2733) 這樣從 $\hat I$ 一路到 $I$ 每個運算都能求梯度了 [▶ 46:07](https://youtu.be/H7dvh35xNuE?t=2767)。

---

## 8. 直覺：率項和失真項在拔河

【課堂討論】[▶ 46:40](https://youtu.be/H7dvh35xNuE?t=2800) **如果損失裡沒有失真項**，只最小化 $\log\frac1{P(\hat z)}$（$P$ 是上面的高斯 CDF 差），$\hat z$ 會長怎樣？

- [▶ 47:54](https://youtu.be/H7dvh35xNuE?t=2874) 最小化 $\log\frac1P$ = 最大化 $P(\hat z)$；高斯的話什麼時候最大？學生答：**0** [▶ 48:27](https://youtu.be/H7dvh35xNuE?t=2907)。所有 $\hat z$ 都會變成 0。
- [▶ 49:02](https://youtu.be/H7dvh35xNuE?t=2942) 為什麼實務上不這樣？學生答：**會丟掉所有資訊** [▶ 49:02](https://youtu.be/H7dvh35xNuE?t=2942)。$\hat z$ 全是 0，率是 0、什麼都不用傳，解碼器只能輸出一個固定值，完全有損 [▶ 49:38](https://youtu.be/H7dvh35xNuE?t=2978)。

[▶ 49:38](https://youtu.be/H7dvh35xNuE?t=2978) 所以 ML 壓縮器有誘因把 $\hat z$ **散開**，解碼器才有東西可用；這是**失真項**在保證 [▶ 50:14](https://youtu.be/H7dvh35xNuE?t=3014)。

> 率項把 $\hat z$ 往 0 推；失真項說「不行，失真會太大」。**$\lambda$ 決定怎麼取捨率和失真** [▶ 50:54](https://youtu.be/H7dvh35xNuE?t=3054)。

**總結** [▶ 50:54](https://youtu.be/H7dvh35xNuE?t=3054)：兩個問題 (1) 量化是離散運算 → 前向加雜訊、反向直通；(2) 機率表 → 假設一個能反向傳播的分布，編解碼器會學著輸出差不多分布的 $\hat z$；率和失真兩項自動決定 $\hat z$ 要多散 [▶ 51:25](https://youtu.be/H7dvh35xNuE?t=3085)。

【Q&A】[▶ 51:58](https://youtu.be/H7dvh35xNuE?t=3118) 學生問：量化的方式也可以學嗎？講者：可以，但這裡沒做 [▶ 52:30](https://youtu.be/H7dvh35xNuE?t=3150)。可以用強化學習：例如 MuZero 相關的工作，用 RL 做率失真取捨，在不同的離散選項中挑 [▶ 52:30](https://youtu.be/H7dvh35xNuE?t=3150)。另一個想法：影像由很多區塊組成，為什麼全用同一個量化矩陣？有些區塊很一致、有些很複雜，可以每個區塊不同取捨，整體更好 [▶ 53:14](https://youtu.be/H7dvh35xNuE?t=3194)。但用 RL 計算量很快就很大 [▶ 53:47](https://youtu.be/H7dvh35xNuE?t=3227)。

---

## 9. Notebook 示範：MNIST 壓縮器

### 9.1 架構

[▶ 53:47](https://youtu.be/H7dvh35xNuE?t=3227) 為 MNIST 手寫數字做一個學習式壓縮器（只描述程式）：

- 編碼器、解碼器也叫**分析轉換**（analysis transform）和**合成轉換**（synthesis transform）[▶ 54:19](https://youtu.be/H7dvh35xNuE?t=3259)：編碼器分析影像給出潛在變數，解碼器從瓶頸合成影像。
- 用 Keras 定義：分析轉換是一些**卷積層** + Leaky ReLU 非線性，從影像尺寸降到小得多的潛在維度 [▶ 54:52](https://youtu.be/H7dvh35xNuE?t=3292)；合成轉換從潛在維度用轉置卷積（Conv2DTranspose）升取樣回去 [▶ 55:32](https://youtu.be/H7dvh35xNuE?t=3332)。
- 共約 **100 萬個可訓練參數**：$\theta$ 是 100 萬維的 [▶ 56:02](https://youtu.be/H7dvh35xNuE?t=3362)。

[▶ 56:35](https://youtu.be/H7dvh35xNuE?t=3395) **未訓練**時：影像 → 分析轉換 $y$ → 合成轉換 $\tilde x$，失真用 L1（也可以用 L2）。重建是亂的，理所當然 [▶ 57:08](https://youtu.be/H7dvh35xNuE?t=3428)。

### 9.2 訓練

[▶ 57:08](https://youtu.be/H7dvh35xNuE?t=3428) 損失：率 $=-\log_2\left[\Phi(\tilde y+0.5)-\Phi(\tilde y-0.5)\right]$，再加 $\lambda\times$ 失真。訓練器 [▶ 57:39](https://youtu.be/H7dvh35xNuE?t=3459)：

1. 前處理影像。
2. 分析轉換得 $y$。
3. **加均勻雜訊** $\tilde y=y+u$（繞法一）[▶ 58:17](https://youtu.be/H7dvh35xNuE?t=3497)。
4. 用兩個 CDF 相減算機率、取負對數得到**率損失**（繞法二）[▶ 58:50](https://youtu.be/H7dvh35xNuE?t=3530)。
5. 合成轉換 $\tilde x=g(\tilde y)$ [▶ 58:50](https://youtu.be/H7dvh35xNuE?t=3530)。
6. 總損失 = 率損失 + $\lambda\times$ 失真損失（$|x-\tilde x|$）[▶ 59:27](https://youtu.be/H7dvh35xNuE?t=3567)。

[▶ 1:00:04](https://youtu.be/H7dvh35xNuE?t=3604) 取 $\lambda=2000$、潛在維度 50（MNIST 是 28×28，從 784 維變 50 維）。現場訓練：總損失一直下降；**率損失一開始反而上升**，這沒問題，因為最佳化的是率 + $\lambda\times$ 失真，這個 $\lambda$ 下一開始比較在意失真 [▶ 1:00:35](https://youtu.be/H7dvh35xNuE?t=3635)。跑 15 個 epoch [▶ 1:01:49](https://youtu.be/H7dvh35xNuE?t=3709)。

### 9.3 真的去壓

[▶ 1:01:12](https://youtu.be/H7dvh35xNuE?t=3672) 訓練只是為了找權重；真正的壓縮器回到一般流程：編碼器 → 量化（真的取整）→ $\hat z$ → 假設機率 $P(\hat z)$ → **真的用算術編碼器** [▶ 1:01:49](https://youtu.be/H7dvh35xNuE?t=3709)。用 SCL 的算術編碼器（作業 3 第 4 題那個 context 自適應編碼器，這裡不自適應）[▶ 1:02:20](https://youtu.be/H7dvh35xNuE?t=3740)。

觀察：

- 實際的 $\hat z$ 頻率表：大部分是 0，往兩邊遞減，大致像我們希望的高斯 [▶ 1:03:38](https://youtu.be/H7dvh35xNuE?t=3818)。
- **實際碼率和估計碼率非常接近** [▶ 1:04:17](https://youtu.be/H7dvh35xNuE?t=3857)：實際是真的熵編碼的結果，估計是 $\log\frac1{P(\hat z)}$；算術編碼只多不到 2 位元，兩者都在 2 位元內 [▶ 1:04:56](https://youtu.be/H7dvh35xNuE?t=3896)。
- 重建：例如一個 5，只用 **89 位元**就解出很像的 5 [▶ 1:04:56](https://youtu.be/H7dvh35xNuE?t=3896)。28×28 黑白影像約 900 位元，學出來的壓縮器約 90 位元就重建得很像 [▶ 1:05:29](https://youtu.be/H7dvh35xNuE?t=3929)。不用設計任何手工參數，也不用事先知道有 DCT 這種東西 [▶ 1:06:07](https://youtu.be/H7dvh35xNuE?t=3967)。
- [▶ 1:06:43](https://youtu.be/H7dvh35xNuE?t=4003) 那張圖再看一次：藍線是標準常態 PDF、紅點是模型的量化 PDF（CDF 差）、**綠點是實際的經驗機率**：不完全一樣，但大致跟著紅點 [▶ 1:07:21](https://youtu.be/H7dvh35xNuE?t=4041)。

### 9.4 改變 $\lambda$【課堂討論】

[▶ 1:07:21](https://youtu.be/H7dvh35xNuE?t=4041) 學習式壓縮器的一個麻煩：**每個 $\lambda$ 要訓練一次**；換 $\lambda$，學到的率就不同 [▶ 1:07:56](https://youtu.be/H7dvh35xNuE?t=4076)。$\lambda$ 從 2000 降到 500，重建會更有損還是更少損？幾乎所有人說**更有損** [▶ 1:08:31](https://youtu.be/H7dvh35xNuE?t=4111)。對：失真的權重變小了，等於說「多一點失真沒關係，把率降下來」[▶ 1:09:02](https://youtu.be/H7dvh35xNuE?t=4142)。

[▶ 1:11:20](https://youtu.be/H7dvh35xNuE?t=4280) 結果：每張圖約 **40 位元**（率確實降了），但有些地方品質變差，例如 8 和 5 [▶ 1:11:53](https://youtu.be/H7dvh35xNuE?t=4313)。另外這些 ML 壓縮器做了很多**低通濾波**（平滑），可以預期，因為高頻很難編 [▶ 1:11:53](https://youtu.be/H7dvh35xNuE?t=4313)。

---

## 10. 好處

[▶ 1:09:38](https://youtu.be/H7dvh35xNuE?t=4178)

1. **不用手調參數**，可以學 [▶ 1:09:38](https://youtu.be/H7dvh35xNuE?t=4178)：
   - **自適應**：傳統編碼器永遠用同樣的矩陣；現在可以每個領域一個自訂的編碼器（卡通、遊戲、電視劇），各學各的轉換。
   - 可以**依內容**、甚至**依任務**訓練 [▶ 1:10:13](https://youtu.be/H7dvh35xNuE?t=4213)。
2. **失真模型分離得更好** [▶ 1:10:13](https://youtu.be/H7dvh35xNuE?t=4213)：失真只要可微分，什麼都行。剛剛用 L1，也可以用 L2，或任何**更符合人類感知**的可微分失真 [▶ 1:10:44](https://youtu.be/H7dvh35xNuE?t=4244)。傳統編碼器很難這樣做，因為很多手工決定都假設在最佳化 MSE 或 PSNR [▶ 1:11:20](https://youtu.be/H7dvh35xNuE?t=4280)。下一講會談一點。

---

## 11. 現況與問題

### 11.1 已經是最先進的

[▶ 1:12:34](https://youtu.be/H7dvh35xNuE?t=4354) 一篇 2022 年的論文的基準測試：橫軸位元／像素（越右率越高），縱軸 PSNR 或 MS-SSIM（品質指標，越高越好）[▶ 1:12:34](https://youtu.be/H7dvh35xNuE?t=4354)。

- 棕色：JPEG；粉紅虛線：BPG [▶ 1:13:11](https://youtu.be/H7dvh35xNuE?t=4391)。
- 棕色虛線：**VVC/VTM**，最先進的傳統編碼器之一（甚至在中間用了一些 ML 元件做小決策，但不是端到端學習）[▶ 1:13:46](https://youtu.be/H7dvh35xNuE?t=4426)。
- 藍色：他們的**學習式影像壓縮器**，在左上角（低率高品質），**最好** [▶ 1:13:46](https://youtu.be/H7dvh35xNuE?t=4426)。

[▶ 1:14:24](https://youtu.be/H7dvh35xNuE?t=4464) VVC 是大團隊 5–10 年對各元件的研究，學習式壓縮器一來就贏了。**MS-SSIM**（另一個指標，和人眼的相關性比較好）上差距更大 [▶ 1:14:24](https://youtu.be/H7dvh35xNuE?t=4464)；PSNR 就是用 dB 表示的 MSE。很多傳統編碼器是為 PSNR 最佳化的 [▶ 1:15:04](https://youtu.be/H7dvh35xNuE?t=4504)。

### 11.2 為什麼還沒到處都是？

[▶ 1:15:38](https://youtu.be/H7dvh35xNuE?t=4538) 主要問題：**速度** [▶ 1:15:38](https://youtu.be/H7dvh35xNuE?t=4538)。這門課一直想強調：**複雜度**決定一個方法實不實用、會不會被部署，因為壓縮是無所不在、一直在跑的運算 [▶ 1:16:17](https://youtu.be/H7dvh35xNuE?t=4577)。

- George Toderici 在 CVPR 2020 的演講截圖：H.266 + 增強（比 JPEG 更耗計算的傳統編碼器）vs. 當時的 ML 編碼器，**計算量多約 20 倍** [▶ 1:16:17](https://youtu.be/H7dvh35xNuE?t=4577)。
- 20 倍聽起來還好，但原本 1 小時要變 20 小時，1 分鐘要變 20 分鐘；你會用嗎？[▶ 1:16:51](https://youtu.be/H7dvh35xNuE?t=4611)

**但硬體在追** [▶ 1:17:22](https://youtu.be/H7dvh35xNuE?t=4642)：深度神經網路橫掃世界，不只壓縮，手機上一大堆應用，所以大量工作在做**神經網路的硬體支援**，壓縮也能搭便車 [▶ 1:17:58](https://youtu.be/H7dvh35xNuE?t=4678)。

【口頭】[▶ 1:17:58](https://youtu.be/H7dvh35xNuE?t=4678) 很多傳統的影像、影片編碼器在你的電腦裡**也有硬體支援**：Intel 做晶片讓影像、影片能在硬體上有效率地解碼，否則用一般硬體達不到要的速度 [▶ 1:18:34](https://youtu.be/H7dvh35xNuE?t=4714)。這決定你看 YouTube、Netflix 時那個轉圈圈是 1 秒還是 1 分鐘。AI 晶片的版圖有上百家公司 [▶ 1:19:07](https://youtu.be/H7dvh35xNuE?t=4747)：Qualcomm 有很有效率的 ML 推論晶片、Apple 的 M3、Nvidia 的 GPU 也在做 [▶ 1:19:07](https://youtu.be/H7dvh35xNuE?t=4747)。

**第二個問題：確定性** [▶ 1:19:41](https://youtu.be/H7dvh35xNuE?t=4781)：不同硬體的浮點運算實作可能不同，會造成災難性的失敗。CPU 界已經統一了，GPU 界還在統一，每次 Nvidia 更新都要小心 [▶ 1:19:41](https://youtu.be/H7dvh35xNuE?t=4781)。**必須在不同機器、平台上可重現**，不然解出來的不是你以為的東西 [▶ 1:20:14](https://youtu.be/H7dvh35xNuE?t=4814)。（呼應第 9 集：編碼器和解碼器必須給出完全一樣的機率。）

### 11.3 總結

[▶ 1:20:14](https://youtu.be/H7dvh35xNuE?t=4814)（`slide_16_2023.pdf` 最後一頁）

- ML 編碼器：學出來的編解碼轉換、對選定機率模型的保真度更好 → 更好的率失真。
- 失真只要可微分，選什麼都行：明天有更好的視覺模型，就能做出更好的壓縮器 [▶ 1:20:14](https://youtu.be/H7dvh35xNuE?t=4814)。
- 可以依領域自適應、很有彈性。
- 關鍵是能對**量化**和**離散機率模型**微分。
- 未來的壓縮器很可能越來越多 ML 編碼器。非常熱門的領域，歡迎參與 [▶ 1:20:51](https://youtu.be/H7dvh35xNuE?t=4851)。

---

## 12. 一頁速查表

### 動機

| 傳統（JPEG/BPG） | 學習式 |
|---|---|
| 線性轉換（DCT、DWT） | 非線性轉換（神經網路），可配合香蕉形分布 |
| 手調量化表、區塊大小 | 端到端學習 |
| 為 MSE/PSNR 設計 | 任何可微分失真 |

### 架構（分析 / 合成轉換）

$$z=g_a(I),\quad\hat z=\mathrm{round}(z),\quad\hat I=g_s(\hat z),\qquad\mathcal L=\log_2\frac1{P(\hat z)}+\lambda\,d(I,\hat I)$$

### 兩個繞法

| 問題 | 訓練時的繞法 |
|---|---|
| 量化不可微 | 前向：$\tilde z=z+U(-\frac12,\frac12)$；反向：直通（梯度 = 1） |
| $P(\hat z)$ 是一張表 | $P(\hat z)=\Phi(\hat z+\frac12)-\Phi(\hat z-\frac12)$，可微 |

**關鍵一步**：選什麼 $P$ 都行，因為最小化 $\mathbb{E}\log\frac1P$ 會逼 $\hat z$ 的實際分布去配合 $P$（用錯分布的代價是 KL 散度）。

### 直覺

- 只有率項 ⇒ 全部 $\hat z=0$ ⇒ 什麼都沒傳。
- 失真項把 $\hat z$ 撐開；$\lambda$ 小 ⇒ 率低、失真大（MNIST：$\lambda$ 2000 → 500，約 89 → 40 位元）。
- 每個 $\lambda$ 要各訓練一個模型。
- 部署時：真的取整 + 真的算術編碼；實際碼率 ≈ 估計碼率（差 2 位元內）。

### 現況

- 基準：學習式 > VVC > BPG > JPEG（PSNR、MS-SSIM 皆然）。
- 問題：速度（約 20× 計算）、跨硬體的確定性；硬體加速正在追上。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 可微分的感知失真、MS-SSIM、PSNR 的問題 | 第 17 集 Humans and Compression |
| 學習式影片壓縮（DVC 等） | 第 18 集影片壓縮 |
| 硬體解碼器 | 第 18 集 |
| 編解碼器機率必須完全一致 | 回顧第 9 集自適應算術編碼 |

> 以上對應是依播放清單標題和本集內容推估的，做到時再更新。

---

## 附：本集一句話總結

> **學習式影像壓縮把 DCT/IDCT 換成神經網路的分析／合成轉換，直接最小化「率 + $\lambda\times$ 失真」：率用 $\log\frac1{P(\hat z)}$ 估計。訓練時量化不可微，就前向加均勻雜訊、反向直通；機率表不可微，就假設 $P(\hat z)=\Phi(\hat z+\frac12)-\Phi(\hat z-\frac12)$，讓網路自己學著輸出符合這個分布的潛在變數。率項把潛在變數往 0 推、失真項把它撐開。它已經在基準上勝過最好的傳統編碼器，也能用任何可微分（包括感知）失真，但計算量和跨硬體的確定性仍是部署的障礙。**

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 16 錄影逐字稿（人工字幕，1:21:18）與投影片 slide_16_2023 整理。*
