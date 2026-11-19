---
course: Number Theory（2021 秋，線上錄影）
episode: 24
lecture: 2021-10-11
date: 2021-10-11
video: https://youtu.be/PUh12RiezXc
notes: 講者照 Stillwell《Elements of Number Theory》第 8 章（講者的講義掃描檔）；Jones & Jones《Elementary Number Theory》§10.4 Lemma 10.5、Theorem 10.6（書頁 202–204，PDF 頁 217–219）、§10.5 四元數（書頁 205–206，PDF 頁 220–221）
---

# 第 24 集 · 四元數與它在數論的應用（Quaternions and Their Application to Number Theory） [▶ 影片](https://youtu.be/PUh12RiezXc)

← 上一集：[23-proving-fermats-last-theorem](23-proving-fermats-last-theorem.md) ｜ [總目錄](README.md) ｜ 下一集：[25-quadratic-reciprocity-1](25-quadratic-reciprocity-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 24 集（2021-10-11）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:12，自動字幕）＋ Jones & Jones《Elementary Number Theory》§10.4–10.5
> **注意**：這部是講者生病在家錄的，對著螢幕上的講義掃描檔講（「我寧願跟你們在教室，但我還是覺得不太舒服」）。講義上的式子很多沒唸出來，下面依 Stillwell 和課本重建，重建的地方會標明。
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：複數當 2×2 實矩陣，範數 = 行列式](#1-回顧複數當-22-實矩陣範數--行列式)
- [2. 四元數當 2×2 複矩陣](#2-四元數當-22-複矩陣)
- [3. 1、i、j、k 的乘法表](#3-1ijk-的乘法表)
- [4. 標準寫法：t + xi + yj + zk](#4-標準寫法t--xi--yj--zk)
- [5. 範數有乘性 ⇒ 四平方恆等式](#5-範數有乘性--四平方恆等式)
- [6. Hurwitz 整數](#6-hurwitz-整數)
- [7. 除法、右因數、Euclid 演算法](#7-除法右因數euclid-演算法)
- [8. 四平方定理的證明](#8-四平方定理的證明)
- [9. 歷史與賦範可除代數](#9-歷史與賦範可除代數)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

用**四元數**（quaternions）推導**四平方定理**：每個非負整數都是四個平方數的和。架構完全模仿高斯整數證明兩平方和的方式（第 15–21 集）。講者依 Stillwell 第 8 章。

| 主題 | 時間 |
|---|---|
| 複數當矩陣 | 00:03 |
| 四元數當矩陣 | 02:37 |
| $i,j,k$ 的乘法 | 06:13 |
| 標準寫法、點積與叉積 | 09:44 |
| 四平方恆等式 | 15:22 |
| Hurwitz 整數 | 19:29 |
| 除法、Euclid 演算法 | 31:04 |
| 四平方定理 | 40:57 |
| 歷史 | 48:18 |
| 賦範可除代數 | 57:19 |

【口頭】講者說他講義的印表機「不太行」，有些地方要手寫補；PDF 掃描檔沒問題，放在他網站的數論頁面。

---

## 1. 回顧：複數當 2×2 實矩陣，範數 = 行列式

[▶ 00:03](https://youtu.be/PUh12RiezXc?t=3)

（第 1–2 集講過。）$a+bi\leftrightarrow\begin{pmatrix}a&-b\\b&a\end{pmatrix}$（講者這次寫成 $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$，轉置一下，效果一樣）。兩個這種矩陣相乘，就是對應的複數相乘。

**新觀點：範數 = 行列式** [▶ 00:35](https://youtu.be/PUh12RiezXc?t=35)：
$$\det\begin{pmatrix}a&-b\\b&a\end{pmatrix} = a^2+b^2 = N(a+bi).$$

所以**範數的乘性**就是**行列式的乘性** $\det(AB) = \det A\det B$——「很漂亮」。講者說之前（第 15 集）是用「乘積的共軛 = 共軛的乘積」證的，那是大家在別的課證過的；「這個某種意義上是更完整的證明」。

【口頭】[▶ 01:35](https://youtu.be/PUh12RiezXc?t=95) 複數「是」2×2 矩陣嗎？講者重申第 2 集的立場：不是，複數有好幾種構造法，這只是其中一種。複數是「像實數那樣、但添加了一個平方為 $-1$ 的元素 $i$、加乘行為正常的形式系統」。矩陣模型給他信心：**真的存在**有這些性質的東西。

---

## 2. 四元數當 2×2 複矩陣

[▶ 02:37](https://youtu.be/PUh12RiezXc?t=157)

> **定義（矩陣模型）**：**四元數**是形如
> $$q = \begin{pmatrix}\alpha & \beta\\ -\bar\beta & \bar\alpha\end{pmatrix},\qquad\alpha,\beta\in\mathbb{C}$$
> 的 2×2 複矩陣。四元數全體記作 $\mathbb{H}$。

- 對角線上兩個元素互為共軛；非對角線上兩個元素差一個共軛和一個負號。
- **乘法封閉** [▶ 03:08](https://youtu.be/PUh12RiezXc?t=188)：兩個這種矩陣相乘，還是這種形狀。

> **定義**：四元數的**範數**是行列式
> $$N(q) = \det q = \alpha\bar\alpha+\beta\bar\beta = |\alpha|^2+|\beta|^2.$$

若 $\alpha = a+bi$、$\beta = c+di$，則 [▶ 04:10](https://youtu.be/PUh12RiezXc?t=250)
$$N(q) = a^2+b^2+c^2+d^2.$$
講者：「也許你開始看出這跟四平方恆等式有關了。」

**性質**（因為是矩陣）[▶ 04:42](https://youtu.be/PUh12RiezXc?t=282)：

- 結合律、兩邊的分配律都成立。
- **範數有乘性**（行列式的乘性）。
- **乘法不可交換**——跟矩陣乘法一樣。

（講者說第 1 節的那種矩陣彼此**可以**交換，「用矩陣也可以建可交換的代數」。）

---

## 3. 1、i、j、k 的乘法表

[▶ 05:42](https://youtu.be/PUh12RiezXc?t=342)

講者：實際上我們用比較好的記號，就像研究複數時寫 $a+bi$ 而不是 2×2 矩陣。令

$$\mathbf 1 = \begin{pmatrix}1&0\\0&1\end{pmatrix},\quad \mathbf i = \begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad \mathbf j = \begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad \mathbf k = \begin{pmatrix}0&i\\i&0\end{pmatrix}.$$

（矩陣的具體寫法**不是逐字稿內容**——講者指著講義說「這個矩陣叫 $i$……」，沒唸出元素。上面是符合 $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$ 形式的標準選法。）

**乘法表** [▶ 07:14](https://youtu.be/PUh12RiezXc?t=434)：

$$\mathbf i^2 = \mathbf j^2 = \mathbf k^2 = -1,$$
$$\mathbf{ij} = \mathbf k = -\mathbf{ji},\qquad \mathbf{jk} = \mathbf i = -\mathbf{kj},\qquad \mathbf{ki} = \mathbf j = -\mathbf{ik}.$$

（這裡 $-1$ 指矩陣 $-\mathbf 1$。講者：「用同一個 1 表示不同東西有歧義的危險——但就是這樣。我很討厭人家說『就是這樣』，結果我自己也在說，可悲。」）

**跟叉積的關係** [▶ 08:44](https://youtu.be/PUh12RiezXc?t=524)：這些規則從微積分三的**叉積**看很自然：$\mathbf i\times\mathbf j = \mathbf k$、$\mathbf j\times\mathbf k = \mathbf i$、$\mathbf k\times\mathbf i = \mathbf j$，而且叉積**反交換**。但 Hamilton 那時叉積還不普及，向量學派（Gibbs 等人）是在四元數**之後**才發展的。【口頭】「大約有 50 年，四元數的地位就像今天的向量。」

【口頭】[▶ 07:44](https://youtu.be/PUh12RiezXc?t=464) **Hamilton**（19 世紀中葉）發現四元數時**不是**用 2×2 複矩陣，他直接寫下 $\mathbb{R}^4$ 上的乘法規則（就是上面的表），大概沒先擔心模型存不存在。

> 【課本補充】§10.5（p. 205）：Hamilton 想找一個三維的數系模擬 $\mathbb{R}^3$，就像 $\mathbb{C}$ 模擬平面，特別是要「乘積的長度 = 長度的乘積」。試了好幾年失敗，**1843 年**他明白需要**四維**。課本直接用 $q = a+bi+cj+dk$ 和上面的乘法規則定義，並假設分配律。課本也記作 $\mathbb{H}$（紀念 Hamilton）。

---

## 4. 標準寫法：t + xi + yj + zk

[▶ 09:44](https://youtu.be/PUh12RiezXc?t=584)

> $$q = t+x\mathbf i+y\mathbf j+z\mathbf k,\qquad t,x,y,z\in\mathbb{R}.$$
> - **實部** $t$，**虛部** $x\mathbf i+y\mathbf j+z\mathbf k$。
> - **共軛** $\bar q = t-x\mathbf i-y\mathbf j-z\mathbf k$（實部減虛部）。
> - 虛部為 0 叫**實的**；實部為 0 叫**純虛的**（pure imaginary）。
> - **範數** $N(q) = q\bar q = t^2+x^2+y^2+z^2$。

講者：「很漂亮，跟複數系統很合拍。但這是**不可交換**的系統，卻跟可交換的數系有那麼多共同點，很特別。我常聽人說四元數『只偏了一點點』。」

**兩個純虛四元數相乘** [▶ 10:44](https://youtu.be/PUh12RiezXc?t=644)：把它們看成 $\mathbb{R}^3$ 的向量 $\vec\alpha_1,\vec\alpha_2$，展開後
$$\alpha_1\alpha_2 = -\vec\alpha_1\cdot\vec\alpha_2 + \vec\alpha_1\times\vec\alpha_2.$$
（$\mathbf i^2$ 等給出 $-1$ → 點積那項；$\mathbf{ij},\mathbf{ji}$ 等給出叉積那項。）**四元數乘法同時含有點積和叉積**——比向量記號早約 50 年。

**驗證 $N(q) = q\bar q$** [▶ 12:49](https://youtu.be/PUh12RiezXc?t=769)：寫 $q = t+\alpha$（$\alpha$ 純虛）。
$$q\bar q = (t+\alpha)(t-\alpha) = t^2 - \alpha^2 = t^2+\vec\alpha\cdot\vec\alpha = t^2+x^2+y^2+z^2.$$
（$t\alpha$ 和 $-t\alpha$ 抵消；$\alpha\alpha = -\vec\alpha\cdot\vec\alpha+\vec\alpha\times\vec\alpha = -|\vec\alpha|^2$，因為向量跟自己的叉積是 0。）

---

## 5. 範數有乘性 ⇒ 四平方恆等式

[▶ 13:51](https://youtu.be/PUh12RiezXc?t=831)

**引理**（講者說留給學生——「我剛找到一個作業題」）：**乘積的共軛是共軛的乘積，但順序相反**：
$$\overline{q_1q_2} = \bar q_2\,\bar q_1.$$

講者：「這其實非常重要。」有了它：
$$N(q_1q_2) = (q_1q_2)\overline{(q_1q_2)} = q_1q_2\bar q_2\bar q_1 = q_1\,N(q_2)\,\bar q_1 = N(q_1)N(q_2).$$
（$N(q_2)$ 是實數，可以跟任何東西交換，拉出來。）

**四平方恆等式** [▶ 15:22](https://youtu.be/PUh12RiezXc?t=922)：$N(q_1)N(q_2) = N(q_1q_2)$ **就是**四平方恆等式。展開：設 $q_1 = a_1+b_1\mathbf i+c_1\mathbf j+d_1\mathbf k$、$q_2$ 類似，把 $q_1q_2$ 乘開（講者說「直接但冗長」——又一個作業題），再取範數：

$$(a_1^2+b_1^2+c_1^2+d_1^2)(a_2^2+b_2^2+c_2^2+d_2^2) = (\cdots)^2+(\cdots)^2+(\cdots)^2+(\cdots)^2.$$

右邊四個括號的具體內容講者沒唸；見下面的課本補充。

- 講者說這是 **Euler 在 1748 年**發現的（沒有用四元數）。Euler 想證明所有自然數都是四平方和；**Lagrange 在 1770 年**做到了。
- 「這**映照**了我們用高斯整數的結構證明兩平方定理的方式。」

> 【課本補充】§10.4 Lemma 10.5（p. 202）：四平方和的集合 $S_4$ **對乘法封閉**，因為恆等式（10.3）
> $$\begin{aligned}
> (a_1^2+b_1^2+c_1^2+d_1^2)(a_2^2+b_2^2+c_2^2+d_2^2) ={}& (a_1a_2-b_1b_2-c_1c_2-d_1d_2)^2\\
> &+(a_1b_2+b_1a_2+c_1d_2-d_1c_2)^2\\
> &+(a_1c_2-b_1d_2+c_1a_2+d_1b_2)^2\\
> &+(a_1d_2+b_1c_2-c_1b_2+d_1a_2)^2.
> \end{aligned}$$
> §10.5（p. 206）：四個括號正好是 $q_1q_2$ 的四個分量（式 10.8）；Exercise 10.15–10.16 就是講者留的作業：證 $|q|^2 = q\bar q$、$\overline{q_1q_2} = \bar q_2\bar q_1$，推出恆等式。

【口頭】[▶ 18:58](https://youtu.be/PUh12RiezXc?t=1138) 四元數有一群忠實粉絲，說它在電腦程式裡做旋轉比較好（萬向鎖等等）。講者：「我試過搞懂怎麼用四元數實作旋轉，感覺是數學的黑洞。不複雜，但我們就不談了。」

---

## 6. Hurwitz 整數

[▶ 19:29](https://youtu.be/PUh12RiezXc?t=1169)

用複數解兩平方問題時，我們看的是**整係數**的複數 $\mathbb{Z}[i]$。所以第一個嘗試是**整係數四元數** $\mathbb{Z}[\mathbf i,\mathbf j,\mathbf k]$。

**問題**：跟 $\mathbb{Z}[\sqrt{-3}]$ 一樣（第 22 集），**太稀疏**，除法定理不成立。

**修補**：加入**半整數**點：

> **定義**：**Hurwitz 整數**（Hurwitz, 1896）是由 $\mathbf i,\mathbf j,\mathbf k$ 和
> $$\frac{1+\mathbf i+\mathbf j+\mathbf k}{2}$$
> 生成的四元數，也就是 $\dfrac{a+b\mathbf i+c\mathbf j+d\mathbf k}{2}$，其中 $a,b,c,d$ **全是偶數或全是奇數**。

講者：「這個可怕的代數系統。」它的和、差、積還是 Hurwitz 整數，而且**範數是普通整數**。

**例子** [▶ 20:30](https://youtu.be/PUh12RiezXc?t=1230)：
$$N\left(\frac{7+\mathbf i+\mathbf j+\mathbf k}{2}\right) = \frac{49+1+1+1}{4} = \frac{52}4 = 13.$$
範數是質數，所以它是 **Hurwitz 質數**（「照老理由」）。

**為什麼範數是整數** [▶ 21:32](https://youtu.be/PUh12RiezXc?t=1292)：寫成 $a\cdot\frac{1+\mathbf i+\mathbf j+\mathbf k}2+b\mathbf i+c\mathbf j+d\mathbf k$，範數是
$$\frac14\left[a^2+(a+2b)^2+(a+2c)^2+(a+2d)^2\right].$$
- $a$ 偶：四個括號都是偶數，平方都是 4 的倍數，除以 4 是整數。
- $a$ 奇：四個括號都是奇數；奇數的平方是 $4k+1$ 型，四個加起來是 4 的倍數。✓

（講者說「這很像我給你們的某個作業題」。）

**一個結果** [▶ 25:10](https://youtu.be/PUh12RiezXc?t=1510)：若 $p$ 是整數質數但**不是** Hurwitz 質數，則 $p$ 是四個平方的和 $a^2+b^2+c^2+d^2$，其中 $2a,2b,2c,2d$ 是整數（$a,b,c,d$ 可能是半整數）。

**證明大意** [▶ 26:43](https://youtu.be/PUh12RiezXc?t=1603)：$p = (a+b\mathbf i+c\mathbf j+d\mathbf k)\gamma$，取範數 $p^2 = (a^2+b^2+c^2+d^2)\,N(\gamma)$。兩個因數都 $>1$（非平凡），所以都是 $p$。「這很像高斯整數裡『$p$ 是整數質數但不是高斯質數 ⇔ $p=a^2+b^2$』。」

【口頭】講者說「我不建議你們抄下這些證明，我無意考細節，會考大故事」。他也在講義裡看到一個看似重複的命題（「質數不是 Hurwitz 質數就是四個整數平方和」），「我搞不懂它為什麼在這，一定是我漏了什麼」。

> 以下**不是逐字稿內容**，是解釋那兩個命題的差別：第一個只說 $a,b,c,d$ 是**半整數**；第二個要的是**整數**平方和。從半整數換成整數需要一個技巧：Hurwitz 整數 $\alpha$ 的係數若全是半奇數，就乘上適當的單位（例如 $\frac{\pm1\pm\mathbf i\pm\mathbf j\pm\mathbf k}2$）讓係數變整數，範數不變。這就是那個命題要補的那一步。

---

## 7. 除法、右因數、Euclid 演算法

[▶ 31:04](https://youtu.be/PUh12RiezXc?t=1864)

**除法性質**：$\alpha,\beta$ 是非零 Hurwitz 整數，存在 Hurwitz 整數 $\mu,\rho$ 使
$$\alpha = \mu\beta+\rho,\qquad N(\rho)<N(\beta).$$

講者說 Stillwell 聲稱 §8.5 有證明，但「我沒看到」，所以他講義裡寫了「幾乎是證明」的東西 [▶ 31:36](https://youtu.be/PUh12RiezXc?t=1896)：Hurwitz 整數組成四維格子；$\alpha\beta^{-1}$ 是某個四元數，取最近的格點 $\mu$，希望 $N(\alpha\beta^{-1}-\mu)<1$，再令 $\rho = \alpha-\mu\beta$。講者講到一半卡住（「抱歉，我卡在某個地方，可能是某個字母寫錯」），也注意到四維裡 $(\frac12,\frac12,\frac12,\frac12)$ 到原點距離剛好是 1。

> 以下**不是逐字稿內容**，是解開卡住的地方：整係數四元數 $\mathbb{Z}[\mathbf i,\mathbf j,\mathbf k]$ 裡，最壞的點 $(\frac12,\frac12,\frac12,\frac12)$ 距離平方是 $4\cdot\frac14 = 1$，不小於 1——所以整係數不行（「太稀疏」）。但**這個點本身就是 Hurwitz 整數**（$\frac{1+\mathbf i+\mathbf j+\mathbf k}2$）。加入半整數點後，任何四元數到最近的 Hurwitz 整數距離平方最多 $\frac12$，嚴格小於 1，除法性質成立。

**右因數與左因數** [▶ 35:58](https://youtu.be/PUh12RiezXc?t=2158)：不可交換，所以要分：
- $\delta$ 是 $\alpha$ 的**右因數**：$\alpha = \gamma\delta$。
- $\delta$ 是 $\alpha$ 的**左因數**：$\alpha = \delta\gamma$。

一個成立不代表另一個成立。Stillwell 用**公共右因數**：若 $\delta$ 右整除 $\alpha$ 和 $\beta$，它也右整除 $\rho = \alpha-\mu\beta$。所以 **Euclid 演算法照樣成立**（注意左右），最後一個非零餘數是右 gcd，而且（Bézout）可以寫成 $\mu\alpha+\nu\beta$。

【口頭】「右因數都還好嗎？——抱歉，這通常不會出現在我的課裡。」「乘在哪一邊非常要緊，跟矩陣一樣挑剔。」

**質因數性質** [▶ 38:01](https://youtu.be/PUh12RiezXc?t=2281)：若 $p$ 是**實的**質數，$p\mid\alpha\beta$，則 $p\mid\alpha$ 或 $p\mid\beta$。

**證明**：設 $p\nmid\alpha$，則右 gcd 可取 1：$\mu p+\nu\alpha = 1$。**右乘** $\beta$：$\mu p\beta+\nu\alpha\beta = \beta$。$p$ 整除兩項（$p$ 是實數，可以移到任何一邊），所以 $p\mid\beta$。

講者：「（除了我把證明講得很糊之外）這跟我們以前可交換時證質因數性質的方式完全一樣。」（第 5 集、第 17 集。）

---

## 8. 四平方定理的證明

[▶ 40:57](https://youtu.be/PUh12RiezXc?t=2457)

> **四平方定理**（Lagrange, 1770）：每個非負整數都能寫成 $a^2+b^2+c^2+d^2$（$a,b,c,d$ 非負整數）。

**Step 1：化簡到奇質數** [▶ 40:57](https://youtu.be/PUh12RiezXc?t=2457)

- $0 = 0^2+0^2+0^2+0^2$、$1 = 1^2+0+0+0$、$2 = 1^2+1^2+0+0$。
- 若 $a$、$b$ 都是四平方和，由**四平方恆等式**，$ab$ 也是。重複用（例如 $abc = a\cdot(bc)$）。
- 每個整數都是質數的乘積，$2$ 已經是四平方和，所以**只要證每個奇質數 $p$ 是四平方和**。

**Step 2：Lagrange 引理** [▶ 43:37](https://youtu.be/PUh12RiezXc?t=2617)

> **引理**（Lagrange）：若 $p$ 是奇質數，則存在整數 $l,m$ 使 $p\mid 1+l^2+m^2$。

講者說證明是「模 $p$ 的同餘論證」，不細講，「我想把重點放在四元數的部分」。

> 【課本補充】§10.4 Theorem 10.6 的證明（p. 203）給了這個引理的證明：$\mathbb{Z}_p$ 裡**恰好有 $\frac{p+1}2$ 個平方數**（$0$ 和 $\frac{p-1}2$ 個二次剩餘）。所以 $K = \{k^2\}$ 有 $\frac{p+1}2$ 個元素，$L = \{-1-l^2\}$ 也有 $\frac{p+1}2$ 個。兩個都超過 $\mathbb{Z}_p$ 的一半，所以**一定有交集**：$u^2\equiv -1-v^2$，即 $p\mid u^2+v^2+1$。例：$p=7$，$K = \{0,1,2,4\}$、$L = \{2,4,5,6\}$，取 $u=3,v=2$：$9+4+1 = 14$。

**Step 3：用 Hurwitz 整數分解** [▶ 46:09](https://youtu.be/PUh12RiezXc?t=2769)

$$1+l^2+m^2 = (1-l\mathbf i-m\mathbf j)(1+l\mathbf i+m\mathbf j).$$
（就是 $\bar\alpha\alpha$，$\alpha = 1+l\mathbf i+m\mathbf j$。）

**Step 4：反證 $p$ 不是 Hurwitz 質數** [▶ 47:16](https://youtu.be/PUh12RiezXc?t=2836)

- 假設 $p$ 是 Hurwitz 質數。$p$ 整除乘積，由質因數性質，$p$ 整除其中一個因數，例如 $1+l\mathbf i+m\mathbf j = p\gamma$。
- 那 $\gamma = \frac1p+\frac lp\mathbf i+\frac mp\mathbf j$。但 $p$ 是奇質數，$\frac1p$ 既不是整數也不是半整數，所以 $\gamma$ **不是** Hurwitz 整數。矛盾。

（講者的說法：「$p$ 兩個都整除……不存在這樣的 $\gamma$，因為 $p\neq 2$。」上面是把論證寫完整。）

**Step 5**：所以 $p$ 是整數質數但不是 Hurwitz 質數，由第 6 節的結果，**$p$ 是四平方和**。∎

講者：「我們不能預設奇質數自動不是 Hurwitz 質數，所以要先反證。反證完，就知道它是四平方和——四平方定理。」

> 【課本補充】§10.4 Theorem 10.6（p. 203–204）給的是**不用四元數**的證明，模仿兩平方定理的 Fermat 遞降法：取最小的 $m$ 使 $mp$ 是四平方和，若 $m>1$ 就用四平方恆等式（10.4）造出更小的 $sp$，矛盾。課本說「第 10.6 節還會給幾何證明」。

---

## 9. 歷史與賦範可除代數

[▶ 48:18](https://youtu.be/PUh12RiezXc?t=2898)

**兩平方恆等式** $(a_1^2+b_1^2)(a_2^2+b_2^2) = (a_1a_2-b_1b_2)^2+(a_1b_2+b_1a_2)^2$：

| 時間 | 誰 | 做了什麼 |
|---|---|---|
| 約 200（講者也說 280） | Diophantus | 已知道 |
| 稍晚 | 印度數學家 | 多處獨立發現（講者說「我想他們也知道四平方定理，如果我沒記錯」） |
| 1593 | Viète | 發現**幾何意義** |
| 之後 | Cotes、de Moivre、Euler | Euler 的 $e^{i\theta} = \cos\theta+i\sin\theta$ |
| 19 世紀 | Dedekind | 用高斯整數乾淨地推出恆等式和相關定理（Stillwell 用的是 Dedekind 的論證；我們跟 Conrad 走了稍微不同的路） |

【口頭】[▶ 49:19](https://youtu.be/PUh12RiezXc?t=2959) 有人說複平面（把複數對應到 $\mathbb{R}^2$）到 19 世紀中葉才被發現，講者說「我很難相信 Euler 寫了那些公式卻不知道這個對應」。

**幾何意義** [▶ 50:21](https://youtu.be/PUh12RiezXc?t=3021)：兩個直角三角形，斜邊長 $h_1,h_2$、角度 $\theta_1,\theta_2$。造第三個三角形，斜邊 $h_1h_2$，兩股分別是 $a_1a_2-b_1b_2$ 和 $a_1b_2+b_1a_2$。

- 三個三角形各自的**畢氏定理**，加上「斜邊相乘」，**就是**兩平方恆等式。
- 講者再用正切的和角公式算出新三角形的角是 $\theta_1+\theta_2$。用指數寫：$h_1e^{i\theta_1}\cdot h_2e^{i\theta_2} = h_1h_2\,e^{i(\theta_1+\theta_2)}$——「長度相乘、角度相加」。

（講者一開始說「此刻我搞不清楚重點是什麼」，後來說「喔，我看到了」，就是上面兩點。）

**四平方恆等式與四元數** [▶ 55:13](https://youtu.be/PUh12RiezXc?t=3313)：

| 時間 | 誰 | 做了什麼 |
|---|---|---|
| 1748 | Euler | 四平方恆等式 |
| 約 1840 | Rodrigues | 旋轉的乘積（講者說 Stillwell 沒細講） |
| 1843 | **Hamilton** | 發現四元數 |
| 19 世紀末 | Hurwitz | Hurwitz 整數，自然地推出四平方恆等式 |

【口頭】[▶ 56:15](https://youtu.be/PUh12RiezXc?t=3375) Hamilton 花了**約十年**找一種三維的乘法，像複數在二維那樣——複數自然地實現平面旋轉，「很自然會想在 $\mathbb{R}^3$ 也做到」。**做不到**：$\mathbb{R}^3$ 上有乘性範數的乘法會推出**三平方恆等式**，而 Legendre 早就知道三平方恆等式不存在。「如果 Hamilton 知道這件事，他就不會去找了。」最後他**加了一個維度**，很快就解決了。

**賦範可除代數** [▶ 57:19](https://youtu.be/PUh12RiezXc?t=3439)：

> **定義**：**賦範可除代數**（normed division algebra）是 $\mathbb{R}$ 上的向量空間，配一個乘法，滿足 $N(zw) = N(z)N(w)$。（通常 $N(z)$ 是長度；數論裡取長度平方，去掉根號，方便直接論證。）

> **定理**（講者說有時叫 Hurwitz 定理）：賦範可除代數**只有** $\mathbb{R}$、$\mathbb{C}$、$\mathbb{H}$（四元數）、$\mathbb{O}$（八元數 octonions）。等價地，**只有 $n = 1,2,4,8$ 有 $n$ 平方恆等式**。

- 講者原本打算證這個（「其實只是幾頁線性代數」），但少了幾天課，只好拿掉。
- 這件事反映在很多高等數學裡：某些維度可以用這些乘法做事，別的維度不行。
- 【口頭】「四元數和旋轉——我不會談這個，我不會談這個。」

> 【課本補充】§10.5（p. 206）：
> - Hamilton 發現四元數後不久，**Cayley 和 Graves** 獨立發現了不滿足結合律的八維系統——**八元數** $\mathbb{O}$，給出**八平方恆等式**。
> - **1878 年 Frobenius** 證明：$\mathbb{R}$、$\mathbb{C}$、$\mathbb{H}$ 是 $\mathbb{R}$ 上僅有的有限維**結合**可除代數。
> - **1898 年 Hurwitz** 證明：只有 $k = 1,2,4,8$ 有所需形式的 $k$ 平方恆等式。
> - 課本說這解釋了為什麼**三平方和比兩平方和、四平方和難研究**——沒有三平方恆等式。

講者最後：「你們提早下課了。希望星期三能回來。如果覺得不有趣，抱歉。」

---

## 10. 一頁速查表

**四元數** $q = t+x\mathbf i+y\mathbf j+z\mathbf k$；矩陣模型 $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$。

- $\mathbf i^2=\mathbf j^2=\mathbf k^2=-1$；$\mathbf{ij}=\mathbf k=-\mathbf{ji}$，$\mathbf{jk}=\mathbf i=-\mathbf{kj}$，$\mathbf{ki}=\mathbf j=-\mathbf{ik}$。
- 不可交換；結合、分配。
- $\bar q = t-x\mathbf i-y\mathbf j-z\mathbf k$；$\overline{q_1q_2} = \bar q_2\bar q_1$（順序相反）。
- $N(q) = q\bar q = t^2+x^2+y^2+z^2 = \det$（矩陣模型）。
- 純虛相乘：$\alpha_1\alpha_2 = -\vec\alpha_1\cdot\vec\alpha_2+\vec\alpha_1\times\vec\alpha_2$。

**範數乘性 ⇒ 四平方恆等式**。**關鍵一步**：$N(q_1q_2) = q_1q_2\bar q_2\bar q_1 = q_1N(q_2)\bar q_1$。

**Hurwitz 整數**：$\frac{a+b\mathbf i+c\mathbf j+d\mathbf k}2$，$a,b,c,d$ 同奇偶。範數是整數；有除法性質（半整數點讓格子夠密）；有右 Euclid 演算法；實質數的質因數性質成立。

**四平方定理的證明**

1. $0,1,2$ 是；四平方和乘四平方和還是 ⇒ 只要證奇質數 $p$。
2. Lagrange 引理：$p\mid1+l^2+m^2$（平方數 $\frac{p+1}2$ 個，鴿籠）。
3. $1+l^2+m^2 = (1-l\mathbf i-m\mathbf j)(1+l\mathbf i+m\mathbf j)$。
4. 若 $p$ 是 Hurwitz 質數，則整除某個因數 ⇒ 係數 $\frac1p$ 不是半整數，矛盾。
5. $p$ 不是 Hurwitz 質數 ⇒ $p^2 = N(\alpha)N(\gamma)$ ⇒ $N(\alpha) = p$ ⇒ $p$ 是四平方和。

**賦範可除代數**只有 $\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O}$；$n$ 平方恆等式只有 $n=1,2,4,8$。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Lagrange 引理的「平方數有 $\frac{p+1}2$ 個」⇒ 二次剩餘 | 第 25–26 集（二次互反律） |
| 不可交換的環、右理想 vs 左理想 | 第 27–32 集（環、理想） |
| 「加半整數修補」（Eisenstein、Hurwitz） | 第 22 集對照；第 46–47 集 |
| $\mathbb{H}$ 是可除環但不是體 | 第 27 集起 |

---

## 附：本集一句話總結

> **四元數 $t+x\mathbf i+y\mathbf j+z\mathbf k$ 是不可交換的四維數系，範數 $t^2+x^2+y^2+z^2$ 有乘性——這就是四平方恆等式。仿照高斯整數，用 Hurwitz 整數（加上半整數點）建立除法和質因數性質，配合 Lagrange 引理 $p\mid1+l^2+m^2$，就證出每個整數都是四個平方的和。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-11 錄影逐字稿（YouTube 自動字幕，59:12）與 Jones & Jones《Elementary Number Theory》§10.4–10.5 整理；講者的主要參考是 Stillwell《Elements of Number Theory》第 8 章。*
