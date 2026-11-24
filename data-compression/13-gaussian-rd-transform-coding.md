---
course: Stanford EE274 Data Compression  Theory and Applications（2023 秋）
episode: 13
lecture: Lecture 13
date: 2023-11-08
video: https://youtu.be/9ZcYlFYqAhU
notes: 投影片 slide_13_2023.pdf、slide_13_2023_ann.pdf；《Elements of Information Theory》§10.3.2–10.3.3（書頁 310–315）
---

# 第 13 集 · Lecture 13：高斯率失真、注水直覺、轉換編碼（Gaussian RD, Water-Filling Intuition; Transform Coding） [▶ 影片](https://youtu.be/9ZcYlFYqAhU)

← 上一集：[12-mutual-information-rate-distortion](12-mutual-information-rate-distortion.md) ｜ [總目錄](README.md) ｜ 下一集：[14-transform-coding-in-practice](14-transform-coding-in-practice.md) →

> **課程**：Stanford EE274 Data Compression: Theory and Applications，2023 秋 — 第 13 集
> **講者**：Pulkit Tandon
> **來源**：YouTube 錄影逐字稿（1:21:23，人工字幕 en-US）＋ 投影片 `slide_13_2023.pdf`、`slide_13_2023_ann.pdf` ＋ Cover & Thomas §10.3.2–10.3.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【投影片補充】` 投影片有、口頭沒講
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 小考檢討](#1-小考檢討)
- [2. 回顧：高斯的率失真函數](#2-回顧高斯的率失真函數)
- [3. 率失真定理推廣到相關來源](#3-率失真定理推廣到相關來源)
- [4. 兩個獨立高斯分量：怎麼分配失真](#4-兩個獨立高斯分量怎麼分配失真)
- [5. 注水直覺（反向注水）](#5-注水直覺反向注水)
- [6. 轉換編碼](#6-轉換編碼)
- [7. 正交矩陣：保持能量和距離](#7-正交矩陣保持能量和距離)
- [8. 特徵值分解與去相關](#8-特徵值分解與去相關)
- [9. KLT（Karhunen–Loève 轉換）](#9-kltkarhunenloève-轉換)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 04:14](https://youtu.be/9ZcYlFYqAhU?t=254) 延續上一講，學一個新技術：**轉換編碼**（transform coding）。

| 主題 | 課本 |
|---|---|
| 高斯率失真回顧、推廣到相關來源 | §10.3.2 |
| 兩個獨立高斯：注水直覺 | §10.3.3 |
| 轉換編碼、正交轉換、KLT | 課本無專節 |

---

## 1. 小考檢討

### 1.1 聯合熵與互資訊

[▶ 00:05](https://youtu.be/9ZcYlFYqAhU?t=5) 直接套公式（`slide_13_2023.pdf`）：

| $P(X,Y)$ | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | 0.5 | 0 |
| $X=1$ | 0.25 | 0.25 |

$$H(X,Y)=0.5\log2+2\times0.25\log4=1.5,\qquad I(X;Y)=h_b(0.5)+h_b(0.75)-1.5\approx1+0.811-1.5=0.31.$$

### 1.2 $\{0,1,2\}$ 均勻來源、MSE

[▶ 00:45](https://youtu.be/9ZcYlFYqAhU?t=45)

- $R(D=0)=H(X)=\log_23$：失真 0 就是無損，算熵。
- $R(D=1)=\mathbf 0$ [▶ 00:45](https://youtu.be/9ZcYlFYqAhU?t=45)：不用算！**永遠送 1**：對任何符號 0、1、2，和 1 的平方誤差都 $\le1$ [▶ 01:19](https://youtu.be/9ZcYlFYqAhU?t=79)。解碼器永遠輸出 1 就好，不用傳任何東西。

【口頭】[▶ 01:52](https://youtu.be/9ZcYlFYqAhU?t=112) 這是要讓大家理解概念，不必每次都做複雜的數學。

### 1.3 $\mathrm{Ber}(1/2)$、Hamming：率失真定理在說什麼

[▶ 01:52](https://youtu.be/9ZcYlFYqAhU?t=112) $R(D)=1-h_b(D)$。哪些對？[▶ 02:28](https://youtu.be/9ZcYlFYqAhU?t=148)

| 敘述 | 對錯 |
|---|---|
| 存在大區塊方案，失真 $D$、率 $<1-h_b(D)$ | ✗：不能壓得比 $R(D)$ 更少 |
| 存在大區塊方案，失真 $D$、率 $>1-h_b(D)$ | ✓ |
| 存在大區塊方案，失真 $D$、率**任意接近** $1-h_b(D)$ | ✓ [▶ 03:01](https://youtu.be/9ZcYlFYqAhU?t=181)（和熵一樣，課堂沒證但更強的敘述） |
| 存在**一次一個符號**的方案，率任意接近 $1-h_b(D)$ | ✗ [▶ 03:40](https://youtu.be/9ZcYlFYqAhU?t=220) |

[▶ 03:01](https://youtu.be/9ZcYlFYqAhU?t=181) **大區塊**很重要：Tsachy 的球體覆蓋論證要高維才會重疊很少。熵也一樣，不是說逐符號就能做到，而是存在夠大的區塊。

---

## 2. 回顧：高斯的率失真函數

### 2.1 率失真定理

[▶ 04:53](https://youtu.be/9ZcYlFYqAhU?t=293) $X_1,\dots,X_n$ iid：

$$R(D)=\min_{P_{Y\mid X}:\ \mathbb{E}d(X,Y)\le D}I(X;Y).$$

[▶ 05:27](https://youtu.be/9ZcYlFYqAhU?t=327) 最小化是在所有聯合分布 $P_{X,Y}$ 上，但 $P_X$ 是給定的（來源），所以實際上是在 $P_{Y\mid X}$ 上 [▶ 05:27](https://youtu.be/9ZcYlFYqAhU?t=327)。[▶ 06:03](https://youtu.be/9ZcYlFYqAhU?t=363) 另外：資料 iid，失真是**逐符號**的（$n$ 元組的失真是各分量失真的平均）。

### 2.2 高斯、MSE

[▶ 06:40](https://youtu.be/9ZcYlFYqAhU?t=400) 再強調：談 $R(D)$ 一定要問**什麼來源、什麼失真** [▶ 07:13](https://youtu.be/9ZcYlFYqAhU?t=433)。$X\sim\mathcal N(0,\sigma^2)$，MSE：

$$R_G(\sigma^2,D)=\begin{cases}\frac12\log\frac{\sigma^2}D,&0\le D\le\sigma^2,\\0,&D>\sigma^2,\end{cases}\qquad\text{也寫成}\quad\left(\frac12\log\frac{\sigma^2}D\right)^+,$$

其中 $(x)^+=\max(0,x)$ [▶ 11:04](https://youtu.be/9ZcYlFYqAhU?t=664)。

[▶ 07:45](https://youtu.be/9ZcYlFYqAhU?t=465) **意思**：

- 允許的失真比變異數還大，就不用傳任何東西：永遠送 0，$\mathbb{E}(X-0)^2=\sigma^2\le D$ [▶ 08:39](https://youtu.be/9ZcYlFYqAhU?t=519)。
- 失真比變異數小，就要聰明地選碼本；最好是 $\frac12\log\frac{\sigma^2}D$ [▶ 09:32](https://youtu.be/9ZcYlFYqAhU?t=572)。
- 另一個角度 [▶ 09:32](https://youtu.be/9ZcYlFYqAhU?t=572)：**變異數小的來源用比較少的位元**。資料很集中，允許大一點失真時就能丟掉很多資訊 [▶ 10:19](https://youtu.be/9ZcYlFYqAhU?t=619)。

[▶ 10:19](https://youtu.be/9ZcYlFYqAhU?t=619) 記號：$R(D)$ 有時寫成 $R(X,D)$ 強調來源；高斯寫 $R_G(\sigma^2,D)$。

### 2.3 實際 vs. 理論

[▶ 11:40](https://youtu.be/9ZcYlFYqAhU?t=700)（第 11 集 notebook 的圖）$\mathcal N(0,1)$：橫軸率、縱軸 MSE。

- **紅線**：理論最佳 $D(R)=\sigma^22^{-2R}$（講者說投影片寫錯了，應該是 $\sigma^2/D=2^{2R}$）[▶ 13:33](https://youtu.be/9ZcYlFYqAhU?t=813)。
- **藍點**：用 k-means（廣義 Lloyd）做 2 維向量量化 [▶ 12:53](https://youtu.be/9ZcYlFYqAhU?t=773)。

[▶ 13:33](https://youtu.be/9ZcYlFYqAhU?t=813) 紅線是任何方案、任意大區塊能做到的最好；只用 2 維向量量化已經能到藍點。看應用，也許這個實用方案就夠了，再往紅線靠可能要付很大的複雜度代價。

### 2.4 經驗法則

[▶ 14:07](https://youtu.be/9ZcYlFYqAhU?t=847)

> **在給定的失真水準下，變異數大的分量要分配比較多位元。**（變異數大，要更多碼本點才能涵蓋到同樣失真。）

---

## 3. 率失真定理推廣到相關來源

[▶ 15:48](https://youtu.be/9ZcYlFYqAhU?t=948) 有損壓縮框架：$X_1,\dots,X_k$ → 編碼成碼本索引 → $R=\frac{\log N}k$ 位元／符號 → 解碼成 $\hat X_1,\dots,\hat X_k$ [▶ 16:24](https://youtu.be/9ZcYlFYqAhU?t=984)。

[▶ 17:02](https://youtu.be/9ZcYlFYqAhU?t=1022) 真實資料不是 iid。以下不證（要證明修 EE376）[▶ 17:37](https://youtu.be/9ZcYlFYqAhU?t=1057)：

1. **$n$ 元組版**：對任意分布的 $X^n$（不假設 iid），
$$R(X^n,D)=\min_{P_{\hat X^n\mid X^n}:\ \mathbb{E}d(X^n,\hat X^n)\le D}\frac1nI(X^n;\hat X^n).$$
（$\frac1n$ 依投影片 `slide_13_2023.pdf`；口頭沒唸出來。這樣 $R(X^n,D)$ 就是每符號的率。）
最小化在 $(X^n,\hat X^n)$ 的聯合分布上 [▶ 18:15](https://youtu.be/9ZcYlFYqAhU?t=1095)。並不明顯 Shannon 定理能推廣到這裡，但可以。它是熵 $H(X^n)$ 的類比 [▶ 18:57](https://youtu.be/9ZcYlFYqAhU?t=1137)。
2. **平穩隨機過程** $\mathbf X=(X_1,X_2,\dots)$ [▶ 19:45](https://youtu.be/9ZcYlFYqAhU?t=1185)：
$$R(\mathbf X,D)=\lim_{n\to\infty}R(X^n,D),$$
是熵率的類比 [▶ 20:20](https://youtu.be/9ZcYlFYqAhU?t=1220)。對平穩來源這個極限存在，是用任意大的區塊時能做到的最好 [▶ 20:59](https://youtu.be/9ZcYlFYqAhU?t=1259)。

[▶ 21:34](https://youtu.be/9ZcYlFYqAhU?t=1294) 這個量實務上很難算，但看一個特定例子很有直覺。

---

## 4. 兩個獨立高斯分量：怎麼分配失真

### 4.1 設定

[▶ 22:09](https://youtu.be/9ZcYlFYqAhU?t=1329) 區塊大小 $k=2$：$X_1\sim\mathcal N(0,\sigma_1^2)$、$X_2\sim\mathcal N(0,\sigma_2^2)$，**先假設獨立**。每次取一個 $X_1$、一個 $X_2$ 湊成二維向量，有損傳送，重複 [▶ 22:44](https://youtu.be/9ZcYlFYqAhU?t=1364)。

### 4.2 可以拆成兩個獨立問題

[▶ 23:16](https://youtu.be/9ZcYlFYqAhU?t=1396) 可以證明（展開互資訊即可）[▶ 25:06](https://youtu.be/9ZcYlFYqAhU?t=1506)：

$$R_G\left(\sigma_1^2,\sigma_2^2,D\right)=\min_{\frac{D_1+D_2}2\le D}\ \frac12\left[R_G(\sigma_1^2,D_1)+R_G(\sigma_2^2,D_2)\right].$$

[▶ 23:48](https://youtu.be/9ZcYlFYqAhU?t=1428) 意思：可以**分別**有損壓縮兩個分量，給第一個失真 $D_1$、第二個失真 $D_2$，只要**平均失真** $\le D$ [▶ 24:27](https://youtu.be/9ZcYlFYqAhU?t=1467)。問題是 $D_1$、$D_2$ 怎麼分 [▶ 25:06](https://youtu.be/9ZcYlFYqAhU?t=1506)。

代入 [▶ 25:43](https://youtu.be/9ZcYlFYqAhU?t=1543)：

$$\min_{\frac{D_1+D_2}2\le D}\ \frac12\left[\left(\frac12\log\frac{\sigma_1^2}{D_1}\right)^++\left(\frac12\log\frac{\sigma_2^2}{D_2}\right)^+\right].$$

[▶ 26:23](https://youtu.be/9ZcYlFYqAhU?t=1583) 上過凸最佳化的話，這用 **KKT 條件**很容易解；沒上過也沒關係，先看直覺 [▶ 27:05](https://youtu.be/9ZcYlFYqAhU?t=1625)。

### 4.3 直覺【課堂討論】

不失一般性設 $\sigma_1<\sigma_2$ [▶ 27:05](https://youtu.be/9ZcYlFYqAhU?t=1625)。

**問一：該給第一個分量 $D_1>\sigma_1^2$ 的失真嗎？** [▶ 27:48](https://youtu.be/9ZcYlFYqAhU?t=1668)

學生答 [▶ 28:28](https://youtu.be/9ZcYlFYqAhU?t=1708)：$D_1\ge\sigma_1^2$ 時左邊那項已經是 0；多給 $D_1$ 只是從 $D_2$ 拿走失真，右邊那項就變大。講者：對，**多給的失真是浪費**，不會讓目標函數變小 [▶ 29:09](https://youtu.be/9ZcYlFYqAhU?t=1749)。若允許的失真已經大於變異數，已經是 0 位元了，何必從另一個分量拿失真過來？[▶ 29:43](https://youtu.be/9ZcYlFYqAhU?t=1783) 所以**不應該**。

**問二：$D_1>\sigma_1^2$ 時，第一個分量用幾位元？** [▶ 30:16](https://youtu.be/9ZcYlFYqAhU?t=1816) 學生答 **0** [▶ 30:59](https://youtu.be/9ZcYlFYqAhU?t=1859)。不可能比 0 更少。

**問三：$D\ge\frac{\sigma_1^2+\sigma_2^2}2$ 時，率是多少？** [▶ 31:37](https://youtu.be/9ZcYlFYqAhU?t=1897) 三四個人答 **0** [▶ 32:15](https://youtu.be/9ZcYlFYqAhU?t=1935)。給第一個分量 $\sigma_1^2$、第二個 $\sigma_2^2$，平均正好是 $\frac{\sigma_1^2+\sigma_2^2}2$，兩個都是 0 位元 [▶ 32:47](https://youtu.be/9ZcYlFYqAhU?t=1967)。失真高到某個量後，什麼都不送就夠了。

### 4.4 解答

[▶ 34:01](https://youtu.be/9ZcYlFYqAhU?t=2041) 把率失真曲線用參數 $\theta$ 表示：

$$D_i=\min\left(\theta,\ \sigma_i^2\right),\qquad\text{選 }\theta\text{ 使 }\frac{D_1+D_2}2=D,$$

（最佳解時不等式取等號 [▶ 35:18](https://youtu.be/9ZcYlFYqAhU?t=2118)），再代回 $R=\frac12(R_1+R_2)$ [▶ 35:51](https://youtu.be/9ZcYlFYqAhU?t=2151)。$\theta$ 就是 Lagrange 乘數。

[▶ 36:25](https://youtu.be/9ZcYlFYqAhU?t=2185) 解讀：

- $D_1$ 永遠不超過 $\sigma_1^2$、$D_2$ 永遠不超過 $\sigma_2^2$（剛剛的直覺）。
- **新的直覺**（從精確解來的）[▶ 37:31](https://youtu.be/9ZcYlFYqAhU?t=2251)：若平均分配失真後，兩個都還在各自的變異數以下，就**平均分**：$D_1=D_2=\theta$。不是照變異數比例分、也不是反比例分，就是一樣多 [▶ 37:31](https://youtu.be/9ZcYlFYqAhU?t=2251)。

【課本補充】§10.3.3 Theorem 10.3.3（書頁 312–315）處理 $m$ 個獨立高斯：
$$R(D)=\sum_{i=1}^m\frac12\log\frac{\sigma_i^2}{D_i},\qquad D_i=\begin{cases}\lambda,&\lambda<\sigma_i^2\\\sigma_i^2,&\lambda\ge\sigma_i^2\end{cases},\quad\sum_iD_i=D.$$
課本叫它**反向注水**（reverse water-filling），用 KKT 推出。（課本的 $D$ 是總失真，本課的 $D$ 是平均失真，差一個除以 $m$。）

---

## 5. 注水直覺（反向注水）

[▶ 38:59](https://youtu.be/9ZcYlFYqAhU?t=2339) KKT 的解在很多地方出現，大家想出一個很直覺的看法：**注水**（water-filling）。

畫法 [▶ 40:03](https://youtu.be/9ZcYlFYqAhU?t=2403)：兩個分量是兩個杯子，杯子高度是 $\sigma_1^2$、$\sigma_2^2$。往杯子裡倒「失真」這種水。

| 情況 | 條件 | 失真分配 | 率 |
|---|---|---|---|
| 1 | $D\le\sigma_1^2$（所以也 $<\sigma_2^2$）[▶ 40:46](https://youtu.be/9ZcYlFYqAhU?t=2446) | $D_1=D_2=D$（水位一樣高）[▶ 41:22](https://youtu.be/9ZcYlFYqAhU?t=2482) | $\frac12\left[\frac12\log\frac{\sigma_1^2}D+\frac12\log\frac{\sigma_2^2}D\right]$ [▶ 41:53](https://youtu.be/9ZcYlFYqAhU?t=2513) |
| 2 | $\sigma_1^2<D<\frac{\sigma_1^2+\sigma_2^2}2$ [▶ 43:28](https://youtu.be/9ZcYlFYqAhU?t=2608) | $D_1=\sigma_1^2$（第一杯滿了），$D_2=2D-\sigma_1^2$（溢出來的倒進第二杯）[▶ 44:04](https://youtu.be/9ZcYlFYqAhU?t=2644) | $\frac12\left[0+\frac12\log\frac{\sigma_2^2}{2D-\sigma_1^2}\right]$ [▶ 44:35](https://youtu.be/9ZcYlFYqAhU?t=2675) |
| 3 | $D\ge\frac{\sigma_1^2+\sigma_2^2}2$ [▶ 46:26](https://youtu.be/9ZcYlFYqAhU?t=2786) | $D_1=\sigma_1^2$、$D_2=\sigma_2^2$，兩杯都滿，多的失真用不到 | 0 [▶ 47:07](https://youtu.be/9ZcYlFYqAhU?t=2827) |

[▶ 42:37](https://youtu.be/9ZcYlFYqAhU?t=2557) 比喻：兩個杯子中間沒隔板時，倒進去的水會等高（情況 1）。第一杯滿了，溢出來的就流到第二杯（情況 2）[▶ 44:04](https://youtu.be/9ZcYlFYqAhU?t=2644)。最後第二杯也滿了（情況 3）[▶ 47:07](https://youtu.be/9ZcYlFYqAhU?t=2827)。

> ⚠️ 逐字稿缺字：[▶ 45:54](https://youtu.be/9ZcYlFYqAhU?t=2754) 學生指出情況 2 的率公式裡減號那裡應該是 $\sigma_2$（講者寫錯了）；[▶ 48:15](https://youtu.be/9ZcYlFYqAhU?t=2895) 另一位學生指出情況 2 的上界應為 $\frac{\sigma_1^2+\sigma_2^2}2$ 而不是 $\sigma_2^2$。講者都更正了，並說講義可能也要改。筆記已照更正後寫。

[▶ 45:19](https://youtu.be/9ZcYlFYqAhU?t=2719) 情況 2 的意思：**變異數小的分量給小失真（就是它的變異數）**，多出來的失真給變異數大的分量。[▶ 47:39](https://youtu.be/9ZcYlFYqAhU?t=2859) 注意情況 3 的門檻不是 $\max(\sigma_1^2,\sigma_2^2)$，而是平均，會比最大值低。情況 1 的那個共同水位就是式子裡的 $\theta$ [▶ 47:39](https://youtu.be/9ZcYlFYqAhU?t=2859)。

[▶ 49:19](https://youtu.be/9ZcYlFYqAhU?t=2959) 總結：在給定失真水準下，**變異數大的分量分配比較多位元**（因為它能容忍較大失真）[▶ 50:03](https://youtu.be/9ZcYlFYqAhU?t=3003)。這以各種方式一再出現。

> 以下**不是逐字稿內容**，是代數字的例子：$\sigma_1^2=1$、$\sigma_2^2=4$。
> - $D=0.5$（情況 1）：$D_1=D_2=0.5$，$R=\frac12\left[\frac12\log2+\frac12\log8\right]=\frac12[0.5+1.5]=1$ 位元／符號。
> - $D=2$（情況 2，$1<2<2.5$）：$D_1=1$、$D_2=3$，$R=\frac12\left[0+\frac12\log\frac43\right]\approx0.104$。
> - $D\ge2.5$（情況 3）：$R=0$。
> 對照：若硬把 $D=2$ 平均分成 $D_1=D_2=2$，第一個分量多給的 1 單位失真完全浪費，$R=\frac12\cdot\frac12\log2=0.25$，比最佳的 0.104 多一倍以上。

### 5.1 小結

[▶ 50:51](https://youtu.be/9ZcYlFYqAhU?t=3051)

- 不相關的高斯：可以用注水直覺**選擇性地**分配位元給不同分量。
- [▶ 51:30](https://youtu.be/9ZcYlFYqAhU?t=3090) 前面用到 Shannon 定理的地方，就是 $\frac12\log\frac{\sigma^2}D$ 來自互資訊。
- [▶ 51:30](https://youtu.be/9ZcYlFYqAhU?t=3090) 更一般地，**相關的**高斯過程也能優美地推廣：高斯有很好的性質，能去相關；再加幾步就能處理高維相關高斯（講義有直覺）[▶ 52:08](https://youtu.be/9ZcYlFYqAhU?t=3128)。
- 但實際上沒有高斯，只有**相關的非高斯**來源，需要比注水更多的東西：**轉換編碼** [▶ 52:41](https://youtu.be/9ZcYlFYqAhU?t=3161)。

---

## 6. 轉換編碼

### 6.1 想法

[▶ 52:41](https://youtu.be/9ZcYlFYqAhU?t=3161) 講者自己的理解方式：

> **把來源轉換到另一個域，讓分量去相關、而且變異數各不相同；然後在轉換域裡用注水直覺選擇性地分配位元。** [▶ 53:19](https://youtu.be/9ZcYlFYqAhU?t=3199)

### 6.2 流程

[▶ 53:53](https://youtu.be/9ZcYlFYqAhU?t=3233)

```
X̄ (k 維) ──[T]──> Ȳ ──[編碼]──> 位元 ──[解碼]──> Ȳ̂ ──[T⁻¹]──> X̄̂
```

只是在編碼前加一個**轉換** $T$，解碼後加 $T^{-1}$ [▶ 55:07](https://youtu.be/9ZcYlFYqAhU?t=3307)；中間照舊做純量量化、向量量化，什麼都行。

- 本課先假設 $T$ **線性**：$\bar Y=T\bar X$，$T$ 是 $k\times k$ 矩陣 [▶ 56:16](https://youtu.be/9ZcYlFYqAhU?t=3376)。
- 【口頭】[▶ 55:42](https://youtu.be/9ZcYlFYqAhU?t=3342) 熟機器學習的人知道 $T$ 不必是線性的，可以是很複雜的大型神經網路；第 16 集學習式影像壓縮會看到學出來的轉換。
- $T$ 要**可逆**，才能從 $Y$ 還原 $X$ [▶ 56:53](https://youtu.be/9ZcYlFYqAhU?t=3413)。（非線性時不一定是精確的反函數，但效果不錯 [▶ 59:39](https://youtu.be/9ZcYlFYqAhU?t=3579)。）

### 6.3 為什麼要轉換

[▶ 57:25](https://youtu.be/9ZcYlFYqAhU?t=3445)

1. **去相關**：$X$ 可能相關，$Y$ 可以去相關。去相關讓量化更有效率：原本可能要很大的向量量化器，現在用簡單的純量量化器就能達到類似壓縮，降低複雜度 [▶ 57:25](https://youtu.be/9ZcYlFYqAhU?t=3445)。
2. **能量集中**（energy compaction）[▶ 57:59](https://youtu.be/9ZcYlFYqAhU?t=3479)：希望第一個分量裝比較多「資訊」（能量），第二個比較少。就像高斯例子：一個分量很重要要保留，另一個或許可以丟掉。這樣就能給重要的分量更多位元（更少失真），給不重要的更少 [▶ 58:36](https://youtu.be/9ZcYlFYqAhU?t=3516)。這就是**偷到位元**的方法。

[▶ 59:08](https://youtu.be/9ZcYlFYqAhU?t=3548) 對應到高斯：變異數大的分量比較難編、比較重要，多花位元；變異數很小的幾乎是常數，不用花位元。這兩個性質是「最好有」，不是硬性要求 [▶ 59:39](https://youtu.be/9ZcYlFYqAhU?t=3579)。

[▶ 1:00:14](https://youtu.be/9ZcYlFYqAhU?t=3614) 再進一步假設：$T$ 是**正交矩陣**。

---

## 7. 正交矩陣：保持能量和距離

[▶ 1:00:53](https://youtu.be/9ZcYlFYqAhU?t=3653)（線性代數複習；沒背景的人可以找助教要資料）

$y=Ax$。方陣 $A$ 稱為**正交矩陣**（orthonormal，記作 $U$），若

$$U^TU=I.$$

### 7.1 保持能量

[▶ 1:02:01](https://youtu.be/9ZcYlFYqAhU?t=3721) 歐氏範數的平方叫**能量**：

$$\|y\|^2=y^Ty=x^TU^TUx=x^Tx=\|x\|^2,\qquad\text{即 }y_1^2+\cdots+y_k^2=x_1^2+\cdots+x_k^2.$$

[▶ 1:03:09](https://youtu.be/9ZcYlFYqAhU?t=3789) 熟訊號處理的人知道 Fourier 轉換的 **Parseval 定理**，這只是它的特例。轉換域的能量 = 原本的能量。

### 7.2 保持歐氏距離

[▶ 1:03:44](https://youtu.be/9ZcYlFYqAhU?t=3824) $y_1=Ux_1$、$y_2=Ux_2$：

$$\|y_1-y_2\|^2=(x_1-x_2)^TU^TU(x_1-x_2)=\|x_1-x_2\|^2.$$

[▶ 1:04:26](https://youtu.be/9ZcYlFYqAhU?t=3866) **很酷**：用 MSE 失真時，轉換域的期望失真 = 原始域的期望失真。所以可以把轉換域的符號當成要壓的東西，盡力壓好，結果原封不動轉回原始域 [▶ 1:05:07](https://youtu.be/9ZcYlFYqAhU?t=3907)。這也是很多理論工作用 MSE 的原因之一。

---

## 8. 特徵值分解與去相關

### 8.1 特徵值分解

[▶ 1:05:07](https://youtu.be/9ZcYlFYqAhU?t=3907) 對稱矩陣 $A$ 可以分解成

$$A=U\Lambda U^T,$$

$U$ 正交，$\Lambda$ 是對角矩陣 [▶ 1:05:55](https://youtu.be/9ZcYlFYqAhU?t=3955)。$U$ 的各行是 $A$ 的正規化**特徵向量** $u_1,\dots,u_n$（$Au_i=\lambda_iu_i$，乘上矩陣只會縮放），$\Lambda$ 的對角線是對應的**特徵值** [▶ 1:06:36](https://youtu.be/9ZcYlFYqAhU?t=3996)、[▶ 1:07:18](https://youtu.be/9ZcYlFYqAhU?t=4038)。

### 8.2 用 $U^T$ 當轉換就能去相關

[▶ 1:07:54](https://youtu.be/9ZcYlFYqAhU?t=4074) $X$ 零平均，**共變異數矩陣** $\Sigma_X=\mathbb{E}[XX^T]$ [▶ 1:08:38](https://youtu.be/9ZcYlFYqAhU?t=4118)。分解 $\Sigma_X=U\Lambda U^T$，取 $Y=U^TX$ [▶ 1:09:17](https://youtu.be/9ZcYlFYqAhU?t=4157)：

$$
\begin{aligned}
\Sigma_Y=\mathbb{E}[YY^T]&=\mathbb{E}\left[U^TXX^TU\right]\\
&=U^T\,\mathbb{E}[XX^T]\,U&&(U\text{ 是常數，期望值線性})\\
&=U^T\Sigma_XU=U^TU\Lambda U^TU=\Lambda.
\end{aligned}
$$

[▶ 1:11:04](https://youtu.be/9ZcYlFYqAhU?t=4264) $\Sigma_Y=\mathrm{diag}(\lambda_1,\dots,\lambda_n)$：**$Y$ 的分量完全不相關**。這個轉換滿足第一個要求（去相關）[▶ 1:11:38](https://youtu.be/9ZcYlFYqAhU?t=4298)。

---

## 9. KLT（Karhunen–Loève 轉換）

### 9.1 定義與最佳性

[▶ 1:12:47](https://youtu.be/9ZcYlFYqAhU?t=4367) 剛剛的轉換有名字：**Karhunen–Loève 轉換**（KLT），訊號處理裡很有名 [▶ 1:12:47](https://youtu.be/9ZcYlFYqAhU?t=4367)。

- 線性（乘一個矩陣）、以特徵值為基礎（算共變異數矩陣的特徵分解）。
- **對給定的共變異數 $\Sigma$，KLT 是最佳轉換**（不證）[▶ 1:13:20](https://youtu.be/9ZcYlFYqAhU?t=4400)：
  1. 最大程度減少轉換後分量的相關性：輸出完全不相關。
  2. 若 $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$，則 $\mathrm{Var}(y_i)=\lambda_i$ [▶ 1:13:52](https://youtu.be/9ZcYlFYqAhU?t=4432)。

【課堂討論】[▶ 1:14:36](https://youtu.be/9ZcYlFYqAhU?t=4476) 這讓你想到什麼？學生答：**能量集中** [▶ 1:14:36](https://youtu.be/9ZcYlFYqAhU?t=4476)。$n$ 個分量有 $n$ 個不同變異數，而且**盡可能分散開來** [▶ 1:15:07](https://youtu.be/9ZcYlFYqAhU?t=4507)。講者（「在想怎麼講得淺一點」）：矩陣乘向量就是旋轉加改變長度；特徵向量是方向不變的那些方向。可以證明，不管用什麼轉換，不相關分量的最大變異數和最小變異數的比，最多就是最大特徵值比最小特徵值，而 KLT 做到了 [▶ 1:15:46](https://youtu.be/9ZcYlFYqAhU?t=4546)。所以它正好給出我們要的能量集中。

【投影片補充】`slide_13_2023.pdf` 有一個去相關的例子（講者說時間不夠，留到下一講）：$X_n=\rho X_{n-1}+\sqrt{1-\rho^2}\,\mathcal N(0,\sigma^2)$、$X_0\sim\mathcal N(0,\sigma^2)$，兩個一組，問 $X$ 的 $2\times2$ 共變異數矩陣、KLT、以及 $Y$ 的共變異數矩陣。

### 9.2 KLT 的實務問題【課堂討論】

[▶ 1:17:38](https://youtu.be/9ZcYlFYqAhU?t=4658) KLT 是最佳的，但實務上有什麼問題？

學生答 [▶ 1:18:24](https://youtu.be/9ZcYlFYqAhU?t=4704)：(1) 特徵分解很貴；(2) 用的是**樣本**共變異數矩陣，不一定準。

講者 [▶ 1:18:58](https://youtu.be/9ZcYlFYqAhU?t=4738)：

1. **轉換依賴資料**：$U$ 不是常數。第一個 $k$ 符號區塊算出一個轉換，下一個區塊又不一樣，每個區塊都得重算、重新套用 [▶ 1:19:31](https://youtu.be/9ZcYlFYqAhU?t=4771)。**這是主要問題**，計算複雜度高很多。
2. $\Sigma_X$ 是經驗估計的，不一定是真的；實務上能繞過，但即使花了這麼多工夫，結果仍是近似 [▶ 1:20:09](https://youtu.be/9ZcYlFYqAhU?t=4809)。

[▶ 1:20:47](https://youtu.be/9ZcYlFYqAhU?t=4847) 下一講：**DFT、DCT、小波**（wavelet）等轉換。它們是**固定的**轉換，對特定資料不一定最佳，但對實際看到的訊號（影像、聲音）相當接近最佳。

---

## 10. 一頁速查表

### 高斯率失真

$$R_G(\sigma^2,D)=\left(\tfrac12\log\tfrac{\sigma^2}D\right)^+,\qquad D(R)=\sigma^22^{-2R}$$

- 經驗法則：變異數大的分量多給位元。

### 推廣

- $n$ 元組：$R(X^n,D)=\min\frac1nI(X^n;\hat X^n)$；平穩過程：$\lim R(X^n,D)$（熵率的類比）。

### 兩個（或 $m$ 個）獨立高斯：反向注水

$$D_i=\min(\theta,\sigma_i^2),\quad\frac1m\sum D_i=D,\quad R=\frac1m\sum_i\left(\frac12\log\frac{\sigma_i^2}{D_i}\right)^+$$

| 情況（$m=2$，$\sigma_1<\sigma_2$） | 分配 |
|---|---|
| $D\le\sigma_1^2$ | 平分 $D_1=D_2=D$ |
| $\sigma_1^2<D<\frac{\sigma_1^2+\sigma_2^2}2$ | $D_1=\sigma_1^2$，$D_2=2D-\sigma_1^2$ |
| $D\ge\frac{\sigma_1^2+\sigma_2^2}2$ | 全部 0 位元 |

**關鍵一步**：$D_i>\sigma_i^2$ 的失真是浪費（率已經 0）；其餘用 KKT 得到等水位。

### 轉換編碼

- 流程：$Y=TX$ → 量化、編碼 → $\hat X=T^{-1}\hat Y$。
- 目的：**去相關**（讓簡單的純量量化夠用）＋**能量集中**（讓注水分配位元有效）。

### 正交轉換 $U^TU=I$

- $\|Ux\|=\|x\|$（Parseval）；$\|Ux_1-Ux_2\|=\|x_1-x_2\|$ ⇒ 轉換域 MSE = 原始域 MSE。

### KLT

- $\Sigma_X=U\Lambda U^T$，$Y=U^TX$ ⇒ $\Sigma_Y=\Lambda$。**關鍵一步**：$U^T\Sigma_XU=\Lambda$。
- 最佳：完全去相關、變異數 $\lambda_1\ge\cdots$ 最分散。
- 問題：依賴資料，每個區塊要重算；共變異數靠估計 ⇒ 實務用固定轉換（DCT 等）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| KLT 的例子（AR(1) 來源） | 第 14 集開頭 |
| 固定轉換：DFT、DCT、小波 | 第 14 集 |
| 轉換 → 量化 → 熵編碼 | 第 14–15 集（音訊、JPEG） |
| 非線性、學出來的轉換 | 第 16 集學習式影像壓縮 |
| 依分量重要性分配位元 | 第 15 集 JPEG 量化表、第 17 集感知 |

> 以上對應是依播放清單標題和本集預告推估的，做到時再更新。

---

## 附：本集一句話總結

> **高斯來源 $R(D)=\left(\frac12\log\frac{\sigma^2}D\right)^+$，所以變異數小的分量能用較少位元；兩個獨立高斯要分配失真時，最佳解是反向注水：每個分量的失真是 $\min(\theta,\sigma_i^2)$，水位相同、滿了就溢到下一杯。轉換編碼把相關、非高斯的資料轉到一個分量去相關、變異數差異大的域，再照注水的精神分配位元；正交轉換保持能量和 MSE，KLT（共變異數的特徵向量）是最佳的去相關轉換，但它依賴資料、要一直重算，所以實務上改用 DCT 這類固定轉換。**

---

*筆記依據 Pulkit Tandon「Stanford EE274 Data Compression: Theory and Applications（2023 秋）」Lecture 13 錄影逐字稿（人工字幕，1:21:23）、投影片 slide_13_2023、slide_13_2023_ann 與 Cover & Thomas《Elements of Information Theory》2nd ed. §10.3.2–10.3.3 整理。*
