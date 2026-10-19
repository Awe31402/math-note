---
course: Abstract Algebra I (Fall 2016)
episode: 6
lecture: 習題課
date: 2016-09-06
video: https://www.youtube.com/watch?v=snuWHOFfBhs
notes: 無直接對應（Gallian 第 2、3 章習題）
---

# 第 6 集 · 習題課：Gallian 第 2、3 章 [▶ 影片](https://www.youtube.com/watch?v=snuWHOFfBhs&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[05-L4-整除-gcd-輾轉相除法]] ｜ [總目錄](../README.md) ｜ 下一集：[[07-L5-模運算基礎]] →

## 本集概要

- 子群判別法的完整範例：行列式為 2 的整數次方的矩陣構成 $GL(2,\mathbb{R})$ 的子群。
- 釐清「單位元素」與「反元素」、「單位元素」與「恆等式」的差別；用 $U(7)$ 的 Cayley 表示範。
- 補完 L3 的論證：**偶數邊形**中通過邊中點的鏡射也滿足 $fRf=R^{-1}$。
- 在 $D_4$ 中純代數化簡；推出好用的交換規則 $fR = R^{-1}f$、$Rf = fR^{-1}$。
- 用元素的階證明 **$U(20)$ 不是循環群**。

> ⚠️ 題號說明：課堂用的是 Gallian **第 5 版**。下面附上第 10 版對應的題號（找得到的話）。

---

## 筆記

### 題 1：$H = \{A\in GL(2,\mathbb{R}) \mid \det A \text{ 是 2 的次方}\}\le GL(2,\mathbb{R})$ [▶ 00:30](https://youtu.be/snuWHOFfBhs?t=30)

（課堂說是 Ch.3 #44；第 10 版為 Ch.3 #74，p.75，題目明寫「integer power of 2」。）

**先釐清題意** [▶ 01:32](https://youtu.be/snuWHOFfBhs?t=92)：「2 的次方」必須包含**負整數次方**，也就是 $\det A = 2^k$，$k\in\mathbb{Z}$。如果只允許正次方，反元素就不會在 $H$ 裡，所以這是唯一合理的解讀。

**證明（兩步法）**
- **非空** [▶ 02:02](https://youtu.be/snuWHOFfBhs?t=122)：$\det I = 1 = 2^0$，所以 $I\in H$。
  - 這裡的單位元素就是 $I$，因為要證的是 $GL(2,\mathbb{R})$ 的**子群**，單位元素必須和大群相同。對比 Ch.2 #37 的 $\begin{pmatrix}a&a\\a&a\end{pmatrix}$ 群：那題不是子群，單位元素也不是 $I$ [▶ 03:04](https://youtu.be/snuWHOFfBhs?t=184)。
- **乘法封閉** [▶ 03:34](https://youtu.be/snuWHOFfBhs?t=214)：設 $\det A = 2^k$、$\det B = 2^l$（$k,l\in\mathbb{Z}$），則
  $$\det(AB) = \det A\det B = 2^{k+l},\qquad k+l\in\mathbb{Z},$$
  所以 $AB\in H$。
- **反元素封閉** [▶ 05:05](https://youtu.be/snuWHOFfBhs?t=305)：設 $\det A = 2^k$。因為 $2^k\neq 0$，$A^{-1}$ 存在於 $GL(2,\mathbb{R})$，且 $AA^{-1}=I$。取行列式得 $2^k\det A^{-1} = 1$，所以 $\det A^{-1} = 2^{-k}$，而 $-k\in\mathbb{Z}$，所以 $A^{-1}\in H$。

由兩步子群判別法，$H\le GL(2,\mathbb{R})$。$\blacksquare$（老師說用一步法會更俐落。）

**判別法的意義** [▶ 08:12](https://youtu.be/snuWHOFfBhs?t=492)：沒有子群判別法的話，要逐一驗證結合律、單位元素、反元素、封閉性。判別法讓我們**不必管結合律**（從大群繼承），通常也不必另外處理單位元素。老師習慣先找單位元素，只是因為它最容易用來證明「非空」；其實任何一個元素都可以 [▶ 09:13](https://youtu.be/snuWHOFfBhs?t=553)。

### 澄清：單位元素、反元素、恆等式 [▶ 09:45](https://youtu.be/snuWHOFfBhs?t=585)

- **單位元素**每個群只有**一個**（L1 定理 1）；**反元素**則是**每個元素各有一個**，通常彼此不同。
- 英文 *identity* 還有另一個意思：**恆等式**，也就是對所有變數值都成立的等式，例如畢氏恆等式 $\sin^2\theta + \cos^2\theta = 1$。這和「單位元素」完全無關 [▶ 10:47](https://youtu.be/snuWHOFfBhs?t=647)。

**例：$U(7) = \{1,2,3,4,5,6\}$ 的 Cayley 表** [▶ 11:47](https://youtu.be/snuWHOFfBhs?t=707)

| $\times$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| **1** | 1 | 2 | 3 | 4 | 5 | 6 |
| **2** | 2 | 4 | 6 | 1 | 3 | 5 |
| **3** | 3 | 6 | 2 | 5 | 1 | 4 |
| **4** | 4 | 1 | 5 | 2 | 6 | 3 |
| **5** | 5 | 3 | 1 | 6 | 4 | 2 |
| **6** | 6 | 5 | 4 | 3 | 2 | 1 |

> 💬 課堂只填了一部分，上表是依模 7 乘法補齊的完整版。

- 每列每行每個元素恰好出現一次，像數獨一樣，也就是**拉丁方陣 (Latin square)**。這是消去律的結果 [▶ 12:49](https://youtu.be/snuWHOFfBhs?t=769)。
- 從表中讀出：$2^{-1}=4$、$3^{-1}=5$、$4^{-1}=2$，不同元素有不同的反元素 [▶ 13:19](https://youtu.be/snuWHOFfBhs?t=799)。
- 考試若要畫 Cayley 表，老師會先幫忙填好單位元素那一列一行。

**平凡子群** [▶ 14:19](https://youtu.be/snuWHOFfBhs?t=859)：$\{e\}$ 是子群，判別法幾乎立刻成立，因為 $ee = e$、$e^{-1} = e$。**空集合不是子群**，因為它沒有單位元素 [▶ 15:20](https://youtu.be/snuWHOFfBhs?t=920)。在 $D_n$ 中，單位元素就是旋轉 $0°$。

### 題 2：偶數邊形的 $fRf = R^{-1}$ [▶ 16:23](https://youtu.be/snuWHOFfBhs?t=983)

**兩種鏡射** [▶ 17:30](https://youtu.be/snuWHOFfBhs?t=1050)
- **奇數邊形**（如三角形）：每條對稱軸都通過一個頂點和對邊中點。
- **偶數邊形**（如正方形、八邊形）：有兩種對稱軸，一種**通過一對頂點**，另一種**通過一對邊的中點**。Gallian 把正方形的鏡射記作 $H, V, D, D'$。

L3 只證明了通過頂點的情況。這次補上**通過邊中點**的鏡射 [▶ 19:08](https://youtu.be/snuWHOFfBhs?t=1148)：追蹤頂點 $1,2,3,\dots,n$，依序做 $f$、$R$（逆時針）、$f$，結果和直接做一次順時針旋轉 $R^{-1}$ 相同 [▶ 20:40](https://youtu.be/snuWHOFfBhs?t=1240)–22:10。

> ⚠️ 待確認：頂點標號的板書圖示字幕無法還原，請看影片 [▶ 19:38](https://youtu.be/snuWHOFfBhs?t=1178)–22:10。

**旋轉方向的選擇** [▶ 22:10](https://youtu.be/snuWHOFfBhs?t=1330)：用逆時針只是慣例（如同極座標）；把所有 $R$ 換成 $R^{-1}$，結構完全一樣。

**結論** [▶ 23:40](https://youtu.be/snuWHOFfBhs?t=1420)：對所有 $D_n$，有 $fRf = R^{-1}$、$f^2 = e$，因此
$$D_n = \{e, R, R^2,\dots,R^{n-1},\ f, fR, fR^2,\dots, fR^{n-1}\},\qquad |D_n| = 2n.$$

### 題 3：在 $D_4$ 中化簡 $fR^{-2}fR^5$ [▶ 25:12](https://youtu.be/snuWHOFfBhs?t=1512)

（課堂說是 Ch.2 #32；第 10 版的同類題 Ch.2 #43（p.56）數字不同，要把 $R^6FRFR^{-3}FRF$ 寫成 $R^k$，把 $FR^4FR^5FR^2$ 寫成 $R^kF$。）

**兩條好用的交換規則** [▶ 26:45](https://youtu.be/snuWHOFfBhs?t=1605)　從 $fRf = R^{-1}$ 與 $f^2 = e$：
- 右乘 $f$：$fR = R^{-1}f$
- 左乘 $f$：$Rf = fR^{-1}$ [▶ 28:49](https://youtu.be/snuWHOFfBhs?t=1729)

**白話**：鏡射和旋轉可以交換位置，**代價是旋轉要變成反方向**。

**化簡** [▶ 27:15](https://youtu.be/snuWHOFfBhs?t=1635)　
$$fR^{-2}fR^5 = (fR^{-2}f)R^5 = R^{2}R^5 = R^7 = R^3,$$
其中 $fR^{-2}f = (fR^{-1}f)^2 = R^2$，最後一步用 $D_4$ 中的 $R^4 = e$ [▶ 30:24](https://youtu.be/snuWHOFfBhs?t=1824)。

> 💬 課堂上老師是一步步用交換規則把 $f$ 移到一起，讓 $ff = e$ 相消（「$f$ is its own natural enemy」）；中途有短暫混亂，學生提醒 $R^4=e$ 才得到 $R^3$。上面是同一結果的精簡寫法。

**要點**
- 化簡後**最多只剩一個 $f$ 或沒有 $f$**，答案一定是 $R^k$ 或 $fR^k$ 的形式 [▶ 29:52](https://youtu.be/snuWHOFfBhs?t=1792)。
- 同樣的計算在 $D_8$ 以上，$R^7$ 就無法再化簡 [▶ 31:54](https://youtu.be/snuWHOFfBhs?t=1914)。
- 寫作業和考試時，要把每一步用了哪條規則寫清楚，否則無法給部分分數 [▶ 28:19](https://youtu.be/snuWHOFfBhs?t=1699)。
- 學生覺得畫 $D_4$ 的 Cayley 表是「busy work」，老師不同意，認為親手做很重要 [▶ 25:43](https://youtu.be/snuWHOFfBhs?t=1543)。

### 題 4：$U(20)$ 不是循環群 [▶ 33:04](https://youtu.be/snuWHOFfBhs?t=1984)

（課堂說是 Ch.3 #9；第 10 版為 Ch.3 #27 後半，p.71。）

$U(20) = \{1,3,7,9,11,13,17,19\}$，共 8 個元素 [▶ 34:05](https://youtu.be/snuWHOFfBhs?t=2045)。

**思路** [▶ 35:39](https://youtu.be/snuWHOFfBhs?t=2139)：若 $U(20) = \langle k\rangle$，則 $\langle k\rangle = \{e,k,\dots,k^7\}$ 要有 8 個元素，所以 $k$ 的**階必須是 8**。只要檢查每個元素的階都不是 8 即可（老師用到「元素的階等於它生成的子群的階」，說這之後會證明）。

| 元素 | 計算 | 階 |
|---|---|---|
| $9$ | $9^2 = 81\equiv 1$ | 2 |
| $3$ | $3^4 = 9^2 \equiv 1$ | 4 |
| $7$ | $7^2 = 49\equiv 9$，$7^4 \equiv 9^2\equiv 1$ | 4 |
| $11$ | $11^2 = 121\equiv 1$ | 2 |
| $13$ | $13^2 = 169\equiv 9$，所以 $13^4\equiv 1$ | 4 |
| $17$ | $17\equiv -3$，$17^2\equiv 9$，所以 $17^4\equiv 1$ | 4 |
| $19$ | $19\equiv -1$，$19^2\equiv 1$ | 2 |

（$3^2 = 9 \neq 1$，所以 $|3|$ 確實是 4；其他階為 4 的元素同理。）

沒有任何元素的階是 8，所以 **$U(20)$ 不是循環群**。$\blacksquare$

**技巧** [▶ 37:39](https://youtu.be/snuWHOFfBhs?t=2259)：接近模數的數用**負代表元**比較好算，例如 $17\equiv -3$、$19\equiv -1 \pmod{20}$。

**老師的評論** [▶ 40:10](https://youtu.be/snuWHOFfBhs?t=2410)：直接畫完整個 Cayley 表當然也行，但看元素的階可以省很多計算。他也承認這可能有點「本末倒置」，用到了第 4 章的理論；也許這題的目的就是先培養直覺，讀第 4 章時會更容易理解。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 恆等式 | identity (equation true for all values) | [10:47](https://youtu.be/snuWHOFfBhs?t=647) |
| 畢氏恆等式 | Pythagorean identity | [11:17](https://youtu.be/snuWHOFfBhs?t=677) |
| 拉丁方陣 | Latin square | [12:49](https://youtu.be/snuWHOFfBhs?t=769) |
| 循環群 | cyclic group | [33:34](https://youtu.be/snuWHOFfBhs?t=2014) |

## ⚠️ 待確認清單

1. [▶ 19:38](https://youtu.be/snuWHOFfBhs?t=1178)–22:10 偶數邊形「過邊中點鏡射」的 $fRf=R^{-1}$ 圖解，頂點標號的板書（字幕無法還原）。
