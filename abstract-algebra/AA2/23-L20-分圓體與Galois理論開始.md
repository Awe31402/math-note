---
course: Abstract Algebra II (Spring 2026)
episode: 23
lecture: L20
date: 2026-03-09
video: https://www.youtube.com/watch?v=Ye9Sf63TTmc
notes: 講義/AA2/Math422_Lecture20_CyclotomicExtensions.pdf
---

# 第 23 集 · L20：分圓體、Galois 理論開始 [▶ 影片](https://www.youtube.com/watch?v=Ye9Sf63TTmc&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[22-L19-可分擴張]] ｜ [總目錄](../README.md) ｜ 下一集：[[24-L21-Galois擴張與Galois群]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 23 集，Lecture 20
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ 手寫講義 `Math422_Lecture20_CyclotomicExtensions.pdf`（10 頁），依 Dummit & Foote §13.6。前半黑板，後半投影。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【講義補充】` 講義有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：最後幾分鐘才開始 Lecture 21（Galois 理論），主要內容在 [[24-L21-Galois擴張與Galois群]]。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. xⁿ − 1 的根：n 次單位根](#1-xⁿ--1-的根n-次單位根)
- [2. 分圓體；μₙ 是群](#2-分圓體μₙ-是群)
- [3. 小的 ζₙ；目標 [ℚ(ζₙ):ℚ] = φ(n)](#3-小的-ζₙ目標-ℚζₙℚ--φn)
- [4. 分圓多項式 Φₙ](#4-分圓多項式-φₙ)
- [5. xⁿ − 1 = ∏_{d|n} Φ_d；n = Σ φ(d)](#5-xⁿ--1--_dn-φ_dn--σ-φd)
- [6. Φₙ 整係數且不可約](#6-φₙ-整係數且不可約)
- [7. xᵖ − 2 的分裂體](#7-xᵖ--2-的分裂體)
- [8. Galois](#8-galois)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/Ye9Sf63TTmc?t=0)（老師擦掉黑板上**三角學的殘渣**。）課前禱告：「幫助我們多懂一點**分圓體**。」

---

## 1. xⁿ − 1 的根：n 次單位根

[▶ 01:00](https://youtu.be/Ye9Sf63TTmc?t=60)「直接**正面攻擊**：我們想懂怎麼分解 $x^n-1$。」（講義 p.1）
- 用**虛指數**：$(e^{i\theta})^j = e^{ij\theta}$；$e^{i\theta} = 1\iff\cos\theta = 1,\sin\theta = 0\iff\theta\in2\pi\mathbb{Z}$。
$$(e^{i\theta})^n-1 = 0\iff e^{in\theta} = 1\iff n\theta = 2\pi k\iff\theta = \frac{2\pi k}n\ (k\in\mathbb{Z}).$$
- ⇒ $f(\zeta_n^k) = 0$，其中 $\zeta_n = e^{2\pi i/n} = \cos\frac{2\pi}n+i\sin\frac{2\pi}n$，**主 $n$ 次單位根**。
- $\deg(x^n-1) = n$ ⇒ 至多 $n$ 個相異根。【課堂討論】[▶ 04:30](https://youtu.be/Ye9Sf63TTmc?t=270)「有什麼能保證**沒有重根**？」「看**導數**。」（學生：「$nx^{n-1}$——今天早上這很難。」）$f' = nx^{n-1} = 0\iff x = 0$（特徵 0——「我們把 $x^n-1$ 看成**有理**多項式，不會有有限特徵的把戲」），而 $f(0) = -1\neq0$ ⇒ **沒有重根**。
- 所以
$$1^{1/n} = \{1,\zeta_n,\zeta_n^2,\dots,\zeta_n^{n-1}\}$$
  是 $n$ 個**相異**的 **$n$ 次單位根**（複分析的記號 $1^{1/n}$；D&F 寫 $\mu_n$）。它們的**生成元**叫**本原 $n$ 次單位根**。
$$x^n-1 = (x-1)(x-\zeta_n)(x-\zeta_n^2)\cdots(x-\zeta_n^{n-1}).$$

---

## 2. 分圓體；μₙ 是群

> **定義**（講義 p.2）[▶ 08:30](https://youtu.be/Ye9Sf63TTmc?t=510)　$\mathbb{Q}(\zeta_n)$ 是 $x^n-1$ 的分裂體，叫 **$n$ 次單位根的分圓體**（cyclotomic field）。

（學生：「C-Y-C-L-O……請**在不同時間**拼它。」）

- 【課堂討論】[▶ 09:00](https://youtu.be/Ye9Sf63TTmc?t=540)「為什麼只要加 $\zeta_n$ 就夠？」學生：「**乘法**。」「對，體對乘法封閉，有它就有它的平方、立方……自動生成其餘的。」

**$\mu_n$ 是群**[▶ 09:30](https://youtu.be/Ye9Sf63TTmc?t=570)：
- $\alpha^n = \beta^n = 1$ ⇒ $(\alpha\beta)^n = \alpha^n\beta^n = 1$。
- **反元素**：$\alpha^{n-1}\alpha = \alpha^n = 1$ ⇒ $\alpha^{-1} = \alpha^{n-1}$，而 $(\alpha^{n-1})^n = (\alpha^n)^{n-1} = 1$。（老師繞了一圈；學生提示「用指數律」：「喔，我早該這樣做。**廢話**。」）⇒ 子群判別法。

【講義補充】講義 p.2：該把分裂體想成**抽象**的 $K/\mathbb{Q}$——$\{\alpha\in K^\times : \alpha^n = 1\}$ 構成 $K^\times$ 的子群。「有時讓這種抽象很有用：例子可能**不住在 $\mathbb{C}$ 裡**，卻有像 $\mathbb{Q}(\zeta_n)$ 的分裂體。」

---

## 3. 小的 ζₙ；目標 [ℚ(ζₙ):ℚ] = φ(n)

[▶ 14:30](https://youtu.be/Ye9Sf63TTmc?t=870)（講義 p.2）
$$\zeta_1 = 1,\ \zeta_2 = -1,\ \zeta_3 = \frac{-1+i\sqrt3}2,\ \zeta_4 = i,\ \zeta_5 = \frac{\sqrt5-1}4+i\frac{\sqrt{10+2\sqrt5}}4,\ \zeta_6 = \frac{1+i\sqrt3}2,\ \zeta_8 = \frac{\sqrt2+i\sqrt2}2.$$
「$\zeta_5$ **別叫我推導**。」（學生：「你的 5 看起來像 S。」「7 怎麼了？」「他**不想要 67**。」）

> **目標**（講義 p.2）[▶ 16:30](https://youtu.be/Ye9Sf63TTmc?t=990)　解釋為什麼 $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$（Euler $\varphi$ 函數）。特別地，$\Phi_n(x) = m_{\zeta_n,\mathbb{Q}}(x)$ 是第 $n$ 個**分圓多項式**。

- $n = 1,2$ **特別蠢**：加 1 或 $-1$ 還是 $\mathbb{Q}$。從 $\zeta_3,\zeta_4,\zeta_5$ 才有趣。

**$n = p$ 質數**[▶ 18:00](https://youtu.be/Ye9Sf63TTmc?t=1080)（講義 p.3）：
$$x^p-1 = (x-1)(x^{p-1}+x^{p-2}+\cdots+x+1),$$
後者我們證過**不可約**（[[17-L14-約化法與Eisenstein判別法]]，平移 + Eisenstein）⇒ 是 $\zeta_p$ 的最小多項式 ⇒ $[\mathbb{Q}(\zeta_p):\mathbb{Q}] = p-1 = \varphi(p)$。
- 「所以我沒寫 $\zeta_7$——它的公式基於一個**六次**多項式，會很難看。$\zeta_5$ 已經難看了：$\varphi(5) = 4$，是 $\mathbb{Q}$ 上 4 次的元素。」
- 「$n$ 是質數就**做完了**。問題是 $n$ **合數**時。」

---

## 4. 分圓多項式 Φₙ

[▶ 21:00](https://youtu.be/Ye9Sf63TTmc?t=1260)（改投影：「我在 D&F 上**加了細節**——花了我好幾個小時把這些分解**明確**寫出來。希望你們欣賞。」）

> **定義**（講義 p.3）　第 $n$ 個**分圓多項式** $\Phi_n(x)$：根恰好是**本原** $n$ 次單位根的多項式。

【口頭】[▶ 24:30](https://youtu.be/Ye9Sf63TTmc?t=1470)「注意 **$\Phi_n$ 不再只是** $x^{n-1}+\cdots+x+1$。你得把這**塞進腦袋**——我以前某一年**沒塞進去**，搞得很混亂。顯然是**閱讀理解**問題。我們就明確地看，看到**無聊**到不得不懂為止。」

**小的 $n$**（講義 p.3–4）
| $n$ | $x^n-1$ 的分解 | $\Phi_n$ |
|---|---|---|
| 1 | $x-1$ | $x-1$ |
| 2 | $(x-1)(x+1)$ | $x+1$（根 $-1$，唯一的本原 2 次根） |
| 3 | $(x-1)(x^2+x+1)$ | $x^2+x+1$（根 $\zeta_3,\zeta_3^2$——「Cardano 時叫 $\omega,\omega^2$」） |
| 4 | $(x-1)(x+1)(x^2+1)$ | $x^2+1$（根 $\pm i$） |
| 5 | $(x-1)(x^4+x^3+x^2+x+1)$ | $x^4+x^3+x^2+x+1$ |
| 6 | $(x-1)(x^2+x+1)(x+1)(x^2-x+1)$ | $x^2-x+1$ |
| 8 | $(x-1)(x+1)(x^2+1)(x^4+1)$ | $x^4+1$（根 $\zeta_8,\zeta_8^3,\zeta_8^5,\zeta_8^7$） |
| 12 | $(x^3-1)(x^3+1)(x^2+1)(x^4-x^2+1)$ | $x^4-x^2+1$ |

- $n = 2$：「1 和 2 是 2 的因數。**說說而已**。」學生：「哇。」「那是一聲 wow，不是 meow。……是很**嗆**的 wow。」
- $n = 4$[▶ 27:30](https://youtu.be/Ye9Sf63TTmc?t=1650)：「本原 4 次根只有 $i$ 和 $-i$。$i^3 = -i$——**不是巧合**：4 的單位群是 $\{1,3\}$，所以取三次方還是本原的，不是二次方。」
- $n = 6$：$x^3+1$ 有根 $-1$，所以有因子 $x+1$。
- $n = 12$[▶ 31:00](https://youtu.be/Ye9Sf63TTmc?t=1860)：$\gcd(k,12) = 1$ 的 $k = 1,5,7,11$ ⇒ 4 個本原 12 次根 ⇒ $\Phi_{12}$ 是 4 次。「**我回到定義**——你把這放進菸斗抽吧。」（「抱歉，我該停止開**代數毒蟲**的玩笑。這種毒蟲在你們出生**之前**。」）配成**互為負**的一對，乘起來是 1、相加是餘弦：
$$\Phi_{12} = (x^2-2\cos\tfrac\pi6x+1)(x^2-2\cos\tfrac{5\pi}6x+1) = (x^2-\sqrt3x+1)(x^2+\sqrt3x+1) = x^4-x^2+1.$$

---

## 5. xⁿ − 1 = ∏_{d|n} Φ_d；n = Σ φ(d)

[▶ 33:30](https://youtu.be/Ye9Sf63TTmc?t=2010)「你們該開始看出**模式**。」

**另一個算法**（講義 p.5）：
$$\Phi_n(x) = \frac{x^n-1}{\prod_{d\mid n,\,d<n}\Phi_d(x)}.$$
「你永遠不會走到不知道前面分圓多項式的地方——只要你**列清單、檢查兩遍**。（不知為何我想這樣說。）」
- 對 $n = 12$ 試：消掉 $x-1$ 後還要乘 $\Phi_2\Phi_3\Phi_4\Phi_6$——「乘出來有 **20 項**要加……我看你們已經**放棄**了。很好。」再長除 ⇒ $x^4-x^2+1$。「我**用 Wolfram Alpha 驗過**那個除法。」「**我不喜歡**這方法。」

【Q&A】[▶ 36:00](https://youtu.be/Ye9Sf63TTmc?t=2160) 學生（Shane）：「你寫 $n = d_1d_2\cdots d_k$，但 $n = 4$ 時 $\Phi_1\Phi_2\Phi_4$，而 $1\cdot2\neq4$。」老師：「喔不……**你說得對**，沒那麼簡單。**結論還是對的**，只是不能說 $n$ 等於因數的乘積——要說『乘積跑遍 $n$ 的**所有相異正因數**』。$n = 12$ 時那乘積是 $1\cdot2\cdot3\cdot4\cdot6\cdot12$，本來就不等於 12。那只是我寫那段時**小例子的假象**。貼出前我得修。**很好**，Shane。」

**理論**（講義 p.6）[▶ 38:30](https://youtu.be/Ye9Sf63TTmc?t=2310)
- **$d\mid n$ ⇒ $\mu_d\subseteq\mu_n$**：$n = md$，$\alpha^d = 1$ ⇒ $\alpha^n = (\alpha^d)^m = 1$。
- $\alpha\in\mu_n$ 的階整除 $n$；階是 $d$ ⇒ $\alpha\in\mu_d$ 且是本原 $d$ 次根。「12 次單位根裡有 2 次、3 次、4 次單位根的子群。」
- 把 $\mu_n$ 的元素**按階分組**：
$$x^n-1 = \prod_{\zeta^n = 1}(x-\zeta) = \prod_{d\mid n}\ \prod_{\substack{\zeta\in\mu_d\\ \text{本原}}}(x-\zeta) = \prod_{d\mid n}\Phi_d(x).$$
- 比較次數（$\deg\Phi_d = \varphi(d)$）[▶ 42:00](https://youtu.be/Ye9Sf63TTmc?t=2520)：
$$n = \sum_{d\mid n}\varphi(d).$$
  驗 $n = 12$：$\varphi(1)+\varphi(2)+\varphi(3)+\varphi(4)+\varphi(6)+\varphi(12) = 1+1+2+2+2+4 = 12$ ✓。「你們大概以前學過。」

---

## 6. Φₙ 整係數且不可約

> **引理 40**（講義 p.7）[▶ 43:00](https://youtu.be/Ye9Sf63TTmc?t=2580)　$\Phi_n(x)$ 是 $\mathbb{Z}[x]$ 中首一、$\varphi(n)$ 次的多項式。

> **定理 41**（講義 p.7）　$\Phi_n(x)$ 在 $\mathbb{Z}[x]$（因此 $\mathbb{Q}[x]$）中**不可約**。

> **推論 42**（講義 p.8）　$[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$。

- 【口頭】「我已經對到 12 為止的**很多情形**證過了，不客氣。真正的證明在我看來**很噁**——是我沒深入的不可約部分。不難，只是**我沒興趣**，寧可把時間花在例子上。」
- 「定理 41 的證明用到 **Frobenius 自同態**，是 D&F 我還沒深入的部分。**你們可以假設** $\Phi_n$ 不可約——除非題目就是要證它，那我要的是針對那個例子的獨立論證。」

【講義補充】證明概要（講義 p.7–8）：
- **引理 40**：對 $n$ 歸納。$x^n-1 = f(x)\Phi_n(x)$，$f = \prod_{d\mid n,d<n}\Phi_d\in\mathbb{Z}[x]$ 首一；$f\mid x^n-1$ 在 $\mathbb{Q}[x]$ ⇒（§9.2 Gauss 引理）在 $\mathbb{Z}[x]$ ⇒ $\Phi_n\in\mathbb{Z}[x]$。
- **定理 41**：$\Phi_n = fg$，$f$ 是含某本原根 $\zeta$ 的不可約因子（$\zeta$ 的最小多項式）。取 $p\nmid n$：$\zeta^p$ 也是本原根，是 $f$ 或 $g$ 的根。若 $g(\zeta^p) = 0$，則 $f(x)\mid g(x^p)$；模 $p$ 用 Frobenius：$\bar g(x^p) = \bar g(x)^p$ ⇒ $\bar f,\bar g$ 有公因子 ⇒ $\bar\Phi_n$ 有重根 ⇒ $x^n-1$ 在 $\mathbb{F}_p$ 上有重根，但 $p\nmid n$ 時它可分，矛盾。所以 $\zeta^p$ 是 $f$ 的根；對 $a = p_1p_2\cdots$（$\gcd(a,n) = 1$）重複 ⇒ 所有本原根都是 $f$ 的根 ⇒ $f = \Phi_n$。
- **推論 42**：$\Phi_n$ 是 $\zeta_n$ 的最小多項式，$\mathbb{Q}[x]/(\Phi_n)\cong\mathbb{Q}(\zeta_n)$。

💬 老師口頭說引理 40 是「首一、在 $\mathbb{Z}_n[x]$」——是 **$\mathbb{Z}[x]$**。

**例**[▶ 44:30](https://youtu.be/Ye9Sf63TTmc?t=2670)
- **E2**（講義 p.8）：$[\mathbb{Q}(\zeta_8):\mathbb{Q}] = \varphi(8) = 4$。$\zeta_8+\zeta_8^7 = \sqrt2$ ⇒ $\sqrt2\in\mathbb{Q}(\zeta_8)$；再除以 $\sqrt2$ 可看出 $i$ 在裡面 ⇒ $\mathbb{Q}(\zeta_8) = \mathbb{Q}(i,\sqrt2)$。「$i$ 在裡面**不是一眼看出**——也許平方再相減之類，可以用有理式把 $i$ 單獨拿出來。」
- **E3**：$\mathbb{Q}(\zeta_2) = \mathbb{Q}(-1) = \mathbb{Q}$——蠢例子。
- **E4**[▶ 46:30](https://youtu.be/Ye9Sf63TTmc?t=2790)：$2\zeta_3+1 = i\sqrt3$ ⇒ $\mathbb{Q}(i\sqrt3)\subseteq\mathbb{Q}(\zeta_3)$。兩者都是 2 次 ⇒ 相等。「子空間的維度等於整個空間 ⇒ **就是**整個空間。不知道哪個是**雞**哪個是**蛋**。」

---

## 7. xᵖ − 2 的分裂體

[▶ 47:30](https://youtu.be/Ye9Sf63TTmc?t=2850)（講義 p.9–10）「回到上次簡短介紹的——現在**東西都在眼前**了。」$f = x^p-2$，$p$ 質數。
1. $\alpha^p = 2$；$\zeta\in\mu_p$ ⇒ $(\alpha\zeta)^p = 2\cdot1 = 2$ ⇒ $\alpha\zeta$ 也是根。
2. 根：$\sqrt[p]2,\zeta_p\sqrt[p]2,\dots,\zeta_p^{p-1}\sqrt[p]2$——「數一數，$p$ 個」，完整解集。
3. 分裂體 $= \mathbb{Q}(\sqrt[p]2,\zeta_p)$——「有這兩個就能造出其他所有的」。
4. $[\mathbb{Q}(\sqrt[p]2,\zeta_p):\mathbb{Q}]\le[\mathbb{Q}(\sqrt[p]2):\mathbb{Q}][\mathbb{Q}(\zeta_p):\mathbb{Q}] = p(p-1)$。
   - 【口頭】「一般：4 次和 8 次的元素加在一起，**可能**到 32 次，但不一定。」
5. $\gcd(p,p-1) = 1$，兩個子體的次數都整除總次數 ⇒ **$= p(p-1)$**。

**體塔圖**（講義 p.10）[▶ 50:30](https://youtu.be/Ye9Sf63TTmc?t=3030)（「那個角**好邪惡**。」）
$$\begin{matrix}&\mathbb{Q}(\sqrt[p]2,\zeta_p)&\\ {\scriptstyle p}\diagup&&\diagdown{\scriptstyle p-1}\\ \mathbb{Q}(\zeta_p)&&\mathbb{Q}(\sqrt[p]2)\\ {\scriptstyle p-1}\diagdown&&\diagup{\scriptstyle p}\\ &\mathbb{Q}&\end{matrix}$$

💬 老師口誤說「$\mathbb{Q}(\sqrt[p]2)$ 是 $\mathbb{Q}$ 上 2 次擴張」——是 **$p$ 次**（最小多項式 $x^p-2$）。

**推論**[▶ 51:30](https://youtu.be/Ye9Sf63TTmc?t=3090)
- $x^p-2$ 在 $\mathbb{Q}(\zeta_p)[x]$ **仍不可約**；$\Phi_p$ 在 $\mathbb{Q}(\sqrt[p]2)[x]$ **仍不可約**。
- 【口頭】「擴大係數體時，不可約性**有危險**：$x^2+1$ 在 $\mathbb{R}$ 上不可約，擴到 $\mathbb{C}$——**哎呀**，變成 $(x+i)(x-i)$。但這裡沒事，因為這兩個體在某種意義下**獨立**：擴張不會打亂定義用的最小多項式的不可約性。直接證這兩件事會**很煩**，但從體論**免費**得到。」

---

## 8. Galois

[▶ 53:30](https://youtu.be/Ye9Sf63TTmc?t=3210)「這把我們帶到 **Galois 理論**。準備好了嗎？」學生：「沒有。」「還有四分鐘。」「我們**終於**到 Lecture 20 了——Lecture 20 剩下**負的**時間。」

- **Évariste Galois**（1811–1832）。學生：「我 21 歲。」「我知道，**別去想**，很令人沮喪。另一方面，如果你活到 22，你就**比他好**了。」學生：「謝謝。」
- [▶ 55:30](https://youtu.be/Ye9Sf63TTmc?t=3330) 體到自己的同構叫**自同構**（automorphism）。「主要差別：我們不寫 $\sigma(\alpha)$，**只寫 $\sigma\alpha$**。」
- 【Q&A】[▶ 55:30](https://youtu.be/Ye9Sf63TTmc?t=3330) 學生：「他怎麼死的？」「**決鬥**。」「真的？」「真的。不確定為什麼——大概是**政治或女人**。」學生：「希望是女人。」「好吧，那我們今天大概不會走太遠。」
- [▶ 56:30](https://youtu.be/Ye9Sf63TTmc?t=3390)（課堂最後在學生要求下播放一段關於 Galois 生平的歌曲影片：父親在他考試前一週自殺、考試失利、政治激進、為一個女孩決鬥而死。）

→ Galois 群的正式內容見 [[24-L21-Galois擴張與Galois群]]。

---

## 9. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $x^n-1$ 有 $n$ 個相異根 $\zeta_n^k$ | $f' = nx^{n-1}$ 只在 0 為零，$f(0) = -1$ |
| $\mathbb{Q}(\zeta_n)$ 是 $x^n-1$ 的分裂體 | 其他根是 $\zeta_n$ 的冪 |
| $\mu_n$ 是群；$d\mid n$ ⇒ $\mu_d\le\mu_n$ | $\alpha^{-1} = \alpha^{n-1}$ |
| $x^n-1 = \prod_{d\mid n}\Phi_d(x)$ | 按階分組 |
| $n = \sum_{d\mid n}\varphi(d)$ | 比較次數 |
| $\Phi_n\in\mathbb{Z}[x]$ 首一、不可約、$\varphi(n)$ 次 | Gauss 引理；Frobenius |
| $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$ | $\Phi_n$ 是最小多項式 |
| $\mathbb{Q}(\zeta_8) = \mathbb{Q}(i,\sqrt2)$；$\mathbb{Q}(\zeta_3) = \mathbb{Q}(i\sqrt3)$ | $\zeta_8+\zeta_8^7 = \sqrt2$；$2\zeta_3+1 = i\sqrt3$ |
| $x^p-2$ 的分裂體 $p(p-1)$ 次 | $\gcd(p,p-1) = 1$ |

**小分圓多項式**：$\Phi_1 = x-1$、$\Phi_2 = x+1$、$\Phi_3 = x^2+x+1$、$\Phi_4 = x^2+1$、$\Phi_6 = x^2-x+1$、$\Phi_8 = x^4+1$、$\Phi_{12} = x^4-x^2+1$。

| 中文 | English |
|---|---|
| $n$ 次單位根 | $n$-th roots of unity $\mu_n$ |
| 本原單位根 | primitive root of unity |
| 分圓體 | cyclotomic field |
| 分圓多項式 | cyclotomic polynomial $\Phi_n$ |
| Euler $\varphi$ 函數 | Euler's totient function |
| 自同構 | automorphism |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **自同構、Galois 群** | [[24-L21-Galois擴張與Galois群]] |
| **$x^p-2$、$\mathbb{Q}(\zeta_8)$ 的子體格** | [[25-L22-Galois理論基本定理]]、[[27-L23-Galois理論例子-上]] |
| **$\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})\cong(\mathbb{Z}/n)^\times$** | [[29-L25-Galois理論結語]] |

---

## 附：本集一句話總結

> **$x^n-1$ 的根是 $n$ 個相異的 $n$ 次單位根 $\zeta_n^k$（導數判別法保證沒有重根），$\mathbb{Q}(\zeta_n)$ 就是它的分裂體——分圓體；把單位根按階分組得到 $x^n-1 = \prod_{d\mid n}\Phi_d(x)$，其中分圓多項式 $\Phi_n$ 的根是本原 $n$ 次單位根、整係數且不可約，所以 $[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$、$n = \sum_{d\mid n}\varphi(d)$；$x^p-2$ 的分裂體 $\mathbb{Q}(\sqrt[p]2,\zeta_p)$ 是 $p(p-1)$ 次；最後幾分鐘，Galois 理論登場。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 20 錄影逐字稿（YouTube 自動字幕，59:51）與手寫講義 `Math422_Lecture20_CyclotomicExtensions.pdf`（依 Dummit & Foote §13.6）整理。*
