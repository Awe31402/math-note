---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 30
lecture: Lec 12-0 Spectrum Estimation — Ergodicity based on Shift-invariant Event
date: 待補
video: https://youtu.be/yzb2fvca0qo
notes: 本集大部分是老師補充（課本沒有）；Papoulis & Pillai 4th ed. §12-1 開頭（p. 523）與 Example 12-1、12-2（p. 524）
---

# 第 30 集 · Lec 12-0：遍歷性 (ergodicity) 的原始定義——shift-invariant 事件、遍歷集合、機率非 0 即 1、遍歷 vs 平穩、Birkhoff–Khinchin 定理、大數法則才是重點 [▶ 影片](https://youtu.be/yzb2fvca0qo)

← 上一集：[29](29-wold-decomposition-intuition-example-discrete-bispectrum.md) ｜ [總目錄](README.md) ｜ 下一集：[31](31-mean-ergodic-slutsky-theorem-sufficient-conditions-spectral.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 30 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（53:24，whisper large-v3-turbo）＋ Papoulis §12-1（pp. 523–524）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「ergodic」→「Ergatic／ergotic／erganic／ergonic／耳嘎點／爾嘎底／Ergatik／ergardic」，「ergodicity」→「ergoticity／ergaticity」，「shift invariant」→「shift invariant」，「alphabet」→「alphabet」，「實數」→「時數」，「Borel σ-field」→「boreal field／Barrell Sigma Field」，「聯集」→「連擊／連級」，「transient state」→「trancient state／trension」，「暫態」→「站態」，「pseudo-inverse」→「Pseudo-inverse」，「遍歷性」→「片力性／騙力性／片立性」，「各態遍歷性」→「个态片力性」，「ensemble average」→「ensemble average」，「converge to a constant」→「Converse to a Constant」，「穩態」→「穩泰」，「Birkhoff」→「Berkhoff」，「Khinchin」→「Kinchen／kerchief」，「pointwise ergodic theorem」→「Point-wise Ergotic Theorem」，「law of large numbers」→「law of large number」，「大數法則」→「大樹法則／大術法則」，「Kolmogorov」→「Komagorov／Comagrove」，「Chebyshev」→「Chevyshev／柴皮學部」，「Gray & Davisson」→「Lee Davidson／Davidson」，「i.i.d.」→「RID」，「hidden Markov」→「hidden Markov chain／hidden mark of」，「Lempel–Ziv」→「lamp zip」，「ergodic decomposition theorem」→「Ergotic Decomposition Theorem」，「mixture」→「minator linear mixture」，「Shannon」→「Shannon」，「information theory」→「消息论／Information Theory」，「線性組合」→「信心組織」。以下一律用正確的字。

> **本集定位**：第 12 章「頻譜估計」——第 11 章已經轉到頻譜分析，第 12 章自然要直接在頻譜上做估計。開頭老師補充課本沒有的內容：有同學寫 email 請老師介紹 ergodic，老師特別做了二三十張投影片。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼 ergodic 容易混淆](#1-為什麼-ergodic-容易混淆)
- [2. 單邊隨機過程與 Borel σ-field](#2-單邊隨機過程與-borel-σ-field)
- [3. Shift-invariant 事件](#3-shift-invariant-事件)
- [4. 「T-invariant 群組」與暫態](#4-t-invariant-群組與暫態)
- [5. Pseudo-inverse 與遍歷集合](#5-pseudo-inverse-與遍歷集合)
- [6. 物理的遍歷性：時間平均 = 系綜平均](#6-物理的遍歷性時間平均--系綜平均)
- [7. 遍歷隨機過程的原始定義](#7-遍歷隨機過程的原始定義)
- [8. 遍歷 ≠ 平穩](#8-遍歷--平穩)
- [9. Birkhoff–Khinchin 逐點遍歷定理](#9-birkhoffkhinchin-逐點遍歷定理)
- [10. 為什麼很少看到「非平穩遍歷」](#10-為什麼很少看到非平穩遍歷)
- [11. 混淆的來源：把結果當定義](#11-混淆的來源把結果當定義)
- [12. 例：平穩但不遍歷](#12-例平穩但不遍歷)
- [13. 遍歷分解定理](#13-遍歷分解定理)
- [14. 結論：重點是大數法則](#14-結論重點是大數法則)
- [15. 一頁速查表](#15-一頁速查表)
- [16. 與後續集數的連結](#16-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 混淆、定義的歷史 | [▶ 00:00](https://youtu.be/yzb2fvca0qo?t=0) | 無（【口頭】） |
| Shift-invariant 事件、遍歷集合 | [▶ 04:04](https://youtu.be/yzb2fvca0qo?t=244) | 無 |
| 遍歷隨機過程、遍歷 vs 平穩 | [▶ 23:23](https://youtu.be/yzb2fvca0qo?t=1403) | 無 |
| Birkhoff–Khinchin、混淆 | [▶ 33:34](https://youtu.be/yzb2fvca0qo?t=2014) | 無 |
| 平穩不遍歷的例子、分解定理 | [▶ 43:14](https://youtu.be/yzb2fvca0qo?t=2594) | 類似 Example 12-2，p. 524 |
| 大數法則 | [▶ 50:25](https://youtu.be/yzb2fvca0qo?t=3025) | 無 |

> 本集幾乎全部是【口頭】補充，以下不再逐段標。

---

## 1. 為什麼 ergodic 容易混淆

[▶ 00:32](https://youtu.be/yzb2fvca0qo?t=32) 老師說：剛拿到博士回來時看到 ergodic process，一直很疑惑，還寫 email 問指導教授這個字的字根是什麼意思，他也沒解釋清楚。後來經過時間慢慢整理才了解。

- 對一件事不理解時，**需要時間**。
- 混淆的原因：一個名詞每個人講法不一樣（就像課本很多定義每個人不同）。
- 做法：做歷史分析——這個字最早出現時，想法是什麼？後來為什麼混淆？

所有 stationary 都有一個字眼：**shift invariant**（shift 指時間平移，不隨時間改變 = 穩態）。統計學家對不隨時間改變的現象特別有興趣。ergodic 一開始的想法也跟 shift invariant 有關。關鍵字：**shift-invariant event**。

---

## 2. 單邊隨機過程與 Borel σ-field

[▶ 02:02](https://youtu.be/yzb2fvca0qo?t=122)

- **雙邊** (two-sided)：$\dots,X_{-2},X_{-1},X_0,X_1,X_2,\dots$，兩邊無限延伸。
- **單邊** (one-sided)：$X_1,X_2,X_3,\dots$——實作上一定從某個時間開始收值，比較實際；但一半沒了，常常出問題。

**字母集** (alphabet)：所有可能出現的值（丟銅板：正、反；丟骰子：1–6）。隨機過程一定是實數（第 9 章），所以正、反要轉成 $\pm1$。

**σ-field**（第 2、9 集）：所有可能的序列分門別類成集合，需要 σ-field 才合理：
1. 空集合、全集在裡面；
2. $A$ 在裡面 ⇒ $A^c$ 在裡面；
3. 可數個 $A_1,A_2,\dots$ 在裡面 ⇒ 聯集在裡面。

**Borel σ-field**：在實數世界，從**區間**出發（$[-1,1]$、$[1,1.5]$……），所有區間可數個的聯集、交集構成的空間。老師說這些都是嚇人的名詞，其實沒那麼特別，只是讓體系完整。

---

## 3. Shift-invariant 事件

[▶ 05:36](https://youtu.be/yzb2fvca0qo?t=336)

**事件** (event)：一個我關心的集合。例：丟銅板三次，「兩正一反」= {正正反, 正反正, 反正正}。

**時間平移 $T$**（left shift）：把明天移到今天、後天移到明天——**砍掉第一個分量** (chopping the first component)：
$$T(x_1,x_2,x_3,\dots)=(x_2,x_3,x_4,\dots).$$

> **T-invariant 事件**（對 left shift）：$TA\subseteq A$。
> 砍掉一段之後，**還落在原來的集合裡、跑不出去**（是子集合，不一定相等）。

**直觀**：從今天開始觀察一堆資料（某人的行為、心跳、帳戶），把今天的資料殺掉、從明天開始記錄——從資料本身完全看不出來。像一個**封閉的世界**，不跟外界交流。物理觀察常需要封閉空間；ergo 有「很自我」的意思。（1950 年代之前的出發點確實是這件事。）

**例 12-1**（投影片編號）：$A=\{1111\cdots,\ 0111\cdots,\ 00111\cdots\}$（一旦打開就永遠開；前三個是 0 的不關心）。砍一個：$1111\cdots\to1111\cdots$，$0111\cdots\to1111\cdots$，$00111\cdots\to0111\cdots$。結果只剩兩個，是 $A$ 的子集合 ⇒ shift-invariant。再砍還在裡面，永遠出不去。

**性質**：$TA\subseteq A$ ⇒ $T^2A\subseteq TA$（$T$ 保持包含關係）。**砍越多越封閉**、越往裡面。

---

## 4. 「T-invariant 群組」與暫態

[▶ 11:43](https://youtu.be/yzb2fvca0qo?t=703)

**例**：$100100100\cdots$ 砍一個 → $001001\cdots$，再砍 → $010010\cdots$，再砍 → 回到 $100100\cdots$。

要形成 shift-invariant 集合，**原來集合要把所有被砍過的版本都納進來**。這三個要麼**全部在裡面**、要麼**全部在外面**，不能一個在裡面兩個在外面——很強的綁定。

- 老師叫它「T-invariant group」（加引號：不是文獻上的標準名詞），而且是**不可分割的** (indecomposable)。
- 比喻：三個死黨要加選同一門課，找老師說「要加就一次加我們三個，不然都不要加」——老師覺得很怪。好朋友要好到這種程度。

**暫態** (transient state)：單邊序列才有的問題。電路學：開機瞬間有暫態脈衝，慢慢才穩定。例 12-1 的三個元素裡，$00111\cdots$ 砍兩次就不見了（不會永遠存在）；只有 $1111\cdots$ 怎麼砍都永遠穩定存在。

---

## 5. Pseudo-inverse 與遍歷集合

[▶ 16:17](https://youtu.be/yzb2fvca0qo?t=977)

**問題**：砍掉第一個可能是**多對一**（$100\cdots$ 和 $000\cdots$ 砍完都是 $00\cdots$），沒有反函數。

**Pseudo-inverse**（假想的反函數）：$T^{-1}$ 把一個對回所有可能——把今天補回來，所有可能的值都補進去。0/1 序列就是一對二，0/1/2 序列就是一對三。

老師說有本書這樣做：1991 年的《Ergodic Theory of Discrete Sample Paths》。⚠️ 待確認：這本書一般記為 P. C. Shields, AMS 1996；老師說 1991。

> **遍歷集合** (ergodic set)：$T^{-1}A=A$。
> 對集合裡所有元素都補回去，補完跟原來相等。

- 這 imply $TA=A$（兩邊都加 $T$）：全部砍掉也跟原來一樣。
- 時間從今天移到明天、後天、昨天，**整個集合的元素完全沒改變**。
- **沒有暫態**（例 12-1 不是遍歷集合，因為有暫態）。
- 其實應該叫 stationary set，但當時沒有這樣用。像**一灘死水**。

老師的比喻：時間轉移到明年、後年、去年，整個（集合）看起來完全不變——就像有些人希望年紀大時臉上都沒變化。

---

## 6. 物理的遍歷性：時間平均 = 系綜平均

[▶ 20:19](https://youtu.be/yzb2fvca0qo?t=1219)

**物理的遍歷性**（各態遍歷性）：一個力學體系從任何初始狀態運動，時間夠長，**所有狀態都會被經歷一次**——不會遺漏、也不會多。

- 原因：封閉體系出不去；$T$（時間）一直切、一直循環；是不可分割的群組。
- 結論：**無限長時間的時間平均 = 系綜平均** (ensemble average)。例如集合有 8 個狀態，經過時間 8 個狀態各經歷一次——根本不用看時間，把所有可能狀態平均就對了。
- 比喻：考試次數夠多，全班 30 人每人輪流當第一名，考 30 次每次不同人第一。完美的世界，但好像沒什麼趣味。在這個體系裡，**時間已經不重要了**。

**雙邊序列**：比較簡單，沒有反函數不存在的問題——左移、右移，兩個定義完全等價。

---

## 7. 遍歷隨機過程的原始定義

[▶ 23:23](https://youtu.be/yzb2fvca0qo?t=1403)

> **遍歷隨機過程**（最早的定義）：對每個遍歷集合 $A$，
> $$P(A)=0\ \text{或}\ 1.$$

- 三個死黨要麼都出現在這門課、要麼都不出現，沒有中間值（不會只出現兩個或一個）。
- 物理體系若是遍歷的：所有狀態要麼都可能出現，要麼都不可能。

> ⚠️ 老師在第 32 集更正：本集用的例子集合其實**不是**遍歷集合——遍歷要用反向 $T^{-1}A=A$ 判斷，老師當時用正向推。以下**不是逐字稿內容**，是依定義推論的：$\{100100\cdots,001001\cdots,010010\cdots\}$ 在 $001001\cdots$ 前面補 0 得 $0001001\cdots$，不在集合裡，所以 $T^{-1}A\ne A$。不過「機率非 0 即 1 ⇒ 平均收斂到常數」的推理方向不受影響。詳見[第 32 集](32-ergodicity-motivation-measurement-correction.md)。

**重要結果：樣本平均收斂到一個常數**（不是隨機變數）。
- 例：$\{100\cdots,001\cdots,010\cdots\}$ 是遍歷集合，機率不是 1 就是 0。若是 1：每兩個 0 出現一個 1，每個序列的平均都是 $\frac13$ ⇒ 平均一定趨近 $\frac13$，沒有別的可能。
- 把平均是 0.1 的全部包在一起是一個遍歷集合，平均 0.2 的是另一個……這些集合每個機率非 0 即 1，總和是 1 ⇒ **只有一個機率是 1**。所以平均一定是一個**絕對穩定的常數**——由定義來的。

---

## 8. 遍歷 ≠ 平穩

[▶ 27:28](https://youtu.be/yzb2fvca0qo?t=1648)

**觀念一**：stationary 和 ergodic 是**完全不同的定義**（雖然都跟時間有關）。所以確實存在**遍歷非平穩**過程，也存在**平穩非遍歷**過程。
- ergodic：關鍵是**事件**——不隨時間改變的事件，機率是 0 或 1。
- stationary：過程的統計性質（一、二、三階動差、分布）不隨時間改變；沒牽涉到事件。

**觀念二**：ergodic 的結果是**所有樣本平均收斂到一個常數** (converge to a constant)。定義完了，這就是百分之百的結果。

**為什麼有的論文假設 ergodic（不一定 stationary）**：觀察河流流速、PM2.5 濃度隨時間變化，要做平均。假設 ergodic，整年平均確實是一個常數，可以估計。
- **只假設 stationary 不保證這件事**：時間平均可能收斂到一個**隨機變數**——例如平均流速 3.2 或 2.4，機率各 $\frac12$。那就量不準（有時真的平均大、有時小）。
- 比喻：骰子若是 ergodic 就永遠穩定是 3 點，很好預測；若只是 stationary（1–6 點機率都 $\frac16$），還是可以預測，但有機率對、有機率錯。

**兩個都成立（stationary ergodic）**：保證時間平均趨近**期望值**。

**ergodic 收斂的常數不一定是期望值**（老師說這個觀念能釐清就值回票價）[▶ 30:29](https://youtu.be/yzb2fvca0qo?t=1829)：
- $\{100\cdots,001\cdots,010\cdots\}$ 三個加起來機率是 1，但沒說各自多少。
- 分配 $\frac13,\frac13,\frac13$：某個特定時間出現 1 的機率是 $\frac13$。
- 分配 $\frac12,\frac14,\frac14$：某個時間出現 1 的機率是 $\frac12$（第一個序列在那個時間是 1，其他是 0）。
- 都是遍歷的，時間平均都是 $\frac13$；但**特定時間的期望值不穩定**（有時高有時低）。
- 若 stationary ergodic，每個時間 0 和 1 的機率要一樣，三個就不能亂分配——要分配成特定機率，常數才會是期望值。

---

## 9. Birkhoff–Khinchin 逐點遍歷定理

[▶ 33:34](https://youtu.be/yzb2fvca0qo?t=2014) 不同的書寫法不同、很多作者寫得不對，但這個定理大家都寫得一樣：

> **逐點遍歷定理** (pointwise ergodic theorem, Birkhoff & Khinchin)：$X$ 是 **stationary**，則
> $$\frac1n\sum_{i=1}^{n}f(X_i)\to\text{一個隨機變數}.$$
> 若**再加上 ergodic**，則收斂到常數，而且是期望值：
> $$\frac1n\sum_{i=1}^{n}f(X_i)\to E\{f(X_1)\}.$$

- 先假設 stationary，再在 stationary 底下討論有沒有 ergodic。
- stationary 時收斂到的隨機變數：有很多可能的值，機率都知道而且穩定。
- $f$ 只是一個函數。這是 ergodic theory 最早的版本。

---

## 10. 為什麼很少看到「非平穩遍歷」

[▶ 35:05](https://youtu.be/yzb2fvca0qo?t=2105) 通訊論文常假設 source、channel 是 stationary 或 stationary ergodic，很少看到 ergodic non-stationary。原因：

1. **難分析**：定義要用遍歷集合，很不直接；機率非 0 即 1，不好延伸。
2. **實際上很難觀察到**：確認系統不穩但又是 ergodic，好像很怪。ergodic 有點 artificial——很少看到一個國家把自己鎖起來永遠不跟外面交流；歷史上看到鎖國，人家就會打進來。

既不好分析、實際上又不一定有用，就只剩數學上的觀點（還是有人做，因為封閉系統的現象蠻有趣，結果是收斂到常數）。所以 Birkhoff–Khinchin 先假設 stationary。

---

## 11. 混淆的來源：把結果當定義

[▶ 38:09](https://youtu.be/yzb2fvca0qo?t=2289) 原始定義不直觀，一般人不容易理解或接受。晚期的機率、統計書（尤其**工程**書）**把結果當作定義**：
> 「stationary 過程若時間平均收斂到常數，就叫 ergodic。」

糟糕的是：這從來不是原來的定義。但在整本書裡這樣定義好像也沒問題，因為 ergodic 最有用的部分就是這個性質。

**這其實是大數法則** (law of large numbers)：在什麼條件下，序列的平均會趨近一個常數。
- 老師在 advanced probability 課花很多時間講。每個人提自己的條件：Kolmogorov 大數法則、Chebyshev 大數法則……ergodic 也是一個條件。
- 「若 A 則 B」，把 B 當成 A 的定義，又不是 if and only if，就很混淆：照新定義，不是 stationary ergodic 就不符合大數法則——**不對**，大數法則非常廣。
- 資訊理論的基本定理（Shannon）分析下來要的都是**大數法則**：大數法則對，Shannon theory 就對。
- 正確圖像：ergodic 和 stationary 是不同定義，有交集；Markov 是另一個定義，也有交集；i.i.d. 在交集裡面，中間還有其他東西。

另一本書（⚠️ 待確認：老師沒說書名）也介紹了這件事：ergodic theorem 是原始定義的**結果**，晚期的書把它當定義。所以 80、90 年代的論文有人用舊定義、有人用新定義，甚至前半用舊、後半用新（作者自己也搞不清楚）。了解來龍去脈，就看得出作者要的是什麼。

---

## 12. 例：平穩但不遍歷

[▶ 43:14](https://youtu.be/yzb2fvca0qo?t=2594)

**Notion of ergodicity 整理**：ergodic 和 stationary 定義來源不同；照原始定義確實存在 stationary 但非 ergodic 的過程（新定義下就沒了）。

**例**：$A_n$、$B_n$ 都是 i.i.d. 的 0/1 序列（i.i.d. 是最強的：既 stationary、又 ergodic、又 Markov）。差別：$P(A_n=1)=\frac14$、$P(B_n=1)=\frac34$。$U$ 是另一個隨機變數，$P(U=1)=P(U=0)=\frac12$；$A,B,U$ 獨立。
$$X_n=\begin{cases}A_n,&U=1\\B_n,&U=0\end{cases}\qquad\text{即}\ X_n=UA_n+(1-U)B_n.$$

- **兩層、參數式**（parametric）：做語音的人喜歡 hidden Markov chain——參數又來自另一個隨機變數。你看到一堆 0101，不知道機率是 $\frac14$ 還是 $\frac34$，決定權在 $U$。這樣的資料很難壓縮。
- **$X_n$ 是 stationary**：每個時間 0/1 的機率都一樣。

**不是 ergodic**（反證）：若是 stationary ergodic，用 Birkhoff–Khinchin：
$$\frac1n\sum_{i=1}^{n}\mathbf 1[X_i=1]\to P(X_n=1).$$
（1 出現的次數除以總次數，例如 100 次出現 80 次就是 0.8。）由全機率：
$$P(X_n=1)=\frac12\cdot\frac14+\frac12\cdot\frac34=\frac12.$$
但實際上時間平均收斂到**隨機變數** $Y$：$Y=\frac14$ 或 $\frac34$，機率各 $\frac12$（不給分析）。違反定理 ⇒ 不是 ergodic。

**hidden 的 source 通常都不是 ergodic**。實際上常觀察到 hidden 現象（hidden Markov chain），所以 ergodic process 不容易單獨見到——要完全封閉的系統。

【課本補充】p. 524 Example 12-2 是同一種想法：$X(t)=X_1(t)+cX_2(t)$，$c$ 是 0 或 1（機率各 0.5），$\eta_T\to\eta_1$ 或 $\eta_1+\eta_2$，所以不是 mean-ergodic。Example 12-1：$X(t)=c$（隨機變數），$\eta_T=c$，若 $c\ne\eta$ 就不是 mean-ergodic。

---

## 13. 遍歷分解定理

[▶ 48:51](https://youtu.be/yzb2fvca0qo?t=2931) 我們喜歡做拆解（上一集）：看到一個東西就想拆，最小單位是什麼？

> **遍歷分解定理** (ergodic decomposition theorem)：任何 stationary 過程都是 stationary ergodic 過程的**混合** (mixture)。

（Gray & Davisson 的結果。）上面的例子就是：$X_n=UA_n+(1-U)B_n$，$A$、$B$ 都是 stationary ergodic，組合成 stationary 的 $X$。所以只要能分析 stationary ergodic，stationary 就可以分析。

**另一個有名的結果**：Markov 過程（一階：只跟前一刻有關；二階：前兩刻……）。階數 $k\to\infty$ 時，在某些條件下會趨近 stationary。後來在資料壓縮上用來證明 **Lempel–Ziv 碼**（平常用的 PKZIP 那些）為什麼壓縮得非常好。

---

## 14. 結論：重點是大數法則

[▶ 50:25](https://youtu.be/yzb2fvca0qo?t=3025) 老師編的資訊理論講義，**所有證明全部改成用大數法則**——因為發現重點就是大數法則。

- 網路流量能控制：因為有一萬個人在用，有大家共同的現象。
- 投票抽樣：抽一兩千人代表一百萬人的投票行為，也是大數法則。
- **stationary、ergodic 對大數法則都不是必要條件**。
  - Chebyshev 條件：variance 有限，大數法則就對（不用提 stationary、ergodic）。
  - Kolmogorov 條件：$\sum_i\frac{\mathrm{Var}(X_i)}{i^2}<\infty$，大數法則也對。
- 有暫態的過程也會收斂：開機時不穩，時間拉久一點就好了，只要暫態一下子就不見。

> **老師的個人觀點**：工程和應用上，主要關心的是**大數法則的現象**（樣本平均如何收斂到系綜平均）。不用太在意 stationary 或 ergodic——論文裡用它們，有時是為了證明方便、說明方便，真正要的是大數法則的行為。

---

## 15. 一頁速查表

| 名詞 | 定義／重點 |
|---|---|
| 時間平移 $T$ | 砍掉第一個分量（left shift） |
| shift-invariant 事件 | $TA\subseteq A$：砍了跑不出去；$T^2A\subseteq TA$ |
| pseudo-inverse $T^{-1}$ | 把今天補回來，所有可能都補（一對多） |
| 遍歷集合 | $T^{-1}A=A$（⇒ $TA=A$），沒有暫態 |
| 遍歷過程（原始定義） | 每個遍歷集合 $P(A)\in\{0,1\}$ |
| 結果 | 樣本平均收斂到**常數**（不一定是期望值） |
| stationary | 統計性質不隨時間變；時間平均收斂到**隨機變數** |
| stationary ergodic | 時間平均 → 期望值（Birkhoff–Khinchin） |

- 遍歷 ≠ 平穩：兩種定義獨立，有交集（i.i.d. 在裡面）。
- 平穩不遍歷例：$X_n=UA_n+(1-U)B_n$，時間平均 → $\frac14$ 或 $\frac34$，但 $P(X_n=1)=\frac12$。
- 遍歷分解：stationary = stationary ergodic 的混合。
- 工程書常把「時間平均收斂到常數」當成 ergodic 的定義——那其實是大數法則。

---

## 16. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 時間平均 vs 系綜平均 | 下一集起：§12-1 mean-ergodic、Slutsky 定理 |
| 大數法則、Chebyshev | 第 31–33 集 |
| 頻譜估計 | 第 34–36 集 |

---

## 附：本集一句話總結

> **ergodic 原本是從「時間平移砍不出去的事件」出發：遍歷集合的機率非 0 即 1，結果是樣本平均收斂到常數（但不一定是期望值）；它和 stationary 是兩個獨立的定義，只有兩者都成立時時間平均才收斂到期望值——後來工程書把這個結果當成定義而造成混淆，而工程上真正要的其實是大數法則。**

---

## ⚠️ 待確認清單

1. 上課日期：OCW 頁面和逐字稿都沒寫。
2. 老師說的 1991 年《Ergodic Theory of Discrete Sample Paths》：一般記為 P. C. Shields（AMS, 1996），年份待確認。
3. 老師說「另一本書也介紹了 ergodic theorem 是結果、晚期的書把它當定義」：沒說書名。

---

*筆記依據陳伯寧老師「隨機過程」Lec 12-0 錄影逐字稿（whisper large-v3-turbo，53:24）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
