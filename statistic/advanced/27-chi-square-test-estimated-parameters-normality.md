---
course: 高等統計學（數理統計續）
episode: 27
lecture: Lec27（第十四週 2/2，最後一集）
date: 待補
video: https://youtu.be/kIN-VV1G7E4
notes: Hogg 8th ed. §4.7 卡方檢定——參數未知、用 MLE 估計時自由度減 p（p. 286 附近）
---

# 第 27 集 · 第十四週 (2/2)：統計推論總整理；參數需估計時的卡方檢定（自由度 k−p−1）；例：檢定常態性 [▶ 影片](https://youtu.be/kIN-VV1G7E4)

← 上一集：[26](26-pearson-chi-square-test-mendel-example.md) ｜ [總目錄](../README.md) ｜ 本課程最後一集

> **課程**：高等統計學（接續上學期「統計學」）— 第 27 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 31 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.7
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「statistical inference」→「statistical influence」，「派別」→「派北」，「值域」→「植域／執語」，「follow」→「虎從」，「信賴區間」→「信奈區間／期間」，「Poisson」→「普華松／普拉松」，「二項」→「歐洲」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 統計推論在做什麼：總整理](#1-統計推論在做什麼總整理)
- [2. 為什麼要檢定分配](#2-為什麼要檢定分配)
- [3. 兩種情形](#3-兩種情形)
- [4. 參數未知：用 MLE，自由度減 p](#4-參數未知用-mle自由度減-p)
- [5. 例：檢定資料是否來自常態](#5-例檢定資料是否來自常態)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與前面集數的連結](#7-與前面集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 統計推論三大塊回顧 | 全書 |
| 參數未知的卡方適合度檢定 | §4.7 |
| 例：常態性檢定 | §4.7 |

---

## 1. 統計推論在做什麼：總整理

[▶ 00:31](https://youtu.be/kIN-VV1G7E4?t=31) 統計推論（statistical inference）推的是**不知道的參數 $\theta$**。有幾個 approach（派別），主要兩個：**估計**和**假設檢定**。

**點估計**（[▶ 01:31](https://youtu.be/kIN-VV1G7E4?t=91)）：

- 用 $\hat\theta(X_1,\dots,X_n)$ 估計 $\theta$。有不偏、一致等理論。
- [▶ 02:01](https://youtu.be/kIN-VV1G7E4?t=121) 用 $X_1,\dots,X_n$ 的函數估計一個常數，不可能相等。頂多證明 $\hat\theta\xrightarrow{P}\theta$（$n\to\infty$）。
- 【口頭】但人生有限，不可能抽無窮多樣本，永遠達不到相等。

**區間估計**（[▶ 03:35](https://youtu.be/kIN-VV1G7E4?t=215)）：

- 兩個統計量構成區間，涵蓋參數的機率要 0.95、0.99 都可以。
- [▶ 04:07](https://youtu.be/kIN-VV1G7E4?t=247) 95% 的 0.95 叫**信賴係數**（confidence coefficient）：你的信心有多大。很有用的工具。

**假設檢定**（[▶ 04:38](https://youtu.be/kIN-VV1G7E4?t=278)）：

- 有時候不想知道 $\theta$ 等於多少，想知道它有沒有超過、小於、等於某個值。
- 有 $H_0$、$H_1$；控制型一錯誤不超過顯著水準（通常 0.05）。
- [▶ 05:40](https://youtu.be/kIN-VV1G7E4?t=340) 在這些檢定中，看誰在 $H_1$ 下 power 最大；$H_1$ 有很多點時找 uniformly 最大——UMP。
- [▶ 06:11](https://youtu.be/kIN-VV1G7E4?t=371) 再沒辦法就用概似比檢定。

---

## 2. 為什麼要檢定分配

[▶ 06:41](https://youtu.be/kIN-VV1G7E4?t=401) 所有推論一開始都說「隨機樣本來自某個分配」（Gamma、Poisson、Bernoulli、二項、常態……），那個分配是**給定**的。

[▶ 07:12](https://youtu.be/kIN-VV1G7E4?t=432) 萬一分配不對：

- 你說資料來自常態，用常態的 UMP 檢定 $\mu$ 有沒有超過某值。常態對的話，結果最可信。
- 但如果資料其實不是常態，你以為是 UMP，**一定不是**——你用的 MLR 等性質都是在常態之下找出來的，假設根本不對。

所以很多情形要先確定資料是不是真的來自那個分配 → **卡方檢定**。

---

## 3. 兩種情形

[▶ 08:42](https://youtu.be/kIN-VV1G7E4?t=522)

| 情形 | 例 | 檢定統計量 | 極限分配 |
|---|---|---|---|
| 分配**完全知道** | Uniform$(0,1)$；$b\left(n,\frac13\right)$ | $Q_k=\sum\frac{(N_j-np_j)^2}{np_j}$ | $\chi^2(k-1)$ |
| 分配形式知道、**參數未知** | 「是不是常態」，不在乎 $\mu,\sigma^2$ 是多少 | $Q_k=\sum\frac{(N_j-n\hat p_j)^2}{n\hat p_j}$ | $\chi^2(k-p-1)$ |

---

## 4. 參數未知：用 MLE，自由度減 p

[▶ 10:13](https://youtu.be/kIN-VV1G7E4?t=613)
$$H_0:F=f(x;\theta_1,\dots,\theta_p)\quad(\theta_1,\dots,\theta_p\text{ 未知})\quad\text{vs}\quad H_1:F\text{ 不是這個分配}.$$

**步驟**：

1. [▶ 11:14](https://youtu.be/kIN-VV1G7E4?t=674) 隨機變數的空間（值域）通常知道：常態是 $(-\infty,\infty)$，Gamma 是 $(0,\infty)$，Poisson 是 $\{0,1,2,\dots\}$。把它 partition 成 $A_1,\dots,A_k$。
2. [▶ 12:16](https://youtu.be/kIN-VV1G7E4?t=736) 求 MLE $\hat\theta_1,\dots,\hat\theta_p$，把 $H_0$ 想成 $F=f(x;\hat\theta_1,\dots,\hat\theta_p)$。
3. [▶ 13:21](https://youtu.be/kIN-VV1G7E4?t=801) 每塊機率用估計的參數算：$\hat p_j=\int_{A_j}f(x;\hat\theta_1,\dots,\hat\theta_p)\,dx$（實際上有時查表就好）。
4. [▶ 14:22](https://youtu.be/kIN-VV1G7E4?t=862) 實際次數 $N_j$（$\sum N_j=n$）。
5. $Q_k=\sum_{j=1}^k\frac{(N_j-n\hat p_j)^2}{n\hat p_j}$。

**自由度**（[▶ 15:24](https://youtu.be/kIN-VV1G7E4?t=924)）：

- 原本 $k-1$：分成 $k$ 塊，知道前 $k-1$ 塊有幾個，最後一塊就知道了（總數是 $n$）。
- [▶ 16:25](https://youtu.be/kIN-VV1G7E4?t=985) **估計幾個參數，自由度就減少幾個**（理論證明一定這樣，不是用背的）：
$$Q_k\xrightarrow{D}\chi^2(k-p-1)\quad(H_0\text{ 下}).$$
- [▶ 16:56](https://youtu.be/kIN-VV1G7E4?t=1016) 自由度越大越準確；估太多參數，檢定的 power 會降低。

**檢定**（[▶ 17:57](https://youtu.be/kIN-VV1G7E4?t=1077)）：拒絕 $H_0$ 若
$$Q_k\ge\chi^2_\alpha(k-p-1)\quad(\text{右尾}).$$

**直覺**（[▶ 18:30](https://youtu.be/kIN-VV1G7E4?t=1110)）：$H_0$ 對時 MLE 會很接近真正的參數，所以 $n\hat p_j$ 接近理論次數，也接近實際次數。$k$ 組都很接近就相信 $H_0$；有很多組差很大就拒絕。size 近似 $\alpha$。

---

## 5. 例：檢定資料是否來自常態

[▶ 19:32](https://youtu.be/kIN-VV1G7E4?t=1172) 最常用：
$$H_0:X\sim N(\mu,\sigma^2)\ (\text{不在乎哪一個常態})\quad\text{vs}\quad H_1:X\text{ 不是常態}.$$

**MLE**（[▶ 20:36](https://youtu.be/kIN-VV1G7E4?t=1236)）：
$$\hat\mu=\bar X,\qquad\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2\quad(\text{MLE 除以 }n,\text{ 不是 }n-1).$$

**切塊**（[▶ 21:06](https://youtu.be/kIN-VV1G7E4?t=1266)）：
$$A_1=(-\infty,a_1],\ A_2=(a_1,a_2],\ \dots,\ A_k=(a_{k-1},\infty).$$
【口頭】沒有特別準則；有 $n$ 筆資料就切成每塊至少有兩三筆，不要有某塊沒有資料。

**每塊機率**（[▶ 22:40](https://youtu.be/kIN-VV1G7E4?t=1360)）：標準化後查表（或用電腦積分），不需要自己積分：
$$\hat p_1=P\left(Z\le\frac{a_1-\hat\mu}{\hat\sigma}\right)=\Phi\left(\frac{a_1-\hat\mu}{\hat\sigma}\right),$$
$$\hat p_j=\Phi\left(\frac{a_j-\hat\mu}{\hat\sigma}\right)-\Phi\left(\frac{a_{j-1}-\hat\mu}{\hat\sigma}\right),\qquad\hat p_k=1-\Phi\left(\frac{a_{k-1}-\hat\mu}{\hat\sigma}\right).$$

（$a_j$ 是自己選的、$\hat\mu,\hat\sigma$ 由資料算出，所以都知道。$\Phi(z)=\int_{-\infty}^z\frac{1}{\sqrt{2\pi}}e^{-t^2/2}\,dt$。）

**檢定**（[▶ 27:53](https://youtu.be/kIN-VV1G7E4?t=1673)）：估了 $p=2$ 個參數，
$$Q_k=\sum_{j=1}^k\frac{(N_j-n\hat p_j)^2}{n\hat p_j}\ \dot\sim\ \chi^2(k-3),\qquad\text{拒絕 }H_0\text{ 若 }Q_k\ge\chi^2_\alpha(k-3).$$
$Q_k$ 要算（$N_j$ 數出來、$\hat p_j$ 算出來），$\chi^2_\alpha(k-3)$ 查表（以上機率 $\alpha$、以下機率 $1-\alpha$ 的點）。

【口頭】[▶ 28:56](https://youtu.be/kIN-VV1G7E4?t=1736)

- 真正自己做要花點時間，沒那麼簡單；但有必要知道。
- 讀統計很久，會用 UMVUE、UMP、最強力檢定、信賴區間……「如果資料來自常態我就會做」——但人家會問：**到底是不是常態？**
- [▶ 29:27](https://youtu.be/kIN-VV1G7E4?t=1767) 以後讀研究所，即使讀管理、經濟，做論文其實都在做統計。用的方法是常態所造的，人家會問你有沒有檢定資料真的來自常態。不是的話，所有分析都是錯的。
- [▶ 30:29](https://youtu.be/kIN-VV1G7E4?t=1829) 這是最後告訴你的統計方法，要了解這套方法。不會叫你去算；考的話很多東西會先給你，會公式就會做。

---

## 6. 一頁速查表

**統計推論**：點估計（不偏、一致、UMVUE）→ 區間估計（信賴係數）→ 假設檢定（顯著水準、MP、UMP、LRT）。全部都建立在「分配假設正確」上。

**卡方適合度檢定**：

| | $p_j$ | 自由度 |
|---|---|---|
| 分配完全已知 | $p_j=P_{F_0}(A_j)$ | $k-1$ |
| 有 $p$ 個參數未知 | $\hat p_j$：代 MLE 後算 | $k-p-1$ |

$$Q_k=\sum_{j=1}^k\frac{(N_j-n\hat p_j)^2}{n\hat p_j},\qquad\text{拒絕 }H_0\text{ 若 }Q_k\ge\chi^2_\alpha(k-p-1).$$

**常態性檢定**：$\hat\mu=\bar x$，$\hat\sigma^2=\frac1n\sum(x_i-\bar x)^2$；$\hat p_j=\Phi\left(\frac{a_j-\hat\mu}{\hat\sigma}\right)-\Phi\left(\frac{a_{j-1}-\hat\mu}{\hat\sigma}\right)$；自由度 $k-3$。

關鍵：估一個參數，自由度少一個。

---

## 7. 與前面集數的連結

| 本集觀念 | 前面在哪裡 |
|---|---|
| Pearson 卡方檢定 | 第 25–26 集 |
| MLE | 上學期（基礎統計學第 16–18 集） |
| UMP、LRT | 第 14–22 集 |

---

## 附：本集一句話總結

> **統計推論（點估計、區間估計、假設檢定）都建立在「資料來自某個分配」的假設上，所以要用卡方適合度檢定確認；分配有 $p$ 個未知參數時，先用 MLE 估計、代入算各塊機率 $\hat p_j$，$Q_k=\sum(N_j-n\hat p_j)^2/(n\hat p_j)$ 在 $H_0$ 下趨近 $\chi^2(k-p-1)$——檢定常態性時估了 $\mu,\sigma^2$，自由度是 $k-3$。**

---

*筆記依據「高等統計學」Lec27 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
