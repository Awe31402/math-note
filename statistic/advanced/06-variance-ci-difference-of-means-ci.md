---
course: 高等統計學（數理統計續）
episode: 6
lecture: Lec06（第四週 1/2）
date: 待補
video: https://youtu.be/3s9RAyloSGU
notes: Hogg 8th ed. §4.2 常態變異數的信賴區間；兩個常態平均數差的信賴區間（pooled $t$，p. 241–243）
---

# 第 6 集 · 第四週 (1/2)：$\sigma^2$ 的信賴區間；兩個常態平均數差 $\mu_X-\mu_Y$ 的信賴區間 [▶ 影片](https://youtu.be/3s9RAyloSGU)

← 上一集：[05](05-normal-mean-ci-sigma-known-unknown-chi-square-table.md) ｜ [總目錄](../README.md) ｜ 下一集：[07](07-large-sample-theory-clt-wlln-modes-of-convergence.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 6 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:14:45，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「卡方」→「攪檔／卡丸／卡荒」，「信賴區間」→「信奈區間」，「pivotal quantity」→「pubular／Pubert quantity」，「variance」→「valence」，「LSL／USL」→「LCL／UCL」。[▶ 27:48](https://youtu.be/3s9RAyloSGU?t=1668)–[▶ 31:48](https://youtu.be/3s9RAyloSGU?t=1908)、[▶ 48:53](https://youtu.be/3s9RAyloSGU?t=2933)–[▶ 53:23](https://youtu.be/3s9RAyloSGU?t=3203) 沒有講課內容（whisper 幻聽字），應是老師在黑板寫字或休息。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. σ² 的信賴區間](#1-σ-的信賴區間)
- [2. σ 或其他一對一函數的信賴區間](#2-σ-或其他一對一函數的信賴區間)
- [3. 為什麼關心 mean 和 variance](#3-為什麼關心-mean-和-variance)
- [4. 為什麼關心兩個 mean 的差](#4-為什麼關心兩個-mean-的差)
- [5. μ_X−μ_Y：兩個變異數已知](#5-μ_xμ_y兩個變異數已知)
- [6. μ_X−μ_Y：變異數未知但相等](#6-μ_xμ_y變異數未知但相等)
- [7. 預告：近似信賴區間](#7-預告近似信賴區間)
- [8. 隨機變數在實際上代表什麼](#8-隨機變數在實際上代表什麼)
- [9. 一頁速查表](#9-一頁速查表)
- [10. 與後續集數的連結](#10-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 樞紐量 | 分配 |
|---|---|---|
| $\sigma^2$ | $\frac{(n-1)S^2}{\sigma^2}$ | $\chi^2(n-1)$ |
| $\mu_X-\mu_Y$，$\sigma_X^2,\sigma_Y^2$ 已知 | $\frac{(\bar X-\bar Y)-(\mu_X-\mu_Y)}{\sqrt{\sigma_X^2/n+\sigma_Y^2/m}}$ | $N(0,1)$ |
| $\mu_X-\mu_Y$，$\sigma_X^2=\sigma_Y^2$ 未知 | $\frac{(\bar X-\bar Y)-(\mu_X-\mu_Y)}{S_p\sqrt{1/n+1/m}}$ | $t(n+m-2)$ |

---

## 1. σ² 的信賴區間

[▶ 00:30](https://youtu.be/3s9RAyloSGU?t=30) 卡方 pdf 從 0 開始、往右拖到無窮。卡方分配可以建造 $\sigma^2$ 的信賴區間。

$X_1,\dots,X_n$ 來自 $N(\mu,\sigma^2)$，找 $\sigma^2$ 的信賴區間。

**Step 1：樞紐量**（[▶ 01:30](https://youtu.be/3s9RAyloSGU?t=90)）。要找 $\sigma^2$，樞紐量裡的參數應該是 $\sigma^2$；**不能有 $\mu$**（$\mu$ 也未知，有它就沒用）。
$$Q=\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1),\qquad S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2.$$
是樣本和 $\sigma^2$ 的函數；卡方在自由度已知時不含參數 ⇒ 樞紐量。

**Step 2：找兩點**（[▶ 04:34](https://youtu.be/3s9RAyloSGU?t=274)）。卡方不對稱，兩邊各留 $\alpha/2$（老師的記號：下標是**以下**的機率）：
$$P\left(\chi^2_{\alpha/2}(n-1)\le\frac{(n-1)S^2}{\sigma^2}\le\chi^2_{1-\alpha/2}(n-1)\right)=1-\alpha.$$

**Step 3：改寫成 $\sigma^2$ 在中間**（[▶ 06:42](https://youtu.be/3s9RAyloSGU?t=402)）。

- 右邊不等式：$\sigma^2$ 乘過去、$\chi^2_{1-\alpha/2}$ 除過來 ⇒ $\sigma^2\ge\dfrac{(n-1)S^2}{\chi^2_{1-\alpha/2}}$。
- 左邊不等式 ⇒ $\sigma^2\le\dfrac{(n-1)S^2}{\chi^2_{\alpha/2}}$。

（右邊的不等式變成左邊、左邊的變成右邊。）

> **結果**（[▶ 08:15](https://youtu.be/3s9RAyloSGU?t=495)）：$\sigma^2$ 的 $100(1-\alpha)\%$ 信賴區間
> $$\left(\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)},\ \frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)}\right).$$

- 每一步是一對一轉換，三個事件一樣，機率都是 $1-\alpha$。
- 兩端只有 $S^2$（樣本算的）、查表值、$n$ ⇒ 統計量。

---

## 2. σ 或其他一對一函數的信賴區間

[▶ 09:50](https://youtu.be/3s9RAyloSGU?t=590) 有時想要的是 $\sigma$。

- 卡方的兩個查表值都是正的，$S^2$、$n-1$ 都正，三項都 $>0$。
- 同時開根號是一對一轉換：
$$\left(\sqrt{\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}}},\ \sqrt{\frac{(n-1)S^2}{\chi^2_{\alpha/2}}}\right)\text{ 是 }\sigma\text{ 的 }100(1-\alpha)\%\text{ 信賴區間}.$$
- [▶ 11:25](https://youtu.be/3s9RAyloSGU?t=685) 只要是一對一（遞增）轉換都行：取三次方、取 $e^{(\cdot)}$……可以造很多。

---

## 3. 為什麼關心 mean 和 variance

[▶ 12:28](https://youtu.be/3s9RAyloSGU?t=748) 【口頭】mean 是中心點。很多人讀統計後到科學園區做**品管**（品質管制）、**品保**（品質保證）。

**傳統產品 vs 高科技產品**（[▶ 13:00](https://youtu.be/3s9RAyloSGU?t=780)）：

- 牛仔褲：以前在台灣生產，後來去中國，現在很多去非洲（人工越來越便宜）。工人不用唸什麼書，做出來照樣賣到美國、歐洲、亞洲，因為**太容易生產**。左右長度差一點、顏色濃淡不一，沒人在乎；現在還故意破個洞，不破反而奇怪。品質變化很大都還是好的，要做出壞的反而很難。
- [▶ 14:35](https://youtu.be/3s9RAyloSGU?t=875) 高科技產品很難：台積電是全世界最大的晶圓代工、第二大是聯電。晶圓從 4 吋、6 吋、8 吋到 12 吋，尺寸越大一次產量越大，但**越難生產**。早期台灣很多半導體工廠都倒了，能存下來的才厲害。生產過程什麼時候會壞沒人知道，所以要統計的人去預測產品有沒有問題。

**規格上下限**（[▶ 16:41](https://youtu.be/3s9RAyloSGU?t=1001)）：每個產品都有標準，有規格的下限和上限，在裡面是好的。

- 品質分配的中心 $\mu$ 在規格中間，大部分產品都在規格內。
- 技術更好 → $\sigma$ 更小 → 分配更集中，壞的更少。所以 $\sigma^2$ 的信賴區間很短就很好。
- [▶ 18:14](https://youtu.be/3s9RAyloSGU?t=1094) 但分配可能**移動**：原料來源出問題、機台程式跑掉、電力供應不穩……整批移出去，大部分都壞了。
- 所以要管制 **mean**（不要跑掉）和 **variance**（不要太大）。這就是為什麼不管區間估計還是檢定，都在討論 $\mu$ 和 $\sigma^2$。

---

## 4. 為什麼關心兩個 mean 的差

[▶ 20:16](https://youtu.be/3s9RAyloSGU?t=1216) 兩個母體，各抽一組樣本，比較兩個平均是否一樣。mean 大概代表產品的品質。

【口頭】[▶ 20:46](https://youtu.be/3s9RAyloSGU?t=1246) 統計會發展出來，相當大的原因是**歐美改善農產品**：

- 歐美大量生產、土地一大片、用機械。要提高品質或產量，一直在開發新品種。
- [▶ 21:48](https://youtu.be/3s9RAyloSGU?t=1308) 養豬：新品種養三個月後的**平均體重**有沒有比舊品種重？美國種小麥、玉米、黃豆：新品種每公畝的平均產量有沒有比較大？
- [▶ 22:53](https://youtu.be/3s9RAyloSGU?t=1373) 生物科技：新藥要上市，要和市場上原有的藥比，治好的機率要比較大。
- 都在做**比較**。
- [▶ 23:55](https://youtu.be/3s9RAyloSGU?t=1435) 一百頭豬三個月後體重不會一樣，所以背後有分配、有平均數。

[▶ 25:27](https://youtu.be/3s9RAyloSGU?t=1527) **設定**：

- 母體 1：$N(\mu_X,\sigma_X^2)$，樣本 $X_1,\dots,X_n$。
- 母體 2：$N(\mu_Y,\sigma_Y^2)$，樣本 $Y_1,\dots,Y_m$。
- 兩個母體**獨立**；$n,m$ 可以不一樣。
- 想知道 $\mu_X=\mu_Y$ 嗎？看差 $\mu_X-\mu_Y$。找它的信賴區間。

【口頭】[▶ 26:28](https://youtu.be/3s9RAyloSGU?t=1588) 兩個平均數差的問題，其實是統計裡最重要的問題。

---

## 5. μ_X−μ_Y：兩個變異數已知

[▶ 32:18](https://youtu.be/3s9RAyloSGU?t=1938)

**Step 1：$\bar X$、$\bar Y$ 的分配**

$$\bar X\sim N\left(\mu_X,\frac{\sigma_X^2}{n}\right),\qquad\bar Y\sim N\left(\mu_Y,\frac{\sigma_Y^2}{m}\right).$$

[▶ 33:52](https://youtu.be/3s9RAyloSGU?t=2032) 兩個母體獨立 ⇒ 兩組樣本獨立 ⇒ $\bar X\perp\bar Y$。（獨立的東西各自取函數還是獨立：$X_1,\dots,X_n$ 和 $Y_1,\dots,Y_m$ 兩組獨立，各取一個函數仍獨立。）

**Step 2：$\bar X-\bar Y$**（[▶ 35:24](https://youtu.be/3s9RAyloSGU?t=2124)）。獨立常態相減還是常態（用 mgf 證）：

- mean：$\mu_X-\mu_Y$。
- variance：$\text{Var}(\bar X+(-1)\bar Y)=\text{Var}(\bar X)+(-1)^2\text{Var}(\bar Y)=\dfrac{\sigma_X^2}{n}+\dfrac{\sigma_Y^2}{m}$（**相加**）。

[▶ 36:57](https://youtu.be/3s9RAyloSGU?t=2217) 為什麼用 $\bar X-\bar Y$？因為會跑出 $\mu_X-\mu_Y$，正是要的。

**Step 3：樞紐量**（[▶ 37:29](https://youtu.be/3s9RAyloSGU?t=2249)）
$$Z=\frac{(\bar X-\bar Y)-(\mu_X-\mu_Y)}{\sqrt{\sigma_X^2/n+\sigma_Y^2/m}}\sim N(0,1).$$

**Step 4：改寫**（[▶ 39:31](https://youtu.be/3s9RAyloSGU?t=2371)）。$P(-z_{\alpha/2}\le Z\le z_{\alpha/2})=1-\alpha$，分母乘到兩邊、移項（老師說自己導一下）：

> **結果**（[▶ 41:02](https://youtu.be/3s9RAyloSGU?t=2462)）：
> $$(\bar X-\bar Y)\pm z_{\alpha/2}\sqrt{\frac{\sigma_X^2}{n}+\frac{\sigma_Y^2}{m}}.$$

[▶ 41:32](https://youtu.be/3s9RAyloSGU?t=2492) 變異數已知的情形有，但不多；大部分是未知的。

---

## 6. μ_X−μ_Y：變異數未知但相等

[▶ 42:02](https://youtu.be/3s9RAyloSGU?t=2522) 規律：變異數已知 → 標準常態；未知 → 要造 $t$ 分配。

[▶ 42:32](https://youtu.be/3s9RAyloSGU?t=2552) **假設**：$\sigma_X^2,\sigma_Y^2$ 未知，但**相等**，記作 $\sigma^2$。

【口頭】如果不相等，處理很困難（不是沒辦法，是超出這門課的範圍）。

**Step 1：四個東西**（[▶ 44:35](https://youtu.be/3s9RAyloSGU?t=2675)）

| | 分配 |
|---|---|
| $\bar X$ | $N(\mu_X,\sigma^2/n)$ |
| $\frac{(n-1)S_X^2}{\sigma^2}$ | $\chi^2(n-1)$ |
| $\bar Y$ | $N(\mu_Y,\sigma^2/m)$ |
| $\frac{(m-1)S_Y^2}{\sigma^2}$ | $\chi^2(m-1)$ |

$S_X^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$，$S_Y^2=\frac{1}{m-1}\sum(Y_i-\bar Y)^2$。

⚠️ 逐字稿缺字：[▶ 45:08](https://youtu.be/3s9RAyloSGU?t=2708) 老師口頭更正：剛才板書寫除以 $n$，要改成 $n-1$（$Y$ 那邊改成 $m-1$）。

**為什麼四個全部獨立**（[▶ 45:39](https://youtu.be/3s9RAyloSGU?t=2739)）：

- 同一組常態樣本的 $\bar X$ 和 $S_X^2$ 獨立（上學期證過；一般同一組樣本造的兩個東西不會獨立，常態才會）。$\bar Y,S_Y^2$ 同理。
- [▶ 47:12](https://youtu.be/3s9RAyloSGU?t=2832) 兩個母體獨立 ⇒ 上面兩個和下面兩個獨立。
- 所以四個彼此獨立。

**Step 2：分子和分母**（[▶ 54:31](https://youtu.be/3s9RAyloSGU?t=3271)）

- $\bar X-\bar Y\sim N\left(\mu_X-\mu_Y,\ \sigma^2\left(\frac1n+\frac1m\right)\right)$。
- 兩個獨立卡方相加還是卡方，自由度相加：
$$\frac{(n-1)S_X^2+(m-1)S_Y^2}{\sigma^2}\sim\chi^2(n+m-2).$$
- [▶ 55:34](https://youtu.be/3s9RAyloSGU?t=3334) 第一個是（第 1、3 個）的函數，第二個是（第 2、4 個）的函數，兩組不同 ⇒ 獨立。

**Step 3：造 $t$**（[▶ 57:09](https://youtu.be/3s9RAyloSGU?t=3429)）。標準常態 ÷ $\sqrt{\text{卡方}/\text{自由度}}$，$\sigma$ 消掉：
$$T=\frac{\dfrac{(\bar X-\bar Y)-(\mu_X-\mu_Y)}{\sigma\sqrt{1/n+1/m}}}{\sqrt{\dfrac{(n-1)S_X^2+(m-1)S_Y^2}{\sigma^2(n+m-2)}}}=\frac{(\bar X-\bar Y)-(\mu_X-\mu_Y)}{S_p\sqrt{\dfrac1n+\dfrac1m}}\sim t(n+m-2),$$
$$S_p^2=\frac{(n-1)S_X^2+(m-1)S_Y^2}{n+m-2}.$$

（$S_p^2$ 這個名字和記號是依課本加的，老師直接寫整串根號。）

【口頭】[▶ 59:10](https://youtu.be/3s9RAyloSGU?t=3550) 式子看起來非常複雜，一定要會導，不要用背的。

**Step 4：改寫**（[▶ 60:42](https://youtu.be/3s9RAyloSGU?t=3642)）

> **結果**（[▶ 62:14](https://youtu.be/3s9RAyloSGU?t=3734)）：
> $$(\bar X-\bar Y)\pm t_{\alpha/2}(n+m-2)\,S_p\sqrt{\frac1n+\frac1m}.$$

【口頭】[▶ 62:44](https://youtu.be/3s9RAyloSGU?t=3764) 公式非常長，背會很痛苦，一定要知道怎麼導。考統計研究所，筆試過了通常有口試，口試有時就叫你導這個。

---

## 7. 預告：近似信賴區間

[▶ 63:17](https://youtu.be/3s9RAyloSGU?t=3797)

- 到目前講了三種信賴區間，都是涵蓋機率**剛好** $1-\alpha$（exact）。
- 要找得到樞紐量，**而且**樞紐量能一對一改寫成「參數在中間、兩端是統計量」。
- [▶ 64:50](https://youtu.be/3s9RAyloSGU?t=3890) 有時樞紐量沒用（改寫不了），有時連樞紐量都找不到。
- [▶ 65:21](https://youtu.be/3s9RAyloSGU?t=3921) 很多重要問題都找不到 exact 的，就找**近似信賴區間**（approximate confidence interval）：涵蓋機率**近似** $1-\alpha$。

[▶ 66:25](https://youtu.be/3s9RAyloSGU?t=3985) 需要機率的背景：**中央極限定理**（central limit theorem，上學期可能沒講）、弱大數法則、依機率收斂（講過）、**依分配收斂**；以及兩種收斂之間的關係。下次講。

---

## 8. 隨機變數在實際上代表什麼

[▶ 67:26](https://youtu.be/3s9RAyloSGU?t=4046) 【口頭】一開始從數學角度講隨機變數（樣本空間到實數的函數），很難想像實際用途。現在比較容易想：

- [▶ 68:28](https://youtu.be/3s9RAyloSGU?t=4108) 工廠造粉筆：長度、顏色、硬度都是隨機變數——拿 100 根同工廠的粉筆精確去量，都不一樣。但粉筆不太需要統計，長一點短一點、濃一點淡一點沒人在乎。
- [▶ 69:28](https://youtu.be/3s9RAyloSGU?t=4168) 高科技產品品質非常難控制，因為**非常隨機**。所以要了解隨機變數背後的分配：mean、variance。
- [▶ 70:30](https://youtu.be/3s9RAyloSGU?t=4230) 半導體、LCD 工廠要無塵室，不能穿一般衣服進去，連灰塵都不行，可見生產多困難。
- [▶ 71:31](https://youtu.be/3s9RAyloSGU?t=4291) 設備大多是美國、歐洲設計的，但很多拿到台灣生產（美國還有德州儀器、IBM 自己生產一些）。台灣工程師很認真：產線出問題半夜打電話就去公司，常做到晚上九點。美國商店五點一到就不賣了。這是生活態度的差別，所以台灣能把品質控制得比較好。
- [▶ 73:34](https://youtu.be/3s9RAyloSGU?t=4414) 點估計估 $\mu$、$\sigma$ 不可能剛好準，所以要找它應該在哪個範圍：信賴區間。

---

## 9. 一頁速查表

**$\sigma^2$**：
$$\left(\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)},\frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)}\right)$$
（樞紐量 $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$；老師記號下標是左尾機率。）$\sigma$：兩端開根號。

**$\mu_X-\mu_Y$**

| 情形 | 信賴區間 |
|---|---|
| $\sigma_X^2,\sigma_Y^2$ 已知 | $(\bar X-\bar Y)\pm z_{\alpha/2}\sqrt{\frac{\sigma_X^2}{n}+\frac{\sigma_Y^2}{m}}$ |
| 未知但相等 | $(\bar X-\bar Y)\pm t_{\alpha/2}(n+m-2)\,S_p\sqrt{\frac1n+\frac1m}$ |

$S_p^2=\dfrac{(n-1)S_X^2+(m-1)S_Y^2}{n+m-2}$。

關鍵：
- $\text{Var}(\bar X-\bar Y)=\text{Var}\bar X+\text{Var}\bar Y$（獨立，相減變異數相加）。
- $\bar X,S_X^2,\bar Y,S_Y^2$ 四個獨立；兩個卡方相加得 $\chi^2(n+m-2)$。

---

## 10. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 近似信賴區間 | 下一集：中央極限定理、依分配收斂 |
| $\mu_X-\mu_Y$ | 兩樣本 $t$ 檢定 |
| $\sigma^2$ 的卡方區間 | 變異數檢定 |

---

## 附：本集一句話總結

> **$\sigma^2$ 的信賴區間用樞紐量 $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$，兩端各查一個卡方值；兩個常態平均數差 $\mu_X-\mu_Y$：變異數已知用 $\bar X-\bar Y$ 標準化成 $N(0,1)$，未知但相等時把兩個卡方合併成 $\chi^2(n+m-2)$，造出 pooled $t$ 統計量。**

---

*筆記依據「高等統計學」Lec06 錄影逐字稿（whisper large-v3-turbo，1:14:45）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
