---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 8
lecture: Lecture 8
date: 2023-10-23
video: https://youtu.be/tGPF2nw5Exc
notes: 投影片 L8.pdf（55 頁，打字＋手寫）；《Elements of Information Theory》§2.2、§2.6、§4.1–4.2、§16.8
---

# 第 8 集 · Lecture 8：超越 iid：條件熵（Beyond IID Distributions: Conditional Entropy） [▶ 影片](https://youtu.be/tGPF2nw5Exc)

← 上一集：[07-ans](07-ans.md) ｜ [總目錄](README.md) ｜ 下一集：[09-context-based-ac-llm-compression](09-context-based-ac-llm-compression.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 8 集
> **講者**：Shubham Chandak（Pulkit 中途補充）
> **來源**：YouTube 錄影逐字稿（1:16:25，人工字幕 en-US）＋ 投影片 `L8.pdf` ＋ Cover & Thomas §2.2、§2.6、§4.1–4.2、§16.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 熵編碼器總回顧](#1-熵編碼器總回顧)
- [2. 小考檢討：rANS 與「什麼時候用誰」](#2-小考檢討rans-與什麼時候用誰)
- [3. 動機：為什麼 gzip 能壓得比熵還小](#3-動機為什麼-gzip-能壓得比熵還小)
- [4. 隨機過程與平穩過程](#4-隨機過程與平穩過程)
- [5. Markov 過程](#5-markov-過程)
- [6. 把相依序列變成 iid：差分](#6-把相依序列變成-iid差分)
- [7. $k$ 階 Markov 來源](#7-k-階-markov-來源)
- [8. 非例子：公車到站時間](#8-非例子公車到站時間)
- [9. 條件熵](#9-條件熵)
- [10. 條件熵的性質](#10-條件熵的性質)
- [11. 熵率](#11-熵率)
- [12. 英文的熵率](#12-英文的熵率)
- [13. 熵率是壓縮的極限](#13-熵率是壓縮的極限)
- [14. 一頁速查表](#14-一頁速查表)
- [15. 與後續集數的連結](#15-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/tGPF2nw5Exc?t=5) 接下來三講：**超越 iid 資料**的無損壓縮。

[▶ 23:57](https://youtu.be/tGPF2nw5Exc?t=1437) 大綱：

| 講 | 內容 |
|---|---|
| 第 8 講（本集） | 非 iid 的機率分布、熵率、Markov 來源（有點理論；學過機率或資訊理論的人會覺得重複） |
| 第 9 講 | context-based 算術編碼、LZ77 通用壓縮入門 |
| 第 10 講 | 無損壓縮實務、案例研究（無損部分最後一講） |

| 本集主題 | 課本 |
|---|---|
| 隨機過程、平穩、Markov | §4.1 |
| 條件熵、鏈鎖律、條件會降低熵 | §2.2、§2.6 |
| 熵率 | §4.2 |
| Shannon–McMillan–Breiman 定理 | §16.8 |

【投影片補充】`L8.pdf` p.2 公告：作業 1 的回饋和解答已發；作業 2 已發（Ed 上有置頂的澄清討論串）；期末專題提案；IT Forum。

---

## 1. 熵編碼器總回顧

[▶ 00:41](https://youtu.be/tGPF2nw5Exc?t=41)

| 編碼器 | 優點 | 缺點 |
|---|---|---|
| **Huffman** | 很快；單符號（或固定區塊）的最佳碼；大區塊時達到熵 | 區塊加大時複雜度指數成長 |
| **算術編碼** [▶ 01:13](https://youtu.be/tGPF2nw5Exc?t=73) | 整份輸入是一個區塊，線性時間達到熵，只多 $\frac2n$ | 要除法或浮點乘法，慢 [▶ 01:49](https://youtu.be/tGPF2nw5Exc?t=109)；所以快速壓縮器不用它，但很多重型壓縮器用 |
| **ANS**（rANS、tANS）[▶ 02:27](https://youtu.be/tGPF2nw5Exc?t=147) | 整份輸入一個區塊，有效率地達到熵；比算術編碼快，tANS 接近 Huffman 速度 | tANS 比算術編碼多一點點負擔 |

[▶ 01:49](https://youtu.be/tGPF2nw5Exc?t=109) 算術編碼有一個今天和下一講很重要的性質：**它能配合非常複雜的機率模型**，遠超過目前課堂看過的。

[▶ 03:01](https://youtu.be/tGPF2nw5Exc?t=181) 課堂的演算法都是簡化的 Python 虛擬碼。大家已經想出在現代 CPU 上極有效率地實作 tANS 的方法，這是它越來越流行的原因。

【口頭】[▶ 03:39](https://youtu.be/tGPF2nw5Exc?t=219) 延伸閱讀：Jarek Duda 的 rANS/tANS 論文、幾位實作者的部落格。很多壓縮界的好東西在一個俄羅斯論壇（encode.su）上，Zstandard 的作者 Yann Collet、ANS 的發明者 Jarek Duda 都在那裡評論最新進展。

[▶ 04:46](https://youtu.be/tGPF2nw5Exc?t=286) rANS 解碼比算術編碼快很多。很多應用裡解碼時間很關鍵。[▶ 04:46](https://youtu.be/tGPF2nw5Exc?t=286) 這些熵編碼器實際上被使用，有時是因為它們最適合，很多時候是因為大家一直在用、壓縮格式很難換（歷史原因）。

[▶ 05:22](https://youtu.be/tGPF2nw5Exc?t=322) 這些熵編碼器做的事都是同一張方塊圖 [▶ 06:07](https://youtu.be/tGPF2nw5Exc?t=367)：

```
已知分布 P（iid）
x1, ..., xn ──> [熵編碼器] ──> 位元數 ≈ n·H(X)
```

---

## 2. 小考檢討：rANS 與「什麼時候用誰」

### 2.1 rANS 編碼

[▶ 06:48](https://youtu.be/tGPF2nw5Exc?t=408) $\mathcal{X}=\{0,1,2\}$，機率 $\left(\frac38,\frac38,\frac28\right)$ → $M=8$、$\mathrm{freq}=[3,3,2]$、$\mathrm{cumul}=[0,3,6]$ [▶ 07:59](https://youtu.be/tGPF2nw5Exc?t=479)。編碼串 `2, 0, 1, 0`：

| 符號 | 計算 | 狀態 |
|---|---|---|
| 2 | $\lfloor0/2\rfloor\cdot8+6+(0\ \mathrm{mod}\ 2)$ | 6 [▶ 07:59](https://youtu.be/tGPF2nw5Exc?t=479) |
| 0 | $\lfloor6/3\rfloor\cdot8+0+(6\ \mathrm{mod}\ 3)$ | 16 [▶ 08:44](https://youtu.be/tGPF2nw5Exc?t=524) |
| 1 | $\lfloor16/3\rfloor\cdot8+3+(16\ \mathrm{mod}\ 3)$ | 44 |
| 0 | $\lfloor44/3\rfloor\cdot8+0+(44\ \mathrm{mod}\ 3)$ | 114 [▶ 09:22](https://youtu.be/tGPF2nw5Exc?t=562) |

（第 3 步是自己算的，課堂只說「做完會得到 114」。）

【口頭】[▶ 06:48](https://youtu.be/tGPF2nw5Exc?t=408) **編碼要除以 $\mathrm{freq}[s]$**，除法很慢；**解碼只除以 $M$**，$M$ 通常是 2 的冪，等於位移，很便宜。所以 rANS 解碼速度差不多是編碼的兩倍 [▶ 07:24](https://youtu.be/tGPF2nw5Exc?t=444)。

> ⚠️ 逐字稿缺字 [▶ 06:48](https://youtu.be/tGPF2nw5Exc?t=408)：字幕「Whereas during encoding, you see there is only one division step, but it's division by M」，依上下文應為「during **decoding**」。

### 2.2 rANS 解碼

[▶ 09:22](https://youtu.be/tGPF2nw5Exc?t=562) 最終狀態 117、4 個符號 [▶ 09:59](https://youtu.be/tGPF2nw5Exc?t=599)：

1. $\text{block\_id}=\lfloor117/8\rfloor=14$，$\text{slot}=117\ \mathrm{mod}\ 8=5$。
2. 5 落在 $[3,6)$ → $s=1$ [▶ 10:36](https://youtu.be/tGPF2nw5Exc?t=636)。
3. $x_{\text{prev}}=14\times3+5-3=44$。

[▶ 11:30](https://youtu.be/tGPF2nw5Exc?t=690) **核心**：編碼是 $x\approx x_{\text{prev}}/p(s)$，解碼是 $x_{\text{prev}}\approx x\cdot p(s)$。這就是 $\log\frac1p$ 的來源。

### 2.3 什麼時候用 ANS、算術編碼、Huffman？

[▶ 12:12](https://youtu.be/tGPF2nw5Exc?t=732)（`L8.pdf` p.13，可複選）

| 情境 | 答案 |
|---|---|
| 要最好的壓縮率，可以犧牲速度 | **算術編碼** [▶ 12:44](https://youtu.be/tGPF2nw5Exc?t=764) |
| 要極快的編解碼，可以犧牲壓縮率 | **Huffman** [▶ 13:21](https://youtu.be/tGPF2nw5Exc?t=801)：誰都比不過它的簡單 |
| 要**自適應**解碼（編碼器和解碼器邊看資料邊建模型） | **算術編碼** [▶ 13:21](https://youtu.be/tGPF2nw5Exc?t=801)（下一講解釋） |
| 要接近最佳的壓縮，也要好的速度 | **ANS** [▶ 13:55](https://youtu.be/tGPF2nw5Exc?t=835) |
| 用現代處理器的平行運算，又要接近最佳的壓縮 | **ANS**（SIMD）[▶ 13:55](https://youtu.be/tGPF2nw5Exc?t=835) |

【口頭】[▶ 14:29](https://youtu.be/tGPF2nw5Exc?t=869) **SIMD**（single instruction, multiple data）：x86、ARM 上同一個運算重複做時可以平行化。rANS 的做法：符號 1、3、5、7… 和 2、4、6、8… **交錯**成兩條同時壓 [▶ 14:29](https://youtu.be/tGPF2nw5Exc?t=869)，不用兩個核心就快兩倍（要照特定方式寫程式；投影片有論文連結）[▶ 15:02](https://youtu.be/tGPF2nw5Exc?t=902)。

【Q&A】[▶ 15:43](https://youtu.be/tGPF2nw5Exc?t=943) 學生問：第一題為什麼不選 ANS？表上 rANS 壓縮率和算術編碼一樣，速度還快很多。講者 [▶ 16:14](https://youtu.be/tGPF2nw5Exc?t=974)：對，表上 rANS 壓縮和算術編碼一樣、只是解碼快；tANS 多一點點負擔。看用途，可以申請重新評分（字幕作「regret thing」）。

【口頭】[▶ 16:45](https://youtu.be/tGPF2nw5Exc?t=1005) **真心建議**：如果資料是 iid、你也知道它是 iid，**不要用算術編碼，用 rANS 或 tANS**。現在用算術編碼的唯一理由是**非 iid 或自適應**的分布。[▶ 16:45](https://youtu.be/tGPF2nw5Exc?t=1005) Pulkit 補充（字幕不全）：表是某個特定資料的結果；算術編碼的真正用處是能自適應地使用機率，下一講會講 [▶ 17:21](https://youtu.be/tGPF2nw5Exc?t=1041)。

---

## 3. 動機：為什麼 gzip 能壓得比熵還小

[▶ 17:55](https://youtu.be/tGPF2nw5Exc?t=1075) 這段文字是哪本書？學生答出：《巴斯克維爾的獵犬》（The Hound of the Baskervilles，柯南·道爾，福爾摩斯）。

[▶ 18:28](https://youtu.be/tGPF2nw5Exc?t=1108) 講者算它的**經驗熵**（各字母頻率 → 熵 × 長度）：

| 方法 | 大小 |
|---|---|
| 原檔 | 387 KB |
| 經驗熵（逐字母、iid） | 199,833 位元組 [▶ 18:28](https://youtu.be/tGPF2nw5Exc?t=1108) |
| gzip | 134,718 位元組 |
| bzip2 | 99,679 位元組 |

（數字依 `L8.pdf` p.15–16。）

[▶ 18:58](https://youtu.be/tGPF2nw5Exc?t=1138) gzip、bzip2 不是最先進的，是 20–30 年的老壓縮器，卻比熵小很多。不是說熵是任何無損壓縮器的下界嗎？

【課堂討論】[▶ 19:32](https://youtu.be/tGPF2nw5Exc?t=1172) 學生答：可以看前一個字母來決定下一個的機率，例如 T 後面很可能是 H [▶ 19:32](https://youtu.be/tGPF2nw5Exc?t=1172)。（作業 1 也有一題 gzip 比 Huffman 好。）

[▶ 20:07](https://youtu.be/tGPF2nw5Exc?t=1207) 講者：對。前七講都假設 **iid**，但世界不是 iid：

- T 後面常是 H（the、then、this、that）。
- **Q 後面幾乎一定是 U** [▶ 20:07](https://youtu.be/tGPF2nw5Exc?t=1207)。
- 句首第一個字母大寫，後面小寫 [▶ 20:43](https://youtu.be/tGPF2nw5Exc?t=1243)。

iid 只說 E 占 15%、T 占 10%……，完全沒說「前一個是什麼時，下一個的分布是什麼」[▶ 21:22](https://youtu.be/tGPF2nw5Exc?t=1282)。

**第二個原因** [▶ 21:22](https://youtu.be/tGPF2nw5Exc?t=1282)：整個檔案的分布可能不一樣。把 Java 程式碼和福爾摩斯小說串在一起算熵，會得到兩者的混合，對哪一個都不是最佳的。【投影片補充】`L8.pdf` p.17：「想像把英文小說和印地文小說接在一起」。

[▶ 22:03](https://youtu.be/tGPF2nw5Exc?t=1323) 接下來處理兩件事：**非 iid 資料**，以及**事先不知道分布**的資料。作業 1 是算經驗熵、用 Huffman 編、存碼本；真實資料的分布通常很複雜，事先不知道 [▶ 22:43](https://youtu.be/tGPF2nw5Exc?t=1363)。

[▶ 22:43](https://youtu.be/tGPF2nw5Exc?t=1363) 不只文字：

- **圖片**：相鄰像素相關，白色旁邊多半白色，天空的藍色聚在一起。
- **影片** [▶ 23:22](https://youtu.be/tGPF2nw5Exc?t=1402)：相鄰畫面很像。
- 表格、幾乎所有真實資料都不是 iid。

[▶ 24:37](https://youtu.be/tGPF2nw5Exc?t=1477) 別灰心：前面學的工具在非 iid 和有損壓縮裡都非常有用。

---

## 4. 隨機過程與平穩過程

### 4.1 機率回顧

[▶ 25:24](https://youtu.be/tGPF2nw5Exc?t=1524) iid：$P(U^n)=\prod_{i=1}^nP(U_i)$。一般情況要用**鏈鎖律** [▶ 25:57](https://youtu.be/tGPF2nw5Exc?t=1557)：

$$P(U^n)=\prod_{i=1}^{n}P(U_i\mid U^{i-1}),\qquad\text{例如 }P(U_1,U_2)=P(U_1)P(U_2\mid U_1).$$

### 4.2 隨機過程

[▶ 26:44](https://youtu.be/tGPF2nw5Exc?t=1604) **隨機過程**（stochastic process，random process）：一串隨機變數 $(U_1,U_2,\dots)$，彼此可以**任意相依**。要描述它，得對每個 $n$ 給出 $(U_1,\dots,U_n)$ 的聯合分布 [▶ 27:18](https://youtu.be/tGPF2nw5Exc?t=1638)。太一般了，理論上用處不大；但要知道有這個概念，$U_n$ 甚至可以依賴一百萬步以前的東西。

### 4.3 平穩過程

[▶ 27:53](https://youtu.be/tGPF2nw5Exc?t=1673) **平穩過程**（stationary process）：**時間不變**的隨機過程。不管從第 0、第 100 還是第一百萬個位置看，機率都一樣 [▶ 28:29](https://youtu.be/tGPF2nw5Exc?t=1709)：對所有 $n$、所有平移 $l$、所有 $(u_1,\dots,u_n)$，

$$P(U_1=u_1,\dots,U_n=u_n)=P(U_{l+1}=u_1,\dots,U_{l+n}=u_n).$$

例：$(U_1,U_2)$ 和 $(U_{100},U_{101})$ 同分布。

[▶ 29:06](https://youtu.be/tGPF2nw5Exc?t=1746) 特別地，平均、變異數、熵都不隨 $n$ 改變：$\mathbb{E}U_1=\mathbb{E}U_{100}$、$H(U_1)=H(U_{100})$、$H(U_1,U_3)=H(U_{1000},U_{1002})$。

[▶ 29:40](https://youtu.be/tGPF2nw5Exc?t=1780) 但平穩過程**可以有任意的時間相依**：$U_1$ 和 $U_{1{,}000{,}000{,}000}$ 可以相依。

### 4.4 iid ⇒ 平穩【課堂討論】

[▶ 30:12](https://youtu.be/tGPF2nw5Exc?t=1812) 公平硬幣 iid：$P(U_1,\dots,U_4)=(H,T,T,H)$ 的機率？學生答 $\frac1{2^4}$ [▶ 30:49](https://youtu.be/tGPF2nw5Exc?t=1849)。往後平移到 $(U_{l+1},\dots,U_{l+4})$ 呢？一樣，因為 iid [▶ 31:22](https://youtu.be/tGPF2nw5Exc?t=1882)。

> **iid 是平穩的特例。** 目前看過的過程都是平穩的。

---

## 5. Markov 過程

### 5.1 定義

[▶ 31:22](https://youtu.be/tGPF2nw5Exc?t=1882) **Markov 過程**：只用一步的條件機率定義：給 $U_1$ 定義 $U_2\mid U_1$，給 $U_2$ 定義 $U_3\mid U_2$……[▶ 32:00](https://youtu.be/tGPF2nw5Exc?t=1920)

> 給定 $U_{n-1}$，$U_n$ 和 $U_{n-2},\dots,U_1$ 獨立。

知道前一個符號就夠了，再告訴你前一百萬個也沒用 [▶ 32:39](https://youtu.be/tGPF2nw5Exc?t=1959)。

### 5.2 例子

[▶ 32:39](https://youtu.be/tGPF2nw5Exc?t=1959)（`L8.pdf` p.22–23）

$$U_1\sim\mathrm{Unif}\{0,1,2\},\qquad U_{i+1}=(U_i+Z_i)\ \mathrm{mod}\ 3,\qquad Z_i\sim\mathrm{Ber}\left(\tfrac12\right)\ \text{iid}.$$

在 0 時，下一個以 $\frac12$ 留在 0、$\frac12$ 到 1；在 1 時到 1 或 2；在 2 時到 2 或 0（mod 3 繞回來）[▶ 33:52](https://youtu.be/tGPF2nw5Exc?t=2032)。三種表示法：狀態圖、方程式、**轉移矩陣**（transition matrix）[▶ 34:26](https://youtu.be/tGPF2nw5Exc?t=2066)：

| $U_i\backslash U_{i+1}$ | 0 | 1 | 2 |
|---|---|---|---|
| 0 | 0.5 | 0.5 | 0 |
| 1 | 0 | 0.5 | 0.5 |
| 2 | 0.5 | 0 | 0.5 |

### 5.3 算 $P(U_2=0)$【課堂討論】

[▶ 34:26](https://youtu.be/tGPF2nw5Exc?t=2066) 先**邊際化**（marginalization，學生回答出名稱 [▶ 35:31](https://youtu.be/tGPF2nw5Exc?t=2131)），再用**鏈鎖律** [▶ 36:03](https://youtu.be/tGPF2nw5Exc?t=2163)：

$$
\begin{aligned}
P(U_2=0)&=\sum_{u=0}^{2}P(U_1=u,U_2=0)=\sum_{u=0}^{2}P(U_1=u)\,P(U_2=0\mid U_1=u)\\
&=\tfrac13\cdot\tfrac12+\tfrac13\cdot0+\tfrac13\cdot\tfrac12=\tfrac13.
\end{aligned}
$$

學生逐項答：$P(U_1=u)=\frac13$（均勻）[▶ 36:47](https://youtu.be/tGPF2nw5Exc?t=2207)；$P(U_2=0\mid U_1=0)=\frac12$；$P(U_2=0\mid U_1=1)=0$（從 1 回不到 0）[▶ 37:20](https://youtu.be/tGPF2nw5Exc?t=2240)。

[▶ 37:53](https://youtu.be/tGPF2nw5Exc?t=2273) 對 Markov 鏈，**只要 $U_2$ 和 $U_1$ 同分布，就是平穩的** [▶ 38:40](https://youtu.be/tGPF2nw5Exc?t=2320)：分布一步不變，歸納下去每一步都不變，所有聯合分布也不變。這裡 $U_2$ 也是均勻分布，所以平穩。

### 5.4 起始分布不對就不平穩【課堂討論】

[▶ 39:16](https://youtu.be/tGPF2nw5Exc?t=2356) 如果 $U_1=0$（機率 1）呢？學生答 $P(U_2=0)=\frac12$ [▶ 39:53](https://youtu.be/tGPF2nw5Exc?t=2393)。分布變了，**不平穩**。Markov 鏈要從正確的分布出發才平穩。（小考有類似題。）

---

## 6. 把相依序列變成 iid：差分

【課堂討論】[▶ 40:31](https://youtu.be/tGPF2nw5Exc?t=2431) 怎麼把這個 Markov 序列變成 iid？寫成

$$U_1,\quad U_1+Z_1,\quad U_2+Z_2,\quad U_3+Z_3,\ \dots\quad(\text{mod }3).$$

學生答：**相鄰相減** [▶ 41:55](https://youtu.be/tGPF2nw5Exc?t=2515)。$U_2-U_1=Z_1$、$U_3-U_2=Z_2$……（mod 3），就是 iid 的 $Z_i$。

[▶ 42:27](https://youtu.be/tGPF2nw5Exc?t=2547) 原本看起來有相依的過程，相減後變 iid，再用你喜歡的 Huffman、ANS 等。不一定都這麼簡單，但常常可以用簡單的轉換把資料變成接近 iid；有損壓縮部分會一再看到。這叫**差分編碼**（delta coding，diff coding）[▶ 42:27](https://youtu.be/tGPF2nw5Exc?t=2547)。

> 以下**不是逐字稿內容**，是算出差分的效果：直接把 $U_i$ 當 iid 均勻編，每符號 $\log_23\approx1.58$ 位元；差分後 $Z_i\sim\mathrm{Ber}(\frac12)$，每符號 1 位元，正好是 §11 算出的熵率。

---

## 7. $k$ 階 Markov 來源

[▶ 43:03](https://youtu.be/tGPF2nw5Exc?t=2583) 推廣：目前符號只依賴前 $k$ 個符號。用預測的話說：$U_{n-1},\dots,U_{n-k}$ 就足以預測 $U_n$，更早的過去沒有幫助 [▶ 43:35](https://youtu.be/tGPF2nw5Exc?t=2615)。

> **$k$ 階 Markov 來源**（`L8.pdf` p.26）：對所有 $n$，
> $$P(U_n\mid U_{n-1},U_{n-2},\dots)=P(U_n\mid U_{n-1},\dots,U_{n-k}).$$

[▶ 44:44](https://youtu.be/tGPF2nw5Exc?t=2684) 平穩來源可以有任意時間相依；$k$ 階 Markov 只依賴過去 $k$ 個。**大多數實際的平穩來源都能用有限 $k$ 階模型近似得很好**；$k$ 越大近似越好，但報酬遞減。

[▶ 45:16](https://youtu.be/tGPF2nw5Exc?t=2716) 說「Markov」通常指 1 階；**iid = 0 階**（不依賴任何過去）。

---

## 8. 非例子：公車到站時間

【課堂討論】[▶ 45:54](https://youtu.be/tGPF2nw5Exc?t=2754) 公車大約每 15 分鐘一班，到站時間 4:16、4:28、4:46、5:02……是平穩過程嗎？

[▶ 46:26](https://youtu.be/tGPF2nw5Exc?t=2786) 平穩過程的平均不隨時間變。第一班預期 4:00 到，第二班也預期 4:00 到嗎？不，是 4:15、4:30……所以**不是平穩的**，平均隨時間增加 [▶ 47:01](https://youtu.be/tGPF2nw5Exc?t=2821)。

能不能轉換成平穩的？學生答：**取相鄰差** [▶ 47:35](https://youtu.be/tGPF2nw5Exc?t=2855)。4:28 − 4:16 = 12 分鐘，這叫**到站間隔時間**（interarrival time），理論上常用指數分布建模 [▶ 48:40](https://youtu.be/tGPF2nw5Exc?t=2920)。

【口頭】[▶ 47:35](https://youtu.be/tGPF2nw5Exc?t=2855) 這在真實資料裡出奇地常見。很多壓縮器在平穩序列上表現很好，給它非平穩的就失敗：把 `1, 2, 3, 4, 5, 6…` 這種一看就能預測的檔案丟給最先進的 Zstandard，它壓得很爛；先做差分，變成一串很像的值，壓縮立刻變好 [▶ 48:07](https://youtu.be/tGPF2nw5Exc?t=2887)。所以理論很重要：知道壓縮器在哪裡好、哪裡不好，不好時能不能轉換成別的序列。

---

## 9. 條件熵

### 9.1 定義

[▶ 49:15](https://youtu.be/tGPF2nw5Exc?t=2955) 回顧 $H(U)=\sum_uP(u)\log\frac1{P(u)}$。

> **條件熵**（conditional entropy）[▶ 49:51](https://youtu.be/tGPF2nw5Exc?t=2991)：
> $$H(U\mid V)\triangleq\mathbb{E}\left[\log\frac1{P(U\mid V)}\right].$$

展開 [▶ 50:29](https://youtu.be/tGPF2nw5Exc?t=3029)：

$$
\begin{aligned}
H(U\mid V)&=\sum_{u,v}P(u,v)\log\frac1{P(u\mid v)}\\
&=\sum_vP(v)\sum_uP(u\mid v)\log\frac1{P(u\mid v)}&&\text{（鏈鎖律 }P(u,v)=P(v)P(u\mid v)\text{）}\\
&=\sum_vP(v)\,H(U\mid V=v).
\end{aligned}
$$

兩個量：

- **$H(U\mid V=v)$** [▶ 50:29](https://youtu.be/tGPF2nw5Exc?t=3029)：已知 $V=v$ 時 $U$ 的熵，就是分布 $P(\cdot\mid v)$ 的普通熵 [▶ 51:15](https://youtu.be/tGPF2nw5Exc?t=3075)。例：若 $V=v$ 時 $U\sim\mathrm{Ber}(\frac12)$，則 $H(U\mid V=v)=1$。
- **$H(U\mid V)$** [▶ 51:48](https://youtu.be/tGPF2nw5Exc?t=3108)：上面那個對 $v$ 的平均。

### 9.2 直覺【課堂討論】

[▶ 52:29](https://youtu.be/tGPF2nw5Exc?t=3149) 熵高代表什麼？學生答：均勻分布最高、常數是 0，也就是不確定性 [▶ 52:29](https://youtu.be/tGPF2nw5Exc?t=3149)。

[▶ 53:04](https://youtu.be/tGPF2nw5Exc?t=3184) 所以：

- $H(U\mid V=v)$ = **已知 $V=v$ 之後，$U$ 還剩多少不確定性**。若知道 $V=v$ 就讓 $U$ 確定，它就很小。
- $H(U\mid V)$ = 平均而言，知道 $V$ 之後 $U$ 剩多少不確定性 [▶ 53:55](https://youtu.be/tGPF2nw5Exc?t=3235)。

**推理遊戲的比喻** [▶ 54:29](https://youtu.be/tGPF2nw5Exc?t=3269)：$U$ = 兇手是誰。你一路拿到線索（例如指紋）。**某個特定線索可能讓你更困惑**（$H(U\mid V=v)$ 可以比 $H(U)$ 大也可以比較小）；但**平均而言，知道越多不會更差** [▶ 55:06](https://youtu.be/tGPF2nw5Exc?t=3306)。像福爾摩斯那樣的好偵探，線索越多不確定性越低，最後鎖定真兇。

### 9.3 例子

[▶ 55:40](https://youtu.be/tGPF2nw5Exc?t=3340) 聯合分布（`L8.pdf` p.32）：

| | $V=0$ | $V=1$ |
|---|---|---|
| $U=0$ | 1/4 | 1/4 |
| $U=1$ | 0 | 1/2 |

- $U$ 均勻分布在 $\{0,1\}$ [▶ 55:40](https://youtu.be/tGPF2nw5Exc?t=3340)。
- $U=0$ 時 [▶ 56:20](https://youtu.be/tGPF2nw5Exc?t=3380)：$P(V=0\mid U=0)=\frac{1/4}{1/2}=\frac12$，$V\sim\mathrm{Ber}(\frac12)$。
- $U=1$ 時：$V$ 一定是 1。

【課堂討論】[▶ 56:55](https://youtu.be/tGPF2nw5Exc?t=3415)

- $H(V\mid U=0)=1$（$\mathrm{Ber}(\frac12)$）。
- $H(V\mid U=1)=0$（確定的）[▶ 57:27](https://youtu.be/tGPF2nw5Exc?t=3447)。
- $H(V\mid U)=\frac12\cdot1+\frac12\cdot0=\frac12$。

講者在家算的 [▶ 58:08](https://youtu.be/tGPF2nw5Exc?t=3488)：

$$H(U)=1,\qquad H(V)=\tfrac14\log_24+\tfrac34\log_2\tfrac43\approx0.811,\qquad H(U,V)=\tfrac14\log4+\tfrac14\log4+\tfrac12\log2=\tfrac32.$$

觀察：

- $H(V\mid U)=0.5\le H(V)=0.811$：知道 $U$ 平均降低了 $V$ 的不確定性。
- 但 $H(V\mid U=0)=1>0.811$：知道 $U=0$ 這個特定值**增加**了不確定性。
- [▶ 58:57](https://youtu.be/tGPF2nw5Exc?t=3537) $H(U,V)=\frac32=H(U)+H(V\mid U)=1+\frac12$。

---

## 10. 條件熵的性質

[▶ 59:34](https://youtu.be/tGPF2nw5Exc?t=3574)（`L8.pdf` p.36）

1. **條件會降低熵**：$H(U\mid V)\le H(U)$，等號當且僅當 $U$、$V$ 獨立 [▶ 59:34](https://youtu.be/tGPF2nw5Exc?t=3574)。（特定證據可能增加不確定性，但平均而言知識總是降低不確定性 [▶ 1:00:10](https://youtu.be/tGPF2nw5Exc?t=3610)。）
2. **熵的鏈鎖律** [▶ 1:00:10](https://youtu.be/tGPF2nw5Exc?t=3610)：
$$H(U,V)=H(U)+H(V\mid U)=H(V)+H(U\mid V).$$
3. **聯合熵 ≤ 熵的和**：$H(U,V)\le H(U)+H(V)$，等號當且僅當獨立。

[▶ 1:00:58](https://youtu.be/tGPF2nw5Exc?t=3658) 回想獨立時是 $H(U,V)=H(U)+H(V)$；一般情況是鏈鎖律。

【課本補充】證明（§2.2 Theorem 2.2.1、§2.6 Theorem 2.6.5；課堂沒證）：

- **鏈鎖律**：$\log\frac1{P(u,v)}=\log\frac1{P(u)}+\log\frac1{P(v\mid u)}$，兩邊取期望值即得。
- **條件降低熵**：
$$H(U)-H(U\mid V)=\sum_{u,v}P(u,v)\log\frac{P(u\mid v)}{P(u)}=\sum_{u,v}P(u,v)\log\frac{P(u,v)}{P(u)P(v)}=D\left(P_{UV}\,\|\,P_UP_V\right)\ge0,$$
等號當且僅當 $P(u,v)=P(u)P(v)$，即獨立。（這個量叫互資訊 $I(U;V)$，第 12 集會講。）
- **性質 3**：由 2 和 1，$H(U,V)=H(U)+H(V\mid U)\le H(U)+H(V)$。

### 10.1 用壓縮的話說

[▶ 1:00:58](https://youtu.be/tGPF2nw5Exc?t=3658)

- $H(U)$：單獨壓 $U$ 最好能到多少。
- $H(V\mid U)$：**已知 $U$** 時壓 $V$ 最好能到多少 [▶ 1:01:42](https://youtu.be/tGPF2nw5Exc?t=3702)。
- 鏈鎖律：要聯合壓 $U$、$V$，可以**先壓 $U$，再在已知 $U$ 下壓 $V$**，位元數相加。例：1 位元 + 0.5 位元 = 1.5 位元。
- 性質 3：分開各自壓縮不會比聯合壓縮好。

**極端例子** [▶ 1:02:29](https://youtu.be/tGPF2nw5Exc?t=3749)：$U\sim\mathrm{Ber}(\frac12)$、$V=1-U$。

$$H(U)=H(V)=1,\qquad H(U,V)=1<H(U)+H(V)=2.$$

分開壓要各 1 位元；用 $U$ 的知識壓 $V$，$V$ 就**免費**了 [▶ 1:03:19](https://youtu.be/tGPF2nw5Exc?t=3799)。

[▶ 1:03:51](https://youtu.be/tGPF2nw5Exc?t=3831) 一般可以對過去 $n$ 個條件化：$H(U_{n+1}\mid U_1,\dots,U_n)$。

---

## 11. 熵率

### 11.1 兩個定義

[▶ 1:03:51](https://youtu.be/tGPF2nw5Exc?t=3831) 熵是壓縮 iid 序列的極限；平穩序列（Markov 等）要什麼？[▶ 1:04:25](https://youtu.be/tGPF2nw5Exc?t=3865) **熵率**（entropy rate），對任何平穩過程都有定義，而且有**兩個**定義（投影片放了「買一送一」的圖）：

$$H_1(\mathbf U)=\lim_{n\to\infty}H(U_{n+1}\mid U_1,\dots,U_n),\qquad H_2(\mathbf U)=\lim_{n\to\infty}\frac{H(U_1,\dots,U_n)}{n}.$$

- $H_1$ [▶ 1:05:04](https://youtu.be/tGPF2nw5Exc?t=3904)：知道前一百萬個符號後，下一個符號還剩多少熵：**每個新符號額外貢獻的熵** [▶ 1:06:16](https://youtu.be/tGPF2nw5Exc?t=3976)。
- $H_2$ [▶ 1:05:04](https://youtu.be/tGPF2nw5Exc?t=3904)：聯合壓 $n$ 個符號，每符號付多少，區塊越來越大：**大區塊時的平均位元／符號**。

[▶ 1:05:41](https://youtu.be/tGPF2nw5Exc?t=3941) 對任何平穩過程兩者相等，這個極限叫熵率，記作 $H(\mathbf U)$。講者說記一個的話記 $H_1$，比較常用。

【投影片補充】`L8.pdf` p.43 引用 **C&T Theorem 4.2.1**：平穩過程的兩個極限相等。

【課本補充】§4.2（書頁 74–76）的證明骨架：(a) 平穩 + 條件降低熵 ⇒ $H(U_{n+1}\mid U^n)\le H(U_{n+1}\mid U_2^n)=H(U_n\mid U^{n-1})$，所以 $H(U_{n+1}\mid U^n)$ 遞減且 $\ge0$，極限存在；(b) 鏈鎖律 $\frac1nH(U^n)=\frac1n\sum_{i=1}^nH(U_i\mid U^{i-1})$ 是這個數列的 Cesàro 平均，收斂到同一個極限。

### 11.2 例子

[▶ 1:06:47](https://youtu.be/tGPF2nw5Exc?t=4007)

- **公平硬幣（iid）**：$\frac1nH(U_1,\dots,U_n)=\frac{nH(U_1)}n=1$ 位元 [▶ 1:07:25](https://youtu.be/tGPF2nw5Exc?t=4045)。**iid 的熵率 = 熵**。
- **Markov 例子** [▶ 1:07:25](https://youtu.be/tGPF2nw5Exc?t=4045)：已知 $U_1$（例如 0），$U_2$ 以相等機率取兩個值，所以 $H(U_2\mid U_1)=h_b(\frac12)=1$ 位元 [▶ 1:08:07](https://youtu.be/tGPF2nw5Exc?t=4087)。由 Markov 性質 $H(U_n\mid U_{n-1},\dots,U_1)=H(U_n\mid U_{n-1})$ [▶ 1:08:43](https://youtu.be/tGPF2nw5Exc?t=4123)，平穩所以都等於 $H(U_2\mid U_1)$，熵率 **1 位元**。

> 以下**不是逐字稿內容**，是對照：同一條 Markov 鏈，每個 $U_i$ 的邊際分布是均勻的，$H(U_i)=\log_23\approx1.58$；熵率只有 1。差的 0.58 位元就是「看前一個符號」能省下的。

[▶ 1:09:20](https://youtu.be/tGPF2nw5Exc?t=4160) 一般公式（`L8.pdf` p.45）：

| 來源 | 熵率 |
|---|---|
| iid | $H(\mathbf U)=H(U_1)$ |
| $k$ 階 Markov | $H(\mathbf U)=H(U_{k+1}\mid U_k,\dots,U_1)$ [▶ 1:09:52](https://youtu.be/tGPF2nw5Exc?t=4192) |

[▶ 1:09:52](https://youtu.be/tGPF2nw5Exc?t=4192) 意思：知道過去 $k$ 個符號後，下一個符號還有多少不確定性。

---

## 12. 英文的熵率

[▶ 1:10:27](https://youtu.be/tGPF2nw5Exc?t=4227) 拿大量英文文本估計機率：一次看 1、2、3、4 個字元，做機率表。例如 [▶ 1:11:13](https://youtu.be/tGPF2nw5Exc?t=4273)：

$$\hat P(U_1=A,U_2=C)=\frac{\#\{n:x_n=A,\ x_{n+1}=C\}}{\text{總數}}.$$

結果（`L8.pdf` p.46，來源是 Duke 的資訊理論講義）[▶ 1:11:49](https://youtu.be/tGPF2nw5Exc?t=4309)：

| 模型 | 位元／字母 |
|---|---|
| 0 階（iid） | 4.76 |
| 1 階 Markov | 4.03（Q 後面多半是 U） |
| 4 階 Markov | 2.8（看到 T、H、I，可能是 this 或 thing）[▶ 1:12:24](https://youtu.be/tGPF2nw5Exc?t=4344) |
| Shannon 1952 年的人類預測實驗 | 1.3 [▶ 1:12:59](https://youtu.be/tGPF2nw5Exc?t=4379) |

[▶ 1:12:59](https://youtu.be/tGPF2nw5Exc?t=4379) Shannon 找受試者（講者說「我想是他太太」）看一段英文、猜下一個字母，用猜對的情形估計英文的熵，假設人是完美預測者，得到 **1.3**。比 4 階模型好很多，因為前一個字、前一句話都提供大量資訊 [▶ 1:13:33](https://youtu.be/tGPF2nw5Exc?t=4413)。

【口頭】[▶ 1:13:33](https://youtu.be/tGPF2nw5Exc?t=4413) 現在 LLM 已經打敗人類，最新模型的位元率比這還低（在特定實驗方式下），下一講會看。

---

## 13. 熵率是壓縮的極限

[▶ 1:14:15](https://youtu.be/tGPF2nw5Exc?t=4455)

- $k$ 階 Markov 來源：最好的壓縮是 $H(U_{k+1}\mid U_k,\dots,U_1)$ 位元／符號。
- 一般平穩來源：**熵率是能期望的最好壓縮**。

[▶ 1:14:52](https://youtu.be/tGPF2nw5Exc?t=4492) 和第 5 講的 AEP 一樣，有 **Shannon–McMillan–Breiman 定理**：在一些技術條件（遍歷性，ergodicity）下

$$-\frac1n\log_2P(U_1,\dots,U_n)\to H(\mathbf U)\quad\text{幾乎必然},$$

也就是 $P(U_1,\dots,U_n)\approx2^{-nH(\mathbf U)}$：把 AEP 的熵換成熵率 [▶ 1:14:52](https://youtu.be/tGPF2nw5Exc?t=4492)。所以這些量是壓縮能做到的極限。

【課本補充】§16.8（書頁 644–）就是這個定理（又叫一般 AEP）的證明。

[▶ 1:15:27](https://youtu.be/tGPF2nw5Exc?t=4527) 下一講：怎麼**達到**這個條件熵、怎麼處理相依的來源。先從 1 階開始，再 $k$ 階，再任意平穩來源，而且會用**算術編碼** [▶ 1:16:04](https://youtu.be/tGPF2nw5Exc?t=4564)。

【投影片補充】`L8.pdf` p.49–54 是下一講的預告：已知 1 階 Markov 來源時，(1) 用 Huffman 編長度 $n$ 的區塊（區塊大、複雜，而且對非 iid 來源逐符號編本來就次佳）；(2) 用算術編碼，每一步依 $P(\cdot\mid u_{i-1})$ 切區間，區間長度 $=P(u_1)P(u_2\mid u_1)\cdots P(u_n\mid u_{n-1})$，期望每符號位元數 $\approx\frac1nH(U_1)+\frac{n-1}nH(U_2\mid U_1)\to H(U_2\mid U_1)$。

---

## 14. 一頁速查表

### 過程

| 名稱 | 條件 |
|---|---|
| 隨機過程 | 任意相依，要給每個 $n$ 的聯合分布 |
| 平穩 | $P(U_1^n)=P(U_{l+1}^{l+n})$；平均、熵不隨時間變；iid ⇒ 平穩 |
| Markov（1 階） | $P(U_n\mid U^{n-1})=P(U_n\mid U_{n-1})$；$U_2$ 和 $U_1$ 同分布 ⇒ 平穩 |
| $k$ 階 Markov | $P(U_n\mid U^{n-1})=P(U_n\mid U_{n-k}^{n-1})$；iid = 0 階 |

### 條件熵

$$H(U\mid V)=\mathbb{E}\log\frac1{P(U\mid V)}=\sum_vP(v)H(U\mid V=v)$$

| 性質 | 式子 | 關鍵一步 |
|---|---|---|
| 條件降低熵 | $H(U\mid V)\le H(U)$ | 差 $=D(P_{UV}\|P_UP_V)\ge0$ |
| 鏈鎖律 | $H(U,V)=H(U)+H(V\mid U)$ | $\log\frac1{P(u,v)}=\log\frac1{P(u)}+\log\frac1{P(v\mid u)}$ |
| 次可加 | $H(U,V)\le H(U)+H(V)$ | 前兩條合起來 |

注意：$H(U\mid V=v)$ 可以 $>H(U)$，只有平均才 $\le$。

### 熵率

$$H(\mathbf U)=\lim_n H(U_{n+1}\mid U^n)=\lim_n\tfrac1nH(U^n)$$

| 來源 | 熵率 |
|---|---|
| iid | $H(U_1)$ |
| $k$ 階 Markov | $H(U_{k+1}\mid U^k)$ |
| 例 $U_{i+1}=U_i+Z_i\ \mathrm{mod}\ 3$ | 1 位元（邊際熵 1.58） |
| 英文 | 4.76 → 4.03 → 2.8 → 人類 1.3 |

- Shannon–McMillan–Breiman：$P(U^n)\approx2^{-nH(\mathbf U)}$ ⇒ 熵率是平穩來源的壓縮極限。

### 實用技巧

- 差分（delta coding）：Markov 例子差分後變 iid；公車時間差分後變平穩；`1,2,3,…` 差分後很好壓。

---

## 15. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 算術編碼每步換條件機率 ⇒ 達到條件熵 | 第 9 集 context-based 算術編碼 |
| 用預測器（甚至 LLM）估計 $P(U_n\mid\text{過去})$ | 第 9 集 LLM 壓縮 |
| 不知道分布、通用壓縮 | 第 10 集 LZ77 |
| 差分等前處理、為什麼 gzip 比熵小 | 第 10 集實務建議 |
| 互資訊 $I(U;V)=H(U)-H(U\mid V)$ | 第 12 集 |
| 相鄰像素、相鄰畫面相關 | 第 13–18 集（轉換編碼、影像、影片） |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **真實資料不是 iid（Q 後面幾乎總是 U），所以 gzip 能壓到比逐字母熵還小。條件熵 $H(U\mid V)$ 是知道 $V$ 後 $U$ 剩下的不確定性，平均而言條件只會降低熵，且 $H(U,V)=H(U)+H(V\mid U)$。平穩過程的極限是熵率 $\lim H(U_{n+1}\mid U^n)$：iid 時就是熵，$k$ 階 Markov 時是 $H(U_{k+1}\mid U^k)$；英文從 iid 的 4.76 位元降到人類預測的 1.3 位元。差分這類簡單轉換常能把相依或非平穩的資料變得好壓。**

---

*筆記依據 Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 8 錄影逐字稿（人工字幕，1:16:25）、投影片 L8 與 Cover & Thomas《Elements of Information Theory》2nd ed. §2.2、§2.6、§4.1–4.2、§16.8 整理。*
