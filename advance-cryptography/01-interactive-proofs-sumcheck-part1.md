---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 01
lecture: Lecture 1 (Part 1) – Interactive Proofs and the Sum-Check Protocol
date: 待補（2023 秋季第一堂課）
video: https://youtu.be/iqSMRO78UD0
notes: Thaler §2.2（書頁 16–17，PDF 頁 17–18）、§3.1–3.2（書頁 23–24，PDF 頁 24–25）、§3.4（書頁 28，PDF 頁 29）、§4.1（書頁 33–38，PDF 頁 34–39）
---

# 第 01 集 · Lecture 1 (Part 1)：互動式證明與 Sum-Check 協定 [▶ 影片](https://youtu.be/iqSMRO78UD0)

← 上一集：（無） ｜ [總目錄](PROGRESS.md) ｜ 下一集：[02-interactive-proofs-sumcheck-part2](02-interactive-proofs-sumcheck-part2.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 01 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（1:31:16，MIT 上傳的真人字幕）＋ Thaler《Proofs, Arguments, and Zero-Knowledge》§2.2、§3.1、§3.4、§4.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤
> - `⚠️ 待確認` 查不清楚的地方，列在最後的清單

> **注意**：這堂課是寫黑板的，影片看不到板書。下面的公式是照口述重建，並和 Thaler 書對過。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. NP：證明就是一份證據](#1-np證明就是一份證據)
- [2. 互動式證明的兩樣新東西](#2-互動式證明的兩樣新東西)
  - [2.1 為什麼一定要隨機](#21-為什麼一定要隨機)
  - [2.2 只有隨機、沒有對話：MA](#22-只有隨機沒有對話ma)
- [3. 例子：在 O(n²) 時間驗證矩陣乘法](#3-例子在-on²-時間驗證矩陣乘法)
  - [3.1 方法](#31-方法)
  - [3.2 為什麼對](#32-為什麼對)
  - [3.3 Q&A：Schwartz–Zippel、MA vs. NP、多項式恆等測試](#33-qaschwartzzippelma-vs-np多項式恆等測試)
- [4. 互動式證明的正式定義](#4-互動式證明的正式定義)
  - [4.1 為什麼常用 2/3 和 1/3](#41-為什麼常用-23-和-13)
  - [4.2 符號 ⟨P, V⟩(x) 的兩個意思](#42-符號-p-vx-的兩個意思)
- [5. IP 有多強：IP = PSPACE](#5-ip-有多強ip--pspace)
- [6. Sum-Check 協定](#6-sum-check-協定)
  - [6.1 要證什麼](#61-要證什麼)
  - [6.2 協定步驟](#62-協定步驟)
  - [6.3 最後一步：問 oracle](#63-最後一步問-oracle)
  - [6.4 Q&A：H 的選法、為什麼用多項式](#64-qah-的選法為什麼用多項式)
- [7. 成本](#7-成本)
- [8. Completeness 與 Soundness](#8-completeness-與-soundness)
  - [8.1 想法：某一輪要「從假變真」](#81-想法某一輪要從假變真)
  - [8.2 正式證明](#82-正式證明)
  - [8.3 Q&A：擴張體、上界是緊的](#83-qa擴張體上界是緊的)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:13](https://youtu.be/iqSMRO78UD0?t=13)

【口頭】講者一開始就說：這門課名字叫「進階密碼學」，但其實是一門講**證明（proof）在電腦科學裡怎麼演變**的課，從 1980 年代中期講到今天。沒學過密碼學也沒關係。

**課務**（[▶ 01:17](https://youtu.be/iqSMRO78UD0?t=77)）：

- 每週一次，下午 1 點到 4 點。共 11 次課。其中一次是 Oded Regev 的客座演講（10 月 6 日），一次是 crypto day，這兩次不用寫 scribe notes。
- 要求兩件事：(1) 每位學生幫一堂課寫 scribe notes（課堂筆記），可以兩人一組；(2) 學期中有一份作業（pset），不會太難。
- 建議每次上課前後讀網站上的讀物，主要是 Justin Thaler 的綜述《Proofs, Arguments, and Zero-Knowledge》。
  - ⚠️ 逐字稿缺字：字幕寫「Justin Taylor」，應為 **Justin Thaler**（就是本筆記用的課本作者）。

**課程地圖**（[▶ 03:49](https://youtu.be/iqSMRO78UD0?t=229)）：

| 階段 | 內容 | 有沒有用到密碼學 |
|---|---|---|
| 1 | 傳統的證明：一行一行寫，一行一行檢查 | 沒有 |
| 2 | 1985 年左右，Goldwasser、Micali、Rackoff 為了做**零知識證明**（zero-knowledge proof，證明一件事是真的、但不洩漏為什麼是真的），發明了**互動式證明**（interactive proof, IP） | 沒有 |
| 3 | 80、90 年代：驗證者要有效率（多項式時間），證明者可以無限強。證明者叫 **Merlin**（巫師，想做什麼都可以） | 沒有 |
| 4 | **雙重有效互動式證明**（doubly efficient interactive proof）：證明者也不能無限強，要在乎它的時間。GKR 協定 | 沒有 |
| 5 | GKR 的應用：PCP（probabilistically checkable proof，可機率檢查的證明）、MIP（multi-prover interactive proof，多證明者互動式證明）、重新證明 Shamir 的 IP = PSPACE | 沒有 |
| 6 | 用密碼學讓證明更**簡短**（succinct）。放棄「假的定理一定沒有證明」：假證明可能存在，但要找到它就得破解一個難題（例如分解大數、破解格問題） | 有 |
| 7 | **Fiat–Shamir 典範**：把互動拿掉。研究它什麼時候安全（MIT 的 Alex Lombardi 是證明它安全的人之一） | 有 |
| 8 | 用 Fiat–Shamir 做非互動的批次證明（batch proof，很多個命題只給一份短證明），最後做到 **SNARG**（succinct non-interactive argument，簡短非互動論證） | 有 |

【口頭】「論證」（argument）就是「只在計算上可靠的證明」（computationally sound proof）的另一個說法。

> 【課本補充】Thaler §3.2 Definition 3.2：argument system 是一種互動式證明，但 soundness 只要求對**多項式時間**的證明者成立。這叫 computational soundness；對無限強證明者都成立的叫 statistical soundness（統計可靠性）。

**本集範圍**：前半堂課。講 IP 的定義、一個隨機驗證的例子、sum-check 協定和它的分析。sum-check 的應用（#SAT ∈ IP）在第 02 集。

---

## 1. NP：證明就是一份證據

[▶ 09:31](https://youtu.be/iqSMRO78UD0?t=571)

這門課的框架是：**驗證者（verifier）很有效率（多項式時間）。我們能向它證明什麼？**

先看最熟悉的類別 **NP**（nondeterministic polynomial time，非決定性多項式時間）：

> **NP** = 所有「成員資格可以向多項式時間驗證者證明」的語言 $L$。
> 也就是：若 $x\in L$，存在一份證據（witness）$w$，驗證者用多項式時間檢查 $(x, w)$ 就能確定 $x\in L$；若 $x\notin L$，任何 $w$ 都騙不過它。

這裡的證明是**古典的證明**：一份寫好的字串，跑一個圖靈機（Turing machine）檢查就好。

【口頭】但 NP 「沒那麼豐富」。我們想要更多。

---

## 2. 互動式證明的兩樣新東西

[▶ 11:43](https://youtu.be/iqSMRO78UD0?t=703)

IP 和 NP 差兩件事：

1. **互動**（interaction）：證明者（prover）和驗證者可以來回對話。
2. **隨機**（randomization）：驗證者可以擲硬幣。

代價是：驗證者有一點點機會接受一個假的命題。但這個機會可以壓得很小，例如通訊量是 $n$ 時，可以壓到大約 $2^{-n}$。所以從這個角度看，模型是「變弱」了（不再保證 100% 不會被騙）。

### 2.1 為什麼一定要隨機

[▶ 13:06](https://youtu.be/iqSMRO78UD0?t=786)

如果驗證者是**決定性的**（deterministic，不擲硬幣），那證明者可以先算出驗證者每一步會問什麼，把整段對話（transcript）一次寫好，直接交出去當證明。這就只是 NP，互動沒有用。

所以 IP 的力量來自：

> **驗證者是隨機的，而且證明者事先不知道這些隨機性。**

【口頭】講者的比喻：我向你證明一件事。我先講第一句，但我不知道你接下來會問什麼隨機問題。我回答完，又不知道你下一題問什麼。如果我事先知道你所有的問題，這個模型就失去力量了。

### 2.2 只有隨機、沒有對話：MA

[▶ 14:41](https://youtu.be/iqSMRO78UD0?t=881)

反過來：只留隨機、拿掉互動，會不會比 NP 強？

這個類別叫 **MA**（Merlin–Arthur）：

- Merlin（證明者）送一則訊息。
- Arthur（驗證者，國王）擲硬幣，根據結果決定接受或拒絕。

【口頭】MA **可能**比 NP 強，但我們不知道。看起來是有多一點力量。下面這個例子之後也會用到。

---

## 3. 例子：在 O(n²) 時間驗證矩陣乘法

[▶ 16:14](https://youtu.be/iqSMRO78UD0?t=974)

**問題**：給三個 $n\times n$ 矩陣 $A, B, C$，元素在有限體（finite field）$\mathbb{F}$ 裡。要驗證 $C = AB$。

- 直接算 $AB$：已知最快的演算法大約是 $O(n^{2.37})$。
  - ⚠️ 逐字稿缺字：字幕寫「n to the 236」，講者說的是指數大約 2.36，學生提醒數字不太對，講者說「close」。【課本補充】Thaler §2.2.1 寫的是 $O(n^{2.37286})$。
- 用隨機：可以在 $O(n^2)$ 時間驗證。這已經是最好的了，因為光讀輸入就要 $n^2$。

### 3.1 方法

[▶ 17:49](https://youtu.be/iqSMRO78UD0?t=1069)

先假設 $|\mathbb{F}|\gg n$。如果不是，就把 $\mathbb{F}$ 放進一個更大的**擴張體**（extension field）裡算（見 [8.3](#83-qa擴張體上界是緊的)）。

1. 隨機選 $r\in\mathbb{F}$。
2. 令 $x = (1, r, r^2, \ldots, r^{n-1})^{T}$。
3. 【課堂討論】講者問「接下來做什麼？」學生答：檢查 $Cx$ 是不是等於 $ABx$。
   檢查 $Cx = A(Bx)$。相等就接受。

**時間**：矩陣乘向量是 $O(n^2)$。$A(Bx)$ 先算 $w = Bx$，再算 $Aw$，兩次都是 $O(n^2)$。產生 $x$ 只要 $O(n)$ 次乘法。

### 3.2 為什麼對

[▶ 19:44](https://youtu.be/iqSMRO78UD0?t=1184)

**Completeness（完備性）**：如果 $C = AB$，對任何 $x$ 都有 $Cx = ABx$，一定接受。

**Soundness（可靠性）**：

【課堂討論】講者問：如果 $C\neq AB$，你還能說服我嗎？學生答：把兩邊相減，看成 $r$ 的多項式；因為體比 $n$ 大很多，隨機一點剛好是根的機率很小。講者說「Fantastic」，接著寫得更正式：

令 $D = AB$。假設 $C\neq D$，那至少有一列（row）不同，假設是第 1 列。把這一列的元素當成多項式的係數：

$$p_{C_1}(X) = \sum_{i=0}^{n-1} C_{1,i}\, X^{i}, \qquad p_{D_1}(X) = \sum_{i=0}^{n-1} D_{1,i}\, X^{i}.$$

那麼 $(Cx)_1 = p_{C_1}(r)$，$(Dx)_1 = p_{D_1}(r)$。

$C_1\neq D_1$，所以 $p_{C_1}$ 和 $p_{D_1}$ 是**兩個不同的、次數 $\le n-1$ 的多項式**。

> **事實（單變數）**：兩個不同的、次數 $\le d$ 的單變數多項式最多在 $d$ 個點相等。
> 證明：它們的差是一個非零、次數 $\le d$ 的多項式，最多有 $d$ 個根。

所以

$$\Pr_{r}\left[ (Cx)_1 = (Dx)_1 \right] \le \frac{n-1}{|\mathbb{F}|}.$$

$|\mathbb{F}|$ 不夠大就換到更大的擴張體，讓這個機率變小。

> 【課本補充】Thaler §2.2 把這個方法叫 **Freivalds 演算法**（Freivalds' algorithm, 1977）。$(Cx)_i$ 就是第 $i$ 列的 **Reed–Solomon 指紋**（fingerprint）。Freivalds 原本用的是完全隨機的向量 $x\in\mathbb{F}^n$，Thaler 改用 $(1, r, \ldots, r^{n-1})$ 是為了套用指紋的分析。Thaler 也把它看成「第一個機率式證明系統」：證明就是答案 $C$ 本身，驗證者用 $O(n^2)$ 時間檢查。

### 3.3 Q&A：Schwartz–Zippel、MA vs. NP、多項式恆等測試

【Q&A】[▶ 23:25](https://youtu.be/iqSMRO78UD0?t=1405) **這是 Schwartz–Zippel 引理嗎？**
不是。Schwartz–Zippel 是類似的東西，但用在**多變數**多項式。這裡是**單變數**的情形。Schwartz–Zippel 就是這個事實的推廣，之後課上會用到。

> 【課本補充】Thaler §3.4 Lemma 3.3（Schwartz–Zippel）：$g:\mathbb{F}^m\to\mathbb{F}$ 是非零的 $m$ 變數多項式，**總次數**（total degree）$\le d$。對任何有限集合 $S\subseteq\mathbb{F}$，
> $$\Pr_{x\leftarrow S^m}\left[ g(x) = 0 \right] \le \frac{d}{|S|}.$$
> 所以兩個不同的、總次數 $\le d$ 的多變數多項式，最多在 $S^m$ 的 $d/|S|$ 比例的點上相等。

【口頭】[▶ 23:36](https://youtu.be/iqSMRO78UD0?t=1416) 講者順便說：課堂有錄影，網站已公開，所以影片也會公開；有人介意可以找她改成私人。

【Q&A】[▶ 24:59](https://youtu.be/iqSMRO78UD0?t=1499) **有沒有例子是「只有隨機、沒有互動」就能得到比多項式加速更多的東西？**
講者換個說法：這是在問 **MA 和 NP 是不是不一樣**。答案：不知道。

講者接著解釋 Arthur–Merlin 這一族類別（MA、MAM、……，字母可以一直加下去）：

- **M** = Merlin（證明者）說話。
- **A** = Arthur（驗證者）回應，用的是隨機性。
- MA 就是：Merlin 說一次話 → Arthur 擲硬幣 → 一個判定函數決定接受或拒絕。Merlin 不再說話。

學生追問：MA 的驗證者要是多項式時間嗎？答：是。

【Q&A】[▶ 26:21](https://youtu.be/iqSMRO78UD0?t=1581) **這其實就是多項式恆等測試（polynomial identity testing, PIT）吧？**
學生的意思：給一個低深度（例如 log 深度）的算術電路（arithmetic circuit），它的次數是多項式等級；要測它是不是恆等於 0，可以在大的擴張體上隨機取點測。講者同意。學生補充：我們不知道怎麼把它**去隨機化**（derandomize，改成不用隨機的演算法）；如果能，就會推出某些電路下界（circuit lower bound）。

接著有人說 PIT 其實不需要 Merlin，它在 **BPP** 裡（BPP = 用隨機、多項式時間、錯誤機率有界就能判定的問題，不需要證明者）。講者同意：「It's in BPP.」

另一位（講者稱他 Vinod）補充：講者剛剛講的（矩陣乘法驗證這類）基本上就是 MA 的典型問題，細節之後會講到。
- ⚠️ 逐字稿缺字：這段有多處 `[INAUDIBLE]`，Vinod 那句話的確切意思聽不清楚（見待確認清單）。

---

## 4. 互動式證明的正式定義

[▶ 28:16](https://youtu.be/iqSMRO78UD0?t=1696)

> **定義（Interactive Proof, IP）**：語言 $L$ 的互動式證明，是一個在
> - 可能無限強的證明者 $P$（要跑多久都可以），和
> - 多項式時間的驗證者 $V$
>
> 之間的協定。兩人都知道輸入 $x$；$V$ 有自己的秘密隨機性 $r$，$P$ 事先不知道。兩人來回對話產生對話紀錄（transcript）$\tau$，最後 $V$ 根據 $(x, r, \tau)$ 輸出 1（接受）或 0（拒絕）。協定要滿足：
>
> 1. **Completeness（完備性）參數 $c$**：對每個 $x\in L$，
> $$\Pr_{r}\left[ V(x, r, \tau) = 1 \right] \ge c, \quad \tau = \langle P, V(r)\rangle(x).$$
> 2. **Soundness（可靠性）參數 $s$**：對每個 $x\notin L$ 和**每個**（作弊的）證明者 $P^{*}$，
> $$\Pr_{r}\left[ V(x, r, \tau^{*}) = 1 \right] \le s, \quad \tau^{*} = \langle P^{*}, V(r)\rangle(x).$$

白話：在語言裡 → 高機率接受（$c$ 大）。不在語言裡 → 不管怎麼騙，都只有小機率接受（$s$ 小）。

- 【口頭】今天看到的協定，大多 $c = 1$（誠實時一定接受）。
- ⚠️ 逐字稿缺字：[▶ 32:12](https://youtu.be/iqSMRO78UD0?t=1932) 板書一開始少寫了「$x\in L$」，學生（Sally）提醒，講者補上。

> 【課本補充】Thaler §3.1 Definition 3.1 的寫法略有不同：
> - 用**錯誤**來寫：completeness error $\delta_c$、soundness error $\delta_s$，對應這裡的 $c = 1-\delta_c$、$s = \delta_s$。$\delta_c, \delta_s\le 1/3$ 叫 valid。
> - Thaler 是證明「函數值 $f(x) = y$」而不是「$x\in L$」：證明者一開始先送一個宣稱的答案 $y$。
> - Thaler 說可以只考慮**決定性**的證明者策略，不失一般性。
> - 回合數（round complexity）：交換 $k$ 則訊息時，回合數是 $\lceil k/2\rceil$。Thaler 也提醒文獻裡「round」的用法不一致。

### 4.1 為什麼常用 2/3 和 1/3

【Q&A】[▶ 33:53](https://youtu.be/iqSMRO78UD0?t=2033) **$s$ 和 $c$ 有限制嗎？是常數嗎？**

文獻常常不寫 $s$、$c$，預設 $c = 2/3$、$s = 1/3$。【口頭】這看起來很隨便，你應該覺得奇怪。

【課堂討論】講者問這些常數從哪來，學生答：可以重複執行協定。講者：「Exactly.」

**放大（amplification）**：只要 $c$ 和 $s$ 之間有差距，就可以：

1. 把協定**獨立重複 $n$ 次**。
2. 數接受的次數。超過 $\frac{c+s}{2}$ 比例（正中間）就接受，否則拒絕。

為什麼有效：

- $x\in L$ 時，每次接受的機率 $\ge 2/3$，期望約 2/3 的次數接受。
- $x\notin L$ 時，期望約 1/3 的次數接受。
- 重複夠多次，依大數法則（law of large numbers）接受比例會很集中在期望值附近，而且集中得很快。

結果：重複 $n$ 次後，completeness 變成約 $1-2^{-n}$，soundness 變成約 $2^{-n}$。所以通常不在乎這兩個常數，直接想成「在語言裡幾乎一定接受、不在語言裡幾乎一定拒絕」。

> 以下**不是逐字稿內容**，是依標準的 Chernoff 界推論的：講者說「very strong concentration」但沒寫出不等式。若每次接受的機率和門檻差 $\varepsilon = \frac{c-s}{2}$，重複 $n$ 次後多數決出錯的機率 $\le e^{-2\varepsilon^2 n}$（Hoeffding 不等式）。所以「約 $2^{-n}$」是「對 $n$ 指數小」的意思，底數會依 $c-s$ 而定。

### 4.2 符號 ⟨P, V⟩(x) 的兩個意思

[▶ 36:38](https://youtu.be/iqSMRO78UD0?t=2198)

$\langle P, V\rangle(x)$ 這個符號被**重複使用**：

- 有時代表**整段對話紀錄**。
- 有時代表驗證者最後的**接受／拒絕那一個位元**。

上課和讀文獻都會看到兩種用法，看上下文判斷。

---

## 5. IP 有多強：IP = PSPACE

[▶ 37:14](https://youtu.be/iqSMRO78UD0?t=2234)

> **定理（Shamir, 1992）**：$\mathrm{IP} = \mathrm{PSPACE}$。

**PSPACE** = 用多項式大小的**記憶體**就能判定的問題（時間可以是指數）。

意思是：任何 PSPACE 語言的成員資格，都可以向一個只跑多項式時間的驗證者證明。我們相信 PSPACE 比 NP 大很多（但也還沒證明）。所以 IP 被相信是比古典證明強很多的證明系統。

【口頭】[▶ 38:36](https://youtu.be/iqSMRO78UD0?t=2316) 講者覺得這是個很好的故事：

- 互動式證明一開始**只是為了零知識**而發明的。大家只想「藏住為什麼定理是真的」，沒人在想能不能證明更多語言。
- 後來大家發現：「誰管零知識，這個模型本身就很有趣。」
- 從傳統證明轉到「互動＋隨機」的世界，帶來很多漂亮的結果。這是第一次發現：向多項式時間驗證者能證明的東西，遠比古典證明多。

本課會在第 05 集用 GKR 重新證明 IP = PSPACE。

---

## 6. Sum-Check 協定

[▶ 40:27](https://youtu.be/iqSMRO78UD0?t=2427)

### 6.1 要證什麼

**設定**：

- 有限體 $\mathbb{F}$。
- 一個子集合 $H\subseteq\mathbb{F}$。可以想成 $H = \{0, 1\}$，也可以更大。
- 一個 $m$ 變數多項式 $f:\mathbb{F}^m\to\mathbb{F}$，**每個變數的次數 $\le d$**。
- 驗證者可以算 $f$：可能 $f$ 有很短的電路，或驗證者有 $f$ 的 **oracle**（神諭，一個黑盒子：丟一個點進去，馬上拿到 $f$ 在那點的值）。今天先假設有 oracle。

**宣稱**：

$$\sum_{(h_1, \ldots, h_m)\in H^m} f(h_1, \ldots, h_m) = \beta.$$

【口頭】[▶ 43:15](https://youtu.be/iqSMRO78UD0?t=2595) 「你們可能會想：我幹嘛在乎這個問題？」講者說：**這是證明系統文獻裡最重要的協定**。之後的每一樣東西都靠它。有了它，就能用黑盒的方式得到很多其他問題的互動式證明，包括所有 PSPACE。

> ⚠️ 逐字稿缺字：[▶ 44:01](https://youtu.be/iqSMRO78UD0?t=2641) 字幕寫「all 3D space」，依上下文（前面剛講 IP = PSPACE）應為「all **PSPACE**」。

> 【課本補充】Thaler 第 4 章開頭：sum-check 協定來自 Lund、Fortnow、Karloff、Nisan [LFKN92]，Thaler 稱它是設計有效互動式證明「最重要的一把鐵鎚」。Thaler §4.1 主要寫 $H = \{0, 1\}$ 的情形（Remark 4.1 說一般的 $B\subseteq\mathbb{F}$ 也可以）。

【Q&A】[▶ 44:28](https://youtu.be/iqSMRO78UD0?t=2668) **$H$ 是 $\mathbb{F}$ 的子集合，是一維的？**
對。例如 $H = \{0, 1\}$，或 $\{0, 1, 2\}$（如果 2 在體裡）。總和是對 $H^m$ 的 $|H|^m$ 個點加。

【Q&A】[▶ 44:51](https://youtu.be/iqSMRO78UD0?t=2691) **$h_1, h_2$ 可以相同嗎？**
可以。對所有組合加，包括 $(0, 0, \ldots, 0)$、$(0, \ldots, 0, 1)$ 等等。

【Q&A】[▶ 45:19](https://youtu.be/iqSMRO78UD0?t=2719) **「每個變數次數 $\le d$」是什麼意思？**
把 $f$ 寫成單項式（monomial）的和。在每個單項式裡，每個變數的次方都 $\le d$。

> 注意：這和 Schwartz–Zippel 用的「總次數」不同。例如 $x_1^{d}x_2^{d}$ 每個變數次數是 $d$，總次數是 $2d$。

### 6.2 協定步驟

[▶ 46:34](https://youtu.be/iqSMRO78UD0?t=2794)

**想法**：每一輪把一個變數「打開」，讓證明者送一個**單變數**多項式；驗證者隨機選一個點把這個變數固定住。每一輪少一個要加總的變數。

下面 $s_i$ 代表誠實時「應該送的」多項式，$g_i$ 是證明者實際送的（作弊時兩者可能不同）。

$$s_i(X) := \sum_{(h_{i+1}, \ldots, h_m)\in H^{m-i}} f(t_1, \ldots, t_{i-1}, X, h_{i+1}, \ldots, h_m).$$

**第 1 輪**

- $P\to V$：送 $g_1(X)$，宣稱等於 $s_1(X) = \sum_{h_2, \ldots, h_m\in H} f(X, h_2, \ldots, h_m)$。
- 【課堂討論】講者問 $g_1$ 是幾次，學生答 $d$。
- $V$ 檢查：
  1. $\deg g_1\le d$。【口頭】因為 $f$ 每個變數次數 $\le d$，誠實的 $g_1$ 一定 $\le d$ 次；超過就是在作弊，直接拒絕。
  2. 【課堂討論】講者問要檢查什麼，學生答 $\beta$：$\displaystyle\sum_{h\in H} g_1(h) = \beta$。
- 有一項不過就拒絕。都過的話，$V$ 隨機選 $t_1\leftarrow\mathbb{F}$ 送給 $P$。
  - 【口頭】$t_1$ 是從**整個大體** $\mathbb{F}$ 選，不是從 $H$ 選。體越大，soundness 越好。
  - $\leftarrow$ 是「隨機選取」的常用符號。

這一步把問題**化簡**成一個少一個變數的新宣稱：

$$\sum_{(h_2, \ldots, h_m)\in H^{m-1}} f(t_1, h_2, \ldots, h_m) = g_1(t_1).$$

**第 2 輪**

- $P\to V$：送 $g_2(X)$，宣稱等於 $s_2(X) = \sum_{h_3, \ldots, h_m} f(t_1, X, h_3, \ldots, h_m)$。
- $V$ 檢查：$\deg g_2\le d$，而且
  【課堂討論】學生答出：$\displaystyle\sum_{h\in H} g_2(h) = g_1(t_1)$。
- 都過就送隨機的 $t_2\leftarrow\mathbb{F}$。

**第 3 輪**

- 【課堂討論】講者問 $g_3$ 應該是什麼，學生答出：$g_3(X) = \sum_{h_4, \ldots, h_m} f(t_1, t_2, X, h_4, \ldots, h_m)$。
- $V$ 檢查 $\deg g_3\le d$，且 $\sum_{h\in H} g_3(h) = g_2(t_2)$。

**第 $i$ 輪**（一般式）

- $P$ 送 $g_i$；$V$ 檢查 $\deg g_i\le d$ 和 $\sum_{h\in H} g_i(h) = g_{i-1}(t_{i-1})$（第 1 輪的右邊是 $\beta$）；都過就送 $t_i\leftarrow\mathbb{F}$。

**第 $m$ 輪**

- $P$ 送 $g_m(X)$，宣稱等於 $f(t_1, \ldots, t_{m-1}, X)$（已經沒有東西要加了）。
- $V$ 照樣檢查次數和 $\sum_{h\in H} g_m(h) = g_{m-1}(t_{m-1})$。

### 6.3 最後一步：問 oracle

[▶ 59:27](https://youtu.be/iqSMRO78UD0?t=3567)

$V$ 選隨機的 $t_m\leftarrow\mathbb{F}$，用 oracle 查一次 $f$，檢查

$$g_m(t_m) = f(t_1, \ldots, t_m).$$

通過就接受。

【口頭】「我給你們一分鐘欣賞它的美，我先擦黑板。」

> 【課本補充】Thaler §4.1 有一個算到底的例子：$g(X_1, X_2, X_3) = 2X_1^3 + X_1X_3 + X_2X_3$，$H = \{0, 1\}$，總和是 12。
> - 第 1 輪：$s_1(X_1) = 8X_1^3 + 2X_1 + 1$，檢查 $s_1(0) + s_1(1) = 1 + 11 = 12$ ✓。
> - 取 $r_1 = 2$。第 2 輪：$s_2(X_2) = g(2, X_2, 0) + g(2, X_2, 1) = 16 + (16 + 2 + X_2) = 34 + X_2$，檢查 $s_2(0) + s_2(1) = 34 + 35 = 69 = s_1(2) = 64 + 4 + 1$ ✓。
> - 取 $r_2 = 3$。第 3 輪：$s_3(X_3) = g(2, 3, X_3) = 16 + 5X_3$，檢查 $16 + 21 = 37 = s_2(3)$ ✓。
> - 取 $r_3 = 6$，用一次 oracle 查詢確認 $s_3(6) = g(2, 3, 6)$。
>
> Thaler 也給了「遞迴」的看法：$V$ 自己算不動 $s_1(r_1)$（要加 $2^{v-1}$ 項），但 $s_1(r_1)$ 本身就是一個少一個變數的 sum-check 問題，所以遞迴地再跑一次 sum-check。

### 6.4 Q&A：H 的選法、為什麼用多項式

【Q&A】[▶ 60:31](https://youtu.be/iqSMRO78UD0?t=3631) **每個變數可以用不同的集合嗎？**
可以，協定裡沒有用到「每一維的 $H$ 都一樣」。可以對 $H_1\times\cdots\times H_m$ 加總。【口頭】看起來比較一般、好像會有用，但「不知為什麼我們總是用一樣的」。

【Q&A】[▶ 61:15](https://youtu.be/iqSMRO78UD0?t=3675) **$H$ 可以等於整個 $\mathbb{F}$ 嗎？**
可以。接著有學生問：那驗證者算 $\sum_{h\in H} g_1(h)$ 要花和 $|H|$ 成正比的時間？另一位說：那 soundness 也會壞掉？講者：先分析 soundness 再看。答案是：**只要 $d$ 小，soundness 不會變差**（見 [8.2](#82-正式證明)，soundness 和 $|H|$ 無關）。

【口頭】[▶ 62:04](https://youtu.be/iqSMRO78UD0?t=3724) 在**應用**裡，通常 $f$ 的每個變數次數剛好是 $|H|-1$（因為 $f$ 是用「低次擴張」做出來的）。這時 $|H|$ 大 → $d$ 大 → soundness 變差。但如果保證 $d$ 小，就沒問題。

【Q&A】[▶ 62:52](https://youtu.be/iqSMRO78UD0?t=3772) **多項式有什麼特別的？只是因為它們只在少數點相等、又能做加總嗎？還是背後有更一般的東西？**

講者的看法分兩層：

1. **多項式有糾錯（error correction）能力**。如果你作弊一次，協定會把你的作弊「放大」。只要你一直送低次多項式，你在某處作弊，就一定對應到在隨機點 $(t_1, \ldots, t_m)$ 上也是錯的。
   > 「多項式的美就在於：**錯了，就幾乎處處都錯**。」
   如果它不是正確的多項式，它和正確的多項式幾乎處處不同。多變數是 Schwartz–Zippel 引理；單變數講者說是「Lagrange 插值」。
2. **為什麼每天都是幸運日**：剛好有多項式的話很幸運，但為什麼多項式到處出現？因為可以把很多問題**嵌入成多項式**。這個技巧叫**低次擴張**（low-degree extension），下週會講：把問題延伸成低次多項式，再用 sum-check。

【Q&A】[▶ 65:35](https://youtu.be/iqSMRO78UD0?t=3935) **sum-check 能不能用在一般的糾錯碼上？還是需要多項式的代數結構？**
很好的問題。幾年前有一篇論文把 sum-check 推廣到更一般的碼，例如**張量碼**（tensor code）。不是任何碼都行，但比多項式更廣。一位學生（Rachel）補充說那篇用到碼的某種「乘法性質」。
> 【課本補充】作者名字在字幕裡是 `[INAUDIBLE]`。Thaler §3.5 註腳 34 說：互動式證明裡用的低次擴張，原則上可以換成**不是多項式**的「放大距離」編碼，並引用 [Mei13, RR19] 為這個方向的論文；[Mei13] 是 Or Meir〈IP = PSPACE using error-correcting codes〉（SIAM J. Comput. 2013）。講者說的應該就是這篇。（「就是這篇」是依 Thaler 的引用和講者的描述對起來的，Thaler 沒有提到張量碼。）

另一位學生問：「sum-check 對更一般的碼成立」是什麼意思？講者解釋：可以把 $f$ 本身看成一個糾錯碼的碼字（codeword）：

| 多項式種類 | 對應的糾錯碼 |
|---|---|
| 多變數多項式 | **Reed–Muller 碼** |
| 單變數多項式 | **Reed–Solomon 碼** |

所以 sum-check 可以看成是「針對 Reed–Muller 碼的協定」，然後可以問其他碼有沒有類似的協定。答案是有。

【Q&A】[▶ 67:38](https://youtu.be/iqSMRO78UD0?t=4058) **如果 $H = \mathbb{F}$，驗證者時間只和 $|H|$、$\log|\mathbb{F}|$ 有關，那協定還有意義嗎？**
有。$H$ 是整個 $\mathbb{F}$ 時，驗證者時間大約是 $|\mathbb{F}|$。但就算 $|\mathbb{F}|$ 是多項式大小，要直接算的總和有 $|\mathbb{F}|^m$ 項，還是很大。**難度不是來自 $\mathbb{F}$，是來自 $m$：對 $m$ 是指數的。**

【Q&A】[▶ 68:45](https://youtu.be/iqSMRO78UD0?t=4125) **那樣不是要再擴張 $\mathbb{F}$ 才有糾錯保證嗎？**
講者先說「對，需要再擴張」，但接著說：soundness 錯誤大約是 $d/|\mathbb{F}|$，$|H|$ 不會出現在裡面。直覺上應該隨 $|H|$ 變差，但其實不會。（真正的限制是 $d$ 要遠小於 $|\mathbb{F}|$。）

---

## 7. 成本

[▶ 69:33](https://youtu.be/iqSMRO78UD0?t=4173)

先做「健全性檢查」：通訊量、執行時間。

| 項目 | 講者的分析 | 理由 |
|---|---|---|
| 回合數 | $O(m)$ | 每一輪拿掉一個變數 |
| 通訊量 | $O(m\cdot d\cdot\log|\mathbb{F}|)$ 位元 | 每輪一個 $d$ 次多項式（$d+1$ 個體元素）＋一個體元素 |
| 驗證者時間 | $O(m\cdot d\cdot|H|\cdot\mathrm{polylog}|\mathbb{F}|)$ ＋ 一次 oracle 查詢 | 每輪要在 $|H|$ 個點上算一個 $d$ 次多項式再加起來 |
| 證明者時間 | 約 $|H|^m\cdot T_f\cdot m\cdot\mathrm{polylog}|\mathbb{F}|$ | 要真的去算那些加總；$T_f$ = 算一次 $f$ 的時間 |

說明：

- 【口頭】這門課（和這個領域）通常把體的加法、乘法當成 $O(1)$。實際上是 $\mathrm{polylog}|\mathbb{F}|$，但「我們不想追這些 polylog 項」。讀 Thaler 時也常看不到這一項。
- 【Q&A】[▶ 71:42](https://youtu.be/iqSMRO78UD0?t=4302) 學生指出驗證者時間要算上 $\sum_{h\in H}$ 的 $|H|$ 次運算。講者一開始漏了 $|H|$，學生提醒後補上（「Good catch」）。
- 【Q&A】[▶ 50:38](https://youtu.be/iqSMRO78UD0?t=3038)（在講協定時就問了）**說驗證者是多項式時間，是對什麼的多項式？** 對變數個數 $m$、次數 $d$；嚴格說還有 $|H|$（學生 Surya 補充）和 $\log|\mathbb{F}|$。因為驗證者用 oracle 拿 $f$，「多項式時間」在這裡不太好定義；到應用時會看到它就對應到多項式時間。
- ⚠️ 逐字稿缺字：[▶ 73:11](https://youtu.be/iqSMRO78UD0?t=4391) 字幕寫證明者跑「h to the f」時間，依上下文應為 $|H|^m$。證明者時間的完整寫法是照口述重建的（見待確認清單）。
- 【Q&A】[▶ 75:35](https://youtu.be/iqSMRO78UD0?t=4535) 證明者算 $g_1$ 時要合併 $O(d)$ 項，有算進去嗎？講者：$|\mathbb{F}|$ 遠大於 $d$，所以被吸收了。

【Q&A】[▶ 74:01](https://youtu.be/iqSMRO78UD0?t=4441) **驗證者既然有 $f$ 的 oracle，為什麼還需要證明者？**
就算可以隨意查 $f$，要自己算總和就得查 $|H|^m$ 次。$m$ 很大時（就算 $|H| = 2$），這是指數的。

【Q&A】[▶ 74:46](https://youtu.be/iqSMRO78UD0?t=4486) **$f$ 的描述要想成多項式大小嗎？**
兩種看法都行：(1) $f$ 有多項式大小的電路，可以算；(2) $f$ 可以很大，但驗證者有一個可信的 oracle 幫它算。

【Q&A】[▶ 77:11](https://youtu.be/iqSMRO78UD0?t=4631) **為什麼不能直接把 $f$ 整個送過去？**
$m$ 個變數、每個變數次數 $d$ 的多項式，係數可以多達 $(d+1)^m$ 個，太大了。
- ⚠️ 逐字稿缺字：講者先說「m to the d」，馬上改口「d to the m, sorry」。

> 【課本補充】Thaler Table 4.1（$H = \{0, 1\}$、$v$ 個變數、$T$ = 一次查詢 $g$ 的成本）：
> - 通訊：$O\left(\sum_i \deg_i(g)\right)$ 個體元素；回合：$v$。
> - 驗證者：$O\left(v + \sum_i \deg_i(g)\right) + T$。
> - 證明者：$O\left(\sum_i \deg_i(g)\cdot 2^{v-i}\cdot T\right)$，若每個 $\deg_i(g) = O(1)$ 就是 $O(2^v\cdot T)$。
>
> 證明者的時間比講者粗估的 $m\cdot 2^m$ 好：第 $j$ 輪要算的項數是 $(1+\deg_j)\cdot 2^{v-j}$，**隨 $j$ 幾何遞減**，加起來是 $O(2^v)$。只比「直接算總和、不證明」多一個常數倍。

> 【課本補充】Thaler Remark 4.2：驗證者送的訊息只是隨機體元素，和 $f$ 本身無關。驗證者只需要知道每個變數的次數上界，和最後能在一個隨機點上算 $f$。這點在之後的應用（$V$ 沒有 oracle、改由證明者再證明 $f(t_1, \ldots, t_m)$）很重要。

---

## 8. Completeness 與 Soundness

[▶ 77:37](https://youtu.be/iqSMRO78UD0?t=4657)

**Completeness = 1**：【課堂討論】講者問誠實時接受機率是多少，學生答 1。誠實的證明者每一輪都送正確的 $s_i$，次數對、總和對、最後和 oracle 一致，一定接受。

**Soundness**：難的部分在這裡。

> **定理（sum-check 的 soundness）**：若 $\sum_{h\in H^m} f(h)\neq\beta$，則對任何作弊的證明者 $P^{*}$，
> $$\Pr\left[ V \text{ 接受} \right] \le \frac{m\cdot d}{|\mathbb{F}|}.$$

### 8.1 想法：某一輪要「從假變真」

[▶ 79:05](https://youtu.be/iqSMRO78UD0?t=4745)

固定一個假的宣稱（真正的總和 $\neq\beta$），固定任何 $P^{*}$。

1. **一開始一定是假的**：如果 $V$ 接受，第 1 輪的檢查 $\sum_h g_1(h) = \beta$ 一定過了。但真正的 $s_1$ 加起來是真正的總和，不是 $\beta$。所以 $g_1\neq s_1$。
   > 白話：作弊的證明者第一句話就一定在說謊。
2. **最後一定是真的**：最後一步是拿 $g_m(t_m)$ 和**真的** $f$（oracle）比。要通過，最後必須和真相一致。
3. 所以協定中間，一定有某一輪**從「假的 $g$」變成「真的 $g$」**。

接下來要證明：每一輪「從假變真」的機率都很小。

講者的口語版：$g_1$ 是假的。那 $g_2$ 要不是真的（機率很小），就還是假的。$g_2$ 假的話，$g_3$ 要不是真的（機率很小），就還是假的……一路到 $g_m$。如果 $g_m$ 還是假的（$g_m\neq f(t_1, \ldots, t_{m-1}, \cdot)$），那對隨機的 $t_m$，$g_m(t_m)$ 剛好等於 $f(t_1, \ldots, t_m)$ 的機率最多 $d/|\mathbb{F}|$，因為兩個不同的 $d$ 次多項式最多在 $d$ 個點相等。

### 8.2 正式證明

[▶ 82:55](https://youtu.be/iqSMRO78UD0?t=4975)

**定義壞事件**。講者的寫法：

$$B_i := \text{「} g_i\neq s_i \text{ 但 } g_{i+1} = s_{i+1} \text{」}.$$

（最後一輪把「$g_{m+1}$ 是真的」理解成「最後的 oracle 檢查通過」。）

**Step 1：$V$ 接受 ⟹ 某個 $B_i$ 發生。**
由 8.1，$g_1$ 是假的、最後是真的，所以一定有第一個 $i$ 使得 $g_i$ 假、下一個真。

**Step 2：$\Pr[B_i]\le d/|\mathbb{F}|$。**

- 固定 $t_1, \ldots, t_{i-1}$（不管怎麼選的）。這決定了作弊證明者送的 $g_i$，也決定了真正的 $s_i$。
  - ⚠️ 逐字稿缺字：[▶ 84:20](https://youtu.be/iqSMRO78UD0?t=5060) 字幕寫「t1 up to ti plus 1」，依上下文應是 $t_1, \ldots, t_{i-1}$（$g_i$ 在 $t_i$ 選之前就送出了）。
- 現在 $V$ 隨機選 $t_i$。因為 $V$ 接受，第 $i+1$ 輪的檢查通過：$\sum_{h} g_{i+1}(h) = g_i(t_i)$。
- 如果 $g_{i+1} = s_{i+1}$（真的），那 $\sum_h s_{i+1}(h) = s_i(t_i)$（這是 $s$ 的定義）。所以 $g_i(t_i) = s_i(t_i)$。
- 但 $g_i\neq s_i$，兩個都是次數 $\le d$ 的單變數多項式，而且都在 $t_i$ 選之前就固定了。它們最多在 $d$ 個點相等：
$$\Pr_{t_i\leftarrow\mathbb{F}}\left[ g_i(t_i) = s_i(t_i) \right] \le \frac{d}{|\mathbb{F}|}.$$

**Step 3：Union bound（聯集界）。**
把每一輪的機率加起來：

$$\Pr\left[ V \text{ 接受} \right] \le \Pr\left[ \exists i:\ B_i \right] \le \sum_{i=1}^{m}\Pr[B_i] \le \frac{m\cdot d}{|\mathbb{F}|}.$$

**重點**：

- **$|H|$ 完全沒有出現在 soundness 裡。**
- soundness 只要求 $m\cdot d\ll|\mathbb{F}|$。

> 【課本補充】Thaler Proposition 4.1 的「非歸納證明」寫法比較直接：作弊要成功，一定有某一輪 $i$ 送了 $g_i\neq s_i$，而 $g_i(r_i) = s_i(r_i)$。每一輪這件事的機率 $\le d/|\mathbb{F}|$，union bound 得 $dv/|\mathbb{F}|$。這和講者的 $B_i$ 是同一件事：Step 2 就是在說「$B_i$ 發生 ⟹ $g_i\neq s_i$ 且 $g_i(t_i) = s_i(t_i)$」。
>
> Thaler 還給了**歸納證明**：對變數個數 $v$ 歸納。$v = 1$ 時直接是單變數的事實。$v\ge 2$ 時，若 $g_1\neq s_1$，則 $g_1(r_1) = s_1(r_1)$ 的機率 $\le d/|\mathbb{F}|$；否則證明者剩下要證一個假的 $(v-1)$ 變數宣稱，由歸納假設被拒絕的機率 $\ge 1 - d(v-1)/|\mathbb{F}|$。合起來拒絕機率 $\ge 1 - d/|\mathbb{F}| - d(v-1)/|\mathbb{F}| = 1 - dv/|\mathbb{F}|$。

### 8.3 Q&A：擴張體、上界是緊的

【Q&A】[▶ 87:16](https://youtu.be/iqSMRO78UD0?t=5236) **所以重點是：選你在乎的 $d$ 和 $H$，然後把體開得很大？**
對。如果 $|\mathbb{F}|$ 沒有遠大於 $m\cdot d$，就用擴張體人為地把它變大，讓 soundness 錯誤變小。
- ⚠️ 逐字稿缺字：[▶ 87:29](https://youtu.be/iqSMRO78UD0?t=5249) 字幕寫「m to the m times d」，依剛寫的上界 $md/|\mathbb{F}|$，應為「$m$ times $d$」。

另一位學生補充（講者說「100%」並複述）：一般的 sum-check 可以用任何 $H$，甚至 $H = \mathbb{F}$（只要 $d$ 小）。但在應用裡，$d$ 通常就等於 $|H|$（或 $|H|-1$），因為低次擴張會讓次數跟著 $|H|$ 走。這時若 $H = \mathbb{F}$，$d/|\mathbb{F}|$ 接近 1，就沒意義了。所以**應用裡 $H$ 很小**，再把 $\mathbb{F}$ 開大，兩者分開。

【Q&A】[▶ 88:57](https://youtu.be/iqSMRO78UD0?t=5337) **任何有限體都能放進更大的體嗎？**
可以，這是數學上的事實。大致說：可以把 $\mathbb{F}$ 嵌入一個大小 $|\mathbb{F}|^{n}$ 的體，$n$ 要多大都行。這叫擴張體。$\mathbb{F}$ 是它的子體（subfield），$\mathbb{F}$ 裡的運算和原本完全一樣，所以不會破壞總和之類的東西。

> 以下**不是逐字稿內容**，是依有限體的標準事實補充的：$\mathbb{F}_q$ 的 $k$ 次擴張是 $\mathbb{F}_{q^k}\cong\mathbb{F}_q[X]/(p(X))$，其中 $p$ 是 $\mathbb{F}_q$ 上一個 $k$ 次不可約多項式。$f$ 的係數都在 $\mathbb{F}_q$ 裡，所以 $f$ 也可以看成 $\mathbb{F}_{q^k}$ 上的多項式，$H\subseteq\mathbb{F}_q$ 上的總和不變；只是驗證者改從 $\mathbb{F}_{q^k}$ 選 $t_i$。

【Q&A】[▶ 89:48](https://youtu.be/iqSMRO78UD0?t=5388) **這個上界是緊的嗎？真的有作弊策略能達到這個機率？**
是，這個分析很緊。作弊的證明者可以「祈禱」：送一個錯的 $g_i$，但讓它和真的 $s_i$ 剛好在 $d$ 個點相等（兩個 $d$ 次多項式可以在 $d$ 個點相等）。如果 $V$ 選的 $t_i$ 剛好落在這 $d$ 個點之一，作弊者就「轉正」了，之後一路送真的多項式，進入「la-la land」，最後通過。每一輪這樣的機會是 $d/|\mathbb{F}|$，union bound 起來是 $md/|\mathbb{F}|$。$|\mathbb{F}|\gg md$ 時，作弊成功的機率很小。

[▶ 91:05](https://youtu.be/iqSMRO78UD0?t=5465) 休息五分鐘，之後講 sum-check 的應用（第 02 集）。

---

## 9. 一頁速查表

### 複雜度類別

| 類別 | 證明者 | 驗證者 | 互動 |
|---|---|---|---|
| NP | 送一份證據 $w$ | 決定性、多項式時間 | 無 |
| BPP | 無 | 隨機、多項式時間 | 無 |
| MA | Merlin 送一則訊息 | Arthur 隨機、多項式時間 | 一則訊息 |
| IP | 無限強 | 隨機、多項式時間，**隨機性對證明者保密** | 多輪 |

- **決定性的 IP = NP**。關鍵一步：證明者能預測驗證者每一步，直接把整段對話寫成證據。
- **IP = PSPACE**（Shamir 1992）。

### IP 的定義

- Completeness $c$：$x\in L\Rightarrow\Pr[\text{接受}]\ge c$。
- Soundness $s$：$x\notin L$，對所有 $P^{*}$，$\Pr[\text{接受}]\le s$。
- 慣例 $c = 2/3$、$s = 1/3$。**放大**：重複 $n$ 次，接受比例超過 $\frac{c+s}{2}$ 才接受。關鍵一步：大數法則／集中不等式，錯誤對 $n$ 指數下降。

### 多項式的關鍵事實

- **單變數**：兩個不同的、次數 $\le d$ 的多項式最多在 $d$ 點相等。關鍵一步：差是非零 $d$ 次多項式，最多 $d$ 個根。
- **Schwartz–Zippel**（多變數，總次數 $\le d$）：$\Pr_{x\leftarrow S^m}[g(x) = 0]\le d/|S|$。

### Freivalds：驗證 $C = AB$

- 選 $r\leftarrow\mathbb{F}$，$x = (1, r, \ldots, r^{n-1})$，檢查 $Cx = A(Bx)$。時間 $O(n^2)$。
- 錯誤機率 $\le (n-1)/|\mathbb{F}|$。關鍵一步：$(Cx)_i = p_{C_i}(r)$，$C_i\neq D_i$ 時是兩個不同的 $n-1$ 次多項式。

### Sum-check 協定

宣稱 $\sum_{h\in H^m} f(h) = \beta$，$f$ 每個變數次數 $\le d$。令 $g_0(t_0) := \beta$。

第 $i = 1, \ldots, m$ 輪：
1. $P$ 送 $g_i(X)$（誠實值 $s_i(X) = \sum_{h_{i+1}, \ldots, h_m\in H} f(t_1, \ldots, t_{i-1}, X, h_{i+1}, \ldots, h_m)$）。
2. $V$ 檢查 $\deg g_i\le d$ 且 $\sum_{h\in H} g_i(h) = g_{i-1}(t_{i-1})$。
3. $V$ 送 $t_i\leftarrow\mathbb{F}$。

最後：$V$ 查 oracle，檢查 $g_m(t_m) = f(t_1, \ldots, t_m)$。

| | |
|---|---|
| 回合 | $O(m)$ |
| 通訊 | $O(md\log|\mathbb{F}|)$ |
| 驗證者 | $O(md|H|)$ 次體運算 ＋ 1 次 oracle |
| 證明者 | 約 $|H|^m\cdot T_f$（Thaler：$H=\{0,1\}$、$d = O(1)$ 時是 $O(2^m T)$） |
| Completeness | 1 |
| Soundness | $\le md/|\mathbb{F}|$，**和 $|H|$ 無關** |

**Soundness 關鍵一步**：$g_1$ 一定假、最後一定真 ⟹ 某輪 $i$ 有 $g_i\neq s_i$ 但 $g_i(t_i) = s_i(t_i)$。$g_i$ 在 $t_i$ 之前就固定，所以這件事機率 $\le d/|\mathbb{F}|$；對 $m$ 輪 union bound。

**上界是緊的**：作弊者讓錯的 $g_i$ 和 $s_i$ 在 $d$ 點相等，賭 $t_i$ 落在那裡。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Sum-check 協定 | 第 02 集：#SAT ∈ IP（Thaler §4.2）；第 03–05 集：GKR 協定的核心子程序 |
| 低次擴張（low-degree extension） | 第 02–03 集：把問題嵌入成多項式再跑 sum-check（Thaler §3.5） |
| IP = PSPACE | 第 05 集：用 GKR 重新證明 |
| 雙重有效互動式證明 | 第 03–04 集 |
| 單變數／Schwartz–Zippel 的「錯了就幾乎處處錯」 | 整門課的 soundness 分析 |
| Argument（計算可靠的證明） | 第 06–09 集：Kilian–Micali、Fiat–Shamir |
| Freivalds 演算法（MA 的典型例子） | 講者說「之後會用到」，⚠️ 待確認在哪一集 |

---

## 附：本集一句話總結

> **互動式證明的力量來自「驗證者隨機、證明者猜不到」。Sum-check 協定每輪把一個變數換成隨機點，用 $m$ 輪把一個 $|H|^m$ 項的總和化簡成 $f$ 在一個點的值；作弊者只能靠隨機點剛好落在兩個多項式的交點上，機率 $\le md/|\mathbb{F}|$。**

---

## ⚠️ 待確認清單

1. [▶ 27:55](https://youtu.be/iqSMRO78UD0?t=1675) Vinod 對 PIT／MA 的補充有多處 `[INAUDIBLE]`，確切說法聽不清楚。筆記只寫了「矩陣乘法驗證是 MA 的典型問題」這個大意。
2. [▶ 73:08](https://youtu.be/iqSMRO78UD0?t=4388) 證明者時間的板書看不到。字幕是「h to the f」「T sub f」「M polylog F」，筆記重建成 $|H|^m\cdot T_f\cdot m\cdot\mathrm{polylog}|\mathbb{F}|$，確切形式待確認。
3. [▶ 16:14](https://youtu.be/iqSMRO78UD0?t=974) 講者說矩陣乘法驗證這個例子「之後會用到」，還不知道是哪一集。

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 1 Part 1 錄影逐字稿（MIT 真人字幕，1:31:16）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§2.2、§3.1、§3.2、§3.4、§4.1 整理。*
