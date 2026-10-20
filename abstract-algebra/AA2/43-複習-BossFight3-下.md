---
course: Abstract Algebra II (Spring 2026)
episode: 43
lecture: 複習（Boss Fight 3，第 2 段）
date: 2026-05-04
video: https://www.youtube.com/watch?v=ZUvRZ34egEE
notes: 無直接對應（最後一份作業的解答）
---

# 第 43 集 · 複習：Boss Fight 3（第 2 段） [▶ 影片](https://www.youtube.com/watch?v=ZUvRZ34egEE&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[42-A可微性與A微積分-上]] ｜ [總目錄](../README.md) ｜ 下一集：[[44-複習-BossFight3-上]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 43 集，期末複習第 2 段
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（4:39，自動字幕）。投影最後一份作業解答（第 11 頁起，習題 104、105 等）。
> **標記說明**：`【口頭】` 老師口頭補充；`💬` 筆記補充或更正；`⚠️` 待對照影片；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：只有 **5 分鐘**，是 5/4 複習課（[[44-複習-BossFight3-上]]）**超過一小時後**的結尾。播放清單排在前面。**請先看第 44 集。**

---

## 目錄

- [1. 正則表示的基底：Daniel 的版本](#1-正則表示的基底daniel-的版本)
- [2. 同構問題](#2-同構問題)
- [3. 習題 105](#3-習題-105)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 1. 正則表示的基底：Daniel 的版本

[▶ 00:00](https://youtu.be/ZUvRZ34egEE?t=0)「這有點**棘手**，我沒時間寫出來。看第 11 頁。」
- 投影解答裡的正則表示：「我**習慣**用那個基底。**Daniel** 用了另一個，結果就是**兩個 $A$** 的區塊對角，其他是零——**超酷**。你們有人這樣做嗎？」

---

## 2. 同構問題

[▶ 00:30](https://youtu.be/ZUvRZ34egEE?t=30)「我們時間到了，往後跳。希望你們**喜歡**這些題目。」
- **9 維複雜數**（complicated numbers——「**這真的是它們的名字**，我沒開玩笑」）[▶ 01:00](https://youtu.be/ZUvRZ34egEE?t=60) **同構於** 9 維雙曲數：**$j\mapsto-j$**。「一般地，**奇數階**的雙曲數和複雜數都同構，本質上用同一招。」
- **$\Gamma_9$** 有**冪零元**，其他交換的例子都沒有 ⇒ **不同構**。$\mathbb{R}^{3\times3}$ **不交換**，不可能同構於交換的那些。
- **習題 104**[▶ 01:30](https://youtu.be/ZUvRZ34egEE?t=90)：第一個不交換，獨自一類。
  - **$\mathcal{H}\times\mathcal{H}\cong\mathbb{R}^4$**（逐分量乘）：證過 $\mathcal{H}\cong\mathbb{R}\times\mathbb{R}$（[[06-L5-環同態與商環]]、[[40-L34-實結合代數的正則表示]]），所以 $\mathcal{H}\times\mathcal{H}\cong\mathbb{R}^4$——「**把課堂上的同構做兩次**」。
  - **$\mathbb{R}\times\mathbb{C}\cong\mathcal{H}_3$**（三重雙曲數）[▶ 02:30](https://youtu.be/ZUvRZ34egEE?t=150)：「這比較**跳躍**。$\mathcal{H}_3$ 的零因子是一個**平面**和它的**法線**；$\mathbb{R}\times\mathbb{C}$ 的零因子是 $(r,0)$ 型（一條線）和 $(0,c)$ 型（一個平面）——**結構一樣**，所以**也許**它們同構。事實上**是**。」
  - 由此 **$\mathbb{R}\times\mathcal{H}_3\cong\mathbb{C}\times\mathcal{H}$**[▶ 03:00](https://youtu.be/ZUvRZ34egEE?t=180)：同構**不太好寫**，「我算了一陣子才找到那個映射。你們**也許找到更好的**。」

💬 為什麼成立：$\mathcal{H}_3\cong\mathbb{R}\times\mathbb{C}$、$\mathcal{H}\cong\mathbb{R}\times\mathbb{R}$ ⇒ 兩邊都 $\cong\mathbb{R}\times\mathbb{R}\times\mathbb{C}$。

---

## 3. 習題 105

[▶ 03:30](https://youtu.be/ZUvRZ34egEE?t=210)「最後一題，這是**更好的基底**——**Daniel 的基底**。」用它，左乘的矩陣正則表示就是對角上的 **$A$、$A$**——「**非常棒**」。
- 「我對 $\mathbb{C}^2$ 的解答用第一個選的基底——**沒錯，但不好**。Daniel 說重排基底會得到對角上的 $A$……『$A$ **張量**某個東西』？Daniel 宣稱有更好的答案。我**還不太懂**，沒關係。」
- [▶ 04:30](https://youtu.be/ZUvRZ34egEE?t=270)「各位——**謝謝大家包容我**。」

💬 Daniel 的觀察用 [[35-L30-張量代數]] 的 Kronecker 積說：基底排列適當時 $\mathbf{M}(x) = I_2\otimes A$（區塊對角兩個 $A$）；換成另一種字典序就是 $A\otimes I_2$。兩者只差一個置換相似。

---

## 4. 一頁速查表

| 結果 | 關鍵 |
|---|---|
| 9 維複雜數 $\cong$ 9 維雙曲數 | $j\mapsto-j$；奇數階皆然 |
| $\Gamma_9$ 不同構 | 有冪零元 |
| $\mathbb{R}^{3\times3}$ 不同構 | 不交換 |
| $\mathcal{H}\times\mathcal{H}\cong\mathbb{R}^4$ | $\mathcal{H}\cong\mathbb{R}\times\mathbb{R}$ 兩次 |
| $\mathbb{R}\times\mathbb{C}\cong\mathcal{H}_3$ | 零因子都是「平面 + 法線」 |
| $\mathbb{R}\times\mathcal{H}_3\cong\mathbb{C}\times\mathcal{H}$ | 都 $\cong\mathbb{R}^2\times\mathbb{C}$ |
| 好的基底 | 正則表示 = 區塊對角 $A,A$ |

| 中文 | English |
|---|---|
| 複雜數 | complicated numbers |
| 三重雙曲數 | 3-hyperbolic numbers $\mathcal{H}_3$ |

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **複習主體** | [[44-複習-BossFight3-上]] |
| **正則表示、零因子結構** | [[40-L34-實結合代數的正則表示]] |

---

## 附：本集一句話總結

> **（5 分鐘結尾）快速走過最後幾題代數同構作業：奇數階的複雜數與雙曲數用 $j\mapsto-j$ 同構，有冪零元或不交換的例子不同構；$\mathcal{H}\times\mathcal{H}\cong\mathbb{R}^4$、$\mathbb{R}\times\mathbb{C}\cong\mathcal{H}_3$（零因子結構都是平面加法線），所以 $\mathbb{R}\times\mathcal{H}_3\cong\mathbb{C}\times\mathcal{H}$；學生 Daniel 找到讓正則表示變成區塊對角 $A,A$ 的好基底——然後老師謝謝大家包容，課程結束。**

---

## ⚠️ 待確認清單

1. $\Gamma_9$、習題 104/105 的確切題目與代數定義不在字幕中，需對照作業或影片。

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) 期末複習課結尾片段錄影（YouTube 自動字幕，4:39）整理；無講義，內容為老師投影的作業解答。*
