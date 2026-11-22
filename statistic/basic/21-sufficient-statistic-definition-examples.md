---
course: 統計學（數理統計，數學系）
episode: 21
lecture: Lec21
date: 待補
video: https://youtu.be/TciSXOFU7Kk
notes: Hogg 8th ed. §7.2 充分統計量（Example 7.2.1 Bernoulli，p. 420；Definition 7.2.1，p. 421）；§7.8 最小充分統計量（p. 455）
---

# 第 21 集 · Lec21：充分統計量（定義、意義、三個例子） [▶ 影片](https://youtu.be/TciSXOFU7Kk)

← 上一集：[20](20-cramer-rao-examples-conditional-pdf.md) ｜ [總目錄](../README.md) ｜ 下一集：[22](22-uniform-max-sufficient-factorization-theorem.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 21 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:07:34，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §7.2、§7.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「充分統計量」→「充溫統計量」，「sufficiency」照錄，「information」照錄（中文「資訊」），「joint」→「join」，「conditional pdf」照錄，「彩券」→「駱駝（樂透）」。開頭 00:00 一段是 whisper 幻聽的重複字，忽略。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 樣本裡有 θ 的資訊](#1-樣本裡有-θ-的資訊)
- [2. 統計量的分配通常含 θ](#2-統計量的分配通常含-θ)
- [3. 給定統計量時，樣本的條件 pdf](#3-給定統計量時樣本的條件-pdf)
- [4. 充分統計量的定義與意義](#4-充分統計量的定義與意義)
- [5. 用機率來理解條件 pdf](#5-用機率來理解條件-pdf)
- [6. 例 1：樣本本身是充分的](#6-例-1樣本本身是充分的)
- [7. 最小充分統計量](#7-最小充分統計量)
- [8. 例 2：順序統計量是充分的](#8-例-2順序統計量是充分的)
- [9. 例 3：Bernoulli，ΣXᵢ 是充分的](#9-例-3bernoulliσxᵢ-是充分的)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/TciSXOFU7Kk?t=0) 統計量很多，要從中找出一種滿足某特性的，叫**充分統計量**（sufficient statistic），具有**充分性**（sufficiency）。「充分」是和**資訊**（information）有關的專業名詞。

| 主題 | 課本 |
|---|---|
| 充分統計量的定義（用條件 pdf） | Definition 7.2.1，p. 421 |
| 例：$(X_1,\dots,X_n)$、順序統計量、Bernoulli 的 $\sum X_i$ | Example 7.2.1，p. 420 |
| 最小充分統計量 | §7.8，p. 455 |

---

## 1. 樣本裡有 θ 的資訊

[▶ 01:35](https://youtu.be/TciSXOFU7Kk?t=95)

- 做統計一定有隨機樣本 $X_1,\dots,X_n$（iid）。**樣本是你唯一掌握得到的東西**。
- [▶ 03:06](https://youtu.be/TciSXOFU7Kk?t=186) 分配 $f(x;\theta)$ 代表一個**母體**（population）。例：交大學生的數學程度——有人很好、有人很差、中間的最多；別的學校分配不同。想知道交大學生的平均程度（$\theta$），就從**交大**這個母體抽，不會跑去別的學校抽。
- [▶ 05:09](https://youtu.be/TciSXOFU7Kk?t=309) 抽出來的樣本一定和 $\theta$ 有關：$\theta$ 通常是中心，pdf 在那附近高，所以大部分樣本落在 $\theta$ 附近。
- [▶ 05:42](https://youtu.be/TciSXOFU7Kk?t=342) 不可能剛好抽到交大第 1 名到第 $n$ 名：隨機樣本照 pdf 抽，pdf 高的地方被抽到的機會大。

【口頭】[▶ 06:44](https://youtu.be/TciSXOFU7Kk?t=404) 樂透頭獎：一百萬人買、每人中獎機率約百萬分之一，就大約有一人中。但同一個人連兩期中頭獎，台灣到現在沒發生過：百萬分之一乘百萬分之一，幾乎不可能。

[▶ 08:16](https://youtu.be/TciSXOFU7Kk?t=496) 結論：**樣本 $X_1,\dots,X_n$ 擁有 $\theta$ 的資訊**。而且你只抽了這 $n$ 個，所以你能擁有的、和 $\theta$ 有關的資訊，**全部都在 $X_1,\dots,X_n$ 裡**，沒有別的。

---

## 2. 統計量的分配通常含 θ

[▶ 09:46](https://youtu.be/TciSXOFU7Kk?t=586) 統計量 $U=u(X_1,\dots,X_n)$：函數裡沒有 $\theta$。但它的**分配**通常有 $\theta$，記 pdf 為 $f_U(u;\theta)$。

- 分配裡沒有 $\theta$ 的統計量沒用，不要。
- [▶ 10:48](https://youtu.be/TciSXOFU7Kk?t=648) 例：$X_i$ iid $N(\mu,\sigma^2)$，$\bar X=\frac1n\sum X_i$ 裡沒有 $\mu,\sigma^2$；但 $\bar X\sim N(\mu,\sigma^2/n)$，分配兩個都有。

---

## 3. 給定統計量時，樣本的條件 pdf

[▶ 11:49](https://youtu.be/TciSXOFU7Kk?t=709) 考慮
$$f(x_1,\dots,x_n\mid U=u;\theta):$$
統計量已經發生、值是 $u$，這時 $X_1,\dots,X_n$ 的（joint）條件 pdf。

照條件 pdf 的定義（[▶ 14:27](https://youtu.be/TciSXOFU7Kk?t=867)）：分母是 $U$ 的 pdf，分子是 $(X_1,\dots,X_n)$ 和 $U$ **同時發生**的 joint pdf。

**分子怎麼算**（[▶ 15:29](https://youtu.be/TciSXOFU7Kk?t=929)）：$U$ 本身就是 $x_1,\dots,x_n$ 的函數。

- 若 $u(x_1,\dots,x_n)\ne u$：$U$ 已經是 $u$，這組 $x$ 不可能發生，交集是空集合，分子是 0。
- 若 $u(x_1,\dots,x_n)=u$：很多點的函數值都是 $u$，這組 $x$ 是其中一點，交集就是這一點，分子＝$f(x_1,\dots,x_n;\theta)$。

$$f(x_1,\dots,x_n\mid U=u)=\begin{cases}\dfrac{f(x_1,\dots,x_n;\theta)}{f_U(u;\theta)}, & u(x_1,\dots,x_n)=u\\ 0, & \text{其他}\end{cases}$$

[▶ 20:34](https://youtu.be/TciSXOFU7Kk?t=1234) 它還是 pdf：對所有滿足 $u(\mathbf x)=u$ 的點積分是 1。

---

## 4. 充分統計量的定義與意義

[▶ 21:36](https://youtu.be/TciSXOFU7Kk?t=1296) 這個條件 pdf 可能和 $\theta$ 有關，也可能無關。關心的是**無關**的情形。

**意義**（[▶ 22:37](https://youtu.be/TciSXOFU7Kk?t=1357)）：

- 原本 $X_1,\dots,X_n$ 的 joint pdf 跟 $\theta$ 有關。
- 一旦知道 $U=u$，條件 pdf 就跟 $\theta$ 無關 ⇒ 這時樣本**不再有任何**和 $\theta$ 有關的資訊。
- [▶ 23:39](https://youtu.be/TciSXOFU7Kk?t=1419) 資訊跑去哪裡？**全部被 $U$ 吸走了**。所以 $U$ 擁有的 $\theta$ 資訊和整個樣本**一樣多**。
- [▶ 25:11](https://youtu.be/TciSXOFU7Kk?t=1511) **為什麼要這樣**：樣本是 $n$ 維，維度太大。找一個維度比較小、資訊一樣多的統計量，當然要它。

> **定義（充分統計量）**（[▶ 26:44](https://youtu.be/TciSXOFU7Kk?t=1604)，課本 Definition 7.2.1，p. 421）：$X_1,\dots,X_n$ 來自 $f(x;\theta)$，$\theta\in\Omega$。統計量 $U=u(X_1,\dots,X_n)$ 若對每個 $u$，條件 pdf
> $$f(x_1,\dots,x_n\mid U=u)$$
> 和它的**定義域**都**不依賴 $\theta$**，就叫 $\theta$ 的**充分統計量**。

【口頭】[▶ 28:15](https://youtu.be/TciSXOFU7Kk?t=1695) 這是點估計裡最終、很重要的觀念。平常做決策（考研究所、選學校）都要蒐集資訊，越多越好。這裡因為你只有一組樣本，所有和 $\theta$ 有關的資訊都在樣本裡；找到一個統計量，知道它的值之後樣本的分配就不再跟 $\theta$ 有關，它就和樣本擁有一樣多的資訊——這就是「充分」。

【課本補充】課本 Definition 7.2.1 的寫法：$\dfrac{f(x_1;\theta)\cdots f(x_n;\theta)}{f_U(u(x_1,\dots,x_n);\theta)}=H(x_1,\dots,x_n)$，其中 $H$ 不依賴 $\theta$。和老師的條件 pdf 版本是同一件事。

---

## 5. 用機率來理解條件 pdf

[▶ 29:48](https://youtu.be/TciSXOFU7Kk?t=1788) 把條件 pdf 想成機率：
$$P(X_1=x_1,\dots,X_n=x_n\mid u(X_1,\dots,X_n)=u).$$

- [▶ 32:26](https://youtu.be/TciSXOFU7Kk?t=1946) 原本 $P(X_1=x_1,\dots,X_n=x_n)=\prod f(x_i;\theta)$，和 $\theta$ 有關。
- [▶ 33:26](https://youtu.be/TciSXOFU7Kk?t=2006) 畫圖：$\theta=\theta_1$ 時 pdf 在某處，$\theta=\theta_2$ 時跑到別處。同一個 $x$，在 $\theta_1$ 下 pdf 可能很高，在 $\theta_2$ 下幾乎是 0。所以 $x$ 發生的機率本來就跟 $\theta$ 有關。
- [▶ 34:58](https://youtu.be/TciSXOFU7Kk?t=2098) $U$ 充分 ⇒ 知道 $U$ 的值後，分配**不再隨 $\theta$ 跑來跑去**，固定了。分配固定，就提供不了任何 $\theta$ 的資訊。

---

## 6. 例 1：樣本本身是充分的

[▶ 36:01](https://youtu.be/TciSXOFU7Kk?t=2161) 取 $U=(X_1,\dots,X_n)$，樣本本身（看成一個 $n$ 維向量，也是統計量）。

【口頭】很簡單，但也很抽象。

給定 $U=(x_1',\dots,x_n')$（[▶ 37:33](https://youtu.be/TciSXOFU7Kk?t=2253)）：

- 分母：$U$ 的 pdf＝樣本在 $(x_1',\dots,x_n')$ 的 joint pdf $f(x_1',\dots,x_n';\theta)$。
- 分子：樣本＝$(x_1,\dots,x_n)$ 且 $U=(x_1',\dots,x_n')$。因為 $U$ 就是樣本：
  - 若 $(x_1,\dots,x_n)=(x_1',\dots,x_n')$（每個分量都相等）：兩件事是同一件，分子＝$f(x_1,\dots,x_n;\theta)$，和分母一樣，比值是 **1**。
  - 若不相等：不可能同時發生，分子是 0，比值是 **0**。

$$f(\mathbf x\mid U=\mathbf x')=\begin{cases}1, & \mathbf x=\mathbf x'\\ 0, & \text{其他}\end{cases}$$

定義域和條件 pdf 都和 $\theta$ 無關 ⇒ **樣本本身是充分統計量**。

[▶ 43:10](https://youtu.be/TciSXOFU7Kk?t=2590) 但我們不要這種：它是 $n$ 維，維度太大。

---

## 7. 最小充分統計量

[▶ 43:40](https://youtu.be/TciSXOFU7Kk?t=2620) 目的：找一個充分統計量，**維度越小越好**。

> **最小充分統計量**（minimal sufficient statistic）：維度最小（smallest dimension）的充分統計量。

- 維度只能是 1、2、3、……，不會是 1.5，所以一定有最小的。
- [▶ 44:41](https://youtu.be/TciSXOFU7Kk?t=2681) 【口頭】這個觀念看起來重要，但本課**用不到**。我們會找另一種有特別名字的充分統計量（後面講），找到它就一定是最小充分的。

【課本補充】課本 §7.8（p. 455）對 minimal sufficient 的正式定義不是用「維度」，而是「它是其他每個充分統計量的函數」。老師用維度來直觀說明。

---

## 8. 例 2：順序統計量是充分的

[▶ 45:41](https://youtu.be/TciSXOFU7Kk?t=2741) 【口頭】例子：班上派三個同學去考學校的微積分。只知道結果有一人第 1 名、一人第 3 名、一人第 5 名，但不知道誰是誰。

- 「甲第 2、乙第 4、丙第 6」的機率？**0**，不可能。
- 「甲第 3、乙第 5、丙第 1」的機率？$>0$，可能。
- 一共有 $3!$ 種可能：甲有 3 種選擇，決定後乙剩 2 種，丙剩 1 種。

[▶ 47:48](https://youtu.be/TciSXOFU7Kk?t=2868) $X_1,\dots,X_n$ 來自**連續**分配（連續 ⇒ 同分機率是 0，名次都不同）。順序統計量 $Y_1<\cdots<Y_n$。

> **命題**：順序統計量 $(Y_1,\dots,Y_n)$ 是充分統計量。

（雖然也是 $n$ 維，但和樣本本身不同。）

給定 $Y_1=y_1,\dots,Y_n=y_n$（[▶ 49:21](https://youtu.be/TciSXOFU7Kk?t=2961)）：

- 可能發生的 $(x_1,\dots,x_n)$：由小排到大剛好是 $(y_1,\dots,y_n)$ 的那些，也就是 $(y_1,\dots,y_n)$ 的**排列**（permutation）。排起來不是它的點不可能發生。
- [▶ 51:55](https://youtu.be/TciSXOFU7Kk?t=3115) 一共 $n!$ 種（$X_1$ 有 $n$ 種選擇、$X_2$ 剩 $n-1$ 種……）。
- [▶ 52:56](https://youtu.be/TciSXOFU7Kk?t=3176) **機會均等**：隨機樣本同分配，誰是最小、誰第二小，機會一樣。（如果知道某同學數學特別強，他第一名的機會比較大；但隨機樣本就像三人程度一樣。）

$$f(\mathbf x\mid Y_1=y_1,\dots,Y_n=y_n)=\begin{cases}\dfrac{1}{n!}, & \mathbf x\text{ 是 }(y_1,\dots,y_n)\text{ 的排列}\\ 0, & \text{其他}\end{cases}$$

定義域和條件 pdf 都和 $\theta$ 無關 ⇒ 充分。

【口頭】[▶ 55:00](https://youtu.be/TciSXOFU7Kk?t=3300) 前兩個例子證法比較特殊，所以先講；它們其實都不重要。其他例子都用同一種證法。

---

## 9. 例 3：Bernoulli，ΣXᵢ 是充分的

[▶ 55:31](https://youtu.be/TciSXOFU7Kk?t=3331) $X_1,\dots,X_n$ iid Bernoulli$(p)$。

**Step 1：樣本的 joint pdf**（[▶ 56:02](https://youtu.be/TciSXOFU7Kk?t=3362)）。獨立 ⇒ 相乘；同分配 ⇒ 都是 $p^x(1-p)^{1-x}$：
$$f(x_1,\dots,x_n;p)=\prod_{i=1}^np^{x_i}(1-p)^{1-x_i}=p^{\sum x_i}(1-p)^{n-\sum x_i},\quad x_i\in\{0,1\}.$$
定義域和 $p$ 無關，但函數和 $p$ 有關 ⇒ 樣本擁有 $p$ 的資訊。

**Step 2：統計量 $Y=\sum X_i$ 的分配**（[▶ 58:39](https://youtu.be/TciSXOFU7Kk?t=3519)）：$Y\sim b(n,p)$（用 mgf 法證，以前證過，要記得）：
$$f_Y(y;p)=\binom ny p^y(1-p)^{n-y},\quad y=0,1,\dots,n.$$

【口頭】[▶ 60:10](https://youtu.be/TciSXOFU7Kk?t=3610) 證過的東西要記得。不知道 $\sum X_i$ 的分配，這題就沒辦法做。

**Step 3：可能發生的點**（[▶ 61:12](https://youtu.be/TciSXOFU7Kk?t=3672)）：給定 $Y=y$，只有 $\sum x_i=y$ 的 $(x_1,\dots,x_n)$ 可能發生；加起來不是 $y$ 的不可能。

**Step 4：條件 pdf**（[▶ 63:16](https://youtu.be/TciSXOFU7Kk?t=3796)）：若 $\sum x_i=y$，分子是樣本的 joint pdf，分母是 $Y$ 的 pdf：
$$\frac{p^{\sum x_i}(1-p)^{n-\sum x_i}}{\binom ny p^y(1-p)^{n-y}}=\frac{p^y(1-p)^{n-y}}{\binom ny p^y(1-p)^{n-y}}=\frac{1}{\binom ny}.$$
和 $p$ 有關的全部消掉。若 $\sum x_i\ne y$，是 0。

$$f(\mathbf x\mid Y=y)=\begin{cases}\dfrac{1}{\binom ny}, & \sum x_i=y\\ 0, & \text{其他}\end{cases}$$

定義域和條件 pdf 都和 $p$ 無關 ⇒ $Y=\sum X_i$ 是 $p$ 的充分統計量（sufficient for $p$）。

（直觀：知道一共 $y$ 次成功後，是哪幾次成功只是 $\binom ny$ 種排法之一、機會均等，跟 $p$ 無關。）

【口頭】[▶ 66:53](https://youtu.be/TciSXOFU7Kk?t=4013) 其他例題證法大概都是這種，要習慣這種方式。

---

## 10. 一頁速查表

**資訊的觀點**：樣本擁有 $\theta$ 的全部資訊。$U$ 充分 ⇔ 知道 $U$ 後，樣本不再有 $\theta$ 的資訊 ⇔ $U$ 和樣本擁有一樣多的資訊。

**定義**：$U$ 充分 ⇔ 對每個 $u$，
$$f(\mathbf x\mid U=u)=\begin{cases}\frac{f(\mathbf x;\theta)}{f_U(u;\theta)}, & u(\mathbf x)=u\\ 0, & \text{其他}\end{cases}$$
和它的定義域都不依賴 $\theta$。

**證充分的步驟**：寫樣本 joint pdf → 求 $U$ 的分配 → 找給定 $U=u$ 時可能的 $\mathbf x$ → 相除，看 $\theta$ 是否消掉。

| 統計量 | 條件 pdf | 充分？ |
|---|---|---|
| 樣本 $(X_1,\dots,X_n)$ | 1 或 0 | ✓（但維度 $n$，太大） |
| 順序統計量（連續分配） | $\frac{1}{n!}$ 或 0 | ✓ |
| Bernoulli 的 $\sum X_i$ | $\frac{1}{\binom ny}$ 或 0 | ✓ |

**最小充分統計量**：維度最小的充分統計量（本課不直接找它）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 充分統計量的定義 | 下一集：因子分解定理（更方便的判斷法） |
| 「另一種名字的充分統計量」 | 完備充分統計量 → Lehmann–Scheffé 找 UMVUE |
| 條件 pdf 不含 $\theta$ | Rao–Blackwell 定理 |

---

## 附：本集一句話總結

> **樣本擁有 $\theta$ 的全部資訊；若給定統計量 $U$ 的值後，樣本的條件 pdf 不再依賴 $\theta$，表示 $U$ 把資訊全吸走了，$U$ 就是充分統計量——樣本本身、順序統計量、Bernoulli 的 $\sum X_i$ 都是，目標是找維度越小越好的充分統計量。**

---

*筆記依據「統計學」Lec21 錄影逐字稿（whisper large-v3-turbo，1:07:34）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
