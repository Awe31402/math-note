---
course: Number Theory（2021 秋，線上錄影）
episode: 46
lecture: 2021-12-01 第 1 部
date: 2021-12-01
video: https://youtu.be/JbU-Ulsjcp8
notes: 講者講義沒有涵蓋（講義到 Lecture 30 為止）；本集講 Keith Conrad 的短文「Factoring in quadratic fields」（約 25 頁 PDF），定理編號照講者口述，該 PDF 不在本筆記的來源清單裡
---

# 第 46 集 · 二次體的整數、理想（How Ideals Fix Numbers, Part 1） [▶ 影片](https://youtu.be/JbU-Ulsjcp8)

← 上一集：[45-algebraic-extensions-degree-2](45-algebraic-extensions-degree-2.md) ｜ [總目錄](README.md) ｜ 下一集：[47-ideals-fix-numbers-2](47-ideals-fix-numbers-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 46 集（2021-12-01 第 1 部，感恩節後）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（59:51，whisper 轉錄；結尾被切斷）。講者照 Keith Conrad 的 PDF 講；那份 PDF 不在本筆記的來源裡，所以定理只寫講者在課堂上說的內容，編號照講者口述。
> **標記說明**：
> - `【口頭】` 講者口頭補充
> - `【課堂討論】` 講者問、學生答
> - `⚠️ 待確認` 查不清楚，列在最後的清單

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 問題：Z[√−14] 裡 15 = 3·5 = (1+√−14)(1−√−14)](#1-問題z14-裡-15--35--1141-14)
- [2. 為什麼唯一分解這麼重要](#2-為什麼唯一分解這麼重要)
- [3. 二次體、共軛、跡、範數](#3-二次體共軛跡範數)
- [4. 二次體的整數 O_K](#4-二次體的整數-o_k)
- [5. O_K 長什麼樣](#5-o_k-長什麼樣)
- [6. 整除與不可約](#6-整除與不可約)
- [7. 理想最多兩個生成元](#7-理想最多兩個生成元)
- [8. 例子：兩個生成元的理想其實是主理想](#8-例子兩個生成元的理想其實是主理想)
- [9. 理想的包含與乘法（開頭）](#9-理想的包含與乘法開頭)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/JbU-Ulsjcp8?t=0)

今天的標題是「**二次體中的分解**」（Factoring in quadratic fields），是 **Keith Conrad** 的「眾多短文之一」，約 25 頁。講者：「我會盡力至少講到它的總和，大概不會證很多定理。」

這份 PDF 回答：**用理想計算，怎麼修好我們在那些數系裡看到的問題**——也就是唯一分解失敗。講者 [▶ 08:23](https://youtu.be/JbU-Ulsjcp8?t=503)：「這是一份理想算術的入門，講理想怎麼運作、怎麼修補。我說的理想，就是我們最近一直在講的那些理想。」

---

## 1. 問題：Z[√−14] 裡 15 = 3·5 = (1+√−14)(1−√−14)

[▶ 01:18](https://youtu.be/JbU-Ulsjcp8?t=78)

**引導問題**：在 $\mathbb{Z}[\sqrt{-14}]$ 裡，
$$3,\quad 5,\quad 1+\sqrt{-14},\quad 1-\sqrt{-14}$$
都不能再分解（不可約，講者說「質的，意思是不能再約」），但
$$15 = 3\cdot5 = (1+\sqrt{-14})(1-\sqrt{-14}).$$

【課堂討論】[▶ 02:33](https://youtu.be/JbU-Ulsjcp8?t=153) 講者問：研究整數時我們用什麼？學生：範數。講者：「對，但在那之前，小學就用**質因數分解**。」關鍵：一個數的兩個質因數分解，用的質數必須一樣（順序和單位之外）。

這裡的因式**不相伴**，兩個分解不是彼此重排。所以 **$\mathbb{Z}[\sqrt{-14}]$ 不是 UFD**（第 39 集的語言）。

---

## 2. 為什麼唯一分解這麼重要

[▶ 04:11](https://youtu.be/JbU-Ulsjcp8?t=251)

- 課程前面 Stillwell 的很多論證是：「某個東西是平方，它也是質數的乘積；那個東西本身也有質因數分解，平方後所有質因數都是平方，所以另一邊也得是平方……」**存在質因數分解**、**互質的數怎麼配合平方**——這些是那些論證的螺絲釘。離開 UFD，這些論證全毀。
- 【口頭】Stillwell 有一整節用 **Eisenstein 整數**的代數結構，以反證法證明 $x^3+y^3 = z^3$ 沒有整數解（$n = 3$ 的費馬最後定理）。（講者手邊沒有 Stillwell，細節記不清。第 22–23 集。）
- **Lamé** 把它推廣到 $n$ 次單位根（**分圓整數**），給出 $x^n+y^n = z^n$ 無解的「證明」——但它依賴「分圓整數都是 UFD」，而它們不是 [▶ 07:23](https://youtu.be/JbU-Ulsjcp8?t=443)。「那本來會是費馬最後定理的漂亮證明。」
- Stillwell 推測 **Gauss** 很清楚這些不是 UFD，所以他不太願意用它們，即使 Lagrange、Euler 用代數整數得到很大的成功。（第 39 集的歷史。）

---

## 3. 二次體、共軛、跡、範數

[▶ 08:23](https://youtu.be/JbU-Ulsjcp8?t=503)

**定義**：$d$ 是**無平方因子**的整數（整份 PDF 都這樣假設）。

- **二次體**（quadratic field）：$K = \mathbb{Q}[\sqrt d] = \{x+y\sqrt d : x,y\in\mathbb{Q}\}$。
- $\mathbb{Z}[\sqrt d] = \{x+y\sqrt d : x,y\in\mathbb{Z}\}$。

（講者說這裡用方括號；$\mathbb{Q}[\sqrt d] = \mathbb{Q}(\sqrt d)$，第 40 集。）

**共軛** [▶ 09:53](https://youtu.be/JbU-Ulsjcp8?t=593)：$\alpha = x+y\sqrt d$，$\bar\alpha = x-y\sqrt d$。性質跟複數共軛一樣：
$$\overline{\alpha+\beta} = \bar\alpha+\bar\beta,\qquad\overline{\alpha\beta} = \bar\alpha\,\bar\beta,\qquad\bar{\bar\alpha} = \alpha.$$

**跡與範數** [▶ 10:25](https://youtu.be/JbU-Ulsjcp8?t=625)：
$$\mathrm{Tr}(\alpha) = \alpha+\bar\alpha,\qquad\mathrm{N}(\alpha) = \alpha\bar\alpha.$$

- 都是 $K\to\mathbb{Q}$ 的函數。講者：以前範數取整數值，現在取有理數值，因為集合比較大。
- **跡可加**：$\mathrm{Tr}(\alpha+\beta) = \mathrm{Tr}\alpha+\mathrm{Tr}\beta$；**範數可乘**：$\mathrm{N}(\alpha\beta) = \mathrm{N}\alpha\,\mathrm{N}\beta$。

（注意：這裡的範數**沒有絕對值**，$d>0$ 時可以是負的；跟第 38 集講義的 $|a^2-db^2|$ 不同。）

**每個二次體的元素都是有理係數首一二次式的根** [▶ 12:25](https://youtu.be/JbU-Ulsjcp8?t=745)：
$$(x-\alpha)(x-\bar\alpha) = x^2-(\alpha+\bar\alpha)x+\alpha\bar\alpha = x^2-\mathrm{Tr}(\alpha)\,x+\mathrm{N}(\alpha).$$

【課堂討論】[▶ 14:25](https://youtu.be/JbU-Ulsjcp8?t=865) 為什麼跡和範數是有理數？設 $\alpha = a+b\sqrt d$：$\mathrm{Tr}\alpha = 2a$、$\mathrm{N}\alpha = a^2-db^2$，都在 $\mathbb{Q}$ 裡。

講者 [▶ 15:25](https://youtu.be/JbU-Ulsjcp8?t=925)：用擴張體的語言，這些元素的**次數最多 2**——是有理數（次數 1）或在 $\mathbb{Q}$ 上次數 2。「這就是叫它們**二次**數體的好理由。」

---

## 4. 二次體的整數 O_K

[▶ 16:28](https://youtu.be/JbU-Ulsjcp8?t=988)

**定義**：$\alpha\in K$ 叫做 **$K$ 的整數**（integer of $K$），如果 $x^2-\mathrm{Tr}(\alpha)x+\mathrm{N}(\alpha)$ 的係數是**整數**。換句話說：**跡和範數都是普通整數**。記號：
$$\mathcal{O}_K = \{K\text{ 的整數}\}.$$
（講者：「不是開玩笑，就是 O-K。」）

**例 1**：$\alpha = a+b\sqrt d\in\mathbb{Z}[\sqrt d]$ [▶ 18:01](https://youtu.be/JbU-Ulsjcp8?t=1081)：$\mathrm{Tr} = 2a$、$\mathrm{N} = a^2-db^2$，都是整數。所以 $\mathbb{Z}[\sqrt d]\subseteq\mathcal{O}_K$。

【Q&A】學生問 $\mathbb{Z}[\sqrt d]$ 是體嗎？講者：不是，通常不是。講者順口想了 $\mathbb{Z}(\frac12)$ 是什麼，「大概是 $\mathbb{Q}$，由質子體的考量……別追這隻兔子。」

**例 2**：$d\equiv1\ (\mathrm{mod}\ 4)$ [▶ 20:36](https://youtu.be/JbU-Ulsjcp8?t=1236)，$\alpha = \dfrac{1+\sqrt d}2$。

- 係數是 $\frac12$，不在 $\mathbb{Z}[\sqrt d]$ 裡。
- $\mathrm{Tr}\alpha = \frac12+\frac12 = 1$。
- $\mathrm{N}\alpha = \left(\frac12\right)^2-d\left(\frac12\right)^2 = \dfrac{1-d}4$ [▶ 22:00](https://youtu.be/JbU-Ulsjcp8?t=1320)。$d\equiv1\ (\mathrm{mod}\ 4)$ ⇒ $1-d = 4j$ ⇒ $\mathrm{N}\alpha = j$，整數。

所以這時 $\mathbb{Z}[\sqrt d]\subsetneq\mathcal{O}_K$：有一個「半整數」也是 $K$ 的整數。

---

## 5. O_K 長什麼樣

[▶ 23:42](https://youtu.be/JbU-Ulsjcp8?t=1422)

> **定理**（Conrad Theorem 3.4，依講者口述）：
> $$\mathcal{O}_K = \begin{cases}\mathbb{Z}[\sqrt d], & d\not\equiv1\ (\mathrm{mod}\ 4),\\[2pt] \mathbb{Z}[\omega] = \{a+b\omega : a,b\in\mathbb{Z}\},\quad\omega = \dfrac{1+\sqrt d}2, & d\equiv1\ (\mathrm{mod}\ 4).\end{cases}$$

統一記號 [▶ 25:20](https://youtu.be/JbU-Ulsjcp8?t=1520)：令 $\omega = \sqrt d$（$d\not\equiv1$）或 $\omega = \frac{1+\sqrt d}2$（$d\equiv1$），則**永遠** $\mathcal{O}_K = \{a+b\omega : a,b\in\mathbb{Z}\}$。（講者一度說成 $\omega = 1+\sqrt d$，後來更正。）

講者說這些「半整數」的東西在 **Eisenstein 整數**裡出現過。

**例子** [▶ 26:51](https://youtu.be/JbU-Ulsjcp8?t=1611)：

| $K$ | $d$ 模 4 | $\mathcal{O}_K$ |
|---|---|---|
| $\mathbb{Q}[i]$（$d=-1$） | 3 | $\mathbb{Z}[i]$（高斯整數） |
| $\mathbb{Q}[\sqrt2]$ | 2 | $\mathbb{Z}[\sqrt2]$ |
| $\mathbb{Q}[\sqrt5]$ | 1 | $\mathbb{Z}\left[\frac{1+\sqrt5}2\right]$ |
| $\mathbb{Q}[\sqrt{-14}]$ | 2 | $\mathbb{Z}[\sqrt{-14}]$ |

⚠️ 講者 [▶ 27:53](https://youtu.be/JbU-Ulsjcp8?t=1673) 說「我可能記錯 Eisenstein 整數那件事……我記得 Eisenstein 整數跟 $\mathbb{Q}(\sqrt3)$ 有關。我得回頭再宣布。」第 47 集沒有聽到更正。見待確認清單。

> 以下**不是逐字稿內容**，是依上面的定理推論的：Eisenstein 整數 $\mathbb{Z}[\omega_3]$（$\omega_3 = \frac{-1+\sqrt{-3}}2$，第 22 集）是 $\mathbb{Q}(\sqrt{-3})$ 的整數：$d = -3\equiv1\ (\mathrm{mod}\ 4)$，$\mathcal{O}_K = \mathbb{Z}\left[\frac{1+\sqrt{-3}}2\right]$，而 $\frac{1+\sqrt{-3}}2 = \omega_3+1$，兩個環相同。所以是 $\sqrt{-3}$ 不是 $\sqrt3$。這也解釋了第 22 集的現象：$\mathbb{Z}[\sqrt{-3}]$ 唯一分解失敗，但它**不是** $\mathbb{Q}(\sqrt{-3})$ 的整數全體；補上半整數的 Eisenstein 整數就有唯一分解。

> **定理**（Conrad Theorem 3.5，依講者口述）[▶ 28:53](https://youtu.be/JbU-Ulsjcp8?t=1733)：$\alpha\in\mathcal{O}_K$ ⇔ $\alpha$ 是某個整係數首一多項式 $x^2+mx+n$ 的根。

- 講者：Stillwell 不用跡和範數定義 $K$ 的整數，而是**把這個定理當定義**。
- 一半已經證了：$x^2-\mathrm{Tr}(\alpha)x+\mathrm{N}(\alpha)$ 就是這種多項式。另一半要「分情況、有點乏味的分析，我拒絕在這裡做」，在 PDF 第 3 頁。

---

## 6. 整除與不可約

> **定理**（Conrad Theorem 3.6，依講者口述）[▶ 30:59](https://youtu.be/JbU-Ulsjcp8?t=1859)：$m\in\mathbb{Z}$，$\alpha = a+b\omega\in\mathbb{Z}[\omega]$。則 $m\mid\alpha$（在 $\mathcal{O}_K$ 裡）⇔ $m\mid a$ 且 $m\mid b$。

講者：普通整數要整除這種新數，只能**兩部分都整除**。例：$3\nmid5+\sqrt{-6}$，因為 $3\nmid5$（也 $3\nmid1$）。

**其他定理**（講者「盡量簡短總結」）[▶ 33:01](https://youtu.be/JbU-Ulsjcp8?t=1981)：

- $\mathcal{O}_K\cap\mathbb{Q} = \mathbb{Z}$：既是 $K$ 的整數又是有理數的，就是普通整數。「沒有奇怪的新有理數在這個定義下變成整數，很好。」
- $\alpha$ 是整數 ⇒ $\bar\alpha$ 也是。
- **$\mathrm{N}(\alpha)$ 是 $\mathbb{Z}$ 的質數（取絕對值）⇒ $\alpha$ 在 $\mathcal{O}_K$ 裡不可約。**（跟第 38 集一樣。）

**例** [▶ 34:36](https://youtu.be/JbU-Ulsjcp8?t=2076)：$\mathrm{N}(3+\sqrt{-14}) = 9-(-14)\cdot1 = 23$。（講者先算成 $9-14 = -5$，「我搞錯了，是 $a^2-db^2$，虛二次體是加號」。）23 是質數，所以 $3+\sqrt{-14}$ 不可約。順帶：$\mathbb{Z}[\sqrt{14}]$ 裡 $\mathrm{N}(3+\sqrt{14}) = -5$，也是質數（的負數），所以也不可約。

（⚠️ 字幕講者說「質範數 ⇒ **質**」，依前後文和 Conrad 的定理應是「⇒ **不可約**」。屬口誤，不列進待確認清單。）

**反方向不對** [▶ 36:38](https://youtu.be/JbU-Ulsjcp8?t=2198)：$\mathrm{N}(3) = 9$ 不是質數，但 3 在 $\mathbb{Z}[\sqrt{-14}]$ 裡不可約（Conrad Example 3.14）。

**$1+\sqrt{-14}$ 不可約**（Conrad Example 3.15）[▶ 37:38](https://youtu.be/JbU-Ulsjcp8?t=2258)：$\mathrm{N} = 1+14 = 15$，不是質數，但還是不可約。講者證明：

1. 設 $1+\sqrt{-14} = \alpha\beta$。$15 = \mathrm{N}\alpha\,\mathrm{N}\beta$。
2. $15 = 3\cdot5$，整數的唯一分解 ⇒ 若都不是單位，不妨 $\mathrm{N}\alpha = 3$（或 5）。
3. $a^2+14b^2 = 3$ 或 $5$ [▶ 39:39](https://youtu.be/JbU-Ulsjcp8?t=2379)：$b\neq0$ 就已經 $\ge14$，所以 $b = 0$；$a^2 = 3$ 或 $5$——$a = 0,\pm1,\pm2,\pm3$ 給 $0,1,4,9$，「我們從沒碰到 3 或 5」。
4. 所以沒有範數 3 或 5 的元素，$1+\sqrt{-14}$ 不可約。

（同樣的論證證明 3、5、$1-\sqrt{-14}$ 也不可約：它們的範數 9、25、15 只能拆成 $3\cdot3$、$5\cdot5$、$3\cdot5$。這句**不是逐字稿內容**。）

> **定理**（依講者口述）[▶ 40:40](https://youtu.be/JbU-Ulsjcp8?t=2440)：$\mathcal{O}_K$ 裡每個非單位都是不可約元的乘積。

- 有些二次體，例如 $\mathbb{Q}[i]$、$\mathbb{Q}[\sqrt2]$，整數**有**唯一分解。
- 但常常**沒有**，例如今天開頭的 $\mathbb{Q}[\sqrt{-14}]$。
- 講者記不得 Conrad 談高斯整數的短文有沒有證唯一分解，「但它可以證」（第 19 集）。

---

## 7. 理想最多兩個生成元

[▶ 42:50](https://youtu.be/JbU-Ulsjcp8?t=2570)（Conrad 第 4 節）

講者：一般的理想比較複雜，但**二次數體裡的理想其實很溫順**，Conrad 給了很細的結構描述。

> **定理**（Conrad Theorem 4.1，依講者口述）[▶ 43:22](https://youtu.be/JbU-Ulsjcp8?t=2602)：$\mathcal{O}_K$ 的每個理想都是有限生成的，**最多兩個生成元**。

**證明概要**（「部分是為下學期吊胃口」）[▶ 44:31](https://youtu.be/JbU-Ulsjcp8?t=2671)：

1. 理想首先是加法子群。
2. 作為加法群，$\mathcal{O}_K\cong\mathbb{Z}\times\mathbb{Z}$：$a+b\omega\mapsto(a,b)$。
3. $\mathbb{Z}\times\mathbb{Z}$ 的子群是 $0$、$\mathbb{Z}$ 或 $\mathbb{Z}^2$ 的樣子（同構意義下），所以最多兩個生成元。這靠**有限生成 Abel 群的分類**。

（作為加法群最多兩個生成元，作為理想當然也最多兩個。這句**不是逐字稿內容**。）

**記號** [▶ 46:03](https://youtu.be/JbU-Ulsjcp8?t=2763)：
$$(\alpha_1,\dots,\alpha_m) = \{\alpha_1\gamma_1+\cdots+\alpha_m\gamma_m : \gamma_i\in\mathcal{O}_K\}.$$
講者：跟我們在環上定義生成理想一樣（例如第 29 集的 $\langle x,y\rangle$），「這其實不是更一般，而是特殊化」。

---

## 8. 例子：兩個生成元的理想其實是主理想

[▶ 47:42](https://youtu.be/JbU-Ulsjcp8?t=2862)（Conrad Example 4.2）

講者：「細講要 10 分鐘，我沒有 10 分鐘……」結果還是講了（「既然寫了這麼多，我就會被拖進去」）：

$$\left(17+2\sqrt{-14},\ 20+\sqrt{-14}\right) = \left(3-\sqrt{-14}\right).$$

**右邊 ⊇ 左邊**：在 $\mathbb{Z}[\sqrt{-14}]/(3-\sqrt{-14})$ 裡算 [▶ 48:43](https://youtu.be/JbU-Ulsjcp8?t=2923)。講者喜歡 Conrad 的寫法：不寫陪集，只寫代表元——**在這個空間裡 $\sqrt{-14} = 3$**。

- 平方：$-14 = 9$，所以 $23 = 0$。
- $17+2\sqrt{-14} = 17+6 = 23 = 0$ [▶ 49:45](https://youtu.be/JbU-Ulsjcp8?t=2985)，所以 $3-\sqrt{-14}\mid17+2\sqrt{-14}$。（「我們用的是同餘和整除的關係。」）
- $20+\sqrt{-14} = 20+3 = 23 = 0$，所以 $3-\sqrt{-14}\mid20+\sqrt{-14}$。
- 它整除兩個生成元，就整除它們的線性組合。所以左邊 $\subseteq$ 右邊。

**左邊 ⊇ 右邊** [▶ 52:48](https://youtu.be/JbU-Ulsjcp8?t=3168)：模掉左邊兩個生成元，$\sqrt{-14} = -20$；Conrad 在一句話裡說明這推出 $23 = 0$，所以 $3-\sqrt{-14} = 3+20 = 23 = 0$。講者說「我沒全部展示」。

> 以下**不是逐字稿內容**，是把兩個方向寫成明確的等式（已驗算）：
> - $23 = (3-\sqrt{-14})(3+\sqrt{-14})$，而
>   $$17+2\sqrt{-14} = (3-\sqrt{-14})(1+\sqrt{-14}),\qquad 20+\sqrt{-14} = (3-\sqrt{-14})(2+\sqrt{-14}).$$
>   所以左邊 $\subseteq$ 右邊。
> - $23 = 2(20+\sqrt{-14})-(17+2\sqrt{-14})$，所以 $23$ 在左邊；$3-\sqrt{-14} = 23-(20+\sqrt{-14})$ 也在左邊。所以右邊 $\subseteq$ 左邊。

【Q&A】[▶ 49:13](https://youtu.be/JbU-Ulsjcp8?t=2953) 學生問：$\mathbb{Z}[\sqrt{-14}]/(3-\sqrt{-14})$ 同構於 $\mathbb{Z}_{23}$ 嗎？講者：「我不知道，我猜不是。」

> 以下**不是逐字稿內容**，是依本集的計算推論的：**是**，同構於 $\mathbb{Z}_{23}$。商環裡 $\sqrt{-14} = 3$，所以每個 $a+b\sqrt{-14}$ 都等於整數 $a+3b$，商環是 $\mathbb{Z}$ 的商 $\mathbb{Z}/n\mathbb{Z}$，$n$ 是理想裡最小的正整數。$23$ 在理想裡，23 是質數，而 $1$ 不在（否則 $3-\sqrt{-14}$ 是單位，但它的範數是 $23\neq1$）。所以 $n = 23$。

---

## 9. 理想的包含與乘法（開頭）

**用生成元判斷包含** [▶ 55:32](https://youtu.be/JbU-Ulsjcp8?t=3332)：講者說 Conrad 用德文花體字母 $\mathfrak{a},\mathfrak{b}$ 寫理想，「我寫不好」。設 $\mathfrak{a} = (\alpha_1,\dots,\alpha_m)$、$\mathfrak{b} = (\beta_1,\dots,\beta_n)$。下列等價：

- $\mathfrak{a}\subseteq\mathfrak{b}$；
- 每個 $\alpha_i\in\mathfrak{b}$；
- 每個 $\alpha_i$ 是 $\beta_j$ 的 $\mathcal{O}_K$ 線性組合。

講者：所以**只要檢查生成元**。要證兩個理想相等，檢查 $\alpha$ 都在 $\mathfrak{b}$、$\beta$ 都在 $\mathfrak{a}$。「像線性代數裡關於基底的論證，算是它的表親。」

**理想的乘法** [▶ 58:02](https://youtu.be/JbU-Ulsjcp8?t=3482)：講者一開始說「理想取代了數，用理想的算術就能修好數的性質壞掉的地方」。要做到這件事，先要會乘理想——它們是集合，怎麼乘集合？

**定義**：
$$\mathfrak{a}\mathfrak{b} = \left\{\sum_{j=1}^rx_jy_j : x_j\in\mathfrak{a},\ y_j\in\mathfrak{b}\right\}.$$
講者：這其實就是由 $\alpha_1\beta_1,\dots$ 生成的理想……（影片在這裡被切斷，接第 47 集。）

---

## 10. 一頁速查表

**問題**：$\mathbb{Z}[\sqrt{-14}]$ 裡 $15 = 3\cdot5 = (1+\sqrt{-14})(1-\sqrt{-14})$，四個都不可約、兩兩不相伴 ⇒ 不是 UFD。

**二次體** $K = \mathbb{Q}(\sqrt d)$（$d$ 無平方因子）：$\mathrm{Tr}\alpha = \alpha+\bar\alpha = 2a$，$\mathrm{N}\alpha = \alpha\bar\alpha = a^2-db^2$（可加／可乘）。$\alpha$ 是 $x^2-\mathrm{Tr}(\alpha)x+\mathrm{N}(\alpha)$ 的根。

**整數** $\mathcal{O}_K$ = 跡和範數都是整數的元素 = 整係數首一二次式的根。

$$\mathcal{O}_K = \mathbb{Z}[\omega],\qquad\omega = \begin{cases}\sqrt d & d\not\equiv1\ (\mathrm{mod}\ 4)\\ \frac{1+\sqrt d}2 & d\equiv1\ (\mathrm{mod}\ 4)\end{cases}$$
**關鍵一步**：$d\equiv1$ 時 $\mathrm{N}\left(\frac{1+\sqrt d}2\right) = \frac{1-d}4\in\mathbb{Z}$。

**整除**：$m\mid a+b\omega\iff m\mid a,\ m\mid b$。**不可約**：$|\mathrm{N}\alpha|$ 是質數 ⇒ 不可約（反之不對：$3$、$1+\sqrt{-14}$）。

**理想**：最多兩個生成元（$\mathcal{O}_K\cong\mathbb{Z}^2$ 加法群）。$\mathfrak{a}\subseteq\mathfrak{b}$ ⇔ $\mathfrak{a}$ 的生成元都在 $\mathfrak{b}$。例：$(17+2\sqrt{-14},20+\sqrt{-14}) = (3-\sqrt{-14})$，**關鍵一步**：模 $3-\sqrt{-14}$ 時 $\sqrt{-14} = 3$、$23 = 0$。

**理想乘法**：$\mathfrak{a}\mathfrak{b}$ = 有限個 $xy$ 的和（$x\in\mathfrak{a}$、$y\in\mathfrak{b}$）。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 理想乘法 = 生成元兩兩相乘；整除 ⇔ 包含 | 第 47 集 |
| $(15) = P\bar PQ\bar Q$：理想的唯一分解修好 $15$ 的兩種分解 | 第 47 集 |
| $\mathcal{O}_K$ 是 UFD ⇔ PID | 第 47 集 |

---

## 附：本集一句話總結

> **$\mathbb{Z}[\sqrt{-14}]$ 裡 $15 = 3\cdot5 = (1+\sqrt{-14})(1-\sqrt{-14})$，四個因式都不可約，唯一分解壞了——而課程前面很多論證都靠它。Conrad 的修法從「二次體的整數」開始：跡和範數都是整數的元素，恰好是 $\mathbb{Z}[\omega]$（$d\equiv1\ (\mathrm{mod}\ 4)$ 時多了半整數）。這裡的理想最多兩個生成元，判斷包含只要看生成元；接下來要用理想的乘法取代數的乘法。**

---

## ⚠️ 待確認清單

1. [▶ 27:53](https://youtu.be/JbU-Ulsjcp8?t=1673) 講者說他可能把 Eisenstein 整數所屬的二次體記錯（他說「跟 $\mathbb{Q}(\sqrt3)$ 有關」），說會再宣布，但第 47 集沒有聽到更正。筆記依定理推論是 $\mathbb{Q}(\sqrt{-3})$；講者有沒有在其他場合更正，待確認。

---

*筆記依據 James S. Cook「Number Theory」2021-12-01 第 1 部錄影逐字稿（whisper 轉錄，59:51）整理；課堂內容出自 Keith Conrad「Factoring in quadratic fields」，該 PDF 未列入本筆記來源，定理編號照講者口述。*
