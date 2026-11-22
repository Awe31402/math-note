---
course: 高等統計學（數理統計續）
episode: 16
lecture: Lec16（第九週 1/2）
date: 待補
video: https://youtu.be/7M3gI1KLkh4
notes: Hogg 8th ed. §8.2 複合對複合的 UMP；Definition 8.2.2 單調概似比（mlr，p. 483）；§8.3 概似比檢定（預告）
---

# 第 16 集 · 第九週 (1/2)：複合假設下的 size 與 UMP 定義；單調概似比（MLR） [▶ 影片](https://youtu.be/7M3gI1KLkh4)

← 上一集：[15](15-ump-examples-normal-mean-variance-poisson-two-sided.md) ｜ [總目錄](../README.md) ｜ 下一集：[17](17-mlr-ump-four-cases-uniform-normal-examples.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 16 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 27 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §8.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「monotone likelihood ratio」→「Molotone／Monotonic Lag Ratio」，「supremum」→「Supremant／Supremium」，「upper bound」→「Apple-Bunk」，「UMP」→「UMB」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 整理：哪種假設有哪種檢定](#1-整理哪種假設有哪種檢定)
- [2. 複合假設下的 size](#2-複合假設下的-size)
- [3. UMP 檢定（一般定義）](#3-ump-檢定一般定義)
- [4. 單調概似比（MLR）](#4-單調概似比mlr)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| $\Theta_0$、$\Theta_1$ 都是集合時的 size、UMP | §8.2 |
| 單調概似比 | Definition 8.2.2，p. 483 |
| 沒有 UMP 時：概似比檢定（預告） | §8.3 |

---

## 1. 整理：哪種假設有哪種檢定

[▶ 00:33](https://youtu.be/7M3gI1KLkh4?t=33)

| 假設 | 檢定 |
|---|---|
| 簡單 vs 簡單 | 一定有 MP |
| 簡單 vs 單邊（$>$ 或 $<$） | （有時）有 UMP |
| 簡單 vs 雙邊（$\ne$） | 沒有 UMP |
| $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$（或 $\ge$ vs $<$） | 會有 UMP（本集要講） |
| 一般集合 vs 集合 | 沒有 UMP 時用**概似比檢定**（likelihood ratio test） |

【口頭】[▶ 02:08](https://youtu.be/7M3gI1KLkh4?t=128) 概似比檢定還是取概似函數的比，但推導過程蠻複雜的。去修管理學院的統計學，會教很多方法，但不會講那是 UMP、MP 還是概似比檢定——其實大部分都是**概似比檢定**導出來的結果拿來用。因為推導太複雜，很多書只介紹「就這麼做」。

---

## 2. 複合假設下的 size

[▶ 03:11](https://youtu.be/7M3gI1KLkh4?t=191) 一般寫法：$H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$。

**檢定力函數**（[▶ 03:41](https://youtu.be/7M3gI1KLkh4?t=221)）：$\pi_C(\theta)=P_\theta(\mathbf X\in C)$，$\theta$ 為真時拒絕 $H_0$ 的機率。

- $\theta\in\Theta_0$：型一錯誤機率，越小越好。$\Theta_0$ 是集合，每一點都有一個型一錯誤機率。
- $\theta\in\Theta_1$：power，越大越好。

> **size**（[▶ 06:13](https://youtu.be/7M3gI1KLkh4?t=373)）：
> $$\text{size of }C=\sup_{\theta\in\Theta_0}\pi_C(\theta)$$
> ＝**型一錯誤機率的最大值**（maximum probability of type I error）。

---

## 3. UMP 檢定（一般定義）

[▶ 08:23](https://youtu.be/7M3gI1KLkh4?t=503) 想法：

1. 只考慮 size $\le\alpha$ 的拒絕域（型一錯誤最大值不能超過顯著水準）。
2. 在這裡面挑 power 最大的。
3. [▶ 11:34](https://youtu.be/7M3gI1KLkh4?t=694) 固定一個 $\theta\in\Theta_1$，power 最大的一定有（power function 有上界 1，從數學觀點有上界就有最大）。
4. [▶ 12:04](https://youtu.be/7M3gI1KLkh4?t=724) 問題是：$\Theta_1$ 每一點 power 最大的是不是**同一個**？是 ⇒ uniformly。

> **定義（size $\alpha$ 的 UMP 檢定）**（[▶ 13:05](https://youtu.be/7M3gI1KLkh4?t=785)）：拒絕域 $C$ 滿足
> 1. $\sup_{\theta\in\Theta_0}\pi_C(\theta)=\alpha$（size **剛好**是 $\alpha$）；
> 2. 對**每一個** $\theta\in\Theta_1$，以及每一個 $\sup_{\theta\in\Theta_0}\pi_{C^*}(\theta)\le\alpha$ 的拒絕域 $C^*$，
> $$\pi_C(\theta)\ge\pi_{C^*}(\theta).$$

- [▶ 14:06](https://youtu.be/7M3gI1KLkh4?t=846) 為什麼 size 要剛好 $\alpha$：比 $\alpha$ 小就一定有比它更好的。
- [▶ 15:40](https://youtu.be/7M3gI1KLkh4?t=940) 固定 $\theta$ 看第 2 條：$C$ 在 $\theta$ 的 power 最大。加上「對所有 $\theta\in\Theta_1$」：不管哪一點，最大的都是 $C$——所以叫 uniformly。

【口頭】[▶ 18:16](https://youtu.be/7M3gI1KLkh4?t=1096) 要花點時間慢慢思考這個定義。找 UMP 的理論沒那麼簡單，下面的定理要從直覺去了解。

[▶ 19:19](https://youtu.be/7M3gI1KLkh4?t=1159) $H_0$、$H_1$ 都是複合時：$H_0$ 的每一點型一錯誤都 $\le\alpha$，在這裡面 $H_1$ 每一點 power 都最大的是同一個——不容易。所以介紹一個條件，在這個條件下它會存在。

---

## 4. 單調概似比（MLR）

[▶ 20:19](https://youtu.be/7M3gI1KLkh4?t=1219) $X_1,\dots,X_n$ 來自 pdf $f(x;\theta)$；給一個 $\theta$ 就有一個 pdf，所有 pdf 構成的集合叫 **family of densities**。

[▶ 21:51](https://youtu.be/7M3gI1KLkh4?t=1311) 不知道 $\Theta_0$ 的點比 $\Theta_1$ 大還是小，所以永遠這樣取：$\theta'<\theta''$，

$$\frac{L(\theta';\mathbf x)}{L(\theta'';\mathbf x)}\qquad(\text{分子是比較小的 }\theta,\ \text{分母是比較大的 }\theta).$$

比較小的 $\theta$ 不代表就是 $H_0$。

> **定義（單調概似比，monotone likelihood ratio，MLR）**（[▶ 22:53](https://youtu.be/7M3gI1KLkh4?t=1373)；課本 Definition 8.2.2，p. 483）：若存在統計量 $T=T(X_1,\dots,X_n)$，使得對所有 $\theta'<\theta''$，
> $$\frac{L(\theta';\mathbf x)}{L(\theta'';\mathbf x)}$$
> 是 $T(\mathbf x)$ 的函數，而且這個函數是**單調**的（nondecreasing 或 nonincreasing；中間有一段是常數也沒關係），則說這個 family of densities 在 $T$ 上有 MLR。

- [▶ 21:21](https://youtu.be/7M3gI1KLkh4?t=1281) 概似比不一定 monotone。
- [▶ 24:55](https://youtu.be/7M3gI1KLkh4?t=1495) 有 MLR、假設滿足某種條件 ⇒ 有 UMP 檢定。沒有 MLR 就沒有辦法找（沒有那種理論）。
- [▶ 26:27](https://youtu.be/7M3gI1KLkh4?t=1587) 看到 $H_0$、$H_1$ 都是複合假設，先檢查有沒有 MLR。

**對照**（[▶ 25:27](https://youtu.be/7M3gI1KLkh4?t=1527)）：

- $H_0$ 一點、$H_1$ 集合：$H_1$ 任取一點就是簡單對簡單，一定有 MP；全部 MP 一樣就是 UMP。比較容易。
- $H_0$、$H_1$ 都是集合：$H_0$ 每一點都要控制型一錯誤，比較難，要靠 MLR。

---

## 5. 一頁速查表

**size**（複合 $H_0$）：$\sup_{\theta\in\Theta_0}\pi_C(\theta)$。

**UMP（size $\alpha$）**：

1. $\sup_{\Theta_0}\pi_C=\alpha$；
2. $\forall\theta\in\Theta_1$、$\forall C^*$ 使 $\sup_{\Theta_0}\pi_{C^*}\le\alpha$：$\pi_C(\theta)\ge\pi_{C^*}(\theta)$。

**MLR**：$\theta'<\theta''$，$\frac{L(\theta';\mathbf x)}{L(\theta'';\mathbf x)}=g(T(\mathbf x))$，$g$ 單調。

有 MLR ⇒ $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$ 這類單邊複合假設有 UMP（下一集）。沒有 UMP ⇒ 概似比檢定。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| MLR | 下一集：MLR 定理、UMP 拒絕域 $T\ge c$ 或 $T\le c$ |
| 概似比檢定 | 之後介紹 |

---

## 附：本集一句話總結

> **$H_0$ 是集合時，size 是 $H_0$ 上型一錯誤的最大值；UMP 檢定是 size 剛好 $\alpha$、且在 $H_1$ 每一點都比所有 size $\le\alpha$ 的檢定 power 大的那個；兩邊都是複合假設時要靠單調概似比（概似比 $L(\theta')/L(\theta'')$ 是某統計量 $T$ 的單調函數）才能找到 UMP。**

---

*筆記依據「高等統計學」Lec16 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
