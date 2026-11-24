---
course: 3D Computer Vision（NUS CS4277/CS5477）
episode: 26
lecture: Lecture 9 (Part 4) – Three-view geometry from points and/or lines
date: 待補（COVID-19 期間錄製的線上課）
video: https://youtu.be/rysdVwyM9FQ
notes: MVG §15.3（書頁 379–383，PDF 頁 397–401）、§16.1–16.4（書頁 391–397，PDF 頁 409–415）
---

# 第 26 集 · Lecture 9 (Part 4)：點轉移、計算 trifocal tensor [▶ 影片](https://youtu.be/rysdVwyM9FQ)

← 上一集：[25-three-view-geometry-part3](25-three-view-geometry-part3.md) ｜ [總目錄](PROGRESS.md) ｜ 下一集：[27-sfm-bundle-adjustment-part1](27-sfm-bundle-adjustment-part1.md) →

> **課程**：3D Computer Vision（CS4277/CS5477），National University of Singapore — 第 26 集
> **講者**：Gim Hee Lee
> **來源**：YouTube 錄影逐字稿（31:50，Whisper `medium.en` 轉錄）＋ MVG §15.3、§16.1–16.4
> **標記說明**：
> - `【口頭】` 講者口頭補充，課本沒有
> - `【課本補充】` MVG 有、課堂沒講
> - `⚠️ 逐字稿缺字` Whisper 聽錯或掉字

---

## 目錄

- [0. 這堂課要做什麼](#0-這堂課要做什麼)
- [1. 點轉移](#1-點轉移)
  - [1.1 用 fundamental matrix：極線交點](#11-用-fundamental-matrix極線交點)
  - [1.2 用 trifocal tensor](#12-用-trifocal-tensor)
- [2. 線性估計 trifocal tensor](#2-線性估計-trifocal-tensor)
  - [2.1 At = 0 與每種對應的方程式數](#21-at--0-與每種對應的方程式數)
  - [2.2 正規化線性演算法](#22-正規化線性演算法)
- [3. 強制極點約束：代數最小化](#3-強制極點約束代數最小化)
- [4. 幾何誤差：Gold Standard](#4-幾何誤差gold-standard)
- [5. Lecture 9 總結](#5-lecture-9-總結)
- [6. 一頁速查表](#6-一頁速查表)
- [7. 與後續集數的連結](#7-與後續集數的連結)

---

## 0. 這堂課要做什麼

| 主題 | MVG |
|---|---|
| 給前兩張圖的對應點，求第三張圖的點（點轉移） | §15.3 |
| 從點／線對應線性估計 tensor（正規化） | §16.1–16.2 |
| 強制內部約束：代數最小化 | §16.3 |
| 幾何誤差：Gold Standard | §16.4 |

---

## 1. 點轉移

### 1.1 用 fundamental matrix：極線交點

[▶ 00:00](https://youtu.be/rysdVwyM9FQ?t=0)

**問題**：已知 $F_{21},F_{31},F_{32}$，以及前兩張圖的對應點 $\mathbf{x}\leftrightarrow\mathbf{x}'$，求第三張圖的對應點 $\mathbf{x}''$。

**做法**：第三張圖的點一定在兩條極線上：

- $\mathbf{x}$ 經 $F_{31}$ 轉成第三張圖的極線：$\mathbf{l}_{13}=F_{31}\mathbf{x}$。
- $\mathbf{x}'$ 經 $F_{32}$ 轉成第三張圖的極線：$\mathbf{l}_{23}=F_{32}\mathbf{x}'$。
- 兩線交點：
$$
\mathbf{x}''=(F_{31}\mathbf{x})\times(F_{32}\mathbf{x}')
$$

**退化** [▶ 03:20](https://youtu.be/rysdVwyM9FQ?t=200)：兩條極線**重合（共線）**時，交點沒有定義——$\mathbf{x}''$ 可以在那條線上任何地方。

【課本補充】MVG §15.3.1：這發生在 3D 點落在**三焦平面（trifocal plane）**——三個相機中心決定的平面——上的時候；點靠近這個平面時，轉移也會不準。

> 以下**不是逐字稿內容**，是為什麼：3D 點 $\mathbf{X}$ 在三焦平面上時，$C,C',\mathbf{X}$ 決定的極平面和 $C,C'',\mathbf{X}$ 決定的極平面是同一個（都是三焦平面），所以兩條極線都是三焦平面和第三張影像的交線，完全重合。

### 1.2 用 trifocal tensor

[▶ 04:07](https://youtu.be/rysdVwyM9FQ?t=247)

用第 24 集的**點–線–點**關係：在第二張圖選一條**通過 $\mathbf{x}'$** 的線 $\mathbf{l}'$，則

$$
x''^k=x^il'_j\,\mathcal{T}_i^{jk}
$$

- 這就是 $\mathbf{l}'$ 反投影平面誘導的 homography $H_{13}(\mathbf{l}')$，把 $\mathbf{x}$ 轉到第三張圖。
- 用 tensor 時，上面的退化（三焦平面）**不再存在**。

**但有另一個特殊情況** [▶ 05:29](https://youtu.be/rysdVwyM9FQ?t=329)：若 $\mathbf{l}'$ 剛好是 $\mathbf{x}$ 在第二張圖的**極線**：

- $\mathbf{l}'$ 的反投影平面就是極平面，包含 $\mathbf{x}$ 的光線。
- 第 24 集：極線是 $\sum_ix^iT_i$ 的左零向量 → $x^il'_j\mathcal{T}_i^{jk}=0^k$ → $\mathbf{x}''$ 求不出來。

**解法：選垂直於極線的線** [▶ 06:53](https://youtu.be/rysdVwyM9FQ?t=413)：

- 設 $\mathbf{x}$ 在第二張圖的極線 $\mathbf{l}'_e=F_{21}\mathbf{x}=(l_1,l_2,l_3)^\mathsf{T}$，對應點 $\mathbf{x}'=(x_1,x_2,1)^\mathsf{T}$。
- $\mathbf{l}'$ 只要通過 $\mathbf{x}'$ 就行。最好選**通過 $\mathbf{x}'$、垂直於 $\mathbf{l}'_e$** 的那條——離退化最遠：
$$
\mathbf{l}'=\left(l_2,\ -l_1,\ -x_1l_2+x_2l_1\right)^\mathsf{T}
$$
- 講者留作練習：驗證它垂直於 $\mathbf{l}'_e$ 並通過 $\mathbf{x}'$。

（$\mathbf{l}'$ 的式子依 MVG §15.3.2 寫出；逐字稿只說「由這個式子給出」。）

> 以下**不是逐字稿內容**，是驗證：(1) 通過 $\mathbf{x}'$：$(x_1,x_2,1)\cdot\mathbf{l}'=x_1l_2-x_2l_1-x_1l_2+x_2l_1=0$ ✓。(2) 垂直：線的法向量是前兩個分量，$(l_2,-l_1)\cdot(l_1,l_2)=0$ ✓。

【課本補充】MVG §15.3.2 建議的完整流程：先用 $F_{21}$ 把 $\mathbf{x}\leftrightarrow\mathbf{x}'$ 修正成完全滿足極線約束的 $\hat{\mathbf{x}}\leftrightarrow\hat{\mathbf{x}}'$（最佳三角化），再用垂直於 $F_{21}\hat{\mathbf{x}}$ 的線轉移。修正過的點，轉移結果和 $\mathbf{l}'$ 的選擇無關（只要不是極線）。用 tensor 唯一的退化是 3D 點在第一、二台相機的**基線**上。

---

## 2. 線性估計 trifocal tensor

### 2.1 At = 0 與每種對應的方程式數

[▶ 09:22](https://youtu.be/rysdVwyM9FQ?t=562)

- 所有關聯關係都**對 tensor 的元素線性**。把 tensor 排成 27 維向量 $\mathbf{t}$：
$$
A\mathbf{t}=\mathbf{0}
$$
- 27 個未知數差縮放 → 需要 **26 條以上**方程式。
- 最小平方：$\min\|A\mathbf{t}\|$ s.t. $\|\mathbf{t}\|=1$，用 SVD。

⚠️ 逐字稿缺字 [▶ 09:55](https://youtu.be/rysdVwyM9FQ?t=595)：Whisper 寫「37 by one vector」，應為 **27**。

**每種對應的獨立方程式數** [▶ 10:44](https://youtu.be/rysdVwyM9FQ?t=644)（MVG Table 16.1）：

| 對應 | 關係 | 獨立方程式 |
|---|---|---|
| 三點 | $x^ix'^jx''^k\epsilon_{jqs}\epsilon_{krt}\mathcal{T}_i^{qr}=0_{st}$ | 4 |
| 兩點一線 | $x^ix'^jl''_r\epsilon_{jqs}\mathcal{T}_i^{qr}=0_s$ | 2 |
| 一點兩線 | $x^il'_ql''_r\mathcal{T}_i^{qr}=0$ | 1 |
| 三線 | $l_pl'_ql''_r\epsilon^{piw}\mathcal{T}_i^{qr}=0^w$ | 2 |

**為什麼三點只有 4 條** [▶ 11:31](https://youtu.be/rysdVwyM9FQ?t=691)：

- $0_{st}$ 原本 $s,t\in\{1,2,3\}$ → 9 條。
- 但只有 **4 條線性獨立**——講者說源自 tensor 的 rank 缺陷（每個 $T_i$ rank 2），證明複雜，本課不講。
- 實作時只取 $s,t\in\{1,2\}$ 的 4 個組合。

> 以下**不是逐字稿內容**，是另一個直覺：點–點–點關係是 $[\mathbf{x}']_\times M[\mathbf{x}'']_\times=0$。$[\mathbf{x}']_\times$、$[\mathbf{x}'']_\times$ 都是 rank 2，所以這個 $3\times3$ 等式實際上只約束 $2\times2=4$ 個自由的組合。

### 2.2 正規化線性演算法

[▶ 12:42](https://youtu.be/rysdVwyM9FQ?t=762)

**正規化**（和 homography、$F$ 一樣，**必要**）：

- 每張圖各自做：平移讓點的重心到原點、縮放讓 RMS 距離為 $\sqrt{2}$。
- **線**的正規化 [▶ 14:29](https://youtu.be/rysdVwyM9FQ?t=869)：用線的**端點**來算重心和尺度，把變換套到端點上，再用變換後的端點定義新的線。

**需要幾組對應** [▶ 15:30](https://youtu.be/rysdVwyM9FQ?t=930)：至少 26 條方程式。

- 只用點：每點 4 條 → **7 點**（$7\times4=28\ge26$）。
- 只用線：每線 2 條 → **13 線**（$13\times2=26$）。
- 混合時照上表算。

**步驟**（MVG Algorithm 16.1）：

1. 三張圖各自正規化（$H,H',H''$）。
2. 用正規化的對應組 $A\mathbf{t}=0$，SVD 求 $\hat{\mathbf{t}}$。
3. 反正規化得原座標下的 tensor。

【課本補充】MVG §16.1.2：理論上 6 點就夠（非線性的最小解，有 1 或 3 組實解），但線性方法需要 7 點。

---

## 3. 強制極點約束：代數最小化

[▶ 17:54](https://youtu.be/rysdVwyM9FQ?t=1074)

**問題**（類比 $F$ 要強制 rank 2）：

- 線性解出的 tensor 因雜訊**不滿足**內部約束（每個 $T_i$ rank 2 等）。
- 後果：從它取出的極點**不唯一**——三條極線不交於一點。

【課本補充】MVG §16.1.1：tensor 有 27 個元素但只有 18 個自由度，元素間要滿足 8 個獨立的代數約束，才叫「幾何上合法（geometrically valid）」。

**做法**（MVG Algorithm 16.2）[▶ 19:54](https://youtu.be/rysdVwyM9FQ?t=1194)：

1. **初始 tensor**：正規化線性演算法得 $[T_1,T_2,T_3]$。
2. **極線**：有雜訊時 $T_i\mathbf{v}_i\neq0$，改成最小化
$$
\min_{\mathbf{v}_i}\|T_i\mathbf{v}_i\|\quad\text{s.t.}\quad\|\mathbf{v}_i\|=1
$$
   （SVD）。$\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$ 是 $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ 在第三張圖的極線。
3. **極點**：三條極線不一定交於一點，最小化
$$
\min_{\mathbf{e}''}\left\|\mathbf{e}''^\mathsf{T}[\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3]\right\|\quad\text{s.t.}\quad\|\mathbf{e}''\|=1
$$
   $\mathbf{e}'$ 同理（用左零向量）。
4. **用極點參數化 tensor** [▶ 23:39](https://youtu.be/rysdVwyM9FQ?t=1419)：
   - $P'=[A\mid\mathbf{e}']$、$P''=[B\mid\mathbf{e}'']$（$\mathbf{a}_4=\mathbf{e}'$、$\mathbf{b}_4=\mathbf{e}''$ 已知）。
   - $T_i=\mathbf{a}_i\mathbf{e}''^\mathsf{T}-\mathbf{e}'\mathbf{b}_i^\mathsf{T}$ 對 $A,B$ 的元素**線性**。
   - 寫成 $\mathbf{t}=E\mathbf{a}$：$E$ 由已知極點組成，$\mathbf{a}$ 是 $A$、$B$ 的 18 個未知元素。
5. **代數最小化**：
$$
\min_\mathbf{a}\|AE\mathbf{a}\|\quad\text{s.t.}\quad\|E\mathbf{a}\|=1
$$
   （等於「$\min\|A\mathbf{t}\|$ s.t. $\|\mathbf{t}\|=1$」，但 $\mathbf{t}$ 被限制成 $E\mathbf{a}$ 的形式。）
6. 解出的 $\mathbf{t}=E\mathbf{a}$ **自動滿足極點約束**——因為它是由已知極點組出來的，是一個合法的 tensor。

（$\mathbf{a}$ 有 18 個元素、$\|E\mathbf{a}\|=1$ 的約束依 MVG Algorithm 16.2 寫出；逐字稿只說「$\mathbf{a}$ 包含 $A$ 和 $B$ 剩下的未知元素」。）

【課本補充】MVG Algorithm 16.2：極點本身也可以再用 Levenberg–Marquardt 迭代調整，讓代數誤差更小（對 6 個極點參數做迭代、每步解一次上面的線性問題）。

---

## 4. 幾何誤差：Gold Standard

[▶ 27:32](https://youtu.be/rysdVwyM9FQ?t=1652)

用代數解當**初值**，再最小化幾何誤差（和 homography、$F$ 一樣）：

1. 從初始 tensor 取出 $P=[I\mid\mathbf{0}]$、$P'$、$P''$（第 25 集）。
2. 用三張圖的對應點和三個相機，**線性三角化**（第 19 集）得 3D 點 $\hat{\mathbf{X}}_i$。
3. 雜訊讓三條光線不剛好交於一點；三角化的點重投影回去，不會剛好落在觀測點上：
$$
\min_{P',P'',\{\hat{\mathbf{X}}_i\}}\ \sum_i\left[d(\mathbf{x}_i,\hat{\mathbf{x}}_i)^2+d(\mathbf{x}_i',\hat{\mathbf{x}}_i')^2+d(\mathbf{x}_i'',\hat{\mathbf{x}}_i'')^2\right]
$$
   $\hat{\mathbf{x}}_i=P\hat{\mathbf{X}}_i$ 等是重投影點。
4. 變數：$n$ 個 3D 點各 3 個 + $P'$、$P''$ 共 24 個 = $3n+24$。$P=[I\mid\mathbf{0}]$ 固定不必最佳化。
5. 這等於**三視角的 bundle adjustment**——下一講細講。

⚠️ 逐字稿缺字 [▶ 30:23](https://youtu.be/rysdVwyM9FQ?t=1823)：Whisper 寫「3m by 24 variable」，應為 $3n+24$ 個變數。

---

## 5. Lecture 9 總結

[▶ 30:52](https://youtu.be/rysdVwyM9FQ?t=1852)

1. 用點／線對應推導三視角的 trifocal tensor 約束（第 23–24 集）。
2. 從 trifocal tensor 得到的 homography 關係（第 24 集）。
3. 從 tensor 取出第二、三張圖的極點和極線（第 24–25 集）。
4. 把 tensor 分解成三視角的相機矩陣和 fundamental matrix（第 25 集）。
5. 用代數和幾何方法，從點／線對應計算 trifocal tensor（本集）。

---

## 6. 一頁速查表

### 點轉移

| 方法 | 公式 | 退化 |
|---|---|---|
| fundamental matrix | $\mathbf{x}''=(F_{31}\mathbf{x})\times(F_{32}\mathbf{x}')$ | 3D 點在三焦平面上（兩極線重合） |
| trifocal tensor | $x''^k=x^il'_j\mathcal{T}_i^{jk}$，$\mathbf{l}'$ 通過 $\mathbf{x}'$ | $\mathbf{l}'$ 是極線時為 0；改用 $\mathbf{l}'=(l_2,-l_1,-x_1l_2+x_2l_1)^\mathsf{T}$ |

### 估計 tensor

| 步驟 | 內容 |
|---|---|
| 線性 | $A\mathbf{t}=0$（27 維），$\ge26$ 條方程式；點 4 條、線 2 條、點線線 1 條、點點線 2 條 → 7 點或 13 線 |
| 正規化 | 每張圖重心到原點、RMS $\sqrt{2}$；線用端點 |
| 極點 | $\min\|T_i\mathbf{v}_i\|$ → 極線；$\min\|\mathbf{e}''^\mathsf{T}[\mathbf{v}_i]\|$ → 極點 |
| 代數最小化 | $\mathbf{t}=E\mathbf{a}$，$\min\|AE\mathbf{a}\|$ s.t. $\|E\mathbf{a}\|=1$——自動合法 |
| Gold Standard | 三角化後最小化三張圖的重投影誤差，$3n+24$ 變數（三視角 BA） |

---

## 7. 與後續集數的連結

| 本集觀念 | 後面在哪裡用到 |
|---|---|
| 最小化重投影誤差、$3n+24$ 變數 | 第 27–30 集（bundle adjustment：任意多視角） |
| 代數初值 → 幾何精修 | 第 27–30 集（SfM 的初始化 + BA） |
| 點轉移 | 第 31–34 集（多視角 stereo 的一致性檢查） |

---

## 附：本集一句話總結

> **用兩個 $F$ 的極線交點做點轉移，在三焦平面上會退化；改用 tensor 的 $x''^k=x^il'_j\mathcal{T}_i^{jk}$，只要選通過 $\mathbf{x}'$ 且垂直於極線的 $\mathbf{l}'$ 就不會壞。估計 tensor 時把所有點線關係疊成 $A\mathbf{t}=0$（三點 4 條、三線 2 條，至少 7 點或 13 線），先正規化、SVD 得初值，再取出極點、把 tensor 參數化成 $E\mathbf{a}$ 強制合法，最後用重投影誤差做三視角的 bundle adjustment。**

---

*筆記依據 Gim Hee Lee「3D Computer Vision」Lecture 9 (Part 4) 錄影逐字稿（Whisper `medium.en`，31:50）與 Hartley & Zisserman《Multiple View Geometry in Computer Vision》第 2 版 §15.3、§16.1–16.4 整理。*
