---
course: Abstract Algebra I (Fall 2016)
episode: 18
lecture: L12
date: 2016-09-28
video: https://www.youtube.com/watch?v=y_GbIG4r3Ks
notes: AlgebraInotes_2018.pdf §2.4.1（p.54–55）
---

# 第 18 集 · L12（上）：同構保持中心與循環子群（4 分鐘） [▶ 影片](https://www.youtube.com/watch?v=y_GbIG4r3Ks&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[17-答疑課]] ｜ [總目錄](../README.md) ｜ 下一集：[[19-L12-陪集與Lagrange定理-下]] →

> **課程**：Abstract Algebra I（Liberty University，Fall 2016）— 第 18 集，Lecture 12 開頭
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（4:37，自動字幕）＋ 講義 `AlgebraInotes_2018.pdf` §2.4.1「isomorphism theorems」（Thm 2.4.23、2.4.24 及之後的證明，p.54–55）。
> **標記說明**：`【口頭】` 老師口頭補充、講義沒有；`【講義補充】` 講義有、課堂沒講；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：影片只有 4 分半。老師開場補充剛上傳的講義，接著設備沒電，影片中斷。今天的正題（陪集、Lagrange 定理）在 [[19-L12-陪集與Lagrange定理-下]]。

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 同構把中心送到中心](#1-同構把中心送到中心)
- [2. 同構把循環子群送到循環子群](#2-同構把循環子群送到循環子群)
- [3. 推論：同構保持元素的階](#3-推論同構保持元素的階)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 0. 這堂課要做什麼

[▶ 00:00](https://youtu.be/y_GbIG4r3Ks?t=0) 課前禱告。今天講**陪集（cosets）**。

在那之前 [▶ 00:30](https://youtu.be/y_GbIG4r3Ks?t=30)：老師重新上傳了講義，在上一講的部分加了兩個證明，要大家讀。

---

## 1. 同構把中心送到中心

[▶ 00:30](https://youtu.be/y_GbIG4r3Ks?t=30)

> **命題**（講義 Thm 2.4.23）　$\varphi:G\to H$ 是同構。則
> $$\varphi(Z(G)) = Z(H).$$

【口頭】[▶ 01:00](https://youtu.be/y_GbIG4r3Ks?t=60)「這不在 Gallian 裡，但對我來說證起來不難。其實證得挺好玩的，我花了點功夫。你們可以讀講義上的證明。」

**用途**[▶ 01:30](https://youtu.be/y_GbIG4r3Ks?t=90)：有了它，「交換群的同構像還是交換群」就**非常簡單**：
$$G\text{ 交換}\iff Z(G) = G\ \Rightarrow\ Z(H) = \varphi(Z(G)) = \varphi(G) = H\iff H\text{ 交換}.$$
（上一講是逐個元素證的，見 [[16-L11-同構的性質]] 第 5 節。）

> 📘 **講義的證明**
>
> **(⊆)** 設 $a\in Z(G)$，取任意 $h\in H$。$\varphi$ 是雙射，$h = \varphi(\varphi^{-1}(h))$。
> $$h\varphi(a) = \varphi(\varphi^{-1}(h))\varphi(a) = \varphi(\varphi^{-1}(h)\,a) = \varphi(a\,\varphi^{-1}(h)) = \varphi(a)\,h.$$
> 第三個等號：$a$ 在中心，跟 $\varphi^{-1}(h)\in G$ 交換。所以 $\varphi(a)\in Z(H)$。
>
> **(⊇)** 設 $b\in Z(H)$。$\varphi$ 映成，所以 $b = \varphi(x)$，$x = \varphi^{-1}(b)$。對任意 $g\in G$：
> $$gx = \varphi^{-1}(\varphi(g))\,\varphi^{-1}(b) = \varphi^{-1}(\varphi(g)\,b) = \varphi^{-1}(b\,\varphi(g)) = \varphi^{-1}(b)\,\varphi^{-1}(\varphi(g)) = xg.$$
> （用到 $\varphi^{-1}$ 也是同態，以及 $b\in Z(H)$。）所以 $x\in Z(G)$，$b = \varphi(x)\in\varphi(Z(G))$。

---

## 2. 同構把循環子群送到循環子群

[▶ 02:00](https://youtu.be/y_GbIG4r3Ks?t=120)「另一個我在講義證的，我希望你們研究：」

> **命題**（講義 Thm 2.4.24）　$\varphi:G\to H$ 是同構，$a\in G$。則
> $$\varphi(\langle a\rangle) = \langle\varphi(a)\rangle.$$
> 「同構把 $a$ 生成的循環子群，送到 $\varphi(a)$ 生成的循環子群。非常好。」

**主要工作**在上一講的引理 $\varphi(a^n) = \varphi(a)^n$。

> 📘 **講義的證明**
> - **(⊆)** $x\in\varphi(\langle a\rangle)$ ⇒ $x = \varphi(a^n) = \varphi(a)^n\in\langle\varphi(a)\rangle$。
> - **(⊇)** $y\in\langle\varphi(a)\rangle$ ⇒ $y = \varphi(a)^n = \varphi(a^n)\in\varphi(\langle a\rangle)$。
>
> 推論：$G = \langle a\rangle$ 循環 ⇒ $H = \varphi(G) = \langle\varphi(a)\rangle$ 循環。反方向對 $\varphi^{-1}$ 用同樣論證。

---

## 3. 推論：同構保持元素的階

[▶ 02:30](https://youtu.be/y_GbIG4r3Ks?t=150)「有了這個，證明元素的階被保持就很容易，因為這個論證：」

$$|a| = |\langle a\rangle| = |\varphi(\langle a\rangle)| = |\langle\varphi(a)\rangle| = |\varphi(a)|.$$

| 等號 | 理由 |
|---|---|
| 第 1 個 | 元素的階 = 它生成的子群的階（L6） |
| 第 2 個 [▶ 03:00](https://youtu.be/y_GbIG4r3Ks?t=180) | $\varphi$ 是**雙射**，集合和它的像元素個數一樣 |
| 第 3 個 | 第 2 節的命題 |
| 第 4 個 | 元素的階 = 它生成的子群的階 |

**第 2 個等號的細節**[▶ 03:00](https://youtu.be/y_GbIG4r3Ks?t=180)：
- 若 $\langle a\rangle$ 有 10 個元素，它的像也有 10 個——否則 $\varphi$ 不是單射就是不是映成。
- 若 $\langle a\rangle$ 是無限集，雙射的像也是無限集。
- 所以有限、無限兩種情況都成立。

> 📘 講義：「我們原本在元素層級的論證也是證明階被保持的合理方法。不過我喜歡上面這個論證。」

[▶ 03:30](https://youtu.be/y_GbIG4r3Ks?t=210)「喔，有個小細節沒插電……糟糕。」影片在此中斷，接續見下一集。

---

## 4. 一頁速查表

| 結果 | 關鍵一步 |
|---|---|
| $\varphi(Z(G)) = Z(H)$ | $h\varphi(a) = \varphi(\varphi^{-1}(h)a) = \varphi(a\varphi^{-1}(h)) = \varphi(a)h$ |
| $G$ 交換 ⟺ $H$ 交換 | $Z(G) = G\iff Z(H) = H$ |
| $\varphi(\langle a\rangle) = \langle\varphi(a)\rangle$ | $\varphi(a^n) = \varphi(a)^n$ |
| $\lvert a\rvert = \lvert\varphi(a)\rvert$ | $\lvert a\rvert = \lvert\langle a\rangle\rvert = \lvert\varphi(\langle a\rangle)\rvert = \lvert\langle\varphi(a)\rangle\rvert = \lvert\varphi(a)\rvert$ |

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **陪集**（今天的正題） | [[19-L12-陪集與Lagrange定理-下]] |
| **同構保持中心** | [[20-答疑課]]：$D_4$ 的中心；[[31-答疑課]]：小階群分類 |
| **雙射保持集合大小** | [[19-L12-陪集與Lagrange定理-下]]：每個陪集跟 $H$ 一樣大（$h\mapsto ah$ 是雙射） |

---

## 附：本集一句話總結

> **同構把中心送到中心、把 $\langle a\rangle$ 送到 $\langle\varphi(a)\rangle$；因為雙射保持集合大小，立刻得到 $|a| = |\langle a\rangle| = |\langle\varphi(a)\rangle| = |\varphi(a)|$，也立刻得到交換性被保持。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra I」(Fall 2016) Lecture 12 開頭錄影逐字稿（YouTube 自動字幕，4:37）與講義 `AlgebraInotes_2018.pdf` §2.4.1（p.54–55）整理。*
