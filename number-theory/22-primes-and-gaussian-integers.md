---
course: Number Theory（2021 秋，線上錄影）
episode: 22
lecture: Lecture 21
date: 待補（2021 秋）
video: https://youtu.be/JkiyK4harX0
notes: Jones & Jones §10.1–10.2（書頁 191–201，PDF 頁 206–216）：Theorem 10.2–10.3、Corollary 10.4、高斯整數不可約元的分類（p. 198–199）、Example 10.3–10.4；§4.1 Theorem 4.6（書頁 71）；畢氏三元數組 §11.5（書頁 223）
---

# 第 22 集 · Lecture 21：質數與高斯整數（Primes and Gaussian Integers） [▶ 影片](https://youtu.be/JkiyK4harX0)

← 上一集：[21-sums-of-squares-gaussian-integers](21-sums-of-squares-gaussian-integers.md) ｜ [總目錄](README.md) ｜ 下一集：[23-quaternions](23-quaternions.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 22 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（26:33，**whisper 轉錄**；YouTube 字幕下載被擋）＋ Jones & Jones §10.1–10.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 高斯質數的質因數性質](#1-高斯質數的質因數性質)
- [2. 兩平方和模 4](#2-兩平方和模-4)
- [3. 複的高斯質數給出 4n+1 型質數](#3-複的高斯質數給出-4n1-型質數)
- [4. Lagrange 引理](#4-lagrange-引理)
- [5. Fermat 兩平方定理](#5-fermat-兩平方定理)
- [6. 哪些數是兩平方和](#6-哪些數是兩平方和)
- [7. 畢氏三元數組](#7-畢氏三元數組)
- [8. 結語](#8-結語)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 段落 | 內容 | 課本 |
|---|---|---|
| 1 | 高斯質數 $\omega\mid\alpha\beta\Rightarrow\omega\mid\alpha$ 或 $\omega\mid\beta$ | （§10.2 提到 Lemma 2.1 的類比） |
| 3–5 | Lagrange 引理；Fermat 兩平方定理 | Theorem 4.6、Theorem 10.2、Corollary 10.4 |
| 6 | $n$ 是兩平方和的條件；用高斯整數找表示法 | Theorem 10.3、Example 10.3–10.4 |
| 7 | 用高斯整數推出畢氏三元數組公式 | §11.5 |

---

## 1. 高斯質數的質因數性質

[▶ 00:00](https://youtu.be/JkiyK4harX0?t=0)

**定理**：$\omega$ 是高斯質數，若 $\omega\mid\alpha\beta$，則 $\omega\mid\alpha$ 或 $\omega\mid\beta$。

**證明**：設 $\omega\nmid\alpha$，要證 $\omega\mid\beta$。
1. Bézout（上一集）：存在高斯整數 $x,y$ 使 $\alpha x+\omega y = \gcd(\alpha,\omega)$。
2. 乘 $\beta$：$\alpha\beta x+\omega\beta y = \beta\gcd(\alpha,\omega)$。
3. $\omega\mid\alpha\beta$，寫 $\alpha\beta = \gamma\omega$：
$$\gcd(\alpha,\omega)\cdot\beta = \omega\,(x\gamma+y\beta).$$
4. $\omega\nmid\alpha$ 且 $\omega$ 是高斯質數，可以證明 $\gcd(\alpha,\omega)$ 是單位 $u$（講者說這是好作業題，可惜沒出）。所以
$$\beta = u^{-1}(x\gamma+y\beta)\,\omega,$$
即 $\omega\mid\beta$。∎

⚠️ 逐字稿缺字：[▶ 00:36](https://youtu.be/JkiyK4harX0?t=36) whisper 寫「it remains to show that alpha divides beta」，應為 $\omega$ 整除 $\beta$。

【口頭】這和整數的證明完全一樣，只是改用高斯整數的 Bézout。算術從整數轉到高斯整數時，很多證明都能原封不動地搬過去，例如「$a\mid b$、$a\mid c$ ⇒ $a\mid b+c$」這類整除定理 [▶ 01:55](https://youtu.be/JkiyK4harX0?t=115)。

---

## 2. 兩平方和模 4

[▶ 02:32](https://youtu.be/JkiyK4harX0?t=152)

【口頭】這件事上一集該說的。

奇數不是在 $4\mathbb{Z}+1$ 就是在 $4\mathbb{Z}+3$（$4\mathbb{Z}$、$4\mathbb{Z}+2$ 是偶數）。

平方模 4：$0^2 = 0$、$1^2 = 1$、$2^2 = 4\equiv0$、$3^2 = 9\equiv1$，只有 0 或 1。所以
$$a^2+b^2\equiv0,1,2\ (\mathrm{mod}\ 4),\quad\text{永遠不是 }3.$$
**$4n+3$ 型的數都不是兩個整數的平方和。**

【口頭】講者記得這在第 4 集附近、以及有了模運算後的某一集明確證過（第 4、11 集：平方數模 4 只有 0、1）[▶ 03:52](https://youtu.be/JkiyK4harX0?t=232)。

---

## 3. 複的高斯質數給出 4n+1 型質數

[▶ 04:26](https://youtu.be/JkiyK4harX0?t=266)

**定理**：若 $a+bi$（$a,b$ 都不為 0）是高斯質數，則 $p = a^2+b^2$ 是（自然數中的）質數。

**證明**：上一集證過 $a-bi$ 也是高斯質數，且 $(a+bi)(a-bi) = a^2+b^2 = p$。設 $p = rs$ 是非平凡分解（$r,s$ 不是單位），則
$$(a+bi)(a-bi) = rs. \tag{$*$}$$
由高斯整數的唯一分解：
- 若 $r,s$ 是高斯質數，它們要和 $a\pm bi$ 在相伴意義下配對。但 $r,s$ 是整數，而 $a\pm bi$ 乘上單位（$\pm1,\pm i$）不會變成整數——「不是同一型」。
- 若 $r,s$ 能再分解，右邊的高斯質因數就有四個以上，左邊只有兩個。

所以 $(*)$ 給出兩種不等價的分解，和唯一分解矛盾。$p$ 是質數。∎

（講者的論證比較口語。以下**不是逐字稿內容**，是更直接的寫法：若 $p = rs$，$r,s>1$ 是整數，則 $N(r)N(s) = r^2s^2 = p^2$……另一種常見寫法是：$a+bi$ 整除整數 $p$，看 $N$ 即可。）

**推論**：每個「複的」高斯質數（實部、虛部都不為 0）給出一個 $a^2+b^2$ 型的質數，由第 2 節，它一定是 $4n+1$ 型（或 2，例如 $1+i$）[▶ 06:40](https://youtu.be/JkiyK4harX0?t=400)。

---

## 4. Lagrange 引理

[▶ 06:40](https://youtu.be/JkiyK4harX0?t=400)

【口頭】這是為 Fermat 兩平方定理做準備。Fermat 敘述了定理，Lagrange 後來證明；講者對歷史不太確定（也許 Lagrange 之前就有人證過），「我就不多說了」[▶ 07:19](https://youtu.be/JkiyK4harX0?t=439)。

**引理（Lagrange）**：若質數 $p = 4n+1$，則存在整數 $m$ 使 $p\mid m^2+1$。

**證明**：用第 13 集的 **Wilson 定理**：$(p-1)!\equiv-1\ (\mathrm{mod}\ p)$。$p-1 = 4n$，所以
$$-1\equiv(4n)! = \underbrace{1\cdot2\cdots2n}_{}\cdot\underbrace{(2n+1)\cdots(4n)}_{}\ (\mathrm{mod}\ p).$$
因為 $p = 4n+1\equiv0$，後半的每個因子可以換成負數：$2n+1\equiv-2n$、$2n+2\equiv-(2n-1)$、……、$4n\equiv-1$。所以
$$-1\equiv(2n)!\cdot(-1)^{2n}(2n)! = \big((2n)!\big)^2\ (\mathrm{mod}\ p).$$
取 $m = (2n)!$：$m^2+1\equiv0$，即 $p\mid m^2+1$。∎

> 【課本補充】這就是第 13 集筆記補過的 Jones & Jones Theorem 4.6 的一半（p. 71）：$x^2\equiv-1\ (\mathrm{mod}\ p)$ 有解 $\iff p\equiv1\ (\mathrm{mod}\ 4)$，解是 $x = k!$，$k = \frac{p-1}2$。也就是第 17 集的 $\left(\frac{-1}p\right) = 1$。

---

## 5. Fermat 兩平方定理

[▶ 09:46](https://youtu.be/JkiyK4harX0?t=586)

【口頭】和許多 Fermat 的事一樣，他敘述了定理，講者印象中他聲稱用**無窮遞降**證過；嚴謹的證明留給後來的數學家。Fermat 是 1600 年代早期（1630–50 年左右）的人 [▶ 10:24](https://youtu.be/JkiyK4harX0?t=624)。

**定理（Fermat 兩平方定理）**：奇質數 $p$ 可以寫成兩個整數的平方和 $\iff p\equiv1\ (\mathrm{mod}\ 4)$。

**證明**：
- (⇐) 設 $p\equiv1\ (\mathrm{mod}\ 4)$。由 Lagrange 引理，$p\mid m^2+1 = (m+i)(m-i)$。
  - 若 $p\mid m\pm i$，則 $\frac{m\pm i}{p} = \frac mp\pm\frac1pi$ 是高斯整數，但虛部 $\frac1p$ 不是整數，矛盾。所以 $p$ 不整除 $m+i$ 也不整除 $m-i$。
  - 這表示 $p$ **不滿足**質因數性質（第 1 節），所以 $p$ **不是**高斯質數。
  - 由上一集的定理（質數 $p$ 是高斯質數 ⇔ $p$ 不是兩平方和），$p = a^2+b^2$。
- (⇒) 若 $p = a^2+b^2$，由第 2 節 $p\not\equiv3\ (\mathrm{mod}\ 4)$，奇數所以 $p\equiv1\ (\mathrm{mod}\ 4)$。∎

⚠️ 逐字稿缺字：[▶ 12:40](https://youtu.be/JkiyK4harX0?t=760) whisper 寫「if p is not a prime and p is equal to a squared plus b squared」，從上下文是「若 $p$ 是質數且 $p = a^2+b^2$」。

> 【課本補充】Theorem 10.2（p. 193）：Fermat 1640 年敘述、**Euler 1754 年證明**。課本的證明不用高斯整數：由 $-1\equiv u^2$ 得 $u^2+1^2 = rp\in S_2$；取最小的 $m$ 使 $mp\in S_2$，若 $m>1$ 則用最小絕對值剩餘和恆等式 (10.2) 造出更小的 $sp\in S_2$，矛盾（無窮遞降）。Corollary 10.4：質數 $p$ 是兩平方和 $\iff p = 2$ 或 $p\equiv1\ (\mathrm{mod}\ 4)$。

**高斯質數的完整分類**（結合上一集和本集）：
- $1+i$（及相伴元），對應 $2 = -i(1+i)^2$；
- $p\equiv3\ (\mathrm{mod}\ 4)$ 的普通質數 $p$（及相伴元 $\pm p,\pm ip$）；
- $a\pm bi$，其中 $a^2+b^2 = p\equiv1\ (\mathrm{mod}\ 4)$（及相伴元）。

（以下**不是逐字稿內容**：講者上一集說要在本集「完整分類」，本集沒有明說這三類；這是課本 p. 198–199 的結論，筆記把它和講者證過的定理對起來列出。）

---

## 6. 哪些數是兩平方和

### 6.1 定理

[▶ 12:40](https://youtu.be/JkiyK4harX0?t=760)

**定理**：整數 $n>1$ 可寫成 $a^2+b^2$（$a,b$ 整數）$\iff$ $n$ 的質因數分解中，每個 $p\equiv3\ (\mathrm{mod}\ 4)$ 的質數的次數都是**偶數**。

講者沒給證明，說把目前的東西拼起來就不難證。這回答了上一集的問題：$S_2$ 是什麼 [▶ 14:29](https://youtu.be/JkiyK4harX0?t=869)。

> 【課本補充】Theorem 10.3（p. 194）的證明：
> - (⇐) $2 = 1^2+1^2$；$p_i\equiv1\ (4)$ 是兩平方和（Theorem 10.2）；$q_j^2 = q_j^2+0^2$；$S_2$ 對乘法封閉。
> - (⇒) 設 $n = x^2+y^2$、$q\equiv3\ (4)$、$q^f\Vert n$，$f$ 奇數。令 $d = \gcd(x,y)$，$x = ad$、$y = bd$，$\gcd(a,b) = 1$，$nd^{-2} = a^2+b^2$。$f-2e$ 是奇數（$q^e\Vert d$），所以 $q\mid a^2+b^2$，$a^2\equiv-b^2$；$b$ 是模 $q$ 的單位，乘 $b^{-2}$ 得 $-1$ 是模 $q$ 的平方剩餘，和 $q\equiv3\ (4)$ 矛盾。
>
> 課本還算出表示法的個數 $r(n) = 4\prod(e_i+1)$（$p_i\equiv1\ (4)$ 的次數 $e_i$），當所有 $q_j$ 的次數都是偶數時。

### 6.2 例子

[▶ 13:50](https://youtu.be/JkiyK4harX0?t=830)

- **15** $= 3\cdot5$：$5 = 1^2+2^2$ 可以，但 3 的次數是 1（奇數），沒辦法把 3 塞進去。**15 不在 $S_2$。**
- **45** $= 3^2\cdot5$：3 的次數是偶數。把 3 分配到兩邊：$45 = 9(1^2+2^2) = (3\cdot1)^2+(3\cdot2)^2 = 3^2+6^2 = 9+36$。✓
- **30** $= 2\cdot3\cdot5$：3 只有一個，**不行**。

**更大的例子**：$1845 = 9\cdot5\cdot41$ [▶ 15:34](https://youtu.be/JkiyK4harX0?t=934)

【口頭】與其直接把 5 和 41 寫成平方和，不如寫成**高斯整數的因數**，再組合，比較好玩 [▶ 16:11](https://youtu.be/JkiyK4harX0?t=971)。

- $5 = (1+2i)(1-2i)$、$41 = (5+4i)(5-4i)$。
- **配法一**：$(1+2i)(5+4i) = -3+14i$，它的共軛是另外兩個的乘積：
$$5\cdot41 = (-3+14i)(-3-14i) = 3^2+14^2,$$
$$1845 = 9(3^2+14^2) = 9^2+42^2.$$
（「你以前知道嗎？我在準備這堂課之前不知道。」）
- **配法二** [▶ 17:36](https://youtu.be/JkiyK4harX0?t=1056)：$(1-2i)(5+4i) = 5+4i-10i+8 = 13-6i$，
$$1845 = 9(13^2+6^2) = 39^2+18^2.$$
（講者手邊沒有計算機，「只能希望我沒算錯」；筆記驗證：$81+1764 = 1521+324 = 1845$。）

**技巧** [▶ 18:52](https://youtu.be/JkiyK4harX0?t=1132)：從每個 $4n+1$ 型質因數的兩個共軛高斯質因數中**各挑一個**（不要從同一個數挑兩個），乘起來得到 $z$，則 $n$（的那部分）$= z\bar z = N(z)$。不同的挑法給出不同的表示法。作業有一題要找不同的寫法，這就是提示。

⚠️ 逐字稿缺字：[▶ 15:34](https://youtu.be/JkiyK4harX0?t=934) whisper 寫「9 times 2 plus i times 2 minus i」（把 5 寫成 $(2+i)(2-i)$），接著卻用 $1+2i$ 計算。兩者是相伴的（$1+2i = i(2-i)$），不影響結果。

> 【課本補充】Example 10.4（p. 195）：$221 = 13\cdot17$，$13 = 3^2+2^2$、$17 = 4^2+1^2$，$221 = 10^2+11^2$，換另一個恆等式得 $14^2+5^2$。Example 10.3：$60$ 不是兩平方和；$180 = 2^2\cdot3^2\cdot5 = 12^2+6^2$。

---

## 7. 畢氏三元數組

[▶ 19:32](https://youtu.be/JkiyK4harX0?t=1172)

【口頭】「我們之前好像談過畢氏三元數組（第 1 集），我的記憶又不行了。」本集暗號是「ace of clubs」[▶ 20:12](https://youtu.be/JkiyK4harX0?t=1212)。

**畢氏三元數組**：非零整數 $x,y,z$ 滿足 $x^2+y^2 = z^2$。

**推導**：
1. $z^2 = x^2+y^2 = (x+iy)(x-iy)$。
2. 假設 $x,y,z$ 已約到最簡（三者若有公因數，例如 3，先除掉）。可以證明 $x,y$ 互質時，$x+iy$ 和 $x-iy$ 在 $\mathbb{Z}[i]$ 互質（講者說是好作業題，也是更好的考題）。
3. 兩個互質的數乘積是平方（$z^2$），由唯一分解，每個都是平方（差單位）。所以 $x+iy$ 是高斯整數的平方：
$$x+iy = (u+iv)^2 = (u^2-v^2) + i\,2uv.$$
4. 比較實部、虛部：
$$x = u^2-v^2,\qquad y = 2uv.$$
5. $z^2 = x^2+y^2 = (u^2-v^2)^2+4u^2v^2 = u^4+2u^2v^2+v^4 = (u^2+v^2)^2$，取正的：
$$z = u^2+v^2.$$

（「交叉項 $-2u^2v^2$ 加上 $+4u^2v^2$，淨得 $+2u^2v^2$。」「把皺眉轉過來」——取正根 [▶ 22:33](https://youtu.be/JkiyK4harX0?t=1353)。）

這正是生成畢氏三元數組的著名公式，而這裡是**從高斯整數推導出來的**。

【口頭】講者翻 Stillwell《Elements of Number Theory》第 1 章：約西元前 300 年 Euclid 證明所有自然數解可由 $(u^2-v^2)w$、$2uvw$、$(u^2+v^2)w$ 產生（$u,v,w$ 跑遍自然數）；Diophantus 約西元 250–280 年用有理數解出。「我保證，有了高斯整數的魔法，我們做得比他們輕鬆多了。」[▶ 23:39](https://youtu.be/JkiyK4harX0?t=1419)

**例**：$u = 10$、$v = 7$：
$$x = 100-49 = 51,\quad y = 140,\quad z = 149;\qquad 51^2+140^2 = 149^2.$$

⚠️ 步驟 3 嚴格說要處理單位：$x+iy = \varepsilon(u+iv)^2$，$\varepsilon\in\{\pm1,\pm i\}$；乘 $\pm i$ 會讓 $x,y$ 互換角色。講者說他在這裡犧牲了不少嚴謹性（包括沒證高斯整數的除法演算法），以前證過，但本課不想陷入技術細節 [▶ 24:46](https://youtu.be/JkiyK4harX0?t=1486)。

> 【課本補充】Jones & Jones §11.5（p. 223，「本原畢氏三元數組的分類」）會在費馬最後定理那章給出完整分類；第 1 集筆記已補過 §11.3 的定義（本原 = 任兩個互質）。

---

## 8. 結語

[▶ 24:46](https://youtu.be/JkiyK4harX0?t=1486)

【口頭】
- 高斯整數用來分析 $x^2+y^2$ 這類問題。若要分析 $a^2+2b^2$、$a^2+3b^2$ 等「帶權重的平方和」，就改用像 $\mathbb{Z}[i\sqrt3]$ 這樣的數系；下一集之後的 Fermat 最後定理會再談 [▶ 25:19](https://youtu.be/JkiyK4harX0?t=1519)。
- 高斯整數是非常好的代數系統，是任何抽象代數課的絕佳例子；對數論來說，它不費多少力氣就回答了很多自然的問題。

---

## 9. 一頁速查表

**質因數性質**：高斯質數 $\omega\mid\alpha\beta\Rightarrow\omega\mid\alpha$ 或 $\omega\mid\beta$。關鍵：Bézout，$\gcd(\alpha,\omega)$ 是單位。

**模 4**：$a^2+b^2\not\equiv3\ (\mathrm{mod}\ 4)$。

**Lagrange 引理**：$p = 4n+1$ ⇒ $p\mid\big((2n)!\big)^2+1$。關鍵：Wilson，$(4n)!\equiv(-1)^{2n}\big((2n)!\big)^2$。

**Fermat 兩平方定理**：奇質數 $p = a^2+b^2\iff p\equiv1\ (\mathrm{mod}\ 4)$。
- 關鍵：$p\mid(m+i)(m-i)$ 但不整除任一個 ⇒ $p$ 不是高斯質數 ⇒ $p = a^2+b^2$。

**高斯質數**：$1+i$；$p\equiv3\ (4)$；$a\pm bi$（$a^2+b^2 = p\equiv1\ (4)$）；以及它們的相伴元。

**$n\in S_2$** $\iff$ 每個 $p\equiv3\ (4)$ 的次數是偶數。
- $15,30\notin S_2$；$45 = 3^2+6^2$；$1845 = 9^2+42^2 = 39^2+18^2$。
- 找表示法：每對共軛高斯質因數各挑一個，乘積 $z$，$n = N(z)$。

**畢氏三元數組**：$x+iy = (u+iv)^2$ ⇒ $(x,y,z) = (u^2-v^2,\ 2uv,\ u^2+v^2)$。$(10,7)\to(51,140,149)$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 平方和、範數的乘法性 | 第 23 集（四元數：四平方和） |
| 畢氏三元數組的分類 | 第 24 集（Fermat 最後定理：$n = 2$ 有無窮多解、$n = 4$ 無解） |
| 其他數系 $\mathbb{Z}[i\sqrt3]$、唯一分解 | 第 24 集（Kummer、分圓整數） |

---

## 附：本集一句話總結

> **高斯質數也有「整除乘積必整除其一」的性質；由 Wilson 定理，$p=4n+1$ 時 $p\mid m^2+1=(m+i)(m-i)$ 卻不整除任一因數，所以 $p$ 在 $\mathbb{Z}[i]$ 中分解成 $(a+bi)(a-bi)$，即 $p=a^2+b^2$（Fermat 兩平方定理）；同樣的想法給出哪些數是兩平方和、怎麼找出表示法，以及畢氏三元數組公式 $(u^2-v^2,2uv,u^2+v^2)$。**

---

## ⚠️ 待確認清單

1. 本集逐字稿是 whisper（large-v3-turbo）轉錄，不是 YouTube 字幕；時間點可能和影片差 1–2 秒。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 21 錄影的 whisper 逐字稿（26:33）與 Jones & Jones《Elementary Number Theory》§4.1、§10.1–10.2、§11.5 整理。*
