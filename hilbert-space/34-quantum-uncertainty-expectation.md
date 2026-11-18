---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 34
lecture: Lecture 34
date: 2023-05-01
video: https://youtu.be/UoY6aVpChU0 （part 1，音質差）、https://youtu.be/JnnGNls8_bc （part 2）、https://youtu.be/2gXOCTH1w0c （part 3）、https://youtu.be/2TlLc6epCHY （part 4）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §7.3（後半）–7.4（書頁 369–378，PDF 頁 388–397）
---

# 第 34 集 · 對易子、期望值、測量假設與測不準原理 [▶ 影片](https://youtu.be/UoY6aVpChU0)

← 上一集：[33-classical-quantum-mechanics](33-classical-quantum-mechanics.md) ｜ [總目錄](README.md) ｜ 下一集：（本系列最後一集）

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 34 集
> **講者**：James Cook（⚠️ 待確認，見第 01 集）
> **來源**：YouTube 自動字幕逐字稿（part 1 約 17:40，教室外很吵；part 2 約 59:50；part 3 約 4:10；part 4 約 14:20）＋ Debnath & Mikusiński §7.3–7.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例一：$[\hat x,\hat p]=i\hbar$](#1-例一hat-xhat-pihbar)
- [2. 例二、例三：動量與 Hamiltonian](#2-例二例三動量與-hamiltonian)
- [3. 本徵基底與時間](#3-本徵基底與時間)
- [4. 假設 III：對應原理](#4-假設-iii對應原理)
- [5. 假設 IV：量子化](#5-假設-iv量子化)
- [6. 期望值與均方根偏差](#6-期望值與均方根偏差)
- [7. Theorem 7.3.3](#7-theorem-733)
- [8. Theorem 7.3.4：偏差為 0 ⟺ 本徵態](#8-theorem-734偏差為-0--本徵態)
- [9. 用本徵基底算期望值：機率詮釋](#9-用本徵基底算期望值機率詮釋)
- [10. 假設 V：測量結果](#10-假設-v測量結果)
- [11. 測不準原理](#11-測不準原理)
- [12. 一頁速查表](#12-一頁速查表)
- [13. 與前面集數的連結](#13-與前面集數的連結)

---

## 0. 這堂課要做什麼

接著課本 p. 369 往下讀。講者先做幾個對易子的計算，「讓這堂課有個重心」，再讀完 §7.3 的假設和期望值，最後到 §7.4 的 Heisenberg 測不準原理。[▶ 00:06](https://youtu.be/UoY6aVpChU0?t=6)

| 主題 | 課本位置 |
|---|---|
| $[\hat x,\hat p]$、動量與 Hamiltonian 的對易子 | (7.65) 附近，p. 372 |
| 本徵基底、時間依賴 | (7.60)–(7.62)，pp. 369–370 |
| 假設 III（對應原理）、Table 7.1 | p. 371 |
| 假設 IV（量子化） | (7.63)–(7.66)，p. 372 |
| 期望值、均方根偏差 | Definition 7.3.1–7.3.2，(7.67)–(7.69)，p. 373 |
| Theorem 7.3.3、7.3.4 | pp. 373–374 |
| 機率詮釋、假設 V | (7.74)–(7.81)，pp. 375–376 |
| 測不準原理 | Theorem 7.4.1、Corollary 7.4.2，pp. 377–378 |

【口頭】part 1 錄音時是學期倒數第二天，教室外一直有人大吵大叫，講者多次抱怨。

---

## 1. 例一：$[\hat x,\hat p]=i\hbar$

[▶ 00:38](https://youtu.be/UoY6aVpChU0?t=38)

**算子**（一維）：
$$\hat x\psi=x\psi,\qquad\hat p=-i\hbar\frac{\partial}{\partial x},\qquad\hbar=\frac{h}{2\pi}\ (h\text{ 是 Planck 常數}).$$

【口頭】課本沒真正解釋**為什麼**動量是 $-i\hbar\partial_x$。講者說從 Fourier 分析的角度看這有點自然：Fourier 變換把微分變成乘法（第 31 集），位置與動量之間也有類似的互動。[▶ 01:12](https://youtu.be/UoY6aVpChU0?t=72)

【口頭】課本前面有各種算子（積分算子、平移算子……），但一到量子力學章節，可觀測量幾乎只有兩類：**乘法算子**和**微分算子**，以及它們的線性組合（Dirac δ 之後也會出現）。[▶ 02:25](https://youtu.be/UoY6aVpChU0?t=145)

**計算**：作用在任意 $\psi$ 上。[▶ 02:58](https://youtu.be/UoY6aVpChU0?t=178)
$$[\hat x,\hat p]\psi=\hat x\hat p\psi-\hat p\hat x\psi .$$
- 第一項：$\hat x\hat p\psi=x\left(-i\hbar\frac{\partial\psi}{\partial x}\right)=-i\hbar x\frac{\partial\psi}{\partial x}$。
- 第二項用乘積法則：$\hat p\hat x\psi=-i\hbar\frac{\partial}{\partial x}(x\psi)=-i\hbar\psi-i\hbar x\frac{\partial\psi}{\partial x}$。

相減：
$$[\hat x,\hat p]\psi=-i\hbar x\psi'+i\hbar\psi+i\hbar x\psi'=i\hbar\psi .$$
（講者說：中間的 $+$ 號來自「對易子的負號」乘「$\hat p$ 定義裡的負號」，含 $\psi'$ 的兩項抵消。）[▶ 05:45](https://youtu.be/UoY6aVpChU0?t=345)

對所有 $\psi$ 成立，所以
$$\boxed{[\hat x,\hat p]=i\hbar}$$
位置和動量**不對易**。

【課堂討論】有人問 $\hbar$ 是不是 $h/2\pi$。講者：是；物理裡「字母加一槓」一般就表示除以 $2\pi$。[▶ 04:36](https://youtu.be/UoY6aVpChU0?t=276)

---

## 2. 例二、例三：動量與 Hamiltonian

**例二**：動能 $\hat T=\dfrac{\hat p^2}{2m}$（三維是 $\frac1{2m}(\hat p_x^2+\hat p_y^2+\hat p_z^2)$）。[▶ 06:21](https://youtu.be/UoY6aVpChU0?t=381)
$$[\hat T,\hat p]=0 .$$
理由：$\hat T$ 是 $\hat p$ 的多項式，$\hat p$ 和自己對易。

**自由粒子**：位能 $V=0$，所以 $\hat H=\hat T$，Hamiltonian 和動量對易。[▶ 08:39](https://youtu.be/UoY6aVpChU0?t=519) Hamiltonian 的本徵值叫能量；所以自由粒子可以有**同時**是能量本徵態和動量本徵態的狀態。

**例三**：有位能時，$\hat H=\hat T+\hat V$，其中 $\hat V\psi=V(x)\psi$ 是乘法算子。[▶ 09:47](https://youtu.be/UoY6aVpChU0?t=587)
$$[\hat p,\hat H]=[\hat p,\hat T]+[\hat p,\hat V]=0+[\hat p,\hat V].$$
作用在 $\psi$ 上，再用一次乘積法則：[▶ 11:28](https://youtu.be/UoY6aVpChU0?t=688)
$$[\hat p,\hat V]\psi=-i\hbar\frac{\partial}{\partial x}(V\psi)+i\hbar V\frac{\partial\psi}{\partial x}=-i\hbar\frac{\partial V}{\partial x}\psi-i\hbar V\psi'+i\hbar V\psi'=-i\hbar\frac{\partial V}{\partial x}\psi .$$
所以
$$[\hat p,\hat H]=-i\hbar\frac{\partial V}{\partial x}.$$
一般不是 0（除非 $V$ 是常數，那就乾脆取成 0）。[▶ 12:36](https://youtu.be/UoY6aVpChU0?t=756)

**結論**：在位能場中運動的粒子，動量和能量不能同時精確決定。要同時對角化，兩個可觀測量的對易子必須是 0（第 33 集）。

---

## 3. 本徵基底與時間

[▶ 13:45](https://youtu.be/UoY6aVpChU0?t=825)

**假設 II 的第三個推論**：一個可觀測量屬於不同本徵值的本徵向量形成**完備正規正交組**：
$$\langle\psi_n|\psi_m\rangle=\int_{-\infty}^{\infty}\overline{\psi_n(x)}\,\psi_m(x)\,dx=\delta_{nm},\qquad\psi(x)=\sum_{n=1}^\infty\langle\psi_n|\psi\rangle\,\psi_n(x).\tag{7.60}$$
這組 $\{\psi_n\}$ 叫可觀測量 $\hat A$ 的**本徵基底**（eigenbasis），$\hat A\psi_n=\lambda_n\psi_n$。

【口頭】講者說 Griffiths 那種量子力學入門課「反覆強調到令人厭煩」的就是這點：物理系的人覺得很怪——用**另一個**物理問題的本徵態當基底，來解這個問題。但數學上「這只是完備正規正交系統在發揮作用」。[▶ 14:19](https://youtu.be/UoY6aVpChU0?t=859)

【口頭】講者更正自己：$\psi(x)$ 該叫「狀態向量」，不是「波函數」；波函數 $\Psi(x,t)$ 帶時間。[▶ 16:27](https://youtu.be/UoY6aVpChU0?t=987)

**時間的角色**（part 2 開始）：[▶ part 2 00:02](https://youtu.be/JnnGNls8_bc?t=2)
- 古典力學：狀態和可觀測量都隨時間變。
- 量子力學：狀態（波函數）$\Psi(x,t)$ 隨時間變；但可觀測量 $\hat A$、它的本徵基底 $\{\psi_n\}$、本徵值 $\{\lambda_n\}$ 都**和時間無關**。
- 所以展開 $\Psi(x,t)=\sum_n\langle\psi_n|\Psi\rangle\psi_n(x)$ 裡，時間全部落在係數上：
$$\langle\psi_n|\Psi\rangle=\int_{-\infty}^{\infty}\overline{\psi_n(x)}\,\Psi(x,t)\,dx\quad(\text{隨時間變的純量}).\tag{7.62}$$

【口頭】「別想太深，這些大部分只是在定記號。」課本也提醒：$\hat A,\psi_n,\lambda_n$ 不隨時間變，不代表**量到的值**不隨時間變。[▶ part 2 01:43](https://youtu.be/JnnGNls8_bc?t=103)

---

## 4. 假設 III：對應原理

[▶ part 2 02:51](https://youtu.be/JnnGNls8_bc?t=171)

【口頭】課本的觀點是「古典力學是基礎，對它做些什麼就得到量子力學」。講者說不是所有物理學家都同意：有些理論物理學家認為量子力學才是基本的。所以量子力學裡有沒有古典對應的東西（例如自旋）並不是問題。但很多東西有對應，而這段對應至少在歷史上很重要。[▶ part 2 03:24](https://youtu.be/JnnGNls8_bc?t=204)

**Table 7.1（節錄）**：[▶ part 2 04:39](https://youtu.be/JnnGNls8_bc?t=279)

| 可觀測量 | 古典 | 量子算子 |
|---|---|---|
| 位置 | $x$ 或 $\mathbf r$ | $\hat x$ 或 $\hat{\mathbf r}$ |
| 線動量 | $p_x=m\dot x$ | $\hat p_x=-i\hbar\dfrac{\partial}{\partial x}$ |
| 線動量（向量） | $\mathbf p=(p_x,p_y,p_z)$ | $\hat{\mathbf p}=-i\hbar\nabla=-i\hbar\left(\partial_x,\partial_y,\partial_z\right)$ |
| 動能 | $T=\dfrac{p^2}{2m}$ | $\hat T=\dfrac{\hat p^2}{2m}=-\dfrac{\hbar^2}{2m}\nabla^2$ |
| Hamiltonian | $H=\dfrac{p^2}{2m}+V(x)$ | $\hat H=-\dfrac{\hbar^2}{2m}\nabla^2+\hat V(\hat x)$ |

（課本表中還有位能和角動量。）講者又說：「課本還是沒解釋為什麼動量是這樣。」

【Q&A】一位學生問：量子的動量算子裡沒有質量，是不是「失去了質量」？[▶ part 2 06:26](https://youtu.be/JnnGNls8_bc?t=386) 討論後的說法：這些是算子，質量包在那個粒子的本徵函數（狀態）裡。

**Postulate III（對應原理，Correspondence Principle）**：對應某個動力學變數的量子可觀測量算子，是把古典力學中的正則變數換成對應的量子算子得到的。[▶ part 2 09:26](https://youtu.be/JnnGNls8_bc?t=566) 這可追溯到 Niels Bohr。課本也承認自旋、同位旋這類東西沒有古典對應。

---

## 5. 假設 IV：量子化

[▶ part 2 10:31](https://youtu.be/JnnGNls8_bc?t=631)

**Postulate IV（量子化）**：每一對正則共軛的可觀測量算子滿足 Heisenberg 對易關係
$$[\hat q_m,\hat q_n]=0=[\hat p_m,\hat p_n],\qquad[\hat q_m,\hat p_n]=i\hbar\,\delta_{mn}.\tag{7.63, 7.64}$$

講者說今天的例一就是這條的特例。「正則共軛」指的是 Lagrangian 力學裡的廣義座標 $q$ 和廣義動量 $p=\partial L/\partial\dot q$ 這種配對（第 33 集）。[▶ part 2 11:04](https://youtu.be/JnnGNls8_bc?t=664)

【課本補充】角動量的對易關係（講者說「有趣，但不確定和現在的討論有什麼關係」）：
$$[\hat L_x,\hat L_y]=i\hbar\hat L_z,\quad[\hat L_y,\hat L_z]=i\hbar\hat L_x,\quad[\hat L_z,\hat L_x]=i\hbar\hat L_y .\tag{7.66}$$

---

## 6. 期望值與均方根偏差

[▶ part 2 12:14](https://youtu.be/JnnGNls8_bc?t=734)

課本的想法：
- 由假設 II，能量到的只有本徵值；量到哪一個，要由測量時的狀態決定。
- 但測量通常會影響系統，所以幾乎不可能確定地預測單次測量。
- 解法：在相同條件下做很多次測量，取平均。這個平均叫**期望值**（expectation value）。

**Definition 7.3.1**：可觀測量 $\hat A$ 在狀態 $\psi$ 的期望值是[▶ part 2 14:58](https://youtu.be/JnnGNls8_bc?t=898)
$$\langle\hat A\rangle=\frac{\langle\psi|\hat A\psi\rangle}{\langle\psi|\psi\rangle};\qquad\text{若 }\psi\text{ 已歸一化，}\langle\hat A\rangle=\langle\psi|\hat A\psi\rangle .\tag{7.67, 7.68}$$

【口頭】角括號被用在太多地方了，要很仔細跟記號。他也開玩笑：叫「可觀測量的期望值」，難道還有不可觀測的算子？[▶ part 2 13:52](https://youtu.be/JnnGNls8_bc?t=832)

**Definition 7.3.2（均方根偏差）**：$(\nabla\hat A)$ 是 $\left(\hat A-\langle\hat A\rangle\right)^2$ 在狀態 $\psi$ 中期望值的**平方根**。[▶ part 2 15:35](https://youtu.be/JnnGNls8_bc?t=935)
$$(\nabla\hat A)^2=\left\langle\left(\hat A-\langle\hat A\rangle\right)^2\right\rangle .$$

【口頭】「他為什麼不直接叫標準差？」講者一開始漏看了「平方根」兩個字，被學生提醒後改正。[▶ part 2 17:12](https://youtu.be/JnnGNls8_bc?t=1032)

**(7.69) 的推導**（設 $\psi$ 歸一化）：[▶ part 2 21:06](https://youtu.be/JnnGNls8_bc?t=1266)
$$(\nabla\hat A)^2=\left\langle\psi\middle|\left(\hat A-\langle\hat A\rangle\right)^2\psi\right\rangle=\left\langle\left(\hat A-\langle\hat A\rangle\right)\psi\middle|\left(\hat A-\langle\hat A\rangle\right)\psi\right\rangle=\left\|\left(\hat A-\langle\hat A\rangle\right)\psi\right\|^2 .$$
中間那步把一個 $\left(\hat A-\langle\hat A\rangle\right)$ 從右邊搬到左邊，理由有兩個：
- $\hat A$ 是 Hermitian：$\langle\hat A\psi|\varphi\rangle=\langle\psi|\hat A\varphi\rangle$；
- $\langle\hat A\rangle$ 是**實數**（Hermitian 的期望值是實的），所以它搬過去不用取共軛。

（算子的平方就是合成兩次。）

【Q&A】學生問：課本是不是突然假設 $\psi$ 已歸一化了？[▶ part 2 24:42](https://youtu.be/JnnGNls8_bc?t=1482) 討論結論：必須歸一化，否則這些公式不成立，也得不到合理的期望值和機率。講者先說可能是編輯疏失，後來又說可能是課本前面說過、他自己忘了。

---

## 7. Theorem 7.3.3

[▶ part 2 23:23](https://youtu.be/JnnGNls8_bc?t=1403)

**Theorem 7.3.3**（$\psi$ 歸一化）：
$$\text{(a)}\ (\nabla\hat A)^2=\langle\hat A^2\rangle-\langle\hat A\rangle^2,\qquad\text{(b)}\ \langle\hat A^2\rangle=\|\hat A\psi\|^2 .$$

**(a) 的證明**：[▶ part 2 26:55](https://youtu.be/JnnGNls8_bc?t=1615)
$$\begin{aligned}
(\nabla\hat A)^2&=\left\langle\psi\middle|\left(\hat A^2-2\langle\hat A\rangle\hat A+\langle\hat A\rangle^2\right)\psi\right\rangle\\
&=\langle\psi|\hat A^2\psi\rangle-2\langle\hat A\rangle\langle\psi|\hat A\psi\rangle+\langle\hat A\rangle^2\langle\psi|\psi\rangle\\
&=\langle\hat A^2\rangle-2\langle\hat A\rangle^2+\langle\hat A\rangle^2\qquad(\langle\psi|\psi\rangle=1)\\
&=\langle\hat A^2\rangle-\langle\hat A\rangle^2 .
\end{aligned}$$
第二行用線性，並把實數 $\langle\hat A\rangle$ 提出來。

【口頭】講者很想把 $\langle\hat A\rangle$ 寫成 $\bar A$：「要是我出考題，一定換個記號，寫起來太長，而且和別的東西長得太像。」[▶ part 2 27:29](https://youtu.be/JnnGNls8_bc?t=1649)

【課堂討論】講者問這是不是變異數（variance）；學生說是，開根號就是標準差。[▶ part 2 29:39](https://youtu.be/JnnGNls8_bc?t=1779)

**(b) 的證明**：$\langle\hat A^2\rangle=\langle\psi|\hat A\hat A\psi\rangle=\langle\hat A\psi|\hat A\psi\rangle=\|\hat A\psi\|^2$（Hermitian）。[▶ part 2 30:09](https://youtu.be/JnnGNls8_bc?t=1809)

---

## 8. Theorem 7.3.4：偏差為 0 ⟺ 本徵態

[▶ part 2 30:49](https://youtu.be/JnnGNls8_bc?t=1849)

**Theorem 7.3.4**：系統處於可觀測量 $\hat A$ 的本徵態 ⟺ $\nabla\hat A=0$。

**(⟹)**：設 $\hat A\psi=\lambda\psi$（$\lambda$ 實數，$\psi$ 歸一化）。[▶ part 2 32:04](https://youtu.be/JnnGNls8_bc?t=1924)
$$\langle\hat A\rangle=\langle\psi|\lambda\psi\rangle=\lambda,\qquad\langle\hat A^2\rangle=\|\hat A\psi\|^2=\|\lambda\psi\|^2=\lambda^2 .$$
由 7.3.3(a)：$(\nabla\hat A)^2=\lambda^2-\lambda^2=0$。

**(⟸)**：課堂上講者和學生在這裡卡了好幾分鐘，最後發現答案就在 (7.69)：[▶ part 2 34:37](https://youtu.be/JnnGNls8_bc?t=2077)
$$0=(\nabla\hat A)^2=\left\|\left(\hat A-\langle\hat A\rangle\right)\psi\right\|^2 .$$
範數為 0 ⟹ 向量是 0：
$$\left(\hat A-\langle\hat A\rangle\right)\psi=0\quad\Longrightarrow\quad\hat A\psi=\langle\hat A\rangle\,\psi .$$
這正是本徵值方程，本徵值是 $\langle\hat A\rangle$（$\psi\ne0$ 因為它已歸一化）。[▶ part 2 40:35](https://youtu.be/JnnGNls8_bc?t=2435)

【口頭】「抱歉，我在這個相當無聊的點上吃掉了一大堆時間。」

---

## 9. 用本徵基底算期望值：機率詮釋

[▶ part 2 41:44](https://youtu.be/JnnGNls8_bc?t=2504)

**情形一**：$\psi_n$ 是本徵向量，$\hat A\psi_n=\lambda_n\psi_n$。則
$$\langle\hat A\rangle=\frac{\langle\psi_n|\hat A\psi_n\rangle}{\langle\psi_n|\psi_n\rangle}=\lambda_n .$$
【課堂討論】學生指出：不管 $\psi_n$ 有沒有歸一化，這個算式都成立，因為 $\lambda_n$ 提出來後分子分母抵消。[▶ part 2 42:51](https://youtu.be/JnnGNls8_bc?t=2571)

**情形二**：$\psi$ 不是本徵向量。用完備正規正交本徵基底展開：[▶ part 2 43:30](https://youtu.be/JnnGNls8_bc?t=2610)
$$\psi=\sum_{n=1}^\infty c_n\psi_n,\qquad c_n=\langle\psi_n|\psi\rangle,\qquad\|\psi\|^2=\sum_{n=1}^\infty|c_n|^2 .\tag{7.74}$$
最後一式是 Parseval（學生指出；第 22 集）。這裡 $\psi_n$ 是歸一化的，但 $\psi$ 還不一定。[▶ part 2 44:46](https://youtu.be/JnnGNls8_bc?t=2686)

**計算**：[▶ part 2 45:49](https://youtu.be/JnnGNls8_bc?t=2749)
$$\begin{aligned}
\langle\hat A\rangle&=\frac1{\|\psi\|^2}\left\langle\sum_mc_m\psi_m\middle|\hat A\sum_nc_n\psi_n\right\rangle=\frac1{\|\psi\|^2}\left\langle\sum_mc_m\psi_m\middle|\sum_nc_n\lambda_n\psi_n\right\rangle\\
&=\frac1{\|\psi\|^2}\sum_{m,n}\overline{c_m}\,c_n\,\lambda_n\,\langle\psi_m|\psi_n\rangle=\frac1{\|\psi\|^2}\sum_n|c_n|^2\lambda_n .
\end{aligned}$$
- 在物理慣例下，從**第一個**位置提出純量要取共軛（講者口頭說成「從第二個位置提出 $\bar c$」，是第 3 章慣例的說法）。
- $\langle\psi_m|\psi_n\rangle=\delta_{mn}$——講者說「Kronecker δ 是和式的天敵」，雙重和變成單一和。
- $\lambda_n$ 是實數。

【口頭】講者發現課本在 p. 374 的式子裡 $A$ 忽然沒戴帽子：「他對帽子一向斤斤計較……別在意，只是打字錯誤。」[▶ part 2 46:22](https://youtu.be/JnnGNls8_bc?t=2782)

所以
$$\langle\hat A\rangle=\sum_{n=1}^\infty a_n\lambda_n,\qquad a_n=\frac{|c_n|^2}{\sum_{m=1}^\infty|c_m|^2}=\frac{|\langle\psi_n|\psi\rangle|^2}{\sum_{m=1}^\infty|\langle\psi_m|\psi\rangle|^2}.\tag{7.76, 7.77}$$

【口頭】講者堅持分母要換一個字母 $m$：課本分子分母都用 $n$，但分子的 $n$ 是**自由**變數，分母的是**求和啞變數**，「我反對」。[▶ part 2 52:54](https://youtu.be/JnnGNls8_bc?t=3174)

【Q&A】學生問：不用先證明 $a_n$ 的分母收斂嗎？講者：它等於 $\|\psi\|^2$，而我們假設本徵基底是完備正規正交組，所以收斂。[▶ part 2 53:29](https://youtu.be/JnnGNls8_bc?t=3209)

**詮釋**：[▶ part 2 55:25](https://youtu.be/JnnGNls8_bc?t=3325)
- (7.76) 是相同條件下大量測量的結果：$\langle\hat A\rangle$ 是大量測量值的**加權平均**。
- 由假設 II，每次量到某個 $\lambda_n$。課本說 (7.77) 的分子代表 $\lambda_n$ 出現的頻率、分母代表總測量次數，所以 $a_n$ 是「量到 $\lambda_n$ 的**機率**」。
- 總機率 $\sum_na_n=1$（分子對 $n$ 求和就等於分母）。[▶ part 2 58:13](https://youtu.be/JnnGNls8_bc?t=3493)

【口頭】課本 p. 375 寫「each measurement yields one of the eigenvalues of $\hat a$」，講者說小寫 $\hat a$ 從沒定義過，是打字錯誤，應為 $\hat A$。[▶ part 2 55:59](https://youtu.be/JnnGNls8_bc?t=3359)

**歸一化的 $\psi$**（part 3）：[▶ part 3 00:02](https://youtu.be/2gXOCTH1w0c?t=2)
$$\|\psi\|^2=\sum_{n=1}^\infty|c_n|^2=\sum_{n=1}^\infty|\langle\psi_n|\psi\rangle|^2=1,\qquad a_n=|c_n|^2=|\langle\psi_n|\psi\rangle|^2,\qquad\langle\hat A\rangle=\sum_{n=1}^\infty|\langle\psi_n|\psi\rangle|^2\lambda_n .\tag{7.78–7.80}$$

【口頭】講者指出課本 (7.78) 最後一項**漏了求和號**：「和式不會自己消失；$n$ 是求和啞變數，不能突然變成不是。」[▶ part 3 00:43](https://youtu.be/2gXOCTH1w0c?t=43)（上式已補上。）

【口頭】「這就是你在量子力學課學到的期望值算法：本徵值的加權平均，權重是本徵函數和實驗所準備的狀態的內積的平方。」$|c_n|^2$ 是量到 $\lambda_n$ 的機率，而且 $0\le|\langle\psi_n|\psi\rangle|^2\le1$，「這正是你希望機率有的性質」。[▶ part 3 02:22](https://youtu.be/2gXOCTH1w0c?t=142)

---

## 10. 假設 V：測量結果

[▶ part 4 00:00](https://youtu.be/2TlLc6epCHY?t=0)

**Postulate V**：若可觀測量 $\hat A$ 有本徵基底 $\{\psi_n\}$、本徵值 $\{\lambda_n\}$，則系統在歸一化狀態 $\psi(x)$ 時，測量得到 $\lambda_n$ 的機率是
$$P(\lambda_n)=|\langle\psi_n|\psi\rangle|^2 .\tag{7.81}$$

課本列出的「激進主張」（講者照唸）：[▶ part 4 00:35](https://youtu.be/2TlLc6epCHY?t=35)
1. 即使狀態完全確定，也無法確定地預測測量結果，因為測量是儀器和系統的交互作用。量子測量的預測是**統計性**的——和完全決定論的古典力學相反。
2. 在狀態 $\psi$ 中量 $\hat A$ 得到的值是一個**隨機變數**，其機率分佈的平均就是期望值。
3. 對同一狀態重複測量兩次，結果不一定相同（測量會影響系統）；古典力學中重複測量總是得到相同結果。

課本接著說：衡量偏離期望值程度的標準差，就叫**不確定度**（uncertainty）。[▶ part 4 02:12](https://youtu.be/2TlLc6epCHY?t=132)

【口頭】講者發現 §7.3 用倒三角 $\nabla\hat A$、§7.4 改用正三角 $\Delta\hat A$，困惑了一下，最後認定「是同一個東西」：[▶ part 4 03:23](https://youtu.be/2TlLc6epCHY?t=203)
$$\Delta\hat A=\left\|\left(\hat A-\langle\hat A\rangle\right)\psi\right\|=\|\psi_1\|,\qquad\psi_1=\left(\hat A-\langle\hat A\rangle\right)\psi .\tag{7.82, 7.83}$$
「這一部分的章節有點粗心：小寫 $\hat a$、(7.78) 漏掉的求和號……別為這個煩惱。」同樣定義 $\Delta\hat B=\|\psi_2\|$，$\psi_2=\left(\hat B-\langle\hat B\rangle\right)\psi$。

---

## 11. 測不準原理

[▶ part 4 07:02](https://youtu.be/2TlLc6epCHY?t=422)

【口頭】「這是今天所有內容的高潮。」課本說：因為狀態向量在 Hilbert 空間中，不確定度之間有關聯，這就是**廣義測不準原理**（Generalized Uncertainty Principle）。

**Theorem 7.4.1**：$\hat A,\hat B$ 是 Hermitian 算子，則對任意（歸一化）狀態
$$\Delta\hat A\,\Delta\hat B\ \ge\ \frac12\left|\frac1i\left\langle[\hat A,\hat B]\right\rangle\right| .\tag{7.85}$$

【課堂討論】課本 (7.85) 印的是嚴格的 $>$。學生指出應該是 $\ge$，講者同意：證明裡全是 $\ge$；學生並說 Gauss 波包能達到等號。[▶ part 4 09:33](https://youtu.be/2TlLc6epCHY?t=573)

【口頭】講者不懂為什麼要寫 $\frac1i$：反正取了絕對值，乘或除 $i$ 都一樣。[▶ part 4 08:56](https://youtu.be/2TlLc6epCHY?t=536) 以下**不是逐字稿內容**，是依 Hermitian 性質推論的：$[\hat A,\hat B]$ 是反 Hermitian（$[\hat A,\hat B]^*=[\hat B^*,\hat A^*]=[\hat B,\hat A]=-[\hat A,\hat B]$），所以 $\langle[\hat A,\hat B]\rangle$ 是純虛數，$\frac1i\langle[\hat A,\hat B]\rangle$ 是**實數**。$\frac1i$ 只是讓括號裡面變成實數，有沒有絕對值都說得通；取了絕對值後確實是多餘的。

【Q&A】學生提到以前推導過測不準原理。講者：那大概是針對位置和動量的特定情形；這裡是一般版本，同時關聯任意兩個算子的不確定度。[▶ part 4 08:22](https://youtu.be/2TlLc6epCHY?t=502)

**證明**：[▶ part 4 10:53](https://youtu.be/2TlLc6epCHY?t=653)

**第 1 步：Cauchy–Schwarz。** 【口頭】「用一種我們幾乎從不用的方式用它」：
$$\|\psi_1\|\,\|\psi_2\|\ \ge\ |\langle\psi_1|\psi_2\rangle| .$$

**第 2 步：複數的絕對值 ≥ 它的虛部的絕對值。**[▶ part 4 11:28](https://youtu.be/2TlLc6epCHY?t=688)
$$|\langle\psi_1|\psi_2\rangle|\ \ge\ \left|\operatorname{Im}\langle\psi_1|\psi_2\rangle\right| .$$

**第 3 步：虛部公式。** $\operatorname{Im}z=\frac1{2i}(z-\bar z)$，且 $\overline{\langle\psi_1|\psi_2\rangle}=\langle\psi_2|\psi_1\rangle$：
$$\operatorname{Im}\langle\psi_1|\psi_2\rangle=\frac1{2i}\left(\langle\psi_1|\psi_2\rangle-\langle\psi_2|\psi_1\rangle\right).$$
【口頭】「這是我有機會的話會出給線性代數班的題目。」課本這一行也寫 $\ge$，講者和學生認為其實是等號，或許課本的 $\ge$ 是指「對上面所有步驟」而言。[▶ part 4 12:04](https://youtu.be/2TlLc6epCHY?t=724)

**第 4 步：對易子出現。** 【口頭】「$\psi_1$ 裡有 $A$、$\psi_2$ 裡有 $B$，兩項順序相反——對易子就從這裡來。」講者時間不夠，說「直接代進去就好」。[▶ part 4 12:37](https://youtu.be/2TlLc6epCHY?t=757)

以下**不是逐字稿內容**，是依 Hermitian 性質補上的中間計算：記 $a=\langle\hat A\rangle$、$b=\langle\hat B\rangle$（實數）。$\hat A-a$ 是 Hermitian，所以
$$\langle\psi_1|\psi_2\rangle=\left\langle(\hat A-a)\psi\middle|(\hat B-b)\psi\right\rangle=\left\langle\psi\middle|(\hat A-a)(\hat B-b)\psi\right\rangle .$$
同理 $\langle\psi_2|\psi_1\rangle=\langle\psi|(\hat B-b)(\hat A-a)\psi\rangle$。兩式相減，展開後 $a$、$b$ 的項全部抵消（因為 $(\hat A-a)(\hat B-b)-(\hat B-b)(\hat A-a)=\hat A\hat B-\hat B\hat A$）：
$$\langle\psi_1|\psi_2\rangle-\langle\psi_2|\psi_1\rangle=\left\langle\psi\middle|[\hat A,\hat B]\psi\right\rangle=\left\langle[\hat A,\hat B]\right\rangle .$$

**合起來**：
$$\Delta\hat A\,\Delta\hat B=\|\psi_1\|\|\psi_2\|\ \ge\ \left|\frac1{2i}\left\langle[\hat A,\hat B]\right\rangle\right|=\frac12\left|\frac1i\left\langle[\hat A,\hat B]\right\rangle\right| .$$

**Corollary 7.4.2**：對共軛算子[▶ part 4 13:11](https://youtu.be/2TlLc6epCHY?t=791)
$$\Delta q_j\,\Delta p_k\ge\frac\hbar2\delta_{jk},\qquad\Delta x_j\,\Delta p_j\ge\frac\hbar2,\qquad\Delta x_j\,\Delta v_j\ge\frac{\hbar}{2m}.$$
例如 $[\hat x,\hat p]=i\hbar$ 代入：$\frac12\left|\frac1i\cdot i\hbar\right|=\frac\hbar2$。這就是 Heisenberg 著名的測不準原理。

【口頭】講者問：「我們物理人最愛的能量–時間測不準關係呢？」然後自答：時間要到 §7.5 Schrödinger 方程才登場，能量–時間關係「哲學上性質不同」，不屬於這個故事。[▶ part 4 13:42](https://youtu.be/2TlLc6epCHY?t=822)

**課程結尾**：講者說下次見面在下週一（Schrödinger 方程那部分；播放清單到這裡結束）。[▶ part 4 14:17](https://youtu.be/2TlLc6epCHY?t=857)

---

## 12. 一頁速查表

| 項目 | 公式／內容 | 關鍵一步 |
|---|---|---|
| 位置、動量 | $\hat x=x$，$\hat p=-i\hbar\partial_x$，$\hbar=h/2\pi$ | |
| 基本對易子 | $[\hat x,\hat p]=i\hbar$ | $\partial_x(x\psi)=\psi+x\psi'$ |
| 自由粒子 | $[\hat T,\hat p]=0$ ⟹ 能量、動量可同時確定 | $\hat T$ 是 $\hat p$ 的多項式 |
| 有位能 | $[\hat p,\hat H]=-i\hbar V'(x)$ | 乘積法則 |
| 本徵基底 | $\psi=\sum\langle\psi_n|\psi\rangle\psi_n$ | 完備正規正交 |
| 時間 | 時間只在係數 $\langle\psi_n|\Psi\rangle$ 裡 | $\hat A,\psi_n,\lambda_n$ 不隨時間變 |
| 假設 III | 正則變數換成算子 | Table 7.1 |
| 假設 IV | $[\hat q_m,\hat p_n]=i\hbar\delta_{mn}$ | |
| 期望值 | $\langle\hat A\rangle=\frac{\langle\psi|\hat A\psi\rangle}{\langle\psi|\psi\rangle}$ | Hermitian ⟹ 實數 |
| 均方根偏差 | $(\nabla\hat A)^2=\|(\hat A-\langle\hat A\rangle)\psi\|^2$ | Hermitian＋$\langle\hat A\rangle$ 實 |
| Thm 7.3.3 | $(\nabla\hat A)^2=\langle\hat A^2\rangle-\langle\hat A\rangle^2$；$\langle\hat A^2\rangle=\|\hat A\psi\|^2$ | 展開平方，$\langle\psi|\psi\rangle=1$ |
| Thm 7.3.4 | 本徵態 ⟺ $\nabla\hat A=0$ | 範數為 0 ⟹ $(\hat A-\langle\hat A\rangle)\psi=0$ |
| 加權平均 | $\langle\hat A\rangle=\sum a_n\lambda_n$，$a_n=\frac{|c_n|^2}{\sum_m|c_m|^2}$ | $\langle\psi_m|\psi_n\rangle=\delta_{mn}$ |
| 假設 V | $P(\lambda_n)=|\langle\psi_n|\psi\rangle|^2$ | $\sum P=1$（Parseval） |
| 測不準原理 | $\Delta\hat A\,\Delta\hat B\ge\frac12\left|\frac1i\langle[\hat A,\hat B]\rangle\right|$ | Cauchy–Schwarz → 虛部 → 對易子 |
| Heisenberg | $\Delta x\,\Delta p\ge\hbar/2$ | 代 $[\hat x,\hat p]=i\hbar$ |

---

## 13. 與前面集數的連結

本集是播放清單的最後一集，所以改列「本集用到前面哪些工具」。

| 本集用到的工具 | 在哪一集學的 |
|---|---|
| Cauchy–Schwarz 不等式 | 第 18 集 |
| 完備正規正交組、Parseval | 第 21–22 集 |
| Hermitian（自伴）算子、實本徵值 | 第 25–27 集 |
| Fourier 變換（$\hat p$ 為何是微分算子的直覺） | 第 31 集 |
| Poisson 括號 → 對易子 | 第 33 集 |

---

## 附：本集一句話總結

> **量子力學把可觀測量變成 Hermitian 算子：$[\hat x,\hat p]=i\hbar$ 表示位置和動量不能同時量準；在狀態 $\psi$ 中量 $\hat A$，得到本徵值 $\lambda_n$ 的機率是 $|\langle\psi_n|\psi\rangle|^2$，期望值是本徵值的加權平均，偏差為 0 恰好是本徵態；而一行 Cauchy–Schwarz 加上「取虛部」，就推出 $\Delta\hat A\,\Delta\hat B\ge\frac12|\langle[\hat A,\hat B]\rangle|$——Heisenberg 測不準原理。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-05-01 錄影逐字稿（YouTube 自動字幕，四段：約 17:40、59:50、4:10、14:20；part 1 背景嘈雜）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §7.3–7.4 整理。*
