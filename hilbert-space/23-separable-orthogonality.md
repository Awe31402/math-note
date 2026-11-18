---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 23
lecture: Lecture 23
date: 2023-03-10
video: https://youtu.be/rkkPCONUMpM （part 1）、https://youtu.be/fT-crF-XENk （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4 Theorem 3.4.24–3.4.27、§3.6、§3.7（書頁 120–135，PDF 頁 139–154；§3.5 跳過）
---

# 第 23 集 · 可分 Hilbert 空間、同構於 ℓ²、正交補與投影 [▶ 影片](https://youtu.be/rkkPCONUMpM)

← 上一集：[22-orthonormal-basis-parseval](22-orthonormal-basis-parseval.md) ｜ [總目錄](README.md) ｜ 下一集：[24-riesz-representation-operators](24-riesz-representation-operators.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 23 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 31:46，自動字幕）＋ Debnath & Mikusiński §3.4、§3.6–3.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【Q&A】` 學生主動提問與回答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 可分空間有可數稠密子集](#1-可分空間有可數稠密子集)
- [2. 可分空間中的正交集是可數的](#2-可分空間中的正交集是可數的)
- [3. Hilbert 空間同構](#3-hilbert-空間同構)
- [4. 每個可分 Hilbert 空間都同構於 ℓ² 或 ℂᴺ](#4-每個可分-hilbert-空間都同構於-ℓ²-或-ℂᴺ)
- [5. 講者的計畫：跳過 §3.5](#5-講者的計畫跳過-35)
- [6. 正交補](#6-正交補)
- [7. 凸集與最近點](#7-凸集與最近點)
- [8. 正交分解與投影](#8-正交分解與投影)
- [9. 線性泛函與 Riesz 表示定理（敘述）](#9-線性泛函與-riesz-表示定理敘述)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者的目標：**講完第 3 章**，「盡量忍住什麼都要證的衝動」。[▶ 00:03](https://youtu.be/rkkPCONUMpM?t=3)

| 主題 | 課本 |
|---|---|
| 可分 ⟹ 可數稠密子集；正交集可數 | Theorem 3.4.24–3.4.25，pp. 120–121 |
| Hilbert 空間同構；可分空間同構於 $\ell^2$ | Definition 3.4.26、Theorem 3.4.27，p. 121 |
| 正交補 | Definition 3.6.1、Theorem 3.6.2，pp. 127–128 |
| 凸集、最近點、正交分解、$S^{\perp\perp}=S$ | Definition 3.6.3–Theorem 3.6.9，pp. 128–132 |
| Riesz 表示定理、延拓（只敘述） | Lemma 3.7.5、Theorem 3.7.7–3.7.8，pp. 133–135 |

---

## 1. 可分空間有可數稠密子集

[▶ 00:41](https://youtu.be/rkkPCONUMpM?t=41) 課本 Theorem 3.4.24。

**定理**：每個可分 Hilbert 空間都含有**可數稠密子集**。

**證明**：$(x_n)$ 是 $H$ 的完備正規正交數列。令

$$S=\left\{(\alpha_1+i\beta_1)x_1+\cdots+(\alpha_n+i\beta_n)x_n:\ \alpha_k,\beta_k\in\mathbb{Q},\ n\in\mathbb{N}\right\},$$

係數是「複有理數」。課本說它「顯然可數」。對每個 $x\in H$，$\left\|\sum_{k=1}^n\langle x,x_k\rangle x_k-x\right\|\to0$。

【課堂討論】[▶ 05:09](https://youtu.be/rkkPCONUMpM?t=309) 講者和學生拆解為什麼 $S$ 稠密：閉包是 $S$ 中數列的極限集。講者想通的關鍵：

- 係數 $\lambda_k=\langle x,x_k\rangle$ 是複數。任何實數都是有理數列的極限；任何複數都是一對有理數列（一個逼近實部、一個逼近虛部）的極限 $\alpha_k^{(j)}+i\beta_k^{(j)}\to\lambda_k$。[▶ 09:32](https://youtu.be/rkkPCONUMpM?t=572)
- 把這些有理數列「配對」到正規正交的 $x_k$ 上，就能逼近 $x$。

> 以下**不是逐字稿內容**，是把論證寫完整：給 $\varepsilon>0$。先取 $n$ 使 $\left\|x-\sum_{k=1}^n\lambda_kx_k\right\|<\frac\varepsilon2$。再對每個 $k\le n$ 取複有理數 $q_k$ 使 $|q_k-\lambda_k|<\frac{\varepsilon}{2\sqrt n}$。由畢氏定理，$\left\|\sum_{k=1}^n(\lambda_k-q_k)x_k\right\|=\sqrt{\sum|\lambda_k-q_k|^2}<\frac\varepsilon2$。所以 $\sum q_kx_k\in S$ 跟 $x$ 的距離 $<\varepsilon$。可數：$S=\bigcup_n\{\text{長度 }n\text{ 的組合}\}$，每個是 $(\mathbb{Q}^2)^n$ 的像，可數集的可數聯集可數。

課本說這個性質（有可數稠密子集）常被直接拿來當**可分**的定義。

---

## 2. 可分空間中的正交集是可數的

[▶ 12:59](https://youtu.be/rkkPCONUMpM?t=779) 課本 Theorem 3.4.25。

**定理**：可分 Hilbert 空間中的每個正交集都是可數的。

講者【口頭】[▶ 14:26](https://youtu.be/rkkPCONUMpM?t=866)：他一開始以為這個定理「毀了量子力學」：物理系統裡如果本徵向量用**連續**的標籤，就沒辦法住在（可分的）Hilbert 空間裡。說到一半他說：「也許不可分就不是這樣，也許這不是罪魁禍首。」（見第 4 節末他的再說明。）

**證明**[▶ 15:35](https://youtu.be/rkkPCONUMpM?t=935)：$S$ 是正交集，正規化成 $S_1=\{x/\|x\|:x\in S\}$。對相異的 $x,y\in S_1$：

$$\|x-y\|^2=\langle x,x\rangle-\langle x,y\rangle-\langle y,x\rangle+\langle y,y\rangle=1-0-0+1=2.$$

任兩個相異元素距離都是 $\sqrt2$。講者：「停下來欣賞一下……20 維空間裡的正規正交集，彼此都相距 $\sqrt2$。不過想想也不意外，它們都在單位球面上。」

以每個元素為中心畫半徑 $\frac1{\sqrt2}$ 的鄰域，兩兩不相交。講者說：「玩得很險，它們幾乎碰在一起，但邊界是模糊的（開球），所以不相交。」[▶ 18:55](https://youtu.be/rkkPCONUMpM?t=1135)

$H$ 有可數稠密子集 $D$，每個鄰域裡都至少有 $D$ 的一點。鄰域互不相交，所以這給出 $S_1$ 到 $D$ 的一對一對應，$S_1$ 可數。∎

講者【口頭】[▶ 21:22](https://youtu.be/rkkPCONUMpM?t=1282)：重點是**不能超過可數無限**。如果有不可數的正交集，你就得從可數集裡找點，放進不可數多個互不相交的盒子，做不到——「像是鴿籠原理」。

【Q&A】[▶ 22:31](https://youtu.be/rkkPCONUMpM?t=1351) 學生開玩笑「顯然比較大」。講者：「你說的『比較大』是什麼意思？」有限的時候偶數比全部整數少，但無限時要用基數來比。

---

## 3. Hilbert 空間同構

[▶ 22:31](https://youtu.be/rkkPCONUMpM?t=1351) 課本 Definition 3.4.26。

**定義**：Hilbert 空間 $H_1$ **同構**於 $H_2$，如果有一對一、映成的線性映射 $T:H_1\to H_2$ 使

$$\langle T(x),T(y)\rangle=\langle x,y\rangle\quad\text{對所有 }x,y\in H_1. \tag{3.33}$$

（左邊是 $H_2$ 的內積，右邊是 $H_1$ 的。）講者一開始漏了「一對一、映成」，學生提醒。

**$\|T\|=1$**[▶ 26:01](https://youtu.be/rkkPCONUMpM?t=1561)：【課堂討論】講者問 $T$ 的範數怎麼定義，學生答：$\sup_{\|x\|=1}\|Tx\|$（第 7 集）。在 Hilbert 空間用的是誘導範數，所以

$$\|Tx\|=\sqrt{\langle Tx,Tx\rangle}=\sqrt{\langle x,x\rangle}=\|x\|,$$

$\sup_{\|x\|=1}\|Tx\|=1$。講者：「如果要猜 Hilbert 空間同構的長度，當然是 1，還能是什麼？」

【Q&A】[▶ 30:00](https://youtu.be/rkkPCONUMpM?t=1800) 學生問距離函數和範數有什麼共同點。講者：每個範數都誘導距離 $d(x,y)=\|x-y\|$；對稱性來自 $\|x-y\|=|-1|\|y-x\|$；「點到自己距離 0」對應「只有零向量範數為 0」。但不是每個距離都來自範數：距離可以定義在各種奇怪的形狀上，不需要線性結構；三角不等式在距離裡只關於距離，不涉及點的代數運算。

---

## 4. 每個可分 Hilbert 空間都同構於 ℓ² 或 ℂᴺ

[▶ 32:18](https://youtu.be/rkkPCONUMpM?t=1938) 課本 Theorem 3.4.27。

**定理**：$H$ 是可分 Hilbert 空間。

- (a) 若 $H$ 無限維，則 $H$ 同構於 $\ell^2$；
- (b) 若 $\dim H=N$，則 $H$ 同構於 $\mathbb{C}^N$。

講者：這是線性代數裡「有限維向量空間同構於 $\mathbb{R}^n$（或 $\mathbb{F}^n$）」的 Hilbert 空間版本。

**證明 (a)**：

1. 取完備正規正交數列 $(x_n)$。$H$ 無限維，所以它是**無限**數列（否則就有有限基底，「那就太尷尬了」）。[▶ 35:58](https://youtu.be/rkkPCONUMpM?t=2158)
2. **定義** $T(x)=(\alpha_n)$，$\alpha_n=\langle x,x_n\rangle$。講者：「這是不可避免的，還能寫什麼？」由 Bessel，$(\alpha_n)\in\ell^2$。

   【課堂討論】[▶ 37:13](https://youtu.be/rkkPCONUMpM?t=2233) 學生一時以為 $\ell^2$ 是函數的 $L^2$。講者：不是，這裡是**數列**的 $\ell^2$（$\sum|\alpha_n|^2<\infty$），第 1 章 Example 1.2.6。「你還在積分的世界裡。」
3. **線性**[▶ 38:55](https://youtu.be/rkkPCONUMpM?t=2335)：$\langle x+y,x_n\rangle=\langle x,x_n\rangle+\langle y,x_n\rangle$，而數列加法是逐項的，所以 $T(x+y)=T(x)+T(y)$；齊次同理。
4. 【課堂討論】學生列出還要檢查的三件事：**保內積、一對一、映成**。
5. **映成**[▶ 41:16](https://youtu.be/rkkPCONUMpM?t=2476)：任給 $(\alpha_n)\in\ell^2$，令 $x=\sum\alpha_nx_n$（Theorem 3.4.10 保證收斂）。則 $\langle x,x_n\rangle=\alpha_n$，所以 $T(x)=(\alpha_n)$。
6. **一對一**[▶ 42:37](https://youtu.be/rkkPCONUMpM?t=2557)：$T(x)=T(y)$ ⟹ $\alpha_n=\beta_n$ 對所有 $n$ ⟹ $x=\sum\alpha_nx_n=\sum\beta_nx_n=y$（完備）。
7. **保內積**[▶ 44:19](https://youtu.be/rkkPCONUMpM?t=2659)：
   $$\langle x,y\rangle=\left\langle\sum_n\alpha_nx_n,\sum_j\beta_jx_j\right\rangle=\sum_n\sum_j\alpha_n\bar\beta_j\langle x_n,x_j\rangle=\sum_n\alpha_n\bar\beta_n=\langle T(x),T(y)\rangle_{\ell^2}.$$
   講者中途寫錯成 $\sum|\alpha_n|^2$（「$\beta$ 不會消失，我真笨」），改正後說：最後一個就是 $\ell^2$ 的內積定義（Example 3.2.4，p. 95）。∎

（(b) 是習題。）

**「某種意義上很無聊」**[▶ 47:10](https://youtu.be/rkkPCONUMpM?t=2830)：講者：只要是可分 Hilbert 空間，除了記號的選擇之外，你其實就是在談平方可和的複數列（或 $n$ 維複向量）。課本：同構是等價關係；任兩個無限維可分 Hilbert 空間都同構；實的也一樣。「某種意義上，只有一個實的、一個複的無限維可分 Hilbert 空間。」

**量子力學的再說明**【口頭】[▶ 47:45](https://youtu.be/rkkPCONUMpM?t=2865)：講者說到量子力學時要記得這個。有些物理系統的能量本徵值在某範圍內是**離散**的，超過某個值就變成**連續**（粒子跑出有限位能井、不再被束縛，就沒有離散能譜）。如果想用一個空間處理全部：Hermitian（自伴）算子的本徵向量，不同本徵值的會**正交**（像線性代數裡正交變換的不同本徵值本徵向量互相垂直）。能量本徵態構成基底，因此是正規正交數列；如果標籤（能量）是連續的，就放不進可分 Hilbert 空間——「這裡不是你的家」。「但我們假設了可分，也許出路就在那裡。」

> 以下**不是逐字稿內容**，是一句補充：講者說的「正交變換」應是「Hermitian／自伴算子」或「正規矩陣」：對稱（Hermitian）矩陣不同本徵值的本徵向量正交。連續譜的處理需要課本第 7 章（量子力學）和廣義本徵向量，第 33–34 集再看講者怎麼說。

---

## 5. 講者的計畫：跳過 §3.5

【口頭】[▶ 51:09](https://youtu.be/rkkPCONUMpM?t=3069)

- **§3.5（三角 Fourier 級數）**：講者說「充滿有趣公式」，但**先跳過**。他想先具體教學生怎麼解經典 PDE（波動方程、熱方程），之後再回來。他想從頭到尾、正反面徹底理解 §3.5，因為裡面的「**可和核**（summability kernel）」跟他想更深入理解的 **Green 函數**有關。
- **Green 函數是什麼**【Q&A】：學生問是不是 Green 定理那個。講者：不是。粗略說，如果微分方程是一個映射，Green 函數某種意義上定義了它的**反映射**——「我講得很揮手」。[▶ 53:29](https://youtu.be/rkkPCONUMpM?t=3209)

> 【課本補充】§3.5 證明 $\{e^{inx}/\sqrt{2\pi}\}$ 在 $L^2([-\pi,\pi])$ 完備：證明 Fourier 部分和的平均（Cesàro 平均，用 Fejér 核）在 $L^1$ 範數下收斂到 $f$。課本也提到：$L^2$ 收斂一般不推出逐點收斂；1966 年 L. Carleson 證明 $L^2([-\pi,\pi])$ 函數的 Fourier 級數**幾乎處處**收斂。

---

## 6. 正交補

[▶ 54:02](https://youtu.be/rkkPCONUMpM?t=3242) 課本 Definition 3.6.1、Theorem 3.6.2。

**定義**：$S$ 是內積空間 $E$ 的非空子集。$x\perp S$ 如果 $\langle x,y\rangle=0$ 對所有 $y\in S$。

$$S^\perp=\{x\in E:x\perp S\}$$

叫 $S$ 的**正交補（orthogonal complement）**。$S^{\perp\perp}=(S^\perp)^\perp$。

課本說記號 $S^\perp$ 不精確，因為依賴 $E$：同一個 $S\subseteq E_1\cap E_2$，在 $E_1$ 和 $E_2$ 裡的正交補不同。講者：「當然。」

**例**【課堂討論】[▶ 56:54](https://youtu.be/rkkPCONUMpM?t=3414)：講者問 $\{0\}^\perp$ 是什麼，學生猜「全部或什麼都沒有」，答案是**全部**：$\{x:\langle x,0\rangle=0\}=E$。【課本補充】而 $E^\perp=\{0\}$（跟所有向量正交的只有 0）。

**正交的集合**[▶ 58:24](https://youtu.be/rkkPCONUMpM?t=3504)：$A\perp B$ 指 $A$ 中每個元素跟 $B$ 中每個都正交。則 $A\cap B=\{0\}$ 或 $\varnothing$。【課堂討論】學生舉 $\{(0,1)\}$ 和 $\{(1,0)\}$：交集是空集。講者：如果是子空間，交集一定含 0；但這裡 $A,B$ 只是集合。

### Theorem 3.6.2：$S^\perp$ 是閉子空間

[▶ part 2 00:05](https://youtu.be/fT-crF-XENk?t=5)

**子空間**：講者說很簡單（$\langle\alpha x+\beta y,z\rangle=\alpha\langle x,z\rangle+\beta\langle y,z\rangle=0$）。

**閉**【課堂討論】：學生先給拓樸定義，講者：「不、不，要序列的……你真是拓樸學家。」「拓樸的定義一旦懂了比較簡單。」他們找到 Theorem 1.3.23（p. 16）：閉包 = 收斂數列極限的集合；閉 ⟺ 每個收斂數列的極限都在集合裡。[▶ part 2 03:11](https://youtu.be/fT-crF-XENk?t=191)

取 $x_n\in S^\perp$，$x_n\to x$。對 $y\in S$：

$$\langle x,y\rangle=\left\langle\lim_nx_n,y\right\rangle=\lim_n\langle x_n,y\rangle=\lim_n0=0.$$

所以 $x\in S^\perp$。極限拿出來是因為內積對第一個位置**連續**（第 19 集）；講者說他本來以為課本會避開，結果「他做的跟我一模一樣，他說『由內積的連續性』」。∎

【課本補充】$S$ 不必是子空間。$S^\perp$ 是 Hilbert 空間（Hilbert 空間的閉子空間完備）。$S\cap S^\perp=\{0\}$ 或 $\varnothing$。

---

## 7. 凸集與最近點

### 凸集

[▶ part 2 07:21](https://youtu.be/fT-crF-XENk?t=441) 課本 Definition 3.6.3。

$U$ 叫**凸（convex）**，如果對任意 $x,y\in U$、$\alpha\in(0,1)$：$\alpha x+(1-\alpha)y\in U$。

【課堂討論】學生說這是連接 $x$ 到 $y$ 的線段。講者：$r(\alpha)=\alpha x+(1-\alpha)y$，$r(0)=y$、$r(1)=x$。課本不含端點（「模糊的線段」），他習慣包含端點，「也許邏輯上等價」。

> 以下**不是逐字稿內容**，是確認：端點就是 $x,y$ 本身，本來就在 $U$ 裡，所以用 $(0,1)$ 或 $[0,1]$ 等價。

講者說他線代課通常不講凸組合，研究所見過，單純形（simplex）那些東西都是用凸包造的。【課本補充】向量子空間是凸集。

### Theorem 3.6.4：最近點性質

[▶ part 2 11:40](https://youtu.be/fT-crF-XENk?t=700)

**定理**：$S$ 是 Hilbert 空間 $H$ 的**閉凸**子集。對每個 $x\in H$，存在**唯一**的 $y\in S$ 使

$$\|x-y\|=\inf_{z\in S}\|x-z\|. \tag{3.42}$$

課本說這對逼近理論有根本的重要性。

**圖像**【課堂討論】[▶ part 2 13:26](https://youtu.be/fT-crF-XENk?t=806)：講者畫了一個有凹陷的形狀，學生指出它不是凸的；講者改畫成「檸檬，不是被壓凹的檸檬」。平面是 Hilbert 空間，可以從圖獲得直覺：最近點在**沿邊界法線**出去的方向上。

（學生中途要去拿一個考試的學生，講者說辦公室的門「不可交換」：出得去，沒卡進不來。）

講者提到一段 Witten 的物理影片：有人問最短測地線，Witten 隨口說「從柯西曲面出發的正交測地線是長度最短的，我們高中都學過」，講者覺得很好笑，說應該收集起來當上課的梗。[▶ part 2 16:51](https://youtu.be/fT-crF-XENk?t=1011)（接著講者聊他想開一個「數學惡搞」頻道：故意教錯的大學代數，例如 $\frac{64}{16}=4$ 因為 6 可以約掉。）

講者：子空間是凸集的例子，所以這也重現了**最小平方法**底下的定理；最小平方法有實際算最近點的方法（就是沿投影走）。他猜 pp. 128–129 的證明某種意義上藏著同一套數學，「但很巧妙，我現在不講」。[▶ part 2 19:37](https://youtu.be/fT-crF-XENk?t=1177)

【課本補充】證明概要：

1. 取 $y_n\in S$ 使 $\|x-y_n\|\to d=\inf_{z\in S}\|x-z\|$。凸 ⟹ $\frac12(y_m+y_n)\in S$ ⟹ $\left\|x-\frac12(y_m+y_n)\right\|\ge d$。
2. **平行四邊形定律**（用在 $x-y_m$、$x-y_n$ 上）：
   $$\|y_m-y_n\|^2=2\left(\|x-y_m\|^2+\|x-y_n\|^2\right)-4\left\|x-\tfrac12(y_m+y_n)\right\|^2\le2(\|x-y_m\|^2+\|x-y_n\|^2)-4d^2\to0.$$
   所以 $(y_n)$ 是 Cauchy。$H$ 完備、$S$ 閉 ⟹ $y_n\to y\in S$，範數連續 ⟹ $\|x-y\|=d$。
3. 唯一：若 $y_1$ 也達到 $d$，同一個式子給 $\|y-y_1\|^2\le4d^2-4d^2=0$。

（這裡用到的三樣東西：平行四邊形定律——所以只在內積空間成立；完備；閉凸。）

### Theorem 3.6.5：最近點的刻畫（實內積空間）

[▶ part 2 20:11](https://youtu.be/fT-crF-XENk?t=1211)

$S$ 是實內積空間 $E$ 的凸子集，$y\in S$，$x\in E$。下面等價：

- (a) $\|x-y\|=\inf_{z\in S}\|x-z\|$；
- (b) $\langle x-y,z-y\rangle\le0$ 對所有 $z\in S$。

講者：下確界有點嚇人，但 (b) 是你能「咬下去」的東西，比較好用。證明在 p. 130，「很巧妙，往下走」。

【課本補充】幾何意義（$\mathbb{R}^2$，Figure 3.3）：從 $y$ 到 $x$ 的線和從 $y$ 到任一 $z\in S$ 的線，夾角總是**鈍角**。

---

## 8. 正交分解與投影

[▶ part 2 22:53](https://youtu.be/fT-crF-XENk?t=1373) 課本 Theorem 3.6.6、3.6.9。

**定理 3.6.6**：$H_1$ 是 Hilbert 空間 $H$ 的**閉**子空間。則每個 $x\in H$ 都能**唯一**寫成

$$x=y+z,\qquad y\in H_1,\ z\in H_1^\perp.$$

講者：「就像有限維的垂直子空間，但這可能是無限維的，很棒。」

也就是 $H=H_1\oplus H_1^\perp$（**正交分解**）。講者：兩個都是子空間，交集是 $\{0\}$，相加得到全部，這就是直和。$H_1$ 的基底聯集 $H_1^\perp$ 的基底，是 $H$ 的基底。

**正交投影**：$P_{H_1}(x)=y$。（課本 §4.7 再談。）

【課本補充】證明概要：$y$ 是 $x$ 在 $H_1$ 中的最近點（Theorem 3.6.4，子空間是閉凸集）。對 $w\in H_1$、$\lambda\in\mathbb{C}$，$\|x-y\|^2\le\|x-y-\lambda w\|^2$，展開得 $-2\operatorname{Re}\lambda\langle w,x-y\rangle+|\lambda|^2\|w\|^2\ge0$；取 $\lambda>0$ 和 $\lambda=-i\cdot$正數、讓 $\lambda\to0$，得 $\operatorname{Re}$ 和 $\operatorname{Im}\langle w,x-y\rangle\le0$；對 $-w$ 也成立，所以 $\langle w,x-y\rangle=0$，$x-y\in H_1^\perp$。唯一：$y-y_1=z_1-z\in H_1\cap H_1^\perp=\{0\}$。

【課本補充】Example 3.6.7：$\mathbb{R}^2$ 中若 $s_0$ 是 $S$ 的單位向量，$y=\langle x,s_0\rangle s_0$。

**定理 3.6.9**：$S$ 是 Hilbert 空間的閉子空間，則 $S^{\perp\perp}=S$。講者：「很酷。」[▶ part 2 25:54](https://youtu.be/fT-crF-XENk?t=1554)

---

## 9. 線性泛函與 Riesz 表示定理（敘述）

[▶ part 2 26:27](https://youtu.be/fT-crF-XENk?t=1587) 課本 §3.7。講者跳過例子，只念出定理。

**Lemma 3.7.5**：若 $f$ 是 Hilbert 空間 $H$ 上非零的有界線性泛函，則 $\dim\mathcal{N}(f)^\perp=1$。

**Theorem 3.7.7（Riesz 表示定理）**：$f$ 是 Hilbert 空間 $H$ 上的有界線性泛函。則存在**唯一**的 $x_0\in H$ 使

$$f(x)=\langle x,x_0\rangle\quad\text{對所有 }x\in H,$$

而且 $\|f\|=\|x_0\|$。

**Theorem 3.7.8**：$f$ 是 Hilbert 空間 $H$ 的子空間 $E$ 上的有界線性泛函。則存在 $H$ 上的有界線性泛函 $g$，使 $g=f$ 在 $E$ 上，而且 $\|g\|=\|f\|$。

講者：這是說子空間上的線性泛函可以**延拓**到整個空間；定理只說存在，沒說唯一，所以可能不唯一。

【課本補充】課本說：泛函分析最重要的定理之一 **Hahn–Banach 定理**說，賦範空間子空間上的有界線性泛函可以延拓到整個空間，但證明不是建構式的；Hilbert 空間的情況簡單得多（用 Riesz 表示定理直接造）。

**講者的打算**【口頭】[▶ part 2 28:14](https://youtu.be/fT-crF-XENk?t=1694)：這些他在有限維的線代課證過很多，每個要一小時；在無限維仔細做很美，但他想往下走到第 4 章。如果第 4 章一直用 Riesz 表示定理，他會回來證（下一集就證了）。他也在考慮先做微分方程的例子：那其實是第 5 章應用的特例，要做到能出作業的程度，因為「要自己解幾個才會懂」。看過之後就會欣賞 §5.9（Sturm–Liouville 系統：解的就是他要示範的問題的一般情形）、§5.10（反微分算子與 Green 函數）、§5.11（Fourier 變換）。講者最後提到要不要開始跟一位學生講 Lie 代數，然後關掉錄影。

---

## 10. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| 可數稠密 | 可分 ⟹ 複有理係數的有限組合稠密 | 先截斷 Fourier 級數，再用有理數逼近係數 |
| 正交集可數 | 可分空間中的正交集可數 | 正規化後兩兩距離 $\sqrt2$；不相交的 $\frac1{\sqrt2}$ 球各含稠密集一點 |
| 同構 | 一對一映成線性、保內積 | $\|T\|=1$ |
| 分類 | 無限維可分 ≅ $\ell^2$；$N$ 維 ≅ $\mathbb{C}^N$ | $T(x)=(\langle x,x_n\rangle)$；Parseval 型計算 |
| 正交補 | $S^\perp$ 是閉子空間 | 內積連續 |
| $\{0\}^\perp=E$，$E^\perp=\{0\}$ | | |
| 凸 | $\alpha x+(1-\alpha)y\in U$ | 子空間是凸集 |
| 最近點 | 閉凸 $S$，唯一 $y$ 使 $\|x-y\|=\inf$ | 平行四邊形定律 ⟹ 最小化數列是 Cauchy |
| 刻畫（實） | $\langle x-y,z-y\rangle\le0$ ∀$z\in S$ | 鈍角 |
| 正交分解 | $H=H_1\oplus H_1^\perp$（$H_1$ 閉） | 最近點 $y$；$x-y\perp H_1$ |
| 雙正交補 | $S^{\perp\perp}=S$（$S$ 閉子空間） | |
| Riesz | $f(x)=\langle x,x_0\rangle$，$\|f\|=\|x_0\|$ | 下一集證明 |

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Riesz 表示定理的證明 | 第 24 集 |
| 正交投影 $P_{H_1}$ | 第 25–26 集起：投影算子、自伴算子（課本 §4.7） |
| 可分空間 ≅ $\ell^2$ | 第 27–28 集：算子的矩陣表示、本徵向量 |
| §3.5 Fourier 級數完備性、Green 函數 | 第 29–31 集：PDE 例子、Sturm–Liouville、Green 函數 |
| 連續譜的問題 | 第 33–34 集：量子力學 |

---

## 附：本集一句話總結

> **可分 Hilbert 空間有可數稠密子集、所有正交集都可數，而且透過 $x\mapsto(\langle x,x_n\rangle)$ 全都同構於 $\ell^2$（或 $\mathbb{C}^N$）——某種意義上只有一個；在 Hilbert 空間裡，平行四邊形定律保證閉凸集上有唯一的最近點，因此每個閉子空間都給出正交分解 $H=H_1\oplus H_1^\perp$，這是投影和 Riesz 表示定理的基礎。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-10 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 31:46）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4、§3.6–3.7 整理。*
