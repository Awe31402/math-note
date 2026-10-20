---
course: Abstract Algebra II (Spring 2026)
episode: 27
lecture: L23
date: 2026-03-23
video: https://www.youtube.com/watch?v=4CV8yVzqWxk
notes: 講義/AA2/Math422_Lecture23_FurtherExamplesGalois.pdf
---

# 第 27 集 · L23：Galois 理論例子、分圓體、共軛技巧 [▶ 影片](https://www.youtube.com/watch?v=4CV8yVzqWxk&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[26-L23-Galois理論例子-下]] ｜ [總目錄](../README.md) ｜ 下一集：[[28-L24-多項式的Galois群]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 27 集，Lecture 23
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ 手寫講義 `Math422_Lecture23_FurtherExamplesGalois.pdf`（8 頁，最後一頁「Fun with Galois Conjugates!」是空白的），依 Dummit & Foote §14.2、§14.5。投影講義為主，最後黑板。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：這是 3/23 那堂課的**前段**（約 1 小時）；最後 5 分鐘（Bill 的 Maple 共軛例子收尾）在 [[26-L23-Galois理論例子-下]]。播放清單把兩段順序排反了。

---

## 目錄

- [1. 用 Galois 對應證明 ℚ(√2, √3) = ℚ(√2 + √3)](#1-用-galois-對應證明-ℚ2-3--ℚ2--3)
- [2. 正規子群 ↔ Galois 子體：V₄ 與 S₃](#2-正規子群--galois-子體v₄-與-s₃)
- [3. x⁸ − 2 的分裂體（擬二面體群）](#3-x⁸--2-的分裂體擬二面體群)
- [4. 分圓體的 Galois 群 ≅ (ℤ/n)ˣ](#4-分圓體的-galois-群--ℤnˣ)
- [5. 例：ℚ(ζ₅)](#5-例ℚζ₅)
- [6. 有理化分母：共軛與 Bézout](#6-有理化分母共軛與-bézout)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 1. 用 Galois 對應證明 ℚ(√2, √3) = ℚ(√2 + √3)

[▶ 00:00](https://youtu.be/4CV8yVzqWxk?t=0) 課前禱告。「先回顧上次，**欣賞**一下基本定理的結構——看它**替我們做了什麼**。」

（講義 p.1）$K = \mathbb{Q}(\sqrt2,\sqrt3)$ 是 $(x^2-2)(x^2-3)$ 的分裂體 ⇒ Galois ⇒ $[K:\mathbb{Q}] = |\mathrm{Aut}(K/\mathbb{Q})|$。
- 【Q&A】學生：「括號裡那個逗號應該是冒號？」「對，謝謝。」
- 自同構固定質子體（1 送 1、2 送 2、$\frac13$ 送 $\frac13$……），所以只由 $\sqrt2$、$\sqrt3$ 的去向決定。

💬 講義這次的命名和上次**對調**了：這裡 $\sigma(\sqrt2) = \sqrt2$、$\sigma(\sqrt3) = -\sqrt3$；$\tau(\sqrt3) = \sqrt3$、$\tau(\sqrt2) = -\sqrt2$。兩者都把 $\sqrt6$ 變號；$\sigma\tau$ 固定 $\sqrt6$。所以 $K^{\langle\tau\rangle} = \mathbb{Q}(\sqrt3)$……講義 p.1 的格圖仍沿用上次的配對，讀的時候注意。

**$\mathbb{Q}(\sqrt2+\sqrt3)$ 是哪個子群的固定體？**[▶ 03:30](https://youtu.be/4CV8yVzqWxk?t=210)（講義 p.2）
$$\sigma(\sqrt2+\sqrt3) = \sqrt2-\sqrt3,\quad\tau(\sqrt2+\sqrt3) = -\sqrt2+\sqrt3,\quad\sigma\tau(\sqrt2+\sqrt3) = -\sqrt2-\sqrt3$$
——**都不等於** $\sqrt2+\sqrt3$。只有恆等元固定它 ⇒ $\mathbb{Q}(\sqrt2+\sqrt3)$ 是 $\{1\}$ 的固定體。而 $K^{\{1\}} = K$ ⇒ 由 **Galois 對應**：
$$\mathbb{Q}(\sqrt2,\sqrt3) = \mathbb{Q}(\sqrt2+\sqrt3).$$
「這跟上次給的論證**本質上不同**，我覺得是個**很好**的論證。」

---

## 2. 正規子群 ↔ Galois 子體：V₄ 與 S₃

**$V_4$**[▶ 05:30](https://youtu.be/4CV8yVzqWxk?t=330)（講義 p.2）：$\langle\sigma\rangle,\langle\tau\rangle,\langle\sigma\tau\rangle$ 都是 2 階、**指標 2** ⇒ 都**正規** ⇒ 對應的固定體 $\mathbb{Q}(\sqrt3)$、$\mathbb{Q}(\sqrt2)$、$\mathbb{Q}(\sqrt6)$ 都在 $\mathbb{Q}$ 上 Galois。「這**不是巧合**：它們正是 $x^2-3$、$x^2-2$、$x^2-6$ 的分裂體。」

**$S_3$**[▶ 06:30](https://youtu.be/4CV8yVzqWxk?t=390)（講義 p.3）：$x^3-2$ 的分裂體 $\mathbb{Q}(\sqrt[3]2,\rho)$。
- $\langle\sigma\rangle$ 指標 2 ⇒ 正規（**唯一**的正規真子群）⇒ $\mathbb{Q}(\rho)$ 在 $\mathbb{Q}$ 上 Galois（$\rho^2+\rho+1 = 0$，$m_{\rho,\mathbb{Q}} = \Phi_3$，2 次）。
- $\langle\tau\rangle,\langle\tau\sigma\rangle,\langle\tau\sigma^2\rangle$ **不正規**：共軛會把它們**互相搬動**。對應的 $\mathbb{Q}(\sqrt[3]2)$、$\mathbb{Q}(\rho\sqrt[3]2)$、$\mathbb{Q}(\rho^2\sqrt[3]2)$ **不是分裂體**——自同構群只有恆等，「群不夠大，不能 Galois」；共軛會把一個子體送到另一個。
- [▶ 08:30](https://youtu.be/4CV8yVzqWxk?t=510) 老師當場用 $\sigma^3 = \tau^2 = 1$、$\sigma\tau = \tau\sigma^{-1} = \tau\sigma^2$ 算共軛 $\sigma^{-1}\tau\sigma$。「我**今天腦袋不行**，先警告你們。」（學生打了個呵欠：「**反對意見**？」）結論：共軛 $\langle\tau\rangle$ 會得到另一個 2 階子群。

💬 例如 $\sigma\tau\sigma^{-1} = \sigma\tau\sigma^2 = \tau\sigma^2\sigma^2 = \tau\sigma^4 = \tau\sigma$，所以 $\sigma\langle\tau\rangle\sigma^{-1} = \langle\tau\sigma\rangle\neq\langle\tau\rangle$。

---

## 3. x⁸ − 2 的分裂體（擬二面體群）

[▶ 13:30](https://youtu.be/4CV8yVzqWxk?t=810)（講義 p.4–5）「D&F 下一個例子我**不打算寫細節**，只想跟你們聊一下——他們花了**將近三頁**在這頭**野獸**上。」

- $\theta = \sqrt[8]2$（正的），$\zeta_8 = e^{\pi i/4} = \frac{1+i}{\sqrt2}$。$x^8 = 2$ 的解是 $\theta\zeta_8^k$（$k = 0,\dots,7$）⇒ 分裂體 $K = \mathbb{Q}(\theta,\zeta_8)$。
- **更好的寫法**[▶ 14:30](https://youtu.be/4CV8yVzqWxk?t=870)：$\zeta_8\sqrt2 = 1+i$ ⇒ $\mathbb{Q}(\zeta_8) = \mathbb{Q}(i,\sqrt2)$。而 $\theta^4 = \sqrt2$ ⇒ 有 $\theta$ 就有 $\sqrt2$ ⇒
$$K = \mathbb{Q}(\sqrt[8]2,\,i).$$
- **次數 16**[▶ 16:00](https://youtu.be/4CV8yVzqWxk?t=960)：$x^8-2$ Eisenstein（$p = 2$）⇒ $[\mathbb{Q}(\sqrt[8]2):\mathbb{Q}] = 8$；它是**實的**體，不含 $i$ ⇒ 再乘 2 ⇒ 16。
- 【課堂討論】[▶ 18:30](https://youtu.be/4CV8yVzqWxk?t=1110)「$\varphi(8)$？」學生：「4。」「1、3、5、7 跟 8 互質。」「乍看用 $\theta$ 和 $\zeta_8$ 會是 $8\times4 = 32$ 次——**不是**，兩者**糾纏**在一起。換個寫法就看出是 16。這段**很聰明**。」
- **Galois 群**[▶ 17:00](https://youtu.be/4CV8yVzqWxk?t=1020)：$\theta\mapsto\zeta^a\theta$（8 種）、$i\mapsto\pm i$（2 種）——共 16 種可能。「它是分裂體 ⇒ Galois ⇒ 自同構恰好 16 個 ⇒ **這 16 種全都是自同構**，不用逐一驗證。**很狡猾**。」
- 經過大量計算（D&F p.578）：
$$\sigma:\begin{cases}\theta\mapsto\zeta\theta\\ i\mapsto i\\ \zeta\mapsto\zeta^5 = -\zeta\end{cases}\qquad\tau:\begin{cases}\theta\mapsto\theta\\ i\mapsto-i\\ \zeta\mapsto\zeta^7\end{cases}$$
$$\mathrm{Gal}(\mathbb{Q}(\sqrt[8]2,i)/\mathbb{Q}) = \langle\sigma,\tau\mid\sigma^8 = \tau^2 = 1,\ \sigma\tau = \tau\sigma^3\rangle.$$
- 【課堂討論】[▶ 21:00](https://youtu.be/4CV8yVzqWxk?t=1260)「如果是二面體群，$\sigma\tau = \tau\sigma^{?}$」「$\sigma^{-1} = \sigma^7$。這裡是 $\sigma^3$——**不是**二面體群，是**擬二面體群**（quasidihedral）。」
- 三個 8 階子群**互不同構**（講義 p.5）：$\langle\sigma^2,\tau\rangle\cong D_8$（正方形的對稱群；這裡下標是群的階）、$\langle\sigma\rangle\cong\mathbb{Z}_8$、$\langle\sigma^2,\tau\sigma^3\rangle\cong Q_8$（四元數群）；固定體分別是 $\mathbb{Q}(\sqrt2)$、$\mathbb{Q}(i)$、$\mathbb{Q}(\sqrt{-2})$。「**非常豐富**的例子。體圖我不畫——**我們會畫一整天**。看看它（D&F p.580–581）。」

💬 [▶ 15:30](https://youtu.be/4CV8yVzqWxk?t=930) 老師口誤說「$\theta$ 是 2 的四次方根，平方得 $\sqrt2$」、「$\theta^8 = 1$」——$\theta = \sqrt[8]2$，**$\theta^4 = \sqrt2$**、$\theta^8 = 2$。

---

## 4. 分圓體的 Galois 群 ≅ (ℤ/n)ˣ

[▶ 23:30](https://youtu.be/4CV8yVzqWxk?t=1410)（講義 p.6，D&F §14.5）證過 $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$，它是 $\Phi_n$ 的分裂體。
- 任何自同構必須把 $\zeta_n$ 送到**本原** $n$ 次單位根 $\zeta_n^k$，$\gcd(k,n) = 1$——「生成元送到生成元」。
- 【課堂討論】[▶ 25:00](https://youtu.be/4CV8yVzqWxk?t=1500)「$n = 4$：跟 4 互質的？」「1 和 3。」「$i\mapsto i^3$ 可以；$i\mapsto i^2 = -1$ 或 $i\mapsto1$ **不行**。」
- 有 $|U(n)| = \varphi(n)$ 種選擇 = Galois 群的大小 ⇒ 每種都是自同構。

> **定理 26**（講義 p.6）[▶ 28:30](https://youtu.be/4CV8yVzqWxk?t=1710)　$\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})\cong(\mathbb{Z}/n\mathbb{Z})^\times = U(n)$，同構為 $a\mapsto\sigma_a$，$\sigma_a(\zeta_n) = \zeta_n^a$。

**證明**[▶ 29:30](https://youtu.be/4CV8yVzqWxk?t=1770)（「我寫在講義的證明是**垃圾**，你們能修。好，我們**現在修**。我警告過你們，我今天**腦袋不靈光**。」）
- $\psi(a) = \sigma_a$ 是兩個**有限集**之間的映射，大小都是 $\varphi(n)$ ⇒ 只要證同態 + 單射。
- **同態**：
$$\sigma_a\sigma_b(\zeta_n) = \sigma_a(\zeta_n^b) = \sigma_a(\zeta_n)^b = (\zeta_n^a)^b = \zeta_n^{ab} = \sigma_{ab}(\zeta_n).$$
  自同構由 $\zeta_n$ 的去向**完全決定** ⇒ $\sigma_a\sigma_b = \sigma_{ab}$ ⇒ $\psi(a)\psi(b) = \psi(ab)$。（「我就知道會有人笑。」）
- **核**[▶ 32:30](https://youtu.be/4CV8yVzqWxk?t=1950)：$\sigma_a = \sigma_1$（恆等）⇒ $\zeta_n^a = \zeta_n$。$a\in U(n)$ 中只有 $a = 1$ 會這樣 ⇒ 核平凡 ⇒ 單射 ⇒ 同構。$\blacksquare$
  - （「我的 $\zeta$ **一個比一個糟**——要問 Spano 博士，他需要**拓撲學**來描述我的 $\zeta$。」）
- 【口頭】[▶ 35:30](https://youtu.be/4CV8yVzqWxk?t=2130)「我的課程規劃裡**好像沒有**這節，但它**很簡單**，該講。這給了我們很好的例子。」

---

## 5. 例：ℚ(ζ₅)

[▶ 36:00](https://youtu.be/4CV8yVzqWxk?t=2160)（講義 p.7）（「她睏了。我還沒有學生睡著過，**現在開始好像時機不錯**。」）
- 【課堂討論】「$[\mathbb{Q}(\zeta_5):\mathbb{Q}]$？」（學生：「那是 S 還是 5？」「是 5。」「你們**好可怕**。」）「$\varphi(5) = 4$。」
- 【課堂討論】[▶ 37:00](https://youtu.be/4CV8yVzqWxk?t=2220)「$1+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4 = ?$」學生：「它們**對稱地**排在單位圓上。」「那五點的**平均**？」「**0**。」「這對所有 $n$ 次單位根都成立：$n = 2$ 是 $\pm1$，$n = 3$ 三點，$n = 4$ 是 $1,i,-1,-i$——平均都是 0。**不是 5 特有的**。」
- $G = \{1,\sigma_2,\sigma_3,\sigma_4\}\cong U(5)\cong\mathbb{Z}_4$，循環群。**生成元**[▶ 40:00](https://youtu.be/4CV8yVzqWxk?t=2400)：
$$\sigma_2:\zeta_5\mapsto\zeta_5^2\mapsto\zeta_5^4\mapsto\zeta_5^8 = \zeta_5^3\mapsto\zeta_5^6 = \zeta_5$$
  ⇒ $\sigma_2$ 階 4，是生成元。【課堂討論】「4 階循環群有幾個生成元？」「$\varphi(4) = 2$。」「另一個是？」學生：「$\sigma_4$。」老師先說對，再算：$\sigma_2^3 = \sigma_3$（送 $\zeta_5\mapsto\zeta_5^3$）——**$\sigma_3$** 才是另一個生成元；$\sigma_2^2 = \sigma_4$，像 $\mathbb{Z}_4$ 裡的 2。
- **子群格**[▶ 44:30](https://youtu.be/4CV8yVzqWxk?t=2670)：【課堂討論】「$\mathbb{Z}_4$ 有幾個非平凡真子群？」學生：「2？」「真的、非平凡的？」「1。」⇒ 只有 $\{1,\sigma_4\}$。
  - 「Klein 四元群有**三個** 2 階子群、三個固定體；這個也是 4 次擴張，卻只有**一個**中間體。」
$$\{1\}\subset\{1,\sigma_4\}\subset G\qquad\longleftrightarrow\qquad\mathbb{Q}(\zeta_5)\supset\mathbb{Q}(\sqrt5)\supset\mathbb{Q}.$$
- **固定體**：$K^{\{1,\sigma_4\}} = \mathbb{Q}(\zeta_5+\zeta_5^{-1}) = \mathbb{Q}(\sqrt5)$。$\sigma_4(\zeta_5+\zeta_5^{-1}) = \zeta_5^4+\zeta_5^{-4} = \zeta_5^{-1}+\zeta_5$ ✓。
  - 【口頭】[▶ 47:00](https://youtu.be/4CV8yVzqWxk?t=2820)「如果我不告訴你，**找這個固定體**是有挑戰的吧？之前的例子固定體**擺在眼前**。這個**有趣**：Galois 群幾乎**免費**得到，固定體卻難——跟之前的難度**對偶**。」「為什麼 $\zeta_5+\zeta_5^{-1}$ 生成的跟加 $\sqrt5$ 一樣？**我一時不知道**。留作謎題。」

💬 謎題解答：$\zeta_5+\zeta_5^{-1} = 2\cos72° = \frac{\sqrt5-1}2$（$\zeta_5$ 的實部是 $\frac{\sqrt5-1}4$，見 [[23-L20-分圓體與Galois理論開始]]）。或者：令 $u = \zeta_5+\zeta_5^{-1}$，由 $1+\zeta+\zeta^2+\zeta^3+\zeta^4 = 0$ 除以 $\zeta^2$ 得 $u^2+u-1 = 0$ ⇒ $u = \frac{-1\pm\sqrt5}2$。所以 $\mathbb{Q}(u) = \mathbb{Q}(\sqrt5)$。

---

## 6. 有理化分母：共軛與 Bézout

[▶ 48:30](https://youtu.be/4CV8yVzqWxk?t=2910)「剩下的時間（學生：『負 4 分鐘。』『不，我才講 49 分鐘，還有 10 分鐘。』『那**不是**這樣算的。』『**就是**這樣算的。』）講上次那個問題：怎麼有理化 $\frac1{2+\sqrt[3]7}$？平方根我們都會。」

**複數共軛**[▶ 49:30](https://youtu.be/4CV8yVzqWxk?t=2970)：$(2+3i)(2-3i) = 4+9 = 13$ ⇒ $\frac1{2+3i} = \frac{2-3i}{13}$。

**$\sqrt3$**：$(2+\sqrt3)(2-\sqrt3) = 4-3 = 1$ ⇒ $\frac1{2+\sqrt3} = 2-\sqrt3$。（老師先寫成 $2-3 = -1$；學生：「$2\times2$ 是 4。」「喔對。」）

**立方根：Galois 共軛**[▶ 51:30](https://youtu.be/4CV8yVzqWxk?t=3090)：$x^3-2 = (x-\sqrt[3]2)(x-\rho\sqrt[3]2)(x-\rho^2\sqrt[3]2)$，代 $x = 3$：
$$25 = (3-\sqrt[3]2)(3-\rho\sqrt[3]2)(3-\rho^2\sqrt[3]2)\ ⇒\ \frac1{3-\sqrt[3]2} = \frac{(3-\rho\sqrt[3]2)(3-\rho^2\sqrt[3]2)}{25}.$$
- 【口頭】「看出這是**推廣**嗎？二次體裡 Galois 群只有 2 階，**只有一個**共軛——在 $\mathbb{C}$ 就是複數共軛，在 $\mathbb{Q}(\sqrt3)$ 是 $\sqrt3\mapsto-\sqrt3$。把 **Galois 共軛全乘起來**，必然落在**基體**裡。」
- 「但這跟我問的題目形式**不完全吻合**。」

**Bézout 方法**[▶ 54:30](https://youtu.be/4CV8yVzqWxk?t=3270)：$\mathbb{Q}(\sqrt[3]7)\cong\mathbb{Q}[x]/(x^3-7)$，$\alpha = x+I$ 扮演 $\sqrt[3]7$。要找 $(2+x)^{-1}$。
- $\gcd(x+2,x^3-7) = 1$ ⇒ **Bézout**：$a(x)(x+2)+b(x)(x^3-7) = 1$。在商裡 $x^3-7$ 那項變 0 ⇒ $(x+2)^{-1} = a(x)$。「**正是醫生開的藥方**——如他們所說，**money**。」
- 【口頭】[▶ 58:00](https://youtu.be/4CV8yVzqWxk?t=3480)「這方法**跟 Galois 理論幾乎無關**，但它是回答這類問題**穩健**的方法。我想給你們看 Galois 的做法。」（「我的**小**弟弟 Bill——我是**大**哥。」）

💬 算出來：$x^3-7 = (x+2)(x^2-2x+4)-15$ ⇒ $(x+2)(x^2-2x+4)\equiv15$ ⇒
$$\frac1{2+\sqrt[3]7} = \frac{\sqrt[3]{49}-2\sqrt[3]7+4}{15}.$$

**Bill 的 Maple 例子**[▶ 59:00](https://youtu.be/4CV8yVzqWxk?t=3540)：用「Galois 共軛技巧」求 $2+3\sqrt[3]2+\sqrt[3]4$ 的反元素——Maple 裡 $\omega$ 是主三次單位根、$\alpha$ 是正的 $\sqrt[3]2$……「我只剩不到一分鐘。」→ 續在 [[26-L23-Galois理論例子-下]]。

---

## 7. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $\mathbb{Q}(\sqrt2+\sqrt3) = \mathbb{Q}(\sqrt2,\sqrt3)$ | 只有 $\{1\}$ 固定它；$K^{\{1\}} = K$ |
| $V_4$ 的子群都正規 ↔ $\mathbb{Q}(\sqrt2),\mathbb{Q}(\sqrt3),\mathbb{Q}(\sqrt6)$ 都 Galois | 指標 2 |
| $S_3$：只有 $\langle\sigma\rangle$ 正規 ↔ 只有 $\mathbb{Q}(\rho)$ Galois | 共軛搬動 2 階子群 |
| $x^8-2$ 分裂體 $= \mathbb{Q}(\sqrt[8]2,i)$，16 次 | $\zeta_8\sqrt2 = 1+i$ |
| $\mathrm{Gal} = \langle\sigma,\tau\mid\sigma^8 = \tau^2 = 1,\sigma\tau = \tau\sigma^3\rangle$ | 擬二面體群；含 $D_8$、$\mathbb{Z}_8$、$Q_8$ |
| $\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})\cong(\mathbb{Z}/n)^\times$ | $\sigma_a\sigma_b = \sigma_{ab}$，核平凡 |
| $\mathrm{Gal}(\mathbb{Q}(\zeta_5)/\mathbb{Q})\cong\mathbb{Z}_4$，生成元 $\sigma_2,\sigma_3$ | 唯一中間體 $\mathbb{Q}(\sqrt5) = \mathbb{Q}(\zeta_5+\zeta_5^{-1})$ |
| 有理化：乘以其他 Galois 共軛 | $\frac1{3-\sqrt[3]2} = \frac{(3-\rho\sqrt[3]2)(3-\rho^2\sqrt[3]2)}{25}$ |
| 或用 Bézout | $a(x)(x+2)+b(x)(x^3-7) = 1$ |

| 中文 | English |
|---|---|
| 擬二面體群 | quasidihedral group |
| 四元數群 | quaternion group $Q_8$ |
| Galois 對應 | Galois correspondence |
| 有理化分母 | rationalize the denominator |
| 範數（共軛之積） | norm (product of conjugates) |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **Bill 的 Maple 共軛例子收尾** | [[26-L23-Galois理論例子-下]] |
| **多項式的 Galois 群、對稱函數** | [[28-L24-多項式的Galois群]] |
| **Abel 擴張、可解性** | [[29-L25-Galois理論結語]] |

---

## 附：本集一句話總結

> **Galois 對應立刻給出 $\mathbb{Q}(\sqrt2+\sqrt3) = \mathbb{Q}(\sqrt2,\sqrt3)$（只有恆等元固定 $\sqrt2+\sqrt3$），並解釋正規子群正好對應 Galois 子體（$V_4$ 全正規、$S_3$ 只有一個）；$x^8-2$ 的分裂體 $\mathbb{Q}(\sqrt[8]2,i)$ 是 16 次，Galois 群是擬二面體群；分圓體的 Galois 群是 $(\mathbb{Z}/n)^\times$，例如 $\mathbb{Q}(\zeta_5)$ 是 4 階循環群、唯一中間體是 $\mathbb{Q}(\sqrt5)$；最後把複數共軛推廣成 Galois 共軛來有理化含立方根的分母，也可以直接用 Bézout。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 23 錄影逐字稿前段（YouTube 自動字幕，59:51）與手寫講義 `Math422_Lecture23_FurtherExamplesGalois.pdf`（依 Dummit & Foote §14.2、§14.5）整理。*
