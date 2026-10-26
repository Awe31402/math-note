---
course: Abstract Algebra II (Spring 2026)
episode: 28
lecture: L24
date: 2026-03-27
video: https://www.youtube.com/watch?v=RrHAN9FtXHI
notes: 講義/AA2/Math422_Lecture24_GaloisGroupPolynomials.pdf
---

# 第 28 集 · L24：多項式的 Galois 群、一般多項式 [▶ 影片](https://www.youtube.com/watch?v=RrHAN9FtXHI&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[27-L23-Galois理論例子-上]] ｜ [總目錄](../README.md) ｜ 下一集：[[29-L25-Galois理論結語]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 28 集，Lecture 24
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（57:12，自動字幕）＋ 手寫講義 `Math422_Lecture24_GaloisGroupPolynomials.pdf`（4 頁），後半依 Dummit & Foote §14.6。黑板為主。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 所有 Galois 共軛之積在基體裡](#1-所有-galois-共軛之積在基體裡)
- [2. Galois 群是 Sₙ 的子群](#2-galois-群是-sₙ-的子群)
- [3. 例：V₄ ≤ S₄、有理化 1/(1+3√2+4√3)](#3-例v₄--s₄有理化-11324√3)
- [4. 例：x³ − 2 的 Galois 群正好是 S₃](#4-例x³--2-的-galois-群正好是-s₃)
- [5. 基本對稱函數、一般多項式](#5-基本對稱函數一般多項式)
- [6. 一般多項式的 Galois 群是 Sₙ](#6-一般多項式的-galois-群是-sₙ)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/RrHAN9FtXHI?t=0) 課前禱告。「今天是 Lecture 24。**難得**有些東西**不在** D&F 裡。之後會回到 D&F。主題：**多項式的 Galois 群**。」

**設定**（講義 p.1）[▶ 00:30](https://youtu.be/RrHAN9FtXHI?t=30)：$f(x)\in F[x]$ **可分、不可約**，$E/F$ 是它的分裂體，根 $\alpha_1,\dots,\alpha_n\in E$。
- 【課堂討論】「為什麼 $E/F$ 是 Galois？」「記得：可分多項式的分裂體是 Galois。」
- $[E:F] = p$（這裡 $p$ 只是個名字）$= |\mathrm{Gal}(E/F)|$ ⇒ $\mathrm{Gal}(E/F) = \{1,\sigma_2,\dots,\sigma_p\}$。

---

## 1. 所有 Galois 共軛之積在基體裡

> **命題**（講義 p.1）[▶ 03:30](https://youtu.be/RrHAN9FtXHI?t=210)　$z\in E$ ⇒ $\prod_{i = 1}^p\sigma_i(z) = \sigma_1(z)\sigma_2(z)\cdots\sigma_p(z)\in F$。因此 $z\neq0$ 時
> $$z^{-1} = \frac{\prod_{i = 2}^p\sigma_i(z)}{\prod_{i = 1}^p\sigma_i(z)}.$$

「（好吧，被你們抓到——$\sigma_1 = 1$。）這可能是 D&F 的作業題，**肯定**是我弟弟建議的——就是上次那份 PDF 的**可怕計算**。但我想證它。」

**證明**[▶ 05:00](https://youtu.be/RrHAN9FtXHI?t=300)：任取 $\tau\in\mathrm{Gal}(E/F)$：
$$\tau\left(\prod_i\sigma_i(z)\right) = \prod_i(\tau\sigma_i)(z).$$
- $\mathrm{Gal}(E/F)$ 是群 ⇒ $\tau\sigma_1,\dots,\tau\sigma_p$ 就是 $\sigma_1,\dots,\sigma_p$ **重新排序** ⇒ 乘積（交換）不變。
- 所以乘積被**每個** $\tau$ 固定 ⇒ 在固定體裡 ⇒ 在 $F$（Galois：$F = E^{\mathrm{Gal}}$）。
- 第二部分：解 $\frac1z$——「**別告訴 Spano**」。$\blacksquare$

**例 1**（講義 p.1）[▶ 09:00](https://youtu.be/RrHAN9FtXHI?t=540)：$x^2+1\in\mathbb{R}[x]$ 在 $\mathbb{C}$ 分裂。
- 【課堂討論】「$[\mathbb{C}:\mathbb{R}]$？」「2。」⇒ $\mathrm{Gal} = \{1,\sigma\}$。「那個 $\mathbb{R}$-固定的自同構叫什麼？」「**複數共軛**。」
- 公式就變成熟悉的 $z^{-1} = \frac{\bar z}{z\bar z}$。「我們的**標準**複數倒數公式，就是這個 **Galois 倒數公式**的例子。」

---

## 2. Galois 群是 Sₙ 的子群

[▶ 11:00](https://youtu.be/RrHAN9FtXHI?t=660)（講義 p.2）$f$ 可分、$\deg f = n$。Galois 群**置換**根（之前證過，「很短的計算」）：$\sigma\in G$ 把 $\alpha_1,\dots,\alpha_n$ 送到 $\alpha_1,\dots,\alpha_n$。
- 把根**編號** 1 到 $n$ ⇒ **$G$ 可看成 $S_n$ 的子群**。
- ⇒
$$[E:F] = |\mathrm{Gal}(E/F)|\le|S_n| = n!.$$
  「所以 $n$ 次多項式**一定**能用至多 $n!$ 次的擴張分裂。當然有時更少就夠。」

💬 講義 p.2 把不等式寫成「$|\mathrm{Gal}(E/F)|\le n! = |S_n| = [E:F]$」——最後的等號放錯了位置，應是 $[E:F] = |\mathrm{Gal}(E/F)|\le n! = |S_n|$。（老師口頭：「我講義有個筆誤，幸好還沒掃描。」）

---

## 3. 例：V₄ ≤ S₄、有理化 1/(1+3√2+4√3)

**例 2**（講義 p.2）[▶ 14:30](https://youtu.be/RrHAN9FtXHI?t=870)：$f = (x^2-2)(x^2-3)$，$E = \mathbb{Q}(\sqrt2,\sqrt3)$。根 $\alpha_1 = \sqrt2$、$\alpha_2 = -\sqrt2$、$\alpha_3 = \sqrt3$、$\alpha_4 = -\sqrt3$。
- 【課堂討論】「$\sigma$ 把 $\alpha_1$ 送去哪？」學生：「不知道？」「我想是 $\alpha_2$。」
$$\sigma = (12),\qquad\tau = (34),\qquad\sigma\tau = (12)(34).$$
$$\mathrm{Gal}(E/\mathbb{Q})\cong\{1,(12),(34),(12)(34)\}\le S_4.$$
- 「Klein 四元群坐在**四個符號的對稱群**裡。同一個例子做夠多次，**總會開始有道理**——反正 D&F 也這樣。」

**好玩的**[▶ 17:30](https://youtu.be/RrHAN9FtXHI?t=1050)：三個非平凡自同構 $\sigma,\tau,\sigma\tau$ 給三個共軛 ⇒
$$\frac1{1+3\sqrt2+4\sqrt3} = \frac{(1-3\sqrt2+4\sqrt3)(1+3\sqrt2-4\sqrt3)(1-3\sqrt2-4\sqrt3)}{(1+3\sqrt2+4\sqrt3)(\cdots)(\cdots)(\cdots)} = \frac{-65-93\sqrt2+116\sqrt3+24\sqrt6}{769}.$$
- 【口頭】[▶ 20:00](https://youtu.be/RrHAN9FtXHI?t=1200)「如果你有**不守規矩的青少年**要打發時間——這是**很難**的數學題，但問題很**簡單**：『有理化這個』。任何高中生都懂你在問什麼。至於為什麼要這樣做，**只有我們知道**。」

💬 驗算分母：$(1+3\sqrt2+4\sqrt3)(1-3\sqrt2+4\sqrt3) = (1+4\sqrt3)^2-18 = 31+8\sqrt3$；另一對 $= 31-8\sqrt3$；相乘 $= 961-192 = 769$ ✓。

---

## 4. 例：x³ − 2 的 Galois 群正好是 S₃

**例 3**（講義 p.3）[▶ 21:00](https://youtu.be/RrHAN9FtXHI?t=1260)：$E = \mathbb{Q}(\sqrt[3]2,\rho)$ 分裂 $x^3-2$（Eisenstein $p = 2$ 不可約）。根 $\alpha_1 = \sqrt[3]2$、$\alpha_2 = \rho\sqrt[3]2$、$\alpha_3 = \rho^2\sqrt[3]2$。
$$\sigma = (123),\qquad\tau = (23).$$
- 【課堂討論】[▶ 22:30](https://youtu.be/RrHAN9FtXHI?t=1350)「$\alpha_2$ 和 $\alpha_3$ 怎麼關聯？那個翻轉是什麼？」「**複數共軛**——所以你們下學期要修**複分析**。」（學生：「我會跟你一起。」「我很想看我的複分析班有誰，但**軟體改進了**，在 Canvas 課程建立之前就**不可能**看名單了。」）
$$\mathrm{Gal}(E/\mathbb{Q})\cong\{1,\underbrace{(123)}_{\sigma},\underbrace{(132)}_{\sigma^2},\underbrace{(23)}_{\tau},\underbrace{(13)}_{\tau\sigma},\underbrace{(12)}_{\tau\sigma^2}\} = S_3.$$
- 「Galois 群是 $S_3$ 的子群，但這裡**就是** $S_3$。」【Q&A】學生：「$F$ 是有理數吧？」「對，我的錯。」

**典型情況**[▶ 25:00](https://youtu.be/RrHAN9FtXHI?t=1500)（講義 p.3）「接下來要想**一般**多項式。開學時我做過一點——用不定元當根。」
- 【口頭】「**例 3 才是典型**：一般的多項式，Galois 群就是**整個**對稱群。如果根之間有**特別的結構**，那多項式就很特別。例 2 的根是**互為負數**——非常特別，所以沒拿到 24 階的 $S_4$，只有 4 階。」

---

## 5. 基本對稱函數、一般多項式

> **定義**（講義 p.3）[▶ 27:00](https://youtu.be/RrHAN9FtXHI?t=1620)　$x_1,\dots,x_n$ 是**不定元**。**基本對稱函數**：
> $$s_1 = x_1+\cdots+x_n,\quad s_2 = x_1x_2+x_1x_3+\cdots+x_{n-1}x_n,\quad\dots,\quad s_n = x_1x_2\cdots x_n.$$
> $s_i$ 是**每次取 $i$ 個相異**不定元相乘、再把所有這種乘積加起來（不能重複——$s_2$ 裡不能有 $x_1^2$）。

【口頭】[▶ 30:00](https://youtu.be/RrHAN9FtXHI?t=1800)「不定元是什麼？它們**不定**——這很確定。它們**交換**：$x_1x_2 = x_2x_1$。用具體模型建構時要把交換性**建進去**。除此之外**沒有特徵**。不交換的不定元也能玩，但**有點可怕**。」

> **定義**（講義 p.4）[▶ 30:30](https://youtu.be/RrHAN9FtXHI?t=1830)　**$n$ 次一般多項式**：$(x-x_1)(x-x_2)\cdots(x-x_n)$，根就是不定元 $x_1,\dots,x_n$。

> **宣稱**（講義 p.4）[▶ 31:30](https://youtu.be/RrHAN9FtXHI?t=1890)　一般多項式的係數是 $\pm$ 基本對稱函數：
> $$(x-x_1)\cdots(x-x_n) = x^n-s_1x^{n-1}+s_2x^{n-2}-\cdots+(-1)^ns_n.$$

**證明**：歸納，「但別擔心，**我不做**。看幾個小情形，你就會懂歸納為什麼會**好玩**。」
- $n = 2$：$x^2-(x_1+x_2)x+x_1x_2 = x^2-s_1x+s_2$。
- $n = 3$[▶ 33:30](https://youtu.be/RrHAN9FtXHI?t=2010)：再乘 $(x-x_3)$，「**歪頭瞇眼**」：
$$x^3-(x_1+x_2+x_3)x^2+(x_1x_2+x_1x_3+x_2x_3)x-x_1x_2x_3 = x^3-s_1x^2+s_2x-s_3.$$
- 「你們至少一個人是**工程雙主修**——我做到 3 了，那構成**工程證明**，對吧？」
- 【口頭】[▶ 35:30](https://youtu.be/RrHAN9FtXHI?t=2130)「這會是**好玩的作業**。以前教這個時我**很困惑**，因為沒意識到**基本對稱函數依賴 $n$**：$n = 2$ 的 $s_1$ 和 $n = 3$ 的 $s_1$ 是**不同**的東西。證明大半在處理記號——D&F **聰明地省略**了，跟我一樣。」學生：「**加分**？」「你們**之前的支線任務都還沒做完**。」

---

## 6. 一般多項式的 Galois 群是 Sₙ

[▶ 38:00](https://youtu.be/RrHAN9FtXHI?t=2280)（以下依 D&F §14.6）
- $E = F(x_1,\dots,x_n)$ 是 $(x-x_1)\cdots(x-x_n)$ 在 $F(s_1,\dots,s_n)$ 上的**分裂體** ⇒ **Galois**。
- 【課堂討論】[▶ 39:30](https://youtu.be/RrHAN9FtXHI?t=2370)「$F(s_1,\dots,s_n)\subseteq E$ 清楚嗎？」「$s_i$ 只是不定元的和與積，所以清楚。」「它**不必**是同一個體：$s_i$ 只以**特定模式**帶進不定元，不保證能從這些模式拿回所有其他模式。」
- **$S_n$ 作用**[▶ 41:00](https://youtu.be/RrHAN9FtXHI?t=2460)：$\sigma\in S_n$ 誘導 $x_i\mapsto x_{\sigma(i)}$——「跟例 2、例 3 **同一個蠢對應**，這就是做那些例子的目的」——是 $E$ 的自同構 ⇒ $S_n\le\mathrm{Aut}(E)$。
- $s_i$ 在任何下標置換下**不變** ⇒ $F(s_1,\dots,s_n)\subseteq E^{S_n}$。
- 次數：$[E:E^{S_n}] = |S_n| = n!$（Thm 9）；而 $E$ 是 $n$ 次多項式在 $F(s_1,\dots,s_n)$ 上的分裂體 ⇒ $[E:F(s_1,\dots,s_n)]\le n!$（學生 Shane 提醒）。⇒ **相等**：
$$F(s_1,\dots,s_n) = E^{S_n}.$$
  （[▶ 45:00](https://youtu.be/RrHAN9FtXHI?t=2700)「抱歉，**這個時段**我的腦袋……」「**8:15** 會更糟。」「你們修過我的 8:15，**抱怨了很多**。等等，那是**每堂課**都這樣。」）

> **命題 30**[▶ 47:00](https://youtu.be/RrHAN9FtXHI?t=2820)　$S_n$ 作用在有理函數體 $F(x_1,\dots,x_n)$ 上的固定體是 $F(s_1,\dots,s_n)$。

> **定義**[▶ 48:00](https://youtu.be/RrHAN9FtXHI?t=2880)　有理函數 $f(x_1,\dots,x_n)$ 叫**對稱**，若 $f(x_{\sigma(1)},\dots,x_{\sigma(n)}) = f(x_1,\dots,x_n)$ 對所有 $\sigma\in S_n$。

（【課堂討論】「對稱是什麼意思？」學生：「$f(-x_1,\dots)$？」「不，不是**反對稱**。」「是可以**任意調換**引數的順序。」）

> **推論 31**[▶ 49:30](https://youtu.be/RrHAN9FtXHI?t=2970)　任何**對稱有理函數**都是 $s_1,\dots,s_n$ 的有理函數。

- 證明：對稱函數在 $S_n$ 的固定體裡，由命題 30。
- 【口頭】[▶ 50:30](https://youtu.be/RrHAN9FtXHI?t=3030)「這一定是在**有理函數**的脈絡下。我**一秒都不信**它對一般函數成立：例如 $\sin(x_1+\cdots+x_n)$，我不認為是基本對稱函數的有理函數。」

**例**[▶ 51:30](https://youtu.be/RrHAN9FtXHI?t=3090)
- $(x_1-x_2)^2 = (x_1+x_2)^2-4x_1x_2 = s_1^2-4s_2$。「我一開始直接展開——**選得很差**。讓 $s_1$ 出現才是好招。」
- $x_1^2+x_2^2+x_3^2 = (x_1+x_2+x_3)^2-2(x_1x_2+x_1x_3+x_2x_3) = s_1^2-2s_2$。「**挺妙的**。」

💬 [▶ 51:30](https://youtu.be/RrHAN9FtXHI?t=3090) 老師一開始說「$x_1-x_2$ 是對稱的」——要**平方**後 $(x_1-x_2)^2$ 才對稱（交換 $x_1,x_2$ 會讓 $x_1-x_2$ 變號）。

> **定理 32**[▶ 54:30](https://youtu.be/RrHAN9FtXHI?t=3270)　一般多項式
> $$x^n-s_1x^{n-1}+\cdots+(-1)^ns_n$$
> 在 $F(s_1,\dots,s_n)$ 上**可分**，Galois 群是 **$S_n$**。

【口頭】[▶ 55:00](https://youtu.be/RrHAN9FtXHI?t=3300)「如果係數之間**沒有關係**（$s_i$ 是不定元的意思），Galois 群就是**完整的對稱群**。所以例 3 是**典型**。（書上有一段我跳過了，但我們很接近了。）」

**預告**[▶ 56:00](https://youtu.be/RrHAN9FtXHI?t=3360)「下次回到**當初激發這整套研究**的問題：**解五次方程**——找像**二次公式**那樣的高次公式，只用係數的加減乘除和開根號。要看**根式擴張**，會連到之前**可解群**的定義，看出為什麼**五次以上一般不可能**。那是**最後一堂** Galois 理論。」學生：「希望會有 **Mission**。」「啊哈，Mission。」

---

## 7. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $\prod_\sigma\sigma(z)\in F$；$z^{-1} = \prod_{\sigma\neq1}\sigma(z)/\prod_\sigma\sigma(z)$ | $\tau\sigma_i$ 只是重新排序 |
| $\mathbb{C}/\mathbb{R}$：$z^{-1} = \bar z/(z\bar z)$ | Galois 群 $\{1,\text{共軛}\}$ |
| $\mathrm{Gal}\le S_n$；$[E:F]\le n!$ | 自同構置換根 |
| $(x^2-2)(x^2-3)$：$\{1,(12),(34),(12)(34)\}$ | |
| $\frac1{1+3\sqrt2+4\sqrt3} = \frac{-65-93\sqrt2+116\sqrt3+24\sqrt6}{769}$ | 乘三個共軛 |
| $x^3-2$：$\sigma = (123)$、$\tau = (23)$ ⇒ $S_3$ | $\tau$ 是複數共軛 |
| $(x-x_1)\cdots(x-x_n) = x^n-s_1x^{n-1}+\cdots+(-1)^ns_n$ | 歸納 |
| $F(x_1..x_n)^{S_n} = F(s_1..s_n)$ | $n!$ 兩邊夾 |
| 對稱有理函數 = $s_i$ 的有理函數 | $(x_1-x_2)^2 = s_1^2-4s_2$ |
| **一般 $n$ 次多項式的 Galois 群是 $S_n$** | Thm 32 |

| 中文 | English |
|---|---|
| 不定元 | indeterminate |
| 基本對稱函數 | elementary symmetric functions |
| 一般多項式 | general polynomial |
| 對稱（有理）函數 | symmetric (rational) function |
| 有理函數體 | field of rational functions |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **根式擴張、可解群、五次方程** | [[29-L25-Galois理論結語]] |
| **基本對稱函數（開學時的 Cardano）** | [[01-L1-群論起源與等距變換]] |

---

## 附：本集一句話總結

> **Galois 擴張中一個元素所有共軛之積被每個自同構固定，所以落在基體裡——這給出 $z^{-1} = (\text{其餘共軛之積})/(\text{範數})$，$\mathbb{C}$ 的 $\bar z/(z\bar z)$ 只是特例，也能有理化 $\frac1{1+3\sqrt2+4\sqrt3}$；Galois 群置換根，所以是 $S_n$ 的子群（$(x^2-2)(x^2-3)$ 得到 $V_4\le S_4$，$x^3-2$ 正好是 $S_3$）；用不定元當根的一般多項式係數就是 $\pm$ 基本對稱函數，$S_n$ 的固定體正是 $F(s_1,\dots,s_n)$，因此對稱有理函數都能寫成基本對稱函數的有理函數，而一般 $n$ 次多項式的 Galois 群是整個 $S_n$。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 24 錄影逐字稿（YouTube 自動字幕，57:12）與手寫講義 `Math422_Lecture24_GaloisGroupPolynomials.pdf`（後半依 Dummit & Foote §14.6）整理。*
