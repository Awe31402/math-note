---
course: 統計學（數理統計，數學系）
episode: 22
lecture: Lec22
date: 待補
video: https://youtu.be/O0YRSmOibxI
notes: Hogg 8th ed. §7.2 充分統計量；Theorem 7.2.1 Neyman 因子分解定理（p. 422）
---

# 第 22 集 · Lec22：$U(0,\theta)$ 的 $Y_n$ 是充分統計量；因子分解定理（⇒ 方向） [▶ 影片](https://youtu.be/O0YRSmOibxI)

← 上一集：[21](21-sufficient-statistic-definition-examples.md) ｜ [總目錄](../README.md) ｜ 下一集：[23](23-factorization-proof-examples-conditional-expectation.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 22 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（32:25，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §7.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「充分統計量」→「充溫／聪温統計量」，「順序統計量」→「瞬息統計量」，「因子分解定理」→「分解定理」，「joint」→「join／糾溫」。[▶ 19:52](https://youtu.be/O0YRSmOibxI?t=1192)–[▶ 24:22](https://youtu.be/O0YRSmOibxI?t=1462) 約 4.5 分鐘沒有講課內容（whisper 只輸出「感谢观看」等幻聽字），應是休息時間。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 驗證充分統計量的思路](#1-驗證充分統計量的思路)
- [2. 例：U(0, θ) 的 Yₙ 是充分統計量](#2-例u0-θ-的-yₙ-是充分統計量)
- [3. 用定義驗證的麻煩](#3-用定義驗證的麻煩)
- [4. 因子分解定理](#4-因子分解定理)
- [5. 證明（⇒）](#5-證明)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 例：$X_i$ iid $U(0,\theta)$，$Y_n=\max X_i$ 充分 | §7.2 |
| 因子分解定理（更簡單的判斷法） | Theorem 7.2.1，p. 422 |

---

## 1. 驗證充分統計量的思路

[▶ 00:30](https://youtu.be/O0YRSmOibxI?t=30) 現階段的題型：題目**先給**一個統計量（例如 $Y_n$），要你驗證它是充分統計量。

[▶ 01:02](https://youtu.be/O0YRSmOibxI?t=62) 思路：

- 隨機樣本擁有所有和 $\theta$ 有關的資訊。
- 要證 $Y_n$ 擁有和樣本一樣多的資訊：給定 $Y_n=y$ 後，$X_1,\dots,X_n$ 的條件 pdf 和 $\theta$ 無關。
- 一旦知道 $Y_n$，樣本的分配不再和 $\theta$ 有關，資訊就全跑到 $Y_n$ 裡了。

[▶ 03:07](https://youtu.be/O0YRSmOibxI?t=187) 所有題目都用同一種證法。

---

## 2. 例：U(0, θ) 的 Yₙ 是充分統計量

[▶ 03:07](https://youtu.be/O0YRSmOibxI?t=187) $X_1,\dots,X_n$ iid $U(0,\theta)$。

**Step 1：pdf**（[▶ 03:38](https://youtu.be/O0YRSmOibxI?t=218)）
$$f(x;\theta)=\frac1\theta I(0\le x\le\theta).$$
函數 $\frac1\theta$ 和範圍 $[0,\theta]$ **都**和 $\theta$ 有關，所以 $X$ 有 $\theta$ 的資訊。

**Step 2：樣本的 joint pdf**（[▶ 05:40](https://youtu.be/O0YRSmOibxI?t=340)）。獨立 ⇒ 相乘；同分配 ⇒ 同一個函數；$n$ 個指示函數相乘，每個都是 1 才是 1：
$$f(x_1,\dots,x_n;\theta)=\begin{cases}\dfrac{1}{\theta^n}, & 0\le x_i\le\theta,\ i=1,\dots,n\\ 0, & \text{其他}\end{cases}$$

**Step 3：$Y_n$ 的 pdf**（[▶ 07:45](https://youtu.be/O0YRSmOibxI?t=465)）。用 $f_{Y_n}(y)=n[F(y)]^{n-1}f(y)$，$F(x)=\int_0^x\frac1\theta\,dt=\frac x\theta$：
$$f_{Y_n}(y;\theta)=n\left(\frac y\theta\right)^{n-1}\frac1\theta=\frac{ny^{n-1}}{\theta^n},\quad 0\le y\le\theta.$$
（每個 $X_i\in[0,\theta]$，最大的也在 $[0,\theta]$。）

**Step 4：給定 $Y_n=y$ 時 $X_i$ 的範圍**（[▶ 10:20](https://youtu.be/O0YRSmOibxI?t=620)）

- 條件 pdf 和 $\theta$ 無關，要**兩件事**都成立：函數和 $\theta$ 無關，**範圍也和 $\theta$ 無關**。
- 原本每個 $X_i\in[0,\theta]$。但一旦知道**最大的**是 $y$（$y\le\theta$），每個 $X_i$ 都只能 $\le y$，不可能超過。
- 所以範圍是 $0\le x_i\le y$。

【口頭】[▶ 11:52](https://youtu.be/O0YRSmOibxI?t=712) 範圍如果寫成 $0\le x_i\le\theta$ 就錯了，那樣範圍就跟 $\theta$ 有關。

**Step 5：條件 pdf**（[▶ 12:23](https://youtu.be/O0YRSmOibxI?t=743)）。分母是 $Y_n$ 的 pdf；分子是同時發生——給定 $y$，所有 $x_i\le y$ 時就是樣本的 joint pdf $\frac{1}{\theta^n}$（$y\le\theta$，所以 $x_i\le y$ 也落在 $[0,\theta]$ 裡）：
$$f(\mathbf x\mid Y_n=y)=\frac{1/\theta^n}{ny^{n-1}/\theta^n}=\frac{1}{ny^{n-1}},\quad 0\le x_i\le y.$$

若有某個 $x_i>y$：已知最大的是 $y$，不可能發生，條件 pdf 是 0。

**Step 6：結論**（[▶ 14:59](https://youtu.be/O0YRSmOibxI?t=899)）：

- 範圍 $0\le x_i\le y$：和 $\theta$ 無關。
- 函數 $\frac{1}{ny^{n-1}}$ 或 0：和 $\theta$ 無關。

所以 $Y_n$ 是 $\theta$ 的充分統計量。

【口頭】[▶ 15:31](https://youtu.be/O0YRSmOibxI?t=931) 照定義直接證有點麻煩，要自己做幾次才熟悉。

---

## 3. 用定義驗證的麻煩

[▶ 16:02](https://youtu.be/O0YRSmOibxI?t=962) 這類題目型態很多：給一個統計量，問它是不是充分的。

**麻煩 1：函數的函數**（[▶ 16:32](https://youtu.be/O0YRSmOibxI?t=992)）。已知 $U$ 充分，那 $U+3$、$e^U$、$\cos U$ 呢？每個都要重新找它的 pdf 再驗證一次，非常麻煩。

**麻煩 2：證明「不是」**（[▶ 17:33](https://youtu.be/O0YRSmOibxI?t=1053)）。例如同一題改問最小的 $Y_1$：要找 $Y_1$ 的 pdf（變成 $1-F$），導出條件 pdf 後發現 $\theta$ 消不掉，才能說它**不是**充分統計量。

【口頭】[▶ 18:35](https://youtu.be/O0YRSmOibxI?t=1115) 就像微積分剛學的時候，有時問你函數在某點連續，有時問它是不是不連續、不可微。

想要一個比較簡單的方法 → **因子分解定理**。

---

## 4. 因子分解定理

[▶ 24:22](https://youtu.be/O0YRSmOibxI?t=1462)

【口頭】這定理很好用，所以證明不會那麼簡單。

**為什麼叫「分解」**（[▶ 24:53](https://youtu.be/O0YRSmOibxI?t=1493)）：分解的是 **joint pdf**。用定義要先找統計量的分配、再相除；用這個定理只要把樣本的 joint pdf 拆開，不用找統計量的分配。

> **因子分解定理**（factorization theorem）（課本 Theorem 7.2.1，Neyman，p. 422）：$X_1,\dots,X_n$ 來自 $f(x;\theta)$。統計量 $U=u(X_1,\dots,X_n)$ 是 $\theta$ 的充分統計量
> $$\iff\text{存在 }k_1\ge 0,\ k_2\ge 0,\text{ 使得}$$
> $$f(x_1,\dots,x_n;\theta)=k_1\left(u(x_1,\dots,x_n);\theta\right)\cdot k_2(x_1,\dots,x_n),$$
> 其中 $k_2$ **不含 $\theta$**。

- [▶ 26:54](https://youtu.be/O0YRSmOibxI?t=1614) 是**若且唯若**（if and only if），雙向都成立。
- $k_1$：只透過統計量 $u(\mathbf x)$ 和 $\theta$ 的函數。
- $k_2$：$x_1,\dots,x_n$ 的函數（裡面有沒有 $u$ 都沒關係），**不能有 $\theta$**。
- 函數長什麼樣都可以，**只要存在**就好。

---

## 5. 證明（⇒）

[▶ 28:59](https://youtu.be/O0YRSmOibxI?t=1739) 假設連續型（離散型也可以）。先證比較簡單的方向：**$U$ 充分 ⇒ joint pdf 可以拆**。

**Step 1**：$U$ 充分 ⇒ 給定 $U=u$，樣本的條件 pdf 不含 $\theta$：
$$f(\mathbf x\mid U=u(\mathbf x))=\frac{f(x_1,\dots,x_n;\theta)}{f_U\left(u(\mathbf x);\theta\right)}\quad\text{不依賴 }\theta.$$
（分子、分母各自都有 $\theta$，但 $U$ 充分，相除後消掉。）

**Step 2**（[▶ 30:30](https://youtu.be/O0YRSmOibxI?t=1830)）：把分母乘過去：
$$f(x_1,\dots,x_n;\theta)=\underbrace{f_U\left(u(\mathbf x);\theta\right)}_{k_1(u(\mathbf x);\theta)}\cdot\underbrace{f(\mathbf x\mid U=u(\mathbf x))}_{k_2(\mathbf x)}.$$

- $k_1$：$U$ 的 pdf，是 $u$ 和 $\theta$ 的函數。
- $k_2$：條件 pdf，不含 $\theta$（因為 $U$ 充分）；它是 $\mathbf x$ 的函數（$u$ 也是 $\mathbf x$ 的函數）。
- 兩者都 $\ge 0$。

所以拆得出來。⇒ 方向得證。

反方向（拆得出來 ⇒ 充分）下次證。

---

## 6. 一頁速查表

**$U(0,\theta)$ 的 $Y_n$ 充分**：

- 給定 $Y_n=y$，範圍變成 $0\le x_i\le y$（不是 $\le\theta$）。
- $f(\mathbf x\mid Y_n=y)=\dfrac{1/\theta^n}{ny^{n-1}/\theta^n}=\dfrac{1}{ny^{n-1}}$。
- 函數和範圍都不含 $\theta$。

**充分的兩個條件**：條件 pdf 的**函數**和**範圍**都不依賴 $\theta$。

**因子分解定理**：
$$U\text{ 充分}\iff f(\mathbf x;\theta)=k_1(u(\mathbf x);\theta)\,k_2(\mathbf x),\quad k_2\text{ 不含 }\theta.$$
（⇒）的關鍵一步：$k_1=f_U$，$k_2=$ 條件 pdf。

好處：不用找統計量的分配，只要拆樣本的 joint pdf。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 因子分解定理（⇐） | 下一集證明，並用它判斷各分配的充分統計量 |
| 充分統計量的函數 | 一對一函數仍是充分統計量 |
| $Y_n$ 充分 | $U(0,\theta)$ 的 UMVUE |

---

## 附：本集一句話總結

> **$U(0,\theta)$ 給定 $Y_n=y$ 後，每個 $X_i$ 只能在 $[0,y]$、條件 pdf 是 $\frac{1}{ny^{n-1}}$，都不含 $\theta$，所以 $Y_n$ 充分；用定義驗證很麻煩，改用因子分解定理：$U$ 充分 ⇔ joint pdf 能拆成「$U$ 與 $\theta$ 的函數」乘「不含 $\theta$ 的函數」。**

---

*筆記依據「統計學」Lec22 錄影逐字稿（whisper large-v3-turbo，32:25）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
