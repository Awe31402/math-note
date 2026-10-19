---
course: Abstract Algebra II (Spring 2026)
episode: 44
lecture: 複習（Boss Fight 3）
date: 2026-05-04
video: https://www.youtube.com/watch?v=wC7fzfnn89M
notes: 無直接對應（最後一份作業解答）
---

# 第 44 集 · 複習：Boss Fight 3 考前問答 [▶ 影片](https://www.youtube.com/watch?v=wC7fzfnn89M&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[43-複習-BossFight3-下]] ｜ [總目錄](../README.md) ｜ 下一集：無（課程結束）

## 本集概要

學期最後一堂，第三次考試（Boss Fight 3）前的複習：
- 考試範圍清單：張量積、直和、$R$-模、撓、零化子、Thm 5 vs. Thm 6、Smith 標準形、$T$-循環基底、有理標準形 vs. Jordan 形、子模判別法、整環上模的線性獨立與生成。
- 交換群的不變因子 vs. 初等因子例子（$\mathbb{Z}_{100}$；$\mathbb{Z}_2\oplus\mathbb{Z}_{20}\oplus\mathbb{Z}_{200}$）。
- 投影作業解答：子模、撓、核與像、$\mathrm{Hom}_R(R,M)\cong M$、商的直積、有限交換群是撓 $\mathbb{Z}$-模、$\mathrm{Hom}(F,R)\cong F$、中心冪等元分解、$\mathbb{C}\otimes\mathbb{C}$、非簡單張量、$S\otimes_RR[x]\cong S[x]$、反對稱雙線性形式與 $\bigwedge^2$、有理標準形與 Jordan 形的大量情況、$A\sim A^T$、$A^2 = I$ 可對角化、純量擴張的矩陣、$\mathcal{A}$-數的單位與零因子。

> 📘 講義對應：無；最後一份作業（Mission）解答。

---

## 筆記

### 1. 考試範圍 [▶ 00:30](https://youtu.be/wC7fzfnn89M?t=30)

- 張量積；直和；$R$-模；**撓**；**零化子**；§12.1 **Thm 5（不變因子）vs. Thm 6（初等因子）**。
- 會算 **Smith 標準形**：$F^{n\times n}$ 的矩陣，或 $\mathbb{Z}$-模的**關係矩陣**——並會解讀（它給出 $A$ 誘導的 $F[x]$-模的不變因子）[▶ 01:30](https://youtu.be/wC7fzfnn89M?t=90)。
- **$T$-循環基底** $\langle\langle v\rangle\rangle$；**有理標準形 vs. Jordan 形**（作業很多）。
- **子模判別法**：不必會證，要會用來證明某東西是子模 [▶ 03:00](https://youtu.be/wC7fzfnn89M?t=180)。
- $R$ 是整環時模中的**線性獨立與生成**（作業有不錯的結果）；$R$ 不是整環時會怎樣。
- 主要的兩類模：$F[x]$-模（由 $T$ 或矩陣 $A$）和**交換群**（由整係數關係定義，作業中有個結果像 $\mathbb{Z}_2\oplus\mathbb{Z}_2\oplus\mathbb{Z}_{24}$）[▶ 06:30](https://youtu.be/wC7fzfnn89M?t=390)。
- （老師的電腦藍畫面，解答消失了一下。）

### 2. 交換群的例子 [▶ 08:00](https://youtu.be/wC7fzfnn89M?t=480)

- 學生提議 $\mathbb{Z}_{331}$、$\mathbb{Z}_{2011}$……最後選 $\mathbb{Z}_{100}$。$100 = 2^2\cdot5^2$，**初等因子**形式 $\mathbb{Z}_4\oplus\mathbb{Z}_{25}$。
- $\mathbb{Z}_{25}\not\cong\mathbb{Z}_5\oplus\mathbb{Z}_5$（一個循環一個不是）；$\mathbb{Z}_{100}\not\cong\mathbb{Z}_{10}\oplus\mathbb{Z}_{10}$——**$\mathbb{Z}_{ab}\cong\mathbb{Z}_a\times\mathbb{Z}_b\iff\gcd(a,b) = 1$** [▶ 13:00](https://youtu.be/wC7fzfnn89M?t=780)。
- 課堂上大家對 $\mathbb{Z}_{100}$ 的不變因子猜了「10」等答案，老師說這例子太無聊、換一個。

> 💬 補充（非課堂內容）：$\mathbb{Z}_{100}$ 是循環群，只有一個不變因子 **100**；初等因子是 $4,25$。

- **更好的例子** [▶ 14:00](https://youtu.be/wC7fzfnn89M?t=840)：不變因子 $a_1 = 2$、$a_2 = 4\cdot5 = 20$、$a_3 = 8\cdot25 = 200$（$2\mid20\mid200$）。（「Violet，為什麼你不能更像 Isaiah？」）
  - 不變因子形式：$\mathbb{Z}_2\oplus\mathbb{Z}_{20}\oplus\mathbb{Z}_{200}$，階 $8000$。這種寫法**唯一**。
  - 初等因子形式：$\mathbb{Z}_2\oplus\mathbb{Z}_4\oplus\mathbb{Z}_5\oplus\mathbb{Z}_8\oplus\mathbb{Z}_{25}$，順序不唯一 [▶ 17:00](https://youtu.be/wC7fzfnn89M?t=1020)。
  - 交換群那邊的書，整除條件有時寫成反方向，小心別搞混。
  - **準素分量**（Thm 7）：2-準素分量 $\mathbb{Z}_2\oplus\mathbb{Z}_4\oplus\mathbb{Z}_8$ 和 5-準素分量 $\mathbb{Z}_5\oplus\mathbb{Z}_{25}$，分別被 2 的冪、5 的冪零化 [▶ 18:30](https://youtu.be/wC7fzfnn89M?t=1110)。

### 3. 作業解答（模） [▶ 19:30](https://youtu.be/wC7fzfnn89M?t=1170)

（有人明天考；「讓 Daniel 週三考就好」——「Heidi 懂我。」）
- **子模判別法**題：理想係數的有限和，關鍵是 $rb_j$ 仍在理想裡（超封閉）。
- **撓不一定是子模**：$\mathbb{Z}_6$ 中撓元素是 $\{0,2,3,4\}$（與 6 不互質的），但 $2+3 = 5$ 不在裡面 [▶ 21:30](https://youtu.be/wC7fzfnn89M?t=1290)。$R$ 有零因子時，每個非零 $R$-模都有非零撓元素。
- **核與像是子模**：$\varphi(0) = 0$ 非空；$rx+y$ 封閉——和線性代數證核是子空間一樣 [▶ 22:30](https://youtu.be/wC7fzfnn89M?t=1350)。
- **$\mathrm{Hom}_R(R,M)\cong M$**：$\varphi\mapsto\varphi(1)$，再找出反映射。
- **習題 78**：$(A_1\times A_2)/(B_1\times B_2)\cong A_1/B_1\times A_2/B_2$。$f = \pi_1\times\pi_2$，可加、提得出 $r$、滿射，核 $B_1\times B_2$，第一同構定理 [▶ 25:00](https://youtu.be/wC7fzfnn89M?t=1500)。
- **有限交換群是撓 $\mathbb{Z}$-模**：$|G| = n$ ⇒ $ng = 0$。無窮的例子：$\mathbb{Z}_2[x]$（任何東西加兩次是 0）；$\mathbb{Z}_p[x]$ 等 [▶ 27:00](https://youtu.be/wC7fzfnn89M?t=1620)。
- **$\mathrm{Hom}_R(F,R)\cong F$**（$F$ 自由，基底 $a_1,\dots,a_n$）：$S(\varphi) = \varphi(a_1)a_1+\cdots+\varphi(a_n)a_n$；滿射靠線性延拓；核為 0。學生用 Prop. 5（內外直和）直接得到（「用定理當鐵鎚」）[▶ 28:30](https://youtu.be/wC7fzfnn89M?t=1710)。
- **中心冪等元**（$e^2 = e$ 且與一切交換——「像 Spano 喜歡的那種環論題」）：$1-e$ 也在中心；$eM$、$(1-e)M$ 是子模（習題 14），$x = ex+(1-e)x$，交集為 0，所以 $M = eM\oplus(1-e)M$ [▶ 31:30](https://youtu.be/wC7fzfnn89M?t=1890)。

### 4. 作業解答（張量） [▶ 33:30](https://youtu.be/wC7fzfnn89M?t=2010)

- $\mathbb{C}\otimes\mathbb{C}$：元素是簡單張量的**有限和**，不一定能寫成單一簡單張量。實純量乘法**就是定義**為 $r\sum a_i\otimes b_i = \sum(ra_i)\otimes b_i$——學生和老師之前就是卡在「推導」這個定義 [▶ 34:00](https://youtu.be/wC7fzfnn89M?t=2040)。
- 要點：$\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$ 實維數 4（$\cong\mathbb{R}^2\otimes\mathbb{R}^2$）；$\mathbb{C}\otimes_\mathbb{C}\mathbb{C}\cong\mathbb{C}$ 實維數 2。明確計算：$(a+ib)\otimes(c+id) = [(ac-bd)+i(ad+bc)](1\otimes1)$（在 $\otimes_\mathbb{C}$ 中 $i$ 可以穿過張量號）[▶ 37:00](https://youtu.be/wC7fzfnn89M?t=2220)。
- **$e_1\otimes e_2+e_2\otimes e_1$ 不是簡單張量**：假設 $= (ae_1+be_2)\otimes(ce_1+de_2)$，得 $ac = 0$、$ad = 1$、$bc = 1$、$bd = 0$，無解 [▶ 38:00](https://youtu.be/wC7fzfnn89M?t=2280)。
- **$S\otimes_RR[x]\cong S[x]$**：線性延拓 $s\otimes f\mapsto sf$；最有趣的是保持乘法（單項式指數相加、係數在 $R$ 上可以提出）[▶ 38:30](https://youtu.be/wC7fzfnn89M?t=2310)。
- **反對稱雙線性形式 ↔ $\bigwedge^2$**（「用了三個寶寶」）：$x = \sum e^i(x)e_i$，代入 $B(x,y)$，把和分成 $k<\ell$、$k>\ell$，重新命名後合併成楔積，張成；代入特定的 $(e_i,e_j)$ 證線性獨立。維數 $\binom n2 = \frac12(n^2-n)$——就是 Math 321 的反對稱矩陣空間的維數 [▶ 40:00](https://youtu.be/wC7fzfnn89M?t=2400)。

### 5. 作業解答（標準形） [▶ 42:30](https://youtu.be/wC7fzfnn89M?t=2550)

**習題 91**（「很長」）：給定特徵多項式（含 $x^2-2$ 和 $(x-3)$ 的冪），列出所有可能。
- **$\mathbb{Q}$ 上**：6 種情況。例：最小 = 特徵多項式（一個不變因子，一個伴隨矩陣）；兩個不變因子；三個（其中兩個相等——**不變因子可以相等**）；……每種都列出初等因子。$\sqrt2,\sqrt3$ 不在 $\mathbb{Q}$，所以**沒有 Jordan 形**。
- **$\mathbb{R}$ 上**：12 種情況（$x^2-2 = (x-\sqrt2)(x+\sqrt2)$ 分裂了），老師只展開幾種 [▶ 46:00](https://youtu.be/wC7fzfnn89M?t=2760)：
  - 情況 12：最小多項式沒有重複一次因式 ⇒ 可對角化；但有理標準形**不是**對角的。
  - 情況 1、6：Jordan 塊對應初等因子，順序可換。
- **$\mathbb{C}$ 上**（另一題含 $x^3-2$）：分成三個一次因式，16 種情況（「我只檢查 $\mathbb{Q}$ 上情況不多，沒想到擴大體後會暴增，抱歉」）[▶ 50:00](https://youtu.be/wC7fzfnn89M?t=3000)。
- **要點**：特徵多項式加最小多項式**都不足以**決定相似類；要知道全部不變因子（或全部初等因子）[▶ 51:00](https://youtu.be/wC7fzfnn89M?t=3060)。

**$A\sim A^T$** [▶ 51:30](https://youtu.be/wC7fzfnn89M?t=3090)：老師以為能直接用 Jordan 形，但題目沒說在 $\mathbb{C}$ 上。正確論證：Smith 標準形由 $xI-A$ 各階子式的 gcd 決定，$xI-A^T$ 的一樣，所以兩者有相同的有理標準形，相似是等價關係 ⇒ $A\sim A^T$。

**$A^2 = I$ 的矩陣可對角化** [▶ 53:00](https://youtu.be/wC7fzfnn89M?t=3180)：最小多項式整除 $(x-1)(x+1)$。除非**特徵 2**（$1 = -1$，因式重複），否則沒有重複一次因式 ⇒ 可對角化。「這門課另一個重要教訓：**可對角化 ⇔ 最小多項式是相異一次因式的乘積**。」

**純量擴張的矩陣** [▶ 54:00](https://youtu.be/wC7fzfnn89M?t=3240)：$T_E = \mathrm{id}_E\otimes T$ 在基底 $1\otimes v_j$ 下的矩陣就是 $T$ 原本的矩陣（$F$-純量可以穿過張量號）。這推廣了**複化**。另一題：每條 $k$-鏈都有共軛 $k$-鏈，合起來給出實 Jordan 基底（Math 321 的內容）。

**$\mathcal{A}$-數**（習題 98、99）[▶ 57:30](https://youtu.be/wC7fzfnn89M?t=3450)：正則表示的反映射公式老師還不完全確定；考試若考，會給第一個基底元素是 1 的基底。
- 老師承認之前「賣了你們一個假貨」：$\det = 0$ 表示矩陣不可逆，確實有矩陣乘它得 0——但**那個矩陣是否也在正則表示裡**並不顯然。他的論文（第 34 講貼的）第 11 頁用**最小多項式**證明這點 [▶ 59:00](https://youtu.be/wC7fzfnn89M?t=3540)。（結尾在第 43 集。）

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 中心冪等元 | central idempotent | §3 |
| 反對稱雙線性形式 | antisymmetric bilinear form | §4 |
| 對偶基底 | dual basis | §4 |

## ⚠️ 待確認清單

（本集無）
