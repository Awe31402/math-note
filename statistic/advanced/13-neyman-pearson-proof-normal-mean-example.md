---
course: 高等統計學（數理統計續）
episode: 13
lecture: Lec13（第七週 2/2）
date: 待補
video: https://youtu.be/HH5AdGTQAX4
notes: Hogg 8th ed. Theorem 8.1.1 Neyman–Pearson 與證明（p. 472）；Example 8.1.2 常態平均數（p. 475）
---

# 第 13 集 · 第七週 (2/2)：Neyman–Pearson 定理的證明；找 k 的轉換技巧；例：N(θ,1) 的最強力檢定 [▶ 影片](https://youtu.be/HH5AdGTQAX4)

← 上一集：[12](12-likelihood-ratio-neyman-pearson-statement.md) ｜ [總目錄](../README.md) ｜ 下一集：[14](14-poisson-mp-test-ump-definition.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 13 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 1:09:00，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §8.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Neyman–Pearson」→「Nayman Pearson／雷曼皮爾審」，「likelihood」→「Likely／Ligreehood／Lugly」，「若且唯若」→「若且為若／弱且微弱」，「$\alpha$」→「阿華／阿花／R」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：最強力檢定與定理敘述](#1-複習最強力檢定與定理敘述)
- [2. 定理的證明](#2-定理的證明)
- [3. 怎麼找 k：一對一轉換](#3-怎麼找-k一對一轉換)
- [4. 例：N(θ,1)，H₀:θ=0 vs H₁:θ=1](#4-例nθ1h₀θ0-vs-h₁θ1)
- [5. 為什麼要懂觀念](#5-為什麼要懂觀念)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

【口頭】[▶ 00:30](https://youtu.be/HH5AdGTQAX4?t=30) 這個證明要好好看，考試會考證明。

| 主題 | 課本 |
|---|---|
| Neyman–Pearson 定理證明 | Theorem 8.1.1，p. 472 |
| 用一對一轉換找 $k$ | §8.1 |
| 例：$N(\theta,1)$ | Example 8.1.2，p. 475 |

---

## 1. 複習：最強力檢定與定理敘述

[▶ 01:01](https://youtu.be/HH5AdGTQAX4?t=61) Neyman–Pearson 處理的是**簡單假設**：$H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$。

[▶ 02:01](https://youtu.be/HH5AdGTQAX4?t=121) 最強力：在所有型一錯誤 $\le\alpha$ 的檢定中，$H_1$ 為真時 power 最大（＝型二錯誤最小）。

【口頭】[▶ 02:32](https://youtu.be/HH5AdGTQAX4?t=152) 將來不管去哪裡說服人家，要先講清楚**什麼叫最好**。沒講清楚就說「我這個最好」，很爛也可以說很好。

**定理**（[▶ 05:33](https://youtu.be/HH5AdGTQAX4?t=333)）：
$$C=\left\{\mathbf x:\frac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}\le k\right\},\qquad P_{\theta_0}(\mathbf X\in C)=\alpha$$
⇒ $C$ 是 size $\alpha$ 的最強力拒絕域。

- [▶ 07:15](https://youtu.be/HH5AdGTQAX4?t=435) $C$ 依賴 $k$：$k$ 越大，比值 $\le k$ 的點越多，$C$ 越大。
- [▶ 08:16](https://youtu.be/HH5AdGTQAX4?t=496) 最好的拒絕域型一錯誤一定**剛好**等於 $\alpha$：若比 $\alpha$ 小，一定有比它更好的。

---

## 2. 定理的證明

[▶ 09:16](https://youtu.be/HH5AdGTQAX4?t=556) **記號**：$B$ 是樣本空間的任一子集，

$$P_\theta(\mathbf X\in B)=\pi_B(\theta)=\int\!\cdots\!\int_BL(\theta;x_1,\dots,x_n)\,dx_1\cdots dx_n\ \equiv\ \int_BL(\theta).$$

（joint pdf＝概似函數；寫一個積分號代表 $n$ 重積分，是對 $x_1,\dots,x_n$ 積分，$\theta$ 固定。）

【口頭】[▶ 10:17](https://youtu.be/HH5AdGTQAX4?t=617) 任何隨機變數落在 $A$ 的機率，就是它的 pdf 在 $A$ 上的積分。一定要記得。

**要證**（[▶ 13:25](https://youtu.be/HH5AdGTQAX4?t=805)）：對任何 $A$ 滿足
$$\int_AL(\theta_0)\le\alpha\qquad(\text{A 的型一錯誤}\le\alpha),$$
都有
$$\int_CL(\theta_1)\ge\int_AL(\theta_1)\qquad(\pi_C(\theta_1)\ge\pi_A(\theta_1)).$$

**Step 1：拆集合**（[▶ 18:36](https://youtu.be/HH5AdGTQAX4?t=1116)）。$C=(C\cap A)\cup(C\cap A^c)$、$A=(A\cap C)\cup(A\cap C^c)$，都是互斥聯集：
$$\int_CL(\theta_1)-\int_AL(\theta_1)=\int_{C\cap A}L(\theta_1)+\int_{C\cap A^c}L(\theta_1)-\int_{A\cap C}L(\theta_1)-\int_{A\cap C^c}L(\theta_1).$$
$C\cap A=A\cap C$，消掉：
$$=\int_{C\cap A^c}L(\theta_1)-\int_{A\cap C^c}L(\theta_1).$$

**Step 2：用比值換掉 $L(\theta_1)$**（[▶ 21:18](https://youtu.be/HH5AdGTQAX4?t=1278)）

- $C\cap A^c\subset C$：在 $C$ 裡 $\frac{L(\theta_0)}{L(\theta_1)}\le k$ ⇒ $L(\theta_1)\ge\frac1kL(\theta_0)$。
- $A\cap C^c\subset C^c$：在 $C$ 外 $\frac{L(\theta_0)}{L(\theta_1)}>k$ ⇒ $L(\theta_1)<\frac1kL(\theta_0)$。

[▶ 24:24](https://youtu.be/HH5AdGTQAX4?t=1464) 前一項大的換成小的（變小）；後一項小的換成大的，但前面有負號（也變小）。兩邊都變小：
$$\ge\frac1k\left[\int_{C\cap A^c}L(\theta_0)-\int_{A\cap C^c}L(\theta_0)\right].$$

**Step 3：加回交集**（[▶ 26:32](https://youtu.be/HH5AdGTQAX4?t=1592)）。兩項各加上 $\int_{C\cap A}L(\theta_0)=\int_{A\cap C}L(\theta_0)$（一加一減，不變）：
$$=\frac1k\left[\int_CL(\theta_0)-\int_AL(\theta_0)\right].$$

**Step 4：用 size**（[▶ 27:35](https://youtu.be/HH5AdGTQAX4?t=1655)）。$\int_CL(\theta_0)=P_{\theta_0}(\mathbf X\in C)=\alpha$；$\int_AL(\theta_0)\le\alpha$。所以括號 $\ge 0$；$k>0$ ⇒
$$\int_CL(\theta_1)-\int_AL(\theta_1)\ge 0.$$

**結論**（[▶ 28:40](https://youtu.be/HH5AdGTQAX4?t=1720)）：$\pi_C(\theta_1)\ge\pi_A(\theta_1)$，對任何型一錯誤 $\le\alpha$ 的 $A$ 都成立。$C$ 是最強力拒絕域。∎

【口頭】技巧就在 Step 2：觀念清楚的話，證明有一點技巧但不困難。

---

## 3. 怎麼找 k：一對一轉換

[▶ 30:41](https://youtu.be/HH5AdGTQAX4?t=1841) 定理告訴你 $C$ 長什麼樣子，比值也算得出來（把 $\theta_0$、$\theta_1$ 代進概似函數），**唯一不知道的是 $k$**。

**直接做的困難**（[▶ 32:42](https://youtu.be/HH5AdGTQAX4?t=1962)）：要解
$$P_{\theta_0}\left(\frac{L(\theta_0;\mathbf X)}{L(\theta_1;\mathbf X)}\le k\right)=\alpha.$$
兩種算法：

1. 對 joint pdf 積分，範圍是比值 $\le k$ 的點；
2. 把比值 $Y=\frac{L(\theta_0;\mathbf X)}{L(\theta_1;\mathbf X)}$ 當成一個隨機變數，$\int_{-\infty}^kf_Y(y)\,dy=\alpha$。

困難：$Y$ 的分配通常**不知道**。

【口頭】[▶ 37:38](https://youtu.be/HH5AdGTQAX4?t=2258) 這兩種算法其實一樣：$P(g(X,Y)\in A)$ 可以對 $(X,Y)$ 的 joint pdf 在 $\{(x,y):g(x,y)\in A\}$ 上積分，也可以令 $Z=g(X,Y)$、對 $Z$ 的 pdf 在 $A$ 上積分。統計和機率裡常交互使用，但大家不太清楚兩者是同一件事。困難在於找 $Z$ 的 pdf。

**轉換方法**（[▶ 42:53](https://youtu.be/HH5AdGTQAX4?t=2573)）：給定 $k$，若存在常數 $c$ 和函數 $u$，使得
$$\frac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}\le k\iff u(x_1,\dots,x_n)\le c\ \ (\text{或}\ \ge c,\text{只有一個成立}),$$
而且 **$u(X_1,\dots,X_n)$ 的分配知道**，那麼：

- 兩個不等式成立的點完全一樣 ⇒ 兩個集合是同一個事件 ⇒ $\{u\le c\}$ 也是最強力拒絕域。
- [▶ 45:58](https://youtu.be/HH5AdGTQAX4?t=2758) 用 $u$ 的分配解 $P_{\theta_0}(u(\mathbf X)\le c)=\alpha$ 找 $c$；有 $c$ 就有 $k$（一一對應），**不必真的去找 $k$**。
- [▶ 47:00](https://youtu.be/HH5AdGTQAX4?t=2820) $u$ 不唯一。十個人找十個答案，寫法不同，集合都一樣，都對。
- 一對一轉換做幾次都可以，合起來還是一對一。

---

## 4. 例：N(θ,1)，H₀:θ=0 vs H₁:θ=1

[▶ 54:11](https://youtu.be/HH5AdGTQAX4?t=3251)（課本 Example 8.1.2）$X_1,\dots,X_n$ iid $N(\theta,1)$（變異數已知為 1）。
$$H_0:\theta=0\quad\text{vs}\quad H_1:\theta=1.$$
找 size $\alpha$ 的最強力拒絕域。由 Neyman–Pearson 一定存在。

**概似函數**（[▶ 55:50](https://youtu.be/HH5AdGTQAX4?t=3350)）：
$$L(\theta;\mathbf x)=\prod_{i=1}^n\frac{1}{\sqrt{2\pi}}e^{-\frac12(x_i-\theta)^2}=(2\pi)^{-n/2}\exp\left\{-\frac12\left[\sum x_i^2-2\theta\sum x_i+n\theta^2\right]\right\}.$$

**概似比**（[▶ 57:57](https://youtu.be/HH5AdGTQAX4?t=3477)）：
$$\frac{L(0;\mathbf x)}{L(1;\mathbf x)}=\frac{(2\pi)^{-n/2}\exp\left\{-\frac12\sum x_i^2\right\}}{(2\pi)^{-n/2}\exp\left\{-\frac12\left[\sum x_i^2-2\sum x_i+n\right]\right\}}.$$

[▶ 59:36](https://youtu.be/HH5AdGTQAX4?t=3576) 直接讓它 $\le k$ 不可能算：這一大串東西的分配不可能知道。先化簡：$(2\pi)^{-n/2}$ 和 $\sum x_i^2$ 消掉，
$$\frac{L(0;\mathbf x)}{L(1;\mathbf x)}=\exp\left\{-\sum x_i+\frac n2\right\}\le k.$$

**一連串一對一轉換**（[▶ 61:42](https://youtu.be/HH5AdGTQAX4?t=3702)）：

1. 取 $\ln$：$-\sum x_i+\frac n2\le\ln k$。
2. $\sum x_i=n\bar x$：$-n\bar x\le\ln k-\frac n2$。
3. [▶ 62:44](https://youtu.be/HH5AdGTQAX4?t=3764) 停在 $\bar x$，因為 $\bar X\sim N\left(\theta,\frac1n\right)$ 知道；$-n\bar X$ 的分配也找得到但麻煩。除以 $-n$（不等號反向）：
$$\bar x\ge-\frac1n\left(\ln k-\frac n2\right)\equiv c.$$

所以 $C=\{\mathbf x:\bar x\ge c\}$。

**找 $c$**（[▶ 65:16](https://youtu.be/HH5AdGTQAX4?t=3916)）：$H_0$ 為真（$\theta=0$）時 $\bar X\sim N\left(0,\frac1n\right)$，
$$P_{\theta=0}(\bar X\ge c)=P\left(\frac{\bar X-0}{1/\sqrt n}\ge\frac{c-0}{1/\sqrt n}\right)=P(Z\ge\sqrt nc)=\alpha.$$
所以 $\sqrt nc=z_\alpha$：

> **答案**（[▶ 67:19](https://youtu.be/HH5AdGTQAX4?t=4039)）：size $\alpha$ 的最強力拒絕域
> $$C=\left\{\mathbf x:\bar x\ge\frac{z_\alpha}{\sqrt n}\right\}.$$

[▶ 68:21](https://youtu.be/HH5AdGTQAX4?t=4101) 有 $c$ 就可以反解出 $k$，但不用去找，因為兩者一樣。

---

## 5. 為什麼要懂觀念

【口頭】[▶ 50:03](https://youtu.be/HH5AdGTQAX4?t=3003)

- 要讀懂例題，要先把虛無／對立假設怎麼定、兩種錯誤和機率、最強力檢定的定義、Neyman–Pearson 定理都搞清楚。
- 例題看起來很簡單，很容易就導出來；但很多人**會做不一定懂**：學技巧比較容易，學觀念比較難。
- [▶ 51:37](https://youtu.be/HH5AdGTQAX4?t=3097) 不懂想法只會用方法，就像背了一大堆三角函數公式卻不知道什麼是三角函數。
- [▶ 52:07](https://youtu.be/HH5AdGTQAX4?t=3127) 沒有一本書讓你去公司上班時翻到某一頁照抄。老闆叫你做假設檢定，如果他自己會就不會叫你做；也不會剛好書上就有。
- 讀書的目的是了解「在這樣的情境下，這是能做到最好的」。學通了，就有能力在不同環境創造屬於自己的方法；背下來一點幫忙都沒有。

---

## 6. 一頁速查表

**Neyman–Pearson**：$C=\left\{\frac{L(\theta_0)}{L(\theta_1)}\le k\right\}$，$P_{\theta_0}(\mathbf X\in C)=\alpha$ ⇒ 最強力。

**證明骨架**（$A$ 任意，$\int_AL(\theta_0)\le\alpha$）：
$$\int_CL(\theta_1)-\int_AL(\theta_1)=\int_{C\cap A^c}L(\theta_1)-\int_{A\cap C^c}L(\theta_1)\ge\frac1k\left[\int_{C\cap A^c}L(\theta_0)-\int_{A\cap C^c}L(\theta_0)\right]=\frac1k\left[\alpha-\int_AL(\theta_0)\right]\ge 0.$$
關鍵：在 $C$ 內 $L(\theta_1)\ge L(\theta_0)/k$；在 $C$ 外 $L(\theta_1)<L(\theta_0)/k$。

**找 $k$**：把「比值 $\le k$」一對一轉成「$u(\mathbf x)\le c$（或 $\ge c$）」，$u(\mathbf X)$ 分配已知，用 $P_{\theta_0}=\alpha$ 解 $c$。

**例**：$N(\theta,1)$，$H_0:\theta=0$ vs $H_1:\theta=1$：
$$\frac{L(0)}{L(1)}=e^{-\sum x_i+n/2}\le k\iff\bar x\ge c,\qquad c=\frac{z_\alpha}{\sqrt n}.$$

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 一對一轉換找 $c$ | 下一集：更多 Neyman–Pearson 例題 |
| 拒絕域不依賴 $\theta_1$ | 一致最強力檢定（UMP） |

---

## 附：本集一句話總結

> **Neyman–Pearson 的證明是把 $C$ 和任一 size $\le\alpha$ 的 $A$ 拆成交集與差集，在 $C$ 內外分別用 $L(\theta_1)\gtrless L(\theta_0)/k$ 換掉，得到 power 差 $\ge\frac1k(\alpha-\int_AL(\theta_0))\ge 0$；實際找拒絕域時，把概似比 $\le k$ 一對一轉成分配已知的統計量（如 $\bar X$）的不等式，用型一錯誤 $=\alpha$ 定出臨界值——$N(\theta,1)$ 的答案是 $\bar x\ge z_\alpha/\sqrt n$。**

---

*筆記依據「高等統計學」Lec13 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
