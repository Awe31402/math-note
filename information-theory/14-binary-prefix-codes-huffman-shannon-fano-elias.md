---
course: 消息理論（陽明交大電機系，NYCU OCW）
episode: 14
lecture: Lec14 3.3.3 Examples of Binary Prefix Codes
date: 待補
video: https://youtu.be/-C9AfziaQ4Y
notes: Alajaji & Chen §3.3.2 末（Observation 3.30、Theorem 3.31）、§3.3.3（Lemma 3.32–Observation 3.36，pp. 86–93）
---

# 第 14 集 · Lec14 §3.3.3：Huffman code、Shannon–Fano–Elias code、Fano code [▶ 影片](https://youtu.be/-C9AfziaQ4Y)

← 上一集：[13](13-variable-length-codes-kraft-inequality.md) ｜ [總目錄](README.md) ｜ 下一集：[15](15-universal-lossless-codes.md) →

> **課程**：消息理論（Information Theory），陽明交大電機系，NYCU OCW — 第 14 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（53:56，whisper large-v3-turbo）＋ 課本 §3.3.2 末、§3.3.3（pp. 86–93）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：whisper 把「Kraft inequality」聽成「craft inequality／Crafty Equality／Cravity Equality」，「prefix code」聽成「Previous Code／previstic」，「suffix」聽成「surface」，「Huffman」聽成「Hoffmann／Hofman／Hofben」，「Fano」聽成「Phanel／Phenol／Penol」，「Elias」聽成「Alias／Elisa」，「Rényi」聽成「Rini／re-need」，「Jelinek」聽成「Jelenic」，「necessary」聽成「nextric」，「bottom-up」聽成「button-up」，「sorting」聽成「縮田」，「ternary」正確，「saturated」聽成「saturate」（正確），「Alice in Wonderland」正確，「Cover」聽成「Colver」，「criterion」聽成「quiterion」，「平均碼長」聽成「平均碼糖／平均馬長」，「ceiling」聽成「sealing」，「機生彈 彈生機」應為「雞生蛋、蛋生雞」。開頭 [00:00]「iiiii Questions」是亂碼。以下一律用正確的字，不再逐一標。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 回顧：Kraft 與 log(1/p) 的碼長](#1-回顧kraft-與-log1p-的碼長)
- [2. 例子回顧與定理總結](#2-例子回顧與定理總結)
- [3. 真實 source 有記憶；指數成本與 Rényi entropy](#3-真實-source-有記憶指數成本與-rényi-entropy)
- [4. Huffman 的故事與思路](#4-huffman-的故事與思路)
- [5. 最佳 prefix code 的三個必要條件](#5-最佳-prefix-code-的三個必要條件)
- [6. Huffman 演算法與例子](#6-huffman-演算法與例子)
- [7. Huffman code 的性質](#7-huffman-code-的性質)
- [8. D 進位與一般化 Huffman](#8-d-進位與一般化-huffman)
- [9. Huffman code 的樹是滿的](#9-huffman-code-的樹是滿的)
- [10. Shannon–Fano–Elias code](#10-shannonfanoelias-code)
- [11. 為什麼是 prefix code、為什麼解得回來](#11-為什麼是-prefix-code為什麼解得回來)
- [12. Fano code](#12-fano-code)
- [13. 排序過的版本：碼長可以少 1](#13-排序過的版本碼長可以少-1)
- [14. 一頁速查表](#14-一頁速查表)
- [15. 與後續集數的連結](#15-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集證明了變長碼的極限是 entropy；這一集看具體的 prefix code 設計：
- **Huffman code**：**最佳**（平均碼長最小），用「最佳碼必須滿足什麼」的必要條件一步步推出來；
- **Shannon–Fano–Elias code**：不用排序，用 CDF 的二進位表示當碼字；
- **Fano code**：排序後一直切成機率接近一半的兩群。

| 主題 | 課本 |
|---|---|
| 指數成本、Rényi entropy | Observation 3.30、Theorem 3.31（pp. 86–87） |
| Huffman：必要條件、演算法、例子、性質 | Lemma 3.32–3.33、Example 3.34、Fig. 3.6、Observation 3.35（pp. 87–91） |
| Shannon–Fano–Elias | §3.3.3 (B)、Observation 3.36（pp. 91–93） |
| Fano code、排序版 | 課本沒有（老師口頭） |

---

## 1. 回顧：Kraft 與 log(1/p) 的碼長

[▶ 00:00](https://youtu.be/-C9AfziaQ4Y?t=0)

- **Kraft inequality** $\sum_iD^{-\ell_i}\le1$：變長碼至少要 entropy。兩種證法：Kraft 原本用 prefix code（樹），以及用 uniquely decodable 的性質（McMillan）。
- 看到碼長 $\ell(x)=\lfloor-\log_DP(x)\rfloor+1$（課本 (3.3.2)）就知道是 Shannon 的概念：self-information $\log\frac1p$ 是三個公設下唯一的函數，所以碼長都要約 $\log\frac1p$。這樣設計就滿足 Kraft，就存在 prefix code。
- 平均碼長 $\le nH+1$（等號用到 i.i.d.）。

**複雜度**（【口頭】）：prefix code 的樹看起來不大，但英文 26 字母加空格 27 個，兩個一起壓是 $27^2$，三個一起是 $27^3$……實作很複雜。不過至少知道存在性；將來實作能力變強或有新想法，還是做得到。

---

## 2. 例子回顧與定理總結

[▶ 03:09](https://youtu.be/-C9AfziaQ4Y?t=189)

**機率從哪來**（【口頭】）：壓縮的檔案很大（4 MB、8 MB、1 GB），A、B、C 出現非常多次。0.8、0.1、0.1 是大數法則下「80% 是 A、10% 是 B……」——一定是大量重複的結果。

上一集的例子：$P=(0.8,0.1,0.1)$，$H\approx0.92$（純數學量，跟實作無關）。
- 一次一個：$\{0,10,11\}$，平均 1.2；
- 兩個一組：（這其實是 Huffman code，最好的碼）平均 0.96 $\le0.92+\frac12=1.42$。
- 三個一組，上下界只差 $\frac13$；四個一組差 $\frac14$……代價是複雜度（英文到 4 個一組，$27^4$ 就幾乎很難寫程式）。

【口頭】有同學問：$\frac1n$ 的上界能不能改善？兩個一組實際 0.96 遠比 1.42 好，所以上界太鬆，後續有一些零星研究在改善它。

**定理總結**（Theorem 3.28）：無損（錯誤率 0）、$D$ 進位（例如 CD 用很大的 $D=256$）。
- Forward：任意 $\varepsilon$，$n$ 夠大時存在 $n$ 階變長碼，平均碼率 $<H_D+\varepsilon$。【口頭】$n$ 通常要很大，這是實作工程師詬病的地方。
- Converse：所有 uniquely decodable code 平均碼率 $\ge H$——用 Kraft，相減、把 log 拿掉（FI 或 log-sum）。

---

## 3. 真實 source 有記憶；指數成本與 Rényi entropy

[▶ 09:50](https://youtu.be/-C9AfziaQ4Y?t=590)

【口頭】
- 前面都假設 i.i.d.，但真實的 source 不獨立。做字母壓縮的大家常用 *Alice in Wonderland* 比誰壓得好。Cover 的書有一章提到 Shannon 後續研究英文字母是幾階 Markov，一般 4 階就夠了；英文大致是 stationary（講話寫字有規律），壓縮極限就是 entropy rate。
- 平均碼長的 criterion 是線性成本（碼長 1 成本 1、碼長 2 成本 2）。但碼太長（例如 26 bit）delay 很久，有些實作的成本是指數的。

【課本補充】**Observation 3.30、Theorem 3.31**（pp. 86–87）：Campbell 的指數成本
$$L_n(t)=\frac1t\log_D\sum_{x^n}P_{X^n}(x^n)D^{t\ell(c_{x^n})},$$
最好的 $\frac1nL_n(t)$ 是 Rényi entropy $H_\alpha(X)$，$\alpha=\frac1{1+t}$（可以任意逼近、不可能更好）。$t\to0$ 回到平均碼長和 Shannon entropy。（第 2 集已介紹。）

【口頭】它叫 entropy，不是因為形式像物理的 entropy，而是因為它是指數成本下的壓縮極限。Jelinek、McEliece 等人也有相關研究。entropy 有各種形式、前面冠上人名；同學做一個特殊情形的研究，也可能有一個「你名字的 entropy」。

---

## 4. Huffman 的故事與思路

[▶ 13:22](https://youtu.be/-C9AfziaQ4Y?t=802)

【口頭】
- Huffman 是 MIT 學生，修 Fano 的課（1951 年）。期中時 Fano 說：這個題目我解不出來，有人解出來就不用考期末考，交報告就給滿分。
- Huffman 想挑戰，想了很久想不出來，準備好好讀書考試，發現時間來不及——突然靈機一動想到了。
- **Shannon 和 Fano 為什麼想不出來**：他們用 **top-down**，從整個系統往下看，直接找「什麼是 optimal」的充分必要條件。Huffman 用 **bottom-up**：退而求其次，問「**如果它是最好的碼，它必須有什麼性質**」——找 **necessary condition**。
- 放掉執著，換個角度想，新的思維就出來了。必要條件雖然不能完全界定最好的碼，但能一步步描繪出它的樣子。必要條件在很多地方有用：現在很多好的設計（例如好的 sequence）是用電腦搜出來的，搜尋空間很大，不符合必要條件的就排除——老師有些研究就是這樣做。
- 1952 年發表。他的博士論文不是這個（指導教授也不是 Shannon 或 Fano）；畢業後 MIT 把他留下來當教授——解了 Shannon 和 Fano 都解不出來的問題。

---

## 5. 最佳 prefix code 的三個必要條件

[▶ 16:54](https://youtu.be/-C9AfziaQ4Y?t=1014)

由 Kraft 的結論，找最佳 uniquely decodable code 只要在 prefix code 裡找（課本 Corollary 3.26）。

**Lemma 3.32**（p. 88）：$\mathcal C$ 是最佳二元 prefix code，機率 $p_1\ge p_2\ge\cdots\ge p_M$（同機率的按碼長遞增排列），碼長 $\ell_1,\dots,\ell_M$。則
1. **機率大的碼長短**：$p_i>p_j\Rightarrow\ell_i\le\ell_j$。
2. **機率最小的兩個碼長相等**：$\ell_{M-1}=\ell_M$。
3. **最長的碼字中，有兩個只差最後一位**（是兄弟）。

**證明**：
1. 若 $p_i>p_j$ 但 $\ell_i>\ell_j$，把兩個 codeword 對調，平均碼長變化
$$p_i\ell_j+p_j\ell_i-(p_i\ell_i+p_j\ell_j)=(p_i-p_j)(\ell_j-\ell_i)<0,$$
   更好，矛盾。【口頭】大家都覺得很自然，但第一個點出來的就是厲害。
2. 由 1，$\ell_{M-1}\le\ell_M$。若 $\ell_{M-1}<\ell_M$：codeword $M$ 是樹上最長、而且**孤單**的樹葉（旁邊沒有被用）。把它最後一位刪掉，因為是 prefix code，不會變成別的 codeword，仍是 prefix code，平均碼長更小，矛盾。【口頭】這是用樹的結構產生必要條件——很棒的觀察。
3. 最長的碼字中若沒有兩個只差最後一位，把它們最後一位都刪掉會更好。【口頭】所以**存在**一個最佳設計，最小的兩個機率是兄弟（不是兄弟就移過去）。注意課本／講義用 **an** optimal code：不唯一，只要存在；寫 **the** 就代表唯一。寫科學論文對 a 和 the 要很敏感。

---

## 6. Huffman 演算法與例子

[▶ 21:58](https://youtu.be/-C9AfziaQ4Y?t=1318)

**Lemma 3.33（Huffman）**（p. 89）：把機率最小的兩個 $a_{M-1},a_M$ 合併成新符號 $a_{M-1,M}$（機率 $p_{M-1}+p_M$），得到 $M-1$ 個符號的縮減 source。若 $\mathcal C'$ 是縮減 source 的最佳 prefix code，則
- $a_1,\dots,a_{M-2}$ 的 codeword 照抄；
- $f(a_{M-1})=[f'(a_{M-1,M})\,0]$、$f(a_M)=[f'(a_{M-1,M})\,1]$，

得到的 $\mathcal C$ 對原 source 是最佳的。

**演算法**：一直合併最小的兩個，直到剩兩個符號——兩個符號的最佳碼是唯一的 0 和 1（不管機率多少）。再往回一步步展開，每次在合併的那個碼後面加 0、加 1。【口頭】課本有提到反證法的證明（不難，同學可以自己想）；網路上也找得到實作。

**Example 3.34**（課本 p. 89，Fig. 3.6）：六個符號，機率 $0.25,0.25,0.25,0.1,0.1,0.05$。
1. 合併 0.1 和 0.05 → 0.15；剩 $0.25,0.25,0.25,0.15,0.1$。
2. 合併 0.15 和 0.1 → 0.25；剩 $0.25,0.25,0.25,0.25$。
3. 合併兩個 0.25 → 0.5；剩 $0.5,0.25,0.25$。（機率一樣時任選。）
4. 合併兩個 0.25 → 0.5；剩 $0.5,0.5$ → 0 和 1。
5. 往回展開：$0.5\to00,01$；$0.5\to10,11$；$11\to110,111$；$111\to1110,1111$。

得到 Huffman code：$00,01,10,110,1110,1111$。

> 以下**不是逐字稿內容**，是驗算：平均碼長 $=0.25\cdot2\cdot3+0.1\cdot3+0.1\cdot4+0.05\cdot4=1.5+0.3+0.4+0.2=2.4$；entropy $=3\cdot0.25\cdot2+2\cdot0.1\log_210+0.05\log_220\approx1.5+0.664+0.216=2.38$。

【口頭】程式看起來不難，但 27 個字母、4 個一組（$27^4$），寫看看就知道要跑很久。前面所有範例裡的「最佳碼」都是 Huffman code。

---

## 7. Huffman code 的性質

[▶ 25:34](https://youtu.be/-C9AfziaQ4Y?t=1534)

**Observation 3.35**（p. 90）：
- **Huffman code 不唯一**：
  - 0 和 1 全部互換（inverse），平均碼長一樣，也是最佳。
  - 機率相同時合併的選擇不同（例如四個 0.25 怎麼兩兩合併），也得到不同的 Huffman code。【口頭】後續有人研究不同選擇的差異：平均碼長一樣，但碼長的變異（second moment、third moment）不同，實作上可能有附帶好處。
- **有不是 Huffman code 的最佳碼**：把兩個同長度的 codeword 互換，平均碼長不變，但可能不是 Huffman 演算法產生的。
- **把 Huffman code 倒過來（reverse）得到最佳的 suffix code**：解碼要從後面解，仍可自由串接。【口頭】老師請學生做過「prefix 加 suffix」兩端都可以自由串接的碼，在記憶體存取有用，演算法可以修改來做。
- **二元 Huffman code 一定讓 Kraft 等號成立**（樹是 saturated 的）。
- $n$ 階二元 Huffman code 對 stationary source：
$$H(\mathbf X)\le\frac1nH(X^n)\le\bar R_n<\frac1nH(X^n)+\frac1n.$$
  $n\to\infty$ 時 $\bar R_n\to H(\mathbf X)$；但編解碼 delay 隨 $n$ 線性成長，**儲存複雜度隨 $n$ 指數成長**。

---

## 8. D 進位與一般化 Huffman

[▶ 28:07](https://youtu.be/-C9AfziaQ4Y?t=1687)

**$D$ 進位 Huffman**（Observation 3.35，p. 91）：每次合併 $D$ 個機率最小的符號（$D$ 叉樹）。
- 必要條件要改：最後的「孤鳥」不行，最後一層必須剛好**填滿 $D$ 個**。
- 所以 source 字母數要滿足 $|\mathcal X'|\equiv1\pmod{D-1}$；不滿足就加**機率為 0 的 dummy 符號**（它不會出現，所以不影響平均碼長）。
- 課本的例子：$|\mathcal X|=6$、$D=3$（ternary，例如用 $+1,-1,0$ 三個準位存資料），要擴充成 7 個，加一個 dummy。
- 【口頭】老師的例子：27 個字元、$D=4$，$27\bmod3=0\ne1$，會產生孤鳥，所以加一個機率 0 的字元變 28（$28\bmod3=1$）。

**一般化 Huffman（指數成本）**（p. 91）：Huffman 原本每次合併權重 $p_i+p_j$；指數成本下改成 $2^t(p_i+p_j)$，就能直接做出最小化 $\frac1nL_n(t)$ 的碼。【口頭】第一個想到的就很厲害；後來的人就慢慢推演。

---

## 9. Huffman code 的樹是滿的

[▶ 31:39](https://youtu.be/-C9AfziaQ4Y?t=1899)

【口頭】
- **最佳設計一定讓 Kraft 等號成立**（可以證明，同學回去想想）。
- 什麼時候等號成立？樹的**每一片樹葉都是 codeword**（full tree、saturated）。反例：$\{00,01,10,110\}$ 是 prefix code，但 111 沒用到，Kraft 嚴格小於 1。
- 好的設計不會有孤單落單的 codeword——「這個社會是很和諧的，每個人都會有人陪伴」。看到有落單的 codeword，就知道它不是最好的設計。
- 下面的 Shannon–Fano–Elias code 會落單，所以不是最好的。

---

## 10. Shannon–Fano–Elias code

[▶ 33:10](https://youtu.be/-C9AfziaQ4Y?t=1990)

**名字的烏龍**（【口頭】）：和 Stein lemma 一樣，Elias 說他根本沒參與。可能因為他們是 MIT 同事，Elias 在某些場合轉述過 Shannon 和 Fano 的想法，大家以為三人一起做的。所以應該叫 Shannon–Fano code，但那又和另一個版本（下面第 13 節）混淆。當時大家都在找好的設計，好幾個版本都很像。

**好處**：**不用排序**。Huffman（和 Fano code）要先掃過整本書算出各字母機率，再排序——額外的複雜度。Shannon–Fano–Elias 直接做。

**定義**（課本 p. 91）：$\mathcal X=\{1,\dots,M\}$，$P_X(x)>0$。
$$F(x):=\sum_{a\le x}P_X(a),\qquad\bar F(x):=\sum_{a<x}P_X(a)+\frac12P_X(x).$$
（CDF，以及「累加到前一個、再加上自己的一半」。）【口頭】Shannon 是機率專家，什麼都用機率去累加的思維。

**Encoder**：把 $\bar F(x)$ 寫成二進位小數 $.c_1c_2\cdots$，取前
$$k=\left\lceil\log_2\frac1{P_X(x)}\right\rceil+1$$
位當 codeword。【口頭】又是碼長 $\approx\log\frac1p$——Shannon 的慣性；兩個人切入角度不同，所以他沒做出 Huffman code，不見得是能力問題。

**例子**（老師；機率**故意不排序**）：$P=(0.1,0.3,0.2,0.4)$。

| $x$ | $P(x)$ | $F(x)$ | $\bar F(x)$ | 二進位 | $k$ | codeword |
|---|---|---|---|---|---|---|
| 1 | 0.1 | 0.1 | 0.05 | .000011… | 5 | 00001 |
| 2 | 0.3 | 0.4 | 0.25 | .01 | 3 | 010 |
| 3 | 0.2 | 0.6 | 0.5 | .1 | 4 | 1000 |
| 4 | 0.4 | 1.0 | 0.8 | .110011… | 3 | 110 |

> ⚠️ 逐字稿缺字：老師口述第 3 個 codeword 為「100」。依 $k=\lceil\log_25\rceil+1=4$ 應為 1000；平均碼長 $0.1\cdot5+0.3\cdot3+0.2\cdot4+0.4\cdot3=3.4$ 和老師說的 3.4 一致，所以應是 4 bit。

- 平均碼長 3.4。$H\approx1.846$，所以 $\bar\ell<H+2$。
- 畫成樹，每個 codeword 都很孤單——不是滿樹，所以不是最好的。但它**漸近**是好的：$n$ 個一組時 $\bar\ell<H(X^n)+2$，平均每個符號只差 $\frac2n$。

**Decoder**（課本 p. 92）[▶ 39:46](https://youtu.be/-C9AfziaQ4Y?t=2386)：收到 $(c_1,\dots,c_k)$，從最小的 $x$ 開始累加 CDF，找**第一個**滿足 $F(x)\ge.c_1\cdots c_k$ 的 $x$，就是原來的符號。（傳送端和接收端都能算 $F$；用 curve fitting 的方式解碼，不用畫樹。）

---

## 11. 為什麼是 prefix code、為什麼解得回來

[▶ 40:18](https://youtu.be/-C9AfziaQ4Y?t=2418)

記號 $[a]_k$：把 $a$ 的二進位表示在第 $k$ 位之後切掉。

**兩個關鍵不等式**：
1. 切掉的部分小於 $2^{-k}$：$\bar F(x)-[\bar F(x)]_k<\frac1{2^k}$。
2. $k=\lceil\log_2\frac1{P(x)}\rceil+1$ ⇒ $\frac1{2^k}\le\frac12P_X(x)=\bar F(x)-F(x-1)$。

**為什麼是 prefix code**（【口頭】）[▶ 41:20](https://youtu.be/-C9AfziaQ4Y?t=2480)：如果 $x$ 的 codeword $0.xx\cdots$ 是下一個 codeword 的前置，下一個就得是 $0.xx\cdots$ 再接別的。但 CDF 是累加的，下一個 $\bar F$ 至少比這個多 $\frac12P(x)+\frac12P(x+1)>2^{-k}$，第 $k$ 位以前一定會進位改變——前面不可能維持一樣。**刻意選的「一半」間距**正是為了讓它是 prefix code。（課本 Observation 3.36：Shannon–Fano–Elias code 是 prefix code。）
- 【口頭】書上通常只給步驟，不說背後的道理。理解了，就知道改成三進位、四進位時間距該設多少（老師出過這個作業）。

**為什麼解得回來**（課本 p. 92）：要證 codeword $c=[\bar F(x)]_k$ 滿足 $F(x-1)<c\le F(x)$——那麼「第一個 $F\ge c$ 的 $x$」就是正確的 $x$。
- $c\le\bar F(x)<F(x)$：trivial。
- $c>F(x-1)$：
$$F(x-1)\le\bar F(x)-\frac1{2^k}<[\bar F(x)]_k.$$
（第一個 ≤ 用不等式 2，第二個 < 用不等式 1。）

【口頭】早期的設計都是先有想法再設計，每個小動作都想過（例如 Huffman 的必要條件、這裡的 1/2 間距）。後來很多系統是靠工程經驗試出來的，知道怎樣好卻說不出為什麼——雞生蛋、蛋生雞，事後應該去想為什麼。

---

## 12. Fano code

[▶ 48:00](https://youtu.be/-C9AfziaQ4Y?t=2880)

Fano 自己做的版本，思路和 Shannon 不同。

**做法**：
1. 機率**排序**。
2. 切成兩群，讓兩群的機率總和**最接近一半、一半**；一群給 0、另一群給 1。
3. 每一群再切成機率最接近一半的兩群，再給 0、1……切到不能切為止。

**例子**（老師）：$0.35,0.25,0.15,0.15,0.1$。
- 第一刀：$\{0.35,0.25\}=0.6$ vs $\{0.15,0.15,0.1\}=0.4$，是最接近一半的切法 → 0 / 1。
- 左群：$\{0.35\}$ vs $\{0.25\}$ → 00、01。
- 右群：$\{0.15\}$ vs $\{0.15,0.1\}=0.25$ → 10、11；再切 $\{0.15\}$、$\{0.1\}$ → 110、111。

> 以下**不是逐字稿內容**，是依老師的切法推出的碼和平均碼長：$\{00,01,10,110,111\}$，平均 $0.35\cdot2+0.25\cdot2+0.15\cdot2+0.15\cdot3+0.1\cdot3=2.25$。（老師口述第一刀時說「右邊 0.7、左邊 0.4」，數字對不上；依機率總和應為 0.6 / 0.4。）

**思路**（【口頭】）：Shannon 的思路是「碼長 = $\log\frac1p$」（從三大公設出發）；Fano 的思路是從**輸出端**出發——**最好的壓縮碼輸出不能再被壓縮，0 和 1 要一半一半、彼此獨立**。所以每一刀都讓 0、1 的機率盡量一半一半。將來不管做什麼壓縮，希望輸出越像 uniform 越好。

**複雜度**：要排序，還要一直檢查所有切法；26 個字母 4 個一組，程式非常難寫。

---

## 13. 排序過的版本：碼長可以少 1

[▶ 52:05](https://youtu.be/-C9AfziaQ4Y?t=3125)

【口頭】另一個也被叫做 Shannon–Fano code 的版本（名稱很混淆）：先**排序**，再做 Shannon–Fano–Elias 的步驟，但碼長的「+1」可以拿掉：
$$k=\left\lceil\log_2\frac1{P_X(x)}\right\rceil.$$
仍然是 prefix code，整個證明都對，平均碼長每個少 1 bit（$<H+1$），代價是排序的額外複雜度。不管哪個版本都要滿足 Kraft；它們都不是 saturated，等號不成立。

---

## 14. 一頁速查表

**最佳 prefix code 的必要條件（Lemma 3.32）**
1. $p_i>p_j\Rightarrow\ell_i\le\ell_j$（否則對調：$\Delta=(p_i-p_j)(\ell_j-\ell_i)<0$）。
2. $\ell_{M-1}=\ell_M$（否則刪掉孤單樹葉的最後一位）。
3. 最長的兩個 codeword 是兄弟。

**Huffman（Lemma 3.33）**：合併最小兩個 → 遞迴 → 兩個符號用 0/1 → 往回加 0、1。
- 例：$(0.25,0.25,0.25,0.1,0.1,0.05)$ → $\{00,01,10,110,1110,1111\}$，平均 2.4（$H\approx2.38$）。
- 不唯一（0/1 互換、tie 的選法）；reverse 得最佳 suffix code；Kraft 等號（滿樹）。
- $D$ 進位：每次合併 $D$ 個；$|\mathcal X'|\equiv1\ (\mathrm{mod}\ D-1)$，不足補 0 機率 dummy。
- 指數成本：合併權重改 $2^t(p_i+p_j)$。

**Shannon–Fano–Elias**（不用排序）
- $\bar F(x)=\sum_{a<x}P(a)+\frac12P(x)$；codeword = $\bar F(x)$ 二進位前 $k=\lceil\log_2\frac1{P(x)}\rceil+1$ 位。
- Prefix：相鄰 $\bar F$ 差 $>\frac12P(x)\ge2^{-k}$ ⇒ 前 $k$ 位一定不同。
- 解碼：第一個 $F(x)\ge c$ 的 $x$；因 $F(x-1)\le\bar F(x)-2^{-k}<[\bar F(x)]_k\le F(x)$。
- $\bar\ell<H+2$。例 $(0.1,0.3,0.2,0.4)$ → $\{00001,010,1000,110\}$，3.4。
- 排序版：碼長 $\lceil\log_2\frac1p\rceil$，$\bar\ell<H+1$。

**Fano**：排序 → 一直切成機率最接近一半的兩群（讓輸出 0、1 接近 uniform）。

---

## 15. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 不知道機率時怎麼壓：adaptive Huffman、Lempel–Ziv | 第 15 集（§3.3.4） |
| Shannon–Fano–Elias → arithmetic code | 第 15 集附近（課本提到 arithmetic codes 基於 SFE） |
| 「最佳碼輸出 uniform」 | 第 2、12 集回顧；第 21 集（joint source-channel） |
| 必要條件的思路 | 第 19 集（capacity 的 KKT 條件）、第 29 集（rate-distortion 計算） |

---

## 附：本集一句話總結

> **Huffman 不找「最好的碼是什麼」，而是問「最好的碼必須長什麼樣」——機率小的碼長、最小的兩個是兄弟——由此一路合併就得到最佳碼，而且它的樹是滿的；Shannon–Fano–Elias 用 CDF 加半格間距保證 prefix、不用排序，代價是比 entropy 多約 2 bit。**

---

*筆記依據陳伯寧老師「消息理論」Lec14 錄影逐字稿（whisper large-v3-turbo，53:56）與 Alajaji & Chen 課本 §3.3.2–3.3.3 整理。*
