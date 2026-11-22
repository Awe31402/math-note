---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 1
lecture: "Lec01 Overview: The philosophy behind information theory"
date: 待補
video: https://youtu.be/i4uhVp_IJE8
notes: Alajaji & Chen《An Introduction to Single-User Information Theory》§1.1（pp. 1–2）；預告 Theorem 4.11（pp. 117–119）
---

# 第 1 集 · Lec01 Overview：Shannon 1948 論文、四個定理、參考書 [▶ 影片](https://youtu.be/i4uhVp_IJE8)

[總目錄](README.md) ｜ 下一集：[02](02-introduction-information-entropy-coding-theorems.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 1 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（22:22，whisper large-v3-turbo）＋ 課本 §1.1（pp. 1–2）、§4.3 Theorem 4.11（pp. 117–119）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Shannon」聽成「Shanen／Jannon／Shanan」，「breakthrough」聽成「bracethrough」，「arbitrarily small」聽成「arbitrismal」，「memoryless」聽成「Memories」，「加性」聽成「香加」，「模稜兩可」聽成「模擬兩可」。開頭 [00:00] 幾句是 whisper 亂碼（夾西班牙文、希臘字母），略過。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要修這門課](#1-為什麼要修這門課)
- [2. Shannon 1948：A Mathematical Theory of Communication](#2-shannon-1948a-mathematical-theory-of-communication)
- [3. Channel capacity：傳輸有上限](#3-channel-capacity傳輸有上限)
- [4. 三個定律的名字](#4-三個定律的名字)
- [5. Entropy 與 uncertainty](#5-entropy-與-uncertainty)
- [6. Information transmission theorem（Theorem 11）](#6-information-transmission-theoremtheorem-11)
- [7. Random coding argument](#7-random-coding-argument)
- [8. 這學期的內容與參考書](#8-這學期的內容與參考書)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

課程導論：介紹 information theory 從哪裡開始、Shannon 1948 年論文為什麼重要、裡面的四個定理，以及參考書。沒有推導。

---

## 1. 為什麼要修這門課

[▶ 01:04](https://youtu.be/i4uhVp_IJE8?t=64)

【口頭】
- 老師在美國 Maryland 大學念博士時，研究所開課不多；通訊組每年一定開的三門是 **Random Process、Detection & Estimation、Information Theory**，因為它們有很重要的數學背景，最好有老師帶。
- 這三門學好，其他通訊的課理解上不會有大問題，只是熟悉度的問題。
- 這門課的目標：(1) 理論背後的**操作意義（operational meaning）**；(2) **很重視證明**，因為證明裡有很多想法；(3) 學會用理論的角度看工程問題——背後是一套哲學體系。

---

## 2. Shannon 1948：A Mathematical Theory of Communication

[▶ 02:39](https://youtu.be/i4uhVp_IJE8?t=159)

- 這個領域從 **Claude Shannon** 1948 年在 Bell Lab 的報告開始。他當年 32 歲，已過世。
- 標題很有自信：**"A Mathematical Theory of Communication"**。
- 這篇是 **conclusive（結論式的）** 論文：幾乎把當時要探討的問題做完了。
- 因為太重要，1949 年又受邀在期刊上發表（原本是 Bell 實驗室內部期刊）。

【課本補充】課本 §1.1（p. 1）：Shannon 主張 (1) 只要傳輸率低於一個由通道統計特性決定的量——**channel capacity**——就能以固定正速率、任意小的錯誤率傳送；(2) 隨機信源可以無失真壓縮到它內在的資訊量——**source entropy**；(3) 若 source entropy 小於 capacity，source 就能可靠傳送；(4) 再推廣到有失真（lossy）的情形。

---

## 3. Channel capacity：傳輸有上限

[▶ 03:43](https://youtu.be/i4uhVp_IJE8?t=223)

**當時的想法**：PCM、PPM 等方法已經在實作。大家認為：同一個傳輸管道，只要技術進步，傳輸速度就能一直增加。

**Shannon 的新觀念**：用純數學證明這**不會發生**。他創造了 **channel capacity（通道容量）** 這個名詞：一個傳輸管道的傳輸**有上限**，技術再進步也不可能超過。這違反當時大部分人的直覺，是劃時代的 breakthrough。

**設定** [▶ 04:44](https://youtu.be/i4uhVp_IJE8?t=284)：
- 固定的傳輸速度（fixed positive rate）$R$，每秒傳幾個 bit。
- 通道有雜訊，雜訊特性是自然界的、固定的。
- 要求錯誤率**任意小（arbitrarily small error）**。
- 這時存在一個 channel capacity $C$。

**論文裡的定義** [▶ 05:17](https://youtu.be/i4uhVp_IJE8?t=317)：老師投影片截錄 Shannon 的定義，大意是
$$C=\lim_{T\to\infty}\frac{\log_2 N(T)}{T},$$
$N(T)$ 是在時間 $0$ 到 $T$ 內可以選擇的訊號（codeword）個數。

> ⚠️ 待確認：投影片的公式逐字稿沒有唸出，上式是依口述（「N 是 codeword 的個數，傳送時間在 0 到大 T 之內」）重建的。

直覺：選 4 種訊號，送一次帶 $\log_2 4=2$ bit；選 8 種，帶 3 bit。若送 3 bit 要 10 ms，速度就是 3 bit / 10 ms。所以 $C$ 代表傳送速度的上限。

---

## 4. 三個定律的名字

[▶ 06:21](https://youtu.be/i4uhVp_IJE8?t=381)

1970 年代以前的書把論文裡的定律叫 **Shannon 第一、第二、第三定律**，還有一個綜合定律。後來的書改用有內容的名字：

| 舊名 | 新名 | 講什麼 |
|---|---|---|
| 第一定律 | **Source coding theorem** | 資料壓縮（無失真），極限是 entropy |
| 第二定律 | **Channel coding theorem** | 資料傳輸，極限是 capacity |
| 第三定律 | **Rate-distortion theorem** | 有失真的資料壓縮：失真和 rate 的關係 |
| 綜合定律 | **Information transmission theorem** | source entropy 和 capacity 比大小（論文 Theorem 11） |

【口頭】「第一、第二、第三」本身沒有資訊，就像說「牛頓第一定律」不如說「慣性定律」清楚；說「第一公路」不知道從哪到哪，說「中投公路」就知道是台中到南投。老師說 1970 年代的書（逐字稿「Blackwood 的書」）還用第一、二、三定律稱呼。

> ⚠️ 逐字稿缺字：[▶ 07:25](https://youtu.be/i4uhVp_IJE8?t=445) 「Blackwood 的書」，依後面 [▶ 18:47](https://youtu.be/i4uhVp_IJE8?t=1127) 介紹「Breha 的書，UIUC 電機系主任」推測是 **Blahut** 的書。

這三個定律在 Shannon 這篇論文裡**全部都已經證明完畢**。

**Rate-distortion 為什麼需要** [▶ 09:26](https://youtu.be/i4uhVp_IJE8?t=566)：例如 entropy 要求每秒 10 Mbps，但管道只能傳 5 Mbps，就必須接受資料損失（distortion）。失真和傳送速度（rate）有什麼關係，就是第三定律。

---

## 5. Entropy 與 uncertainty

[▶ 07:55](https://youtu.be/i4uhVp_IJE8?t=475)

- 論文 Section 6 討論 **entropy**。entropy 這個名詞不是 Shannon 取的，很多領域都在用（是能量的概念）。
- Shannon 是**第一個把 entropy 和 uncertainty 串在一起**的人。【口頭】老師說這是一個 32 歲年輕人很厲害的「理論直覺」。
- 他提出訊息的**三個假設（three assumptions）**，唯一符合的公式就是 entropy；證明在第 2 章（第 8 集）。
- 第一定律：無失真壓縮的最好極限就是 entropy。

---

## 6. Information transmission theorem（Theorem 11）

[▶ 09:57](https://youtu.be/i4uhVp_IJE8?t=597)

這是論文最重要的結果。$H$ = source entropy，$C$ = channel capacity，單位都是每秒幾個 bit。$C$ 只是自然界雜訊的函數，管道確定 $C$ 就確定。

**正向（$H\le C$）**：存在一種傳送方法，使錯誤的頻率**任意小**（arbitrarily small frequency of errors）。付出的代價是複雜度。

**Equivocation** [▶ 10:57](https://youtu.be/i4uhVp_IJE8?t=657)：Shannon 用的字，意思是「模稜兩可」——接收端收到的東西不確定是 1 還是 −1。模稜兩可越高，錯誤率越大。「equivocation 任意小」= 「錯誤率任意小」。【口頭】70 年代以前的古典論文會看到這個字，後來不用了。

**反向（$H>C$）** [▶ 11:29](https://youtu.be/i4uhVp_IJE8?t=689)：不存在方法讓錯誤任意小，錯誤率有天然的下限。老師說下限是
$$P_e\ \ge\ 1-\frac CH.$$
例：$C=5$ Mbps、$H=10$ Mbps，$1-\frac5{10}=\frac12$，錯誤率超過 50%，用最好的方法也一樣。

> ⚠️ 待確認：[▶ 11:29](https://youtu.be/i4uhVp_IJE8?t=689) 老師一開始說「錯誤率小於 $H-C$」（Shannon 原文是用 equivocation 和 $H-C$ 比），後來改說「定理應該是 $1-C/H$」。投影片沒有唸出全文，兩個說法並列。

**Weak converse vs strong converse** [▶ 12:32](https://youtu.be/i4uhVp_IJE8?t=752)：
- Shannon 證的是 **weak converse**：只證明錯誤率大於某個正值。
- 後來有人對無記憶（memoryless）雜訊（例如加性白高斯雜訊）補上 **strong converse**：$H>C$ 時錯誤率其實會**趨近 1**。
- 所以像上帝畫了一條明確的界線：$H<C$，錯誤率可任意小；$H>C$，錯誤率趨近 1，幾乎不可能送成功。

【課本補充】課本 Theorem 4.11（Shannon's channel coding theorem，pp. 117–118）對離散無記憶通道（DMC）定義 $C=\max_{P_X}I(X;Y)$。strong converse 的結論是錯誤率 $\to1$。第 16–18 集會正式講。

---

## 7. Random coding argument

[▶ 13:39](https://youtu.be/i4uhVp_IJE8?t=819)

Shannon 提出全新的證明方法：**random coding argument（隨機編碼論證）**。

- 他**沒有找到**最好的傳送方法，只證明**存在**。
- 怎麼證：把世界上所有傳送方法（碼）都給一個機率，算「錯誤率的期望值」。證明這個期望值會趨近 0。
- 期望值能任意逼近 0 ⇒ 必定存在一個碼，它的錯誤率也那麼小。但它在哪裡，不知道。
- 【口頭】比喻：全班平均 90 分，一定有人考 90 分以上，但不知道是誰。

【課本補充】課本 Theorem 4.11 的證明（pp. 118–119）就是這樣寫的：對一族碼和選碼分布 $\Pr[\mathcal C_n]$，證明
$$E_{\mathcal C_n}\left[P_e(\mathcal C_n)\right]=\sum_{\mathcal C_n}\Pr[\mathcal C_n]\,P_e(\mathcal C_n)\to0\quad(n\to\infty),$$
所以至少存在一個碼序列 $\mathcal C_n^*$ 使 $P_e(\mathcal C_n^*)\to0$。

這種辯證法後來被用在很多領域。【口頭】Cover 的書裡有統計物理、經濟學的應用；簡仁宗老師的 machine learning 課本也有一章講 information theory，因為要用 entropy 當 criterion。

---

## 8. 這學期的內容與參考書

[▶ 15:44](https://youtu.be/i4uhVp_IJE8?t=944)

**主軸**：講清楚三個定律和它們的證明。後半學期做一些延伸（不完全照 Shannon 古典的方式）。

**課本**：老師「去年出的書」，即本課課本 Alajaji & Chen（2018）。

**參考書**（【口頭】老師的評語；書名在投影片上，逐字稿沒有唸，以下只記作者和評語）：

1. **老師和 Moser 合寫的書**：寫給高中生看，只要高中數學，**沒有證明**，用範例講概念。想快速認識 information theory 可以看。
2. **Cover（與 Thomas）的書**：最常用的課本，包山包海，幾乎把後期的領域都涵蓋（但 channel reliability function 等較深的沒放）。Cover 是 Stanford 教授，前幾年過世。缺點：太厚、**很多證明步驟省略**（像 Proakis 的數位通訊），初學者容易抓不到重點。
3. **Han（韓太舜）的書**：韓國人、在日本當教授。非常數學，「幾乎看不懂、很多我也看不懂」，但提出全新的看問題觀點，是**第二部分的主要內容**。他開啟了這個領域，得過 Shannon Award。
4. **Raymond Yeung（楊偉豪，香港中文大學）的書**：network information theory 的創始人，有 best paper。書寫得不錯，但很貴（每頁 14 塊）。
5. **Blahut 的書**：老師在 Maryland 時，Cover 的書還沒出，大部分人用這本。古典寫法，證明寫得很清楚，老師很喜歡。作者曾是 UIUC 電機系主任。好像絕版了。
6. **Csiszár 和 Körner 的書**（匈牙利）：不容易看，**全部用 typical set（典型集合）的方式證明**，和別人不一樣，有很多別的書沒有的定理（例如第 2 章的 **blowing-up lemma**：把一個集合稍微擴大，它的機率就變成趨近 1）。可以挖寶。
7. **Gallager 的書**（MIT）：老師**最喜歡**的一本。很經典，證明步驟和解釋都非常清楚。

> ⚠️ 逐字稿缺字：「Breha」→ Blahut；「Sesar 跟 Briven」→ Csiszár 與 Körner（依「匈牙利學者」推測）；「提升韓語日本人」→ Han；「Raymond Young」→ Raymond Yeung；「Gellaguer／Galegger」→ Gallager；「Blow up Lemma」→ blowing-up lemma；「Prokes」→ Proakis；「簡仁中」→ 簡仁宗（推測）。

【口頭】小故事 [▶ 20:18](https://youtu.be/i4uhVp_IJE8?t=1218)：
- Csiszár 和 Gallager 都是八十幾歲的古典學者，很樂意分享研究，鼓勵年輕人。
- 1988 年左右 Cover 募款找了一群學者聚在一起三天解難題，大部分人在吃吃喝喝，只有 Gallager 很認真，解了半個問題；其他四十幾個問題都沒解出來。後來集結成書 *Open Problems in Communication and Computation*。
- 台灣的李穎（逐字稿「原汁大學」，推測是元智大學）是 Gallager 的學生。

**成績** [▶ 21:49](https://youtu.be/i4uhVp_IJE8?t=1309)：考兩次；每週給習題和解答。影片在這裡結束，後面待補。

---

## 9. 一頁速查表

**Shannon 1948 的四個定理**
- Source coding theorem：無失真壓縮的極限 = source entropy $H$。
- Channel coding theorem：錯誤率任意小時，傳輸率的上限 = channel capacity $C$。
- Rate-distortion theorem：容許失真時，rate 和 distortion 的關係。
- Information transmission theorem（Theorem 11）：$H\le C$ ⇒ 可以可靠傳送；$H>C$ ⇒ 不行。

**Converse**
- Weak：$H>C$ 時錯誤率有正的下限（老師口述 $1-C/H$）。
- Strong：$H>C$ 時錯誤率 → 1。

**Random coding argument**
所有碼的平均錯誤率 $E[P_e]\to0$ ⇒ 至少有一個碼的 $P_e\to0$（平均 90 分 ⇒ 有人 ≥ 90 分）。只證存在，不給構造。

**Capacity（論文的定義，重建）**
$C=\lim_{T\to\infty}\frac1T\log_2N(T)$，$N(T)$ = 時間 $T$ 內可選的訊號數。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Shannon 的思路、entropy 的公設 | 第 2 集、第 8 集 |
| Source coding theorem | 第 12 集（第 3 章） |
| Channel coding theorem、random coding、weak/strong converse | 第 16–18 集（§4.3） |
| Rate-distortion theorem | 第 27–29 集（第 6 章） |
| Information transmission theorem（$H$ vs $C$） | 第 21 集（§4.6）、第 30–31 集 |
| Han 的觀點（第二部分） | 第 32–35 集 |

---

## 附：本集一句話總結

> **Shannon 1948 年證明了：通道有一個技術再進步也超不過的上限 capacity；只要 source entropy 小於 capacity，就存在錯誤率任意小的傳法——而他是用「所有碼的平均」證明存在性，不是真的造出來。**

---

## ⚠️ 待確認清單

1. [▶ 05:17](https://youtu.be/i4uhVp_IJE8?t=317) 投影片上 Shannon 的 capacity 定義公式沒有唸出，筆記的式子是重建的。
2. [▶ 11:29](https://youtu.be/i4uhVp_IJE8?t=689) Theorem 11 反向的下限：老師先說「$H-C$」，後說「$1-C/H$」，投影片原文待補。

---

*筆記依據陳伯寧老師「消息理論」Lec01 錄影逐字稿（whisper large-v3-turbo，22:22）與 Alajaji & Chen 課本 §1.1、Theorem 4.11 整理。*
