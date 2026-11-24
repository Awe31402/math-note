---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 9
lecture: Lecture 9
date: 2023-10-25
video: https://youtu.be/B8ucNShRwjQ
notes: 投影片 L9_ann.pdf（62 頁）；《Elements of Information Theory》§13.2–13.3、§14.13
---

# 第 9 集 · Lecture 9：context-based 算術編碼與 LLM 壓縮（Context-based AC & LLM Compression） [▶ 影片](https://youtu.be/B8ucNShRwjQ)

← 上一集：[08-conditional-entropy](08-conditional-entropy.md) ｜ [總目錄](README.md) ｜ 下一集：[10-lz-universal-compression](10-lz-universal-compression.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 9 集
> **講者**：Shubham Chandak（Pulkit 結尾補充）
> **來源**：YouTube 錄影逐字稿（1:19:52，人工字幕 en-US）＋ 投影片 `L9_ann.pdf` ＋ Cover & Thomas §13.2–13.3、§14.13
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧與小考：一條不平穩的 Markov 鏈](#1-回顧與小考一條不平穩的-markov-鏈)
- [2. 怎麼達到熵率：兩條路](#2-怎麼達到熵率兩條路)
- [3. 算術編碼一頁回顧](#3-算術編碼一頁回顧)
- [4. 1 階 Markov 來源的算術編碼](#4-1-階-markov-來源的算術編碼)
- [5. context-based 算術編碼：更好的預測 = 更好的壓縮](#5-context-based-算術編碼更好的預測--更好的壓縮)
- [6. 例子：用 Llama 預測下一個 token](#6-例子用-llama-預測下一個-token)
- [7. 解碼](#7-解碼)
- [8. 沒有模型怎麼辦：兩段式 vs. 自適應](#8-沒有模型怎麼辦兩段式-vs-自適應)
- [9. 壓縮 = 預測](#9-壓縮--預測)
- [10. $k$ 階自適應算術編碼](#10-k-階自適應算術編碼)
- [11. 實驗：福爾摩斯小說](#11-實驗福爾摩斯小說)
- [12. 兩段式的陷阱：模型開始記住資料（MDL）](#12-兩段式的陷阱模型開始記住資料mdl)
- [13. 進階模型：PPM、CTW、NNCP、CMIX](#13-進階模型ppmctwnncpcmix)
- [14. LLM 壓縮](#14-llm-壓縮)
- [15. 一頁速查表](#15-一頁速查表)
- [16. 與後續集數的連結](#16-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/B8ucNShRwjQ?t=5) 兩件事：

1. 把上一講的理論變成實作：怎麼**達到** Markov 過程、平穩過程的熵率，並深入**文字壓縮**。
2. 如果有時間，開始講 LZ77（**本集沒講到**，移到第 10 集）。

| 主題 | 課本 |
|---|---|
| context-based 算術編碼 | §13.3 |
| 自適應（逐次估計機率） | §13.2 |
| 最小描述長度（MDL） | §14.13 |
| LLM 壓縮 | 課本無 |

---

## 1. 回顧與小考：一條不平穩的 Markov 鏈

### 1.1 回顧

[▶ 00:41](https://youtu.be/B8ucNShRwjQ?t=41) $k$ 階 Markov：要前 $k$ 個符號就夠預測下一個。平穩過程：統計量不隨時間變 [▶ 01:20](https://youtu.be/B8ucNShRwjQ?t=80)；實務上就想成「給過去，可以預測一些未來」[▶ 02:00](https://youtu.be/B8ucNShRwjQ?t=120)。條件熵 $H(U\mid V)$：知道 $V$ 後 $U$ 平均剩多少不確定性，也就是知道 $V$ 時壓 $U$ 要幾位元 [▶ 02:36](https://youtu.be/B8ucNShRwjQ?t=156)。鏈鎖律、條件降低熵。熵率兩個等價定義 [▶ 03:11](https://youtu.be/B8ucNShRwjQ?t=191)、[▶ 03:45](https://youtu.be/B8ucNShRwjQ?t=225)。

### 1.2 小考第 1 題

[▶ 04:25](https://youtu.be/B8ucNShRwjQ?t=265) Markov 鏈（沒說平穩）：

$$U_1\sim\mathrm{Ber}(0.5),\quad P(U_{i+1}=1\mid U_i=0)=1,\quad P(U_{i+1}=1\mid U_i=1)=P(U_{i+1}=0\mid U_i=1)=0.5.$$

$U_i=0$ 時下一個一定是 1；$U_i=1$ 時下一個 0、1 各半 [▶ 05:00](https://youtu.be/B8ucNShRwjQ?t=300)。

| 題 | 答案 |
|---|---|
| $H(U_1)$ | 1 位元 [▶ 05:35](https://youtu.be/B8ucNShRwjQ?t=335) |
| $H(U_2)$ | $P(U_2=0)=\frac12\cdot0+\frac12\cdot\frac12=\frac14$ [▶ 07:14](https://youtu.be/B8ucNShRwjQ?t=434)，$H=h_b(\frac14)\approx0.81$ [▶ 07:48](https://youtu.be/B8ucNShRwjQ?t=468) |
| 平穩嗎？ | **否** [▶ 08:26](https://youtu.be/B8ucNShRwjQ?t=506)：$H(U_2)\ne H(U_1)$ |
| $H(U_2\mid U_1)$ | $\frac12\cdot0+\frac12\cdot1=\frac12$ [▶ 09:46](https://youtu.be/B8ucNShRwjQ?t=586) |
| 改成 $U_1\sim\mathrm{Ber}(\frac23)$（平穩），熵率？ | $\frac23$ 位元 [▶ 11:41](https://youtu.be/B8ucNShRwjQ?t=701) |

[▶ 06:09](https://youtu.be/B8ucNShRwjQ?t=369) Ed 上有人問：$U_2$ 依賴 $U_1$，那 $H(U_2)$ 是什麼意思？講者：不管依不依賴別人，都是隨機變數，都有邊際分布、都能算熵。

【課堂討論】[▶ 07:48](https://youtu.be/B8ucNShRwjQ?t=468) 有學生以為 Markov 鏈一定平穩。講者：不一定，所以上課才特別說「平穩的 Markov 鏈」；要從平穩分布出發才平穩 [▶ 08:26](https://youtu.be/B8ucNShRwjQ?t=506)。

> 以下**不是逐字稿內容**，是補上最後一題的計算：$U_1\sim\mathrm{Ber}(\frac23)$ 時 $P(U_2=1)=\frac13\cdot1+\frac23\cdot\frac12=\frac23$，分布不變，所以平穩。熵率 $=H(U_2\mid U_1)=P(U_1=0)\cdot0+P(U_1=1)\cdot1=\frac23$。

【口頭】[▶ 11:41](https://youtu.be/B8ucNShRwjQ?t=701) 條件機率不只這門課，機器學習、統計、機率課都會一直碰到，要熟。

---

## 2. 怎麼達到熵率：兩條路

[▶ 12:20](https://youtu.be/B8ucNShRwjQ?t=740) 先從 1 階 Markov 來源開始。熵率的兩個定義 [▶ 12:59](https://youtu.be/B8ucNShRwjQ?t=779) 各指出一條路：

$$H(\mathbf U)=\lim_{n\to\infty}\frac{H(U_1,\dots,U_n)}{n}=H(U_2\mid U_1)\quad\text{（1 階 Markov）}.$$

1. **分組**：$n$ 個一組做 Huffman 或算術編碼，$n$ 越來越大，照定義會到熵率 [▶ 12:59](https://youtu.be/B8ucNShRwjQ?t=779)。
2. **逐步條件化** [▶ 13:37](https://youtu.be/B8ucNShRwjQ?t=817)：先編 $U_1$，再編 $U_2\mid U_1$、$U_3\mid U_2$……**今天主要走這條**。

**分組為什麼不好** [▶ 14:09](https://youtu.be/B8ucNShRwjQ?t=849)：

- 區塊不能太大（複雜度）。
- iid 時，分組次佳只因為 Huffman 只對二進分布最佳。
- **非 iid 時還有新問題** [▶ 14:41](https://youtu.be/B8ucNShRwjQ?t=881)：把 $(U_1,U_2)$、$(U_3,U_4)$ 分開編，就丟掉了 $U_2$ 和 $U_3$ 之間的相關。

【投影片補充】`L9_ann.pdf` p.10 練習：對 $U_1\sim\mathrm{Unif}\{0,1,2\}$、$U_{i+1}=U_i+Z_i\bmod3$ 算 $H(U_1)$、$H(U_1,U_2)$，和 $H(\mathbf U)$ 比較。

> 以下**不是逐字稿內容**，是做這個練習：$H(U_1)=\log_23\approx1.585$；$H(U_1,U_2)=H(U_1)+H(U_2\mid U_1)=1.585+1=2.585$，兩個一組每符號 $1.29$；熵率是 1。所以兩個一組（就算用最好的碼）每符號仍多 0.29 位元。

---

## 3. 算術編碼一頁回顧

[▶ 15:15](https://youtu.be/B8ucNShRwjQ?t=915) 本講（以及不實作的話整門課）需要知道的算術編碼：

- 把區間依符號機率切開；每一步把當前符號的子區間再切 [▶ 15:50](https://youtu.be/B8ucNShRwjQ?t=950)。
- 最後區間長度 = 機率的乘積。
- 碼長 ≈ $\log\frac1{\text{區間長度}}=\log\frac1{P(x_1)P(x_2)\cdots P(x_n)}$ [▶ 16:30](https://youtu.be/B8ucNShRwjQ?t=990)。

[▶ 17:08](https://youtu.be/B8ucNShRwjQ?t=1028) 對照經驗法則：每個符號 $x$ 付 $\log\frac1{P(x)}$，算術編碼正好如此。

---

## 4. 1 階 Markov 來源的算術編碼

【課堂討論】[▶ 18:25](https://youtu.be/B8ucNShRwjQ?t=1105) Markov 鏈：每個符號以 $\frac12$ 留在自己、$\frac12$ 到「自己 + 1 mod 3」。編 `2, 0, 1`。投影片的做法和以前有什麼不同？

- 編第一個 2：沒有不同，假設初始均勻，切成三等份 [▶ 18:58](https://youtu.be/B8ucNShRwjQ?t=1138)。
- 第二步 [▶ 18:58](https://youtu.be/B8ucNShRwjQ?t=1138)：學生答：2 不可能到 1，所以第二步只有 0 和 2 兩段。

[▶ 19:34](https://youtu.be/B8ucNShRwjQ?t=1174) 講者：知道第一個是 2 後，模型說下一個是 0 或 2 各半，所以**依條件分布切區間**，而不是死守原本的分布。下一步也一樣，用「前一個是 0」的知識，下一個只能是 0 或 1 [▶ 20:05](https://youtu.be/B8ucNShRwjQ?t=1205)。

> **唯一的改變：每一步用 $P(\cdot\mid\text{過去})$ 切區間**，而不是邊際機率。1 階 Markov 只需要看最後一個符號；一般可以看整個過去 [▶ 20:43](https://youtu.be/B8ucNShRwjQ?t=1243)。

**期望位元數** [▶ 21:14](https://youtu.be/B8ucNShRwjQ?t=1274)（`L9_ann.pdf` p.13）：區間長度 $=P(u_1)P(u_2\mid u_1)\cdots P(u_n\mid u_{n-1})$，

$$
\begin{aligned}
\frac1n\mathbb{E}\left[\log_2\frac1{P(U_1)P(U_2\mid U_1)\cdots P(U_n\mid U_{n-1})}\right]
&=\frac1n\mathbb{E}\left[\log_2\frac1{P(U_1)}\right]+\frac1n\sum_{i=2}^{n}\mathbb{E}\left[\log_2\frac1{P(U_i\mid U_{i-1})}\right]\\
&=\frac1nH(U_1)+\frac{n-1}nH(U_2\mid U_1)\ \to\ H(U_2\mid U_1).
\end{aligned}
$$

（第二個等號用平穩：每個 $H(U_i\mid U_{i-1})$ 都等於 $H(U_2\mid U_1)$。）[▶ 21:50](https://youtu.be/B8ucNShRwjQ?t=1310) 第一項特別，因為沒有過去；之後每項都有。

【課本補充】§13.3（書頁 436–440）的算術編碼本來就寫成一般形式：只要能算出 $P(x_i\mid x^{i-1})$，就能逐步縮小區間，總碼長 $\le\log\frac1{P(x^n)}+2$。

---

## 5. context-based 算術編碼：更好的預測 = 更好的壓縮

### 5.1 一般形式

[▶ 22:27](https://youtu.be/B8ucNShRwjQ?t=1347) **context-based 算術編碼**（本講核心）：

- 有資料，有一個**模型**。模型不一定是資料的真實模型；資料甚至不一定來自某個機率分布，只是給你一串序列 [▶ 22:27](https://youtu.be/B8ucNShRwjQ?t=1347)。
- 模型就是一個預測器：「過去是 ABCD，下一個是 E 的機率 50%」。
- 第一步沒有過去，用模型預測第一個符號；第二步用前一個；之後用整個過去 [▶ 22:58](https://youtu.be/B8ucNShRwjQ?t=1378)。

[▶ 23:30](https://youtu.be/B8ucNShRwjQ?t=1410) 投影片例子：模型認為前兩個是 2、0 時，下一個是 1 的機率比 0、2 大，就照它的預測切區間。碼長仍是 $\log\frac1{\text{區間長度}}$。

$$\text{總位元數}=\sum_{i=1}^n\log_2\frac1{\hat P(u_i\mid u_1,\dots,u_{i-1})}.$$

### 5.2 核心鏈條

[▶ 24:11](https://youtu.be/B8ucNShRwjQ?t=1451)

> **更好的預測器 → 實際觀察到的東西機率更高 → 區間更大 → 碼長更短。**
> **更好的預測 = 更好的壓縮。** [▶ 24:42](https://youtu.be/B8ucNShRwjQ?t=1482)

好的英文預測器會說 Q 後面很可能是 U。[▶ 24:42](https://youtu.be/B8ucNShRwjQ?t=1482) 講者：到這裡可以忘掉算術編碼了，它只是工具。

[▶ 25:38](https://youtu.be/B8ucNShRwjQ?t=1538) 只要能估計「給定 context（過去）時下一個符號的機率」，就能用算術編碼，編 $u_n$ 用 $\log\frac1{\hat P(u_n\mid\text{past})}$ 位元：

- **好模型** [▶ 26:10](https://youtu.be/B8ucNShRwjQ?t=1570)：$\hat P(u_n\mid\text{past})\approx1$，幾乎 0 位元。
- **壞模型** [▶ 26:50](https://youtu.be/B8ucNShRwjQ?t=1610)：例如說「Q 後面絕不會是 U」，$\log\frac1{\text{很小}}$ 很大。

---

## 6. 例子：用 Llama 預測下一個 token

[▶ 26:50](https://youtu.be/B8ucNShRwjQ?t=1610) Llama 是 Meta 發布的語言模型。講者昨天試了，給一段字，看下一個 token 的前五名（`L9_ann.pdf` p.17–22）：

| 輸入 | 前幾名 |
|---|---|
| `than` | x 18.6%、e 8.5%、`,` 5.2%、the 5.2%、king 4.3% |
| `louder than` | words 30.4%、love 11.9%、a 11.2%、the 5.8%、bombs 4.7% |
| `speak louder than` | words 47.8%、money 7.8%、a 4.7%、the 3.2%、actions 2.5% |
| `Actions speak louder than` | words 96.5%、the 0.2%、a 0.1%… |

[▶ 27:23](https://youtu.be/B8ucNShRwjQ?t=1643) 只給 `than` 時，模型以為是 thanx（某種新用語）、thane、thanking 之類。給更多 context，分布就變了 [▶ 28:01](https://youtu.be/B8ucNShRwjQ?t=1681)。

【課堂討論】[▶ 28:01](https://youtu.be/B8ucNShRwjQ?t=1681) 給 `speak louder than`，若下一個真的是 words，大約要幾位元？學生答 **1 位元** [▶ 28:37](https://youtu.be/B8ucNShRwjQ?t=1717)：$\log_2\frac1{1/2}=1$。一個字本來要很多位元，現在 1 位元就夠。給 `Actions speak louder than` 時 96.5%，遠少於 1 位元。

[▶ 29:15](https://youtu.be/B8ucNShRwjQ?t=1755) **給好模型越多 context，它越有把握，壓縮用的位元越少。**（20 年前的笨模型給再長也沒用。）

另一例 [▶ 29:15](https://youtu.be/B8ucNShRwjQ?t=1755)：

| 輸入 | 前幾名 |
|---|---|
| `Stanford's data compression` | research 9.0%、group 7.5%、and 5.6%、library 5.3%、team 4.1%（沒有 class、course，講者說很難過） |
| `Enrolling in Stanford's data compression` | course 56.6%、class 10.1%、program 4.8%、courses 4.5%… |

[▶ 29:54](https://youtu.be/B8ucNShRwjQ?t=1794) 若資料是 $k$ 階 Markov，前 $k$ 個就夠；但真實資料不是任何 $k$ 階 Markov [▶ 30:32](https://youtu.be/B8ucNShRwjQ?t=1832)。讀小說時，第一章出現的角色可能消失五章後又出現，要猜他的名字需要前六章的 context。計算上不可能看全部過去，但大腦某種程度上做得到（記不得就翻回去看）[▶ 31:05](https://youtu.be/B8ucNShRwjQ?t=1865)。

---

## 7. 解碼

[▶ 31:42](https://youtu.be/B8ucNShRwjQ?t=1902) 方塊圖：

```
過去 (u1..u_{i-1}) ──> [模型] ──P̂(·|過去)──> [算術編碼步驟] <── u_i
                                               └─> log2 1/P̂(u_i|過去) 位元
```

【課堂討論】[▶ 31:42](https://youtu.be/B8ucNShRwjQ?t=1902) 解碼需要模型嗎？學生點頭 [▶ 32:22](https://youtu.be/B8ucNShRwjQ?t=1942)。算術解碼和編碼對稱，解碼器也要知道怎麼切區間，所以**需要同一個模型**。

[▶ 32:56](https://youtu.be/B8ucNShRwjQ?t=1976) 解碼一步一步來：第 0 步沒有過去但有模型，能切區間 → 解出 $u_1$ → 把 $u_1$ 餵給模型 → 得到下一步機率 → 解出 $u_2$……

```
過去 ──> [模型] ──P̂──> [算術解碼步驟] <── 壓縮位元
                            └─> u_i ──> 加進過去
```

【口頭】[▶ 34:14](https://youtu.be/B8ucNShRwjQ?t=2054) 寫了壓縮器一定也要寫解壓縮器。有些東西能「壓到 0 位元」，結果解不回來。

---

## 8. 沒有模型怎麼辦：兩段式 vs. 自適應

【課堂討論】[▶ 34:51](https://youtu.be/B8ucNShRwjQ?t=2091) 沒有模型怎麼辦？學生答：作業 1 第 5 題是看輸入資料的經驗分布 [▶ 35:30](https://youtu.be/B8ucNShRwjQ?t=2130)。講者：對，當時用 Huffman（還沒學算術編碼），模型是 iid 的 [▶ 36:04](https://youtu.be/B8ucNShRwjQ?t=2164)。

兩種做法 [▶ 36:04](https://youtu.be/B8ucNShRwjQ?t=2164)：

1. **兩段式**（two-pass）：先從資料建模型，再用它編碼。作業 1 就是這樣。
2. **自適應**（adaptive）[▶ 36:38](https://youtu.be/B8ucNShRwjQ?t=2198)：**邊看資料邊建模型**。

### 8.1 自適應的方塊圖

[▶ 36:38](https://youtu.be/B8ucNShRwjQ?t=2198) 模型不固定：每一步模型給出下一個符號的機率 → 編碼 → **用這個符號更新模型** → 下一步。模型看到越多資料，就一直訓練、更新自己。

【課堂討論】[▶ 37:11](https://youtu.be/B8ucNShRwjQ?t=2231) 怎麼解碼？學生答：解碼器一次解一個符號，就照樣更新模型，保持和編碼器一樣的狀態 [▶ 37:51](https://youtu.be/B8ucNShRwjQ?t=2271)。

[▶ 37:51](https://youtu.be/B8ucNShRwjQ?t=2271) 解碼順序：解 $u_1$ → 更新模型 → 解 $u_2$ → 更新模型……**必須和編碼器完全一樣地更新**。

### 8.2 三個注意事項

（`L9_ann.pdf` p.29）

1. **編碼器和解碼器每一步（包括初始化）都要有完全相同的模型狀態** [▶ 38:30](https://youtu.be/B8ucNShRwjQ?t=2310)。只要某一步看到不同的分布就壞了，之後全部都壞。
   - 【口頭】[▶ 38:30](https://youtu.be/B8ucNShRwjQ?t=2310) 簡單模型沒問題，但神經網路函式庫有各種隨機性就很麻煩 [▶ 39:05](https://youtu.be/B8ucNShRwjQ?t=2345)。ChatGPT 不在乎同一個輸入每次輸出一樣；壓縮模型卻必須每次給出一樣的機率，不能有 GPU 層級的隨機、浮點誤差。所以用神經網路做壓縮的人得自己寫函式庫；就算寫好了，在一張 GPU 上壓、另一張 GPU 上解還是會壞 [▶ 39:40](https://youtu.be/B8ucNShRwjQ?t=2380)。
2. **別太心急：編 $u_i$ 之前不要先用 $u_i$ 更新模型** [▶ 39:40](https://youtu.be/B8ucNShRwjQ?t=2380)。編碼器手上有全部輸入，但永遠要想「解碼器此刻知道什麼」。【課堂討論】[▶ 40:16](https://youtu.be/B8ucNShRwjQ?t=2416) 如果先用 $u_1$ 更新再編 $u_1$，解碼器能動嗎？學生答：不能，解碼器還沒有 $u_1$。有損壓縮的自適應方法也會遇到 [▶ 40:51](https://youtu.be/B8ucNShRwjQ?t=2451)。
3. **永遠不要給任何符號 0 機率** [▶ 40:51](https://youtu.be/B8ucNShRwjQ?t=2451)。模型說不會出現、偏偏出現了，$\log\frac10=\infty$，算術編碼器就壞了。就算認為英文裡 Q 後面絕不會是 Q，也給它一點點機率。

### 8.3 優缺點

[▶ 41:33](https://youtu.be/B8ucNShRwjQ?t=2493)（`L9_ann.pdf` p.28）

| | 兩段式 | 自適應 |
|---|---|---|
| ✅ | 從整份資料學模型，可能壓得比較好；比較好平行化 | 不用存模型；適合串流，邊收邊壓 [▶ 42:07](https://youtu.be/B8ucNShRwjQ?t=2527)；實務上效果很好 |
| ❌ | 要把模型存進壓縮檔；要兩次掃過資料（常常不行：資料一直來、放不進記憶體）[▶ 42:07](https://youtu.be/B8ucNShRwjQ?t=2527)；統計量隨時間變時（前半小說、後半程式碼）學到的是混合模型 | 一開始模型很爛，前面的樣本壓得差 [▶ 42:41](https://youtu.be/B8ucNShRwjQ?t=2561) |

---

## 9. 壓縮 = 預測

### 9.1 交叉熵損失就是碼長

[▶ 43:17](https://youtu.be/B8ucNShRwjQ?t=2597) 機器學習的**交叉熵損失**（cross-entropy loss，又叫 log loss）：分類時預測器給機率，例如 貓 90%、狗 5%、牛 5%；真實答案是貓，損失就是 $\log\frac1{0.9}$ [▶ 43:50](https://youtu.be/B8ucNShRwjQ?t=2630)。

$$\text{損失}=\sum_{c\in\mathcal C}\mathbf 1_{y_i=c}\log_2\frac1{\hat P(c\mid y_1,\dots,y_{i-1})}=\log_2\frac1{\hat P(y_i\mid y_1,\dots,y_{i-1})}.$$

[▶ 44:32](https://youtu.be/B8ucNShRwjQ?t=2672) **這和算術編碼的碼長完全一樣。** 預測和壓縮是同一個問題。ML 意義下的好預測器就是好壓縮器 [▶ 45:06](https://youtu.be/B8ucNShRwjQ?t=2706)。

[▶ 45:06](https://youtu.be/B8ucNShRwjQ?t=2706) 壓縮就是要有好的資料模型；有好模型就自動有好壓縮器。有些壓縮器（像 LZ77）沒有**明確**建模，但內在都有建模。也可以在某些情況用 rANS 取代算術編碼（有些問題，部分能解決）[▶ 45:41](https://youtu.be/B8ucNShRwjQ?t=2741)。

### 9.2 反過來：壓縮器也給出預測器

[▶ 45:41](https://youtu.be/B8ucNShRwjQ?t=2741) 每個壓縮器都誘導出一個預測器。若壓縮器把 $x_1,\dots,x_n$ 編成 $l$ 位元 [▶ 46:39](https://youtu.be/B8ucNShRwjQ?t=2799)：

$$l=\log_2\frac1p\quad\Longrightarrow\quad\hat P(x_1,\dots,x_n)\approx2^{-l}.$$

[▶ 46:39](https://youtu.be/B8ucNShRwjQ?t=2799) 有篇很新的論文把 gzip 變成預測器，效果不怎麼好，但做得到。有些壓縮器比較容易明確求出預測機率。

---

## 10. $k$ 階自適應算術編碼

### 10.1 想法

[▶ 47:15](https://youtu.be/B8ucNShRwjQ?t=2835) 邊看資料邊學一個 $k$ 階模型（`L9_ann.pdf` p.34）：

- 一開始，$(k+1)$ 階字母表裡每個組合的頻率都設成 1（避免 0 機率）。
- 每看到一個符號就更新頻率。
- 每一步，頻率誘導出下一個符號的機率分布。

[▶ 47:53](https://youtu.be/B8ucNShRwjQ?t=2873) 例：過去看過很多次 BANA，90% 後面接 N、10% 接 L；下次看到 BANA，就預測 N 90%、L 10%。

### 10.2 例子：1 階，資料 `101011`

[▶ 48:30](https://youtu.be/B8ucNShRwjQ?t=2910) 1 階模型要記**兩個一組**的計數。初始 $c(0,0)=c(0,1)=c(1,0)=c(1,1)=1$。第一個符號沒有過去，前面補一個假的 0 [▶ 49:02](https://youtu.be/B8ucNShRwjQ?t=2942)。

【課堂討論】[▶ 49:41](https://youtu.be/B8ucNShRwjQ?t=2981) 過去是 0 時下一個是 1 的機率？選項 1、1/3、1/2，只有少數人選 **1/2**，正確 [▶ 49:41](https://youtu.be/B8ucNShRwjQ?t=2981)：

$$\hat P(1\mid0)=\frac{c(0,1)}{c(0,0)+c(0,1)}.$$

[▶ 50:18](https://youtu.be/B8ucNShRwjQ?t=3018) 例：看過 01 九十九次、00 一次，就說 $\hat P(1\mid0)=\frac9{10}$（講者口誤，99 次應為 9 次；投影片手寫是 9 次和 1 次）。

| 步 | 前一個 | 目前 | 預測機率 | 更新 |
|---|---|---|---|---|
| 1 | 0（補的） | 1 | $\hat P(1\mid0)=\frac12$ [▶ 50:53](https://youtu.be/B8ucNShRwjQ?t=3053) | $c(0,1):1\to2$ |
| 2 | 1 | 0 | $\hat P(0\mid1)=\frac12$ [▶ 51:27](https://youtu.be/B8ucNShRwjQ?t=3087) | $c(1,0):1\to2$ |
| 3 | 0 | 1 | $\hat P(1\mid0)=\frac23$ [▶ 51:27](https://youtu.be/B8ucNShRwjQ?t=3087) | $c(0,1):2\to3$ |
| 4 | 1 | 0 | $\hat P(0\mid1)=\frac23$ | $c(1,0):2\to3$ |

（前四步依 `L9_ann.pdf` p.36–39。）

[▶ 51:58](https://youtu.be/B8ucNShRwjQ?t=3118) 看越多資料，模型就學到資料的統計，預測越來越符合資料。作業裡會自己做一個。

> 以下**不是逐字稿內容**，是把剩下兩步做完：第 5 步前 0、目前 1，$\hat P(1\mid0)=\frac34$，$c(0,1)\to4$；第 6 步前 1、目前 1，$\hat P(1\mid1)=\frac{c(1,1)}{c(1,0)+c(1,1)}=\frac14$，$c(1,1)\to2$。總位元數 $\approx\log_22+\log_22+\log_2\frac32+\log_2\frac32+\log_2\frac43+\log_24\approx1+1+0.585+0.585+0.415+2=5.585$。最後一個 1 很「意外」（模型以為 1 後面多半接 0），所以花了 2 位元。

### 10.3 觀察

[▶ 52:33](https://youtu.be/B8ucNShRwjQ?t=3153)（`L9_ann.pdf` p.41）

- 漸漸學到資料的經驗分布。
- 一開始用均勻分布；若知道資料的一些先驗知識，可以用它初始化計數（編解碼器都要知道），**而且不能有 0**。
- $k=0$ 就是 iid 但未知分布的情況，作業 1 那題可以這樣做 [▶ 52:33](https://youtu.be/B8ucNShRwjQ?t=3153)。

【課堂討論】[▶ 53:06](https://youtu.be/B8ucNShRwjQ?t=3186) $k=0$：看過 `1011000111`（六個 1、四個 0），下一個是 0 的機率 $\frac4{10}$；再下一個也是 0 呢？學生答 $\frac5{11}$ [▶ 53:46](https://youtu.be/B8ucNShRwjQ?t=3226)。

> ⚠️ 逐字稿缺字 [▶ 53:46](https://youtu.be/B8ucNShRwjQ?t=3226)：字幕「the last symbol will increase the count of 0's and increase the count of 1's」，應為「增加 0 的計數和總數」。

【課本補充】§13.2（書頁 433–436）就是這個「計數 + 1」的估計：看過 $i$ 個位元、其中 $k_i$ 個 1，預測下一個是 1 的機率 $\frac{k_i+1}{i+2}$（式 13.44，**Laplace 估計**，等於對 Bernoulli 參數取均勻先驗的貝氏後驗）。用它做算術編碼，整條序列的碼長只比「事先知道參數 $k/n$ 時的最佳碼長 $nH(k/n)$」多約 $\frac12\log n$ 位元（式 13.40），而且不需要對來源做任何假設。

---

## 11. 實驗：福爾摩斯小說

[▶ 53:46](https://youtu.be/B8ucNShRwjQ?t=3226) 用 SCL 跑《巴斯克維爾的獵犬》（`L9_ann.pdf` p.44–46，位元／位元組）：

| 壓縮器 | 位元／位元組 |
|---|---|
| 0 階（iid） | 4.26 |
| 1 階 | 3.34 |
| 2 階 | 2.87 |
| 3 階 | 3.10 |
| gzip | 2.78 |
| bzip2 | 2.05 |

【課堂討論】[▶ 54:20](https://youtu.be/B8ucNShRwjQ?t=3260) 為什麼 0 → 2 階變好？如果輸入真的沒有相依，加大 context 會變好嗎？不會 [▶ 54:54](https://youtu.be/B8ucNShRwjQ?t=3294)。英文前兩個字母能幫忙預測下一個，所以階數越高越好。

**為什麼 3 階反而變差？** [▶ 54:54](https://youtu.be/B8ucNShRwjQ?t=3294) 提示：檔案只有幾百 KB。在一個小檔案裡，長度 4 的特定序列會出現很多次嗎？

[▶ 55:34](https://youtu.be/B8ucNShRwjQ?t=3334) 資料太少，計數根本累積不起來。1 階要記 $(x_i,x_{i+1})$，2 階要記三個一組……計數陣列大小 [▶ 56:10](https://youtu.be/B8ucNShRwjQ?t=3370)

$$|\mathcal X|^{k+1}$$

隨階數指數成長。資料少時計數非常稀疏，大部分是 0，大部分組合根本沒看過，預測器很爛 [▶ 56:47](https://youtu.be/B8ucNShRwjQ?t=3407)。例：看到 THIN，如果過去沒看過 THIN，就沒有模型。

[▶ 57:21](https://youtu.be/B8ucNShRwjQ?t=3441) gzip、bzip2 打敗了這些模型，下一講會講它們。

**$k$ 階模型的限制** [▶ 57:21](https://youtu.be/B8ucNShRwjQ?t=3441)（`L9_ann.pdf` p.47）：

- 慢，記憶體隨 $k$ 指數成長。
- $k$ 大時計數非常稀疏，效果變差。
- **無法利用相似 context** [▶ 58:03](https://youtu.be/B8ucNShRwjQ?t=3483)：`thi` 和 `Thi` 只差大小寫，聰明的模型知道兩者有關；笨的 $k$ 階模型把它們當完全不同的 context，各自計數。

[▶ 58:42](https://youtu.be/B8ucNShRwjQ?t=3522) 雖然說了很多壞話，它們仍在特定情境下被使用；簡單、可以試。【投影片補充】`L9_ann.pdf` p.47：儘管有這些限制，context-based 模型仍常被用在**前處理後**（LZ、BWT 等）的熵編碼階段。

---

## 12. 兩段式的陷阱：模型開始記住資料（MDL）

### 12.1 經驗條件熵越來越小

[▶ 58:42](https://youtu.be/B8ucNShRwjQ?t=3522) 如果用兩段式，可以直接從資料算經驗條件熵（`L9_ann.pdf` p.48）：

| 階 | 自適應 | 經驗條件熵 |
|---|---|---|
| 0 | 4.26 | 4.26 |
| 1 | 3.34 | 3.27 |
| 2 | 2.87 | 2.44 |
| 3 | 3.10 | 1.86 |

0 階兩者很近，階數越高差距越大。兩段式看起來能做得非常好？[▶ 59:17](https://youtu.be/B8ucNShRwjQ?t=3557)

【課堂討論】[▶ 59:17](https://youtu.be/B8ucNShRwjQ?t=3557) 3 階模型：整本書裡 `thi` 只出現一次，後面接 S。編那個 S 要幾位元？學生答：**0** [▶ 1:00:08](https://youtu.be/B8ucNShRwjQ?t=3608)。只看過一次，分布是確定的。可是解碼器怎麼知道？

[▶ 1:00:46](https://youtu.be/B8ucNShRwjQ?t=3646) **模型開始存資料了。** 極端情況：長度 1000 的文字用 1000 階模型，整份輸入機率 1、其他都是 0，「0 位元就編完」[▶ 1:01:32](https://youtu.be/B8ucNShRwjQ?t=3692)。把整本福爾摩斯小說放進模型，壓縮檔是 0 位元，解碼器「本來就知道」是福爾摩斯小說 [▶ 1:02:07](https://youtu.be/B8ucNShRwjQ?t=3727)。這很蠢。

[▶ 1:02:07](https://youtu.be/B8ucNShRwjQ?t=3727) 階數越高，「知道經驗分布」就越接近「把資料存在模型裡」；而模型大小隨階數指數成長，最後模型會壓過一切。所以**必須算進存模型的成本**。這也是實務上常偏好自適應的原因之一（不用兩次掃描、不用存模型）[▶ 1:02:41](https://youtu.be/B8ucNShRwjQ?t=3761)。

【投影片補充】`L9_ann.pdf` p.49：極端時就是一個長度 $|\text{data}|$ 的 context，模型就是資料本身。

### 12.2 最小描述長度

[▶ 1:02:41](https://youtu.be/B8ucNShRwjQ?t=3761) 模型越複雜，壓縮後的資料越小（模型開始學到資料），但模型大小指數成長。真正在乎的是**總大小 = 模型大小 + 壓縮後資料大小**，最佳點在中間某處 [▶ 1:03:14](https://youtu.be/B8ucNShRwjQ?t=3794)。

> **最小描述長度原則**（Minimum Description Length, MDL）：最小化「模型大小 + 給定模型後的壓縮大小」。由 Rissanen 提出 [▶ 1:03:14](https://youtu.be/B8ucNShRwjQ?t=3794)。

【口頭】[▶ 1:03:14](https://youtu.be/B8ucNShRwjQ?t=3794) Rissanen 在壓縮理論做了很多有趣的工作，也是算術編碼的發明人之一。

【課本補充】§14.13（書頁 500–501）用 Kolmogorov 複雜度講 MDL：選擇使「描述模型的位元 + 用模型描述資料的位元」最小的模型。

---

## 13. 進階模型：PPM、CTW、NNCP、CMIX

[▶ 1:03:53](https://youtu.be/B8ucNShRwjQ?t=3833) 很好的期末專題題目。$k$ 階自適應已在 SCL 裡實作 [▶ 1:03:53](https://youtu.be/B8ucNShRwjQ?t=3833)。

- **解決計數稀疏** [▶ 1:04:29](https://youtu.be/B8ucNShRwjQ?t=3869)：**PPM**（Prediction by Partial Matching）、**CTW**（Context Tree Weighting）。想法：也許沒看過 TH，但看過 HI，或至少看過 I，那就混合各種長度的 context，別把已有的資訊丟掉。
- **進階預測模型** [▶ 1:04:29](https://youtu.be/B8ucNShRwjQ?t=3869)：
  - 神經網路：NNCP、tensorflow-compress、DZip [▶ 1:05:04](https://youtu.be/B8ucNShRwjQ?t=3904)。過去的符號 → 神經網路預測器 → 算術編碼；解碼對稱。可以兩段式，也可以自適應地一直更新網路。
  - 集成方法：**CMIX** [▶ 1:05:53](https://youtu.be/B8ucNShRwjQ?t=3953)。幾千個模型：看最後一個位元、最後兩個、三個位元、前一個字、前一個字的首字母、末字母、這是不是句子的第一個字……再用一個神經網路把它們**混合**成一個機率 [▶ 1:06:34](https://youtu.be/B8ucNShRwjQ?t=3994)。
  - 資源：Matt Mahoney 的線上教科書（他做過很多重型壓縮器）[▶ 1:05:04](https://youtu.be/B8ucNShRwjQ?t=3904)。
- 這些通常是最強的壓縮器，但對很多實際應用太慢。

【投影片補充】`L9_ann.pdf` p.51：**DeepZip** 是兩段式：先在資料上訓練模型，再用它壓縮，模型存進壓縮檔。**NNCP** 是邊看資料邊定期更新神經網路預測器。

[▶ 1:06:34](https://youtu.be/B8ucNShRwjQ?t=3994) 去年 IT Forum 有 CMIX 作者的演講。

### 13.1 文字壓縮的歷年進展

[▶ 1:06:34](https://youtu.be/B8ucNShRwjQ?t=3994)（Pulkit 做的圖，`L9_ann.pdf` p.53，位元／字元）

| 方法 | 位元／字元 |
|---|---|
| 均勻 iid 字元 | 4.7 |
| 只考慮字母頻率 | 4.14 |
| 考慮字頻 | 2.62 |
| gzip（LZ77 + Huffman） | 2.58 |
| zstd（LZ77 + ANS） | 1.73 |
| bzip2（BWT + Huffman） | 2.03 |
| 7zip（LZMA2 + range coder） | 1.43 |
| Shannon 的估計（1 位受試者、100 個片語的上界） | 1.3 |
| Cover & King（用賭博做的漸近上界） | 1.3 |
| Ren, Takahashi, Tanaka-Ishii（大規模 Shannon 實驗） | 1.22 |
| CMIX（依 context 的模型集成） | 0.89 |
| NNCP（Transformer + 算術編碼） | 0.87 |

[▶ 1:07:12](https://youtu.be/B8ucNShRwjQ?t=4032) 最右邊的 CMIX 和 NNCP 已經**低於 Shannon 估計的英文熵率**。【口頭】[▶ 1:07:45](https://youtu.be/B8ucNShRwjQ?t=4065) 人類產生的文字總共只有幾 TB，不是最大的資料來源，但大家就是好奇文字能壓到多好。

---

## 14. LLM 壓縮

### 14.1 跳出 MDL 的設定

[▶ 1:07:45](https://youtu.be/B8ucNShRwjQ?t=4065) （講者說沒聽前面的話，至少聽這段。）好預測 = 好壓縮，而現在最強的預測器是 **LLM**。這是今年新加的內容。

[▶ 1:08:19](https://youtu.be/B8ucNShRwjQ?t=4099) **暫時忘掉 MDL**：不管存模型的成本，拿最強的預測器來，幾 GB、幾百 GB 都沒關係。一般情況這沒用，模型要存哪？跟檔案一起存就沒意義。

【課堂討論】[▶ 1:08:53](https://youtu.be/B8ucNShRwjQ?t=4133) 什麼情況下用超大模型當預測器是可以的？問題在要存模型，**真的要嗎？** [▶ 1:09:26](https://youtu.be/B8ucNShRwjQ?t=4166) 也許有一天每個人的手機、筆電上都有 GPT-4，大家假設彼此都有那個大模型，都用它來壓縮、互傳。

什麼時候有用（`L9_ann.pdf` p.55）：

1. 有大量同類型資料，又負擔得起在每個解壓縮端部署模型。
2. 了解壓縮的極限（文字預測能多好、熵率估計）[▶ 1:10:00](https://youtu.be/B8ucNShRwjQ?t=4200)。
3. 在壓縮課上玩得開心（講者說他是為了這個）。

[▶ 1:10:00](https://youtu.be/B8ucNShRwjQ?t=4200) LLM 本來就是訓練成預測器，損失函數是交叉熵（或 perplexity $=2^{\text{交叉熵}}$），所以它們**實際上就是在被訓練成壓縮器**。

### 14.2 實驗一：2023 年的小說

[▶ 1:10:33](https://youtu.be/B8ucNShRwjQ?t=4233) 用 NNCP 作者的新工作 **ts_zip**（用 LLM 壓縮文字），可以下載任何模型來壓。【投影片補充】`L9_ann.pdf` p.56：用的是 rwkv_169M 和 rwkv_430M 兩個模型。

結果（848 KB 的 2023 年英文小說，壓縮位元／位元組，`L9_ann.pdf` p.57；context 長度以 token 計）：

| 方法 | 位元／位元組 |
|---|---|
| 2 階自適應算術編碼 | 3.04 |
| bzip2 | 2.03 |
| 小模型，context 16 | 1.806 |
| 中模型，context 16 | 1.759 |
| 小模型，context 512 | 1.186 |
| 中模型，context 512 | 1.073 |

[▶ 1:11:09](https://youtu.be/B8ucNShRwjQ?t=4269) 只看最後 16 個 token 時比 bzip2 好但不驚人；中模型比小模型好一點。**長 context 時才真的發光**：LLM 能看很長的過去做預測。[▶ 1:11:42](https://youtu.be/B8ucNShRwjQ?t=4302) 給夠長的 context，就低於 Shannon 的估計，非常接近 CMIX、NNCP。而且這只是 4.3 億參數的小模型，GPT 是幾百億以上。

> 更好的模型 → 更好的壓縮；更多 context → 更好的壓縮（不計模型大小）。[▶ 1:11:42](https://youtu.be/B8ucNShRwjQ?t=4302)

### 14.3 實驗二：巴利文【課堂討論】

[▶ 1:12:17](https://youtu.be/B8ucNShRwjQ?t=4337) 巴利文（Pali，古印度語言，類似梵文），轉寫成羅馬字母（`L9_ann.pdf` p.58）：

| 方法 | 位元／位元組 |
|---|---|
| 2 階自適應算術編碼 | 2.66 |
| gzip | 2.11 |
| bzip2 | 1.71 |
| 小 LLM | 2.41 |
| 中 LLM | 2.19 |

LLM 連 gzip 都贏不了。為什麼？學生答：模型不是為這種特定分布訓練的 [▶ 1:12:52](https://youtu.be/B8ucNShRwjQ?t=4372)。講者：LLM 的訓練資料（尤其小模型）主要是英文、限定的語料。gzip、bzip2、2 階算術編碼不對資料做任何假設，任何資料只要樣本夠多都能從資料學分布，某種意義上是**通用的** [▶ 1:13:25](https://youtu.be/B8ucNShRwjQ?t=4405)；LLM 假設資料來自某個分布，資料不是那樣時就變差。

### 14.4 實驗三：Llama-13B 與訓練資料汙染

[▶ 1:13:25](https://youtu.be/B8ucNShRwjQ?t=4405) Kedar 用更大的 Llama 13B（4 位元量化）做的實驗（`L9_ann.pdf` p.59–60）：

| 資料 | context 10 | context 50 | context 512 |
|---|---|---|---|
| 2023 年短篇小說 | 1.228 | 1.027 | 0.874 |
| 福爾摩斯 | 1.433 | 0.542 | **0.200** |

[▶ 1:14:03](https://youtu.be/B8ucNShRwjQ?t=4443) 短篇小說：context 越長越好，0.874 比前面的好，因為模型更強。福爾摩斯卻到 **0.2**，比平常約 1 位元好 5 倍。

【課堂討論】[▶ 1:14:37](https://youtu.be/B8ucNShRwjQ?t=4477) 為什麼？要嘛柯南·道爾的英文比現代小說簡單很多，要嘛有別的原因。Llama 怎麼做出來的？學生答：用了舊書 [▶ 1:15:12](https://youtu.be/B8ucNShRwjQ?t=4512)。講者：對，還有 Wikipedia 等。福爾摩斯大概在訓練資料裡，模型**記住**了一部分 [▶ 1:15:45](https://youtu.be/B8ucNShRwjQ?t=4545)。所以評估時要小心，這就是為什麼前面都用 2023 年的文字（假設不在最近發布的模型的訓練資料裡）。

### 14.5 小結

[▶ 1:15:45](https://youtu.be/B8ucNShRwjQ?t=4545)（`L9_ann.pdf` p.61）

- 結果驚人，把文字壓縮推到極限。
- 小心**模型與資料不匹配**（巴利文）和**訓練資料重疊**（福爾摩斯）[▶ 1:16:21](https://youtu.be/B8ucNShRwjQ?t=4581)。
- 現在很慢、很吃計算；但小模型在 GPU 上還算快，未來某些應用可能真的會用（硬體加速）。

【口頭】[▶ 1:16:54](https://youtu.be/B8ucNShRwjQ?t=4614) Pulkit 補充：機器學習要小心**過擬合**；但對壓縮而言，如果模型過擬合到你要壓的資料、而模型又是兩邊共享的，那反而是好事 [▶ 1:17:29](https://youtu.be/B8ucNShRwjQ?t=4649)。實務上難在需要越來越大的模型。Shubham：要把福爾摩斯小說傳給別人，模型記住它反而有幫助；LLM 厲害在記住了大量過去，卻在最新資料上也泛化得很好 [▶ 1:17:29](https://youtu.be/B8ucNShRwjQ?t=4649)。

### 14.6 實用小技巧與資源

[▶ 1:18:06](https://youtu.be/B8ucNShRwjQ?t=4686)

- Kedar 的 notebook：示範預測下一個 token、怎麼壓縮。
- [▶ 1:18:50](https://youtu.be/B8ucNShRwjQ?t=4730) **評估時常常根本不做算術編碼**，直接算 $\sum\log\frac1{\hat P}$，因為算術編碼只多約 2 位元。要知道壓縮器（預測器）表現多好，算 log loss 就夠了。
- ts_zip（bellard.org）；DeepMind 的論文 **〈Language Modeling Is Compression〉** [▶ 1:18:50](https://youtu.be/B8ucNShRwjQ?t=4730)（arXiv 2309.10668），學完這門課、懂一點 LLM 就看得懂整篇。

[▶ 1:19:29](https://youtu.be/B8ucNShRwjQ?t=4769) 下一講：LZ77，以及無損壓縮的實務。

---

## 15. 一頁速查表

### context-based 算術編碼

- 每一步用 $\hat P(u_i\mid u_1,\dots,u_{i-1})$ 切區間。
- 總位元數 $\approx\sum_i\log_2\frac1{\hat P(u_i\mid u^{i-1})}$（= 交叉熵 / log loss）。
- 已知 1 階 Markov：$\frac1n\mathbb{E}[\text{位元}]=\frac1nH(U_1)+\frac{n-1}nH(U_2\mid U_1)\to H(U_2\mid U_1)$。**關鍵一步**：$\log$ 乘積拆成和，平穩讓每項相等。
- **更好的預測 = 更好的壓縮**；壓縮器 ↔ 預測器：$\hat P(x^n)\approx2^{-l}$。

### 解碼與自適應

| 規則 | 理由 |
|---|---|
| 解碼器要有完全相同的模型（含初始化） | 機率一不同，區間就不同，之後全壞 |
| 先編碼 $u_i$，再用 $u_i$ 更新 | 解碼器解出 $u_i$ 之前不知道它 |
| 任何符號機率 $>0$ | $\log\frac10=\infty$ |

### 兩段式 vs. 自適應

| | 兩段式 | 自適應 |
|---|---|---|
| 存模型 | 要 | 不用 |
| 串流 | 不行 | 可以 |
| 統計量變動 | 學到混合 | 能跟上 |
| 起步 | — | 一開始較差 |

### $k$ 階自適應

- $\hat P(x\mid\text{前 }k\text{ 個})=\frac{c(\text{前 }k,x)}{\sum_{x'}c(\text{前 }k,x')}$，計數從 1 開始。
- 計數陣列 $|\mathcal X|^{k+1}$ ⇒ 資料少時稀疏，$k$ 太大反而變差（福爾摩斯：2 階 2.87，3 階 3.10）。
- 解法：PPM、CTW 混合不同長度 context；NNCP、CMIX 用神經網路。

### MDL

總大小 = 模型 + 資料；高階兩段式「經驗條件熵」會騙人（模型記住資料）。

### LLM 壓縮

- 更大模型、更長 context → 更好（2023 小說：bzip2 2.03 → 中模型 ctx512 1.073）。
- 陷阱：資料不在訓練分布（巴利文輸給 bzip2）、資料在訓練集（福爾摩斯 0.2）。

---

## 16. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| gzip、bzip2 為什麼贏過 $k$ 階模型；通用壓縮 | 第 10 集 LZ77 |
| 前處理（LZ、BWT）後再用 context 模型熵編碼 | 第 10 集實務 |
| 用神經網路預測機率 + 熵編碼 | 第 16 集學習式影像壓縮 |
| 自適應、編解碼器狀態同步 | 第 14–18 集（影像、影片編碼器的自適應算術編碼） |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **算術編碼每一步改用預測器給的條件機率切區間，總碼長就是 $\sum\log\frac1{\hat P(u_i\mid\text{過去})}$，也就是機器學習的交叉熵損失：更好的預測就是更好的壓縮。沒有模型時可以兩段式（要存模型）或自適應（邊壓邊學，編解碼器必須同步、不能給 0 機率）。$k$ 階計數模型在資料少時會因計數稀疏而變差；兩段式高階模型則會偷偷把資料存進模型（MDL）。LLM 當預測器能把英文壓到約 1 位元／位元組以下，但要小心資料不在訓練分布或剛好在訓練集裡。**

---

*筆記依據 Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 9 錄影逐字稿（人工字幕，1:19:52）、投影片 L9_ann 與 Cover & Thomas《Elements of Information Theory》2nd ed. §13.2–13.3、§14.13 整理。*
