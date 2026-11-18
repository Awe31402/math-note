---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 11
lecture: Lecture 11
date: 2023-02-08
video: https://youtu.be/-eopGv3Vfto （part 1）、https://youtu.be/Uq9O8NvL_ok （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.1–2.3 開頭（書頁 39–45，PDF 頁 58–64）
---

# 第 11 集 · Lebesgue 積分登場：階梯函數 [▶ 影片](https://youtu.be/-eopGv3Vfto)

← 上一集：[10-matrix-exponential](10-matrix-exponential.md) ｜ [總目錄](README.md) ｜ 下一集：[12-lebesgue-integrable-functions](12-lebesgue-integrable-functions.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 11 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 5:02，自動字幕）＋ Debnath & Mikusiński §2.1–2.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼要 Lebesgue 積分、這本書的路線](#1-為什麼要-lebesgue-積分這本書的路線)
- [2. 特徵函數與階梯函數](#2-特徵函數與階梯函數)
- [3. 階梯函數的積分](#3-階梯函數的積分)
- [4. 積分的性質、支撐、平移](#4-積分的性質支撐平移)
- [5. 兩個引理：區間長度](#5-兩個引理區間長度)
- [6. 單調階梯函數列的積分](#6-單調階梯函數列的積分)
- [7. Lebesgue 可積函數的定義](#7-lebesgue-可積函數的定義)
- [8. 第 2 章路線圖](#8-第-2-章路線圖)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 為什麼需要 Lebesgue 積分；MacNeille–Mikusiński 路線 | §2.1，pp. 39–40 |
| 階梯函數、基本表示 | §2.2，p. 40 |
| 階梯函數的積分與性質 | Definition 2.2.1、Theorem 2.2.2，p. 41 |
| 區間長度的兩個引理；有理數的反例 | Lemma 2.2.3–2.2.4、Example 2.2.5，pp. 42–43 |
| 單調階梯函數列的積分 | Theorem 2.2.6、Corollary 2.2.7，pp. 43–44 |
| Lebesgue 可積函數 | Definition 2.3.1，p. 45 |

講者開場說他今天在物理上被一題難倒，還沒回過神。⚠️ 逐字稿缺字：字幕把 Lebesgue 聽成「the bay / lebay / labay」。

---

## 1. 為什麼要 Lebesgue 積分、這本書的路線

[▶ 00:35](https://youtu.be/-eopGv3Vfto?t=35) 課本 §2.1。

課本：Hilbert 空間最重要的例子之一是 $\mathbb{R}^N$ 上 **Lebesgue 平方可積函數**的空間，所以 Lebesgue 積分是理解 Hilbert 空間理論的關鍵。Henri Lebesgue（1875–1941）在 1899–1901 年的五篇短文裡提出這個積分。

**兩種路線**[▶ 01:44](https://youtu.be/-eopGv3Vfto?t=104)：

- 常見的路線：先花很多時間建**測度論（measure theory）**——Borel 集等等理論準備——再定義積分。講者說走那條路要繞很久。
- 這本書：照 **H. M. MacNeille 和 J. Mikusiński** 的想法，直接定義積分，不需要測度。先在 $\mathbb{R}$ 上做實值函數，再推廣到複值，最後到 $\mathbb{R}^N$。

講者注意到 Mikusiński 這個名字在第 1 章 Banach–Steinhaus 的證明（對角定理）也出現過。那個證法不用 Baire 綱定理那種抽象工具，比較具體，「也許更合分析學家的口味」。他猜課本作者是不是 Mikusiński 的學生，接著發現作者之一就叫 Mikusiński，猜可能是兒子或親戚，「像 Bernoulli 家族一樣」。[▶ 02:50](https://youtu.be/-eopGv3Vfto?t=170)

> 【課本補充】課本扉頁寫著「獻給我們父親的紀念：Jogesh Chandra Debnath 與 Jan Mikusiński」。所以作者 Piotr Mikusiński 是 Jan Mikusiński 的兒子。

---

## 2. 特徵函數與階梯函數

[▶ 04:29](https://youtu.be/-eopGv3Vfto?t=269) 課本 §2.2。

**特徵函數（characteristic function）**：講者用的記號（課本沒有）

$$\chi_{[a,b)}(t)=\begin{cases}1, & t\in[a,b)\\0, & \text{其他}\end{cases}$$

一般集合 $A$ 也一樣定義 $\chi_A$，它「刻畫」了這個集合。

**例子**【口頭】[▶ 06:10](https://youtu.be/-eopGv3Vfto?t=370)：有理數的特徵函數 $\chi_{\mathbb{Q}}$：有理數處是 1，無理數處是 0。畫圖像兩條水平線。講者說這種函數正是想要 Lebesgue 積分的主要原因之一，它超出 Riemann 積分的範圍。

**階梯函數（step function）**：**半開區間** $[a_k,b_k)$ 的特徵函數的有限線性組合，

$$f=\lambda_1f_1+\lambda_2f_2+\cdots+\lambda_nf_n,\qquad f_k=\chi_{[a_k,b_k)},\ \lambda_k\in\mathbb{R}. \tag{2.1}$$

**例子**[▶ 07:50](https://youtu.be/-eopGv3Vfto?t=470)（講者的例子，一開始畫錯後改正）：

$$f=\chi_{[0,1)}+2\chi_{[1,5)}+3\chi_{[3,7)}.$$

| 區間 | $[0,1)$ | $[1,3)$ | $[3,5)$ | $[5,7)$ | 其他 |
|---|---|---|---|---|---|
| $f$ 的值 | 1 | 2 | $2+3=5$ | 3 | 0 |

圖形是一階一階的，所以叫階梯函數。區間是左閉右開，所以每個跳躍點的值取右邊那一階。畫垂直線連起來只是為了好看，不是數學的一部分。

**基本表示**【課本補充】：(2.1) 的寫法不唯一。如果要求區間**互不相交**而且用最少個數，表示就唯一，叫**基本表示（basic representation）**：設 $a_0<a_1<\cdots<a_n$ 是 $f$ 所有跳躍點，

$$f=\alpha_1\chi_{[a_0,a_1)}+\cdots+\alpha_n\chi_{[a_{n-1},a_n)},\qquad\alpha_k=f(a_{k-1}).$$

上面的例子的基本表示是 $\chi_{[0,1)}+2\chi_{[1,3)}+5\chi_{[3,5)}+3\chi_{[5,7)}$。

---

## 3. 階梯函數的積分

[▶ 11:24](https://youtu.be/-eopGv3Vfto?t=684) 課本 Definition 2.2.1。

【課堂討論】講者問怎麼定義積分，學生答：權重乘區間長度。

$$\int f=\lambda_1(b_1-a_1)+\lambda_2(b_2-a_2)+\cdots+\lambda_n(b_n-a_n).$$

講者說：不用寫 $dx$，「別告訴大一新生」。

**區間重疊沒關係**[▶ 14:01](https://youtu.be/-eopGv3Vfto?t=841)：上例用 (2.1)：

$$\int f=1\cdot1+2\cdot4+3\cdot4=21.$$

用基本表示：$1\cdot1+2\cdot2+5\cdot2+3\cdot2=1+4+10+6=21$。一樣。講者解釋：$[3,5)$ 那一段高 5、寬 2，面積 10，正好是綠色（高 2）的 4 加上黑色（高 3）的 6，重疊的部分剛好疊加成正確的面積。他也說：因為只有有限多個區間，總能改寫成不重疊的階梯，不重疊時面積顯然是各階相加；但課本既然叫它「基本表示」，證明顯然可以直接用重疊的寫法進行。[▶ 17:10](https://youtu.be/-eopGv3Vfto?t=1030)

【課本補充】$\int f$ 等於 $f$ 的 Riemann 積分，所以不依賴表示法；課本要讀者不用 Riemann 積分，自己給一個初等證明（習題）。

---

## 4. 積分的性質、支撐、平移

[▶ 19:26](https://youtu.be/-eopGv3Vfto?t=1166) 課本 Theorem 2.2.2。

對階梯函數 $f,g$：

- (a) $\int(f+g)=\int f+\int g$；
- (b) $\int\lambda f=\lambda\int f$；
- (c) $f\le g$ ⟹ $\int f\le\int g$；
- (d) $\left|\int f\right|\le\int|f|$；
- (e) $\int\tau_zf=\int f$。

講者提醒：$f\le g$ 要理解成**逐點**，對所有 $x$ 都成立。[▶ 20:53](https://youtu.be/-eopGv3Vfto?t=1253)

【課本補充】證明重點：(c) 先證 $f\ge0\Rightarrow\int f\ge0$（基本表示的係數都 $\ge0$），再對 $g-f$ 用；(d) 由 $\pm f\le|f|$ 和 (c)。

**向量空間、絕對值、min/max**[▶ 21:33](https://youtu.be/-eopGv3Vfto?t=1293)：階梯函數構成向量空間；$|f|$ 也是階梯函數；

$$\min\{f,g\}=\tfrac12\left(f+g-|f-g|\right),\qquad\max\{f,g\}=\tfrac12\left(f+g+|f-g|\right).$$

講者說課本 p. 40 這兩個式子一開始讓他覺得怪，後來想通要**逐點**理解：在每個 $x$，$\frac12(a+b\pm|a-b|)$ 就是 $a,b$ 的較大／較小者。所以 min、max 也是階梯函數。

**支撐（support）**[▶ 22:12](https://youtu.be/-eopGv3Vfto?t=1332)（p. 41）：

$$\operatorname{supp}f=\{x\in\mathbb{R}:f(x)\ne0\}.$$

例如非零常數函數的支撐是整個 $\mathbb{R}$。階梯函數 (2.1)（$\lambda_k\ne0$）的支撐包含在 $\bigcup_k[a_k,b_k)$ 裡。講者說應該要求 $\lambda_k\ne0$，不然寫它幹嘛。

> 以下**不是逐字稿內容**，是補一個細節：區間重疊時係數可能相消（例如 $\chi_{[0,2)}-\chi_{[1,2)}=\chi_{[0,1)}$），所以支撐一般只是**包含於**聯集；用基本表示時才相等。

**平移（translation）**[▶ 24:40](https://youtu.be/-eopGv3Vfto?t=1480)：

$$(\tau_zf)(x)=f(x-z).$$

圖形向右平移 $z$。$\chi_{[a,b)}$ 平移後是 $\chi_{[a+z,b+z)}$，所以 $\tau_zf=\lambda_1\tau_zf_1+\cdots+\lambda_n\tau_zf_n$。往右平移面積不變，所以 (e) 成立。

講者的抱怨【口頭】[▶ 25:53](https://youtu.be/-eopGv3Vfto?t=1553)：如果把 $\tau_z$ 看成「$f$ 合成平移函數 $x\mapsto x-z$」，照一般的合成記號應該寫在右邊；課本寫成 $\tau_zf$，順序跟數學其他地方相反。「但我確定這是標準寫法。」

---

## 5. 兩個引理：區間長度

### Lemma 2.2.3

[▶ 30:13](https://youtu.be/-eopGv3Vfto?t=1813)

$f$ 是階梯函數，$\operatorname{supp}f\subseteq[a_1,b_1)\cup\cdots\cup[a_n,b_n)$，而且 $|f|<M$。則

$$\int|f|\le M\sum_{k=1}^n(b_k-a_k).$$

講者：直觀上，區間不重疊時右邊是「最大高度 × 總寬度」；重疊時右邊更大，所以也對。課本說證明容易，留作習題。

### Lemma 2.2.4

[▶ 32:39](https://youtu.be/-eopGv3Vfto?t=1959)

若 $[a_1,b_1),[a_2,b_2),\dots$（可以**無限多個**）是 $[a,b)$ 的一個**分割**（partition），則

$$\sum_{n=1}^\infty(b_n-a_n)=b-a.$$

【課堂討論】講者問「分割」是什麼意思，學生答：互不相交的聯集。也就是 $\bigcup_n[a_n,b_n)=[a,b)$，且 $i\ne j$ 時 $[a_i,b_i)\cap[a_j,b_j)=\varnothing$。

講者：直觀上顯然，但課本用 $\mathbb{R}$ 的**完備性**（最小上界性質）給了半頁的仔細證明。課本說：「這個引理聽起來顯然，證明卻出乎意料地難。」

【課本補充】證明概要：令 $S$ 是所有使「$[a,c)$ 的部分也滿足長度和 $=c-a$」的 $c\in(a,b]$。證 $\sup S\in S$，再證 $\sup S=b$（若 $s=\sup S<b$，$s$ 落在某個 $[a_k,b_k)$ 裡，則 $b_k\in S$ 且 $b_k>s$，矛盾）。

### Example 2.2.5：有理數上不成立

[▶ 36:23](https://youtu.be/-eopGv3Vfto?t=2183)

在 $\mathbb{Q}$ 上，令 $[a,b)_{\mathbb{Q}}=\{x\in\mathbb{Q}:a\le x<b\}$。課本證明：對任意有理數 $\varepsilon>0$，可以用有理區間蓋住 $[0,1)_{\mathbb{Q}}$，而長度總和 $<\varepsilon$。

講者說：不只總長加不到 $1-0$，還能**任意小**，「局勢完全翻轉」。原因是 $\mathbb{R}$ 沒有縫隙（完備），$\mathbb{Q}$ 不完備，才能造出這種「惡魔般的例子」。細節是習題。

【課本補充】構造：$[0,1)_{\mathbb{Q}}$ 可數，排成 $q_1,q_2,\dots$。令 $a_n=q_n$，$b_n=q_n+\varepsilon/2^{n+1}$。每個 $q_n$ 都被蓋到，總長 $\sum\varepsilon/2^{n+1}=\varepsilon/2<\varepsilon$。（再調整成互不相交、包含在 $[0,1)$ 裡是習題。）

---

## 6. 單調階梯函數列的積分

### Theorem 2.2.6

[▶ 40:18](https://youtu.be/-eopGv3Vfto?t=2418)

$(f_n)$ 是**非遞增**的**非負**階梯函數列，且 $\lim_nf_n(x)=0$ 對每個 $x\in\mathbb{R}$。則

$$\lim_{n\to\infty}\int f_n=0.$$

**「非遞增」是什麼意思**【課堂討論】[▶ 42:08](https://youtu.be/-eopGv3Vfto?t=2528)：講者和學生討論。有一派用語把「遞增／遞減」留給**嚴格**的情形；這時「非遞增（nonincreasing）」= 遞減或保持不變，即 $f_{n+1}\le f_n$。講者說用語依書而異，「如果我說錯了先道歉」。

**直觀**[▶ 47:19](https://youtu.be/-eopGv3Vfto?t=2839)：$n$ 夠大之後，階梯函數的圖形都很「薄」，所以面積也很小。講者說：先證這些「低科技、直觀上顯然」的階梯函數定理，再一步步推到更有趣的函數。課本的證明一頁半，「不容易」。

【課本補充】證明概要（反證）：

1. $\int f_n$ 遞減且 $\ge0$，所以收斂，設極限 $\varepsilon>0$。
2. 取區間 $[a,b)$ 包住 $f_1$ 的支撐（所以包住所有 $f_n$ 的支撐）。令 $\alpha=\frac{\varepsilon}{2(b-a)}$，$A_n=\{x\in[a,b):f_n(x)<\alpha\}$，$A_n$ 遞增，聯集是 $[a,b)$（因為 $f_n(x)\to0$）。
3. $B_n=A_n\setminus A_{n-1}$ 互不相交，每個是有限多個半開區間的聯集，合起來是 $[a,b)$ 的分割。由 Lemma 2.2.4，長度總和 $=b-a$，所以尾巴長度能任意小。
4. 選 $n_0$ 使尾巴長度 $<\delta=\frac{\varepsilon}{2\max f_1}$。把 $f_{n_0}$ 拆成「$f_{n_0}<\alpha$ 的部分」和「剩下的部分」，用 Lemma 2.2.3 估計：前者積分 $<\alpha(b-a)=\varepsilon/2$，後者 $<\delta\max f_1=\varepsilon/2$。
5. 所以 $\int f_{n_0}<\varepsilon$，但 $\int f_n$ 遞減到 $\varepsilon$，矛盾。

（這裡用到 Lemma 2.2.4，也就是 $\mathbb{R}$ 的完備性。）

### Corollary 2.2.7

[▶ 48:31](https://youtu.be/-eopGv3Vfto?t=2911)

$(f_n)$ 是**非遞減**的階梯函數列。若 $\lim_nf_n(x)\ge0$ 對每個 $x$，則 $\lim_n\int f_n\ge0$（極限可以是 $+\infty$）。

講者說證明只有幾行，巧妙地用了前一個定理、max、積分的線性。

【課本補充】證明：$\max\{0,-f_n\}$ 是非遞增、非負的階梯函數列，逐點趨近 0（因為 $f_n$ 的極限 $\ge0$）。由 Theorem 2.2.6，$\int\max\{0,-f_n\}\to0$。而 $f_n=\max\{0,f_n\}-\max\{0,-f_n\}$，所以

$$\int f_n=\int\max\{0,f_n\}-\int\max\{0,-f_n\}\ge-\int\max\{0,-f_n\}\to0.$$

---

## 7. Lebesgue 可積函數的定義

[▶ 51:18](https://youtu.be/-eopGv3Vfto?t=3078) 課本 Definition 2.3.1。⚠️ 逐字稿缺字：講者自己提到拼法是 L-e-b-e-s-g-u-e，「有時看到拼成 q」。

**定義**：實值函數 $f:\mathbb{R}\to\mathbb{R}$ 叫 **Lebesgue 可積（Lebesgue integrable）**，如果存在階梯函數列 $(f_n)$ 滿足：

- (a) $\displaystyle\sum_{n=1}^\infty\int|f_n|<\infty$；
- (b) $\displaystyle f(x)=\sum_{n=1}^\infty f_n(x)$ 對每個使 $\displaystyle\sum_{n=1}^\infty|f_n(x)|<\infty$ 的 $x$。

這時定義

$$\int f=\sum_{n=1}^\infty\int f_n, \tag{2.10}$$

並寫 $f\simeq f_1+f_2+\cdots$ 或 $f\simeq\sum f_n$。

**記號**[▶ 55:25](https://youtu.be/-eopGv3Vfto?t=3325)：講者說 $\simeq$ 常用來表示「等價」；他暫時念成「等價」，之後會有「幾乎處處」這個詞說得更精確。課本接下來幾頁就在解釋為什麼用這個記號。

**白話**【課堂討論】[▶ 57:13](https://youtu.be/-eopGv3Vfto?t=3433) 學生的總結：存在一串階梯函數，面積（絕對值）加起來有限，它們的**級數和**就是 $f$；要積分 $f$，就把階梯函數的積分加起來。講者補充：要說「級數的和」，也就是部分和數列的極限。

**為什麼比 Riemann 積分更一般**【課堂討論】[▶ 58:58](https://youtu.be/-eopGv3Vfto?t=3538)：

- Riemann 積分只能處理**有限多個**不連續點；Lebesgue 積分不在乎有多少個不連續點，只要面積有界就能處理非常不連續的函數。
- 講者補充（part 2）：嚴格說，Riemann 積分是為**連續函數**準備的；它的主要定理（微積分基本定理等）的證明都用到中間值定理、極值定理，連續性「烤在定理裡」。Lebesgue 積分不需要連續性。具體的例子之後會看到。[▶ part 2 00:03](https://youtu.be/Uq9O8NvL_ok?t=3)

【課本補充】課本接著（p. 45）說：要證 (2.10) 定義合理，必須證 $\int f$ 不依賴表示 $f\simeq f_1+f_2+\cdots$ 的選擇（Lemma 2.3.2、Corollary 2.3.3）。下一集講。

---

## 8. 第 2 章路線圖

【口頭】[▶ part 2 01:09](https://youtu.be/Uq9O8NvL_ok?t=69)

| 節 | 內容 |
|---|---|
| §2.3 | 積分與表示無關；$L^1(\mathbb{R})$ |
| §2.4 | 可積函數的絕對值 |
| §2.5 | 可積函數的級數 |
| §2.6 | $L^1$ 範數、範數收斂 |
| §2.7 | 幾乎處處收斂（Definition 2.7.6, p. 56）：$f_n(x)\to f(x)$ 對**零集以外**的每個 $x$ |
| §2.8 | 收斂定理：單調收斂定理、Lebesgue 控制收斂定理、Fatou 引理 |
| §2.9 | 局部可積函數 |
| §2.10 | Lebesgue 積分 vs Riemann 積分；微積分基本定理 |
| §2.11 | 可測集 |
| 之後 | 複值函數、$\mathbb{R}^N$ 上的函數 |

講者說「幾乎處處」這個概念會開始搔到今天的癢處。他會盡量不在技術性證明上停太久，「在這種材料上很容易花很多時間證一件事，卻收穫不多」。

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵 |
|---|---|---|
| 階梯函數 | $f=\sum_{k=1}^n\lambda_k\chi_{[a_k,b_k)}$ | 半開區間；基本表示：不相交、最少個數 |
| 積分 | $\int f=\sum\lambda_k(b_k-a_k)$ | 不依賴表示（重疊也可以） |
| 性質 | 線性、單調、$|\int f|\le\int|f|$、平移不變 | $f\ge0\Rightarrow\int f\ge0$ |
| min/max | $\frac12(f+g\mp|f-g|)$ | 逐點理解 |
| 平移 | $(\tau_zf)(x)=f(x-z)$ | 向右移 $z$ |
| Lemma 2.2.4 | 可數分割 ⟹ $\sum(b_n-a_n)=b-a$ | 用 $\mathbb{R}$ 的完備性 |
| Example 2.2.5 | $\mathbb{Q}$ 中 $[0,1)_\mathbb{Q}$ 可被總長 $<\varepsilon$ 蓋住 | $q_n$ 處放長 $\varepsilon/2^{n+1}$ |
| Thm 2.2.6 | 非負非遞增、逐點 $\to0$ ⟹ $\int f_n\to0$ | 拆成「值小」和「區間短」兩部分 |
| Cor 2.2.7 | 非遞減、逐點極限 $\ge0$ ⟹ $\lim\int f_n\ge0$ | $f_n=\max\{0,f_n\}-\max\{0,-f_n\}$ |
| Lebesgue 可積 | $\sum\int|f_n|<\infty$，且絕對收斂處 $f=\sum f_n$ | $\int f=\sum\int f_n$ |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Definition 2.3.1 | 第 12 集：積分與表示無關、$L^1(\mathbb{R})$ |
| Corollary 2.2.7 | 第 12 集：Lemma 2.3.2 的證明 |
| $\chi_{\mathbb{Q}}$ | 第 16 集：Riemann 不可積但 Lebesgue 可積 |
| 「級數只在零集以外收斂」 | 第 14 集：零集、幾乎處處 |
| 平移 $\tau_z$ | 第 17 集：摺積 |

---

## 附：本集一句話總結

> **這本書不先建測度，而是直接從半開區間上的階梯函數出發：階梯函數的積分就是「高度 × 寬度」加起來；一個函數如果能寫成一串階梯函數的級數，而且這些階梯函數的 $\int|f_n|$ 加起來有限，它就是 Lebesgue 可積的，積分就是 $\sum\int f_n$——背後撐住一切的是 ℝ 的完備性。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-08 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 5:02）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.1–2.3 整理。*
