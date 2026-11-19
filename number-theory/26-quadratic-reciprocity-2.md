---
course: Number Theory（2021 秋，線上錄影）
episode: 26
lecture: 2021-10-13 第 2 部
date: 2021-10-13
video: https://youtu.be/2pqaUWxNgbQ
notes: 講者照 Silverman《A Friendly Introduction to Number Theory》；Jones & Jones §7.3–7.4（書頁 123–132，PDF 頁 138–147）：Theorem 7.5、Theorem 7.11、Example 7.9–7.10
---

# 第 26 集 · 二次互反律（下）（Quadratic Reciprocity, part 2） [▶ 影片](https://youtu.be/2pqaUWxNgbQ)

← 上一集：[25-quadratic-reciprocity-1](25-quadratic-reciprocity-1.md) ｜ [總目錄](README.md) ｜ 下一集：[27-rings-and-subrings-1](27-rings-and-subrings-1.md) →

> **課程**：Number Theory（2021 秋）— 第 26 集（2021-10-13 第 2 部）。接續第 25 集的同一堂實體課。
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（11:45，自動字幕）＋ Jones & Jones §7.3–7.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 完成 (55/179)](#1-完成-55179)
- [2. 例：(299/397)](#2-例299397)
- [3. 學生的問題](#3-學生的問題)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

上一集講完二次互反律的敘述，這段（11 分鐘）把兩個計算例子做完，並回答學生的問題。

（第 25 集的定理在這裡簡寫：$p,q$ 相異奇質數，$\left(\frac{-1}p\right) = 1\iff p\equiv1\ (4)$；$\left(\frac2p\right) = 1\iff p\equiv\pm1\ (8)$；$\left(\frac qp\right) = \left(\frac pq\right)$，除非 $p\equiv q\equiv3\ (4)$ 時加負號。）

---

## 1. 完成 (55/179)

[▶ 00:00](https://youtu.be/2pqaUWxNgbQ?t=0)

上一集化到
$$\left(\frac{55}{179}\right) = \left(\frac45\right)\cdot\left(-\left(\frac3{11}\right)\right).$$

化簡到底之後，就變成能直接檢查的小問題：
- **$\left(\frac45\right)$**：$2^2 = 4$，所以是 1。
- **$\left(\frac3{11}\right)$**：$3^2 = 9$ 不行；學生找到 $6^2 = 36\equiv3$（也有 $5^2 = 25\equiv3$），所以是 1。

【課堂討論】學生在找 3 的平方根時，講者說：「不用找全部，只要有一個就行。」而且由上一集的定理，平方根**總是成對**出現 [▶ 01:47](https://youtu.be/2pqaUWxNgbQ?t=107)。

所以
$$\left(\frac{55}{179}\right) = 1\cdot(-1) = -1.$$
**55 不是模 179 的二次剩餘。**（筆記用 Euler 判別法 $55^{89}\bmod179$ 驗證：$-1$。）

【口頭】這也讓人清醒：平方根只有一對。模大質數時隨便猜一個數是平方根，猜中的機率只有 $\frac2{p-1}$。模 5、11 還好 [▶ 02:21](https://youtu.be/2pqaUWxNgbQ?t=141)。

---

## 2. 例：(299/397)

[▶ 03:30](https://youtu.be/2pqaUWxNgbQ?t=210)

【口頭】講者說他身體好些了：「不是我變好了，就是講課讓我覺得好些——也許週一該來學校的。」

**第 1 步：分解**：$299 = 13\cdot23$。
$$\left(\frac{299}{397}\right) = \left(\frac{13}{397}\right)\left(\frac{23}{397}\right).$$

**第 2 步：翻轉**。【課堂討論】「兩個都能翻嗎？」學生：可以（$397\equiv1\ (\mathrm{mod}\ 4)$）。
$$= \left(\frac{397}{13}\right)\left(\frac{397}{23}\right).$$

**第 3 步：上面模下面**：$397 = 30\cdot13+7$、$397 = 17\cdot23+6$。
$$= \left(\frac7{13}\right)\left(\frac6{23}\right).$$

**第 4 步：分別處理**。
- $\left(\frac7{13}\right)$：$13\equiv1\ (\mathrm{mod}\ 4)$，翻轉：$\left(\frac{13}7\right) = \left(\frac67\right)$。$6\equiv-1\ (\mathrm{mod}\ 7)$，$7\equiv3\ (\mathrm{mod}\ 4)$，由 $-1$ 的補充律 $\left(\frac{-1}7\right) = -1$。
- $\left(\frac6{23}\right) = \left(\frac2{23}\right)\left(\frac3{23}\right)$（乘法性）。
  - 【課堂討論】「2 的那條規則要看什麼？」學生：23 模 8。$24\equiv0$，所以 $23\equiv-1\equiv7\ (\mathrm{mod}\ 8)$，$\left(\frac2{23}\right) = 1$ [▶ 05:35](https://youtu.be/2pqaUWxNgbQ?t=335)。
  - $\left(\frac3{23}\right)$：3 和 23 都 $\equiv3\ (\mathrm{mod}\ 4)$，翻轉加負號：$-\left(\frac{23}3\right) = -\left(\frac23\right)$。
  - $\left(\frac23\right)$：模 3 的平方 $1^2 = 1$、$2^2 = 4\equiv1$，2 不是 QR，$= -1$。所以 $\left(\frac3{23}\right) = -(-1) = 1$。

【課堂討論】「負號會抵消對吧？」講者：對 [▶ 07:22](https://youtu.be/2pqaUWxNgbQ?t=442)。（講者途中提到「把上面變成 $-1$ 很好用，因為 $-1$ 有規則」：$23-14\cdot\ldots$ 這類操作，見下面註記。）

**第 5 步：合起來**：
$$\left(\frac{299}{397}\right) = (-1)\cdot(1\cdot1) = -1.$$

**結論**：299 是模 397 的**非剩餘**——不存在整數 $x$ 使 $x^2\equiv299\ (\mathrm{mod}\ 397)$。（筆記用 Euler 判別法驗證：$-1$。）

【口頭】模 3 的二次剩餘「清單只有一個長」：1 和 1 成對 [▶ 07:55](https://youtu.be/2pqaUWxNgbQ?t=475)。

⚠️ 逐字稿缺字：[▶ 06:50](https://youtu.be/2pqaUWxNgbQ?t=410) 這段字幕順序很亂（「minus one over seven three over twenty three wait a minute so minus 23 over 3 … if you subtract 14 from the top you get to minus one」），講者在螢幕上同時處理兩個因子。筆記依每一步的規則重新排出計算順序；「減 14」指的可能是 $\left(\frac{13}{7}\right)$ 化成 $\left(\frac{-1}{7}\right)$（$13-14 = -1$）。

> 【課本補充】Jones & Jones Example 7.9（p. 131）：$\left(\frac{83}{103}\right)$。83、103 都 $\equiv3\ (4)$：$= -\left(\frac{103}{83}\right) = -\left(\frac{20}{83}\right) = -\left(\frac2{83}\right)^2\left(\frac5{83}\right) = -\left(\frac5{83}\right) = -\left(\frac{83}5\right) = -\left(\frac35\right) = -\left(\frac53\right) = -\left(\frac23\right) = 1$。所以 83 是模 103 的二次剩餘（事實上 $83\equiv17^2$）。Example 7.10：$3$ 是模 $p$ 的 QR $\iff p = 2$ 或 $p\equiv\pm1\ (\mathrm{mod}\ 12)$。

---

## 3. 學生的問題

【Q&A】[▶ 02:54](https://youtu.be/2pqaUWxNgbQ?t=174) 學生問：「所以他們有證明一般情況嗎？」講者：「有，證明是一般的。」

【Q&A】[▶ 08:30](https://youtu.be/2pqaUWxNgbQ?t=510) 學生複述規則確認：「$q/p$ 等於 $p/q$，如果 $p\equiv1$ 或 $q\equiv1\ (\mathrm{mod}\ 4)$；如果兩個都 $\equiv3$，就變負的？」講者：對。

【Q&A】[▶ 09:36](https://youtu.be/2pqaUWxNgbQ?t=576) 學生問：$\left(\frac6{23}\right)$ 的 6 是哪來的？講者：因為 397 除以 23 餘 6。

接著學生問為什麼可以這樣換。講者解釋 [▶ 10:12](https://youtu.be/2pqaUWxNgbQ?t=612)：
- 這**從來不是分數**。
- $\left(\frac ap\right)$ 本質上是在問「$x^2\equiv a\ (\mathrm{mod}\ p)$ 有沒有解」：有就是 1、沒有就是 $-1$。
- 在這個問題裡，$a$ 可以換成任何和 $a$ 模 $p$ 同餘的數，答案不變。所以**上面的數總是可以模下面的數化簡**。

【口頭】「這整套思考方式就是很外星。」學生：「你喜歡它？」講者：「對。」[▶ 11:35](https://youtu.be/2pqaUWxNgbQ?t=695)

---

## 4. 一頁速查表

**計算 Legendre 符號的工具箱**
1. 上面模下面化簡：$a\equiv a'\ (\mathrm{mod}\ p)\Rightarrow\left(\frac ap\right) = \left(\frac{a'}p\right)$。
2. 乘法性：分解上面；平方因子 $= 1$。
3. $\left(\frac{-1}p\right)$：$p\equiv1\ (4)$ 時 1，$\equiv3$ 時 $-1$。
4. $\left(\frac2p\right)$：$p\equiv\pm1\ (8)$ 時 1，$\pm3$ 時 $-1$。
5. 奇質數翻轉：都 $\equiv3\ (4)$ 時加負號，否則直接翻。
6. 化到很小時直接列平方檢查。

**本集結果**
- $\left(\frac{55}{179}\right) = \left(\frac45\right)\cdot\left(-\left(\frac3{11}\right)\right) = 1\cdot(-1) = -1$。
- $\left(\frac{299}{397}\right) = \left(\frac7{13}\right)\left(\frac6{23}\right) = \left(\frac{-1}7\right)\cdot\left(\frac2{23}\right)\left(\frac3{23}\right) = (-1)(1)(1) = -1$。

**機率**：模 $p$ 時一個 QR 只有 2 個平方根，亂猜中的機率 $\frac2{p-1}$。

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $\left(\frac{-1}p\right)$ | 第 19–21 集（$p\equiv1\ (4)$ 的質數是兩平方和、在高斯整數中分解） |
| 「上面模下面」的同餘想法 | 第 22 集（單位根）、第 29 集起（商環） |

---

## 附：本集一句話總結

> **用乘法性分解、上面模下面化簡、能翻就翻（兩個都 $\equiv3\ (\mathrm{mod}\ 4)$ 才加負號），再用 $-1$ 和 $2$ 的補充律收尾，就算出 $\left(\frac{55}{179}\right)=-1$、$\left(\frac{299}{397}\right)=-1$——Legendre 符號不是分數，只是在問 $x^2\equiv a\ (\mathrm{mod}\ p)$ 有沒有解。**

---

*筆記依據 James S. Cook「Number Theory」2021-10-13 課堂錄影（下）逐字稿（YouTube 自動字幕，11:45）與 Jones & Jones《Elementary Number Theory》§7.3–7.4 整理。*
