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

## 本集概要

5 分鐘，是 3/23 那堂課（第 27 集）的**結尾**：
- 用 **Galois 共軛**把 $\mathbb{Q}(\sqrt[3]2,\rho)$ 中元素的分母有理化（D&F 的例子，用 Maple 驗證）。
- 所有共軛的乘積是**範數**，落在基礎體裡（這例是 900）。$a^{-1}$ = 非平凡共軛的積 ÷ 範數——就像 $1/z = \bar z/(z\bar z)$。
- 更簡單的方法：**擴充歐幾里得演算法**（Bill Cook 的網站）。

**建議先看第 27 集。**

> 📘 講義對應：Math422 Lecture 23「Further Examples of Galois Theory」；D&F §14.2 習題（範數）。

---

## 筆記

### 1. 用共軛求反元素 [▶ 00:00](https://youtu.be/HIMHncPm6Lk?t=0)

設定：$\rho$ 是三次單位根，$\alpha = \sqrt[3]2$（正實的那個），要求 $a = \alpha^2+3\alpha+2$（$x^2+3x+2$ 代入 $\alpha$）的反元素。
- Maple 直接給出有理化的答案——「那不是 Galois 理論，只是黑盒子」。Mathematica 也行。
- Galois 群是 $S_3$，所以 $a$ 有 **6 個共軛**（含平凡的那個），用 $S_3$ 記號 $1,(12),(13),(23),(123),(132)$ 對根作用 [▶ 01:00](https://youtu.be/HIMHncPm6Lk?t=60)。
- 把 6 個共軛全部相乘得到基礎體中的數——**範數**（norm）。這例子是 900。D&F 有一串（約四題）習題講這種範數 [▶ 01:30](https://youtu.be/HIMHncPm6Lk?t=90)。
- 所以
$$a^{-1} = \frac{\text{5 個非平凡共軛的乘積}}{N(a)},$$
  和 $\dfrac1z = \dfrac{\bar z}{z\bar z}$ 是同一招。結果跟 Maple 一樣，驗算 $aa^{-1} = 1$ [▶ 02:30](https://youtu.be/HIMHncPm6Lk?t=150)。

### 2. 更簡單：歐幾里得演算法 [▶ 03:30](https://youtu.be/HIMHncPm6Lk?t=210)

（桌上的東西「無害」，「這是美國，自由之地、勇者之家」。）

- 把 $x^2+3x+2$ 和 $x^3-2$ 丟進擴充歐幾里得演算法：得 $a(x)(x^2+3x+2)+b(x)(x^3-2) = 1$，代入 $\alpha$ 後 $a(\alpha)$ 就是反元素——正好是剛才用共軛算出的結果 [▶ 04:00](https://youtu.be/HIMHncPm6Lk?t=240)。
- 為什麼比較簡單？不需要 Maple，用老師弟弟的免費網站 billcookmath.com，係數體可以換（例如 $\mathbb{Z}_5$）。（又提到北卡沒有休假、只有「帶薪行政假」。）
- 週三在辦公室回答作業問題。

---

## 本集新出現的術語

| 中文 | English | 首次出現 |
|---|---|---|
| 範數（Galois） | norm | §1 |

## ⚠️ 待確認清單

（本集無）
