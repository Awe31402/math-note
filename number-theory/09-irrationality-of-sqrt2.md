---
course: Number Theory（2021 秋，線上錄影）
episode: 9
lecture: Lecture 9
date: 待補（2021 秋）
video: https://youtu.be/Y4lLt7Pchpc
notes: Jones & Jones §2.1 Corollary 2.5（書頁 24–25，PDF 頁 39–40）；Pell 方程課本無專節（講者引用 Burton、Silverman、Stillwell 的書）
---

# 第 9 集 · Lecture 9：√2 是無理數（Irrationality of the Square Root of 2） [▶ 影片](https://youtu.be/Y4lLt7Pchpc)

← 上一集：[08-structure-of-primes](08-structure-of-primes.md) ｜ [總目錄](README.md) ｜ 下一集：[10-modular-arithmetic](10-modular-arithmetic.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 9 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（27:07，自動字幕）＋ Jones & Jones §2.1 Corollary 2.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 證法一：算術基本定理](#1-證法一算術基本定理)
- [2. 證法二：Bézout](#2-證法二bézout)
- [3. 證法三（未完成）：Eisenstein](#3-證法三未完成eisenstein)
- [4. 數系 Q(√2) 與 Z[√2]](#4-數系-q2-與-z2)
- [5. Pell 方程](#5-pell-方程)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】歷史：約西元前 500 年，畢達哥拉斯學派就知道 $\sqrt2$ 不是有理數（**無理數**，irrational）；講者相信其他古文明也知道 [▶ 00:00](https://youtu.be/Y4lLt7Pchpc?t=0)。

| 段落 | 內容 |
|---|---|
| 1–3 | $\sqrt2$ 是無理數的三個證法（第三個沒成功） |
| 4 | $\mathbb{Q}(\sqrt2)$ 是一個體 |
| 5 | 用 $\mathbb{Z}[\sqrt2]$ 的乘法從一組解生出 Pell 方程 $x^2-2y^2=1$ 的無窮多解 |

---

## 1. 證法一：算術基本定理

[▶ 00:32](https://youtu.be/Y4lLt7Pchpc?t=32)

**定理**：$\sqrt2$ 是無理數。

**證明**（反證）：設 $\sqrt2 = a/b$，$a,b$ 正整數，且分數已約到**最簡**（$\gcd(a,b)=1$；可以先約掉公因數，所以不失一般性）。則
$$2 = \frac{a^2}{b^2}\quad\Longrightarrow\quad 2b^2 = a^2.$$
用同一組質數寫分解（允許指數為 0）：
$$a = p_1^{e_1}\cdots p_k^{e_k},\qquad b = p_1^{f_1}\cdots p_k^{f_k}.$$
於是
$$2\cdot p_1^{2f_1}\cdots p_k^{2f_k} = p_1^{2e_1}\cdots p_k^{2e_k}.$$
質數 2 出現在左邊，所以也出現在右邊：$2 = p_j$ 對某個 $j$。比較 $p_j=2$ 的指數：左邊 $2f_j+1$（奇數），右邊 $2e_j$（偶數）。由分解的**唯一性**，$2f_j+1 = 2e_j$，奇數等於偶數，矛盾。∎

【口頭】這大概是最常見的證法 [▶ 03:14](https://youtu.be/Y4lLt7Pchpc?t=194)。

> 【課本補充】Corollary 2.5（p. 24–25）證更一般的結果：**若正整數 $m$ 不是完全平方數，則 $\sqrt m$ 是無理數。** 證逆否命題：設 $\sqrt m = a/b$，則 $m = a^2/b^2$，分解得
> $$m = p_1^{2e_1-2f_1}\cdots p_k^{2e_k-2f_k} = \left(p_1^{e_1-f_1}\cdots p_k^{e_k-f_k}\right)^2,$$
> 每個指數都是偶數且 $e_i-f_i\ge0$，所以 $m$ 是完全平方數。
>
> 【口頭】講者說課本這個逆否論證他不太容易直接改寫成 $\sqrt2$ 的版本，所以沒用 [▶ 03:45](https://youtu.be/Y4lLt7Pchpc?t=225)。（其實取 $m=2$，2 不是完全平方數，就直接得到 $\sqrt2$ 無理。）

---

## 2. 證法二：Bézout

[▶ 03:45](https://youtu.be/Y4lLt7Pchpc?t=225)

【口頭】出自 David M. Burton《Elementary Number Theory》p. 42，另一本不錯的入門書。講者其實比較喜歡這個證法 [▶ 06:29](https://youtu.be/Y4lLt7Pchpc?t=389)。

**證明**（反證）：設 $\sqrt2 = a/b$，$\gcd(a,b)=1$。由 Bézout，存在整數 $x,y$ 使
$$ax+by = 1.$$
兩邊乘 $\sqrt2$：
$$\sqrt2 = (\sqrt2a)x + (\sqrt2b)y.$$
由 $\sqrt2 = a/b$ 得 $\sqrt2\,b = a$，以及 $\sqrt2\,a = \sqrt2\cdot\sqrt2\,b = 2b$。代入：
$$\sqrt2 = 2bx + ay.$$
右邊是整數，所以 $\sqrt2$ 是整數，不可能。∎

**補洞** [▶ 06:29](https://youtu.be/Y4lLt7Pchpc?t=389)：要說明 $\sqrt2$ 不是整數。講者的想法：平方根函數遞增，$1<2<4$ ⇒ $1=\sqrt1<\sqrt2<\sqrt4=2$，1 和 2 之間沒有整數。

---

## 3. 證法三（未完成）：Eisenstein

[▶ 07:01](https://youtu.be/Y4lLt7Pchpc?t=421)

講者的嘗試：
1. $f(x) = x^2-2$ 由 Eisenstein（$p=2$：$2\mid-2$、$4\nmid-2$、$2\nmid1$）在 $\mathbb{Z}$ 上不可約。
2. 若 $\sqrt2 = a/b$，則 $\pm a/b$ 是 $f$ 的根，由因式定理 $f(x) = \left(x-\tfrac ab\right)\left(x+\tfrac ab\right)$。
3. 乘 $b^2$：$b^2f(x) = (bx-a)(bx+a)$。所以 $b^2f(x)$ 在 $\mathbb{Z}$ 上可約——但這**不是**需要的矛盾：要的是 $f(x)$ 本身可約。

【口頭】「所以，算了。」能修好這個論證的同學可以加分；在 YouTube 上看的人可以得到「免費的網路點數」[▶ 08:39](https://youtu.be/Y4lLt7Pchpc?t=519)。

---

## 4. 數系 Q(√2) 與 Z[√2]

### 4.1 定義

[▶ 09:11](https://youtu.be/Y4lLt7Pchpc?t=551)

$$\mathbb{Q}(\sqrt2) = \{\,a+b\sqrt2 : a,b\in\mathbb{Q}\,\}\quad(\text{讀作「}\mathbb{Q}\text{ 添加 }\sqrt2\text{」，adjoin}),$$
$$\mathbb{Z}[\sqrt2] = \{\,a+b\sqrt2 : a,b\in\mathbb{Z}\,\}.$$
兩者都是 $\mathbb{R}$ 的子集合，加減乘除照實數的規則。

【口頭】**代數數論**用這種數系來揭露質數的性質，以及某些丟番圖方程的結構——例如本集的 Pell 方程 [▶ 09:49](https://youtu.be/Y4lLt7Pchpc?t=589)。

### 4.2 $\mathbb{Z}[\sqrt2]$ 的商落在 $\mathbb{Q}(\sqrt2)$

[▶ 10:22](https://youtu.be/Y4lLt7Pchpc?t=622)

**定理**：若 $z,w\in\mathbb{Z}[\sqrt2]$、$w\neq0$，則 $z/w\in\mathbb{Q}(\sqrt2)$。

（原則上沒理由預期這樣，商可能落在更大的數系裡。）

**證明**：$z = a+b\sqrt2$、$w = c+d\sqrt2$。像上一集一樣乘共軛有理化：
$$\frac{z}{w} = \frac{(a+b\sqrt2)(c-d\sqrt2)}{(c+d\sqrt2)(c-d\sqrt2)} = \frac{ac-2bd}{c^2-2d^2} + \frac{bc-ad}{c^2-2d^2}\sqrt2.$$
只要 $c^2-2d^2\neq0$，兩個係數都是有理數。

**為什麼 $c^2-2d^2\neq0$**：講者先試了幾個數（$c=1$ 給 1 或 $-1$；$c=2$ 要 $d=\sqrt2$）說服自己 [▶ 11:27](https://youtu.be/Y4lLt7Pchpc?t=687)。嚴格的理由他在下一個定理後說：若 $c^2=2d^2$ 且 $d\neq0$，則 $\sqrt2 = |c/d|$ 是有理數，和第 1–2 節矛盾；而 $d=0$ 時 $c^2=0$ 推出 $w=0$。

### 4.3 $\mathbb{Q}(\sqrt2)$ 是體

[▶ 12:32](https://youtu.be/Y4lLt7Pchpc?t=752)

【口頭】「趁停電之前把這集錄完吧」——外面風很大，講者準備了電池和手機手電筒。

**定理**：若 $z = a+b\sqrt2\in\mathbb{Q}(\sqrt2)$（$a,b$ 有理）且 $z\neq0$，則 $1/z\in\mathbb{Q}(\sqrt2)$。

**證明**：
$$\frac1z = \frac{a-b\sqrt2}{(a+b\sqrt2)(a-b\sqrt2)} = \frac{a}{a^2-2b^2} - \frac{b}{a^2-2b^2}\sqrt2,$$
兩個係數都是有理數。$a^2-2b^2\neq0$：若為 0 且 $b\neq0$，則 $\sqrt2 = |a/b|$ 是有理數，矛盾 [▶ 14:08](https://youtu.be/Y4lLt7Pchpc?t=848)。∎

⚠️ 逐字稿缺字：[▶ 13:36](https://youtu.be/Y4lLt7Pchpc?t=816) 字幕說結果「is in z adjoin square root of two」，應為 $\mathbb{Q}(\sqrt2)$（係數是有理數）。

$\mathbb{Q}(\sqrt2)$ 是**有單位元素的交換環**（加法、乘法交換、結合、分配，照一般算術），再加上每個非零元素都有乘法反元素，所以是**體**（第 1 集的定義）。

---

## 5. Pell 方程

### 5.1 歷史

[▶ 14:39](https://youtu.be/Y4lLt7Pchpc?t=879)

**Pell 方程**：$x^2 - ny^2 = 1$。

【口頭】名字是誤稱。講者翻 Joseph H. Silverman《A Friendly Introduction to Number Theory》p. 245 [▶ 15:11](https://youtu.be/Y4lLt7Pchpc?t=911)：
- 最早出現在 **Archimedes 的牛群問題**：八種牛，問各有幾頭，最後化成 $x^2 - 4729494\,y^2 = 1$；1880 年才由 Amthor 解出，解有 41 位數。
- 印度的 Brahmagupta 知道如何用已知解造新解（字幕「magupta」）；西元 1150 年有人給出找初始解的巧妙方法。
- 歐洲：1657 年 Brouncker 描述一般解法（字幕「brookner/bruckner」），Wallis 在書中轉述；Euler 讀了 Wallis 的書，誤以為是 Pell 的方法。

講者：其實是很多社會的很多人，「我們別爭了，這是個古老而重要的問題」；他說自己對歷史問題的終極答案常常是「我不在乎」——也不完全是，只是太久遠的問題資料不夠 [▶ 17:29](https://youtu.be/Y4lLt7Pchpc?t=1049)。

### 5.2 $\mathbb{Z}[\sqrt2]$ 對乘法封閉

[▶ 18:02](https://youtu.be/Y4lLt7Pchpc?t=1082)

$$(x_1+y_1\sqrt2)(x_2+y_2\sqrt2) = (x_1x_2+2y_1y_2) + (x_1y_2+y_1x_2)\sqrt2.$$
還是「整數 + 整數 $\cdot\sqrt2$」。

### 5.3 從兩組解造新解

[▶ 18:35](https://youtu.be/Y4lLt7Pchpc?t=1115)

**定理**：若 $(x_1,y_1)$、$(x_2,y_2)$ 都是 $x^2-2y^2=1$ 的解，則
$$(x_1x_2+2y_1y_2,\ \ x_1y_2+y_1x_2)$$
也是解。

**證明**：在有 $\sqrt2$ 的數系裡，2 是平方數，所以可以用平方差分解：
$$(x_1-y_1\sqrt2)(x_1+y_1\sqrt2) = 1,\qquad (x_2-y_2\sqrt2)(x_2+y_2\sqrt2) = 1.$$
**狡猾的一步**：兩式相乘，把「$-$」配「$-$」、「$+$」配「$+$」：
$$\big[(x_1-y_1\sqrt2)(x_2-y_2\sqrt2)\big]\big[(x_1+y_1\sqrt2)(x_2+y_2\sqrt2)\big] = 1.$$
由 5.2，令 $X = x_1x_2+2y_1y_2$、$Y = x_1y_2+y_1x_2$：
$$(X - Y\sqrt2)(X+Y\sqrt2) = 1.$$
（第一個括號展開時 $\sqrt2$ 項的符號是負的。）再把平方差乘回去：
$$X^2 - 2Y^2 = 1.\ ∎$$

【口頭】
- 「從一對舊解得到新解，非常非常奇怪。大部分方程不是這樣運作的。」[▶ 20:51](https://youtu.be/Y4lLt7Pchpc?t=1251)
- 這些解其實形成一個**群**（group），是數學裡最早的群的例子之一，像循環群，初始解就像生成元——那時還沒人叫它群。講者不展開。

### 5.4 例子：$x^2-2y^2=1$

[▶ 21:59](https://youtu.be/Y4lLt7Pchpc?t=1319)

【口頭】講者問學生這個方程，然後尷尬地盯著他們大約兩分鐘，通常十個人的班五分鐘內一定有人猜到 $x=3$、$y=2$。

- $(3,2)$：$9-2\cdot4 = 1$。✓ 對應 $3+2\sqrt2$。
- 平方：$(3+2\sqrt2)^2 = 9+8+12\sqrt2 = 17+12\sqrt2$ → $(17,12)$：$289-288=1$。✓
- 再乘：$(3+2\sqrt2)(17+12\sqrt2) = 51+48+(36+34)\sqrt2 = 99+70\sqrt2$ → $(99,70)$：$9801-9800=1$。✓
- 再一次：$(99+70\sqrt2)^2 = 9801+9800+13860\sqrt2 = 19601+13860\sqrt2$ → $(19601,13860)$。✓

⚠️ 逐字稿缺字：[▶ 22:31](https://youtu.be/Y4lLt7Pchpc?t=1351) 字幕把 $3+2\sqrt2$ 唸成「3 plus root 2 root 2」，平方算式也唸得含糊（「9 plus 2 times 2 squared plus 12 over 2」）；筆記照正確的乘法寫。最後一組字幕有「19 600 1」「3 13 860」等斷字，應為 $19601$、$13860$。

所以 Pell 方程有**無窮多**整數解：只要有一組解，就能生出一整族。

**初始解怎麼找** [▶ 24:47](https://youtu.be/Y4lLt7Pchpc?t=1487)：
- 如果有人先猜到 $(17,12)$ 而不是 $(3,2)$，從那裡往上生，就會漏掉前面的解。
- 找初始解（以及證明它存在）**難得多**。講者第一次錄 Pell 方程影片時，YouTube 留言有人很氣他沒證明解存在——就是因為很難。
- 推薦 John Stillwell《Elements of Number Theory》論 Pell 方程的那章，封面是 Conway 的「river」圖；讀久了大概能看出怎麼找初始解。講者說這對課程來說總是有點太多，沒教過 [▶ 25:51](https://youtu.be/Y4lLt7Pchpc?t=1551)。

---

## 6. 一頁速查表

**$\sqrt2$ 無理**
- 證法一：$2b^2=a^2$，比較 2 的指數：$2f_j+1 = 2e_j$，奇 = 偶，矛盾。
- 證法二：$ax+by=1$ 乘 $\sqrt2$：$\sqrt2 = 2bx+ay\in\mathbb{Z}$，矛盾（$1<\sqrt2<2$）。
- 【課本】$m$ 不是完全平方數 ⇒ $\sqrt m$ 無理（逆否：$m = (\prod p_i^{e_i-f_i})^2$）。

**$\mathbb{Q}(\sqrt2)$ 是體**
$$\frac{1}{a+b\sqrt2} = \frac{a-b\sqrt2}{a^2-2b^2},\qquad a^2-2b^2\neq0 \text{（否則 }\sqrt2\in\mathbb{Q}\text{）}.$$

**Pell 方程** $x^2-2y^2=1$
- 乘法：$(x_1+y_1\sqrt2)(x_2+y_2\sqrt2) = (x_1x_2+2y_1y_2)+(x_1y_2+y_1x_2)\sqrt2$。
- 新解：兩組解的「$-$」相乘、「$+$」相乘，再用平方差。
- 解：$(3,2)\to(17,12)\to(99,70)\to(19601,13860)$，即 $(3+2\sqrt2)^k$。
- 初始解的存在與尋找很難（Stillwell）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 添加根號的數系 $\mathbb{Z}[\sqrt2]$、$\mathbb{Q}(\sqrt2)$ | 第 21–22 集（高斯整數 $\mathbb{Z}[i]$） |
| $(a+b\sqrt2)(a-b\sqrt2)=a^2-2b^2$（範數） | 第 21–22 集（$N(a+bi)=a^2+b^2$） |
| 解形成群 | 第 14–15 集（群的語言：單位群） |
| 無理性、Pythagoras | 第 24 集（費馬最後定理那章的等腰直角三角形論證） |

---

## 附：本集一句話總結

> **$\sqrt2$ 是無理數（比較 2 的指數，或用 Bézout 推出 $\sqrt2$ 是整數）；由此 $\mathbb{Q}(\sqrt2)$ 是體，而 $\mathbb{Z}[\sqrt2]$ 的乘法讓 Pell 方程 $x^2-2y^2=1$ 從一組解 $(3,2)$ 生出無窮多解：$(3+2\sqrt2)^k$。**

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 9 錄影逐字稿（YouTube 自動字幕，27:07）與 Jones & Jones《Elementary Number Theory》§2.1 Corollary 2.5 整理。*
