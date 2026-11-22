---
course: 高等統計學（數理統計續）
episode: 22
lecture: Lec22（第十二週 1/2）
date: 待補
video: https://youtu.be/QohgVwzLzGw
notes: Hogg 8th ed. §8.3.2 常態變異數的 LRT（兩變異數相等）
---

# 第 22 集 · 第十二週 (1/2)：兩變異數相等的檢定就是概似比檢定（推導） [▶ 影片](https://youtu.be/QohgVwzLzGw)

← 上一集：[21](21-f-table-variance-ratio-ci-test.md) ｜ [總目錄](../README.md) ｜ 下一集：[23](23-two-sample-means-proportion-test-summary.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 22 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 28 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §8.3.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「概似比」→「概釋比」，「variance」→「Valence／變因素」，「F test」→「app test」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 概似函數](#1-概似函數)
- [2. 分子：H₀ 下的最大](#2-分子h₀-下的最大)
- [3. 分母：整個參數空間的最大](#3-分母整個參數空間的最大)
- [4. Λ 與轉換](#4-λ-與轉換)
- [5. Λ 不是單調：兩邊都拒絕](#5-λ-不是單調兩邊都拒絕)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/QohgVwzLzGw?t=0) $X_1,\dots,X_n$ iid $N(\mu_x,\sigma_x^2)$；$Y_1,\dots,Y_m$ iid $N(\mu_y,\sigma_y^2)$；兩組獨立；四個參數都未知。
$$H_0:\sigma_x^2=\sigma_y^2\quad\text{vs}\quad H_1:\sigma_x^2\ne\sigma_y^2.$$
用概似比檢定，證明它就是上一集的 F 檢定。

| 主題 | 課本 |
|---|---|
| 兩變異數相等的 LRT | §8.3.2 |

---

## 1. 概似函數

[▶ 02:41](https://youtu.be/QohgVwzLzGw?t=161) 概似函數＝全部 $n+m$ 個隨機變數的 joint pdf。每組是隨機樣本（pdf 相乘），兩組獨立（再相乘）：
$$L(\mu_x,\mu_y,\sigma_x^2,\sigma_y^2)=(2\pi)^{-\frac{n+m}{2}}(\sigma_x^2)^{-\frac n2}(\sigma_y^2)^{-\frac m2}\exp\left\{-\frac{\sum(x_i-\mu_x)^2}{2\sigma_x^2}-\frac{\sum(y_j-\mu_y)^2}{2\sigma_y^2}\right\}.$$

記 $A=\sum(x_i-\bar x)^2$，$B=\sum(y_j-\bar y)^2$。

---

## 2. 分子：H₀ 下的最大

[▶ 06:21](https://youtu.be/QohgVwzLzGw?t=381) $H_0$ 為真：$\sigma_x^2=\sigma_y^2=\sigma^2$，
$$L_0=(2\pi)^{-\frac{n+m}{2}}(\sigma^2)^{-\frac{n+m}{2}}\exp\left\{-\frac{1}{2\sigma^2}\left[\sum(x_i-\mu_x)^2+\sum(y_j-\mu_y)^2\right]\right\}.$$
三個參數 $\mu_x,\mu_y,\sigma^2$ 求最大。

[▶ 07:54](https://youtu.be/QohgVwzLzGw?t=474) 取 log 微分：

- 對 $\mu_x$：$\frac{1}{\sigma^2}\sum(x_i-\mu_x)=0$ ⇒ $\hat\mu_x=\bar x$。
- 對 $\mu_y$：$\hat\mu_y=\bar y$。
- [▶ 08:58](https://youtu.be/QohgVwzLzGw?t=538) 代入後對 $\sigma^2$：
$$-\frac{n+m}{2\sigma^2}+\frac{A+B}{2\sigma^4}=0\ \Rightarrow\ \hat\sigma^2=\frac{A+B}{n+m}.$$

**代回**（[▶ 11:03](https://youtu.be/QohgVwzLzGw?t=663)）：指數裡 $\frac{A+B}{2\hat\sigma^2}=\frac{n+m}{2}$，最麻煩的一項變最簡單：
$$\max_{\Theta_0}L=(2\pi)^{-\frac{n+m}{2}}\left(\frac{A+B}{n+m}\right)^{-\frac{n+m}{2}}e^{-\frac{n+m}{2}}.$$

---

## 3. 分母：整個參數空間的最大

[▶ 13:39](https://youtu.be/QohgVwzLzGw?t=819) 沒有限制，四個參數都微分等於 0：

- $\hat\mu_x=\bar x$，$\hat\mu_y=\bar y$；
- [▶ 15:42](https://youtu.be/QohgVwzLzGw?t=942) 對 $\sigma_x^2$（先把 $\mu_x$ 換成 $\bar x$）：$\hat\sigma_x^2=\frac An$；
- [▶ 16:12](https://youtu.be/QohgVwzLzGw?t=972) 對 $\sigma_y^2$：$\hat\sigma_y^2=\frac Bm$。

**代回**（[▶ 16:42](https://youtu.be/QohgVwzLzGw?t=1002)）：兩個指數項分別變成 $-\frac n2$、$-\frac m2$，合併成 $e^{-\frac{n+m}{2}}$：
$$\max_\Omega L=(2\pi)^{-\frac{n+m}{2}}\left(\frac An\right)^{-\frac n2}\left(\frac Bm\right)^{-\frac m2}e^{-\frac{n+m}{2}}.$$

---

## 4. Λ 與轉換

[▶ 18:45](https://youtu.be/QohgVwzLzGw?t=1125) $(2\pi)^{-\frac{n+m}{2}}$、$e^{-\frac{n+m}{2}}$ 消掉：
$$\Lambda=\frac{(n+m)^{\frac{n+m}{2}}}{n^{\frac n2}m^{\frac m2}}\cdot\frac{A^{\frac n2}B^{\frac m2}}{(A+B)^{\frac{n+m}{2}}}.$$

[▶ 21:18](https://youtu.be/QohgVwzLzGw?t=1278) 沒辦法再簡化，令 $\Lambda\le\lambda_0$。

**目標**（[▶ 21:51](https://youtu.be/QohgVwzLzGw?t=1311)）：上一集的 F 檢定用的是
$$\frac{s_y^2}{s_x^2}=\frac{B/(m-1)}{A/(n-1)},$$
所以要想辦法化成 $\frac BA$ 的函數。

**拆開**（[▶ 22:22](https://youtu.be/QohgVwzLzGw?t=1342)）：$(A+B)^{\frac{n+m}{2}}=(A+B)^{\frac n2}(A+B)^{\frac m2}$，
$$\frac{A^{\frac n2}B^{\frac m2}}{(A+B)^{\frac{n+m}{2}}}=\left(\frac{A}{A+B}\right)^{\frac n2}\left(\frac{B}{A+B}\right)^{\frac m2}=\left(\frac{1}{1+\frac BA}\right)^{\frac n2}\left(\frac{1}{1+\frac AB}\right)^{\frac m2}.$$

令 $x=\frac BA>0$（[▶ 24:26](https://youtu.be/QohgVwzLzGw?t=1466)）：
$$\Lambda=\text{常數}\times g(x),\qquad g(x)=\frac{1}{(1+x)^{n/2}\left(1+\frac1x\right)^{m/2}}.$$

⚠️ 逐字稿缺字：[▶ 24:26](https://youtu.be/QohgVwzLzGw?t=1466) 老師口述的指數對應（哪個配 $n$、哪個配 $m$）聽不清楚；上式是依 $\Lambda$ 的式子重新推的，結構和老師的一樣。

---

## 5. Λ 不是單調：兩邊都拒絕

[▶ 23:55](https://youtu.be/QohgVwzLzGw?t=1435) 以前會取 log 做一對一轉換，得到「某統計量大於或小於」。這裡 $g(x)$ **不是單調**的：

- [▶ 25:26](https://youtu.be/QohgVwzLzGw?t=1526) $x\to\infty$：$(1+x)^{n/2}\to\infty$，$g\to 0$。
- [▶ 25:56](https://youtu.be/QohgVwzLzGw?t=1556) $x\to 0^+$：$\left(1+\frac1x\right)^{m/2}\to\infty$，$g\to 0$。

$x=B/A$ 是平方和的比，永遠是正的。$\Lambda$ 小 ⇔ $x$ **很小或很大**：
$$\frac BA\le c_1\quad\text{或}\quad\frac BA\ge c_2.$$

[▶ 26:57](https://youtu.be/QohgVwzLzGw?t=1617) 乘上常數 $\frac{n-1}{m-1}$ 變成 $\frac{s_y^2}{s_x^2}\sim F(m-1,n-1)$（$H_0$ 下）。取左右各 $\frac\alpha2$：
$$\frac{s_y^2}{s_x^2}\le F_{\alpha/2}(m-1,n-1)=\frac{1}{F_{1-\alpha/2}(n-1,m-1)}\quad\text{或}\quad\frac{s_y^2}{s_x^2}\ge F_{1-\alpha/2}(m-1,n-1).$$

> **結論**（[▶ 27:27](https://youtu.be/QohgVwzLzGw?t=1647)）：上一集的 F 檢定就是概似比檢定。

以下**不是逐字稿內容**，是依 LRT 的定義推論的：嚴格說，LRT 的兩個臨界值要滿足 $g(c_1)=g(c_2)$，不一定剛好左右各 $\frac\alpha2$；左右各 $\frac\alpha2$ 是實務上常用的版本。課堂直接取左右各 $\frac\alpha2$。

【口頭】[▶ 27:58](https://youtu.be/QohgVwzLzGw?t=1678) 證明過程相當麻煩，所以有時候不見得都要證明它是什麼檢定；告訴你它就是 LRT。

---

## 6. 一頁速查表

**設定**：兩獨立常態樣本，$A=\sum(x_i-\bar x)^2$，$B=\sum(y_j-\bar y)^2$。

| | MLE | 最大概似值（去掉共同因子 $(2\pi)^{-\frac{n+m}{2}}e^{-\frac{n+m}{2}}$） |
|---|---|---|
| $H_0$（$\sigma_x^2=\sigma_y^2$） | $\bar x,\bar y,\ \hat\sigma^2=\frac{A+B}{n+m}$ | $\left(\frac{A+B}{n+m}\right)^{-\frac{n+m}{2}}$ |
| $\Omega$ | $\bar x,\bar y,\ \frac An,\ \frac Bm$ | $\left(\frac An\right)^{-\frac n2}\left(\frac Bm\right)^{-\frac m2}$ |

$$\Lambda=\frac{(n+m)^{\frac{n+m}{2}}}{n^{\frac n2}m^{\frac m2}}\left(\frac{1}{1+\frac BA}\right)^{\frac n2}\left(\frac{1}{1+\frac AB}\right)^{\frac m2}.$$

關鍵：$\Lambda$ 是 $x=B/A$ 的函數，$x\to 0^+$ 或 $x\to\infty$ 時 $\Lambda\to 0$ ⇒ 雙邊拒絕 ⇒ F 檢定：
$$\frac{s_y^2}{s_x^2}\le\frac{1}{F_{1-\alpha/2}(n-1,m-1)}\ \text{或}\ \ge F_{1-\alpha/2}(m-1,n-1).$$

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 變異數相等 | 兩樣本 $t$ 檢定、ANOVA |
| LRT 推導技巧 | 之後的檢定 |

---

## 附：本集一句話總結

> **兩獨立常態樣本檢定變異數相等的 LRT：$H_0$ 下 $\hat\sigma^2=(A+B)/(n+m)$、無限制時 $\hat\sigma_x^2=A/n$、$\hat\sigma_y^2=B/m$，相除後 $\Lambda$ 是 $B/A$ 的函數，在 $B/A\to 0$ 或 $\infty$ 時都趨近 0，所以 $s_y^2/s_x^2$ 太小或太大都拒絕——正是上一集的 F 檢定。**

---

*筆記依據「高等統計學」Lec22 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
