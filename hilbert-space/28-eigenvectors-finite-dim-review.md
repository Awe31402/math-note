---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 28
lecture: Lecture 28
date: 2023-04-05
video: https://youtu.be/4M--O74xj8Y （part 1）、https://youtu.be/AubT2T0_DGU （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.9，Corollary 4.9.9–Theorem 4.9.21（書頁 190–196，PDF 頁 209–215）
---

# 第 28 集 · 本徵向量（續）：自伴與么正算子、有限維旋轉複習 [▶ 影片](https://youtu.be/4M--O74xj8Y)

← 上一集：[27-eigenvectors-spectrum-resolvent](27-eigenvectors-spectrum-resolvent.md) ｜ [總目錄](README.md) ｜ 下一集：[29-spectral-theorem-bvp-wave](29-spectral-theorem-bvp-wave.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 28 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 6:52，自動字幕）＋ Debnath & Mikusiński §4.9
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 譜半徑 ≤ 範數](#1-譜半徑--範數)
- [2. 相似變換不改變本徵值](#2-相似變換不改變本徵值)
- [3. 自伴算子的本徵值是實數](#3-自伴算子的本徵值是實數)
- [4. 自伴：譜半徑 = 範數；正算子](#4-自伴譜半徑--範數正算子)
- [5. 么正算子的本徵值模為 1](#5-么正算子的本徵值模為-1)
- [6. 題外話：二維、三維旋轉的本徵值](#6-題外話二維三維旋轉的本徵值)
- [7. 不同本徵值的本徵向量正交](#7-不同本徵值的本徵向量正交)
- [8. 緊緻自伴算子](#8-緊緻自伴算子)
- [9. 用投影組出算子](#9-用投影組出算子)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $r(A)\le\|A\|$ | Corollary 4.9.9，p. 190 |
| 相似算子有相同本徵值 | Theorem 4.9.10，p. 190 |
| 自伴：實本徵值、$r(A)=\|A\|$；正算子 | Theorem 4.9.11–4.9.13，pp. 190–191 |
| 么正：$|\lambda|=1$；不同本徵值的本徵向量正交 | Theorem 4.9.14–4.9.15，pp. 191–192 |
| 緊緻自伴算子 | Theorem 4.9.16–4.9.19，pp. 192–193 |
| 投影的級數 | Theorem 4.9.21，pp. 194–195 |

---

## 1. 譜半徑 ≤ 範數

[▶ 00:01](https://youtu.be/4M--O74xj8Y?t=1)

複習上次：$\|A\|<|\lambda|$ ⟹ $(A-\lambda I)^{-1}$ 有界，可用 Neumann 級數寫出。

**譜半徑在有限維**【口頭】[▶ 03:07](https://youtu.be/4M--O74xj8Y?t=187)：有限維時一切簡單：特徵方程是 $n$ 次多項式，在複數上有 $n$ 個（可能重複的）根，就是本徵值。譜半徑就是**離原點最遠的本徵值的距離**。所有本徵值都在以原點為心、以譜半徑為半徑的圓盤裡——所以叫「半徑」。

**Corollary 4.9.9**：$r(A)\le\|A\|$。

【課堂討論】[▶ 05:37](https://youtu.be/4M--O74xj8Y?t=337) 講者說這應該是上次定理的推論，一時看不出來。學生提示：$\|A\|<|\lambda|$ 的 $\lambda$ 都在預解集裡。講者整理：若 $|\lambda|>\|A\|$，預解式存在且有界，所以 $\lambda\notin\sigma(A)$。因此譜裡每個點都滿足 $|\lambda|\le\|A\|$，上確界 $r(A)\le\|A\|$。

講者【口頭】[▶ 09:29](https://youtu.be/4M--O74xj8Y?t=569)：這有時很有用：算出算子的範數，就知道本徵值要往哪裡找——找模不超過它的數。

---

## 2. 相似變換不改變本徵值

[▶ 09:29](https://youtu.be/4M--O74xj8Y?t=569) 課本 Theorem 4.9.10。

**定理**：$T$ 是向量空間 $E$ 上的可逆算子，$A$ 是 $E$ 上的算子。則 $A$ 和 $TAT^{-1}$ 有相同的本徵值。

**證明**：

- 設 $Au=\lambda u$，$u\ne0$。$T$ 可逆，只把 0 送到 0，所以 $Tu\ne0$。
  $$TAT^{-1}(Tu)=TAu=T(\lambda u)=\lambda Tu.$$
  $\lambda$ 是 $TAT^{-1}$ 的本徵值，本徵向量 $Tu$。
- 反過來：設 $TAT^{-1}v=\lambda v$，$v\ne0$。講者：照前面的模式，猜 $T^{-1}v$ 是 $A$ 的本徵向量。
  $$A(T^{-1}v)=T^{-1}(TAT^{-1}v)=T^{-1}(\lambda v)=\lambda T^{-1}v.$$ ∎

講者【口頭】[▶ 13:54](https://youtu.be/4M--O74xj8Y?t=834)：$A$ 和 $TAT^{-1}$ 由**相似變換**相關（用可逆算子「共軛」）。他不確定無限維是否也用「相似變換」這個詞。有限維線代的大定理：任何矩陣在複數上都相似於它的 **Jordan 標準形**；在實數上也相似於某種實標準形。「我淺見認為每個有限維線代課都該講到這裡，但心靈固然願意，肉體卻軟弱——別怪學生。」

---

## 3. 自伴算子的本徵值是實數

[▶ 15:39](https://youtu.be/4M--O74xj8Y?t=939) 課本 Theorem 4.9.11。

**定理**：Hilbert 空間上自伴算子的所有本徵值都是實數。

（講者說今天又有兩塊黑板，「生活很高級」。）

**證明**：$T=T^*$，$Tu=\lambda u$，$u\ne0$。講者：「看 $\lambda\langle u,u\rangle$，魔法就會發生。」

$$\lambda\langle u,u\rangle=\langle\lambda u,u\rangle=\langle Tu,u\rangle=\langle u,T^*u\rangle=\langle u,Tu\rangle=\langle u,\lambda u\rangle=\bar\lambda\langle u,u\rangle.$$

$\langle u,u\rangle\ne0$，所以 $\lambda=\bar\lambda$，實數。∎

**物理的意義**【課堂討論】[▶ 20:04](https://youtu.be/4M--O74xj8Y?t=1204)：自伴在物理裡叫 **Hermitian**；我們要可觀測量是 Hermitian 算子，因為本徵值是實驗測到的值，必須是實數——「我們在物理裡是這樣告訴自己的」。

學生問：為什麼不能測量複數？講者：複數描述平面向量，我們一直在測「方向和大小」，「我隨時都在測複數」。他認為「物理可觀測量必須是實數」其實是物理的一個**慣例**；原則上可以用別種數學寫物理定律——有人寫過一整本用四元數的量子力學（他沒看過，以前的老師 Falk 博士會提到）。[▶ 20:36](https://youtu.be/4M--O74xj8Y?t=1236)

---

## 4. 自伴：譜半徑 = 範數；正算子

[▶ 21:41](https://youtu.be/4M--O74xj8Y?t=1301)

**Theorem 4.9.12**：$A$ 是 Hilbert 空間上的有界自伴算子，則 $r(A)=\|A\|$。

講者：所以不等式 $r(A)\le\|A\|$ 變成等式，而且「被達到」——其實不一定真有一個本徵值達到它，但至少有譜中的點以它為極限，因為譜半徑是用上確界定義的，「有一點迴旋空間」。

【課本補充】證明概要：由 Theorem 4.4.14，$\|A\|=\sup_{\|x\|=1}|\langle Ax,x\rangle|$，取 $\|x_n\|=1$ 使 $\langle Ax_n,x_n\rangle\to\lambda$，$|\lambda|=\|A\|$。則
$$\|Ax_n-\lambda x_n\|^2\le\|A\|^2-2\lambda\langle Ax_n,x_n\rangle+\lambda^2\to0.$$
若 $\lambda\in\rho(A)$，則 $1=\|x_n\|=\|(A-\lambda I)^{-1}(A-\lambda I)x_n\|\to0$，矛盾。所以 $\lambda\in\sigma(A)$。（這種 $\lambda$ 叫**近似本徵值**：有單位向量使 $\|Ax_n-\lambda x_n\|\to0$。）

**Theorem 4.9.13**：正算子的本徵值非負；嚴格正算子的本徵值為正。講者說這門課沒深入講正算子，有興趣可以看那節。

【課本補充】證明：$0\le\langle Ax,x\rangle=\lambda\|x\|^2$。

---

## 5. 么正算子的本徵值模為 1

[▶ 22:50](https://youtu.be/4M--O74xj8Y?t=1370) 課本 Theorem 4.9.14。

**定理**：Hilbert 空間上么正算子的本徵值都是模為 1 的複數。

【課堂討論】講者先問么正怎麼定義，以為是 $\langle Ux,Uy\rangle=\langle x,y\rangle$；課本是 $U^*U=UU^*=I$。講者說兩者等價；學生補充：取伴隨，有一個就有另一個。[▶ 23:47](https://youtu.be/4M--O74xj8Y?t=1427)

**證明**：$Ux=\lambda x$，$x\ne0$。講者先用 $x,y$ 兩個向量寫，然後說「我真笨，不需要 $y$」：

$$\langle x,x\rangle=\langle U^*Ux,x\rangle=\langle Ux,Ux\rangle=\langle\lambda x,\lambda x\rangle=\lambda\bar\lambda\langle x,x\rangle.$$

$\langle x,x\rangle=\|x\|^2\ne0$，所以 $|\lambda|^2=1$。本徵值在複平面的**單位圓**上。∎

講者：實的情形，么正算子就是**正交**算子；它不一定對稱（他一度說錯又改正）。正交算子的本徵值（若允許複數）也都在單位圓上。

---

## 6. 題外話：二維、三維旋轉的本徵值

【口頭】[▶ 27:15](https://youtu.be/4M--O74xj8Y?t=1635) 講者說「我強烈懷疑你們以前的線代課沒聽過這個」。

### 二維

$$R=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},\qquad R^TR=I,\ \det R=1.$$

滿足這兩個條件的矩陣構成 $SO(2)$。

**本徵值**[▶ 29:25](https://youtu.be/4M--O74xj8Y?t=1765)：$\det(\lambda I-R)=0$：

$$(\lambda-\cos\theta)^2+\sin^2\theta=0\ \Longrightarrow\ \lambda=\cos\theta\pm i\sin\theta=e^{\pm i\theta}.$$

（模都是 1，符合上一節。）但這要看情境：在**實**線代裡不允許複數本徵值，所以通常說「沒有本徵值，除非 $\theta=0$ 或 $\pi$」——那時 $R=\pm I$。

講者：想想幾何就很明顯：旋轉把 $v$ 轉到 $Rv$，長度相同但方向轉了；除非角度是 0 或 $\pi$，$Rv$ 不可能是 $v$ 的倍數。「我們可以做很花俏的數學，但從頭就很明顯。」[▶ 32:13](https://youtu.be/4M--O74xj8Y?t=1933)

### 三維

【課堂討論】[▶ 32:52](https://youtu.be/4M--O74xj8Y?t=1972) 學生猜：三維會有一個方向（例如 $z$ 方向）不動，平面上的部分在轉。講者畫圖：繞 $z$ 軸轉，

$$R=\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}.$$

$v=(v_1,v_2,0)+v_3e_3$，垂直的那一段不動，$Re_3=e_3$：**$e_3$ 是本徵值 1 的本徵向量**（軸）。另外兩個本徵值一定是複數：只有平行於 $z$ 軸的部分不動，其餘被轉。

**跡**[▶ 41:51](https://youtu.be/4M--O74xj8Y?t=2511)：

$$\operatorname{tr}R=2\cos\theta+1=\lambda_1+\lambda_2+\lambda_3.$$

$\lambda_1=1$，所以 $\lambda_2+\lambda_3=2\cos\theta$；而 $\lambda_2,\lambda_3=\cos\theta\pm i\sin\theta$。

**一般的三維旋轉**[▶ 43:53](https://youtu.be/4M--O74xj8Y?t=2633)：講者說只用 $R^TR=I$、$\det R=1$（$R\in SO(3)$）就能證明有本徵值 1 的本徵向量。他有點迷路（「抱歉，我在跟你們做作業」），最後整理出邏輯：

1. 本徵值的乘積是 $\det R=1$。
2. 把 $R$ 延拓到 $\mathbb{C}^3$，它在那裡是真正的么正算子，所以每個本徵值 $|\lambda|=1$（上一節）。
3. 實矩陣的複本徵值成共軛對。
4. 情況：$\{1,1,1\}$（$R=I$，任何非零向量都是本徵向量）；$\{1,-1,-1\}$（$R$ 是轉 $\pi$，二維那個例外情況）；否則兩個是共軛複數 $\lambda,\bar\lambda$（$\lambda\bar\lambda=1$），第三個就得是 1。
5. 不管哪種，1 都是本徵值，所以有**旋轉軸**。

在軸的垂直平面上選座標，矩陣就是上面的形式；所以對**任何**三維旋轉，

$$\operatorname{tr}R=1+2\cos\theta,$$

$\theta$ 是旋轉角。講者：「這是算三維旋轉角度的快速方法……如果我出研究所線代資格考，就會考這種題目。」[▶ 54:50](https://youtu.be/4M--O74xj8Y?t=3290)

> 以下**不是逐字稿內容**，是把第 4 步寫完整：三個實數或共軛對的乘積為 1、模都為 1。實本徵值只能是 $\pm1$。若三個都實：$\{1,1,1\}$ 或 $\{1,-1,-1\}$（$\{-1,-1,-1\}$ 的乘積是 $-1$，排除）。若有一對共軛複數 $\lambda,\bar\lambda$：$\lambda\bar\lambda=|\lambda|^2=1$，第三個實本徵值乘上 1 要等於 1，所以是 1。三種情況都含 1。

---

## 7. 不同本徵值的本徵向量正交

[▶ 56:02](https://youtu.be/4M--O74xj8Y?t=3362) 課本 Theorem 4.9.15。

**定理**：Hilbert 空間上自伴或么正算子的不同本徵值的本徵向量互相正交。

講者說他原本計畫講更多，但花時間在有限維線代上，「我不後悔，那對你們兩個都有幫助」。

**證明（自伴）**：$Au_1=\lambda_1u_1$、$Au_2=\lambda_2u_2$，$\lambda_1\ne\lambda_2$。由 Theorem 4.9.11，$\lambda_2$ 是實數。

$$\lambda_1\langle u_1,u_2\rangle=\langle Au_1,u_2\rangle=\langle u_1,Au_2\rangle=\langle u_1,\lambda_2u_2\rangle=\bar\lambda_2\langle u_1,u_2\rangle=\lambda_2\langle u_1,u_2\rangle.$$

所以 $(\lambda_1-\lambda_2)\langle u_1,u_2\rangle=0$，而 $\lambda_1\ne\lambda_2$，故 $\langle u_1,u_2\rangle=0$。∎

講者說么正的情形論證類似。

【課本補充】么正：$|\lambda_2|=1$ 且 $\lambda_1\ne\lambda_2$ ⟹ $\lambda_1\bar\lambda_2\ne1$。而 $\lambda_1\bar\lambda_2\langle u_1,u_2\rangle=\langle Au_1,Au_2\rangle=\langle u_1,u_2\rangle$，所以 $\langle u_1,u_2\rangle=0$。

（這就是第 23 集講者說的：Hermitian 算子不同本徵值的本徵態正交。）

---

## 8. 緊緻自伴算子

[▶ 59:43](https://youtu.be/4M--O74xj8Y?t=3583) 課本 Theorem 4.9.16–4.9.19。

**Theorem 4.9.16**：$A$ 是 Hilbert 空間上的緊緻自伴算子，則 $\|A\|$ 或 $-\|A\|$ 至少有一個是 $A$ 的**本徵值**。

（對一般的有界算子，不一定有 $|\lambda|=\|A\|$ 的本徵值；緊緻自伴時成立。）

**Corollary 4.9.17**：有 $\|w\|=1$ 使

$$|\langle Aw,w\rangle|=\sup_{\|x\|\le1}|\langle Ax,x\rangle|.$$

講者【口頭】[▶ part 2 00:01](https://youtu.be/AubT2T0_DGU?t=1)：這本質上是一個**極值定理**——緊緻自伴算子的「最大值」被達到。【課本補充】課本說：這給出一個求那個本徵值的方法：把一個二次式最大化。

**Theorem 4.9.18**：緊緻自伴算子對應**非零**本徵值的本徵空間是**有限維**的。講者：「我們得到了本徵空間的有限維性。」

**Theorem 4.9.19**：緊緻自伴算子相異的非零本徵值 $(\lambda_n)$ 是有限多個或可數多個，而且 $\lambda_n\to0$。

【課本補充】4.9.18–4.9.19 的證明都用第 26 集「緊緻算子把弱收斂變強收斂」：正規正交數列弱收斂到 0，所以 $Ax_n\to0$；但若 $Ax_n=\lambda x_n$（$\lambda\ne0$），$\|Ax_n\|=|\lambda|$ 不趨近 0，矛盾。

---

## 9. 用投影組出算子

[▶ part 2 02:15](https://youtu.be/AubT2T0_DGU?t=135) 課本 Theorem 4.9.21。

**定理**：$(P_n)$ 是兩兩正交的投影算子，$\lambda_n\to0$。則

- (a) $A=\sum\lambda_nP_n$ 在 $B(H,H)$ 中收斂，是有界算子；
- (b) 每個 $\lambda_n$ 都是 $A$ 的本徵值，其他唯一可能的本徵值是 0；
- (c) 若所有 $\lambda_n$ 是實數，$A$ 自伴；
- (d) 若所有 $P_n$ 都是有限維投影，$A$ 緊緻。

講者說這個關於投影的定理最有趣，用有限維說明【口頭】[▶ part 2 03:27](https://youtu.be/AubT2T0_DGU?t=207)：

設 $Au_j=\lambda_ju_j$（$j=1,2,3$），$u_1,u_2,u_3$ 正規正交。則

$$A=\lambda_1u_1u_1^T+\lambda_2u_2u_2^T+\lambda_3u_3u_3^T.$$

講者問：轉置放在哪個向量上？三乘一的向量要做出三乘三的矩陣，所以轉置放在**第二個**（外積）。

- $u_1u_1^T$ 作用在 $u_1$ 上得 $u_1$；作用在 $u_2,u_3$ 上是 0（點積為 0）。
- 所以 $u_ju_j^T$ 是投影到第 $j$ 個本徵空間的**投影矩陣** $P_j$：

$$A=\sum_{j=1}^3\lambda_jP_j.$$

Theorem 4.9.21 就是這個想法的**無限版**：本徵值數列 + 投影算子的級數。

> 以下**不是逐字稿內容**，是補一句：在複數情形外積要用共軛轉置 $P_j=u_ju_j^*$（物理寫 $|u_j\rangle\langle u_j|$）；實數時就是 $u_ju_j^T$。

講者【口頭】[▶ part 2 06:05](https://youtu.be/AubT2T0_DGU?t=365)：這很好玩：如果你想造一個有指定本徵向量的矩陣，有正規正交基底就能倒推，放進任何你要的本徵值。他有時這樣出例題；更簡單的方法是從對角矩陣出發，用么模矩陣共軛——「合理的人會用電腦代數系統」。

【課本補充】§4.9 最後還介紹**近似本徵值**（approximate eigenvalue）及其與緊緻算子的關係。

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 譜半徑 | $r(A)\le\|A\|$ | $|\lambda|>\|A\|$ ⟹ 預解式存在（Neumann） |
| 相似 | $A$、$TAT^{-1}$ 同本徵值 | 本徵向量 $u\leftrightarrow Tu$ |
| 自伴 | 本徵值實數 | $\lambda\langle u,u\rangle=\langle Tu,u\rangle=\langle u,Tu\rangle=\bar\lambda\langle u,u\rangle$ |
| 自伴 | $r(A)=\|A\|$ | $\|A\|=\sup|\langle Ax,x\rangle|$；近似本徵值 |
| 正算子 | 本徵值 $\ge0$ | $\langle Ax,x\rangle=\lambda\|x\|^2$ |
| 么正 | $|\lambda|=1$ | $\langle x,x\rangle=\langle Ux,Ux\rangle=|\lambda|^2\langle x,x\rangle$ |
| $SO(2)$ | 本徵值 $e^{\pm i\theta}$；實的只有 $\theta=0,\pi$ | |
| $SO(3)$ | 必有本徵值 1（旋轉軸）；$\operatorname{tr}R=1+2\cos\theta$ | $\det=1$、$|\lambda|=1$、共軛對 |
| 正交 | 自伴或么正：不同本徵值的本徵向量正交 | $(\lambda_1-\lambda_2)\langle u_1,u_2\rangle=0$ |
| 緊緻自伴 | $\pm\|A\|$ 是本徵值；非零本徵空間有限維；本徵值 $\to0$ | 緊緻：弱收斂 → 強收斂 |
| 投影分解 | $A=\sum\lambda_nP_n$ | 有限維：$A=\sum\lambda_ju_ju_j^*$ |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 緊緻自伴算子 + 投影分解 | 第 29 集：譜定理（§4.10） |
| 自伴 → 實本徵值、正交本徵函數 | 第 29–30 集：邊界值問題、Sturm–Liouville |
| 么正、旋轉 | 第 33–34 集：量子力學的對稱與時間演化 |
| 二次式最大化求本徵值 | 課本第 9 章：最佳化（變分法） |

---

## 附：本集一句話總結

> **譜半徑不超過範數；自伴算子的本徵值是實數、不同本徵值的本徵向量正交（這就是量子力學要 Hermitian 可觀測量的理由），么正算子的本徵值在單位圓上——所以三維旋轉一定有一根軸，轉角可以從跡 $1+2\cos\theta$ 讀出；緊緻自伴算子更好：本徵值可數、趨近 0、非零本徵空間有限維，算子可以寫成「本徵值乘投影」的和。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-04-05 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 6:52）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.9 整理。*
