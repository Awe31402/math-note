---
course: 高等統計學（數理統計續）
episode: 12
lecture: Lec12（第七週 1/2）
date: 待補
video: https://youtu.be/bXx3koFTgyE
notes: Hogg 8th ed. §8.1 最強力檢定；Theorem 8.1.1 Neyman–Pearson（p. 472）；概似函數 §6.1
---

# 第 12 集 · 第七週 (1/2)：最強力檢定再解釋；概似函數與概似比；Neyman–Pearson 定理（敘述） [▶ 影片](https://youtu.be/bXx3koFTgyE)

← 上一集：[11](11-size-significance-level-most-powerful-test.md) ｜ [總目錄](../README.md) ｜ 下一集：[13](13-neyman-pearson-proof-normal-mean-example.md) →

> **課程**：高等統計學（接續上學期「統計學」）— 第 12 集
> **講者**：待補
> **來源**：YouTube 錄影逐字稿（約 29 分鐘，whisper large-v3-turbo）＋ Hogg《Introduction to Mathematical Statistics》8th ed. §6.1、§8.1
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `⚠️ 逐字稿缺字` 字幕聽錯；寫出原字幕和修正

> ⚠️ 逐字稿缺字（整集通用）：「likelihood function」→「Likely／Ligrid／Lugly Function」，「likelihood ratio」→「likely ratio／Lock Ratio」，「significance level」→「Skinemic Level」，「Lehmann–Scheffé」→「Lehmann Suffer」，「Neyman–Pearson」→「Neiman-Pearson」，「joint pdf」→「Join PDM」。以下一律用正確的字。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 再看最強力檢定](#1-再看最強力檢定)
- [2. 概似函數](#2-概似函數)
- [3. 概似比](#3-概似比)
- [4. 直覺：比值大就相信 θ₀](#4-直覺比值大就相信-θ₀)
- [5. Neyman–Pearson 定理](#5-neymanpearson-定理)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | 課本 |
|---|---|
| 最強力拒絕域：型一＝$\alpha$、型二最小 | §8.1 |
| 概似函數 $L(\theta;\mathbf x)$、概似比 | §6.1、§8.1 |
| Neyman–Pearson 定理 | Theorem 8.1.1 |

---

## 1. 再看最強力檢定

[▶ 00:31](https://youtu.be/bXx3koFTgyE?t=31) $H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$：其實只有兩個選擇。把「對卻被拒絕比較嚴重」的放 $H_0$。

[▶ 02:09](https://youtu.be/bXx3koFTgyE?t=129) **level $\alpha$**＝顯著水準：型一錯誤不可能不發生，那就讓它的機率 $\le\alpha$。

[▶ 04:12](https://youtu.be/bXx3koFTgyE?t=252) size $\alpha$ 的最強力拒絕域 $C$：

1. $\pi_C(\theta_0)=P_{\theta_0}(\mathbf X\in C)=\alpha$（型一錯誤剛好 $\alpha$）；
2. 對每個 $\pi_A(\theta_0)\le\alpha$ 的 $A$：$\pi_C(\theta_1)\ge\pi_A(\theta_1)$。

[▶ 05:45](https://youtu.be/bXx3koFTgyE?t=345) 第 2 條等價於（兩邊用 1 減）：
$$P_{\theta_1}(\mathbf X\notin C)\le P_{\theta_1}(\mathbf X\notin A).$$
$H_1$ 對、樣本沒落在 $C$ ⇒ 不拒絕 $H_0$ ⇒ **型二錯誤**。所以 $C$ 的型二錯誤機率最小。power 最大＝型二錯誤最小，所以叫 most powerful。

---

## 2. 概似函數

[▶ 08:22](https://youtu.be/bXx3koFTgyE?t=502) $X_1,\dots,X_n$ 是隨機樣本，pdf $f(x;\theta)$。iid ⇒ joint pdf 是個別 pdf 相乘（獨立），而且是**同一個**函數（同分配）：
$$f(x_1,\dots,x_n;\theta)=\prod_{i=1}^nf(x_i;\theta).$$

- [▶ 09:54](https://youtu.be/bXx3koFTgyE?t=594) 看成 **joint pdf** 時：$\theta$ 固定，是 $x_1,\dots,x_n$ 的函數，$\int\cdots\int f\,dx_1\cdots dx_n=1$。
- [▶ 10:54](https://youtu.be/bXx3koFTgyE?t=654) 看成 **概似函數**（likelihood function）時：$x_1,\dots,x_n$ 給定，是 $\theta$ 的函數，寫成
$$L(\theta;x_1,\dots,x_n)=\prod_{i=1}^nf(x_i;\theta).$$

[▶ 12:31](https://youtu.be/bXx3koFTgyE?t=751) 給一個 $\theta$ 就得一個值，叫在 $\theta$ 的**概似值**（likelihood at $\theta$）。

---

## 3. 概似比

[▶ 13:01](https://youtu.be/bXx3koFTgyE?t=781) 現在只有 $\theta_0$、$\theta_1$ 兩個值，各有一個概似值。相除：

> **概似比**（likelihood ratio）：
> $$\frac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}.$$

【口頭】[▶ 14:03](https://youtu.be/bXx3koFTgyE?t=843) 任何統計領域要找最好的東西，最後一定靠一個關鍵量。點估計找 UMVUE 靠**充分**統計量，還要**完備**——Lehmann–Scheffé 定理：充分完備統計量的函數只要不偏就是 UMVUE。假設檢定找最好的拒絕域，靠的就是概似比。

[▶ 15:35](https://youtu.be/bXx3koFTgyE?t=935) 拒絕域是樣本空間的子集。找最好的拒絕域＝找一個**規則**：樣本點滿足什麼條件就放進 $C$，不滿足就不放。

---

## 4. 直覺：比值大就相信 θ₀

[▶ 18:10](https://youtu.be/bXx3koFTgyE?t=1090) 概似函數還是 pdf，可以想成：

- 分子 $L(\theta_0;\mathbf x)$：$\theta_0$ 對時，發生 $\mathbf x$ 這一點的「機率」；
- 分母 $L(\theta_1;\mathbf x)$：$\theta_1$ 對時，發生這一點的「機率」。

$\mathbf x$ 已經發生了：

| 比值 | 意思 | 決定 |
|---|---|---|
| **大** | $\theta_0$ 對時發生它的機會比較大 → 相信 $\theta_0$ | **不放進** $C$（不拒絕 $H_0$） |
| **小** | $\theta_1$ 對時發生它的機會比較大 → 相信 $\theta_1$ | **放進** $C$（拒絕 $H_0$） |

[▶ 24:56](https://youtu.be/bXx3koFTgyE?t=1496) 問題只剩：多小才放進去？由**型一錯誤**（顯著水準）決定。

【口頭】[▶ 22:22](https://youtu.be/bXx3koFTgyE?t=1342) 不管讀哪一門科學，理論一定要跟直覺很接近。直覺不是這樣，要嘛理論有問題；理論沒問題，就是直覺要改。最後一定要對理論有感覺。

---

## 5. Neyman–Pearson 定理

[▶ 25:26](https://youtu.be/bXx3koFTgyE?t=1526) 由 Neyman 和 Pearson 兩人證明，跟上面的直覺一模一樣。

> **Neyman–Pearson 定理**（課本 Theorem 8.1.1，p. 472）：$H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$。設 $k>0$，拒絕域
> $$C=\left\{\mathbf x:\frac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}\le k\right\},$$
> 而且 $k$ 選得使
> $$P_{\theta_0}(\mathbf X\in C)=\alpha.$$
> 則 $C$ 是 size $\alpha$ 的**最強力拒絕域**。

- [▶ 26:27](https://youtu.be/bXx3koFTgyE?t=1587) 比值 $\le k$ 的點全放進來，$>k$ 的都不要。
- [▶ 26:58](https://youtu.be/bXx3koFTgyE?t=1618) 不同的 $k$ 給不同的 $C$；選那個讓「$H_0$ 對時拒絕 $H_0$ 的機率剛好是 $\alpha$」的 $k$。

【課本補充】課本的敘述是：$C$ 內 $\frac{L(\theta_0)}{L(\theta_1)}\le k$、$C$ 外 $\ge k$，加上 $\alpha=P_{H_0}(\mathbf X\in C)$。課堂寫的集合形式與此一致。

證明下一次講。

---

## 6. 一頁速查表

**最強力拒絕域**（$\theta_0$ vs $\theta_1$）：$\pi_C(\theta_0)=\alpha$，且型二錯誤 $P_{\theta_1}(\mathbf X\notin C)$ 在所有 size $\le\alpha$ 的拒絕域中最小。

**概似函數**：$L(\theta;\mathbf x)=\prod f(x_i;\theta)$——joint pdf 看成 $\theta$ 的函數。

**概似比**：$\dfrac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}$。小 → 樣本比較像 $\theta_1$ 產生的 → 拒絕 $H_0$。

**Neyman–Pearson**：
$$C=\left\{\mathbf x:\frac{L(\theta_0;\mathbf x)}{L(\theta_1;\mathbf x)}\le k\right\},\quad P_{\theta_0}(\mathbf X\in C)=\alpha\ \Rightarrow\ C\text{ 是 size }\alpha\text{ 的最強力拒絕域}.$$

類比：點估計靠充分完備統計量（Lehmann–Scheffé）；檢定靠概似比（Neyman–Pearson）。

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Neyman–Pearson 定理 | 下一集：證明與例子 |
| 概似比 | 一致最強力檢定、概似比檢定 |

---

## 附：本集一句話總結

> **把 joint pdf 看成 $\theta$ 的函數就是概似函數；概似比 $L(\theta_0)/L(\theta_1)$ 小代表樣本比較像 $H_1$ 產生的，該拒絕 $H_0$；Neyman–Pearson 定理說，把比值 $\le k$ 的點都放進拒絕域、$k$ 選到型一錯誤剛好 $\alpha$，就得到最強力檢定。**

---

*筆記依據「高等統計學」Lec12 錄影逐字稿（whisper large-v3-turbo）與 Hogg, McKean & Craig《Introduction to Mathematical Statistics》8th ed. 整理。*
