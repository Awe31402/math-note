---
course: Stanford EE274 Data Compression  Theory and Applications（2023 秋）
episode: 18
lecture: Lecture 18
date: 2023-12-04
video: https://youtu.be/uKnEZKpZKVA
notes: 投影片 L18.pdf、L18_conclusion.pdf；課本沒有影片壓縮
---

# 第 18 集 · Lecture 18：影片壓縮（Video Compression） [▶ 影片](https://youtu.be/uKnEZKpZKVA)

← 上一集：[17-humans-and-compression](17-humans-and-compression.md) ｜ [總目錄](README.md) ｜ 下一集：無（本課最後一集）

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 18 集
> **講者**：客座講者 Kedar Tatwawadi（影片壓縮）；Shubham Chandak（開場介紹、課程總結）
> **來源**：YouTube 錄影逐字稿（1:08:39，人工字幕 en-US）＋ 投影片 `L18.pdf`、`L18_conclusion.pdf`。課本沒有這部分。
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
- [1. 為什麼影片壓縮這麼重要](#1-為什麼影片壓縮這麼重要)
- [2. 影片是什麼：解析度、FPS、原始位元率](#2-影片是什麼解析度fps原始位元率)
- [3. 用 H.264 壓壓看](#3-用-h264-壓壓看)
- [4. 想法一：每張畫面獨立壓（I-frame）](#4-想法一每張畫面獨立壓i-frame)
- [5. 想法二：用前一張預測（P-frame）](#5-想法二用前一張預測p-frame)
- [6. 怎麼找運動：區塊匹配](#6-怎麼找運動區塊匹配)
- [7. 實際看編碼後的檔案](#7-實際看編碼後的檔案)
- [8. 想法三：前後都參考（B-frame）](#8-想法三前後都參考b-frame)
- [9. 三種模式與延遲](#9-三種模式與延遲)
- [10. 區塊運動的問題與學習式影片編碼](#10-區塊運動的問題與學習式影片編碼)
- [11. 課程總結（Shubham）](#11-課程總結shubham)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 整門課的連結](#13-整門課的連結)

---

## 0. 這堂課要做什麼

[▶ 00:06](https://youtu.be/uKnEZKpZKVA?t=6) Shubham 介紹客座講者 **Kedar Tatwawadi**：2020 年在 Tsachy Weissman 指導下拿到 Stanford 博士，之後在影片壓縮新創 **WaveOne** 工作，現在在 **Apple** [▶ 00:43](https://youtu.be/uKnEZKpZKVA?t=43)。整門課常聽到他的名字：這門課和 Stanford Compression Library 都是他起頭的，Pulkit 和 Shubham 後來加入。

[▶ 01:21](https://youtu.be/uKnEZKpZKVA?t=81) Kedar：前面學了文字、log、基因資料的無損壓縮，以及影像壓縮（作業 4 有一題 JPEG 風格的壓縮器）；今天把這些用在**最後的、大概也是最重要的領域：影片壓縮**。今天講得比較高層次 [▶ 02:01](https://youtu.be/uKnEZKpZKVA?t=121)。

---

## 1. 為什麼影片壓縮這麼重要

[▶ 02:01](https://youtu.be/uKnEZKpZKVA?t=121) 影片的產生和消費量非常驚人（投影片的數字是幾年前的）[▶ 02:40](https://youtu.be/uKnEZKpZKVA?t=160)。

**影片編碼標準** [▶ 02:40](https://youtu.be/uKnEZKpZKVA?t=160)：

| 標準 | 說明 |
|---|---|
| **H.264**（AVC） | 最常見，大約 15–20 年了，但幾乎所有裝置都支援 [▶ 03:17](https://youtu.be/uKnEZKpZKVA?t=197) |
| H.265（HEVC） | 較新，約 5–10 年前 |
| H.266（VVC） | 還在發展，裝置上大多還沒有 [▶ 03:49](https://youtu.be/uKnEZKpZKVA?t=229) |
| VP9、AV1 | 其他家族（投影片） |

[▶ 03:49](https://youtu.be/uKnEZKpZKVA?t=229) 影片壓縮重要又**耗計算**，所以編碼、解碼都被做進**晶片**：例如 Apple M2 晶片上有一塊**媒體引擎**專做影片編解碼 [▶ 04:26](https://youtu.be/uKnEZKpZKVA?t=266)。很多博士論文就在把編碼器最佳化到每一毫秒、放上晶片；今天不談這部分 [▶ 05:13](https://youtu.be/uKnEZKpZKVA?t=313)。

---

## 2. 影片是什麼：解析度、FPS、原始位元率

[▶ 05:46](https://youtu.be/uKnEZKpZKVA?t=346) 影片就是**一連串畫面（影像）**，所以叫 motion pictures [▶ 05:46](https://youtu.be/uKnEZKpZKVA?t=346)。

【口頭】[▶ 06:24](https://youtu.be/uKnEZKpZKVA?t=384) **第一支影片就是在 Stanford 校園拍的**：Leland Stanford 的馬，大概 12 張照片，目的是知道馬奔跑時是否有一瞬間四腳離地。

[▶ 06:58](https://youtu.be/uKnEZKpZKVA?t=418) 今天的範例影片：**騎師**（jockey），又是一匹馬。兩個數字 [▶ 07:38](https://youtu.be/uKnEZKpZKVA?t=458)：

- **解析度**：720p（$1280\times720$）。
- **FPS**（frames per second）：30。現在很多影片是 60 FPS [▶ 07:38](https://youtu.be/uKnEZKpZKVA?t=458)。

[▶ 08:13](https://youtu.be/uKnEZKpZKVA?t=493) 拍個 5–10 分鐘就是很大的檔案。

**MediaInfo 看原始檔**（`.y4m` 原始影片格式）[▶ 08:48](https://youtu.be/uKnEZKpZKVA?t=528)：解析度 1280×720、30 FPS、色彩格式 **YUV 4:2:0**（Pulkit 講過）、**位元率 332 Mb/s** [▶ 08:48](https://youtu.be/uKnEZKpZKVA?t=528)。

[▶ 09:30](https://youtu.be/uKnEZKpZKVA?t=570) 家裡大概 100 Mb/s 的網路，根本播不了 [▶ 09:30](https://youtu.be/uKnEZKpZKVA?t=570)。這還是小影片，Netflix 看 4K 更大。

> 以下**不是逐字稿內容**，是驗算 332 Mb/s：4:2:0 時每像素平均 $1+\frac14+\frac14=1.5$ 個樣本，每樣本 8 位元，所以每張畫面 $1280\times720\times1.5\times8\approx11.06$ Mb，乘 30 FPS $\approx332$ Mb/s。

---

## 3. 用 H.264 壓壓看

[▶ 10:05](https://youtu.be/uKnEZKpZKVA?t=605) 用 **FFmpeg**（常用的影片處理工具），以 **x264**（H.264 的一個編碼器實作）壓縮 [▶ 10:05](https://youtu.be/uKnEZKpZKVA?t=605)。

**CRF**（Constant Rate Factor）是品質參數；**CRF 20 通常是人眼看不出差別**的程度 [▶ 10:40](https://youtu.be/uKnEZKpZKVA?t=640)。

| 設定 | 位元率 | PSNR（投影片） | 觀察 |
|---|---|---|---|
| 原始 | 332 Mb/s | — | |
| x264 CRF 20 | **6.2 Mb/s**（約 50×）[▶ 11:12](https://youtu.be/uKnEZKpZKVA?t=672) | 43 dB | 幾乎看不出假影（噴泉可能有一點） |
| x264 CRF 40 | 0.8 Mb/s [▶ 11:45](https://youtu.be/uKnEZKpZKVA?t=705) | 33 dB | 騎師的頭、馬腿有明顯方塊假影 [▶ 11:45](https://youtu.be/uKnEZKpZKVA?t=705) |

[▶ 12:24](https://youtu.be/uKnEZKpZKVA?t=744) 接下來用前面學過的東西，特別是把**影像壓縮當黑盒子**，看怎麼做到 50 倍 [▶ 12:56](https://youtu.be/uKnEZKpZKVA?t=776)。

---

## 4. 想法一：每張畫面獨立壓（I-frame）

【課堂討論】[▶ 12:56](https://youtu.be/uKnEZKpZKVA?t=776) 手上有影像壓縮器（例如作業的 JPEG），第一件事做什麼？學生答：**每張畫面獨立壓** [▶ 13:28](https://youtu.be/uKnEZKpZKVA?t=808)。

> **I-frame**：獨立當成影像壓縮的畫面 [▶ 13:28](https://youtu.be/uKnEZKpZKVA?t=808)。全部用 I-frame 叫 **I-frame 壓縮**。

[▶ 14:02](https://youtu.be/uKnEZKpZKVA?t=842) 結果：騎師影片只用 H.264 的 I-frame 壓縮，CRF 20 是 **9 Mb/s**（投影片：PSNR 44），比完整 H.264 的 6.2 差，但已經不錯 [▶ 14:02](https://youtu.be/uKnEZKpZKVA?t=842)。這支影片運動很多；運動少的影片只用 I-frame 會差很多（等一下會看到）[▶ 14:43](https://youtu.be/uKnEZKpZKVA?t=883)。

---

## 5. 想法二：用前一張預測（P-frame）

### 5.1 想法【課堂討論】

[▶ 14:43](https://youtu.be/uKnEZKpZKVA?t=883) 提示：**壓縮就是去除冗餘**，有相關就要去相關 [▶ 15:20](https://youtu.be/uKnEZKpZKVA?t=920)。兩張相鄰畫面來回切換，學生答：**畫面之間有相關**，先編第一張，第二張很多部分一樣 [▶ 15:52](https://youtu.be/uKnEZKpZKVA?t=952)。

[▶ 15:52](https://youtu.be/uKnEZKpZKVA?t=952) Kedar：對。第 1 張大部分只是往某個方向移了一點，可以直接複製；有一點差異，再用影像壓縮編那點差異 [▶ 16:27](https://youtu.be/uKnEZKpZKVA?t=987)。

### 5.2 流程

[▶ 16:27](https://youtu.be/uKnEZKpZKVA?t=987)

1. Frame 0（已編碼、解碼）。
2. 找 Frame 0 到 Frame 1 的**運動**（motion）。（畫面上的 logo 不動，那是另一回事。）
3. 把運動套到 Frame 0 上，得到**運動補償畫面**（motion-compensated frame）[▶ 16:27](https://youtu.be/uKnEZKpZKVA?t=987)。
4. 和真正的 Frame 1 相減，得到**殘差**（residual），用影像壓縮編 [▶ 17:00](https://youtu.be/uKnEZKpZKVA?t=1020)。

```
已解碼的前一張 ──[套用運動]──> 運動補償畫面
目前畫面 − 運動補償畫面 = 殘差 ──[影像壓縮]──> 位元
運動 ──[編碼]──> 位元
```

[▶ 17:00](https://youtu.be/uKnEZKpZKVA?t=1020) 能成立是因為 FPS 夠高：相隔 $\frac1{30}$ 秒的兩張畫面通常差不多 [▶ 17:00](https://youtu.be/uKnEZKpZKVA?t=1020)。

> **P-frame**（predicted frame）[▶ 17:34](https://youtu.be/uKnEZKpZKVA?t=1054)：根據前一張**已編碼**畫面預測的畫面。第一張是 I-frame，第二張依第一張、第三張依第二張……

[▶ 17:34](https://youtu.be/uKnEZKpZKVA?t=1054) 每次預測都會累積一點雜訊，越來越貴，所以每隔一段**插入新的 I-frame 刷新**；或場景變了（例如馬跑過時有東西擋在中間）也插入 I-frame [▶ 18:10](https://youtu.be/uKnEZKpZKVA?t=1090)。

**keyint**：兩個 I-frame（key frame）之間的距離，這個例子是 6 [▶ 18:10](https://youtu.be/uKnEZKpZKVA?t=1090)。

### 5.3 為什麼比較好？【課堂討論】

[▶ 18:42](https://youtu.be/uKnEZKpZKVA?t=1122) I-frame 壓縮也是用影像壓縮；這裡多了運動補償，最後還是影像壓縮。為什麼會比較好？

學生答：**殘差很小，大多是空白** [▶ 19:16](https://youtu.be/uKnEZKpZKVA?t=1156)。Kedar：對。影像壓縮的效果取決於影像本身：簡單的影像好壓，複雜的影像要很多位元 [▶ 19:47](https://youtu.be/uKnEZKpZKVA?t=1187)。殘差大部分是空白，用 JPEG 這類方法就能壓得好很多。**在用影像壓縮之前，先把所有相關性抽掉**，大多數影片編碼器都這樣做 [▶ 19:47](https://youtu.be/uKnEZKpZKVA?t=1187)。

---

## 6. 怎麼找運動：區塊匹配

[▶ 20:24](https://youtu.be/uKnEZKpZKVA?t=1224) 運動的**編碼**今天不多講（和課堂學的類似），講怎麼**找**運動 [▶ 21:03](https://youtu.be/uKnEZKpZKVA?t=1263)：

> **區塊匹配**（block matching）：取參考畫面裡的一個區塊，在另一張畫面上移動它，看在哪裡最匹配；匹配到的位置就是**運動向量**（motion vector）[▶ 21:03](https://youtu.be/uKnEZKpZKVA?t=1263)。

細節看演算法：區塊多大、怎麼搜尋 [▶ 21:37](https://youtu.be/uKnEZKpZKVA?t=1297)。【口頭】[▶ 21:03](https://youtu.be/uKnEZKpZKVA?t=1263) Stanford 以前 Bernd Girod 的課網站上有很多好資源，想深入的人可以看。

**搜尋策略** [▶ 22:14](https://youtu.be/uKnEZKpZKVA?t=1334)：

- **全搜尋**（full search）：搜整張圖，很貴。
- **階層式搜尋**（hierarchical search）[▶ 22:14](https://youtu.be/uKnEZKpZKVA?t=1334)：先把畫面降取樣（例如 4 倍）在小圖上匹配，找到粗略位置後再到較高解析度細找……多尺度讓問題可解 [▶ 22:51](https://youtu.be/uKnEZKpZKVA?t=1371)。很多影像、影片處理都用類似的**影像金字塔**。

找到後，每個區塊編它的運動（向量差）[▶ 22:51](https://youtu.be/uKnEZKpZKVA?t=1371)。

---

## 7. 實際看編碼後的檔案

### 7.1 每張畫面用的位元

[▶ 23:31](https://youtu.be/uKnEZKpZKVA?t=1411) 用一個串流分析軟體（字幕作「[? Stream-I ?]」）看一支比較簡單的影片 [▶ 24:21](https://youtu.be/uKnEZKpZKVA?t=1461)：長條圖是每張畫面用的位元數。

【課堂討論】[▶ 24:21](https://youtu.be/uKnEZKpZKVA?t=1461) 為什麼有些畫面的長條很高、後面一串很矮，又一個很高？學生答出：高的是 **I-frame** [▶ 24:59](https://youtu.be/uKnEZKpZKVA?t=1499)。I-frame 獨立壓縮，佔很多位元；後面的 P-frame 用很少。這支影片 2 個 I-frame、14 個 P-frame，但位元**幾乎都花在 I-frame** 上 [▶ 24:59](https://youtu.be/uKnEZKpZKVA?t=1499)。

### 7.2 運動向量、預測畫面、殘差

[▶ 25:38](https://youtu.be/uKnEZKpZKVA?t=1538) 軟體可以顯示每個區塊的運動向量（箭頭）[▶ 26:14](https://youtu.be/uKnEZKpZKVA?t=1574)。**區塊大小不固定**：和 BPG 一樣，紋理少的地方用大區塊、細節多的地方用小區塊 [▶ 26:14](https://youtu.be/uKnEZKpZKVA?t=1574)。

[▶ 26:47](https://youtu.be/uKnEZKpZKVA?t=1607) 也可以看**預測畫面**（從前一張運動補償來的）和解碼畫面的差異：某些地方有方塊感；這反映在**殘差**上：殘差很稀疏，幾乎都是 0，再用影像壓縮編 [▶ 27:21](https://youtu.be/uKnEZKpZKVA?t=1641)。

【Q&A】[▶ 27:59](https://youtu.be/uKnEZKpZKVA?t=1679) 學生問：殘差畫面和自然影像看起來不一樣，壓殘差時是用不同的影像壓縮器或不同參數嗎？Kedar：超參數可以不同，看編碼器。他記得殘差用的預設 Huffman 表就不太一樣 [▶ 28:39](https://youtu.be/uKnEZKpZKVA?t=1719)。**H.264 標準只規定解碼器**，所以不同編碼器可以自由發揮 [▶ 28:39](https://youtu.be/uKnEZKpZKVA?t=1719)。

### 7.3 騎師影片

[▶ 29:17](https://youtu.be/uKnEZKpZKVA?t=1757) 用高品質編騎師影片：區塊小很多。**高品質、運動又多時，I-frame 和 P-frame 差不多大**，反映在檔案大小上：只用 I-frame 9 Mb/s，I + P 6 Mb/s，幫助沒那麼大 [▶ 29:17](https://youtu.be/uKnEZKpZKVA?t=1757)。因為 P-frame 靠殘差稀疏才壓得好；運動很多、很怪時就預測不準，要花很多位元 [▶ 29:53](https://youtu.be/uKnEZKpZKVA?t=1793)。

### 7.4 MediaInfo 看編碼後的檔案

[▶ 31:08](https://youtu.be/uKnEZKpZKVA?t=1868)

- **AVC**（Advanced Video Codec）就是 H.264 的另一個名字（十年前很先進，現在不太先進了）[▶ 31:08](https://youtu.be/uKnEZKpZKVA?t=1868)。
- 位元率 6 Mb/s [▶ 31:47](https://youtu.be/uKnEZKpZKVA?t=1907)。
- 很多編碼設定（FFmpeg 內部選的，可手動改）[▶ 31:47](https://youtu.be/uKnEZKpZKVA?t=1907)：例如用 **CABAC**（自適應算術編碼）而不是 Huffman；**LookAhead**：一張畫面會影響之後約 8 張 P-frame，所以找運動時要往前看 [▶ 32:28](https://youtu.be/uKnEZKpZKVA?t=1948)。各種最佳化讓編碼慢很多，但有時壓得更好。

---

## 8. 想法三：前後都參考（B-frame）

### 8.1 想法

[▶ 32:28](https://youtu.be/uKnEZKpZKVA?t=1948) P-frame 是**外插**：從前一張推到下一張再編差異。實際上**內插比外插好** [▶ 33:08](https://youtu.be/uKnEZKpZKVA?t=1988)。

做法：第 1 張是 I-frame；第 4 張是根據 I-frame 預測的 P-frame（隔了幾張，運動較多，可能比較貴）；中間的第 2、3 張用第 1 張和第 4 張**內插** [▶ 33:08](https://youtu.be/uKnEZKpZKVA?t=1988)，位元率可以小很多 [▶ 33:47](https://youtu.be/uKnEZKpZKVA?t=2027)。

> **B-frame**：同時參考**過去和未來**的畫面 [▶ 33:47](https://youtu.be/uKnEZKpZKVA?t=2027)。（`L18.pdf`：「references past and future」。）

> ⚠️ 逐字稿缺字 [▶ 33:47](https://youtu.be/uKnEZKpZKVA?t=2027)：字幕說「B stands for bilinear coding because it references both left to right directions」；投影片只寫「references past and future」。B 代表什麼的確切說法待確認（以下**不是逐字稿內容**：一般稱為 bi-directional predicted frame，雙向預測畫面）。

[▶ 34:25](https://youtu.be/uKnEZKpZKVA?t=2065) 上傳到 YouTube 或 Netflix 上的影片大多用 B-frame（實際上用**階層式 B-frame**，hierarchical B-frames）[▶ 34:25](https://youtu.be/uKnEZKpZKVA?t=2065)。主要理由：內插比外插簡單 [▶ 34:25](https://youtu.be/uKnEZKpZKVA?t=2065)。

### 8.2 看 B-frame 編碼的檔案【課堂討論】

[▶ 38:38](https://youtu.be/uKnEZKpZKVA?t=2318) 「foreman」影片（另一支經典測試影片）：從每張畫面的位元數能猜出哪些是 I、P、B 嗎？[▶ 38:38](https://youtu.be/uKnEZKpZKVA?t=2318)

[▶ 39:15](https://youtu.be/uKnEZKpZKVA?t=2355) Kedar 提示：最高的兩個是 I-frame；稍微高一點的是 P-frame；中間三個很矮的是 B-frame（依兩邊內插）[▶ 39:15](https://youtu.be/uKnEZKpZKVA?t=2355)。

【Q&A】[▶ 39:53](https://youtu.be/uKnEZKpZKVA?t=2393) 學生指出軟體顯示有 4 個 P-frame。Kedar 看相依結構圖確認：確實有 4 個 P-frame [▶ 40:26](https://youtu.be/uKnEZKpZKVA?t=2426)；某處多一個 P-frame，可能是編碼器判斷那裡有場景切換 [▶ 41:36](https://youtu.be/uKnEZKpZKVA?t=2496)。從**相依結構圖**可以看出誰參考誰 [▶ 41:36](https://youtu.be/uKnEZKpZKVA?t=2496)。

[▶ 42:13](https://youtu.be/uKnEZKpZKVA?t=2533) 觀察：B-frame 數量多，但佔的位元比例小很多。B-frame 也**不只參考兩張**：例如某個 B-frame 參考三張（P-frame、I-frame 和其他 P-frame），由編碼器決定 [▶ 42:51](https://youtu.be/uKnEZKpZKVA?t=2571)。

[▶ 42:51](https://youtu.be/uKnEZKpZKVA?t=2571) 騎師影片：就算要求用 IPB，編碼器判斷運動太多、用 B-frame 不划算，大多還是 P-frame，只有少數 B-frame [▶ 43:40](https://youtu.be/uKnEZKpZKVA?t=2620)。**指定可用 B-frame，編碼器不一定會用** [▶ 43:40](https://youtu.be/uKnEZKpZKVA?t=2620)。

---

## 9. 三種模式與延遲

【課堂討論】[▶ 35:00](https://youtu.be/uKnEZKpZKVA?t=2100) 什麼時候寧可用 I + P 而不用 I + P + B？提示：課堂大多只在乎壓縮率，但實際上還有**速度、延遲**等限制 [▶ 35:36](https://youtu.be/uKnEZKpZKVA?t=2136)。

[▶ 35:36](https://youtu.be/uKnEZKpZKVA?t=2136) 用 B-frame 時：第 1 張是獨立影像，很快就能解；但要解第 2 張，得先解第 4 張、再解第 3 張……**多了延遲** [▶ 35:36](https://youtu.be/uKnEZKpZKVA?t=2136)。

（`L18.pdf`）

| 模式 | 用途 | 理由 |
|---|---|---|
| **I + P**（低延遲 / low-delay 模式） | 視訊通話：Zoom、Google Meet、FaceTime [▶ 36:12](https://youtu.be/uKnEZKpZKVA?t=2172) | 不知道未來的畫面，不能等幾張畫面再編，否則大家都收到延遲的畫面 |
| **I + P + B**（random access 模式） | Netflix、隨選影片 [▶ 36:12](https://youtu.be/uKnEZKpZKVA?t=2172) | 整支影片已知，可以用 B-frame；通常壓縮最好 [▶ 37:25](https://youtu.be/uKnEZKpZKVA?t=2245) |
| **只有 I-frame** | 影片剪輯軟體（ProRes 等 mezzanine 格式）[▶ 37:25](https://youtu.be/uKnEZKpZKVA?t=2245) | 不是為了省空間，而是讓**剪輯**可行：可以載入一張畫面、處理、放回去 [▶ 38:01](https://youtu.be/uKnEZKpZKVA?t=2281) |

[▶ 36:49](https://youtu.be/uKnEZKpZKVA?t=2209) **為什麼 YouTube 跳轉不準**：在 YouTube 上跳到任意時間點，它常常不是從那一點開始，而是往左或往右一點，因為**必須從 I-frame 開始解碼** [▶ 36:49](https://youtu.be/uKnEZKpZKVA?t=2209)。（呼應第 1 集 Pulkit 說的「跳轉的最小單位」。）

[▶ 37:25](https://youtu.be/uKnEZKpZKVA?t=2245) 講者說「random access」這個名字有點名不副實，但它壓得更好，又能在多處跳轉。

---

## 10. 區塊運動的問題與學習式影片編碼

### 10.1 區塊的問題

[▶ 44:14](https://youtu.be/uKnEZKpZKVA?t=2654) 區塊搜尋和編碼**極有效率**，但和 BPG、JPEG 一樣是**沿座標軸對齊**的，會產生**方塊假影**：Zoom 頻寬掉下來時看到的怪方塊就是這個 [▶ 44:14](https://youtu.be/uKnEZKpZKVA?t=2654)。所以這些演算法在迴圈裡還需要**去區塊濾波**（deblocking filter）做後處理，但假影太多時常常也沒用 [▶ 44:49](https://youtu.be/uKnEZKpZKVA?t=2689)。

### 10.2 學習式影片編碼

[▶ 44:49](https://youtu.be/uKnEZKpZKVA?t=2689) 平行的研究：從傳統影片編碼走向 **ML 影片編碼**。

1. 最簡單：保留運動那一塊，**把影像壓縮換成學習式的影像壓縮器** [▶ 45:24](https://youtu.be/uKnEZKpZKVA?t=2724)。
2. **整個端到端學習**：運動的品質更好，不是一塊一塊的，而是**平滑的光流**（flow），假影更少 [▶ 46:00](https://youtu.be/uKnEZKpZKVA?t=2760)。

[▶ 46:33](https://youtu.be/uKnEZKpZKVA?t=2793) 例：H.265（比 H.264 新一代）低位元率時有很多方塊假影；ML 編碼器平滑很多 [▶ 46:33](https://youtu.be/uKnEZKpZKVA?t=2793)。

[▶ 46:33](https://youtu.be/uKnEZKpZKVA?t=2793) 基準（`L18.pdf`：UVG 資料集、低延遲設定、keyint = 16）：

- **PSNR**：ML 編碼器已經比 H.265（紫色）好很多；AV1（較新、部分裝置支援）也比 H.265 好 [▶ 47:17](https://youtu.be/uKnEZKpZKVA?t=2837)。（講者說投影片是幾年前的，之後進步很多，主要在 PSNR 以外的指標上。）
- **MS-SSIM**（較感知的指標）：ML 編碼器優勢更大，因為 ML 編碼器很容易最佳化更複雜的指標 [▶ 47:55](https://youtu.be/uKnEZKpZKVA?t=2875)。

### 10.3 限制

[▶ 47:55](https://youtu.be/uKnEZKpZKVA?t=2875) H.264、H.265 簡單、能用；ML 編碼器能做得好很多。但影片編解碼**必須即時**（30 或 60 FPS），所以不能用超大的模型（大型語言模型、大型影片模型今天不可能即時跑）[▶ 48:29](https://youtu.be/uKnEZKpZKVA?t=2909)。再努力一點，總有一天可以 [▶ 48:29](https://youtu.be/uKnEZKpZKVA?t=2909)。

【口頭】[▶ 49:11](https://youtu.be/uKnEZKpZKVA?t=2951) Kedar：他在 Apple 的團隊在招人（ML 影像、影片處理與壓縮，實習或全職）。Shubham：可惜不能說 Amazon 的壓縮團隊在招人 [▶ 49:11](https://youtu.be/uKnEZKpZKVA?t=2951)。

---

## 11. 課程總結（Shubham）

### 11.1 iid 資料

[▶ 49:47](https://youtu.be/uKnEZKpZKVA?t=2987) 幾個月前從簡單的 iid 資料開始：熵、前綴碼、Huffman、算術編碼、rANS [▶ 49:47](https://youtu.be/uKnEZKpZKVA?t=2987)。

> 這些是**基本建構塊**：前半和後半都一直用到（Kedar 今天也提到 CABAC，非常有效率的算術編碼器）[▶ 50:22](https://youtu.be/uKnEZKpZKVA?t=3022)。就算資料不是 iid，也可以用各種方法轉成近乎 iid，再用這些。各有接近熵的程度和效率的取捨 [▶ 50:22](https://youtu.be/uKnEZKpZKVA?t=3022)。

[▶ 51:00](https://youtu.be/uKnEZKpZKVA?t=3060) **熵是壓縮的根本極限**。【口頭】Shubham 最喜歡壓縮的一點：**理論真的幫得上實務**，特別是無損：從理論出發，為資料建模、算數字，再和實際結果比，能得到很多洞見 [▶ 51:00](https://youtu.be/uKnEZKpZKVA?t=3060)。資訊理論的工具也用在別處：「任何演算法都不可能比熵更好」這種非平凡的下界證明，在很多地方被使用；作業 4「找最好的划船手」那題就有一點味道 [▶ 51:39](https://youtu.be/uKnEZKpZKVA?t=3099)。

### 11.2 非 iid（真實資料）

[▶ 52:20](https://youtu.be/uKnEZKpZKVA?t=3140) 熵率、條件熵；**好的預測器 = 好的壓縮器**；$k$ 階自適應編碼器；有些期末專題做 CTW、PPM 等更進階的預測器；今年新加的 LLaMA 等 LLM 當壓縮器 [▶ 52:59](https://youtu.be/uKnEZKpZKVA?t=3179)。

通用壓縮器：不明確建模，對任何平穩來源都達到熵率；主要講 LZ77，專題也有 LZ77、LZ78 [▶ 53:30](https://youtu.be/uKnEZKpZKVA?t=3210)。

**實務建議** [▶ 53:30](https://youtu.be/uKnEZKpZKVA?t=3210)：以後研究、工作要壓縮東西時，回去看那份投影片。**從第一原理出發** [▶ 54:17](https://youtu.be/uKnEZKpZKVA?t=3257)：先評估標準工具做得如何、有沒有資料模型、能不能算熵、標準壓縮器和目標之間有沒有差距；不要每個檔案都自己寫壓縮器。

> 一個一再出現的關鍵想法：**不管資料第一眼看起來多複雜，就建模、轉換成標準壓縮器能處理的形式**；重用現成工具，不要重寫 Huffman、算術編碼、LZ77（專題可以）[▶ 54:55](https://youtu.be/uKnEZKpZKVA?t=3295)。

### 11.3 有損壓縮

[▶ 54:55](https://youtu.be/uKnEZKpZKVA?t=3295) 量化（最簡單的有損壓縮：純量、均勻純量）；率失真理論（對應熵）；向量量化；轉換編碼（特徵向量分解、去相關）；DCT [▶ 55:30](https://youtu.be/uKnEZKpZKVA?t=3330)。

[▶ 55:30](https://youtu.be/uKnEZKpZKVA?t=3330) **有損壓縮的理論沒有無損那麼好用** [▶ 56:13](https://youtu.be/uKnEZKpZKVA?t=3373)：

- 無損：iid 來源可以用算術編碼在熵的 2 位元內做到；有損沒有這麼簡單的演算法。
- 甚至不知道根本極限：高斯以外的分布，率失真函數常常只能估計。
- 但仍提供很多洞見；JPEG 的設計是**理論和人類感知**很好的結合 [▶ 56:53](https://youtu.be/uKnEZKpZKVA?t=3413)。（現在大家直接做機器學習，但做機器學習也需要懂理論。）

### 11.4 應用

[▶ 56:53](https://youtu.be/uKnEZKpZKVA?t=3413) 影像（JPEG、ML 影像壓縮）、訊號與系統入門（DCT）、音訊示範、今天的影片。

> 這張方塊圖一再出現：**轉換去相關 →（影像、音訊）量化 /（影片）運動補償殘差 → 無損編碼**。量化是唯一有損的部分；無損編碼可以用任何學過的方法：PNG 用 LZ77、JPEG 用 Huffman，新的用算術編碼或 ANS [▶ 58:02](https://youtu.be/uKnEZKpZKVA?t=3482)。

【投影片補充】`L18_conclusion.pdf`：「各領域的關鍵概念都差不多：轉換編碼、殘差編碼，最後是無損編碼。」

### 11.5 沒講到的

[▶ 58:39](https://youtu.be/uKnEZKpZKVA?t=3519)

| 主題 | 說明 |
|---|---|
| **分散式壓縮** | 多個感測器、節點各自壓縮，但資料彼此相關；作業 3 那個「你要送 $X$、對方有 $Y$」的謎題有一點味道。和資訊理論的另一半**錯誤更正碼**有關，常借用其工具 [▶ 59:13](https://youtu.be/uKnEZKpZKVA?t=3553) |
| **精簡資料結構**（succinct data structures） | 課堂一直假設壓縮 → 冷儲存 → 解壓；但常需要**隨機存取**（像 YouTube 跳轉；基因體裡要在壓縮資料上快速搜尋）[▶ 59:48](https://youtu.be/uKnEZKpZKVA?t=3588) |
| **神經網路的壓縮** | 模型量化、稀疏化；失真不是人的感知，而是模型的**準確率** [▶ 1:00:37](https://youtu.be/uKnEZKpZKVA?t=3637) |
| **硬體中的壓縮** | 晶片上的影片編碼硬體；zstd 比 gzip 快的原因之一是能用專用（SIMD）指令；有專題做 GPU 上的壓縮；也可以為特定演算法設計專用硬體 [▶ 1:01:13](https://youtu.be/uKnEZKpZKVA?t=3673) |
| **特殊領域** | AR/VR：依注視點分配位元，讓頭戴裝置不發燙、線不用很粗 [▶ 1:02:21](https://youtu.be/uKnEZKpZKVA?t=3741)；**基因體**（Shubham 博士大多做這個）[▶ 1:02:58](https://youtu.be/uKnEZKpZKVA?t=3778) |

### 11.6 接下來

[▶ 1:04:08](https://youtu.be/uKnEZKpZKVA?t=3848)

- **Stanford Compression Library**：歡迎把專題做成 merge request 貢獻 [▶ 1:04:47](https://youtu.be/uKnEZKpZKVA?t=3887)。【口頭】起因是想搞懂算術編碼、ANS、range coding，卻遇到極度最佳化、難以閱讀的 C 程式（把一切塞進奇怪的位元遮罩）[▶ 1:04:47](https://youtu.be/uKnEZKpZKVA?t=3887)。
- 課程網站的資源頁。
- 相關課程 [▶ 1:05:21](https://youtu.be/uKnEZKpZKVA?t=3921)：**EE276**（資訊理論，Tsachy 今年教，有更多理論，特別是有損）；**EE376**（資訊理論專題；以前的 376C「Universal Schemes in Information Theory」證明了 LZ78 對平穩來源達到熵率等）[▶ 1:06:02](https://youtu.be/uKnEZKpZKVA?t=3962)；**Music 422**（感知音訊編碼，心理聲學；Facebook 的 ML 音訊編碼很有影響力）[▶ 1:06:33](https://youtu.be/uKnEZKpZKVA?t=3993)、[▶ 1:07:08](https://youtu.be/uKnEZKpZKVA?t=4028)；**CS 228**（機率圖模型）、**CS 236**（生成模型）：好模型才有好壓縮器，而好模型從哪來？[▶ 1:07:08](https://youtu.be/uKnEZKpZKVA?t=4028)

【口頭】[▶ 1:07:52](https://youtu.be/uKnEZKpZKVA?t=4072) Shubham：他的壓縮旅程從 2016 年進 Tsachy 的實驗室開始，本來沒想到博士會做壓縮。謝謝所有講者、學生和助教 [▶ 1:08:26](https://youtu.be/uKnEZKpZKVA?t=4106)。

> ⚠️ 逐字稿缺字：[▶ 00:06](https://youtu.be/uKnEZKpZKVA?t=6)、[▶ 1:05:21](https://youtu.be/uKnEZKpZKVA?t=3921) 字幕把 Tsachy 寫成「[? Saki ?]」；[▶ 55:30](https://youtu.be/uKnEZKpZKVA?t=3330) 字幕「Pulkit [INAUDIBLE] and Saki」。

---

## 12. 一頁速查表

### 影片基本量

- 原始位元率 = 寬 × 高 × 每像素樣本數（4:2:0 = 1.5）× 位元 × FPS；720p30 ≈ 332 Mb/s。
- H.264 CRF 20：6.2 Mb/s（~50×，PSNR 43）；CRF 40：0.8 Mb/s（PSNR 33，方塊假影）。

### 三種畫面

| 畫面 | 怎麼編 | 位元 | 特性 |
|---|---|---|---|
| I | 獨立當影像壓 | 最多 | 可以從這裡開始解碼；刷新預測誤差、場景切換 |
| P | 前一張已解碼畫面 + 運動補償 → 殘差 | 中 | 外插；殘差稀疏才好壓 |
| B | 前後畫面內插 → 殘差 | 最少 | 內插比外插好；增加延遲 |

- **keyint**：兩個 I-frame 的距離。
- 運動：區塊匹配（全搜尋、階層式搜尋）、可變區塊大小。
- 為什麼有效：在影像壓縮前先把畫面間的相關性抽掉，殘差幾乎是 0。

### 模式

| 模式 | 畫面 | 用途 |
|---|---|---|
| 低延遲 | I + P | 視訊通話 |
| random access | I + P + B | 隨選影片（YouTube 跳轉會對齊到 I-frame） |
| 全 I | I | 剪輯（ProRes） |

### 細節

- H.264 = AVC；**標準只規定解碼器**。
- CABAC（自適應算術編碼）、LookAhead、去區塊濾波。
- 運動多時 B-frame、P-frame 的好處都變小。

### 學習式影片編碼

平滑光流取代方塊運動；PSNR 和 MS-SSIM 都勝過 H.265；瓶頸是即時（30/60 FPS）。

### 整門課的方塊圖

轉換（去相關）→ 量化或運動補償殘差（唯一有損）→ 無損熵編碼（Huffman / 算術 / ANS / LZ77）。

---

## 13. 整門課的連結

| 本集用到的觀念 | 出自 |
|---|---|
| 影片跳轉的最小單位、I/P/B | 第 1 集預告 |
| CABAC = 自適應算術編碼 | 第 6、9 集 |
| 預測 → 殘差 → 熵編碼 | 第 8–9 集（預測 = 壓縮）、第 15 集 BPG |
| YUV 4:2:0 | 第 15、17 集 |
| 可變區塊大小 | 第 15 集 BPG |
| 學習式壓縮、MS-SSIM | 第 16、17 集 |
| 硬體解碼器 | 第 1、4、16 集 |
| 總結裡的實務建議（先試 zstd） | 第 10 集 |

---

## 附：本集一句話總結

> **720p30 的原始影片要 332 Mb/s，H.264 能壓到約 6 Mb/s 幾乎看不出差別：每張畫面獨立壓（I-frame）已經不錯，但更好的是用區塊匹配找運動、從前一張已解碼畫面預測（P-frame），只壓稀疏的殘差；再用前後畫面內插（B-frame）壓得更小，代價是延遲，所以視訊通話用 I + P、隨選影片用 I + P + B、剪輯用全 I。區塊運動會造成方塊假影，學習式影片編碼用平滑的光流做得更好，但要能即時跑。整門課最後歸結成一張圖：轉換去相關 → 量化（或殘差）→ 無損熵編碼。**

---

## ⚠️ 待確認清單

1. [▶ 33:47](https://youtu.be/uKnEZKpZKVA?t=2027) B-frame 的 B 代表什麼：字幕作「bilinear」，投影片只寫「references past and future」。

---

*筆記依據 Kedar Tatwawadi、Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 18 錄影逐字稿（人工字幕，1:08:39）與投影片 L18、L18_conclusion 整理。*
