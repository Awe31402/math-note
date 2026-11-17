---
course: Number Theory（2021 秋，線上錄影）
episode: 23
lecture: Lecture 22
date: 待補（2021 秋）
video: https://youtu.be/pH5yhI17fCw
notes: Jones & Jones §10.4–10.5（書頁 202–206，PDF 頁 217–221）：Lemma 10.5、Theorem 10.6（四平方定理）、§10.5 四元數；講者另引 Stillwell《Elements of Number Theory》第 8 章（Hurwitz 整數）
---

# 第 23 集 · Lecture 22：四元數（Quaternions） [▶ 影片](https://youtu.be/pH5yhI17fCw)

← 上一集：[22-primes-and-gaussian-integers](22-primes-and-gaussian-integers.md) ｜ [總目錄](README.md) ｜ 下一集：[24-fermats-last-theorem](24-fermats-last-theorem.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 23 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（39:04，自動字幕）＋ Jones & Jones §10.4–10.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 定義與乘法](#1-定義與乘法)
- [2. 和內積、外積的關係](#2-和內積外積的關係)
- [3. 例子](#3-例子)
- [4. 矩陣表示與長度](#4-矩陣表示與長度)
- [5. 長度的乘法性](#5-長度的乘法性)
- [6. S_4 對乘法封閉](#6-s_4-對乘法封閉)
- [7. Hurwitz 整數與四平方定理](#7-hurwitz-整數與四平方定理)
- [8. 歷史與賦範除法代數](#8-歷史與賦範除法代數)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

第 21 集用高斯整數的範數證明「兩平方和的積還是兩平方和」；本集用四元數的長度證明「四平方和的積還是四平方和」，並談四平方定理和相關歷史。

| 段落 | 內容 | 課本 |
|---|---|---|
| 1–3 | $\mathbb{H}$ 的定義、乘法 = $-$內積 + 外積 | §10.5 |
| 4–5 | $\lvert\alpha\beta\rvert = \lvert\alpha\rvert\lvert\beta\rvert$（矩陣證法、$\overline{\alpha\beta} = \bar\beta\bar\alpha$ 證法） | Exercise 10.15–10.16 |
| 6 | $S_4$ 封閉；把 70 寫成四平方和 | Lemma 10.5 |
| 7–8 | Hurwitz 整數、四平方定理；Frobenius、Hurwitz | Theorem 10.6、p. 206 |

【口頭】期末考如果考四元數，大概就是像例 3、例 4 那樣的題目 [▶ 38:07](https://youtu.be/pH5yhI17fCw?t=2287)。

---

## 1. 定義與乘法

[▶ 00:00](https://youtu.be/pH5yhI17fCw?t=0)

**定義**：**四元數**（quaternion）是形如
$$\alpha = \alpha_0 + i\alpha_1 + j\alpha_2 + k\alpha_3,\qquad \alpha_0,\dots,\alpha_3\in\mathbb{R}$$
的數，$i,j,k$ 是**虛數單位**，滿足
$$i^2 = j^2 = k^2 = -1,$$
$$ij = -ji = k,\qquad jk = -kj = i,\qquad ki = -ik = j.$$
所有四元數的集合記作 $\mathbb{H}$。和複數很不一樣：**乘法不交換**。

- **實部**：$\mathrm{Re}\,\alpha = \alpha_0$。
- **共軛**：$\bar\alpha = \alpha_0 - i\alpha_1 - j\alpha_2 - k\alpha_3$。

（講者找不到修正筆，「只好忍受塗鴉」。）

**乘法**：照一般方式分配展開，記得 $ij = -ji$ 等規則 [▶ 01:34](https://youtu.be/pH5yhI17fCw?t=94)：
$$\begin{aligned}
\alpha\beta = {}&(\alpha_0\beta_0 - \alpha_1\beta_1 - \alpha_2\beta_2 - \alpha_3\beta_3)\\
&+ i(\alpha_0\beta_1 + \alpha_1\beta_0 + \alpha_2\beta_3 - \alpha_3\beta_2)\\
&+ j(\alpha_0\beta_2 - \alpha_1\beta_3 + \alpha_2\beta_0 + \alpha_3\beta_1)\\
&+ k(\alpha_0\beta_3 + \alpha_1\beta_2 - \alpha_2\beta_1 + \alpha_3\beta_0).
\end{aligned}$$
三個負號來自 $i^2 = j^2 = k^2 = -1$；例如 $i$ 分量的 $\alpha_2\beta_3 - \alpha_3\beta_2$ 來自 $jk = i$、$kj = -i$。

【口頭】這規則和微積分三的**外積**一樣：$\hat i\times\hat j = \hat k$ 等等，這不是巧合 [▶ 02:41](https://youtu.be/pH5yhI17fCw?t=161)。

**長度**（範數）：
$$\lvert\alpha\rvert = \sqrt{\alpha_0^2+\alpha_1^2+\alpha_2^2+\alpha_3^2}.$$

---

## 2. 和內積、外積的關係

[▶ 03:14](https://youtu.be/pH5yhI17fCw?t=194)

把四元數拆成**純量部分**和**向量部分**：$\alpha = \alpha_0+\vec\alpha$，$\vec\alpha = i\alpha_1+j\alpha_2+k\alpha_3$。

**純向量相乘**：
$$\vec\alpha\,\vec\beta = -\vec\alpha\cdot\vec\beta + \vec\alpha\times\vec\beta.$$
**四元數的乘法同時包含內積和外積！**

**一般情形**：
$$(\alpha_0+\vec\alpha)(\beta_0+\vec\beta) = \alpha_0\beta_0 - \vec\alpha\cdot\vec\beta + \alpha_0\vec\beta + \beta_0\vec\alpha + \vec\alpha\times\vec\beta.$$

【口頭】
- 講者大學時發現這件事覺得「哇，好酷」。但想久了會發現向量記號好得多 [▶ 04:20](https://youtu.be/pH5yhI17fCw?t=260)。
- 四元數「像一部邪典電影，有一群忠實信徒在讚美它」——它確實有它的角色，是重要的例子。

---

## 3. 例子

**例 1**：$\alpha = 1+i+j$、$\beta = 3+4k$ [▶ 05:59](https://youtu.be/pH5yhI17fCw?t=359)

三項乘兩項共 6 項：
$$(1+i+j)(3+4k) = 3 + 4k + 3i + 4ik + 3j + 4jk.$$
用 $ik = -j$、$jk = i$：
$$= 3+4k+3i-4j+3j+4i = 3+7i-j+4k.$$

【口頭】不用照講者的展開順序，「我有時排序選得很爛」。加減法不談，就是同類項相加 [▶ 06:34](https://youtu.be/pH5yhI17fCw?t=394)。

**例 2**：$(i+j)(j+k)$ [▶ 07:08](https://youtu.be/pH5yhI17fCw?t=428)
$$(i+j)(j+k) = ij + ik + j^2 + jk = k - j - 1 + i = -1 + i - j + k.$$
用向量看：$(1,1,0)\cdot(0,1,1) = 1$，給 $-1$；$(1,1,0)\times(0,1,1) = (1,-1,1)$，給 $i-j+k$，它和兩個向量都垂直。

【口頭】外積常用的「行列式公式」第一列放向量、後兩列放數字，講者說它在大多數人的形式體系裡「技術上不被允許」，雖然有某種精緻的理論能讓它合法；另外期末考不會出微積分三的題目，別擔心 [▶ 08:16](https://youtu.be/pH5yhI17fCw?t=496)。

（兩個例子的結果筆記用 Python 依乘法公式驗證過。）

**應用與歷史** [▶ 09:23](https://youtu.be/pH5yhI17fCw?t=563)：
【口頭】
- 四元數現在還用在電腦繪圖：用四元數實作旋轉對繪圖引擎比較好。工程師問過講者為什麼，他還沒搞懂；他自己用矩陣想旋轉。
- 四元數比向量早約 60 年：Hamilton 約 1840 年代發現，直到約 1900 年才被 Gibbs、Heaviside 學派的向量記號取代。向量的 $i,j,k$ 就是在紀念 Hamilton——講者覺得這記號不好，他偏好能反映座標系的記號。

---

## 4. 矩陣表示與長度

[▶ 11:06](https://youtu.be/pH5yhI17fCw?t=666)

【口頭】如果有人懷疑四元數「是不是瞎編的」：可以說四元數就是某些 $4\times4$ 矩陣，它們的乘法和四元數一樣；矩陣顯然存在，所以四元數存在。講者把矩陣當成四元數的模型，說推導會離題，有興趣可以問他 [▶ 11:39](https://youtu.be/pH5yhI17fCw?t=699)。

把四元數 $\alpha$ 對應到矩陣 $M_\alpha$，性質：
1. $M_\alpha^T = M_{\bar\alpha}$（轉置 = 共軛的矩陣）；
2. $M_\alpha M_\beta = M_{\alpha\beta}$（講者說這是「相當乏味的作業」，他沒證，大約要一頁計算）；
3. $\det M_\alpha$ 和長度有關（見下）。

具體矩陣字幕沒唸出。以下**不是逐字稿內容**，是一個滿足性質 1、2 的標準選擇（左乘 $\alpha$ 在基底 $1,i,j,k$ 下的矩陣）：
$$M_\alpha = \begin{pmatrix}\alpha_0 & -\alpha_1 & -\alpha_2 & -\alpha_3\\ \alpha_1 & \alpha_0 & -\alpha_3 & \alpha_2\\ \alpha_2 & \alpha_3 & \alpha_0 & -\alpha_1\\ \alpha_3 & -\alpha_2 & \alpha_1 & \alpha_0\end{pmatrix}.$$
它的第一行是 $\alpha$ 的係數，乘上 $\beta$ 的係數向量就得到 $\alpha\beta$ 的係數（對照第 1 節的公式）。

**行列式** [▶ 13:14](https://youtu.be/pH5yhI17fCw?t=794)：沿第一列做 Laplace 展開，正負號 $+,-,+,-$ 配上矩陣裡的負號正好讓東西相消。$4\times4$ 行列式有 $4! = 24$ 項，其中 8 項兩兩相消，剩 16 項整理成
$$\det M_\alpha = (\alpha_0^2+\alpha_1^2+\alpha_2^2+\alpha_3^2)(\alpha_0^2+\alpha_1^2+\alpha_2^2+\alpha_3^2).$$
講者說「這就是四元數的長度平方」，所以這個矩陣表示完美地銜接了矩陣乘法、行列式和四元數的範數。

（以下**不是逐字稿內容**，是筆記的澄清：上式是「平方和 × 平方和」$= (\lvert\alpha\rvert^2)^2 = \lvert\alpha\rvert^4$；講者口頭說的「長度平方」應理解為這個量。下一節的論證不受影響。）

**另一個性質** [▶ 16:29](https://youtu.be/pH5yhI17fCw?t=989)：
$$\alpha\bar\alpha = (\alpha_0+\vec\alpha)(\alpha_0-\vec\alpha) = \alpha_0^2 - \alpha_0\vec\alpha + \alpha_0\vec\alpha - \vec\alpha\,\vec\alpha = \alpha_0^2 + \vec\alpha\cdot\vec\alpha - \vec\alpha\times\vec\alpha = \lvert\alpha\rvert^2,$$
因為向量和自己的外積是 0。

---

## 5. 長度的乘法性

**定理**：$\lvert\alpha\beta\rvert = \lvert\alpha\rvert\,\lvert\beta\rvert$。

【口頭】這是驚人的恆等式，對幾乎所有代數都不成立。能在代數上定義一個和乘法相容的長度，是非常珍貴、罕見的例子 [▶ 17:03](https://youtu.be/pH5yhI17fCw?t=1023)。

**證法一（矩陣）** [▶ 18:09](https://youtu.be/pH5yhI17fCw?t=1089)：長度非負，比較冪次即可。
$$\det M_{\alpha\beta} = \det(M_\alpha M_\beta) = \det M_\alpha\cdot\det M_\beta,$$
（用了沒證的性質 2，以及「積的行列式 = 行列式的積」這個非平凡的恆等式）。代入上一節的行列式公式即得。

【口頭】這本質上就是**四平方恆等式** [▶ 18:41](https://youtu.be/pH5yhI17fCw?t=1121)。

**證法二（不用矩陣）** [▶ 18:41](https://youtu.be/pH5yhI17fCw?t=1121)：

先證**共軛的乘積 = 反序共軛的乘積**：
$$\overline{\alpha\beta} = \bar\beta\,\bar\alpha.$$
- $\alpha\beta = \alpha_0\beta_0 - \vec\alpha\cdot\vec\beta + \alpha_0\vec\beta + \beta_0\vec\alpha + \vec\alpha\times\vec\beta$。取共軛：實數部分（$\alpha_0\beta_0$、$\vec\alpha\cdot\vec\beta$）不變，向量部分變號：
$$\overline{\alpha\beta} = \alpha_0\beta_0 - \vec\alpha\cdot\vec\beta - \alpha_0\vec\beta - \beta_0\vec\alpha - \vec\alpha\times\vec\beta.$$
- $\bar\beta\bar\alpha = (\beta_0-\vec\beta)(\alpha_0-\vec\alpha) = \beta_0\alpha_0 - \vec\beta\cdot\vec\alpha - \beta_0\vec\alpha - \alpha_0\vec\beta + \vec\beta\times\vec\alpha$，而外積反交換 $\vec\beta\times\vec\alpha = -\vec\alpha\times\vec\beta$。兩者相等。

【口頭】順序會反過來，「如果沒注意會被嚇一跳」——因為虛數單位反交換（$ij = -ji$）[▶ 19:14](https://youtu.be/pH5yhI17fCw?t=1154)。

然後：
$$\lvert\alpha\beta\rvert^2 = (\alpha\beta)\overline{(\alpha\beta)} = \alpha\beta\bar\beta\bar\alpha = \alpha\,\lvert\beta\rvert^2\,\bar\alpha = \lvert\beta\rvert^2\,\alpha\bar\alpha = \lvert\alpha\rvert^2\lvert\beta\rvert^2.$$
（$\lvert\beta\rvert^2$ 是實數，可以拿到前面。）∎

> 【課本補充】這就是 Exercise 10.15–10.16（p. 206）：驗證 $\lvert q\rvert^2 = q\bar q$、$\overline{q_1q_2} = \bar q_2\bar q_1$，再推出 $\lvert q_1q_2\rvert^2 = \lvert q_1\rvert^2\lvert q_2\rvert^2$ 和四平方恆等式 (10.3)。

---

## 6. S_4 對乘法封閉

[▶ 21:28](https://youtu.be/pH5yhI17fCw?t=1288)

$S_4$ = 能寫成四個整數平方和的數（第 21 集的記號；「好像是一個遊戲的名字？」）。

**定理**：$a,b\in S_4\Rightarrow ab\in S_4$。

**證明**：$a = \alpha_0^2+\cdots+\alpha_3^2$、$b = \beta_0^2+\cdots+\beta_3^2$（整數）。令 $\alpha = \alpha_0+i\alpha_1+j\alpha_2+k\alpha_3$、$\beta$ 同理，則 $\lvert\alpha\rvert^2 = a$、$\lvert\beta\rvert^2 = b$。
$$ab = \lvert\alpha\rvert^2\lvert\beta\rvert^2 = \lvert\alpha\beta\rvert^2 = (\text{實部})^2+(i\text{ 部})^2+(j\text{ 部})^2+(k\text{ 部})^2,$$
四個部分由第 1 節的乘法公式給出，都是整數。所以 $ab\in S_4$。∎

這也就是 **Euler 四平方恆等式**：
$$\Big(\sum\alpha_i^2\Big)\Big(\sum\beta_i^2\Big) = (\alpha_0\beta_0-\alpha_1\beta_1-\alpha_2\beta_2-\alpha_3\beta_3)^2 + (\alpha_0\beta_1+\alpha_1\beta_0+\alpha_2\beta_3-\alpha_3\beta_2)^2 + \cdots$$

**用它造表示法**（像高斯整數那樣）[▶ 24:54](https://youtu.be/pH5yhI17fCw?t=1494)：

**例 3**：把 70 寫成四平方和。
- $7 = 2^2+1^2+1^2+1^2$，$\alpha = 2+i+j+k$，$7 = \alpha\bar\alpha$。
- $10 = 3^2+1^2+0^2+0^2$，$\beta = 3+i$，$10 = \beta\bar\beta$。
- $70 = \lvert\alpha\beta\rvert^2$，只要算 $\alpha\beta$：
$$\alpha\beta = (2+i+j+k)(3+i) = 5+5i+4j+2k.$$
$$70 = 5^2+5^2+4^2+2^2 = 25+25+16+4.\ ✓$$

（講者一開始算錯，用筆把答案改寫過 [▶ 26:02](https://youtu.be/pH5yhI17fCw?t=1562)。）

**例 4**：換一種配法 [▶ 26:39](https://youtu.be/pH5yhI17fCw?t=1599)
- 改算 $\alpha\bar\beta$；剩下的 $\beta\bar\alpha = \overline{\alpha\bar\beta}$ 正好是它的共軛，所以 $70 = \lvert\alpha\bar\beta\rvert^2$。
$$\alpha\bar\beta = (2+i+j+k)(3-i) = 7+i+2j+4k.$$
$$70 = 7^2+1^2+2^2+4^2 = 49+1+4+16.\ ✓$$

（兩個乘積筆記用 Python 驗證過。）這樣可以找出同一個數的各種四平方表示法，就像用高斯整數找兩平方表示法。

> 【課本補充】Lemma 10.5（p. 202）就是四平方恆等式 (10.3)；把 $b_1,c_1,d_1$ 換號得 (10.4)。

---

## 7. Hurwitz 整數與四平方定理

[▶ 27:44](https://youtu.be/pH5yhI17fCw?t=1664)

- 高斯整數的「天真推廣」是 $\mathbb{Z}[i,j,k] = \{a+bi+cj+dk : a,b,c,d\in\mathbb{Z}\}$，但它**沒有除法演算法**。
- 要用 **Hurwitz 整數**：$a+bi+cj+dk$，其中 $a,b,c,d$ 是「整數乘 $\frac12$」，例如 $\frac12+\frac32i-\frac32j+8k$。（講者自己用一個花體 H 當臨時記號，說不是標準記號。）

（以下**不是逐字稿內容**，是補充說明：標準定義要求 $a,b,c,d$ **全是整數或全是半整數**；講者舉的例子 $\frac12+\frac32i-\frac32j+8k$ 混了半整數和整數 8，嚴格說不是 Hurwitz 整數。）

- Hurwitz 整數包含天真推廣，而且有除法演算法——但要小心**左除和右除**不同，因為乘法不交換，「真的很亂」。所以不能說它是歐幾里得整環（那要求交換環）[▶ 29:23](https://youtu.be/pH5yhI17fCw?t=1763)。
- 有 Hurwitz 質數、可以分解、有質因數性質。這套技術是證明**四平方定理**的一部分：**每個自然數都是四個平方的和**。
- 細節見 Stillwell《Elements of Number Theory》第 8 章——「很多」。

> 【課本補充】Theorem 10.6（p. 203–204，Lagrange 1770）的證明不用 Hurwitz 整數：
> 1. $0,1,2\in S_4$，由封閉性只要證每個奇質數 $p\in S_4$。
> 2. 模 $p$ 的平方（含 0）有 $\frac{p+1}2$ 個，$-1-l^2$ 也有 $\frac{p+1}2$ 個，兩集合必相交，所以有 $u^2+v^2+1 = rp$，$0<r<p$。
> 3. 取最小的 $m$ 使 $mp\in S_4$；若 $m>1$，先證 $m$ 是奇數，再用最小絕對值剩餘和恆等式 (10.4) 造出更小的 $sp\in S_4$（無窮遞降），矛盾。

---

## 8. 歷史與賦範除法代數

[▶ 29:57](https://youtu.be/pH5yhI17fCw?t=1797)

【口頭】
- 平方和的事古人就知道：希臘的 Diophantus，以及另一位講者想不起名字的偉大古印度數學家——「足以說明許多傑出的古代數學家被遺忘了」。
- 19 世紀初，複數和平面幾何的關係已經清楚：每個複數對應一個旋轉加伸縮，例如乘 $i$ 就是轉 90°。自然想在 $\mathbb{R}^3$ 上發明一種乘法來描述三維旋轉 [▶ 31:01](https://youtu.be/pH5yhI17fCw?t=1861)。
- Hamilton 花了大約 13 年想在 $\mathbb{R}^3$ 上找乘法，最後明白行不通，決定在三個空間維度外加上**時間**，事情就展開了：1843 年發現 $\mathbb{R}^4$ 上的四元數乘法。
- Rodrigues 在 1840 年就用這種乘法研究 $\mathbb{R}^3$ 的旋轉；一般歸功 Hamilton，因為他推廣了這個想法、說明它的重要性。所以大概還有其他人有過這想法。
- 「和往常一樣，Euler 早就知道」：大約早一百年，Euler 就知道四平方恆等式（第 6 節那條），雖然據我們所知他不知道四元數。Legendre 知道**沒有三平方恆等式** [▶ 33:10](https://youtu.be/pH5yhI17fCw?t=1990)。
- Hamilton 花 13 年在這問題上，顯然不太熟悉已知的結果。講者說不要因此輕視他：人有了想法就一直追，常常不先看別人做過什麼，同一件事被不同人重新發現很常見；在網路時代比較難找藉口，但還是會發生 [▶ 34:14](https://youtu.be/pH5yhI17fCw?t=2054)。

**四元數幾乎是一個體** [▶ 34:46](https://youtu.be/pH5yhI17fCw?t=2086)：體是每個非零元素都有乘法反元素的**交換**環；四元數是有單位元素、每個非零元素都有反元素的環，只差**乘法不交換**，所以叫**斜體**（skew field）。很多對體成立的構造在四元數上「差一點」成立——它正好在「行不通」的邊緣。

**再往後** [▶ 35:53](https://youtu.be/pH5yhI17fCw?t=2153)：
- **八元數**（octonions）：8 維，由 Cayley 和 Graves 獨立發現；**不結合**（更糟），但講者相信它是 power associative。
- **Frobenius（1878）**：$\mathbb{R}$、$\mathbb{C}$、$\mathbb{H}$ 是 $\mathbb{R}$ 上僅有的有限維**結合除法代數**（「除法」= 每個非零元素有反元素；「在 $\mathbb{R}$ 上」= 實數和所有元素交換）。所以 Hamilton 在 $\mathbb{R}^3$ 失敗不是缺乏想像力。講者說 Frobenius 可能是第一個把線性代數做得很仔細的人：線性代數的想法在古代數學到處都有，但 Frobenius 把很多只做過特例的事做成一般情形 [▶ 37:00](https://youtu.be/pH5yhI17fCw?t=2220)。
- **Hurwitz**：只有 $k = 1,2,4,8$ 時有 $k$ 平方恆等式。換句話說，**賦範除法代數**（normed division algebra，範數是乘法的）只有 1、2、4、8 維四種：$\mathbb{R}$、$\mathbb{C}$、$\mathbb{H}$、八元數（同構意義下）。範數的乘法性正是本集看到的「平方和恆等式」。

⚠️ 逐字稿缺字：[▶ 37:34](https://youtu.be/pH5yhI17fCw?t=2254) 字幕寫「horowitz 1998」；課本 p. 206 寫 Hurwitz **1898**。

> 【課本補充】§10.5（p. 205–206）：Hamilton 想找一個 3 維數系模擬 $\mathbb{R}^3$，並保持「積的長度 = 長度的積」，多年失敗後 1843 年明白需要 4 維。$\mathbb{H}$ 以 Hamilton 命名；他寫了兩本書和很多論文，利用四元數的 4 維性同時研究空間與時間。這些事實（Frobenius 1878、Hurwitz 1898）也解釋了**為什麼三平方和比兩平方、四平方和難研究**。

---

## 9. 一頁速查表

**四元數** $\alpha = \alpha_0+i\alpha_1+j\alpha_2+k\alpha_3$
- $i^2 = j^2 = k^2 = -1$；$ij = k = -ji$、$jk = i = -kj$、$ki = j = -ik$。
- $\bar\alpha = \alpha_0-\vec\alpha$；$\lvert\alpha\rvert^2 = \sum\alpha_i^2 = \alpha\bar\alpha$。
- $(\alpha_0+\vec\alpha)(\beta_0+\vec\beta) = \alpha_0\beta_0-\vec\alpha\cdot\vec\beta+\alpha_0\vec\beta+\beta_0\vec\alpha+\vec\alpha\times\vec\beta$。

**例**：$(1+i+j)(3+4k) = 3+7i-j+4k$；$(i+j)(j+k) = -1+i-j+k$。

**長度乘法性** $\lvert\alpha\beta\rvert = \lvert\alpha\rvert\lvert\beta\rvert$
- 關鍵：$\overline{\alpha\beta} = \bar\beta\bar\alpha$ ⇒ $\lvert\alpha\beta\rvert^2 = \alpha\beta\bar\beta\bar\alpha = \lvert\alpha\rvert^2\lvert\beta\rvert^2$。
- 或矩陣：$\det M_{\alpha\beta} = \det M_\alpha\det M_\beta$，$\det M_\alpha = \lvert\alpha\rvert^4$。

**$S_4$ 封閉** ⇒ Euler 四平方恆等式。
- $70$：$(2+i+j+k)(3+i) = 5+5i+4j+2k$ ⇒ $5^2+5^2+4^2+2^2$；$(2+i+j+k)(3-i) = 7+i+2j+4k$ ⇒ $7^2+1^2+2^2+4^2$。

**四平方定理**（Lagrange 1770）：每個自然數 $\in S_4$。用 Hurwitz 整數（$\mathbb{Z}[i,j,k]$ 沒有除法演算法）。

**分類定理**：結合除法代數 $\mathbb{R},\mathbb{C},\mathbb{H}$（Frobenius 1878）；賦範除法代數維度 1、2、4、8（Hurwitz 1898）⇔ $k$ 平方恆等式只有 $k = 1,2,4,8$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 「換一個數系來研究方程」 | 第 24 集（Fermat 最後定理：Kummer 的分圓整數） |
| 範數乘法性、唯一分解 | 第 24 集（唯一分解在某些數系失敗） |

---

## 附：本集一句話總結

> **四元數 $\mathbb{H}$ 的乘法同時包含內積和外積，雖然不交換，但 $\overline{\alpha\beta}=\bar\beta\bar\alpha$ 使長度仍是乘法的：$\lvert\alpha\beta\rvert=\lvert\alpha\rvert\lvert\beta\rvert$——這正是 Euler 四平方恆等式，所以四平方和的積還是四平方和（例如 $70=5^2+5^2+4^2+2^2=7^2+1^2+2^2+4^2$）；而這種乘法範數只在 1、2、4、8 維存在。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 22 錄影逐字稿（YouTube 自動字幕，39:04）與 Jones & Jones《Elementary Number Theory》§10.4–10.5 整理。*
