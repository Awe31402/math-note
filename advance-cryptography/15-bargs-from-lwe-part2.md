---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 15
lecture: Lecture 8 (Part 2) – Succinct Non-Interactive Arguments for Batch NP (BARGs) from LWE
date: 待補（2023 秋季，感恩節後第一堂，後段）
video: https://youtu.be/p60ShJrbrf8
notes: OCW 本講無指定讀物。相關論文未取得，只依逐字稿。
---

# 第 15 集 · Lecture 8 (Part 2)：索引 BARG——遞迴、二合一、快速線上驗證的 PCP、半適應性 soundness [▶ 影片](https://youtu.be/p60ShJrbrf8)

← 上一集：[14-bargs-from-lwe-part1](14-bargs-from-lwe-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[16-bargs-to-snargs-part1](16-bargs-to-snargs-part1.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 15 集
> **講者**：**Zhengzhong Jin**（客座）
> **來源**：YouTube 錄影逐字稿（1:14:14，MIT 上傳的真人字幕）。**本集沒有次要來源**。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：字幕把「SSB」常聽成「SSV」、「construction」聽成「contraction」、「third-round」聽成「Celeron」等，筆記直接改正。符號沿用第 14 集筆記。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 補充：需要哪種 CI 雜湊](#1-補充需要哪種-ci-雜湊)
- [2. 第一版 BARG 的成本與問題](#2-第一版-barg-的成本與問題)
- [3. 索引 BARG](#3-索引-barg)
  - [3.1 定義](#31-定義)
  - [3.2 主定理](#32-主定理)
  - [3.3 索引 BARG ⟹ 一般 BARG](#33-索引-barg--一般-barg)
- [4. 構造索引 BARG：把第三則訊息委託出去](#4-構造索引-barg把第三則訊息委託出去)
  - [4.1 想法：遞迴](#41-想法遞迴)
  - [4.2 讓證據變小：有局部打開的 SSB](#42-讓證據變小有局部打開的-ssb)
  - [4.3 有局部打開的 SSB 雜湊](#43-有局部打開的-ssb-雜湊)
  - [4.4 二合一技巧：讓遞迴會結束](#44-二合一技巧讓遞迴會結束)
  - [4.5 問題：電路每層變兩倍](#45-問題電路每層變兩倍)
  - [4.6 快速線上驗證的 PCP](#46-快速線上驗證的-pcp)
- [5. 半適應性 soundness](#5-半適應性-soundness)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

接續第 14 集：
1. 第一版 BARG 的證明長度和驗證時間還太大。
2. 定義**索引 BARG**（index BARG），它沒有「驗證者要讀全部實例」的下界。
3. 用**遞迴**＋**二合一**＋**快速線上驗證的 PCP** 造出證明長度和驗證時間都是 polylog 的索引 BARG。
4. 安全性需要**半適應性 soundness**（下一集也要用）。

---

## 1. 補充：需要哪種 CI 雜湊

[▶ 00:13](https://youtu.be/p60ShJrbrf8?t=13)

第 14 集的證明需要對關係 $R$（「萃取出的第 $i^{*}$ 列 PCP 被 $Q$ 接受」）的 CI 雜湊。這來自另一篇工作：**對「可有效率驗證的乘積關係」的 CI 雜湊**，在平行重複的意義下，幾乎能處理所有稀疏關係。講者不細講。
- ⚠️ 待確認：作者字幕是 `[INAUDIBLE]`／「HR」，確切出處不確定。
- 【課本補充】Thaler §5.2 說 [PS19, HLR21] 在 LWE 下替各種自然的 IP 和論證造出 CI 雜湊族。[HLR21] 是 Holmgren、Lombardi、Rothblum〈Fiat-Shamir via list-recoverable codes (or: parallel repetition of GMW is not zero-knowledge)〉（STOC 2021）。字幕的「HR」可能指這篇，但 Thaler 沒有提到「乘積關係」，所以還不能確定。

【Q&A】[▶ 00:56](https://youtu.be/p60ShJrbrf8?t=56) **為什麼上週（第 13 集）的 CI 雜湊不夠？**
上週的是**可搜尋**關係：每個 $\alpha$ 最多一個 $\beta$，而且能有效率地算出來。這裡固定一個 PCP，可能有**很多個**查詢都讓它被接受，不是唯一的。那篇工作顯示：若稀疏關係有有效率的**驗證**演算法（能檢查 $(\alpha, \beta)\in R$），在平行重複的意義下就能造 CI 雜湊。

---

## 2. 第一版 BARG 的成本與問題

[▶ 03:04](https://youtu.be/p60ShJrbrf8?t=184)

| 部分 | 大小 |
|---|---|
| 第一則訊息 $h_1, \ldots, h_{\ell}$ | 每個是一個密文 $\mathrm{poly}(\lambda)$，共 $\mathrm{poly}(|C|, \lambda)$，**和 $k$ 無關** |
| 第三則訊息（打開的欄） | $k\cdot|Q| = k\cdot\lambda\cdot\mathrm{polylog}(|C|)$ |

- 已經不平凡：第一項約 $|C|$，第二項約 $k$，遠小於 $k\cdot|w|$。
- 【Q&A】[▶ 05:18](https://youtu.be/p60ShJrbrf8?t=318) 為什麼有 $\lambda$？因為平行重複 $\lambda$ 次放大 soundness。完美 completeness 的 PCP 在平行重複時不用擔心 completeness。

**大問題：驗證時間 $k\cdot\mathrm{poly}(|C|)$**：驗證者要對每個 $x_i$ 跑 PCP 驗證，每個要 $|C|$ 時間。直接這樣做，驗證時間**完全沒有省**。

**一般 BARG 的下界**（[▶ 06:43](https://youtu.be/p60ShJrbrf8?t=403)）：驗證者至少要讀 CRS 和**所有實例**，所以驗證時間至少 $k\cdot|x|$。

---

## 3. 索引 BARG

### 3.1 定義

[▶ 07:27](https://youtu.be/p60ShJrbrf8?t=447)

考慮實例是**一致的**（uniform）特殊情形：存在一個電路 $U$，第 $i$ 個實例是 $x_i = U(i)$。

那麼「所有 $x_i\in L$」等價於：對每個 $i$，存在 $w_i$ 使 $C(U(i), w_i) = 1$。把它看成一個新的 NP 關係，**實例就是索引 $i$**，驗證電路 $C'(i, w_i) := C(U(i), w_i)$。

> **索引 BARG**（index BARG，也叫 batch index 的 SNARG）：對這種語言的 BARG。
> - 證明者要說服驗證者 $1, 2, \ldots, k$ 都在 $L$ 裡；誠實證明者有 $w_1, \ldots, w_k$。
> - **驗證者只拿到 $k$**（$\log k$ 位元）。
> - Completeness、soundness 和之前一樣。

【課堂討論】[▶ 12:40](https://youtu.be/p60ShJrbrf8?t=760) 最好能希望的驗證時間？驗證者只要讀 $k$ 和證明，所以可以只有 $\mathrm{poly}(\log k, \lambda)$。

【Q&A】[▶ 13:21](https://youtu.be/p60ShJrbrf8?t=801) **$U$ 怎麼想？** 可以吸收進關係電路裡。驗證時間其實也依賴 $C$，因為驗證者要讀電路。學生：$C$ 算輸入嗎？看怎麼定義：可以對固定的 $C$ 定義證明系統，或對任意 $C$ 定義（那驗證時間要隨 $|C|$ 成長）。學生：固定 $C$ 好像沒什麼用？可以選 $C$ 為萬用電路，那就很一般。講者說「把 $C$ 當成輸入比較好」。

### 3.2 主定理

[▶ 15:24](https://youtu.be/p60ShJrbrf8?t=924)

> **定理**：從 **LWE** 可以造出索引 BARG，
> - 證明長度 $\mathrm{poly}(\log k, \log|C|, \lambda)$；
> - 驗證時間 $\mathrm{poly}(\log k, |C|, \lambda)$。

兩者都幾乎達到最好的可能（差多項式）。（字幕寫驗證時間「log K C lambda」；依上下文驗證者要讀電路 $C$，對 $|C|$ 是多項式。）

### 3.3 索引 BARG ⟹ 一般 BARG

[▶ 16:15](https://youtu.be/p60ShJrbrf8?t=975)

【口頭】「批次的實例，某種意義上不失一般性都是一致的。」

給一般實例 $x_1, \ldots, x_k$：

1. 證明者對所有實例建 **Merkle 樹**，把樹根 $h$ 送給驗證者。
2. 定義新的索引關係：對每個 $i$，存在局部打開 $\rho_i$ 和證據 $w_i$ 使
   - $\mathrm{Merkle.Verify}(h, i, x_i, \rho_i) = 1$（$x_i$ 確實是第 $i$ 片葉子）；
   - $C(x_i, w_i) = 1$。
   也就是電路 $C'_h(i, (x_i, \rho_i, w_i))$。
3. 對 $C'_h$ 和索引 $1, \ldots, k$ 產生索引 BARG $\pi$，送 $(h, \pi)$。

驗證者：算出 $h$（讀全部實例，$k\cdot|x|$，這是**前處理**），再驗證 $\pi$（**線上**，很快）。$h$ 和 $\pi$ 都小，所以證明也小。

**soundness 不是顯然的**（[▶ 21:41](https://youtu.be/p60ShJrbrf8?t=1301)）：電路 $C'_h$ **依賴 $h$**，而 $h$ 是作弊者**適應性地**選的（看了 CRS 之後）。之前的非適應性 soundness 不夠。（見第 5 節。）

---

## 4. 構造索引 BARG：把第三則訊息委託出去

### 4.1 想法：遞迴

[▶ 22:24](https://youtu.be/p60ShJrbrf8?t=1344)

第一版：第一則訊息小（只依賴 $|C|$），第三則訊息大。索引 BARG 裡實例就是 $1, \ldots, k$。

**想法**：不送第三則訊息。證明者手上有被打開的欄，但**自己做驗證**，再**證明**驗證是對的。也就是跑另一個 SNARG，證明以下語言：

> 存在欄 $\{\mathrm{col}_q\}_{q\in Q}$ 使得
> 1. 對每個 $q\in Q$：$h_q = \mathrm{SSB}(\mathrm{col}_q)$（雜湊和第一則訊息一致）；
> 2. 對每個 $i\in[k]$：$V_{\mathrm{PCP}}(i, Q, (\mathrm{col}_q[i])_{q\in Q}) = 1$。

如果能把它寫成**批次索引**的形式，就能對它**再套同一個構造**，遞迴下去。

**問題**（[▶ 28:31](https://youtu.be/p60ShJrbrf8?t=1711)）：第 2 條已經是「對每個索引 $i$」的形式，但第 1 條不是。$Q$ 很小，但證據（整欄）很大，**每欄有 $k$ 個位置**。如果把整欄當證據，遞迴時新的第一則訊息（$h'_1, \ldots, h'_{\ell'}$）會隨 $k$ 成長，負擔不起。

要改寫成：**實例數是 $k$，但每個實例的證據很小**。

### 4.2 讓證據變小：有局部打開的 SSB

[▶ 29:52](https://youtu.be/p60ShJrbrf8?t=1792)

如果 SSB 雜湊是用 **Merkle 樹的方式**建的，就可以**局部驗證**：把「重算整欄的雜湊」換成「對每個 $i\in[k]$，存在 $\mathrm{col}_q[i]$ 的局部打開 $\rho_{i,q}$」。

**新的語言** $L'$（[▶ 33:46](https://youtu.be/p60ShJrbrf8?t=2026)）：$i\in L'$ 若存在證據 $w'_i = \left( (\mathrm{col}_q[i], \rho_{i,q})_{q\in Q} \right)$ 使得
1. $V_{\mathrm{PCP}}(i, Q, (\mathrm{col}_q[i])_{q\in Q}) = 1$；
2. 對每個 $q\in Q$：$\mathrm{SSB.LocalVerify}(h_q, i, \mathrm{col}_q[i], \rho_{i,q}) = 1$。

證明者要證 $1, \ldots, k$ 全在 $L'$ 裡。每個證據只有 $|Q|$ 個位元加上 $|Q|$ 條路徑，**很小**。

【Q&A】[▶ 37:09](https://youtu.be/p60ShJrbrf8?t=2229) **這樣遞迴，實例數還是 $k$，不會永遠不停？** 對，直接遞迴會無限迴圈。要把它們「綁在一起」（4.4）。

【Q&A】[▶ 37:53](https://youtu.be/p60ShJrbrf8?t=2273) **$h_q$ 是什麼的雜湊？** 就是第一則訊息裡的 $h_q$：PCP 矩陣第 $q$ 欄的 SSB 雜湊。

### 4.3 有局部打開的 SSB 雜湊

[▶ 38:39](https://youtu.be/p60ShJrbrf8?t=2319)

第 14 集的 SSB（一次 FHE 求值）沒有局部打開。改成 **Merkle 樹形式**：

- 每個節點從兩個子節點**在 FHE 底下挑一個**。
- 每一層有一個加密的位元 $b_1, b_2, \ldots$（$i$ 的二進位寫法）：例如這層挑左邊、下一層挑右邊，一路指到葉子 $i$。
- 每層用這個加密位元同態地挑子節點，跟之前一樣。

**局部打開的正確性**（[▶ 41:23](https://youtu.be/p60ShJrbrf8?t=2483)）：soundness 證明需要「被接受的第三則訊息和 SSB 萃取出的值一致」。原本驗證者看到整欄，很容易保證；現在只看到一條根到葉的路徑，需要：

> 若 SSB 金鑰是對位置 $i$ 產生的，且 $\mathrm{LocalVerify}(h, i, x_i, \rho_i) = 1$，則 $\mathrm{Ext}(td, h) = x_i$。

**這不是自動成立的**：驗證路徑上的**兄弟節點**可能不是格式正確的 FHE 密文。需要加一個**自舉**機制：每一層用不同的 FHE 金鑰，下一層在同態底下**解密**上一層的密文，保證它格式正確。「細節不講，你們可以自己修好。」

【Q&A】[▶ 45:00](https://youtu.be/p60ShJrbrf8?t=2700) 為什麼不直接把 SSB 疊成 Merkle 樹？那樣密文大小可能每層放大 $\lambda$ 倍。

### 4.4 二合一技巧：讓遞迴會結束

[▶ 46:25](https://youtu.be/p60ShJrbrf8?t=2785)

$k$ 個實例 $1, \ldots, k$，證據 $w'_1, \ldots, w'_k$。**相鄰兩個合併**：

$$i\in L''\iff\exists\,(w'_{2i-1}, w'_{2i}):\ C'(2i-1, w'_{2i-1}) = 1\ \wedge\ C'(2i, w'_{2i}) = 1.$$

- 實例數變成 $k/2$，代價是證據長度變兩倍。
- 遞迴時對 $L''$ 證 $1, \ldots, k/2$。每層實例數減半，$\log k$ 層後只剩**一個**。

【課堂討論】[▶ 51:24](https://youtu.be/p60ShJrbrf8?t=3084) 剩一個時怎麼辦？學生答：直接送證據，驗證者自己檢查。

【Q&A】[▶ 63:16](https://youtu.be/p60ShJrbrf8?t=3796) 最後的證據多大？遞迴一層後，證據只是 PCP 的打開，polylog $|C|$，所以最後一層的證據也很小。

### 4.5 問題：電路每層變兩倍

[▶ 52:19](https://youtu.be/p60ShJrbrf8?t=3139)

第一則訊息大小是 $\mathrm{poly}(|C|, \lambda)$。下一層的第一則訊息是 $\mathrm{poly}(|C''|, \lambda)$。

- $C''$ 包含兩份 $C'$，$|C''|\approx 2|C'|$。
- $C'$ 包含 PCP 驗證，而 **PCP 驗證者要知道 NP 關係**，跑 $|C|$ 時間，所以 $|C'|\ge|C|$。
- 每層變兩倍：$|C|, 2|C|, 4|C|, \ldots$，$\log k$ 層後是 $k\cdot|C|$。證明會隨 $k\cdot|C|$ 成長，太大了。

### 4.6 快速線上驗證的 PCP

[▶ 56:12](https://youtu.be/p60ShJrbrf8?t=3372)

> **快速線上驗證的 PCP**（PCP with fast online verification）：PCP 驗證者拆成兩段：
> 1. **離線前處理**：$\mathrm{st}\leftarrow V_{\mathrm{off}}(C, Q)$，只依賴關係電路 $C$ 和查詢 $Q$，輸出很短的狀態（大小約 $\mathrm{poly}(|x|, |Q|)$）。
> 2. **線上驗證**：$V_{\mathrm{on}}(\mathrm{st}, x, Q, \mathrm{PCP}|_Q)$，時間 $\mathrm{poly}(|x|, |Q|)$，**和 $|C|$ 無關**。

- 電路很大、實例很小時，前處理佔大部分時間，線上很快。
- 大部分**代數的 PCP 構造**都有這個性質。
- 【口頭】很多實用的 SNARG 也用這個：它們也用 PCP 或某種形式的 PCP（例如線性 PCP），關係電路很大但驗證要小，所以先對關係做前處理產生簡短的驗證狀態。

**修改構造**（[▶ 60:52](https://youtu.be/p60ShJrbrf8?t=3652)）：
1. 用 CI 雜湊產生 $Q$。
2. 對 $Q$ 做前處理得到 $\mathrm{st}$（用到 $C$）。可以這樣做是因為**所有 PCP 共用同一個查詢 $Q$**。
3. 把 $\mathrm{st}$ 寫死在 $C'$ 裡，$C'$ 只做**線上驗證**。

現在 $C'$ 只含線上驗證（對 $|i| = \log k$ 是多項式）和 Merkle 局部驗證（polylog $k$），**不再依賴 $|C|$**，是 $\mathrm{poly}(\log k, \log|C|, \lambda)$。代進遞迴分析，總證明長度 $\mathrm{poly}(\log|C|, \log k, \lambda)$。

---

## 5. 半適應性 soundness

[▶ 64:05](https://youtu.be/p60ShJrbrf8?t=3845)

**問題**：遞迴時 $L''$ 依賴 $C'$，$C'$ 用到樹根 $h_q$，而 $h_q$ 來自作弊者送的第一則訊息。所以作弊者可以**看了 CRS 之後**選下一層的命題，非適應性 soundness 不夠。但**完全適應性**的 soundness（作弊者看了 CRS 再選實例）不知道怎麼做到。

> **半適應性 soundness**（semi-adaptive soundness）：存在另一個 CRS 產生器 $\overline{\mathrm{Gen}}(1^{\lambda}, i^{*})\to\mathrm{CRS}^{*}$，和真的 CRS **不可區分**，而且對每個非一致 PPT 作弊者 $P^{*}$：
> $$\Pr\left[ (C, \pi^{*})\leftarrow P^{*}(\mathrm{CRS}^{*}):\ V(\mathrm{CRS}^{*}, C, k, \pi^{*}) = 1\ \wedge\ i^{*}\notin L_C \right]\le\mathrm{negl}.$$
> 作弊者可以**適應性地選關係電路 $C$**，但不能選**要在哪個索引作弊**（$i^{*}$ 寫在 CRS 裡）。

【口頭】這個概念不只在這個證明裡重要，下一集把批次索引 SNARG 編譯成 P 的 SNARG 時也很關鍵。

**直覺**：SSB 綁定某個位置。把 $\overline{\mathrm{Gen}}$ 設成產生「綁定第 $i^{*}$ 個位置」的 SSB 金鑰，作弊者就不能在第 $i^{*}$ 個實例作弊。

**證明想法**（[▶ 70:00](https://youtu.be/p60ShJrbrf8?t=4200)）：
- 固定 $i^{*}\notin L$，把 CRS 換到 $i^{*}$。
- 只要作弊者沒有破解 CI 雜湊（$(h, Q)$ 不在 CI 的關係 $R$ 裡），「$i^{*}$ 是假的」就會**傳遞**到下一層：由於二合一，$\lceil i^{*}/2\rceil$ 在 $L''$ 裡也是假的。
- 一層一層追蹤這個固定的 $i^{*}$（每次除以 2 取上整），最後一層直接送證據，一定抓得到。

【Q&A】[▶ 72:06](https://youtu.be/p60ShJrbrf8?t=4326) **整個構造有任何適應性 soundness 嗎？** 只有這種半適應性的。一般 BARG 大概也有類似的概念。

【Q&A】[▶ 72:47](https://youtu.be/p60ShJrbrf8?t=4367) **有適應性 sound 的構造嗎？** 一般來說，任何非適應性 sound 的 SNARG 都能用**複雜度槓桿**（complexity leveraging）升級成適應性的，但安全性證明要付出實例大小的代價。BARG 的總實例大小是 $k\cdot|x|$，很大，不確定行得通。學生：所以先驗地不清楚？講者：似乎有落差，不確定多大；也許聰明的複雜度槓桿能幾乎補上。

---

## 6. 一頁速查表

### 第一版 BARG 的問題

證明 $\mathrm{poly}(|C|, \lambda) + k\lambda\,\mathrm{polylog}|C|$；驗證 $k\cdot\mathrm{poly}(|C|)$（沒省）。一般 BARG 驗證下界 $k|x|$。

### 索引 BARG

- 實例 $x_i = U(i)$，驗證者只拿 $k$。目標：證明、驗證都 $\mathrm{poly}(\log k, \cdot, \lambda)$。
- 一般 BARG = Merkle 樹根 $h$ + 對 $C'_h(i, (x_i, \rho_i, w_i))$ 的索引 BARG。需要適應性（半適應性）soundness。

### 構造

1. PCP 矩陣，逐欄用**有局部打開的 SSB**（Merkle 形式，每層 FHE 挑子節點，加自舉保證局部打開正確性）。
2. $Q = H_{\mathrm{CI}}(h_1, \ldots, h_{\ell})$；前處理 $\mathrm{st} = V_{\mathrm{off}}(C, Q)$。
3. 新語言 $L'$：$i$ 的證據 = $(\mathrm{col}_q[i], \rho_{i,q})_{q\in Q}$，檢查 $V_{\mathrm{on}}(\mathrm{st}, i, Q, \cdot)$ 和局部打開。
4. 二合一：$L''$ 合併相鄰實例，實例數減半。
5. 遞迴 $\log k$ 層，最後送證據。

關鍵一步：快速線上驗證讓 $|C'|$ 不依賴 $|C|$，否則每層翻倍成 $k|C|$。

### 半適應性 soundness

$\overline{\mathrm{Gen}}(1^{\lambda}, i^{*})\approx_c\mathrm{Gen}$；作弊者可選 $C$，但不能在 $i^{*}$ 作弊。證明：$i^{*}$ 的「假」逐層傳到 $\lceil i^{*}/2\rceil$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 索引 BARG（半適應性 soundness） | 第 16–17 集：Kalai 用它造 P 的 SNARG |
| 有局部打開的 SSB、萃取 | 第 16–17 集 |
| 快速線上驗證的 PCP | 實用 SNARG |

---

## 附：本集一句話總結

> **直接的 BARG 驗證者要讀所有實例、跑所有 PCP 驗證；改成「索引 BARG」後，證明者把第三則訊息的驗證本身再用 BARG 證明，用有局部打開的 SSB 讓每個實例的證據變小、用二合一讓實例數每層減半、用快速線上驗證的 PCP 讓電路不再每層翻倍，遞迴 $\log k$ 層就得到 polylog 的證明——安全性靠的是半適應性 soundness：作弊者可以挑電路，但不能挑在哪個索引作弊。**

---

## ⚠️ 待確認清單

1. [▶ 00:56](https://youtu.be/p60ShJrbrf8?t=56) 「對可有效率驗證的乘積關係的 CI 雜湊」那篇工作的作者（字幕 `[INAUDIBLE]`／「HR」）不確定。

---

*筆記依據 Zhengzhong Jin 客座講授的「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 8 Part 2 錄影逐字稿（MIT 真人字幕，1:14:14）整理；本集無次要來源。*
