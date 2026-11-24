---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 08
lecture: Lecture 5 (Part 1) – The Kilian-Micali Protocol
date: 待補（2023 秋季第五堂課；前一週是 crypto day）
video: https://youtu.be/OO2qyzBAD14
notes: Thaler §9.2（書頁 135–137，PDF 頁 136–138）；Micali「Computationally Sound Proofs」（SIAM J. Comput. 30(4), 2000）
---

# 第 08 集 · Lecture 5 (Part 1)：Kilian–Micali 協定——有局部打開的雜湊、協定、soundness [▶ 影片](https://youtu.be/OO2qyzBAD14)

← 上一集：[07-pcp-via-gkr-part2](07-pcp-via-gkr-part2.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[09-kilian-micali-part2](09-kilian-micali-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 08 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:44:35，MIT 上傳的真人字幕）＋ Thaler §9.2；Micali（OCW 指定讀物）
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書和論文都沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：GKR → PCP](#1-回顧gkr--pcp)
- [2. 回顧：論證，以及安全參數該多大](#2-回顧論證以及安全參數該多大)
- [3. 有局部打開的抗碰撞雜湊](#3-有局部打開的抗碰撞雜湊)
  - [3.1 五個演算法](#31-五個演算法)
  - [3.2 正確性](#32-正確性)
  - [3.3 抗碰撞（綁定）](#33-抗碰撞綁定)
- [4. Kilian–Micali 協定](#4-kilianmicali-協定)
  - [4.1 協定](#41-協定)
  - [4.2 為什麼不直接跑互動式 GKR](#42-為什麼不直接跑互動式-gkr)
  - [4.3 通訊量](#43-通訊量)
  - [4.4 驗證者可以只送隨機數](#44-驗證者可以只送隨機數)
- [5. Completeness](#5-completeness)
- [6. Soundness（第一個證明）](#6-soundness第一個證明)
  - [6.1 歸約：用作弊者找碰撞](#61-歸約用作弊者找碰撞)
  - [6.2 沒有碰撞 ⟹ 拼出一個會被接受的 PCP](#62-沒有碰撞--拼出一個會被接受的-pcp)
  - [6.3 這個證明的漏洞](#63-這個證明的漏洞)
  - [6.4 Q&A：一定要倒帶嗎](#64-qa一定要倒帶嗎)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:12](https://youtu.be/OO2qyzBAD14?t=12)

上週是 crypto day，沒上課。本集：

1. 回顧 PCP 和論證。
2. 定義**有局部打開的抗碰撞雜湊**。
3. **Kilian–Micali 協定**：用 PCP＋雜湊造 NP 的簡短論證；證明 completeness 和 soundness（第一個證明，有漏洞）。

（休息後的第 09 集：更好的 soundness 證明、雜湊的構造。）

**作業**：這個週末公布。原本截止日在感恩節後，改到感恩節前（「讓你們不用帶著它去度假」）。需要延期就說。

---

## 1. 回顧：GKR → PCP

[▶ 00:54](https://youtu.be/OO2qyzBAD14?t=54)

- PCP：把證據**變長**，但驗證只要讀少數位置。
- 構造：把 3SAT 歸約到它的驗證電路 $C_{\varphi}$（深度很小：一堆局部檢查再 AND 起來）。在腦中跑 GKR：
  - PCP 裡先放**證據的低次擴張**（驗證者沒有輸入，「別擔心，我們給他」）；
  - 再對 GKR 驗證者**每個可能的問題**寫下證明者的回答。
- 看起來是指數大的樹，但 GKR 證明者**無記憶**：每則訊息只依賴最近一個 sum-check 的約 $m = \log n/\log\log n$ 則驗證者訊息，每則是 polylog 大的體元素，所以 $|\mathbb{F}|^m = \mathrm{poly}(n)$。「這就是為什麼選那組怪參數，而不是 $H = \{0,1\}$、$m = \log n$。」
- 驗證：假裝自己是 GKR 驗證者，沿著樹隨機走；最後檢查證據擴張在一個隨機點的值。

**缺的一塊**：低次檢驗。如果證明者給的 $W^{*}$ 不是低次的呢？作業裡要你**找出一個攻擊**，證明沒有低次檢驗就不可靠。驗證者沒辦法確認是低次，但可以確認**接近**低次（和某個低次 $W$ 在 $1 - \varepsilon$ 比例的點上一致）。

**PCP 一定要先固定**（[▶ 12:05](https://youtu.be/OO2qyzBAD14?t=725)）：如果不送 PCP，只讓證明者回答查詢，他可以依據所有查詢來選答案（問 $i$ 和 $j$ 時答一個，問 $i$ 和 $j'$ 時答另一個），soundness 完全崩潰。【口頭】回頭看 GKR 也是：如果把 sum-check 的所有問題都事先告訴證明者，一切都壞掉。

**問題**：驗證者很弱，誰來存這個巨大的 PCP？答案：用密碼學（抗碰撞雜湊）把它**壓扁**。

---

## 2. 回顧：論證，以及安全參數該多大

[▶ 14:49](https://youtu.be/OO2qyzBAD14?t=889)

**論證**：completeness 照舊（有證據的話，證明者也有效率）。Soundness：對每個大小 $\mathrm{poly}(\lambda)$ 的 $P^{*}$，存在可忽略的 $\mu$，使得對所有 $\lambda$ 和 $x\notin L$，

$$\Pr\left[ \langle P^{*}, V\rangle(x, 1^{\lambda}) = 1 \right]\le\mu(\lambda).$$

作弊者要想成**一族**證明者，每個 $\lambda$ 一個，例如都跑最多 $\lambda^{10}$ 時間。

【Q&A】[▶ 17:38](https://youtu.be/OO2qyzBAD14?t=1058) **這裡證明者要藏證據嗎？** 不，完全不管隱藏。如果不要簡短，直接把證據給驗證者就好。我們要的額外性質是**簡短**。

【Q&A】[▶ 18:18](https://youtu.be/OO2qyzBAD14?t=1098) **3SAT 的深度怎麼這麼小？** 3-CNF 是一堆子句的 AND。fan-in 2 的話，AND 排成二元樹深度 $O(\log m)$；每個子句是常數大小。

**安全參數該多大**（[▶ 21:45](https://youtu.be/OO2qyzBAD14?t=1305)）：

- 想要通訊 polylog，就取 $\lambda = \mathrm{polylog}(n)$。但這時作弊者只能跑 $\mathrm{poly}(\lambda)$，**連 $x$ 都讀不完**；誠實證明者卻能跑 $\mathrm{poly}(n)$。這很奇怪，保證太弱。
- 【Q&A】[▶ 25:12](https://youtu.be/OO2qyzBAD14?t=1512) 如果取 $\lambda = n^{\varepsilon}$（例如 $n^{0.001}$）呢？那就沒問題：通訊隨 $\lambda$ 成長仍遠小於 $n$，作弊者可以跑任何 $\mathrm{poly}(\lambda) = \mathrm{poly}(n)$ 時間。通常就是對每個 $n$ 選一個依賴 $n$ 的 $\lambda$。
- 但如果要 polylog：用**更強的假設**，假設大小 $2^{\lambda^{\varepsilon}}$ 的攻擊者也找不到碰撞（**次指數假設**）。這樣 $\lambda$ 很小，攻擊者仍可以跑遠大於 $\lambda$ 的時間。所以談簡短證明時，常見次指數假設。
- 一般化：說假設是「$T$-安全」（$T(\lambda)$ 大小的攻擊者破解不了），$T$ 可以是多項式、次指數……選定 $T$ 後，剩下就是數學。

【Q&A】[▶ 21:04](https://youtu.be/OO2qyzBAD14?t=1264) **整個互動協定的意義是不是在補「沒強迫證明者先固定 PCP」的洞？** 「就是這樣。」

---

## 3. 有局部打開的抗碰撞雜湊

[▶ 30:44](https://youtu.be/OO2qyzBAD14?t=1844)

目標：3SAT，證據長度 $n$，通訊只隨 $\lambda$ 成長。想法：證明者把 PCP **雜湊**，給驗證者一個摘要；驗證者再要求看 PCP 的少數位置。

一般的 CRH 只保證「給了雜湊值後，你不能打開成兩個不同的 $x, x'$」。但我們不想讓證明者送整個原像，只想看**幾個位元**，並確認它們對應到雜湊的那個輸入。

### 3.1 五個演算法

[▶ 33:31](https://youtu.be/OO2qyzBAD14?t=2011)

| 演算法 | 輸入 → 輸出 | 性質 |
|---|---|---|
| $\mathrm{Gen}(1^{\lambda})$ | → $hk$ | PPT（必須隨機） |
| $\mathrm{Eval}(hk, x)$ | $x\in\{0,1\}^{*}$ → $v\in\{0,1\}^{\lambda}$ | 決定性、多項式時間（跑 $|x|$ 時間） |
| $\mathrm{Open}(hk, x, i)$ | $i\in[|x|]$ → $(b, \rho)$，$b = x_i$，$|\rho| = \mathrm{poly}(\lambda)$ | 決定性、多項式時間（跑 $|x|$ 時間） |
| $\mathrm{Verify}(hk, v, i, b, \rho)$ | → $\{0, 1\}$ | 決定性、**$\mathrm{poly}(\lambda)$ 時間** |

- $\mathrm{Eval}$ 把任意長的輸入壓成 $\lambda$ 位元。
- ⚠️ 逐字稿缺字：[▶ 37:37](https://youtu.be/OO2qyzBAD14?t=2257) 講者先寫 $i\in\{0,1\}^{|x|}$，學生提醒應是索引 $i\in\{1, \ldots, |x|\}$（或 $\log|x|$ 位元），講者改正。
- **誰跑 Open**（【Q&A】[▶ 36:13](https://youtu.be/OO2qyzBAD14?t=2173)）：產生雜湊的人（證明者）。$\rho_i$ 是「我雜湊的東西第 $i$ 位確實是 $x_i$」的一個小證明。只給 $x_i$ 不給證明，他可以亂說。
- 【Q&A】[▶ 37:37](https://youtu.be/OO2qyzBAD14?t=2257) **要打開就得存著整個 $x$，很有趣。** 打開第 $i$ 位只需要 $\rho_i$，但所有 $\rho_i$ 合起來包含整個 $x$，所以要存。（看到構造就清楚了。）
- 【Q&A】[▶ 41:03](https://youtu.be/OO2qyzBAD14?t=2463) **為什麼 Eval 不能是隨機的？** 不是不行，只是不需要。Gen 必須是隨機的。
- $\mathrm{Verify}$ 只跑 $\mathrm{poly}(\lambda)$：輸入 $hk$、$v$、$\rho$ 都是 $\mathrm{poly}(\lambda)$ 大小，$b$ 是一個位元。**和 $n$ 無關**（$\lambda$ 可以依賴 $n$，但不隨 $n$ 成長）。

### 3.2 正確性

[▶ 41:44](https://youtu.be/OO2qyzBAD14?t=2504)

對每個 $\lambda$、每個 $hk\in\mathrm{Gen}(1^{\lambda})$ 的值域、每個 $|x|\le 2^{\lambda}$、每個 $i$：

$$\mathrm{Verify}\left( hk,\ \mathrm{Eval}(hk, x),\ i,\ x_i,\ \rho_i \right) = 1, \qquad (x_i, \rho_i) = \mathrm{Open}(hk, x, i).$$

- 誠實就一定通過，對**每個**金鑰都成立。也可以定義成「對隨機金鑰，$1 - \mathrm{negl}$ 機率」，但很多構造是機率 1。
- **為什麼 $|x|\le 2^{\lambda}$**（【Q&A】[▶ 44:31](https://youtu.be/OO2qyzBAD14?t=2671)）：構造的雜湊值大小隨 $\log|x|$ 成長，但我們想說輸出是 $\lambda$。所以總是取 $\lambda\ge\log|x|$。「我們從不把安全參數取得比 $\log n$ 小。」

### 3.3 抗碰撞（綁定）

[▶ 45:13](https://youtu.be/OO2qyzBAD14?t=2713)

> **$T$-抗碰撞**：對每個大小 $\mathrm{poly}(T(\lambda))$ 的攻擊者 $A$，存在可忽略的 $\mu$：
> $$\Pr_{hk\leftarrow\mathrm{Gen}(1^{\lambda})}\left[ (v, i, \rho_0, \rho_1)\leftarrow A(hk):\ \forall b\in\{0,1\},\ \mathrm{Verify}(hk, v, i, b, \rho_b) = 1 \right]\le\mu(\lambda).$$

白話：攻擊者給出雜湊值 $v$ 後，對任何位置 $i$，都**不能**同時給出打開成 0 和打開成 1 的有效證明。$T$ 可以是多項式，也可以是 $2^{\lambda^{\varepsilon}}$。

【Q&A】[▶ 43:49](https://youtu.be/OO2qyzBAD14?t=2629) **正確性對每個金鑰都成立，但抗碰撞需要金鑰是隨機的？** 對。

【課堂討論】[▶ 49:33](https://youtu.be/OO2qyzBAD14?t=2973) 講者問先講構造還是先講協定，大家選先講協定。

---

## 4. Kilian–Micali 協定

### 4.1 協定

[▶ 50:19](https://youtu.be/OO2qyzBAD14?t=3019)

**材料**：(1) 一個 PCP（例如 GKR 的 PCP），completeness 1、**soundness 可忽略**；(2) 有局部打開的抗碰撞雜湊。

**為什麼 PCP 的 soundness 要可忽略**（[▶ 54:30](https://youtu.be/OO2qyzBAD14?t=3270)）：論證的 soundness 要可忽略，而它取決於 PCP 的 soundness。GKR 的 PCP 跑一次只有 $1/\mathrm{polylog}$（體只有 polylog 大），不夠。重複：如果 soundness 是 1/2，就讓 PCP 驗證者重複 $\lambda$ 次，得到 $2^{-\lambda}$。

**共同輸入**：$x$、$1^{\lambda}$。證明者另有證據 $w$。（以 3-CNF 和滿足賦值為例。）

| 步驟 | 方向 | 內容 |
|---|---|---|
| 1 | $V\to P$ | $hk\leftarrow\mathrm{Gen}(1^{\lambda})$ |
| 2 | $P\to V$ | 【課堂討論】學生答：算 PCP $\pi$，再雜湊。送 $v = \mathrm{Eval}(hk, \pi)$ |
| 3 | $V\to P$ | 【課堂討論】學生答：照 **PCP 驗證者**的分布選位置。$V$ 跑 $V_{\mathrm{PCP}}(1^{\lambda}, n; r)$ 得到 $i_1, \ldots, i_{\ell}$，送出 |
| 4 | $P\to V$ | 對每個 $j$：$(\pi_{i_j}, \rho_{i_j}) = \mathrm{Open}(hk, \pi, i_j)$，送出 |
| 驗證 | | 【課堂討論】學生答：(a) 每個打開都通過 $\mathrm{Verify}(hk, v, i_j, \pi_{i_j}, \rho_{i_j}) = 1$；(b) $V_{\mathrm{PCP}}(x, i_1, \ldots, i_{\ell}, \pi_{i_1}, \ldots, \pi_{i_{\ell}}) = 1$ |

- PCP 從來不會被整個打開，只打開被查的位置。
- 【Q&A】[▶ 62:11](https://youtu.be/OO2qyzBAD14?t=3731) **查詢可以一次全送，還是要分好幾輪？** 用 PCP 的話**一次全送**就好：證明者已經被雜湊綁住了。如果改用互動式 GKR（下面），就得循序。
- 【Q&A】[▶ 63:33](https://youtu.be/OO2qyzBAD14?t=3813) PCP 驗證者那一步要 $x$ 嗎？要：驗證者永遠不讀整個 $\pi$，但要對照命題，所以要讀 $x$。驗證者時間對 $|x|$ 是線性的，但**通訊**很小。
- 【口頭】（PCP of proximity：驗證者連 $x$ 都不讀完，只能保證接受的命題「接近」在語言裡。本課不講。）

### 4.2 為什麼不直接跑互動式 GKR

【Q&A】[▶ 57:20](https://youtu.be/OO2qyzBAD14?t=3440) **3SAT 深度很小，GKR 本身就很簡短，何必攤開成 PCP 再加雜湊？**

【課堂討論】講者反問哪裡有問題，學生答：**驗證者需要證據**。GKR 假設驗證者有輸入，最後要拿擴張的值對照自己的輸入。這裡驗證者沒有證據。

但講者說，**實際上的實作更接近這個學生的想法**（[▶ 59:22](https://youtu.be/OO2qyzBAD14?t=3562)）：

1. 證明者只**雜湊證據的低次擴張**（不是整個 PCP）。
2. 雙方跑互動式 GKR。
3. GKR 最後需要擴張在一個隨機點的值：請證明者打開那一點。因為事先已經承諾了，他不能改。
4. 學生補充：還要加低次檢驗。講者：「沒錯。」

【口頭】近幾年很多工作不是在改進 GKR，而是在改進**承諾**（commitment）：怎麼做最有效率。現在還有更好的協定（IOP），「那是另一回事」。

【Q&A】[▶ 60:43](https://youtu.be/OO2qyzBAD14?t=3643) **不給驗證者證據，是因為太大？** 對。學生：所以沒有零知識性質？講者：現在完全不管零知識。實作時通常會在上面再加零知識，那是另一個方向。

> 【課本補充】Thaler §9.2 開頭說的正是這個做法（第 7 章）：證明者先送證據多線性擴張 $\tilde{w}$ 的密碼學承諾，雙方跑 GKR 檢查 $C(x, w) = y$；GKR 最後證明者要宣稱 $\tilde{w}(r)$ 的值，驗證者對照承諾。這個**多項式承諾**由 Merkle 樹（字串承諾）加上低次檢驗組成。如果改從 PCP 出發，就可以省掉承諾裡的低次檢驗（Remark 9.4：其實是推進 PCP 裡了）。

### 4.3 通訊量

[▶ 64:17](https://youtu.be/OO2qyzBAD14?t=3857)

| 訊息 | 大小 |
|---|---|
| $hk$ | $\mathrm{poly}(\lambda)$ |
| $v$ | $\lambda$ |
| $i_1, \ldots, i_{\ell}$ | 最多 $\mathrm{poly}(\lambda)$（PCP 查詢數 × $\log|\pi|$） |
| 打開 | $\ell\cdot\mathrm{poly}(\lambda)$ |

全部只隨 $\lambda$ 成長，不隨 $|x|$。$\lambda = \mathrm{polylog}(n)$ 時通訊就是 polylog。驗證打開的部分是 $\mathrm{poly}(\lambda)$；但 PCP 驗證要讀輸入，所以驗證者整體是 $|x|$ 的線性。

### 4.4 驗證者可以只送隨機數

[▶ 67:00](https://youtu.be/OO2qyzBAD14?t=4020)

第 3 步驟不必送 $i_1, \ldots, i_{\ell}$，可以**直接送 PCP 驗證者的隨機數 $r$**，讓證明者自己算位置。

**為什麼要強調**：下週要把互動拿掉（**Fiat–Shamir**），而它適用於「驗證者的訊息是**完全隨機**的位元」的協定。所以要記得：**第 3 則訊息可以是完全隨機的**。

第 1 則訊息（$hk$）不一定是隨機位元，**也不需要**：第一則訊息比較特別，Fiat–Shamir 不需要消掉它。

【Q&A】[▶ 69:48](https://youtu.be/OO2qyzBAD14?t=4188) **為什麼第一則特別？金鑰還是要抽樣吧？** 當然要抽樣。只是金鑰本身不一定是均勻隨機位元，要看用哪種雜湊（有些是隨機的，有些有 LWE 那種結構）。

【Q&A】[▶ 70:28](https://youtu.be/OO2qyzBAD14?t=4228) **那 Gen 也送隨機數不就好了？** 可以，但不是所有雜湊都行：很多雜湊只給金鑰時安全，但**給了產生金鑰的隨機數就可能找到碰撞**。我們等一下要造的那個可以（但依賴特定假設）。反正 Fiat–Shamir 只需要後面的訊息是隨機的。

【Q&A】[▶ 71:52](https://youtu.be/OO2qyzBAD14?t=4312) **$n$ 是什麼？為什麼 $n$ 用二進位、$\lambda$ 用一進位？** $n = |x|$，PCP 驗證者要知道它才知道查哪裡。用二進位是強調：**產生查詢**只要 $\mathrm{poly}(\lambda, \log n)$ 時間，不用對 $n$ 線性。（這裡反正要讀 $x$，所以不太重要；之後談 proximity 時會變重要。）

> 【課本補充】Thaler §9.2：Kilian 協定分 commit 和 reveal 兩階段。commit：證明者把 PCP 的符號當葉子建 **Merkle 樹**，送樹根雜湊。reveal：驗證者模擬 PCP 驗證者決定查詢 $q_1, \ldots, q_k$，證明者回傳 $\pi(q_1), \ldots, \pi(q_k)$ 和**驗證路徑**（authentication path）。通訊是每次查詢 $O(\log n)$ 個雜湊值。

---

## 5. Completeness

[▶ 73:55](https://youtu.be/OO2qyzBAD14?t=4435)

「簡單到不值得寫。」$x\in L$、有證據，誠實證明者：
- PCP 的 completeness 是 1，所以 $V_{\mathrm{PCP}}$ 一定接受；
- 雜湊的正確性是 1，所以每個 $\mathrm{Verify}$ 一定接受。

兩個都是機率 1，所以整體機率 1。

---

## 6. Soundness（第一個證明）

[▶ 76:02](https://youtu.be/OO2qyzBAD14?t=4562)

> **Claim**：若雜湊是 $T$-抗碰撞，PCP 的 soundness 可忽略，則協定對大小 $\mathrm{poly}(T)$ 的作弊者是 sound 的。

（$T$ 實際上要多大，等一下會看到：要相當大。）

### 6.1 歸約：用作弊者找碰撞

**假設**：存在大小 $\mathrm{poly}(T)$ 的 $P^{*}$、一串 $x_{\lambda}\notin L$、不可忽略的 $\varepsilon$，使得對每個 $\lambda$：

$$\Pr\left[ \langle P^{*}, V\rangle(x_{\lambda}, 1^{\lambda}) = 1 \right]\ge\varepsilon(\lambda).$$

（假設 $|x_{\lambda}|\le 2^{\lambda}$；這其實只有 completeness 需要。）

**想法**（[▶ 79:37](https://youtu.be/OO2qyzBAD14?t=4777)）：作弊者雜湊了「某個東西」，然後打開它。我要**倒帶**（rewind）他：同一個 $v$，給他很多組不同的查詢，收集很多打開。

**攻擊者 $A(hk)$**：

1. $v\leftarrow P^{*}(hk)$。
2. 對 $j = 1, \ldots, M$（$M = \mathrm{poly}(|\pi|, 1/\varepsilon)$）：
   - 選新的隨機數 $r_j$，算出 PCP 查詢 $i_1, \ldots, i_{\ell}$；
   - 把 $P^{*}$ **倒帶回送出 $v$ 之後**，給他這組查詢，記下他的回答和打開 $(\pi_{i_k}, \rho_{i_k})$。
   - 打開沒通過的，丟掉（他只有 $\varepsilon$ 比例成功，所以會丟掉 $1 - \varepsilon$ 比例；$M$ 取到 $\mathrm{poly}(1/\varepsilon)$ 以上，剩下的還很多）。
3. 如果某個位置 $i$ 曾被**有效地**打開成 0、也曾被有效地打開成 1，輸出這組碰撞。

- ⚠️ 逐字稿缺字：[▶ 87:17](https://youtu.be/OO2qyzBAD14?t=5237) 講者說「丟掉 $\varepsilon$」，學生更正為「丟掉 $1 - \varepsilon$，留下 $\varepsilon$」，講者同意。
- 講者說 $M$ 可以想成「PCP 長度乘 $\lambda$ 除以 $\varepsilon^3$」這種量級。

### 6.2 沒有碰撞 ⟹ 拼出一個會被接受的 PCP

[▶ 88:47](https://youtu.be/OO2qyzBAD14?t=5327)

兩種情形：

1. **找到碰撞的機率不可忽略**：$A$ 破解了雜湊，矛盾（假設雜湊是安全的）。
2. **找到碰撞的機率可忽略**：（想成「從沒遇過碰撞」。）那每個位置 $i$，只要被有效打開過，**永遠是同一個值**。把這些值拼起來成為一個 PCP $\hat{\pi}$：
   - 被有效打開過的位置：填那個值；
   - 從沒被有效打開過的（作弊者每次被問都失敗），或驗證者從沒問過的位置：填 0。

**Claim**：$V_{\mathrm{PCP}}^{\hat{\pi}}(x_{\lambda})$ 接受的機率約 $\mathrm{poly}(\varepsilon)$，不可忽略。但 $x_{\lambda}\notin L$，PCP 的 soundness 可忽略，矛盾。

**為什麼 $\hat{\pi}$ 會被接受**（[▶ 93:41](https://youtu.be/OO2qyzBAD14?t=5621)）：
- $P^{*}$ 成功時，他答的就是 $\hat{\pi}$ 裡的值（沒有碰撞）。
- 擔心的是：驗證者查到 $\hat{\pi}$ 裡填 0 的位置。但為什麼那裡是 0？因為**問了很多次，作弊者每次都失敗**（或驗證者從來不問那裡）。所以在那些位置，作弊者本來也會失敗。
- 「我們問了這麼多次，如果他在那裡會成功，我們早就拿到正確答案了。」所以「我們失敗而他成功」的機率非常小。

【口頭】細節很繁瑣，網站上有論文連結。而且講者說：**「這不是對的證明。」**

### 6.3 這個證明的漏洞

[▶ 95:47](https://youtu.be/OO2qyzBAD14?t=5747)

「我騙了你們。」

- 要得到矛盾，$A$ 必須在 $\mathrm{poly}(T(\lambda))$ 時間內找到碰撞（假設是 $T$-抗碰撞）。
- 跑 $P^{*}$：$\mathrm{poly}(T)$，沒問題。重複 $1/\varepsilon$ 次：$\varepsilon\ge 1/\mathrm{poly}(T)$，也沒問題。
- 但 $A$ 要**拼出整個 PCP**，必須重複 $\mathrm{poly}(|\pi|) = \mathrm{poly}(n)$ 次。如果 $T(\lambda) < n$，$A$ 就太慢了。
- 所以這個證明**只在 $T(\lambda)\ge n$ 時成立**。

【口頭】你可能說：$T(\lambda)$ 本來就該大於 $n$，不讓作弊者跑 $\mathrm{poly}(n)$ 時間的定義不合理。也許，也許不是：也許應用裡作弊者真的不會跑 $n$ 時間。這一直**困擾著密碼學家**：雖然假設 $T(\lambda)\ge n$ 合理，但被迫要這樣很煩。

**Barak–Goldreich 2002** 有一篇漂亮的論文，對**任何** $T$ 都成立。他們**不拼整個 PCP**，「我覺得更聰明、更漂亮，是這個定理對的證明」。休息後講（第 09 集）。

【Q&A】[▶ 102:42](https://youtu.be/OO2qyzBAD14?t=6162) **$n$ 是 PCP 的長度？** 對，嚴格說要放 PCP 長度。3SAT 的實例、證據、PCP 長度都多項式相關，所以沒差。但一般證據可能遠小於實例（例如 log-clique：證據 $\log^2 n$，實例 $n$），也可能遠大於（非決定性時間 $T$：證據 $T(n)$ 可能超多項式）。PCP 長度永遠和「實例＋證據」多項式相關。

### 6.4 Q&A：一定要倒帶嗎

【Q&A】[▶ 100:00](https://youtu.be/OO2qyzBAD14?t=6000) **倒帶是必要的嗎？**
就目前所知，是。這個問題對**後量子**很重要：如果作弊者是量子裝置，就不能倒帶，因為量測量子態會讓它塌縮。證明這個協定是後量子安全的很費工，要說明為什麼能倒帶量子作弊者；結論是可以，**它已知是後量子安全的**。但「我們沒有不倒帶（straight-line）的 soundness 證明」。

追問：是因為要拼證據嗎？第 09 集的證明不拼整個 PCP，但要找碰撞**至少要跑兩次**：選一個隨機位置 $i$，一次配一組查詢、一次配另一組查詢；作弊的唯一方法是前後不一致。

【Q&A】[▶ 102:02](https://youtu.be/OO2qyzBAD14?t=6122) **用具體的雜湊函數能避免倒帶嗎？** 講者不這麼認為。看進雜湊函數內部只會更亂；把雜湊抽象成它提供的性質，證明反而更乾淨。

---

## 7. 一頁速查表

### 有局部打開的 CRH

- $\mathrm{Gen}(1^{\lambda})\to hk$；$\mathrm{Eval}(hk, x)\to v\in\{0,1\}^{\lambda}$；$\mathrm{Open}(hk, x, i)\to(x_i, \rho)$，$|\rho| = \mathrm{poly}(\lambda)$；$\mathrm{Verify}(hk, v, i, b, \rho)\to\{0,1\}$，$\mathrm{poly}(\lambda)$ 時間。
- 正確性：$|x|\le 2^{\lambda}$ 時，誠實打開一定通過。
- 抗碰撞：$\Pr[A(hk)$ 找到 $v, i$ 和 $\rho_0, \rho_1$ 都通過$]\le\mathrm{negl}$。

### Kilian–Micali 協定（4 則訊息）

1. $V\to P$：$hk$。
2. $P\to V$：$v = \mathrm{Eval}(hk, \pi)$。
3. $V\to P$：PCP 查詢 $i_1, \ldots, i_{\ell}$（或直接送隨機數 $r$）。
4. $P\to V$：$(\pi_{i_j}, \rho_{i_j})$。
- 接受 ⟺ 所有 $\mathrm{Verify} = 1$ 且 $V_{\mathrm{PCP}} = 1$。
- 通訊 $\mathrm{poly}(\lambda)$；PCP soundness 要可忽略（重複 $\lambda$ 次）。
- 第 3 則可以是純隨機 → 之後能用 Fiat–Shamir。

### Soundness（第一個證明）

- 倒帶 $P^{*}$：同一個 $v$，$M = \mathrm{poly}(|\pi|, 1/\varepsilon)$ 組查詢。
- 有碰撞 → 破解雜湊。沒碰撞 → 拼出 $\hat{\pi}$（沒打開的填 0），$V_{\mathrm{PCP}}^{\hat{\pi}}$ 接受機率 $\approx\mathrm{poly}(\varepsilon)$，違反 PCP soundness。
- **漏洞**：要跑 $\mathrm{poly}(|\pi|)$ 時間，只在 $T(\lambda)\ge n$ 時成立。Barak–Goldreich 2002 修好。

### 安全參數

- $\lambda = n^{\varepsilon}$：多項式假設就夠。
- $\lambda = \mathrm{polylog}(n)$：需要次指數假設（$2^{\lambda^{\varepsilon}}$ 大小也找不到碰撞）。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Barak–Goldreich 的 soundness 證明 | 第 09 集 |
| 有局部打開的雜湊的構造（Merkle 樹） | 第 09 集 |
| 驗證者第 3 則訊息純隨機 | 第 10 集：Fiat–Shamir 把它變非互動 |
| 倒帶、後量子安全 | 之後談 Fiat–Shamir 安全性時 |
| 只承諾證據擴張＋互動 GKR | 實務上的 SNARK 做法 |

---

## 附：本集一句話總結

> **Kilian–Micali：證明者把 PCP 用「能局部打開」的抗碰撞雜湊壓成一個 $\lambda$ 位元的摘要，驗證者照 PCP 驗證者選幾個位置要他打開；作弊者若能騙過，就能被倒帶來找出碰撞或拼出一個會被接受的假 PCP——但這種拼法要跑 PCP 長度那麼久，下一集會看到不用拼的做法。**

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 5 Part 1 錄影逐字稿（MIT 真人字幕，1:44:35）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§9.2 整理。*
