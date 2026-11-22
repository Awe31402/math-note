---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 15
lecture: Lec15 3.3.4 Universal Lossless Variable-Length Codes
date: 待補
video: https://youtu.be/yFuE7Qx9aug
notes: Alajaji & Chen §3.3.4（pp. 93–98，Definition 3.37–Theorem 3.39、Fig. 3.7–3.9）
---

# 第 15 集 · Lec15 §3.3.4：universal code——adaptive Huffman 與 Lempel–Ziv [▶ 影片](https://youtu.be/yFuE7Qx9aug)

← 上一集：[14](14-binary-prefix-codes-huffman-shannon-fano-elias.md) ｜ [總目錄](README.md) ｜ 下一集：[16](16-block-codes-dmc-channel-capacity-1.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 15 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（27:18，whisper large-v3-turbo）＋ 課本 §3.3.4（pp. 93–98）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Huffman」聽成「Hoffen／Hofman」，「Fano」聽成「phenol／Fennel」，「Elias」聽成「alias」，「Gallager」聽成「Gallagher／Gellaguer」，「Lempel–Ziv」聽成「Lample Zip／Lampold-Ziv／Lample GIF」，「Welch」正確，「sibling」聽成「Siblin／Sybring」，「parsing」正確，「大數法則」聽成「大術法」，「Markov」聽成「Marco」，「stationary ergodic」聽成「station organic／stational ergotic」，「asymptotic equipartition」聽成「a syntactic equal partition」，「von Neumann」聽成「Newman」。結尾「字幕志愿者」是幻覺。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 什麼是 universal code](#1-什麼是-universal-code)
- [2. Adaptive Huffman：一邊壓縮、一邊估計機率](#2-adaptive-huffman一邊壓縮一邊估計機率)
- [3. Gallager 的貢獻：sibling property](#3-gallager-的貢獻sibling-property)
- [4. 例子：什麼時候要重新造碼](#4-例子什麼時候要重新造碼)
- [5. Lempel–Ziv 的背景與想法](#5-lempelziv-的背景與想法)
- [6. Stationary source 可以用 Markov 逼近](#6-stationary-source-可以用-markov-逼近)
- [7. Lempel–Ziv：parsing 與編碼](#7-lempelzivparsing-與編碼)
- [8. 檔案太小反而變大、解碼](#8-檔案太小反而變大解碼)
- [9. 第 3 章總結](#9-第-3-章總結)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

前面所有設計（Huffman、Shannon–Fano–Elias、Fano）都要**事先知道機率**。這一集介紹不知道機率也能壓到 entropy（rate）的 **universal code**：adaptive Huffman code 和 Lempel–Ziv code。最後總結第 3 章。

| 主題 | 課本 |
|---|---|
| Universal code 的概念 | §3.3.4 開頭（p. 93） |
| Adaptive Huffman、sibling property | (A)、Definition 3.37、Observation 3.38、Fig. 3.7–3.9（pp. 93–96） |
| Lempel–Ziv | (B)、Theorem 3.39（pp. 96–98） |

---

## 1. 什麼是 universal code

[▶ 00:00](https://youtu.be/yFuE7Qx9aug?t=0)

- 要知道 A、B、C 的機率，就得先把整個檔案（整本書）掃一遍算出來，才能開始造碼、壓縮。
- **Universal code**：不需要知道 source distribution（unknown）就能壓縮，而且還能壓到 entropy 或 entropy rate——答案竟然是可以。現在很多實用的碼都是 universal code。
- 「完全 unknown」也不對：要知道 source 屬於某個 **family**。例如不知道字母機率，但確定是 i.i.d.（前後獨立、每個時間分布一樣）。
- 核心還是一樣：**大數法則要發生**。i.i.d. 自然有大數法則，只是不知道集中在哪裡。
- **所有 universal code 都隱含一件事：一邊壓縮、一邊估計機率。**

【課本補充】課本（p. 93）列的 universal code：adaptive Huffman code、arithmetic code（以 Shannon–Fano–Elias 為基礎）、Lempel–Ziv code，廣泛用在各種多媒體壓縮軟體和標準。

---

## 2. Adaptive Huffman：一邊壓縮、一邊估計機率

[▶ 02:38](https://youtu.be/yFuE7Qx9aug?t=158)

【口頭】這是 MIT 的 **Gallager** 1978 年的工作。老師非常喜歡他的書：很經典、解釋清楚、範例都用最簡單的；他很適合教學，研究也做得很好。

**想法**：讀 *Alice in Wonderland*，從第一個字母開始讀；讀到第三頁，就用目前讀到的 A、B、C 頻率當機率做 Huffman code。讀越多估得越準（i.i.d. 會收斂），壓縮就越接近 entropy。

**估計**（課本 p. 93）：
$$N(a_i|x^n):=x_1,\dots,x_n\text{ 中 }a_i\text{ 出現的次數},\qquad\hat P(a_i)=\frac{N(a_i|x^n)}n.$$

**更新**（課本 p. 94）：若第 $n+1$ 個是 $a_j$，
$$\hat P^{(n+1)}(a_j)=\frac{n\hat P^{(n)}(a_j)+1}{n+1},\qquad\hat P^{(n+1)}(a_i)=\frac n{n+1}\hat P^{(n)}(a_i)\quad(i\ne j).$$

- 收斂速度大約是 $\frac{\log n}n$，比前面證明的 $\frac1n$ 慢一點，但 $n$ 夠大時還好。
- **問題**：每讀一個新字元，傳送端和接收端都要**同步**用新的機率重新造 Huffman code（接收端看到 A、A、B、C，也能算出 $\frac24,\frac14,\frac14$）。每次都重新造碼，複雜度沒辦法接受。
- 【口頭】Gallager 的貢獻不在起始的想法，而是找到方法讓它**不用每次重新造碼**——前一個碼可以延續使用。

---

## 3. Gallager 的貢獻：sibling property

[▶ 06:43](https://youtu.be/yFuE7Qx9aug?t=403)

**Definition 3.37（sibling property）**（p. 94）：二元 prefix code 的樹滿足
1. 除了根以外，**每個節點都有兄弟**（sibling）——樹是 saturated 的；
2. 節點可以按機率**非遞增排序**，而且**每個節點和它的兄弟相鄰**。

**Observation 3.38**（p. 94）：一個二元 prefix code 是 Huffman code **iff** 它滿足 sibling property。

**意義**（【口頭】）：
- Huffman 最好，所以沒有孤單者，每個人都有手足。
- 兄弟的機率一定差不多：排序後兄弟一定是隔壁——等長的兄弟，彼此機率最接近。這和 Fano code 的想法很像（每次切成機率接近一半的兩群），其實是 Huffman 的概念：**好的設計往下分支時，兩邊機率要很像**。
- 記得這些性質比記步驟重要：將來聽演講、看別人的設計，可以很快判斷好不好——碼長有沒有符合必要條件（機率低的長、最低兩個等長）、樹是不是滿的、兄弟機率是不是最接近。這就是**資料壓縮的 golden rule**。

**怎麼用**：更新機率後，樹的位置先不動，只檢查 sibling property 是否還成立（不用完整重新排序）。**只有被違反時才重新造 Huffman code**；兩端都做同樣的檢查，所以保持同步。

【口頭】還是滿複雜的。好像還沒有人嘗試用硬體做 Huffman code，說不定可以做——那是完全不同的思維。

---

## 4. 例子：什麼時候要重新造碼

[▶ 09:16](https://youtu.be/yFuE7Qx9aug?t=556)

（課本 Fig. 3.7–3.9，pp. 95–96）時間 $n=16$ 時的估計和 Huffman code：

| 符號 | codeword | $\hat P^{(16)}$ |
|---|---|---|
| $a_1$ | 00 | 3/8 |
| $a_2$ | 01 | 1/4 |
| $a_3$ | 100 | 1/8 |
| $a_4$ | 101 | 1/8 |
| $a_5$ | 110 | 1/16 |
| $a_6$ | 111 | 1/16 |

內部節點：$b_0=\frac58$、$b_1=\frac38$、$b_{10}=\frac14$、$b_{11}=\frac18$。排序：
$$b_0\left(\tfrac58\right)\ge b_1\left(\tfrac38\right)\ge a_1\left(\tfrac38\right)\ge a_2\left(\tfrac14\right)\ge b_{10}\left(\tfrac14\right)\ge b_{11}\left(\tfrac18\right)\ge a_3\ge a_4\ge a_5\ge a_6,$$
每一對兄弟都相鄰——滿足 sibling property。

**$n=17$ 觀察到 $a_3$**：輸出它目前的 codeword 100，再更新機率：
$$\hat P^{(17)}=\left(\tfrac6{17},\tfrac4{17},\tfrac3{17},\tfrac2{17},\tfrac1{17},\tfrac1{17}\right).$$
（例：$a_3$：$\frac{16\cdot\frac18+1}{17}=\frac3{17}$；$a_1$：$\frac{16\cdot\frac38}{17}=\frac6{17}$。）

更新後節點變成 $b_0=\frac{10}{17}$、$b_1=\frac7{17}$、$a_1=\frac6{17}$、$b_{10}=\frac5{17}$、$a_2=\frac4{17}$……排序後 $a_1$ 和 $a_2$ 中間夾了 $b_{10}$，**兄弟不再相鄰**——sibling property 被違反（Fig. 3.8）。所以要依新的機率重新造碼（Fig. 3.9），$n=18$ 用新的 codebook 編碼。

【口頭】老師口述：更新完機率後發現 $a_1$、$a_2$ 本來應該是兄弟，現在不在一起了，就要重新執行 Huffman 造碼。

---

## 5. Lempel–Ziv 的背景與想法

[▶ 12:23](https://youtu.be/yFuE7Qx9aug?t=743)

【口頭】
- 1977–1978 年兩位非常聰明的以色列人 **Lempel** 和 **Ziv** 重新思考這個問題，跳脫了 Shannon、Fano、Huffman、Elias 的思維。adaptive Huffman 還是要靠「估計的機率慢慢接近真實機率」；Lempel–Ziv 的思路完全不同。
- 從 1977、78 年起整整十年，研討會都會有一個 Lempel–Ziv 的 session，論文特別多。
- 想法很簡單，是 **Markov** 的概念：**根據以前出現過的去 encode**。
- 貢獻：有嚴謹的理論證明——對**所有 stationary ergodic source**（不只 i.i.d.）都能漸近達到 **entropy rate**。原始論文不容易看；完整證明在 Cover 的書（課本 Theorem 3.39 也指向 Cover §13.5）。

---

## 6. Stationary source 可以用 Markov 逼近

[▶ 13:55](https://youtu.be/yFuE7Qx9aug?t=835)

證明背後的數學概念：**所有 stationary distribution 都可以用 Markov 逼近**。

$X_1,X_2,\dots$ stationary（不是 Markov）。由 Bayes 法則（chain rule），
$$P(x_1,x_2,x_3,x_4)=P(x_1)\,P(x_2|x_1)\,P(x_3|x_1,x_2)\,P(x_4|x_1,x_2,x_3).$$
這也是 entropy chain rule 成立的原因。

- **一階近似**：只記前一個字母，把多的條件砍掉：
$$P(x_1,x_2,x_3,x_4)\approx P(x_1)\,P(x_2|x_1)\,P(x_3|x_2)\,P(x_4|x_3).$$
  只要統計「前一個是 A、下一個是 B」的機率表。
- **二階近似**：$P(x_3|x_1,x_2)$ 保留、$P(x_4|x_2,x_3)$……要統計前兩個字母對下一個的表，空間約 $27^3$，也許還做得到；四階要 $27^4$。
- 英文字母大概四階以上的 Markov；$k$ 階 Markov 近似的 $k\to\infty$ 時就趨近原來的 stationary 分布——$k$ 越大越準。Lempel–Ziv 的編解碼就是用這個思維想出來的。

---

## 7. Lempel–Ziv：parsing 與編碼

[▶ 16:58](https://youtu.be/yFuE7Qx9aug?t=1018)

**Step 1：Parsing（切割）**：掃描輸入，把序列切成**以前沒出現過的 string**。
- 文字例子：讀到 A，新的；再讀到 A，出現過了，不記錄，再讀一個 → AB，新的；再讀 B，新的……凡是看過的就繼續讀，所以**後面切的長度越來越長**——無限多階 Markov 的概念。

**例子**（課本 p. 97）：binary 序列 $1011010100010\ldots$。不知道 0、1 的機率，也不知道是否獨立，但知道是 stationary ergodic（有大數法則，機率形式會收斂；沒有 stationary ergodic 就沒有壓縮的行為）。
- 1：新 → string「1」。
- 0：新 → 「0」。
- 1：出現過 → 11：新 → 「11」。
- 0：出現過 → 01：新 → 「01」。
- 0、01：出現過 → 010：新 → 「010」。
- 0：出現過 → 00：新 → 「00」。
- 1：出現過 → 10：新 → 「10」。

結果：$1,\ 0,\ 11,\ 01,\ 010,\ 00,\ 10$。

**Step 2：編碼**：
- 共 $L$ 個 string，用 $\lceil\log_2L\rceil+1$ 個 bit（課本：從 1 開始編號）的 index 指它。本例 $L=7$，用 3 bits：

| string | 1 | 0 | 11 | 01 | 010 | 00 | 10 |
|---|---|---|---|---|---|---|---|
| index | 001 | 010 | 011 | 100 | 101 | 110 | 111 |

- **每個 string 的 codeword = 它的 prefix（去掉最後一個 bit）的 index + 最後一個 bit**。
  - 關鍵觀察：任何新 string 把最後一個 bit 拿掉，**前面一定出現過**（不然早就切開了）。所以只要「指向舊的 + 補一個新 bit」。
  - 例：「01」的 prefix 是「0」（index 010），最後一位是 1 → (010, 1)。「010」的 prefix「01」是 100 → (100, 0)。全新的（prefix 是空的）用 000。
- 編出來：
$$(000,1)(000,0)(001,1)(010,1)(100,0)(010,0)(001,0)=0001000000110101100001000010.$$

【口頭】前面幾個 string 很短，用 index 有點浪費；但 string 的長度增加得非常快（像金字塔一樣展開），後面的 string 很長，卻只用幾個 bit 的 index 代表，非常省空間。他們不只提出做法，還證明它是最好的——非常厲害。

【課本補充】(p. 97) 傳統的 Lempel–Ziv 要掃兩次（第一次決定 $L$，第二次產生 codeword），可以改成只掃一次；index 也不一定要等長。Welch 1984 年做了高效率的版本，叫 **Lempel–Ziv–Welch（LZW）**。

【口頭】網路上都有程式；有 77 和 78 兩個版本，以及非常多變形——現在都可以一邊 parsing、一邊建表、一邊壓縮。

---

## 8. 檔案太小反而變大、解碼

[▶ 22:34](https://youtu.be/yFuE7Qx9aug?t=1354)

**故意的例子**：上面 13 個 bit 的輸入，編完變成 28 個 bit——**壓完比壓之前還大**。
- 【口頭】就像一本 92 頁的書，壓縮完變 800 頁。Lempel–Ziv 檔案太小會越壓越糟；漸近收斂到 entropy rate 需要很長的時間——這是**不知道 source distribution 的代價**：只知道是 stationary ergodic，其他都不知道，也沒去估機率，它是隱含地在做這件事。
- 【口頭】Unix 底下所有壓縮程式、現在所有商用壓縮程式（PKZip、arc……）都是 Lempel–Ziv 為基礎。它們都會在檔案太小時告訴你「不用壓了，送原檔就好」（例如 1 KB）；4 MB、5 MB 的檔案壓完至少減一半。檔案越大壓得越好，但算得越久。

**解碼**：每 4 個 bit 一個單位。000 + 1：全新的開始，string「1」；000 + 0：string「0」；001 + 1：index 001 的 string（1）接 1 → 11……一路建出 string 表，再把逗點拿掉就是原檔。

**Theorem 3.39**（p. 97）：這個演算法對**任何 stationary ergodic source**（統計未知）都漸近達到 entropy rate。

---

## 9. 第 3 章總結

[▶ 25:06](https://youtu.be/yFuE7Qx9aug?t=1506)

【口頭】
- Shannon 從理論出發，得到 entropy（名稱照 von Neumann 的建議），發現它就是操作上的壓縮極限。
- **固定長度（block code）**：理論上的概念，證明靠 **typical set**。
- **變長碼**：重點是 **uniquely decodable** 和 **Kraft inequality**。
- 大數法則的行為：一群人佔了大部分財富，而且對我們來說一樣有錢——壓縮時沒有任何一個人可以忽略：**asymptotic equipartition** 這個字非常重要。Shannon 很聰明地選了 typical set。
- 任何有 typical set 行為的東西都能用同樣的概念。**自然界的東西幾乎都有 typical set**——陽光四處灑，不會刻意不照某人；**凡是碰到人的就很討厭**：人會一窩蜂（有人賣蛋塔就一堆人賣蛋塔），沒有大數法則的行為，就不能這樣做資料壓縮。
- 證明步驟可以不詳背，但概念一定要知道。

---

## 10. 一頁速查表

**Universal code**：不知道分布（但知道屬於某 family，例如 i.i.d. 或 stationary ergodic）；一邊壓縮、一邊（隱含地）估計機率。

**Adaptive Huffman（Gallager 1978）**
- 估計 $\hat P(a_i)=N(a_i|x^n)/n$；更新 $\hat P^{(n+1)}(a_j)=\frac{n\hat P^{(n)}(a_j)+1}{n+1}$，其他乘 $\frac n{n+1}$。
- **Sibling property**：每個節點都有兄弟（滿樹）、按機率排序時兄弟相鄰。Huffman ⟺ sibling property。
- 只有 sibling property 被違反時才重新造碼。例：$n=16$ 的 $(\frac38,\frac14,\frac18,\frac18,\frac1{16},\frac1{16})$ 看到 $a_3$ → $(\frac6{17},\frac4{17},\frac3{17},\frac2{17},\frac1{17},\frac1{17})$，$a_1,a_2$ 被 $b_{10}$ 隔開 → 重造。
- 收斂約 $\frac{\log n}n$。

**Lempel–Ziv（1977、1978）**
- 背後：stationary 分布可用 $k$ 階 Markov 逼近（$k\to\infty$）。
- Parsing：切成沒出現過的 string（越來越長）。例 $1011010100010\to1,0,11,01,010,00,10$。
- Codeword = prefix 的 index + 最後一個 bit（prefix 一定出現過）。
- 對任何 stationary ergodic source 漸近達到 entropy rate（Thm 3.39）；檔案小時可能變大（13 bit → 28 bit）。
- LZW（Welch 1984）；商用壓縮軟體的基礎。

**第 3 章**：block code ↔ typical set（AEP）；變長碼 ↔ Kraft；兩者極限都是 entropy（rate）；最好的壓縮器輸出 ≈ i.i.d. uniform。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 資料傳輸（有雜訊）、block code、capacity | 第 16–18 集（第 4 章） |
| Typical set 的手法 → jointly typical set | 第 16–17 集 |
| 壓縮和傳輸接在一起（separation） | 第 21 集（§4.6） |
| 沒有大數法則的 source（一般化） | 第 33–34 集（第二部分） |

---

## 附：本集一句話總結

> **不知道機率也能壓到 entropy rate：adaptive Huffman 一邊數頻率、一邊用 sibling property 判斷何時重造碼；Lempel–Ziv 更徹底，把序列切成「沒看過的新字串」並用「舊字串的 index + 一個新 bit」編碼——背後是 stationary source 可被越來越高階的 Markov 逼近。**

---

*筆記依據陳伯寧老師「消息理論」Lec15 錄影逐字稿（whisper large-v3-turbo，27:18）與 Alajaji & Chen 課本 §3.3.4 整理。*
