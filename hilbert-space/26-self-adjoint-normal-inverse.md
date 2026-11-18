---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 26
lecture: Lecture 26
date: 2023-03-29
video: https://youtu.be/UREpRbEZ22w （part 1）、https://youtu.be/Y1GqjfSWE1w （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.4–4.5（書頁 158–168，PDF 頁 177–187）；§4.6–4.8 只念過
---

# 第 26 集 · 自伴、正規、可逆、等距、么正算子 [▶ 影片](https://youtu.be/UREpRbEZ22w)

← 上一集：[25-bilinear-forms-adjoint](25-bilinear-forms-adjoint.md) ｜ [總目錄](README.md) ｜ 下一集：[27-eigenvectors-spectrum-resolvent](27-eigenvectors-spectrum-resolvent.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 26 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 40:27，自動字幕）＋ Debnath & Mikusiński §4.4–4.8
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 算一個伴隨的例子](#1-算一個伴隨的例子)
- [2. 自伴算子與 Hermitian 矩陣](#2-自伴算子與-hermitian-矩陣)
- [3. Fredholm 算子的伴隨](#3-fredholm-算子的伴隨)
- [4. 構造自伴算子的定理](#4-構造自伴算子的定理)
- [5. T = A + iB：算子的「實部、虛部」](#5-t--a--ib算子的實部虛部)
- [6. 自伴算子的範數](#6-自伴算子的範數)
- [7. 可逆算子](#7-可逆算子)
- [8. 正規算子](#8-正規算子)
- [9. 等距算子](#9-等距算子)
- [10. 么正算子](#10-么正算子)
- [11. §4.6–4.8 速覽](#11-4648-速覽)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與後續集數的連結](#13-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說今天換到一間大教室，「因為其他人都在考試，哈哈」。[▶ 00:03](https://youtu.be/UREpRbEZ22w?t=3)

| 主題 | 課本 |
|---|---|
| 伴隨的例子、自伴、Hermitian | pp. 158–159、Example 4.4.4–4.4.5 |
| Fredholm 算子、乘以 $t$ | Example 4.4.6–4.4.7，p. 160 |
| 構造自伴算子；$T=A+iB$；$\|T\|=\sup|\langle Tx,x\rangle|$ | Theorem 4.4.9–4.4.14，pp. 161–163 |
| 可逆算子 | Definition 4.5.1–Corollary 4.5.6，pp. 163–165 |
| 正規算子 | Definition 4.5.7–Theorem 4.5.12，pp. 165–166 |
| 等距、么正算子 | Definition 4.5.13–Theorem 4.5.20，pp. 166–168 |

---

## 1. 算一個伴隨的例子

[▶ 00:34](https://youtu.be/UREpRbEZ22w?t=34) 課本 p. 159。

複習：$\langle Ax,y\rangle=\langle x,A^*y\rangle$ 定義伴隨；有界時 $\|A^*\|=\|A\|$、$\|A^*A\|=\|A\|^2$。

**例**：$H=\mathbb{C}^2$，$A(z_1,z_2)=(0,z_1)$。

講者用定義硬算：$\mathbb{C}^n$ 的內積是 $z^T\bar w$。

$$\langle Az,w\rangle=(0,z_1)\cdot(\bar w_1,\bar w_2)=z_1\bar w_2,\qquad\langle z,A^*w\rangle=z_1\overline{(A^*w)_1}+z_2\overline{(A^*w)_2}.$$

對所有 $z$ 相等：

- 取 $z=(0,1)$：$\overline{(A^*w)_2}=0$。
- 取 $z=(1,0)$：$\overline{(A^*w)_1}=\bar w_2$。

所以 $A^*(w_1,w_2)=(w_2,0)$。[▶ 07:49](https://youtu.be/UREpRbEZ22w?t=469)

講者說這是笨方法；簡單的方法是用矩陣：$A$ 的矩陣是 $\begin{pmatrix}0&0\\1&0\end{pmatrix}$，伴隨是**共軛轉置** $\begin{pmatrix}0&1\\0&0\end{pmatrix}$，就是 $(w_1,w_2)\mapsto(w_2,0)$。

$A\ne A^*$：伴隨不一定等於自己。

---

## 2. 自伴算子與 Hermitian 矩陣

[▶ 10:11](https://youtu.be/UREpRbEZ22w?t=611) 課本 Definition 4.4.3、Example 4.4.4–4.4.5。

**自伴（self-adjoint）**：$A=A^*$，即 $\langle Ax,y\rangle=\langle x,Ay\rangle$。

- 在 $\mathbb{C}^N$ 中：$A$ 的矩陣 $M$ 滿足 $\overline{M}^T=M$，叫 **Hermitian 矩陣**（物理寫 $M^\dagger=M$）。
- 在可分無限維 Hilbert 空間中，對正規正交數列的**無窮矩陣**也可以談共軛轉置：$A$ 自伴 ⟺ $a_{ij}=\overline{a_{ji}}$。

---

## 3. Fredholm 算子的伴隨

[▶ 12:31](https://youtu.be/UREpRbEZ22w?t=751) 課本 Example 4.4.6。講者說這個例子之前一直跳過。

**Fredholm 算子**：在 $L^2([a,b])$ 上

$$(Tx)(s)=\int_a^bK(s,t)x(t)\,dt,\qquad\int_a^b\int_a^b|K(s,t)|^2dsdt<\infty$$

（$K$ 連續時這個條件自動成立）。

**算伴隨**[▶ 14:16](https://youtu.be/UREpRbEZ22w?t=856)：

$$\langle Tx,y\rangle=\int_a^b\left(\int_a^bK(s,t)x(t)dt\right)\overline{y(s)}\,ds.$$

講者說這裡用 **Fubini** 交換積分順序（有限的二重積分條件允許）。把整個式子寫成「共軛的共軛」，把 $x(t)$ 拉到外面：

$$\langle Tx,y\rangle=\int_a^bx(t)\overline{\left(\int_a^b\overline{K(s,t)}\,y(s)\,ds\right)}dt.$$

所以共軛號下的那個東西就是 $(T^*y)(t)$：

$$(T^*y)(t)=\int_a^b\overline{K(s,t)}\,y(s)\,ds,\qquad\text{換字母：}\quad(T^*y)(s)=\int_a^b\overline{K(t,s)}\,y(t)\,dt.$$

**自伴的條件**[▶ 23:43](https://youtu.be/UREpRbEZ22w?t=1423)：$T$ 自伴 ⟺

$$K(s,t)=\overline{K(t,s)}.$$

講者【口頭】：這跟矩陣的情況很像——「翻轉輸入再取共軛」，就像共軛轉置。直觀上可以把 $K(s,t)$ 想成一個「連續指標」的無窮矩陣，這就是「連續指標層次的 Hermitian 條件」。他說 Fredholm 算子在微分方程和 Green 函數裡會再出現（他幾年前帶學生做 PDE 小課程時碰過）。[▶ 27:32](https://youtu.be/UREpRbEZ22w?t=1652)

**乘以 $t$**（Example 4.4.7）[▶ 25:23](https://youtu.be/UREpRbEZ22w?t=1523)：$(Ax)(t)=tx(t)$ 在 $L^2([a,b])$ 上自伴：

$$\langle Ax,y\rangle=\int_a^btx(t)\overline{y(t)}dt=\int_a^bx(t)\overline{ty(t)}dt=\langle x,Ay\rangle,$$

因為 $t$ 是實數，等於自己的共軛（$x,y$ 可以是複值）。

---

## 4. 構造自伴算子的定理

[▶ 27:32](https://youtu.be/UREpRbEZ22w?t=1652)

**Theorem 4.4.9**：$\varphi$ 有界雙線性泛函，$\varphi(x,y)=\langle x,Ay\rangle$。則 $A$ 自伴 ⟺ $\varphi$ 對稱。

講者的計算：$\overline{\varphi(y,x)}=\overline{\langle y,Ax\rangle}=\langle Ax,y\rangle=\langle x,A^*y\rangle$。若 $\varphi$ 對稱，左邊是 $\varphi(x,y)=\langle x,Ay\rangle$，所以 $A^*=A$；反之亦然。

**Theorem 4.4.10**[▶ 31:42](https://youtu.be/UREpRbEZ22w?t=1902)：$A$ 有界，則 $T_1=A^*A$、$T_2=A+A^*$ 都自伴。

（講者其實證的是 $AA^*$，同理。）

$$\langle AA^*x,y\rangle=\langle A^*x,A^*y\rangle=\langle x,(A^*)^*A^*y\rangle=\langle x,AA^*y\rangle,$$

用了 $(A^*)^*=A$（p. 158 說由定義直接得到）。對所有 $x,y$ 成立，所以自伴。$T_2$：$(A+A^*)^*=A^*+A^{**}=A^*+A$，加法可交換。

**Theorem 4.4.11**[▶ 35:51](https://youtu.be/UREpRbEZ22w?t=2151)：$T_1,T_2$ 自伴，則 $T_1T_2$ 自伴 ⟺ $T_1T_2=T_2T_1$。

$$\langle T_1T_2x,y\rangle=\langle T_2x,T_1y\rangle=\langle x,T_2T_1y\rangle,$$

所以 $(T_1T_2)^*=T_2T_1$；等於 $T_1T_2$ ⟺ 兩者交換。

**Corollary 4.4.12**[▶ 38:09](https://youtu.be/UREpRbEZ22w?t=2289)：$A$ 自伴，則 $A$ 的多項式 $\alpha_nA^n+\cdots+\alpha_1A+\alpha_0I$ 也自伴。（課本要求係數是**實數**。）

講者【口頭】：很多數學系學生沒修微分方程，就很少接觸「算子的多項式」。「如果我教線代，就塞一週微分方程進去。」算子的多項式：乘積變成合成，係數就是純量。

> 以下**不是逐字稿內容**，是補一句為什麼要實係數：$(\alpha A)^*=\bar\alpha A^*$；係數是複數時，例如 $(iA)^*=-iA\ne iA$。

---

## 5. T = A + iB：算子的「實部、虛部」

[▶ 39:52](https://youtu.be/UREpRbEZ22w?t=2392) 課本 Theorem 4.4.13。

**定理**：每個有界算子 $T$ 都有**唯一**的自伴算子 $A,B$ 使

$$T=A+iB,\qquad T^*=A-iB.$$

講者說：其實只要說第一個，第二個由伴隨的性質自動成立。這讓人更了解自伴是什麼：**自伴算子就像實數**，這是算子的實部、虛部分解。

**構造**[▶ 41:45](https://youtu.be/UREpRbEZ22w?t=2505)：

$$A=\frac12(T+T^*),\qquad B=\frac1{2i}(T-T^*).$$

- $A^*=\frac12(T^*+T)=A$。
- $B^*=\overline{\left(\tfrac{1}{2i}\right)}(T^*-T)=-\frac1{2i}(T^*-T)=\frac1{2i}(T-T^*)=B$（伴隨會把純量取共軛，$\frac1{2i}$ 變 $-\frac1{2i}$，負號把順序翻回來）。

講者說課本是直接在內積上算 $T^*=A-iB$（p. 162）。（唯一性是習題。）

【課本補充】課本：「特別地，若 $T$ 自伴，則 $A=T$、$B=0$。自伴算子就像 $\mathbb{C}$ 中的實數。」

---

## 6. 自伴算子的範數

[▶ 43:30](https://youtu.be/UREpRbEZ22w?t=2610) 課本 Theorem 4.4.14。

**定理**：$T$ 是自伴算子，則

$$\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|. \tag{4.4}$$

【課堂討論】講者問 $\|T\|$ 的定義，學生說「差不多是這個」；講者：「差不多……就像少了一個 $T$。」（定義是 $\sup\|Tx\|$。）他也說：向量跟自己的內積是實數，所以那個絕對值其實……（自伴時 $\langle Tx,x\rangle$ 是實數，但可能是負的，所以絕對值要留著。）證明一頁，「不完全平凡」。

**一個方向**[▶ 45:56](https://youtu.be/UREpRbEZ22w?t=2756)：$\|x\|=1$ 時，由 Schwarz 和 $\|Tx\|\le\|T\|\|x\|$：

$$|\langle Tx,x\rangle|\le\|Tx\|\|x\|\le\|T\|.$$

所以 $M=\sup|\langle Tx,x\rangle|\le\|T\|$。

**另一方向**：講者說課本「做得更狡猾」，讓學生自己看。

【課本補充】另一方向：對所有 $x,z$，

$$\langle T(x+z),x+z\rangle-\langle T(x-z),x-z\rangle=4\operatorname{Re}\langle Tx,z\rangle$$

（用到自伴），所以 $\operatorname{Re}\langle Tx,z\rangle\le\frac M4(\|x+z\|^2+\|x-z\|^2)=\frac M2(\|x\|^2+\|z\|^2)$（平行四邊形定律）。取 $\|x\|=1$、$z=Tx/\|Tx\|$，左邊是 $\|Tx\|$，右邊是 $M$。所以 $\|T\|\le M$。

---

## 7. 可逆算子

[▶ 48:52](https://youtu.be/UREpRbEZ22w?t=2932) 課本 Definition 4.5.1–Corollary 4.5.6。

**定義**：$A$ 定義在 $E$ 的子空間上。定義在值域 $\mathcal R(A)$ 上的算子 $B$ 叫 $A$ 的**逆**，如果 $ABx=x$（$x\in\mathcal R(A)$）且 $BAx=x$（$x\in\mathcal D(A)$）。記作 $A^{-1}$。

講者：「我只是在說算子的逆，就跟函數的逆一樣的笨定義。」課本計較定義域，是因為這本書有一部分是寫給研究所的工程師看的。[▶ 51:29](https://youtu.be/UREpRbEZ22w?t=3089)

**Theorem 4.5.2**（證明是習題）：

- (a) 線性算子的逆是線性的；
- (b) $A$ 可逆 ⟺ $Ax=0$ 只有 $x=0$（齊次方程只有零解）；
- (c) $A$ 可逆、$x_1,\dots,x_n$ 線性獨立 ⟹ $Ax_1,\dots,Ax_n$ 線性獨立；
- (d) $(AB)^{-1}=B^{-1}A^{-1}$。講者叫它「襪子鞋子公式」。

**有限維 vs 無限維**[▶ 53:56](https://youtu.be/UREpRbEZ22w?t=3236)：由 (c)，有限維時可逆算子的值域一定是整個 $E$。無限維不一定。

講者【口頭】：在 $\mathbb{R}$、$\mathbb{C}$、$\mathbb{Q}$ 這種特徵為 0 的體上，向量空間本身是無限集合；有限集合之間的函數「一對一 ⟺ 映成」，無限集合一般不成立。但有限**維**時，維度給了某種有限性，所以線性變換仍然「映成 ⟺ 一對一」。「這是我哥哥（賣二手車那位）的想法，不是我的。」

**例**（Example 4.5.3，單邊移位）[▶ 55:38](https://youtu.be/UREpRbEZ22w?t=3338)：$\ell^2$ 上 $A(x_1,x_2,\dots)=(0,x_1,x_2,\dots)$。可逆（在值域上），但值域是 $\ell^2$ 的真子空間。講者：這就是定義要計較值域的原因。

**例**（Example 4.5.4，有界算子的逆不一定有界）[▶ 56:54](https://youtu.be/UREpRbEZ22w?t=3414)：

$$A(x_1,x_2,x_3,\dots)=\left(x_1,\frac{x_2}2,\frac{x_3}3,\dots\right),\qquad A^{-1}(x_1,x_2,\dots)=(x_1,2x_2,3x_3,\dots).$$

$\|Ax\|^2=\sum\frac{|x_n|^2}{n^2}\le\|x\|^2$，$A$ 有界；但 $A^{-1}e_n=ne_n$，$A^{-1}$ 不有界。講者：一個會像 $p=2$ 級數那樣收斂，另一個算範數時會像 $\sum n^2$。

**Theorem 4.5.5**[▶ 58:48](https://youtu.be/UREpRbEZ22w?t=3528)：$A$ 有界、$\mathcal R(A)=H$、有有界的逆，則 $A^*$ 可逆，而且

$$(A^*)^{-1}=(A^{-1})^*.$$

講者：「一次兩個」：只要證 $(A^{-1})^*A^*x=x$ 而且 $A^*(A^{-1})^*x=x$（左右逆都要）。[▶ part 2 00:59](https://youtu.be/Y1GqjfSWE1w?t=59) 課本的計算：

$$\langle y,(A^{-1})^*A^*x\rangle=\langle A^{-1}y,A^*x\rangle=\langle AA^{-1}y,x\rangle=\langle y,x\rangle,$$

對所有 $y$ 成立，所以 $(A^{-1})^*A^*x=x$；另一個一樣，只是 $A$ 和 $A^{-1}$ 的順序對調，而 $A^{-1}A$ 也是恆等。

講者【口頭】[▶ part 2 03:55](https://youtu.be/Y1GqjfSWE1w?t=235)：他在線代課有時出這題（有限維版），會讓學生卡住，「也曾經讓我卡住……很容易相信，但要證的時候就打結」。

**Corollary 4.5.6**[▶ part 2 04:36](https://youtu.be/Y1GqjfSWE1w?t=276)：有界自伴算子若有有界的逆，則 $A^{-1}$ 自伴：$(A^{-1})^*=(A^*)^{-1}=A^{-1}$。

---

## 8. 正規算子

[▶ part 2 05:22](https://youtu.be/Y1GqjfSWE1w?t=322) 課本 Definition 4.5.7–Theorem 4.5.12。

**定義**：有界算子 $T$ 叫**正規（normal）**，如果 $TT^*=T^*T$（跟自己的伴隨交換）。

【課堂討論】講者問：自伴算子是正規的嗎？學生答：是。講者：「很蠢：$T^*T=TT$。」反過來不成立。

**Theorem 4.5.8**（講者說可以拿來當定義，跳過證明）[▶ part 2 07:25](https://youtu.be/Y1GqjfSWE1w?t=445)：

$$T\text{ 正規}\iff\|Tx\|=\|T^*x\|\quad\text{對所有 }x.$$

【課本補充】證明：$\|Tx\|^2=\langle T^*Tx,x\rangle$，$\|T^*x\|^2=\langle TT^*x,x\rangle$；兩者對所有 $x$ 相等 ⟺（Corollary 4.3.8）$T^*T=TT^*$。課本提醒：$\|Tx\|=\|T^*x\|$ 對所有 $x$，比 $\|T\|=\|T^*\|$ 強得多。

**例：正規但不自伴**（Example 4.5.9）[▶ part 2 08:32](https://youtu.be/Y1GqjfSWE1w?t=512)：$Tx=ix$。$T^*x=-ix=-Tx$，不自伴；但 $\|Tx\|=\|T^*x\|$，正規。講者【口頭】：$T^*=-T$ 的算子在物理裡有時叫**反自伴（anti-self-adjoint）**。

**Theorem 4.5.10**[▶ part 2 10:14](https://youtu.be/Y1GqjfSWE1w?t=614)：$A$ 正規 ⟹ $\alpha I-A$ 正規（任意 $\alpha\in\mathbb{C}$）。講者說「有點出乎意料」。

$$(\alpha I-A)(\alpha I-A)^*=(\alpha I-A)(\bar\alpha I-A^*)=|\alpha|^2I-\alpha A^*-\bar\alpha A+AA^*.$$

（$I^*=I$。）另一個順序展開也一樣，關鍵是 $AA^*=A^*A$（正規），而純量項和加法都可交換。

**Theorem 4.5.11**[▶ part 2 13:16](https://youtu.be/Y1GqjfSWE1w?t=796)：$T=A+iB$（$A,B$ 自伴），則 $T$ 正規 ⟺ $AB=BA$。

$$TT^*=(A+iB)(A-iB)=A^2+B^2-i(AB-BA),\qquad T^*T=(A-iB)(A+iB)=A^2+B^2+i(AB-BA).$$

兩者相等 ⟺ $AB-BA=0$。講者：「當然。」

**Theorem 4.5.12**[▶ part 2 16:12](https://youtu.be/Y1GqjfSWE1w?t=972)：$T$ 正規 ⟹ $\|T^n\|=\|T\|^n$。講者：「正規算子很棒，有這種很酷的性質。」

**譜定理的預告**【口頭】[▶ part 2 16:58](https://youtu.be/Y1GqjfSWE1w?t=1018)：在實線性代數裡，**對稱矩陣有正規正交的本徵向量基底，而且本徵值都是實數**。正規算子、伴隨這套技術就用在譜定理的證明裡；這本書稍後會有無限維的版本，跟投影算子有關。

---

## 9. 等距算子

[▶ part 2 17:35](https://youtu.be/Y1GqjfSWE1w?t=1055) 課本 Definition 4.5.13–Theorem 4.5.15。

**定義**：有界算子 $T$ 叫**等距（isometric）**，如果 $\|Tx\|=\|x\|$ 對所有 $x$。

**例：單邊移位**（Example 4.5.14）[▶ part 2 18:59](https://youtu.be/Y1GqjfSWE1w?t=1139)：$(e_n)$ 是（可分空間的）完備正規正交數列，$Ae_n=e_{n+1}$，即 $A\left(\sum\alpha_ne_n\right)=\sum\alpha_ne_{n+1}$。

【課堂討論】學生說：像物理的**階梯算子**。講者：數學家叫它**移位算子（shift operator）**，物理叫階梯算子，「真是把我帶回過去」。

$\|Ax\|^2=\sum|\alpha_n|^2=\|x\|^2$：係數完全一樣，只是往右移一格，不會多算。所以 $A$ 等距。

**Theorem 4.5.15**[▶ part 2 21:56](https://youtu.be/Y1GqjfSWE1w?t=1316)：有界算子 $T$ 等距 ⟺ $T^*T=I$。

**(⟹)**：$\|Tx\|^2=\|x\|^2$ ⟹ $\langle T^*Tx,x\rangle=\langle Tx,Tx\rangle=\langle x,x\rangle$ 對所有 $x$ ⟹（Corollary 4.3.8）$T^*T=I$。

【課堂討論】[▶ part 2 24:07](https://youtu.be/Y1GqjfSWE1w?t=1447) 講者接著想推出 $TT^*=I$，說「$\|T^*x\|=\|Tx\|$ 是任何有界算子的一般恆等式」。學生指出：那只對**正規**算子成立。講者：「你說得對……別買我賣的東西，那不對。」所以只得到 $T^*T=I$，而那正是要證的。

> 以下**不是逐字稿內容**，是補例子：單邊移位 $A$ 等距，$A^*A=I$；但 $A^*e_1=0$，所以 $AA^*e_1=0\ne e_1$，$AA^*\ne I$。等距算子不一定正規。

**(⟸)**：$T^*T=I$ ⟹ $\|Tx\|^2=\langle T^*Tx,x\rangle=\langle x,x\rangle$。講者：「反過來把計算倒著走。」

【課本補充】等距算子**保內積**：$\langle Tx,Ty\rangle=\langle x,y\rangle$（極化恆等式），所以保正交；它是 $H$ 到 $\mathcal R(T)$ 的 Hilbert 空間同構。

---

## 10. 么正算子

[▶ part 2 27:30](https://youtu.be/Y1GqjfSWE1w?t=1650) 課本 Definition 4.5.16–Theorem 4.5.20。

**定義**：有界算子 $T$ 叫**么正（unitary）**，如果 $T^*T=TT^*=I$。

**Theorem 4.5.17**：$T$ 么正 ⟺ $T$ 可逆且 $T^{-1}=T^*$。講者：「離定義只有一步之遙」，那個方程就是說 $T$ 有逆，而逆必須是伴隨。

**例：雙邊移位**（Example 4.5.18）[▶ part 2 28:43](https://youtu.be/Y1GqjfSWE1w?t=1723)：

$$H=\left\{x=(\dots,x_{-1},x_0,x_1,\dots):\sum_{n=-\infty}^\infty|x_n|^2<\infty\right\},\qquad\langle x,y\rangle=\sum_{n=-\infty}^\infty x_n\bar y_n.$$

講者說這種向兩邊無限延伸的數列有人叫「雙向數列（double sequence）」。$T(x_n)=(x_{n-1})$。

**驗證**[▶ part 2 31:46](https://youtu.be/Y1GqjfSWE1w?t=1906)：$T$ 可逆，而且

$$\langle Tx,y\rangle=\sum_nx_{n-1}\bar y_n\overset{k=n-1}{=}\sum_kx_k\bar y_{k+1}=\langle x,T^{-1}y\rangle,$$

所以 $T^*=T^{-1}$，么正。講者：「懂了內積之後，它是么正的就擺在你眼前——長度被保持。」**么正算子就是保長度的映射**；在歐氏空間（實的情形）就是**正交**算子。

【課本補充】么正 = 值域是整個 $H$ 的等距算子。Example 4.5.19：$L^2([0,1])$ 上 $(Tx)(t)=x(1-t)$ 么正。么正 ⟹ 正規，反之不然（例如範數不是 1 的自伴算子）。

**Theorem 4.5.20**[▶ part 2 33:28](https://youtu.be/Y1GqjfSWE1w?t=2008)：$T$ 么正 ⟹ $T^{-1}$、$T^*$ 也么正。

---

## 11. §4.6–4.8 速覽

【口頭】[▶ part 2 34:09](https://youtu.be/Y1GqjfSWE1w?t=2049) 講者很想跳過幾節直接到本徵值；他念過這幾節的重點：

**§4.6 正算子**（最不在意跳過）：本質上在問「算子能不能開平方根」，答案是「差不多、有時候」。

- **正算子**：自伴，而且 $\langle Ax,x\rangle\ge0$ 對所有 $x$。
- **平方根**：自伴的 $B$ 使 $B^2=A$。
- Theorem 4.6.14：每個正算子 $A$ 都有唯一的正平方根 $B$，而且 $B$ 跟每個與 $A$ 交換的算子交換。
- 講者：正算子的定義是「為了讓平方根存在而量身訂做的」，不過也不算不自然。

**§4.7 投影算子**：他認為跳過也不會太糟。

**§4.8 緊緻算子**：他比較擔心跳過會不會「欺騙」學生。講到緊緻就是在談某種「有限性」。

- **緊緻（compact／completely continuous）算子**：對每個有界數列 $(x_n)$，$(Ax_n)$ 有收斂子數列。有限維空間上的每個算子都緊緻。
- 緊緻算子構成向量空間；$A$ 緊緻、$B$ 有界 ⟹ $AB$、$BA$ 緊緻。
- 投影到**有限維**子空間的投影算子緊緻。
- **有限維算子**：值域有限維。
- 緊緻算子的一致極限是緊緻的（又是 $\varepsilon/3$ 論證）；所以有限維算子的極限是緊緻的。
- 緊緻算子的伴隨是緊緻的。
- **緊緻算子把弱收斂數列變成強收斂數列**（較技術）；推論：把正規正交數列映成強收斂到 0 的數列——講者：「這聽起來有用……證明只有一行。」
- 課本說：緊緻性是比連續更強的連續；Riesz 用這個條件當緊緻算子的定義，Hilbert 有另一個等價定義（用內積）。

**下次**：本徵值與本徵向量，或者先跳到偏微分方程。

---

## 12. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 伴隨例 | $A(z_1,z_2)=(0,z_1)$，$A^*(w_1,w_2)=(w_2,0)$ | 共軛轉置 |
| 自伴 | $A=A^*$；矩陣 Hermitian $a_{ij}=\overline{a_{ji}}$ | |
| Fredholm | $(T^*y)(s)=\int\overline{K(t,s)}y(t)dt$；自伴 ⟺ $K(s,t)=\overline{K(t,s)}$ | Fubini |
| 乘以 $t$ | 自伴 | $t$ 實數 |
| 構造 | $A^*A$、$A+A^*$ 自伴；$T_1T_2$ 自伴 ⟺ 交換 | $(A^*)^*=A$ |
| 分解 | $T=A+iB$，$A=\frac{T+T^*}2$，$B=\frac{T-T^*}{2i}$ | 自伴 ≈ 實數 |
| 自伴範數 | $\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|$ | 平行四邊形定律 |
| 可逆 | $(AB)^{-1}=B^{-1}A^{-1}$；$(A^*)^{-1}=(A^{-1})^*$ | 有限維：可逆 ⟹ 映成 |
| 反例 | 單邊移位可逆但不映成；$\operatorname{diag}(1/n)$ 的逆不有界 | |
| 正規 | $TT^*=T^*T$ ⟺ $\|Tx\|=\|T^*x\|$ ∀$x$ | 例：$iI$ |
| 正規性質 | $\alpha I-A$ 正規；$T=A+iB$ 正規 ⟺ $AB=BA$；$\|T^n\|=\|T\|^n$ | |
| 等距 | $\|Tx\|=\|x\|$ ⟺ $T^*T=I$ | 單邊移位；$TT^*\ne I$ |
| 么正 | $T^*T=TT^*=I$ ⟺ $T^{-1}=T^*$ | 雙邊移位；保長度 |
| 正算子 | 自伴、$\langle Ax,x\rangle\ge0$；有唯一正平方根 | |
| 緊緻 | 有界數列的像有收斂子數列；弱收斂 → 強收斂 | |

---

## 13. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 自伴、正規 | 第 27–28 集：自伴算子的本徵值是實數、不同本徵值的本徵向量正交 |
| $\alpha I-A$ | 第 27 集：預解式 $(A-\lambda I)^{-1}$、譜 |
| 緊緻算子 | 第 29 集：緊緻自伴算子的譜定理 |
| Fredholm 算子 | 第 31 集：Green 函數 |
| 移位／階梯算子、么正 | 第 33–34 集：量子力學（時間演化、諧振子） |

---

## 附：本集一句話總結

> **伴隨在有限維是共軛轉置、在積分算子是「翻轉核再取共軛」；自伴算子像實數（每個算子都能寫成 $A+iB$），正規算子是跟伴隨交換的、等價於 $\|Tx\|=\|T^*x\|$，等距算子保長度（$T^*T=I$），么正算子則是可逆的等距、逆就是伴隨——而無限維裡，可逆不一定映成、有界算子的逆也不一定有界。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-29 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 40:27）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.4–4.8 整理。*
