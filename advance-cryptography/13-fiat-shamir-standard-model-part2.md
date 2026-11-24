---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 13
lecture: Lecture 7 (Part 2) – Soundness of the Fiat-Shamir Paradigm in the Standard Model
date: 待補（2023 秋季第七堂課，後段）
video: https://youtu.be/GAF78dg8-nE
notes: OCW 指定讀物 Canetti–Lombardi–Wichs（ePrint 2018/1248）——未取得，只依逐字稿。
---

# 第 13 集 · Lecture 7 (Part 2)：NIZK、相關性難解雜湊、推廣到 sum-check [▶ 影片](https://youtu.be/GAF78dg8-nE)

← 上一集：[12-fiat-shamir-standard-model-part1](12-fiat-shamir-standard-model-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[14-bargs-from-lwe-part1](14-bargs-from-lwe-part1.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 13 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:04:59，MIT 上傳的真人字幕）。指定論文未取得，**本集沒有次要來源**。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：符號沿用第 12 集筆記：FHE 金鑰 $(pk, sk)$、承諾的陷門 $td$、壞挑戰 $\beta_{\mathrm{bad}}(\alpha)$、CLW 雜湊 $H_{hk}(\alpha) = \mathrm{FHE.Eval}(pk, U_{\alpha}, \hat{g})$。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Fiat–Shamir 後的協定](#1-fiatshamir-後的協定)
- [2. 非互動零知識（NIZK）的定義](#2-非互動零知識nizk的定義)
- [3. 為什麼是 NIZK：模擬器可以設定 CRS](#3-為什麼是-nizk模擬器可以設定-crs)
  - [3.1 誠實驗證者零知識](#31-誠實驗證者零知識)
  - [3.2 改一下雜湊：加上隨機的 z](#32-改一下雜湊加上隨機的-z)
  - [3.3 模擬器](#33-模擬器)
  - [3.4 為什麼不再矛盾](#34-為什麼不再矛盾)
- [4. 這個技巧用到了什麼](#4-這個技巧用到了什麼)
- [5. 相關性難解雜湊](#5-相關性難解雜湊)
  - [5.1 定義](#51-定義)
  - [5.2 和 Fiat–Shamir 的關係](#52-和-fiatshamir-的關係)
  - [5.3 CLW 定理](#53-clw-定理)
  - [5.4 證明（同一個雜湊）](#54-證明同一個雜湊)
  - [5.5 Q&A](#55-qa)
- [6. 應用：sum-check（想法）](#6-應用sum-check想法)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:12](https://youtu.be/GAF78dg8-nE?t=12)

1. 套用 Fiat–Shamir 後得到 **NIZK**（非互動零知識證明）。
2. 回答上半場的問題：這和「Fiat–Shamir 與零知識互相矛盾」有什麼關係。
3. 說明這個技巧更一般：**相關性難解雜湊**（correlation intractable hash）。

---

## 1. Fiat–Shamir 後的協定

[▶ 00:53](https://youtu.be/GAF78dg8-nE?t=53)

- **CRS**：承諾用的公鑰 $pk_{\mathrm{com}}$，加上 Fiat–Shamir 的雜湊金鑰 $hk$。
- **證明**：一則訊息 $(\alpha, \beta, \gamma)$，其中 $\beta$ 必須是 $H_{hk}(G, \alpha)$（證明者的手被綁住）。
- 【口頭】講者在黑板上把實例 $G$ 省略了，其實 Fiat–Shamir 是對「實例和第一則訊息」取雜湊。
- 非互動、complete，在循環安全 FHE 下 sound（第 12 集）。

【Q&A】[▶ 03:00](https://youtu.be/GAF78dg8-nE?t=180) **用了計算假設，所以是 NIZK「論證」？** 可以做成證明或論證，等一下談。

---

## 2. 非互動零知識（NIZK）的定義

[▶ 04:27](https://youtu.be/GAF78dg8-nE?t=267)

> **NIZK**：對語言 $L$，存在 PPT 模擬器 $\mathrm{Sim}$，使得對每個 $x\in L$（有證據 $w$）和每個輔助資訊 $\mathrm{aux}$：
> $$\left( \mathrm{CRS},\ \pi\leftarrow P(\mathrm{CRS}, x, w),\ \mathrm{aux} \right)\ \approx_c\ \left( \mathrm{Sim}(x, \mathrm{aux}),\ \mathrm{aux} \right).$$
> 左邊是驗證者在真實世界看到的：CRS（也包含安全參數）和真證明者給的證明。$\mathrm{Sim}$ 輸出一個 CRS 和一個假證明。

- 有沒有 $\mathrm{aux}$ 是兩種版本；**輔助輸入零知識**比較強，通常要這個。
- 【Q&A】[▶ 07:54](https://youtu.be/GAF78dg8-nE?t=474) 學生：非互動就不需要 $V^{*}$ 了？對，驗證者什麼都不送，所以只要「存在模擬器」就好。
- **關鍵**：模擬器**自己選 CRS**（和真的 CRS 不可區分）。這是作弊證明者**沒有**的能力。

---

## 3. 為什麼是 NIZK：模擬器可以設定 CRS

[▶ 10:43](https://youtu.be/GAF78dg8-nE?t=643)

**難處**：模擬器拿到 $x$，不知道 $x$ 在不在 $L$。如果它成功，對某些 $x\notin L$ 也會成功，所以它必須產生**撞到壞挑戰**的 $(\alpha, \beta, \gamma)$。怎麼做到？因為**它自己選加密**，有秘密鑰，可以「破解」。

【口頭】講者說：對第 12 集原本的雜湊，她**不知道**怎麼證明是 NIZK（也許是，但不會證）。稍微改一下雜湊（不影響 soundness）就能證。

### 3.1 誠實驗證者零知識

[▶ 13:36](https://youtu.be/GAF78dg8-nE?t=816)

**平行重複**的 Blum 協定是**誠實驗證者零知識**（honest-verifier ZK）：誠實驗證者的 $b_1, \ldots, b_{\lambda}$ 是完全隨機的。

**模擬**（「不照順序來」）：
1. 先選隨機的 $b_1, \ldots, b_{\lambda}$（$\beta$）。
2. 再造 $\alpha$：第 $j$ 份若 $b_j = 0$，承諾一個和 $G$ 無關的**隨機哈密頓圈**；若 $b_j = 1$，誠實地承諾 $\pi(G)$（裡面沒有哈密頓圈，但不會被要求打開圈）。
3. 照 $\beta$ 打開，得到 $\gamma$。

這樣故意讓 $\alpha$「撞到」$\beta$。

### 3.2 改一下雜湊：加上隨機的 z

[▶ 16:26](https://youtu.be/GAF78dg8-nE?t=986)

問題：$\alpha, \beta$ 已經選好，要選 $hk$ 使 $H_{hk}(G, \alpha) = \beta$，做得到嗎？講者不確定。所以**改雜湊**：

$$H'_{(hk, z)}(\alpha) := H_{hk}(\alpha)\oplus z,\qquad z\leftarrow\{0,1\}^{\lambda}\ \text{（金鑰的一部分）}.$$

**soundness 不受影響**（[▶ 20:34](https://youtu.be/GAF78dg8-nE?t=1234)）：要證 $H_{hk}(\alpha)\oplus z\neq\beta_{\mathrm{bad}}(\alpha)$，也就是 $H_{hk}(\alpha)\neq\beta_{\mathrm{bad}}(\alpha)\oplus z$。分析時把 $g^{*}$ 改成

$$g^{*}(\alpha) := \mathrm{Dec}\left( sk,\ \beta_{\mathrm{bad}}(\alpha)\oplus z \right)\oplus 0\cdots 01,$$

證明和之前一模一樣（若相等，兩邊解密就矛盾）。「加上 $z$ 對證明沒有任何影響。」

【Q&A】[▶ 19:54](https://youtu.be/GAF78dg8-nE?t=1194) 學生問最終金鑰：$hk' = (pk, \widehat{0^{T}}, z)$，$z$ 是隨機的 $\lambda$ 位元字串。

### 3.3 模擬器

[▶ 17:51](https://youtu.be/GAF78dg8-nE?t=1071)

$\mathrm{Sim}(x = G, \mathrm{aux})$：
1. 用 3.1 產生 $(\alpha, \beta, \gamma)$。
2. CRS：隨機選 $pk_{\mathrm{com}}$；誠實選 $hk = (pk, \widehat{0^{T}})$；然後令
$$z := \beta\oplus H_{hk}(G, \alpha).$$
   這樣 $H'_{(hk, z)}(G, \alpha) = \beta$。
3. 輸出 $\left( (pk_{\mathrm{com}}, hk, z),\ (\alpha, \beta, \gamma) \right)$。

$z$ 在真實世界是均勻隨機的；這裡 $\beta$ 是均勻隨機的，所以 $z$ 也是均勻隨機的。

- **只是計算零知識**：模擬的 $\alpha$ 裡放的不是真的 $\pi(C)$，而是垃圾。而且 soundness 也只是計算的（用了假的 $g$）。【口頭】玩一玩參數可以得到統計的版本（第 12 集提過：CRS 用真公鑰或隨機字串，在統計 soundness 和統計零知識之間取捨）。

### 3.4 為什麼不再矛盾

[▶ 23:28](https://youtu.be/GAF78dg8-nE?t=1408)

- 證明零知識的方式：誠實驗證者零知識，再**設定（program）CRS 的一部分**（$z$）。如果雜湊金鑰是別人事先選好、模擬器碰不到，她不知道怎麼模擬。
- **互動**的情形沒有 CRS，模擬器和作弊證明者能力一樣：拿「Fiat–Shamir 驗證者」當 $V^{*}$，模擬器就是作弊證明者。所以「沒有作弊證明者 ⟹ 沒有模擬器」。
- **非互動**的情形，模擬器能選 CRS，比作弊證明者強得多。所以可以**同時**有 Fiat–Shamir soundness 和非互動零知識。

【口頭】[▶ 26:10](https://youtu.be/GAF78dg8-nE?t=1570) 從 LWE 得到 NIZK 曾是很久的開放問題（這裡展示的是循環安全 LWE / FHE 的版本）。「我覺得很了不起，能在一堂課從頭到尾教完。我可以用以前那些更糟、更複雜的嘗試折磨你們，讓你們更欣賞這個。但對我這個在那些舊方法上流過很多淚和汗的人來說，我完全欣賞它的美。」

---

## 4. 這個技巧用到了什麼

[▶ 27:33](https://youtu.be/GAF78dg8-nE?t=1653)

協定的具體結構用得很少，只用到兩件事：

1. **壞的 $\beta$ 是唯一的**。可以放寬：若有 $d$ 個壞的 $\beta$，假設會**多損失 $1/d$**：分析時猜作弊者用哪一個，$1/d$ 機率猜中，之後照唯一的情形做。$d$ 很大就有問題。
2. **壞的 $\beta$ 能有效率地算出來**（用陷門）。這個真的用到了：雜湊要算 $\beta_{\mathrm{bad}}$。「壞的 $\beta$ 算不出來的情形，我完全不知道怎麼處理。」

【Q&A】[▶ 24:48](https://youtu.be/GAF78dg8-nE?t=1488) **壞的 $\beta$ 不唯一時，隨機的 $z$ 有幫助嗎？** 講者說這個問題有比較長的答案，就是上面第 1 點和第 5 節。

---

## 5. 相關性難解雜湊

### 5.1 定義

[▶ 29:48](https://youtu.be/GAF78dg8-nE?t=1788)

這個概念是為了證明 Fiat–Shamir 的 soundness 而提出的。大致上：一個雜湊是相關性難解的，就代表 Fiat–Shamir 用它是可行的。

> **相關性難解**（correlation intractable, CI）：雜湊族 $\mathcal{H} = (\mathrm{Gen}, \mathrm{Eval})$ 對關係 $R\subseteq\{0,1\}^{n(\lambda)}\times\{0,1\}^{m(\lambda)}$ 是相關性難解的，若對每個大小 $\mathrm{poly}(\lambda)$ 的攻擊者 $A$，存在可忽略的 $\mu$：
> $$\Pr_{hk\leftarrow\mathrm{Gen}(1^{\lambda})}\left[ x\leftarrow A(hk):\ (x, \mathrm{Eval}(hk, x))\in R \right]\le\mu(\lambda).$$

白話：拿到金鑰後，找不到一個 $x$ 讓它的雜湊值和它「相關」（落在 $R$ 裡）。

**不能對所有關係都成立**：如果 $R$ 包含所有 $(x, y)$，當然會撞到。所以最多只能希望對**稀疏**（sparse，或叫 evasive）的關係成立：

$$\forall x:\quad\Pr_{y\leftarrow\{0,1\}^{m}}\left[ (x, y)\in R \right]\le\mathrm{negl}.$$

> **大問題**：是否存在對**每個**稀疏關係都相關性難解的雜湊？

### 5.2 和 Fiat–Shamir 的關係

[▶ 33:59](https://youtu.be/GAF78dg8-nE?t=2039)

三則訊息的證明系統，固定 $x\notin L$，定義

$$R_x := \left\{ (\alpha, \beta) : \exists\gamma,\ (\alpha, \beta, \gamma)\ \text{被接受} \right\}.$$

- 因為是**證明**，對每個 $\alpha$ 只有可忽略比例的 $\beta$ 答得出來，所以 $R_x$ 是稀疏的。
- 若 $\mathcal{H}$ 對 $R_x$ 相關性難解，作弊者找不到 $\alpha$ 使 $H(\alpha)$ 是壞的 $\beta$，Fiat–Shamir 就 sound。
- 所以：**對每個稀疏關係都 CI 的雜湊存在 ⟹ Fiat–Shamir 對所有（三則訊息、常數回合的）證明都 sound**。

【Q&A】[▶ 37:28](https://youtu.be/GAF78dg8-nE?t=2248) Fiat–Shamir 那裡是 $x\notin L$？對。

**歷史**：這個概念大約 2004 年就提出了（講者說記不清楚）。已知隨機預言機是 CI 的，但之後一直卡住。

> 【課本補充】Thaler §5.2「Recent results constructing CI hash families」（書頁 82–83，PDF 頁 83–84）：近年一系列工作 [CCR16, KRR17, CCRR18, HL18, CCH+19, PS19, JKKZ21, HLR21, LV22, BKM20] 在標準假設下，替各種自然的 IP 和論證造出 CI 雜湊族；其中 [PS19, HLR21] 假設 **LWE**。這些構造都「有 FHE 的味道」，計算量很大，比 GKR 的證明者和驗證者貴得多，所以不實用；但實務上用的雜湊也許真的滿足相關的 CI 性質。這些結果適用於 GKR，也適用於 [Blu86, GMW91] 那類 NP 完全語言的零知識證明（不簡短）。Thaler 也指出：想用這個方法把**簡短**的 public-coin 論證變成非互動，目前的結果都是負面的 [GW11, BBH+19]。

### 5.3 CLW 定理

[▶ 39:35](https://youtu.be/GAF78dg8-nE?t=2375)

> **可在時間 $t$ 搜尋的關係**（searchable in time $t$）：對每個 $\alpha$，**最多一個** $\beta$ 使 $(\alpha, \beta)\in R$，而且從 $\alpha$ 算出那個 $\beta$（或知道沒有）只要時間 $t$。
>
> **定理（Canetti–Lombardi–Wichs）**：對每個多項式 $t$，存在**一個**雜湊族（求值時間隨 $t$ 成長），它對**所有**可在時間 $t$ 搜尋的關係都是相關性難解的。（假設循環安全 FHE。）

**量詞順序很重要**（[▶ 42:24](https://youtu.be/GAF78dg8-nE?t=2544)）：
- 「對每個時間 $t$ 可搜尋的關係，**存在**一個 CI 雜湊」是**顯然**的：$H(\alpha) := f(\alpha)\oplus 1$（$f$ 是找 $\beta$ 的函數）。
- CLW 證的是反過來：**存在一個雜湊族**，對**所有**時間 $t$ 可搜尋的關係都 CI。

【口頭】這個敘述很一般，很多後續工作都用它，例如幾乎可以用來證明 GKR 或 sum-check 的 Fiat–Shamir soundness。

### 5.4 證明（同一個雜湊）

[▶ 51:59](https://youtu.be/GAF78dg8-nE?t=3119)

【課堂討論】講者問 Gen 做什麼，學生答：產生 FHE 公鑰。

- **$\mathrm{Gen}(1^{\lambda})$**：$(pk, sk)\leftarrow\mathrm{FHE.Gen}$，輸出 $hk = (pk, \mathrm{Enc}(pk, 0^{t'}))$。$t'$ 比 $t$ 大一點（= $g^{*}$ 的大小：$t$ 加上解密加上翻一位）。
- **$\mathrm{Eval}(hk, \alpha)$**：$\mathrm{FHE.Eval}(pk, U_{\alpha}, \hat{g})$，在加密底下算 $g(\alpha)$。

給定任何時間 $t$ 可搜尋的關係 $R$，記 $f(\alpha)$ 為那個唯一的 $\beta$。

1. 假設 $A(hk)$ 以機率 $\varepsilon$ 輸出 $\alpha$ 使 $\mathrm{Eval}(hk, \alpha) = f(\alpha)$。
2. 由語意安全（＋循環安全），換成 $hk^{*} = (pk, \mathrm{Enc}(pk, g^{*}))$，$A$ 仍以約 $\varepsilon$ 成功，其中
$$g^{*}(\alpha) := \mathrm{Dec}\left( sk, f(\alpha) \right)\oplus 1.$$
3. 但用 $hk^{*}$ 時，$\mathrm{Eval}(hk^{*}, \alpha) = \widehat{g^{*}(\alpha)}$ **永遠不等於** $f(\alpha)$：若相等，兩邊解密得 $g^{*}(\alpha) = \mathrm{Dec}(sk, f(\alpha))$，和定義矛盾。
4. 「換到 $g^{*}$ 之後，我們就不在乎假設了，進入統計的世界：連無限強的攻擊者都撞不到。」$\blacksquare$

**有 $d$ 個壞的 $\beta$**（$f_1, \ldots, f_d$）：對每個 $f_i$ 分別用一個 $g_i^{*}$ 證明「撞到 $f_i$ 的機率可忽略」，再 union bound：總機率 $\le d\cdot\mathrm{negl}$。$d$ 是多項式就好。

### 5.5 Q&A

【Q&A】[▶ 57:37](https://youtu.be/GAF78dg8-nE?t=3457) **$f$ 是誰選的？** 雜湊族是固定的；對**每個**時間 $t$ 可搜尋的關係都成立。「選你最喜歡的關係。」$f$ 就是那個關係的搜尋函數。

【Q&A】[▶ 60:24](https://youtu.be/GAF78dg8-nE?t=3624) **攻擊者看到雜湊金鑰後再選關係也行嗎？** 講者先說行（他還是分不出 $\widehat{0}$ 和 $\widehat{g^{*}}$），學生追問：那他不就選「$f$ = 對這把金鑰做 FHE 求值」？講者更正：**看到雜湊族之後**可以選關係，但**不能看到具體的金鑰之後**再選（否則 $f$ 就可以是雜湊本身）。學生補充：密文是隨機化的，拿到 $\hat{g}$ 之前很難預測求值結果。

【Q&A】[▶ 62:26](https://youtu.be/GAF78dg8-nE?t=3746) 學生：這和 sum-check 裡「後面的壞關係依賴驗證者訊息」是同一個問題？講者：「完全正確。」

【Q&A】[▶ 63:11](https://youtu.be/GAF78dg8-nE?t=3791) **$f$ 不唯一時怎麼改 $g^{*}$？** 分析時對每個 $f_i$ 換一個不同的 $g^{*}$。學生問 CLW 的「可搜尋」定義怎麼推廣：把關係想成每個 $\alpha$ 對應 $f_1(\alpha), \ldots, f_d(\alpha)$。

---

## 6. 應用：sum-check（想法）

[▶ 45:41](https://youtu.be/GAF78dg8-nE?t=2741)

「不是直接的，需要更多密碼學，但讓你們感受一下為什麼這很有用。」

宣稱 $\sum_{b} g(b_1, \ldots, b_m) = v$（假的）。

- 第一輪證明者送 $g_1^{*}$（假的；真的應該是 $g_1(X) = \sum_{b_2, \ldots} g(X, b_2, \ldots)$，但它加起來不是 $v$）。
- **壞的 $\beta$**：所有 $t\in\mathbb{F}$ 使 $g_1^{*}(t) = g_1(t)$。最多 $d$ 個（$d$ 是次數）。撞到就「轉正」了，之後是真命題。
- **能有效率地算**：$g_1$ 本身可能難算，但可以**寫死當陷門**；有了 $g_1$，給定 $g_1^{*}$，找出 $g_1^{*} - g_1$ 的所有根有有效率的演算法。
- 所以第一輪：$d$ 個壞挑戰、可有效率搜尋，CLW 直接適用（損失 $d$ 倍）。

**為什麼不完全直接**（[▶ 49:10](https://youtu.be/GAF78dg8-nE?t=2950)）：第二輪的真多項式 $g_2(X) = \sum g(t_1, X, b_3, \ldots)$ **依賴 $t_1$**，而 $t_1$ 是 Fiat–Shamir 算出來的，事先不知道，沒辦法把 $g_2$ 寫死。所以要再加一些密碼學、多做一些工作。

**用到這個技巧的地方**：證明 GKR 的 Fiat–Shamir soundness；以及下次 **Zhengzhong Jin** 要講的、用 Fiat–Shamir 證明**批次非互動論證**（BARG）存在的結果。

【Q&A】[▶ 50:37](https://youtu.be/GAF78dg8-nE?t=3037) **所以是拿到所有壞的再隨機選一個？** 分析時：作弊者以 $1/d$ 機率是用某個特定的壞挑戰作弊；對每個固定的壞挑戰，他作弊的機率可忽略；union bound 得 $d\cdot\mathrm{negl}$。

---

## 7. 一頁速查表

### NIZK

- 定義：$\exists\mathrm{Sim}$，$\forall x\in L, \mathrm{aux}$：$(\mathrm{CRS}, P(\mathrm{CRS}, x, w), \mathrm{aux})\approx_c(\mathrm{Sim}(x, \mathrm{aux}), \mathrm{aux})$。
- 模擬器可以選 CRS → 不和 Fiat–Shamir soundness 矛盾。
- 構造：平行 Blum + 承諾 = 加密（$pk$ 在 CRS）+ FS 雜湊 $H'(\alpha) = H_{hk}(\alpha)\oplus z$。
- 模擬：先選 $\beta$，造撞到它的 $\alpha$（誠實驗證者零知識），再設 $z := \beta\oplus H_{hk}(G, \alpha)$。
- 加 $z$ 不影響 soundness：分析時 $g^{*}(\alpha) = \mathrm{Dec}(sk, \beta_{\mathrm{bad}}(\alpha)\oplus z)\oplus 1$。

### 相關性難解

- $\Pr[A(hk)\to x:\ (x, H_{hk}(x))\in R]\le\mathrm{negl}$。只能對稀疏 $R$ 要求。
- Fiat–Shamir：$R_x = \{(\alpha, \beta):\exists\gamma$ 接受$\}$，$x\notin L$ 時稀疏 ⟹ CI 就 FS-sound。
- **CLW**：一個雜湊族對所有「時間 $t$ 可搜尋」的關係都 CI。關鍵一步：分析時加密 $g^{*}(\alpha) = \mathrm{Dec}(sk, f(\alpha))\oplus 1$，解密後必不同。
- $d$ 個壞挑戰：每個分別證，union bound，損失 $d$。
- 攻擊者可在看到雜湊族後選關係，但不能在看到金鑰後選。

### 技巧用到的

1. 壞挑戰少（唯一或多項式個）。
2. 壞挑戰能有效率算出（用陷門）。

### Sum-check

第一輪壞挑戰 = $g_1^{*} - g_1$ 的根（$\le d$ 個，陷門 $g_1$）。後面幾輪的真多項式依賴之前的 FS 輸出，需要額外工作。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 相關性難解雜湊 + LWE | 第 14–15 集：Jin 用它造 BARG |
| sum-check / GKR 的 Fiat–Shamir | 第 16–17 集：SNARG |
| NIZK | （本課到此為止） |

---

## 附：本集一句話總結

> **Fiat–Shamir 後的平行 Blum 協定是 NIZK，因為模擬器能自己設定 CRS（在雜湊上加一個它挑的 $z$），這是作弊證明者沒有的能力；而 CLW 的技巧可以抽象成：一個 FHE 雜湊對所有「壞挑戰可以有效率搜尋」的關係都是相關性難解的——這正是讓 Fiat–Shamir 在標準模型下成立的工具。**

---

## ⚠️ 待確認清單

1. 指定論文 Canetti–Lombardi–Wichs（ePrint 2018/1248）未取得。NIZK 模擬器裡「改雜湊加上 $z$」是講者為了教學做的改動（她說原本的雜湊她不會證），論文的實際做法待對照。相關性難解這個概念提出的年份和作者，講者說大約 2004 年、記不清楚。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 7 Part 2 錄影逐字稿（MIT 真人字幕，1:04:59）整理；本集無次要來源。*
