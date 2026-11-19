---
course: Number Theory（2021 秋，線上錄影）
episode: 44
lecture: 2021-11-17 第 1 部
date: 2021-11-17
video: https://youtu.be/nOfJamAwAn0
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.9（p. 169–170）：Corollary 4.9.27、Example 4.9.28；§4.10 Lecture 30（p. 171–172）：Definition 4.10.1–4.10.2、Theorem 4.10.3–4.10.4、Corollary 4.10.5–4.10.6、Example 4.10.7（開頭）
---

# 第 44 集 · 代數擴張、擴張的次數、塔定理（Algebraic Extensions and Degree, Part 1） [▶ 影片](https://youtu.be/nOfJamAwAn0)

← 上一集：[43-irreducible-polynomial-simple-extensions-2](43-irreducible-polynomial-simple-extensions-2.md) ｜ [總目錄](README.md) ｜ 下一集：[45-algebraic-extensions-degree-2](45-algebraic-extensions-degree-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 44 集（2021-11-17 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，whisper 轉錄；23:21 附近有一段轉錄重複的亂碼；結尾被切斷）＋ 講者講義 §4.9–4.10
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 推論：1, α, …, αⁿ⁻¹ 是基底](#1-推論1-α--αⁿ⁻¹-是基底)
- [2. 代數擴張](#2-代數擴張)
- [3. 擴張的次數 [E : F]](#3-擴張的次數-e--f)
- [4. 有限擴張 ⇒ 代數擴張](#4-有限擴張--代數擴張)
- [5. 塔定理：[K : F] = [K : E][E : F]](#5-塔定理k--f--k--ee--f)
- [6. 推論：多層塔、deg(β, F) | deg(α, F)](#6-推論多層塔degβ-f--degα-f)
- [7. 例子：x³ − 2 在 Q(√2) 裡沒有根（開頭）](#7-例子x--2-在-q2-裡沒有根開頭)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/nOfJamAwAn0?t=0)

重述 Theorem 4.9.26（第 42–43 集），然後進入講義 **Lecture 30：代數擴張**（照 Fraleigh 第 31 節）。

講者 [▶ 05:35](https://youtu.be/nOfJamAwAn0?t=335)：「我們到了**我講義的最後一講**。之後要換成一份 PDF，像我們看過的那種短文。」（第 46–47 集。）

---

## 1. 推論：1, α, …, αⁿ⁻¹ 是基底

[▶ 00:00](https://youtu.be/nOfJamAwAn0?t=0)

**重述**（Theorem 4.9.26）：$E = F(\alpha)$，$\alpha$ 在 $F$ 上代數，$\deg(\alpha,F) = n\ge1$，則每個 $\beta\in E$ 唯一地寫成 $b_0+b_1\alpha+\cdots+b_{n-1}\alpha^{n-1}$。

> **推論**（講義 Corollary 4.9.27）[▶ 01:29](https://youtu.be/nOfJamAwAn0?t=89)：$\{1,\alpha,\dots,\alpha^{n-1}\}$ 是 $E$ 作為 $F$ 上向量空間的基底，$E = \mathrm{span}_F\{1,\alpha,\dots,\alpha^{n-1}\}$。

不只是生成集，還線性獨立。**基底 = 線性獨立的生成集。**

【口頭】[▶ 02:43](https://youtu.be/nOfJamAwAn0?t=163) 講者：「這是線性代數該學會並記住的事，但我說大部分學生都忘了。如果數學系調查畢業生，發現只有 5% 知道基底是線性獨立的生成集，你會難過——但你會有很多同伴。」「不用就會忘。真正學會線性代數的方法是在其他課用它。好消息是，依 **Raoul Bott** 的說法，高等數學 80% 是線性代數。所以你繼續做數學，就躲不掉線性代數。」

**例**（Ex 4.9.28）[▶ 03:56](https://youtu.be/nOfJamAwAn0?t=236)：$\mathbb{C} = \mathbb{R}(i)$，元素 $a+bi$。$\mathrm{irr}(i,\mathbb{R}) = x^2+1$（以 $i$ 為根、次數最小的首一多項式），所以 $\deg(i,\mathbb{R}) = 2$，$\{1,i\}$ 是 $\mathbb{C}$ 作為 2 維實向量空間的基底——「複數平面是 2 維實向量空間」。

【Q&A】學生問首一的意思：**首項係數是 1**。講者：「我們喜歡分解首一多項式。我在線性代數裡專攻首一分解，因為分解有 2、3、6 的東西讓我毫無喜悅，留給其他老師。」

---

## 2. 代數擴張

[▶ 06:10](https://youtu.be/nOfJamAwAn0?t=370)

> **定義**（講義 Definition 4.10.1）：若 $E$ 的**每個**元素在 $F$ 上都是代數的，就說 $E$ 是 $F$ 的**代數擴張**（algebraic extension）。否則叫**超越擴張**（transcendental extension）。

【課堂討論】[▶ 07:43](https://youtu.be/nOfJamAwAn0?t=463) 講者問「每個元素在 $F$ 上代數」是什麼意思，學生不確定。回顧：$\alpha$ 在 $F$ 上代數 ⇔ 存在 $p(x)\in F[x]$（非零）使 $p(\alpha) = 0$。

講者：**跟之前的差別**是現在講整個擴張體，**不同元素可能需要不同的多項式**。之前專注在一個元素和它的多項式；現在是每個元素都要有。

**例：$\mathbb{C}$ 是 $\mathbb{R}$ 的代數擴張** [▶ 08:56](https://youtu.be/nOfJamAwAn0?t=536)：取 $\alpha = a+ib$。

- $b = 0$：$p(x) = x-a$，$p(\alpha) = 0$。其實這就是不可約多項式，次數 1（$\alpha$ 是實數）。
- $b\neq0$ [▶ 10:03](https://youtu.be/nOfJamAwAn0?t=603)：$p(x) = (x-a)^2+b^2$。
  $$p(a+ib) = (ib)^2+b^2 = -b^2+b^2 = 0.$$
  展開是 $x^2-2ax+a^2+b^2$，實係數。（而且在 $\mathbb{R}$ 上不可約，所以就是 $a+ib$ 的首一最小多項式。）

每個複數都是某個實多項式的根，所以 $\mathbb{C}$ 是 $\mathbb{R}$ 的代數擴張。

---

## 3. 擴張的次數 [E : F]

[▶ 12:26](https://youtu.be/nOfJamAwAn0?t=746)（講者懶得寫整個定義，「講義 p. 171 的 Definition 4.10.2，自己讀」）

> **定義**（講義 Definition 4.10.2）：若擴張體 $E$ 作為 $F$ 上的向量空間是有限維 $n$，就說 $E$ 是 $F$ 的**有限擴張**，**次數** $n$，記作
> $$[E:F] = n.$$

**例**：$[\mathbb{C}:\mathbb{R}] = 2$。

【課堂討論】[▶ 14:13](https://youtu.be/nOfJamAwAn0?t=853) 「你們會問：為什麼不像線性代數那樣說維度是 2？我不知道。我們喜歡發明新記號來搞混學生。」這個記號在**群論**裡意思不同：$H\le G$，$[G:H]$ = **陪集的個數**。

【口頭】講者岔題：$H$ 是正規子群時商群有定義，商群的階 = 陪集數。例如 $\mathbb{Z}_{20}$ 模 $\{0,5,10,15\}$（4 個元素），切成 5 個陪集，同構於 $\mathbb{Z}_5$。「這對 mission 5 的 $\mathbb{Z}_{48}$ 那題會有幫助。」

**$[F:F] = 1$** [▶ 17:26](https://youtu.be/nOfJamAwAn0?t=1046)（「很蠢的例子」）：$\{1\}$ 是基底——$c = c\cdot1$，而單一個非零向量線性獨立。**任何體在自己上面都是 1 維**。

> 【講義補充】講義（p. 171）也證了反方向：$[E:F] = 1$ ⇒ $E = F$。因為 $1\in F$，$\{1\}$ 就是基底，$E = \mathrm{span}(1) = F$。

---

## 4. 有限擴張 ⇒ 代數擴張

[▶ 19:08](https://youtu.be/nOfJamAwAn0?t=1148)

> **定理**（講義 Theorem 4.10.3）：$F$ 的有限擴張 $E$ 一定是代數擴張。

**證明**：

1. 設 $[E:F] = n$，任取 $\alpha\in E$。
2. 考慮 $\{1,\alpha,\alpha^2,\dots,\alpha^n\}$：$n+1$ 個向量 [▶ 22:15](https://youtu.be/nOfJamAwAn0?t=1335)。
3. **線性代數**：$n$ 維空間裡超過 $n$ 個向量一定線性相依。（「三維空間給我四個向量，一定有線性相依；平面上不可能有三個線性獨立的向量。」）
4. 所以存在**不全為 0** 的 $c_0,\dots,c_n\in F$：
   $$c_0+c_1\alpha+\cdots+c_n\alpha^n = 0.$$
5. $p(x) = c_0+c_1x+\cdots+c_nx^n\in F[x]$ 是**非零**多項式，$p(\alpha) = 0$。$\alpha$ 是代數的。
6. $\alpha$ 是任意的，所以 $E$ 是代數擴張。∎

講者 [▶ 24:02](https://youtu.be/nOfJamAwAn0?t=1442)：「驚人地簡單。讀的時候看起來很難證——要替擴張體的**任意**元素給出一個多項式。但**線性代數幫我們做完了所有事**。」重要的是係數不全為 0，因為要**非零**多項式。不同元素可以用不同多項式。

（⚠️ 23:21 附近字幕是 whisper 重複輸出的 "dot dot dot"，內容依講義 Theorem 4.10.3 補。）

（課中有學生進來拿補考的東西，說隔天要早走去參加牛仔競技。）

---

## 5. 塔定理：[K : F] = [K : E][E : F]

[▶ 25:33](https://youtu.be/nOfJamAwAn0?t=1533)

講者：「這是這部分材料裡**我最喜歡的定理之一**。部分因為它是線性代數，部分因為它也是代數，兩個都有。而且是使用求和記號的藉口，我承認我很愛。」

> **定理**（講義 Theorem 4.10.4）：若 $E$ 是 $F$ 的有限擴張，$K$ 是 $E$ 的有限擴張，則 $K$ 是 $F$ 的有限擴張，而且
> $$[K:F] = [K:E]\,[E:F].$$

⚠️ 講義原文寫「$K$ is a finite extension field of a field **$F$**」，講者 [▶ 27:25](https://youtu.be/nOfJamAwAn0?t=1645) 說「我想定理有打字錯誤」，應是「$K$ 是 **$E$** 的有限擴張」。新的結論是「$K$ 是 $F$ 的有限擴張」並且公式成立——要先知道 $K$ 是 $F$ 的有限擴張，才能談 $[K:F]$。

**證明**：設 $[E:F] = n$、$[K:E] = m$（「m 像 mummy」）。要給出 $K$ 在 $F$ 上的基底。

1. $\{\alpha_1,\dots,\alpha_n\}$ 是 $E$ 在 $F$ 上的基底；$\{\beta_1,\dots,\beta_m\}$ 是 $K$ 在 $E$ 上的基底 [▶ 30:11](https://youtu.be/nOfJamAwAn0?t=1811)。（「over $F$ 還是 over $E$ 很重要，它說明用哪種係數組合。」）
2. **生成** [▶ 32:05](https://youtu.be/nOfJamAwAn0?t=1925)：任取 $x\in K$，
   $$x = \sum_{j=1}^mc_j\beta_j,\qquad c_j\in E.$$
   每個 $c_j\in E = \mathrm{span}_F\{\alpha_i\}$：
   $$c_j = \sum_{i=1}^nb_{ij}\alpha_i,\qquad b_{ij}\in F.$$
   代進去 [▶ 35:18](https://youtu.be/nOfJamAwAn0?t=2118)：
   $$x = \sum_{j=1}^m\sum_{i=1}^nb_{ij}\,\alpha_i\beta_j.$$
   所以 $S = \{\alpha_i\beta_j : 1\le i\le n,\ 1\le j\le m\}$ 在 $F$ 上生成 $K$。
3. **數 $S$ 有幾個** [▶ 37:39](https://youtu.be/nOfJamAwAn0?t=2259)【課堂討論】：$\alpha_1\beta_1,\dots,\alpha_1\beta_m$（$m$ 個）、$\alpha_2\beta_1,\dots,\alpha_2\beta_m$（$m$ 個）……共 $n$ 組，**$mn$ 個**。
   講者：目前只知道維度最多 $mn$；若 $S$ 線性獨立，就恰好是 $mn = [K:E][E:F]$。
4. **線性獨立** [▶ 40:33](https://youtu.be/nOfJamAwAn0?t=2433)：設 $\sum_j\sum_ic_{ij}\alpha_i\beta_j = 0$（$c_{ij}\in F$）。用分配律重寫：
   $$\sum_{j=1}^m\left(\sum_{i=1}^nc_{ij}\alpha_i\right)\beta_j = 0.$$
   括號裡是 $\alpha$ 的 $F$ 組合，在 $E$ 裡。所以這是 $\beta$ 的 $E$ 組合 [▶ 42:36](https://youtu.be/nOfJamAwAn0?t=2556)。
   - **$\beta$ 線性獨立**（在 $E$ 上）⇒ 每個 $\sum_ic_{ij}\alpha_i = 0$。
   - **$\alpha$ 線性獨立**（在 $F$ 上）⇒ 所有 $c_{ij} = 0$。
5. $S$ 是基底，$[K:F] = mn$。∎

（講者說要嚴格定義基底 $S$ 應該規定順序，「我沒有計較順序」。）

---

## 6. 推論：多層塔、deg(β, F) | deg(α, F)

> **推論**（講義 Corollary 4.10.5）[▶ 45:03](https://youtu.be/nOfJamAwAn0?t=2703)：$F_{i+1}$ 是 $F_i$ 的有限擴張（$i = 1,\dots,r-1$），則 $F_r$ 是 $F_1$ 的有限擴張，
> $$[F_r:F_1] = [F_r:F_{r-1}][F_{r-1}:F_{r-2}]\cdots[F_2:F_1].$$

「能做兩次就能做 $n$ 次。」講者畫體塔：$F_1\subseteq F_2\subseteq\cdots\subseteq F_r$，每層次數 $n_1,n_2,\dots,n_{r-1}$，**乘起來**就是頂層對底層的次數。「別擔心，有例子，等一下就沒那麼抽象了。」

> **推論**（講義 Corollary 4.10.6）[▶ 48:22](https://youtu.be/nOfJamAwAn0?t=2902)：$E$ 是 $F$ 的擴張，$\alpha\in E$ 在 $F$ 上代數，$\beta\in F(\alpha)$。則
> $$\deg(\beta,F)\ \Big|\ \deg(\alpha,F).$$

**證明** [▶ 49:52](https://youtu.be/nOfJamAwAn0?t=2992)：體塔 $F\subseteq F(\beta)\subseteq F(\alpha)$。塔定理：
$$[F(\alpha):F] = [F(\alpha):F(\beta)]\,[F(\beta):F].$$
$[F(\alpha):F] = \deg(\alpha,F)$、$[F(\beta):F] = \deg(\beta,F)$，所以 $\deg(\beta,F)$ 整除 $\deg(\alpha,F)$。∎

**講者卡住的一步** [▶ 51:47](https://youtu.be/nOfJamAwAn0?t=3107)：為什麼 $[F(\alpha):F] = n$ 就代表 $\deg(\alpha,F) = n$（有一個 $n$ 次不可約多項式以 $\alpha$ 為根）？講者：「我想我把它搞複雜了……我不確定我完全證過。」他把它留成「好的作業題」（不是正式指派）：

> 給定體 $F$，$[F(\alpha):F] = n$，能解釋為什麼 $\deg(\alpha,F) = n$ 嗎？

【口頭】[▶ 54:45](https://youtu.be/nOfJamAwAn0?t=3285) 「我承認現在有什麼東西從我腦中溜過，我對內部邏輯不是 100% 確定。我知道它是對的——99.9%，像得了 COVID 的存活率那樣確定；但現在大家都認識某個死於 COVID 的長輩，所以也不能這樣說。」

> 以下**不是逐字稿內容**，是依第 43 集的結果補的：這正是講義 **Corollary 4.9.27**。設 $\deg(\alpha,F) = d$（$\alpha$ 代數，因為 $F(\alpha)$ 是有限擴張，用第 4 節）。第 43 集證過 $\{1,\alpha,\dots,\alpha^{d-1}\}$ 是 $F(\alpha)$ 的基底，所以 $[F(\alpha):F] = d$。若 $[F(\alpha):F] = n$，維度唯一，$d = n$。

> 【講義補充】講義（p. 172）：這個推論在**尺規作圖**的研究裡很重要。可作圖的數來自一連串 2 次擴張；若某個數需要 3 次擴張，$2\nmid3$……（講義原文寫「$2\nmid3$ forbids」，意思是 3 不整除 2 的冪）就不能作圖，例如用尺規**三等分角**。

---

## 7. 例子：x³ − 2 在 Q(√2) 裡沒有根（開頭）

[▶ 55:52](https://youtu.be/nOfJamAwAn0?t=3352)（講義 Example 4.10.7，課堂叫例 4）

講者：「我漏了一個大字，無視我自己的蠢講義——這裡有個超大的『**假設**』。」

**假設** $\mathbb{Q}(\sqrt2)$ 裡有 $p(x) = x^3-2$ 的根 $\beta$。

1. $x^3-2$ 在 $\mathbb{Q}$ 上不可約：Eisenstein，$p = 2$（$2\mid-2$，$4\nmid-2$）[▶ 57:06](https://youtu.be/nOfJamAwAn0?t=3426)。
2. 所以 $\deg(\beta,\mathbb{Q}) = 3$（$\beta$ 是 3 次不可約多項式的根）。
3. 若 $\beta\in\mathbb{Q}(\sqrt2)$：體塔 $\mathbb{Q}\subseteq\mathbb{Q}(\beta)\subseteq\mathbb{Q}(\sqrt2)$ [▶ 58:11](https://youtu.be/nOfJamAwAn0?t=3491)。
4. $[\mathbb{Q}(\sqrt2):\mathbb{Q}] = 2$（$\mathrm{irr}(\sqrt2,\mathbb{Q}) = x^2-2$）。
5. 塔定理：$[\mathbb{Q}(\sqrt2):\mathbb{Q}] = [\mathbb{Q}(\sqrt2):\mathbb{Q}(\beta)]\cdot[\mathbb{Q}(\beta):\mathbb{Q}]$……（影片在這裡被切斷，接第 45 集。）

---

## 8. 一頁速查表

**基底**：$\{1,\alpha,\dots,\alpha^{n-1}\}$ 是 $F(\alpha)$ 的基底，$[F(\alpha):F] = \deg(\alpha,F)$。基底 = 線性獨立的生成集。

**代數擴張**：每個元素都代數（可以用不同多項式）。例：$\mathbb{C}/\mathbb{R}$，$a+ib$ 是 $(x-a)^2+b^2$ 的根。

**次數** $[E:F] = \dim_FE$。$[F:F] = 1$；$[E:F] = 1\Leftrightarrow E = F$。（群論的 $[G:H]$ 是陪集數。）

| 定理 | 關鍵一步 |
|---|---|
| 有限 ⇒ 代數 | $1,\alpha,\dots,\alpha^n$ 是 $n+1$ 個向量 ⇒ 線性相依 ⇒ 非零多項式 |
| $[K:F] = [K:E][E:F]$ | 基底 $\{\alpha_i\beta_j\}$；獨立性先用 $\beta$ 再用 $\alpha$ |
| 多層塔 | 次數相乘 |
| $\deg(\beta,F)\mid\deg(\alpha,F)$（$\beta\in F(\alpha)$） | $F\subseteq F(\beta)\subseteq F(\alpha)$ 用塔定理 |

**應用**：$x^3-2$ 在 $\mathbb{Q}(\sqrt2)$ 裡沒有根，因為 $3\nmid2$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $x^3-2$ 在 $\mathbb{Q}(\sqrt2)$ 上不可約；$\mathbb{Q}(\sqrt2,\sqrt[3]2) = \mathbb{Q}(\sqrt[6]2)$ | 第 45 集 |
| 本原元素定理；$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3)$ | 第 45 集 |
| 尺規作圖、Galois 理論 | 本課沒講 |

---

## 附：本集一句話總結

> **$F(\alpha)$ 的維度就是 $\alpha$ 的次數。每個元素都是代數的擴張叫代數擴張（例如 $\mathbb{C}/\mathbb{R}$），而有限維的擴張一定是代數的，因為 $1,\alpha,\dots,\alpha^n$ 太多、必然線性相依。擴張的次數在體塔裡相乘：$[K:F] = [K:E][E:F]$，基底就是兩組基底兩兩相乘；所以 $F(\alpha)$ 裡元素的次數一定整除 $\alpha$ 的次數——$\mathbb{Q}(\sqrt2)$ 裝不下 3 次的 $\sqrt[3]2$。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-17 第 1 部錄影逐字稿（whisper 轉錄，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.9–4.10 整理。*
