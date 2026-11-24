---
course: Stanford EE274 Data Compression  Theory and Applications（2023 秋）
episode: 5
lecture: Lecture 5
date: 2023-10-11
video: https://youtu.be/yeKngztLcBs
notes: 本集沒有自己的投影片；後半用 L4_extended.pdf（34 頁）p.22–34。《Elements of Information Theory》第 3 章 §3.1–3.3、§5.4 Theorem 5.4.3
---

# 第 5 集 · Lecture 5：漸近均分性（Asymptotic Equipartition Property） [▶ 影片](https://youtu.be/yeKngztLcBs)

← 上一集：[04-huffman-codes](04-huffman-codes.md) ｜ [總目錄](README.md) ｜ 下一集：[06-arithmetic-coding](06-arithmetic-coding.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 5 集
> **講者**：前半 Tsachy Weissman（AEP、不匹配壓縮）；後半 Shubham Chandak（實驗圖、Huffman 收尾、小考）
> **來源**：YouTube 錄影逐字稿（1:20:03，人工字幕 en-US）＋ 投影片 `L4_extended.pdf`（第 4 集投影片的延伸版，後半用到）＋ Cover & Thomas 第 3 章、§5.4
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
- [1. 一個例子看懂 AEP](#1-一個例子看懂-aep)
- [2. 典型序列有多少個](#2-典型序列有多少個)
- [3. 典型集合只是極小的一部分](#3-典型集合只是極小的一部分)
- [4. 典型集合編碼器](#4-典型集合編碼器)
- [5. 為什麼叫「漸近均分」](#5-為什麼叫漸近均分)
- [6. 反向：不能低於熵](#6-反向不能低於熵)
- [7. 和分組 Shannon 碼比較](#7-和分組-shannon-碼比較)
- [8. 不匹配壓縮：KL 散度是代價](#8-不匹配壓縮kl-散度是代價)
- [9. 實驗：三種分組碼的比較](#9-實驗三種分組碼的比較)
- [10. Huffman 收尾：實際用在哪、標準碼表、典型 Huffman 碼](#10-huffman-收尾實際用在哪標準碼表典型-huffman-碼)
- [11. 小考檢討：「最佳」是對期望值說的](#11-小考檢討最佳是對期望值說的)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/yeKngztLcBs?t=5) Tsachy 開場先向家人朋友在以色列、巴勒斯坦地區的同學致意，說需要協助或通融可以找教學團隊；他說自己也是其中之一 [▶ 00:43](https://youtu.be/yeKngztLcBs?t=43)。

[▶ 00:43](https://youtu.be/yeKngztLcBs?t=43) 本集內容：

| 段落 | 講者 | 內容 | 課本 |
|---|---|---|---|
| [▶ 00:43](https://youtu.be/yeKngztLcBs?t=43)–[▶ 55:20](https://youtu.be/yeKngztLcBs?t=3320) | Tsachy | **AEP**（漸近均分性）和無損壓縮的根本限制；**不匹配壓縮** | §3.1–3.3、§5.4 |
| [▶ 55:20](https://youtu.be/yeKngztLcBs?t=3320)–[▶ 1:01:01](https://youtu.be/yeKngztLcBs?t=3661) | Shubham | 典型集合碼、Shannon 碼、Huffman 碼的實驗圖 | 無 |
| [▶ 1:01:01](https://youtu.be/yeKngztLcBs?t=3661)–結尾 | Shubham | Huffman 收尾（gzip、典型 Huffman 碼）、小考 | 無 |

[▶ 01:53](https://youtu.be/yeKngztLcBs?t=113) Tsachy：下學季的 EE276 會嚴謹地做；這裡只講**要點**，省掉 ε、δ，而且只用**一個例子**。懂了這個例子，就懂了 AEP。

---

## 1. 一個例子看懂 AEP

### 1.1 設定

[▶ 02:41](https://youtu.be/yeKngztLcBs?t=161) 要壓縮的資料是 $n$ 元組 $X^n=(X_1,X_2,\dots,X_n)$ [▶ 03:16](https://youtu.be/yeKngztLcBs?t=196)。最簡單又不無聊的例子：各分量 **iid**，都和 $X\sim\mathrm{Ber}(p)$ 同分布，也就是每個分量獨立擲一枚出現 1 的機率是 $p$ 的硬幣 [▶ 04:03](https://youtu.be/yeKngztLcBs?t=243)。

### 1.2 大數法則告訴我們的三件事

[▶ 04:03](https://youtu.be/yeKngztLcBs?t=243) 依**大數法則**，$X^n$ **以高機率**有這些性質：

1. 【課堂討論】[▶ 04:47](https://youtu.be/yeKngztLcBs?t=287) 大約有多少比例是 1？學生答：$p$。所以約有 $np$ 個 1 [▶ 05:19](https://youtu.be/yeKngztLcBs?t=319)。
2. 剩下的位置是 0：約 $n(1-p)$ 個 0 [▶ 05:55](https://youtu.be/yeKngztLcBs?t=355)。
3. 回頭問：**剛剛實現的這個序列，機率是多少？** [▶ 06:35](https://youtu.be/yeKngztLcBs?t=395)

（大寫 $P$ 表示序列的機率，小寫 $p$ 是 Bernoulli 參數。）

### 1.3 一個序列的機率

【課堂討論】[▶ 07:17](https://youtu.be/yeKngztLcBs?t=437) 某個特定序列（例如 `00110110`）的機率是多少？

- 一位學生答 $\frac1{2^n}$。講者：那是 $p=\frac12$ 時才對，那時所有序列一樣可能 [▶ 07:56](https://youtu.be/yeKngztLcBs?t=476)。
- 另一位學生答：要看有幾個 1，是 $p$ 的（1 的個數）次方乘 $(1-p)$ 的（0 的個數）次方 [▶ 08:30](https://youtu.be/yeKngztLcBs?t=510)。對。

**精確值** [▶ 08:30](https://youtu.be/yeKngztLcBs?t=510)：

$$P(x^n)=p^{\#\{1\text{ in }x^n\}}\,(1-p)^{\#\{0\text{ in }x^n\}}.$$

每個 1 貢獻一個 $p$，每個 0 貢獻一個 $1-p$ [▶ 09:11](https://youtu.be/yeKngztLcBs?t=551)。

**代入性質 1、2**（以高機率）[▶ 09:11](https://youtu.be/yeKngztLcBs?t=551)：

$$
\begin{aligned}
P(X^n)&\approx p^{np}(1-p)^{n(1-p)}\\
&=2^{\log_2\left(p^{np}(1-p)^{n(1-p)}\right)}&&\text{（}a=2^{\log_2a}\text{）}\\
&=2^{\,n\left[p\log_2p+(1-p)\log_2(1-p)\right]}\\
&=2^{-n\left[p\log_2\frac1p+(1-p)\log_2\frac1{1-p}\right]}\\
&=2^{-nH(X)}.
\end{aligned}
$$

【課堂討論】[▶ 11:46](https://youtu.be/yeKngztLcBs?t=706) 中括號裡這個東西眼熟嗎？就是 $X$ 的**熵** [▶ 12:39](https://youtu.be/yeKngztLcBs?t=759)：Bernoulli 兩個值，1 的機率 $p$ 給出 $p\log\frac1p$，0 的機率 $1-p$ 給出 $(1-p)\log\frac1{1-p}$。

> **以高機率，實現出來的序列，機率大約是 $2^{-nH}$。** [▶ 13:20](https://youtu.be/yeKngztLcBs?t=800)

---

## 2. 典型序列有多少個

[▶ 13:20](https://youtu.be/yeKngztLcBs?t=800) 一共有 $2^n$ 個二元序列。有多少個的機率約為 $2^{-nH}$？[▶ 14:38](https://youtu.be/yeKngztLcBs?t=878)

- 這些序列**合起來**的機率約為 1（大數法則：以高機率實現出來的序列有這個性質）。
- **每一個**的機率約為 $2^{-nH}$ [▶ 15:45](https://youtu.be/yeKngztLcBs?t=945)。

【課堂討論】[▶ 16:32](https://youtu.be/yeKngztLcBs?t=992) 所以有幾個？學生答：$2^{nH}$ [▶ 17:13](https://youtu.be/yeKngztLcBs?t=1033)。講者：每個的機率都差不多是同一個很小的數 $\varepsilon$，加起來約為 1，所以個數約為 $\frac1\varepsilon$ [▶ 17:58](https://youtu.be/yeKngztLcBs?t=1078)。這幾乎就是**這個集合上的均勻分布**。

> **約有 $2^{nH}$ 個這種序列，叫做典型序列（typical sequences）。** [▶ 18:43](https://youtu.be/yeKngztLcBs?t=1123)

[▶ 18:43](https://youtu.be/yeKngztLcBs?t=1123) 定義上的細節（EE276 會講）：有時「典型」要求三條性質都成立，有時只要求第 3 條（機率約 $2^{-nH}$），本質上一樣。

[▶ 19:26](https://youtu.be/yeKngztLcBs?t=1166) 小結：因為大數法則，看到的序列幾乎一定是典型的：約 $p$ 比例的 1、$1-p$ 比例的 0、機率約 $2^{-nH}$；這種序列約 $2^{nH}$ 個。

【課本補充】§3.1（書頁 57–60）的正式版本：

- **AEP**（Theorem 3.1.1）：$X_1,X_2,\dots$ iid $\sim p(x)$，則
$$-\frac1n\log_2p(X_1,\dots,X_n)\to H(X)\quad\text{（依機率收斂）}.$$
證明一行：$-\frac1n\log p(X^n)=\frac1n\sum_{i=1}^n\log\frac1{p(X_i)}$ 是 iid 隨機變數 $\log\frac1{p(X_i)}$ 的樣本平均，依弱大數法則收斂到 $\mathbb{E}\left[\log\frac1{p(X)}\right]=H(X)$。
- **典型集合** $A_\varepsilon^{(n)}$：滿足 $2^{-n(H+\varepsilon)}\le p(x^n)\le2^{-n(H-\varepsilon)}$ 的序列。
- 性質（Theorem 3.1.2）：
  1. $n$ 夠大時 $P\left(A_\varepsilon^{(n)}\right)>1-\varepsilon$。
  2. $\left|A_\varepsilon^{(n)}\right|\le2^{n(H+\varepsilon)}$。**關鍵一步**：$1\ge\sum_{x^n\in A}p(x^n)\ge|A|\,2^{-n(H+\varepsilon)}$。
  3. $n$ 夠大時 $\left|A_\varepsilon^{(n)}\right|\ge(1-\varepsilon)2^{n(H-\varepsilon)}$。**關鍵一步**：$1-\varepsilon<P(A)\le|A|\,2^{-n(H-\varepsilon)}$。

這就是課堂「每個約 $2^{-nH}$、合起來約 1、所以約 $2^{nH}$ 個」的嚴謹寫法。

---

## 3. 典型集合只是極小的一部分

[▶ 20:05](https://youtu.be/yeKngztLcBs?t=1205) 示意圖：所有二元序列的集合大小是 $2^n$ [▶ 20:47](https://youtu.be/yeKngztLcBs?t=1247)，裡面有一個**非常小**的子集合，就是典型集合，大小約 $2^{nH}$ [▶ 21:59](https://youtu.be/yeKngztLcBs?t=1319)。

所占比例 [▶ 22:36](https://youtu.be/yeKngztLcBs?t=1356)：

$$\frac{2^{nH}}{2^n}=2^{-n(1-H)}.$$

【課堂討論】[▶ 22:36](https://youtu.be/yeKngztLcBs?t=1356) $p\ne\frac12$ 時，$H$ 比 1 大還是小？學生答：**小** [▶ 23:30](https://youtu.be/yeKngztLcBs?t=1410)。所有 Bernoulli 裡熵最大的是 $\mathrm{Ber}(\frac12)$，熵為 1；其他都 $<1$。

所以 $1-H>0$，典型集合占的比例**隨 $n$ 指數變小** [▶ 24:13](https://youtu.be/yeKngztLcBs?t=1453)。圖沒按比例畫，其實它小到幾乎看不見。

> **這對壓縮影響很大：應該把所有編碼的力氣花在典型集合上**，因為要描述給解碼器的序列，幾乎一定在這個小集合裡 [▶ 24:13](https://youtu.be/yeKngztLcBs?t=1453)。

---

## 4. 典型集合編碼器

### 4.1 想法【課堂討論】

[▶ 25:04](https://youtu.be/yeKngztLcBs?t=1504) 能不能根據這個觀察設計一個接近熵的壓縮器？

[▶ 25:52](https://youtu.be/yeKngztLcBs?t=1552) 先想：如果**確定**序列在一個大小 $2^{nH}$ 的集合裡，要幾個位元？要在一個大小為 $N$ 的集合裡指出一個元素，大約需要 $\log N$ 位元（不計取整）[▶ 27:10](https://youtu.be/yeKngztLcBs?t=1630)。所以約 $nH$ 位元。

但現在只是「幾乎一定」在裡面。[▶ 28:02](https://youtu.be/yeKngztLcBs?t=1682) 一位學生提議：如果在集合裡，壓縮字串用一個旗標位元開頭，接著是它在典型集合裡的編號（約 $nH$ 位元）；不然就用另一個旗標開頭，接著直接寫原始序列。講者：好主意 [▶ 28:36](https://youtu.be/yeKngztLcBs?t=1716)。

### 4.2 方案

[▶ 28:36](https://youtu.be/yeKngztLcBs?t=1716)

1. 先輸出 **1 位元**，告訴解碼器序列是不是典型的。
2. 若**是**典型的 [▶ 29:16](https://youtu.be/yeKngztLcBs?t=1756)：接著用約 $nH$ 位元（$\log$ 典型集合大小）寫出它在典型集合裡的編號。
3. 若**不是** [▶ 30:00](https://youtu.be/yeKngztLcBs?t=1800)：直接用 $n$ 位元寫出整個序列。浪費一點沒關係。

（第 9 節 SCL 的實作用 0 代表典型、1 代表非典型，和學生的提議相反，不影響。）

### 4.3 期望碼長

[▶ 30:34](https://youtu.be/yeKngztLcBs?t=1834) 設 $\varepsilon_n=P(\text{不典型})$ [▶ 32:06](https://youtu.be/yeKngztLcBs?t=1926)：

$$\mathbb{E}\left[l(X^n)\right]\approx1+(1-\varepsilon_n)\,nH+\varepsilon_n\,n.$$

除以 $n$（每個信源符號）[▶ 32:06](https://youtu.be/yeKngztLcBs?t=1926)：

$$\frac{\mathbb{E}\left[l(X^n)\right]}{n}\approx\frac1n+(1-\varepsilon_n)H+\varepsilon_n\ \xrightarrow{\ n\to\infty\ }\ H.$$

因為 $\varepsilon_n\to0$（不典型的機率趨近 0）、$\frac1n\to0$ [▶ 33:05](https://youtu.be/yeKngztLcBs?t=1985)。

> **用越來越大的資料區塊，就能任意接近熵。** [▶ 33:05](https://youtu.be/yeKngztLcBs?t=1985)

【課本補充】§3.2 Theorem 3.2.1（書頁 61–62）：典型序列用 $\le n(H+\varepsilon)+1$ 位元編號、非典型用 $\le n\log|\mathcal{X}|+1$ 位元，各加 1 位元旗標，可得 $\mathbb{E}\left[\frac1nl(X^n)\right]\le H(X)+\varepsilon$（$n$ 夠大）。

---

## 5. 為什麼叫「漸近均分」

[▶ 34:15](https://youtu.be/yeKngztLcBs?t=2055) **漸近均分性**（Asymptotic Equipartition Property, AEP）：

- **漸近**：$n$ 夠大、大數法則開始起作用時。
- **均分**：所有事情都發生在一個小子集合裡，那裡實際上是**均勻分布**，每個典型序列機率都約 $2^{-nH}$ [▶ 34:56](https://youtu.be/yeKngztLcBs?t=2096)。

AEP 也隱含：可以任意接近每符號 $H$ 位元 [▶ 34:56](https://youtu.be/yeKngztLcBs?t=2096)。而且還隱含**不能更好**。

---

## 6. 反向：不能低於熵

[▶ 35:37](https://youtu.be/yeKngztLcBs?t=2137) 能不能用**少於** $H$ 位元／符號做無損壓縮？AEP 裡其實已經藏著答案：**不行**。

[▶ 36:17](https://youtu.be/yeKngztLcBs?t=2177) 給我任何壓縮器，假設它用 $nR$ 位元描述信源序列，也就是每符號 $R$ 位元。$nR$ 位元只能表示 $2^{nR}$ 個不同的序列 [▶ 36:17](https://youtu.be/yeKngztLcBs?t=2177)。

[▶ 37:37](https://youtu.be/yeKngztLcBs?t=2257) 若 $R<H$ [▶ 38:19](https://youtu.be/yeKngztLcBs?t=2299)：解碼器看到 $nR$ 位元，輸出只能是 $2^{nR}$ 個可能序列之一。這個「能重建的集合」的機率很小 [▶ 39:00](https://youtu.be/yeKngztLcBs?t=2340)：

- 它落在非典型區的部分：非典型區整體機率就可以忽略。
- 它落在典型區的部分：大小 $\le2^{nR}$，遠小於典型集合的 $2^{nH}$ [▶ 39:37](https://youtu.be/yeKngztLcBs?t=2377)。典型集合上幾乎是均勻分布，所以這部分的機率也很小。

[▶ 40:11](https://youtu.be/yeKngztLcBs?t=2411) 壓縮器成功的機率 = 信源序列落在某個大小 $2^{nR}$ 的集合裡的機率；$R<H$ 時這個機率可以忽略 [▶ 40:47](https://youtu.be/yeKngztLcBs?t=2447)。

> **$R<H$ 的壓縮器不可能是無損的。** 而且不只「不是無損」，它**以高機率會出錯**，因為實現的序列以高機率不在它會重建的集合裡 [▶ 41:24](https://youtu.be/yeKngztLcBs?t=2484)。

[▶ 42:18](https://youtu.be/yeKngztLcBs?t=2538) 總結：AEP 告訴我們，無損壓縮可以每符號任意接近 $H$；任何低於熵的方案都不可能無損。

> 以下**不是逐字稿內容**，是把「這部分機率也很小」算出來：典型區裡每個序列機率 $\le2^{-n(H-\varepsilon)}$，大小 $\le2^{nR}$ 的集合在典型區的機率 $\le2^{nR}\cdot2^{-n(H-\varepsilon)}=2^{-n(H-\varepsilon-R)}$。取 $\varepsilon<H-R$，它隨 $n$ 指數趨近 0；再加上非典型區的機率 $\le\varepsilon$。所以成功機率 $\to$ 很小。

【課本補充】§3.3（書頁 62–63）證明更強的版本：任何機率 $\ge1-\delta$ 的集合 $B_\delta^{(n)}$，大小至少約 $2^{nH}$（$\frac1n\log|B_\delta^{(n)}|>H-\delta'$）。也就是說，典型集合基本上已經是「最小的高機率集合」。

---

## 7. 和分組 Shannon 碼比較

【Q&A】[▶ 42:57](https://youtu.be/yeKngztLcBs?t=2577) 學生問：用 $n$ 個一組的分組碼，已經可以到熵的 $\frac1n$ 以內；這裡也是約 $\frac1n$。AEP 的方法比較好，還是一樣？

Tsachy：好問題，Shubham 等一下會用圖回答。[▶ 43:58](https://youtu.be/yeKngztLcBs?t=2638) 你說的對應到 **Shannon 碼**，那是另一種接近熵的方法：

$$l(x^n)=\left\lceil\log\frac1{P(x^n)}\right\rceil\le\log\frac1{P(x^n)}+1.$$

[▶ 45:19](https://youtu.be/yeKngztLcBs?t=2719)【課堂討論】$\mathbb{E}\left[\log\frac1{P(X^n)}\right]$ 是什麼？學生答：熵。所以

$$\frac{\mathbb{E}[l(X^n)]}{n}<\frac{H(X^n)+1}{n}=\frac{nH(X)+1}{n}=H(X)+\frac1n.$$

（iid ⇒ $H(X^n)=nH(X)$ [▶ 46:04](https://youtu.be/yeKngztLcBs?t=2764)。）

[▶ 46:47](https://youtu.be/yeKngztLcBs?t=2807) 哪個好？等一下看圖。但**實務上兩個都不是我們想要的**：時間和記憶體複雜度都隨 $n$ **指數成長** [▶ 47:30](https://youtu.be/yeKngztLcBs?t=2850)。典型集合編碼器雖然只需要典型集合大小的查表，那仍然是 $n$ 的指數。之後會講怎麼用合理的複雜度任意接近熵。

---

## 8. 不匹配壓縮：KL 散度是代價

[▶ 47:30](https://youtu.be/yeKngztLcBs?t=2850) **不匹配壓縮**（mismatched compression）。先不管 $n$ 元組，只看一個元素 [▶ 48:24](https://youtu.be/yeKngztLcBs?t=2904)。

[▶ 49:12](https://youtu.be/yeKngztLcBs?t=2952) 如果以為 $X$ 的分布是 $q$，就造 Shannon 碼：

$$l(x)=\left\lceil\log\frac1{q(x)}\right\rceil\approx\log\frac1{q(x)}$$

（「朋友之間差一個位元算什麼」，先忽略取整 [▶ 49:12](https://youtu.be/yeKngztLcBs?t=2952)。）

[▶ 49:50](https://youtu.be/yeKngztLcBs?t=2990) 但實際上 $X$ 的分布是 $p$。付出的代價是多少？[▶ 50:55](https://youtu.be/yeKngztLcBs?t=3055)

$$
\begin{aligned}
\mathbb{E}_p[l(X)]&=\sum_xp(x)\log\frac1{q(x)}\\
&=\sum_xp(x)\log\left(\frac1{p(x)}\cdot\frac{p(x)}{q(x)}\right)&&\text{（log 裡乘以 1）}\\
&=\sum_xp(x)\log\frac1{p(x)}+\sum_xp(x)\log\frac{p(x)}{q(x)}\\
&=H(X)+D(p\|q).
\end{aligned}
$$

【課堂討論】[▶ 53:08](https://youtu.be/yeKngztLcBs?t=3188) 第一項是熵；第二項學生答出來：**相對熵／KL 散度**（第 3 集證明下界時定義過）[▶ 53:45](https://youtu.be/yeKngztLcBs?t=3225)。

> **$D(p\|q)$ 就是不匹配的代價**：用為 $q$ 設計的壓縮器去壓實際上來自 $p$ 的資料，平均要多付 $D(p\|q)$ 位元 [▶ 54:33](https://youtu.be/yeKngztLcBs?t=3273)。它永遠 $\ge0$（本來就不可能贏過熵），$q$ 離 $p$ 越遠代價越大。

【課本補充】§5.4 Theorem 5.4.3（書頁 115）把取整也算進去：$H(p)+D(p\|q)\le\mathbb{E}_p[l(X)]<H(p)+D(p\|q)+1$。

---

## 9. 實驗：三種分組碼的比較

### 9.1 典型集合碼的 SCL 實作

[▶ 55:20](https://youtu.be/yeKngztLcBs?t=3320) 換 Shubham。[▶ 55:59](https://youtu.be/yeKngztLcBs?t=3359) SCL 實作了典型集合編碼器（只描述）：

- `is_typical`：檢查一個序列是不是典型的。
- 產生典型集合的碼表：走過所有 $n$ 元組，檢查是否典型，再依序編號。
- 編碼 [▶ 56:40](https://youtu.be/yeKngztLcBs?t=3400)：如果這段是典型的，輸出 0 加上它在典型集合裡的編號；否則輸出 1 加上它在全部序列裡的編號。

[▶ 56:40](https://youtu.be/yeKngztLcBs?t=3400) 很慢，因為複雜度是指數的：區塊 10 沒問題、20 要好幾分鐘、30 跑不完。所以實驗只跑到 10。

### 9.2 壓縮率

[▶ 57:54](https://youtu.be/yeKngztLcBs?t=3474) 三種碼：Huffman、Shannon、典型集合碼（「大約等於」有一個參數，選了合理的值）。信源 $\mathrm{Ber}(0.01)$：

- 紅色虛線（最下面）：熵，最好只能到這裡。
- 紫色虛線：$H+\frac1n$ 的上界；它對 Shannon 碼成立，所以對 Huffman 碼也成立 [▶ 58:29](https://youtu.be/yeKngztLcBs?t=3509)。

觀察 [▶ 58:29](https://youtu.be/yeKngztLcBs?t=3509)：

- 三種碼都不錯，彼此很接近。
- **Huffman 最好**（在最下面），因為它是最佳的。
- 典型集合碼和 Shannon 碼看區塊大小，互有勝負。
- 區塊 10 還沒到熵，但有 $H+\frac1n$ 的保證：區塊 20 就在熵的 0.05 以內，越大越近。

### 9.3 複雜度

[▶ 59:13](https://youtu.be/yeKngztLcBs?t=3553) 三種碼**建碼表**都是指數複雜度：典型集合碼要走過所有序列；Shannon 碼和 Huffman 碼也要處理每個序列、建樹。**存**碼表也是指數的。

[▶ 59:13](https://youtu.be/yeKngztLcBs?t=3553) 下圖：建碼表時間對區塊大小。[▶ 59:55](https://youtu.be/yeKngztLcBs?t=3595) Huffman 花的時間最多（合併節點的工作多），但相對快慢也和實作有關，別太在意。改用對數座標：三條都接近直線，**對數座標上的直線 = 指數成長** [▶ 1:00:26](https://youtu.be/yeKngztLcBs?t=3626)。

> 結論：三種都無法放大。用它們就只能用小區塊，也就拿不到熵。接下來兩講要學的方法，等於能用**很大的區塊**，卻沒有指數複雜度 [▶ 1:00:26](https://youtu.be/yeKngztLcBs?t=3626)。

[▶ 1:01:01](https://youtu.be/yeKngztLcBs?t=3661) 這是最後一堂理論課，之後大約五講都是演算法。

---

## 10. Huffman 收尾：實際用在哪、標準碼表、典型 Huffman 碼

### 10.1 回顧

[▶ 1:01:40](https://youtu.be/yeKngztLcBs?t=3700) Huffman 樹的建構、最佳性、真實資料的例子、查表解碼（作業會做）。

### 10.2 Huffman 碼用在哪

[▶ 1:01:40](https://youtu.be/yeKngztLcBs?t=3700) 很多常用格式的最後一步都用 Huffman 做熵編碼，例如 **JPEG** [▶ 1:02:18](https://youtu.be/yeKngztLcBs?t=3738)。

【投影片補充】`L4_extended.pdf` p.27「Huffman coding in practice」：Deflate/gzip（RFC 1951）、HTTP/2 標頭壓縮（RFC 7541 附錄 B）、JPEG 的 Huffman 碼表（ITU-T T.81）。p.28 是 JPEG 標準裡亮度 DC 係數差的典型 Huffman 碼表（Table K.3）。

### 10.3 解碼器怎麼知道用哪個 Huffman 碼？

[▶ 1:02:18](https://youtu.be/yeKngztLcBs?t=3738) 以 **Deflate**（gzip 的格式，RFC）為例。作業第 5 題的問題：解碼器要怎麼知道編碼器用的是哪個 Huffman 碼？[▶ 1:03:01](https://youtu.be/yeKngztLcBs?t=3781) 三種做法：

1. 把**機率分布**傳過去，解碼器自己建樹（作業的做法）[▶ 1:04:10](https://youtu.be/yeKngztLcBs?t=3850)。
2. 把 **Huffman 碼本身**傳過去。
3. **固定 Huffman 碼**（RFC 3.2.6 節）[▶ 1:03:01](https://youtu.be/yeKngztLcBs?t=3781)：看過大量資料、找一個合理的分布，造一個標準碼表寫死在格式裡，編碼器和解碼器都有。很多 gzip 檔就用這個。像超參數一樣事先定好 [▶ 1:03:37](https://youtu.be/yeKngztLcBs?t=3817)。

格式也支援**動態 Huffman 碼** [▶ 1:03:37](https://youtu.be/yeKngztLcBs?t=3817)。gzip 不傳機率分布 [▶ 1:04:10](https://youtu.be/yeKngztLcBs?t=3850)。【口頭】建議第 10 講之後讀完 gzip 格式的 RFC：每一個位元他們都想兩次，「怎麼省下這一位元又保持很快」。JPEG 格式裡也有固定的 Huffman 碼表 [▶ 1:04:46](https://youtu.be/yeKngztLcBs?t=3886)。

### 10.4 典型 Huffman 碼

[▶ 1:04:46](https://youtu.be/yeKngztLcBs?t=3886) Huffman 碼**不唯一** [▶ 1:05:53](https://youtu.be/yeKngztLcBs?t=3953)：平手怎麼斷、左右子節點怎麼放都有彈性。所以編碼器和解碼器必須做**完全一樣**的事，不然整個壞掉。【口頭】去年很多人在作業第 5 題栽在這裡。

**例**（`L4_extended.pdf` p.29）：

| 符號 | 碼 1 | 碼 2 |
|---|---|---|
| A | `00` | `10` |
| B | `1` | `0` |
| C | `011` | `110` |
| D | `010` | `111` |

兩個碼的碼長一樣，期望碼長也一樣。[▶ 1:06:28](https://youtu.be/yeKngztLcBs?t=3988) 碼 1 **不是典型的**：短碼字在右、長碼字在左；C、D 一樣長，但字母序較小的 C 在右邊。

**典型碼**（canonical code）的兩條規則 [▶ 1:06:59](https://youtu.be/yeKngztLcBs?t=4019)：

1. **依碼長排序**：由左到右越來越長（左邊的不比右邊的長）。
2. **同長度依字母序**：字母序小的在左（C 在 D 左邊；A、B 同長則 A 在左）。

可以證明：任何 Huffman 碼都能調整成典型碼（移動樹的枝葉即可）[▶ 1:06:59](https://youtu.be/yeKngztLcBs?t=4019)。碼 2 就是典型的。

### 10.5 只傳碼長就夠了【課堂討論】

[▶ 1:07:43](https://youtu.be/yeKngztLcBs?t=4063) 典型碼的好處：**不用傳機率、不用傳樹的結構，只要傳每個符號的碼長**，就能重建碼本。例：A 長 2、B 長 1、C 長 3、D 長 3：

1. 從最短的開始：B 長 1，必須在所有碼字左邊 → B = `0` [▶ 1:08:16](https://youtu.be/yeKngztLcBs?t=4096)。
2. 下一個？學生答 A。A 的碼字？學生答 `10`：一路由左到右，只有這個可能 [▶ 1:08:51](https://youtu.be/yeKngztLcBs?t=4131)。
3. C、D 都長 3，哪個在左？C（典型碼的規則）→ C = `110`、D = `111`。

非常精簡，解碼端重建也便宜。**gzip 的動態模式就用典型 Huffman 碼** [▶ 1:09:28](https://youtu.be/yeKngztLcBs?t=4168)。

> 以下**不是逐字稿內容**，是把重建步驟寫成通用演算法（依上面的規則推出來的）：把符號依（碼長, 字母序）排序；`code = 0`；對排好的每個符號：若它比前一個長，就把 `code` 左移補 0 到新長度；指定 `code`（用該長度的二進位表示）；再 `code += 1`。例：B(1) → `0`；A(2)：`code` 變 1、左移成 `10` → A = `10`；C(3)：`code` 變 11、左移成 `110` → C = `110`；D(3)：`111`。

### 10.6 碼長本身怎麼存？【課堂討論】

[▶ 1:09:28](https://youtu.be/yeKngztLcBs?t=4168) 碼長要放進壓縮檔裡，怎麼存？例如知道碼長最多 8。[▶ 1:10:19](https://youtu.be/yeKngztLcBs?t=4219) 碼長本身也要是前綴碼（不然另一邊讀不出來）。簡單做法：最大長度 8 就每個碼長用 3 位元。

gzip 更省 [▶ 1:11:06](https://youtu.be/yeKngztLcBs?t=4266)：RFC 說兩個字母集的 Huffman 碼放在區塊標頭之後，每個碼用典型描述的碼長序列來定義；**為了更精簡，碼長序列本身再用 Huffman 碼壓縮**。也就是用 Huffman 碼壓資料，再用另一個 Huffman 碼描述那個 Huffman 碼。

[▶ 1:11:43](https://youtu.be/yeKngztLcBs?t=4303) gzip 的結構：

```
資料串流 ──(動態 Huffman 碼)──> 位元
動態碼的碼長序列 ──(靜態 Huffman 碼，碼表寫死)──> 位元
```

---

## 11. 小考檢討：「最佳」是對期望值說的

### 11.1 第 1 題

[▶ 1:12:23](https://youtu.be/yeKngztLcBs?t=4343)

| 題 | 問題 | 答案 |
|---|---|---|
| 1.1 | $\mathrm{Ber}(0.5)$ 的 Huffman 碼 | `0`、`1` [▶ 1:13:00](https://youtu.be/yeKngztLcBs?t=4380) |
| 1.2 | $\mathrm{Ber}(0.9)$ 的 Huffman 碼 | 一樣是 `0`、`1` |
| 1.3 | $\mathrm{Ber}(0.5)$ 不可能比上面的 Huffman 碼更好？ | **對**：熵是 1 [▶ 1:13:31](https://youtu.be/yeKngztLcBs?t=4411) |
| 1.4 | $\mathrm{Ber}(0.9)$ 不可能比上面的 Huffman 碼更好？ | **錯**：熵 $<1$ |

【課堂討論】[▶ 1:13:31](https://youtu.be/yeKngztLcBs?t=4411) 1.4 怎麼和「Huffman 最佳」相容？學生答：**用分組碼** [▶ 1:14:08](https://youtu.be/yeKngztLcBs?t=4448)。講者：如果規定一次只能編一個符號，那它確實最佳；但題目沒這樣規定。如果你是這樣假設才答「對」的，可以來談。

### 11.2 第 2 題：Gandhi 碼

[▶ 1:14:43](https://youtu.be/yeKngztLcBs?t=4483) $\mathcal{X}=\{A,B,C,D\}$ 均勻分布。Huffman 碼就是固定長度碼。另一個前綴碼（題目叫它「Gandhi 碼」）：

| 符號 | Huffman | Gandhi |
|---|---|---|
| A | `00` | `0` |
| B | `01` | `10` |
| C | `10` | `110` |
| D | `11` | `111` |

特定序列 `AAABBBCD` [▶ 1:15:23](https://youtu.be/yeKngztLcBs?t=4523)：

- Gandhi：`0 0 0 10 10 10 110 111` → **15 位元**。
- Huffman：8 個符號 × 2 = **16 位元**。

在這個序列上 Gandhi 碼贏了 Huffman。

| 題 | 敘述 | 答案 |
|---|---|---|
| 2.3 | Gandhi 碼對這個信源是最佳的 | **錯** [▶ 1:16:00](https://youtu.be/yeKngztLcBs?t=4560) |
| 2.4 | Gandhi 碼對這個信源的**這個特定實例**是最佳的 | **對** |

> ⚠️ 逐字稿缺字 [▶ 1:16:00](https://youtu.be/yeKngztLcBs?t=4560)：講者說「oh, sorry, this should be 2.3, 2.4」，投影片上題號原本寫成 2.1、2.2，手寫改成 2.3、2.4。

**重點** [▶ 1:16:47](https://youtu.be/yeKngztLcBs?t=4607)：信源是**機率性的**。說一個碼「最佳」，意思是**期望碼長**最小（Huffman 給出最小期望碼長），**不是**在每一個實現的序列上都最短。不可能有一個碼在每個序列上都贏過其他所有碼：如果只要傳某一個特定序列，又允許分組，就把那個序列的碼定成 `0`，其他隨便。

[▶ 1:17:34](https://youtu.be/yeKngztLcBs?t=4654) 這就是作弊。傳東西有意義，是因為**有不確定性**；所以我們在機率的設定下工作，解碼器事先不知道你要傳什麼。

【口頭】[▶ 1:17:34](https://youtu.be/yeKngztLcBs?t=4654) 壓縮比賽常有這種作弊：解壓縮器裡直接內建整個檔案，壓縮器只送 1 個位元組，解壓縮器收到就展開成整個檔案 [▶ 1:18:17](https://youtu.be/yeKngztLcBs?t=4697)。所以這類比賽會**限制解壓縮器的大小**。

[▶ 1:18:17](https://youtu.be/yeKngztLcBs?t=4697) 對這個特定實例：A 出現 $\frac38$、B $\frac38$、C $\frac18$、D $\frac18$。用這個分布造 Huffman 碼，得到的就是 Gandhi 碼 [▶ 1:19:01](https://youtu.be/yeKngztLcBs?t=4741)，所以它對這個實例是最佳的。

> 以下**不是逐字稿內容**，是算出來對照：對**均勻**信源，Gandhi 碼的期望碼長 $\frac14(1+2+3+3)=2.25>2$，所以平均而言比 Huffman 差。

### 11.3 預告

[▶ 1:19:01](https://youtu.be/yeKngztLcBs?t=4741) 下一講開始講**實用的碼**：不只更接近熵，對**自適應**方案、**非 iid** 信源、不想事先假設分布的情況也非常重要 [▶ 1:19:35](https://youtu.be/yeKngztLcBs?t=4775)。

> ⚠️ 逐字稿缺字 [▶ 55:20](https://youtu.be/yeKngztLcBs?t=3320)：字幕「Thank you, Saki」應為 Tsachy。

---

## 12. 一頁速查表

### AEP（iid $X_i\sim p$）

$$-\frac1n\log_2P(X^n)\ \to\ H(X)\quad\text{（以高機率）}$$

- **關鍵一步**：$-\frac1n\log P(X^n)=\frac1n\sum_i\log\frac1{p(X_i)}$，大數法則 $\to\mathbb{E}\left[\log\frac1{p(X)}\right]=H$。
- Bernoulli 版：約 $np$ 個 1 ⇒ $P(X^n)\approx p^{np}(1-p)^{n(1-p)}=2^{-nH}$。

### 典型集合

| 性質 | 值 | 關鍵一步 |
|---|---|---|
| 每個序列的機率 | $\approx2^{-nH}$ | AEP |
| 總機率 | $\approx1$ | 大數法則 |
| 個數 | $\approx2^{nH}$ | $1\approx|A|\cdot2^{-nH}$ |
| 占全部的比例（二元） | $2^{-n(1-H)}$ | $H<1$ 時指數變小 |

### 典型集合編碼器

1 位元旗標 + （典型：$\approx nH$ 位元編號；不典型：$n$ 位元原樣）

$$\frac{\mathbb{E}[l]}{n}\approx\frac1n+(1-\varepsilon_n)H+\varepsilon_n\to H$$

### 反向

$R<H$ 位元／符號 ⇒ 只能重建 $2^{nR}$ 個序列 ⇒ 落在典型集合的機率 $\lesssim2^{-n(H-R)}\to0$ ⇒ 不可能無損，以高機率出錯。

### 不匹配壓縮

$$\mathbb{E}_p\left[\log\frac1{q(X)}\right]=H(p)+D(p\|q)$$

**關鍵一步**：$\log\frac1q=\log\frac1p+\log\frac pq$。

### 典型 Huffman 碼

- 規則：碼長由左到右遞增；同長度依字母序。
- 只要傳碼長就能重建碼本；gzip 動態模式用它，碼長序列再用靜態 Huffman 碼壓。

### 「最佳」的意思

期望碼長最小，不是每個實現都最短。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 分組碼複雜度指數成長 ⇒ 需要串流碼 | 第 6 集算術編碼、第 7 集 ANS |
| 不匹配代價 $D(p\|q)$ | 第 8–10 集（模型、自適應、通用壓縮） |
| 典型序列、AEP | 第 12 集率失真（有損壓縮的典型性論證） |
| gzip 的動態／靜態 Huffman | 第 10 集 LZ77 與 gzip |
| JPEG 用 Huffman | 第 15 集 JPEG |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **iid 信源的 $n$ 元組以高機率是「典型的」：機率約 $2^{-nH}$，這種序列約 $2^{nH}$ 個，只占全部的指數小一部分。所以用約 $nH$ 位元給典型序列編號，就能任意接近熵；少於 $H$ 位元只能涵蓋可忽略的機率，不可能無損。用錯分布 $q$ 去壓 $p$ 的資料，代價正好是 $D(p\|q)$。這些分組方法都是指數複雜度，所以需要下一講的串流碼。**

---

*筆記依據 Tsachy Weissman、Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 5 錄影逐字稿（人工字幕，1:20:03）、投影片 L4_extended 與 Cover & Thomas《Elements of Information Theory》2nd ed. §3.1–3.3、§5.4 整理。*
