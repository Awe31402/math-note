---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 11
lecture: Lecture 11
date: 2023-11-01
video: https://youtu.be/YEF0iCiQlOg
notes: 投影片 slide_11_2023.pdf、slide_11_2023_ann.pdf；《Elements of Information Theory》§10.1（書頁 301–303）
---

# 第 11 集 · Lecture 11：有損壓縮基礎、量化（Lossy Compression Basics; Quantization） [▶ 影片](https://youtu.be/YEF0iCiQlOg)

← 上一集：[10-lz-universal-compression](10-lz-universal-compression.md) ｜ [總目錄](README.md) ｜ 下一集：[12-mutual-information-rate-distortion](12-mutual-information-rate-distortion.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 11 集
> **講者**：Pulkit Tandon
> **來源**：YouTube 錄影逐字稿（1:24:27，人工字幕 en-US）＋ 投影片 `slide_11_2023.pdf`、`slide_11_2023_ann.pdf` ＋ Cover & Thomas §10.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 小考檢討：LZ77、zstd vs. LLM](#1-小考檢討lz77zstd-vs-llm)
- [2. 從無損到有損](#2-從無損到有損)
- [3. 連續來源有多少資訊？](#3-連續來源有多少資訊)
- [4. 失真與率失真取捨](#4-失真與率失真取捨)
- [5. 例子：溫度感測器](#5-例子溫度感測器)
- [6. 量化](#6-量化)
- [7. 例子：1 位元量化高斯來源](#7-例子1-位元量化高斯來源)
- [8. 純量量化](#8-純量量化)
- [9. 向量量化](#9-向量量化)
- [10. 向量量化的好處與代價](#10-向量量化的好處與代價)
- [11. Lloyd 演算法 = k-means](#11-lloyd-演算法--k-means)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/YEF0iCiQlOg?t=5) 進入課程後半：**有損壓縮**（lossy compression）。

| 主題 | 課本 |
|---|---|
| 連續來源、失真、率失真取捨 | §10.1–10.2 |
| 量化：純量量化 | §10.1 |
| 向量量化、Lloyd 演算法（k-means） | §10.1 |

---

## 1. 小考檢討：LZ77、zstd vs. LLM

### 1.1 LZ77 反解析

[▶ 00:05](https://youtu.be/YEF0iCiQlOg?t=5) 第 1 題（上一講的表）：偏移 1、長度 4 → 輸出四個 B；偏移 9、長度 5 → 回到字串開頭抄 `AABBB`；偏移 2、長度 2 → 再抄 `CD` [▶ 00:38](https://youtu.be/YEF0iCiQlOg?t=38)。得到 `AABBBBBBBAABBBCDCDCD`。

[▶ 01:15](https://youtu.be/YEF0iCiQlOg?t=75) Ed 上有人問：用上課教的解析器解析這個字串，不會得到這張表。講者：LZ77 的解析方式**不唯一**（貪婪、懶惰、動態規劃），但不管用哪種解析，有了這張表都能還原原字串 [▶ 01:57](https://youtu.be/YEF0iCiQlOg?t=117)。題目也特別說明了這是不同的解析器 [▶ 02:31](https://youtu.be/YEF0iCiQlOg?t=151)。

### 1.2 LZ77 解析

[▶ 02:31](https://youtu.be/YEF0iCiQlOg?t=151) 第 2 題輸入 `TATWAWADI`（Kedar 的姓），用上課的解析器 [▶ 03:15](https://youtu.be/YEF0iCiQlOg?t=195)：

| 未匹配字面值 | 長度 | 偏移 |
|---|---|---|
| `TA` | 1 | 2 |
| `W` | 1 | 3 |
| — | 2 | 2 |
| `DI` | — | — |

T 重複（2 個前）；W 沒看過，接著 A 在 3 個前看過；然後 `WA` 在 2 個前出現過；最後 `DI` 沒有匹配 [▶ 03:52](https://youtu.be/YEF0iCiQlOg?t=232)。

### 1.3 字母平移後的英文

[▶ 04:34](https://youtu.be/YEF0iCiQlOg?t=274) 第 3 題：把英文的每個字母平移（A→B、B→C……）。

| 敘述 | 答案 |
|---|---|
| zstd 在原文和平移後表現差不多 | **對** [▶ 05:07](https://youtu.be/YEF0iCiQlOg?t=307)：zstd 不在乎確切的機率分布，只找匹配，匹配不變，只有字面值變了 |
| 用英文訓練的 LLM 壓縮器表現差不多 | **錯** [▶ 05:43](https://youtu.be/YEF0iCiQlOg?t=343)：LLM 預測器只和它的機率模型一樣好，平移後模型完全錯了 |

[▶ 05:43](https://youtu.be/YEF0iCiQlOg?t=343) 這就是 LZ 類方法和算術編碼／rANS（需要機率正確匹配）在概念上的差別。

### 1.4 第一步是什麼

[▶ 06:23](https://youtu.be/YEF0iCiQlOg?t=383) 第 4 題：遇到壓縮問題，**永遠先試標準壓縮器（例如 zstd）**，再去做其他學過的東西。【口頭】聽起來像玩笑，但在業界或自己做壓縮器時，這才是重要的事。

---

## 2. 從無損到有損

[▶ 06:58](https://youtu.be/YEF0iCiQlOg?t=418) 回顧前半：無損壓縮的根本極限是**熵**；經驗法則 $l(x)\approx\lceil\log_2\frac1{p(x)}\rceil$ [▶ 07:35](https://youtu.be/YEF0iCiQlOg?t=455)；各種熵編碼器（Shannon、Huffman 分組碼；算術、ANS 串流碼；LZ77 通用碼）；非 iid：context-based、自適應 [▶ 08:16](https://youtu.be/YEF0iCiQlOg?t=496)。

[▶ 08:55](https://youtu.be/YEF0iCiQlOg?t=535) **前半學到的全部在後半仍然適用**：

- **無損壓縮是有損壓縮的特例**（損失 = 0）。
- 更實際地說：**任何實用的有損壓縮器都包含無損壓縮的部分** [▶ 09:28](https://youtu.be/YEF0iCiQlOg?t=568)：先做有損的那一步，最後還是要把一些符號無損地壓起來。

[▶ 09:28](https://youtu.be/YEF0iCiQlOg?t=568) 另一個重點：無損壓縮都假設**離散來源**（有限字母集）。但實際上什麼都不是離散的：影像、感測器、影片在現實中都是**連續的** [▶ 10:09](https://youtu.be/YEF0iCiQlOg?t=609)。後半學期要處理連續值。

---

## 3. 連續來源有多少資訊？

【課堂討論】[▶ 10:49](https://youtu.be/YEF0iCiQlOg?t=649) 一個連續來源有多少資訊？

學生答：看機器的浮點精度 [▶ 11:25](https://youtu.be/YEF0iCiQlOg?t=685)。講者：那時你已經假設了某種**離散化**，丟掉了一些資訊；誰說 64 位元是儲存一切的根本精度？那和任何數字一樣任意 [▶ 11:25](https://youtu.be/YEF0iCiQlOg?t=685)。

> **答案：無限多。** [▶ 12:00](https://youtu.be/YEF0iCiQlOg?t=720) 兩個實數之間還有無限多個實數。不管用多高的精度（明天就算有百萬位元的電腦），只要不是無限，就丟了資訊；極限最後在物理擷取那一端 [▶ 12:37](https://youtu.be/YEF0iCiQlOg?t=757)。

[▶ 13:08](https://youtu.be/YEF0iCiQlOg?t=788) 所以連續來源**不可能精確表示**，一定要**近似**，而任何近似都代表資訊損失。有損壓縮是很自然、不得不做的事。

---

## 4. 失真與率失真取捨

### 4.1 失真

[▶ 13:08](https://youtu.be/YEF0iCiQlOg?t=788) 有損壓縮的文獻引入一個參數：**失真**（distortion），衡量資訊損失。

| 失真 | 式子 |
|---|---|
| 均方誤差（MSE） | $D=\mathbb{E}\left[(X-\hat X)^2\right]$ |
| 平均絕對誤差（MAE） | $D=\mathbb{E}\left[|X-\hat X|\right]$ [▶ 13:52](https://youtu.be/YEF0iCiQlOg?t=832) |

$X$ 是來源符號，$\hat X$ 是用來表示它的值。任何距離函數都可以當失真；**要用哪個看應用** [▶ 13:52](https://youtu.be/YEF0iCiQlOg?t=832)。

[▶ 14:31](https://youtu.be/YEF0iCiQlOg?t=871) 後半學期講影像、影片、一點音訊時會看到：很多研究發現，這些數學上很好處理的失真其實是**錯的**，和人類的感知不相關：失真高不一定代表資訊損失大。所以選失真很重要，影響了很多多媒體壓縮器的設計；之後有一講專講**感知壓縮** [▶ 15:13](https://youtu.be/YEF0iCiQlOg?t=913)。

### 4.2 率

[▶ 15:50](https://youtu.be/YEF0iCiQlOg?t=950) 決定能容忍多少失真後，要**最小化表示來源的位元數**，這就是**率**（rate，$R$）。直覺上：**率越高，失真越低**，因為能花更多位元表示來源 [▶ 16:27](https://youtu.be/YEF0iCiQlOg?t=987)。

### 4.3 率失真曲線

[▶ 16:27](https://youtu.be/YEF0iCiQlOg?t=987) 這就是有損壓縮最根本的**率失真取捨**（rate–distortion tradeoff）。第 1 集看過影像、音訊的例子 [▶ 17:07](https://youtu.be/YEF0iCiQlOg?t=1027)。

[▶ 17:07](https://youtu.be/YEF0iCiQlOg?t=1027) 橫軸是率 $R$、縱軸是失真 $D$：率增加、失真下降。講者特別畫成凸向原點的形狀而不是其他樣子，因為率失真有很深的理論性質，Tsachy 下一講會講 [▶ 17:43](https://youtu.be/YEF0iCiQlOg?t=1063)。

### 4.4 兩種看法

[▶ 18:26](https://youtu.be/YEF0iCiQlOg?t=1106) 講者說實務上這兩種觀點非常有用：

1. **給定失真 $D$，最小化率** [▶ 18:58](https://youtu.be/YEF0iCiQlOg?t=1138)：例如應用上不能容忍超過某失真，否則沒人看你的串流。在所有達到這個失真的方法裡，找位元最少的。
2. **給定率 $R$，最小化失真** [▶ 19:33](https://youtu.be/YEF0iCiQlOg?t=1173)：例如客戶的頻寬就是不夠看 4K，你只有這麼多位元可用，在所有方法裡找失真最小的。

[▶ 20:14](https://youtu.be/YEF0iCiQlOg?t=1214) 兩者都是在找 **Pareto 最佳的率失真曲線**。

---

## 5. 例子：溫度感測器

[▶ 20:50](https://youtu.be/YEF0iCiQlOg?t=1250) 每小時量一次房間溫度（攝氏）。實際溫度是連續的，要無限位元；感測器本身記錄時就已經是有損的了 [▶ 21:25](https://youtu.be/YEF0iCiQlOg?t=1285)。假設這個感測器很靈敏，給到小數點後 6 位：38.xxxxxx、36.xxxxxx……

【課堂討論】[▶ 22:03](https://youtu.be/YEF0iCiQlOg?t=1323) 要分配多少位元？

學生答：看房間，如果溫度只會在 0 到 100 之間就比較容易 [▶ 22:40](https://youtu.be/YEF0iCiQlOg?t=1360)。講者：對，這不完全是陷阱題，但實務上設計有損壓縮器，**很多時間就花在這個問題：看應用** [▶ 23:15](https://youtu.be/YEF0iCiQlOg?t=1395)：

- 用來控制冷氣的恆溫器，也許要多幾位小數。
- FitBit 上用來決定要不要帶連帽外套，完全是另一回事。
- 工業上的精密量測又不一樣 [▶ 23:57](https://youtu.be/YEF0iCiQlOg?t=1437)。

> **先決定能接受的失真。** 小數點後 6 位的溫度，幾乎對任何應用都是浪費（除非做材料科學）[▶ 23:57](https://youtu.be/YEF0iCiQlOg?t=1437)。

【課堂討論】[▶ 24:44](https://youtu.be/YEF0iCiQlOg?t=1484) 那合理的值是？學生答：把小數全部去掉，38.1 和 37.9 沒差 [▶ 25:15](https://youtu.be/YEF0iCiQlOg?t=1515)。講者：例如存 38、36、37、37、35 [▶ 25:48](https://youtu.be/YEF0iCiQlOg?t=1548)。

> **四捨五入就已經引入了損失**，這是最基本的有損壓縮技術 [▶ 26:21](https://youtu.be/YEF0iCiQlOg?t=1581)。

[▶ 26:21](https://youtu.be/YEF0iCiQlOg?t=1581) 類似**轉換資料型態**：把 float 轉 int。有人用 float64 存一個人的收入？很浪費，先轉 float32（或整數，不過大家在乎「分」）。只要這樣做就引入了失真，也是有損壓縮，之後表示它所需的位元就少很多 [▶ 26:54](https://youtu.be/YEF0iCiQlOg?t=1614)。

---

## 6. 量化

### 6.1 定義

[▶ 27:31](https://youtu.be/YEF0iCiQlOg?t=1651) 剛剛的四捨五入，正式的名字叫**量化**（quantization）。講者引用 Stanford 的 Gray 教授（量化專家）的簡單定義：

> **量化是把連續來源對應到離散來源的過程。** [▶ 28:09](https://youtu.be/YEF0iCiQlOg?t=1689)

- 量化是有損的，會引入失真。
- 它是有損壓縮的**基本運算**：講者說他想不出世上有哪個有損壓縮器不在某處做某種量化 [▶ 28:41](https://youtu.be/YEF0iCiQlOg?t=1721)。

**術語** [▶ 28:41](https://youtu.be/YEF0iCiQlOg?t=1721)：

- 量化後的值叫**符號**（symbol）或**碼字**（codeword）。
- 所有可用量化值的集合叫**碼本**（codebook）或**字典**（dictionary）。

例 [▶ 29:14](https://youtu.be/YEF0iCiQlOg?t=1754)：38、36、37、37、35，只有四個不同值，碼本 $=\{35,36,37,38\}$。

[▶ 29:48](https://youtu.be/YEF0iCiQlOg?t=1788) 另一種看法：給定碼本，每個值對應到碼本裡**最近**的元素。

### 6.2 碼本大小 $N$ 時的率【課堂討論】

[▶ 30:23](https://youtu.be/YEF0iCiQlOg?t=1823) 碼本大小 $N$，率是多少？[▶ 30:58](https://youtu.be/YEF0iCiQlOg?t=1858) 提示：碼字是離散的；4 個碼字均勻分布，要幾位元？學生答：**2**，就是碼本大小的 $\log_2$ [▶ 31:29](https://youtu.be/YEF0iCiQlOg?t=1889)。

[▶ 31:29](https://youtu.be/YEF0iCiQlOg?t=1889) 只要送**索引**：收到索引 $i$，解碼器重建碼字 $i$ [▶ 32:12](https://youtu.be/YEF0iCiQlOg?t=1932)。所以

$$R=\left\lceil\log_2N\right\rceil\ \text{位元／符號};\qquad\text{反過來，}R\text{ 位元可以用 }2^R\text{ 個不同的值}.$$

[▶ 32:52](https://youtu.be/YEF0iCiQlOg?t=1972) 這和第 5 講 AEP 的原理一樣：數索引、編索引。

### 6.3 碼本大小和率失真

[▶ 33:30](https://youtu.be/YEF0iCiQlOg?t=2010)

- 率高 → 碼本大 → 選擇多 → **失真低**。
- 能接受較高失真 → 縮小碼本 → **率低** [▶ 34:04](https://youtu.be/YEF0iCiQlOg?t=2044)。

---

## 7. 例子：1 位元量化高斯來源

### 7.1 要送什麼【課堂討論】

[▶ 34:46](https://youtu.be/YEF0iCiQlOg?t=2086) 談到連續來源，第一個想到的模型應該是**高斯隨機變數**。$X\sim\mathcal N(0,1)$。朋友說只能送 **1 位元／符號** [▶ 35:29](https://youtu.be/YEF0iCiQlOg?t=2129)。

合理的值是什麼？學生答：**正負號** [▶ 36:00](https://youtu.be/YEF0iCiQlOg?t=2160)。高斯分布對 0 對稱，只有兩種選擇時送正負號很直覺 [▶ 36:32](https://youtu.be/YEF0iCiQlOg?t=2192)。（要知道是不是最好，得先說失真是什麼；但合理的失真應該也對 0 對稱。）

### 7.2 收到「正」時要重建成什麼？

[▶ 37:48](https://youtu.be/YEF0iCiQlOg?t=2268) 對方收到正號，該用什麼值表示這個符號（量化後的值）？[▶ 38:20](https://youtu.be/YEF0iCiQlOg?t=2300) **要先決定失真**；不同失真，最好的重建值不同。

【課堂討論】[▶ 38:55](https://youtu.be/YEF0iCiQlOg?t=2335) 取 MSE。學生猜變異數 [▶ 38:55](https://youtu.be/YEF0iCiQlOg?t=2335)。講者：不對。答案是

$$\hat x=\mathbb{E}\left[X\mid\hat X>0\right].$$

這是很有名的結果：**最小均方誤差估計**（minimum mean square error estimator, MMSE）[▶ 39:32](https://youtu.be/YEF0iCiQlOg?t=2372)。上過訊號處理的人應該知道；不知道的話，本課可以先相信它 [▶ 40:07](https://youtu.be/YEF0iCiQlOg?t=2407)。

> 以下**不是逐字稿內容**，是補上 MMSE 的一行證明：要最小化 $\mathbb{E}[(X-c)^2\mid A]$，展開成 $\mathbb{E}[X^2\mid A]-2c\,\mathbb{E}[X\mid A]+c^2$，對 $c$ 微分令其為 0 得 $c=\mathbb{E}[X\mid A]$。二次項係數為正，所以是最小值。

[▶ 40:51](https://youtu.be/YEF0iCiQlOg?t=2451) 重點：這個碼本是**針對 MSE 的**。若換一個奇怪的失真（例如非線性的、神經網路算的），就不一定成立 [▶ 41:45](https://youtu.be/YEF0iCiQlOg?t=2505)。

> **沒有「最佳碼本」這種東西，除非知道要最佳化的失真。** 有人跟你談有損壓縮，先問失真是什麼 [▶ 41:45](https://youtu.be/YEF0iCiQlOg?t=2505)。

### 7.3 算出來

[▶ 42:23](https://youtu.be/YEF0iCiQlOg?t=2543) $X\sim\mathcal N(0,1)$，密度 $f_X(x)=\frac1{\sqrt{2\pi}}e^{-x^2/2}$。

$$\mathbb{E}\left[X\mid\hat X>0\right]=\int_{-\infty}^{\infty}x\,f_{X\mid\hat X>0}(x)\,dx.$$

[▶ 43:15](https://youtu.be/YEF0iCiQlOg?t=2595) 用 Bayes 規則：分布對 0 對稱，$P(X>0)=\frac12$，所以條件密度是 $x>0$ 時 $2f_X(x)$、否則 0（**半高斯**）[▶ 43:52](https://youtu.be/YEF0iCiQlOg?t=2632)：

$$\mathbb{E}\left[X\mid X>0\right]=\int_0^\infty x\cdot\frac{2}{\sqrt{2\pi}}e^{-x^2/2}\,dx=\sqrt{\frac2\pi}\int_0^\infty x\,e^{-x^2/2}\,dx.$$

[▶ 43:52](https://youtu.be/YEF0iCiQlOg?t=2632) 代換 $u=x^2/2$（$du=x\,dx$）：$\int_0^\infty e^{-u}du=1$。所以 [▶ 44:34](https://youtu.be/YEF0iCiQlOg?t=2674)

$$\mathbb{E}\left[X\mid X>0\right]=\sqrt{\frac2\pi}\approx0.798,\qquad\mathbb{E}\left[X\mid X<0\right]=-\sqrt{\frac2\pi}.$$

【投影片補充】`slide_11_2023.pdf` Quiz-6：碼本 $C=\left\{\mathbb{E}[X\mid\hat X>0],\ \mathbb{E}[X\mid\hat X<0]\right\}$。

> 以下**不是逐字稿內容**，是算這個量化器的失真：$\mathbb{E}\left[(X-\hat X)^2\right]=\mathbb{E}[X^2]-2\,\mathbb{E}[|X|]\sqrt{2/\pi}+\frac2\pi=1-\frac2\pi\approx0.363$（用 $\mathbb{E}|X|=\sqrt{2/\pi}$）。作為對照，第 13 集會講高斯的率失真函數，1 位元時理論最小失真是 $2^{-2}=0.25$。

【課本補充】§10.1（書頁 301–302）正是這個例子：1 位元表示 $\mathcal N(0,\sigma^2)$ 時重建點取 $\pm\sqrt{2/\pi}\,\sigma$，失真 $\frac{\pi-2}{\pi}\sigma^2\approx0.3634\sigma^2$。

### 7.4 整個通訊流程

[▶ 46:32](https://youtu.be/YEF0iCiQlOg?t=2792)

```
連續來源 X ──(決定 1 位元/符號)──> 只編正負號（離散）──> 傳碼本索引
   解碼端：收到索引 ──> 知道正負號 ──> 依共享的碼本重建 ±√(2/π)
```

[▶ 47:09](https://youtu.be/YEF0iCiQlOg?t=2829) 「編碼離散分布」這一步，就是前半學的無損壓縮派上用場的地方（現在還沒用到，但看得出來）。碼本要共享，或解碼端能自己算出來 [▶ 47:48](https://youtu.be/YEF0iCiQlOg?t=2868)。

---

## 8. 純量量化

[▶ 48:22](https://youtu.be/YEF0iCiQlOg?t=2902) 畫出 $\mathcal N(0,1)$ 的直方圖。整個做法其實做了兩件事 [▶ 48:55](https://youtu.be/YEF0iCiQlOg?t=2935)：

1. **決策邊界**（decision boundary）：1 位元時是 $x>0$、$x<0$，門檻是 0。
2. 每個區域**對應到碼本裡的一個值** [▶ 49:32](https://youtu.be/YEF0iCiQlOg?t=2972)：例如樣本是 2.xx，就對到 $\sqrt{2/\pi}$。

> **純量量化**（scalar quantization）[▶ 50:14](https://youtu.be/YEF0iCiQlOg?t=3014)：每次只看一個符號。量化器是一個函數 $Q:x\mapsto\hat x$（畫成階梯狀的 xy 圖），由兩樣東西決定 [▶ 50:47](https://youtu.be/YEF0iCiQlOg?t=3047)：
> - **決策門檻**（decision thresholds）：哪些區域對到同一個值；
> - 對應的**量化值**。

[▶ 51:20](https://youtu.be/YEF0iCiQlOg?t=3080) 一般地，給定位元率就知道碼本有幾個量化值，再選門檻。[▶ 51:56](https://youtu.be/YEF0iCiQlOg?t=3116) **決策區域不必等寬**，可以依失真函數決定。

---

## 9. 向量量化

### 9.1 想法【課堂討論】

[▶ 53:02](https://youtu.be/YEF0iCiQlOg?t=3182) 還能怎麼改進？回想無損壓縮做過什麼。

- 一位學生：依前一個符號調整決策門檻 [▶ 53:38](https://youtu.be/YEF0iCiQlOg?t=3218)。講者：很好的想法，大家確實這樣做，但更進一步；今天不講，講義有參考，影像編碼（如 BPG）時會看到例子 [▶ 54:13](https://youtu.be/YEF0iCiQlOg?t=3253)。
- 回想第 1、2 講：不在乎複雜度時，什麼總是讓壓縮更好？學生答：**把區塊合起來** [▶ 54:55](https://youtu.be/YEF0iCiQlOg?t=3295)。

> **向量量化**（vector quantization, VQ）[▶ 54:55](https://youtu.be/YEF0iCiQlOg?t=3295)：一次量化兩個、三個……$k$ 個符號。

[▶ 55:34](https://youtu.be/YEF0iCiQlOg?t=3334) 向量可以是：同一感測器每兩個值一組（像分組碼）；兩個感測器量同一個來源；甚至兩個感測器量兩個不同房間 [▶ 56:12](https://youtu.be/YEF0iCiQlOg?t=3372)。任何兩個值湊成二元組都是向量。

### 9.2 碼本大小【課堂討論】

[▶ 57:28](https://youtu.be/YEF0iCiQlOg?t=3448) 區塊大小 2，要和 1 位元／符號的純量量化比。碼本可以多大？學生答 **4**：2 個符號共 2 位元 [▶ 58:43](https://youtu.be/YEF0iCiQlOg?t=3523)。

$$N=2^{R\cdot k}\quad\left(k\text{ 為向量長度，}R\text{ 位元／符號}\right),\qquad R=\frac{\log_2N}{k}\ \text{位元／符號}.$$

### 9.3 二維高斯：四個碼字怎麼放【課堂討論】

[▶ 1:00:40](https://youtu.be/YEF0iCiQlOg?t=3640) $(X_1,X_2)$ 都是 $\mathcal N(0,1)$ 獨立，二維密度對原點球對稱。1 位元／符號 → 4 個碼字。先不管最佳性，你會怎麼做？

1. 學生答：**分成四個象限** [▶ 1:02:22](https://youtu.be/YEF0iCiQlOg?t=3742)。決策邊界是兩條軸；因為球對稱（取 MSE），量化值在某個圓上，每個象限一個 [▶ 1:02:22](https://youtu.be/YEF0iCiQlOg?t=3742)。
2. 朋友說：我想要量化值在**軸上** [▶ 1:03:16](https://youtu.be/YEF0iCiQlOg?t=3796)。那決策區域是兩條軸之間的角平分線（學生看出來了）[▶ 1:03:52](https://youtu.be/YEF0iCiQlOg?t=3832)。

【課堂討論】[▶ 1:04:31](https://youtu.be/YEF0iCiQlOg?t=3871) 用 MSE 的話哪個比較好？學生答：**一樣**，可以旋轉 [▶ 1:05:05](https://youtu.be/YEF0iCiQlOg?t=3905)。講者：對，分布是球對稱的，用任何正交基底都一樣。碼向量在你的座標系裡看起來多複雜都沒關係，因為只送索引 [▶ 1:05:05](https://youtu.be/YEF0iCiQlOg?t=3905)。

3. 講者「很貪心」[▶ 1:05:46](https://youtu.be/YEF0iCiQlOg?t=3946)：把一個碼字放在**原點**，另外三個在某個圓上。決策區域由兩兩之間的分隔超平面決定 [▶ 1:06:20](https://youtu.be/YEF0iCiQlOg?t=3980)。[▶ 1:06:55](https://youtu.be/YEF0iCiQlOg?t=4015) 可以證明這**不是最佳的**；等一下的 notebook 會看到前兩種比較好。

### 9.4 正式定義

[▶ 1:07:34](https://youtu.be/YEF0iCiQlOg?t=4054)

> **向量量化器**：映射 $Q:\mathbb{R}^k\to\mathcal C$，碼本 $\mathcal C=\{y_i\}_{i=1}^N$ 是 $N$ 個 $k$ 維向量。$\{S_i\}_{i=1}^N$ 是 $\mathbb{R}^k$ 的一個**分割**，$Q(x)=y_i$ 若 $x\in S_i$。率 $R=\frac{\log_2N}{k}$ 位元／樣本。

[▶ 1:08:13](https://youtu.be/YEF0iCiQlOg?t=4093) 分割必須蓋滿整個空間，否則有向量不知道該對到哪。

---

## 10. 向量量化的好處與代價

### 10.1 好處一：利用分量之間的相依

[▶ 1:08:48](https://youtu.be/YEF0iCiQlOg?t=4128) 例：$(X_1,X_2)$ 的分布只在第一、三象限（$X_1$、$X_2$ 永遠同號）[▶ 1:09:20](https://youtu.be/YEF0iCiQlOg?t=4160)。

- **均勻純量量化**：$x$ 方向切一組格、$y$ 方向切一組格，6 × 6 = 36 個方塊，每個向量（2 個符號）$\log_2 36$ 位元，每符號 $\frac{\log_236}2=\log_26\approx2.58$ [▶ 1:09:20](https://youtu.be/YEF0iCiQlOg?t=4160)。
- **向量量化** [▶ 1:09:59](https://youtu.be/YEF0iCiQlOg?t=4199)：知道兩者總是同號，只需要和密度重疊的 18 個方塊：每符號 $\frac{\log_218}2\approx2.08$。

[▶ 1:10:33](https://youtu.be/YEF0iCiQlOg?t=4233) **同樣失真（決策區域一模一樣）省了半位元**。

### 10.2 好處二：更一般的決策區域

[▶ 1:11:09](https://youtu.be/YEF0iCiQlOg?t=4269) 更強的是（不證明，講義有）：

- **即使是最簡單的均勻 iid 情況，最佳區域一般也不是方格**（不是純量量化那種）[▶ 1:11:09](https://youtu.be/YEF0iCiQlOg?t=4269)。
- 二維均勻 iid：**六角形格子**最好 [▶ 1:11:48](https://youtu.be/YEF0iCiQlOg?t=4308)。量化點每一列錯開半格，像蜂巢，每個點的區域是六角形 [▶ 1:12:23](https://youtu.be/YEF0iCiQlOg?t=4343)。同樣的率，MSE 低約 4% [▶ 1:12:58](https://youtu.be/YEF0iCiQlOg?t=4378)。

【投影片補充】`slide_11_2023.pdf`：$\frac{\text{MSE}_{\text{lattice}}}{\text{MSE}_{\text{SQ}}}\approx0.962$（二維）。這叫**格點量化**（lattice quantization）或 **Voronoi 圖**，可推廣到更高維 [▶ 1:12:58](https://youtu.be/YEF0iCiQlOg?t=4378)。

### 10.3 代價

[▶ 1:13:35](https://youtu.be/YEF0iCiQlOg?t=4415) 純量均勻量化什麼都不用想（32 位元浮點數就是一種）；VQ 要找出向量、格子怎麼設計，才拿到那 4% [▶ 1:14:08](https://youtu.be/YEF0iCiQlOg?t=4448)。

- Ziv（就是 Lempel–Ziv 的 Ziv）在〈On universal quantization〉證明：某些情況下，純量量化器比任何向量量化器多不到 **0.754 位元／樣本** [▶ 1:14:08](https://youtu.be/YEF0iCiQlOg?t=4448)。
- 最佳區域一般不容易算，而且帶來的好處可能很小 [▶ 1:14:47](https://youtu.be/YEF0iCiQlOg?t=4487)。

> **向量量化可能很辛苦卻收穫不多，要小心複雜度和收益的取捨。** 就像分組碼：很棒、理論保證好，但複雜度指數成長，所以實務上相對少見 [▶ 1:14:47](https://youtu.be/YEF0iCiQlOg?t=4487)。

---

## 11. Lloyd 演算法 = k-means

### 11.1 量化值和決策區域互相依賴

[▶ 1:15:24](https://youtu.be/YEF0iCiQlOg?t=4524) 量化值取決於決策區域（例如取區域內的條件期望值），決策區域又取決於附近的量化值（最近的那個）。很難直接算，實務上用**迭代演算法** [▶ 1:16:05](https://youtu.be/YEF0iCiQlOg?t=4565)。

【課堂討論】[▶ 1:16:05](https://youtu.be/YEF0iCiQlOg?t=4565) 以前在哪看過這個問題？學生答：**分群**（clustering）[▶ 1:16:45](https://youtu.be/YEF0iCiQlOg?t=4605)。

### 11.2 Lloyd 演算法

[▶ 1:16:45](https://youtu.be/YEF0iCiQlOg?t=4605) 機器學習的 **k-means** 就是它；從壓縮、訊號處理、量化的角度叫 **Lloyd–Max 演算法**或**廣義 Lloyd 演算法**（Generalized Lloyd）[▶ 1:17:26](https://youtu.be/YEF0iCiQlOg?t=4646)。k-means 是廣義 Lloyd 在**平方誤差**下的特例。

【投影片補充】`slide_11_2023.pdf`：Stuart Lloyd 1957 年在 Bell Labs 提出（動機是音訊壓縮），廣為流傳但 1982 年才正式發表 [▶ 1:18:02](https://youtu.be/YEF0iCiQlOg?t=4682)。

[▶ 1:18:02](https://youtu.be/YEF0iCiQlOg?t=4682) 目標：把資料點分成 $N$ 群（碼本大小 $N$ = k-means 的 $k$），選點使平均失真最小。給定 $N$（也就是率），要找最佳的決策區域和量化值 [▶ 1:18:36](https://youtu.be/YEF0iCiQlOg?t=4716)。

迭代兩步：

1. **給定碼本，算最佳分割**：每個點分到最近的中心。
2. **給定分割，算最佳碼本**：每群的新中心（MSE 時就是群內平均）。
3. 重複直到收斂 [▶ 1:19:17](https://youtu.be/YEF0iCiQlOg?t=4757)。

```
centroids = 隨機初始化(data, N)        # 碼本
重複：
    clusters = 每個點分到最近的 centroid   # 分割
    new_centroids = 每群的平均             # 更新碼本
    若 new_centroids ≈ centroids：停
    centroids = new_centroids
```

[▶ 1:19:50](https://youtu.be/YEF0iCiQlOg?t=4790) **注意符號**：k-means 的 $k$ 是群數，本講叫 $N$；本講的 $k$ 是向量長度。

### 11.3 Notebook 示範

[▶ 1:19:50](https://youtu.be/YEF0iCiQlOg?t=4790)

- **二維高斯、$N=4$**（1 位元／符號）[▶ 1:20:23](https://youtu.be/YEF0iCiQlOg?t=4823)：從四個隨意位置開始迭代，收斂到**球對稱**的四個點（和 §9.3 的分析一致）。
- **$N=8$** [▶ 1:20:56](https://youtu.be/YEF0iCiQlOg?t=4856)：結果不一樣；k-means 的結果**不唯一**，取決於初始點 [▶ 1:21:30](https://youtu.be/YEF0iCiQlOg?t=4890)。
- **失真 vs. 迭代次數**：MSE 一路下降（它就是在最佳化失真）。
- **失真 vs. 碼本大小** [▶ 1:22:08](https://youtu.be/YEF0iCiQlOg?t=4928)：碼本越大（率越高）失真越低，**率失真曲線**出現了。
- **MNIST 影像** [▶ 1:22:41](https://youtu.be/YEF0iCiQlOg?t=4961)：取一千張 MNIST，向量長度是 $28\times28$，照樣可以分群、指定位元。MSE vs. 群數又是一條率失真曲線 [▶ 1:23:13](https://youtu.be/YEF0iCiQlOg?t=4993)。這某種意義上已經是一種影像有損壓縮：把影像分群再分配位元。

[▶ 1:23:49](https://youtu.be/YEF0iCiQlOg?t=5029) 最後一張圖：藍線是 k-means 實際得到的，紅線是 $D(R)=2^{-2R}$，**高斯的理論界**。Tsachy 下一講會講為什麼不管用什麼演算法（向量量化等）都不可能低於紅線。

> 以下**不是逐字稿內容**，是對照：§7 的 1 位元正負號量化器失真 0.363，紅線在 $R=1$ 是 0.25；兩者的差距就是更大區塊的向量量化理論上可以拿回來的。

---

## 12. 一頁速查表

### 有損壓縮的基本量

- 連續來源資訊量無限 ⇒ 一定要近似 ⇒ 有損。
- 失真：MSE $\mathbb{E}(X-\hat X)^2$、MAE $\mathbb{E}|X-\hat X|$；**看應用選**。
- 率：每符號位元數。率失真取捨：給 $D$ 最小化 $R$，或給 $R$ 最小化 $D$。

### 量化

| 名詞 | 意思 |
|---|---|
| 量化 | 連續 → 離散 |
| 碼字 / 符號 | 量化後的值 |
| 碼本 / 字典 | 所有量化值 |
| 率 | $R=\lceil\log_2N\rceil$（純量）；$R=\frac{\log_2N}{k}$（$k$ 維向量） |

### 1 位元量化 $\mathcal N(0,1)$（MSE）

- 決策門檻 0，重建 $\pm\mathbb{E}[X\mid X>0]=\pm\sqrt{2/\pi}\approx\pm0.798$。
- **關鍵一步**：MMSE $=\mathbb{E}[X\mid A]$；半高斯 $\int_0^\infty x\,2f(x)dx$ 用 $u=x^2/2$。
- 失真 $1-\frac2\pi\approx0.363$（理論最佳 0.25）。

### 純量 vs. 向量量化

| | 純量 | 向量 |
|---|---|---|
| 決定 | 門檻 + 量化值 | $\mathbb{R}^k$ 的分割 + $N$ 個碼向量 |
| 好處 | 簡單 | 利用相依（同號例子省 0.5 位元）；更好的區域形狀（六角形，MSE × 0.962） |
| 代價 | — | 最佳區域難算；Ziv：純量最多多 0.754 位元 |

### Lloyd / k-means

交替：最近中心分割 ↔ 群內平均更新碼本；結果依初始化而定；失真隨碼本變大而降，畫出率失真曲線。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 率失真曲線的理論、$D(R)=2^{-2R}$ | 第 12–13 集（互資訊、率失真函數、高斯） |
| 依前一個符號調整（預測） | 第 13–14 集轉換編碼、第 15 集 BPG |
| 量化後再無損熵編碼 | 第 14–15 集（JPEG：DCT → 量化 → Huffman） |
| 感知失真 vs. MSE | 第 17 集 Humans and Compression |
| 向量量化、學習出來的量化 | 第 16 集學習式影像壓縮 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **連續來源有無限多資訊，所以只能有損地近似；有損壓縮就是在失真（例如 MSE）和率之間取捨。量化把連續值對到大小 $N$ 的碼本，率約 $\log_2N$；最佳重建值取決於失真，MSE 下是條件期望值（1 位元量化高斯就是 $\pm\sqrt{2/\pi}$）。向量量化一次處理 $k$ 個符號，能利用相依、用更好的區域形狀，但最佳化很難、收益可能有限；實務上用 Lloyd 演算法（也就是 k-means）迭代求碼本，跑出來的就是一條率失真曲線。**

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 11 錄影逐字稿（人工字幕，1:24:27）、投影片 slide_11_2023、slide_11_2023_ann 與 Cover & Thomas《Elements of Information Theory》2nd ed. §10.1 整理。*
