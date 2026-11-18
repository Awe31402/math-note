---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 25
lecture: Lecture 25
date: 2023-03-24
video: https://youtu.be/YESsX40YL1c （part 1）、https://youtu.be/uqszOPtXFFQ （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.3、§4.4 開頭（書頁 151–159，PDF 頁 170–178）
---

# 第 25 集 · 雙線性泛函與二次型、Lax–Milgram、伴隨算子 [▶ 影片](https://youtu.be/YESsX40YL1c)

← 上一集：[24-riesz-representation-operators](24-riesz-representation-operators.md) ｜ [總目錄](README.md) ｜ 下一集：[26-self-adjoint-normal-inverse](26-self-adjoint-normal-inverse.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 25 集。一位學生在路上，事後看錄影。
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 9:58，自動字幕）＋ Debnath & Mikusiński §4.3–4.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 雙線性泛函（其實是 sesquilinear）](#1-雙線性泛函其實是-sesquilinear)
- [2. 對稱、正、嚴格正、有界](#2-對稱正嚴格正有界)
- [3. 二次型](#3-二次型)
- [4. 極化恆等式與它的推論](#4-極化恆等式與它的推論)
- [5. 對稱 ⟺ 二次型是實的；範數的關係](#5-對稱--二次型是實的範數的關係)
- [6. ⟨Ax,y⟩ 的範數就是 ‖A‖](#6-axy-的範數就是-a)
- [7. 每個有界雙線性泛函都是 ⟨x,Ay⟩](#7-每個有界雙線性泛函都是-xay)
- [8. 強制性與 Lax–Milgram 定理](#8-強制性與-laxmilgram-定理)
- [9. 伴隨算子](#9-伴隨算子)
- [10. 預告](#10-預告)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者說這節要很快帶過，「我大概忍不住會證一些東西」，但這節的證明大多很清楚。[▶ 00:46](https://youtu.be/YESsX40YL1c?t=46)

| 主題 | 課本 |
|---|---|
| 雙線性泛函、對稱、正、有界 | Definition 4.3.1–4.3.5，pp. 151–152 |
| 二次型、極化恆等式 | Definition 4.3.6、Theorem 4.3.7–4.3.8，pp. 152–153 |
| 對稱 ⟺ 二次型實；範數關係 | Theorem 4.3.9–4.3.11，pp. 153–155 |
| $\|\langle A\cdot,\cdot\rangle\|=\|A\|$；表示定理 | Theorem 4.3.12–4.3.13，pp. 155–156 |
| 強制性、Lax–Milgram | Definition 4.3.14、Theorem 4.3.16，pp. 156–158 |
| 伴隨算子 | Definition 4.4.1、Theorem 4.4.2，pp. 158–159 |

---

## 1. 雙線性泛函（其實是 sesquilinear）

[▶ 01:21](https://youtu.be/YESsX40YL1c?t=81) 課本 Definition 4.3.1。

**定義**：複向量空間 $E$ 上的**雙線性泛函（bilinear functional）**是 $\varphi:E\times E\to\mathbb{C}$，滿足

- (a) $\varphi(\alpha x_1+\beta x_2,y)=\alpha\varphi(x_1,y)+\beta\varphi(x_2,y)$；
- (b) $\varphi(x,\alpha y_1+\beta y_2)=\bar\alpha\varphi(x,y_1)+\bar\beta\varphi(x,y_2)$。

講者：課本的「雙線性」其實是 **sesquilinear**（第一位置線性、第二位置共軛線性），課本自己也承認。他說數學用語常因領域而異，例如「範數」在數論裡是整數值、不一定定義在向量空間上。[▶ 01:56](https://youtu.be/YESsX40YL1c?t=116)

**例**[▶ 03:23](https://youtu.be/YESsX40YL1c?t=203)：

1. **內積** $\varphi(x,y)=\langle x,y\rangle$（這是研究它的主要動機）。很多內積的性質對 sesquilinear 形式也成立，例如第二位置可加。
2. $\varphi(x,y)=\langle Ax,y\rangle$ 或 $\langle x,By\rangle$，$A,B$ 是（線性）算子。
3. $f,g$ 是線性泛函，$\varphi(x,y)=f(x)\overline{g(y)}$：$f$ 線性給第一位置，$g$ 線性再取共軛給第二位置的共軛線性。

---

## 2. 對稱、正、嚴格正、有界

[▶ 06:22](https://youtu.be/YESsX40YL1c?t=382) 課本 Definition 4.3.5。

| 名稱 | 條件 |
|---|---|
| 對稱（symmetric） | $\varphi(x,y)=\overline{\varphi(y,x)}$；實的情形就是 $\varphi(x,y)=\varphi(y,x)$ |
| 正（positive） | $\varphi(x,x)\ge0$ |
| 嚴格正（strictly positive） | 正，且 $x\ne0$ 時 $\varphi(x,x)>0$ |
| 有界（$E$ 是賦範空間） | $|\varphi(x,y)|\le K\|x\|\|y\|$ |

**範數**：$\|\varphi\|=\sup_{\|x\|=\|y\|=1}|\varphi(x,y)|$，所以 $|\varphi(x,y)|\le\|\varphi\|\|x\|\|y\|$。

講者說：前面的定義只要複向量空間；有界需要範數；例子用到內積。【Q&A】學生問需不需要完備，講者：「我不覺得完備性在這裡有作用……內積空間就夠了。」[▶ 08:43](https://youtu.be/YESsX40YL1c?t=523)

**內積的範數**[▶ 11:07](https://youtu.be/YESsX40YL1c?t=667)：內積是對稱、嚴格正、有界的雙線性泛函，有界常數 $K=1$（Cauchy–Schwarz）。講者問：內積的範數是多少？

$$\|\langle\cdot,\cdot\rangle\|=\sup_{\|x\|=\|y\|=1}|\langle x,y\rangle|\le\sup\|x\|\|y\|=1,$$

而取 $x=y$（單位向量）就達到 $\|x\|^2=1$，所以範數就是 **1**。講者說他沒完全證完，但給了思路。【Q&A】學生問不完備時是否仍成立，講者：Cauchy–Schwarz 只是內積的性質，不需要完備，所以成立。

【課本補充】例 3 中若 $f=g$，$\varphi$ 對稱且正；若 $A,B$（或 $f,g$）有界，例 2、3 都是有界的。

---

## 3. 二次型

[▶ 15:20](https://youtu.be/YESsX40YL1c?t=920) 課本 Definition 4.3.6。

**定義**：$\varphi$ 是雙線性泛函，

$$\Phi(x)=\varphi(x,x)$$

叫與 $\varphi$ 相伴的**二次型（quadratic form）**。

- **有界**：$|\Phi(x)|\le K\|x\|^2$。
- **範數**：$\|\Phi\|=\sup_{\|x\|=1}|\Phi(x)|$，所以 $|\Phi(x)|\le\|\Phi\|\|x\|^2$。

課本：雙線性泛函和二次型的性質，類似內積 $\langle x,y\rangle$ 和範數平方 $\|x\|^2$。

**具體例子**【口頭】[▶ 18:17](https://youtu.be/YESsX40YL1c?t=1097)：$E=\mathbb{R}^n$，$\varphi(x,y)=x\cdot y$，相伴的二次型是

$$\Phi(x)=x\cdot x=x_1^2+x_2^2+\cdots+x_n^2,$$

是座標的**齊次多項式**（每一項都是二次），所以叫「二次型」。

---

## 4. 極化恆等式與它的推論

[▶ 19:21](https://youtu.be/YESsX40YL1c?t=1161) 課本 Theorem 4.3.7。

**極化恆等式（polarization identity）**：

$$4\varphi(x,y)=\Phi(x+y)-\Phi(x-y)+i\Phi(x+iy)-i\Phi(x-iy). \tag{4.2}$$

講者覺得這跟「1-範數不能由內積誘導」那件事有關，但細節他一時想不起來。

> 以下**不是逐字稿內容**，是補上那個關聯：把 (4.2) 用在內積上，得 $\langle x,y\rangle=\frac14\left(\|x+y\|^2-\|x-y\|^2+i\|x+iy\|^2-i\|x-iy\|^2\right)$：內積可以**從範數算回來**。所以如果一個範數來自內積，內積只能是這個公式；而這個公式定義出的東西是內積，若且唯若範數滿足平行四邊形定律（第 18 集）。

講者說 p. 153 的證明很清楚：寫出

$$\Phi(\alpha x+\beta y)=|\alpha|^2\Phi(x)+\alpha\bar\beta\varphi(x,y)+\bar\alpha\beta\varphi(y,x)+|\beta|^2\Phi(y),$$

分別代 $(\alpha,\beta)=(1,1),(1,-1),(1,i),(1,-i)$，乘上 $1,-1,i,-i$ 相加，除了四份 $\varphi(x,y)$ 之外全部消掉。

### Corollary 4.3.8

[▶ 21:23](https://youtu.be/YESsX40YL1c?t=1283)

**推論**：若 $\varphi_1(x,x)=\varphi_2(x,x)$ 對**所有** $x$，則 $\varphi_1=\varphi_2$。同樣，若 $\langle Ax,x\rangle=\langle Bx,x\rangle$ 對所有 $x$，則 $A=B$。

講者強調「對所有 $x$」很重要；只對某個 $x$ 成立說明不了什麼。

**第一部分**[▶ 22:37](https://youtu.be/YESsX40YL1c?t=1357)：二次型相等，代入極化恆等式，$\varphi_1(x,y)=\frac14(\Phi_1\text{ 的組合})=\frac14(\Phi_2\text{ 的組合})=\varphi_2(x,y)$。講者：「這個論證的美在於完全不依賴座標，所以可能是無限維。」

**算子的部分**【課堂討論】[▶ 25:45](https://youtu.be/YESsX40YL1c?t=1545)：課本令 $\varphi_1(x,y)=\langle Ax,y\rangle$、$\varphi_2(x,y)=\langle Bx,y\rangle$。由第一部分 $\langle Ax,y\rangle=\langle Bx,y\rangle$ 對所有 $x,y$。講者卡在「為什麼這就推出 $A=B$」：他先想用正規正交基底展開（有限維或可分空間可以），又擔心課本從沒保證任意 Hilbert 空間都有正規正交基底，「也許這是書的盔甲上的一道縫」。他改寫成 $\langle(A-B)x,y\rangle=0$ 對所有 $y$，說「這表示 $(A-B)x$ 跟所有 $y$ 都垂直，應該推出它是 0」，然後想找第 3 章的相關定理。最後說：「我在這上面拖太久了，往下走。」[▶ 37:28](https://youtu.be/YESsX40YL1c?t=2248)

> 以下**不是逐字稿內容**，是補上那一步：不需要基底。取 $y=(A-B)x$：$\|(A-B)x\|^2=\langle(A-B)x,(A-B)x\rangle=0$，所以 $(A-B)x=0$ 對每個 $x$，$A=B$。（這就是第 23 集的 $E^\perp=\{0\}$。）

---

## 5. 對稱 ⟺ 二次型是實的；範數的關係

[▶ 38:35](https://youtu.be/YESsX40YL1c?t=2315)

**Theorem 4.3.9**：雙線性泛函 $\varphi$ 對稱 ⟺ 相伴的二次型 $\Phi$ 是實值的。

講者說（⟹）幾乎一眼看出：$\overline{\Phi(x)}=\overline{\varphi(x,x)}=\varphi(x,x)=\Phi(x)$（對稱），等於自己的共軛就是實數。

【課本補充】（⟸）：令 $\psi(x,y)=\overline{\varphi(y,x)}$，它的二次型是 $\overline{\Phi}=\Phi$；由 Corollary 4.3.8，$\psi=\varphi$，即對稱。

**Theorem 4.3.10**[▶ 39:47](https://youtu.be/YESsX40YL1c?t=2387)：$\varphi$ 有界 ⟺ $\Phi$ 有界，而且

$$\|\Phi\|\le\|\varphi\|\le2\|\Phi\|. \tag{4.3}$$

講者：又是極化恆等式配三角不等式（課本還用了平行四邊形定律）。

**Theorem 4.3.11**[▶ 40:54](https://youtu.be/YESsX40YL1c?t=2454)：若 $\varphi$ 對稱且有界，則 $\|\varphi\|=\|\Phi\|$。

---

## 6. ⟨Ax,y⟩ 的範數就是 ‖A‖

[▶ 41:25](https://youtu.be/YESsX40YL1c?t=2485) 課本 Theorem 4.3.12。

**定理**：$A$ 是 Hilbert 空間上的有界算子，則 $\varphi(x,y)=\langle Ax,y\rangle$ 是有界雙線性泛函，而且 $\|A\|=\|\varphi\|$。

講者放慢速度證這個。

**$\|\varphi\|\le\|A\|$**[▶ 42:52](https://youtu.be/YESsX40YL1c?t=2572)：由 Schwarz，

$$|\varphi(x,y)|=|\langle Ax,y\rangle|\le\|Ax\|\|y\|\le\|A\|\|x\|\|y\|.$$

第二步是算子範數的性質 $\|Ax\|\le\|A\|\|x\|$（不是等號）。

**$\|A\|\le\|\varphi\|$**[▶ 44:44](https://youtu.be/YESsX40YL1c?t=2684)：代 $y=Ax$：

$$\|Ax\|^2=\langle Ax,Ax\rangle=\varphi(x,Ax)\le\|\varphi\|\|x\|\|Ax\|.$$

$Ax\ne0$ 時兩邊除以 $\|Ax\|$：$\|Ax\|\le\|\varphi\|\|x\|$；$Ax=0$ 時顯然。所以 $\|A\|\le\|\varphi\|$。∎

講者：「我以為會更有趣……我得承認，如果上課前不吃點東西，講到這裡就會很吃力。」[▶ 48:01](https://youtu.be/YESsX40YL1c?t=2881)

---

## 7. 每個有界雙線性泛函都是 ⟨x,Ay⟩

[▶ 49:26](https://youtu.be/YESsX40YL1c?t=2966) 課本 Theorem 4.3.13。

**定理**：$\varphi$ 是 Hilbert 空間 $H$ 上的有界雙線性泛函。則存在**唯一**的有界算子 $A$ 使

$$\varphi(x,y)=\langle x,Ay\rangle\quad\text{對所有 }x,y\in H.$$

講者：這是 Riesz 表示定理的「下一層」：Riesz 是線性泛函 $f(x)=\langle x,x_0\rangle$；這裡是雙線性泛函。課本的證明（約一頁，步驟直接）就從 Riesz 表示定理出發。

【課本補充】證明概要：固定 $y$，$x\mapsto\varphi(x,y)$ 是有界線性泛函，由 Riesz，有唯一的 $Ay$ 使 $\varphi(x,y)=\langle x,Ay\rangle$。$y\mapsto Ay$ 線性（由 $\varphi$ 第二位置的共軛線性和內積第二位置的共軛線性抵消）；有界：取 $x=Ay$，$\|Ay\|^2=\varphi(Ay,y)\le k\|Ay\|\|y\|$。唯一：$\langle x,Ay\rangle=\langle x,By\rangle$ ∀$x,y$ ⟹ $A=B$。

---

## 8. 強制性與 Lax–Milgram 定理

[▶ 51:35](https://youtu.be/YESsX40YL1c?t=3095) 課本 Definition 4.3.14、Theorem 4.3.16。

**強制（coercive，或 elliptic）**：存在 $K>0$ 使

$$\varphi(x,x)\ge K\|x\|^2\quad\text{對所有 }x.$$

講者：「我不記得聽過這個詞，不過我過著與世隔絕的生活。」

【課本補充】Example 4.3.15：$z$ 是 $[0,1]$ 上的連續實函數，$\min z>0$，則 $\varphi(x,y)=\int_0^1x\bar yz$ 在 $L^2([0,1])$ 上是強制的，$K=\min z$。（這就是第 19 集的加權內積。）

**Lax–Milgram 定理**[▶ 53:28](https://youtu.be/YESsX40YL1c?t=3208)（P. Lax、A. N. Milgram，1954）：$\varphi$ 是 Hilbert 空間 $H$ 上**有界、強制**的雙線性泛函。則對每個 $H$ 上的有界線性泛函 $f$，存在**唯一**的 $x_f\in H$ 使

$$f(x)=\varphi(x,x_f)\quad\text{對所有 }x\in H.$$

講者【口頭】[▶ 55:56](https://youtu.be/YESsX40YL1c?t=3356)：取 $\varphi=$ 內積，這就是 Riesz 表示定理。所以這個定理是說：有界、強制的雙線性泛函，至少在 Riesz 表示定理這方面，表現得**像內積**。證明大部分直接，最後有個反證，「有點狡猾」。課本說它對邊界值問題的應用在第 6 章。

【課本補充】證明概要：

1. 由 Theorem 4.3.13，$\varphi(x,y)=\langle x,Ay\rangle$。
2. 強制：$K\|x\|^2\le\varphi(x,x)=\langle x,Ax\rangle\le\|x\|\|Ax\|$，所以 $\|Ax\|\ge K\|x\|$。這推出 $A$ **一對一**。
3. **值域閉**：若 $Ax_n\to y$，則 $\|x_n-x_m\|\le\frac1K\|Ax_n-Ax_m\|\to0$，Cauchy，$x_n\to x$，$Ax=y$。
4. **值域是全部**：若不是，由正交分解有非零 $x\perp\mathcal R(A)$，則 $0=\langle x,Ax\rangle=\varphi(x,x)\ge K\|x\|^2$，矛盾。
5. 由 Riesz，$f(x)=\langle x,x_0\rangle$；$A$ 是雙射，取 $x_f=A^{-1}x_0$，得 $f(x)=\langle x,Ax_f\rangle=\varphi(x,x_f)$。

講者也補充：Riesz 型的表示要求泛函有界；若泛函無界卻有這種表示，就會推出它有界，矛盾。[▶ 56:30](https://youtu.be/YESsX40YL1c?t=3390)

---

## 9. 伴隨算子

[▶ 57:34](https://youtu.be/YESsX40YL1c?t=3454) 課本 Definition 4.4.1。

由 Theorem 4.3.12，$\varphi(x,y)=\langle Ax,y\rangle$ 有界；由 Theorem 4.3.13，有唯一的有界算子 $A^*$ 使 $\langle Ax,y\rangle=\langle x,A^*y\rangle$。

**定義**：$A$ 是 Hilbert 空間 $H$ 上的有界算子。$A^*:H\to H$ 由

$$\langle Ax,y\rangle=\langle x,A^*y\rangle\quad\text{對所有 }x,y\in H$$

定義，叫 $A$ 的**伴隨算子（adjoint operator）**，也叫 **Hilbert 伴隨**。

**在 $\mathbb{C}^n$ 中**[▶ part 2 00:37](https://youtu.be/uqszOPtXFFQ?t=37)：內積 $\langle x,y\rangle=x^T\bar y$。

$$\langle Ax,y\rangle=(Ax)^T\bar y=x^TA^T\bar y,\qquad\langle x,A^*y\rangle=x^T\overline{A^*y}=x^T\overline{A^*}\,\bar y.$$

對所有 $x,y$ 相等，所以 $A^T=\overline{A^*}$，即

$$A^*=\overline{A}^T\quad(\text{共軛轉置}).$$

講者：這就是 **Hermitian 伴隨**，物理裡寫成 $A^\dagger$。

【課本補充】性質：$(A+B)^*=A^*+B^*$，$(\alpha A)^*=\bar\alpha A^*$，$(A^*)^*=A$，$I^*=I$，$(AB)^*=B^*A^*$。

### Theorem 4.4.2：$\|A^*\|=\|A\|$

[▶ part 2 01:46](https://youtu.be/uqszOPtXFFQ?t=106)

**定理**：有界算子的伴隨也有界，而且 $\|A\|=\|A^*\|$、$\|A^*A\|=\|A\|^2$。

講者的論證：$\|Ax\|=\sqrt{\langle Ax,Ax\rangle}=\sqrt{\langle x,A^*Ax\rangle}$，然後說「這基本上跟 $\sup\|A^*x\|$ 一樣」，所以兩個範數相等。

> 以下**不是逐字稿內容**，是依數學推論的修正：$\|Ax\|=\|A^*x\|$ 對每個 $x$ **一般不成立**——那正是下一集「正規算子」的定義。例如 $A(z_1,z_2)=(0,z_1)$：$A^*(z_1,z_2)=(z_2,0)$，$\|Ae_1\|=1$ 但 $\|A^*e_1\|=0$。不過 $\|A\|=\|A^*\|$（兩個上確界）仍然對。
>
> 【課本補充】課本的證法：$\langle Ax,y\rangle$ 和 $\langle x,A^*y\rangle$ 是**同一個**雙線性泛函，由 Theorem 4.3.12（及其 $\langle x,Ay\rangle$ 版本）兩者的範數都等於它的範數，所以 $\|A\|=\|A^*\|$。
>
> **$\|A^*A\|=\|A\|^2$**：$\le$ 由 $\|A^*A\|\le\|A^*\|\|A\|=\|A\|^2$；$\ge$ 由 $\|Ax\|^2=\langle A^*Ax,x\rangle\le\|A^*A\|\|x\|^2$。

講者說 $\|A^*A\|=\|A\|^2$ 也能類似地算出來。

【課本補充】$A$ 和 $A^*$ 不必相等：上面的 $A(z_1,z_2)=(0,z_1)$ 就是。$A=A^*$ 的算子叫**自伴（self-adjoint）**——下一集。

---

## 10. 預告

【口頭】[▶ part 2 06:37](https://youtu.be/uqszOPtXFFQ?t=397)

- **自伴算子**：「對稱」的複數版本（實的情形伴隨就是轉置）。例子：Fredholm 算子等。
- **Theorem 4.4.13**：每個有界算子 $T$ 可唯一寫成 $T=A+iB$、$T^*=A-iB$，$A,B$ 自伴——「實部、虛部」的類比。
- **§4.5**：正規、等距、么正算子，講者會摘要重點。
- **§4.6 正算子**：大概跳過。那節本質上在問「算子的平方根是什麼、什麼時候有意義」（線代裡問矩陣的平方根）。
- **§4.7 投影算子**：比較重要。
- **§4.8 緊緻算子**：講者在想哪些節可以跳過而不太傷害課程。
- **§4.9 本徵值、本徵向量**：一定要講，跟有限維有很有趣的差異：無限維空間的算子不能取**行列式**，那怎麼刻畫退化？
- **§4.10 譜分解**。之後（或中間）講分離變數、邊界值問題。

---

## 11. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 雙線性泛函 | 第一位置線性、第二位置共軛線性 | 例：$\langle x,y\rangle$、$\langle Ax,y\rangle$、$f(x)\overline{g(y)}$ |
| 有界 | $|\varphi(x,y)|\le K\|x\|\|y\|$，$\|\varphi\|=\sup_{\|x\|=\|y\|=1}|\varphi|$ | 內積的範數 = 1 |
| 二次型 | $\Phi(x)=\varphi(x,x)$ | $\mathbb{R}^n$：$\sum x_i^2$ |
| 極化 | $4\varphi(x,y)=\Phi(x+y)-\Phi(x-y)+i\Phi(x+iy)-i\Phi(x-iy)$ | 代 $\beta=\pm1,\pm i$ |
| 推論 | $\Phi_1=\Phi_2$ ⟹ $\varphi_1=\varphi_2$；$\langle Ax,x\rangle=\langle Bx,x\rangle$ ∀$x$ ⟹ $A=B$ | 取 $y=(A-B)x$ |
| 對稱 | ⟺ $\Phi$ 實值 | |
| 範數 | $\|\Phi\|\le\|\varphi\|\le2\|\Phi\|$；對稱時相等 | 極化 + 平行四邊形 |
| $\langle Ax,y\rangle$ | $\|\varphi\|=\|A\|$ | 代 $y=Ax$ |
| 表示 | 有界 $\varphi$ ⟹ $\varphi(x,y)=\langle x,Ay\rangle$ | 對固定 $y$ 用 Riesz |
| 強制 | $\varphi(x,x)\ge K\|x\|^2$ | |
| Lax–Milgram | 有界強制 $\varphi$：$f(x)=\varphi(x,x_f)$，唯一 | $\|Ax\|\ge K\|x\|$，值域閉且稠密 |
| 伴隨 | $\langle Ax,y\rangle=\langle x,A^*y\rangle$ | $\mathbb{C}^n$：$A^*=\bar A^T$ |
| 伴隨範數 | $\|A^*\|=\|A\|$，$\|A^*A\|=\|A\|^2$ | 同一個雙線性泛函 |

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 自伴算子、$T=A+iB$ | 第 26 集 |
| $\langle Ax,x\rangle$ 決定 $A$ | 第 26 集：自伴 ⟺ $\langle Ax,x\rangle$ 實；正規 ⟺ $\|Ax\|=\|A^*x\|$ |
| $\|A^*A\|=\|A\|^2$ | $C^*$-代數（課本沒談） |
| Lax–Milgram | 課本 §6.5：橢圓邊界值問題的弱解 |
| Hermitian 伴隨 $A^\dagger$ | 第 33–34 集：量子力學的可觀測量 |

---

## 附：本集一句話總結

> **雙線性泛函是內積的推廣，二次型是範數平方的推廣，極化恆等式讓二次型完全決定雙線性泛函；在 Hilbert 空間裡，每個有界雙線性泛函都是 $\langle x,Ay\rangle$（Riesz 的下一層），強制的還能像內積一樣表示所有有界泛函（Lax–Milgram）；由此定義的伴隨 $\langle Ax,y\rangle=\langle x,A^*y\rangle$，在 $\mathbb{C}^n$ 上就是共軛轉置，而且 $\|A^*\|=\|A\|$。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-24 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 9:58）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §4.3–4.4 整理。*
