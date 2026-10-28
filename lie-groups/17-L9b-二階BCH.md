---
course: Matrix Lie Groups (Spring 2016)
episode: 17
lecture: L9b
date: 2016-04-04（part 2）
video: https://www.youtube.com/watch?v=mMpFnTxGtFA
notes: Hall 第 1 版 第 3 章導言、式 (3.1)–(3.3)（p.63–64）
---

# 第 17 集 · L9b：用 BCH 證明 Φ 是同態；二階 BCH 的計算 [▶ 影片](https://www.youtube.com/watch?v=mMpFnTxGtFA&list=PLBY4G2o7DhF3FS2CaX62eiQWGP9_xdLYs)

← 上一集：[[16-L9a-李代數例子與複數化]] ｜ [總目錄](README.md) ｜ 下一集：[[18-L10a-BCH恆等式]] →

> **課程**：Matrix Lie Groups（Liberty University，Spring 2016）— 第 17 集，April 4 part 2
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（25:49，自動字幕）＋ Hall《Lie Groups, Lie Algebras, and Representations》第 1 版 第 3 章開頭（p.63–64）
> **標記說明**：`【口頭】` 老師口頭補充、課本沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【課本補充】` 課本有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 「用 Φ(e^X) = e^{φ(X)} 定義 Φ」的兩個問題](#1-用-φex--eφx-定義-φ的兩個問題)
- [2. BCH 公式（形式）](#2-bch-公式形式)
- [3. BCH 讓 Φ 在單位元素附近是同態](#3-bch-讓-φ-在單位元素附近是同態)
- [4. 親手算二階 BCH](#4-親手算二階-bch)
- [5. 物理：動量生成平移](#5-物理動量生成平移)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

接上一集最後：給李代數同態 $\phi$，想用

$$
\Phi(e^X) = e^{\phi(X)} \tag{3.1}
$$

**定義**群同態 $\Phi$。今天說明 BCH 公式怎麼讓這件事行得通，並親手推 BCH 到二階。

## 1. 「用 Φ(e^X) = e^{φ(X)} 定義 Φ」的兩個問題

【課堂討論】[▶ 00:03](https://youtu.be/mMpFnTxGtFA?t=3) 學生：這有點像用大 $\operatorname{Ad}$ 定義小 $\operatorname{ad}$，只是反過來。Hall 說 (3.1) **隱式地**定義了 $\Phi$。

[▶ 01:10](https://youtu.be/mMpFnTxGtFA?t=70) 老師：問題是
1. **映成**：怎麼知道 $G$ 的每個元素都能寫成 $e^X$？「這很自以為是。」第 14 集看過，有些群的指數映射不是映成（$SL(2)$ 的例子）。
2. [▶ 01:43](https://youtu.be/mMpFnTxGtFA?t=103) **單射**：$X$ 不唯一的話，$\Phi$ 定義得好嗎？

> 【課本補充】Hall p.63–64：還有第二個嚴重問題：就算 $\Phi$ 定義得好，**為什麼它會是群同態**，一點也不清楚。
> - BCH 公式處理「為什麼是同態」。
> - 「每個元素是不是 $e^X$」則用 **$G$ 單連通**來處理。

## 2. BCH 公式（形式）

[▶ 02:18](https://youtu.be/mMpFnTxGtFA?t=138) **Baker–Campbell–Hausdorff 關係**，用對數寫：

$$
\log\left(e^Xe^Y\right) = X + Y + \frac12[X, Y] + \frac1{12}[X, [X, Y]] - \frac1{12}[Y, [X, Y]] + \cdots \tag{3.2}
$$

[▶ 03:24](https://youtu.be/mMpFnTxGtFA?t=204) **只在 $X, Y$ 夠小時成立**。

[▶ 03:59](https://youtu.be/mMpFnTxGtFA?t=239) 「$\cdots$」是什麼現在不重要。重點是：**每一項都只用 $X$、$Y$、它們的括號、括號的括號……寫成**。

⚠️ 逐字稿缺字：[▶ 03:59](https://youtu.be/mMpFnTxGtFA?t=239) 學生問三階係數是什麼，老師說「我不知道，連那個負號都不確定」。上面的係數和正負號依 Hall (3.2)。

## 3. BCH 讓 Φ 在單位元素附近是同態

[▶ 04:32](https://youtu.be/mMpFnTxGtFA?t=272) $\phi$ 是李代數同態：**線性、保持括號**。把它套在 (3.2) 兩邊：

$$
\begin{aligned}
\phi\left(\log(e^Xe^Y)\right) &= \phi(X) + \phi(Y) + \frac12[\phi(X), \phi(Y)] + \frac1{12}[\phi(X), [\phi(X), \phi(Y)]] - \cdots\\
&= \log\left(e^{\phi(X)}e^{\phi(Y)}\right). \tag{3.3}
\end{aligned}
$$

[▶ 05:40](https://youtu.be/mMpFnTxGtFA?t=340) 最後一步是**再用一次 BCH**，把 $X, Y$ 換成 $\phi(X), \phi(Y)$。【口頭】可以這樣用，因為 $\phi$ 是線性變換，**連續**，所以小的東西映過去還是小的。

[▶ 06:16](https://youtu.be/mMpFnTxGtFA?t=376)–[▶ 09:54](https://youtu.be/mMpFnTxGtFA?t=594) 然後（老師和學生一起理清步驟）：

$$
\begin{aligned}
\Phi\left(e^Xe^Y\right) &= \Phi\left(e^{\log(e^Xe^Y)}\right) &&e^{\log A} = A\\
&= e^{\phi\left(\log(e^Xe^Y)\right)} &&\text{(3.1)，代入 } \log(e^Xe^Y)\in\mathfrak g\\
&= e^{\log\left(e^{\phi(X)}e^{\phi(Y)}\right)} &&\text{(3.3)}\\
&= e^{\phi(X)}e^{\phi(Y)} = \Phi(e^X)\,\Phi(e^Y). &&\text{(3.1)}
\end{aligned}
$$

【Q&A】[▶ 09:10](https://youtu.be/mMpFnTxGtFA?t=550) 學生沒看懂第一行的 $\log$ 從哪來。老師補了一步：$e^Xe^Y = e^{\log(e^Xe^Y)}$，然後對它套 $\Phi$。

[▶ 10:45](https://youtu.be/mMpFnTxGtFA?t=645) **結論**：先不管指數映射的映成、單射問題，**至少對小的 $X$**，這樣定義的 $\Phi$ **是群同態**。同態性質來自上面的**李代數同態**。

[▶ 11:56](https://youtu.be/mMpFnTxGtFA?t=716) 【口頭】BCH 說的是：**李括號完全決定了群乘法**，至少對「由小元素指數化而來」的東西，也就是**單位元素附近**。

> 【課本補充】Hall p.64：「BCH 公式說明群乘積的所有資訊，至少在單位元素附近，都**編碼**在李代數裡。」

## 4. 親手算二階 BCH

[▶ 12:29](https://youtu.be/mMpFnTxGtFA?t=749) 【口頭】「我不貪心，只推 $\frac12$ 那一項。我手算過 $\frac1{12}$ 那項，但那要一小時。」

[▶ 13:37](https://youtu.be/mMpFnTxGtFA?t=817) 要證：

$$
e^Ae^B = e^{A + B + \frac12[A, B] + \cdots},
$$

「$\cdots$」是 $A, B$ 的**三階以上**（總次數）。所以只要**兩邊比到二階**。

[▶ 14:10](https://youtu.be/mMpFnTxGtFA?t=850) **左邊**：

$$
\begin{aligned}
e^Ae^B &= \left(I + A + \tfrac12A^2 + \cdots\right)\left(I + B + \tfrac12B^2 + \cdots\right)\\
&= I + A + B + \tfrac12A^2 + AB + \tfrac12B^2 + (\text{三階以上}).
\end{aligned}
$$

[▶ 14:45](https://youtu.be/mMpFnTxGtFA?t=885) **右邊**（「中間相遇」證法）：令

$$
U = A + B + \tfrac12AB - \tfrac12BA.
$$

[▶ 15:56](https://youtu.be/mMpFnTxGtFA?t=956)

$$
e^U = I + U + \tfrac12U^2 + \cdots
$$

【口頭】「聰明一點：只寫可能影響到二階的東西。」$U^2$ 裡只有 $(A + B)^2$ 是二階，含 $AB$ 的項平方後至少三階。

[▶ 16:31](https://youtu.be/mMpFnTxGtFA?t=991)

$$
\begin{aligned}
e^U &= I + A + B + \tfrac12AB - \tfrac12BA + \tfrac12\left(A^2 + AB + BA + B^2\right) + (\text{三階以上})\\
&= I + A + B + \tfrac12A^2 + AB + \tfrac12B^2 + (\text{三階以上}).
\end{aligned}
$$

[▶ 17:05](https://youtu.be/mMpFnTxGtFA?t=1025) $-\frac12BA$ 和 $+\frac12BA$「一起慘死」；$\frac12AB + \frac12AB = AB$。

[▶ 17:41](https://youtu.be/mMpFnTxGtFA?t=1061) 和左邊**到二階完全相同**。∎

【口頭】[▶ 18:14](https://youtu.be/mMpFnTxGtFA?t=1094) 「這是個**沒什麼用**的證明。它沒告訴你 $\frac12$ 從哪來，也沒告訴你下一項是什麼。也許花一週算到七階，會開始對係數有直覺。」

[▶ 18:48](https://youtu.be/mMpFnTxGtFA?t=1128) 【口頭】老師曾對州立大學的一位教授說「BCH 有點神祕」，對方好像覺得被冒犯，直接開始推給他看。「有辦法可以理解、很快推出來。也許我們會發現。我現在還說不出 $\frac1{12}$ 之後的係數。」

> 推論（不是逐字稿內容）：$\frac12$ 的另一種看法：$\log(e^Ae^B)$ 的二階部分必須對 $A\leftrightarrow B$ 互換時「變號的部分」是 $\frac12(AB - BA)$，因為 $\log(e^Be^A)$ 和 $\log(e^Ae^B)$ 的差在二階正好是 $AB - BA$。

## 5. 物理：動量生成平移

【口頭】[▶ 19:53](https://youtu.be/mMpFnTxGtFA?t=1193)
- 動量分量互相交換：$[p_1, p_2] = 0$。所以 $e^{tp_1}e^{sp_2} = e^{tp_1 + sp_2}$，BCH 的修正項全是 0。
- [▶ 20:33](https://youtu.be/mMpFnTxGtFA?t=1233) 讓 $e^{xp_1 + yp_2 + zp_3}\leftrightarrow$ 點 $(x, y, z)$。**用動量代數的指數表示物理空間。**
- [▶ 21:45](https://youtu.be/mMpFnTxGtFA?t=1305) $e^{a\cdot p}\,e^{r\cdot p} = e^{(r + a)\cdot p}$：乘上動量的指數，就是**平移**。動量的指數生成平移；角動量的指數生成旋轉。
- [▶ 22:59](https://youtu.be/mMpFnTxGtFA?t=1379) 數學上更仔細的理解是**齊性空間**（homogeneous space）：李群除以子群 $G/H$。例：剛體運動群 $\operatorname{ASO}(3)$（旋轉＋平移）除以 $SO(3)$，本質上就是 $\mathbb{R}^3$，點用平移的指數表示。
- [▶ 24:03](https://youtu.be/mMpFnTxGtFA?t=1443) 李代數 $\mathfrak{aso}(3)$ 由平移生成元 $p_1, p_2, p_3$ 和旋轉生成元 $J_{12}, J_{23}, J_{31}$ 張成。
- [▶ 24:38](https://youtu.be/mMpFnTxGtFA?t=1478) 「BCH 是物理上**真正算東西**的日常工具：李代數和群之間的指數化，是靠 BCH 才可能。就像芝麻街：『現代物理，由字母 B、C、H 贊助播出』。」

## 6. 一頁速查表

| 敘述 | 關鍵一步 |
|---|---|
| 想用 $\Phi(e^X) = e^{\phi(X)}$ 定義 $\Phi$ | 問題：$\exp$ 不一定映成、不一定單射；為何是同態 |
| BCH：$\log(e^Xe^Y) = X + Y + \frac12[X,Y] + \frac1{12}[X,[X,Y]] - \frac1{12}[Y,[X,Y]] + \cdots$ | 只用括號；$X, Y$ 小 |
| $\phi(\log(e^Xe^Y)) = \log(e^{\phi(X)}e^{\phi(Y)})$ | $\phi$ 線性、保持括號 |
| $\Phi(e^Xe^Y) = \Phi(e^X)\Phi(e^Y)$（小 $X, Y$） | $e^{\log A} = A$ ＋ 上式 |
| 李括號決定單位元素附近的群乘法 | |
| 二階 BCH | $e^{A+B+\frac12[A,B]}$ 和 $e^Ae^B$ 展開到二階相同 |
| 交換的生成元：BCH 修正為 0 | $e^{a\cdot p}e^{r\cdot p} = e^{(a+r)\cdot p}$ |

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| BCH 完整公式 | 下一集：BCH 恆等式（April 11），$\log$ 的導數 |
| Heisenberg 群（$[X,Y]$ 和 $X, Y$ 都交換） | Hall §3.1 Thm. 3.1 |
| 「$e^X$ 是不是涵蓋全部」→ 單連通 | 萬有覆蓋與 Lie 定理（April 25） |
| 齊性空間 $G/H$ | 群軌道與齊性空間（May 2） |

---

## 附：本集一句話總結

> **想用 $\Phi(e^X) = e^{\phi(X)}$ 從李代數同態造出群同態，關鍵是 BCH 公式：$\log(e^Xe^Y)$ 只由 $X, Y$ 和它們的巢狀括號決定，所以保持括號的 $\phi$ 自動讓 $\Phi$ 在單位元素附近保持乘法；把兩邊展開到二階，就能親手看到 $\frac12[X, Y]$ 這一項。**
