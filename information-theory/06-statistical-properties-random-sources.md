---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 6
lecture: Lec06 B.3 Statistical properties of random sources
date: 待補
video: https://youtu.be/CpBgsd5q1hM
notes: Alajaji & Chen 附錄 B §B.3（pp. 276–283，T-invariant、ergodic set、memoryless／stationary／ergodic、Theorem B.4、Markov chain、Fig. B.1）
---

# 第 6 集 · Lec06 B.3：T-invariant、ergodic、stationary、Markov source [▶ 影片](https://youtu.be/CpBgsd5q1hM)

← 上一集：[05](05-probability-random-processes-overview.md) ｜ [總目錄](README.md) ｜ 下一集：[07](07-ergodicity-law-of-large-numbers-clt.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 6 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（50:33，whisper large-v3-turbo）＋ 課本附錄 B §B.3（pp. 276–283）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「ergodic」聽成「ergatic／Egatic／Argatic／爾嘎迪／騙力」，「遍歷性」聽成「騙力性／片力」，「穩態」聽成「穩泰」，「indecomposable」聽成「indiscomparable」，「反函數」聽成「反弹数」，「memoryless」聽成「memories」，「Birkhoff」聽成「Burkoff」，「Khinchin」聽成「Kinchin」，「variance」聽成「Variant」，「探針」聽成「碳針」，「大數法則」聽成「大樹法則／大術法」，「收斂」聽成「熟練」，「Markov chain」聽成「Marco Chan／Mark of Chen」，「最大公因數」聽成「最大供應數」，「initial probability」聽成「Initial Publicity」。[▶ 30:36](https://youtu.be/CpBgsd5q1hM?t=1836) 一段是 whisper 重複輸出的亂碼（x'x'x'…）。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼在乎時間：left-shift T](#1-為什麼在乎時間left-shift-t)
- [2. T-invariant 事件](#2-t-invariant-事件)
- [3. 不可切割的群組](#3-不可切割的群組)
- [4. Ergodic set](#4-ergodic-set)
- [5. Memoryless 與 stationary](#5-memoryless-與-stationary)
- [6. Ergodic process 與它的意義](#6-ergodic-process-與它的意義)
- [7. Ergodic ≠ stationary：time average vs ensemble average](#7-ergodic--stationarytime-average-vs-ensemble-average)
- [8. Pointwise ergodic theorem](#8-pointwise-ergodic-theorem)
- [9. 擲骰子的例子與大數法則](#9-擲骰子的例子與大數法則)
- [10. 為什麼少見 ergodic 但 non-stationary](#10-為什麼少見-ergodic-但-non-stationary)
- [11. Markov chain](#11-markov-chain)
- [12. Markov source 的性質](#12-markov-source-的性質)
- [13. 一頁速查表](#13-一頁速查表)
- [14. 與後續集數的連結](#14-與後續集數的連結)

---

## 0. 這堂課要做什麼

隨機過程（在消息理論裡常叫 **random source**）有哪些和**時間**有關的統計性質：memoryless（i.i.d.）、stationary、**ergodic**、Markov。最花時間的是 ergodic——Cover 的書用了 73 次卻從不解釋。

| 主題 | 課本 |
|---|---|
| left-shift T、T-invariant、$T^{-1}$、ergodic set | §B.3（pp. 276–278） |
| memoryless、stationary、ergodic process | p. 278–279 |
| Theorem B.4（pointwise ergodic theorem）、擲骰子 | pp. 279–280 |
| Markov chain、k 階 Markov、irreducible、aperiodic、stationary distribution | pp. 280–282 |
| Fig. B.1 各類 process 的關係 | p. 283 |

---

## 1. 為什麼在乎時間：left-shift T

[▶ 00:00](https://youtu.be/CpBgsd5q1hM?t=0)

- 通訊講究時間：一個系統隨時間改變時，統計特性有沒有改變？
- 我們關心的不是一次，而是一整串。例：丟銅板出現「正正正反反正反正……」，這一整串是一個 outcome。
- 例：手機出廠後兩年是否都好用。你可能 3 月 8 日（老師說今天是婦女節）開始用，也可能 3 月 9 日開始用——**起始時間往右挪一格**。如果系統的統計特性會隨啟用時間而變，工程上是不好的。

【課本補充】課本（p. 276）的定義：$\mathcal X^\infty$ 是所有實數序列 $\mathbf x=(x_1,x_2,x_3,\dots)$ 的集合。**left-shift**（shift transformation）$T$：
$$T\mathbf x=T(x_1,x_2,x_3,\dots)=(x_2,x_3,\dots),$$
就是「切掉第一個分量」。對事件 $E$，$TE:=\{T\mathbf x:\mathbf x\in E\}$。

---

## 2. T-invariant 事件

[▶ 01:33](https://youtu.be/CpBgsd5q1hM?t=93)

**定義**（課本 p. 276）：事件 $E$ 叫 **T-invariant**（對 left-shift 不變），若
$$TE\subseteq E.$$

**例 1** [▶ 02:04](https://youtu.be/CpBgsd5q1hM?t=124)：事件 = {正反正反…, 反正反正…}（正反交錯出現）。切掉一個，兩個序列互換，集合不變。從 3 月 8 日開始丟和從 3 月 9 日開始丟，機率一樣。

**例 2** [▶ 03:34](https://youtu.be/CpBgsd5q1hM?t=214)：「一旦出現正面就永遠是正面，而且前兩個之內就出現」——
$$E_1=\{(1,1,1,1,\dots),\ (0,1,1,1,\dots),\ (0,0,1,1,\dots)\}.$$
切掉第一個：
$$TE_1=\{(1,1,1,\dots),\ (1,1,1,\dots),\ (0,1,1,\dots)\}=\{(1,1,1,\dots),\ (0,1,1,\dots)\}\subseteq E_1.$$
集合變小了，所以 $E_1$ 是 T-invariant。（課本 (B.3.1)，p. 276–277 的同一個例子。）

**為什麼定義成「變小」不是「相等」** [▶ 04:04](https://youtu.be/CpBgsd5q1hM?t=244)：工程上希望現象**收斂**、越來越集中、可以預測，而不是發散。「t gets smaller and smaller → more condensed」。

**切越多越小** [▶ 05:05](https://youtu.be/CpBgsd5q1hM?t=305)：若 $TE\subseteq E$，則 $T^2E\subseteq TE$；歸納得
$$\cdots\subseteq T^3E\subseteq T^2E\subseteq TE\subseteq E.$$
（課本 p. 277，證明在註 3：$A\subseteq B\Rightarrow TA\subseteq TB$，取 $A=TE$、$B=E$。）

【口頭】手機越晚用越穩定，因為能出現的可能性越來越少。

---

## 3. 不可切割的群組

[▶ 05:35](https://youtu.be/CpBgsd5q1hM?t=335)

若 $(1,0,0,1,0,0,\dots)$ 在 T-invariant 集合 $E$ 裡，那它所有往左 shift 的版本 $(0,0,1,0,0,1,\dots)$、$(0,1,0,0,1,0,\dots)$ 也都要在 $E$ 裡（因為切完之後只會變小、不會跑出去）。

所以：**一個元素和它所有 shift 的版本，要嘛全部在 $E$ 裡，要嘛全部不在**，不能只有一部分在。這叫 **indecomposable group（不可切割的群組）**，課本叫「T-invariant group」（p. 277）。

- 反例 [▶ 07:37](https://youtu.be/CpBgsd5q1hM?t=457)：只有 {正反正反…} 一個元素的集合不是 T-invariant，切一次就跑出去了。正反正反和反正反正要嘛一起進來、要嘛一起拿掉。
- 【口頭】比喻：三個結拜兄弟，要入黨就三個一起入，不然三個都不入。
- 所以早期不關心「只含 100100… 而不含另外兩個 shift」這種事件：我們不希望系統的起始點影響之後的統計行為。

**Continuous 的情形** [▶ 08:08](https://youtu.be/CpBgsd5q1hM?t=488)：（老師說「剛剛同學有問 continuous」，問題沒有錄到）事件是一群波形；從某個時間切開，這個波形變那個波形，若整群不變就是 T-invariant。第 5 章才討論 continuous。

**$T^{-1}$** [▶ 11:12](https://youtu.be/CpBgsd5q1hM?t=672)：
- $T$ 是多對一，沒有反函數：$(0,0,1,0,0,1,\dots)$ 可能是 $(1,0,0,1,\dots)$ 切來的，也可能是 $(0,0,0,1,0,0,1,\dots)$ 切來的。
- 有些「過渡」元素（例如 $E_1$ 裡的 $(0,0,1,1,\dots)$）切一次就被排除。為了處理這個，把集合**放大**：定義
$$T^{-1}E:=\{\mathbf x\in\mathcal X^\infty:\ T\mathbf x\in E\},$$
把所有往右 shift（前面補任何東西）的版本補滿。【口頭】這是數學上的便利，不是真的反函數。

---

## 4. Ergodic set

[▶ 11:43](https://youtu.be/CpBgsd5q1hM?t=703)

**定義**（課本 (B.3.2)，p. 277–278）：滿足
$$T^{-1}E=E$$
的集合叫 **ergodic set**。此時 $TE=T(T^{-1}E)=E$（課本註 4 有證明），所以
$$\cdots=T^{-2}E=T^{-1}E=E=TE=T^2E=\cdots,$$
$E$ 只由 T-invariant 群組組成。

**意義** [▶ 12:45](https://youtu.be/CpBgsd5q1hM?t=765)：
- T-invariant 是「隨時間切割越來越小」；ergodic set 是**完全不隨時間改變**——從哪個時間開始看，都好像凍結了。
- 課本的話：as time goes by, the set always stays in the state that it has been before。
- 例：{正反正反…, 反正反正…} 切一個是同一個集合，怎麼看都一樣，是 ergodic set。

【課本補充】課本（p. 278）另一個例子：$\mathcal X=\{0,1\}$ 時，「只含有限多個 0 的所有二元序列」是 ergodic set。

**Two-sided 的情形** [▶ 14:49](https://youtu.be/CpBgsd5q1hM?t=889)：工程系統多從某個時間開始用，所以談 **one-sided** process。若接受從 $-\infty$ 就開始的 **two-sided** process，$T$ 就只是**重新標號（re-index）**——把今天當昨天、明天當今天——有唯一反函數，ergodic 只要 $TE=E$。（課本 p. 278 註 5。）

---

## 5. Memoryless 與 stationary

[▶ 15:52](https://youtu.be/CpBgsd5q1hM?t=952)

**Memoryless（無記憶）**（課本 p. 278）：$X$ 的隨機變數是 **i.i.d.**：
- independent：任何有限個 $X_{i_1},\dots,X_{i_n}$ 滿足 $\Pr[X_{i_1}=x_1,\dots,X_{i_n}=x_n]=\prod_l\Pr[X_{i_l}=x_l]$；
- identically distributed：$\Pr[X_i=x]=\Pr[X_1=x]$ 對所有 $i$。

例：$X_1,X_2,X_3,\dots$ 都是 0/1、獨立、機率各 1/2。

【口頭】機率上叫 i.i.d.，工程上叫 **memoryless**：不管從哪一天開始用，機率模式都一樣，記得過去發生什麼完全沒意義，所以**不需要 buffer、不需要記憶體**。

**Stationary（穩態，strictly stationary）** [▶ 16:52](https://youtu.be/CpBgsd5q1hM?t=1012)：每個事件的機率在時間平移後不變。等價地，對任何 $j$，
$$\Pr[X_1=x_1,\dots,X_n=x_n]=\Pr[X_{j+1}=x_1,\dots,X_{j+n}=x_n].$$

【課本補充】課本（p. 278）：memoryless source 一定 stationary；stationary source 的隨機變數一定同分布。

---

## 6. Ergodic process 與它的意義

[▶ 17:22](https://youtu.be/CpBgsd5q1hM?t=1042)

**「遍歷」的直覺**（【口頭】）：
- ergodic 在物理上翻成**遍歷性**：遊歷所有可能。
- 集合裡有 8 個元素。把量測儀器放在一點，隨著時間平移（一直切），這個元素會變成那個，循環下去，**所有的元素都會走一遍**。所以不用到處量，乖乖在一個地方量，就能量到所有現象。
- 它是**封閉體系**：不跟外界交流。只有封閉體系能做實驗。
- 老師的比喻：佛家的因果輪迴，經過生生世世會經歷人世間所有的苦；跳出來，就不在這個循環裡。

**Ergodic sets 互不相交** [▶ 19:52](https://youtu.be/CpBgsd5q1hM?t=1192)：把 ergodic set 切到最小，彼此沒有交集（封閉體系，不跟別人互動）。例：
- {101010…, 010101…} 是一個 ergodic set；
- {100100…, 010010…, 001001…} 是另一個 ergodic set；
- 兩者沒有交集。

**定義**（課本 p. 278）：$X$ 叫 **ergodic process**，若 $\mathcal F_X$ 中每個 ergodic set 的機率**不是 1 就是 0**。

課本說這個定義不太直觀；而且它**跟 stationarity 無關**，只是說「不受時間平移（左、右）影響的事件，機率不是 0 就是 1」（p. 279）。

**它到底給我們什麼** [▶ 21:24](https://youtu.be/CpBgsd5q1hM?t=1284)：
- 定義集合 $A_{0.1}=\left\{\mathbf x:\lim_{n\to\infty}\frac1n\sum_{k=1}^nx_k=0.1\right\}$。從哪裡開始切，極限平均都一樣，所以它是 ergodic set。
- 同樣 $A_{0.2}$（極限平均 0.2）也是 ergodic set，而且和 $A_{0.1}$ 沒有交集。
- ergodic 的定義說：這些集合只有一個機率是 1，其他都是 0。
- 所以：**所有收斂的 time average（時間平均）都收斂到一個常數**（以機率 1）。這就是 Cover 書上要 ergodic process 的原因。

**為什麼物理要講 ergodic** [▶ 23:25](https://youtu.be/CpBgsd5q1hM?t=1405)：實驗要有**一致性、可重複性**。每個人從不同點出發、探針放不同位置、不同時間開始量，長期平均最後都一樣。若不一致，表示體系不是封閉的、不是 ergodic。不收斂的東西沒辦法用工程體系操作。

---

## 7. Ergodic ≠ stationary：time average vs ensemble average

[▶ 24:26](https://youtu.be/CpBgsd5q1hM?t=1466)

- **Time average（時間平均）**：$\frac{X_1+X_2+X_3+X_4}4$，不同時間的結果平均。課本也叫 sample average 或 Cesàro mean（p. 279 註 6）。
- **Ensemble average（集成平均）**：對機率的可能性平均，就是期望值。例：$X$ 取 0、1 各機率 1/2，ensemble average $=\frac12\cdot0+\frac12\cdot1=\frac12$。這也是為什麼要映射到實數——才能平均。

**Ergodic 的極限不一定等於期望值** [▶ 25:26](https://youtu.be/CpBgsd5q1hM?t=1526)：
- 例：只告訴你 ergodic set {1010…, 0101…} 機率是 1，其他 ergodic set 機率 0。不管從哪看，time average 都收斂到 1/2。
- 但我沒說兩個序列各 1/2。可能「1010…」機率 0.8、「0101…」機率 0.2（從正面出發和從反面出發的機率不同）。
- 這時 ensemble average 隨時間改變：
  - 第 1 個時間：$0.8\cdot1+0.2\cdot0=0.8$；
  - 第 2 個時間：$0.8\cdot0+0.2\cdot1=0.2$；
  - ……來回變化。
- 所以它**不是 stationary**（stationary 要每個時間的 ensemble average 都一樣），但它是 ergodic：time average 收斂到常數 1/2。

【口頭】老師說投影片還有一個用 limsup 寫的版本（因為 limsup 一定存在，不用討論極限存不存在），留給同學看。

**結論** [▶ 28:02](https://youtu.be/CpBgsd5q1hM?t=1682)：看到 ergodic，腦中要想到——工程上要的是**平均收斂**。做量測的人要知道某個量，那個量是從平均來的；不收斂就沒有重複性，量了沒意義。ergodic 告訴你這個體系可以實驗。

---

## 8. Pointwise ergodic theorem

[▶ 29:04](https://youtu.be/CpBgsd5q1hM?t=1744)

**Theorem B.4（pointwise ergodic theorem，Birkhoff–Khinchin）**（p. 279）：$X=\{X_n\}$ 是離散時間 **stationary** process。對實值函數 $f$，若 $|E[f(X_n)]|<\infty$，則存在隨機變數 $Y$ 使
$$\lim_{n\to\infty}\frac1n\sum_{k=1}^nf(X_k)=Y\quad\text{with probability 1}.$$
若除了 stationary 還是 **ergodic**，則
$$\lim_{n\to\infty}\frac1n\sum_{k=1}^nf(X_k)=E[f(X_1)]\quad\text{with probability 1}.$$

**看出端倪** [▶ 29:34](https://youtu.be/CpBgsd5q1hM?t=1774)：
- **只有 stationary**：平均收斂到一個**隨機變數** $Y$（可能是好幾個值，各有機率）。例：說雜訊是 stationary，你量出來的能量（variance）和我量出來的可能不一樣，但**都是對的**。碰到 stationary 系統做實驗要特別注意。
- **stationary + ergodic**：收斂到**常數**；而且因為 stationary（每個時間機率一樣），這個常數**就是期望值**。例如上面的 {1010…, 0101…}：stationary 就只能各 0.5，平均 1/2 = 期望值。

【課本補充】課本（p. 279）的說法：ergodicity 保證所有收斂的 sample average 收斂到常數（但不一定是期望值）；stationarity 保證 time average 收斂到隨機變數；兩者合起來，time average = ensemble average。

所以 information theory 的書都假設 **stationary ergodic**：要的是可量測（每個人量都一樣）、而且收斂到期望值。

---

## 9. 擲骰子的例子與大數法則

[▶ 33:13](https://youtu.be/CpBgsd5q1hM?t=1993)

擲骰子 30 次，得到（課本 p. 280）
$$x^{30}=154326543334225632425644234443.$$
估計「出現 1 點的機率」：數 30 次裡出現 1 點的次數放分子、總次數放分母，約 $\frac1{30}$。

**什麼時候能這樣做？** 骰子行為是 **stationary ergodic** 時。否則這種結論數學上不嚴謹。stationary ergodic 保證量越多越準，越接近真正的機率。
- 理由：令 $f(x)=1$ 若 $x=1$、否則 0。估計值就是 $\frac{f(X_1)+\cdots+f(X_{30})}{30}$，由 Theorem B.4 收斂到 $E[f(X_1)]=\Pr[X_1=1]$。

【課本補充】課本 Example B.5（p. 279）：i.i.d. 二元序列（顯然 stationary ergodic），取 $f(0)=0$、$f(1)=1$，得 $\lim\frac{X_1+\cdots+X_n}n=P_X(1)$。課本 p. 280 列出整組估計：
$$\Pr\{X=1\}\approx\tfrac1{30},\ \Pr\{X=2\}\approx\tfrac6{30},\ \Pr\{X=3\}\approx\tfrac7{30},\ \Pr\{X=4\}\approx\tfrac9{30},\ \Pr\{X=5\}\approx\tfrac4{30},\ \Pr\{X=6\}\approx\tfrac3{30}.$$

**大數法則（law of large numbers）** [▶ 35:16](https://youtu.be/CpBgsd5q1hM?t=2116)：
- 大數法則講的其實是**條件**：「平均收斂到期望值」這個**結果**很重要，所以很多人提出不同的條件讓它成立，就有很多大數法則定理。
- stationary ergodic 是讓這個結果成立的其中一種條件。
- 要的結果：**empirical distribution（經驗分布）或 relative frequency（相對頻率）一定要收斂**。系統能收斂、能量測，才能設計工程系統去對付雜訊。
- 【口頭】投票行為也要 stationary ergodic 才能預測——但人常常「跳 tone」，不是 ergodic。

---

## 10. 為什麼少見 ergodic 但 non-stationary

[▶ 36:46](https://youtu.be/CpBgsd5q1hM?t=2206)

通訊理論常假設 source stationary 或 stationary ergodic，但幾乎看不到「ergodic 但 non-stationary」：
1. ergodic 保證收斂，但不保證收斂到期望值，工程上不好用、應用有限。
2. ergodic 的定義很抽象，理論分析很難。stationary 很好分析——收斂到隨機變數也沒關係，例如「50% 機率收斂到 1 瓦、50% 收斂到 2 瓦」也很清楚。

所以 Theorem B.4 的敘述順序是**先 stationary 再 ergodic**，不會先 ergodic 再談 stationary。（課本 p. 280 也這樣說明。）

【口頭】老師的人生建議：最好不要當一個 ergodic people——偶爾要踏出自己的圈圈、跟外界交流，不要永遠被預測。

---

## 11. Markov chain

[▶ 38:48](https://youtu.be/CpBgsd5q1hM?t=2328)

**三個隨機變數的 Markov chain**（課本 (B.3.3)，p. 280）：$X,Y,Z$ 形成 Markov chain，記 $X\to Y\to Z$，若
$$P_{X,Y,Z}(x,y,z)=P_X(x)\,P_{Y|X}(y|x)\,P_{Z|Y}(z|y),$$
即 $P_{Z|X,Y}(z|x,y)=P_{Z|Y}(z|y)$。

**推導** [▶ 39:21](https://youtu.be/CpBgsd5q1hM?t=2361)：由 Bayes 法則（chain rule）一定有
$$P_{X,Y,Z}=P_X\,P_{Y|X}\,P_{Z|X,Y}.$$
Markov 的意思是第三項裡 $Z$ 只跟 $Y$ 有統計關係、跟 $X$ 無關，可以把 $X$ 拿掉。機率特性完全由前一個決定。

> ⚠️ 待確認：[▶ 38:48](https://youtu.be/CpBgsd5q1hM?t=2328) 老師說 Markov chain「在 70 年代提出來」，可能是口誤或字幕錯誤（Markov 本人的工作早得多），課本沒有提年代。

【口頭】Markov chain 和 stationary、ergodic 都沒有完全的關係，是從不同角度出發：它講的是「根據過去看未來」。

**中間一拉，兩邊獨立** [▶ 40:23](https://youtu.be/CpBgsd5q1hM?t=2423)：$X\to Y\to Z$ 等價於「給定 $Y$，$X$ 和 $Z$ 條件獨立」：
$$P_{X,Z|Y}(x,z|y)=P_{X|Y}(x|y)\,P_{Z|Y}(z|y).$$

> 以下**不是逐字稿內容**，是補的推導（老師說「可以被證明」）：
> $$P_{X,Z|Y}(x,z|y)=\frac{P_{X,Y,Z}(x,y,z)}{P_Y(y)}=\frac{P_X(x)P_{Y|X}(y|x)}{P_Y(y)}\,P_{Z|Y}(z|y)=\frac{P_{X,Y}(x,y)}{P_Y(y)}\,P_{Z|Y}(z|y)=P_{X|Y}(x|y)\,P_{Z|Y}(z|y).$$
> 反過來，若條件獨立成立，$P_{X,Y,Z}=P_Y\,P_{X|Y}\,P_{Z|Y}=P_{X,Y}\,P_{Z|Y}=P_X\,P_{Y|X}\,P_{Z|Y}$。

- 因為這個式子對 $X$、$Z$ 對稱，$X\to Y\to Z$ 等價於 $Z\to Y\to X$，所以也寫成 $X\leftrightarrow Y\leftrightarrow Z$（課本 p. 280）。
- 【口頭】$X$ 是昨天、$Y$ 是今天、$Z$ 是明天，但可以反過來，昨天、明天只是名詞。

**Latent variable** [▶ 40:23](https://youtu.be/CpBgsd5q1hM?t=2423)（【口頭】）：在 data analytics 裡，量到的 $X,Y,Z$ 彼此相依很討厭。可以自己加一個 **latent variable（隱變數）** $W$（隨機特性由你定義，可能實際不存在），湊成 Markov chain。這樣「$W$ 已知」時，兩邊完全獨立，體系就切開了。

**k 階 Markov source** [▶ 41:56](https://youtu.be/CpBgsd5q1hM?t=2516)（課本 (B.3.4)，p. 280）：對所有 $n>k$，
$$\Pr[X_n=x_n\mid X_{n-1}=x_{n-1},\dots,X_1=x_1]=\Pr[X_n=x_n\mid X_{n-1}=x_{n-1},\dots,X_{n-k}=x_{n-k}].$$
只跟過去 $k$ 個有關。$(x_{n-k},\dots,x_{n-1})\in\mathcal X^k$ 叫時間 $n$ 的 **state（狀態）**。$k=1$ 就是一般的 Markov source。

---

## 12. Markov source 的性質

[▶ 42:27](https://youtu.be/CpBgsd5q1hM?t=2547)

**Irreducible（不可約）**（課本 p. 281）：從任一個 state 經有限步走到任一個 state 都有正機率：對所有 $x^k,y^k\in\mathcal X^k$，存在 $j\ge1$ 使
$$\Pr\left[X_j^{k+j-1}=x^k\ \middle|\ X_1^k=y^k\right]>0.$$
【口頭】state 不會因為時間而消失（不會 reduce）。不 irreducible 的 Markov chain 可能不收斂，量測不收斂。

**Time-invariant／homogeneous** [▶ 43:28](https://youtu.be/CpBgsd5q1hM?t=2608)：轉移機率不隨時間改變。
- 反例：3/8→3/9 的轉移機率是 0.1、0.9，3/9→3/10 變成 0.2、0.8，就不是 homogeneous。
- homogeneous 的一階 Markov chain 由轉移矩陣 $\left[\Pr\{X_2=x_2\mid X_1=x_1\}\right]_{|\mathcal X|\times|\mathcal X|}$ 和初始分布 $P_{X_1}$ 決定（課本 p. 281）。

【口頭】我們需要穩態、需要 ergodic、希望平均收斂到期望值——這一直是工程真正要的東西。這本書裡 Shannon 三大定律的證明**全部用同一個方法：大數法則**，只用收斂來證，因為 Shannon 根本的精神就是要大數法則的結果。

**Period 與 aperiodic** [▶ 44:59](https://youtu.be/CpBgsd5q1hM?t=2699)（課本 p. 281–282）：一階 Markov chain 中 state $x$ 的週期
$$d(x):=\gcd\{n\ge1:\ \Pr\{X_{n+1}=x\mid X_1=x\}>0\}.$$
- 從 $x$ 出發，只有在 $d(x)$ 的倍數時間才可能回到 $x$。
- $d(x)=1$ 叫 **aperiodic（非週期）**；$d(x)>1$ 叫 periodic。所有 state 都 aperiodic，chain 就是 aperiodic。
- 例：若回到自己的可能步數是 3 和 5，gcd = 1，沒有週期 pattern。若 gcd = 2，就像銅板自然出現 0101 的週期。

> ⚠️ 逐字稿缺字／口誤：老師一開始用「從 0 走到 1」舉例，[▶ 47:33](https://youtu.be/CpBgsd5q1hM?t=2853) 自己更正：週期講的是**從自己回到自己**（$x$ 到 $x$）。

- **Irreducible chain 中所有 state 的週期相同**：只要有一個 state aperiodic，整個 chain 就 aperiodic（課本 p. 282）。

**Stationary distribution** [▶ 48:35](https://youtu.be/CpBgsd5q1hM?t=2915)（課本 p. 282）：$\pi$ 是 homogeneous 一階 Markov chain 的 stationary distribution，若
$$\pi(y)=\sum_{x\in\mathcal X}\pi(x)\Pr\{X_2=y\mid X_1=x\},\quad\forall y.$$
- 有限字母 homogeneous chain：$\pi$ **一定存在**；若 irreducible，$\pi$ **唯一**。
- 若 irreducible **且** aperiodic：$\lim_{n\to\infty}\Pr\{X_{n+1}=y\mid X_1=x\}=\pi(y)$，對所有 $x,y$（會收斂）。
- **初始分布等於 stationary distribution 時，chain 才是 stationary process**。初始機率不對，即使 homogeneous、aperiodic、irreducible 也不是穩態。
- 有限字母的 stationary Markov source 是 ergodic $\iff$ 它 irreducible（課本 p. 282）。

【口頭】老師說 irreducible、time-invariant、aperiodic 都成立時，Markov chain 會變成 ergodic，這樣的 Markov source 就可以壓縮、會有極限。

**各類 process 的關係**（課本 Fig. B.1，p. 283）：i.i.d. ⊂ stationary；Markov、ergodic 各自和 stationary 部分重疊；Markov 不一定是 i.i.d.、stationary 或 ergodic。

**結語** [▶ 49:37](https://youtu.be/CpBgsd5q1hM?t=2977)：很多文獻從 Markov 出發還要加一堆條件，就是為了得到「收斂到期望值」。老師寫書時決定不強調 Markov、stationary、ergodic，而是告訴你**用大數法則就夠了**——我們要的是那個結果。

---

## 13. 一頁速查表

**Left-shift 與 invariance**
- $T(x_1,x_2,\dots)=(x_2,x_3,\dots)$。T-invariant：$TE\subseteq E$ ⇒ $\cdots\subseteq T^2E\subseteq TE\subseteq E$。
- 例：$E_1=\{1111\ldots,0111\ldots,0011\ldots\}$，$TE_1=\{111\ldots,0111\ldots\}\subseteq E_1$。
- 一個元素和它所有 shift 要嘛全在、要嘛全不在（indecomposable group）。
- $T^{-1}E=\{\mathbf x:T\mathbf x\in E\}$；**ergodic set**：$T^{-1}E=E$（⇒ $TE=E$），完全不隨時間變。

**三種 process**
- Memoryless = i.i.d.（不需記憶體）⇒ stationary。
- Stationary：$\Pr[X_1^n=x^n]=\Pr[X_{j+1}^{j+n}=x^n]$ $\forall j$。
- Ergodic：每個 ergodic set 機率 0 或 1；和 stationary 無關。直覺：遍歷、封閉、可重複實驗。

**Time average vs ensemble average**
- Ergodic ⇒ 收斂的 time average 都收斂到常數（不一定是期望值）。例：{1010…}機率 0.8、{0101…}機率 0.2：time average → 1/2，但 ensemble average 在 0.8、0.2 間跳（非 stationary）。
- Stationary ⇒ time average 收斂到隨機變數 $Y$。

**Pointwise ergodic theorem（B.4）**：stationary ⇒ $\frac1n\sum f(X_k)\to Y$ a.s.；stationary + ergodic ⇒ $\to E[f(X_1)]$ a.s.
- 應用：相對頻率 → 真機率（擲骰子 $\Pr\{X=1\}\approx\frac1{30}$）。

**Markov**
- $X\to Y\to Z$：$P_{XYZ}=P_XP_{Y|X}P_{Z|Y}$ $\iff$ $P_{XZ|Y}=P_{X|Y}P_{Z|Y}$ $\iff$ $Z\to Y\to X$。
- k 階：只看過去 $k$ 個；state $\in\mathcal X^k$。
- irreducible（任一 state 可到任一 state）、homogeneous（轉移機率不變）、$d(x)=\gcd\{n:\Pr\{X_{n+1}=x|X_1=x\}>0\}$，aperiodic ⇔ $d=1$；irreducible ⇒ 所有 state 週期相同。
- $\pi(y)=\sum_x\pi(x)P(y|x)$：有限字母必存在；irreducible ⇒ 唯一；+aperiodic ⇒ $P^n(y|x)\to\pi(y)$；初始 $=\pi$ ⇒ stationary。
- 有限字母 stationary Markov：ergodic ⇔ irreducible。

---

## 14. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 隨機變數的收斂、大數法則、中央極限定理 | 第 7 集（§B.4–B.6） |
| Markov chain $X\to Y\to Z$ | 第 9 集（data processing inequality） |
| Stationary source 的 entropy rate | 第 11–12 集（§2.9、第 3 章） |
| Stationary ergodic source 的 AEP（Shannon–McMillan–Breiman） | 第 12 集（§3.2） |
| Markov source 的壓縮 | 第 12–13 集 |
| 第二部分：非 stationary／非 ergodic 的一般化 | 第 32–35 集 |

---

## 附：本集一句話總結

> **Ergodic 的意思是「從哪裡開始量、量多久，長期平均都收斂到同一個常數」；再加上 stationary，那個常數就是期望值——這正是大數法則要的結果，也是所有編碼定理證明的根本。**

---

## ⚠️ 待確認清單

1. [▶ 38:48](https://youtu.be/CpBgsd5q1hM?t=2328) 老師說 Markov chain「在 70 年代提出來」，年代可能是口誤或字幕錯誤，課本沒有提。

---

*筆記依據陳伯寧老師「消息理論」Lec06 錄影逐字稿（whisper large-v3-turbo，50:33）與 Alajaji & Chen 課本附錄 B §B.3 整理。*
