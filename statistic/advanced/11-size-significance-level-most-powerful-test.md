---
course: 高等統計學（數理統計續）
episode: 11
lecture: Lec11（第六週 2/2）
date: 待補
video: https://youtu.be/5g6Qv_0iNCc
notes: Hogg 8th ed. §4.5 檢定的大小（size）、顯著水準；§8.1 最強力檢定（most powerful test）定義（Definition 8.1.1）
---

# 第 11 集 · 第六週 (2/2)：檢定力函數再解釋；檢定的大小與顯著水準；最強力檢定 [▶ 影片](https://youtu.be/5g6Qv_0iNCc)

← 上一集：[10](10-test-critical-region-type-errors-power-function.md) ｜ [總目錄](../README.md) ｜ 下一集：[12](12-likelihood-ratio-neyman-pearson-statement.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 11 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（36:00 左右，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §4.5、§8.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正
> - `⚠️ 待確認` 查不清楚的地方

> ⚠️ 逐字稿缺字（整集通用）：「power function」→「Paw Function」，「maximum」→「Maximin」，「顯著水準」→「顯示水準」，「$\alpha$」→「阿華／RF／RWA」，「遞增」→「地震」。[▶ 18:44](https://youtu.be/5g6Qv_0iNCc?t=1124)–[▶ 23:39](https://youtu.be/5g6Qv_0iNCc?t=1419) 約 5 分鐘全是幻聽字（可能是下課或錄影中斷），內容遺失。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 再看例子：兩個拒絕域的檢定力函數](#1-再看例子兩個拒絕域的檢定力函數)
- [2. 圖上的型一、型二錯誤](#2-圖上的型一型二錯誤)
- [3. 檢定的大小（size）](#3-檢定的大小size)
- [4. 顯著水準與找檢定的原則](#4-顯著水準與找檢定的原則)
- [5. 最強力檢定（簡單對簡單）](#5-最強力檢定簡單對簡單)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)
- [⚠️ 待確認清單](#️-待確認清單)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 在檢定力函數圖上看型一、型二錯誤 | §4.5 |
| size $=\max_{\theta\in H_0}\pi_C(\theta)$ | §4.5 |
| 顯著水準 $\alpha$；在 size $\le\alpha$ 中讓檢定力最大 | §4.5、§8.1 |
| 最強力檢定（$H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$） | Definition 8.1.1 |

---

## 1. 再看例子：兩個拒絕域的檢定力函數

[▶ 00:00](https://youtu.be/5g6Qv_0iNCc?t=0) 上一集的例子：$X_1,\dots,X_{25}$ iid $N(\mu,100)$（考試成績），
$$H_0:\mu\le 75\quad\text{vs}\quad H_1:\mu>75.$$

| 拒絕域 | 檢定力函數 |
|---|---|
| $C_1=\{\bar x>75\}$ | $\pi_{C_1}(\mu)=P_\mu(\bar X>75)$ |
| $C_2=\{\bar x>78\}$ | $\pi_{C_2}(\mu)=P_\mu(\bar X>78)$ |

兩者都是 $\mu$ 的**遞增**函數。

---

## 2. 圖上的型一、型二錯誤

[▶ 02:31](https://youtu.be/5g6Qv_0iNCc?t=151) 橫軸 $\mu$，75 把它切成兩段：左邊 $H_0$ 為真，右邊 $H_1$ 為真。

**左段（$\mu\le 75$）**：曲線高度＝$H_0$ 對卻拒絕的機率＝**型一錯誤機率**。$\mu$ 越小越小，最大在 $\mu=75$。

**右段（$\mu>75$）**（[▶ 04:35](https://youtu.be/5g6Qv_0iNCc?t=275)）：

- 曲線高度＝$H_1$ 對時拒絕 $H_0$ 的機率，越大越好。
- [▶ 06:08](https://youtu.be/5g6Qv_0iNCc?t=368) 曲線**上方到 1 的那一段**＝$1-\pi_C(\mu)$＝$H_1$ 對卻不拒絕 $H_0$ 的機率＝**型二錯誤機率**。

**比較 $C_1$、$C_2$**：

| | 型一錯誤（左段最高點） | 型二錯誤（右段曲線上方） |
|---|---|---|
| $C_1$（$\bar x>75$） | 0.5，太大 | 小（$\mu=77$ 時 power 0.84） |
| $C_2$（$\bar x>78$） | 0.067，很小 | [▶ 09:19](https://youtu.be/5g6Qv_0iNCc?t=559) 變大 |

[▶ 10:50](https://youtu.be/5g6Qv_0iNCc?t=650) 型一錯誤變小，型二錯誤就變大；**沒辦法同時讓兩種都很小**。所以把「對的時候被拒絕比較嚴重」的放 $H_0$，控制型一錯誤。

【口頭】[▶ 12:23](https://youtu.be/5g6Qv_0iNCc?t=743) 很嚴格的法官，要充分證據才判有罪；他一生中一定比較常把有罪的人判成沒罪（證據不足）——型二錯誤，沒辦法。但不希望把沒罪的人判有罪（型一錯誤）：一個人被關十幾年才發現不是他，政府賠一千萬、一億都沒意義，整個人生都沒了。

---

## 3. 檢定的大小（size）

[▶ 13:57](https://youtu.be/5g6Qv_0iNCc?t=837) 任何檢定的檢定力函數：

- $H_0$ 為真：$\pi_C(\theta)$＝型一錯誤機率；
- $H_1$ 為真：$\pi_C(\theta)$＝power，$1-\pi_C(\theta)$＝型二錯誤機率。

> **定義（size）**（[▶ 14:58](https://youtu.be/5g6Qv_0iNCc?t=898)）：拒絕域 $C$（檢定）的大小
> $$\text{size}=\max_{\theta\in H_0}\pi_C(\theta),$$
> 也就是**型一錯誤機率的最大值**。

（老師先寫成最小值，馬上改正為**最大值**。）

[▶ 16:29](https://youtu.be/5g6Qv_0iNCc?t=989) 例：

- $C_1$：$\max_{\mu\le 75}\pi_{C_1}(\mu)=\pi_{C_1}(75)=0.5$（遞增，最大在端點 75）。
- $C_2$：$\max_{\mu\le 75}\pi_{C_2}(\mu)=\pi_{C_2}(75)=0.067$。

$C_2$ 比較好：它的型一錯誤最大只有 0.067。

---

## 4. 顯著水準與找檢定的原則

[▶ 24:10](https://youtu.be/5g6Qv_0iNCc?t=1450) 任何檢定都可能犯兩種錯誤。我們比較怕型一錯誤，所以：先設定一個值，所有考慮的檢定，型一錯誤都不能超過它；再在這裡面挑最好的。

【口頭】[▶ 25:12](https://youtu.be/5g6Qv_0iNCc?t=1512) 班上不可能有一個同學體育、數學、英文每一科都最好。如果某一科一定要最好，其他標準就要降低——體育只要 100 公尺跑 25 秒、全校前 100 名就好——這樣才挑得到。

> **定義（顯著水準，significance level）**（[▶ 26:13](https://youtu.be/5g6Qv_0iNCc?t=1573)）：事先給定的 $\alpha$，要求 size $\le\alpha$。用來控制型一錯誤機率。

**原則**（[▶ 28:14](https://youtu.be/5g6Qv_0iNCc?t=1694)）：

1. 先固定顯著水準 $\alpha$。
2. 在**size $\le\alpha$ 的檢定**這一類裡找。
3. 挑**型二錯誤機率最小**的——等價於 **$H_1$ 為真時 power 最大**（因為 power $=1-$ 型二錯誤機率）。

【口頭】[▶ 30:24](https://youtu.be/5g6Qv_0iNCc?t=1824) 人生做決策也是：不可能每樣都最好，要有所選擇，保守一點，先決定哪些東西一定不能怎麼樣。

---

## 5. 最強力檢定（簡單對簡單）

[▶ 31:26](https://youtu.be/5g6Qv_0iNCc?t=1886) 先只看**簡單假設**：
$$H_0:\theta=\theta_0\quad\text{vs}\quad H_1:\theta=\theta_1.$$

> **定義（最強力檢定，most powerful test，size $\alpha$）**（[▶ 32:27](https://youtu.be/5g6Qv_0iNCc?t=1947)；課本 Definition 8.1.1）：拒絕域 $C$ 滿足
> 1. $P_{\theta_0}\left((X_1,\dots,X_n)\in C\right)=\alpha$（size 剛好是 $\alpha$，即 $\pi_C(\theta_0)=\alpha$）；
> 2. 對**每一個**滿足 $P_{\theta_0}\left((X_1,\dots,X_n)\in A\right)\le\alpha$ 的拒絕域 $A$，
> $$P_{\theta_1}\left((X_1,\dots,X_n)\in C\right)\ge P_{\theta_1}\left((X_1,\dots,X_n)\in A\right).$$
>
> 則 $C$ 叫 size $\alpha$ 的**最強力拒絕域**，對應的檢定叫最強力檢定。

意思：在所有型一錯誤 $\le\alpha$ 的拒絕域裡，$C$ 在 $H_1$ 為真時拒絕 $H_0$ 的機率（power）最大。

[▶ 35:29](https://youtu.be/5g6Qv_0iNCc?t=2129) 下一次詳細解釋。

---

## 6. 一頁速查表

**檢定力函數圖**：

- $H_0$ 區：曲線高度＝型一錯誤機率。
- $H_1$ 區：曲線高度＝power；曲線到 1 的距離＝型二錯誤機率。

**size**：$\max_{\theta\in H_0}\pi_C(\theta)$（型一錯誤最大值）。例：$C_1$ 0.5、$C_2$ 0.067。

**顯著水準 $\alpha$**：要求 size $\le\alpha$。

**原則**：在 size $\le\alpha$ 的檢定中，讓 $H_1$ 下的 power 最大（＝型二錯誤最小）。

**最強力檢定**（$\theta_0$ vs $\theta_1$）：
$$\pi_C(\theta_0)=\alpha,\qquad\pi_C(\theta_1)\ge\pi_A(\theta_1)\ \ \forall A\text{ 使 }\pi_A(\theta_0)\le\alpha.$$

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 最強力檢定 | 下一集：Neyman–Pearson 引理（怎麼找到它） |
| 簡單 → 複合 | 一致最強力檢定（UMP test） |

---

## 附：本集一句話總結

> **檢定力函數在 $H_0$ 區是型一錯誤、在 $H_1$ 區到 1 的距離是型二錯誤，兩者此消彼長；所以先給顯著水準 $\alpha$，只考慮 size（型一錯誤最大值）$\le\alpha$ 的檢定，再從中挑 $H_1$ 下 power 最大的——簡單對簡單時這叫最強力檢定。**

---

## ⚠️ 待確認清單

1. [▶ 18:44](https://youtu.be/5g6Qv_0iNCc?t=1124)–[▶ 23:39](https://youtu.be/5g6Qv_0iNCc?t=1419) 約 5 分鐘逐字稿全是幻聽，不知道這段有沒有講課（回來時老師說「這裡是 $\theta_0$ 不是 $\theta_1$」，可能中間寫了東西）。待補。

---

*筆記依據「高等統計學」Lec11 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
