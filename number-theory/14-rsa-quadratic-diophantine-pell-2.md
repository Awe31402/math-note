---
course: Number Theory（2021 秋，線上錄影）
episode: 14
lecture: 2021-09-20 第 2 部
date: 2021-09-20
video: https://youtu.be/oYTGNI8GT5I
notes: 講者照 Silverman《A Friendly Introduction to Number Theory》第 32 章（講者發的掃描講義）；Jones & Jones 沒有 Pell 方程的專節
---

# 第 14 集 · Pell 方程（RSA Encryption, Quadratic Diophantine, Pell's Equation, Part 2） [▶ 影片](https://youtu.be/oYTGNI8GT5I)

← 上一集：[13-rsa-quadratic-diophantine-pell-1](13-rsa-quadratic-diophantine-pell-1.md) ｜ [總目錄](README.md) ｜ 下一集：[15-gaussian-integers-division-algorithm-1](15-gaussian-integers-division-algorithm-1.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 14 集（2021-09-20 第 2 部，接第 13 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（20:19，自動字幕）。講者照 Silverman 的書講，課本 Jones & Jones 沒有這個主題，本集沒有課本補充。
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Pell 方程不是 Pell 的](#1-pell-方程不是-pell-的)
- [2. 定義](#2-定義)
- [3. 從一組解造出新的解](#3-從一組解造出新的解)
- [4. 例子：x² − 3y² = 1](#4-例子x--3y--1)
- [5. Pell 方程定理](#5-pell-方程定理)
- [6. 最小解可能大得嚇人：d = 61](#6-最小解可能大得嚇人d--61)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

**考試範圍** [▶ 00:04](https://youtu.be/oYTGNI8GT5I?t=4)：RSA 在第一次考試範圍內（第一次考試的內容到加密為止）。Pell 方程和之後的內容是**第二次考試**。

**用哪本書** [▶ 02:08](https://youtu.be/oYTGNI8GT5I?t=128)：【口頭】講者照 **Silverman《A Friendly Introduction to Number Theory》第 32 章**講，發了掃描講義。理由：Stillwell 對 Pell 方程的講法「非常技術、很難跟，講什麼對角線、內部的數，沒有圖。我讀了那節，就是不行」。Silverman「一直是我選課本的候選」。

| 主題 | 時間 |
|---|---|
| 歷史 | 00:34 |
| 定義、牛群問題 | 03:40 |
| 從一組解造新解 | 05:10 |
| $x^2-3y^2=1$ | 10:01 |
| Pell 方程定理 | 13:26 |
| $d=61$ | 16:20 |

---

## 1. Pell 方程不是 Pell 的

[▶ 00:34](https://youtu.be/oYTGNI8GT5I?t=34)

【口頭】「好笑的是 Pell 方程不是 Pell 的。」講者說的歷史：

| 時間 | 誰 | 做了什麼 |
|---|---|---|
| 古代 | Archimedes | 牛群問題歸結成一個很可怕的 Pell 方程 |
| 628 年 | 印度數學家（講者說名字以 B 開頭，「我會唸錯」） | 研究 Pell 方程、發展解法 |
| 1150 年 | 另一位印度數學家 Bhaskara | 同上 |
| 1657 年 | William Brouncker（字幕寫「bruckner」） | 在歐洲研究 |

⚠️ 逐字稿缺字：628 年那位講者沒唸出名字。以下**不是逐字稿內容**，是依年代推論的：應是 **Brahmagupta**。

- 【口頭】Silverman 建議**不該叫 Pell 方程**，因為那兩位印度數學家和 Brouncker 都獨立研究過它。⚠️ 逐字稿缺字：字幕把 Silverman 建議的名字寫成「the d cubed equation」，聽不清楚。
- **為什麼叫 Pell** [▶ 03:09](https://youtu.be/oYTGNI8GT5I?t=189)：Euler 不知怎麼以為它出自 **John Pell** 的一本書。「一個有名數學家的命名失誤，就這樣黏住了。」

（第 1 集講者也說是 Euler 叫錯名字的。）

---

## 2. 定義

[▶ 03:40](https://youtu.be/oYTGNI8GT5I?t=220)

> **Pell 方程**（Pell's equation）：
> $$x^2 - dy^2 = 1,$$
> 其中 $d$ **不是完全平方數**。找整數解 $x,y$。

（$d$ 是完全平方數時 $x^2-dy^2 = (x-\sqrt d\,y)(x+\sqrt d\,y)$ 是兩個整數的乘積等於 1，只有平凡解。這一句**不是逐字稿內容**，是補上為什麼要排除完全平方數。）

$(x,y) = (1,0)$ 永遠是解，叫**平凡解**（trivial solution）。我們要找非平凡的。

**Archimedes 的牛群問題** [▶ 04:10](https://youtu.be/oYTGNI8GT5I?t=250)：講者說它歸結成
$$x^2 - 472949\,y^2 = 1$$
（字幕寫「4 000 excuse me 472 949」，見待確認清單）。「我們**不會**解這一題。」

【口頭】1880 年 **Amthor** 找到最小解，講者說「顯然有 41 位數」。

---

## 3. 從一組解造出新的解

[▶ 05:10](https://youtu.be/oYTGNI8GT5I?t=310)

講者：Pell 方程特別有意思的地方是**裡面藏了一個群結構**。

設 $(x_1,y_1)$ 是一組解：$x_1^2 - dy_1^2 = 1$。

**Step 1：因式分解** [▶ 05:43](https://youtu.be/oYTGNI8GT5I?t=343)（用 $\sqrt d$）：
$$1 = x_1^2-dy_1^2 = \left(x_1+y_1\sqrt d\right)\left(x_1-y_1\sqrt d\right).$$

**Step 2：兩邊平方** [▶ 06:13](https://youtu.be/oYTGNI8GT5I?t=373)：
$$1 = \left(x_1+y_1\sqrt d\right)^2\left(x_1-y_1\sqrt d\right)^2.$$
展開：
$$\left(x_1\pm y_1\sqrt d\right)^2 = \left(x_1^2+dy_1^2\right)\pm 2x_1y_1\sqrt d.$$

**Step 3：看出 $(A+B)(A-B)$ 的形式** [▶ 07:56](https://youtu.be/oYTGNI8GT5I?t=476)：令 $A = x_1^2+dy_1^2$、$B = 2x_1y_1\sqrt d$，
$$1 = (A+B)(A-B) = A^2-B^2 = \left(x_1^2+dy_1^2\right)^2 - d\left(2x_1y_1\right)^2.$$

**結論** [▶ 09:31](https://youtu.be/oYTGNI8GT5I?t=571)：令
$$x_2 = x_1^2+dy_1^2,\qquad y_2 = 2x_1y_1,$$
則 $x_2^2-dy_2^2 = 1$。**給我一組解，我就能造出新的一組。**

（白話：$x_2+y_2\sqrt d = \left(x_1+y_1\sqrt d\right)^2$。）

---

## 4. 例子：x² − 3y² = 1

[▶ 10:01](https://youtu.be/oYTGNI8GT5I?t=601)

【課堂討論】講者要學生找一組非平凡解（「試試看」）。試 $(1,1)$ 不行；**$(2,1)$**：
$$2^2 - 3\cdot 1^2 = 4-3 = 1.\ \checkmark$$

【口頭】講者問大家介不介意他超時 10 分鐘。

**用第 3 節的公式** [▶ 12:13](https://youtu.be/oYTGNI8GT5I?t=733)：$x_1=2$、$y_1=1$、$d=3$，
$$x_2 = 2^2+3\cdot 1^2 = 7,\qquad y_2 = 2\cdot 2\cdot 1 = 4.$$

驗算：$7^2-3\cdot 4^2 = 49-48 = 1$。✓

> 以下**不是逐字稿內容**，是再往下做一步：用 $(x_1+y_1\sqrt3)^3 = (2+\sqrt3)(7+4\sqrt3) = 14+8\sqrt3+7\sqrt3+12 = 26+15\sqrt3$，得 $(26,15)$。驗算：$676-3\cdot225 = 676-675 = 1$。✓

---

## 5. Pell 方程定理

[▶ 13:26](https://youtu.be/oYTGNI8GT5I?t=806)

> **Pell 方程定理**：$d$ 不是完全平方數。
> 1. $x^2-dy^2=1$ **一定有正整數解**。
> 2. 設 $(x_1,y_1)$ 是 $x_1$ 最小的那組正整數解。則**每一組**正整數解 $(x_k,y_k)$ 都由
>    $$x_k+y_k\sqrt d = \left(x_1+y_1\sqrt d\right)^k,\qquad k=1,2,3,\dots$$
>    得到。

講者：「用剛才的計算，我們幾乎證完了。」第 3 節證了「從一組解可以生出新的解」；但可能會擔心**漏掉**一些解。

**真正技術性的部分** [▶ 15:19](https://youtu.be/oYTGNI8GT5I?t=919)：證明**存在**一組最小解，以及所有解都是它的次方。

【課堂討論】學生問：如果找到一組解，但不知道它是不是最小的，能往回推嗎？講者：「你不會知道。就像在 $\mathbb{Z}_{500}$ 裡拿到一個不是生成元的元素——它生出很多東西，但不是全部。」（第 10–11 集：非生成元只生成子群。）

---

## 6. 最小解可能大得嚇人：d = 61

[▶ 16:20](https://youtu.be/oYTGNI8GT5I?t=980)

講者的講義（Silverman p. 249）有一張表：各個 $d$ 的最小解。$d=3$ 稍微試一下就找到 $(2,1)$，但請看 **$d=61$**：

$$x^2-61y^2 = 1$$
的最小解是
$$x = 1766319049,\qquad y = 226153980.$$

（講者說「如果我沒抄錯的話」。）

> 以下**不是逐字稿內容**，是驗算：$1766319049^2 = 3119882982860264401$，$61\cdot 226153980^2 = 61\cdot 51145622669840400 = 3119882982860264400$，相差 1。✓

**歷史** [▶ 17:52](https://youtu.be/oYTGNI8GT5I?t=1072)（講者念 Silverman 的書）：

- 1657 年 **Fermat** 向其他數學家挑戰解 $x^2-61y^2=1$，最後有人找到了（講者說這跟 Brouncker 有關）。
- 印度數學家 **Bhaskara** 在 Fermat 之前 500 多年，就用解 $x^2-61y^2=1$ 來示範他的方法。

【口頭】
- 有些 $d$ 不大，第一組非平凡解卻巨大無比。
- 找最小解有方法，但「很技術，你可以輕鬆花一個月的課講它」。它跟**二次型**的研究、**Conway 的「河流」**（Conway's river）有關。講者說看 Stillwell 會發現這個很好懂、很美，值得花時間；但要真正證明存在、找出第一組解，是更大的工程。
- 講者只想讓大家知道 Pell 方程是什麼，以及這個**漂亮的群結構**：「又一次，**代數方法**幫我們找到新的數論解。」

---

## 7. 一頁速查表

**Pell 方程** $x^2-dy^2=1$，$d$ 不是完全平方數。平凡解 $(1,0)$。

**從舊解造新解**：
$$x_2+y_2\sqrt d = \left(x_1+y_1\sqrt d\right)^2\ \Longrightarrow\ x_2 = x_1^2+dy_1^2,\quad y_2 = 2x_1y_1.$$

- **關鍵一步**：$1 = (x_1+y_1\sqrt d)(x_1-y_1\sqrt d)$，兩邊平方後是 $(A+B)(A-B) = A^2-B^2$ 的形式。

**定理**：一定有正整數解；所有正整數解是最小解的次方 $\left(x_1+y_1\sqrt d\right)^k$。

**例子**

| $d$ | 最小解 | 下一組 |
|---|---|---|
| 3 | $(2,1)$ | $(7,4)$，再下一組 $(26,15)$ |
| 61 | $(1766319049,\ 226153980)$ | — |

**歷史**：Archimedes（牛群問題）→ Brahmagupta（628）、Bhaskara（1150）→ Brouncker、Fermat 的挑戰（1657）→ Euler 誤以為是 John Pell 的。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $x+y\sqrt d$ 這種數、它的「範數」$x^2-dy^2$ | 第 15 集起（高斯整數 $a+bi$ 的範數 $a^2+b^2$） |
| 用代數結構解丟番圖方程 | 第 15–22 集 |
| $\mathbb{Z}[\sqrt d]$ 的單位（Pell 方程的解就是單位） | 第 22 集（代數整數） |
| $\mathbb{Q}(\sqrt d)$ 這種體擴張 | 第 40–45 集 |

---

## 附：本集一句話總結

> **Pell 方程 $x^2-dy^2=1$ 其實不是 Pell 的；把 $x_1^2-dy_1^2$ 分解成 $(x_1+y_1\sqrt d)(x_1-y_1\sqrt d)$ 再平方，就從一組解造出新解。所有正整數解都是最小解 $x_1+y_1\sqrt d$ 的次方，但最小解可能大得驚人——$d=61$ 時是十位數。**

---

## ⚠️ 待確認清單

1. [▶ 04:10](https://youtu.be/oYTGNI8GT5I?t=250) 牛群問題的 Pell 方程係數：字幕寫「4 000 excuse me 472 949」。講者念的是 Silverman 講義上的數字，可能是 $472949$，也可能漏了位數。講義看不到，待確認。
2. [▶ 04:40](https://youtu.be/oYTGNI8GT5I?t=280) 「Amthor 1880 年找到最小解，有 41 位數」：講者說「顯然」，是念講義的。本課的來源無法核對。

---

*筆記依據 James S. Cook「Number Theory」2021-09-20 第 2 部錄影逐字稿（YouTube 自動字幕，20:19）整理；講者的主要參考是 Silverman《A Friendly Introduction to Number Theory》第 32 章。*
