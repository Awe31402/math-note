---
course: Number Theory（2021 秋，線上錄影）
episode: 20
lecture: Lecture 19
date: 待補（2021 秋）
video: https://youtu.be/Bw7o1pAhoq4
notes: Jones & Jones 沒有三次方程的專節；講者照 Rotman《Galois Theory》第二版 p. 44 起
---

# 第 20 集 · Lecture 19：三次方程的解法（On the Solution of the Cubic Equation） [▶ 影片](https://youtu.be/Bw7o1pAhoq4)

← 上一集：[19-complex-numbers-roots-of-unity](19-complex-numbers-roots-of-unity.md) ｜ [總目錄](README.md) ｜ 下一集：[21-sums-of-squares-gaussian-integers](21-sums-of-squares-gaussian-integers.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 20 集
> **講者**：James Cook（推斷，見第 1 集待確認清單）
> **來源**：YouTube 錄影逐字稿（47:24，**whisper 轉錄**；YouTube 字幕下載被擋）；課本無對應章節
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯或掉字
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 一次與二次](#1-一次與二次)
- [2. 降階多項式（depressed polynomial）](#2-降階多項式depressed-polynomial)
- [3. 三次式的降階](#3-三次式的降階)
- [4. 解降階三次式](#4-解降階三次式)
- [5. 三次公式](#5-三次公式)
- [6. 例子](#6-例子)
- [7. 五次方程與 Galois 理論](#7-五次方程與-galois-理論)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

推導一般三次方程的解。講者照 Rotman《Galois Theory》第二版 p. 44 起的講法 [▶ 01:09](https://youtu.be/Bw7o1pAhoq4?t=69)。

【口頭】Rotman 寫了很多數學書，講者很推崇：很多人寫好書，但仔細讀 Rotman 會發現他的講法勝過很多人 [▶ 01:45](https://youtu.be/Bw7o1pAhoq4?t=105)。

| 段落 | 內容 |
|---|---|
| 1–3 | 代換 $X = x-\frac{a_{n-1}}n$ 消去次高項（配方法的推廣） |
| 4–5 | $u = y+z$、$3yz+q=0$ ⇒ $y^3$ 滿足二次方程 ⇒ 三個根 |
| 6 | 五個例子（含「實根卻需要複數」的情形） |
| 7 | 四次可解、五次一般不可用根式解：Abel、Galois |

> Jones & Jones 沒有三次方程的內容，本集沒有【課本補充】。

---

## 1. 一次與二次

[▶ 00:00](https://youtu.be/Bw7o1pAhoq4?t=0)

- **$n=1$**：$ax+b = 0$，$a\neq0$ ⇒ $x = -b/a$。
- **$n=2$**：$ax^2+bx+c = 0$，$a\neq0$。提出 $a$、配方：
$$\left(x+\frac b{2a}\right)^2 = \frac{b^2-4ac}{4a^2}\ \Rightarrow\ x+\frac b{2a} = \pm\frac{\sqrt{b^2-4ac}}{2a}.$$
上一集說過，$a,b,c$ 是複數時照樣成立，只是平方根要取複數的意思。

配方法在三次有類比。

---

## 2. 降階多項式（depressed polynomial）

[▶ 02:19](https://youtu.be/Bw7o1pAhoq4?t=139)

**定義**：$n$ 次多項式若**沒有 $x^{n-1}$ 項**（跳過次高項），叫**降階的**（depressed；講者說 Rotman 用 reduced，但 depressed 更常見）。

**引理**：$f(X) = X^n + a_{n-1}X^{n-1}+\cdots+a_0$（首一）。代換
$$X = x - \frac1n a_{n-1}$$
得到降階多項式
$$\tilde f(x) = x^n + b_{n-2}x^{n-2}+\cdots+b_1x+b_0.$$
而且若 $u$ 是 $\tilde f$ 的根，則 $u - \frac1na_{n-1}$ 是 $f$ 的根。

**證明** [▶ 03:29](https://youtu.be/Bw7o1pAhoq4?t=209)：代入後用二項式定理展開。$x^{n-1}$ 的係數有兩個來源：
- $\left(x-\frac{a_{n-1}}n\right)^n$ 給 $n\cdot x^{n-1}\cdot\left(-\frac{a_{n-1}}n\right) = -a_{n-1}x^{n-1}$；
- $a_{n-1}\left(x-\frac{a_{n-1}}n\right)^{n-1}$ 給 $a_{n-1}x^{n-1}$。

兩者相消。$b_{n-2},\dots,b_0$ 是原係數的複雜組合。根的對應：$\tilde f(x) = f\!\left(x-\frac{a_{n-1}}n\right)$，所以 $\tilde f(u) = 0\iff f\!\left(u-\frac{a_{n-1}}n\right) = 0$。∎

**$n = 2$** [▶ 05:29](https://youtu.be/Bw7o1pAhoq4?t=329)：$f(X) = X^2+bX+c$，代 $X = x-\frac b2$：
$$\left(x-\tfrac b2\right)^2 + b\left(x-\tfrac b2\right)+c = x^2 + \tfrac{b^2}4 - \tfrac{b^2}2 + c = x^2 - \tfrac14b^2 + c.$$
$bx$ 項相消。解 $\tilde f(u) = 0$：$u = \pm\frac12\sqrt{b^2-4c}$。原方程的根 $= u - \frac b2$，就是 $a=1$ 時的二次公式。

【口頭】這就像配方法，只是改用代換來做 [▶ 05:29](https://youtu.be/Bw7o1pAhoq4?t=329)。

---

## 3. 三次式的降階

[▶ 06:40](https://youtu.be/Bw7o1pAhoq4?t=400)

$g(X) = X^3+aX^2+bX+c$（不是首一就先除以首項係數）。代 $X = x-\frac a3$，整理得
$$\tilde g(x) = x^3 + qx + r,\qquad q = b-\frac13a^2,\qquad r = \frac2{27}a^3 - \frac13ab + c.$$
若 $\tilde g(u) = 0$，則 $u-\frac a3$ 是 $g$ 的根。所以只要會解降階三次式就行。

---

## 4. 解降階三次式

### 4.1 歷史

[▶ 09:23](https://youtu.be/Bw7o1pAhoq4?t=563)

【口頭】依 Rotman：公式本質上是 Scipione del Ferro 約 1515 年發現；Tartaglia 大約同時發現類似公式；兩者首次印刷在 Cardano 1545 年的書。三人之間的故事很有意思，YouTube 上有一部很棒的影片。至少在歐洲，三次方程的解從約 1500 年就知道了，四次不久後也解出來 [▶ 09:58](https://youtu.be/Bw7o1pAhoq4?t=598)。

【口頭】本集暗號是「Voltron」[▶ 10:34](https://youtu.be/Bw7o1pAhoq4?t=634)。

### 4.2 推導

[▶ 10:34](https://youtu.be/Bw7o1pAhoq4?t=634)

**想法**：設根可以寫成 $u = y+z$，推出 $y,z$ 要滿足的條件。只有 $u = y+z$ 不夠決定 $y,z$，需要再加一個條件。

1. 展開：
$$u^3 = (y+z)^3 = y^3+z^3+3yz(y+z) = y^3+z^3+3uyz.$$
2. 代入 $u^3+qu+r = 0$：
$$y^3+z^3 + (3yz+q)\,u + r = 0. \tag{1}$$
3. **再加一個條件**：要求
$$3yz+q = 0.$$
【口頭】這像微分方程裡常做的事：猜解的形式，猜得太鬆就再加條件，加到夠固定，再回去驗證。條件可能加太多，但這裡不會壞事。Rotman 有一題作業解釋為什麼這是合理的 [▶ 12:25](https://youtu.be/Bw7o1pAhoq4?t=745)。
4. 於是 (1) 變成 $y^3+z^3 = -r$，而 $yz = -\frac q3$，立方得
$$y^3z^3 = -\frac{q^3}{27}.$$
5. 由 4，$z^3 = -\dfrac{q^3}{27y^3}$，代入 $y^3+z^3 = -r$ 再乘 $y^3$：
$$y^6 + ry^3 - \frac{q^3}{27} = 0.$$
這是 $y^3$ 的**二次方程**。令 $\lambda = y^3$，二次公式：
$$y^3 = \frac12\left(-r+\sqrt{r^2+\frac{4q^3}{27}}\right). \tag{2}$$
（$\pm$ 只要取一個，取 $+$。）

⚠️ 講者板書一度把 $\frac{4q^3}{27}$ 寫成 $\frac{4q^2}{27}$，當場發現改成三次方，並提醒「這頁後面還有幾處要注意」[▶ 14:49](https://youtu.be/Bw7o1pAhoq4?t=889)、[▶ 19:12](https://youtu.be/Bw7o1pAhoq4?t=1152)。

6. 由 (2) 開立方得 $y$，再令 $z = -\dfrac q{3y}$，$u = y+z$ 就是根。

**記號**：$R = r^2+\dfrac{4q^3}{27}$（講者說這東西應該有名字，但一時想不起來）[▶ 22:31](https://youtu.be/Bw7o1pAhoq4?t=1351)。

（以下**不是逐字稿內容**，是依代數推得的：三次式 $x^3+qx+r$ 的判別式是 $\Delta = -4q^3-27r^2 = -27R$，所以 $R$ 和判別式只差一個負的常數倍。）

**為什麼需要複數** [▶ 16:08](https://youtu.be/Bw7o1pAhoq4?t=968)：即使 $q,r$ 是實數，$q^3$ 可能是負的，$R$ 可能是負數，$\sqrt R$ 是虛數，接著還要開**複數的立方根**。二次方程遇到複數時還能安慰自己「那是沒有 $x$ 截距的情況，不對應物理問題」；但三次方程**即使是實係數、實根**，中間也會出現複數（例 2）。

### 4.3 三個根

[▶ 17:23](https://youtu.be/Bw7o1pAhoq4?t=1043)

用 $\omega$ 表示立方單位根（上一集的 $\zeta_3$）：
$$\omega = e^{2\pi i/3} = \frac{-1+i\sqrt3}2,\qquad \omega^2 = \frac{-1-i\sqrt3}2 = \bar\omega = \frac1\omega.$$

若 $y_0$ 滿足 (2)，則 $(y_0\omega)^3 = y_0^3\omega^3 = y_0^3$、$(y_0\omega^2)^3 = y_0^3$，所以 $y_0\omega$、$y_0\omega^2$ 也滿足 (2)。對應的 $z$：$-\frac q{3y_0\omega} = z_0\cdot\frac1\omega = z_0\omega^2$。

**三個根**（$z_0 = -\frac q{3y_0}$）：
$$u_1 = y_0+z_0,\qquad u_2 = \omega y_0+\omega^2z_0,\qquad u_3 = \omega^2y_0+\omega z_0.$$

【口頭】「立方單位根有各種好玩的性質，例如 $1/\omega = \omega^2$。」[▶ 20:54](https://youtu.be/Bw7o1pAhoq4?t=1254)

---

## 5. 三次公式

**摘要（三次公式）** [▶ 21:58](https://youtu.be/Bw7o1pAhoq4?t=1318)：解 $x^3+qx+r = 0$：
$$y^3 = \frac12\left(-r+\sqrt R\right),\quad R = r^2+\frac{4q^3}{27},\quad z = -\frac q{3y},$$
$$u\in\{\,y+z,\ \ \omega y+\omega^2z,\ \ \omega^2y+\omega z\,\}.$$

**全部寫成一條公式？** [▶ 28:12](https://youtu.be/Bw7o1pAhoq4?t=1692)：對 $X^3+aX^2+bX+c = 0$，
$$X = u - \frac a3,\qquad u = y - \frac q{3y},\qquad y = \sqrt[3]{\frac12\left(-r+\sqrt{r^2+\frac4{27}q^3}\right)},$$
其中 $q = b-\frac13a^2$、$r = \frac2{27}a^3-\frac13ab+c$。

【口頭】
- 「即使搞了這麼多，我還是沒寫成只含 $a,b,c$ 的公式」——還留著討厭的 $q$，要再代 $q = b-\frac13a^2$ 才是「冷冰冰的」純係數公式，講者留給大家 [▶ 29:49](https://youtu.be/Bw7o1pAhoq4?t=1789)。
- 這就是為什麼高中不教、他教過的代數書裡也沒有（頂多章末特別專題）：三次就是難這麼多。
- 有趣的是四次**不會**再難很多：降階後有所謂的「預解三次式」（resolvent cubic），化成三次問題再用這裡的方法，四次的解大約一頁長，三次也大約一頁 [▶ 30:52](https://youtu.be/Bw7o1pAhoq4?t=1852)。
- 要得到另外兩個根的明確公式，還得配上立方單位根；而且公式裡的立方根可能是複數的立方根——所以第 4.3 節那種寫法是比較好的路 [▶ 31:24](https://youtu.be/Bw7o1pAhoq4?t=1884)。

---

## 6. 例子

### 例 1：$x^3-15x-126 = 0$（Rotman 的例子）

[▶ 23:38](https://youtu.be/Bw7o1pAhoq4?t=1418)
- 已經降階：$q = -15$、$r = -126$。
- $R = 126^2 + \frac{4(-15)^3}{27} = 15876 - 500 = 15376 = 124^2$，$\sqrt R = 124$。
- $y^3 = \frac12(126+124) = 125$，$y = 5$。
- $z = -\frac{q}{3y} = \frac{15}{15} = 1$。
- $u_1 = 6$。（檢查：$216-90-126 = 0$。）
- 其他兩根：
$$5\omega+\omega^2 = \frac{5(-1+i\sqrt3)+(-1-i\sqrt3)}2 = -3+2i\sqrt3,\qquad 5\omega^2+\omega = -3-2i\sqrt3.$$

【口頭】「這例子太刻意了」——完全是反向設計出來讓每一步都漂亮。這就是講者說 Rotman 寫得美的地方 [▶ 24:10](https://youtu.be/Bw7o1pAhoq4?t=1450)。

⚠️ 講者算 $5\omega+\omega^2$、$5\omega^2+\omega$ 時正負號一度弄反，自己更正 [▶ 26:37](https://youtu.be/Bw7o1pAhoq4?t=1597)。

**另一種做法**：有了一個根就做除法：$x^3-15x-126 = (x-6)(x^2+6x+21)$，再對二次式配方：$x = -3\pm\sqrt{9-21} = -3\pm2i\sqrt3$。哪種好看個人口味 [▶ 27:08](https://youtu.be/Bw7o1pAhoq4?t=1628)。

### 例 2：$x^3-7x+6 = 0$（實根卻需要複數）

[▶ 32:33](https://youtu.be/Bw7o1pAhoq4?t=1953)
- 其實 $x^3-7x+6 = (x-1)(x-2)(x+3)$，根是 $1, 2, -3$。看三次公式怎麼把事情變複雜。
- $q = -7$、$r = 6$：$R = 36+\frac{4(-343)}{27} = \frac{972-1372}{27} = -\frac{400}{27}$。
- $y^3 = \frac12\left(-6+\sqrt{-\frac{400}{27}}\right)$——**實係數、實根的問題，三次公式卻要用到複數**。
- 講者把三個根的公式丟進 Wolfram Alpha，分別得到 2、$-3$、1。

【口頭】「這明顯嗎？我不覺得。」證明這種複數立方根的和等於 1，會是不錯的複變作業——不用計算機，直接操作。重點是：**有了三次公式不代表該用它** [▶ 34:46](https://youtu.be/Bw7o1pAhoq4?t=2086)。

（講者在螢幕上把立方根寫成平方根，自己更正：「指數的 3 和分母的 3 不是同一個 3」[▶ 33:41](https://youtu.be/Bw7o1pAhoq4?t=2021)。）

### 例 3：$x^3+27 = 0$（公式不適用的特例）

[▶ 34:46](https://youtu.be/Bw7o1pAhoq4?t=2086)
- $q = 0$、$r = 27$：$R = 729$，$y^3 = \frac12(-27+27) = 0$，$y = 0$，$z = -\frac q{3y}$ **除以 0**。
- 嚴格來說要另外處理這種情況；但這時直接 $x = (-27)^{1/3}$ 就好（上一集的方法），「選擇你自己的冒險」。

### 例 4：$x^3-3x = 0$（$r = 0$、$q\neq0$）

[▶ 35:47](https://youtu.be/Bw7o1pAhoq4?t=2147)
- $q = -3$、$r = 0$：$R = \frac{4(-27)}{27} = -4$，$\sqrt R = 2i$。
- $y^3 = \frac12(0+2i) = i = e^{i\pi/2}$（極座標形式，上一集）。
- 開立方：角度除以 3，$y = e^{i\pi/6}$。
- $z = -\frac{-3}{3y} = \frac1y = e^{-i\pi/6}$。
- $u_1 = e^{i\pi/6}+e^{-i\pi/6} = 2\cos\frac\pi6 = \sqrt3$。
- 另外兩根：$\omega y+\omega^2z = 2\cos\frac{5\pi}6 = -\sqrt3$，$\omega^2y+\omega z = 2\cos\frac{3\pi}2 = 0$。

所以根是 $0,\pm\sqrt3$，和直接分解 $x(x^2-3) = x(x-\sqrt3)(x+\sqrt3)$ 一致。

⚠️ 逐字稿缺字：[▶ 37:30](https://youtu.be/Bw7o1pAhoq4?t=2250) 講者說另外兩個組合「add together to give me root 3 or to give me 0」，照計算應為 $-\sqrt3$ 和 0。

### 例 5：$x^3-3x^2+6x-4 = 0$（需要降階）

[▶ 39:06](https://youtu.be/Bw7o1pAhoq4?t=2346)

【口頭】至少要有一個真的需要降階的例子；這裡故意用公式解（不是最聰明的解法），為了示範 [▶ 40:10](https://youtu.be/Bw7o1pAhoq4?t=2410)。
- $a = -3$，代 $X = x-\frac{-3}3 = x+1$：
$$(x+1)^3 - 3(x+1)^2 + 6(x+1) - 4 = x^3+3x.$$
（次高項相消；講者直接展開，沒套一般公式。）
- $q = 3$、$r = 0$：$R = \frac{4\cdot27}{27} = 4$，$y^3 = \frac12\sqrt4 = 1$，$y = 1$，$z = -1$。
- 降階方程的根：$u_1 = 0$、$u_2 = \omega-\omega^2 = i\sqrt3$、$u_3 = \omega^2-\omega = -i\sqrt3$。
- **別忘了加回 1**（「給它一個笑臉」）：原方程的根是
$$X = 1,\quad 1+i\sqrt3,\quad 1-i\sqrt3.$$
所以 $X^3-3X^2+6X-4 = (X-1)(X-1-i\sqrt3)(X-1+i\sqrt3) = (X-1)(X^2-2X+4)$。

---

## 7. 五次方程與 Galois 理論

[▶ 41:48](https://youtu.be/Bw7o1pAhoq4?t=2508)

【口頭】
- 二次自古就會解；三次曾被認為不可解，後來解出；四次緊接著解出。這些在 1500 年代找到、1600 年代初鞏固。
- 1700 年代，大家想用這些技巧攻五次方程，什麼都不行。三次的情形裡根之間有一種**旋轉**（基於單位圓上的單位根），可以推廣成**根的置換**。講者記得 Lagrange 花了幾十年試各種代換，都不成功，漸漸大家認為五次方程大概沒有一般公式 [▶ 43:24](https://youtu.be/Bw7o1pAhoq4?t=2604)。
- 講者說的年代：約 1812 年 Ruffini 給了一個普遍被認為有瑕疵的證明（講者認識的代數學家沒人說它好話）；約 1820 年 Abel 證明不可能有像三次那樣用根式表示的一般公式；1830 年 Galois 創立 **Galois 理論** [▶ 43:57](https://youtu.be/Bw7o1pAhoq4?t=2637)。
- Gallian《Contemporary Abstract Algebra》（第四版）第 32 章在大三、大四抽象代數課的最後，給出判斷五次方程能否用根式解的方法。好好教 Galois 理論大概要一學期；講者在抽象代數課用三分之一學期「不太恰當地」教過。
- 對五次方程可以算它的 **Galois 群**：若是**可解群**（solvable group），就能用根式公式解；若不是（例如是單群，simple group），就**不能**用根式寫出解——也就是沒有二次公式那樣的類比 [▶ 45:32](https://youtu.be/Bw7o1pAhoq4?t=2732)。
- 「$n = 1,2,3,4$ 都能做，到 $n=5$ 突然一般來說就不行了，非常有趣的轉折。」
- 這個問題也是**近代群論的誕生**；群論的另一個入口是變換群：什麼變換讓形狀不變——對稱性 [▶ 46:37](https://youtu.be/Bw7o1pAhoq4?t=2797)。

⚠️ 待確認：Ruffini、Abel 的年份是講者口述（「about 1812」「about 1820」），筆記未另外查證。

---

## 8. 一頁速查表

**降階**：$X^n+a_{n-1}X^{n-1}+\cdots$，代 $X = x-\frac{a_{n-1}}n$ 消去 $x^{n-1}$；$\tilde f(u)=0$ ⇒ $u-\frac{a_{n-1}}n$ 是原根。
- 三次：$X^3+aX^2+bX+c$，$X = x-\frac a3$ ⇒ $x^3+qx+r$，$q = b-\frac{a^2}3$，$r = \frac{2a^3}{27}-\frac{ab}3+c$。

**解 $x^3+qx+r = 0$**
- 設 $u = y+z$，要求 $3yz+q = 0$ ⇒ $y^3+z^3 = -r$、$y^3z^3 = -\frac{q^3}{27}$。
- $y^3$ 滿足 $\lambda^2+r\lambda-\frac{q^3}{27} = 0$ ⇒ $y^3 = \frac12(-r+\sqrt R)$，$R = r^2+\frac{4q^3}{27}$。
- $z = -\frac q{3y}$；根 $y+z$、$\omega y+\omega^2z$、$\omega^2y+\omega z$，$\omega = \frac{-1+i\sqrt3}2$。

**例**
- $x^3-15x-126$：$R = 124^2$，$y=5$、$z=1$，根 $6$、$-3\pm2i\sqrt3$。
- $x^3-7x+6$：$R = -\frac{400}{27}<0$，實根 $1,2,-3$ 卻要經過複數。
- $x^3-3x$：$y^3 = i$，$y = e^{i\pi/6}$，根 $\sqrt3, -\sqrt3, 0$。
- $x^3-3x^2+6x-4$：$X = x+1$ ⇒ $x^3+3x$，根 $1, 1\pm i\sqrt3$。
- $q = 0$ 時公式除以 0，直接開立方。

**歷史**：del Ferro（~1515）、Tartaglia、Cardano（1545）；四次不久後；五次一般不能用根式解（Abel；Galois 1830：Galois 群可解 ⇔ 根式可解）。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 複數、單位根的運算 | 第 21–22 集（高斯整數 $\mathbb{Z}[i]$） |
| 群論的起源、Galois 理論 | 第 23 集（四元數，另一種代數結構） |
| 根的置換、對稱 | 第 24 集（Fermat 最後定理的現代發展） |

---

## 附：本集一句話總結

> **代換 $X = x-\frac a3$ 把三次式降階成 $x^3+qx+r$；設根 $u=y+z$ 並強加 $3yz+q=0$，$y^3$ 就滿足一個二次方程，解出 $y^3=\frac12(-r+\sqrt{r^2+4q^3/27})$，三個根是 $y+z$、$\omega y+\omega^2z$、$\omega^2y+\omega z$——即使三個根都是實數，過程也可能必須經過複數；而五次方程一般根本沒有這種根式公式（Abel、Galois）。**

---

## ⚠️ 待確認清單

1. [▶ 43:57](https://youtu.be/Bw7o1pAhoq4?t=2637) Ruffini（「約 1812」）、Abel（「約 1820」）的年份是講者口述，未查證。
2. 本集逐字稿是 whisper（large-v3-turbo）轉錄，不是 YouTube 字幕；時間點可能和影片差 1–2 秒。

---

*筆記依據 James Cook（推斷）「Number Theory」Lecture 19 錄影的 whisper 逐字稿（47:24）整理；講者課堂內容取材自 Rotman《Galois Theory》第二版；Jones & Jones 無對應章節。*
