---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 12
lecture: Lecture 7 (Part 1) – Soundness of the Fiat-Shamir Paradigm in the Standard Model
date: 待補（2023 秋季第七堂課，感恩節前一週）
video: https://youtu.be/R2izY69q0m8
notes: OCW 指定讀物 Canetti–Lombardi–Wichs「Fiat-Shamir: From Practice to Theory, Part II」（STOC 2019，ePrint 2018/1248）——本筆記製作時未能下載，只依逐字稿。
---

# 第 12 集 · Lecture 7 (Part 1)：標準模型下的 Fiat–Shamir——用 FHE 加密「避開壞挑戰」的函數 [▶ 影片](https://youtu.be/R2izY69q0m8)

← 上一集：[11-fiat-shamir-zk-part2](11-fiat-shamir-zk-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[13-fiat-shamir-standard-model-part2](13-fiat-shamir-standard-model-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 12 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:33:40，MIT 上傳的真人字幕）。OCW 指定論文（CLW 2019）未取得，**本集沒有次要來源**。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：Thaler 書沒有涵蓋這部分（相關性難解雜湊、FHE），指定論文又沒能下載，所以下面所有內容都只依逐字稿。黑板看不到，符號照口述重建。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：平行重複的 Blum 協定](#1-回顧平行重複的-blum-協定)
- [2. 為什麼重要：NIZK、SNARG、BARG](#2-為什麼重要nizksnargbarg)
- [3. 跟「Fiat–Shamir 和零知識互相矛盾」有沒有衝突](#3-跟fiatshamir-和零知識互相矛盾有沒有衝突)
- [4. 核心觀察：每個 α 只有一個壞的 β](#4-核心觀察每個-α-只有一個壞的-β)
- [5. 第一個靈感：讓承諾有陷門](#5-第一個靈感讓承諾有陷門)
  - [5.1 公鑰加密](#51-公鑰加密)
  - [5.2 用加密當承諾，公鑰放在 CRS](#52-用加密當承諾公鑰放在-crs)
  - [5.3 陷門不能公開](#53-陷門不能公開)
- [6. 全同態加密](#6-全同態加密)
- [7. 第二個靈感：加密一個函數 g](#7-第二個靈感加密一個函數-g)
  - [7.1 雜湊函數](#71-雜湊函數)
  - [7.2 分析時換成特別的 g*](#72-分析時換成特別的-g)
  - [7.3 Soundness 的證明](#73-soundness-的證明)
  - [7.4 小作弊：需要循環安全](#74-小作弊需要循環安全)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:12](https://youtu.be/R2izY69q0m8?t=12)

**課務**：
- 作業第 2B 題有點問題，網站上公告了要加的假設。
- 下週感恩節。再下週講者去給主題演講；那堂講 **BARG**（batch arguments，批次論證），由論文作者之一親自來講。最後一堂把所有東西收起來，得到整學期的目標（SNARG）。
- ⚠️ 逐字稿缺字：字幕寫作者是「Jain Jin, Choudhuri, Jain Jin」，依 OCW 第 9 講讀物應為 **Choudhuri、Jain、Jin**；來講的是 Jin。

**回顧**（[▶ 02:20](https://youtu.be/R2izY69q0m8?t=140)）：GKR → PCP → Kilian–Micali（4 則訊息、簡短）→ Fiat–Shamir（ROM 下對 Kilian–Micali sound）。問題是：換成具體的雜湊，還 sound 嗎？這曾是很重要的開放問題，因為 Fiat–Shamir 到處都在用。

【口頭】[▶ 05:07](https://youtu.be/R2izY69q0m8?t=307) ROM 結果是很好的替身：ROM 下證明安全的實用方案沒有一個被破解過。「老實說我還是不懂它為什麼是這麼好的替身，這讓我很驚訝。」Kilian–Micali 本身就是 ROM 下安全、但某些（刻意的）CRH 下對任何具體雜湊都不安全的例子。

**本集**：證明平行重複的 Blum 協定（配合特定的承諾），在標準模型下用一個具體的雜湊套 Fiat–Shamir 仍是 sound 的。假設：**循環安全的全同態加密**（circular-secure FHE），可由循環安全的 **LWE**（learning with errors）實作。【口頭】今天已經知道怎麼拿掉循環安全的假設，但今天講的版本用它，比較簡單。

---

## 1. 回顧：平行重複的 Blum 協定

[▶ 07:10](https://youtu.be/R2izY69q0m8?t=430)

單次 Blum 協定（第 10 集）：
1. $P$：隨機排列 $\pi$，承諾 $\pi(G)$ 上哈密頓圈的 $n\times n$ 矩陣（只有圈上是 1）。
2. $V$：隨機位元 $b$。
3. $b = 0$：打開圈的位置，檢查是 1、而且形成圈。$b = 1$：給 $\pi$，打開 $\pi(G)$ 所有非邊，檢查是 0。

單次 soundness 只有 1/2，連 ROM 都不安全。所以**本集的 $(P, V)$ 一律指平行重複 $\lambda$ 次的版本**：$P$ 一次送 $\lambda$ 份承諾（**每份用新的排列**），$V$ 送 $\lambda$ 個位元，$P$ 回 $\lambda$ 份打開。

【口頭】為什麼每份都要新的排列？用同一個 $\pi$ 的話，$b = 0$ 和 $b = 1$ 都被問到時，你就全知道了。

上集證明：常數回合＋可忽略 soundness ⟹ ROM 下 sound，所以它在 ROM 下安全。

---

## 2. 為什麼重要：NIZK、SNARG、BARG

[▶ 13:22](https://youtu.be/R2izY69q0m8?t=802)

「我為什麼這麼執著這個協定？讓我給你們一個保持清醒的理由。」

1. 對這個協定套 Fiat–Shamir，會得到**非互動零知識證明**（NIZK）。**從格（lattice）假設得到 NIZK** 曾是很久的開放問題，就是這篇（**Canetti、Lombardi、Wichs**）解決的。
2. 這個技巧**很一般**，不只適用這個協定。之後用同樣的技巧證明 **GKR** 套 Fiat–Shamir 在 LWE（或 FHE）下安全，得到 SNARG。
3. 感恩節後，Jin 會用**同樣的工具**得到 NP 的批次論證。「這種 Fiat–Shamir 幾乎被烤進我們所有的結果裡。」

- ⚠️ 逐字稿缺字：[▶ 14:43](https://youtu.be/R2izY69q0m8?t=883) 字幕寫「G-CARE protocol」，應為 **GKR** 協定。

---

## 3. 跟「Fiat–Shamir 和零知識互相矛盾」有沒有衝突

【Q&A】[▶ 15:24](https://youtu.be/R2izY69q0m8?t=924) 上次說零知識的協定不可能 Fiat–Shamir 安全；現在卻說它 Fiat–Shamir 安全、還得到非互動零知識。矛盾嗎？

1. **平行**重複後的 Blum 協定，本來就沒理由相信它是零知識（只知道單次、循序重複是零知識）。
2. 這個結果的確顯示平行重複不保持零知識，「幾乎」：因為承諾會改成特別的版本，所以不完全是原本那個協定。
3. **NIZK 的模擬器比作弊證明者更強**：它可以自己**選共同參考字串**（CRS）。上次的論證是「模擬器可以拿來當作弊證明者」；在非互動模型裡不行，因為作弊證明者不能選 CRS。（第 13 集細講。）

---

## 4. 核心觀察：每個 α 只有一個壞的 β

[▶ 20:22](https://youtu.be/R2izY69q0m8?t=1222)

【口頭】「這是我們以為非常非常難、結果換個角度想就非常簡單的例子。我要你們跟我一起想出證明。」

一般地看三則訊息協定 $\alpha, \beta, \gamma$。要找一個雜湊 $H$ 讓 Fiat–Shamir sound。固定 $x\notin L$：

- 因為是**證明系統**，對每個 $\alpha$，只有**很少**的 $\beta$ 存在被接受的 $\gamma$。
- 對平行 Blum 協定更具體：每一份承諾，作弊者**只能答其中一個挑戰**（$b = 0$ 或 $b = 1$），不能兩個都答（兩個都答就表示 $G$ 有哈密頓圈）。所以對每個 $\alpha$，**恰好有一個**壞的挑戰
$$\beta_{\mathrm{bad}}(\alpha).$$

**所以只要**：找一個雜湊，使得對**每個** $\alpha$，$H(\alpha)\neq\beta_{\mathrm{bad}}(\alpha)$。

「這能有多難？只要避開一個。」例如 $H(\alpha) := \beta_{\mathrm{bad}}(\alpha)\oplus 1$。

【Q&A】[▶ 26:09](https://youtu.be/R2izY69q0m8?t=1569) **承諾用的是計算假設，壞 $\beta$ 不一定唯一吧？** 這裡的承諾會是**統計綁定**的（只有隱藏性是計算的）：真的只能用一種方式打開。學生：鴿籠原理，很多排列對應一個？沒關係：兩種挑戰都答得出，就表示 $G$ 有哈密頓圈。

【課堂討論】[▶ 27:33](https://youtu.be/R2izY69q0m8?t=1653) 講者問 $H(\alpha) = \beta_{\mathrm{bad}}(\alpha)\oplus 1$ 哪裡不行？學生答：**要打開承諾才知道哪個是壞的 $\beta$**。

- 算 $\beta_{\mathrm{bad}}$ 很**難**。如果簡單，就根本不需要互動：給 $\alpha$、自己算出 $\beta$、再給 $\gamma$，等於一個 NP 證據。「互動的力量正在於：算出壞的 $\beta$ 是難的。」

---

## 5. 第一個靈感：讓承諾有陷門

[▶ 29:37](https://youtu.be/R2izY69q0m8?t=1777)

**想法**：如果承諾有一個**陷門**（trapdoor），有了它就能打開承諾、算出 $\beta_{\mathrm{bad}}$。

### 5.1 公鑰加密

[▶ 31:47](https://youtu.be/R2izY69q0m8?t=1907)

> **公鑰加密**（訊息空間 $\mathcal{M}$）：三個 PPT 演算法
> - $\mathrm{Gen}\to(pk, sk)$
> - $\mathrm{Enc}(pk, m)\to ct$（隨機化的）
> - $\mathrm{Dec}(sk, ct)\to m$ 或失敗
>
> **正確性**：對每個 $m$，$\Pr_{(pk, sk)\leftarrow\mathrm{Gen}}\left[ \mathrm{Dec}(sk, \mathrm{Enc}(pk, m)) = m \right] = 1$。
>
> **語意安全**（semantic security）：對每對**固定的** $m_0, m_1\in\mathcal{M}$，
> $$(pk, \mathrm{Enc}(pk, m_0))\approx_c(pk, \mathrm{Enc}(pk, m_1)),\quad (pk, sk)\leftarrow\mathrm{Gen}.$$

- 訊息長度會洩漏，通常固定大小。這裡想成 $\mathcal{M} = \{0, 1\}$，長訊息就一位元一位元加密（理論上這樣做；實務上不夠快）。
- 很多假設都能造（格、離散對數……），這門課不講構造。

### 5.2 用加密當承諾，公鑰放在 CRS

[▶ 37:37](https://youtu.be/R2izY69q0m8?t=2257)

把承諾換成**加密**：$\mathrm{Enc}(pk, \cdot)$。
- **隱藏**：語意安全 → 驗證者不知道裡面是什麼，仍是零知識。
- **綁定**：加密了就卡住了，用 $sk$ 一定解回同一個訊息。
- **陷門**：$sk$。有了它就能看到哪裡是 1、哪裡是 0，算出 $\beta_{\mathrm{bad}}$。
- **打開**：證明者不用 $sk$（沒人知道 $sk$），而是**公開加密時用的隨機數**，驗證者重算加密比對。

【Q&A】[▶ 38:18](https://youtu.be/R2izY69q0m8?t=2298) **會不會有另一把秘密鑰把它解成別的？** 依定義不會：正確性要求對 $\mathrm{Gen}$ 產生的金鑰對，解密一定得到原訊息。

【Q&A】[▶ 39:40](https://youtu.be/R2izY69q0m8?t=2380) **保證都假設 $pk$ 是照 $\mathrm{Gen}$ 產生的。如果讓證明者自己產生 $pk$ 呢？** 「你找到問題了。」而且不是假設性的：用的格方案正有這個問題，**壞的公鑰看起來和好的一樣，但沒有綁定**，可以打開成兩種。

**解法**：假設一個**共同參考字串**（CRS）：可信的一方照 $\mathrm{Gen}$ 產生 $pk$，大家都同意，**沒有人有 $sk$**（協定裡從來不用 $sk$）。

【Q&A】[▶ 43:14](https://youtu.be/R2izY69q0m8?t=2594) **那 CRS 就不能是均勻隨機字串？** 這個方案的公鑰不是隨機的（LWE 結構），但和隨機**不可區分**。如果在這種公鑰下 sound，換成完全隨機的字串 soundness 也成立。論文就利用這點：
- 用真的公鑰 → **統計 soundness、計算零知識**；
- 用假的（例如全 0 或隨機）公鑰 → **計算 soundness、統計零知識**。
可以在兩者之間調。

【Q&A】[▶ 45:20](https://youtu.be/R2izY69q0m8?t=2720) **叫證明者打開時附上產生 $pk$ 的隨機數？** 能保證 soundness，但會破壞零知識：那組隨機數也產生了 $sk$。

### 5.3 陷門不能公開

[▶ 46:46](https://youtu.be/R2izY69q0m8?t=2806)

從現在起，忘掉「承諾是加密」，只記得：**承諾有一個陷門 $td$，有了它能有效率地算出 $\beta_{\mathrm{bad}}(\alpha)$**（打開所有格子，看非邊是不是全 0 等等）。

- 講者先說可能還要承諾 $\pi$，想了一下覺得不需要（打開就看得到）。
- 【Q&A】[▶ 61:27](https://youtu.be/R2izY69q0m8?t=3687) 怎麼用陷門算 $\beta_{\mathrm{bad}}$：打開每一份承諾。如果某條 $\pi(G)$ 的非邊位置是 1，$b = 1$ 一定失敗，所以壞的是 $b = 0$；如果非邊全是 0，就不可能打開成哈密頓圈（$G$ 沒有），壞的是 $b = 1$。
- 【Q&A】[▶ 63:32](https://youtu.be/R2izY69q0m8?t=3812) **陷門是承諾時用的隨機數嗎？** 不是，是**對應 CRS 公鑰的秘密鑰**。用隨機數不行：設計雜湊時不知道作弊者會用什麼隨機數（他甚至可能是決定性的），每個作弊者都不一樣。秘密鑰不在協定裡用，**只在分析裡用**。

**問題**：把 $td$ 寫進 Fiat–Shamir 雜湊（$H(\alpha) = \beta_{\mathrm{bad}}(\alpha)\oplus 1$ 用 $td$ 算）就公開了 $td$，**零知識就沒了**。

【口頭】[▶ 48:59](https://youtu.be/R2izY69q0m8?t=2939) 之前有一系列工作試著把陷門**混淆**（obfuscation）起來，「丟了很多大錘子」，得到非常強、不知道對不對的假設，方法很亂。然後就是這篇。

---

## 6. 全同態加密

[▶ 50:19](https://youtu.be/R2izY69q0m8?t=3019)

**第二個靈感**：給**陷門的加密** $\widehat{td}$（帽子是全同態加密的常用記號）。「然後呢？密文就是垃圾。」所以要用**全同態加密**：可以在加密的資料上計算。

> **全同態加密**（fully homomorphic encryption, FHE）：公鑰加密 $(\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$，加上
> $$\mathrm{Eval}(pk, C, ct_1, \ldots, ct_n)\to ct,$$
> $C:\{0,1\}^n\to\{0,1\}$ 是 mod 2 加法、乘法閘組成的多項式大小電路，$ct_i$ 各加密一個位元 $b_i$。
>
> **Eval 的正確性**：
> $$\Pr\left[ \mathrm{Dec}\left( sk, \mathrm{Eval}(pk, C, \mathrm{Enc}(pk, b_1), \ldots, \mathrm{Enc}(pk, b_n)) \right) = C(b_1, \ldots, b_n) \right]\ge 1 - \mathrm{negl}.$$

（$1 - \mathrm{negl}$ 而不是 1，因為現有方案有可忽略的錯誤機率。）

【Q&A】[▶ 56:34](https://youtu.be/R2izY69q0m8?t=3394) $C$ 是什麼？任何 mod 2 加法、乘法閘的多項式大小電路。

**天真的想法**（[▶ 57:19](https://youtu.be/R2izY69q0m8?t=3439)）：雜湊裡放 $\widehat{td}$，在加密底下算 $\beta_{\mathrm{bad}}(\alpha)\oplus 1$。輸出是「$\beta_{\mathrm{bad}}(\alpha)\oplus 1$ 的加密」。
- 我們要的是輸出**本身**不等於 $\beta$，不是「底下的東西」不等於 $\beta$。
- 而且**型別都對不上**：$\beta$ 是 $\lambda$ 位元；密文是一位元一位元加密的，長度是 $\lambda$ × 安全參數。
- 「他們第一次講這個想法時，我覺得完全沒用。」

【Q&A】[▶ 73:28](https://youtu.be/R2izY69q0m8?t=4408) Anand：**能不能改協定，叫證明者在加密底下也算出 $\gamma$？** 講者想了一下，覺得可能可以，但會改變協定（不再公開可驗證，要解密才看得到）。更重要的是：**實際的方案裡，CRS 根本不含陷門的加密**，只是加密了一個無用的東西；分析時才換成陷門（兩者不可區分）。所以在實際方案裡，那個加密的 $\gamma$ 沒有意義。

---

## 7. 第二個靈感：加密一個函數 g

### 7.1 雜湊函數

[▶ 67:45](https://youtu.be/R2izY69q0m8?t=4065)

> **Fiat–Shamir 雜湊（CLW）**：
> - **金鑰**：$hk = (pk, \hat{g})$，$(pk, sk)\leftarrow\mathrm{FHE.Gen}$，$\hat{g} = \mathrm{Enc}(pk, \langle g\rangle)$ 是某個電路 $g$ 的描述（大小 $T$）的位元一位元加密。**實際方案裡 $g$ 就是全 0 字串** $0^{T}$（反正沒人會解密）。
> - **求值**：
> $$H_{hk}(\alpha) := \mathrm{FHE.Eval}(pk, U_{\alpha}, \hat{g}),\qquad U_{\alpha}(g) := g(\alpha).$$
> 也就是在加密底下算 $g(\alpha)$，輸出 $\widehat{g(\alpha)}$（一個密文）。

- $U_{\alpha}$ 是萬用電路：輸入電路 $g$ 的描述，輸出 $g(\alpha)$。
- 有兩個「Eval」：雜湊的求值、FHE 的 Eval，容易混淆。
- 【口頭】「你們應該非常困惑，我來解釋。」

### 7.2 分析時換成特別的 g*

[▶ 76:22](https://youtu.be/R2izY69q0m8?t=4582)

我們只需要：對每個 $\alpha$，$H_{hk}(\alpha)\neq\beta_{\mathrm{bad}}(\alpha)$。

**分析時**，把 $g$ 換成這個特別的 $g^{*}$（$td$ 和 $sk$ 寫死在裡面）：

$$g^{*}(\alpha) := \mathrm{Dec}\left( sk,\ \beta_{\mathrm{bad}}(\alpha) \right)\oplus 1.$$

逐步：
1. 用陷門 $td$ 算出 $\beta_{\mathrm{bad}}(\alpha)$（一個 $\lambda$ 位元的字串）。
2. 把這個字串**當成密文**，用 FHE 的 $sk$ **解密**。它根本不是密文，只是一串隨機的 0/1，「解密它是什麼意思？」但 $\mathrm{Dec}(sk, \cdot)$ 就是一個函數，可以對任何字串算。（把長度設成對得上。）
3. 某一位 XOR 1，讓它變得不一樣。

【Q&A】[▶ 77:58](https://youtu.be/R2izY69q0m8?t=4678) 符號：$\widehat{g(\alpha)}$ 是 $\mathrm{Enc}(pk, g(\alpha))$，帽子蓋住整個。

### 7.3 Soundness 的證明

[▶ 80:50](https://youtu.be/R2izY69q0m8?t=4850)

**Claim 1（資訊理論）**：用 $g^{*}$ 時，對每個 $\alpha$，$H(\alpha)\neq\beta_{\mathrm{bad}}(\alpha)$。

證明：假設 $H(\alpha) = \widehat{g^{*}(\alpha)} = \beta_{\mathrm{bad}}(\alpha)$。兩邊都套 $\mathrm{Dec}(sk, \cdot)$（決定性的函數，相等的字串解密還是相等）：

$$\underbrace{\mathrm{Dec}\left( sk, \widehat{g^{*}(\alpha)} \right)}_{= g^{*}(\alpha)\ (\text{FHE 正確性})} = \mathrm{Dec}\left( sk, \beta_{\mathrm{bad}}(\alpha) \right).$$

但 $g^{*}(\alpha) = \mathrm{Dec}(sk, \beta_{\mathrm{bad}}(\alpha))\oplus 1\neq\mathrm{Dec}(sk, \beta_{\mathrm{bad}}(\alpha))$。矛盾。$\blacksquare$

（嚴格說 FHE 的 Eval 正確性只有 $1 - \mathrm{negl}$，所以這是高機率成立。）

**Claim 2（計算）**（[▶ 82:16](https://youtu.be/R2izY69q0m8?t=4936)）：假設多項式大小的 $P^{*}$ 對某個沒有哈密頓圈的 $G$，在 $hk = (pk, \widehat{0^{T}})$ 下以不可忽略的機率 $\varepsilon$ 作弊成功。那麼在 $hk^{*} = (pk, \widehat{g^{*}})$ 下，他也以約 $\varepsilon - \mathrm{negl}$ 的機率成功。理由：**語意安全**，他分不出 $\widehat{0^{T}}$ 和 $\widehat{g^{*}}$。

- 【Q&A】[▶ 84:21](https://youtu.be/R2izY69q0m8?t=5061) 這裡用到證明者有效率？對，所以這是**計算 soundness**。

**合起來**：在 $hk^{*}$ 下作弊成功，代表找到 $\alpha$ 使得 $H(\alpha)$ 是壞的 $\beta$（壞 $\beta$ 的定義就是「能作弊的 $\beta$」）。但 Claim 1 說用 $g^{*}$ **永遠不會**撞到壞的 $\beta$。矛盾。$\blacksquare$

- **$T$ 是多少**（【Q&A】[▶ 92:49](https://youtu.be/R2izY69q0m8?t=5569)）：表示 $g^{*}$ 所需的位元數，因為分析時要把 $0^{T}$ 換成 $g^{*}$ 的描述。

### 7.4 小作弊：需要循環安全

[▶ 85:45](https://youtu.be/R2izY69q0m8?t=5145)

學生指出：$g^{*}$ 裡寫死了 $sk$。

- 加密 $td$ 沒問題：它和這把 FHE 公鑰無關，是固定的訊息。
- 但 $g^{*}$ 裡還有**這把 FHE 公鑰自己的秘密鑰 $sk$**。語意安全只說「兩個**固定**訊息的加密不可區分」，沒說「秘密鑰自己的加密」和「0 的加密」不可區分。

> **循環安全**（circular security）：
> $$(pk, \mathrm{Enc}(pk, sk))\approx_c(pk, \mathrm{Enc}(pk, 0^{|sk|})).$$
> （位元一位元加密：$\lambda$ 個密文，各加密 $sk$ 的一個位元，和 $\lambda$ 個 0 的加密不可區分。）

- 有沒有循環安全的 FHE？在**循環安全的 LWE** 假設下有。「我們相信它是對的，但不知道。」
- 【口頭】其實可以不用：有後續工作看進具體的格方案，用一堆格的技巧拿掉循環安全的需求（本課不講）。

【Q&A】[▶ 87:08](https://youtu.be/R2izY69q0m8?t=5228) **$\beta_{\mathrm{bad}}$ 是給定的還是算的？** 是 $g^{*}$ 用 $td$ **算**出來的。學生又問 $td$ 是不是秘密鑰：是承諾那個加密方案的秘密鑰（和 FHE 的 $sk$ 是兩把不同的鑰匙）。「最好忘掉承諾也是加密，不然兩套加密會混淆。」

---

## 8. 一頁速查表

### 目標

平行 Blum 協定（承諾用加密、$pk$ 在 CRS）在標準模型下 Fiat–Shamir sound。

### 關鍵觀察

$x\notin L$ 時每個 $\alpha$ 恰有一個 $\beta_{\mathrm{bad}}(\alpha)$。只要 $H(\alpha)\neq\beta_{\mathrm{bad}}(\alpha)$ 對所有 $\alpha$ 成立。困難：$\beta_{\mathrm{bad}}$ 難算；有陷門 $td$ 就好算，但 $td$ 不能公開。

### CLW 雜湊

- $hk = (pk, \mathrm{FHE.Enc}(pk, 0^{T}))$；$H_{hk}(\alpha) = \mathrm{FHE.Eval}(pk, U_{\alpha}, \hat{g})$。
- 分析：$g^{*}(\alpha) = \mathrm{Dec}(sk, \beta_{\mathrm{bad}}(\alpha))\oplus 1$（用 $td$ 算 $\beta_{\mathrm{bad}}$）。
- Claim 1：$H_{hk^{*}}(\alpha) = \beta_{\mathrm{bad}}(\alpha)$ ⟹ 兩邊解密 ⟹ $g^{*}(\alpha) = \mathrm{Dec}(sk, \beta_{\mathrm{bad}}(\alpha))$，矛盾。
- Claim 2：$\widehat{0^{T}}\approx_c\widehat{g^{*}}$（需要**循環安全**，因為 $g^{*}$ 含 $sk$）。
- 結論：計算 soundness。

### 公鑰加密／FHE

- 正確性、語意安全（固定 $m_0, m_1$）。
- FHE：$\mathrm{Eval}(pk, C, ct_1, \ldots, ct_n)$ 解密得 $C(b_1, \ldots, b_n)$（$1 - \mathrm{negl}$）。
- 循環安全：$\mathrm{Enc}(pk, sk)\approx_c\mathrm{Enc}(pk, 0)$。

### CRS 的取捨

真公鑰 → 統計 soundness、計算 ZK；隨機字串 → 計算 soundness、統計 ZK。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Fiat–Shamir 後的平行 Blum 協定 | 第 13 集：NIZK 的定義與證明 |
| 「加密一個避開壞挑戰的函數」的技巧 | 第 13 集：推廣到 GKR / sum-check（相關性難解） |
| FHE、LWE | 第 14–15 集：BARG from LWE |
| BARG | 第 14–17 集 |

---

## 附：本集一句話總結

> **對平行重複的 Blum 協定，假的命題下每個 $\alpha$ 只有一個「壞」挑戰；CLW 的雜湊是「在 FHE 底下算一個加密的電路 $g$」——實際上 $g$ 是全 0，分析時換成「把壞挑戰當密文解密再翻一位」的 $g^{*}$，於是雜湊的輸出一解密就和壞挑戰不同、永遠撞不到它，而作弊者分不出這兩種金鑰（需要循環安全）。**

---

## ⚠️ 待確認清單

1. 本集的指定讀物 Canetti–Lombardi–Wichs（ePrint 2018/1248）自動下載被擋，筆記沒有對照論文。構造細節（例如 $\beta_{\mathrm{bad}}$ 解密時長度怎麼對齊、$T$ 的確切大小、如何拿掉循環安全）待取得論文後補。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 7 Part 1 錄影逐字稿（MIT 真人字幕，1:33:40）整理；本集無次要來源。*
