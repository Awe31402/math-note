---
course: 高等統計學（數理統計續）
episode: 14
lecture: Lec14（第八週 1/2）
date: 待補
video: https://youtu.be/vctLnl7fsyw
notes: Hogg 8th ed. §8.1 Neyman–Pearson 例題；§8.2 Definition 8.2.1 一致最強力檢定（UMP，p. 479）
---

# 第 14 集 · 第八週 (1/2)：例：Poisson 的最強力檢定；一致最強力檢定（UMP）的定義 [▶ 影片](https://youtu.be/vctLnl7fsyw)

← 上一集：[13](13-neyman-pearson-proof-normal-mean-example.md) ｜ [總目錄](../README.md) ｜ 下一集：[15](15-ump-examples-normal-mean-variance-poisson-two-sided.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 14 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 26 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §8.1、§8.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「Poisson」→「普阿松／普哈松」，「Neyman–Pearson」→「雷曼·比爾審／聯門 Person／流氓標準」，「composite hypothesis」→「Compositive Hyphasis」，「uniformly」→「uniforme」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 例：Poisson，H₀:λ=10 vs H₁:λ=1](#1-例poissonh₀λ10-vs-h₁λ1)
- [2. 簡單對簡單：最強力檢定永遠存在](#2-簡單對簡單最強力檢定永遠存在)
- [3. H₁ 是集合時：什麼叫最好](#3-h₁-是集合時什麼叫最好)
- [4. 一致最強力檢定（UMP）](#4-一致最強力檢定ump)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| Poisson 的最強力拒絕域 | §8.1 |
| 一致最強力檢定（UMP） | Definition 8.2.1，p. 479 |

---

## 1. 例：Poisson，H₀:λ=10 vs H₁:λ=1

[▶ 00:31](https://youtu.be/vctLnl7fsyw?t=31) $X_1,\dots,X_n$ iid Poisson$(\lambda)$。
$$H_0:\lambda=10\quad\text{vs}\quad H_1:\lambda=1.$$
兩個都是簡單假設，所以有最強力檢定，照 Neyman–Pearson 做。

**概似函數**（[▶ 02:33](https://youtu.be/vctLnl7fsyw?t=153)）：
$$L(\lambda;\mathbf x)=\prod_{i=1}^n\frac{\lambda^{x_i}e^{-\lambda}}{x_i!}=\frac{\lambda^{\sum x_i}e^{-n\lambda}}{\prod x_i!}.$$

**概似比**（[▶ 03:03](https://youtu.be/vctLnl7fsyw?t=183)）：
$$\frac{L(10;\mathbf x)}{L(1;\mathbf x)}=\frac{10^{\sum x_i}e^{-10n}}{1^{\sum x_i}e^{-n}}=10^{\sum x_i}e^{-9n}\le k.$$

[▶ 04:05](https://youtu.be/vctLnl7fsyw?t=245) 理論上這個集合就是最強力拒絕域，但 $k$ 要滿足
$$P_{\lambda=10}\left(10^{\sum X_i}e^{-9n}\le k\right)=\alpha,$$
不知道這個量的分配，**不好找**。（寫成機率時 $x_i$ 要改成大寫 $X_i$，才是隨機變數。）

**一對一轉換**（[▶ 06:39](https://youtu.be/vctLnl7fsyw?t=399)）：

1. 取 $\log$：$\left(\sum x_i\right)\log 10-9n\le\log k$。
2. 移項，除以 $\log 10>0$（不等號不變）：
$$\sum x_i\le\frac{\log k+9n}{\log 10}\equiv c.$$

[▶ 07:40](https://youtu.be/vctLnl7fsyw?t=460) 為什麼轉到 $\sum x_i$：獨立 Poisson 相加還是 Poisson，**分配知道**。

> **最強力拒絕域**（[▶ 09:11](https://youtu.be/vctLnl7fsyw?t=551)）：$C=\left\{\mathbf x:\sum x_i\le c\right\}$。$\sum x_i\le c$ 就拒絕 $H_0$。

**找 $c$**（[▶ 09:41](https://youtu.be/vctLnl7fsyw?t=581)）：令 $Y=\sum X_i\sim$ Poisson$(n\lambda)$；$H_0$ 為真時 $Y\sim$ Poisson$(10n)$。
$$\alpha=P_{\lambda=10}(Y\le c)=\sum_{y=0}^{c}\frac{(10n)^ye^{-10n}}{y!}.$$
[▶ 11:13](https://youtu.be/vctLnl7fsyw?t=673) 知道 $n$ 就用電腦從 0 開始加，加到等於 $\alpha$ 的那個 $c$ 就是答案。

以下不是逐字稿內容，是依 Poisson 是離散分配推論的：累加和是跳著增加的，不一定剛好有 $c$ 使和**恰好**等於 $\alpha$；這種情況通常只能選一個 size 接近 $\alpha$ 的 $c$（或用隨機化檢定），課堂沒有討論。

[▶ 11:43](https://youtu.be/vctLnl7fsyw?t=703) 不同問題都是這種解法：一對一轉換到**分配已知**的統計量。萬一不知道，就用以前教過的**變數轉換**把分配找出來。

---

## 2. 簡單對簡單：最強力檢定永遠存在

[▶ 12:48](https://youtu.be/vctLnl7fsyw?t=768) $H_0$、$H_1$ 都是簡單假設 ⇒ 由 Neyman–Pearson，最強力檢定**永遠存在**，拒絕域就是「概似比 $\le k$」，$k$ 使型一錯誤 $=\alpha$。

---

## 3. H₁ 是集合時：什麼叫最好

[▶ 14:24](https://youtu.be/vctLnl7fsyw?t=864) 現在 $H_0:\theta=\theta_0$（一點），$H_1:\theta\in\Theta_1$（一個集合）。這時最好的檢定不應該叫 MP（MP 專指簡單對簡單）。

【口頭】[▶ 15:24](https://youtu.be/vctLnl7fsyw?t=924) 班上 50 個同學都修 A、B、C、D、E 五門課。

- 每門課**一定有**第一名（成績在 0 到 100，一定有最大值）——就像 Neyman–Pearson 保證每個簡單假設都有最好的。
- 五門課的第一名如果是不同人，誰是第一名？
- 取平均當然也有第一名，但那是統計另一個領域：**Bayesian**。
- [▶ 16:56](https://youtu.be/vctLnl7fsyw?t=1016) 這裡關心的是：五門課的第一名**是不是同一個人**？是的話，他就是 **uniformly** 的第一名。

**類比 UMVUE**（[▶ 17:27](https://youtu.be/vctLnl7fsyw?t=1047)）：對每一個 $\theta$，變異數最小的不偏估計量一定有；問題是每個 $\theta$ 得到的是不是同一個。是的話叫 UMVUE。UMVUE 不一定存在：充分完備統計量不一定有，有了它的不偏函數也不一定找得到。

**H₁ 兩點的例子**（[▶ 18:30](https://youtu.be/vctLnl7fsyw?t=1110)）：$H_0:\theta=\theta_0$，$H_1:\theta\in\{\theta_1,\theta_2\}$（複合假設）。

- $H_0:\theta_0$ vs $H_1:\theta_1$：最強力拒絕域
$$C_1=\left\{\mathbf x:\frac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}\le k_1\right\},\quad P_{\theta_0}(\mathbf X\in C_1)=\alpha.$$
- $H_0:\theta_0$ vs $H_1:\theta_2$：最強力拒絕域
$$C_2=\left\{\mathbf x:\frac{L(\theta_0;\mathbf x)}{L(\theta_2;\mathbf x)}\le k_2\right\},\quad P_{\theta_0}(\mathbf X\in C_2)=\alpha.$$

[▶ 21:04](https://youtu.be/vctLnl7fsyw?t=1264) $k_1$、$k_2$ 通常不一樣，但集合 $C_1$、$C_2$ **可能相等**（因為都是由 $\theta_0$ 為真時的型一錯誤決定）。

- 相等 ⇒ 叫這個共同的 $C$ 為**一致最強力**（uniformly most powerful，UMP）拒絕域：不管對立假設取哪一點，它都是最強力的。
- [▶ 22:35](https://youtu.be/vctLnl7fsyw?t=1355) 不相等 ⇒ UMP 拒絕域**不存在**（像有兩門課第一名不是同一人，就沒有 uniform 的第一名）。

---

## 4. 一致最強力檢定（UMP）

> **定義**（[▶ 23:38](https://youtu.be/vctLnl7fsyw?t=1418)；課本 Definition 8.2.1，p. 479）：考慮 $H_0:\theta=\theta_0$ vs $H_1:\theta\in\Theta_1$。拒絕域 $C$ 叫 size $\alpha$ 的**一致最強力**（UMP）拒絕域，如果對**每一個** $\theta_1\in\Theta_1$，$C$ 都是
> $$H_0:\theta=\theta_0\quad\text{vs}\quad H_1:\theta=\theta_1$$
> 的 size $\alpha$ 最強力拒絕域。對應的檢定叫 UMP 檢定。

[▶ 25:12](https://youtu.be/vctLnl7fsyw?t=1512) 做法：對立假設的每一點都拿出來，各做一個簡單對簡單、各找最強力拒絕域（一定存在）。

- 不管取哪一點答案都是同一個 ⇒ 它就是 UMP。
- 有兩點答案不一樣 ⇒ UMP 不存在。

例子下一次講。

---

## 5. 一頁速查表

**Poisson**（$H_0:\lambda=10$ vs $H_1:\lambda=1$）：
$$\frac{L(10)}{L(1)}=10^{\sum x_i}e^{-9n}\le k\iff\sum x_i\le c,\qquad\sum_{y=0}^{c}\frac{(10n)^ye^{-10n}}{y!}=\alpha.$$
關鍵：$\sum X_i\sim$ Poisson$(n\lambda)$。

**找最強力拒絕域的步驟**：

1. 寫概似函數。
2. 概似比 $\frac{L(\theta_0)}{L(\theta_1)}\le k$，化簡。
3. 一對一轉換到分配已知的統計量 $u(\mathbf x)\le c$ 或 $\ge c$。
4. 用 $P_{\theta_0}=\alpha$ 解 $c$。

**MP vs UMP**

| | 假設 | 存在嗎 |
|---|---|---|
| MP | 簡單 vs 簡單 | 永遠存在（Neyman–Pearson） |
| UMP | 簡單 vs 複合 | 對每個 $\theta_1\in\Theta_1$ 的 MP 拒絕域都一樣才存在 |

類比：每門課都有第一名（MP）；五門課是同一人才有 uniform 第一名（UMP）。同理 UMVUE。

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| UMP 定義 | 下一集：UMP 存在與不存在的例子 |
| 一對一轉換到已知分配 | 所有 Neyman–Pearson 類型題目 |

---

## 附：本集一句話總結

> **Poisson 例中，概似比 $10^{\sum x_i}e^{-9n}\le k$ 一對一轉成 $\sum x_i\le c$，再用 $\sum X_i\sim$ Poisson$(10n)$ 定出 $c$；簡單對簡單永遠有最強力檢定，而當 $H_1$ 是集合時，若對每個 $\theta_1\in\Theta_1$ 的最強力拒絕域都相同，它就叫一致最強力（UMP）檢定，否則 UMP 不存在。**

---

*筆記依據「高等統計學」Lec14 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
