---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 13
lecture: Lec13 3.3 Variable-Length Code for Lossless Data Comp. 3.3.1 Non-singular Codes …
date: 待補
video: https://youtu.be/SwS8qXXFakY
notes: Alajaji & Chen §3.3.1–3.3.2（pp. 76–86，Definition 3.19–Observation 3.29）
---

# 第 13 集 · Lec13 §3.3.1–3.3.2：變長碼、uniquely decodable、Kraft 不等式、prefix code [▶ 影片](https://youtu.be/SwS8qXXFakY)

← 上一集：[12](12-lossless-data-compression-principles-aep.md) ｜ [總目錄](README.md) ｜ 下一集：[14](14-binary-prefix-codes-huffman-shannon-fano-elias.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 13 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（52:09，whisper large-v3-turbo）＋ 課本 §3.3.1–3.3.2（pp. 76–86）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「不定長度」聽成「不定常度」，「typical set」聽成「typical say」，「non-singular」聽成「non-singer／non-sino」，「comma／逗號」聽成「鬥號／dough」，「Kraft」聽成「Craft／Crab」，「McMillan」聽成「Macmillan／McVillian／猛運」，「Massey」聽成「Maisie／Macy」，「prefix」聽成「previous／previce／previctical／prefist」，「suffix」聽成「suffic／suffice」，「平均碼長」聽成「平均碼糖／平均馬長」，「floor function」聽成「flower function」，「Fano」聽成「Phenol」，「Elias」聽成「Alias」，「D-ary」聽成「deary／theory」。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 變長碼也要抓到 Shannon 的精神](#1-變長碼也要抓到-shannon-的精神)
- [2. Non-singular vs uniquely decodable](#2-non-singular-vs-uniquely-decodable)
- [3. 變長碼的定義：codebook 列的是 codeword](#3-變長碼的定義codebook-列的是-codeword)
- [4. Kraft–McMillan 不等式](#4-kraftmcmillan-不等式)
- [5. 平均碼率不低於 entropy](#5-平均碼率不低於-entropy)
- [6. Prefix code（instantaneous code）](#6-prefix-codeinstantaneous-code)
- [7. Prefix code 與樹](#7-prefix-code-與樹)
- [8. Kraft 不等式 ⟺ 存在 prefix code](#8-kraft-不等式--存在-prefix-code)
- [9. 可以任意逼近 entropy](#9-可以任意逼近-entropy)
- [10. 例子：一次編 1 個 vs 2 個](#10-例子一次編-1-個-vs-2-個)
- [11. 變長碼的 source coding theorem](#11-變長碼的-source-coding-theorem)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

實際用的壓縮碼都是**變長碼**，而且**完全無損**。這一集證明：
1. 能**無限串接、不用標點**的碼（uniquely decodable）一定滿足 **Kraft 不等式**，所以平均碼率 ≥ entropy；
2. 滿足 Kraft 的碼長一定能做成 **prefix code**（一棵樹的樹葉）；
3. 碼長取 $\lceil\log\frac1p\rceil$ 左右，平均碼率 ≤ $H+\frac1n$，可以任意逼近 entropy。

| 主題 | 課本 |
|---|---|
| VLC、non-singular、uniquely decodable | Definition 3.19–3.20（pp. 76–77） |
| Kraft（McMillan）不等式 | Theorem 3.21（pp. 78–79） |
| 平均碼率 ≥ entropy | Theorem 3.22、Exercise 3.23（pp. 79–80） |
| Prefix code、樹、Kraft ⟺ prefix | Definition 3.24、Fig. 3.4–3.5、Theorem 3.25（pp. 80–83） |
| $\le H+\frac1n$、例子、定理 | Theorem 3.27–3.28、Observation 3.29（pp. 83–86） |

---

## 1. 變長碼也要抓到 Shannon 的精神

[▶ 00:00](https://youtu.be/SwS8qXXFakY?t=0)

- 變長碼表面上看不出 typical set 的行為：它要 **completely lossless**，錯誤率 **exactly 0**，不能是漸近 0，所以不能像 block code 那樣「外面 $\delta$ 的機率不要了」。
- 但好的壓縮碼還是要抓到 Shannon 的精神：**碼長要正比於 $\log\frac1{P_X(x)}$**——就是 self-information，三個公設下唯一的函數。
- 直覺 [▶ 09:47](https://youtu.be/SwS8qXXFakY?t=587)：typical set 裡機率大的、大家一樣重要，碼長都要短；外面總機率只有 $\delta$，碼長可以拉很長（反正乘上很小的機率），但一定要不一樣、還要能串接。

---

## 2. Non-singular vs uniquely decodable

[▶ 01:31](https://youtu.be/SwS8qXXFakY?t=91)

**例子**（課本 p. 77）：$\{A,B,C,D,E,F\}$ 編成 A→0、B→1、C→00、D→01、E→10、F→11。
- 每個 codeword 都不同，**用一次**解壓縮沒問題（看到 00 就是 C）。這叫 **non-singular**（one-shot）。
- 但**不能串接**：壓縮 AB 得 01，解壓縮會解成 D。課本的例子：010 可以是 ABA、DA 或 AE。
- 加逗號分隔可以解決，但**逗號也要佔儲存空間**——總量算下來還是不能低於 entropy。

**Uniquely decodable**（課本 p. 76）：任何有限串 codeword **不加標點**（concatenation **without punctuation**）串起來，都能唯一解回原來的 sourceword 序列。
- 例：$\{0,10,11\}$。串成 1011011011……，每個人解的都一樣：看到 1 不是 codeword，再看下一個，10 是 B；11 是 C；0 是 A……可以**無限串接**。
- 【口頭】Shannon 講的是**長期使用**（大數法則）：買了東西要能連續用 10 萬次。有些東西是用一次就丟（one-shot），那就只要 non-singular。
- 【口頭】當然要約定起始點；實際通訊在有雜訊環境下，一錯就 error propagation 錯一大串，所以一段時間還是要同步一次。

**Shannon 會證明**：uniquely decodable 且無損時，最小平均壓縮率就是 entropy。non-singular 碼只用一次，平均碼長可以低於 entropy，但它不能串接——不能說「我找到比 entropy 更好的方法」。

---

## 3. 變長碼的定義：codebook 列的是 codeword

[▶ 06:06](https://youtu.be/SwS8qXXFakY?t=366)

**Definition 3.19**（p. 76）：有限字母 $\mathcal X$，$D$-ary 碼字母 $\mathcal B=\{0,\dots,D-1\}$。$D$-ary **$n$ 階變長碼（VLC）** 是函數
$$f:\mathcal X^n\to\mathcal B^*,$$
$\mathcal B^*$ 是所有有限長度字串。每 $n$ 個 source symbol 編一次，編出來的長度不一定。

**和 block code 的差別**（【口頭】）：
- Block code 的 codebook 列的是 **sourceword**（分析靠 source 分布定義 typical set；sourceword 都一樣長）。
- VLC 的 codebook 列的是 **codeword** $\mathcal C=f(\mathcal X^n)$（例如 001、01110、1101），因為要算的是**平均碼長**；錯誤率永遠是 0，不用討論。

**Definition 3.20**（p. 77）：codeword $c_{x^n}=f(x^n)$ 的長度 $\ell(c_{x^n})$。
$$\bar\ell:=\sum_{x^n}P_{X^n}(x^n)\,\ell(c_{x^n}),\qquad\bar R_n:=\frac{\bar\ell}n\quad(D\text{-ary code symbols / source symbol}).$$
例：長度 3、5、4 的 codeword，機率 $\frac14,\frac12,\frac14$，平均碼長 $\frac14\cdot3+\frac12\cdot5+\frac14\cdot4$。除以 $n$ 是每個 source symbol 平均幾個 bit，和 block code 的 rate 是同一個定義。

---

## 4. Kraft–McMillan 不等式

[▶ 10:47](https://youtu.be/SwS8qXXFakY?t=647)

【口頭】Kraft 和 McMillan 在不同時期、針對不同對象獨立做出一樣的結果。Cover 之前的書都叫 Kraft inequality；其實 **Kraft 證的是 prefix code**，**McMillan 證的是 uniquely decodable code**，所以也叫 Kraft–McMillan theorem。課本照慣例叫 Kraft inequality（p. 78 註 17 提到 McMillan）。

**Theorem 3.21（Kraft inequality for uniquely decodable codes）**（p. 78）：$\mathcal C$ 是 uniquely decodable 的 $D$-ary $n$ 階 VLC，$M=|\mathcal X|^n$ 個 codeword 長度 $\ell_1,\dots,\ell_M$，則
$$\sum_{m=1}^MD^{-\ell_m}\le1.$$

**直覺**（【口頭】）[▶ 11:49](https://youtu.be/SwS8qXXFakY?t=709)：機率 $\frac12$ 對碼長 1、$\frac14$ 對碼長 2、$\frac18$ 對碼長 3——二分再二分，就是一棵樹，$2^{-\ell}$ 就像機率。機率總和是 1，所以 $\sum2^{-\ell_m}\le1$。

【口頭】Massey（瑞士聯邦理工學院，已過世）有一份上課講義（網路上找得到，沒出書），用不同的角度（樹）介紹這個。他聽演講常坐第一排閉眼睡覺，講完就舉手發問；論文很少，但每篇都經典。

**證明**（McMillan，課本 pp. 78–79）[▶ 13:51](https://youtu.be/SwS8qXXFakY?t=831)：
- 串接 $N$ 個 codeword $c_1c_2\cdots c_N$。考慮這個 **identity**：
$$\left(\sum_{c\in\mathcal C}D^{-\ell(c)}\right)^N=\sum_{c_1\in\mathcal C}\sum_{c_2\in\mathcal C}\cdots\sum_{c_N\in\mathcal C}D^{-[\ell(c_1)+\ell(c_2)+\cdots+\ell(c_N)]}.$$
  （左邊乘開：summation 範圍都一樣，可以對調、相乘、變成 $N$ 次方。）
  - 【口頭】它其實在做機率總和：$D^{-\ell}$ 就像那個 codeword 的機率，相乘就像獨立事件的機率相乘。碼長已經反映了機率，所以這裡不用另外看機率。
- 按總長度 $i=\ell(c_1)+\cdots+\ell(c_N)$ 分組：令 $A_i$ = 總長度為 $i$ 的 $N$ 個 codeword 串的個數，$L=\max_c\ell(c)$。
$$\left(\sum_{m=1}^MD^{-\ell_m}\right)^N=\sum_{i=1}^{LN}A_iD^{-i}.$$
- **關鍵**：uniquely decodable ⇒ 總長 $i$ 的 code 串最多只有 $D^i$ 種不同的 0/1 組合，每一種最多對應一種解法（否則就像 01 可以解成 D 或 AB）。所以 $A_i\le D^i$：
$$\left(\sum_mD^{-\ell_m}\right)^N\le\sum_{i=1}^{LN}D^iD^{-i}=LN\ \Rightarrow\ \sum_mD^{-\ell_m}\le(LN)^{1/N}.$$
- 對**所有** $N$ 都成立（無限串接），$(LN)^{1/N}\to1$（$N\to\infty$），得證。∎

【口頭】整個證明完全沒用到編碼的結構，只用到「能串接、能唯一解回來」。所以**任何** uniquely decodable code，不管好壞，都滿足它。

---

## 5. 平均碼率不低於 entropy

[▶ 22:03](https://youtu.be/SwS8qXXFakY?t=1323)

**Theorem 3.22**（p. 79）：DMS 的任何 uniquely decodable $D$-ary $n$ 階 VLC，平均碼率 $\bar R_n\ge H_D(X)$。

**證明**（口訣：相減、合併 log、log-sum）：
$$\begin{aligned}
\bar R_n-H_D(X)&=\frac1n\sum_{x^n}P_{X^n}(x^n)\ell(c_{x^n})-\frac1nH_D(X^n)
=\frac1n\sum_{x^n}P_{X^n}(x^n)\log_D\frac{P_{X^n}(x^n)}{D^{-\ell(c_{x^n})}}\\
&\ge\frac1n\left(\sum_{x^n}P_{X^n}(x^n)\right)\log_D\frac{\sum_{x^n}P_{X^n}(x^n)}{\sum_{x^n}D^{-\ell(c_{x^n})}}
=-\frac1n\log_D\left(\sum_{x^n}D^{-\ell(c_{x^n})}\right)\ge0.
\end{aligned}$$
- 第一行：$\ell=\log_DD^{\ell}$，和 $-\log_DP$ 合併。DMS 時 $\frac1nH_D(X^n)=H_D(X)$。
- 不等號：log-sum（用 FI 也一樣）。最後一步用 Kraft（$\sum D^{-\ell}\le1$ ⇒ $-\log\ge0$）。

**觀察**（【口頭】）：證明真正的癥結只有 Kraft 不等式。甚至 entropy rate 存不存在都沒用到——只要 Kraft 成立，壓縮極限就對了（就像 block code 那邊只要 typical set 對了）。

【課本補充】(p. 80) $\bar R_n=H_D(X)$ iff $P_{X^n}(x^n)=D^{-\ell(c_{x^n})}$——機率都是 $D$ 的負整數次方，叫 **$D$-adic** source，此時碼叫 absolutely optimal。

**Exercise 3.23**（p. 80）：
1. 找一個 non-singular 但非 uniquely decodable、違反 Kraft 的碼：就是第 2 節的例子，$2^{-1}+2^{-1}+4\cdot2^{-2}=2>1$。
2. 找一個 non-singular、非 uniquely decodable、平均碼長比 entropy 還低的碼：同一個碼隨便給個機率常常就低於 entropy——但它只能用一次。

---

## 6. Prefix code（instantaneous code）

[▶ 28:12](https://youtu.be/SwS8qXXFakY?t=1692)

Converse 證完了（任何碼都 ≥ entropy）；forward 只要找到**一種**設計能任意逼近 entropy——就是 **prefix code**。

**Definition 3.24**（p. 80）：**沒有任何 codeword 是另一個 codeword 的 prefix（前置）**，叫 prefix code 或 **instantaneous code**（也叫 prefix-free code）。

- 反例：$\{0,01,10\}$——0 是 01 的前置，不符合 prefix condition。
- 為什麼重要（【口頭】）：有人是我的前置，解到一半就 ambiguous——看到 0，不知道是 0 這個 codeword，還是 01 的開頭。
- **Instantaneous**：沒有人是我的前置，解碼不需要 buffer，**看到就能立即決定**。例：$\{0,10,11\}$，看到 0 立刻輸出 A；看到 1 知道還沒完，再看一個就決定 B 或 C。

【口頭】老師有篇論文做「雙向 prefix code」：沒人是我的 prefix，也沒人是我的 suffix（後置），可以雙向解碼加快速度（記憶體有時需要）。條件越嚴，設計越難。

**關係**（Fig. 3.4，p. 81）：prefix codes ⊂ uniquely decodable codes ⊂ non-singular codes。
- 例：$\{0,01,11\}$ 是 uniquely decodable 但不是 prefix code——它是 suffix code（沒有 codeword 是別人的後置），倒過來讀就是 prefix code $\{0,10,11\}$，所以能串接解碼。

> ⚠️ 逐字稿缺字：[▶ 33:47](https://youtu.be/SwS8qXXFakY?t=2027) 原字幕「0 0 1 1 1 1 這個也是 uniquely decodable」，依「它事實上是 suffix code，倒過來就好」推測為 $\{0,01,11\}$。
- 【口頭】現在大概 80% 實用的碼都是 prefix code。

---

## 7. Prefix code 與樹

[▶ 32:15](https://youtu.be/SwS8qXXFakY?t=1935)

**Prefix code 都可以畫成一棵樹，所有 codeword 都在樹葉（leaves）上**，沒有 codeword 是枝幹（內部節點）。
- 理由：選了某個節點當 codeword，它後面（子孫）都不能再是 codeword。
- 解碼的便利：心中想像一棵 binary tree，沿著樹走，走到樹葉就輸出那個 source symbol。

【課本補充】Fig. 3.5（p. 81）的例子：codeword 00、01、10、110、1110、1111 都在樹葉上。

---

## 8. Kraft 不等式 ⟺ 存在 prefix code

[▶ 34:49](https://youtu.be/SwS8qXXFakY?t=2089)

**Theorem 3.25（Kraft inequality for prefix codes）**（p. 81）：存在一個 $D$-ary $n$ 階 prefix code、碼長為 $\ell_1,\dots,\ell_M$ ⟺ 這些碼長滿足 Kraft 不等式。

**推論的重要性**（【口頭】）：
- uniquely decodable ⇒ Kraft 成立 ⇒ 存在**同樣碼長**的 prefix code ⇒ 平均碼長一樣。
- 所以全世界最好的設計若平均碼長是 3.2 bit，一定有一個 prefix code 也是 3.2。**最好的設計可能很多，但 prefix code 一定是其中之一**——就像 Neyman–Pearson 說 likelihood ratio test 一定是最好的之一。而 prefix code 有樹狀結構、操作方便，所以好的碼幾乎都是 prefix code。

**證明**（$D=2$）：

**(⇒) Prefix code 滿足 Kraft**（Kraft 原本的證明）：令 $\ell_{\max}=\max_m\ell_m$，第 $\ell_{\max}$ 層原本有 $2^{\ell_{\max}}$ 個節點。長度 $\ell_m$ 的 codeword 會擋掉它下面第 $\ell_{\max}$ 層的 $2^{\ell_{\max}-\ell_m}$ 個節點，而且兩個 codeword 不會擋到同一個節點。所以
$$\sum_{m=1}^M2^{\ell_{\max}-\ell_m}\le2^{\ell_{\max}}\ \Rightarrow\ \sum_m2^{-\ell_m}\le1.$$
（例：$\ell_{\max}=3$，長度 1 的 codeword 擋掉 4 個、長度 2 的擋掉 2 個……）也可以直接說：prefix code 是 uniquely decodable，所以由 McMillan 成立；這個證明是為了展示樹的特性。

**(⇐) Kraft ⇒ 存在 prefix code**：令 $n_i$ = 長度為 $i$ 的 codeword 個數。Kraft 寫成
$$n_12^{-1}\le1,\quad n_12^{-1}+n_22^{-2}\le1,\quad\dots,\quad\sum_{i=1}^{\ell_{\max}}n_i2^{-i}\le1.$$
由短到長依序在樹上選樹葉：第 1 層有 2 個節點，選 $n_1$ 個（$n_1\le2$）；第 2 層 4 個節點扣掉被擋掉的 $2n_1$ 個，剩下的 $\ge n_2$（由第二個不等式乘 4）……每一層都夠選，所以一定做得出來。
- 例：碼長 1、2、3：$\frac12+\frac14+\frac18=\frac78\le1$。選 0；再選 10；再選 110。剩下一個 $\frac18$ 沒用。

**等號** [▶ 41:58](https://youtu.be/SwS8qXXFakY?t=2518)：樹是**滿的**（所有樹葉都用完）時 Kraft 等號成立；有樹葉沒用到就是嚴格不等式（上例少一個 $2^{-3}$）。

---

## 9. 可以任意逼近 entropy

[▶ 43:02](https://youtu.be/SwS8qXXFakY?t=2582)

**Theorem 3.27**（p. 83）：DMS。
1. 任何 $D$-ary $n$ 階 prefix code 的平均碼率 ≥ $H_D(X)$。（prefix ⇒ UD ⇒ Theorem 3.22。）
2. 存在一個 $D$-ary $n$ 階 prefix code，
$$\bar R_n\le H_D(X)+\frac1n.$$

**證明（第 2 部分）**：取碼長（老師稱這個設計為 Shannon–Fano code）
$$\ell(c_{x^n})=\left\lfloor-\log_DP_{X^n}(x^n)\right\rfloor+1.$$
- **滿足 Kraft**：$\ell\ge-\log_DP$ ⇒ $D^{-\ell}\le P_{X^n}(x^n)$，加總 $\sum D^{-\ell}\le1$。所以存在這樣碼長的 prefix code。【口頭】就是把機率轉成樹。
- **平均碼長**：$\ell\le-\log_DP+1$，乘機率加總：
$$\sum_{x^n}P_{X^n}(x^n)\ell(c_{x^n})\le H_D(X^n)+1=nH_D(X)+1.$$
  除以 $n$ 即得。∎

**意義**（【口頭】）：
- $\frac1n\to0$，所以可以任意逼近壓縮極限。
- 代價是**複雜度**：$n=300$ 個英文字母一組，buffer 的可能性是 $26^{300}$。學生做專題，大概 $n=20$ 電腦就受不了。所以有人質疑這個定理沒有實作意義；但理論的意義是 guideline：**絕對存在方法能無限逼近**，所以 entropy 的確是壓縮極限。
- 後來的變形（Shannon code、Shannon–Fano code、Shannon–Fano–Elias code）都要抓同一個重點：**碼長正比於 $\log\frac1p$**。

---

## 10. 例子：一次編 1 個 vs 2 個

[▶ 47:39](https://youtu.be/SwS8qXXFakY?t=2859)

（課本 pp. 84–85）DMS $\{A,B,C\}$，$P_X(A)=0.8$、$P_X(B)=P_X(C)=0.1$。
$$H(X)=-0.8\log_20.8-2\cdot0.1\log_20.1\approx0.92\text{ bits}.$$

**$n=1$**：A→0、B→10、C→11（prefix code）。
$$\bar R_1=0.8\cdot1+0.2\cdot2=1.2\ \text{bits}\ \ge0.92,\quad\text{也}\le0.92+1.$$

**$n=2$**：9 個 pair，機率 $P(x_1)P(x_2)$：AA 0.64；AB、AC、BA、CA 各 0.08；BB、BC、CB、CC 各 0.01。一個最佳 prefix code：
- AA→0；AB→100、AC→101、BA→110、CA→1110；
- BB→111100、BC→111101、CB→111110、CC→111111。
$$\bar R_2=\frac{0.64\cdot1+0.08(3\cdot3+4\cdot1)+0.01(6\cdot4)}2=\frac{0.64+1.04+0.24}2=0.96\text{ bits}\le0.92+\tfrac12.$$

【口頭】1.2 和 0.96 差很多：壓縮 1000 個 symbol，前者要 1200 bit，後者只要 960 bit；檔案通常是幾 MB，節省 20%–30%。三個三個、四個四個壓會更省，但再怎麼好也不可能少於 $1000\times0.92=920$ bit。

---

## 11. 變長碼的 source coding theorem

[▶ 50:42](https://youtu.be/SwS8qXXFakY?t=3042)

**Theorem 3.28（Shannon's lossless variable-length source coding theorem：DMS）**（p. 85）：
- **Forward**：對任意 $\varepsilon>0$，$n$ 夠大時存在 $D$-ary $n$ 階 **prefix**（故 uniquely decodable）code，$\bar R_n<H_D(X)+\varepsilon$。（取 $\frac1n<\varepsilon$。）
- **Converse**：任何 uniquely decodable code 都有 $\bar R_n\ge H_D(X)$。（Kraft。）

**Observation 3.29**（p. 86）：對 stationary source 也成立，把 $H_D(X)$ 換成 entropy rate $\lim\frac1nH_D(X^n)$（用 $\frac1nH(X^n)$ 對 $n$ 非遞增）。

**Block code vs 變長碼**（【口頭】）：stationary ergodic（或 i.i.d.）source 下兩者壓縮極限都是 entropy。第二部分會看到：**non-stationary source 時兩者極限不同**——變長碼壓得比 block code 好，而且變長碼還是沒有錯誤率，block code 還有。

---

## 12. 一頁速查表

**名詞**
- Non-singular：codeword 都不同（只用一次 OK）。例 $\{0,1,00,01,10,11\}$：010 = ABA = DA = AE。
- Uniquely decodable：任意串接、不加標點都唯一可解。
- Prefix（instantaneous）：沒有 codeword 是別人的前置；樹葉；立即解碼。
- Prefix ⊂ UD ⊂ non-singular。

**Kraft–McMillan**：UD ⇒ $\sum_mD^{-\ell_m}\le1$。
- 關鍵：$\left(\sum D^{-\ell}\right)^N=\sum_iA_iD^{-i}$，UD ⇒ $A_i\le D^i$ ⇒ $\le LN$ ⇒ $\sum D^{-\ell}\le(LN)^{1/N}\to1$。

**Converse（Thm 3.22）**：$\bar R_n-H=\frac1n\sum P\log\frac P{D^{-\ell}}\ge-\frac1n\log\sum D^{-\ell}\ge0$（log-sum + Kraft）。等號 iff $D$-adic。

**Kraft ⟺ prefix（Thm 3.25）**：(⇒) 每個 codeword 擋掉 $2^{\ell_{\max}-\ell_m}$ 個最底層節點；(⇐) 由短到長選樹葉，每層都夠。滿樹 ⟺ 等號。

**Achievability（Thm 3.27）**：$\ell=\lfloor-\log_DP\rfloor+1$ ⇒ $D^{-\ell}\le P$（Kraft）且 $\bar\ell\le nH+1$ ⇒ $\bar R_n\le H+\frac1n$。

**例**：$(0.8,0.1,0.1)$，$H=0.92$；$n=1$：$\{0,10,11\}$，1.2；$n=2$：0.96。

**定理（Thm 3.28）**：UD 碼 $\bar R_n\ge H$；prefix 碼可達 $<H+\varepsilon$。Stationary source 用 entropy rate。

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 最佳 prefix code：Huffman | 第 14 集（§3.3.3） |
| Shannon–Fano–Elias、arithmetic code | 第 14 集 |
| 碼長 $\log\frac1p$、誤用分布的代價 $D(P\|Q)$ | 第 10 集回顧、第 14–15 集 |
| Lempel–Ziv（不知道分布也能逼近 entropy rate） | 第 15 集（§3.3.4） |
| 指數成本、Rényi entropy（Observation 3.30、Theorem 3.31） | 第 2 集預告、第 14–15 集附近 |
| Non-stationary 時 block 和變長碼極限不同 | 第 33 集（第二部分） |

---

## 附：本集一句話總結

> **能無限串接、不加逗號的碼，碼長一定滿足 Kraft 不等式 $\sum D^{-\ell}\le1$——碼長就像機率——所以平均碼率逃不出 entropy；反過來，滿足 Kraft 的碼長一定能做成一棵樹上的 prefix code，取 $\ell\approx\log\frac1p$ 就能把平均碼率壓到 $H+\frac1n$。**

---

*筆記依據陳伯寧老師「消息理論」Lec13 錄影逐字稿（whisper large-v3-turbo，52:09）與 Alajaji & Chen 課本 §3.3.1–3.3.2 整理。*
