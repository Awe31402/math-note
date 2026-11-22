---
course: 高等統計學（數理統計續）
episode: 8
lecture: Lec08（第五週 1/2）
date: 待補
video: https://youtu.be/HCrObDolpWQ
notes: Hogg 8th ed. Theorem 5.2.5 Slutsky（p. 333）；§4.2 大樣本信賴區間（平均數、比例 $p$、$p_1-p_2$）；§5.3 中央極限定理
---

# 第 8 集 · 第五週 (1/2)：Slutsky 定理；近似信賴區間（$\mu$、$p$、$p_1-p_2$）；什麼是好的信賴區間 [▶ 影片](https://youtu.be/HCrObDolpWQ)

← 上一集：[07](07-large-sample-theory-clt-wlln-modes-of-convergence.md) ｜ [總目錄](../README.md) ｜ 下一集：[09](09-hypothesis-testing-intro-null-alternative.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 8 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（1:21:56，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.2、§5.2、§5.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Slutsky」→「Slasky／斯拉斯基」，「近似」→「近視」，「機率收斂」→「激勵收斂」，「pivotal quantity」→「pubular quality」，「Bernoulli」→「Bernoni／本努力」，「二項」→「歐向／偶向」。[▶ 07:15](https://youtu.be/HCrObDolpWQ?t=435)–[▶ 08:15](https://youtu.be/HCrObDolpWQ?t=495) 約 1 分鐘幻聽字，忽略。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Slutsky 定理](#1-slutsky-定理)
- [2. 近似信賴區間：μ（分配未知）](#2-近似信賴區間μ分配未知)
  - [2.1 S² 依機率收斂到 σ²](#21-s-依機率收斂到-σ)
  - [2.2 把 σ 換成 S](#22-把-σ-換成-s)
- [3. 近似信賴區間：二項的 p](#3-近似信賴區間二項的-p)
- [4. 近似信賴區間：p₁−p₂](#4-近似信賴區間p₁p₂)
- [5. 什麼是好的信賴區間](#5-什麼是好的信賴區間)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/HCrObDolpWQ?t=0) 收斂主要兩種：依機率、依分配。統計推論（信賴區間、檢定）想要的是**依分配收斂**：收斂到已知分配（例如 $N(0,1)$），就能算機率、造信賴區間。依機率收斂是**配合**用的。

| 主題 | 課本 |
|---|---|
| Slutsky 定理 | Theorem 5.2.5，p. 333 |
| $\mu$ 的近似信賴區間（分配未知） | §4.2 |
| 二項 $p$、$p_1-p_2$ 的近似信賴區間 | §4.2 |

---

## 1. Slutsky 定理

[▶ 02:03](https://youtu.be/HCrObDolpWQ?t=123) 依機率收斂強、依分配收斂弱，合在一起通常還會收斂，但變弱（依分配）。

> **Slutsky 定理**（課本 Theorem 5.2.5，p. 333）：$X_n\xrightarrow{D}X$，$Y_n\xrightarrow{P}a$（$a$ 是**常數**），則
> 1. $X_n\pm Y_n\xrightarrow{D}X\pm a$；
> 2. $X_nY_n\xrightarrow{D}aX$；
> 3. $X_n/Y_n\xrightarrow{D}X/a$（$a\ne 0$）。

- [▶ 05:12](https://youtu.be/HCrObDolpWQ?t=312) 相除時：依分配收斂的在**分子**，依機率收斂的在**分母**。

【口頭】[▶ 05:43](https://youtu.be/HCrObDolpWQ?t=343) 現在看不太出來，但會慢慢用到，要熟悉。前面講的東西後面都會用到。

---

## 2. 近似信賴區間：μ（分配未知）

[▶ 06:15](https://youtu.be/HCrObDolpWQ?t=375) 有些問題找不到真正的樞紐量，只能找**近似樞紐量**，造**近似信賴區間**（approximate confidence interval）。

[▶ 08:15](https://youtu.be/HCrObDolpWQ?t=495) **設定**：$X_1,\dots,X_n$ 是隨機樣本，**分配未知**（沒說是常態），mean $\mu$、variance $\sigma^2$ 都未知。找 $\mu$ 的信賴區間。分配不知道，不可能建造真正的樞紐量。

### 2.1 S² 依機率收斂到 σ²

[▶ 09:48](https://youtu.be/HCrObDolpWQ?t=588) 要用 Slutsky 的相除，需要一個依機率收斂的東西：證 $S^2\xrightarrow{P}\sigma^2$（上學期證過，再證一遍）。

$$S^2=\frac{1}{n-1}\left[\sum X_i^2-n\bar X^2\right]=\frac{n}{n-1}\cdot\frac1n\sum X_i^2-\frac{n}{n-1}\bar X^2.$$

【口頭】[▶ 10:50](https://youtu.be/HCrObDolpWQ?t=650) $\sum(X_i-\bar X)^2=\sum X_i^2-n\bar X^2$ 要熟悉，自己拆看看。

- [▶ 12:34](https://youtu.be/HCrObDolpWQ?t=754) **WLLN**：iid 的平均依機率收斂到 mean。
- [▶ 14:10](https://youtu.be/HCrObDolpWQ?t=850) $X_i$ iid ⇒ $X_i^2$ iid（獨立的各取函數仍獨立；同分配的取**同一個**函數仍同分配）⇒ $\frac1n\sum X_i^2\xrightarrow{P}E(X^2)$。
- [▶ 17:47](https://youtu.be/HCrObDolpWQ?t=1067) $\bar X\xrightarrow{P}\mu$；平方是連續函數 ⇒ $\bar X^2\xrightarrow{P}\mu^2$。
- $\frac{n}{n-1}\to 1$。

[▶ 20:34](https://youtu.be/HCrObDolpWQ?t=1234) 合起來：$S^2\xrightarrow{P}E(X^2)-\mu^2=\sigma^2$（$E(X^2)=\mu^2+\sigma^2$）。

### 2.2 把 σ 換成 S

[▶ 22:06](https://youtu.be/HCrObDolpWQ?t=1326) 要的是 $\frac{\bar X-\mu}{S/\sqrt n}$（不能有 $\sigma$，有 $\sigma$ 就不是樞紐量）。乘一個除一個 $\sigma$：

$$\frac{\bar X-\mu}{S/\sqrt n}=\underbrace{\frac{\bar X-\mu}{\sigma/\sqrt n}}_{\xrightarrow{D}N(0,1)\ (\text{CLT})}\cdot\underbrace{\frac{\sigma}{S}}_{\xrightarrow{P}1}.$$

- [▶ 23:41](https://youtu.be/HCrObDolpWQ?t=1421) 第一項：**中央極限定理**。
- [▶ 23:41](https://youtu.be/HCrObDolpWQ?t=1421) 第二項：$\frac{\sigma}{S}=\frac{\sigma}{\sqrt{S^2}}$ 是 $S^2$ 的連續函數；$S^2\xrightarrow{P}\sigma^2$ ⇒ $\frac{\sigma}{S}\xrightarrow{P}\frac{\sigma}{\sigma}=1$。
- [▶ 25:45](https://youtu.be/HCrObDolpWQ?t=1545) **Slutsky**（相乘）：
$$\frac{\bar X-\mu}{S/\sqrt n}\xrightarrow{D}N(0,1).$$

**造區間**（[▶ 26:46](https://youtu.be/HCrObDolpWQ?t=1606)）：分配函數收斂 ⇒ 在同兩點之間的機率很接近：
$$P\left(-z_{\alpha/2}\le\frac{\bar X-\mu}{S/\sqrt n}\le z_{\alpha/2}\right)\approx P(-z_{\alpha/2}\le Z\le z_{\alpha/2})=1-\alpha.$$
分母乘過去、移項：

> **結果**（[▶ 32:20](https://youtu.be/HCrObDolpWQ?t=1940)）：$\mu$ 的近似 $100(1-\alpha)\%$ 信賴區間
> $$\bar X\pm z_{\alpha/2}\frac{S}{\sqrt n}.$$

不知道分配也能用。

---

## 3. 近似信賴區間：二項的 p

[▶ 33:26](https://youtu.be/HCrObDolpWQ?t=2006) $Y\sim b(n,p)$（只有一個隨機變數），找 $p$ 的信賴區間。【口頭】不同問題有不同的處理方式，要幫它**創造**一些東西。

**Step 1：造 Bernoulli**（[▶ 34:26](https://youtu.be/HCrObDolpWQ?t=2066)）。令 $X_1,\dots,X_n$ iid Bernoulli$(p)$（我們造出來的，實際上沒有）。$\sum X_i\sim b(n,p)$（用 mgf 證）。所以
$$Y\overset{D}{=}\sum X_i\quad(\text{分配相同}).$$

**Step 2：分配相同的數列收斂也一樣**（[▶ 37:31](https://youtu.be/HCrObDolpWQ?t=2251)）：若 $X_n\overset{D}{=}Y_n$，$X_n\xrightarrow{P}X$ ⇒ $Y_n\xrightarrow{P}X$；依分配收斂也一樣。

**Step 3：$\hat p=Y/n\xrightarrow{P}p$**（[▶ 38:35](https://youtu.be/HCrObDolpWQ?t=2315)）：$\hat p\overset{D}{=}\bar X$；WLLN ⇒ $\bar X\xrightarrow{P}E(X)=p$。所以 $\hat p\xrightarrow{P}p$。

**Step 4：CLT**（[▶ 40:08](https://youtu.be/HCrObDolpWQ?t=2408)）：$E\hat p=p$，$\text{Var}\hat p=\frac{p(1-p)}{n}$。Bernoulli 的 $\mu=p$、$\sigma^2=p(1-p)$，所以
$$\frac{\hat p-p}{\sqrt{p(1-p)/n}}\overset{D}{=}\frac{\bar X-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1).$$

**Step 5：沒用的樞紐量**（[▶ 46:43](https://youtu.be/HCrObDolpWQ?t=2803)）：上式近似 $N(0,1)$、是近似樞紐量，但分母有 $p$，**改寫不成 $p$ 在中間**。沒用。

**Step 6：分母換成 $\hat p$**（[▶ 47:43](https://youtu.be/HCrObDolpWQ?t=2863)）：
$$\frac{\hat p-p}{\sqrt{\hat p(1-\hat p)/n}}=\underbrace{\frac{\hat p-p}{\sqrt{p(1-p)/n}}}_{\xrightarrow{D}N(0,1)}\cdot\underbrace{\sqrt{\frac{p(1-p)}{\hat p(1-\hat p)}}}_{\xrightarrow{P}1}.$$
第二項是 $\hat p$ 的連續函數，$\hat p\xrightarrow{P}p$ ⇒ 收斂到 1。Slutsky ⇒ 整個 $\xrightarrow{D}N(0,1)$。

這個可以算：只有 $\hat p=Y/n$。

**Step 7：造區間**（[▶ 51:29](https://youtu.be/HCrObDolpWQ?t=3089)）

> **結果**（[▶ 54:46](https://youtu.be/HCrObDolpWQ?t=3286)）：$p$ 的近似 $100(1-\alpha)\%$ 信賴區間
> $$\hat p\pm z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}.$$

---

## 4. 近似信賴區間：p₁−p₂

[▶ 56:18](https://youtu.be/HCrObDolpWQ?t=3378) 【口頭】$p$ 是成功機率。美國研究新藥，考慮藥治好一個人的成功機率。比較兩種藥，就要找成功機率差的信賴區間。

[▶ 56:49](https://youtu.be/HCrObDolpWQ?t=3409) $Y_1\sim b(n,p_1)$、$Y_2\sim b(m,p_2)$ **獨立**。$\hat p_1=Y_1/n$，$\hat p_2=Y_2/m$。

**Step 1**（[▶ 57:51](https://youtu.be/HCrObDolpWQ?t=3471)）：各自（CLT）
$$\frac{\hat p_1-p_1}{\sqrt{p_1(1-p_1)/n}}\xrightarrow{D}N(0,1),\qquad\frac{\hat p_2-p_2}{\sqrt{p_2(1-p_2)/m}}\xrightarrow{D}N(0,1),$$
兩者獨立（$Y_1,Y_2$ 獨立，各取函數）。

**Step 2：近似常態**（[▶ 59:58](https://youtu.be/HCrObDolpWQ?t=3598)）：$X\sim N(\mu,\sigma^2)\iff\frac{X-\mu}{\sigma}\sim N(0,1)$（用 mgf 證）。所以
$$\hat p_1\ \dot\sim\ N\left(p_1,\frac{p_1(1-p_1)}{n}\right),\qquad\hat p_2\ \dot\sim\ N\left(p_2,\frac{p_2(1-p_2)}{m}\right).$$

**Step 3：相減**（[▶ 63:12](https://youtu.be/HCrObDolpWQ?t=3792)）：獨立常態相減仍常態，mean 相減、variance 相加：
$$\frac{(\hat p_1-\hat p_2)-(p_1-p_2)}{\sqrt{\frac{p_1(1-p_1)}{n}+\frac{p_2(1-p_2)}{m}}}\ \dot\sim\ N(0,1).$$

**Step 4：沒用 → 分母換成估計值**（[▶ 66:22](https://youtu.be/HCrObDolpWQ?t=3982)）：分母有 $p_1,p_2$，改寫不了。WLLN：$\hat p_1\xrightarrow{P}p_1$、$\hat p_2\xrightarrow{P}p_2$。由 Slutsky，**只換分母**（分子的 $p_1-p_2$ 不能換，換了就沒用）：
$$\frac{(\hat p_1-\hat p_2)-(p_1-p_2)}{\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}}\ \dot\sim\ N(0,1).$$

> **結果**（[▶ 72:08](https://youtu.be/HCrObDolpWQ?t=4328)）：$p_1-p_2$ 的近似 $100(1-\alpha)\%$ 信賴區間
> $$(\hat p_1-\hat p_2)\pm z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}.$$

【口頭】[▶ 72:39](https://youtu.be/HCrObDolpWQ?t=4359) 去外面考試，根號裡的東西要寫出來，不要只寫「開根號」。

---

## 5. 什麼是好的信賴區間

[▶ 73:11](https://youtu.be/HCrObDolpWQ?t=4391) 信賴區間就講到這裡。【口頭】信賴區間沒有多少理論，只用了收斂的理論就能造。

[▶ 73:42](https://youtu.be/HCrObDolpWQ?t=4422) 統計推論都要告訴人家「這個東西有多好」。好的信賴區間：同樣信心水準下，**越窄越好**。

【口頭】

- [▶ 74:12](https://youtu.be/HCrObDolpWQ?t=4452) 考完試問老師會不會及格：「成績在 30 到 80 之間，機率 95%（甚至 99%）」——區間太長，沒感覺。
- [▶ 74:45](https://youtu.be/HCrObDolpWQ?t=4485) 感冒看醫生：「吃我的藥會好的機率在 0.4 到 0.8，有 90% 把握」——喝開水大概就有 0.6，我回去就把藥丟了。「0.7 到 0.9」——比喝開水好，就會吃。

**期望長度**（[▶ 76:18](https://youtu.be/HCrObDolpWQ?t=4578)）：$(T_1,T_2)$ 是隨機的，看 $E_\theta(T_2-T_1)$，叫**期望長度**（expected length），一定和 $\theta$ 有關。

**理想**（[▶ 77:19](https://youtu.be/HCrObDolpWQ?t=4639)）：對同信心水準的**任何**信賴區間 $(T_1^*,T_2^*)$，
$$E_\theta(T_2-T_1)\le E_\theta(T_2^*-T_1^*),\qquad\forall\theta.$$
叫 **uniformly minimum expected length** 信賴區間。

[▶ 78:49](https://youtu.be/HCrObDolpWQ?t=4729) 【口頭】大約 1963、1964 年有位教授寫書證明這個**不存在**：要和所有信賴區間比，太多了。

**對照點估計**（[▶ 79:19](https://youtu.be/HCrObDolpWQ?t=4759)）：

- 點估計原本想要：所有估計量裡，**均方誤差**（mean square error）uniform 最小。這不存在。
- 所以縮小範圍到**不偏**估計量裡，比變異數，uniform 最小——就存在了（UMVUE）。
- 信賴區間也一樣：標準太高就找不到最好的；要修改、壓低標準。那些方法太理論，大學部的書不講。

---

## 6. 一頁速查表

**Slutsky**：$X_n\xrightarrow{D}X$、$Y_n\xrightarrow{P}a$ ⇒ $X_n\pm Y_n\xrightarrow{D}X\pm a$、$X_nY_n\xrightarrow{D}aX$、$X_n/Y_n\xrightarrow{D}X/a$（$a\ne 0$）。

**近似信賴區間**（技巧：CLT 得 $N(0,1)$，分母的未知參數用一致估計量取代，Slutsky 保證仍 $\xrightarrow{D}N(0,1)$）

| 參數 | 近似 $100(1-\alpha)\%$ 信賴區間 |
|---|---|
| $\mu$（分配未知） | $\bar X\pm z_{\alpha/2}\frac{S}{\sqrt n}$ |
| $p$ | $\hat p\pm z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}$ |
| $p_1-p_2$ | $(\hat p_1-\hat p_2)\pm z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n}+\frac{\hat p_2(1-\hat p_2)}{m}}$ |

關鍵：
- $S^2\xrightarrow{P}\sigma^2$（WLLN＋連續函數）。
- $\frac{\bar X-\mu}{S/\sqrt n}=\frac{\bar X-\mu}{\sigma/\sqrt n}\cdot\frac{\sigma}{S}$。
- 二項：$Y\overset{D}{=}\sum$ Bernoulli，借用 WLLN、CLT。
- 只換**分母**的未知參數，分子不能換。

**好的信賴區間**：期望長度短。uniformly minimum expected length 不存在（類比：所有估計量中 MSE uniform 最小不存在 → 改在不偏估計量中找）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Slutsky、CLT | 假設檢定的大樣本檢定統計量 |
| 信賴區間結束 | 下一主題：假設檢定 |

---

## 附：本集一句話總結

> **Slutsky 定理說依分配收斂和依機率收斂到常數的東西做加減乘除仍依分配收斂；利用它，把 CLT 得到的標準化統計量分母中的未知參數換成一致估計量（$S$、$\hat p$），就得到 $\mu$、$p$、$p_1-p_2$ 的近似信賴區間；好的信賴區間要期望長度短，但「對所有 $\theta$ 都最短」是不存在的。**

---

*筆記依據「高等統計學」Lec08 錄影逐字稿（whisper large-v3-turbo，1:21:56）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
