---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 10
lecture: Lec10 2.6 Divergence and variational distance
date: 待補
video: https://youtu.be/5thqXPaSBrM
notes: Alajaji & Chen §2.6（pp. 26–36，Definition 2.29–Lemma 2.43）
---

# 第 10 集 · Lec10 §2.6：divergence（relative entropy）、refinement、variational distance、Pinsker [▶ 影片](https://youtu.be/5thqXPaSBrM)

← 上一集：[09](09-data-processing-fano-inequality.md) ｜ [總目錄](README.md) ｜ 下一集：[11](11-convexity-information-measures-hypothesis-testing.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 10 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（31:07，whisper large-v3-turbo）＋ 課本 §2.6（pp. 26–36）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Kullback–Leibler」聽成「Callback Library」，「hypothesis testing」聽成「hypothic testing」，「Blahut」聽成「Blankwood／Breyhart」，「Cover」聽成「Hover」，「Chernoff–Stein lemma」聽成「Chernov-Stein-Lema／Chern of Stein Lema」，「Poisson」聽成「頗重」，「Morse code」聽成「摩斯碼」（正確），「variational」聽成「Varitional」，「Pinsker」正確，「Kolmogorov」聽成「Komagrov」，「supremum」聽成「Supremant」，「addictivity」應為「additivity」，「bias」聽成「bios」，「聯集」聽成「連擊」，「公設」聽成「公社」，「倒數」聽成「導數」。開頭 [00:00]「NASA」是亂碼。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Divergence 的定義與名字](#1-divergence-的定義與名字)
- [2. Chernoff–Stein lemma 的預告與烏龍史](#2-chernoffstein-lemma-的預告與烏龍史)
- [3. 為什麼叫 relative entropy](#3-為什麼叫-relative-entropy)
- [4. 非負性](#4-非負性)
- [5. Mutual information 就是 divergence](#5-mutual-information-就是-divergence)
- [6. Refinement：processing 的反操作](#6-refinementprocessing-的反操作)
- [7. Divergence 不是距離](#7-divergence-不是距離)
- [8. Variational distance](#8-variational-distance)
- [9. Pinsker 不等式](#9-pinsker-不等式)
- [10. Conditional divergence、chain rule、conditioning 不減少 divergence](#10-conditional-divergencechain-ruleconditioning-不減少-divergence)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】這一節**獨立於** Shannon 1948 年的論文：那篇完全沒提這些結果。Shannon 用數學量定義了操作上的壓縮極限和傳輸極限；這裡的 **divergence** 則刻畫 **hypothesis testing（假設檢定）錯誤率的收斂速度**，也有操作意義。看起來沒那麼經典，其實非常重要。這是 1951 年 Kullback 和 Leibler 的結果。

| 主題 | 課本 |
|---|---|
| Divergence、非負、和 MI 的關係 | Definition 2.29、Lemma 2.30–2.31（pp. 26–28） |
| Refinement | Definition 2.32、Lemma 2.33（pp. 28–29） |
| 不是距離、variational distance | Observation 2.34、Definition 2.35、Lemma 2.36（pp. 29–31） |
| Pinsker、反向 Pinsker | Lemma 2.37、Observation 2.38、Lemma 2.39（pp. 31–34） |
| Conditional divergence、chain rule | Definition 2.40、Lemma 2.41–2.43（pp. 34–36） |

---

## 1. Divergence 的定義與名字

[▶ 01:01](https://youtu.be/5thqXPaSBrM?t=61)

**Definition 2.29**（pp. 26–27）：$X$、$\hat X$ 定義在同一個字母集 $\mathcal X$，
$$D(X\|\hat X)=D(P_X\|P_{\hat X}):=E_X\left[\log_2\frac{P_X(X)}{P_{\hat X}(X)}\right]=\sum_{x\in\mathcal X}P_X(x)\log_2\frac{P_X(x)}{P_{\hat X}(x)}.$$

- 【口頭】**要背**。口訣「$p\log\frac pq$」：兩個分布 $p$、$q$ 的比值取 log，**對第一個分布 $p$** 取期望值，不是對 $q$。
- Convention：$0\log\frac0p=0$；$p\log\frac p0=\infty$（$p>0$）。
- 記號用**兩條槓** $\|$：一條槓 $|$ 已經是條件機率，用兩條避免誤會。

**名字**：Kullback–Leibler divergence；有的書（Blahut）叫 distance 或 **discrimination**；也叫 **relative entropy**（顯然受 Shannon 1948 用 entropy 一詞的影響）。現在通稱 divergence。

**動機**（【口頭】）[▶ 02:02](https://youtu.be/5thqXPaSBrM?t=122)：想像一個 distribution space，每一點是一個分布。高斯離 Poisson 比較近，還是離 uniform、binomial 比較近？要一個量來描述分布之間的遠近。但數學上 distance 要滿足三角不等式，divergence 不滿足，所以不叫 distance。

---

## 2. Chernoff–Stein lemma 的預告與烏龍史

[▶ 03:04](https://youtu.be/5thqXPaSBrM?t=184)

**為什麼叫 divergence 比較常用**：有名的 **Chernoff–Stein lemma**（下一集講）說，hypothesis testing 時根據 $n$ 個觀察猜是 $P_X$ 還是 $P_{\hat X}$，錯誤率大約是
$$2^{-n\,D(P_X\|P_{\hat X})}.$$
divergence 越大，兩個分布越「發散」，錯誤率隨觀察數衰減得越快。

【口頭】烏龍史：
- Chernoff 1952 年投稿時，一位匿名 reviewer 說「這個定理我記得 Charles Stein 證過了」。投稿時不敢反駁 reviewer，Chernoff 就把其中一個結果歸給 Stein。
- 後來 Stein 自己說：我根本沒證過這個 lemma。
- 但 1970 年代的書（例如 Blahut）全部叫 **Stein's lemma**，Chernoff 反而沒名字。後來才證實是烏龍。
- Cover 的書知道不是 Stein 做的，但因為大家都叫 Stein lemma，就叫 **Chernoff–Stein lemma**；本課課本也這樣叫。其實應該叫 Chernoff lemma。

---

## 3. 為什麼叫 relative entropy

[▶ 05:05](https://youtu.be/5thqXPaSBrM?t=305)

- 壓縮極限是 entropy $H(X)=\sum_xP_X(x)\log_2\frac1{P_X(x)}$（之後證明）。好的碼，**碼長約等於 $\log_2\frac1{P_X(x)}$**：機率越大、碼越短。【口頭】最有名的例子是摩斯碼：最常出現的字母最短，一個點。
- 假如真正的分布是 $P_X$，你**誤以為**是 $P_{\hat X}$，就會用碼長 $\log_2\frac1{P_{\hat X}(x)}$ 設計碼。平均碼長變成
$$\sum_xP_X(x)\log_2\frac1{P_{\hat X}(x)}=\sum_xP_X(x)\log_2\frac1{P_X(x)}+\sum_xP_X(x)\log_2\frac{P_X(x)}{P_{\hat X}(x)}=H(X)+D(P_X\|P_{\hat X}).$$
- 所以 divergence 是**錯誤認知（mistakenly assuming）付出的代價**：比最好的 entropy 多出來的部分——相對於 entropy 的量，所以叫 relative entropy。

【課本補充】課本（p. 27）同樣的說法：$D$ 衡量「誤以為來源分布是 $P_{\hat X}$ 時的無效率」。

【口頭】有人事後仿照 Shannon 給出公設、導出這個量（事後諸葛），概念差不多，這裡不介紹。

---

## 4. 非負性

[▶ 08:42](https://youtu.be/5thqXPaSBrM?t=522)

要檢驗這個數學定義符合操作預期（mathematical definition = operational expectation）。

**Lemma 2.30**（p. 27）：$D(X\|\hat X)\ge0$，等號 iff $P_X(x)=P_{\hat X}(x)$ 對所有 $x$。

- 直覺：錯誤認知的損失不可能是負的——不會因為誤認反而讓平均碼長更短。
- **證明**（log-sum）：
$$D(X\|\hat X)=\sum_xP_X(x)\log_2\frac{P_X(x)}{P_{\hat X}(x)}\ge\left(\sum_xP_X(x)\right)\log_2\frac{\sum_xP_X(x)}{\sum_xP_{\hat X}(x)}=1\cdot\log_2\frac11=0.$$
- 等號：log-sum 等號 iff $\frac{P_X(x)}{P_{\hat X}(x)}$ 是常數；總和都是 1，常數就是 1，兩個分布相同。
- 【口頭】所以 divergence 可以拿來當資料分析中兩個分布的「距離」：兩點重疊時才是 0。

---

## 5. Mutual information 就是 divergence

[▶ 10:12](https://youtu.be/5thqXPaSBrM?t=612)

**Lemma 2.31**（p. 28）：
$$I(X;Y)=D(P_{X,Y}\|P_X\times P_Y).$$
直接由定義得到（上一集要你背的寫法）。

【口頭】傳輸的物理意義：區隔「傳送端和接收端真正的關聯 $P_{X,Y}$」和「把它們當作完全獨立 $P_XP_Y$」之間的差異。差異越大能傳越多；完全重疊（$X$、$Y$ 獨立）就不能傳。

---

## 6. Refinement：processing 的反操作

[▶ 11:46](https://youtu.be/5thqXPaSBrM?t=706)

既然 MI 是 divergence，divergence 應該也有 data processing 的性質。反過來，介紹 **refinement（精煉）**。

**比喻**（【口頭】）：
- **Processing** 是把問題簡化：收集了一萬人的資料，精簡成六種狀況的三頁報告交給經理。經理只知道六種狀況，不知道細節。這是多對一的 mapping。
- 精簡時可能有誤認（自己的 bias）：真正的分布（黃色）和你誤認的分布（白色）之間有 divergence，它就是**用誤認的分布做判斷會付出的代價**（之後會看到正是錯誤率的代價）。
- 要讓錯誤率變小，就要看細節：經理說「第一種狀況範圍太大，年齡層分開、男女分開，重新給我一份報告」——這叫 **refinement**。

**Definition 2.32（refinement）**（p. 28）：把 $\mathcal X$ 分成 $k$ 個互斥集合 $\mathcal U_1,\dots,\mathcal U_k$（$\mathcal X=\bigcup_i\mathcal U_i$），定義 $\mathcal U=\{1,\dots,k\}$ 上的分布
$$P_U(i)=\sum_{x\in\mathcal U_i}P_X(x).$$
則 $P_X$ 叫 $P_U$ 的 **refinement**（$k$-refinement）。

**Lemma 2.33（refinement 不會減少 divergence）**（p. 29）：$P_X$、$P_{\hat X}$ 分別是 $P_U$、$P_{\hat U}$ 的 $k$-refinement，則
$$D(P_X\|P_{\hat X})\ge D(P_U\|P_{\hat U}).$$

**證明**（log-sum，每一塊分別用）：對每個 $i$，
$$\sum_{x\in\mathcal U_i}P_X(x)\log_2\frac{P_X(x)}{P_{\hat X}(x)}\ge\left(\sum_{x\in\mathcal U_i}P_X(x)\right)\log_2\frac{\sum_{x\in\mathcal U_i}P_X(x)}{\sum_{x\in\mathcal U_i}P_{\hat X}(x)}=P_U(i)\log_2\frac{P_U(i)}{P_{\hat U}(i)}.$$
對 $i$ 加總即得。等號 iff $\frac{P_X(x)}{P_{\hat X}(x)}=\frac{P_U(i)}{P_{\hat U}(i)}$ 對所有 $i$ 和 $x\in\mathcal U_i$。

- 等號的意義（【口頭】）：一塊裡每個細節的比值都一樣（例如整體 1:3，每個細節也都 1:3），看細節就沒有幫助。
- 等價說法：**processing（partition）只會降低 divergence**——兩個分布的區隔性降低，錯誤率會增加（Chernoff lemma 會給精確的意義）。

**總結**（【口頭】）[▶ 15:52](https://youtu.be/5thqXPaSBrM?t=952)：
- Processing = 多對一 mapping，細節消失；refinement 讓細節回復。
- Processing 降低 MI（傳輸量降低）、降低 divergence（區隔性降低、錯誤率上升）。
- 要增加傳輸量就 refine。例：$X=\pm1$，接收值 $Y$ 是實數；hard decision 是先量化（quantization）再決定，量化只會讓資料變差。refinement 就是**增加量化的 level**——從 2 bit 改成 4 bit，錯誤率就會變少。

---

## 7. Divergence 不是距離

[▶ 16:54](https://youtu.be/5thqXPaSBrM?t=1014)

數學上 distance（metric）要滿足（課本 p. 29 註 12）：
1. 非負，等號 iff 兩點相同——divergence **滿足**（Lemma 2.30）；
2. **對稱** $d(a,b)=d(b,a)$——divergence **不滿足**：$D(P_X\|P_{\hat X})\ne D(P_{\hat X}\|P_X)$（大部分情形不等），甲地到乙地的距離和乙地到甲地不同；
3. **三角不等式**——divergence **不滿足**。

所以 70 年代書上叫 distance 會誤導，後來不用了（Observation 2.34）。

---

## 8. Variational distance

[▶ 18:27](https://youtu.be/5thqXPaSBrM?t=1107)

證明時有時需要一個真正的距離（對稱、滿足三角不等式）。

**Definition 2.35（variational distance，$L_1$-distance）**（p. 30）：
$$\|P_X-P_{\hat X}\|:=\sum_{x\in\mathcal X}\left|P_X(x)-P_{\hat X}(x)\right|.$$
三個 metric 性質都滿足：絕對值非負（全為 0 iff 兩分布相同）、對稱、三角不等式。加上 variational 是為了和歐氏距離等區隔。

**例子**（老師）：$\mathcal X=\{0,1,2\}$，$P=\left(\frac13,\frac13,\frac13\right)$，$Q=\left(\frac14,\frac12,\frac14\right)$。
- divergence：$D(P\|Q)=\frac13\log\frac{1/3}{1/4}+\frac13\log\frac{1/3}{1/2}+\frac13\log\frac{1/3}{1/4}$。
- variational distance：對應項相減取絕對值再相加。

> 以下**不是逐字稿內容**，是把老師的例子算完：$\|P-Q\|=\frac1{12}+\frac16+\frac1{12}=\frac13$；$D(P\|Q)=\frac13\log_2\frac{4}{3}\cdot\frac23\cdot\frac43=\frac13\log_2\frac{32}{27}\approx0.0817$ bits。

**好算的公式** [▶ 19:59](https://youtu.be/5thqXPaSBrM?t=1199)（【口頭】）：兩個分布總和都是 1，就像兩人一樣有錢、投資在不同項目：有些項目我比你多，就一定有些比你少，多出來的剛好補少的。所以 variational distance = 2 × 「我比你大的部分」的總和。

**Lemma 2.36**（p. 30）：
$$\|P_X-P_{\hat X}\|=2\sup_{E\subset\mathcal X}\left|P_X(E)-P_{\hat X}(E)\right|=2\sum_{x:\,P_X(x)>P_{\hat X}(x)}\left[P_X(x)-P_{\hat X}(x)\right].$$

**證明第二個等號**（課本 p. 30）：令 $A=\{x:P_X(x)>P_{\hat X}(x)\}$。
$$\begin{aligned}
\|P_X-P_{\hat X}\|&=\sum_{x\in A}\left[P_X(x)-P_{\hat X}(x)\right]+\sum_{x\in A^c}\left[P_{\hat X}(x)-P_X(x)\right]\\
&=\sum_{x\in A}\left[P_X-P_{\hat X}\right]+\left[P_{\hat X}(A^c)-P_X(A^c)\right]\\
&=\sum_{x\in A}\left[P_X-P_{\hat X}\right]+\left[P_X(A)-P_{\hat X}(A)\right]=2\sum_{x\in A}\left[P_X(x)-P_{\hat X}(x)\right].
\end{aligned}$$
（用 $P(A^c)=1-P(A)$。）

**sup 的形式**（【口頭】）：任意切一個集合 $E$，把機率加起來再相減取絕對值——有的我大、有的我小，加在一起相減只會變小。最大的切法就是把「我比你大」的全切在一起（$E=A$），乘 2 就是 variational distance。
- 課本的證明（p. 31）：對任意 $E$，三角不等式得 $\|P_X-P_{\hat X}\|\ge|P_X(E)-P_{\hat X}(E)|+|P_X(E^c)-P_{\hat X}(E^c)|=2|P_X(E)-P_{\hat X}(E)|$；反過來取 $E=A$ 達到等號。
- 「切割後加總」就是 processing；processing 只會降低 variational distance。

---

## 9. Pinsker 不等式

[▶ 22:31](https://youtu.be/5thqXPaSBrM?t=1351)

【口頭】Pinsker 是蘇聯人，1964 年；他的老師是 Kolmogorov（強大數法則那位）——「這些人都是我們小時候的偶像」。

**Lemma 2.37（Pinsker's inequality）**（p. 31）：
$$D(X\|\hat X)\ge\frac{\log_2(e)}2\,\|P_X-P_{\hat X}\|^2.$$

把不是距離的 divergence 和真正的距離連起來，第二部分會用到。

**證明**（課本 pp. 31–32，老師講想法）[▶ 24:05](https://youtu.be/5thqXPaSBrM?t=1445)：
1. 令 $A=\{x:P_X(x)>P_{\hat X}(x)\}$，由 Lemma 2.36，$\|P_X-P_{\hat X}\|=2[P_X(A)-P_{\hat X}(A)]$。
2. **Worst case 的 processing**：只切成兩塊 $A$、$A^c$（就像報告只說「要做 / 不要做」，完全沒細節）。定義 $U=\mathbf 1\{X\in A\}$、$\hat U=\mathbf 1\{\hat X\in A\}$。$P_X$、$P_{\hat X}$ 是它們的 2-refinement，由 Lemma 2.33：$D(P_X\|P_{\hat X})\ge D(P_U\|P_{\hat U})$。而這個切法正好讓 variational distance 不變（最好的切割）。
3. 只剩二元的情形：令 $p=P_U(1)$、$q=P_{\hat U}(1)$，要證
$$p\ln\frac pq+(1-p)\ln\frac{1-p}{1-q}\ge2(p-q)^2.$$
   令 $f(p,q)$ 為左減右，
$$\frac{\partial f}{\partial q}=(p-q)\left(4-\frac1{q(1-q)}\right)\le0\quad(q\le p),$$
   因為 $q(1-q)\le\frac14$。所以 $q\le p$ 時 $f$ 對 $q$ 非遞增，又 $f(p,p)=0$，得 $f\ge0$。$q\ge p$ 的情形由對稱 $f(1-p,1-q)=f(p,q)$ 得到。
   - 【口頭】工程做法：寫個程式，$p,q$ 在 $[0,1]$ 畫圖，全部是正的就做完了；一定要證就微分。

> 以下**不是逐字稿內容**，是用第 8 節的例子檢查：右邊 $=\frac{\log_2e}{2}\cdot\frac19\approx0.7213\times0.1111\approx0.0801\le0.0817=D(P\|Q)$，成立。

【課本補充】**Observation 2.38**（pp. 32–33）：$D\to0$ ⇒ variational distance $\to0$，但反過來不成立。反例：$P_{X_n}(0)=\frac1n$、$P_{\hat X_n}(0)=0$。$D=\infty$（因為 $\frac1n\log\frac{1/n}0=\infty$），但 $\|P_{X_n}-P_{\hat X_n}\|=\frac2n\to0$。

**反向 Pinsker**（Lemma 2.39，p. 33）[▶ 25:06](https://youtu.be/5thqXPaSBrM?t=1506)：若 $D(P_X\|P_{\hat X})<\infty$，
$$D(P_X\|P_{\hat X})\le\frac{\log_2(e)}{\min_{x:P_X(x)>0}\min\{P_X(x),P_{\hat X}(x)\}}\cdot\|P_X-P_{\hat X}\|.$$
老師不打算講（後面不會用到），只說：variational distance 很小時，divergence 也不會太大，但界裡有「最小的機率」。

---

## 10. Conditional divergence、chain rule、conditioning 不減少 divergence

[▶ 25:36](https://youtu.be/5thqXPaSBrM?t=1536)

$X$ 是對的分布、$\hat X$ 是錯誤認知；給一個條件 $Z$，會不會幫我們分辨兩者？

**Definition 2.40（conditional divergence）**（p. 34）：
$$D(X\|\hat X|Z)=D(P_{X|Z}\|P_{\hat X|Z}|P_Z):=\sum_zP_Z(z)\sum_xP_{X|Z}(x|z)\log\frac{P_{X|Z}(x|z)}{P_{\hat X|Z}(x|z)}=\sum_{z,x}P_{X,Z}(x,z)\log\frac{P_{X|Z}(x|z)}{P_{\hat X|Z}(x|z)}.$$
【口頭】一定要從「對 $P_{X,Z}$ 取期望值、看條件機率的比值」這個觀點去看。

**Lemma 2.41**（p. 35）：
$$I(X;Y|Z)=D(P_{X,Y|Z}\|P_{X|Z}P_{Y|Z}|P_Z).$$
（同一類：條件聯合分布 vs 條件下當作獨立。）

**Lemma 2.42（chain rule for divergence）**（p. 35）：
$$D(P_{X_1,X_2}\|Q_{X_1,X_2})=D(P_{X_1}\|Q_{X_1})+D(P_{X_2|X_1}\|Q_{X_2|X_1}|P_{X_1}),$$
一般地 $D(P_{X^n}\|Q_{X^n})=\sum_{i=1}^nD(P_{X_i|X^{i-1}}\|Q_{X_i|X^{i-1}}|P_{X^{i-1}})$。
【口頭】二維分布之間的距離，可以先看第一維的區隔，再看給定第一維之後第二維的區隔——它是對的量，所以有 chain rule。

**Lemma 2.43（conditioning 不會減少 divergence）**（p. 35）[▶ 28:08](https://youtu.be/5thqXPaSBrM?t=1688)：
$$D(P_{X|Z}\|P_{\hat X|Z}|P_Z)\ge D(P_X\|P_{\hat X}).$$

**意義**：對照 $H(X|Z)\le H(X)$——side information 讓不確定性變小；對 divergence 來說，divergence 是「多容易分辨兩個分布」的指標，side information 讓我們更能分辨，所以 divergence 變大。兩者都說明 side information 有用。（課本 p. 34 的說明。）

**證明**（照口訣，FI）（課本 pp. 35–36）：
$$\begin{aligned}
&D(P_{X|Z}\|P_{\hat X|Z}|P_Z)-D(P_X\|P_{\hat X})=\sum_{z,x}P_{X,Z}(x,z)\log_2\frac{P_{X|Z}(x|z)P_{\hat X}(x)}{P_{\hat X|Z}(x|z)P_X(x)}\\
&\ge\log_2(e)\sum_{z,x}P_{X,Z}(x,z)\left(1-\frac{P_{\hat X|Z}(x|z)P_X(x)}{P_{X|Z}(x|z)P_{\hat X}(x)}\right)
=\log_2(e)\left(1-\sum_x\frac{P_X(x)}{P_{\hat X}(x)}\sum_zP_Z(z)P_{\hat X|Z}(x|z)\right)\\
&=\log_2(e)\left(1-\sum_x\frac{P_X(x)}{P_{\hat X}(x)}P_{\hat X}(x)\right)=0.
\end{aligned}$$
（第二行把 $P_X(x)$ 寫成 $\sum_zP_{X,Z}$ 放進第一項；$\sum_zP_ZP_{\hat X|Z}=P_{\hat X}$。）

等號 iff $\frac{P_X(x)}{P_{\hat X}(x)}=\frac{P_{X|Z}(x|z)}{P_{\hat X|Z}(x|z)}$ 對所有 $x,z$：給了 $Z$ 比值不變，就沒有幫助。

【口頭】例：台北市居民對某候選人的支持度，按年齡分細節（60 歲以上 vs 年輕人）。若不管年紀支持度都一樣，有沒有細節都一樣；若不同，細節就讓 divergence 嚴格變大。若 $Z$ 和要分辨的對象獨立（independent side information），就沒有用。獨立時 divergence 也有可加性（additivity），符合 Shannon 的公設。

【課本補充】課本 p. 36 提醒：不一定有 $D(P_{X|Z}\|P_{\hat X|\hat Z}|P_Z)\ge D(P_X\|P_{\hat X})$——兩邊用的 side information 不同時，結論不成立。

Chernoff–Stein lemma 下一集講。

---

## 11. 一頁速查表

**Divergence**（要背：$p\log\frac pq$，對 $p$ 取期望）
- $D(P\|Q)=\sum_xP(x)\log_2\frac{P(x)}{Q(x)}$；$0\log\frac0q=0$，$p\log\frac p0=\infty$。
- 誤用 $Q$ 設計碼：平均碼長 $=H(P)+D(P\|Q)$ ⇒ relative entropy。
- $D\ge0$（log-sum），等號 iff $P=Q$。
- $I(X;Y)=D(P_{XY}\|P_XP_Y)$；$I(X;Y|Z)=D(P_{XY|Z}\|P_{X|Z}P_{Y|Z}|P_Z)$。
- Chernoff–Stein（預告）：hypothesis testing 錯誤率 $\approx2^{-nD}$。

**Refinement**：$P_U(i)=\sum_{x\in\mathcal U_i}P_X(x)$ ⇒ $D(P_X\|P_{\hat X})\ge D(P_U\|P_{\hat U})$（每塊用 log-sum）。Processing 降低 MI 和 divergence；refinement（例如增加量化 level）提高。

**不是距離**：不對稱、不滿足三角不等式。

**Variational distance**
- $\|P-Q\|=\sum|P(x)-Q(x)|=2\sum_{P>Q}(P-Q)=2\sup_E|P(E)-Q(E)|$。
- 例：$(\frac13,\frac13,\frac13)$ vs $(\frac14,\frac12,\frac14)$：$\|P-Q\|=\frac13$，$D\approx0.0817$ bits。

**Pinsker**：$D(P\|Q)\ge\frac{\log_2e}{2}\|P-Q\|^2$。
- 關鍵：切成 $A=\{P>Q\}$ 兩塊（refinement 只會讓 $D$ 變大，$\|\cdot\|$ 不變），再證二元版 $p\ln\frac pq+(1-p)\ln\frac{1-p}{1-q}\ge2(p-q)^2$（$\partial_qf=(p-q)(4-\frac1{q(1-q)})\le0$）。
- $D\to0\Rightarrow\|\cdot\|\to0$，反之不然（$P_n(0)=\frac1n$、$Q_n(0)=0$）。

**Conditional divergence**
- Chain rule：$D(P_{X_1X_2}\|Q_{X_1X_2})=D(P_{X_1}\|Q_{X_1})+D(P_{X_2|X_1}\|Q_{X_2|X_1}|P_{X_1})$。
- $D(P_{X|Z}\|P_{\hat X|Z}|P_Z)\ge D(P_X\|P_{\hat X})$（FI），等號 iff 條件比值 = 無條件比值。對照 $H(X|Z)\le H(X)$：side information 都有用。

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Chernoff–Stein lemma、hypothesis testing | 第 11 集（§2.8） |
| Divergence 的 convexity | 第 11 集（§2.7） |
| $H(P)+D(P\|Q)$：誤認分布的碼長代價 | 第 13–14 集（變長碼、Huffman） |
| Divergence 在 AEP、典型集合 | 第 12 集 |
| Pinsker、variational distance | 第 32–35 集（第二部分） |
| Differential divergence | 第 23 集（§5.2） |

---

## 附：本集一句話總結

> **Divergence $D(P\|Q)$ 是「把 $P$ 誤認為 $Q$」的代價——多出來的平均碼長、也是兩個分布能被分辨的程度；它非負、refinement 和 side information 只會讓它變大，但它不是真正的距離，所以需要 variational distance，並用 Pinsker 不等式把兩者連起來。**

---

*筆記依據陳伯寧老師「消息理論」Lec10 錄影逐字稿（whisper large-v3-turbo，31:07）與 Alajaji & Chen 課本 §2.6 整理。*
