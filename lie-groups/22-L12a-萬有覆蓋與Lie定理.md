---
course: Matrix Lie Groups (Spring 2016)
episode: 22
lecture: L12a
date: 2016-04-25（part 1）
video: https://www.youtube.com/watch?v=0Jzh0ZtTqAY
notes: Hall 第 1 版 §3.6 Thm. 3.7、§3.7 萬有覆蓋（p.79–81）、§1.6.1 SU(2) → SO(3)（p.18–19）、§3.8 子群與子代數（p.82–87）
---

# 第 22 集 · L12a：萬有覆蓋、SU(2) → SO(3) 的明確映射、連通李子群 [▶ 影片](https://www.youtube.com/watch?v=0Jzh0ZtTqAY&list=PLBY4G2o7DhF3FS2CaX62eiQWGP9_xdLYs)

← 上一集：[[21-L11b-BCH三階項]] ｜ [總目錄](README.md) ｜ 下一集：[[23-L12b-Lie定理收尾]] →

> **課程**：Matrix Lie Groups（Liberty University，Spring 2016）— 第 22 集，April 25 part 1
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（59:51，自動字幕）＋ Hall《Lie Groups, Lie Algebras, and Representations》第 1 版 §1.6.1（p.18–19）、§3.6–3.8（p.77–87）
> **標記說明**：`【口頭】` 老師口頭補充、課本沒有；`【Q&A】` 學生提問；`【課堂討論】` 老師問、學生答；`【課本補充】` 課本有、課堂沒講；`⚠️ 逐字稿缺字` 自動字幕聽錯或掉字；`[▶ mm:ss]` 點了跳到影片該時間點

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 萬有覆蓋的定義](#1-萬有覆蓋的定義)
- [2. 例 1：S¹ 的萬有覆蓋是 ℝ](#2-例-1s¹-的萬有覆蓋是-ℝ)
- [3. 例 2：SO(3) 的萬有覆蓋是 SU(2)——終於有明確映射](#3-例-2so3-的萬有覆蓋是-su2終於有明確映射)
- [4. 例 3、4：U(n)、SO(n)；SL(n, ℝ)](#4-例-34unsonsln-ℝ)
- [5. 子群與子代數](#5-子群與子代數)
  - [5.1 反方向不一定成立](#51-反方向不一定成立)
  - [5.2 放寬定義：連通李子群](#52-放寬定義連通李子群)
  - [5.3 主要定理](#53-主要定理)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:02](https://youtu.be/0Jzh0ZtTqAY?t=2) 「這大概是這本書的終點了。」講 Hall §3.7 覆蓋群、§3.8 子群與子代數。

【口頭】[▶ 03:15](https://youtu.be/0Jzh0ZtTqAY?t=195) 「學期這時候我特別累，所以不證了。不是定理變難，是證明要花更久。我跳過的證明書上都寫得很清楚，所以不算太大的罪過。」

> 【課本補充】Hall §3.6 的核心定理（第 16 集講過動機，用 BCH 證明）：
> **Theorem 3.7（Hall p.79）**　$G, H$ 是矩陣李群，$\phi:\mathfrak g\to\mathfrak h$ 是李代數同態。若 **$G$ 單連通**，則存在唯一的李群同態 $\Phi: G\to H$ 使 $\Phi(e^X) = e^{\phi(X)}$。

## 1. 萬有覆蓋的定義

[▶ 00:35](https://youtu.be/0Jzh0ZtTqAY?t=35)

> **Definition 3.9（Hall p.80）**　$G$ 是連通李群。$G$ 的**萬有覆蓋群**（universal covering group / universal cover）是一個**單連通**李群 $H$，加上一個李群同態 $\Phi: H\to G$，使對應的李代數同態 $\phi:\mathfrak h\to\mathfrak g$ 是**同構**。$\Phi$ 叫**覆蓋同態**（covering homomorphism）或投影。

[▶ 03:52](https://youtu.be/0Jzh0ZtTqAY?t=232)

> **Theorem 3.10（Hall p.80）**　每個連通李群都有萬有覆蓋。若 $(H_1, \Phi_1)$、$(H_2, \Phi_2)$ 都是 $G$ 的萬有覆蓋，則存在李群同構 $\Psi: H_1\to H_2$ 使 $\Phi_2\circ\Psi = \Phi_1$。

[▶ 05:39](https://youtu.be/0Jzh0ZtTqAY?t=339) 所以萬有覆蓋**在標準同構意義下唯一**，記作 $(\tilde G, \Phi)$。

[▶ 06:26](https://youtu.be/0Jzh0ZtTqAY?t=386) 非正式說法：**$G$ 的萬有覆蓋，是唯一一個李代數和 $G$ 相同的單連通群 $\tilde G$**。覆蓋同態就是「對應的李代數映射是恆等」的那個唯一的李群同態（存在性由 Thm. 3.7）。

【口頭】[▶ 07:01](https://youtu.be/0Jzh0ZtTqAY?t=421) 「偶爾我會想起以前修過的李群課……要真的講透這些，會是三小時的研究所課。」

[▶ 10:34](https://youtu.be/0Jzh0ZtTqAY?t=634) 注意：**不是所有**連通矩陣李群的萬有覆蓋都還是矩陣李群。證明要用到不少表示論（Hall 附錄 C.3）：假設萬有覆蓋有某種表示，它必須是**忠實的**（faithful），再證明它不是。例子是 **$SL(n, \mathbb{R})$**。「它還是有萬有覆蓋，只是會把你帶出矩陣李群的世界。」

## 2. 例 1：S¹ 的萬有覆蓋是 ℝ

[▶ 11:41](https://youtu.be/0Jzh0ZtTqAY?t=701) $S^1$ 的李代數是 $\mathbb{R}$（交換）。

【課堂討論】[▶ 12:24](https://youtu.be/0Jzh0ZtTqAY?t=744) $S^1$ 單連通嗎？
- 什麼是**單連通**（simply connected）：圈可以縮成一點；用基本群的話，**基本群是平凡的**。
- 繞圓一圈的圈縮不回去，所以 $S^1$ **不**單連通。

[▶ 13:03](https://youtu.be/0Jzh0ZtTqAY?t=783)

$$
\tilde{S^1} = \mathbb{R},\qquad\Phi:\mathbb{R}\to S^1,\quad\theta\mapsto e^{i\theta}.
$$

## 3. 例 2：SO(3) 的萬有覆蓋是 SU(2)——終於有明確映射

[▶ 13:48](https://youtu.be/0Jzh0ZtTqAY?t=828) $SU(2)$ 和 $SO(3)$ 有相同的李代數（相同的結構常數）。覆蓋同態「一點也不簡單（非技術意義）」。

【課堂討論】[▶ 15:29](https://youtu.be/0Jzh0ZtTqAY?t=929) 學生：這就是學期初那個讓我們煩惱的問題吧？老師：對，Hall 說「就是 §1.6 描述的映射」，那裡有細節。

[▶ 16:10](https://youtu.be/0Jzh0ZtTqAY?t=970) **構造（Hall §1.6.1，p.18）**：$V$ = 所有**自伴**（self-adjoint，$A^* = A$）、**跡為零**的 $2\times 2$ 複數矩陣。它是 3 維**實**向量空間，基底

$$
A_1 = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix},\quad A_2 = \begin{pmatrix}0 & i\\ -i & 0\end{pmatrix},\quad A_3 = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}.
$$

內積

$$
\langle A, B\rangle = \tfrac12\operatorname{tr}(AB).
$$

【課堂討論】[▶ 18:25](https://youtu.be/0Jzh0ZtTqAY?t=1105) 算 $A_1A_2 = \begin{pmatrix}-i & 0\\ 0 & i\end{pmatrix} = -iA_3$，跡為 0。其他乘積也類似，所以兩兩正交。[▶ 18:58](https://youtu.be/0Jzh0ZtTqAY?t=1138) $A_k^2 = I$，$\frac12\operatorname{tr}I = 1$。**$\{A_1, A_2, A_3\}$ 是正交規範基底**。

[▶ 19:32](https://youtu.be/0Jzh0ZtTqAY?t=1172) 用它把 $V$ 等同於 $\mathbb{R}^3$：

$$
\psi(x, y, z) = xA_1 + yA_2 + zA_3.
$$

$\psi$ 保持長度（正交規範基底）。

[▶ 20:09](https://youtu.be/0Jzh0ZtTqAY?t=1209) 對 $U\in SU(2)$，定義

$$
\Phi_U(A) = UAU^{-1}.
$$

**$\Phi_U$ 把 $V$ 映到 $V$**　[▶ 21:14](https://youtu.be/0Jzh0ZtTqAY?t=1274)
- 跡：$\operatorname{tr}(UAU^{-1}) = \operatorname{tr}A = 0$。
- [▶ 23:35](https://youtu.be/0Jzh0ZtTqAY?t=1415) 自伴：$(UAU^{-1})^* = (U^{-1})^*A^*U^* = UAU^{-1}$，因為 $U^* = U^{-1}$、$A^* = A$。

【課堂討論】[▶ 22:18](https://youtu.be/0Jzh0ZtTqAY?t=1338) 老師一度把 $V$ 說成「斜 Hermitian」，自己更正：$V$ 是**Hermitian**（$A^* = A$）跡為零的矩陣。【口頭】「我一直搞不清楚 star、bar、dagger 哪個是哪個。Hall 的 star 就是共軛轉置。我是被物理學家帶大的。」

**性質**　[▶ 24:47](https://youtu.be/0Jzh0ZtTqAY?t=1487)
- 對固定的 $U$，$A\mapsto UAU^{-1}$ 是線性的。
- [▶ 24:47](https://youtu.be/0Jzh0ZtTqAY?t=1487) $\Phi_{U_1U_2} = \Phi_{U_1}\circ\Phi_{U_2}$（襪子鞋子把 $U_2$ 放在裡面）：**同態**。
- [▶ 26:19](https://youtu.be/0Jzh0ZtTqAY?t=1579) **保持內積**：$\frac12\operatorname{tr}(UAU^{-1}UBU^{-1}) = \frac12\operatorname{tr}(UABU^{-1}) = \frac12\operatorname{tr}(AB)$（中間的 $U^{-1}U$ 抵消，外面的用跡的循環性）。所以 $\Phi_U$ 是 $V$ 上的正交變換。

[▶ 28:21](https://youtu.be/0Jzh0ZtTqAY?t=1701) 【口頭】用 $\psi$ 把它搬到 $\mathbb{R}^3$：

$$
\gamma_U = \psi^{-1}\circ\Phi_U\circ\psi:\mathbb{R}^3\to\mathbb{R}^3,
$$

[▶ 29:46](https://youtu.be/0Jzh0ZtTqAY?t=1786) 每一步都保持長度，所以是等距變換；[▶ 30:32](https://youtu.be/0Jzh0ZtTqAY?t=1832) $\gamma_{U_1U_2} = \gamma_{U_1}\gamma_{U_2}$。

[▶ 31:14](https://youtu.be/0Jzh0ZtTqAY?t=1874) **覆蓋映射**：

$$
\Phi(U) = [\gamma_U]\quad\text{（$\gamma_U$ 的標準矩陣，$3\times 3$）}.
$$

[▶ 31:52](https://youtu.be/0Jzh0ZtTqAY?t=1912) 它是正交矩陣。【口頭】「$\det = 1$ 我現在不完全確定，書上應該有講。」

> 【課本補充】Hall p.19：每個 $O(3)$ 元素的行列式是 $\pm 1$。$SU(2)$ 連通、$\Phi$ 連續、$\Phi(I) = I$，所以 $\det\Phi(U)$ 恆為 $+1$，像落在 $SO(3)$。

[▶ 32:27](https://youtu.be/0Jzh0ZtTqAY?t=1947) 【口頭】「**這就是我要你們找的那個映射**（第 5 集的作業）。沒有我想要的那麼明確，但已經很接近了。」

[▶ 33:08](https://youtu.be/0Jzh0ZtTqAY?t=1988) 從公式看出：$I$ 和 $-I$ 都映到 $SO(3)$ 的單位元素（$(-I)A(-I)^{-1} = A$），所以 **2 對 1**。

【口頭】[▶ 33:50](https://youtu.be/0Jzh0ZtTqAY?t=2030) 物理書上更明確的版本：

$$
U = e^{i\vec\sigma\cdot\vec\theta/2}\ \longmapsto\ R = e^{i\vec J\cdot\vec\theta},
$$

$\sigma_k$ 是 $SU(2)$ 的生成元（Pauli 矩陣），$J_k$ 是 $SO(3)$ 的生成元。角度差一個 $\frac12$——就是第 2 集的「$t = \cos\frac\alpha2 + u\sin\frac\alpha2$ 轉 $\alpha$」。

> 推論（不是逐字稿內容）：用第 2 集的記號也能直接寫出來。$U$ 對應單位四元數 $t$，$\Phi(U)$ 就是 $q\mapsto t^{-1}qt$ 在基底 $i, j, k$ 下的矩陣（或 $tqt^{-1}$，看慣例）。兩種構造都是「用單位元素共軛一個 3 維空間」。

## 4. 例 3、4：U(n)、SO(n)；SL(n, ℝ)

**例 3**　[▶ 35:04](https://youtu.be/0Jzh0ZtTqAY?t=2104)

$$
\widetilde{U(n)} = \mathbb{R}\times SU(n),\qquad\Phi(\theta, U) = e^{i\theta}U.
$$

【課堂討論】[▶ 36:16](https://youtu.be/0Jzh0ZtTqAY?t=2176) 老師：$O(n)$ 行列式 $\pm 1$、$SO(n)$ 行列式 $1$；複數的 $U(n)$ 行列式是任意**模長 1** 的複數（由 $U^*U = I$ 得 $|\det U|^2 = 1$）。乘上 $e^{i\theta}$ 就能湊出任意行列式。
- [▶ 37:20](https://youtu.be/0Jzh0ZtTqAY?t=2240) 單連通：$\mathbb{R}$ 和 $SU(n)$ 都單連通，乘積也單連通。
- [▶ 37:53](https://youtu.be/0Jzh0ZtTqAY?t=2273) 李代數同構：維數上，$SU(n)$ 的 $\det = 1$ 少了一維，$\mathbb{R}$ 把它補回來。可以明確證明（Hall 習題 15）。

**例 4**　[▶ 38:25](https://youtu.be/0Jzh0ZtTqAY?t=2305) $SO(n)$ 的萬有覆蓋叫 **$\operatorname{Spin}(n)$**，是**雙覆蓋**。$\operatorname{Spin}(n)$ 裡取值的東西叫**旋量**（spinor）；旋量場就是在每一點附上一個 $\operatorname{Spin}(n)$ 的值。和 **Clifford 代數**有關。老師說也許可以另花一天講。

> 【課本補充】Hall p.81：
> - $n\ge 3$ 時 $SO(n)$ 的基本群有兩個元素，所以覆蓋是 2 對 1。
> - $\operatorname{Spin}(n)$ 可以用 $\mathbb{R}^n$ 上的 Clifford 代數的可逆元素構造（Bröcker–tom Dieck 第 I 章 §6），它是矩陣李群。
> - 特例：$\operatorname{Spin}(3)\cong SU(2)$、$\operatorname{Spin}(4)\cong SU(2)\times SU(2)$（對照第 6 集的 $SU(2)\times SU(2)\to SO(4)$）。
> - 緊緻矩陣李群的萬有覆蓋**一定**還是矩陣李群。

**$SL(n, \mathbb{R})$**　[▶ 40:11](https://youtu.be/0Jzh0ZtTqAY?t=2411) 【口頭】老師在 Math StackExchange 找到的回答（他歸功給 Neil）：
- $SL(n, \mathbb{R})$ 同胚於 $SO(n)\times\mathbb{R}^k$。
- 所以基本群：$n\ge 3$ 是 $\mathbb{Z}_2$，$n = 2$ 是 $\mathbb{Z}$。
- 萬有覆蓋：$n\ge 3$ 是雙覆蓋，$n = 2$ 是無限循環覆蓋。
- [▶ 41:21](https://youtu.be/0Jzh0ZtTqAY?t=2481) 「它是什麼群？它就是 $SL(n, \mathbb{R})$ 的萬有覆蓋。**刻畫它的就是這些性質**（單連通、同樣的李代數、有覆蓋同態），這才是你該怎麼想它。」

## 5. 子群與子代數

### 5.1 反方向不一定成立

[▶ 41:54](https://youtu.be/0Jzh0ZtTqAY?t=2514) Hall §3.8 開頭的問題：$H\subseteq G$ 都是矩陣李群，$\mathfrak h$ 當然是 $\mathfrak g$ 的子代數（把包含映射微分）。**反過來呢？** 給 $\mathfrak g$ 的子代數 $\mathfrak h$，一定有矩陣李群 $H\subseteq G$ 以 $\mathfrak h$ 為李代數嗎？

[▶ 45:08](https://youtu.be/0Jzh0ZtTqAY?t=2708) **反例**（$a$ 無理數，$G = GL(2; \mathbb{C})$）：

$$
\mathfrak h = \left\{\begin{pmatrix}it & 0\\ 0 & ita\end{pmatrix} : t\in\mathbb{R}\right\}.
$$

[▶ 46:14](https://youtu.be/0Jzh0ZtTqAY?t=2774) $\mathfrak{gl}(2; \mathbb{C})$ 是所有 $2\times 2$ 複數矩陣。對角矩陣互相交換，交換子是 0，所以 $\mathfrak h$ 是（1 維）子代數。

[▶ 46:49](https://youtu.be/0Jzh0ZtTqAY?t=2809) 如果有 $H$，它要包含所有 $e^X$，$X\in\mathfrak h$：

$$
\begin{pmatrix}e^{it} & 0\\ 0 & e^{ita}\end{pmatrix}
$$

——就是第 9 集的「環面上的無理直線」。

[▶ 47:58](https://youtu.be/0Jzh0ZtTqAY?t=2878) $H$ 要是閉的，就得包含它的**閉包**。$a$ 無理，這條線稠密地纏繞整個環面，[▶ 48:36](https://youtu.be/0Jzh0ZtTqAY?t=2916) 閉包是整個 $\{\operatorname{diag}(e^{i\theta}, e^{i\varphi})\}$，**二維**，李代數也是二維。但 $\mathfrak h$ 是一維的，矛盾。

### 5.2 放寬定義：連通李子群

【口頭】[▶ 49:11](https://youtu.be/0Jzh0ZtTqAY?t=2951) 兩種哲學態度：
- 「我們的李子群定義很蠢，在正確的定義下這個對應應該成立。」
- 「我們的定義沒問題，只是需要**新的、更弱的**子群概念。」

Hall 走第二條路。

[▶ 49:45](https://youtu.be/0Jzh0ZtTqAY?t=2985) **任意子群的李代數**（Hall）：$H$ 是 $GL(n; \mathbb{C})$ 的**任意**子群（不要求閉），定義

$$
\mathfrak h = \{\,X : e^{tX}\in H\ \ \forall t\in\mathbb{R}\,\}.
$$

【口頭】[▶ 51:34](https://youtu.be/0Jzh0ZtTqAY?t=3094) 「又是那個狡猾的定義：指數化回到群裡就是李代數。」

[▶ 52:10](https://youtu.be/0Jzh0ZtTqAY?t=3130)

> **Definition 3.12（Hall p.82）**　$G$ 是矩陣李群。$H\subseteq G$ 是**連通李子群**（connected Lie subgroup），如果
> 1. $H$ 是 $G$ 的子群（一般意義）；
> 2. $H$ 的李代數 $\mathfrak h$ 是 $\mathfrak g$ 的子空間；
> 3. $H$ 的每個元素都能寫成 $e^{X_1}e^{X_2}\cdots e^{X_m}$，$X_j\in\mathfrak h$。

【口頭】[▶ 52:49](https://youtu.be/0Jzh0ZtTqAY?t=3169) 「（$SU(2)\to SO(3)$ 那件事）困擾了我一整學期，我現在感覺好多了。等我能明確寫出公式才會真的好。」

[▶ 55:13](https://youtu.be/0Jzh0ZtTqAY?t=3313) **命題**：連通李子群是**路徑連通**的。（解釋了名字。）

[▶ 55:48](https://youtu.be/0Jzh0ZtTqAY?t=3348) **Proposition 3.14（Hall p.83）**：連通李子群的 $\mathfrak h$ 不只是子空間，還對括號封閉，是**子代數**。

【口頭】[▶ 57:06](https://youtu.be/0Jzh0ZtTqAY?t=3426) 證明用到微分（「讓我開心」），還有那個「拓樸閉」的論證（第 12 集）。

> 【課本補充】Hall p.83 證明：$A\in H$、$Y\in\mathfrak h$ ⟹ $e^{tAYA^{-1}} = Ae^{tY}A^{-1}\in H$，所以 $AYA^{-1}\in\mathfrak h$。再取 $A = e^{tX}$，$\mathfrak h$ 是子空間所以是閉集，$[X, Y] = \lim_{h\to0}\frac{e^{hX}Ye^{-hX} - Y}{h}\in\mathfrak h$。

### 5.3 主要定理

[▶ 57:06](https://youtu.be/0Jzh0ZtTqAY?t=3426)

> **Theorem 3.15（Hall p.83）**　$G$ 是矩陣李群，$\mathfrak h$ 是 $\mathfrak g$ 的李子代數。則存在**唯一**的連通李子群 $H\subseteq G$，其李代數是 $\mathfrak h$。$H$ 恰好由有限個 $\mathfrak h$ 元素的指數乘積組成：
> $$H = \{\,e^{X_1}e^{X_2}\cdots e^{X_m} : X_j\in\mathfrak h\,\}.$$

[▶ 59:05](https://youtu.be/0Jzh0ZtTqAY?t=3545) 【口頭】「我們發明了合適的、比較弱的子群概念，好讓這個定理成立。問題出在矩陣李群『閉』這個要求太貪心了；要允許更奇特的子群，才有空間讓對應成立。」

[▶ 59:40](https://youtu.be/0Jzh0ZtTqAY?t=3580) **Theorem 3.17（Hall p.85）**：$H$ 是 $G$ 的連通李子群，則 $H$ 可以賦予李群結構，使包含映射 $H\hookrightarrow G$ 是李群同態。影片在這裡斷掉。

> 【課本補充】Hall p.85：
> **Theorem 3.18**　每個有限維實李代數都同構於某個李群的李代數。（Thm. 3.17 ＋ Ado 定理。）
> 對照：上面 $\mathfrak h$ 的例子，對應的連通李子群就是那條無理直線本身——它不是閉的，所以不是矩陣李群，但它是連通李子群。

## 6. 一頁速查表

| 敘述 | 關鍵一步 |
|---|---|
| 萬有覆蓋：單連通 $\tilde G$ ＋ $\Phi:\tilde G\to G$，$\phi$ 是同構 | 唯一（標準同構意義下） |
| $\tilde{S^1} = \mathbb{R}$，$\theta\mapsto e^{i\theta}$ | $S^1$ 不單連通 |
| $\widetilde{SO(3)} = SU(2)$ | $\Phi_U(A) = UAU^{-1}$ 在 Hermitian 跡零矩陣上 |
| $\langle A, B\rangle = \frac12\operatorname{tr}(AB)$，$A_1, A_2, A_3$ 正交規範 | $A_k^2 = I$、$A_1A_2 = -iA_3$ |
| $\Phi_U$ 保持內積 | 跡的循環性 |
| $\pm U$ 給同一個旋轉 | $(-U)A(-U)^{-1} = UAU^{-1}$ |
| $\widetilde{U(n)} = \mathbb{R}\times SU(n)$，$(\theta, U)\mapsto e^{i\theta}U$ | |
| $\widetilde{SO(n)} = \operatorname{Spin}(n)$，雙覆蓋（$n\ge 3$） | $\operatorname{Spin}(3) = SU(2)$ |
| $\widetilde{SL(n, \mathbb{R})}$ 不是矩陣李群 | |
| 子代數 ↛ 閉子群 | 環面上的無理直線 |
| 子代數 ↔ 唯一的連通李子群 | $H = \{e^{X_1}\cdots e^{X_m}\}$ |

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Thm. 3.7（單連通 ⟹ 李代數同態升成群同態） | 下一集：收尾 |
| 表示論 | Hall 第 4 章以後（本課程不講） |
| 子群、商、齊性空間 | May 2：群軌道與齊性空間 |

---

## 附：本集一句話總結

> **每個連通李群都有唯一的萬有覆蓋：李代數相同的單連通群，例如 $\mathbb{R}\to S^1$、$SU(2)\to SO(3)$（用 $U$ 共軛 Hermitian 跡零矩陣就是學期初找不到的那個明確映射）；而反過來從子代數找子群時，必須把「閉」放寬成「連通李子群」，才能得到子代數與子群的一一對應。**
