---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 17
lecture: Lecture 17
date: 2023-11-29
video: https://youtu.be/LE6GLWv63wc
notes: 投影片 slide_17_2023.pdf；課本沒有這部分
---

# 第 17 集 · Lecture 17：人與壓縮（Humans and Compression） [▶ 影片](https://youtu.be/LE6GLWv63wc)

← 上一集：[16-learnt-image-compression](16-learnt-image-compression.md) ｜ [總目錄](README.md) ｜ 下一集：[18-video-compression](18-video-compression.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 17 集
> **講者**：Pulkit Tandon
> **來源**：YouTube 錄影逐字稿（1:18:39，人工字幕 en-US；有幾處「[AUDIO OUT]」）＋ 投影片 `slide_17_2023.pdf`。課本沒有這部分。
> **標記說明**：
> - `【口頭】` 講者口頭補充，投影片沒有
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 兩個引子](#1-兩個引子)
- [2. 人眼怎麼運作](#2-人眼怎麼運作)
- [3. 桿細胞、錐細胞、中央窩](#3-桿細胞錐細胞中央窩)
- [4. 顏色：三色說與對立歷程說](#4-顏色三色說與對立歷程說)
- [5. 回頭看 JPEG：為什麼轉 YCbCr、為什麼色度降取樣](#5-回頭看-jpeg為什麼轉-ycbcr為什麼色度降取樣)
- [6. 讀懂一個 JPEG 檔](#6-讀懂一個-jpeg-檔)
- [7. 感知失真度量](#7-感知失真度量)
- [8. 率–失真–感知取捨](#8-率失真感知取捨)
- [9. 結語](#9-結語)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/LE6GLWv63wc?t=5) 有損壓縮的**人的角度**，特別是視覺。資訊理論課通常不講，但會出現在實用的有損壓縮器裡 [▶ 00:05](https://youtu.be/LE6GLWv63wc?t=5)。

[▶ 01:21](https://youtu.be/LE6GLWv63wc?t=81) 目前大多用 MSE。但**多媒體最終是給人用的**，人的感官在多媒體有損壓縮器的設計裡扮演重要角色 [▶ 01:55](https://youtu.be/LE6GLWv63wc?t=115)。今天要問 [▶ 01:55](https://youtu.be/LE6GLWv63wc?t=115)：

1. JPEG 的某些設計為什麼這樣做？
2. 知道最終是給人看的，怎麼進一步改進影像、影片壓縮？
3. MSE 不是萬能的，業界還有哪些選擇 [▶ 02:26](https://youtu.be/LE6GLWv63wc?t=146)？

【投影片補充】`slide_17_2023.pdf`：本講的內容有些是神經科學和心理視覺文獻的「很直覺、不嚴謹」的介紹。

---

## 1. 兩個引子

### 1.1 MP3 為什麼是雙聲道、44.1 kHz？【課堂討論】

[▶ 02:59](https://youtu.be/LE6GLWv63wc?t=179) 用 MediaInfo 看一個壓縮過的寶可夢主題曲 MP3：格式是 MPEG Audio（音訊界的 JPEG），**兩個聲道**、**取樣率 44.1 kHz** [▶ 02:59](https://youtu.be/LE6GLWv63wc?t=179)。

學生答：人耳聽到約 20 kHz，44 kHz 就能精確表示到約 22 kHz [▶ 03:34](https://youtu.be/LE6GLWv63wc?t=214)。講者：

- **兩個聲道**：因為人有兩隻耳朵；人若有三隻耳朵，大概就會用三聲道 [▶ 03:34](https://youtu.be/LE6GLWv63wc?t=214)。這個簡單事實直接影響檔案大小（不壓縮就是兩倍）[▶ 04:10](https://youtu.be/LE6GLWv63wc?t=250)。
- **44.1 kHz** [▶ 04:10](https://youtu.be/LE6GLWv63wc?t=250)：人聽得到 20 Hz–20 kHz（講者說他不認識真的聽得到 20 kHz 的人）。**Nyquist 準則**：要不失真（無混疊）地表示，取樣率要是最高頻率的兩倍 [▶ 04:45](https://youtu.be/LE6GLWv63wc?t=285)，所以 40 kHz；低通濾波器不完美，要留一點餘裕，所以多一點；44.1 這個數能被 2、3、5 等多個質數整除，之後降取樣比較容易 [▶ 04:45](https://youtu.be/LE6GLWv63wc?t=285)。

[▶ 05:20](https://youtu.be/LE6GLWv63wc?t=320) 這個看似隨意的數字是有人認真想過的，現在是預設值，每個 MP3 都受它影響。

### 1.2 同樣 MSE 的五張圖

[▶ 05:53](https://youtu.be/LE6GLWv63wc?t=353) 上一講的那張圖：B–F 和原圖 A 的 MSE 都一樣，但 B 顯然好很多；C、E 太平滑，D、E、F 撒滿雜訊 [▶ 06:33](https://youtu.be/LE6GLWv63wc?t=393)。不考慮人眼就可能設計出產生這種重建的壓縮器，那是糟糕的設計 [▶ 07:05](https://youtu.be/LE6GLWv63wc?t=425)。

[▶ 07:05](https://youtu.be/LE6GLWv63wc?t=425) 接下來：(1) 人眼怎麼運作、它在傳統壓縮器設計裡的角色；(2) 感知度量；(3) 怎麼把感知放進率失真框架。

---

## 2. 人眼怎麼運作

### 2.1 光學：天生的低通濾波

[▶ 07:41](https://youtu.be/LE6GLWv63wc?t=461) 角膜、瞳孔、晶狀體把光聚焦到眼睛後方的**視網膜**；視網膜把光**轉換**成電訊號，經**視神經**送到大腦 [▶ 08:14](https://youtu.be/LE6GLWv63wc?t=494)。

[▶ 08:14](https://youtu.be/LE6GLWv63wc?t=494) 一個只有單點的光源（像素的 delta 函數），到了視網膜上**不再是 delta**，而是**散開** [▶ 08:51](https://youtu.be/LE6GLWv63wc?t=531)：

> **眼睛一開始就因為光學物理做了低通濾波。** 很多靠很近的線本來就分辨不出來，所以保留極高頻的東西沒有意義 [▶ 08:51](https://youtu.be/LE6GLWv63wc?t=531)。

[▶ 09:24](https://youtu.be/LE6GLWv63wc?t=564) 有趣的是自然訊號本身的高頻能量也很低；可以說人被設計成接收這種訊號，但這也就是基本光學。

### 2.2 視網膜不是相機

[▶ 09:57](https://youtu.be/LE6GLWv63wc?t=597) 視網膜放大看：光先落在**感光細胞**（photoreceptors），把光（波長）轉成電訊號 [▶ 09:57](https://youtu.be/LE6GLWv63wc?t=597)；再經過很多神經元，**視網膜神經節細胞**（retinal ganglion cells, RGC），發出電脈衝送到大腦 [▶ 10:39](https://youtu.be/LE6GLWv63wc?t=639)。

[▶ 10:39](https://youtu.be/LE6GLWv63wc?t=639) **第二個大差別**：我們把影像想成像素陣列（每像素三個 RGB 值），但人不是這樣感知的 [▶ 11:13](https://youtu.be/LE6GLWv63wc?t=673)：

- 大約有 **20 種** RGC，每一種各自**鋪滿整個視野**，各自送一條獨立的訊號到視覺皮質 [▶ 11:13](https://youtu.be/LE6GLWv63wc?t=673)。
- 也就是說，不同類的細胞在**擷取視覺場景的不同特徵**（很多細節還有爭議）[▶ 11:49](https://youtu.be/LE6GLWv63wc?t=709)。

> 人在視網膜就已經有特徵擷取器，再由視覺皮質建立更複雜的關聯。**人的視網膜不是相機，不只是像素陣列** [▶ 12:27](https://youtu.be/LE6GLWv63wc?t=747)。

---

## 3. 桿細胞、錐細胞、中央窩

### 3.1 桿細胞：亮度與動態範圍

[▶ 12:59](https://youtu.be/LE6GLWv63wc?t=779) **桿細胞**（rods）只負責編碼**亮度**（intensity），沒有顏色資訊；數量很多（投影片：約 $100\times10^6$）；能適應約 **$10^9$** 的動態範圍 [▶ 13:35](https://youtu.be/LE6GLWv63wc?t=815)。

例 [▶ 13:35](https://youtu.be/LE6GLWv63wc?t=815)：從加州夏天的大太陽下衝進一間暗教室，一開始幾秒什麼都看不到，然後眼睛就適應了。外面的亮度極高、所有東西都在一個很高的基準附近變化；進到暗室亮度大跌，變成在一個很低的基準附近變化 [▶ 14:06](https://youtu.be/LE6GLWv63wc?t=846)。相機到今天都還在和這個問題奮鬥（iPhone 的賣點之一就是夜拍）[▶ 14:37](https://youtu.be/LE6GLWv63wc?t=877)；人卻自然做到，桿細胞的工作就是適應亮度、調整基準 [▶ 14:37](https://youtu.be/LE6GLWv63wc?t=877)。

**盲點** [▶ 15:16](https://youtu.be/LE6GLWv63wc?t=916)：視神經連接的地方沒有感光細胞，落在那裡的東西看不到。【口頭】可以自己試：盯著前方、移動大拇指，到某個角度大拇指會消失再出現 [▶ 15:49](https://youtu.be/LE6GLWv63wc?t=949)。

### 3.2 錐細胞：顏色與細節，只在中央窩

[▶ 16:21](https://youtu.be/LE6GLWv63wc?t=981) 感光細胞密度對角度的圖：

- **桿細胞**幾乎遍布整個視網膜，除了盲點（約 20 度）。
- **錐細胞**（cones）負責**顏色和細節**；幾乎只出現在 **0 度附近**的極小區域，叫**中央窩**（fovea）[▶ 16:56](https://youtu.be/LE6GLWv63wc?t=1016)（投影片：約 $5\times10^6$ 個）。

[▶ 17:29](https://youtu.be/LE6GLWv63wc?t=1049) 高解析度視覺只在一個很小的角度裡，那為什麼我們看到的畫面平滑又清楚？

### 3.3 掃視與 foveation

[▶ 18:05](https://youtu.be/LE6GLWv63wc?t=1085) 因為我們**從來不是在看靜態畫面**：任何時刻都在看「影片」，眼睛做著很快的**掃視運動**（saccadic movements），不斷把場景的不同點對準中央窩 [▶ 18:45](https://youtu.be/LE6GLWv63wc?t=1125)；大腦再把這些訊號內插成連續平滑的畫面 [▶ 19:17](https://youtu.be/LE6GLWv63wc?t=1157)。（講者：我如果很刻意地只盯著時鐘，你們的臉就消失了 [▶ 18:45](https://youtu.be/LE6GLWv63wc?t=1125)。）

[▶ 19:49](https://youtu.be/LE6GLWv63wc?t=1189) 這叫 **foveation**（中央窩取樣）。**在壓縮上的利用** [▶ 20:27](https://youtu.be/LE6GLWv63wc?t=1227)：如果能**追蹤眼球**、延遲又夠低，就知道這一秒眼睛在看哪裡；那裡多給位元，其他地方給很少，甚至 0。聽起來像科幻，但近年 **VR** 很多研究在做這件事：3D 環境裡周邊不需要和中心一樣多的位元 [▶ 21:08](https://youtu.be/LE6GLWv63wc?t=1268)。

### 3.4 Weber 定律

[▶ 21:46](https://youtu.be/LE6GLWv63wc?t=1306) 適應性的另一面：**Weber 定律**：人只在乎**相對**變化，不在乎絕對變化 [▶ 21:46](https://youtu.be/LE6GLWv63wc?t=1306)。

> 同樣改 1 個位元，在**高亮度**時不明顯，在**低亮度**時很明顯 [▶ 22:22](https://youtu.be/LE6GLWv63wc?t=1342)。

所以位元分配要小心：均勻分配的話，低亮度區的假影可能看得到 [▶ 22:22](https://youtu.be/LE6GLWv63wc?t=1342)。[▶ 23:04](https://youtu.be/LE6GLWv63wc?t=1384) 4K、HD 時代這些效應更重要，大公司花大錢研究，因為每省一位元或提升使用體驗都是錢。

---

## 4. 顏色：三色說與對立歷程說

### 4.1 三種錐細胞 → RGB

[▶ 23:35](https://youtu.be/LE6GLWv63wc?t=1415) 錐細胞對不同波長的反應（橫軸 400–700 nm 左右的可見光）：**三種錐細胞**，叫 **L、M、S**（長、中、短波長）[▶ 24:44](https://youtu.be/LE6GLWv63wc?t=1484)。

【課堂討論】[▶ 24:44](https://youtu.be/LE6GLWv63wc?t=1484) 為什麼有三種錐細胞？答案就在投影片上。[▶ 25:21](https://youtu.be/LE6GLWv63wc?t=1521) 你可能想過「為什麼是 RGB？」：**因為人的錐細胞有三種，大致取樣紅、綠、藍** [▶ 25:21](https://youtu.be/LE6GLWv63wc?t=1521)。1700 年代的哲學家透過心理視覺實驗就發現 RGB 在視覺裡有特殊地位，後來神經科學測出它們的反應特性。所以不是因為有 RGB 才這樣，而是反過來 [▶ 25:55](https://youtu.be/LE6GLWv63wc?t=1555)。這叫**三色說**（trichromatic theory）[▶ 25:55](https://youtu.be/LE6GLWv63wc?t=1555)。

### 4.2 色彩空間

[▶ 26:35](https://youtu.be/LE6GLWv63wc?t=1595) 同一個顏色可以用 RGB（**加法**色彩空間）表示，也可以用 **CMYK**（舊式印表機、**減法**色彩空間：C、M、Y 加起來是黑）表示 [▶ 27:07](https://youtu.be/LE6GLWv63wc?t=1627)。

[▶ 27:42](https://youtu.be/LE6GLWv63wc?t=1662) 這是很多心理物理學研究的主題。**CIE 1931 色度圖**（chromaticity diagram）用二維表示顏色 [▶ 28:17](https://youtu.be/LE6GLWv63wc?t=1697)：

- 黃色的馬蹄形區域是**人眼看得到的顏色** [▶ 28:53](https://youtu.be/LE6GLWv63wc?t=1733)。
- 實務上表示不了那麼多：RGB、**sRGB**（黑線）、**Adobe RGB** 等標準各涵蓋一個三角形 [▶ 28:53](https://youtu.be/LE6GLWv63wc?t=1733)。

[▶ 29:25](https://youtu.be/LE6GLWv63wc?t=1765) 為什麼要講這些？數位值（例如 224, 102, 102）最終要由螢幕、印表機轉成物理訊號，相機記錄時也是把物理訊號轉成 RGB 值，這些都**取決於色彩空間** [▶ 29:58](https://youtu.be/LE6GLWv63wc?t=1798)。螢幕的色彩空間和記錄時不同，重建就完全不同，**失真也就完全不同** [▶ 29:58](https://youtu.be/LE6GLWv63wc?t=1798)。做影像、影片壓縮時常有很奇怪的 bug：你以為是 Huffman 編碼器壞了，其實是色彩空間的問題 [▶ 30:32](https://youtu.be/LE6GLWv63wc?t=1832)。

### 4.3 那件洋裝，還有對立歷程說【課堂討論】

[▶ 30:32](https://youtu.be/LE6GLWv63wc?t=1832) 那件爆紅的洋裝：有人看成**金白**、有人看成**藍黑**，但 RGB 值一模一樣 [▶ 31:05](https://youtu.be/LE6GLWv63wc?t=1865)。

[▶ 31:38](https://youtu.be/LE6GLWv63wc?t=1898) **Lilac chaser 錯覺**：一圈紫色圓點，一個一個消失。盯著中間的 X：學生說看到黃點、一整圈黃點；講者說他會叫它綠色，大概是黃綠色 [▶ 32:13](https://youtu.be/LE6GLWv63wc?t=1933)、[▶ 32:44](https://youtu.be/LE6GLWv63wc?t=1964)。眼睛沒問題，不用換眼鏡，這是已知的**後像效應**（after images）：盯著一個顏色，眼睛會適應把它減掉，所以看別處時會看到它的「負片」[▶ 33:20](https://youtu.be/LE6GLWv63wc?t=2000)。

> **對立歷程說**（opponent process theory）[▶ 32:44](https://youtu.be/LE6GLWv63wc?t=1964)：有幾對顏色互為負片。三種錐細胞的訊號被**合併**成：
> - **白–黑**（大致是三種的和）；
> - **藍–黃**；
> - **紅–綠** [▶ 34:27](https://youtu.be/LE6GLWv63wc?t=2067)。

[▶ 34:59](https://youtu.be/LE6GLWv63wc?t=2099) 這個理論有大量經驗證據，也一直有爭議（講者說到 2019 年左右還有論文說它對或錯，從 1800 年代爭到現在），但工程上我們就用它。這正是 **YUV** 的來源 [▶ 33:56](https://youtu.be/LE6GLWv63wc?t=2036)。

---

## 5. 回頭看 JPEG：為什麼轉 YCbCr、為什麼色度降取樣

### 5.1 為什麼轉 YCbCr

[▶ 35:33](https://youtu.be/LE6GLWv63wc?t=2133) Y'UV、YCbCr、Y'CbCr 今天都當成一樣 [▶ 36:08](https://youtu.be/LE6GLWv63wc?t=2168)。對照對立歷程說：**Y 是亮度**、**Cb 對應藍–黃**、**Cr 對應紅–綠**：等於在模仿人眼，拆成三條我們認為人眼使用的獨立通道 [▶ 36:08](https://youtu.be/LE6GLWv63wc?t=2168)。

【投影片補充】`slide_17_2023.pdf`：轉 YCbCr 的兩個理由：(1) 基於對立歷程說的**感知色彩空間**；(2) Y、Cb、Cr 通道有**不同的對比敏感度** [▶ 37:16](https://youtu.be/LE6GLWv63wc?t=2236)。

### 5.2 對比敏感度

[▶ 37:50](https://youtu.be/LE6GLWv63wc?t=2270) 就像人耳聽 20 Hz–20 kHz，人眼對**空間頻率**和**對比**（某點附近的變異、亮度改變多少）也有範圍 [▶ 38:27](https://youtu.be/LE6GLWv63wc?t=2307)。

[▶ 38:27](https://youtu.be/LE6GLWv63wc?t=2307) 一張圖：往右空間頻率越來越高的條紋、往下對比越來越大。紅線是一般人的界線：紅線內分得出條紋，外面看起來是一片灰 [▶ 38:59](https://youtu.be/LE6GLWv63wc?t=2339)。（講者說有些區域他自己都看不到。）

【課堂討論】[▶ 39:30](https://youtu.be/LE6GLWv63wc?t=2370) 為什麼設計壓縮器時在乎這個？學生答：反正看不到的東西就可以壓 [▶ 39:30](https://youtu.be/LE6GLWv63wc?t=2370)。講者：對。落在看不到的區域，MSE 再高也沒關係，人不在乎 [▶ 40:07](https://youtu.be/LE6GLWv63wc?t=2407)。

[▶ 40:07](https://youtu.be/LE6GLWv63wc?t=2407) **亮度 vs. 色度的對比敏感度曲線**：**色度的敏感度隨空間頻率下降得快很多** [▶ 40:07](https://youtu.be/LE6GLWv63wc?t=2407)。所以：

1. **高頻 DCT 係數量化得更狠**：「人看不到高頻」的定量版本 [▶ 40:39](https://youtu.be/LE6GLWv63wc?t=2439)。
2. **色度降取樣**：色度不需要高解析度。
3. **亮度和色度用不同的量化矩陣**（課堂之前只口頭提過），率失真取捨的設計不同 [▶ 41:14](https://youtu.be/LE6GLWv63wc?t=2474)。

JPEG 全都用了 [▶ 41:47](https://youtu.be/LE6GLWv63wc?t=2507)。

### 5.3 數字和 4:2:0

[▶ 41:47](https://youtu.be/LE6GLWv63wc?t=2507) 上一講的例子：

| 處理 | 大小 |
|---|---|
| 原圖 | 429 KB |
| 不降取樣、JPEG | 323 KB |
| 只做色度降取樣（不 JPEG） | 352 KB（看不出差別）[▶ 42:23](https://youtu.be/LE6GLWv63wc?t=2543) |
| 色度降取樣 + JPEG | 176 KB [▶ 42:55](https://youtu.be/LE6GLWv63wc?t=2575) |

（講者口頭說成 kilobit，投影片上一講寫 KB；好處相乘：直接丟樣本，加上降取樣後更相關、更好壓 [▶ 43:29](https://youtu.be/LE6GLWv63wc?t=2609)。）

[▶ 43:29](https://youtu.be/LE6GLWv63wc?t=2609) **4:4:4、4:2:2、4:2:0** 描述色度怎麼降取樣：

- **4:4:4**：全解析度，每個像素有自己的 Y、Cb、Cr [▶ 43:29](https://youtu.be/LE6GLWv63wc?t=2609)。
- **4:2:0**：Y 不變；色度取 **2×2 的平均**，八個像素的顏色只剩兩個 [▶ 44:06](https://youtu.be/LE6GLWv63wc?t=2646)。很多影像、影片壓縮器的**預設**就是 4:2:0 [▶ 44:37](https://youtu.be/LE6GLWv63wc?t=2677)。

### 5.4 色度降取樣的假影

[▶ 44:37](https://youtu.be/LE6GLWv63wc?t=2677) 要小心：

- 4 個紅色像素、其他是藍色，降到 4:2:0 會出現**顏色錯誤**的假影 [▶ 45:10](https://youtu.be/LE6GLWv63wc?t=2710)。
- **終端機截圖**（「The quick brown fox jumps over the lazy dog」）：2×2 平均後邊緣還在，但**顏色本身變了** [▶ 45:44](https://youtu.be/LE6GLWv63wc?t=2744)。MSE 不一定很高，但這非常有損 [▶ 45:44](https://youtu.be/LE6GLWv63wc?t=2744)。

### 5.5 RGB → YUV 到底怎麼算

[▶ 46:54](https://youtu.be/LE6GLWv63wc?t=2814) 沒那麼簡單，因為色彩空間一團亂 [▶ 47:28](https://youtu.be/LE6GLWv63wc?t=2848)：不同標準用不同的矩陣，例如 SDTV 用 **ITU-R BT.601**、HDTV（sRGB）用 **ITU-R BT.709**（投影片）[▶ 47:28](https://youtu.be/LE6GLWv63wc?t=2848)。實務上不注意轉換用的色彩空間，就會出很奇怪的 bug [▶ 48:01](https://youtu.be/LE6GLWv63wc?t=2881)。

> 以下**不是逐字稿內容**，是補一個常見例子（投影片上的矩陣是圖片，這裡寫的是 BT.601 亮度的常見係數）：$Y'=0.299R'+0.587G'+0.114B'$。綠色權重最大，因為人眼對綠色最敏感；BT.709 的係數不同。

---

## 6. 讀懂一個 JPEG 檔

[▶ 48:01](https://youtu.be/LE6GLWv63wc?t=2881) 用 ExifTool 看 Stanford 標誌的 JPEG [▶ 48:35](https://youtu.be/LE6GLWv63wc?t=2915)。上完這門課應該能解釋它的各個欄位：

| 欄位 | 值 | 意思 |
|---|---|---|
| Color Space | sRGB | 色彩空間（§4.2） |
| Encoding Process | Baseline DCT, Huffman coding | 第 15 集的流程 [▶ 49:09](https://youtu.be/LE6GLWv63wc?t=2949) |
| Bits Per Sample | 8 | 不是 12 位元的 HDR |
| Color Components | 3 | 沒有 alpha 通道 |
| YCbCr Sub Sampling | 4:2:0 | 網路下載的圖幾乎都是這個預設 [▶ 49:44](https://youtu.be/LE6GLWv63wc?t=2984) |

---

## 7. 感知失真度量

### 7.1 三類方法

[▶ 50:27](https://youtu.be/LE6GLWv63wc?t=3027) MSE 是很差的失真度量（講者說課堂至少講了十次）。往**感知度量**走，大致三類 [▶ 51:03](https://youtu.be/LE6GLWv63wc?t=3063)：

| 類別 | 想法 | 代表 |
|---|---|---|
| 1. 模擬低階人眼特徵 | 把人眼特性寫成比 MSE 複雜一點的公式 | **SSIM**、MS-SSIM、VIF [▶ 51:36](https://youtu.be/LE6GLWv63wc?t=3096) |
| 2. 用大型學習模型 | 深度網路擷取的特徵和人很像 | **LPIPS** [▶ 52:16](https://youtu.be/LE6GLWv63wc?t=3136) |
| 3. 中間路線 | 手工特徵 + 用人的主觀評分學怎麼組合 | **VMAF**（Netflix 推廣）、DISTS [▶ 53:24](https://youtu.be/LE6GLWv63wc?t=3204) |

[▶ 51:36](https://youtu.be/LE6GLWv63wc?t=3096) 現在影像、影片壓縮的論文幾乎 100% 會報 SSIM；只報 MSE 很難說服別人 [▶ 52:16](https://youtu.be/LE6GLWv63wc?t=3136)。時間（講者記得的）：SSIM 約 2002、LPIPS 約 2018–2020、VMAF 約 2015–2016 [▶ 54:01](https://youtu.be/LE6GLWv63wc?t=3241)；全是本世紀的，很熱門。

### 7.2 SSIM

[▶ 54:36](https://youtu.be/LE6GLWv63wc?t=3276) **SSIM**（Structural Similarity）用三個特徵比較兩張圖 [▶ 55:07](https://youtu.be/LE6GLWv63wc?t=3307)：

1. **亮度**（luminance）：區塊平均 $\mu_x,\mu_y$ 的函數 [▶ 55:41](https://youtu.be/LE6GLWv63wc?t=3341)。
2. **對比**（contrast）：變異 $\sigma_x,\sigma_y$ 的函數 [▶ 56:16](https://youtu.be/LE6GLWv63wc?t=3376)。
3. **結構**（structure）：兩張圖的**共變異** $\sigma_{xy}$，邊緣、平坦區在不在同樣的地方 [▶ 56:16](https://youtu.be/LE6GLWv63wc?t=3376)。

三個分數用指數 $\alpha,\beta,\gamma$ 組合成 SSIM [▶ 56:50](https://youtu.be/LE6GLWv63wc?t=3410)。就是算兩張圖的一些二階統計量。那張「同 MSE 五張圖」就出自這篇論文 [▶ 55:41](https://youtu.be/LE6GLWv63wc?t=3341)。

**加權平均** [▶ 57:24](https://youtu.be/LE6GLWv63wc?t=3444)：$\mu$ 等不是單純平均，而是用**高斯核**加權，中心權重大。這是經驗法則，動機是 **foveation**：看一個區塊時會比較注意中心 [▶ 58:03](https://youtu.be/LE6GLWv63wc?t=3483)。實驗顯示 SSIM 和人的判斷相關性比 MSE 好很多 [▶ 58:49](https://youtu.be/LE6GLWv63wc?t=3529)。

> 以下**不是逐字稿內容**，是補上 SSIM 常見的完整式子（取 $\alpha=\beta=\gamma=1$；$C_1,C_2$ 是避免除以 0 的小常數）：
> $$\mathrm{SSIM}(x,y)=\frac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}{(\mu_x^2+\mu_y^2+C_1)(\sigma_x^2+\sigma_y^2+C_2)}.$$
> 兩張圖相同時為 1。

**MS-SSIM**（multi-scale）[▶ 58:49](https://youtu.be/LE6GLWv63wc?t=3529)：算一次 SSIM，兩張圖都降取樣，再算，再降取樣……最後組合起來。目的是看影像在**不同空間頻率**上的反應（人對不同空間頻率像是有獨立的通道）。比 SSIM 好不少，也很常用 [▶ 59:22](https://youtu.be/LE6GLWv63wc?t=3562)。

### 7.3 LPIPS

[▶ 59:57](https://youtu.be/LE6GLWv63wc?t=3597) **LPIPS**（Learned Perceptual Image Patch Similarity）。論文的一句話：「我們的結果顯示，**感知相似性是深度視覺表示共有的湧現性質**。」[▶ 1:00:31](https://youtu.be/LE6GLWv63wc?t=3631) 白話：學出來的特徵本身就和人看重的特徵相似。

做法：用深度網路的**嵌入**（embeddings，網路的輸出）當特徵空間，在嵌入上定義距離，當作壓縮器的新失真度量 [▶ 1:01:06](https://youtu.be/LE6GLWv63wc?t=3666)。

例 [▶ 1:01:06](https://youtu.be/LE6GLWv63wc?t=3666)：參考圖和兩張壓縮圖，人會選右邊；L2 選左邊；SSIM 也選左邊；三種網路的 LPIPS 都選右邊。所以網路學到的嵌入可能更像人 [▶ 1:01:46](https://youtu.be/LE6GLWv63wc?t=3706)。

### 7.4 VMAF

[▶ 1:02:21](https://youtu.be/LE6GLWv63wc?t=3741) 預先定義的空間特徵（VIF、DLM，可以想成 SSIM 的兄弟），再**用機器學習、蒐集大量人的偏好資料**，學怎麼把這幾個度量組合起來 [▶ 1:02:55](https://youtu.be/LE6GLWv63wc?t=3775)。訓練好的參數固定下來，就是另一個失真度量 [▶ 1:03:32](https://youtu.be/LE6GLWv63wc?t=3812)。

[▶ 1:03:32](https://youtu.be/LE6GLWv63wc?t=3812) 這個領域還很不成熟，貢獻的話影響很大。

---

## 8. 率–失真–感知取捨

### 8.1 草地的例子【課堂討論】

[▶ 1:04:08](https://youtu.be/LE6GLWv63wc?t=3848) 很新的工作（講者說約 2018–2019）：**率–失真–感知取捨**（rate–distortion–perception tradeoff, RDP）[▶ 1:04:41](https://youtu.be/LE6GLWv63wc?t=3881)。

[▶ 1:04:41](https://youtu.be/LE6GLWv63wc?t=3881) A：在 Stanford 拍的一張草地；B：JPEG 壓縮；C：**神經網路生成**的草，統計上像草，但不是同一片草（例如某根草在 A 有、在 C 沒有）[▶ 1:05:14](https://youtu.be/LE6GLWv63wc?t=3914)。

[▶ 1:05:50](https://youtu.be/LE6GLWv63wc?t=3950) 和 A 比，偏好 B 還是 C？學生答 C。講者也偏好 C：B 很模糊（雖然每根草的位置都對）；C 的 MSE 很高（草的排列是隨機的），但人不在乎草的位置 [▶ 1:06:24](https://youtu.be/LE6GLWv63wc?t=3984)。如果是人臉這樣扭曲就會抓狂；但**草地、地毯這類紋理**，只要統計上相似（**感知上看起來一樣**）就好 [▶ 1:06:24](https://youtu.be/LE6GLWv63wc?t=3984)。

### 8.2 公式

[▶ 1:07:06](https://youtu.be/LE6GLWv63wc?t=4026)（依口述重建）

- 率：$R$，$X$ 和 $\hat X$ 的函數。
- 失真：$\mathbb{E}\left[d(X,\hat X)\right]$。
- **感知**：原始和重建的**機率分布之間的距離** $d\left(p_X,p_{\hat X}\right)$，因為感知最終是對機率分布的某種統計量 [▶ 1:07:46](https://youtu.be/LE6GLWv63wc?t=4066)。

不只取捨兩個，而是三個一起調 [▶ 1:07:46](https://youtu.be/LE6GLWv63wc?t=4066)。

> 以下**不是逐字稿內容**，是把上面寫成式子（課堂沒寫出來）：
> $$R(D,P)=\min_{p_{\hat X\mid X}}I(X;\hat X)\quad\text{s.t.}\quad\mathbb{E}\,d(X,\hat X)\le D,\quad d\left(p_X,p_{\hat X}\right)\le P.$$

### 8.3 MNIST 例子

[▶ 1:07:46](https://youtu.be/LE6GLWv63wc?t=4066) MNIST 數字壓成 **2 位元**再解碼，固定率、改變失真和感知的取捨 [▶ 1:08:21](https://youtu.be/LE6GLWv63wc?t=4101)：

- 第一行：只最佳化率失真（不管感知）：**非常模糊** [▶ 1:08:52](https://youtu.be/LE6GLWv63wc?t=4132)。
- 往右越重視感知：越來越清晰，但**數字可能不對了**（就像草的位置不對）：例如 5 變成 7 [▶ 1:09:28](https://youtu.be/LE6GLWv63wc?t=4168)、[▶ 1:10:01](https://youtu.be/LE6GLWv63wc?t=4201)。

[▶ 1:09:28](https://youtu.be/LE6GLWv63wc?t=4168) 率很高時當然希望每樣都精確；**RDP 的好處在率受限時才顯現**：那時花不起位元讓 MSE 完美，與其接受模糊，不如接受一點扭曲（但別誇張到 5 變 7）[▶ 1:10:01](https://youtu.be/LE6GLWv63wc?t=4201)。

[▶ 1:10:34](https://youtu.be/LE6GLWv63wc?t=4234) 理論面：有論文證明在某些條件下，就算最佳化感知，**失真的誤差有界**（不會讓 5 變成 1）[▶ 1:11:20](https://youtu.be/LE6GLWv63wc?t=4280)。率失真研究了 50–60 年，RDP 才剛開始，喜歡理論的人可以看看。

### 8.4 實務上怎麼用

[▶ 1:11:20](https://youtu.be/LE6GLWv63wc?t=4280) 回到學習式壓縮：失真項只要可微就能換 [▶ 1:11:55](https://youtu.be/LE6GLWv63wc?t=4315)。

1. **用 SSIM 當失真**：SSIM 由平均、變異等組成，可微 [▶ 1:12:26](https://youtu.be/LE6GLWv63wc?t=4346)：
$$\mathcal L\approx L(\text{bits})+\lambda\,\mathrm{SSIM}(I,\hat I).$$
（投影片原樣；實際最佳化時應該用 $1-\mathrm{SSIM}$ 之類，因為 SSIM 越大越好。）
2. **加權的 MSE（或 MAE）加上感知損失**（例如 LPIPS）[▶ 1:13:01](https://youtu.be/LE6GLWv63wc?t=4381)：
$$\mathcal L\approx L(\text{bits})+\lambda_1\,\mathrm{MAE}(I,\hat I)+\lambda_2\,\mathrm{LPIPS}(I,\hat I).$$
幾乎所有學習式影像、影片壓縮器都用類似這樣的損失 [▶ 1:13:01](https://youtu.be/LE6GLWv63wc?t=4381)：失真項確保不會亂編，LPIPS 不在乎像素細節、看較高層的結構，追蹤 $p_X$ 和 $p_{\hat X}$ [▶ 1:13:33](https://youtu.be/LE6GLWv63wc?t=4413)、[▶ 1:14:11](https://youtu.be/LE6GLWv63wc?t=4451)。
3. **GAN** [▶ 1:14:11](https://youtu.be/LE6GLWv63wc?t=4451)：除了編碼器和生成器（解碼器），再訓練一個**判別器**判斷 $I$ 和 $\hat I$ 是否分得出來；原理上判別器就是感知損失，確保 $I$ 和 $\hat I$ 來自同一分布 [▶ 1:14:48](https://youtu.be/LE6GLWv63wc?t=4488)。

【投影片補充】**HiFiC**：用條件 GAN + LPIPS 的損失，約兩年前達到最先進 [▶ 1:16:35](https://youtu.be/LE6GLWv63wc?t=4595)。

[▶ 1:14:48](https://youtu.be/LE6GLWv63wc?t=4488) 最近生成模型突飛猛進（Stable Diffusion、LLM、CLIP、DALL·E），讓感知（$p_X$ 和 $p_{\hat X}$）更居於壓縮的中心 [▶ 1:15:20](https://youtu.be/LE6GLWv63wc?t=4520)。Shubham 在第 9 講用 LLM 做無損壓縮；現在也可以想怎麼用在**有損**上 [▶ 1:15:59](https://youtu.be/LE6GLWv63wc?t=4559)。LLM 似乎有世界的知識，怎麼讓它幫忙做到極低的位元率？這是非常熱門的方向。

---

## 9. 結語

[▶ 1:17:11](https://youtu.be/LE6GLWv63wc?t=4631) 工程之外，**神經科學和心理視覺**其實是設計這些系統的核心。今天詳談影像、稍微談音訊（44.1 kHz）。未來還有新的資料型態：VR、基因、各種感測器資料 [▶ 1:17:45](https://youtu.be/LE6GLWv63wc?t=4665)。

> 不只是人的感知：設計任何利基領域的有損壓縮器時，都要**了解資料是什麼、用在什麼應用**，不要只為 MSE 設計；利用其他面向，常常在特定應用上有巨大收益 [▶ 1:18:19](https://youtu.be/LE6GLWv63wc?t=4699)。

---

## 10. 一頁速查表

### 人的感官 → 壓縮設計

| 人的特性 | 壓縮上的利用 |
|---|---|
| 兩隻耳朵、聽 20 Hz–20 kHz | 雙聲道、44.1 kHz（Nyquist + 餘裕 + 好降取樣） |
| 眼睛光學 = 低通濾波 | 高頻可以丟 |
| 桿細胞：亮度、$10^9$ 動態範圍 | — |
| 錐細胞只在中央窩；掃視 | foveation：追蹤眼球、注視點多給位元（VR） |
| Weber 定律：只在乎相對變化 | 低亮度區要小心位元分配 |
| 三種錐細胞（L、M、S） | RGB |
| 對立歷程（白黑、藍黃、紅綠） | YCbCr |
| 色度對比敏感度下降快 | 色度降取樣（4:2:0）、色度用不同量化表 |
| 高頻對比敏感度低 | 高頻 DCT 量化狠 |

### 色彩

- 色彩空間（sRGB、Adobe RGB…）不同 ⇒ 同一組數值顯示不同 ⇒ 失真不同；轉換矩陣（BT.601 vs. BT.709）要對。
- 4:2:0：色度 2×2 平均；文字截圖會變色。

### 感知度量

| 度量 | 做法 |
|---|---|
| SSIM | 亮度 $\mu$、對比 $\sigma$、結構 $\sigma_{xy}$，高斯加權（foveation） |
| MS-SSIM | 多尺度 SSIM（不同空間頻率） |
| LPIPS | 深度網路嵌入的距離 |
| VMAF | 手工特徵 + 人的評分學組合 |

### RDP

- 感知 = $d(p_X,p_{\hat X})$；低率時寧可統計上像（紋理）也不要模糊。
- 實務損失：率 + $\lambda_1$ MAE + $\lambda_2$ LPIPS，或 GAN 判別器（HiFiC）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 掃視、人看的是「影片」 | 第 18 集影片壓縮 |
| VMAF、編碼表、感知品質 | 第 18 集串流 |
| 4:2:0 是影片預設 | 第 18 集 |

> 以上對應是依播放清單標題推估的，做到時再更新。

---

## 附：本集一句話總結

> **多媒體最終給人看、聽，所以很多壓縮設計來自人的感官：雙聲道、44.1 kHz；眼睛光學本身就低通；錐細胞只在中央窩（可以依注視點分配位元）；Weber 定律；三種錐細胞對應 RGB，對立歷程說對應 YCbCr，色度的對比敏感度低所以可以 4:2:0 降取樣。MSE 不符合人眼，所以有 SSIM（亮度、對比、結構）、LPIPS（深度特徵距離）、VMAF（學出來的組合）；更進一步的率–失真–感知取捨讓低率時重建「統計上像」而不是「模糊地對」，實務上用 MAE + LPIPS 或 GAN 的損失來訓練學習式壓縮器。**

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 17 錄影逐字稿（人工字幕，1:18:39）與投影片 slide_17_2023 整理。*
