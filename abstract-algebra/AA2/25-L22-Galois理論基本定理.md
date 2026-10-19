---
course: Abstract Algebra II (Spring 2026)
episode: 25
lecture: L22
date: 2026-03-13
video: https://www.youtube.com/watch?v=XzUDV4DVU0A
notes: 講義/AA2/Math422_Lecture22_FundamentalTheoremGalois.pdf
---

# 第 25 集 · L22：Galois 理論基本定理 [▶ 影片](https://www.youtube.com/watch?v=XzUDV4DVU0A&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[24-L21-Galois擴張與Galois群]] ｜ [總目錄](../README.md) ｜ 下一集：[[26-L23-Galois理論例子-下]] →

## 本集概要

D&F §14.2：
- 回顧 $\mathbb{Q}(\sqrt2,\sqrt3)$：子體格和子群格「上下顛倒」地對應。
- 詳細算 $x^3-2$ 的分裂體 $K = \mathbb{Q}(\sqrt[3]2,\rho)$：6 次；自同構 $\sigma$（$\sqrt[3]2\mapsto\rho\sqrt[3]2$）、$\tau$（$\rho\mapsto\rho^2$）；$\sigma\tau = \tau\sigma^2$；Galois 群 $\cong S_3$。
- 只有正規子群 $\langle\sigma\rangle$ 對應的子體 $\mathbb{Q}(\rho)$ 是 Galois 的。
- 證明的工具（略講）：**特徵標**、自同構的線性獨立；$[K:K^G] = |G|$。
- **Galois 共軛**；**Galois 理論基本定理**。

> 📘 講義對應：Math422 Lecture 22「Fundamental Theorem of Galois Theory」；D&F §14.2（Cor. 8–11、Thm 9、Thm 14）。


---

## 筆記

### 1. 回顧 $\mathbb{Q}(\sqrt2,\sqrt3)$ [▶ 01:30](https://youtu.be/XzUDV4DVU0A?t=90)

（開場在分薄荷糖。「也許改變討厭你」——老師朋友的口頭禪。）

$K = \mathbb{Q}(\sqrt2,\sqrt3)$，$G = \{1,\sigma,\tau,\sigma\tau\}\cong V_4$（$\sigma$：$\sqrt2\mapsto-\sqrt2$；$\tau$：$\sqrt3\mapsto-\sqrt3$）。

| 子群 | 固定體 |
|---|---|
| $\{1\}$ | $K$ |
| $\langle\tau\rangle$ | $\mathbb{Q}(\sqrt2)$ |
| $\langle\sigma\tau\rangle$ | $\mathbb{Q}(\sqrt6)$（$\sigma\tau(\sqrt2\sqrt3) = (-\sqrt2)(-\sqrt3)$） |
| $\langle\sigma\rangle$ | $\mathbb{Q}(\sqrt3)$ |
| $G$ | $\mathbb{Q}$ |

- 所有擴張都是 2 次。子群圖通常把大群畫在上面；這裡和體塔對照時是**上下顛倒**的——最大的群對應最小的體 [▶ 07:00](https://youtu.be/XzUDV4DVU0A?t=420)。

### 2. $x^3-2$ 的分裂體 [▶ 08:00](https://youtu.be/XzUDV4DVU0A?t=480)

根：$\sqrt[3]2$、$\rho\sqrt[3]2$、$\rho^2\sqrt[3]2$，$\rho = e^{2\pi i/3} = \frac{-1+i\sqrt3}2$（暫時記號，不想一直寫 $\zeta_3$）。
- （學生故意亂喊「sigma」；有一群國中游泳隊員在看老師的影片；「sigma 是去年的梗了」。）[▶ 10:30](https://youtu.be/XzUDV4DVU0A?t=630)

**更精簡的描述** [▶ 12:00](https://youtu.be/XzUDV4DVU0A?t=720)：$\frac{\rho^2\sqrt[3]2}{\rho\sqrt[3]2} = \rho\in K$，所以 $K = \mathbb{Q}(\sqrt[3]2,\rho)$。D&F 也寫成 $\mathbb{Q}(\sqrt[3]2,\rho\sqrt[3]2)$——學生：相除得 $\rho$，就能生出第三個根。
- $[K:\mathbb{Q}] = 3\times2 = 6$。$\mathbb{Q}$-基底：$1,\sqrt[3]2,\sqrt[3]4,\rho,\rho\sqrt[3]2,\rho\sqrt[3]4$ [▶ 16:30](https://youtu.be/XzUDV4DVU0A?t=990)。

**自同構的選擇** [▶ 18:00](https://youtu.be/XzUDV4DVU0A?t=1080)
- $\sqrt[3]2$ 必須送到 $x^3-2$ 的根：3 種選擇。
- $\rho$ 必須送到 $\Phi_3 = x^2+x+1$ 的根：$\rho$ 或 $\rho^2$（$\rho^2 = -1-\rho$）。
- 一般不保證每種組合都是自同構，但這裡 6 種都是。

> **定義**（本例）：$\sigma$：$\sqrt[3]2\mapsto\rho\sqrt[3]2$、$\rho\mapsto\rho$。$\tau$：$\sqrt[3]2\mapsto\sqrt[3]2$、$\rho\mapsto\rho^2$ [▶ 22:00](https://youtu.be/XzUDV4DVU0A?t=1320)。

- 自同構由兩個生成元的去向完全決定。例：$\sigma(\rho\sqrt[3]2) = \sigma(\rho)\sigma(\sqrt[3]2) = \rho\cdot\rho\sqrt[3]2 = \rho^2\sqrt[3]2 = -\sqrt[3]2-\rho\sqrt[3]2$（要用 $\rho^2 = -1-\rho$ 換回基底——「你們掉進我的陷阱了」）[▶ 24:30](https://youtu.be/XzUDV4DVU0A?t=1470)。
- 講義寫出 $\sigma$ 對一般元素 $a+b\sqrt[3]2+\cdots+f\rho\sqrt[3]4$ 的完整公式。

**六個自同構** [▶ 30:00](https://youtu.be/XzUDV4DVU0A?t=1800)

| | $\sqrt[3]2\mapsto$ | $\rho\mapsto$ |
|---|---|---|
| $1$ | $\sqrt[3]2$ | $\rho$ |
| $\sigma$ | $\rho\sqrt[3]2$ | $\rho$ |
| $\sigma^2$ | $\rho^2\sqrt[3]2$ | $\rho$ |
| $\tau$ | $\sqrt[3]2$ | $\rho^2$ |
| $\tau\sigma$ | $\rho^2\sqrt[3]2$ | $\rho^2$ |
| $\tau\sigma^2$ | $\rho\sqrt[3]2$ | $\rho^2$ |

- （學生在老師算 $\sigma^2$ 時一直插話，「你們不讓我自己想完」。）
- $\sigma\tau$：先 $\tau$ 再 $\sigma$。$\sqrt[3]2\mapsto\sqrt[3]2\mapsto\rho\sqrt[3]2$；$\rho\mapsto\rho^2\mapsto\rho^2$。所以 **$\sigma\tau = \tau\sigma^2$** [▶ 35:00](https://youtu.be/XzUDV4DVU0A?t=2100)。
- $\sigma^3 = 1$、$\tau^2 = 1$（$\rho\mapsto\rho^2\mapsto\rho^4 = \rho$）、$\sigma\tau = \tau\sigma^{-1}$。6 階、有 2 階和 3 階元素、這樣交纏——學生：「$D_3$」；老師：「沒錯，但通常叫 **$S_3$**」（只有 $n = 3$ 時 $n! = 2n$）[▶ 37:00](https://youtu.be/XzUDV4DVU0A?t=2220)。

> 💬 學生拿 Jacob 要讀哪本群論書、Jacob 要不要交女朋友開玩笑；大家比誰的副修多 [▶ 38:30](https://youtu.be/XzUDV4DVU0A?t=2310)。

### 3. 對應關係 [▶ 40:30](https://youtu.be/XzUDV4DVU0A?t=2430)

（改用投影：「以前我零零碎碎地算總是搞混；其實細節都很簡單，除非你手滑把 $\rho\sqrt[3]4$ 寫成 $\rho^2\sqrt[3]2$。」）

- $K$ 是分裂體，Galois 的：6 次擴張、6 階群。（老師口誤說「3 次」。）
- **子群**：$\langle\sigma\rangle$（3 階，指數 2，**正規**）；$\langle\tau\rangle$、$\langle\tau\sigma\rangle$、$\langle\tau\sigma^2\rangle$（2 階，指數 3，不正規——共軛後跑到另一個 2 階子群）。
- **子體**：$\mathbb{Q}(\sqrt[3]2)$、$\mathbb{Q}(\rho\sqrt[3]2)$、$\mathbb{Q}(\rho^2\sqrt[3]2)$（都 3 次）；$\mathbb{Q}(\rho) = \mathbb{Q}(i\sqrt3)$（2 次）[▶ 42:30](https://youtu.be/XzUDV4DVU0A?t=2550)。
- 三個 3 次子體的自同構群都是平凡的，**不是 Galois**；$\mathbb{Q}(\rho)$ 的自同構群是 $\{1,\text{複數共軛}\}$，**是 Galois**。
- **固定體**：$K^{\langle\tau\rangle} = \mathbb{Q}(\sqrt[3]2)$；$K^{\langle\tau\sigma\rangle} = \mathbb{Q}(\rho\sqrt[3]2)$；$K^{\langle\tau\sigma^2\rangle} = \mathbb{Q}(\rho^2\sqrt[3]2)$；$K^{\langle\sigma\rangle} = \mathbb{Q}(\rho)$ [▶ 44:30](https://youtu.be/XzUDV4DVU0A?t=2670)。
- **唯一的正規子群 ↔ 唯一的 Galois 子體**。不是每個中間體都是 Galois 的；只有對應正規子群的才是 [▶ 46:00](https://youtu.be/XzUDV4DVU0A?t=2760)。

### 4. 證明的工具（略講）[▶ 46:30](https://youtu.be/XzUDV4DVU0A?t=2790)

「如果是一整門 Galois 理論課，這部分要花一週，再逼你們證明。我們只花三分鐘。」
- **特徵標**（character）：群到體的單位群的同態。自同構可以看成特徵標。
- **推論**：體 $K$ 到 $L$ 的相異嵌入作為函數線性獨立；特別地，相異自同構線性獨立 [▶ 47:30](https://youtu.be/XzUDV4DVU0A?t=2850)。

> **定理**（D&F Thm 9）：$G\le\mathrm{Aut}(K)$，$|G| = n$，$F = K^G$。則 $[K:K^G] = |G|$。

- 老師用 $K^G$ 記號，讓 $G$ 明顯出現（「我很笨，沒有 $G$ 我很難理清」）。證明兩頁、是「漂亮的線性代數」：一段反證 $[K:F]\le n$，另一段反證 $\ge n$，用到重新編號群元素、方程組太多或太少解。
- **推論 10**：有限擴張 $|\mathrm{Aut}(K/F)|\le[K:F]$，等號 $\iff F$ 是 $\mathrm{Aut}(K/F)$ 的固定體，即 Galois。
- **推論 11**：$\mathrm{Gal}(K/K^G) = G$；相異子群給出相異固定體 [▶ 50:00](https://youtu.be/XzUDV4DVU0A?t=3000)。

> **定義**：$K/F$ Galois，$\sigma\in\mathrm{Gal}(K/F)$。$\sigma\alpha$ 叫 $\alpha$ 的（**Galois**）**共軛**；$\sigma(E)$ 叫子體 $E$ 的**共軛體** [▶ 51:00](https://youtu.be/XzUDV4DVU0A?t=3060)。

- 支線任務（2 分）：把 $\dfrac1{2+\sqrt[3]7}$ 的分母**有理化**。「AI 之前做這個要花一分鐘。」（學生：「作業讓我難過。」——「你剛踢了一隻小狗。」）[▶ 52:00](https://youtu.be/XzUDV4DVU0A?t=3120)

### 5. Galois 理論基本定理 [▶ 53:30](https://youtu.be/XzUDV4DVU0A?t=3210)

> **定理**（D&F Thm 14）：$K/F$ 是 Galois 擴張，$G = \mathrm{Gal}(K/F)$。
> 1. 中間體 $E$（$F\subseteq E\subseteq K$）與子群 $H\le G$ 一一對應：$E\mapsto\mathrm{Gal}(K/E)$（固定 $E$ 的元素），$H\mapsto K^H$（被 $H$ 固定的體）。兩者互逆，且**包含關係反轉**。
> 2. $[K:E] = |H|$，$[E:F] = [G:H]$。
> 3. $K/E$ 永遠是 Galois 的，$\mathrm{Gal}(K/E) = H$。
> 4. $E/F$ 是 Galois 的 $\iff H\lhd G$；此時 $\mathrm{Gal}(E/F)\cong G/H$。
> 5. 交集 $E_1\cap E_2$ 對應 $\langle H_1,H_2\rangle$；合成體 $E_1E_2$ 對應 $H_1\cap H_2$。子體格和子群格**互為對偶**（上下顛倒）。

- 講義上 (5) 旁有一塊老師忘了擦的地方（「沒時間了，Jacob」）。
- **下一步**：這套理論怎麼證明五次方程一般不能用根式解——回到它原本被發明的目的 [▶ 56:30](https://youtu.be/XzUDV4DVU0A?t=3390)。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 特徵標 | character | §4 |
| 嵌入 | embedding | §4 |
| Galois 共軛 | Galois conjugate | §4 |
| 共軛體 | conjugate field | §4 |
| 有理化分母 | rationalize the denominator | §4 |
| Galois 理論基本定理 | Fundamental Theorem of Galois Theory | §5 |

## ⚠️ 待確認清單

（本集無）
