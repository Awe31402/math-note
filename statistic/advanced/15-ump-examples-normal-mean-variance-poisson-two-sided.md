---
course: 高等統計學（數理統計續）
episode: 15
lecture: Lec15（第八週 2/2）
date: 待補
video: https://youtu.be/iuMdD_j9kFY
notes: Hogg 8th ed. §8.2 UMP 檢定；Example 8.2.2 N(0,θ) 變異數（p. 480）；Example 8.2.3 雙邊無 UMP（p. 481）
---

# 第 15 集 · 第八週 (2/2)：UMP 的例子——常態平均數、常態變異數；雙邊 Poisson 沒有 UMP；四種假設的整理 [▶ 影片](https://youtu.be/iuMdD_j9kFY)

← 上一集：[14](14-poisson-mp-test-ump-definition.md) ｜ [總目錄](../README.md) ｜ 下一集：[16](16-ump-composite-definition-monotone-likelihood-ratio.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 15 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 1:09:30，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §8.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚的地方

> ⚠️ 逐字稿缺字（整集通用）：「Poisson」→「普拉松／滑鬆」，「Neyman–Pearson」→「Lemon／Naman／雷門皮爾森」，「one-sided／two-sided」照錄（老師說「單維／單位」＝單尾、「雙圍」＝雙尾），「$\chi^2$」→「卡方」，「$\lambda_0$」→「辣馬零／Lm0」。[▶ 66:54](https://youtu.be/iuMdD_j9kFY?t=4014)–[▶ 67:24](https://youtu.be/iuMdD_j9kFY?t=4044) 是幻聽廣告詞，忽略。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 類比：連續函數](#1-類比連續函數)
- [2. 找 UMP 的步驟](#2-找-ump-的步驟)
- [3. 什麼時候 UMP 存在](#3-什麼時候-ump-存在)
- [4. 例一：N(μ,1)，H₀:μ=0 vs H₁:μ>0](#4-例一nμ1h₀μ0-vs-h₁μ0)
- [5. 例二：N(0,σ²)，H₀:σ²=1 vs H₁:σ²<1](#5-例二n0σ²h₀σ²1-vs-h₁σ²1)
- [6. 例三：Poisson，H₀:λ=1 vs H₁:λ≠1（UMP 不存在）](#6-例三poissonh₀λ1-vs-h₁λ1ump-不存在)
- [7. 整理：四種假設](#7-整理四種假設)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| UMP 的找法與存在性 | §8.2 |
| $N(\mu,1)$ 單邊 | §8.2（類似 Example 8.1.2） |
| $N(0,\sigma^2)$ 變異數 | Example 8.2.2，p. 480 |
| 雙邊沒有 UMP | Example 8.2.3（常態）；課堂用 Poisson |

---

## 1. 類比：連續函數

[▶ 00:00](https://youtu.be/iuMdD_j9kFY?t=0) 用微積分想：

- $f$ 在 $x_0$ 連續：$\lim_{x\to x_0}f(x)=f(x_0)$（極限值等於函數值；左右極限相等極限才存在）。
- $f$ 在集合 $A$ 上連續：$A$ 的**每一點**都連續。

[▶ 02:38](https://youtu.be/iuMdD_j9kFY?t=158) UMP 也一樣：$H_0:\theta=\theta_0$（簡單），$H_1$ 是集合（像 $A$）。對 $H_1$ 的每一點 $\theta_1$ 做簡單對簡單，都有最強力拒絕域（Neyman–Pearson）；如果它們**全都一樣**，那就是 UMP。

（[▶ 03:09](https://youtu.be/iuMdD_j9kFY?t=189) 老師口誤說「一定有 UMP test」，接著改說 most powerful。）

[▶ 08:54](https://youtu.be/iuMdD_j9kFY?t=534) 要說函數不連續比較好證：找到一點不連續就好。要說 UMP 不存在也是：找到兩點的最強力拒絕域不一樣就好。

---

## 2. 找 UMP 的步驟

[▶ 05:15](https://youtu.be/iuMdD_j9kFY?t=315)

1. 在 $H_1$ 裡**隨便取一點** $\theta_1$——用符號，不能代特定的數（只算 $\mu=1$、$\mu=2$，那 $\mu=1.5$ 怎麼辦？）。
2. 對 $H_0:\theta_0$ vs $H_1:\theta_1$，用 Neyman–Pearson：$\frac{L(\theta_0)}{L(\theta_1)}\le k_{\theta_1}$（$k$ 可能依賴 $\theta_1$）。
3. 一對一轉換成 $T(\mathbf x)\le c_{\theta_1}$ 或 $\ge c_{\theta_1}$（只能有一種）。
4. 檢查：**不等式方向**、**統計量 $T$**、**常數 $c$** 是否與 $\theta_1$ 無關。全都一樣 ⇒ $C$ 是 UMP 拒絕域。

【口頭】[▶ 10:57](https://youtu.be/iuMdD_j9kFY?t=657) 做一兩個題目就覺得都會了，學做題目很容易。但做的過程要思考你到底在幹什麼：有沒有發覺對立假設不管取哪一點，找到的都一模一樣。

---

## 3. 什麼時候 UMP 存在

[▶ 09:25](https://youtu.be/iuMdD_j9kFY?t=565)

| 假設 | 名稱 | UMP |
|---|---|---|
| $H_0:\theta=\theta_0$ vs $H_1:\theta>\theta_0$（或 $<$） | 單邊（one-sided） | 經常存在 |
| $H_0:\theta=\theta_0$ vs $H_1:\theta\ne\theta_0$ | 雙邊（two-sided） | 通常不存在 |

---

## 4. 例一：N(μ,1)，H₀:μ=0 vs H₁:μ>0

[▶ 11:28](https://youtu.be/iuMdD_j9kFY?t=688) $X_1,\dots,X_n$ iid $N(\mu,1)$。單邊。

**取一點**（[▶ 12:30](https://youtu.be/iuMdD_j9kFY?t=750)）：$\mu_1>0$，考慮 $H_0:\mu=0$ vs $H_1:\mu=\mu_1$。

**概似函數**（[▶ 14:33](https://youtu.be/iuMdD_j9kFY?t=873)）：
$$L(\mu;\mathbf x)=(2\pi)^{-n/2}\exp\left\{-\frac12\sum(x_i-\mu)^2\right\}.$$

**概似比**（[▶ 15:33](https://youtu.be/iuMdD_j9kFY?t=933)）：$(2\pi)^{-n/2}$ 消掉，分母展開，$\sum x_i^2$ 消掉：
$$\frac{L(0;\mathbf x)}{L(\mu_1;\mathbf x)}=\exp\left\{-\mu_1\sum x_i+\frac{n\mu_1^2}{2}\right\}\le k.$$

[▶ 16:05](https://youtu.be/iuMdD_j9kFY?t=965) 看起來 $k$ 跟 $\mu_1$ 有關。

**轉換**（[▶ 16:36](https://youtu.be/iuMdD_j9kFY?t=996)）：取 $\log$、移項：
$$-\mu_1\sum x_i\le\log k-\frac{n\mu_1^2}{2}.$$
除以 $-\mu_1$：因為 $\mu_1>0$，$-\mu_1<0$，**不等號反向**——而且不管 $\mu_1$ 取哪一點都反向：
$$\sum x_i\ge c\quad\Longleftrightarrow\quad\bar x\ge c^*.$$

[▶ 18:09](https://youtu.be/iuMdD_j9kFY?t=1089) 不等式方向一樣、統計量一樣，只剩 $c$ 要檢查。

**找 $c$**（[▶ 19:40](https://youtu.be/iuMdD_j9kFY?t=1180)）：$H_0$ 為真時 $\bar X\sim N\left(0,\frac1n\right)$，$\sqrt n\bar X\sim N(0,1)$：
$$\alpha=P_{\mu=0}(\bar X\ge c^*)=P(Z\ge\sqrt nc^*)\ \Rightarrow\ c^*=\frac{z_\alpha}{\sqrt n}.$$

⚠️ 逐字稿缺字：[▶ 23:21](https://youtu.be/iuMdD_j9kFY?t=1401)–[▶ 25:59](https://youtu.be/iuMdD_j9kFY?t=1559) 老師在 $n\bar x$ 和 $\sqrt n\bar x$ 之間弄混、改了好幾次，最後說「轉成 $\bar x\ge c^*$ 比較不會錯」，結論 $\sqrt n\bar x\ge z_\alpha$。上面寫的是整理後的正確版。

**結論**（[▶ 26:29](https://youtu.be/iuMdD_j9kFY?t=1589)）：$z_\alpha$ 跟 $\mu_1$ 無關。對每一個 $\mu_1>0$，
$$C=\left\{\mathbf x:\sqrt n\bar x\ge z_\alpha\right\}$$
都是最強力拒絕域 ⇒ $C$ 是 $H_0:\mu=0$ vs $H_1:\mu>0$ 的 size $\alpha$ **UMP 拒絕域**。

---

## 5. 例二：N(0,σ²)，H₀:σ²=1 vs H₁:σ²<1

[▶ 28:07](https://youtu.be/iuMdD_j9kFY?t=1687)（課本 Example 8.2.2 是同類型）$X_1,\dots,X_n$ iid $N(0,\sigma^2)$，平均數已知為 0。
$$H_0:\sigma^2=1\quad\text{vs}\quad H_1:\sigma^2<1\ \ (\text{單邊}).$$

**取一點**（[▶ 29:41](https://youtu.be/iuMdD_j9kFY?t=1781)）：$\theta<1$，考慮 $H_1:\sigma^2=\theta$。

**概似函數**（[▶ 31:43](https://youtu.be/iuMdD_j9kFY?t=1903)）：
$$L(\sigma^2;\mathbf x)=(2\pi)^{-n/2}(\sigma^2)^{-n/2}\exp\left\{-\frac{1}{2\sigma^2}\sum x_i^2\right\}.$$

**概似比**（[▶ 32:50](https://youtu.be/iuMdD_j9kFY?t=1970)）：
$$\frac{L(1;\mathbf x)}{L(\theta;\mathbf x)}=\theta^{n/2}\exp\left\{-\frac12\left(1-\frac1\theta\right)\sum x_i^2\right\}\le k.$$

[▶ 34:23](https://youtu.be/iuMdD_j9kFY?t=2063) 這個量的分配不知道 → 一對一轉換。

**轉換**（[▶ 35:33](https://youtu.be/iuMdD_j9kFY?t=2133)）：$\theta$ 是常數，除以 $\theta^{n/2}$、取 $\log$：
$$-\frac12\left(1-\frac1\theta\right)\sum x_i^2\le\log\frac{k}{\theta^{n/2}}.$$
[▶ 36:05](https://youtu.be/iuMdD_j9kFY?t=2165) $\theta<1$ ⇒ $\frac1\theta>1$ ⇒ $1-\frac1\theta<0$ ⇒ $-\frac12\left(1-\frac1\theta\right)>0$。不管取哪個 $\theta<1$ 都是正的，除過去**不等號不變**：
$$\sum x_i^2\le c.$$

[▶ 37:41](https://youtu.be/iuMdD_j9kFY?t=2261) 不等式方向、統計量 $\sum x_i^2$ 都一樣，只剩 $c$。

**找 $c$**（[▶ 38:41](https://youtu.be/iuMdD_j9kFY?t=2321)）：

- $X_i/\sigma$ iid $N(0,1)$（減平均數 0、除標準差；同一個函數，仍 iid）。
- [▶ 40:42](https://youtu.be/iuMdD_j9kFY?t=2442) 平方是 $\chi^2(1)$，$n$ 個獨立相加是 $\chi^2(n)$。
- $H_0$ 為真時 $\sigma^2=1$ ⇒ $\sum X_i^2\sim\chi^2(n)$。

$$\alpha=P_{\sigma^2=1}\left(\sum X_i^2\le c\right)=P(\chi^2(n)\le c).$$
$c$ 就是 $\chi^2(n)$ 左尾機率為 $\alpha$ 的點（老師記為「卡方 $\alpha$」）。

**結論**（[▶ 42:48](https://youtu.be/iuMdD_j9kFY?t=2568)）：$c$ 與 $\theta$ 無關。對每一個 $\theta<1$ 最強力拒絕域都是
$$C=\left\{\mathbf x:\sum x_i^2\le c\right\},\qquad P(\chi^2(n)\le c)=\alpha,$$
所以它是 size $\alpha$ 的 UMP 拒絕域。

⚠️ 待確認：[▶ 44:24](https://youtu.be/iuMdD_j9kFY?t=2664) 老師收尾時說「我們真正關心的是 $H_1:\sigma^2>1$」，和前面整段推導用的 $\sigma^2<1$ 矛盾。依推導（$1-\frac1\theta<0$ 才得到 $\le c$）應是 $\sigma^2<1$，判斷是口誤。

---

## 6. 例三：Poisson，H₀:λ=1 vs H₁:λ≠1（UMP 不存在）

[▶ 46:50](https://youtu.be/iuMdD_j9kFY?t=2810) $X_1,\dots,X_n$ iid Poisson$(\lambda)$。雙邊，通常不存在；證明它不存在。

**取一點**（[▶ 47:59](https://youtu.be/iuMdD_j9kFY?t=2879)）：$\lambda_0\ne 1$（可能比 1 大也可能比 1 小），考慮 $H_0:\lambda=1$ vs $H_1:\lambda=\lambda_0$。

**概似函數**（[▶ 49:03](https://youtu.be/iuMdD_j9kFY?t=2943)）：
$$L(\lambda;\mathbf x)=\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}.$$

**概似比**（[▶ 50:34](https://youtu.be/iuMdD_j9kFY?t=3034)）：$\prod x_i!$ 消掉，
$$\frac{L(1;\mathbf x)}{L(\lambda_0;\mathbf x)}=\frac{e^{-n}}{\lambda_0^{\sum x_i}e^{-n\lambda_0}}\le k\iff\lambda_0^{\sum x_i}\ge\frac{e^{-n}}{k\,e^{-n\lambda_0}}.$$

取 $\log$（[▶ 53:15](https://youtu.be/iuMdD_j9kFY?t=3195)）：
$$-\left(\sum x_i\right)\log\lambda_0\le\log\left(k\,e^{n}e^{-n\lambda_0}\right).$$

[▶ 53:46](https://youtu.be/iuMdD_j9kFY?t=3226) 要除以 $-\log\lambda_0$，它的正負**取決於** $\lambda_0$：

| | $-\log\lambda_0$ | 最強力拒絕域 |
|---|---|---|
| $\lambda_0>1$ | $<0$，不等號反向 | $\sum x_i\ge c_1$ |
| $\lambda_0<1$ | $>0$，不等號不變 | $\sum x_i\le c_2$ |

[▶ 58:01](https://youtu.be/iuMdD_j9kFY?t=3481) 不用管 $c_1$、$c_2$ 相不相等：**不等式方向已經不同**，兩個拒絕域不一樣。

**結論**（[▶ 59:15](https://youtu.be/iuMdD_j9kFY?t=3555)）：存在 $\lambda_0>1$ 和 $\lambda_0<1$ 使最強力拒絕域不同 ⇒ **UMP 拒絕域不存在**。

[▶ 59:50](https://youtu.be/iuMdD_j9kFY?t=3590) 要證不存在，只要在 $H_1$ 找兩點、驗證它們的最強力拒絕域不一樣。【口頭】這種也要會證，通常大家比較不注意。

---

## 7. 整理：四種假設

[▶ 61:12](https://youtu.be/iuMdD_j9kFY?t=3672) 要搞清楚哪一種假設才有哪一種檢定。（老師說「五種狀況」，實際列了四種。）

| | 假設 | 最好的檢定 |
|---|---|---|
| 1 | $H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$（簡單 vs 簡單） | MP **永遠存在**（Neyman–Pearson） |
| 2 | $H_0:\theta=\theta_0$ vs $H_1:\theta>\theta_0$（或 $<$） | UMP **在某些分配存在** |
| 3 | $H_0:\theta=\theta_0$ vs $H_1:\theta\ne\theta_0$（雙邊） | UMP **通常不存在** |
| 4 | $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$（或 $\ge$ vs $<$）：兩邊都是複合、但都是單邊 | UMP **在某些特別的分配存在**；要**重新定義** UMP |

[▶ 68:36](https://youtu.be/iuMdD_j9kFY?t=4116) 第 4 種：**等號一定放在 $H_0$**，$H_1$ 一定沒有等號。下一次討論。

---

## 8. 一頁速查表

**找 UMP**：$H_1$ 任取一點（符號）→ Neyman–Pearson → 轉成 $T(\mathbf x)\le c$ 或 $\ge c$ → 檢查方向、$T$、$c$ 都與該點無關。

**證明 UMP 不存在**：$H_1$ 找兩點，最強力拒絕域不同即可。

| 例 | 概似比 | 轉換關鍵 | UMP 拒絕域 |
|---|---|---|---|
| $N(\mu,1)$，$\mu=0$ vs $\mu>0$ | $e^{-\mu_1\sum x_i+n\mu_1^2/2}$ | $-\mu_1<0$ | $\sqrt n\bar x\ge z_\alpha$ |
| $N(0,\sigma^2)$，$\sigma^2=1$ vs $\sigma^2<1$ | $\theta^{n/2}e^{-\frac12(1-\frac1\theta)\sum x_i^2}$ | $-\frac12(1-\frac1\theta)>0$ | $\sum x_i^2\le c$，$P(\chi^2(n)\le c)=\alpha$ |
| Poisson，$\lambda=1$ vs $\lambda\ne 1$ | $\frac{e^{-n}}{\lambda_0^{\sum x_i}e^{-n\lambda_0}}$ | $-\log\lambda_0$ 正負隨 $\lambda_0$ 變 | **不存在**（$\ge c_1$ vs $\le c_2$） |

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 第 4 種假設（兩邊複合、單邊） | 下一集：重新定義 UMP；單調概似比 |
| 雙邊沒有 UMP | 不偏檢定、概似比檢定 |

---

## 附：本集一句話總結

> **UMP 就像「在集合上連續＝每點都連續」：對 $H_1$ 每一點做 Neyman–Pearson，若轉換後的不等式方向、統計量、臨界值都與該點無關就是 UMP——$N(\mu,1)$ 單邊得 $\sqrt n\bar x\ge z_\alpha$、$N(0,\sigma^2)$ 單邊得 $\sum x_i^2\le\chi^2$ 左尾點；Poisson 雙邊時 $\lambda_0>1$ 和 $<1$ 給出方向相反的拒絕域，所以 UMP 不存在。**

---

## ⚠️ 待確認清單

1. [▶ 44:24](https://youtu.be/iuMdD_j9kFY?t=2664) 變異數例的對立假設：推導用 $\sigma^2<1$，收尾時說 $\sigma^2>1$。判斷是口誤，待確認。

---

*筆記依據「高等統計學」Lec15 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
