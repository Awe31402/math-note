---
course: Stanford EE274 Data Compression: Theory and Applications（2023 秋）
episode: 4
lecture: Lecture 4
date: 2023-10-09
video: https://youtu.be/975qcAxZCG0
notes: 投影片 L4_ann.pdf（29 頁，手寫）；《Elements of Information Theory》§5.6、§5.8（書頁 118–127）
---

# 第 4 集 · Lecture 4：Huffman 碼（Huffman Codes） [▶ 影片](https://youtu.be/975qcAxZCG0)

← 上一集：[03-kraft-inequality-entropy](03-kraft-inequality-entropy.md) ｜ [總目錄](README.md) ｜ 下一集：[05-asymptotic-equipartition-property](05-asymptotic-equipartition-property.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 4 集
> **講者**：Shubham Chandak（Pulkit Tandon 中途補充）
> **來源**：YouTube 錄影逐字稿（1:15:09，人工字幕 en-US）＋ 投影片 `L4_ann.pdf`（上課手寫版）＋ Cover & Thomas §5.6、§5.8
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
- [1. 公告與回顧](#1-公告與回顧)
- [2. 小考檢討：二元熵函數、KL 散度、偏斜分布](#2-小考檢討二元熵函數kl-散度偏斜分布)
- [3. 最佳前綴碼的兩個條件](#3-最佳前綴碼的兩個條件)
- [4. Huffman 的故事](#4-huffman-的故事)
- [5. Huffman 碼的建構](#5-huffman-碼的建構)
- [6. 為什麼最佳？以及其他性質](#6-為什麼最佳以及其他性質)
- [7. 實作：用 heap 挑最小的兩個](#7-實作用-heap-挑最小的兩個)
- [8. 解碼：為什麼不用樹，改用查表](#8-解碼為什麼不用樹改用查表)
- [9. 實際例子：英文、程式碼、加密檔](#9-實際例子英文程式碼加密檔)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 19:57](https://youtu.be/975qcAxZCG0?t=1197) 大綱：

| 主題 | 課本 |
|---|---|
| 最佳前綴碼的條件 | §5.8 Lemma 5.8.1 |
| Huffman 碼的建構 | §5.6 |
| Huffman 碼的實務（實作、解碼、例子） | 課本無 |

---

## 1. 公告與回顧

### 1.1 SCL 教學

[▶ 00:05](https://youtu.be/975qcAxZCG0?t=5) 網站 Lectures 頁已放 SCL 教學（tutorial）[▶ 00:42](https://youtu.be/975qcAxZCG0?t=42)：安裝與使用、SCL 的結構、共用介面（讓各壓縮器只需專注在邏輯上）、資料區塊、編碼器／解碼器、機率分布工具（經驗分布、算熵）、標準壓縮器、位元／位元組與樹的工具 [▶ 01:15](https://youtu.be/975qcAxZCG0?t=75)。

[▶ 01:49](https://youtu.be/975qcAxZCG0?t=109) 還有一個練習（去年作業 0 的題目，附解答）和一個 Colab notebook。【口頭】[▶ 02:24](https://youtu.be/975qcAxZCG0?t=144) Pulkit 補充：notebook 示範怎麼在 Colab 裡裝 SCL，對期末專題很有用。

【投影片補充】`L4_ann.pdf` p.2：作業 1 的修正放在 Ed 上；**作業早點開始**；SCL 在 Windows 上的說明。

### 1.2 回顧

[▶ 02:58](https://youtu.be/975qcAxZCG0?t=178) 只回顧之後會用到的結果，不回顧證明：

- **Kraft 不等式**：前綴碼 ⇒ 碼長滿足 $\sum2^{-l_i}\le1$；滿足它 ⇒ 可以造出前綴碼。（講者口誤說「if and only if」，馬上改口 [▶ 03:33](https://youtu.be/975qcAxZCG0?t=213)。）之後用不太到。
- **熵** $H(X)=\sum p_i\log\frac1{p_i}$：無損壓縮的下界。
- **iid 的聯合熵** [▶ 04:06](https://youtu.be/975qcAxZCG0?t=246)：$H(X^n)=\sum H(X_i)=nH(X)$。第一步用**獨立**，第二步用**同分布**。
- **KL 散度** [▶ 04:40](https://youtu.be/975qcAxZCG0?t=280)：$D(p\|q)\ge0$，等號當且僅當 $p=q$。
- **主定理** [▶ 05:14](https://youtu.be/975qcAxZCG0?t=314)：任何前綴碼（作業：任何唯一可解碼碼）$\mathbb{E}[l]\ge H$；用分組可以任意接近 $H$。

[▶ 05:50](https://youtu.be/975qcAxZCG0?t=350) 可達性：Shannon 碼 $H\le\mathbb{E}[l]<H+1$；$n$ 個一組可以到 $H+\frac1n$ 以內 [▶ 06:25](https://youtu.be/975qcAxZCG0?t=385)。

【口頭】[▶ 06:59](https://youtu.be/975qcAxZCG0?t=419) **分組非常重要**。早期的壓縮器（像 gzip）用 Huffman 碼，沒有分組，效果沒那麼好；現代壓縮器全都用分組，但不是作業裡那種分法，有更好的方法（下週講）[▶ 07:32](https://youtu.be/975qcAxZCG0?t=452)。

---

## 2. 小考檢討：二元熵函數、KL 散度、偏斜分布

### 2.1 Bernoulli 的熵

[▶ 07:32](https://youtu.be/975qcAxZCG0?t=452) $X\sim\mathrm{Ber}(p)$：$P(X=1)=p$、$P(X=0)=1-p$。

$$H(X)=p\log_2\frac1p+(1-p)\log_2\frac1{1-p}\ \triangleq\ h_b(p)$$

[▶ 08:42](https://youtu.be/975qcAxZCG0?t=522) 這叫**二元熵函數**（binary entropy function），常寫成 $h_2(p)$ 或 $h_b(p)$。

【課堂討論】[▶ 08:42](https://youtu.be/975qcAxZCG0?t=522) 幾個值：

- $h_b(0)=0$：$\mathrm{Ber}(0)$ 永遠是 0，確定的。
- $h_b(1)=0$ [▶ 09:18](https://youtu.be/975qcAxZCG0?t=558)：永遠是 1。（記得 $0\log\frac10=0$。）
- $h_b\left(\frac12\right)=1$ [▶ 09:51](https://youtu.be/975qcAxZCG0?t=591)。

[▶ 09:51](https://youtu.be/975qcAxZCG0?t=591) 它是**凹函數**（concave），對 $\frac12$ 對稱，形狀像一個拱。

【口頭】[▶ 10:23](https://youtu.be/975qcAxZCG0?t=623) 它在 $\frac12$ 附近**很平**：$\mathrm{Ber}(0.5)$、$\mathrm{Ber}(0.4)$、$\mathrm{Ber}(0.6)$ 的檔案可壓縮程度差不多。

> 以下**不是逐字稿內容**，是算出來佐證「很平」：$h_b(0.4)=0.4\log_2\frac1{0.4}+0.6\log_2\frac1{0.6}\approx0.4\times1.3219+0.6\times0.7370\approx0.971$，只比 1 少 3%。

### 2.2 兩個 Bernoulli 的 KL 散度

[▶ 10:55](https://youtu.be/975qcAxZCG0?t=655)

$$D\left(\mathrm{Ber}(p)\,\|\,\mathrm{Ber}(q)\right)=p\log_2\frac pq+(1-p)\log_2\frac{1-p}{1-q}$$

【投影片補充】`L4_ann.pdf` p.6：$D(\mathrm{Ber}(0.3)\|\mathrm{Ber}(0.7))\approx0.4883$。

> 以下**不是逐字稿內容**，是驗算：$0.3\log_2\frac37+0.7\log_2\frac73=(0.7-0.3)\log_2\frac73=0.4\times1.2224\approx0.489$。

**最大值？**【課堂討論】[▶ 11:27](https://youtu.be/975qcAxZCG0?t=687) 學生答：**無限大** [▶ 12:06](https://youtu.be/975qcAxZCG0?t=726)。取 $q=0$、$p=1$，得到 $1\cdot\log\frac10=\infty$ [▶ 12:48](https://youtu.be/975qcAxZCG0?t=768)。最小是 0（$p=q$ 時）。

【口頭】[▶ 12:48](https://youtu.be/975qcAxZCG0?t=768) 衡量兩個分布差多少，最常見的兩種：KL 散度和**全變差距離**（total variation distance，也就是 $L_1$ 距離）。全變差對稱、有界、性質比較好；KL 在很多機器學習應用裡表現比較好 [▶ 13:23](https://youtu.be/975qcAxZCG0?t=803)。

**對稱嗎？** 不對稱 [▶ 13:23](https://youtu.be/975qcAxZCG0?t=803)。【投影片補充】`L4_ann.pdf` p.7 的反例：$p=0.3$、$q=0.4$。

> ⚠️ 逐字稿缺字 [▶ 13:23](https://youtu.be/975qcAxZCG0?t=803)：字幕說「Even if you take p equal to 0.3, q equal to 0.7, you will see that it will be symmetric」，意思是 $0.3$ 和 $0.7$ 剛好互補（$p=1-q$），這組會算出一樣的值，不能當反例；要用投影片的 $p=0.3$、$q=0.4$ 這種組合。

> 以下**不是逐字稿內容**，是驗算反例：$D(0.3\|0.4)=0.3\log_2\frac34+0.7\log_2\frac76\approx-0.1245+0.1557=0.0312$；$D(0.4\|0.3)=0.4\log_2\frac43+0.6\log_2\frac67\approx0.1660-0.1334=0.0326$。兩者不同。

### 2.3 偏斜分布：Shannon 碼很慘

[▶ 13:57](https://youtu.be/975qcAxZCG0?t=837) $X\sim\mathrm{Ber}(0.001)$，幾乎總是 0。

**Shannon 碼** [▶ 14:31](https://youtu.be/975qcAxZCG0?t=871)：

| $x$ | $P(x)$ | $l(x)=\left\lceil\log_2\frac1{P(x)}\right\rceil$ | 碼字 |
|---|---|---|---|
| 0 | 0.999 | 1 | `0` |
| 1 | 0.001 | 10 | `1000000000` |

$$\mathbb{E}[l]=0.999\times1+0.001\times10=1.009,\qquad H(X)\approx0.011,\qquad\frac{\mathbb{E}[l]}{H}\approx88$$

【口頭】[▶ 15:06](https://youtu.be/975qcAxZCG0?t=906) 題目要大家取兩位小數，如果兩個數都先取到兩位再相除，會得到 100 左右；這種情況可以申請重新評分（字幕作「regret request」，應為 regrade request）。

[▶ 15:41](https://youtu.be/975qcAxZCG0?t=941) 重點：這麼偏斜的分布，每符號應該只要約 0.01 位元，Shannon 碼卻花超過 1 位元。

### 2.4 怎麼改進？【課堂討論】

[▶ 16:18](https://youtu.be/975qcAxZCG0?t=978) 學生建議：把 1 的碼字砍到只剩 `1`。期望碼長變成 **1**。[▶ 16:54](https://youtu.be/975qcAxZCG0?t=1014) 這就是**單符號的最佳碼**：兩個符號至少要 1 位元／符號。但 1 還是遠大於熵 0.011。

**兩個一組** [▶ 17:35](https://youtu.be/975qcAxZCG0?t=1055)：$(X_1,X_2)$ 有 00、01、10、11 四種。

【課堂討論】[▶ 17:35](https://youtu.be/975qcAxZCG0?t=1055) 二元組的機率怎麼算？學生答：相乘。為什麼可以相乘？學生答：**獨立** [▶ 18:11](https://youtu.be/975qcAxZCG0?t=1091)。$P(x_1,x_2)=P(x_1)P(x_2)$。接下來幾週都假設獨立。

（表依 `L4_ann.pdf` p.11）

| $x^2$ | $P(x^2)$ | 碼字 |
|---|---|---|
| 00 | 0.998001 | `0` |
| 01 | 0.000999 | `10` |
| 10 | 0.000999 | `110` |
| 11 | 0.000001 | `111` |

[▶ 18:48](https://youtu.be/975qcAxZCG0?t=1128) 這是這個分布的**最佳碼**（等一下就學怎麼造）。[▶ 19:24](https://youtu.be/975qcAxZCG0?t=1164)

$$\frac{\mathbb{E}[l(X^2)]}{2}=\frac{1.002999}{2}\approx0.501\ \text{位元／符號}$$

比 1 好，但還是熵的約 50 倍。組可以再加大，但很快就不實際；真正的解法是**串流碼**（streaming codes），下週講 [▶ 19:24](https://youtu.be/975qcAxZCG0?t=1164)。

---

## 3. 最佳前綴碼的兩個條件

### 3.1 什麼叫最佳

[▶ 20:32](https://youtu.be/975qcAxZCG0?t=1232)

$$\min_{l_1,\dots,l_k}\ \sum_{i=1}^{k}p_il_i\quad\text{s.t.}\quad\text{前綴條件，等價地 }\sum_{i=1}^{k}2^{-l_i}\le1$$

【口頭】[▶ 21:35](https://youtu.be/975qcAxZCG0?t=1295) 學過凸最佳化的人可以用 Lagrange 乘數解（講義有），會得到 $l_i=\log\frac1{p_i}$ 的經驗法則。今天走另一條路。

> 以下**不是逐字稿內容**，是依課本 §5.3 補的 Lagrange 推導（忽略 $l_i$ 必須是整數）：令 $J=\sum p_il_i+\lambda\sum2^{-l_i}$。$\frac{\partial J}{\partial l_i}=p_i-\lambda2^{-l_i}\ln2=0$，所以 $2^{-l_i}=\frac{p_i}{\lambda\ln2}$。代回限制式 $\sum2^{-l_i}=1$ 得 $\lambda=\frac1{\ln2}$，於是 $2^{-l_i}=p_i$，$l_i^*=\log_2\frac1{p_i}$，期望碼長 $=H(X)$。

### 3.2 兩個條件

[▶ 22:09](https://youtu.be/975qcAxZCG0?t=1329)

1. **若 $p_i>p_j$，則 $l_i\le l_j$** [▶ 22:41](https://youtu.be/975qcAxZCG0?t=1361)。不然交換碼字可以更好（第 2 集證過）。
2. **最長的兩個碼字一樣長** [▶ 23:15](https://youtu.be/975qcAxZCG0?t=1395)。（新的）

[▶ 23:54](https://youtu.be/975qcAxZCG0?t=1434) 講者畫了一個碼：最長的兩個碼字一個長 2、一個長 3，所以不是最佳。

【課堂討論】[▶ 23:54](https://youtu.be/975qcAxZCG0?t=1434) 為什麼？學生答：把最長的那個往上移一層。[▶ 24:27](https://youtu.be/975qcAxZCG0?t=1467) 為什麼這樣還是前綴碼？另一位學生答：最長的兩個差一個位元……

[▶ 24:58](https://youtu.be/975qcAxZCG0?t=1498) 講者：把最長的碼字**砍短**到第二長的長度。[▶ 25:35](https://youtu.be/975qcAxZCG0?t=1535) 如果砍短之後違反前綴條件，可以論證原本的碼就已經違反了 [▶ 26:27](https://youtu.be/975qcAxZCG0?t=1587)。【口頭】Shannon 碼常常不滿足這個條件，所以不一定最佳。

> 以下**不是逐字稿內容**，是把這個論證寫完整：設最長碼字 $c$ 長 $L$，其他碼字都 $\le L'<L$。把 $c$ 砍成它的前 $L'$ 位 $c'$。(a) $c'$ 不會是別人的前綴：別的碼字長度 $\le L'$，要以 $c'$ 為前綴只能等於 $c'$，那它也是 $c$ 的前綴，原碼就違反了。(b) 別人也不會是 $c'$ 的前綴：$c'$ 是 $c$ 的前綴，若 $w$ 是 $c'$ 的前綴，$w$ 就是 $c$ 的前綴，原碼也違反了。所以砍短後仍是前綴碼，期望碼長嚴格變小（$c$ 的機率 $>0$ 時）。

【課本補充】§5.8 Lemma 5.8.1 還有第 3 條：存在一個最佳碼，它最長的兩個碼字**只差最後一位**，而且對應**機率最小的兩個符號**。這是 Huffman 合併最小兩個的根據（§6.1）。

---

## 4. Huffman 的故事

[▶ 27:01](https://youtu.be/975qcAxZCG0?t=1621) David Huffman 當時是博士生（講者說「I think」），修 Robert Fano 開的資訊理論課，那是 Shannon 1948 年論文後沒幾年。

- Fano 讓學生選：考期末考，或做專題 [▶ 27:41](https://youtu.be/975qcAxZCG0?t=1661)。
- Huffman 覺得專題比較好玩、比較簡單，選了專題，題目是**找出最佳前綴碼**。
- 他做了很久，一度覺得不可能，最後解出來了 [▶ 28:15](https://youtu.be/975qcAxZCG0?t=1695)。
- 事後 Fano 才說這其實是**未解問題**。Huffman 後來說，早知道是未解問題，大概根本不會去試。

【口頭】有時候我們會低估自己。Fano 也有一個貪婪建構，但很多時候不是最佳的；Huffman 的貪婪建構是最佳的 [▶ 28:52](https://youtu.be/975qcAxZCG0?t=1732)。

【課本補充】§5.7（書頁 123）：Fano 碼把機率由大到小排好，切成總機率最接近相等的兩半，上半給 0、下半給 1，遞迴下去；一般不是最佳，但 $L\le H(X)+2$。

---

## 5. Huffman 碼的建構

### 5.1 演算法

[▶ 28:52](https://youtu.be/975qcAxZCG0?t=1732)（`L4_ann.pdf` p.15）

1. 建一個節點清單：每個符號一個節點，記著它的機率 [▶ 29:40](https://youtu.be/975qcAxZCG0?t=1780)。
2. **當剩下不只一個節點時**：
   1. 挑**機率最小的兩個**節點；
   2. 合併：造一個新節點，兩個舊節點當它的子節點，機率 = 兩個子節點機率的和 [▶ 31:44](https://youtu.be/975qcAxZCG0?t=1904)。
3. 最後剩下的節點就是根。

\* **平手時任意挑** [▶ 31:44](https://youtu.be/975qcAxZCG0?t=1904)。

[▶ 32:28](https://youtu.be/975qcAxZCG0?t=1948) 最後得到一棵樹，所有原本的符號都在葉子上；標上 0、1 就是碼。

【課堂討論】[▶ 30:22](https://youtu.be/975qcAxZCG0?t=1822) 誰看過 Huffman 碼？一位學生在 Stanford CS106B 的期末作業做過；另一位在 Berkeley 大學部的課看過 [▶ 30:58](https://youtu.be/975qcAxZCG0?t=1858)。講者：它是**貪婪演算法**（greedy algorithm）的經典例子。

### 5.2 例 1

[▶ 32:28](https://youtu.be/975qcAxZCG0?t=1948)（機率依 `L4_ann.pdf` p.16）

| 符號 | A | B | C | D |
|---|---|---|---|---|
| 機率 | 0.55 | 0.25 | 0.13 | 0.07 |

1. 最小的兩個 C（0.13）、D（0.07）→ 合併成 $N_1$，機率 0.2 [▶ 33:23](https://youtu.be/975qcAxZCG0?t=2003)。
2. 剩 A、B、$N_1$。最小的兩個 B（0.25）、$N_1$（0.2）→ $N_2$，0.45 [▶ 33:59](https://youtu.be/975qcAxZCG0?t=2039)。
3. 剩 A、$N_2$ → 根 $N_3$，1.0 [▶ 34:33](https://youtu.be/975qcAxZCG0?t=2073)。

標上 0/1（投影片的標法）：A→`0`、B→`10`、C→`110`、D→`111`。

> 以下**不是逐字稿內容**，是算出來對照：$\mathbb{E}[l]=0.55+0.5+0.39+0.21=1.65$；$H\approx1.626$。

### 5.3 例 2【課堂討論】

[▶ 35:12](https://youtu.be/975qcAxZCG0?t=2112)

| 符號 | A | B | C | D | E |
|---|---|---|---|---|---|
| 機率 | 0.35 | 0.25 | 0.2 | 0.12 | 0.08 |

> ⚠️ 逐字稿缺字 [▶ 35:12](https://youtu.be/975qcAxZCG0?t=2112)：講者先念「0.3」，後面 [▶ 37:17](https://youtu.be/975qcAxZCG0?t=2237) 說「A, which is 0.35」；投影片 `L4_ann.pdf` p.17 也是 0.35（機率加起來才是 1）。

1. [▶ 36:01](https://youtu.be/975qcAxZCG0?t=2161) 學生：D（0.12）和 E（0.08）→ $N_1$ = 0.2。
2. [▶ 36:42](https://youtu.be/975qcAxZCG0?t=2202) 學生：C 和 $N_1$ → $N_2$ = 0.4。
3. 有學生說「$N_2$ 和 B」，**不對**：[▶ 37:17](https://youtu.be/975qcAxZCG0?t=2237) 剩下 $N_2$（0.4）、B（0.25）、A（0.35），最小的兩個是 **A 和 B** → $N_3$ = 0.6。
4. $N_2$、$N_3$ → 根，1.0。

[▶ 37:57](https://youtu.be/975qcAxZCG0?t=2277) 碼字（樹的根畫在右邊，所以從右往左讀）：

| 符號 | 機率 | 碼字 | 長度 |
|---|---|---|---|
| A | 0.35 | `00` | 2 |
| B | 0.25 | `01` | 2 |
| C | 0.2 | `10` | 2 |
| D | 0.12 | `110` | 3 |
| E | 0.08 | `111` | 3 |

[▶ 38:32](https://youtu.be/975qcAxZCG0?t=2312) 滿足兩個最佳條件：最長的兩個（D、E）一樣長；機率大的碼不會比較長。

> 以下**不是逐字稿內容**，是算出來對照：$\mathbb{E}[l]=0.7+0.5+0.4+0.36+0.24=2.2$；$H\approx2.153$；Shannon 碼長度 $(2,2,3,4,4)$，期望碼長 $0.7+0.5+0.6+0.48+0.32=2.6$。

【口頭】[▶ 39:03](https://youtu.be/975qcAxZCG0?t=2343) 想練程式面試可以自己實作：用什麼資料結構？遞迴還是迭代？

---

## 6. 為什麼最佳？以及其他性質

### 6.1 最佳性（課堂只講概念）

[▶ 39:42](https://youtu.be/975qcAxZCG0?t=2382) 只滿足兩個條件不代表最佳，要另外證。課堂不證，請看 Cover & Thomas 第 5 章（講者更正：講義沒有，要看課本）。

[▶ 40:32](https://youtu.be/975qcAxZCG0?t=2432) 想法是**歸納**：最終的碼是最佳的 ⟺ 合併一步後的碼是最佳的 ⟺ 再合併一步後的碼是最佳的 ⟺ …… [▶ 41:10](https://youtu.be/975qcAxZCG0?t=2470) 最後只剩兩個節點，碼就是 0 和 1，一定最佳。

【課本補充】§5.8（書頁 125–127）的證明骨架。設 $p_1\ge\cdots\ge p_m$，**Huffman 化簡** $p'=(p_1,\dots,p_{m-2},\,p_{m-1}+p_m)$。

1. 由 Lemma 5.8.1，存在一個最佳碼（**典型碼**，canonical code），其中 $x_{m-1}$、$x_m$ 的碼字最長、只差最後一位。
2. 從 $p'$ 的最佳碼 $C^*_{m-1}$ 展開：把 $p_{m-1}+p_m$ 的碼字後面各接 0、1 給 $x_{m-1}$、$x_m$。期望碼長
$$L(p)=L^*(p')+p_{m-1}+p_m.$$
3. 反過來，從 $p$ 的典型最佳碼把 $x_{m-1}$、$x_m$ 合併（去掉最後一位）：
$$L(p')=L^*(p)-p_{m-1}-p_m.$$
4. 兩式相加：$\left(L(p')-L^*(p')\right)+\left(L(p)-L^*(p)\right)=0$。兩個括號都 $\ge0$（$L^*$ 是最小值），所以都 $=0$。也就是：**把 $p'$ 的最佳碼展開，就得到 $p$ 的最佳碼**。Huffman 演算法正是一路這樣做。

### 6.2 其他性質

[▶ 41:56](https://youtu.be/975qcAxZCG0?t=2516)（`L4_ann.pdf` p.19）

- **貪婪演算法**：不做全域最佳化，每一步只合併最小的兩個。【口頭】貪婪演算法的證明常常有點難寫。
- **適用一般權重** $w_i\ge0$ [▶ 42:33](https://youtu.be/975qcAxZCG0?t=2553)：要最小化 $\sum w_il_i$（限制是前綴碼），權重不必是機率，同一個演算法。所以 Huffman 碼在編碼以外也有應用，作業會看到。
- **平手 ⇒ 可能有很多個 Huffman 碼** [▶ 42:33](https://youtu.be/975qcAxZCG0?t=2553)。例如三個節點都是 0.2，可以合併任兩個 [▶ 43:17](https://youtu.be/975qcAxZCG0?t=2597)。它們期望碼長一樣、都是最佳的，但碼不同。【口頭】**作業第 5 題特別小心**，去年很多同學在這裡出問題。
- **期望碼長的位置** [▶ 43:53](https://youtu.be/975qcAxZCG0?t=2633)：
$$H(X)\le\mathbb{E}\left[l_{\text{Huff}}(X)\right]\le\mathbb{E}\left[l_{\text{Shannon}}(X)\right]<H(X)+1.$$
（中間的 $\le$ 因為 Huffman 是最佳的。）對某些分布可以證更強的結果 [▶ 44:29](https://youtu.be/975qcAxZCG0?t=2669)。

---

## 7. 實作：用 heap 挑最小的兩個

【課堂討論】[▶ 45:13](https://youtu.be/975qcAxZCG0?t=2713) 怎麼有效率地挑出機率最小的兩個？學生答：**heap（堆積）或優先佇列**（priority queue）[▶ 45:53](https://youtu.be/975qcAxZCG0?t=2753)，可以一直取出最小（或最大）的元素。

- 沒效率的做法：每次排序清單、取最小兩個、放回新節點、再排序。也能用 [▶ 45:53](https://youtu.be/975qcAxZCG0?t=2753)。
- 【口頭】[▶ 46:27](https://youtu.be/975qcAxZCG0?t=2787) 很多時候 Huffman 碼建一次、用很多次，所以建構慢一點沒關係。

**SCL 的實作**（`scl/compressors/huffman_coder.py`，只描述）[▶ 47:08](https://youtu.be/975qcAxZCG0?t=2828)：

- 定義 `HuffmanNode`，用機率定義大小比較（`self.prob <= other.prob`）[▶ 47:48](https://youtu.be/975qcAxZCG0?t=2868)。
- `build_huffman_tree`：字母集只有一個符號就直接結束（遞迴的基本情況）；否則每個符號建一個節點放進清單，用 `heapify` 變成 heap [▶ 48:24](https://youtu.be/975qcAxZCG0?t=2904)；當 heap 裡不只一個節點時，pop 出最小的兩個，造一個機率相加的合併節點，push 回去 [▶ 49:02](https://youtu.be/975qcAxZCG0?t=2942)；最後剩的就是根。
- 拿掉註解不到 10–15 行 Python。

---

## 8. 解碼：為什麼不用樹，改用查表

### 8.1 用樹解碼的問題

[▶ 49:51](https://youtu.be/975qcAxZCG0?t=2991)（和作業第 4 題有關）第 2 集的樹解碼：照位元往下走到葉子。[▶ 51:13](https://youtu.be/975qcAxZCG0?t=3073) **實務上沒人這樣做**，原因是**分支太多**：每一步都是「是 0 往左、是 1 往右」的 if-else。

【口頭】[▶ 51:59](https://youtu.be/975qcAxZCG0?t=3119) 現代 CPU 用**管線化**（pipelining）同時處理一串指令；猜錯分支就要清空整條管線，白做很多工。就算有分支預測器，分支還是讓程式變很慢。

[▶ 52:31](https://youtu.be/975qcAxZCG0?t=3151) 為什麼在乎？**gzip 的熵編碼器就是 Huffman**，你每次從網路下載檔案，大概都有 Huffman 解碼在跑；舊的影片編碼也用 Huffman。電腦運作時，到處都在解前綴碼。用樹解碼，影片的吞吐量就不可能這麼高 [▶ 53:11](https://youtu.be/975qcAxZCG0?t=3191)。

### 8.2 查表解碼

[▶ 53:53](https://youtu.be/975qcAxZCG0?t=3233) 碼 A→`0`、B→`10`、C→`110`、D→`111`。兩張表：

`decode_state_table`（3 位元 → 符號）：

| 3 位元 | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| 符號 | A | A | A | A | B | B | C | D |

`encode_len`：A→1、B→2、C→3、D→3 [▶ 54:42](https://youtu.be/975qcAxZCG0?t=3282)。

【課堂討論】[▶ 55:18](https://youtu.be/975qcAxZCG0?t=3318) 這張表在做什麼？學生答：一次抓 3 個位元，查出對應的符號，再依碼長往前推進。[▶ 55:57](https://youtu.be/975qcAxZCG0?t=3357) 為什麼 000、001、010、011 都對到 A？學生答：開頭是 0 的都可以解成 A。講者：對，就是看**前綴**：開頭 0 → A；開頭 10 → B；110 → C；111 → D [▶ 56:29](https://youtu.be/975qcAxZCG0?t=3389)。

**解一個符號**（講者說這不是作業要做的；作業是建這些表）[▶ 57:07](https://youtu.be/975qcAxZCG0?t=3427)：

1. 從位元陣列取接下來 3 個位元當 `state`。
2. `s = decode_state_table[state]`：解出**一個**符號 [▶ 57:47](https://youtu.be/975qcAxZCG0?t=3467)。
3. `num_bits = encode_len[s]`：這個符號實際用了幾個位元。
4. 往前推進 `num_bits` 個位元 [▶ 58:23](https://youtu.be/975qcAxZCG0?t=3503)。

【課堂討論】[▶ 58:55](https://youtu.be/975qcAxZCG0?t=3535) 為什麼是 3？學生答：**最長碼字的長度**。

【Q&A】[▶ 58:55](https://youtu.be/975qcAxZCG0?t=3535) 學生問：什麼情況下會有這種位元陣列？講者：你把一大串 ABCD… 編成一長串位元 [▶ 59:28](https://youtu.be/975qcAxZCG0?t=3568)。第一次看第 1、2、3 位；若解出 A，只用了 1 位，下次看第 2、3、4 位；若再解出用 2 位的符號，下次看第 4、5、6 位。[▶ 1:00:00](https://youtu.be/975qcAxZCG0?t=3600) 學生追問為什麼會有這個陣列。講者：因為幾乎都不是只編一個符號，而是一長串，要能解回原本的序列；這就是為什麼要前綴碼，而不是像摩斯電碼在每個符號間加分隔 [▶ 1:00:33](https://youtu.be/975qcAxZCG0?t=3633)。

[▶ 1:01:06](https://youtu.be/975qcAxZCG0?t=3666) Pulkit 補充**結尾的邊界情況**：例如編 AB = `010`，讀 3 位解出 A，只剩 `10`；不夠 3 位就補 0，讀 `100` 解出 B，然後停 [▶ 1:01:45](https://youtu.be/975qcAxZCG0?t=3705)。

### 8.3 表的大小與受限 Huffman 碼

[▶ 1:02:23](https://youtu.be/975qcAxZCG0?t=3743)

- 表的大小是 $2^{\text{最大深度}}$。剛剛是 $2^3=8$。
- 實務上希望表**放得進快取**（cache），所以要**限制最大深度** [▶ 1:02:58](https://youtu.be/975qcAxZCG0?t=3778)。
- **受限 Huffman 碼**（constrained Huffman code，又叫 length-limited）：在最大深度限制下最好的碼 [▶ 1:02:58](https://youtu.be/975qcAxZCG0?t=3778)。建構比一般 Huffman 複雜一些；實務上常用的是這種，常限制在 16 或 24 這類位元組倍數 [▶ 1:03:50](https://youtu.be/975qcAxZCG0?t=3830)。去年有同學做成專題。

【口頭】[▶ 1:03:50](https://youtu.be/975qcAxZCG0?t=3830) 壓縮的很多功夫在很底層的地方。演算法好還不夠，如果要用複雜的樹，就處理不了大量資料。影片、log 都很大；純文字沒那麼大 [▶ 1:04:21](https://youtu.be/975qcAxZCG0?t=3861)。

### 8.4 費氏分布：最壞情況

[▶ 1:04:21](https://youtu.be/975qcAxZCG0?t=3861)【課堂討論】這個數列是什麼？學生答：**費氏數列**（Fibonacci）[▶ 1:05:11](https://youtu.be/975qcAxZCG0?t=3911)。

【投影片補充】`L4_ann.pdf` p.23：$P=\left(\frac1{33},\frac1{33},\frac2{33},\frac3{33},\frac5{33},\frac8{33},\frac{13}{33}\right)$；「Huffman code: HW!」；最大深度 $\approx|\mathcal{X}|$。

[▶ 1:05:11](https://youtu.be/975qcAxZCG0?t=3911) 回家自己做。這是**對抗性的情況**：碼字會非常長，最大深度大約等於符號數減 1 [▶ 1:05:55](https://youtu.be/975qcAxZCG0?t=3955)，例如 `111111…`。所以「實務上碼字都不會太長」不一定成立，限制最大深度是必要的。（課堂指定回家做，本筆記不寫解答。）

---

## 9. 實際例子：英文、程式碼、加密檔

[▶ 1:06:33](https://youtu.be/975qcAxZCG0?t=3993) 有人把鍵盤上每個字母的高度做成它在英文裡的頻率：E 最高，T 第二，A 第三。對這個分布造 Huffman 碼 [▶ 1:07:21](https://youtu.be/975qcAxZCG0?t=4041)：E 的碼字很短；Z、Q、X、J 這些少用的字母很長。

講者在家用 SCL 做的實驗 [▶ 1:07:21](https://youtu.be/975qcAxZCG0?t=4041)（照 Pulkit 的 SCL 教學安裝）：

| 檔案 | 觀察 | 原大小 → 壓縮後 |
|---|---|---|
| 《頑童歷險記》（Huckleberry Finn）英文文字 [▶ 1:08:00](https://youtu.be/975qcAxZCG0?t=4080) | 小寫 e 碼字很短；大寫 E 長很多（句首很少是 E）[▶ 1:08:38](https://youtu.be/975qcAxZCG0?t=4118) | 622,542 → 348,142 位元組，約少 44% [▶ 1:09:09](https://youtu.be/975qcAxZCG0?t=4149) |
| Apache Camel（Java 函式庫）原始碼 [▶ 1:09:43](https://youtu.be/975qcAxZCG0?t=4183) | 括號、分號的碼字比在英文裡短很多，因為程式碼裡多 | 約少 40% [▶ 1:10:35](https://youtu.be/975qcAxZCG0?t=4235) |
| AES 加密過的檔案 [▶ 1:10:35](https://youtu.be/975qcAxZCG0?t=4235) | 所有碼字**一樣長** | 壓縮率 1，完全沒壓縮 [▶ 1:13:33](https://youtu.be/975qcAxZCG0?t=4413) |

[▶ 1:10:35](https://youtu.be/975qcAxZCG0?t=4235) 重點：資料分布不同，Huffman 碼就長得很不一樣；任何分布都能造出它的最佳碼。

**加密檔**【課堂討論】[▶ 1:11:07](https://youtu.be/975qcAxZCG0?t=4267) 為什麼所有碼字一樣長？學生答：這就是第 1 集的固定長度碼……[▶ 1:11:40](https://youtu.be/975qcAxZCG0?t=4300) 講者：好的加密演算法輸出在位元組上**接近 iid 均勻**，不然會洩漏原始資料分布的資訊。這裡用的是 AES [▶ 1:12:15](https://youtu.be/975qcAxZCG0?t=4335)。每個位元組 0–255 機率一樣，每符號就是 8 位元。

> **教訓**：**加密過的資料壓不了。要壓縮，先壓再加密** [▶ 1:12:15](https://youtu.be/975qcAxZCG0?t=4335)。加密會破壞資料的所有結構，在壓縮器眼裡就是隨機的。
>
> 【口頭】[▶ 1:12:48](https://youtu.be/975qcAxZCG0?t=4368) 有人說他的新創能把任何檔案壓 50%，就丟一個加密檔給他。如果真能壓，他等於破解了 AES。

### 9.1 預告

[▶ 1:13:33](https://youtu.be/975qcAxZCG0?t=4413) Huffman 碼還有一兩個小主題下次講完。下一講由 Tsachy 教授講熵和分組編碼背後的理論直覺（為什麼是熵、分組為什麼有用、和大數法則的關係）[▶ 1:14:13](https://youtu.be/975qcAxZCG0?t=4453)；再下週開始講實用的分組碼／串流碼，它們非常接近熵，是現代最先進壓縮器用的方法 [▶ 1:14:49](https://youtu.be/975qcAxZCG0?t=4489)。

> ⚠️ 逐字稿缺字 [▶ 1:14:13](https://youtu.be/975qcAxZCG0?t=4453)：字幕「Professor Saki」應為 Tsachy（Weissman）。

---

## 10. 一頁速查表

### 二元熵函數

$$h_b(p)=p\log_2\frac1p+(1-p)\log_2\frac1{1-p}$$

$h_b(0)=h_b(1)=0$，$h_b(1/2)=1$，凹、對 $\frac12$ 對稱、在 $\frac12$ 附近很平。

### KL 散度（Bernoulli）

$D(\mathrm{Ber}(p)\|\mathrm{Ber}(q))=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}$；可以是 $\infty$（$q=0$、$p>0$）；不對稱。

### 最佳前綴碼的條件

1. $p_i>p_j\Rightarrow l_i\le l_j$。**關鍵一步**：交換碼字，差 $=-(p_i-p_j)(l_i-l_j)$。
2. 最長兩個碼字等長。**關鍵一步**：把最長的砍短，仍是前綴碼。
3. （課本）存在最佳碼，最長兩個只差最後一位、屬於機率最小的兩個符號。

### Huffman 演算法

```
節點 = 每個符號一個（機率）
當 節點數 > 1：
    取機率最小的兩個 a, b
    新節點 n：子節點 a, b，機率 = P(a) + P(b)
剩下的節點 = 根；左 0 右 1
```

- 最佳性**關鍵一步**：$L(p)=L^*(p')+p_{m-1}+p_m$，且 $L(p')=L^*(p)-p_{m-1}-p_m$ ⇒ 兩邊都最佳。
- $H\le\mathbb{E}[l_{\text{Huff}}]\le\mathbb{E}[l_{\text{Shannon}}]<H+1$。
- 平手 ⇒ 多個最佳碼；適用任意權重 $w_i\ge0$；用 heap 實作。

### 解碼

| 方法 | 做法 | 問題 |
|---|---|---|
| 樹 | 每位元一次分支 | 分支多，CPU 管線常被清空 |
| 查表 | 一次讀 $L_{\max}$ 位元，查符號，前進 $l(s)$ 位 | 表大小 $2^{L_{\max}}$ ⇒ 用受限 Huffman 碼限制深度 |

### 例子

| 分布 | 碼 | $\mathbb{E}[l]$ |
|---|---|---|
| $\mathrm{Ber}(0.001)$ Shannon | `0`、`1000000000` | 1.009（熵 0.011，88 倍） |
| $\mathrm{Ber}(0.001)$ 單符號最佳 | `0`、`1` | 1 |
| $\mathrm{Ber}(0.001)$ 兩個一組 Huffman | `0`、`10`、`110`、`111` | 0.501／符號 |
| $(0.35,0.25,0.2,0.12,0.08)$ Huffman | `00`、`01`、`10`、`110`、`111` | 2.2 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 分組編碼、熵的直覺、大數法則 | 第 5 集 AEP |
| 串流碼：比分組更好的接近熵方法 | 第 6 集算術編碼、第 7 集 ANS |
| 查表解碼、快取、分支 | 第 7 集 tANS（也用查表） |
| gzip 用 Huffman | 第 10 集 LZ77 與 gzip |
| JPEG 的「baseline DCT, Huffman coding」 | 第 15 集 JPEG |
| 加密資料壓不了、先壓再加密 | 第 10 集實務建議 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **最佳前綴碼要讓機率大的碼短、最長的兩個碼字等長；Huffman 演算法每次合併機率最小的兩個節點，就能造出最佳前綴碼（課本用「合併後仍最佳」的歸納法證明）。實務上用查表而不是走樹來解碼，並限制最大深度讓表放得進快取；加密過的資料接近均勻分布，壓不了。**

---

*筆記依據 Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 4 錄影逐字稿（人工字幕，1:15:09）、投影片 L4_ann 與 Cover & Thomas《Elements of Information Theory》2nd ed. §5.3、§5.6–5.8 整理。*
