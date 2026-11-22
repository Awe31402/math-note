---
course: 高等統計學（數理統計續）
episode: 18
lecture: Lec18（第十週 1/2）
date: 待補
video: https://youtu.be/AlGyLvrR2X4
notes: Hogg 8th ed. §8.3 概似比檢定（p. 487–488）；§6.3 概似比檢定 $\Lambda$ 的定義（式 6.3.3）
---

# 第 18 集 · 第十週 (1/2)：概似比檢定（LRT）的定義與直覺 [▶ 影片](https://youtu.be/AlGyLvrR2X4)

← 上一集：[17](17-mlr-ump-four-cases-uniform-normal-examples.md) ｜ [總目錄](../README.md) ｜ 下一集：[19](19-lrt-examples-exponential-normal-mean.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 18 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 24 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §6.3、§8.3
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「generalized likelihood ratio」→「General Right Ligreehood Ratio」，「Neyman–Pearson」→「Lemon Pearson」，「parameter space」→「primited space」，「UMP」→「UMB」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 複習：什麼時候有 MP／UMP](#1-複習什麼時候有-mpump)
- [2. 兩個最大概似值](#2-兩個最大概似值)
- [3. 廣義概似比 Λ](#3-廣義概似比-λ)
- [4. 概似比檢定](#4-概似比檢定)
- [5. 困難：Λ 的分配](#5-困難λ-的分配)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 沒有 UMP 時的檢定：概似比檢定 | §8.3，p. 487–488 |
| $\Lambda=\frac{\max_{\Theta_0}L}{\max_\Omega L}$ | 式 (6.3.3) |

---

## 1. 複習：什麼時候有 MP／UMP

[▶ 00:31](https://youtu.be/AlGyLvrR2X4?t=31)

| 假設 | 最好的檢定 | 條件 |
|---|---|---|
| 簡單 vs 簡單 | MP | 永遠存在（Neyman–Pearson） |
| 簡單 vs 單邊複合 | UMP | 常常存在（例如指數族），不是永遠 |
| 單邊複合 vs 單邊複合 | UMP | 兩邊都是單邊 **而且** 有 MLR |

[▶ 03:36](https://youtu.be/AlGyLvrR2X4?t=216) 這些條件都沒有，就沒有 UMP。即使兩邊都是單邊，概似比沒有單調也沒有 UMP。很多情形是沒有 UMP 的，但還是要做檢定 → **概似比檢定**（likelihood ratio test）。

---

## 2. 兩個最大概似值

[▶ 04:06](https://youtu.be/AlGyLvrR2X4?t=246) $X_1,\dots,X_n$ 來自 $f(x;\theta)$，$\theta\in\Omega$（參數空間）。概似函數 $L(\theta;\mathbf x)=\prod f(x_i;\theta)$，看成 $\theta$ 的函數。

假設：
$$H_0:\theta\in\Theta_0\quad\text{vs}\quad H_1:\theta\notin\Theta_0\ \ (\theta\in\Omega\setminus\Theta_0).$$
假定沒有 UMP。

**(1) $H_0$ 上的最大概似值**（[▶ 06:14](https://youtu.be/AlGyLvrR2X4?t=374)）：
$$\max_{\theta\in\Theta_0}L(\theta;\mathbf x).$$

[▶ 06:44](https://youtu.be/AlGyLvrR2X4?t=404) 一般**不能**直接取 log、微分等於 0：微分等於 0 解出的點可能不在 $\Theta_0$ 裡。要去判斷函數的形狀（例如在 $\Theta_0$ 上遞增，最大就在端點）。通常比較麻煩。

**(2) 整個參數空間的最大概似值**（[▶ 07:48](https://youtu.be/AlGyLvrR2X4?t=468)）：不找 $H_1$ 上的最大（也很麻煩），而是找整個 $\Omega$ 上的最大——那就是 **MLE**：
$$\max_{\theta\in\Omega}L(\theta;\mathbf x)=L(\hat\theta_{\text{MLE}};\mathbf x).$$

**大小關係**（[▶ 08:49](https://youtu.be/AlGyLvrR2X4?t=529)）：範圍大的最大一定比較大，
$$\max_{\Theta_0}L\le\max_\Omega L.$$

【口頭】全班最後一名的成績一定 $\le$ 某一排最後一名；全班第一名一定 $\ge$ 某一排第一名。找最小，範圍越大越小；找最大，範圍越大越大。（老師一開始寫反了不等號，馬上改正。）

---

## 3. 廣義概似比 Λ

> **定義**（[▶ 12:58](https://youtu.be/AlGyLvrR2X4?t=778)）：
> $$\Lambda(x_1,\dots,x_n)=\frac{\max_{\theta\in\Theta_0}L(\theta;\mathbf x)}{\max_{\theta\in\Omega}L(\theta;\mathbf x)}=\frac{\max_{\theta\in\Theta_0}L(\theta;\mathbf x)}{L(\hat\theta_{\text{MLE}};\mathbf x)}$$
> 叫**廣義概似比**（generalized likelihood ratio）。

- [▶ 13:29](https://youtu.be/AlGyLvrR2X4?t=809) 取了最大，$\theta$ 就不見了，$\Lambda$ 只是 $x_1,\dots,x_n$ 的函數。
- [▶ 13:59](https://youtu.be/AlGyLvrR2X4?t=839) 分子、分母都是正的，分母比較大：
$$0\le\Lambda\le 1.$$

**直覺**（[▶ 10:23](https://youtu.be/AlGyLvrR2X4?t=623)）：概似值想成「$\theta$ 為真時發生 $\mathbf x$ 的機率」，而 $\mathbf x$ 已經發生了。

| $\Lambda$ | 意思 | 決定 |
|---|---|---|
| 接近 1 | $H_0$ 上的最大和全部的最大差不多：$H_0$ 讓它發生的機會和整體一樣大 | 相信 $H_0$ |
| 很小 | $H_0$ 上的 $\theta$ 讓已經發生的 $\mathbf x$ 發生的機率很小 | 拒絕 $H_0$ |

---

## 4. 概似比檢定

> **定義（概似比檢定，LRT）**（[▶ 15:31](https://youtu.be/AlGyLvrR2X4?t=931)）：拒絕域
> $$C=\left\{\mathbf x:\Lambda(\mathbf x)\le\lambda_0\right\},$$
> $\lambda_0$ 由 size 決定：
> $$\alpha=\max_{\theta\in\Theta_0}P_\theta\left(\Lambda(X_1,\dots,X_n)\le\lambda_0\right).$$

- 寫機率時 $X_i$ 要大寫，才是隨機變數。
- [▶ 16:31](https://youtu.be/AlGyLvrR2X4?t=991) $H_0$ 是複合的，有很多點；型一錯誤機率的最大值就是 size，要剛好等於 $\alpha$。
- [▶ 23:43](https://youtu.be/AlGyLvrR2X4?t=1423) LRT 不保證是最好的檢定，就是一個方法。

---

## 5. 困難：Λ 的分配

[▶ 18:33](https://youtu.be/AlGyLvrR2X4?t=1113) 要找 $\lambda_0$，需要 $\Lambda$ 的分配：若知道它的 pdf $f_\Lambda(\lambda;\theta)$，
$$\alpha=\max_{\theta\in\Theta_0}\int_{-\infty}^{\lambda_0}f_\Lambda(\lambda;\theta)\,d\lambda.$$
但 $\Lambda$ 的分配**通常拿不到**（not available）。

**轉換**（[▶ 21:07](https://youtu.be/AlGyLvrR2X4?t=1267)）：某些情形（不是所有）存在統計量 $T=T(X_1,\dots,X_n)$，使
$$\Lambda\le\lambda_0\iff T\le k\ \ (\text{或}\ T\ge k,\ \text{只有一個成立}).$$
兩個不等式成立的 $\mathbf x$ 完全一樣 ⇒ 同一個拒絕域。選 **分配已知**的 $T$，就能用
$$\alpha=\max_{\theta\in\Theta_0}P_\theta(T\le k)$$
找 $k$。

[▶ 23:11](https://youtu.be/AlGyLvrR2X4?t=1391) LRT 的兩個困難：

1. 分子在 $H_0$ 上的最大值有時很難找；
2. 轉換到分配已知的 $T$ 有時也很難。

例題下次講。

---

## 6. 一頁速查表

**沒有 UMP 時** → 概似比檢定。

$$\Lambda=\frac{\max_{\theta\in\Theta_0}L(\theta)}{\max_{\theta\in\Omega}L(\theta)}=\frac{\max_{\Theta_0}L}{L(\hat\theta_{\text{MLE}})},\qquad 0\le\Lambda\le 1.$$

- 分子：$H_0$ 上的最大，**不能**直接微分等於 0（解可能不在 $\Theta_0$）。
- 分母：整個參數空間的最大＝代入 MLE。
- $\Lambda$ 小 ⇒ 拒絕 $H_0$：$C=\{\Lambda\le\lambda_0\}$，$\max_{\Theta_0}P_\theta(\Lambda\le\lambda_0)=\alpha$。
- 實作：把 $\Lambda\le\lambda_0$ 一對一轉成分配已知的 $T\le k$ 或 $T\ge k$。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| LRT 定義 | 下一集：LRT 例題（常態平均數等） |
| 轉換到已知分配 | $t$ 檢定、$\chi^2$ 檢定、$F$ 檢定 |

---

## 附：本集一句話總結

> **沒有 UMP 時用概似比檢定：$\Lambda$＝$H_0$ 上的最大概似值 ÷ 整個參數空間的最大概似值（代 MLE），介於 0 和 1；$\Lambda$ 小代表 $H_0$ 很難產生已觀察到的資料，就拒絕 $H_0$，臨界值由 size $=\alpha$ 決定，實作上把 $\Lambda\le\lambda_0$ 轉成分配已知的統計量的不等式。**

---

*筆記依據「高等統計學」Lec18 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
