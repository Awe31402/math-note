---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 7
lecture: Lecture 7
date: 2023-10-18
video: https://youtu.be/5Hp4bnvSjng
notes: 投影片 L7.pdf、L7_ann.pdf（打字版，去年 Kedar 的投影片）；課本沒有 ANS
---

# 第 7 集 · Lecture 7：非對稱記數系統（ANS） [▶ 影片](https://youtu.be/5Hp4bnvSjng)

← 上一集：[06-arithmetic-coding](06-arithmetic-coding.md) ｜ [總目錄](README.md) ｜ 下一集：[08-conditional-entropy](08-conditional-entropy.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 7 集
> **講者**：Pulkit Tandon（投影片大多是去年 Kedar 做的；Shubham 中途補充）
> **來源**：YouTube 錄影逐字稿（1:20:03，人工字幕 en-US）＋ 投影片 `L7.pdf`、`L7_ann.pdf`。Cover & Thomas 沒有 ANS（2006 年出版，ANS 是之後才發展的），本集只靠逐字稿和投影片。
> **標記說明**：
> - `【口頭】` 講者口頭補充，投影片沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 小考檢討](#1-小考檢討)
- [2. 回顧：算術編碼很好，但不夠快](#2-回顧算術編碼很好但不夠快)
- [3. 從十進位開始：對稱記數系統](#3-從十進位開始對稱記數系統)
- [4. 非均勻分布：狀態要乘 $1/p(s)$](#4-非均勻分布狀態要乘-1ps)
- [5. rANS 的編碼步驟](#5-rans-的編碼步驟)
- [6. rANS 的解碼步驟](#6-rans-的解碼步驟)
- [7. 壓縮率：為什麼接近熵](#7-壓縮率為什麼接近熵)
- [8. 另一個角度：bits-back](#8-另一個角度bits-back)
- [9. rANS 的性質](#9-rans-的性質)
- [10. 串流 rANS：狀態會溢位](#10-串流-rans狀態會溢位)
- [11. tANS：用查表加速](#11-tans用查表加速)
- [12. 無損壓縮前半段的總結](#12-無損壓縮前半段的總結)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/5Hp4bnvSjng?t=5) 主題：**非對稱記數系統**（Asymmetric Numeral Systems, ANS）。兩個代表：

- **rANS**（range ANS）：可以直接取代算術編碼，但更快。
- **tANS**（table ANS）：可以直接取代 Huffman，速度差不多，壓縮更好。

第 1 集提過「$2\times10+2=22$ 這種記數系統和壓縮有什麼關係」，就是這一集。

---

## 1. 小考檢討

### 1.1 AB 和 BA

[▶ 00:05](https://youtu.be/5Hp4bnvSjng?t=5) $X\sim\mathrm{Ber}(p)$，$P(A)=p$、$P(B)=1-p$。用算術編碼編 AB 和 BA。

| 題 | 問題 | 答案 |
|---|---|---|
| 1.1 | 兩者碼長一樣嗎？ | **一樣** [▶ 00:42](https://youtu.be/5Hp4bnvSjng?t=42)：$P(AB)=P(BA)=p(1-p)$，碼長只看區間長度，也就是機率 |
| 1.2 | 輸出同一個碼字嗎？ | **不一樣** [▶ 02:29](https://youtu.be/5Hp4bnvSjng?t=149)：在 $[0,1)$ 上 AB 和 BA 落在不同區域 |

【口頭】[▶ 01:20](https://youtu.be/5Hp4bnvSjng?t=80) Shubham 補充：實際的算術編碼器碼長只保證上界，兩者可能差到 2 位元，所以題目要求假設「理想化」的算術編碼器。

### 1.2 算術解碼

[▶ 03:10](https://youtu.be/5Hp4bnvSjng?t=190)（`L7.pdf` 小考頁）$P(A)=0.5$、$P(B)=0.25$、$P(C)=0.25$，收到位元串 `100111`、長度 3。

- `100111` $=0.100111_2=0.609375$ [▶ 03:43](https://youtu.be/5Hp4bnvSjng?t=223)。
- A $[0,0.5)$、B $[0.5,0.75)$、C $[0.75,1)$：0.609375 落在 B。放大再切，重複 [▶ 04:25](https://youtu.be/5Hp4bnvSjng?t=265)。
- 解出 **BAC**。

> 以下**不是逐字稿內容**，是把後兩步算出來：B $=[0.5,0.75)$ 切成 BA $[0.5,0.625)$、BB $[0.625,0.6875)$、BC $[0.6875,0.75)$；0.609375 在 BA。BA 切成 BAA $[0.5,0.5625)$、BAB $[0.5625,0.59375)$、BAC $[0.59375,0.625)$；0.609375 在 BAC。

---

## 2. 回顧：算術編碼很好，但不夠快

[▶ 04:25](https://youtu.be/5Hp4bnvSjng?t=265) 算術編碼：

- 對任何分布 $P$ 都達到最佳壓縮。
- 讓**模型**和**熵編碼**分開 [▶ 05:04](https://youtu.be/5Hp4bnvSjng?t=304)：模型想辦法算好機率，熵編碼保證碼長接近 $\log\frac1p$。Huffman、Shannon 碼做不到這點。
- 分布可以變動，所以可以做**自適應**演算法（兩講之後）[▶ 05:47](https://youtu.be/5Hp4bnvSjng?t=347)。
- 各種變體大多差在怎麼處理邊界、怎麼有效率地實作；到處都在用。

[▶ 06:27](https://youtu.be/5Hp4bnvSjng?t=387) 那無損壓縮解決了嗎？**沒有**。

【投影片補充】速度表（Charles Bloom 的部落格）：

| 編碼器 | 編碼速度 | 解碼速度 | 壓縮（位元／符號，越小越好） |
|---|---|---|---|
| Huffman | 252 MB/s | 300 MB/s | 1.66 |
| 算術編碼 | 120 MB/s | 69 MB/s | 1.24 |
| rANS | 76 MB/s | 140 MB/s | 1.24 |
| tANS | 163 MB/s | 284 MB/s | 1.25 |

[▶ 06:27](https://youtu.be/5Hp4bnvSjng?t=387) 算術編碼壓得比 Huffman 好（等於整份資料是一個區塊），但編碼、解碼都慢很多。看應用，可能要拿壓縮換速度 [▶ 06:59](https://youtu.be/5Hp4bnvSjng?t=419)。

[▶ 07:42](https://youtu.be/5Hp4bnvSjng?t=462) rANS、tANS 壓縮和算術編碼差不多，但解碼快很多。tANS 解碼速度接近 Huffman、編碼比算術編碼快，壓縮只比算術編碼差一點 [▶ 07:42](https://youtu.be/5Hp4bnvSjng?t=462)。

[▶ 08:16](https://youtu.be/5Hp4bnvSjng?t=496) ANS 約 2014 年左右被發現（講者說「I think」）。現在很多實用壓縮器都用某種 ANS。ANS 是**一族**壓縮器，rANS（r = range）和 tANS（t = table）是兩個極端 [▶ 08:57](https://youtu.be/5Hp4bnvSjng?t=537)：

- rANS：取代算術編碼，更快。在乎壓縮率時用。
- tANS：取代 Huffman，幾乎一樣快，壓縮更好。

---

## 3. 從十進位開始：對稱記數系統

### 3.1 把一串數字變成一個數【課堂討論】

[▶ 09:34](https://youtu.be/5Hp4bnvSjng?t=574) 輸入是 0–9 的數字串，例如 `3, 2, 4, 1, 5` [▶ 10:14](https://youtu.be/5Hp4bnvSjng?t=614)。能不能用**一個數** $x$ 表示它？

學生答：當成一個數的各位數字，**32415**，用十進位 [▶ 10:52](https://youtu.be/5Hp4bnvSjng?t=652)。

### 3.2 串流編碼

[▶ 11:31](https://youtu.be/5Hp4bnvSjng?t=691) 想成資料一個一個來：

```
x = 0           # 初始狀態
x = x*10 + 3    # 3
x = x*10 + 2    # 32
x = x*10 + 4    # 324
x = x*10 + 1    # 3241
x = x*10 + 5    # 32415  ← 最終狀態
```

[▶ 12:41](https://youtu.be/5Hp4bnvSjng?t=761) 只維護一個**狀態**（state）$x$：每來一個符號 $s$，就

$$x\leftarrow10\,x+s.$$

### 3.3 解碼【課堂討論】

[▶ 13:24](https://youtu.be/5Hp4bnvSjng?t=804) 朋友給你 32415，怎麼還原？學生答：除以 10 取餘數 [▶ 13:24](https://youtu.be/5Hp4bnvSjng?t=804)。

```
s, x = x % 10, x // 10    # 5, 3241
s, x = x % 10, x // 10    # 1, 324
...
```

- 餘數 → 符號；整數商 → **前一個狀態** [▶ 14:03](https://youtu.be/5Hp4bnvSjng?t=843)。
- 符號會**倒著**出來 [▶ 14:38](https://youtu.be/5Hp4bnvSjng?t=878)：從 32415 依序得到 5、1、4、2、3。
- 怎麼知道何時停：知道符號數 $n$，或回到初始狀態 0 [▶ 15:15](https://youtu.be/5Hp4bnvSjng?t=915)。

> ⚠️ 逐字稿缺字 [▶ 13:24](https://youtu.be/5Hp4bnvSjng?t=804)：講者把最終狀態念成「32145」，投影片程式也寫 `x = 32145`（解出 5、4、1、2、3，反轉是 3、2、1、4、5）；但編碼範例的最終狀態是 **32415**（解出 5、1、4、2、3，反轉是 3、2、4、1、5）。`L7.pdf` 的狀態序列也寫成 0 → 3 → 32 → 321 → 3214 → 32145。兩處都是把 32415 打成 32145，不影響概念。

### 3.4 編碼和解碼互為反函數

[▶ 15:50](https://youtu.be/5Hp4bnvSjng?t=950)

```
encode_step(x_prev, s):  return x_prev*10 + s
decode_step(x):          return (x % 10, x // 10)   # (s, x_prev)
```

[▶ 16:30](https://youtu.be/5Hp4bnvSjng?t=990) 解碼一步一步回到**完全一樣的狀態**，只是順序相反。這就是**對稱記數系統**（symmetric numeral system）的編碼器。

### 3.5 變成位元

[▶ 17:40](https://youtu.be/5Hp4bnvSjng?t=1060) 最後用 $\lceil\log_2(x+1)\rceil$ 位元把最終狀態 $x$ 以二進位送出。【投影片補充】例：$32415$ 的二進位要 15 位元。[▶ 18:13](https://youtu.be/5Hp4bnvSjng?t=1093) 解碼：先把位元轉回整數，再做 $n$ 次 `decode_step`，最後**把符號反轉** [▶ 18:48](https://youtu.be/5Hp4bnvSjng?t=1128)。

### 3.6 壓縮率是多少？【課堂討論】

[▶ 19:26](https://youtu.be/5Hp4bnvSjng?t=1166) 提示：看編碼步驟，$s$ 一直在 0–9，$x$ 呢？學生答：一直變大，每次約 **10 倍** [▶ 20:39](https://youtu.be/5Hp4bnvSjng?t=1239)。

[▶ 20:39](https://youtu.be/5Hp4bnvSjng?t=1239) $x$ 很快就遠大於 $s$，所以每個符號的代價就是「數變成 10 倍」，約 $\log_210$ 位元 [▶ 21:19](https://youtu.be/5Hp4bnvSjng?t=1279)。

> **若 0–9 均勻分布（各 0.1），這個壓縮器是最佳的**：每個符號都付 $\log_210$ 位元，正好是熵 [▶ 21:52](https://youtu.be/5Hp4bnvSjng?t=1312)。10 也可以換成任何進位。

---

## 4. 非均勻分布：狀態要乘 $1/p(s)$

【課堂討論】[▶ 23:17](https://youtu.be/5Hp4bnvSjng?t=1397) 如果符號不是均勻分布，怎麼辦？為什麼剛剛是最佳的？

[▶ 23:55](https://youtu.be/5Hp4bnvSjng?t=1435) 因為不管符號是什麼，狀態都乘 10，每次多付 $\log_210$ 位元。課堂一直遵守的經驗法則：碼長約 $\log_2\frac1p$ 就做到了 [▶ 24:33](https://youtu.be/5Hp4bnvSjng?t=1473)。

[▶ 25:15](https://youtu.be/5Hp4bnvSjng?t=1515) 有學生猜：乘一個比較小的數。講者：10 不是隨便選的，它是 $\frac1p$。

> **想法**：不要 $x\approx10\,x_{\text{prev}}$，而要 $x\approx\dfrac{1}{p(s)}\,x_{\text{prev}}$。[▶ 26:00](https://youtu.be/5Hp4bnvSjng?t=1560)

這樣編碼符號 $s$ 時，就只多付約 $\log_2\frac1{p(s)}$ 位元，這是最好的 [▶ 26:37](https://youtu.be/5Hp4bnvSjng?t=1597)。這就是 ANS 的基本想法。**非對稱**的意思：狀態乘的倍數**依符號而不同** [▶ 54:08](https://youtu.be/5Hp4bnvSjng?t=3248)。

---

## 5. rANS 的編碼步驟

### 5.1 記號：整數頻率

[▶ 27:08](https://youtu.be/5Hp4bnvSjng?t=1628) 把機率寫成整數頻率除以 $M$：

$$p(s)=\frac{\mathrm{freq}[s]}{M}.$$

例 [▶ 27:43](https://youtu.be/5Hp4bnvSjng?t=1663)：字母集 $\{0,1,2\}$，機率 $\left(\frac38,\frac38,\frac28\right)$ → $\mathrm{freq}=[3,3,2]$、$M=8$。

**累積頻率** [▶ 28:18](https://youtu.be/5Hp4bnvSjng?t=1698)：$\mathrm{cumul}[s]=\sum_{s'<s}\mathrm{freq}[s']$。例：$\mathrm{cumul}=[0,3,6]$。

### 5.2 編碼步驟

[▶ 29:28](https://youtu.be/5Hp4bnvSjng?t=1768) 整體架構和對稱版一樣：從初始狀態開始，每個符號做一次 `base_encode_step`，最後輸出二進位。只要換掉 `10*x + s` 那一步。

【課堂討論】[▶ 30:06](https://youtu.be/5Hp4bnvSjng?t=1806) 學生提議：把 $x$ 除以 $p(s)$，取個整數之類的，但不確定怎麼解碼。講者：很好，那個問題等一下解決 [▶ 30:43](https://youtu.be/5Hp4bnvSjng?t=1843)。

> **rANS 編碼步驟**：
> $$x=\left\lfloor\frac{x_{\text{prev}}}{\mathrm{freq}[s]}\right\rfloor\cdot M+\mathrm{cumul}[s]+\left(x_{\text{prev}}\ \mathrm{mod}\ \mathrm{freq}[s]\right)$$

[▶ 30:43](https://youtu.be/5Hp4bnvSjng?t=1843) 看 $x_{\text{prev}}$ 的部分：除以 $\mathrm{freq}[s]$ 再乘 $M$，就是學生說的「除以機率」。所以符號 $s$ 進來時，狀態大約變成 $\frac1{p(s)}$ 倍 [▶ 31:26](https://youtu.be/5Hp4bnvSjng?t=1886)。

[▶ 31:58](https://youtu.be/5Hp4bnvSjng?t=1918) 和十進位比：`*10` 換成 $\lfloor\cdot/\mathrm{freq}[s]\rfloor\cdot M$，`+s` 換成 $\mathrm{cumul}[s]+(\cdot\ \mathrm{mod}\ \mathrm{freq}[s])$。

### 5.3 例子：編 `1, 0, 2, 1`

[▶ 32:43](https://youtu.be/5Hp4bnvSjng?t=1963)（$\mathrm{freq}=[3,3,2]$、$M=8$、$\mathrm{cumul}=[0,3,6]$）

| 步 | 符號 | 計算 | 新狀態 |
|---|---|---|---|
| 0 | — | — | 0 |
| 1 | 1 | $\lfloor0/3\rfloor\cdot8+3+(0\ \mathrm{mod}\ 3)$ | 3 [▶ 34:06](https://youtu.be/5Hp4bnvSjng?t=2046) |
| 2 | 0 | $\lfloor3/3\rfloor\cdot8+0+(3\ \mathrm{mod}\ 3)$ | 8 [▶ 34:42](https://youtu.be/5Hp4bnvSjng?t=2082) |
| 3 | 2 | $\lfloor8/2\rfloor\cdot8+6+(8\ \mathrm{mod}\ 2)$ | 38 |
| 4 | 1 | $\lfloor38/3\rfloor\cdot8+3+(38\ \mathrm{mod}\ 3)$ | 101 [▶ 35:16](https://youtu.be/5Hp4bnvSjng?t=2116) |

（第 3、4 步依投影片 `L7.pdf`。）最終狀態 101 = `1100101`。

### 5.4 均勻分布時退化成十進位

[▶ 35:51](https://youtu.be/5Hp4bnvSjng?t=2151) 講者留作回家算：$\{0,\dots,9\}$、$\mathrm{freq}[s]=1$、$M=10$。[▶ 36:38](https://youtu.be/5Hp4bnvSjng?t=2198) 答案：$\lfloor x/1\rfloor\cdot10+s+(x\ \mathrm{mod}\ 1)=10x+s$，回到一開始的式子 [▶ 37:12](https://youtu.be/5Hp4bnvSjng?t=2232)。（$\mathrm{cumul}[s]=s$、$x\ \mathrm{mod}\ 1=0$。）

---

## 6. rANS 的解碼步驟

### 6.1 block ID 和 slot

[▶ 37:47](https://youtu.be/5Hp4bnvSjng?t=2267) 把編碼步驟拆成兩塊：

$$x=\underbrace{\left\lfloor\frac{x_{\text{prev}}}{\mathrm{freq}[s]}\right\rfloor}_{\text{block\_id}}\cdot M+\underbrace{\mathrm{cumul}[s]+\left(x_{\text{prev}}\ \mathrm{mod}\ \mathrm{freq}[s]\right)}_{\text{slot}}.$$

格式和 `10*x + s` 一樣：$x=\text{block\_id}\cdot M+\text{slot}$ [▶ 38:20](https://youtu.be/5Hp4bnvSjng?t=2300)。

【課堂討論】[▶ 38:20](https://youtu.be/5Hp4bnvSjng?t=2300) slot 有什麼性質？學生答：在 $\mathrm{cumul}[s]$ 和 $\mathrm{cumul}[s+1]$ 之間 [▶ 38:52](https://youtu.be/5Hp4bnvSjng?t=2332)。

[▶ 38:52](https://youtu.be/5Hp4bnvSjng?t=2332) 因為 $0\le x_{\text{prev}}\ \mathrm{mod}\ \mathrm{freq}[s]<\mathrm{freq}[s]$：

$$\mathrm{cumul}[s]\le\text{slot}<\mathrm{cumul}[s]+\mathrm{freq}[s]=\mathrm{cumul}[s+1]\le M.$$

所以更鬆地 $0\le\text{slot}<M$ [▶ 39:31](https://youtu.be/5Hp4bnvSjng?t=2371)。

### 6.2 步驟一：取出 block ID 和 slot

【課堂討論】[▶ 40:13](https://youtu.be/5Hp4bnvSjng?t=2413) 知道 $x=\text{block\_id}\cdot M+\text{slot}$、$0\le\text{slot}<M$，怎麼分開？學生答：除以 $M$ [▶ 41:13](https://youtu.be/5Hp4bnvSjng?t=2473)。

$$\text{block\_id}=\lfloor x/M\rfloor,\qquad\text{slot}=x\ \mathrm{mod}\ M.$$

### 6.3 步驟二：找出符號

[▶ 42:34](https://youtu.be/5Hp4bnvSjng?t=2554) 提示：slot 不只在 $[0,M)$，還在 $[\mathrm{cumul}[s],\mathrm{cumul}[s+1])$。

【課堂討論】[▶ 43:44](https://youtu.be/5Hp4bnvSjng?t=2624) 學生答：找最後一個 $\mathrm{cumul}[s]\le\text{slot}$ 的 $s$ [▶ 43:44](https://youtu.be/5Hp4bnvSjng?t=2624)。[▶ 44:31](https://youtu.be/5Hp4bnvSjng?t=2671) 講者：$\mathrm{cumul}$ 是**遞增**陣列，每個符號占一段，只要找 slot 落在哪一段。因為陣列已排序，可以用**二分搜尋**（左偏）[▶ 45:41](https://youtu.be/5Hp4bnvSjng?t=2741)，而且答案唯一 [▶ 46:17](https://youtu.be/5Hp4bnvSjng?t=2777)。

### 6.4 步驟三：還原前一個狀態

[▶ 46:52](https://youtu.be/5Hp4bnvSjng?t=2812) 還不夠，還要前一個狀態。現在知道：$s$、$\text{block\_id}=\lfloor x_{\text{prev}}/\mathrm{freq}[s]\rfloor$、$\text{slot}=\mathrm{cumul}[s]+(x_{\text{prev}}\ \mathrm{mod}\ \mathrm{freq}[s])$。

【課堂討論】[▶ 47:24](https://youtu.be/5Hp4bnvSjng?t=2844) 學生：block ID 乘 $\mathrm{freq}[s]$，再把餘數加回來（餘數 = slot − $\mathrm{cumul}[s]$）[▶ 47:58](https://youtu.be/5Hp4bnvSjng?t=2878)。講者：對，就是重排原式 [▶ 48:48](https://youtu.be/5Hp4bnvSjng?t=2928)：

$$x_{\text{prev}}=\text{block\_id}\cdot\mathrm{freq}[s]+\text{slot}-\mathrm{cumul}[s].$$

（整數除法的商乘除數再加餘數，就是被除數。）

> **rANS 解碼步驟**：
> ```
> block_id, slot = x // M, x % M                 # 一
> s = 使 cumul[s] <= slot < cumul[s+1] 的符號     # 二（二分搜尋）
> x_prev = block_id * freq[s] + slot - cumul[s]  # 三
> return s, x_prev
> ```

### 6.5 例子：從 101 解回去

[▶ 50:03](https://youtu.be/5Hp4bnvSjng?t=3003) $x=101$ [▶ 50:39](https://youtu.be/5Hp4bnvSjng?t=3039)：

1. $\text{block\_id}=\lfloor101/8\rfloor=12$、$\text{slot}=101\ \mathrm{mod}\ 8=5$ [▶ 51:16](https://youtu.be/5Hp4bnvSjng?t=3076)。
2. $\mathrm{cumul}=[0,3,6]$：5 在 3 和 6 之間 → $s=1$，$\mathrm{cumul}[s]=3$ [▶ 51:53](https://youtu.be/5Hp4bnvSjng?t=3113)。
3. $x_{\text{prev}}=12\times3+(5-3)=38$ [▶ 52:38](https://youtu.be/5Hp4bnvSjng?t=3158)。

輸出 $s=1$、前一個狀態 38，正好是編碼時第 3 步的狀態 [▶ 53:17](https://youtu.be/5Hp4bnvSjng?t=3197)。講者請大家回家把剩下的做完。

> 以下**不是逐字稿內容**，是照同樣步驟做完：
>
> | $x$ | block_id | slot | $s$ | $x_{\text{prev}}$ |
> |---|---|---|---|---|
> | 101 | 12 | 5 | 1 | $12\cdot3+2=38$ |
> | 38 | 4 | 6 | 2 | $4\cdot2+0=8$ |
> | 8 | 1 | 0 | 0 | $1\cdot3+0=3$ |
> | 3 | 0 | 3 | 1 | $0\cdot3+0=0$ |
>
> 解出 1、2、0、1，反轉得 `1, 0, 2, 1`，狀態回到 0。

【Q&A】[▶ 54:08](https://youtu.be/5Hp4bnvSjng?t=3248) 學生問「非對稱」指的是什麼（字幕不全）。講者：不是指編碼、解碼的流程，而是**記數系統**：對稱的系統不管什麼符號都乘 10；這裡乘的倍數依進來的符號而定 [▶ 54:44](https://youtu.be/5Hp4bnvSjng?t=3284)。**而且一定要保證前進、後退時重現完全一樣的狀態**，這才保證無損。

【口頭】[▶ 55:29](https://youtu.be/5Hp4bnvSjng?t=3329) Kedar 寫過一篇 ANS 的部落格，附互動工具：輸入符號計數和字串，可以看狀態怎麼變。講者現場輸入 `1,0,2,1`，得到一樣的狀態 [▶ 56:01](https://youtu.be/5Hp4bnvSjng?t=3361)。建議還是先手算，再用工具對答案。

---

## 7. 壓縮率：為什麼接近熵

[▶ 58:54](https://youtu.be/5Hp4bnvSjng?t=3534) 狀態每編一個符號 $s$，大約乘 $\frac1{p(s)}$。最終狀態可用約 $\log_2x_{\text{final}}$ 位元表示。

【課堂討論】[▶ 59:31](https://youtu.be/5Hp4bnvSjng?t=3571) 編 $s_1,\dots,s_n$ 大約要幾位元？學生答：$\log_2\frac1{p(s)}$ 加起來 [▶ 1:00:12](https://youtu.be/5Hp4bnvSjng?t=3612)。

$$x_{\text{final}}\approx\frac1{p(s_1)}\cdot\frac1{p(s_2)}\cdots\frac1{p(s_n)}=\frac1{p(s^n)},\qquad\text{碼長}\approx\log_2\frac1{p(s^n)}.$$

[▶ 1:00:57](https://youtu.be/5Hp4bnvSjng?t=3657) 呼應經驗法則：非常接近熵。

【口頭】[▶ 1:00:57](https://youtu.be/5Hp4bnvSjng?t=3657) 這是很粗略的論證。算術編碼有「多 2 位元」、Huffman 有「多 1 位元」這種嚴格界；ANS 要做出正式的界**不簡單**，有興趣可以私下討論 [▶ 1:01:41](https://youtu.be/5Hp4bnvSjng?t=3701)。要帶走的是：直覺上它接近最佳，和算術編碼差不多。

> 以下**不是逐字稿內容**，是把「約乘 $\frac1{p(s)}$」寫精確一點：令 $q=\lfloor x_{\text{prev}}/f\rfloor$、$r=x_{\text{prev}}\ \mathrm{mod}\ f$（$f=\mathrm{freq}[s]$），則 $x=qM+\mathrm{cumul}[s]+r$。因為 $x_{\text{prev}}=qf+r$，$q=\frac{x_{\text{prev}}-r}{f}$，所以 $x=\frac{M}{f}(x_{\text{prev}}-r)+\mathrm{cumul}[s]+r$。$x_{\text{prev}}$ 很大時，$r<f$、$\mathrm{cumul}[s]<M$ 都是小項，$x\approx\frac{M}{f}x_{\text{prev}}=\frac{x_{\text{prev}}}{p(s)}$。

---

## 8. 另一個角度：bits-back

[▶ 1:02:12](https://youtu.be/5Hp4bnvSjng?t=3732) 很多人第一次看到 rANS 的式子都會問：那個 $\mathrm{cumul}[s]+$ 取餘數是哪來的？解碼又怎麼這麼剛好？[▶ 1:02:47](https://youtu.be/5Hp4bnvSjng?t=3767) 歷史上也差不多：Duda 想出這個方法，大家花了很久才真正理解。

[▶ 1:02:47](https://youtu.be/5Hp4bnvSjng?t=3767) 一個可愛的理解方式是 **bits-back coding**（本集不細講）[▶ 1:03:21](https://youtu.be/5Hp4bnvSjng?t=3801)。它和這個恆等式有關（$Z$ 是任意隨機變數）：

$$H(X)=H(X,Z)-H(Z\mid X).$$

[▶ 1:03:54](https://youtu.be/5Hp4bnvSjng?t=3834) 想法：用一組編碼器／解碼器處理 $X$ 和 $Z$ 的聯合分布，再用另一組處理 $Z$ 在 $X$ 條件下的分布；那個**減號**意思是先編進去、再「把一些位元還回來」（bits back）[▶ 1:04:26](https://youtu.be/5Hp4bnvSjng?t=3866)。

[▶ 1:04:26](https://youtu.be/5Hp4bnvSjng?t=3866) 作業 2 第 4 題會做。接下來幾講會講條件熵、條件分布（因為不再假設獨立），到時再回頭看會更清楚 [▶ 1:05:19](https://youtu.be/5Hp4bnvSjng?t=3919)。

> ⚠️ 逐字稿缺字 [▶ 1:02:47](https://youtu.be/5Hp4bnvSjng?t=3767)：字幕把人名標成「[? Duda, ?]」（字幕員不確定）。下一講（第 8 集）投影片 `L8.pdf` 寫明 ANS 的發明者是 **Jarek Duda**（「Paper by inventor (Jarek Duda)」），Shubham 在第 8 集口頭也這樣說。

---

## 9. rANS 的性質

[▶ 1:05:19](https://youtu.be/5Hp4bnvSjng?t=3919)

1. **壓縮率接近最佳**，和算術編碼很像。
2. **解碼順序相反** [▶ 1:05:54](https://youtu.be/5Hp4bnvSjng?t=3954)：編碼是串流的，解碼卻倒著出符號，對低延遲或高吞吐的應用可能是問題；實務上有繞過的辦法。
3. **編碼、解碼更簡單** [▶ 1:05:54](https://youtu.be/5Hp4bnvSjng?t=3954)：算術編碼到處是浮點運算；rANS 的運算可以做得很有效率 [▶ 1:06:39](https://youtu.be/5Hp4bnvSjng?t=3999)：
   - 整數除以 $\mathrm{freq}[s]$：可以預先算 $\frac1{\mathrm{freq}[s]}$ 存起來。
   - 選 $M$ 為 2 的冪：乘 $M$ 就是左移，硬體上極快 [▶ 1:07:14](https://youtu.be/5Hp4bnvSjng?t=4034)。

---

## 10. 串流 rANS：狀態會溢位

### 10.1 問題【課堂討論】

[▶ 1:07:14](https://youtu.be/5Hp4bnvSjng?t=4034) 實務上有什麼問題？一位學生說要找一個好用的 $M$（大概是做作業 1 的感想）。[▶ 1:07:49](https://youtu.be/5Hp4bnvSjng?t=4069) 講者：那確實要處理，但不是根本問題，$M$ 取夠大就行。

**根本問題** [▶ 1:08:28](https://youtu.be/5Hp4bnvSjng?t=4108)：狀態**一直變大**，從不縮小。大約 20–40 個符號之後，不管怎樣都會**溢位**。這和算術編碼的區間越乘越小是平行的問題 [▶ 1:09:01](https://youtu.be/5Hp4bnvSjng?t=4141)。

### 10.2 解法：把狀態限制在 $[L,H]$

[▶ 1:09:01](https://youtu.be/5Hp4bnvSjng?t=4141) 不能溢位就重來：那會失去「整份資料是一個區塊」的好處，而且狀態要夠大才能讓碼長接近 $\log\frac1p$ [▶ 1:09:36](https://youtu.be/5Hp4bnvSjng?t=4176)。

做法 [▶ 1:09:36](https://youtu.be/5Hp4bnvSjng?t=4176)：讓狀態一直留在區間 $[L,H]$ 裡。

- 呼叫 `base_encode_step` 之前，先呼叫 **`shrink_state`**，把狀態縮小，使得編碼後的狀態落在 $[L,H]$ [▶ 1:10:20](https://youtu.be/5Hp4bnvSjng?t=4220)。
- 縮小會丟資訊，所以 `shrink_state` 要**輸出一些位元**。

**`shrink_state` 的做法** [▶ 1:10:54](https://youtu.be/5Hp4bnvSjng?t=4254)：每次除以 2，把最低位元輸出。例（`L7.pdf`）：

| $x_{\text{shrunk}}$ | out_bits |
|---|---|
| $22=10110_2$ | `""` |
| $11=1011_2$ | `"0"` |
| $5=101_2$ | `"10"` |

```
shrink_state(x, s):
    out_bits = ""
    while base_encode_step(x, s) 不在 [L, H]:
        out_bits = (x % 2) + out_bits    # 輸出最低位元
        x = x // 2
    return x, out_bits
```

[▶ 1:12:04](https://youtu.be/5Hp4bnvSjng?t=4324) 關鍵差別：**每一步可能就輸出一些位元**，不是等到最後才輸出整個狀態。

### 10.3 $[L,H]$ 怎麼選

[▶ 1:12:04](https://youtu.be/5Hp4bnvSjng?t=4324) 要確保縮小狀態時有**唯一**性：不管從什麼狀態開始，縮小後都正好有一個（且只有一個）落在正確區間 [▶ 1:12:40](https://youtu.be/5Hp4bnvSjng?t=4360)。原論文的選法：

$$[L,H]=[\,M\,t,\ 2Mt-1\,],\quad t\text{ 為任意正整數}.$$

【投影片補充】`L7.pdf` 的 `shrink_state` 實際寫成：縮小 $x$ 直到 $x\in[\mathrm{freq}[s]\,t,\ 2\,\mathrm{freq}[s]\,t-1]$，這樣編碼後的狀態就落在 $[Mt,2Mt-1]$。

> 以下**不是逐字稿內容**，是驗證這個選法：若 $x\in[ft,2ft-1]$（$f=\mathrm{freq}[s]$），則 $\lfloor x/f\rfloor\in[t,2t-1]$，編碼後 $x'=\lfloor x/f\rfloor M+\text{slot}$，$0\le\text{slot}<M$，所以 $x'\in[tM,(2t-1)M+M-1]=[Mt,2Mt-1]$。而且 $[ft,2ft-1]$ 正好是「除以 2 一次就縮一半」的一個倍頻區間，所以從任何 $x\ge ft$ 一直除以 2，恰好會有一次落進去。

[▶ 1:13:16](https://youtu.be/5Hp4bnvSjng?t=4396) 細節在講義，課堂不講。

### 10.4 解碼端：擴張狀態

[▶ 1:13:52](https://youtu.be/5Hp4bnvSjng?t=4432) 解碼時要做相反的事：`base_decode_step` 得到符號和縮小過的狀態，再用串流裡的位元**擴張狀態**（expand state）回去 [▶ 1:13:52](https://youtu.be/5Hp4bnvSjng?t=4432)。兩者合起來就是完整的串流編碼器和解碼器。

[▶ 1:14:30](https://youtu.be/5Hp4bnvSjng?t=4470) 實務上：$M$ 取 2 的冪；$t$ 盡量大；不要一次輸出一個位元，而是一次一個位元組。SCL 裡有 rANS 的實作。

---

## 11. tANS：用查表加速

[▶ 1:15:05](https://youtu.be/5Hp4bnvSjng?t=4505) 本集沒細講 tANS，只講基本想法：**還能快取什麼？**

【課堂討論】[▶ 1:15:05](https://youtu.be/5Hp4bnvSjng?t=4505) 作業 1 學到什麼？一再出現的主題：**樹很慢，因為要做決定** [▶ 1:15:52](https://youtu.be/5Hp4bnvSjng?t=4552)。要加速，就做**查表**。這是寫程式非常好的經驗法則。

[▶ 1:15:52](https://youtu.be/5Hp4bnvSjng?t=4552) tANS 的根據：串流 rANS 的編碼步驟，狀態永遠在**同一個** $[L,H]$ 裡。所以可以**預先算好**「目前狀態 + 新符號 → 新狀態」的表，執行時根本不用算 [▶ 1:16:32](https://youtu.be/5Hp4bnvSjng?t=4592)。這就是 **table ANS**。

代價：壓縮率稍微差一點（因為快取、不做精確運算）；好處：查表很快 [▶ 1:16:32](https://youtu.be/5Hp4bnvSjng?t=4592)。

[▶ 1:17:09](https://youtu.be/5Hp4bnvSjng?t=4629) 想深入 tANS 看講義、SCL 原始碼，或找助教。rANS、tANS 的變體也可以是期末專題。

[▶ 1:17:46](https://youtu.be/5Hp4bnvSjng?t=4666) 再看一次速度表：rANS 壓縮和算術編碼很像（因為達到了經驗法則）；tANS 稍差（快取、近似）；但 tANS 解碼速度接近 Huffman，編碼至少有競爭力。

---

## 12. 無損壓縮前半段的總結

[▶ 1:18:24](https://youtu.be/5Hp4bnvSjng?t=4704) 這是一系列講次的最後一講：從簡單的 iid 例子開始，學會怎麼無損編碼、怎麼最佳地無損編碼；再學各種實用的無損編碼器：Huffman、Shannon、算術編碼、ANS。

[▶ 1:19:00](https://youtu.be/5Hp4bnvSjng?t=4740) 但一直有一個強假設：**iid**。真實資料高度相關：下一個符號和前一個不獨立，例如語言。接下來幾講講怎麼處理相關性、怎麼自適應、怎麼用 LLM 做出最先進的壓縮器 [▶ 1:19:00](https://youtu.be/5Hp4bnvSjng?t=4740)。

---

## 13. 一頁速查表

### 對稱記數系統（十進位）

| | 式子 |
|---|---|
| 編碼 | $x\leftarrow10x+s$ |
| 解碼 | $s=x\ \mathrm{mod}\ 10$，$x\leftarrow\lfloor x/10\rfloor$ |
| 代價 | 每符號 $\log_210$；均勻分布時最佳 |

### rANS

記號：$p(s)=\mathrm{freq}[s]/M$，$\mathrm{cumul}[s]=\sum_{s'<s}\mathrm{freq}[s']$。

| | 式子 |
|---|---|
| 編碼 | $x=\lfloor x_p/\mathrm{freq}[s]\rfloor\,M+\mathrm{cumul}[s]+(x_p\ \mathrm{mod}\ \mathrm{freq}[s])$ |
| 拆解 | $x=\text{block\_id}\cdot M+\text{slot}$，$\mathrm{cumul}[s]\le\text{slot}<\mathrm{cumul}[s+1]$ |
| 解碼 | $\text{block\_id}=\lfloor x/M\rfloor$，$\text{slot}=x\ \mathrm{mod}\ M$；二分搜尋找 $s$；$x_p=\text{block\_id}\cdot\mathrm{freq}[s]+\text{slot}-\mathrm{cumul}[s]$ |
| 代價 | $x\approx x_p/p(s)$ ⇒ 總長 $\approx\log_2\frac1{p(s^n)}$ |

- **關鍵一步**（解碼可行）：slot 夾在 $\mathrm{cumul}[s]$ 和 $\mathrm{cumul}[s+1]$ 之間，所以 $x\ \mathrm{mod}\ M$ 唯一決定 $s$。
- 解碼順序相反；均勻分布時退化成 $10x+s$。

### 例子

$\mathrm{freq}=[3,3,2]$、$M=8$：編 `1,0,2,1`：$0\to3\to8\to38\to101$；解：$101\to38\to8\to3\to0$。

### 串流 rANS

- 狀態限制在 $[Mt,\,2Mt-1]$；編碼前 `shrink_state`：一直輸出最低位元、除以 2，直到 $x\in[\mathrm{freq}[s]t,\,2\mathrm{freq}[s]t-1]$。
- 解碼後 `expand_state`：讀回位元。

### tANS

狀態永遠在固定區間 ⇒ 預先建表「(狀態, 符號) → 新狀態」；接近 Huffman 的速度，壓縮率接近算術編碼。

### 家族比較

| | 取代誰 | 優點 |
|---|---|---|
| rANS | 算術編碼 | 壓縮一樣好、更快、整數運算 |
| tANS | Huffman | 幾乎一樣快、壓縮更好 |

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 不再假設 iid：條件熵、條件分布 | 第 8 集 |
| bits-back、$H(X)=H(X,Z)-H(Z\mid X)$ | 第 8 集條件熵；作業 2 第 4 題 |
| 模型和熵編碼分開、自適應 | 第 8–9 集 |
| zstd 等現代壓縮器用 tANS | 第 10 集實務建議 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **十進位編碼 $x\leftarrow10x+s$ 對均勻分布是最佳的，因為狀態每次乘 $\frac1p=10$；rANS 把它推廣成依符號乘 $\frac{M}{\mathrm{freq}[s]}=\frac1{p(s)}$，用 block_id 和 slot 的拆法讓解碼可以唯一還原符號和前一個狀態，所以總長約 $\log\frac1{p(s^n)}$，壓縮和算術編碼一樣好但只用整數運算。狀態會溢位，所以用 shrink/expand 把它限制在 $[Mt,2Mt-1]$ 並串流輸出位元；tANS 再把固定區間內的轉移預先做成表，速度接近 Huffman。**

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 7 錄影逐字稿（人工字幕，1:20:03）與投影片 L7、L7_ann 整理。*
