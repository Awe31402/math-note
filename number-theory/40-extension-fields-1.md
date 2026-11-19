---
course: Number Theory（2021 秋，線上錄影）
episode: 40
lecture: 2021-11-10 第 1 部
date: 2021-11-10
video: https://youtu.be/edCfHBhMyz4
notes: 講者講義 Cook《Lecture Notes for Abstract Algebra I》（2018）§4.9 Lecture 29（p. 165–166、170）：Definition 4.9.1、Example 4.9.2–4.9.6、Theorem 4.9.7（Kronecker）、Example 4.9.8–4.9.9；雙曲數（p. 170）
---

# 第 40 集 · 擴張體、Kronecker 定理（Extension Fields, Part 1） [▶ 影片](https://youtu.be/edCfHBhMyz4)

← 上一集：[39-pids-euclidean-domains-ufds-2](39-pids-euclidean-domains-ufds-2.md) ｜ [總目錄](README.md) ｜ 下一集：[41-extension-fields-2](41-extension-fields-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 40 集（2021-11-10 第 1 部；YouTube 標題寫 Part 2，實際是第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，whisper 轉錄；23:42–25:15 字幕是亂碼；結尾被切斷）＋ 講者講義 §4.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，講義沒有
> - `【講義補充】` 講者講義有、課堂沒講
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 擴張體與體塔](#1-擴張體與體塔)
- [2. Q[√2] = Q(√2)：環已經是體](#2-q2--q2環已經是體)
- [3. R[x] 和 R(x)](#3-rx-和-rx)
- [4. 「子集合」其實是「同構的子集合」](#4-子集合其實是同構的子集合)
- [5. Kronecker 定理：每個多項式都有根（在某個擴張體裡）](#5-kronecker-定理每個多項式都有根在某個擴張體裡)
- [6. 不只是體：雙曲數](#6-不只是體雙曲數)
- [7. 例子：R[x]/⟨x² + 4x + 5⟩ ≅ C](#7-例子rxx--4x--5--c)
- [8. 例子：x⁴ − 5x² + 6（開頭）](#8-例子x--5x--6開頭)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/edCfHBhMyz4?t=0)

**回顧**（最近兩小時的課）：

- 交換環模**極大理想** ⇔ 得到**體**；模**質理想** ⇔ 得到**整環**。體是整環，所以極大 ⇒ 質。反過來不行：$\mathbb{Z}$ 是整環不是體（$\frac12\notin\mathbb{Z}$），所以有不是極大的質理想。
- Euclid 整環、PID、UFD 的關係。重點：$F[x]$ 是 Euclid 整環 ⇒ PID ⇒ UFD。
- 講者：「你們該把最近幾講的大定理寫出來帶著走。」接近第 3 次考試時他會說哪些證明要會。

今天開始**擴張體**（講義 Lecture 29，照 Fraleigh 第 29 節）。

---

## 1. 擴張體與體塔

[▶ 02:11](https://youtu.be/edCfHBhMyz4?t=131)

> **定義**（講義 Definition 4.9.1）：若 $F\subseteq E$，而且 $F$ 的運算就是 $E$ 的運算限制在 $F$ 上，就說體 $E$ 是 $F$ 的**擴張體**（extension field）。$F$ 叫**基體**（base field）。

**例子**（Ex 4.9.2–4.9.4）[▶ 03:39](https://youtu.be/edCfHBhMyz4?t=219)：

- $\mathbb{R}$ 是 $\mathbb{Q}$ 的擴張（同樣的加法、乘法）。
- $\mathbb{C}$ 是 $\mathbb{R}$ 的擴張。
- $\mathbb{C}$ 也是 $\mathbb{Q}$ 的擴張。

**體塔** [▶ 04:51](https://youtu.be/edCfHBhMyz4?t=291)：講者臨場編一個定理——若 $E$ 擴張 $F_1$、$F_1$ 擴張 $F$，則 $E$ 擴張 $F$。（「每次我臨場編都會出事」，字母一度搞混，「我是白痴」。）

證明基本上是集合論：$F\subseteq F_1\subseteq E$，$E$ 的運算給 $F_1$ 共用，所以也給 $F$ 共用。

- $F_1$ 叫**中間體**（intermediate field）。
- 這種圖叫**體塔**（tower of fields）：

$$\mathbb{Q}\subseteq\mathbb{R}\subseteq\mathbb{C}\qquad(\text{基體}\to\text{中間體}\to\text{擴張體})$$

---

## 2. Q[√2] = Q(√2)：環已經是體

[▶ 08:02](https://youtu.be/edCfHBhMyz4?t=482)（講義 Example 4.9.5）

講者說「這個我真該出成作業」：

- **方括號** $\mathbb{Q}[\sqrt2] = \{a+b\sqrt2 : a,b\in\mathbb{Q}\}$：添加 $\sqrt2$ 得到的**環**。
- **圓括號** $\mathbb{Q}(\sqrt2)$：包含 $\mathbb{Q}$ 和 $\sqrt2$ 的**最小的體**。

**這個環已經對反元素封閉** [▶ 09:38](https://youtu.be/edCfHBhMyz4?t=578)：分母有理化（「我這一兩週在中級代數課教的東西」）
$$\frac1{a+b\sqrt2} = \frac{a-b\sqrt2}{(a+b\sqrt2)(a-b\sqrt2)} = \frac{a-b\sqrt2}{a^2-2b^2}.$$

【課堂討論】[▶ 10:46](https://youtu.be/edCfHBhMyz4?t=646) 分母什麼時候是 0？$a^2-2b^2 = 0$ 要 $\frac ab = \pm\sqrt2$，有理數做不到（$a,b$ 不全為 0 時）。所以這個公式給出 $\mathbb{Q}[\sqrt2]$ 裡的元素，而且乘回去是 1。**每個非零元素都有反元素**，$\mathbb{Q}[\sqrt2]$ 已經是體。

**它是最小的** [▶ 12:17](https://youtu.be/edCfHBhMyz4?t=737)：

- 含 $\mathbb{Q}$（取 $b = 0$）和 $\sqrt2$（$a = 0$、$b = 1$）。
- 不能更小：特徵 0 的體一定含**質子體** $\mathbb{Q}$（第 32–33 集），也不能丟掉 $\sqrt2$。

所以 $\mathbb{Q}[\sqrt2] = \mathbb{Q}(\sqrt2)$，「但注意兩個記號**有意的**不同」。

> 【講義補充】Example 4.9.5（p. 165）：$\mathbb{Q}(\sqrt2)$ 是 $\mathbb{Q}$ 的擴張，$\mathbb{R}$ 又是 $\mathbb{Q}(\sqrt2)$ 的擴張：$\mathbb{Q}\subseteq\mathbb{Q}(\sqrt2)\subseteq\mathbb{R}$。

---

## 3. R[x] 和 R(x)

[▶ 13:51](https://youtu.be/edCfHBhMyz4?t=831)

- $\mathbb{R}[x]$：多項式（$x$ 是不定元）。
- $\mathbb{R}(x)$：包含 $\mathbb{R}$ 和 $x$、**也包含它的反元素**的最小的體。自然的看法是**有理函數** $\frac{f(x)}{g(x)}$（$f,g\in\mathbb{R}[x]$）。

【課堂討論】[▶ 14:58](https://youtu.be/edCfHBhMyz4?t=898) 非零的 $\frac fg$ 的反元素？$\frac gf$。所以有理函數都有反元素，裡面有 $x$ 也有 $\frac1x$。講者：它也是 $\mathbb{R}[x]$ 做**分式體**構造（第 34 集）得到的東西。

---

## 4. 「子集合」其實是「同構的子集合」

[▶ 15:59](https://youtu.be/edCfHBhMyz4?t=959)（講義 Example 4.9.6）

$E = \mathbb{Z}_2[x]/\langle x^2+x+1\rangle$ 是體（$x^2+x+1$ 不可約 ⇒ 理想極大 ⇒ 商是體），而且是 $\mathbb{Z}_2$ 的擴張。

**記號**（上次介紹的）：$\alpha = x+\langle x^2+x+1\rangle$，
$$E = \{a+b\alpha : a,b\in\mathbb{Z}_2\},\qquad\alpha^2+\alpha+1 = 0.$$

**講究一下** [▶ 17:31](https://youtu.be/edCfHBhMyz4?t=1051)：$\mathbb{Z}_2$ **嚴格來說**是 $E$ 的子集合嗎？$E$ 的元素是陪集，裡面有一組陪集 $\{0+I,\ 1+I\}$ 跟 $\mathbb{Z}_2$ 同構。所以「子集合」要理解成「**有一個子體跟 $F$ 同構**」。

講者 [▶ 18:31](https://youtu.be/edCfHBhMyz4?t=1111)：複數到底是什麼？

- $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ 形式的 $2\times2$ 矩陣？
- $\mathbb{R}[x]/\langle x^2+1\rangle$ 的陪集（多項式的等價類）？
- 平面上的實數對，配特定的乘法（Gauss 構造，「也許是 Argand」）？

「這些構造**沒有一個**真的把 $\mathbb{R}$ 當作字面上的子集合，但每個都有一個跟 $\mathbb{R}$ 環同構的子集合，我們就算它是。」如果你教條地認為子集合就是字面上的子集合，可能會困惑。「大家不想在定義裡講這些，因為想讓事情看起來比實際簡單。」

**添加新元素** [▶ 20:01](https://youtu.be/edCfHBhMyz4?t=1201)：$E$ 就是 $\mathbb{Z}_2$ 添加一個 $\alpha$，$\alpha^2+\alpha+1 = 0$。$\mathbb{Z}_2$ 裡沒有這種數：$0^2+0+1 = 1$、$1^2+1+1 = 1$。**$\alpha$ 是新的。**

**蠢例子** [▶ 21:03](https://youtu.be/edCfHBhMyz4?t=1263)：$\mathbb{R}$ 添加 $\pi$——$\pi$ 已經在裡面，還是 $\mathbb{R}$。$\mathbb{Q}$ 添加 $\frac12$，還是 $\mathbb{Q}$。**添加原本沒有的元素才有趣。**

---

## 5. Kronecker 定理：每個多項式都有根（在某個擴張體裡）

[▶ 21:33](https://youtu.be/edCfHBhMyz4?t=1293)

講者：這是 **Kronecker** 1887 年的定理。【課堂討論】學生問：是 Kronecker delta 那個 Kronecker 嗎？是。講者：「我猜他本人不覺得那有什麼大不了，大家才小題大作」——$\delta_{ij}$ 在 $i=j$ 時是 1、否則 0，是單位矩陣的分量，算內積要用的公式。

> **體論基本定理**（講義 Theorem 4.9.7，Kronecker 1887）：$F$ 是體，$f(x)\in F[x]$ 不是常數。則存在 $F$ 的擴張體 $E$，使 $f(x)$ 在 $E$ 裡有根。

**證明** [▶ 25:15](https://youtu.be/edCfHBhMyz4?t=1515)：

1. $\deg f\ge1$。**$F[x]$ 是 UFD**，所以 $f$ 能分解成不可約因式：$f(x) = p(x)g(x)$，$p$ 不可約 [▶ 25:45](https://youtu.be/edCfHBhMyz4?t=1545)。（「其他因式是什麼，對這個證明不重要。」）
2. 若 $p(\alpha) = 0$，則 $f(\alpha) = p(\alpha)g(\alpha) = 0$。**所以只要找 $\alpha$ 使 $p(\alpha) = 0$** [▶ 26:55](https://youtu.be/edCfHBhMyz4?t=1615)。（這裡 $p(\alpha) = \varphi_\alpha(p)$ 是擴張體上的求值同態。）
3. 設 $p(x) = a_nx^n+\cdots+a_1x+a_0$。令
   $$E = F[x]/\langle p(x)\rangle.$$
   $p$ 不可約 ⇒ $\langle p\rangle$ 極大 ⇒ **$E$ 是體** [▶ 28:49](https://youtu.be/edCfHBhMyz4?t=1729)。
4. 令 $\alpha = x+\langle p\rangle$。則 $\alpha^j = x^j+\langle p\rangle$（$j=2$ 直接乘開，再歸納）[▶ 29:53](https://youtu.be/edCfHBhMyz4?t=1793)。
5. 代進去 [▶ 30:55](https://youtu.be/edCfHBhMyz4?t=1855)：
   $$p(\alpha) = a_n\alpha^n+\cdots+a_0 = (a_nx^n+\langle p\rangle)+\cdots+(a_0+\langle p\rangle).$$
   陪集相加就是代表元相加：
   $$p(\alpha) = (a_nx^n+\cdots+a_1x+a_0)+\langle p\rangle = p(x)+\langle p\rangle = \langle p\rangle.$$
6. $\langle p\rangle$ 就是 $E$ 的 **0**。所以 $p(\alpha) = 0$，$f(\alpha) = 0$。∎

（講者寫到一半：「拜託告訴我我沒寫到另一塊板子上——呼，沒有。」又抱怨一直寫 $\langle p(x)\rangle$「寫得好累」。）

> 【講義補充】講義（p. 165）：「上面的證明告訴我們**怎麼造出一個體，讓給定的多項式有根**。」講義註腳：這裡的「體論」（field theory）跟物理的場論不是同一回事。

【Q&A】[▶ 34:14](https://youtu.be/edCfHBhMyz4?t=2054) 學生問：$F$ 一定要是體嗎？只是整環可以嗎？是 UFD 就行？講者：「我想**連那個都不需要**。」

【口頭】講者寫下一個（不是體論的）版本：$R$ 是有單位元的交換環，$f(x)\in R[x]$，則存在交換環 $\tilde R$ 和 $\alpha\in\tilde R$ 使 $f(\alpha) = 0$。

- 取 $\tilde R = R[x]/\langle f(x)\rangle$。$R[x]$ 不一定是整環（$R$ 的零因子會變成多項式的零因子），但商環的構造只要求**模掉一個理想**，$\langle f\rangle$ 還是理想（對減法封閉、超級封閉）[▶ 37:18](https://youtu.be/edCfHBhMyz4?t=2238)。
- 同樣的計算：$\alpha = x+\langle f\rangle$ 滿足 $f(\alpha) = 0$。
- 「如果你們能戳破它，歡迎。」

講者：這是講者研究裡要用的東西——交換環可以是一個**代數**，模掉多項式得到「同類型的代數，多了一個照我們意思行事的新元素」。體論版本多做的事：體 ⇒ UFD ⇒ 能找不可約因式 ⇒ 模極大理想 ⇒ 商是體，並且把 $F$ 跟常數多項式的陪集等同。

---

## 6. 不只是體：雙曲數

[▶ 40:00](https://youtu.be/edCfHBhMyz4?t=2400)（「原諒我，我有點不守規矩。」）

**雙曲數**（hyperbolic numbers）：$\mathcal{H} = \{a+bj : a,b\in\mathbb{R}\}$，$j^2 = 1$。$j$ 不是實數，就像虛數單位不是實數。

- 可以給雙曲數添加虛數單位：$\mathcal{H}[x]/\langle x^2+1\rangle$。
- 雙曲數裡**沒有**平方是 $-1$ 的元素（「可以證明」），但這個商裡有。
- 【口頭】講者提到一位研究夥伴的論文直接用 $k$ 代替 $x$：$\mathcal{H}$ 添加 $k$，元素像 $(a+bj)+k(c+dj)$。
- $\mathcal{H}$ 是 2 維實代數，添加 $k$ 後是 4 維實代數（向量空間的維度）。

**「代數」是什麼？** [▶ 42:43](https://youtu.be/edCfHBhMyz4?t=2563) 講者：「整門抽象代數課，你們有定義過**代數**嗎？沒有吧。」例如**有單位元的結合代數**：一個向量空間配上一個結合的乘法，跟純量乘法滿足分配律等，通常有乘法單位元。所以代數是環，又是向量空間。「我們看過的交換環大多不是向量空間。」

講者 [▶ 43:45](https://youtu.be/edCfHBhMyz4?t=2625)：**「把你想變成 0 的東西模掉」——取係數在這個物件上的多項式，再模掉描述新元素的多項式——是比體論一般得多的技巧。**

> 【講義補充】講義（p. 170）：$\mathbb{R}[x]/\langle x^2-1\rangle$ 裡 $j = x+\langle x^2-1\rangle$ 滿足 $j^2 = 1$；$a+bj$ 叫雙曲數。它們有點麻煩：$(1+j)(1-j) = 1-j^2 = 0$，但 $1\pm j\neq0$——**有零因子**（$x^2-1$ 可約，所以商不是體）。

---

## 7. 例子：R[x]/⟨x² + 4x + 5⟩ ≅ C

[▶ 44:23](https://youtu.be/edCfHBhMyz4?t=2663)（講義 Example 4.9.8）

$f(x) = x^2+4x+5 = (x+2)^2+1\in\mathbb{R}[x]$。沒有實根（$(x+2)^2+1\ge1$），2 次，所以不可約。

擴張：$E = \mathbb{R}[x]/\langle x^2+4x+5\rangle = \{a+b\alpha : a,b\in\mathbb{R}\}$，$\alpha = x+\langle f\rangle$，
$$\alpha^2+4\alpha+5 = 0.$$

**這個新體是什麼？**[▶ 46:31](https://youtu.be/edCfHBhMyz4?t=2791)「這變成一個有趣的問題：同構意義下它是什麼？」

**找出扮演 $i$ 的東西** [▶ 47:02](https://youtu.be/edCfHBhMyz4?t=2822)：$(\alpha+2)^2 = -1$。令 $i = \alpha+2$，則 $\alpha = i-2$，
$$a+b\alpha = a+b(i-2) = (a-2b)+bi.$$
講者：「我的直覺是這只是**複數的醜記號**。」

**提出同構**：
$$\psi:E\to\mathbb{C},\qquad\psi(a+b\alpha) = (a-2b)+bi.$$

「我說它是同構，但現在那裡有個巨大的問號。」講者檢查一部分 [▶ 49:10](https://youtu.be/edCfHBhMyz4?t=2950)：

- **1 對到 1**：$\psi(1+0\alpha) = 1-0+0i = 1$。
- **加法**：$a,b$ 線性地出現，容易驗證。
- **乘法**（「比較不平凡」）[▶ 50:50](https://youtu.be/edCfHBhMyz4?t=3050)：

  左邊：$\alpha^2 = -4\alpha-5$，
  $$(a+b\alpha)(c+d\alpha) = ac+(ad+bc)\alpha+bd\alpha^2 = (ac-5bd)+(ad+bc-4bd)\alpha.$$
  令 $\bar a = ac-5bd$、$\bar b = ad+bc-4bd$（講者：「不要跟虛構的大象巴巴 Babar 搞混。我一直看不進那部卡通，好無聊。」）：
  $$\psi(\cdots) = (\bar a-2\bar b)+\bar bi = (ac-5bd-2ad-2bc+8bd)+(ad+bc-4bd)i\qquad(\star)$$

  右邊 [▶ 53:55](https://youtu.be/edCfHBhMyz4?t=3235)：
  $$\big((a-2b)+bi\big)\big((c-2d)+di\big)$$
  實部 $= (a-2b)(c-2d)-bd = ac-2ad-2bc+3bd$；虛部 $= (a-2b)d+b(c-2d) = ad+bc-4bd$。$(\star\star)$

  比較：虛部一樣；實部 $-5bd+8bd = 3bd$，其他項也一樣。「**萬歲**。」

**講者的方法** [▶ 57:27](https://youtu.be/edCfHBhMyz4?t=3447)：要證兩個東西同構，找出**抓住它本質的那個東西**，把它對過去。「在我看來，虛數單位 $i$ 就是讓複數成為複數的東西。」找出誰在扮演 $i$，就能看出同構。「某種意義上，**同構就是換記號**。」

---

## 8. 例子：x⁴ − 5x² + 6（開頭）

[▶ 58:27](https://youtu.be/edCfHBhMyz4?t=3507)（講義 Example 4.9.9）

$$f(x) = x^4-5x^2+6 = (x^2-3)(x^2-2)\in\mathbb{Q}[x].$$
$f$ 在 $\mathbb{Q}$ 上**可約**。講者說會盡量簡短。（影片在這裡被切斷，接第 41 集。）

---

## 9. 一頁速查表

**擴張體** $E\supseteq F$：$F$ 是子體（同構意義下），共用運算。**體塔** $F\subseteq F_1\subseteq E$，$F_1$ 是中間體。

**記號**

| 記號 | 意思 |
|---|---|
| $F[\alpha]$ | 添加 $\alpha$ 的環（$\alpha$ 的多項式） |
| $F(\alpha)$ | 含 $F$ 和 $\alpha$ 的最小的體 |
| $\mathbb{R}(x)$ | 有理函數 = $\mathbb{R}[x]$ 的分式體 |

$\mathbb{Q}[\sqrt2] = \mathbb{Q}(\sqrt2)$。**關鍵一步**：$\dfrac1{a+b\sqrt2} = \dfrac{a-b\sqrt2}{a^2-2b^2}$，分母不為 0（$\sqrt2$ 無理）。

**Kronecker 定理**：體上的非常數多項式在某個擴張體裡有根。**關鍵一步**：取不可約因式 $p$，$E = F[x]/\langle p\rangle$ 是體，$\alpha = x+\langle p\rangle$ 滿足 $p(\alpha) = p(x)+\langle p\rangle = 0$。

**更一般**：交換環 $R$、$f\in R[x]$，$R[x]/\langle f\rangle$ 裡 $x+\langle f\rangle$ 是 $f$ 的根（不一定是體）。例：雙曲數 $\mathbb{R}[x]/\langle x^2-1\rangle$，$j^2 = 1$，$(1+j)(1-j) = 0$。

**找同構的方法**：找出扮演關鍵角色的元素。$\mathbb{R}[x]/\langle x^2+4x+5\rangle$：$(\alpha+2)^2 = -1$，$i = \alpha+2$，$\psi(a+b\alpha) = (a-2b)+bi$ 是到 $\mathbb{C}$ 的同構。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $x^4-5x^2+6$：$\mathbb{Q}(\alpha,\beta)$ | 第 41 集 |
| 代數元、超越元 | 第 41 集 |
| 最小多項式 $\mathrm{irr}(\alpha,F)$、$F(\alpha)$ 的基底 | 第 42–43 集 |
| 擴張的次數 $[E:F]$、塔定理 | 第 44–45 集 |

---

## 附：本集一句話總結

> **擴張體就是把小體當成子體（同構意義下）的大體，像 $\mathbb{Q}\subseteq\mathbb{Q}(\sqrt2)\subseteq\mathbb{R}\subseteq\mathbb{C}$。Kronecker 定理說：體上任何非常數多項式，都能在 $F[x]/\langle p(x)\rangle$（$p$ 是它的不可約因式）裡找到根——就是 $x$ 的陪集。這個「把想變成 0 的東西模掉」的技巧比體論更一般；而要看出新體是誰，就找扮演關鍵角色的元素，例如 $\mathbb{R}[x]/\langle x^2+4x+5\rangle$ 裡 $\alpha+2$ 就是 $i$。**

---

*筆記依據 James S. Cook「Number Theory」2021-11-10 第 1 部錄影逐字稿（whisper 轉錄，59:51）與講者講義《Lecture Notes for Abstract Algebra I》（2018）§4.9 整理。*
