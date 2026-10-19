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

## 本集概要

- **群的指數律** $g^a g^b = g^{a+b}$：看起來簡單，嚴格證明要分很多情況；示範正整數情形的歸納法。
- 用指數律證明 **$|g| = |g^{-1}|$**（很多同學作業卡在這題）。
- **兩個元素生成的子群** $\langle a,b\rangle = \{a^ib^j\}$（交換群中）是子群；用 $U(20)$ 舉例：$U(20)$ 不是循環群，但可以由 $3$ 和 $11$ 生成。
- 作業裡的 $D_4$ 表示法 $x^4 = y^2 = (xy)^2 = 1$ 就是課堂的 $R$、$f$。
- **中心化子 vs. 中心**：$Z(G)\subseteq C(a)$；而且 $Z(G) = \bigcap_{a\in G} C(a)$。

> ⚠️ 題號說明：課堂用的是 Gallian **第 5 版**。下面附上第 10 版對應的題號（找得到的話）。

---

## 筆記

### 開場：作業解答 [▶ 00:30](https://youtu.be/11juNBWZhO4?t=30)

老師會把前三份「講義習題 (lecture problems)」的解答貼出來。很多人在「證明 $|g| = |g^{-1}|$」這題差很遠。

### 題 1：群的指數律 $g^ag^b = g^{a+b}$ [▶ 01:00](https://youtu.be/11juNBWZhO4?t=60)

要嚴格證明 $|g|=|g^{-1}|$，老師發現需要先有這個**引理 (lemma)**：

> **引理（指數律 law of exponents）**　對群元素 $g$ 和所有 $a,b\in\mathbb{Z}$：$g^ag^b = g^{a+b}$。

老師說完整證明寫了**三頁**：負指數會冒出一大堆情況。課堂只示範 $a,b\in\mathbb{N}$ 的情形 [▶ 01:30](https://youtu.be/11juNBWZhO4?t=90)。

**證明（$a,b\in\mathbb{N}$，固定 $a$，對 $b$ 歸納）**
- **$b=1$** [▶ 02:00](https://youtu.be/11juNBWZhO4?t=120)：由次方的定義，$g^a g = g^{a+1}$。
- **歸納步驟** [▶ 02:30](https://youtu.be/11juNBWZhO4?t=150)：假設 $g^ag^b = g^{a+b}$。則
$$g^ag^{b+1} \overset{\text{定義}}{=} g^a(g^bg) = (g^ag^b)g \overset{\text{歸納假設}}{=} g^{a+b}g \overset{\text{定義}}{=} g^{a+b+1}.$$
- 所以對所有 $a,b\in\mathbb{N}$ 成立。$\blacksquare$

**老師的評論**
- 同樣也成立 $(g^m)^n = g^{mn}$，作業解答裡沒證 [▶ 08:30](https://youtu.be/11juNBWZhO4?t=510)。之後把情況縮小（例如兩個都是正數），可能會變成考題 [▶ 09:00](https://youtu.be/11juNBWZhO4?t=540)。
- 這不在課本裡，課堂也沒講，但作業需要它。Gallian 很棒，但有些地方「比較隨興 (freewheeling)」[▶ 09:30](https://youtu.be/11juNBWZhO4?t=570)。
- 老師打電話問了做代數的哥哥，哥哥說：指數律本來就很繁瑣 [▶ 13:00](https://youtu.be/11juNBWZhO4?t=780)。

### 題 2：$|g| = |g^{-1}|$ [▶ 05:00](https://youtu.be/11juNBWZhO4?t=300)

**設定**：$|g| = n$，也就是 $g^n = e$，而且 $g^j\neq e$ 對 $j = 1,2,\dots,n-1$ [▶ 05:30](https://youtu.be/11juNBWZhO4?t=330)。（**兩個條件都要**：$n$ 次會回到 $e$，而且沒有更小的正次方會。）

**步驟 1：$(g^{-1})^n = e$** [▶ 06:00](https://youtu.be/11juNBWZhO4?t=360)
- 從 $g^n = e$ 出發，兩邊右乘 $g^{-n}$：$g^ng^{-n} = g^{-n}$。
- 用指數律，左邊是 $g^{n-n} = g^0 = e$。所以 $g^{-n} = e$。
- 依負指數的定義，$g^{-n} = (g^{-1})^n$。所以 $(g^{-1})^n = e$，得 $|g^{-1}|\le n$ [▶ 07:30](https://youtu.be/11juNBWZhO4?t=450)。

**注意**：這一步還不能說 $|g^{-1}| = n$，因為可能有更小的次方也回到 $e$ [▶ 07:30](https://youtu.be/11juNBWZhO4?t=450)。

**步驟 2：沒有更小的次方（反證法）** [▶ 10:00](https://youtu.be/11juNBWZhO4?t=600)
- 假設 $(g^{-1})^j = e$，某個 $1\le j<n$。也就是 $g^{-j} = e$。
- 兩邊乘 $g^j$：$g^jg^{-j} = g^0 = e$，另一邊是 $eg^j = g^j$。所以 $g^j = e$ [▶ 11:00](https://youtu.be/11juNBWZhO4?t=660)。
- 這和 $|g| = n$ 矛盾。

所以 $|g^{-1}| = n$。$\blacksquare$

### 題 3：$\langle a,b\rangle$ 是子群（Ch.3 #54）[▶ 14:30](https://youtu.be/11juNBWZhO4?t=870)

（第 10 版為 Ch.3 #80，p.75。）

> **題目**　$G$ 是有限交換群，$a,b\in G$。證明
> $$\langle a,b\rangle = \{a^ib^j\mid i,j\in\mathbb{Z}\}$$
> 是 $G$ 的子群。$|\langle a,b\rangle|$ 和 $|a|$、$|b|$ 有什麼關係？

這是「一個元素生成的循環子群」的推廣：**兩個元素生成的子群**。它不一定是循環群，因為循環群只有一個生成元 [▶ 15:00](https://youtu.be/11juNBWZhO4?t=900)。

**證明（兩步法）**
- **非空** [▶ 16:30](https://youtu.be/11juNBWZhO4?t=990)：取 $i=j=0$，$a^0b^0 = ee = e\in\langle a,b\rangle$。
- **是子集** [▶ 17:00](https://youtu.be/11juNBWZhO4?t=1020)：$a^ib^j\in G$，所以 $\langle a,b\rangle\subseteq G$。老師說這步常被省略，但嚴格來說要檢查。反例：Ch.2 #37 的 $\begin{pmatrix}a&a\\a&a\end{pmatrix}$ 根本不是 $GL(2)$ 的子集 [▶ 18:00](https://youtu.be/11juNBWZhO4?t=1080)。
- **乘法封閉** [▶ 18:30](https://youtu.be/11juNBWZhO4?t=1110)：設 $x = a^ib^j$、$y = a^kb^l$。則
$$xy = a^ib^ja^kb^l = a^ia^kb^jb^l = a^{i+k}b^{j+l}\in\langle a,b\rangle.$$
  中間交換 $b^j$ 和 $a^k$ 要用到**交換群**；最後一步用到**指數律**（對任意整數）[▶ 19:30](https://youtu.be/11juNBWZhO4?t=1170)。
- **反元素封閉** [▶ 22:00](https://youtu.be/11juNBWZhO4?t=1320)：$a^{-i}b^{-j}\in\langle a,b\rangle$，而且
$$(a^{-i}b^{-j})(a^ib^j) = a^{-i}a^ib^{-j}b^j = e.$$
  交換群裡左反元素就是右反元素 [▶ 22:30](https://youtu.be/11juNBWZhO4?t=1350)。

由兩步子群判別法，$\langle a,b\rangle\le G$。$\blacksquare$

**非交換群就不行** [▶ 23:30](https://youtu.be/11juNBWZhO4?t=1410)：沒辦法交換，乘完不一定能回到 $a^ib^j$ 的形式。

**例：$U(20) = \{1,3,7,9,11,13,17,19\}$** [▶ 24:00](https://youtu.be/11juNBWZhO4?t=1440)
- **$\langle 3,7\rangle$**：$3^2 = 9$，$3^3 = 27\equiv 7$，所以 $7$ 已經是 $3$ 的次方。$\langle 3,7\rangle = \langle 3\rangle = \{1,3,9,7\}$。「選得不好」[▶ 26:30](https://youtu.be/11juNBWZhO4?t=1590)。
- **$\langle 3,11\rangle$** [▶ 27:00](https://youtu.be/11juNBWZhO4?t=1620)：
  - $3$ 的次方：$1,3,9,7$
  - $11^2 = 121\equiv 1$，所以 $11$ 的次方：$1,11$
  - 乘積：$3\cdot 11 = 33\equiv 13$，$9\cdot 11 = 99\equiv 19$，$7\cdot 11 = 77\equiv 17$
  - 共 $\{1,3,7,9,11,13,17,19\} = U(20)$。

所以 **$U(20)$ 不是循環群，但可以由兩個元素生成**（上一堂習題課證過它不是循環群）。

**和階的關係** [▶ 29:00](https://youtu.be/11juNBWZhO4?t=1740)：這例子 $|3| = 4$、$|11| = 2$、$|\langle 3,11\rangle| = 8$。觀察：$|a|$、$|b|$ 都**整除** $|\langle a,b\rangle|$。
- 原因：$\langle a\rangle\le\langle a,b\rangle$，而之後會學到「子群的階整除群的階」（第 7 章，Lagrange 定理）。
- 老師說這是「禁術」，第一次考試前**還不能用** [▶ 30:00](https://youtu.be/11juNBWZhO4?t=1800)。

### 題 4：$D_n$ 的兩種看法 [▶ 31:00](https://youtu.be/11juNBWZhO4?t=1860)

$$D_n = \{e,R,R^2,\dots,R^{n-1},\ f,Rf,R^2f,\dots,R^{n-1}f\},\qquad |D_n| = 2n.$$

**旋轉可以寫成矩陣** [▶ 33:00](https://youtu.be/11juNBWZhO4?t=1980)：旋轉 $2\pi/n$ 是線性變換
$$T(x,y) = \begin{pmatrix}\cos\frac{2\pi}{n} & -\sin\frac{2\pi}{n}\\ \sin\frac{2\pi}{n} & \cos\frac{2\pi}{n}\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}.$$
可以用這種公式研究，但用 $R$、$f$ 的符號簡單得多 [▶ 34:00](https://youtu.be/11juNBWZhO4?t=2040)。

> 💬 老師說「可能差一個正負號」，上面是標準的逆時針旋轉矩陣。他也一度想把旋轉子群寫成 $D_n\cap O(2)$，隨即自己更正：正交群 $O(2)$ 也含鏡射，所以不對。

**作業的 $D_4$ 表示法** [▶ 34:30](https://youtu.be/11juNBWZhO4?t=2070)：作業寫的是 $x^4 = 1$、$y^2 = 1$、$(xy)^2 = 1$。
- $(xy)^2 = 1$ 就是 $xyxy = 1$。兩邊左乘 $x^{-1}$：$yxy = x^{-1}$。
- 對照 $fRf = R^{-1}$：**$y$ 就是 $f$，$x$ 就是 $R$** [▶ 35:00](https://youtu.be/11juNBWZhO4?t=2100)。
- 這和畫圖轉來翻去得到的是**同一個群**。

### 題 5：中心化子 vs. 中心 [▶ 37:00](https://youtu.be/11juNBWZhO4?t=2220)

**定義** [▶ 37:30](https://youtu.be/11juNBWZhO4?t=2250)
- **中心化子** $C(a) = \{g\in G\mid ag = ga\}$：和**某一個** $a$ 交換的元素。
- **中心** $Z(G) = \{g\in G\mid gx = xg,\ \forall x\in G\}$：和**所有**元素交換的元素。

**哪個包含哪個？** [▶ 39:30](https://youtu.be/11juNBWZhO4?t=2370)
- $C(a)\subseteq Z(G)$？**不一定**。和 $a$ 交換的元素，不見得和別的元素交換 [▶ 40:00](https://youtu.be/11juNBWZhO4?t=2400)。
- $Z(G)\subseteq C(a)$？**對**。和所有人交換，當然和 $a$ 交換。而且 $Z(G)$ 是 $C(a)$ 的子群 [▶ 41:00](https://youtu.be/11juNBWZhO4?t=2460)。

**Ch.3 #15：$Z(G) = \bigcap_{a\in G} C(a)$** [▶ 41:30](https://youtu.be/11juNBWZhO4?t=2490)

（第 10 版為 Ch.3 #41，p.72。）

- **（$\subseteq$）** [▶ 42:30](https://youtu.be/11juNBWZhO4?t=2550)：設 $y\in Z(G)$。則 $ya = ay$ 對所有 $a$，所以 $y\in C(a)$ 對所有 $a$，所以 $y$ 在交集裡。（在交集裡 = 在每一個集合裡。）
- **（$\supseteq$）** [▶ 43:30](https://youtu.be/11juNBWZhO4?t=2610)：設 $z\in\bigcap_a C(a)$。由交集的定義，$z\in C(a)$ 對每個 $a$，也就是 $za = az$ 對所有 $a\in G$。所以 $z\in Z(G)$。$\blacksquare$

**和作業的關係** [▶ 46:00](https://youtu.be/11juNBWZhO4?t=2760)：L2 作業要算 $GL(2)$ 的中心化子和中心。老師的做法就是找同時和兩個特定矩陣交換的矩陣，條件合起來就得到中心（單位矩陣的倍數）。這正是「中心 = 中心化子的交集」在運作。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 引理 | lemma | [01:30](https://youtu.be/11juNBWZhO4?t=90) |
| 指數律 | law of exponents | [05:00](https://youtu.be/11juNBWZhO4?t=300) |
| 由兩個元素生成的子群 | subgroup generated by $a$ and $b$ | [15:00](https://youtu.be/11juNBWZhO4?t=900) |
| 生成元 | generator | [15:00](https://youtu.be/11juNBWZhO4?t=900) |
| 旋轉矩陣 | rotation matrix | [33:30](https://youtu.be/11juNBWZhO4?t=2010) |
| 正交群 | orthogonal group | [33:00](https://youtu.be/11juNBWZhO4?t=1980) |
| 交集 | intersection | [41:30](https://youtu.be/11juNBWZhO4?t=2490) |

## ⚠️ 待確認清單

（本集無）
