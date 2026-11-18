---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 33
lecture: Lecture 33
date: 2023-04-26
video: https://youtu.be/DQ2DxDz8bog （part 1）、https://youtu.be/ftNfc6Fx5V8 （part 2，約 3 分鐘）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §7.1–7.3（書頁 351–369，PDF 頁 370–388）
---

# 第 33 集 · 古典力學回顧與量子力學的基本假設 [▶ 影片](https://youtu.be/DQ2DxDz8bog)

← 上一集：[32-fourier-transform-distributions](32-fourier-transform-distributions.md) ｜ [總目錄](README.md) ｜ 下一集：[34-quantum-uncertainty-expectation](34-quantum-uncertainty-expectation.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 33 集
> **講者**：James Cook（⚠️ 待確認，見第 01 集）
> **來源**：YouTube 自動字幕逐字稿（part 1 約 59:50；part 2 約 2:40）＋ Debnath & Mikusiński §7.1–7.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Lagrangian 與 Euler–Lagrange 方程](#1-lagrangian-與-eulerlagrange-方程)
- [2. 廣義動量：兩個例子](#2-廣義動量兩個例子)
- [3. Hamiltonian 與 Hamilton 方程](#3-hamiltonian-與-hamilton-方程)
- [4. 【Q&A】古典力學與量子力學](#4-qa古典力學與量子力學)
- [5. Poisson 括號](#5-poisson-括號)
- [6. 為什麼需要量子力學：Rutherford 原子](#6-為什麼需要量子力學rutherford-原子)
- [7. 假設 I：狀態向量](#7-假設-i狀態向量)
- [8. 假設 II：可觀測量是 Hermitian 算子](#8-假設-ii可觀測量是-hermitian-算子)
- [9. 不對易與同時測量](#9-不對易與同時測量)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

進入第 7 章「量子力學基礎」。目標：用 Hilbert 空間的算子理論來講量子力學的基本概念和假設。[▶ 00:32](https://youtu.be/DQ2DxDz8bog?t=32)

講者先唸了章首兩段引文：[▶ 01:06](https://youtu.be/DQ2DxDz8bog?t=66)
- **Hilbert**：數學是理論與實踐、思想與觀察之間的橋樑；引 Galileo「只有學會自然的語言才能理解自然，而那語言是數學」。
- **Dirac**：研究者用數學表達自然定律時，應該主要追求數學之美；簡單性次之，兩者衝突時美優先。

| 主題 | 課本位置 |
|---|---|
| Lagrangian、Euler–Lagrange、廣義動量 | §7.2，(7.21)–(7.26)，pp. 352–357 |
| Hamiltonian、Hamilton 方程 | (7.27)–(7.33)，pp. 357–359 |
| Poisson 括號 | (7.36)–(7.40)，pp. 361–362 |
| Rutherford 原子的困難 | §7.3 開頭，pp. 363–364 |
| 假設 I、II | Postulate I–II，(7.46)–(7.56)，pp. 365–369 |

【口頭】講者說要先看 §7.2 古典力學的重點，「這樣才能欣賞量子力學發生了什麼」。

---

## 1. Lagrangian 與 Euler–Lagrange 方程

[▶ 03:28](https://youtu.be/DQ2DxDz8bog?t=208)

**Lagrangian**：動能減位能，
$$L=T-V .$$
講者強調它是「相空間」（phase space）上的函數：同時是位置 $x_i$ 和速度 $\dot x_i$ 的函數（下標 $i$ 標記粒子／座標）。

**Euler–Lagrange 方程**（運動方程）：[▶ 04:03](https://youtu.be/DQ2DxDz8bog?t=243)
$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot x_i}\right)=\frac{\partial L}{\partial x_i} .$$

【口頭】它重現牛頓第二定律，也重現力矩方程，還有一些普通物理裡沒有名字的一般方程。它在任何座標系都成立，所以最好用**廣義座標**（generalized coordinates）$q_i$ 代替 $x_i$。[▶ 04:37](https://youtu.be/DQ2DxDz8bog?t=277)

**廣義動量與廣義力**：[▶ 05:45](https://youtu.be/DQ2DxDz8bog?t=345)
$$p_j=\frac{\partial L}{\partial\dot q_j},\qquad F_j=\frac{\partial L}{\partial q_j} .$$
於是 Euler–Lagrange 方程就是
$$\frac{dp_j}{dt}=F_j ,$$
正是動量形式的牛頓第二定律。課本說 $p_j$ 和 $q_j$ 叫**共軛變數**（conjugate variables）。

【口頭】點是時間導數，這是牛頓的記號。「Leibniz 在微積分記號戰爭中贏了牛頓」，但物理裡牛頓的點還活著。[▶ 07:33](https://youtu.be/DQ2DxDz8bog?t=453)

---

## 2. 廣義動量：兩個例子

[▶ 06:53](https://youtu.be/DQ2DxDz8bog?t=413)

**例 1（直角座標）**：$L=\frac12m\left(\dot x^2+\dot y^2\right)$。
$$\frac{\partial L}{\partial\dot x}=m\dot x=p_x,\qquad\frac{\partial L}{\partial\dot y}=m\dot y=p_y .$$
就是一般的線動量。

**例 2（極座標）**：$L=\frac12m\left(\dot r^2+r^2\dot\theta^2\right)$。（字幕只聽到「$\frac12m\dot r^2$ 加 $r$…」，第二項依講者接著算出的 $mr^2\dot\theta$ 補上。）[▶ 08:07](https://youtu.be/DQ2DxDz8bog?t=487)
$$\frac{\partial L}{\partial\dot r}=m\dot r,\qquad\frac{\partial L}{\partial\dot\theta}=mr^2\dot\theta .$$
- 第一個是徑向的線動量（$r$ 是長度座標）。
- 第二個是 $mr^2\omega=I\omega$，就是**角動量**。

【口頭】Lagrangian 觀點把普通古典力學課分開講的概念統一起來，給出動量的一般定義：Lagrangian 對第 $j$ 個座標導數的偏導數。[▶ 08:40](https://youtu.be/DQ2DxDz8bog?t=520)

【口頭】相空間把 $q_i$ 和 $\dot q_i$ 當成**獨立**變數，這背後有有趣的數學（最終會引到 jet space）。三維中一個粒子的相空間是 6 維；其中只有後 3 個座標真的是前 3 個的時間導數的曲線，才對應真實運動。[▶ 09:49](https://youtu.be/DQ2DxDz8bog?t=589)

---

## 3. Hamiltonian 與 Hamilton 方程

[▶ 10:54](https://youtu.be/DQ2DxDz8bog?t=654)

**Hamiltonian**：位置和**動量**的函數（把 $\dot q_i$ 換掉）：
$$H(p,q)=\sum_jp_j\dot q_j-L .\tag{7.27}$$
課本之後推出 $H=T+V$（總能量）。

**最簡單的例子**：[▶ 12:06](https://youtu.be/DQ2DxDz8bog?t=726) 動能在 Lagrangian 裡寫成 $\frac12m\dot x^2$；在 Hamiltonian 裡用 $p_x=m\dot x$ 改寫成
$$T=\frac{p_x^2}{2m} .$$

**Hamilton 方程**：講者在黑板上推（中間掉了一個負號，看課本後補回）：[▶ 14:19](https://youtu.be/DQ2DxDz8bog?t=859)
$$\dot q_j=\frac{\partial H}{\partial p_j},\qquad\dot p_j=-\frac{\partial H}{\partial q_j} .\tag{7.32a, 7.33b}$$

【課本補充】推導的關鍵一步（pp. 358–359）：
1. $H$ 是 $p_j,q_j,t$ 的函數，所以 $dH=\sum\frac{\partial H}{\partial p_j}dp_j+\sum\frac{\partial H}{\partial q_j}dq_j+\frac{\partial H}{\partial t}dt$。
2. 直接對 (7.27) 取微分：$dH=\sum p_j\,d\dot q_j+\sum\dot q_j\,dp_j-\sum\frac{\partial L}{\partial q_j}dq_j-\sum\frac{\partial L}{\partial\dot q_j}d\dot q_j-\frac{\partial L}{\partial t}dt$。
3. 因為 $p_j=\frac{\partial L}{\partial\dot q_j}$，含 $d\dot q_j$ 的兩項抵消：$dH=\sum\dot q_j\,dp_j-\sum\frac{\partial L}{\partial q_j}dq_j-\frac{\partial L}{\partial t}dt$。
4. 比較係數：$\dot q_j=\frac{\partial H}{\partial p_j}$，$\frac{\partial H}{\partial q_j}=-\frac{\partial L}{\partial q_j}=-\dot p_j$（最後一步用 Euler–Lagrange 方程 $\dot p_j=\frac{\partial L}{\partial q_j}$）。

【口頭】講者說這裡「把 $q$ 和 $\dot q$、$p$ 和 $q$ 都當成獨立」的做法，大學時讓他抓狂，現在還是；要好好教的話他得「好好清算一番」。[▶ 16:41](https://youtu.be/DQ2DxDz8bog?t=1001)

【口頭】做理論物理至今有兩種選擇：Hamiltonian 形式或 Lagrangian 形式。兩者相關又不同，「我們兩個都需要」。[▶ 18:27](https://youtu.be/DQ2DxDz8bog?t=1107)

---

## 4. 【Q&A】古典力學與量子力學

**Q：Hamiltonian 不是只有在某些條件下才等於總能量嗎？**[▶ 13:12](https://youtu.be/DQ2DxDz8bog?t=792)
講者：對。這牽涉到約束、完整（holonomic）與非完整約束等更大的討論，他「很遺憾沒準備好」在這裡談。課本 p. 359 有 $H=T+V$ 的推導。後來學生又補充：在量子力學裡 Hamiltonian 算子總是動能加位能。[▶ 19:11](https://youtu.be/DQ2DxDz8bog?t=1151)

【課本補充】課本 p. 359 的條件：$L$（因而 $H$）不顯含時間 $t$ 時，$\frac{dH}{dt}=0$（能量守恆）；再用動能是 $\dot q_j$ 的二次齊次式，得 $\sum p_j\dot q_j=2T$，所以 $H=2T-(T-V)=T+V$。

【口頭】為什麼要看古典力學：寫下量子力學的那批人都深受古典力學訓練，懂得比我們今天深得多；量子力學對他們來說是已知理論物理的自然延伸。[▶ 19:46](https://youtu.be/DQ2DxDz8bog?t=1186)

**Q：古典力學「解決了」嗎？**[▶ 20:32](https://youtu.be/DQ2DxDz8bog?t=1232)
講者：古典力學至今仍有未解的難題，但那不是理論的失敗。配上萬有引力，它預測了太陽系絕大多數軌道運動，只差像水星近日點進動這類小地方（後來由廣義相對論解釋）；時間膨脹則完全漏掉。古典力學現在仍然要教：「古典力學之於物理系，就像實分析之於數學系。」

---

## 5. Poisson 括號

[▶ 22:11](https://youtu.be/DQ2DxDz8bog?t=1331)

任一「正則函數」$F(p_i,q_i,t)$ 對時間的導數：用連鎖律，再代入 Hamilton 方程（$\dot q_i=\frac{\partial H}{\partial p_i}$，$\dot p_i=-\frac{\partial H}{\partial q_i}$）：
$$\frac{dF}{dt}=\sum_{i=1}^{3n}\left(\frac{\partial F}{\partial q_i}\dot q_i+\frac{\partial F}{\partial p_i}\dot p_i\right)+\frac{\partial F}{\partial t}
=\sum_{i=1}^{3n}\left(\frac{\partial F}{\partial q_i}\frac{\partial H}{\partial p_i}-\frac{\partial F}{\partial p_i}\frac{\partial H}{\partial q_i}\right)+\frac{\partial F}{\partial t} .$$

**Poisson 括號**（Poisson bracket）定義為括號裡那一項：[▶ 24:35](https://youtu.be/DQ2DxDz8bog?t=1475)
$$\{F,H\}=\sum_{i=1}^{3n}\left(\frac{\partial F}{\partial q_i}\frac{\partial H}{\partial p_i}-\frac{\partial F}{\partial p_i}\frac{\partial H}{\partial q_i}\right),\qquad\frac{dF}{dt}=\{F,H\}+\frac{\partial F}{\partial t} .\tag{7.36}$$
（$3n$：$n$ 個粒子，每個 3 個座標。$\frac{\partial F}{\partial t}$ 不屬於括號。）

【口頭】這個括號是個奇妙的代數東西，把 Hamilton 方程「編織」進去。轉到量子力學時，Poisson 括號會變成**對易子**（commutator）。[▶ 25:46](https://youtu.be/DQ2DxDz8bog?t=1546)

若 $F$ 不顯含 $t$：$\frac{dF}{dt}=\{F,H\}$。【課本補充】若再有 $\{F,H\}=0$，$F$ 就是運動常數（守恆量）。

**基本 Poisson 括號**：[▶ 26:19](https://youtu.be/DQ2DxDz8bog?t=1579)
$$\{q_i,p_j\}=\delta_{ij},\qquad\{q_i,q_j\}=\{p_i,p_j\}=0 ,$$
$$\{L_i,L_j\}=L_k\ (i,j,k=x,y,z\text{ 循環}),\qquad\{L_i,L^2\}=0,\quad L^2=L_x^2+L_y^2+L_z^2 .$$

【口頭】講者笑說課本混用 $x,y,z$ 和 $i,j$ 記號，「像回到家，回到物理真好」。[▶ 27:32](https://youtu.be/DQ2DxDz8bog?t=1652)

**課堂算例**（作業有幾題 Poisson 括號）：[▶ 28:05](https://youtu.be/DQ2DxDz8bog?t=1685) 一維、一個粒子，算 $\{q,p\}$。講者一度困惑：「$H$ 不是 Hamiltonian 嗎？怎麼能算任意兩個東西的括號？」看清楚後明白定義裡的 $H$ 可以是**任意**函數。[▶ 29:29](https://youtu.be/DQ2DxDz8bog?t=1769) 取 $F=q$、$H=p$：
$$\{q,p\}=\frac{\partial q}{\partial q}\frac{\partial p}{\partial p}-\frac{\partial q}{\partial p}\frac{\partial p}{\partial q}=1\cdot1-0\cdot0=1 .$$
講者說「答案是 1，但我還是有點困惑……我的困惑不必是你們的困惑」。[▶ 31:58](https://youtu.be/DQ2DxDz8bog?t=1918)

以下**不是逐字稿內容**，是依 (7.36) 推論的：若取 $H$ 真的是 Hamiltonian $H=\frac{p^2}{2m}$，則
$$\{q,H\}=\frac{\partial q}{\partial q}\frac{\partial H}{\partial p}-0=\frac pm=\dot q,\qquad\{p,H\}=0-\frac{\partial p}{\partial p}\frac{\partial H}{\partial q}=0=\dot p .$$
這正是自由粒子的 Hamilton 方程——也就是課本說「(7.37) 包含 Hamilton 方程（令 $F=p_i$ 或 $q_i$）」的意思。

---

## 6. 為什麼需要量子力學：Rutherford 原子

[▶ 33:00](https://youtu.be/DQ2DxDz8bog?t=1980)

導致量子力學的問題：黑體輻射無法解釋（講者補充光電效應也是），以及古典概念用在電子運動上的失敗，最明顯的是氫原子。

**Rutherford 模型**：帶負電的電子繞著很重、帶正電的原子核轉。

【Q&A】學生問：為什麼電子不會撞進核裡？月亮也不會撞進地球啊。[▶ 34:10](https://youtu.be/DQ2DxDz8bog?t=2050)
講者：電磁學告訴我們，**加速的帶電粒子會輻射**。繞核轉的電子一直在加速，應該一直輻射、損失能量，然後掉進核裡；但實際上沒有。[▶ 34:42](https://youtu.be/DQ2DxDz8bog?t=2082)
- 他的近代物理教授第一堂課就拿這個問題開場。
- 量子力學的答案基本上是「它就是不會」——「很令人不滿意」。能階是離散的，有一個最低能階，沒有更低的能量可以輻射過去。[▶ 35:48](https://youtu.be/DQ2DxDz8bog?t=2148)

課本的數字：電子應該在約 $10^{-10}$ 秒內和核合併、原子崩潰。所以 Rutherford 模型有兩個弱點：[▶ 36:57](https://youtu.be/DQ2DxDz8bog?t=2217)
1. 原子應該非常不穩定；
2. 應該輻射連續頻率的能量。

兩者都和實驗矛盾。量子力學最初的問題就是解釋原子、分子的穩定性，以及激發原子輻射的**離散**光譜。

---

## 7. 假設 I：狀態向量

[▶ 37:32](https://youtu.be/DQ2DxDz8bog?t=2252)

古典力學把系統狀態等同於可觀測量（位置、動量）的值；量子力學則清楚區分**狀態**和**可觀測量**。

**Postulate I（狀態向量）**：[▶ 38:05](https://youtu.be/DQ2DxDz8bog?t=2285)
- 每個量子系統對應一個複數域上的**可分** Hilbert 空間。
- 系統的狀態由空間中一個**非零向量**表示；它的每個非零純量倍代表同一個狀態。
- 時刻 $t$ 的狀態向量記為 $\Psi(x,t)$，系統在時刻 $t$ 的（幾乎）所有資訊都可以從它得到。

【口頭】講者覺得課本第一句「每個狀態對應一個可分 Hilbert 空間」怪怪的，應該是「對應可分 Hilbert 空間中的一個**向量**」；下一句就說清楚了。[▶ 38:40](https://youtu.be/DQ2DxDz8bog?t=2320)

**Dirac 記號**：狀態向量常寫成小寫 $\psi(x)$，
$$\psi(x)=\langle x|\psi\rangle,\qquad\overline{\psi(x)}=\langle\psi|x\rangle .\tag{7.46, 7.47}$$
【口頭】講者抱怨課本沒解釋大寫 $\Psi$ 和小寫 $\psi$ 的差別，「這一步有點滑頭」。[▶ 39:49](https://youtu.be/DQ2DxDz8bog?t=2389)

**歸一化**：乘非零純量不改變物理，所以可以要求[▶ 40:21](https://youtu.be/DQ2DxDz8bog?t=2421)
$$\int\overline{\psi(x)}\,\psi(x)\,dx=\int|\psi(x)|^2dx=1,\qquad\text{簡寫 }\langle\psi|\psi\rangle=1 .$$

**內積**：
$$\langle\varphi|\psi\rangle=\int\overline{\varphi(x)}\,\psi(x)\,dx=\int\langle\varphi|x\rangle\langle x|\psi\rangle\,dx ,\qquad\langle\varphi|\psi\rangle=\overline{\langle\psi|\varphi\rangle} .$$

【口頭】講者把 $\langle F,\varphi\rangle=\int f\varphi$（上次的分佈記號，對正則分佈）拿來比，發現順序不一樣：分佈是 $F$ 在前、$\varphi$ 在後；這裡的 $x$ 卻是「後者為先、先者為後」——「這不是什麼深刻的評論」。[▶ 41:41](https://youtu.be/DQ2DxDz8bog?t=2501) 以下**不是逐字稿內容**，是依兩個定義對照推論的：差別在於這裡的內積是**第一個**變數取共軛（物理慣例），而課本第 3 章起的內積 $\langle x,y\rangle$ 是**第二個**變數取共軛；所以 $\langle\varphi|\psi\rangle$ 對應第 3 章的 $\langle\psi,\varphi\rangle$。

**正交與展開**：[▶ 44:42](https://youtu.be/DQ2DxDz8bog?t=2682)
- $\langle\varphi|\psi\rangle=0$ 叫正交；$\langle\psi_i|\psi_j\rangle=\delta_{ij}$ 叫正規正交。
- 任意狀態可用**完備**正規正交組展開：
$$|\psi\rangle=\sum_ic_i|\psi_i\rangle,\qquad c_i=\langle\psi_i|\psi\rangle .\tag{7.54, 7.55}$$

講者驗算係數公式：用 $\langle\psi_j|\cdot\rangle$ 作用在兩邊、利用線性，[▶ 48:12](https://youtu.be/DQ2DxDz8bog?t=2892)
$$\langle\psi_j|\psi\rangle=\sum_ic_i\langle\psi_j|\psi_i\rangle=\sum_ic_i\delta_{ji}=c_j .$$
【口頭】這需要內積結構：對第二個位置可以直接把純量提出來（不用共軛）、而且可加。學生補充：右邊的 ket 是狀態向量，(7.54) 的前提是正規正交組是**完備**的（第 22 集的 Parseval／基底）。[▶ 50:52](https://youtu.be/DQ2DxDz8bog?t=3052)

課本說這個假設包含**疊加原理**。空間維度＝正規正交組的元素個數；有限維就是有限和，無窮維就是無窮級數，要談收斂。

**時間的角色**：[▶ 46:29](https://youtu.be/DQ2DxDz8bog?t=2789)
- 古典力學：狀態由 $q(t)$、$p(t)$ 兩組實數完全描述。
- 量子力學：$\Psi(x,t)$ 作為 Hilbert 空間的向量**只是 $x$ 的函數**，$t$ 只是參數。$\Psi(x,t_1)$ 和 $\Psi(x,t_2)$ 是空間中兩個不同的向量。$\Psi$ 也叫**狀態函數**或**波函數**（wave function）。

---

## 8. 假設 II：可觀測量是 Hermitian 算子

[▶ 51:23](https://youtu.be/DQ2DxDz8bog?t=3083)

**古典**：可觀測量就是動力學變數（位置、動量及其函數，如角動量、能量）。測量得到一個實數，而且默認測量不會明顯干擾系統——所以「可觀測量的數學表示」和「它的值」沒有差別。

**Postulate II（可觀測量算子與它們的值）**：[▶ 52:32](https://youtu.be/DQ2DxDz8bog?t=3152)
- (a) 每個物理可觀測量對應 Hilbert 空間中一個**線性 Hermitian 算子** $\hat A$，它有一組**完備正規正交本徵向量** $\{\psi_n\}$，本徵值 $\{\lambda_n\}$：
$$\hat A\psi_n=\lambda_n\psi_n .\tag{7.56}$$
  反過來，每個這樣的算子都對應某個可觀測量。
- (b) 可觀測量**唯一可能的值**就是這些本徵值。

【口頭】(b) 最終會「拯救 Rutherford 原子免於必然的崩潰」。[▶ 53:07](https://youtu.be/DQ2DxDz8bog?t=3187)

【口頭】課本說可觀測量算子「通常」滿足 Hilbert 空間算子理論的規則。講者：「通常——這是個閃躲的詞。你的註腳在哪？告訴我什麼時候不成立。」[▶ 54:16](https://youtu.be/DQ2DxDz8bog?t=3256)

**推論**（課本列的）：[▶ 54:50](https://youtu.be/DQ2DxDz8bog?t=3290)
1. Hermitian ⟹ 本徵值是實數（第 26–27 集）。這對應「量到的是實數」。
2. 本徵值的寫法暗示它們是離散的，所以某些可觀測量可以被「量子化」——這正符合分子的離散光譜。【課本補充】但課本也說本徵值可以是離散、連續或兩者混合，看算子而定。
3. **最深刻的差別**：兩個古典變數一定可交換；兩個可觀測量算子一般**不可交換**，對易子 $\hat A\hat B-\hat B\hat A$ 不一定是 0。

---

## 9. 不對易與同時測量

[▶ 55:24](https://youtu.be/DQ2DxDz8bog?t=3324)

課本的哲學：$\hat A\hat B\ne\hat B\hat A$ 表示「先量 $B$ 再量 $A$」和「先量 $A$ 再量 $B$」不一樣；非零的對易子對應兩次測量不可避免的干擾。量子理論中的測量會影響系統，可能無法同時測量兩個可觀測量，測一個可能改變另一個的值。這引向 Heisenberg 測不準原理（下次）。

【口頭】講者的重點：[▶ 57:03](https://youtu.be/DQ2DxDz8bog?t=3423)
$$\left[\hat A,\hat B\right]=0\quad\Longrightarrow\quad\text{有共同的本徵向量（可同時對角化）},$$
所以要同時量兩個可觀測量，它們的對易子必須是 0。

講者舉的例子（說「還沒有引入」動量和位置算子）：[▶ 58:14](https://youtu.be/DQ2DxDz8bog?t=3494)
- $\left[\hat x,\hat p\right]=i\hbar$（他一開始寫反成 $[\hat p,\hat x]$，又改正）⟹ 不能同時知道位置和動量。
- $\left[\hat L^2,\hat L_z\right]=0$ ⟹ 可以同時量總角動量平方和 $z$ 分量。
- $\left[\hat L_x,\hat L_y\right]$ 字幕作「等於 $L_z$」⟹ 不能同時量 $x$、$y$ 分量。

以下**不是逐字稿內容**，是依「Poisson 括號 → 對易子」的對應推論的：古典是 $\{L_x,L_y\}=L_z$；量子版通常寫成 $\left[\hat L_x,\hat L_y\right]=i\hbar\hat L_z$，多一個 $i\hbar$，和 $\{q,p\}=1\ \to\ [\hat x,\hat p]=i\hbar$ 是同一個規則。講者口頭可能省略了 $i\hbar$。

【口頭】理解量子系統的遊戲，就是找一組**可同時對角化**的可觀測量。最重要的是能量：Hamiltonian 的能量本徵態極為重要；和 Hamiltonian 對易的算子可以和它同時對角化，於是它們的本徵態也是能量本徵態，可以同時量能量和那個可觀測量。[▶ part 2 00:02](https://youtu.be/ftNfc6Fx5V8?t=2)

**預告**：下次講這些從哪裡來，希望能談 Schrödinger 表象和 Heisenberg 表象。[▶ part 2 00:35](https://youtu.be/ftNfc6Fx5V8?t=35)

【口頭】課後閒聊：講者和學生都說當年討厭近代物理，他至今仍有概念上的障礙。他鼓勵大家好好讀這一章：「它會讓你對量子力學的理解比讀量子力學課本還深。」[▶ part 2 02:38](https://youtu.be/ftNfc6Fx5V8?t=158)

---

## 10. 一頁速查表

| 項目 | 公式／內容 | 關鍵一步 |
|---|---|---|
| Lagrangian | $L=T-V$，相空間 $(q,\dot q)$ 上的函數 | |
| Euler–Lagrange | $\frac{d}{dt}\frac{\partial L}{\partial\dot q_j}=\frac{\partial L}{\partial q_j}$ | 即 $\dot p_j=F_j$ |
| 廣義動量 | $p_j=\partial L/\partial\dot q_j$ | 極座標：$m\dot r$、$mr^2\dot\theta$（角動量） |
| Hamiltonian | $H=\sum p_j\dot q_j-L$；常為 $T+V$ | $T=\frac{p^2}{2m}$ |
| Hamilton 方程 | $\dot q_j=\frac{\partial H}{\partial p_j}$，$\dot p_j=-\frac{\partial H}{\partial q_j}$ | 比較 $dH$ 兩種寫法的係數 |
| Poisson 括號 | $\{F,H\}=\sum\left(F_{q_i}H_{p_i}-F_{p_i}H_{q_i}\right)$ | $\dot F=\{F,H\}+\partial_tF$ |
| 基本括號 | $\{q_i,p_j\}=\delta_{ij}$；$\{L_x,L_y\}=L_z$；$\{L_i,L^2\}=0$ | 直接代定義 |
| 量子化對應 | Poisson 括號 → 對易子 | $\{q,p\}=1\to[\hat x,\hat p]=i\hbar$ |
| Rutherford 困難 | 加速電荷輻射 ⟹ 約 $10^{-10}$ s 崩潰、連續光譜 | 量子：離散能階、有最低能階 |
| 假設 I | 狀態＝可分 Hilbert 空間中的非零向量（差純量倍） | $\langle\psi|\psi\rangle=1$ |
| Dirac 記號 | $\psi(x)=\langle x|\psi\rangle$，$\langle\varphi|\psi\rangle=\int\bar\varphi\psi$ | 物理慣例：第一個變數取共軛 |
| 展開 | $|\psi\rangle=\sum c_i|\psi_i\rangle$，$c_i=\langle\psi_i|\psi\rangle$ | 需完備正規正交組 |
| 假設 II | 可觀測量＝Hermitian 算子，有完備正規正交本徵向量；值＝本徵值 | Hermitian ⟹ 實本徵值 |
| 同時測量 | $[\hat A,\hat B]=0$ ⟹ 共同本徵向量 | $[\hat x,\hat p]=i\hbar\ne0$ |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 對易子、$[\hat x,\hat p]=i\hbar$ | 第 34 集：Heisenberg 測不準原理 |
| 假設 II、本徵值 | 第 34 集：期望值、測量結果（Postulate V） |
| Hamiltonian | 第 34 集：Schrödinger 方程 |

---

## 附：本集一句話總結

> **古典力學用 Lagrangian／Hamiltonian 寫運動方程，Poisson 括號 $\{F,H\}$ 把它們全部打包；量子力學則把狀態變成可分 Hilbert 空間中的單位向量 $|\psi\rangle$、把可觀測量變成 Hermitian 算子（只能量到本徵值，所以能階是離散的），而 Poisson 括號變成對易子——不對易的兩個量（例如 $[\hat x,\hat p]=i\hbar$）不能同時量準。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-04-26 錄影逐字稿（YouTube 自動字幕，part 1 約 59:50、part 2 約 2:40）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §7.1–7.3 整理。*
