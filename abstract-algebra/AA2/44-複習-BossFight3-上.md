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

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 44 集，期末複習
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）。沒有講義；老師投影最後一份作業（Mission）的解答。
> **標記說明**：`【口頭】` 老師口頭補充；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`💬` 筆記補充或更正；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：學期最後一堂，第三次考試（**Boss Fight 3**）前的複習。只記課堂上實際講到的題目。這堂超過一小時，結尾 5 分鐘在 [[43-複習-BossFight3-下]]。

---

## 目錄

- [1. 考試範圍](#1-考試範圍)
- [2. Abel 群的例子：不變因子、初等因子、準素分量](#2-abel-群的例子不變因子初等因子準素分量)
- [3. 作業解答：模](#3-作業解答模)
- [4. 作業解答：張量](#4-作業解答張量)
- [5. 作業解答：標準形](#5-作業解答標準形)
- [6. 作業解答：𝒜-數](#6-作業解答𝒜-數)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 1. 考試範圍

[▶ 00:00](https://youtu.be/wC7fzfnn89M?t=0) 課前禱告。「為了即將到來的 Boss Fight，我想……」

[▶ 00:30](https://youtu.be/wC7fzfnn89M?t=30)
- **張量積**；**直和**；**$R$-模**；**撓**；**零化子**；§12.1 **Thm 5（不變因子）vs. Thm 6（初等因子）**。
- 會算 **Smith 標準形**[▶ 01:30](https://youtu.be/wC7fzfnn89M?t=90)：$F^{n\times n}$ 的矩陣，或 $\mathbb{Z}$-模的**關係矩陣**——而且會**解讀**它（給出 $A$ 誘導的 $F[x]$-模的不變因子）。
- **$T$-循環基底** $\langle\!\langle v\rangle\!\rangle$；**有理標準形 vs. Jordan 形**（作業很多）。
- **子模判別法**[▶ 03:00](https://youtu.be/wC7fzfnn89M?t=180)：不必會證，要會**用**它證某東西是子模。
- $R$ 是整環時模中的**線性獨立與生成**（作業有不錯的結果）；$R$ 不是整環時會怎樣。
- [▶ 06:30](https://youtu.be/wC7fzfnn89M?t=390) 主要的兩類模：**$F[x]$-模**（由 $T$ 或矩陣 $A$）和 **Abel 群**（由整係數關係定義——作業中有個結果像 $\mathbb{Z}_2\oplus\mathbb{Z}_2\oplus\mathbb{Z}_{24}$）。
- （老師的電腦**藍畫面**，解答消失了一下。）

---

## 2. Abel 群的例子：不變因子、初等因子、準素分量

[▶ 08:00](https://youtu.be/wC7fzfnn89M?t=480)【課堂討論】「給個 Abel 群。」學生提議 $\mathbb{Z}_{331}$、$\mathbb{Z}_{2011}$……最後選 **$\mathbb{Z}_{100}$**。
- $100 = 2^2\cdot5^2$ ⇒ **初等因子形式** $\mathbb{Z}_4\oplus\mathbb{Z}_{25}$。
- $\mathbb{Z}_{25}\not\cong\mathbb{Z}_5\oplus\mathbb{Z}_5$（一個循環、一個不是）；$\mathbb{Z}_{100}\not\cong\mathbb{Z}_{10}\oplus\mathbb{Z}_{10}$——
$$\mathbb{Z}_{ab}\cong\mathbb{Z}_a\times\mathbb{Z}_b\iff\gcd(a,b) = 1\qquad[▶\ 13{:}00].$$
- 課堂上對 $\mathbb{Z}_{100}$ 的不變因子有人猜「10」等，老師說這例子**太無聊**、換一個。

💬 $\mathbb{Z}_{100}$ 是循環群，**只有一個**不變因子 **100**；初等因子是 $4,25$。

**更好的例子**[▶ 14:00](https://youtu.be/wC7fzfnn89M?t=840)：不變因子 $a_1 = 2$、$a_2 = 4\cdot5 = 20$、$a_3 = 8\cdot25 = 200$（$2\mid20\mid200$）。（「Violet，你為什麼**不能更像 Isaiah**？」）
- **不變因子形式**：$\mathbb{Z}_2\oplus\mathbb{Z}_{20}\oplus\mathbb{Z}_{200}$，階 8000。這種寫法**唯一**。
- **初等因子形式**[▶ 17:00](https://youtu.be/wC7fzfnn89M?t=1020)：$\mathbb{Z}_2\oplus\mathbb{Z}_4\oplus\mathbb{Z}_5\oplus\mathbb{Z}_8\oplus\mathbb{Z}_{25}$，**順序不唯一**。
- 【口頭】「Abel 群那邊的書，整除條件有時寫成**反方向**——小心別搞混。」
- **準素分量**（Thm 7）[▶ 18:30](https://youtu.be/wC7fzfnn89M?t=1110)：2-準素分量 $\mathbb{Z}_2\oplus\mathbb{Z}_4\oplus\mathbb{Z}_8$、5-準素分量 $\mathbb{Z}_5\oplus\mathbb{Z}_{25}$，分別被 2 的冪、5 的冪零化。

---

## 3. 作業解答：模

[▶ 19:30](https://youtu.be/wC7fzfnn89M?t=1170)（有人明天考；「讓 Daniel 週三考就好。」「**Heidi 懂我**。」）
- **子模判別法**題：理想係數的有限和，關鍵是 $rb_j$ 仍在理想裡（**超封閉**）。
- **撓不一定是子模**[▶ 21:30](https://youtu.be/wC7fzfnn89M?t=1290)：$\mathbb{Z}_6$ 作為自己的模，撓元素是 $\{0,2,3,4\}$（與 6 不互質的），但 $2+3 = 5$ 不在裡面。$R$ 有零因子時，每個非零 $R$-模都有非零撓元素。
- **核與像是子模**[▶ 22:30](https://youtu.be/wC7fzfnn89M?t=1350)：$\varphi(0) = 0$ ⇒ 非空；$rx+y$ 封閉——「和線代證核是子空間**一樣**」。
- **$\mathrm{Hom}_R(R,M)\cong M$**：$\varphi\mapsto\varphi(1)$，再找出反映射。
- **習題 78**[▶ 25:00](https://youtu.be/wC7fzfnn89M?t=1500)：$(A_1\times A_2)/(B_1\times B_2)\cong A_1/B_1\times A_2/B_2$。$f = \pi_1\times\pi_2$：可加、提得出 $r$、滿射，核 $B_1\times B_2$ ⇒ 第一同構定理。
- **有限 Abel 群是撓 $\mathbb{Z}$-模**[▶ 27:00](https://youtu.be/wC7fzfnn89M?t=1620)：$|G| = n$ ⇒ $ng = 0$。**無窮**的例子：$\mathbb{Z}_2[x]$（任何東西加兩次是 0）、$\mathbb{Z}_p[x]$ 等。
- **$\mathrm{Hom}_R(F,R)\cong F$**（$F$ 自由，基底 $a_1..a_n$）[▶ 28:30](https://youtu.be/wC7fzfnn89M?t=1710)：$S(\varphi) = \varphi(a_1)a_1+\cdots+\varphi(a_n)a_n$；滿射靠**線性延拓**；核為 0。學生用 Prop 5（內外直和）直接得到——「**用定理當鐵鎚**」。
- **中心冪等元**（$e^2 = e$ 且與一切交換——「像 Spano 喜歡的那種環論題」）[▶ 31:30](https://youtu.be/wC7fzfnn89M?t=1890)：$1-e$ 也在中心、也冪等；$eM$、$(1-e)M$ 是子模（習題 14），$x = ex+(1-e)x$，交集為 0 ⇒
$$M = eM\oplus(1-e)M.$$

---

## 4. 作業解答：張量

[▶ 33:30](https://youtu.be/wC7fzfnn89M?t=2010)
- **$\mathbb{C}\otimes\mathbb{C}$**：元素是簡單張量的**有限和**，不一定能寫成單一簡單張量。實純量乘法**就是定義**為 $r\sum a_i\otimes b_i = \sum(ra_i)\otimes b_i$——「學生和我之前就是卡在試圖**推導**這個定義」[▶ 34:00](https://youtu.be/wC7fzfnn89M?t=2040)。
- **要點**[▶ 37:00](https://youtu.be/wC7fzfnn89M?t=2220)：$\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$ 實維數 **4**（$\cong\mathbb{R}^2\otimes\mathbb{R}^2$）；$\mathbb{C}\otimes_\mathbb{C}\mathbb{C}\cong\mathbb{C}$ 實維數 **2**。明確計算（$\otimes_\mathbb{C}$ 中 $i$ 可以穿過張量號）：
$$(a+ib)\otimes(c+id) = \left[(ac-bd)+i(ad+bc)\right](1\otimes1).$$
- **$e_1\otimes e_2+e_2\otimes e_1$ 不是簡單張量**[▶ 38:00](https://youtu.be/wC7fzfnn89M?t=2280)：設 $= (ae_1+be_2)\otimes(ce_1+de_2)$ ⇒ $ac = 0$、$ad = 1$、$bc = 1$、$bd = 0$，**無解**。
- **$S\otimes_RR[x]\cong S[x]$**[▶ 38:30](https://youtu.be/wC7fzfnn89M?t=2310)：線性延拓 $s\otimes f\mapsto sf$；最有趣的是**保持乘法**（單項式指數相加、$R$ 係數可以提出）。
- **反對稱雙線性形式 ↔ $\bigwedge^2$**（「用了**三個寶寶**」）[▶ 40:00](https://youtu.be/wC7fzfnn89M?t=2400)：$x = \sum e^i(x)e_i$（**對偶基底**）代入 $B(x,y)$，把和分成 $k<\ell$、$k>\ell$，重新命名後合併成楔積 ⇒ 張成；代入特定的 $(e_i,e_j)$ 證線性獨立。維數 $\binom n2 = \frac12(n^2-n)$——「就是 Math 321 **反對稱矩陣**空間的維數」。

---

## 5. 作業解答：標準形

**習題 91**（「很長」）[▶ 42:30](https://youtu.be/wC7fzfnn89M?t=2550)：給定特徵多項式（含 $x^2-2$ 和 $(x-3)$ 的冪），列出所有可能。
- **$\mathbb{Q}$ 上**：6 種情況。例：最小 = 特徵多項式（一個不變因子、一個伴隨矩陣）；兩個不變因子；三個（其中兩個相等——**不變因子可以相等**）……每種都列出初等因子。$\sqrt2$ 不在 $\mathbb{Q}$ ⇒ **沒有 Jordan 形**。
- **$\mathbb{R}$ 上**[▶ 46:00](https://youtu.be/wC7fzfnn89M?t=2760)：12 種情況（$x^2-2 = (x-\sqrt2)(x+\sqrt2)$ 分裂了），老師只展開幾種：
  - 情況 12：最小多項式沒有重複一次因式 ⇒ **可對角化**；但有理標準形**不是**對角的。
  - 情況 1、6：Jordan 塊對應初等因子，**順序可換**。
- **$\mathbb{C}$ 上**（另一題含 $x^3-2$）[▶ 50:00](https://youtu.be/wC7fzfnn89M?t=3000)：分成三個一次因式，**16 種**情況。「我只檢查了 $\mathbb{Q}$ 上情況不多，**沒想到擴大體後會暴增**，抱歉。」
- **要點**[▶ 51:00](https://youtu.be/wC7fzfnn89M?t=3060)：**特徵多項式加最小多項式都不足以決定相似類**；要知道**全部**不變因子（或全部初等因子）。

**$A\sim A^T$**[▶ 51:30](https://youtu.be/wC7fzfnn89M?t=3090)：老師以為能直接用 Jordan 形，但題目**沒說**在 $\mathbb{C}$ 上。正確論證：Smith 標準形由 $xI-A$ 各階子式的 gcd 決定，$xI-A^T$ 的**一樣** ⇒ 兩者有相同的有理標準形；相似是等價關係 ⇒ $A\sim A^T$。

**$A^2 = I$ 可對角化**[▶ 53:00](https://youtu.be/wC7fzfnn89M?t=3180)：最小多項式整除 $(x-1)(x+1)$。除非**特徵 2**（$1 = -1$，因式重複），否則沒有重複一次因式 ⇒ 可對角化。
- 【口頭】「這門課**另一個重要教訓**：**可對角化 ⟺ 最小多項式是相異一次因式的乘積**。」

**純量擴張的矩陣**[▶ 54:00](https://youtu.be/wC7fzfnn89M?t=3240)：$T_E = \mathrm{id}_E\otimes T$ 在基底 $1\otimes v_j$ 下的矩陣就是 $T$ 原本的矩陣（$F$-純量可以穿過張量號）——這推廣了**複化**。另一題：每條 $k$-鏈都有**共軛** $k$-鏈，合起來給出**實 Jordan 基底**（Math 321 的內容）。

---

## 6. 作業解答：𝒜-數

**習題 98、99**[▶ 57:30](https://youtu.be/wC7fzfnn89M?t=3450)：正則表示的**反映射**公式老師還**不完全確定**；考試若考，會給**第一個基底元素是 1** 的基底。

【口頭】[▶ 59:00](https://youtu.be/wC7fzfnn89M?t=3540)「我之前**賣了你們一個假貨**：$\det = 0$ 表示矩陣不可逆，確實**存在**某個方陣乘它得 0——但**那個矩陣是否也在正則表示裡**並**不顯然**，而那才是它在表示中是零因子所需要的。其實**有點技術性**：看我第 34 講貼的論文**第 11 頁**，我用**最小多項式**證明這點。」（[[40-L34-實結合代數的正則表示]] 的 Thm 4.14。）→ 結尾在 [[43-複習-BossFight3-下]]

---

## 7. 一頁速查表

| 題目 | 要點 |
|---|---|
| $\mathbb{Z}_{ab}\cong\mathbb{Z}_a\times\mathbb{Z}_b$ | ⟺ $\gcd(a,b) = 1$ |
| $\mathbb{Z}_2\oplus\mathbb{Z}_{20}\oplus\mathbb{Z}_{200}$ | 初等因子 $2,4,8,5,25$；準素分量 2-、5- |
| 撓不一定是子模 | $\mathbb{Z}_6$：$2+3 = 5$ |
| $\mathrm{Hom}_R(R,M)\cong M$ | $\varphi\mapsto\varphi(1)$ |
| $(A_1\times A_2)/(B_1\times B_2)$ | $\cong A_1/B_1\times A_2/B_2$ |
| $\mathrm{Hom}_R(F,R)\cong F$ | 線性延拓 |
| 中心冪等元 | $M = eM\oplus(1-e)M$ |
| $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$ vs $\mathbb{C}\otimes_\mathbb{C}\mathbb{C}$ | 實維數 4 vs 2 |
| $e_1\otimes e_2+e_2\otimes e_1$ | 不是簡單張量 |
| $S\otimes_RR[x]\cong S[x]$ | $s\otimes f\mapsto sf$ |
| 反對稱雙線性形式 | $\bigwedge^2$，維數 $\binom n2$ |
| 相似類 | 需要全部不變因子 |
| $A\sim A^T$ | 同樣的 Smith 形 |
| $A^2 = I$ | 特徵 $\neq2$ ⇒ 可對角化 |
| $\mathcal{A}$ 零因子 | $\det = 0$ ⇒ 零因子要用最小多項式證 |

| 中文 | English |
|---|---|
| 中心冪等元 | central idempotent |
| 反對稱雙線性形式 | antisymmetric bilinear form |
| 對偶基底 | dual basis |
| 實 Jordan 基底 | real Jordan basis |

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **複習結尾：代數同構題** | [[43-複習-BossFight3-下]] |
| **（課程結束）** | [總目錄](../README.md) |

---

## 附：本集一句話總結

> **學期最後一堂、Boss Fight 3 前的複習：考試範圍是張量積、直和、撓與零化子、不變因子 vs. 初等因子、Smith 標準形、有理標準形與 Jordan 形、子模判別法；用 $\mathbb{Z}_2\oplus\mathbb{Z}_{20}\oplus\mathbb{Z}_{200}$ 示範三種分解；作業解答涵蓋撓不一定是子模、$\mathrm{Hom}_R(R,M)\cong M$、中心冪等元分解、$\mathbb{C}\otimes_\mathbb{R}\mathbb{C}$ 與 $\mathbb{C}\otimes_\mathbb{C}\mathbb{C}$ 的差別、非簡單張量、反對稱形式 ↔ $\bigwedge^2$、特徵＋最小多項式不足以決定相似、$A\sim A^T$、$A^2 = I$ 可對角化；最後老師承認 $\mathcal{A}$-數零因子的論證需要最小多項式補上。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) 期末複習課錄影逐字稿前段（YouTube 自動字幕，59:51）整理；無講義，內容為老師投影的作業解答。*
