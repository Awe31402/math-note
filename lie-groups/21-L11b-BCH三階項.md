---
course: Matrix Lie Groups (Spring 2016)
episode: 21
lecture: L11b
date: 2016-04-18（part 2）
video: https://www.youtube.com/watch?v=xVngdQsYL4M
notes: Hall 第 1 版 §3.5（p.74–76）
---

# 第 21 集 · L11b：BCH 的三階項（和一次四階的嘗試） [▶ 影片](https://www.youtube.com/watch?v=xVngdQsYL4M&list=PLBY4G2o7DhF3FS2CaX62eiQWGP9_xdLYs)

← 上一集：[[20-L11a-BCH的計算]] ｜ [總目錄](README.md) ｜ 下一集：[[22-L12a-萬有覆蓋與Lie定理]] →

> **課程**：Matrix Lie Groups（Liberty University，Spring 2016）— 第 21 集，April 18 part 2
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（30:21，自動字幕）＋ Hall《Lie Groups, Lie Algebras, and Representations》第 1 版 §3.5「The Series Form of the BCH Formula」（p.74–76）
> **標記說明**：`【口頭】` 老師口頭補充、課本沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【課本補充】` 課本有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`⚠️ 待確認` 查不清楚，列在最後清單；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 記號與分層原則](#1-記號與分層原則)
- [2. 兩層交換子：1/12 的兩項](#2-兩層交換子112-的兩項)
- [3. 三層交換子：課堂的嘗試](#3-三層交換子課堂的嘗試)
- [4. 三層交換子：完整計算（補充）](#4-三層交換子完整計算補充)
- [5. 課程安排](#5-課程安排)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

接上一集：用

$$
\log(e^Xe^Y) = X + \int_0^1g\left(e^{\operatorname{ad}_X}e^{t\operatorname{ad}_Y}\right)(Y)\,dt,\qquad g(z) = 1 + \tfrac12(z-1) - \tfrac16(z-1)^2 + \tfrac1{12}(z-1)^3 - \cdots
$$

算 BCH 的高階項。

## 1. 記號與分層原則

簡寫 $a = \operatorname{ad}_X$、$b = \operatorname{ad}_Y$、$W = e^ae^{tb} - I$。上一集算出 $W$ 依次數分成

$$
W_1 = a + tb,\quad W_2 = \tfrac12a^2 + tab + \tfrac{t^2}2b^2,\quad W_3 = \tfrac16a^3 + \tfrac t2a^2b + \tfrac{t^2}2ab^2 + \tfrac{t^3}6b^3.
$$

**兩個原則**：
1. 最後作用在 $Y$ 上，**最右邊是 $b$ 的詞都是 0**（$\operatorname{ad}_Y(Y) = 0$）。
2. [▶ 14:24](https://youtu.be/xVngdQsYL4M?t=864) 【口頭】「理解這個展開的方法，就是**一次只看一層巢狀交換子**。分而治之。」$k$ 層交換子只會來自 $g$ 的前 $k$ 項。

## 2. 兩層交換子：1/12 的兩項

[▶ 00:06](https://youtu.be/xVngdQsYL4M?t=6)–[▶ 04:53](https://youtu.be/xVngdQsYL4M?t=293) 全班一起找二次的詞（二層交換子），作用在 $Y$ 上：

**來自 $\frac12W$**：只有 $W_2$ 裡不以 $b$ 結尾的：$\frac12\cdot\frac12a^2 = \frac14a^2$。

**來自 $-\frac16W^2$**：$(W^2)_2 = W_1W_1 = (a + tb)^2$。[▶ 03:19](https://youtu.be/xVngdQsYL4M?t=199) 不以 $b$ 結尾的：$a^2$ 和 $t\,ba$。所以貢獻 $-\frac16(a^2 + t\,ba)$。

[▶ 08:37](https://youtu.be/xVngdQsYL4M?t=517)–[▶ 11:37](https://youtu.be/xVngdQsYL4M?t=697) 【課堂討論】老師先寫成 $\frac12 - \frac16 = \frac13$，學生指出：$\frac12W$ 的二階部分係數是 $\frac12\cdot\frac12 = \frac14$，不是 $\frac12$。「我呈現計算的方式不是最好的。」更正後：

$$
\left(\tfrac14 - \tfrac16\right)a^2(Y) - \tfrac t6\,ba(Y) = \tfrac1{12}[X, [X, Y]] - \tfrac t6[Y, [X, Y]].
$$

[▶ 11:04](https://youtu.be/xVngdQsYL4M?t=664) 和 Hall p.75 底下的式子對上。

積分 $\int_0^1dt$：$\frac1{12}[X,[X,Y]] - \frac1{12}[Y,[X,Y]]$。

[▶ 12:10](https://youtu.be/xVngdQsYL4M?t=730) 所以到三階（總次數）：

$$
\boxed{\ \log(e^Xe^Y) = X + Y + \tfrac12[X, Y] + \tfrac1{12}[X, [X, Y]] - \tfrac1{12}[Y, [X, Y]] + \cdots\ }
$$

兩邊取指數就是 $e^Xe^Y$，「我喜歡叫它 BCH 關係」。

【口頭】[▶ 12:45](https://youtu.be/xVngdQsYL4M?t=765) 「我花了一整個學期，就為了理解這一小塊數學。至少我們拿到了比一般書上多一點的東西。」

> 【課本補充】Hall p.76：Hall 也只算到這一階，結果相同。

## 3. 三層交換子：課堂的嘗試

[▶ 14:24](https://youtu.be/xVngdQsYL4M?t=864) 延長十分鐘，試算三層交換子（四次項）。需要：$\frac12W_3$、$-\frac16(W^2)_3$、$\frac1{12}(W^3)_3$。

【口頭】[▶ 15:32](https://youtu.be/xVngdQsYL4M?t=932) 「好奇怪，只多一層交換子，看起來就糟這麼多。」（像唸「banana」或「Mississippi」唸到一半不知道該停。）

[▶ 16:43](https://youtu.be/xVngdQsYL4M?t=1003)–[▶ 22:40](https://youtu.be/xVngdQsYL4M?t=1360) 全班逐項找詞、配係數，發現好幾組互相抵消（「每一行最後的項都抵消了」），最後得到一個 $\frac1{24}$ 的項。

[▶ 23:28](https://youtu.be/xVngdQsYL4M?t=1408) 老師：「這一定是錯的，不知道為什麼。」上網查 Wikipedia（投影時還開玩笑要把畫面上的選舉廣告打馬賽克），四次項是

$$
-\frac1{24}[Y, [X, [X, Y]]].
$$

[▶ 26:25](https://youtu.be/xVngdQsYL4M?t=1585) 「我們離它不遠。」Wikipedia 還列了五次項（$\frac1{720}$、$\frac1{360}$、$\frac1{120}$ 的組合），以及相關的 **Zassenhaus 公式**（字幕聽成「Dawson house」）。

⚠️ 逐字稿缺字：[▶ 22:01](https://youtu.be/xVngdQsYL4M?t=1321)–[▶ 22:40](https://youtu.be/xVngdQsYL4M?t=1360) 課堂最後得到的那一項，字幕只聽得出「$\frac1{24}$ … XY … YX」，確切是哪個交換子聽不出來，見待確認 #1。

[▶ 27:51](https://youtu.be/xVngdQsYL4M?t=1671) **帶回家考試**：用 $\operatorname{ad}$ 的語言（**不准**把交換子全部乘開），確認或否定 Wikipedia 的三層交換子項。

【Q&A】[▶ 29:02](https://youtu.be/xVngdQsYL4M?t=1742) 學生：直接把交換子乘開不行嗎？老師：「那**不是**允許的解法。」

## 4. 三層交換子：完整計算（補充）

以下**不是逐字稿內容**，是依上一集的方法推的完整三階詞計算（可以拿來對照帶回家考試）。

**$\frac12W_3$**，不以 $b$ 結尾：$\frac12\cdot\frac16a^3 = \frac1{12}a^3$。

**$-\frac16(W^2)_3 = -\frac16(W_1W_2 + W_2W_1)_3$**，不以 $b$ 結尾：
- $W_1W_2 = (a + tb)(\tfrac12a^2 + tab + \tfrac{t^2}{2}b^2)$：$\tfrac12a^3$、$\tfrac t2ba^2$。
- $W_2W_1 = (\tfrac12a^2 + tab + \tfrac{t^2}2b^2)(a + tb)$：$\tfrac12a^3$、$t\,aba$、$\tfrac{t^2}{2}b^2a$。
- 乘 $-\frac16$：$-\tfrac16a^3 - \tfrac t{12}ba^2 - \tfrac t6aba - \tfrac{t^2}{12}b^2a$。

**$\frac1{12}(W^3)_3 = \frac1{12}(a + tb)^3$**，不以 $b$ 結尾的詞：$a^3$、$t\,aba$、$t\,ba^2$、$t^2b^2a$（係數都是 1）。乘 $\frac1{12}$。

**合計**：

| 詞 | $\frac12W$ | $-\frac16W^2$ | $\frac1{12}W^3$ | 合計 |
|---|---|---|---|---|
| $a^3$ | $\frac1{12}$ | $-\frac16$ | $\frac1{12}$ | $0$ |
| $t\,ba^2$ | | $-\frac1{12}$ | $\frac1{12}$ | $0$ |
| $t\,aba$ | | $-\frac16$ | $\frac1{12}$ | $-\frac1{12}$ |
| $t^2b^2a$ | | $-\frac1{12}$ | $\frac1{12}$ | $0$ |

只剩 $-\frac t{12}\,aba(Y) = -\frac t{12}[X, [Y, [X, Y]]]$。積分得

$$
-\frac1{24}[X, [Y, [X, Y]]].
$$

**和 Wikipedia 一致**：由 Jacobi 恆等式，$[X, [Y, Z]] - [Y, [X, Z]] = [[X, Y], Z]$。取 $Z = [X, Y]$，右邊 $= [[X,Y],[X,Y]] = 0$，所以

$$
[X, [Y, [X, Y]]] = [Y, [X, [X, Y]]].
$$

因此四次項確實是 $-\frac1{24}[Y, [X, [X, Y]]]$。課堂上「很多項抵消」的觀察是對的（$a^3$、$ba^2$、$b^2a$ 三組都抵消），問題可能出在 $aba$ 那項的係數或交換子的寫法。

## 5. 課程安排

【口頭】[▶ 13:16](https://youtu.be/xVngdQsYL4M?t=796)
- 本來今天要講**覆蓋群**，延到下次。
- 還剩兩三堂（加一堂補課）。**不會講表示論**：那是一整學期的量。「我不講對你們比較好，你們可以自己讀、寫報告，我不搶走容易摘的果實。」
- 也許明年春天開表示論。

## 6. 一頁速查表

| 敘述 | 關鍵一步 |
|---|---|
| $k$ 層交換子只來自 $g$ 的前 $k$ 項 | $W$ 沒有零階項 |
| 最右邊是 $\operatorname{ad}_Y$ 的詞丟掉 | $[Y, Y] = 0$ |
| 兩層：$(\frac14 - \frac16)a^2 - \frac t6ba$ | $\frac12\cdot\frac12$，不是 $\frac12$ |
| $\log(e^Xe^Y) = X + Y + \frac12[X,Y] + \frac1{12}[X,[X,Y]] - \frac1{12}[Y,[X,Y]] + \cdots$ | 積分 $\int_0^1t\,dt = \frac12$ |
| 三層：只剩 $-\frac t{12}aba$，得 $-\frac1{24}[X,[Y,[X,Y]]]$ | $a^3, ba^2, b^2a$ 抵消 |
| $[X,[Y,[X,Y]]] = [Y,[X,[X,Y]]]$ | Jacobi，$[[X,Y],[X,Y]] = 0$ |

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| BCH ⟹ 李代數同態在單位元素附近給群同態 | 下一集：萬有覆蓋、Lie 定理（April 25） |
| 只靠李括號決定局部群結構 | 單連通群由李代數決定 |

---

## 附：本集一句話總結

> **用 $g(z)$ 的級數、每次只看一層巢狀交換子、丟掉最右邊是 $\operatorname{ad}_Y$ 的詞，就能逐階算出 BCH：$X + Y + \frac12[X,Y] + \frac1{12}[X,[X,Y]] - \frac1{12}[Y,[X,Y]] - \frac1{24}[Y,[X,[X,Y]]] + \cdots$；課堂上三層那項沒算對，留成帶回家考試。**

---

## ⚠️ 待確認清單

1. [▶ 22:01](https://youtu.be/xVngdQsYL4M?t=1321) 課堂上算出的三層交換子項，字幕聽不清楚確切形式（只聽到 $\frac1{24}$ 和一串 X、Y），無法判斷錯在哪一步。第 4 節的完整計算（推論）得到 $-\frac1{24}[X,[Y,[X,Y]]] = -\frac1{24}[Y,[X,[X,Y]]]$，和老師在課堂上查到的 Wikipedia 一致。
