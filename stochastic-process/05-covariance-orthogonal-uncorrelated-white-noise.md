---
course: 隨機過程（陽明交大電機系，2017 秋）
episode: 5
lecture: Lec 9-1 General Concepts — Definitions (4/7)
date: 待補
video: https://youtu.be/nq5n-7yJ-kM
notes: Papoulis & Pillai 4th ed. §9-1 General Properties（式 (9-32)–(9-43)，pp. 383–386）
---

# 第 5 集 · Lec 9-1 (4/7)：平均功率、協方差、獨立／正交／不相關、a-dependent、白雜訊的三種定義 [▶ 影片](https://youtu.be/nq5n-7yJ-kM)

← 上一集：[04](04-random-process-definition-fdd-density-autocorrelation.md) ｜ [總目錄](README.md) ｜ 下一集：[06](06-independent-increment-normal-riemann-lebesgue-poisson.md) →

> **課程**：隨機過程（Random Processes），陽明交大電機系，NYCU OCW 2017 — 第 5 集
> **講者**：陳伯寧老師
> **來源**：YouTube 錄影逐字稿（47:03，whisper large-v3-turbo）＋ Papoulis §9-1（pp. 383–386）
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚，列在最後的清單

> ⚠️ 逐字稿缺字（整集通用）：「correlation」→「collation／coration」，「uncorrelated」→「unquality／uncollated／uncoalleted」，「orthogonality」→「Othogonality」，「正交」→「證交」，「傅立葉轉換」→「負列轉換／复列转换／負率的轉換／复理的转换」，「wide-sense stationary」→「Wisen stationary」，「Papoulis」→「Propolis／Perpolis／PoPoly」，「Proakis」→「Prokes／Prokeys／Progic」，「Gray & Davisson」→「M. Gray 跟 Lee Davidson」，「strictly／weakly white」→「stricky／weekly white」，「Pólya contagion」→「polyarcontagion」，「伏」→「幅」，「complex conjugate」→「Compress Conjugate」，「相乘」→「相成」，「乘數」＝「陳述」，「self-similarity」→「Self-Seminarity」。以下一律用正確的字。

> **接上一集**：上一集定義了平均 $\eta(t)$ 和自相關 $R(t_1,t_2)$。這一集從工程角度把一階、二階的量補齊，再給隨機過程加上各種「限制」：獨立、正交、不相關、a-dependent、白。重點是老師比較三本書對「白雜訊」的定義，練習**嚴謹地讀定義**。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 一階、二階的量都是能量](#1-一階二階的量都是能量)
- [2. 平均功率、自協方差、相關係數](#2-平均功率自協方差相關係數)
- [3. 互相關、互協方差](#3-互相關互協方差)
- [4. 加上限制：獨立](#4-加上限制獨立)
- [5. 正交 vs 不相關](#5-正交-vs-不相關)
- [6. a-dependent](#6-a-dependent)
- [7. 白過程：strictly white vs weakly white](#7-白過程strictly-white-vs-weakly-white)
  - [7.1 Papoulis 的定義允許什麼](#71-papoulis-的定義允許什麼)
  - [7.2 Proakis 的定義](#72-proakis-的定義)
  - [7.3 Gray & Davisson 的定義](#73-gray--davisson-的定義)
  - [7.4 三本書比較](#74-三本書比較)
- [8. 插曲：平穩與非平穩（Pólya 罐子）](#8-插曲平穩與非平穩pólya-罐子)
- [9. 功率頻譜看不出 strictly 還是 weakly](#9-功率頻譜看不出-strictly-還是-weakly)
- [10. 一頁速查表](#10-一頁速查表)
- [11. 與後續集數的連結](#11-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 影片 | 課本 |
|---|---|---|
| 平均功率、自協方差、相關係數 | [▶ 00:00](https://youtu.be/nq5n-7yJ-kM?t=0) | 式 (9-32)、(9-34)、(9-35)，pp. 383–384 |
| 互相關、互協方差 | [▶ 07:07](https://youtu.be/nq5n-7yJ-kM?t=427) | 式 (9-38)、(9-39)，pp. 384–385 |
| 獨立、正交、不相關、a-dependent | [▶ 09:13](https://youtu.be/nq5n-7yJ-kM?t=553) | 式 (9-40)–(9-42)，pp. 385–386 |
| 白雜訊 | [▶ 20:34](https://youtu.be/nq5n-7yJ-kM?t=1234) | 式 (9-43)，p. 385 |

---

## 1. 一階、二階的量都是能量

[▶ 00:31](https://youtu.be/nq5n-7yJ-kM?t=31)【口頭】

- 幾乎所有未知的東西，工程上都定義成隨機過程。大部分應用只看**一階、二階**；少數看**三階**，因為要看**相位**——二階常常看不到相位（後面會稍微講）。
- **二階**的量，單位上視為**能量**。
- **一階也是能量，不能忽略**：一階是 **DC**（直流）的部分。要維持一個 5 V 的固定準位，也要給能量。一階要平方才變成能量。
- 工程上看的都是能量／功率：傳這個訊號要花多少瓦特。

---

## 2. 平均功率、自協方差、相關係數

[▶ 01:32](https://youtu.be/nq5n-7yJ-kM?t=92)

> **平均功率** (average power)：
> $$E\left[X(t)X^*(t)\right]=E\left[|X(t)|^2\right]=R_{XX}(t,t)\ge 0.$$

- 單位時間要花多少能量。工程上把它視為這個隨機過程的能量，單位也剛好對得上。
- 能量一定 $\ge 0$：公式是絕對值平方再取期望值，自然非負。不同時間可以有不同的期望能量。

> **自協方差** (autocovariance)：扣掉期望值之後的相關
> $$C_{XX}(t_1,t_2)=E\left[\left(X(t_1)-\eta_X(t_1)\right)\left(X(t_2)-\eta_X(t_2)\right)^*\right]=R_{XX}(t_1,t_2)-\eta_X(t_1)\eta_X^*(t_2).$$
> **變異數** (variance)：單一時間 $C_{XX}(t,t)$。

- **auto** = self，自己跟自己。**variance** 是扣掉期望值之後、左右變異的程度。
- 直觀【口頭】：能量影響的**偏差**有多大。
- 第二個等號：展開 $E\left[X_1X_2^*-X_1\eta_2^*-\eta_1X_2^*+\eta_1\eta_2^*\right]=R-\eta_1\eta_2^*-\eta_1\eta_2^*+\eta_1\eta_2^*=R-\eta_1\eta_2^*$（$X_i=X(t_i)$，$\eta_i=\eta_X(t_i)$）。
- 老師說最好背，但做久了會變直觀。

**記號**：這門課下標寫清楚，自己跟自己寫 $XX$，$X$ 跟 $Y$ 寫 $XY$。

> **相關係數** (correlation coefficient)：
> $$r(t_1,t_2)=\frac{C(t_1,t_2)}{\sqrt{C(t_1,t_1)\,C(t_2,t_2)}}.$$

為什麼要正規化 (normalize)？只看相關性的**程度**【口頭】：

- 算出相關 20 W，但基礎能量是 30 W → 相關程度 $20/30\approx 67\%$。（老師口頭說「60%」；$20/30$ 實際約 67%。）
- 算出相關只有 1 W，但基礎能量只有 1.1 W → 相關程度很高。
- 老師提到這學期最熱門的課是 deep learning，learning 很多參數，彼此之間也要算 correlation，是類似的基礎。

【課本補充】式 (9-34)、(9-35)，p. 384。課本也說 $|r(t_1,t_2)|\le 1$、$r(t,t)=1$（式 (9-36)），而且 $C$ 是**中心化過程** $\tilde{X}(t)=X(t)-\eta(t)$ 的自相關，所以 $C$ 也是 p.d.。

**重要事實**（老師說可以證明，但不提供證明）：

> 所有自相關函數、所有自協方差函數，**一定是非負定的**，而且是 **if and only if**。

老師寫「PD 或 NND」，因為 Papoulis 的 PD 就是他認定的 NND（上一集第 11 節）。

老師的提醒【口頭】：不要只查一本書，每本書作者看法不一樣、見仁見智；定義是人給的，兩三百年前的書可能有別的定義，只是後來發現不好推廣，就慢慢消失了。

---

## 3. 互相關、互協方差

[▶ 07:07](https://youtu.be/nq5n-7yJ-kM?t=427)

> **互相關** (cross-correlation)：$R_{XY}(t_1,t_2)=E\left[X(t_1)Y^*(t_2)\right]$
> **互協方差** (cross-covariance)：$C_{XY}(t_1,t_2)=R_{XY}(t_1,t_2)-\eta_X(t_1)\eta_Y^*(t_2)$

- 定義裡沒寫機率空間，但心裡要知道：要討論 $X$ 和 $Y$ 的關係，**兩個一定要定義在同一個機率空間上**。
- 通訊角度：兩個訊號能量的相互影響。最關心的是**輸入 $X$ 和系統輸出 $Y$**：能量有沒有不見、影響強不強。
- 互協方差：扣掉期望值，只看變異的差距。

老師舉例【口頭】：他在台大參加一個口試，學生做各種 learning，有很多參數，不知道彼此關係，就做大量量測（big data），然後算任兩個參數的 correlation，發現完全沒想到的強相關，再事後找解釋。

【課本補充】式 (9-38)、(9-39)，pp. 384–385；$R_{XY}(t_1,t_2)=R_{YX}^*(t_2,t_1)$。

---

## 4. 加上限制：獨立

[▶ 09:13](https://youtu.be/nq5n-7yJ-kM?t=553) 前面的定義都沒給隨機過程任何限制。現在開始加限制。

- 限制常常是為了**做研究方便**。你觀察到的過程不一定真的符合，但做研究時會假設它符合。
- 最常用的是**獨立**：假設雜訊是獨立過程，分析、模擬都方便。（然後你會發現雜訊其實不獨立。）

> **獨立** (independent)：任取**有限個**取樣時間，這些樣本互相獨立，也就是聯合分布 = 個別分布的乘積。例：在時間 1、3、5、7 取四個樣本，
> $$F(x_1,x_3,x_5,x_7;1,3,5,7)=F(x_1;1)F(x_3;3)F(x_5;5)F(x_7;7).$$

- 時間是連續的，所以一定要講「取樣」(sample)，而且只講**有限維**。無限的不符合這個定義，你也不知道。工程上夠用。
- **綠框 comment**：有限維聯合分布**不能完全決定**隨機過程的所有性質，要回到原始的機率空間。所以這個獨立的定義是**從應用角度**給的。
- 配合上一集的例子：只告訴你「獨立」，對「時間 0 到 1 之間發生過的最小值」**完全沒有任何資訊**。
- 你假設獨立時要的就是：任何有限個樣本，機率相乘。

【課本補充】Papoulis p. 386「Independent processes」講的是**兩個**過程：若 $X(t_1),\dots,X(t_n)$ 和 $Y(t_1'),\dots,Y(t_n')$ 互相獨立，則 $X(t)$、$Y(t)$ 稱為獨立過程。

⚠️ 待確認：逐字稿開頭說「兩個 random process 被稱為 independent」，但舉的例子是在 1、3、5、7 取**同一個**過程的四個樣本互相獨立。投影片上的定義是哪一種，逐字稿無法確定；上面照例子寫。

老師說【口頭】：他認為工程科系的三門數學課是 **Random Process**、**Detection & Estimation**（Neyman–Pearson、Lehmann 那些全部是數學）、**Information Theory**。重點是觀念，不是數學本身。

---

## 5. 正交 vs 不相關

[▶ 13:54](https://youtu.be/nq5n-7yJ-kM?t=834)

> **正交** (orthogonal)：$R_{XY}(t_1,t_2)=0$，對所有 $t_1,t_2$。
> **不相關** (uncorrelated)：$C_{XY}(t_1,t_2)=0$，對所有 $t_1,t_2$。

**正交的直觀**【口頭】：4G 行動通訊就是「正交通訊」。兩個訊號彼此**能量不會互相影響**：我傳送不影響你的能量，你送 1 W 收到也是 1 W。

- 正交用的是**相關函數** $R$，它同時包含一階和二階，**包含 DC**。DC 本身是能量：我對你的 DC 能量有影響，還是在影響你。
- 如果將來某個應用的「能量」不是二次而是三次（例如腦波），定義就可能要更高階。完全是應用導向的。

⚠️ 逐字稿缺字：[▶ 14:56](https://youtu.be/nq5n-7yJ-kM?t=896) 字幕說「Auto-Correlation Function S 跟 Y 之間是 0」，應是 $X$ 跟 $Y$ 的**互相關** $R_{XY}=0$（課本式 (9-40)）。

**不相關的直觀**【口頭】：比較像數學上的定義。

- 它**扣掉了一階**（DC）。維持一個 5 V 的固定準位，永遠是 5 V、沒有變化；沒有變化就不會影響你。
- 所以不相關看的是**變化的影響**：你怎麼動，我這邊都沒有變化，就說我們沒關係。
- 跟正交的概念不一樣。依需求決定要用哪一個。

【課本補充】式 (9-40)、(9-41)，p. 385。兩者關係（由 $C_{XY}=R_{XY}-\eta_X\eta_Y^*$ 直接得到）：若其中一個過程平均為 0，正交 ⇔ 不相關。

---

## 6. a-dependent

[▶ 16:58](https://youtu.be/nq5n-7yJ-kM?t=1018) 這個名詞比較少用，但有時做研究會額外加這個條件。

情境：觀察到的雜訊或訊號是有關係的，但關係很難細緻描述，造成研究困擾。乾脆規定：**關係只維持一段長度 $a$**。

> **a-dependent**：若 $t<t_0$ 的所有 $X(t)$ 和 $t>t_0+a$ 的所有 $X(t)$ 互相**獨立**（獨立的意思回到第 4 節：有限維樣本獨立），則 $X(t)$ 稱為 a-dependent。

- 例：$a$ = 兩小時，間隔超過兩小時就沒關係。用這種二分法簡化系統，分析比較容易。

> **correlation a-dependent**：自相關（協方差）在 $|t_1-t_2|>a$ 時為 0，也就是間隔超過 $a$ 就**不相關**。

【課本補充】Papoulis p. 385：a-dependent 推出 $C(t_1,t_2)=0$，$|t_1-t_2|>a$（式 (9-42)）；滿足 (9-42) 的叫 correlation a-dependent。

老師談定義的重要【口頭】：

- 好幾個著名研究者都說：**定義定對了，後面的證明就容易**。
- 例：有一篇 IEEE Transactions on Information Theory 的論文，把歷史上出現過的 **self-similarity**（自相似）定義全部拿出來比較：誰是誰的子集、哪個好哪個不好。這也是貢獻。
- 定義可以改，但要告訴別人改完為什麼比較好。這是科學會進步的原因。

---

## 7. 白過程：strictly white vs weakly white

[▶ 20:34](https://youtu.be/nq5n-7yJ-kM?t=1234) 通訊上常見 white process（白過程），通常講的是雜訊。

> **Papoulis 的定義**：
> - **白** (white)：$X(t_1)$ 和 $X(t_2)$ **不相關**，對每一對 $t_1\ne t_2$。
> - **嚴格白** (strictly white)：$X(t_1)$ 和 $X(t_2)$ **獨立**，對每一對 $t_1\ne t_2$。

- 過去數位通訊教的白，其實是 **weakly white**（弱白）：只看二階，「能量上我跟你不互相影響」。例如 10 點和 10 點 10 分的樣本不相關。
- **strictly white** 很強：不只二階，三階、四階……兩兩之間都獨立。
- 為什麼需要 strictly white？有時只用二階很難證明，必須用到機率性質，就假設雜訊是 strictly white，比較好做。
- 兩個定義的敘述**只差一個字**：uncorrelated vs independent。這種寫法容易推廣（像隨機過程是 indexed family 一樣）。

### 7.1 Papoulis 的定義允許什麼

[▶ 22:39](https://youtu.be/nq5n-7yJ-kM?t=1359) 老師問：如果你寫論文要給 white 一個定義，你會怎麼寫？

看這個定義：「$t_1\ne t_2$ 時不相關」。那 **$t_1=t_2$ 呢？不知道，沒定義。** 它不關心。這隱含了兩件事：

1. **允許 DC**：用的是「不相關」（扣掉平均），所以平均不一定是 0。
2. **允許時變** (time-varying)：寫成 $t$ 和 $t+\tau$，只要 $\tau\ne 0$ 協方差就是 0，可以用 Dirac delta $\delta(\tau)$ 表示。但 $\tau=0$ 的值（同一時間對同一時間）可以**隨 $t$ 不同**：
$$C(t,t+\tau)=q(t)\,\delta(\tau).$$
   也就是雖然白，能量還是會隨時間動。這叫 **time-varying white process**。

有沒有用？有。之後會看到：把一個**廣義平穩** (wide-sense stationary) 的雜訊做**傅立葉轉換**，得到的就是這種過程。所以 Papoulis 這樣定義是為了配合後面的章節，前後一致。有些作者不小心，前一章的定義到下一章就出現漏洞。

【課本補充】Papoulis p. 385 寫的是 $C(t_i,t_j)=0$，$t_i\ne t_j$；並說非平凡的白雜訊，自協方差一定是
$$C(t_1,t_2)=q(t_1)\,\delta(t_1-t_2),\qquad q(t)\ge 0\qquad\text{(9-43)}.$$
另外課本也寫：**除非另外說明，白雜訊的平均假設為 0**。

【課本補充】Example 9-9（p. 385）：$X(t)=\int_0^t\nu(\alpha)\,d\alpha$，$\nu$ 是白雜訊。由 (9-43)，
$$E[X^2(t)]=\int_0^t\!\!\int_0^t q(t_1)\delta(t_1-t_2)\,dt_2\,dt_1=\int_0^t q(t_1)\,dt_1,$$
關鍵一步是 $\int_0^t\delta(t_1-t_2)\,dt_2=1$（$0<t_1<t$）。

### 7.2 Proakis 的定義

[▶ 27:16](https://youtu.be/nq5n-7yJ-kM?t=1636) Proakis《Digital Communications》（數位通訊賣得最好的課本）：

- p. 77：自相關定義為
$$R(\tau)=\frac{N_0}{2}\,\delta(\tau),$$
  這樣的過程稱為 white noise。直接從自相關定義。
- p. 157：white noise 是一個有 **flat**（平坦）功率頻譜密度的隨機過程。配合 p. 77，自相關的傅立葉轉換就是常數 $\frac{N_0}{2}$。
- 書中的功率頻譜密度定義為**自相關函數的傅立葉轉換**。

這個定義**不允許時變**：$R$ 只是 $\tau$ 的函數，所以不可能有 time-varying white process。對 Proakis 的書夠用（它不討論時變白雜訊），但對 Papoulis 的書可能不夠。

**它允許 DC 嗎？不允許。** [▶ 30:23](https://youtu.be/nq5n-7yJ-kM?t=1823)

1. 若有 DC，自相關會多一個常數：$R(\tau)=C+E\,\delta(\tau)$。
2. 常數的傅立葉轉換是脈衝：$\mathcal{F}\{C\}=C\,\delta(f)$。
3. 所以頻譜 $=C\,\delta(f)+E$：大部分頻率是 $E$，但在 $f=0$ 衝出一根，值是無限大。
4. 這不是「對所有頻率都是常數」，違反 **flat**。

所以「flat」這個字已經**排除了 white noise 有 DC**。老師說【口頭】：寫論文時用字要這麼嚴謹。

**Proakis 隱含平穩** [▶ 34:02](https://youtu.be/nq5n-7yJ-kM?t=2042)：$R$ 只依賴 $\tau$，等於預設白過程是**平穩的** (stationary)。Papoulis 的定義**完全沒說**要平穩。所以 Proakis 的定義局限比較大，但工程上大部分過程都假設平穩，也還好。

### 7.3 Gray & Davisson 的定義

[▶ 39:39](https://youtu.be/nq5n-7yJ-kM?t=2379) 1986 年 R. M. Gray 和 L. D. Davisson 的《Random Processes》，二三十年前美國常用的課本，嚴謹、不厚（老師喜歡不厚的書，容易看完、精簡）。

- 定義：隨機過程稱為 white，如果它的**功率頻譜密度對所有 $f$ 是常數**。直觀：白光就是所有頻率分量一樣。
- 特別的是 p. 193：它把功率頻譜密度定義為**自協方差**的傅立葉轉換（後來的書都定義成**自相關**的傅立葉轉換）。兩者差在 DC（平均、一階）。所以這等於**排除了 DC**。

老師的吹毛求疵【口頭】：對非零平均的平穩過程，這樣定義的功率頻譜**不是**它真正的功率，因為 DC 有能量（維持 5 V 要給能量，不然準位會掉下來）。他認為功率要一階、二階都看才合理。

作者在 p. 197 補了一句：*A white process is almost always assumed to have zero mean.* 零平均時，自協方差 = 自相關，兩種定義就一樣了。所以前後文看清楚，作者還是有一致性。

⚠️ 待確認：[▶ 40:09](https://youtu.be/nq5n-7yJ-kM?t=2409) 老師提到 Davisson 證出某個著名定理，逐字稿聽成「Best Competition Theorem」，聽不出是哪個定理。

### 7.4 三本書比較

[▶ 43:44](https://youtu.be/nq5n-7yJ-kM?t=2624)

| | Papoulis | Proakis（p. 77、157） | Gray & Davisson（p. 193、197） |
|---|---|---|---|
| 定義 | $t_1\ne t_2$ 時**不相關** | $R(\tau)=\frac{N_0}{2}\delta(\tau)$；PSD flat | PSD 對所有 $f$ 是常數 |
| PSD 是誰的傅立葉轉換 | （之後講） | 自相關 | **自協方差** |
| 允許 DC？ | 可以（原點可有 DC 脈衝） | 不行（flat 排除） | 定義上排除；另說幾乎都假設零平均 |
| 允許時變？ | 可以，$q(t)\delta(\tau)$ | 不行 | — |
| 要求平穩？ | 沒有 | 隱含要求 | — |
| 類型 | **間接定義**（和「白」字面無關） | 直接定義 | 直接定義 |

- 老師說 Papoulis 是數學系的老師，從數學角度看；Proakis、Davisson 是工程的，發表很多工程應用論文，所以角度不同。【口頭】
- **間接定義** (indirect definition)：「白」字面上是白光——紅橙黃綠藍靛紫每個分量一樣，所以直接的定義應該是「所有頻率分量一樣」。Papoulis 的定義（不相關）跟「白」這個字**沒有直接關係**，所以是間接定義。它這樣做是想定義得比較廣，也方便引進 strictly white。

老師說【口頭】：所有定義都會改，三十年後課本的定義可能也不一樣。日本學者 Te Sun Han（⚠️ 逐字稿聽成「Tyson Hahn」）的書一開始就寫：定義非常重要，定錯了後面就很難。花這麼多時間，是要建立嚴謹的思考模式。

---

## 8. 插曲：平穩與非平穩（Pólya 罐子）

[▶ 35:02](https://youtu.be/nq5n-7yJ-kM?t=2102)【口頭】

工程上大部分過程都假設**平穩** (stationary)，討論**非平穩** (non-stationary) 過程或通道的論文很少，但有。例如非平穩訊號源怎麼做資料壓縮。

**例：疾病傳播**（像禽流感）。每個時間有多少人感染是一個隨機過程，而且是非平穩的。常用 **Pólya contagion process**（Pólya 傳染過程）描述：

1. 袋子裡有 4 個紅球、4 個黑球。紅 = 感染，黑 = 沒感染。一開始被感染的機率 $4/8=1/2$。
2. 抓到一個紅球，放回去時**多放一個紅球**。下一次有 5 紅 4 黑，被感染的機率變成 $5/9$。
3. 再抓到紅球，再多放一個紅球，機率更高。疾病會擴散，最後像黑死病一樣失控，全部都是紅球。
4. 抓到黑球（治好一個人），就多放一個黑球。治癒也是擴散的現象。

老師說：已經有數學證明，如果雜訊是這種擴散式的非平穩過程，**通道容量是 0**，沒辦法傳輸，很難對付。自然界很多現象有傳染性、擴散性、相互影響性。

---

## 9. 功率頻譜看不出 strictly 還是 weakly

[▶ 45:47](https://youtu.be/nq5n-7yJ-kM?t=2747)

- 工程上最注重**功率頻譜密度**，常常要畫它。
- 老師一向認為功率頻譜密度應該是**自相關**（包含一階）的傅立葉轉換。
- 功率頻譜只看一階和二階，所以**看不出**過程是 strictly white 還是 weakly white。只看一階、二階時，兩者沒差；更細的分析才有差。

---

## 10. 一頁速查表

### 一階、二階的量

| 名稱 | 公式 |
|---|---|
| 平均功率 | $E\lvert X(t)\rvert^2=R_{XX}(t,t)\ge 0$ |
| 自協方差 | $C_{XX}(t_1,t_2)=R_{XX}(t_1,t_2)-\eta(t_1)\eta^*(t_2)$ |
| 相關係數 | $r=C(t_1,t_2)/\sqrt{C(t_1,t_1)C(t_2,t_2)}$，$\lvert r\rvert\le 1$ |
| 互相關 | $R_{XY}(t_1,t_2)=E[X(t_1)Y^*(t_2)]$ |
| 互協方差 | $C_{XY}=R_{XY}-\eta_X(t_1)\eta_Y^*(t_2)$ |

- 推導關鍵：展開 $E[(X_1-\eta_1)(X_2-\eta_2)^*]$，三項 $\eta_1\eta_2^*$ 抵掉兩項。
- $R$、$C$ 都是非負定；反之非負定函數必是某過程的自相關。

### 限制

| 名稱 | 條件 | 直觀 |
|---|---|---|
| 獨立 | 任何有限樣本的聯合分布 = 乘積 | 只管有限維 |
| 正交 | $R_{XY}=0$ | 含 DC 的能量不互相影響 |
| 不相關 | $C_{XY}=0$ | 變化不互相影響 |
| a-dependent | 間隔 $>a$ 的樣本獨立 | |
| correlation a-dependent | $C(t_1,t_2)=0$，$\lvert t_1-t_2\rvert>a$ | |
| 白（Papoulis） | $C(t_1,t_2)=0$，$t_1\ne t_2$ ⇒ $C=q(t_1)\delta(t_1-t_2)$ | 允許 DC、時變 |
| 嚴格白 | $X(t_1)$、$X(t_2)$ 獨立，$t_1\ne t_2$ | |

### 白雜訊的定義比較

- Proakis：$R(\tau)=\frac{N_0}{2}\delta(\tau)$，PSD flat → 不允許 DC（DC 會在 $f=0$ 多一個 $C\delta(f)$）、隱含平穩。
- Gray & Davisson：PSD = 自協方差的傅立葉轉換且為常數 → 排除 DC。
- Papoulis：最廣，間接定義。

---

## 11. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 平穩 (stationary) | 下一集起：SSS、WSS 的定義 |
| WSS 過程的傅立葉轉換是時變白過程 | §11-4 頻譜表示（第 28–29 集） |
| 功率頻譜密度 = 自相關的傅立葉轉換 | §9-3 Power Spectrum（第 12–14 集） |
| 白雜訊 $q(t)\delta(\tau)$ | 系統輸入白雜訊（§9-2，第 9–11 集） |
| 三階動差與相位 | 老師說後面會稍微講 |

---

## 附：本集一句話總結

> **自相關含 DC、自協方差扣掉 DC——正交和不相關的差別就在這裡；同樣的道理，「白雜訊」在 Papoulis（不相關、允許 DC 和時變）、Proakis（$\frac{N_0}{2}\delta(\tau)$、flat 排除 DC）、Gray & Davisson（自協方差的頻譜是常數）三本書裡定義都不一樣，讀定義要讀到它允許什麼、排除什麼。**

---

## ⚠️ 待確認清單

1. [▶ 10:46](https://youtu.be/nq5n-7yJ-kM?t=646) 「獨立」的投影片定義是「兩個過程獨立」還是「一個過程的樣本互相獨立」，逐字稿兩種說法都有。
2. [▶ 40:09](https://youtu.be/nq5n-7yJ-kM?t=2409) Davisson 證出的定理，逐字稿聽成「Best Competition Theorem」，不確定是哪個。
3. [▶ 33:31](https://youtu.be/nq5n-7yJ-kM?t=2011) 「Tyson Hahn」推測是 Te Sun Han，書名沒說。
4. 上課日期：OCW 頁面和逐字稿都沒寫。

---

*筆記依據陳伯寧老師「隨機過程」Lec 9-1 (4/7) 錄影逐字稿（whisper large-v3-turbo，47:03）與 Papoulis & Pillai《Probability, Random Variables and Stochastic Processes》4th ed. 整理。*
