---
course: Abstract Algebra II (Spring 2026)
episode: 25
lecture: L22
date: 2026-03-13
video: https://www.youtube.com/watch?v=XzUDV4DVU0A
notes: 講義/AA2/Math422_Lecture22_FundamentalTheoremGalois.pdf
---

# 第 25 集 · L22：Galois 理論基本定理 [▶ 影片](https://www.youtube.com/watch?v=XzUDV4DVU0A&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[24-L21-Galois擴張與Galois群]] ｜ [總目錄](../README.md) ｜ 下一集：[[26-L23-Galois理論例子-下]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 25 集，Lecture 22
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（57:24，自動字幕）＋ 手寫講義 `Math422_Lecture22_FundamentalTheoremGalois.pdf`（8 頁），依 Dummit & Foote §14.2。前 40 分鐘黑板，後面投影。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 回顧：ℚ(√2, √3) 的兩個格](#0-回顧ℚ2-3-的兩個格)
- [1. x³ − 2 的分裂體：生成元與基底](#1-x³--2-的分裂體生成元與基底)
- [2. 六個自同構；σ 的完整公式](#2-六個自同構σ-的完整公式)
- [3. στ = τσ²：Galois 群是 S₃](#3-στ--τσ²galois-群是-s₃)
- [4. 子群格與子體格](#4-子群格與子體格)
- [5. 背後的理論：特徵標與線性獨立](#5-背後的理論特徵標與線性獨立)
- [6. Galois 共軛；Galois 理論基本定理](#6-galois-共軛galois-理論基本定理)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 回顧：ℚ(√2, √3) 的兩個格

[▶ 00:00](https://youtu.be/XzUDV4DVU0A?t=0)（開課前大家在分薄荷糖。）課前禱告：「幫助我們懂這個 **Galois 理論基本定理**。」（學生：「我討厭改變。」「也許**改變討厭你**。這是我的反射——我有個朋友，有人說討厭什麼，他總回『也許那東西討厭你』，不管是雨還是人。」）

[▶ 01:30](https://youtu.be/XzUDV4DVU0A?t=90)（講義 p.1）上次的 $K = \mathbb{Q}(\sqrt2,\sqrt3)$：
$$\begin{matrix}&\{1\}&\\ \langle\tau\rangle&\langle\sigma\tau\rangle&\langle\sigma\rangle\\ &\{1,\sigma,\tau,\sigma\tau\}&\end{matrix}\qquad\qquad\begin{matrix}&\mathbb{Q}(\sqrt2,\sqrt3)&\\ \mathbb{Q}(\sqrt2)&\mathbb{Q}(\sqrt6)&\mathbb{Q}(\sqrt3)\\ &\mathbb{Q}&\end{matrix}$$
每條邊都是 2。$\sigma\sqrt2 = -\sqrt2$、$\sigma\sqrt3 = \sqrt3$；$\tau\sqrt2 = \sqrt2$、$\tau\sqrt3 = -\sqrt3$。
- 【課堂討論】[▶ 05:30](https://youtu.be/XzUDV4DVU0A?t=330)「哪個固定 $\sqrt2$？」「$\tau$。」⇒ $K^{\langle\tau\rangle} = \mathbb{Q}(\sqrt2)$；$K^{\langle\sigma\rangle} = \mathbb{Q}(\sqrt3)$。
- $\sigma\tau(\sqrt6) = \sigma\tau(\sqrt2\sqrt3)$：$\tau$ 給 $-\sqrt2\sqrt3$ 的一個負號，$\sigma$ 再給一個 ⇒ 兩個負號 ⇒ $\sqrt6$ ⇒ $K^{\langle\sigma\tau\rangle} = \mathbb{Q}(\sqrt6)$。
- 【口頭】[▶ 07:00](https://youtu.be/XzUDV4DVU0A?t=420)「注意有件**怪事**：子群圖通常最大的群在上面，這裡卻是**倒過來**畫的；體塔則是正常畫法。但兩者**顯然對應**：Galois 群的子群有個固定體，是 Galois 體的子體。」

---

## 1. x³ − 2 的分裂體：生成元與基底

**例 1**（講義 p.2）[▶ 08:00](https://youtu.be/XzUDV4DVU0A?t=480)「這會花點功夫。」上次 $\mathrm{Aut}(\mathbb{Q}(\sqrt[3]2)) = \{1\}$，「不太有趣」；分裂體會**刺激得多**。
- 【課堂討論】「$x^3-2$ 的根？」「$\sqrt[3]2$。」「很好。還有 $\rho\sqrt[3]2$、$\rho^2\sqrt[3]2$。」**$\rho$** 是暫時的記號：$\rho = \zeta_3 = e^{2\pi i/3} = \frac{-1+i\sqrt3}2$。
  - （「我說 sigma 了？sigma sigma sigma，**開心了吧**。」「有群國中游泳隊員在看我的影片，不知為何。聽說亂用 sigma 這個字有某種**污名**，是**腦腐**宇宙的一部分。」學生：「sigma 有點**過時**了。」「**去年**的。」）
- $K = \mathbb{Q}(\sqrt[3]2,\rho\sqrt[3]2,\rho^2\sqrt[3]2)$——「要算自同構，我們想要**更精簡**的描述」：
  - $\rho^2\sqrt[3]2/\rho\sqrt[3]2 = \rho$ ⇒ $\rho\in K$；$\rho,\sqrt[3]2$ 生成三個根 ⇒ **$K = \mathbb{Q}(\sqrt[3]2,\rho)$**。
  - D&F 也用 $\mathbb{Q}(\sqrt[3]2,\rho\sqrt[3]2)$。【課堂討論】[▶ 14:30](https://youtu.be/XzUDV4DVU0A?t=870)「為什麼這也行？第三個根從哪來？」學生：「$\rho\sqrt[3]2$ 除以 $\sqrt[3]2$ 得 $\rho$，就能造出 $\rho^2\sqrt[3]2$。」「很好。我寫講義時是用 $(\rho\sqrt[3]2)^2/\sqrt[3]2 = \rho^2\sqrt[3]2$，你的也很好。」
- 【課堂討論】[▶ 16:00](https://youtu.be/XzUDV4DVU0A?t=960)「分裂體幾次？不是 3。」「$3\times2 = $ **6**。」$\mathbb{Q}$-基底：
$$1,\ \sqrt[3]2,\ \sqrt[3]4,\ \rho,\ \rho\sqrt[3]2,\ \rho\sqrt[3]4.$$
  （「$\sqrt[3]4$ 比 $(\sqrt[3]2)^2$ 好寫。」學生：「為什麼叫 $K$？」「歡迎來到**我的世界**。」）

---

## 2. 六個自同構；σ 的完整公式

[▶ 18:00](https://youtu.be/XzUDV4DVU0A?t=1080)（講義 p.2）任一自同構必須把根送到**同一不可約多項式的根**：
- $\sqrt[3]2\mapsto\sqrt[3]2$、$\rho\sqrt[3]2$ 或 $\rho^2\sqrt[3]2$（$x^3-2$ 的根）。
- $\rho\mapsto\rho$ 或 $\rho^2$（$\Phi_3(x) = x^2+x+1$ 的根；$\deg\Phi_3 = 2$）。【課堂討論】「$\rho$ 能去哪？」「$\rho^2$。」
- 記得 $\rho^2 = -\rho-1$——「**有些地方會用到**」。
- 共 **6 種選擇**。「一般來說，生成元的每種『根到根』的指派**不一定**都定義出真正的自同構；但這裡**六個都是**，而且互不相同。」

> **定義**（講義 p.2）[▶ 22:00](https://youtu.be/XzUDV4DVU0A?t=1320)
> $$\sigma:\begin{cases}\sqrt[3]2\mapsto\rho\sqrt[3]2\\ \rho\mapsto\rho\end{cases}\qquad\tau:\begin{cases}\sqrt[3]2\mapsto\sqrt[3]2\\ \rho\mapsto\rho^2 = -1-\rho\end{cases}$$
> 生成元的命運決定基底的命運，因此決定整個自同構。

**例**[▶ 24:00](https://youtu.be/XzUDV4DVU0A?t=1440)【課堂討論】「$\sigma(\rho\sqrt[3]2)$？」「環同態，照常規則」：
$$\sigma(\rho\sqrt[3]2) = \sigma(\rho)\sigma(\sqrt[3]2) = \rho\cdot\rho\sqrt[3]2 = \rho^2\sqrt[3]2 = -\sqrt[3]2-\rho\sqrt[3]2.$$
（全班笑。「你們怎麼了？**Galois 理論**哪裡讓你們一直咯咯笑？」）

**$\sigma$ 的完整公式**（講義 p.3）[▶ 26:00](https://youtu.be/XzUDV4DVU0A?t=1560)：$\alpha = a+b\sqrt[3]2+c\sqrt[3]4+d\rho+e\rho\sqrt[3]2+f\rho\sqrt[3]4$ ⇒
$$\sigma\alpha = (a)+(-e)\sqrt[3]2+(f-c)\sqrt[3]4+d\rho+(b-e)\rho\sqrt[3]2-c\rho\sqrt[3]4.$$
- 拆開看：$\sigma\alpha = a\sigma(1)+b\sigma(\sqrt[3]2)+\cdots$。
- 「$\rho^2$ 不在基底裡（老師一度寫成 $\rho^2$，學生提醒）——要換成 $-1-\rho$。**你們中了我的陷阱，哈哈**。其實不是。」兩個 $-e$ 都來自剛才的計算。「其餘你們覺得推得出來嗎？」「好，很好，往下。」

💬 驗算其他項：$\sigma(\sqrt[3]4) = \rho^2\sqrt[3]4 = -\sqrt[3]4-\rho\sqrt[3]4$、$\sigma(\rho\sqrt[3]4) = \rho^3\sqrt[3]4 = \sqrt[3]4$，代入即得上式。

---

## 3. στ = τσ²：Galois 群是 S₃

**其餘自同構**（講義 p.3）[▶ 30:00](https://youtu.be/XzUDV4DVU0A?t=1800)
| | $\sqrt[3]2\mapsto$ | $\rho\mapsto$ |
|---|---|---|
| $1$ | $\sqrt[3]2$ | $\rho$ |
| $\sigma$ | $\rho\sqrt[3]2$ | $\rho$ |
| $\sigma^2$ | $\rho^2\sqrt[3]2$ | $\rho$ |
| $\tau$ | $\sqrt[3]2$ | $\rho^2$ |
| $\tau\sigma$ | $\rho^2\sqrt[3]2$ | $\rho^2$ |
| $\tau\sigma^2$ | $\rho\sqrt[3]2$ | $\rho^2$ |

- 【課堂討論】「$1$ 對 $\rho$ 做什麼？**沒人知道**？」「$\rho$。」「好答案。我問的就是**那種蠢問題**。」
- $\sigma^2$：$\sqrt[3]2\mapsto\rho\sqrt[3]2\mapsto\rho\cdot\rho\sqrt[3]2 = \rho^2\sqrt[3]2$。（老師在算時學生一直指黑板上方：「你們不讓我**把它推完**！」）
- $\tau\sigma$：$\sqrt[3]2\overset\sigma\mapsto\rho\sqrt[3]2\overset\tau\mapsto\rho^2\sqrt[3]2$——學生：「應該寫 $-\sqrt[3]2-\rho\sqrt[3]2$。」「你說得對。我寫 $\rho^2\sqrt[3]2$ 是因為**另一個塞不下**——技術上在基底外，但很方便。」

**$\sigma\tau$**[▶ 34:00](https://youtu.be/XzUDV4DVU0A?t=2040)【課堂討論】「誰先？」「$\tau$ 先。」
$$\sigma\tau:\ \sqrt[3]2\overset\tau\mapsto\sqrt[3]2\overset\sigma\mapsto\rho\sqrt[3]2;\qquad\rho\overset\tau\mapsto\rho^2\overset\sigma\mapsto\rho^2.$$
「看起來眼熟嗎？」「**$\tau\sigma^2$**。」⇒ $\sigma\tau = \tau\sigma^2$。（「我**需要休息**。」學生：「Fire。」「喔，fire，好。」）
- 【課堂討論】「$\sigma$ 幾次方是 1？$\tau$ 呢？」**$\sigma^3 = 1$**、**$\tau^2 = 1$**（$\rho\mapsto\rho^2\mapsto\rho^4 = \rho$）。所以 $\sigma\tau = \tau\sigma^{-1}$。
- 「6 階群，有 2 階元、3 階元，用這關係**纏在一起**——是什麼？」學生：「$D_3$。」「**你沒錯**。但通常叫？」「**$S_3$**。」「$D_n\cong S_n$ 只在 $n = 3$——那是唯一 $n! = 2n$ 的時候。**我把它想成三個東西的對稱群**。」

$$\mathrm{Gal}(\mathbb{Q}(\sqrt[3]2,\zeta_3)/\mathbb{Q}) = \langle\sigma,\tau\rangle\cong S_3.$$

---

## 4. 子群格與子體格

[▶ 38:00](https://youtu.be/XzUDV4DVU0A?t=2280)（改投影。學生：「Jacob 在問我該從哪本群論書開始讀。」「那是你們**整我**的主意吧？**任務完成**。」「他最不需要的就是**再一個分心的東西**。」）
- 【口頭】[▶ 40:30](https://youtu.be/XzUDV4DVU0A?t=2430)「以前我只**零碎地**做這些時，**非常困惑**。其實沒必要——細節**非常簡單**。但如果你分心了，例如把 $\rho\sqrt[3]4$ 寫成 $\rho^2\sqrt[3]2$，**壞事就會發生**。」
- [▶ 41:00](https://youtu.be/XzUDV4DVU0A?t=2460)「分裂體是 Galois 的：擴張是 **6** 次（老師先說 3，自己改正），Galois 群也是 6 階，**一切安好**。」

**格**（講義 p.4）
$$\begin{matrix}&&\langle1\rangle&&\\ \langle\sigma\rangle&&\langle\tau\rangle\ \ \langle\tau\sigma\rangle\ \ \langle\tau\sigma^2\rangle&&\\ &&\langle\sigma,\tau\rangle&&\end{matrix}\qquad\qquad\begin{matrix}&&K = \mathbb{Q}(\sqrt[3]2,\rho)&&\\ \mathbb{Q}(\rho)&&\mathbb{Q}(\sqrt[3]2)\ \ \mathbb{Q}(\rho\sqrt[3]2)\ \ \mathbb{Q}(\rho^2\sqrt[3]2)&&\\ &&\mathbb{Q}&&\end{matrix}$$
- 三個 2 階子群 $\langle\tau\rangle,\langle\tau\sigma\rangle,\langle\tau\sigma^2\rangle$；一個 3 階子群 $\langle\sigma\rangle$，**指標 2** ⇒ **正規**。
- 三個 3 次子體 $\mathbb{Q}(\sqrt[3]2)$、$\mathbb{Q}(\rho\sqrt[3]2)$、$\mathbb{Q}(\rho^2\sqrt[3]2)$；$\mathbb{Q}(\rho) = \mathbb{Q}(i\sqrt3)$ 是 2 次，再上去 3 次 ⇒ 共 6。

**固定體**（講義 p.4）[▶ 44:30](https://youtu.be/XzUDV4DVU0A?t=2670)
$$K^{\langle\tau\rangle} = \mathbb{Q}(\sqrt[3]2),\quad K^{\langle\tau\sigma\rangle} = \mathbb{Q}(\rho\sqrt[3]2),\quad K^{\langle\tau\sigma^2\rangle} = \mathbb{Q}(\rho^2\sqrt[3]2),\quad K^{\langle\sigma\rangle} = \mathbb{Q}(\rho).$$
- $\tau$ 顯然固定 $\sqrt[3]2$。$\tau\sigma(\rho\sqrt[3]2) = \tau(\rho^2\sqrt[3]2) = \rho^2\rho^2\sqrt[3]2 = \rho\sqrt[3]2$——「我不覺得明顯，但這計算說明了」。第三個「沒證，但用今天的公式**很容易**算出來」。

**哪些是 Galois？**[▶ 43:30](https://youtu.be/XzUDV4DVU0A?t=2610)
- 三個 3 次子體的自同構群都只有 $\{1\}$（上次算過 $\mathbb{Q}(\sqrt[3]2)$）⇒ **都不是** Galois。
- $\mathbb{Q}(\rho) = \mathbb{Q}(i\sqrt3)$：2 次，自同構是恆等和**複數共軛**（$i\sqrt3\mapsto-i\sqrt3$）⇒ **是** Galois。
- 【口頭】[▶ 45:30](https://youtu.be/XzUDV4DVU0A?t=2730)「$S_3$ 中**唯一正規**的子群 $\langle\sigma\rangle$，正好對應**唯一 Galois** 的子體 $\mathbb{Q}(\rho)$。所以**正規子群 ↔ Galois 子體**之間有某種對應。Galois 擴張裡不是每個子體都是 Galois——只有對應子群正規時才是。」

💬 老師說另外三個 2 階子群不正規「因為指標是 3」——指標 3 本身不代表不正規；真正原因是共軛會把它們互相搬動（$\sigma\tau\sigma^{-1}$ 不在 $\langle\tau\rangle$ 裡），老師接著也這樣說了。

---

## 5. 背後的理論：特徵標與線性獨立

[▶ 46:30](https://youtu.be/XzUDV4DVU0A?t=2790)「這些**模式**就是 Galois 理論基本定理。如果我教專門的 Galois 理論課，我們會花**一週**在我接下來 **3 分鐘**講的東西上，然後**逼你們**證它。我們不這樣做——那會很**刻薄**。」

（講義 p.5，D&F §14.2）
- **特徵標**（character）$\chi:G\to L^\times$，$\chi(g_1g_2) = \chi(g_1)\chi(g_2)$。把自同構看成 $K^\times\to L^\times$ 的特徵標（$K$ 嵌入 $L$）。整個故事是在判斷**不同自同構是否獨立**——可以用**線性代數**研究。
- **Cor 8**：體 $K$ 到 $L$ 的相異嵌入作為 $K$ 上的函數**線性獨立**；特別地，相異自同構線性獨立。
- **Thm 9**：$G = \{\sigma_1 = 1,\dots,\sigma_n\}\le\mathrm{Aut}(K)$，$F = K^G$ ⇒
$$[K:F] = [K:K^G] = n = |G|.$$
  - 【口頭】[▶ 48:30](https://youtu.be/XzUDV4DVU0A?t=2910)「D&F **沒寫成這樣**——我加了 $K^G$，因為這讓模式**直接打在你臉上**。他們的記號裡 $G$ 不顯現，我就比較難理解發生什麼——因為**我很笨**。」
  - 證明在 D&F p.570–571，**兩頁漂亮的線性代數**：「今天我**懂了**。本質上兩條故事線：一條反證 $[K:F]\not>n$，一條反證 $[K:F]\not<n$。造方程組、證它們過度或不足相依、把群**重新編號**……**真的真的很好玩**。但你們安全了。這**不是** Galois 理論課，是**有講** Galois 理論的課。」
- **Cor 10**：$K/F$ 有限 ⇒ $|\mathrm{Aut}(K/F)|\le[K:F]$，等號 $\iff F = K^{\mathrm{Aut}(K/F)}$。即 **$K/F$ Galois $\iff$ $F$ 是 $\mathrm{Aut}(K/F)$ 的固定體**。
- **Cor 11**：$G$ 是 $\mathrm{Aut}(K)$ 的有限子群、$F = K^G$ ⇒ $\mathrm{Aut}(K/F) = G$，$K/F$ Galois，$\mathrm{Gal}(K/K^G) = G$。
- **Cor 12**：相異有限子群 $G_1\neq G_2$ ⇒ $K^{G_1}\neq K^{G_2}$。

【講義補充】**Thm 13**（講義 p.6）：$K/F$ 是 Galois $\iff$ $K$ 是 $F$ 上某個**可分**多項式的分裂體。此時 $F$ 上任何在 $K$ 有一個根的不可約多項式都可分、且**所有根都在 $K$**（所以 $K/F$ 是可分擴張）。

---

## 6. Galois 共軛；Galois 理論基本定理

> **定義**（講義 p.6）[▶ 51:00](https://youtu.be/XzUDV4DVU0A?t=3060)　$K/F$ Galois，$\alpha\in K$。$\sigma\alpha$（$\sigma\in\mathrm{Gal}(K/F)$）叫 $\alpha$ 在 $F$ 上的**（Galois）共軛**。$E$ 是含 $F$ 的子體，$\sigma(E)$ 叫 $E$ 的**共軛體**。

- 「這些**非常有趣**，下次想多探索。」
- **支線任務（2 分）**[▶ 52:00](https://youtu.be/XzUDV4DVU0A?t=3120)：「你們試過**有理化分母裡的立方根**嗎？放假時試試：
$$\frac1{2+\sqrt[3]7}.$$
  可以做到。」學生：「我**問 AI** 就好。」「如果你想**抽掉所有樂趣**的話。」（「你**踢了一隻小狗**。」「你們**吸乾了我所有的力量**。」）「在 AI 之前的世界，這要花你一分鐘。」
  - （學生：「她一直在等『fundamental』——講題裡的那個字。」）

> **定理 14（Galois 理論基本定理）**（講義 p.7–8）[▶ 53:30](https://youtu.be/XzUDV4DVU0A?t=3210)　$K/F$ 是 Galois 擴張，$G = \mathrm{Gal}(K/F)$。則
> $$\{\text{含 }F\text{ 的子體 }E\subseteq K\}\ \longleftrightarrow\ \{\text{子群 }H\le G\}$$
> 是**雙射**，由 $E\mapsto\{G\text{ 中固定 }E\text{ 的元素}\}$、$H\mapsto K^H$ 給出，兩者**互逆**。在這對應下：
> 1. **包含反轉**：$H_2\le H_1\iff K^{H_1}\subseteq K^{H_2}$。
> 2. $[K:E] = [K:K^H] = |H|$，$[E:F] = [K^H:F] = [G:H]$。
> 3. $K/E$ 總是 Galois，$\mathrm{Gal}(K/E) = H$，即 $\mathrm{Gal}(K/K^H) = H$。
> 4. $E = K^H$ 在 $F$ 上 Galois $\iff$ $H\trianglelefteq G$。此時 $\mathrm{Gal}(E/F)\cong G/H$。
> 5. $E_1,E_2$ 對應 $H_1,H_2$ ⇒ $E_1\cap E_2$ 對應 $\langle H_1,H_2\rangle$，合成體 $E_1E_2$ 對應 $H_1\cap H_2$。所以子體格與子群格**對偶**（上下顛倒）。

- 【口頭】「顯然有對應：從子體到**固定它的** Galois 群元素；反方向從子群到它的**固定體**。互逆。上次證了**包含反轉**。」「我偏愛 $\mathrm{Gal}(E/K^H)\cong G/H$ 這個寫法。」
- [▶ 56:00](https://youtu.be/XzUDV4DVU0A?t=3360)「第 5 點——抱歉，Jacob，我**沒時間**了。」
- 【口頭】[▶ 56:30](https://youtu.be/XzUDV4DVU0A?t=3390)「**簡而言之，這就是 Galois 理論**。有趣的是，它讓我們能證明：一般的**五次**多項式方程**不可能用根號解**。這是我們接下來要的——回到它**原本被發展出來的目的**：討論多項式方程。」

---

## 7. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $\mathbb{Q}(\sqrt[3]2,\rho\sqrt[3]2,\rho^2\sqrt[3]2) = \mathbb{Q}(\sqrt[3]2,\rho)$ | 比值給 $\rho$ |
| 基底 $1,\sqrt[3]2,\sqrt[3]4,\rho,\rho\sqrt[3]2,\rho\sqrt[3]4$ | $3\times2 = 6$ |
| $\sigma:\sqrt[3]2\mapsto\rho\sqrt[3]2,\rho\mapsto\rho$；$\tau:\sqrt[3]2\mapsto\sqrt[3]2,\rho\mapsto\rho^2$ | 根到根 |
| $\sigma^3 = \tau^2 = 1$、$\sigma\tau = \tau\sigma^2$ | $\mathrm{Gal}\cong S_3$ |
| $\langle\sigma\rangle\trianglelefteq S_3$ ↔ $\mathbb{Q}(\rho)$ Galois | 唯一指標 2 子群 |
| $K^{\langle\tau\rangle} = \mathbb{Q}(\sqrt[3]2)$ 等三個 3 次子體不是 Galois | $\mathrm{Aut} = \{1\}$ |
| $[K:K^G] = |G|$ | 特徵標的線性獨立 |
| Galois ⟺ $F = K^{\mathrm{Aut}(K/F)}$ ⟺ 可分多項式的分裂體 | Cor 10、Thm 13 |
| **基本定理**：子體 ↔ 子群，包含反轉，$[E:F] = [G:H]$，正規 ↔ Galois，$\mathrm{Gal}(E/F)\cong G/H$ | Thm 14 |

| 中文 | English |
|---|---|
| 子群格；子體格 | subgroup lattice; subfield lattice |
| 特徵標 | character |
| 嵌入 | embedding |
| Galois 共軛；共軛體 | Galois conjugate; conjugate field |
| Galois 理論基本定理 | Fundamental Theorem of Galois Theory |
| 對偶 | dual |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **更多例子（$\mathbb{Q}(\zeta_8)$、$x^4-2$ 等）** | [[26-L23-Galois理論例子-下]]、[[27-L23-Galois理論例子-上]] |
| **多項式的 Galois 群、判別式** | [[28-L24-多項式的Galois群]] |
| **五次方程不可用根號解** | [[29-L25-Galois理論結語]] |

---

## 附：本集一句話總結

> **$x^3-2$ 的分裂體 $\mathbb{Q}(\sqrt[3]2,\rho)$ 是 6 次，自同構由 $\sqrt[3]2\mapsto\{\sqrt[3]2,\rho\sqrt[3]2,\rho^2\sqrt[3]2\}$、$\rho\mapsto\{\rho,\rho^2\}$ 決定，六種都成立；$\sigma^3 = \tau^2 = 1$、$\sigma\tau = \tau\sigma^2$ 給出 $S_3$，它的子群格倒過來正好是子體格，而唯一正規子群 $\langle\sigma\rangle$ 對應唯一 Galois 子體 $\mathbb{Q}(\rho)$；背後由特徵標的線性獨立證出 $[K:K^G] = |G|$，最後得到 Galois 理論基本定理：Galois 擴張的子體與 Galois 群的子群一一對應、包含反轉、次數 = 指標，正規子群對應 Galois 子擴張且 $\mathrm{Gal}(E/F)\cong G/H$。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 22 錄影逐字稿（YouTube 自動字幕，57:24）與手寫講義 `Math422_Lecture22_FundamentalTheoremGalois.pdf`（依 Dummit & Foote §14.2）整理。*
