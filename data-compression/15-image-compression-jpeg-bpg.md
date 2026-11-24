---
course: Stanford EE274 Data Compression  Theory and Applications（2023 秋）
episode: 15
lecture: Lecture 15
date: 2023-11-15
video: https://youtu.be/pMNVQIZa-G8
notes: 投影片 L15.pdf、L15_ann.pdf；課本沒有影像壓縮
---

# 第 15 集 · Lecture 15：影像壓縮：JPEG、BPG（Image Compression: JPEG, BPG） [▶ 影片](https://youtu.be/pMNVQIZa-G8)

← 上一集：[14-transform-coding-in-practice](14-transform-coding-in-practice.md) ｜ [總目錄](README.md) ｜ 下一集：[16-learnt-image-compression](16-learnt-image-compression.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 15 集
> **講者**：Pulkit Tandon
> **來源**：YouTube 錄影逐字稿（1:24:15，人工字幕 en-US）＋ 投影片 `L15.pdf`、`L15_ann.pdf`。Cover & Thomas 沒有影像壓縮，本集只靠逐字稿和投影片。
> **標記說明**：
> - `【口頭】` 講者口頭補充，投影片沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 小考檢討與回顧](#1-小考檢討與回顧)
- [2. 影像有多大、能壓多小](#2-影像有多大能壓多小)
- [3. MSE 不是對的失真](#3-mse-不是對的失真)
- [4. 問題設定](#4-問題設定)
- [5. 簡單的想法一：降取樣](#5-簡單的想法一降取樣)
- [6. 簡單的想法二：顏色量化](#6-簡單的想法二顏色量化)
- [7. 簡單的想法三：利用相鄰像素（Color Cell Compression）](#7-簡單的想法三利用相鄰像素color-cell-compression)
- [8. 二維區塊轉換編碼與 2D-DCT](#8-二維區塊轉換編碼與-2d-dct)
- [9. JPEG](#9-jpeg)
- [10. BPG：怎麼改進 JPEG](#10-bpg怎麼改進-jpeg)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:06](https://youtu.be/pMNVQIZa-G8?t=6) 課程進入尾聲，接下來幾講看真實的壓縮器。今天是**影像壓縮**，後兩講建立在今天的基礎上 [▶ 00:06](https://youtu.be/pMNVQIZa-G8?t=6)。

[▶ 05:44](https://youtu.be/pMNVQIZa-G8?t=344) 把前面學的無損、有損全部兜起來，學 **JPEG 的基礎**（講者說不會講到 JPEG 的每個小細節，但上完應該能談它的基本元件）[▶ 06:18](https://youtu.be/pMNVQIZa-G8?t=378)。

【投影片補充】`L15.pdf` 的投影片資源：YouTube 頻道 Reducible 的〈The Unreasonable Effectiveness of JPEG: A Signal Processing Approach〉（講者大力推薦，動畫很漂亮）[▶ 06:18](https://youtu.be/pMNVQIZa-G8?t=378)；Stanford EE398A（Bernd Girod）的講義。

---

## 1. 小考檢討與回顧

[▶ 00:40](https://youtu.be/pMNVQIZa-G8?t=40) 轉換編碼的兩個旋鈕：**轉換的區塊大小**、**每條轉換串流量化多少**；音訊壓縮器裡就是頻率截止和量化等級。實用壓縮器多半都有這兩個旋鈕 [▶ 01:18](https://youtu.be/pMNVQIZa-G8?t=78)。

**小考第 1 題** [▶ 01:18](https://youtu.be/pMNVQIZa-G8?t=78)：

| 問題 | 答案 |
|---|---|
| 向量量化在哪些情況會改善有損壓縮？ | **兩者都會**（iid、非 iid）：向量量化總是會改善，做不了只是因為複雜度 |
| 轉換編碼在哪些情況會改善？ | 只有**非 iid（相關）**資料 [▶ 01:56](https://youtu.be/pMNVQIZa-G8?t=116)：iid 資料沒什麼好去相關的 |

**DCT 回顧** [▶ 01:56](https://youtu.be/pMNVQIZa-G8?t=116)：把高頻 DCT 係數歸零後，重建的綠色訊號是原本紅色訊號的**平滑版**：尖的三角形峰變圓了，因為高頻分量被拿掉 [▶ 02:33](https://youtu.be/pMNVQIZa-G8?t=153)。

【口頭】[▶ 03:09](https://youtu.be/pMNVQIZa-G8?t=189) 上一講「為什麼用 DCT 而不用 DFT」課堂沒回答好，已在 Ed 貼了詳細回答：DCT 能得到比 DFT 更稀疏的分量，原因和邊界條件有關 [▶ 03:55](https://youtu.be/pMNVQIZa-G8?t=235)。

**小考第 2、3 題** [▶ 03:55](https://youtu.be/pMNVQIZa-G8?t=235)：

- 把訊號配對到它的 DCT：頻率越高，大的 DCT 係數就越往右 [▶ 04:35](https://youtu.be/pMNVQIZa-G8?t=275)。
- 把某訊號的 DCT 高頻（32 個中的 16 個）歸零後，重建的是哪一個？應該是原訊號的平滑版，不會一樣、也不會更高頻 [▶ 05:07](https://youtu.be/pMNVQIZa-G8?t=307)。

---

## 2. 影像有多大、能壓多小

### 2.1 數位影像

[▶ 06:54](https://youtu.be/pMNVQIZa-G8?t=414) 影像就是像素陣列：**高 × 寬 × 通道數**的三維陣列。RGB 三個通道，今天假設每個值 8 位元，所以每像素 24 位元（3 位元組）[▶ 07:34](https://youtu.be/pMNVQIZa-G8?t=454)。

例 [▶ 07:34](https://youtu.be/pMNVQIZa-G8?t=454)：$764\times512$（講者說高 764、寬 512），3 通道：

$$764\times512\times3\ \text{位元組}\approx1.1\ \text{MB}.$$

這麼小的圖要 1.1 MB，很多 [▶ 08:12](https://youtu.be/pMNVQIZa-G8?t=492)。

### 2.2 壓縮後

| 方法 | 大小 | 壓縮比 | 觀察 |
|---|---|---|---|
| JPEG | 27 KB | ~40× | 來回切換看不出差別 [▶ 08:52](https://youtu.be/pMNVQIZa-G8?t=532) |
| JPEG | 14 KB | ~80× | 出現**方塊狀假影**，臉上看得到不同的等高線 [▶ 09:57](https://youtu.be/pMNVQIZa-G8?t=597) |
| JPEG | 8 KB | ~137× | 「純垃圾」，沒有應用會接受 [▶ 10:32](https://youtu.be/pMNVQIZa-G8?t=632) |
| BPG | 8 KB | ~137× | 明顯好很多 [▶ 11:12](https://youtu.be/pMNVQIZa-G8?t=672) |
| ML 壓縮器 | 8 KB | ~137× | 臉更平滑（下一講）[▶ 12:28](https://youtu.be/pMNVQIZa-G8?t=748) |

[▶ 11:47](https://youtu.be/pMNVQIZa-G8?t=707) JPEG 存在很久、到處都是，但還有很大的改進空間；我們也不知道實用壓縮器是不是已經接近最佳。BPG 仍是傳統的、手工設計規則的壓縮器；下一講講機器學習的壓縮器 [▶ 11:47](https://youtu.be/pMNVQIZa-G8?t=707)。

【口頭】[▶ 12:59](https://youtu.be/pMNVQIZa-G8?t=779) 比較影像壓縮時要看原始素材，因為不同螢幕會丟掉細節。

### 2.3 為什麼大家都壓縮影像

[▶ 13:41](https://youtu.be/pMNVQIZa-G8?t=821)

- 40–137 倍幾乎看不出差別，所以**幾乎沒人存未壓縮的影像**。
- 連 DSLR 相機預設都會 JPEG 壓縮。PNG 是**無損**影像格式，但 JPEG 普遍得多：何必多付兩個數量級的空間，存一張看起來一模一樣的圖？[▶ 13:41](https://youtu.be/pMNVQIZa-G8?t=821)
- 其他影像壓縮器 [▶ 14:18](https://youtu.be/pMNVQIZa-G8?t=858)：JPEG 2000、BPG（HEIC）、AVIF、**JPEG-XL**（講者說是效能最好的傳統影像壓縮器之一）、ML 類。效能越好，複雜度通常越高。

[▶ 14:51](https://youtu.be/pMNVQIZa-G8?t=891) 1992 年介紹 JPEG 標準的論文說：當時多數商業和消費者還是用**類比**方式使用照片；影像需要的資料量太大，是很多應用無法數位化的關鍵障礙，儲存或傳輸成本太高 [▶ 15:24](https://youtu.be/pMNVQIZa-G8?t=924)。現在已經完全不同了。

---

## 3. MSE 不是對的失真

[▶ 16:01](https://youtu.be/pMNVQIZa-G8?t=961) 有損壓縮：影像 → 編碼 → JPEG 檔 → 解碼 → 重建。原圖和重建圖不同，要用失真度量比較 [▶ 16:35](https://youtu.be/pMNVQIZa-G8?t=995)。目前理論都用 MSE。

**練習**【課堂討論】[▶ 16:35](https://youtu.be/pMNVQIZa-G8?t=995) 原圖 A 和五張重建 B、C、D、E、F：

1. [▶ 17:10](https://youtu.be/pMNVQIZa-G8?t=1030) 你視覺上偏好哪張？學生答 **B**，大家同意 [▶ 17:51](https://youtu.be/pMNVQIZa-G8?t=1071)。
2. [▶ 17:51](https://youtu.be/pMNVQIZa-G8?t=1071) 最佳化 MSE 的壓縮器會偏好哪張？有人答 F（看起來一樣，只是多了些椒鹽雜訊）[▶ 18:35](https://youtu.be/pMNVQIZa-G8?t=1115)。

[▶ 18:35](https://youtu.be/pMNVQIZa-G8?t=1115) **陷阱題：B 到 F 和 A 的 MSE 完全一樣。** 只看 MSE 的壓縮器對它們一視同仁，但這顯然是錯的：你不會同樣喜歡 B 和 E [▶ 19:16](https://youtu.be/pMNVQIZa-G8?t=1156)。

> **人不是用 MSE 在比較影像**，人有自己的視覺路徑。很多研究（從神經科學、心理物理學到壓縮器設計）在研究人的感知失真；很多時間、實驗和金錢花在調參數以符合人的觀看 [▶ 19:47](https://youtu.be/pMNVQIZa-G8?t=1187)。學習式壓縮之後的第三講會深入 [▶ 20:25](https://youtu.be/pMNVQIZa-G8?t=1225)。

[▶ 20:25](https://youtu.be/pMNVQIZa-G8?t=1225) 今天為了簡單先用 MSE。JPEG 當初也以 MSE 為主，但在各處加了很多**經驗法則**來彌補人眼的特性；所以看 JPEG 某些設計時會覺得莫名其妙，後來才知道是主觀實驗決定的 [▶ 20:59](https://youtu.be/pMNVQIZa-G8?t=1259)。

---

## 4. 問題設定

[▶ 21:34](https://youtu.be/pMNVQIZa-G8?t=1294)

- 通常是壓縮**單張**影像，不是一組影像（一組可以做得更好）。
- 所以**非漸近**的表現很重要：資料是有限的 [▶ 21:34](https://youtu.be/pMNVQIZa-G8?t=1294)。
- 資料多半**非平穩**，像素值也不是 iid，所以轉換能幫很大的忙去相關 [▶ 22:08](https://youtu.be/pMNVQIZa-G8?t=1328)。

可用的工具 [▶ 22:08](https://youtu.be/pMNVQIZa-G8?t=1328)：

| 工具 | 特性 |
|---|---|
| 純量量化 | 極快，但不是最好 |
| 向量量化 | 很好，但維度一高就很慢 |
| 轉換編碼 | 去相關後用簡單的純量量化 |
| **預測編碼** | 用過去的符號預測目前的，只編差值；預測越準，位元越少（呼應 context-based 那講）[▶ 22:41](https://youtu.be/pMNVQIZa-G8?t=1361) |

---

## 5. 簡單的想法一：降取樣

【課堂討論】[▶ 23:57](https://youtu.be/pMNVQIZa-G8?t=1437) 怎麼壓縮這張圖？先不管失真。學生答：大塊的同色區域 [▶ 24:27](https://youtu.be/pMNVQIZa-G8?t=1467)（等一下會用到）。

[▶ 24:59](https://youtu.be/pMNVQIZa-G8?t=1499) 最簡單的：**把高、寬砍半**（降取樣），$H\times W\times C\to\frac HD\times\frac WD\times C$ [▶ 25:38](https://youtu.be/pMNVQIZa-G8?t=1538)。砍半就是 4 倍壓縮。

解碼端做反向的**升取樣**（upsampling）：雙三次插值（bicubic）、Lanczos 插值等，在離散點之間填值，恢復原尺寸，再和原圖算 MSE [▶ 26:18](https://youtu.be/pMNVQIZa-G8?t=1578)。改變 $D$（2、3、4、8、16）就能調率失真。

[▶ 26:51](https://youtu.be/pMNVQIZa-G8?t=1611) 聽起來很蠢，但這其實是**影像壓縮器建立率失真曲線的主要方式之一**：YouTube 的 240p、360p、480p、720p、1080p、4K 就是解析度 [▶ 26:51](https://youtu.be/pMNVQIZa-G8?t=1611)。看無聊的紀錄片時 720p 也許就夠了 [▶ 27:32](https://youtu.be/pMNVQIZa-G8?t=1652)。

[▶ 28:06](https://youtu.be/pMNVQIZa-G8?t=1686) 實務上：把 4K 降到 720p 傳，電視收到再升取樣回 4K；不是導演原本的樣子，但大家一直在用。轉換編碼那幾講沒提，但做多媒體的率失真曲線時一直有這個旋鈕；音訊可以改取樣率 [▶ 28:06](https://youtu.be/pMNVQIZa-G8?t=1686)。

---

## 6. 簡單的想法二：顏色量化

[▶ 28:40](https://youtu.be/pMNVQIZa-G8?t=1720) 不改高寬，對**通道**下手：把 RGB 三維向量做量化 [▶ 29:13](https://youtu.be/pMNVQIZa-G8?t=1753)。

- 原本每個顏色有 $2^8\times2^8\times2^8=2^{24}$ 種 [▶ 29:44](https://youtu.be/pMNVQIZa-G8?t=1784)。
- 只用 **256 種顏色**表示：來回切換看不出差別，約 **3 倍**壓縮 [▶ 30:22](https://youtu.be/pMNVQIZa-G8?t=1822)。自然影像根本用不到那麼多顏色，很多顏色不自然、不會出現 [▶ 30:56](https://youtu.be/pMNVQIZa-G8?t=1856)。
- 只用 **16 種顏色**：約 **6 倍**壓縮，開始看得到明顯假影 [▶ 30:56](https://youtu.be/pMNVQIZa-G8?t=1856)。

[▶ 31:31](https://youtu.be/pMNVQIZa-G8?t=1891) 這就是對顏色通道做**向量量化**，叫**顏色量化**（color quantization），是這個領域最早被探索的想法之一。

---

## 7. 簡單的想法三：利用相鄰像素（Color Cell Compression）

【課堂討論】[▶ 32:02](https://youtu.be/pMNVQIZa-G8?t=1922) 還能利用什麼？學生答：相鄰的像素顏色一樣 [▶ 32:32](https://youtu.be/pMNVQIZa-G8?t=1952)。講者：很接近；就算不完全一樣，**自然影像是平滑的**，相鄰像素**高度相關** [▶ 33:06](https://youtu.be/pMNVQIZa-G8?t=1986)。放大看局部，很多像素非常相關。

**Color Cell Compression**（1984）[▶ 33:46](https://youtu.be/pMNVQIZa-G8?t=2026)：

- 每個 **4×4 區塊只用 2 種顏色**（從 256 種裡選）[▶ 34:17](https://youtu.be/pMNVQIZa-G8?t=2057)。
- 每區塊存兩個顏色：$8+8=16$ 位元；每像素 1 位元指出用哪個顏色：16 位元 [▶ 35:29](https://youtu.be/pMNVQIZa-G8?t=2129)。
- 每 4×4 區塊共 32 位元 → **每像素 2 位元** [▶ 36:07](https://youtu.be/pMNVQIZa-G8?t=2167)，相較於 24 位元是 **12 倍**壓縮（投影片）。

[▶ 34:51](https://youtu.be/pMNVQIZa-G8?t=2091) 遠看大致沒問題。[▶ 36:40](https://youtu.be/pMNVQIZa-G8?t=2200) 放大眼睛那裡：橘色變黃色、有紅色的像素瑕疵，因為每 16 個像素只用兩種顏色 [▶ 37:18](https://youtu.be/pMNVQIZa-G8?t=2238)。

> ⚠️ 逐字稿缺字 [▶ 36:07](https://youtu.be/pMNVQIZa-G8?t=2167)：講者說「we started from 2 raised to 24 bits per pixel」，應為每像素 24 位元（$2^{24}$ 是顏色種類數）。

[▶ 37:18](https://youtu.be/pMNVQIZa-G8?t=2238) 這很像經驗法則（為什麼 2 種顏色？為什麼 4×4？），它能壓縮是因為利用了**空間相關性**。處理相關性有更好的方法：**轉換編碼** [▶ 37:55](https://youtu.be/pMNVQIZa-G8?t=2275)。

---

## 8. 二維區塊轉換編碼與 2D-DCT

### 8.1 從一維到二維

[▶ 38:27](https://youtu.be/pMNVQIZa-G8?t=2307) 方塊圖和前兩講一樣：原圖 → 轉換係數 → 量化、熵編碼 → 反轉換 → 重建 [▶ 38:27](https://youtu.be/pMNVQIZa-G8?t=2307)。唯一的新東西：轉換作用在**二維**訊號上 [▶ 39:00](https://youtu.be/pMNVQIZa-G8?t=2340)。

- 選區塊大小 $b\times b$（相當於上一講的區塊 2）。
- 先想灰階影像。$n\times n$ 的區塊可以排成長 $n^2$ 的向量，轉換矩陣是 $n^2\times n^2$ [▶ 40:06](https://youtu.be/pMNVQIZa-G8?t=2406)。
- 正交轉換的反轉換就是轉置，不用算反矩陣（$n\times n$ 矩陣求反要 $n^3$）[▶ 40:40](https://youtu.be/pMNVQIZa-G8?t=2440)。

### 8.2 DC 和 AC

[▶ 41:14](https://youtu.be/pMNVQIZa-G8?t=2474) 一維 DCT 矩陣（區塊 8）的第一列給出 **DC 分量**：區塊的平均值。DC 源自電機的「直流」（direct current）；很多多媒體壓縮器都這樣稱呼，就是平均值 [▶ 42:01](https://youtu.be/pMNVQIZa-G8?t=2521)。其他分量叫 **AC 分量**（交流），有頻率行為 [▶ 42:35](https://youtu.be/pMNVQIZa-G8?t=2555)。

### 8.3 2D-DCT 的基底【課堂討論】

[▶ 43:06](https://youtu.be/pMNVQIZa-G8?t=2586) 二維 DCT 矩陣：$n\times n$ 區塊時是 $n^2\times n^2$；區塊 8 時就是 64 張 $8\times8$ 的小圖 [▶ 43:46](https://youtu.be/pMNVQIZa-G8?t=2626)。它是一維 DCT 的推廣：取樣的是二維餘弦波。

[▶ 45:02](https://youtu.be/pMNVQIZa-G8?t=2702) 看出什麼規律？

- 學生：**第一列**和一維 DCT 很像，第一張是平的，往右是**垂直條紋**、頻率越來越高 [▶ 45:46](https://youtu.be/pMNVQIZa-G8?t=2746)。
- 學生：**第一行**也一樣，但是**水平條紋** [▶ 46:25](https://youtu.be/pMNVQIZa-G8?t=2785)。
- 往右下：兩個方向的頻率都增加，混在一起 [▶ 46:58](https://youtu.be/pMNVQIZa-G8?t=2818)；某張圖垂直方向的頻率比水平高，就和上面對應的那張一致 [▶ 47:28](https://youtu.be/pMNVQIZa-G8?t=2848)。

[▶ 48:03](https://youtu.be/pMNVQIZa-G8?t=2883) 總結：左上是 DC（純白，區塊平均）；往右，水平方向的頻率增加（垂直條紋）；往下，垂直方向的頻率增加（水平條紋）；中間是兩者混合 [▶ 48:42](https://youtu.be/pMNVQIZa-G8?t=2922)。

**可分離**（separable）[▶ 44:17](https://youtu.be/pMNVQIZa-G8?t=2657)：2D-DCT 可以先沿一個方向做 1D-DCT，再沿另一個方向做 1D-DCT [▶ 45:02](https://youtu.be/pMNVQIZa-G8?t=2702)。

### 8.4 例子

[▶ 48:42](https://youtu.be/pMNVQIZa-G8?t=2922) 左邊影像區塊、右邊 2D-DCT（黃大、深藍為 0）：

- **常數區塊**：只有 DC [▶ 48:42](https://youtu.be/pMNVQIZa-G8?t=2922)。
- 只有某個 $x$ 方向頻率的區塊：只有一個係數非 0（delta）[▶ 49:56](https://youtu.be/pMNVQIZa-G8?t=2996)。基底圖本身做 2D-DCT 都是單一個點，訊號**極度稀疏**；64 個係數只要壓 1 個 [▶ 50:30](https://youtu.be/pMNVQIZa-G8?t=3030)。
- 經典測試影像（講者說不確定來源）的三個區塊 [▶ 51:05](https://youtu.be/pMNVQIZa-G8?t=3065)：
  - 平滑區：大部分係數 0，有幾個非 0，**很稀疏** [▶ 51:38](https://youtu.be/pMNVQIZa-G8?t=3098)。自然影像平滑變化、沒什麼高頻。
  - 有水平條紋的區：係數沿 $x$ 軸散開，$y$ 軸幾乎 0 [▶ 52:14](https://youtu.be/pMNVQIZa-G8?t=3134)。
  - 格紋桌布：高頻分量多很多，但仍然相當稀疏，因為基底裡本來就有這些高頻圖樣 [▶ 52:54](https://youtu.be/pMNVQIZa-G8?t=3174)。
- **雜訊影像** [▶ 53:28](https://youtu.be/pMNVQIZa-G8?t=3208)：DCT **不稀疏**（投影片寫成「sparse」是錯的，講者更正）。自然界不太會有這種影像。

### 8.5 截斷 2D-DCT

[▶ 54:01](https://youtu.be/pMNVQIZa-G8?t=3241) 一隻小狗的圖，只保留前幾個 DCT 係數 [▶ 54:01](https://youtu.be/pMNVQIZa-G8?t=3241)：

| 保留 | 結果 |
|---|---|
| 只有 DC | 每個區塊只剩平均值 |
| 前 2 個 | 已經看得出狗的結構（丟掉 62 個）[▶ 54:41](https://youtu.be/pMNVQIZa-G8?t=3281) |
| 前 8 個 | 重建已經很好 [▶ 54:41](https://youtu.be/pMNVQIZa-G8?t=3281) |

[▶ 55:15](https://youtu.be/pMNVQIZa-G8?t=3315) 這就是轉換編碼的威力：去相關、能量集中，讓你丟掉大量頻率分量。作業有一題會用到。

> **觀察**：對大多數「自然」影像區塊，DCT 是**稀疏的**，能量集中在低頻。這是 JPEG 相對於顏色量化等方法的關鍵 [▶ 55:47](https://youtu.be/pMNVQIZa-G8?t=3347)。

---

## 9. JPEG

### 9.1 整體流程

[▶ 56:22](https://youtu.be/pMNVQIZa-G8?t=3382)

```
影像 ──[顏色轉換 + 色度降取樣]──> [前向 DCT] ──> [量化] ──> [無損編碼] ──> JPEG 檔
```

[▶ 56:56](https://youtu.be/pMNVQIZa-G8?t=3416) 後三格就是上一講的陽春有損壓縮器：轉換、量化、熵編碼。[▶ 56:56](https://youtu.be/pMNVQIZa-G8?t=3416) 很多 JPEG 的設計是基於人眼的特性（之後專講），所以今天講的是「簡化版 JPEG」。

### 9.2 第一步：顏色轉換

[▶ 57:33](https://youtu.be/pMNVQIZa-G8?t=3453) RGB 三個通道也**高度相關**（有一樣的空間結構），何必分開存？把 RGB **色彩空間**轉成 **Y'CbCr** [▶ 57:33](https://youtu.be/pMNVQIZa-G8?t=3453)：

- **Y**（luma，亮度）：存「平均值」，大致是灰階影像，抓住結構 [▶ 58:23](https://youtu.be/pMNVQIZa-G8?t=3503)。（講者說今天先當它是平均值，其實不完全是。）
- **Cb、Cr**（chroma，色度）：存顏色 [▶ 59:02](https://youtu.be/pMNVQIZa-G8?t=3542)。

這立刻改善了顏色之間的去相關。

【投影片補充】`L15.pdf`：為什麼轉成 YCbCr？人的因素：(1) 基於顏色視覺**對立歷程理論**（opponent process theory）的感知色彩空間；(2) Y、Cb、Cr 通道的**對比敏感度**不同。也叫 Y'CbCr、YUV、Y'UV [▶ 1:02:41](https://youtu.be/pMNVQIZa-G8?t=3761)（講者說它們今天當成一樣，有很多歷史背景）。

### 9.3 第二步：色度降取樣

[▶ 59:02](https://youtu.be/pMNVQIZa-G8?t=3542) 結合本講一開始的降取樣：轉成 Y'UV 後，**只對色度通道降取樣** [▶ 59:47](https://youtu.be/pMNVQIZa-G8?t=3587)。

> 亮度通道已經有大部分結構；人對**結構**的改變比對**顏色**的改變敏感。顏色量化時也看到：丟掉很多顏色資訊，失真不太增加 [▶ 59:47](https://youtu.be/pMNVQIZa-G8?t=3587)。

「4:2:0」這種記號在講人的那一講解釋 [▶ 1:00:27](https://youtu.be/pMNVQIZa-G8?t=3627)。這是**第一個根據人眼特性做的具體設計決定**：人眼對顏色沒有對亮度那麼敏感 [▶ 1:03:17](https://youtu.be/pMNVQIZa-G8?t=3797)。

**數字例子** [▶ 1:01:02](https://youtu.be/pMNVQIZa-G8?t=3662)（四張品質差不多）：

| 處理 | 大小 |
|---|---|
| 原圖 | 429 KB |
| 不做降取樣、直接 JPEG | 323 KB |
| 色度降取樣 + JPEG | **176 KB** [▶ 1:01:36](https://youtu.be/pMNVQIZa-G8?t=3696) |

[▶ 1:02:09](https://youtu.be/pMNVQIZa-G8?t=3729) 好處有**兩層**：(1) 直接丟掉樣本；(2) 降取樣等於低通濾波，資料**更相關**，下游壓縮器能壓得更好。幾乎一半大小，品質差不多 [▶ 1:02:41](https://youtu.be/pMNVQIZa-G8?t=3761)。

### 9.4 第三步：8×8 區塊 2D-DCT

[▶ 1:04:22](https://youtu.be/pMNVQIZa-G8?t=3862)

1. 把影像切成 **8×8** 的區塊（**8×8 像素**，見下面的 Q&A）。
2. **減 128**，讓像素值以 0 為中心（8 位元有 256 個值）[▶ 1:04:55](https://youtu.be/pMNVQIZa-G8?t=3895)。
3. 對每個區塊做 2D-DCT [▶ 1:05:29](https://youtu.be/pMNVQIZa-G8?t=3929)。

例：一個灰階 8×8 區塊，值從 94（暗）到 221、230（亮）[▶ 1:05:29](https://youtu.be/pMNVQIZa-G8?t=3929)。

**可分離的實作** [▶ 1:06:02](https://youtu.be/pMNVQIZa-G8?t=3962)：先對每一**列**做 1D-DCT，再對每一**行**做 1D-DCT [▶ 1:06:35](https://youtu.be/pMNVQIZa-G8?t=3995)，合起來就是 2D-DCT。

【Q&A】[▶ 1:06:35](https://youtu.be/pMNVQIZa-G8?t=3995) 學生問：8×8 區塊是 8×8 個像素，還是把整張圖切成 8×8 份？講者：**8×8 個像素** [▶ 1:07:10](https://youtu.be/pMNVQIZa-G8?t=4030)。整張圖比較大，切成很多 8×8 像素的區塊，一次處理一個。這在影像壓縮裡到處出現。

[▶ 1:07:48](https://youtu.be/pMNVQIZa-G8?t=4068) 2D 轉換後的係數有正有負，實作時要處理正負號。

**複雜度** [▶ 1:08:28](https://youtu.be/pMNVQIZa-G8?t=4108)：不可分離時是 $n^2\times n^2=64\times64$ 的矩陣；可分離時只要兩次 8×8 的一維轉換，**$2\times8\times8$ 而不是 $64\times64$** [▶ 1:08:28](https://youtu.be/pMNVQIZa-G8?t=4108)。

### 9.5 第四步：量化

[▶ 1:09:09](https://youtu.be/pMNVQIZa-G8?t=4149) 這一步決定率和失真的取捨；有些壓縮器叫它**碼率控制器**（rate controller）[▶ 1:09:09](https://youtu.be/pMNVQIZa-G8?t=4149)。

JPEG 用**固定的量化表**，對每個係數做**均勻純量量化**：除以表裡的數，取整數 [▶ 1:09:53](https://youtu.be/pMNVQIZa-G8?t=4193)。例：338 除以 16；−10 除以 99 → 0。

量化表的值是事先決定的（大量人眼實驗調出來的），但有明顯規律 [▶ 1:10:27](https://youtu.be/pMNVQIZa-G8?t=4227)：

> **右下（高頻）的數比左上（低頻）大很多**：高頻量化得更狠。回想注水。

[▶ 1:10:58](https://youtu.be/pMNVQIZa-G8?t=4258) 不同壓縮率用**不同的量化表**；表一固定，率大致就固定了。表的設計依據注水 + 人眼特性。下一份作業會讓大家自己玩 [▶ 1:11:31](https://youtu.be/pMNVQIZa-G8?t=4291)。

### 9.6 第五步：無損編碼

[▶ 1:11:31](https://youtu.be/pMNVQIZa-G8?t=4291) 量化後是整數（離散訊號），有很多 0，可以無損地壓。JPEG 用**修改過的 Huffman 編碼**，相當複雜 [▶ 1:12:11](https://youtu.be/pMNVQIZa-G8?t=4331)。

**主要想法：行程編碼 + Huffman** [▶ 1:12:11](https://youtu.be/pMNVQIZa-G8?t=4331)：

1. **之字形掃描**（zigzag）：照之字形走，相鄰的係數比較相關；照 $x$ 走完再回頭，兩個像素會隔很遠 [▶ 1:12:11](https://youtu.be/pMNVQIZa-G8?t=4331)。
2. **行程編碼**（run-length encoding）[▶ 1:12:48](https://youtu.be/pMNVQIZa-G8?t=4368)：例如 `90, -40, 0, 0, 0, 5, …` 寫成 `90, -40, 三個 0, 5, …`，不用一個一個存 0。
3. JPEG 再進一步存**三元組** [▶ 1:13:29](https://youtu.be/pMNVQIZa-G8?t=4409)：
   - 第 1 個數：這個非零值**前面有幾個 0**；
   - 第 2 個數：這個值的**位元長度**（約 $\log_2$ 值）[▶ 1:14:36](https://youtu.be/pMNVQIZa-G8?t=4476)；
   - 第 3 個數：值本身。

> ⚠️ 逐字稿缺字 [▶ 1:14:05](https://youtu.be/pMNVQIZa-G8?t=4445)：講者說他剛剛示範的行程編碼走錯了順序，例子只是為了說明行程編碼的想法。

**為什麼這樣做** [▶ 1:15:19](https://youtu.be/pMNVQIZa-G8?t=4519)：直接對值做 Huffman，值可能有 0–255 種，Huffman 樹可能很深、很不平衡，事先也不知道長什麼樣。改成**只對長度做 Huffman 編碼，值本身照原樣存成位元**，Huffman 表的複雜度大降 [▶ 1:16:06](https://youtu.be/pMNVQIZa-G8?t=4566)。（Shubham 講 gzip 時也提過類似的做法。）【投影片補充】`L15.pdf`：「Huffman Encode the length; store the value as-is in bits」。

**還有很多細節** [▶ 1:16:06](https://youtu.be/pMNVQIZa-G8?t=4566)：

- 係數的正負號。
- **DC 和 AC 分開處理**：DC 變化比 AC 平滑，而且 DC（平均值）更重要。各有不同的 Huffman 表 [▶ 1:16:44](https://youtu.be/pMNVQIZa-G8?t=4604)。
- **跨區塊**：DC 會跨區塊一起編，AC 不會。
- 亮度 vs. 色度通道、色度降取樣。

【口頭】[▶ 1:16:44](https://youtu.be/pMNVQIZa-G8?t=4604) 從頭到尾寫一個 JPEG 可不是開玩笑，但主要想法都能理解。

### 9.7 總結與假影

[▶ 1:17:20](https://youtu.be/pMNVQIZa-G8?t=4640)（`L15.pdf`）

- **顏色轉換**：RGB → YUV。
- **顏色通道**各自獨立編碼。
- **區塊編碼**：每個 8×8 區塊**幾乎**獨立編碼（DC 係數除外）。
- **Huffman / 算術編碼**：JPEG 也支援算術編碼，但很少用；Huffman 的用法有很多細節 [▶ 1:17:53](https://youtu.be/pMNVQIZa-G8?t=4673)。

[▶ 1:17:53](https://youtu.be/pMNVQIZa-G8?t=4673) 80 倍壓縮的 JPEG 有很多**方形的**假影：每個 8×8 區塊獨立處理，邊界就會不連續，非常顯眼 [▶ 1:18:31](https://youtu.be/pMNVQIZa-G8?t=4711)。

[▶ 1:18:31](https://youtu.be/pMNVQIZa-G8?t=4711) JPEG 解碼器的規格：要告訴它高寬、Huffman 表（或足以建出 Huffman 表的資訊，像作業 1 那題）、量化表，然後才是影像資料 [▶ 1:19:05](https://youtu.be/pMNVQIZa-G8?t=4745)。

---

## 10. BPG：怎麼改進 JPEG

[▶ 1:19:40](https://youtu.be/pMNVQIZa-G8?t=4780) JPEG 在設計當時（計算資源有限）非常好，但有明顯可改進之處。**BPG** 做了兩件事：

1. **更大、可變大小的區塊** [▶ 1:19:40](https://youtu.be/pMNVQIZa-G8?t=4780)：不死守 8×8。格紋那種區域 8×8 內沒什麼相關；很平滑的區域可以用大區塊，把更多東西推到低頻，去相關更好 [▶ 1:20:15](https://youtu.be/pMNVQIZa-G8?t=4815)。
2. **區塊不獨立** [▶ 1:20:50](https://youtu.be/pMNVQIZa-G8?t=4850)：用前面的區塊**預測**下一個（預測編碼）。

[▶ 1:20:50](https://youtu.be/pMNVQIZa-G8?t=4850) 這兩個限制都直接來自轉換編碼和量化的基本道理。137 倍時 JPEG 慘不忍睹，BPG 在 8 KB 好很多 [▶ 1:21:27](https://youtu.be/pMNVQIZa-G8?t=4887)。

[▶ 1:21:27](https://youtu.be/pMNVQIZa-G8?t=4887) 一張兔子圖的 BPG 示意：

- **不同大小的區塊**：大片平坦區用大區塊，變化多的地方用小區塊，更能利用注水 [▶ 1:22:01](https://youtu.be/pMNVQIZa-G8?t=4921)。
- **預測**：兩個幾乎一樣的區塊，存前一個就完成大部分工作，轉換係數要存的更少 [▶ 1:22:01](https://youtu.be/pMNVQIZa-G8?t=4921)。

【投影片補充】`L15.pdf`：BPG 就是 H.265（HEVC）的 I-frame（畫面內編碼）。

### 10.1 預告

[▶ 1:22:40](https://youtu.be/pMNVQIZa-G8?t=4960) 感恩節後是學習式影像壓縮。作業 4 只考到今天。接下來三講比較進階 [▶ 1:22:40](https://youtu.be/pMNVQIZa-G8?t=4960)：

1. 我們一直只用**線性**轉換，也許可以超越線性 [▶ 1:23:19](https://youtu.be/pMNVQIZa-G8?t=4999)。
2. JPEG 有大量**手工參數**：轉 Y'UV、UV 降取樣 2 倍、每個率一張固定的量化表，64 個值都是有人決定「這裡放 30」，應該能做得更好 [▶ 1:23:52](https://youtu.be/pMNVQIZa-G8?t=5032)。

---

## 11. 一頁速查表

### 影像基本量

- $H\times W\times3$ 位元組；例 $764\times512\times3\approx1.1$ MB。
- JPEG 40× 看不出來、80× 方塊假影、137× 爛；BPG/ML 在 137× 好很多。

### 簡單的方法

| 方法 | 做法 | 效果 |
|---|---|---|
| 降取樣 | 高寬除以 $D$，解碼端插值 | 4× 起；240p…4K 就是這個旋鈕 |
| 顏色量化 | RGB 向量量化成 256 / 16 色 | 3× / 6× |
| Color Cell（1984） | 4×4 區塊 2 色 + 每像素 1 位元 | 2 bpp，12× |

### 2D-DCT

- $n\times n$ 區塊、$n^2\times n^2$ 矩陣；**可分離**：列 1D-DCT 再行 1D-DCT，$2n^2$ 而非 $n^4$（8×8：128 vs. 4096）。
- 左上 DC = 平均；往右水平頻率↑（垂直條紋），往下垂直頻率↑（水平條紋）。
- 自然影像 DCT 稀疏、能量在低頻；雜訊影像不稀疏。

### JPEG 流程

| 步驟 | 做法 | 理由 |
|---|---|---|
| 1 顏色轉換 | RGB → Y'CbCr | 通道去相關；人眼特性 |
| 2 色度降取樣 | 只降 Cb、Cr（如 4:2:0） | 人眼對顏色不如對亮度敏感；429→176 KB |
| 3 DCT | 8×8、減 128、可分離 2D-DCT | 去相關、能量集中 |
| 4 量化 | 除以量化表、取整；高頻除數大 | 唯一有損步驟；注水 + 人眼 |
| 5 熵編碼 | 之字形 + 行程 + (0 的個數, 位元長度, 值)；Huffman 只編長度；DC/AC 分開 | 降低 Huffman 表複雜度 |

假影：8×8 區塊獨立 ⇒ 方塊效應。

### BPG（H.265 I-frame）

更大、可變區塊 + 區塊間預測。

### MSE 的問題

同 MSE 的五張圖，人眼偏好差很多 ⇒ 需要感知失真（第 17 集）。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 非線性、學出來的轉換；不用手工量化表 | 第 16 集學習式影像壓縮 |
| 4:2:0、對立歷程、對比敏感度、MSE 不對 | 第 17 集 Humans and Compression |
| 區塊間預測、I-frame | 第 18 集影片壓縮（I/P/B 畫面） |
| 降取樣 + 升取樣當率失真旋鈕 | 第 18 集串流 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **一張 1.1 MB 的影像用 JPEG 壓 40 倍幾乎看不出來：先把 RGB 轉成亮度 + 色度並把色度降取樣（人眼對顏色不敏感，而且降取樣讓資料更相關），再對每個 8×8 區塊減 128 做可分離的 2D-DCT，用高頻除數大的量化表做純量量化，最後之字形掃描、行程編碼、只對長度做 Huffman。獨立處理 8×8 區塊會造成方塊假影；BPG 用可變大小的區塊和區塊間預測大幅改進。而 MSE 並不符合人眼，這是後兩講的主題。**

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 15 錄影逐字稿（人工字幕，1:24:15）與投影片 L15、L15_ann 整理。*
