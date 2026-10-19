---
course: Abstract Algebra I (Fall 2016)
episode: 8
lecture: 習題課
date: 2016-09-08
video: https://www.youtube.com/watch?v=11juNBWZhO4
notes: 無直接對應（Gallian 第 3 章習題、課堂作業）
---

# 第 8 集 · 習題課：Gallian 第 3 章 [▶ 影片](https://www.youtube.com/watch?v=11juNBWZhO4&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[07-L5-模運算基礎]] ｜ [總目錄](../README.md) ｜ 下一集：[[09-L6-循環群-上]] →

> **課程**：Abstract Algebra I（Liberty University，Fall 2016）— 第 8 集，習題課
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（46:49，自動字幕）＋ Gallian《Contemporary Abstract Algebra》10th ed. 第 3 章習題。本集沒有對應講義（指數律見講義 Thm 2.1.17）。
> **標記說明**：`【口頭】` 老師口頭補充；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點
> **題號**：課堂用 Gallian **第 5 版**。下面附第 10 版題號（找得到的話）。

---

## 目錄

- [0. 開場：作業解答](#0-開場作業解答)
- [1. 引理：群的指數律](#1-引理群的指數律)
- [2. 作業題：|g| = |g⁻¹|](#2-作業題g--g¹)
- [3. 題：兩個元素生成的子群 ⟨a,b⟩](#3-題兩個元素生成的子群-ab)
  - [3.1 證明它是子群](#31-證明它是子群)
  - [3.2 例：U(20) 由兩個元素生成](#32-例u20-由兩個元素生成)
  - [3.3 階的關係](#33-階的關係)
- [4. 【Q&A】Dn 的兩種看法](#4-qadn-的兩種看法)
- [5. 【Q&A】中心化子與中心](#5-qa中心化子與中心)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 開場：作業解答

[▶ 00:30](https://youtu.be/11juNBWZhO4?t=30) 老師會把前三份「講義習題（lecture problems）」的解答貼上網。「如果我今晚忘了，寄 email 提醒我。」

很多人在「**證明 $|g| = |g^{-1}|$**」這題「差很遠」。老師發現自己要有把握地證它，**需要先有一個引理**。

---

## 1. 引理：群的指數律

[▶ 01:00](https://youtu.be/11juNBWZhO4?t=60)

> **引理（指數律 law of exponents）**　$G$ 是群，$g\in G$。對所有 $a,b\in\mathbb{Z}$：
> $$g^ag^b = g^{a+b}.$$

【口頭】[▶ 01:30](https://youtu.be/11juNBWZhO4?t=90)「我叫它引理，因為對我來說它只是證明階的必要工具。但我花了**大約三頁**才寫完。要想的情況非常多。」

**課堂只示範一種情況：$a,b\in\mathbb{N}$。**固定 $a$，對 $b$ 歸納 [▶ 02:00](https://youtu.be/11juNBWZhO4?t=120)。

回憶次方的定義（L2）：$g^1 = g$，$g^{n+1} = g^ng$。

**基底 $b = 1$**：由定義，
$$g^ag^1 = g^ag = g^{a+1}.$$

**歸納步驟**[▶ 03:00](https://youtu.be/11juNBWZhO4?t=180)：假設 $g^ag^b = g^{a+b}$ 對某個 $b\in\mathbb{N}$ 成立。則
$$
\begin{aligned}
g^ag^{b+1} &= g^a(g^bg) &&(\text{次方的定義})\\
&= (g^ag^b)g &&(\text{結合律})\\
&= g^{a+b}g &&(\text{歸納假設})\\
&= g^{a+b+1}. &&(\text{次方的定義})
\end{aligned}
$$
所以對所有 $a,b\in\mathbb{N}$ 成立。$\blacksquare$

【口頭】[▶ 03:30](https://youtu.be/11juNBWZhO4?t=210)（學生說出「由歸納假設」）「我知道我得這樣說，但我也有同樣的問題：常常找不到需要的字。」

**負指數**[▶ 04:30](https://youtu.be/11juNBWZhO4?t=270)：「但一開始處理負次方，各種情況就從木頭裡冒出來。」「它其實就是簡單的歸納法。很繁瑣，但不可怕。」

**相關的事**[▶ 08:30](https://youtu.be/11juNBWZhO4?t=510)：$(g^m)^n = g^{mn}$ 也成立，但作業解答裡沒證。「如果我把情況縮小——例如兩個都是正數，或一正一負——它們可能會變成合理的考題。」

**為什麼要擔心這個**[▶ 09:00](https://youtu.be/11juNBWZhO4?t=540)：
- 這**不在課本裡**，課堂也沒證、沒講，但**作業需要它**。
- 「應該有人問我：『我好像需要很多群的指數律，你要我們證嗎？』其實我不想要你們證，我以為這是一題只用到課堂內容的好作業題，沒發現少了這個。」
- 「Gallian 很棒，但有些地方有點『隨興』（freewheeling），例如這裡。」

【口頭】[▶ 13:00](https://youtu.be/11juNBWZhO4?t=780)「寫完三頁的蠢證明之後，我想一定有更簡單的方法。所以我打電話給我哥——他是代數學家，這是他的快樂天堂。他的回答基本上是：**指數律就是很繁瑣**。」當然可以證幾個小引理讓它短一點，「但我懶得想聰明的辦法，花了好幾個小時直接做完。它像一根刺卡在我腦裡，我非拔掉不可。」

【口頭】[▶ 21:00](https://youtu.be/11juNBWZhO4?t=1260)「它就這麼無害地坐在 Dummit & Foote 的習題裡：『證明群的指數律』，看起來好小好簡單。大家不知道它有多可怕。」

> 📘 講義 Thm 2.1.17 收錄了指數律，並給了 $(g^m)^n = g^{mn}$ 的部分證明（見 [[01-L1-群的定義]] 第 9 節）。

---

## 2. 作業題：|g| = |g⁻¹|

[▶ 05:00](https://youtu.be/11juNBWZhO4?t=300)

> **題目**　$G$ 是群，$g\in G$。證明 $|g| = |g^{-1}|$。

**$|g| = n$ 的意思**[▶ 05:30](https://youtu.be/11juNBWZhO4?t=330)（**兩個條件都要**）：
1. $g^n = e$；
2. $g^j\neq e$ 對 $j = 1,2,\dots,n-1$（沒有更小的正次方回到 $e$）。

**Step 1：$(g^{-1})^n = e$**[▶ 06:30](https://youtu.be/11juNBWZhO4?t=390)

「從真的東西開始，而不是從想要的東西開始。」已知 $g^n = e$。兩邊右乘 $g^{-n}$：
$$g^ng^{-n} = eg^{-n} = g^{-n}.$$
左邊用**指數律**（「花了大代價得來的」）：$g^ng^{-n} = g^{n-n} = g^0 = e$。所以
$$g^{-n} = e.$$
由負次方的定義，$g^{-n} = (g^{-1})^n$ [▶ 07:30](https://youtu.be/11juNBWZhO4?t=450)。所以 $(g^{-1})^n = e$，得到
$$|g^{-1}|\le n.$$

**注意**[▶ 07:30](https://youtu.be/11juNBWZhO4?t=450)：這一步**還不能**說 $|g^{-1}| = n$。可能有更小的次方也回到 $e$。例如若 $n = 8$，邏輯上可能 $(g^{-1})^2 = e$，那 $(g^{-1})^8 = ((g^{-1})^2)^4 = e$ 也照樣成立。「這在本題的條件下其實不可能，但邏輯上還沒排除。」

**Step 2：沒有更小的次方（反證法）**[▶ 10:00](https://youtu.be/11juNBWZhO4?t=600)

假設 $(g^{-1})^j = e$，某個 $1\le j<n$。也就是
$$g^{-j} = e.$$

【課堂討論】[▶ 10:30](https://youtu.be/11juNBWZhO4?t=630)「我們要矛盾什麼？要證明：如果反元素的階小於 $n$，就逼得 $g$ 的階也小於 $n$。」

兩邊乘 $g^j$ [▶ 11:00](https://youtu.be/11juNBWZhO4?t=660)：
$$g^jg^{-j} = g^je\ \Rightarrow\ g^{j-j} = g^j\ \Rightarrow\ e = g^j.$$
但 $1\le j<n$，這跟 $|g| = n$ 的條件 2 **矛盾**。

所以不存在這樣的 $j$，$|g^{-1}| = n$。$\blacksquare$

【口頭】[▶ 12:00](https://youtu.be/11juNBWZhO4?t=720)「我看到大概只有三、四個人基本上是一點一點從群的定律推出來的。其他人是不知不覺**假設了**指數律。」

（無限階的情況：若 $|g| = \infty$ 而 $|g^{-1}| = m<\infty$，對 $g^{-1}$ 用同樣論證得 $|g| = |(g^{-1})^{-1}|\le m$，矛盾。所以兩者同時無限。）

---

## 3. 題：兩個元素生成的子群 ⟨a,b⟩

[▶ 14:30](https://youtu.be/11juNBWZhO4?t=870)（第 5 版 Ch.3 #54；第 10 版 Ch.3 #80，p.75）

> **題目**　$G$ 是**有限交換群**，$a,b\in G$。證明
> $$\langle a,b\rangle = \{a^ib^j : i,j\in\mathbb{Z}\}$$
> 是 $G$ 的子群。$|\langle a,b\rangle|$ 和 $|a|$、$|b|$ 有什麼關係？

這是循環子群的推廣 [▶ 15:00](https://youtu.be/11juNBWZhO4?t=900)：**兩個元素生成的子群**。它「不是循環子群」——循環子群只有一個生成元，這個有兩個。

### 3.1 證明它是子群

**Step 0：非空、是子集**
- 取 $i = j = 0$ [▶ 16:30](https://youtu.be/11juNBWZhO4?t=990)：$a^0b^0 = ee = e$，所以 $e\in\langle a,b\rangle$，非空。
- $a^ib^j\in G$（群對乘法、反元素封閉），所以 $\langle a,b\rangle\subseteq G$ [▶ 17:00](https://youtu.be/11juNBWZhO4?t=1020)。

【口頭】[▶ 17:30](https://youtu.be/11juNBWZhO4?t=1050)「如果我要從證明裡省略什麼，『它是子集』大概排第一。有時候我忘了，有時候它很明顯，有時候兩者都有。但嚴格來說要檢查。有時候這很有用——像第 37 題那些行列式為 0 的怪矩陣，**連 $GL(2)$ 的子集都不是**。」

**Step 1：乘法封閉**[▶ 18:30](https://youtu.be/11juNBWZhO4?t=1110)

設 $x,y\in\langle a,b\rangle$，即存在 $i,j,k,l\in\mathbb{Z}$ 使
$$x = a^ib^j,\qquad y = a^kb^l.$$
則
$$
\begin{aligned}
xy &= a^ib^ja^kb^l\\
&= a^ia^kb^jb^l &&(G\text{ 交換，可以把 }b^j\text{ 和 }a^k\text{ 對調})\\
&= a^{i+k}b^{j+l}. &&(\text{指數律，對任意整數})
\end{aligned}
$$
$i+k,\ j+l\in\mathbb{Z}$，所以 $xy\in\langle a,b\rangle$ [▶ 21:30](https://youtu.be/11juNBWZhO4?t=1290)。

【口頭】[▶ 19:30](https://youtu.be/11juNBWZhO4?t=1170)「很好笑，我開場講的東西本來跟你的問題無關，結果完全有關：這裡要用對**任意整數**的指數律。」「在我考你們證明它之前，你們可以用。」

**Step 2：反元素封閉**[▶ 22:00](https://youtu.be/11juNBWZhO4?t=1320)

$a^{-i}b^{-j}\in\langle a,b\rangle$，而且
$$(a^{-i}b^{-j})(a^ib^j) = a^{-i}a^ib^{-j}b^j = a^0b^0 = e.$$
另一個順序也立刻成立，因為**交換群裡左反元素自動是右反元素**[▶ 22:30](https://youtu.be/11juNBWZhO4?t=1350)。所以 $x^{-1} = a^{-i}b^{-j}\in\langle a,b\rangle$。

由兩步子群判別法，$\langle a,b\rangle\le G$。$\blacksquare$

**非交換群就不行**[▶ 23:30](https://youtu.be/11juNBWZhO4?t=1410)：不能交換的話，乘完不一定能回到 $a^ib^j$ 的形式（「看群裡的關係式而定」）。

### 3.2 例：U(20) 由兩個元素生成

[▶ 24:00](https://youtu.be/11juNBWZhO4?t=1440)「我想找一個不是循環的群，小一點的。」用上一堂習題課的 $U(20)$：
$$U(20) = \{1,3,7,9,11,13,17,19\}.$$

**試 $\langle3,7\rangle$**[▶ 25:30](https://youtu.be/11juNBWZhO4?t=1530)：
- $3^2 = 9$，$3^3 = 27\equiv7$。「喔喔，所以……」
- $3^4 = 27\cdot3 = 81\equiv1$，回來了。
- 7 已經是 3 的次方，所以 $\langle3,7\rangle = \langle3\rangle = \{1,3,9,7\}$。
- 「3 或 7 生成同一個子群。**我選得不好**。」[▶ 26:30](https://youtu.be/11juNBWZhO4?t=1590)

**試 $\langle3,11\rangle$**[▶ 27:00](https://youtu.be/11juNBWZhO4?t=1620)：「選一個不在這個清單裡的。」
- 3 的次方：$1,3,9,7$。
- 11 的次方：$11^2 = 121\equiv1$，所以只有 $1,11$。
- 乘積【課堂討論】：
  - $3\cdot11 = 33\equiv13$；
  - $9\cdot11 = 99\equiv19$；
  - 「還缺什麼？17。我猜是 $3^3\cdot11$」[▶ 28:30](https://youtu.be/11juNBWZhO4?t=1710)：$7\cdot11 = 77\equiv17$。
- 共 $\{1,3,7,9,11,13,17,19\} = U(20)$。

**結論**：$U(20)$ **不是循環群，但可以由兩個元素生成**——「如果你挑對兩個」。

### 3.3 階的關係

[▶ 29:00](https://youtu.be/11juNBWZhO4?t=1740)【課堂討論】這個例子：$|3| = 4$、$|11| = 2$、$|\langle3,11\rangle| = 8$。學生觀察：**$|a|$ 和 $|b|$ 都整除 $|\langle a,b\rangle|$**。

理由 [▶ 30:00](https://youtu.be/11juNBWZhO4?t=1800)：
- 不難看出 $\langle a\rangle\le\langle a,b\rangle$（取 $j = 0$）。
- 之後會學到：**子群的階整除群的階**（Lagrange 定理，第 7 章）。

【口頭】「喔，我不該現在告訴你們。那是第 7 章，在第一次考試**之後**。所以它是**禁忌的知識**——禁術。你們還不准用。」

---

## 4. 【Q&A】Dn 的兩種看法

[▶ 31:00](https://youtu.be/11juNBWZhO4?t=1860) 學生問置換和等距變換。

**$D_n$ 的元素**：
$$D_n = \{e,R,R^2,\dots,R^{n-1},\ f,Rf,R^2f,\dots,R^{n-1}f\},\qquad|D_n| = 2n.$$

**旋轉也可以寫成矩陣**[▶ 32:30](https://youtu.be/11juNBWZhO4?t=1950)：轉 $2\pi/n$ 是平面上的線性變換
$$T\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}\cos\frac{2\pi}{n}&-\sin\frac{2\pi}{n}\\[2pt]\sin\frac{2\pi}{n}&\cos\frac{2\pi}{n}\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}.$$
（老師：「我可能差一個正負號——sign，s-i-g-n 的那個。」上面是標準的逆時針旋轉矩陣。）

老師一度想把旋轉子群寫成「$D_n\cap\operatorname{Orth}(2)$」，馬上自己更正 [▶ 33:00](https://youtu.be/11juNBWZhO4?t=1980)：「我是白痴，正交群也包含鏡射。」

**可以用公式研究，但不想**[▶ 34:00](https://youtu.be/11juNBWZhO4?t=2040)：用 $R$、$f$ 的符號「簡單太多了」。

**作業的 $D_4$ 表示法**[▶ 34:30](https://youtu.be/11juNBWZhO4?t=2070)：作業寫的是
$$x^4 = 1,\qquad y^2 = 1,\qquad(xy)^2 = 1.$$
「別被騙了，這是同一個東西。」
- $(xy)^2 = 1$ 就是 $xyxy = 1$。
- 兩邊左乘 $x^{-1}$（老師先說乘 $y$，「我是白痴」，改成 $x^{-1}$）[▶ 35:00](https://youtu.be/11juNBWZhO4?t=2100)：
$$yxy = x^{-1}.$$
- 對照 $fRf = R^{-1}$：**$y$ 就是 $f$，$x$ 就是 $R$**。

「我不是故意換記號，只是從某個數學家那裡抄了這題。」

**重點**[▶ 36:00](https://youtu.be/11juNBWZhO4?t=2160)：作業用關係式描述的 $D_4$，跟畫圖轉來翻去的 $D_4$，**是同一個群**。

---

## 5. 【Q&A】中心化子與中心

[▶ 37:00](https://youtu.be/11juNBWZhO4?t=2220) 學生想搞懂中心化子和中心的差別。「它們看起來很像，但不一樣。其實一個自動是另一個的子集。來看是哪個。」

**定義**[▶ 37:30](https://youtu.be/11juNBWZhO4?t=2250)：

| | 定義 | 白話 |
|---|---|---|
| 中心化子 $C(a)$ | $\{g\in G : ag = ga\}$ | 跟**某一個** $a$ 交換的元素 |
| 中心 $Z(G)$ | $\{g\in G : gx = xg\ \forall x\in G\}$ | 跟**所有**元素交換的元素 |

**哪個包含哪個？**

- **$C(a)\subseteq Z(G)$？不一定。**[▶ 40:00](https://youtu.be/11juNBWZhO4?t=2400) 老師一開始「想說」是這個，然後自問問題在哪：$g$ 跟 $a$ 交換，**不代表** $g$ 跟所有東西交換。可能存在某個 $b$ 使 $bg\neq gb$。
- **$Z(G)\subseteq C(a)$？對。**[▶ 41:00](https://youtu.be/11juNBWZhO4?t=2460)「如果某個東西跟**每個人**交換，它當然跟**某個人**交換。」而且 $Z(G)$ 其實是 $C(a)$ 的**子群**，對每個 $a$ 都是。

### 作業題：Z(G) = 所有中心化子的交集

[▶ 41:30](https://youtu.be/11juNBWZhO4?t=2490)（第 5 版 Ch.3 #15；第 10 版 Ch.3 #41，p.72）

> **題目**　證明
> $$Z(G) = \bigcap_{a\in G}C(a).$$

**($\subseteq$)**[▶ 42:30](https://youtu.be/11juNBWZhO4?t=2550)【課堂討論】設 $y\in Z(G)$。則 $ya = ay$ 對所有 $a\in G$。所以 $y\in C(a)$ 對所有 $a$。所以 $y$ 在交集裡。

「要在交集裡，需要什麼？要在**每一個**組成交集的集合裡。這裡正是如此。」

**($\supseteq$)**[▶ 43:30](https://youtu.be/11juNBWZhO4?t=2610)設 $z\in\bigcap_{a\in G}C(a)$。由交集的定義，$z\in C(a)$ 對每個 $a\in G$。也就是
$$za = az\quad\text{對每個 }a\in G.$$
「所以 $z$ **取得了入場資格**，進入那個叫做『中心』的俱樂部。」$z\in Z(G)$。$\blacksquare$

【口頭】[▶ 45:00](https://youtu.be/11juNBWZhO4?t=2700) 老師把「subset（子集）」說成「sub-soup（子湯）」：「什麼是子湯？我今天還沒喝我的湯。」接著討論湯是用「喝」還是「吃」——「自從我加入亞洲文化圈，被告知是『喝』。看你用不用湯匙。」

**跟作業的關係**[▶ 45:30](https://youtu.be/11juNBWZhO4?t=2730)：Lecture 2 有一題要算 $GL(2)$ 的中心化子和中心。老師的做法：找同時跟兩個特定矩陣交換的矩陣——兩個條件合起來就得到中心（**單位矩陣的倍數**）。「這正是『中心 = 中心化子的交集』在運作。」（老師也承認：「老實說，我早就知道中心是單位矩陣的倍數，因為我做過這題。」）

「我要遲到一個小孩的生日派對了。」

---

## 6. 一頁速查表

### 6.1 本集結果

| 結果 | 關鍵一步 |
|---|---|
| 指數律 $g^ag^b = g^{a+b}$（$a,b\in\mathbb{N}$） | 固定 $a$ 對 $b$ 歸納：$g^ag^{b+1} = (g^ag^b)g = g^{a+b}g$ |
| $\lvert g\rvert = \lvert g^{-1}\rvert$ | ① $g^n = e\Rightarrow g^{-n} = (g^{-1})^n = e$；② 若 $(g^{-1})^j = e$，乘 $g^j$ 得 $g^j = e$，矛盾 |
| $\langle a,b\rangle\le G$（$G$ 交換） | $a^ib^ja^kb^l = a^{i+k}b^{j+l}$（**要交換**）；反元素 $a^{-i}b^{-j}$ |
| $U(20) = \langle3,11\rangle$，但不是循環的 | $\{1,3,9,7\}\times\{1,11\}$ 的乘積給出全部 8 個 |
| 作業的 $D_4$：$x^4 = y^2 = (xy)^2 = 1$ | $xyxy = 1\Rightarrow yxy = x^{-1}$，即 $fRf = R^{-1}$ |
| $Z(G)\subseteq C(a)$（反過來不一定） | 跟所有人交換 ⇒ 跟 $a$ 交換 |
| $Z(G) = \bigcap_aC(a)$ | 雙向包含：交集 = 在每一個裡面 |

### 6.2 提醒

- 「$|g| = n$」有兩個條件：$g^n = e$，**而且**沒有更小的正次方。
- 證明 $|x|\le n$ 和 $|x| = n$ 是兩回事。
- 子群判別法前先確認**子集**。
- Lagrange 定理（子群的階整除群的階）：第一次考試前「禁用」。

### 6.3 術語

| 中文 | English |
|---|---|
| 引理 | lemma |
| 指數律 | law of exponents |
| 歸納假設 | induction hypothesis |
| 由兩個元素生成的子群 | subgroup generated by $a$ and $b$ |
| 生成元 | generator |
| 旋轉矩陣 | rotation matrix |
| 交集 | intersection |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **指數律** | [[09-L6-循環群-上]]、[[10-L7-循環群-下]]：循環群的所有計算 |
| **$\lvert g\rvert = \lvert g^{-1}\rvert$** | [[09-L6-循環群-上]]：$\lvert a\rvert = \lvert\langle a\rangle\rvert$；[[16-L11-同構的性質]]：同構保持階 |
| **$\langle a,b\rangle$、$\langle a\rangle\le\langle a,b\rangle$** | [[19-L12-陪集與Lagrange定理-下]]：Lagrange 定理；[[25-L16-外直積與內直積]]：$U(20)\cong\mathbb{Z}_2\oplus\mathbb{Z}_4$、內直積 |
| **$D_n$ 的生成元與關係式** | [[04-L3-中心-中心化子-二面體群]] 講義補充；[[31-答疑課]]：6 階群分類 |
| **中心、中心化子** | [[28-L19-軌道穩定子定理]]、[[30-L20-Cauchy定理]]：類方程 $\lvert G\rvert = \lvert Z(G)\rvert+\sum[G:C(a)]$ |

---

## 附：本集一句話總結

> **群的指數律 $g^ag^b = g^{a+b}$ 看似簡單但證明很繁瑣（正整數情形用歸納法），它是證明 $|g| = |g^{-1}|$ 的關鍵；在交換群裡兩個元素生成的 $\langle a,b\rangle = \{a^ib^j\}$ 是子群（$U(20) = \langle3,11\rangle$ 雖然不是循環群）；中心是所有中心化子的交集，所以 $Z(G)\subseteq C(a)$，反過來不一定。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra I」(Fall 2016) 2016-09-08 習題課錄影逐字稿（YouTube 自動字幕，46:49）與 Gallian《Contemporary Abstract Algebra》10th ed. 習題整理。*
