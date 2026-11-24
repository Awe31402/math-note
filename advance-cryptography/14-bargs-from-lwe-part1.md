---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 14
lecture: Lecture 8 (Part 1) – Succinct Non-Interactive Arguments for Batch NP (BARGs) from LWE
date: 待補（2023 秋季，感恩節後第一堂）
video: https://youtu.be/t3C6cpQlSvA
notes: OCW 本講無指定讀物。講者是 Choudhuri–Jain–Jin 論文的作者之一（OCW 第 9 講讀物，ePrint 2021/808，未取得）。只依逐字稿。
---

# 第 14 集 · Lecture 8 (Part 1)：批次論證（BARG）——PCP 矩陣、相關性難解雜湊、某處統計綁定雜湊 [▶ 影片](https://youtu.be/t3C6cpQlSvA)

← 上一集：[13-fiat-shamir-standard-model-part2](13-fiat-shamir-standard-model-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[15-bargs-from-lwe-part2](15-bargs-from-lwe-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 14 集
> **講者**：**Zhengzhong Jin**（客座；BARG 論文作者之一）
> **來源**：YouTube 錄影逐字稿（1:21:37，MIT 上傳的真人字幕）。本講沒有指定讀物，相關論文未取得，**本集沒有次要來源**。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：字幕把「NP」常聽成「MP」、「PPT」聽成「PBT」、「SNARG」聽成「SNAG」、「third-round」聽成「pseudorandom」等，筆記直接改正，不一一標出。黑板看不到，符號照口述重建。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. BARG 的定義](#1-barg-的定義)
- [2. 為什麼研究 BARG](#2-為什麼研究-barg)
  - [2.1 應用](#21-應用)
  - [2.2 Gentry–Wichs 的不可能結果與 BARG 的關係](#22-gentrywichs-的不可能結果與-barg-的關係)
- [3. 主定理](#3-主定理)
- [4. 第一版：Kilian 的變形](#4-第一版kilian-的變形)
  - [4.1 PCP 回顧](#41-pcp-回顧)
  - [4.2 PCP 矩陣與逐欄雜湊](#42-pcp-矩陣與逐欄雜湊)
- [5. 用相關性難解雜湊拿掉互動](#5-用相關性難解雜湊拿掉互動)
  - [5.1 CI 雜湊回顧](#51-ci-雜湊回顧)
  - [5.2 問題：關係不稀疏](#52-問題關係不稀疏)
- [6. 某處統計綁定（SSB）雜湊](#6-某處統計綁定ssb雜湊)
  - [6.1 定義](#61-定義)
  - [6.2 從 FHE 構造](#62-從-fhe-構造)
  - [6.3 萃取性質](#63-萃取性質)
- [7. 用 SSB 雜湊的 BARG 與 soundness](#7-用-ssb-雜湊的-barg-與-soundness)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/t3C6cpQlSvA?t=0)

講者 Zhengzhong Jin。主題是 **NP 批次的 SNARG**，也叫**批次論證**（batch argument, BARG）。

【口頭】「批次」是電腦科學很基本的概念：把很多東西收集在一起，例如程式裡的批次處理。這堂課講的是證明系統裡的「批次」。

---

## 1. BARG 的定義

[▶ 01:26](https://youtu.be/t3C6cpQlSvA?t=86)

> **BARG** 是一組演算法 $(\mathrm{Gen}, P, V)$：
> - $\mathrm{Gen}(1^{\lambda})\to\mathrm{CRS}$；證明者和驗證者都能用 CRS。
> - 固定 NP 語言 $L$（關係電路 $C$）。證明者有 $k$ 個實例 $x_1, \ldots, x_k$ 和證據 $w_1, \ldots, w_k$，要說服驗證者**全部** $x_i\in L$。證明是**一則訊息** $\pi$。
>
> **簡短**（succinct）：$|\pi| < k\cdot|w|$。
>
> **Completeness**：誠實產生的證明一定被接受。
>
> **Soundness**：若不是所有 $x_i\in L$，對每個非一致 PPT 作弊者 $P^{*}$：
> $$\Pr\left[ \pi^{*}\leftarrow P^{*}(\mathrm{CRS}):\ V(\mathrm{CRS}, x_1, \ldots, x_k, \pi^{*}) = 1 \right]\le\mathrm{negl}(\lambda).$$

【課堂討論】[▶ 03:37](https://youtu.be/t3C6cpQlSvA?t=217) 為什麼要求 $|\pi| < k|w|$？學生答：否則直接把所有證據送過去（長度 $k|w|$）就好了。

---

## 2. 為什麼研究 BARG

### 2.1 應用

[▶ 06:30](https://youtu.be/t3C6cpQlSvA?t=390)

這顯然是 NP 的一個子類別，為什麼在乎？

- 「批次」是很基本的概念，密碼學其他地方也研究過：**聚合簽章**（aggregated signature，把很多簽章合成一個短簽章，只要驗證短的那個）、**批次互動式證明**（batch interactive proof）。
- **下一集 Kalai 會用 BARG 造 P 的 SNARG**。到目前為止有很多從不同假設造 P 的 SNARG 的方法，**全部都用 BARG 當積木**。

【Q&A】[▶ 12:01](https://youtu.be/t3C6cpQlSvA?t=721) **有沒有希望做出統計 sound 的 BARG？** 有最近的工作顯示：如果能做出統計 BARG，就能造出某種統計的證據不可區分（witness indistinguishability）的東西。確切答案還不知道。
- ⚠️ 待確認：這段字幕不太清楚（「statistical witness in distinguishibility」），確切的結論和出處不確定。

### 2.2 Gentry–Wichs 的不可能結果與 BARG 的關係

[▶ 12:41](https://youtu.be/t3C6cpQlSvA?t=761)

講者說研究 BARG 還有技術上的理由（不細講這個下界）：

- **Gentry–Wichs**：若語言是「$T$-難」的（判定需要 $T$ 時間），在**可證偽假設**（falsifiable assumption，例如 LWE 這種「好的」假設）下，不可能造出證明長度**遠小於 $\log T$** 的 SNARG。
- 一般 NP 語言、證據長度 $|w|$，判定大約要 $2^{|w|}$ 時間，$\log T\approx|w|$。所以：**NP 的 SNARG，證明遠短於 $|w|$ 很難**（在好的假設下）。

**對 BARG 呢**？【課堂討論】要證的語言是
$$L^{\otimes k} = \left\{ (x_1, \ldots, x_k) : \forall i,\ x_i\in L \right\}.$$
判定它要多久？學生答：$k$ 倍單個的時間，$k\cdot 2^{|w|}$。

> 【課本補充】Thaler 的參考文獻列出 [GW11]：Craig Gentry、Daniel Wichs〈Separating succinct non-interactive arguments from all falsifiable assumptions〉；正文也說用 Fiat–Shamir 把簡短論證變成非互動的結果目前是負面的 [GW11, BBH+19]（§5.2）。Thaler 沒有寫出「$\log T$」這個確切的界。

所以 $\log T\approx|w| + \log k$。Gentry–Wichs 只說證明遠短於 $|w|$ 很難；**長度約 $|w|$ 的 BARG 不和它矛盾**，而且已經很簡短了（遠小於 $k|w|$）。

---

## 3. 主定理

[▶ 12:20](https://youtu.be/t3C6cpQlSvA?t=740)

> **定理**：從 **LWE** 可以造出 BARG，
> - 證明長度 $|\pi| = \mathrm{poly}(|C|, \log k, \lambda)$；
> - 驗證時間 $k\cdot|x| + \mathrm{poly}(\log k, |C|, \lambda)$。

- 以 3SAT 為例，電路很淺，$|C|$ 和 $|w|$ 差不多；$\log k$ 很小，所以證明長度接近 $|w|$。
- **驗證者可以拆成兩段**：
  1. **前處理**：只讀所有實例，輸出一個很小的狀態（$k\cdot|x|$ 那一項）。
  2. **線上階段**：拿這個狀態，在很短的時間內驗證證明，**和 $k$ 無關**（之後會講）。

【Q&A】[▶ 15:21](https://youtu.be/t3C6cpQlSvA?t=921) **$k$ 比 $|w|$ 大很多嗎？** 可以想成 $k$ 是 $|w|$ 的多項式（證明者要多項式時間）。學生：那只有在 $\mathrm{poly}(|C|)$ 是小多項式時才簡短？對。講者說有一般的**自舉**（bootstrap）方法可以把對電路大小的依賴拿掉，只依賴證據長度，但要用到下一集 Kalai 講的東西。

---

## 4. 第一版：Kilian 的變形

[▶ 17:25](https://youtu.be/t3C6cpQlSvA?t=1045)

「直接給你構造會很複雜，我先給第一版，再一個一個加積木。」起點是 **Kilian 協定的簡化版**。

### 4.1 PCP 回顧

[▶ 19:10](https://youtu.be/t3C6cpQlSvA?t=1150)

- PCP 證明者：給 $(x, w)$，產生一個長字串 $\mathrm{PCP}\in\{0,1\}^{\ell}$。
- PCP 驗證者：抽一個隨機的位置子集 $Q\subseteq[\ell]$，讀 $\mathrm{PCP}|_Q$，配合 $x$ 決定接受或拒絕。
- Completeness：$(x, w)$ 在關係裡就一定接受。Soundness：$x\notin L$ 時，對任何 $\mathrm{PCP}^{*}$，接受機率 $\le\varepsilon$（常數）。
- **平行重複 $\lambda$ 次**：錯誤變成 $\varepsilon^{\lambda} = 2^{-O(\lambda)}$，代價是查詢數乘 $\lambda$。所以不失一般性：查詢數 $|Q|\approx\lambda\cdot\mathrm{polylog}(|C|)$、soundness 錯誤 $\approx 2^{-\lambda}$。

【Q&A】[▶ 22:40](https://youtu.be/t3C6cpQlSvA?t=1360) **有些 PCP 查詢數只要 $O(\lambda)$，需要 polylog 那項嗎？** 也許可以不要。但這個構造需要 PCP 有一些**額外結構**，講者只知道從 Reed–Muller 碼來的代數構造有，不知道其他 PCP 有沒有。（字幕寫「written numeric code」，應是 Reed–Muller。）

【Q&A】[▶ 23:20](https://youtu.be/t3C6cpQlSvA?t=1400) **$\ell$ 多大？** $\mathrm{poly}(|C|)$。也許有更有效率的 PCP 讓 $\ell$ 接近 $|C|$ 的線性。

### 4.2 PCP 矩陣與逐欄雜湊

[▶ 24:00](https://youtu.be/t3C6cpQlSvA?t=1440)

證明者對每個實例算一個 PCP：$\mathrm{PCP}_1, \ldots, \mathrm{PCP}_k$。把它們疊成一個 **$k\times\ell$ 的矩陣**（第 $i$ 列是 $\mathrm{PCP}_i$）。CRS 裡放一把雜湊金鑰。

**協定（互動版）**：

1. $P\to V$：**每一欄**分別雜湊：$h_j := H(\text{第 } j \text{ 欄})$，$j = 1, \ldots, \ell$。送出 $h_1, \ldots, h_{\ell}$。
2. $V\to P$：**一個** PCP 查詢 $Q$（所有實例共用同一個）。
3. $P\to V$：打開被查到的**欄**：所有 $j\in Q$ 的第 $j$ 欄。

**驗證**：
- 重算被打開的欄的雜湊，和 $h_j$ 比對。
- 對每個 $i = 1, \ldots, k$：跑 PCP 驗證者 $V_{\mathrm{PCP}}(x_i, Q, \text{第 } i \text{ 列在 } Q \text{ 上的值})$。

- 和 Kilian 差在：**不用 Merkle 樹**，而是每一欄直接雜湊。
- 【Q&A】[▶ 28:14](https://youtu.be/t3C6cpQlSvA?t=1694) $h_1, \ldots, h_{\ell}$ 也用 Merkle 樹承諾嗎？目前不用，直接送。送出就直覺上固定了 PCP 矩陣。
- 【Q&A】[▶ 28:54](https://youtu.be/t3C6cpQlSvA?t=1734) 學生：第三則訊息就是我們會想壓縮的地方？講者：「好觀察。」
- 【Q&A】[▶ 30:03](https://youtu.be/t3C6cpQlSvA?t=1803) **打開的欄對驗證者夠小嗎？** $|Q|$ 只有大約 $\mathrm{polylog}(|C|)$。但每一欄有 $k$ 列，所以第三則訊息大約 $k\cdot|Q|$，**隨 $k$ 成長**。（下一集處理。）

---

## 5. 用相關性難解雜湊拿掉互動

### 5.1 CI 雜湊回顧

[▶ 32:53](https://youtu.be/t3C6cpQlSvA?t=1973)

- **CI 雜湊**（對關係 $R$）：$(\mathrm{Gen}, H)$；對每個非一致 PPT 攻擊者，拿到 $hk$ 後輸出 $x$ 使 $(x, H_{hk}(x))\in R$ 的機率可忽略。
- **編譯三則訊息 public-coin 協定**：證明是 $(\alpha, \beta, \gamma)$，$\beta = H_{hk}(\alpha)$。
- **Soundness 證明**：定義 $R = \{(\alpha, \beta):\exists\gamma$ 使驗證者接受$\}$。作弊者輸出被接受的 $(\alpha^{*}, \beta^{*}, \gamma^{*})$，就代表 $(\alpha^{*}, H(\alpha^{*}))\in R$，違反 CI。
- **關鍵條件：$R$ 要稀疏**：對每個固定的 $\alpha$，$|\{\beta : (\alpha, \beta)\in R\}|/|\mathcal{Y}|$ 可忽略。
  - 【課堂討論】為什麼需要？極端情形：若某個 $\alpha_0$ 對**所有** $\beta$ 都在 $R$ 裡，任何雜湊都會撞到。至少這個比例要小於 1。

### 5.2 問題：關係不稀疏

[▶ 41:39](https://youtu.be/t3C6cpQlSvA?t=2499)

套用：證明者自己算 $Q := H_{\mathrm{CI}}(h_1, \ldots, h_{\ell})$（CI 金鑰放在 CRS），證明是 $(h_1, \ldots, h_{\ell})$ 加第三則訊息。

- 【Q&A】[▶ 44:05](https://youtu.be/t3C6cpQlSvA?t=2645) CI 雜湊的輸出要是驗證者會查的子集？需要 PCP 是 public coin：有一個查詢取樣器，吃均勻隨機字串、產生 PCP 查詢。拿 CI 雜湊的輸出當那個隨機字串。
- 【Q&A】[▶ 46:14](https://youtu.be/t3C6cpQlSvA?t=2774) Completeness？選完美 completeness 的 PCP，任何查詢都接受。

**第一次嘗試**（[▶ 46:54](https://youtu.be/t3C6cpQlSvA?t=2814)）：

$$R = \left\{ (h_1, \ldots, h_{\ell}, Q) : \exists\ \text{第三則訊息使驗證者接受} \right\}.$$

**問題**：雜湊是**壓縮**的。固定 $h_1, \ldots, h_{\ell}$，可能有**很多個**原像（很多個 PCP 矩陣）。每個原像各自有一個讓它被接受的 $Q$；$R$ 是**所有原像的 $Q$ 的聯集**。原像數遠多於 $Q$ 的可能數，所以不知道 $R$ 是否稀疏（甚至不知道比例是否小於 1）。

【Q&A】[▶ 56:01](https://youtu.be/t3C6cpQlSvA?t=3361) **作弊者要利用這點，得找到碰撞，為什麼要擔心？** 用具體雜湊時，不清楚作弊者能不能利用；但**也不知道怎麼證明 soundness**。

**解法**：用一種特別的雜湊，仍然壓縮，但會**透露一些原像的資訊**。

---

## 6. 某處統計綁定（SSB）雜湊

### 6.1 定義

[▶ 49:13](https://youtu.be/t3C6cpQlSvA?t=2953)

> **某處統計綁定雜湊**（somewhere statistically binding, SSB）：$(\mathrm{Gen}, H)$
> - $\mathrm{Gen}(1^{\lambda}, i)\to k$：多吃一個**索引** $i\in[n]$。
> - $H_k(x_1, \ldots, x_n)\to$ 雜湊值。
>
> **金鑰不可區分**（key indistinguishability / key hiding）：對任何 $i_1, i_2\in[n]$，$\mathrm{Gen}(1^{\lambda}, i_1)\approx_c\mathrm{Gen}(1^{\lambda}, i_2)$。
>
> **在 $i$ 處統計綁定**：若 $k\leftarrow\mathrm{Gen}(1^{\lambda}, i)$，則對任何 $(x_1, \ldots, x_n)$、$(x_1', \ldots, x_n')$，
> $$H_k(x_1, \ldots, x_n) = H_k(x_1', \ldots, x_n')\ \Longrightarrow\ x_i = x_i'.$$

白話：雜湊值**完全決定第 $i$ 個位置**的值（資訊理論的），但從金鑰看不出 $i$ 是哪個。

### 6.2 從 FHE 構造

[▶ 56:44](https://youtu.be/t3C6cpQlSvA?t=3404)

回顧 FHE：公鑰加密，給 $m$ 的密文，可以對任何函數 $F$ 同態求值得到 $F(m)$ 的密文。

- $\mathrm{Gen}(1^{\lambda}, i)$：輸出 $i$ 的 FHE 密文 $\hat{i} = \mathrm{Enc}(pk, i)$（和 $pk$）。
- $H_k(x_1, \ldots, x_n) := \mathrm{FHE.Eval}(pk, F_{x_1, \ldots, x_n}, \hat{i})$，其中 $F_{x_1, \ldots, x_n}(i) := x_i$（把 $x$ 寫死在函數裡）。

直覺：**在 FHE 底下挑出第 $i$ 個位置**。

- **壓縮**：雜湊值只是一個密文，$\mathrm{poly}(\lambda)$。
- **金鑰不可區分**：由 FHE 的安全性，$i$ 是隱藏的。
- **統計綁定**：雜湊值就是 $x_i$ 的同態加密，解密一定得到 $x_i$。

### 6.3 萃取性質

[▶ 59:48](https://youtu.be/t3C6cpQlSvA?t=3588)

雜湊值裡就是 $x_i$ 的 FHE 密文，有秘密鑰就能解出來。正式地：

> **萃取**：$\mathrm{Gen}(1^{\lambda}, i)$ 額外輸出陷門 $td$（FHE 秘密鑰）。存在多項式時間的萃取器 $\mathrm{Ext}$：對任何 $(x_1, \ldots, x_n)$，若 $s = H_k(x_1, \ldots, x_n)$、$k$ 是對位置 $i$ 產生的，則 $\mathrm{Ext}(td, s) = x_i$。

---

## 7. 用 SSB 雜湊的 BARG 與 soundness

[▶ 62:07](https://youtu.be/t3C6cpQlSvA?t=3727)

**修改**：逐欄雜湊改用 **SSB 雜湊**，SSB 金鑰放進 CRS。其他照舊（驗證時也用 SSB 重算每一欄）。

【Q&A】[▶ 63:35](https://youtu.be/t3C6cpQlSvA?t=3815) **SSB 金鑰用哪個 $i$？** 其實實際構造根本不需要 $i$：FHE 密文是偽隨機的，放任何索引都行。

**直覺**（[▶ 64:15](https://youtu.be/t3C6cpQlSvA?t=3855)）：若金鑰是對 $i^{*}$ 產生的，每一欄的雜湊都綁定那一欄的第 $i^{*}$ 個位置。所以 $h_1, \ldots, h_{\ell}$ **綁定整個第 $i^{*}$ 列**（它們就是那一列每個位元的 FHE 密文，包含那一列完整的資訊）。

**關鍵觀察**（[▶ 66:25](https://youtu.be/t3C6cpQlSvA?t=3985)）：若「全部 $x_i\in L$」不成立，就**存在某個 $i^{*}$ 使 $x_{i^{*}}\notin L$**。只要抓住這一個就能證 soundness。SSB 能綁定第 $i^{*}$ 列，而第 $i^{*}$ 列正是 $x_{i^{*}}$ 的 PCP。

**正式證明（混合論證，hybrid）**：

- **$H_0$**：$P^{*}$ 拿到 CRS，輸出 $\pi^{*}$，以機率 $\ge\varepsilon$ 被接受。
- **$H_1$**：把 CRS 裡的 SSB 金鑰換成 $\mathrm{Gen}(1^{\lambda}, i^{*})$。由**金鑰不可區分**，$P^{*}$ 仍以約 $\varepsilon - \mathrm{negl}$ 被接受。
- **定義新的關係**：
$$R := \left\{ (h_1, \ldots, h_{\ell}, Q):\ \mathrm{PCP}^{*} := \mathrm{Ext}(td, h_1, \ldots, h_{\ell})\ \text{（第 } i^{*} \text{ 列）},\ V_{\mathrm{PCP}}(x_{i^{*}}, Q, \mathrm{PCP}^{*}|_Q) = 1 \right\}.$$
- **Claim（資訊理論）**：若 $\pi^{*} = (h_1^{*}, \ldots, h_{\ell}^{*}, \text{打開的欄})$ 被接受，則 $(h^{*}, Q^{*})\in R$，$Q^{*} = H_{\mathrm{CI}}(h^{*})$。
  - 理由：由萃取正確性，被打開的欄的第 $i^{*}$ 個位置必須和萃取出的 $\mathrm{PCP}^{*}$ 一致（否則雜湊對不上）。驗證者接受代表 $V_{\mathrm{PCP}}(x_{i^{*}}, Q^{*}, \cdot)$ 接受那些值，也就是接受 $\mathrm{PCP}^{*}|_{Q^{*}}$。
- **$R$ 是稀疏的**：每個 $h$ 只決定**一個** $\mathrm{PCP}^{*}$；$x_{i^{*}}\notin L$，所以讓它被接受的 $Q$ 只佔 $2^{-\lambda}$ 比例（PCP soundness）。
- 所以作弊者找到了 $h^{*}$ 使 $(h^{*}, H_{\mathrm{CI}}(h^{*}))\in R$，違反 CI。（$R$ 是可以用陷門有效率檢查的關係，第 13 集的 CI 技巧適用。）$\blacksquare$

【Q&A】[▶ 67:50](https://youtu.be/t3C6cpQlSvA?t=4070) 學生：綁定的那一列剛好是不在語言裡的那個？就是這樣設定的。

【Q&A】[▶ 78:49](https://youtu.be/t3C6cpQlSvA?t=4729) **混合論證裡怎麼知道是哪個 $i^{*}$？** 這個 soundness 證明是**非一致、非適應性**的：從固定的 $x_1, \ldots, x_k$ 開始，存在一個固定的 $i^{*}$ 使 $x_{i^{*}}$ 是假的。這個 $i^{*}$ 以非一致的方式給歸約。

**還剩的問題**：第三則訊息（打開的欄）有 $k\cdot|Q|$ 位元，隨 $k$ 成長。休息後處理（第 15 集）。

---

## 8. 一頁速查表

### BARG

- 證明 $(x_1, \ldots, x_k)\in L^{\otimes k}$，一則訊息，$|\pi| < k|w|$。
- 主定理（LWE）：$|\pi| = \mathrm{poly}(|C|, \log k, \lambda)$，驗證 $k|x| + \mathrm{poly}(\log k, |C|, \lambda)$（前處理 + 線上）。
- Gentry–Wichs：好假設下 SNARG 證明不能遠短於 $\log T$；$L^{\otimes k}$ 的 $\log T\approx|w| + \log k$，所以長度約 $|w|$ 的 BARG 不矛盾。

### 構造（第一版）

1. PCP 矩陣（$k\times\ell$，第 $i$ 列 = $\mathrm{PCP}(x_i, w_i)$）。
2. 每欄雜湊 → $h_1, \ldots, h_{\ell}$。
3. $Q = H_{\mathrm{CI}}(h_1, \ldots, h_{\ell})$（Fiat–Shamir）。
4. 打開 $Q$ 的欄（$k|Q|$ 位元，下一集壓縮）。

### SSB 雜湊

- $\mathrm{Gen}(1^{\lambda}, i)$；金鑰不可區分；在 $i$ 處統計綁定；可萃取。
- FHE 構造：金鑰 $= \mathrm{Enc}(i)$，$H(x) = \mathrm{Eval}(F_x, \hat{i})$，$F_x(i) = x_i$。

### Soundness

- 若某個 $x_{i^{*}}\notin L$：把 SSB 金鑰換到 $i^{*}$（不可區分）。
- $R = \{(h, Q):\ V_{\mathrm{PCP}}(x_{i^{*}}, Q, \mathrm{Ext}(td, h)|_Q) = 1\}$：每個 $h$ 決定一個 PCP，所以稀疏（$2^{-\lambda}$）。
- 被接受 ⟹ $(h, H_{\mathrm{CI}}(h))\in R$，違反 CI。
- 沒有 SSB 時，壓縮的雜湊有很多原像，$R$ 不一定稀疏。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 第三則訊息隨 $k$ 成長 | 第 15 集：壓縮 |
| BARG | 第 16–17 集：Kalai 用 BARG 造 P 的 SNARG |
| SSB 雜湊（萃取、綁定一個位置） | 第 16–17 集 |

---

## 附：本集一句話總結

> **批次論證要用比 $k$ 份證據短得多的證明說服「$k$ 個實例全對」；做法是把 $k$ 份 PCP 疊成矩陣、逐欄用 SSB 雜湊、再用 CI 雜湊產生共用的查詢——SSB 金鑰可以偷偷指向那個假的實例 $i^{*}$，讓雜湊值唯一決定它那一列，於是「會被接受的查詢」這個關係變得稀疏，CI 雜湊就擋得住作弊。**

---

## ⚠️ 待確認清單

1. [▶ 12:01](https://youtu.be/t3C6cpQlSvA?t=721) 「統計 sound 的 BARG ⟹ 某種統計證據不可區分」那段的確切結論和出處，字幕不清楚。
2. 本講沒有 OCW 指定讀物，相關論文（Choudhuri–Jain–Jin，ePrint 2021/808）未取得；PCP 需要的「額外結構」是什麼、Gentry–Wichs 不可能結果的確切敘述（Thaler 只列出論文標題），待對照論文。

---

*筆記依據 Zhengzhong Jin 客座講授的「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 8 Part 1 錄影逐字稿（MIT 真人字幕，1:21:37）整理；本集無次要來源。*
