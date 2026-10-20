---
course: Abstract Algebra II (Spring 2026)
episode: 26
lecture: L23（第 2 段）
date: 2026-03-23
video: https://www.youtube.com/watch?v=HIMHncPm6Lk
notes: 講義/AA2/Math422_Lecture23_FurtherExamplesGalois.pdf
---

# 第 26 集 · L23：Galois 理論例子——共軛技巧（第 2 段） [▶ 影片](https://www.youtube.com/watch?v=HIMHncPm6Lk&list=PLBY4G2o7DhF1x_afv1rv_d0hFCoMWEb-j)

← 上一集：[[25-L22-Galois理論基本定理]] ｜ [總目錄](../README.md) ｜ 下一集：[[27-L23-Galois理論例子-上]] →

> **課程**：Abstract Algebra II（Math 422，Liberty University，Spring 2026）— 第 26 集，Lecture 23（第 2 段）
> **講者**：James S. Cook
> **來源**：YouTube 錄影逐字稿（5:06，自動字幕）。內容是投影老師弟弟 Bill Cook 的 Maple 工作表和 Bill 的網站；講義 `Math422_Lecture23_FurtherExamplesGalois.pdf` 最後一頁（「Fun with Galois Conjugates!」）是空白的。
> **標記說明**：`【口頭】` 老師口頭補充；`💬` 筆記補充或更正；`[▶ mm:ss]` 點了跳到影片該時間點
> **說明**：只有 **5 分鐘**，是 3/23 那堂課（[[27-L23-Galois理論例子-上]]）的**結尾**。播放清單把它排在前面。**請先看第 27 集。**

---

## 目錄

- [1. Maple 的黑盒子答案](#1-maple-的黑盒子答案)
- [2. 六個 Galois 共軛、範數 900](#2-六個-galois-共軛範數-900)
- [3. 更簡單：延伸輾轉相除法](#3-更簡單延伸輾轉相除法)
- [4. 一頁速查表](#4-一頁速查表)
- [5. 與後續集數的連結](#5-與後續集數的連結)

---

## 1. Maple 的黑盒子答案

[▶ 00:00](https://youtu.be/HIMHncPm6Lk?t=0) 接第 27 集：要求 $a = 2+3\sqrt[3]2+\sqrt[3]4$ 的反元素。Bill 的 Maple 工作表裡，$\omega$ 是主三次單位根、$\alpha$ 是正的 $\sqrt[3]2$，列出三次式的三個根。
- 先讓 Maple 施展「**Maple 魔法**」直接有理化——「那**不是** Galois 理論，只是 Maple 這個**黑盒子**。Mathematica 也有類似的。」
- [▶ 00:30](https://youtu.be/HIMHncPm6Lk?t=30) 令多項式 $x^2+3x+2$ 對應要反轉的元素，代入 $\alpha$：$a = \alpha^2+3\alpha+2$。

---

## 2. 六個 Galois 共軛、範數 900

[▶ 01:00](https://youtu.be/HIMHncPm6Lk?t=60)
- 在 $\mathbb{Q}(\sqrt[3]2,\omega)$ 上 Galois 群是 **$S_3$** ⇒ 有 **6 個共軛**要算（Bill 用 $S_3$ 記號：恆等、三個 2-循環、兩個 3-循環）；最蠢的是恆等，送到自己。
- 「這些是**明確地**對我們關心的那個根作用的 Galois 共軛。」
- [▶ 01:30](https://youtu.be/HIMHncPm6Lk?t=90) **六個共軛全乘起來**得到基體裡的數——這裡是 **900**。「D&F 有大約**四題**作業在講用 Galois 共軛之積算**範數**。」
- [▶ 02:00](https://youtu.be/HIMHncPm6Lk?t=120)
$$a^{-1} = \frac{\text{所有非平凡共軛之積}}{\text{範數}}.$$
  「範數 = 所有非平凡共軛 × $a$ 本身。就像 $\frac1z = \frac{\bar z}{z\bar z}$——$\bar z$ 抵消，留下 $\frac1z$。**同一招**。」結果跟 Maple 黑盒子的一樣。
- [▶ 03:00](https://youtu.be/HIMHncPm6Lk?t=180)「$a\cdot a^{-1} = 1$。**好兆頭**。耶！」

💬 900 的來源：$a = \alpha^2+3\alpha+2 = (\alpha+1)(\alpha+2)$。$\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}$ 的範數 $N(\alpha+c) = c^3+2$（代 $x = -c$ 進 $x^3-2$ 再變號），所以 $N(\alpha+1) = 3$、$N(\alpha+2) = 10$，$N(a) = 30$。$a$ 在 $\mathbb{Q}(\sqrt[3]2)$ 裡，6 個 Galois 共軛裡每個值出現兩次，乘積 $= 30^2 = 900$。用 3 個相異共軛就夠：$a^{-1} = \frac{a'a''}{30}$。

---

## 3. 更簡單：延伸輾轉相除法

[▶ 03:30](https://youtu.be/HIMHncPm6Lk?t=210)（「讓我**避免被取消**。」學生：「你左邊放的是什麼？」「**無害**的東西，不談。畢竟這是**美國**——自由之地、勇者之家。」）

[▶ 04:00](https://youtu.be/HIMHncPm6Lk?t=240)「這**正是**他用 Galois 共軛技巧做的那個例子。」把 $x^2+3x+2$ 和 $x^3-2$ 丟進**延伸輾轉相除法**：得到 $a(x)$、$b(x)$——
$$a(x)(x^2+3x+2)+b(x)(x^3-2) = 1,$$
$a(x)$ **正是**共軛技巧推出來的反元素。
- 【課堂討論】「為什麼這比較**簡單**？」學生：「**不需要 Maple**。」「用**我弟弟的網站**，**免費**、免費、免費：billcookmath.com 的延伸輾轉相除法。注意可以調係數體——例如 $\mathbb{Z}_5$。**你們有選擇**。」
- 「這全來自我弟弟的**休假年**——抱歉，**帶薪行政假**。北卡州議會的限制，他們沒有休假年。」
- [▶ 04:30](https://youtu.be/HIMHncPm6Lk?t=270)「我閉嘴了。週三我會在，你們有作業問題可以來問。」

---

## 4. 一頁速查表

| 方法 | 做法 |
|---|---|
| Galois 共軛（範數） | $a^{-1} = \dfrac{\prod_{\sigma\neq1}\sigma(a)}{N(a)}$，$N(a) = \prod_\sigma\sigma(a)\in\mathbb{Q}$ |
| 延伸輾轉相除法 | $a(x)f(x)+b(x)m(x) = 1$ ⇒ $f(\alpha)^{-1} = a(\alpha)$ |
| 例 | $(2+3\sqrt[3]2+\sqrt[3]4)^{-1}$；共軛之積 900 |

| 中文 | English |
|---|---|
| 範數 | norm |
| Galois 共軛 | Galois conjugate |
| 延伸輾轉相除法 | extended Euclidean algorithm |

---

## 5. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| **本講主體** | [[27-L23-Galois理論例子-上]] |
| **共軛、對稱函數** | [[28-L24-多項式的Galois群]] |

---

## 附：本集一句話總結

> **（5 分鐘結尾）用 Bill 的 Maple 例子示範：要反轉 $2+3\sqrt[3]2+\sqrt[3]4$，把它的 6 個 Galois 共軛乘起來得到有理數 900（範數），反元素就是其餘共軛之積除以範數——像 $1/z = \bar z/(z\bar z)$；但更簡單的是對 $x^2+3x+2$ 和 $x^3-2$ 做延伸輾轉相除法，Bill 的網站免費就能算。**

---

## ⚠️ 待確認清單

（本集無）

---

*筆記依據 James S. Cook「Abstract Algebra II」(Spring 2026) Lecture 23 結尾片段錄影（YouTube 自動字幕，5:06）整理；課堂投影 Bill Cook 的 Maple 工作表與網站。*
