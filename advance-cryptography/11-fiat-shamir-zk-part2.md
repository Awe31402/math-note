---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 11
lecture: Lecture 6 (Part 2) – Fiat-Shamir Paradigm and Zero-Knowledge Proofs
date: 待補（2023 秋季第六堂課，後段）
video: https://youtu.be/zEf_dECRUjY
notes: Thaler §5.2（書頁 75–78，PDF 頁 76–79）。OCW 本講無指定讀物。
---

# 第 11 集 · Lecture 6 (Part 2)：Fiat–Shamir 在隨機預言機模型下何時 sound、平行零知識的反面 [▶ 影片](https://youtu.be/zEf_dECRUjY)

← 上一集：[10-fiat-shamir-zk-part1](10-fiat-shamir-zk-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[12-fiat-shamir-standard-model-part1](12-fiat-shamir-standard-model-part1.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 11 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:08:59，MIT 上傳的真人字幕）＋ Thaler §5.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 隨機預言機模型下的攻擊](#1-隨機預言機模型下的攻擊)
  - [1.1 soundness 不可忽略時](#11-soundness-不可忽略時)
  - [1.2 soundness 可忽略但回合很多時](#12-soundness-可忽略但回合很多時)
- [2. 定理：常數回合＋可忽略 soundness ⟹ ROM 下 sound](#2-定理常數回合可忽略-soundness--rom-下-sound)
  - [2.1 證明（三則訊息）](#21-證明三則訊息)
  - [2.2 Q&A](#22-qa)
  - [2.3 更多回合](#23-更多回合)
  - [2.4 Round-by-round soundness（只提一下）](#24-round-by-round-soundness只提一下)
- [3. Kilian–Micali＋Fiat–Shamir：ROM 下 sound，標準模型不保證](#3-kilianmicalifiatshamirrom-下-sound標準模型不保證)
- [4. 閒聊：密碼真的被破解嗎？NSA 知道更多嗎？](#4-閒聊密碼真的被破解嗎nsa-知道更多嗎)
- [5. 平行重複 Blum 協定：零知識 vs. Fiat–Shamir](#5-平行重複-blum-協定零知識-vs-fiatshamir)
  - [5.1 循序重複保持零知識](#51-循序重複保持零知識)
  - [5.2 平行重複為什麼難模擬](#52-平行重複為什麼難模擬)
  - [5.3 Fiat–Shamir sound ⟹ 不是零知識](#53-fiatshamir-sound--不是零知識)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:13](https://youtu.be/zEf_dECRUjY?t=13)

1. 用第 10 集的 Blum 協定，說明 Fiat–Shamir 在隨機預言機模型下也會失敗。
2. 證明：**常數回合、soundness 可忽略**的 public-coin 協定，Fiat–Shamir 在隨機預言機模型下是 sound 的。
3. 平行重複 Blum 協定：「Fiat–Shamir sound」和「零知識」不能同時成立。

【口頭】講者說零知識講得很粗略，本來沒打算教，「但它太美了，很難不講」。

---

## 1. 隨機預言機模型下的攻擊

### 1.1 soundness 不可忽略時

[▶ 00:56](https://youtu.be/zEf_dECRUjY?t=56)

直覺是「跟驗證者說話或跟隨機函數說話，都是拿到隨機 $\beta$，沒差」。「幾乎對，但不對。」

**攻擊 Blum 協定**（$G$ 沒有哈密頓圈）：

1. **猜** $b$。猜 0：承諾一個隨機的圈；猜 1：承諾全 0 矩陣。
2. 把 $(G, \alpha)$ 丟給隨機預言機，拿到 $b$。
3. 猜中了：照猜的方式打開（猜 0 就打開那個圈；猜 1 就給 $\pi$、打開非邊，全是 0）。猜錯了：**重來**。

在真的互動裡，你只有一次機會（1/2 機率成功），「你失敗了，不能再試」。但在隨機預言機模型下，預言機在你手上，**可以一直試**，平均試兩次就成功。

> **結論**：原協定的 soundness 不可忽略，Fiat–Shamir 在隨機預言機模型下就不 sound。（回答第 10 集 Leo 的問題。）

### 1.2 soundness 可忽略但回合很多時

[▶ 04:23](https://youtu.be/zEf_dECRUjY?t=263)

「soundness 可忽略就 sound 嗎？」也不是。

把 Blum 協定**循序重複 $\lambda$ 次**，soundness 變成 $2^{-\lambda}$。攻擊：

- 一輪一輪來。第 1 輪：猜 $\beta_1$、做 $\alpha_1$、雜湊，猜中就算出 $\gamma_1$，**保留**這輪的紀錄。猜錯就只重做這一輪。
- 第 2 輪：在已經成功的紀錄後面接著做，猜 $\beta_2$、做 $\alpha_2$、雜湊**整個紀錄**（$\alpha_1, \beta_1, \gamma_1, \alpha_2$），猜中就繼續，猜錯就只重做第 2 輪。
- 每輪平均 2 次，總共 $O(\lambda)$ 次雜湊，有效率。

【Q&A】[▶ 06:32](https://youtu.be/zEf_dECRUjY?t=392) **雜湊整個之前的紀錄，不就沒辦法了？** 學生自己回答：不，只要換新的承諾，一直試到滿意。講者：已經成功的部分不用重算，每次都是**延伸**它。

【Q&A】[▶ 07:53](https://youtu.be/zEf_dECRUjY?t=473) **這對有界的證明者不是很難嗎？** 不，每輪平均兩次，很快。

> 【課本補充】Thaler §5.2 註腳 70 用同樣的例子：任何 soundness 1/3 的 IP 循序重複 $n$ 次，soundness 是 $3^{-\Omega(n)}$，但套 Fiat–Shamir 在隨機預言機模型下不 sound [Rot19]。這種攻擊叫 **state-restoration attack**（或 grinding attack）：倒回對話的某一點，換一個回答試試看。

---

## 2. 定理：常數回合＋可忽略 soundness ⟹ ROM 下 sound

[▶ 10:00](https://youtu.be/zEf_dECRUjY?t=600)

> **定理**：若 public-coin 協定有**常數回合**且 **soundness 可忽略**，則 Fiat–Shamir 在隨機預言機模型下是 sound 的。

- 【Q&A】學生提醒要 public coin。講者：對，不是 public coin 連 completeness 都不成立（驗證者訊息沒辦法用雜湊產生）。
- 這**不是**充要條件：有些很多回合的協定也行，例如 **GKR**（見 2.4）。

### 2.1 證明（三則訊息）

[▶ 13:45](https://youtu.be/zEf_dECRUjY?t=825)

原協定 $(P, V)$：$P\xrightarrow{\alpha}V$，$V\xrightarrow{\beta}P$（隨機，$k$ 位元），$P\xrightarrow{\gamma}V$。

**$\beta$ 一定來自超多項式大小的空間**（[▶ 15:57](https://youtu.be/zEf_dECRUjY?t=957)）：對任何 $\alpha$，總有某些 $\beta$ 能讓證明者作弊（否則根本不需要互動，固定一個 $\beta$ 就好）。如果 $\beta$ 只有多項式種，「猜」的攻擊就成功。所以 soundness 可忽略 ⟹ $k$ 是超對數的，$2^{-k}$ 可忽略。

【口頭】講者說希伯來文有一個很好的詞形容「作弊時希望不被抓」，「但美國人太老實不作弊，所以沒有這個詞」。學生建議「con」、「fake it till you make it」，講者：「完全就是。」

**假設**：存在大小 $\mathrm{poly}$ 的 $P^{*}$ 和 $x\notin L$，

$$\Pr\left[ (P^{*})^{H}\ \text{讓}\ V^{H}_{\mathrm{FS}}\ \text{接受}\ x \right]\ge\varepsilon.$$

$P^{*}$ 輸出 $(\alpha, \beta, \gamma)$，驗證者檢查 $\beta = H(x, \alpha)$ 且原驗證者接受。

**$P^{*}$ 最多問 $q$ 次**：記他對 $H$ 的查詢為 $(x, \alpha_1), \ldots, (x, \alpha_q)$，$q\le$ $P^{*}$ 的大小。

**Step 1：輸出的 $\alpha$ 幾乎一定是查過的**（[▶ 19:42](https://youtu.be/zEf_dECRUjY?t=1182)）：如果 $(x, \alpha)$ 沒問過，$P^{*}$ 不知道 $H(x, \alpha)$，猜中 $\beta$ 的機率 $2^{-k}$：

$$\Pr\left[ \text{接受}\ \wedge\ \alpha\notin\{\alpha_1, \ldots, \alpha_q\} \right]\le 2^{-k}.$$

- 【Q&A】[▶ 21:03](https://youtu.be/zEf_dECRUjY?t=1263) 學生：要查的是 $(x, \alpha)$ 不只是 $\alpha$。講者：對。

**Step 2：造互動協定的作弊者 $P^{**}$**（[▶ 22:26](https://youtu.be/zEf_dECRUjY?t=1346)）。「我自己不會作弊，我用他。」

1. 用同一個 $x$。
2. **猜**一個隨機的 $i\in\{1, \ldots, q\}$。
3. 執行 $P^{*}$，**自己扮演預言機**：
   - 第 $j\neq i$ 次查詢：回一個隨機值（記住，同樣的查詢回一樣的值）。
   - 第 $i$ 次查詢 $(x, \alpha_i)$：把 $\alpha_i$ 送給**真的驗證者**，拿到隨機 $\beta$，把 $\beta$ 當成預言機的回答給 $P^{*}$。
4. $P^{*}$ 輸出 $(\alpha, \beta, \gamma)$。如果 $\alpha = \alpha_i$，把 $\gamma$ 送給驗證者；否則失敗。

**分析**：$P^{**}$ 給 $P^{*}$ 的預言機回答全都是均勻隨機的（真驗證者的 $\beta$ 也是），所以 $P^{*}$ 的行為和在真的隨機預言機下一樣。$P^{*}$ 成功、而且用的是某個查過的 $\alpha_{j}$，而 $i$ 是隨機猜的、和 $P^{*}$ 的行為獨立，猜中的機率 $1/q$：

$$\Pr\left[ P^{**}\ \text{被接受} \right]\ \ge\ \frac{\varepsilon - 2^{-k}}{q}.$$

- 【課堂討論】[▶ 29:04](https://youtu.be/zEf_dECRUjY?t=1744) 講者問成功機率，學生答「除以 $q$」。
- $q$ 是多項式，$\varepsilon$ 不可忽略 ⟹ 這仍不可忽略，違反原協定的 soundness。$\blacksquare$

### 2.2 Q&A

【Q&A】[▶ 29:46](https://youtu.be/zEf_dECRUjY?t=1786) **證明哪裡真的用到隨機預言機模型？** Step 1 那行（沒查過就不知道 $H$ 的值），還有「能觀察到他問了哪些 $\alpha$」這件事本身，以及能替他模擬預言機。

【口頭】[▶ 30:27](https://youtu.be/zEf_dECRUjY?t=1827) 隨機預言機模型的動機是「我們要雜湊看起來隨機」，所以很誘人地說「只要一個表現得像隨機的雜湊就好」，例如偽隨機函數。但怎麼證明 soundness？上面的證明只在「作弊者只會把輸入丟進函數、看輸出」時才有意義。「只要他能做『盲目地餵輸入、拿輸出』以外的事，我就沒有證明。」

【Q&A】[▶ 32:33](https://youtu.be/zEf_dECRUjY?t=1953) **怎麼知道 $q$？** 不知道，而且 $q$ 可以是**適應性**的（看了 $\beta_1$ 滿意就不問了，不滿意再問）。但 $P^{*}$ 是固定的多項式大小電路，例如 $\lambda^3$，每次查詢至少佔一個單位，所以 $q\le\lambda^3$。最壞情形成功機率是 $\varepsilon/$（$P^{*}$ 的大小）。
- 【Q&A】電路會不會不停機？不會：$P^{*}$ 是多項式大小的電路，裡面有 $H$ 閘（輸入 $(x, \alpha)$、輸出一個值，算一個單位），沒有迴圈，最多 $\lambda^3$ 個閘。

### 2.3 更多回合

[▶ 36:03](https://youtu.be/zEf_dECRUjY?t=2163)

【課堂討論】$c$ 個驗證者訊息時，機率怎麼衰減？學生答：大約 $\varepsilon/q^{c}$。

做法一樣：假設每一層「部分對話紀錄」最多 $q$ 次查詢（$(x, \alpha)$ 形式的、$(x, \alpha, \beta, \gamma)$ 形式的……）。$P^{**}$ 對**每個**驗證者訊息各猜一個索引 $i_1, \ldots, i_c$：數到第 $i_1$ 個「第一層形式」的查詢時用真驗證者的 $\beta$，數到第 $i_2$ 個「第二層形式」的查詢時用真驗證者的 $\delta$……其他全回隨機。每個猜中機率 $1/q$，所以

$$\Pr\left[ P^{**}\ \text{被接受} \right]\gtrsim\frac{\varepsilon}{q^{c}}.$$

【Q&A】[▶ 40:18](https://youtu.be/zEf_dECRUjY?t=2418) **回合數不是安全參數就還安全？** $c$ 是常數就好。$c = \log$ 的話，$q^{\log}$ 是擬多項式（quasi-poly），損失 $1/\mathrm{quasipoly}$。如果原協定保證作弊機率小於 $1/\mathrm{quasipoly}$（例如次指數小），那 $\log$ 回合也行。「$q^{c}$ 就是你能承受的作弊機率。」

【Q&A】[▶ 41:48](https://youtu.be/zEf_dECRUjY?t=2508) **$q$ 是總查詢數，能不能改成 $(q/c)^{c}$？** 沒那麼簡單：查詢怎麼分配在各層是**適應性**的，可能全部都在第一層。講者用均勻隨機選索引；也許能用更好的分布（偏向前面）改進一點，她沒算過，「我們通常不在乎常數」。一般而言不能直接這樣改。

> 【課本補充】Thaler §5.2 [PS00]：若原協定有 $t$ 回合，任何在時間 $T$、以機率 $\varepsilon$ 讓 Fiat–Shamir 驗證者接受的證明者，可以轉成原協定裡至少以 $(\varepsilon/T)^{O(t)}$ 機率成功的證明者。$t$ 是常數時是 $\mathrm{poly}(\varepsilon, 1/T)$，不可忽略。Thaler 在第 5 章末尾對三則訊息協定證明這個結果（Theorem 5.1）。註腳 69：如果原協定是論證（不是證明），ROM 下的 soundness 也繼承原本的計算假設。

### 2.4 Round-by-round soundness（只提一下）

[▶ 12:09](https://youtu.be/zEf_dECRUjY?t=729)

很多回合的協定也可能在 ROM 下 sound，例如 **GKR**：它有一個性質叫 **round-by-round soundness**，任何有這個性質的協定在 ROM 下都 sound。講者說「今天不講，也許之後會回來找我們」。

> 【課本補充】Thaler §5.2 [CCH+19, BCS16]：**round-by-round soundness** 的意思是：(1) 協定執行的每個階段都有一個由部分對話紀錄決定的「狀態」，有些狀態是「**注定失敗**」（doomed）的：一旦進入，不管證明者怎麼做，除了可忽略機率外永遠注定失敗；(2) $x\notin L$ 時初始狀態是注定失敗的；(3) 結束時若是注定失敗的狀態，驗證者拒絕。Canetti 等人證明 GKR（以及任何基於 sum-check 的 IP）都有這個性質，所以 Fiat–Shamir 後在 ROM 下 sound。直覺：作弊者唯一的辦法是讓驗證者的硬幣「剛好」落在把協定推出注定失敗狀態的一小群壞硬幣裡；state-restoration 攻擊（倒回去換回答）也沒用，因為一旦注定失敗就逃不掉。循序重複的 Blum 協定**沒有**這個性質（1.2 的攻擊就是逃出去的方法）。

---

## 3. Kilian–Micali＋Fiat–Shamir：ROM 下 sound，標準模型不保證

[▶ 43:54](https://youtu.be/zEf_dECRUjY?t=2634)

學生提醒：這就證明了 Kilian–Micali 的情形。Kilian–Micali 有 **4 則訊息（常數）**，PCP 取 soundness 可忽略的就有可忽略的錯誤。所以 **Fiat–Shamir 在 ROM 下對 Kilian–Micali 是 sound 的**。

**標準模型呢**（[▶ 44:39](https://youtu.be/zEf_dECRUjY?t=2679)）：

- 很長一段時間大家相信：**ROM 下有證明 ⟹ 一定存在某個雜湊讓它 sound**。所以如果實務上用 SHA-256 套 Fiat–Shamir 被破解，就怪雜湊：「SHA-256 不是好雜湊，換一個。」
- 但 Kilian–Micali 是很自然、不是為了當反例而發明的協定，它在 ROM 下安全，卻存在（刻意的）CRH 和 PCP 使得它**對任何具體的雜湊族**套 Fiat–Shamir 都不安全。
- **教訓**：ROM 是不錯的**合理性檢查**（sanity check），但不是證明，甚至不保證存在證明。
- 【口頭】實務上大家就是這樣檢查：在 ROM 下安全就用。據她所知，從沒有東西因為 ROM 不安全而被破解。「這比較是理論上有趣的事。」

---

## 4. 閒聊：密碼真的被破解嗎？NSA 知道更多嗎？

【Q&A】[▶ 47:25](https://youtu.be/zEf_dECRUjY?t=2845) **有人試著破解 ROM 下安全的東西嗎？**
東西一直被駭、被破解，但**很少是密碼學本身被破**。常見的是**隨機性**：密碼學假設秘密鑰是隨機的，但實作裡隨機數從哪來？常常做得不好，結果不夠隨機，就被攻擊了。為什麼不是密碼學本身？可能因為它真的安全、問題在實作。有很多人很努力在攻擊密碼學，但都在關起來的門後面做。

【口頭】講者說社群裡有一位很棒的人（字幕寫「Joe Killion」）當過教授、後來去了 NSA。她問他「你們會分解大數嗎？」他說：「我工作最糟的部分，就是連拿這種事開玩笑都不准。」學生：「所以你不知道他們不知道。」講者：「對。」
- ⚠️ 待確認：字幕「Joe Killion」的確切身分。

【Q&A】[▶ 50:14](https://youtu.be/zEf_dECRUjY?t=3014) **NSA 比公開的密碼學進步嗎？** 講者猜是：我們不藏任何東西，他們知道我們知道的一切，而且他們也有聰明人。會不會分解大數？不知道。學生提到 RSA：公開發明之前其實已經私下被知道了。「歷史上有例子，所以今天大概也是。」

【Q&A】[▶ 51:39](https://youtu.be/zEf_dECRUjY?t=3099) **有人發表「我們試著破解 SHA-256 的 ROM 協定但失敗了」嗎？** 沒有，大家不發表失敗。所以「沒有已知的破解」只代表我們不知道破解，不代表沒有；也很難知道社群花了多少力氣。

【Q&A】[▶ 52:20](https://youtu.be/zEf_dECRUjY?t=3140) **破解了是不是不能馬上發表？** 講者不做破解，但她認識做安全研究的同事，「他們聊天時總是提到『監獄』這個詞」。「在理論的世界裡很容易不坐牢，他們不會追我們。」

---

## 5. 平行重複 Blum 協定：零知識 vs. Fiat–Shamir

### 5.1 循序重複保持零知識

[▶ 53:43](https://youtu.be/zEf_dECRUjY?t=3223)

【Q&A】零知識協定能平行重複嗎？

**循序重複**仍是零知識。模擬器的做法**正好就是 1.1 的 ROM 攻擊**：猜 $\beta_1$、做承諾、算 $V^{*}$ 對這個承諾的回答，猜中就打開，沒猜中就重來。學生：「幫你模擬的東西，也幫你破解了隨機預言機模型。」講者：「完全正確。」

### 5.2 平行重複為什麼難模擬

[▶ 55:05](https://youtu.be/zEf_dECRUjY?t=3305)

平行：一次送 $\alpha_1, \ldots, \alpha_{\lambda}$，收到 $\beta_1, \ldots, \beta_{\lambda}$，回 $\gamma_1, \ldots, \gamma_{\lambda}$。

- 誠實驗證者：每份各自模擬就好。
- **惡意驗證者**：例如 $(\beta_1, \ldots, \beta_{\lambda}) = f(\alpha_1, \ldots, \alpha_{\lambda})$，$f$ 像隨機函數。模擬器猜 $\beta_1$、調 $\alpha_1$；但改 $\alpha_2$ 時 $\beta_1$ 也可能跟著變，因為所有 $\beta$ 都是全部 $\alpha$ 的函數。不知道怎麼模擬。

「這是不是零知識？」是**開放了二十多年**的問題。大家真的很努力，有發表部分結果，「我們分享彼此的挫折」。

**2019 年**，在 MIT（「我們這一帶」）有一群人證明：**它不是零知識**。而且他們的證法是**證明 Fiat–Shamir 對它是 sound 的**：在一個標準的密碼學假設下（**LWE**，learning with errors，講者說「幾乎是 LWE，加上循環安全性」，「別管」），存在一個雜湊族使得平行重複的 Blum 協定（配合特定的承諾）套 Fiat–Shamir 後仍是 sound。下次證明。

- ⚠️ 逐字稿缺字：[▶ 58:37](https://youtu.be/zEf_dECRUjY?t=3517) 字幕寫「showing it's sound in the random oracle model」，依上下文（她說的是標準模型下的突破）應為「**standard** model」。
- 以下**不是逐字稿內容**，是依 OCW 課程網站推論的：第 7 講（第 12–13 集）的指定讀物是 Canetti、Lombardi、Wichs「Fiat-Shamir: From Practice to Theory, Part II」（STOC 2019），應該就是講者說的這個結果之一。

【Q&A】[▶ 60:17](https://youtu.be/zEf_dECRUjY?t=3617) **是說所有零知識協定平行重複都不是零知識嗎？** 不是。只說**這個特定的**哈密頓圈協定平行重複後不是零知識。

### 5.3 Fiat–Shamir sound ⟹ 不是零知識

[▶ 63:09](https://youtu.be/zEf_dECRUjY?t=3789)

> **Claim**：如果某個三則訊息協定在某個雜湊族下 Fiat–Shamir sound，那它（平行版本）不是零知識。

【Q&A】[▶ 61:01](https://youtu.be/zEf_dECRUjY?t=3661) 學生：是因為沒辦法照那個順序產生？講者：「就是這樣。」

**證明**：假設它是零知識：存在有效率的模擬器 $S$，對每個多項式大小的 $V^{*}$ 和每個 $x\in L$，$S$ 輸出和真實互動不可區分的紀錄。

1. **選一個特別的 $V^{*}$**：「Fiat–Shamir 驗證者」。固定 Fiat–Shamir sound 的那個雜湊族裡的一把金鑰 $hk$，$V^{*}$ 用 $\beta = H_{hk}(x, \alpha)$ 選挑戰。「我是 $V^{*}$，我的目標就是學到東西。我不想讓你模擬得出來。」
2. 對 $x\in L$：誠實證明者一定被接受，所以 $S(x)$ 也要輸出一個**被接受的** $(\alpha, \beta, \gamma)$，而且 $\beta = H_{hk}(x, \alpha)$（否則可以區分）。
3. 對 $x\notin L$：$S$ 是有效率的，**分不出** $x$ 在不在語言裡（不然它就解決了 NP 困難的問題）。所以一定有某些 $x\notin L$，$S(x)$ 也輸出被接受的紀錄。
4. 但那就是一個對 $x\notin L$ 的、被 Fiat–Shamir 驗證者接受的證明，**破解了 Fiat–Shamir 的 soundness**。矛盾。$\blacksquare$

【口頭】[▶ 67:27](https://youtu.be/zEf_dECRUjY?t=4047) 「這是個奇怪的世界狀態。」大家相信平行零知識應該成立（「你能學到什麼？試試看啊」），也相信 Fiat–Shamir 成立。但**兩者不能同時相信**，而且不清楚哪個才對。現在至少對這個協定知道了：Fiat–Shamir 成立，它不是零知識。

【Q&A】[▶ 68:08](https://youtu.be/zEf_dECRUjY?t=4088) 學生：所以更一般地，任何 Fiat–Shamir 成立的互動式證明都不能是零知識？講者：「沒錯。」（因為用那個具體的雜湊當惡意驗證者的策略，就是一個沒辦法模擬的互動。）

---

## 6. 一頁速查表

### ROM 下的攻擊

- soundness 不可忽略：一直重猜到中。
- 循序重複（很多回合）：一輪一輪延伸，每輪平均 2 次（state-restoration）。

### 定理

public-coin、常數回合 $c$、soundness 可忽略 ⟹ Fiat–Shamir 在 ROM 下 sound。

**關鍵一步**（三則訊息）：
1. 輸出的 $\alpha$ 沒查過 → 猜中 $\beta$ 機率 $2^{-k}$（$k$ 超對數）。
2. 猜 $P^{*}$ 的第 $i$ 次查詢，那次用真驗證者的 $\beta$，其他自己模擬隨機。
3. $\Pr[P^{**}] \ge (\varepsilon - 2^{-k})/q$；$c$ 輪則 $\gtrsim\varepsilon/q^{c}$。

$q\le$ $P^{*}$ 的大小（適應性也沒關係）。

### Round-by-round soundness

注定失敗的狀態逃不出去 ⟹ ROM 下 sound，回合數不限。GKR、sum-check 有；循序重複沒有。

### Kilian–Micali

4 則訊息、可忽略 soundness ⟹ ROM 下 FS-sound。但存在 CRH、PCP 使得對任何具體雜湊都不 sound ⟹ ROM 只是合理性檢查。

### 平行 Blum 協定

- 循序重複：零知識（模擬器 = ROM 攻擊）。
- 平行重複：開放 20 多年；2019 年證明在 LWE 類假設下 FS-sound ⟹ **不是零知識**。
- 一般：FS-sound（某個雜湊）⟹ 不是零知識。關鍵一步：拿那個雜湊當惡意 $V^{*}$；模擬器分不出 $x$ 在不在 $L$，對某個 $x\notin L$ 會輸出被接受的紀錄，破解 FS。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Fiat–Shamir 在標準模型下對平行 Blum 協定 sound | 第 12–13 集：相關性難解雜湊（correlation intractability）、LWE |
| 「FS-sound ⟹ 不是零知識」 | 第 12–13 集：同時得到 NIZK 的方法 |
| Round-by-round soundness | 第 12–13 集：Fiat–Shamir 用在 GKR 這類多回合協定 |
| LWE | 第 12–15 集 |

---

## 附：本集一句話總結

> **在隨機預言機模型下，作弊者可以一直重問預言機，所以 soundness 不可忽略、或靠循序重複換來的可忽略都不夠；但常數回合＋可忽略 soundness 就行（猜中作弊者用的那次查詢，只損失 $q^{c}$ 倍）。而平行重複的 Blum 協定揭示了一個張力：只要 Fiat–Shamir 對它 sound，它就不可能是零知識。**

---

## ⚠️ 待確認清單

1. [▶ 49:34](https://youtu.be/zEf_dECRUjY?t=2974) 講者提到去了 NSA 的那位研究者，字幕寫「Joe Killion」，確切身分不確定。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 6 Part 2 錄影逐字稿（MIT 真人字幕，1:08:59）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§5.2 整理。*
