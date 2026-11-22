---
course: 統計學（數理統計，數學系）
episode: 12
lecture: Lec12
date: 待補
video: https://youtu.be/u2F_IfY91Vk
notes: Hogg 8th ed. §4.1 估計量、估計值、不偏（Definition 4.1.3，p. 226）；參數空間 $\Omega$（§4.1）；§5.1 依機率收斂（預告）
---

# 第 12 集 · Lec12：參數空間、估計量與估計值、不偏估計量 [▶ 影片](https://youtu.be/u2F_IfY91Vk)

← 上一集：[11](11-xbar-s2-independence-chi-square-statistical-inference.md) ｜ [總目錄](../README.md) ｜ 下一集：[13](13-convergence-in-probability-wlln-consistency.md) →

> **課程**：統計學（數學系的「數理統計」）— 第 12 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（35:38，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【Q&A】` 學生提問與回答
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「parameter space」→「primited space」，「estimator / estimate」→「estimator／XMETA／Astimate／esmet」，「$\theta$／$\hat\theta$」→「Sita／SETA／Sitta Head」，「biased」→「BIOS」，「iid」→「RID」，「$\epsilon$」→「Epson」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 參數空間](#1-參數空間)
- [2. 估計量 vs 估計值](#2-估計量-vs-估計值)
- [3. 兩個問題：什麼是好的？怎麼找？](#3-兩個問題什麼是好的怎麼找)
- [4. 不偏估計量](#4-不偏估計量)
  - [4.1 定義](#41-定義)
  - [4.2 為什麼這樣定義是合理的](#42-為什麼這樣定義是合理的)
  - [4.3 期望值的兩種算法](#43-期望值的兩種算法)
  - [4.4 例：常態的 μ](#44-例常態的-μ)
- [5. 預告：n→∞ 時要趨近 θ](#5-預告n-時要趨近-θ)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:31](https://youtu.be/u2F_IfY91Vk?t=31) 統計推論分成**估計**和**檢定**；估計分成點估計和區間估計。從**點估計**開始。

| 主題 | 課本 |
|---|---|
| 參數空間 $\Omega$ | §4.1 |
| 估計量（estimator）vs 估計值（estimate） | §4.1 |
| 不偏估計量 | Definition 4.1.3，p. 226 |

---

## 1. 參數空間

[▶ 01:01](https://youtu.be/u2F_IfY91Vk?t=61) 統計的起點：$X_1,\dots,X_n$ iid，pdf $f(x;\theta)$。$f$ 知道，$\theta$ 不知道。

但通常**知道 $\theta$ 落在什麼範圍**。

> **參數空間**（parameter space）：$\theta$ 可能的值的集合，記作 $\Omega$。

| 分配 | 參數 | 參數空間 |
|---|---|---|
| $N(\mu,\sigma^2)$ | $\mu$ | $(-\infty,\infty)$ |
| | $\sigma^2$ | $(0,\infty)$ |
| Poisson$(\lambda)$ | $\lambda$ | $(0,\infty)$ |
| $b(n,p)$ | $p$ | $(0,1)$ |

---

## 2. 估計量 vs 估計值

[▶ 02:35](https://youtu.be/u2F_IfY91Vk?t=155) 點估計想知道 $\theta$ 等於多少。不能憑空猜，要有隨機樣本（iid 隨機變數＝隨機樣本）。

**統計量**（[▶ 03:06](https://youtu.be/u2F_IfY91Vk?t=186)）：隨機樣本的函數，裡面**沒有** $\theta$。寫成 $\hat\theta(X_1,\dots,X_n)$，帽子表示「拿來估 $\theta$ 的」，函數裡不含 $\theta$。

> **估計量**（estimator）：用來估 $\theta$ 的統計量 $\hat\theta(X_1,\dots,X_n)$。

[▶ 04:38](https://youtu.be/u2F_IfY91Vk?t=278) 只是換個名字：它還是統計量，只是目的是估 $\theta$。

[▶ 05:08](https://youtu.be/u2F_IfY91Vk?t=308) **抽之前 vs 抽之後**：

- 抽之前：每個新竹市民都可能被抽到，所以 $X_i$ 是隨機變數。
- 抽之後（打完電話、問完 100 人）：值都知道了，改寫成小寫 $x_1,\dots,x_n$。

> **估計值**（estimate）：觀察到 $X_i=x_i$ 後代進去得到的數 $\hat\theta(x_1,\dots,x_n)$。

| | 估計量 estimator | 估計值 estimate |
|---|---|---|
| 寫法 | $\hat\theta(X_1,\dots,X_n)$ | $\hat\theta(x_1,\dots,x_n)$ |
| 是什麼 | 隨機變數（實數函數的函數），有分配 | 常數 |

[▶ 08:45](https://youtu.be/u2F_IfY91Vk?t=525) 【口頭】管理統計常在算估計值。本課主要討論**估計量**。

---

## 3. 兩個問題：什麼是好的？怎麼找？

[▶ 09:15](https://youtu.be/u2F_IfY91Vk?t=555) 通常有**很多**估計量可用。要選哪一個？

**問題 1：建立標準**。什麼叫「好的」、什麼叫「最佳的」。

【口頭】[▶ 10:18](https://youtu.be/u2F_IfY91Vk?t=618) 人生一直在做選擇（選科系、選男女朋友……），每人心中有自己的標準，可以不一樣。但統計要大家一樣的標準，前人經過很長時間分析，決定哪些標準合理，我們學那些。最好的當然要；但最好的有時**不存在**，那挑好的就可以（「退而求其次」）。

**問題 2：找的規則**（[▶ 11:50](https://youtu.be/u2F_IfY91Vk?t=710)）。就算知道什麼叫好，沒有方向也不知道怎麼找。要有規則（rule）導出合理的估計量。後面會介紹兩種方法。

---

## 4. 不偏估計量

### 4.1 定義

[▶ 12:51](https://youtu.be/u2F_IfY91Vk?t=771) 先定義「好的」估計量。

[▶ 13:23](https://youtu.be/u2F_IfY91Vk?t=803) 估計量是隨機變數：今天抽到 $x_1,\dots,x_n$，明天抽到 $x_1',\dots,x_n'$，兩天的估計值不一樣。

> **定義（不偏估計量，unbiased estimator）**（課本 Definition 4.1.3，p. 226）：
> $$E_\theta\left[\hat\theta(X_1,\dots,X_n)\right]=\theta,\qquad\text{對所有 }\theta\in\Omega.$$
> 不成立就叫**偏的**（biased）。

[▶ 15:29](https://youtu.be/u2F_IfY91Vk?t=929) 下標 $\theta$ 的意思：「當真正的參數是 $\theta$ 時」，期望值就等於那個真正的 $\theta$。不管 $\theta$ 是多少都要成立。

### 4.2 為什麼這樣定義是合理的

[▶ 15:59](https://youtu.be/u2F_IfY91Vk?t=959) 畫 $\hat\theta$ 的 pdf：

- $\hat\theta$ 會落在線上**每一點**都有可能，每天估的都不一樣。
- 期望值＝平均＝分配的**中心點**。中心點剛好在真正的 $\theta$。
- [▶ 18:02](https://youtu.be/u2F_IfY91Vk?t=1082) 【口頭】班上平均 70 分，大部分同學在 70 附近，越高越低的人越少。
- 所以 $\hat\theta$ 落在真正 $\theta$ **附近的機會最大**；跑到很遠的地方，pdf 很低，機會很小。

[▶ 20:08](https://youtu.be/u2F_IfY91Vk?t=1208) 重點：

- 估計量是隨機變數，參數是常數，所以 $P(\hat\theta=\theta)$ 通常是 0，**不可能剛好等於**。
- 但不偏 ⇒ **很靠近**它。很靠近就好了。

[▶ 24:18](https://youtu.be/u2F_IfY91Vk?t=1458) **偏的情形**：真正的 $\theta$ 在這裡，$E(\hat\theta)$ 在別處。大部分會落在 $E(\hat\theta)$ 附近，落在真正 $\theta$ 附近的機會相對比較小。所以喜歡不偏的。

【口頭】要了解定義的合理性，不要只背。

### 4.3 期望值的兩種算法

[▶ 21:44](https://youtu.be/u2F_IfY91Vk?t=1304)

**方法 1**：$\hat\theta$ 是 $X_1,\dots,X_n$ 的函數 → 大寫改小寫，乘隨機樣本的 joint pdf，$n$ 重積分：
$$E_\theta(\hat\theta)=\int\!\cdots\!\int\hat\theta(x_1,\dots,x_n)\prod_{i=1}^nf(x_i;\theta)\,dx_1\cdots dx_n.$$
（$f$ 裡放同一個 $\theta$，才代表「$\theta$ 是對的」。）

**方法 2**（[▶ 22:48](https://youtu.be/u2F_IfY91Vk?t=1368)）：$\hat\theta$ 是隨機變數，如果能找到它的 pdf $f_{\hat\theta}$：
$$E_\theta(\hat\theta)=\int u\,f_{\hat\theta}(u)\,du.$$

### 4.4 例：常態的 μ

[▶ 25:19](https://youtu.be/u2F_IfY91Vk?t=1519) $X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$，估 $\mu$。用 $E(X_i)=\mu$、期望值的線性：

| 估計量 | 期望值 | 不偏？ |
|---|---|---|
| $X_1$ | $\mu$ | ✓ |
| $\frac12(X_1+X_2)$ | $\frac12(\mu+\mu)=\mu$ | ✓ |
| $\bar X=\frac1n\sum X_i$ | $\mu$ | ✓ |
| $\frac{1}{n+1}\sum X_i$ | $\frac{n}{n+1}\mu\ne\mu$ | ✗（biased） |

不偏的估計量可以有很多個，所以只靠不偏還不夠選。

【Q&A】[▶ 28:21](https://youtu.be/u2F_IfY91Vk?t=1701) 學生問（逐字稿聽不清楚完整問題，大意是）：數據的分配如果不知道怎麼辦？
老師答：現在學的是知道分配形式、只有參數不知道。分配不知道是另外的問題，統計還是可以做。只要背後有分配，數據就照那個分配產生，用統計方法估出來一定會很接近，可以放心。統計推論能告訴你「我有多大的信心說這樣是對的」。

---

## 5. 預告：n→∞ 時要趨近 θ

[▶ 29:24](https://youtu.be/u2F_IfY91Vk?t=1764) 不偏只說分配中心在 $\theta$，但 $\hat\theta$ 不會等於 $\theta$。我們還會希望：

$$\hat\theta(X_1,\dots,X_n)\to\theta\quad\text{當 }n\to\infty.$$

這不成立的話，估計量有問題（樣本無限多還估不準）。

**數列的收斂**（[▶ 31:26](https://youtu.be/u2F_IfY91Vk?t=1886)，微積分）：$a_n\to a$ 是指
$$\forall\epsilon>0,\ \exists N,\ \text{使得 } n>N\Rightarrow|a_n-a|<\epsilon.$$

- 每個 $a_n$ 都不需要等於 $a$。
- $\epsilon$ 可以任意小（$0.1^{1000}$、$0.1^{10000}$ 都行）；超過 $N$ 之後，$a_n$ 和 $a$ 的差比任意小的數還小，就當作沒有差距。
- 【口頭】99 分跟 100 分有差嗎？很接近最好的就好。

[▶ 34:01](https://youtu.be/u2F_IfY91Vk?t=2041) **難處**：$\hat\theta$ 不管 $n$ 多大都是**隨機變數**，$\theta$ 是**常數**。一串隨機變數怎麼收斂到常數？機率裡有好幾種不同的定義。下次講。

---

## 6. 一頁速查表

**名詞**

| 名詞 | 意思 |
|---|---|
| 參數空間 $\Omega$ | $\theta$ 可能的值 |
| 估計量 $\hat\theta(X_1,\dots,X_n)$ | 拿來估 $\theta$ 的統計量；隨機變數 |
| 估計值 $\hat\theta(x_1,\dots,x_n)$ | 代入觀察值；常數 |

**不偏**：$E_\theta(\hat\theta)=\theta$，$\forall\theta\in\Omega$。

- 意義：$\hat\theta$ 的分配中心在真正的 $\theta$，所以落在 $\theta$ 附近機會最大。
- 算 $E_\theta(\hat\theta)$：用 joint pdf $\prod f(x_i;\theta)$ 積分，或用 $\hat\theta$ 自己的 pdf。

**常態 $\mu$**：$X_1$、$\frac{X_1+X_2}2$、$\bar X$ 都不偏；$\frac{1}{n+1}\sum X_i$ 偏（期望值 $\frac{n}{n+1}\mu$）。

**下一步**：$n\to\infty$ 時 $\hat\theta\to\theta$（隨機變數收斂到常數，要新定義）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 不偏 | 均方誤差、最小變異不偏估計量 |
| 隨機變數收斂到常數 | 下一集：依機率收斂、一致估計量 |
| 「找估計量的規則」 | 動差法、最大概似估計 |

---

## 附：本集一句話總結

> **估計量是拿來估 $\theta$ 的統計量（隨機變數），代入觀察值後才是估計值（常數）；估計量不可能剛好等於 $\theta$，但如果它不偏（$E_\theta\hat\theta=\theta$），它的分配中心就在 $\theta$，會很靠近 $\theta$。**

---

*筆記依據「統計學」Lec12 錄影逐字稿（whisper large-v3-turbo，35:38）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
