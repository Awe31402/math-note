---
course: Stanford EE274 Data Compression  Theory and Applications（2023 秋）
episode: 3
lecture: Lecture 3
date: 2023-10-04
video: https://youtu.be/kbAif7XhlTI
notes: 投影片 L3_ann.pdf（39 頁，手寫）；《Elements of Information Theory》§2.1、§2.3、§2.6、§5.2–5.4
---

# 第 3 集 · Lecture 3：Kraft 不等式、熵、SCL 入門（Kraft Inequality, Entropy, Introduction to SCL） [▶ 影片](https://youtu.be/kbAif7XhlTI)

← 上一集：[02-prefix-free-codes](02-prefix-free-codes.md) ｜ [總目錄](README.md) ｜ 下一集：[04-huffman-codes](04-huffman-codes.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 3 集
> **講者**：Shubham Chandak
> **來源**：YouTube 錄影逐字稿（1:17:02，人工字幕 en-US）＋ 投影片 `L3_ann.pdf`（上課手寫版）＋ Cover & Thomas §2.1、§2.3、§2.6、§5.2–5.4
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
- [1. SCL：Stanford Compression Library](#1-sclstanford-compression-library)
- [2. Kraft 不等式](#2-kraft-不等式)
- [3. 小考檢討：用 Kraft 和來檢查碼](#3-小考檢討用-kraft-和來檢查碼)
- [4. 熵](#4-熵)
- [5. 獨立隨機變數的聯合熵](#5-獨立隨機變數的聯合熵)
- [6. KL 散度（相對熵）](#6-kl-散度相對熵)
- [7. 無損壓縮的主定理](#7-無損壓縮的主定理)
- [8. 證明下界：$\mathbb{E}[l(X)]\ge H(X)$](#8-證明下界mathbbelxge-hx)
- [9. 可達性：Shannon 碼離熵不到 1 位元](#9-可達性shannon-碼離熵不到-1-位元)
- [10. 分組編碼：任意接近熵](#10-分組編碼任意接近熵)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:05](https://youtu.be/kbAif7XhlTI?t=5) 這是**最後一堂偏理論的無損壓縮課**，之後大多是演算法。三個主題：

| 主題 | 課本 |
|---|---|
| Kraft 不等式 | §5.2 |
| 熵 | §2.1、§2.6 |
| 無損壓縮的根本限制（主定理） | §5.3–5.4 |

[▶ 00:37](https://youtu.be/kbAif7XhlTI?t=37) 後兩個主題是無損壓縮的**主要結果**：最好能壓到多少。接下來好幾講都在想辦法達到它。

【投影片補充】`L3_ann.pdf` p.2 公告：IT Forum 10/6（五）下午 2 點，Packard 202，UCSC 的 Jouni Sirén 講基因體壓縮；網站上有程式片段；SCL 教學；作業 1。

【Q&A】[▶ 01:09](https://youtu.be/kbAif7XhlTI?t=69) 學生問作業能不能一起討論。講者：可以，但**作業要各自交**；期末專題可以分組。

---

## 1. SCL：Stanford Compression Library

### 1.1 為什麼做 SCL

[▶ 02:15](https://youtu.be/kbAif7XhlTI?t=135) 學壓縮時懂了理論和演算法，想找實作來用，常常只找到很底層的 C 程式（甚至用 SIMD），初學者看不懂 [▶ 02:53](https://youtu.be/kbAif7XhlTI?t=173)。而且「懂演算法」不等於「寫得出來」，自己實作才會發現理解上的漏洞。

所以課程團隊從去年開始寫 SCL [▶ 03:30](https://youtu.be/kbAif7XhlTI?t=210)：

- 常見壓縮演算法的**研究用實作**：目標不是最快，而是**看得懂**。
- 一個**框架**，讓人可以改現有的壓縮器、做研究。
- 【口頭】自私的理由：自稱壓縮研究者，自己至少要實作過。

【口頭】[▶ 01:42](https://youtu.be/kbAif7XhlTI?t=102) 如果不熟 Python 或這種寫法的 Python 而卡住，馬上找助教。

### 1.2 快速導覽

[▶ 04:06](https://youtu.be/kbAif7XhlTI?t=246) 用 Fall 23 的網站（Google 有時會連到 Fall 22 的舊網站）。作業在 assignments 分頁；logistics → useful links 第一個就是 SCL（GitHub）。

[▶ 04:39](https://youtu.be/kbAif7XhlTI?t=279) 內容（只描述，不寫程式碼）：

- **utils**：
  - 位元陣列工具 [▶ 05:50](https://youtu.be/kbAif7XhlTI?t=350)：機器以位元組運作，但很多壓縮演算法以位元運作，需要整數 ↔ 位元陣列等轉換。作業的起始程式會提示該用哪些函式。
  - 樹的工具 [▶ 06:24](https://youtu.be/kbAif7XhlTI?t=384)：上一集的演算法都用樹。
  - 機率分布工具：排序、正規化、累積分布（Shannon 碼就需要排序）。
- **compressors** [▶ 07:00](https://youtu.be/kbAif7XhlTI?t=420)：例如前綴碼解碼器。它的結構就是上一集的演算法：
  - 解一個區塊（decode block）：只要還有位元沒讀，就一次解一個符號 [▶ 07:33](https://youtu.be/kbAif7XhlTI?t=453)。
  - 解一個符號 [▶ 08:11](https://youtu.be/kbAif7XhlTI?t=491)：已讀位元數設 0、目前節點設成根，往下走到葉子就輸出。
- 也有其他更有效率的熵編碼器、外部函式庫、安裝說明。

[▶ 08:41](https://youtu.be/kbAif7XhlTI?t=521) 本週會出 SCL 教學。去年很多期末專題是擴充 SCL，再貢獻回去。

---

## 2. Kraft 不等式

### 2.1 回顧

[▶ 09:44](https://youtu.be/kbAif7XhlTI?t=584) 上一集：前綴碼、用樹解碼、好的碼 $l(x)\approx\log_2\frac{1}{P(x)}$、Shannon 碼 $l(x)=\left\lceil\log_2\frac1{P(x)}\right\rceil$ 和它的建構證明。[▶ 10:51](https://youtu.be/kbAif7XhlTI?t=651) 上次的證明沒跟上沒關係，今天的證明很像。

### 2.2 定理

[▶ 10:51](https://youtu.be/kbAif7XhlTI?t=651) 上一集用文字刻畫前綴碼（碼字在二元樹的葉子上）；今天給一個**數學**刻畫：

> **Kraft 不等式**（Kraft's inequality）[▶ 11:57](https://youtu.be/kbAif7XhlTI?t=717)
> - **正向**：任何前綴碼，碼長 $l_1,\dots,l_k$ 都滿足 $\displaystyle\sum_{i=1}^{k}2^{-l_i}\le1$。
> - **反向**（converse）[▶ 12:30](https://youtu.be/kbAif7XhlTI?t=750)：給任意正整數 $l_1,\dots,l_k$ 滿足 $\sum_i2^{-l_i}\le1$，就**存在**一個碼長為 $l_1,\dots,l_k$ 的前綴碼。

所以：碼字在葉子上 ⟺ 前綴碼 ⟺ 碼長滿足 Kraft 不等式（`L3_ann.pdf` p.7 的圖）。

【課本補充】§5.2 Theorem 5.2.1 寫的是 $D$ 元版本：$\sum_iD^{-l_i}\le1$。

### 2.3 反向的證明

[▶ 13:06](https://youtu.be/kbAif7XhlTI?t=786) 和 Shannon 碼的建構一模一樣：把長度排序，依序在樹上挑不違反前綴條件的節點。上一集的證明只用到 $\sum2^{-l(x)}\le1$ 這件事，所以對任何滿足 Kraft 不等式的長度都成立。

### 2.4 正向的證明（概要）

[▶ 13:44](https://youtu.be/kbAif7XhlTI?t=824) 設 $l_{\max}=\max\{l_1,\dots,l_k\}$，最長的碼字長度。[▶ 14:54](https://youtu.be/kbAif7XhlTI?t=894)

1. 第 $i$ 個碼字在深度 $l_{\max}$ 有 $2^{\,l_{\max}-l_i}$ 個後代 [▶ 15:31](https://youtu.be/kbAif7XhlTI?t=931)。（深度 $n$ 的完整二元樹有 $2^n$ 個葉子；從深度 $l_i$ 走到 $l_{\max}$ 是一棵高 $l_{\max}-l_i$ 的子樹。）
2. 不同碼字的後代**不重疊** [▶ 16:06](https://youtu.be/kbAif7XhlTI?t=966)：前綴碼的碼字是樹上不同的分支。
3. 互不相交的子集合，大小加起來不超過全集 [▶ 16:39](https://youtu.be/kbAif7XhlTI?t=999)。深度 $l_{\max}$ 一共 $2^{l_{\max}}$ 個節點：

$$\sum_{i=1}^{k}2^{\,l_{\max}-l_i}\le2^{\,l_{\max}}\quad\Longrightarrow\quad\sum_{i=1}^{k}2^{-l_i}\le1.$$

（最後一步是兩邊除以 $2^{l_{\max}}$。）

【Q&A】[▶ 17:17](https://youtu.be/kbAif7XhlTI?t=1037) 學生問：$l_i$ 是走到葉子之前經過的分支數嗎？講者：對，就是深度，也就是碼字長度。例如圖上 $l_1=1$、$l_2=3$。

[▶ 17:49](https://youtu.be/kbAif7XhlTI?t=1069) 這是最後一次用樹的證明。

[▶ 18:22](https://youtu.be/kbAif7XhlTI?t=1102) 上一集還有更大的類別「唯一可解碼碼」。今天證的是前綴碼版；**作業要證唯一可解碼碼也滿足 Kraft 不等式**，那是更強的結果、證法也很不一樣。

【課本補充】§5.5 Theorem 5.5.1（McMillan）就是唯一可解碼版的 Kraft 不等式。這是作業題，這裡不寫證明。

---

## 3. 小考檢討：用 Kraft 和來檢查碼

### 3.1 第 1 題：Shannon 碼【課堂討論】

[▶ 18:59](https://youtu.be/kbAif7XhlTI?t=1139) 分布和長度（`L3_ann.pdf` p.11）：

| $x$ | $P(x)$ | $l(x)=\left\lceil\log_2\frac1{P(x)}\right\rceil$ | Shannon 碼 | 更好的碼 |
|---|---|---|---|---|
| A | 0.25 | 2 | `00` | `00` |
| B | 0.25 | 2 | `01` | `01` |
| C | 0.25 | 2 | `10` | `10` |
| D | 0.13 | 3 | `110` | `111` |
| E | 0.12 | 4 | `1110` | `110` |

[▶ 19:35](https://youtu.be/kbAif7XhlTI?t=1175) 學生依序幫忙挑：A 選 `00`；B 選 `01`；C 選 `10`（講者說照字典順序比較簡單）；D 選 `110`（不能選 `100`，`10` 已經是 C 的了）[▶ 20:07](https://youtu.be/kbAif7XhlTI?t=1207)；E 一定要長度 4，選 `1110`。【口頭】明明 `111` 可以用，但 Shannon 碼規定長度就得是 4，所以不是最佳。

**期望碼長** [▶ 20:42](https://youtu.be/kbAif7XhlTI?t=1242)：

$$0.25\times2\times3+0.13\times3+0.12\times4=1.5+0.39+0.48=2.37\ \text{位元／符號}$$

**Kraft 和**（講者說本來想出在小考上，沒來得及）[▶ 21:17](https://youtu.be/kbAif7XhlTI?t=1277)：

$$3\times\frac1{2^2}+\frac1{2^3}+\frac1{2^4}=\frac34+\frac18+\frac1{16}=\frac{15}{16}<1$$

滿足 Kraft 不等式，但**有缺口**（不等於 1）。

**更好的碼** [▶ 21:52](https://youtu.be/kbAif7XhlTI?t=1312)：E 的長度改成 3（`110` 不是任何碼字的前綴）。

$$\mathbb{E}[l]=1.5+0.39+0.12\times3=2.25<2.37,\qquad\text{Kraft 和}=\frac34+\frac28=1.$$

[▶ 22:27](https://youtu.be/kbAif7XhlTI?t=1347) Kraft 和**剛好等於 1**。[▶ 23:03](https://youtu.be/kbAif7XhlTI?t=1383) 下一集會看到：**最佳碼的 Kraft 和一定等於 1**；1 和 Kraft 和之間的缺口，反映離最佳還有多遠。

### 3.2 第 2 題：是前綴碼嗎？

[▶ 23:03](https://youtu.be/kbAif7XhlTI?t=1383)（碼字依 `L3_ann.pdf` p.14）

| 題 | 碼字 | 前綴碼？ | Kraft 和 |
|---|---|---|---|
| 2.1 | `00` `01` `10` `11` `110` | 否：D=`11` 是 E=`110` 的前綴 [▶ 23:39](https://youtu.be/kbAif7XhlTI?t=1419) | $4\times\frac14+\frac18=\frac98>1$ |
| 2.2 | `001` `011` `100` `111` `110` | 是 [▶ 24:43](https://youtu.be/kbAif7XhlTI?t=1483) | $5\times\frac18=\frac58\le1$ |
| 2.3 | `00` `00` `10` `111` `110` | 否：兩個碼字一樣 [▶ 25:18](https://youtu.be/kbAif7XhlTI?t=1518) | $3\times\frac14+2\times\frac18=1$ |

重點：

- **2.1**：Kraft 和 $>1$，**光看長度就知道它不可能是前綴碼**，連碼字都不用看 [▶ 24:10](https://youtu.be/kbAif7XhlTI?t=1450)。
- **2.3**：Kraft 和 $=1\le1$，卻不是前綴碼。矛盾嗎？【課堂討論】[▶ 25:53](https://youtu.be/kbAif7XhlTI?t=1553) 學生說「可以換一下」。講者：Kraft 只保證「**存在**一個這種長度的前綴碼」，不保證**你手上這個**就是。把第二個 `00` 改成 `01` 就是前綴碼了 [▶ 26:24](https://youtu.be/kbAif7XhlTI?t=1584)。

---

## 4. 熵

### 4.1 接下來要做什麼

[▶ 26:56](https://youtu.be/kbAif7XhlTI?t=1616) 定義資訊理論的量（只講壓縮需要的），然後精確刻畫「最好的前綴碼」，並證明經驗法則 $l(x)\approx\log\frac1{P(x)}$。

【口頭】[▶ 27:27](https://youtu.be/kbAif7XhlTI?t=1647) $\log\frac1{P(x)}$ 在機器學習裡也一直出現（log loss）。DeepMind 最近有一篇論文標題就是在說語言模型和壓縮的關係（字幕作「language modeling compression」），後面的作業會碰到。壓縮和建模、學習有很深的關係。

### 4.2 定義

[▶ 28:01](https://youtu.be/kbAif7XhlTI?t=1681) 很多人在物理學過熵；講者說他沒學物理，但概念很像。

[▶ 28:34](https://youtu.be/kbAif7XhlTI?t=1714) 從現在起字母集用 $\mathcal{X}=\{1,\dots,k\}$，不用 A、B、C、D（比較好追蹤）。記 $p_i=P(X=i)$。

> **熵**（entropy）：
> $$H(X)=\sum_{i=1}^{k}p_i\log_2\frac1{p_i}\qquad\text{單位：位元（bits）}$$

注意事項 [▶ 28:34](https://youtu.be/kbAif7XhlTI?t=1714)：

1. **熵只看分布**，不是 $X$ 本身的函數 [▶ 29:13](https://youtu.be/kbAif7XhlTI?t=1753)。兩個分布一樣的隨機變數熵一樣，所以 $H(X)$ 其實是 $H(p)$。
2. 可以寫成期望值 [▶ 29:52](https://youtu.be/kbAif7XhlTI?t=1792)：$H(X)=\mathbb{E}\left[\log_2\frac1{P(X)}\right]$。
3. **$p=0$ 時定義 $p\log\frac1p=0$** [▶ 29:52](https://youtu.be/kbAif7XhlTI?t=1792)。可以直接規定，也可以用微積分取極限；寫程式時不處理會得到 NaN [▶ 30:28](https://youtu.be/kbAif7XhlTI?t=1828)。

> 以下**不是逐字稿內容**，是補上取極限的計算：$\lim_{p\to0^+}p\log\frac1p=\lim_{p\to0^+}\frac{-\log p}{1/p}$，用 L'Hôpital：$=\lim\frac{-1/(p\ln2)}{-1/p^2}=\lim\frac{p}{\ln2}=0$。

### 4.3 例子

**均勻分布** [▶ 30:28](https://youtu.be/kbAif7XhlTI?t=1828)：$X\sim\mathrm{Unif}\{1,\dots,k\}$，$p_i=\frac1k$：

$$H(X)=\sum_{i=1}^{k}\frac1k\log_2k=\log_2k\ \text{位元}.$$

[▶ 31:40](https://youtu.be/kbAif7XhlTI?t=1900) $\log k$ 在前兩集出現過：固定長度碼的長度是 $\lceil\log k\rceil$。熵和碼長已經看得出關係。

特例：$X\sim\mathrm{Ber}\left(\frac12\right)$（0、1 各半）[▶ 31:40](https://youtu.be/kbAif7XhlTI?t=1900)，$H(X)=\log_22=1$ 位元 [▶ 32:28](https://youtu.be/kbAif7XhlTI?t=1948)。

**$\left(\frac12,\frac14,\frac18,\frac18\right)$** [▶ 32:28](https://youtu.be/kbAif7XhlTI?t=1948)：

$$
\begin{aligned}
H(X)&=\frac12\log_22+\frac14\log_24+2\times\frac18\log_28\\
&=\frac12+\frac12+\frac34=\frac74\ \text{位元}.
\end{aligned}
$$

> ⚠️ 逐字稿缺字 [▶ 33:06](https://youtu.be/kbAif7XhlTI?t=1986)：字幕「1/4 log2 plus 1/8 times 5 plus 1/8 times 3」對不上；投影片 `L3_ann.pdf` p.16 寫的是 $\frac12\log_2\frac1{1/2}+\frac14\log_2\frac1{1/4}+\frac18\log_2\frac1{1/8}\times2=\frac74$，筆記照投影片。

[▶ 33:37](https://youtu.be/kbAif7XhlTI?t=2017) 回家練習：這個分布配上碼 `0`、`10`、`110`、`111`，期望碼長也是 $\frac12\cdot1+\frac14\cdot2+\frac18\cdot3\cdot2=\frac74$，**剛好等於熵** [▶ 34:13](https://youtu.be/kbAif7XhlTI?t=2053)。

### 4.4 性質：$0\le H(X)\le\log k$

[▶ 34:13](https://youtu.be/kbAif7XhlTI?t=2053) 若 $|\mathcal{X}|=k$：

$$0\le H(X)\le\log_2k$$

- $=0$：$X$ 是**確定的**（deterministic），以機率 1 取某個值 [▶ 34:47](https://youtu.be/kbAif7XhlTI?t=2087)。$1\times\log\frac11=0$。
- $=\log k$：$X$ 均勻分布。

[▶ 34:47](https://youtu.be/kbAif7XhlTI?t=2087) $\ge0$ 的證明很簡單：機率 $\le1$。$\le\log k$ 要用凸性和 Jensen 不等式 [▶ 35:20](https://youtu.be/kbAif7XhlTI?t=2120)。

【課本補充】完整證明（§2.6 Theorem 2.6.4 的方法；課堂沒寫）：

- $H\ge0$：每項 $p_i\log\frac1{p_i}$ 中 $0<p_i\le1$，所以 $\log\frac1{p_i}\ge0$；$p_i=0$ 的項定義為 0。等號要每項都是 0，也就是每個 $p_i$ 是 0 或 1，即確定的。
- $H\le\log k$：設 $u$ 是均勻分布 $u_i=\frac1k$。用下面 §6 的 $D(p\|u)\ge0$：
$$0\le D(p\|u)=\sum_ip_i\log\frac{p_i}{1/k}=\log k-H(X).$$
等號當且僅當 $p=u$。

### 4.5 熵代表什麼

[▶ 35:20](https://youtu.be/kbAif7XhlTI?t=2120)

- **不確定性、隨機程度**：確定的變數熵是 0；均勻分布熵最大。物理上的意思也很像 [▶ 35:54](https://youtu.be/kbAif7XhlTI?t=2154)。
- **訊息含有的資訊量**：朋友每次都傳「hello」，你收到也沒得到什麼資訊；有時傳 hello、有時傳 hi，就有一點資訊 [▶ 36:25](https://youtu.be/kbAif7XhlTI?t=2185)。
- **能壓多小**：壓縮就是儲存資訊，所以熵也是壓縮的極限 [▶ 36:58](https://youtu.be/kbAif7XhlTI?t=2218)。這就是單位叫「位元」的原因。
- **很多謎題的答案** [▶ 36:58](https://youtu.be/kbAif7XhlTI?t=2218)：一堆硬幣裡找出較輕或較重的那枚最少要秤幾次；錦標賽找出最強選手要幾輪 [▶ 37:34](https://youtu.be/kbAif7XhlTI?t=2254)。
- **從分布取樣**：用公平硬幣模擬不公平硬幣，或反過來，極限也是熵。作業會碰到。

【課本補充】§5.11（書頁 134）：用公平硬幣產生分布 $p$ 的隨機樣本，平均需要的擲幣次數介於 $H$ 和 $H+2$ 之間。

---

## 5. 獨立隨機變數的聯合熵

[▶ 38:14](https://youtu.be/kbAif7XhlTI?t=2294) 兩個隨機變數 $X_1,X_2$ 獨立。[▶ 38:49](https://youtu.be/kbAif7XhlTI?t=2329) 思考方式：把整個二元組 $Y=(X_1,X_2)$ 看成**一個**隨機變數，它的熵就是 $H(Y)$。

$$
\begin{aligned}
H(X_1,X_2)&=\mathbb{E}\left[\log\frac1{P(X_1,X_2)}\right]\\
&=\mathbb{E}\left[\log\frac1{P(X_1)P(X_2)}\right]&&\text{（獨立）}\\
&=\mathbb{E}\left[\log\frac1{P(X_1)}\right]+\mathbb{E}\left[\log\frac1{P(X_2)}\right]&&\text{（對數性質、期望值線性）}\\
&=H(X_1)+H(X_2).
\end{aligned}
$$

【課堂討論】[▶ 38:49](https://youtu.be/kbAif7XhlTI?t=2329) 第二步怎麼來的？學生答：獨立，所以聯合機率等於乘積 [▶ 39:28](https://youtu.be/kbAif7XhlTI?t=2368)。

[▶ 39:28](https://youtu.be/kbAif7XhlTI?t=2368) 意思：獨立的兩個變數，總資訊量就是各自資訊量的和。不獨立的話第 8 集再講。

**iid** [▶ 40:03](https://youtu.be/kbAif7XhlTI?t=2403)：**獨立同分布**（independent and identically distributed）。$X^n=(X_1,\dots,X_n)$ 全體**互相**獨立（不只兩兩獨立），而且都和 $X$ 同分布 [▶ 40:36](https://youtu.be/kbAif7XhlTI?t=2436)。例如擲 $n$ 次同一枚硬幣 [▶ 41:08](https://youtu.be/kbAif7XhlTI?t=2468)。歸納可得

$$H(X^n)=\sum_{i=1}^nH(X_i)=nH(X).$$

---

## 6. KL 散度（相對熵）

### 6.1 定義

[▶ 41:47](https://youtu.be/kbAif7XhlTI?t=2507) $p=(p_1,\dots,p_k)$、$q=(q_1,\dots,q_k)$ 是同一個字母集上的兩個分布：

> **KL 散度**（Kullback–Leibler divergence），又叫**相對熵**（relative entropy）：
> $$D_{KL}(p\|q)=\sum_{i=1}^{k}p_i\log_2\frac{p_i}{q_i}$$

### 6.2 唯一要用的性質

[▶ 42:24](https://youtu.be/kbAif7XhlTI?t=2544)

> $$D_{KL}(p\|q)\ge0,\quad\text{等號當且僅當 }p=q.$$

[▶ 42:57](https://youtu.be/kbAif7XhlTI?t=2577) 所以它像兩個分布之間的「距離」：越像越小。證明在講義，用凸性和 Jensen 不等式。

【課本補充】證明（§2.6 Theorem 2.6.3，資訊不等式）：令 $A=\{i:p_i>0\}$。$\log$ 是凹函數，由 Jensen 不等式 $\mathbb{E}[\log Y]\le\log\mathbb{E}[Y]$：

$$
\begin{aligned}
-D(p\|q)&=\sum_{i\in A}p_i\log\frac{q_i}{p_i}\\
&\le\log\sum_{i\in A}p_i\frac{q_i}{p_i}=\log\sum_{i\in A}q_i\\
&\le\log\sum_{i=1}^{k}q_i=\log1=0.
\end{aligned}
$$

等號：Jensen 的等號要 $q_i/p_i$ 在 $A$ 上是常數，第二個不等式的等號要 $\sum_{i\in A}q_i=1$，合起來就是 $p=q$。

### 6.3 其他知識

[▶ 43:33](https://youtu.be/kbAif7XhlTI?t=2613)

- **不對稱**：一般 $D(p\|q)\ne D(q\|p)$。不像歐氏距離、$\ell_1$、$\ell_2$。小考會看到例子。
- [▶ 44:07](https://youtu.be/kbAif7XhlTI?t=2647) **機器學習**：生成模型（LLM、擴散模型）想產生和真實分布相近的樣本，需要一個衡量兩個分布差多少的損失函數。KL 散度可微分等原因，常常是首選 [▶ 44:39](https://youtu.be/kbAif7XhlTI?t=2679)。
- [▶ 45:10](https://youtu.be/kbAif7XhlTI?t=2710) 它在壓縮裡也有意思，講義有寫。

> 以下**不是逐字稿內容**，是依課本 §5.4 Theorem 5.4.3 補的：KL 散度在壓縮裡的意思是「用錯分布的代價」。真實分布是 $p$，卻照 $q$ 設計碼長 $l(x)=\lceil\log\frac1{q(x)}\rceil$，期望碼長滿足 $H(p)+D(p\|q)\le\mathbb{E}_p[l(X)]<H(p)+D(p\|q)+1$。

---

## 7. 無損壓縮的主定理

[▶ 45:10](https://youtu.be/kbAif7XhlTI?t=2710) 資訊理論的結果常常非常精確：

> **主定理**（`L3_ann.pdf` p.26）
> 1. **下界**（lower bound，又叫 converse）[▶ 45:45](https://youtu.be/kbAif7XhlTI?t=2745)：**任何前綴碼**都有 $\mathbb{E}[l(X)]\ge H(X)$。任何分布、任何前綴碼都贏不了熵。
> 2. **可達性**（achievability）[▶ 46:18](https://youtu.be/kbAif7XhlTI?t=2778)：可以用前綴碼讓 $\mathbb{E}[l(X)]$ **任意接近** $H(X)$。

[▶ 47:13](https://youtu.be/kbAif7XhlTI?t=2833) 意思：**熵是無損壓縮的根本極限。**

- Shannon 1948 年的論文就證明了這件事。之後 50 年、甚至到 2014 年左右，大家還在找更有效率達到熵的方法。
- 所有無損和有損壓縮器的核心都有一個**熵編碼器**（entropy coder）[▶ 47:52](https://youtu.be/kbAif7XhlTI?t=2872)：想辦法讓輸出接近輸入的熵。Huffman、算術編碼、ANS 都是。
- 【口頭】Shannon 證明這個結果後大約 30 年，才有人找到**線性時間**達到熵的方法；最近的方法也是線性時間，但更適合現代硬體 [▶ 48:25](https://youtu.be/kbAif7XhlTI?t=2905)。

[▶ 48:25](https://youtu.be/kbAif7XhlTI?t=2905) 補充：

- 同樣的下界對**唯一可解碼碼**也成立（作業）。所以不管用不用前綴碼，熵都是無損壓縮的極限。
- [▶ 49:02](https://youtu.be/kbAif7XhlTI?t=2942) 這裡假設 **iid**。別以為只能用在特殊情況，它到處都有用；更一般的分布第 8–10 講再講。

---

## 8. 證明下界：$\mathbb{E}[l(X)]\ge H(X)$

[▶ 49:38](https://youtu.be/kbAif7XhlTI?t=2978) 講者說證明本身不重要，懂這個結果的份量才是重點；但證明會給一個有用的東西（等號條件）。

### 8.1 設定

[▶ 50:17](https://youtu.be/kbAif7XhlTI?t=3017) $X\sim p$，前綴碼的碼長 $l_1,\dots,l_k$。要證

$$\sum_{i=1}^{k}p_il_i\ge H(p).$$

### 8.2 造一個新分布 $q$

[▶ 50:55](https://youtu.be/kbAif7XhlTI?t=3055) 令

$$q_i=c\,2^{-l_i},\qquad c=\frac1{\sum_{j=1}^{k}2^{-l_j}}\ge1.$$

【課堂討論】為什麼 $c\ge1$？學生答：**Kraft 不等式** [▶ 51:35](https://youtu.be/kbAif7XhlTI?t=3095)。講者：對，這就是用到「前綴碼」的地方。一定要用到某處，因為對非無損的碼這個結論不成立（例如所有長度都是 0 或 1 的碼）[▶ 51:35](https://youtu.be/kbAif7XhlTI?t=3095)。

[▶ 52:10](https://youtu.be/kbAif7XhlTI?t=3130) $c$ 是**正規化常數**：$\sum_iq_i=c\sum_i2^{-l_i}=1$，所以 $q$ 是一個分布。

### 8.3 用 $D(p\|q)\ge0$

[▶ 52:47](https://youtu.be/kbAif7XhlTI?t=3167) 有兩個分布，就用 KL 散度 [▶ 53:18](https://youtu.be/kbAif7XhlTI?t=3198)：

$$
\begin{aligned}
0&\le D(p\|q)=\sum_ip_i\log\frac{p_i}{q_i}\\
&=\sum_ip_i\log p_i+\sum_ip_i\log\frac1{q_i}&&\text{（拆開 log）}\\
&=-H(X)+\sum_ip_i\log\frac1{q_i}.
\end{aligned}
$$

所以 $\sum_ip_i\log\frac1{q_i}\ge H(X)$ [▶ 54:24](https://youtu.be/kbAif7XhlTI?t=3264)。代入 $q_i=c\,2^{-l_i}$，$\log\frac1{q_i}=l_i-\log c$ [▶ 54:56](https://youtu.be/kbAif7XhlTI?t=3296)：

$$\sum_ip_il_i-\log c\ge H(X).$$

因為 $c\ge1$，$\log c\ge0$：

$$\mathbb{E}[l(X)]=\sum_ip_il_i\ \ge\ \sum_ip_il_i-\log c\ \ge\ H(X).\qquad\blacksquare$$

[▶ 55:31](https://youtu.be/kbAif7XhlTI?t=3331) 用到的三樣東西：代數整理、Kraft 不等式、KL 散度非負。

【課本補充】§5.3 Theorem 5.3.1 是同一個證明（課本記 $r_i=D^{-l_i}/\sum_jD^{-l_j}$）：$L-H=D(p\|r)+\log\frac1c\ge0$。

### 8.4 等號什麼時候成立

[▶ 55:31](https://youtu.be/kbAif7XhlTI?t=3331) 兩個不等式都要變等號 [▶ 56:06](https://youtu.be/kbAif7XhlTI?t=3366)：

1. $c=1$：$\sum_i2^{-l_i}=1$，**Kraft 不等式取等號**。剛剛小考的次佳碼 Kraft 和 $<1$、更好的碼 $=1$。
2. $p_i=q_i$（$D=0$）[▶ 56:39](https://youtu.be/kbAif7XhlTI?t=3399)：$p_i=2^{-l_i}$，也就是 $l_i=\log_2\frac1{p_i}$，**經驗法則**！

> 所以：期望碼長**等於**熵 ⟺ 滿足 Kraft 等號，且 $l_i=\log\frac1{p_i}$。[▶ 57:15](https://youtu.be/kbAif7XhlTI?t=3435)

### 8.5 兩個等號條件一樣嗎？【Q&A】

[▶ 57:47](https://youtu.be/kbAif7XhlTI?t=3467) 學生問：這兩個條件好像是同一件事？如果機率不是剛好 $\log_2$ 的形式，Kraft 等號就不會成立吧？能不能滿足 Kraft 等號但長度不是 $\log\frac1p$？

講者 [▶ 58:22](https://youtu.be/kbAif7XhlTI?t=3502)：

- Kraft 不等式**只和長度有關**，沒有機率。Kraft 和 $<1$ 的碼對任何分布都不是最佳碼，它就是爛碼。
- [▶ 59:38](https://youtu.be/kbAif7XhlTI?t=3578) 反例（`L3_ann.pdf` p.31）：碼 A→`0`、B→`10`、C→`110`、D→`111`，Kraft 和 $=1$ [▶ 1:00:18](https://youtu.be/kbAif7XhlTI?t=3618)。但分布是 $P(A)=\frac18$、$P(B)=\frac18$、$P(C)=\frac14$、$P(D)=\frac12$：D 機率最大卻拿到最長的碼字，$l_i\ne\log\frac1{p_i}$ [▶ 1:01:00](https://youtu.be/kbAif7XhlTI?t=3660)。所以**兩個條件都需要**。
- 反方向成立 [▶ 1:01:00](https://youtu.be/kbAif7XhlTI?t=3660)：若 $l_i=\log_2\frac1{p_i}$，則 $\sum_i2^{-l_i}=\sum_i2^{-\log_2(1/p_i)}=\sum_ip_i=1$，**自動滿足 Kraft 等號** [▶ 1:01:37](https://youtu.be/kbAif7XhlTI?t=3697)。

學生：所以一個推得出另一個，反過來不行。

---

## 9. 可達性：Shannon 碼離熵不到 1 位元

### 9.1 Shannon 碼的上界

[▶ 1:02:13](https://youtu.be/kbAif7XhlTI?t=3733) Shannon 碼 $l_i=\left\lceil\log_2\frac1{p_i}\right\rceil$ [▶ 1:02:44](https://youtu.be/kbAif7XhlTI?t=3764)。用 $a\le\lceil a\rceil<a+1$ [▶ 1:03:18](https://youtu.be/kbAif7XhlTI?t=3798)：

$$
\begin{aligned}
\mathbb{E}[l(X)]=\sum_ip_i\left\lceil\log_2\frac1{p_i}\right\rceil
&<\sum_ip_i\left(\log_2\frac1{p_i}+1\right)\\
&=H(X)+\sum_ip_i=H(X)+1.
\end{aligned}
$$

合併下界 [▶ 1:03:50](https://youtu.be/kbAif7XhlTI?t=3830)：

$$H(X)\le\mathbb{E}[l(X)]<H(X)+1.$$

Shannon 碼**離熵不到 1 位元** [▶ 1:04:22](https://youtu.be/kbAif7XhlTI?t=3862)。

### 9.2 二進分布

[▶ 1:04:22](https://youtu.be/kbAif7XhlTI?t=3862) **二進分布**（dyadic distribution）：所有機率都是 2 的冪（$\frac12,\frac14,\dots$）。這時 $\log\frac1p$ 都是整數，上整不起作用，$\mathbb{E}[l]=H(X)$，**剛好達到熵** [▶ 1:04:57](https://youtu.be/kbAif7XhlTI?t=3897)。

【口頭】而且**只有**二進分布能剛好達到熵（因為等號要 $l_i=\log\frac1{p_i}$ 是整數）。

### 9.3 還不夠

[▶ 1:05:30](https://youtu.be/kbAif7XhlTI?t=3930) 「差 1 位元以內」看起來很強，其實不然：如果熵是 0.00001，Shannon 碼可能要 1.00001，是熵的幾萬倍 [▶ 1:06:05](https://youtu.be/kbAif7XhlTI?t=3965)。還不算「任意接近」。

### 9.4 例子：$\mathrm{Unif}\{1,2,3\}$【課堂討論】

[▶ 1:06:05](https://youtu.be/kbAif7XhlTI?t=3965)

- 熵 $=\log_23\approx1.58$ 位元 [▶ 1:06:38](https://youtu.be/kbAif7XhlTI?t=3998)（學生算出來）。
- Shannon 碼：$\lceil\log_23\rceil=2$，碼 `00`、`01`、`10`，期望碼長 2 [▶ 1:07:14](https://youtu.be/kbAif7XhlTI?t=4034)。其實就是第 1 集的固定長度碼。
- 上界 $H+1=2.58$。2 比熵多約 25% [▶ 1:07:56](https://youtu.be/kbAif7XhlTI?t=4076)。
- [▶ 1:08:38](https://youtu.be/kbAif7XhlTI?t=4118) 更好的碼：第三個碼字 `10` 的 0 不需要，改成 `1`（仍是前綴碼）[▶ 1:09:12](https://youtu.be/kbAif7XhlTI?t=4152)。期望碼長 $\frac23+\frac23+\frac13=\frac53\approx1.67$ [▶ 1:09:46](https://youtu.be/kbAif7XhlTI?t=4186)（學生算出）。

[▶ 1:09:46](https://youtu.be/kbAif7XhlTI?t=4186) 這個 `00`、`01`、`1` 是 **Huffman 碼**，下一講的主題，是這個分布的**最佳碼**，不可能更好 [▶ 1:10:26](https://youtu.be/kbAif7XhlTI?t=4226)。但 1.67 還是比 1.58 大。

> ⚠️ 逐字稿缺字 [▶ 1:10:26](https://youtu.be/kbAif7XhlTI?t=4226)：字幕「Still, 1.67 versus 1.5」，熵是 1.58，「1.5」是講者說簡略了。

### 9.5 怎麼消掉缺口？【課堂討論】

[▶ 1:10:26](https://youtu.be/kbAif7XhlTI?t=4226) 學生：是不是對每個精度，都有某個夠長的字母集？講者：可是字母集是給定的，怎麼從它造出更大的？[▶ 1:11:00](https://youtu.be/kbAif7XhlTI?t=4260) 學生答：**分組編碼**。作業 1 的小考就做過：9 個符號 → 81 個符號，越大越好 [▶ 1:11:32](https://youtu.be/kbAif7XhlTI?t=4292)。

---

## 10. 分組編碼：任意接近熵

[▶ 1:13:15](https://youtu.be/kbAif7XhlTI?t=4395) 剩 4 分鐘，講分組編碼證明可達性。

把 $n$ 個 iid 符號當一組，在 $\mathcal{X}^n$ 上做 Shannon 碼 [▶ 1:15:27](https://youtu.be/kbAif7XhlTI?t=4527)。Shannon 碼的上下界對**任何**分布都成立，所以對 $X^n$ 的分布也成立 [▶ 1:16:01](https://youtu.be/kbAif7XhlTI?t=4561)：

$$H(X^n)\le\mathbb{E}\left[l(X^n)\right]<H(X^n)+1.$$

iid 所以 $H(X^n)=nH(X)$ [▶ 1:13:48](https://youtu.be/kbAif7XhlTI?t=4428)：

$$nH(X)\le\mathbb{E}\left[l(X^n)\right]<nH(X)+1.$$

除以 $n$，得到**每符號**的位元數 [▶ 1:14:52](https://youtu.be/kbAif7XhlTI?t=4492)：

$$H(X)\le\frac{\mathbb{E}\left[l(X^n)\right]}{n}<H(X)+\frac1n.$$

> **對任意 $\varepsilon>0$，取 $n>1/\varepsilon$，就能離熵 $\varepsilon$ 以內。這就是「任意接近」。** [▶ 1:11:32](https://youtu.be/kbAif7XhlTI?t=4292)、[▶ 1:16:01](https://youtu.be/kbAif7XhlTI?t=4561)

【課本補充】§5.4 Theorem 5.4.2 就是這個結果。

**缺點** [▶ 1:12:06](https://youtu.be/kbAif7XhlTI?t=4326)：組越大，碼表指數成長，複雜度是指數的。所以接下來的路線 [▶ 1:12:38](https://youtu.be/kbAif7XhlTI?t=4358)：

| 方法 | 基礎 | 集數 |
|---|---|---|
| Huffman 碼 | 樹 | 第 4 集 |
| 分組碼 | — | 第 4–5 集 |
| 算術編碼 | 算術 | 第 6 集 |
| ANS | 記數系統 | 第 7 集 |

每一個都在實際的壓縮器裡用到。

[▶ 1:12:06](https://youtu.be/kbAif7XhlTI?t=4326) 小考會有一個 Shannon 碼「爛到離譜」的例子。

> 以下**不是逐字稿內容**，是依本集公式推論的一個例子：$P=(0.99,0.01)$ 的熵 $\approx0.081$ 位元，但任何單符號前綴碼至少 1 位元／符號，是熵的 12 倍以上；Shannon 碼更給 0.01 那個符號 $\lceil\log_2100\rceil=7$ 位元，期望碼長 $0.99\times1+0.01\times7=1.06$。

---

## 11. 一頁速查表

### Kraft 不等式

$$\text{前綴碼存在，碼長 }l_1,\dots,l_k\iff\sum_{i=1}^{k}2^{-l_i}\le1$$

- **正向關鍵一步**：碼字 $i$ 在深度 $l_{\max}$ 有 $2^{l_{\max}-l_i}$ 個後代，互不重疊 ⇒ $\sum2^{l_{\max}-l_i}\le2^{l_{\max}}$。
- **反向**：照 Shannon 碼的貪婪建構。
- 用法：Kraft 和 $>1$ ⇒ 一定不是前綴碼；$\le1$ 只保證「存在」。最佳碼 Kraft 和 $=1$。

### 熵

$$H(X)=\sum_ip_i\log_2\frac1{p_i}=\mathbb{E}\left[\log_2\frac1{P(X)}\right],\qquad0\log\frac10=0$$

| 分布 | 熵 |
|---|---|
| $\mathrm{Unif}\{1..k\}$ | $\log_2k$ |
| $\mathrm{Ber}(1/2)$ | 1 |
| $(1/2,1/4,1/8,1/8)$ | 7/4 |
| $\mathrm{Unif}\{1,2,3\}$ | $\log_23\approx1.58$ |

- $0\le H(X)\le\log_2|\mathcal{X}|$。**關鍵一步**：$D(p\|u)=\log k-H\ge0$。
- 獨立：$H(X_1,X_2)=H(X_1)+H(X_2)$；iid：$H(X^n)=nH(X)$。**關鍵一步**：$\log\frac1{P(x_1)P(x_2)}$ 拆成兩項。

### KL 散度

$$D(p\|q)=\sum_ip_i\log\frac{p_i}{q_i}\ge0,\quad=0\iff p=q;\quad\text{不對稱}$$

**關鍵一步**：Jensen，$-D=\sum p\log\frac qp\le\log\sum q\le0$。

### 主定理

$$H(X)\le\mathbb{E}[l(X)]\quad\text{（任何前綴碼／唯一可解碼碼）}$$

- **關鍵一步**：$q_i=c2^{-l_i}$，$c\ge1$（Kraft）；$0\le D(p\|q)=\mathbb{E}[l]-\log c-H$。
- 等號 ⟺ Kraft 等號 且 $l_i=\log\frac1{p_i}$（後者推得出前者，反之不行）。

| 碼 | 期望碼長 |
|---|---|
| Shannon 碼 $\lceil\log\frac1p\rceil$ | $[H,\ H+1)$；二進分布時 $=H$ |
| $n$ 個一組的 Shannon 碼 | 每符號 $[H,\ H+\frac1n)$ |

**關鍵一步**：$\lceil a\rceil<a+1$，$\sum p_i\cdot1=1$。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 最佳前綴碼、Kraft 等號 | 第 4 集 Huffman |
| 分組編碼的指數複雜度 | 第 4–5 集（分組、AEP、典型集合） |
| 更有效率的熵編碼器 | 第 6 集算術編碼、第 7 集 ANS |
| 非 iid 的熵 | 第 8 集條件熵 |
| $\log\frac1{P(x)}$、壓縮 = 預測、語言模型 | 第 9 集 Context-based AC & LLM 壓縮 |
| KL 散度 = 用錯分布的代價 | 第 9–10 集（模型不準時的壓縮、通用壓縮） |
| SCL | 各集作業 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **前綴碼的碼長一定滿足 Kraft 不等式 $\sum2^{-l_i}\le1$，反過來滿足它就存在前綴碼。熵 $H(X)=\sum p\log\frac1p$ 是無損壓縮的根本極限：用 Kraft 和 KL 散度非負，可證任何前綴碼 $\mathbb{E}[l]\ge H$，等號要 $l_i=\log\frac1{p_i}$；Shannon 碼做到 $H+1$ 以內，$n$ 個一組做到 $H+\frac1n$ 以內，但代價是指數大的碼表。**

---

*筆記依據 Shubham Chandak「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 3 錄影逐字稿（人工字幕，1:17:02）、投影片 L3_ann 與 Cover & Thomas《Elements of Information Theory》2nd ed. §2.1、§2.3、§2.6、§5.2–5.5、§5.11 整理。*
