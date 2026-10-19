---
course: Abstract Algebra II (Spring 2026)
episode: 27
lecture: L23
date: 2026-03-23
video: https://www.youtube.com/watch?v=4CV8yVzqWxk
notes: 講義/AA2/Math422_Lecture23_FurtherExamplesGalois.pdf
---

# 第 27 集 · L23：Galois 理論例子、分圓體、共軛技巧 [▶ 影片](https://www.youtube.com/watch?v=4CV8yVzqWxk&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[26-L23-Galois理論例子-下]] ｜ [總目錄](../README.md) ｜ 下一集：[[28-L24-多項式的Galois群]] →

## 本集概要

春假後第一堂（D&F §14.2 例子、§14.5 分圓擴張）：
- 用 Galois 對應重新證明 $\mathbb{Q}(\sqrt2+\sqrt3) = \mathbb{Q}(\sqrt2,\sqrt3)$；$V_4$ 的三個子群都正規 ↔ 三個中間體都是 Galois 的；對比 $x^3-2$（$S_3$）。
- $x^8-2$ 的分裂體：$\mathbb{Q}(\sqrt[8]2,i)$，次數 16，Galois 群是**擬二面體群**。
- **$\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})\cong(\mathbb{Z}/n\mathbb{Z})^\times$**（證明）。
- $\mathbb{Q}(\zeta_5)$：Galois 群 $\cong\mathbb{Z}_4$，由 $\sigma_2$ 生成；唯一的二次子體 $\mathbb{Q}(\zeta_5+\zeta_5^{-1}) = \mathbb{Q}(\sqrt5)$。
- 有理化分母：共軛相乘；或用 Bézout（歐幾里得演算法）。結尾在第 26 集。

> 📘 講義對應：Math422 Lecture 23「Further Examples of Galois Theory」；D&F §14.2（$x^8-2$ 的例子）、§14.5（分圓擴張）。

---

## 筆記

### 1. 再看 $\mathbb{Q}(\sqrt2,\sqrt3)$ [▶ 00:30](https://youtu.be/4CV8yVzqWxk?t=30)

（開場：「Chat，這是老鼠嗎？」）
- 它是 $(x^2-2)(x^2-3)$ 的分裂體 ⇒ Galois；自同構自動固定 $\mathbb{Q}$（$1\mapsto1$、$2\mapsto2$、$\frac13\mapsto\frac13$……），由 $\sqrt2,\sqrt3$ 的去向決定。四個自同構、子群和固定體如上次 [▶ 02:00](https://youtu.be/4CV8yVzqWxk?t=120)。

**用 Galois 對應證 $\mathbb{Q}(\sqrt2+\sqrt3) = K$** [▶ 03:30](https://youtu.be/4CV8yVzqWxk?t=210)：$\mathbb{Q}(\sqrt2+\sqrt3)$ 是哪個子群的固定體？$\sqrt2+\sqrt3$ 被三個非恆等元分別送到 $\pm\sqrt2\mp\sqrt3$、$-\sqrt2-\sqrt3$，都不固定。只有恆等元固定它，所以它是 $\{1\}$ 的固定體，也就是 $K$ 本身。「和上次的論證本質不同，我很喜歡。」

**正規 ↔ Galois** [▶ 05:30](https://youtu.be/4CV8yVzqWxk?t=330)
- $V_4$ 的三個 2 階子群指數 2，都正規 ⇒ 三個中間體 $\mathbb{Q}(\sqrt2),\mathbb{Q}(\sqrt3),\mathbb{Q}(\sqrt6)$ 都是 Galois 的——確實，它們是 $x^2-2$、$x^2-3$、$x^2-6$ 的分裂體。
- 對比 $x^3-2$（$\mathrm{Gal}\cong S_3$）：只有 $\langle\sigma\rangle$ 正規，對應 $\mathbb{Q}(\rho)$（2 次）；三個 3 次子體不是分裂體，自同構群只有恆等元。2 階子群互相**共軛**（Galois 共軛）[▶ 07:00](https://youtu.be/4CV8yVzqWxk?t=420)。
- 老師試著算 $\sigma^{-1}\tau\sigma$，用關係 $\sigma^3 = \tau^2 = 1$、$\tau\sigma = \sigma^{-1}\tau$，算了一陣子（「今天我沒辦法思考，先警告你們」），結論：$\langle\tau\rangle$ 的共軛是另一個 2 階子群，不正規 [▶ 11:00](https://youtu.be/4CV8yVzqWxk?t=660)。

### 2. $x^8-2$ 的分裂體 [▶ 13:30](https://youtu.be/4CV8yVzqWxk?t=810)

D&F 花三頁講這個例子，老師只討論、不寫細節。
- 根：$\theta\zeta_8^k$（$k = 0,\dots,7$），$\theta = \sqrt[8]2$（正實數）。分裂體 $\mathbb{Q}(\theta,\zeta_8)$。
- **更好的描述**：$\mathbb{Q}(\zeta_8) = \mathbb{Q}(i,\sqrt2)$（因為 $\sqrt2\,\zeta_8 = 1+i$）；而 $\theta^4 = \sqrt2$ 已在 $\mathbb{Q}(\theta)$ 裡。所以分裂體 $= \mathbb{Q}(\sqrt[8]2,i)$ [▶ 15:30](https://youtu.be/4CV8yVzqWxk?t=930)。
- **次數 16**：$x^8-2$ 由 Eisenstein（$p = 2$）不可約，$\mathbb{Q}(\theta)$ 是 8 次實的體，$i$ 不在裡面，再加 $i$ 是 2 次。
- 天真地看 $\mathbb{Q}(\theta,\zeta_8)$：$8\times\varphi(8) = 8\times4 = 32$？不是——兩者糾纏在一起，只有 16。換一組生成元讓這件事變明顯，「很聰明」[▶ 19:30](https://youtu.be/4CV8yVzqWxk?t=1170)。
- 自同構：$\theta$ 送到 8 個根之一、$i$ 送到 $\pm i$，共 16 種可能。又知道群有 16 個元素（Galois），所以 **16 種全都是自同構**，不必逐一驗證——「很狡猾」[▶ 20:30](https://youtu.be/4CV8yVzqWxk?t=1230)。
- $\sigma$ 移動 $\theta$、$\tau$ 移動 $i$，Galois 群
$$\langle\sigma,\tau\mid\sigma^8 = \tau^2 = 1,\ \sigma\tau = \tau\sigma^3\rangle.$$
  不是二面體群（那會是 $\tau\sigma^7 = \tau\sigma^{-1}$），是**擬二面體群**（quasidihedral group）[▶ 21:30](https://youtu.be/4CV8yVzqWxk?t=1290)。
- 它有三個互不同構的 8 階子群：$D_8$（正方形的對稱，D&F 用群的階編號）、$\mathbb{Z}_8$、四元數群 $Q_8$。固定體有實二次體、Gauss 型的、虛二次體……「體的圖我不畫，會畫一整天。」

### 3. 分圓擴張的 Galois 群 [▶ 23:30](https://youtu.be/4CV8yVzqWxk?t=1410)

$[\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n)$，它是 $\Phi_n$ 的分裂體，Galois。
- 自同構必須把 $\zeta_n$ 送到**本原** $n$ 次單位根：$\zeta_n\mapsto\zeta_n^a$，$\gcd(a,n) = 1$。例 $n = 4$：$i$ 可以送到 $i$ 或 $i^3 = -i$，不能送到 $i^2 = -1$ 或 1（生成元要送到生成元）[▶ 24:30](https://youtu.be/4CV8yVzqWxk?t=1470)。
- 共 $\varphi(n)$ 種選擇，正好是 Galois 群的大小。

> **定理**：$\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})\cong(\mathbb{Z}/n\mathbb{Z})^\times$，同構 $a\mapsto\sigma_a$，$\sigma_a(\zeta_n) = \zeta_n^a$。

**證明**（講義上的寫得不好，老師現場重做；「我今天腦袋不行」）[▶ 28:00](https://youtu.be/4CV8yVzqWxk?t=1680)
- 兩邊都是 $\varphi(n)$ 個元素的有限集合，只要證同態 + 單射。
- 同態：$\sigma_a\sigma_b(\zeta_n) = \sigma_a(\zeta_n^b) = (\sigma_a\zeta_n)^b = \zeta_n^{ab} = \sigma_{ab}(\zeta_n)$。自同構由 $\zeta_n$ 的像決定，所以 $\sigma_a\sigma_b = \sigma_{ab}$ [▶ 31:30](https://youtu.be/4CV8yVzqWxk?t=1890)。（「我就知道 sigh-homo 會引來笑聲。」）
- 核：$\sigma_a = \sigma_1$ ⇒ $\zeta_n^a = \zeta_n$ ⇒ $a = 1$。單射 ⇒ 同構 [▶ 34:00](https://youtu.be/4CV8yVzqWxk?t=2040)。（老師的 $\zeta$ 越寫越歪，「要請 Spano 博士用拓撲描述」。）
- 「課程計畫裡好像沒排這節，但它很簡單，應該講。」

### 4. 例：$\mathbb{Q}(\zeta_5)$ [▶ 36:00](https://youtu.be/4CV8yVzqWxk?t=2160)

- 次數 $\varphi(5) = 4$。$1+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4 = 0$：五個根在單位圓上對稱分布，平均是 0——對所有 $n\ge2$ 都成立（$n = 2$：$1,-1$；$n = 4$：$1,i,-1,-i$）[▶ 37:30](https://youtu.be/4CV8yVzqWxk?t=2250)。
- $G = \{1,\sigma_2,\sigma_3,\sigma_4\}\cong(\mathbb{Z}/5)^\times\cong\mathbb{Z}_4$。
- **$\sigma_2$ 是生成元** [▶ 40:00](https://youtu.be/4CV8yVzqWxk?t=2400)：$\zeta_5\mapsto\zeta_5^2\mapsto\zeta_5^4\mapsto\zeta_5^8 = \zeta_5^3\mapsto\zeta_5^6 = \zeta_5$。所以 $\sigma_2^2 = \sigma_4$、$\sigma_2^3 = \sigma_3$、$\sigma_2^4 = 1$。另一個生成元是 $\sigma_3$；$\sigma_4$ 像 $\mathbb{Z}_4$ 中的 2。（老師中途一度說成 $\sigma_4$。）
- **子群與固定體** [▶ 44:30](https://youtu.be/4CV8yVzqWxk?t=2670)：$\mathbb{Z}_4$ 只有一個非平凡真子群 $\langle\sigma_4\rangle$（2 階）。所以和 $V_4$（三個二次子體）不同，這個 4 次擴張**只有一個**二次子體：$\mathbb{Q}(\sqrt5)$。
- $\sigma_4$（複數共軛）固定 $\zeta_5+\zeta_5^{-1} = \zeta_5+\zeta_5^4$。為什麼這等於加入 $\sqrt5$？老師一時說不出來，留作謎題 [▶ 47:30](https://youtu.be/4CV8yVzqWxk?t=2850)。
- 「好玩的是：這裡 Galois 群幾乎免費，固定體反而難找——和之前的例子在難度上是對偶的。」

> 💬 補充（非課堂內容）：$\zeta_5+\zeta_5^{-1} = 2\cos\frac{2\pi}5 = \frac{-1+\sqrt5}2$，它滿足 $x^2+x-1 = 0$，所以 $\mathbb{Q}(\zeta_5+\zeta_5^{-1}) = \mathbb{Q}(\sqrt5)$。

### 5. 有理化分母 [▶ 48:30](https://youtu.be/4CV8yVzqWxk?t=2910)

回到上次的支線任務：怎麼有理化 $\dfrac1{2+\sqrt[3]7}$？（學生：「負 4 分鐘。」——「不，我才講到 49 分鐘。」）

- 複數：$(2+3i)(2-3i) = 13$，所以 $\frac1{2+3i} = \frac{2-3i}{13}$。
- 平方根：$(2+\sqrt3)(2-\sqrt3) = 4-3 = 1$，所以 $\frac1{2+\sqrt3} = 2-\sqrt3$。（老師先算成 $-1$，學生提醒「$2\times2 = 4$」。）[▶ 50:30](https://youtu.be/4CV8yVzqWxk?t=3030)
- **立方根**：$x^3-2 = (x-\sqrt[3]2)(x-\rho\sqrt[3]2)(x-\rho^2\sqrt[3]2)$，代 $x = 3$：
$$25 = (3-\sqrt[3]2)(3-\rho\sqrt[3]2)(3-\rho^2\sqrt[3]2),\quad\frac1{3-\sqrt[3]2} = \frac{(3-\rho\sqrt[3]2)(3-\rho^2\sqrt[3]2)}{25}.$$
  所有 **Galois 共軛**相乘落在基礎體——推廣了複數共軛 [▶ 52:00](https://youtu.be/4CV8yVzqWxk?t=3120)。
- **另一法（與 Galois 無關但很穩）**：$\mathbb{Q}(\sqrt[3]7)\cong\mathbb{Q}[x]/(x^3-7)$，$\alpha = x+(x^3-7)$。$\gcd(x+2,x^3-7) = 1$，由 Bézout 有 $a(x)(x+2)+b(x)(x^3-7) = 1$；在商環中第二項是 0，所以 $(\alpha+2)^{-1} = a(\alpha)$ [▶ 56:30](https://youtu.be/4CV8yVzqWxk?t=3390)。
- （老師的「小弟弟」Bill——學生以為 Bill 是哥哥。）
- 最後開始講 D&F 的例子：求 $2+3\sqrt[3]2+\sqrt[3]4$ 的反元素（Maple 計算），結尾在第 26 集。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 擬二面體群 | quasidihedral group | §2 |
| 分圓擴張 | cyclotomic extension | §3 |
| 有理化分母 | rationalizing the denominator | §5 |

## ⚠️ 待確認清單

（本集無）
