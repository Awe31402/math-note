---
course: Number Theory（2021 秋，線上錄影）
episode: 18
lecture: 2021-10-04 第 2 部
date: 2021-10-04
video: https://youtu.be/tQJiKBEiUpM
notes: 講者照 Keith Conrad〈The Gaussian Integers〉§6（Definition 6.2、Theorem 6.3–6.4）；Jones & Jones《Elementary Number Theory》§10.2 不可約元素、q ≡ 3 mod 4 在 Z[i] 不可約（書頁 198，PDF 頁 213）
---

# 第 18 集 · 高斯質數、分解成質數的乘積（Euclidean Algorithm, Factoring Gaussian Integers, Composite vs. Prime, Part 2） [▶ 影片](https://youtu.be/tQJiKBEiUpM)

← 上一集：[17-gaussian-euclid-factoring-1](17-gaussian-euclid-factoring-1.md) ｜ [總目錄](README.md) ｜ 下一集：[19-gaussian-primes-applications-1](19-gaussian-primes-applications-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 18 集（2021-10-04 第 2 部，接第 17 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（19:35，whisper 轉錄）＋ Jones & Jones《Elementary Number Theory》§10.2
> **注意**：這部的 whisper 轉錄品質很差，像是被轉成別的語言再翻回英文（例如把「nontrivial factorization」寫成「irrational factorization」、把「9 is 3 squared」寫成「9 is the 3rd category」）。數學內容依上下文和 Conrad 講義的結構重建，時間點可信，個別用字不可信。
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 三種高斯整數：單位、質數、合數](#1-三種高斯整數單位質數合數)
- [2. 例子：7 + i 是合數](#2-例子7--i-是合數)
- [3. 3 在 Z[i] 裡還是質數，13 不是](#3-3-在-zi-裡還是質數13-不是)
- [4. 範數是質數 ⇒ 是高斯質數](#4-範數是質數--是高斯質數)
- [5. 每個非單位都是高斯質數的乘積](#5-每個非單位都是高斯質數的乘積)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

接第 17 集最後的「合數」定義，定義**高斯質數**，證明每個非單位都能寫成高斯質數的乘積（**存在性**）。**唯一性**留到下一集。

【口頭】[▶ 06:26](https://youtu.be/tQJiKBEiUpM?t=386) 講者：「我有個錯覺以為今天能講完，因為我是白痴。我寄信給你們時就知道要兩天。」

| 主題 | 時間 | Conrad 編號 |
|---|---|---|
| 質數的定義 | 00:02 | Definition 6.2 |
| $7+i$ 是合數 | 00:33 | — |
| 3 是高斯質數、13 不是 | 01:36 | — |
| 範數是質數 ⇒ 高斯質數 | 06:26 | Theorem 6.3 |
| 分解成質數的乘積 | 12:28 | Theorem 6.4 |

---

## 1. 三種高斯整數：單位、質數、合數

[▶ 00:02](https://youtu.be/tQJiKBEiUpM?t=2)

接第 17 集的 Definition 6.2：$\alpha\in\mathbb{Z}[i]$，$N(\alpha)>1$。

- 若 $\alpha$ 有**非平凡分解**（$\alpha = \beta\gamma$，$N(\beta),N(\gamma)>1$），叫**合數**（composite）。
- **否則**，叫 **質數**（prime，又叫**高斯質數** Gaussian prime）。

所以高斯整數（非零的）分成三類 [▶ 00:33](https://youtu.be/tQJiKBEiUpM?t=33)：

| 類別 | 條件 |
|---|---|
| 單位 | $N(\alpha) = 1$：$\pm1,\pm i$ |
| 質數 | $N(\alpha)>1$，只有平凡因數 |
| 合數 | $N(\alpha)>1$，有非平凡因數 |

⚠️ 逐字稿缺字：字幕把「nontrivial factorization」寫成「irrational factorization」「unscientific factor division」。依 Conrad 講義和第 17 集的定義修正。

---

## 2. 例子：7 + i 是合數

[▶ 00:33](https://youtu.be/tQJiKBEiUpM?t=33)

$$7+i = (1-2i)(1+3i).$$

驗算 [▶ 01:03](https://youtu.be/tQJiKBEiUpM?t=63)：$(1-2i)(1+3i) = 1+3i-2i-6i^2 = 7+i$。✓

$N(1-2i) = 5>1$、$N(1+3i) = 10>1$，所以這是非平凡分解，**$7+i$ 是合數**。

（範數檢查：$N(7+i) = 50 = 5\cdot 10$。）

---

## 3. 3 在 Z[i] 裡還是質數，13 不是

[▶ 01:36](https://youtu.be/tQJiKBEiUpM?t=96)

講者：3 在整數裡是質數，但在高斯整數裡還是質數嗎？「這是不同的問題，因為你有更多選擇。」

**先看一個反例：13** [▶ 02:12](https://youtu.be/tQJiKBEiUpM?t=132)

$13 = 4+9 = 2^2+3^2$，所以
$$13 = (2+3i)(2-3i).$$
兩個因數範數都是 13，非平凡。所以 **13 在整數裡是質數，在高斯整數裡是合數**。

講者 [▶ 02:44](https://youtu.be/tQJiKBEiUpM?t=164)：

- 整數的質數**大多數**在高斯整數裡還是質數。（以下**不是逐字稿內容**：其實奇質數裡 $4n+1$ 型和 $4n+3$ 型各佔一半左右，「大多數」不精確。講者想說的應該是「很多質數保持質數」。）
- 而且剛才發生的事是**唯一可能的情況**：整數的質數在 $\mathbb{Z}[i]$ 裡**要嘛還是質數，要嘛分裂成一對共軛**，像 $13 = (2+3i)(2-3i)$。

**證明 3 是高斯質數**（反證）[▶ 03:17](https://youtu.be/tQJiKBEiUpM?t=197)

1. 假設 3 是合數：$3 = \alpha\beta$，$N(\alpha),N(\beta)>1$。
2. 取範數：$9 = N(\alpha)N(\beta)$。
3. $9 = 3^2$，由整數的唯一分解，又兩個範數都 $>1$，只能 $N(\alpha) = N(\beta) = 3$。
4. 寫 $\alpha = a+bi$：$a^2+b^2 = 3$ [▶ 04:47](https://youtu.be/tQJiKBEiUpM?t=287)。

【課堂討論】講者要大家試著解 $a^2+b^2 = 3$。學生試：$1^2+2^2 = 5$；$1^2+1^2 = 2$；$0^2+1^2 = 1$。「永遠得不到 3。」（正負號不影響。）

5. 沒有整數解，矛盾。所以 **3 是高斯質數**。∎

（這也可以用第 13 集：$3\equiv 3\ (\mathrm{mod}\ 4)$，所以不是兩平方和。）

> 【課本補充】§10.2（p. 198）證明了一般的情況：**每個質數 $q\equiv 3\ (\mathrm{mod}\ 4)$ 在 $\mathbb{Z}[i]$ 裡都不可約。** 若 $q = zw$，則 $d(z)d(w) = q^2$，所以 $d(z)=d(w)=q$ 或 $\{d(z),d(w)\} = \{1,q^2\}$。前者給出 $q = x^2+y^2$，但 $q\equiv 3\ (\mathrm{mod}\ 4)$ 不可能是兩平方和；所以只能是後者，$z$ 或 $w$ 是單位。例如 $3,7,11,19,\dots$ 都是高斯質數，每個有四個相伴元 $\pm q,\pm qi$。

---

## 4. 範數是質數 ⇒ 是高斯質數

[▶ 06:26](https://youtu.be/tQJiKBEiUpM?t=386)

> **定理**（Conrad 6.3）：若 $N(\alpha)$ 是**整數裡的質數**，則 $\alpha$ 是 $\mathbb{Z}[i]$ 裡的質數。

講者：「定理 6.3 會幫你解很多作業題。」

**證明** [▶ 07:33](https://youtu.be/tQJiKBEiUpM?t=453)：設 $N(\alpha)$ 是質數，$\alpha = \beta\gamma$。目標：$\beta$ 或 $\gamma$ 是單位。

1. 取範數：$N(\alpha) = N(\beta)N(\gamma)$。
2. 兩個整數乘起來是質數，**其中一個一定是 1**。
3. 所以 $N(\beta)=1$ 或 $N(\gamma)=1$，$\beta$ 或 $\gamma$ 是單位。
4. $\alpha$ 沒有非平凡因數，是質數。∎

**例子**：$N(1-2i) = 5$、$N(2+3i) = 13$ 都是質數，所以 $1-2i$、$2+3i$ 都是高斯質數。

**逆命題不成立** [▶ 10:23](https://youtu.be/tQJiKBEiUpM?t=623)：高斯質數的範數**不一定**是質數。

【課堂討論】講者問：如果是高斯質數，它的範數一定是質數嗎？答案是不一定。

| $\alpha$ | $N(\alpha)$ | $N(\alpha)$ 是質數？ | $\alpha$ 是高斯質數？ |
|---|---|---|---|
| $3$ | $9$ | ❌ | ✅（第 3 節） |
| $13$ | $169$ | ❌ | ❌（$=(2+3i)(2-3i)$） |

所以 $3$ 就是反例：高斯質數，範數 9 卻不是質數。

講者順便說 [▶ 11:56](https://youtu.be/tQJiKBEiUpM?t=716)：**整數的合數在高斯整數裡還是合數**（例如 $9 = 3\cdot 3$）。

---

## 5. 每個非單位都是高斯質數的乘積

[▶ 12:28](https://youtu.be/tQJiKBEiUpM?t=748)

> **定理**（Conrad 6.4）：每個 $N(\alpha)>1$ 的高斯整數（也就是非零、非單位的）都是 $\mathbb{Z}[i]$ 裡**質數的乘積**。

**證明：對範數做（強）歸納法** [▶ 13:23](https://youtu.be/tQJiKBEiUpM?t=803)

**基礎情況**：$N(\alpha) = 2$。（範數 1 是單位，不算，所以從 2 開始。）

- $a^2+b^2 = 2$ 的解是 $\alpha = \pm1\pm i$。
- 也可以用第 15 集：範數是偶數 ⇔ 是 $1+i$ 的倍數。
- 範數 2 是質數，由定理 6.3，這些都是高斯質數。一個質數本身就是「質數的乘積」。✓

**歸納步驟** [▶ 15:27](https://youtu.be/tQJiKBEiUpM?t=927)：設 $n\ge 3$，而且**所有**範數在 $1$ 和 $n$ 之間（不含）的高斯整數都是質數的乘積。設 $N(\gamma) = n$。

- **$\gamma$ 是質數**：做完了。
- **$\gamma$ 是合數** [▶ 17:00](https://youtu.be/tQJiKBEiUpM?t=1020)：$\gamma = \beta\delta$，$N(\beta),N(\delta)>1$。
  - 由乘性 $N(\beta)N(\delta) = n$，兩個都 $>1$，所以 $N(\beta)<n$、$N(\delta)<n$。
  - 由歸納假設 [▶ 18:02](https://youtu.be/tQJiKBEiUpM?t=1082)：$\beta = \pi_1\cdots\pi_r$、$\delta = \pi_{r+1}\cdots\pi_{r+s}$（$\pi_j$ 都是高斯質數）。
  - 所以 $\gamma = \pi_1\cdots\pi_{r+s}$，是質數的乘積。∎

【口頭】[▶ 18:34](https://youtu.be/tQJiKBEiUpM?t=1114) 「這裡所有難的證明，通常都是**對範數做歸納**。範數是整數，所以可以對它歸納。」（跟第 5 集整數的算術基本定理存在性證明一模一樣，只是把「大小」換成「範數」。）

**下一步**：Lemma 6.5（「非常關鍵」），然後是**唯一分解**。講者說解釋細節沒辦法快，「我快到一個很好的停點了，得停了」。

---

## 6. 一頁速查表

**三類**：單位（$N=1$）、高斯質數（$N>1$，只有平凡因數）、合數（有非平凡因數）。

**例子**

| 數 | 結論 | 理由 |
|---|---|---|
| $7+i$ | 合數 | $=(1-2i)(1+3i)$ |
| $13$ | 合數 | $=(2+3i)(2-3i)$ |
| $3$ | 高斯質數 | $a^2+b^2=3$ 無解 |
| $1\pm i$、$1-2i$、$2+3i$ | 高斯質數 | 範數 2、5、13 是質數 |

**整數質數在 $\mathbb{Z}[i]$**：保持質數，或分裂成一對共軛 $(a+bi)(a-bi)$。$q\equiv3\ (\mathrm{mod}\ 4)$ 一定保持質數（課本）。

**定理 6.3**：$N(\alpha)$ 是質數 ⇒ $\alpha$ 是高斯質數。**關鍵一步**：$N(\beta)N(\gamma)$ = 質數 ⇒ 其中一個是 1。逆不成立（$3$）。

**定理 6.4**：非單位 ⇒ 高斯質數的乘積。**關鍵一步**：對範數強歸納；合數 $\gamma=\beta\delta$ 的兩個因數範數都比較小。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Lemma 6.5（高斯質數整除乘積 ⇒ 整除其一）、唯一分解 | 第 19 集 |
| 哪些整數質數會分裂（$p=2$、$p\equiv1$、$p\equiv3$ mod 4） | 第 19–21 集 |
| $p\equiv1\ (\mathrm{mod}\ 4)$ ⇒ $p=a^2+b^2$ | 第 19–21 集 |
| 對範數歸納的證明方法 | 第 22 集起 |
| 質元素 vs 不可約元素的一般區分 | 第 36–39 集 |

---

## 附：本集一句話總結

> **非零高斯整數分成單位、高斯質數、合數三類。整數的質數到了 $\mathbb{Z}[i]$ 可能保持質數（像 3），也可能分裂成共軛對（像 $13=(2+3i)(2-3i)$）；範數是質數的一定是高斯質數。對範數做歸納，就證出每個非單位都是高斯質數的乘積。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-04 第 2 部錄影逐字稿（whisper 轉錄，19:35；轉錄品質差）與 Jones & Jones《Elementary Number Theory》§10.2 整理；講者的主要參考是 Keith Conrad〈The Gaussian Integers〉。*
