---
course: Abstract Algebra I (Fall 2016)
episode: 18
lecture: L12（第 1 段）
date: 2016-09-28
video: https://www.youtube.com/watch?v=y_GbIG4r3Ks
notes: AlgebraInotes_2018.pdf §2.9（p.76–78）
---

# 第 18 集 · L12（上）：講義補充——同構保持中心與循環子群 [▶ 影片](https://www.youtube.com/watch?v=y_GbIG4r3Ks&list=PLBY4G2o7DhF0JCgapYKrqibGaJuvV4Gkb)

← 上一集：[[17-答疑課]] ｜ [總目錄](../README.md) ｜ 下一集：[[19-L12-陪集與Lagrange定理-下]] →

## 本集概要

只有 4 分半鐘。老師開場補充剛上傳的講義內容，接著投影設備沒電，影片中斷。正式內容（陪集、Lagrange 定理）在 [[19-L12-陪集與Lagrange定理-下]]。

- 若 $\varphi:G\to H$ 是同構，則 $\varphi(Z(G)) = Z(H)$。
- 若 $\varphi$ 是同構，則 $\varphi(\langle a\rangle) = \langle\varphi(a)\rangle$。
- 由此立刻得到：同構保持交換性、保持元素的階。

---

## 筆記

### 1. 同構把中心送到中心 [▶ 00:30](https://youtu.be/y_GbIG4r3Ks?t=30)

老師在講義上一講的部分加了證明（Gallian 沒有）：

> **命題**　$\varphi:G\to H$ 是同構，則
> $$\varphi(Z(G)) = Z(H).$$

有了這個，「交換群的同構像是交換群」就很簡單：$G$ 交換 $\iff Z(G) = G$，所以 $Z(H) = \varphi(Z(G)) = \varphi(G) = H$。上一講是用逐個元素證的 [▶ 01:30](https://youtu.be/y_GbIG4r3Ks?t=90)。

### 2. 同構把循環子群送到循環子群 [▶ 02:00](https://youtu.be/y_GbIG4r3Ks?t=120)

> **命題**　$\varphi$ 是同構，則
> $$\varphi(\langle a\rangle) = \langle\varphi(a)\rangle.$$

主要靠上一講的引理 $\varphi(a^n) = \varphi(a)^n$。

**推出「階相同」** [▶ 02:30](https://youtu.be/y_GbIG4r3Ks?t=150)
$$|a| = |\langle a\rangle| = |\varphi(\langle a\rangle)| = |\langle\varphi(a)\rangle| = |\varphi(a)|.$$
- 第一、四個等號：元素的階 = 它生成的子群的階（L6）。
- 第二個等號：$\varphi$ 是雙射，集合和它的像一樣大 [▶ 03:00](https://youtu.be/y_GbIG4r3Ks?t=180)。若 $\langle a\rangle$ 有 10 個元素，像也有 10 個，否則 $\varphi$ 不是單射或不是滿射；無限集的雙射像也是無限的。
- 第三個等號：上面的命題。

> 💬 影片在 [▶ 03:30](https://youtu.be/y_GbIG4r3Ks?t=210) 因為設備沒插電而中斷，接續見下一集。

---

## 本集新出現的術語

（本集無新術語）

## ⚠️ 待確認清單

（本集無）
