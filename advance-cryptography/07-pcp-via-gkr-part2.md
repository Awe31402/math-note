---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 07
lecture: Lecture 4 (Part 2) – PCP via GKR and Interactive Arguments
date: 待補（2023 秋季第四堂課，後段）
video: https://youtu.be/rdFIIHIjb7A
notes: Thaler §3.2（書頁 24，PDF 頁 25）、§4.5.5 末段（書頁 57，PDF 頁 58）、§9.2（書頁 135–137，PDF 頁 136–138）。OCW 本講無指定讀物。
---

# 第 07 集 · Lecture 4 (Part 2)：低次檢驗、PCP 的極限、論證與抗碰撞雜湊 [▶ 影片](https://youtu.be/rdFIIHIjb7A)

← 上一集：[06-pcp-via-gkr-part1](06-pcp-via-gkr-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[08-kilian-micali-part1](08-kilian-micali-part1.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 07 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:10:48，MIT 上傳的真人字幕）＋ Thaler §3.2、§4.5.5、§9.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 這個 PCP 是非適應性的](#1-這個-pcp-是非適應性的)
- [2. 低次檢驗](#2-低次檢驗)
  - [2.1 只能檢查「接近」低次](#21-只能檢查接近低次)
  - [2.2 直線檢驗](#22-直線檢驗)
  - [2.3 Q&A](#23-qa)
- [3. PCP 能做到多好](#3-pcp-能做到多好)
- [4. 資訊理論部分的收尾](#4-資訊理論部分的收尾)
  - [4.1 Reingold–Rothblum–Rothblum 與 500 美元的開放問題](#41-reingoldrothblumrothblum-與-500-美元的開放問題)
  - [4.2 為什麼還不夠](#42-為什麼還不夠)
- [5. 論證：計算可靠性](#5-論證計算可靠性)
- [6. Kilian–Micali 定理](#6-kilianmicali-定理)
  - [6.1 安全參數與可忽略函數](#61-安全參數與可忽略函數)
  - [6.2 定理的正式敘述](#62-定理的正式敘述)
  - [6.3 Q&A：作弊者比誠實證明者還弱？](#63-qa作弊者比誠實證明者還弱)
  - [6.4 Q&A：論證能用重複降低錯誤嗎](#64-qa論證能用重複降低錯誤嗎)
- [7. 抗碰撞雜湊函數族](#7-抗碰撞雜湊函數族)
- [8. 預告：局部打開與 Kilian 的想法](#8-預告局部打開與-kilian-的想法)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

1. 把第 06 集的 PCP 收尾：低次檢驗、PCP 的極限、資訊理論部分總結。
2. **進入密碼學**：論證（argument）的定義、Kilian–Micali 定理的敘述、抗碰撞雜湊函數族。

---

## 1. 這個 PCP 是非適應性的

[▶ 00:12](https://youtu.be/rdFIIHIjb7A?t=12)

驗證者的查詢是什麼？他表現得像 GKR 驗證者，也就是 sum-check 驗證者。sum-check 是 **public coin**：驗證者的訊息只是隨機數，不依賴證明者的回答。所以查詢位置只由隨機數決定，**不依賴查到的答案**。這就是非適應性。

---

## 2. 低次檢驗

### 2.1 只能檢查「接近」低次

[▶ 00:52](https://youtu.be/rdFIIHIjb7A?t=52)

證明者應該在 $H^m$ 上放證據 $w_0, w_1, \ldots$（不夠就補 0），然後寫下它在 $\mathbb{F}^m$ 上的低次擴張（每個座標次數 $\le |H| - 1$）。

**壞消息**：沒辦法真的檢查「這是低次多項式」。驗證者只能查少數幾點；證明者可以在某一點放壞的值，驗證者查不到就不知道。

**改成檢查「接近」低次**：通過檢驗後，保證（高機率）

$$\exists\ \text{低次的 } \tilde{W}\ \text{使得}\ \Pr_{z\leftarrow\mathbb{F}^m}\left[ V_0(z) = \tilde{W}(z) \right] \ge 1 - \varepsilon.$$

**為什麼這就夠了**：GKR 最後只在一個**隨機點** $z$ 查 $V_0$。查到「不一致的點」的機率只有 $\varepsilon$。所以可以假裝證明者放的是 $\tilde{W}$。
- 少數不一致的點：(1) 沒辦法偵測，不查就不知道那裡放什麼；(2) 也不在乎，因為高機率不會查到。

【Q&A】[▶ 07:58](https://youtu.be/rdFIIHIjb7A?t=478) **接近低次的多項式對應到一個證據嗎？**
對。取它接近的那個真正的低次 $\tilde{W}$，看它在 $H^m$ 上的值，就定義了一個證據。soundness 就是對這個證據論證。

### 2.2 直線檢驗

[▶ 05:07](https://youtu.be/rdFIIHIjb7A?t=307)

學生建議隨機抽樣。低次檢驗有很多種，常見的一種：

1. 在 $\mathbb{F}^m$ 裡隨機選一條**直線** $\ell(t) = a + tb$。
2. $V_0$ 限制在直線上應該是單變數多項式，次數 $\le m(|H| - 1)$（每個座標次數 $|H| - 1$，共 $m$ 個座標，所以總次數 $\le m(|H|-1)$）。
3. 查直線上 $m(|H| - 1) + 1$ 個點，插值出一個多項式，再查一個額外的點檢查是否一致。或者乾脆把整條線讀完：$|\mathbb{F}|$ 只有 polylog，用插值檢查是不是低次。不是就拒絕。

**還要證明的**：「隨機直線上和低次多項式一致」⟹「整體接近某個低次多項式」。這是一大步。【口頭】「我有一個好作業題目跟這有關。」

> 【課本補充】Thaler §9.2 Remark 9.4：用 PCP 造簡短論證時，看起來不需要低次檢驗，但其實低次檢驗只是被「推進 PCP 裡面」了；短 PCP 本身通常基於低次多項式，也會用到低次檢驗。Thaler 指出短 PCP 常用**單變數**低次多項式（Reed–Solomon 碼），所以它們的低次檢驗針對單變數；而互動式證明和 MIP 通常基於**多變數**低次多項式（Reed–Muller 碼）。

### 2.3 Q&A

【Q&A】[▶ 08:39](https://youtu.be/rdFIIHIjb7A?t=519) **3SAT 的電路很特別（一個大 AND 加很多小 OR），不需要用一般的 GKR，可以更直接吧？**
「100% 對。」講者展示的是一個可行性結果。實際用的 GKR 有很多最佳化，很多是在電路層級：怎麼算術化最有效率、怎麼產生電路。現在 GKR 的證明者能做到準線性，甚至線性（新的工作，她還沒時間細看）。

【Q&A】[▶ 14:57](https://youtu.be/rdFIIHIjb7A?t=897) **因為低次檢驗，現在還有完美 completeness 嗎？**
有。誠實的證明者給真的 $\tilde{w}$，任何直線上都是低次，一定通過。損失的是 **soundness**：證明者可能稍微作弊而沒被抓到，所以 soundness 要留一點空間吃掉這部分。

【Q&A】[▶ 15:39](https://youtu.be/rdFIIHIjb7A?t=939) **要降低錯誤時，要重做整個 PCP 嗎？**
不用。PCP 不變，**驗證者用新的隨機數再跑 $k$ 次**。每次獨立地有 1/2 機率拒絕，被騙的機率變成 $2^{-k}$。證明者不參與重複。

---

## 3. PCP 能做到多好

[▶ 10:45](https://youtu.be/rdFIIHIjb7A?t=645)

（以下都是在**完美 completeness**、**常數 soundness** 下。）

- **3 次查詢是最好的**，不能更少。
- 從 polylog 查詢到 3 次：先遞迴降到 $\log\log n$ 次，再對這個小 PCP 套一個**指數大小**、只要 3 次查詢的 PCP。
- **2 個位元不行**。直覺上的理由：**2SAT 是容易的**。（講者說也許出成作業。）
- 但如果每次查詢回答的是一個**區塊**（一個 polylog 位元的「字」，而不是一個位元），**2 次查詢**可以做到。（1 次查詢、回答整個證據，太簡單；她不確定 1 次 + polylog 區塊行不行，應該不行。）

【Q&A】[▶ 13:35](https://youtu.be/rdFIIHIjb7A?t=815) 學生指出：如果允許**不完美的 completeness**（$1 - \varepsilon$），2 個位元就可以。講者同意：「你說得對，我講的都是完美 completeness。」學生說參數大約是 2/3 對 1/3。

【Q&A】[▶ 14:57](https://youtu.be/rdFIIHIjb7A?t=897) **「區塊」是連續的位元嗎？** 把 PCP 想成一個字一個字，每個字 polylog 位元，可以讀第 $i$ 個字和第 $j$ 個字。

【Q&A】[▶ 17:04](https://youtu.be/rdFIIHIjb7A?t=1024) 兩次查詢結果的出處？講者說會放在 Canvas 上。
- ⚠️ 待確認：2 次查詢（區塊）PCP、2 位元不完美 completeness 的確切出處和參數，課堂上沒給。

---

## 4. 資訊理論部分的收尾

[▶ 17:04](https://youtu.be/rdFIIHIjb7A?t=1024)

沒講到的：3 次查詢的 PCP（遞迴、Hadamard 碼等技巧）；**多證明者互動式證明**（MIP，和 PCP 本質上等價，可能出成作業）。

### 4.1 Reingold–Rothblum–Rothblum 與 500 美元的開放問題

[▶ 17:48](https://youtu.be/rdFIIHIjb7A?t=1068)

【口頭】Reingold、Rothblum、Rothblum 有一個「非常、非常漂亮」的結果（2016 年開始，現在版本標 2018）。

**問題**：GKR 給了**有界深度**計算的雙重有效證明。能不能給**有界空間**計算雙重有效證明？

- 不可能超過 PSPACE（IP = PSPACE）。
- 深度和空間可以互換，但**互換不保持效率**：把一個多項式大小、有界深度的電路轉成有界空間的計算，計算時間可能變成指數。

> **開放問題**：對任何時間 $T$、空間 $S$ 的計算，找一個互動式證明，使得
> - 證明者時間 $\mathrm{poly}(T)$；
> - 驗證者時間 $|x|\cdot\mathrm{poly}(S)$（不依賴 $T$）；
> - 通訊量 $\mathrm{poly}(S)$（要加 $|x|$ 也行）。

**RRR 做到了幾乎這樣**，但驗證者時間和通訊量多了一個 $T^{\varepsilon}$ 因子（$S\cdot T^{\varepsilon}$），而且 $\varepsilon$ 必須是**常數**（通訊量大約隨 $2^{\tilde{O}(1/\varepsilon)}$ 成長）。所以若 $T$ 是超多項式，驗證者就不有效率了；這其實是針對 P 的結果。

【口頭】「我拜託你們這些聰明的 MIT、哈佛、BU、Northeastern 學生，這是私人請求。」除了大概能拿 ACM 博士論文獎之外，**講者提供 500 美元獎金**給把 $T^{\varepsilon}$ 拿掉的人。學生：「你出價比〔某人〕高。」（那人好像只給了 15 美元之類的假獎金。）

> 【課本補充】Thaler §4.5.5 末段：用組態圖矩陣乘冪做的小空間 IP，證明者總得花至少 $N\ge 2^{s}$ 時間（要探索所有組態），即使機器實際只跑很短時間。[RRR16] 給了一個很不一樣的 IP 避開這個低效率（針對 P），而且只要**常數回合**。

### 4.2 為什麼還不夠

[▶ 24:44](https://youtu.be/rdFIIHIjb7A?t=1484)

資訊理論的世界：我們被困在 PSPACE；驗證可以很有效率，但證明很長（PCP）。

**PCP 一定要「真的寫下來」**（[▶ 25:28](https://youtu.be/rdFIIHIjb7A?t=1528)）：如果 PCP 沒寫在某處，驗證者只是跟證明者說「我知道你有一份 PCP，給我位置 $i, j, k$」，作弊的證明者會**看完所有位置再決定答案**：問 $(i, j, k)$ 時在 $i$ 放 0，問 $(i, j', k')$ 時在 $i$ 放 1。PCP 的 soundness 依賴「第 $i$ 格的答案不能依賴其他查詢」。

**我們真正想要的**：拿一份證明（證據），把它**縮小**，放在某個地方給全世界看。

| 模型 | 問題 |
|---|---|
| 互動式證明 | 一對一：我可以跟 Tina、Sue、Leo 各自互動，但沒辦法給全世界一份證明 |
| PCP | 可以公開貼出來，但**很大** |

「用密碼學的魔法，我們可以得到這些。」

---

## 5. 論證：計算可靠性

[▶ 27:34](https://youtu.be/rdFIIHIjb7A?t=1654)

**計算可靠的證明**（computationally sound proof），也叫**論證**（argument）。和證明只差在 soundness：

> **計算 soundness**：對任何**計算受限**的證明者 $P^{*}$ 和任何 $x\notin L$，$\Pr\left[ \langle P^{*}, V\rangle(x) = 1 \right]$ 很小（通常要求可忽略）。

Completeness 不變。

【口頭】為什麼可以這樣放寬：何必在乎有一個跑 $2^{1000}$ 時間的證明者能作弊？「宇宙裡沒有那麼多分子。」只考慮時間有界的證明者，就可以用**密碼學**：假設證明者破解不了某個密碼學難題。「整個新世界就打開了。」

【Q&A】[▶ 31:13](https://youtu.be/rdFIIHIjb7A?t=1873) **對 $x$ 有分布嗎？** 沒有，還是對**每個** $x$。

【Q&A】[▶ 31:58](https://youtu.be/rdFIIHIjb7A?t=1918) **作弊的證明者不能把某個假命題的假證明「背」起來嗎？**
對，所以**非互動**的計算可靠證明不存在：假證明存在（只是難找），非一致的證明者可以把一個 $x\notin L$ 和它的假證明直接寫死在電路裡。

「但我們**幾乎**有。」做法：假設一個**共同參考字串**（common reference string），例如大家同意用某個雜湊函數。它是萬用的、不依賴 $x$。作弊者要找出假證明，就得破解這個雜湊函數。

> 【課本補充】Thaler §3.2 Definition 3.2：argument system 是只要求 soundness 對多項式時間證明者成立的互動式證明。這叫 computational soundness；Definition 3.1 的叫 statistical（或 information-theoretic）soundness。論證由 Brassard、Chaum、Crépeau 1986 年提出。

---

## 6. Kilian–Micali 定理

[▶ 34:45](https://youtu.be/rdFIIHIjb7A?t=2085)

> **定理（Kilian 1992；Micali 1994）**：假設**抗碰撞雜湊函數族**（collision-resistant hash family, CRH）存在。則每個 NP 語言都有一個**簡短的 4 則訊息論證系統**。

【口頭】「這些結果奠定了這個領域的基礎。」想法：拿一個很長、但能有效率檢查的 PCP，用密碼學把它「縮進一個小盒子」送給驗證者，再說服驗證者盒子裡是一個會被接受的證明。

### 6.1 安全參數與可忽略函數

[▶ 37:13](https://youtu.be/rdFIIHIjb7A?t=2233)

- **安全參數** $\lambda$：直覺上「$\lambda$ 位元的安全性」代表跑 $2^{\lambda}$ 左右時間的人破解不了。實務上設成 128 或 256；理論上當作參數。
- 資訊理論的安全是說「不管多強，機率都是 $\varepsilon$」；密碼學的安全通常是對**時間**設限，而且要求錯誤是**可忽略**的。

> **可忽略**（negligible）：$\mu(\lambda)$ 可忽略，若對每個多項式 $p$，存在 $\lambda^{*}$，使得對所有 $\lambda > \lambda^{*}$，$\mu(\lambda) < 1/p(\lambda)$。也就是比任何 $1/\mathrm{poly}$ 都快趨近 0。

### 6.2 定理的正式敘述

[▶ 39:23](https://youtu.be/rdFIIHIjb7A?t=2363)

| 性質 | 內容 |
|---|---|
| 訊息數 | 4 |
| 證明者時間 | $\mathrm{poly}(n, \lambda)$（給定 $x$ 和證據 $w$） |
| 驗證者時間 | $\mathrm{poly}(\lambda)$ ＋ 讀 $x$ ＋ PCP 驗證者的時間（例如 polylog） |
| Completeness | 對每個 $x\in L$、證據 $w$、每個 $\lambda$：$\Pr\left[ \langle P(w), V\rangle(x, 1^{\lambda}) = 1 \right] = 1$ |
| Soundness | 對每個大小 $\mathrm{poly}(\lambda)$ 的 $P^{*}$、每個 $x\notin L$：$\Pr\left[ \langle P^{*}, V\rangle(x, 1^{\lambda}) = 1 \right]\le\mathrm{negl}(\lambda)$ |

- 【Q&A】[▶ 40:12](https://youtu.be/rdFIIHIjb7A?t=2412) 證明者拿到的是 $x$ 和證據 $w$（講者補上）。
- 【Q&A】[▶ 43:51](https://youtu.be/rdFIIHIjb7A?t=2631) **「大小」是什麼意思？** 密碼學通常允許攻擊者是**非一致的**（可以有 advice），所以用多項式大小的**電路**來建模。說「大小 $\mathrm{poly}(\lambda)$」就是「跑 $\mathrm{poly}(\lambda)$ 時間，但可以有固定的 advice」。

### 6.3 Q&A：作弊者比誠實證明者還弱？

【Q&A】[▶ 44:31](https://youtu.be/rdFIIHIjb7A?t=2671) **如果 $\lambda$ 比 $|x|$ 小，作弊的證明者連 $x$ 都讀不完？**

講者說這是定義裡她「略過」的微妙處：

- 作弊者可以跑任何 $\mathrm{poly}(\lambda)$ 時間，所以只要 $|x|\le\lambda^{100}$ 之類的，他就讀得完。
- 但如果想要通訊量 $\mathrm{polylog}(n)$，$\lambda$ 就得是 $\mathrm{polylog}(n)$，這時作弊者連 $x$ 都讀不完。
- 解法：用**更強的假設**。假設大小 $2^{\lambda^{\varepsilon}}$ 的攻擊者也破解不了（**次指數**假設）。這樣 $\lambda = \mathrm{polylog}(n)$ 時，攻擊者仍可以跑 $\mathrm{poly}(n)$ 時間。
- 「多項式假設」（$\mathrm{poly}(\lambda)$ 時間破解不了）是標準、保守的；次指數假設比較強，看你願意冒多少險。

**怎麼想才對**（[▶ 49:33](https://youtu.be/rdFIIHIjb7A?t=2973)）：設定「作弊者最多跑 $\mathrm{poly}(\lambda)$」，等於說**這個世界裡沒有人能跑更久**。如果有人能，計算受限就沒意義了。所以大於那個的 $x$ 其實也沒有誠實證明者能處理。「這是關於世界的假設，對真實世界攻擊者合理時間的上界。」

【Q&A】[▶ 51:35](https://youtu.be/rdFIIHIjb7A?t=3095) **誠實證明者多了 $\mathrm{poly}(n)$，是因為他要處理證據？** 對：他要讀 $x$、讀證據、產生 PCP……

### 6.4 Q&A：論證能用重複降低錯誤嗎

【Q&A】[▶ 52:17](https://youtu.be/rdFIIHIjb7A?t=3137)

- **循序重複**：可以，錯誤從 $s$ 降到 $s^k$，跟預期一樣。
- **平行重複**（同時跑 $k$ 份、各用新的隨機數）：對互動式**證明**有效，錯誤指數下降。對**論證**曾是開放問題；後來有人給出反例：存在一個互動式論證，平行重複後 **soundness 完全不下降**。反例很刻意，但說明「一般而言不成立」。
- 後來有人證明可以用比較聰明的方式平行重複：加一個奇怪的「以某個機率中止」（abort）的條件，soundness 就會下降。
- 「簡短的回答：很複雜。」所以密碼學裡通常直接寫 completeness 1（或 $1 - \mathrm{negl}$）、soundness $\mathrm{negl}$。

- ⚠️ 逐字稿缺字：反例作者字幕寫「Baioumy, Meo, and two other people」，加 abort 技巧的人字幕寫「[Tak?]」，講者自己也說記不清（見待確認清單）。

---

## 7. 抗碰撞雜湊函數族

[▶ 56:26](https://youtu.be/rdFIIHIjb7A?t=3386)

> **定義（Collision-Resistant Hash Family）**：$\mathcal{H}$ 由兩個演算法組成：
> - $\mathrm{Gen}(1^{\lambda})\to hk$：PPT，產生雜湊金鑰 $hk$（長度 $\mathrm{poly}(\lambda)$）。
> - $\mathrm{Eval}(hk, x)\to v\in\{0,1\}^{\lambda}$：多項式時間，$x\in\{0,1\}^{*}$。
>
> **抗碰撞**：對每個大小 $\mathrm{poly}(\lambda)$ 的攻擊者 $A$，存在可忽略函數 $\mu$，使得對所有 $\lambda$：
> $$\Pr_{hk\leftarrow\mathrm{Gen}(1^{\lambda})}\left[ (x, x')\leftarrow A(hk):\ x\neq x' \ \wedge\ \mathrm{Eval}(hk, x) = \mathrm{Eval}(hk, x') \right] \le \mu(\lambda).$$

- **$1^{\lambda}$**（一進位）：密碼學的小技巧。「我說『1 的安全參數次方』時覺得自己像白痴。」演算法的時間是對輸入長度的多項式；把 $\lambda$ 用一進位寫，「多項式時間」就自然是 $\mathrm{poly}(\lambda)$。
- **重點是壓縮**：輸入可以是任意長（或 $2\lambda$、$\lambda + 1$ 位元，定義方式很多），輸出 $\lambda$ 位元。
- 碰撞一定**存在**（鴿籠原理），要求的是**難找**。
- 【Q&A】[▶ 62:53](https://youtu.be/rdFIIHIjb7A?t=3773) 多項式大小是對 $\lambda$ 的多項式。

【Q&A】[▶ 60:00](https://youtu.be/rdFIIHIjb7A?t=3600) **金鑰可以是空字串嗎？為什麼需要金鑰？**
這是**建模**問題：
- 如果攻擊者是**非一致**的（有 advice），沒有金鑰的話，他可以把一組碰撞 $(x, x')$ 直接當 advice 帶著，輸出就好。所以非一致模型**必須有金鑰**。
- 如果攻擊者是**一致**的（uniform，只有常數大小的描述），就可以不要金鑰：小的輸入讓它們不碰撞，大的碰撞他「肚子裡裝不下」。理論密碼學文獻裡有研究**無金鑰雜湊**，但要搭配一致攻擊者。
- 最標準的是非一致攻擊者＋有金鑰。
- 【口頭】實務上用的雜湊函數（例如 SHA-256）某種意義上沒有金鑰，是固定的。「實務是另一回事。」

---

## 8. 預告：局部打開與 Kilian 的想法

[▶ 65:40](https://youtu.be/rdFIIHIjb7A?t=3940)

定理真正需要的是**有局部打開的雜湊**（hash with local opening），但它可以從 CRH 造出來，所以假設只寫 CRH。

**局部打開**：我雜湊了一個很長的值 $x$，給你 $v$。我不想給你整個 $x$（太大，你讀不完），只想證明「$x$ 的第 $i$ 位是 0」。多兩個演算法：
- $\mathrm{Open}$：產生一個小證明，說第 $i$ 位是某個值；
- $\mathrm{Verify}$：檢查這個小證明。

（正式定義下次講。）

**Kilian 的想法**（[▶ 68:33](https://youtu.be/rdFIIHIjb7A?t=4113)）：

1. 證明者算出巨大的 PCP，把它**雜湊**，只把雜湊值送給驗證者。
2. 驗證者表現得像 PCP 驗證者：產生隨機數，決定要看 PCP 的位置 $i_1, \ldots, i_{\ell}$，送給證明者。
3. 證明者回答 $b_1, \ldots, b_{\ell}$，每個附上局部打開的證明。
4. 驗證者檢查打開都正確，而且 PCP 驗證者接受。

「把 PCP 和這種能把 PCP 壓成小東西、又能只打開特定位置的密碼學技術結合起來，就是這樣。」

> 【課本補充】Thaler §9.2：Kilian [Kil92] 證明任何 PCP 加上 Merkle 雜湊，就得到 NP 的 4 則訊息論證系統（假設 CRH 存在）。證明者、驗證者時間和 PCP 差不多，通訊量是每次 PCP 查詢 $O(\log n)$ 個雜湊值。分成 commit 和 reveal 兩階段：commit 時證明者把 PCP 當葉子建 Merkle 樹，送樹根；reveal 時驗證者模擬 PCP 驗證者決定查詢，證明者回傳答案和驗證路徑（authentication path）。Soundness：Merkle 樹把證明者**綁**在一個固定的字串 $\pi'$ 上，每個位置最多只能成功打開成一個值，否則就找到了碰撞。Micali [Mic00] 再對這個 4 則訊息協定套用 Fiat–Shamir，得到隨機預言機模型下的非互動簡短論證。

---

## 9. 一頁速查表

### 低次檢驗

- 只能保證：$\exists$ 低次 $\tilde{W}$，$\Pr_z[V_0(z) = \tilde{W}(z)]\ge 1 - \varepsilon$。夠用，因為 GKR 最後只在隨機點查 $V_0$。
- 直線檢驗：隨機直線上，限制應是 $\le m(|H|-1)$ 次的單變數多項式；讀整條線（$|\mathbb{F}|$ 個點）用插值檢查。
- 完美 completeness 保留；soundness 多吃一點。
- 降低錯誤：PCP 不變，驗證者用新隨機數重跑 $k$ 次 → $2^{-k}$。

### PCP 的極限（完美 completeness、常數 soundness）

- 3 個位元是最少的；2 個位元不行（2SAT 容易）。
- 2 次查詢、每次回答一個 polylog 位元的區塊：可以。
- 不完美 completeness：2 個位元可以。

### 開放問題（500 美元）

時間 $T$、空間 $S$：證明者 $\mathrm{poly}(T)$，驗證者 $|x|\cdot\mathrm{poly}(S)$，通訊 $\mathrm{poly}(S)$。RRR 差一個 $T^{\varepsilon}$（常數 $\varepsilon$）。

### 論證

- 計算 soundness：$\forall$ 大小 $\mathrm{poly}(\lambda)$ 的 $P^{*}$，$\forall x\notin L$，$\Pr[\text{接受}]\le\mathrm{negl}(\lambda)$。
- 非互動論證沒有共同參考字串就不可能（非一致作弊者可寫死假證明）。
- 可忽略：$\forall p$，$\exists\lambda^{*}$，$\lambda > \lambda^{*}\Rightarrow\mu(\lambda) < 1/p(\lambda)$。
- polylog 通訊需要次指數假設（$2^{\lambda^{\varepsilon}}$ 大小也破解不了）。
- 論證：循序重複有效；天真平行重複可能無效。

### Kilian–Micali

CRH ⟹ NP 有 4 則訊息簡短論證：證明者 $\mathrm{poly}(n, \lambda)$，驗證者 $\mathrm{poly}(\lambda)$ ＋ PCP 驗證者。

### CRH

$\mathrm{Gen}(1^{\lambda})\to hk$；$\mathrm{Eval}(hk, x)\to\{0,1\}^{\lambda}$；$\Pr[A(hk)$ 找到碰撞$]\le\mathrm{negl}$。非一致攻擊者 ⟹ 需要金鑰。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 有局部打開的雜湊（Merkle 樹） | 第 08 集：定義與構造 |
| Kilian–Micali 協定 | 第 08–09 集：協定與分析 |
| 共同參考字串、非互動 | 第 10–13 集：Fiat–Shamir |
| 次指數假設 | 第 08 集起的參數設定 |

---

## 附：本集一句話總結

> **PCP 收尾：證據的擴張只能檢查「接近低次」，但 GKR 只查隨機點所以夠用；資訊理論的證明不是一對一、就是太長，所以放寬成只防計算受限作弊者的「論證」——有了抗碰撞雜湊，Kilian–Micali 就能把巨大的 PCP 壓成一個雜湊值，再只打開驗證者要查的幾個位置。**

---

## ⚠️ 待確認清單

1. [▶ 17:04](https://youtu.be/rdFIIHIjb7A?t=1024) 2 次查詢（區塊）PCP、2 位元不完美 completeness PCP 的出處和確切參數，課堂沒給（講者說會放在 Canvas）。
2. [▶ 53:38](https://youtu.be/rdFIIHIjb7A?t=3218) 「論證的平行重複不一定降低錯誤」的反例作者（字幕「Baioumy, Meo, and two other people」），以及「加 abort 條件就能平行重複」的作者（字幕「[Tak?]」），講者自己也說記不清。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 4 Part 2 錄影逐字稿（MIT 真人字幕，1:10:48）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§3.2、§4.5.5、§9.2 整理。*
