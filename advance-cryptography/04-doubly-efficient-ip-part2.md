---
course: Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）
episode: 04
lecture: Lecture 2 (Part 2) – Doubly Efficient Interactive Proofs
date: 待補（2023 秋季第二堂課，後段）
video: https://youtu.be/Ob1fFHAXlJQ
notes: Thaler §4.6.4–4.6.5（書頁 59–64，PDF 頁 60–65）
---

# 第 04 集 · Lecture 2 (Part 2)：GKR 協定（下）——兩個宣稱、平行 sum-check、soundness [▶ 影片](https://youtu.be/Ob1fFHAXlJQ)

← 上一集：[03-doubly-efficient-ip-part1](03-doubly-efficient-ip-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[05-gkr-continuation-ip-pspace](05-gkr-continuation-ip-pspace.md) →

> **課程**：Advanced Topics in Cryptography（6.5630），MIT，Fall 2023 — 第 04 集
> **講者**：Yael Tauman Kalai
> **來源**：YouTube 錄影逐字稿（42:30，MIT 上傳的真人字幕）＋ Thaler §4.6
> **標記說明**：
> - `【口頭】` 講者口頭補充，Thaler 書上沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` Thaler 書上有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯、掉字，或講者口誤

> **注意**：黑板內容看不到，公式照口述重建，符號沿用第 03 集筆記（固定點 $z^{*}$、驗證者隨機數 $r_0, r_1, r_2$）。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：一層 sum-check 之後](#1-回顧一層-sum-check-之後)
- [2. 解法：兩個 sum-check 用同一組隨機數](#2-解法兩個-sum-check-用同一組隨機數)
- [3. 完整的 GKR 協定](#3-完整的-gkr-協定)
- [4. 成本](#4-成本)
- [5. Soundness](#5-soundness)
  - [5.1 證明](#51-證明)
  - [5.2 用同一組隨機數為什麼沒事](#52-用同一組隨機數為什麼沒事)
- [6. 輸入層與其他 Q&A](#6-輸入層與其他-qa)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:13](https://youtu.be/Ob1fFHAXlJQ?t=13)

**課務**：scribe 的報名表很快就滿了。修學分但沒報到的人來找講者，可以兩人合寫，或做 scribe 相關的其他工作。

**本集**：解決第 03 集留下的問題（一個宣稱變成兩個），寫出完整的 GKR 協定，分析成本和 soundness。

---

## 1. 回顧：一層 sum-check 之後

[▶ 00:59](https://youtu.be/Ob1fFHAXlJQ?t=59)

講者先重講一次（因為下課時有人問）。

定義第 $i$ 層、固定點 $z^{*}$ 的多項式：

$$f_{i, z^{*}}(p, w_1, w_2) := \tilde{\chi}(p, z^{*})\left[ \widetilde{\mathrm{add}}_i(p, w_1, w_2)\left( \tilde{V}_{i+1}(w_1) + \tilde{V}_{i+1}(w_2) \right) + \widetilde{\mathrm{mult}}_i(p, w_1, w_2)\,\tilde{V}_{i+1}(w_1)\,\tilde{V}_{i+1}(w_2) \right].$$

證明者宣稱 $\tilde{V}_i(z^{*}) = v_i^{*}$，等價於宣稱

$$v_i^{*} = \sum_{p, w_1, w_2\in H^m} f_{i, z^{*}}(p, w_1, w_2).$$

- 把 sum-check 當**黑盒**用。不用記細節，只要記得：過程中驗證者**只送隨機數**，不需要知道 $f$；只有最後要檢查 $f(r_0, r_1, r_2) = \gamma$。
- 驗證者能算 $\tilde{\chi}$；（假設）能查 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$；算不出 $\tilde{V}_{i+1}(r_1)$、$\tilde{V}_{i+1}(r_2)$。
- 叫證明者報這兩個值。由 sum-check 的 soundness，$\gamma$ 高機率是錯的；證明者報真值就會被抓，所以**至少一個要說謊**。
- 結果：第 $i$ 層一個宣稱 → 第 $i+1$ 層兩個宣稱。

---

## 2. 解法：兩個 sum-check 用同一組隨機數

[▶ 06:33](https://youtu.be/Ob1fFHAXlJQ?t=393)

【口頭】GKR 原論文是用另一個子協定把「兩個宣稱變一個」。但有個簡單得多的想法：**什麼都不用做**，「其實這不是問題」。

- 講者一開始說是 Rachel 的想法，Rachel 在台下更正：「不是我，是 Lisa 的。」

**想法**：就帶著兩個宣稱繼續往下。不會變成 4 個、8 個，而是**一直保持 2 個**。

第 $i+1$ 層有兩個宣稱：

$$v_{i+1,1}^{*} = \sum_{p, w_1, w_2} f_{i+1, z_1^{*}}(p, w_1, w_2), \qquad v_{i+1,2}^{*} = \sum_{p, w_1, w_2} f_{i+1, z_2^{*}}(p, w_1, w_2),$$

其中 $z_1^{*} := r_1$、$z_2^{*} := r_2$ 是上一層驗證者選的點（現在固定了，加星號）。注意這是**兩個不同的函數**（固定點不同）。

**關鍵**：這兩個 sum-check **平行跑，而且驗證者用同一組隨機數**。

結束時，驗證者要檢查：

$$f_{i+1, z_1^{*}}(r_0', r_1', r_2') = \gamma_1, \qquad f_{i+1, z_2^{*}}(r_0', r_1', r_2') = \gamma_2,$$

$(r_0', r_1', r_2')$ 是這一層新的隨機數。兩個式子裡需要證明者幫忙的部分是

$$\tilde{V}_{i+2}(r_1') \quad\text{和}\quad \tilde{V}_{i+2}(r_2'),$$

**兩式用的是同樣兩個點**！$\tilde{\chi}(r_0', z_1^{*})$、$\tilde{\chi}(r_0', z_2^{*})$ 不同，但驗證者自己會算。

所以證明者只要報 2 個值。「開始時兩個，結束時兩個。就這樣。」

【Q&A】[▶ 17:48](https://youtu.be/Ob1fFHAXlJQ?t=1068) Gabe：**兩個 sum-check 要交錯進行吧？**
對，一定要**平行**：每一輪兩個 sum-check 都送完單變數多項式，驗證者才公開那一輪的隨機數。如果循序做，跑第二個時證明者已經知道硬幣了，就能作弊（見第 02 集：知道 $t_1$ 就能作弊）。

【Q&A】[▶ 19:53](https://youtu.be/Ob1fFHAXlJQ?t=1193) **同一組隨機數是指同一層的兩個 sum-check 之間？**
對。不同層的隨機數是重新選的。

> 【課本補充】Thaler §4.6.4 用的是另一種方法（「Reducing to Verification of a Single Point」）：取通過 $b^{*}$、$c^{*}$ 的唯一直線 $\ell:\mathbb{F}\to\mathbb{F}^{k_{i+1}}$，$\ell(0) = b^{*}$、$\ell(1) = c^{*}$。證明者送 $\tilde{W}_{i+1}\circ\ell$（一個單變數多項式 $q$，次數 $\le k_{i+1}$）。驗證者用 $q(0)$、$q(1)$ 當兩個值做檢查，再取隨機 $r^{*}$，新宣稱是 $\tilde{W}_{i+1}(\ell(r^{*})) = q(r^{*})$。這樣每層只有一個宣稱。講者的方法不需要這一步，但需要 sum-check 有「最後只查驗證者自己選的一個點」的性質（見 5.2）。

---

## 3. 完整的 GKR 協定

[▶ 17:07](https://youtu.be/Ob1fFHAXlJQ?t=1027)

**輸入**：分層算術電路 $C$（深度 $d$），輸入 $x$。證明者宣稱 $C(x) = v_0^{*}$。

1. **第 0 層**：宣稱 $\tilde{V}_0(z_0) = v_0^{*}$（$z_0$ 是輸出閘）。跑 sum-check（形式上是兩個一樣的，等於一個）。
2. **第 $i$ 層**（$i = 0, \ldots, d-1$）：手上有兩個宣稱 $\tilde{V}_i(z_1^{*}) = v_{i,1}^{*}$、$\tilde{V}_i(z_2^{*}) = v_{i,2}^{*}$。
   - 對 $f_{i, z_1^{*}}$ 和 $f_{i, z_2^{*}}$ **平行**跑 sum-check，驗證者用**同一組**新隨機數 $(r_0, r_1, r_2)$。
   - 證明者報 $v_{i+1,1}^{*} := \tilde{V}_{i+1}(r_1)$、$v_{i+1,2}^{*} := \tilde{V}_{i+1}(r_2)$。
   - 驗證者用這兩個值、自己算的 $\tilde{\chi}$、查到的 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$，檢查兩個 sum-check 的最後一步。
   - 新的固定點 $z_1^{*} := r_1$、$z_2^{*} := r_2$，進入第 $i+1$ 層。
3. **輸入層**：最後的兩個宣稱是 $\tilde{V}_d(z_1^{*}) = v_{d,1}^{*}$、$\tilde{V}_d(z_2^{*}) = v_{d,2}^{*}$。$\tilde{V}_d$ 就是輸入 $x$ 的低次擴張，驗證者**自己算**（見第 6 節）。

【口頭】「所以 GKR 協定是什麼？就是 $d$ 對平行的 sum-check。中間證明者給一些 $\tilde{V}$ 的值幫忙。就這樣。」

---

## 4. 成本

[▶ 21:17](https://youtu.be/Ob1fFHAXlJQ?t=1277)

**Completeness**：照抄 sum-check 的 completeness，誠實就一定通過，是 1。

**通訊**：$d$ 對 sum-check。每個 sum-check 的通訊是（變數數）×（次數）×$\log|\mathbb{F}|$：

- 變數數 $3m = O\left( \frac{\log S}{\log\log S} \right)$，次數 $O(|H|) = O(\log S)$，都是 $\mathrm{polylog}(S)$。
- $\log|\mathbb{F}|$ 取成 $\mathrm{polylog}(S)$。

所以通訊 $= d\cdot\mathrm{polylog}(S)$。

- ⚠️ 逐字稿缺字：[▶ 21:59](https://youtu.be/Ob1fFHAXlJQ?t=1319) 講者先說「$\mathbb{F}$ 取 polylog $S$」，又改成「poly $S$」，最後說「$\log|\mathbb{F}|$ 是 polylog $S$」。結論是 $\log|\mathbb{F}| = \mathrm{polylog}(S)$。

**驗證者**：跑 sum-check 的部分（送隨機數、做簡單檢查），加上每層收兩個值、做一個代數檢查（假設能查 $\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$），加上最後算輸入的擴張。總共 $d\cdot\mathrm{polylog}(S)$ ＋ $\tilde{O}(n)$。

**證明者**：$2d$ 個 sum-check，每個大約 $m\cdot|H|^m\cdot$（算一次 $f$ 的時間）。$|H|^m = S$；算一次 $f$ 要算擴張，每個擴張是 $|H|^m$ 項的加權和，也是 $\mathrm{poly}(S)$；$d\le S$。所以總共 $\mathrm{poly}(S)$。

| | |
|---|---|
| 通訊 | $d\cdot\mathrm{polylog}(S)$ |
| 驗證者 | $d\cdot\mathrm{polylog}(S) + \tilde{O}(n)$ |
| 證明者 | $\mathrm{poly}(S)$ |

---

## 5. Soundness

### 5.1 證明

[▶ 24:46](https://youtu.be/Ob1fFHAXlJQ?t=1486)

假設有作弊證明者 $P^{*}$，宣稱假的 $v_0^{*}$，卻有機率 $\varepsilon$ 被接受。

**記號**：第 $i$ 對 sum-check 中驗證者的隨機數記為 $(r_0^{(i)}, r_1^{(i)}, r_2^{(i)})$；之後證明者報的兩個值是 $v_{i,1}$、$v_{i,2}$，宣稱 $\tilde{V}_i(r_1^{(i-1)}) = v_{i,1}$、$\tilde{V}_i(r_2^{(i-1)}) = v_{i,2}$。

**想法**：一開始是假的，最後（輸入層，驗證者自己算）一定是真的。所以中間某一層要「從假變真」。

**壞事件**：

$$B_i := \text{「第 } i-1 \text{ 層的兩個宣稱至少一個是假的，但第 } i \text{ 層的兩個宣稱都是真的」}.$$

作弊成功 ⟹ 某個 $B_i$ 發生。用 union bound：

$$\varepsilon \le \Pr\left[ \bigcup_i B_i \right] \le \sum_{i=1}^{d}\Pr[B_i].$$

**再拆成兩半**（[▶ 30:43](https://youtu.be/Ob1fFHAXlJQ?t=1843)）：

- $B_{i,1}$：第 $i-1$ 層的**第一個**宣稱是假的，但第 $i$ 層兩個都真。
- $B_{i,2}$：第 $i-1$ 層的**第二個**宣稱是假的，但第 $i$ 層兩個都真。

$B_i\subseteq B_{i,1}\cup B_{i,2}$，所以

$$\varepsilon \le \sum_{i=1}^{d}\sum_{b\in\{1,2\}}\Pr[B_{i,b}].$$

- ⚠️ 逐字稿缺字：[▶ 33:05](https://youtu.be/Ob1fFHAXlJQ?t=1985) 學生提醒 union bound 那幾步應該是「$\le$」不是「$=$」，講者改正（中間那個是定義，用「$=$」）。

**$\Pr[B_{i,1}]$ 有多大**：$B_{i,1}$ 代表第一個 sum-check 從一個**假的**宣稱開始，最後卻落到**真的**值上（如果最後的值是真的而一開始是假的，驗證者其實應該會抓到）。這正是「在那個 sum-check 裡作弊成功」。由 sum-check 的 soundness：

$$\Pr[B_{i,b}] \le \frac{(\text{變數數})\cdot(\text{次數})}{|\mathbb{F}|} \approx \frac{\log^2 S}{|\mathbb{F}|}.$$

（變數數 $\approx\log S/\log\log S$，次數 $\approx\log S$，講者粗估成 $\log^2 S$。）

所以

$$\varepsilon \le 2d\cdot\frac{O(\log^2 S)}{|\mathbb{F}|}.$$

取 $|\mathbb{F}|$ 夠大（只在通訊裡付 $\log|\mathbb{F}|$）就好。

- ⚠️ 逐字稿缺字：[▶ 35:09](https://youtu.be/Ob1fFHAXlJQ?t=2109) 字幕寫「epsilon is smaller than log squared f divided by epsilon」，依上下文是「$\le\log^2 S/|\mathbb{F}|$」（每個 sum-check），講者漏講了 $d$ 和 2 的因子。

> 【課本補充】Thaler Table 4.4：原始 GKR 的 soundness 錯誤是 $O(d\log(S)/|\mathbb{F}|)$（Thaler 用 $H = \{0,1\}$，每層 sum-check 有 $O(\log S)$ 個變數、每變數次數 $O(1)$）。

### 5.2 用同一組隨機數為什麼沒事

[▶ 35:52](https://youtu.be/Ob1fFHAXlJQ?t=2152)

【Q&A】（接續 [▶ 19:53](https://youtu.be/Ob1fFHAXlJQ?t=1193) 的問題）**兩個 sum-check 用同一組隨機數，安全嗎？**

不危險，因為上面用的是 **union bound**：

- 只看其中一個 sum-check。就算旁邊同時在做別的事，在**這一個**上作弊成功的機率仍 $\le$ sum-check 的錯誤。
- 兩個事件可能相關（例如「在一個上作弊成功當且僅當在另一個上也成功」），但 union bound 不在乎相關性。

【Q&A】[▶ 36:34](https://youtu.be/Ob1fFHAXlJQ?t=2194) **GKR 是把 sum-check 當黑盒用嗎？**
對，完全黑盒。需要的性質只有一個（除了 completeness 和 soundness）：

> 協定結束時，化簡成「驗證者檢查 $f$ 在**一個由驗證者自己隨機選的點** $(t_1, \ldots, t_m)$ 上的值」。

正是這個性質讓兩個 sum-check 能平行、而且最後查的是同樣的點。

【口頭】原始 GKR 用「二變一」的技巧，所以任何 sum-check 都行；這裡比較簡單的版本需要上面那個性質。

---

## 6. 輸入層與其他 Q&A

【Q&A】[▶ 37:55](https://youtu.be/Ob1fFHAXlJQ?t=2275) **到輸入層怎麼辦？輸入的擴張怎麼算？**

驗證者要檢查 $\tilde{V}_d(z_1^{*}) = v_{d,1}^{*}$、$\tilde{V}_d(z_2^{*}) = v_{d,2}^{*}$。$\tilde{V}_d$ 就是輸入 $x = (x_1, \ldots, x_n)$（補 0 到 $S$ 個）的低次擴張：

$$\tilde{V}_d(z) = \sum_{h\in H^m} V_d(h)\,\chi(h, z) = \sum_{j=1}^{n} x_j\,\chi(h^{(j)}, z),$$

只有 $n$ 項非零（其他是補的 0），每個 $\chi(h^{(j)}, z)$ 是 polylog 時間可算的小多項式。所以驗證者 $\tilde{O}(n)$ 時間算完。

- 學生：所以 $n$ 很小？講者：$n$ 遠小於 $S$。驗證者本來就得讀輸入，不然不知道在驗證什麼；如果 $n$ 和 $S$ 差不多，整件事就沒意義了。
- 【Q&A】補 0 的假閘？對，都設成 0。【口頭】原論文沒有全設成 0，所以符號更複雜。

【Q&A】[▶ 40:45](https://youtu.be/Ob1fFHAXlJQ?t=2445) **$v_1$、$v_2$ 是來自 fan-in 2 的左右兩個輸入嗎？**
是。因為 fan-in 2，$\mathrm{add}_i$ 只有 $(p, w_1, w_2)$ 三個參數。若 fan-in 更大，就會有 $V(w_1) + V(w_2) + V(w_3) + \cdots$。

【Q&A】[▶ 41:27](https://youtu.be/Ob1fFHAXlJQ?t=2487) Leo：**fan-in 更大、深度更淺，能不能平行跑更多 sum-check 來省深度？**
可以，2 沒什麼神奇的。但 fan-in 太大，通訊之類的成本會變大。只要 fan-in 最多 polylog 就還行。

---

## 7. 一頁速查表

### GKR 協定

$$f_{i, z^{*}}(p, w_1, w_2) = \tilde{\chi}(p, z^{*})\left[ \widetilde{\mathrm{add}}_i\cdot\left( \tilde{V}_{i+1}(w_1) + \tilde{V}_{i+1}(w_2) \right) + \widetilde{\mathrm{mult}}_i\cdot\tilde{V}_{i+1}(w_1)\,\tilde{V}_{i+1}(w_2) \right], \quad \tilde{V}_i(z^{*}) = \sum_{p, w_1, w_2\in H^m} f_{i, z^{*}}.$$

每一層：
1. 兩個宣稱 $\tilde{V}_i(z_1^{*})$、$\tilde{V}_i(z_2^{*})$。
2. 對 $f_{i, z_1^{*}}$、$f_{i, z_2^{*}}$ **平行**跑 sum-check，**同一組**隨機數 $(r_0, r_1, r_2)$。
3. 證明者報 $\tilde{V}_{i+1}(r_1)$、$\tilde{V}_{i+1}(r_2)$；驗證者檢查兩個 sum-check 的最後一步。
4. 新固定點 $(r_1, r_2)$。

輸入層：驗證者自己算 $\tilde{x}$ 在兩點的值，$\tilde{O}(n)$。

| | |
|---|---|
| Completeness | 1 |
| 通訊 | $d\cdot\mathrm{polylog}(S)$ |
| 驗證者 | $d\cdot\mathrm{polylog}(S) + \tilde{O}(n)$（假設可查 $\widetilde{\mathrm{add}}$、$\widetilde{\mathrm{mult}}$） |
| 證明者 | $\mathrm{poly}(S)$ |
| Soundness 錯誤 | $\le 2d\cdot O(\log^2 S)/|\mathbb{F}|$ |

**Soundness 關鍵一步**：開始假、最後真 ⟹ 某層某個 sum-check 從假到真。每個機率 $\le$ sum-check 錯誤；對 $2d$ 個做 union bound（不在乎相關性，所以共用隨機數沒問題）。

**平行的必要性**：循序的話，第二個 sum-check 時證明者已知道硬幣，可以作弊。

**需要的 sum-check 性質**：最後只查 $f$ 在驗證者自選隨機點上的值。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 驗證者要查 $\widetilde{\mathrm{add}}_i$、$\widetilde{\mathrm{mult}}_i$ | 第 05 集：怎麼處理（log-space uniform） |
| GKR 的推論 | 第 05 集：IP = PSPACE |
| GKR | 第 06–07 集：用 GKR 做 PCP |
| public coin、「最後查自選點」 | 第 10–13 集：Fiat–Shamir |

---

## 附：本集一句話總結

> **一個宣稱變兩個不用擔心：下一層把兩個 sum-check 平行跑、共用同一組隨機數，最後需要的又剛好是同樣兩個點的值，所以每層永遠只有兩個宣稱；GKR 就是 $d$ 對這樣的 sum-check，soundness 用 union bound 加起來。**

---

*筆記依據 Yael Tauman Kalai「Advanced Topics in Cryptography（MIT 6.5630, Fall 2023）」Lecture 2 Part 2 錄影逐字稿（MIT 真人字幕，42:30）與 Thaler《Proofs, Arguments, and Zero-Knowledge》§4.6 整理。*
