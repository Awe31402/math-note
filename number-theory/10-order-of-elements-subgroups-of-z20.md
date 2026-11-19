---
course: Number Theory（2021 秋，線上錄影）
episode: 10
lecture: 2021-08-31 第 2 部
date: 2021-08-31
video: https://youtu.be/qdbZCjSL4UM
notes: Jones & Jones《Elementary Number Theory》附錄 B：陪集、Lagrange 定理、元素的階、循環群的子群、直積（書頁 244，PDF 頁 259）；§5.2 φ 的數值表（書頁 85，PDF 頁 100）
---

# 第 10 集 · 元素的階、Z₂₀ 的循環子群（Order of Elements, Unique Cyclic Subgroups of Z₂₀） [▶ 影片](https://youtu.be/qdbZCjSL4UM)

← 上一集：[09-review-of-groups-cyclic-groups](09-review-of-groups-cyclic-groups.md) ｜ [總目錄](README.md) ｜ 下一集：[11-cyclic-groups-short-course-2](11-cyclic-groups-short-course-2.md) →

> **課程**：Number Theory（線上課，2021 秋）— 第 10 集（2021-08-31 第 2 部，接第 9 集）
> **講者**：James S. Cook（Liberty University）
> **來源**：YouTube 錄影逐字稿（24:23，whisper 轉錄）＋ Jones & Jones《Elementary Number Theory》附錄 B、§5.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` 課本有、課堂沒講
> - `【Q&A】` 學生主動提問與回答

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. Lagrange 定理](#1-lagrange-定理)
- [2. 元素的階](#2-元素的階)
- [3. 應用：Z₅₀₀ 沒有 11 階元素](#3-應用z-沒有-11-階元素)
- [4. 循環群與它的生成元](#4-循環群與它的生成元)
- [5. 循環群基本定理](#5-循環群基本定理)
- [6. 例子：Z₂₀ 的所有子群](#6-例子z-的所有子群)
- [7. 預告：φ 的乘性、U_n 的結構](#7-預告φ-的乘性u_n-的結構)
- [8. 一頁速查表](#8-一頁速查表)
- [9. 與後續集數的連結](#9-與後續集數的連結)

---

## 0. 這堂課要做什麼

講者剩約 15 分鐘，說這段「先陳述不證明」，下次再回來證。（下一部影片是兩週多以後的 9-18-21，見第 11 集。）

| 主題 | 時間 | 課本 |
|---|---|---|
| Lagrange 定理 | 00:44 | 附錄 B |
| 元素的階 | 01:47 | 附錄 B |
| $\mathbb{Z}_{500}$ 的例子 | 03:56 | — |
| 循環群的生成元 | 06:51 | — |
| 循環群基本定理 | 14:12 | 附錄 B |
| $\mathbb{Z}_{20}$ 的子群 | 17:20 | — |
| $\varphi$ 的乘性（預告） | 17:53 | — |

---

## 1. Lagrange 定理

[▶ 00:44](https://youtu.be/qdbZCjSL4UM?t=44)

> **Lagrange 定理**：若 $H\le G$ 且 $|G|<\infty$，則
> $$|H|\ \text{整除}\ |G|.$$

講者說 Stillwell 有證明，希望下堂課講。

> 【課本補充】附錄 B（p. 244）的證明想法：
> - $H$ 的**右陪集**（right coset）$Hg = \{hg : h\in H\}$。每個右陪集都有 $|H|$ 個元素。
> - 兩個右陪集要嘛相等、要嘛不相交，所以它們把 $G$ **分割**成互不相交的子集合。
> - 陪集的個數叫 $H$ 在 $G$ 中的**指數**（index）$|G:H|$。
> - **關鍵一步**：$G$ 被切成 $|G:H|$ 塊、每塊 $|H|$ 個，所以 $|G| = |G:H|\cdot|H|$，$|H|$ 整除 $|G|$。

---

## 2. 元素的階

[▶ 01:47](https://youtu.be/qdbZCjSL4UM?t=107)

講者先寫「$a$ 的階 = $\langle a\rangle$ 的階」當定義，馬上說「我寫錯了，這其實是定理」。

> **定義**：$a\in G$ 的**階**（order）$|a|$ 是使 $a^n = e$ 的**最小正整數** $n$。若沒有這樣的 $n$，就說 $|a|=\infty$。

講者的說法是「$a^n=1$ 但 $a^{n-1}\neq 1$」。嚴格說要「$a^m\neq 1$ 對所有 $0<m<n$」，也就是 $n$ 是**最小的**。（這一句**不是逐字稿內容**，是補上定義的精確寫法。）

白話：把元素一直乘自己，**第一次回到單位元素**是第幾次。

- 有些無限群裡的元素永遠回不去，例如 $\mathbb{Z}$ 裡的 $1$：$1,2,3,\dots$ 永遠不會是 $0$。

> **定理** [▶ 02:53](https://youtu.be/qdbZCjSL4UM?t=173)：$|a| = |\langle a\rangle|$。元素的階 = 它生成的子群的大小。

> **推論** [▶ 03:26](https://youtu.be/qdbZCjSL4UM?t=206)：若 $|G|=n$、$a\in G$，則 $|a|$ 整除 $|G|$。

**證明**：$\langle a\rangle$ 是子群（第 9 集），由 Lagrange，$|\langle a\rangle|$ 整除 $|G|$；而 $|a| = |\langle a\rangle|$。

> 【課本補充】附錄 B（p. 244）：若 $G$ 有限，每個 $g$ 都有有限的階 $n$；$g,g^2,\dots,g^{n-1},g^n(=1)$ 組成一個子群，由 Lagrange 定理 $n$ 整除 $|G|$。

---

## 3. 應用：Z₅₀₀ 沒有 11 階元素

[▶ 03:56](https://youtu.be/qdbZCjSL4UM?t=236)

> **例子**：$\mathbb{Z}_{500}$ 裡**沒有**階為 $11$ 的元素。

**證明**：

1. 假設 $|x| = 11$。則 $\langle x\rangle$ 是 11 個元素的子群。
2. 由 Lagrange，$11$ 整除 $|\mathbb{Z}_{500}| = 500$。
3. 但 $11\nmid 500$。矛盾。

【口頭】「11 整除 500，這不是你在商店能買到的真理。你得重新定義 11 和 500 的意思才行。」

**反過來呢？** [▶ 05:40](https://youtu.be/qdbZCjSL4UM?t=340) 有沒有 50 階的元素？學生說：$50\mid 500$，所以可能。講者：對，「目前我們手上的定理還沒說一定有，但其實有」——見第 5 節（$\mathbb{Z}_{500}$ 是循環群）。

---

## 4. 循環群與它的生成元

[▶ 06:51](https://youtu.be/qdbZCjSL4UM?t=411)

> **定義**：若存在 $a\in G$ 使 $G = \langle a\rangle$，就說 $G$ 是**循環群**（cyclic group），$a$ 是**生成元**（generator）。

例如 $\mathbb{Z}_n = \langle 1\rangle$ 是循環群。

**$a$ 是生成元的話，還有誰是生成元？** [▶ 07:21](https://youtu.be/qdbZCjSL4UM?t=441)

> **定理** [▶ 08:14](https://youtu.be/qdbZCjSL4UM?t=494)：若 $G = \langle a\rangle$，$|G| = n<\infty$，且 $\gcd(n,k)=1$，則
> $$G = \langle a^k\rangle.$$

白話：**跟 $n$ 互質的次方 $a^k$ 也是生成元。**

講者說這些「完全在我們能力範圍內，沒有比之前做過的更難」，下次有時間會證。

**例子** [▶ 09:27](https://youtu.be/qdbZCjSL4UM?t=567)：$G = \langle a\rangle$，$|G| = 10$。$1$ 到 $9$ 裡跟 $10$ 互質的：

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $\gcd(k,10)=1$？ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |

所以
$$G = \langle a\rangle = \langle a^3\rangle = \langle a^7\rangle = \langle a^9\rangle.$$

> **推論** [▶ 11:07](https://youtu.be/qdbZCjSL4UM?t=667)：循環群 $G$ 的生成元個數是 $\varphi(|G|)$。

（$\varphi(10)=4$，正好是上面 4 個。）

【口頭】作業有幾題是根據這種計數。

**例子** [▶ 12:38](https://youtu.be/qdbZCjSL4UM?t=758)：若 $H\le G$ 是**循環**子群、$|H|=8$，則 $H$ 有 $\varphi(8)=4$ 個生成元。

講者特別補上「循環」：**不是每個群都是循環群**。不是循環群就不能用一個元素生成。

---

## 5. 循環群基本定理

[▶ 14:12](https://youtu.be/qdbZCjSL4UM?t=852)

> **循環群基本定理**（fundamental theorem of cyclic groups，講者說「有些人這樣叫」）：$G$ 是循環群、$|G|=n$。
> 1. 若 $k\mid n$，則 $G$ 有**唯一**一個 $k$ 階子群。
> 2. 循環群的每個子群都是循環群。
> 3. 具體公式 [▶ 16:19](https://youtu.be/qdbZCjSL4UM?t=979)：若 $G=\langle a\rangle$，那個 $k$ 階子群是
>    $$H = \langle a^{n/k}\rangle.$$
>    （$k\mid n$，所以 $n/k$ 是整數。）加法記號下是 $\langle (n/k)\,a\rangle$。

**這是 Lagrange 定理的部分逆命題** [▶ 15:19](https://youtu.be/qdbZCjSL4UM?t=919)：

- Lagrange：子群的階一定整除群的階。
- 反過來，「$k$ 整除 $|G|$ ⇒ 有 $k$ 階子群」，**一般的群不一定對**，但**循環群一定對**。

【口頭】講者說：「如果 20 整除一個（可能不交換的）抽象群的階，不一定有 20 階子群。」他本來想用 3 舉例，又說「3 可能太小會碰到特殊情況」，「請原諒我的無知，我懂的群論不夠多，沒辦法把這講得很清楚」。

> 【課本補充】附錄 B（p. 244）：循環群 $G$ 有生成元 $c$；若 $c$ 的階是 $n$，則 $|G|=n$，記作 $C_n$。**$C_n$ 對每個整除 $n$ 的 $m$ 恰有一個 $m$ 階子群，而且沒有別的子群**；那個子群是循環群，生成元是 $c^{n/m}$。跟講者的公式一致。

---

## 6. 例子：Z₂₀ 的所有子群

[▶ 17:20](https://youtu.be/qdbZCjSL4UM?t=1040)

（回答第 9 集學生的問題：$\mathbb{Z}_n$ 的循環子群有哪些？）

$\mathbb{Z}_{20} = \langle 1\rangle$，加法群。

**生成元有幾個？** $\varphi(20)$。講者用下一節的乘性公式：$\varphi(20) = \varphi(5)\varphi(4) = 4\cdot 2 = 8$。所以有 8 個生成元。

> 以下**不是逐字稿內容**，是把 8 個生成元列出來：跟 20 互質的 $1,3,7,9,11,13,17,19$。

**子群** [▶ 18:53](https://youtu.be/qdbZCjSL4UM?t=1133)：20 的正因數是 $1,2,4,5,10,20$。（字幕裡講者多唸了一個 12，$12\nmid 20$，不算。）

對每個因數 $k$，唯一的 $k$ 階子群是 $\langle 20/k\rangle$：

| 階 $k$ | 生成元 $20/k$ | 子群 | 同構於 |
|---|---|---|---|
| 1 | $20\equiv 0$ | $\{0\}$ | 平凡群 |
| 2 | $10$ | $\{0,10\}$ | $\mathbb{Z}_2$ |
| 4 | $5$ | $\{0,5,10,15\}$ | $\mathbb{Z}_4$ |
| 5 | $4$ | $\{0,4,8,12,16\}$ | $\mathbb{Z}_5$ |
| 10 | $2$ | $\{0,2,4,\dots,18\}$ | $\mathbb{Z}_{10}$ |
| 20 | $1$ | $\mathbb{Z}_{20}$ | $\mathbb{Z}_{20}$ |

由第 5 節，**這就是 $\mathbb{Z}_{20}$ 的全部子群**。

- 【口頭】$\langle 20\rangle = \{0\}$ 「是很蠢的那個，就是平凡的加法子群」。
- 【Q&A】[▶ 21:05](https://youtu.be/qdbZCjSL4UM?t=1265) 學生問：為什麼 $\langle 4\rangle$ 不寫到 20？講者：因為用 $0$ 到 $19$ 當代表元，$20\equiv 0$。
- [▶ 22:06](https://youtu.be/qdbZCjSL4UM?t=1326) 每個子群都是循環群，而**同階的循環群在同構意義下只有一個**。所以 2 階子群同構於 $\mathbb{Z}_2$，4 階的同構於 $\mathbb{Z}_4$，等等。
- 【Q&A】學生問：所以 $\{0,5,10,15\}$ 這種本身也有子群？講者說對，它們是循環群，例如 $\{0,5,10,15\}\cong\mathbb{Z}_4$。

---

## 7. 預告：φ 的乘性、U_n 的結構

[▶ 17:53](https://youtu.be/qdbZCjSL4UM?t=1073)

> **定理**（下次證明）：若 $m,n$ 互質，則
> $$\varphi(mn) = \varphi(m)\,\varphi(n).$$

**原因**：$U_{mn}$ 同構於 **直積**（direct product）$U_m\times U_n$。要講清楚，得先談**同構**和**群的直積**。

（講者口誤說「$U_m\times U_m$」，應是 $U_m\times U_n$。）

> 【課本補充】附錄 B（p. 244）：
> - **直積** $G_1\times G_2$：所有有序對 $(g_1,g_2)$，運算是分量各自算 $(g_1,g_2)(h_1,h_2) = (g_1h_1,\ g_2h_2)$。
> - **同構**（isomorphism）：一對一且映成、滿足 $\theta(gh)=\theta(g)\theta(h)$ 的函數。同構的兩個群「結構一樣，只是元素的記號不同」，寫 $G\cong G'$。
> - 若 $m,n$ 互質，則 $C_m\times C_n\cong C_{mn}$：$c_1,c_2$ 分別生成 $C_m,C_n$，則 $(c_1,c_2)$ 的階是 $mn$，生成整個直積。

**$U_n$ 是循環群嗎？** [▶ 22:36](https://youtu.be/qdbZCjSL4UM?t=1356) 講者：**有時候是**。$U_n$ 是交換群，而**有限生成交換群基本定理**（fundamental theorem of finitely generated abelian groups）說：每個（有限）交換群在同構意義下都是一些 $\mathbb{Z}_n$ 的直積。下次再講。

【口頭】講者說他主要是想幫大家複習群論，「（抽象代數）學期結束有一陣子了」（字幕原文是「kind of the end of the semester」，現在才 8 月底，應是指大家修完抽象代數一段時間了），「考 GRE 數學科目考或修研究所抽象代數前，這些都該會」。

---

## 8. 一頁速查表

**Lagrange**：$H\le G$、$G$ 有限 ⇒ $|H|$ 整除 $|G|$。**關鍵一步**：陪集把 $G$ 切成大小都是 $|H|$ 的塊。

**元素的階** $|a|$：使 $a^n=e$ 的最小正整數。$|a|=|\langle a\rangle|$，所以 $|a|$ 整除 $|G|$。

- 例：$\mathbb{Z}_{500}$ 沒有 11 階元素（$11\nmid500$）。

**循環群** $G=\langle a\rangle$，$|G|=n$：

- $\gcd(k,n)=1$ ⇒ $a^k$ 也是生成元。生成元共 $\varphi(n)$ 個。
- 例：$|G|=10$ ⇒ 生成元 $a,a^3,a^7,a^9$。

**循環群基本定理**：$k\mid n$ ⇒ 恰有一個 $k$ 階子群 $\langle a^{n/k}\rangle$；所有子群都是循環群。

- 一般的群：$k\mid|G|$ 不保證有 $k$ 階子群。

**$\mathbb{Z}_{20}$ 的子群**：$\langle 0\rangle,\langle10\rangle,\langle5\rangle,\langle4\rangle,\langle2\rangle,\langle1\rangle$，階 $1,2,4,5,10,20$。生成元 8 個：$1,3,7,9,11,13,17,19$。

**預告**：$\gcd(m,n)=1$ ⇒ $\varphi(mn)=\varphi(m)\varphi(n)$，因為 $U_{mn}\cong U_m\times U_n$。

---

## 9. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| Lagrange 定理的證明、生成元定理的證明 | 第 11 集 |
| $U_{mn}\cong U_m\times U_n$、$\varphi$ 的乘性 | 第 11–12 集 |
| $U_n$ 什麼時候是循環群 | 第 12 集 |
| $|a|$ 整除 $|G|$ ⇒ Euler 定理 $a^{\varphi(n)}\equiv1$ | 第 12–13 集 |
| 群論知識用在 RSA | 第 13–14 集 |
| 有限生成交換群基本定理 | 第 12 集 |

---

## 附：本集一句話總結

> **Lagrange 定理說子群的階整除群的階，所以元素的階也整除群的階。循環群更好：和 $n$ 互質的次方都是生成元（共 $\varphi(n)$ 個），而且每個因數 $k$ 恰好對應一個 $k$ 階子群 $\langle a^{n/k}\rangle$——$\mathbb{Z}_{20}$ 的 6 個子群就是這樣來的。**

---

*筆記依據 James S. Cook「Number Theory」2021-08-31 第 2 部錄影逐字稿（whisper 轉錄，24:23）與 Jones & Jones《Elementary Number Theory》附錄 B、§5.2 整理。*
