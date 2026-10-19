---
course: Abstract Algebra I (Fall 2016)
episode: 30
lecture: L20
date: 2016-10-19
video: https://www.youtube.com/watch?v=FhfqXJeQwEw
notes: AlgebraInotes_2018.pdf §3.7 Lecture 17（p.116–118）；Sylow 定理講義（Beachy & Blair、Nicholson 影印）
---

# 第 30 集 · L20：共軛類、類方程、Cauchy 定理、Sylow 定理簡介 [▶ 影片](https://www.youtube.com/watch?v=FhfqXJeQwEw&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[29-答疑課-L10-12習題解答]] ｜ [總目錄](../README.md) ｜ 下一集：[[31-答疑課]] →

## 本集概要

- **共軛保持循環型**（更正上一堂的錯誤想法）；$S_n$ 的共軛類就是循環型。
- 共軛類記號 $x^G$；$|x^G| = [G:C(x)]$。推論：每種循環型的置換個數整除 $n!$。$S_4$：$1+6+8+6+3$；$S_5$：$1+10+20+30+24+20+15 = 120$（作業提示）。
- **類方程** $|G| = |Z(G)| + \sum[G:C(x_i)]$。
- **Cauchy 定理**：質數 $p$ 整除 $|G|$，則 $G$ 有 $p$ 階元素。用強歸納法和類方程證明（交換群的情形是作業）。
- **Sylow 定理**（只介紹，不考）：Sylow 本人是高中老師；三個定理的陳述；應用：100 階群有正規的 25 階子群。

> 📘 講義對應：2018 講義 §3.7 Lecture 17「conjugacy and the class equation」（p.116–118）。Sylow 部分是課堂發的影印講義（Beachy & Blair、Nicholson《Introduction to Abstract Algebra》3rd ed.）。老師明說**不期望大家會陳述或應用 Sylow 定理**。

---

## 筆記

### 1. 共軛保持循環型 [▶ 01:30](https://youtu.be/FhfqXJeQwEw?t=90)

**複習**：$\langle\sigma\rangle$ 作用在數字上，軌道就是互斥循環。例：$\sigma = (1234)(56)(78)$，1 的軌道 $\{1,2,3,4\}$、5 的軌道 $\{5,6\}$、7 的軌道 $\{7,8\}$，9、10 不動。

**更正** [▶ 02:30](https://youtu.be/FhfqXJeQwEw?t=150)：老師昨天在答疑課發現自己一直以為「用置換共軛，循環不變」。**不對。**

**例：$\alpha = (12)(34)\in S_4$**

| 用誰共軛 | 結果 |
|---|---|
| $(123)$ | $(14)(23)$ |
| $(124)$ | $(13)(24)$ |
| $(23)$ | $(13)(24)$ |
| $(1234)$ | $(14)(23)$ |
| $(12)$ | $(12)(34)$（不變） |

共同點：都是**兩個互斥換位的乘積**——**循環型 (cycle type)** 相同 [▶ 04:00](https://youtu.be/FhfqXJeQwEw?t=240)。用 $\alpha$ 自己的循環 $(12)$ 或 $(34)$ 共軛，$\alpha$ 不變。

- 4-循環共軛還是 4-循環：$(12)(1234)(12) = (1342)$ [▶ 05:00](https://youtu.be/FhfqXJeQwEw?t=300)。
- 3-循環共軛還是 3-循環：$(124)(123)(124)^{-1} = (243)$ [▶ 05:30](https://youtu.be/FhfqXJeQwEw?t=330)。

> **定理（不證）**　若 $\alpha = \beta_1\cdots\beta_t$ 是互斥循環分解，則任何共軛 $\sigma\alpha\sigma^{-1} = \gamma_1\cdots\gamma_t$ 也是互斥循環分解，而且可以排成 $|\gamma_i| = |\beta_i|$ [▶ 07:00](https://youtu.be/FhfqXJeQwEw?t=420)。

（具體地：$\sigma(a_1\cdots a_k)\sigma^{-1} = (\sigma(a_1)\cdots\sigma(a_k))$。）

**所以**：$S_n$ 中互相共軛的置換，循環型相同。

### 2. 共軛類的大小 [▶ 08:00](https://youtu.be/FhfqXJeQwEw?t=480)

> **推論（軌道穩定子定理）**　$G$ 有限，$x\in G$。
> $$|\{gxg^{-1}\mid g\in G\}| = [G:C(x)].$$

共軛作用：軌道 = 共軛類，穩定子 = $\{g\mid gxg^{-1} = x\} = C(x)$ [▶ 09:00](https://youtu.be/FhfqXJeQwEw?t=540)。

**記號** [▶ 10:00](https://youtu.be/FhfqXJeQwEw?t=600)：群論學家常把 $x$ 的共軛類寫成 $x^G$。所以 $|x^G| = [G:C(x)]$。

> **推論的推論**　$S_n$ 中具有某種循環型的置換個數整除 $n!$ [▶ 11:00](https://youtu.be/FhfqXJeQwEw?t=660)。

$S_n$ 的共軛類就是循環型，$|x^G| = [S_n:C(x)]$，而 $[S_n:C(x)]\cdot|C(x)| = n!$。

**$S_4$** [▶ 12:30](https://youtu.be/FhfqXJeQwEw?t=750)：$1,6,8,6,3$ 都整除 24；加起來也是 24（循環型分割 $S_4$）。（6 個換位：$(12),(13),(14),(23),(24),(34)$。）

老師想到一個「三階推論」：$n!$ 可以寫成若干個 $n!$ 的因數之和——「我不確定這有沒有特別有趣」[▶ 14:00](https://youtu.be/FhfqXJeQwEw?t=840)。

**$S_5$（作業提示）** [▶ 15:30](https://youtu.be/FhfqXJeQwEw?t=930)
$$120 = 1+10+20+30+24+20+15.$$
（依序是恆等、換位、3-循環、4-循環、5-循環、3-循環×換位、兩個換位。）

### 3. Cauchy 定理 [▶ 16:00](https://youtu.be/FhfqXJeQwEw?t=960)

> **定理（Cauchy 定理）**　$G$ 是有限群，質數 $p$ 整除 $|G|$。則 $G$ 有 $p$ 階元素。

**沒有**假設 $G$ 是循環群或交換群。**作業**：證明 $G$ 是**交換群**的情形（「不像上一題那麼簡單，但會給提示」）[▶ 16:30](https://youtu.be/FhfqXJeQwEw?t=990)。

**證明（對 $|G|$ 強歸納）** [▶ 17:30](https://youtu.be/FhfqXJeQwEw?t=1050)

老師覺得「對群的階做歸納」很有想像力，他自己從方程式的角度大概想不到。

- **$|G| = 1$**：沒有質因數，不用檢查。
- **歸納假設**：定理對所有階 $<n$ 的群成立；設 $|G| = n$，$p\mid n$。
- $G$ 交換的情形是作業，以下設 $G$ **不交換**，所以有 $x\notin Z(G)$ [▶ 22:00](https://youtu.be/FhfqXJeQwEw?t=1320)。

**觀察** [▶ 19:00](https://youtu.be/FhfqXJeQwEw?t=1140)：$x\in Z(G)\iff gxg^{-1} = x$ 對所有 $g\iff x^G = \{x\}$。所以 $x\notin Z(G)$ 時共軛類多於一個元素，$[G:C(x)]>1$，$C(x)$ 是**真子群**，$|C(x)|<n$。

**情形 1：$p\mid|C(x)|$（某個非中心的 $x$）** [▶ 22:00](https://youtu.be/FhfqXJeQwEw?t=1320)：由歸納假設，$C(x)$ 有 $p$ 階元素，它也在 $G$ 裡。

**情形 2：對所有非中心的 $x$，$p\nmid|C(x)|$** [▶ 22:30](https://youtu.be/FhfqXJeQwEw?t=1350)
- $|G| = [G:C(x)]\cdot|C(x)|$，$p\mid|G|$。
- **Euclid 引理**：質數整除乘積，就整除其中一個因數（質數不能拆成兩半）[▶ 23:30](https://youtu.be/FhfqXJeQwEw?t=1410)。所以 $p\mid[G:C(x)]$。
- **類方程 (class equation)** [▶ 24:00](https://youtu.be/FhfqXJeQwEw?t=1440)：共軛類分割 $G$；單點的共軛類正好是中心的元素。所以
$$|G| = |Z(G)| + \sum_i[G:C(x_i)],$$
  每個非單點共軛類取一個代表 $x_i$。
- $p$ 整除 $|G|$，也整除每個 $[G:C(x_i)]$，所以 $p\mid|Z(G)|$ [▶ 25:00](https://youtu.be/FhfqXJeQwEw?t=1500)。
- $Z(G)$ 是**交換群**，由作業，它有 $p$ 階元素；而 $Z(G)\le G$。$\blacksquare$

**推論**：有 $p$ 階元素，就有 $p$ 階（循環）子群 [▶ 26:00](https://youtu.be/FhfqXJeQwEw?t=1560)。

**例**：$|G| = 11\cdot13\cdot53$，則 $G$ 有 11 階、13 階、53 階子群 [▶ 27:30](https://youtu.be/FhfqXJeQwEw?t=1650)。

> 💬 老師提到 Grothendieck 被要求舉一個具體質數的故事（「改變了數學，但你們大概現在才聽到他的名字」）。他記不清是 51 還是 53。眾所周知的版本是 **57**（所謂「Grothendieck 質數」，其實 $57 = 3\times19$ 不是質數）[▶ 27:00](https://youtu.be/FhfqXJeQwEw?t=1620)。

**和 Lagrange 的對比** [▶ 28:00](https://youtu.be/FhfqXJeQwEw?t=1680)：Lagrange 說子群的階**必須**整除群的階，但不保證那些子群**存在**。就像微積分的 Fermat 定理：極值處導數為 0 或不存在，但臨界點不一定是極值。Cauchy 定理說：**質因數階的子群一定存在**。

### 4. Sylow 定理（介紹）[▶ 29:00](https://youtu.be/FhfqXJeQwEw?t=1740)

老師發了影印講義。**不期望會陳述，甚至寧願你們不要去用**；只希望大家欣賞這些定理。想看證明可以看 Harvard 的 Gross 教授的 YouTube 課程 [▶ 30:00](https://youtu.be/FhfqXJeQwEw?t=1800)。

**Sylow 小傳**（Nicholson）[▶ 31:00](https://youtu.be/FhfqXJeQwEw?t=1860)：Peter Ludwig Mejdell Sylow（1832–1918），挪威人，大半輩子在 Halden 當**高中老師**。教學負擔很重，還是研讀 Abel，1862–63 年在 Christiania 大學（奧斯陸）講 Galois 理論和置換群。Sylow 定理 1872 年發表（針對置換群），1887 年 Frobenius 推廣到抽象群。他用這些定理證明：Galois 群是質數冪階的方程可以用根式解。他還花了 8 年編輯 Abel 的全集；從高中退休後才被聘為 Christiania 的講座教授。

> 💬 老師說他也希望教自己的孩子高中數學；「去高中教書然後當上 UVA 的系主任？現在好像不會發生了。」[▶ 33:00](https://youtu.be/FhfqXJeQwEw?t=1980)

> **Sylow 第一定理**　若 $p^\alpha$ 整除 $|G|$（$\alpha\ge1$），則 $G$ 有 $p^\alpha$ 階子群 [▶ 34:30](https://youtu.be/FhfqXJeQwEw?t=2070)。

是 Cauchy 定理的加強版；證明同樣是用共軛作用。

> **定義（Sylow $p$-子群）**　$P\le G$，$|P| = p^\alpha$，且 $p^\alpha\mid|G|$ 但 $p^{\alpha+1}\nmid|G|$。也就是 $G$ 中「最大的 $p$ 冪階」子群 [▶ 35:30](https://youtu.be/FhfqXJeQwEw?t=2130)。

**例**：$|G| = 250 = 2\cdot5^3$。125 階子群是 Sylow 5-子群，2 階子群是 Sylow 2-子群。25 階子群存在，但不是 Sylow 5-子群 [▶ 36:30](https://youtu.be/FhfqXJeQwEw?t=2190)。

**引理**（講義）：$|G| = mp^\alpha$，$p\nmid m$。若 Sylow $p$-子群 $P$ 是**正規**的，則它包含 $G$ 的每個 $p$-子群 [▶ 37:30](https://youtu.be/FhfqXJeQwEw?t=2250)。（上例中 125 階子群指數為 2，一定正規。）

> **Sylow 第二、三定理**　[▶ 38:30](https://youtu.be/FhfqXJeQwEw?t=2310)
> - 所有 Sylow $p$-子群彼此**共軛**；每個 $p$-子群都包含在某個 Sylow $p$-子群裡。
> - 設 $|G| = mp^\alpha$，$\gcd(m,p) = 1$，Sylow $p$-子群有 $k$ 個，則 $k\mid m$ 且 $k\equiv1\pmod p$。

**為什麼不多講** [▶ 39:00](https://youtu.be/FhfqXJeQwEw?t=2340)：與其花一週證 Sylow，不如講基本的**環論**；有些人不會修 Math 422，離開第一門課前應該對代數的整體結構有個概念。

**應用例** [▶ 39:30](https://youtu.be/FhfqXJeQwEw?t=2370)
- **100 階群有正規的 25 階子群**：$100 = 4\cdot25$，Sylow 5-子群個數 $k\mid4$ 且 $k\equiv1\pmod5$，只能 $k = 1$。唯一的 Sylow 5-子群和它所有共軛都相等，所以正規。
- **$pq$ 階的群不是單群**（講義 Example 5）[▶ 40:30](https://youtu.be/FhfqXJeQwEw?t=2430)。$p = q$ 的情形用到「有限 $p$-群的中心非平凡」（講義 Thm 7；**$p$-群**：每個元素的階都是 $p$ 的冪）。$|G| = p^2$ 時：若 $Z(G)\neq G$，$Z(G)$ 是非平凡真正規子群；若 $Z(G) = G$，$G$ 交換而 $p^2$ 不是質數，也不是單群。

這些例子用目前的工具很難證；Sylow 定理讓你能解另一類更難的問題 [▶ 43:30](https://youtu.be/FhfqXJeQwEw?t=2610)。

**下次預告** [▶ 44:00](https://youtu.be/FhfqXJeQwEw?t=2640)：週五講**格定理**，完成同構定理的故事（第二、三、四同構定理），也會談一點有限單群（資訊性質）。下週三考試；明天答疑課講更多作業解答。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 循環型 | cycle type | [04:00](https://youtu.be/FhfqXJeQwEw?t=240) |
| 共軛類記號 | $x^G$ | [10:00](https://youtu.be/FhfqXJeQwEw?t=600) |
| Cauchy 定理 | Cauchy's Theorem | [16:00](https://youtu.be/FhfqXJeQwEw?t=960) |
| 強歸納法 | strong induction | [18:30](https://youtu.be/FhfqXJeQwEw?t=1110) |
| 非中心元素 | non-central element | [22:00](https://youtu.be/FhfqXJeQwEw?t=1320) |
| Euclid 引理 | Euclid's lemma | [23:30](https://youtu.be/FhfqXJeQwEw?t=1410) |
| 類方程 | class equation | [24:00](https://youtu.be/FhfqXJeQwEw?t=1440) |
| Sylow $p$-子群 | Sylow $p$-subgroup | [35:30](https://youtu.be/FhfqXJeQwEw?t=2130) |
| $p$-群 | $p$-group | [42:00](https://youtu.be/FhfqXJeQwEw?t=2520) |

## ⚠️ 待確認清單

（本集無）
