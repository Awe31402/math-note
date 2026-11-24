---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 17
lecture: Lecture 7 (Part 2) – The fundamental and essential matrices
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/mNThwULGR-g
notes: MVG §9.2.5–9.3（書頁 246–250，PDF 頁 264–268）、§9.5.1–9.5.2（書頁 253–255，PDF 頁 271–273）
---

# 第 17 集 · Lecture 7 (Part 2)：極線 homography、純平移、一般運動、F 的射影模糊 [▶ 影片](https://youtu.be/mNThwULGR-g)

← 上一集：[16-fundamental-essential-part1](16-fundamental-essential-part1.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[18-fundamental-essential-part3](18-fundamental-essential-part3.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 17 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（35:38，Whisper `medium.en` 轉錄）＋ MVG §9.2.5–9.3、§9.5.1–9.5.2
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 極線之間的 homography](#1-極線之間的-homography)
- [2. 純平移](#2-純平移)
  - [2.1 F = [e']×](#21-f--e)
  - [2.2 x、x'、e' 共線](#22-xxe-共線)
  - [2.3 兩個例子](#23-兩個例子)
- [3. 一般運動 = 純旋轉 + 純平移](#3-一般運動--純旋轉--純平移)
- [4. 從 F 求相機矩陣：射影模糊](#4-從-f-求相機矩陣射影模糊)
  - [4.1 (P, P') 和 (PH, P'H) 給同一個 F](#41-p-p-和-ph-ph-給同一個-f)
  - [4.2 標準相機對：F = [m]× M](#42-標準相機對f--m-m)
  - [4.3 定理與引理（證明下一集續）](#43-定理與引理證明下一集續)
- [5. 一頁速查表](#5-一頁速查表)
- [6. 與後續集數的連結](#6-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 對應極線之間的 homography | §9.2.5 |
| 純平移、一般運動下的 $F$ | §9.3 |
| 從 $F$ 求 $P,P'$：射影模糊、標準形式 | §9.5.1–9.5.2 |

**回顧** [▶ 00:00](https://youtu.be/mNThwULGR-g?t=0)：$F$ 把點映到極線（$\mathbf{l}'=F\mathbf{x}$），也給對應點約束（$\mathbf{x}'^\mathsf{T}F\mathbf{x}=0$）。

---

## 1. 極線之間的 homography

[▶ 00:40](https://youtu.be/mNThwULGR-g?t=40)

$F$ 也能把第一張圖的**極線** $\mathbf{l}$ 轉到第二張圖的對應極線 $\mathbf{l}'$：

> **Result 9.5（MVG）** 設 $\mathbf{l}$、$\mathbf{l}'$ 是對應極線，$\mathbf{k}$ 是任何不通過極點 $\mathbf{e}$ 的線，則
> $$\mathbf{l}'=F[\mathbf{k}]_\times\mathbf{l}$$
> 對稱地，$\mathbf{l}=F^\mathsf{T}[\mathbf{k}']_\times\mathbf{l}'$。

**證明** [▶ 01:20](https://youtu.be/mNThwULGR-g?t=80)：

1. 第一張圖上任取一條線 $\mathbf{k}$，它和極線 $\mathbf{l}$ 交於一點：$\tilde{\mathbf{x}}=\mathbf{k}\times\mathbf{l}=[\mathbf{k}]_\times\mathbf{l}$。
2. $\tilde{\mathbf{x}}$ 在 $\mathbf{l}$ 上，所以它的極線就是 $\mathbf{l}'$：$\mathbf{l}'=F\tilde{\mathbf{x}}=F[\mathbf{k}]_\times\mathbf{l}$。∎

- **對任何線 $\mathbf{k}$ 都成立**：$\mathbf{k}$ 不管怎麼畫，都和 $\mathbf{l}$ 交於某一點。
- $F[\mathbf{k}]_\times$ 是 $3\times3$，把 2D 線映到 2D 線——可以看成一個 **homography**（作用在極線束上）。

【課本補充】MVG Result 9.5 要求 $\mathbf{k}$ **不通過**極點 $\mathbf{e}$。

> 以下**不是逐字稿內容**，是說明為什麼要這個條件：若 $\mathbf{k}$ 通過 $\mathbf{e}$，交點 $\tilde{\mathbf{x}}$ 可能就是 $\mathbf{e}$ 本身（當 $\mathbf{l}$ 也通過 $\mathbf{e}$——所有極線都通過 $\mathbf{e}$），而 $F\mathbf{e}=\mathbf{0}$，得不到 $\mathbf{l}'$。

**1D homography 的看法** [▶ 04:40](https://youtu.be/mNThwULGR-g?t=280)：

- 線 $\mathbf{k}$ 和極線束交於一串點；這些點在第二張圖的對應點也在一條線上（線性映射）。
- 兩串點透過一個投影中心相連 → 兩串點**射影相關**，**交比**相同（第 02 集）→ 它們之間是一個 **1D homography**。

【課本補充】MVG §9.2.5：極線束是 1D 射影空間，兩張圖的極線束之間的對應就是 $\mathbb{P}^1$ 上的 homography，有 3 個自由度。加上兩個極點各 2 個自由度，$2+2+3=7$——正好是 $F$ 的自由度。

---

## 2. 純平移

### 2.1 F = [e']×

[▶ 06:26](https://youtu.be/mNThwULGR-g?t=386)

**假設**：沒有旋轉（$R=I$）、內參不變（$K'=K$）：

$$
P=K[I\mid\mathbf{0}],\qquad P'=K[I\mid\mathbf{t}]
$$

代入第 16 集的 $F=[\mathbf{e}']_\times K'RK^{-1}$：

$$
F=[\mathbf{e}']_\times KIK^{-1}=[\mathbf{e}']_\times
$$

- $K$ 和 $K^{-1}$ 消掉，**$F$ 就是第二個極點的反對稱矩陣**。
- 反對稱矩陣 rank 2，和 $F$ 該有的 rank 一致。

⚠️ 逐字稿缺字：Whisper 把 epipole 多處寫成 “epipode”。

【課本補充】MVG §9.3.1：純平移時 $F$ 是反對稱的，只有 **2 個自由度**（就是極點的位置）。

### 2.2 x、x'、e' 共線

[▶ 08:47](https://youtu.be/mNThwULGR-g?t=527)

- 極線：$\mathbf{l}'=F\mathbf{x}=[\mathbf{e}']_\times\mathbf{x}=\mathbf{e}'\times\mathbf{x}$。
- $\mathbf{x}'$ 在極線上：
$$
\mathbf{x}'^\mathsf{T}[\mathbf{e}']_\times\mathbf{x}=0
$$
- 意義：$\mathbf{e}'\times\mathbf{x}$ 是通過 $\mathbf{e}'$ 和 $\mathbf{x}$ 的線，$\mathbf{x}'$ 在這條線上 → **$\mathbf{x}$、$\mathbf{x}'$、$\mathbf{e}'$ 三點共線**（把 $\mathbf{x}$ 畫在第二張圖的同一座標上看）。
- 這只在**純平移**時成立。一般運動的 $F$ 多了一項 $K'RK^{-1}$，就沒有這個性質。

### 2.3 兩個例子

**例一：相機不動、物體反向平移** [▶ 12:01](https://youtu.be/mNThwULGR-g?t=721)：

- 把「相機平移 $\mathbf{t}$」看成「相機不動、世界平移 $-\mathbf{t}$」。
- 立方體的每個角點沿**平行的直線**移動。
- 平行線交於無窮遠 → 投影到影像上交於一個**消失點**——這個消失點就是**極點**。
- 每對對應點 $\mathbf{x}$、$\mathbf{x}'$ 在同一條平行線的像上，這條像線通過消失點（極點）→ $\mathbf{x}$、$\mathbf{x}'$、$\mathbf{e}$ 共線。

**例二：相機往前平移** [▶ 16:01](https://youtu.be/mNThwULGR-g?t=961)：

- 相機從 $C$ 往前移到 $C'$。
- 基線通過兩個相機中心，和兩張影像交於**同一個位置**的極點 → 極點不變、極線也不變。
- 第二張圖的點 $\mathbf{x}'$ 畫在第一張圖上，會落在同一條極線上、**更外面**。
- 結論：相機往前走時，極點不動，**所有對應點看起來都從極點往外放射移動**——極點是**擴張焦點（focus of expansion）**。

【課本補充】MVG Example 9.6 使用的名稱就是 focus of expansion（往前移時）；往後移時叫 focus of contraction。

---

## 3. 一般運動 = 純旋轉 + 純平移

[▶ 18:10](https://youtu.be/mNThwULGR-g?t=1090)

一般運動（$R$、$\mathbf{t}$）可以拆成兩步：

1. **純旋轉**：影像經過一個 homography 轉到中間影像。純旋轉的 homography（第 13 集）是
$$
H_\infty=K'RK^{-1}
$$
   叫**無窮遠 homography（infinite homography）**（無窮遠平面誘導的 homography，第 14 集 $H=KR$ 的雙相機版）。
2. **純平移**：中間影像到最終影像只差純平移，$\tilde{F}=[\mathbf{e}']_\times$（第 2 節）。

兩步合起來 [▶ 21:16](https://youtu.be/mNThwULGR-g?t=1276)：

$$
F=[\mathbf{e}']_\times H_\infty=[\mathbf{e}']_\times K'RK^{-1}
$$

- 和第 16 集代數推導的結果**一模一樣**。
- $[\mathbf{e}']_\times$ 是純平移部分；$H_\infty$ 是純旋轉部分。

⚠️ 逐字稿缺字 [▶ 19:12](https://youtu.be/mNThwULGR-g?t=1152)：講者說「旋轉完之後，剩下的關係只是一個 pure rotation」，依上下文應為 **pure translation**。[▶ 20:09](https://youtu.be/mNThwULGR-g?t=1209) 講者提醒投影片上的第一個 $K$ 應該加 prime（$K'$）。

---

## 4. 從 F 求相機矩陣：射影模糊

[▶ 22:31](https://youtu.be/mNThwULGR-g?t=1351)

前面都是「已知相機 → 求 $F$」。現在反過來：**給 $F$，能分解出 $P$、$P'$ 嗎？**

答案：**不唯一**。同一個 $F$ 對應很多組相機，它們之間差一個 $4\times4$ 射影變換。

### 4.1 (P, P') 和 (PH, P'H) 給同一個 F

[▶ 24:10](https://youtu.be/mNThwULGR-g?t=1450)

> **Result 9.8（MVG，課堂版）** $H$ 是 $4\times4$ 射影變換。則 $(P,P')$ 和 $(PH,P'H)$ 的 fundamental matrix 相同。

**證明**：

$$
P\mathbf{X}=(PH)(H^{-1}\mathbf{X})
$$

- $H$ 消掉。所以相機 $PH$ 看點 $H^{-1}\mathbf{X}$，和相機 $P$ 看點 $\mathbf{X}$，得到**同一個像點**。
- $P'$ 也一樣。
- 所以：$\mathbf{x}\leftrightarrow\mathbf{x}'$ 在 $(P,P')$ 下是一對對應點，在 $(PH,P'H)$ 下**也是**（只是對應的 3D 點變成 $H^{-1}\mathbf{X}$）。
- 影像上的對應完全一樣 → $F$ 一樣（$F$ 只由對應點決定）。

**意義** [▶ 26:06](https://youtu.be/mNThwULGR-g?t=1566)：

- 給 $P,P'$ → $F$ **唯一**（第 16 集）。
- 給 $F$ → $P,P'$ **不唯一**，只能確定到差一個 $4\times4$ 射影變換。

⚠️ 逐字稿缺字 [▶ 23:45](https://youtu.be/mNThwULGR-g?t=1425)：講者說「related by a homography」，指的是 $4\times4$ **射影變換**（3D homography）。

### 4.2 標準相機對：F = [m]× M

[▶ 27:18](https://youtu.be/mNThwULGR-g?t=1638)

先定義**標準形式（canonical form）**：第一個相機是 $P=[I\mid\mathbf{0}]$（忽略 $K$），第二個是一般的 $P'=[M\mid\mathbf{m}]$（$M$ 是 $3\times3$、$\mathbf{m}$ 是 $3\times1$）。

> **Result 9.9（MVG）** 標準相機對 $P=[I\mid\mathbf{0}]$、$P'=[M\mid\mathbf{m}]$ 的 fundamental matrix 是
> $$F=[\mathbf{m}]_\times M$$

**證明** [▶ 28:26](https://youtu.be/mNThwULGR-g?t=1706)：

1. 第一個相機中心：$\mathbf{C}=(0,0,0,1)^\mathsf{T}$。
2. 第二張圖的極點：$\mathbf{e}'=P'\mathbf{C}=[M\mid\mathbf{m}](0,0,0,1)^\mathsf{T}=\mathbf{m}$（$P'$ 的最後一行）。
3. $P$ 的偽逆：$P^+=\begin{pmatrix}I\\\mathbf{0}^\mathsf{T}\end{pmatrix}$（驗證 $PP^+=I$，講者留作練習）。
4. 代入 $F=[\mathbf{e}']_\times P'P^+$：
$$
F=[\mathbf{m}]_\times[M\mid\mathbf{m}]\begin{pmatrix}I\\\mathbf{0}^\mathsf{T}\end{pmatrix}=[\mathbf{m}]_\times M\qquad\blacksquare
$$

⚠️ 逐字稿缺字 [▶ 27:39](https://youtu.be/mNThwULGR-g?t=1659)：講者說「let's ignore the camera projection matrix over here」，依上下文應為「忽略**內參 $K$**」。

### 4.3 定理與引理（證明下一集續）

[▶ 30:25](https://youtu.be/mNThwULGR-g?t=1825)

> **Theorem 9.10（MVG）** 若 $(P,P')$ 和 $(\tilde{P},\tilde{P}')$ 對應**同一個** fundamental matrix $F$，則存在非奇異 $4\times4$ 矩陣 $H$，使
> $$\tilde{P}=PH,\qquad \tilde{P}'=P'H$$

（這是 4.1 的**反方向**：不只「差 $H$ 的相機給同一個 $F$」，而是「給同一個 $F$ 的相機**一定**只差一個 $H$」。）

**證明的開頭** [▶ 31:58](https://youtu.be/mNThwULGR-g?t=1918)：

1. 假設兩組相機給同一個 $F$。
2. 不失一般性，兩組都化成標準形式（4.1 說可以用射影變換做到）：
$$
P=\tilde{P}=[I\mid\mathbf{0}],\qquad P'=[A\mid\mathbf{a}],\qquad \tilde{P}'=[\tilde{A}\mid\tilde{\mathbf{a}}]
$$
3. 由 4.2：
$$
F=[\mathbf{a}]_\times A=[\tilde{\mathbf{a}}]_\times\tilde{A}
$$

**需要的引理** [▶ 34:37](https://youtu.be/mNThwULGR-g?t=2077)：

> **Lemma 9.11（MVG）** 若 rank 2 的 $F$ 能寫成兩種形式 $F=[\mathbf{a}]_\times A=[\tilde{\mathbf{a}}]_\times\tilde{A}$，則
> $$\tilde{\mathbf{a}}=k\mathbf{a},\qquad \tilde{A}=k^{-1}\left(A+\mathbf{a}\mathbf{v}^\mathsf{T}\right)$$
> 其中 $k$ 是非零常數，$\mathbf{v}$ 是某個 3 維向量。

（本集到 35:31 引理敘述結束；引理和定理的證明在下一集。）

---

## 5. 一頁速查表

| 公式 | 意義 | 關鍵一步 |
|---|---|---|
| $\mathbf{l}'=F[\mathbf{k}]_\times\mathbf{l}$ | 極線之間的 homography | $\mathbf{k}\times\mathbf{l}$ 是 $\mathbf{l}$ 上一點 |
| 純平移 $F=[\mathbf{e}']_\times$（2 dof） | $\mathbf{x},\mathbf{x}',\mathbf{e}'$ 共線；往前走 → 擴張焦點 | $K'RK^{-1}=KIK^{-1}=I$ |
| 一般運動 $F=[\mathbf{e}']_\times H_\infty$，$H_\infty=K'RK^{-1}$ | 純旋轉（$H_\infty$）+ 純平移（$[\mathbf{e}']_\times$） | — |
| $(P,P')$ 和 $(PH,P'H)$ 同一個 $F$ | 射影模糊 | $P\mathbf{X}=(PH)(H^{-1}\mathbf{X})$ |
| 標準形式 $P=[I\mid\mathbf{0}]$、$P'=[M\mid\mathbf{m}]$ → $F=[\mathbf{m}]_\times M$ | — | $\mathbf{e}'=\mathbf{m}$，$P^+=(I;\mathbf{0}^\mathsf{T})$ |
| 引理：$F=[\mathbf{a}]_\times A=[\tilde{\mathbf{a}}]_\times\tilde{A}$ ⟹ $\tilde{\mathbf{a}}=k\mathbf{a}$，$\tilde{A}=k^{-1}(A+\mathbf{a}\mathbf{v}^\mathsf{T})$ | 下一集證明 | — |

---

## 6. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 引理 9.11、定理 9.10 | 第 18 集（證明；標準相機對 $P'=[[\mathbf{e}']_\times F\mid\mathbf{e}']$） |
| 射影模糊 | 第 19 集（分層重建：射影 → 仿射 → 度量）；第 27–30 集（SfM） |
| $H_\infty=K'RK^{-1}$ | 第 19 集（無窮遠平面、仿射重建） |
| 純平移、擴張焦點 | 第 31–34 集（stereo 校正後極線平行，相當於特殊的純平移） |

---

## 附：本集一句話總結

> **$F$ 還能把極線送到極線（$F[\mathbf{k}]_\times$）；純平移時 $F$ 退化成 $[\mathbf{e}']_\times$，對應點和極點共線、往前走時從極點放射出去；一般運動就是「純旋轉 $H_\infty=K'RK^{-1}$ 再純平移」，$F=[\mathbf{e}']_\times H_\infty$；而反過來從 $F$ 只能求出差一個 $4\times4$ 射影變換的相機對——標準形式 $P=[I\mid\mathbf{0}]$、$P'=[M\mid\mathbf{m}]$ 時 $F=[\mathbf{m}]_\times M$。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 7 (Part 2) 錄影逐字稿（Whisper `medium.en`，35:38）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §9.2.5–9.3、§9.5.1–9.5.2 整理。*
