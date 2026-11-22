---
course: 高等統計學（數理統計續）
episode: 23
lecture: Lec23（第十二週 2/2）
date: 待補
video: https://youtu.be/ZYEZbPNdqcQ
notes: Hogg 8th ed. §4.2 兩平均數差的信賴區間、比例的大樣本信賴區間；§4.5–4.6 檢定；§8.3.2 變異數相等
---

# 第 23 集 · 第十二週 (2/2)：兩平均數的信賴區間與檢定（兩階段）；比例 p 的大樣本檢定；p₁−p₂ [▶ 影片](https://youtu.be/ZYEZbPNdqcQ)

← 上一集：[22](22-lrt-equal-variances-derivation.md) ｜ [總目錄](../README.md) ｜ 下一集：[24](24-p1-p2-test-bivariate-normal-preliminaries.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 23 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 46 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.2、§4.5、§8.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「信賴區間」→「信奈區間／心愛期間／心態期間」，「pivotal quantity」→「pubular quantity」，「Bernoulli」→「本努力／Bernouni」，「二項」→「歐項」，「近似」→「近視」，「Slutsky」→「Slaski」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 兩個母體、兩個平均數](#1-兩個母體兩個平均數)
- [2. 情形一：已知變異數相等](#2-情形一已知變異數相等)
- [3. 情形二：不知道變異數是否相等（兩階段）](#3-情形二不知道變異數是否相等兩階段)
- [4. 成功機率 p 為什麼重要](#4-成功機率-p-為什麼重要)
- [5. p 的大樣本推論](#5-p-的大樣本推論)
- [6. p₁−p₂ 的大樣本信賴區間](#6-p₁p₂-的大樣本信賴區間)
- [7. 一頁速查表](#7-一頁速查表)
- [8. 與後續集數的連結](#8-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/ZYEZbPNdqcQ?t=0) 把前面講的東西整合起來。

| 主題 | 課本 |
|---|---|
| $\mu_1-\mu_2$ 的 CI 與檢定（變異數相等） | §4.2 |
| 先檢定變異數相等（F），再做 $t$ | §8.3.2 |
| $p$ 的大樣本 CI 與檢定 | §4.2、§4.5 |
| $p_1-p_2$ 的大樣本 CI | §4.2 |


---

## 1. 兩個母體、兩個平均數

[▶ 00:33](https://youtu.be/ZYEZbPNdqcQ?t=33) 統計最想做的是平均數，尤其是**兩個**平均數之間的關係：

- 信賴區間：$\mu_1-\mu_2$（difference of means）；
- 檢定：$H_0:\mu_1=\mu_2$。

兩個母體（population 1、2），各抽一組樣本，都假設常態：$N(\mu_1,\sigma_1^2)$、$N(\mu_2,\sigma_2^2)$；兩個母體**獨立**。

[▶ 03:07](https://youtu.be/ZYEZbPNdqcQ?t=187) 兩條路：

1. 從過去經驗已經知道變異數相等；
2. 不知道，要先檢定。

---

## 2. 情形一：已知變異數相等

[▶ 03:38](https://youtu.be/ZYEZbPNdqcQ?t=218) $\sigma_1^2=\sigma_2^2=\sigma^2$。$X_1,\dots,X_n$ iid $N(\mu_1,\sigma^2)$，$Y_1,\dots,Y_m$ iid $N(\mu_2,\sigma^2)$，獨立。

**建構**（[▶ 04:40](https://youtu.be/ZYEZbPNdqcQ?t=280)）：

- $\bar X\sim N\left(\mu_1,\frac{\sigma^2}{n}\right)$，$\frac{(n-1)S_x^2}{\sigma^2}\sim\chi^2(n-1)$，兩者獨立。
- $\bar Y\sim N\left(\mu_2,\frac{\sigma^2}{m}\right)$，$\frac{(m-1)S_y^2}{\sigma^2}\sim\chi^2(m-1)$，兩者獨立。
- [▶ 05:43](https://youtu.be/ZYEZbPNdqcQ?t=343) 兩個母體獨立 ⇒ 四個量全部獨立。

[▶ 06:13](https://youtu.be/ZYEZbPNdqcQ?t=373)
$$\bar X-\bar Y\sim N\left(\mu_1-\mu_2,\ \sigma^2\left(\frac1n+\frac1m\right)\right),\qquad\frac{(n-1)S_x^2+(m-1)S_y^2}{\sigma^2}\sim\chi^2(n+m-2).$$

標準常態 ÷ $\sqrt{\chi^2/\text{df}}$，$\sigma$ 消掉（[▶ 07:13](https://youtu.be/ZYEZbPNdqcQ?t=433)）：
$$T=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_p\sqrt{\frac1n+\frac1m}}\sim t(n+m-2),\qquad S_p^2=\frac{(n-1)S_x^2+(m-1)S_y^2}{n+m-2}.$$

**信賴區間**（[▶ 08:15](https://youtu.be/ZYEZbPNdqcQ?t=495)）：
$$(\bar X-\bar Y)\pm t_{\alpha/2}(n+m-2)\,S_p\sqrt{\frac1n+\frac1m}.$$
（自己去導。）

**檢定** $H_0:\mu_1=\mu_2$ vs $H_1:\mu_1\ne\mu_2$（[▶ 09:15](https://youtu.be/ZYEZbPNdqcQ?t=555)）：樞紐量（pivotal quantity）把 $H_0$ 的訊息帶進來（$\mu_1-\mu_2=0$）就變成**檢定統計量**（test statistic）：
$$T=\frac{\bar X-\bar Y}{S_p\sqrt{\frac1n+\frac1m}}\sim t(n+m-2)\ \ (H_0\text{ 下}).$$
拒絕域：$|T|\ge t_{\alpha/2}(n+m-2)$。$H_0$ 下外面兩塊合起來剛好 $\alpha$。

---

## 3. 情形二：不知道變異數是否相等（兩階段）

[▶ 11:51](https://youtu.be/ZYEZbPNdqcQ?t=711) 例如考試題目沒告訴你變異數是否相等。

**第一階段**（[▶ 12:56](https://youtu.be/ZYEZbPNdqcQ?t=776)）：檢定
$$H_0:\frac{\sigma_1^2}{\sigma_2^2}=1\quad\text{vs}\quad H_1:\frac{\sigma_1^2}{\sigma_2^2}\ne 1.$$
$H_0$ 下 $F=\frac{S_y^2}{S_x^2}\sim F(m-1,n-1)$。拒絕域：
$$F\le\frac{1}{F_{1-\alpha/2}(n-1,m-1)}\quad\text{或}\quad F\ge F_{1-\alpha/2}(m-1,n-1).$$

（[▶ 14:31](https://youtu.be/ZYEZbPNdqcQ?t=871) 老師先把自由度寫成 $n-1,m-1$，隨即改正為 $m-1,n-1$。）

**第二階段**（[▶ 18:46](https://youtu.be/ZYEZbPNdqcQ?t=1126)）：

- 算出 $F$ 值落在兩點中間 ⇒ **接受 $H_0$** ⇒ 相信變異數相等 ⇒ 用情形一的 $t$ 區間、$t$ 檢定。
- [▶ 20:50](https://youtu.be/ZYEZbPNdqcQ?t=1250) **拒絕 $H_0$** ⇒ 變異數不相等 ⇒ 上面的公式都不對。這變成很困難的問題，課堂不做下去。

【課本補充】變異數不相等的兩平均數問題（Behrens–Fisher 問題）一般用近似方法（例如 Welch $t$ 檢定）。這段不是逐字稿內容，課堂沒講。

---

## 4. 成功機率 p 為什麼重要

【口頭】[▶ 21:51](https://youtu.be/ZYEZbPNdqcQ?t=1311)

- 一個、兩個平均數（$t$、F 分配）講完了。接著有興趣的是 $p$：**成功的機率**。
- 跟醫學、藥有關：吃了藥病會好的機率就是成功機率。在生物科學、**生物統計**裡非常重要。
- [▶ 22:53](https://youtu.be/ZYEZbPNdqcQ?t=1373) 也會討論**兩個**成功機率：發明新藥說它很好，不可能沒有比較就說最好，要跟現在大家在用的藥比較——兩個成功機率的差的信賴區間、或是否相等的檢定。
- [▶ 23:24](https://youtu.be/ZYEZbPNdqcQ?t=1404) 分配和 Bernoulli、二項有關，沒辦法找剛好 $100(1-\alpha)\%$ 的信賴區間、剛好顯著水準 $\alpha$ 的檢定，只能找**近似**的——用中央極限定理。
- [▶ 23:55](https://youtu.be/ZYEZbPNdqcQ?t=1435) 以前只講了信賴區間，現在把檢定一起講。樞紐量和檢定統計量是一樣的東西，可以一起做。

---

## 5. p 的大樣本推論

[▶ 24:28](https://youtu.be/ZYEZbPNdqcQ?t=1468) $Y$＝成功的個數，$Y\sim b(n,p)$。唯一觀察得到的是 $Y$。

**造 Bernoulli**（[▶ 24:58](https://youtu.be/ZYEZbPNdqcQ?t=1498)）：**令** $Y_1,\dots,Y_n$ iid Bernoulli$(p)$。

- [▶ 25:29](https://youtu.be/ZYEZbPNdqcQ?t=1529) 不能說它們是隨機樣本：隨機樣本是 iid 而且**可以觀察**的；這些是我們給的，觀察不到，只能說是 iid 隨機變數。
- [▶ 26:30](https://youtu.be/ZYEZbPNdqcQ?t=1590) $\sum Y_i\sim b(n,p)$ ⇒ $Y\overset{D}{=}\sum Y_i$。

**一致性**（[▶ 27:00](https://youtu.be/ZYEZbPNdqcQ?t=1620)）：$\hat p=\frac Yn$（可觀察）$\overset{D}{=}\frac1n\sum Y_i$。Bernoulli 的 $\mu=p$、$\sigma^2=p(1-p)$。WLLN：$\frac1n\sum Y_i\xrightarrow{P}p$；分配一樣 ⇒
$$\hat p\xrightarrow{P}p.$$

**CLT**（[▶ 30:45](https://youtu.be/ZYEZbPNdqcQ?t=1845)）：
$$\frac{\hat p-p}{\sqrt{p(1-p)/n}}\overset{D}{=}\frac{\bar Y-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1).$$

**分母換成 $\hat p$**（[▶ 33:49](https://youtu.be/ZYEZbPNdqcQ?t=2029)）：
$$\frac{\hat p-p}{\sqrt{\hat p(1-\hat p)/n}}=\underbrace{\frac{\hat p-p}{\sqrt{p(1-p)/n}}}_{\xrightarrow{D}N(0,1)}\cdot\underbrace{\sqrt{\frac{p(1-p)}{\hat p(1-\hat p)}}}_{\xrightarrow{P}1}\xrightarrow{D}N(0,1)$$
（第二項是 $\hat p$ 的連續函數；Slutsky 定理。）

**信賴區間**（[▶ 36:56](https://youtu.be/ZYEZbPNdqcQ?t=2216)）：$\hat p\pm z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}$。

**檢定** $H_0:p=p_0$ vs $H_1:p\ne p_0$（[▶ 37:26](https://youtu.be/ZYEZbPNdqcQ?t=2246)）：$H_0$ 下
$$Z=\frac{\hat p-p_0}{\sqrt{\hat p(1-\hat p)/n}}\ \dot\sim\ N(0,1).$$
拒絕域：$|Z|\ge z_{\alpha/2}$。

**size 近似 $\alpha$**（[▶ 38:27](https://youtu.be/ZYEZbPNdqcQ?t=2307)）：
$$P_{H_0}(|Z|\ge z_{\alpha/2})=1-P_{H_0}(-z_{\alpha/2}<Z<z_{\alpha/2})\approx 1-(1-\alpha)=\alpha.$$
只能寫「近似」，因為它不是真正的 $N(0,1)$。

以下**不是逐字稿內容**，是補充：課堂檢定統計量的分母用 $\hat p$；另一個常見寫法是分母用 $p_0$（$H_0$ 下的變異數 $p_0(1-p_0)/n$），兩者大樣本下都近似 $N(0,1)$。

---

## 6. p₁−p₂ 的大樣本信賴區間

[▶ 40:30](https://youtu.be/ZYEZbPNdqcQ?t=2430) 兩個母體。

【口頭】[▶ 41:00](https://youtu.be/ZYEZbPNdqcQ?t=2460) 例如亞洲人和美國人吃同一種藥，藥效一不一樣？要從美國進口藥，要知道我們吃的藥效跟美國人是不是一樣——美國人通常比較壯、比較高，那個藥我們吃會不會太重。[▶ 42:33](https://youtu.be/ZYEZbPNdqcQ?t=2553) 兩組要獨立：在台灣找人吃藥，要先問清楚有沒有親戚在美國——怕找到有相關的人。

**設定**（[▶ 42:02](https://youtu.be/ZYEZbPNdqcQ?t=2522)）：$X\sim b(n,p_1)$、$Y\sim b(m,p_2)$ 獨立；$\hat p_1=\frac Xn$，$\hat p_2=\frac Ym$。

[▶ 43:37](https://youtu.be/ZYEZbPNdqcQ?t=2617)

- $\hat p_1\ \dot\sim\ N\left(p_1,\frac{p_1(1-p_1)}{n}\right)$，$\hat p_2\ \dot\sim\ N\left(p_2,\frac{p_2(1-p_2)}{m}\right)$，獨立。
- 相減：平均數相減、變異數相加，近似常態；標準化近似 $N(0,1)$。
- [▶ 45:12](https://youtu.be/ZYEZbPNdqcQ?t=2712) 分母的 $p_1,p_2$ 換成 $\hat p_1,\hat p_2$（$\hat p_i\xrightarrow{P}p_i$），仍近似 $N(0,1)$。

> **$p_1-p_2$ 的近似 $100(1-\alpha)\%$ 信賴區間**（[▶ 45:43](https://youtu.be/ZYEZbPNdqcQ?t=2743)）：
> $$(\hat p_1-\hat p_2)\pm z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}.$$

[▶ 46:15](https://youtu.be/ZYEZbPNdqcQ?t=2775) 下次用這個東西做假設檢定。

---

## 7. 一頁速查表

**兩平均數（變異數相等）**：
$$S_p^2=\frac{(n-1)S_x^2+(m-1)S_y^2}{n+m-2},\qquad T=\frac{(\bar X-\bar Y)-(\mu_1-\mu_2)}{S_p\sqrt{\frac1n+\frac1m}}\sim t(n+m-2).$$

| | 結果 |
|---|---|
| CI | $(\bar X-\bar Y)\pm t_{\alpha/2}(n+m-2)S_p\sqrt{\frac1n+\frac1m}$ |
| 檢定 $\mu_1=\mu_2$ | $\left\lvert\frac{\bar X-\bar Y}{S_p\sqrt{1/n+1/m}}\right\rvert\ge t_{\alpha/2}(n+m-2)$ |

**不知道變異數是否相等**：先 F 檢定 → 接受就用上表；拒絕則公式不適用（課堂不處理）。

**比例**（$\hat p=Y/n$）：

| | 結果 |
|---|---|
| CI | $\hat p\pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ |
| 檢定 $p=p_0$ | $\left\lvert\frac{\hat p-p_0}{\sqrt{\hat p(1-\hat p)/n}}\right\rvert\ge z_{\alpha/2}$（size $\approx\alpha$） |
| $p_1-p_2$ 的 CI | $(\hat p_1-\hat p_2)\pm z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}$ |

關鍵：$Y\overset{D}{=}\sum$ Bernoulli → WLLN、CLT → Slutsky 換分母。

---

## 8. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| $p_1-p_2$ | 下一集：$H_0:p_1=p_2$ 的檢定 |
| 兩階段（F 再 $t$） | 實務分析流程 |

---

## 附：本集一句話總結

> **比較兩個常態平均數時，變異數相等就用合併變異數 $S_p^2$ 的 $t(n+m-2)$ 做信賴區間與檢定；不知道是否相等就先用 F 檢定，接受了才能用 $t$；成功機率 $p$ 的推論靠「$Y$ 和 Bernoulli 和同分配」加上 WLLN、CLT、Slutsky，得到 $p$ 的近似區間與 size 約 $\alpha$ 的檢定，以及 $p_1-p_2$ 的近似信賴區間。**

---

*筆記依據「高等統計學」Lec23 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
