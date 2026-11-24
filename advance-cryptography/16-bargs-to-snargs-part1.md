---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 16
lecture: Lecture 9 (Part 1) – BARGs Implies SNARGs and Connection to Non-Signaling PCPs
date: 待補（2023 秋季最後一堂課）
video: https://youtu.be/nmuXpvSIm3k
notes: OCW 指定讀物 Choudhuri–Jain–Jin「SNARGs for P from LWE」（ePrint 2021/808）、Kalai–Vaikuntanathan–Zhang「Somewhere Statistical Soundness, Post-Quantum Security, and SNARGs」（ePrint 2021/788）——均未取得，只依逐字稿。
---

# 第 16 集 · Lecture 9 (Part 1)：從 BARG 到 SNARG——某處可萃取雜湊、雜湊所有線路＋BARG 所有閘 [▶ 影片](https://youtu.be/nmuXpvSIm3k)

← 上一集：[15-bargs-from-lwe-part2](15-bargs-from-lwe-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[17-bargs-to-snargs-part2](17-bargs-to-snargs-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 16 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:27:28，MIT 上傳的真人字幕）。OCW 指定論文未取得，**本集沒有次要來源**。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：字幕把「SSB」聽成「FSB」等，筆記直接改正。黑板看不到，符號照口述重建。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. BARG 回顧與半適應性 soundness](#1-barg-回顧與半適應性-soundness)
  - [1.1 為什麼不能用「猜」升級成完全適應性](#11-為什麼不能用猜升級成完全適應性)
- [2. 某處可萃取雜湊](#2-某處可萃取雜湊)
  - [2.1 定義](#21-定義)
  - [2.2 推論：所有位置都計算綁定](#22-推論所有位置都計算綁定)
  - [2.3 綁定 ℓ 個位置](#23-綁定-ℓ-個位置)
- [3. BARG 的兩個額外性質](#3-barg-的兩個額外性質)
  - [3.1 索引語言：驗證者不用讀全部實例](#31-索引語言驗證者不用讀全部實例)
  - [3.2 某處可萃取的 BARG](#32-某處可萃取的-barg)
- [4. 再談某處可萃取雜湊的構造](#4-再談某處可萃取雜湊的構造)
  - [4.1 天真的做法為什麼不夠](#41-天真的做法為什麼不夠)
  - [4.2 每層換金鑰、在加密底下解密](#42-每層換金鑰在加密底下解密)
- [5. SNARG 的構造](#5-snarg-的構造)
  - [5.1 想法](#51-想法)
  - [5.2 和 GKR 的差別](#52-和-gkr-的差別)
  - [5.3 演算法](#53-演算法)
  - [5.4 效率](#54-效率)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:13](https://youtu.be/nmuXpvSIm3k?t=13)

最後一堂課（「很開心可以放假，但我還有好多想跟你們說」）。講者帶了餅乾。

**目標**：終於要造出整門課在追的 **SNARG**（succinct non-interactive argument，簡短非互動論證）。材料：
1. 上一堂 Jin 講的 **BARG**；
2. **某處可萃取雜湊**（somewhere extractable hash）：就是 Jin 說的 SSB 雜湊（somewhere statistically binding），文獻兩個名字都用。

【口頭】BARG 本身有趣，但讓它**超級**有趣的是：可以很直接地用它造 SNARG。

---

## 1. BARG 回顧與半適應性 soundness

[▶ 02:15](https://youtu.be/nmuXpvSIm3k?t=135)

> **BARG**（NP 語言 $L$）：
> - $\mathrm{Gen}(1^{\lambda}, k, n)\to\mathrm{CRS}$：$\lambda$ 一進位；$k$（實例數）、$n$（每個實例長度）二進位，所以時間 $\mathrm{polylog}(k, n)$。
> - $P(\mathrm{CRS}, (x_1, w_1), \ldots, (x_k, w_k))\to\pi$，$|\pi| = \mathrm{poly}(\lambda, |w|, \log k)$：只依賴**一個**證據的長度，對 $k$ 是 polylog。
> - $V(\mathrm{CRS}, x_1, \ldots, x_k, \pi)\to\{0, 1\}$。
>
> **Completeness**：有合法證據，證明以機率 1 被接受。

**soundness 的時機問題**：作弊者在看到 CRS **之前**還是**之後**選 $x$？之前選是非適應性；之後選是適應性。理想上要適應性。能做到的是中間的：

> **半適應性 soundness**：對每個多項式大小的 $P^{*}$ 和每個 $i$（可依賴 $\lambda$），
> $$\Pr\left[ (x_1, \ldots, x_k, \pi)\leftarrow P^{*}(\mathrm{CRS}):\ x_i\notin L\ \wedge\ V(\mathrm{CRS}, x_1, \ldots, x_k, \pi) = 1 \right]\le\mathrm{negl}.$$
> 作弊者可以**看了 CRS 再選實例**，但**要在哪個位置 $i$ 作弊**必須事先決定。

【Q&A】[▶ 09:23](https://youtu.be/nmuXpvSIm3k?t=563) **其他位置要在語言裡嗎？** 不用管，愛怎麼選都行。他贏的條件是 $x_i\notin L$ 且證明被接受。

### 1.1 為什麼不能用「猜」升級成完全適應性

【Q&A】[▶ 10:05](https://youtu.be/nmuXpvSIm3k?t=605) **猜 $i$ 能升級成完全適應性嗎？**

可以猜，$1/k$ 機率猜中，但不夠。理由在分析的方式：

- 分析時把 CRS 換成一個**分布很不一樣、但不可區分**的 CRS，裡面偷偷「寫死」了 $i$（某處可萃取雜湊綁定在 $i$）。作弊者分不出來，還是給出合法的 BARG；但在新 CRS 下他**不可能**在位置 $i$ 作弊。
- 如果作弊者是適應性的：你猜他在位置 7 作弊、把 CRS 寫死在 7，他可能就**改到別的位置**作弊，躲開你。
- 你說「他換了位置我就分得出來」？不行：判斷 $x_i$ 在不在語言裡可能非常難。也許換了 CRS 之後 $x_i$ 也跟著變成在語言裡，而你分不出「在」和「不在」。

【Q&A】[▶ 12:53](https://youtu.be/nmuXpvSIm3k?t=773) 叫他承諾？他說什麼我們都不信；他作弊時我們不知道哪個 $x_i$ 是假的。

---

## 2. 某處可萃取雜湊

### 2.1 定義

[▶ 14:17](https://youtu.be/nmuXpvSIm3k?t=857)

> **某處可萃取雜湊**（somewhere extractable hash）：五個 PPT 演算法
> - $\mathrm{Gen}(1^{\lambda}, N, i)\to(hk, td)$：雜湊 $N$ 位元，可萃取的位置是 $i$；$td$ 是陷門。
> - $\mathrm{Eval}(hk, x\in\{0,1\}^N)\to v$（簡短）。
> - $\mathrm{Open}(hk, x, j)\to\rho_j$（$\mathrm{poly}(\lambda)$）。
> - $\mathrm{Ver}(hk, v, j, b, \rho)\to\{0, 1\}$。
> - $\mathrm{Ext}(td, v)\to$ 一個位元（應是 $x_i$）。
>
> **Completeness**：對每個 $x$、$\lambda$、$N\le 2^{\lambda}$、$i$、$j$，誠實地做：$\mathrm{Ver}(hk, v, j, x_j, \rho_j) = 1$，而且 $\mathrm{Ext}(td, v) = x_i$，機率 1。
>
> **索引隱藏**（index hiding）：對每個 $i, j$，$hk^{(i)}\approx_c hk^{(j)}$。
>
> **某處統計綁定**（SSB）：對**每個（無限強的）**攻擊者 $A$，
> $$\Pr_{hk\leftarrow\mathrm{Gen}(1^{\lambda}, N, i)}\left[ (v, \rho_0, \rho_1)\leftarrow A(hk):\ \forall b,\ \mathrm{Ver}(hk, v, i, b, \rho_b) = 1 \right]\le\mathrm{negl}.$$

- 【Q&A】[▶ 24:26](https://youtu.be/nmuXpvSIm3k?t=1466) **$v$ 要是 Eval 產生的嗎？** 不用，$v$ 是惡意的、隨他怎麼產生。
- 【Q&A】[▶ 25:07](https://youtu.be/nmuXpvSIm3k?t=1507) 學生：所以光有萃取不夠推出綁定？對：誠實的 $v$ 裡確實坐著 $x_i$；但惡意的 $v$ 可能萃取不出任何東西。
- 【Q&A】[▶ 25:49](https://youtu.be/nmuXpvSIm3k?t=1549) 等價說法：對幾乎所有金鑰，**根本不存在**這樣的 $(v, \rho_0, \rho_1)$。

### 2.2 推論：所有位置都計算綁定

[▶ 26:34](https://youtu.be/nmuXpvSIm3k?t=1594)

綁定只說了位置 $i$。其他位置 $j$ 呢？

> **推論**：對每個**多項式大小**的 $A$（不是無限強）和每個 $j$，$A$ 在位置 $j$ 給出兩個合法打開的機率可忽略。

【課堂討論】學生答：因為**索引隱藏**。如果 $A$ 能在 $j$ 做到，把金鑰換成綁定在 $j$ 的，$A$ 分不出來，仍以不可忽略的機率做到，但這在資訊理論上不可能。

### 2.3 綁定 ℓ 個位置

[▶ 29:59](https://youtu.be/nmuXpvSIm3k?t=1799)

產生 $hk_1, \ldots, hk_{\ell}$，分別綁定在 $i_1, \ldots, i_{\ell}$。雜湊值是 $(v_1, \ldots, v_{\ell})$，$v_t = \mathrm{Eval}(hk_t, x)$；打開時給每把金鑰的打開。雜湊值長度乘 $\ell$。

**額外性質**：就算公開其中一些陷門（例如 $td_1, td_2, td_3$），其他的索引（$hk_4$ 綁定在哪）仍然完全隱藏，因為是獨立產生的。（給了陷門，那把金鑰的索引就全知道了。）SNARG 會用到這點。

---

## 3. BARG 的兩個額外性質

### 3.1 索引語言：驗證者不用讀全部實例

[▶ 33:39](https://youtu.be/nmuXpvSIm3k?t=2019)

$V$ 是多項式時間，但輸入 $x_1, \ldots, x_k$ 很大，所以至少 $\mathrm{poly}(k)$。但我們的 BARG（Jin 說的**索引語言**的 BARG）：

> 若存在簡短描述 $M$ 使 $x_i = M(i)$，則驗證者時間只隨 $|M|$ 成長，**不隨 $k$ 成長**（只有 $\log k$，因為要讀索引）。

可以想成 $x_i = (M, i)$。

【口頭】「我忘了帶彩色粉筆，抱歉。但至少你們有餅乾。彩色粉筆和餅乾，你們選哪個？」

【Q&A】[▶ 36:29](https://youtu.be/nmuXpvSIm3k?t=2189) **CRS 對 $k$ 也是次線性的嗎？** 一般希望如此；Jin 講的 LWE 構造 CRS 是 $\mathrm{polylog}(k)$。

### 3.2 某處可萃取的 BARG

【Q&A】[▶ 37:10](https://youtu.be/nmuXpvSIm3k?t=2230)

**更強的需求**：不只「作弊者不能在位置 $i$ 作弊」，而是能把 CRS 換成某個分布（看起來一樣），用陷門**從作弊者身上萃取出 $x_i$ 的證據**。這叫**某處可萃取的 BARG**。

**任何 BARG 都能加上這個性質**：叫證明者附上**所有證據的某處可萃取雜湊**，然後 BARG 的不是原本的 $L$，而是升級版：「對每個 $i$，我有雜湊在 $w_i$ 那些位置的合法打開，而且打開出來的 $w_i$ 是 $x_i$ 的合法證據」。分析時讓雜湊綁定在 $w_i$ 的位置；由 soundness，那裡坐著的一定是正確的證據，用陷門萃取出來。

學生追問：有沒有從比「某處可萃取雜湊」更弱的假設造出的 BARG？講者：她不知道怎麼從造不出某處可萃取雜湊的假設造 BARG。

---

## 4. 再談某處可萃取雜湊的構造

[▶ 41:20](https://youtu.be/nmuXpvSIm3k?t=2480)

【口頭】「我想確定你們沒有錯過上一堂講得太快的部分。」

### 4.1 天真的做法為什麼不夠

$N = 2^n$（不是就補齊）。

- $\mathrm{Gen}$：$hk = (pk, \mathrm{Enc}(pk, i_1), \ldots, \mathrm{Enc}(pk, i_n))$（$i$ 的每個位元），$td = sk$。
- $\mathrm{Eval}$：Merkle 樹的形式，每個節點放一個密文。第 1 層：每對葉子 $(x_1, x_2)$，依 $\mathrm{Enc}(i_1)$ 在 FHE 底下挑一個（$i_1 = 0$ 挑左、$1$ 挑右）。第 2 層依 $\mathrm{Enc}(i_2)$ 挑……樹根是 $\mathrm{Enc}(x_i)$。
- 【Q&A】學生：像 OT（不經意傳輸）？「真的很像 OT。」
- 打開：給路徑上的密文和兄弟，驗證者檢查每個節點的密文是兩個子節點和那層加密位元的**決定性同態求值**。

**問題：不知道怎麼證明綁定**（[▶ 48:28](https://youtu.be/nmuXpvSIm3k?t=2908)）：惡意攻擊者可以給**垃圾**密文（根本不是合法密文，解不開）。也許能造出一個解不開的 $v$，卻有兩種合法打開。「也許對自然的構造是綁定的，但我不會證，也許能找到奇怪的 FHE 讓它不綁定。」

### 4.2 每層換金鑰、在加密底下解密

[▶ 50:35](https://youtu.be/nmuXpvSIm3k?t=3035)

- 用 $n$ 把公鑰 $pk_1, \ldots, pk_n$，第 $j$ 層用 $pk_j$。
- 用 $pk_j$ 加密 $i_j$，**以及上一層的秘密鑰 $sk_{j-1}$**。
- 每個節點的同態運算（在 $pk_j$ 的加密底下）：
  1. 用 $sk_{j-1}$ **解密**兩個子節點的密文，得到 $\alpha_0, \alpha_1$（解不開的就是「壞」）；
  2. 依 $i_j$ 輸出 $\alpha_{i_j}$。
  - 結果是 $pk_j$ 下的密文。

**為什麼這樣就綁定**（[▶ 52:05](https://youtu.be/nmuXpvSIm3k?t=3125)）：打開時給的**兄弟**密文可能是壞的，但我們要的是**路徑上**的密文都格式正確。在綁定的位置 $i$，路徑上每一步挑的都是「好的那個子節點」（由歸納法，從葉子開始是對的），壞的兄弟被丟掉，然後重新加密到下一把金鑰。所以路徑上每個節點都是 $\mathrm{Enc}(x_i)$，一直到根。不可能打開成兩種。

- 【Q&A】驗證者也做同樣的計算來檢查？對。
- 【Q&A】[▶ 57:53](https://youtu.be/nmuXpvSIm3k?t=3473) 這只綁定金鑰裡加密的那個 $i$；其他 $j$ 由索引隱藏得到計算綁定。
- 【Q&A】[▶ 57:53](https://youtu.be/nmuXpvSIm3k?t=3473) **能不能只用一把金鑰、加密自己的秘密鑰？** 可以，但要依賴**循環安全**。
- 【Q&A】[▶ 58:34](https://youtu.be/nmuXpvSIm3k?t=3514) 抗碰撞嗎？對綁定的 $i$，統計綁定。
- 【Q&A】[▶ 59:14](https://youtu.be/nmuXpvSIm3k?t=3554) 兩個在位置 $i$ 相同、其他不同的 $x$，誠實雜湊值會不同（看起來很不一樣），但解密都得到 $x_i$。
- 【Q&A】[▶ 60:37](https://youtu.be/nmuXpvSIm3k?t=3637) **為什麼這裡不需要循環安全？** 從來沒有用一把公鑰加密它自己的秘密鑰。學生：而且一般的 FHE 要「無界」還得假設循環安全 LWE。講者：這裡的計算很特定、深度很淺，**不需要完全的 FHE**，只要有界深度的同態加密。

---

## 5. SNARG 的構造

### 5.1 想法

[▶ 62:03](https://youtu.be/nmuXpvSIm3k?t=3723)

學生：「三個月後，我們 SNARG 了。」講者：「最後兩小時，我們 SNARG。」「簡單到你們自己就做得出來。」

語言 $L$ 有驗證電路 $C$（$C(x, w)$ 或決定性的 $C(x)$）。要證 $C(x) = 1$：

1. **雜湊所有線路**：證明者算出電路所有線路的值，用**某處可萃取雜湊**雜湊起來（壓縮的），送出雜湊值。
2. **BARG 所有閘**：對**每個閘**，證明「存在兩條輸入線和一條輸出線的合法打開，而且打開的值滿足這個閘」。
3. 也證明**輸出線是 1**。

### 5.2 和 GKR 的差別

【Q&A】[▶ 66:10](https://youtu.be/nmuXpvSIm3k?t=3970) **和 GKR 有什麼不同？**
- GKR 是互動協定（可以套 Fiat–Shamir）：算出所有線路，但不是 BARG「所有線路都滿足」，而是從輸出線的宣稱出發，用 sum-check 一層一層化簡，直到葉子。
- 這裡從 BARG 出發。Jin 的 BARG 構造用了 Fiat–Shamir，但**有些 BARG 構造根本不用** Fiat–Shamir，有很多種。除了 BARG 內部可能有的東西之外，這裡沒有互動：就是雜湊所有線路、證明一切一致。

### 5.3 演算法

[▶ 68:19](https://youtu.be/nmuXpvSIm3k?t=4099)

**材料**：BARG（索引語言、半適應性 soundness）、某處可萃取雜湊。

**$\mathrm{Gen}(1^{\lambda}, n)$**：
1. $hk\leftarrow\mathrm{Hash.Gen}(1^{\lambda}, N, (i_1, \ldots, i_{\ell}))$：$N$ = 電路 $C$ 的線路數；綁定 $\ell$ 個位置，**位置隨便選**（例如全是 1）。$\ell$ 是參數，越大越「安全」但越不簡短；理想上 $\ell = \mathrm{polylog}$。
2. $\mathrm{CRS}_{\mathrm{BARG}}\leftarrow\mathrm{BARG.Gen}(1^{\lambda}, K, n')$：$K$ = 閘的數目，$n'$ 是 BARG 實例長度。
3. 輸出 $\mathrm{CRS} = (hk, \mathrm{CRS}_{\mathrm{BARG}})$。

【Q&A】[▶ 74:34](https://youtu.be/nmuXpvSIm3k?t=4474) **對 $\ell$ 的依賴能次線性嗎？** 雜湊值 $v$ 不行：要萃取 $\ell$ 個位元，資訊理論上至少那麼長。雜湊金鑰可以：如果 $i_1, \ldots, i_{\ell}$ 有簡短描述（例如證據的連續位置，只要寫起點），就能讓金鑰變小，「我們確實知道怎麼做」。

**$P(\mathrm{CRS}, x, w)$**：
1. 算出所有線路 $w_1, \ldots, w_N$（不含 $x$ 的輸入線，那是驗證者知道的；有證據的話，前幾條就是證據）。
2. $v := \mathrm{Hash.Eval}(hk, (w_1, \ldots, w_N))$。
3. 對每個閘 $j = 1, \ldots, K$：
   - 實例 $x_j^{*} := (hk, v, j)$；
   - 證據 $w_j^{*} := (b_L, \rho_L, b_R, \rho_R, b_{\mathrm{out}}, \rho_{\mathrm{out}})$：左輸入線、右輸入線、輸出線的值和打開。
   - 合法 ⟺ 三個打開都通過（對閘 $j$ 的三條線的編號），而且 $b_{\mathrm{out}} = \mathrm{gate}_j(b_L, b_R)$。輸出閘還要 $b_{\mathrm{out}} = 1$。
4. $\pi_{\mathrm{BARG}}\leftarrow\mathrm{BARG.P}(\mathrm{CRS}_{\mathrm{BARG}}, (x_j^{*}, w_j^{*})_{j=1}^{K})$。
5. 輸出 $(v, \pi_{\mathrm{BARG}})$。

- 電路是 uniform 的：每個閘 $j$ 對應哪三條線是知道的。
- 【Q&A】[▶ 79:37](https://youtu.be/nmuXpvSIm3k?t=4777) 所有閘用**同一把**雜湊金鑰（綁定 $\ell$ 個位置的那一把）。
- 【Q&A】[▶ 80:18](https://youtu.be/nmuXpvSIm3k?t=4818) $x_j^{*}$ 之間只差 $j$：這是**索引語言**。
- 第一層的閘的輸入線是 $x$，所以 BARG 的關係要知道 $x$。

**$V(\mathrm{CRS}, x, (v, \pi_{\mathrm{BARG}}))$**：接受 ⟺ $\mathrm{BARG.V}(\mathrm{CRS}_{\mathrm{BARG}}, (x_j^{*})_{j=1}^{K}, \pi_{\mathrm{BARG}}) = 1$。

### 5.4 效率

[▶ 84:07](https://youtu.be/nmuXpvSIm3k?t=5047)

- BARG 驗證者的輸入是 $K$ 個實例（$K$ ≈ 電路大小），**不能讓驗證者跑 $K$ 時間**。沒問題：$x_j^{*} = (hk, v, j)$ 是**索引語言**，簡短描述就是 $(hk, v)$，所以驗證者時間只是 $\mathrm{poly}(|hk|, |v|, \log K)$。「沒有這個性質，就不能用在 SNARG 上。」
- **SNARG 長度** = $|v| + |\pi_{\mathrm{BARG}}|$：BARG 證明是 $\mathrm{polylog}(K)$（電路大小的 polylog）；$|v|$ 隨 $\ell$ 成長，希望 $\ell = \mathrm{polylog}(K)$。
- **驗證時間**：$\mathrm{polylog}(K)$ 加上讀 $x$（第一層的閘要用 $x$）。

**下半場**（第 17 集）：分析，以及 $\ell$ 要多大。

---

## 6. 一頁速查表

### BARG

- $|\pi| = \mathrm{poly}(\lambda, |w|, \log k)$。
- 半適應性 soundness：作弊位置 $i$ 事先決定，實例可看 CRS 後選。猜 $i$ 不能升級成完全適應性（換 CRS 後作弊者可能換位置，而 $x_i\in L$ 難判斷）。
- 索引語言：$x_i = M(i)$ ⟹ 驗證時間 $\mathrm{poly}(|M|, \log k)$。
- 某處可萃取 BARG：附上證據的某處可萃取雜湊，BARG 升級版語言。

### 某處可萃取雜湊

- $\mathrm{Gen}(1^{\lambda}, N, i)\to(hk, td)$；Eval、Open、Ver、Ext。
- 索引隱藏、在 $i$ 統計綁定 ⟹ 所有位置計算綁定。
- $\ell$ 個位置：$\ell$ 把獨立金鑰；公開部分陷門不洩漏其他索引。
- 構造：Merkle 形式，每層 $pk_j$ 加密 $(i_j, sk_{j-1})$，每個節點在加密底下**解密兩個子節點再挑一個**（擋掉垃圾兄弟）；或單一金鑰＋循環安全。只需有界深度同態。

### SNARG

- CRS $= (hk_{\ell\text{ 位置}}, \mathrm{CRS}_{\mathrm{BARG}})$。
- 證明 $= (v = \mathrm{Hash}(\text{所有線路}),\ \pi_{\mathrm{BARG}})$，BARG：對每個閘 $j$，$(hk, v, j)$ 有三條線的合法打開且滿足閘（輸出閘為 1）。
- 驗證 = BARG 驗證（索引語言，不用跑 $K$ 時間）。
- 長度 $\approx\ell\cdot\mathrm{poly}(\lambda) + \mathrm{polylog}(K)$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| SNARG 的 soundness 分析、$\ell$ 要多大 | 第 17 集 |
| 「局部 soundness」與非信號 PCP | 第 17 集（OCW 第 9 講主題） |

---

## 附：本集一句話總結

> **SNARG 的構造簡單到不可思議：用某處可萃取雜湊把電路所有線路的值壓成一個 $v$，再用 BARG 證明「每一個閘的三條線都有合法打開而且滿足閘、輸出是 1」；因為每個 BARG 實例只是 $(hk, v, j)$，是索引語言，驗證者不用碰整個電路。**

---

## ⚠️ 待確認清單

1. OCW 第 9 講的兩篇指定讀物（Choudhuri–Jain–Jin ePrint 2021/808、Kalai–Vaikuntanathan–Zhang ePrint 2021/788）未取得；本集的構造與定義只依逐字稿，沒有對照論文。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 9 Part 1 錄影逐字稿（MIT 真人字幕，1:27:28）整理；本集無次要來源。*
