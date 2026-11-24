---
course: Stanford EE274 Data Compression  Theory and Applications（2023 秋）
episode: 10
lecture: Lecture 10
date: 2023-10-30
video: https://youtu.be/amv9LiGyY5s
notes: 投影片 L10.pdf、L10_ann.pdf（打字版）；《Elements of Information Theory》§13.4–13.5（書頁 440–449）
---

# 第 10 集 · Lecture 10：LZ 與通用壓縮（LZ and Universal Compression） [▶ 影片](https://youtu.be/amv9LiGyY5s)

← 上一集：[09-context-based-ac-llm-compression](09-context-based-ac-llm-compression.md) ｜ [總目錄](README.md) ｜ 下一集：[11-lossy-compression-quantization](11-lossy-compression-quantization.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 10 集
> **講者**：Shubham Chandak
> **來源**：YouTube 錄影逐字稿（1:24:38，人工字幕 en-US）＋ 投影片 `L10.pdf`、`L10_ann.pdf` ＋ Cover & Thomas §13.4–13.5
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
- [1. 回顧與小考](#1-回顧與小考)
- [2. 通用壓縮](#2-通用壓縮)
- [3. LZ 家族](#3-lz-家族)
- [4. LZ77 的解析（編碼）](#4-lz77-的解析編碼)
- [5. LZ77 的反解析（解碼）](#5-lz77-的反解析解碼)
- [6. 為什麼 LZ77 是通用的](#6-為什麼-lz77-是通用的)
- [7. 真實資料上的匹配](#7-真實資料上的匹配)
- [8. 實務：滑動視窗](#8-實務滑動視窗)
- [9. 實務：怎麼找匹配](#9-實務怎麼找匹配)
- [10. 實務：熵編碼](#10-實務熵編碼)
- [11. 各種 LZ77 實作的比較](#11-各種-lz77-實作的比較)
- [12. 無損壓縮的實務建議](#12-無損壓縮的實務建議)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/amv9LiGyY5s?t=5) 無損壓縮的最後一講：

| 段落 | 內容 | 課本 |
|---|---|---|
| 前半 | **LZ77**：最重要的無損壓縮技術、為什麼它是通用的 | §13.4–13.5 |
| 後半 | 無損壓縮的**實務建議**（講者和其他人的經驗，今年新加的） | 課本無 |

[▶ 02:06](https://youtu.be/amv9LiGyY5s?t=126) 前幾講都靠仔細建模、學資料的機率分布；今天看一個**完全不同**的技術：不建模，照樣效果很好。

---

## 1. 回顧與小考

[▶ 00:05](https://youtu.be/amv9LiGyY5s?t=5) 回顧：

- **熵率**：平穩來源無損壓縮的根本極限（iid → 熵；Markov → 條件熵）[▶ 00:49](https://youtu.be/amv9LiGyY5s?t=49)。
- context-based 算術編碼：**預測 ⇒ 壓縮** [▶ 01:31](https://youtu.be/amv9LiGyY5s?t=91)；$k$ 階自適應、進階模型、LLM。

**小考第 2 題**（1 階自適應算術編碼）[▶ 02:06](https://youtu.be/amv9LiGyY5s?t=126)：講者做了一張表（每一步前一個符號、目前符號、更新前後的計數），請大家自己看。

**小考第 1 題：該用哪一個？** [▶ 03:19](https://youtu.be/amv9LiGyY5s?t=199)

| 情境 | 答案 |
|---|---|
| 知道資料大致是 2 階 Markov，但不知道轉移機率 | **context-based 自適應**算術編碼 [▶ 03:19](https://youtu.be/amv9LiGyY5s?t=199)：不知道機率，就從資料學 |
| 知道資料是 3 階 Markov，也知道確切分布 | **context-based**算術編碼 [▶ 03:56](https://youtu.be/amv9LiGyY5s?t=236)：已知分布，從資料學反而沒效率 |
| 對輸入資料一無所知（題目因為沒教到而刪掉） | **LZ77**：今天的主題，不對資料做任何假設 [▶ 03:56](https://youtu.be/amv9LiGyY5s?t=236) |

---

## 2. 通用壓縮

### 2.1 歷史

[▶ 04:38](https://youtu.be/amv9LiGyY5s?t=278) Shannon 1948 年後，大家研究 iid 來源、做 context 方法。但沒人知道：對一般平穩分布，能不能有一個**不需要事先知道分布**、對任何分布都有效的壓縮器？然後 Bell Labs 的 **Abraham Lempel 和 Jacob Ziv** 在 1977、1978 年的一系列論文改變了壓縮的世界。

### 2.2 定義

[▶ 05:20](https://youtu.be/amv9LiGyY5s?t=320) **通用壓縮器**（universal compressor）：對任何平穩輸入都表現良好，不需要事先知道來源分布。

[▶ 05:55](https://youtu.be/amv9LiGyY5s?t=355) 正式一點：壓縮器有長度函數 $l(x^n)$（描述 $x^n$ 要幾位元）。它是**通用的**，若對**任何**平穩遍歷（ergodic，技術條件）來源，

$$\lim_{n\to\infty}\frac{\mathbb{E}\left[l(X^n)\right]}{n}=H(\mathbf X)\quad\text{（熵率）}.$$

[▶ 06:30](https://youtu.be/amv9LiGyY5s?t=390) 沒有附帶條件：不是「對 $k$ 階成立、對 $k+1$ 階不成立」，而是對任何平穩來源，再複雜都一樣。**單一個壓縮器漸近最佳**。【口頭】Lempel 和 Ziv 之前，大家以為這不可能；到今天這仍是很令人驚訝的結果。

### 2.3 通用預測

[▶ 06:30](https://youtu.be/amv9LiGyY5s?t=390) 反過來看：上一講說每個壓縮器誘導一個分布 $\hat p=2^{-l}$ [▶ 07:14](https://youtu.be/amv9LiGyY5s?t=434)。通用壓縮器的 $\hat p$，隨 $n$ 增大能任意逼近**任何**平穩分布。示意圖 [▶ 07:55](https://youtu.be/amv9LiGyY5s?t=475)：所有平穩分布散在空間中，存在一個點 $\hat p_{\text{LZ}}$ 和每一點都很近。

[▶ 07:55](https://youtu.be/amv9LiGyY5s?t=475) 要嚴格表述需要更多工夫。【口頭】Tsachy 是這方面的專家，他把通用壓縮的理論推廣到通用去雜訊、通用有損壓縮；可以看他的講義，或等 EE376C（通用壓縮、通用去雜訊的理論課）下次開課 [▶ 08:30](https://youtu.be/amv9LiGyY5s?t=510)。

---

## 3. LZ 家族

[▶ 09:04](https://youtu.be/amv9LiGyY5s?t=544) Lempel–Ziv 家族有很多實作：1977 年的叫 **LZ77**、1978 年的叫 **LZ78**，之後大家各自加東西做變體 [▶ 09:41](https://youtu.be/amv9LiGyY5s?t=581)。

【投影片補充】`L10.pdf`：

| 變體 | 用在 |
|---|---|
| LZ77 | gzip、zstd、PNG、zip、LZ4、Snappy |
| LZW（LZ78 的變體） | Linux 的 `compress`、GIF |
| LZMA（LZ77 的變體） | 7-Zip、xz |

[▶ 09:41](https://youtu.be/amv9LiGyY5s?t=581) 今天常見的壓縮器大多建立在某種 Lempel–Ziv 上。

---

## 4. LZ77 的解析（編碼）

### 4.1 想法

[▶ 09:41](https://youtu.be/amv9LiGyY5s?t=581) 講者放了一首每一行都重複前一行的歌（字幕沒寫歌名；投影片手寫「Around the world」）[▶ 10:16](https://youtu.be/amv9LiGyY5s?t=616)。

> **歷史會重演**：看到的序列多半以前就看過；那就放一個指標：「這個字我 100 個字之前看過」[▶ 10:16](https://youtu.be/amv9LiGyY5s?t=616)。
> **把重複的片段換成指標（offset）和長度（length）** [▶ 10:50](https://youtu.be/amv9LiGyY5s?t=650)。

- **offset（偏移）**：在多遠以前出現過。
- **length（長度）**：匹配多長 [▶ 11:26](https://youtu.be/amv9LiGyY5s?t=686)。

### 4.2 例子：`ABBABBABBCAB`

[▶ 11:59](https://youtu.be/amv9LiGyY5s?t=719) 把序列分成三條串流：**未匹配的字面值**（unmatched literals）、**匹配長度**、**匹配偏移**。

1. [▶ 12:31](https://youtu.be/amv9LiGyY5s?t=751) 第一個 A：沒看過 → 字面值。B：沒看過 → 字面值。
2. 下一個 B：剛看過 B！能延伸嗎？看過 B，但沒看過 BA，所以長度 1、偏移 1（就在前一個字元）[▶ 12:31](https://youtu.be/amv9LiGyY5s?t=751)。
3. [▶ 13:08](https://youtu.be/amv9LiGyY5s?t=788) 看過 A 嗎？AB？ABB？ABBA？……學生意見不一。講者：先相信我（重疊的匹配等一下解釋）。ABBABB 確實和前面一樣 [▶ 13:43](https://youtu.be/amv9LiGyY5s?t=823)。【課堂討論】長度？學生答 **6**；偏移？**3** [▶ 14:19](https://youtu.be/amv9LiGyY5s?t=859)。
4. C：沒看過 → 字面值。
5. AB：剛看過。【課堂討論】偏移？學生答 **4** [▶ 14:50](https://youtu.be/amv9LiGyY5s?t=890)（把目前位置當 0，往回數 −1、−2、−3、−4）。

（依 `L10.pdf`）

| 未匹配字面值 | 匹配長度 | 匹配偏移 |
|---|---|---|
| `AB` | 1 | 1 |
| — | 6 | 3 |
| `C` | 2 | 4 |

> 以下**不是逐字稿內容**，是解釋第 3 步的「重疊」：位置 3 開始要編 `ABBABB`（位置 3–8）。偏移 3 表示從位置 0 開始抄：位置 0–5 是 `ABBABB`。但位置 3–5 本身就在要抄的範圍裡，所以來源和目的地**重疊**了。照順序一個字元一個字元抄就沒問題：要寫位置 $t$ 時，位置 $t-3$ 一定已經寫好了。

### 4.3 虛擬碼

[▶ 17:51](https://youtu.be/amv9LiGyY5s?t=1071)（`L10.pdf`）

```
已解析到 x[i-1]：
    找最大的 k，使得對某個 j < i：x[j : j+k] == x[i : i+k]
        （j:j+k 和 i:i+k 允許重疊）
    匹配長度 = k，匹配偏移 = i - j
    找不到匹配 → 存成字面值
```

### 4.4 很多種合法的編碼

[▶ 20:33](https://youtu.be/amv9LiGyY5s?t=1233) LZ77 有很多種編法，都用**同一個解碼器**：

- 很懶，什麼都不匹配、全部當字面值：合法。
- 很努力找最好的匹配：合法。
- 匹配長度不准超過 100：也合法。

---

## 5. LZ77 的反解析（解碼）

### 5.1 例子

[▶ 15:33](https://youtu.be/amv9LiGyY5s?t=933) 解碼剛剛的表（假裝不知道答案）：

1. [▶ 16:04](https://youtu.be/amv9LiGyY5s?t=964) 先抄字面值 `AB`。長度 1、偏移 1：抄前一個字元 → `ABB`。
2. [▶ 16:36](https://youtu.be/amv9LiGyY5s?t=996) 長度 6、偏移 3：一個字元一個字元抄。第 1 個抄 3 個前的 A、再抄 B、B……[▶ 17:10](https://youtu.be/amv9LiGyY5s?t=1030) 到了重疊的部分，要抄的字元**剛剛才解出來**，照樣可以抄 → `ABBABBABB`。
3. 字面值 `C`；長度 2、偏移 4：從 4 個前開始抄 A、B → `ABBABBABBCAB` [▶ 17:10](https://youtu.be/amv9LiGyY5s?t=1030)。

> **只要依序解碼，匹配和自己重疊也沒關係。**

### 5.2 虛擬碼

[▶ 18:36](https://youtu.be/amv9LiGyY5s?t=1116)（`L10.pdf`）

```
每一步：
    先把字面值抄到輸出 y
    解長度 l、偏移 o 的匹配：
        若 l < o：  把 y[-o : -o+l] 接到 y 後面        # 情況一：整段複製
        否則：      重複 l 次：把 y[-o] 接到 y 後面     # 情況二：重疊，要逐字元
```

[▶ 19:13](https://youtu.be/amv9LiGyY5s?t=1153) 情況一：偏移比長度大很多，直接整段複製。情況二：偏移很小、會重疊，要小心 [▶ 19:56](https://youtu.be/amv9LiGyY5s?t=1196)。

> **解壓縮非常快，因為只是在複製。**

【投影片補充】`L10.pdf` 有一題小考：解析 `AABBBBBBBAABBBCDCDCD`，以及反解析一張用不同解析器產生的表（字面值 `AABBB`、長度 4 偏移 1；長度 5 偏移 9；字面值 `CDCD`、長度 2 偏移 2）。講者說這會出在小考 [▶ 19:56](https://youtu.be/amv9LiGyY5s?t=1196)，本筆記不寫答案。

### 5.3 編碼流程

[▶ 21:12](https://youtu.be/amv9LiGyY5s?t=1272)

```
輸入 ──> [LZ77 解析] ──> 字面值、匹配 ──> [熵編碼] ──> 壓縮檔
```

字面值、匹配長度、匹配偏移都要再用 Huffman、ANS 或算術編碼壓。各實作的差別主要在這裡（§10）。

---

## 6. 為什麼 LZ77 是通用的

[▶ 21:51](https://youtu.be/amv9LiGyY5s?t=1311) 只給直覺，不給完整證明。

### 6.1 iid：兩次出現的平均間隔【課堂討論】

[▶ 21:51](https://youtu.be/amv9LiGyY5s?t=1311) iid 序列裡，機率 $P(a)$ 的符號 $a$，相鄰兩次出現平均隔多遠？

- [▶ 22:31](https://youtu.be/amv9LiGyY5s?t=1351) $a$ 機率大，間隔大還是小？學生答：**小**，常出現就常碰到。
- [▶ 23:04](https://youtu.be/amv9LiGyY5s?t=1384) 長度 $n$ 的區塊裡預期看到幾次 $a$？學生答 $nP(a)$ [▶ 23:42](https://youtu.be/amv9LiGyY5s?t=1422)：每個位置是 $a$ 的機率都是 $P(a)$，期望值線性。依大數法則，實際次數也很接近 $nP(a)$。
- [▶ 24:18](https://youtu.be/amv9LiGyY5s?t=1458) 若 $n=1000$、$nP(a)=200$，平均間隔？學生答 **5** [▶ 24:54](https://youtu.be/amv9LiGyY5s?t=1494)：$1000/200$。

所以**平均間隔是 $\frac{n}{nP(a)}=\frac1{P(a)}$**。

### 6.2 Kac 引理

[▶ 25:26](https://youtu.be/amv9LiGyY5s?t=1526) 推廣到平穩過程的**序列**（`L10.pdf`）：

> **Kac 引理**：$\dots,X_{-1},X_0,X_1,\dots$ 是平穩遍歷過程，$R_n$ 是 $(X_0,\dots,X_{n-1})$ 的**回返時間**（上一次在位置 0 之前出現是多久以前）。給定 $(X_0,\dots,X_{n-1})=x_0^{n-1}$，
> $$\mathbb{E}\left[R_n\right]=\frac1{p(x_0^{n-1})}.$$

意思：現在看到序列 $x^n$，上一次看到它平均是 $\frac1{p(x^n)}$ 個位置以前 [▶ 26:10](https://youtu.be/amv9LiGyY5s?t=1570)。所以 **LZ77 的匹配偏移約為 $\frac1{p(x^n)}$**。

### 6.3 碼長

[▶ 26:49](https://youtu.be/amv9LiGyY5s?t=1609) 一個整數 $N$ 大約用 $\log N$ 位元就能編（投影片：例如 SCL 裡的 Elias Delta 碼）。所以偏移 $\frac1{p(x^n)}$ 約用

$$\log_2\frac1{p(x^n)}\ \text{位元}.$$

【課堂討論】[▶ 27:30](https://youtu.be/amv9LiGyY5s?t=1650) $\log\frac1p$ 讓你想到什麼？**第 2 講起的經驗法則**：做到 $\log\frac1p$ 就是最佳的。

- 可以證明**長度和字面值的貢獻可以忽略**，理論上幾乎所有空間都在偏移 [▶ 27:30](https://youtu.be/amv9LiGyY5s?t=1650)。
- [▶ 28:04](https://youtu.be/amv9LiGyY5s?t=1684) 取期望值：$\mathbb{E}[l(X^n)]\approx\mathbb{E}\left[\log\frac1{p(X^n)}\right]=H(X^n)$，這是最佳的；取 $n\to\infty$，就達到熵率。

> **一個序列平均在 $\frac1p$ 個位置之前出現過 ⇒ 用 $\log\frac1p$ 位元編它的偏移 ⇒ 達到熵率。**

[▶ 28:51](https://youtu.be/amv9LiGyY5s?t=1731) 完整證明出乎意料地難；LZ78 的理論漂亮得多，但課堂講 LZ77 是因為實務上用得多 [▶ 29:26](https://youtu.be/amv9LiGyY5s?t=1766)。

【投影片補充】嚴謹證明見 Cover & Thomas 第 13 章，或 Wyner & Ziv〈The sliding-window Lempel-Ziv algorithm is asymptotically optimal〉（Proc. IEEE, 1994）。

【課本補充】§13.5.1（書頁 443–448）用 Kac 引理（Lemma 13.5.1）證明滑動視窗 LZ 的漸近最佳性；§13.4.1（書頁 441）是滑動視窗 LZ77 的演算法描述，§13.4.2 是樹狀 LZ78。

### 6.4 理論解釋不了實務表現

[▶ 29:26](https://youtu.be/amv9LiGyY5s?t=1766) 漸近理論無法完全解釋 LZ77 在實務上**為什麼這麼好** [▶ 29:58](https://youtu.be/amv9LiGyY5s?t=1798)：

- 對 $k$ 階 Markov 來源，LZ77 在極限下會達到熵率，但收斂速度不怎麼樣，正常大小的資料不該期待它多好。
- 但在**真實資料**上效果極好，因為世界不是 $k$ 階 Markov [▶ 30:35](https://youtu.be/amv9LiGyY5s?t=1835)：英文裡的重複比 $k$ 階模型預期的長得多，人名會一再出現。所以找匹配這個想法和真實資料非常契合。

---

## 7. 真實資料上的匹配

[▶ 31:20](https://youtu.be/amv9LiGyY5s?t=1880) SCL 有去年的 LZ77 實作，講者這幾天又寫了一個（今年有 ChatGPT，寫程式容易多了）[▶ 31:56](https://youtu.be/amv9LiGyY5s?t=1916)。

**長匹配** [▶ 31:56](https://youtu.be/amv9LiGyY5s?t=1916)：

- 《愛麗絲夢遊仙境》（標準壓縮語料之一）：「Beautiful soup, beautiful soup, soup of the evening」兩段完全一樣 [▶ 32:28](https://youtu.be/amv9LiGyY5s?t=1948)。$k$ 階模型解釋不了這種長匹配；LZ77 用兩個數字（偏移、長度）就描述完。
- CSS 檔：`transparent 25%, transparent 25%` 這類很長的重複 [▶ 33:09](https://youtu.be/amv9LiGyY5s?t=1989)。

**遠處的短匹配也划算** [▶ 33:09](https://youtu.be/amv9LiGyY5s?t=1989)：`pleasure` 在書的第一頁和最後一頁各出現一次，相隔約 150,000 位元組。粗算 [▶ 34:20](https://youtu.be/amv9LiGyY5s?t=2060)：

- 直接編：一般 Huffman 碼大約每位元組 3 位元（最好的壓縮器約 1 位元），8 個字元約 24 位元。
- 當匹配：偏移 150,000 要 $\log_2150000\approx17.2$ 位元 [▶ 34:53](https://youtu.be/amv9LiGyY5s?t=2093)（學生算出）。

[▶ 35:24](https://youtu.be/amv9LiGyY5s?t=2124) 所以就算是很遠的短匹配也省位元。3 位元也不是亂選的，是英文的 0 階熵量級（約 4 位元）。當然有臨界點：偏移十億的長度 2 匹配大概就不划算 [▶ 36:00](https://youtu.be/amv9LiGyY5s?t=2160)。

**偏移和長度的分布** [▶ 36:38](https://youtu.be/amv9LiGyY5s?t=2198)（`L10.pdf` 的直方圖，對數座標）：

- 愛麗絲：偏移多半小，偶爾很大（最大約 150,000，因為書就這麼長）；長度多半小，偶爾超過 100 位元組。
- Bootstrap 的 CSS（bootstrap.min.css）[▶ 37:09](https://youtu.be/amv9LiGyY5s?t=2229)：有超過 500 位元組的極長匹配。

[▶ 37:42](https://youtu.be/amv9LiGyY5s?t=2262) **每個檔案、每種資料分布都不一樣**：程式碼同樣的關鍵字、變數名重複很多；文字是重複的字但不常整句重複；CSV 表格可能整列重複；隨機資料幾乎找不到匹配 [▶ 38:16](https://youtu.be/amv9LiGyY5s?t=2296)。這應該影響你選哪種 LZ77。

【口頭】[▶ 38:16](https://youtu.be/amv9LiGyY5s?t=2296) LZ77 大概是今天最流行、最廣泛使用的壓縮技術。要完整講 gzip 怎麼運作要好幾講，講 Zstandard 大概要整門課；講者說他也不夠格講那麼深 [▶ 38:57](https://youtu.be/amv9LiGyY5s?t=2337)。

---

## 8. 實務：滑動視窗

[▶ 38:57](https://youtu.be/amv9LiGyY5s?t=2337) 要保留**無限的過去**嗎？1 GB 的檔案要把前 1 GB 都放在記憶體裡找匹配？不。

> **滑動視窗 LZ77**（sliding window）：只在最近一段（gzip 幾十 KB、zstd 到幾 MB）裡找匹配 [▶ 39:32](https://youtu.be/amv9LiGyY5s?t=2372)。

- 技術細節：用**環形緩衝區**（circular buffer），不必每次重新配置記憶體或搬動資料。
- [▶ 40:08](https://youtu.be/amv9LiGyY5s?t=2408) **視窗越大壓縮越好**（能找到更遠的匹配），但**編碼和解碼兩端**都要更多記憶體（要存整個視窗）。
- SCL 有實作（`LZ77Window`、`LZ77SlidingWindowEncoder`/`Decoder`），講者說文件寫得不錯，他自己找不到容易講解的實作 [▶ 40:08](https://youtu.be/amv9LiGyY5s?t=2408)。

**實驗** [▶ 40:44](https://youtu.be/amv9LiGyY5s?t=2444)：愛麗絲，視窗大小以指數放大。視窗越大越好，然後**趨於平緩**；視窗比檔案還大當然沒用，一般而言過了某個點也幫助不大。看資料、看能負擔多少記憶體，沒有「永遠用 100,000」這種規則 [▶ 41:20](https://youtu.be/amv9LiGyY5s?t=2480)。

---

## 9. 實務：怎麼找匹配

### 9.1 雜湊表

[▶ 41:52](https://youtu.be/amv9LiGyY5s?t=2512) **找匹配只是編碼器的事**，不管怎麼找，解碼器都解得出來。

基本做法 [▶ 41:52](https://youtu.be/amv9LiGyY5s?t=2512)：

1. 把過去出現過的固定長度子字串（例如長度 4）**索引**在雜湊表（或二元樹）裡：`ABCD` 出現在位置 1、10、15、20……[▶ 42:33](https://youtu.be/amv9LiGyY5s?t=2553)
2. 在目前位置看到 `ABCD`，查表得到候選位置。
3. **延伸**每個候選，看哪個匹配最長 [▶ 43:13](https://youtu.be/amv9LiGyY5s?t=2593)。例：位置 10 的 `ABCD` 後面接 `EF`、位置 1 的後面接 `ZX`，目前是 `ABCDEF`，就選位置 10。

這叫 **seed** 的想法（索引的那段叫 seed），很多演算法都用：大幅縮小搜尋空間 [▶ 43:57](https://youtu.be/amv9LiGyY5s?t=2637)。

【Q&A】[▶ 44:33](https://youtu.be/amv9LiGyY5s?t=2673) 學生問：為什麼用長度 4？長度 2、3 的匹配不值得嗎？講者 [▶ 45:09](https://youtu.be/amv9LiGyY5s?t=2709)：長度 2 會有很多**假陽性**（AB 比 ABCD 常見太多），要檢查的候選大增，複雜度上升；但真的很努力，可能找到比長度 4 更好的匹配。這是取捨：通常更慢、可能壓得更好。太長則會錯過很多匹配 [▶ 45:41](https://youtu.be/amv9LiGyY5s?t=2741)。

### 9.2 貪婪 vs. 懶惰

[▶ 45:41](https://youtu.be/amv9LiGyY5s?t=2741) 理論版的 LZ77 是**貪婪的**：第一個找到的匹配就拿，不考慮未來。

例 [▶ 46:17](https://youtu.be/amv9LiGyY5s?t=2777)：過去有 `…ABCDEF…BBCED…`，目前是 `…ABCDE…`（講者寫在白板上）。

- **貪婪**：看到 `AB` 有匹配就拿，長度 2 [▶ 46:57](https://youtu.be/amv9LiGyY5s?t=2817)。
- **懶惰**（lazy）[▶ 47:28](https://youtu.be/amv9LiGyY5s?t=2848)：先別急著拿。跳過 A（當字面值），從 B 開始找，結果找到長度 5 的匹配。

[▶ 48:07](https://youtu.be/amv9LiGyY5s?t=2887) 更進一步，把它變成最佳化問題（動態規劃），叫 **optimal parsing**：哪種解析讓字面值最少、壓縮最好？策略越複雜越慢：貪婪最快；懶惰較慢；最佳解析最慢 [▶ 48:39](https://youtu.be/amv9LiGyY5s?t=2919)。

### 9.3 SCL 的編碼器結構

[▶ 49:11](https://youtu.be/amv9LiGyY5s?t=2951)（只描述）`LZ77SlidingWindowEncoder` 接一個匹配器（match finder）和視窗大小；匹配器的核心是 `find_best_match`。講者寫的 `HashBasedMatchFinder` 參數 [▶ 49:47](https://youtu.be/amv9LiGyY5s?t=2987)：

| 參數 | 意思 |
|---|---|
| `hash_length` | 雜湊的子字串長度（例如 4） |
| `hash_table_size` | 雜湊表大小（不能無限大） |
| `max_chain_length` | 雜湊鏈最長多少（課堂不講） |
| `lazy` | 是否往前看一步、跳過一個字面值換更長的匹配 |
| `minimum_match_length` | 最短可接受的匹配 |

[▶ 50:18](https://youtu.be/amv9LiGyY5s?t=3018) **這些全都相容於同一個解碼器**。可以不斷用更聰明的編碼策略壓得更好，而不會讓讀檔的人壞掉。SCL 把匹配器分開，可以抽換、自己寫（例如動態規劃）[▶ 53:22](https://youtu.be/amv9LiGyY5s?t=3202)。

### 9.4 實驗：最短匹配長度、貪婪 vs. 懶惰

[▶ 50:58](https://youtu.be/amv9LiGyY5s?t=3058) 愛麗絲，加大最短匹配長度：**字面值越來越多、匹配越來越少**。

【課堂討論】[▶ 50:58](https://youtu.be/amv9LiGyY5s?t=3058) 為什麼？學生答：沒匹配就得存成字面值 [▶ 51:33](https://youtu.be/amv9LiGyY5s?t=3093)。講者：不准短匹配，就有更多未匹配的字面值；匹配變少，存匹配的成本也變少。取捨：最短長度太小，滿是長度 1、2 的匹配，每個都要花錢；也許留幾個字面值、改用長一點的匹配比較好 [▶ 52:09](https://youtu.be/amv9LiGyY5s?t=3129)。

[▶ 52:43](https://youtu.be/amv9LiGyY5s?t=3163) 懶惰策略在每個最短匹配長度下都**勝過**貪婪策略（這個檔案）。編碼器有很多選擇：更慢換更好的壓縮，或更多記憶體換更好的壓縮 [▶ 52:43](https://youtu.be/amv9LiGyY5s?t=3163)。

---

## 10. 實務：熵編碼

[▶ 53:56](https://youtu.be/amv9LiGyY5s?t=3236) 最後還要存成位元。現代壓縮器的標準做法（gzip 稍有不同）：把一個區塊裡的未匹配字面值**串在一起**，並記錄每段有幾個字面值 [▶ 53:56](https://youtu.be/amv9LiGyY5s?t=3236)。

（依 `L10.pdf`）

| 未匹配字面值 | 匹配長度 | 匹配偏移 |
|---|---|---|
| `AABBB` | 4 | 1 |
| — | 5 | 9 |
| `CDCD` | 2 | 2 |

變成 [▶ 54:33](https://youtu.be/amv9LiGyY5s?t=3273)：

```
literals = AABBBCDCD
```

| 字面值個數 | 匹配長度 | 匹配偏移 |
|---|---|---|
| 5 | 4 | 1 |
| 0 | 5 | 9 |
| 4 | 2 | 2 |

也就是一條位元組序列加三條整數序列。

[▶ 54:33](https://youtu.be/amv9LiGyY5s?t=3273) **熵編碼器的威力就在這裡**：LZ77 把很複雜的平穩分布**轉換成簡單得多、接近 iid 的分布**，再用你喜歡的 iid 熵編碼器 [▶ 55:09](https://youtu.be/amv9LiGyY5s?t=3309)。

| 做法 | 誰在用 |
|---|---|
| Huffman | gzip 全靠它；zstd 只用在字面值 [▶ 55:09](https://youtu.be/amv9LiGyY5s?t=3309) |
| tANS | zstd 用在匹配長度和偏移（投影片寫字面值和匹配長度；講者口頭自我更正） |
| context-based 算術編碼（編解碼都慢） | LZMA、xz、7-Zip [▶ 55:42](https://youtu.be/amv9LiGyY5s?t=3342) |
| 跳過熵編碼、用固定長度碼（極快） | LZ4、Snappy |

> ⚠️ 逐字稿缺字 [▶ 55:09](https://youtu.be/amv9LiGyY5s?t=3309)：字幕「C-standard uses it for-- oh, what are this? Not for literals. It uses for match lengths and offsets」，「C-standard」應為 zstandard。投影片寫「zstd uses tANS for literals and match lengths」，和口頭不一致，兩邊都列。

【投影片補充】整數的熵編碼（講者跳過，請回家讀）[▶ 56:19](https://youtu.be/amv9LiGyY5s?t=3379)：匹配長度、偏移範圍很大（可達數百萬），個別值的計數很少（某個偏移 14546 不會出現很多次）。典型做法是**分箱**：例如 2–3、4–7、8–15……對**箱子編號**做熵編碼，箱內位置用固定長度碼（落在 8–15 就用 3 位元）。可以想成一棵 Huffman 樹，葉子是箱子，每個葉子再接一棵完整二元樹。SCL 有 `LogScaleBinnedIntegerEncoder`。

---

## 11. 各種 LZ77 實作的比較

[▶ 56:19](https://youtu.be/amv9LiGyY5s?t=3379) 解析策略、視窗大小、熵編碼器、實作細節（SIMD、平行化）對速度和記憶體影響很大。

**zstd vs. zlib（gzip 背後的函式庫）** [▶ 56:19](https://youtu.be/amv9LiGyY5s?t=3379)（zstd 網站的圖）：

- 壓縮：橫軸壓縮速度、縱軸壓縮比，要往右上 [▶ 57:00](https://youtu.be/amv9LiGyY5s?t=3420)。各點是不同等級（更大視窗、更強的匹配器）。**zstd 在每個方面都勝過 zlib**：演算法更好、用更多記憶體、實作更能利用現代硬體指令。
- 解壓縮 [▶ 57:41](https://youtu.be/amv9LiGyY5s?t=3461)：zstd 極快（某資料集約 1.4 GB/s），主要因為解碼器的實作和格式的設計。LZMA 用算術編碼，解碼很慢 [▶ 58:13](https://youtu.be/amv9LiGyY5s?t=3493)。解壓縮圖沒有分等級，因為不管用哪種匹配，解碼都一樣是從過去複製。

[▶ 58:53](https://youtu.be/amv9LiGyY5s?t=3533) 其他：Brotli（Google）、LZ4（Yann Collet，也是 zstd 的作者）、Snappy（Google）……每家都做自己的版本。

> **通用不等於完美** [▶ 58:53](https://youtu.be/amv9LiGyY5s?t=3533)：LZ77 只是**漸近**通用，你的資料是有限的。它不一定最適合你的資料；就算壓縮比最好，也可能太慢、太耗記憶體。而且 gzip 和 zstd 都是 LZ77，卻差很多 [▶ 1:00:04](https://youtu.be/amv9LiGyY5s?t=3604)。

[▶ 1:00:04](https://youtu.be/amv9LiGyY5s?t=3604) 沒講的：LZ78（EE376C 會詳講，課名「Universal Schemes in Information Theory」）、LZ77 的 repcodes、optimal parsing。都是好的期末專題題目 [▶ 1:00:40](https://youtu.be/amv9LiGyY5s?t=3640)。

---

## 12. 無損壓縮的實務建議

[▶ 1:01:12](https://youtu.be/amv9LiGyY5s?t=3672) 每個壓縮器我們都說它好、它某種意義下最佳。那實際上該怎麼想？

### 12.1 第一步：真的需要這些資料嗎？

[▶ 1:01:12](https://youtu.be/amv9LiGyY5s?t=3672) **先想能不能直接刪掉**。這真的很重要，大部分成本節省都來自「發現這 1 EB 資料不需要，刪掉」[▶ 1:01:51](https://youtu.be/amv9LiGyY5s?t=3711)。

- 也許不能全刪，但可以找出**哪些部分最花錢**。例：網頁伺服器 log，每行都有主機名稱（`10.1.1.12`），看起來很長，但每行都一樣，**熵幾乎是 0**，壓縮後不占位元 [▶ 1:02:28](https://youtu.be/amv9LiGyY5s?t=3748)；反而某個隨機的 request ID（`XYAZXXBDC`）看起來很短，卻很難壓 [▶ 1:03:00](https://youtu.be/amv9LiGyY5s?t=3780)。上過壓縮課就該問：ID 一定要這麼隨機嗎？要 64 位元組嗎？10 位元組夠不夠？能不能用遞增而不是隨機？
- [▶ 1:03:33](https://youtu.be/amv9LiGyY5s?t=3813) 法規或其他理由要保留資料，那就保留，但要認真想。
- **資料的存取模式** [▶ 1:03:33](https://youtu.be/amv9LiGyY5s?t=3813)：一年前的照片不會每天看，可以放便宜的冷儲存（cold storage），像電腦的快取階層一樣 [▶ 1:04:08](https://youtu.be/amv9LiGyY5s?t=3848)。
- 很多資料（**影片**是代表）做無損壓縮根本不實際，那是下半學期 [▶ 1:04:39](https://youtu.be/amv9LiGyY5s?t=3879)。

[▶ 1:04:39](https://youtu.be/amv9LiGyY5s?t=3879) 別灰心，壓縮不只為了儲存：它減少記憶體、頻寬，有時還讓查詢更快。

【口頭】[▶ 1:05:13](https://youtu.be/amv9LiGyY5s?t=3913) 這些聽起來像玩笑，但和業界的人談時，這正是懂壓縮的人能提供的獨特價值：很多人以為「這麼長一定很難壓」，你知道它熵是 0。

### 12.2 不要做的事

[▶ 1:05:45](https://youtu.be/amv9LiGyY5s?t=3945) 決定要無損儲存了，然後呢？**不要**：

- 覺得自己上過 EE274 很聰明，自己設計壓縮器（LZ77 + Huffman，或自己的 LLM）。
- 自己從頭用 Python 或 C 實作 LZ77 和熵編碼器 [▶ 1:06:22](https://youtu.be/amv9LiGyY5s?t=3982)。
- 上網搜一個很貴的壓縮器買授權。
- 只聽了一小段課：「LZ77 是通用的，gzip 是 LZ77，所以 gzip 一定完美」，用 gzip 預設值，因為大家都這樣 [▶ 1:07:06](https://youtu.be/amv9LiGyY5s?t=4026)。

這些都可能有道理，但不是第一步。

### 12.3 先了解你的應用

[▶ 1:07:06](https://youtu.be/amv9LiGyY5s?t=4026) 為什麼要壓縮？需要多快？多少記憶體？壓縮在哪裡發生：自己的機器還是別人的？開源還是公司內部？業餘專案還是要處理 GB 到 PB 的正式系統？用 CLI 還是函式庫（C、Python、Java……都有）[▶ 1:07:37](https://youtu.be/amv9LiGyY5s?t=4057)？

**資料是否同質** [▶ 1:08:18](https://youtu.be/amv9LiGyY5s?t=4098)：一大堆基因體資料 → 也許值得做專用壓縮器；雲端儲存服務，別人放什麼你不知道 → 用通用壓縮器（LZ）[▶ 1:08:52](https://youtu.be/amv9LiGyY5s?t=4132)。

### 12.4 看基準測試

[▶ 1:08:52](https://youtu.be/amv9LiGyY5s?t=4132) 拿一個語料（可以是你的資料或混合檔案），跑各種壓縮器的各種參數，畫圖 [▶ 1:09:24](https://youtu.be/amv9LiGyY5s?t=4164)。

壓縮速度 vs. 壓縮比（要往右上）：

- 要速度：**LZ4**，沒人接近，快好幾倍 [▶ 1:09:58](https://youtu.be/amv9LiGyY5s?t=4198)。
- 要極致壓縮：ZPAQ、CMIX 這種很慢但很強的。
- 中間：zstd；稍慢、壓得更好：bzip2、BSC。

【課堂討論】[▶ 1:10:31](https://youtu.be/amv9LiGyY5s?t=4231) 看這張圖，會選 gzip 而不選 zstd 嗎？zstd 每個等級都比 gzip 好（更好的 Pareto 前緣），因為想法類似但更現代。但 zstd 用比較多記憶體：在樹莓派或 1970 年代的電腦上可能要用 gzip，gzip 幾 KB 記憶體就能跑，zstd 至少要幾 MB [▶ 1:11:15](https://youtu.be/amv9LiGyY5s?t=4275)。

解壓縮速度：LZ4 又是贏家；zstd、Brotli 很快；gzip 慢一些但仍很快，因為都是 LZ77 [▶ 1:11:47](https://youtu.be/amv9LiGyY5s?t=4307)。

【Q&A】[▶ 1:11:47](https://youtu.be/amv9LiGyY5s?t=4307) 學生問 gzip 和 zstd 的記憶體用量。講者：zstd 預設視窗比較大。gzip 最大視窗講者記得是 32 KB 或 64 KB；zstd 可以加大到 GB，預設幾 MB [▶ 1:12:21](https://youtu.be/amv9LiGyY5s?t=4341)。所以 zstd 通常用幾十 MB，gzip 幾 MB 以下。多數應用今天都能接受 zstd 的記憶體用量。gzip 在格式裡把最大視窗寫死，無法增加；zstd 學到教訓，不設上限 [▶ 1:12:54](https://youtu.be/amv9LiGyY5s?t=4374)。zstd 也可以用很小的視窗跑在很少的記憶體上 [▶ 1:13:30](https://youtu.be/amv9LiGyY5s?t=4410)。

### 12.5 經驗法則

[▶ 1:13:30](https://youtu.be/amv9LiGyY5s?t=4410)（`L10.pdf`）

- **zstd**：解壓縮在任何等級都很快，等級很多，**應該第一個試**。除非有很好的理由（例如相容性：別人系統上沒有 zstd，只能寫 gzip），**不要用 gzip** [▶ 1:14:00](https://youtu.be/amv9LiGyY5s?t=4440)。
- 要更快：**LZ4**：匹配器很快，而且**不做熵編碼**，用固定位元數 [▶ 1:14:31](https://youtu.be/amv9LiGyY5s?t=4471)。
- 要更好、可以更慢（例如歸檔 10 年）[▶ 1:14:31](https://youtu.be/amv9LiGyY5s?t=4471)：
  - **LZMA 系**（7-Zip、xz）：LZ77 + 算術編碼（可做 context-based）。
  - **BWT 系**（bzip2、BSC）：Burrows–Wheeler 轉換，作業 3 會教。壓縮比 LZMA 快，但解壓縮比較慢（不再只是複製）[▶ 1:15:41](https://youtu.be/amv9LiGyY5s?t=4541)。
- 更吃資源：自己建模、做 context-based 編碼（PPMd 等；投影片註明這些不一定贏 LZ/BWT）。
- 完全不在乎時間：超強的那些。【口頭】這是今天的情況，五年後也許每台機器都有 GPU [▶ 1:16:12](https://youtu.be/amv9LiGyY5s?t=4572)。

### 12.6 把 zstd 用好

[▶ 1:16:12](https://youtu.be/amv9LiGyY5s?t=4572)

- 用最新的穩定版本。
- **選對等級**：1–19、負等級、19 以上的 ultra 等級，壓縮速度和壓縮比的取捨範圍很大 [▶ 1:16:45](https://youtu.be/amv9LiGyY5s?t=4605)。等級只是參數的特定組合，必要時可以自訂（視窗大小、hash 長度、最短匹配長度……）。
- 用 CLI 或你語言的函式庫（zstd 也支援多執行緒）。
- **重複使用 zstd 的 context 物件** [▶ 1:16:45](https://youtu.be/amv9LiGyY5s?t=4605)：常見錯誤是每壓一個檔就刪掉重建。壓很多小檔時重複使用能加速很多 [▶ 1:17:20](https://youtu.be/amv9LiGyY5s?t=4640)。
- **很小的檔案**（檔案內找不到好匹配）：用**字典壓縮**（dictionary compression），作業 3 的題目 [▶ 1:17:20](https://youtu.be/amv9LiGyY5s?t=4640)。

【Q&A】[▶ 1:17:52](https://youtu.be/amv9LiGyY5s?t=4672) 學生問：zstd 比 gzip 好，只是因為視窗比較大嗎？限制在 64 KB 還會比較好嗎？講者 [▶ 1:17:52](https://youtu.be/amv9LiGyY5s?t=4672)：不只。

1. 匹配位置和長度從 Huffman 換成 **tANS**，更接近算術編碼。
2. 匹配策略更進階，很多只在長視窗才有意義 [▶ 1:18:24](https://youtu.be/amv9LiGyY5s?t=4704)；gzip 只用簡單的雜湊匹配器。
3. **寫得更好**：編碼器、解碼器、格式都盡量減少迴圈，迴圈在現代硬體上很貴。

[▶ 1:19:02](https://youtu.be/amv9LiGyY5s?t=4742) 不要只想成「zstd 壓縮比較好」：同樣壓縮比時 zstd 更快，同樣速度時 zstd 檔案更小。這不是說 gzip 爛，它在 1990 年代是非常有效率的程式，只是今天不該用它了 [▶ 1:19:35](https://youtu.be/amv9LiGyY5s?t=4775)。

### 12.7 真的要自己做壓縮器之前

[▶ 1:19:35](https://youtu.be/amv9LiGyY5s?t=4775) 你有 EB 等級的資料或特殊應用（基因體），想做自己的壓縮器。先想：

- **有沒有空間**：建自己的機率模型估計熵，例如 zstd 給 100 KB，估計熵約 50 KB，才有改進空間 [▶ 1:20:15](https://youtu.be/amv9LiGyY5s?t=4815)。
- **專用的優勢** [▶ 1:20:15](https://youtu.be/amv9LiGyY5s?t=4815)：zstd 是通用的，要對任何資料都有效；你的只需處理一種（表格、基因、CSV），設計上有更多彈性。
- **封閉的生態系比較容易** [▶ 1:20:47](https://youtu.be/amv9LiGyY5s?t=4847)：如果有 100 個人用自己的工具讀壓縮檔，你一換格式，大家都壞了 [▶ 1:21:21](https://youtu.be/amv9LiGyY5s?t=4881)。
- **要有很強的理由** [▶ 1:21:21](https://youtu.be/amv9LiGyY5s?t=4881)：壓縮器要設計、實作、大量測試；要定**格式**（作業裡存浮點數那題就很難）；一旦發布 v1 就卡住了，改格式會讓別人的解碼器壞掉，要顧向下相容 [▶ 1:21:57](https://youtu.be/amv9LiGyY5s?t=4917)；要監控、修 bug（gzip 都 30 年了，去年還找到 bug）[▶ 1:22:30](https://youtu.be/amv9LiGyY5s?t=4950)；要支援 Java、C、Python……，新舊機器、各種架構和作業系統 [▶ 1:23:05](https://youtu.be/amv9LiGyY5s?t=4985)。

[▶ 1:23:05](https://youtu.be/amv9LiGyY5s?t=4985) 大公司常找得到值得的情況；如果壓縮就是你的產品，也可能值得。**基因體**就是例子：大量同類資料，確實做了專用壓縮器 [▶ 1:23:37](https://youtu.be/amv9LiGyY5s?t=5017)。但之後每個人都發論文稍微改進、而且不相容，結果沒人用：如果有一百萬種專用壓縮器，誰能互通？就像每個人都用自己的語言一樣 [▶ 1:23:37](https://youtu.be/amv9LiGyY5s?t=5017)。

[▶ 1:24:14](https://youtu.be/amv9LiGyY5s?t=5054) 去年有同學針對 MRI 資料做專題。有興趣的領域可以來談。

---

## 13. 一頁速查表

### 通用壓縮

- 定義：對任何平穩遍歷來源，$\frac1n\mathbb{E}[l(X^n)]\to H(\mathbf X)$，不需事先知道分布。
- 等價看法：$\hat p=2^{-l}$ 能逼近任何平穩分布。

### LZ77

| | 做法 |
|---|---|
| 解析 | 找最大 $k$ 使 $x[j:j+k]=x[i:i+k]$（$j<i$，可重疊）；輸出（字面值, 長度 $k$, 偏移 $i-j$） |
| 反解析 | 抄字面值；$l<o$ 整段複製，否則逐字元 `y.append(y[-o])` |
| 例 | `ABBABBABBCAB` → (AB,1,1)、(—,6,3)、(C,2,4) |
| 性質 | 很多種合法編碼共用一個解碼器；解碼只是複製，極快 |

### 通用性的直覺

- iid：$a$ 的平均間隔 $\frac1{P(a)}$。
- **Kac 引理**：$\mathbb{E}[R_n\mid x^n]=\frac1{p(x^n)}$ ⇒ 偏移 $\approx\frac1{p(x^n)}$ ⇒ 用 $\log\frac1{p(x^n)}$ 位元 ⇒ 期望 $H(X^n)$ ⇒ 熵率。
- 長度、字面值的成本可忽略；收斂慢，但真實資料的長重複讓它實務上很好。

### 實務旋鈕

| 旋鈕 | 取捨 |
|---|---|
| 視窗大小 | 大 → 壓得好、兩端都更耗記憶體；超過資料大小沒用 |
| hash 長度 | 短 → 候選多、慢、可能更好；長 → 錯過匹配 |
| 貪婪 / 懶惰 / 最佳解析 | 越後面越慢、越好 |
| 最短匹配長度 | 太小 → 一堆昂貴的短匹配；太大 → 一堆字面值 |
| 熵編碼 | Huffman（gzip）、tANS（zstd）、算術（LZMA）、不編（LZ4） |

整數用分箱：箱子編號熵編碼 + 箱內固定長度。

### 實務建議

1. 先問：要不要刪？哪部分最貴？存取模式？
2. 先試 **zstd**（選對等級、重用 context、小檔用字典）；要更快 LZ4；要更好 xz/7-Zip（LZMA）或 bzip2/BSC（BWT）。
3. gzip 只為相容性。
4. 自己做壓縮器：要有明顯的熵缺口、封閉生態系、大量資料、長期維護的覺悟。

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 影片無法實際做無損壓縮 ⇒ 有損壓縮 | 第 11 集起 |
| PNG（LZ77 系）、GIF（LZW） | 第 15 集影像壓縮（對照） |
| 有損壓縮常建在無損壓縮上（量化後再熵編碼） | 第 11、14–15 集 |
| BWT、字典壓縮 | 作業 3 |

> 以上對應是依播放清單標題和本集內容推估的，做到時再更新。

---

## 附：本集一句話總結

> **LZ77 不建模，只把重複片段換成（偏移, 長度）指標，解碼只是從過去複製，所以極快；依 Kac 引理，一個序列平均在 $\frac1{p}$ 個位置前出現過，偏移只要 $\log\frac1p$ 位元，所以它對任何平穩來源都漸近達到熵率（通用壓縮）。實作的差異在視窗、找匹配的策略和熵編碼：zstd 用更好的匹配器、tANS 和更適合現代硬體的寫法全面勝過 gzip。實務上先問能不能刪資料、找出最貴的部分，再先試 zstd，最後才考慮自己做壓縮器。**

---

*筆記依據 Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 10 錄影逐字稿（人工字幕，1:24:38）、投影片 L10、L10_ann 與 Cover & Thomas《Elements of Information Theory》2nd ed. §13.4–13.5 整理。*
