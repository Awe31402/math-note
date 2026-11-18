---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 13
lecture: Lecture 13
date: 2023-02-13
video: https://youtu.be/J_vsyczvSdc （part 1）、https://youtu.be/N9zbir7C1kY （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.4–2.5（書頁 48–52，PDF 頁 67–71）；預告 §2.6–2.7
---

# 第 13 集 · 可積函數的絕對值、可積函數的級數 [▶ 影片](https://youtu.be/J_vsyczvSdc)

← 上一集：[12-lebesgue-integrable-functions](12-lebesgue-integrable-functions.md) ｜ [總目錄](README.md) ｜ 下一集：[14-convergence-ae-vs-norm](14-convergence-ae-vs-norm.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 13 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 33:26 whisper 轉錄，時間點可能差 1–2 秒；part 2 22:11 自動字幕）＋ Debnath & Mikusiński §2.4–2.5
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 可積函數的絕對值](#1-可積函數的絕對值)
- [2. min、max 也可積](#2-minmax-也可積)
- [3. |f| 可積不代表 f 可積；平移的連續性](#3-f-可積不代表-f-可積平移的連續性)
- [4. 用可積函數展開](#4-用可積函數展開)
- [5. Theorem 2.5.3：展開成可積函數級數不會得到新東西](#5-theorem-253展開成可積函數級數不會得到新東西)
- [6. Corollary 2.5.4：由級數造函數](#6-corollary-254由級數造函數)
- [7. 預告：L¹ 範數、零函數、零集](#7-預告l¹-範數零函數零集)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $f\in L^1\Rightarrow|f|\in L^1$ | Theorem 2.4.1，pp. 48–49 |
| $\min,\max$ 可積 | Corollary 2.4.2，p. 49 |
| 平移的連續性 | Theorem 2.4.3，p. 50 |
| 用可積函數展開 | Definition 2.5.1、Lemma 2.5.2，pp. 50–52 |
| 可積函數級數的和可積 | Theorem 2.5.3、Corollary 2.5.4，p. 52 |

開場閒聊：講者說如果他兒子以後開店用麥克筆，他要把店裡的筆全換成香味筆。錄影改成 HD。[▶ 00:00](https://youtu.be/J_vsyczvSdc?t=0)

---

## 1. 可積函數的絕對值

[▶ 00:33](https://youtu.be/J_vsyczvSdc?t=33) 課本 Theorem 2.4.1。

**定理**：若 $f\in L^1(\mathbb{R})$ 且 $f\simeq f_1+f_2+\cdots$，則 $|f|\in L^1(\mathbb{R})$，而且

$$\left|\int f\right|\le\int|f|\le\sum_{n=1}^\infty\int|f_n|.$$

講者跳過證明，說跟之前的類似，用了「偷偷加 0」的技巧。他提醒：這一節的 $Z$ 意思跟上一節**相反**——上一節 $Z$ 是級數發散的點，這裡 $Z$ 是**收斂**的點。[▶ 02:12](https://youtu.be/J_vsyczvSdc?t=132)

【課本補充】證明概要：

1. 令 $Z=\{x:\sum|f_n(x)|<\infty\}$，部分和 $s_n=f_1+\cdots+f_n$。在 $Z$ 上 $f=\lim s_n$，所以 $|f|=\lim|s_n|$，即伸縮和
   $$|f(x)|=|s_1(x)|+\big(|s_2(x)|-|s_1(x)|\big)+\cdots,\qquad x\in Z.$$
2. 令 $g_1=|s_1|$，$g_n=|s_n|-|s_{n-1}|$。由反向三角不等式
   $$|g_n|=\big||s_n|-|s_{n-1}|\big|\le|s_n-s_{n-1}|=|f_n|, \tag{2.12}$$
   所以 $\sum\int|g_n|<\infty$。
3. 問題：在 $Z$ 外可能 $\sum|g_n(x)|$ 收斂，那些點不保證 $\sum g_n(x)=|f(x)|$。解法：**加減 $f_n$** 讓那些點發散：
   $$|f|\simeq g_1+f_1-f_1+g_2+f_2-f_2+\cdots. \tag{2.13}$$
   在 $Z$ 上不影響收斂；在 $Z$ 外 $\sum|f_n|$ 發散，所以這個級數也發散，條件 (b) 不用檢查。這就是「偷偷加 0」。
4. 積分：$\int|f|=\sum\int g_n\le\sum\int|g_n|\le\sum\int|f_n|$。$\left|\int f\right|\le\int|f|$ 由 $\pm f\le|f|$ 和單調性。

【課本補充】課本這節開頭的提醒（p. 48）：Riemann 可積函數都 Lebesgue 可積（Riemann 可積的定義要求函數在有界區間外為 0），但**瑕積分**不是。例如 $\int_{-\infty}^\infty\frac{\sin x}{x}dx$ 作為瑕積分收斂，但由這個定理，$\frac{\sin x}{x}$ 不是 Lebesgue 可積的（否則 $\left|\frac{\sin x}{x}\right|$ 也可積，但它的積分是無窮大）。

---

## 2. min、max 也可積

[▶ 02:45](https://youtu.be/J_vsyczvSdc?t=165) 課本 Corollary 2.4.2。

**推論**：$f,g\in L^1(\mathbb{R})$ ⟹ $\min\{f,g\},\max\{f,g\}\in L^1(\mathbb{R})$。

講者說他以前不知道 min、max 有公式。【口頭】他以前有個學生叫 Min Win，一直想讓他跟一個叫 Max Loss 的學生合寫論文。

$$\min\{f,g\}=\tfrac12\big(f+g-|f-g|\big),\qquad\max\{f,g\}=\tfrac12\big(f+g+|f-g|\big).$$

**逐點驗證**[▶ 04:24](https://youtu.be/J_vsyczvSdc?t=264)：

- 若 $f(x)>g(x)$：$|f-g|=f-g$，所以 $\frac12(f+g-(f-g))=\frac12\cdot2g=g$ ✓。
- 若 $f(x)<g(x)$：$|f-g|=-(f-g)$，所以 $\frac12(f+g+(f-g))=f$ ✓。

講者沒看書猜出 max 的公式：把減號換成加號，促成相反的抵消。

**證明**【課堂討論】[▶ 08:13](https://youtu.be/J_vsyczvSdc?t=493)：講者想證 $\int|f-g|$ 存在，開始擔心要重新造輪子。學生提醒 Theorem 2.3.4：

1. $L^1$ 是向量空間，所以 $f-g\in L^1$。
2. 由 Theorem 2.4.1，$|f-g|\in L^1$。
3. 再由向量空間，$\frac12(f+g\mp|f-g|)\in L^1$，而且由線性
   $$\int\min\{f,g\}=\tfrac12\left(\int f+\int g-\int|f-g|\right).$$

講者：「謝謝……我有種不祥的預感要重新發明輪子，果然沒錯，那就等於重證 $L^1$ 是向量空間。」[▶ 14:04](https://youtu.be/J_vsyczvSdc?t=844)

---

## 3. |f| 可積不代表 f 可積；平移的連續性

**$|f|$ 可積不推出 $f$ 可積**[▶ 15:07](https://youtu.be/J_vsyczvSdc?t=907)：課本說，這種函數**無法具體寫出來**，只能證明它存在；證明需要本書不介紹的工具，請看實分析或測度論的書，例如 Friedman（1982）或 Halmos（1974）。

講者猜 Friedman 是不是做奇異四維流形的那位。【口頭】他說做四維流形的人也可能是分析學家，那是分析的前線；他的學生 Min 曾說，數學成長的一個體驗是明白「實流形論到某個程度就是分析」，而講者在大學部教流形時，展示的幾乎都是線性代數。

> 【課本補充】查課本參考書目：「Friedman, A., *Foundations of Modern Analysis*, Dover, 1982」；「Halmos, P.R., *Measure Theory*, Springer, 1974」。

> 以下**不是逐字稿內容**，是補充這種函數為什麼需要額外工具：標準例子是取一個**不可測集** $V\subseteq[0,1]$，令 $f=\chi_V-\chi_{[0,1]\setminus V}$。則 $|f|=\chi_{[0,1]}$ 可積，但 $f$ 不可積。不可測集的存在要用選擇公理。

**Theorem 2.4.3（平移的連續性）**[▶ 14:37](https://youtu.be/J_vsyczvSdc?t=877)：若 $f\in L^1(\mathbb{R})$，則

$$\lim_{z\to0}\int|\tau_zf-f|=0.$$

講者只敘述，說這些直觀上夠清楚，就往下走。

【課本補充】證明概要：階梯函數的情況容易。一般情況，$f\simeq\sum f_n$，取 $n_0$ 使 $\sum_{n>n_0}\int|f_n|<\varepsilon/3$，則

$$\int|\tau_zf-f|\le\int\left|\tau_z\sum_{n\le n_0}f_n-\sum_{n\le n_0}f_n\right|+2\sum_{n>n_0}\int|f_n|,$$

第一項是階梯函數的情況，$z\to0$ 時趨近 0；第二項 $<2\varepsilon/3$。（課本說這個定理在 Theorem 2.15.3 摺積那裡會用到。）

---

## 4. 用可積函數展開

[▶ 18:18](https://youtu.be/J_vsyczvSdc?t=1098) 課本 Definition 2.5.1。

**問題**：之前是用**階梯函數**的級數定義可積函數。如果改用**可積函數**的級數重複這個構造，會得到新的函數嗎？課本：**不會**。這是 Lebesgue 可積函數空間的一種**完備性**，是 Lebesgue 積分理論的基本結果。

**定義**：$f$ 實值，$(f_n)$ 是**可積函數**（不再要求是階梯函數）。若

- (a) $\sum_{n=1}^\infty\int|f_n|<\infty$；
- (b) $f(x)=\sum f_n(x)$ 對每個 $\sum|f_n(x)|<\infty$ 的 $x$，

就寫 $f\simeq f_1+f_2+\cdots$。

【課堂討論】[▶ 18:52](https://youtu.be/J_vsyczvSdc?t=1132) 講者問：之前級數裡是什麼函數？學生答：階梯函數。講者：現在每個 $f_n$ 本身是 Lebesgue 可積，也就是本身又是一串階梯函數的級數。所以這是「級數的級數」。

講者的類比【口頭】[▶ 20:28](https://youtu.be/J_vsyczvSdc?t=1228)：線性代數裡「線性組合的線性組合」是什麼？還是線性組合，很無聊。這裡也一樣，只是不是有限組合，而是級數。

【Q&A】[▶ 22:19](https://youtu.be/J_vsyczvSdc?t=1339) 學生問：這些不是都能寫成階梯函數嗎？講者：對，每個 $f_n$ 都能寫成 $f_n\simeq\sum_kf_{n,k}$，$f_{n,k}$ 是階梯函數。

**Lemma 2.5.2**[▶ 23:33](https://youtu.be/J_vsyczvSdc?t=1413)：若 $f\in L^1(\mathbb{R})$，則對每個 $\varepsilon>0$，存在階梯函數列 $(f_n)$ 使 $f\simeq f_1+f_2+\cdots$ 而且

$$\sum_{n=1}^\infty\int|f_n|\le\int|f|+\varepsilon.$$

講者說：課本叫它「技術性引理」，通常表示不太有趣；證明一頁長，跳過。它的意思是：可積函數一定能用階梯函數級數表示，而且還能讓 $\sum\int|f_n|$ 幾乎等於 $\int|f|$——這個「額外的小鈴鐺」下一個定理要用。[▶ 29:11](https://youtu.be/J_vsyczvSdc?t=1751)

【課本補充】證明概要：任取 $f\simeq g_1+g_2+\cdots$，取 $n_0$ 使 $\sum_{n>n_0}\int|g_n|<\varepsilon/2$。把前 $n_0$ 項合併：$f_1=g_1+\cdots+g_{n_0}$，$f_n=g_{n_0+n-1}$（$n\ge2$）。由 $\int|f_1|-\int|f|\le\int|f_1-f|\le\sum_{n\ge2}\int|f_n|$，得

$$\sum_n\int|f_n|=\left(\int|f_1|-\sum_{n\ge2}\int|f_n|\right)+2\sum_{n\ge2}\int|f_n|\le\int|f|+2\sum_{n>n_0}\int|g_n|<\int|f|+\varepsilon.$$

---

## 5. Theorem 2.5.3：展開成可積函數級數不會得到新東西

[▶ 25:22](https://youtu.be/J_vsyczvSdc?t=1522)

**定理**：若 $f\simeq f_1+f_2+\cdots$，$f_n$ 是可積函數，則 $f$ 可積，而且

$$\int f=\int f_1+\int f_2+\cdots.$$

講者強調：左邊的「$f\simeq\sum f_n$」只是**記號**，還沒說 $f$ 可積；「$f$ 可積」是定理的結論。[▶ 27:44](https://youtu.be/J_vsyczvSdc?t=1664)

**證明**[▶ 28:28](https://youtu.be/J_vsyczvSdc?t=1708)：

1. 由 Lemma 2.5.2（取 $\varepsilon=2^{-n}$），每個 $f_n$ 有階梯函數展開
   $$f_n\simeq f_{n,1}+f_{n,2}+\cdots,\qquad\sum_k\int|f_{n,k}|\le\int|f_n|+2^{-n}.$$
   講者：「選哪個 $\varepsilon$？這種證明永遠選 $2^{-n}$，因為幾何級數總會出現。」
2. 把所有 $f_{n,k}$（$n,k\in\mathbb{N}$）排成一個數列 $(h_m)$。課本寫「arranged from all the functions $g_{n,k}$」，講者認為是**筆誤**，應該是 $f_{n,k}$。[▶ 31:12](https://youtu.be/J_vsyczvSdc?t=1872)
   **為什麼能排**：這是「數列的數列」，但總共還是**可數**多個，所以能列舉。[▶ part 2 00:02](https://youtu.be/N9zbir7C1kY?t=2)
3. **條件 (a)**【課堂討論】（學生追問 $2^{-n}$ 怎麼用，講者寫出課本省略的計算）[▶ part 2 05:18](https://youtu.be/N9zbir7C1kY?t=318)：
   $$\sum_m\int|h_m|=\sum_{n=1}^\infty\sum_{k=1}^\infty\int|f_{n,k}|\le\sum_{n=1}^\infty\left(\int|f_n|+2^{-n}\right)=\sum_n\int|f_n|+1<\infty.$$
   $\sum\int|f_n|<\infty$ 是假設 (a)；$\frac12+\frac14+\cdots=1$。講者口誤說成「無窮加一還是小於無窮」，意思是有限的數加 1 還是有限。「幾何級數明白出現了。」
4. 所以 $f\simeq h_1+h_2+\cdots$，$f$ 可積。
5. **積分**[▶ part 2 11:56](https://youtu.be/N9zbir7C1kY?t=716)：所有級數都**絕對收斂**，可以任意重排（Riemann 重排定理反過來說：絕對收斂級數重排不改變和；條件收斂的才能重排成任何值），所以
   $$\int f=\sum_m\int h_m=\sum_n\sum_k\int f_{n,k}=\sum_n\int f_n.$$ ∎

> 以下**不是逐字稿內容**，是補上第 4 步的條件 (b)：若 $\sum_{n,k}|f_{n,k}(x)|<\infty$，則對每個 $n$，$\sum_k|f_{n,k}(x)|<\infty$，所以 $f_n(x)=\sum_kf_{n,k}(x)$，而且 $|f_n(x)|\le\sum_k|f_{n,k}(x)|$，故 $\sum_n|f_n(x)|<\infty$，於是 $f(x)=\sum_nf_n(x)=\sum_mh_m(x)$。

**關鍵一步**：雙重級數展開成單一數列；用 Lemma 2.5.2 的 $2^{-n}$ 讓總和還是有限。

---

## 6. Corollary 2.5.4：由級數造函數

[▶ part 2 12:29](https://youtu.be/N9zbir7C1kY?t=749)

**推論**：若 $f_1,f_2,\ldots\in L^1(\mathbb{R})$ 而且 $\sum\int|f_n|<\infty$，則存在可積函數 $f$ 使 $f\simeq f_1+f_2+\cdots$。

講者說這個方向反過來：Theorem 2.5.3 從一個已表示的函數出發；這裡從一串可積函數出發，**造出**一個函數。他喜歡「證明就是一個公式」：

$$f(x)=\begin{cases}\sum_{n=1}^\infty f_n(x), & \sum_{n=1}^\infty|f_n(x)|<\infty\\[2pt] 0, & \text{其他}\end{cases}$$

再用 Theorem 2.5.3，這個 $f$ 可積。[▶ part 2 15:32](https://youtu.be/N9zbir7C1kY?t=932)

---

## 7. 預告：L¹ 範數、零函數、零集

【口頭】[▶ part 2 16:24](https://youtu.be/N9zbir7C1kY?t=984)

- **$L^1$ 範數**（§2.6）：$\|f\|=\int|f|$。
- **零函數（null function）**：$\int|f|=0$。課本會給一些從零函數得到新零函數的方法。
- **範數收斂**：用 $L^1$ 範數定義收斂；要跟另一種收斂「幾乎處處收斂」區分。
- **零集（null set，測度為零的集合）**（§2.7）：$S$ 的特徵函數是零函數，即 $\int\chi_S=0$。
- **為什麼 $L^1$「幾乎」是 Banach 空間**：我們想說 $L^1$ 是 Banach 空間，但零函數不是 0 卻範數為 0，破壞了範數公理 (a)。解法是**等價類**：把幾乎處處相等（只在零集上不同）的函數視為同一個。它們的積分一樣。

**講者的動機**【口頭】[▶ part 2 20:24](https://youtu.be/N9zbir7C1kY?t=1224)：我們一直觀察到「積分時丟掉有限多個點不影響結果」，這是把這件事講清楚的方法。微分方程的**反 Laplace 變換**就是例子：改變函數在幾個點的值，Laplace 變換不變，所以正變換不是一對一，那怎麼談反變換？因為我們其實是在處理函數的**等價類**。可以規定反變換取連續的那個代表，或定個特別規則挑一個，或者乾脆不提，「工程師一百萬年都不會注意到」。

---

## 8. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| Thm 2.4.1 | $f\in L^1\Rightarrow|f|\in L^1$；$|\int f|\le\int|f|\le\sum\int|f_n|$ | $g_n=|s_n|-|s_{n-1}|$，$|g_n|\le|f_n|$；加減 $f_n$ 讓 $Z$ 外發散 |
| 瑕積分 | $\frac{\sin x}{x}$ 瑕積分收斂但不 Lebesgue 可積 | $|f|$ 不可積 |
| Cor 2.4.2 | $\min,\max\in L^1$ | $\frac12(f+g\mp|f-g|)$，逐點驗證 |
| 反向 | $|f|\in L^1\not\Rightarrow f\in L^1$ | 需要不可測集 |
| Thm 2.4.3 | $\int|\tau_zf-f|\to0$（$z\to0$） | 前有限項是階梯函數，尾巴 $<\varepsilon$ |
| Def 2.5.1 | 可積函數的級數 $f\simeq\sum f_n$ | 同 Def 2.3.1，只是 $f_n\in L^1$ |
| Lemma 2.5.2 | 可選階梯展開使 $\sum\int|f_n|\le\int|f|+\varepsilon$ | 合併前 $n_0$ 項 |
| Thm 2.5.3 | 可積函數級數表示 ⟹ $f\in L^1$，$\int f=\sum\int f_n$ | 雙重級數排成一列；$\sum2^{-n}=1$；絕對收斂可重排 |
| Cor 2.5.4 | $\sum\int|f_n|<\infty$ ⟹ 有 $f\simeq\sum f_n$ | 收斂處取和、其他處取 0 |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Theorem 2.5.3（$L^1$ 的完備性雛形） | 第 14 集：Riesz–Fischer 定理，$L^1$ 是 Banach 空間 |
| 零函數、零集、等價類 | 第 14 集（§2.6–2.7） |
| 平移的連續性 | 第 17 集：摺積 |
| Laplace／Fourier 變換的反變換 | 第 31–32 集：Fourier 變換 |

---

## 附：本集一句話總結

> **可積函數的絕對值、min、max 都可積；更重要的是，用可積函數（而不只是階梯函數）的級數去展開，得到的仍然只是可積函數，積分也照樣逐項相加——這是 $L^1$ 完備性的雛形，而下一步要處理的障礙，是那些「積分為 0 卻不是 0」的零函數。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-02-13 錄影逐字稿（part 1 whisper large-v3-turbo 轉錄 33:26；part 2 YouTube 自動字幕 22:11）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §2.4–2.5 整理。*
