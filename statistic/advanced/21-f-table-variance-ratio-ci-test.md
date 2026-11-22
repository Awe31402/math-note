---
course: 高等統計學（數理統計續）
episode: 21
lecture: Lec21（第十一週 2/2）
date: 待補
video: https://youtu.be/qr3kK7wcQmo
notes: Hogg 8th ed. §3.6.2 F 分配；§8.3.2 常態變異數的 LRT（兩變異數相等）
---

# 第 21 集 · 第十一週 (2/2)：F 分配的查表技巧；兩變異數比的信賴區間與檢定 [▶ 影片](https://youtu.be/qr3kK7wcQmo)

← 上一集：[20](20-lrt-to-t-test-f-distribution.md) ｜ [總目錄](../README.md) ｜ 下一集：[22](22-lrt-equal-variances-derivation.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 21 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 51 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §3.6.2、§8.3.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「F 分配」→「AppFone Pay／Apple Pay／App 分配」，「信賴區間」→「心愛期間／信頼期間」，「variance」→「Valence／辨利素／便利數」，「$\chi^2$」→「卡方／Kawang／卡瘡」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 為什麼叫隨機變數](#1-為什麼叫隨機變數)
- [2. F 分配與記號](#2-f-分配與記號)
- [3. 1/F 的分配](#3-1f-的分配)
- [4. 查表技巧：F_α(r₁,r₂)=1/F₁₋α(r₂,r₁)](#4-查表技巧f_αr₁r₂1f₁₋αr₂r₁)
- [5. σₓ²/σᵧ² 的信賴區間](#5-σₓ²σᵧ²-的信賴區間)
- [6. 檢定 H₀:σₓ²=σᵧ²](#6-檢定-h₀σₓ²σᵧ²)
- [7. 它是 LRT 嗎：設定](#7-它是-lrt-嗎設定)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $1/F\sim F(r_2,r_1)$；查表技巧 | §3.6.2 |
| $\sigma_x^2/\sigma_y^2$ 的信賴區間 | §3.6.2 習題類型 |
| $H_0:\sigma_x^2=\sigma_y^2$ 的檢定 | §8.3.2 |

---

## 1. 為什麼叫隨機變數

【口頭】[▶ 00:34](https://youtu.be/qr3kK7wcQmo?t=34)

- **變數**（variable）：值不固定，可能發生這個也可能發生那個（今天可能下雨也可能不下）。數值分析、工程裡也常講變數。
- 不會變的例子：物理、化學實驗如果條件完全控制一樣，做一百次結果都一樣。
- [▶ 02:05](https://youtu.be/qr3kK7wcQmo?t=125) **隨機**變數：很多點都可能發生，但每一點是**按照一定的機率**發生的。
- [▶ 03:08](https://youtu.be/qr3kK7wcQmo?t=188) pdf 描述每一點發生的可能性有多大：曲線越高的地方，發生的機會越大。

---

## 2. F 分配與記號

[▶ 04:11](https://youtu.be/qr3kK7wcQmo?t=251) F 分配有兩個自由度 $r_1,r_2$。只有正的值；曲線很快上升、到最高點後遞減，拖到無窮，但很遠的地方可能性很小。

**定義**（[▶ 05:43](https://youtu.be/qr3kK7wcQmo?t=343)）：$F=\frac{U/r_1}{V/r_2}$，$U\sim\chi^2(r_1)$、$V\sim\chi^2(r_2)$ 獨立。pdf 比較複雜，不介紹，會用就好。

**記號**（[▶ 07:14](https://youtu.be/qr3kK7wcQmo?t=434)）：做信賴區間或檢定要找兩個點，左右各 $\alpha/2$：

- 以下機率 $\frac\alpha2$ 的點：$F_{\alpha/2}(r_1,r_2)$；
- 以下機率 $1-\frac\alpha2$ 的點：$F_{1-\alpha/2}(r_1,r_2)$。

（$F_\alpha$ 是**左尾**機率 $\alpha$ 的點。）

[▶ 08:46](https://youtu.be/qr3kK7wcQmo?t=526) 每本書都有表，考試題目下面也會附表。但表**只列以下機率超過 0.5 的點**。例如 90% 信賴區間，$F_{0.95}$ 查得到，$F_{0.05}$ 表上絕對沒有。

---

## 3. 1/F 的分配

> **定理**（[▶ 09:49](https://youtu.be/qr3kK7wcQmo?t=589)）：$F\sim F(r_1,r_2)$ ⇒ $\frac1F\sim F(r_2,r_1)$（自由度對調）。

**證明**（[▶ 10:49](https://youtu.be/qr3kK7wcQmo?t=649)）：由定義，存在獨立的 $U\sim\chi^2(r_1)$、$V\sim\chi^2(r_2)$ 使 $F=\frac{U/r_1}{V/r_2}$。所以
$$\frac1F=\frac{V/r_2}{U/r_1},$$
分子是 $\chi^2(r_2)$ 除以自由度、分母是 $\chi^2(r_1)$ 除以自由度，兩者獨立 ⇒ $\frac1F\sim F(r_2,r_1)$。∎

（隨機變數是實數函數，它的倒數還是實數函數，還是隨機變數。）

---

## 4. 查表技巧：F_α(r₁,r₂)=1/F₁₋α(r₂,r₁)

> **定理**（[▶ 13:24](https://youtu.be/qr3kK7wcQmo?t=804)）：
> $$F_\alpha(r_1,r_2)=\frac{1}{F_{1-\alpha}(r_2,r_1)}.$$

$\alpha<0.5$ 時左邊查不到，改查 $F(r_2,r_1)$ 以下機率 $1-\alpha$（$>0.5$，查得到）的點，取倒數。

**證明**（[▶ 15:27](https://youtu.be/qr3kK7wcQmo?t=927)）：$F\sim F(r_1,r_2)$。由定義
$$P\left(F\le F_\alpha(r_1,r_2)\right)=\alpha.$$
兩邊都是正的，取倒數，不等號反向：
$$P\left(\frac1F\ge\frac{1}{F_\alpha(r_1,r_2)}\right)=\alpha\ \Rightarrow\ P\left(\frac1F\le\frac{1}{F_\alpha(r_1,r_2)}\right)=1-\alpha.$$
$\frac1F\sim F(r_2,r_1)$，以下機率 $1-\alpha$ 的點是 $F_{1-\alpha}(r_2,r_1)$：
$$\frac{1}{F_\alpha(r_1,r_2)}=F_{1-\alpha}(r_2,r_1).$$
∎

【口頭】[▶ 19:01](https://youtu.be/qr3kK7wcQmo?t=1141) 自己證一兩遍才清楚這些符號；證過之後要記下來。人家給你表、表上沒有，你要知道這個關係。

---

## 5. σₓ²/σᵧ² 的信賴區間

[▶ 20:35](https://youtu.be/qr3kK7wcQmo?t=1235) 介紹 F 分配主要是為了**兩個變異數的比**（ratio of variances）。

**設定**（[▶ 21:07](https://youtu.be/qr3kK7wcQmo?t=1267)）：$X_1,\dots,X_n$ iid $N(\mu_x,\sigma_x^2)$；$Y_1,\dots,Y_m$ iid $N(\mu_y,\sigma_y^2)$；兩組獨立。

[▶ 22:39](https://youtu.be/qr3kK7wcQmo?t=1359)
$$S_x^2=\frac{1}{n-1}\sum(X_i-\bar X)^2,\qquad S_y^2=\frac{1}{m-1}\sum(Y_j-\bar Y)^2$$
（除以 $n-1$ 才不偏）。
$$\frac{(n-1)S_x^2}{\sigma_x^2}\sim\chi^2(n-1),\qquad\frac{(m-1)S_y^2}{\sigma_y^2}\sim\chi^2(m-1),\qquad\text{獨立}.$$

**造 F**（[▶ 24:14](https://youtu.be/qr3kK7wcQmo?t=1454)）：
$$F=\frac{\frac{(m-1)S_y^2}{\sigma_y^2}\Big/(m-1)}{\frac{(n-1)S_x^2}{\sigma_x^2}\Big/(n-1)}=\frac{S_y^2}{S_x^2}\cdot\frac{\sigma_x^2}{\sigma_y^2}\sim F(m-1,n-1).$$

**區間**（[▶ 25:49](https://youtu.be/qr3kK7wcQmo?t=1549)）：
$$P\left(F_{\alpha/2}(m-1,n-1)\le\frac{S_y^2}{S_x^2}\cdot\frac{\sigma_x^2}{\sigma_y^2}\le F_{1-\alpha/2}(m-1,n-1)\right)=1-\alpha,$$
其中 $F_{\alpha/2}(m-1,n-1)=\frac{1}{F_{1-\alpha/2}(n-1,m-1)}$（查得到）。乘以 $\frac{S_x^2}{S_y^2}$：

> **$\frac{\sigma_x^2}{\sigma_y^2}$ 的 $100(1-\alpha)\%$ 信賴區間**（[▶ 27:55](https://youtu.be/qr3kK7wcQmo?t=1675)）：
> $$\left[\frac{1}{F_{1-\alpha/2}(n-1,m-1)}\cdot\frac{S_x^2}{S_y^2},\ \ F_{1-\alpha/2}(m-1,n-1)\cdot\frac{S_x^2}{S_y^2}\right].$$

兩端是統計量（沒有參數，查表可算），涵蓋參數的機率 $1-\alpha$。

**變形**（[▶ 29:30](https://youtu.be/qr3kK7wcQmo?t=1770)）：不等式每一項都 $>0$，

- 要 $\frac{\sigma_x}{\sigma_y}$：每一項開根號（同一個事件，機率不變）。
- 要 $\frac{\sigma_y^2}{\sigma_x^2}$：每一項取倒數（不等號反向）。
- 要三次方：開根號再三次方。

---

## 6. 檢定 H₀:σₓ²=σᵧ²

[▶ 32:02](https://youtu.be/qr3kK7wcQmo?t=1922) 這個問題上，假設檢定比較重要。

**為什麼**（[▶ 32:35](https://youtu.be/qr3kK7wcQmo?t=1955)）：真正重要的是 $H_0:\mu_x=\mu_y$ vs $H_1:\mu_x\ne\mu_y$。能處理的前提是**變異數相等**（$\sigma_x^2=\sigma_y^2=\sigma^2$），不相等就沒辦法做。所以要**先**檢定變異數相等；接受 $H_0$ 就相信相等，可以用以前學的方法。

**假設**（[▶ 35:08](https://youtu.be/qr3kK7wcQmo?t=2108)）：
$$H_0:\sigma_x^2=\sigma_y^2\iff\frac{\sigma_x^2}{\sigma_y^2}=1\quad\text{vs}\quad H_1:\frac{\sigma_x^2}{\sigma_y^2}\ne 1.$$

**檢定統計量**（[▶ 38:15](https://youtu.be/qr3kK7wcQmo?t=2295)）：$H_0$ 為真時 $\frac{\sigma_x^2}{\sigma_y^2}=1$，
$$\frac{S_y^2}{S_x^2}\sim F(m-1,n-1).$$
這叫**檢定統計量**（test statistic）。

**拒絕域**（[▶ 41:19](https://youtu.be/qr3kK7wcQmo?t=2479)）：左右各 $\frac\alpha2$，
$$\frac{s_y^2}{s_x^2}\le\frac{1}{F_{1-\alpha/2}(n-1,m-1)}\quad\text{或}\quad\frac{s_y^2}{s_x^2}\ge F_{1-\alpha/2}(m-1,n-1).$$

【口頭】[▶ 39:18](https://youtu.be/qr3kK7wcQmo?t=2358) 這裡 MP、UMP 都沒有（$H_1$ 是不等）。先用簡單的找法，之後再證明它是哪一種檢定。

**驗證 size $=\alpha$**（[▶ 42:21](https://youtu.be/qr3kK7wcQmo?t=2541)）：令 $A=\{\text{左邊}\}$、$B=\{\text{右邊}\}$。左邊的點（以下機率 $\frac\alpha2$）一定比右邊的點（以下機率 $1-\frac\alpha2$）小，同一個值不可能同時小於左點又大於右點 ⇒ $A\cap B=\varnothing$。所以
$$P_{H_0}(A\cup B)=P_{H_0}(A)+P_{H_0}(B)=\frac\alpha2+\frac\alpha2=\alpha.$$

---

## 7. 它是 LRT 嗎：設定

[▶ 46:30](https://youtu.be/qr3kK7wcQmo?t=2790) 要證明這個檢定其實是**概似比檢定**。

**參數空間**（[▶ 48:01](https://youtu.be/qr3kK7wcQmo?t=2881)）：四個參數都不知道，
$$\Omega=\{(\mu_x,\mu_y,\sigma_x^2,\sigma_y^2):\mu_x,\mu_y\in\mathbb R,\ \sigma_x^2,\sigma_y^2>0\},$$
$$\Theta_0=\{(\mu_x,\mu_y,\sigma^2,\sigma^2):\mu_x,\mu_y\in\mathbb R,\ \sigma^2>0\}.$$
（假設只在變異數上，$\mu_x,\mu_y$ 仍是任意實數。）

**做法**（[▶ 49:35](https://youtu.be/qr3kK7wcQmo?t=2975)）：

- 分母：取 log，對四個參數微分等於 0，解聯立，代入 MLE。
- 分子：令 $\sigma_x^2=\sigma_y^2=\sigma^2$，對 $\mu_x,\mu_y,\sigma^2$ 三個微分，解出來代入。

下次導出來，結果跟今天的一樣。

---

## 8. 一頁速查表

**F 分配**：$\frac{U/r_1}{V/r_2}$；$F_\alpha(r_1,r_2)$ 是**以下**機率 $\alpha$ 的點。

$$\frac1F\sim F(r_2,r_1),\qquad F_\alpha(r_1,r_2)=\frac{1}{F_{1-\alpha}(r_2,r_1)}.$$
證明關鍵：$P(F\le F_\alpha)=\alpha$ ⇒ $P(1/F\le 1/F_\alpha)=1-\alpha$。

**兩變異數**（獨立常態樣本，大小 $n$、$m$）：
$$\frac{S_y^2/\sigma_y^2}{S_x^2/\sigma_x^2}\sim F(m-1,n-1).$$

| | 結果 |
|---|---|
| $\frac{\sigma_x^2}{\sigma_y^2}$ 的 CI | $\left[\frac{1}{F_{1-\alpha/2}(n-1,m-1)}\frac{S_x^2}{S_y^2},\ F_{1-\alpha/2}(m-1,n-1)\frac{S_x^2}{S_y^2}\right]$ |
| $H_0:\sigma_x^2=\sigma_y^2$ 拒絕域 | $\frac{s_y^2}{s_x^2}\le\frac{1}{F_{1-\alpha/2}(n-1,m-1)}$ 或 $\ge F_{1-\alpha/2}(m-1,n-1)$ |

用途：兩樣本比較平均數前，先確認變異數相等。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 變異數相等檢定 = LRT | 下一集：導出 LRT |
| 變異數相等 | 兩樣本 $t$ 檢定 |

---

## 附：本集一句話總結

> **$1/F\sim F(r_2,r_1)$ 所以 $F_\alpha(r_1,r_2)=1/F_{1-\alpha}(r_2,r_1)$，用來查表上沒有的左尾點；兩獨立常態樣本的 $\frac{S_y^2/\sigma_y^2}{S_x^2/\sigma_x^2}\sim F(m-1,n-1)$，由此得到 $\sigma_x^2/\sigma_y^2$ 的信賴區間，以及「$s_y^2/s_x^2$ 太小或太大就拒絕變異數相等」的 size $\alpha$ 檢定——它其實是 LRT，下集證明。**

---

*筆記依據「高等統計學」Lec21 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
