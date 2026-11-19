---
course: Number Theory（2021 秋，線上錄影）
episode: 11
lecture: 2021-09-18 第 1 部
date: 2021-09-18
video: https://youtu.be/NMBZuUuHnVg
notes: Jones & Jones《Elementary Number Theory》附錄 B：元素的階、循環群 C_n 的子群、同構（書頁 244，PDF 頁 259）；講者講義主要取自 Gallian《Contemporary Abstract Algebra》，課本無專節
---

# 第 11 集 · 循環群短期課程（二）（Short Course in Cyclic Groups, Part 2） [▶ 影片](https://youtu.be/NMBZuUuHnVg)

← 上一集：[10-order-of-elements-subgroups-of-z20](10-order-of-elements-subgroups-of-z20.md) ｜ [總目錄](README.md) ｜ 下一集：[12-structure-of-un](12-structure-of-un.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 11 集（2021-09-18 第 1 部）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（48:16，whisper 轉錄；48:34 之後是 whisper 亂編的句子，已略過）＋ Jones & Jones《Elementary Number Theory》附錄 B
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 快速複習](#1-快速複習)
- [2. 同階的循環群只有一個](#2-同階的循環群只有一個)
- [3. 次方什麼時候相等](#3-次方什麼時候相等)
- [4. 三個推論](#4-三個推論)
- [5. ⟨aᵏ⟩ = ⟨a^gcd(n,k)⟩，|aᵏ| = n / gcd(n,k)](#5-aᵏ--agcdnkaᵏ--n--gcdnk)
- [6. 誰是生成元](#6-誰是生成元)
- [7. 例子：U₁₄、5 階、8 階循環群](#7-例子u5-階8-階循環群)
- [8. 循環群基本定理（證明）](#8-循環群基本定理證明)
- [9. d 階元素有幾個](#9-d-階元素有幾個)
- [10. 例子：U₂₀ 不是循環群](#10-例子u-不是循環群)
- [11. 一頁速查表](#11-一頁速查表)
- [12. 與後續集數的連結](#12-與後續集數的連結)

---

## 0. 這堂課要做什麼

這部是講者**在家錄的講義導讀**（日期 9-18-21，是星期六）。他做了一份循環群的講義，逐頁講解，會掃描放到課程網站。【口頭】講者提到他在生病（「是肺炎在講話」）。

⚠️ 播放清單在 8-31 和 9-18 之間沒有影片，中間的課堂內容沒有錄影。

【口頭】[▶ 06:28](https://youtu.be/NMBZuUuHnVg?t=388) 講者的態度：「對數論學生來說，**知道這些結果、會用它們**，比會重現證明更重要。」證明幾乎都是整除理論、Bézout 和定義的應用。但他「覺得有義務把整個證明都攤在桌上」。考試若要考證明，他會事先明講。

【口頭】[▶ 14:30](https://youtu.be/NMBZuUuHnVg?t=870) 講義主要取自 **Gallian 的抽象代數**，是他 2015–2016 年教抽象代數時寫的。定理編號（1.6.14、1.6.15、1.75、1.77、1.79）是他講義的編號。

| 主題 | 時間 |
|---|---|
| 複習第 9–10 集 | 00:00 |
| 同階循環群唯一 | 11:21 |
| $a^i=a^j$ 的條件 | 14:30 |
| $\langle a^k\rangle=\langle a^{\gcd(n,k)}\rangle$ | 21:26 |
| 生成元、例子 | 29:05 |
| 循環群基本定理證明 | 34:38 |
| $d$ 階元素個數 | 41:13 |
| $U_{20}$ 不是循環群 | 45:50 |

---

## 1. 快速複習

[▶ 00:00](https://youtu.be/NMBZuUuHnVg?t=0)

講者花約 11 分鐘複習第 9–10 集：群的定義、$\mathbb{Z}_n$ 與 $U_n$、$\varphi(p)=p-1$、$\varphi(p^n)$、子群判別法、循環子群、Lagrange 定理、生成元、$\mathbb{Z}_{20}$ 的子群。

新補充的一點 [▶ 02:09](https://youtu.be/NMBZuUuHnVg?t=129)：$\varphi(25) = 25-5 = 20$（上次講義漏寫）。

【口頭】[▶ 03:11](https://youtu.be/NMBZuUuHnVg?t=191) 計數上 $2^n$ 跟奇質數的冪差不多，但之後會看到 **$U_{2^n}$ 的結構**跟奇質數冪的 $U_{p^n}$ 不一樣。

講者說 Lagrange 定理這次**不證**：「我想你們在抽象代數課看過。」證法就是把群切成小塊（陪集）。

**這一系列的目標** [▶ 10:43](https://youtu.be/NMBZuUuHnVg?t=643)：$U_n$ 是循環群嗎？它到底長什麼樣？「不是每次都是循環群，但我們能說很多。」

---

## 2. 同階的循環群只有一個

[▶ 11:21](https://youtu.be/NMBZuUuHnVg?t=681)

> **定理**：在同構意義下，$n$ 階循環群只有一個。

**證明**：設 $G=\langle x\rangle$、$H=\langle y\rangle$ 都是 $n$ 階循環群。定義
$$\psi: G\to H,\qquad \psi(x^m) = y^m.$$

1. **送單位元素到單位元素**：$\psi(e_G)=\psi(x^0)=y^0=e_H$。（講者說「好兆頭」。）
2. **是同態**（homomorphism，保持運算）[▶ 12:22](https://youtu.be/NMBZuUuHnVg?t=742)：設 $a=x^m$、$b=x^n$，
   $$\psi(ab) = \psi(x^{m+n}) = y^{m+n} = y^my^n = \psi(a)\psi(b).$$
3. **映成**：任取 $z\in H$，$z=y^n$，則 $\psi(x^n)=z$。
4. **一對一**：講者說 $G,H$ 都是有限集合、元素個數一樣，映成就自動一對一（「這只是集合論」）。他講義裡也直接證了：$\psi(a)=\psi(b)$ ⇒ $y^m=y^n$ ⇒ … ⇒ $a=b$。

所以 $\psi$ 是同構。∎

> 以下**不是逐字稿內容**，是補一個講者帶過的細節：$\psi$ 要是**函數**，得先確認「$x^m = x^{m'}$ ⇒ $y^m = y^{m'}$」（同一個元素寫成不同次方時，送去的值要一樣）。由第 3 節的定理，$x^m=x^{m'}\iff n\mid m-m'\iff y^m=y^{m'}$（兩者的階都是 $n$），所以沒問題。

【口頭】[▶ 13:59](https://youtu.be/NMBZuUuHnVg?t=839) 所以講者說「那就是 7 階循環群」好像故事結束了——**在記號之外**確實結束了。用加法或乘法寫，都只有一個。

講者的證明用 $e_G$、$e_H$ 區分兩個群的單位元素；他說在抽象代數講義裡他都只寫 $e$，「一直區分會很煩」。

---

## 3. 次方什麼時候相等

[▶ 14:30](https://youtu.be/NMBZuUuHnVg?t=870)

講者說這是「後面很多東西的**技術關鍵**（linchpin）」，給出在循環群裡計算的規則。

> **定理**：$G$ 是群、$a\in G$。
> 1. 若 $|a|=\infty$：$i\neq j\implies a^i\neq a^j$。（所有次方都不同。）
> 2. 若 $|a|=n$：
>    $$\langle a\rangle = \{e, a, a^2,\dots,a^{n-1}\},$$
>    這 $n$ 個**互不相同**；而且
>    $$a^i = a^j\iff n\mid i-j.$$

【口頭】無限的情況，主要的例子是 $\mathbb{Z}$：$i\cdot 1 = j\cdot 1$ 就表示 $i=j$。

**證明 1.** [▶ 16:09](https://youtu.be/NMBZuUuHnVg?t=969) 假設 $i>j$ 且 $a^i=a^j$。兩邊乘 $a^{-j}$：$a^{i-j}=e$。所以 $|a|\le i-j<\infty$，矛盾。

**證明 2.**

- **沒有重複**：假設 $0\le j<i<n$ 且 $a^i=a^j$。乘 $a^{-j}$ 得 $a^{i-j}=e$，而 $0<i-j<n$，跟「$n$ 是最小的」矛盾。
- **只有這 $n$ 個** [▶ 17:11](https://youtu.be/NMBZuUuHnVg?t=1031)：任取整數 $k$，除法演算法 $k=qn+r$、$0\le r<n$。
  $$a^k = a^{qn+r} = (a^n)^q\,a^r = e^q\,a^r = a^r.$$
  所以每個次方都等於 $a^0,\dots,a^{n-1}$ 之一。
- **$a^i=a^j\Rightarrow n\mid i-j$** [▶ 18:17](https://youtu.be/NMBZuUuHnVg?t=1097)：$a^{i-j}=e$。除法演算法 $i-j = qn+r$，同上得 $a^r = e$。$0\le r<n$，而 $n$ 是最小的正次方，所以 $r=0$，$n\mid i-j$。
- **反過來**：$i-j = qn$ ⇒ $a^{i-j} = (a^n)^q = e$ ⇒ $a^i=a^j$。∎

【口頭】講者說他讓抽象代數學生負責證這個，但「不預期要你們證，我要你們懂這個定理」。

---

## 4. 三個推論

[▶ 20:25](https://youtu.be/NMBZuUuHnVg?t=1225)

> **推論 A**：在 $n$ 階循環群裡，$a^i=a^j\iff i = j+nk$（某個整數 $k$）。

> **推論 B**：$|a| = |\langle a\rangle|$。
> 「非常重要，把元素的階連到它生成的子群的階。我們一直在用。」

> **推論 C**（講者講義 1.6.14）：若 $|a|=n$ 且 $a^k=e$，則 $n\mid k$。
> **證明**：$a^k = e = a^0$，由第 3 節，$n\mid k-0$。

白話：**某個次方回到 $e$，那個次方一定是階的倍數。**

---

## 5. ⟨aᵏ⟩ = ⟨a^gcd(n,k)⟩，|aᵏ| = n / gcd(n,k)

[▶ 21:26](https://youtu.be/NMBZuUuHnVg?t=1286)

> **定理**（講者講義 1.6.15）：$|a|=n$，$k\in\mathbb{N}$。則
> $$\langle a^k\rangle = \langle a^{\gcd(n,k)}\rangle,\qquad |a^k| = \frac{n}{\gcd(n,k)}.$$

**證明**：令 $d=\gcd(n,k)$。

**($\subseteq$)** [▶ 22:29](https://youtu.be/NMBZuUuHnVg?t=1349) $d\mid k$，寫 $k=cd$。若 $x\in\langle a^k\rangle$，$x = (a^k)^y = a^{cdy} = (a^d)^{cy}\in\langle a^d\rangle$。

**($\supseteq$)** [▶ 24:04](https://youtu.be/NMBZuUuHnVg?t=1444) 若 $w\in\langle a^d\rangle$，$w = a^{du}$。由 **Bézout**，存在 $p,q$ 使 $pn+qk = d$。則
$$w = a^{du} = a^{(pn+qk)u} = (a^n)^{pu}\,(a^k)^{qu} = e\cdot(a^k)^{qu}\in\langle a^k\rangle.$$

所以兩個子群相等。

**階** [▶ 25:04](https://youtu.be/NMBZuUuHnVg?t=1504)：

1. $n/d$ 是整數（$d\mid n$）。$(a^d)^{n/d} = a^n = e$，所以 $|a^d|\le n/d$。
2. 若 $0<i<n/d$，則 $0<di<n$，所以 $(a^d)^i = a^{di}\neq e$（$n$ 是 $a$ 的階）。
3. 所以 $|a^d| = n/d$。
4. 由推論 B，$|a^k| = |\langle a^k\rangle| = |\langle a^d\rangle| = |a^d| = n/d$。∎

**推論** [▶ 27:05](https://youtu.be/NMBZuUuHnVg?t=1625)：若 $|a|=n$，則
$$\langle a^i\rangle = \langle a^j\rangle\iff\gcd(n,i) = \gcd(n,j).$$

- (⇐) 兩邊都等於 $\langle a^{\gcd}\rangle$。
- (⇒) 子群相等 ⇒ 階相等 ⇒ $n/\gcd(n,i) = n/\gcd(n,j)$ ⇒ gcd 相等。

**例子** [▶ 28:35](https://youtu.be/NMBZuUuHnVg?t=1715)：10 階循環群裡，$\gcd(10,4) = 2 = \gcd(10,8)$，所以 $\langle a^4\rangle = \langle a^8\rangle$。

【口頭】「**群的階很重要**。生成什麼，永遠是相對於你所在的群的大小來判斷。」

---

## 6. 誰是生成元

[▶ 29:05](https://youtu.be/NMBZuUuHnVg?t=1745)

> **推論**：$G=\langle a\rangle$、$|G|=n$。則
> $$G = \langle a^k\rangle\iff\gcd(k,n)=1.$$

**證明**：由上面的推論，$\langle a^k\rangle = \langle a^1\rangle\iff\gcd(n,k) = \gcd(n,1) = 1$。∎

（第 10 集只講了 ⇐，這裡兩個方向都有。）

> **特例** [▶ 30:06](https://youtu.be/NMBZuUuHnVg?t=1806)：$k\in\mathbb{Z}_n$ 是 $\mathbb{Z}_n$ 的生成元 $\iff\gcd(k,n)=1$。
> 也就是說：**$\mathbb{Z}_n$ 的生成元恰好就是 $U_n$ 裡的元素。**

講者：「這對我們的思考非常關鍵。」

---

## 7. 例子：U₁₄、5 階、8 階循環群

**$U_{14}$ 是循環群** [▶ 31:07](https://youtu.be/NMBZuUuHnVg?t=1867)

$U_{14} = \{1,3,5,9,11,13\}$，$|U_{14}|=6$。算 $3$ 的次方（模 14）：

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $3^k$ | 3 | 9 | $27\equiv13$ | $39\equiv11$ | $33\equiv5$ | $15\equiv1$ |

六個元素全跑出來了（順序不同），所以 $U_{14} = \langle 3\rangle$ 是循環群。

另一個生成元：跟 6 互質的是 $1,5$，所以 $3^5\equiv 5$ 也是生成元。$U_{14}=\langle 3\rangle = \langle 5\rangle$。

講者強調：**不是每個 $U_n$ 都是循環群**（見第 10 節）。

**5 階循環群** [▶ 32:08](https://youtu.be/NMBZuUuHnVg?t=1928)：$2,3,4$ 都跟 5 互質，所以
$$\langle a\rangle = \langle a^2\rangle = \langle a^3\rangle = \langle a^4\rangle.$$
有 $\varphi(5)=4$ 個生成元：給任何一個生成元，它的平方、立方、四次方也都是生成元。

**8 階循環群** [▶ 33:08](https://youtu.be/NMBZuUuHnVg?t=1988)：

| 子群 | 元素 | 階 | 理由 |
|---|---|---|---|
| $\langle a\rangle=\langle a^3\rangle=\langle a^5\rangle=\langle a^7\rangle$ | 全部 | 8 | $\gcd(k,8)=1$ |
| $\langle a^2\rangle=\langle a^6\rangle$ | $e,a^2,a^4,a^6$ | 4 | $\gcd(2,8)=\gcd(6,8)=2$ |
| $\langle a^4\rangle$ | $e,a^4$ | 2 | $\gcd(4,8)=4$ |
| $\langle e\rangle$ | $e$ | 1 | — |

講者也從另一個角度看：$\langle a^2\rangle$ 是 4 階群，$\gcd(3,4)=1$，所以 $(a^2)^3 = a^6$ 也生成它。

---

## 8. 循環群基本定理（證明）

[▶ 34:38](https://youtu.be/NMBZuUuHnVg?t=2078)

> **循環群基本定理**（講者講義 1.75）：$G=\langle a\rangle$。
> 1. $G$ 的每個子群都是循環群。
> 2. 若 $|G|=n$、$H\le G$、$|H|=k$，則 $k\mid n$。
> 3. 若 $|G|=n$、$k\mid n$，則 $\langle a^{n/k}\rangle$ 是 $G$ **唯一**的 $k$ 階子群。

（講者口誤說「唯一的 $n/k$ 階子群」，證明裡是 $k$ 階。）

**判斷不是循環群的好工具** [▶ 35:43](https://youtu.be/NMBZuUuHnVg?t=2143)：如果一個群有**兩個** 5 階子群，它就**不是**循環群。

**證明 1**（子群都是循環群）[▶ 36:13](https://youtu.be/NMBZuUuHnVg?t=2173)

- $H=\{e\}$ 是循環群。以下設 $H\neq\{e\}$。
- 若 $a^k\in H$，則 $a^{-k}\in H$（對反元素封閉）。所以 $H$ 裡有 $a$ 的**正**次方。
- 令 $\Lambda = \{\,m\in\mathbb{N} : a^m\in H\,\}$，非空。由良序原理，有最小元素 $t$。
- **主張 $H=\langle a^t\rangle$**：
  - $a^t\in H$，所以 $(a^t)^s\in H$，$\langle a^t\rangle\subseteq H$。
  - 任取 $a^k\in H$。除法演算法 $k = qt+r$，$0\le r<t$。則 [▶ 37:43](https://youtu.be/NMBZuUuHnVg?t=2263)
    $$a^r = a^{-qt}\,a^k.$$
    $a^{-qt} = (a^t)^{-q}\in H$、$a^k\in H$，所以 $a^r\in H$。
  - **關鍵一步**：$t$ 是最小的正次方，而 $0\le r<t$，所以 $r=0$。於是 $a^k = (a^t)^q\in\langle a^t\rangle$。
- 所以 $H=\langle a^t\rangle$ 是循環群。

**證明 2**（$k\mid n$）[▶ 38:43](https://youtu.be/NMBZuUuHnVg?t=2323)：由 1，$H = \langle a^t\rangle$。$(a^t)^n = (a^n)^t = e$，由推論 C，$|a^t|$ 整除 $n$。而 $|a^t| = |H| = k$。

【口頭】「這我們早就由 Lagrange 定理知道，但這段論證**不用 Lagrange**，自給自足，滿好的。」

**證明 3**（唯一）[▶ 39:43](https://youtu.be/NMBZuUuHnVg?t=2383)

- **存在**：由第 5 節，$|\langle a^{n/k}\rangle| = \dfrac{n}{\gcd(n,\,n/k)} = \dfrac{n}{n/k} = k$。
- **唯一**：設 $H'$ 是另一個 $k$ 階子群。由 1，$H'=\langle a^t\rangle$，而且可以取 $t\mid n$（取 $t=\gcd(t,n)$，第 5 節保證生成同一個子群）。則
  $$k = |a^t| = \frac{n}{\gcd(n,t)} = \frac nt,$$
  所以 $t = n/k$，$H' = \langle a^{n/k}\rangle$。∎

【口頭】[▶ 41:13](https://youtu.be/NMBZuUuHnVg?t=2473) 「其實滿好學的。我當學生時如果考試沒預期要證，可能會有點嚇到。但我要考的話會先說。我又不是怪物。」

---

## 9. d 階元素有幾個

[▶ 41:13](https://youtu.be/NMBZuUuHnVg?t=2473)

> **定理**（講者講義 1.77）：$G$ 是 $n$ 階循環群、$d$ 是 $n$ 的正因數。則 $G$ 裡**階為 $d$ 的元素恰有 $\varphi(d)$ 個**。

**證明**（講者說他講義的句子寫得不太對，口頭重講）：

1. 由基本定理，$G$ 恰有一個 $d$ 階子群 $H$，而且 $H=\langle b\rangle$，$|b|=d$。
2. 任何 $d$ 階元素 $x$ 生成的 $\langle x\rangle$ 也是 $d$ 階子群，所以 $\langle x\rangle = H$。也就是說：**$d$ 階元素 = $H$ 的生成元**。
3. 由第 6 節，$H$ 的生成元是 $b^k$ 且 $\gcd(k,d)=1$，共 $\varphi(d)$ 個。∎

**例子** [▶ 42:44](https://youtu.be/NMBZuUuHnVg?t=2564)：$G$ 是 $19k$ 階循環群（任意 $k$）。$19\mid|G|$，所以 19 階元素有 $\varphi(19) = 18$ 個。「不管在 $\mathbb{Z}_{19}$ 還是 $\mathbb{Z}_{19000000}$，都是 18 個。」

> **推論**（講者講義 1.79）[▶ 43:44](https://youtu.be/NMBZuUuHnVg?t=2624)：在**任何有限群**裡（不一定是循環群），$d$ 階元素的個數是 $\varphi(d)$ 的倍數。

**證明**：

- 沒有 $d$ 階元素：個數 $0$，是 $\varphi(d)$ 的倍數。
- 有一個 $d$ 階元素 $a$：$\langle a\rangle$ 是 $d$ 階循環群，裡面有 $\varphi(d)$ 個 $d$ 階元素。
- 若還有 $d$ 階元素 $b\notin\langle a\rangle$：$\langle b\rangle$ 也貢獻 $\varphi(d)$ 個。**這兩批不重疊** [▶ 44:14](https://youtu.be/NMBZuUuHnVg?t=2654)：若 $x$ 是兩者共同的 $d$ 階元素，則 $\langle a\rangle = \langle x\rangle = \langle b\rangle$（都是 $d$ 階循環群裡的生成元），推出 $b\in\langle a\rangle$，矛盾。
- 繼續下去，群是有限的，最後用完所有 $d$ 階元素。每批 $\varphi(d)$ 個，所以總數是 $\varphi(d)$ 的倍數。∎

【口頭】「所以就算不是循環群，也不是蠻荒西部，個數不能是隨便一個數，一定是 $\varphi(d)$ 的倍數。」

---

## 10. 例子：U₂₀ 不是循環群

[▶ 45:50](https://youtu.be/NMBZuUuHnVg?t=2750)

$U_{20} = \{1,3,7,9,11,13,17,19\}$，$|U_{20}| = \varphi(20) = 8$。

**2 階元素**：

$$9^2 = 81\equiv 1,\qquad 11^2 = 121\equiv 1,\qquad 19^2 = 361\equiv 1\pmod{20}.$$

$9,11,19$ 都是 2 階，所以有**三個** 2 階子群 $\{1,9\},\{1,11\},\{1,19\}$。由基本定理，循環群只能有一個 2 階子群，所以 **$U_{20}$ 不是循環群**。

**4 階元素** [▶ 46:21](https://youtu.be/NMBZuUuHnVg?t=2781)：看次方什麼時候「繞回來」。

$$3^2 = 9,\ 3^4 = 81\equiv 1;\qquad 7^2 = 49\equiv 9,\ 7^4\equiv 1;\qquad 13^2=169\equiv 9;\qquad 17^2 = 289\equiv 9.$$

$3,7,13,17$ 都是 4 階，共 4 個 $= 2\times\varphi(4)$。正好示範了推論 1.79：個數是 $\varphi(4)=2$ 的倍數。

（2 階元素 3 個 $= 3\times\varphi(2)$，也符合。）

講者說下一個大主題是**群的直積**，「這是停下來吃早餐的好地方」，接第 12 集。

> 【課本補充】附錄 B（p. 244）只簡短陳述了本集的幾個結果：元素的階整除 $|G|$；$n$ 階循環群記作 $C_n$，對每個 $m\mid n$ 恰有一個 $m$ 階子群（生成元 $c^{n/m}$），沒有別的子群；同構的定義。課本沒有證明，本集的證明都來自講者（Gallian 風格）的講義。

---

## 11. 一頁速查表

**同階循環群唯一**：$\psi(x^m)=y^m$ 是同構。

**次方相等**（$|a|=n$）：$\langle a\rangle=\{e,a,\dots,a^{n-1}\}$ 互不相同；$a^i=a^j\iff n\mid i-j$。

- **關鍵一步**：$k=qn+r$ ⇒ $a^k=a^r$。
- $a^k=e\Rightarrow n\mid k$；$|a|=|\langle a\rangle|$。

**gcd 定理**：$\langle a^k\rangle=\langle a^{\gcd(n,k)}\rangle$，$|a^k|=n/\gcd(n,k)$。

- **關鍵一步**（$\supseteq$）：Bézout $pn+qk=d$ ⇒ $a^{du}=(a^n)^{pu}(a^k)^{qu}$。
- $\langle a^i\rangle=\langle a^j\rangle\iff\gcd(n,i)=\gcd(n,j)$。
- $a^k$ 是生成元 $\iff\gcd(k,n)=1$。$\mathbb{Z}_n$ 的生成元 = $U_n$ 的元素。

**基本定理**：子群都是循環群；$k\mid n$ ⇒ 唯一 $k$ 階子群 $\langle a^{n/k}\rangle$。

- **子群是循環群的關鍵一步**：取最小的 $t$ 使 $a^t\in H$；$k=qt+r$ ⇒ $a^r\in H$ ⇒ $r=0$。

**$d$ 階元素個數**：循環群裡恰 $\varphi(d)$ 個；任何有限群裡是 $\varphi(d)$ 的倍數。

**例子**

| 群 | 結論 |
|---|---|
| $U_{14}$ | $=\langle 3\rangle=\langle5\rangle$，循環群 |
| $U_{20}$ | 2 階元素 $9,11,19$（三個 2 階子群）⇒ 不是循環群；4 階元素 $3,7,13,17$ |
| $19k$ 階循環群 | 19 階元素 18 個 |

---

## 12. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 群的直積、$U_{mn}\cong U_m\times U_n$ | 第 12 集 |
| $U_n$ 什麼時候是循環群（原根） | 第 12 集 |
| $a^k=e\Rightarrow|a|\mid k$ ⇒ Euler 定理 | 第 12–13 集 |
| 用「子群唯一性」判斷不是循環群 | 第 12 集、作業 |
| 子群都是循環的 ⇔ 「主理想」的類比 | 第 29 集起（理想）、第 36–39 集（PID） |

---

## 附：本集一句話總結

> **$|a|=n$ 時，$a^i=a^j$ 恰好在 $n\mid i-j$ 時成立，而 $a^k$ 生成的子群只看 $\gcd(n,k)$：$|a^k|=n/\gcd(n,k)$。由此得到循環群基本定理——子群都循環、每個因數恰一個子群——以及「$d$ 階元素有 $\varphi(d)$ 個」，用它一眼看出 $U_{20}$ 不是循環群。**

---

## ⚠️ 待確認清單

1. 播放清單在 2021-08-31（第 10 集）和 2021-09-18（本集）之間沒有影片。這段期間有沒有上課、講了什麼，逐字稿裡沒有交代。本集開頭講者說「前幾頁上次已經講過好幾次」，複習的都是第 9–10 集的內容。

---

*筆記依據 James S. Cook「Number Theory」2021-09-18 第 1 部錄影逐字稿（whisper 轉錄，48:16）與 Jones & Jones《Elementary Number Theory》附錄 B 整理。*
