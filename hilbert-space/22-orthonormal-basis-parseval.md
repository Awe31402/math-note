---
course: Hilbert Spaces（2023 春，實體課錄影）
episode: 22
lecture: Lecture 22
date: 2023-03-08
video: https://youtu.be/D8I5swVDkuQ （part 1）、https://youtu.be/kmy0xwKHJ_g （part 2）
notes: Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4，Definition 3.4.13–Example 3.4.23（書頁 114–120，PDF 頁 133–139）
---

# 第 22 集 · 正規正交基底、Parseval 公式、例子、可分空間 [▶ 影片](https://youtu.be/D8I5swVDkuQ)

← 上一集：[21-orthonormal-sequences-fourier](21-orthonormal-sequences-fourier.md) ｜ [總目錄](README.md) ｜ 下一集：[23-separable-orthogonality](23-separable-orthogonality.md) →

> **課程**：Hilbert Spaces（實體小班課，2023 春）— 第 22 集
> **講者**：James Cook（⚠️ 待確認）
> **來源**：YouTube 錄影逐字稿（part 1 59:51 ＋ part 2 17:17，自動字幕）＋ Debnath & Mikusiński §3.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課堂討論】` 講者問、學生答
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 正規正交基底：可能不可數嗎？](#1-正規正交基底可能不可數嗎)
- [2. 完備正規正交數列的 span 稠密](#2-完備正規正交數列的-span-稠密)
- [3. Theorem 3.4.14：完備 ⟺ 只有 0 跟所有 xₙ 正交](#3-theorem-3414完備--只有-0-跟所有-xₙ-正交)
- [4. Parseval 公式](#4-parseval-公式)
- [5. 例：複指數函數與 L²([0,a])](#5-例複指數函數與-l²0a)
- [6. 例：三角函數系](#6-例三角函數系)
- [7. 例：Rademacher 與 Walsh 函數](#7-例rademacher-與-walsh-函數)
- [8. 可分 Hilbert 空間](#8-可分-hilbert-空間)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 正規正交基底、span 稠密 | Definition 3.4.13，p. 114 |
| 完備 ⟺ 正交補只有 0 | Theorem 3.4.14，p. 115 |
| Parseval 公式 | Theorem 3.4.15，pp. 115–116 |
| 例：$e^{inx}/\sqrt{2\pi}$、三角函數系、cos／sin 系、Rademacher、Walsh | Example 3.4.16–3.4.19，pp. 116–119 |
| 可分空間；不可分的例子 | Definition 3.4.20–Example 3.4.23，pp. 119–120 |

---

## 1. 正規正交基底：可能不可數嗎？

[▶ 00:49](https://youtu.be/D8I5swVDkuQ?t=49)

複習：正規正交系統 $B$ 是**正規正交基底**，如果每個 $x$ 都能**唯一**寫成 $\sum_{n=1}^\infty\alpha_nx_n$（$x_n\in B$ 相異）。正規正交數列**完備**，如果每個 $x=\sum\langle x,x_n\rangle x_n$。上次證了：完備的正規正交數列是正規正交基底。

**講者的疑問**【口頭】[▶ 04:05](https://youtu.be/D8I5swVDkuQ?t=245)：這個定義有沒有強迫正規正交系統是**可數**的？我們把線性組合推廣成**可數**的級數，但 $B$ 本身原則上好像可以比可數還大（不可數）。課本也許會、也許不會談到。

> 【課本補充】課本接下來（p. 120）說「本書只考慮**可分**的 Hilbert 空間」，而可分空間中每個正交集都可數（Theorem 3.4.25，下一集）。不可分的空間（例如本集最後的例子）才會有不可數的正規正交系統。

---

## 2. 完備正規正交數列的 span 稠密

[▶ 05:14](https://youtu.be/D8I5swVDkuQ?t=314) 課本 p. 114。

**主張**：若 $(x_n)$ 是內積空間 $E$ 中的完備正規正交數列，則

$$\operatorname{span}\{x_1,x_2,\dots\}=\left\{\sum_{k=1}^n\alpha_kx_k:n\in\mathbb{N},\ \alpha_k\in\mathbb{C}\right\}$$

在 $E$ 中**稠密**（閉包是整個 $E$）。

講者說課本沒解釋，表示「把字放在一起想一想就顯然」。【課堂討論】他問閉包的**序列刻畫**是什麼，學生找到 Theorem 1.3.23（第 4 集）：$\operatorname{cl}S$ = $S$ 中收斂數列的所有極限。講者說：「這也是我複習單的危險：少了『你該知道、但不必會證』的定理那一類，這些定理是命脈。」[▶ 08:48](https://youtu.be/D8I5swVDkuQ?t=528)

**證明**[▶ 12:42](https://youtu.be/D8I5swVDkuQ?t=762)：任取 $x\in E$。由完備，

$$x=\sum_{n=1}^\infty\langle x,x_n\rangle x_n=\lim_{n\to\infty}\sum_{k=1}^n\langle x,x_k\rangle x_k,$$

部分和都在 span 裡，所以 $x$ 是 span 中數列的極限，由 Theorem 1.3.23，$x\in\operatorname{cl}(\operatorname{span})$。所以 $E\subseteq\operatorname{cl}(\operatorname{span})$；反向包含顯然（span 是 $E$ 的子空間）。∎

講者：「很顯然——還是花了我五分鐘。」

---

## 3. Theorem 3.4.14：完備 ⟺ 只有 0 跟所有 xₙ 正交

[▶ 15:06](https://youtu.be/D8I5swVDkuQ?t=906)

**定理**：Hilbert 空間 $H$ 中的正規正交數列 $(x_n)$ 是完備的 ⟺

$$\langle x,x_n\rangle=0\ \text{對所有 }n\ \Longrightarrow\ x=0.$$

講者：完備性本質上等價於內積對這個數列「非退化」。（他也說應該把書掃描起來，別一直拿著書，橡皮擦屑都掉進書裡了。）

**(⟹)**[▶ 17:18](https://youtu.be/D8I5swVDkuQ?t=1038)：講者先想代入展開再用 δ，接著說：「我想太多了……犯規。」直接：若所有 $\langle x,x_n\rangle=0$，

$$x=\sum_{j=1}^\infty\langle x,x_j\rangle x_j=\sum_{j=1}^\infty0\cdot x_j=0.$$

**(⟸)**[▶ 19:43](https://youtu.be/D8I5swVDkuQ?t=1183)：設「跟所有 $x_n$ 正交 ⟹ 是 0」。任取 $y\in H$，令

$$z=\sum_{j=1}^\infty\langle y,x_j\rangle x_j.$$

【課本補充】$z$ 存在：由 Bessel，$\sum|\langle y,x_j\rangle|^2\le\|y\|^2<\infty$；由 Theorem 3.4.10（$H$ **完備**），級數收斂。

計算 $\langle y-z,x_n\rangle$：

$$\langle y-z,x_n\rangle=\langle y,x_n\rangle-\sum_{j=1}^\infty\langle y,x_j\rangle\langle x_j,x_n\rangle=\langle y,x_n\rangle-\langle y,x_n\rangle=0.$$

講者：「我最喜歡的 Kronecker δ：有限和死掉了，在血霧中只剩 $j$ 換成 $n$。」（第一步用了內積對第一位置的連續性，把無窮和拉出來。）[▶ 24:03](https://youtu.be/D8I5swVDkuQ?t=1443)

所以 $y-z$ 跟所有 $x_n$ 正交，由假設 $y-z=0$，即 $y=\sum\langle y,x_j\rangle x_j$。$y$ 任意，所以完備。∎

---

## 4. Parseval 公式

[▶ 25:06](https://youtu.be/D8I5swVDkuQ?t=1506) 課本 Theorem 3.4.15。Marc-Antoine Parseval des Chênes（1755–1836）。課本說它可以看成**畢氏定理推廣到無窮和**。

**定理**：Hilbert 空間中的正規正交數列 $(x_n)$ 是完備的 ⟺ 對每個 $x\in H$，

$$\|x\|^2=\sum_{n=1}^\infty|\langle x,x_n\rangle|^2. \tag{3.31}$$

**證明的工具**[▶ 27:34](https://youtu.be/D8I5swVDkuQ?t=1654)：【課堂討論】學生指出：上次的 **Bessel 等式**

$$\left\|x-\sum_{k=1}^n\langle x,x_k\rangle x_k\right\|^2=\|x\|^2-\sum_{k=1}^n|\langle x,x_k\rangle|^2. \tag{3.32}$$

講者：「天啊，寫下來幾乎就是顯然的。」

**(⟹)**：完備 ⟹ 左邊 $\to0$（$n\to\infty$）。講者說：範數連續、平方也連續，可以把極限拿進去（要嚴格也能寫 $\varepsilon$）。所以右邊 $\to0$：$\|x\|^2=\sum|\langle x,x_n\rangle|^2$。

**(⟸)**[▶ 30:55](https://youtu.be/D8I5swVDkuQ?t=1855)：講者在這個方向卡了一陣，試三角不等式也沒用。【課堂討論】學生提醒 (3.32)；講者：「我搞反了，我是笨蛋……」：Parseval 成立 ⟹ (3.32) **右邊** $\to0$ ⟹ 左邊 $\to0$ ⟹ $x=\sum\langle x,x_k\rangle x_k$，即完備。「全都是 Bessel 等式。我在這上面花了太多時間。」[▶ 40:19](https://youtu.be/D8I5swVDkuQ?t=2419)∎

**要點**：完備 ⟺ 每個 $x$ 的係數平方和等於 $\|x\|^2$；把它想成基底時，**係數就是內積**。

> 以下**不是逐字稿內容**，是把三個條件放在一起（Hilbert 空間中的正規正交數列 $(x_n)$）：
> 完備 ⟺ 是正規正交基底 ⟺ 正交補只有 $\{0\}$ ⟺ span 稠密 ⟺ Parseval 對每個 $x$ 成立。

---

## 5. 例：複指數函數與 L²([0,a])

[▶ 42:03](https://youtu.be/D8I5swVDkuQ?t=2523) 課本 Example 3.4.16。

$$\varphi_n(x)=\frac{e^{inx}}{\sqrt{2\pi}},\qquad n=0,\pm1,\pm2,\dots$$

在 $L^2([-\pi,\pi])$ 中**完備**。課本說：完備性的證明不簡單，§3.5 討論。

**換尺度到 $[0,a]$**[▶ 43:50](https://youtu.be/D8I5swVDkuQ?t=2630)：課本說簡單的換尺度，就能把 $f\in L^2([0,a])$ 表示成

$$f(x)=\sum_{n=-\infty}^\infty\beta_ne^{2n\pi ix/a},\qquad\beta_n=\frac1a\int_0^af(t)e^{-2n\pi it/a}dt.$$

講者覺得「在節中間沒任何解釋就寫這個很煩」。他說如果是 $[-a,a]$ 他比較容易看，$[0,a]$ 要想一下。學生說 §3.5 一開始就講這個。

**講者的推導**【課堂討論】[▶ 49:56](https://youtu.be/D8I5swVDkuQ?t=2996)：找線性映射把 $[-\pi,\pi]$ 送到 $[0,a]$：設 $t=mx+b$，$-\pi\mapsto0$、$\pi\mapsto a$，解得

$$t=\frac a2\left(1+\frac x\pi\right),\qquad x=\pi\left(\frac{2t}{a}-1\right),\qquad dt=\frac{a}{2\pi}dx.$$

代入 $\beta_n$：

$$\beta_n=\frac1a\cdot\frac{a}{2\pi}\int_{-\pi}^\pi f\!\left(\tfrac a2\left(1+\tfrac x\pi\right)\right)e^{-2\pi in\cdot\frac{1}{2}(1+x/\pi)}dx,$$

指數是 $-\pi in-inx$，所以 $e^{-\pi in}e^{-inx}$，而 $e^{-\pi in}=\cos n\pi=(-1)^n$（講者說他剛在微積分 II 講過）。[▶ part 2 00:04](https://youtu.be/kmy0xwKHJ_g?t=4)

講者：「你可以從那個公式走到這個公式。」這就是課本說的換尺度。

> 以下**不是逐字稿內容**，是整理：令 $g(x)=f\!\left(\frac a2(1+\frac x\pi)\right)\in L^2([-\pi,\pi])$，則 $\beta_n=\frac{(-1)^n}{2\pi}\int_{-\pi}^\pi g(x)e^{-inx}dx$，也就是 $g$ 的普通 Fourier 係數乘 $(-1)^n$。換句話說，$\left\{\frac{1}{\sqrt a}e^{2n\pi ix/a}\right\}_{n\in\mathbb{Z}}$ 是 $L^2([0,a])$（內積 $\int_0^af\bar g$）的完備正規正交數列；$\beta_n$ 是對**未正規化**的 $e^{2n\pi ix/a}$ 寫的係數，所以前面是 $\frac1a$。

講者今天多講 10 分鐘：有個學生要考試，他寫字的手腕脫臼，講者想多爭取點時間。[▶ part 2 05:30](https://youtu.be/kmy0xwKHJ_g?t=330)

---

## 6. 例：三角函數系

[▶ part 2 06:05](https://youtu.be/kmy0xwKHJ_g?t=365) 課本 Example 3.4.17–3.4.18。

**Example 3.4.17**：

$$\frac{1}{\sqrt{2\pi}},\ \frac{\cos x}{\sqrt\pi},\ \frac{\sin x}{\sqrt\pi},\ \frac{\cos2x}{\sqrt\pi},\ \frac{\sin2x}{\sqrt\pi},\dots$$

是 $L^2([-\pi,\pi])$ 中的完備正規正交系統。講者：這是上一個例子的替代版，本質上只是 $e^{inx}=\cos nx+i\sin nx$，而 sin 和 cos 是正交的函數。

【課本補充】正交性由積化和差：

$$2\cos nx\cos mx=\cos(n+m)x+\cos(n-m)x,\quad2\sin nx\sin mx=\cos(n-m)x-\cos(n+m)x,\quad2\cos nx\sin mx=\sin(n+m)x-\sin(n-m)x,$$

再積分；$\int_{-\pi}^\pi\cos^2nx=\int_{-\pi}^\pi\sin^2mx=\pi$ 給出正規化。完備性由 Example 3.4.16 推出（$e^0=1$，$e^{inx}=\cos nx+i\sin nx$）。

**Example 3.4.18**：下面兩組**各自**是 $L^2([0,\pi])$ 中的完備正規正交系統：

$$\frac1{\sqrt\pi},\ \sqrt{\tfrac2\pi}\cos x,\ \sqrt{\tfrac2\pi}\cos2x,\dots\qquad\text{與}\qquad\sqrt{\tfrac2\pi}\sin x,\ \sqrt{\tfrac2\pi}\sin2x,\dots$$

講者問：課本有沒有寫 $L^2([0,a])$ 的內積？他在黑板上寫了一個問號。[▶ part 2 08:03](https://youtu.be/kmy0xwKHJ_g?t=483)

> 以下**不是逐字稿內容**，是回答那個問號：$L^2([0,\pi])$ 的內積就是第 18 集的 $\langle f,g\rangle=\int_0^\pi f\bar g$（Example 3.2.7 說的「$L^2(\Omega)$ 用 $\Omega$ 上的積分」）。在這個內積下，$\int_0^\pi\frac2\pi\sin^2nx\,dx=1$，所以係數 $\sqrt{2/\pi}$ 正好正規化。這兩組就是 Fourier **半幅**（只用 cos 或只用 sin）展開；講者在本集第 5 節前提到「研究 Fourier 級數時有半幅級數、全幅級數等各種技巧，可以把一種情況的功夫偷到另一種」。[▶ 44:23](https://youtu.be/D8I5swVDkuQ?t=2663)

---

## 7. 例：Rademacher 與 Walsh 函數

[▶ part 2 10:35](https://youtu.be/kmy0xwKHJ_g?t=635) 課本 Example 3.4.19。

**Rademacher 函數**：

$$R(m,x)=\operatorname{sgn}\big(\sin(2^m\pi x)\big),\quad m=0,1,2,\dots,\ x\in[0,1],$$

sgn 在正數是 1、0 是 0、負數是 $-1$。它們構成 $L^2([0,1])$ 中的正規正交系統（證明在 pp. 117–118）。講者：「這是什麼黑魔法……好奇怪的例子。」

**Walsh 函數**用 Rademacher 函數造，構成**完備**正規正交系統；圖在 p. 119，講者說像之前階梯函數的構造。他猜課本放這兩個例子是為了某個反例，「如果要我猜，跟可分空間有關」。

【課本補充】

- $R(m,x)$ 是在 $[0,1]$ 上切成 $2^m$ 段、交替取 $\pm1$ 的方波；$\int R^2=1$；$m>n$ 時在 $R(n,\cdot)$ 為常數的每一段上 $R(m,\cdot)$ 積分為 0，所以正交。
- **Rademacher 系不完備**：$f=\chi_{[1/4,3/4]}$，$\int fR(0,\cdot)=\frac12$，$\int fR(m,\cdot)=0$（$m\ge1$），但 $f\ne\frac12R(0,\cdot)$。
- **Walsh 函數**：$W(0,x)=1$；$m=a_1+2a_2+4a_3+\cdots$（二進位），$W(m,x)=\prod_kR(k,x)^{a_k}$。例如 $53=110101_2$，$W(53,x)=R(1,x)R(3,x)R(5,x)R(6,x)$。

---

## 8. 可分 Hilbert 空間

[▶ part 2 12:15](https://youtu.be/kmy0xwKHJ_g?t=735) 課本 Definition 3.4.20–Example 3.4.23。

**定義**：Hilbert 空間叫**可分（separable）**，如果它含有一個**完備的正規正交數列**。有限維 Hilbert 空間也算可分。

講者：要另外說有限維，是因為「數列」通常是無限長的。

**例**：$L^2([-\pi,\pi])$ 可分（Example 3.4.16）；$\ell^2$ 可分（$e_n$）。

**不可分的例子**（Example 3.4.23）[▶ part 2 14:10](https://youtu.be/kmy0xwKHJ_g?t=850)：

$$H=\left\{f:\mathbb{R}\to\mathbb{C}\ :\ f\text{ 只在可數多個點不為 0，且 }\sum_{f(x)\ne0}|f(x)|^2<\infty\right\},$$

$$\langle f,g\rangle=\sum_{f(x)\overline{g(x)}\ne0}f(x)\overline{g(x)}\quad(\text{可數和}).$$

課本：$H$ 不可分，因為對**任何**數列 $f_n\in H$，都有非零的 $f$ 使 $\langle f,f_n\rangle=0$ 對所有 $n$。講者：這違反今天證的 Theorem 3.4.14；而且不是對某一個數列，而是對**每一個**數列都發生。

> 以下**不是逐字稿內容**，是補上課本那句話的理由：每個 $f_n$ 只在可數多個點不為 0，所以所有 $f_n$ 的非零點合起來還是可數集 $C$。$\mathbb{R}$ 不可數，取 $x_0\notin C$，令 $f=\chi_{\{x_0\}}$。則 $\langle f,f_n\rangle=0$ 對所有 $n$，但 $f\ne0$。由 Theorem 3.4.14，沒有任何正規正交數列是完備的。這個空間的正規正交基底是 $\{\chi_{\{x\}}:x\in\mathbb{R}\}$，**不可數**——正好回答第 1 節講者的疑問。

【課本補充】課本接著說：「本書只考慮可分的 Hilbert 空間。」

講者：「這節長得離譜，我們還需要一天。」[▶ part 2 16:36](https://youtu.be/kmy0xwKHJ_g?t=996)

---

## 9. 一頁速查表

| 項目 | 內容 | 關鍵一步 |
|---|---|---|
| span 稠密 | 完備正規正交數列的有限組合在 $E$ 稠密 | 部分和收斂到 $x$；閉包 = 極限集 |
| Thm 3.4.14 | 完備 ⟺ ($\langle x,x_n\rangle=0$ ∀$n$ ⟹ $x=0$) | ⟸ $z=\sum\langle y,x_j\rangle x_j$ 存在，$\langle y-z,x_n\rangle=0$ |
| Parseval | 完備 ⟺ $\|x\|^2=\sum|\langle x,x_n\rangle|^2$ ∀$x$ | Bessel 等式兩邊同時 $\to0$ |
| 複指數 | $\frac{e^{inx}}{\sqrt{2\pi}}$ 在 $L^2([-\pi,\pi])$ 完備 | 證明在 §3.5 |
| $L^2([0,a])$ | $f=\sum\beta_ne^{2n\pi ix/a}$，$\beta_n=\frac1a\int_0^afe^{-2n\pi it/a}$ | $t=\frac a2(1+\frac x\pi)$ |
| 三角函數系 | $\frac1{\sqrt{2\pi}},\frac{\cos nx}{\sqrt\pi},\frac{\sin nx}{\sqrt\pi}$ | 積化和差 |
| 半幅 | $[0,\pi]$ 上 cos 系、sin 系各自完備 | |
| Rademacher | $\operatorname{sgn}\sin(2^m\pi x)$ 正規正交但不完備 | Walsh 函數補成完備 |
| 可分 | 有完備正規正交數列 | $L^2([-\pi,\pi])$、$\ell^2$ |
| 不可分 | 只在可數點非零、平方可和的函數 | 任何數列都有 $\chi_{\{x_0\}}$ 跟它正交 |

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 可分 ⟹ 可數稠密子集、正交集可數 | 第 23 集（Theorem 3.4.24–3.4.25） |
| 可分 Hilbert 空間都同構於 $\ell^2$ | 第 23 集（Theorem 3.4.27） |
| $e^{inx}$ 的完備性 | §3.5（Fejér 核論證） |
| 正交補 | 第 23 集：投影定理 |
| 三角級數、半幅展開 | 第 29–30 集：分離變數、Sturm–Liouville |

---

## 附：本集一句話總結

> **在 Hilbert 空間裡，一個正規正交數列「完備」有好幾種等價說法：每個向量都能展開、它的有限組合稠密、只有 0 跟它全部正交、Parseval 公式 $\|x\|^2=\sum|\langle x,x_n\rangle|^2$ 成立；複指數函數、三角函數、Walsh 函數都是完備的例子，有這種可數完備系的空間叫可分——而只在可數點非零的函數空間就不是。**

---

*筆記依據 James Cook（待確認）「Hilbert Spaces」2023-03-08 錄影逐字稿（YouTube 自動字幕，part 1 59:51 ＋ part 2 17:17）與 Debnath & Mikusiński《Hilbert Spaces with Applications》3rd ed. §3.4 整理。*
