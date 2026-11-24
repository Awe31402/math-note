---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 06
lecture: Lecture 4 (Part 1) – PCP via GKR and Interactive Arguments
date: 待補（2023 秋季第四堂課）
video: https://youtu.be/L8PXcZ2ExiU
notes: Thaler §9.1（書頁 134–135，PDF 頁 135–136）。OCW 本講無指定讀物。
---

# 第 06 集 · Lecture 4 (Part 1)：PCP 的定義，以及把 GKR 攤開成 PCP [▶ 影片](https://youtu.be/L8PXcZ2ExiU)

← 上一集：[05-gkr-continuation-ip-pspace](05-gkr-continuation-ip-pspace.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[07-pcp-via-gkr-part2](07-pcp-via-gkr-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 06 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:29:42，MIT 上傳的真人字幕）＋ Thaler §9.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：黑板看不到，公式照口述重建。GKR 的符號沿用第 03–04 集筆記。講者在課堂上當場想了幾個細節（一致性檢查、低次檢驗），筆記照實記下她的思考過程和最後結論。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. PCP 的想法](#1-pcp-的想法)
- [2. 正式定義](#2-正式定義)
  - [2.1 非適應性的驗證者](#21-非適應性的驗證者)
  - [2.2 Q&A](#22-qa)
- [3. 本集要證的定理](#3-本集要證的定理)
- [4. 從 GKR 造 PCP](#4-從-gkr-造-pcp)
  - [4.1 先歸約到 3SAT](#41-先歸約到-3sat)
  - [4.2 參數：為什麼 |F| 只能是 polylog](#42-參數為什麼-f-只能是-polylog)
  - [4.3 PCP 裡放什麼](#43-pcp-裡放什麼)
  - [4.4 驗證者怎麼做](#44-驗證者怎麼做)
  - [4.5 討論：要不要一致性檢查、低次檢驗](#45-討論要不要一致性檢查低次檢驗)
- [5. Soundness](#5-soundness)
- [6. 隨機性與查詢次數](#6-隨機性與查詢次數)
- [7. Q&A：能不能每輪共用隨機數](#7-qa能不能每輪共用隨機數)
- [8. 輸入層需要低次檢驗](#8-輸入層需要低次檢驗)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:12](https://youtu.be/L8PXcZ2ExiU?t=12)

1. **前半**：一個新概念，**可機率檢查的證明**（probabilistically checkable proof, PCP）。定義它，再用 GKR 造出來。
2. **後半**（第 07 集）：**第一次用到密碼學**。到目前為止都是資訊理論的（其實是複雜度理論）。「任何證明者都騙不了」這種保證有極限，所以要放寬成**論證**（argument，計算可靠性）：無限強的證明者也許能騙，但計算受限的證明者騙不了。放寬之後能做到很多以前做不到的事。

【口頭】講者說好久沒見大家，「很多事都變了」，今天可能會有點分心。

---

## 1. PCP 的想法

[▶ 02:21](https://youtu.be/L8PXcZ2ExiU?t=141)

**NP 的證明**：實例 $x$（長度 $n$）、證據 $w$（長度 $m$）。驗證要**讀完整個 $w$**，跑一個驗證電路。

**PCP 的想法**：把 $w$ 轉成一個新的證明 $\pi$，可能**更長**（但仍是 $\mathrm{poly}(n, m)$）。好處是：

> 驗證者**不必讀完** $\pi$，只要**隨機查幾個位置**，再對這幾個位元跑一個驗證電路。

**位置一定要隨機、證明者事先不知道**：如果證明者知道驗證者只看第 17、22、25 位，那等於把證據壓得很短。我們不相信任意證據都能壓短。

【Q&A】[▶ 04:31](https://youtu.be/L8PXcZ2ExiU?t=271) **PCP 只在 $m\gg n$ 時有用嗎？**
不是。就算 $m = n^{o(1)}$ 很短，PCP 長度仍是 $\mathrm{poly}(n)$，等於比原證明大了超過多項式倍。得到的好處是：驗證者只讀**非常少**的位元。

【Q&A】[▶ 05:12](https://youtu.be/L8PXcZ2ExiU?t=312) **驗證者要讀完整個 $x$ 嗎？**
要。漏讀一個位元，就不知道在證明什麼。

【口頭】有一個延伸叫 **PCP of proximity**：驗證者連 $x$ 都不讀完，但保證變成「給驗證者的 oracle 和某個在語言裡的東西很接近」。很有用，但敘述不容易，本課不講。

**已知的結果**（[▶ 06:38](https://youtu.be/L8PXcZ2ExiU?t=398)）：任何證據都能轉成只要讀 **3 個位元**的 PCP，就有一定的 soundness；要更好就重複。
- ⚠️ 逐字稿缺字：字幕寫「7/7 is the parameter」，應是某個小於 1 的常數 soundness（例如 7/8），確切數字聽不清楚（見待確認清單）。

今天不證 3 位元版本，而是證**查詢 polylog 個位元**的版本。要降到常數需要遞迴（recursion）等額外技巧，本課不講。

【口頭】這些不只是漂亮的數學，**實際上有在用**，所以我們在乎效率。

---

## 2. 正式定義

[▶ 08:45](https://youtu.be/L8PXcZ2ExiU?t=525)

> **定義** $\mathrm{PCP}_{c,s}[r, q]$：所有滿足下列條件的語言 $L$。存在一個機率多項式時間（probabilistic polynomial time, PPT）的 **oracle 機器** $V$（以 PCP 為 oracle）：
> 1. **Completeness**：對每個 $x\in L$，**存在**證明 $\pi$ 使 $\Pr\left[ V^{\pi}(x) = 1 \right]\ge c$。
> 2. **Soundness**：對每個 $x\notin L$ 和**每個** $\pi^{*}$，$\Pr\left[ V^{\pi^{*}}(x) = 1 \right]\le s$。
> 3. $V$ 用 $r$ 個隨機位元、做 $q$ 次 oracle 查詢，而且查詢是**非適應性的**（見 2.1）。

- 今天的 PCP，$c = 1$。理想上 $c\to 1$、$s\to 0$。
- 【課堂討論】講者問 soundness 怎麼定義，學生答出：對所有 $\pi'$，接受機率 $\le s$。
- **Oracle 是什麼**（【Q&A】[▶ 10:55](https://youtu.be/L8PXcZ2ExiU?t=655)）：$\pi$ 就是一個字串 $\pi_1\pi_2\cdots\pi_N$。驗證者可以問「給我 $\pi_i$」。不要想成函數，就是能查某個位元的字串。

**密碼學額外的要求**（[▶ 22:03](https://youtu.be/L8PXcZ2ExiU?t=1323)）：對每個 $x\in L$ 和證據 $w$，**給定 $(x, w)$ 能有效率地算出 $\pi$**。不只是存在。

> 【課本補充】Thaler §9.1 Definition 9.1 用錯誤來寫：completeness error $\delta_c$、soundness error $\delta_s$，證明是字母表 $\Sigma$ 上長度 $\ell$ 的字串。Remark 9.2：傳統記號 $\mathrm{PCP}_{\delta_c, \delta_s}[r, q]_{\Sigma}$ 的參數 $r, q, \Sigma$ 對**近似困難度**（hardness of approximation）很重要；在可驗證計算裡，重要的是證明者和驗證者時間，以及查詢次數 $q$（因為轉成簡短論證時，論證長度主要由 $q$ 決定）。證明長度 $\ell$ 是證明者時間的下界。Remark 9.1：PCP 模型由 Fortnow、Rompel、Sipser 提出（叫 oracle 模型），「PCP」這個名字是 Arora 和 Safra 取的。

### 2.1 非適應性的驗證者

[▶ 13:42](https://youtu.be/L8PXcZ2ExiU?t=822)

把 $V$ 拆成兩段：

1. **$V_1$**：只看 $x$ 和隨機數，**不看 oracle**，算出 $q$ 個位置 $i_1, \ldots, i_q$。（通常是隨機的。）
2. **$V_2$**：拿到 $x$、$i_1, \ldots, i_q$、$\pi_{i_1}, \ldots, \pi_{i_q}$，決定接受或拒絕。（通常是決定性的。）

**適應性**的驗證者則是：查 $\pi_{i_1}$，看了結果再決定下一個要查哪裡……

- PCP 文獻通常要求非適應性。這個性質對**應用**很重要：今天後半造簡短論證時就會用到。
- 【口頭】她知道的 PCP 全是非適應性的（沒做完整文獻搜尋）。

### 2.2 Q&A

【Q&A】[▶ 15:50](https://youtu.be/L8PXcZ2ExiU?t=950) **驗證者知道 PCP 的長度 $N$ 嗎？**
知道。$V$ 知道 $n$，也知道語言，所以知道證據長度 $m(n)$；PCP 長度 $N$ 也是 PCP 定義好的參數。證明者、驗證者都知道。

【Q&A】[▶ 16:32](https://youtu.be/L8PXcZ2ExiU?t=992) **允許適應性，會得到或失去什麼？**
失去的是**應用**：等一下用 PCP 造簡短論證時，適應性會出問題。得到什麼？可能可以造出更好的 PCP，但講者不這麼認為，不過不確定。就她所知，要求非適應性不是代價，只是現有的 PCP 剛好都這樣。

【Q&A】[▶ 17:12](https://youtu.be/L8PXcZ2ExiU?t=1032) **查詢位置一定要依賴 $x$ 嗎？**
不用。今天的 PCP，查詢位置**只依賴 $n$**，不依賴 $x$ 本身。

【Q&A】[▶ 17:53](https://youtu.be/L8PXcZ2ExiU?t=1073) **那證明者不就知道會查哪裡了？**
不。位置是從一個**分布**抽出來的，證明者不知道會抽到哪個。重點是分布不依賴 $x$。如果位置是決定性的，就等於把 NP 證據壓短了，我們不相信可能。

---

## 3. 本集要證的定理

[▶ 19:58](https://youtu.be/L8PXcZ2ExiU?t=1198)

> **定理**：$\mathrm{NP}\subseteq\mathrm{PCP}_{1, 1/2}\left[ \mathrm{polylog}(n), \mathrm{polylog}(n) \right]$，而且證明者能有效率地算出 PCP。

（soundness 可以是任何常數，用 1/2 只是因為重複就能降。）

【Q&A】[▶ 20:43](https://youtu.be/L8PXcZ2ExiU?t=1243) Tina：**通常要求隨機性是 $O(\log n)$ 吧？**
對。傳統上（複雜度理論的定義）要求 $O(\log n)$ 隨機位元，是因為這樣**PCP 自動只有多項式大小**：所有可能的隨機串只有 $2^{O(\log n)} = \mathrm{poly}(n)$ 種，能查的位置就這麼多。講者這裡改成直接要求「能有效率地算出 $\pi$」（所以 $\pi$ 是多項式大小），就不那麼在乎隨機位元數。

**已知最好的**（[▶ 23:29](https://youtu.be/L8PXcZ2ExiU?t=1409)）：隨機性 $O(\log n)$、查詢 3 次。

【口頭】「想想看，費馬最後定理，數學裡最難的證明，都能寫成只要看 3 個位元就能檢查的形式。不滿意 1/2 的機率？重複 500 次，被騙的機率就只有 $2^{-500}$。」

【Q&A】[▶ 23:29](https://youtu.be/L8PXcZ2ExiU?t=1409) 學生覺得 $\binom{N}{3}$ 種組合很多。講者：對實務來說，PCP 要線性或準線性大小才好用，平方大小大家就不喜歡了。「但我們還在理論的雲端，多項式就很棒。」

---

## 4. 從 GKR 造 PCP

[▶ 24:51](https://youtu.be/L8PXcZ2ExiU?t=1491)

【口頭】「其實你們已經會造 PCP 了，只是不知道。怎麼造？就是 GKR。把 GKR 攤開就好。」

### 4.1 先歸約到 3SAT

- 3SAT 是 NP 完全的，所以只要對 3SAT 造 PCP。
- 3SAT 的驗證電路（輸入 $\varphi$ 和賦值 $w$，檢查 $\varphi(w) = 1$）**深度很小**：本身深度 2（一層小 OR、一個大 AND），改成 fan-in 2 後深度 $O(\log n)$。GKR 的通訊隨深度成長，所以深度小很重要。
- 這個電路是 **log-space uniform**。再用 Rachel 第 05 集的方法改造（萬用電路等，深度只多 polylog 因子），讓 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ 能有效率地算。

【Q&A】[▶ 39:43](https://youtu.be/L8PXcZ2ExiU?t=2383) **GKR 對電路的限制（log-space uniform）這裡還要嗎？** 要。3SAT 的驗證電路非常規則，是 log-space uniform；再照第 05 集改造，深度仍是 polylog，$\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ 就能有效率地算。

**和 GKR 的差別**：在 GKR 裡驗證者手上有輸入。這裡輸入的一部分是**證據 $w$**（滿足的賦值），驗證者**沒有**。

### 4.2 參數：為什麼 |F| 只能是 polylog

[▶ 31:53](https://youtu.be/L8PXcZ2ExiU?t=1913)

證明者算出每層的閘值 $V_i: H^m\to\{0,1\}$（每層 $S$ 個閘，$|H|^m = S$）和低次擴張 $\tilde{V}_i:\mathbb{F}^m\to\mathbb{F}$。

【口頭】「記得我說過喜歡 $|H| = \log S$、$m = \log S/\log\log S$ 嗎？你們心裡想『還能多煩？』。就是為了現在。」

- $\tilde{V}_i$ 在**所有** $\mathbb{F}^m$ 上的值都要寫進 PCP。所以需要 $|\mathbb{F}|^m = \mathrm{poly}(S)$。
- 取 $|\mathbb{F}| = \mathrm{poly}(|H|) = \mathrm{polylog}(S)$。那麼 $|\mathbb{F}|^m = \mathrm{poly}(|H|)^m = \mathrm{poly}(|H|^m) = \mathrm{poly}(S)$ ✓。
- 如果 $H = \{0,1\}$、$m = \log S$：soundness 要 $|\mathbb{F}|$ 大於 $m\cdot|H|\cdot d$，至少 $\log S$。那 $|\mathbb{F}|^m\ge(\log S)^{\log S}$，**超多項式**。✗

- ⚠️ 逐字稿缺字：[▶ 32:35](https://youtu.be/L8PXcZ2ExiU?t=1955) 講者先把 $S$ 說成 $n$，自己改成 $S$。

### 4.3 PCP 裡放什麼

[▶ 38:20](https://youtu.be/L8PXcZ2ExiU?t=2300)

「我的 PCP 就是 GKR，但完全攤開。」

**(1) 每層的低次擴張**：對每層 $i$、每個 $z\in\mathbb{F}^m$，寫下 $\tilde{V}_i(z)$。
- 包括**輸入層**：可憐的驗證者沒有 $w$，所以給他 $w$ 的低次擴張 $\tilde{w}$。
- 【口頭】[▶ 49:47](https://youtu.be/L8PXcZ2ExiU?t=2987) 只放 $\tilde{w}$，不放 $x$。驗證者有 $x$；如果讓證明者寫 $x$ 而驗證者又不讀，證明者可以寫錯的 $x$。
- 大小：$d\cdot|\mathbb{F}|^m = \mathrm{poly}(S)$。

**(2) 每個可能的 sum-check 的證明者回答**：GKR 裡驗證者要在哪個點 $z$ 做 sum-check，取決於他的隨機數。所以**每個** $i$ 和**每個** $z$ 都要準備一份 sum-check。

sum-check 是對 $p, w_1, w_2\in H^m$ 加總，共 $3m$ 個變數，驗證者每輪送一個隨機體元素 $r_j$。要小心：**不能**把完整的 $(r_1, \ldots, r_{3m})$ 告訴證明者（知道 $r$ 就能作弊）。所以要寫成一棵**樹**：

- 對每個 $r_1\in\mathbb{F}$：寫下證明者看到 $r_1$ 後的回答。（$|\mathbb{F}|$ 個。）
- 對每個 $(r_1, r_2)$：寫下看到 $r_1, r_2$ 後的回答。（$|\mathbb{F}|^2$ 個。）
- ……
- 對每個部分對話紀錄 $(r_1, \ldots, r_j)$，$j = 1, \ldots, 3m$，寫一個回答。

每個回答只依賴到目前為止的隨機數，不能偷看後面的。

**大小**：每棵樹約 $|\mathbb{F}|^{3m} = \mathrm{poly}(S)$（講者說「$S^3$ 左右」）。「看起來是指數樹，它也確實是，但深度很小。」共有 $d\cdot|\mathbb{F}|^m$ 棵（每個 $i$、每個 $z$），總共 $\mathrm{poly}(S)$。

【口頭】這對實務不夠好，但 GKR 有很多最佳化，可以讓 PCP 變成準線性、今天甚至線性。

> 【課本補充】Thaler §9.1 Lemma 9.2 是同樣的想法用在 MIP 上：對每個證明者、驗證者**每一則可能的訊息**，PCP 都有一格寫著證明者的回答；PCP 驗證者模擬 MIP 驗證者，把查到的格子當成證明者的回答。Remark 9.3：如果驗證者對同一個證明者送多則訊息，就把第 $j$ 個問題換成「前 $j$ 則訊息的串接」，確保回答可以依賴先前的訊息（正是講者說的「對每個部分對話紀錄寫一個回答」）。Thaler 也指出：PCP 證明者必須**預先算好所有可能問題的回答**，所以只有在可能的問題數量很少時，證明者才不會太慢。

### 4.4 驗證者怎麼做

[▶ 51:09](https://youtu.be/L8PXcZ2ExiU?t=3069)

驗證者**假裝在和 GKR 證明者互動**，只是證明者「坐在天上」，策略已經全部攤開寫在 oracle 裡：

1. 讀輸出層的值，應該是 1。
2. 從輸出往輸入，一層一層做 GKR：要送隨機數 $r_1$ 時，就去 oracle 查樹上 $r_1$ 那格；再送 $r_2$，查 $(r_1, r_2)$ 那格……
3. 一層的 sum-check 結束，需要 $\tilde{V}_{i+1}$ 在兩個點的值，就去查 (1) 部分。然後進入下一層，用那兩個點的 sum-check 樹。
4. 最後需要輸入的擴張在某點的值。輸入是 $(x, w)$。$(x, w)$ 的擴張在任一點的值，可以寫成「$x$ 的擴張的某個值」和「$w$ 的擴張的某個值」的加權和。$x$ 的部分自己算，$w$ 的部分查 $\tilde{w}$。

正式地：

> $V^{\pi}$：(1) 以 oracle 當證明者，執行 GKR 驗證者 $V_{\mathrm{GKR}}$；(2) 檢查 $\tilde{w}$ 是低次的（見第 8 節）。

### 4.5 討論：要不要一致性檢查、低次檢驗

**一致性**（[▶ 52:33](https://youtu.be/L8PXcZ2ExiU?t=3153)）：講者一開始說要檢查 sum-check 樹裡給的值和 (1) 裡的 $\tilde{V}_{i+1}$ 一致（否則不同分支可能給不同的值）。接著她自己質疑：「其實我不確定需不需要。」

結論（[▶ 54:38](https://youtu.be/L8PXcZ2ExiU?t=3278)～[▶ 55:58](https://youtu.be/L8PXcZ2ExiU?t=3358)）：兩種寫法等價。想成在和證明者互動，作弊的證明者本來就可以在不同分支給不同的值；下一層只要從那兩個值繼續就好。學生總結：「就是把驗證者的隨機性全部攤開，驗證者就像在和證明者互動。」

**$\tilde{V}_i$ 是不是低次的？**（[▶ 56:41](https://youtu.be/L8PXcZ2ExiU?t=3401)）學生問：證明者寫的 $\tilde{V}_i$ 可能根本不是低次多項式，例如一個任意的真值表。要檢查嗎？

講者想了一下：中間層（$i < d$）**不用另外檢查**，GKR 本身的 soundness 已經處理了。理由：

- 任何互動式證明的證明者，都可以看成一棵巨大的樹（對每個可能的問題給一個回答）。把樹寫成 PCP，soundness 自然繼承。
- 一般這棵樹會太大。但 GKR 有「**無記憶**」（memoryless）的性質：做完一個 sum-check 後，之前發生什麼不重要，只需要記得 $\tilde{V}_{i+1}$ 在哪兩點、值是多少。所以不必重複整棵樹，可以用比較有效率的方式攤開。
- 學生：「所以 GKR 的樹大部分是重複的，不用重複寫，查表就好。」講者：「沒錯。」而且這裡其實比 GKR **更限制**證明者：GKR 的作弊證明者可以記住之前的隨機數來調整策略；這裡不行。
- 【口頭】這有點令人困惑：熟悉 PCP 文獻的人知道裡面**總有一個低次檢驗**（low-degree test）。這裡它「藏在 GKR 裡面」。（但輸入層例外，見第 8 節。）

【Q&A】[▶ 64:29](https://youtu.be/L8PXcZ2ExiU?t=3869) **這個轉換不只適用 GKR 吧？只要證明者能有效率地寫成驗證者知道去哪查的序列就行。**
對，任何簡短的互動式證明都可以這樣攤開。但「我們其實只有兩個左右的簡短互動式證明例子」，所以選擇不多。造出簡短的互動式證明本身就是很有趣的問題。

---

## 5. Soundness

[▶ 65:54](https://youtu.be/L8PXcZ2ExiU?t=3954)

【Q&A】[▶ 48:25](https://youtu.be/L8PXcZ2ExiU?t=2905)（先問的）**sum-check 不是需要 $\mathbb{F}$ 很大嗎？** 講者：「勉強，但可以。」

- 有 $2d$ 個 sum-check，作弊只要在**一個**上成功就夠了，所以每個都要夠可靠。
- 每個 sum-check：$3m$ 個變數，每個變數次數 $\approx|H|$，錯誤 $\le 3m\cdot|H|/|\mathbb{F}|$。
- Union bound：

$$\Pr[\text{被騙}] \le 2d\cdot\frac{3m|H|}{|\mathbb{F}|}.$$

- 要 $\le 1/2$：$|\mathbb{F}|\ge 12\,d\,m\,|H|$。$d$、$m$、$|H|$ 都是 $\mathrm{polylog}(S)$，所以 $|\mathbb{F}|$ 還是 polylog，$|\mathbb{F}|^m$ 還是多項式。✓

- 講者後來說（[▶ 74:29](https://youtu.be/L8PXcZ2ExiU?t=4469)）：sum-check 多項式的次數其實受 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ 的次數影響（第 05 集的「夠低」擴張），是 $\mathrm{poly}(|H|)$，但仍是 polylog，結論不變。

**Completeness = 1**：GKR（和 sum-check）的 completeness 是 1。

【Q&A】[▶ 68:50](https://youtu.be/L8PXcZ2ExiU?t=4130) **為什麼 $|\mathbb{F}|^m$ 一定要是多項式？** 因為我們要 PCP 是 $\mathrm{poly}(S)$ 大小，要能有效率地從證據算出來。PCP 大小隨 $|\mathbb{F}|^{3m}$ 成長；如果 $|\mathbb{F}|$ 比 $\mathrm{poly}(|H|)$ 大，$|\mathbb{F}|^m$ 就比 $\mathrm{poly}(|H|^m)$ 大。

【Q&A】[▶ 84:09](https://youtu.be/L8PXcZ2ExiU?t=5049) **Soundness 用了 union bound？** 對。作弊的證明者（一個「手被綁住的 GKR 證明者」）必須在某個 sum-check 從假變真。最後驗證的是證據；沒有滿足的賦值，所以他放的是假的。$2d$ 個 sum-check union bound。

【Q&A】[▶ 85:32](https://youtu.be/L8PXcZ2ExiU?t=5132) **共用隨機數時 union bound 還行嗎？** 行。union bound 不在乎事件怎麼相關：$\Pr[A\cup B]\le\Pr[A] + \Pr[B]$ 永遠成立。

---

## 6. 隨機性與查詢次數

[▶ 70:14](https://youtu.be/L8PXcZ2ExiU?t=4214)

**隨機性**：$2d$ 個 sum-check，每個要 $3m$ 個體元素：

$$r = 2d\cdot 3m\cdot\log|\mathbb{F}| = \mathrm{polylog}(S).$$

注意這是 polylog，不是 $\log S$。

【Q&A】[▶ 69:33](https://youtu.be/L8PXcZ2ExiU?t=4173) / [▶ 71:38](https://youtu.be/L8PXcZ2ExiU?t=4298) **隨機性是 polylog，照理 PCP 會是 $2^{\mathrm{polylog}}$ 那麼大；這裡怎麼變小的？**
因為 GKR 的「遺忘」性質，我們沒有天真地把整棵樹攤開。如果天真地攤開，會是深度很深的巨大樹。學生：「每棵樹是多項式大小，而且只有多項式棵？」講者：「沒錯。我們是一塊一塊打包的。」

**查詢次數**：$2d$ 個 sum-check，每個 $3m$ 輪，每輪讀一個單變數多項式（次數 $\mathrm{poly}(|H|)$，每個係數 $\log|\mathbb{F}|$ 位元）：

$$q = 2d\cdot 3m\cdot\mathrm{poly}(|H|)\cdot\log|\mathbb{F}| = \mathrm{polylog}(S).$$

**回顧**（[▶ 74:29](https://youtu.be/L8PXcZ2ExiU?t=4469)）：「我在第一堂課說 sum-check 是奇蹟，它給你一切。」從 sum-check 出發：重複 sum-check → 任何低深度計算的驗證（GKR）→ IP = PSPACE → 現在攤開 GKR → PCP。而且很直接：算出計算、做所有低次擴張、一輪一輪攤開。

【Q&A】[▶ 76:31](https://youtu.be/L8PXcZ2ExiU?t=4591) **能攤開成多項式大小，是因為 GKR 由獨立的 sum-check 組成，還是因為 sum-check 每個問題只是隨機數？**
兩個都是：
1. 每個 sum-check 做完就可以忘掉隨機數，對每個 $\tilde{V}_i$ 重新開始。所以只要寫 $d\cdot|\mathbb{F}|^m$ 個 sum-check。
2. 每個 sum-check 本身攤開是**對變數數 $m$ 指數**的成本，$|\mathbb{F}|^{3m}$。這裡 $m$ 是 $\log S/\log\log S$、$|\mathbb{F}| = \mathrm{poly}(|H|)$，所以是多項式。這就是要做「參數工程」的原因。

【口頭】[▶ 78:38](https://youtu.be/L8PXcZ2ExiU?t=4718) 「$\log n/\log\log n$，你在開玩笑嗎？找不到好看一點的嗎？」這組參數在 90 年代早期的 PCP 構造裡就一再出現。「我們不是第一個用的，是最後一個。」

---

## 7. Q&A：能不能每輪共用隨機數

[▶ 78:38](https://youtu.be/L8PXcZ2ExiU?t=4718)

【Q&A】**PCP 的證明者是非適應性的（不記得之前的隨機數），那能不能讓 $d$ 層的 sum-check 都用同一組隨機數，省掉 $d$ 因子？**

講者一開始答「不行」：在 GKR 裡，作弊的證明者會在第一層故意作弊、學到你的隨機數，之後利用它。這裡的驗證者應該表現得像誠實的 GKR 驗證者。

學生澄清：這裡的證明者手被綁住了，他不記得隨機數，只依賴 $\tilde{V}_{i-1}$。講者：「喔，現在我懂你的問題了。很好的問題。」

其他學生反駁：證明者雖然不記得隨機數，但他**事先知道**隨機數會重複，可以把所有回答設計成利用這種相關性。

講者結論：「這個討論非常有趣。我們這門課有一份作業，你給了我一個好題目。」（沒有在課堂上下定論。）

**作業公告**（[▶ 83:26](https://youtu.be/L8PXcZ2ExiU?t=5006)）：網站上原本寫作業在後面才出，但講者考慮提早出、給兩週。時間不行就跟她說可以延期：「說實話我不太在意，只是想讓你們想想、玩玩這些材料。」

---

## 8. 輸入層需要低次檢驗

[▶ 84:50](https://youtu.be/L8PXcZ2ExiU?t=5090)

講者在回答 union bound 的問題時突然想起來：「等一下，有一件事。我們需要一個低次檢驗。」

學生同時指出：**第一層**（輸入層）。在 GKR 裡，驗證者**有輸入**（證據），自己算低次擴張。在這裡，**$\tilde{w}$ 是證明者給的**。如果他給的根本不是低次多項式呢？GKR 的分析假設最後查的是一個真正的低次擴張。

所以：

> **需要對 $\tilde{V}_d = \tilde{w}$ 做一次低次檢驗（low-degree test）。除此之外，就是黑盒的 GKR。**

【口頭】GKR 的一個好性質在這裡被用到：驗證者最後只需要**輸入的擴張在兩個點的值**。現在證據在天上（PCP 裡），驗證者讀不完，但讀得了簡短協定要他讀的那幾個點。

低次檢驗怎麼做：休息後（第 07 集）講。

---

## 9. 一頁速查表

### PCP 定義

- $\mathrm{PCP}_{c,s}[r, q]$：$x\in L$ ⟹ $\exists\pi$，$\Pr[V^{\pi}(x) = 1]\ge c$；$x\notin L$ ⟹ $\forall\pi^{*}$，$\Pr\le s$。$r$ 隨機位元、$q$ 次查詢。
- 非適應性：$V_1(x; \text{隨機})\to(i_1, \ldots, i_q)$，$V_2(x, i, \pi_i)\to\{0,1\}$。
- 密碼學要求：$\pi$ 可從 $(x, w)$ 有效率算出。
- 已知：$\mathrm{NP} = \mathrm{PCP}[O(\log n), 3]$。

### 從 GKR 造的 PCP

- 對 3SAT 驗證電路（深度 polylog、log-space uniform）。
- 參數：$|H| = \log S$、$m = \log S/\log\log S$、$|\mathbb{F}| = \mathrm{polylog}(S)$ ⟹ $|\mathbb{F}|^m = \mathrm{poly}(S)$。
- $\pi$ 包含：(1) 所有 $\tilde{V}_i(z)$，$z\in\mathbb{F}^m$（含 $\tilde{w}$，不含 $x$）；(2) 對每個 $(i, z)$，sum-check 證明者對每個部分對話紀錄 $(r_1, \ldots, r_j)$ 的回答，每棵樹 $|\mathbb{F}|^{3m}$。
- 驗證者：以 $\pi$ 當證明者跑 GKR 驗證者；對 $\tilde{w}$ 做低次檢驗。

| | |
|---|---|
| Completeness | 1 |
| Soundness | $\le 2d\cdot 3m|H|/|\mathbb{F}|$；取 $|\mathbb{F}|\ge 12dm|H|$ 得 1/2 |
| 隨機性 | $2d\cdot 3m\log|\mathbb{F}| = \mathrm{polylog}$ |
| 查詢 | $2d\cdot 3m\cdot\mathrm{poly}|H|\cdot\log|\mathbb{F}| = \mathrm{polylog}$ |
| 長度 | $d\cdot|\mathbb{F}|^m\cdot|\mathbb{F}|^{3m} = \mathrm{poly}(S)$ |

**為什麼長度是多項式**：(1) GKR 無記憶，每層每個 $z$ 一棵 sum-check 樹；(2) 每棵樹 $|\mathbb{F}|^{3m}$，因為參數選得好所以是多項式。

**為什麼只有輸入層要低次檢驗**：中間層由 GKR 的 soundness 處理；輸入層在 GKR 裡是驗證者自己算的，這裡改成證明者給。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 對 $\tilde{w}$ 的低次檢驗 | 第 07 集 |
| 非適應性的 PCP | 第 07–09 集：Kilian–Micali 用 PCP 造簡短論證（Merkle 樹） |
| 論證（計算可靠性） | 第 07 集起：第一次用密碼學 |
| 「共用隨機數」的問題 | 作業（講者說會出成題目） |

---

## 附：本集一句話總結

> **PCP 讓驗證者只隨機查幾個位元就能檢查證明；把 GKR 證明者對「每一層、每個點、每個部分隨機數」的回答全部預先寫下，就是一個 polylog 查詢的 PCP——參數 $|H| = \log S$、$|\mathbb{F}| = \mathrm{polylog}$ 讓它只有多項式大小，而唯一要另外補的是對證據擴張 $\tilde{w}$ 的低次檢驗。**

---

## ⚠️ 待確認清單

1. [▶ 06:38](https://youtu.be/L8PXcZ2ExiU?t=398) 3 位元 PCP 的 soundness 參數，字幕寫「7/7」，確切數字聽不清楚（可能是 7/8 之類的常數）。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 4 Part 1 錄影逐字稿（MIT 真人字幕，1:29:42）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§9.1 整理。*
